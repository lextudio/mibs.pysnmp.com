# SNMP MIB module (CISCO-UNIFIED-COMPUTING-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:58 2024
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
 CucsConditionSeverity,
 CucsEtherSatelliteConnectionDisc,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsIpProtocol,
 CucsMgmtAccess,
 CucsMgmtAdminState,
 CucsMgmtBackupFsmCurrentFsm,
 CucsMgmtBackupFsmStageName,
 CucsMgmtBackupFsmTaskItem,
 CucsMgmtBackupInterval,
 CucsMgmtBackupIssue,
 CucsMgmtBackupJob,
 CucsMgmtBackupJobStatus,
 CucsMgmtBackupPolicyFsmCurrentFsm,
 CucsMgmtBackupPolicyFsmStageName,
 CucsMgmtBackupPostAction,
 CucsMgmtBackupProto,
 CucsMgmtBackupType,
 CucsMgmtCapability,
 CucsMgmtCfgExportPolicyFsmCurrentFsm,
 CucsMgmtCfgExportPolicyFsmStageName,
 CucsMgmtCimcSecureBootAdminState,
 CucsMgmtConfigState,
 CucsMgmtConnectionState,
 CucsMgmtControllerFsmCurrentFsm,
 CucsMgmtControllerFsmStageName,
 CucsMgmtControllerFsmTaskFlags,
 CucsMgmtControllerFsmTaskItem,
 CucsMgmtDimmBlacklistingOperState,
 CucsMgmtEntityChassisDeviceIoState1,
 CucsMgmtEntityChassisDeviceIoState2,
 CucsMgmtEntityChassisDeviceIoState3,
 CucsMgmtEntityHaFailureReason,
 CucsMgmtEntityHaReadiness,
 CucsMgmtEntityLeadership,
 CucsMgmtEntityMgmtServicesState,
 CucsMgmtEntityProblems,
 CucsMgmtEntityState,
 CucsMgmtEntityUmbilicalState,
 CucsMgmtExportPolicyAdminState,
 CucsMgmtExportPolicyFsmCurrentFsm,
 CucsMgmtExportPolicyFsmStageName,
 CucsMgmtExportPolicyFsmTaskItem,
 CucsMgmtExportPolicyProto,
 CucsMgmtIPv6IfAddrFsmCurrentFsm,
 CucsMgmtIPv6IfAddrFsmStageName,
 CucsMgmtIPv6IfAddrFsmTaskItem,
 CucsMgmtIfFsmCurrentFsm,
 CucsMgmtIfFsmStageName,
 CucsMgmtIfFsmTaskItem,
 CucsMgmtImportAction,
 CucsMgmtImportStatus,
 CucsMgmtImporterFsmCurrentFsm,
 CucsMgmtImporterFsmStageName,
 CucsMgmtImporterFsmTaskItem,
 CucsMgmtImporterPostAction,
 CucsMgmtImporterProto,
 CucsMgmtIntAuthPolicyMethod,
 CucsMgmtMaintMode,
 CucsMgmtMode,
 CucsMgmtOperState,
 CucsMgmtPmonEntryState,
 CucsMgmtSecureBootOperState,
 CucsMgmtSource,
 CucsMgmtStateQual,
 CucsMgmtStorageSubsystemState,
 CucsMgmtSubject,
 CucsNetworkConnectionType,
 CucsNetworkLocale,
 CucsNetworkPhysEpIfType,
 CucsNetworkPortRole,
 CucsNetworkSwitchId,
 CucsNetworkTransport,
 CucsPolicyPolicyOwner,
 CucsTrigAdminState,
 CucsTrigTrigOperState,
 CucsVnicExternalMgmtIPMode) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsCommClientAdminState",
    "CucsConditionRemoteInvRslt",
    "CucsConditionSeverity",
    "CucsEtherSatelliteConnectionDisc",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsIpProtocol",
    "CucsMgmtAccess",
    "CucsMgmtAdminState",
    "CucsMgmtBackupFsmCurrentFsm",
    "CucsMgmtBackupFsmStageName",
    "CucsMgmtBackupFsmTaskItem",
    "CucsMgmtBackupInterval",
    "CucsMgmtBackupIssue",
    "CucsMgmtBackupJob",
    "CucsMgmtBackupJobStatus",
    "CucsMgmtBackupPolicyFsmCurrentFsm",
    "CucsMgmtBackupPolicyFsmStageName",
    "CucsMgmtBackupPostAction",
    "CucsMgmtBackupProto",
    "CucsMgmtBackupType",
    "CucsMgmtCapability",
    "CucsMgmtCfgExportPolicyFsmCurrentFsm",
    "CucsMgmtCfgExportPolicyFsmStageName",
    "CucsMgmtCimcSecureBootAdminState",
    "CucsMgmtConfigState",
    "CucsMgmtConnectionState",
    "CucsMgmtControllerFsmCurrentFsm",
    "CucsMgmtControllerFsmStageName",
    "CucsMgmtControllerFsmTaskFlags",
    "CucsMgmtControllerFsmTaskItem",
    "CucsMgmtDimmBlacklistingOperState",
    "CucsMgmtEntityChassisDeviceIoState1",
    "CucsMgmtEntityChassisDeviceIoState2",
    "CucsMgmtEntityChassisDeviceIoState3",
    "CucsMgmtEntityHaFailureReason",
    "CucsMgmtEntityHaReadiness",
    "CucsMgmtEntityLeadership",
    "CucsMgmtEntityMgmtServicesState",
    "CucsMgmtEntityProblems",
    "CucsMgmtEntityState",
    "CucsMgmtEntityUmbilicalState",
    "CucsMgmtExportPolicyAdminState",
    "CucsMgmtExportPolicyFsmCurrentFsm",
    "CucsMgmtExportPolicyFsmStageName",
    "CucsMgmtExportPolicyFsmTaskItem",
    "CucsMgmtExportPolicyProto",
    "CucsMgmtIPv6IfAddrFsmCurrentFsm",
    "CucsMgmtIPv6IfAddrFsmStageName",
    "CucsMgmtIPv6IfAddrFsmTaskItem",
    "CucsMgmtIfFsmCurrentFsm",
    "CucsMgmtIfFsmStageName",
    "CucsMgmtIfFsmTaskItem",
    "CucsMgmtImportAction",
    "CucsMgmtImportStatus",
    "CucsMgmtImporterFsmCurrentFsm",
    "CucsMgmtImporterFsmStageName",
    "CucsMgmtImporterFsmTaskItem",
    "CucsMgmtImporterPostAction",
    "CucsMgmtImporterProto",
    "CucsMgmtIntAuthPolicyMethod",
    "CucsMgmtMaintMode",
    "CucsMgmtMode",
    "CucsMgmtOperState",
    "CucsMgmtPmonEntryState",
    "CucsMgmtSecureBootOperState",
    "CucsMgmtSource",
    "CucsMgmtStateQual",
    "CucsMgmtStorageSubsystemState",
    "CucsMgmtSubject",
    "CucsNetworkConnectionType",
    "CucsNetworkLocale",
    "CucsNetworkPhysEpIfType",
    "CucsNetworkPortRole",
    "CucsNetworkSwitchId",
    "CucsNetworkTransport",
    "CucsPolicyPolicyOwner",
    "CucsTrigAdminState",
    "CucsTrigTrigOperState",
    "CucsVnicExternalMgmtIPMode")

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

cucsMgmtObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsMgmtAccessPolicyTable_Object = MibTable
cucsMgmtAccessPolicyTable = _CucsMgmtAccessPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 1)
)
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyTable.setStatus("current")
_CucsMgmtAccessPolicyEntry_Object = MibTableRow
cucsMgmtAccessPolicyEntry = _CucsMgmtAccessPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 1, 1)
)
cucsMgmtAccessPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtAccessPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyEntry.setStatus("current")
_CucsMgmtAccessPolicyInstanceId_Type = CucsManagedObjectId
_CucsMgmtAccessPolicyInstanceId_Object = MibTableColumn
cucsMgmtAccessPolicyInstanceId = _CucsMgmtAccessPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 1, 1, 1),
    _CucsMgmtAccessPolicyInstanceId_Type()
)
cucsMgmtAccessPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyInstanceId.setStatus("current")
_CucsMgmtAccessPolicyDn_Type = CucsManagedObjectDn
_CucsMgmtAccessPolicyDn_Object = MibTableColumn
cucsMgmtAccessPolicyDn = _CucsMgmtAccessPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 1, 1, 2),
    _CucsMgmtAccessPolicyDn_Type()
)
cucsMgmtAccessPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyDn.setStatus("current")
_CucsMgmtAccessPolicyRn_Type = SnmpAdminString
_CucsMgmtAccessPolicyRn_Object = MibTableColumn
cucsMgmtAccessPolicyRn = _CucsMgmtAccessPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 1, 1, 3),
    _CucsMgmtAccessPolicyRn_Type()
)
cucsMgmtAccessPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyRn.setStatus("current")
_CucsMgmtAccessPolicyItemTable_Object = MibTable
cucsMgmtAccessPolicyItemTable = _CucsMgmtAccessPolicyItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 2)
)
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyItemTable.setStatus("current")
_CucsMgmtAccessPolicyItemEntry_Object = MibTableRow
cucsMgmtAccessPolicyItemEntry = _CucsMgmtAccessPolicyItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 2, 1)
)
cucsMgmtAccessPolicyItemEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtAccessPolicyItemInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyItemEntry.setStatus("current")
_CucsMgmtAccessPolicyItemInstanceId_Type = CucsManagedObjectId
_CucsMgmtAccessPolicyItemInstanceId_Object = MibTableColumn
cucsMgmtAccessPolicyItemInstanceId = _CucsMgmtAccessPolicyItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 2, 1, 1),
    _CucsMgmtAccessPolicyItemInstanceId_Type()
)
cucsMgmtAccessPolicyItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyItemInstanceId.setStatus("current")
_CucsMgmtAccessPolicyItemDn_Type = CucsManagedObjectDn
_CucsMgmtAccessPolicyItemDn_Object = MibTableColumn
cucsMgmtAccessPolicyItemDn = _CucsMgmtAccessPolicyItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 2, 1, 2),
    _CucsMgmtAccessPolicyItemDn_Type()
)
cucsMgmtAccessPolicyItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyItemDn.setStatus("current")
_CucsMgmtAccessPolicyItemRn_Type = SnmpAdminString
_CucsMgmtAccessPolicyItemRn_Object = MibTableColumn
cucsMgmtAccessPolicyItemRn = _CucsMgmtAccessPolicyItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 2, 1, 3),
    _CucsMgmtAccessPolicyItemRn_Type()
)
cucsMgmtAccessPolicyItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyItemRn.setStatus("current")
_CucsMgmtAccessPolicyItemDescr_Type = SnmpAdminString
_CucsMgmtAccessPolicyItemDescr_Object = MibTableColumn
cucsMgmtAccessPolicyItemDescr = _CucsMgmtAccessPolicyItemDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 2, 1, 4),
    _CucsMgmtAccessPolicyItemDescr_Type()
)
cucsMgmtAccessPolicyItemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyItemDescr.setStatus("current")
_CucsMgmtAccessPolicyItemIntId_Type = SnmpAdminString
_CucsMgmtAccessPolicyItemIntId_Object = MibTableColumn
cucsMgmtAccessPolicyItemIntId = _CucsMgmtAccessPolicyItemIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 2, 1, 5),
    _CucsMgmtAccessPolicyItemIntId_Type()
)
cucsMgmtAccessPolicyItemIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyItemIntId.setStatus("current")
_CucsMgmtAccessPolicyItemIpPoolName_Type = SnmpAdminString
_CucsMgmtAccessPolicyItemIpPoolName_Object = MibTableColumn
cucsMgmtAccessPolicyItemIpPoolName = _CucsMgmtAccessPolicyItemIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 2, 1, 6),
    _CucsMgmtAccessPolicyItemIpPoolName_Type()
)
cucsMgmtAccessPolicyItemIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyItemIpPoolName.setStatus("current")
_CucsMgmtAccessPolicyItemName_Type = SnmpAdminString
_CucsMgmtAccessPolicyItemName_Object = MibTableColumn
cucsMgmtAccessPolicyItemName = _CucsMgmtAccessPolicyItemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 2, 1, 7),
    _CucsMgmtAccessPolicyItemName_Type()
)
cucsMgmtAccessPolicyItemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyItemName.setStatus("current")
_CucsMgmtAccessPolicyItemSubject_Type = CucsMgmtSubject
_CucsMgmtAccessPolicyItemSubject_Object = MibTableColumn
cucsMgmtAccessPolicyItemSubject = _CucsMgmtAccessPolicyItemSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 2, 1, 8),
    _CucsMgmtAccessPolicyItemSubject_Type()
)
cucsMgmtAccessPolicyItemSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyItemSubject.setStatus("current")
_CucsMgmtAccessPolicyItemPolicyLevel_Type = Gauge32
_CucsMgmtAccessPolicyItemPolicyLevel_Object = MibTableColumn
cucsMgmtAccessPolicyItemPolicyLevel = _CucsMgmtAccessPolicyItemPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 2, 1, 9),
    _CucsMgmtAccessPolicyItemPolicyLevel_Type()
)
cucsMgmtAccessPolicyItemPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyItemPolicyLevel.setStatus("current")
_CucsMgmtAccessPolicyItemPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsMgmtAccessPolicyItemPolicyOwner_Object = MibTableColumn
cucsMgmtAccessPolicyItemPolicyOwner = _CucsMgmtAccessPolicyItemPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 2, 1, 10),
    _CucsMgmtAccessPolicyItemPolicyOwner_Type()
)
cucsMgmtAccessPolicyItemPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPolicyItemPolicyOwner.setStatus("current")
_CucsMgmtAccessPortTable_Object = MibTable
cucsMgmtAccessPortTable = _CucsMgmtAccessPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 3)
)
if mibBuilder.loadTexts:
    cucsMgmtAccessPortTable.setStatus("current")
_CucsMgmtAccessPortEntry_Object = MibTableRow
cucsMgmtAccessPortEntry = _CucsMgmtAccessPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 3, 1)
)
cucsMgmtAccessPortEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtAccessPortInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtAccessPortEntry.setStatus("current")
_CucsMgmtAccessPortInstanceId_Type = CucsManagedObjectId
_CucsMgmtAccessPortInstanceId_Object = MibTableColumn
cucsMgmtAccessPortInstanceId = _CucsMgmtAccessPortInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 3, 1, 1),
    _CucsMgmtAccessPortInstanceId_Type()
)
cucsMgmtAccessPortInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtAccessPortInstanceId.setStatus("current")
_CucsMgmtAccessPortDn_Type = CucsManagedObjectDn
_CucsMgmtAccessPortDn_Object = MibTableColumn
cucsMgmtAccessPortDn = _CucsMgmtAccessPortDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 3, 1, 2),
    _CucsMgmtAccessPortDn_Type()
)
cucsMgmtAccessPortDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPortDn.setStatus("current")
_CucsMgmtAccessPortRn_Type = SnmpAdminString
_CucsMgmtAccessPortRn_Object = MibTableColumn
cucsMgmtAccessPortRn = _CucsMgmtAccessPortRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 3, 1, 3),
    _CucsMgmtAccessPortRn_Type()
)
cucsMgmtAccessPortRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPortRn.setStatus("current")
_CucsMgmtAccessPortPort_Type = Gauge32
_CucsMgmtAccessPortPort_Object = MibTableColumn
cucsMgmtAccessPortPort = _CucsMgmtAccessPortPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 3, 1, 4),
    _CucsMgmtAccessPortPort_Type()
)
cucsMgmtAccessPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPortPort.setStatus("current")
_CucsMgmtAccessPortProtocol_Type = CucsIpProtocol
_CucsMgmtAccessPortProtocol_Object = MibTableColumn
cucsMgmtAccessPortProtocol = _CucsMgmtAccessPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 3, 1, 5),
    _CucsMgmtAccessPortProtocol_Type()
)
cucsMgmtAccessPortProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtAccessPortProtocol.setStatus("current")
_CucsMgmtBackupTable_Object = MibTable
cucsMgmtBackupTable = _CucsMgmtBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4)
)
if mibBuilder.loadTexts:
    cucsMgmtBackupTable.setStatus("current")
_CucsMgmtBackupEntry_Object = MibTableRow
cucsMgmtBackupEntry = _CucsMgmtBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1)
)
cucsMgmtBackupEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtBackupInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtBackupEntry.setStatus("current")
_CucsMgmtBackupInstanceId_Type = CucsManagedObjectId
_CucsMgmtBackupInstanceId_Object = MibTableColumn
cucsMgmtBackupInstanceId = _CucsMgmtBackupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 1),
    _CucsMgmtBackupInstanceId_Type()
)
cucsMgmtBackupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtBackupInstanceId.setStatus("current")
_CucsMgmtBackupDn_Type = CucsManagedObjectDn
_CucsMgmtBackupDn_Object = MibTableColumn
cucsMgmtBackupDn = _CucsMgmtBackupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 2),
    _CucsMgmtBackupDn_Type()
)
cucsMgmtBackupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupDn.setStatus("current")
_CucsMgmtBackupRn_Type = SnmpAdminString
_CucsMgmtBackupRn_Object = MibTableColumn
cucsMgmtBackupRn = _CucsMgmtBackupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 3),
    _CucsMgmtBackupRn_Type()
)
cucsMgmtBackupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupRn.setStatus("current")
_CucsMgmtBackupAdminState_Type = CucsCommClientAdminState
_CucsMgmtBackupAdminState_Object = MibTableColumn
cucsMgmtBackupAdminState = _CucsMgmtBackupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 4),
    _CucsMgmtBackupAdminState_Type()
)
cucsMgmtBackupAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupAdminState.setStatus("current")
_CucsMgmtBackupDescr_Type = SnmpAdminString
_CucsMgmtBackupDescr_Object = MibTableColumn
cucsMgmtBackupDescr = _CucsMgmtBackupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 5),
    _CucsMgmtBackupDescr_Type()
)
cucsMgmtBackupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupDescr.setStatus("current")
_CucsMgmtBackupFsmDescr_Type = SnmpAdminString
_CucsMgmtBackupFsmDescr_Object = MibTableColumn
cucsMgmtBackupFsmDescr = _CucsMgmtBackupFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 6),
    _CucsMgmtBackupFsmDescr_Type()
)
cucsMgmtBackupFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmDescr.setStatus("current")
_CucsMgmtBackupFsmPrev_Type = SnmpAdminString
_CucsMgmtBackupFsmPrev_Object = MibTableColumn
cucsMgmtBackupFsmPrev = _CucsMgmtBackupFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 7),
    _CucsMgmtBackupFsmPrev_Type()
)
cucsMgmtBackupFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmPrev.setStatus("current")
_CucsMgmtBackupFsmProgr_Type = Gauge32
_CucsMgmtBackupFsmProgr_Object = MibTableColumn
cucsMgmtBackupFsmProgr = _CucsMgmtBackupFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 8),
    _CucsMgmtBackupFsmProgr_Type()
)
cucsMgmtBackupFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmProgr.setStatus("current")
_CucsMgmtBackupFsmRmtInvErrCode_Type = Gauge32
_CucsMgmtBackupFsmRmtInvErrCode_Object = MibTableColumn
cucsMgmtBackupFsmRmtInvErrCode = _CucsMgmtBackupFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 9),
    _CucsMgmtBackupFsmRmtInvErrCode_Type()
)
cucsMgmtBackupFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmRmtInvErrCode.setStatus("current")
_CucsMgmtBackupFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsMgmtBackupFsmRmtInvErrDescr_Object = MibTableColumn
cucsMgmtBackupFsmRmtInvErrDescr = _CucsMgmtBackupFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 10),
    _CucsMgmtBackupFsmRmtInvErrDescr_Type()
)
cucsMgmtBackupFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmRmtInvErrDescr.setStatus("current")
_CucsMgmtBackupFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtBackupFsmRmtInvRslt_Object = MibTableColumn
cucsMgmtBackupFsmRmtInvRslt = _CucsMgmtBackupFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 11),
    _CucsMgmtBackupFsmRmtInvRslt_Type()
)
cucsMgmtBackupFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmRmtInvRslt.setStatus("current")
_CucsMgmtBackupFsmStageDescr_Type = SnmpAdminString
_CucsMgmtBackupFsmStageDescr_Object = MibTableColumn
cucsMgmtBackupFsmStageDescr = _CucsMgmtBackupFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 12),
    _CucsMgmtBackupFsmStageDescr_Type()
)
cucsMgmtBackupFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmStageDescr.setStatus("current")
_CucsMgmtBackupFsmStamp_Type = DateAndTime
_CucsMgmtBackupFsmStamp_Object = MibTableColumn
cucsMgmtBackupFsmStamp = _CucsMgmtBackupFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 13),
    _CucsMgmtBackupFsmStamp_Type()
)
cucsMgmtBackupFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmStamp.setStatus("current")
_CucsMgmtBackupFsmStatus_Type = SnmpAdminString
_CucsMgmtBackupFsmStatus_Object = MibTableColumn
cucsMgmtBackupFsmStatus = _CucsMgmtBackupFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 14),
    _CucsMgmtBackupFsmStatus_Type()
)
cucsMgmtBackupFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmStatus.setStatus("current")
_CucsMgmtBackupFsmTry_Type = Gauge32
_CucsMgmtBackupFsmTry_Object = MibTableColumn
cucsMgmtBackupFsmTry = _CucsMgmtBackupFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 15),
    _CucsMgmtBackupFsmTry_Type()
)
cucsMgmtBackupFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmTry.setStatus("current")
_CucsMgmtBackupHostname_Type = SnmpAdminString
_CucsMgmtBackupHostname_Object = MibTableColumn
cucsMgmtBackupHostname = _CucsMgmtBackupHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 16),
    _CucsMgmtBackupHostname_Type()
)
cucsMgmtBackupHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupHostname.setStatus("current")
_CucsMgmtBackupIntId_Type = SnmpAdminString
_CucsMgmtBackupIntId_Object = MibTableColumn
cucsMgmtBackupIntId = _CucsMgmtBackupIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 17),
    _CucsMgmtBackupIntId_Type()
)
cucsMgmtBackupIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupIntId.setStatus("current")
_CucsMgmtBackupJob_Type = CucsMgmtBackupJob
_CucsMgmtBackupJob_Object = MibTableColumn
cucsMgmtBackupJob = _CucsMgmtBackupJob_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 18),
    _CucsMgmtBackupJob_Type()
)
cucsMgmtBackupJob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupJob.setStatus("current")
_CucsMgmtBackupName_Type = SnmpAdminString
_CucsMgmtBackupName_Object = MibTableColumn
cucsMgmtBackupName = _CucsMgmtBackupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 19),
    _CucsMgmtBackupName_Type()
)
cucsMgmtBackupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupName.setStatus("current")
_CucsMgmtBackupPostAction_Type = CucsMgmtBackupPostAction
_CucsMgmtBackupPostAction_Object = MibTableColumn
cucsMgmtBackupPostAction = _CucsMgmtBackupPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 20),
    _CucsMgmtBackupPostAction_Type()
)
cucsMgmtBackupPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPostAction.setStatus("current")
_CucsMgmtBackupPreservePooledValues_Type = TruthValue
_CucsMgmtBackupPreservePooledValues_Object = MibTableColumn
cucsMgmtBackupPreservePooledValues = _CucsMgmtBackupPreservePooledValues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 21),
    _CucsMgmtBackupPreservePooledValues_Type()
)
cucsMgmtBackupPreservePooledValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPreservePooledValues.setStatus("current")
_CucsMgmtBackupProto_Type = CucsMgmtBackupProto
_CucsMgmtBackupProto_Object = MibTableColumn
cucsMgmtBackupProto = _CucsMgmtBackupProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 22),
    _CucsMgmtBackupProto_Type()
)
cucsMgmtBackupProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupProto.setStatus("current")
_CucsMgmtBackupPwd_Type = SnmpAdminString
_CucsMgmtBackupPwd_Object = MibTableColumn
cucsMgmtBackupPwd = _CucsMgmtBackupPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 23),
    _CucsMgmtBackupPwd_Type()
)
cucsMgmtBackupPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPwd.setStatus("current")
_CucsMgmtBackupRemoteFile_Type = SnmpAdminString
_CucsMgmtBackupRemoteFile_Object = MibTableColumn
cucsMgmtBackupRemoteFile = _CucsMgmtBackupRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 24),
    _CucsMgmtBackupRemoteFile_Type()
)
cucsMgmtBackupRemoteFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupRemoteFile.setStatus("current")
_CucsMgmtBackupType_Type = CucsMgmtBackupType
_CucsMgmtBackupType_Object = MibTableColumn
cucsMgmtBackupType = _CucsMgmtBackupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 25),
    _CucsMgmtBackupType_Type()
)
cucsMgmtBackupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupType.setStatus("current")
_CucsMgmtBackupUser_Type = SnmpAdminString
_CucsMgmtBackupUser_Object = MibTableColumn
cucsMgmtBackupUser = _CucsMgmtBackupUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 26),
    _CucsMgmtBackupUser_Type()
)
cucsMgmtBackupUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupUser.setStatus("current")
_CucsMgmtBackupMaxFiles_Type = Gauge32
_CucsMgmtBackupMaxFiles_Object = MibTableColumn
cucsMgmtBackupMaxFiles = _CucsMgmtBackupMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 27),
    _CucsMgmtBackupMaxFiles_Type()
)
cucsMgmtBackupMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupMaxFiles.setStatus("current")
_CucsMgmtBackupOwnerPolicy_Type = SnmpAdminString
_CucsMgmtBackupOwnerPolicy_Object = MibTableColumn
cucsMgmtBackupOwnerPolicy = _CucsMgmtBackupOwnerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 28),
    _CucsMgmtBackupOwnerPolicy_Type()
)
cucsMgmtBackupOwnerPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupOwnerPolicy.setStatus("current")
_CucsMgmtBackupPolicyLevel_Type = Gauge32
_CucsMgmtBackupPolicyLevel_Object = MibTableColumn
cucsMgmtBackupPolicyLevel = _CucsMgmtBackupPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 29),
    _CucsMgmtBackupPolicyLevel_Type()
)
cucsMgmtBackupPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyLevel.setStatus("current")
_CucsMgmtBackupPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsMgmtBackupPolicyOwner_Object = MibTableColumn
cucsMgmtBackupPolicyOwner = _CucsMgmtBackupPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 30),
    _CucsMgmtBackupPolicyOwner_Type()
)
cucsMgmtBackupPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyOwner.setStatus("current")
_CucsMgmtBackupBackupstatus_Type = CucsMgmtBackupJobStatus
_CucsMgmtBackupBackupstatus_Object = MibTableColumn
cucsMgmtBackupBackupstatus = _CucsMgmtBackupBackupstatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 4, 1, 31),
    _CucsMgmtBackupBackupstatus_Type()
)
cucsMgmtBackupBackupstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupBackupstatus.setStatus("current")
_CucsMgmtBackupFsmTaskTable_Object = MibTable
cucsMgmtBackupFsmTaskTable = _CucsMgmtBackupFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 5)
)
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmTaskTable.setStatus("current")
_CucsMgmtBackupFsmTaskEntry_Object = MibTableRow
cucsMgmtBackupFsmTaskEntry = _CucsMgmtBackupFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 5, 1)
)
cucsMgmtBackupFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtBackupFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmTaskEntry.setStatus("current")
_CucsMgmtBackupFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsMgmtBackupFsmTaskInstanceId_Object = MibTableColumn
cucsMgmtBackupFsmTaskInstanceId = _CucsMgmtBackupFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 5, 1, 1),
    _CucsMgmtBackupFsmTaskInstanceId_Type()
)
cucsMgmtBackupFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmTaskInstanceId.setStatus("current")
_CucsMgmtBackupFsmTaskDn_Type = CucsManagedObjectDn
_CucsMgmtBackupFsmTaskDn_Object = MibTableColumn
cucsMgmtBackupFsmTaskDn = _CucsMgmtBackupFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 5, 1, 2),
    _CucsMgmtBackupFsmTaskDn_Type()
)
cucsMgmtBackupFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmTaskDn.setStatus("current")
_CucsMgmtBackupFsmTaskRn_Type = SnmpAdminString
_CucsMgmtBackupFsmTaskRn_Object = MibTableColumn
cucsMgmtBackupFsmTaskRn = _CucsMgmtBackupFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 5, 1, 3),
    _CucsMgmtBackupFsmTaskRn_Type()
)
cucsMgmtBackupFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmTaskRn.setStatus("current")
_CucsMgmtBackupFsmTaskCompletion_Type = CucsFsmCompletion
_CucsMgmtBackupFsmTaskCompletion_Object = MibTableColumn
cucsMgmtBackupFsmTaskCompletion = _CucsMgmtBackupFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 5, 1, 4),
    _CucsMgmtBackupFsmTaskCompletion_Type()
)
cucsMgmtBackupFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmTaskCompletion.setStatus("current")
_CucsMgmtBackupFsmTaskFlags_Type = CucsFsmFlags
_CucsMgmtBackupFsmTaskFlags_Object = MibTableColumn
cucsMgmtBackupFsmTaskFlags = _CucsMgmtBackupFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 5, 1, 5),
    _CucsMgmtBackupFsmTaskFlags_Type()
)
cucsMgmtBackupFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmTaskFlags.setStatus("current")
_CucsMgmtBackupFsmTaskItem_Type = CucsMgmtBackupFsmTaskItem
_CucsMgmtBackupFsmTaskItem_Object = MibTableColumn
cucsMgmtBackupFsmTaskItem = _CucsMgmtBackupFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 5, 1, 6),
    _CucsMgmtBackupFsmTaskItem_Type()
)
cucsMgmtBackupFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmTaskItem.setStatus("current")
_CucsMgmtBackupFsmTaskSeqId_Type = Gauge32
_CucsMgmtBackupFsmTaskSeqId_Object = MibTableColumn
cucsMgmtBackupFsmTaskSeqId = _CucsMgmtBackupFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 5, 1, 7),
    _CucsMgmtBackupFsmTaskSeqId_Type()
)
cucsMgmtBackupFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmTaskSeqId.setStatus("current")
_CucsMgmtControllerTable_Object = MibTable
cucsMgmtControllerTable = _CucsMgmtControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6)
)
if mibBuilder.loadTexts:
    cucsMgmtControllerTable.setStatus("current")
_CucsMgmtControllerEntry_Object = MibTableRow
cucsMgmtControllerEntry = _CucsMgmtControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1)
)
cucsMgmtControllerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtControllerEntry.setStatus("current")
_CucsMgmtControllerInstanceId_Type = CucsManagedObjectId
_CucsMgmtControllerInstanceId_Object = MibTableColumn
cucsMgmtControllerInstanceId = _CucsMgmtControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 1),
    _CucsMgmtControllerInstanceId_Type()
)
cucsMgmtControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtControllerInstanceId.setStatus("current")
_CucsMgmtControllerDn_Type = CucsManagedObjectDn
_CucsMgmtControllerDn_Object = MibTableColumn
cucsMgmtControllerDn = _CucsMgmtControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 2),
    _CucsMgmtControllerDn_Type()
)
cucsMgmtControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerDn.setStatus("current")
_CucsMgmtControllerRn_Type = SnmpAdminString
_CucsMgmtControllerRn_Object = MibTableColumn
cucsMgmtControllerRn = _CucsMgmtControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 3),
    _CucsMgmtControllerRn_Type()
)
cucsMgmtControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerRn.setStatus("current")
_CucsMgmtControllerFsmDescr_Type = SnmpAdminString
_CucsMgmtControllerFsmDescr_Object = MibTableColumn
cucsMgmtControllerFsmDescr = _CucsMgmtControllerFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 4),
    _CucsMgmtControllerFsmDescr_Type()
)
cucsMgmtControllerFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmDescr.setStatus("current")
_CucsMgmtControllerFsmFlags_Type = SnmpAdminString
_CucsMgmtControllerFsmFlags_Object = MibTableColumn
cucsMgmtControllerFsmFlags = _CucsMgmtControllerFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 5),
    _CucsMgmtControllerFsmFlags_Type()
)
cucsMgmtControllerFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmFlags.setStatus("current")
_CucsMgmtControllerFsmPrev_Type = SnmpAdminString
_CucsMgmtControllerFsmPrev_Object = MibTableColumn
cucsMgmtControllerFsmPrev = _CucsMgmtControllerFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 6),
    _CucsMgmtControllerFsmPrev_Type()
)
cucsMgmtControllerFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmPrev.setStatus("current")
_CucsMgmtControllerFsmProgr_Type = Gauge32
_CucsMgmtControllerFsmProgr_Object = MibTableColumn
cucsMgmtControllerFsmProgr = _CucsMgmtControllerFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 7),
    _CucsMgmtControllerFsmProgr_Type()
)
cucsMgmtControllerFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmProgr.setStatus("current")
_CucsMgmtControllerFsmRmtInvErrCode_Type = Gauge32
_CucsMgmtControllerFsmRmtInvErrCode_Object = MibTableColumn
cucsMgmtControllerFsmRmtInvErrCode = _CucsMgmtControllerFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 8),
    _CucsMgmtControllerFsmRmtInvErrCode_Type()
)
cucsMgmtControllerFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmRmtInvErrCode.setStatus("current")
_CucsMgmtControllerFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsMgmtControllerFsmRmtInvErrDescr_Object = MibTableColumn
cucsMgmtControllerFsmRmtInvErrDescr = _CucsMgmtControllerFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 9),
    _CucsMgmtControllerFsmRmtInvErrDescr_Type()
)
cucsMgmtControllerFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmRmtInvErrDescr.setStatus("current")
_CucsMgmtControllerFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtControllerFsmRmtInvRslt_Object = MibTableColumn
cucsMgmtControllerFsmRmtInvRslt = _CucsMgmtControllerFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 10),
    _CucsMgmtControllerFsmRmtInvRslt_Type()
)
cucsMgmtControllerFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmRmtInvRslt.setStatus("current")
_CucsMgmtControllerFsmStageDescr_Type = SnmpAdminString
_CucsMgmtControllerFsmStageDescr_Object = MibTableColumn
cucsMgmtControllerFsmStageDescr = _CucsMgmtControllerFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 11),
    _CucsMgmtControllerFsmStageDescr_Type()
)
cucsMgmtControllerFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmStageDescr.setStatus("current")
_CucsMgmtControllerFsmStamp_Type = DateAndTime
_CucsMgmtControllerFsmStamp_Object = MibTableColumn
cucsMgmtControllerFsmStamp = _CucsMgmtControllerFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 12),
    _CucsMgmtControllerFsmStamp_Type()
)
cucsMgmtControllerFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmStamp.setStatus("current")
_CucsMgmtControllerFsmStatus_Type = SnmpAdminString
_CucsMgmtControllerFsmStatus_Object = MibTableColumn
cucsMgmtControllerFsmStatus = _CucsMgmtControllerFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 13),
    _CucsMgmtControllerFsmStatus_Type()
)
cucsMgmtControllerFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmStatus.setStatus("current")
_CucsMgmtControllerFsmTry_Type = Gauge32
_CucsMgmtControllerFsmTry_Object = MibTableColumn
cucsMgmtControllerFsmTry = _CucsMgmtControllerFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 14),
    _CucsMgmtControllerFsmTry_Type()
)
cucsMgmtControllerFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmTry.setStatus("current")
_CucsMgmtControllerGuid_Type = SnmpAdminString
_CucsMgmtControllerGuid_Object = MibTableColumn
cucsMgmtControllerGuid = _CucsMgmtControllerGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 15),
    _CucsMgmtControllerGuid_Type()
)
cucsMgmtControllerGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerGuid.setStatus("current")
_CucsMgmtControllerModel_Type = SnmpAdminString
_CucsMgmtControllerModel_Object = MibTableColumn
cucsMgmtControllerModel = _CucsMgmtControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 16),
    _CucsMgmtControllerModel_Type()
)
cucsMgmtControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerModel.setStatus("current")
_CucsMgmtControllerRevision_Type = SnmpAdminString
_CucsMgmtControllerRevision_Object = MibTableColumn
cucsMgmtControllerRevision = _CucsMgmtControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 17),
    _CucsMgmtControllerRevision_Type()
)
cucsMgmtControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerRevision.setStatus("current")
_CucsMgmtControllerSerial_Type = SnmpAdminString
_CucsMgmtControllerSerial_Object = MibTableColumn
cucsMgmtControllerSerial = _CucsMgmtControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 18),
    _CucsMgmtControllerSerial_Type()
)
cucsMgmtControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerSerial.setStatus("current")
_CucsMgmtControllerSubject_Type = CucsMgmtSubject
_CucsMgmtControllerSubject_Object = MibTableColumn
cucsMgmtControllerSubject = _CucsMgmtControllerSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 19),
    _CucsMgmtControllerSubject_Type()
)
cucsMgmtControllerSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerSubject.setStatus("current")
_CucsMgmtControllerVendor_Type = SnmpAdminString
_CucsMgmtControllerVendor_Object = MibTableColumn
cucsMgmtControllerVendor = _CucsMgmtControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 20),
    _CucsMgmtControllerVendor_Type()
)
cucsMgmtControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerVendor.setStatus("current")
_CucsMgmtControllerOperConn_Type = SnmpAdminString
_CucsMgmtControllerOperConn_Object = MibTableColumn
cucsMgmtControllerOperConn = _CucsMgmtControllerOperConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 21),
    _CucsMgmtControllerOperConn_Type()
)
cucsMgmtControllerOperConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerOperConn.setStatus("current")
_CucsMgmtControllerDimmBlacklistingOperState_Type = CucsMgmtDimmBlacklistingOperState
_CucsMgmtControllerDimmBlacklistingOperState_Object = MibTableColumn
cucsMgmtControllerDimmBlacklistingOperState = _CucsMgmtControllerDimmBlacklistingOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 22),
    _CucsMgmtControllerDimmBlacklistingOperState_Type()
)
cucsMgmtControllerDimmBlacklistingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerDimmBlacklistingOperState.setStatus("current")
_CucsMgmtControllerStorageOobInterfaceSupported_Type = TruthValue
_CucsMgmtControllerStorageOobInterfaceSupported_Object = MibTableColumn
cucsMgmtControllerStorageOobInterfaceSupported = _CucsMgmtControllerStorageOobInterfaceSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 23),
    _CucsMgmtControllerStorageOobInterfaceSupported_Type()
)
cucsMgmtControllerStorageOobInterfaceSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerStorageOobInterfaceSupported.setStatus("current")
_CucsMgmtControllerStorageSubsystemState_Type = CucsMgmtStorageSubsystemState
_CucsMgmtControllerStorageSubsystemState_Object = MibTableColumn
cucsMgmtControllerStorageSubsystemState = _CucsMgmtControllerStorageSubsystemState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 24),
    _CucsMgmtControllerStorageSubsystemState_Type()
)
cucsMgmtControllerStorageSubsystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerStorageSubsystemState.setStatus("current")
_CucsMgmtControllerStorageOobConfigSupported_Type = TruthValue
_CucsMgmtControllerStorageOobConfigSupported_Object = MibTableColumn
cucsMgmtControllerStorageOobConfigSupported = _CucsMgmtControllerStorageOobConfigSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 25),
    _CucsMgmtControllerStorageOobConfigSupported_Type()
)
cucsMgmtControllerStorageOobConfigSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerStorageOobConfigSupported.setStatus("current")
_CucsMgmtControllerId_Type = CucsNetworkSwitchId
_CucsMgmtControllerId_Object = MibTableColumn
cucsMgmtControllerId = _CucsMgmtControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 26),
    _CucsMgmtControllerId_Type()
)
cucsMgmtControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerId.setStatus("current")
_CucsMgmtControllerDesiredMaintenanceMode_Type = CucsMgmtMaintMode
_CucsMgmtControllerDesiredMaintenanceMode_Object = MibTableColumn
cucsMgmtControllerDesiredMaintenanceMode = _CucsMgmtControllerDesiredMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 27),
    _CucsMgmtControllerDesiredMaintenanceMode_Type()
)
cucsMgmtControllerDesiredMaintenanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerDesiredMaintenanceMode.setStatus("current")
_CucsMgmtControllerLastRebootReason_Type = SnmpAdminString
_CucsMgmtControllerLastRebootReason_Object = MibTableColumn
cucsMgmtControllerLastRebootReason = _CucsMgmtControllerLastRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 28),
    _CucsMgmtControllerLastRebootReason_Type()
)
cucsMgmtControllerLastRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerLastRebootReason.setStatus("current")
_CucsMgmtControllerPowerFanSpeedPolicySupported_Type = TruthValue
_CucsMgmtControllerPowerFanSpeedPolicySupported_Object = MibTableColumn
cucsMgmtControllerPowerFanSpeedPolicySupported = _CucsMgmtControllerPowerFanSpeedPolicySupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 29),
    _CucsMgmtControllerPowerFanSpeedPolicySupported_Type()
)
cucsMgmtControllerPowerFanSpeedPolicySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerPowerFanSpeedPolicySupported.setStatus("current")
_CucsMgmtControllerSupportedCapability_Type = CucsMgmtCapability
_CucsMgmtControllerSupportedCapability_Object = MibTableColumn
cucsMgmtControllerSupportedCapability = _CucsMgmtControllerSupportedCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 6, 1, 30),
    _CucsMgmtControllerSupportedCapability_Type()
)
cucsMgmtControllerSupportedCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerSupportedCapability.setStatus("current")
_CucsMgmtControllerFsmTaskTable_Object = MibTable
cucsMgmtControllerFsmTaskTable = _CucsMgmtControllerFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 7)
)
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmTaskTable.setStatus("current")
_CucsMgmtControllerFsmTaskEntry_Object = MibTableRow
cucsMgmtControllerFsmTaskEntry = _CucsMgmtControllerFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 7, 1)
)
cucsMgmtControllerFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtControllerFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmTaskEntry.setStatus("current")
_CucsMgmtControllerFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsMgmtControllerFsmTaskInstanceId_Object = MibTableColumn
cucsMgmtControllerFsmTaskInstanceId = _CucsMgmtControllerFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 7, 1, 1),
    _CucsMgmtControllerFsmTaskInstanceId_Type()
)
cucsMgmtControllerFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmTaskInstanceId.setStatus("current")
_CucsMgmtControllerFsmTaskDn_Type = CucsManagedObjectDn
_CucsMgmtControllerFsmTaskDn_Object = MibTableColumn
cucsMgmtControllerFsmTaskDn = _CucsMgmtControllerFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 7, 1, 2),
    _CucsMgmtControllerFsmTaskDn_Type()
)
cucsMgmtControllerFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmTaskDn.setStatus("current")
_CucsMgmtControllerFsmTaskRn_Type = SnmpAdminString
_CucsMgmtControllerFsmTaskRn_Object = MibTableColumn
cucsMgmtControllerFsmTaskRn = _CucsMgmtControllerFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 7, 1, 3),
    _CucsMgmtControllerFsmTaskRn_Type()
)
cucsMgmtControllerFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmTaskRn.setStatus("current")
_CucsMgmtControllerFsmTaskCompletion_Type = CucsFsmCompletion
_CucsMgmtControllerFsmTaskCompletion_Object = MibTableColumn
cucsMgmtControllerFsmTaskCompletion = _CucsMgmtControllerFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 7, 1, 4),
    _CucsMgmtControllerFsmTaskCompletion_Type()
)
cucsMgmtControllerFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmTaskCompletion.setStatus("current")
_CucsMgmtControllerFsmTaskFlags_Type = CucsMgmtControllerFsmTaskFlags
_CucsMgmtControllerFsmTaskFlags_Object = MibTableColumn
cucsMgmtControllerFsmTaskFlags = _CucsMgmtControllerFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 7, 1, 5),
    _CucsMgmtControllerFsmTaskFlags_Type()
)
cucsMgmtControllerFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmTaskFlags.setStatus("current")
_CucsMgmtControllerFsmTaskItem_Type = CucsMgmtControllerFsmTaskItem
_CucsMgmtControllerFsmTaskItem_Object = MibTableColumn
cucsMgmtControllerFsmTaskItem = _CucsMgmtControllerFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 7, 1, 6),
    _CucsMgmtControllerFsmTaskItem_Type()
)
cucsMgmtControllerFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmTaskItem.setStatus("current")
_CucsMgmtControllerFsmTaskSeqId_Type = Gauge32
_CucsMgmtControllerFsmTaskSeqId_Object = MibTableColumn
cucsMgmtControllerFsmTaskSeqId = _CucsMgmtControllerFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 7, 1, 7),
    _CucsMgmtControllerFsmTaskSeqId_Type()
)
cucsMgmtControllerFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmTaskSeqId.setStatus("current")
_CucsMgmtEntityTable_Object = MibTable
cucsMgmtEntityTable = _CucsMgmtEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8)
)
if mibBuilder.loadTexts:
    cucsMgmtEntityTable.setStatus("current")
