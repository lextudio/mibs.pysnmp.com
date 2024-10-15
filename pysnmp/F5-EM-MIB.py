# SNMP MIB module (F5-EM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F5-EM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:39 2024
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

(LongDisplayString,
 bigipCompliances,
 bigipGroups,
 f5) = mibBuilder.importSymbols(
    "F5-BIGIP-COMMON-MIB",
    "LongDisplayString",
    "bigipCompliances",
    "bigipGroups",
    "f5")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 Opaque,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

enterpriseManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EmDevices_ObjectIdentity = ObjectIdentity
emDevices = _EmDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1)
)
_EmDeviceList_ObjectIdentity = ObjectIdentity
emDeviceList = _EmDeviceList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 1)
)
_DeviceNumber_Type = Integer32
_DeviceNumber_Object = MibScalar
deviceNumber = _DeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 1),
    _DeviceNumber_Type()
)
deviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceNumber.setStatus("current")
_DeviceEntryTable_Object = MibTable
deviceEntryTable = _DeviceEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    deviceEntryTable.setStatus("current")
_DeviceEntry_Object = MibTableRow
deviceEntry = _DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2, 1)
)
deviceEntry.setIndexNames(
    (0, "F5-EM-MIB", "deviceName"),
)
if mibBuilder.loadTexts:
    deviceEntry.setStatus("current")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibTableColumn
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2, 1, 1),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_DeviceAddressType_Type = InetAddressType
_DeviceAddressType_Object = MibTableColumn
deviceAddressType = _DeviceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2, 1, 2),
    _DeviceAddressType_Type()
)
deviceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAddressType.setStatus("current")
_DeviceAddress_Type = InetAddress
_DeviceAddress_Object = MibTableColumn
deviceAddress = _DeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2, 1, 3),
    _DeviceAddress_Type()
)
deviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAddress.setStatus("current")
_EmDeviceGroups_ObjectIdentity = ObjectIdentity
emDeviceGroups = _EmDeviceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 2)
)
_GroupNumber_Type = Integer32
_GroupNumber_Object = MibScalar
groupNumber = _GroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 2, 1),
    _GroupNumber_Type()
)
groupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupNumber.setStatus("current")
_GroupEntryTable_Object = MibTable
groupEntryTable = _GroupEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 2, 2)
)
if mibBuilder.loadTexts:
    groupEntryTable.setStatus("current")
_GroupEntry_Object = MibTableRow
groupEntry = _GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 2, 2, 1)
)
groupEntry.setIndexNames(
    (0, "F5-EM-MIB", "groupName"),
)
if mibBuilder.loadTexts:
    groupEntry.setStatus("current")
_GroupName_Type = DisplayString
_GroupName_Object = MibTableColumn
groupName = _GroupName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 2, 2, 1, 1),
    _GroupName_Type()
)
groupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupName.setStatus("current")
_GroupDescription_Type = DisplayString
_GroupDescription_Object = MibTableColumn
groupDescription = _GroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 2, 2, 1, 2),
    _GroupDescription_Type()
)
groupDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupDescription.setStatus("current")
_EmImages_ObjectIdentity = ObjectIdentity
emImages = _EmImages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 3)
)
_ImageNumber_Type = Integer32
_ImageNumber_Object = MibScalar
imageNumber = _ImageNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 3, 1),
    _ImageNumber_Type()
)
imageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageNumber.setStatus("current")
_ImageEntryTable_Object = MibTable
imageEntryTable = _ImageEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 3, 2)
)
if mibBuilder.loadTexts:
    imageEntryTable.setStatus("current")
_ImageEntry_Object = MibTableRow
imageEntry = _ImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 3, 2, 1)
)
imageEntry.setIndexNames(
    (0, "F5-EM-MIB", "imageVersion"),
)
if mibBuilder.loadTexts:
    imageEntry.setStatus("current")
_ImageVersion_Type = DisplayString
_ImageVersion_Object = MibTableColumn
imageVersion = _ImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 3, 2, 1, 1),
    _ImageVersion_Type()
)
imageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageVersion.setStatus("current")
_ImageDescription_Type = DisplayString
_ImageDescription_Object = MibTableColumn
imageDescription = _ImageDescription_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 3, 2, 1, 2),
    _ImageDescription_Type()
)
imageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageDescription.setStatus("current")
_EmArchives_ObjectIdentity = ObjectIdentity
emArchives = _EmArchives_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 4)
)
_ArchiveNumber_Type = Integer32
_ArchiveNumber_Object = MibScalar
archiveNumber = _ArchiveNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 4, 1),
    _ArchiveNumber_Type()
)
archiveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveNumber.setStatus("obsolete")
_ArchiveEntryTable_Object = MibTable
archiveEntryTable = _ArchiveEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 4, 2)
)
if mibBuilder.loadTexts:
    archiveEntryTable.setStatus("obsolete")
