# SNMP MIB module (CISCO-SMART-INSTALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SMART-INSTALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:25 2024
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

(Cisco2KVlanList,
 CiscoURLStringOrEmpty,
 TimeIntervalMin) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Cisco2KVlanList",
    "CiscoURLStringOrEmpty",
    "TimeIntervalMin")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSmartInstallMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 725)
)
ciscoSmartInstallMIB.setRevisions(
        ("2010-04-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSmartInstallMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSmartInstallMIBNotifs = _CiscoSmartInstallMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 0)
)
_CiscoSmartInstallMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSmartInstallMIBObjects = _CiscoSmartInstallMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1)
)
_CsiGlobalConfig_ObjectIdentity = ObjectIdentity
csiGlobalConfig = _CsiGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1)
)


class _CsiOperationMode_Type(Integer32):
    """Custom type csiOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 2),
          ("disabled", 1))
    )


_CsiOperationMode_Type.__name__ = "Integer32"
_CsiOperationMode_Object = MibScalar
csiOperationMode = _CsiOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 1),
    _CsiOperationMode_Type()
)
csiOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csiOperationMode.setStatus("current")
_CsiDirectorIpAddressType_Type = InetAddressType
_CsiDirectorIpAddressType_Object = MibScalar
csiDirectorIpAddressType = _CsiDirectorIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 2),
    _CsiDirectorIpAddressType_Type()
)
csiDirectorIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csiDirectorIpAddressType.setStatus("current")
_CsiDirectorIpAddress_Type = InetAddress
_CsiDirectorIpAddress_Object = MibScalar
csiDirectorIpAddress = _CsiDirectorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 3),
    _CsiDirectorIpAddress_Type()
)
csiDirectorIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csiDirectorIpAddress.setStatus("current")
_CsiManagementVlan_Type = TruthValue
_CsiManagementVlan_Object = MibScalar
csiManagementVlan = _CsiManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 4),
    _CsiManagementVlan_Type()
)
csiManagementVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiManagementVlan.setStatus("current")
_CsiManagementVlansFirst2K_Type = Cisco2KVlanList
_CsiManagementVlansFirst2K_Object = MibScalar
csiManagementVlansFirst2K = _CsiManagementVlansFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 5),
    _CsiManagementVlansFirst2K_Type()
)
csiManagementVlansFirst2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csiManagementVlansFirst2K.setStatus("current")
_CsiManagementVlansSecond2K_Type = Cisco2KVlanList
_CsiManagementVlansSecond2K_Object = MibScalar
csiManagementVlansSecond2K = _CsiManagementVlansSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 6),
    _CsiManagementVlansSecond2K_Type()
)
csiManagementVlansSecond2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csiManagementVlansSecond2K.setStatus("current")
_CsiBackup_ObjectIdentity = ObjectIdentity
csiBackup = _CsiBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 7)
)
_CsiBackupHostUrl_Type = CiscoURLStringOrEmpty
_CsiBackupHostUrl_Object = MibScalar
csiBackupHostUrl = _CsiBackupHostUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 7, 1),
    _CsiBackupHostUrl_Type()
)
csiBackupHostUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csiBackupHostUrl.setStatus("current")
_CsiBackupEnable_Type = TruthValue
_CsiBackupEnable_Object = MibScalar
csiBackupEnable = _CsiBackupEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 7, 2),
    _CsiBackupEnable_Type()
)
csiBackupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csiBackupEnable.setStatus("current")
_CsiJoinWindow_ObjectIdentity = ObjectIdentity
csiJoinWindow = _CsiJoinWindow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 8)
)


class _CsiJoinWindowConfigOperationMode_Type(Integer32):
    """Custom type csiJoinWindowConfigOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("closed", 1),
          ("manual", 3))
    )


_CsiJoinWindowConfigOperationMode_Type.__name__ = "Integer32"
_CsiJoinWindowConfigOperationMode_Object = MibScalar
csiJoinWindowConfigOperationMode = _CsiJoinWindowConfigOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 8, 1),
    _CsiJoinWindowConfigOperationMode_Type()
)
csiJoinWindowConfigOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csiJoinWindowConfigOperationMode.setStatus("current")