_CucsMgmtEntityEntry_Object = MibTableRow
cucsMgmtEntityEntry = _CucsMgmtEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1)
)
cucsMgmtEntityEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtEntityInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtEntityEntry.setStatus("current")
_CucsMgmtEntityInstanceId_Type = CucsManagedObjectId
_CucsMgmtEntityInstanceId_Object = MibTableColumn
cucsMgmtEntityInstanceId = _CucsMgmtEntityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 1),
    _CucsMgmtEntityInstanceId_Type()
)
cucsMgmtEntityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtEntityInstanceId.setStatus("current")
_CucsMgmtEntityDn_Type = CucsManagedObjectDn
_CucsMgmtEntityDn_Object = MibTableColumn
cucsMgmtEntityDn = _CucsMgmtEntityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 2),
    _CucsMgmtEntityDn_Type()
)
cucsMgmtEntityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityDn.setStatus("current")
_CucsMgmtEntityRn_Type = SnmpAdminString
_CucsMgmtEntityRn_Object = MibTableColumn
cucsMgmtEntityRn = _CucsMgmtEntityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 3),
    _CucsMgmtEntityRn_Type()
)
cucsMgmtEntityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityRn.setStatus("current")
_CucsMgmtEntityChassis1_Type = SnmpAdminString
_CucsMgmtEntityChassis1_Object = MibTableColumn
cucsMgmtEntityChassis1 = _CucsMgmtEntityChassis1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 4),
    _CucsMgmtEntityChassis1_Type()
)
cucsMgmtEntityChassis1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityChassis1.setStatus("current")
_CucsMgmtEntityChassis2_Type = SnmpAdminString
_CucsMgmtEntityChassis2_Object = MibTableColumn
cucsMgmtEntityChassis2 = _CucsMgmtEntityChassis2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 5),
    _CucsMgmtEntityChassis2_Type()
)
cucsMgmtEntityChassis2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityChassis2.setStatus("current")
_CucsMgmtEntityChassis3_Type = SnmpAdminString
_CucsMgmtEntityChassis3_Object = MibTableColumn
cucsMgmtEntityChassis3 = _CucsMgmtEntityChassis3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 6),
    _CucsMgmtEntityChassis3_Type()
)
cucsMgmtEntityChassis3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityChassis3.setStatus("current")
_CucsMgmtEntityChassisDeviceIoState1_Type = CucsMgmtEntityChassisDeviceIoState1
_CucsMgmtEntityChassisDeviceIoState1_Object = MibTableColumn
cucsMgmtEntityChassisDeviceIoState1 = _CucsMgmtEntityChassisDeviceIoState1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 7),
    _CucsMgmtEntityChassisDeviceIoState1_Type()
)
cucsMgmtEntityChassisDeviceIoState1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityChassisDeviceIoState1.setStatus("current")
_CucsMgmtEntityChassisDeviceIoState2_Type = CucsMgmtEntityChassisDeviceIoState2
_CucsMgmtEntityChassisDeviceIoState2_Object = MibTableColumn
cucsMgmtEntityChassisDeviceIoState2 = _CucsMgmtEntityChassisDeviceIoState2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 8),
    _CucsMgmtEntityChassisDeviceIoState2_Type()
)
cucsMgmtEntityChassisDeviceIoState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityChassisDeviceIoState2.setStatus("current")
_CucsMgmtEntityChassisDeviceIoState3_Type = CucsMgmtEntityChassisDeviceIoState3
_CucsMgmtEntityChassisDeviceIoState3_Object = MibTableColumn
cucsMgmtEntityChassisDeviceIoState3 = _CucsMgmtEntityChassisDeviceIoState3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 9),
    _CucsMgmtEntityChassisDeviceIoState3_Type()
)
cucsMgmtEntityChassisDeviceIoState3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityChassisDeviceIoState3.setStatus("current")
_CucsMgmtEntityHaFailureReason_Type = CucsMgmtEntityHaFailureReason
_CucsMgmtEntityHaFailureReason_Object = MibTableColumn
cucsMgmtEntityHaFailureReason = _CucsMgmtEntityHaFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 10),
    _CucsMgmtEntityHaFailureReason_Type()
)
cucsMgmtEntityHaFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityHaFailureReason.setStatus("current")
_CucsMgmtEntityHaReadiness_Type = CucsMgmtEntityHaReadiness
_CucsMgmtEntityHaReadiness_Object = MibTableColumn
cucsMgmtEntityHaReadiness = _CucsMgmtEntityHaReadiness_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 11),
    _CucsMgmtEntityHaReadiness_Type()
)
cucsMgmtEntityHaReadiness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityHaReadiness.setStatus("current")
_CucsMgmtEntityHaReady_Type = TruthValue
_CucsMgmtEntityHaReady_Object = MibTableColumn
cucsMgmtEntityHaReady = _CucsMgmtEntityHaReady_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 12),
    _CucsMgmtEntityHaReady_Type()
)
cucsMgmtEntityHaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityHaReady.setStatus("current")
_CucsMgmtEntityId_Type = CucsNetworkSwitchId
_CucsMgmtEntityId_Object = MibTableColumn
cucsMgmtEntityId = _CucsMgmtEntityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 13),
    _CucsMgmtEntityId_Type()
)
cucsMgmtEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityId.setStatus("current")
_CucsMgmtEntityLeadership_Type = CucsMgmtEntityLeadership
_CucsMgmtEntityLeadership_Object = MibTableColumn
cucsMgmtEntityLeadership = _CucsMgmtEntityLeadership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 14),
    _CucsMgmtEntityLeadership_Type()
)
cucsMgmtEntityLeadership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityLeadership.setStatus("current")
_CucsMgmtEntityMgmtServicesState_Type = CucsMgmtEntityMgmtServicesState
_CucsMgmtEntityMgmtServicesState_Object = MibTableColumn
cucsMgmtEntityMgmtServicesState = _CucsMgmtEntityMgmtServicesState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 15),
    _CucsMgmtEntityMgmtServicesState_Type()
)
cucsMgmtEntityMgmtServicesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityMgmtServicesState.setStatus("current")
_CucsMgmtEntityProblems_Type = CucsMgmtEntityProblems
_CucsMgmtEntityProblems_Object = MibTableColumn
cucsMgmtEntityProblems = _CucsMgmtEntityProblems_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 16),
    _CucsMgmtEntityProblems_Type()
)
cucsMgmtEntityProblems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityProblems.setStatus("current")
_CucsMgmtEntityState_Type = CucsMgmtEntityState
_CucsMgmtEntityState_Object = MibTableColumn
cucsMgmtEntityState = _CucsMgmtEntityState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 17),
    _CucsMgmtEntityState_Type()
)
cucsMgmtEntityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityState.setStatus("current")
_CucsMgmtEntityUmbilicalState_Type = CucsMgmtEntityUmbilicalState
_CucsMgmtEntityUmbilicalState_Object = MibTableColumn
cucsMgmtEntityUmbilicalState = _CucsMgmtEntityUmbilicalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 18),
    _CucsMgmtEntityUmbilicalState_Type()
)
cucsMgmtEntityUmbilicalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityUmbilicalState.setStatus("current")
_CucsMgmtEntityVersionMismatch_Type = TruthValue
_CucsMgmtEntityVersionMismatch_Object = MibTableColumn
cucsMgmtEntityVersionMismatch = _CucsMgmtEntityVersionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 19),
    _CucsMgmtEntityVersionMismatch_Type()
)
cucsMgmtEntityVersionMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntityVersionMismatch.setStatus("current")
_CucsMgmtEntitySshAuthKeysCsum_Type = SnmpAdminString
_CucsMgmtEntitySshAuthKeysCsum_Object = MibTableColumn
cucsMgmtEntitySshAuthKeysCsum = _CucsMgmtEntitySshAuthKeysCsum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 20),
    _CucsMgmtEntitySshAuthKeysCsum_Type()
)
cucsMgmtEntitySshAuthKeysCsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntitySshAuthKeysCsum.setStatus("current")
_CucsMgmtEntitySshAuthKeysSize_Type = Unsigned64
_CucsMgmtEntitySshAuthKeysSize_Object = MibTableColumn
cucsMgmtEntitySshAuthKeysSize = _CucsMgmtEntitySshAuthKeysSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 21),
    _CucsMgmtEntitySshAuthKeysSize_Type()
)
cucsMgmtEntitySshAuthKeysSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntitySshAuthKeysSize.setStatus("current")
_CucsMgmtEntitySshKeyStatus_Type = Unsigned64
_CucsMgmtEntitySshKeyStatus_Object = MibTableColumn
cucsMgmtEntitySshKeyStatus = _CucsMgmtEntitySshKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 22),
    _CucsMgmtEntitySshKeyStatus_Type()
)
cucsMgmtEntitySshKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntitySshKeyStatus.setStatus("current")
_CucsMgmtEntitySshRootPubKeyCsum_Type = SnmpAdminString
_CucsMgmtEntitySshRootPubKeyCsum_Object = MibTableColumn
cucsMgmtEntitySshRootPubKeyCsum = _CucsMgmtEntitySshRootPubKeyCsum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 23),
    _CucsMgmtEntitySshRootPubKeyCsum_Type()
)
cucsMgmtEntitySshRootPubKeyCsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntitySshRootPubKeyCsum.setStatus("current")
_CucsMgmtEntitySshRootPubKeySize_Type = Unsigned64
_CucsMgmtEntitySshRootPubKeySize_Object = MibTableColumn
cucsMgmtEntitySshRootPubKeySize = _CucsMgmtEntitySshRootPubKeySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 8, 1, 24),
    _CucsMgmtEntitySshRootPubKeySize_Type()
)
cucsMgmtEntitySshRootPubKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtEntitySshRootPubKeySize.setStatus("current")
_CucsMgmtIfTable_Object = MibTable
cucsMgmtIfTable = _CucsMgmtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9)
)
if mibBuilder.loadTexts:
    cucsMgmtIfTable.setStatus("current")
_CucsMgmtIfEntry_Object = MibTableRow
cucsMgmtIfEntry = _CucsMgmtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1)
)
cucsMgmtIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtIfEntry.setStatus("current")
_CucsMgmtIfInstanceId_Type = CucsManagedObjectId
_CucsMgmtIfInstanceId_Object = MibTableColumn
cucsMgmtIfInstanceId = _CucsMgmtIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 1),
    _CucsMgmtIfInstanceId_Type()
)
cucsMgmtIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtIfInstanceId.setStatus("current")
_CucsMgmtIfDn_Type = CucsManagedObjectDn
_CucsMgmtIfDn_Object = MibTableColumn
cucsMgmtIfDn = _CucsMgmtIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 2),
    _CucsMgmtIfDn_Type()
)
cucsMgmtIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfDn.setStatus("current")
_CucsMgmtIfRn_Type = SnmpAdminString
_CucsMgmtIfRn_Object = MibTableColumn
cucsMgmtIfRn = _CucsMgmtIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 3),
    _CucsMgmtIfRn_Type()
)
cucsMgmtIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfRn.setStatus("current")
_CucsMgmtIfAccess_Type = CucsMgmtAccess
_CucsMgmtIfAccess_Object = MibTableColumn
cucsMgmtIfAccess = _CucsMgmtIfAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 4),
    _CucsMgmtIfAccess_Type()
)
cucsMgmtIfAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfAccess.setStatus("current")
_CucsMgmtIfAdminState_Type = CucsMgmtAdminState
_CucsMgmtIfAdminState_Object = MibTableColumn
cucsMgmtIfAdminState = _CucsMgmtIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 5),
    _CucsMgmtIfAdminState_Type()
)
cucsMgmtIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfAdminState.setStatus("current")
_CucsMgmtIfChassisId_Type = Gauge32
_CucsMgmtIfChassisId_Object = MibTableColumn
cucsMgmtIfChassisId = _CucsMgmtIfChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 6),
    _CucsMgmtIfChassisId_Type()
)
cucsMgmtIfChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfChassisId.setStatus("current")
_CucsMgmtIfDiscovery_Type = CucsEtherSatelliteConnectionDisc
_CucsMgmtIfDiscovery_Object = MibTableColumn
cucsMgmtIfDiscovery = _CucsMgmtIfDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 7),
    _CucsMgmtIfDiscovery_Type()
)
cucsMgmtIfDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfDiscovery.setStatus("current")
_CucsMgmtIfEpDn_Type = SnmpAdminString
_CucsMgmtIfEpDn_Object = MibTableColumn
cucsMgmtIfEpDn = _CucsMgmtIfEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 8),
    _CucsMgmtIfEpDn_Type()
)
cucsMgmtIfEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfEpDn.setStatus("current")
_CucsMgmtIfExtBroadcast_Type = InetAddressIPv4
_CucsMgmtIfExtBroadcast_Object = MibTableColumn
cucsMgmtIfExtBroadcast = _CucsMgmtIfExtBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 9),
    _CucsMgmtIfExtBroadcast_Type()
)
cucsMgmtIfExtBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfExtBroadcast.setStatus("current")
_CucsMgmtIfExtGw_Type = InetAddressIPv4
_CucsMgmtIfExtGw_Object = MibTableColumn
cucsMgmtIfExtGw = _CucsMgmtIfExtGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 10),
    _CucsMgmtIfExtGw_Type()
)
cucsMgmtIfExtGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfExtGw.setStatus("current")
_CucsMgmtIfExtIp_Type = InetAddressIPv4
_CucsMgmtIfExtIp_Object = MibTableColumn
cucsMgmtIfExtIp = _CucsMgmtIfExtIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 11),
    _CucsMgmtIfExtIp_Type()
)
cucsMgmtIfExtIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfExtIp.setStatus("current")
_CucsMgmtIfExtMask_Type = InetAddressIPv4
_CucsMgmtIfExtMask_Object = MibTableColumn
cucsMgmtIfExtMask = _CucsMgmtIfExtMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 12),
    _CucsMgmtIfExtMask_Type()
)
cucsMgmtIfExtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfExtMask.setStatus("current")
_CucsMgmtIfFsmDescr_Type = SnmpAdminString
_CucsMgmtIfFsmDescr_Object = MibTableColumn
cucsMgmtIfFsmDescr = _CucsMgmtIfFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 13),
    _CucsMgmtIfFsmDescr_Type()
)
cucsMgmtIfFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmDescr.setStatus("current")
_CucsMgmtIfFsmPrev_Type = SnmpAdminString
_CucsMgmtIfFsmPrev_Object = MibTableColumn
cucsMgmtIfFsmPrev = _CucsMgmtIfFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 14),
    _CucsMgmtIfFsmPrev_Type()
)
cucsMgmtIfFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmPrev.setStatus("current")
_CucsMgmtIfFsmProgr_Type = Gauge32
_CucsMgmtIfFsmProgr_Object = MibTableColumn
cucsMgmtIfFsmProgr = _CucsMgmtIfFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 15),
    _CucsMgmtIfFsmProgr_Type()
)
cucsMgmtIfFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmProgr.setStatus("current")
_CucsMgmtIfFsmRmtInvErrCode_Type = Gauge32
_CucsMgmtIfFsmRmtInvErrCode_Object = MibTableColumn
cucsMgmtIfFsmRmtInvErrCode = _CucsMgmtIfFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 16),
    _CucsMgmtIfFsmRmtInvErrCode_Type()
)
cucsMgmtIfFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmRmtInvErrCode.setStatus("current")
_CucsMgmtIfFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsMgmtIfFsmRmtInvErrDescr_Object = MibTableColumn
cucsMgmtIfFsmRmtInvErrDescr = _CucsMgmtIfFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 17),
    _CucsMgmtIfFsmRmtInvErrDescr_Type()
)
cucsMgmtIfFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmRmtInvErrDescr.setStatus("current")
_CucsMgmtIfFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtIfFsmRmtInvRslt_Object = MibTableColumn
cucsMgmtIfFsmRmtInvRslt = _CucsMgmtIfFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 18),
    _CucsMgmtIfFsmRmtInvRslt_Type()
)
cucsMgmtIfFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmRmtInvRslt.setStatus("current")
_CucsMgmtIfFsmStageDescr_Type = SnmpAdminString
_CucsMgmtIfFsmStageDescr_Object = MibTableColumn
cucsMgmtIfFsmStageDescr = _CucsMgmtIfFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 19),
    _CucsMgmtIfFsmStageDescr_Type()
)
cucsMgmtIfFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmStageDescr.setStatus("current")
_CucsMgmtIfFsmStamp_Type = DateAndTime
_CucsMgmtIfFsmStamp_Object = MibTableColumn
cucsMgmtIfFsmStamp = _CucsMgmtIfFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 20),
    _CucsMgmtIfFsmStamp_Type()
)
cucsMgmtIfFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmStamp.setStatus("current")
_CucsMgmtIfFsmStatus_Type = SnmpAdminString
_CucsMgmtIfFsmStatus_Object = MibTableColumn
cucsMgmtIfFsmStatus = _CucsMgmtIfFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 21),
    _CucsMgmtIfFsmStatus_Type()
)
cucsMgmtIfFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmStatus.setStatus("current")
_CucsMgmtIfFsmTry_Type = Gauge32
_CucsMgmtIfFsmTry_Object = MibTableColumn
cucsMgmtIfFsmTry = _CucsMgmtIfFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 22),
    _CucsMgmtIfFsmTry_Type()
)
cucsMgmtIfFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmTry.setStatus("current")
_CucsMgmtIfId_Type = Gauge32
_CucsMgmtIfId_Object = MibTableColumn
cucsMgmtIfId = _CucsMgmtIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 23),
    _CucsMgmtIfId_Type()
)
cucsMgmtIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfId.setStatus("current")
_CucsMgmtIfIfRole_Type = CucsNetworkPortRole
_CucsMgmtIfIfRole_Object = MibTableColumn
cucsMgmtIfIfRole = _CucsMgmtIfIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 24),
    _CucsMgmtIfIfRole_Type()
)
cucsMgmtIfIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfIfRole.setStatus("current")
_CucsMgmtIfIfType_Type = CucsNetworkPhysEpIfType
_CucsMgmtIfIfType_Object = MibTableColumn
cucsMgmtIfIfType = _CucsMgmtIfIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 25),
    _CucsMgmtIfIfType_Type()
)
cucsMgmtIfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfIfType.setStatus("current")
_CucsMgmtIfIp_Type = InetAddressIPv4
_CucsMgmtIfIp_Object = MibTableColumn
cucsMgmtIfIp = _CucsMgmtIfIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 26),
    _CucsMgmtIfIp_Type()
)
cucsMgmtIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfIp.setStatus("current")
_CucsMgmtIfLocale_Type = CucsNetworkLocale
_CucsMgmtIfLocale_Object = MibTableColumn
cucsMgmtIfLocale = _CucsMgmtIfLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 27),
    _CucsMgmtIfLocale_Type()
)
cucsMgmtIfLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfLocale.setStatus("current")
_CucsMgmtIfMac_Type = MacAddress
_CucsMgmtIfMac_Object = MibTableColumn
cucsMgmtIfMac = _CucsMgmtIfMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 28),
    _CucsMgmtIfMac_Type()
)
cucsMgmtIfMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfMac.setStatus("current")
_CucsMgmtIfMask_Type = InetAddressIPv4
_CucsMgmtIfMask_Object = MibTableColumn
cucsMgmtIfMask = _CucsMgmtIfMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 29),
    _CucsMgmtIfMask_Type()
)
cucsMgmtIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfMask.setStatus("current")
_CucsMgmtIfName_Type = SnmpAdminString
_CucsMgmtIfName_Object = MibTableColumn
cucsMgmtIfName = _CucsMgmtIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 30),
    _CucsMgmtIfName_Type()
)
cucsMgmtIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfName.setStatus("current")
_CucsMgmtIfPeerDn_Type = SnmpAdminString
_CucsMgmtIfPeerDn_Object = MibTableColumn
cucsMgmtIfPeerDn = _CucsMgmtIfPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 31),
    _CucsMgmtIfPeerDn_Type()
)
cucsMgmtIfPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfPeerDn.setStatus("current")
_CucsMgmtIfPeerPortId_Type = Gauge32
_CucsMgmtIfPeerPortId_Object = MibTableColumn
cucsMgmtIfPeerPortId = _CucsMgmtIfPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 32),
    _CucsMgmtIfPeerPortId_Type()
)
cucsMgmtIfPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfPeerPortId.setStatus("current")
_CucsMgmtIfPeerSlotId_Type = Gauge32
_CucsMgmtIfPeerSlotId_Object = MibTableColumn
cucsMgmtIfPeerSlotId = _CucsMgmtIfPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 33),
    _CucsMgmtIfPeerSlotId_Type()
)
cucsMgmtIfPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfPeerSlotId.setStatus("current")
_CucsMgmtIfPortId_Type = Gauge32
_CucsMgmtIfPortId_Object = MibTableColumn
cucsMgmtIfPortId = _CucsMgmtIfPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 34),
    _CucsMgmtIfPortId_Type()
)
cucsMgmtIfPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfPortId.setStatus("current")
_CucsMgmtIfSlotId_Type = Gauge32
_CucsMgmtIfSlotId_Object = MibTableColumn
cucsMgmtIfSlotId = _CucsMgmtIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 35),
    _CucsMgmtIfSlotId_Type()
)
cucsMgmtIfSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfSlotId.setStatus("current")
_CucsMgmtIfStateQual_Type = CucsMgmtStateQual
_CucsMgmtIfStateQual_Object = MibTableColumn
cucsMgmtIfStateQual = _CucsMgmtIfStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 36),
    _CucsMgmtIfStateQual_Type()
)
cucsMgmtIfStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfStateQual.setStatus("current")
_CucsMgmtIfSubject_Type = CucsMgmtSubject
_CucsMgmtIfSubject_Object = MibTableColumn
cucsMgmtIfSubject = _CucsMgmtIfSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 37),
    _CucsMgmtIfSubject_Type()
)
cucsMgmtIfSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfSubject.setStatus("current")
_CucsMgmtIfSwitchId_Type = CucsNetworkSwitchId
_CucsMgmtIfSwitchId_Object = MibTableColumn
cucsMgmtIfSwitchId = _CucsMgmtIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 38),
    _CucsMgmtIfSwitchId_Type()
)
cucsMgmtIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfSwitchId.setStatus("current")
_CucsMgmtIfTransport_Type = CucsNetworkTransport
_CucsMgmtIfTransport_Object = MibTableColumn
cucsMgmtIfTransport = _CucsMgmtIfTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 39),
    _CucsMgmtIfTransport_Type()
)
cucsMgmtIfTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfTransport.setStatus("current")
_CucsMgmtIfType_Type = CucsNetworkConnectionType
_CucsMgmtIfType_Object = MibTableColumn
cucsMgmtIfType = _CucsMgmtIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 40),
    _CucsMgmtIfType_Type()
)
cucsMgmtIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfType.setStatus("current")
_CucsMgmtIfVnet_Type = Gauge32
_CucsMgmtIfVnet_Object = MibTableColumn
cucsMgmtIfVnet = _CucsMgmtIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 41),
    _CucsMgmtIfVnet_Type()
)
cucsMgmtIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfVnet.setStatus("current")
_CucsMgmtIfPeerChassisId_Type = Gauge32
_CucsMgmtIfPeerChassisId_Object = MibTableColumn
cucsMgmtIfPeerChassisId = _CucsMgmtIfPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 42),
    _CucsMgmtIfPeerChassisId_Type()
)
cucsMgmtIfPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfPeerChassisId.setStatus("current")
_CucsMgmtIfAggrPortId_Type = Gauge32
_CucsMgmtIfAggrPortId_Object = MibTableColumn
cucsMgmtIfAggrPortId = _CucsMgmtIfAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 43),
    _CucsMgmtIfAggrPortId_Type()
)
cucsMgmtIfAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfAggrPortId.setStatus("current")
_CucsMgmtIfPeerAggrPortId_Type = Gauge32
_CucsMgmtIfPeerAggrPortId_Object = MibTableColumn
cucsMgmtIfPeerAggrPortId = _CucsMgmtIfPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 9, 1, 44),
    _CucsMgmtIfPeerAggrPortId_Type()
)
cucsMgmtIfPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfPeerAggrPortId.setStatus("current")
_CucsMgmtIfFsmTaskTable_Object = MibTable
cucsMgmtIfFsmTaskTable = _CucsMgmtIfFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 10)
)
if mibBuilder.loadTexts:
    cucsMgmtIfFsmTaskTable.setStatus("current")
_CucsMgmtIfFsmTaskEntry_Object = MibTableRow
cucsMgmtIfFsmTaskEntry = _CucsMgmtIfFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 10, 1)
)
cucsMgmtIfFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtIfFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtIfFsmTaskEntry.setStatus("current")
_CucsMgmtIfFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsMgmtIfFsmTaskInstanceId_Object = MibTableColumn
cucsMgmtIfFsmTaskInstanceId = _CucsMgmtIfFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 10, 1, 1),
    _CucsMgmtIfFsmTaskInstanceId_Type()
)
cucsMgmtIfFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmTaskInstanceId.setStatus("current")
_CucsMgmtIfFsmTaskDn_Type = CucsManagedObjectDn
_CucsMgmtIfFsmTaskDn_Object = MibTableColumn
cucsMgmtIfFsmTaskDn = _CucsMgmtIfFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 10, 1, 2),
    _CucsMgmtIfFsmTaskDn_Type()
)
cucsMgmtIfFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmTaskDn.setStatus("current")
_CucsMgmtIfFsmTaskRn_Type = SnmpAdminString
_CucsMgmtIfFsmTaskRn_Object = MibTableColumn
cucsMgmtIfFsmTaskRn = _CucsMgmtIfFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 10, 1, 3),
    _CucsMgmtIfFsmTaskRn_Type()
)
cucsMgmtIfFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmTaskRn.setStatus("current")
_CucsMgmtIfFsmTaskCompletion_Type = CucsFsmCompletion
_CucsMgmtIfFsmTaskCompletion_Object = MibTableColumn
cucsMgmtIfFsmTaskCompletion = _CucsMgmtIfFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 10, 1, 4),
    _CucsMgmtIfFsmTaskCompletion_Type()
)
cucsMgmtIfFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmTaskCompletion.setStatus("current")
_CucsMgmtIfFsmTaskFlags_Type = CucsFsmFlags
_CucsMgmtIfFsmTaskFlags_Object = MibTableColumn
cucsMgmtIfFsmTaskFlags = _CucsMgmtIfFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 10, 1, 5),
    _CucsMgmtIfFsmTaskFlags_Type()
)
cucsMgmtIfFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmTaskFlags.setStatus("current")
_CucsMgmtIfFsmTaskItem_Type = CucsMgmtIfFsmTaskItem
_CucsMgmtIfFsmTaskItem_Object = MibTableColumn
cucsMgmtIfFsmTaskItem = _CucsMgmtIfFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 10, 1, 6),
    _CucsMgmtIfFsmTaskItem_Type()
)
cucsMgmtIfFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmTaskItem.setStatus("current")
_CucsMgmtIfFsmTaskSeqId_Type = Gauge32
_CucsMgmtIfFsmTaskSeqId_Object = MibTableColumn
cucsMgmtIfFsmTaskSeqId = _CucsMgmtIfFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 10, 1, 7),
    _CucsMgmtIfFsmTaskSeqId_Type()
)
cucsMgmtIfFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmTaskSeqId.setStatus("current")
_CucsMgmtImporterTable_Object = MibTable
cucsMgmtImporterTable = _CucsMgmtImporterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11)
)
if mibBuilder.loadTexts:
    cucsMgmtImporterTable.setStatus("current")
