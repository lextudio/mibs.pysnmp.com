# SNMP MIB module (CISCO-UNIFIED-COMPUTING-LSBOOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-LSBOOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:52 2024
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

(CucsLsbootADefBootMode,
 CucsLsbootAccessType,
 CucsLsbootDefaultLocalImageType,
 CucsLsbootEmbeddedLocalDiskImagePathType,
 CucsLsbootEmbeddedLocalDiskImageType,
 CucsLsbootEmbeddedLocalLunImageType,
 CucsLsbootIScsiAccess,
 CucsLsbootIScsiImagePathType,
 CucsLsbootIScsiType,
 CucsLsbootLanAccess,
 CucsLsbootLanBootProt,
 CucsLsbootLanImagePathType,
 CucsLsbootLanType,
 CucsLsbootLocalDiskImagePathType,
 CucsLsbootLocalDiskImageType,
 CucsLsbootLocalHddImageType,
 CucsLsbootLocalLunImagePathType,
 CucsLsbootPurpose,
 CucsLsbootSanAccess,
 CucsLsbootSanCatSanImagePathType,
 CucsLsbootSanCatSanImageType,
 CucsLsbootSanImagePathType,
 CucsLsbootSanImageType,
 CucsLsbootSanType,
 CucsLsbootStorageAccess,
 CucsLsbootStorageType,
 CucsLsbootUsbExternalImageType,
 CucsLsbootUsbFlashStorageImageType,
 CucsLsbootUsbInternalImageType,
 CucsLsbootVirtualMediaType,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsLsbootADefBootMode",
    "CucsLsbootAccessType",
    "CucsLsbootDefaultLocalImageType",
    "CucsLsbootEmbeddedLocalDiskImagePathType",
    "CucsLsbootEmbeddedLocalDiskImageType",
    "CucsLsbootEmbeddedLocalLunImageType",
    "CucsLsbootIScsiAccess",
    "CucsLsbootIScsiImagePathType",
    "CucsLsbootIScsiType",
    "CucsLsbootLanAccess",
    "CucsLsbootLanBootProt",
    "CucsLsbootLanImagePathType",
    "CucsLsbootLanType",
    "CucsLsbootLocalDiskImagePathType",
    "CucsLsbootLocalDiskImageType",
    "CucsLsbootLocalHddImageType",
    "CucsLsbootLocalLunImagePathType",
    "CucsLsbootPurpose",
    "CucsLsbootSanAccess",
    "CucsLsbootSanCatSanImagePathType",
    "CucsLsbootSanCatSanImageType",
    "CucsLsbootSanImagePathType",
    "CucsLsbootSanImageType",
    "CucsLsbootSanType",
    "CucsLsbootStorageAccess",
    "CucsLsbootStorageType",
    "CucsLsbootUsbExternalImageType",
    "CucsLsbootUsbFlashStorageImageType",
    "CucsLsbootUsbInternalImageType",
    "CucsLsbootVirtualMediaType",
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

cucsLsbootObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsLsbootDefTable_Object = MibTable
cucsLsbootDefTable = _CucsLsbootDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1)
)
if mibBuilder.loadTexts:
    cucsLsbootDefTable.setStatus("current")
_CucsLsbootDefEntry_Object = MibTableRow
cucsLsbootDefEntry = _CucsLsbootDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1, 1)
)
cucsLsbootDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootDefEntry.setStatus("current")
_CucsLsbootDefInstanceId_Type = CucsManagedObjectId
_CucsLsbootDefInstanceId_Object = MibTableColumn
cucsLsbootDefInstanceId = _CucsLsbootDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1, 1, 1),
    _CucsLsbootDefInstanceId_Type()
)
cucsLsbootDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootDefInstanceId.setStatus("current")
_CucsLsbootDefDn_Type = CucsManagedObjectDn
_CucsLsbootDefDn_Object = MibTableColumn
cucsLsbootDefDn = _CucsLsbootDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1, 1, 2),
    _CucsLsbootDefDn_Type()
)
cucsLsbootDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefDn.setStatus("current")
_CucsLsbootDefRn_Type = SnmpAdminString
_CucsLsbootDefRn_Object = MibTableColumn
cucsLsbootDefRn = _CucsLsbootDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1, 1, 3),
    _CucsLsbootDefRn_Type()
)
cucsLsbootDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefRn.setStatus("current")
_CucsLsbootDefDescr_Type = SnmpAdminString
_CucsLsbootDefDescr_Object = MibTableColumn
cucsLsbootDefDescr = _CucsLsbootDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1, 1, 4),
    _CucsLsbootDefDescr_Type()
)
cucsLsbootDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefDescr.setStatus("current")
_CucsLsbootDefEnforceVnicName_Type = TruthValue
_CucsLsbootDefEnforceVnicName_Object = MibTableColumn
cucsLsbootDefEnforceVnicName = _CucsLsbootDefEnforceVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1, 1, 5),
    _CucsLsbootDefEnforceVnicName_Type()
)
cucsLsbootDefEnforceVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefEnforceVnicName.setStatus("current")
_CucsLsbootDefIntId_Type = SnmpAdminString
_CucsLsbootDefIntId_Object = MibTableColumn
cucsLsbootDefIntId = _CucsLsbootDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1, 1, 6),
    _CucsLsbootDefIntId_Type()
)
cucsLsbootDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefIntId.setStatus("current")
_CucsLsbootDefName_Type = SnmpAdminString
_CucsLsbootDefName_Object = MibTableColumn
cucsLsbootDefName = _CucsLsbootDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1, 1, 7),
    _CucsLsbootDefName_Type()
)
cucsLsbootDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefName.setStatus("current")
_CucsLsbootDefPurpose_Type = CucsLsbootPurpose
_CucsLsbootDefPurpose_Object = MibTableColumn
cucsLsbootDefPurpose = _CucsLsbootDefPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1, 1, 8),
    _CucsLsbootDefPurpose_Type()
)
cucsLsbootDefPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefPurpose.setStatus("current")
_CucsLsbootDefRebootOnUpdate_Type = TruthValue
_CucsLsbootDefRebootOnUpdate_Object = MibTableColumn
cucsLsbootDefRebootOnUpdate = _CucsLsbootDefRebootOnUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1, 1, 9),
    _CucsLsbootDefRebootOnUpdate_Type()
)
cucsLsbootDefRebootOnUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefRebootOnUpdate.setStatus("current")
_CucsLsbootDefPolicyLevel_Type = Gauge32
_CucsLsbootDefPolicyLevel_Object = MibTableColumn
cucsLsbootDefPolicyLevel = _CucsLsbootDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1, 1, 10),
    _CucsLsbootDefPolicyLevel_Type()
)
cucsLsbootDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefPolicyLevel.setStatus("current")
_CucsLsbootDefPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsLsbootDefPolicyOwner_Object = MibTableColumn
cucsLsbootDefPolicyOwner = _CucsLsbootDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1, 1, 11),
    _CucsLsbootDefPolicyOwner_Type()
)
cucsLsbootDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefPolicyOwner.setStatus("current")
_CucsLsbootDefAdvBootOrderApplicable_Type = TruthValue
_CucsLsbootDefAdvBootOrderApplicable_Object = MibTableColumn
cucsLsbootDefAdvBootOrderApplicable = _CucsLsbootDefAdvBootOrderApplicable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1, 1, 12),
    _CucsLsbootDefAdvBootOrderApplicable_Type()
)
cucsLsbootDefAdvBootOrderApplicable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefAdvBootOrderApplicable.setStatus("current")
_CucsLsbootDefBootMode_Type = CucsLsbootADefBootMode
_CucsLsbootDefBootMode_Object = MibTableColumn
cucsLsbootDefBootMode = _CucsLsbootDefBootMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 1, 1, 13),
    _CucsLsbootDefBootMode_Type()
)
cucsLsbootDefBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefBootMode.setStatus("current")
_CucsLsbootLanTable_Object = MibTable
cucsLsbootLanTable = _CucsLsbootLanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 2)
)
if mibBuilder.loadTexts:
    cucsLsbootLanTable.setStatus("current")
_CucsLsbootLanEntry_Object = MibTableRow
cucsLsbootLanEntry = _CucsLsbootLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 2, 1)
)
cucsLsbootLanEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootLanInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootLanEntry.setStatus("current")
_CucsLsbootLanInstanceId_Type = CucsManagedObjectId
_CucsLsbootLanInstanceId_Object = MibTableColumn
cucsLsbootLanInstanceId = _CucsLsbootLanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 2, 1, 1),
    _CucsLsbootLanInstanceId_Type()
)
cucsLsbootLanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootLanInstanceId.setStatus("current")
_CucsLsbootLanDn_Type = CucsManagedObjectDn
_CucsLsbootLanDn_Object = MibTableColumn
cucsLsbootLanDn = _CucsLsbootLanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 2, 1, 2),
    _CucsLsbootLanDn_Type()
)
cucsLsbootLanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanDn.setStatus("current")
_CucsLsbootLanRn_Type = SnmpAdminString
_CucsLsbootLanRn_Object = MibTableColumn
cucsLsbootLanRn = _CucsLsbootLanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 2, 1, 3),
    _CucsLsbootLanRn_Type()
)
cucsLsbootLanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanRn.setStatus("current")
_CucsLsbootLanAccess_Type = CucsLsbootLanAccess
_CucsLsbootLanAccess_Object = MibTableColumn
cucsLsbootLanAccess = _CucsLsbootLanAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 2, 1, 4),
    _CucsLsbootLanAccess_Type()
)
cucsLsbootLanAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanAccess.setStatus("current")
_CucsLsbootLanOrder_Type = Gauge32
_CucsLsbootLanOrder_Object = MibTableColumn
cucsLsbootLanOrder = _CucsLsbootLanOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 2, 1, 5),
    _CucsLsbootLanOrder_Type()
)
cucsLsbootLanOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanOrder.setStatus("current")
_CucsLsbootLanType_Type = CucsLsbootLanType
_CucsLsbootLanType_Object = MibTableColumn
cucsLsbootLanType = _CucsLsbootLanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 2, 1, 6),
    _CucsLsbootLanType_Type()
)
cucsLsbootLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanType.setStatus("current")
_CucsLsbootLanProt_Type = CucsLsbootLanBootProt
_CucsLsbootLanProt_Object = MibTableColumn
cucsLsbootLanProt = _CucsLsbootLanProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 2, 1, 7),
    _CucsLsbootLanProt_Type()
)
cucsLsbootLanProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanProt.setStatus("current")
_CucsLsbootLanImagePathTable_Object = MibTable
cucsLsbootLanImagePathTable = _CucsLsbootLanImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 3)
)
if mibBuilder.loadTexts:
    cucsLsbootLanImagePathTable.setStatus("current")
_CucsLsbootLanImagePathEntry_Object = MibTableRow
cucsLsbootLanImagePathEntry = _CucsLsbootLanImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 3, 1)
)
cucsLsbootLanImagePathEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootLanImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootLanImagePathEntry.setStatus("current")
_CucsLsbootLanImagePathInstanceId_Type = CucsManagedObjectId
_CucsLsbootLanImagePathInstanceId_Object = MibTableColumn
cucsLsbootLanImagePathInstanceId = _CucsLsbootLanImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 3, 1, 1),
    _CucsLsbootLanImagePathInstanceId_Type()
)
cucsLsbootLanImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootLanImagePathInstanceId.setStatus("current")
_CucsLsbootLanImagePathDn_Type = CucsManagedObjectDn
_CucsLsbootLanImagePathDn_Object = MibTableColumn
cucsLsbootLanImagePathDn = _CucsLsbootLanImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 3, 1, 2),
    _CucsLsbootLanImagePathDn_Type()
)
cucsLsbootLanImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanImagePathDn.setStatus("current")
_CucsLsbootLanImagePathRn_Type = SnmpAdminString
_CucsLsbootLanImagePathRn_Object = MibTableColumn
cucsLsbootLanImagePathRn = _CucsLsbootLanImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 3, 1, 3),
    _CucsLsbootLanImagePathRn_Type()
)
cucsLsbootLanImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanImagePathRn.setStatus("current")
_CucsLsbootLanImagePathType_Type = CucsLsbootLanImagePathType
_CucsLsbootLanImagePathType_Object = MibTableColumn
cucsLsbootLanImagePathType = _CucsLsbootLanImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 3, 1, 4),
    _CucsLsbootLanImagePathType_Type()
)
cucsLsbootLanImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanImagePathType.setStatus("current")
_CucsLsbootLanImagePathVnicName_Type = SnmpAdminString
_CucsLsbootLanImagePathVnicName_Object = MibTableColumn
cucsLsbootLanImagePathVnicName = _CucsLsbootLanImagePathVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 3, 1, 5),
    _CucsLsbootLanImagePathVnicName_Type()
)
cucsLsbootLanImagePathVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanImagePathVnicName.setStatus("current")
_CucsLsbootLanImagePathImgPolicyName_Type = SnmpAdminString
_CucsLsbootLanImagePathImgPolicyName_Object = MibTableColumn
cucsLsbootLanImagePathImgPolicyName = _CucsLsbootLanImagePathImgPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 3, 1, 6),
    _CucsLsbootLanImagePathImgPolicyName_Type()
)
cucsLsbootLanImagePathImgPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanImagePathImgPolicyName.setStatus("current")
_CucsLsbootLanImagePathImgSecPolicyName_Type = SnmpAdminString
_CucsLsbootLanImagePathImgSecPolicyName_Object = MibTableColumn
cucsLsbootLanImagePathImgSecPolicyName = _CucsLsbootLanImagePathImgSecPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 3, 1, 7),
    _CucsLsbootLanImagePathImgSecPolicyName_Type()
)
cucsLsbootLanImagePathImgSecPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanImagePathImgSecPolicyName.setStatus("current")
_CucsLsbootLanImagePathBootIpPolicyName_Type = SnmpAdminString
_CucsLsbootLanImagePathBootIpPolicyName_Object = MibTableColumn
cucsLsbootLanImagePathBootIpPolicyName = _CucsLsbootLanImagePathBootIpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 3, 1, 8),
    _CucsLsbootLanImagePathBootIpPolicyName_Type()
)
cucsLsbootLanImagePathBootIpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanImagePathBootIpPolicyName.setStatus("current")
_CucsLsbootLanImagePathProvSrvPolicyName_Type = SnmpAdminString
_CucsLsbootLanImagePathProvSrvPolicyName_Object = MibTableColumn
cucsLsbootLanImagePathProvSrvPolicyName = _CucsLsbootLanImagePathProvSrvPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 3, 1, 9),
    _CucsLsbootLanImagePathProvSrvPolicyName_Type()
)
cucsLsbootLanImagePathProvSrvPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanImagePathProvSrvPolicyName.setStatus("current")
_CucsLsbootLanImagePathISCSIVnicName_Type = SnmpAdminString
_CucsLsbootLanImagePathISCSIVnicName_Object = MibTableColumn
cucsLsbootLanImagePathISCSIVnicName = _CucsLsbootLanImagePathISCSIVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 3, 1, 10),
    _CucsLsbootLanImagePathISCSIVnicName_Type()
)
cucsLsbootLanImagePathISCSIVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLanImagePathISCSIVnicName.setStatus("current")
_CucsLsbootLocalStorageTable_Object = MibTable
cucsLsbootLocalStorageTable = _CucsLsbootLocalStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 4)
)
if mibBuilder.loadTexts:
    cucsLsbootLocalStorageTable.setStatus("current")
