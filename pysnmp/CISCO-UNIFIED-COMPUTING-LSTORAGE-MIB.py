# SNMP MIB module (CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:54 2024
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

(CucsLsConfigIssues,
 CucsLstorageAdminState,
 CucsLstorageAutoDeploy,
 CucsLstorageAvailability,
 CucsLstorageBootDevice,
 CucsLstorageConfigIssues,
 CucsLstorageConfigState,
 CucsLstorageControllerQualifierControllerType,
 CucsLstorageDasScsiLunStorageClass,
 CucsLstorageLunMapType,
 CucsLstorageVirtualDriveDefAccessPolicy,
 CucsLstorageVirtualDriveDefDriveCache,
 CucsLstorageVirtualDriveDefIoPolicy,
 CucsLstorageVirtualDriveDefReadPolicy,
 CucsLstorageVirtualDriveDefStripSize,
 CucsLstorageVirtualDriveDefWriteCachePolicy,
 CucsPolicyPolicyOwner,
 CucsStorageControllerId,
 CucsStorageDiskRole,
 CucsStorageLocalDiskMode,
 CucsStorageLunType,
 CucsStorageTechnologyConfig,
 CucsStorageUnitOperState) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsLsConfigIssues",
    "CucsLstorageAdminState",
    "CucsLstorageAutoDeploy",
    "CucsLstorageAvailability",
    "CucsLstorageBootDevice",
    "CucsLstorageConfigIssues",
    "CucsLstorageConfigState",
    "CucsLstorageControllerQualifierControllerType",
    "CucsLstorageDasScsiLunStorageClass",
    "CucsLstorageLunMapType",
    "CucsLstorageVirtualDriveDefAccessPolicy",
    "CucsLstorageVirtualDriveDefDriveCache",
    "CucsLstorageVirtualDriveDefIoPolicy",
    "CucsLstorageVirtualDriveDefReadPolicy",
    "CucsLstorageVirtualDriveDefStripSize",
    "CucsLstorageVirtualDriveDefWriteCachePolicy",
    "CucsPolicyPolicyOwner",
    "CucsStorageControllerId",
    "CucsStorageDiskRole",
    "CucsStorageLocalDiskMode",
    "CucsStorageLunType",
    "CucsStorageTechnologyConfig",
    "CucsStorageUnitOperState")

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

cucsLstorageObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsLstorageDasScsiLunTable_Object = MibTable
cucsLstorageDasScsiLunTable = _CucsLstorageDasScsiLunTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14)
)
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunTable.setStatus("current")
_CucsLstorageDasScsiLunEntry_Object = MibTableRow
cucsLstorageDasScsiLunEntry = _CucsLstorageDasScsiLunEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1)
)
cucsLstorageDasScsiLunEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB", "cucsLstorageDasScsiLunInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunEntry.setStatus("current")
_CucsLstorageDasScsiLunInstanceId_Type = CucsManagedObjectId
_CucsLstorageDasScsiLunInstanceId_Object = MibTableColumn
cucsLstorageDasScsiLunInstanceId = _CucsLstorageDasScsiLunInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 1),
    _CucsLstorageDasScsiLunInstanceId_Type()
)
cucsLstorageDasScsiLunInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunInstanceId.setStatus("current")
_CucsLstorageDasScsiLunDn_Type = CucsManagedObjectDn
_CucsLstorageDasScsiLunDn_Object = MibTableColumn
cucsLstorageDasScsiLunDn = _CucsLstorageDasScsiLunDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 2),
    _CucsLstorageDasScsiLunDn_Type()
)
cucsLstorageDasScsiLunDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunDn.setStatus("current")
_CucsLstorageDasScsiLunRn_Type = SnmpAdminString
_CucsLstorageDasScsiLunRn_Object = MibTableColumn
cucsLstorageDasScsiLunRn = _CucsLstorageDasScsiLunRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 3),
    _CucsLstorageDasScsiLunRn_Type()
)
cucsLstorageDasScsiLunRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunRn.setStatus("current")
_CucsLstorageDasScsiLunAdminState_Type = CucsLstorageAdminState
_CucsLstorageDasScsiLunAdminState_Object = MibTableColumn
cucsLstorageDasScsiLunAdminState = _CucsLstorageDasScsiLunAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 4),
    _CucsLstorageDasScsiLunAdminState_Type()
)
cucsLstorageDasScsiLunAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunAdminState.setStatus("current")
_CucsLstorageDasScsiLunAutoDeploy_Type = CucsLstorageAutoDeploy
_CucsLstorageDasScsiLunAutoDeploy_Object = MibTableColumn
cucsLstorageDasScsiLunAutoDeploy = _CucsLstorageDasScsiLunAutoDeploy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 5),
    _CucsLstorageDasScsiLunAutoDeploy_Type()
)
cucsLstorageDasScsiLunAutoDeploy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunAutoDeploy.setStatus("current")
_CucsLstorageDasScsiLunBootDev_Type = CucsLstorageBootDevice
_CucsLstorageDasScsiLunBootDev_Object = MibTableColumn
cucsLstorageDasScsiLunBootDev = _CucsLstorageDasScsiLunBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 6),
    _CucsLstorageDasScsiLunBootDev_Type()
)
cucsLstorageDasScsiLunBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunBootDev.setStatus("current")
_CucsLstorageDasScsiLunConfigQualifier_Type = CucsLstorageConfigIssues
_CucsLstorageDasScsiLunConfigQualifier_Object = MibTableColumn
cucsLstorageDasScsiLunConfigQualifier = _CucsLstorageDasScsiLunConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 7),
    _CucsLstorageDasScsiLunConfigQualifier_Type()
)
cucsLstorageDasScsiLunConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunConfigQualifier.setStatus("current")
_CucsLstorageDasScsiLunConfigState_Type = CucsLstorageConfigState
_CucsLstorageDasScsiLunConfigState_Object = MibTableColumn
cucsLstorageDasScsiLunConfigState = _CucsLstorageDasScsiLunConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 8),
    _CucsLstorageDasScsiLunConfigState_Type()
)
cucsLstorageDasScsiLunConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunConfigState.setStatus("current")
_CucsLstorageDasScsiLunExpandToAvail_Type = TruthValue
_CucsLstorageDasScsiLunExpandToAvail_Object = MibTableColumn
cucsLstorageDasScsiLunExpandToAvail = _CucsLstorageDasScsiLunExpandToAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 9),
    _CucsLstorageDasScsiLunExpandToAvail_Type()
)
cucsLstorageDasScsiLunExpandToAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunExpandToAvail.setStatus("current")
_CucsLstorageDasScsiLunLocalDiskPolicyName_Type = SnmpAdminString
_CucsLstorageDasScsiLunLocalDiskPolicyName_Object = MibTableColumn
cucsLstorageDasScsiLunLocalDiskPolicyName = _CucsLstorageDasScsiLunLocalDiskPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 10),
    _CucsLstorageDasScsiLunLocalDiskPolicyName_Type()
)
cucsLstorageDasScsiLunLocalDiskPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunLocalDiskPolicyName.setStatus("current")
_CucsLstorageDasScsiLunLunDn_Type = SnmpAdminString
_CucsLstorageDasScsiLunLunDn_Object = MibTableColumn
cucsLstorageDasScsiLunLunDn = _CucsLstorageDasScsiLunLunDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 11),
    _CucsLstorageDasScsiLunLunDn_Type()
)
cucsLstorageDasScsiLunLunDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunLunDn.setStatus("current")
_CucsLstorageDasScsiLunLunMapType_Type = CucsLstorageLunMapType
_CucsLstorageDasScsiLunLunMapType_Object = MibTableColumn
cucsLstorageDasScsiLunLunMapType = _CucsLstorageDasScsiLunLunMapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 12),
    _CucsLstorageDasScsiLunLunMapType_Type()
)
cucsLstorageDasScsiLunLunMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunLunMapType.setStatus("current")
_CucsLstorageDasScsiLunName_Type = SnmpAdminString
_CucsLstorageDasScsiLunName_Object = MibTableColumn
cucsLstorageDasScsiLunName = _CucsLstorageDasScsiLunName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 13),
    _CucsLstorageDasScsiLunName_Type()
)
cucsLstorageDasScsiLunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunName.setStatus("current")
_CucsLstorageDasScsiLunOperLocalDiskPolicyName_Type = SnmpAdminString
_CucsLstorageDasScsiLunOperLocalDiskPolicyName_Object = MibTableColumn
cucsLstorageDasScsiLunOperLocalDiskPolicyName = _CucsLstorageDasScsiLunOperLocalDiskPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 14),
    _CucsLstorageDasScsiLunOperLocalDiskPolicyName_Type()
)
cucsLstorageDasScsiLunOperLocalDiskPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunOperLocalDiskPolicyName.setStatus("current")
_CucsLstorageDasScsiLunOperState_Type = CucsStorageUnitOperState
_CucsLstorageDasScsiLunOperState_Object = MibTableColumn
cucsLstorageDasScsiLunOperState = _CucsLstorageDasScsiLunOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 15),
    _CucsLstorageDasScsiLunOperState_Type()
)
cucsLstorageDasScsiLunOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunOperState.setStatus("current")
_CucsLstorageDasScsiLunOrder_Type = Gauge32
_CucsLstorageDasScsiLunOrder_Object = MibTableColumn
cucsLstorageDasScsiLunOrder = _CucsLstorageDasScsiLunOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 16),
    _CucsLstorageDasScsiLunOrder_Type()
)
cucsLstorageDasScsiLunOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunOrder.setStatus("current")
_CucsLstorageDasScsiLunSize_Type = Unsigned64
_CucsLstorageDasScsiLunSize_Object = MibTableColumn
cucsLstorageDasScsiLunSize = _CucsLstorageDasScsiLunSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 17),
    _CucsLstorageDasScsiLunSize_Type()
)
cucsLstorageDasScsiLunSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunSize.setStatus("current")
_CucsLstorageDasScsiLunStorageClass_Type = CucsLstorageDasScsiLunStorageClass
_CucsLstorageDasScsiLunStorageClass_Object = MibTableColumn
cucsLstorageDasScsiLunStorageClass = _CucsLstorageDasScsiLunStorageClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 18),
    _CucsLstorageDasScsiLunStorageClass_Type()
)
cucsLstorageDasScsiLunStorageClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunStorageClass.setStatus("current")
_CucsLstorageDasScsiLunDeferredNaming_Type = TruthValue
_CucsLstorageDasScsiLunDeferredNaming_Object = MibTableColumn
cucsLstorageDasScsiLunDeferredNaming = _CucsLstorageDasScsiLunDeferredNaming_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 14, 1, 19),
    _CucsLstorageDasScsiLunDeferredNaming_Type()
)
cucsLstorageDasScsiLunDeferredNaming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDasScsiLunDeferredNaming.setStatus("current")
_CucsLstorageDiskGroupConfigDefTable_Object = MibTable
cucsLstorageDiskGroupConfigDefTable = _CucsLstorageDiskGroupConfigDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 15)
)
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigDefTable.setStatus("current")
_CucsLstorageDiskGroupConfigDefEntry_Object = MibTableRow
cucsLstorageDiskGroupConfigDefEntry = _CucsLstorageDiskGroupConfigDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 15, 1)
)
cucsLstorageDiskGroupConfigDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB", "cucsLstorageDiskGroupConfigDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigDefEntry.setStatus("current")
_CucsLstorageDiskGroupConfigDefInstanceId_Type = CucsManagedObjectId
_CucsLstorageDiskGroupConfigDefInstanceId_Object = MibTableColumn
cucsLstorageDiskGroupConfigDefInstanceId = _CucsLstorageDiskGroupConfigDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 15, 1, 1),
    _CucsLstorageDiskGroupConfigDefInstanceId_Type()
)
cucsLstorageDiskGroupConfigDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigDefInstanceId.setStatus("current")
_CucsLstorageDiskGroupConfigDefDn_Type = CucsManagedObjectDn
_CucsLstorageDiskGroupConfigDefDn_Object = MibTableColumn
cucsLstorageDiskGroupConfigDefDn = _CucsLstorageDiskGroupConfigDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 15, 1, 2),
    _CucsLstorageDiskGroupConfigDefDn_Type()
)
cucsLstorageDiskGroupConfigDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigDefDn.setStatus("current")
_CucsLstorageDiskGroupConfigDefRn_Type = SnmpAdminString
_CucsLstorageDiskGroupConfigDefRn_Object = MibTableColumn
cucsLstorageDiskGroupConfigDefRn = _CucsLstorageDiskGroupConfigDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 15, 1, 3),
    _CucsLstorageDiskGroupConfigDefRn_Type()
)
cucsLstorageDiskGroupConfigDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigDefRn.setStatus("current")
_CucsLstorageDiskGroupConfigDefDescr_Type = SnmpAdminString
_CucsLstorageDiskGroupConfigDefDescr_Object = MibTableColumn
cucsLstorageDiskGroupConfigDefDescr = _CucsLstorageDiskGroupConfigDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 15, 1, 4),
    _CucsLstorageDiskGroupConfigDefDescr_Type()
)
cucsLstorageDiskGroupConfigDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigDefDescr.setStatus("current")
_CucsLstorageDiskGroupConfigDefIntId_Type = SnmpAdminString
_CucsLstorageDiskGroupConfigDefIntId_Object = MibTableColumn
cucsLstorageDiskGroupConfigDefIntId = _CucsLstorageDiskGroupConfigDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 15, 1, 5),
    _CucsLstorageDiskGroupConfigDefIntId_Type()
)
cucsLstorageDiskGroupConfigDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigDefIntId.setStatus("current")
_CucsLstorageDiskGroupConfigDefName_Type = SnmpAdminString
_CucsLstorageDiskGroupConfigDefName_Object = MibTableColumn
cucsLstorageDiskGroupConfigDefName = _CucsLstorageDiskGroupConfigDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 15, 1, 6),
    _CucsLstorageDiskGroupConfigDefName_Type()
)
cucsLstorageDiskGroupConfigDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigDefName.setStatus("current")
_CucsLstorageDiskGroupConfigDefPolicyLevel_Type = Gauge32
_CucsLstorageDiskGroupConfigDefPolicyLevel_Object = MibTableColumn
cucsLstorageDiskGroupConfigDefPolicyLevel = _CucsLstorageDiskGroupConfigDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 15, 1, 7),
    _CucsLstorageDiskGroupConfigDefPolicyLevel_Type()
)
cucsLstorageDiskGroupConfigDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigDefPolicyLevel.setStatus("current")
_CucsLstorageDiskGroupConfigDefPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsLstorageDiskGroupConfigDefPolicyOwner_Object = MibTableColumn
cucsLstorageDiskGroupConfigDefPolicyOwner = _CucsLstorageDiskGroupConfigDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 15, 1, 8),
    _CucsLstorageDiskGroupConfigDefPolicyOwner_Type()
)
cucsLstorageDiskGroupConfigDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigDefPolicyOwner.setStatus("current")
_CucsLstorageDiskGroupConfigDefRaidLevel_Type = CucsStorageLunType
_CucsLstorageDiskGroupConfigDefRaidLevel_Object = MibTableColumn
cucsLstorageDiskGroupConfigDefRaidLevel = _CucsLstorageDiskGroupConfigDefRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 15, 1, 9),
    _CucsLstorageDiskGroupConfigDefRaidLevel_Type()
)
cucsLstorageDiskGroupConfigDefRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigDefRaidLevel.setStatus("current")
_CucsLstorageDiskGroupConfigPolicyTable_Object = MibTable
cucsLstorageDiskGroupConfigPolicyTable = _CucsLstorageDiskGroupConfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 16)
)
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigPolicyTable.setStatus("current")
_CucsLstorageDiskGroupConfigPolicyEntry_Object = MibTableRow
cucsLstorageDiskGroupConfigPolicyEntry = _CucsLstorageDiskGroupConfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 16, 1)
)
cucsLstorageDiskGroupConfigPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB", "cucsLstorageDiskGroupConfigPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigPolicyEntry.setStatus("current")
_CucsLstorageDiskGroupConfigPolicyInstanceId_Type = CucsManagedObjectId
_CucsLstorageDiskGroupConfigPolicyInstanceId_Object = MibTableColumn
cucsLstorageDiskGroupConfigPolicyInstanceId = _CucsLstorageDiskGroupConfigPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 16, 1, 1),
    _CucsLstorageDiskGroupConfigPolicyInstanceId_Type()
)
cucsLstorageDiskGroupConfigPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigPolicyInstanceId.setStatus("current")
_CucsLstorageDiskGroupConfigPolicyDn_Type = CucsManagedObjectDn
_CucsLstorageDiskGroupConfigPolicyDn_Object = MibTableColumn
cucsLstorageDiskGroupConfigPolicyDn = _CucsLstorageDiskGroupConfigPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 16, 1, 2),
    _CucsLstorageDiskGroupConfigPolicyDn_Type()
)
cucsLstorageDiskGroupConfigPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigPolicyDn.setStatus("current")
_CucsLstorageDiskGroupConfigPolicyRn_Type = SnmpAdminString
_CucsLstorageDiskGroupConfigPolicyRn_Object = MibTableColumn
cucsLstorageDiskGroupConfigPolicyRn = _CucsLstorageDiskGroupConfigPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 16, 1, 3),
    _CucsLstorageDiskGroupConfigPolicyRn_Type()
)
cucsLstorageDiskGroupConfigPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigPolicyRn.setStatus("current")
_CucsLstorageDiskGroupConfigPolicyDescr_Type = SnmpAdminString
_CucsLstorageDiskGroupConfigPolicyDescr_Object = MibTableColumn
cucsLstorageDiskGroupConfigPolicyDescr = _CucsLstorageDiskGroupConfigPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 16, 1, 4),
    _CucsLstorageDiskGroupConfigPolicyDescr_Type()
)
cucsLstorageDiskGroupConfigPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigPolicyDescr.setStatus("current")
_CucsLstorageDiskGroupConfigPolicyIntId_Type = SnmpAdminString
_CucsLstorageDiskGroupConfigPolicyIntId_Object = MibTableColumn
cucsLstorageDiskGroupConfigPolicyIntId = _CucsLstorageDiskGroupConfigPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 16, 1, 5),
    _CucsLstorageDiskGroupConfigPolicyIntId_Type()
)
cucsLstorageDiskGroupConfigPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigPolicyIntId.setStatus("current")
_CucsLstorageDiskGroupConfigPolicyName_Type = SnmpAdminString
_CucsLstorageDiskGroupConfigPolicyName_Object = MibTableColumn
cucsLstorageDiskGroupConfigPolicyName = _CucsLstorageDiskGroupConfigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 16, 1, 6),
    _CucsLstorageDiskGroupConfigPolicyName_Type()
)
cucsLstorageDiskGroupConfigPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigPolicyName.setStatus("current")
_CucsLstorageDiskGroupConfigPolicyPolicyLevel_Type = Gauge32
_CucsLstorageDiskGroupConfigPolicyPolicyLevel_Object = MibTableColumn
cucsLstorageDiskGroupConfigPolicyPolicyLevel = _CucsLstorageDiskGroupConfigPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 16, 1, 7),
    _CucsLstorageDiskGroupConfigPolicyPolicyLevel_Type()
)
cucsLstorageDiskGroupConfigPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigPolicyPolicyLevel.setStatus("current")
_CucsLstorageDiskGroupConfigPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsLstorageDiskGroupConfigPolicyPolicyOwner_Object = MibTableColumn
cucsLstorageDiskGroupConfigPolicyPolicyOwner = _CucsLstorageDiskGroupConfigPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 16, 1, 8),
    _CucsLstorageDiskGroupConfigPolicyPolicyOwner_Type()
)
cucsLstorageDiskGroupConfigPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigPolicyPolicyOwner.setStatus("current")
_CucsLstorageDiskGroupConfigPolicyRaidLevel_Type = CucsStorageLunType
_CucsLstorageDiskGroupConfigPolicyRaidLevel_Object = MibTableColumn
cucsLstorageDiskGroupConfigPolicyRaidLevel = _CucsLstorageDiskGroupConfigPolicyRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 16, 1, 9),
    _CucsLstorageDiskGroupConfigPolicyRaidLevel_Type()
)
cucsLstorageDiskGroupConfigPolicyRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupConfigPolicyRaidLevel.setStatus("current")
_CucsLstorageDiskGroupQualifierTable_Object = MibTable
cucsLstorageDiskGroupQualifierTable = _CucsLstorageDiskGroupQualifierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 17)
)
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupQualifierTable.setStatus("current")
_CucsLstorageDiskGroupQualifierEntry_Object = MibTableRow
cucsLstorageDiskGroupQualifierEntry = _CucsLstorageDiskGroupQualifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 17, 1)
)
cucsLstorageDiskGroupQualifierEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB", "cucsLstorageDiskGroupQualifierInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupQualifierEntry.setStatus("current")
_CucsLstorageDiskGroupQualifierInstanceId_Type = CucsManagedObjectId
_CucsLstorageDiskGroupQualifierInstanceId_Object = MibTableColumn
cucsLstorageDiskGroupQualifierInstanceId = _CucsLstorageDiskGroupQualifierInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 17, 1, 1),
    _CucsLstorageDiskGroupQualifierInstanceId_Type()
)
cucsLstorageDiskGroupQualifierInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupQualifierInstanceId.setStatus("current")
_CucsLstorageDiskGroupQualifierDn_Type = CucsManagedObjectDn
_CucsLstorageDiskGroupQualifierDn_Object = MibTableColumn
cucsLstorageDiskGroupQualifierDn = _CucsLstorageDiskGroupQualifierDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 17, 1, 2),
    _CucsLstorageDiskGroupQualifierDn_Type()
)
cucsLstorageDiskGroupQualifierDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupQualifierDn.setStatus("current")
_CucsLstorageDiskGroupQualifierRn_Type = SnmpAdminString
_CucsLstorageDiskGroupQualifierRn_Object = MibTableColumn
cucsLstorageDiskGroupQualifierRn = _CucsLstorageDiskGroupQualifierRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 17, 1, 3),
    _CucsLstorageDiskGroupQualifierRn_Type()
)
cucsLstorageDiskGroupQualifierRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupQualifierRn.setStatus("current")
_CucsLstorageDiskGroupQualifierDriveType_Type = CucsStorageTechnologyConfig
_CucsLstorageDiskGroupQualifierDriveType_Object = MibTableColumn
cucsLstorageDiskGroupQualifierDriveType = _CucsLstorageDiskGroupQualifierDriveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 17, 1, 4),
    _CucsLstorageDiskGroupQualifierDriveType_Type()
)
cucsLstorageDiskGroupQualifierDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupQualifierDriveType.setStatus("current")
_CucsLstorageDiskGroupQualifierMinDriveSize_Type = Unsigned64
_CucsLstorageDiskGroupQualifierMinDriveSize_Object = MibTableColumn
cucsLstorageDiskGroupQualifierMinDriveSize = _CucsLstorageDiskGroupQualifierMinDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 17, 1, 5),
    _CucsLstorageDiskGroupQualifierMinDriveSize_Type()
)
cucsLstorageDiskGroupQualifierMinDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupQualifierMinDriveSize.setStatus("current")
_CucsLstorageDiskGroupQualifierNumDedHotSpares_Type = Gauge32
_CucsLstorageDiskGroupQualifierNumDedHotSpares_Object = MibTableColumn
cucsLstorageDiskGroupQualifierNumDedHotSpares = _CucsLstorageDiskGroupQualifierNumDedHotSpares_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 17, 1, 6),
    _CucsLstorageDiskGroupQualifierNumDedHotSpares_Type()
)
cucsLstorageDiskGroupQualifierNumDedHotSpares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupQualifierNumDedHotSpares.setStatus("current")
_CucsLstorageDiskGroupQualifierNumDrives_Type = Gauge32
_CucsLstorageDiskGroupQualifierNumDrives_Object = MibTableColumn
cucsLstorageDiskGroupQualifierNumDrives = _CucsLstorageDiskGroupQualifierNumDrives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 17, 1, 7),
    _CucsLstorageDiskGroupQualifierNumDrives_Type()
)
cucsLstorageDiskGroupQualifierNumDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupQualifierNumDrives.setStatus("current")
_CucsLstorageDiskGroupQualifierNumGlobHotSpares_Type = Gauge32
_CucsLstorageDiskGroupQualifierNumGlobHotSpares_Object = MibTableColumn
cucsLstorageDiskGroupQualifierNumGlobHotSpares = _CucsLstorageDiskGroupQualifierNumGlobHotSpares_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 17, 1, 8),
    _CucsLstorageDiskGroupQualifierNumGlobHotSpares_Type()
)
cucsLstorageDiskGroupQualifierNumGlobHotSpares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupQualifierNumGlobHotSpares.setStatus("current")
_CucsLstorageDiskGroupQualifierUseRemainingDisks_Type = TruthValue
_CucsLstorageDiskGroupQualifierUseRemainingDisks_Object = MibTableColumn
cucsLstorageDiskGroupQualifierUseRemainingDisks = _CucsLstorageDiskGroupQualifierUseRemainingDisks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 17, 1, 9),
    _CucsLstorageDiskGroupQualifierUseRemainingDisks_Type()
)
cucsLstorageDiskGroupQualifierUseRemainingDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageDiskGroupQualifierUseRemainingDisks.setStatus("current")
_CucsLstorageLocalDiskConfigRefTable_Object = MibTable
cucsLstorageLocalDiskConfigRefTable = _CucsLstorageLocalDiskConfigRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 21)
)
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskConfigRefTable.setStatus("current")
_CucsLstorageLocalDiskConfigRefEntry_Object = MibTableRow
cucsLstorageLocalDiskConfigRefEntry = _CucsLstorageLocalDiskConfigRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 21, 1)
)
cucsLstorageLocalDiskConfigRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB", "cucsLstorageLocalDiskConfigRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskConfigRefEntry.setStatus("current")
_CucsLstorageLocalDiskConfigRefInstanceId_Type = CucsManagedObjectId
_CucsLstorageLocalDiskConfigRefInstanceId_Object = MibTableColumn
cucsLstorageLocalDiskConfigRefInstanceId = _CucsLstorageLocalDiskConfigRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 21, 1, 1),
    _CucsLstorageLocalDiskConfigRefInstanceId_Type()
)
cucsLstorageLocalDiskConfigRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskConfigRefInstanceId.setStatus("current")
_CucsLstorageLocalDiskConfigRefDn_Type = CucsManagedObjectDn
_CucsLstorageLocalDiskConfigRefDn_Object = MibTableColumn
cucsLstorageLocalDiskConfigRefDn = _CucsLstorageLocalDiskConfigRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 21, 1, 2),
    _CucsLstorageLocalDiskConfigRefDn_Type()
)
cucsLstorageLocalDiskConfigRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskConfigRefDn.setStatus("current")
_CucsLstorageLocalDiskConfigRefRn_Type = SnmpAdminString
_CucsLstorageLocalDiskConfigRefRn_Object = MibTableColumn
cucsLstorageLocalDiskConfigRefRn = _CucsLstorageLocalDiskConfigRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 21, 1, 3),
    _CucsLstorageLocalDiskConfigRefRn_Type()
)
cucsLstorageLocalDiskConfigRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskConfigRefRn.setStatus("current")
_CucsLstorageLocalDiskConfigRefRole_Type = CucsStorageDiskRole
_CucsLstorageLocalDiskConfigRefRole_Object = MibTableColumn
cucsLstorageLocalDiskConfigRefRole = _CucsLstorageLocalDiskConfigRefRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 21, 1, 4),
    _CucsLstorageLocalDiskConfigRefRole_Type()
)
cucsLstorageLocalDiskConfigRefRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskConfigRefRole.setStatus("current")
_CucsLstorageLocalDiskConfigRefSlotNum_Type = Gauge32
_CucsLstorageLocalDiskConfigRefSlotNum_Object = MibTableColumn
cucsLstorageLocalDiskConfigRefSlotNum = _CucsLstorageLocalDiskConfigRefSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 21, 1, 5),
    _CucsLstorageLocalDiskConfigRefSlotNum_Type()
)
cucsLstorageLocalDiskConfigRefSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskConfigRefSlotNum.setStatus("current")
_CucsLstorageLocalDiskConfigRefSpanId_Type = Gauge32
_CucsLstorageLocalDiskConfigRefSpanId_Object = MibTableColumn
cucsLstorageLocalDiskConfigRefSpanId = _CucsLstorageLocalDiskConfigRefSpanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 21, 1, 6),
    _CucsLstorageLocalDiskConfigRefSpanId_Type()
)
cucsLstorageLocalDiskConfigRefSpanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskConfigRefSpanId.setStatus("current")
_CucsLstorageLocalDiskRefTable_Object = MibTable
cucsLstorageLocalDiskRefTable = _CucsLstorageLocalDiskRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 22)
)
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskRefTable.setStatus("current")
_CucsLstorageLocalDiskRefEntry_Object = MibTableRow
cucsLstorageLocalDiskRefEntry = _CucsLstorageLocalDiskRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 22, 1)
)
cucsLstorageLocalDiskRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB", "cucsLstorageLocalDiskRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskRefEntry.setStatus("current")
_CucsLstorageLocalDiskRefInstanceId_Type = CucsManagedObjectId
_CucsLstorageLocalDiskRefInstanceId_Object = MibTableColumn
cucsLstorageLocalDiskRefInstanceId = _CucsLstorageLocalDiskRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 22, 1, 1),
    _CucsLstorageLocalDiskRefInstanceId_Type()
)
cucsLstorageLocalDiskRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskRefInstanceId.setStatus("current")
_CucsLstorageLocalDiskRefDn_Type = CucsManagedObjectDn
_CucsLstorageLocalDiskRefDn_Object = MibTableColumn
cucsLstorageLocalDiskRefDn = _CucsLstorageLocalDiskRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 22, 1, 2),
    _CucsLstorageLocalDiskRefDn_Type()
)
cucsLstorageLocalDiskRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskRefDn.setStatus("current")
_CucsLstorageLocalDiskRefRn_Type = SnmpAdminString
_CucsLstorageLocalDiskRefRn_Object = MibTableColumn
cucsLstorageLocalDiskRefRn = _CucsLstorageLocalDiskRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 22, 1, 3),
    _CucsLstorageLocalDiskRefRn_Type()
)
cucsLstorageLocalDiskRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskRefRn.setStatus("current")
_CucsLstorageLocalDiskRefEnclosureId_Type = Gauge32
_CucsLstorageLocalDiskRefEnclosureId_Object = MibTableColumn
cucsLstorageLocalDiskRefEnclosureId = _CucsLstorageLocalDiskRefEnclosureId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 22, 1, 4),
    _CucsLstorageLocalDiskRefEnclosureId_Type()
)
cucsLstorageLocalDiskRefEnclosureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskRefEnclosureId.setStatus("current")
_CucsLstorageLocalDiskRefSlotId_Type = Gauge32
_CucsLstorageLocalDiskRefSlotId_Object = MibTableColumn
cucsLstorageLocalDiskRefSlotId = _CucsLstorageLocalDiskRefSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 22, 1, 5),
    _CucsLstorageLocalDiskRefSlotId_Type()
)
cucsLstorageLocalDiskRefSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageLocalDiskRefSlotId.setStatus("current")
_CucsLstorageProfileTable_Object = MibTable
cucsLstorageProfileTable = _CucsLstorageProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 37)
)
if mibBuilder.loadTexts:
    cucsLstorageProfileTable.setStatus("current")