_CucsMgmtImporterEntry_Object = MibTableRow
cucsMgmtImporterEntry = _CucsMgmtImporterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1)
)
cucsMgmtImporterEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtImporterInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtImporterEntry.setStatus("current")
_CucsMgmtImporterInstanceId_Type = CucsManagedObjectId
_CucsMgmtImporterInstanceId_Object = MibTableColumn
cucsMgmtImporterInstanceId = _CucsMgmtImporterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 1),
    _CucsMgmtImporterInstanceId_Type()
)
cucsMgmtImporterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtImporterInstanceId.setStatus("current")
_CucsMgmtImporterDn_Type = CucsManagedObjectDn
_CucsMgmtImporterDn_Object = MibTableColumn
cucsMgmtImporterDn = _CucsMgmtImporterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 2),
    _CucsMgmtImporterDn_Type()
)
cucsMgmtImporterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterDn.setStatus("current")
_CucsMgmtImporterRn_Type = SnmpAdminString
_CucsMgmtImporterRn_Object = MibTableColumn
cucsMgmtImporterRn = _CucsMgmtImporterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 3),
    _CucsMgmtImporterRn_Type()
)
cucsMgmtImporterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterRn.setStatus("current")
_CucsMgmtImporterAction_Type = CucsMgmtImportAction
_CucsMgmtImporterAction_Object = MibTableColumn
cucsMgmtImporterAction = _CucsMgmtImporterAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 4),
    _CucsMgmtImporterAction_Type()
)
cucsMgmtImporterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterAction.setStatus("current")
_CucsMgmtImporterAdminState_Type = CucsCommClientAdminState
_CucsMgmtImporterAdminState_Object = MibTableColumn
cucsMgmtImporterAdminState = _CucsMgmtImporterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 5),
    _CucsMgmtImporterAdminState_Type()
)
cucsMgmtImporterAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterAdminState.setStatus("current")
_CucsMgmtImporterDescr_Type = SnmpAdminString
_CucsMgmtImporterDescr_Object = MibTableColumn
cucsMgmtImporterDescr = _CucsMgmtImporterDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 6),
    _CucsMgmtImporterDescr_Type()
)
cucsMgmtImporterDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterDescr.setStatus("current")
_CucsMgmtImporterFsmDescr_Type = SnmpAdminString
_CucsMgmtImporterFsmDescr_Object = MibTableColumn
cucsMgmtImporterFsmDescr = _CucsMgmtImporterFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 7),
    _CucsMgmtImporterFsmDescr_Type()
)
cucsMgmtImporterFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmDescr.setStatus("current")
_CucsMgmtImporterFsmPrev_Type = SnmpAdminString
_CucsMgmtImporterFsmPrev_Object = MibTableColumn
cucsMgmtImporterFsmPrev = _CucsMgmtImporterFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 8),
    _CucsMgmtImporterFsmPrev_Type()
)
cucsMgmtImporterFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmPrev.setStatus("current")
_CucsMgmtImporterFsmProgr_Type = Gauge32
_CucsMgmtImporterFsmProgr_Object = MibTableColumn
cucsMgmtImporterFsmProgr = _CucsMgmtImporterFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 9),
    _CucsMgmtImporterFsmProgr_Type()
)
cucsMgmtImporterFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmProgr.setStatus("current")
_CucsMgmtImporterFsmRmtInvErrCode_Type = Gauge32
_CucsMgmtImporterFsmRmtInvErrCode_Object = MibTableColumn
cucsMgmtImporterFsmRmtInvErrCode = _CucsMgmtImporterFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 10),
    _CucsMgmtImporterFsmRmtInvErrCode_Type()
)
cucsMgmtImporterFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmRmtInvErrCode.setStatus("current")
_CucsMgmtImporterFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsMgmtImporterFsmRmtInvErrDescr_Object = MibTableColumn
cucsMgmtImporterFsmRmtInvErrDescr = _CucsMgmtImporterFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 11),
    _CucsMgmtImporterFsmRmtInvErrDescr_Type()
)
cucsMgmtImporterFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmRmtInvErrDescr.setStatus("current")
_CucsMgmtImporterFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtImporterFsmRmtInvRslt_Object = MibTableColumn
cucsMgmtImporterFsmRmtInvRslt = _CucsMgmtImporterFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 12),
    _CucsMgmtImporterFsmRmtInvRslt_Type()
)
cucsMgmtImporterFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmRmtInvRslt.setStatus("current")
_CucsMgmtImporterFsmStageDescr_Type = SnmpAdminString
_CucsMgmtImporterFsmStageDescr_Object = MibTableColumn
cucsMgmtImporterFsmStageDescr = _CucsMgmtImporterFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 13),
    _CucsMgmtImporterFsmStageDescr_Type()
)
cucsMgmtImporterFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmStageDescr.setStatus("current")
_CucsMgmtImporterFsmStamp_Type = DateAndTime
_CucsMgmtImporterFsmStamp_Object = MibTableColumn
cucsMgmtImporterFsmStamp = _CucsMgmtImporterFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 14),
    _CucsMgmtImporterFsmStamp_Type()
)
cucsMgmtImporterFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmStamp.setStatus("current")
_CucsMgmtImporterFsmStatus_Type = SnmpAdminString
_CucsMgmtImporterFsmStatus_Object = MibTableColumn
cucsMgmtImporterFsmStatus = _CucsMgmtImporterFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 15),
    _CucsMgmtImporterFsmStatus_Type()
)
cucsMgmtImporterFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmStatus.setStatus("current")
_CucsMgmtImporterFsmTry_Type = Gauge32
_CucsMgmtImporterFsmTry_Object = MibTableColumn
cucsMgmtImporterFsmTry = _CucsMgmtImporterFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 16),
    _CucsMgmtImporterFsmTry_Type()
)
cucsMgmtImporterFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmTry.setStatus("current")
_CucsMgmtImporterHostname_Type = SnmpAdminString
_CucsMgmtImporterHostname_Object = MibTableColumn
cucsMgmtImporterHostname = _CucsMgmtImporterHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 17),
    _CucsMgmtImporterHostname_Type()
)
cucsMgmtImporterHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterHostname.setStatus("current")
_CucsMgmtImporterIntId_Type = SnmpAdminString
_CucsMgmtImporterIntId_Object = MibTableColumn
cucsMgmtImporterIntId = _CucsMgmtImporterIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 18),
    _CucsMgmtImporterIntId_Type()
)
cucsMgmtImporterIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterIntId.setStatus("current")
_CucsMgmtImporterName_Type = SnmpAdminString
_CucsMgmtImporterName_Object = MibTableColumn
cucsMgmtImporterName = _CucsMgmtImporterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 19),
    _CucsMgmtImporterName_Type()
)
cucsMgmtImporterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterName.setStatus("current")
_CucsMgmtImporterPostAction_Type = CucsMgmtImporterPostAction
_CucsMgmtImporterPostAction_Object = MibTableColumn
cucsMgmtImporterPostAction = _CucsMgmtImporterPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 20),
    _CucsMgmtImporterPostAction_Type()
)
cucsMgmtImporterPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterPostAction.setStatus("current")
_CucsMgmtImporterProto_Type = CucsMgmtImporterProto
_CucsMgmtImporterProto_Object = MibTableColumn
cucsMgmtImporterProto = _CucsMgmtImporterProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 21),
    _CucsMgmtImporterProto_Type()
)
cucsMgmtImporterProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterProto.setStatus("current")
_CucsMgmtImporterPwd_Type = SnmpAdminString
_CucsMgmtImporterPwd_Object = MibTableColumn
cucsMgmtImporterPwd = _CucsMgmtImporterPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 22),
    _CucsMgmtImporterPwd_Type()
)
cucsMgmtImporterPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterPwd.setStatus("current")
_CucsMgmtImporterRemoteFile_Type = SnmpAdminString
_CucsMgmtImporterRemoteFile_Object = MibTableColumn
cucsMgmtImporterRemoteFile = _CucsMgmtImporterRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 23),
    _CucsMgmtImporterRemoteFile_Type()
)
cucsMgmtImporterRemoteFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterRemoteFile.setStatus("current")
_CucsMgmtImporterUser_Type = SnmpAdminString
_CucsMgmtImporterUser_Object = MibTableColumn
cucsMgmtImporterUser = _CucsMgmtImporterUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 24),
    _CucsMgmtImporterUser_Type()
)
cucsMgmtImporterUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterUser.setStatus("current")
_CucsMgmtImporterPolicyLevel_Type = Gauge32
_CucsMgmtImporterPolicyLevel_Object = MibTableColumn
cucsMgmtImporterPolicyLevel = _CucsMgmtImporterPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 25),
    _CucsMgmtImporterPolicyLevel_Type()
)
cucsMgmtImporterPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterPolicyLevel.setStatus("current")
_CucsMgmtImporterPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsMgmtImporterPolicyOwner_Object = MibTableColumn
cucsMgmtImporterPolicyOwner = _CucsMgmtImporterPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 26),
    _CucsMgmtImporterPolicyOwner_Type()
)
cucsMgmtImporterPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterPolicyOwner.setStatus("current")
_CucsMgmtImporterOperStatus_Type = CucsMgmtImportStatus
_CucsMgmtImporterOperStatus_Object = MibTableColumn
cucsMgmtImporterOperStatus = _CucsMgmtImporterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 11, 1, 27),
    _CucsMgmtImporterOperStatus_Type()
)
cucsMgmtImporterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterOperStatus.setStatus("current")
_CucsMgmtImporterFsmTaskTable_Object = MibTable
cucsMgmtImporterFsmTaskTable = _CucsMgmtImporterFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 12)
)
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmTaskTable.setStatus("current")
_CucsMgmtImporterFsmTaskEntry_Object = MibTableRow
cucsMgmtImporterFsmTaskEntry = _CucsMgmtImporterFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 12, 1)
)
cucsMgmtImporterFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtImporterFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmTaskEntry.setStatus("current")
_CucsMgmtImporterFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsMgmtImporterFsmTaskInstanceId_Object = MibTableColumn
cucsMgmtImporterFsmTaskInstanceId = _CucsMgmtImporterFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 12, 1, 1),
    _CucsMgmtImporterFsmTaskInstanceId_Type()
)
cucsMgmtImporterFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmTaskInstanceId.setStatus("current")
_CucsMgmtImporterFsmTaskDn_Type = CucsManagedObjectDn
_CucsMgmtImporterFsmTaskDn_Object = MibTableColumn
cucsMgmtImporterFsmTaskDn = _CucsMgmtImporterFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 12, 1, 2),
    _CucsMgmtImporterFsmTaskDn_Type()
)
cucsMgmtImporterFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmTaskDn.setStatus("current")
_CucsMgmtImporterFsmTaskRn_Type = SnmpAdminString
_CucsMgmtImporterFsmTaskRn_Object = MibTableColumn
cucsMgmtImporterFsmTaskRn = _CucsMgmtImporterFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 12, 1, 3),
    _CucsMgmtImporterFsmTaskRn_Type()
)
cucsMgmtImporterFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmTaskRn.setStatus("current")
_CucsMgmtImporterFsmTaskCompletion_Type = CucsFsmCompletion
_CucsMgmtImporterFsmTaskCompletion_Object = MibTableColumn
cucsMgmtImporterFsmTaskCompletion = _CucsMgmtImporterFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 12, 1, 4),
    _CucsMgmtImporterFsmTaskCompletion_Type()
)
cucsMgmtImporterFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmTaskCompletion.setStatus("current")
_CucsMgmtImporterFsmTaskFlags_Type = CucsFsmFlags
_CucsMgmtImporterFsmTaskFlags_Object = MibTableColumn
cucsMgmtImporterFsmTaskFlags = _CucsMgmtImporterFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 12, 1, 5),
    _CucsMgmtImporterFsmTaskFlags_Type()
)
cucsMgmtImporterFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmTaskFlags.setStatus("current")
_CucsMgmtImporterFsmTaskItem_Type = CucsMgmtImporterFsmTaskItem
_CucsMgmtImporterFsmTaskItem_Object = MibTableColumn
cucsMgmtImporterFsmTaskItem = _CucsMgmtImporterFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 12, 1, 6),
    _CucsMgmtImporterFsmTaskItem_Type()
)
cucsMgmtImporterFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmTaskItem.setStatus("current")
_CucsMgmtImporterFsmTaskSeqId_Type = Gauge32
_CucsMgmtImporterFsmTaskSeqId_Object = MibTableColumn
cucsMgmtImporterFsmTaskSeqId = _CucsMgmtImporterFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 12, 1, 7),
    _CucsMgmtImporterFsmTaskSeqId_Type()
)
cucsMgmtImporterFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmTaskSeqId.setStatus("current")
_CucsMgmtIntAuthPolicyTable_Object = MibTable
cucsMgmtIntAuthPolicyTable = _CucsMgmtIntAuthPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 13)
)
if mibBuilder.loadTexts:
    cucsMgmtIntAuthPolicyTable.setStatus("current")
_CucsMgmtIntAuthPolicyEntry_Object = MibTableRow
cucsMgmtIntAuthPolicyEntry = _CucsMgmtIntAuthPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 13, 1)
)
cucsMgmtIntAuthPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtIntAuthPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtIntAuthPolicyEntry.setStatus("current")
_CucsMgmtIntAuthPolicyInstanceId_Type = CucsManagedObjectId
_CucsMgmtIntAuthPolicyInstanceId_Object = MibTableColumn
cucsMgmtIntAuthPolicyInstanceId = _CucsMgmtIntAuthPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 13, 1, 1),
    _CucsMgmtIntAuthPolicyInstanceId_Type()
)
cucsMgmtIntAuthPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtIntAuthPolicyInstanceId.setStatus("current")
_CucsMgmtIntAuthPolicyDn_Type = CucsManagedObjectDn
_CucsMgmtIntAuthPolicyDn_Object = MibTableColumn
cucsMgmtIntAuthPolicyDn = _CucsMgmtIntAuthPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 13, 1, 2),
    _CucsMgmtIntAuthPolicyDn_Type()
)
cucsMgmtIntAuthPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIntAuthPolicyDn.setStatus("current")
_CucsMgmtIntAuthPolicyRn_Type = SnmpAdminString
_CucsMgmtIntAuthPolicyRn_Object = MibTableColumn
cucsMgmtIntAuthPolicyRn = _CucsMgmtIntAuthPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 13, 1, 3),
    _CucsMgmtIntAuthPolicyRn_Type()
)
cucsMgmtIntAuthPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIntAuthPolicyRn.setStatus("current")
_CucsMgmtIntAuthPolicyMethod_Type = CucsMgmtIntAuthPolicyMethod
_CucsMgmtIntAuthPolicyMethod_Object = MibTableColumn
cucsMgmtIntAuthPolicyMethod = _CucsMgmtIntAuthPolicyMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 13, 1, 4),
    _CucsMgmtIntAuthPolicyMethod_Type()
)
cucsMgmtIntAuthPolicyMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIntAuthPolicyMethod.setStatus("current")
_CucsMgmtIntAuthPolicyName_Type = SnmpAdminString
_CucsMgmtIntAuthPolicyName_Object = MibTableColumn
cucsMgmtIntAuthPolicyName = _CucsMgmtIntAuthPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 13, 1, 5),
    _CucsMgmtIntAuthPolicyName_Type()
)
cucsMgmtIntAuthPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIntAuthPolicyName.setStatus("current")
_CucsMgmtIntAuthPolicyPwd_Type = SnmpAdminString
_CucsMgmtIntAuthPolicyPwd_Object = MibTableColumn
cucsMgmtIntAuthPolicyPwd = _CucsMgmtIntAuthPolicyPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 13, 1, 6),
    _CucsMgmtIntAuthPolicyPwd_Type()
)
cucsMgmtIntAuthPolicyPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIntAuthPolicyPwd.setStatus("current")
_CucsMgmtPmonEntryTable_Object = MibTable
cucsMgmtPmonEntryTable = _CucsMgmtPmonEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14)
)
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryTable.setStatus("current")
_CucsMgmtPmonEntryEntry_Object = MibTableRow
cucsMgmtPmonEntryEntry = _CucsMgmtPmonEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1)
)
cucsMgmtPmonEntryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtPmonEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryEntry.setStatus("current")
_CucsMgmtPmonEntryInstanceId_Type = CucsManagedObjectId
_CucsMgmtPmonEntryInstanceId_Object = MibTableColumn
cucsMgmtPmonEntryInstanceId = _CucsMgmtPmonEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 1),
    _CucsMgmtPmonEntryInstanceId_Type()
)
cucsMgmtPmonEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryInstanceId.setStatus("current")
_CucsMgmtPmonEntryDn_Type = CucsManagedObjectDn
_CucsMgmtPmonEntryDn_Object = MibTableColumn
cucsMgmtPmonEntryDn = _CucsMgmtPmonEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 2),
    _CucsMgmtPmonEntryDn_Type()
)
cucsMgmtPmonEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryDn.setStatus("current")
_CucsMgmtPmonEntryRn_Type = SnmpAdminString
_CucsMgmtPmonEntryRn_Object = MibTableColumn
cucsMgmtPmonEntryRn = _CucsMgmtPmonEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 3),
    _CucsMgmtPmonEntryRn_Type()
)
cucsMgmtPmonEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryRn.setStatus("current")
_CucsMgmtPmonEntryExitSignal_Type = Gauge32
_CucsMgmtPmonEntryExitSignal_Object = MibTableColumn
cucsMgmtPmonEntryExitSignal = _CucsMgmtPmonEntryExitSignal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 4),
    _CucsMgmtPmonEntryExitSignal_Type()
)
cucsMgmtPmonEntryExitSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryExitSignal.setStatus("current")
_CucsMgmtPmonEntryFullPathname_Type = SnmpAdminString
_CucsMgmtPmonEntryFullPathname_Object = MibTableColumn
cucsMgmtPmonEntryFullPathname = _CucsMgmtPmonEntryFullPathname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 5),
    _CucsMgmtPmonEntryFullPathname_Type()
)
cucsMgmtPmonEntryFullPathname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryFullPathname.setStatus("current")
_CucsMgmtPmonEntryHeapSize_Type = Unsigned64
_CucsMgmtPmonEntryHeapSize_Object = MibTableColumn
cucsMgmtPmonEntryHeapSize = _CucsMgmtPmonEntryHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 6),
    _CucsMgmtPmonEntryHeapSize_Type()
)
cucsMgmtPmonEntryHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryHeapSize.setStatus("current")
_CucsMgmtPmonEntryHeapSize16Gb_Type = Unsigned64
_CucsMgmtPmonEntryHeapSize16Gb_Object = MibTableColumn
cucsMgmtPmonEntryHeapSize16Gb = _CucsMgmtPmonEntryHeapSize16Gb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 7),
    _CucsMgmtPmonEntryHeapSize16Gb_Type()
)
cucsMgmtPmonEntryHeapSize16Gb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryHeapSize16Gb.setStatus("current")
_CucsMgmtPmonEntryLastExitCode_Type = Gauge32
_CucsMgmtPmonEntryLastExitCode_Object = MibTableColumn
cucsMgmtPmonEntryLastExitCode = _CucsMgmtPmonEntryLastExitCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 8),
    _CucsMgmtPmonEntryLastExitCode_Type()
)
cucsMgmtPmonEntryLastExitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryLastExitCode.setStatus("current")
_CucsMgmtPmonEntryMaxRetries_Type = Gauge32
_CucsMgmtPmonEntryMaxRetries_Object = MibTableColumn
cucsMgmtPmonEntryMaxRetries = _CucsMgmtPmonEntryMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 9),
    _CucsMgmtPmonEntryMaxRetries_Type()
)
cucsMgmtPmonEntryMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryMaxRetries.setStatus("current")
_CucsMgmtPmonEntryName_Type = SnmpAdminString
_CucsMgmtPmonEntryName_Object = MibTableColumn
cucsMgmtPmonEntryName = _CucsMgmtPmonEntryName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 10),
    _CucsMgmtPmonEntryName_Type()
)
cucsMgmtPmonEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryName.setStatus("current")
_CucsMgmtPmonEntryRetries_Type = Gauge32
_CucsMgmtPmonEntryRetries_Object = MibTableColumn
cucsMgmtPmonEntryRetries = _CucsMgmtPmonEntryRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 11),
    _CucsMgmtPmonEntryRetries_Type()
)
cucsMgmtPmonEntryRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryRetries.setStatus("current")
_CucsMgmtPmonEntrySpuriousRetries_Type = Gauge32
_CucsMgmtPmonEntrySpuriousRetries_Object = MibTableColumn
cucsMgmtPmonEntrySpuriousRetries = _CucsMgmtPmonEntrySpuriousRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 12),
    _CucsMgmtPmonEntrySpuriousRetries_Type()
)
cucsMgmtPmonEntrySpuriousRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntrySpuriousRetries.setStatus("current")
_CucsMgmtPmonEntryState_Type = CucsMgmtPmonEntryState
_CucsMgmtPmonEntryState_Object = MibTableColumn
cucsMgmtPmonEntryState = _CucsMgmtPmonEntryState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 13),
    _CucsMgmtPmonEntryState_Type()
)
cucsMgmtPmonEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryState.setStatus("current")
_CucsMgmtPmonEntrySwitchId_Type = CucsNetworkSwitchId
_CucsMgmtPmonEntrySwitchId_Object = MibTableColumn
cucsMgmtPmonEntrySwitchId = _CucsMgmtPmonEntrySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 14),
    _CucsMgmtPmonEntrySwitchId_Type()
)
cucsMgmtPmonEntrySwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntrySwitchId.setStatus("current")
_CucsMgmtPmonEntryWorkingDirectory_Type = SnmpAdminString
_CucsMgmtPmonEntryWorkingDirectory_Object = MibTableColumn
cucsMgmtPmonEntryWorkingDirectory = _CucsMgmtPmonEntryWorkingDirectory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 14, 1, 15),
    _CucsMgmtPmonEntryWorkingDirectory_Type()
)
cucsMgmtPmonEntryWorkingDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtPmonEntryWorkingDirectory.setStatus("current")
_CucsMgmtBackupFsmTable_Object = MibTable
cucsMgmtBackupFsmTable = _CucsMgmtBackupFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 15)
)
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmTable.setStatus("current")
_CucsMgmtBackupFsmEntry_Object = MibTableRow
cucsMgmtBackupFsmEntry = _CucsMgmtBackupFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 15, 1)
)
cucsMgmtBackupFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtBackupFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmEntry.setStatus("current")
_CucsMgmtBackupFsmInstanceId_Type = CucsManagedObjectId
_CucsMgmtBackupFsmInstanceId_Object = MibTableColumn
cucsMgmtBackupFsmInstanceId = _CucsMgmtBackupFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 15, 1, 1),
    _CucsMgmtBackupFsmInstanceId_Type()
)
cucsMgmtBackupFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmInstanceId.setStatus("current")
_CucsMgmtBackupFsmDn_Type = CucsManagedObjectDn
_CucsMgmtBackupFsmDn_Object = MibTableColumn
cucsMgmtBackupFsmDn = _CucsMgmtBackupFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 15, 1, 2),
    _CucsMgmtBackupFsmDn_Type()
)
cucsMgmtBackupFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmDn.setStatus("current")
_CucsMgmtBackupFsmRn_Type = SnmpAdminString
_CucsMgmtBackupFsmRn_Object = MibTableColumn
cucsMgmtBackupFsmRn = _CucsMgmtBackupFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 15, 1, 3),
    _CucsMgmtBackupFsmRn_Type()
)
cucsMgmtBackupFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmRn.setStatus("current")
_CucsMgmtBackupFsmCompletionTime_Type = DateAndTime
_CucsMgmtBackupFsmCompletionTime_Object = MibTableColumn
cucsMgmtBackupFsmCompletionTime = _CucsMgmtBackupFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 15, 1, 4),
    _CucsMgmtBackupFsmCompletionTime_Type()
)
cucsMgmtBackupFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmCompletionTime.setStatus("current")
_CucsMgmtBackupFsmCurrentFsm_Type = CucsMgmtBackupFsmCurrentFsm
_CucsMgmtBackupFsmCurrentFsm_Object = MibTableColumn
cucsMgmtBackupFsmCurrentFsm = _CucsMgmtBackupFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 15, 1, 5),
    _CucsMgmtBackupFsmCurrentFsm_Type()
)
cucsMgmtBackupFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmCurrentFsm.setStatus("current")
_CucsMgmtBackupFsmDescrData_Type = SnmpAdminString
_CucsMgmtBackupFsmDescrData_Object = MibTableColumn
cucsMgmtBackupFsmDescrData = _CucsMgmtBackupFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 15, 1, 6),
    _CucsMgmtBackupFsmDescrData_Type()
)
cucsMgmtBackupFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmDescrData.setStatus("current")
_CucsMgmtBackupFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtBackupFsmFsmStatus_Object = MibTableColumn
cucsMgmtBackupFsmFsmStatus = _CucsMgmtBackupFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 15, 1, 7),
    _CucsMgmtBackupFsmFsmStatus_Type()
)
cucsMgmtBackupFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmFsmStatus.setStatus("current")
_CucsMgmtBackupFsmProgress_Type = Gauge32
_CucsMgmtBackupFsmProgress_Object = MibTableColumn
cucsMgmtBackupFsmProgress = _CucsMgmtBackupFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 15, 1, 8),
    _CucsMgmtBackupFsmProgress_Type()
)
cucsMgmtBackupFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmProgress.setStatus("current")
_CucsMgmtBackupFsmRmtErrCode_Type = Gauge32
_CucsMgmtBackupFsmRmtErrCode_Object = MibTableColumn
cucsMgmtBackupFsmRmtErrCode = _CucsMgmtBackupFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 15, 1, 9),
    _CucsMgmtBackupFsmRmtErrCode_Type()
)
cucsMgmtBackupFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmRmtErrCode.setStatus("current")
_CucsMgmtBackupFsmRmtErrDescr_Type = SnmpAdminString
_CucsMgmtBackupFsmRmtErrDescr_Object = MibTableColumn
cucsMgmtBackupFsmRmtErrDescr = _CucsMgmtBackupFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 15, 1, 10),
    _CucsMgmtBackupFsmRmtErrDescr_Type()
)
cucsMgmtBackupFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmRmtErrDescr.setStatus("current")
_CucsMgmtBackupFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtBackupFsmRmtRslt_Object = MibTableColumn
cucsMgmtBackupFsmRmtRslt = _CucsMgmtBackupFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 15, 1, 11),
    _CucsMgmtBackupFsmRmtRslt_Type()
)
cucsMgmtBackupFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmRmtRslt.setStatus("current")
_CucsMgmtBackupFsmStageTable_Object = MibTable
cucsMgmtBackupFsmStageTable = _CucsMgmtBackupFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 16)
)
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmStageTable.setStatus("current")
_CucsMgmtBackupFsmStageEntry_Object = MibTableRow
cucsMgmtBackupFsmStageEntry = _CucsMgmtBackupFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 16, 1)
)
cucsMgmtBackupFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtBackupFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmStageEntry.setStatus("current")
_CucsMgmtBackupFsmStageInstanceId_Type = CucsManagedObjectId
_CucsMgmtBackupFsmStageInstanceId_Object = MibTableColumn
cucsMgmtBackupFsmStageInstanceId = _CucsMgmtBackupFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 16, 1, 1),
    _CucsMgmtBackupFsmStageInstanceId_Type()
)
cucsMgmtBackupFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmStageInstanceId.setStatus("current")
_CucsMgmtBackupFsmStageDn_Type = CucsManagedObjectDn
_CucsMgmtBackupFsmStageDn_Object = MibTableColumn
cucsMgmtBackupFsmStageDn = _CucsMgmtBackupFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 16, 1, 2),
    _CucsMgmtBackupFsmStageDn_Type()
)
cucsMgmtBackupFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmStageDn.setStatus("current")
_CucsMgmtBackupFsmStageRn_Type = SnmpAdminString
_CucsMgmtBackupFsmStageRn_Object = MibTableColumn
cucsMgmtBackupFsmStageRn = _CucsMgmtBackupFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 16, 1, 3),
    _CucsMgmtBackupFsmStageRn_Type()
)
cucsMgmtBackupFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmStageRn.setStatus("current")
_CucsMgmtBackupFsmStageDescrData_Type = SnmpAdminString
_CucsMgmtBackupFsmStageDescrData_Object = MibTableColumn
cucsMgmtBackupFsmStageDescrData = _CucsMgmtBackupFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 16, 1, 4),
    _CucsMgmtBackupFsmStageDescrData_Type()
)
cucsMgmtBackupFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmStageDescrData.setStatus("current")
_CucsMgmtBackupFsmStageLastUpdateTime_Type = DateAndTime
_CucsMgmtBackupFsmStageLastUpdateTime_Object = MibTableColumn
cucsMgmtBackupFsmStageLastUpdateTime = _CucsMgmtBackupFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 16, 1, 5),
    _CucsMgmtBackupFsmStageLastUpdateTime_Type()
)
cucsMgmtBackupFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmStageLastUpdateTime.setStatus("current")
_CucsMgmtBackupFsmStageName_Type = CucsMgmtBackupFsmStageName
_CucsMgmtBackupFsmStageName_Object = MibTableColumn
cucsMgmtBackupFsmStageName = _CucsMgmtBackupFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 16, 1, 6),
    _CucsMgmtBackupFsmStageName_Type()
)
cucsMgmtBackupFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmStageName.setStatus("current")
_CucsMgmtBackupFsmStageOrder_Type = Gauge32
_CucsMgmtBackupFsmStageOrder_Object = MibTableColumn
cucsMgmtBackupFsmStageOrder = _CucsMgmtBackupFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 16, 1, 7),
    _CucsMgmtBackupFsmStageOrder_Type()
)
cucsMgmtBackupFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmStageOrder.setStatus("current")
_CucsMgmtBackupFsmStageRetry_Type = Gauge32
_CucsMgmtBackupFsmStageRetry_Object = MibTableColumn
cucsMgmtBackupFsmStageRetry = _CucsMgmtBackupFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 16, 1, 8),
    _CucsMgmtBackupFsmStageRetry_Type()
)
cucsMgmtBackupFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmStageRetry.setStatus("current")
_CucsMgmtBackupFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtBackupFsmStageStageStatus_Object = MibTableColumn
cucsMgmtBackupFsmStageStageStatus = _CucsMgmtBackupFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 16, 1, 9),
    _CucsMgmtBackupFsmStageStageStatus_Type()
)
cucsMgmtBackupFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupFsmStageStageStatus.setStatus("current")
_CucsMgmtBackupPolicyTable_Object = MibTable
cucsMgmtBackupPolicyTable = _CucsMgmtBackupPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17)
)
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyTable.setStatus("current")
_CucsMgmtBackupPolicyEntry_Object = MibTableRow
cucsMgmtBackupPolicyEntry = _CucsMgmtBackupPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1)
)
cucsMgmtBackupPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtBackupPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyEntry.setStatus("current")
_CucsMgmtBackupPolicyInstanceId_Type = CucsManagedObjectId
_CucsMgmtBackupPolicyInstanceId_Object = MibTableColumn
cucsMgmtBackupPolicyInstanceId = _CucsMgmtBackupPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 1),
    _CucsMgmtBackupPolicyInstanceId_Type()
)
cucsMgmtBackupPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyInstanceId.setStatus("current")
_CucsMgmtBackupPolicyDn_Type = CucsManagedObjectDn
_CucsMgmtBackupPolicyDn_Object = MibTableColumn
cucsMgmtBackupPolicyDn = _CucsMgmtBackupPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 2),
    _CucsMgmtBackupPolicyDn_Type()
)
cucsMgmtBackupPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyDn.setStatus("current")
_CucsMgmtBackupPolicyRn_Type = SnmpAdminString
_CucsMgmtBackupPolicyRn_Object = MibTableColumn
cucsMgmtBackupPolicyRn = _CucsMgmtBackupPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 3),
    _CucsMgmtBackupPolicyRn_Type()
)
cucsMgmtBackupPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyRn.setStatus("current")
_CucsMgmtBackupPolicyAdminState_Type = CucsMgmtExportPolicyAdminState
_CucsMgmtBackupPolicyAdminState_Object = MibTableColumn
cucsMgmtBackupPolicyAdminState = _CucsMgmtBackupPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 4),
    _CucsMgmtBackupPolicyAdminState_Type()
)
cucsMgmtBackupPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyAdminState.setStatus("current")
_CucsMgmtBackupPolicyDescr_Type = SnmpAdminString
_CucsMgmtBackupPolicyDescr_Object = MibTableColumn
cucsMgmtBackupPolicyDescr = _CucsMgmtBackupPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 5),
    _CucsMgmtBackupPolicyDescr_Type()
)
cucsMgmtBackupPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyDescr.setStatus("current")
_CucsMgmtBackupPolicyFsmDescr_Type = SnmpAdminString
_CucsMgmtBackupPolicyFsmDescr_Object = MibTableColumn
cucsMgmtBackupPolicyFsmDescr = _CucsMgmtBackupPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 6),
    _CucsMgmtBackupPolicyFsmDescr_Type()
)
cucsMgmtBackupPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmDescr.setStatus("current")
_CucsMgmtBackupPolicyFsmPrev_Type = SnmpAdminString
_CucsMgmtBackupPolicyFsmPrev_Object = MibTableColumn
cucsMgmtBackupPolicyFsmPrev = _CucsMgmtBackupPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 7),
    _CucsMgmtBackupPolicyFsmPrev_Type()
)
cucsMgmtBackupPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmPrev.setStatus("current")
_CucsMgmtBackupPolicyFsmProgr_Type = Gauge32
_CucsMgmtBackupPolicyFsmProgr_Object = MibTableColumn
cucsMgmtBackupPolicyFsmProgr = _CucsMgmtBackupPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 8),
    _CucsMgmtBackupPolicyFsmProgr_Type()
)
cucsMgmtBackupPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmProgr.setStatus("current")
_CucsMgmtBackupPolicyFsmRmtInvErrCode_Type = Gauge32
_CucsMgmtBackupPolicyFsmRmtInvErrCode_Object = MibTableColumn
cucsMgmtBackupPolicyFsmRmtInvErrCode = _CucsMgmtBackupPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 9),
    _CucsMgmtBackupPolicyFsmRmtInvErrCode_Type()
)
cucsMgmtBackupPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmRmtInvErrCode.setStatus("current")
_CucsMgmtBackupPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsMgmtBackupPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cucsMgmtBackupPolicyFsmRmtInvErrDescr = _CucsMgmtBackupPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 10),
    _CucsMgmtBackupPolicyFsmRmtInvErrDescr_Type()
)
cucsMgmtBackupPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmRmtInvErrDescr.setStatus("current")
_CucsMgmtBackupPolicyFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtBackupPolicyFsmRmtInvRslt_Object = MibTableColumn
cucsMgmtBackupPolicyFsmRmtInvRslt = _CucsMgmtBackupPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 11),
    _CucsMgmtBackupPolicyFsmRmtInvRslt_Type()
)
cucsMgmtBackupPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmRmtInvRslt.setStatus("current")
_CucsMgmtBackupPolicyFsmStageDescr_Type = SnmpAdminString
_CucsMgmtBackupPolicyFsmStageDescr_Object = MibTableColumn
cucsMgmtBackupPolicyFsmStageDescr = _CucsMgmtBackupPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 12),
    _CucsMgmtBackupPolicyFsmStageDescr_Type()
)
cucsMgmtBackupPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmStageDescr.setStatus("current")
_CucsMgmtBackupPolicyFsmStamp_Type = DateAndTime
_CucsMgmtBackupPolicyFsmStamp_Object = MibTableColumn
cucsMgmtBackupPolicyFsmStamp = _CucsMgmtBackupPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 13),
    _CucsMgmtBackupPolicyFsmStamp_Type()
)
cucsMgmtBackupPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmStamp.setStatus("current")
_CucsMgmtBackupPolicyFsmStatus_Type = SnmpAdminString
_CucsMgmtBackupPolicyFsmStatus_Object = MibTableColumn
cucsMgmtBackupPolicyFsmStatus = _CucsMgmtBackupPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 14),
    _CucsMgmtBackupPolicyFsmStatus_Type()
)
cucsMgmtBackupPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmStatus.setStatus("current")
_CucsMgmtBackupPolicyFsmTry_Type = Gauge32
_CucsMgmtBackupPolicyFsmTry_Object = MibTableColumn
cucsMgmtBackupPolicyFsmTry = _CucsMgmtBackupPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 15),
    _CucsMgmtBackupPolicyFsmTry_Type()
)
cucsMgmtBackupPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmTry.setStatus("current")
_CucsMgmtBackupPolicyHost_Type = SnmpAdminString
_CucsMgmtBackupPolicyHost_Object = MibTableColumn
cucsMgmtBackupPolicyHost = _CucsMgmtBackupPolicyHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 16),
    _CucsMgmtBackupPolicyHost_Type()
)
cucsMgmtBackupPolicyHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyHost.setStatus("current")
_CucsMgmtBackupPolicyIntId_Type = SnmpAdminString
_CucsMgmtBackupPolicyIntId_Object = MibTableColumn
cucsMgmtBackupPolicyIntId = _CucsMgmtBackupPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 17),
    _CucsMgmtBackupPolicyIntId_Type()
)
cucsMgmtBackupPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyIntId.setStatus("current")
_CucsMgmtBackupPolicyLastBackup_Type = DateAndTime
_CucsMgmtBackupPolicyLastBackup_Object = MibTableColumn
cucsMgmtBackupPolicyLastBackup = _CucsMgmtBackupPolicyLastBackup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 18),
    _CucsMgmtBackupPolicyLastBackup_Type()
)
cucsMgmtBackupPolicyLastBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyLastBackup.setStatus("current")
_CucsMgmtBackupPolicyMaxFiles_Type = Gauge32
_CucsMgmtBackupPolicyMaxFiles_Object = MibTableColumn
cucsMgmtBackupPolicyMaxFiles = _CucsMgmtBackupPolicyMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 19),
    _CucsMgmtBackupPolicyMaxFiles_Type()
)
cucsMgmtBackupPolicyMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyMaxFiles.setStatus("current")
_CucsMgmtBackupPolicyName_Type = SnmpAdminString
_CucsMgmtBackupPolicyName_Object = MibTableColumn
cucsMgmtBackupPolicyName = _CucsMgmtBackupPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 20),
    _CucsMgmtBackupPolicyName_Type()
)
cucsMgmtBackupPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyName.setStatus("current")
_CucsMgmtBackupPolicyPolicyLevel_Type = Gauge32
_CucsMgmtBackupPolicyPolicyLevel_Object = MibTableColumn
cucsMgmtBackupPolicyPolicyLevel = _CucsMgmtBackupPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 21),
    _CucsMgmtBackupPolicyPolicyLevel_Type()
)
cucsMgmtBackupPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyPolicyLevel.setStatus("current")
_CucsMgmtBackupPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsMgmtBackupPolicyPolicyOwner_Object = MibTableColumn
cucsMgmtBackupPolicyPolicyOwner = _CucsMgmtBackupPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 22),
    _CucsMgmtBackupPolicyPolicyOwner_Type()
)
cucsMgmtBackupPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyPolicyOwner.setStatus("current")
_CucsMgmtBackupPolicyProto_Type = CucsMgmtExportPolicyProto
_CucsMgmtBackupPolicyProto_Object = MibTableColumn
cucsMgmtBackupPolicyProto = _CucsMgmtBackupPolicyProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 23),
    _CucsMgmtBackupPolicyProto_Type()
)
cucsMgmtBackupPolicyProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyProto.setStatus("current")
_CucsMgmtBackupPolicyPwd_Type = SnmpAdminString
_CucsMgmtBackupPolicyPwd_Object = MibTableColumn
cucsMgmtBackupPolicyPwd = _CucsMgmtBackupPolicyPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 24),
    _CucsMgmtBackupPolicyPwd_Type()
)
cucsMgmtBackupPolicyPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyPwd.setStatus("current")
_CucsMgmtBackupPolicyRemoteFile_Type = SnmpAdminString
_CucsMgmtBackupPolicyRemoteFile_Object = MibTableColumn
cucsMgmtBackupPolicyRemoteFile = _CucsMgmtBackupPolicyRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 25),
    _CucsMgmtBackupPolicyRemoteFile_Type()
)
cucsMgmtBackupPolicyRemoteFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyRemoteFile.setStatus("current")
_CucsMgmtBackupPolicySchedule_Type = CucsMgmtBackupInterval
_CucsMgmtBackupPolicySchedule_Object = MibTableColumn
cucsMgmtBackupPolicySchedule = _CucsMgmtBackupPolicySchedule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 26),
    _CucsMgmtBackupPolicySchedule_Type()
)
cucsMgmtBackupPolicySchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicySchedule.setStatus("current")
_CucsMgmtBackupPolicyUser_Type = SnmpAdminString
_CucsMgmtBackupPolicyUser_Object = MibTableColumn
cucsMgmtBackupPolicyUser = _CucsMgmtBackupPolicyUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 17, 1, 27),
    _CucsMgmtBackupPolicyUser_Type()
)
cucsMgmtBackupPolicyUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyUser.setStatus("current")
_CucsMgmtBackupPolicyFsmTable_Object = MibTable
cucsMgmtBackupPolicyFsmTable = _CucsMgmtBackupPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 18)
)
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmTable.setStatus("current")
_CucsMgmtBackupPolicyFsmEntry_Object = MibTableRow
cucsMgmtBackupPolicyFsmEntry = _CucsMgmtBackupPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 18, 1)
)
cucsMgmtBackupPolicyFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtBackupPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmEntry.setStatus("current")
_CucsMgmtBackupPolicyFsmInstanceId_Type = CucsManagedObjectId
_CucsMgmtBackupPolicyFsmInstanceId_Object = MibTableColumn
cucsMgmtBackupPolicyFsmInstanceId = _CucsMgmtBackupPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 18, 1, 1),
    _CucsMgmtBackupPolicyFsmInstanceId_Type()
)
cucsMgmtBackupPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmInstanceId.setStatus("current")
_CucsMgmtBackupPolicyFsmDn_Type = CucsManagedObjectDn
_CucsMgmtBackupPolicyFsmDn_Object = MibTableColumn
cucsMgmtBackupPolicyFsmDn = _CucsMgmtBackupPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 18, 1, 2),
    _CucsMgmtBackupPolicyFsmDn_Type()
)
cucsMgmtBackupPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmDn.setStatus("current")
_CucsMgmtBackupPolicyFsmRn_Type = SnmpAdminString
_CucsMgmtBackupPolicyFsmRn_Object = MibTableColumn
cucsMgmtBackupPolicyFsmRn = _CucsMgmtBackupPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 18, 1, 3),
    _CucsMgmtBackupPolicyFsmRn_Type()
)
cucsMgmtBackupPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmRn.setStatus("current")
_CucsMgmtBackupPolicyFsmCompletionTime_Type = DateAndTime
_CucsMgmtBackupPolicyFsmCompletionTime_Object = MibTableColumn
cucsMgmtBackupPolicyFsmCompletionTime = _CucsMgmtBackupPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 18, 1, 4),
    _CucsMgmtBackupPolicyFsmCompletionTime_Type()
)
cucsMgmtBackupPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmCompletionTime.setStatus("current")
_CucsMgmtBackupPolicyFsmCurrentFsm_Type = CucsMgmtBackupPolicyFsmCurrentFsm
_CucsMgmtBackupPolicyFsmCurrentFsm_Object = MibTableColumn
cucsMgmtBackupPolicyFsmCurrentFsm = _CucsMgmtBackupPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 18, 1, 5),
    _CucsMgmtBackupPolicyFsmCurrentFsm_Type()
)
cucsMgmtBackupPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmCurrentFsm.setStatus("current")
_CucsMgmtBackupPolicyFsmDescrData_Type = SnmpAdminString
_CucsMgmtBackupPolicyFsmDescrData_Object = MibTableColumn
cucsMgmtBackupPolicyFsmDescrData = _CucsMgmtBackupPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 18, 1, 6),
    _CucsMgmtBackupPolicyFsmDescrData_Type()
)
cucsMgmtBackupPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmDescrData.setStatus("current")
_CucsMgmtBackupPolicyFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtBackupPolicyFsmFsmStatus_Object = MibTableColumn
cucsMgmtBackupPolicyFsmFsmStatus = _CucsMgmtBackupPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 18, 1, 7),
    _CucsMgmtBackupPolicyFsmFsmStatus_Type()
)
cucsMgmtBackupPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmFsmStatus.setStatus("current")
_CucsMgmtBackupPolicyFsmProgress_Type = Gauge32
_CucsMgmtBackupPolicyFsmProgress_Object = MibTableColumn
cucsMgmtBackupPolicyFsmProgress = _CucsMgmtBackupPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 18, 1, 8),
    _CucsMgmtBackupPolicyFsmProgress_Type()
)
cucsMgmtBackupPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmProgress.setStatus("current")
_CucsMgmtBackupPolicyFsmRmtErrCode_Type = Gauge32
_CucsMgmtBackupPolicyFsmRmtErrCode_Object = MibTableColumn
cucsMgmtBackupPolicyFsmRmtErrCode = _CucsMgmtBackupPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 18, 1, 9),
    _CucsMgmtBackupPolicyFsmRmtErrCode_Type()
)
cucsMgmtBackupPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmRmtErrCode.setStatus("current")
_CucsMgmtBackupPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CucsMgmtBackupPolicyFsmRmtErrDescr_Object = MibTableColumn
cucsMgmtBackupPolicyFsmRmtErrDescr = _CucsMgmtBackupPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 18, 1, 10),
    _CucsMgmtBackupPolicyFsmRmtErrDescr_Type()
)
cucsMgmtBackupPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmRmtErrDescr.setStatus("current")
_CucsMgmtBackupPolicyFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtBackupPolicyFsmRmtRslt_Object = MibTableColumn
cucsMgmtBackupPolicyFsmRmtRslt = _CucsMgmtBackupPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 18, 1, 11),
    _CucsMgmtBackupPolicyFsmRmtRslt_Type()
)
cucsMgmtBackupPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmRmtRslt.setStatus("current")
_CucsMgmtBackupPolicyFsmStageTable_Object = MibTable
cucsMgmtBackupPolicyFsmStageTable = _CucsMgmtBackupPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 19)
)
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmStageTable.setStatus("current")
_CucsMgmtBackupPolicyFsmStageEntry_Object = MibTableRow
cucsMgmtBackupPolicyFsmStageEntry = _CucsMgmtBackupPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 19, 1)
)
cucsMgmtBackupPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtBackupPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmStageEntry.setStatus("current")
_CucsMgmtBackupPolicyFsmStageInstanceId_Type = CucsManagedObjectId
_CucsMgmtBackupPolicyFsmStageInstanceId_Object = MibTableColumn
cucsMgmtBackupPolicyFsmStageInstanceId = _CucsMgmtBackupPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 19, 1, 1),
    _CucsMgmtBackupPolicyFsmStageInstanceId_Type()
)
cucsMgmtBackupPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmStageInstanceId.setStatus("current")
_CucsMgmtBackupPolicyFsmStageDn_Type = CucsManagedObjectDn
_CucsMgmtBackupPolicyFsmStageDn_Object = MibTableColumn
cucsMgmtBackupPolicyFsmStageDn = _CucsMgmtBackupPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 19, 1, 2),
    _CucsMgmtBackupPolicyFsmStageDn_Type()
)
cucsMgmtBackupPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmStageDn.setStatus("current")
_CucsMgmtBackupPolicyFsmStageRn_Type = SnmpAdminString
_CucsMgmtBackupPolicyFsmStageRn_Object = MibTableColumn
cucsMgmtBackupPolicyFsmStageRn = _CucsMgmtBackupPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 19, 1, 3),
    _CucsMgmtBackupPolicyFsmStageRn_Type()
)
cucsMgmtBackupPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmStageRn.setStatus("current")
_CucsMgmtBackupPolicyFsmStageDescrData_Type = SnmpAdminString
_CucsMgmtBackupPolicyFsmStageDescrData_Object = MibTableColumn
cucsMgmtBackupPolicyFsmStageDescrData = _CucsMgmtBackupPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 19, 1, 4),
    _CucsMgmtBackupPolicyFsmStageDescrData_Type()
)
cucsMgmtBackupPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmStageDescrData.setStatus("current")
_CucsMgmtBackupPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CucsMgmtBackupPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cucsMgmtBackupPolicyFsmStageLastUpdateTime = _CucsMgmtBackupPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 19, 1, 5),
    _CucsMgmtBackupPolicyFsmStageLastUpdateTime_Type()
)
cucsMgmtBackupPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmStageLastUpdateTime.setStatus("current")
_CucsMgmtBackupPolicyFsmStageName_Type = CucsMgmtBackupPolicyFsmStageName
_CucsMgmtBackupPolicyFsmStageName_Object = MibTableColumn
cucsMgmtBackupPolicyFsmStageName = _CucsMgmtBackupPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 19, 1, 6),
    _CucsMgmtBackupPolicyFsmStageName_Type()
)
cucsMgmtBackupPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmStageName.setStatus("current")
_CucsMgmtBackupPolicyFsmStageOrder_Type = Gauge32
_CucsMgmtBackupPolicyFsmStageOrder_Object = MibTableColumn
cucsMgmtBackupPolicyFsmStageOrder = _CucsMgmtBackupPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 19, 1, 7),
    _CucsMgmtBackupPolicyFsmStageOrder_Type()
)
cucsMgmtBackupPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmStageOrder.setStatus("current")
_CucsMgmtBackupPolicyFsmStageRetry_Type = Gauge32
_CucsMgmtBackupPolicyFsmStageRetry_Object = MibTableColumn
cucsMgmtBackupPolicyFsmStageRetry = _CucsMgmtBackupPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 19, 1, 8),
    _CucsMgmtBackupPolicyFsmStageRetry_Type()
)
cucsMgmtBackupPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmStageRetry.setStatus("current")
_CucsMgmtBackupPolicyFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtBackupPolicyFsmStageStageStatus_Object = MibTableColumn
cucsMgmtBackupPolicyFsmStageStageStatus = _CucsMgmtBackupPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 19, 1, 9),
    _CucsMgmtBackupPolicyFsmStageStageStatus_Type()
)
cucsMgmtBackupPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyFsmStageStageStatus.setStatus("current")
_CucsMgmtCfgExportPolicyTable_Object = MibTable
cucsMgmtCfgExportPolicyTable = _CucsMgmtCfgExportPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20)
)
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyTable.setStatus("current")
_CucsMgmtCfgExportPolicyEntry_Object = MibTableRow
cucsMgmtCfgExportPolicyEntry = _CucsMgmtCfgExportPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1)
)
cucsMgmtCfgExportPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtCfgExportPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyEntry.setStatus("current")
_CucsMgmtCfgExportPolicyInstanceId_Type = CucsManagedObjectId
_CucsMgmtCfgExportPolicyInstanceId_Object = MibTableColumn
cucsMgmtCfgExportPolicyInstanceId = _CucsMgmtCfgExportPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 1),
    _CucsMgmtCfgExportPolicyInstanceId_Type()
)
cucsMgmtCfgExportPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyInstanceId.setStatus("current")
_CucsMgmtCfgExportPolicyDn_Type = CucsManagedObjectDn
_CucsMgmtCfgExportPolicyDn_Object = MibTableColumn
cucsMgmtCfgExportPolicyDn = _CucsMgmtCfgExportPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 2),
    _CucsMgmtCfgExportPolicyDn_Type()
)
cucsMgmtCfgExportPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyDn.setStatus("current")
_CucsMgmtCfgExportPolicyRn_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyRn_Object = MibTableColumn
cucsMgmtCfgExportPolicyRn = _CucsMgmtCfgExportPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 3),
    _CucsMgmtCfgExportPolicyRn_Type()
)
cucsMgmtCfgExportPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyRn.setStatus("current")
_CucsMgmtCfgExportPolicyAdminState_Type = CucsMgmtExportPolicyAdminState
_CucsMgmtCfgExportPolicyAdminState_Object = MibTableColumn
cucsMgmtCfgExportPolicyAdminState = _CucsMgmtCfgExportPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 4),
    _CucsMgmtCfgExportPolicyAdminState_Type()
)
cucsMgmtCfgExportPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyAdminState.setStatus("current")
_CucsMgmtCfgExportPolicyDescr_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyDescr_Object = MibTableColumn
cucsMgmtCfgExportPolicyDescr = _CucsMgmtCfgExportPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 5),
    _CucsMgmtCfgExportPolicyDescr_Type()
)
cucsMgmtCfgExportPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyDescr.setStatus("current")
_CucsMgmtCfgExportPolicyFsmDescr_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyFsmDescr_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmDescr = _CucsMgmtCfgExportPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 6),
    _CucsMgmtCfgExportPolicyFsmDescr_Type()
)
cucsMgmtCfgExportPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmDescr.setStatus("current")
_CucsMgmtCfgExportPolicyFsmPrev_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyFsmPrev_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmPrev = _CucsMgmtCfgExportPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 7),
    _CucsMgmtCfgExportPolicyFsmPrev_Type()
)
cucsMgmtCfgExportPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmPrev.setStatus("current")
_CucsMgmtCfgExportPolicyFsmProgr_Type = Gauge32
_CucsMgmtCfgExportPolicyFsmProgr_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmProgr = _CucsMgmtCfgExportPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 8),
    _CucsMgmtCfgExportPolicyFsmProgr_Type()
)
cucsMgmtCfgExportPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmProgr.setStatus("current")
_CucsMgmtCfgExportPolicyFsmRmtInvErrCode_Type = Gauge32
_CucsMgmtCfgExportPolicyFsmRmtInvErrCode_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmRmtInvErrCode = _CucsMgmtCfgExportPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 9),
    _CucsMgmtCfgExportPolicyFsmRmtInvErrCode_Type()
)
cucsMgmtCfgExportPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmRmtInvErrCode.setStatus("current")
_CucsMgmtCfgExportPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmRmtInvErrDescr = _CucsMgmtCfgExportPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 10),
    _CucsMgmtCfgExportPolicyFsmRmtInvErrDescr_Type()
)
cucsMgmtCfgExportPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmRmtInvErrDescr.setStatus("current")
_CucsMgmtCfgExportPolicyFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtCfgExportPolicyFsmRmtInvRslt_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmRmtInvRslt = _CucsMgmtCfgExportPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 11),
    _CucsMgmtCfgExportPolicyFsmRmtInvRslt_Type()
)
cucsMgmtCfgExportPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmRmtInvRslt.setStatus("current")
_CucsMgmtCfgExportPolicyFsmStageDescr_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyFsmStageDescr_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmStageDescr = _CucsMgmtCfgExportPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 12),
    _CucsMgmtCfgExportPolicyFsmStageDescr_Type()
)
cucsMgmtCfgExportPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmStageDescr.setStatus("current")
_CucsMgmtCfgExportPolicyFsmStamp_Type = DateAndTime
_CucsMgmtCfgExportPolicyFsmStamp_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmStamp = _CucsMgmtCfgExportPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 13),
    _CucsMgmtCfgExportPolicyFsmStamp_Type()
)
cucsMgmtCfgExportPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmStamp.setStatus("current")
_CucsMgmtCfgExportPolicyFsmStatus_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyFsmStatus_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmStatus = _CucsMgmtCfgExportPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 14),
    _CucsMgmtCfgExportPolicyFsmStatus_Type()
)
cucsMgmtCfgExportPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmStatus.setStatus("current")
_CucsMgmtCfgExportPolicyFsmTry_Type = Gauge32
_CucsMgmtCfgExportPolicyFsmTry_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmTry = _CucsMgmtCfgExportPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 15),
    _CucsMgmtCfgExportPolicyFsmTry_Type()
)
cucsMgmtCfgExportPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmTry.setStatus("current")
_CucsMgmtCfgExportPolicyHost_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyHost_Object = MibTableColumn
cucsMgmtCfgExportPolicyHost = _CucsMgmtCfgExportPolicyHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 16),
    _CucsMgmtCfgExportPolicyHost_Type()
)
cucsMgmtCfgExportPolicyHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyHost.setStatus("current")
_CucsMgmtCfgExportPolicyIntId_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyIntId_Object = MibTableColumn
cucsMgmtCfgExportPolicyIntId = _CucsMgmtCfgExportPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 17),
    _CucsMgmtCfgExportPolicyIntId_Type()
)
cucsMgmtCfgExportPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyIntId.setStatus("current")
_CucsMgmtCfgExportPolicyLastBackup_Type = DateAndTime
_CucsMgmtCfgExportPolicyLastBackup_Object = MibTableColumn
cucsMgmtCfgExportPolicyLastBackup = _CucsMgmtCfgExportPolicyLastBackup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 18),
    _CucsMgmtCfgExportPolicyLastBackup_Type()
)
cucsMgmtCfgExportPolicyLastBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyLastBackup.setStatus("current")
_CucsMgmtCfgExportPolicyMaxFiles_Type = Gauge32
_CucsMgmtCfgExportPolicyMaxFiles_Object = MibTableColumn
cucsMgmtCfgExportPolicyMaxFiles = _CucsMgmtCfgExportPolicyMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 19),
    _CucsMgmtCfgExportPolicyMaxFiles_Type()
)
cucsMgmtCfgExportPolicyMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyMaxFiles.setStatus("current")
_CucsMgmtCfgExportPolicyName_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyName_Object = MibTableColumn
cucsMgmtCfgExportPolicyName = _CucsMgmtCfgExportPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 20),
    _CucsMgmtCfgExportPolicyName_Type()
)
cucsMgmtCfgExportPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyName.setStatus("current")
_CucsMgmtCfgExportPolicyPolicyLevel_Type = Gauge32
_CucsMgmtCfgExportPolicyPolicyLevel_Object = MibTableColumn
cucsMgmtCfgExportPolicyPolicyLevel = _CucsMgmtCfgExportPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 21),
    _CucsMgmtCfgExportPolicyPolicyLevel_Type()
)
cucsMgmtCfgExportPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyPolicyLevel.setStatus("current")
_CucsMgmtCfgExportPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsMgmtCfgExportPolicyPolicyOwner_Object = MibTableColumn
cucsMgmtCfgExportPolicyPolicyOwner = _CucsMgmtCfgExportPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 22),
    _CucsMgmtCfgExportPolicyPolicyOwner_Type()
)
cucsMgmtCfgExportPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyPolicyOwner.setStatus("current")
_CucsMgmtCfgExportPolicyProto_Type = CucsMgmtExportPolicyProto
_CucsMgmtCfgExportPolicyProto_Object = MibTableColumn
cucsMgmtCfgExportPolicyProto = _CucsMgmtCfgExportPolicyProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 23),
    _CucsMgmtCfgExportPolicyProto_Type()
)
cucsMgmtCfgExportPolicyProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyProto.setStatus("current")
_CucsMgmtCfgExportPolicyPwd_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyPwd_Object = MibTableColumn
cucsMgmtCfgExportPolicyPwd = _CucsMgmtCfgExportPolicyPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 24),
    _CucsMgmtCfgExportPolicyPwd_Type()
)
cucsMgmtCfgExportPolicyPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyPwd.setStatus("current")
_CucsMgmtCfgExportPolicyRemoteFile_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyRemoteFile_Object = MibTableColumn
cucsMgmtCfgExportPolicyRemoteFile = _CucsMgmtCfgExportPolicyRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 25),
    _CucsMgmtCfgExportPolicyRemoteFile_Type()
)
cucsMgmtCfgExportPolicyRemoteFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyRemoteFile.setStatus("current")
_CucsMgmtCfgExportPolicySchedule_Type = CucsMgmtBackupInterval
_CucsMgmtCfgExportPolicySchedule_Object = MibTableColumn
cucsMgmtCfgExportPolicySchedule = _CucsMgmtCfgExportPolicySchedule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 26),
    _CucsMgmtCfgExportPolicySchedule_Type()
)
cucsMgmtCfgExportPolicySchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicySchedule.setStatus("current")
_CucsMgmtCfgExportPolicyUser_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyUser_Object = MibTableColumn
cucsMgmtCfgExportPolicyUser = _CucsMgmtCfgExportPolicyUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 20, 1, 27),
    _CucsMgmtCfgExportPolicyUser_Type()
)
cucsMgmtCfgExportPolicyUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyUser.setStatus("current")
_CucsMgmtCfgExportPolicyFsmTable_Object = MibTable
cucsMgmtCfgExportPolicyFsmTable = _CucsMgmtCfgExportPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 21)
)
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmTable.setStatus("current")
_CucsMgmtCfgExportPolicyFsmEntry_Object = MibTableRow
cucsMgmtCfgExportPolicyFsmEntry = _CucsMgmtCfgExportPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 21, 1)
)
cucsMgmtCfgExportPolicyFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtCfgExportPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmEntry.setStatus("current")
_CucsMgmtCfgExportPolicyFsmInstanceId_Type = CucsManagedObjectId
_CucsMgmtCfgExportPolicyFsmInstanceId_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmInstanceId = _CucsMgmtCfgExportPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 21, 1, 1),
    _CucsMgmtCfgExportPolicyFsmInstanceId_Type()
)
cucsMgmtCfgExportPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmInstanceId.setStatus("current")
_CucsMgmtCfgExportPolicyFsmDn_Type = CucsManagedObjectDn
_CucsMgmtCfgExportPolicyFsmDn_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmDn = _CucsMgmtCfgExportPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 21, 1, 2),
    _CucsMgmtCfgExportPolicyFsmDn_Type()
)
cucsMgmtCfgExportPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmDn.setStatus("current")
_CucsMgmtCfgExportPolicyFsmRn_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyFsmRn_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmRn = _CucsMgmtCfgExportPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 21, 1, 3),
    _CucsMgmtCfgExportPolicyFsmRn_Type()
)
cucsMgmtCfgExportPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmRn.setStatus("current")
_CucsMgmtCfgExportPolicyFsmCompletionTime_Type = DateAndTime
_CucsMgmtCfgExportPolicyFsmCompletionTime_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmCompletionTime = _CucsMgmtCfgExportPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 21, 1, 4),
    _CucsMgmtCfgExportPolicyFsmCompletionTime_Type()
)
cucsMgmtCfgExportPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmCompletionTime.setStatus("current")
_CucsMgmtCfgExportPolicyFsmCurrentFsm_Type = CucsMgmtCfgExportPolicyFsmCurrentFsm
_CucsMgmtCfgExportPolicyFsmCurrentFsm_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmCurrentFsm = _CucsMgmtCfgExportPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 21, 1, 5),
    _CucsMgmtCfgExportPolicyFsmCurrentFsm_Type()
)
cucsMgmtCfgExportPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmCurrentFsm.setStatus("current")
_CucsMgmtCfgExportPolicyFsmDescrData_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyFsmDescrData_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmDescrData = _CucsMgmtCfgExportPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 21, 1, 6),
    _CucsMgmtCfgExportPolicyFsmDescrData_Type()
)
cucsMgmtCfgExportPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmDescrData.setStatus("current")
_CucsMgmtCfgExportPolicyFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtCfgExportPolicyFsmFsmStatus_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmFsmStatus = _CucsMgmtCfgExportPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 21, 1, 7),
    _CucsMgmtCfgExportPolicyFsmFsmStatus_Type()
)
cucsMgmtCfgExportPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmFsmStatus.setStatus("current")
_CucsMgmtCfgExportPolicyFsmProgress_Type = Gauge32
_CucsMgmtCfgExportPolicyFsmProgress_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmProgress = _CucsMgmtCfgExportPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 21, 1, 8),
    _CucsMgmtCfgExportPolicyFsmProgress_Type()
)
cucsMgmtCfgExportPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmProgress.setStatus("current")
_CucsMgmtCfgExportPolicyFsmRmtErrCode_Type = Gauge32
_CucsMgmtCfgExportPolicyFsmRmtErrCode_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmRmtErrCode = _CucsMgmtCfgExportPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 21, 1, 9),
    _CucsMgmtCfgExportPolicyFsmRmtErrCode_Type()
)
cucsMgmtCfgExportPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmRmtErrCode.setStatus("current")
_CucsMgmtCfgExportPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyFsmRmtErrDescr_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmRmtErrDescr = _CucsMgmtCfgExportPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 21, 1, 10),
    _CucsMgmtCfgExportPolicyFsmRmtErrDescr_Type()
)
cucsMgmtCfgExportPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmRmtErrDescr.setStatus("current")
_CucsMgmtCfgExportPolicyFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtCfgExportPolicyFsmRmtRslt_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmRmtRslt = _CucsMgmtCfgExportPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 21, 1, 11),
    _CucsMgmtCfgExportPolicyFsmRmtRslt_Type()
)
cucsMgmtCfgExportPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmRmtRslt.setStatus("current")
_CucsMgmtCfgExportPolicyFsmStageTable_Object = MibTable
cucsMgmtCfgExportPolicyFsmStageTable = _CucsMgmtCfgExportPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 22)
)
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmStageTable.setStatus("current")
_CucsMgmtCfgExportPolicyFsmStageEntry_Object = MibTableRow
cucsMgmtCfgExportPolicyFsmStageEntry = _CucsMgmtCfgExportPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 22, 1)
)
cucsMgmtCfgExportPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtCfgExportPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmStageEntry.setStatus("current")
_CucsMgmtCfgExportPolicyFsmStageInstanceId_Type = CucsManagedObjectId
_CucsMgmtCfgExportPolicyFsmStageInstanceId_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmStageInstanceId = _CucsMgmtCfgExportPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 22, 1, 1),
    _CucsMgmtCfgExportPolicyFsmStageInstanceId_Type()
)
cucsMgmtCfgExportPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmStageInstanceId.setStatus("current")
_CucsMgmtCfgExportPolicyFsmStageDn_Type = CucsManagedObjectDn
_CucsMgmtCfgExportPolicyFsmStageDn_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmStageDn = _CucsMgmtCfgExportPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 22, 1, 2),
    _CucsMgmtCfgExportPolicyFsmStageDn_Type()
)
cucsMgmtCfgExportPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmStageDn.setStatus("current")
_CucsMgmtCfgExportPolicyFsmStageRn_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyFsmStageRn_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmStageRn = _CucsMgmtCfgExportPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 22, 1, 3),
    _CucsMgmtCfgExportPolicyFsmStageRn_Type()
)
cucsMgmtCfgExportPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmStageRn.setStatus("current")
_CucsMgmtCfgExportPolicyFsmStageDescrData_Type = SnmpAdminString
_CucsMgmtCfgExportPolicyFsmStageDescrData_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmStageDescrData = _CucsMgmtCfgExportPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 22, 1, 4),
    _CucsMgmtCfgExportPolicyFsmStageDescrData_Type()
)
cucsMgmtCfgExportPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmStageDescrData.setStatus("current")
_CucsMgmtCfgExportPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CucsMgmtCfgExportPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmStageLastUpdateTime = _CucsMgmtCfgExportPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 22, 1, 5),
    _CucsMgmtCfgExportPolicyFsmStageLastUpdateTime_Type()
)
cucsMgmtCfgExportPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmStageLastUpdateTime.setStatus("current")
_CucsMgmtCfgExportPolicyFsmStageName_Type = CucsMgmtCfgExportPolicyFsmStageName
_CucsMgmtCfgExportPolicyFsmStageName_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmStageName = _CucsMgmtCfgExportPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 22, 1, 6),
    _CucsMgmtCfgExportPolicyFsmStageName_Type()
)
cucsMgmtCfgExportPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmStageName.setStatus("current")
_CucsMgmtCfgExportPolicyFsmStageOrder_Type = Gauge32
_CucsMgmtCfgExportPolicyFsmStageOrder_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmStageOrder = _CucsMgmtCfgExportPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 22, 1, 7),
    _CucsMgmtCfgExportPolicyFsmStageOrder_Type()
)
cucsMgmtCfgExportPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmStageOrder.setStatus("current")
_CucsMgmtCfgExportPolicyFsmStageRetry_Type = Gauge32
_CucsMgmtCfgExportPolicyFsmStageRetry_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmStageRetry = _CucsMgmtCfgExportPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 22, 1, 8),
    _CucsMgmtCfgExportPolicyFsmStageRetry_Type()
)
cucsMgmtCfgExportPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmStageRetry.setStatus("current")
_CucsMgmtCfgExportPolicyFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtCfgExportPolicyFsmStageStageStatus_Object = MibTableColumn
cucsMgmtCfgExportPolicyFsmStageStageStatus = _CucsMgmtCfgExportPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 22, 1, 9),
    _CucsMgmtCfgExportPolicyFsmStageStageStatus_Type()
)
cucsMgmtCfgExportPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCfgExportPolicyFsmStageStageStatus.setStatus("current")
_CucsMgmtConnectionTable_Object = MibTable
cucsMgmtConnectionTable = _CucsMgmtConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 23)
)
if mibBuilder.loadTexts:
    cucsMgmtConnectionTable.setStatus("current")
