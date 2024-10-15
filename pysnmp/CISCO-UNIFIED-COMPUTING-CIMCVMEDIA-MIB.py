# SNMP MIB module (CISCO-UNIFIED-COMPUTING-CIMCVMEDIA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-CIMCVMEDIA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:08 2024
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

(CucsCimcvmediaAuthProtocol,
 CucsCimcvmediaDeviceType,
 CucsCimcvmediaErrorType,
 CucsCimcvmediaImageNameVariable,
 CucsCimcvmediaMountConfigRetryOnMountFail,
 CucsCimcvmediaMountStatus,
 CucsCimcvmediaTransport,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsCimcvmediaAuthProtocol",
    "CucsCimcvmediaDeviceType",
    "CucsCimcvmediaErrorType",
    "CucsCimcvmediaImageNameVariable",
    "CucsCimcvmediaMountConfigRetryOnMountFail",
    "CucsCimcvmediaMountStatus",
    "CucsCimcvmediaTransport",
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

cucsCimcvmediaObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsCimcvmediaActualMountEntryTable_Object = MibTable
cucsCimcvmediaActualMountEntryTable = _CucsCimcvmediaActualMountEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1)
)
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryTable.setStatus("current")
_CucsCimcvmediaActualMountEntryEntry_Object = MibTableRow
cucsCimcvmediaActualMountEntryEntry = _CucsCimcvmediaActualMountEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1)
)
cucsCimcvmediaActualMountEntryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CIMCVMEDIA-MIB", "cucsCimcvmediaActualMountEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryEntry.setStatus("current")
_CucsCimcvmediaActualMountEntryInstanceId_Type = CucsManagedObjectId
_CucsCimcvmediaActualMountEntryInstanceId_Object = MibTableColumn
cucsCimcvmediaActualMountEntryInstanceId = _CucsCimcvmediaActualMountEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 1),
    _CucsCimcvmediaActualMountEntryInstanceId_Type()
)
cucsCimcvmediaActualMountEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryInstanceId.setStatus("current")
_CucsCimcvmediaActualMountEntryDn_Type = CucsManagedObjectDn
_CucsCimcvmediaActualMountEntryDn_Object = MibTableColumn
cucsCimcvmediaActualMountEntryDn = _CucsCimcvmediaActualMountEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 2),
    _CucsCimcvmediaActualMountEntryDn_Type()
)
cucsCimcvmediaActualMountEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryDn.setStatus("current")
_CucsCimcvmediaActualMountEntryRn_Type = SnmpAdminString
_CucsCimcvmediaActualMountEntryRn_Object = MibTableColumn
cucsCimcvmediaActualMountEntryRn = _CucsCimcvmediaActualMountEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 3),
    _CucsCimcvmediaActualMountEntryRn_Type()
)
cucsCimcvmediaActualMountEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryRn.setStatus("current")
_CucsCimcvmediaActualMountEntryDeviceType_Type = CucsCimcvmediaDeviceType
_CucsCimcvmediaActualMountEntryDeviceType_Object = MibTableColumn
cucsCimcvmediaActualMountEntryDeviceType = _CucsCimcvmediaActualMountEntryDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 4),
    _CucsCimcvmediaActualMountEntryDeviceType_Type()
)
cucsCimcvmediaActualMountEntryDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryDeviceType.setStatus("current")
_CucsCimcvmediaActualMountEntryEncPwd_Type = SnmpAdminString
_CucsCimcvmediaActualMountEntryEncPwd_Object = MibTableColumn
cucsCimcvmediaActualMountEntryEncPwd = _CucsCimcvmediaActualMountEntryEncPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 5),
    _CucsCimcvmediaActualMountEntryEncPwd_Type()
)
cucsCimcvmediaActualMountEntryEncPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryEncPwd.setStatus("current")
_CucsCimcvmediaActualMountEntryErrorType_Type = CucsCimcvmediaErrorType
_CucsCimcvmediaActualMountEntryErrorType_Object = MibTableColumn
cucsCimcvmediaActualMountEntryErrorType = _CucsCimcvmediaActualMountEntryErrorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 6),
    _CucsCimcvmediaActualMountEntryErrorType_Type()
)
cucsCimcvmediaActualMountEntryErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryErrorType.setStatus("current")
_CucsCimcvmediaActualMountEntryImageFileName_Type = SnmpAdminString
_CucsCimcvmediaActualMountEntryImageFileName_Object = MibTableColumn
cucsCimcvmediaActualMountEntryImageFileName = _CucsCimcvmediaActualMountEntryImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 7),
    _CucsCimcvmediaActualMountEntryImageFileName_Type()
)
cucsCimcvmediaActualMountEntryImageFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryImageFileName.setStatus("current")
_CucsCimcvmediaActualMountEntryImagePath_Type = SnmpAdminString
_CucsCimcvmediaActualMountEntryImagePath_Object = MibTableColumn
cucsCimcvmediaActualMountEntryImagePath = _CucsCimcvmediaActualMountEntryImagePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 8),
    _CucsCimcvmediaActualMountEntryImagePath_Type()
)
cucsCimcvmediaActualMountEntryImagePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryImagePath.setStatus("current")
_CucsCimcvmediaActualMountEntryMappingName_Type = SnmpAdminString
_CucsCimcvmediaActualMountEntryMappingName_Object = MibTableColumn
cucsCimcvmediaActualMountEntryMappingName = _CucsCimcvmediaActualMountEntryMappingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 9),
    _CucsCimcvmediaActualMountEntryMappingName_Type()
)
cucsCimcvmediaActualMountEntryMappingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryMappingName.setStatus("current")
_CucsCimcvmediaActualMountEntryMountProtocol_Type = CucsCimcvmediaTransport
_CucsCimcvmediaActualMountEntryMountProtocol_Object = MibTableColumn
cucsCimcvmediaActualMountEntryMountProtocol = _CucsCimcvmediaActualMountEntryMountProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 10),
    _CucsCimcvmediaActualMountEntryMountProtocol_Type()
)
cucsCimcvmediaActualMountEntryMountProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryMountProtocol.setStatus("current")
_CucsCimcvmediaActualMountEntryOperMountStatus_Type = CucsCimcvmediaMountStatus
_CucsCimcvmediaActualMountEntryOperMountStatus_Object = MibTableColumn
cucsCimcvmediaActualMountEntryOperMountStatus = _CucsCimcvmediaActualMountEntryOperMountStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 11),
    _CucsCimcvmediaActualMountEntryOperMountStatus_Type()
)
cucsCimcvmediaActualMountEntryOperMountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryOperMountStatus.setStatus("current")
_CucsCimcvmediaActualMountEntryPassword_Type = SnmpAdminString
_CucsCimcvmediaActualMountEntryPassword_Object = MibTableColumn
cucsCimcvmediaActualMountEntryPassword = _CucsCimcvmediaActualMountEntryPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 12),
    _CucsCimcvmediaActualMountEntryPassword_Type()
)
cucsCimcvmediaActualMountEntryPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryPassword.setStatus("current")
_CucsCimcvmediaActualMountEntryPwdSet_Type = TruthValue
_CucsCimcvmediaActualMountEntryPwdSet_Object = MibTableColumn
cucsCimcvmediaActualMountEntryPwdSet = _CucsCimcvmediaActualMountEntryPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 13),
    _CucsCimcvmediaActualMountEntryPwdSet_Type()
)
cucsCimcvmediaActualMountEntryPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryPwdSet.setStatus("current")
_CucsCimcvmediaActualMountEntryRemoteHost_Type = SnmpAdminString
_CucsCimcvmediaActualMountEntryRemoteHost_Object = MibTableColumn
cucsCimcvmediaActualMountEntryRemoteHost = _CucsCimcvmediaActualMountEntryRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 14),
    _CucsCimcvmediaActualMountEntryRemoteHost_Type()
)
cucsCimcvmediaActualMountEntryRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryRemoteHost.setStatus("current")
_CucsCimcvmediaActualMountEntryRemoteIpAddress_Type = SnmpAdminString
_CucsCimcvmediaActualMountEntryRemoteIpAddress_Object = MibTableColumn
cucsCimcvmediaActualMountEntryRemoteIpAddress = _CucsCimcvmediaActualMountEntryRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 15),
    _CucsCimcvmediaActualMountEntryRemoteIpAddress_Type()
)
cucsCimcvmediaActualMountEntryRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryRemoteIpAddress.setStatus("current")
_CucsCimcvmediaActualMountEntryRemotePort_Type = Gauge32
_CucsCimcvmediaActualMountEntryRemotePort_Object = MibTableColumn
cucsCimcvmediaActualMountEntryRemotePort = _CucsCimcvmediaActualMountEntryRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 16),
    _CucsCimcvmediaActualMountEntryRemotePort_Type()
)
cucsCimcvmediaActualMountEntryRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryRemotePort.setStatus("current")
_CucsCimcvmediaActualMountEntryUserId_Type = SnmpAdminString
_CucsCimcvmediaActualMountEntryUserId_Object = MibTableColumn
cucsCimcvmediaActualMountEntryUserId = _CucsCimcvmediaActualMountEntryUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 17),
    _CucsCimcvmediaActualMountEntryUserId_Type()
)
cucsCimcvmediaActualMountEntryUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryUserId.setStatus("current")
_CucsCimcvmediaActualMountEntryVirtualDiskId_Type = Gauge32
_CucsCimcvmediaActualMountEntryVirtualDiskId_Object = MibTableColumn
cucsCimcvmediaActualMountEntryVirtualDiskId = _CucsCimcvmediaActualMountEntryVirtualDiskId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 18),
    _CucsCimcvmediaActualMountEntryVirtualDiskId_Type()
)
cucsCimcvmediaActualMountEntryVirtualDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryVirtualDiskId.setStatus("current")
_CucsCimcvmediaActualMountEntryAuthOption_Type = CucsCimcvmediaAuthProtocol
_CucsCimcvmediaActualMountEntryAuthOption_Object = MibTableColumn
cucsCimcvmediaActualMountEntryAuthOption = _CucsCimcvmediaActualMountEntryAuthOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 19),
    _CucsCimcvmediaActualMountEntryAuthOption_Type()
)
cucsCimcvmediaActualMountEntryAuthOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryAuthOption.setStatus("current")
_CucsCimcvmediaActualMountEntryImageNameVariable_Type = CucsCimcvmediaImageNameVariable
_CucsCimcvmediaActualMountEntryImageNameVariable_Object = MibTableColumn
cucsCimcvmediaActualMountEntryImageNameVariable = _CucsCimcvmediaActualMountEntryImageNameVariable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 1, 1, 20),
    _CucsCimcvmediaActualMountEntryImageNameVariable_Type()
)
cucsCimcvmediaActualMountEntryImageNameVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountEntryImageNameVariable.setStatus("current")
_CucsCimcvmediaActualMountListTable_Object = MibTable
cucsCimcvmediaActualMountListTable = _CucsCimcvmediaActualMountListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 2)
)
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountListTable.setStatus("current")
_CucsCimcvmediaActualMountListEntry_Object = MibTableRow
cucsCimcvmediaActualMountListEntry = _CucsCimcvmediaActualMountListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 2, 1)
)
cucsCimcvmediaActualMountListEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CIMCVMEDIA-MIB", "cucsCimcvmediaActualMountListInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountListEntry.setStatus("current")
_CucsCimcvmediaActualMountListInstanceId_Type = CucsManagedObjectId
_CucsCimcvmediaActualMountListInstanceId_Object = MibTableColumn
cucsCimcvmediaActualMountListInstanceId = _CucsCimcvmediaActualMountListInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 2, 1, 1),
    _CucsCimcvmediaActualMountListInstanceId_Type()
)
cucsCimcvmediaActualMountListInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountListInstanceId.setStatus("current")
_CucsCimcvmediaActualMountListDn_Type = CucsManagedObjectDn
_CucsCimcvmediaActualMountListDn_Object = MibTableColumn
cucsCimcvmediaActualMountListDn = _CucsCimcvmediaActualMountListDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 2, 1, 2),
    _CucsCimcvmediaActualMountListDn_Type()
)
cucsCimcvmediaActualMountListDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountListDn.setStatus("current")
_CucsCimcvmediaActualMountListRn_Type = SnmpAdminString
_CucsCimcvmediaActualMountListRn_Object = MibTableColumn
cucsCimcvmediaActualMountListRn = _CucsCimcvmediaActualMountListRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 2, 1, 3),
    _CucsCimcvmediaActualMountListRn_Type()
)
cucsCimcvmediaActualMountListRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaActualMountListRn.setStatus("current")
_CucsCimcvmediaConfigMountEntryTable_Object = MibTable
cucsCimcvmediaConfigMountEntryTable = _CucsCimcvmediaConfigMountEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3)
)
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryTable.setStatus("current")
_CucsCimcvmediaConfigMountEntryEntry_Object = MibTableRow
cucsCimcvmediaConfigMountEntryEntry = _CucsCimcvmediaConfigMountEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1)
)
cucsCimcvmediaConfigMountEntryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CIMCVMEDIA-MIB", "cucsCimcvmediaConfigMountEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryEntry.setStatus("current")
_CucsCimcvmediaConfigMountEntryInstanceId_Type = CucsManagedObjectId
_CucsCimcvmediaConfigMountEntryInstanceId_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryInstanceId = _CucsCimcvmediaConfigMountEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 1),
    _CucsCimcvmediaConfigMountEntryInstanceId_Type()
)
cucsCimcvmediaConfigMountEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryInstanceId.setStatus("current")
_CucsCimcvmediaConfigMountEntryDn_Type = CucsManagedObjectDn
_CucsCimcvmediaConfigMountEntryDn_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryDn = _CucsCimcvmediaConfigMountEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 2),
    _CucsCimcvmediaConfigMountEntryDn_Type()
)
cucsCimcvmediaConfigMountEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryDn.setStatus("current")
_CucsCimcvmediaConfigMountEntryRn_Type = SnmpAdminString
_CucsCimcvmediaConfigMountEntryRn_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryRn = _CucsCimcvmediaConfigMountEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 3),
    _CucsCimcvmediaConfigMountEntryRn_Type()
)
cucsCimcvmediaConfigMountEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryRn.setStatus("current")
_CucsCimcvmediaConfigMountEntryDescription_Type = SnmpAdminString
_CucsCimcvmediaConfigMountEntryDescription_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryDescription = _CucsCimcvmediaConfigMountEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 4),
    _CucsCimcvmediaConfigMountEntryDescription_Type()
)
cucsCimcvmediaConfigMountEntryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryDescription.setStatus("current")
_CucsCimcvmediaConfigMountEntryDeviceType_Type = CucsCimcvmediaDeviceType
_CucsCimcvmediaConfigMountEntryDeviceType_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryDeviceType = _CucsCimcvmediaConfigMountEntryDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 5),
    _CucsCimcvmediaConfigMountEntryDeviceType_Type()
)
cucsCimcvmediaConfigMountEntryDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryDeviceType.setStatus("current")
_CucsCimcvmediaConfigMountEntryEncPwd_Type = SnmpAdminString
_CucsCimcvmediaConfigMountEntryEncPwd_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryEncPwd = _CucsCimcvmediaConfigMountEntryEncPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 6),
    _CucsCimcvmediaConfigMountEntryEncPwd_Type()
)
cucsCimcvmediaConfigMountEntryEncPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryEncPwd.setStatus("current")
_CucsCimcvmediaConfigMountEntryImageFileName_Type = SnmpAdminString
_CucsCimcvmediaConfigMountEntryImageFileName_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryImageFileName = _CucsCimcvmediaConfigMountEntryImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 7),
    _CucsCimcvmediaConfigMountEntryImageFileName_Type()
)
cucsCimcvmediaConfigMountEntryImageFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryImageFileName.setStatus("current")
_CucsCimcvmediaConfigMountEntryImagePath_Type = SnmpAdminString
_CucsCimcvmediaConfigMountEntryImagePath_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryImagePath = _CucsCimcvmediaConfigMountEntryImagePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 8),
    _CucsCimcvmediaConfigMountEntryImagePath_Type()
)
cucsCimcvmediaConfigMountEntryImagePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryImagePath.setStatus("current")
_CucsCimcvmediaConfigMountEntryMappingName_Type = SnmpAdminString
_CucsCimcvmediaConfigMountEntryMappingName_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryMappingName = _CucsCimcvmediaConfigMountEntryMappingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 9),
    _CucsCimcvmediaConfigMountEntryMappingName_Type()
)
cucsCimcvmediaConfigMountEntryMappingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryMappingName.setStatus("current")
_CucsCimcvmediaConfigMountEntryMountProtocol_Type = CucsCimcvmediaTransport
_CucsCimcvmediaConfigMountEntryMountProtocol_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryMountProtocol = _CucsCimcvmediaConfigMountEntryMountProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 10),
    _CucsCimcvmediaConfigMountEntryMountProtocol_Type()
)
cucsCimcvmediaConfigMountEntryMountProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryMountProtocol.setStatus("current")
_CucsCimcvmediaConfigMountEntryPassword_Type = SnmpAdminString
_CucsCimcvmediaConfigMountEntryPassword_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryPassword = _CucsCimcvmediaConfigMountEntryPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 11),
    _CucsCimcvmediaConfigMountEntryPassword_Type()
)
cucsCimcvmediaConfigMountEntryPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryPassword.setStatus("current")
_CucsCimcvmediaConfigMountEntryPwdSet_Type = TruthValue
_CucsCimcvmediaConfigMountEntryPwdSet_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryPwdSet = _CucsCimcvmediaConfigMountEntryPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 12),
    _CucsCimcvmediaConfigMountEntryPwdSet_Type()
)
cucsCimcvmediaConfigMountEntryPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryPwdSet.setStatus("current")
_CucsCimcvmediaConfigMountEntryRemoteHost_Type = SnmpAdminString
_CucsCimcvmediaConfigMountEntryRemoteHost_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryRemoteHost = _CucsCimcvmediaConfigMountEntryRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 13),
    _CucsCimcvmediaConfigMountEntryRemoteHost_Type()
)
cucsCimcvmediaConfigMountEntryRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryRemoteHost.setStatus("current")
_CucsCimcvmediaConfigMountEntryRemoteIpAddress_Type = SnmpAdminString
_CucsCimcvmediaConfigMountEntryRemoteIpAddress_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryRemoteIpAddress = _CucsCimcvmediaConfigMountEntryRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 14),
    _CucsCimcvmediaConfigMountEntryRemoteIpAddress_Type()
)
cucsCimcvmediaConfigMountEntryRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryRemoteIpAddress.setStatus("current")
_CucsCimcvmediaConfigMountEntryRemotePort_Type = Gauge32
_CucsCimcvmediaConfigMountEntryRemotePort_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryRemotePort = _CucsCimcvmediaConfigMountEntryRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 15),
    _CucsCimcvmediaConfigMountEntryRemotePort_Type()
)
cucsCimcvmediaConfigMountEntryRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryRemotePort.setStatus("current")
_CucsCimcvmediaConfigMountEntryUserId_Type = SnmpAdminString
_CucsCimcvmediaConfigMountEntryUserId_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryUserId = _CucsCimcvmediaConfigMountEntryUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 16),
    _CucsCimcvmediaConfigMountEntryUserId_Type()
)
cucsCimcvmediaConfigMountEntryUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryUserId.setStatus("current")
_CucsCimcvmediaConfigMountEntryAuthOption_Type = CucsCimcvmediaAuthProtocol
_CucsCimcvmediaConfigMountEntryAuthOption_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryAuthOption = _CucsCimcvmediaConfigMountEntryAuthOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 17),
    _CucsCimcvmediaConfigMountEntryAuthOption_Type()
)
cucsCimcvmediaConfigMountEntryAuthOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryAuthOption.setStatus("current")
_CucsCimcvmediaConfigMountEntryImageNameVariable_Type = CucsCimcvmediaImageNameVariable
_CucsCimcvmediaConfigMountEntryImageNameVariable_Object = MibTableColumn
cucsCimcvmediaConfigMountEntryImageNameVariable = _CucsCimcvmediaConfigMountEntryImageNameVariable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 3, 1, 18),
    _CucsCimcvmediaConfigMountEntryImageNameVariable_Type()
)
cucsCimcvmediaConfigMountEntryImageNameVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaConfigMountEntryImageNameVariable.setStatus("current")
_CucsCimcvmediaExtMgmtRuleEntryTable_Object = MibTable
cucsCimcvmediaExtMgmtRuleEntryTable = _CucsCimcvmediaExtMgmtRuleEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 4)
)
if mibBuilder.loadTexts:
    cucsCimcvmediaExtMgmtRuleEntryTable.setStatus("current")