_CucsLsbootLocalStorageEntry_Object = MibTableRow
cucsLsbootLocalStorageEntry = _CucsLsbootLocalStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 4, 1)
)
cucsLsbootLocalStorageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootLocalStorageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootLocalStorageEntry.setStatus("current")
_CucsLsbootLocalStorageInstanceId_Type = CucsManagedObjectId
_CucsLsbootLocalStorageInstanceId_Object = MibTableColumn
cucsLsbootLocalStorageInstanceId = _CucsLsbootLocalStorageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 4, 1, 1),
    _CucsLsbootLocalStorageInstanceId_Type()
)
cucsLsbootLocalStorageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootLocalStorageInstanceId.setStatus("current")
_CucsLsbootLocalStorageDn_Type = CucsManagedObjectDn
_CucsLsbootLocalStorageDn_Object = MibTableColumn
cucsLsbootLocalStorageDn = _CucsLsbootLocalStorageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 4, 1, 2),
    _CucsLsbootLocalStorageDn_Type()
)
cucsLsbootLocalStorageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalStorageDn.setStatus("current")
_CucsLsbootLocalStorageRn_Type = SnmpAdminString
_CucsLsbootLocalStorageRn_Object = MibTableColumn
cucsLsbootLocalStorageRn = _CucsLsbootLocalStorageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 4, 1, 3),
    _CucsLsbootLocalStorageRn_Type()
)
cucsLsbootLocalStorageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalStorageRn.setStatus("current")
_CucsLsbootLocalStoragePropAcl_Type = Unsigned64
_CucsLsbootLocalStoragePropAcl_Object = MibTableColumn
cucsLsbootLocalStoragePropAcl = _CucsLsbootLocalStoragePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 4, 1, 4),
    _CucsLsbootLocalStoragePropAcl_Type()
)
cucsLsbootLocalStoragePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalStoragePropAcl.setStatus("current")
_CucsLsbootPolicyTable_Object = MibTable
cucsLsbootPolicyTable = _CucsLsbootPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5)
)
if mibBuilder.loadTexts:
    cucsLsbootPolicyTable.setStatus("current")
_CucsLsbootPolicyEntry_Object = MibTableRow
cucsLsbootPolicyEntry = _CucsLsbootPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5, 1)
)
cucsLsbootPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootPolicyEntry.setStatus("current")
_CucsLsbootPolicyInstanceId_Type = CucsManagedObjectId
_CucsLsbootPolicyInstanceId_Object = MibTableColumn
cucsLsbootPolicyInstanceId = _CucsLsbootPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5, 1, 1),
    _CucsLsbootPolicyInstanceId_Type()
)
cucsLsbootPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootPolicyInstanceId.setStatus("current")
_CucsLsbootPolicyDn_Type = CucsManagedObjectDn
_CucsLsbootPolicyDn_Object = MibTableColumn
cucsLsbootPolicyDn = _CucsLsbootPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5, 1, 2),
    _CucsLsbootPolicyDn_Type()
)
cucsLsbootPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootPolicyDn.setStatus("current")
_CucsLsbootPolicyRn_Type = SnmpAdminString
_CucsLsbootPolicyRn_Object = MibTableColumn
cucsLsbootPolicyRn = _CucsLsbootPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5, 1, 3),
    _CucsLsbootPolicyRn_Type()
)
cucsLsbootPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootPolicyRn.setStatus("current")
_CucsLsbootPolicyDescr_Type = SnmpAdminString
_CucsLsbootPolicyDescr_Object = MibTableColumn
cucsLsbootPolicyDescr = _CucsLsbootPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5, 1, 4),
    _CucsLsbootPolicyDescr_Type()
)
cucsLsbootPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootPolicyDescr.setStatus("current")
_CucsLsbootPolicyEnforceVnicName_Type = TruthValue
_CucsLsbootPolicyEnforceVnicName_Object = MibTableColumn
cucsLsbootPolicyEnforceVnicName = _CucsLsbootPolicyEnforceVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5, 1, 5),
    _CucsLsbootPolicyEnforceVnicName_Type()
)
cucsLsbootPolicyEnforceVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootPolicyEnforceVnicName.setStatus("current")
_CucsLsbootPolicyIntId_Type = SnmpAdminString
_CucsLsbootPolicyIntId_Object = MibTableColumn
cucsLsbootPolicyIntId = _CucsLsbootPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5, 1, 6),
    _CucsLsbootPolicyIntId_Type()
)
cucsLsbootPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootPolicyIntId.setStatus("current")
_CucsLsbootPolicyName_Type = SnmpAdminString
_CucsLsbootPolicyName_Object = MibTableColumn
cucsLsbootPolicyName = _CucsLsbootPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5, 1, 7),
    _CucsLsbootPolicyName_Type()
)
cucsLsbootPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootPolicyName.setStatus("current")
_CucsLsbootPolicyPurpose_Type = CucsLsbootPurpose
_CucsLsbootPolicyPurpose_Object = MibTableColumn
cucsLsbootPolicyPurpose = _CucsLsbootPolicyPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5, 1, 8),
    _CucsLsbootPolicyPurpose_Type()
)
cucsLsbootPolicyPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootPolicyPurpose.setStatus("current")
_CucsLsbootPolicyRebootOnUpdate_Type = TruthValue
_CucsLsbootPolicyRebootOnUpdate_Object = MibTableColumn
cucsLsbootPolicyRebootOnUpdate = _CucsLsbootPolicyRebootOnUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5, 1, 9),
    _CucsLsbootPolicyRebootOnUpdate_Type()
)
cucsLsbootPolicyRebootOnUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootPolicyRebootOnUpdate.setStatus("current")
_CucsLsbootPolicyPolicyLevel_Type = Gauge32
_CucsLsbootPolicyPolicyLevel_Object = MibTableColumn
cucsLsbootPolicyPolicyLevel = _CucsLsbootPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5, 1, 10),
    _CucsLsbootPolicyPolicyLevel_Type()
)
cucsLsbootPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootPolicyPolicyLevel.setStatus("current")
_CucsLsbootPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsLsbootPolicyPolicyOwner_Object = MibTableColumn
cucsLsbootPolicyPolicyOwner = _CucsLsbootPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5, 1, 11),
    _CucsLsbootPolicyPolicyOwner_Type()
)
cucsLsbootPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootPolicyPolicyOwner.setStatus("current")
_CucsLsbootPolicyBootMode_Type = CucsLsbootADefBootMode
_CucsLsbootPolicyBootMode_Object = MibTableColumn
cucsLsbootPolicyBootMode = _CucsLsbootPolicyBootMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5, 1, 12),
    _CucsLsbootPolicyBootMode_Type()
)
cucsLsbootPolicyBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootPolicyBootMode.setStatus("current")
_CucsLsbootPolicyPropAcl_Type = Unsigned64
_CucsLsbootPolicyPropAcl_Object = MibTableColumn
cucsLsbootPolicyPropAcl = _CucsLsbootPolicyPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 5, 1, 13),
    _CucsLsbootPolicyPropAcl_Type()
)
cucsLsbootPolicyPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootPolicyPropAcl.setStatus("current")
_CucsLsbootSanImageTable_Object = MibTable
cucsLsbootSanImageTable = _CucsLsbootSanImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 6)
)
if mibBuilder.loadTexts:
    cucsLsbootSanImageTable.setStatus("current")
_CucsLsbootSanImageEntry_Object = MibTableRow
cucsLsbootSanImageEntry = _CucsLsbootSanImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 6, 1)
)
cucsLsbootSanImageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootSanImageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootSanImageEntry.setStatus("current")
_CucsLsbootSanImageInstanceId_Type = CucsManagedObjectId
_CucsLsbootSanImageInstanceId_Object = MibTableColumn
cucsLsbootSanImageInstanceId = _CucsLsbootSanImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 6, 1, 1),
    _CucsLsbootSanImageInstanceId_Type()
)
cucsLsbootSanImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootSanImageInstanceId.setStatus("current")
_CucsLsbootSanImageDn_Type = CucsManagedObjectDn
_CucsLsbootSanImageDn_Object = MibTableColumn
cucsLsbootSanImageDn = _CucsLsbootSanImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 6, 1, 2),
    _CucsLsbootSanImageDn_Type()
)
cucsLsbootSanImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanImageDn.setStatus("current")
_CucsLsbootSanImageRn_Type = SnmpAdminString
_CucsLsbootSanImageRn_Object = MibTableColumn
cucsLsbootSanImageRn = _CucsLsbootSanImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 6, 1, 3),
    _CucsLsbootSanImageRn_Type()
)
cucsLsbootSanImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanImageRn.setStatus("current")
_CucsLsbootSanImageType_Type = CucsLsbootSanImageType
_CucsLsbootSanImageType_Object = MibTableColumn
cucsLsbootSanImageType = _CucsLsbootSanImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 6, 1, 4),
    _CucsLsbootSanImageType_Type()
)
cucsLsbootSanImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanImageType.setStatus("current")
_CucsLsbootSanImageVnicName_Type = SnmpAdminString
_CucsLsbootSanImageVnicName_Object = MibTableColumn
cucsLsbootSanImageVnicName = _CucsLsbootSanImageVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 6, 1, 5),
    _CucsLsbootSanImageVnicName_Type()
)
cucsLsbootSanImageVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanImageVnicName.setStatus("current")
_CucsLsbootSanImagePathTable_Object = MibTable
cucsLsbootSanImagePathTable = _CucsLsbootSanImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 7)
)
if mibBuilder.loadTexts:
    cucsLsbootSanImagePathTable.setStatus("current")
_CucsLsbootSanImagePathEntry_Object = MibTableRow
cucsLsbootSanImagePathEntry = _CucsLsbootSanImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 7, 1)
)
cucsLsbootSanImagePathEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootSanImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootSanImagePathEntry.setStatus("current")
_CucsLsbootSanImagePathInstanceId_Type = CucsManagedObjectId
_CucsLsbootSanImagePathInstanceId_Object = MibTableColumn
cucsLsbootSanImagePathInstanceId = _CucsLsbootSanImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 7, 1, 1),
    _CucsLsbootSanImagePathInstanceId_Type()
)
cucsLsbootSanImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootSanImagePathInstanceId.setStatus("current")
_CucsLsbootSanImagePathDn_Type = CucsManagedObjectDn
_CucsLsbootSanImagePathDn_Object = MibTableColumn
cucsLsbootSanImagePathDn = _CucsLsbootSanImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 7, 1, 2),
    _CucsLsbootSanImagePathDn_Type()
)
cucsLsbootSanImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanImagePathDn.setStatus("current")
_CucsLsbootSanImagePathRn_Type = SnmpAdminString
_CucsLsbootSanImagePathRn_Object = MibTableColumn
cucsLsbootSanImagePathRn = _CucsLsbootSanImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 7, 1, 3),
    _CucsLsbootSanImagePathRn_Type()
)
cucsLsbootSanImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanImagePathRn.setStatus("current")
_CucsLsbootSanImagePathLun_Type = SnmpAdminString
_CucsLsbootSanImagePathLun_Object = MibTableColumn
cucsLsbootSanImagePathLun = _CucsLsbootSanImagePathLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 7, 1, 4),
    _CucsLsbootSanImagePathLun_Type()
)
cucsLsbootSanImagePathLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanImagePathLun.setStatus("current")
_CucsLsbootSanImagePathType_Type = CucsLsbootSanImagePathType
_CucsLsbootSanImagePathType_Object = MibTableColumn
cucsLsbootSanImagePathType = _CucsLsbootSanImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 7, 1, 5),
    _CucsLsbootSanImagePathType_Type()
)
cucsLsbootSanImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanImagePathType.setStatus("current")
_CucsLsbootSanImagePathVnicName_Type = SnmpAdminString
_CucsLsbootSanImagePathVnicName_Object = MibTableColumn
cucsLsbootSanImagePathVnicName = _CucsLsbootSanImagePathVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 7, 1, 6),
    _CucsLsbootSanImagePathVnicName_Type()
)
cucsLsbootSanImagePathVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanImagePathVnicName.setStatus("current")
_CucsLsbootSanImagePathWwn_Type = Unsigned64
_CucsLsbootSanImagePathWwn_Object = MibTableColumn
cucsLsbootSanImagePathWwn = _CucsLsbootSanImagePathWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 7, 1, 7),
    _CucsLsbootSanImagePathWwn_Type()
)
cucsLsbootSanImagePathWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanImagePathWwn.setStatus("current")
_CucsLsbootStorageTable_Object = MibTable
cucsLsbootStorageTable = _CucsLsbootStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 8)
)
if mibBuilder.loadTexts:
    cucsLsbootStorageTable.setStatus("current")