_CucsMgmtConnectionEntry_Object = MibTableRow
cucsMgmtConnectionEntry = _CucsMgmtConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 23, 1)
)
cucsMgmtConnectionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtConnectionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtConnectionEntry.setStatus("current")
_CucsMgmtConnectionInstanceId_Type = CucsManagedObjectId
_CucsMgmtConnectionInstanceId_Object = MibTableColumn
cucsMgmtConnectionInstanceId = _CucsMgmtConnectionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 23, 1, 1),
    _CucsMgmtConnectionInstanceId_Type()
)
cucsMgmtConnectionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtConnectionInstanceId.setStatus("current")
_CucsMgmtConnectionDn_Type = CucsManagedObjectDn
_CucsMgmtConnectionDn_Object = MibTableColumn
cucsMgmtConnectionDn = _CucsMgmtConnectionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 23, 1, 2),
    _CucsMgmtConnectionDn_Type()
)
cucsMgmtConnectionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtConnectionDn.setStatus("current")
_CucsMgmtConnectionRn_Type = SnmpAdminString
_CucsMgmtConnectionRn_Object = MibTableColumn
cucsMgmtConnectionRn = _CucsMgmtConnectionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 23, 1, 3),
    _CucsMgmtConnectionRn_Type()
)
cucsMgmtConnectionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtConnectionRn.setStatus("current")
_CucsMgmtConnectionAck_Type = CucsMgmtConnectionState
_CucsMgmtConnectionAck_Object = MibTableColumn
cucsMgmtConnectionAck = _CucsMgmtConnectionAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 23, 1, 4),
    _CucsMgmtConnectionAck_Type()
)
cucsMgmtConnectionAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtConnectionAck.setStatus("current")
_CucsMgmtConnectionOperState_Type = CucsMgmtConnectionState
_CucsMgmtConnectionOperState_Object = MibTableColumn
cucsMgmtConnectionOperState = _CucsMgmtConnectionOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 23, 1, 5),
    _CucsMgmtConnectionOperState_Type()
)
cucsMgmtConnectionOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtConnectionOperState.setStatus("current")
_CucsMgmtConnectionType_Type = CucsMgmtSource
_CucsMgmtConnectionType_Object = MibTableColumn
cucsMgmtConnectionType = _CucsMgmtConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 23, 1, 6),
    _CucsMgmtConnectionType_Type()
)
cucsMgmtConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtConnectionType.setStatus("current")
_CucsMgmtControllerFsmTable_Object = MibTable
cucsMgmtControllerFsmTable = _CucsMgmtControllerFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 24)
)
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmTable.setStatus("current")
_CucsMgmtControllerFsmEntry_Object = MibTableRow
cucsMgmtControllerFsmEntry = _CucsMgmtControllerFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 24, 1)
)
cucsMgmtControllerFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtControllerFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmEntry.setStatus("current")
_CucsMgmtControllerFsmInstanceId_Type = CucsManagedObjectId
_CucsMgmtControllerFsmInstanceId_Object = MibTableColumn
cucsMgmtControllerFsmInstanceId = _CucsMgmtControllerFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 24, 1, 1),
    _CucsMgmtControllerFsmInstanceId_Type()
)
cucsMgmtControllerFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmInstanceId.setStatus("current")
_CucsMgmtControllerFsmDn_Type = CucsManagedObjectDn
_CucsMgmtControllerFsmDn_Object = MibTableColumn
cucsMgmtControllerFsmDn = _CucsMgmtControllerFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 24, 1, 2),
    _CucsMgmtControllerFsmDn_Type()
)
cucsMgmtControllerFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmDn.setStatus("current")
_CucsMgmtControllerFsmRn_Type = SnmpAdminString
_CucsMgmtControllerFsmRn_Object = MibTableColumn
cucsMgmtControllerFsmRn = _CucsMgmtControllerFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 24, 1, 3),
    _CucsMgmtControllerFsmRn_Type()
)
cucsMgmtControllerFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmRn.setStatus("current")
_CucsMgmtControllerFsmCompletionTime_Type = DateAndTime
_CucsMgmtControllerFsmCompletionTime_Object = MibTableColumn
cucsMgmtControllerFsmCompletionTime = _CucsMgmtControllerFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 24, 1, 4),
    _CucsMgmtControllerFsmCompletionTime_Type()
)
cucsMgmtControllerFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmCompletionTime.setStatus("current")
_CucsMgmtControllerFsmCurrentFsm_Type = CucsMgmtControllerFsmCurrentFsm
_CucsMgmtControllerFsmCurrentFsm_Object = MibTableColumn
cucsMgmtControllerFsmCurrentFsm = _CucsMgmtControllerFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 24, 1, 5),
    _CucsMgmtControllerFsmCurrentFsm_Type()
)
cucsMgmtControllerFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmCurrentFsm.setStatus("current")
_CucsMgmtControllerFsmDescrData_Type = SnmpAdminString
_CucsMgmtControllerFsmDescrData_Object = MibTableColumn
cucsMgmtControllerFsmDescrData = _CucsMgmtControllerFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 24, 1, 6),
    _CucsMgmtControllerFsmDescrData_Type()
)
cucsMgmtControllerFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmDescrData.setStatus("current")
_CucsMgmtControllerFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtControllerFsmFsmStatus_Object = MibTableColumn
cucsMgmtControllerFsmFsmStatus = _CucsMgmtControllerFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 24, 1, 7),
    _CucsMgmtControllerFsmFsmStatus_Type()
)
cucsMgmtControllerFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmFsmStatus.setStatus("current")
_CucsMgmtControllerFsmProgress_Type = Gauge32
_CucsMgmtControllerFsmProgress_Object = MibTableColumn
cucsMgmtControllerFsmProgress = _CucsMgmtControllerFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 24, 1, 8),
    _CucsMgmtControllerFsmProgress_Type()
)
cucsMgmtControllerFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmProgress.setStatus("current")
_CucsMgmtControllerFsmRmtErrCode_Type = Gauge32
_CucsMgmtControllerFsmRmtErrCode_Object = MibTableColumn
cucsMgmtControllerFsmRmtErrCode = _CucsMgmtControllerFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 24, 1, 9),
    _CucsMgmtControllerFsmRmtErrCode_Type()
)
cucsMgmtControllerFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmRmtErrCode.setStatus("current")
_CucsMgmtControllerFsmRmtErrDescr_Type = SnmpAdminString
_CucsMgmtControllerFsmRmtErrDescr_Object = MibTableColumn
cucsMgmtControllerFsmRmtErrDescr = _CucsMgmtControllerFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 24, 1, 10),
    _CucsMgmtControllerFsmRmtErrDescr_Type()
)
cucsMgmtControllerFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmRmtErrDescr.setStatus("current")
_CucsMgmtControllerFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtControllerFsmRmtRslt_Object = MibTableColumn
cucsMgmtControllerFsmRmtRslt = _CucsMgmtControllerFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 24, 1, 11),
    _CucsMgmtControllerFsmRmtRslt_Type()
)
cucsMgmtControllerFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmRmtRslt.setStatus("current")
_CucsMgmtControllerFsmStageTable_Object = MibTable
cucsMgmtControllerFsmStageTable = _CucsMgmtControllerFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 25)
)
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmStageTable.setStatus("current")
_CucsMgmtControllerFsmStageEntry_Object = MibTableRow
cucsMgmtControllerFsmStageEntry = _CucsMgmtControllerFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 25, 1)
)
cucsMgmtControllerFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtControllerFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmStageEntry.setStatus("current")
_CucsMgmtControllerFsmStageInstanceId_Type = CucsManagedObjectId
_CucsMgmtControllerFsmStageInstanceId_Object = MibTableColumn
cucsMgmtControllerFsmStageInstanceId = _CucsMgmtControllerFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 25, 1, 1),
    _CucsMgmtControllerFsmStageInstanceId_Type()
)
cucsMgmtControllerFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmStageInstanceId.setStatus("current")
_CucsMgmtControllerFsmStageDn_Type = CucsManagedObjectDn
_CucsMgmtControllerFsmStageDn_Object = MibTableColumn
cucsMgmtControllerFsmStageDn = _CucsMgmtControllerFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 25, 1, 2),
    _CucsMgmtControllerFsmStageDn_Type()
)
cucsMgmtControllerFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmStageDn.setStatus("current")
_CucsMgmtControllerFsmStageRn_Type = SnmpAdminString
_CucsMgmtControllerFsmStageRn_Object = MibTableColumn
cucsMgmtControllerFsmStageRn = _CucsMgmtControllerFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 25, 1, 3),
    _CucsMgmtControllerFsmStageRn_Type()
)
cucsMgmtControllerFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmStageRn.setStatus("current")
_CucsMgmtControllerFsmStageDescrData_Type = SnmpAdminString
_CucsMgmtControllerFsmStageDescrData_Object = MibTableColumn
cucsMgmtControllerFsmStageDescrData = _CucsMgmtControllerFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 25, 1, 4),
    _CucsMgmtControllerFsmStageDescrData_Type()
)
cucsMgmtControllerFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmStageDescrData.setStatus("current")
_CucsMgmtControllerFsmStageLastUpdateTime_Type = DateAndTime
_CucsMgmtControllerFsmStageLastUpdateTime_Object = MibTableColumn
cucsMgmtControllerFsmStageLastUpdateTime = _CucsMgmtControllerFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 25, 1, 5),
    _CucsMgmtControllerFsmStageLastUpdateTime_Type()
)
cucsMgmtControllerFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmStageLastUpdateTime.setStatus("current")
_CucsMgmtControllerFsmStageName_Type = CucsMgmtControllerFsmStageName
_CucsMgmtControllerFsmStageName_Object = MibTableColumn
cucsMgmtControllerFsmStageName = _CucsMgmtControllerFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 25, 1, 6),
    _CucsMgmtControllerFsmStageName_Type()
)
cucsMgmtControllerFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmStageName.setStatus("current")
_CucsMgmtControllerFsmStageOrder_Type = Gauge32
_CucsMgmtControllerFsmStageOrder_Object = MibTableColumn
cucsMgmtControllerFsmStageOrder = _CucsMgmtControllerFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 25, 1, 7),
    _CucsMgmtControllerFsmStageOrder_Type()
)
cucsMgmtControllerFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmStageOrder.setStatus("current")
_CucsMgmtControllerFsmStageRetry_Type = Gauge32
_CucsMgmtControllerFsmStageRetry_Object = MibTableColumn
cucsMgmtControllerFsmStageRetry = _CucsMgmtControllerFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 25, 1, 8),
    _CucsMgmtControllerFsmStageRetry_Type()
)
cucsMgmtControllerFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmStageRetry.setStatus("current")
_CucsMgmtControllerFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtControllerFsmStageStageStatus_Object = MibTableColumn
cucsMgmtControllerFsmStageStageStatus = _CucsMgmtControllerFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 25, 1, 9),
    _CucsMgmtControllerFsmStageStageStatus_Type()
)
cucsMgmtControllerFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtControllerFsmStageStageStatus.setStatus("current")
_CucsMgmtExportPolicyFsmTable_Object = MibTable
cucsMgmtExportPolicyFsmTable = _CucsMgmtExportPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 26)
)
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmTable.setStatus("current")
_CucsMgmtExportPolicyFsmEntry_Object = MibTableRow
cucsMgmtExportPolicyFsmEntry = _CucsMgmtExportPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 26, 1)
)
cucsMgmtExportPolicyFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtExportPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmEntry.setStatus("current")
_CucsMgmtExportPolicyFsmInstanceId_Type = CucsManagedObjectId
_CucsMgmtExportPolicyFsmInstanceId_Object = MibTableColumn
cucsMgmtExportPolicyFsmInstanceId = _CucsMgmtExportPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 26, 1, 1),
    _CucsMgmtExportPolicyFsmInstanceId_Type()
)
cucsMgmtExportPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmInstanceId.setStatus("current")
_CucsMgmtExportPolicyFsmDn_Type = CucsManagedObjectDn
_CucsMgmtExportPolicyFsmDn_Object = MibTableColumn
cucsMgmtExportPolicyFsmDn = _CucsMgmtExportPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 26, 1, 2),
    _CucsMgmtExportPolicyFsmDn_Type()
)
cucsMgmtExportPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmDn.setStatus("current")
_CucsMgmtExportPolicyFsmRn_Type = SnmpAdminString
_CucsMgmtExportPolicyFsmRn_Object = MibTableColumn
cucsMgmtExportPolicyFsmRn = _CucsMgmtExportPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 26, 1, 3),
    _CucsMgmtExportPolicyFsmRn_Type()
)
cucsMgmtExportPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmRn.setStatus("current")
_CucsMgmtExportPolicyFsmCompletionTime_Type = DateAndTime
_CucsMgmtExportPolicyFsmCompletionTime_Object = MibTableColumn
cucsMgmtExportPolicyFsmCompletionTime = _CucsMgmtExportPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 26, 1, 4),
    _CucsMgmtExportPolicyFsmCompletionTime_Type()
)
cucsMgmtExportPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmCompletionTime.setStatus("current")
_CucsMgmtExportPolicyFsmCurrentFsm_Type = CucsMgmtExportPolicyFsmCurrentFsm
_CucsMgmtExportPolicyFsmCurrentFsm_Object = MibTableColumn
cucsMgmtExportPolicyFsmCurrentFsm = _CucsMgmtExportPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 26, 1, 5),
    _CucsMgmtExportPolicyFsmCurrentFsm_Type()
)
cucsMgmtExportPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmCurrentFsm.setStatus("current")
_CucsMgmtExportPolicyFsmDescr_Type = SnmpAdminString
_CucsMgmtExportPolicyFsmDescr_Object = MibTableColumn
cucsMgmtExportPolicyFsmDescr = _CucsMgmtExportPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 26, 1, 6),
    _CucsMgmtExportPolicyFsmDescr_Type()
)
cucsMgmtExportPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmDescr.setStatus("current")
_CucsMgmtExportPolicyFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtExportPolicyFsmFsmStatus_Object = MibTableColumn
cucsMgmtExportPolicyFsmFsmStatus = _CucsMgmtExportPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 26, 1, 7),
    _CucsMgmtExportPolicyFsmFsmStatus_Type()
)
cucsMgmtExportPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmFsmStatus.setStatus("current")
_CucsMgmtExportPolicyFsmProgress_Type = Gauge32
_CucsMgmtExportPolicyFsmProgress_Object = MibTableColumn
cucsMgmtExportPolicyFsmProgress = _CucsMgmtExportPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 26, 1, 8),
    _CucsMgmtExportPolicyFsmProgress_Type()
)
cucsMgmtExportPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmProgress.setStatus("current")
_CucsMgmtExportPolicyFsmRmtErrCode_Type = Gauge32
_CucsMgmtExportPolicyFsmRmtErrCode_Object = MibTableColumn
cucsMgmtExportPolicyFsmRmtErrCode = _CucsMgmtExportPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 26, 1, 9),
    _CucsMgmtExportPolicyFsmRmtErrCode_Type()
)
cucsMgmtExportPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmRmtErrCode.setStatus("current")
_CucsMgmtExportPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CucsMgmtExportPolicyFsmRmtErrDescr_Object = MibTableColumn
cucsMgmtExportPolicyFsmRmtErrDescr = _CucsMgmtExportPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 26, 1, 10),
    _CucsMgmtExportPolicyFsmRmtErrDescr_Type()
)
cucsMgmtExportPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmRmtErrDescr.setStatus("current")
_CucsMgmtExportPolicyFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtExportPolicyFsmRmtRslt_Object = MibTableColumn
cucsMgmtExportPolicyFsmRmtRslt = _CucsMgmtExportPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 26, 1, 11),
    _CucsMgmtExportPolicyFsmRmtRslt_Type()
)
cucsMgmtExportPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmRmtRslt.setStatus("current")
_CucsMgmtExportPolicyFsmStageTable_Object = MibTable
cucsMgmtExportPolicyFsmStageTable = _CucsMgmtExportPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 27)
)
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmStageTable.setStatus("current")
_CucsMgmtExportPolicyFsmStageEntry_Object = MibTableRow
cucsMgmtExportPolicyFsmStageEntry = _CucsMgmtExportPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 27, 1)
)
cucsMgmtExportPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtExportPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmStageEntry.setStatus("current")
_CucsMgmtExportPolicyFsmStageInstanceId_Type = CucsManagedObjectId
_CucsMgmtExportPolicyFsmStageInstanceId_Object = MibTableColumn
cucsMgmtExportPolicyFsmStageInstanceId = _CucsMgmtExportPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 27, 1, 1),
    _CucsMgmtExportPolicyFsmStageInstanceId_Type()
)
cucsMgmtExportPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmStageInstanceId.setStatus("current")
_CucsMgmtExportPolicyFsmStageDn_Type = CucsManagedObjectDn
_CucsMgmtExportPolicyFsmStageDn_Object = MibTableColumn
cucsMgmtExportPolicyFsmStageDn = _CucsMgmtExportPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 27, 1, 2),
    _CucsMgmtExportPolicyFsmStageDn_Type()
)
cucsMgmtExportPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmStageDn.setStatus("current")
_CucsMgmtExportPolicyFsmStageRn_Type = SnmpAdminString
_CucsMgmtExportPolicyFsmStageRn_Object = MibTableColumn
cucsMgmtExportPolicyFsmStageRn = _CucsMgmtExportPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 27, 1, 3),
    _CucsMgmtExportPolicyFsmStageRn_Type()
)
cucsMgmtExportPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmStageRn.setStatus("current")
_CucsMgmtExportPolicyFsmStageDescr_Type = SnmpAdminString
_CucsMgmtExportPolicyFsmStageDescr_Object = MibTableColumn
cucsMgmtExportPolicyFsmStageDescr = _CucsMgmtExportPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 27, 1, 4),
    _CucsMgmtExportPolicyFsmStageDescr_Type()
)
cucsMgmtExportPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmStageDescr.setStatus("current")
_CucsMgmtExportPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CucsMgmtExportPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cucsMgmtExportPolicyFsmStageLastUpdateTime = _CucsMgmtExportPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 27, 1, 5),
    _CucsMgmtExportPolicyFsmStageLastUpdateTime_Type()
)
cucsMgmtExportPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmStageLastUpdateTime.setStatus("current")
_CucsMgmtExportPolicyFsmStageName_Type = CucsMgmtExportPolicyFsmStageName
_CucsMgmtExportPolicyFsmStageName_Object = MibTableColumn
cucsMgmtExportPolicyFsmStageName = _CucsMgmtExportPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 27, 1, 6),
    _CucsMgmtExportPolicyFsmStageName_Type()
)
cucsMgmtExportPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmStageName.setStatus("current")
_CucsMgmtExportPolicyFsmStageOrder_Type = Gauge32
_CucsMgmtExportPolicyFsmStageOrder_Object = MibTableColumn
cucsMgmtExportPolicyFsmStageOrder = _CucsMgmtExportPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 27, 1, 7),
    _CucsMgmtExportPolicyFsmStageOrder_Type()
)
cucsMgmtExportPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmStageOrder.setStatus("current")
_CucsMgmtExportPolicyFsmStageRetry_Type = Gauge32
_CucsMgmtExportPolicyFsmStageRetry_Object = MibTableColumn
cucsMgmtExportPolicyFsmStageRetry = _CucsMgmtExportPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 27, 1, 8),
    _CucsMgmtExportPolicyFsmStageRetry_Type()
)
cucsMgmtExportPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmStageRetry.setStatus("current")
_CucsMgmtExportPolicyFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtExportPolicyFsmStageStageStatus_Object = MibTableColumn
cucsMgmtExportPolicyFsmStageStageStatus = _CucsMgmtExportPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 27, 1, 9),
    _CucsMgmtExportPolicyFsmStageStageStatus_Type()
)
cucsMgmtExportPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmStageStageStatus.setStatus("current")
_CucsMgmtExportPolicyFsmTaskTable_Object = MibTable
cucsMgmtExportPolicyFsmTaskTable = _CucsMgmtExportPolicyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 28)
)
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmTaskTable.setStatus("current")
_CucsMgmtExportPolicyFsmTaskEntry_Object = MibTableRow
cucsMgmtExportPolicyFsmTaskEntry = _CucsMgmtExportPolicyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 28, 1)
)
cucsMgmtExportPolicyFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtExportPolicyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmTaskEntry.setStatus("current")
_CucsMgmtExportPolicyFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsMgmtExportPolicyFsmTaskInstanceId_Object = MibTableColumn
cucsMgmtExportPolicyFsmTaskInstanceId = _CucsMgmtExportPolicyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 28, 1, 1),
    _CucsMgmtExportPolicyFsmTaskInstanceId_Type()
)
cucsMgmtExportPolicyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmTaskInstanceId.setStatus("current")
_CucsMgmtExportPolicyFsmTaskDn_Type = CucsManagedObjectDn
_CucsMgmtExportPolicyFsmTaskDn_Object = MibTableColumn
cucsMgmtExportPolicyFsmTaskDn = _CucsMgmtExportPolicyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 28, 1, 2),
    _CucsMgmtExportPolicyFsmTaskDn_Type()
)
cucsMgmtExportPolicyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmTaskDn.setStatus("current")
_CucsMgmtExportPolicyFsmTaskRn_Type = SnmpAdminString
_CucsMgmtExportPolicyFsmTaskRn_Object = MibTableColumn
cucsMgmtExportPolicyFsmTaskRn = _CucsMgmtExportPolicyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 28, 1, 3),
    _CucsMgmtExportPolicyFsmTaskRn_Type()
)
cucsMgmtExportPolicyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmTaskRn.setStatus("current")
_CucsMgmtExportPolicyFsmTaskCompletion_Type = CucsFsmCompletion
_CucsMgmtExportPolicyFsmTaskCompletion_Object = MibTableColumn
cucsMgmtExportPolicyFsmTaskCompletion = _CucsMgmtExportPolicyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 28, 1, 4),
    _CucsMgmtExportPolicyFsmTaskCompletion_Type()
)
cucsMgmtExportPolicyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmTaskCompletion.setStatus("current")
_CucsMgmtExportPolicyFsmTaskFlags_Type = CucsFsmFlags
_CucsMgmtExportPolicyFsmTaskFlags_Object = MibTableColumn
cucsMgmtExportPolicyFsmTaskFlags = _CucsMgmtExportPolicyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 28, 1, 5),
    _CucsMgmtExportPolicyFsmTaskFlags_Type()
)
cucsMgmtExportPolicyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmTaskFlags.setStatus("current")
_CucsMgmtExportPolicyFsmTaskItem_Type = CucsMgmtExportPolicyFsmTaskItem
_CucsMgmtExportPolicyFsmTaskItem_Object = MibTableColumn
cucsMgmtExportPolicyFsmTaskItem = _CucsMgmtExportPolicyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 28, 1, 6),
    _CucsMgmtExportPolicyFsmTaskItem_Type()
)
cucsMgmtExportPolicyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmTaskItem.setStatus("current")
_CucsMgmtExportPolicyFsmTaskSeqId_Type = Gauge32
_CucsMgmtExportPolicyFsmTaskSeqId_Object = MibTableColumn
cucsMgmtExportPolicyFsmTaskSeqId = _CucsMgmtExportPolicyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 28, 1, 7),
    _CucsMgmtExportPolicyFsmTaskSeqId_Type()
)
cucsMgmtExportPolicyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtExportPolicyFsmTaskSeqId.setStatus("current")
_CucsMgmtIfFsmTable_Object = MibTable
cucsMgmtIfFsmTable = _CucsMgmtIfFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 29)
)
if mibBuilder.loadTexts:
    cucsMgmtIfFsmTable.setStatus("current")