_ArchiveEntry_Object = MibTableRow
archiveEntry = _ArchiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1)
)
archiveEntry.setIndexNames(
    (0, "F5-EM-MIB", "archiveSourceDevice"),
)
if mibBuilder.loadTexts:
    archiveEntry.setStatus("obsolete")
_ArchiveSourceDevice_Type = DisplayString
_ArchiveSourceDevice_Object = MibTableColumn
archiveSourceDevice = _ArchiveSourceDevice_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 1),
    _ArchiveSourceDevice_Type()
)
archiveSourceDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveSourceDevice.setStatus("obsolete")
_ArchiveProduct_Type = DisplayString
_ArchiveProduct_Object = MibTableColumn
archiveProduct = _ArchiveProduct_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 2),
    _ArchiveProduct_Type()
)
archiveProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveProduct.setStatus("obsolete")
_ArchiveVersion_Type = DisplayString
_ArchiveVersion_Object = MibTableColumn
archiveVersion = _ArchiveVersion_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 3),
    _ArchiveVersion_Type()
)
archiveVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveVersion.setStatus("obsolete")
_ArchiveTimeStamp_Type = DateAndTime
_ArchiveTimeStamp_Object = MibTableColumn
archiveTimeStamp = _ArchiveTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 4),
    _ArchiveTimeStamp_Type()
)
archiveTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveTimeStamp.setStatus("obsolete")
_ArchiveFilename_Type = DisplayString
_ArchiveFilename_Object = MibTableColumn
archiveFilename = _ArchiveFilename_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 5),
    _ArchiveFilename_Type()
)
archiveFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveFilename.setStatus("obsolete")
_ArchiveDescription_Type = DisplayString
_ArchiveDescription_Object = MibTableColumn
archiveDescription = _ArchiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 6),
    _ArchiveDescription_Type()
)
archiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    archiveDescription.setStatus("obsolete")
_EmGlobals_ObjectIdentity = ObjectIdentity
emGlobals = _EmGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 5)
)
_EmMaxConcurrentUpdates_Type = Integer32
_EmMaxConcurrentUpdates_Object = MibScalar
emMaxConcurrentUpdates = _EmMaxConcurrentUpdates_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 5, 1),
    _EmMaxConcurrentUpdates_Type()
)
emMaxConcurrentUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emMaxConcurrentUpdates.setStatus("obsolete")
_EmRefreshInterval_Type = Integer32
_EmRefreshInterval_Object = MibScalar
emRefreshInterval = _EmRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 5, 2),
    _EmRefreshInterval_Type()
)
emRefreshInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emRefreshInterval.setStatus("obsolete")
_EmVersion_Type = DisplayString
_EmVersion_Object = MibScalar
emVersion = _EmVersion_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 5, 3),
    _EmVersion_Type()
)
emVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emVersion.setStatus("obsolete")
_EmAlert_ObjectIdentity = ObjectIdentity
emAlert = _EmAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6)
)
_EmAlerts_ObjectIdentity = ObjectIdentity
emAlerts = _EmAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0)
)
_EmAlertConfigObjects_ObjectIdentity = ObjectIdentity
emAlertConfigObjects = _EmAlertConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 0)
)
_EmAlertObjects_ObjectIdentity = ObjectIdentity
emAlertObjects = _EmAlertObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 1)
)
_EmAlertObjMsg_Type = DisplayString
_EmAlertObjMsg_Object = MibScalar
emAlertObjMsg = _EmAlertObjMsg_Object(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 1, 1),
    _EmAlertObjMsg_Type()
)
emAlertObjMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emAlertObjMsg.setStatus("current")

# Managed Objects groups


# Notification objects

emDeviceConfigSettingChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 0, 1)
)
emDeviceConfigSettingChanged.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emDeviceConfigSettingChanged.setStatus(
        "obsolete"
    )

emDeviceUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 1)
)
emDeviceUnreachable.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emDeviceUnreachable.setStatus(
        "current"
    )

emSoftwareInstallComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 2)
)
emSoftwareInstallComplete.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emSoftwareInstallComplete.setStatus(
        "current"
    )

emSoftwareInstallFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 3)
)
emSoftwareInstallFailed.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emSoftwareInstallFailed.setStatus(
        "current"
    )

emDeviceClockSkew = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 4)
)
emDeviceClockSkew.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emDeviceClockSkew.setStatus(
        "current"
    )

emDiskUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 5)
)
emDiskUsage.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emDiskUsage.setStatus(
        "current"
    )

emMemoryUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 6)
)
emMemoryUsage.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emMemoryUsage.setStatus(
        "current"
    )

emHotfixInstallComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 7)
)
emHotfixInstallComplete.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emHotfixInstallComplete.setStatus(
        "current"
    )

emHotfixInstallFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 8)
)
emHotfixInstallFailed.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emHotfixInstallFailed.setStatus(
        "current"
    )

emCpuUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 9)
)
emCpuUsage.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emCpuUsage.setStatus(
        "current"
    )

emCertificateExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 10)
)
emCertificateExpiration.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emCertificateExpiration.setStatus(
        "current"
    )

emScheduledArchiveFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 11)
)
emScheduledArchiveFailed.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emScheduledArchiveFailed.setStatus(
        "current"
    )

emDeviceActiveMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 12)
)
emDeviceActiveMode.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emDeviceActiveMode.setStatus(
        "current"
    )

emDeviceStandbyMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 13)
)
emDeviceStandbyMode.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emDeviceStandbyMode.setStatus(
        "current"
    )

emDeviceConfigSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 14)
)
emDeviceConfigSync.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emDeviceConfigSync.setStatus(
        "current"
    )

emRaidDriveFailureDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 15)
)
emRaidDriveFailureDetected.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emRaidDriveFailureDetected.setStatus(
        "current"
    )

emRaidDriveRebuildComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 16)
)
emRaidDriveRebuildComplete.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emRaidDriveRebuildComplete.setStatus(
        "current"
    )

emHaSyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 19)
)
emHaSyncFailed.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emHaSyncFailed.setStatus(
        "current"
    )

emASMSigInstallComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 20)
)
emASMSigInstallComplete.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emASMSigInstallComplete.setStatus(
        "current"
    )

emASMSigInstallFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 21)
)
emASMSigInstallFailed.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emASMSigInstallFailed.setStatus(
        "current"
    )

emASMSigUpdateAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 22)
)
emASMSigUpdateAvailable.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emASMSigUpdateAvailable.setStatus(
        "current"
    )

emASMSigUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 23)
)
emASMSigUpdateFailed.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emASMSigUpdateFailed.setStatus(
        "current"
    )

emPerformanceStorageDays = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 25)
)
emPerformanceStorageDays.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emPerformanceStorageDays.setStatus(
        "current"
    )

emPerformanceStorageCap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 26)
)
emPerformanceStorageCap.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emPerformanceStorageCap.setStatus(
        "current"
    )

emPerformanceThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 27)
)
emPerformanceThreshold.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emPerformanceThreshold.setStatus(
        "current"
    )

emSchedBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 28)
)
emSchedBackupFailed.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emSchedBackupFailed.setStatus(
        "current"
    )

emStatsCollectionRateCap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 29)
)
emStatsCollectionRateCap.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emStatsCollectionRateCap.setStatus(
        "current"
    )

emDeviceOfflineMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 30)
)
emDeviceOfflineMode.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emDeviceOfflineMode.setStatus(
        "current"
    )

emDeviceForcedOfflineMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 31)
)
emDeviceForcedOfflineMode.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emDeviceForcedOfflineMode.setStatus(
        "current"
    )

emServiceContractExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 32)
)
emServiceContractExpiry.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emServiceContractExpiry.setStatus(
        "current"
    )

emStatsDBConnectivityLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 33)
)
emStatsDBConnectivityLost.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emStatsDBConnectivityLost.setStatus(
        "current"
    )

emGatherServiceContractFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 34)
)
emGatherServiceContractFailure.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emGatherServiceContractFailure.setStatus(
        "current"
    )

emDeviceImpaired = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 35)
)
emDeviceImpaired.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emDeviceImpaired.setStatus(
        "current"
    )

emStatsDBConnectivityRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 36)
)
emStatsDBConnectivityRestored.setObjects(
    ("F5-EM-MIB", "emAlertObjMsg")
)
if mibBuilder.loadTexts:
    emStatsDBConnectivityRestored.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F5-EM-MIB",
    **{"enterpriseManagement": enterpriseManagement,
       "emDevices": emDevices,
       "emDeviceList": emDeviceList,
       "deviceNumber": deviceNumber,
       "deviceEntryTable": deviceEntryTable,
       "deviceEntry": deviceEntry,
       "deviceName": deviceName,
       "deviceAddressType": deviceAddressType,
       "deviceAddress": deviceAddress,
       "emDeviceGroups": emDeviceGroups,
       "groupNumber": groupNumber,
       "groupEntryTable": groupEntryTable,
       "groupEntry": groupEntry,
       "groupName": groupName,
       "groupDescription": groupDescription,
       "emImages": emImages,
       "imageNumber": imageNumber,
       "imageEntryTable": imageEntryTable,
       "imageEntry": imageEntry,
       "imageVersion": imageVersion,
       "imageDescription": imageDescription,
       "emArchives": emArchives,
       "archiveNumber": archiveNumber,
       "archiveEntryTable": archiveEntryTable,
       "archiveEntry": archiveEntry,
       "archiveSourceDevice": archiveSourceDevice,
       "archiveProduct": archiveProduct,
       "archiveVersion": archiveVersion,
       "archiveTimeStamp": archiveTimeStamp,
       "archiveFilename": archiveFilename,
       "archiveDescription": archiveDescription,
       "emGlobals": emGlobals,
       "emMaxConcurrentUpdates": emMaxConcurrentUpdates,
       "emRefreshInterval": emRefreshInterval,
       "emVersion": emVersion,
       "emAlert": emAlert,
       "emAlerts": emAlerts,
       "emAlertConfigObjects": emAlertConfigObjects,
       "emDeviceConfigSettingChanged": emDeviceConfigSettingChanged,
       "emDeviceUnreachable": emDeviceUnreachable,
       "emSoftwareInstallComplete": emSoftwareInstallComplete,
       "emSoftwareInstallFailed": emSoftwareInstallFailed,
       "emDeviceClockSkew": emDeviceClockSkew,
       "emDiskUsage": emDiskUsage,
       "emMemoryUsage": emMemoryUsage,
       "emHotfixInstallComplete": emHotfixInstallComplete,
       "emHotfixInstallFailed": emHotfixInstallFailed,
       "emCpuUsage": emCpuUsage,
       "emCertificateExpiration": emCertificateExpiration,
       "emScheduledArchiveFailed": emScheduledArchiveFailed,
       "emDeviceActiveMode": emDeviceActiveMode,
       "emDeviceStandbyMode": emDeviceStandbyMode,
       "emDeviceConfigSync": emDeviceConfigSync,
       "emRaidDriveFailureDetected": emRaidDriveFailureDetected,
       "emRaidDriveRebuildComplete": emRaidDriveRebuildComplete,
       "emHaSyncFailed": emHaSyncFailed,
       "emASMSigInstallComplete": emASMSigInstallComplete,
       "emASMSigInstallFailed": emASMSigInstallFailed,
       "emASMSigUpdateAvailable": emASMSigUpdateAvailable,
       "emASMSigUpdateFailed": emASMSigUpdateFailed,
       "emPerformanceStorageDays": emPerformanceStorageDays,
       "emPerformanceStorageCap": emPerformanceStorageCap,
       "emPerformanceThreshold": emPerformanceThreshold,
       "emSchedBackupFailed": emSchedBackupFailed,
       "emStatsCollectionRateCap": emStatsCollectionRateCap,
       "emDeviceOfflineMode": emDeviceOfflineMode,
       "emDeviceForcedOfflineMode": emDeviceForcedOfflineMode,
       "emServiceContractExpiry": emServiceContractExpiry,
       "emStatsDBConnectivityLost": emStatsDBConnectivityLost,
       "emGatherServiceContractFailure": emGatherServiceContractFailure,
       "emDeviceImpaired": emDeviceImpaired,
       "emStatsDBConnectivityRestored": emStatsDBConnectivityRestored,
       "emAlertObjects": emAlertObjects,
       "emAlertObjMsg": emAlertObjMsg}
)