_CucsLsbootStorageEntry_Object = MibTableRow
cucsLsbootStorageEntry = _CucsLsbootStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 8, 1)
)
cucsLsbootStorageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootStorageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootStorageEntry.setStatus("current")
_CucsLsbootStorageInstanceId_Type = CucsManagedObjectId
_CucsLsbootStorageInstanceId_Object = MibTableColumn
cucsLsbootStorageInstanceId = _CucsLsbootStorageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 8, 1, 1),
    _CucsLsbootStorageInstanceId_Type()
)
cucsLsbootStorageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootStorageInstanceId.setStatus("current")
_CucsLsbootStorageDn_Type = CucsManagedObjectDn
_CucsLsbootStorageDn_Object = MibTableColumn
cucsLsbootStorageDn = _CucsLsbootStorageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 8, 1, 2),
    _CucsLsbootStorageDn_Type()
)
cucsLsbootStorageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootStorageDn.setStatus("current")
_CucsLsbootStorageRn_Type = SnmpAdminString
_CucsLsbootStorageRn_Object = MibTableColumn
cucsLsbootStorageRn = _CucsLsbootStorageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 8, 1, 3),
    _CucsLsbootStorageRn_Type()
)
cucsLsbootStorageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootStorageRn.setStatus("current")
_CucsLsbootStorageAccess_Type = CucsLsbootStorageAccess
_CucsLsbootStorageAccess_Object = MibTableColumn
cucsLsbootStorageAccess = _CucsLsbootStorageAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 8, 1, 4),
    _CucsLsbootStorageAccess_Type()
)
cucsLsbootStorageAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootStorageAccess.setStatus("current")
_CucsLsbootStorageOrder_Type = Gauge32
_CucsLsbootStorageOrder_Object = MibTableColumn
cucsLsbootStorageOrder = _CucsLsbootStorageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 8, 1, 5),
    _CucsLsbootStorageOrder_Type()
)
cucsLsbootStorageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootStorageOrder.setStatus("current")
_CucsLsbootStorageType_Type = CucsLsbootStorageType
_CucsLsbootStorageType_Object = MibTableColumn
cucsLsbootStorageType = _CucsLsbootStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 8, 1, 6),
    _CucsLsbootStorageType_Type()
)
cucsLsbootStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootStorageType.setStatus("current")
_CucsLsbootStoragePropAcl_Type = Unsigned64
_CucsLsbootStoragePropAcl_Object = MibTableColumn
cucsLsbootStoragePropAcl = _CucsLsbootStoragePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 8, 1, 7),
    _CucsLsbootStoragePropAcl_Type()
)
cucsLsbootStoragePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootStoragePropAcl.setStatus("current")
_CucsLsbootVirtualMediaTable_Object = MibTable
cucsLsbootVirtualMediaTable = _CucsLsbootVirtualMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 9)
)
if mibBuilder.loadTexts:
    cucsLsbootVirtualMediaTable.setStatus("current")
_CucsLsbootVirtualMediaEntry_Object = MibTableRow
cucsLsbootVirtualMediaEntry = _CucsLsbootVirtualMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 9, 1)
)
cucsLsbootVirtualMediaEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootVirtualMediaInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootVirtualMediaEntry.setStatus("current")
_CucsLsbootVirtualMediaInstanceId_Type = CucsManagedObjectId
_CucsLsbootVirtualMediaInstanceId_Object = MibTableColumn
cucsLsbootVirtualMediaInstanceId = _CucsLsbootVirtualMediaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 9, 1, 1),
    _CucsLsbootVirtualMediaInstanceId_Type()
)
cucsLsbootVirtualMediaInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootVirtualMediaInstanceId.setStatus("current")
_CucsLsbootVirtualMediaDn_Type = CucsManagedObjectDn
_CucsLsbootVirtualMediaDn_Object = MibTableColumn
cucsLsbootVirtualMediaDn = _CucsLsbootVirtualMediaDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 9, 1, 2),
    _CucsLsbootVirtualMediaDn_Type()
)
cucsLsbootVirtualMediaDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootVirtualMediaDn.setStatus("current")
_CucsLsbootVirtualMediaRn_Type = SnmpAdminString
_CucsLsbootVirtualMediaRn_Object = MibTableColumn
cucsLsbootVirtualMediaRn = _CucsLsbootVirtualMediaRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 9, 1, 3),
    _CucsLsbootVirtualMediaRn_Type()
)
cucsLsbootVirtualMediaRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootVirtualMediaRn.setStatus("current")
_CucsLsbootVirtualMediaAccess_Type = CucsLsbootAccessType
_CucsLsbootVirtualMediaAccess_Object = MibTableColumn
cucsLsbootVirtualMediaAccess = _CucsLsbootVirtualMediaAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 9, 1, 4),
    _CucsLsbootVirtualMediaAccess_Type()
)
cucsLsbootVirtualMediaAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootVirtualMediaAccess.setStatus("current")
_CucsLsbootVirtualMediaOrder_Type = Gauge32
_CucsLsbootVirtualMediaOrder_Object = MibTableColumn
cucsLsbootVirtualMediaOrder = _CucsLsbootVirtualMediaOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 9, 1, 5),
    _CucsLsbootVirtualMediaOrder_Type()
)
cucsLsbootVirtualMediaOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootVirtualMediaOrder.setStatus("current")
_CucsLsbootVirtualMediaType_Type = CucsLsbootVirtualMediaType
_CucsLsbootVirtualMediaType_Object = MibTableColumn
cucsLsbootVirtualMediaType = _CucsLsbootVirtualMediaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 9, 1, 6),
    _CucsLsbootVirtualMediaType_Type()
)
cucsLsbootVirtualMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootVirtualMediaType.setStatus("current")
_CucsLsbootVirtualMediaLunId_Type = SnmpAdminString
_CucsLsbootVirtualMediaLunId_Object = MibTableColumn
cucsLsbootVirtualMediaLunId = _CucsLsbootVirtualMediaLunId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 9, 1, 7),
    _CucsLsbootVirtualMediaLunId_Type()
)
cucsLsbootVirtualMediaLunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootVirtualMediaLunId.setStatus("current")
_CucsLsbootVirtualMediaMappingName_Type = SnmpAdminString
_CucsLsbootVirtualMediaMappingName_Object = MibTableColumn
cucsLsbootVirtualMediaMappingName = _CucsLsbootVirtualMediaMappingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 9, 1, 8),
    _CucsLsbootVirtualMediaMappingName_Type()
)
cucsLsbootVirtualMediaMappingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootVirtualMediaMappingName.setStatus("current")
_CucsLsbootVirtualMediaPropAcl_Type = Unsigned64
_CucsLsbootVirtualMediaPropAcl_Object = MibTableColumn
cucsLsbootVirtualMediaPropAcl = _CucsLsbootVirtualMediaPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 9, 1, 9),
    _CucsLsbootVirtualMediaPropAcl_Type()
)
cucsLsbootVirtualMediaPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootVirtualMediaPropAcl.setStatus("current")
_CucsLsbootIScsiTable_Object = MibTable
cucsLsbootIScsiTable = _CucsLsbootIScsiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 10)
)
if mibBuilder.loadTexts:
    cucsLsbootIScsiTable.setStatus("current")
_CucsLsbootIScsiEntry_Object = MibTableRow
cucsLsbootIScsiEntry = _CucsLsbootIScsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 10, 1)
)
cucsLsbootIScsiEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootIScsiInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootIScsiEntry.setStatus("current")
_CucsLsbootIScsiInstanceId_Type = CucsManagedObjectId
_CucsLsbootIScsiInstanceId_Object = MibTableColumn
cucsLsbootIScsiInstanceId = _CucsLsbootIScsiInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 10, 1, 1),
    _CucsLsbootIScsiInstanceId_Type()
)
cucsLsbootIScsiInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootIScsiInstanceId.setStatus("current")
_CucsLsbootIScsiDn_Type = CucsManagedObjectDn
_CucsLsbootIScsiDn_Object = MibTableColumn
cucsLsbootIScsiDn = _CucsLsbootIScsiDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 10, 1, 2),
    _CucsLsbootIScsiDn_Type()
)
cucsLsbootIScsiDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootIScsiDn.setStatus("current")
_CucsLsbootIScsiRn_Type = SnmpAdminString
_CucsLsbootIScsiRn_Object = MibTableColumn
cucsLsbootIScsiRn = _CucsLsbootIScsiRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 10, 1, 3),
    _CucsLsbootIScsiRn_Type()
)
cucsLsbootIScsiRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootIScsiRn.setStatus("current")
_CucsLsbootIScsiAccess_Type = CucsLsbootIScsiAccess
_CucsLsbootIScsiAccess_Object = MibTableColumn
cucsLsbootIScsiAccess = _CucsLsbootIScsiAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 10, 1, 4),
    _CucsLsbootIScsiAccess_Type()
)
cucsLsbootIScsiAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootIScsiAccess.setStatus("current")
_CucsLsbootIScsiOrder_Type = Gauge32
_CucsLsbootIScsiOrder_Object = MibTableColumn
cucsLsbootIScsiOrder = _CucsLsbootIScsiOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 10, 1, 5),
    _CucsLsbootIScsiOrder_Type()
)
cucsLsbootIScsiOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootIScsiOrder.setStatus("current")
_CucsLsbootIScsiType_Type = CucsLsbootIScsiType
_CucsLsbootIScsiType_Object = MibTableColumn
cucsLsbootIScsiType = _CucsLsbootIScsiType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 10, 1, 6),
    _CucsLsbootIScsiType_Type()
)
cucsLsbootIScsiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootIScsiType.setStatus("current")
_CucsLsbootIScsiImagePathTable_Object = MibTable
cucsLsbootIScsiImagePathTable = _CucsLsbootIScsiImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 11)
)
if mibBuilder.loadTexts:
    cucsLsbootIScsiImagePathTable.setStatus("current")
_CucsLsbootIScsiImagePathEntry_Object = MibTableRow
cucsLsbootIScsiImagePathEntry = _CucsLsbootIScsiImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 11, 1)
)
cucsLsbootIScsiImagePathEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootIScsiImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootIScsiImagePathEntry.setStatus("current")
_CucsLsbootIScsiImagePathInstanceId_Type = CucsManagedObjectId
_CucsLsbootIScsiImagePathInstanceId_Object = MibTableColumn
cucsLsbootIScsiImagePathInstanceId = _CucsLsbootIScsiImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 11, 1, 1),
    _CucsLsbootIScsiImagePathInstanceId_Type()
)
cucsLsbootIScsiImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootIScsiImagePathInstanceId.setStatus("current")
_CucsLsbootIScsiImagePathDn_Type = CucsManagedObjectDn
_CucsLsbootIScsiImagePathDn_Object = MibTableColumn
cucsLsbootIScsiImagePathDn = _CucsLsbootIScsiImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 11, 1, 2),
    _CucsLsbootIScsiImagePathDn_Type()
)
cucsLsbootIScsiImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootIScsiImagePathDn.setStatus("current")
_CucsLsbootIScsiImagePathRn_Type = SnmpAdminString
_CucsLsbootIScsiImagePathRn_Object = MibTableColumn
cucsLsbootIScsiImagePathRn = _CucsLsbootIScsiImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 11, 1, 3),
    _CucsLsbootIScsiImagePathRn_Type()
)
cucsLsbootIScsiImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootIScsiImagePathRn.setStatus("current")
_CucsLsbootIScsiImagePathISCSIVnicName_Type = SnmpAdminString
_CucsLsbootIScsiImagePathISCSIVnicName_Object = MibTableColumn
cucsLsbootIScsiImagePathISCSIVnicName = _CucsLsbootIScsiImagePathISCSIVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 11, 1, 4),
    _CucsLsbootIScsiImagePathISCSIVnicName_Type()
)
cucsLsbootIScsiImagePathISCSIVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootIScsiImagePathISCSIVnicName.setStatus("current")
_CucsLsbootIScsiImagePathType_Type = CucsLsbootIScsiImagePathType
_CucsLsbootIScsiImagePathType_Object = MibTableColumn
cucsLsbootIScsiImagePathType = _CucsLsbootIScsiImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 11, 1, 5),
    _CucsLsbootIScsiImagePathType_Type()
)
cucsLsbootIScsiImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootIScsiImagePathType.setStatus("current")
_CucsLsbootIScsiImagePathVnicName_Type = SnmpAdminString
_CucsLsbootIScsiImagePathVnicName_Object = MibTableColumn
cucsLsbootIScsiImagePathVnicName = _CucsLsbootIScsiImagePathVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 11, 1, 6),
    _CucsLsbootIScsiImagePathVnicName_Type()
)
cucsLsbootIScsiImagePathVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootIScsiImagePathVnicName.setStatus("current")
_CucsLsbootBootSecurityTable_Object = MibTable
cucsLsbootBootSecurityTable = _CucsLsbootBootSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 12)
)
if mibBuilder.loadTexts:
    cucsLsbootBootSecurityTable.setStatus("current")