_CucsMgmtIfFsmEntry_Object = MibTableRow
cucsMgmtIfFsmEntry = _CucsMgmtIfFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 29, 1)
)
cucsMgmtIfFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtIfFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtIfFsmEntry.setStatus("current")
_CucsMgmtIfFsmInstanceId_Type = CucsManagedObjectId
_CucsMgmtIfFsmInstanceId_Object = MibTableColumn
cucsMgmtIfFsmInstanceId = _CucsMgmtIfFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 29, 1, 1),
    _CucsMgmtIfFsmInstanceId_Type()
)
cucsMgmtIfFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmInstanceId.setStatus("current")
_CucsMgmtIfFsmDn_Type = CucsManagedObjectDn
_CucsMgmtIfFsmDn_Object = MibTableColumn
cucsMgmtIfFsmDn = _CucsMgmtIfFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 29, 1, 2),
    _CucsMgmtIfFsmDn_Type()
)
cucsMgmtIfFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmDn.setStatus("current")
_CucsMgmtIfFsmRn_Type = SnmpAdminString
_CucsMgmtIfFsmRn_Object = MibTableColumn
cucsMgmtIfFsmRn = _CucsMgmtIfFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 29, 1, 3),
    _CucsMgmtIfFsmRn_Type()
)
cucsMgmtIfFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmRn.setStatus("current")
_CucsMgmtIfFsmCompletionTime_Type = DateAndTime
_CucsMgmtIfFsmCompletionTime_Object = MibTableColumn
cucsMgmtIfFsmCompletionTime = _CucsMgmtIfFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 29, 1, 4),
    _CucsMgmtIfFsmCompletionTime_Type()
)
cucsMgmtIfFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmCompletionTime.setStatus("current")
_CucsMgmtIfFsmCurrentFsm_Type = CucsMgmtIfFsmCurrentFsm
_CucsMgmtIfFsmCurrentFsm_Object = MibTableColumn
cucsMgmtIfFsmCurrentFsm = _CucsMgmtIfFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 29, 1, 5),
    _CucsMgmtIfFsmCurrentFsm_Type()
)
cucsMgmtIfFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmCurrentFsm.setStatus("current")
_CucsMgmtIfFsmDescrData_Type = SnmpAdminString
_CucsMgmtIfFsmDescrData_Object = MibTableColumn
cucsMgmtIfFsmDescrData = _CucsMgmtIfFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 29, 1, 6),
    _CucsMgmtIfFsmDescrData_Type()
)
cucsMgmtIfFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmDescrData.setStatus("current")
_CucsMgmtIfFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtIfFsmFsmStatus_Object = MibTableColumn
cucsMgmtIfFsmFsmStatus = _CucsMgmtIfFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 29, 1, 7),
    _CucsMgmtIfFsmFsmStatus_Type()
)
cucsMgmtIfFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmFsmStatus.setStatus("current")
_CucsMgmtIfFsmProgress_Type = Gauge32
_CucsMgmtIfFsmProgress_Object = MibTableColumn
cucsMgmtIfFsmProgress = _CucsMgmtIfFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 29, 1, 8),
    _CucsMgmtIfFsmProgress_Type()
)
cucsMgmtIfFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmProgress.setStatus("current")
_CucsMgmtIfFsmRmtErrCode_Type = Gauge32
_CucsMgmtIfFsmRmtErrCode_Object = MibTableColumn
cucsMgmtIfFsmRmtErrCode = _CucsMgmtIfFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 29, 1, 9),
    _CucsMgmtIfFsmRmtErrCode_Type()
)
cucsMgmtIfFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmRmtErrCode.setStatus("current")
_CucsMgmtIfFsmRmtErrDescr_Type = SnmpAdminString
_CucsMgmtIfFsmRmtErrDescr_Object = MibTableColumn
cucsMgmtIfFsmRmtErrDescr = _CucsMgmtIfFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 29, 1, 10),
    _CucsMgmtIfFsmRmtErrDescr_Type()
)
cucsMgmtIfFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmRmtErrDescr.setStatus("current")
_CucsMgmtIfFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtIfFsmRmtRslt_Object = MibTableColumn
cucsMgmtIfFsmRmtRslt = _CucsMgmtIfFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 29, 1, 11),
    _CucsMgmtIfFsmRmtRslt_Type()
)
cucsMgmtIfFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmRmtRslt.setStatus("current")
_CucsMgmtIfFsmStageTable_Object = MibTable
cucsMgmtIfFsmStageTable = _CucsMgmtIfFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 30)
)
if mibBuilder.loadTexts:
    cucsMgmtIfFsmStageTable.setStatus("current")
_CucsMgmtIfFsmStageEntry_Object = MibTableRow
cucsMgmtIfFsmStageEntry = _CucsMgmtIfFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 30, 1)
)
cucsMgmtIfFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtIfFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtIfFsmStageEntry.setStatus("current")
_CucsMgmtIfFsmStageInstanceId_Type = CucsManagedObjectId
_CucsMgmtIfFsmStageInstanceId_Object = MibTableColumn
cucsMgmtIfFsmStageInstanceId = _CucsMgmtIfFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 30, 1, 1),
    _CucsMgmtIfFsmStageInstanceId_Type()
)
cucsMgmtIfFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmStageInstanceId.setStatus("current")
_CucsMgmtIfFsmStageDn_Type = CucsManagedObjectDn
_CucsMgmtIfFsmStageDn_Object = MibTableColumn
cucsMgmtIfFsmStageDn = _CucsMgmtIfFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 30, 1, 2),
    _CucsMgmtIfFsmStageDn_Type()
)
cucsMgmtIfFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmStageDn.setStatus("current")
_CucsMgmtIfFsmStageRn_Type = SnmpAdminString
_CucsMgmtIfFsmStageRn_Object = MibTableColumn
cucsMgmtIfFsmStageRn = _CucsMgmtIfFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 30, 1, 3),
    _CucsMgmtIfFsmStageRn_Type()
)
cucsMgmtIfFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmStageRn.setStatus("current")
_CucsMgmtIfFsmStageDescrData_Type = SnmpAdminString
_CucsMgmtIfFsmStageDescrData_Object = MibTableColumn
cucsMgmtIfFsmStageDescrData = _CucsMgmtIfFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 30, 1, 4),
    _CucsMgmtIfFsmStageDescrData_Type()
)
cucsMgmtIfFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmStageDescrData.setStatus("current")
_CucsMgmtIfFsmStageLastUpdateTime_Type = DateAndTime
_CucsMgmtIfFsmStageLastUpdateTime_Object = MibTableColumn
cucsMgmtIfFsmStageLastUpdateTime = _CucsMgmtIfFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 30, 1, 5),
    _CucsMgmtIfFsmStageLastUpdateTime_Type()
)
cucsMgmtIfFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmStageLastUpdateTime.setStatus("current")
_CucsMgmtIfFsmStageName_Type = CucsMgmtIfFsmStageName
_CucsMgmtIfFsmStageName_Object = MibTableColumn
cucsMgmtIfFsmStageName = _CucsMgmtIfFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 30, 1, 6),
    _CucsMgmtIfFsmStageName_Type()
)
cucsMgmtIfFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmStageName.setStatus("current")
_CucsMgmtIfFsmStageOrder_Type = Gauge32
_CucsMgmtIfFsmStageOrder_Object = MibTableColumn
cucsMgmtIfFsmStageOrder = _CucsMgmtIfFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 30, 1, 7),
    _CucsMgmtIfFsmStageOrder_Type()
)
cucsMgmtIfFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmStageOrder.setStatus("current")
_CucsMgmtIfFsmStageRetry_Type = Gauge32
_CucsMgmtIfFsmStageRetry_Object = MibTableColumn
cucsMgmtIfFsmStageRetry = _CucsMgmtIfFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 30, 1, 8),
    _CucsMgmtIfFsmStageRetry_Type()
)
cucsMgmtIfFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmStageRetry.setStatus("current")
_CucsMgmtIfFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtIfFsmStageStageStatus_Object = MibTableColumn
cucsMgmtIfFsmStageStageStatus = _CucsMgmtIfFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 30, 1, 9),
    _CucsMgmtIfFsmStageStageStatus_Type()
)
cucsMgmtIfFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIfFsmStageStageStatus.setStatus("current")
_CucsMgmtImporterFsmTable_Object = MibTable
cucsMgmtImporterFsmTable = _CucsMgmtImporterFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 31)
)
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmTable.setStatus("current")
_CucsMgmtImporterFsmEntry_Object = MibTableRow
cucsMgmtImporterFsmEntry = _CucsMgmtImporterFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 31, 1)
)
cucsMgmtImporterFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtImporterFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmEntry.setStatus("current")
_CucsMgmtImporterFsmInstanceId_Type = CucsManagedObjectId
_CucsMgmtImporterFsmInstanceId_Object = MibTableColumn
cucsMgmtImporterFsmInstanceId = _CucsMgmtImporterFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 31, 1, 1),
    _CucsMgmtImporterFsmInstanceId_Type()
)
cucsMgmtImporterFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmInstanceId.setStatus("current")
_CucsMgmtImporterFsmDn_Type = CucsManagedObjectDn
_CucsMgmtImporterFsmDn_Object = MibTableColumn
cucsMgmtImporterFsmDn = _CucsMgmtImporterFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 31, 1, 2),
    _CucsMgmtImporterFsmDn_Type()
)
cucsMgmtImporterFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmDn.setStatus("current")
_CucsMgmtImporterFsmRn_Type = SnmpAdminString
_CucsMgmtImporterFsmRn_Object = MibTableColumn
cucsMgmtImporterFsmRn = _CucsMgmtImporterFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 31, 1, 3),
    _CucsMgmtImporterFsmRn_Type()
)
cucsMgmtImporterFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmRn.setStatus("current")
_CucsMgmtImporterFsmCompletionTime_Type = DateAndTime
_CucsMgmtImporterFsmCompletionTime_Object = MibTableColumn
cucsMgmtImporterFsmCompletionTime = _CucsMgmtImporterFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 31, 1, 4),
    _CucsMgmtImporterFsmCompletionTime_Type()
)
cucsMgmtImporterFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmCompletionTime.setStatus("current")
_CucsMgmtImporterFsmCurrentFsm_Type = CucsMgmtImporterFsmCurrentFsm
_CucsMgmtImporterFsmCurrentFsm_Object = MibTableColumn
cucsMgmtImporterFsmCurrentFsm = _CucsMgmtImporterFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 31, 1, 5),
    _CucsMgmtImporterFsmCurrentFsm_Type()
)
cucsMgmtImporterFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmCurrentFsm.setStatus("current")
_CucsMgmtImporterFsmDescrData_Type = SnmpAdminString
_CucsMgmtImporterFsmDescrData_Object = MibTableColumn
cucsMgmtImporterFsmDescrData = _CucsMgmtImporterFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 31, 1, 6),
    _CucsMgmtImporterFsmDescrData_Type()
)
cucsMgmtImporterFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmDescrData.setStatus("current")
_CucsMgmtImporterFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtImporterFsmFsmStatus_Object = MibTableColumn
cucsMgmtImporterFsmFsmStatus = _CucsMgmtImporterFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 31, 1, 7),
    _CucsMgmtImporterFsmFsmStatus_Type()
)
cucsMgmtImporterFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmFsmStatus.setStatus("current")
_CucsMgmtImporterFsmProgress_Type = Gauge32
_CucsMgmtImporterFsmProgress_Object = MibTableColumn
cucsMgmtImporterFsmProgress = _CucsMgmtImporterFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 31, 1, 8),
    _CucsMgmtImporterFsmProgress_Type()
)
cucsMgmtImporterFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmProgress.setStatus("current")
_CucsMgmtImporterFsmRmtErrCode_Type = Gauge32
_CucsMgmtImporterFsmRmtErrCode_Object = MibTableColumn
cucsMgmtImporterFsmRmtErrCode = _CucsMgmtImporterFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 31, 1, 9),
    _CucsMgmtImporterFsmRmtErrCode_Type()
)
cucsMgmtImporterFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmRmtErrCode.setStatus("current")
_CucsMgmtImporterFsmRmtErrDescr_Type = SnmpAdminString
_CucsMgmtImporterFsmRmtErrDescr_Object = MibTableColumn
cucsMgmtImporterFsmRmtErrDescr = _CucsMgmtImporterFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 31, 1, 10),
    _CucsMgmtImporterFsmRmtErrDescr_Type()
)
cucsMgmtImporterFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmRmtErrDescr.setStatus("current")
_CucsMgmtImporterFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtImporterFsmRmtRslt_Object = MibTableColumn
cucsMgmtImporterFsmRmtRslt = _CucsMgmtImporterFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 31, 1, 11),
    _CucsMgmtImporterFsmRmtRslt_Type()
)
cucsMgmtImporterFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmRmtRslt.setStatus("current")
_CucsMgmtImporterFsmStageTable_Object = MibTable
cucsMgmtImporterFsmStageTable = _CucsMgmtImporterFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 32)
)
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmStageTable.setStatus("current")
_CucsMgmtImporterFsmStageEntry_Object = MibTableRow
cucsMgmtImporterFsmStageEntry = _CucsMgmtImporterFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 32, 1)
)
cucsMgmtImporterFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtImporterFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmStageEntry.setStatus("current")
_CucsMgmtImporterFsmStageInstanceId_Type = CucsManagedObjectId
_CucsMgmtImporterFsmStageInstanceId_Object = MibTableColumn
cucsMgmtImporterFsmStageInstanceId = _CucsMgmtImporterFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 32, 1, 1),
    _CucsMgmtImporterFsmStageInstanceId_Type()
)
cucsMgmtImporterFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmStageInstanceId.setStatus("current")
_CucsMgmtImporterFsmStageDn_Type = CucsManagedObjectDn
_CucsMgmtImporterFsmStageDn_Object = MibTableColumn
cucsMgmtImporterFsmStageDn = _CucsMgmtImporterFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 32, 1, 2),
    _CucsMgmtImporterFsmStageDn_Type()
)
cucsMgmtImporterFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmStageDn.setStatus("current")
_CucsMgmtImporterFsmStageRn_Type = SnmpAdminString
_CucsMgmtImporterFsmStageRn_Object = MibTableColumn
cucsMgmtImporterFsmStageRn = _CucsMgmtImporterFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 32, 1, 3),
    _CucsMgmtImporterFsmStageRn_Type()
)
cucsMgmtImporterFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmStageRn.setStatus("current")
_CucsMgmtImporterFsmStageDescrData_Type = SnmpAdminString
_CucsMgmtImporterFsmStageDescrData_Object = MibTableColumn
cucsMgmtImporterFsmStageDescrData = _CucsMgmtImporterFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 32, 1, 4),
    _CucsMgmtImporterFsmStageDescrData_Type()
)
cucsMgmtImporterFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmStageDescrData.setStatus("current")
_CucsMgmtImporterFsmStageLastUpdateTime_Type = DateAndTime
_CucsMgmtImporterFsmStageLastUpdateTime_Object = MibTableColumn
cucsMgmtImporterFsmStageLastUpdateTime = _CucsMgmtImporterFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 32, 1, 5),
    _CucsMgmtImporterFsmStageLastUpdateTime_Type()
)
cucsMgmtImporterFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmStageLastUpdateTime.setStatus("current")
_CucsMgmtImporterFsmStageName_Type = CucsMgmtImporterFsmStageName
_CucsMgmtImporterFsmStageName_Object = MibTableColumn
cucsMgmtImporterFsmStageName = _CucsMgmtImporterFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 32, 1, 6),
    _CucsMgmtImporterFsmStageName_Type()
)
cucsMgmtImporterFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmStageName.setStatus("current")
_CucsMgmtImporterFsmStageOrder_Type = Gauge32
_CucsMgmtImporterFsmStageOrder_Object = MibTableColumn
cucsMgmtImporterFsmStageOrder = _CucsMgmtImporterFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 32, 1, 7),
    _CucsMgmtImporterFsmStageOrder_Type()
)
cucsMgmtImporterFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmStageOrder.setStatus("current")
_CucsMgmtImporterFsmStageRetry_Type = Gauge32
_CucsMgmtImporterFsmStageRetry_Object = MibTableColumn
cucsMgmtImporterFsmStageRetry = _CucsMgmtImporterFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 32, 1, 8),
    _CucsMgmtImporterFsmStageRetry_Type()
)
cucsMgmtImporterFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmStageRetry.setStatus("current")
_CucsMgmtImporterFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtImporterFsmStageStageStatus_Object = MibTableColumn
cucsMgmtImporterFsmStageStageStatus = _CucsMgmtImporterFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 32, 1, 9),
    _CucsMgmtImporterFsmStageStageStatus_Type()
)
cucsMgmtImporterFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtImporterFsmStageStageStatus.setStatus("current")
_CucsMgmtIPv6IfAddrTable_Object = MibTable
cucsMgmtIPv6IfAddrTable = _CucsMgmtIPv6IfAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33)
)
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrTable.setStatus("current")
_CucsMgmtIPv6IfAddrEntry_Object = MibTableRow
cucsMgmtIPv6IfAddrEntry = _CucsMgmtIPv6IfAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1)
)
cucsMgmtIPv6IfAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtIPv6IfAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrEntry.setStatus("current")
_CucsMgmtIPv6IfAddrInstanceId_Type = CucsManagedObjectId
_CucsMgmtIPv6IfAddrInstanceId_Object = MibTableColumn
cucsMgmtIPv6IfAddrInstanceId = _CucsMgmtIPv6IfAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 1),
    _CucsMgmtIPv6IfAddrInstanceId_Type()
)
cucsMgmtIPv6IfAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrInstanceId.setStatus("current")
_CucsMgmtIPv6IfAddrDn_Type = CucsManagedObjectDn
_CucsMgmtIPv6IfAddrDn_Object = MibTableColumn
cucsMgmtIPv6IfAddrDn = _CucsMgmtIPv6IfAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 2),
    _CucsMgmtIPv6IfAddrDn_Type()
)
cucsMgmtIPv6IfAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrDn.setStatus("current")
_CucsMgmtIPv6IfAddrRn_Type = SnmpAdminString
_CucsMgmtIPv6IfAddrRn_Object = MibTableColumn
cucsMgmtIPv6IfAddrRn = _CucsMgmtIPv6IfAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 3),
    _CucsMgmtIPv6IfAddrRn_Type()
)
cucsMgmtIPv6IfAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrRn.setStatus("current")
_CucsMgmtIPv6IfAddrAddr_Type = InetAddressIPv6
_CucsMgmtIPv6IfAddrAddr_Object = MibTableColumn
cucsMgmtIPv6IfAddrAddr = _CucsMgmtIPv6IfAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 4),
    _CucsMgmtIPv6IfAddrAddr_Type()
)
cucsMgmtIPv6IfAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrAddr.setStatus("current")
_CucsMgmtIPv6IfAddrDefGw_Type = InetAddressIPv6
_CucsMgmtIPv6IfAddrDefGw_Object = MibTableColumn
cucsMgmtIPv6IfAddrDefGw = _CucsMgmtIPv6IfAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 5),
    _CucsMgmtIPv6IfAddrDefGw_Type()
)
cucsMgmtIPv6IfAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrDefGw.setStatus("current")
_CucsMgmtIPv6IfAddrFsmDescr_Type = SnmpAdminString
_CucsMgmtIPv6IfAddrFsmDescr_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmDescr = _CucsMgmtIPv6IfAddrFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 6),
    _CucsMgmtIPv6IfAddrFsmDescr_Type()
)
cucsMgmtIPv6IfAddrFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmDescr.setStatus("current")
_CucsMgmtIPv6IfAddrFsmPrev_Type = SnmpAdminString
_CucsMgmtIPv6IfAddrFsmPrev_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmPrev = _CucsMgmtIPv6IfAddrFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 7),
    _CucsMgmtIPv6IfAddrFsmPrev_Type()
)
cucsMgmtIPv6IfAddrFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmPrev.setStatus("current")
_CucsMgmtIPv6IfAddrFsmProgr_Type = Gauge32
_CucsMgmtIPv6IfAddrFsmProgr_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmProgr = _CucsMgmtIPv6IfAddrFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 8),
    _CucsMgmtIPv6IfAddrFsmProgr_Type()
)
cucsMgmtIPv6IfAddrFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmProgr.setStatus("current")
_CucsMgmtIPv6IfAddrFsmRmtInvErrCode_Type = Gauge32
_CucsMgmtIPv6IfAddrFsmRmtInvErrCode_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmRmtInvErrCode = _CucsMgmtIPv6IfAddrFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 9),
    _CucsMgmtIPv6IfAddrFsmRmtInvErrCode_Type()
)
cucsMgmtIPv6IfAddrFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmRmtInvErrCode.setStatus("current")
_CucsMgmtIPv6IfAddrFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsMgmtIPv6IfAddrFsmRmtInvErrDescr_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmRmtInvErrDescr = _CucsMgmtIPv6IfAddrFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 10),
    _CucsMgmtIPv6IfAddrFsmRmtInvErrDescr_Type()
)
cucsMgmtIPv6IfAddrFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmRmtInvErrDescr.setStatus("current")
_CucsMgmtIPv6IfAddrFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtIPv6IfAddrFsmRmtInvRslt_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmRmtInvRslt = _CucsMgmtIPv6IfAddrFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 11),
    _CucsMgmtIPv6IfAddrFsmRmtInvRslt_Type()
)
cucsMgmtIPv6IfAddrFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmRmtInvRslt.setStatus("current")
_CucsMgmtIPv6IfAddrFsmStageDescr_Type = SnmpAdminString
_CucsMgmtIPv6IfAddrFsmStageDescr_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmStageDescr = _CucsMgmtIPv6IfAddrFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 12),
    _CucsMgmtIPv6IfAddrFsmStageDescr_Type()
)
cucsMgmtIPv6IfAddrFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmStageDescr.setStatus("current")
_CucsMgmtIPv6IfAddrFsmStamp_Type = DateAndTime
_CucsMgmtIPv6IfAddrFsmStamp_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmStamp = _CucsMgmtIPv6IfAddrFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 13),
    _CucsMgmtIPv6IfAddrFsmStamp_Type()
)
cucsMgmtIPv6IfAddrFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmStamp.setStatus("current")
_CucsMgmtIPv6IfAddrFsmStatus_Type = SnmpAdminString
_CucsMgmtIPv6IfAddrFsmStatus_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmStatus = _CucsMgmtIPv6IfAddrFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 14),
    _CucsMgmtIPv6IfAddrFsmStatus_Type()
)
cucsMgmtIPv6IfAddrFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmStatus.setStatus("current")
_CucsMgmtIPv6IfAddrFsmTry_Type = Gauge32
_CucsMgmtIPv6IfAddrFsmTry_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmTry = _CucsMgmtIPv6IfAddrFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 15),
    _CucsMgmtIPv6IfAddrFsmTry_Type()
)
cucsMgmtIPv6IfAddrFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmTry.setStatus("current")
_CucsMgmtIPv6IfAddrPrefix_Type = Gauge32
_CucsMgmtIPv6IfAddrPrefix_Object = MibTableColumn
cucsMgmtIPv6IfAddrPrefix = _CucsMgmtIPv6IfAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 33, 1, 16),
    _CucsMgmtIPv6IfAddrPrefix_Type()
)
cucsMgmtIPv6IfAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrPrefix.setStatus("current")
_CucsMgmtIPv6IfAddrFsmTable_Object = MibTable
cucsMgmtIPv6IfAddrFsmTable = _CucsMgmtIPv6IfAddrFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 34)
)
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmTable.setStatus("current")
_CucsMgmtIPv6IfAddrFsmEntry_Object = MibTableRow
cucsMgmtIPv6IfAddrFsmEntry = _CucsMgmtIPv6IfAddrFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 34, 1)
)
cucsMgmtIPv6IfAddrFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtIPv6IfAddrFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmEntry.setStatus("current")
_CucsMgmtIPv6IfAddrFsmInstanceId_Type = CucsManagedObjectId
_CucsMgmtIPv6IfAddrFsmInstanceId_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmInstanceId = _CucsMgmtIPv6IfAddrFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 34, 1, 1),
    _CucsMgmtIPv6IfAddrFsmInstanceId_Type()
)
cucsMgmtIPv6IfAddrFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmInstanceId.setStatus("current")
_CucsMgmtIPv6IfAddrFsmDn_Type = CucsManagedObjectDn
_CucsMgmtIPv6IfAddrFsmDn_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmDn = _CucsMgmtIPv6IfAddrFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 34, 1, 2),
    _CucsMgmtIPv6IfAddrFsmDn_Type()
)
cucsMgmtIPv6IfAddrFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmDn.setStatus("current")
_CucsMgmtIPv6IfAddrFsmRn_Type = SnmpAdminString
_CucsMgmtIPv6IfAddrFsmRn_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmRn = _CucsMgmtIPv6IfAddrFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 34, 1, 3),
    _CucsMgmtIPv6IfAddrFsmRn_Type()
)
cucsMgmtIPv6IfAddrFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmRn.setStatus("current")
_CucsMgmtIPv6IfAddrFsmCompletionTime_Type = DateAndTime
_CucsMgmtIPv6IfAddrFsmCompletionTime_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmCompletionTime = _CucsMgmtIPv6IfAddrFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 34, 1, 4),
    _CucsMgmtIPv6IfAddrFsmCompletionTime_Type()
)
cucsMgmtIPv6IfAddrFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmCompletionTime.setStatus("current")
_CucsMgmtIPv6IfAddrFsmCurrentFsm_Type = CucsMgmtIPv6IfAddrFsmCurrentFsm
_CucsMgmtIPv6IfAddrFsmCurrentFsm_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmCurrentFsm = _CucsMgmtIPv6IfAddrFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 34, 1, 5),
    _CucsMgmtIPv6IfAddrFsmCurrentFsm_Type()
)
cucsMgmtIPv6IfAddrFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmCurrentFsm.setStatus("current")
_CucsMgmtIPv6IfAddrFsmDescrData_Type = SnmpAdminString
_CucsMgmtIPv6IfAddrFsmDescrData_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmDescrData = _CucsMgmtIPv6IfAddrFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 34, 1, 6),
    _CucsMgmtIPv6IfAddrFsmDescrData_Type()
)
cucsMgmtIPv6IfAddrFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmDescrData.setStatus("current")
_CucsMgmtIPv6IfAddrFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtIPv6IfAddrFsmFsmStatus_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmFsmStatus = _CucsMgmtIPv6IfAddrFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 34, 1, 7),
    _CucsMgmtIPv6IfAddrFsmFsmStatus_Type()
)
cucsMgmtIPv6IfAddrFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmFsmStatus.setStatus("current")
_CucsMgmtIPv6IfAddrFsmProgress_Type = Gauge32
_CucsMgmtIPv6IfAddrFsmProgress_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmProgress = _CucsMgmtIPv6IfAddrFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 34, 1, 8),
    _CucsMgmtIPv6IfAddrFsmProgress_Type()
)
cucsMgmtIPv6IfAddrFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmProgress.setStatus("current")
_CucsMgmtIPv6IfAddrFsmRmtErrCode_Type = Gauge32
_CucsMgmtIPv6IfAddrFsmRmtErrCode_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmRmtErrCode = _CucsMgmtIPv6IfAddrFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 34, 1, 9),
    _CucsMgmtIPv6IfAddrFsmRmtErrCode_Type()
)
cucsMgmtIPv6IfAddrFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmRmtErrCode.setStatus("current")
_CucsMgmtIPv6IfAddrFsmRmtErrDescr_Type = SnmpAdminString
_CucsMgmtIPv6IfAddrFsmRmtErrDescr_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmRmtErrDescr = _CucsMgmtIPv6IfAddrFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 34, 1, 10),
    _CucsMgmtIPv6IfAddrFsmRmtErrDescr_Type()
)
cucsMgmtIPv6IfAddrFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmRmtErrDescr.setStatus("current")
_CucsMgmtIPv6IfAddrFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsMgmtIPv6IfAddrFsmRmtRslt_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmRmtRslt = _CucsMgmtIPv6IfAddrFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 34, 1, 11),
    _CucsMgmtIPv6IfAddrFsmRmtRslt_Type()
)
cucsMgmtIPv6IfAddrFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmRmtRslt.setStatus("current")
_CucsMgmtIPv6IfAddrFsmStageTable_Object = MibTable
cucsMgmtIPv6IfAddrFsmStageTable = _CucsMgmtIPv6IfAddrFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 35)
)
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmStageTable.setStatus("current")
_CucsMgmtIPv6IfAddrFsmStageEntry_Object = MibTableRow
cucsMgmtIPv6IfAddrFsmStageEntry = _CucsMgmtIPv6IfAddrFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 35, 1)
)
cucsMgmtIPv6IfAddrFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtIPv6IfAddrFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmStageEntry.setStatus("current")
_CucsMgmtIPv6IfAddrFsmStageInstanceId_Type = CucsManagedObjectId
_CucsMgmtIPv6IfAddrFsmStageInstanceId_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmStageInstanceId = _CucsMgmtIPv6IfAddrFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 35, 1, 1),
    _CucsMgmtIPv6IfAddrFsmStageInstanceId_Type()
)
cucsMgmtIPv6IfAddrFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmStageInstanceId.setStatus("current")
_CucsMgmtIPv6IfAddrFsmStageDn_Type = CucsManagedObjectDn
_CucsMgmtIPv6IfAddrFsmStageDn_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmStageDn = _CucsMgmtIPv6IfAddrFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 35, 1, 2),
    _CucsMgmtIPv6IfAddrFsmStageDn_Type()
)
cucsMgmtIPv6IfAddrFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmStageDn.setStatus("current")
_CucsMgmtIPv6IfAddrFsmStageRn_Type = SnmpAdminString
_CucsMgmtIPv6IfAddrFsmStageRn_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmStageRn = _CucsMgmtIPv6IfAddrFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 35, 1, 3),
    _CucsMgmtIPv6IfAddrFsmStageRn_Type()
)
cucsMgmtIPv6IfAddrFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmStageRn.setStatus("current")
_CucsMgmtIPv6IfAddrFsmStageDescrData_Type = SnmpAdminString
_CucsMgmtIPv6IfAddrFsmStageDescrData_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmStageDescrData = _CucsMgmtIPv6IfAddrFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 35, 1, 4),
    _CucsMgmtIPv6IfAddrFsmStageDescrData_Type()
)
cucsMgmtIPv6IfAddrFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmStageDescrData.setStatus("current")
_CucsMgmtIPv6IfAddrFsmStageLastUpdateTime_Type = DateAndTime
_CucsMgmtIPv6IfAddrFsmStageLastUpdateTime_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmStageLastUpdateTime = _CucsMgmtIPv6IfAddrFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 35, 1, 5),
    _CucsMgmtIPv6IfAddrFsmStageLastUpdateTime_Type()
)
cucsMgmtIPv6IfAddrFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmStageLastUpdateTime.setStatus("current")
_CucsMgmtIPv6IfAddrFsmStageName_Type = CucsMgmtIPv6IfAddrFsmStageName
_CucsMgmtIPv6IfAddrFsmStageName_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmStageName = _CucsMgmtIPv6IfAddrFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 35, 1, 6),
    _CucsMgmtIPv6IfAddrFsmStageName_Type()
)
cucsMgmtIPv6IfAddrFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmStageName.setStatus("current")
_CucsMgmtIPv6IfAddrFsmStageOrder_Type = Gauge32
_CucsMgmtIPv6IfAddrFsmStageOrder_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmStageOrder = _CucsMgmtIPv6IfAddrFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 35, 1, 7),
    _CucsMgmtIPv6IfAddrFsmStageOrder_Type()
)
cucsMgmtIPv6IfAddrFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmStageOrder.setStatus("current")
_CucsMgmtIPv6IfAddrFsmStageRetry_Type = Gauge32
_CucsMgmtIPv6IfAddrFsmStageRetry_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmStageRetry = _CucsMgmtIPv6IfAddrFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 35, 1, 8),
    _CucsMgmtIPv6IfAddrFsmStageRetry_Type()
)
cucsMgmtIPv6IfAddrFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmStageRetry.setStatus("current")
_CucsMgmtIPv6IfAddrFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsMgmtIPv6IfAddrFsmStageStageStatus_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmStageStageStatus = _CucsMgmtIPv6IfAddrFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 35, 1, 9),
    _CucsMgmtIPv6IfAddrFsmStageStageStatus_Type()
)
cucsMgmtIPv6IfAddrFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmStageStageStatus.setStatus("current")
_CucsMgmtIPv6IfAddrFsmTaskTable_Object = MibTable
cucsMgmtIPv6IfAddrFsmTaskTable = _CucsMgmtIPv6IfAddrFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 36)
)
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmTaskTable.setStatus("current")
_CucsMgmtIPv6IfAddrFsmTaskEntry_Object = MibTableRow
cucsMgmtIPv6IfAddrFsmTaskEntry = _CucsMgmtIPv6IfAddrFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 36, 1)
)
cucsMgmtIPv6IfAddrFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtIPv6IfAddrFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmTaskEntry.setStatus("current")
_CucsMgmtIPv6IfAddrFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsMgmtIPv6IfAddrFsmTaskInstanceId_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmTaskInstanceId = _CucsMgmtIPv6IfAddrFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 36, 1, 1),
    _CucsMgmtIPv6IfAddrFsmTaskInstanceId_Type()
)
cucsMgmtIPv6IfAddrFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmTaskInstanceId.setStatus("current")
_CucsMgmtIPv6IfAddrFsmTaskDn_Type = CucsManagedObjectDn
_CucsMgmtIPv6IfAddrFsmTaskDn_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmTaskDn = _CucsMgmtIPv6IfAddrFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 36, 1, 2),
    _CucsMgmtIPv6IfAddrFsmTaskDn_Type()
)
cucsMgmtIPv6IfAddrFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmTaskDn.setStatus("current")
_CucsMgmtIPv6IfAddrFsmTaskRn_Type = SnmpAdminString
_CucsMgmtIPv6IfAddrFsmTaskRn_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmTaskRn = _CucsMgmtIPv6IfAddrFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 36, 1, 3),
    _CucsMgmtIPv6IfAddrFsmTaskRn_Type()
)
cucsMgmtIPv6IfAddrFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmTaskRn.setStatus("current")
_CucsMgmtIPv6IfAddrFsmTaskCompletion_Type = CucsFsmCompletion
_CucsMgmtIPv6IfAddrFsmTaskCompletion_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmTaskCompletion = _CucsMgmtIPv6IfAddrFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 36, 1, 4),
    _CucsMgmtIPv6IfAddrFsmTaskCompletion_Type()
)
cucsMgmtIPv6IfAddrFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmTaskCompletion.setStatus("current")
_CucsMgmtIPv6IfAddrFsmTaskFlags_Type = CucsFsmFlags
_CucsMgmtIPv6IfAddrFsmTaskFlags_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmTaskFlags = _CucsMgmtIPv6IfAddrFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 36, 1, 5),
    _CucsMgmtIPv6IfAddrFsmTaskFlags_Type()
)
cucsMgmtIPv6IfAddrFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmTaskFlags.setStatus("current")
_CucsMgmtIPv6IfAddrFsmTaskItem_Type = CucsMgmtIPv6IfAddrFsmTaskItem
_CucsMgmtIPv6IfAddrFsmTaskItem_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmTaskItem = _CucsMgmtIPv6IfAddrFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 36, 1, 6),
    _CucsMgmtIPv6IfAddrFsmTaskItem_Type()
)
cucsMgmtIPv6IfAddrFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmTaskItem.setStatus("current")
_CucsMgmtIPv6IfAddrFsmTaskSeqId_Type = Gauge32
_CucsMgmtIPv6IfAddrFsmTaskSeqId_Object = MibTableColumn
cucsMgmtIPv6IfAddrFsmTaskSeqId = _CucsMgmtIPv6IfAddrFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 36, 1, 7),
    _CucsMgmtIPv6IfAddrFsmTaskSeqId_Type()
)
cucsMgmtIPv6IfAddrFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfAddrFsmTaskSeqId.setStatus("current")
_CucsMgmtIPv6IfConfigTable_Object = MibTable
cucsMgmtIPv6IfConfigTable = _CucsMgmtIPv6IfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 37)
)
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfConfigTable.setStatus("current")
_CucsMgmtIPv6IfConfigEntry_Object = MibTableRow
cucsMgmtIPv6IfConfigEntry = _CucsMgmtIPv6IfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 37, 1)
)
cucsMgmtIPv6IfConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtIPv6IfConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfConfigEntry.setStatus("current")
_CucsMgmtIPv6IfConfigInstanceId_Type = CucsManagedObjectId
_CucsMgmtIPv6IfConfigInstanceId_Object = MibTableColumn
cucsMgmtIPv6IfConfigInstanceId = _CucsMgmtIPv6IfConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 37, 1, 1),
    _CucsMgmtIPv6IfConfigInstanceId_Type()
)
cucsMgmtIPv6IfConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfConfigInstanceId.setStatus("current")
_CucsMgmtIPv6IfConfigDn_Type = CucsManagedObjectDn
_CucsMgmtIPv6IfConfigDn_Object = MibTableColumn
cucsMgmtIPv6IfConfigDn = _CucsMgmtIPv6IfConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 37, 1, 2),
    _CucsMgmtIPv6IfConfigDn_Type()
)
cucsMgmtIPv6IfConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfConfigDn.setStatus("current")
_CucsMgmtIPv6IfConfigRn_Type = SnmpAdminString
_CucsMgmtIPv6IfConfigRn_Object = MibTableColumn
cucsMgmtIPv6IfConfigRn = _CucsMgmtIPv6IfConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 37, 1, 3),
    _CucsMgmtIPv6IfConfigRn_Type()
)
cucsMgmtIPv6IfConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtIPv6IfConfigRn.setStatus("current")
_CucsMgmtInbandProfileTable_Object = MibTable
cucsMgmtInbandProfileTable = _CucsMgmtInbandProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 38)
)
if mibBuilder.loadTexts:
    cucsMgmtInbandProfileTable.setStatus("current")