_CucsLstorageProfileEntry_Object = MibTableRow
cucsLstorageProfileEntry = _CucsLstorageProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 37, 1)
)
cucsLstorageProfileEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB", "cucsLstorageProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLstorageProfileEntry.setStatus("current")
_CucsLstorageProfileInstanceId_Type = CucsManagedObjectId
_CucsLstorageProfileInstanceId_Object = MibTableColumn
cucsLstorageProfileInstanceId = _CucsLstorageProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 37, 1, 1),
    _CucsLstorageProfileInstanceId_Type()
)
cucsLstorageProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLstorageProfileInstanceId.setStatus("current")
_CucsLstorageProfileDn_Type = CucsManagedObjectDn
_CucsLstorageProfileDn_Object = MibTableColumn
cucsLstorageProfileDn = _CucsLstorageProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 37, 1, 2),
    _CucsLstorageProfileDn_Type()
)
cucsLstorageProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileDn.setStatus("current")
_CucsLstorageProfileRn_Type = SnmpAdminString
_CucsLstorageProfileRn_Object = MibTableColumn
cucsLstorageProfileRn = _CucsLstorageProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 37, 1, 3),
    _CucsLstorageProfileRn_Type()
)
cucsLstorageProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileRn.setStatus("current")
_CucsLstorageProfileAssignedToDn_Type = SnmpAdminString
_CucsLstorageProfileAssignedToDn_Object = MibTableColumn
cucsLstorageProfileAssignedToDn = _CucsLstorageProfileAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 37, 1, 4),
    _CucsLstorageProfileAssignedToDn_Type()
)
cucsLstorageProfileAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileAssignedToDn.setStatus("current")
_CucsLstorageProfileAvailability_Type = CucsLstorageAvailability
_CucsLstorageProfileAvailability_Object = MibTableColumn
cucsLstorageProfileAvailability = _CucsLstorageProfileAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 37, 1, 5),
    _CucsLstorageProfileAvailability_Type()
)
cucsLstorageProfileAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileAvailability.setStatus("current")
_CucsLstorageProfileDescr_Type = SnmpAdminString
_CucsLstorageProfileDescr_Object = MibTableColumn
cucsLstorageProfileDescr = _CucsLstorageProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 37, 1, 6),
    _CucsLstorageProfileDescr_Type()
)
cucsLstorageProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileDescr.setStatus("current")
_CucsLstorageProfileIntId_Type = SnmpAdminString
_CucsLstorageProfileIntId_Object = MibTableColumn
cucsLstorageProfileIntId = _CucsLstorageProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 37, 1, 7),
    _CucsLstorageProfileIntId_Type()
)
cucsLstorageProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileIntId.setStatus("current")
_CucsLstorageProfileName_Type = SnmpAdminString
_CucsLstorageProfileName_Object = MibTableColumn
cucsLstorageProfileName = _CucsLstorageProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 37, 1, 8),
    _CucsLstorageProfileName_Type()
)
cucsLstorageProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileName.setStatus("current")
_CucsLstorageProfilePolicyLevel_Type = Gauge32
_CucsLstorageProfilePolicyLevel_Object = MibTableColumn
cucsLstorageProfilePolicyLevel = _CucsLstorageProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 37, 1, 9),
    _CucsLstorageProfilePolicyLevel_Type()
)
cucsLstorageProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfilePolicyLevel.setStatus("current")
_CucsLstorageProfilePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsLstorageProfilePolicyOwner_Object = MibTableColumn
cucsLstorageProfilePolicyOwner = _CucsLstorageProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 37, 1, 10),
    _CucsLstorageProfilePolicyOwner_Type()
)
cucsLstorageProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfilePolicyOwner.setStatus("current")
_CucsLstorageProfileBindingTable_Object = MibTable
cucsLstorageProfileBindingTable = _CucsLstorageProfileBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 38)
)
if mibBuilder.loadTexts:
    cucsLstorageProfileBindingTable.setStatus("current")