_CucsLsbootBootSecurityEntry_Object = MibTableRow
cucsLsbootBootSecurityEntry = _CucsLsbootBootSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 12, 1)
)
cucsLsbootBootSecurityEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootBootSecurityInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootBootSecurityEntry.setStatus("current")
_CucsLsbootBootSecurityInstanceId_Type = CucsManagedObjectId
_CucsLsbootBootSecurityInstanceId_Object = MibTableColumn
cucsLsbootBootSecurityInstanceId = _CucsLsbootBootSecurityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 12, 1, 1),
    _CucsLsbootBootSecurityInstanceId_Type()
)
cucsLsbootBootSecurityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootBootSecurityInstanceId.setStatus("current")
_CucsLsbootBootSecurityDn_Type = CucsManagedObjectDn
_CucsLsbootBootSecurityDn_Object = MibTableColumn
cucsLsbootBootSecurityDn = _CucsLsbootBootSecurityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 12, 1, 2),
    _CucsLsbootBootSecurityDn_Type()
)
cucsLsbootBootSecurityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootBootSecurityDn.setStatus("current")
_CucsLsbootBootSecurityRn_Type = SnmpAdminString
_CucsLsbootBootSecurityRn_Object = MibTableColumn
cucsLsbootBootSecurityRn = _CucsLsbootBootSecurityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 12, 1, 3),
    _CucsLsbootBootSecurityRn_Type()
)
cucsLsbootBootSecurityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootBootSecurityRn.setStatus("current")
_CucsLsbootBootSecuritySecureBoot_Type = TruthValue
_CucsLsbootBootSecuritySecureBoot_Object = MibTableColumn
cucsLsbootBootSecuritySecureBoot = _CucsLsbootBootSecuritySecureBoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 12, 1, 4),
    _CucsLsbootBootSecuritySecureBoot_Type()
)
cucsLsbootBootSecuritySecureBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootBootSecuritySecureBoot.setStatus("current")
_CucsLsbootDefaultLocalImageTable_Object = MibTable
cucsLsbootDefaultLocalImageTable = _CucsLsbootDefaultLocalImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 13)
)
if mibBuilder.loadTexts:
    cucsLsbootDefaultLocalImageTable.setStatus("current")
_CucsLsbootDefaultLocalImageEntry_Object = MibTableRow
cucsLsbootDefaultLocalImageEntry = _CucsLsbootDefaultLocalImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 13, 1)
)
cucsLsbootDefaultLocalImageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootDefaultLocalImageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootDefaultLocalImageEntry.setStatus("current")
_CucsLsbootDefaultLocalImageInstanceId_Type = CucsManagedObjectId
_CucsLsbootDefaultLocalImageInstanceId_Object = MibTableColumn
cucsLsbootDefaultLocalImageInstanceId = _CucsLsbootDefaultLocalImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 13, 1, 1),
    _CucsLsbootDefaultLocalImageInstanceId_Type()
)
cucsLsbootDefaultLocalImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootDefaultLocalImageInstanceId.setStatus("current")
_CucsLsbootDefaultLocalImageDn_Type = CucsManagedObjectDn
_CucsLsbootDefaultLocalImageDn_Object = MibTableColumn
cucsLsbootDefaultLocalImageDn = _CucsLsbootDefaultLocalImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 13, 1, 2),
    _CucsLsbootDefaultLocalImageDn_Type()
)
cucsLsbootDefaultLocalImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefaultLocalImageDn.setStatus("current")
_CucsLsbootDefaultLocalImageRn_Type = SnmpAdminString
_CucsLsbootDefaultLocalImageRn_Object = MibTableColumn
cucsLsbootDefaultLocalImageRn = _CucsLsbootDefaultLocalImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 13, 1, 3),
    _CucsLsbootDefaultLocalImageRn_Type()
)
cucsLsbootDefaultLocalImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefaultLocalImageRn.setStatus("current")
_CucsLsbootDefaultLocalImageOrder_Type = Gauge32
_CucsLsbootDefaultLocalImageOrder_Object = MibTableColumn
cucsLsbootDefaultLocalImageOrder = _CucsLsbootDefaultLocalImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 13, 1, 6),
    _CucsLsbootDefaultLocalImageOrder_Type()
)
cucsLsbootDefaultLocalImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefaultLocalImageOrder.setStatus("current")
_CucsLsbootDefaultLocalImageType_Type = CucsLsbootDefaultLocalImageType
_CucsLsbootDefaultLocalImageType_Object = MibTableColumn
cucsLsbootDefaultLocalImageType = _CucsLsbootDefaultLocalImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 13, 1, 7),
    _CucsLsbootDefaultLocalImageType_Type()
)
cucsLsbootDefaultLocalImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefaultLocalImageType.setStatus("current")
_CucsLsbootDefaultLocalImagePropAcl_Type = Unsigned64
_CucsLsbootDefaultLocalImagePropAcl_Object = MibTableColumn
cucsLsbootDefaultLocalImagePropAcl = _CucsLsbootDefaultLocalImagePropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 13, 1, 8),
    _CucsLsbootDefaultLocalImagePropAcl_Type()
)
cucsLsbootDefaultLocalImagePropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootDefaultLocalImagePropAcl.setStatus("current")
_CucsLsbootLocalHddImageTable_Object = MibTable
cucsLsbootLocalHddImageTable = _CucsLsbootLocalHddImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 14)
)
if mibBuilder.loadTexts:
    cucsLsbootLocalHddImageTable.setStatus("current")
_CucsLsbootLocalHddImageEntry_Object = MibTableRow
cucsLsbootLocalHddImageEntry = _CucsLsbootLocalHddImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 14, 1)
)
cucsLsbootLocalHddImageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootLocalHddImageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootLocalHddImageEntry.setStatus("current")
_CucsLsbootLocalHddImageInstanceId_Type = CucsManagedObjectId
_CucsLsbootLocalHddImageInstanceId_Object = MibTableColumn
cucsLsbootLocalHddImageInstanceId = _CucsLsbootLocalHddImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 14, 1, 1),
    _CucsLsbootLocalHddImageInstanceId_Type()
)
cucsLsbootLocalHddImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootLocalHddImageInstanceId.setStatus("current")
_CucsLsbootLocalHddImageDn_Type = CucsManagedObjectDn
_CucsLsbootLocalHddImageDn_Object = MibTableColumn
cucsLsbootLocalHddImageDn = _CucsLsbootLocalHddImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 14, 1, 2),
    _CucsLsbootLocalHddImageDn_Type()
)
cucsLsbootLocalHddImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalHddImageDn.setStatus("current")
_CucsLsbootLocalHddImageRn_Type = SnmpAdminString
_CucsLsbootLocalHddImageRn_Object = MibTableColumn
cucsLsbootLocalHddImageRn = _CucsLsbootLocalHddImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 14, 1, 3),
    _CucsLsbootLocalHddImageRn_Type()
)
cucsLsbootLocalHddImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalHddImageRn.setStatus("current")
_CucsLsbootLocalHddImageOrder_Type = Gauge32
_CucsLsbootLocalHddImageOrder_Object = MibTableColumn
cucsLsbootLocalHddImageOrder = _CucsLsbootLocalHddImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 14, 1, 6),
    _CucsLsbootLocalHddImageOrder_Type()
)
cucsLsbootLocalHddImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalHddImageOrder.setStatus("current")
_CucsLsbootLocalHddImageType_Type = CucsLsbootLocalHddImageType
_CucsLsbootLocalHddImageType_Object = MibTableColumn
cucsLsbootLocalHddImageType = _CucsLsbootLocalHddImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 14, 1, 7),
    _CucsLsbootLocalHddImageType_Type()
)
cucsLsbootLocalHddImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalHddImageType.setStatus("current")
_CucsLsbootSanTable_Object = MibTable
cucsLsbootSanTable = _CucsLsbootSanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 15)
)
if mibBuilder.loadTexts:
    cucsLsbootSanTable.setStatus("current")
_CucsLsbootSanEntry_Object = MibTableRow
cucsLsbootSanEntry = _CucsLsbootSanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 15, 1)
)
cucsLsbootSanEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootSanInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootSanEntry.setStatus("current")
_CucsLsbootSanInstanceId_Type = CucsManagedObjectId
_CucsLsbootSanInstanceId_Object = MibTableColumn
cucsLsbootSanInstanceId = _CucsLsbootSanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 15, 1, 1),
    _CucsLsbootSanInstanceId_Type()
)
cucsLsbootSanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootSanInstanceId.setStatus("current")
_CucsLsbootSanDn_Type = CucsManagedObjectDn
_CucsLsbootSanDn_Object = MibTableColumn
cucsLsbootSanDn = _CucsLsbootSanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 15, 1, 2),
    _CucsLsbootSanDn_Type()
)
cucsLsbootSanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanDn.setStatus("current")
_CucsLsbootSanRn_Type = SnmpAdminString
_CucsLsbootSanRn_Object = MibTableColumn
cucsLsbootSanRn = _CucsLsbootSanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 15, 1, 3),
    _CucsLsbootSanRn_Type()
)
cucsLsbootSanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanRn.setStatus("current")
_CucsLsbootSanAccess_Type = CucsLsbootSanAccess
_CucsLsbootSanAccess_Object = MibTableColumn
cucsLsbootSanAccess = _CucsLsbootSanAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 15, 1, 4),
    _CucsLsbootSanAccess_Type()
)
cucsLsbootSanAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanAccess.setStatus("current")
_CucsLsbootSanOrder_Type = Gauge32
_CucsLsbootSanOrder_Object = MibTableColumn
cucsLsbootSanOrder = _CucsLsbootSanOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 15, 1, 5),
    _CucsLsbootSanOrder_Type()
)
cucsLsbootSanOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanOrder.setStatus("current")
_CucsLsbootSanType_Type = CucsLsbootSanType
_CucsLsbootSanType_Object = MibTableColumn
cucsLsbootSanType = _CucsLsbootSanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 15, 1, 6),
    _CucsLsbootSanType_Type()
)
cucsLsbootSanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanType.setStatus("current")
_CucsLsbootSanCatSanImageTable_Object = MibTable
cucsLsbootSanCatSanImageTable = _CucsLsbootSanCatSanImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 16)
)
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImageTable.setStatus("current")
_CucsLsbootSanCatSanImageEntry_Object = MibTableRow
cucsLsbootSanCatSanImageEntry = _CucsLsbootSanCatSanImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 16, 1)
)
cucsLsbootSanCatSanImageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootSanCatSanImageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImageEntry.setStatus("current")
_CucsLsbootSanCatSanImageInstanceId_Type = CucsManagedObjectId
_CucsLsbootSanCatSanImageInstanceId_Object = MibTableColumn
cucsLsbootSanCatSanImageInstanceId = _CucsLsbootSanCatSanImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 16, 1, 1),
    _CucsLsbootSanCatSanImageInstanceId_Type()
)
cucsLsbootSanCatSanImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImageInstanceId.setStatus("current")
_CucsLsbootSanCatSanImageDn_Type = CucsManagedObjectDn
_CucsLsbootSanCatSanImageDn_Object = MibTableColumn
cucsLsbootSanCatSanImageDn = _CucsLsbootSanCatSanImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 16, 1, 2),
    _CucsLsbootSanCatSanImageDn_Type()
)
cucsLsbootSanCatSanImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImageDn.setStatus("current")
_CucsLsbootSanCatSanImageRn_Type = SnmpAdminString
_CucsLsbootSanCatSanImageRn_Object = MibTableColumn
cucsLsbootSanCatSanImageRn = _CucsLsbootSanCatSanImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 16, 1, 3),
    _CucsLsbootSanCatSanImageRn_Type()
)
cucsLsbootSanCatSanImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImageRn.setStatus("current")
_CucsLsbootSanCatSanImageType_Type = CucsLsbootSanCatSanImageType
_CucsLsbootSanCatSanImageType_Object = MibTableColumn
cucsLsbootSanCatSanImageType = _CucsLsbootSanCatSanImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 16, 1, 4),
    _CucsLsbootSanCatSanImageType_Type()
)
cucsLsbootSanCatSanImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImageType.setStatus("current")
_CucsLsbootSanCatSanImageVnicName_Type = SnmpAdminString
_CucsLsbootSanCatSanImageVnicName_Object = MibTableColumn
cucsLsbootSanCatSanImageVnicName = _CucsLsbootSanCatSanImageVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 16, 1, 5),
    _CucsLsbootSanCatSanImageVnicName_Type()
)
cucsLsbootSanCatSanImageVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImageVnicName.setStatus("current")
_CucsLsbootSanCatSanImagePathTable_Object = MibTable
cucsLsbootSanCatSanImagePathTable = _CucsLsbootSanCatSanImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 17)
)
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImagePathTable.setStatus("current")
_CucsLsbootSanCatSanImagePathEntry_Object = MibTableRow
cucsLsbootSanCatSanImagePathEntry = _CucsLsbootSanCatSanImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 17, 1)
)
cucsLsbootSanCatSanImagePathEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootSanCatSanImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImagePathEntry.setStatus("current")
_CucsLsbootSanCatSanImagePathInstanceId_Type = CucsManagedObjectId
_CucsLsbootSanCatSanImagePathInstanceId_Object = MibTableColumn
cucsLsbootSanCatSanImagePathInstanceId = _CucsLsbootSanCatSanImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 17, 1, 1),
    _CucsLsbootSanCatSanImagePathInstanceId_Type()
)
cucsLsbootSanCatSanImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImagePathInstanceId.setStatus("current")
_CucsLsbootSanCatSanImagePathDn_Type = CucsManagedObjectDn
_CucsLsbootSanCatSanImagePathDn_Object = MibTableColumn
cucsLsbootSanCatSanImagePathDn = _CucsLsbootSanCatSanImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 17, 1, 2),
    _CucsLsbootSanCatSanImagePathDn_Type()
)
cucsLsbootSanCatSanImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImagePathDn.setStatus("current")
_CucsLsbootSanCatSanImagePathRn_Type = SnmpAdminString
_CucsLsbootSanCatSanImagePathRn_Object = MibTableColumn
cucsLsbootSanCatSanImagePathRn = _CucsLsbootSanCatSanImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 17, 1, 3),
    _CucsLsbootSanCatSanImagePathRn_Type()
)
cucsLsbootSanCatSanImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImagePathRn.setStatus("current")
_CucsLsbootSanCatSanImagePathLun_Type = SnmpAdminString
_CucsLsbootSanCatSanImagePathLun_Object = MibTableColumn
cucsLsbootSanCatSanImagePathLun = _CucsLsbootSanCatSanImagePathLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 17, 1, 4),
    _CucsLsbootSanCatSanImagePathLun_Type()
)
cucsLsbootSanCatSanImagePathLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImagePathLun.setStatus("current")
_CucsLsbootSanCatSanImagePathType_Type = CucsLsbootSanCatSanImagePathType
_CucsLsbootSanCatSanImagePathType_Object = MibTableColumn
cucsLsbootSanCatSanImagePathType = _CucsLsbootSanCatSanImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 17, 1, 5),
    _CucsLsbootSanCatSanImagePathType_Type()
)
cucsLsbootSanCatSanImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImagePathType.setStatus("current")
_CucsLsbootSanCatSanImagePathVnicName_Type = SnmpAdminString
_CucsLsbootSanCatSanImagePathVnicName_Object = MibTableColumn
cucsLsbootSanCatSanImagePathVnicName = _CucsLsbootSanCatSanImagePathVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 17, 1, 6),
    _CucsLsbootSanCatSanImagePathVnicName_Type()
)
cucsLsbootSanCatSanImagePathVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImagePathVnicName.setStatus("current")
_CucsLsbootSanCatSanImagePathWwn_Type = Unsigned64
_CucsLsbootSanCatSanImagePathWwn_Object = MibTableColumn
cucsLsbootSanCatSanImagePathWwn = _CucsLsbootSanCatSanImagePathWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 17, 1, 7),
    _CucsLsbootSanCatSanImagePathWwn_Type()
)
cucsLsbootSanCatSanImagePathWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootSanCatSanImagePathWwn.setStatus("current")
_CucsLsbootUsbExternalImageTable_Object = MibTable
cucsLsbootUsbExternalImageTable = _CucsLsbootUsbExternalImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 18)
)
if mibBuilder.loadTexts:
    cucsLsbootUsbExternalImageTable.setStatus("current")