class _CsiJoinWindowPeriodNextFreeIndex_Type(Unsigned32):
    """Custom type csiJoinWindowPeriodNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CsiJoinWindowPeriodNextFreeIndex_Type.__name__ = "Unsigned32"
_CsiJoinWindowPeriodNextFreeIndex_Object = MibScalar
csiJoinWindowPeriodNextFreeIndex = _CsiJoinWindowPeriodNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 8, 2),
    _CsiJoinWindowPeriodNextFreeIndex_Type()
)
csiJoinWindowPeriodNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiJoinWindowPeriodNextFreeIndex.setStatus("current")
_CsiJoinWindowPeriodTable_Object = MibTable
csiJoinWindowPeriodTable = _CsiJoinWindowPeriodTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 8, 3)
)
if mibBuilder.loadTexts:
    csiJoinWindowPeriodTable.setStatus("current")
_CsiJoinWindowPeriodEntry_Object = MibTableRow
csiJoinWindowPeriodEntry = _CsiJoinWindowPeriodEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 8, 3, 1)
)
csiJoinWindowPeriodEntry.setIndexNames(
    (0, "CISCO-SMART-INSTALL-MIB", "csiJoinWindowPeriodIndex"),
)
if mibBuilder.loadTexts:
    csiJoinWindowPeriodEntry.setStatus("current")
_CsiJoinWindowPeriodIndex_Type = Unsigned32
_CsiJoinWindowPeriodIndex_Object = MibTableColumn
csiJoinWindowPeriodIndex = _CsiJoinWindowPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 8, 3, 1, 1),
    _CsiJoinWindowPeriodIndex_Type()
)
csiJoinWindowPeriodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csiJoinWindowPeriodIndex.setStatus("current")
_CsiJoinWindowPeriodStartTime_Type = DateAndTime
_CsiJoinWindowPeriodStartTime_Object = MibTableColumn
csiJoinWindowPeriodStartTime = _CsiJoinWindowPeriodStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 8, 3, 1, 2),
    _CsiJoinWindowPeriodStartTime_Type()
)
csiJoinWindowPeriodStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiJoinWindowPeriodStartTime.setStatus("current")
_CsiJoinWindowPeriodInterval_Type = TimeIntervalMin
_CsiJoinWindowPeriodInterval_Object = MibTableColumn
csiJoinWindowPeriodInterval = _CsiJoinWindowPeriodInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 8, 3, 1, 3),
    _CsiJoinWindowPeriodInterval_Type()
)
csiJoinWindowPeriodInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiJoinWindowPeriodInterval.setStatus("current")


class _CsiJoinWindowPeriodRecurrencePattern_Type(Integer32):
    """Custom type csiJoinWindowPeriodRecurrencePattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("daily", 2),
          ("none", 1))
    )


_CsiJoinWindowPeriodRecurrencePattern_Type.__name__ = "Integer32"
_CsiJoinWindowPeriodRecurrencePattern_Object = MibTableColumn
csiJoinWindowPeriodRecurrencePattern = _CsiJoinWindowPeriodRecurrencePattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 8, 3, 1, 4),
    _CsiJoinWindowPeriodRecurrencePattern_Type()
)
csiJoinWindowPeriodRecurrencePattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiJoinWindowPeriodRecurrencePattern.setStatus("current")
_CsiJoinWindowPeriodExpirationDate_Type = DateAndTime
_CsiJoinWindowPeriodExpirationDate_Object = MibTableColumn
csiJoinWindowPeriodExpirationDate = _CsiJoinWindowPeriodExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 8, 3, 1, 5),
    _CsiJoinWindowPeriodExpirationDate_Type()
)
csiJoinWindowPeriodExpirationDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiJoinWindowPeriodExpirationDate.setStatus("current")


class _CsiJoinWindowPeriodStorageType_Type(StorageType):
    """Custom type csiJoinWindowPeriodStorageType based on StorageType"""


_CsiJoinWindowPeriodStorageType_Object = MibTableColumn
csiJoinWindowPeriodStorageType = _CsiJoinWindowPeriodStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 8, 3, 1, 6),
    _CsiJoinWindowPeriodStorageType_Type()
)
csiJoinWindowPeriodStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiJoinWindowPeriodStorageType.setStatus("current")
_CsiJoinWindowPeriodRowStatus_Type = RowStatus
_CsiJoinWindowPeriodRowStatus_Object = MibTableColumn
csiJoinWindowPeriodRowStatus = _CsiJoinWindowPeriodRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 1, 8, 3, 1, 7),
    _CsiJoinWindowPeriodRowStatus_Type()
)
csiJoinWindowPeriodRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiJoinWindowPeriodRowStatus.setStatus("current")
_CsiProfile_ObjectIdentity = ObjectIdentity
csiProfile = _CsiProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2)
)
_CsiImageFileUrl_Type = CiscoURLStringOrEmpty
_CsiImageFileUrl_Object = MibScalar
csiImageFileUrl = _CsiImageFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 1),
    _CsiImageFileUrl_Type()
)
csiImageFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csiImageFileUrl.setStatus("current")
_CsiConfigFileUrl_Type = CiscoURLStringOrEmpty
_CsiConfigFileUrl_Object = MibScalar
csiConfigFileUrl = _CsiConfigFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 2),
    _CsiConfigFileUrl_Type()
)
csiConfigFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csiConfigFileUrl.setStatus("current")