_CucsLstorageProfileBindingEntry_Object = MibTableRow
cucsLstorageProfileBindingEntry = _CucsLstorageProfileBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 38, 1)
)
cucsLstorageProfileBindingEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB", "cucsLstorageProfileBindingInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLstorageProfileBindingEntry.setStatus("current")
_CucsLstorageProfileBindingInstanceId_Type = CucsManagedObjectId
_CucsLstorageProfileBindingInstanceId_Object = MibTableColumn
cucsLstorageProfileBindingInstanceId = _CucsLstorageProfileBindingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 38, 1, 1),
    _CucsLstorageProfileBindingInstanceId_Type()
)
cucsLstorageProfileBindingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLstorageProfileBindingInstanceId.setStatus("current")
_CucsLstorageProfileBindingDn_Type = CucsManagedObjectDn
_CucsLstorageProfileBindingDn_Object = MibTableColumn
cucsLstorageProfileBindingDn = _CucsLstorageProfileBindingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 38, 1, 2),
    _CucsLstorageProfileBindingDn_Type()
)
cucsLstorageProfileBindingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileBindingDn.setStatus("current")
_CucsLstorageProfileBindingRn_Type = SnmpAdminString
_CucsLstorageProfileBindingRn_Object = MibTableColumn
cucsLstorageProfileBindingRn = _CucsLstorageProfileBindingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 38, 1, 3),
    _CucsLstorageProfileBindingRn_Type()
)
cucsLstorageProfileBindingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileBindingRn.setStatus("current")
_CucsLstorageProfileBindingAssignedToDn_Type = SnmpAdminString
_CucsLstorageProfileBindingAssignedToDn_Object = MibTableColumn
cucsLstorageProfileBindingAssignedToDn = _CucsLstorageProfileBindingAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 38, 1, 4),
    _CucsLstorageProfileBindingAssignedToDn_Type()
)
cucsLstorageProfileBindingAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileBindingAssignedToDn.setStatus("current")
_CucsLstorageProfileBindingIssues_Type = CucsLsConfigIssues
_CucsLstorageProfileBindingIssues_Object = MibTableColumn
cucsLstorageProfileBindingIssues = _CucsLstorageProfileBindingIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 38, 1, 5),
    _CucsLstorageProfileBindingIssues_Type()
)
cucsLstorageProfileBindingIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileBindingIssues.setStatus("current")
_CucsLstorageProfileBindingName_Type = SnmpAdminString
_CucsLstorageProfileBindingName_Object = MibTableColumn
cucsLstorageProfileBindingName = _CucsLstorageProfileBindingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 38, 1, 6),
    _CucsLstorageProfileBindingName_Type()
)
cucsLstorageProfileBindingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileBindingName.setStatus("current")
_CucsLstorageProfileBindingOperStorageProfileName_Type = SnmpAdminString
_CucsLstorageProfileBindingOperStorageProfileName_Object = MibTableColumn
cucsLstorageProfileBindingOperStorageProfileName = _CucsLstorageProfileBindingOperStorageProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 38, 1, 7),
    _CucsLstorageProfileBindingOperStorageProfileName_Type()
)
cucsLstorageProfileBindingOperStorageProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileBindingOperStorageProfileName.setStatus("current")
_CucsLstorageProfileBindingStorageProfileName_Type = SnmpAdminString
_CucsLstorageProfileBindingStorageProfileName_Object = MibTableColumn
cucsLstorageProfileBindingStorageProfileName = _CucsLstorageProfileBindingStorageProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 38, 1, 8),
    _CucsLstorageProfileBindingStorageProfileName_Type()
)
cucsLstorageProfileBindingStorageProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileBindingStorageProfileName.setStatus("current")
_CucsLstorageProfileDefTable_Object = MibTable
cucsLstorageProfileDefTable = _CucsLstorageProfileDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 39)
)
if mibBuilder.loadTexts:
    cucsLstorageProfileDefTable.setStatus("current")