_CucsLsbootUsbExternalImageEntry_Object = MibTableRow
cucsLsbootUsbExternalImageEntry = _CucsLsbootUsbExternalImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 18, 1)
)
cucsLsbootUsbExternalImageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootUsbExternalImageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootUsbExternalImageEntry.setStatus("current")
_CucsLsbootUsbExternalImageInstanceId_Type = CucsManagedObjectId
_CucsLsbootUsbExternalImageInstanceId_Object = MibTableColumn
cucsLsbootUsbExternalImageInstanceId = _CucsLsbootUsbExternalImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 18, 1, 1),
    _CucsLsbootUsbExternalImageInstanceId_Type()
)
cucsLsbootUsbExternalImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootUsbExternalImageInstanceId.setStatus("current")
_CucsLsbootUsbExternalImageDn_Type = CucsManagedObjectDn
_CucsLsbootUsbExternalImageDn_Object = MibTableColumn
cucsLsbootUsbExternalImageDn = _CucsLsbootUsbExternalImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 18, 1, 2),
    _CucsLsbootUsbExternalImageDn_Type()
)
cucsLsbootUsbExternalImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUsbExternalImageDn.setStatus("current")
_CucsLsbootUsbExternalImageRn_Type = SnmpAdminString
_CucsLsbootUsbExternalImageRn_Object = MibTableColumn
cucsLsbootUsbExternalImageRn = _CucsLsbootUsbExternalImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 18, 1, 3),
    _CucsLsbootUsbExternalImageRn_Type()
)
cucsLsbootUsbExternalImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUsbExternalImageRn.setStatus("current")
_CucsLsbootUsbExternalImageOrder_Type = Gauge32
_CucsLsbootUsbExternalImageOrder_Object = MibTableColumn
cucsLsbootUsbExternalImageOrder = _CucsLsbootUsbExternalImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 18, 1, 6),
    _CucsLsbootUsbExternalImageOrder_Type()
)
cucsLsbootUsbExternalImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUsbExternalImageOrder.setStatus("current")
_CucsLsbootUsbExternalImageType_Type = CucsLsbootUsbExternalImageType
_CucsLsbootUsbExternalImageType_Object = MibTableColumn
cucsLsbootUsbExternalImageType = _CucsLsbootUsbExternalImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 18, 1, 7),
    _CucsLsbootUsbExternalImageType_Type()
)
cucsLsbootUsbExternalImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUsbExternalImageType.setStatus("current")
_CucsLsbootUsbFlashStorageImageTable_Object = MibTable
cucsLsbootUsbFlashStorageImageTable = _CucsLsbootUsbFlashStorageImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 19)
)
if mibBuilder.loadTexts:
    cucsLsbootUsbFlashStorageImageTable.setStatus("current")
_CucsLsbootUsbFlashStorageImageEntry_Object = MibTableRow
cucsLsbootUsbFlashStorageImageEntry = _CucsLsbootUsbFlashStorageImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 19, 1)
)
cucsLsbootUsbFlashStorageImageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootUsbFlashStorageImageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootUsbFlashStorageImageEntry.setStatus("current")
_CucsLsbootUsbFlashStorageImageInstanceId_Type = CucsManagedObjectId
_CucsLsbootUsbFlashStorageImageInstanceId_Object = MibTableColumn
cucsLsbootUsbFlashStorageImageInstanceId = _CucsLsbootUsbFlashStorageImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 19, 1, 1),
    _CucsLsbootUsbFlashStorageImageInstanceId_Type()
)
cucsLsbootUsbFlashStorageImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootUsbFlashStorageImageInstanceId.setStatus("current")
_CucsLsbootUsbFlashStorageImageDn_Type = CucsManagedObjectDn
_CucsLsbootUsbFlashStorageImageDn_Object = MibTableColumn
cucsLsbootUsbFlashStorageImageDn = _CucsLsbootUsbFlashStorageImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 19, 1, 2),
    _CucsLsbootUsbFlashStorageImageDn_Type()
)
cucsLsbootUsbFlashStorageImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUsbFlashStorageImageDn.setStatus("current")
_CucsLsbootUsbFlashStorageImageRn_Type = SnmpAdminString
_CucsLsbootUsbFlashStorageImageRn_Object = MibTableColumn
cucsLsbootUsbFlashStorageImageRn = _CucsLsbootUsbFlashStorageImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 19, 1, 3),
    _CucsLsbootUsbFlashStorageImageRn_Type()
)
cucsLsbootUsbFlashStorageImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUsbFlashStorageImageRn.setStatus("current")
_CucsLsbootUsbFlashStorageImageOrder_Type = Gauge32
_CucsLsbootUsbFlashStorageImageOrder_Object = MibTableColumn
cucsLsbootUsbFlashStorageImageOrder = _CucsLsbootUsbFlashStorageImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 19, 1, 6),
    _CucsLsbootUsbFlashStorageImageOrder_Type()
)
cucsLsbootUsbFlashStorageImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUsbFlashStorageImageOrder.setStatus("current")
_CucsLsbootUsbFlashStorageImageType_Type = CucsLsbootUsbFlashStorageImageType
_CucsLsbootUsbFlashStorageImageType_Object = MibTableColumn
cucsLsbootUsbFlashStorageImageType = _CucsLsbootUsbFlashStorageImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 19, 1, 7),
    _CucsLsbootUsbFlashStorageImageType_Type()
)
cucsLsbootUsbFlashStorageImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUsbFlashStorageImageType.setStatus("current")
_CucsLsbootUsbInternalImageTable_Object = MibTable
cucsLsbootUsbInternalImageTable = _CucsLsbootUsbInternalImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 20)
)
if mibBuilder.loadTexts:
    cucsLsbootUsbInternalImageTable.setStatus("current")
_CucsLsbootUsbInternalImageEntry_Object = MibTableRow
cucsLsbootUsbInternalImageEntry = _CucsLsbootUsbInternalImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 20, 1)
)
cucsLsbootUsbInternalImageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootUsbInternalImageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootUsbInternalImageEntry.setStatus("current")
_CucsLsbootUsbInternalImageInstanceId_Type = CucsManagedObjectId
_CucsLsbootUsbInternalImageInstanceId_Object = MibTableColumn
cucsLsbootUsbInternalImageInstanceId = _CucsLsbootUsbInternalImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 20, 1, 1),
    _CucsLsbootUsbInternalImageInstanceId_Type()
)
cucsLsbootUsbInternalImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootUsbInternalImageInstanceId.setStatus("current")
_CucsLsbootUsbInternalImageDn_Type = CucsManagedObjectDn
_CucsLsbootUsbInternalImageDn_Object = MibTableColumn
cucsLsbootUsbInternalImageDn = _CucsLsbootUsbInternalImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 20, 1, 2),
    _CucsLsbootUsbInternalImageDn_Type()
)
cucsLsbootUsbInternalImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUsbInternalImageDn.setStatus("current")
_CucsLsbootUsbInternalImageRn_Type = SnmpAdminString
_CucsLsbootUsbInternalImageRn_Object = MibTableColumn
cucsLsbootUsbInternalImageRn = _CucsLsbootUsbInternalImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 20, 1, 3),
    _CucsLsbootUsbInternalImageRn_Type()
)
cucsLsbootUsbInternalImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUsbInternalImageRn.setStatus("current")
_CucsLsbootUsbInternalImageOrder_Type = Gauge32
_CucsLsbootUsbInternalImageOrder_Object = MibTableColumn
cucsLsbootUsbInternalImageOrder = _CucsLsbootUsbInternalImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 20, 1, 6),
    _CucsLsbootUsbInternalImageOrder_Type()
)
cucsLsbootUsbInternalImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUsbInternalImageOrder.setStatus("current")
_CucsLsbootUsbInternalImageType_Type = CucsLsbootUsbInternalImageType
_CucsLsbootUsbInternalImageType_Object = MibTableColumn
cucsLsbootUsbInternalImageType = _CucsLsbootUsbInternalImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 20, 1, 7),
    _CucsLsbootUsbInternalImageType_Type()
)
cucsLsbootUsbInternalImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUsbInternalImageType.setStatus("current")
_CucsLsbootLocalDiskImageTable_Object = MibTable
cucsLsbootLocalDiskImageTable = _CucsLsbootLocalDiskImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 21)
)
if mibBuilder.loadTexts:
    cucsLsbootLocalDiskImageTable.setStatus("current")
_CucsLsbootLocalDiskImageEntry_Object = MibTableRow
cucsLsbootLocalDiskImageEntry = _CucsLsbootLocalDiskImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 21, 1)
)
cucsLsbootLocalDiskImageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootLocalDiskImageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootLocalDiskImageEntry.setStatus("current")
_CucsLsbootLocalDiskImageInstanceId_Type = CucsManagedObjectId
_CucsLsbootLocalDiskImageInstanceId_Object = MibTableColumn
cucsLsbootLocalDiskImageInstanceId = _CucsLsbootLocalDiskImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 21, 1, 1),
    _CucsLsbootLocalDiskImageInstanceId_Type()
)
cucsLsbootLocalDiskImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootLocalDiskImageInstanceId.setStatus("current")
_CucsLsbootLocalDiskImageDn_Type = CucsManagedObjectDn
_CucsLsbootLocalDiskImageDn_Object = MibTableColumn
cucsLsbootLocalDiskImageDn = _CucsLsbootLocalDiskImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 21, 1, 2),
    _CucsLsbootLocalDiskImageDn_Type()
)
cucsLsbootLocalDiskImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalDiskImageDn.setStatus("current")
_CucsLsbootLocalDiskImageRn_Type = SnmpAdminString
_CucsLsbootLocalDiskImageRn_Object = MibTableColumn
cucsLsbootLocalDiskImageRn = _CucsLsbootLocalDiskImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 21, 1, 3),
    _CucsLsbootLocalDiskImageRn_Type()
)
cucsLsbootLocalDiskImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalDiskImageRn.setStatus("current")
_CucsLsbootLocalDiskImageOrder_Type = Gauge32
_CucsLsbootLocalDiskImageOrder_Object = MibTableColumn
cucsLsbootLocalDiskImageOrder = _CucsLsbootLocalDiskImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 21, 1, 4),
    _CucsLsbootLocalDiskImageOrder_Type()
)
cucsLsbootLocalDiskImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalDiskImageOrder.setStatus("current")
_CucsLsbootLocalDiskImageType_Type = CucsLsbootLocalDiskImageType
_CucsLsbootLocalDiskImageType_Object = MibTableColumn
cucsLsbootLocalDiskImageType = _CucsLsbootLocalDiskImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 21, 1, 5),
    _CucsLsbootLocalDiskImageType_Type()
)
cucsLsbootLocalDiskImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalDiskImageType.setStatus("current")
_CucsLsbootLocalDiskImagePathTable_Object = MibTable
cucsLsbootLocalDiskImagePathTable = _CucsLsbootLocalDiskImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 22)
)
if mibBuilder.loadTexts:
    cucsLsbootLocalDiskImagePathTable.setStatus("current")