class _CsiHostnamePrefix_Type(SnmpAdminString):
    """Custom type csiHostnamePrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CsiHostnamePrefix_Type.__name__ = "SnmpAdminString"
_CsiHostnamePrefix_Object = MibScalar
csiHostnamePrefix = _CsiHostnamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 3),
    _CsiHostnamePrefix_Type()
)
csiHostnamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csiHostnamePrefix.setStatus("current")


class _CsiProfileNextFreeIndex_Type(Unsigned32):
    """Custom type csiProfileNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4294967295),
    )


_CsiProfileNextFreeIndex_Type.__name__ = "Unsigned32"
_CsiProfileNextFreeIndex_Object = MibScalar
csiProfileNextFreeIndex = _CsiProfileNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 4),
    _CsiProfileNextFreeIndex_Type()
)
csiProfileNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiProfileNextFreeIndex.setStatus("current")
_CsiProfileTable_Object = MibTable
csiProfileTable = _CsiProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 5)
)
if mibBuilder.loadTexts:
    csiProfileTable.setStatus("current")
_CsiProfileEntry_Object = MibTableRow
csiProfileEntry = _CsiProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 5, 1)
)
csiProfileEntry.setIndexNames(
    (0, "CISCO-SMART-INSTALL-MIB", "csiProfileIndex"),
)
if mibBuilder.loadTexts:
    csiProfileEntry.setStatus("current")
_CsiProfileIndex_Type = Unsigned32
_CsiProfileIndex_Object = MibTableColumn
csiProfileIndex = _CsiProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 5, 1, 1),
    _CsiProfileIndex_Type()
)
csiProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csiProfileIndex.setStatus("current")


class _CsiProfileGroupName_Type(SnmpAdminString):
    """Custom type csiProfileGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CsiProfileGroupName_Type.__name__ = "SnmpAdminString"
_CsiProfileGroupName_Object = MibTableColumn
csiProfileGroupName = _CsiProfileGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 5, 1, 2),
    _CsiProfileGroupName_Type()
)
csiProfileGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiProfileGroupName.setStatus("current")
_CsiProfileImageUrl_Type = CiscoURLStringOrEmpty
_CsiProfileImageUrl_Object = MibTableColumn
csiProfileImageUrl = _CsiProfileImageUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 5, 1, 3),
    _CsiProfileImageUrl_Type()
)
csiProfileImageUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiProfileImageUrl.setStatus("current")
_CsiProfileImageTwoUrl_Type = CiscoURLStringOrEmpty
_CsiProfileImageTwoUrl_Object = MibTableColumn
csiProfileImageTwoUrl = _CsiProfileImageTwoUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 5, 1, 4),
    _CsiProfileImageTwoUrl_Type()
)
csiProfileImageTwoUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiProfileImageTwoUrl.setStatus("current")
_CsiProfileConfigUrl_Type = CiscoURLStringOrEmpty
_CsiProfileConfigUrl_Object = MibTableColumn
csiProfileConfigUrl = _CsiProfileConfigUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 5, 1, 5),
    _CsiProfileConfigUrl_Type()
)
csiProfileConfigUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiProfileConfigUrl.setStatus("current")


class _CsiProfileStorageType_Type(StorageType):
    """Custom type csiProfileStorageType based on StorageType"""


_CsiProfileStorageType_Object = MibTableColumn
csiProfileStorageType = _CsiProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 5, 1, 6),
    _CsiProfileStorageType_Type()
)
csiProfileStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiProfileStorageType.setStatus("current")
_CsiProfileRowStatus_Type = RowStatus
_CsiProfileRowStatus_Object = MibTableColumn
csiProfileRowStatus = _CsiProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 5, 1, 7),
    _CsiProfileRowStatus_Type()
)
csiProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiProfileRowStatus.setStatus("current")
_CsiMatchTable_Object = MibTable
csiMatchTable = _CsiMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 6)
)
if mibBuilder.loadTexts:
    csiMatchTable.setStatus("current")
_CsiMatchEntry_Object = MibTableRow
csiMatchEntry = _CsiMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 6, 1)
)
csiMatchEntry.setIndexNames(
    (0, "CISCO-SMART-INSTALL-MIB", "csiProfileIndex"),
    (0, "CISCO-SMART-INSTALL-MIB", "csiMatchIndex"),
)
if mibBuilder.loadTexts:
    csiMatchEntry.setStatus("current")
_CsiMatchIndex_Type = Unsigned32
_CsiMatchIndex_Object = MibTableColumn
csiMatchIndex = _CsiMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 6, 1, 1),
    _CsiMatchIndex_Type()
)
csiMatchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csiMatchIndex.setStatus("current")


class _CsiMatchGroupType_Type(Integer32):
    """Custom type csiMatchGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("connectivity", 3),
          ("mac", 2),
          ("product", 4),
          ("stack", 5),
          ("unknown", 1))
    )