_CucsLstorageProfileDefEntry_Object = MibTableRow
cucsLstorageProfileDefEntry = _CucsLstorageProfileDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 39, 1)
)
cucsLstorageProfileDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB", "cucsLstorageProfileDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLstorageProfileDefEntry.setStatus("current")
_CucsLstorageProfileDefInstanceId_Type = CucsManagedObjectId
_CucsLstorageProfileDefInstanceId_Object = MibTableColumn
cucsLstorageProfileDefInstanceId = _CucsLstorageProfileDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 39, 1, 1),
    _CucsLstorageProfileDefInstanceId_Type()
)
cucsLstorageProfileDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLstorageProfileDefInstanceId.setStatus("current")
_CucsLstorageProfileDefDn_Type = CucsManagedObjectDn
_CucsLstorageProfileDefDn_Object = MibTableColumn
cucsLstorageProfileDefDn = _CucsLstorageProfileDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 39, 1, 2),
    _CucsLstorageProfileDefDn_Type()
)
cucsLstorageProfileDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileDefDn.setStatus("current")
_CucsLstorageProfileDefRn_Type = SnmpAdminString
_CucsLstorageProfileDefRn_Object = MibTableColumn
cucsLstorageProfileDefRn = _CucsLstorageProfileDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 39, 1, 3),
    _CucsLstorageProfileDefRn_Type()
)
cucsLstorageProfileDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileDefRn.setStatus("current")
_CucsLstorageProfileDefAssignedToDn_Type = SnmpAdminString
_CucsLstorageProfileDefAssignedToDn_Object = MibTableColumn
cucsLstorageProfileDefAssignedToDn = _CucsLstorageProfileDefAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 39, 1, 4),
    _CucsLstorageProfileDefAssignedToDn_Type()
)
cucsLstorageProfileDefAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileDefAssignedToDn.setStatus("current")
_CucsLstorageProfileDefAvailability_Type = CucsLstorageAvailability
_CucsLstorageProfileDefAvailability_Object = MibTableColumn
cucsLstorageProfileDefAvailability = _CucsLstorageProfileDefAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 39, 1, 5),
    _CucsLstorageProfileDefAvailability_Type()
)
cucsLstorageProfileDefAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileDefAvailability.setStatus("current")
_CucsLstorageProfileDefDescr_Type = SnmpAdminString
_CucsLstorageProfileDefDescr_Object = MibTableColumn
cucsLstorageProfileDefDescr = _CucsLstorageProfileDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 39, 1, 6),
    _CucsLstorageProfileDefDescr_Type()
)
cucsLstorageProfileDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileDefDescr.setStatus("current")
_CucsLstorageProfileDefIntId_Type = SnmpAdminString
_CucsLstorageProfileDefIntId_Object = MibTableColumn
cucsLstorageProfileDefIntId = _CucsLstorageProfileDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 39, 1, 7),
    _CucsLstorageProfileDefIntId_Type()
)
cucsLstorageProfileDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileDefIntId.setStatus("current")
_CucsLstorageProfileDefName_Type = SnmpAdminString
_CucsLstorageProfileDefName_Object = MibTableColumn
cucsLstorageProfileDefName = _CucsLstorageProfileDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 39, 1, 8),
    _CucsLstorageProfileDefName_Type()
)
cucsLstorageProfileDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileDefName.setStatus("current")
_CucsLstorageProfileDefPolicyLevel_Type = Gauge32
_CucsLstorageProfileDefPolicyLevel_Object = MibTableColumn
cucsLstorageProfileDefPolicyLevel = _CucsLstorageProfileDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 39, 1, 9),
    _CucsLstorageProfileDefPolicyLevel_Type()
)
cucsLstorageProfileDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileDefPolicyLevel.setStatus("current")
_CucsLstorageProfileDefPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsLstorageProfileDefPolicyOwner_Object = MibTableColumn
cucsLstorageProfileDefPolicyOwner = _CucsLstorageProfileDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 39, 1, 10),
    _CucsLstorageProfileDefPolicyOwner_Type()
)
cucsLstorageProfileDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageProfileDefPolicyOwner.setStatus("current")
_CucsLstorageVirtualDriveDefTable_Object = MibTable
cucsLstorageVirtualDriveDefTable = _CucsLstorageVirtualDriveDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 49)
)
if mibBuilder.loadTexts:
    cucsLstorageVirtualDriveDefTable.setStatus("current")