_CucsLsbootLocalDiskImagePathEntry_Object = MibTableRow
cucsLsbootLocalDiskImagePathEntry = _CucsLsbootLocalDiskImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 22, 1)
)
cucsLsbootLocalDiskImagePathEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootLocalDiskImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootLocalDiskImagePathEntry.setStatus("current")
_CucsLsbootLocalDiskImagePathInstanceId_Type = CucsManagedObjectId
_CucsLsbootLocalDiskImagePathInstanceId_Object = MibTableColumn
cucsLsbootLocalDiskImagePathInstanceId = _CucsLsbootLocalDiskImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 22, 1, 1),
    _CucsLsbootLocalDiskImagePathInstanceId_Type()
)
cucsLsbootLocalDiskImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootLocalDiskImagePathInstanceId.setStatus("current")
_CucsLsbootLocalDiskImagePathDn_Type = CucsManagedObjectDn
_CucsLsbootLocalDiskImagePathDn_Object = MibTableColumn
cucsLsbootLocalDiskImagePathDn = _CucsLsbootLocalDiskImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 22, 1, 2),
    _CucsLsbootLocalDiskImagePathDn_Type()
)
cucsLsbootLocalDiskImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalDiskImagePathDn.setStatus("current")
_CucsLsbootLocalDiskImagePathRn_Type = SnmpAdminString
_CucsLsbootLocalDiskImagePathRn_Object = MibTableColumn
cucsLsbootLocalDiskImagePathRn = _CucsLsbootLocalDiskImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 22, 1, 3),
    _CucsLsbootLocalDiskImagePathRn_Type()
)
cucsLsbootLocalDiskImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalDiskImagePathRn.setStatus("current")
_CucsLsbootLocalDiskImagePathSlotNumber_Type = Gauge32
_CucsLsbootLocalDiskImagePathSlotNumber_Object = MibTableColumn
cucsLsbootLocalDiskImagePathSlotNumber = _CucsLsbootLocalDiskImagePathSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 22, 1, 4),
    _CucsLsbootLocalDiskImagePathSlotNumber_Type()
)
cucsLsbootLocalDiskImagePathSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalDiskImagePathSlotNumber.setStatus("current")
_CucsLsbootLocalDiskImagePathType_Type = CucsLsbootLocalDiskImagePathType
_CucsLsbootLocalDiskImagePathType_Object = MibTableColumn
cucsLsbootLocalDiskImagePathType = _CucsLsbootLocalDiskImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 22, 1, 5),
    _CucsLsbootLocalDiskImagePathType_Type()
)
cucsLsbootLocalDiskImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalDiskImagePathType.setStatus("current")
_CucsLsbootLocalLunImagePathTable_Object = MibTable
cucsLsbootLocalLunImagePathTable = _CucsLsbootLocalLunImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 23)
)
if mibBuilder.loadTexts:
    cucsLsbootLocalLunImagePathTable.setStatus("current")
_CucsLsbootLocalLunImagePathEntry_Object = MibTableRow
cucsLsbootLocalLunImagePathEntry = _CucsLsbootLocalLunImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 23, 1)
)
cucsLsbootLocalLunImagePathEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootLocalLunImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootLocalLunImagePathEntry.setStatus("current")
_CucsLsbootLocalLunImagePathInstanceId_Type = CucsManagedObjectId
_CucsLsbootLocalLunImagePathInstanceId_Object = MibTableColumn
cucsLsbootLocalLunImagePathInstanceId = _CucsLsbootLocalLunImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 23, 1, 1),
    _CucsLsbootLocalLunImagePathInstanceId_Type()
)
cucsLsbootLocalLunImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootLocalLunImagePathInstanceId.setStatus("current")
_CucsLsbootLocalLunImagePathDn_Type = CucsManagedObjectDn
_CucsLsbootLocalLunImagePathDn_Object = MibTableColumn
cucsLsbootLocalLunImagePathDn = _CucsLsbootLocalLunImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 23, 1, 2),
    _CucsLsbootLocalLunImagePathDn_Type()
)
cucsLsbootLocalLunImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalLunImagePathDn.setStatus("current")
_CucsLsbootLocalLunImagePathRn_Type = SnmpAdminString
_CucsLsbootLocalLunImagePathRn_Object = MibTableColumn
cucsLsbootLocalLunImagePathRn = _CucsLsbootLocalLunImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 23, 1, 3),
    _CucsLsbootLocalLunImagePathRn_Type()
)
cucsLsbootLocalLunImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalLunImagePathRn.setStatus("current")
_CucsLsbootLocalLunImagePathLunName_Type = SnmpAdminString
_CucsLsbootLocalLunImagePathLunName_Object = MibTableColumn
cucsLsbootLocalLunImagePathLunName = _CucsLsbootLocalLunImagePathLunName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 23, 1, 4),
    _CucsLsbootLocalLunImagePathLunName_Type()
)
cucsLsbootLocalLunImagePathLunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalLunImagePathLunName.setStatus("current")
_CucsLsbootLocalLunImagePathType_Type = CucsLsbootLocalLunImagePathType
_CucsLsbootLocalLunImagePathType_Object = MibTableColumn
cucsLsbootLocalLunImagePathType = _CucsLsbootLocalLunImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 23, 1, 5),
    _CucsLsbootLocalLunImagePathType_Type()
)
cucsLsbootLocalLunImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootLocalLunImagePathType.setStatus("current")
_CucsLsbootUEFIBootParamTable_Object = MibTable
cucsLsbootUEFIBootParamTable = _CucsLsbootUEFIBootParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 24)
)
if mibBuilder.loadTexts:
    cucsLsbootUEFIBootParamTable.setStatus("current")