_CsiMatchGroupType_Type.__name__ = "Integer32"
_CsiMatchGroupType_Object = MibTableColumn
csiMatchGroupType = _CsiMatchGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 6, 1, 2),
    _CsiMatchGroupType_Type()
)
csiMatchGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiMatchGroupType.setStatus("current")
_CsiMatchMacAddress_Type = MacAddress
_CsiMatchMacAddress_Object = MibTableColumn
csiMatchMacAddress = _CsiMatchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 6, 1, 3),
    _CsiMatchMacAddress_Type()
)
csiMatchMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiMatchMacAddress.setStatus("current")
_CsiMatchHostAddressType_Type = InetAddressType
_CsiMatchHostAddressType_Object = MibTableColumn
csiMatchHostAddressType = _CsiMatchHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 6, 1, 4),
    _CsiMatchHostAddressType_Type()
)
csiMatchHostAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiMatchHostAddressType.setStatus("current")
_CsiMatchHostAddress_Type = InetAddress
_CsiMatchHostAddress_Object = MibTableColumn
csiMatchHostAddress = _CsiMatchHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 6, 1, 5),
    _CsiMatchHostAddress_Type()
)
csiMatchHostAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiMatchHostAddress.setStatus("current")
_CsiMatchHostInterface_Type = SnmpAdminString
_CsiMatchHostInterface_Object = MibTableColumn
csiMatchHostInterface = _CsiMatchHostInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 6, 1, 6),
    _CsiMatchHostInterface_Type()
)
csiMatchHostInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiMatchHostInterface.setStatus("current")
_CsiMatchProductId_Type = SnmpAdminString
_CsiMatchProductId_Object = MibTableColumn
csiMatchProductId = _CsiMatchProductId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 6, 1, 7),
    _CsiMatchProductId_Type()
)
csiMatchProductId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiMatchProductId.setStatus("current")
_CsiMatchSwitchNum_Type = Unsigned32
_CsiMatchSwitchNum_Object = MibTableColumn
csiMatchSwitchNum = _CsiMatchSwitchNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 6, 1, 8),
    _CsiMatchSwitchNum_Type()
)
csiMatchSwitchNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiMatchSwitchNum.setStatus("current")
_CsiMatchSwitchProductId_Type = SnmpAdminString
_CsiMatchSwitchProductId_Object = MibTableColumn
csiMatchSwitchProductId = _CsiMatchSwitchProductId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 6, 1, 9),
    _CsiMatchSwitchProductId_Type()
)
csiMatchSwitchProductId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiMatchSwitchProductId.setStatus("current")


class _CsiMatchStorageType_Type(StorageType):
    """Custom type csiMatchStorageType based on StorageType"""


_CsiMatchStorageType_Object = MibTableColumn
csiMatchStorageType = _CsiMatchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 6, 1, 10),
    _CsiMatchStorageType_Type()
)
csiMatchStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiMatchStorageType.setStatus("current")
_CsiMatchRowStatus_Type = RowStatus
_CsiMatchRowStatus_Object = MibTableColumn
csiMatchRowStatus = _CsiMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 2, 6, 1, 11),
    _CsiMatchRowStatus_Type()
)
csiMatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csiMatchRowStatus.setStatus("current")
_CsiDeviceInfo_ObjectIdentity = ObjectIdentity
csiDeviceInfo = _CsiDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 3)
)
_CsiDeviceTable_Object = MibTable
csiDeviceTable = _CsiDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 3, 1)
)
if mibBuilder.loadTexts:
    csiDeviceTable.setStatus("current")
_CsiDeviceEntry_Object = MibTableRow
csiDeviceEntry = _CsiDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 3, 1, 1)
)
csiDeviceEntry.setIndexNames(
    (0, "CISCO-SMART-INSTALL-MIB", "csiDeviceNum"),
)
if mibBuilder.loadTexts:
    csiDeviceEntry.setStatus("current")