_CucsLstorageVirtualDriveDefEntry_Object = MibTableRow
cucsLstorageVirtualDriveDefEntry = _CucsLstorageVirtualDriveDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 49, 1)
)
cucsLstorageVirtualDriveDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB", "cucsLstorageVirtualDriveDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLstorageVirtualDriveDefEntry.setStatus("current")
_CucsLstorageVirtualDriveDefInstanceId_Type = CucsManagedObjectId
_CucsLstorageVirtualDriveDefInstanceId_Object = MibTableColumn
cucsLstorageVirtualDriveDefInstanceId = _CucsLstorageVirtualDriveDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 49, 1, 1),
    _CucsLstorageVirtualDriveDefInstanceId_Type()
)
cucsLstorageVirtualDriveDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLstorageVirtualDriveDefInstanceId.setStatus("current")
_CucsLstorageVirtualDriveDefDn_Type = CucsManagedObjectDn
_CucsLstorageVirtualDriveDefDn_Object = MibTableColumn
cucsLstorageVirtualDriveDefDn = _CucsLstorageVirtualDriveDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 49, 1, 2),
    _CucsLstorageVirtualDriveDefDn_Type()
)
cucsLstorageVirtualDriveDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageVirtualDriveDefDn.setStatus("current")
_CucsLstorageVirtualDriveDefRn_Type = SnmpAdminString
_CucsLstorageVirtualDriveDefRn_Object = MibTableColumn
cucsLstorageVirtualDriveDefRn = _CucsLstorageVirtualDriveDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 49, 1, 3),
    _CucsLstorageVirtualDriveDefRn_Type()
)
cucsLstorageVirtualDriveDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageVirtualDriveDefRn.setStatus("current")
_CucsLstorageVirtualDriveDefAccessPolicy_Type = CucsLstorageVirtualDriveDefAccessPolicy
_CucsLstorageVirtualDriveDefAccessPolicy_Object = MibTableColumn
cucsLstorageVirtualDriveDefAccessPolicy = _CucsLstorageVirtualDriveDefAccessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 49, 1, 4),
    _CucsLstorageVirtualDriveDefAccessPolicy_Type()
)
cucsLstorageVirtualDriveDefAccessPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageVirtualDriveDefAccessPolicy.setStatus("current")
_CucsLstorageVirtualDriveDefDriveCache_Type = CucsLstorageVirtualDriveDefDriveCache
_CucsLstorageVirtualDriveDefDriveCache_Object = MibTableColumn
cucsLstorageVirtualDriveDefDriveCache = _CucsLstorageVirtualDriveDefDriveCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 49, 1, 5),
    _CucsLstorageVirtualDriveDefDriveCache_Type()
)
cucsLstorageVirtualDriveDefDriveCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageVirtualDriveDefDriveCache.setStatus("current")
_CucsLstorageVirtualDriveDefIoPolicy_Type = CucsLstorageVirtualDriveDefIoPolicy
_CucsLstorageVirtualDriveDefIoPolicy_Object = MibTableColumn
cucsLstorageVirtualDriveDefIoPolicy = _CucsLstorageVirtualDriveDefIoPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 49, 1, 6),
    _CucsLstorageVirtualDriveDefIoPolicy_Type()
)
cucsLstorageVirtualDriveDefIoPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageVirtualDriveDefIoPolicy.setStatus("current")
_CucsLstorageVirtualDriveDefReadPolicy_Type = CucsLstorageVirtualDriveDefReadPolicy
_CucsLstorageVirtualDriveDefReadPolicy_Object = MibTableColumn
cucsLstorageVirtualDriveDefReadPolicy = _CucsLstorageVirtualDriveDefReadPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 49, 1, 7),
    _CucsLstorageVirtualDriveDefReadPolicy_Type()
)
cucsLstorageVirtualDriveDefReadPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageVirtualDriveDefReadPolicy.setStatus("current")
_CucsLstorageVirtualDriveDefStripSize_Type = CucsLstorageVirtualDriveDefStripSize
_CucsLstorageVirtualDriveDefStripSize_Object = MibTableColumn
cucsLstorageVirtualDriveDefStripSize = _CucsLstorageVirtualDriveDefStripSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 49, 1, 8),
    _CucsLstorageVirtualDriveDefStripSize_Type()
)
cucsLstorageVirtualDriveDefStripSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageVirtualDriveDefStripSize.setStatus("current")
_CucsLstorageVirtualDriveDefWriteCachePolicy_Type = CucsLstorageVirtualDriveDefWriteCachePolicy
_CucsLstorageVirtualDriveDefWriteCachePolicy_Object = MibTableColumn
cucsLstorageVirtualDriveDefWriteCachePolicy = _CucsLstorageVirtualDriveDefWriteCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 49, 1, 9),
    _CucsLstorageVirtualDriveDefWriteCachePolicy_Type()
)
cucsLstorageVirtualDriveDefWriteCachePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageVirtualDriveDefWriteCachePolicy.setStatus("current")
_CucsLstorageControllerDefTable_Object = MibTable
cucsLstorageControllerDefTable = _CucsLstorageControllerDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 52)
)
if mibBuilder.loadTexts:
    cucsLstorageControllerDefTable.setStatus("current")
_CucsLstorageControllerDefEntry_Object = MibTableRow
cucsLstorageControllerDefEntry = _CucsLstorageControllerDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 52, 1)
)
cucsLstorageControllerDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB", "cucsLstorageControllerDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLstorageControllerDefEntry.setStatus("current")
_CucsLstorageControllerDefInstanceId_Type = CucsManagedObjectId
_CucsLstorageControllerDefInstanceId_Object = MibTableColumn
cucsLstorageControllerDefInstanceId = _CucsLstorageControllerDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 52, 1, 1),
    _CucsLstorageControllerDefInstanceId_Type()
)
cucsLstorageControllerDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLstorageControllerDefInstanceId.setStatus("current")
_CucsLstorageControllerDefDn_Type = CucsManagedObjectDn
_CucsLstorageControllerDefDn_Object = MibTableColumn
cucsLstorageControllerDefDn = _CucsLstorageControllerDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 52, 1, 2),
    _CucsLstorageControllerDefDn_Type()
)
cucsLstorageControllerDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerDefDn.setStatus("current")
_CucsLstorageControllerDefRn_Type = SnmpAdminString
_CucsLstorageControllerDefRn_Object = MibTableColumn
cucsLstorageControllerDefRn = _CucsLstorageControllerDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 52, 1, 3),
    _CucsLstorageControllerDefRn_Type()
)
cucsLstorageControllerDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerDefRn.setStatus("current")
_CucsLstorageControllerDefAdminState_Type = CucsLstorageAdminState
_CucsLstorageControllerDefAdminState_Object = MibTableColumn
cucsLstorageControllerDefAdminState = _CucsLstorageControllerDefAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 52, 1, 4),
    _CucsLstorageControllerDefAdminState_Type()
)
cucsLstorageControllerDefAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerDefAdminState.setStatus("current")
_CucsLstorageControllerDefConfigQualifier_Type = CucsLstorageConfigIssues
_CucsLstorageControllerDefConfigQualifier_Object = MibTableColumn
cucsLstorageControllerDefConfigQualifier = _CucsLstorageControllerDefConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 52, 1, 5),
    _CucsLstorageControllerDefConfigQualifier_Type()
)
cucsLstorageControllerDefConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerDefConfigQualifier.setStatus("current")
_CucsLstorageControllerDefConfigState_Type = CucsLstorageConfigState
_CucsLstorageControllerDefConfigState_Object = MibTableColumn
cucsLstorageControllerDefConfigState = _CucsLstorageControllerDefConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 52, 1, 6),
    _CucsLstorageControllerDefConfigState_Type()
)
cucsLstorageControllerDefConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerDefConfigState.setStatus("current")
_CucsLstorageControllerDefName_Type = SnmpAdminString
_CucsLstorageControllerDefName_Object = MibTableColumn
cucsLstorageControllerDefName = _CucsLstorageControllerDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 52, 1, 7),
    _CucsLstorageControllerDefName_Type()
)
cucsLstorageControllerDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerDefName.setStatus("current")
_CucsLstorageControllerDefOperState_Type = CucsStorageUnitOperState
_CucsLstorageControllerDefOperState_Object = MibTableColumn
cucsLstorageControllerDefOperState = _CucsLstorageControllerDefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 52, 1, 8),
    _CucsLstorageControllerDefOperState_Type()
)
cucsLstorageControllerDefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerDefOperState.setStatus("current")
_CucsLstorageControllerModeConfigTable_Object = MibTable
cucsLstorageControllerModeConfigTable = _CucsLstorageControllerModeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 53)
)
if mibBuilder.loadTexts:
    cucsLstorageControllerModeConfigTable.setStatus("current")
_CucsLstorageControllerModeConfigEntry_Object = MibTableRow
cucsLstorageControllerModeConfigEntry = _CucsLstorageControllerModeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 53, 1)
)
cucsLstorageControllerModeConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB", "cucsLstorageControllerModeConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLstorageControllerModeConfigEntry.setStatus("current")
_CucsLstorageControllerModeConfigInstanceId_Type = CucsManagedObjectId
_CucsLstorageControllerModeConfigInstanceId_Object = MibTableColumn
cucsLstorageControllerModeConfigInstanceId = _CucsLstorageControllerModeConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 53, 1, 1),
    _CucsLstorageControllerModeConfigInstanceId_Type()
)
cucsLstorageControllerModeConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLstorageControllerModeConfigInstanceId.setStatus("current")
_CucsLstorageControllerModeConfigDn_Type = CucsManagedObjectDn
_CucsLstorageControllerModeConfigDn_Object = MibTableColumn
cucsLstorageControllerModeConfigDn = _CucsLstorageControllerModeConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 53, 1, 2),
    _CucsLstorageControllerModeConfigDn_Type()
)
cucsLstorageControllerModeConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerModeConfigDn.setStatus("current")
_CucsLstorageControllerModeConfigRn_Type = SnmpAdminString
_CucsLstorageControllerModeConfigRn_Object = MibTableColumn
cucsLstorageControllerModeConfigRn = _CucsLstorageControllerModeConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 53, 1, 3),
    _CucsLstorageControllerModeConfigRn_Type()
)
cucsLstorageControllerModeConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerModeConfigRn.setStatus("current")
_CucsLstorageControllerModeConfigProtectConfig_Type = TruthValue
_CucsLstorageControllerModeConfigProtectConfig_Object = MibTableColumn
cucsLstorageControllerModeConfigProtectConfig = _CucsLstorageControllerModeConfigProtectConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 53, 1, 4),
    _CucsLstorageControllerModeConfigProtectConfig_Type()
)
cucsLstorageControllerModeConfigProtectConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerModeConfigProtectConfig.setStatus("current")
_CucsLstorageControllerModeConfigRaidMode_Type = CucsStorageLocalDiskMode
_CucsLstorageControllerModeConfigRaidMode_Object = MibTableColumn
cucsLstorageControllerModeConfigRaidMode = _CucsLstorageControllerModeConfigRaidMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 53, 1, 5),
    _CucsLstorageControllerModeConfigRaidMode_Type()
)
cucsLstorageControllerModeConfigRaidMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerModeConfigRaidMode.setStatus("current")
_CucsLstorageControllerQualifierTable_Object = MibTable
cucsLstorageControllerQualifierTable = _CucsLstorageControllerQualifierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 54)
)
if mibBuilder.loadTexts:
    cucsLstorageControllerQualifierTable.setStatus("current")