_CucsLsbootUEFIBootParamEntry_Object = MibTableRow
cucsLsbootUEFIBootParamEntry = _CucsLsbootUEFIBootParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 24, 1)
)
cucsLsbootUEFIBootParamEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootUEFIBootParamInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootUEFIBootParamEntry.setStatus("current")
_CucsLsbootUEFIBootParamInstanceId_Type = CucsManagedObjectId
_CucsLsbootUEFIBootParamInstanceId_Object = MibTableColumn
cucsLsbootUEFIBootParamInstanceId = _CucsLsbootUEFIBootParamInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 24, 1, 1),
    _CucsLsbootUEFIBootParamInstanceId_Type()
)
cucsLsbootUEFIBootParamInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootUEFIBootParamInstanceId.setStatus("current")
_CucsLsbootUEFIBootParamDn_Type = CucsManagedObjectDn
_CucsLsbootUEFIBootParamDn_Object = MibTableColumn
cucsLsbootUEFIBootParamDn = _CucsLsbootUEFIBootParamDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 24, 1, 2),
    _CucsLsbootUEFIBootParamDn_Type()
)
cucsLsbootUEFIBootParamDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUEFIBootParamDn.setStatus("current")
_CucsLsbootUEFIBootParamRn_Type = SnmpAdminString
_CucsLsbootUEFIBootParamRn_Object = MibTableColumn
cucsLsbootUEFIBootParamRn = _CucsLsbootUEFIBootParamRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 24, 1, 3),
    _CucsLsbootUEFIBootParamRn_Type()
)
cucsLsbootUEFIBootParamRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUEFIBootParamRn.setStatus("current")
_CucsLsbootUEFIBootParamBootDescription_Type = SnmpAdminString
_CucsLsbootUEFIBootParamBootDescription_Object = MibTableColumn
cucsLsbootUEFIBootParamBootDescription = _CucsLsbootUEFIBootParamBootDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 24, 1, 4),
    _CucsLsbootUEFIBootParamBootDescription_Type()
)
cucsLsbootUEFIBootParamBootDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUEFIBootParamBootDescription.setStatus("current")
_CucsLsbootUEFIBootParamBootLoaderName_Type = SnmpAdminString
_CucsLsbootUEFIBootParamBootLoaderName_Object = MibTableColumn
cucsLsbootUEFIBootParamBootLoaderName = _CucsLsbootUEFIBootParamBootLoaderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 24, 1, 5),
    _CucsLsbootUEFIBootParamBootLoaderName_Type()
)
cucsLsbootUEFIBootParamBootLoaderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUEFIBootParamBootLoaderName.setStatus("current")
_CucsLsbootUEFIBootParamBootLoaderPath_Type = SnmpAdminString
_CucsLsbootUEFIBootParamBootLoaderPath_Object = MibTableColumn
cucsLsbootUEFIBootParamBootLoaderPath = _CucsLsbootUEFIBootParamBootLoaderPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 24, 1, 6),
    _CucsLsbootUEFIBootParamBootLoaderPath_Type()
)
cucsLsbootUEFIBootParamBootLoaderPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootUEFIBootParamBootLoaderPath.setStatus("current")
_CucsLsbootEmbeddedLocalDiskImageTable_Object = MibTable
cucsLsbootEmbeddedLocalDiskImageTable = _CucsLsbootEmbeddedLocalDiskImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 25)
)
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalDiskImageTable.setStatus("current")
_CucsLsbootEmbeddedLocalDiskImageEntry_Object = MibTableRow
cucsLsbootEmbeddedLocalDiskImageEntry = _CucsLsbootEmbeddedLocalDiskImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 25, 1)
)
cucsLsbootEmbeddedLocalDiskImageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootEmbeddedLocalDiskImageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalDiskImageEntry.setStatus("current")
_CucsLsbootEmbeddedLocalDiskImageInstanceId_Type = CucsManagedObjectId
_CucsLsbootEmbeddedLocalDiskImageInstanceId_Object = MibTableColumn
cucsLsbootEmbeddedLocalDiskImageInstanceId = _CucsLsbootEmbeddedLocalDiskImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 25, 1, 1),
    _CucsLsbootEmbeddedLocalDiskImageInstanceId_Type()
)
cucsLsbootEmbeddedLocalDiskImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalDiskImageInstanceId.setStatus("current")
_CucsLsbootEmbeddedLocalDiskImageDn_Type = CucsManagedObjectDn
_CucsLsbootEmbeddedLocalDiskImageDn_Object = MibTableColumn
cucsLsbootEmbeddedLocalDiskImageDn = _CucsLsbootEmbeddedLocalDiskImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 25, 1, 2),
    _CucsLsbootEmbeddedLocalDiskImageDn_Type()
)
cucsLsbootEmbeddedLocalDiskImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalDiskImageDn.setStatus("current")
_CucsLsbootEmbeddedLocalDiskImageRn_Type = SnmpAdminString
_CucsLsbootEmbeddedLocalDiskImageRn_Object = MibTableColumn
cucsLsbootEmbeddedLocalDiskImageRn = _CucsLsbootEmbeddedLocalDiskImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 25, 1, 3),
    _CucsLsbootEmbeddedLocalDiskImageRn_Type()
)
cucsLsbootEmbeddedLocalDiskImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalDiskImageRn.setStatus("current")
_CucsLsbootEmbeddedLocalDiskImageOrder_Type = Gauge32
_CucsLsbootEmbeddedLocalDiskImageOrder_Object = MibTableColumn
cucsLsbootEmbeddedLocalDiskImageOrder = _CucsLsbootEmbeddedLocalDiskImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 25, 1, 4),
    _CucsLsbootEmbeddedLocalDiskImageOrder_Type()
)
cucsLsbootEmbeddedLocalDiskImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalDiskImageOrder.setStatus("current")
_CucsLsbootEmbeddedLocalDiskImageType_Type = CucsLsbootEmbeddedLocalDiskImageType
_CucsLsbootEmbeddedLocalDiskImageType_Object = MibTableColumn
cucsLsbootEmbeddedLocalDiskImageType = _CucsLsbootEmbeddedLocalDiskImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 25, 1, 5),
    _CucsLsbootEmbeddedLocalDiskImageType_Type()
)
cucsLsbootEmbeddedLocalDiskImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalDiskImageType.setStatus("current")
_CucsLsbootEmbeddedLocalDiskImagePathTable_Object = MibTable
cucsLsbootEmbeddedLocalDiskImagePathTable = _CucsLsbootEmbeddedLocalDiskImagePathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 26)
)
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalDiskImagePathTable.setStatus("current")
_CucsLsbootEmbeddedLocalDiskImagePathEntry_Object = MibTableRow
cucsLsbootEmbeddedLocalDiskImagePathEntry = _CucsLsbootEmbeddedLocalDiskImagePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 26, 1)
)
cucsLsbootEmbeddedLocalDiskImagePathEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootEmbeddedLocalDiskImagePathInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalDiskImagePathEntry.setStatus("current")
_CucsLsbootEmbeddedLocalDiskImagePathInstanceId_Type = CucsManagedObjectId
_CucsLsbootEmbeddedLocalDiskImagePathInstanceId_Object = MibTableColumn
cucsLsbootEmbeddedLocalDiskImagePathInstanceId = _CucsLsbootEmbeddedLocalDiskImagePathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 26, 1, 1),
    _CucsLsbootEmbeddedLocalDiskImagePathInstanceId_Type()
)
cucsLsbootEmbeddedLocalDiskImagePathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalDiskImagePathInstanceId.setStatus("current")
_CucsLsbootEmbeddedLocalDiskImagePathDn_Type = CucsManagedObjectDn
_CucsLsbootEmbeddedLocalDiskImagePathDn_Object = MibTableColumn
cucsLsbootEmbeddedLocalDiskImagePathDn = _CucsLsbootEmbeddedLocalDiskImagePathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 26, 1, 2),
    _CucsLsbootEmbeddedLocalDiskImagePathDn_Type()
)
cucsLsbootEmbeddedLocalDiskImagePathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalDiskImagePathDn.setStatus("current")
_CucsLsbootEmbeddedLocalDiskImagePathRn_Type = SnmpAdminString
_CucsLsbootEmbeddedLocalDiskImagePathRn_Object = MibTableColumn
cucsLsbootEmbeddedLocalDiskImagePathRn = _CucsLsbootEmbeddedLocalDiskImagePathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 26, 1, 3),
    _CucsLsbootEmbeddedLocalDiskImagePathRn_Type()
)
cucsLsbootEmbeddedLocalDiskImagePathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalDiskImagePathRn.setStatus("current")
_CucsLsbootEmbeddedLocalDiskImagePathSlotNumber_Type = Gauge32
_CucsLsbootEmbeddedLocalDiskImagePathSlotNumber_Object = MibTableColumn
cucsLsbootEmbeddedLocalDiskImagePathSlotNumber = _CucsLsbootEmbeddedLocalDiskImagePathSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 26, 1, 4),
    _CucsLsbootEmbeddedLocalDiskImagePathSlotNumber_Type()
)
cucsLsbootEmbeddedLocalDiskImagePathSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalDiskImagePathSlotNumber.setStatus("current")
_CucsLsbootEmbeddedLocalDiskImagePathType_Type = CucsLsbootEmbeddedLocalDiskImagePathType
_CucsLsbootEmbeddedLocalDiskImagePathType_Object = MibTableColumn
cucsLsbootEmbeddedLocalDiskImagePathType = _CucsLsbootEmbeddedLocalDiskImagePathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 26, 1, 5),
    _CucsLsbootEmbeddedLocalDiskImagePathType_Type()
)
cucsLsbootEmbeddedLocalDiskImagePathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalDiskImagePathType.setStatus("current")
_CucsLsbootEmbeddedLocalLunImageTable_Object = MibTable
cucsLsbootEmbeddedLocalLunImageTable = _CucsLsbootEmbeddedLocalLunImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 27)
)
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalLunImageTable.setStatus("current")
_CucsLsbootEmbeddedLocalLunImageEntry_Object = MibTableRow
cucsLsbootEmbeddedLocalLunImageEntry = _CucsLsbootEmbeddedLocalLunImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 27, 1)
)
cucsLsbootEmbeddedLocalLunImageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB", "cucsLsbootEmbeddedLocalLunImageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalLunImageEntry.setStatus("current")
_CucsLsbootEmbeddedLocalLunImageInstanceId_Type = CucsManagedObjectId
_CucsLsbootEmbeddedLocalLunImageInstanceId_Object = MibTableColumn
cucsLsbootEmbeddedLocalLunImageInstanceId = _CucsLsbootEmbeddedLocalLunImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 27, 1, 1),
    _CucsLsbootEmbeddedLocalLunImageInstanceId_Type()
)
cucsLsbootEmbeddedLocalLunImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalLunImageInstanceId.setStatus("current")
_CucsLsbootEmbeddedLocalLunImageDn_Type = CucsManagedObjectDn
_CucsLsbootEmbeddedLocalLunImageDn_Object = MibTableColumn
cucsLsbootEmbeddedLocalLunImageDn = _CucsLsbootEmbeddedLocalLunImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 27, 1, 2),
    _CucsLsbootEmbeddedLocalLunImageDn_Type()
)
cucsLsbootEmbeddedLocalLunImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalLunImageDn.setStatus("current")
_CucsLsbootEmbeddedLocalLunImageRn_Type = SnmpAdminString
_CucsLsbootEmbeddedLocalLunImageRn_Object = MibTableColumn
cucsLsbootEmbeddedLocalLunImageRn = _CucsLsbootEmbeddedLocalLunImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 27, 1, 3),
    _CucsLsbootEmbeddedLocalLunImageRn_Type()
)
cucsLsbootEmbeddedLocalLunImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalLunImageRn.setStatus("current")
_CucsLsbootEmbeddedLocalLunImageOrder_Type = Gauge32
_CucsLsbootEmbeddedLocalLunImageOrder_Object = MibTableColumn
cucsLsbootEmbeddedLocalLunImageOrder = _CucsLsbootEmbeddedLocalLunImageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 27, 1, 4),
    _CucsLsbootEmbeddedLocalLunImageOrder_Type()
)
cucsLsbootEmbeddedLocalLunImageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalLunImageOrder.setStatus("current")
_CucsLsbootEmbeddedLocalLunImageType_Type = CucsLsbootEmbeddedLocalLunImageType
_CucsLsbootEmbeddedLocalLunImageType_Object = MibTableColumn
cucsLsbootEmbeddedLocalLunImageType = _CucsLsbootEmbeddedLocalLunImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 27, 27, 1, 5),
    _CucsLsbootEmbeddedLocalLunImageType_Type()
)
cucsLsbootEmbeddedLocalLunImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsbootEmbeddedLocalLunImageType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-LSBOOT-MIB",
    **{"cucsLsbootObjects": cucsLsbootObjects,
       "cucsLsbootDefTable": cucsLsbootDefTable,
       "cucsLsbootDefEntry": cucsLsbootDefEntry,
       "cucsLsbootDefInstanceId": cucsLsbootDefInstanceId,
       "cucsLsbootDefDn": cucsLsbootDefDn,
       "cucsLsbootDefRn": cucsLsbootDefRn,
       "cucsLsbootDefDescr": cucsLsbootDefDescr,
       "cucsLsbootDefEnforceVnicName": cucsLsbootDefEnforceVnicName,
       "cucsLsbootDefIntId": cucsLsbootDefIntId,
       "cucsLsbootDefName": cucsLsbootDefName,
       "cucsLsbootDefPurpose": cucsLsbootDefPurpose,
       "cucsLsbootDefRebootOnUpdate": cucsLsbootDefRebootOnUpdate,
       "cucsLsbootDefPolicyLevel": cucsLsbootDefPolicyLevel,
       "cucsLsbootDefPolicyOwner": cucsLsbootDefPolicyOwner,
       "cucsLsbootDefAdvBootOrderApplicable": cucsLsbootDefAdvBootOrderApplicable,
       "cucsLsbootDefBootMode": cucsLsbootDefBootMode,
       "cucsLsbootLanTable": cucsLsbootLanTable,
       "cucsLsbootLanEntry": cucsLsbootLanEntry,
       "cucsLsbootLanInstanceId": cucsLsbootLanInstanceId,
       "cucsLsbootLanDn": cucsLsbootLanDn,
       "cucsLsbootLanRn": cucsLsbootLanRn,
       "cucsLsbootLanAccess": cucsLsbootLanAccess,
       "cucsLsbootLanOrder": cucsLsbootLanOrder,
       "cucsLsbootLanType": cucsLsbootLanType,
       "cucsLsbootLanProt": cucsLsbootLanProt,
       "cucsLsbootLanImagePathTable": cucsLsbootLanImagePathTable,
       "cucsLsbootLanImagePathEntry": cucsLsbootLanImagePathEntry,
       "cucsLsbootLanImagePathInstanceId": cucsLsbootLanImagePathInstanceId,
       "cucsLsbootLanImagePathDn": cucsLsbootLanImagePathDn,
       "cucsLsbootLanImagePathRn": cucsLsbootLanImagePathRn,
       "cucsLsbootLanImagePathType": cucsLsbootLanImagePathType,
       "cucsLsbootLanImagePathVnicName": cucsLsbootLanImagePathVnicName,
       "cucsLsbootLanImagePathImgPolicyName": cucsLsbootLanImagePathImgPolicyName,
       "cucsLsbootLanImagePathImgSecPolicyName": cucsLsbootLanImagePathImgSecPolicyName,
       "cucsLsbootLanImagePathBootIpPolicyName": cucsLsbootLanImagePathBootIpPolicyName,
       "cucsLsbootLanImagePathProvSrvPolicyName": cucsLsbootLanImagePathProvSrvPolicyName,
       "cucsLsbootLanImagePathISCSIVnicName": cucsLsbootLanImagePathISCSIVnicName,
       "cucsLsbootLocalStorageTable": cucsLsbootLocalStorageTable,
       "cucsLsbootLocalStorageEntry": cucsLsbootLocalStorageEntry,
       "cucsLsbootLocalStorageInstanceId": cucsLsbootLocalStorageInstanceId,
       "cucsLsbootLocalStorageDn": cucsLsbootLocalStorageDn,
       "cucsLsbootLocalStorageRn": cucsLsbootLocalStorageRn,
       "cucsLsbootLocalStoragePropAcl": cucsLsbootLocalStoragePropAcl,
       "cucsLsbootPolicyTable": cucsLsbootPolicyTable,
       "cucsLsbootPolicyEntry": cucsLsbootPolicyEntry,
       "cucsLsbootPolicyInstanceId": cucsLsbootPolicyInstanceId,
       "cucsLsbootPolicyDn": cucsLsbootPolicyDn,
       "cucsLsbootPolicyRn": cucsLsbootPolicyRn,
       "cucsLsbootPolicyDescr": cucsLsbootPolicyDescr,
       "cucsLsbootPolicyEnforceVnicName": cucsLsbootPolicyEnforceVnicName,
       "cucsLsbootPolicyIntId": cucsLsbootPolicyIntId,
       "cucsLsbootPolicyName": cucsLsbootPolicyName,
       "cucsLsbootPolicyPurpose": cucsLsbootPolicyPurpose,
       "cucsLsbootPolicyRebootOnUpdate": cucsLsbootPolicyRebootOnUpdate,
       "cucsLsbootPolicyPolicyLevel": cucsLsbootPolicyPolicyLevel,
       "cucsLsbootPolicyPolicyOwner": cucsLsbootPolicyPolicyOwner,
       "cucsLsbootPolicyBootMode": cucsLsbootPolicyBootMode,
       "cucsLsbootPolicyPropAcl": cucsLsbootPolicyPropAcl,
       "cucsLsbootSanImageTable": cucsLsbootSanImageTable,
       "cucsLsbootSanImageEntry": cucsLsbootSanImageEntry,
       "cucsLsbootSanImageInstanceId": cucsLsbootSanImageInstanceId,
       "cucsLsbootSanImageDn": cucsLsbootSanImageDn,
       "cucsLsbootSanImageRn": cucsLsbootSanImageRn,
       "cucsLsbootSanImageType": cucsLsbootSanImageType,
       "cucsLsbootSanImageVnicName": cucsLsbootSanImageVnicName,
       "cucsLsbootSanImagePathTable": cucsLsbootSanImagePathTable,
       "cucsLsbootSanImagePathEntry": cucsLsbootSanImagePathEntry,
       "cucsLsbootSanImagePathInstanceId": cucsLsbootSanImagePathInstanceId,
       "cucsLsbootSanImagePathDn": cucsLsbootSanImagePathDn,
       "cucsLsbootSanImagePathRn": cucsLsbootSanImagePathRn,
       "cucsLsbootSanImagePathLun": cucsLsbootSanImagePathLun,
       "cucsLsbootSanImagePathType": cucsLsbootSanImagePathType,
       "cucsLsbootSanImagePathVnicName": cucsLsbootSanImagePathVnicName,
       "cucsLsbootSanImagePathWwn": cucsLsbootSanImagePathWwn,
       "cucsLsbootStorageTable": cucsLsbootStorageTable,
       "cucsLsbootStorageEntry": cucsLsbootStorageEntry,
       "cucsLsbootStorageInstanceId": cucsLsbootStorageInstanceId,
       "cucsLsbootStorageDn": cucsLsbootStorageDn,
       "cucsLsbootStorageRn": cucsLsbootStorageRn,
       "cucsLsbootStorageAccess": cucsLsbootStorageAccess,
       "cucsLsbootStorageOrder": cucsLsbootStorageOrder,
       "cucsLsbootStorageType": cucsLsbootStorageType,
       "cucsLsbootStoragePropAcl": cucsLsbootStoragePropAcl,
       "cucsLsbootVirtualMediaTable": cucsLsbootVirtualMediaTable,
       "cucsLsbootVirtualMediaEntry": cucsLsbootVirtualMediaEntry,
       "cucsLsbootVirtualMediaInstanceId": cucsLsbootVirtualMediaInstanceId,
       "cucsLsbootVirtualMediaDn": cucsLsbootVirtualMediaDn,
       "cucsLsbootVirtualMediaRn": cucsLsbootVirtualMediaRn,
       "cucsLsbootVirtualMediaAccess": cucsLsbootVirtualMediaAccess,
       "cucsLsbootVirtualMediaOrder": cucsLsbootVirtualMediaOrder,
       "cucsLsbootVirtualMediaType": cucsLsbootVirtualMediaType,
       "cucsLsbootVirtualMediaLunId": cucsLsbootVirtualMediaLunId,
       "cucsLsbootVirtualMediaMappingName": cucsLsbootVirtualMediaMappingName,
       "cucsLsbootVirtualMediaPropAcl": cucsLsbootVirtualMediaPropAcl,
       "cucsLsbootIScsiTable": cucsLsbootIScsiTable,
       "cucsLsbootIScsiEntry": cucsLsbootIScsiEntry,
       "cucsLsbootIScsiInstanceId": cucsLsbootIScsiInstanceId,
       "cucsLsbootIScsiDn": cucsLsbootIScsiDn,
       "cucsLsbootIScsiRn": cucsLsbootIScsiRn,
       "cucsLsbootIScsiAccess": cucsLsbootIScsiAccess,
       "cucsLsbootIScsiOrder": cucsLsbootIScsiOrder,
       "cucsLsbootIScsiType": cucsLsbootIScsiType,
       "cucsLsbootIScsiImagePathTable": cucsLsbootIScsiImagePathTable,
       "cucsLsbootIScsiImagePathEntry": cucsLsbootIScsiImagePathEntry,
       "cucsLsbootIScsiImagePathInstanceId": cucsLsbootIScsiImagePathInstanceId,
       "cucsLsbootIScsiImagePathDn": cucsLsbootIScsiImagePathDn,
       "cucsLsbootIScsiImagePathRn": cucsLsbootIScsiImagePathRn,
       "cucsLsbootIScsiImagePathISCSIVnicName": cucsLsbootIScsiImagePathISCSIVnicName,
       "cucsLsbootIScsiImagePathType": cucsLsbootIScsiImagePathType,
       "cucsLsbootIScsiImagePathVnicName": cucsLsbootIScsiImagePathVnicName,
       "cucsLsbootBootSecurityTable": cucsLsbootBootSecurityTable,
       "cucsLsbootBootSecurityEntry": cucsLsbootBootSecurityEntry,
       "cucsLsbootBootSecurityInstanceId": cucsLsbootBootSecurityInstanceId,
       "cucsLsbootBootSecurityDn": cucsLsbootBootSecurityDn,
       "cucsLsbootBootSecurityRn": cucsLsbootBootSecurityRn,
       "cucsLsbootBootSecuritySecureBoot": cucsLsbootBootSecuritySecureBoot,
       "cucsLsbootDefaultLocalImageTable": cucsLsbootDefaultLocalImageTable,
       "cucsLsbootDefaultLocalImageEntry": cucsLsbootDefaultLocalImageEntry,
       "cucsLsbootDefaultLocalImageInstanceId": cucsLsbootDefaultLocalImageInstanceId,
       "cucsLsbootDefaultLocalImageDn": cucsLsbootDefaultLocalImageDn,
       "cucsLsbootDefaultLocalImageRn": cucsLsbootDefaultLocalImageRn,
       "cucsLsbootDefaultLocalImageOrder": cucsLsbootDefaultLocalImageOrder,
       "cucsLsbootDefaultLocalImageType": cucsLsbootDefaultLocalImageType,
       "cucsLsbootDefaultLocalImagePropAcl": cucsLsbootDefaultLocalImagePropAcl,
       "cucsLsbootLocalHddImageTable": cucsLsbootLocalHddImageTable,
       "cucsLsbootLocalHddImageEntry": cucsLsbootLocalHddImageEntry,
       "cucsLsbootLocalHddImageInstanceId": cucsLsbootLocalHddImageInstanceId,
       "cucsLsbootLocalHddImageDn": cucsLsbootLocalHddImageDn,
       "cucsLsbootLocalHddImageRn": cucsLsbootLocalHddImageRn,
       "cucsLsbootLocalHddImageOrder": cucsLsbootLocalHddImageOrder,
       "cucsLsbootLocalHddImageType": cucsLsbootLocalHddImageType,
       "cucsLsbootSanTable": cucsLsbootSanTable,
       "cucsLsbootSanEntry": cucsLsbootSanEntry,
       "cucsLsbootSanInstanceId": cucsLsbootSanInstanceId,
       "cucsLsbootSanDn": cucsLsbootSanDn,
       "cucsLsbootSanRn": cucsLsbootSanRn,
       "cucsLsbootSanAccess": cucsLsbootSanAccess,
       "cucsLsbootSanOrder": cucsLsbootSanOrder,
       "cucsLsbootSanType": cucsLsbootSanType,
       "cucsLsbootSanCatSanImageTable": cucsLsbootSanCatSanImageTable,
       "cucsLsbootSanCatSanImageEntry": cucsLsbootSanCatSanImageEntry,
       "cucsLsbootSanCatSanImageInstanceId": cucsLsbootSanCatSanImageInstanceId,
       "cucsLsbootSanCatSanImageDn": cucsLsbootSanCatSanImageDn,
       "cucsLsbootSanCatSanImageRn": cucsLsbootSanCatSanImageRn,
       "cucsLsbootSanCatSanImageType": cucsLsbootSanCatSanImageType,
       "cucsLsbootSanCatSanImageVnicName": cucsLsbootSanCatSanImageVnicName,
       "cucsLsbootSanCatSanImagePathTable": cucsLsbootSanCatSanImagePathTable,
       "cucsLsbootSanCatSanImagePathEntry": cucsLsbootSanCatSanImagePathEntry,
       "cucsLsbootSanCatSanImagePathInstanceId": cucsLsbootSanCatSanImagePathInstanceId,
       "cucsLsbootSanCatSanImagePathDn": cucsLsbootSanCatSanImagePathDn,
       "cucsLsbootSanCatSanImagePathRn": cucsLsbootSanCatSanImagePathRn,
       "cucsLsbootSanCatSanImagePathLun": cucsLsbootSanCatSanImagePathLun,
       "cucsLsbootSanCatSanImagePathType": cucsLsbootSanCatSanImagePathType,
       "cucsLsbootSanCatSanImagePathVnicName": cucsLsbootSanCatSanImagePathVnicName,
       "cucsLsbootSanCatSanImagePathWwn": cucsLsbootSanCatSanImagePathWwn,
       "cucsLsbootUsbExternalImageTable": cucsLsbootUsbExternalImageTable,
       "cucsLsbootUsbExternalImageEntry": cucsLsbootUsbExternalImageEntry,
       "cucsLsbootUsbExternalImageInstanceId": cucsLsbootUsbExternalImageInstanceId,
       "cucsLsbootUsbExternalImageDn": cucsLsbootUsbExternalImageDn,
       "cucsLsbootUsbExternalImageRn": cucsLsbootUsbExternalImageRn,
       "cucsLsbootUsbExternalImageOrder": cucsLsbootUsbExternalImageOrder,
       "cucsLsbootUsbExternalImageType": cucsLsbootUsbExternalImageType,
       "cucsLsbootUsbFlashStorageImageTable": cucsLsbootUsbFlashStorageImageTable,
       "cucsLsbootUsbFlashStorageImageEntry": cucsLsbootUsbFlashStorageImageEntry,
       "cucsLsbootUsbFlashStorageImageInstanceId": cucsLsbootUsbFlashStorageImageInstanceId,
       "cucsLsbootUsbFlashStorageImageDn": cucsLsbootUsbFlashStorageImageDn,
       "cucsLsbootUsbFlashStorageImageRn": cucsLsbootUsbFlashStorageImageRn,
       "cucsLsbootUsbFlashStorageImageOrder": cucsLsbootUsbFlashStorageImageOrder,
       "cucsLsbootUsbFlashStorageImageType": cucsLsbootUsbFlashStorageImageType,
       "cucsLsbootUsbInternalImageTable": cucsLsbootUsbInternalImageTable,
       "cucsLsbootUsbInternalImageEntry": cucsLsbootUsbInternalImageEntry,
       "cucsLsbootUsbInternalImageInstanceId": cucsLsbootUsbInternalImageInstanceId,
       "cucsLsbootUsbInternalImageDn": cucsLsbootUsbInternalImageDn,
       "cucsLsbootUsbInternalImageRn": cucsLsbootUsbInternalImageRn,
       "cucsLsbootUsbInternalImageOrder": cucsLsbootUsbInternalImageOrder,
       "cucsLsbootUsbInternalImageType": cucsLsbootUsbInternalImageType,
       "cucsLsbootLocalDiskImageTable": cucsLsbootLocalDiskImageTable,
       "cucsLsbootLocalDiskImageEntry": cucsLsbootLocalDiskImageEntry,
       "cucsLsbootLocalDiskImageInstanceId": cucsLsbootLocalDiskImageInstanceId,
       "cucsLsbootLocalDiskImageDn": cucsLsbootLocalDiskImageDn,
       "cucsLsbootLocalDiskImageRn": cucsLsbootLocalDiskImageRn,
       "cucsLsbootLocalDiskImageOrder": cucsLsbootLocalDiskImageOrder,
       "cucsLsbootLocalDiskImageType": cucsLsbootLocalDiskImageType,
       "cucsLsbootLocalDiskImagePathTable": cucsLsbootLocalDiskImagePathTable,
       "cucsLsbootLocalDiskImagePathEntry": cucsLsbootLocalDiskImagePathEntry,
       "cucsLsbootLocalDiskImagePathInstanceId": cucsLsbootLocalDiskImagePathInstanceId,
       "cucsLsbootLocalDiskImagePathDn": cucsLsbootLocalDiskImagePathDn,
       "cucsLsbootLocalDiskImagePathRn": cucsLsbootLocalDiskImagePathRn,
       "cucsLsbootLocalDiskImagePathSlotNumber": cucsLsbootLocalDiskImagePathSlotNumber,
       "cucsLsbootLocalDiskImagePathType": cucsLsbootLocalDiskImagePathType,
       "cucsLsbootLocalLunImagePathTable": cucsLsbootLocalLunImagePathTable,
       "cucsLsbootLocalLunImagePathEntry": cucsLsbootLocalLunImagePathEntry,
       "cucsLsbootLocalLunImagePathInstanceId": cucsLsbootLocalLunImagePathInstanceId,
       "cucsLsbootLocalLunImagePathDn": cucsLsbootLocalLunImagePathDn,
       "cucsLsbootLocalLunImagePathRn": cucsLsbootLocalLunImagePathRn,
       "cucsLsbootLocalLunImagePathLunName": cucsLsbootLocalLunImagePathLunName,
       "cucsLsbootLocalLunImagePathType": cucsLsbootLocalLunImagePathType,
       "cucsLsbootUEFIBootParamTable": cucsLsbootUEFIBootParamTable,
       "cucsLsbootUEFIBootParamEntry": cucsLsbootUEFIBootParamEntry,
       "cucsLsbootUEFIBootParamInstanceId": cucsLsbootUEFIBootParamInstanceId,
       "cucsLsbootUEFIBootParamDn": cucsLsbootUEFIBootParamDn,
       "cucsLsbootUEFIBootParamRn": cucsLsbootUEFIBootParamRn,
       "cucsLsbootUEFIBootParamBootDescription": cucsLsbootUEFIBootParamBootDescription,
       "cucsLsbootUEFIBootParamBootLoaderName": cucsLsbootUEFIBootParamBootLoaderName,
       "cucsLsbootUEFIBootParamBootLoaderPath": cucsLsbootUEFIBootParamBootLoaderPath,
       "cucsLsbootEmbeddedLocalDiskImageTable": cucsLsbootEmbeddedLocalDiskImageTable,
       "cucsLsbootEmbeddedLocalDiskImageEntry": cucsLsbootEmbeddedLocalDiskImageEntry,
       "cucsLsbootEmbeddedLocalDiskImageInstanceId": cucsLsbootEmbeddedLocalDiskImageInstanceId,
       "cucsLsbootEmbeddedLocalDiskImageDn": cucsLsbootEmbeddedLocalDiskImageDn,
       "cucsLsbootEmbeddedLocalDiskImageRn": cucsLsbootEmbeddedLocalDiskImageRn,
       "cucsLsbootEmbeddedLocalDiskImageOrder": cucsLsbootEmbeddedLocalDiskImageOrder,
       "cucsLsbootEmbeddedLocalDiskImageType": cucsLsbootEmbeddedLocalDiskImageType,
       "cucsLsbootEmbeddedLocalDiskImagePathTable": cucsLsbootEmbeddedLocalDiskImagePathTable,
       "cucsLsbootEmbeddedLocalDiskImagePathEntry": cucsLsbootEmbeddedLocalDiskImagePathEntry,
       "cucsLsbootEmbeddedLocalDiskImagePathInstanceId": cucsLsbootEmbeddedLocalDiskImagePathInstanceId,
       "cucsLsbootEmbeddedLocalDiskImagePathDn": cucsLsbootEmbeddedLocalDiskImagePathDn,
       "cucsLsbootEmbeddedLocalDiskImagePathRn": cucsLsbootEmbeddedLocalDiskImagePathRn,
       "cucsLsbootEmbeddedLocalDiskImagePathSlotNumber": cucsLsbootEmbeddedLocalDiskImagePathSlotNumber,
       "cucsLsbootEmbeddedLocalDiskImagePathType": cucsLsbootEmbeddedLocalDiskImagePathType,
       "cucsLsbootEmbeddedLocalLunImageTable": cucsLsbootEmbeddedLocalLunImageTable,
       "cucsLsbootEmbeddedLocalLunImageEntry": cucsLsbootEmbeddedLocalLunImageEntry,
       "cucsLsbootEmbeddedLocalLunImageInstanceId": cucsLsbootEmbeddedLocalLunImageInstanceId,
       "cucsLsbootEmbeddedLocalLunImageDn": cucsLsbootEmbeddedLocalLunImageDn,
       "cucsLsbootEmbeddedLocalLunImageRn": cucsLsbootEmbeddedLocalLunImageRn,
       "cucsLsbootEmbeddedLocalLunImageOrder": cucsLsbootEmbeddedLocalLunImageOrder,
       "cucsLsbootEmbeddedLocalLunImageType": cucsLsbootEmbeddedLocalLunImageType}
)