_CsiDeviceNum_Type = Unsigned32
_CsiDeviceNum_Object = MibTableColumn
csiDeviceNum = _CsiDeviceNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 3, 1, 1, 1),
    _CsiDeviceNum_Type()
)
csiDeviceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csiDeviceNum.setStatus("current")
_CsiDeviceMacAddress_Type = MacAddress
_CsiDeviceMacAddress_Object = MibTableColumn
csiDeviceMacAddress = _CsiDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 3, 1, 1, 2),
    _CsiDeviceMacAddress_Type()
)
csiDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiDeviceMacAddress.setStatus("current")
_CsiDeviceAddressType_Type = InetAddressType
_CsiDeviceAddressType_Object = MibTableColumn
csiDeviceAddressType = _CsiDeviceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 3, 1, 1, 3),
    _CsiDeviceAddressType_Type()
)
csiDeviceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiDeviceAddressType.setStatus("current")
_CsiDeviceAddress_Type = InetAddress
_CsiDeviceAddress_Object = MibTableColumn
csiDeviceAddress = _CsiDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 3, 1, 1, 4),
    _CsiDeviceAddress_Type()
)
csiDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiDeviceAddress.setStatus("current")
_CsiDeviceName_Type = SnmpAdminString
_CsiDeviceName_Object = MibTableColumn
csiDeviceName = _CsiDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 3, 1, 1, 5),
    _CsiDeviceName_Type()
)
csiDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiDeviceName.setStatus("current")
_CsiDeviceBackupConfigFileName_Type = SnmpAdminString
_CsiDeviceBackupConfigFileName_Object = MibTableColumn
csiDeviceBackupConfigFileName = _CsiDeviceBackupConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 3, 1, 1, 6),
    _CsiDeviceBackupConfigFileName_Type()
)
csiDeviceBackupConfigFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiDeviceBackupConfigFileName.setStatus("current")
_CsiDeviceImageVersion_Type = SnmpAdminString
_CsiDeviceImageVersion_Object = MibTableColumn
csiDeviceImageVersion = _CsiDeviceImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 3, 1, 1, 7),
    _CsiDeviceImageVersion_Type()
)
csiDeviceImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiDeviceImageVersion.setStatus("current")
_CsiDevicePlatform_Type = SnmpAdminString
_CsiDevicePlatform_Object = MibTableColumn
csiDevicePlatform = _CsiDevicePlatform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 3, 1, 1, 8),
    _CsiDevicePlatform_Type()
)
csiDevicePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiDevicePlatform.setStatus("current")
_CsiDeviceSerialNum_Type = SnmpAdminString
_CsiDeviceSerialNum_Object = MibTableColumn
csiDeviceSerialNum = _CsiDeviceSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 3, 1, 1, 9),
    _CsiDeviceSerialNum_Type()
)
csiDeviceSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiDeviceSerialNum.setStatus("current")
_CsiDeviceStatus_Type = SnmpAdminString
_CsiDeviceStatus_Object = MibTableColumn
csiDeviceStatus = _CsiDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 3, 1, 1, 10),
    _CsiDeviceStatus_Type()
)
csiDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiDeviceStatus.setStatus("current")
_CsiNotifObjects_ObjectIdentity = ObjectIdentity
csiNotifObjects = _CsiNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 4)
)


class _CsiNotifEnable_Type(Bits):
    """Custom type csiNotifEnable based on Bits"""
    namedValues = NamedValues(
        *(("deviceAdded", 1),
          ("deviceLost", 2),
          ("fileLoadFailed", 3),
          ("operationModeChange", 0))
    )

_CsiNotifEnable_Type.__name__ = "Bits"
_CsiNotifEnable_Object = MibScalar
csiNotifEnable = _CsiNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 4, 1),
    _CsiNotifEnable_Type()
)
csiNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csiNotifEnable.setStatus("current")