_CucsMgmtInbandProfileEntry_Object = MibTableRow
cucsMgmtInbandProfileEntry = _CucsMgmtInbandProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 38, 1)
)
cucsMgmtInbandProfileEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtInbandProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtInbandProfileEntry.setStatus("current")
_CucsMgmtInbandProfileInstanceId_Type = CucsManagedObjectId
_CucsMgmtInbandProfileInstanceId_Object = MibTableColumn
cucsMgmtInbandProfileInstanceId = _CucsMgmtInbandProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 38, 1, 1),
    _CucsMgmtInbandProfileInstanceId_Type()
)
cucsMgmtInbandProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtInbandProfileInstanceId.setStatus("current")
_CucsMgmtInbandProfileDn_Type = CucsManagedObjectDn
_CucsMgmtInbandProfileDn_Object = MibTableColumn
cucsMgmtInbandProfileDn = _CucsMgmtInbandProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 38, 1, 2),
    _CucsMgmtInbandProfileDn_Type()
)
cucsMgmtInbandProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtInbandProfileDn.setStatus("current")
_CucsMgmtInbandProfileRn_Type = SnmpAdminString
_CucsMgmtInbandProfileRn_Object = MibTableColumn
cucsMgmtInbandProfileRn = _CucsMgmtInbandProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 38, 1, 3),
    _CucsMgmtInbandProfileRn_Type()
)
cucsMgmtInbandProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtInbandProfileRn.setStatus("current")
_CucsMgmtInbandProfileDefaultVlanName_Type = SnmpAdminString
_CucsMgmtInbandProfileDefaultVlanName_Object = MibTableColumn
cucsMgmtInbandProfileDefaultVlanName = _CucsMgmtInbandProfileDefaultVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 38, 1, 4),
    _CucsMgmtInbandProfileDefaultVlanName_Type()
)
cucsMgmtInbandProfileDefaultVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtInbandProfileDefaultVlanName.setStatus("current")
_CucsMgmtInbandProfileName_Type = SnmpAdminString
_CucsMgmtInbandProfileName_Object = MibTableColumn
cucsMgmtInbandProfileName = _CucsMgmtInbandProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 38, 1, 5),
    _CucsMgmtInbandProfileName_Type()
)
cucsMgmtInbandProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtInbandProfileName.setStatus("current")
_CucsMgmtInbandProfilePoolName_Type = SnmpAdminString
_CucsMgmtInbandProfilePoolName_Object = MibTableColumn
cucsMgmtInbandProfilePoolName = _CucsMgmtInbandProfilePoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 38, 1, 6),
    _CucsMgmtInbandProfilePoolName_Type()
)
cucsMgmtInbandProfilePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtInbandProfilePoolName.setStatus("current")
_CucsMgmtInterfaceTable_Object = MibTable
cucsMgmtInterfaceTable = _CucsMgmtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 39)
)
if mibBuilder.loadTexts:
    cucsMgmtInterfaceTable.setStatus("current")
_CucsMgmtInterfaceEntry_Object = MibTableRow
cucsMgmtInterfaceEntry = _CucsMgmtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 39, 1)
)
cucsMgmtInterfaceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtInterfaceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtInterfaceEntry.setStatus("current")
_CucsMgmtInterfaceInstanceId_Type = CucsManagedObjectId
_CucsMgmtInterfaceInstanceId_Object = MibTableColumn
cucsMgmtInterfaceInstanceId = _CucsMgmtInterfaceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 39, 1, 1),
    _CucsMgmtInterfaceInstanceId_Type()
)
cucsMgmtInterfaceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtInterfaceInstanceId.setStatus("current")
_CucsMgmtInterfaceDn_Type = CucsManagedObjectDn
_CucsMgmtInterfaceDn_Object = MibTableColumn
cucsMgmtInterfaceDn = _CucsMgmtInterfaceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 39, 1, 2),
    _CucsMgmtInterfaceDn_Type()
)
cucsMgmtInterfaceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtInterfaceDn.setStatus("current")
_CucsMgmtInterfaceRn_Type = SnmpAdminString
_CucsMgmtInterfaceRn_Object = MibTableColumn
cucsMgmtInterfaceRn = _CucsMgmtInterfaceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 39, 1, 3),
    _CucsMgmtInterfaceRn_Type()
)
cucsMgmtInterfaceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtInterfaceRn.setStatus("current")
_CucsMgmtInterfaceConfigMessage_Type = SnmpAdminString
_CucsMgmtInterfaceConfigMessage_Object = MibTableColumn
cucsMgmtInterfaceConfigMessage = _CucsMgmtInterfaceConfigMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 39, 1, 4),
    _CucsMgmtInterfaceConfigMessage_Type()
)
cucsMgmtInterfaceConfigMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtInterfaceConfigMessage.setStatus("current")
_CucsMgmtInterfaceConfigState_Type = CucsMgmtConfigState
_CucsMgmtInterfaceConfigState_Object = MibTableColumn
cucsMgmtInterfaceConfigState = _CucsMgmtInterfaceConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 39, 1, 5),
    _CucsMgmtInterfaceConfigState_Type()
)
cucsMgmtInterfaceConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtInterfaceConfigState.setStatus("current")
_CucsMgmtInterfaceIpV4State_Type = CucsVnicExternalMgmtIPMode
_CucsMgmtInterfaceIpV4State_Object = MibTableColumn
cucsMgmtInterfaceIpV4State = _CucsMgmtInterfaceIpV4State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 39, 1, 6),
    _CucsMgmtInterfaceIpV4State_Type()
)
cucsMgmtInterfaceIpV4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtInterfaceIpV4State.setStatus("current")
_CucsMgmtInterfaceIpV6State_Type = CucsVnicExternalMgmtIPMode
_CucsMgmtInterfaceIpV6State_Object = MibTableColumn
cucsMgmtInterfaceIpV6State = _CucsMgmtInterfaceIpV6State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 39, 1, 7),
    _CucsMgmtInterfaceIpV6State_Type()
)
cucsMgmtInterfaceIpV6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtInterfaceIpV6State.setStatus("current")
_CucsMgmtInterfaceMode_Type = CucsMgmtMode
_CucsMgmtInterfaceMode_Object = MibTableColumn
cucsMgmtInterfaceMode = _CucsMgmtInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 39, 1, 8),
    _CucsMgmtInterfaceMode_Type()
)
cucsMgmtInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtInterfaceMode.setStatus("current")
_CucsMgmtInterfaceOperState_Type = CucsMgmtOperState
_CucsMgmtInterfaceOperState_Object = MibTableColumn
cucsMgmtInterfaceOperState = _CucsMgmtInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 39, 1, 9),
    _CucsMgmtInterfaceOperState_Type()
)
cucsMgmtInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtInterfaceOperState.setStatus("current")
_CucsMgmtInterfaceIsDefaultDerived_Type = TruthValue
_CucsMgmtInterfaceIsDefaultDerived_Object = MibTableColumn
cucsMgmtInterfaceIsDefaultDerived = _CucsMgmtInterfaceIsDefaultDerived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 39, 1, 10),
    _CucsMgmtInterfaceIsDefaultDerived_Type()
)
cucsMgmtInterfaceIsDefaultDerived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtInterfaceIsDefaultDerived.setStatus("current")
_CucsMgmtProfDerivedInterfaceTable_Object = MibTable
cucsMgmtProfDerivedInterfaceTable = _CucsMgmtProfDerivedInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 40)
)
if mibBuilder.loadTexts:
    cucsMgmtProfDerivedInterfaceTable.setStatus("current")
_CucsMgmtProfDerivedInterfaceEntry_Object = MibTableRow
cucsMgmtProfDerivedInterfaceEntry = _CucsMgmtProfDerivedInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 40, 1)
)
cucsMgmtProfDerivedInterfaceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtProfDerivedInterfaceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtProfDerivedInterfaceEntry.setStatus("current")
_CucsMgmtProfDerivedInterfaceInstanceId_Type = CucsManagedObjectId
_CucsMgmtProfDerivedInterfaceInstanceId_Object = MibTableColumn
cucsMgmtProfDerivedInterfaceInstanceId = _CucsMgmtProfDerivedInterfaceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 40, 1, 1),
    _CucsMgmtProfDerivedInterfaceInstanceId_Type()
)
cucsMgmtProfDerivedInterfaceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtProfDerivedInterfaceInstanceId.setStatus("current")
_CucsMgmtProfDerivedInterfaceDn_Type = CucsManagedObjectDn
_CucsMgmtProfDerivedInterfaceDn_Object = MibTableColumn
cucsMgmtProfDerivedInterfaceDn = _CucsMgmtProfDerivedInterfaceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 40, 1, 2),
    _CucsMgmtProfDerivedInterfaceDn_Type()
)
cucsMgmtProfDerivedInterfaceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtProfDerivedInterfaceDn.setStatus("current")
_CucsMgmtProfDerivedInterfaceRn_Type = SnmpAdminString
_CucsMgmtProfDerivedInterfaceRn_Object = MibTableColumn
cucsMgmtProfDerivedInterfaceRn = _CucsMgmtProfDerivedInterfaceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 40, 1, 3),
    _CucsMgmtProfDerivedInterfaceRn_Type()
)
cucsMgmtProfDerivedInterfaceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtProfDerivedInterfaceRn.setStatus("current")
_CucsMgmtProfDerivedInterfaceConfigMessage_Type = SnmpAdminString
_CucsMgmtProfDerivedInterfaceConfigMessage_Object = MibTableColumn
cucsMgmtProfDerivedInterfaceConfigMessage = _CucsMgmtProfDerivedInterfaceConfigMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 40, 1, 4),
    _CucsMgmtProfDerivedInterfaceConfigMessage_Type()
)
cucsMgmtProfDerivedInterfaceConfigMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtProfDerivedInterfaceConfigMessage.setStatus("current")
_CucsMgmtProfDerivedInterfaceConfigState_Type = CucsMgmtConfigState
_CucsMgmtProfDerivedInterfaceConfigState_Object = MibTableColumn
cucsMgmtProfDerivedInterfaceConfigState = _CucsMgmtProfDerivedInterfaceConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 40, 1, 5),
    _CucsMgmtProfDerivedInterfaceConfigState_Type()
)
cucsMgmtProfDerivedInterfaceConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtProfDerivedInterfaceConfigState.setStatus("current")
_CucsMgmtProfDerivedInterfaceIpV4State_Type = CucsVnicExternalMgmtIPMode
_CucsMgmtProfDerivedInterfaceIpV4State_Object = MibTableColumn
cucsMgmtProfDerivedInterfaceIpV4State = _CucsMgmtProfDerivedInterfaceIpV4State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 40, 1, 6),
    _CucsMgmtProfDerivedInterfaceIpV4State_Type()
)
cucsMgmtProfDerivedInterfaceIpV4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtProfDerivedInterfaceIpV4State.setStatus("current")
_CucsMgmtProfDerivedInterfaceIpV6State_Type = CucsVnicExternalMgmtIPMode
_CucsMgmtProfDerivedInterfaceIpV6State_Object = MibTableColumn
cucsMgmtProfDerivedInterfaceIpV6State = _CucsMgmtProfDerivedInterfaceIpV6State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 40, 1, 7),
    _CucsMgmtProfDerivedInterfaceIpV6State_Type()
)
cucsMgmtProfDerivedInterfaceIpV6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtProfDerivedInterfaceIpV6State.setStatus("current")
_CucsMgmtProfDerivedInterfaceMode_Type = CucsMgmtMode
_CucsMgmtProfDerivedInterfaceMode_Object = MibTableColumn
cucsMgmtProfDerivedInterfaceMode = _CucsMgmtProfDerivedInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 40, 1, 8),
    _CucsMgmtProfDerivedInterfaceMode_Type()
)
cucsMgmtProfDerivedInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtProfDerivedInterfaceMode.setStatus("current")
_CucsMgmtProfDerivedInterfaceOperState_Type = CucsMgmtOperState
_CucsMgmtProfDerivedInterfaceOperState_Object = MibTableColumn
cucsMgmtProfDerivedInterfaceOperState = _CucsMgmtProfDerivedInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 40, 1, 9),
    _CucsMgmtProfDerivedInterfaceOperState_Type()
)
cucsMgmtProfDerivedInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtProfDerivedInterfaceOperState.setStatus("current")
_CucsMgmtVnetTable_Object = MibTable
cucsMgmtVnetTable = _CucsMgmtVnetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 41)
)
if mibBuilder.loadTexts:
    cucsMgmtVnetTable.setStatus("current")
_CucsMgmtVnetEntry_Object = MibTableRow
cucsMgmtVnetEntry = _CucsMgmtVnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 41, 1)
)
cucsMgmtVnetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtVnetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtVnetEntry.setStatus("current")
_CucsMgmtVnetInstanceId_Type = CucsManagedObjectId
_CucsMgmtVnetInstanceId_Object = MibTableColumn
cucsMgmtVnetInstanceId = _CucsMgmtVnetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 41, 1, 1),
    _CucsMgmtVnetInstanceId_Type()
)
cucsMgmtVnetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtVnetInstanceId.setStatus("current")
_CucsMgmtVnetDn_Type = CucsManagedObjectDn
_CucsMgmtVnetDn_Object = MibTableColumn
cucsMgmtVnetDn = _CucsMgmtVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 41, 1, 2),
    _CucsMgmtVnetDn_Type()
)
cucsMgmtVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtVnetDn.setStatus("current")
_CucsMgmtVnetRn_Type = SnmpAdminString
_CucsMgmtVnetRn_Object = MibTableColumn
cucsMgmtVnetRn = _CucsMgmtVnetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 41, 1, 3),
    _CucsMgmtVnetRn_Type()
)
cucsMgmtVnetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtVnetRn.setStatus("current")
_CucsMgmtVnetConfigState_Type = CucsMgmtConfigState
_CucsMgmtVnetConfigState_Object = MibTableColumn
cucsMgmtVnetConfigState = _CucsMgmtVnetConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 41, 1, 4),
    _CucsMgmtVnetConfigState_Type()
)
cucsMgmtVnetConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtVnetConfigState.setStatus("current")
_CucsMgmtVnetId_Type = Gauge32
_CucsMgmtVnetId_Object = MibTableColumn
cucsMgmtVnetId = _CucsMgmtVnetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 41, 1, 5),
    _CucsMgmtVnetId_Type()
)
cucsMgmtVnetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtVnetId.setStatus("current")
_CucsMgmtVnetName_Type = SnmpAdminString
_CucsMgmtVnetName_Object = MibTableColumn
cucsMgmtVnetName = _CucsMgmtVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 41, 1, 6),
    _CucsMgmtVnetName_Type()
)
cucsMgmtVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtVnetName.setStatus("current")
_CucsMgmtBackupExportExtPolicyTable_Object = MibTable
cucsMgmtBackupExportExtPolicyTable = _CucsMgmtBackupExportExtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 42)
)
if mibBuilder.loadTexts:
    cucsMgmtBackupExportExtPolicyTable.setStatus("current")
_CucsMgmtBackupExportExtPolicyEntry_Object = MibTableRow
cucsMgmtBackupExportExtPolicyEntry = _CucsMgmtBackupExportExtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 42, 1)
)
cucsMgmtBackupExportExtPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtBackupExportExtPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtBackupExportExtPolicyEntry.setStatus("current")
_CucsMgmtBackupExportExtPolicyInstanceId_Type = CucsManagedObjectId
_CucsMgmtBackupExportExtPolicyInstanceId_Object = MibTableColumn
cucsMgmtBackupExportExtPolicyInstanceId = _CucsMgmtBackupExportExtPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 42, 1, 1),
    _CucsMgmtBackupExportExtPolicyInstanceId_Type()
)
cucsMgmtBackupExportExtPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtBackupExportExtPolicyInstanceId.setStatus("current")
_CucsMgmtBackupExportExtPolicyDn_Type = CucsManagedObjectDn
_CucsMgmtBackupExportExtPolicyDn_Object = MibTableColumn
cucsMgmtBackupExportExtPolicyDn = _CucsMgmtBackupExportExtPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 42, 1, 2),
    _CucsMgmtBackupExportExtPolicyDn_Type()
)
cucsMgmtBackupExportExtPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupExportExtPolicyDn.setStatus("current")
_CucsMgmtBackupExportExtPolicyRn_Type = SnmpAdminString
_CucsMgmtBackupExportExtPolicyRn_Object = MibTableColumn
cucsMgmtBackupExportExtPolicyRn = _CucsMgmtBackupExportExtPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 42, 1, 3),
    _CucsMgmtBackupExportExtPolicyRn_Type()
)
cucsMgmtBackupExportExtPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupExportExtPolicyRn.setStatus("current")
_CucsMgmtBackupExportExtPolicyAdminState_Type = CucsMgmtAdminState
_CucsMgmtBackupExportExtPolicyAdminState_Object = MibTableColumn
cucsMgmtBackupExportExtPolicyAdminState = _CucsMgmtBackupExportExtPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 42, 1, 4),
    _CucsMgmtBackupExportExtPolicyAdminState_Type()
)
cucsMgmtBackupExportExtPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupExportExtPolicyAdminState.setStatus("current")
_CucsMgmtBackupExportExtPolicyDescr_Type = SnmpAdminString
_CucsMgmtBackupExportExtPolicyDescr_Object = MibTableColumn
cucsMgmtBackupExportExtPolicyDescr = _CucsMgmtBackupExportExtPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 42, 1, 5),
    _CucsMgmtBackupExportExtPolicyDescr_Type()
)
cucsMgmtBackupExportExtPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupExportExtPolicyDescr.setStatus("current")
_CucsMgmtBackupExportExtPolicyFrequency_Type = Gauge32
_CucsMgmtBackupExportExtPolicyFrequency_Object = MibTableColumn
cucsMgmtBackupExportExtPolicyFrequency = _CucsMgmtBackupExportExtPolicyFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 42, 1, 6),
    _CucsMgmtBackupExportExtPolicyFrequency_Type()
)
cucsMgmtBackupExportExtPolicyFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupExportExtPolicyFrequency.setStatus("current")
_CucsMgmtBackupExportExtPolicyIntId_Type = SnmpAdminString
_CucsMgmtBackupExportExtPolicyIntId_Object = MibTableColumn
cucsMgmtBackupExportExtPolicyIntId = _CucsMgmtBackupExportExtPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 42, 1, 7),
    _CucsMgmtBackupExportExtPolicyIntId_Type()
)
cucsMgmtBackupExportExtPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupExportExtPolicyIntId.setStatus("current")
_CucsMgmtBackupExportExtPolicyName_Type = SnmpAdminString
_CucsMgmtBackupExportExtPolicyName_Object = MibTableColumn
cucsMgmtBackupExportExtPolicyName = _CucsMgmtBackupExportExtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 42, 1, 8),
    _CucsMgmtBackupExportExtPolicyName_Type()
)
cucsMgmtBackupExportExtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupExportExtPolicyName.setStatus("current")
_CucsMgmtBackupExportExtPolicyPolicyLevel_Type = Gauge32
_CucsMgmtBackupExportExtPolicyPolicyLevel_Object = MibTableColumn
cucsMgmtBackupExportExtPolicyPolicyLevel = _CucsMgmtBackupExportExtPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 42, 1, 9),
    _CucsMgmtBackupExportExtPolicyPolicyLevel_Type()
)
cucsMgmtBackupExportExtPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupExportExtPolicyPolicyLevel.setStatus("current")
_CucsMgmtBackupExportExtPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsMgmtBackupExportExtPolicyPolicyOwner_Object = MibTableColumn
cucsMgmtBackupExportExtPolicyPolicyOwner = _CucsMgmtBackupExportExtPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 42, 1, 10),
    _CucsMgmtBackupExportExtPolicyPolicyOwner_Type()
)
cucsMgmtBackupExportExtPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupExportExtPolicyPolicyOwner.setStatus("current")
_CucsMgmtBackupPolicyConfigTable_Object = MibTable
cucsMgmtBackupPolicyConfigTable = _CucsMgmtBackupPolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43)
)
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigTable.setStatus("current")
_CucsMgmtBackupPolicyConfigEntry_Object = MibTableRow
cucsMgmtBackupPolicyConfigEntry = _CucsMgmtBackupPolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1)
)
cucsMgmtBackupPolicyConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtBackupPolicyConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigEntry.setStatus("current")
_CucsMgmtBackupPolicyConfigInstanceId_Type = CucsManagedObjectId
_CucsMgmtBackupPolicyConfigInstanceId_Object = MibTableColumn
cucsMgmtBackupPolicyConfigInstanceId = _CucsMgmtBackupPolicyConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 1),
    _CucsMgmtBackupPolicyConfigInstanceId_Type()
)
cucsMgmtBackupPolicyConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigInstanceId.setStatus("current")
_CucsMgmtBackupPolicyConfigDn_Type = CucsManagedObjectDn
_CucsMgmtBackupPolicyConfigDn_Object = MibTableColumn
cucsMgmtBackupPolicyConfigDn = _CucsMgmtBackupPolicyConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 2),
    _CucsMgmtBackupPolicyConfigDn_Type()
)
cucsMgmtBackupPolicyConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigDn.setStatus("current")
_CucsMgmtBackupPolicyConfigRn_Type = SnmpAdminString
_CucsMgmtBackupPolicyConfigRn_Object = MibTableColumn
cucsMgmtBackupPolicyConfigRn = _CucsMgmtBackupPolicyConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 3),
    _CucsMgmtBackupPolicyConfigRn_Type()
)
cucsMgmtBackupPolicyConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigRn.setStatus("current")
_CucsMgmtBackupPolicyConfigAdminState_Type = CucsTrigAdminState
_CucsMgmtBackupPolicyConfigAdminState_Object = MibTableColumn
cucsMgmtBackupPolicyConfigAdminState = _CucsMgmtBackupPolicyConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 4),
    _CucsMgmtBackupPolicyConfigAdminState_Type()
)
cucsMgmtBackupPolicyConfigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigAdminState.setStatus("current")
_CucsMgmtBackupPolicyConfigAutoDelete_Type = TruthValue
_CucsMgmtBackupPolicyConfigAutoDelete_Object = MibTableColumn
cucsMgmtBackupPolicyConfigAutoDelete = _CucsMgmtBackupPolicyConfigAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 5),
    _CucsMgmtBackupPolicyConfigAutoDelete_Type()
)
cucsMgmtBackupPolicyConfigAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigAutoDelete.setStatus("current")
_CucsMgmtBackupPolicyConfigBackupDate_Type = DateAndTime
_CucsMgmtBackupPolicyConfigBackupDate_Object = MibTableColumn
cucsMgmtBackupPolicyConfigBackupDate = _CucsMgmtBackupPolicyConfigBackupDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 6),
    _CucsMgmtBackupPolicyConfigBackupDate_Type()
)
cucsMgmtBackupPolicyConfigBackupDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigBackupDate.setStatus("current")
_CucsMgmtBackupPolicyConfigBackupIssue_Type = CucsMgmtBackupIssue
_CucsMgmtBackupPolicyConfigBackupIssue_Object = MibTableColumn
cucsMgmtBackupPolicyConfigBackupIssue = _CucsMgmtBackupPolicyConfigBackupIssue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 7),
    _CucsMgmtBackupPolicyConfigBackupIssue_Type()
)
cucsMgmtBackupPolicyConfigBackupIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigBackupIssue.setStatus("current")
_CucsMgmtBackupPolicyConfigDescr_Type = SnmpAdminString
_CucsMgmtBackupPolicyConfigDescr_Object = MibTableColumn
cucsMgmtBackupPolicyConfigDescr = _CucsMgmtBackupPolicyConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 8),
    _CucsMgmtBackupPolicyConfigDescr_Type()
)
cucsMgmtBackupPolicyConfigDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigDescr.setStatus("current")
_CucsMgmtBackupPolicyConfigIgnoreCap_Type = TruthValue
_CucsMgmtBackupPolicyConfigIgnoreCap_Object = MibTableColumn
cucsMgmtBackupPolicyConfigIgnoreCap = _CucsMgmtBackupPolicyConfigIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 9),
    _CucsMgmtBackupPolicyConfigIgnoreCap_Type()
)
cucsMgmtBackupPolicyConfigIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigIgnoreCap.setStatus("current")
_CucsMgmtBackupPolicyConfigIntId_Type = SnmpAdminString
_CucsMgmtBackupPolicyConfigIntId_Object = MibTableColumn
cucsMgmtBackupPolicyConfigIntId = _CucsMgmtBackupPolicyConfigIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 10),
    _CucsMgmtBackupPolicyConfigIntId_Type()
)
cucsMgmtBackupPolicyConfigIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigIntId.setStatus("current")
_CucsMgmtBackupPolicyConfigName_Type = SnmpAdminString
_CucsMgmtBackupPolicyConfigName_Object = MibTableColumn
cucsMgmtBackupPolicyConfigName = _CucsMgmtBackupPolicyConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 11),
    _CucsMgmtBackupPolicyConfigName_Type()
)
cucsMgmtBackupPolicyConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigName.setStatus("current")
_CucsMgmtBackupPolicyConfigOperScheduler_Type = SnmpAdminString
_CucsMgmtBackupPolicyConfigOperScheduler_Object = MibTableColumn
cucsMgmtBackupPolicyConfigOperScheduler = _CucsMgmtBackupPolicyConfigOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 12),
    _CucsMgmtBackupPolicyConfigOperScheduler_Type()
)
cucsMgmtBackupPolicyConfigOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigOperScheduler.setStatus("current")
_CucsMgmtBackupPolicyConfigOperState_Type = CucsTrigTrigOperState
_CucsMgmtBackupPolicyConfigOperState_Object = MibTableColumn
cucsMgmtBackupPolicyConfigOperState = _CucsMgmtBackupPolicyConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 13),
    _CucsMgmtBackupPolicyConfigOperState_Type()
)
cucsMgmtBackupPolicyConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigOperState.setStatus("current")
_CucsMgmtBackupPolicyConfigPolicyLevel_Type = Gauge32
_CucsMgmtBackupPolicyConfigPolicyLevel_Object = MibTableColumn
cucsMgmtBackupPolicyConfigPolicyLevel = _CucsMgmtBackupPolicyConfigPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 14),
    _CucsMgmtBackupPolicyConfigPolicyLevel_Type()
)
cucsMgmtBackupPolicyConfigPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigPolicyLevel.setStatus("current")
_CucsMgmtBackupPolicyConfigPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsMgmtBackupPolicyConfigPolicyOwner_Object = MibTableColumn
cucsMgmtBackupPolicyConfigPolicyOwner = _CucsMgmtBackupPolicyConfigPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 15),
    _CucsMgmtBackupPolicyConfigPolicyOwner_Type()
)
cucsMgmtBackupPolicyConfigPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigPolicyOwner.setStatus("current")
_CucsMgmtBackupPolicyConfigScheduler_Type = SnmpAdminString
_CucsMgmtBackupPolicyConfigScheduler_Object = MibTableColumn
cucsMgmtBackupPolicyConfigScheduler = _CucsMgmtBackupPolicyConfigScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 43, 1, 16),
    _CucsMgmtBackupPolicyConfigScheduler_Type()
)
cucsMgmtBackupPolicyConfigScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtBackupPolicyConfigScheduler.setStatus("current")
_CucsMgmtCimcSecureBootTable_Object = MibTable
cucsMgmtCimcSecureBootTable = _CucsMgmtCimcSecureBootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 44)
)
if mibBuilder.loadTexts:
    cucsMgmtCimcSecureBootTable.setStatus("current")