_CucsCimcvmediaExtMgmtRuleEntryEntry_Object = MibTableRow
cucsCimcvmediaExtMgmtRuleEntryEntry = _CucsCimcvmediaExtMgmtRuleEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 4, 1)
)
cucsCimcvmediaExtMgmtRuleEntryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CIMCVMEDIA-MIB", "cucsCimcvmediaExtMgmtRuleEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCimcvmediaExtMgmtRuleEntryEntry.setStatus("current")
_CucsCimcvmediaExtMgmtRuleEntryInstanceId_Type = CucsManagedObjectId
_CucsCimcvmediaExtMgmtRuleEntryInstanceId_Object = MibTableColumn
cucsCimcvmediaExtMgmtRuleEntryInstanceId = _CucsCimcvmediaExtMgmtRuleEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 4, 1, 1),
    _CucsCimcvmediaExtMgmtRuleEntryInstanceId_Type()
)
cucsCimcvmediaExtMgmtRuleEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCimcvmediaExtMgmtRuleEntryInstanceId.setStatus("current")
_CucsCimcvmediaExtMgmtRuleEntryDn_Type = CucsManagedObjectDn
_CucsCimcvmediaExtMgmtRuleEntryDn_Object = MibTableColumn
cucsCimcvmediaExtMgmtRuleEntryDn = _CucsCimcvmediaExtMgmtRuleEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 4, 1, 2),
    _CucsCimcvmediaExtMgmtRuleEntryDn_Type()
)
cucsCimcvmediaExtMgmtRuleEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaExtMgmtRuleEntryDn.setStatus("current")
_CucsCimcvmediaExtMgmtRuleEntryRn_Type = SnmpAdminString
_CucsCimcvmediaExtMgmtRuleEntryRn_Object = MibTableColumn
cucsCimcvmediaExtMgmtRuleEntryRn = _CucsCimcvmediaExtMgmtRuleEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 4, 1, 3),
    _CucsCimcvmediaExtMgmtRuleEntryRn_Type()
)
cucsCimcvmediaExtMgmtRuleEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaExtMgmtRuleEntryRn.setStatus("current")
_CucsCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr_Type = InetAddressIPv4
_CucsCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr_Object = MibTableColumn
cucsCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr = _CucsCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 4, 1, 4),
    _CucsCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr_Type()
)
cucsCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr.setStatus("current")
_CucsCimcvmediaExtMgmtRuleEntryMappingName_Type = SnmpAdminString
_CucsCimcvmediaExtMgmtRuleEntryMappingName_Object = MibTableColumn
cucsCimcvmediaExtMgmtRuleEntryMappingName = _CucsCimcvmediaExtMgmtRuleEntryMappingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 4, 1, 5),
    _CucsCimcvmediaExtMgmtRuleEntryMappingName_Type()
)
cucsCimcvmediaExtMgmtRuleEntryMappingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaExtMgmtRuleEntryMappingName.setStatus("current")
_CucsCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr_Type = InetAddressIPv4
_CucsCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr_Object = MibTableColumn
cucsCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr = _CucsCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 4, 1, 6),
    _CucsCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr_Type()
)
cucsCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr.setStatus("current")
_CucsCimcvmediaExtMgmtRuleEntryMountProtocol_Type = CucsCimcvmediaTransport
_CucsCimcvmediaExtMgmtRuleEntryMountProtocol_Object = MibTableColumn
cucsCimcvmediaExtMgmtRuleEntryMountProtocol = _CucsCimcvmediaExtMgmtRuleEntryMountProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 4, 1, 7),
    _CucsCimcvmediaExtMgmtRuleEntryMountProtocol_Type()
)
cucsCimcvmediaExtMgmtRuleEntryMountProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaExtMgmtRuleEntryMountProtocol.setStatus("current")
_CucsCimcvmediaExtMgmtRuleEntryRemoteIpAddr_Type = InetAddressIPv4
_CucsCimcvmediaExtMgmtRuleEntryRemoteIpAddr_Object = MibTableColumn
cucsCimcvmediaExtMgmtRuleEntryRemoteIpAddr = _CucsCimcvmediaExtMgmtRuleEntryRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 4, 1, 8),
    _CucsCimcvmediaExtMgmtRuleEntryRemoteIpAddr_Type()
)
cucsCimcvmediaExtMgmtRuleEntryRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaExtMgmtRuleEntryRemoteIpAddr.setStatus("current")
_CucsCimcvmediaExtMgmtRuleEntryRemotePort_Type = Gauge32
_CucsCimcvmediaExtMgmtRuleEntryRemotePort_Object = MibTableColumn
cucsCimcvmediaExtMgmtRuleEntryRemotePort = _CucsCimcvmediaExtMgmtRuleEntryRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 4, 1, 9),
    _CucsCimcvmediaExtMgmtRuleEntryRemotePort_Type()
)
cucsCimcvmediaExtMgmtRuleEntryRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaExtMgmtRuleEntryRemotePort.setStatus("current")
_CucsCimcvmediaMountConfigDefTable_Object = MibTable
cucsCimcvmediaMountConfigDefTable = _CucsCimcvmediaMountConfigDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 5)
)
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigDefTable.setStatus("current")
_CucsCimcvmediaMountConfigDefEntry_Object = MibTableRow
cucsCimcvmediaMountConfigDefEntry = _CucsCimcvmediaMountConfigDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 5, 1)
)
cucsCimcvmediaMountConfigDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CIMCVMEDIA-MIB", "cucsCimcvmediaMountConfigDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigDefEntry.setStatus("current")
_CucsCimcvmediaMountConfigDefInstanceId_Type = CucsManagedObjectId
_CucsCimcvmediaMountConfigDefInstanceId_Object = MibTableColumn
cucsCimcvmediaMountConfigDefInstanceId = _CucsCimcvmediaMountConfigDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 5, 1, 1),
    _CucsCimcvmediaMountConfigDefInstanceId_Type()
)
cucsCimcvmediaMountConfigDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigDefInstanceId.setStatus("current")
_CucsCimcvmediaMountConfigDefDn_Type = CucsManagedObjectDn
_CucsCimcvmediaMountConfigDefDn_Object = MibTableColumn
cucsCimcvmediaMountConfigDefDn = _CucsCimcvmediaMountConfigDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 5, 1, 2),
    _CucsCimcvmediaMountConfigDefDn_Type()
)
cucsCimcvmediaMountConfigDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigDefDn.setStatus("current")
_CucsCimcvmediaMountConfigDefRn_Type = SnmpAdminString
_CucsCimcvmediaMountConfigDefRn_Object = MibTableColumn
cucsCimcvmediaMountConfigDefRn = _CucsCimcvmediaMountConfigDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 5, 1, 3),
    _CucsCimcvmediaMountConfigDefRn_Type()
)
cucsCimcvmediaMountConfigDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigDefRn.setStatus("current")
_CucsCimcvmediaMountConfigDefDescr_Type = SnmpAdminString
_CucsCimcvmediaMountConfigDefDescr_Object = MibTableColumn
cucsCimcvmediaMountConfigDefDescr = _CucsCimcvmediaMountConfigDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 5, 1, 4),
    _CucsCimcvmediaMountConfigDefDescr_Type()
)
cucsCimcvmediaMountConfigDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigDefDescr.setStatus("current")
_CucsCimcvmediaMountConfigDefIntId_Type = SnmpAdminString
_CucsCimcvmediaMountConfigDefIntId_Object = MibTableColumn
cucsCimcvmediaMountConfigDefIntId = _CucsCimcvmediaMountConfigDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 5, 1, 5),
    _CucsCimcvmediaMountConfigDefIntId_Type()
)
cucsCimcvmediaMountConfigDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigDefIntId.setStatus("current")
_CucsCimcvmediaMountConfigDefName_Type = SnmpAdminString
_CucsCimcvmediaMountConfigDefName_Object = MibTableColumn
cucsCimcvmediaMountConfigDefName = _CucsCimcvmediaMountConfigDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 5, 1, 6),
    _CucsCimcvmediaMountConfigDefName_Type()
)
cucsCimcvmediaMountConfigDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigDefName.setStatus("current")
_CucsCimcvmediaMountConfigDefPolicyLevel_Type = Gauge32
_CucsCimcvmediaMountConfigDefPolicyLevel_Object = MibTableColumn
cucsCimcvmediaMountConfigDefPolicyLevel = _CucsCimcvmediaMountConfigDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 5, 1, 7),
    _CucsCimcvmediaMountConfigDefPolicyLevel_Type()
)
cucsCimcvmediaMountConfigDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigDefPolicyLevel.setStatus("current")
_CucsCimcvmediaMountConfigDefPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCimcvmediaMountConfigDefPolicyOwner_Object = MibTableColumn
cucsCimcvmediaMountConfigDefPolicyOwner = _CucsCimcvmediaMountConfigDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 5, 1, 8),
    _CucsCimcvmediaMountConfigDefPolicyOwner_Type()
)
cucsCimcvmediaMountConfigDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigDefPolicyOwner.setStatus("current")
_CucsCimcvmediaMountConfigDefRetryOnMountFail_Type = CucsCimcvmediaMountConfigRetryOnMountFail
_CucsCimcvmediaMountConfigDefRetryOnMountFail_Object = MibTableColumn
cucsCimcvmediaMountConfigDefRetryOnMountFail = _CucsCimcvmediaMountConfigDefRetryOnMountFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 5, 1, 9),
    _CucsCimcvmediaMountConfigDefRetryOnMountFail_Type()
)
cucsCimcvmediaMountConfigDefRetryOnMountFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigDefRetryOnMountFail.setStatus("current")
_CucsCimcvmediaMountConfigPolicyTable_Object = MibTable
cucsCimcvmediaMountConfigPolicyTable = _CucsCimcvmediaMountConfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 6)
)
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigPolicyTable.setStatus("current")
_CucsCimcvmediaMountConfigPolicyEntry_Object = MibTableRow
cucsCimcvmediaMountConfigPolicyEntry = _CucsCimcvmediaMountConfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 6, 1)
)
cucsCimcvmediaMountConfigPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CIMCVMEDIA-MIB", "cucsCimcvmediaMountConfigPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigPolicyEntry.setStatus("current")
_CucsCimcvmediaMountConfigPolicyInstanceId_Type = CucsManagedObjectId
_CucsCimcvmediaMountConfigPolicyInstanceId_Object = MibTableColumn
cucsCimcvmediaMountConfigPolicyInstanceId = _CucsCimcvmediaMountConfigPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 6, 1, 1),
    _CucsCimcvmediaMountConfigPolicyInstanceId_Type()
)
cucsCimcvmediaMountConfigPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigPolicyInstanceId.setStatus("current")
_CucsCimcvmediaMountConfigPolicyDn_Type = CucsManagedObjectDn
_CucsCimcvmediaMountConfigPolicyDn_Object = MibTableColumn
cucsCimcvmediaMountConfigPolicyDn = _CucsCimcvmediaMountConfigPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 6, 1, 2),
    _CucsCimcvmediaMountConfigPolicyDn_Type()
)
cucsCimcvmediaMountConfigPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigPolicyDn.setStatus("current")
_CucsCimcvmediaMountConfigPolicyRn_Type = SnmpAdminString
_CucsCimcvmediaMountConfigPolicyRn_Object = MibTableColumn
cucsCimcvmediaMountConfigPolicyRn = _CucsCimcvmediaMountConfigPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 6, 1, 3),
    _CucsCimcvmediaMountConfigPolicyRn_Type()
)
cucsCimcvmediaMountConfigPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigPolicyRn.setStatus("current")
_CucsCimcvmediaMountConfigPolicyDescr_Type = SnmpAdminString
_CucsCimcvmediaMountConfigPolicyDescr_Object = MibTableColumn
cucsCimcvmediaMountConfigPolicyDescr = _CucsCimcvmediaMountConfigPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 6, 1, 4),
    _CucsCimcvmediaMountConfigPolicyDescr_Type()
)
cucsCimcvmediaMountConfigPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigPolicyDescr.setStatus("current")
_CucsCimcvmediaMountConfigPolicyIntId_Type = SnmpAdminString
_CucsCimcvmediaMountConfigPolicyIntId_Object = MibTableColumn
cucsCimcvmediaMountConfigPolicyIntId = _CucsCimcvmediaMountConfigPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 6, 1, 5),
    _CucsCimcvmediaMountConfigPolicyIntId_Type()
)
cucsCimcvmediaMountConfigPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigPolicyIntId.setStatus("current")
_CucsCimcvmediaMountConfigPolicyName_Type = SnmpAdminString
_CucsCimcvmediaMountConfigPolicyName_Object = MibTableColumn
cucsCimcvmediaMountConfigPolicyName = _CucsCimcvmediaMountConfigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 6, 1, 6),
    _CucsCimcvmediaMountConfigPolicyName_Type()
)
cucsCimcvmediaMountConfigPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigPolicyName.setStatus("current")
_CucsCimcvmediaMountConfigPolicyPolicyLevel_Type = Gauge32
_CucsCimcvmediaMountConfigPolicyPolicyLevel_Object = MibTableColumn
cucsCimcvmediaMountConfigPolicyPolicyLevel = _CucsCimcvmediaMountConfigPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 6, 1, 7),
    _CucsCimcvmediaMountConfigPolicyPolicyLevel_Type()
)
cucsCimcvmediaMountConfigPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigPolicyPolicyLevel.setStatus("current")
_CucsCimcvmediaMountConfigPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCimcvmediaMountConfigPolicyPolicyOwner_Object = MibTableColumn
cucsCimcvmediaMountConfigPolicyPolicyOwner = _CucsCimcvmediaMountConfigPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 6, 1, 8),
    _CucsCimcvmediaMountConfigPolicyPolicyOwner_Type()
)
cucsCimcvmediaMountConfigPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigPolicyPolicyOwner.setStatus("current")
_CucsCimcvmediaMountConfigPolicyRetryOnMountFail_Type = CucsCimcvmediaMountConfigRetryOnMountFail
_CucsCimcvmediaMountConfigPolicyRetryOnMountFail_Object = MibTableColumn
cucsCimcvmediaMountConfigPolicyRetryOnMountFail = _CucsCimcvmediaMountConfigPolicyRetryOnMountFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 76, 6, 1, 9),
    _CucsCimcvmediaMountConfigPolicyRetryOnMountFail_Type()
)
cucsCimcvmediaMountConfigPolicyRetryOnMountFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCimcvmediaMountConfigPolicyRetryOnMountFail.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-CIMCVMEDIA-MIB",
    **{"cucsCimcvmediaObjects": cucsCimcvmediaObjects,
       "cucsCimcvmediaActualMountEntryTable": cucsCimcvmediaActualMountEntryTable,
       "cucsCimcvmediaActualMountEntryEntry": cucsCimcvmediaActualMountEntryEntry,
       "cucsCimcvmediaActualMountEntryInstanceId": cucsCimcvmediaActualMountEntryInstanceId,
       "cucsCimcvmediaActualMountEntryDn": cucsCimcvmediaActualMountEntryDn,
       "cucsCimcvmediaActualMountEntryRn": cucsCimcvmediaActualMountEntryRn,
       "cucsCimcvmediaActualMountEntryDeviceType": cucsCimcvmediaActualMountEntryDeviceType,
       "cucsCimcvmediaActualMountEntryEncPwd": cucsCimcvmediaActualMountEntryEncPwd,
       "cucsCimcvmediaActualMountEntryErrorType": cucsCimcvmediaActualMountEntryErrorType,
       "cucsCimcvmediaActualMountEntryImageFileName": cucsCimcvmediaActualMountEntryImageFileName,
       "cucsCimcvmediaActualMountEntryImagePath": cucsCimcvmediaActualMountEntryImagePath,
       "cucsCimcvmediaActualMountEntryMappingName": cucsCimcvmediaActualMountEntryMappingName,
       "cucsCimcvmediaActualMountEntryMountProtocol": cucsCimcvmediaActualMountEntryMountProtocol,
       "cucsCimcvmediaActualMountEntryOperMountStatus": cucsCimcvmediaActualMountEntryOperMountStatus,
       "cucsCimcvmediaActualMountEntryPassword": cucsCimcvmediaActualMountEntryPassword,
       "cucsCimcvmediaActualMountEntryPwdSet": cucsCimcvmediaActualMountEntryPwdSet,
       "cucsCimcvmediaActualMountEntryRemoteHost": cucsCimcvmediaActualMountEntryRemoteHost,
       "cucsCimcvmediaActualMountEntryRemoteIpAddress": cucsCimcvmediaActualMountEntryRemoteIpAddress,
       "cucsCimcvmediaActualMountEntryRemotePort": cucsCimcvmediaActualMountEntryRemotePort,
       "cucsCimcvmediaActualMountEntryUserId": cucsCimcvmediaActualMountEntryUserId,
       "cucsCimcvmediaActualMountEntryVirtualDiskId": cucsCimcvmediaActualMountEntryVirtualDiskId,
       "cucsCimcvmediaActualMountEntryAuthOption": cucsCimcvmediaActualMountEntryAuthOption,
       "cucsCimcvmediaActualMountEntryImageNameVariable": cucsCimcvmediaActualMountEntryImageNameVariable,
       "cucsCimcvmediaActualMountListTable": cucsCimcvmediaActualMountListTable,
       "cucsCimcvmediaActualMountListEntry": cucsCimcvmediaActualMountListEntry,
       "cucsCimcvmediaActualMountListInstanceId": cucsCimcvmediaActualMountListInstanceId,
       "cucsCimcvmediaActualMountListDn": cucsCimcvmediaActualMountListDn,
       "cucsCimcvmediaActualMountListRn": cucsCimcvmediaActualMountListRn,
       "cucsCimcvmediaConfigMountEntryTable": cucsCimcvmediaConfigMountEntryTable,
       "cucsCimcvmediaConfigMountEntryEntry": cucsCimcvmediaConfigMountEntryEntry,
       "cucsCimcvmediaConfigMountEntryInstanceId": cucsCimcvmediaConfigMountEntryInstanceId,
       "cucsCimcvmediaConfigMountEntryDn": cucsCimcvmediaConfigMountEntryDn,
       "cucsCimcvmediaConfigMountEntryRn": cucsCimcvmediaConfigMountEntryRn,
       "cucsCimcvmediaConfigMountEntryDescription": cucsCimcvmediaConfigMountEntryDescription,
       "cucsCimcvmediaConfigMountEntryDeviceType": cucsCimcvmediaConfigMountEntryDeviceType,
       "cucsCimcvmediaConfigMountEntryEncPwd": cucsCimcvmediaConfigMountEntryEncPwd,
       "cucsCimcvmediaConfigMountEntryImageFileName": cucsCimcvmediaConfigMountEntryImageFileName,
       "cucsCimcvmediaConfigMountEntryImagePath": cucsCimcvmediaConfigMountEntryImagePath,
       "cucsCimcvmediaConfigMountEntryMappingName": cucsCimcvmediaConfigMountEntryMappingName,
       "cucsCimcvmediaConfigMountEntryMountProtocol": cucsCimcvmediaConfigMountEntryMountProtocol,
       "cucsCimcvmediaConfigMountEntryPassword": cucsCimcvmediaConfigMountEntryPassword,
       "cucsCimcvmediaConfigMountEntryPwdSet": cucsCimcvmediaConfigMountEntryPwdSet,
       "cucsCimcvmediaConfigMountEntryRemoteHost": cucsCimcvmediaConfigMountEntryRemoteHost,
       "cucsCimcvmediaConfigMountEntryRemoteIpAddress": cucsCimcvmediaConfigMountEntryRemoteIpAddress,
       "cucsCimcvmediaConfigMountEntryRemotePort": cucsCimcvmediaConfigMountEntryRemotePort,
       "cucsCimcvmediaConfigMountEntryUserId": cucsCimcvmediaConfigMountEntryUserId,
       "cucsCimcvmediaConfigMountEntryAuthOption": cucsCimcvmediaConfigMountEntryAuthOption,
       "cucsCimcvmediaConfigMountEntryImageNameVariable": cucsCimcvmediaConfigMountEntryImageNameVariable,
       "cucsCimcvmediaExtMgmtRuleEntryTable": cucsCimcvmediaExtMgmtRuleEntryTable,
       "cucsCimcvmediaExtMgmtRuleEntryEntry": cucsCimcvmediaExtMgmtRuleEntryEntry,
       "cucsCimcvmediaExtMgmtRuleEntryInstanceId": cucsCimcvmediaExtMgmtRuleEntryInstanceId,
       "cucsCimcvmediaExtMgmtRuleEntryDn": cucsCimcvmediaExtMgmtRuleEntryDn,
       "cucsCimcvmediaExtMgmtRuleEntryRn": cucsCimcvmediaExtMgmtRuleEntryRn,
       "cucsCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr": cucsCimcvmediaExtMgmtRuleEntryExtMgmtIpAddr,
       "cucsCimcvmediaExtMgmtRuleEntryMappingName": cucsCimcvmediaExtMgmtRuleEntryMappingName,
       "cucsCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr": cucsCimcvmediaExtMgmtRuleEntryMgmtIfIpAddr,
       "cucsCimcvmediaExtMgmtRuleEntryMountProtocol": cucsCimcvmediaExtMgmtRuleEntryMountProtocol,
       "cucsCimcvmediaExtMgmtRuleEntryRemoteIpAddr": cucsCimcvmediaExtMgmtRuleEntryRemoteIpAddr,
       "cucsCimcvmediaExtMgmtRuleEntryRemotePort": cucsCimcvmediaExtMgmtRuleEntryRemotePort,
       "cucsCimcvmediaMountConfigDefTable": cucsCimcvmediaMountConfigDefTable,
       "cucsCimcvmediaMountConfigDefEntry": cucsCimcvmediaMountConfigDefEntry,
       "cucsCimcvmediaMountConfigDefInstanceId": cucsCimcvmediaMountConfigDefInstanceId,
       "cucsCimcvmediaMountConfigDefDn": cucsCimcvmediaMountConfigDefDn,
       "cucsCimcvmediaMountConfigDefRn": cucsCimcvmediaMountConfigDefRn,
       "cucsCimcvmediaMountConfigDefDescr": cucsCimcvmediaMountConfigDefDescr,
       "cucsCimcvmediaMountConfigDefIntId": cucsCimcvmediaMountConfigDefIntId,
       "cucsCimcvmediaMountConfigDefName": cucsCimcvmediaMountConfigDefName,
       "cucsCimcvmediaMountConfigDefPolicyLevel": cucsCimcvmediaMountConfigDefPolicyLevel,
       "cucsCimcvmediaMountConfigDefPolicyOwner": cucsCimcvmediaMountConfigDefPolicyOwner,
       "cucsCimcvmediaMountConfigDefRetryOnMountFail": cucsCimcvmediaMountConfigDefRetryOnMountFail,
       "cucsCimcvmediaMountConfigPolicyTable": cucsCimcvmediaMountConfigPolicyTable,
       "cucsCimcvmediaMountConfigPolicyEntry": cucsCimcvmediaMountConfigPolicyEntry,
       "cucsCimcvmediaMountConfigPolicyInstanceId": cucsCimcvmediaMountConfigPolicyInstanceId,
       "cucsCimcvmediaMountConfigPolicyDn": cucsCimcvmediaMountConfigPolicyDn,
       "cucsCimcvmediaMountConfigPolicyRn": cucsCimcvmediaMountConfigPolicyRn,
       "cucsCimcvmediaMountConfigPolicyDescr": cucsCimcvmediaMountConfigPolicyDescr,
       "cucsCimcvmediaMountConfigPolicyIntId": cucsCimcvmediaMountConfigPolicyIntId,
       "cucsCimcvmediaMountConfigPolicyName": cucsCimcvmediaMountConfigPolicyName,
       "cucsCimcvmediaMountConfigPolicyPolicyLevel": cucsCimcvmediaMountConfigPolicyPolicyLevel,
       "cucsCimcvmediaMountConfigPolicyPolicyOwner": cucsCimcvmediaMountConfigPolicyPolicyOwner,
       "cucsCimcvmediaMountConfigPolicyRetryOnMountFail": cucsCimcvmediaMountConfigPolicyRetryOnMountFail}
)