_CucsLstorageControllerQualifierEntry_Object = MibTableRow
cucsLstorageControllerQualifierEntry = _CucsLstorageControllerQualifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 54, 1)
)
cucsLstorageControllerQualifierEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB", "cucsLstorageControllerQualifierInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLstorageControllerQualifierEntry.setStatus("current")
_CucsLstorageControllerQualifierInstanceId_Type = CucsManagedObjectId
_CucsLstorageControllerQualifierInstanceId_Object = MibTableColumn
cucsLstorageControllerQualifierInstanceId = _CucsLstorageControllerQualifierInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 54, 1, 1),
    _CucsLstorageControllerQualifierInstanceId_Type()
)
cucsLstorageControllerQualifierInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLstorageControllerQualifierInstanceId.setStatus("current")
_CucsLstorageControllerQualifierDn_Type = CucsManagedObjectDn
_CucsLstorageControllerQualifierDn_Object = MibTableColumn
cucsLstorageControllerQualifierDn = _CucsLstorageControllerQualifierDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 54, 1, 2),
    _CucsLstorageControllerQualifierDn_Type()
)
cucsLstorageControllerQualifierDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerQualifierDn.setStatus("current")
_CucsLstorageControllerQualifierRn_Type = SnmpAdminString
_CucsLstorageControllerQualifierRn_Object = MibTableColumn
cucsLstorageControllerQualifierRn = _CucsLstorageControllerQualifierRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 54, 1, 3),
    _CucsLstorageControllerQualifierRn_Type()
)
cucsLstorageControllerQualifierRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerQualifierRn.setStatus("current")
_CucsLstorageControllerQualifierControllerId_Type = CucsStorageControllerId
_CucsLstorageControllerQualifierControllerId_Object = MibTableColumn
cucsLstorageControllerQualifierControllerId = _CucsLstorageControllerQualifierControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 54, 1, 4),
    _CucsLstorageControllerQualifierControllerId_Type()
)
cucsLstorageControllerQualifierControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerQualifierControllerId.setStatus("current")
_CucsLstorageControllerQualifierControllerType_Type = CucsLstorageControllerQualifierControllerType
_CucsLstorageControllerQualifierControllerType_Object = MibTableColumn
cucsLstorageControllerQualifierControllerType = _CucsLstorageControllerQualifierControllerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 79, 54, 1, 5),
    _CucsLstorageControllerQualifierControllerType_Type()
)
cucsLstorageControllerQualifierControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLstorageControllerQualifierControllerType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-LSTORAGE-MIB",
    **{"cucsLstorageObjects": cucsLstorageObjects,
       "cucsLstorageDasScsiLunTable": cucsLstorageDasScsiLunTable,
       "cucsLstorageDasScsiLunEntry": cucsLstorageDasScsiLunEntry,
       "cucsLstorageDasScsiLunInstanceId": cucsLstorageDasScsiLunInstanceId,
       "cucsLstorageDasScsiLunDn": cucsLstorageDasScsiLunDn,
       "cucsLstorageDasScsiLunRn": cucsLstorageDasScsiLunRn,
       "cucsLstorageDasScsiLunAdminState": cucsLstorageDasScsiLunAdminState,
       "cucsLstorageDasScsiLunAutoDeploy": cucsLstorageDasScsiLunAutoDeploy,
       "cucsLstorageDasScsiLunBootDev": cucsLstorageDasScsiLunBootDev,
       "cucsLstorageDasScsiLunConfigQualifier": cucsLstorageDasScsiLunConfigQualifier,
       "cucsLstorageDasScsiLunConfigState": cucsLstorageDasScsiLunConfigState,
       "cucsLstorageDasScsiLunExpandToAvail": cucsLstorageDasScsiLunExpandToAvail,
       "cucsLstorageDasScsiLunLocalDiskPolicyName": cucsLstorageDasScsiLunLocalDiskPolicyName,
       "cucsLstorageDasScsiLunLunDn": cucsLstorageDasScsiLunLunDn,
       "cucsLstorageDasScsiLunLunMapType": cucsLstorageDasScsiLunLunMapType,
       "cucsLstorageDasScsiLunName": cucsLstorageDasScsiLunName,
       "cucsLstorageDasScsiLunOperLocalDiskPolicyName": cucsLstorageDasScsiLunOperLocalDiskPolicyName,
       "cucsLstorageDasScsiLunOperState": cucsLstorageDasScsiLunOperState,
       "cucsLstorageDasScsiLunOrder": cucsLstorageDasScsiLunOrder,
       "cucsLstorageDasScsiLunSize": cucsLstorageDasScsiLunSize,
       "cucsLstorageDasScsiLunStorageClass": cucsLstorageDasScsiLunStorageClass,
       "cucsLstorageDasScsiLunDeferredNaming": cucsLstorageDasScsiLunDeferredNaming,
       "cucsLstorageDiskGroupConfigDefTable": cucsLstorageDiskGroupConfigDefTable,
       "cucsLstorageDiskGroupConfigDefEntry": cucsLstorageDiskGroupConfigDefEntry,
       "cucsLstorageDiskGroupConfigDefInstanceId": cucsLstorageDiskGroupConfigDefInstanceId,
       "cucsLstorageDiskGroupConfigDefDn": cucsLstorageDiskGroupConfigDefDn,
       "cucsLstorageDiskGroupConfigDefRn": cucsLstorageDiskGroupConfigDefRn,
       "cucsLstorageDiskGroupConfigDefDescr": cucsLstorageDiskGroupConfigDefDescr,
       "cucsLstorageDiskGroupConfigDefIntId": cucsLstorageDiskGroupConfigDefIntId,
       "cucsLstorageDiskGroupConfigDefName": cucsLstorageDiskGroupConfigDefName,
       "cucsLstorageDiskGroupConfigDefPolicyLevel": cucsLstorageDiskGroupConfigDefPolicyLevel,
       "cucsLstorageDiskGroupConfigDefPolicyOwner": cucsLstorageDiskGroupConfigDefPolicyOwner,
       "cucsLstorageDiskGroupConfigDefRaidLevel": cucsLstorageDiskGroupConfigDefRaidLevel,
       "cucsLstorageDiskGroupConfigPolicyTable": cucsLstorageDiskGroupConfigPolicyTable,
       "cucsLstorageDiskGroupConfigPolicyEntry": cucsLstorageDiskGroupConfigPolicyEntry,
       "cucsLstorageDiskGroupConfigPolicyInstanceId": cucsLstorageDiskGroupConfigPolicyInstanceId,
       "cucsLstorageDiskGroupConfigPolicyDn": cucsLstorageDiskGroupConfigPolicyDn,
       "cucsLstorageDiskGroupConfigPolicyRn": cucsLstorageDiskGroupConfigPolicyRn,
       "cucsLstorageDiskGroupConfigPolicyDescr": cucsLstorageDiskGroupConfigPolicyDescr,
       "cucsLstorageDiskGroupConfigPolicyIntId": cucsLstorageDiskGroupConfigPolicyIntId,
       "cucsLstorageDiskGroupConfigPolicyName": cucsLstorageDiskGroupConfigPolicyName,
       "cucsLstorageDiskGroupConfigPolicyPolicyLevel": cucsLstorageDiskGroupConfigPolicyPolicyLevel,
       "cucsLstorageDiskGroupConfigPolicyPolicyOwner": cucsLstorageDiskGroupConfigPolicyPolicyOwner,
       "cucsLstorageDiskGroupConfigPolicyRaidLevel": cucsLstorageDiskGroupConfigPolicyRaidLevel,
       "cucsLstorageDiskGroupQualifierTable": cucsLstorageDiskGroupQualifierTable,
       "cucsLstorageDiskGroupQualifierEntry": cucsLstorageDiskGroupQualifierEntry,
       "cucsLstorageDiskGroupQualifierInstanceId": cucsLstorageDiskGroupQualifierInstanceId,
       "cucsLstorageDiskGroupQualifierDn": cucsLstorageDiskGroupQualifierDn,
       "cucsLstorageDiskGroupQualifierRn": cucsLstorageDiskGroupQualifierRn,
       "cucsLstorageDiskGroupQualifierDriveType": cucsLstorageDiskGroupQualifierDriveType,
       "cucsLstorageDiskGroupQualifierMinDriveSize": cucsLstorageDiskGroupQualifierMinDriveSize,
       "cucsLstorageDiskGroupQualifierNumDedHotSpares": cucsLstorageDiskGroupQualifierNumDedHotSpares,
       "cucsLstorageDiskGroupQualifierNumDrives": cucsLstorageDiskGroupQualifierNumDrives,
       "cucsLstorageDiskGroupQualifierNumGlobHotSpares": cucsLstorageDiskGroupQualifierNumGlobHotSpares,
       "cucsLstorageDiskGroupQualifierUseRemainingDisks": cucsLstorageDiskGroupQualifierUseRemainingDisks,
       "cucsLstorageLocalDiskConfigRefTable": cucsLstorageLocalDiskConfigRefTable,
       "cucsLstorageLocalDiskConfigRefEntry": cucsLstorageLocalDiskConfigRefEntry,
       "cucsLstorageLocalDiskConfigRefInstanceId": cucsLstorageLocalDiskConfigRefInstanceId,
       "cucsLstorageLocalDiskConfigRefDn": cucsLstorageLocalDiskConfigRefDn,
       "cucsLstorageLocalDiskConfigRefRn": cucsLstorageLocalDiskConfigRefRn,
       "cucsLstorageLocalDiskConfigRefRole": cucsLstorageLocalDiskConfigRefRole,
       "cucsLstorageLocalDiskConfigRefSlotNum": cucsLstorageLocalDiskConfigRefSlotNum,
       "cucsLstorageLocalDiskConfigRefSpanId": cucsLstorageLocalDiskConfigRefSpanId,
       "cucsLstorageLocalDiskRefTable": cucsLstorageLocalDiskRefTable,
       "cucsLstorageLocalDiskRefEntry": cucsLstorageLocalDiskRefEntry,
       "cucsLstorageLocalDiskRefInstanceId": cucsLstorageLocalDiskRefInstanceId,
       "cucsLstorageLocalDiskRefDn": cucsLstorageLocalDiskRefDn,
       "cucsLstorageLocalDiskRefRn": cucsLstorageLocalDiskRefRn,
       "cucsLstorageLocalDiskRefEnclosureId": cucsLstorageLocalDiskRefEnclosureId,
       "cucsLstorageLocalDiskRefSlotId": cucsLstorageLocalDiskRefSlotId,
       "cucsLstorageProfileTable": cucsLstorageProfileTable,
       "cucsLstorageProfileEntry": cucsLstorageProfileEntry,
       "cucsLstorageProfileInstanceId": cucsLstorageProfileInstanceId,
       "cucsLstorageProfileDn": cucsLstorageProfileDn,
       "cucsLstorageProfileRn": cucsLstorageProfileRn,
       "cucsLstorageProfileAssignedToDn": cucsLstorageProfileAssignedToDn,
       "cucsLstorageProfileAvailability": cucsLstorageProfileAvailability,
       "cucsLstorageProfileDescr": cucsLstorageProfileDescr,
       "cucsLstorageProfileIntId": cucsLstorageProfileIntId,
       "cucsLstorageProfileName": cucsLstorageProfileName,
       "cucsLstorageProfilePolicyLevel": cucsLstorageProfilePolicyLevel,
       "cucsLstorageProfilePolicyOwner": cucsLstorageProfilePolicyOwner,
       "cucsLstorageProfileBindingTable": cucsLstorageProfileBindingTable,
       "cucsLstorageProfileBindingEntry": cucsLstorageProfileBindingEntry,
       "cucsLstorageProfileBindingInstanceId": cucsLstorageProfileBindingInstanceId,
       "cucsLstorageProfileBindingDn": cucsLstorageProfileBindingDn,
       "cucsLstorageProfileBindingRn": cucsLstorageProfileBindingRn,
       "cucsLstorageProfileBindingAssignedToDn": cucsLstorageProfileBindingAssignedToDn,
       "cucsLstorageProfileBindingIssues": cucsLstorageProfileBindingIssues,
       "cucsLstorageProfileBindingName": cucsLstorageProfileBindingName,
       "cucsLstorageProfileBindingOperStorageProfileName": cucsLstorageProfileBindingOperStorageProfileName,
       "cucsLstorageProfileBindingStorageProfileName": cucsLstorageProfileBindingStorageProfileName,
       "cucsLstorageProfileDefTable": cucsLstorageProfileDefTable,
       "cucsLstorageProfileDefEntry": cucsLstorageProfileDefEntry,
       "cucsLstorageProfileDefInstanceId": cucsLstorageProfileDefInstanceId,
       "cucsLstorageProfileDefDn": cucsLstorageProfileDefDn,
       "cucsLstorageProfileDefRn": cucsLstorageProfileDefRn,
       "cucsLstorageProfileDefAssignedToDn": cucsLstorageProfileDefAssignedToDn,
       "cucsLstorageProfileDefAvailability": cucsLstorageProfileDefAvailability,
       "cucsLstorageProfileDefDescr": cucsLstorageProfileDefDescr,
       "cucsLstorageProfileDefIntId": cucsLstorageProfileDefIntId,
       "cucsLstorageProfileDefName": cucsLstorageProfileDefName,
       "cucsLstorageProfileDefPolicyLevel": cucsLstorageProfileDefPolicyLevel,
       "cucsLstorageProfileDefPolicyOwner": cucsLstorageProfileDefPolicyOwner,
       "cucsLstorageVirtualDriveDefTable": cucsLstorageVirtualDriveDefTable,
       "cucsLstorageVirtualDriveDefEntry": cucsLstorageVirtualDriveDefEntry,
       "cucsLstorageVirtualDriveDefInstanceId": cucsLstorageVirtualDriveDefInstanceId,
       "cucsLstorageVirtualDriveDefDn": cucsLstorageVirtualDriveDefDn,
       "cucsLstorageVirtualDriveDefRn": cucsLstorageVirtualDriveDefRn,
       "cucsLstorageVirtualDriveDefAccessPolicy": cucsLstorageVirtualDriveDefAccessPolicy,
       "cucsLstorageVirtualDriveDefDriveCache": cucsLstorageVirtualDriveDefDriveCache,
       "cucsLstorageVirtualDriveDefIoPolicy": cucsLstorageVirtualDriveDefIoPolicy,
       "cucsLstorageVirtualDriveDefReadPolicy": cucsLstorageVirtualDriveDefReadPolicy,
       "cucsLstorageVirtualDriveDefStripSize": cucsLstorageVirtualDriveDefStripSize,
       "cucsLstorageVirtualDriveDefWriteCachePolicy": cucsLstorageVirtualDriveDefWriteCachePolicy,
       "cucsLstorageControllerDefTable": cucsLstorageControllerDefTable,
       "cucsLstorageControllerDefEntry": cucsLstorageControllerDefEntry,
       "cucsLstorageControllerDefInstanceId": cucsLstorageControllerDefInstanceId,
       "cucsLstorageControllerDefDn": cucsLstorageControllerDefDn,
       "cucsLstorageControllerDefRn": cucsLstorageControllerDefRn,
       "cucsLstorageControllerDefAdminState": cucsLstorageControllerDefAdminState,
       "cucsLstorageControllerDefConfigQualifier": cucsLstorageControllerDefConfigQualifier,
       "cucsLstorageControllerDefConfigState": cucsLstorageControllerDefConfigState,
       "cucsLstorageControllerDefName": cucsLstorageControllerDefName,
       "cucsLstorageControllerDefOperState": cucsLstorageControllerDefOperState,
       "cucsLstorageControllerModeConfigTable": cucsLstorageControllerModeConfigTable,
       "cucsLstorageControllerModeConfigEntry": cucsLstorageControllerModeConfigEntry,
       "cucsLstorageControllerModeConfigInstanceId": cucsLstorageControllerModeConfigInstanceId,
       "cucsLstorageControllerModeConfigDn": cucsLstorageControllerModeConfigDn,
       "cucsLstorageControllerModeConfigRn": cucsLstorageControllerModeConfigRn,
       "cucsLstorageControllerModeConfigProtectConfig": cucsLstorageControllerModeConfigProtectConfig,
       "cucsLstorageControllerModeConfigRaidMode": cucsLstorageControllerModeConfigRaidMode,
       "cucsLstorageControllerQualifierTable": cucsLstorageControllerQualifierTable,
       "cucsLstorageControllerQualifierEntry": cucsLstorageControllerQualifierEntry,
       "cucsLstorageControllerQualifierInstanceId": cucsLstorageControllerQualifierInstanceId,
       "cucsLstorageControllerQualifierDn": cucsLstorageControllerQualifierDn,
       "cucsLstorageControllerQualifierRn": cucsLstorageControllerQualifierRn,
       "cucsLstorageControllerQualifierControllerId": cucsLstorageControllerQualifierControllerId,
       "cucsLstorageControllerQualifierControllerType": cucsLstorageControllerQualifierControllerType}
)