class _CsiNotifOperationType_Type(Integer32):
    """Custom type csiNotifOperationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("downloadConfig", 2),
          ("downloadImage", 3),
          ("other", 1),
          ("uploadConfig", 4))
    )


_CsiNotifOperationType_Type.__name__ = "Integer32"
_CsiNotifOperationType_Object = MibScalar
csiNotifOperationType = _CsiNotifOperationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 4, 2),
    _CsiNotifOperationType_Type()
)
csiNotifOperationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiNotifOperationType.setStatus("current")
_CsiNotifOperationResult_Type = SnmpAdminString
_CsiNotifOperationResult_Object = MibScalar
csiNotifOperationResult = _CsiNotifOperationResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 1, 4, 3),
    _CsiNotifOperationResult_Type()
)
csiNotifOperationResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csiNotifOperationResult.setStatus("current")
_CiscoSmartInstallMIBConform_ObjectIdentity = ObjectIdentity
ciscoSmartInstallMIBConform = _CiscoSmartInstallMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 2)
)
_CiscoSmartInstallCompliances_ObjectIdentity = ObjectIdentity
ciscoSmartInstallCompliances = _CiscoSmartInstallCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 2, 1)
)
_CiscoSmartInstallGroups_ObjectIdentity = ObjectIdentity
ciscoSmartInstallGroups = _CiscoSmartInstallGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 2, 2)
)

# Managed Objects groups

ciscoSmartInstallGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 2, 2, 1)
)
ciscoSmartInstallGlobalConfigGroup.setObjects(
      *(("CISCO-SMART-INSTALL-MIB", "csiOperationMode"),
        ("CISCO-SMART-INSTALL-MIB", "csiDirectorIpAddressType"),
        ("CISCO-SMART-INSTALL-MIB", "csiDirectorIpAddress"),
        ("CISCO-SMART-INSTALL-MIB", "csiManagementVlan"),
        ("CISCO-SMART-INSTALL-MIB", "csiManagementVlansFirst2K"),
        ("CISCO-SMART-INSTALL-MIB", "csiManagementVlansSecond2K"))
)
if mibBuilder.loadTexts:
    ciscoSmartInstallGlobalConfigGroup.setStatus("current")

ciscoSmartInstallConfigBackupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 2, 2, 2)
)
ciscoSmartInstallConfigBackupGroup.setObjects(
      *(("CISCO-SMART-INSTALL-MIB", "csiBackupEnable"),
        ("CISCO-SMART-INSTALL-MIB", "csiBackupHostUrl"))
)
if mibBuilder.loadTexts:
    ciscoSmartInstallConfigBackupGroup.setStatus("current")

ciscoSmartInstallJoinWindowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 2, 2, 3)
)
ciscoSmartInstallJoinWindowGroup.setObjects(
      *(("CISCO-SMART-INSTALL-MIB", "csiJoinWindowConfigOperationMode"),
        ("CISCO-SMART-INSTALL-MIB", "csiJoinWindowPeriodNextFreeIndex"),
        ("CISCO-SMART-INSTALL-MIB", "csiJoinWindowPeriodStartTime"),
        ("CISCO-SMART-INSTALL-MIB", "csiJoinWindowPeriodInterval"),
        ("CISCO-SMART-INSTALL-MIB", "csiJoinWindowPeriodRecurrencePattern"),
        ("CISCO-SMART-INSTALL-MIB", "csiJoinWindowPeriodExpirationDate"),
        ("CISCO-SMART-INSTALL-MIB", "csiJoinWindowPeriodRowStatus"),
        ("CISCO-SMART-INSTALL-MIB", "csiJoinWindowPeriodStorageType"))
)
if mibBuilder.loadTexts:
    ciscoSmartInstallJoinWindowGroup.setStatus("current")

ciscoSmartInstallProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 2, 2, 4)
)
ciscoSmartInstallProfileGroup.setObjects(
      *(("CISCO-SMART-INSTALL-MIB", "csiImageFileUrl"),
        ("CISCO-SMART-INSTALL-MIB", "csiConfigFileUrl"),
        ("CISCO-SMART-INSTALL-MIB", "csiHostnamePrefix"),
        ("CISCO-SMART-INSTALL-MIB", "csiProfileNextFreeIndex"),
        ("CISCO-SMART-INSTALL-MIB", "csiProfileGroupName"),
        ("CISCO-SMART-INSTALL-MIB", "csiProfileImageUrl"),
        ("CISCO-SMART-INSTALL-MIB", "csiProfileImageTwoUrl"),
        ("CISCO-SMART-INSTALL-MIB", "csiProfileConfigUrl"),
        ("CISCO-SMART-INSTALL-MIB", "csiProfileStorageType"),
        ("CISCO-SMART-INSTALL-MIB", "csiProfileRowStatus"),
        ("CISCO-SMART-INSTALL-MIB", "csiMatchGroupType"),
        ("CISCO-SMART-INSTALL-MIB", "csiMatchProductId"),
        ("CISCO-SMART-INSTALL-MIB", "csiMatchSwitchNum"),
        ("CISCO-SMART-INSTALL-MIB", "csiMatchSwitchProductId"),
        ("CISCO-SMART-INSTALL-MIB", "csiMatchHostAddressType"),
        ("CISCO-SMART-INSTALL-MIB", "csiMatchHostAddress"),
        ("CISCO-SMART-INSTALL-MIB", "csiMatchHostInterface"),
        ("CISCO-SMART-INSTALL-MIB", "csiMatchMacAddress"),
        ("CISCO-SMART-INSTALL-MIB", "csiMatchStorageType"),
        ("CISCO-SMART-INSTALL-MIB", "csiMatchRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSmartInstallProfileGroup.setStatus("current")

ciscoSmartInstallDeviceInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 2, 2, 5)
)
ciscoSmartInstallDeviceInformationGroup.setObjects(
      *(("CISCO-SMART-INSTALL-MIB", "csiDeviceMacAddress"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceAddressType"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceAddress"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceName"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceBackupConfigFileName"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceImageVersion"),
        ("CISCO-SMART-INSTALL-MIB", "csiDevicePlatform"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceSerialNum"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceStatus"))
)
if mibBuilder.loadTexts:
    ciscoSmartInstallDeviceInformationGroup.setStatus("current")

ciscoSmartInstallNotificationEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 2, 2, 6)
)
ciscoSmartInstallNotificationEnableGroup.setObjects(
    ("CISCO-SMART-INSTALL-MIB", "csiNotifEnable")
)
if mibBuilder.loadTexts:
    ciscoSmartInstallNotificationEnableGroup.setStatus("current")

ciscoSmartInstallNotifyVarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 2, 2, 8)
)
ciscoSmartInstallNotifyVarsGroup.setObjects(
      *(("CISCO-SMART-INSTALL-MIB", "csiNotifOperationType"),
        ("CISCO-SMART-INSTALL-MIB", "csiNotifOperationResult"))
)
if mibBuilder.loadTexts:
    ciscoSmartInstallNotifyVarsGroup.setStatus("current")


# Notification objects

csiOperationModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 0, 1)
)
csiOperationModeChange.setObjects(
    ("CISCO-SMART-INSTALL-MIB", "csiOperationMode")
)
if mibBuilder.loadTexts:
    csiOperationModeChange.setStatus(
        "current"
    )

csiDeviceAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 0, 2)
)
csiDeviceAdded.setObjects(
      *(("CISCO-SMART-INSTALL-MIB", "csiDeviceName"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceAddressType"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceAddress"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceMacAddress"))
)
if mibBuilder.loadTexts:
    csiDeviceAdded.setStatus(
        "current"
    )

csiDeviceLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 0, 3)
)
csiDeviceLost.setObjects(
      *(("CISCO-SMART-INSTALL-MIB", "csiDeviceName"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceAddressType"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceAddress"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceMacAddress"))
)
if mibBuilder.loadTexts:
    csiDeviceLost.setStatus(
        "current"
    )

csiFileLoadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 0, 4)
)
csiFileLoadFailed.setObjects(
      *(("CISCO-SMART-INSTALL-MIB", "csiDeviceName"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceAddressType"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceAddress"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceMacAddress"),
        ("CISCO-SMART-INSTALL-MIB", "csiNotifOperationType"),
        ("CISCO-SMART-INSTALL-MIB", "csiNotifOperationResult"))
)
if mibBuilder.loadTexts:
    csiFileLoadFailed.setStatus(
        "current"
    )


# Notifications groups

ciscoSmartInstallNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 2, 2, 7)
)
ciscoSmartInstallNotificationsGroup.setObjects(
      *(("CISCO-SMART-INSTALL-MIB", "csiOperationModeChange"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceAdded"),
        ("CISCO-SMART-INSTALL-MIB", "csiDeviceLost"),
        ("CISCO-SMART-INSTALL-MIB", "csiFileLoadFailed"))
)
if mibBuilder.loadTexts:
    ciscoSmartInstallNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSmartInstallCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 725, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSmartInstallCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SMART-INSTALL-MIB",
    **{"ciscoSmartInstallMIB": ciscoSmartInstallMIB,
       "ciscoSmartInstallMIBNotifs": ciscoSmartInstallMIBNotifs,
       "csiOperationModeChange": csiOperationModeChange,
       "csiDeviceAdded": csiDeviceAdded,
       "csiDeviceLost": csiDeviceLost,
       "csiFileLoadFailed": csiFileLoadFailed,
       "ciscoSmartInstallMIBObjects": ciscoSmartInstallMIBObjects,
       "csiGlobalConfig": csiGlobalConfig,
       "csiOperationMode": csiOperationMode,
       "csiDirectorIpAddressType": csiDirectorIpAddressType,
       "csiDirectorIpAddress": csiDirectorIpAddress,
       "csiManagementVlan": csiManagementVlan,
       "csiManagementVlansFirst2K": csiManagementVlansFirst2K,
       "csiManagementVlansSecond2K": csiManagementVlansSecond2K,
       "csiBackup": csiBackup,
       "csiBackupHostUrl": csiBackupHostUrl,
       "csiBackupEnable": csiBackupEnable,
       "csiJoinWindow": csiJoinWindow,
       "csiJoinWindowConfigOperationMode": csiJoinWindowConfigOperationMode,
       "csiJoinWindowPeriodNextFreeIndex": csiJoinWindowPeriodNextFreeIndex,
       "csiJoinWindowPeriodTable": csiJoinWindowPeriodTable,
       "csiJoinWindowPeriodEntry": csiJoinWindowPeriodEntry,
       "csiJoinWindowPeriodIndex": csiJoinWindowPeriodIndex,
       "csiJoinWindowPeriodStartTime": csiJoinWindowPeriodStartTime,
       "csiJoinWindowPeriodInterval": csiJoinWindowPeriodInterval,
       "csiJoinWindowPeriodRecurrencePattern": csiJoinWindowPeriodRecurrencePattern,
       "csiJoinWindowPeriodExpirationDate": csiJoinWindowPeriodExpirationDate,
       "csiJoinWindowPeriodStorageType": csiJoinWindowPeriodStorageType,
       "csiJoinWindowPeriodRowStatus": csiJoinWindowPeriodRowStatus,
       "csiProfile": csiProfile,
       "csiImageFileUrl": csiImageFileUrl,
       "csiConfigFileUrl": csiConfigFileUrl,
       "csiHostnamePrefix": csiHostnamePrefix,
       "csiProfileNextFreeIndex": csiProfileNextFreeIndex,
       "csiProfileTable": csiProfileTable,
       "csiProfileEntry": csiProfileEntry,
       "csiProfileIndex": csiProfileIndex,
       "csiProfileGroupName": csiProfileGroupName,
       "csiProfileImageUrl": csiProfileImageUrl,
       "csiProfileImageTwoUrl": csiProfileImageTwoUrl,
       "csiProfileConfigUrl": csiProfileConfigUrl,
       "csiProfileStorageType": csiProfileStorageType,
       "csiProfileRowStatus": csiProfileRowStatus,
       "csiMatchTable": csiMatchTable,
       "csiMatchEntry": csiMatchEntry,
       "csiMatchIndex": csiMatchIndex,
       "csiMatchGroupType": csiMatchGroupType,
       "csiMatchMacAddress": csiMatchMacAddress,
       "csiMatchHostAddressType": csiMatchHostAddressType,
       "csiMatchHostAddress": csiMatchHostAddress,
       "csiMatchHostInterface": csiMatchHostInterface,
       "csiMatchProductId": csiMatchProductId,
       "csiMatchSwitchNum": csiMatchSwitchNum,
       "csiMatchSwitchProductId": csiMatchSwitchProductId,
       "csiMatchStorageType": csiMatchStorageType,
       "csiMatchRowStatus": csiMatchRowStatus,
       "csiDeviceInfo": csiDeviceInfo,
       "csiDeviceTable": csiDeviceTable,
       "csiDeviceEntry": csiDeviceEntry,
       "csiDeviceNum": csiDeviceNum,
       "csiDeviceMacAddress": csiDeviceMacAddress,
       "csiDeviceAddressType": csiDeviceAddressType,
       "csiDeviceAddress": csiDeviceAddress,
       "csiDeviceName": csiDeviceName,
       "csiDeviceBackupConfigFileName": csiDeviceBackupConfigFileName,
       "csiDeviceImageVersion": csiDeviceImageVersion,
       "csiDevicePlatform": csiDevicePlatform,
       "csiDeviceSerialNum": csiDeviceSerialNum,
       "csiDeviceStatus": csiDeviceStatus,
       "csiNotifObjects": csiNotifObjects,
       "csiNotifEnable": csiNotifEnable,
       "csiNotifOperationType": csiNotifOperationType,
       "csiNotifOperationResult": csiNotifOperationResult,
       "ciscoSmartInstallMIBConform": ciscoSmartInstallMIBConform,
       "ciscoSmartInstallCompliances": ciscoSmartInstallCompliances,
       "ciscoSmartInstallCompliance": ciscoSmartInstallCompliance,
       "ciscoSmartInstallGroups": ciscoSmartInstallGroups,
       "ciscoSmartInstallGlobalConfigGroup": ciscoSmartInstallGlobalConfigGroup,
       "ciscoSmartInstallConfigBackupGroup": ciscoSmartInstallConfigBackupGroup,
       "ciscoSmartInstallJoinWindowGroup": ciscoSmartInstallJoinWindowGroup,
       "ciscoSmartInstallProfileGroup": ciscoSmartInstallProfileGroup,
       "ciscoSmartInstallDeviceInformationGroup": ciscoSmartInstallDeviceInformationGroup,
       "ciscoSmartInstallNotificationEnableGroup": ciscoSmartInstallNotificationEnableGroup,
       "ciscoSmartInstallNotificationsGroup": ciscoSmartInstallNotificationsGroup,
       "ciscoSmartInstallNotifyVarsGroup": ciscoSmartInstallNotifyVarsGroup}
)