_CucsMgmtCimcSecureBootEntry_Object = MibTableRow
cucsMgmtCimcSecureBootEntry = _CucsMgmtCimcSecureBootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 44, 1)
)
cucsMgmtCimcSecureBootEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtCimcSecureBootInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtCimcSecureBootEntry.setStatus("current")
_CucsMgmtCimcSecureBootInstanceId_Type = CucsManagedObjectId
_CucsMgmtCimcSecureBootInstanceId_Object = MibTableColumn
cucsMgmtCimcSecureBootInstanceId = _CucsMgmtCimcSecureBootInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 44, 1, 1),
    _CucsMgmtCimcSecureBootInstanceId_Type()
)
cucsMgmtCimcSecureBootInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtCimcSecureBootInstanceId.setStatus("current")
_CucsMgmtCimcSecureBootDn_Type = CucsManagedObjectDn
_CucsMgmtCimcSecureBootDn_Object = MibTableColumn
cucsMgmtCimcSecureBootDn = _CucsMgmtCimcSecureBootDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 44, 1, 2),
    _CucsMgmtCimcSecureBootDn_Type()
)
cucsMgmtCimcSecureBootDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCimcSecureBootDn.setStatus("current")
_CucsMgmtCimcSecureBootRn_Type = SnmpAdminString
_CucsMgmtCimcSecureBootRn_Object = MibTableColumn
cucsMgmtCimcSecureBootRn = _CucsMgmtCimcSecureBootRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 44, 1, 3),
    _CucsMgmtCimcSecureBootRn_Type()
)
cucsMgmtCimcSecureBootRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCimcSecureBootRn.setStatus("current")
_CucsMgmtCimcSecureBootAdminState_Type = CucsMgmtCimcSecureBootAdminState
_CucsMgmtCimcSecureBootAdminState_Object = MibTableColumn
cucsMgmtCimcSecureBootAdminState = _CucsMgmtCimcSecureBootAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 44, 1, 4),
    _CucsMgmtCimcSecureBootAdminState_Type()
)
cucsMgmtCimcSecureBootAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCimcSecureBootAdminState.setStatus("current")
_CucsMgmtCimcSecureBootOperState_Type = CucsMgmtSecureBootOperState
_CucsMgmtCimcSecureBootOperState_Object = MibTableColumn
cucsMgmtCimcSecureBootOperState = _CucsMgmtCimcSecureBootOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 44, 1, 5),
    _CucsMgmtCimcSecureBootOperState_Type()
)
cucsMgmtCimcSecureBootOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtCimcSecureBootOperState.setStatus("current")
_CucsMgmtHealthAttrTable_Object = MibTable
cucsMgmtHealthAttrTable = _CucsMgmtHealthAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 66)
)
if mibBuilder.loadTexts:
    cucsMgmtHealthAttrTable.setStatus("current")
_CucsMgmtHealthAttrEntry_Object = MibTableRow
cucsMgmtHealthAttrEntry = _CucsMgmtHealthAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 66, 1)
)
cucsMgmtHealthAttrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtHealthAttrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtHealthAttrEntry.setStatus("current")
_CucsMgmtHealthAttrInstanceId_Type = CucsManagedObjectId
_CucsMgmtHealthAttrInstanceId_Object = MibTableColumn
cucsMgmtHealthAttrInstanceId = _CucsMgmtHealthAttrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 66, 1, 1),
    _CucsMgmtHealthAttrInstanceId_Type()
)
cucsMgmtHealthAttrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtHealthAttrInstanceId.setStatus("current")
_CucsMgmtHealthAttrDn_Type = CucsManagedObjectDn
_CucsMgmtHealthAttrDn_Object = MibTableColumn
cucsMgmtHealthAttrDn = _CucsMgmtHealthAttrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 66, 1, 2),
    _CucsMgmtHealthAttrDn_Type()
)
cucsMgmtHealthAttrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtHealthAttrDn.setStatus("current")
_CucsMgmtHealthAttrRn_Type = SnmpAdminString
_CucsMgmtHealthAttrRn_Object = MibTableColumn
cucsMgmtHealthAttrRn = _CucsMgmtHealthAttrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 66, 1, 3),
    _CucsMgmtHealthAttrRn_Type()
)
cucsMgmtHealthAttrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtHealthAttrRn.setStatus("current")
_CucsMgmtHealthAttrDescription_Type = SnmpAdminString
_CucsMgmtHealthAttrDescription_Object = MibTableColumn
cucsMgmtHealthAttrDescription = _CucsMgmtHealthAttrDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 66, 1, 4),
    _CucsMgmtHealthAttrDescription_Type()
)
cucsMgmtHealthAttrDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtHealthAttrDescription.setStatus("current")
_CucsMgmtHealthAttrName_Type = SnmpAdminString
_CucsMgmtHealthAttrName_Object = MibTableColumn
cucsMgmtHealthAttrName = _CucsMgmtHealthAttrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 66, 1, 5),
    _CucsMgmtHealthAttrName_Type()
)
cucsMgmtHealthAttrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtHealthAttrName.setStatus("current")
_CucsMgmtHealthAttrSeverity_Type = CucsConditionSeverity
_CucsMgmtHealthAttrSeverity_Object = MibTableColumn
cucsMgmtHealthAttrSeverity = _CucsMgmtHealthAttrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 66, 1, 6),
    _CucsMgmtHealthAttrSeverity_Type()
)
cucsMgmtHealthAttrSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtHealthAttrSeverity.setStatus("current")
_CucsMgmtHealthAttrValue_Type = SnmpAdminString
_CucsMgmtHealthAttrValue_Object = MibTableColumn
cucsMgmtHealthAttrValue = _CucsMgmtHealthAttrValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 66, 1, 7),
    _CucsMgmtHealthAttrValue_Type()
)
cucsMgmtHealthAttrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtHealthAttrValue.setStatus("current")
_CucsMgmtHealthStatusTable_Object = MibTable
cucsMgmtHealthStatusTable = _CucsMgmtHealthStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 67)
)
if mibBuilder.loadTexts:
    cucsMgmtHealthStatusTable.setStatus("current")
_CucsMgmtHealthStatusEntry_Object = MibTableRow
cucsMgmtHealthStatusEntry = _CucsMgmtHealthStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 67, 1)
)
cucsMgmtHealthStatusEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MGMT-MIB", "cucsMgmtHealthStatusInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMgmtHealthStatusEntry.setStatus("current")
_CucsMgmtHealthStatusInstanceId_Type = CucsManagedObjectId
_CucsMgmtHealthStatusInstanceId_Object = MibTableColumn
cucsMgmtHealthStatusInstanceId = _CucsMgmtHealthStatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 67, 1, 1),
    _CucsMgmtHealthStatusInstanceId_Type()
)
cucsMgmtHealthStatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMgmtHealthStatusInstanceId.setStatus("current")
_CucsMgmtHealthStatusDn_Type = CucsManagedObjectDn
_CucsMgmtHealthStatusDn_Object = MibTableColumn
cucsMgmtHealthStatusDn = _CucsMgmtHealthStatusDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 67, 1, 2),
    _CucsMgmtHealthStatusDn_Type()
)
cucsMgmtHealthStatusDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtHealthStatusDn.setStatus("current")
_CucsMgmtHealthStatusRn_Type = SnmpAdminString
_CucsMgmtHealthStatusRn_Object = MibTableColumn
cucsMgmtHealthStatusRn = _CucsMgmtHealthStatusRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 67, 1, 3),
    _CucsMgmtHealthStatusRn_Type()
)
cucsMgmtHealthStatusRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtHealthStatusRn.setStatus("current")
_CucsMgmtHealthStatusHealthQualifier_Type = SnmpAdminString
_CucsMgmtHealthStatusHealthQualifier_Object = MibTableColumn
cucsMgmtHealthStatusHealthQualifier = _CucsMgmtHealthStatusHealthQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 67, 1, 4),
    _CucsMgmtHealthStatusHealthQualifier_Type()
)
cucsMgmtHealthStatusHealthQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtHealthStatusHealthQualifier.setStatus("current")
_CucsMgmtHealthStatusHealthSeverity_Type = CucsConditionSeverity
_CucsMgmtHealthStatusHealthSeverity_Object = MibTableColumn
cucsMgmtHealthStatusHealthSeverity = _CucsMgmtHealthStatusHealthSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 31, 67, 1, 5),
    _CucsMgmtHealthStatusHealthSeverity_Type()
)
cucsMgmtHealthStatusHealthSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMgmtHealthStatusHealthSeverity.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-MGMT-MIB",
    **{"cucsMgmtObjects": cucsMgmtObjects,
       "cucsMgmtAccessPolicyTable": cucsMgmtAccessPolicyTable,
       "cucsMgmtAccessPolicyEntry": cucsMgmtAccessPolicyEntry,
       "cucsMgmtAccessPolicyInstanceId": cucsMgmtAccessPolicyInstanceId,
       "cucsMgmtAccessPolicyDn": cucsMgmtAccessPolicyDn,
       "cucsMgmtAccessPolicyRn": cucsMgmtAccessPolicyRn,
       "cucsMgmtAccessPolicyItemTable": cucsMgmtAccessPolicyItemTable,
       "cucsMgmtAccessPolicyItemEntry": cucsMgmtAccessPolicyItemEntry,
       "cucsMgmtAccessPolicyItemInstanceId": cucsMgmtAccessPolicyItemInstanceId,
       "cucsMgmtAccessPolicyItemDn": cucsMgmtAccessPolicyItemDn,
       "cucsMgmtAccessPolicyItemRn": cucsMgmtAccessPolicyItemRn,
       "cucsMgmtAccessPolicyItemDescr": cucsMgmtAccessPolicyItemDescr,
       "cucsMgmtAccessPolicyItemIntId": cucsMgmtAccessPolicyItemIntId,
       "cucsMgmtAccessPolicyItemIpPoolName": cucsMgmtAccessPolicyItemIpPoolName,
       "cucsMgmtAccessPolicyItemName": cucsMgmtAccessPolicyItemName,
       "cucsMgmtAccessPolicyItemSubject": cucsMgmtAccessPolicyItemSubject,
       "cucsMgmtAccessPolicyItemPolicyLevel": cucsMgmtAccessPolicyItemPolicyLevel,
       "cucsMgmtAccessPolicyItemPolicyOwner": cucsMgmtAccessPolicyItemPolicyOwner,
       "cucsMgmtAccessPortTable": cucsMgmtAccessPortTable,
       "cucsMgmtAccessPortEntry": cucsMgmtAccessPortEntry,
       "cucsMgmtAccessPortInstanceId": cucsMgmtAccessPortInstanceId,
       "cucsMgmtAccessPortDn": cucsMgmtAccessPortDn,
       "cucsMgmtAccessPortRn": cucsMgmtAccessPortRn,
       "cucsMgmtAccessPortPort": cucsMgmtAccessPortPort,
       "cucsMgmtAccessPortProtocol": cucsMgmtAccessPortProtocol,
       "cucsMgmtBackupTable": cucsMgmtBackupTable,
       "cucsMgmtBackupEntry": cucsMgmtBackupEntry,
       "cucsMgmtBackupInstanceId": cucsMgmtBackupInstanceId,
       "cucsMgmtBackupDn": cucsMgmtBackupDn,
       "cucsMgmtBackupRn": cucsMgmtBackupRn,
       "cucsMgmtBackupAdminState": cucsMgmtBackupAdminState,
       "cucsMgmtBackupDescr": cucsMgmtBackupDescr,
       "cucsMgmtBackupFsmDescr": cucsMgmtBackupFsmDescr,
       "cucsMgmtBackupFsmPrev": cucsMgmtBackupFsmPrev,
       "cucsMgmtBackupFsmProgr": cucsMgmtBackupFsmProgr,
       "cucsMgmtBackupFsmRmtInvErrCode": cucsMgmtBackupFsmRmtInvErrCode,
       "cucsMgmtBackupFsmRmtInvErrDescr": cucsMgmtBackupFsmRmtInvErrDescr,
       "cucsMgmtBackupFsmRmtInvRslt": cucsMgmtBackupFsmRmtInvRslt,
       "cucsMgmtBackupFsmStageDescr": cucsMgmtBackupFsmStageDescr,
       "cucsMgmtBackupFsmStamp": cucsMgmtBackupFsmStamp,
       "cucsMgmtBackupFsmStatus": cucsMgmtBackupFsmStatus,
       "cucsMgmtBackupFsmTry": cucsMgmtBackupFsmTry,
       "cucsMgmtBackupHostname": cucsMgmtBackupHostname,
       "cucsMgmtBackupIntId": cucsMgmtBackupIntId,
       "cucsMgmtBackupJob": cucsMgmtBackupJob,
       "cucsMgmtBackupName": cucsMgmtBackupName,
       "cucsMgmtBackupPostAction": cucsMgmtBackupPostAction,
       "cucsMgmtBackupPreservePooledValues": cucsMgmtBackupPreservePooledValues,
       "cucsMgmtBackupProto": cucsMgmtBackupProto,
       "cucsMgmtBackupPwd": cucsMgmtBackupPwd,
       "cucsMgmtBackupRemoteFile": cucsMgmtBackupRemoteFile,
       "cucsMgmtBackupType": cucsMgmtBackupType,
       "cucsMgmtBackupUser": cucsMgmtBackupUser,
       "cucsMgmtBackupMaxFiles": cucsMgmtBackupMaxFiles,
       "cucsMgmtBackupOwnerPolicy": cucsMgmtBackupOwnerPolicy,
       "cucsMgmtBackupPolicyLevel": cucsMgmtBackupPolicyLevel,
       "cucsMgmtBackupPolicyOwner": cucsMgmtBackupPolicyOwner,
       "cucsMgmtBackupBackupstatus": cucsMgmtBackupBackupstatus,
       "cucsMgmtBackupFsmTaskTable": cucsMgmtBackupFsmTaskTable,
       "cucsMgmtBackupFsmTaskEntry": cucsMgmtBackupFsmTaskEntry,
       "cucsMgmtBackupFsmTaskInstanceId": cucsMgmtBackupFsmTaskInstanceId,
       "cucsMgmtBackupFsmTaskDn": cucsMgmtBackupFsmTaskDn,
       "cucsMgmtBackupFsmTaskRn": cucsMgmtBackupFsmTaskRn,
       "cucsMgmtBackupFsmTaskCompletion": cucsMgmtBackupFsmTaskCompletion,
       "cucsMgmtBackupFsmTaskFlags": cucsMgmtBackupFsmTaskFlags,
       "cucsMgmtBackupFsmTaskItem": cucsMgmtBackupFsmTaskItem,
       "cucsMgmtBackupFsmTaskSeqId": cucsMgmtBackupFsmTaskSeqId,
       "cucsMgmtControllerTable": cucsMgmtControllerTable,
       "cucsMgmtControllerEntry": cucsMgmtControllerEntry,
       "cucsMgmtControllerInstanceId": cucsMgmtControllerInstanceId,
       "cucsMgmtControllerDn": cucsMgmtControllerDn,
       "cucsMgmtControllerRn": cucsMgmtControllerRn,
       "cucsMgmtControllerFsmDescr": cucsMgmtControllerFsmDescr,
       "cucsMgmtControllerFsmFlags": cucsMgmtControllerFsmFlags,
       "cucsMgmtControllerFsmPrev": cucsMgmtControllerFsmPrev,
       "cucsMgmtControllerFsmProgr": cucsMgmtControllerFsmProgr,
       "cucsMgmtControllerFsmRmtInvErrCode": cucsMgmtControllerFsmRmtInvErrCode,
       "cucsMgmtControllerFsmRmtInvErrDescr": cucsMgmtControllerFsmRmtInvErrDescr,
       "cucsMgmtControllerFsmRmtInvRslt": cucsMgmtControllerFsmRmtInvRslt,
       "cucsMgmtControllerFsmStageDescr": cucsMgmtControllerFsmStageDescr,
       "cucsMgmtControllerFsmStamp": cucsMgmtControllerFsmStamp,
       "cucsMgmtControllerFsmStatus": cucsMgmtControllerFsmStatus,
       "cucsMgmtControllerFsmTry": cucsMgmtControllerFsmTry,
       "cucsMgmtControllerGuid": cucsMgmtControllerGuid,
       "cucsMgmtControllerModel": cucsMgmtControllerModel,
       "cucsMgmtControllerRevision": cucsMgmtControllerRevision,
       "cucsMgmtControllerSerial": cucsMgmtControllerSerial,
       "cucsMgmtControllerSubject": cucsMgmtControllerSubject,
       "cucsMgmtControllerVendor": cucsMgmtControllerVendor,
       "cucsMgmtControllerOperConn": cucsMgmtControllerOperConn,
       "cucsMgmtControllerDimmBlacklistingOperState": cucsMgmtControllerDimmBlacklistingOperState,
       "cucsMgmtControllerStorageOobInterfaceSupported": cucsMgmtControllerStorageOobInterfaceSupported,
       "cucsMgmtControllerStorageSubsystemState": cucsMgmtControllerStorageSubsystemState,
       "cucsMgmtControllerStorageOobConfigSupported": cucsMgmtControllerStorageOobConfigSupported,
       "cucsMgmtControllerId": cucsMgmtControllerId,
       "cucsMgmtControllerDesiredMaintenanceMode": cucsMgmtControllerDesiredMaintenanceMode,
       "cucsMgmtControllerLastRebootReason": cucsMgmtControllerLastRebootReason,
       "cucsMgmtControllerPowerFanSpeedPolicySupported": cucsMgmtControllerPowerFanSpeedPolicySupported,
       "cucsMgmtControllerSupportedCapability": cucsMgmtControllerSupportedCapability,
       "cucsMgmtControllerFsmTaskTable": cucsMgmtControllerFsmTaskTable,
       "cucsMgmtControllerFsmTaskEntry": cucsMgmtControllerFsmTaskEntry,
       "cucsMgmtControllerFsmTaskInstanceId": cucsMgmtControllerFsmTaskInstanceId,
       "cucsMgmtControllerFsmTaskDn": cucsMgmtControllerFsmTaskDn,
       "cucsMgmtControllerFsmTaskRn": cucsMgmtControllerFsmTaskRn,
       "cucsMgmtControllerFsmTaskCompletion": cucsMgmtControllerFsmTaskCompletion,
       "cucsMgmtControllerFsmTaskFlags": cucsMgmtControllerFsmTaskFlags,
       "cucsMgmtControllerFsmTaskItem": cucsMgmtControllerFsmTaskItem,
       "cucsMgmtControllerFsmTaskSeqId": cucsMgmtControllerFsmTaskSeqId,
       "cucsMgmtEntityTable": cucsMgmtEntityTable,
       "cucsMgmtEntityEntry": cucsMgmtEntityEntry,
       "cucsMgmtEntityInstanceId": cucsMgmtEntityInstanceId,
       "cucsMgmtEntityDn": cucsMgmtEntityDn,
       "cucsMgmtEntityRn": cucsMgmtEntityRn,
       "cucsMgmtEntityChassis1": cucsMgmtEntityChassis1,
       "cucsMgmtEntityChassis2": cucsMgmtEntityChassis2,
       "cucsMgmtEntityChassis3": cucsMgmtEntityChassis3,
       "cucsMgmtEntityChassisDeviceIoState1": cucsMgmtEntityChassisDeviceIoState1,
       "cucsMgmtEntityChassisDeviceIoState2": cucsMgmtEntityChassisDeviceIoState2,
       "cucsMgmtEntityChassisDeviceIoState3": cucsMgmtEntityChassisDeviceIoState3,
       "cucsMgmtEntityHaFailureReason": cucsMgmtEntityHaFailureReason,
       "cucsMgmtEntityHaReadiness": cucsMgmtEntityHaReadiness,
       "cucsMgmtEntityHaReady": cucsMgmtEntityHaReady,
       "cucsMgmtEntityId": cucsMgmtEntityId,
       "cucsMgmtEntityLeadership": cucsMgmtEntityLeadership,
       "cucsMgmtEntityMgmtServicesState": cucsMgmtEntityMgmtServicesState,
       "cucsMgmtEntityProblems": cucsMgmtEntityProblems,
       "cucsMgmtEntityState": cucsMgmtEntityState,
       "cucsMgmtEntityUmbilicalState": cucsMgmtEntityUmbilicalState,
       "cucsMgmtEntityVersionMismatch": cucsMgmtEntityVersionMismatch,
       "cucsMgmtEntitySshAuthKeysCsum": cucsMgmtEntitySshAuthKeysCsum,
       "cucsMgmtEntitySshAuthKeysSize": cucsMgmtEntitySshAuthKeysSize,
       "cucsMgmtEntitySshKeyStatus": cucsMgmtEntitySshKeyStatus,
       "cucsMgmtEntitySshRootPubKeyCsum": cucsMgmtEntitySshRootPubKeyCsum,
       "cucsMgmtEntitySshRootPubKeySize": cucsMgmtEntitySshRootPubKeySize,
       "cucsMgmtIfTable": cucsMgmtIfTable,
       "cucsMgmtIfEntry": cucsMgmtIfEntry,
       "cucsMgmtIfInstanceId": cucsMgmtIfInstanceId,
       "cucsMgmtIfDn": cucsMgmtIfDn,
       "cucsMgmtIfRn": cucsMgmtIfRn,
       "cucsMgmtIfAccess": cucsMgmtIfAccess,
       "cucsMgmtIfAdminState": cucsMgmtIfAdminState,
       "cucsMgmtIfChassisId": cucsMgmtIfChassisId,
       "cucsMgmtIfDiscovery": cucsMgmtIfDiscovery,
       "cucsMgmtIfEpDn": cucsMgmtIfEpDn,
       "cucsMgmtIfExtBroadcast": cucsMgmtIfExtBroadcast,
       "cucsMgmtIfExtGw": cucsMgmtIfExtGw,
       "cucsMgmtIfExtIp": cucsMgmtIfExtIp,
       "cucsMgmtIfExtMask": cucsMgmtIfExtMask,
       "cucsMgmtIfFsmDescr": cucsMgmtIfFsmDescr,
       "cucsMgmtIfFsmPrev": cucsMgmtIfFsmPrev,
       "cucsMgmtIfFsmProgr": cucsMgmtIfFsmProgr,
       "cucsMgmtIfFsmRmtInvErrCode": cucsMgmtIfFsmRmtInvErrCode,
       "cucsMgmtIfFsmRmtInvErrDescr": cucsMgmtIfFsmRmtInvErrDescr,
       "cucsMgmtIfFsmRmtInvRslt": cucsMgmtIfFsmRmtInvRslt,
       "cucsMgmtIfFsmStageDescr": cucsMgmtIfFsmStageDescr,
       "cucsMgmtIfFsmStamp": cucsMgmtIfFsmStamp,
       "cucsMgmtIfFsmStatus": cucsMgmtIfFsmStatus,
       "cucsMgmtIfFsmTry": cucsMgmtIfFsmTry,
       "cucsMgmtIfId": cucsMgmtIfId,
       "cucsMgmtIfIfRole": cucsMgmtIfIfRole,
       "cucsMgmtIfIfType": cucsMgmtIfIfType,
       "cucsMgmtIfIp": cucsMgmtIfIp,
       "cucsMgmtIfLocale": cucsMgmtIfLocale,
       "cucsMgmtIfMac": cucsMgmtIfMac,
       "cucsMgmtIfMask": cucsMgmtIfMask,
       "cucsMgmtIfName": cucsMgmtIfName,
       "cucsMgmtIfPeerDn": cucsMgmtIfPeerDn,
       "cucsMgmtIfPeerPortId": cucsMgmtIfPeerPortId,
       "cucsMgmtIfPeerSlotId": cucsMgmtIfPeerSlotId,
       "cucsMgmtIfPortId": cucsMgmtIfPortId,
       "cucsMgmtIfSlotId": cucsMgmtIfSlotId,
       "cucsMgmtIfStateQual": cucsMgmtIfStateQual,
       "cucsMgmtIfSubject": cucsMgmtIfSubject,
       "cucsMgmtIfSwitchId": cucsMgmtIfSwitchId,
       "cucsMgmtIfTransport": cucsMgmtIfTransport,
       "cucsMgmtIfType": cucsMgmtIfType,
       "cucsMgmtIfVnet": cucsMgmtIfVnet,
       "cucsMgmtIfPeerChassisId": cucsMgmtIfPeerChassisId,
       "cucsMgmtIfAggrPortId": cucsMgmtIfAggrPortId,
       "cucsMgmtIfPeerAggrPortId": cucsMgmtIfPeerAggrPortId,
       "cucsMgmtIfFsmTaskTable": cucsMgmtIfFsmTaskTable,
       "cucsMgmtIfFsmTaskEntry": cucsMgmtIfFsmTaskEntry,
       "cucsMgmtIfFsmTaskInstanceId": cucsMgmtIfFsmTaskInstanceId,
       "cucsMgmtIfFsmTaskDn": cucsMgmtIfFsmTaskDn,
       "cucsMgmtIfFsmTaskRn": cucsMgmtIfFsmTaskRn,
       "cucsMgmtIfFsmTaskCompletion": cucsMgmtIfFsmTaskCompletion,
       "cucsMgmtIfFsmTaskFlags": cucsMgmtIfFsmTaskFlags,
       "cucsMgmtIfFsmTaskItem": cucsMgmtIfFsmTaskItem,
       "cucsMgmtIfFsmTaskSeqId": cucsMgmtIfFsmTaskSeqId,
       "cucsMgmtImporterTable": cucsMgmtImporterTable,
       "cucsMgmtImporterEntry": cucsMgmtImporterEntry,
       "cucsMgmtImporterInstanceId": cucsMgmtImporterInstanceId,
       "cucsMgmtImporterDn": cucsMgmtImporterDn,
       "cucsMgmtImporterRn": cucsMgmtImporterRn,
       "cucsMgmtImporterAction": cucsMgmtImporterAction,
       "cucsMgmtImporterAdminState": cucsMgmtImporterAdminState,
       "cucsMgmtImporterDescr": cucsMgmtImporterDescr,
       "cucsMgmtImporterFsmDescr": cucsMgmtImporterFsmDescr,
       "cucsMgmtImporterFsmPrev": cucsMgmtImporterFsmPrev,
       "cucsMgmtImporterFsmProgr": cucsMgmtImporterFsmProgr,
       "cucsMgmtImporterFsmRmtInvErrCode": cucsMgmtImporterFsmRmtInvErrCode,
       "cucsMgmtImporterFsmRmtInvErrDescr": cucsMgmtImporterFsmRmtInvErrDescr,
       "cucsMgmtImporterFsmRmtInvRslt": cucsMgmtImporterFsmRmtInvRslt,
       "cucsMgmtImporterFsmStageDescr": cucsMgmtImporterFsmStageDescr,
       "cucsMgmtImporterFsmStamp": cucsMgmtImporterFsmStamp,
       "cucsMgmtImporterFsmStatus": cucsMgmtImporterFsmStatus,
       "cucsMgmtImporterFsmTry": cucsMgmtImporterFsmTry,
       "cucsMgmtImporterHostname": cucsMgmtImporterHostname,
       "cucsMgmtImporterIntId": cucsMgmtImporterIntId,
       "cucsMgmtImporterName": cucsMgmtImporterName,
       "cucsMgmtImporterPostAction": cucsMgmtImporterPostAction,
       "cucsMgmtImporterProto": cucsMgmtImporterProto,
       "cucsMgmtImporterPwd": cucsMgmtImporterPwd,
       "cucsMgmtImporterRemoteFile": cucsMgmtImporterRemoteFile,
       "cucsMgmtImporterUser": cucsMgmtImporterUser,
       "cucsMgmtImporterPolicyLevel": cucsMgmtImporterPolicyLevel,
       "cucsMgmtImporterPolicyOwner": cucsMgmtImporterPolicyOwner,
       "cucsMgmtImporterOperStatus": cucsMgmtImporterOperStatus,
       "cucsMgmtImporterFsmTaskTable": cucsMgmtImporterFsmTaskTable,
       "cucsMgmtImporterFsmTaskEntry": cucsMgmtImporterFsmTaskEntry,
       "cucsMgmtImporterFsmTaskInstanceId": cucsMgmtImporterFsmTaskInstanceId,
       "cucsMgmtImporterFsmTaskDn": cucsMgmtImporterFsmTaskDn,
       "cucsMgmtImporterFsmTaskRn": cucsMgmtImporterFsmTaskRn,
       "cucsMgmtImporterFsmTaskCompletion": cucsMgmtImporterFsmTaskCompletion,
       "cucsMgmtImporterFsmTaskFlags": cucsMgmtImporterFsmTaskFlags,
       "cucsMgmtImporterFsmTaskItem": cucsMgmtImporterFsmTaskItem,
       "cucsMgmtImporterFsmTaskSeqId": cucsMgmtImporterFsmTaskSeqId,
       "cucsMgmtIntAuthPolicyTable": cucsMgmtIntAuthPolicyTable,
       "cucsMgmtIntAuthPolicyEntry": cucsMgmtIntAuthPolicyEntry,
       "cucsMgmtIntAuthPolicyInstanceId": cucsMgmtIntAuthPolicyInstanceId,
       "cucsMgmtIntAuthPolicyDn": cucsMgmtIntAuthPolicyDn,
       "cucsMgmtIntAuthPolicyRn": cucsMgmtIntAuthPolicyRn,
       "cucsMgmtIntAuthPolicyMethod": cucsMgmtIntAuthPolicyMethod,
       "cucsMgmtIntAuthPolicyName": cucsMgmtIntAuthPolicyName,
       "cucsMgmtIntAuthPolicyPwd": cucsMgmtIntAuthPolicyPwd,
       "cucsMgmtPmonEntryTable": cucsMgmtPmonEntryTable,
       "cucsMgmtPmonEntryEntry": cucsMgmtPmonEntryEntry,
       "cucsMgmtPmonEntryInstanceId": cucsMgmtPmonEntryInstanceId,
       "cucsMgmtPmonEntryDn": cucsMgmtPmonEntryDn,
       "cucsMgmtPmonEntryRn": cucsMgmtPmonEntryRn,
       "cucsMgmtPmonEntryExitSignal": cucsMgmtPmonEntryExitSignal,
       "cucsMgmtPmonEntryFullPathname": cucsMgmtPmonEntryFullPathname,
       "cucsMgmtPmonEntryHeapSize": cucsMgmtPmonEntryHeapSize,
       "cucsMgmtPmonEntryHeapSize16Gb": cucsMgmtPmonEntryHeapSize16Gb,
       "cucsMgmtPmonEntryLastExitCode": cucsMgmtPmonEntryLastExitCode,
       "cucsMgmtPmonEntryMaxRetries": cucsMgmtPmonEntryMaxRetries,
       "cucsMgmtPmonEntryName": cucsMgmtPmonEntryName,
       "cucsMgmtPmonEntryRetries": cucsMgmtPmonEntryRetries,
       "cucsMgmtPmonEntrySpuriousRetries": cucsMgmtPmonEntrySpuriousRetries,
       "cucsMgmtPmonEntryState": cucsMgmtPmonEntryState,
       "cucsMgmtPmonEntrySwitchId": cucsMgmtPmonEntrySwitchId,
       "cucsMgmtPmonEntryWorkingDirectory": cucsMgmtPmonEntryWorkingDirectory,
       "cucsMgmtBackupFsmTable": cucsMgmtBackupFsmTable,
       "cucsMgmtBackupFsmEntry": cucsMgmtBackupFsmEntry,
       "cucsMgmtBackupFsmInstanceId": cucsMgmtBackupFsmInstanceId,
       "cucsMgmtBackupFsmDn": cucsMgmtBackupFsmDn,
       "cucsMgmtBackupFsmRn": cucsMgmtBackupFsmRn,
       "cucsMgmtBackupFsmCompletionTime": cucsMgmtBackupFsmCompletionTime,
       "cucsMgmtBackupFsmCurrentFsm": cucsMgmtBackupFsmCurrentFsm,
       "cucsMgmtBackupFsmDescrData": cucsMgmtBackupFsmDescrData,
       "cucsMgmtBackupFsmFsmStatus": cucsMgmtBackupFsmFsmStatus,
       "cucsMgmtBackupFsmProgress": cucsMgmtBackupFsmProgress,
       "cucsMgmtBackupFsmRmtErrCode": cucsMgmtBackupFsmRmtErrCode,
       "cucsMgmtBackupFsmRmtErrDescr": cucsMgmtBackupFsmRmtErrDescr,
       "cucsMgmtBackupFsmRmtRslt": cucsMgmtBackupFsmRmtRslt,
       "cucsMgmtBackupFsmStageTable": cucsMgmtBackupFsmStageTable,
       "cucsMgmtBackupFsmStageEntry": cucsMgmtBackupFsmStageEntry,
       "cucsMgmtBackupFsmStageInstanceId": cucsMgmtBackupFsmStageInstanceId,
       "cucsMgmtBackupFsmStageDn": cucsMgmtBackupFsmStageDn,
       "cucsMgmtBackupFsmStageRn": cucsMgmtBackupFsmStageRn,
       "cucsMgmtBackupFsmStageDescrData": cucsMgmtBackupFsmStageDescrData,
       "cucsMgmtBackupFsmStageLastUpdateTime": cucsMgmtBackupFsmStageLastUpdateTime,
       "cucsMgmtBackupFsmStageName": cucsMgmtBackupFsmStageName,
       "cucsMgmtBackupFsmStageOrder": cucsMgmtBackupFsmStageOrder,
       "cucsMgmtBackupFsmStageRetry": cucsMgmtBackupFsmStageRetry,
       "cucsMgmtBackupFsmStageStageStatus": cucsMgmtBackupFsmStageStageStatus,
       "cucsMgmtBackupPolicyTable": cucsMgmtBackupPolicyTable,
       "cucsMgmtBackupPolicyEntry": cucsMgmtBackupPolicyEntry,
       "cucsMgmtBackupPolicyInstanceId": cucsMgmtBackupPolicyInstanceId,
       "cucsMgmtBackupPolicyDn": cucsMgmtBackupPolicyDn,
       "cucsMgmtBackupPolicyRn": cucsMgmtBackupPolicyRn,
       "cucsMgmtBackupPolicyAdminState": cucsMgmtBackupPolicyAdminState,
       "cucsMgmtBackupPolicyDescr": cucsMgmtBackupPolicyDescr,
       "cucsMgmtBackupPolicyFsmDescr": cucsMgmtBackupPolicyFsmDescr,
       "cucsMgmtBackupPolicyFsmPrev": cucsMgmtBackupPolicyFsmPrev,
       "cucsMgmtBackupPolicyFsmProgr": cucsMgmtBackupPolicyFsmProgr,
       "cucsMgmtBackupPolicyFsmRmtInvErrCode": cucsMgmtBackupPolicyFsmRmtInvErrCode,
       "cucsMgmtBackupPolicyFsmRmtInvErrDescr": cucsMgmtBackupPolicyFsmRmtInvErrDescr,
       "cucsMgmtBackupPolicyFsmRmtInvRslt": cucsMgmtBackupPolicyFsmRmtInvRslt,
       "cucsMgmtBackupPolicyFsmStageDescr": cucsMgmtBackupPolicyFsmStageDescr,
       "cucsMgmtBackupPolicyFsmStamp": cucsMgmtBackupPolicyFsmStamp,
       "cucsMgmtBackupPolicyFsmStatus": cucsMgmtBackupPolicyFsmStatus,
       "cucsMgmtBackupPolicyFsmTry": cucsMgmtBackupPolicyFsmTry,
       "cucsMgmtBackupPolicyHost": cucsMgmtBackupPolicyHost,
       "cucsMgmtBackupPolicyIntId": cucsMgmtBackupPolicyIntId,
       "cucsMgmtBackupPolicyLastBackup": cucsMgmtBackupPolicyLastBackup,
       "cucsMgmtBackupPolicyMaxFiles": cucsMgmtBackupPolicyMaxFiles,
       "cucsMgmtBackupPolicyName": cucsMgmtBackupPolicyName,
       "cucsMgmtBackupPolicyPolicyLevel": cucsMgmtBackupPolicyPolicyLevel,
       "cucsMgmtBackupPolicyPolicyOwner": cucsMgmtBackupPolicyPolicyOwner,
       "cucsMgmtBackupPolicyProto": cucsMgmtBackupPolicyProto,
       "cucsMgmtBackupPolicyPwd": cucsMgmtBackupPolicyPwd,
       "cucsMgmtBackupPolicyRemoteFile": cucsMgmtBackupPolicyRemoteFile,
       "cucsMgmtBackupPolicySchedule": cucsMgmtBackupPolicySchedule,
       "cucsMgmtBackupPolicyUser": cucsMgmtBackupPolicyUser,
       "cucsMgmtBackupPolicyFsmTable": cucsMgmtBackupPolicyFsmTable,
       "cucsMgmtBackupPolicyFsmEntry": cucsMgmtBackupPolicyFsmEntry,
       "cucsMgmtBackupPolicyFsmInstanceId": cucsMgmtBackupPolicyFsmInstanceId,
       "cucsMgmtBackupPolicyFsmDn": cucsMgmtBackupPolicyFsmDn,
       "cucsMgmtBackupPolicyFsmRn": cucsMgmtBackupPolicyFsmRn,
       "cucsMgmtBackupPolicyFsmCompletionTime": cucsMgmtBackupPolicyFsmCompletionTime,
       "cucsMgmtBackupPolicyFsmCurrentFsm": cucsMgmtBackupPolicyFsmCurrentFsm,
       "cucsMgmtBackupPolicyFsmDescrData": cucsMgmtBackupPolicyFsmDescrData,
       "cucsMgmtBackupPolicyFsmFsmStatus": cucsMgmtBackupPolicyFsmFsmStatus,
       "cucsMgmtBackupPolicyFsmProgress": cucsMgmtBackupPolicyFsmProgress,
       "cucsMgmtBackupPolicyFsmRmtErrCode": cucsMgmtBackupPolicyFsmRmtErrCode,
       "cucsMgmtBackupPolicyFsmRmtErrDescr": cucsMgmtBackupPolicyFsmRmtErrDescr,
       "cucsMgmtBackupPolicyFsmRmtRslt": cucsMgmtBackupPolicyFsmRmtRslt,
       "cucsMgmtBackupPolicyFsmStageTable": cucsMgmtBackupPolicyFsmStageTable,
       "cucsMgmtBackupPolicyFsmStageEntry": cucsMgmtBackupPolicyFsmStageEntry,
       "cucsMgmtBackupPolicyFsmStageInstanceId": cucsMgmtBackupPolicyFsmStageInstanceId,
       "cucsMgmtBackupPolicyFsmStageDn": cucsMgmtBackupPolicyFsmStageDn,
       "cucsMgmtBackupPolicyFsmStageRn": cucsMgmtBackupPolicyFsmStageRn,
       "cucsMgmtBackupPolicyFsmStageDescrData": cucsMgmtBackupPolicyFsmStageDescrData,
       "cucsMgmtBackupPolicyFsmStageLastUpdateTime": cucsMgmtBackupPolicyFsmStageLastUpdateTime,
       "cucsMgmtBackupPolicyFsmStageName": cucsMgmtBackupPolicyFsmStageName,
       "cucsMgmtBackupPolicyFsmStageOrder": cucsMgmtBackupPolicyFsmStageOrder,
       "cucsMgmtBackupPolicyFsmStageRetry": cucsMgmtBackupPolicyFsmStageRetry,
       "cucsMgmtBackupPolicyFsmStageStageStatus": cucsMgmtBackupPolicyFsmStageStageStatus,
       "cucsMgmtCfgExportPolicyTable": cucsMgmtCfgExportPolicyTable,
       "cucsMgmtCfgExportPolicyEntry": cucsMgmtCfgExportPolicyEntry,
       "cucsMgmtCfgExportPolicyInstanceId": cucsMgmtCfgExportPolicyInstanceId,
       "cucsMgmtCfgExportPolicyDn": cucsMgmtCfgExportPolicyDn,
       "cucsMgmtCfgExportPolicyRn": cucsMgmtCfgExportPolicyRn,
       "cucsMgmtCfgExportPolicyAdminState": cucsMgmtCfgExportPolicyAdminState,
       "cucsMgmtCfgExportPolicyDescr": cucsMgmtCfgExportPolicyDescr,
       "cucsMgmtCfgExportPolicyFsmDescr": cucsMgmtCfgExportPolicyFsmDescr,
       "cucsMgmtCfgExportPolicyFsmPrev": cucsMgmtCfgExportPolicyFsmPrev,
       "cucsMgmtCfgExportPolicyFsmProgr": cucsMgmtCfgExportPolicyFsmProgr,
       "cucsMgmtCfgExportPolicyFsmRmtInvErrCode": cucsMgmtCfgExportPolicyFsmRmtInvErrCode,
       "cucsMgmtCfgExportPolicyFsmRmtInvErrDescr": cucsMgmtCfgExportPolicyFsmRmtInvErrDescr,
       "cucsMgmtCfgExportPolicyFsmRmtInvRslt": cucsMgmtCfgExportPolicyFsmRmtInvRslt,
       "cucsMgmtCfgExportPolicyFsmStageDescr": cucsMgmtCfgExportPolicyFsmStageDescr,
       "cucsMgmtCfgExportPolicyFsmStamp": cucsMgmtCfgExportPolicyFsmStamp,
       "cucsMgmtCfgExportPolicyFsmStatus": cucsMgmtCfgExportPolicyFsmStatus,
       "cucsMgmtCfgExportPolicyFsmTry": cucsMgmtCfgExportPolicyFsmTry,
       "cucsMgmtCfgExportPolicyHost": cucsMgmtCfgExportPolicyHost,
       "cucsMgmtCfgExportPolicyIntId": cucsMgmtCfgExportPolicyIntId,
       "cucsMgmtCfgExportPolicyLastBackup": cucsMgmtCfgExportPolicyLastBackup,
       "cucsMgmtCfgExportPolicyMaxFiles": cucsMgmtCfgExportPolicyMaxFiles,
       "cucsMgmtCfgExportPolicyName": cucsMgmtCfgExportPolicyName,
       "cucsMgmtCfgExportPolicyPolicyLevel": cucsMgmtCfgExportPolicyPolicyLevel,
       "cucsMgmtCfgExportPolicyPolicyOwner": cucsMgmtCfgExportPolicyPolicyOwner,
       "cucsMgmtCfgExportPolicyProto": cucsMgmtCfgExportPolicyProto,
       "cucsMgmtCfgExportPolicyPwd": cucsMgmtCfgExportPolicyPwd,
       "cucsMgmtCfgExportPolicyRemoteFile": cucsMgmtCfgExportPolicyRemoteFile,
       "cucsMgmtCfgExportPolicySchedule": cucsMgmtCfgExportPolicySchedule,
       "cucsMgmtCfgExportPolicyUser": cucsMgmtCfgExportPolicyUser,
       "cucsMgmtCfgExportPolicyFsmTable": cucsMgmtCfgExportPolicyFsmTable,
       "cucsMgmtCfgExportPolicyFsmEntry": cucsMgmtCfgExportPolicyFsmEntry,
       "cucsMgmtCfgExportPolicyFsmInstanceId": cucsMgmtCfgExportPolicyFsmInstanceId,
       "cucsMgmtCfgExportPolicyFsmDn": cucsMgmtCfgExportPolicyFsmDn,
       "cucsMgmtCfgExportPolicyFsmRn": cucsMgmtCfgExportPolicyFsmRn,
       "cucsMgmtCfgExportPolicyFsmCompletionTime": cucsMgmtCfgExportPolicyFsmCompletionTime,
       "cucsMgmtCfgExportPolicyFsmCurrentFsm": cucsMgmtCfgExportPolicyFsmCurrentFsm,
       "cucsMgmtCfgExportPolicyFsmDescrData": cucsMgmtCfgExportPolicyFsmDescrData,
       "cucsMgmtCfgExportPolicyFsmFsmStatus": cucsMgmtCfgExportPolicyFsmFsmStatus,
       "cucsMgmtCfgExportPolicyFsmProgress": cucsMgmtCfgExportPolicyFsmProgress,
       "cucsMgmtCfgExportPolicyFsmRmtErrCode": cucsMgmtCfgExportPolicyFsmRmtErrCode,
       "cucsMgmtCfgExportPolicyFsmRmtErrDescr": cucsMgmtCfgExportPolicyFsmRmtErrDescr,
       "cucsMgmtCfgExportPolicyFsmRmtRslt": cucsMgmtCfgExportPolicyFsmRmtRslt,
       "cucsMgmtCfgExportPolicyFsmStageTable": cucsMgmtCfgExportPolicyFsmStageTable,
       "cucsMgmtCfgExportPolicyFsmStageEntry": cucsMgmtCfgExportPolicyFsmStageEntry,
       "cucsMgmtCfgExportPolicyFsmStageInstanceId": cucsMgmtCfgExportPolicyFsmStageInstanceId,
       "cucsMgmtCfgExportPolicyFsmStageDn": cucsMgmtCfgExportPolicyFsmStageDn,
       "cucsMgmtCfgExportPolicyFsmStageRn": cucsMgmtCfgExportPolicyFsmStageRn,
       "cucsMgmtCfgExportPolicyFsmStageDescrData": cucsMgmtCfgExportPolicyFsmStageDescrData,
       "cucsMgmtCfgExportPolicyFsmStageLastUpdateTime": cucsMgmtCfgExportPolicyFsmStageLastUpdateTime,
       "cucsMgmtCfgExportPolicyFsmStageName": cucsMgmtCfgExportPolicyFsmStageName,
       "cucsMgmtCfgExportPolicyFsmStageOrder": cucsMgmtCfgExportPolicyFsmStageOrder,
       "cucsMgmtCfgExportPolicyFsmStageRetry": cucsMgmtCfgExportPolicyFsmStageRetry,
       "cucsMgmtCfgExportPolicyFsmStageStageStatus": cucsMgmtCfgExportPolicyFsmStageStageStatus,
       "cucsMgmtConnectionTable": cucsMgmtConnectionTable,
       "cucsMgmtConnectionEntry": cucsMgmtConnectionEntry,
       "cucsMgmtConnectionInstanceId": cucsMgmtConnectionInstanceId,
       "cucsMgmtConnectionDn": cucsMgmtConnectionDn,
       "cucsMgmtConnectionRn": cucsMgmtConnectionRn,
       "cucsMgmtConnectionAck": cucsMgmtConnectionAck,
       "cucsMgmtConnectionOperState": cucsMgmtConnectionOperState,
       "cucsMgmtConnectionType": cucsMgmtConnectionType,
       "cucsMgmtControllerFsmTable": cucsMgmtControllerFsmTable,
       "cucsMgmtControllerFsmEntry": cucsMgmtControllerFsmEntry,
       "cucsMgmtControllerFsmInstanceId": cucsMgmtControllerFsmInstanceId,
       "cucsMgmtControllerFsmDn": cucsMgmtControllerFsmDn,
       "cucsMgmtControllerFsmRn": cucsMgmtControllerFsmRn,
       "cucsMgmtControllerFsmCompletionTime": cucsMgmtControllerFsmCompletionTime,
       "cucsMgmtControllerFsmCurrentFsm": cucsMgmtControllerFsmCurrentFsm,
       "cucsMgmtControllerFsmDescrData": cucsMgmtControllerFsmDescrData,
       "cucsMgmtControllerFsmFsmStatus": cucsMgmtControllerFsmFsmStatus,
       "cucsMgmtControllerFsmProgress": cucsMgmtControllerFsmProgress,
       "cucsMgmtControllerFsmRmtErrCode": cucsMgmtControllerFsmRmtErrCode,
       "cucsMgmtControllerFsmRmtErrDescr": cucsMgmtControllerFsmRmtErrDescr,
       "cucsMgmtControllerFsmRmtRslt": cucsMgmtControllerFsmRmtRslt,
       "cucsMgmtControllerFsmStageTable": cucsMgmtControllerFsmStageTable,
       "cucsMgmtControllerFsmStageEntry": cucsMgmtControllerFsmStageEntry,
       "cucsMgmtControllerFsmStageInstanceId": cucsMgmtControllerFsmStageInstanceId,
       "cucsMgmtControllerFsmStageDn": cucsMgmtControllerFsmStageDn,
       "cucsMgmtControllerFsmStageRn": cucsMgmtControllerFsmStageRn,
       "cucsMgmtControllerFsmStageDescrData": cucsMgmtControllerFsmStageDescrData,
       "cucsMgmtControllerFsmStageLastUpdateTime": cucsMgmtControllerFsmStageLastUpdateTime,
       "cucsMgmtControllerFsmStageName": cucsMgmtControllerFsmStageName,
       "cucsMgmtControllerFsmStageOrder": cucsMgmtControllerFsmStageOrder,
       "cucsMgmtControllerFsmStageRetry": cucsMgmtControllerFsmStageRetry,
       "cucsMgmtControllerFsmStageStageStatus": cucsMgmtControllerFsmStageStageStatus,
       "cucsMgmtExportPolicyFsmTable": cucsMgmtExportPolicyFsmTable,
       "cucsMgmtExportPolicyFsmEntry": cucsMgmtExportPolicyFsmEntry,
       "cucsMgmtExportPolicyFsmInstanceId": cucsMgmtExportPolicyFsmInstanceId,
       "cucsMgmtExportPolicyFsmDn": cucsMgmtExportPolicyFsmDn,
       "cucsMgmtExportPolicyFsmRn": cucsMgmtExportPolicyFsmRn,
       "cucsMgmtExportPolicyFsmCompletionTime": cucsMgmtExportPolicyFsmCompletionTime,
       "cucsMgmtExportPolicyFsmCurrentFsm": cucsMgmtExportPolicyFsmCurrentFsm,
       "cucsMgmtExportPolicyFsmDescr": cucsMgmtExportPolicyFsmDescr,
       "cucsMgmtExportPolicyFsmFsmStatus": cucsMgmtExportPolicyFsmFsmStatus,
       "cucsMgmtExportPolicyFsmProgress": cucsMgmtExportPolicyFsmProgress,
       "cucsMgmtExportPolicyFsmRmtErrCode": cucsMgmtExportPolicyFsmRmtErrCode,
       "cucsMgmtExportPolicyFsmRmtErrDescr": cucsMgmtExportPolicyFsmRmtErrDescr,
       "cucsMgmtExportPolicyFsmRmtRslt": cucsMgmtExportPolicyFsmRmtRslt,
       "cucsMgmtExportPolicyFsmStageTable": cucsMgmtExportPolicyFsmStageTable,
       "cucsMgmtExportPolicyFsmStageEntry": cucsMgmtExportPolicyFsmStageEntry,
       "cucsMgmtExportPolicyFsmStageInstanceId": cucsMgmtExportPolicyFsmStageInstanceId,
       "cucsMgmtExportPolicyFsmStageDn": cucsMgmtExportPolicyFsmStageDn,
       "cucsMgmtExportPolicyFsmStageRn": cucsMgmtExportPolicyFsmStageRn,
       "cucsMgmtExportPolicyFsmStageDescr": cucsMgmtExportPolicyFsmStageDescr,
       "cucsMgmtExportPolicyFsmStageLastUpdateTime": cucsMgmtExportPolicyFsmStageLastUpdateTime,
       "cucsMgmtExportPolicyFsmStageName": cucsMgmtExportPolicyFsmStageName,
       "cucsMgmtExportPolicyFsmStageOrder": cucsMgmtExportPolicyFsmStageOrder,
       "cucsMgmtExportPolicyFsmStageRetry": cucsMgmtExportPolicyFsmStageRetry,
       "cucsMgmtExportPolicyFsmStageStageStatus": cucsMgmtExportPolicyFsmStageStageStatus,
       "cucsMgmtExportPolicyFsmTaskTable": cucsMgmtExportPolicyFsmTaskTable,
       "cucsMgmtExportPolicyFsmTaskEntry": cucsMgmtExportPolicyFsmTaskEntry,
       "cucsMgmtExportPolicyFsmTaskInstanceId": cucsMgmtExportPolicyFsmTaskInstanceId,
       "cucsMgmtExportPolicyFsmTaskDn": cucsMgmtExportPolicyFsmTaskDn,
       "cucsMgmtExportPolicyFsmTaskRn": cucsMgmtExportPolicyFsmTaskRn,
       "cucsMgmtExportPolicyFsmTaskCompletion": cucsMgmtExportPolicyFsmTaskCompletion,
       "cucsMgmtExportPolicyFsmTaskFlags": cucsMgmtExportPolicyFsmTaskFlags,
       "cucsMgmtExportPolicyFsmTaskItem": cucsMgmtExportPolicyFsmTaskItem,
       "cucsMgmtExportPolicyFsmTaskSeqId": cucsMgmtExportPolicyFsmTaskSeqId,
       "cucsMgmtIfFsmTable": cucsMgmtIfFsmTable,
       "cucsMgmtIfFsmEntry": cucsMgmtIfFsmEntry,
       "cucsMgmtIfFsmInstanceId": cucsMgmtIfFsmInstanceId,
       "cucsMgmtIfFsmDn": cucsMgmtIfFsmDn,
       "cucsMgmtIfFsmRn": cucsMgmtIfFsmRn,
       "cucsMgmtIfFsmCompletionTime": cucsMgmtIfFsmCompletionTime,
       "cucsMgmtIfFsmCurrentFsm": cucsMgmtIfFsmCurrentFsm,
       "cucsMgmtIfFsmDescrData": cucsMgmtIfFsmDescrData,
       "cucsMgmtIfFsmFsmStatus": cucsMgmtIfFsmFsmStatus,
       "cucsMgmtIfFsmProgress": cucsMgmtIfFsmProgress,
       "cucsMgmtIfFsmRmtErrCode": cucsMgmtIfFsmRmtErrCode,
       "cucsMgmtIfFsmRmtErrDescr": cucsMgmtIfFsmRmtErrDescr,
       "cucsMgmtIfFsmRmtRslt": cucsMgmtIfFsmRmtRslt,
       "cucsMgmtIfFsmStageTable": cucsMgmtIfFsmStageTable,
       "cucsMgmtIfFsmStageEntry": cucsMgmtIfFsmStageEntry,
       "cucsMgmtIfFsmStageInstanceId": cucsMgmtIfFsmStageInstanceId,
       "cucsMgmtIfFsmStageDn": cucsMgmtIfFsmStageDn,
       "cucsMgmtIfFsmStageRn": cucsMgmtIfFsmStageRn,
       "cucsMgmtIfFsmStageDescrData": cucsMgmtIfFsmStageDescrData,
       "cucsMgmtIfFsmStageLastUpdateTime": cucsMgmtIfFsmStageLastUpdateTime,
       "cucsMgmtIfFsmStageName": cucsMgmtIfFsmStageName,
       "cucsMgmtIfFsmStageOrder": cucsMgmtIfFsmStageOrder,
       "cucsMgmtIfFsmStageRetry": cucsMgmtIfFsmStageRetry,
       "cucsMgmtIfFsmStageStageStatus": cucsMgmtIfFsmStageStageStatus,
       "cucsMgmtImporterFsmTable": cucsMgmtImporterFsmTable,
       "cucsMgmtImporterFsmEntry": cucsMgmtImporterFsmEntry,
       "cucsMgmtImporterFsmInstanceId": cucsMgmtImporterFsmInstanceId,
       "cucsMgmtImporterFsmDn": cucsMgmtImporterFsmDn,
       "cucsMgmtImporterFsmRn": cucsMgmtImporterFsmRn,
       "cucsMgmtImporterFsmCompletionTime": cucsMgmtImporterFsmCompletionTime,
       "cucsMgmtImporterFsmCurrentFsm": cucsMgmtImporterFsmCurrentFsm,
       "cucsMgmtImporterFsmDescrData": cucsMgmtImporterFsmDescrData,
       "cucsMgmtImporterFsmFsmStatus": cucsMgmtImporterFsmFsmStatus,
       "cucsMgmtImporterFsmProgress": cucsMgmtImporterFsmProgress,
       "cucsMgmtImporterFsmRmtErrCode": cucsMgmtImporterFsmRmtErrCode,
       "cucsMgmtImporterFsmRmtErrDescr": cucsMgmtImporterFsmRmtErrDescr,
       "cucsMgmtImporterFsmRmtRslt": cucsMgmtImporterFsmRmtRslt,
       "cucsMgmtImporterFsmStageTable": cucsMgmtImporterFsmStageTable,
       "cucsMgmtImporterFsmStageEntry": cucsMgmtImporterFsmStageEntry,
       "cucsMgmtImporterFsmStageInstanceId": cucsMgmtImporterFsmStageInstanceId,
       "cucsMgmtImporterFsmStageDn": cucsMgmtImporterFsmStageDn,
       "cucsMgmtImporterFsmStageRn": cucsMgmtImporterFsmStageRn,
       "cucsMgmtImporterFsmStageDescrData": cucsMgmtImporterFsmStageDescrData,
       "cucsMgmtImporterFsmStageLastUpdateTime": cucsMgmtImporterFsmStageLastUpdateTime,
       "cucsMgmtImporterFsmStageName": cucsMgmtImporterFsmStageName,
       "cucsMgmtImporterFsmStageOrder": cucsMgmtImporterFsmStageOrder,
       "cucsMgmtImporterFsmStageRetry": cucsMgmtImporterFsmStageRetry,
       "cucsMgmtImporterFsmStageStageStatus": cucsMgmtImporterFsmStageStageStatus,
       "cucsMgmtIPv6IfAddrTable": cucsMgmtIPv6IfAddrTable,
       "cucsMgmtIPv6IfAddrEntry": cucsMgmtIPv6IfAddrEntry,
       "cucsMgmtIPv6IfAddrInstanceId": cucsMgmtIPv6IfAddrInstanceId,
       "cucsMgmtIPv6IfAddrDn": cucsMgmtIPv6IfAddrDn,
       "cucsMgmtIPv6IfAddrRn": cucsMgmtIPv6IfAddrRn,
       "cucsMgmtIPv6IfAddrAddr": cucsMgmtIPv6IfAddrAddr,
       "cucsMgmtIPv6IfAddrDefGw": cucsMgmtIPv6IfAddrDefGw,
       "cucsMgmtIPv6IfAddrFsmDescr": cucsMgmtIPv6IfAddrFsmDescr,
       "cucsMgmtIPv6IfAddrFsmPrev": cucsMgmtIPv6IfAddrFsmPrev,
       "cucsMgmtIPv6IfAddrFsmProgr": cucsMgmtIPv6IfAddrFsmProgr,
       "cucsMgmtIPv6IfAddrFsmRmtInvErrCode": cucsMgmtIPv6IfAddrFsmRmtInvErrCode,
       "cucsMgmtIPv6IfAddrFsmRmtInvErrDescr": cucsMgmtIPv6IfAddrFsmRmtInvErrDescr,
       "cucsMgmtIPv6IfAddrFsmRmtInvRslt": cucsMgmtIPv6IfAddrFsmRmtInvRslt,
       "cucsMgmtIPv6IfAddrFsmStageDescr": cucsMgmtIPv6IfAddrFsmStageDescr,
       "cucsMgmtIPv6IfAddrFsmStamp": cucsMgmtIPv6IfAddrFsmStamp,
       "cucsMgmtIPv6IfAddrFsmStatus": cucsMgmtIPv6IfAddrFsmStatus,
       "cucsMgmtIPv6IfAddrFsmTry": cucsMgmtIPv6IfAddrFsmTry,
       "cucsMgmtIPv6IfAddrPrefix": cucsMgmtIPv6IfAddrPrefix,
       "cucsMgmtIPv6IfAddrFsmTable": cucsMgmtIPv6IfAddrFsmTable,
       "cucsMgmtIPv6IfAddrFsmEntry": cucsMgmtIPv6IfAddrFsmEntry,
       "cucsMgmtIPv6IfAddrFsmInstanceId": cucsMgmtIPv6IfAddrFsmInstanceId,
       "cucsMgmtIPv6IfAddrFsmDn": cucsMgmtIPv6IfAddrFsmDn,
       "cucsMgmtIPv6IfAddrFsmRn": cucsMgmtIPv6IfAddrFsmRn,
       "cucsMgmtIPv6IfAddrFsmCompletionTime": cucsMgmtIPv6IfAddrFsmCompletionTime,
       "cucsMgmtIPv6IfAddrFsmCurrentFsm": cucsMgmtIPv6IfAddrFsmCurrentFsm,
       "cucsMgmtIPv6IfAddrFsmDescrData": cucsMgmtIPv6IfAddrFsmDescrData,
       "cucsMgmtIPv6IfAddrFsmFsmStatus": cucsMgmtIPv6IfAddrFsmFsmStatus,
       "cucsMgmtIPv6IfAddrFsmProgress": cucsMgmtIPv6IfAddrFsmProgress,
       "cucsMgmtIPv6IfAddrFsmRmtErrCode": cucsMgmtIPv6IfAddrFsmRmtErrCode,
       "cucsMgmtIPv6IfAddrFsmRmtErrDescr": cucsMgmtIPv6IfAddrFsmRmtErrDescr,
       "cucsMgmtIPv6IfAddrFsmRmtRslt": cucsMgmtIPv6IfAddrFsmRmtRslt,
       "cucsMgmtIPv6IfAddrFsmStageTable": cucsMgmtIPv6IfAddrFsmStageTable,
       "cucsMgmtIPv6IfAddrFsmStageEntry": cucsMgmtIPv6IfAddrFsmStageEntry,
       "cucsMgmtIPv6IfAddrFsmStageInstanceId": cucsMgmtIPv6IfAddrFsmStageInstanceId,
       "cucsMgmtIPv6IfAddrFsmStageDn": cucsMgmtIPv6IfAddrFsmStageDn,
       "cucsMgmtIPv6IfAddrFsmStageRn": cucsMgmtIPv6IfAddrFsmStageRn,
       "cucsMgmtIPv6IfAddrFsmStageDescrData": cucsMgmtIPv6IfAddrFsmStageDescrData,
       "cucsMgmtIPv6IfAddrFsmStageLastUpdateTime": cucsMgmtIPv6IfAddrFsmStageLastUpdateTime,
       "cucsMgmtIPv6IfAddrFsmStageName": cucsMgmtIPv6IfAddrFsmStageName,
       "cucsMgmtIPv6IfAddrFsmStageOrder": cucsMgmtIPv6IfAddrFsmStageOrder,
       "cucsMgmtIPv6IfAddrFsmStageRetry": cucsMgmtIPv6IfAddrFsmStageRetry,
       "cucsMgmtIPv6IfAddrFsmStageStageStatus": cucsMgmtIPv6IfAddrFsmStageStageStatus,
       "cucsMgmtIPv6IfAddrFsmTaskTable": cucsMgmtIPv6IfAddrFsmTaskTable,
       "cucsMgmtIPv6IfAddrFsmTaskEntry": cucsMgmtIPv6IfAddrFsmTaskEntry,
       "cucsMgmtIPv6IfAddrFsmTaskInstanceId": cucsMgmtIPv6IfAddrFsmTaskInstanceId,
       "cucsMgmtIPv6IfAddrFsmTaskDn": cucsMgmtIPv6IfAddrFsmTaskDn,
       "cucsMgmtIPv6IfAddrFsmTaskRn": cucsMgmtIPv6IfAddrFsmTaskRn,
       "cucsMgmtIPv6IfAddrFsmTaskCompletion": cucsMgmtIPv6IfAddrFsmTaskCompletion,
       "cucsMgmtIPv6IfAddrFsmTaskFlags": cucsMgmtIPv6IfAddrFsmTaskFlags,
       "cucsMgmtIPv6IfAddrFsmTaskItem": cucsMgmtIPv6IfAddrFsmTaskItem,
       "cucsMgmtIPv6IfAddrFsmTaskSeqId": cucsMgmtIPv6IfAddrFsmTaskSeqId,
       "cucsMgmtIPv6IfConfigTable": cucsMgmtIPv6IfConfigTable,
       "cucsMgmtIPv6IfConfigEntry": cucsMgmtIPv6IfConfigEntry,
       "cucsMgmtIPv6IfConfigInstanceId": cucsMgmtIPv6IfConfigInstanceId,
       "cucsMgmtIPv6IfConfigDn": cucsMgmtIPv6IfConfigDn,
       "cucsMgmtIPv6IfConfigRn": cucsMgmtIPv6IfConfigRn,
       "cucsMgmtInbandProfileTable": cucsMgmtInbandProfileTable,
       "cucsMgmtInbandProfileEntry": cucsMgmtInbandProfileEntry,
       "cucsMgmtInbandProfileInstanceId": cucsMgmtInbandProfileInstanceId,
       "cucsMgmtInbandProfileDn": cucsMgmtInbandProfileDn,
       "cucsMgmtInbandProfileRn": cucsMgmtInbandProfileRn,
       "cucsMgmtInbandProfileDefaultVlanName": cucsMgmtInbandProfileDefaultVlanName,
       "cucsMgmtInbandProfileName": cucsMgmtInbandProfileName,
       "cucsMgmtInbandProfilePoolName": cucsMgmtInbandProfilePoolName,
       "cucsMgmtInterfaceTable": cucsMgmtInterfaceTable,
       "cucsMgmtInterfaceEntry": cucsMgmtInterfaceEntry,
       "cucsMgmtInterfaceInstanceId": cucsMgmtInterfaceInstanceId,
       "cucsMgmtInterfaceDn": cucsMgmtInterfaceDn,
       "cucsMgmtInterfaceRn": cucsMgmtInterfaceRn,
       "cucsMgmtInterfaceConfigMessage": cucsMgmtInterfaceConfigMessage,
       "cucsMgmtInterfaceConfigState": cucsMgmtInterfaceConfigState,
       "cucsMgmtInterfaceIpV4State": cucsMgmtInterfaceIpV4State,
       "cucsMgmtInterfaceIpV6State": cucsMgmtInterfaceIpV6State,
       "cucsMgmtInterfaceMode": cucsMgmtInterfaceMode,
       "cucsMgmtInterfaceOperState": cucsMgmtInterfaceOperState,
       "cucsMgmtInterfaceIsDefaultDerived": cucsMgmtInterfaceIsDefaultDerived,
       "cucsMgmtProfDerivedInterfaceTable": cucsMgmtProfDerivedInterfaceTable,
       "cucsMgmtProfDerivedInterfaceEntry": cucsMgmtProfDerivedInterfaceEntry,
       "cucsMgmtProfDerivedInterfaceInstanceId": cucsMgmtProfDerivedInterfaceInstanceId,
       "cucsMgmtProfDerivedInterfaceDn": cucsMgmtProfDerivedInterfaceDn,
       "cucsMgmtProfDerivedInterfaceRn": cucsMgmtProfDerivedInterfaceRn,
       "cucsMgmtProfDerivedInterfaceConfigMessage": cucsMgmtProfDerivedInterfaceConfigMessage,
       "cucsMgmtProfDerivedInterfaceConfigState": cucsMgmtProfDerivedInterfaceConfigState,
       "cucsMgmtProfDerivedInterfaceIpV4State": cucsMgmtProfDerivedInterfaceIpV4State,
       "cucsMgmtProfDerivedInterfaceIpV6State": cucsMgmtProfDerivedInterfaceIpV6State,
       "cucsMgmtProfDerivedInterfaceMode": cucsMgmtProfDerivedInterfaceMode,
       "cucsMgmtProfDerivedInterfaceOperState": cucsMgmtProfDerivedInterfaceOperState,
       "cucsMgmtVnetTable": cucsMgmtVnetTable,
       "cucsMgmtVnetEntry": cucsMgmtVnetEntry,
       "cucsMgmtVnetInstanceId": cucsMgmtVnetInstanceId,
       "cucsMgmtVnetDn": cucsMgmtVnetDn,
       "cucsMgmtVnetRn": cucsMgmtVnetRn,
       "cucsMgmtVnetConfigState": cucsMgmtVnetConfigState,
       "cucsMgmtVnetId": cucsMgmtVnetId,
       "cucsMgmtVnetName": cucsMgmtVnetName,
       "cucsMgmtBackupExportExtPolicyTable": cucsMgmtBackupExportExtPolicyTable,
       "cucsMgmtBackupExportExtPolicyEntry": cucsMgmtBackupExportExtPolicyEntry,
       "cucsMgmtBackupExportExtPolicyInstanceId": cucsMgmtBackupExportExtPolicyInstanceId,
       "cucsMgmtBackupExportExtPolicyDn": cucsMgmtBackupExportExtPolicyDn,
       "cucsMgmtBackupExportExtPolicyRn": cucsMgmtBackupExportExtPolicyRn,
       "cucsMgmtBackupExportExtPolicyAdminState": cucsMgmtBackupExportExtPolicyAdminState,
       "cucsMgmtBackupExportExtPolicyDescr": cucsMgmtBackupExportExtPolicyDescr,
       "cucsMgmtBackupExportExtPolicyFrequency": cucsMgmtBackupExportExtPolicyFrequency,
       "cucsMgmtBackupExportExtPolicyIntId": cucsMgmtBackupExportExtPolicyIntId,
       "cucsMgmtBackupExportExtPolicyName": cucsMgmtBackupExportExtPolicyName,
       "cucsMgmtBackupExportExtPolicyPolicyLevel": cucsMgmtBackupExportExtPolicyPolicyLevel,
       "cucsMgmtBackupExportExtPolicyPolicyOwner": cucsMgmtBackupExportExtPolicyPolicyOwner,
       "cucsMgmtBackupPolicyConfigTable": cucsMgmtBackupPolicyConfigTable,
       "cucsMgmtBackupPolicyConfigEntry": cucsMgmtBackupPolicyConfigEntry,
       "cucsMgmtBackupPolicyConfigInstanceId": cucsMgmtBackupPolicyConfigInstanceId,
       "cucsMgmtBackupPolicyConfigDn": cucsMgmtBackupPolicyConfigDn,
       "cucsMgmtBackupPolicyConfigRn": cucsMgmtBackupPolicyConfigRn,
       "cucsMgmtBackupPolicyConfigAdminState": cucsMgmtBackupPolicyConfigAdminState,
       "cucsMgmtBackupPolicyConfigAutoDelete": cucsMgmtBackupPolicyConfigAutoDelete,
       "cucsMgmtBackupPolicyConfigBackupDate": cucsMgmtBackupPolicyConfigBackupDate,
       "cucsMgmtBackupPolicyConfigBackupIssue": cucsMgmtBackupPolicyConfigBackupIssue,
       "cucsMgmtBackupPolicyConfigDescr": cucsMgmtBackupPolicyConfigDescr,
       "cucsMgmtBackupPolicyConfigIgnoreCap": cucsMgmtBackupPolicyConfigIgnoreCap,
       "cucsMgmtBackupPolicyConfigIntId": cucsMgmtBackupPolicyConfigIntId,
       "cucsMgmtBackupPolicyConfigName": cucsMgmtBackupPolicyConfigName,
       "cucsMgmtBackupPolicyConfigOperScheduler": cucsMgmtBackupPolicyConfigOperScheduler,
       "cucsMgmtBackupPolicyConfigOperState": cucsMgmtBackupPolicyConfigOperState,
       "cucsMgmtBackupPolicyConfigPolicyLevel": cucsMgmtBackupPolicyConfigPolicyLevel,
       "cucsMgmtBackupPolicyConfigPolicyOwner": cucsMgmtBackupPolicyConfigPolicyOwner,
       "cucsMgmtBackupPolicyConfigScheduler": cucsMgmtBackupPolicyConfigScheduler,
       "cucsMgmtCimcSecureBootTable": cucsMgmtCimcSecureBootTable,
       "cucsMgmtCimcSecureBootEntry": cucsMgmtCimcSecureBootEntry,
       "cucsMgmtCimcSecureBootInstanceId": cucsMgmtCimcSecureBootInstanceId,
       "cucsMgmtCimcSecureBootDn": cucsMgmtCimcSecureBootDn,
       "cucsMgmtCimcSecureBootRn": cucsMgmtCimcSecureBootRn,
       "cucsMgmtCimcSecureBootAdminState": cucsMgmtCimcSecureBootAdminState,
       "cucsMgmtCimcSecureBootOperState": cucsMgmtCimcSecureBootOperState,
       "cucsMgmtHealthAttrTable": cucsMgmtHealthAttrTable,
       "cucsMgmtHealthAttrEntry": cucsMgmtHealthAttrEntry,
       "cucsMgmtHealthAttrInstanceId": cucsMgmtHealthAttrInstanceId,
       "cucsMgmtHealthAttrDn": cucsMgmtHealthAttrDn,
       "cucsMgmtHealthAttrRn": cucsMgmtHealthAttrRn,
       "cucsMgmtHealthAttrDescription": cucsMgmtHealthAttrDescription,
       "cucsMgmtHealthAttrName": cucsMgmtHealthAttrName,
       "cucsMgmtHealthAttrSeverity": cucsMgmtHealthAttrSeverity,
       "cucsMgmtHealthAttrValue": cucsMgmtHealthAttrValue,
       "cucsMgmtHealthStatusTable": cucsMgmtHealthStatusTable,
       "cucsMgmtHealthStatusEntry": cucsMgmtHealthStatusEntry,
       "cucsMgmtHealthStatusInstanceId": cucsMgmtHealthStatusInstanceId,
       "cucsMgmtHealthStatusDn": cucsMgmtHealthStatusDn,
       "cucsMgmtHealthStatusRn": cucsMgmtHealthStatusRn,
       "cucsMgmtHealthStatusHealthQualifier": cucsMgmtHealthStatusHealthQualifier,
       "cucsMgmtHealthStatusHealthSeverity": cucsMgmtHealthStatusHealthSeverity}
)
