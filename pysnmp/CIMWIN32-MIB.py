# SNMP MIB module (CIMWIN32-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIMWIN32-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:14 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(Boolean,
 Datetime,
 Real32,
 Real64,
 Sint16,
 Sint32,
 Sint64,
 Sint8,
 String,
 Uint16,
 Uint32,
 Uint64,
 Uint8,
 win32WMI) = mibBuilder.importSymbols(
    "UMS-MIB",
    "Boolean",
    "Datetime",
    "Real32",
    "Real64",
    "Sint16",
    "Sint32",
    "Sint64",
    "Sint8",
    "String",
    "Uint16",
    "Uint32",
    "Uint64",
    "Uint8",
    "win32WMI")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Win32ComputerSystemTable_Object = MibTable
win32ComputerSystemTable = _Win32ComputerSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10)
)
if mibBuilder.loadTexts:
    win32ComputerSystemTable.setStatus("mandatory")
_Win32ComputerSystemEntry_Object = MibTableRow
win32ComputerSystemEntry = _Win32ComputerSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1)
)
win32ComputerSystemEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32ComputerSystemKeyIndex"),
)
if mibBuilder.loadTexts:
    win32ComputerSystemEntry.setStatus("mandatory")
_Win32ComputerSystemKeyIndex_Type = String
_Win32ComputerSystemKeyIndex_Object = MibTableColumn
win32ComputerSystemKeyIndex = _Win32ComputerSystemKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 1),
    _Win32ComputerSystemKeyIndex_Type()
)
win32ComputerSystemKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemKeyIndex.setStatus("mandatory")
_Win32ComputerSystemAutomaticResetBootOption_Type = Boolean
_Win32ComputerSystemAutomaticResetBootOption_Object = MibTableColumn
win32ComputerSystemAutomaticResetBootOption = _Win32ComputerSystemAutomaticResetBootOption_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 2),
    _Win32ComputerSystemAutomaticResetBootOption_Type()
)
win32ComputerSystemAutomaticResetBootOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemAutomaticResetBootOption.setStatus("mandatory")
_Win32ComputerSystemAutomaticResetCapability_Type = Boolean
_Win32ComputerSystemAutomaticResetCapability_Object = MibTableColumn
win32ComputerSystemAutomaticResetCapability = _Win32ComputerSystemAutomaticResetCapability_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 3),
    _Win32ComputerSystemAutomaticResetCapability_Type()
)
win32ComputerSystemAutomaticResetCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemAutomaticResetCapability.setStatus("mandatory")
_Win32ComputerSystemBootROMSupported_Type = Boolean
_Win32ComputerSystemBootROMSupported_Object = MibTableColumn
win32ComputerSystemBootROMSupported = _Win32ComputerSystemBootROMSupported_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 4),
    _Win32ComputerSystemBootROMSupported_Type()
)
win32ComputerSystemBootROMSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemBootROMSupported.setStatus("mandatory")
_Win32ComputerSystemBootupState_Type = String
_Win32ComputerSystemBootupState_Object = MibTableColumn
win32ComputerSystemBootupState = _Win32ComputerSystemBootupState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 5),
    _Win32ComputerSystemBootupState_Type()
)
win32ComputerSystemBootupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemBootupState.setStatus("mandatory")
_Win32ComputerSystemCurrentTimeZone_Type = Sint16
_Win32ComputerSystemCurrentTimeZone_Object = MibTableColumn
win32ComputerSystemCurrentTimeZone = _Win32ComputerSystemCurrentTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 6),
    _Win32ComputerSystemCurrentTimeZone_Type()
)
win32ComputerSystemCurrentTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemCurrentTimeZone.setStatus("mandatory")
_Win32ComputerSystemDomain_Type = String
_Win32ComputerSystemDomain_Object = MibTableColumn
win32ComputerSystemDomain = _Win32ComputerSystemDomain_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 7),
    _Win32ComputerSystemDomain_Type()
)
win32ComputerSystemDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemDomain.setStatus("mandatory")
_Win32ComputerSystemInfraredSupported_Type = Boolean
_Win32ComputerSystemInfraredSupported_Object = MibTableColumn
win32ComputerSystemInfraredSupported = _Win32ComputerSystemInfraredSupported_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 8),
    _Win32ComputerSystemInfraredSupported_Type()
)
win32ComputerSystemInfraredSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemInfraredSupported.setStatus("mandatory")
_Win32ComputerSystemManufacturer_Type = String
_Win32ComputerSystemManufacturer_Object = MibTableColumn
win32ComputerSystemManufacturer = _Win32ComputerSystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 9),
    _Win32ComputerSystemManufacturer_Type()
)
win32ComputerSystemManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemManufacturer.setStatus("mandatory")
_Win32ComputerSystemModel_Type = String
_Win32ComputerSystemModel_Object = MibTableColumn
win32ComputerSystemModel = _Win32ComputerSystemModel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 10),
    _Win32ComputerSystemModel_Type()
)
win32ComputerSystemModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemModel.setStatus("mandatory")
_Win32ComputerSystemNetworkServerModeEnabled_Type = Boolean
_Win32ComputerSystemNetworkServerModeEnabled_Object = MibTableColumn
win32ComputerSystemNetworkServerModeEnabled = _Win32ComputerSystemNetworkServerModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 11),
    _Win32ComputerSystemNetworkServerModeEnabled_Type()
)
win32ComputerSystemNetworkServerModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemNetworkServerModeEnabled.setStatus("mandatory")
_Win32ComputerSystemOEMLogoBitmap_Type = Uint8
_Win32ComputerSystemOEMLogoBitmap_Object = MibTableColumn
win32ComputerSystemOEMLogoBitmap = _Win32ComputerSystemOEMLogoBitmap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 12),
    _Win32ComputerSystemOEMLogoBitmap_Type()
)
win32ComputerSystemOEMLogoBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemOEMLogoBitmap.setStatus("mandatory")
_Win32ComputerSystemSupportContactDescription_Type = String
_Win32ComputerSystemSupportContactDescription_Object = MibTableColumn
win32ComputerSystemSupportContactDescription = _Win32ComputerSystemSupportContactDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 13),
    _Win32ComputerSystemSupportContactDescription_Type()
)
win32ComputerSystemSupportContactDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemSupportContactDescription.setStatus("mandatory")
_Win32ComputerSystemSystemStartupDelay_Type = Uint16
_Win32ComputerSystemSystemStartupDelay_Object = MibTableColumn
win32ComputerSystemSystemStartupDelay = _Win32ComputerSystemSystemStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 14),
    _Win32ComputerSystemSystemStartupDelay_Type()
)
win32ComputerSystemSystemStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemSystemStartupDelay.setStatus("mandatory")
_Win32ComputerSystemSystemStartupOptions_Type = String
_Win32ComputerSystemSystemStartupOptions_Object = MibTableColumn
win32ComputerSystemSystemStartupOptions = _Win32ComputerSystemSystemStartupOptions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 15),
    _Win32ComputerSystemSystemStartupOptions_Type()
)
win32ComputerSystemSystemStartupOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemSystemStartupOptions.setStatus("mandatory")
_Win32ComputerSystemSystemStartupSetting_Type = Uint8
_Win32ComputerSystemSystemStartupSetting_Object = MibTableColumn
win32ComputerSystemSystemStartupSetting = _Win32ComputerSystemSystemStartupSetting_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 16),
    _Win32ComputerSystemSystemStartupSetting_Type()
)
win32ComputerSystemSystemStartupSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemSystemStartupSetting.setStatus("mandatory")
_Win32ComputerSystemSystemType_Type = String
_Win32ComputerSystemSystemType_Object = MibTableColumn
win32ComputerSystemSystemType = _Win32ComputerSystemSystemType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 17),
    _Win32ComputerSystemSystemType_Type()
)
win32ComputerSystemSystemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemSystemType.setStatus("mandatory")
_Win32ComputerSystemUserName_Type = String
_Win32ComputerSystemUserName_Object = MibTableColumn
win32ComputerSystemUserName = _Win32ComputerSystemUserName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 18),
    _Win32ComputerSystemUserName_Type()
)
win32ComputerSystemUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemUserName.setStatus("mandatory")
_Win32ComputerSystemStatus_Type = String
_Win32ComputerSystemStatus_Object = MibTableColumn
win32ComputerSystemStatus = _Win32ComputerSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 10, 1, 19),
    _Win32ComputerSystemStatus_Type()
)
win32ComputerSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ComputerSystemStatus.setStatus("mandatory")
_Win32TapeDriveTable_Object = MibTable
win32TapeDriveTable = _Win32TapeDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 20)
)
if mibBuilder.loadTexts:
    win32TapeDriveTable.setStatus("mandatory")
_Win32TapeDriveEntry_Object = MibTableRow
win32TapeDriveEntry = _Win32TapeDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 20, 1)
)
win32TapeDriveEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32TapeDriveKeyIndex"),
)
if mibBuilder.loadTexts:
    win32TapeDriveEntry.setStatus("mandatory")
_Win32TapeDriveKeyIndex_Type = String
_Win32TapeDriveKeyIndex_Object = MibTableColumn
win32TapeDriveKeyIndex = _Win32TapeDriveKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 20, 1, 1),
    _Win32TapeDriveKeyIndex_Type()
)
win32TapeDriveKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TapeDriveKeyIndex.setStatus("mandatory")
_Win32TapeDriveCompression_Type = Uint32
_Win32TapeDriveCompression_Object = MibTableColumn
win32TapeDriveCompression = _Win32TapeDriveCompression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 20, 1, 2),
    _Win32TapeDriveCompression_Type()
)
win32TapeDriveCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TapeDriveCompression.setStatus("mandatory")
_Win32TapeDriveECC_Type = Uint32
_Win32TapeDriveECC_Object = MibTableColumn
win32TapeDriveECC = _Win32TapeDriveECC_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 20, 1, 3),
    _Win32TapeDriveECC_Type()
)
win32TapeDriveECC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TapeDriveECC.setStatus("mandatory")
_Win32TapeDriveFeaturesHigh_Type = Uint32
_Win32TapeDriveFeaturesHigh_Object = MibTableColumn
win32TapeDriveFeaturesHigh = _Win32TapeDriveFeaturesHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 20, 1, 4),
    _Win32TapeDriveFeaturesHigh_Type()
)
win32TapeDriveFeaturesHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TapeDriveFeaturesHigh.setStatus("mandatory")
_Win32TapeDriveFeaturesLow_Type = Uint32
_Win32TapeDriveFeaturesLow_Object = MibTableColumn
win32TapeDriveFeaturesLow = _Win32TapeDriveFeaturesLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 20, 1, 5),
    _Win32TapeDriveFeaturesLow_Type()
)
win32TapeDriveFeaturesLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TapeDriveFeaturesLow.setStatus("mandatory")
_Win32TapeDriveMediaType_Type = String
_Win32TapeDriveMediaType_Object = MibTableColumn
win32TapeDriveMediaType = _Win32TapeDriveMediaType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 20, 1, 6),
    _Win32TapeDriveMediaType_Type()
)
win32TapeDriveMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TapeDriveMediaType.setStatus("mandatory")
_Win32TapeDriveReportSetMarks_Type = Uint32
_Win32TapeDriveReportSetMarks_Object = MibTableColumn
win32TapeDriveReportSetMarks = _Win32TapeDriveReportSetMarks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 20, 1, 7),
    _Win32TapeDriveReportSetMarks_Type()
)
win32TapeDriveReportSetMarks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TapeDriveReportSetMarks.setStatus("mandatory")
_Win32TapeDriveStatus_Type = String
_Win32TapeDriveStatus_Object = MibTableColumn
win32TapeDriveStatus = _Win32TapeDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 20, 1, 8),
    _Win32TapeDriveStatus_Type()
)
win32TapeDriveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TapeDriveStatus.setStatus("mandatory")
_Win32DiskDriveTable_Object = MibTable
win32DiskDriveTable = _Win32DiskDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30)
)
if mibBuilder.loadTexts:
    win32DiskDriveTable.setStatus("mandatory")
_Win32DiskDriveEntry_Object = MibTableRow
win32DiskDriveEntry = _Win32DiskDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1)
)
win32DiskDriveEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32DiskDriveKeyIndex"),
)
if mibBuilder.loadTexts:
    win32DiskDriveEntry.setStatus("mandatory")
_Win32DiskDriveKeyIndex_Type = String
_Win32DiskDriveKeyIndex_Object = MibTableColumn
win32DiskDriveKeyIndex = _Win32DiskDriveKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 1),
    _Win32DiskDriveKeyIndex_Type()
)
win32DiskDriveKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveKeyIndex.setStatus("mandatory")
_Win32DiskDriveBytesPerSector_Type = Uint32
_Win32DiskDriveBytesPerSector_Object = MibTableColumn
win32DiskDriveBytesPerSector = _Win32DiskDriveBytesPerSector_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 2),
    _Win32DiskDriveBytesPerSector_Type()
)
win32DiskDriveBytesPerSector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveBytesPerSector.setStatus("mandatory")
_Win32DiskDriveInterfaceType_Type = String
_Win32DiskDriveInterfaceType_Object = MibTableColumn
win32DiskDriveInterfaceType = _Win32DiskDriveInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 3),
    _Win32DiskDriveInterfaceType_Type()
)
win32DiskDriveInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveInterfaceType.setStatus("mandatory")
_Win32DiskDrivePartitions_Type = Uint32
_Win32DiskDrivePartitions_Object = MibTableColumn
win32DiskDrivePartitions = _Win32DiskDrivePartitions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 4),
    _Win32DiskDrivePartitions_Type()
)
win32DiskDrivePartitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDrivePartitions.setStatus("mandatory")
_Win32DiskDriveSectorsPerTrack_Type = Uint32
_Win32DiskDriveSectorsPerTrack_Object = MibTableColumn
win32DiskDriveSectorsPerTrack = _Win32DiskDriveSectorsPerTrack_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 5),
    _Win32DiskDriveSectorsPerTrack_Type()
)
win32DiskDriveSectorsPerTrack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveSectorsPerTrack.setStatus("mandatory")
_Win32DiskDriveTotalCylinders_Type = String
_Win32DiskDriveTotalCylinders_Object = MibTableColumn
win32DiskDriveTotalCylinders = _Win32DiskDriveTotalCylinders_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 6),
    _Win32DiskDriveTotalCylinders_Type()
)
win32DiskDriveTotalCylinders.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveTotalCylinders.setStatus("mandatory")
_Win32DiskDriveTotalHeads_Type = Uint32
_Win32DiskDriveTotalHeads_Object = MibTableColumn
win32DiskDriveTotalHeads = _Win32DiskDriveTotalHeads_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 7),
    _Win32DiskDriveTotalHeads_Type()
)
win32DiskDriveTotalHeads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveTotalHeads.setStatus("mandatory")
_Win32DiskDriveTotalSectors_Type = String
_Win32DiskDriveTotalSectors_Object = MibTableColumn
win32DiskDriveTotalSectors = _Win32DiskDriveTotalSectors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 8),
    _Win32DiskDriveTotalSectors_Type()
)
win32DiskDriveTotalSectors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveTotalSectors.setStatus("mandatory")
_Win32DiskDriveTotalTracks_Type = String
_Win32DiskDriveTotalTracks_Object = MibTableColumn
win32DiskDriveTotalTracks = _Win32DiskDriveTotalTracks_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 9),
    _Win32DiskDriveTotalTracks_Type()
)
win32DiskDriveTotalTracks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveTotalTracks.setStatus("mandatory")
_Win32DiskDriveTracksPerCylinder_Type = Uint32
_Win32DiskDriveTracksPerCylinder_Object = MibTableColumn
win32DiskDriveTracksPerCylinder = _Win32DiskDriveTracksPerCylinder_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 10),
    _Win32DiskDriveTracksPerCylinder_Type()
)
win32DiskDriveTracksPerCylinder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveTracksPerCylinder.setStatus("mandatory")
_Win32DiskDriveIndex_Type = Uint32
_Win32DiskDriveIndex_Object = MibTableColumn
win32DiskDriveIndex = _Win32DiskDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 11),
    _Win32DiskDriveIndex_Type()
)
win32DiskDriveIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveIndex.setStatus("mandatory")
_Win32DiskDriveManufacturer_Type = String
_Win32DiskDriveManufacturer_Object = MibTableColumn
win32DiskDriveManufacturer = _Win32DiskDriveManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 12),
    _Win32DiskDriveManufacturer_Type()
)
win32DiskDriveManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveManufacturer.setStatus("mandatory")
_Win32DiskDriveMediaLoaded_Type = Boolean
_Win32DiskDriveMediaLoaded_Object = MibTableColumn
win32DiskDriveMediaLoaded = _Win32DiskDriveMediaLoaded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 13),
    _Win32DiskDriveMediaLoaded_Type()
)
win32DiskDriveMediaLoaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveMediaLoaded.setStatus("mandatory")
_Win32DiskDriveMediaType_Type = String
_Win32DiskDriveMediaType_Object = MibTableColumn
win32DiskDriveMediaType = _Win32DiskDriveMediaType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 14),
    _Win32DiskDriveMediaType_Type()
)
win32DiskDriveMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveMediaType.setStatus("mandatory")
_Win32DiskDriveModel_Type = String
_Win32DiskDriveModel_Object = MibTableColumn
win32DiskDriveModel = _Win32DiskDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 15),
    _Win32DiskDriveModel_Type()
)
win32DiskDriveModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveModel.setStatus("mandatory")
_Win32DiskDriveSCSIBus_Type = Uint32
_Win32DiskDriveSCSIBus_Object = MibTableColumn
win32DiskDriveSCSIBus = _Win32DiskDriveSCSIBus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 16),
    _Win32DiskDriveSCSIBus_Type()
)
win32DiskDriveSCSIBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveSCSIBus.setStatus("mandatory")
_Win32DiskDriveSCSILogicalUnit_Type = Uint16
_Win32DiskDriveSCSILogicalUnit_Object = MibTableColumn
win32DiskDriveSCSILogicalUnit = _Win32DiskDriveSCSILogicalUnit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 17),
    _Win32DiskDriveSCSILogicalUnit_Type()
)
win32DiskDriveSCSILogicalUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveSCSILogicalUnit.setStatus("mandatory")
_Win32DiskDriveSCSIPort_Type = Uint16
_Win32DiskDriveSCSIPort_Object = MibTableColumn
win32DiskDriveSCSIPort = _Win32DiskDriveSCSIPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 18),
    _Win32DiskDriveSCSIPort_Type()
)
win32DiskDriveSCSIPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveSCSIPort.setStatus("mandatory")
_Win32DiskDriveSCSITargetId_Type = Uint16
_Win32DiskDriveSCSITargetId_Object = MibTableColumn
win32DiskDriveSCSITargetId = _Win32DiskDriveSCSITargetId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 19),
    _Win32DiskDriveSCSITargetId_Type()
)
win32DiskDriveSCSITargetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveSCSITargetId.setStatus("mandatory")
_Win32DiskDriveSize_Type = String
_Win32DiskDriveSize_Object = MibTableColumn
win32DiskDriveSize = _Win32DiskDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 20),
    _Win32DiskDriveSize_Type()
)
win32DiskDriveSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveSize.setStatus("mandatory")
_Win32DiskDriveStatus_Type = String
_Win32DiskDriveStatus_Object = MibTableColumn
win32DiskDriveStatus = _Win32DiskDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 30, 1, 21),
    _Win32DiskDriveStatus_Type()
)
win32DiskDriveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveStatus.setStatus("mandatory")
_Win32CDROMDriveTable_Object = MibTable
win32CDROMDriveTable = _Win32CDROMDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40)
)
if mibBuilder.loadTexts:
    win32CDROMDriveTable.setStatus("mandatory")
_Win32CDROMDriveEntry_Object = MibTableRow
win32CDROMDriveEntry = _Win32CDROMDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1)
)
win32CDROMDriveEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32CDROMDriveKeyIndex"),
)
if mibBuilder.loadTexts:
    win32CDROMDriveEntry.setStatus("mandatory")
_Win32CDROMDriveKeyIndex_Type = String
_Win32CDROMDriveKeyIndex_Object = MibTableColumn
win32CDROMDriveKeyIndex = _Win32CDROMDriveKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 1),
    _Win32CDROMDriveKeyIndex_Type()
)
win32CDROMDriveKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveKeyIndex.setStatus("mandatory")
_Win32CDROMDriveDrive_Type = String
_Win32CDROMDriveDrive_Object = MibTableColumn
win32CDROMDriveDrive = _Win32CDROMDriveDrive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 2),
    _Win32CDROMDriveDrive_Type()
)
win32CDROMDriveDrive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveDrive.setStatus("mandatory")
_Win32CDROMDriveFileSystemFlags_Type = Uint16
_Win32CDROMDriveFileSystemFlags_Object = MibTableColumn
win32CDROMDriveFileSystemFlags = _Win32CDROMDriveFileSystemFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 3),
    _Win32CDROMDriveFileSystemFlags_Type()
)
win32CDROMDriveFileSystemFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveFileSystemFlags.setStatus("mandatory")
_Win32CDROMDriveId_Type = String
_Win32CDROMDriveId_Object = MibTableColumn
win32CDROMDriveId = _Win32CDROMDriveId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 4),
    _Win32CDROMDriveId_Type()
)
win32CDROMDriveId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveId.setStatus("mandatory")
_Win32CDROMDriveManufacturer_Type = String
_Win32CDROMDriveManufacturer_Object = MibTableColumn
win32CDROMDriveManufacturer = _Win32CDROMDriveManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 5),
    _Win32CDROMDriveManufacturer_Type()
)
win32CDROMDriveManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveManufacturer.setStatus("mandatory")
_Win32CDROMDriveMaximumComponentLength_Type = Uint32
_Win32CDROMDriveMaximumComponentLength_Object = MibTableColumn
win32CDROMDriveMaximumComponentLength = _Win32CDROMDriveMaximumComponentLength_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 6),
    _Win32CDROMDriveMaximumComponentLength_Type()
)
win32CDROMDriveMaximumComponentLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveMaximumComponentLength.setStatus("mandatory")
_Win32CDROMDriveMediaType_Type = String
_Win32CDROMDriveMediaType_Object = MibTableColumn
win32CDROMDriveMediaType = _Win32CDROMDriveMediaType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 7),
    _Win32CDROMDriveMediaType_Type()
)
win32CDROMDriveMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveMediaType.setStatus("mandatory")
_Win32CDROMDriveRevisionLevel_Type = String
_Win32CDROMDriveRevisionLevel_Object = MibTableColumn
win32CDROMDriveRevisionLevel = _Win32CDROMDriveRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 8),
    _Win32CDROMDriveRevisionLevel_Type()
)
win32CDROMDriveRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveRevisionLevel.setStatus("mandatory")
_Win32CDROMDriveSCSITargetId_Type = Uint16
_Win32CDROMDriveSCSITargetId_Object = MibTableColumn
win32CDROMDriveSCSITargetId = _Win32CDROMDriveSCSITargetId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 9),
    _Win32CDROMDriveSCSITargetId_Type()
)
win32CDROMDriveSCSITargetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveSCSITargetId.setStatus("mandatory")
_Win32CDROMDriveVolumeName_Type = String
_Win32CDROMDriveVolumeName_Object = MibTableColumn
win32CDROMDriveVolumeName = _Win32CDROMDriveVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 10),
    _Win32CDROMDriveVolumeName_Type()
)
win32CDROMDriveVolumeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveVolumeName.setStatus("mandatory")
_Win32CDROMDriveVolumeSerialNumber_Type = String
_Win32CDROMDriveVolumeSerialNumber_Object = MibTableColumn
win32CDROMDriveVolumeSerialNumber = _Win32CDROMDriveVolumeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 11),
    _Win32CDROMDriveVolumeSerialNumber_Type()
)
win32CDROMDriveVolumeSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveVolumeSerialNumber.setStatus("mandatory")
_Win32CDROMDriveTransferRate_Type = Real64
_Win32CDROMDriveTransferRate_Object = MibTableColumn
win32CDROMDriveTransferRate = _Win32CDROMDriveTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 12),
    _Win32CDROMDriveTransferRate_Type()
)
win32CDROMDriveTransferRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveTransferRate.setStatus("mandatory")
_Win32CDROMDriveDriveIntegrity_Type = Boolean
_Win32CDROMDriveDriveIntegrity_Object = MibTableColumn
win32CDROMDriveDriveIntegrity = _Win32CDROMDriveDriveIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 13),
    _Win32CDROMDriveDriveIntegrity_Type()
)
win32CDROMDriveDriveIntegrity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveDriveIntegrity.setStatus("mandatory")
_Win32CDROMDriveMediaLoaded_Type = Boolean
_Win32CDROMDriveMediaLoaded_Object = MibTableColumn
win32CDROMDriveMediaLoaded = _Win32CDROMDriveMediaLoaded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 14),
    _Win32CDROMDriveMediaLoaded_Type()
)
win32CDROMDriveMediaLoaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveMediaLoaded.setStatus("mandatory")
_Win32CDROMDriveStatus_Type = String
_Win32CDROMDriveStatus_Object = MibTableColumn
win32CDROMDriveStatus = _Win32CDROMDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 40, 1, 15),
    _Win32CDROMDriveStatus_Type()
)
win32CDROMDriveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CDROMDriveStatus.setStatus("mandatory")
_Win32PointingDeviceTable_Object = MibTable
win32PointingDeviceTable = _Win32PointingDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 50)
)
if mibBuilder.loadTexts:
    win32PointingDeviceTable.setStatus("mandatory")
_Win32PointingDeviceEntry_Object = MibTableRow
win32PointingDeviceEntry = _Win32PointingDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 50, 1)
)
win32PointingDeviceEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32PointingDeviceKeyIndex"),
)
if mibBuilder.loadTexts:
    win32PointingDeviceEntry.setStatus("mandatory")
_Win32PointingDeviceKeyIndex_Type = String
_Win32PointingDeviceKeyIndex_Object = MibTableColumn
win32PointingDeviceKeyIndex = _Win32PointingDeviceKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 50, 1, 1),
    _Win32PointingDeviceKeyIndex_Type()
)
win32PointingDeviceKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PointingDeviceKeyIndex.setStatus("mandatory")
_Win32PointingDeviceHardwareType_Type = String
_Win32PointingDeviceHardwareType_Object = MibTableColumn
win32PointingDeviceHardwareType = _Win32PointingDeviceHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 50, 1, 2),
    _Win32PointingDeviceHardwareType_Type()
)
win32PointingDeviceHardwareType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PointingDeviceHardwareType.setStatus("mandatory")
_Win32PointingDeviceInfFileName_Type = String
_Win32PointingDeviceInfFileName_Object = MibTableColumn
win32PointingDeviceInfFileName = _Win32PointingDeviceInfFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 50, 1, 3),
    _Win32PointingDeviceInfFileName_Type()
)
win32PointingDeviceInfFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PointingDeviceInfFileName.setStatus("mandatory")
_Win32PointingDeviceInfSection_Type = String
_Win32PointingDeviceInfSection_Object = MibTableColumn
win32PointingDeviceInfSection = _Win32PointingDeviceInfSection_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 50, 1, 4),
    _Win32PointingDeviceInfSection_Type()
)
win32PointingDeviceInfSection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PointingDeviceInfSection.setStatus("mandatory")
_Win32PointingDeviceSampleRate_Type = Uint32
_Win32PointingDeviceSampleRate_Object = MibTableColumn
win32PointingDeviceSampleRate = _Win32PointingDeviceSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 50, 1, 5),
    _Win32PointingDeviceSampleRate_Type()
)
win32PointingDeviceSampleRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PointingDeviceSampleRate.setStatus("mandatory")
_Win32PointingDeviceSynch_Type = Uint32
_Win32PointingDeviceSynch_Object = MibTableColumn
win32PointingDeviceSynch = _Win32PointingDeviceSynch_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 50, 1, 6),
    _Win32PointingDeviceSynch_Type()
)
win32PointingDeviceSynch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PointingDeviceSynch.setStatus("mandatory")
_Win32PointingDeviceDoubleSpeedThreshold_Type = Uint32
_Win32PointingDeviceDoubleSpeedThreshold_Object = MibTableColumn
win32PointingDeviceDoubleSpeedThreshold = _Win32PointingDeviceDoubleSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 50, 1, 7),
    _Win32PointingDeviceDoubleSpeedThreshold_Type()
)
win32PointingDeviceDoubleSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PointingDeviceDoubleSpeedThreshold.setStatus("mandatory")
_Win32PointingDeviceQuadSpeedThreshold_Type = Uint32
_Win32PointingDeviceQuadSpeedThreshold_Object = MibTableColumn
win32PointingDeviceQuadSpeedThreshold = _Win32PointingDeviceQuadSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 50, 1, 8),
    _Win32PointingDeviceQuadSpeedThreshold_Type()
)
win32PointingDeviceQuadSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PointingDeviceQuadSpeedThreshold.setStatus("mandatory")
_Win32PointingDeviceStatus_Type = String
_Win32PointingDeviceStatus_Object = MibTableColumn
win32PointingDeviceStatus = _Win32PointingDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 50, 1, 9),
    _Win32PointingDeviceStatus_Type()
)
win32PointingDeviceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PointingDeviceStatus.setStatus("mandatory")
_Win32LogicalDiskTable_Object = MibTable
win32LogicalDiskTable = _Win32LogicalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70)
)
if mibBuilder.loadTexts:
    win32LogicalDiskTable.setStatus("mandatory")
_Win32LogicalDiskEntry_Object = MibTableRow
win32LogicalDiskEntry = _Win32LogicalDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70, 1)
)
win32LogicalDiskEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32LogicalDiskKeyIndex"),
)
if mibBuilder.loadTexts:
    win32LogicalDiskEntry.setStatus("mandatory")
_Win32LogicalDiskKeyIndex_Type = String
_Win32LogicalDiskKeyIndex_Object = MibTableColumn
win32LogicalDiskKeyIndex = _Win32LogicalDiskKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70, 1, 1),
    _Win32LogicalDiskKeyIndex_Type()
)
win32LogicalDiskKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskKeyIndex.setStatus("mandatory")
_Win32LogicalDiskCompressed_Type = Boolean
_Win32LogicalDiskCompressed_Object = MibTableColumn
win32LogicalDiskCompressed = _Win32LogicalDiskCompressed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70, 1, 2),
    _Win32LogicalDiskCompressed_Type()
)
win32LogicalDiskCompressed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskCompressed.setStatus("mandatory")
_Win32LogicalDiskDriveType_Type = Uint32
_Win32LogicalDiskDriveType_Object = MibTableColumn
win32LogicalDiskDriveType = _Win32LogicalDiskDriveType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70, 1, 3),
    _Win32LogicalDiskDriveType_Type()
)
win32LogicalDiskDriveType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskDriveType.setStatus("mandatory")
_Win32LogicalDiskFileSystem_Type = String
_Win32LogicalDiskFileSystem_Object = MibTableColumn
win32LogicalDiskFileSystem = _Win32LogicalDiskFileSystem_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70, 1, 4),
    _Win32LogicalDiskFileSystem_Type()
)
win32LogicalDiskFileSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskFileSystem.setStatus("mandatory")
_Win32LogicalDiskFreeSpace_Type = String
_Win32LogicalDiskFreeSpace_Object = MibTableColumn
win32LogicalDiskFreeSpace = _Win32LogicalDiskFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70, 1, 5),
    _Win32LogicalDiskFreeSpace_Type()
)
win32LogicalDiskFreeSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskFreeSpace.setStatus("mandatory")
_Win32LogicalDiskMaximumComponentLength_Type = Uint32
_Win32LogicalDiskMaximumComponentLength_Object = MibTableColumn
win32LogicalDiskMaximumComponentLength = _Win32LogicalDiskMaximumComponentLength_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70, 1, 6),
    _Win32LogicalDiskMaximumComponentLength_Type()
)
win32LogicalDiskMaximumComponentLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskMaximumComponentLength.setStatus("mandatory")
_Win32LogicalDiskProviderName_Type = String
_Win32LogicalDiskProviderName_Object = MibTableColumn
win32LogicalDiskProviderName = _Win32LogicalDiskProviderName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70, 1, 7),
    _Win32LogicalDiskProviderName_Type()
)
win32LogicalDiskProviderName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskProviderName.setStatus("mandatory")
_Win32LogicalDiskSize_Type = String
_Win32LogicalDiskSize_Object = MibTableColumn
win32LogicalDiskSize = _Win32LogicalDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70, 1, 8),
    _Win32LogicalDiskSize_Type()
)
win32LogicalDiskSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskSize.setStatus("mandatory")
_Win32LogicalDiskSupportsFileBasedCompression_Type = Boolean
_Win32LogicalDiskSupportsFileBasedCompression_Object = MibTableColumn
win32LogicalDiskSupportsFileBasedCompression = _Win32LogicalDiskSupportsFileBasedCompression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70, 1, 9),
    _Win32LogicalDiskSupportsFileBasedCompression_Type()
)
win32LogicalDiskSupportsFileBasedCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskSupportsFileBasedCompression.setStatus("mandatory")
_Win32LogicalDiskVolumeName_Type = String
_Win32LogicalDiskVolumeName_Object = MibTableColumn
win32LogicalDiskVolumeName = _Win32LogicalDiskVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70, 1, 10),
    _Win32LogicalDiskVolumeName_Type()
)
win32LogicalDiskVolumeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskVolumeName.setStatus("mandatory")
_Win32LogicalDiskVolumeSerialNumber_Type = String
_Win32LogicalDiskVolumeSerialNumber_Object = MibTableColumn
win32LogicalDiskVolumeSerialNumber = _Win32LogicalDiskVolumeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70, 1, 11),
    _Win32LogicalDiskVolumeSerialNumber_Type()
)
win32LogicalDiskVolumeSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskVolumeSerialNumber.setStatus("mandatory")
_Win32LogicalDiskMediaType_Type = Uint32
_Win32LogicalDiskMediaType_Object = MibTableColumn
win32LogicalDiskMediaType = _Win32LogicalDiskMediaType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70, 1, 12),
    _Win32LogicalDiskMediaType_Type()
)
win32LogicalDiskMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskMediaType.setStatus("mandatory")
_Win32LogicalDiskStatus_Type = String
_Win32LogicalDiskStatus_Object = MibTableColumn
win32LogicalDiskStatus = _Win32LogicalDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 70, 1, 13),
    _Win32LogicalDiskStatus_Type()
)
win32LogicalDiskStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskStatus.setStatus("mandatory")
_Win32DiskPartitionTable_Object = MibTable
win32DiskPartitionTable = _Win32DiskPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 80)
)
if mibBuilder.loadTexts:
    win32DiskPartitionTable.setStatus("mandatory")
_Win32DiskPartitionEntry_Object = MibTableRow
win32DiskPartitionEntry = _Win32DiskPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 80, 1)
)
win32DiskPartitionEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32DiskPartitionKeyIndex"),
)
if mibBuilder.loadTexts:
    win32DiskPartitionEntry.setStatus("mandatory")
_Win32DiskPartitionKeyIndex_Type = String
_Win32DiskPartitionKeyIndex_Object = MibTableColumn
win32DiskPartitionKeyIndex = _Win32DiskPartitionKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 80, 1, 1),
    _Win32DiskPartitionKeyIndex_Type()
)
win32DiskPartitionKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskPartitionKeyIndex.setStatus("mandatory")
_Win32DiskPartitionBootPartition_Type = Boolean
_Win32DiskPartitionBootPartition_Object = MibTableColumn
win32DiskPartitionBootPartition = _Win32DiskPartitionBootPartition_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 80, 1, 2),
    _Win32DiskPartitionBootPartition_Type()
)
win32DiskPartitionBootPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskPartitionBootPartition.setStatus("mandatory")
_Win32DiskPartitionDiskIndex_Type = Uint32
_Win32DiskPartitionDiskIndex_Object = MibTableColumn
win32DiskPartitionDiskIndex = _Win32DiskPartitionDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 80, 1, 3),
    _Win32DiskPartitionDiskIndex_Type()
)
win32DiskPartitionDiskIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskPartitionDiskIndex.setStatus("mandatory")
_Win32DiskPartitionHiddenSectors_Type = Uint32
_Win32DiskPartitionHiddenSectors_Object = MibTableColumn
win32DiskPartitionHiddenSectors = _Win32DiskPartitionHiddenSectors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 80, 1, 4),
    _Win32DiskPartitionHiddenSectors_Type()
)
win32DiskPartitionHiddenSectors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskPartitionHiddenSectors.setStatus("mandatory")
_Win32DiskPartitionIndex_Type = Uint32
_Win32DiskPartitionIndex_Object = MibTableColumn
win32DiskPartitionIndex = _Win32DiskPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 80, 1, 5),
    _Win32DiskPartitionIndex_Type()
)
win32DiskPartitionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskPartitionIndex.setStatus("mandatory")
_Win32DiskPartitionRewritePartition_Type = Boolean
_Win32DiskPartitionRewritePartition_Object = MibTableColumn
win32DiskPartitionRewritePartition = _Win32DiskPartitionRewritePartition_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 80, 1, 6),
    _Win32DiskPartitionRewritePartition_Type()
)
win32DiskPartitionRewritePartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskPartitionRewritePartition.setStatus("mandatory")
_Win32DiskPartitionSize_Type = String
_Win32DiskPartitionSize_Object = MibTableColumn
win32DiskPartitionSize = _Win32DiskPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 80, 1, 7),
    _Win32DiskPartitionSize_Type()
)
win32DiskPartitionSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskPartitionSize.setStatus("mandatory")
_Win32DiskPartitionStartingOffset_Type = String
_Win32DiskPartitionStartingOffset_Object = MibTableColumn
win32DiskPartitionStartingOffset = _Win32DiskPartitionStartingOffset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 80, 1, 8),
    _Win32DiskPartitionStartingOffset_Type()
)
win32DiskPartitionStartingOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskPartitionStartingOffset.setStatus("mandatory")
_Win32DiskPartitionType_Type = String
_Win32DiskPartitionType_Object = MibTableColumn
win32DiskPartitionType = _Win32DiskPartitionType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 80, 1, 9),
    _Win32DiskPartitionType_Type()
)
win32DiskPartitionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskPartitionType.setStatus("mandatory")
_Win32DiskPartitionStatus_Type = String
_Win32DiskPartitionStatus_Object = MibTableColumn
win32DiskPartitionStatus = _Win32DiskPartitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 80, 1, 10),
    _Win32DiskPartitionStatus_Type()
)
win32DiskPartitionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskPartitionStatus.setStatus("mandatory")
_Win32BatteryTable_Object = MibTable
win32BatteryTable = _Win32BatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 90)
)
if mibBuilder.loadTexts:
    win32BatteryTable.setStatus("mandatory")
_Win32BatteryEntry_Object = MibTableRow
win32BatteryEntry = _Win32BatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 90, 1)
)
win32BatteryEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32BatteryKeyIndex"),
)
if mibBuilder.loadTexts:
    win32BatteryEntry.setStatus("mandatory")
_Win32BatteryKeyIndex_Type = String
_Win32BatteryKeyIndex_Object = MibTableColumn
win32BatteryKeyIndex = _Win32BatteryKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 90, 1, 1),
    _Win32BatteryKeyIndex_Type()
)
win32BatteryKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BatteryKeyIndex.setStatus("mandatory")
_Win32BatteryExpectedBatteryLife_Type = Uint16
_Win32BatteryExpectedBatteryLife_Object = MibTableColumn
win32BatteryExpectedBatteryLife = _Win32BatteryExpectedBatteryLife_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 90, 1, 2),
    _Win32BatteryExpectedBatteryLife_Type()
)
win32BatteryExpectedBatteryLife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BatteryExpectedBatteryLife.setStatus("mandatory")
_Win32BatteryBatteryRechargeTime_Type = Uint16
_Win32BatteryBatteryRechargeTime_Object = MibTableColumn
win32BatteryBatteryRechargeTime = _Win32BatteryBatteryRechargeTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 90, 1, 3),
    _Win32BatteryBatteryRechargeTime_Type()
)
win32BatteryBatteryRechargeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BatteryBatteryRechargeTime.setStatus("mandatory")
_Win32BatteryBatteryStatus_Type = String
_Win32BatteryBatteryStatus_Object = MibTableColumn
win32BatteryBatteryStatus = _Win32BatteryBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 90, 1, 4),
    _Win32BatteryBatteryStatus_Type()
)
win32BatteryBatteryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BatteryBatteryStatus.setStatus("mandatory")
_Win32MotherboardDeviceTable_Object = MibTable
win32MotherboardDeviceTable = _Win32MotherboardDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 100)
)
if mibBuilder.loadTexts:
    win32MotherboardDeviceTable.setStatus("mandatory")
_Win32MotherboardDeviceEntry_Object = MibTableRow
win32MotherboardDeviceEntry = _Win32MotherboardDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 100, 1)
)
win32MotherboardDeviceEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32MotherboardDeviceKeyIndex"),
)
if mibBuilder.loadTexts:
    win32MotherboardDeviceEntry.setStatus("mandatory")
_Win32MotherboardDeviceKeyIndex_Type = String
_Win32MotherboardDeviceKeyIndex_Object = MibTableColumn
win32MotherboardDeviceKeyIndex = _Win32MotherboardDeviceKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 100, 1, 1),
    _Win32MotherboardDeviceKeyIndex_Type()
)
win32MotherboardDeviceKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32MotherboardDeviceKeyIndex.setStatus("mandatory")
_Win32MotherboardDevicePrimaryBusType_Type = String
_Win32MotherboardDevicePrimaryBusType_Object = MibTableColumn
win32MotherboardDevicePrimaryBusType = _Win32MotherboardDevicePrimaryBusType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 100, 1, 2),
    _Win32MotherboardDevicePrimaryBusType_Type()
)
win32MotherboardDevicePrimaryBusType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32MotherboardDevicePrimaryBusType.setStatus("mandatory")
_Win32MotherboardDeviceRevisionNumber_Type = String
_Win32MotherboardDeviceRevisionNumber_Object = MibTableColumn
win32MotherboardDeviceRevisionNumber = _Win32MotherboardDeviceRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 100, 1, 3),
    _Win32MotherboardDeviceRevisionNumber_Type()
)
win32MotherboardDeviceRevisionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32MotherboardDeviceRevisionNumber.setStatus("mandatory")
_Win32MotherboardDeviceSecondaryBusType_Type = String
_Win32MotherboardDeviceSecondaryBusType_Object = MibTableColumn
win32MotherboardDeviceSecondaryBusType = _Win32MotherboardDeviceSecondaryBusType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 100, 1, 4),
    _Win32MotherboardDeviceSecondaryBusType_Type()
)
win32MotherboardDeviceSecondaryBusType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32MotherboardDeviceSecondaryBusType.setStatus("mandatory")
_Win32MotherboardDeviceStatus_Type = String
_Win32MotherboardDeviceStatus_Object = MibTableColumn
win32MotherboardDeviceStatus = _Win32MotherboardDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 100, 1, 5),
    _Win32MotherboardDeviceStatus_Type()
)
win32MotherboardDeviceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32MotherboardDeviceStatus.setStatus("mandatory")
_Win32ProcessorTable_Object = MibTable
win32ProcessorTable = _Win32ProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 110)
)
if mibBuilder.loadTexts:
    win32ProcessorTable.setStatus("mandatory")
_Win32ProcessorEntry_Object = MibTableRow
win32ProcessorEntry = _Win32ProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 110, 1)
)
win32ProcessorEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32ProcessorKeyIndex"),
)
if mibBuilder.loadTexts:
    win32ProcessorEntry.setStatus("mandatory")
_Win32ProcessorKeyIndex_Type = String
_Win32ProcessorKeyIndex_Object = MibTableColumn
win32ProcessorKeyIndex = _Win32ProcessorKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 110, 1, 1),
    _Win32ProcessorKeyIndex_Type()
)
win32ProcessorKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessorKeyIndex.setStatus("mandatory")
_Win32ProcessorVersion_Type = String
_Win32ProcessorVersion_Object = MibTableColumn
win32ProcessorVersion = _Win32ProcessorVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 110, 1, 2),
    _Win32ProcessorVersion_Type()
)
win32ProcessorVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessorVersion.setStatus("mandatory")
_Win32ProcessorManufacturer_Type = String
_Win32ProcessorManufacturer_Object = MibTableColumn
win32ProcessorManufacturer = _Win32ProcessorManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 110, 1, 3),
    _Win32ProcessorManufacturer_Type()
)
win32ProcessorManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessorManufacturer.setStatus("mandatory")
_Win32ProcessorL2CacheSize_Type = Uint32
_Win32ProcessorL2CacheSize_Object = MibTableColumn
win32ProcessorL2CacheSize = _Win32ProcessorL2CacheSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 110, 1, 4),
    _Win32ProcessorL2CacheSize_Type()
)
win32ProcessorL2CacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessorL2CacheSize.setStatus("mandatory")
_Win32ProcessorL2CacheSpeed_Type = Uint32
_Win32ProcessorL2CacheSpeed_Object = MibTableColumn
win32ProcessorL2CacheSpeed = _Win32ProcessorL2CacheSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 110, 1, 5),
    _Win32ProcessorL2CacheSpeed_Type()
)
win32ProcessorL2CacheSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessorL2CacheSpeed.setStatus("mandatory")
_Win32ProcessorArchitecture_Type = Uint16
_Win32ProcessorArchitecture_Object = MibTableColumn
win32ProcessorArchitecture = _Win32ProcessorArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 110, 1, 6),
    _Win32ProcessorArchitecture_Type()
)
win32ProcessorArchitecture.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessorArchitecture.setStatus("mandatory")
_Win32ProcessorLevel_Type = Uint16
_Win32ProcessorLevel_Object = MibTableColumn
win32ProcessorLevel = _Win32ProcessorLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 110, 1, 7),
    _Win32ProcessorLevel_Type()
)
win32ProcessorLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessorLevel.setStatus("mandatory")
_Win32ProcessorRevision_Type = Uint16
_Win32ProcessorRevision_Object = MibTableColumn
win32ProcessorRevision = _Win32ProcessorRevision_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 110, 1, 8),
    _Win32ProcessorRevision_Type()
)
win32ProcessorRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessorRevision.setStatus("mandatory")
_Win32ProcessorStatus_Type = String
_Win32ProcessorStatus_Object = MibTableColumn
win32ProcessorStatus = _Win32ProcessorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 110, 1, 9),
    _Win32ProcessorStatus_Type()
)
win32ProcessorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessorStatus.setStatus("mandatory")
_Win32PrinterTable_Object = MibTable
win32PrinterTable = _Win32PrinterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120)
)
if mibBuilder.loadTexts:
    win32PrinterTable.setStatus("mandatory")
_Win32PrinterEntry_Object = MibTableRow
win32PrinterEntry = _Win32PrinterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1)
)
win32PrinterEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32PrinterKeyIndex"),
)
if mibBuilder.loadTexts:
    win32PrinterEntry.setStatus("mandatory")
_Win32PrinterKeyIndex_Type = String
_Win32PrinterKeyIndex_Object = MibTableColumn
win32PrinterKeyIndex = _Win32PrinterKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 1),
    _Win32PrinterKeyIndex_Type()
)
win32PrinterKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterKeyIndex.setStatus("mandatory")
_Win32PrinterAttributes_Type = Uint32
_Win32PrinterAttributes_Object = MibTableColumn
win32PrinterAttributes = _Win32PrinterAttributes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 2),
    _Win32PrinterAttributes_Type()
)
win32PrinterAttributes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterAttributes.setStatus("mandatory")
_Win32PrinterDriverName_Type = String
_Win32PrinterDriverName_Object = MibTableColumn
win32PrinterDriverName = _Win32PrinterDriverName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 3),
    _Win32PrinterDriverName_Type()
)
win32PrinterDriverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterDriverName.setStatus("mandatory")
_Win32PrinterLocation_Type = String
_Win32PrinterLocation_Object = MibTableColumn
win32PrinterLocation = _Win32PrinterLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 4),
    _Win32PrinterLocation_Type()
)
win32PrinterLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterLocation.setStatus("mandatory")
_Win32PrinterPrinterPaperNames_Type = String
_Win32PrinterPrinterPaperNames_Object = MibTableColumn
win32PrinterPrinterPaperNames = _Win32PrinterPrinterPaperNames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 5),
    _Win32PrinterPrinterPaperNames_Type()
)
win32PrinterPrinterPaperNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterPrinterPaperNames.setStatus("mandatory")
_Win32PrinterPortName_Type = String
_Win32PrinterPortName_Object = MibTableColumn
win32PrinterPortName = _Win32PrinterPortName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 6),
    _Win32PrinterPortName_Type()
)
win32PrinterPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterPortName.setStatus("mandatory")
_Win32PrinterPrintJobDataType_Type = String
_Win32PrinterPrintJobDataType_Object = MibTableColumn
win32PrinterPrintJobDataType = _Win32PrinterPrintJobDataType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 7),
    _Win32PrinterPrintJobDataType_Type()
)
win32PrinterPrintJobDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterPrintJobDataType.setStatus("mandatory")
_Win32PrinterSeparatorFile_Type = String
_Win32PrinterSeparatorFile_Object = MibTableColumn
win32PrinterSeparatorFile = _Win32PrinterSeparatorFile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 8),
    _Win32PrinterSeparatorFile_Type()
)
win32PrinterSeparatorFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterSeparatorFile.setStatus("mandatory")
_Win32PrinterServerName_Type = String
_Win32PrinterServerName_Object = MibTableColumn
win32PrinterServerName = _Win32PrinterServerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 9),
    _Win32PrinterServerName_Type()
)
win32PrinterServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterServerName.setStatus("mandatory")
_Win32PrinterShareName_Type = String
_Win32PrinterShareName_Object = MibTableColumn
win32PrinterShareName = _Win32PrinterShareName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 10),
    _Win32PrinterShareName_Type()
)
win32PrinterShareName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterShareName.setStatus("mandatory")
_Win32PrinterStartTime_Type = Datetime
_Win32PrinterStartTime_Object = MibTableColumn
win32PrinterStartTime = _Win32PrinterStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 11),
    _Win32PrinterStartTime_Type()
)
win32PrinterStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterStartTime.setStatus("mandatory")
_Win32PrinterUntilTime_Type = Datetime
_Win32PrinterUntilTime_Object = MibTableColumn
win32PrinterUntilTime = _Win32PrinterUntilTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 12),
    _Win32PrinterUntilTime_Type()
)
win32PrinterUntilTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterUntilTime.setStatus("mandatory")
_Win32PrinterDefaultPriority_Type = Uint32
_Win32PrinterDefaultPriority_Object = MibTableColumn
win32PrinterDefaultPriority = _Win32PrinterDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 13),
    _Win32PrinterDefaultPriority_Type()
)
win32PrinterDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterDefaultPriority.setStatus("mandatory")
_Win32PrinterAveragePagesPerMinute_Type = Uint32
_Win32PrinterAveragePagesPerMinute_Object = MibTableColumn
win32PrinterAveragePagesPerMinute = _Win32PrinterAveragePagesPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 14),
    _Win32PrinterAveragePagesPerMinute_Type()
)
win32PrinterAveragePagesPerMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterAveragePagesPerMinute.setStatus("mandatory")
_Win32PrinterPrintProcessor_Type = String
_Win32PrinterPrintProcessor_Object = MibTableColumn
win32PrinterPrintProcessor = _Win32PrinterPrintProcessor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 15),
    _Win32PrinterPrintProcessor_Type()
)
win32PrinterPrintProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterPrintProcessor.setStatus("mandatory")
_Win32PrinterStatus_Type = String
_Win32PrinterStatus_Object = MibTableColumn
win32PrinterStatus = _Win32PrinterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 120, 1, 16),
    _Win32PrinterStatus_Type()
)
win32PrinterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterStatus.setStatus("mandatory")
_Win32UninterruptiblePowerSupplyTable_Object = MibTable
win32UninterruptiblePowerSupplyTable = _Win32UninterruptiblePowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 130)
)
if mibBuilder.loadTexts:
    win32UninterruptiblePowerSupplyTable.setStatus("mandatory")
_Win32UninterruptiblePowerSupplyEntry_Object = MibTableRow
win32UninterruptiblePowerSupplyEntry = _Win32UninterruptiblePowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 130, 1)
)
win32UninterruptiblePowerSupplyEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32UninterruptiblePowerSupplyKeyIndex"),
)
if mibBuilder.loadTexts:
    win32UninterruptiblePowerSupplyEntry.setStatus("mandatory")
_Win32UninterruptiblePowerSupplyKeyIndex_Type = String
_Win32UninterruptiblePowerSupplyKeyIndex_Object = MibTableColumn
win32UninterruptiblePowerSupplyKeyIndex = _Win32UninterruptiblePowerSupplyKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 130, 1, 1),
    _Win32UninterruptiblePowerSupplyKeyIndex_Type()
)
win32UninterruptiblePowerSupplyKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UninterruptiblePowerSupplyKeyIndex.setStatus("mandatory")
_Win32UninterruptiblePowerSupplyBatteryInstalled_Type = Boolean
_Win32UninterruptiblePowerSupplyBatteryInstalled_Object = MibTableColumn
win32UninterruptiblePowerSupplyBatteryInstalled = _Win32UninterruptiblePowerSupplyBatteryInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 130, 1, 2),
    _Win32UninterruptiblePowerSupplyBatteryInstalled_Type()
)
win32UninterruptiblePowerSupplyBatteryInstalled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UninterruptiblePowerSupplyBatteryInstalled.setStatus("mandatory")
_Win32UninterruptiblePowerSupplyCanTurnOffRemotely_Type = Boolean
_Win32UninterruptiblePowerSupplyCanTurnOffRemotely_Object = MibTableColumn
win32UninterruptiblePowerSupplyCanTurnOffRemotely = _Win32UninterruptiblePowerSupplyCanTurnOffRemotely_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 130, 1, 3),
    _Win32UninterruptiblePowerSupplyCanTurnOffRemotely_Type()
)
win32UninterruptiblePowerSupplyCanTurnOffRemotely.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UninterruptiblePowerSupplyCanTurnOffRemotely.setStatus("mandatory")
_Win32UninterruptiblePowerSupplyCommandFile_Type = String
_Win32UninterruptiblePowerSupplyCommandFile_Object = MibTableColumn
win32UninterruptiblePowerSupplyCommandFile = _Win32UninterruptiblePowerSupplyCommandFile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 130, 1, 4),
    _Win32UninterruptiblePowerSupplyCommandFile_Type()
)
win32UninterruptiblePowerSupplyCommandFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UninterruptiblePowerSupplyCommandFile.setStatus("mandatory")
_Win32UninterruptiblePowerSupplyFirstMessageDelay_Type = Uint32
_Win32UninterruptiblePowerSupplyFirstMessageDelay_Object = MibTableColumn
win32UninterruptiblePowerSupplyFirstMessageDelay = _Win32UninterruptiblePowerSupplyFirstMessageDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 130, 1, 5),
    _Win32UninterruptiblePowerSupplyFirstMessageDelay_Type()
)
win32UninterruptiblePowerSupplyFirstMessageDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UninterruptiblePowerSupplyFirstMessageDelay.setStatus("mandatory")
_Win32UninterruptiblePowerSupplyLowBatterySignal_Type = Boolean
_Win32UninterruptiblePowerSupplyLowBatterySignal_Object = MibTableColumn
win32UninterruptiblePowerSupplyLowBatterySignal = _Win32UninterruptiblePowerSupplyLowBatterySignal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 130, 1, 6),
    _Win32UninterruptiblePowerSupplyLowBatterySignal_Type()
)
win32UninterruptiblePowerSupplyLowBatterySignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UninterruptiblePowerSupplyLowBatterySignal.setStatus("mandatory")
_Win32UninterruptiblePowerSupplyMessageInterval_Type = Uint32
_Win32UninterruptiblePowerSupplyMessageInterval_Object = MibTableColumn
win32UninterruptiblePowerSupplyMessageInterval = _Win32UninterruptiblePowerSupplyMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 130, 1, 7),
    _Win32UninterruptiblePowerSupplyMessageInterval_Type()
)
win32UninterruptiblePowerSupplyMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UninterruptiblePowerSupplyMessageInterval.setStatus("mandatory")
_Win32UninterruptiblePowerSupplyPowerFailSignal_Type = Boolean
_Win32UninterruptiblePowerSupplyPowerFailSignal_Object = MibTableColumn
win32UninterruptiblePowerSupplyPowerFailSignal = _Win32UninterruptiblePowerSupplyPowerFailSignal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 130, 1, 8),
    _Win32UninterruptiblePowerSupplyPowerFailSignal_Type()
)
win32UninterruptiblePowerSupplyPowerFailSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UninterruptiblePowerSupplyPowerFailSignal.setStatus("mandatory")
_Win32UninterruptiblePowerSupplyUPSPort_Type = String
_Win32UninterruptiblePowerSupplyUPSPort_Object = MibTableColumn
win32UninterruptiblePowerSupplyUPSPort = _Win32UninterruptiblePowerSupplyUPSPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 130, 1, 9),
    _Win32UninterruptiblePowerSupplyUPSPort_Type()
)
win32UninterruptiblePowerSupplyUPSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UninterruptiblePowerSupplyUPSPort.setStatus("mandatory")
_Win32UninterruptiblePowerSupplyStatus_Type = String
_Win32UninterruptiblePowerSupplyStatus_Object = MibTableColumn
win32UninterruptiblePowerSupplyStatus = _Win32UninterruptiblePowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 130, 1, 10),
    _Win32UninterruptiblePowerSupplyStatus_Type()
)
win32UninterruptiblePowerSupplyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UninterruptiblePowerSupplyStatus.setStatus("mandatory")
_Win32POTSModemTable_Object = MibTable
win32POTSModemTable = _Win32POTSModemTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140)
)
if mibBuilder.loadTexts:
    win32POTSModemTable.setStatus("mandatory")
_Win32POTSModemEntry_Object = MibTableRow
win32POTSModemEntry = _Win32POTSModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1)
)
win32POTSModemEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32POTSModemKeyIndex"),
)
if mibBuilder.loadTexts:
    win32POTSModemEntry.setStatus("mandatory")
_Win32POTSModemKeyIndex_Type = String
_Win32POTSModemKeyIndex_Object = MibTableColumn
win32POTSModemKeyIndex = _Win32POTSModemKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 1),
    _Win32POTSModemKeyIndex_Type()
)
win32POTSModemKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemKeyIndex.setStatus("mandatory")
_Win32POTSModemAttachedTo_Type = String
_Win32POTSModemAttachedTo_Object = MibTableColumn
win32POTSModemAttachedTo = _Win32POTSModemAttachedTo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 2),
    _Win32POTSModemAttachedTo_Type()
)
win32POTSModemAttachedTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemAttachedTo.setStatus("mandatory")
_Win32POTSModemBlindOff_Type = String
_Win32POTSModemBlindOff_Object = MibTableColumn
win32POTSModemBlindOff = _Win32POTSModemBlindOff_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 3),
    _Win32POTSModemBlindOff_Type()
)
win32POTSModemBlindOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemBlindOff.setStatus("mandatory")
_Win32POTSModemBlindOn_Type = String
_Win32POTSModemBlindOn_Object = MibTableColumn
win32POTSModemBlindOn = _Win32POTSModemBlindOn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 4),
    _Win32POTSModemBlindOn_Type()
)
win32POTSModemBlindOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemBlindOn.setStatus("mandatory")
_Win32POTSModemCompatibilityFlags_Type = String
_Win32POTSModemCompatibilityFlags_Object = MibTableColumn
win32POTSModemCompatibilityFlags = _Win32POTSModemCompatibilityFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 5),
    _Win32POTSModemCompatibilityFlags_Type()
)
win32POTSModemCompatibilityFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemCompatibilityFlags.setStatus("mandatory")
_Win32POTSModemCompressionOff_Type = String
_Win32POTSModemCompressionOff_Object = MibTableColumn
win32POTSModemCompressionOff = _Win32POTSModemCompressionOff_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 6),
    _Win32POTSModemCompressionOff_Type()
)
win32POTSModemCompressionOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemCompressionOff.setStatus("mandatory")
_Win32POTSModemCompressionOn_Type = String
_Win32POTSModemCompressionOn_Object = MibTableColumn
win32POTSModemCompressionOn = _Win32POTSModemCompressionOn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 7),
    _Win32POTSModemCompressionOn_Type()
)
win32POTSModemCompressionOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemCompressionOn.setStatus("mandatory")
_Win32POTSModemConfigurationDialog_Type = String
_Win32POTSModemConfigurationDialog_Object = MibTableColumn
win32POTSModemConfigurationDialog = _Win32POTSModemConfigurationDialog_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 8),
    _Win32POTSModemConfigurationDialog_Type()
)
win32POTSModemConfigurationDialog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemConfigurationDialog.setStatus("mandatory")
_Win32POTSModemDCB_Type = Uint8
_Win32POTSModemDCB_Object = MibTableColumn
win32POTSModemDCB = _Win32POTSModemDCB_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 9),
    _Win32POTSModemDCB_Type()
)
win32POTSModemDCB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemDCB.setStatus("mandatory")
_Win32POTSModemDefault_Type = Uint8
_Win32POTSModemDefault_Object = MibTableColumn
win32POTSModemDefault = _Win32POTSModemDefault_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 10),
    _Win32POTSModemDefault_Type()
)
win32POTSModemDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemDefault.setStatus("mandatory")
_Win32POTSModemDeviceLoader_Type = String
_Win32POTSModemDeviceLoader_Object = MibTableColumn
win32POTSModemDeviceLoader = _Win32POTSModemDeviceLoader_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 11),
    _Win32POTSModemDeviceLoader_Type()
)
win32POTSModemDeviceLoader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemDeviceLoader.setStatus("mandatory")
_Win32POTSModemDeviceType_Type = String
_Win32POTSModemDeviceType_Object = MibTableColumn
win32POTSModemDeviceType = _Win32POTSModemDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 12),
    _Win32POTSModemDeviceType_Type()
)
win32POTSModemDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemDeviceType.setStatus("mandatory")
_Win32POTSModemDriverDate_Type = Datetime
_Win32POTSModemDriverDate_Object = MibTableColumn
win32POTSModemDriverDate = _Win32POTSModemDriverDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 13),
    _Win32POTSModemDriverDate_Type()
)
win32POTSModemDriverDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemDriverDate.setStatus("mandatory")
_Win32POTSModemErrorControlForced_Type = String
_Win32POTSModemErrorControlForced_Object = MibTableColumn
win32POTSModemErrorControlForced = _Win32POTSModemErrorControlForced_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 14),
    _Win32POTSModemErrorControlForced_Type()
)
win32POTSModemErrorControlForced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemErrorControlForced.setStatus("mandatory")
_Win32POTSModemErrorControlOff_Type = String
_Win32POTSModemErrorControlOff_Object = MibTableColumn
win32POTSModemErrorControlOff = _Win32POTSModemErrorControlOff_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 15),
    _Win32POTSModemErrorControlOff_Type()
)
win32POTSModemErrorControlOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemErrorControlOff.setStatus("mandatory")
_Win32POTSModemErrorControlOn_Type = String
_Win32POTSModemErrorControlOn_Object = MibTableColumn
win32POTSModemErrorControlOn = _Win32POTSModemErrorControlOn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 16),
    _Win32POTSModemErrorControlOn_Type()
)
win32POTSModemErrorControlOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemErrorControlOn.setStatus("mandatory")
_Win32POTSModemFlowControlHard_Type = String
_Win32POTSModemFlowControlHard_Object = MibTableColumn
win32POTSModemFlowControlHard = _Win32POTSModemFlowControlHard_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 17),
    _Win32POTSModemFlowControlHard_Type()
)
win32POTSModemFlowControlHard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemFlowControlHard.setStatus("mandatory")
_Win32POTSModemFlowControlSoft_Type = String
_Win32POTSModemFlowControlSoft_Object = MibTableColumn
win32POTSModemFlowControlSoft = _Win32POTSModemFlowControlSoft_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 18),
    _Win32POTSModemFlowControlSoft_Type()
)
win32POTSModemFlowControlSoft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemFlowControlSoft.setStatus("mandatory")
_Win32POTSModemFlowControlOff_Type = String
_Win32POTSModemFlowControlOff_Object = MibTableColumn
win32POTSModemFlowControlOff = _Win32POTSModemFlowControlOff_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 19),
    _Win32POTSModemFlowControlOff_Type()
)
win32POTSModemFlowControlOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemFlowControlOff.setStatus("mandatory")
_Win32POTSModemInactivityScale_Type = String
_Win32POTSModemInactivityScale_Object = MibTableColumn
win32POTSModemInactivityScale = _Win32POTSModemInactivityScale_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 20),
    _Win32POTSModemInactivityScale_Type()
)
win32POTSModemInactivityScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemInactivityScale.setStatus("mandatory")
_Win32POTSModemIndex_Type = Uint32
_Win32POTSModemIndex_Object = MibTableColumn
win32POTSModemIndex = _Win32POTSModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 21),
    _Win32POTSModemIndex_Type()
)
win32POTSModemIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemIndex.setStatus("mandatory")
_Win32POTSModemModel_Type = String
_Win32POTSModemModel_Object = MibTableColumn
win32POTSModemModel = _Win32POTSModemModel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 22),
    _Win32POTSModemModel_Type()
)
win32POTSModemModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemModel.setStatus("mandatory")
_Win32POTSModemModemInfPath_Type = String
_Win32POTSModemModemInfPath_Object = MibTableColumn
win32POTSModemModemInfPath = _Win32POTSModemModemInfPath_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 23),
    _Win32POTSModemModemInfPath_Type()
)
win32POTSModemModemInfPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemModemInfPath.setStatus("mandatory")
_Win32POTSModemModemInfSection_Type = String
_Win32POTSModemModemInfSection_Object = MibTableColumn
win32POTSModemModemInfSection = _Win32POTSModemModemInfSection_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 24),
    _Win32POTSModemModemInfSection_Type()
)
win32POTSModemModemInfSection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemModemInfSection.setStatus("mandatory")
_Win32POTSModemModulationBell_Type = String
_Win32POTSModemModulationBell_Object = MibTableColumn
win32POTSModemModulationBell = _Win32POTSModemModulationBell_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 25),
    _Win32POTSModemModulationBell_Type()
)
win32POTSModemModulationBell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemModulationBell.setStatus("mandatory")
_Win32POTSModemModulationCCITT_Type = String
_Win32POTSModemModulationCCITT_Object = MibTableColumn
win32POTSModemModulationCCITT = _Win32POTSModemModulationCCITT_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 26),
    _Win32POTSModemModulationCCITT_Type()
)
win32POTSModemModulationCCITT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemModulationCCITT.setStatus("mandatory")
_Win32POTSModemPortSubClass_Type = String
_Win32POTSModemPortSubClass_Object = MibTableColumn
win32POTSModemPortSubClass = _Win32POTSModemPortSubClass_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 27),
    _Win32POTSModemPortSubClass_Type()
)
win32POTSModemPortSubClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemPortSubClass.setStatus("mandatory")
_Win32POTSModemPrefix_Type = String
_Win32POTSModemPrefix_Object = MibTableColumn
win32POTSModemPrefix = _Win32POTSModemPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 28),
    _Win32POTSModemPrefix_Type()
)
win32POTSModemPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemPrefix.setStatus("mandatory")
_Win32POTSModemProperties_Type = Uint8
_Win32POTSModemProperties_Object = MibTableColumn
win32POTSModemProperties = _Win32POTSModemProperties_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 29),
    _Win32POTSModemProperties_Type()
)
win32POTSModemProperties.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemProperties.setStatus("mandatory")
_Win32POTSModemProviderName_Type = String
_Win32POTSModemProviderName_Object = MibTableColumn
win32POTSModemProviderName = _Win32POTSModemProviderName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 30),
    _Win32POTSModemProviderName_Type()
)
win32POTSModemProviderName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemProviderName.setStatus("mandatory")
_Win32POTSModemPulse_Type = String
_Win32POTSModemPulse_Object = MibTableColumn
win32POTSModemPulse = _Win32POTSModemPulse_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 31),
    _Win32POTSModemPulse_Type()
)
win32POTSModemPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemPulse.setStatus("mandatory")
_Win32POTSModemReset_Type = String
_Win32POTSModemReset_Object = MibTableColumn
win32POTSModemReset = _Win32POTSModemReset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 32),
    _Win32POTSModemReset_Type()
)
win32POTSModemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemReset.setStatus("mandatory")
_Win32POTSModemResponsesKeyName_Type = String
_Win32POTSModemResponsesKeyName_Object = MibTableColumn
win32POTSModemResponsesKeyName = _Win32POTSModemResponsesKeyName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 33),
    _Win32POTSModemResponsesKeyName_Type()
)
win32POTSModemResponsesKeyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemResponsesKeyName.setStatus("mandatory")
_Win32POTSModemSpeakerModeDial_Type = String
_Win32POTSModemSpeakerModeDial_Object = MibTableColumn
win32POTSModemSpeakerModeDial = _Win32POTSModemSpeakerModeDial_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 34),
    _Win32POTSModemSpeakerModeDial_Type()
)
win32POTSModemSpeakerModeDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemSpeakerModeDial.setStatus("mandatory")
_Win32POTSModemSpeakerModeOff_Type = String
_Win32POTSModemSpeakerModeOff_Object = MibTableColumn
win32POTSModemSpeakerModeOff = _Win32POTSModemSpeakerModeOff_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 35),
    _Win32POTSModemSpeakerModeOff_Type()
)
win32POTSModemSpeakerModeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemSpeakerModeOff.setStatus("mandatory")
_Win32POTSModemSpeakerModeOn_Type = String
_Win32POTSModemSpeakerModeOn_Object = MibTableColumn
win32POTSModemSpeakerModeOn = _Win32POTSModemSpeakerModeOn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 36),
    _Win32POTSModemSpeakerModeOn_Type()
)
win32POTSModemSpeakerModeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemSpeakerModeOn.setStatus("mandatory")
_Win32POTSModemSpeakerModeSetup_Type = String
_Win32POTSModemSpeakerModeSetup_Object = MibTableColumn
win32POTSModemSpeakerModeSetup = _Win32POTSModemSpeakerModeSetup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 37),
    _Win32POTSModemSpeakerModeSetup_Type()
)
win32POTSModemSpeakerModeSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemSpeakerModeSetup.setStatus("mandatory")
_Win32POTSModemSpeakerVolumeHigh_Type = String
_Win32POTSModemSpeakerVolumeHigh_Object = MibTableColumn
win32POTSModemSpeakerVolumeHigh = _Win32POTSModemSpeakerVolumeHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 38),
    _Win32POTSModemSpeakerVolumeHigh_Type()
)
win32POTSModemSpeakerVolumeHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemSpeakerVolumeHigh.setStatus("mandatory")
_Win32POTSModemSpeakerVolumeLow_Type = String
_Win32POTSModemSpeakerVolumeLow_Object = MibTableColumn
win32POTSModemSpeakerVolumeLow = _Win32POTSModemSpeakerVolumeLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 39),
    _Win32POTSModemSpeakerVolumeLow_Type()
)
win32POTSModemSpeakerVolumeLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemSpeakerVolumeLow.setStatus("mandatory")
_Win32POTSModemSpeakerVolumeMed_Type = String
_Win32POTSModemSpeakerVolumeMed_Object = MibTableColumn
win32POTSModemSpeakerVolumeMed = _Win32POTSModemSpeakerVolumeMed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 40),
    _Win32POTSModemSpeakerVolumeMed_Type()
)
win32POTSModemSpeakerVolumeMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemSpeakerVolumeMed.setStatus("mandatory")
_Win32POTSModemStringFormat_Type = String
_Win32POTSModemStringFormat_Object = MibTableColumn
win32POTSModemStringFormat = _Win32POTSModemStringFormat_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 41),
    _Win32POTSModemStringFormat_Type()
)
win32POTSModemStringFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemStringFormat.setStatus("mandatory")
_Win32POTSModemTerminator_Type = String
_Win32POTSModemTerminator_Object = MibTableColumn
win32POTSModemTerminator = _Win32POTSModemTerminator_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 42),
    _Win32POTSModemTerminator_Type()
)
win32POTSModemTerminator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemTerminator.setStatus("mandatory")
_Win32POTSModemTone_Type = String
_Win32POTSModemTone_Object = MibTableColumn
win32POTSModemTone = _Win32POTSModemTone_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 43),
    _Win32POTSModemTone_Type()
)
win32POTSModemTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemTone.setStatus("mandatory")
_Win32POTSModemVoiceSwitchFeature_Type = String
_Win32POTSModemVoiceSwitchFeature_Object = MibTableColumn
win32POTSModemVoiceSwitchFeature = _Win32POTSModemVoiceSwitchFeature_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 44),
    _Win32POTSModemVoiceSwitchFeature_Type()
)
win32POTSModemVoiceSwitchFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemVoiceSwitchFeature.setStatus("mandatory")
_Win32POTSModemStatus_Type = String
_Win32POTSModemStatus_Object = MibTableColumn
win32POTSModemStatus = _Win32POTSModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 140, 1, 45),
    _Win32POTSModemStatus_Type()
)
win32POTSModemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32POTSModemStatus.setStatus("mandatory")
_Win32SerialPortTable_Object = MibTable
win32SerialPortTable = _Win32SerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150)
)
if mibBuilder.loadTexts:
    win32SerialPortTable.setStatus("mandatory")
_Win32SerialPortEntry_Object = MibTableRow
win32SerialPortEntry = _Win32SerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1)
)
win32SerialPortEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32SerialPortKeyIndex"),
)
if mibBuilder.loadTexts:
    win32SerialPortEntry.setStatus("mandatory")
_Win32SerialPortKeyIndex_Type = String
_Win32SerialPortKeyIndex_Object = MibTableColumn
win32SerialPortKeyIndex = _Win32SerialPortKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 1),
    _Win32SerialPortKeyIndex_Type()
)
win32SerialPortKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortKeyIndex.setStatus("mandatory")
_Win32SerialPortBinary_Type = Boolean
_Win32SerialPortBinary_Object = MibTableColumn
win32SerialPortBinary = _Win32SerialPortBinary_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 2),
    _Win32SerialPortBinary_Type()
)
win32SerialPortBinary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortBinary.setStatus("mandatory")
_Win32SerialPortMaximumInputBufferSize_Type = Uint32
_Win32SerialPortMaximumInputBufferSize_Object = MibTableColumn
win32SerialPortMaximumInputBufferSize = _Win32SerialPortMaximumInputBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 3),
    _Win32SerialPortMaximumInputBufferSize_Type()
)
win32SerialPortMaximumInputBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortMaximumInputBufferSize.setStatus("mandatory")
_Win32SerialPortMaximumOutputBufferSize_Type = Uint32
_Win32SerialPortMaximumOutputBufferSize_Object = MibTableColumn
win32SerialPortMaximumOutputBufferSize = _Win32SerialPortMaximumOutputBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 4),
    _Win32SerialPortMaximumOutputBufferSize_Type()
)
win32SerialPortMaximumOutputBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortMaximumOutputBufferSize.setStatus("mandatory")
_Win32SerialPortProviderType_Type = String
_Win32SerialPortProviderType_Object = MibTableColumn
win32SerialPortProviderType = _Win32SerialPortProviderType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 5),
    _Win32SerialPortProviderType_Type()
)
win32SerialPortProviderType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortProviderType.setStatus("mandatory")
_Win32SerialPortSettableBaudRate_Type = Boolean
_Win32SerialPortSettableBaudRate_Object = MibTableColumn
win32SerialPortSettableBaudRate = _Win32SerialPortSettableBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 6),
    _Win32SerialPortSettableBaudRate_Type()
)
win32SerialPortSettableBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSettableBaudRate.setStatus("mandatory")
_Win32SerialPortSettableDataBits_Type = Boolean
_Win32SerialPortSettableDataBits_Object = MibTableColumn
win32SerialPortSettableDataBits = _Win32SerialPortSettableDataBits_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 7),
    _Win32SerialPortSettableDataBits_Type()
)
win32SerialPortSettableDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSettableDataBits.setStatus("mandatory")
_Win32SerialPortSettableFlowControl_Type = Boolean
_Win32SerialPortSettableFlowControl_Object = MibTableColumn
win32SerialPortSettableFlowControl = _Win32SerialPortSettableFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 8),
    _Win32SerialPortSettableFlowControl_Type()
)
win32SerialPortSettableFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSettableFlowControl.setStatus("mandatory")
_Win32SerialPortSettableParity_Type = Boolean
_Win32SerialPortSettableParity_Object = MibTableColumn
win32SerialPortSettableParity = _Win32SerialPortSettableParity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 9),
    _Win32SerialPortSettableParity_Type()
)
win32SerialPortSettableParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSettableParity.setStatus("mandatory")
_Win32SerialPortSettableParityCheck_Type = Boolean
_Win32SerialPortSettableParityCheck_Object = MibTableColumn
win32SerialPortSettableParityCheck = _Win32SerialPortSettableParityCheck_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 10),
    _Win32SerialPortSettableParityCheck_Type()
)
win32SerialPortSettableParityCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSettableParityCheck.setStatus("mandatory")
_Win32SerialPortSettableRLSD_Type = Boolean
_Win32SerialPortSettableRLSD_Object = MibTableColumn
win32SerialPortSettableRLSD = _Win32SerialPortSettableRLSD_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 11),
    _Win32SerialPortSettableRLSD_Type()
)
win32SerialPortSettableRLSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSettableRLSD.setStatus("mandatory")
_Win32SerialPortSettableStopBits_Type = Boolean
_Win32SerialPortSettableStopBits_Object = MibTableColumn
win32SerialPortSettableStopBits = _Win32SerialPortSettableStopBits_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 12),
    _Win32SerialPortSettableStopBits_Type()
)
win32SerialPortSettableStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSettableStopBits.setStatus("mandatory")
_Win32SerialPortSupports16BitMode_Type = Boolean
_Win32SerialPortSupports16BitMode_Object = MibTableColumn
win32SerialPortSupports16BitMode = _Win32SerialPortSupports16BitMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 13),
    _Win32SerialPortSupports16BitMode_Type()
)
win32SerialPortSupports16BitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSupports16BitMode.setStatus("mandatory")
_Win32SerialPortSupportsDTRDSR_Type = Boolean
_Win32SerialPortSupportsDTRDSR_Object = MibTableColumn
win32SerialPortSupportsDTRDSR = _Win32SerialPortSupportsDTRDSR_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 14),
    _Win32SerialPortSupportsDTRDSR_Type()
)
win32SerialPortSupportsDTRDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSupportsDTRDSR.setStatus("mandatory")
_Win32SerialPortSupportsElapsedTimeouts_Type = Boolean
_Win32SerialPortSupportsElapsedTimeouts_Object = MibTableColumn
win32SerialPortSupportsElapsedTimeouts = _Win32SerialPortSupportsElapsedTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 15),
    _Win32SerialPortSupportsElapsedTimeouts_Type()
)
win32SerialPortSupportsElapsedTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSupportsElapsedTimeouts.setStatus("mandatory")
_Win32SerialPortSupportsIntTimeouts_Type = Boolean
_Win32SerialPortSupportsIntTimeouts_Object = MibTableColumn
win32SerialPortSupportsIntTimeouts = _Win32SerialPortSupportsIntTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 16),
    _Win32SerialPortSupportsIntTimeouts_Type()
)
win32SerialPortSupportsIntTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSupportsIntTimeouts.setStatus("mandatory")
_Win32SerialPortSupportsParityCheck_Type = Boolean
_Win32SerialPortSupportsParityCheck_Object = MibTableColumn
win32SerialPortSupportsParityCheck = _Win32SerialPortSupportsParityCheck_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 17),
    _Win32SerialPortSupportsParityCheck_Type()
)
win32SerialPortSupportsParityCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSupportsParityCheck.setStatus("mandatory")
_Win32SerialPortSupportsRLSD_Type = Boolean
_Win32SerialPortSupportsRLSD_Object = MibTableColumn
win32SerialPortSupportsRLSD = _Win32SerialPortSupportsRLSD_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 18),
    _Win32SerialPortSupportsRLSD_Type()
)
win32SerialPortSupportsRLSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSupportsRLSD.setStatus("mandatory")
_Win32SerialPortSupportsRTSCTS_Type = Boolean
_Win32SerialPortSupportsRTSCTS_Object = MibTableColumn
win32SerialPortSupportsRTSCTS = _Win32SerialPortSupportsRTSCTS_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 19),
    _Win32SerialPortSupportsRTSCTS_Type()
)
win32SerialPortSupportsRTSCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSupportsRTSCTS.setStatus("mandatory")
_Win32SerialPortSupportsSpecialCharacters_Type = Boolean
_Win32SerialPortSupportsSpecialCharacters_Object = MibTableColumn
win32SerialPortSupportsSpecialCharacters = _Win32SerialPortSupportsSpecialCharacters_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 20),
    _Win32SerialPortSupportsSpecialCharacters_Type()
)
win32SerialPortSupportsSpecialCharacters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSupportsSpecialCharacters.setStatus("mandatory")
_Win32SerialPortSupportsXOnXOff_Type = Boolean
_Win32SerialPortSupportsXOnXOff_Object = MibTableColumn
win32SerialPortSupportsXOnXOff = _Win32SerialPortSupportsXOnXOff_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 21),
    _Win32SerialPortSupportsXOnXOff_Type()
)
win32SerialPortSupportsXOnXOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSupportsXOnXOff.setStatus("mandatory")
_Win32SerialPortSupportsXOnXOffSet_Type = Boolean
_Win32SerialPortSupportsXOnXOffSet_Object = MibTableColumn
win32SerialPortSupportsXOnXOffSet = _Win32SerialPortSupportsXOnXOffSet_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 22),
    _Win32SerialPortSupportsXOnXOffSet_Type()
)
win32SerialPortSupportsXOnXOffSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortSupportsXOnXOffSet.setStatus("mandatory")
_Win32SerialPortStatus_Type = String
_Win32SerialPortStatus_Object = MibTableColumn
win32SerialPortStatus = _Win32SerialPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 150, 1, 23),
    _Win32SerialPortStatus_Type()
)
win32SerialPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortStatus.setStatus("mandatory")
_Win32NetworkAdapterTable_Object = MibTable
win32NetworkAdapterTable = _Win32NetworkAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 160)
)
if mibBuilder.loadTexts:
    win32NetworkAdapterTable.setStatus("mandatory")
_Win32NetworkAdapterEntry_Object = MibTableRow
win32NetworkAdapterEntry = _Win32NetworkAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 160, 1)
)
win32NetworkAdapterEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32NetworkAdapterKeyIndex"),
)
if mibBuilder.loadTexts:
    win32NetworkAdapterEntry.setStatus("mandatory")
_Win32NetworkAdapterKeyIndex_Type = String
_Win32NetworkAdapterKeyIndex_Object = MibTableColumn
win32NetworkAdapterKeyIndex = _Win32NetworkAdapterKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 160, 1, 1),
    _Win32NetworkAdapterKeyIndex_Type()
)
win32NetworkAdapterKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkAdapterKeyIndex.setStatus("mandatory")
_Win32NetworkAdapterProductName_Type = String
_Win32NetworkAdapterProductName_Object = MibTableColumn
win32NetworkAdapterProductName = _Win32NetworkAdapterProductName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 160, 1, 2),
    _Win32NetworkAdapterProductName_Type()
)
win32NetworkAdapterProductName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkAdapterProductName.setStatus("mandatory")
_Win32NetworkAdapterAdapterType_Type = String
_Win32NetworkAdapterAdapterType_Object = MibTableColumn
win32NetworkAdapterAdapterType = _Win32NetworkAdapterAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 160, 1, 3),
    _Win32NetworkAdapterAdapterType_Type()
)
win32NetworkAdapterAdapterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkAdapterAdapterType.setStatus("mandatory")
_Win32NetworkAdapterMACAddress_Type = String
_Win32NetworkAdapterMACAddress_Object = MibTableColumn
win32NetworkAdapterMACAddress = _Win32NetworkAdapterMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 160, 1, 4),
    _Win32NetworkAdapterMACAddress_Type()
)
win32NetworkAdapterMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkAdapterMACAddress.setStatus("mandatory")
_Win32NetworkAdapterServiceName_Type = String
_Win32NetworkAdapterServiceName_Object = MibTableColumn
win32NetworkAdapterServiceName = _Win32NetworkAdapterServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 160, 1, 5),
    _Win32NetworkAdapterServiceName_Type()
)
win32NetworkAdapterServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkAdapterServiceName.setStatus("mandatory")
_Win32NetworkAdapterManufacturer_Type = String
_Win32NetworkAdapterManufacturer_Object = MibTableColumn
win32NetworkAdapterManufacturer = _Win32NetworkAdapterManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 160, 1, 6),
    _Win32NetworkAdapterManufacturer_Type()
)
win32NetworkAdapterManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkAdapterManufacturer.setStatus("mandatory")
_Win32NetworkAdapterInstalled_Type = Boolean
_Win32NetworkAdapterInstalled_Object = MibTableColumn
win32NetworkAdapterInstalled = _Win32NetworkAdapterInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 160, 1, 7),
    _Win32NetworkAdapterInstalled_Type()
)
win32NetworkAdapterInstalled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkAdapterInstalled.setStatus("mandatory")
_Win32NetworkAdapterIndex_Type = Uint32
_Win32NetworkAdapterIndex_Object = MibTableColumn
win32NetworkAdapterIndex = _Win32NetworkAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 160, 1, 8),
    _Win32NetworkAdapterIndex_Type()
)
win32NetworkAdapterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkAdapterIndex.setStatus("mandatory")
_Win32NetworkAdapterMaxNumberControlled_Type = Uint32
_Win32NetworkAdapterMaxNumberControlled_Object = MibTableColumn
win32NetworkAdapterMaxNumberControlled = _Win32NetworkAdapterMaxNumberControlled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 160, 1, 9),
    _Win32NetworkAdapterMaxNumberControlled_Type()
)
win32NetworkAdapterMaxNumberControlled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkAdapterMaxNumberControlled.setStatus("mandatory")
_Win32NetworkAdapterTimeOfLastReset_Type = Datetime
_Win32NetworkAdapterTimeOfLastReset_Object = MibTableColumn
win32NetworkAdapterTimeOfLastReset = _Win32NetworkAdapterTimeOfLastReset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 160, 1, 10),
    _Win32NetworkAdapterTimeOfLastReset_Type()
)
win32NetworkAdapterTimeOfLastReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkAdapterTimeOfLastReset.setStatus("mandatory")
_Win32NetworkAdapterStatus_Type = String
_Win32NetworkAdapterStatus_Object = MibTableColumn
win32NetworkAdapterStatus = _Win32NetworkAdapterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 160, 1, 11),
    _Win32NetworkAdapterStatus_Type()
)
win32NetworkAdapterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkAdapterStatus.setStatus("mandatory")
_Win32SCSIControllerTable_Object = MibTable
win32SCSIControllerTable = _Win32SCSIControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 170)
)
if mibBuilder.loadTexts:
    win32SCSIControllerTable.setStatus("mandatory")
_Win32SCSIControllerEntry_Object = MibTableRow
win32SCSIControllerEntry = _Win32SCSIControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 170, 1)
)
win32SCSIControllerEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32SCSIControllerKeyIndex"),
)
if mibBuilder.loadTexts:
    win32SCSIControllerEntry.setStatus("mandatory")
_Win32SCSIControllerKeyIndex_Type = String
_Win32SCSIControllerKeyIndex_Object = MibTableColumn
win32SCSIControllerKeyIndex = _Win32SCSIControllerKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 170, 1, 1),
    _Win32SCSIControllerKeyIndex_Type()
)
win32SCSIControllerKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SCSIControllerKeyIndex.setStatus("mandatory")
_Win32SCSIControllerIndex_Type = Uint32
_Win32SCSIControllerIndex_Object = MibTableColumn
win32SCSIControllerIndex = _Win32SCSIControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 170, 1, 2),
    _Win32SCSIControllerIndex_Type()
)
win32SCSIControllerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SCSIControllerIndex.setStatus("mandatory")
_Win32SCSIControllerDriverName_Type = String
_Win32SCSIControllerDriverName_Object = MibTableColumn
win32SCSIControllerDriverName = _Win32SCSIControllerDriverName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 170, 1, 3),
    _Win32SCSIControllerDriverName_Type()
)
win32SCSIControllerDriverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SCSIControllerDriverName.setStatus("mandatory")
_Win32SCSIControllerDeviceMap_Type = String
_Win32SCSIControllerDeviceMap_Object = MibTableColumn
win32SCSIControllerDeviceMap = _Win32SCSIControllerDeviceMap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 170, 1, 4),
    _Win32SCSIControllerDeviceMap_Type()
)
win32SCSIControllerDeviceMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SCSIControllerDeviceMap.setStatus("mandatory")
_Win32SCSIControllerHardwareVersion_Type = String
_Win32SCSIControllerHardwareVersion_Object = MibTableColumn
win32SCSIControllerHardwareVersion = _Win32SCSIControllerHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 170, 1, 5),
    _Win32SCSIControllerHardwareVersion_Type()
)
win32SCSIControllerHardwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SCSIControllerHardwareVersion.setStatus("mandatory")
_Win32SCSIControllerManufacturer_Type = String
_Win32SCSIControllerManufacturer_Object = MibTableColumn
win32SCSIControllerManufacturer = _Win32SCSIControllerManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 170, 1, 6),
    _Win32SCSIControllerManufacturer_Type()
)
win32SCSIControllerManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SCSIControllerManufacturer.setStatus("mandatory")
_Win32SCSIControllerStatus_Type = String
_Win32SCSIControllerStatus_Object = MibTableColumn
win32SCSIControllerStatus = _Win32SCSIControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 170, 1, 7),
    _Win32SCSIControllerStatus_Type()
)
win32SCSIControllerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SCSIControllerStatus.setStatus("mandatory")
_Win32CodecFileTable_Object = MibTable
win32CodecFileTable = _Win32CodecFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 190)
)
if mibBuilder.loadTexts:
    win32CodecFileTable.setStatus("mandatory")
_Win32CodecFileEntry_Object = MibTableRow
win32CodecFileEntry = _Win32CodecFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 190, 1)
)
win32CodecFileEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32CodecFileKeyIndex"),
)
if mibBuilder.loadTexts:
    win32CodecFileEntry.setStatus("mandatory")
_Win32CodecFileKeyIndex_Type = String
_Win32CodecFileKeyIndex_Object = MibTableColumn
win32CodecFileKeyIndex = _Win32CodecFileKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 190, 1, 1),
    _Win32CodecFileKeyIndex_Type()
)
win32CodecFileKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CodecFileKeyIndex.setStatus("mandatory")
_Win32CodecFileGroup_Type = String
_Win32CodecFileGroup_Object = MibTableColumn
win32CodecFileGroup = _Win32CodecFileGroup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 190, 1, 2),
    _Win32CodecFileGroup_Type()
)
win32CodecFileGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CodecFileGroup.setStatus("mandatory")
_Win32CodecFileDescription_Type = String
_Win32CodecFileDescription_Object = MibTableColumn
win32CodecFileDescription = _Win32CodecFileDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 190, 1, 3),
    _Win32CodecFileDescription_Type()
)
win32CodecFileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CodecFileDescription.setStatus("mandatory")
_Win32CodecFileStatus_Type = String
_Win32CodecFileStatus_Object = MibTableColumn
win32CodecFileStatus = _Win32CodecFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 190, 1, 4),
    _Win32CodecFileStatus_Type()
)
win32CodecFileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CodecFileStatus.setStatus("mandatory")
_Win32PageFileTable_Object = MibTable
win32PageFileTable = _Win32PageFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 210)
)
if mibBuilder.loadTexts:
    win32PageFileTable.setStatus("mandatory")
_Win32PageFileEntry_Object = MibTableRow
win32PageFileEntry = _Win32PageFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 210, 1)
)
win32PageFileEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32PageFileKeyIndex"),
)
if mibBuilder.loadTexts:
    win32PageFileEntry.setStatus("mandatory")
_Win32PageFileKeyIndex_Type = String
_Win32PageFileKeyIndex_Object = MibTableColumn
win32PageFileKeyIndex = _Win32PageFileKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 210, 1, 1),
    _Win32PageFileKeyIndex_Type()
)
win32PageFileKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PageFileKeyIndex.setStatus("mandatory")
_Win32PageFileName_Type = String
_Win32PageFileName_Object = MibTableColumn
win32PageFileName = _Win32PageFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 210, 1, 2),
    _Win32PageFileName_Type()
)
win32PageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PageFileName.setStatus("mandatory")
_Win32PageFileFreeSpace_Type = Uint32
_Win32PageFileFreeSpace_Object = MibTableColumn
win32PageFileFreeSpace = _Win32PageFileFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 210, 1, 3),
    _Win32PageFileFreeSpace_Type()
)
win32PageFileFreeSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PageFileFreeSpace.setStatus("mandatory")
_Win32PageFileInitialSize_Type = Uint32
_Win32PageFileInitialSize_Object = MibTableColumn
win32PageFileInitialSize = _Win32PageFileInitialSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 210, 1, 4),
    _Win32PageFileInitialSize_Type()
)
win32PageFileInitialSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PageFileInitialSize.setStatus("mandatory")
_Win32PageFileMaximumSize_Type = Uint32
_Win32PageFileMaximumSize_Object = MibTableColumn
win32PageFileMaximumSize = _Win32PageFileMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 210, 1, 5),
    _Win32PageFileMaximumSize_Type()
)
win32PageFileMaximumSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PageFileMaximumSize.setStatus("mandatory")
_Win32PageFileStatus_Type = String
_Win32PageFileStatus_Object = MibTableColumn
win32PageFileStatus = _Win32PageFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 210, 1, 6),
    _Win32PageFileStatus_Type()
)
win32PageFileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PageFileStatus.setStatus("mandatory")
_Win32DriverVXDTable_Object = MibTable
win32DriverVXDTable = _Win32DriverVXDTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 230)
)
if mibBuilder.loadTexts:
    win32DriverVXDTable.setStatus("mandatory")
_Win32DriverVXDEntry_Object = MibTableRow
win32DriverVXDEntry = _Win32DriverVXDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 230, 1)
)
win32DriverVXDEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32DriverVXDKeyIndex"),
)
if mibBuilder.loadTexts:
    win32DriverVXDEntry.setStatus("mandatory")
_Win32DriverVXDKeyIndex_Type = String
_Win32DriverVXDKeyIndex_Object = MibTableColumn
win32DriverVXDKeyIndex = _Win32DriverVXDKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 230, 1, 1),
    _Win32DriverVXDKeyIndex_Type()
)
win32DriverVXDKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DriverVXDKeyIndex.setStatus("mandatory")
_Win32DriverVXDControl_Type = String
_Win32DriverVXDControl_Object = MibTableColumn
win32DriverVXDControl = _Win32DriverVXDControl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 230, 1, 2),
    _Win32DriverVXDControl_Type()
)
win32DriverVXDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DriverVXDControl.setStatus("mandatory")
_Win32DriverVXDDeviceDescriptorBlock_Type = String
_Win32DriverVXDDeviceDescriptorBlock_Object = MibTableColumn
win32DriverVXDDeviceDescriptorBlock = _Win32DriverVXDDeviceDescriptorBlock_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 230, 1, 3),
    _Win32DriverVXDDeviceDescriptorBlock_Type()
)
win32DriverVXDDeviceDescriptorBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DriverVXDDeviceDescriptorBlock.setStatus("mandatory")
_Win32DriverVXDPMAPI_Type = String
_Win32DriverVXDPMAPI_Object = MibTableColumn
win32DriverVXDPMAPI = _Win32DriverVXDPMAPI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 230, 1, 4),
    _Win32DriverVXDPMAPI_Type()
)
win32DriverVXDPMAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DriverVXDPMAPI.setStatus("mandatory")
_Win32DriverVXDServiceTableSize_Type = Uint32
_Win32DriverVXDServiceTableSize_Object = MibTableColumn
win32DriverVXDServiceTableSize = _Win32DriverVXDServiceTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 230, 1, 5),
    _Win32DriverVXDServiceTableSize_Type()
)
win32DriverVXDServiceTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DriverVXDServiceTableSize.setStatus("mandatory")
_Win32DriverVXDV86API_Type = String
_Win32DriverVXDV86API_Object = MibTableColumn
win32DriverVXDV86API = _Win32DriverVXDV86API_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 230, 1, 6),
    _Win32DriverVXDV86API_Type()
)
win32DriverVXDV86API.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DriverVXDV86API.setStatus("mandatory")
_Win32DriverVXDVersion_Type = String
_Win32DriverVXDVersion_Object = MibTableColumn
win32DriverVXDVersion = _Win32DriverVXDVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 230, 1, 7),
    _Win32DriverVXDVersion_Type()
)
win32DriverVXDVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DriverVXDVersion.setStatus("mandatory")
_Win32DriverVXDStatus_Type = String
_Win32DriverVXDStatus_Object = MibTableColumn
win32DriverVXDStatus = _Win32DriverVXDStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 230, 1, 8),
    _Win32DriverVXDStatus_Type()
)
win32DriverVXDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DriverVXDStatus.setStatus("mandatory")
_Win32AccountTable_Object = MibTable
win32AccountTable = _Win32AccountTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 240)
)
if mibBuilder.loadTexts:
    win32AccountTable.setStatus("mandatory")
_Win32AccountEntry_Object = MibTableRow
win32AccountEntry = _Win32AccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 240, 1)
)
win32AccountEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32AccountKeyIndex"),
)
if mibBuilder.loadTexts:
    win32AccountEntry.setStatus("mandatory")
_Win32AccountKeyIndex_Type = String
_Win32AccountKeyIndex_Object = MibTableColumn
win32AccountKeyIndex = _Win32AccountKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 240, 1, 1),
    _Win32AccountKeyIndex_Type()
)
win32AccountKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32AccountKeyIndex.setStatus("mandatory")
_Win32AccountDomain_Type = String
_Win32AccountDomain_Object = MibTableColumn
win32AccountDomain = _Win32AccountDomain_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 240, 1, 2),
    _Win32AccountDomain_Type()
)
win32AccountDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32AccountDomain.setStatus("mandatory")
_Win32AccountSID_Type = String
_Win32AccountSID_Object = MibTableColumn
win32AccountSID = _Win32AccountSID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 240, 1, 3),
    _Win32AccountSID_Type()
)
win32AccountSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32AccountSID.setStatus("mandatory")
_Win32AccountSIDType_Type = Uint8
_Win32AccountSIDType_Object = MibTableColumn
win32AccountSIDType = _Win32AccountSIDType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 240, 1, 4),
    _Win32AccountSIDType_Type()
)
win32AccountSIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32AccountSIDType.setStatus("mandatory")
_Win32AccountStatus_Type = String
_Win32AccountStatus_Object = MibTableColumn
win32AccountStatus = _Win32AccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 240, 1, 5),
    _Win32AccountStatus_Type()
)
win32AccountStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32AccountStatus.setStatus("mandatory")
_Win32SystemAccountTable_Object = MibTable
win32SystemAccountTable = _Win32SystemAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 250)
)
if mibBuilder.loadTexts:
    win32SystemAccountTable.setStatus("mandatory")
_Win32SystemAccountEntry_Object = MibTableRow
win32SystemAccountEntry = _Win32SystemAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 250, 1)
)
win32SystemAccountEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32SystemAccountKeyIndex"),
)
if mibBuilder.loadTexts:
    win32SystemAccountEntry.setStatus("mandatory")
_Win32SystemAccountKeyIndex_Type = String
_Win32SystemAccountKeyIndex_Object = MibTableColumn
win32SystemAccountKeyIndex = _Win32SystemAccountKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 250, 1, 1),
    _Win32SystemAccountKeyIndex_Type()
)
win32SystemAccountKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SystemAccountKeyIndex.setStatus("mandatory")
_Win32SystemAccountDomain_Type = String
_Win32SystemAccountDomain_Object = MibTableColumn
win32SystemAccountDomain = _Win32SystemAccountDomain_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 250, 1, 2),
    _Win32SystemAccountDomain_Type()
)
win32SystemAccountDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SystemAccountDomain.setStatus("mandatory")
_Win32SystemAccountName_Type = String
_Win32SystemAccountName_Object = MibTableColumn
win32SystemAccountName = _Win32SystemAccountName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 250, 1, 3),
    _Win32SystemAccountName_Type()
)
win32SystemAccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SystemAccountName.setStatus("mandatory")
_Win32SystemAccountStatus_Type = String
_Win32SystemAccountStatus_Object = MibTableColumn
win32SystemAccountStatus = _Win32SystemAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 250, 1, 4),
    _Win32SystemAccountStatus_Type()
)
win32SystemAccountStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SystemAccountStatus.setStatus("mandatory")
_Win32GroupTable_Object = MibTable
win32GroupTable = _Win32GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 260)
)
if mibBuilder.loadTexts:
    win32GroupTable.setStatus("mandatory")
_Win32GroupEntry_Object = MibTableRow
win32GroupEntry = _Win32GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 260, 1)
)
win32GroupEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32GroupKeyIndex"),
)
if mibBuilder.loadTexts:
    win32GroupEntry.setStatus("mandatory")
_Win32GroupKeyIndex_Type = String
_Win32GroupKeyIndex_Object = MibTableColumn
win32GroupKeyIndex = _Win32GroupKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 260, 1, 1),
    _Win32GroupKeyIndex_Type()
)
win32GroupKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32GroupKeyIndex.setStatus("mandatory")
_Win32GroupDomain_Type = String
_Win32GroupDomain_Object = MibTableColumn
win32GroupDomain = _Win32GroupDomain_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 260, 1, 2),
    _Win32GroupDomain_Type()
)
win32GroupDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32GroupDomain.setStatus("mandatory")
_Win32GroupName_Type = String
_Win32GroupName_Object = MibTableColumn
win32GroupName = _Win32GroupName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 260, 1, 3),
    _Win32GroupName_Type()
)
win32GroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32GroupName.setStatus("mandatory")
_Win32GroupStatus_Type = String
_Win32GroupStatus_Object = MibTableColumn
win32GroupStatus = _Win32GroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 260, 1, 4),
    _Win32GroupStatus_Type()
)
win32GroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32GroupStatus.setStatus("mandatory")
_Win32UserAccountTable_Object = MibTable
win32UserAccountTable = _Win32UserAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 270)
)
if mibBuilder.loadTexts:
    win32UserAccountTable.setStatus("mandatory")
_Win32UserAccountEntry_Object = MibTableRow
win32UserAccountEntry = _Win32UserAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 270, 1)
)
win32UserAccountEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32UserAccountKeyIndex"),
)
if mibBuilder.loadTexts:
    win32UserAccountEntry.setStatus("mandatory")
_Win32UserAccountKeyIndex_Type = String
_Win32UserAccountKeyIndex_Object = MibTableColumn
win32UserAccountKeyIndex = _Win32UserAccountKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 270, 1, 1),
    _Win32UserAccountKeyIndex_Type()
)
win32UserAccountKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UserAccountKeyIndex.setStatus("mandatory")
_Win32UserAccountAccountType_Type = Uint32
_Win32UserAccountAccountType_Object = MibTableColumn
win32UserAccountAccountType = _Win32UserAccountAccountType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 270, 1, 2),
    _Win32UserAccountAccountType_Type()
)
win32UserAccountAccountType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UserAccountAccountType.setStatus("mandatory")
_Win32UserAccountDisabled_Type = Boolean
_Win32UserAccountDisabled_Object = MibTableColumn
win32UserAccountDisabled = _Win32UserAccountDisabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 270, 1, 3),
    _Win32UserAccountDisabled_Type()
)
win32UserAccountDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UserAccountDisabled.setStatus("mandatory")
_Win32UserAccountDomain_Type = String
_Win32UserAccountDomain_Object = MibTableColumn
win32UserAccountDomain = _Win32UserAccountDomain_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 270, 1, 4),
    _Win32UserAccountDomain_Type()
)
win32UserAccountDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UserAccountDomain.setStatus("mandatory")
_Win32UserAccountFullName_Type = String
_Win32UserAccountFullName_Object = MibTableColumn
win32UserAccountFullName = _Win32UserAccountFullName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 270, 1, 5),
    _Win32UserAccountFullName_Type()
)
win32UserAccountFullName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UserAccountFullName.setStatus("mandatory")
_Win32UserAccountLockout_Type = Boolean
_Win32UserAccountLockout_Object = MibTableColumn
win32UserAccountLockout = _Win32UserAccountLockout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 270, 1, 6),
    _Win32UserAccountLockout_Type()
)
win32UserAccountLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UserAccountLockout.setStatus("mandatory")
_Win32UserAccountName_Type = String
_Win32UserAccountName_Object = MibTableColumn
win32UserAccountName = _Win32UserAccountName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 270, 1, 7),
    _Win32UserAccountName_Type()
)
win32UserAccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UserAccountName.setStatus("mandatory")
_Win32UserAccountPasswordChangeable_Type = Boolean
_Win32UserAccountPasswordChangeable_Object = MibTableColumn
win32UserAccountPasswordChangeable = _Win32UserAccountPasswordChangeable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 270, 1, 8),
    _Win32UserAccountPasswordChangeable_Type()
)
win32UserAccountPasswordChangeable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UserAccountPasswordChangeable.setStatus("mandatory")
_Win32UserAccountPasswordExpires_Type = Boolean
_Win32UserAccountPasswordExpires_Object = MibTableColumn
win32UserAccountPasswordExpires = _Win32UserAccountPasswordExpires_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 270, 1, 9),
    _Win32UserAccountPasswordExpires_Type()
)
win32UserAccountPasswordExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UserAccountPasswordExpires.setStatus("mandatory")
_Win32UserAccountPasswordRequired_Type = Boolean
_Win32UserAccountPasswordRequired_Object = MibTableColumn
win32UserAccountPasswordRequired = _Win32UserAccountPasswordRequired_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 270, 1, 10),
    _Win32UserAccountPasswordRequired_Type()
)
win32UserAccountPasswordRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UserAccountPasswordRequired.setStatus("mandatory")
_Win32UserAccountStatus_Type = String
_Win32UserAccountStatus_Object = MibTableColumn
win32UserAccountStatus = _Win32UserAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 270, 1, 11),
    _Win32UserAccountStatus_Type()
)
win32UserAccountStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32UserAccountStatus.setStatus("mandatory")
_Win32NetworkConnectionTable_Object = MibTable
win32NetworkConnectionTable = _Win32NetworkConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280)
)
if mibBuilder.loadTexts:
    win32NetworkConnectionTable.setStatus("mandatory")
_Win32NetworkConnectionEntry_Object = MibTableRow
win32NetworkConnectionEntry = _Win32NetworkConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280, 1)
)
win32NetworkConnectionEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32NetworkConnectionKeyIndex"),
)
if mibBuilder.loadTexts:
    win32NetworkConnectionEntry.setStatus("mandatory")
_Win32NetworkConnectionKeyIndex_Type = String
_Win32NetworkConnectionKeyIndex_Object = MibTableColumn
win32NetworkConnectionKeyIndex = _Win32NetworkConnectionKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280, 1, 1),
    _Win32NetworkConnectionKeyIndex_Type()
)
win32NetworkConnectionKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkConnectionKeyIndex.setStatus("mandatory")
_Win32NetworkConnectionComment_Type = String
_Win32NetworkConnectionComment_Object = MibTableColumn
win32NetworkConnectionComment = _Win32NetworkConnectionComment_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280, 1, 2),
    _Win32NetworkConnectionComment_Type()
)
win32NetworkConnectionComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkConnectionComment.setStatus("mandatory")
_Win32NetworkConnectionConnectionType_Type = String
_Win32NetworkConnectionConnectionType_Object = MibTableColumn
win32NetworkConnectionConnectionType = _Win32NetworkConnectionConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280, 1, 3),
    _Win32NetworkConnectionConnectionType_Type()
)
win32NetworkConnectionConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkConnectionConnectionType.setStatus("mandatory")
_Win32NetworkConnectionDisplayType_Type = String
_Win32NetworkConnectionDisplayType_Object = MibTableColumn
win32NetworkConnectionDisplayType = _Win32NetworkConnectionDisplayType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280, 1, 4),
    _Win32NetworkConnectionDisplayType_Type()
)
win32NetworkConnectionDisplayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkConnectionDisplayType.setStatus("mandatory")
_Win32NetworkConnectionLocalName_Type = String
_Win32NetworkConnectionLocalName_Object = MibTableColumn
win32NetworkConnectionLocalName = _Win32NetworkConnectionLocalName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280, 1, 5),
    _Win32NetworkConnectionLocalName_Type()
)
win32NetworkConnectionLocalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkConnectionLocalName.setStatus("mandatory")
_Win32NetworkConnectionName_Type = String
_Win32NetworkConnectionName_Object = MibTableColumn
win32NetworkConnectionName = _Win32NetworkConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280, 1, 6),
    _Win32NetworkConnectionName_Type()
)
win32NetworkConnectionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkConnectionName.setStatus("mandatory")
_Win32NetworkConnectionPersistent_Type = Boolean
_Win32NetworkConnectionPersistent_Object = MibTableColumn
win32NetworkConnectionPersistent = _Win32NetworkConnectionPersistent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280, 1, 7),
    _Win32NetworkConnectionPersistent_Type()
)
win32NetworkConnectionPersistent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkConnectionPersistent.setStatus("mandatory")
_Win32NetworkConnectionProviderName_Type = String
_Win32NetworkConnectionProviderName_Object = MibTableColumn
win32NetworkConnectionProviderName = _Win32NetworkConnectionProviderName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280, 1, 8),
    _Win32NetworkConnectionProviderName_Type()
)
win32NetworkConnectionProviderName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkConnectionProviderName.setStatus("mandatory")
_Win32NetworkConnectionRemoteName_Type = String
_Win32NetworkConnectionRemoteName_Object = MibTableColumn
win32NetworkConnectionRemoteName = _Win32NetworkConnectionRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280, 1, 9),
    _Win32NetworkConnectionRemoteName_Type()
)
win32NetworkConnectionRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkConnectionRemoteName.setStatus("mandatory")
_Win32NetworkConnectionRemotePath_Type = String
_Win32NetworkConnectionRemotePath_Object = MibTableColumn
win32NetworkConnectionRemotePath = _Win32NetworkConnectionRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280, 1, 10),
    _Win32NetworkConnectionRemotePath_Type()
)
win32NetworkConnectionRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkConnectionRemotePath.setStatus("mandatory")
_Win32NetworkConnectionResourceType_Type = String
_Win32NetworkConnectionResourceType_Object = MibTableColumn
win32NetworkConnectionResourceType = _Win32NetworkConnectionResourceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280, 1, 11),
    _Win32NetworkConnectionResourceType_Type()
)
win32NetworkConnectionResourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkConnectionResourceType.setStatus("mandatory")
_Win32NetworkConnectionUserName_Type = String
_Win32NetworkConnectionUserName_Object = MibTableColumn
win32NetworkConnectionUserName = _Win32NetworkConnectionUserName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280, 1, 12),
    _Win32NetworkConnectionUserName_Type()
)
win32NetworkConnectionUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkConnectionUserName.setStatus("mandatory")
_Win32NetworkConnectionStatus_Type = String
_Win32NetworkConnectionStatus_Object = MibTableColumn
win32NetworkConnectionStatus = _Win32NetworkConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 280, 1, 13),
    _Win32NetworkConnectionStatus_Type()
)
win32NetworkConnectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkConnectionStatus.setStatus("mandatory")
_Win32DeviceMemoryAddressTable_Object = MibTable
win32DeviceMemoryAddressTable = _Win32DeviceMemoryAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 290)
)
if mibBuilder.loadTexts:
    win32DeviceMemoryAddressTable.setStatus("mandatory")
_Win32DeviceMemoryAddressEntry_Object = MibTableRow
win32DeviceMemoryAddressEntry = _Win32DeviceMemoryAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 290, 1)
)
win32DeviceMemoryAddressEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32DeviceMemoryAddressKeyIndex"),
)
if mibBuilder.loadTexts:
    win32DeviceMemoryAddressEntry.setStatus("mandatory")
_Win32DeviceMemoryAddressKeyIndex_Type = String
_Win32DeviceMemoryAddressKeyIndex_Object = MibTableColumn
win32DeviceMemoryAddressKeyIndex = _Win32DeviceMemoryAddressKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 290, 1, 1),
    _Win32DeviceMemoryAddressKeyIndex_Type()
)
win32DeviceMemoryAddressKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DeviceMemoryAddressKeyIndex.setStatus("mandatory")
_Win32DeviceMemoryAddressMemoryType_Type = String
_Win32DeviceMemoryAddressMemoryType_Object = MibTableColumn
win32DeviceMemoryAddressMemoryType = _Win32DeviceMemoryAddressMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 290, 1, 2),
    _Win32DeviceMemoryAddressMemoryType_Type()
)
win32DeviceMemoryAddressMemoryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DeviceMemoryAddressMemoryType.setStatus("mandatory")
_Win32DeviceMemoryAddressStatus_Type = String
_Win32DeviceMemoryAddressStatus_Object = MibTableColumn
win32DeviceMemoryAddressStatus = _Win32DeviceMemoryAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 290, 1, 3),
    _Win32DeviceMemoryAddressStatus_Type()
)
win32DeviceMemoryAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DeviceMemoryAddressStatus.setStatus("mandatory")
_Win32PortResourceTable_Object = MibTable
win32PortResourceTable = _Win32PortResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 300)
)
if mibBuilder.loadTexts:
    win32PortResourceTable.setStatus("mandatory")
_Win32PortResourceEntry_Object = MibTableRow
win32PortResourceEntry = _Win32PortResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 300, 1)
)
win32PortResourceEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32PortResourceKeyIndex"),
)
if mibBuilder.loadTexts:
    win32PortResourceEntry.setStatus("mandatory")
_Win32PortResourceKeyIndex_Type = String
_Win32PortResourceKeyIndex_Object = MibTableColumn
win32PortResourceKeyIndex = _Win32PortResourceKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 300, 1, 1),
    _Win32PortResourceKeyIndex_Type()
)
win32PortResourceKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PortResourceKeyIndex.setStatus("mandatory")
_Win32PortResourceAlias_Type = Boolean
_Win32PortResourceAlias_Object = MibTableColumn
win32PortResourceAlias = _Win32PortResourceAlias_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 300, 1, 2),
    _Win32PortResourceAlias_Type()
)
win32PortResourceAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PortResourceAlias.setStatus("mandatory")
_Win32PortResourceStatus_Type = String
_Win32PortResourceStatus_Object = MibTableColumn
win32PortResourceStatus = _Win32PortResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 300, 1, 3),
    _Win32PortResourceStatus_Type()
)
win32PortResourceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PortResourceStatus.setStatus("mandatory")
_Win32DMAChannelTable_Object = MibTable
win32DMAChannelTable = _Win32DMAChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 310)
)
if mibBuilder.loadTexts:
    win32DMAChannelTable.setStatus("mandatory")
_Win32DMAChannelEntry_Object = MibTableRow
win32DMAChannelEntry = _Win32DMAChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 310, 1)
)
win32DMAChannelEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32DMAChannelKeyIndex"),
)
if mibBuilder.loadTexts:
    win32DMAChannelEntry.setStatus("mandatory")
_Win32DMAChannelKeyIndex_Type = String
_Win32DMAChannelKeyIndex_Object = MibTableColumn
win32DMAChannelKeyIndex = _Win32DMAChannelKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 310, 1, 1),
    _Win32DMAChannelKeyIndex_Type()
)
win32DMAChannelKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DMAChannelKeyIndex.setStatus("mandatory")
_Win32DMAChannelPort_Type = Uint32
_Win32DMAChannelPort_Object = MibTableColumn
win32DMAChannelPort = _Win32DMAChannelPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 310, 1, 2),
    _Win32DMAChannelPort_Type()
)
win32DMAChannelPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DMAChannelPort.setStatus("mandatory")
_Win32DMAChannelStatus_Type = String
_Win32DMAChannelStatus_Object = MibTableColumn
win32DMAChannelStatus = _Win32DMAChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 310, 1, 3),
    _Win32DMAChannelStatus_Type()
)
win32DMAChannelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DMAChannelStatus.setStatus("mandatory")
_Win32EnvironmentTable_Object = MibTable
win32EnvironmentTable = _Win32EnvironmentTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 320)
)
if mibBuilder.loadTexts:
    win32EnvironmentTable.setStatus("mandatory")
_Win32EnvironmentEntry_Object = MibTableRow
win32EnvironmentEntry = _Win32EnvironmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 320, 1)
)
win32EnvironmentEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32EnvironmentKeyIndex"),
)
if mibBuilder.loadTexts:
    win32EnvironmentEntry.setStatus("mandatory")
_Win32EnvironmentKeyIndex_Type = String
_Win32EnvironmentKeyIndex_Object = MibTableColumn
win32EnvironmentKeyIndex = _Win32EnvironmentKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 320, 1, 1),
    _Win32EnvironmentKeyIndex_Type()
)
win32EnvironmentKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32EnvironmentKeyIndex.setStatus("mandatory")
_Win32EnvironmentName_Type = String
_Win32EnvironmentName_Object = MibTableColumn
win32EnvironmentName = _Win32EnvironmentName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 320, 1, 2),
    _Win32EnvironmentName_Type()
)
win32EnvironmentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32EnvironmentName.setStatus("mandatory")
_Win32EnvironmentSystemVariable_Type = Boolean
_Win32EnvironmentSystemVariable_Object = MibTableColumn
win32EnvironmentSystemVariable = _Win32EnvironmentSystemVariable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 320, 1, 3),
    _Win32EnvironmentSystemVariable_Type()
)
win32EnvironmentSystemVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32EnvironmentSystemVariable.setStatus("mandatory")
_Win32EnvironmentUserName_Type = String
_Win32EnvironmentUserName_Object = MibTableColumn
win32EnvironmentUserName = _Win32EnvironmentUserName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 320, 1, 4),
    _Win32EnvironmentUserName_Type()
)
win32EnvironmentUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32EnvironmentUserName.setStatus("mandatory")
_Win32EnvironmentVariableValue_Type = String
_Win32EnvironmentVariableValue_Object = MibTableColumn
win32EnvironmentVariableValue = _Win32EnvironmentVariableValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 320, 1, 5),
    _Win32EnvironmentVariableValue_Type()
)
win32EnvironmentVariableValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32EnvironmentVariableValue.setStatus("mandatory")
_Win32EnvironmentStatus_Type = String
_Win32EnvironmentStatus_Object = MibTableColumn
win32EnvironmentStatus = _Win32EnvironmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 320, 1, 6),
    _Win32EnvironmentStatus_Type()
)
win32EnvironmentStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32EnvironmentStatus.setStatus("mandatory")
_Win32IRQResourceTable_Object = MibTable
win32IRQResourceTable = _Win32IRQResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 330)
)
if mibBuilder.loadTexts:
    win32IRQResourceTable.setStatus("mandatory")
_Win32IRQResourceEntry_Object = MibTableRow
win32IRQResourceEntry = _Win32IRQResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 330, 1)
)
win32IRQResourceEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32IRQResourceKeyIndex"),
)
if mibBuilder.loadTexts:
    win32IRQResourceEntry.setStatus("mandatory")
_Win32IRQResourceKeyIndex_Type = String
_Win32IRQResourceKeyIndex_Object = MibTableColumn
win32IRQResourceKeyIndex = _Win32IRQResourceKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 330, 1, 1),
    _Win32IRQResourceKeyIndex_Type()
)
win32IRQResourceKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32IRQResourceKeyIndex.setStatus("mandatory")
_Win32IRQResourceVector_Type = Uint32
_Win32IRQResourceVector_Object = MibTableColumn
win32IRQResourceVector = _Win32IRQResourceVector_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 330, 1, 2),
    _Win32IRQResourceVector_Type()
)
win32IRQResourceVector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32IRQResourceVector.setStatus("mandatory")
_Win32IRQResourceHardware_Type = Boolean
_Win32IRQResourceHardware_Object = MibTableColumn
win32IRQResourceHardware = _Win32IRQResourceHardware_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 330, 1, 3),
    _Win32IRQResourceHardware_Type()
)
win32IRQResourceHardware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32IRQResourceHardware.setStatus("mandatory")
_Win32IRQResourceStatus_Type = String
_Win32IRQResourceStatus_Object = MibTableColumn
win32IRQResourceStatus = _Win32IRQResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 330, 1, 4),
    _Win32IRQResourceStatus_Type()
)
win32IRQResourceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32IRQResourceStatus.setStatus("mandatory")
_Win32LoadOrderGroupTable_Object = MibTable
win32LoadOrderGroupTable = _Win32LoadOrderGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 340)
)
if mibBuilder.loadTexts:
    win32LoadOrderGroupTable.setStatus("mandatory")
_Win32LoadOrderGroupEntry_Object = MibTableRow
win32LoadOrderGroupEntry = _Win32LoadOrderGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 340, 1)
)
win32LoadOrderGroupEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32LoadOrderGroupKeyIndex"),
)
if mibBuilder.loadTexts:
    win32LoadOrderGroupEntry.setStatus("mandatory")
_Win32LoadOrderGroupKeyIndex_Type = String
_Win32LoadOrderGroupKeyIndex_Object = MibTableColumn
win32LoadOrderGroupKeyIndex = _Win32LoadOrderGroupKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 340, 1, 1),
    _Win32LoadOrderGroupKeyIndex_Type()
)
win32LoadOrderGroupKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LoadOrderGroupKeyIndex.setStatus("mandatory")
_Win32LoadOrderGroupGroupOrder_Type = Uint32
_Win32LoadOrderGroupGroupOrder_Object = MibTableColumn
win32LoadOrderGroupGroupOrder = _Win32LoadOrderGroupGroupOrder_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 340, 1, 2),
    _Win32LoadOrderGroupGroupOrder_Type()
)
win32LoadOrderGroupGroupOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LoadOrderGroupGroupOrder.setStatus("mandatory")
_Win32LoadOrderGroupName_Type = String
_Win32LoadOrderGroupName_Object = MibTableColumn
win32LoadOrderGroupName = _Win32LoadOrderGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 340, 1, 3),
    _Win32LoadOrderGroupName_Type()
)
win32LoadOrderGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LoadOrderGroupName.setStatus("mandatory")
_Win32LoadOrderGroupDriverEnabled_Type = Boolean
_Win32LoadOrderGroupDriverEnabled_Object = MibTableColumn
win32LoadOrderGroupDriverEnabled = _Win32LoadOrderGroupDriverEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 340, 1, 4),
    _Win32LoadOrderGroupDriverEnabled_Type()
)
win32LoadOrderGroupDriverEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LoadOrderGroupDriverEnabled.setStatus("mandatory")
_Win32LoadOrderGroupStatus_Type = String
_Win32LoadOrderGroupStatus_Object = MibTableColumn
win32LoadOrderGroupStatus = _Win32LoadOrderGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 340, 1, 5),
    _Win32LoadOrderGroupStatus_Type()
)
win32LoadOrderGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LoadOrderGroupStatus.setStatus("mandatory")
_Win32NetworkClientTable_Object = MibTable
win32NetworkClientTable = _Win32NetworkClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 350)
)
if mibBuilder.loadTexts:
    win32NetworkClientTable.setStatus("mandatory")
_Win32NetworkClientEntry_Object = MibTableRow
win32NetworkClientEntry = _Win32NetworkClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 350, 1)
)
win32NetworkClientEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32NetworkClientKeyIndex"),
)
if mibBuilder.loadTexts:
    win32NetworkClientEntry.setStatus("mandatory")
_Win32NetworkClientKeyIndex_Type = String
_Win32NetworkClientKeyIndex_Object = MibTableColumn
win32NetworkClientKeyIndex = _Win32NetworkClientKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 350, 1, 1),
    _Win32NetworkClientKeyIndex_Type()
)
win32NetworkClientKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkClientKeyIndex.setStatus("mandatory")
_Win32NetworkClientManufacturer_Type = String
_Win32NetworkClientManufacturer_Object = MibTableColumn
win32NetworkClientManufacturer = _Win32NetworkClientManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 350, 1, 2),
    _Win32NetworkClientManufacturer_Type()
)
win32NetworkClientManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkClientManufacturer.setStatus("mandatory")
_Win32NetworkClientName_Type = String
_Win32NetworkClientName_Object = MibTableColumn
win32NetworkClientName = _Win32NetworkClientName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 350, 1, 3),
    _Win32NetworkClientName_Type()
)
win32NetworkClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkClientName.setStatus("mandatory")
_Win32NetworkClientStatus_Type = String
_Win32NetworkClientStatus_Object = MibTableColumn
win32NetworkClientStatus = _Win32NetworkClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 350, 1, 4),
    _Win32NetworkClientStatus_Type()
)
win32NetworkClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkClientStatus.setStatus("mandatory")
_Win32ShareTable_Object = MibTable
win32ShareTable = _Win32ShareTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 360)
)
if mibBuilder.loadTexts:
    win32ShareTable.setStatus("mandatory")
_Win32ShareEntry_Object = MibTableRow
win32ShareEntry = _Win32ShareEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 360, 1)
)
win32ShareEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32ShareKeyIndex"),
)
if mibBuilder.loadTexts:
    win32ShareEntry.setStatus("mandatory")
_Win32ShareKeyIndex_Type = String
_Win32ShareKeyIndex_Object = MibTableColumn
win32ShareKeyIndex = _Win32ShareKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 360, 1, 1),
    _Win32ShareKeyIndex_Type()
)
win32ShareKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ShareKeyIndex.setStatus("mandatory")
_Win32ShareAllowMaximum_Type = Boolean
_Win32ShareAllowMaximum_Object = MibTableColumn
win32ShareAllowMaximum = _Win32ShareAllowMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 360, 1, 2),
    _Win32ShareAllowMaximum_Type()
)
win32ShareAllowMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ShareAllowMaximum.setStatus("mandatory")
_Win32ShareMaximumAllowed_Type = Uint32
_Win32ShareMaximumAllowed_Object = MibTableColumn
win32ShareMaximumAllowed = _Win32ShareMaximumAllowed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 360, 1, 3),
    _Win32ShareMaximumAllowed_Type()
)
win32ShareMaximumAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ShareMaximumAllowed.setStatus("mandatory")
_Win32ShareName_Type = String
_Win32ShareName_Object = MibTableColumn
win32ShareName = _Win32ShareName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 360, 1, 4),
    _Win32ShareName_Type()
)
win32ShareName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ShareName.setStatus("mandatory")
_Win32SharePath_Type = String
_Win32SharePath_Object = MibTableColumn
win32SharePath = _Win32SharePath_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 360, 1, 5),
    _Win32SharePath_Type()
)
win32SharePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SharePath.setStatus("mandatory")
_Win32ShareType_Type = Uint32
_Win32ShareType_Object = MibTableColumn
win32ShareType = _Win32ShareType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 360, 1, 6),
    _Win32ShareType_Type()
)
win32ShareType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ShareType.setStatus("mandatory")
_Win32ShareStatus_Type = String
_Win32ShareStatus_Object = MibTableColumn
win32ShareStatus = _Win32ShareStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 360, 1, 7),
    _Win32ShareStatus_Type()
)
win32ShareStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ShareStatus.setStatus("mandatory")
_Win32RegistryTable_Object = MibTable
win32RegistryTable = _Win32RegistryTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 370)
)
if mibBuilder.loadTexts:
    win32RegistryTable.setStatus("mandatory")
_Win32RegistryEntry_Object = MibTableRow
win32RegistryEntry = _Win32RegistryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 370, 1)
)
win32RegistryEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32RegistryKeyIndex"),
)
if mibBuilder.loadTexts:
    win32RegistryEntry.setStatus("mandatory")
_Win32RegistryKeyIndex_Type = String
_Win32RegistryKeyIndex_Object = MibTableColumn
win32RegistryKeyIndex = _Win32RegistryKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 370, 1, 1),
    _Win32RegistryKeyIndex_Type()
)
win32RegistryKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32RegistryKeyIndex.setStatus("mandatory")
_Win32RegistryCurrentSize_Type = Uint32
_Win32RegistryCurrentSize_Object = MibTableColumn
win32RegistryCurrentSize = _Win32RegistryCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 370, 1, 2),
    _Win32RegistryCurrentSize_Type()
)
win32RegistryCurrentSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32RegistryCurrentSize.setStatus("mandatory")
_Win32RegistryProposedSize_Type = Uint32
_Win32RegistryProposedSize_Object = MibTableColumn
win32RegistryProposedSize = _Win32RegistryProposedSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 370, 1, 3),
    _Win32RegistryProposedSize_Type()
)
win32RegistryProposedSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32RegistryProposedSize.setStatus("mandatory")
_Win32RegistryMaximumSize_Type = Uint32
_Win32RegistryMaximumSize_Object = MibTableColumn
win32RegistryMaximumSize = _Win32RegistryMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 370, 1, 4),
    _Win32RegistryMaximumSize_Type()
)
win32RegistryMaximumSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32RegistryMaximumSize.setStatus("mandatory")
_Win32RegistryName_Type = String
_Win32RegistryName_Object = MibTableColumn
win32RegistryName = _Win32RegistryName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 370, 1, 5),
    _Win32RegistryName_Type()
)
win32RegistryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32RegistryName.setStatus("mandatory")
_Win32RegistryStatus_Type = String
_Win32RegistryStatus_Object = MibTableColumn
win32RegistryStatus = _Win32RegistryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 370, 1, 6),
    _Win32RegistryStatus_Type()
)
win32RegistryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32RegistryStatus.setStatus("mandatory")
_Win32NetworkProtocolTable_Object = MibTable
win32NetworkProtocolTable = _Win32NetworkProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380)
)
if mibBuilder.loadTexts:
    win32NetworkProtocolTable.setStatus("mandatory")
_Win32NetworkProtocolEntry_Object = MibTableRow
win32NetworkProtocolEntry = _Win32NetworkProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1)
)
win32NetworkProtocolEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32NetworkProtocolKeyIndex"),
)
if mibBuilder.loadTexts:
    win32NetworkProtocolEntry.setStatus("mandatory")
_Win32NetworkProtocolKeyIndex_Type = String
_Win32NetworkProtocolKeyIndex_Object = MibTableColumn
win32NetworkProtocolKeyIndex = _Win32NetworkProtocolKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 1),
    _Win32NetworkProtocolKeyIndex_Type()
)
win32NetworkProtocolKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolKeyIndex.setStatus("mandatory")
_Win32NetworkProtocolConnectionlessService_Type = Boolean
_Win32NetworkProtocolConnectionlessService_Object = MibTableColumn
win32NetworkProtocolConnectionlessService = _Win32NetworkProtocolConnectionlessService_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 2),
    _Win32NetworkProtocolConnectionlessService_Type()
)
win32NetworkProtocolConnectionlessService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolConnectionlessService.setStatus("mandatory")
_Win32NetworkProtocolGuranteesDelivery_Type = Boolean
_Win32NetworkProtocolGuranteesDelivery_Object = MibTableColumn
win32NetworkProtocolGuranteesDelivery = _Win32NetworkProtocolGuranteesDelivery_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 3),
    _Win32NetworkProtocolGuranteesDelivery_Type()
)
win32NetworkProtocolGuranteesDelivery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolGuranteesDelivery.setStatus("mandatory")
_Win32NetworkProtocolGuranteesSequencing_Type = Boolean
_Win32NetworkProtocolGuranteesSequencing_Object = MibTableColumn
win32NetworkProtocolGuranteesSequencing = _Win32NetworkProtocolGuranteesSequencing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 4),
    _Win32NetworkProtocolGuranteesSequencing_Type()
)
win32NetworkProtocolGuranteesSequencing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolGuranteesSequencing.setStatus("mandatory")
_Win32NetworkProtocolMaximumAddressSize_Type = Uint32
_Win32NetworkProtocolMaximumAddressSize_Object = MibTableColumn
win32NetworkProtocolMaximumAddressSize = _Win32NetworkProtocolMaximumAddressSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 5),
    _Win32NetworkProtocolMaximumAddressSize_Type()
)
win32NetworkProtocolMaximumAddressSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolMaximumAddressSize.setStatus("mandatory")
_Win32NetworkProtocolMaximumMessageSize_Type = Uint32
_Win32NetworkProtocolMaximumMessageSize_Object = MibTableColumn
win32NetworkProtocolMaximumMessageSize = _Win32NetworkProtocolMaximumMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 6),
    _Win32NetworkProtocolMaximumMessageSize_Type()
)
win32NetworkProtocolMaximumMessageSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolMaximumMessageSize.setStatus("mandatory")
_Win32NetworkProtocolMessageOriented_Type = Boolean
_Win32NetworkProtocolMessageOriented_Object = MibTableColumn
win32NetworkProtocolMessageOriented = _Win32NetworkProtocolMessageOriented_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 7),
    _Win32NetworkProtocolMessageOriented_Type()
)
win32NetworkProtocolMessageOriented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolMessageOriented.setStatus("mandatory")
_Win32NetworkProtocolMinimumAddressSize_Type = Uint32
_Win32NetworkProtocolMinimumAddressSize_Object = MibTableColumn
win32NetworkProtocolMinimumAddressSize = _Win32NetworkProtocolMinimumAddressSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 8),
    _Win32NetworkProtocolMinimumAddressSize_Type()
)
win32NetworkProtocolMinimumAddressSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolMinimumAddressSize.setStatus("mandatory")
_Win32NetworkProtocolName_Type = String
_Win32NetworkProtocolName_Object = MibTableColumn
win32NetworkProtocolName = _Win32NetworkProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 9),
    _Win32NetworkProtocolName_Type()
)
win32NetworkProtocolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolName.setStatus("mandatory")
_Win32NetworkProtocolPseudoStreamOriented_Type = Boolean
_Win32NetworkProtocolPseudoStreamOriented_Object = MibTableColumn
win32NetworkProtocolPseudoStreamOriented = _Win32NetworkProtocolPseudoStreamOriented_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 10),
    _Win32NetworkProtocolPseudoStreamOriented_Type()
)
win32NetworkProtocolPseudoStreamOriented.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolPseudoStreamOriented.setStatus("mandatory")
_Win32NetworkProtocolSupportsBroadcasting_Type = Boolean
_Win32NetworkProtocolSupportsBroadcasting_Object = MibTableColumn
win32NetworkProtocolSupportsBroadcasting = _Win32NetworkProtocolSupportsBroadcasting_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 11),
    _Win32NetworkProtocolSupportsBroadcasting_Type()
)
win32NetworkProtocolSupportsBroadcasting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolSupportsBroadcasting.setStatus("mandatory")
_Win32NetworkProtocolSupportsConnectData_Type = Boolean
_Win32NetworkProtocolSupportsConnectData_Object = MibTableColumn
win32NetworkProtocolSupportsConnectData = _Win32NetworkProtocolSupportsConnectData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 12),
    _Win32NetworkProtocolSupportsConnectData_Type()
)
win32NetworkProtocolSupportsConnectData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolSupportsConnectData.setStatus("mandatory")
_Win32NetworkProtocolSupportsDisconnectData_Type = Boolean
_Win32NetworkProtocolSupportsDisconnectData_Object = MibTableColumn
win32NetworkProtocolSupportsDisconnectData = _Win32NetworkProtocolSupportsDisconnectData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 13),
    _Win32NetworkProtocolSupportsDisconnectData_Type()
)
win32NetworkProtocolSupportsDisconnectData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolSupportsDisconnectData.setStatus("mandatory")
_Win32NetworkProtocolSupportsEncryption_Type = Boolean
_Win32NetworkProtocolSupportsEncryption_Object = MibTableColumn
win32NetworkProtocolSupportsEncryption = _Win32NetworkProtocolSupportsEncryption_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 14),
    _Win32NetworkProtocolSupportsEncryption_Type()
)
win32NetworkProtocolSupportsEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolSupportsEncryption.setStatus("mandatory")
_Win32NetworkProtocolSupportsExpiditeData_Type = Boolean
_Win32NetworkProtocolSupportsExpiditeData_Object = MibTableColumn
win32NetworkProtocolSupportsExpiditeData = _Win32NetworkProtocolSupportsExpiditeData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 15),
    _Win32NetworkProtocolSupportsExpiditeData_Type()
)
win32NetworkProtocolSupportsExpiditeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolSupportsExpiditeData.setStatus("mandatory")
_Win32NetworkProtocolSupportsFragmentation_Type = Boolean
_Win32NetworkProtocolSupportsFragmentation_Object = MibTableColumn
win32NetworkProtocolSupportsFragmentation = _Win32NetworkProtocolSupportsFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 16),
    _Win32NetworkProtocolSupportsFragmentation_Type()
)
win32NetworkProtocolSupportsFragmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolSupportsFragmentation.setStatus("mandatory")
_Win32NetworkProtocolSupportsGracefulClosing_Type = Boolean
_Win32NetworkProtocolSupportsGracefulClosing_Object = MibTableColumn
win32NetworkProtocolSupportsGracefulClosing = _Win32NetworkProtocolSupportsGracefulClosing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 17),
    _Win32NetworkProtocolSupportsGracefulClosing_Type()
)
win32NetworkProtocolSupportsGracefulClosing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolSupportsGracefulClosing.setStatus("mandatory")
_Win32NetworkProtocolSupportsGuaranteedBandwidth_Type = Boolean
_Win32NetworkProtocolSupportsGuaranteedBandwidth_Object = MibTableColumn
win32NetworkProtocolSupportsGuaranteedBandwidth = _Win32NetworkProtocolSupportsGuaranteedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 18),
    _Win32NetworkProtocolSupportsGuaranteedBandwidth_Type()
)
win32NetworkProtocolSupportsGuaranteedBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolSupportsGuaranteedBandwidth.setStatus("mandatory")
_Win32NetworkProtocolSupportsMulticasting_Type = Boolean
_Win32NetworkProtocolSupportsMulticasting_Object = MibTableColumn
win32NetworkProtocolSupportsMulticasting = _Win32NetworkProtocolSupportsMulticasting_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 19),
    _Win32NetworkProtocolSupportsMulticasting_Type()
)
win32NetworkProtocolSupportsMulticasting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolSupportsMulticasting.setStatus("mandatory")
_Win32NetworkProtocolStatus_Type = String
_Win32NetworkProtocolStatus_Object = MibTableColumn
win32NetworkProtocolStatus = _Win32NetworkProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 380, 1, 20),
    _Win32NetworkProtocolStatus_Type()
)
win32NetworkProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkProtocolStatus.setStatus("mandatory")
_Win32ProcessStartupTable_Object = MibTable
win32ProcessStartupTable = _Win32ProcessStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400)
)
if mibBuilder.loadTexts:
    win32ProcessStartupTable.setStatus("mandatory")
_Win32ProcessStartupEntry_Object = MibTableRow
win32ProcessStartupEntry = _Win32ProcessStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1)
)
win32ProcessStartupEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32ProcessStartupKeyIndex"),
)
if mibBuilder.loadTexts:
    win32ProcessStartupEntry.setStatus("mandatory")
_Win32ProcessStartupKeyIndex_Type = String
_Win32ProcessStartupKeyIndex_Object = MibTableColumn
win32ProcessStartupKeyIndex = _Win32ProcessStartupKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 1),
    _Win32ProcessStartupKeyIndex_Type()
)
win32ProcessStartupKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupKeyIndex.setStatus("mandatory")
_Win32ProcessStartupCreateFlags_Type = Uint32
_Win32ProcessStartupCreateFlags_Object = MibTableColumn
win32ProcessStartupCreateFlags = _Win32ProcessStartupCreateFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 2),
    _Win32ProcessStartupCreateFlags_Type()
)
win32ProcessStartupCreateFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupCreateFlags.setStatus("mandatory")
_Win32ProcessStartupPriorityClass_Type = Uint32
_Win32ProcessStartupPriorityClass_Object = MibTableColumn
win32ProcessStartupPriorityClass = _Win32ProcessStartupPriorityClass_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 3),
    _Win32ProcessStartupPriorityClass_Type()
)
win32ProcessStartupPriorityClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupPriorityClass.setStatus("mandatory")
_Win32ProcessStartupWinstationDesktop_Type = String
_Win32ProcessStartupWinstationDesktop_Object = MibTableColumn
win32ProcessStartupWinstationDesktop = _Win32ProcessStartupWinstationDesktop_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 5),
    _Win32ProcessStartupWinstationDesktop_Type()
)
win32ProcessStartupWinstationDesktop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupWinstationDesktop.setStatus("mandatory")
_Win32ProcessStartupTitle_Type = String
_Win32ProcessStartupTitle_Object = MibTableColumn
win32ProcessStartupTitle = _Win32ProcessStartupTitle_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 6),
    _Win32ProcessStartupTitle_Type()
)
win32ProcessStartupTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupTitle.setStatus("mandatory")
_Win32ProcessStartupX_Type = Uint32
_Win32ProcessStartupX_Object = MibTableColumn
win32ProcessStartupX = _Win32ProcessStartupX_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 7),
    _Win32ProcessStartupX_Type()
)
win32ProcessStartupX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupX.setStatus("mandatory")
_Win32ProcessStartupY_Type = Uint32
_Win32ProcessStartupY_Object = MibTableColumn
win32ProcessStartupY = _Win32ProcessStartupY_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 8),
    _Win32ProcessStartupY_Type()
)
win32ProcessStartupY.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupY.setStatus("mandatory")
_Win32ProcessStartupXSize_Type = Uint32
_Win32ProcessStartupXSize_Object = MibTableColumn
win32ProcessStartupXSize = _Win32ProcessStartupXSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 9),
    _Win32ProcessStartupXSize_Type()
)
win32ProcessStartupXSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupXSize.setStatus("mandatory")
_Win32ProcessStartupYSize_Type = Uint32
_Win32ProcessStartupYSize_Object = MibTableColumn
win32ProcessStartupYSize = _Win32ProcessStartupYSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 10),
    _Win32ProcessStartupYSize_Type()
)
win32ProcessStartupYSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupYSize.setStatus("mandatory")
_Win32ProcessStartupXCountChars_Type = Uint32
_Win32ProcessStartupXCountChars_Object = MibTableColumn
win32ProcessStartupXCountChars = _Win32ProcessStartupXCountChars_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 11),
    _Win32ProcessStartupXCountChars_Type()
)
win32ProcessStartupXCountChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupXCountChars.setStatus("mandatory")
_Win32ProcessStartupYCountChars_Type = Uint32
_Win32ProcessStartupYCountChars_Object = MibTableColumn
win32ProcessStartupYCountChars = _Win32ProcessStartupYCountChars_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 12),
    _Win32ProcessStartupYCountChars_Type()
)
win32ProcessStartupYCountChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupYCountChars.setStatus("mandatory")
_Win32ProcessStartupFillAttribute_Type = Uint32
_Win32ProcessStartupFillAttribute_Object = MibTableColumn
win32ProcessStartupFillAttribute = _Win32ProcessStartupFillAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 13),
    _Win32ProcessStartupFillAttribute_Type()
)
win32ProcessStartupFillAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupFillAttribute.setStatus("mandatory")
_Win32ProcessStartupShowWindow_Type = Uint16
_Win32ProcessStartupShowWindow_Object = MibTableColumn
win32ProcessStartupShowWindow = _Win32ProcessStartupShowWindow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 14),
    _Win32ProcessStartupShowWindow_Type()
)
win32ProcessStartupShowWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupShowWindow.setStatus("mandatory")
_Win32ProcessStartupErrorMode_Type = Uint16
_Win32ProcessStartupErrorMode_Object = MibTableColumn
win32ProcessStartupErrorMode = _Win32ProcessStartupErrorMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 15),
    _Win32ProcessStartupErrorMode_Type()
)
win32ProcessStartupErrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupErrorMode.setStatus("mandatory")
_Win32ProcessStartupStatus_Type = String
_Win32ProcessStartupStatus_Object = MibTableColumn
win32ProcessStartupStatus = _Win32ProcessStartupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 400, 1, 16),
    _Win32ProcessStartupStatus_Type()
)
win32ProcessStartupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStartupStatus.setStatus("mandatory")
_Win32ProcessTable_Object = MibTable
win32ProcessTable = _Win32ProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410)
)
if mibBuilder.loadTexts:
    win32ProcessTable.setStatus("mandatory")
_Win32ProcessEntry_Object = MibTableRow
win32ProcessEntry = _Win32ProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1)
)
win32ProcessEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32ProcessKeyIndex"),
)
if mibBuilder.loadTexts:
    win32ProcessEntry.setStatus("mandatory")
_Win32ProcessKeyIndex_Type = String
_Win32ProcessKeyIndex_Object = MibTableColumn
win32ProcessKeyIndex = _Win32ProcessKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1, 1),
    _Win32ProcessKeyIndex_Type()
)
win32ProcessKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessKeyIndex.setStatus("mandatory")
_Win32ProcessExecutablePath_Type = String
_Win32ProcessExecutablePath_Object = MibTableColumn
win32ProcessExecutablePath = _Win32ProcessExecutablePath_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1, 2),
    _Win32ProcessExecutablePath_Type()
)
win32ProcessExecutablePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessExecutablePath.setStatus("mandatory")
_Win32ProcessMaximumWorkingSetSize_Type = Uint32
_Win32ProcessMaximumWorkingSetSize_Object = MibTableColumn
win32ProcessMaximumWorkingSetSize = _Win32ProcessMaximumWorkingSetSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1, 3),
    _Win32ProcessMaximumWorkingSetSize_Type()
)
win32ProcessMaximumWorkingSetSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessMaximumWorkingSetSize.setStatus("mandatory")
_Win32ProcessMinimumWorkingSetSize_Type = Uint32
_Win32ProcessMinimumWorkingSetSize_Object = MibTableColumn
win32ProcessMinimumWorkingSetSize = _Win32ProcessMinimumWorkingSetSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1, 4),
    _Win32ProcessMinimumWorkingSetSize_Type()
)
win32ProcessMinimumWorkingSetSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessMinimumWorkingSetSize.setStatus("mandatory")
_Win32ProcessPageFaults_Type = Uint32
_Win32ProcessPageFaults_Object = MibTableColumn
win32ProcessPageFaults = _Win32ProcessPageFaults_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1, 5),
    _Win32ProcessPageFaults_Type()
)
win32ProcessPageFaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessPageFaults.setStatus("mandatory")
_Win32ProcessPageFileUsage_Type = Uint32
_Win32ProcessPageFileUsage_Object = MibTableColumn
win32ProcessPageFileUsage = _Win32ProcessPageFileUsage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1, 6),
    _Win32ProcessPageFileUsage_Type()
)
win32ProcessPageFileUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessPageFileUsage.setStatus("mandatory")
_Win32ProcessPeakWorkingSetSize_Type = Uint32
_Win32ProcessPeakWorkingSetSize_Object = MibTableColumn
win32ProcessPeakWorkingSetSize = _Win32ProcessPeakWorkingSetSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1, 7),
    _Win32ProcessPeakWorkingSetSize_Type()
)
win32ProcessPeakWorkingSetSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessPeakWorkingSetSize.setStatus("mandatory")
_Win32ProcessProcessId_Type = Uint32
_Win32ProcessProcessId_Object = MibTableColumn
win32ProcessProcessId = _Win32ProcessProcessId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1, 8),
    _Win32ProcessProcessId_Type()
)
win32ProcessProcessId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessProcessId.setStatus("mandatory")
_Win32ProcessQuotaNonPagedPoolUsage_Type = Uint32
_Win32ProcessQuotaNonPagedPoolUsage_Object = MibTableColumn
win32ProcessQuotaNonPagedPoolUsage = _Win32ProcessQuotaNonPagedPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1, 9),
    _Win32ProcessQuotaNonPagedPoolUsage_Type()
)
win32ProcessQuotaNonPagedPoolUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessQuotaNonPagedPoolUsage.setStatus("mandatory")
_Win32ProcessQuotaPagedPoolUsage_Type = Uint32
_Win32ProcessQuotaPagedPoolUsage_Object = MibTableColumn
win32ProcessQuotaPagedPoolUsage = _Win32ProcessQuotaPagedPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1, 10),
    _Win32ProcessQuotaPagedPoolUsage_Type()
)
win32ProcessQuotaPagedPoolUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessQuotaPagedPoolUsage.setStatus("mandatory")
_Win32ProcessQuotaPeakNonPagedPoolUsage_Type = Uint32
_Win32ProcessQuotaPeakNonPagedPoolUsage_Object = MibTableColumn
win32ProcessQuotaPeakNonPagedPoolUsage = _Win32ProcessQuotaPeakNonPagedPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1, 11),
    _Win32ProcessQuotaPeakNonPagedPoolUsage_Type()
)
win32ProcessQuotaPeakNonPagedPoolUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessQuotaPeakNonPagedPoolUsage.setStatus("mandatory")
_Win32ProcessQuotaPeakPagedPoolUsage_Type = Uint32
_Win32ProcessQuotaPeakPagedPoolUsage_Object = MibTableColumn
win32ProcessQuotaPeakPagedPoolUsage = _Win32ProcessQuotaPeakPagedPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1, 12),
    _Win32ProcessQuotaPeakPagedPoolUsage_Type()
)
win32ProcessQuotaPeakPagedPoolUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessQuotaPeakPagedPoolUsage.setStatus("mandatory")
_Win32ProcessWindowsVersion_Type = String
_Win32ProcessWindowsVersion_Object = MibTableColumn
win32ProcessWindowsVersion = _Win32ProcessWindowsVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1, 13),
    _Win32ProcessWindowsVersion_Type()
)
win32ProcessWindowsVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessWindowsVersion.setStatus("mandatory")
_Win32ProcessStatus_Type = String
_Win32ProcessStatus_Object = MibTableColumn
win32ProcessStatus = _Win32ProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 410, 1, 14),
    _Win32ProcessStatus_Type()
)
win32ProcessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProcessStatus.setStatus("mandatory")
_Win32ThreadTable_Object = MibTable
win32ThreadTable = _Win32ThreadTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 420)
)
if mibBuilder.loadTexts:
    win32ThreadTable.setStatus("mandatory")
_Win32ThreadEntry_Object = MibTableRow
win32ThreadEntry = _Win32ThreadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 420, 1)
)
win32ThreadEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32ThreadKeyIndex"),
)
if mibBuilder.loadTexts:
    win32ThreadEntry.setStatus("mandatory")
_Win32ThreadKeyIndex_Type = String
_Win32ThreadKeyIndex_Object = MibTableColumn
win32ThreadKeyIndex = _Win32ThreadKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 420, 1, 1),
    _Win32ThreadKeyIndex_Type()
)
win32ThreadKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ThreadKeyIndex.setStatus("mandatory")
_Win32ThreadProcessHandle_Type = String
_Win32ThreadProcessHandle_Object = MibTableColumn
win32ThreadProcessHandle = _Win32ThreadProcessHandle_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 420, 1, 2),
    _Win32ThreadProcessHandle_Type()
)
win32ThreadProcessHandle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ThreadProcessHandle.setStatus("mandatory")
_Win32ThreadHandle_Type = String
_Win32ThreadHandle_Object = MibTableColumn
win32ThreadHandle = _Win32ThreadHandle_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 420, 1, 3),
    _Win32ThreadHandle_Type()
)
win32ThreadHandle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ThreadHandle.setStatus("mandatory")
_Win32ThreadElapsedTime_Type = String
_Win32ThreadElapsedTime_Object = MibTableColumn
win32ThreadElapsedTime = _Win32ThreadElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 420, 1, 4),
    _Win32ThreadElapsedTime_Type()
)
win32ThreadElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ThreadElapsedTime.setStatus("mandatory")
_Win32ThreadPriorityBase_Type = Uint32
_Win32ThreadPriorityBase_Object = MibTableColumn
win32ThreadPriorityBase = _Win32ThreadPriorityBase_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 420, 1, 5),
    _Win32ThreadPriorityBase_Type()
)
win32ThreadPriorityBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ThreadPriorityBase.setStatus("mandatory")
_Win32ThreadPriority_Type = Uint32
_Win32ThreadPriority_Object = MibTableColumn
win32ThreadPriority = _Win32ThreadPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 420, 1, 6),
    _Win32ThreadPriority_Type()
)
win32ThreadPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ThreadPriority.setStatus("mandatory")
_Win32ThreadStartAddress_Type = Uint32
_Win32ThreadStartAddress_Object = MibTableColumn
win32ThreadStartAddress = _Win32ThreadStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 420, 1, 7),
    _Win32ThreadStartAddress_Type()
)
win32ThreadStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ThreadStartAddress.setStatus("mandatory")
_Win32ThreadThreadState_Type = Uint32
_Win32ThreadThreadState_Object = MibTableColumn
win32ThreadThreadState = _Win32ThreadThreadState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 420, 1, 8),
    _Win32ThreadThreadState_Type()
)
win32ThreadThreadState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ThreadThreadState.setStatus("mandatory")
_Win32ThreadThreadWaitReason_Type = Uint32
_Win32ThreadThreadWaitReason_Object = MibTableColumn
win32ThreadThreadWaitReason = _Win32ThreadThreadWaitReason_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 420, 1, 9),
    _Win32ThreadThreadWaitReason_Type()
)
win32ThreadThreadWaitReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ThreadThreadWaitReason.setStatus("mandatory")
_Win32ThreadStatus_Type = String
_Win32ThreadStatus_Object = MibTableColumn
win32ThreadStatus = _Win32ThreadStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 420, 1, 10),
    _Win32ThreadStatus_Type()
)
win32ThreadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ThreadStatus.setStatus("mandatory")
_Win32OperatingSystemTable_Object = MibTable
win32OperatingSystemTable = _Win32OperatingSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430)
)
if mibBuilder.loadTexts:
    win32OperatingSystemTable.setStatus("mandatory")
_Win32OperatingSystemEntry_Object = MibTableRow
win32OperatingSystemEntry = _Win32OperatingSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1)
)
win32OperatingSystemEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32OperatingSystemKeyIndex"),
)
if mibBuilder.loadTexts:
    win32OperatingSystemEntry.setStatus("mandatory")
_Win32OperatingSystemKeyIndex_Type = String
_Win32OperatingSystemKeyIndex_Object = MibTableColumn
win32OperatingSystemKeyIndex = _Win32OperatingSystemKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 1),
    _Win32OperatingSystemKeyIndex_Type()
)
win32OperatingSystemKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemKeyIndex.setStatus("mandatory")
_Win32OperatingSystemBootDevice_Type = String
_Win32OperatingSystemBootDevice_Object = MibTableColumn
win32OperatingSystemBootDevice = _Win32OperatingSystemBootDevice_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 2),
    _Win32OperatingSystemBootDevice_Type()
)
win32OperatingSystemBootDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemBootDevice.setStatus("mandatory")
_Win32OperatingSystemBuildNumber_Type = String
_Win32OperatingSystemBuildNumber_Object = MibTableColumn
win32OperatingSystemBuildNumber = _Win32OperatingSystemBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 3),
    _Win32OperatingSystemBuildNumber_Type()
)
win32OperatingSystemBuildNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemBuildNumber.setStatus("mandatory")
_Win32OperatingSystemBuildType_Type = String
_Win32OperatingSystemBuildType_Object = MibTableColumn
win32OperatingSystemBuildType = _Win32OperatingSystemBuildType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 4),
    _Win32OperatingSystemBuildType_Type()
)
win32OperatingSystemBuildType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemBuildType.setStatus("mandatory")
_Win32OperatingSystemCodeSet_Type = String
_Win32OperatingSystemCodeSet_Object = MibTableColumn
win32OperatingSystemCodeSet = _Win32OperatingSystemCodeSet_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 5),
    _Win32OperatingSystemCodeSet_Type()
)
win32OperatingSystemCodeSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemCodeSet.setStatus("mandatory")
_Win32OperatingSystemCountryCode_Type = String
_Win32OperatingSystemCountryCode_Object = MibTableColumn
win32OperatingSystemCountryCode = _Win32OperatingSystemCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 6),
    _Win32OperatingSystemCountryCode_Type()
)
win32OperatingSystemCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemCountryCode.setStatus("mandatory")
_Win32OperatingSystemCSDVersion_Type = String
_Win32OperatingSystemCSDVersion_Object = MibTableColumn
win32OperatingSystemCSDVersion = _Win32OperatingSystemCSDVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 7),
    _Win32OperatingSystemCSDVersion_Type()
)
win32OperatingSystemCSDVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemCSDVersion.setStatus("mandatory")
_Win32OperatingSystemDebug_Type = Boolean
_Win32OperatingSystemDebug_Object = MibTableColumn
win32OperatingSystemDebug = _Win32OperatingSystemDebug_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 8),
    _Win32OperatingSystemDebug_Type()
)
win32OperatingSystemDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemDebug.setStatus("mandatory")
_Win32OperatingSystemForegroundApplicationBoost_Type = Uint8
_Win32OperatingSystemForegroundApplicationBoost_Object = MibTableColumn
win32OperatingSystemForegroundApplicationBoost = _Win32OperatingSystemForegroundApplicationBoost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 9),
    _Win32OperatingSystemForegroundApplicationBoost_Type()
)
win32OperatingSystemForegroundApplicationBoost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemForegroundApplicationBoost.setStatus("mandatory")
_Win32OperatingSystemLocale_Type = String
_Win32OperatingSystemLocale_Object = MibTableColumn
win32OperatingSystemLocale = _Win32OperatingSystemLocale_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 10),
    _Win32OperatingSystemLocale_Type()
)
win32OperatingSystemLocale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemLocale.setStatus("mandatory")
_Win32OperatingSystemManufacturer_Type = String
_Win32OperatingSystemManufacturer_Object = MibTableColumn
win32OperatingSystemManufacturer = _Win32OperatingSystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 11),
    _Win32OperatingSystemManufacturer_Type()
)
win32OperatingSystemManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemManufacturer.setStatus("mandatory")
_Win32OperatingSystemOrganization_Type = String
_Win32OperatingSystemOrganization_Object = MibTableColumn
win32OperatingSystemOrganization = _Win32OperatingSystemOrganization_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 12),
    _Win32OperatingSystemOrganization_Type()
)
win32OperatingSystemOrganization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemOrganization.setStatus("mandatory")
_Win32OperatingSystemOSLanguage_Type = Uint32
_Win32OperatingSystemOSLanguage_Object = MibTableColumn
win32OperatingSystemOSLanguage = _Win32OperatingSystemOSLanguage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 13),
    _Win32OperatingSystemOSLanguage_Type()
)
win32OperatingSystemOSLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemOSLanguage.setStatus("mandatory")
_Win32OperatingSystemPlusProductID_Type = String
_Win32OperatingSystemPlusProductID_Object = MibTableColumn
win32OperatingSystemPlusProductID = _Win32OperatingSystemPlusProductID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 14),
    _Win32OperatingSystemPlusProductID_Type()
)
win32OperatingSystemPlusProductID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemPlusProductID.setStatus("mandatory")
_Win32OperatingSystemPlusVersionNumber_Type = String
_Win32OperatingSystemPlusVersionNumber_Object = MibTableColumn
win32OperatingSystemPlusVersionNumber = _Win32OperatingSystemPlusVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 15),
    _Win32OperatingSystemPlusVersionNumber_Type()
)
win32OperatingSystemPlusVersionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemPlusVersionNumber.setStatus("mandatory")
_Win32OperatingSystemPrimary_Type = Boolean
_Win32OperatingSystemPrimary_Object = MibTableColumn
win32OperatingSystemPrimary = _Win32OperatingSystemPrimary_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 16),
    _Win32OperatingSystemPrimary_Type()
)
win32OperatingSystemPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemPrimary.setStatus("mandatory")
_Win32OperatingSystemQuantumLength_Type = Uint8
_Win32OperatingSystemQuantumLength_Object = MibTableColumn
win32OperatingSystemQuantumLength = _Win32OperatingSystemQuantumLength_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 17),
    _Win32OperatingSystemQuantumLength_Type()
)
win32OperatingSystemQuantumLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemQuantumLength.setStatus("mandatory")
_Win32OperatingSystemQuantumType_Type = Uint8
_Win32OperatingSystemQuantumType_Object = MibTableColumn
win32OperatingSystemQuantumType = _Win32OperatingSystemQuantumType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 18),
    _Win32OperatingSystemQuantumType_Type()
)
win32OperatingSystemQuantumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemQuantumType.setStatus("mandatory")
_Win32OperatingSystemRegisteredUser_Type = String
_Win32OperatingSystemRegisteredUser_Object = MibTableColumn
win32OperatingSystemRegisteredUser = _Win32OperatingSystemRegisteredUser_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 19),
    _Win32OperatingSystemRegisteredUser_Type()
)
win32OperatingSystemRegisteredUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemRegisteredUser.setStatus("mandatory")
_Win32OperatingSystemSerialNumber_Type = String
_Win32OperatingSystemSerialNumber_Object = MibTableColumn
win32OperatingSystemSerialNumber = _Win32OperatingSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 20),
    _Win32OperatingSystemSerialNumber_Type()
)
win32OperatingSystemSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemSerialNumber.setStatus("mandatory")
_Win32OperatingSystemSystemDevice_Type = String
_Win32OperatingSystemSystemDevice_Object = MibTableColumn
win32OperatingSystemSystemDevice = _Win32OperatingSystemSystemDevice_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 21),
    _Win32OperatingSystemSystemDevice_Type()
)
win32OperatingSystemSystemDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemSystemDevice.setStatus("mandatory")
_Win32OperatingSystemSystemDirectory_Type = String
_Win32OperatingSystemSystemDirectory_Object = MibTableColumn
win32OperatingSystemSystemDirectory = _Win32OperatingSystemSystemDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 22),
    _Win32OperatingSystemSystemDirectory_Type()
)
win32OperatingSystemSystemDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemSystemDirectory.setStatus("mandatory")
_Win32OperatingSystemVersion_Type = String
_Win32OperatingSystemVersion_Object = MibTableColumn
win32OperatingSystemVersion = _Win32OperatingSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 23),
    _Win32OperatingSystemVersion_Type()
)
win32OperatingSystemVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemVersion.setStatus("mandatory")
_Win32OperatingSystemWindowsDirectory_Type = String
_Win32OperatingSystemWindowsDirectory_Object = MibTableColumn
win32OperatingSystemWindowsDirectory = _Win32OperatingSystemWindowsDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 24),
    _Win32OperatingSystemWindowsDirectory_Type()
)
win32OperatingSystemWindowsDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemWindowsDirectory.setStatus("mandatory")
_Win32OperatingSystemDescription_Type = String
_Win32OperatingSystemDescription_Object = MibTableColumn
win32OperatingSystemDescription = _Win32OperatingSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 25),
    _Win32OperatingSystemDescription_Type()
)
win32OperatingSystemDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemDescription.setStatus("mandatory")
_Win32OperatingSystemStatus_Type = String
_Win32OperatingSystemStatus_Object = MibTableColumn
win32OperatingSystemStatus = _Win32OperatingSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 430, 1, 26),
    _Win32OperatingSystemStatus_Type()
)
win32OperatingSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OperatingSystemStatus.setStatus("mandatory")
_Win32PrintJobTable_Object = MibTable
win32PrintJobTable = _Win32PrintJobTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440)
)
if mibBuilder.loadTexts:
    win32PrintJobTable.setStatus("mandatory")
_Win32PrintJobEntry_Object = MibTableRow
win32PrintJobEntry = _Win32PrintJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440, 1)
)
win32PrintJobEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32PrintJobKeyIndex"),
)
if mibBuilder.loadTexts:
    win32PrintJobEntry.setStatus("mandatory")
_Win32PrintJobKeyIndex_Type = String
_Win32PrintJobKeyIndex_Object = MibTableColumn
win32PrintJobKeyIndex = _Win32PrintJobKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440, 1, 1),
    _Win32PrintJobKeyIndex_Type()
)
win32PrintJobKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrintJobKeyIndex.setStatus("mandatory")
_Win32PrintJobName_Type = String
_Win32PrintJobName_Object = MibTableColumn
win32PrintJobName = _Win32PrintJobName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440, 1, 2),
    _Win32PrintJobName_Type()
)
win32PrintJobName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrintJobName.setStatus("mandatory")
_Win32PrintJobDataType_Type = String
_Win32PrintJobDataType_Object = MibTableColumn
win32PrintJobDataType = _Win32PrintJobDataType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440, 1, 3),
    _Win32PrintJobDataType_Type()
)
win32PrintJobDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrintJobDataType.setStatus("mandatory")
_Win32PrintJobDocument_Type = String
_Win32PrintJobDocument_Object = MibTableColumn
win32PrintJobDocument = _Win32PrintJobDocument_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440, 1, 4),
    _Win32PrintJobDocument_Type()
)
win32PrintJobDocument.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrintJobDocument.setStatus("mandatory")
_Win32PrintJobDriverName_Type = String
_Win32PrintJobDriverName_Object = MibTableColumn
win32PrintJobDriverName = _Win32PrintJobDriverName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440, 1, 5),
    _Win32PrintJobDriverName_Type()
)
win32PrintJobDriverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrintJobDriverName.setStatus("mandatory")
_Win32PrintJobHostPrintQueue_Type = String
_Win32PrintJobHostPrintQueue_Object = MibTableColumn
win32PrintJobHostPrintQueue = _Win32PrintJobHostPrintQueue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440, 1, 6),
    _Win32PrintJobHostPrintQueue_Type()
)
win32PrintJobHostPrintQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrintJobHostPrintQueue.setStatus("mandatory")
_Win32PrintJobJobId_Type = Uint32
_Win32PrintJobJobId_Object = MibTableColumn
win32PrintJobJobId = _Win32PrintJobJobId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440, 1, 7),
    _Win32PrintJobJobId_Type()
)
win32PrintJobJobId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrintJobJobId.setStatus("mandatory")
_Win32PrintJobPagesPrinted_Type = Uint32
_Win32PrintJobPagesPrinted_Object = MibTableColumn
win32PrintJobPagesPrinted = _Win32PrintJobPagesPrinted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440, 1, 8),
    _Win32PrintJobPagesPrinted_Type()
)
win32PrintJobPagesPrinted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrintJobPagesPrinted.setStatus("mandatory")
_Win32PrintJobParameters_Type = String
_Win32PrintJobParameters_Object = MibTableColumn
win32PrintJobParameters = _Win32PrintJobParameters_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440, 1, 9),
    _Win32PrintJobParameters_Type()
)
win32PrintJobParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrintJobParameters.setStatus("mandatory")
_Win32PrintJobPrintProcessor_Type = String
_Win32PrintJobPrintProcessor_Object = MibTableColumn
win32PrintJobPrintProcessor = _Win32PrintJobPrintProcessor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440, 1, 10),
    _Win32PrintJobPrintProcessor_Type()
)
win32PrintJobPrintProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrintJobPrintProcessor.setStatus("mandatory")
_Win32PrintJobSize_Type = Uint32
_Win32PrintJobSize_Object = MibTableColumn
win32PrintJobSize = _Win32PrintJobSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440, 1, 11),
    _Win32PrintJobSize_Type()
)
win32PrintJobSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrintJobSize.setStatus("mandatory")
_Win32PrintJobTotalPages_Type = Uint32
_Win32PrintJobTotalPages_Object = MibTableColumn
win32PrintJobTotalPages = _Win32PrintJobTotalPages_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440, 1, 12),
    _Win32PrintJobTotalPages_Type()
)
win32PrintJobTotalPages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrintJobTotalPages.setStatus("mandatory")
_Win32PrintJobStatus_Type = String
_Win32PrintJobStatus_Object = MibTableColumn
win32PrintJobStatus = _Win32PrintJobStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 440, 1, 13),
    _Win32PrintJobStatus_Type()
)
win32PrintJobStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrintJobStatus.setStatus("mandatory")
_Win32ScheduledJobTable_Object = MibTable
win32ScheduledJobTable = _Win32ScheduledJobTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 450)
)
if mibBuilder.loadTexts:
    win32ScheduledJobTable.setStatus("mandatory")
_Win32ScheduledJobEntry_Object = MibTableRow
win32ScheduledJobEntry = _Win32ScheduledJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 450, 1)
)
win32ScheduledJobEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32ScheduledJobKeyIndex"),
)
if mibBuilder.loadTexts:
    win32ScheduledJobEntry.setStatus("mandatory")
_Win32ScheduledJobKeyIndex_Type = String
_Win32ScheduledJobKeyIndex_Object = MibTableColumn
win32ScheduledJobKeyIndex = _Win32ScheduledJobKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 450, 1, 1),
    _Win32ScheduledJobKeyIndex_Type()
)
win32ScheduledJobKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ScheduledJobKeyIndex.setStatus("mandatory")
_Win32ScheduledJobJobId_Type = Uint32
_Win32ScheduledJobJobId_Object = MibTableColumn
win32ScheduledJobJobId = _Win32ScheduledJobJobId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 450, 1, 2),
    _Win32ScheduledJobJobId_Type()
)
win32ScheduledJobJobId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ScheduledJobJobId.setStatus("mandatory")
_Win32ScheduledJobCommand_Type = String
_Win32ScheduledJobCommand_Object = MibTableColumn
win32ScheduledJobCommand = _Win32ScheduledJobCommand_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 450, 1, 3),
    _Win32ScheduledJobCommand_Type()
)
win32ScheduledJobCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ScheduledJobCommand.setStatus("mandatory")
_Win32ScheduledJobStartTime_Type = Datetime
_Win32ScheduledJobStartTime_Object = MibTableColumn
win32ScheduledJobStartTime = _Win32ScheduledJobStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 450, 1, 4),
    _Win32ScheduledJobStartTime_Type()
)
win32ScheduledJobStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ScheduledJobStartTime.setStatus("mandatory")
_Win32ScheduledJobRunRepeatedly_Type = Boolean
_Win32ScheduledJobRunRepeatedly_Object = MibTableColumn
win32ScheduledJobRunRepeatedly = _Win32ScheduledJobRunRepeatedly_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 450, 1, 5),
    _Win32ScheduledJobRunRepeatedly_Type()
)
win32ScheduledJobRunRepeatedly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ScheduledJobRunRepeatedly.setStatus("mandatory")
_Win32ScheduledJobInteractWithDesktop_Type = Boolean
_Win32ScheduledJobInteractWithDesktop_Object = MibTableColumn
win32ScheduledJobInteractWithDesktop = _Win32ScheduledJobInteractWithDesktop_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 450, 1, 6),
    _Win32ScheduledJobInteractWithDesktop_Type()
)
win32ScheduledJobInteractWithDesktop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ScheduledJobInteractWithDesktop.setStatus("mandatory")
_Win32ScheduledJobDaysOfWeek_Type = Uint32
_Win32ScheduledJobDaysOfWeek_Object = MibTableColumn
win32ScheduledJobDaysOfWeek = _Win32ScheduledJobDaysOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 450, 1, 7),
    _Win32ScheduledJobDaysOfWeek_Type()
)
win32ScheduledJobDaysOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ScheduledJobDaysOfWeek.setStatus("mandatory")
_Win32ScheduledJobDaysOfMonth_Type = Uint32
_Win32ScheduledJobDaysOfMonth_Object = MibTableColumn
win32ScheduledJobDaysOfMonth = _Win32ScheduledJobDaysOfMonth_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 450, 1, 8),
    _Win32ScheduledJobDaysOfMonth_Type()
)
win32ScheduledJobDaysOfMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ScheduledJobDaysOfMonth.setStatus("mandatory")
_Win32ScheduledJobJobStatus_Type = String
_Win32ScheduledJobJobStatus_Object = MibTableColumn
win32ScheduledJobJobStatus = _Win32ScheduledJobJobStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 450, 1, 9),
    _Win32ScheduledJobJobStatus_Type()
)
win32ScheduledJobJobStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ScheduledJobJobStatus.setStatus("mandatory")
_Win32ScheduledJobStatus_Type = String
_Win32ScheduledJobStatus_Object = MibTableColumn
win32ScheduledJobStatus = _Win32ScheduledJobStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 450, 1, 10),
    _Win32ScheduledJobStatus_Type()
)
win32ScheduledJobStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ScheduledJobStatus.setStatus("mandatory")
_Win32BIOSTable_Object = MibTable
win32BIOSTable = _Win32BIOSTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 460)
)
if mibBuilder.loadTexts:
    win32BIOSTable.setStatus("mandatory")
_Win32BIOSEntry_Object = MibTableRow
win32BIOSEntry = _Win32BIOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 460, 1)
)
win32BIOSEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32BIOSKeyIndex"),
)
if mibBuilder.loadTexts:
    win32BIOSEntry.setStatus("mandatory")
_Win32BIOSKeyIndex_Type = String
_Win32BIOSKeyIndex_Object = MibTableColumn
win32BIOSKeyIndex = _Win32BIOSKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 460, 1, 1),
    _Win32BIOSKeyIndex_Type()
)
win32BIOSKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BIOSKeyIndex.setStatus("mandatory")
_Win32BIOSReleaseDate_Type = Datetime
_Win32BIOSReleaseDate_Object = MibTableColumn
win32BIOSReleaseDate = _Win32BIOSReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 460, 1, 2),
    _Win32BIOSReleaseDate_Type()
)
win32BIOSReleaseDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BIOSReleaseDate.setStatus("mandatory")
_Win32BIOSVersion_Type = String
_Win32BIOSVersion_Object = MibTableColumn
win32BIOSVersion = _Win32BIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 460, 1, 3),
    _Win32BIOSVersion_Type()
)
win32BIOSVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BIOSVersion.setStatus("mandatory")
_Win32BIOSStatus_Type = String
_Win32BIOSStatus_Object = MibTableColumn
win32BIOSStatus = _Win32BIOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 460, 1, 4),
    _Win32BIOSStatus_Type()
)
win32BIOSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BIOSStatus.setStatus("mandatory")
_Win32BootConfigurationTable_Object = MibTable
win32BootConfigurationTable = _Win32BootConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 470)
)
if mibBuilder.loadTexts:
    win32BootConfigurationTable.setStatus("mandatory")
_Win32BootConfigurationEntry_Object = MibTableRow
win32BootConfigurationEntry = _Win32BootConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 470, 1)
)
win32BootConfigurationEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32BootConfigurationKeyIndex"),
)
if mibBuilder.loadTexts:
    win32BootConfigurationEntry.setStatus("mandatory")
_Win32BootConfigurationKeyIndex_Type = String
_Win32BootConfigurationKeyIndex_Object = MibTableColumn
win32BootConfigurationKeyIndex = _Win32BootConfigurationKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 470, 1, 1),
    _Win32BootConfigurationKeyIndex_Type()
)
win32BootConfigurationKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BootConfigurationKeyIndex.setStatus("mandatory")
_Win32BootConfigurationBootDirectory_Type = String
_Win32BootConfigurationBootDirectory_Object = MibTableColumn
win32BootConfigurationBootDirectory = _Win32BootConfigurationBootDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 470, 1, 2),
    _Win32BootConfigurationBootDirectory_Type()
)
win32BootConfigurationBootDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BootConfigurationBootDirectory.setStatus("mandatory")
_Win32BootConfigurationConfigurationPath_Type = String
_Win32BootConfigurationConfigurationPath_Object = MibTableColumn
win32BootConfigurationConfigurationPath = _Win32BootConfigurationConfigurationPath_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 470, 1, 3),
    _Win32BootConfigurationConfigurationPath_Type()
)
win32BootConfigurationConfigurationPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BootConfigurationConfigurationPath.setStatus("mandatory")
_Win32BootConfigurationLastDrive_Type = String
_Win32BootConfigurationLastDrive_Object = MibTableColumn
win32BootConfigurationLastDrive = _Win32BootConfigurationLastDrive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 470, 1, 4),
    _Win32BootConfigurationLastDrive_Type()
)
win32BootConfigurationLastDrive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BootConfigurationLastDrive.setStatus("mandatory")
_Win32BootConfigurationName_Type = String
_Win32BootConfigurationName_Object = MibTableColumn
win32BootConfigurationName = _Win32BootConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 470, 1, 5),
    _Win32BootConfigurationName_Type()
)
win32BootConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BootConfigurationName.setStatus("mandatory")
_Win32BootConfigurationScratchDirectory_Type = String
_Win32BootConfigurationScratchDirectory_Object = MibTableColumn
win32BootConfigurationScratchDirectory = _Win32BootConfigurationScratchDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 470, 1, 6),
    _Win32BootConfigurationScratchDirectory_Type()
)
win32BootConfigurationScratchDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BootConfigurationScratchDirectory.setStatus("mandatory")
_Win32BootConfigurationTempDirectory_Type = String
_Win32BootConfigurationTempDirectory_Object = MibTableColumn
win32BootConfigurationTempDirectory = _Win32BootConfigurationTempDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 470, 1, 7),
    _Win32BootConfigurationTempDirectory_Type()
)
win32BootConfigurationTempDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32BootConfigurationTempDirectory.setStatus("mandatory")
_Win32DesktopTable_Object = MibTable
win32DesktopTable = _Win32DesktopTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480)
)
if mibBuilder.loadTexts:
    win32DesktopTable.setStatus("mandatory")
_Win32DesktopEntry_Object = MibTableRow
win32DesktopEntry = _Win32DesktopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1)
)
win32DesktopEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32DesktopKeyIndex"),
)
if mibBuilder.loadTexts:
    win32DesktopEntry.setStatus("mandatory")
_Win32DesktopKeyIndex_Type = String
_Win32DesktopKeyIndex_Object = MibTableColumn
win32DesktopKeyIndex = _Win32DesktopKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 1),
    _Win32DesktopKeyIndex_Type()
)
win32DesktopKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopKeyIndex.setStatus("mandatory")
_Win32DesktopBorderWidth_Type = Uint32
_Win32DesktopBorderWidth_Object = MibTableColumn
win32DesktopBorderWidth = _Win32DesktopBorderWidth_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 2),
    _Win32DesktopBorderWidth_Type()
)
win32DesktopBorderWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopBorderWidth.setStatus("mandatory")
_Win32DesktopCoolSwitch_Type = Boolean
_Win32DesktopCoolSwitch_Object = MibTableColumn
win32DesktopCoolSwitch = _Win32DesktopCoolSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 3),
    _Win32DesktopCoolSwitch_Type()
)
win32DesktopCoolSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopCoolSwitch.setStatus("mandatory")
_Win32DesktopCursorBlinkRate_Type = Uint32
_Win32DesktopCursorBlinkRate_Object = MibTableColumn
win32DesktopCursorBlinkRate = _Win32DesktopCursorBlinkRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 4),
    _Win32DesktopCursorBlinkRate_Type()
)
win32DesktopCursorBlinkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopCursorBlinkRate.setStatus("mandatory")
_Win32DesktopDragFullWindows_Type = Boolean
_Win32DesktopDragFullWindows_Object = MibTableColumn
win32DesktopDragFullWindows = _Win32DesktopDragFullWindows_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 5),
    _Win32DesktopDragFullWindows_Type()
)
win32DesktopDragFullWindows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopDragFullWindows.setStatus("mandatory")
_Win32DesktopGridGranularity_Type = Uint32
_Win32DesktopGridGranularity_Object = MibTableColumn
win32DesktopGridGranularity = _Win32DesktopGridGranularity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 6),
    _Win32DesktopGridGranularity_Type()
)
win32DesktopGridGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopGridGranularity.setStatus("mandatory")
_Win32DesktopIconSpacing_Type = Uint32
_Win32DesktopIconSpacing_Object = MibTableColumn
win32DesktopIconSpacing = _Win32DesktopIconSpacing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 7),
    _Win32DesktopIconSpacing_Type()
)
win32DesktopIconSpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopIconSpacing.setStatus("mandatory")
_Win32DesktopIconTitleFaceName_Type = String
_Win32DesktopIconTitleFaceName_Object = MibTableColumn
win32DesktopIconTitleFaceName = _Win32DesktopIconTitleFaceName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 8),
    _Win32DesktopIconTitleFaceName_Type()
)
win32DesktopIconTitleFaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopIconTitleFaceName.setStatus("mandatory")
_Win32DesktopIconTitleSize_Type = Uint32
_Win32DesktopIconTitleSize_Object = MibTableColumn
win32DesktopIconTitleSize = _Win32DesktopIconTitleSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 9),
    _Win32DesktopIconTitleSize_Type()
)
win32DesktopIconTitleSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopIconTitleSize.setStatus("mandatory")
_Win32DesktopIconTitleWrap_Type = Boolean
_Win32DesktopIconTitleWrap_Object = MibTableColumn
win32DesktopIconTitleWrap = _Win32DesktopIconTitleWrap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 10),
    _Win32DesktopIconTitleWrap_Type()
)
win32DesktopIconTitleWrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopIconTitleWrap.setStatus("mandatory")
_Win32DesktopName_Type = String
_Win32DesktopName_Object = MibTableColumn
win32DesktopName = _Win32DesktopName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 11),
    _Win32DesktopName_Type()
)
win32DesktopName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopName.setStatus("mandatory")
_Win32DesktopPattern_Type = String
_Win32DesktopPattern_Object = MibTableColumn
win32DesktopPattern = _Win32DesktopPattern_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 12),
    _Win32DesktopPattern_Type()
)
win32DesktopPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopPattern.setStatus("mandatory")
_Win32DesktopScreenSaverActive_Type = Boolean
_Win32DesktopScreenSaverActive_Object = MibTableColumn
win32DesktopScreenSaverActive = _Win32DesktopScreenSaverActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 13),
    _Win32DesktopScreenSaverActive_Type()
)
win32DesktopScreenSaverActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopScreenSaverActive.setStatus("mandatory")
_Win32DesktopScreenSaverExecutable_Type = String
_Win32DesktopScreenSaverExecutable_Object = MibTableColumn
win32DesktopScreenSaverExecutable = _Win32DesktopScreenSaverExecutable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 14),
    _Win32DesktopScreenSaverExecutable_Type()
)
win32DesktopScreenSaverExecutable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopScreenSaverExecutable.setStatus("mandatory")
_Win32DesktopScreenSaverSecure_Type = Boolean
_Win32DesktopScreenSaverSecure_Object = MibTableColumn
win32DesktopScreenSaverSecure = _Win32DesktopScreenSaverSecure_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 15),
    _Win32DesktopScreenSaverSecure_Type()
)
win32DesktopScreenSaverSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopScreenSaverSecure.setStatus("mandatory")
_Win32DesktopScreenSaverTimeout_Type = Uint32
_Win32DesktopScreenSaverTimeout_Object = MibTableColumn
win32DesktopScreenSaverTimeout = _Win32DesktopScreenSaverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 16),
    _Win32DesktopScreenSaverTimeout_Type()
)
win32DesktopScreenSaverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopScreenSaverTimeout.setStatus("mandatory")
_Win32DesktopWallpaper_Type = String
_Win32DesktopWallpaper_Object = MibTableColumn
win32DesktopWallpaper = _Win32DesktopWallpaper_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 17),
    _Win32DesktopWallpaper_Type()
)
win32DesktopWallpaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopWallpaper.setStatus("mandatory")
_Win32DesktopWallpaperTiled_Type = Boolean
_Win32DesktopWallpaperTiled_Object = MibTableColumn
win32DesktopWallpaperTiled = _Win32DesktopWallpaperTiled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 18),
    _Win32DesktopWallpaperTiled_Type()
)
win32DesktopWallpaperTiled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopWallpaperTiled.setStatus("mandatory")
_Win32DesktopWallpaperStretched_Type = Boolean
_Win32DesktopWallpaperStretched_Object = MibTableColumn
win32DesktopWallpaperStretched = _Win32DesktopWallpaperStretched_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 480, 1, 19),
    _Win32DesktopWallpaperStretched_Type()
)
win32DesktopWallpaperStretched.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DesktopWallpaperStretched.setStatus("mandatory")
_Win32DisplayConfigurationTable_Object = MibTable
win32DisplayConfigurationTable = _Win32DisplayConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490)
)
if mibBuilder.loadTexts:
    win32DisplayConfigurationTable.setStatus("mandatory")
_Win32DisplayConfigurationEntry_Object = MibTableRow
win32DisplayConfigurationEntry = _Win32DisplayConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490, 1)
)
win32DisplayConfigurationEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32DisplayConfigurationKeyIndex"),
)
if mibBuilder.loadTexts:
    win32DisplayConfigurationEntry.setStatus("mandatory")
_Win32DisplayConfigurationKeyIndex_Type = String
_Win32DisplayConfigurationKeyIndex_Object = MibTableColumn
win32DisplayConfigurationKeyIndex = _Win32DisplayConfigurationKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490, 1, 1),
    _Win32DisplayConfigurationKeyIndex_Type()
)
win32DisplayConfigurationKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayConfigurationKeyIndex.setStatus("mandatory")
_Win32DisplayConfigurationBitsPerPel_Type = Uint32
_Win32DisplayConfigurationBitsPerPel_Object = MibTableColumn
win32DisplayConfigurationBitsPerPel = _Win32DisplayConfigurationBitsPerPel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490, 1, 2),
    _Win32DisplayConfigurationBitsPerPel_Type()
)
win32DisplayConfigurationBitsPerPel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayConfigurationBitsPerPel.setStatus("mandatory")
_Win32DisplayConfigurationDeviceName_Type = String
_Win32DisplayConfigurationDeviceName_Object = MibTableColumn
win32DisplayConfigurationDeviceName = _Win32DisplayConfigurationDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490, 1, 3),
    _Win32DisplayConfigurationDeviceName_Type()
)
win32DisplayConfigurationDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayConfigurationDeviceName.setStatus("mandatory")
_Win32DisplayConfigurationDisplayFlags_Type = Uint32
_Win32DisplayConfigurationDisplayFlags_Object = MibTableColumn
win32DisplayConfigurationDisplayFlags = _Win32DisplayConfigurationDisplayFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490, 1, 4),
    _Win32DisplayConfigurationDisplayFlags_Type()
)
win32DisplayConfigurationDisplayFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayConfigurationDisplayFlags.setStatus("mandatory")
_Win32DisplayConfigurationDisplayFrequency_Type = Uint32
_Win32DisplayConfigurationDisplayFrequency_Object = MibTableColumn
win32DisplayConfigurationDisplayFrequency = _Win32DisplayConfigurationDisplayFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490, 1, 5),
    _Win32DisplayConfigurationDisplayFrequency_Type()
)
win32DisplayConfigurationDisplayFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayConfigurationDisplayFrequency.setStatus("mandatory")
_Win32DisplayConfigurationDitherType_Type = Uint32
_Win32DisplayConfigurationDitherType_Object = MibTableColumn
win32DisplayConfigurationDitherType = _Win32DisplayConfigurationDitherType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490, 1, 6),
    _Win32DisplayConfigurationDitherType_Type()
)
win32DisplayConfigurationDitherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayConfigurationDitherType.setStatus("mandatory")
_Win32DisplayConfigurationDriverVersion_Type = String
_Win32DisplayConfigurationDriverVersion_Object = MibTableColumn
win32DisplayConfigurationDriverVersion = _Win32DisplayConfigurationDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490, 1, 7),
    _Win32DisplayConfigurationDriverVersion_Type()
)
win32DisplayConfigurationDriverVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayConfigurationDriverVersion.setStatus("mandatory")
_Win32DisplayConfigurationICMIntent_Type = Uint32
_Win32DisplayConfigurationICMIntent_Object = MibTableColumn
win32DisplayConfigurationICMIntent = _Win32DisplayConfigurationICMIntent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490, 1, 8),
    _Win32DisplayConfigurationICMIntent_Type()
)
win32DisplayConfigurationICMIntent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayConfigurationICMIntent.setStatus("mandatory")
_Win32DisplayConfigurationICMMethod_Type = Uint32
_Win32DisplayConfigurationICMMethod_Object = MibTableColumn
win32DisplayConfigurationICMMethod = _Win32DisplayConfigurationICMMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490, 1, 9),
    _Win32DisplayConfigurationICMMethod_Type()
)
win32DisplayConfigurationICMMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayConfigurationICMMethod.setStatus("mandatory")
_Win32DisplayConfigurationLogPixels_Type = Uint32
_Win32DisplayConfigurationLogPixels_Object = MibTableColumn
win32DisplayConfigurationLogPixels = _Win32DisplayConfigurationLogPixels_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490, 1, 10),
    _Win32DisplayConfigurationLogPixels_Type()
)
win32DisplayConfigurationLogPixels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayConfigurationLogPixels.setStatus("mandatory")
_Win32DisplayConfigurationPelsHeight_Type = Uint32
_Win32DisplayConfigurationPelsHeight_Object = MibTableColumn
win32DisplayConfigurationPelsHeight = _Win32DisplayConfigurationPelsHeight_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490, 1, 11),
    _Win32DisplayConfigurationPelsHeight_Type()
)
win32DisplayConfigurationPelsHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayConfigurationPelsHeight.setStatus("mandatory")
_Win32DisplayConfigurationPelsWidth_Type = Uint32
_Win32DisplayConfigurationPelsWidth_Object = MibTableColumn
win32DisplayConfigurationPelsWidth = _Win32DisplayConfigurationPelsWidth_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490, 1, 12),
    _Win32DisplayConfigurationPelsWidth_Type()
)
win32DisplayConfigurationPelsWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayConfigurationPelsWidth.setStatus("mandatory")
_Win32DisplayConfigurationSpecificationVersion_Type = Uint32
_Win32DisplayConfigurationSpecificationVersion_Object = MibTableColumn
win32DisplayConfigurationSpecificationVersion = _Win32DisplayConfigurationSpecificationVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 490, 1, 13),
    _Win32DisplayConfigurationSpecificationVersion_Type()
)
win32DisplayConfigurationSpecificationVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayConfigurationSpecificationVersion.setStatus("mandatory")
_Win32DisplayControllerConfigurationTable_Object = MibTable
win32DisplayControllerConfigurationTable = _Win32DisplayControllerConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 500)
)
if mibBuilder.loadTexts:
    win32DisplayControllerConfigurationTable.setStatus("mandatory")
_Win32DisplayControllerConfigurationEntry_Object = MibTableRow
win32DisplayControllerConfigurationEntry = _Win32DisplayControllerConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 500, 1)
)
win32DisplayControllerConfigurationEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32DisplayControllerConfigurationKeyIndex"),
)
if mibBuilder.loadTexts:
    win32DisplayControllerConfigurationEntry.setStatus("mandatory")
_Win32DisplayControllerConfigurationKeyIndex_Type = String
_Win32DisplayControllerConfigurationKeyIndex_Object = MibTableColumn
win32DisplayControllerConfigurationKeyIndex = _Win32DisplayControllerConfigurationKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 500, 1, 1),
    _Win32DisplayControllerConfigurationKeyIndex_Type()
)
win32DisplayControllerConfigurationKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayControllerConfigurationKeyIndex.setStatus("mandatory")
_Win32DisplayControllerConfigurationBitsPerPixel_Type = Uint32
_Win32DisplayControllerConfigurationBitsPerPixel_Object = MibTableColumn
win32DisplayControllerConfigurationBitsPerPixel = _Win32DisplayControllerConfigurationBitsPerPixel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 500, 1, 2),
    _Win32DisplayControllerConfigurationBitsPerPixel_Type()
)
win32DisplayControllerConfigurationBitsPerPixel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayControllerConfigurationBitsPerPixel.setStatus("mandatory")
_Win32DisplayControllerConfigurationColorPlanes_Type = Uint32
_Win32DisplayControllerConfigurationColorPlanes_Object = MibTableColumn
win32DisplayControllerConfigurationColorPlanes = _Win32DisplayControllerConfigurationColorPlanes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 500, 1, 3),
    _Win32DisplayControllerConfigurationColorPlanes_Type()
)
win32DisplayControllerConfigurationColorPlanes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayControllerConfigurationColorPlanes.setStatus("mandatory")
_Win32DisplayControllerConfigurationDeviceEntriesInAColorTable_Type = Uint32
_Win32DisplayControllerConfigurationDeviceEntriesInAColorTable_Object = MibTableColumn
win32DisplayControllerConfigurationDeviceEntriesInAColorTable = _Win32DisplayControllerConfigurationDeviceEntriesInAColorTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 500, 1, 4),
    _Win32DisplayControllerConfigurationDeviceEntriesInAColorTable_Type()
)
win32DisplayControllerConfigurationDeviceEntriesInAColorTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayControllerConfigurationDeviceEntriesInAColorTable.setStatus("mandatory")
_Win32DisplayControllerConfigurationDeviceSpecificPens_Type = Uint32
_Win32DisplayControllerConfigurationDeviceSpecificPens_Object = MibTableColumn
win32DisplayControllerConfigurationDeviceSpecificPens = _Win32DisplayControllerConfigurationDeviceSpecificPens_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 500, 1, 5),
    _Win32DisplayControllerConfigurationDeviceSpecificPens_Type()
)
win32DisplayControllerConfigurationDeviceSpecificPens.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayControllerConfigurationDeviceSpecificPens.setStatus("mandatory")
_Win32DisplayControllerConfigurationHorizontalResolution_Type = Uint32
_Win32DisplayControllerConfigurationHorizontalResolution_Object = MibTableColumn
win32DisplayControllerConfigurationHorizontalResolution = _Win32DisplayControllerConfigurationHorizontalResolution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 500, 1, 6),
    _Win32DisplayControllerConfigurationHorizontalResolution_Type()
)
win32DisplayControllerConfigurationHorizontalResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayControllerConfigurationHorizontalResolution.setStatus("mandatory")
_Win32DisplayControllerConfigurationName_Type = String
_Win32DisplayControllerConfigurationName_Object = MibTableColumn
win32DisplayControllerConfigurationName = _Win32DisplayControllerConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 500, 1, 7),
    _Win32DisplayControllerConfigurationName_Type()
)
win32DisplayControllerConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayControllerConfigurationName.setStatus("mandatory")
_Win32DisplayControllerConfigurationRefreshRate_Type = Sint32
_Win32DisplayControllerConfigurationRefreshRate_Object = MibTableColumn
win32DisplayControllerConfigurationRefreshRate = _Win32DisplayControllerConfigurationRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 500, 1, 8),
    _Win32DisplayControllerConfigurationRefreshRate_Type()
)
win32DisplayControllerConfigurationRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayControllerConfigurationRefreshRate.setStatus("mandatory")
_Win32DisplayControllerConfigurationReservedSystemPaletteEntries_Type = Uint32
_Win32DisplayControllerConfigurationReservedSystemPaletteEntries_Object = MibTableColumn
win32DisplayControllerConfigurationReservedSystemPaletteEntries = _Win32DisplayControllerConfigurationReservedSystemPaletteEntries_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 500, 1, 9),
    _Win32DisplayControllerConfigurationReservedSystemPaletteEntries_Type()
)
win32DisplayControllerConfigurationReservedSystemPaletteEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayControllerConfigurationReservedSystemPaletteEntries.setStatus("mandatory")
_Win32DisplayControllerConfigurationSystemPaletteEntries_Type = Uint32
_Win32DisplayControllerConfigurationSystemPaletteEntries_Object = MibTableColumn
win32DisplayControllerConfigurationSystemPaletteEntries = _Win32DisplayControllerConfigurationSystemPaletteEntries_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 500, 1, 10),
    _Win32DisplayControllerConfigurationSystemPaletteEntries_Type()
)
win32DisplayControllerConfigurationSystemPaletteEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayControllerConfigurationSystemPaletteEntries.setStatus("mandatory")
_Win32DisplayControllerConfigurationVerticalResolution_Type = Uint32
_Win32DisplayControllerConfigurationVerticalResolution_Object = MibTableColumn
win32DisplayControllerConfigurationVerticalResolution = _Win32DisplayControllerConfigurationVerticalResolution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 500, 1, 11),
    _Win32DisplayControllerConfigurationVerticalResolution_Type()
)
win32DisplayControllerConfigurationVerticalResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayControllerConfigurationVerticalResolution.setStatus("mandatory")
_Win32DisplayControllerConfigurationVideoMode_Type = String
_Win32DisplayControllerConfigurationVideoMode_Object = MibTableColumn
win32DisplayControllerConfigurationVideoMode = _Win32DisplayControllerConfigurationVideoMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 500, 1, 12),
    _Win32DisplayControllerConfigurationVideoMode_Type()
)
win32DisplayControllerConfigurationVideoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DisplayControllerConfigurationVideoMode.setStatus("mandatory")
_Win32LogicalMemoryConfigurationTable_Object = MibTable
win32LogicalMemoryConfigurationTable = _Win32LogicalMemoryConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 510)
)
if mibBuilder.loadTexts:
    win32LogicalMemoryConfigurationTable.setStatus("mandatory")
_Win32LogicalMemoryConfigurationEntry_Object = MibTableRow
win32LogicalMemoryConfigurationEntry = _Win32LogicalMemoryConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 510, 1)
)
win32LogicalMemoryConfigurationEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32LogicalMemoryConfigurationKeyIndex"),
)
if mibBuilder.loadTexts:
    win32LogicalMemoryConfigurationEntry.setStatus("mandatory")
_Win32LogicalMemoryConfigurationKeyIndex_Type = String
_Win32LogicalMemoryConfigurationKeyIndex_Object = MibTableColumn
win32LogicalMemoryConfigurationKeyIndex = _Win32LogicalMemoryConfigurationKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 510, 1, 1),
    _Win32LogicalMemoryConfigurationKeyIndex_Type()
)
win32LogicalMemoryConfigurationKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalMemoryConfigurationKeyIndex.setStatus("mandatory")
_Win32LogicalMemoryConfigurationAvailableVirtualMemory_Type = Uint32
_Win32LogicalMemoryConfigurationAvailableVirtualMemory_Object = MibTableColumn
win32LogicalMemoryConfigurationAvailableVirtualMemory = _Win32LogicalMemoryConfigurationAvailableVirtualMemory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 510, 1, 2),
    _Win32LogicalMemoryConfigurationAvailableVirtualMemory_Type()
)
win32LogicalMemoryConfigurationAvailableVirtualMemory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalMemoryConfigurationAvailableVirtualMemory.setStatus("mandatory")
_Win32LogicalMemoryConfigurationName_Type = String
_Win32LogicalMemoryConfigurationName_Object = MibTableColumn
win32LogicalMemoryConfigurationName = _Win32LogicalMemoryConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 510, 1, 3),
    _Win32LogicalMemoryConfigurationName_Type()
)
win32LogicalMemoryConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalMemoryConfigurationName.setStatus("mandatory")
_Win32LogicalMemoryConfigurationTotalPageFileSpace_Type = Uint32
_Win32LogicalMemoryConfigurationTotalPageFileSpace_Object = MibTableColumn
win32LogicalMemoryConfigurationTotalPageFileSpace = _Win32LogicalMemoryConfigurationTotalPageFileSpace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 510, 1, 4),
    _Win32LogicalMemoryConfigurationTotalPageFileSpace_Type()
)
win32LogicalMemoryConfigurationTotalPageFileSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalMemoryConfigurationTotalPageFileSpace.setStatus("mandatory")
_Win32LogicalMemoryConfigurationTotalPhysicalMemory_Type = Uint32
_Win32LogicalMemoryConfigurationTotalPhysicalMemory_Object = MibTableColumn
win32LogicalMemoryConfigurationTotalPhysicalMemory = _Win32LogicalMemoryConfigurationTotalPhysicalMemory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 510, 1, 5),
    _Win32LogicalMemoryConfigurationTotalPhysicalMemory_Type()
)
win32LogicalMemoryConfigurationTotalPhysicalMemory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalMemoryConfigurationTotalPhysicalMemory.setStatus("mandatory")
_Win32LogicalMemoryConfigurationTotalVirtualMemory_Type = Uint32
_Win32LogicalMemoryConfigurationTotalVirtualMemory_Object = MibTableColumn
win32LogicalMemoryConfigurationTotalVirtualMemory = _Win32LogicalMemoryConfigurationTotalVirtualMemory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 510, 1, 6),
    _Win32LogicalMemoryConfigurationTotalVirtualMemory_Type()
)
win32LogicalMemoryConfigurationTotalVirtualMemory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalMemoryConfigurationTotalVirtualMemory.setStatus("mandatory")
_Win32NetworkLoginProfileTable_Object = MibTable
win32NetworkLoginProfileTable = _Win32NetworkLoginProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520)
)
if mibBuilder.loadTexts:
    win32NetworkLoginProfileTable.setStatus("mandatory")
_Win32NetworkLoginProfileEntry_Object = MibTableRow
win32NetworkLoginProfileEntry = _Win32NetworkLoginProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1)
)
win32NetworkLoginProfileEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32NetworkLoginProfileKeyIndex"),
)
if mibBuilder.loadTexts:
    win32NetworkLoginProfileEntry.setStatus("mandatory")
_Win32NetworkLoginProfileKeyIndex_Type = String
_Win32NetworkLoginProfileKeyIndex_Object = MibTableColumn
win32NetworkLoginProfileKeyIndex = _Win32NetworkLoginProfileKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 1),
    _Win32NetworkLoginProfileKeyIndex_Type()
)
win32NetworkLoginProfileKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileKeyIndex.setStatus("mandatory")
_Win32NetworkLoginProfileAccountExpires_Type = Datetime
_Win32NetworkLoginProfileAccountExpires_Object = MibTableColumn
win32NetworkLoginProfileAccountExpires = _Win32NetworkLoginProfileAccountExpires_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 2),
    _Win32NetworkLoginProfileAccountExpires_Type()
)
win32NetworkLoginProfileAccountExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileAccountExpires.setStatus("mandatory")
_Win32NetworkLoginProfileAuthorizationFlags_Type = Uint32
_Win32NetworkLoginProfileAuthorizationFlags_Object = MibTableColumn
win32NetworkLoginProfileAuthorizationFlags = _Win32NetworkLoginProfileAuthorizationFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 3),
    _Win32NetworkLoginProfileAuthorizationFlags_Type()
)
win32NetworkLoginProfileAuthorizationFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileAuthorizationFlags.setStatus("mandatory")
_Win32NetworkLoginProfileBadPasswordCount_Type = Uint32
_Win32NetworkLoginProfileBadPasswordCount_Object = MibTableColumn
win32NetworkLoginProfileBadPasswordCount = _Win32NetworkLoginProfileBadPasswordCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 4),
    _Win32NetworkLoginProfileBadPasswordCount_Type()
)
win32NetworkLoginProfileBadPasswordCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileBadPasswordCount.setStatus("mandatory")
_Win32NetworkLoginProfileCodePage_Type = Uint32
_Win32NetworkLoginProfileCodePage_Object = MibTableColumn
win32NetworkLoginProfileCodePage = _Win32NetworkLoginProfileCodePage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 5),
    _Win32NetworkLoginProfileCodePage_Type()
)
win32NetworkLoginProfileCodePage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileCodePage.setStatus("mandatory")
_Win32NetworkLoginProfileComment_Type = String
_Win32NetworkLoginProfileComment_Object = MibTableColumn
win32NetworkLoginProfileComment = _Win32NetworkLoginProfileComment_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 6),
    _Win32NetworkLoginProfileComment_Type()
)
win32NetworkLoginProfileComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileComment.setStatus("mandatory")
_Win32NetworkLoginProfileCountryCode_Type = Uint32
_Win32NetworkLoginProfileCountryCode_Object = MibTableColumn
win32NetworkLoginProfileCountryCode = _Win32NetworkLoginProfileCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 7),
    _Win32NetworkLoginProfileCountryCode_Type()
)
win32NetworkLoginProfileCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileCountryCode.setStatus("mandatory")
_Win32NetworkLoginProfileFlags_Type = Uint32
_Win32NetworkLoginProfileFlags_Object = MibTableColumn
win32NetworkLoginProfileFlags = _Win32NetworkLoginProfileFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 8),
    _Win32NetworkLoginProfileFlags_Type()
)
win32NetworkLoginProfileFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileFlags.setStatus("mandatory")
_Win32NetworkLoginProfileFullName_Type = String
_Win32NetworkLoginProfileFullName_Object = MibTableColumn
win32NetworkLoginProfileFullName = _Win32NetworkLoginProfileFullName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 9),
    _Win32NetworkLoginProfileFullName_Type()
)
win32NetworkLoginProfileFullName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileFullName.setStatus("mandatory")
_Win32NetworkLoginProfileHomeDirectory_Type = String
_Win32NetworkLoginProfileHomeDirectory_Object = MibTableColumn
win32NetworkLoginProfileHomeDirectory = _Win32NetworkLoginProfileHomeDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 10),
    _Win32NetworkLoginProfileHomeDirectory_Type()
)
win32NetworkLoginProfileHomeDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileHomeDirectory.setStatus("mandatory")
_Win32NetworkLoginProfileHomeDirectoryDrive_Type = String
_Win32NetworkLoginProfileHomeDirectoryDrive_Object = MibTableColumn
win32NetworkLoginProfileHomeDirectoryDrive = _Win32NetworkLoginProfileHomeDirectoryDrive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 11),
    _Win32NetworkLoginProfileHomeDirectoryDrive_Type()
)
win32NetworkLoginProfileHomeDirectoryDrive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileHomeDirectoryDrive.setStatus("mandatory")
_Win32NetworkLoginProfileLastLogoff_Type = Datetime
_Win32NetworkLoginProfileLastLogoff_Object = MibTableColumn
win32NetworkLoginProfileLastLogoff = _Win32NetworkLoginProfileLastLogoff_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 12),
    _Win32NetworkLoginProfileLastLogoff_Type()
)
win32NetworkLoginProfileLastLogoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileLastLogoff.setStatus("mandatory")
_Win32NetworkLoginProfileLastLogon_Type = Datetime
_Win32NetworkLoginProfileLastLogon_Object = MibTableColumn
win32NetworkLoginProfileLastLogon = _Win32NetworkLoginProfileLastLogon_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 13),
    _Win32NetworkLoginProfileLastLogon_Type()
)
win32NetworkLoginProfileLastLogon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileLastLogon.setStatus("mandatory")
_Win32NetworkLoginProfileLogonHours_Type = String
_Win32NetworkLoginProfileLogonHours_Object = MibTableColumn
win32NetworkLoginProfileLogonHours = _Win32NetworkLoginProfileLogonHours_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 14),
    _Win32NetworkLoginProfileLogonHours_Type()
)
win32NetworkLoginProfileLogonHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileLogonHours.setStatus("mandatory")
_Win32NetworkLoginProfileLogonServer_Type = String
_Win32NetworkLoginProfileLogonServer_Object = MibTableColumn
win32NetworkLoginProfileLogonServer = _Win32NetworkLoginProfileLogonServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 15),
    _Win32NetworkLoginProfileLogonServer_Type()
)
win32NetworkLoginProfileLogonServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileLogonServer.setStatus("mandatory")
_Win32NetworkLoginProfileMaximumStorage_Type = String
_Win32NetworkLoginProfileMaximumStorage_Object = MibTableColumn
win32NetworkLoginProfileMaximumStorage = _Win32NetworkLoginProfileMaximumStorage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 16),
    _Win32NetworkLoginProfileMaximumStorage_Type()
)
win32NetworkLoginProfileMaximumStorage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileMaximumStorage.setStatus("mandatory")
_Win32NetworkLoginProfileName_Type = String
_Win32NetworkLoginProfileName_Object = MibTableColumn
win32NetworkLoginProfileName = _Win32NetworkLoginProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 17),
    _Win32NetworkLoginProfileName_Type()
)
win32NetworkLoginProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileName.setStatus("mandatory")
_Win32NetworkLoginProfileNumberOfLogons_Type = Uint32
_Win32NetworkLoginProfileNumberOfLogons_Object = MibTableColumn
win32NetworkLoginProfileNumberOfLogons = _Win32NetworkLoginProfileNumberOfLogons_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 18),
    _Win32NetworkLoginProfileNumberOfLogons_Type()
)
win32NetworkLoginProfileNumberOfLogons.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileNumberOfLogons.setStatus("mandatory")
_Win32NetworkLoginProfileParameters_Type = String
_Win32NetworkLoginProfileParameters_Object = MibTableColumn
win32NetworkLoginProfileParameters = _Win32NetworkLoginProfileParameters_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 19),
    _Win32NetworkLoginProfileParameters_Type()
)
win32NetworkLoginProfileParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileParameters.setStatus("mandatory")
_Win32NetworkLoginProfilePasswordAge_Type = Datetime
_Win32NetworkLoginProfilePasswordAge_Object = MibTableColumn
win32NetworkLoginProfilePasswordAge = _Win32NetworkLoginProfilePasswordAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 20),
    _Win32NetworkLoginProfilePasswordAge_Type()
)
win32NetworkLoginProfilePasswordAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfilePasswordAge.setStatus("mandatory")
_Win32NetworkLoginProfilePasswordExpires_Type = Datetime
_Win32NetworkLoginProfilePasswordExpires_Object = MibTableColumn
win32NetworkLoginProfilePasswordExpires = _Win32NetworkLoginProfilePasswordExpires_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 21),
    _Win32NetworkLoginProfilePasswordExpires_Type()
)
win32NetworkLoginProfilePasswordExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfilePasswordExpires.setStatus("mandatory")
_Win32NetworkLoginProfilePrimaryGroupId_Type = Uint32
_Win32NetworkLoginProfilePrimaryGroupId_Object = MibTableColumn
win32NetworkLoginProfilePrimaryGroupId = _Win32NetworkLoginProfilePrimaryGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 22),
    _Win32NetworkLoginProfilePrimaryGroupId_Type()
)
win32NetworkLoginProfilePrimaryGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfilePrimaryGroupId.setStatus("mandatory")
_Win32NetworkLoginProfilePrivileges_Type = Uint32
_Win32NetworkLoginProfilePrivileges_Object = MibTableColumn
win32NetworkLoginProfilePrivileges = _Win32NetworkLoginProfilePrivileges_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 23),
    _Win32NetworkLoginProfilePrivileges_Type()
)
win32NetworkLoginProfilePrivileges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfilePrivileges.setStatus("mandatory")
_Win32NetworkLoginProfileProfile_Type = String
_Win32NetworkLoginProfileProfile_Object = MibTableColumn
win32NetworkLoginProfileProfile = _Win32NetworkLoginProfileProfile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 24),
    _Win32NetworkLoginProfileProfile_Type()
)
win32NetworkLoginProfileProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileProfile.setStatus("mandatory")
_Win32NetworkLoginProfileScriptPath_Type = String
_Win32NetworkLoginProfileScriptPath_Object = MibTableColumn
win32NetworkLoginProfileScriptPath = _Win32NetworkLoginProfileScriptPath_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 25),
    _Win32NetworkLoginProfileScriptPath_Type()
)
win32NetworkLoginProfileScriptPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileScriptPath.setStatus("mandatory")
_Win32NetworkLoginProfileUnitsPerWeek_Type = Uint32
_Win32NetworkLoginProfileUnitsPerWeek_Object = MibTableColumn
win32NetworkLoginProfileUnitsPerWeek = _Win32NetworkLoginProfileUnitsPerWeek_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 26),
    _Win32NetworkLoginProfileUnitsPerWeek_Type()
)
win32NetworkLoginProfileUnitsPerWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileUnitsPerWeek.setStatus("mandatory")
_Win32NetworkLoginProfileUserComment_Type = String
_Win32NetworkLoginProfileUserComment_Object = MibTableColumn
win32NetworkLoginProfileUserComment = _Win32NetworkLoginProfileUserComment_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 27),
    _Win32NetworkLoginProfileUserComment_Type()
)
win32NetworkLoginProfileUserComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileUserComment.setStatus("mandatory")
_Win32NetworkLoginProfileUserId_Type = Uint32
_Win32NetworkLoginProfileUserId_Object = MibTableColumn
win32NetworkLoginProfileUserId = _Win32NetworkLoginProfileUserId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 28),
    _Win32NetworkLoginProfileUserId_Type()
)
win32NetworkLoginProfileUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileUserId.setStatus("mandatory")
_Win32NetworkLoginProfileUserType_Type = String
_Win32NetworkLoginProfileUserType_Object = MibTableColumn
win32NetworkLoginProfileUserType = _Win32NetworkLoginProfileUserType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 29),
    _Win32NetworkLoginProfileUserType_Type()
)
win32NetworkLoginProfileUserType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileUserType.setStatus("mandatory")
_Win32NetworkLoginProfileWorkstations_Type = String
_Win32NetworkLoginProfileWorkstations_Object = MibTableColumn
win32NetworkLoginProfileWorkstations = _Win32NetworkLoginProfileWorkstations_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 520, 1, 30),
    _Win32NetworkLoginProfileWorkstations_Type()
)
win32NetworkLoginProfileWorkstations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32NetworkLoginProfileWorkstations.setStatus("mandatory")
_Win32OSRecoveryConfigurationTable_Object = MibTable
win32OSRecoveryConfigurationTable = _Win32OSRecoveryConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 530)
)
if mibBuilder.loadTexts:
    win32OSRecoveryConfigurationTable.setStatus("mandatory")
_Win32OSRecoveryConfigurationEntry_Object = MibTableRow
win32OSRecoveryConfigurationEntry = _Win32OSRecoveryConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 530, 1)
)
win32OSRecoveryConfigurationEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32OSRecoveryConfigurationKeyIndex"),
)
if mibBuilder.loadTexts:
    win32OSRecoveryConfigurationEntry.setStatus("mandatory")
_Win32OSRecoveryConfigurationKeyIndex_Type = String
_Win32OSRecoveryConfigurationKeyIndex_Object = MibTableColumn
win32OSRecoveryConfigurationKeyIndex = _Win32OSRecoveryConfigurationKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 530, 1, 1),
    _Win32OSRecoveryConfigurationKeyIndex_Type()
)
win32OSRecoveryConfigurationKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OSRecoveryConfigurationKeyIndex.setStatus("mandatory")
_Win32OSRecoveryConfigurationAutoReboot_Type = Boolean
_Win32OSRecoveryConfigurationAutoReboot_Object = MibTableColumn
win32OSRecoveryConfigurationAutoReboot = _Win32OSRecoveryConfigurationAutoReboot_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 530, 1, 2),
    _Win32OSRecoveryConfigurationAutoReboot_Type()
)
win32OSRecoveryConfigurationAutoReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OSRecoveryConfigurationAutoReboot.setStatus("mandatory")
_Win32OSRecoveryConfigurationDebugFilePath_Type = String
_Win32OSRecoveryConfigurationDebugFilePath_Object = MibTableColumn
win32OSRecoveryConfigurationDebugFilePath = _Win32OSRecoveryConfigurationDebugFilePath_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 530, 1, 3),
    _Win32OSRecoveryConfigurationDebugFilePath_Type()
)
win32OSRecoveryConfigurationDebugFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OSRecoveryConfigurationDebugFilePath.setStatus("mandatory")
_Win32OSRecoveryConfigurationName_Type = String
_Win32OSRecoveryConfigurationName_Object = MibTableColumn
win32OSRecoveryConfigurationName = _Win32OSRecoveryConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 530, 1, 4),
    _Win32OSRecoveryConfigurationName_Type()
)
win32OSRecoveryConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OSRecoveryConfigurationName.setStatus("mandatory")
_Win32OSRecoveryConfigurationOverwriteExistingDebugFile_Type = Boolean
_Win32OSRecoveryConfigurationOverwriteExistingDebugFile_Object = MibTableColumn
win32OSRecoveryConfigurationOverwriteExistingDebugFile = _Win32OSRecoveryConfigurationOverwriteExistingDebugFile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 530, 1, 5),
    _Win32OSRecoveryConfigurationOverwriteExistingDebugFile_Type()
)
win32OSRecoveryConfigurationOverwriteExistingDebugFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OSRecoveryConfigurationOverwriteExistingDebugFile.setStatus("mandatory")
_Win32OSRecoveryConfigurationSendAdminAlert_Type = Boolean
_Win32OSRecoveryConfigurationSendAdminAlert_Object = MibTableColumn
win32OSRecoveryConfigurationSendAdminAlert = _Win32OSRecoveryConfigurationSendAdminAlert_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 530, 1, 6),
    _Win32OSRecoveryConfigurationSendAdminAlert_Type()
)
win32OSRecoveryConfigurationSendAdminAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OSRecoveryConfigurationSendAdminAlert.setStatus("mandatory")
_Win32OSRecoveryConfigurationWriteDebugInfo_Type = Boolean
_Win32OSRecoveryConfigurationWriteDebugInfo_Object = MibTableColumn
win32OSRecoveryConfigurationWriteDebugInfo = _Win32OSRecoveryConfigurationWriteDebugInfo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 530, 1, 7),
    _Win32OSRecoveryConfigurationWriteDebugInfo_Type()
)
win32OSRecoveryConfigurationWriteDebugInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OSRecoveryConfigurationWriteDebugInfo.setStatus("mandatory")
_Win32OSRecoveryConfigurationWriteToSystemLog_Type = Boolean
_Win32OSRecoveryConfigurationWriteToSystemLog_Object = MibTableColumn
win32OSRecoveryConfigurationWriteToSystemLog = _Win32OSRecoveryConfigurationWriteToSystemLog_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 530, 1, 8),
    _Win32OSRecoveryConfigurationWriteToSystemLog_Type()
)
win32OSRecoveryConfigurationWriteToSystemLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32OSRecoveryConfigurationWriteToSystemLog.setStatus("mandatory")
_Win32PrinterConfigurationTable_Object = MibTable
win32PrinterConfigurationTable = _Win32PrinterConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540)
)
if mibBuilder.loadTexts:
    win32PrinterConfigurationTable.setStatus("mandatory")
_Win32PrinterConfigurationEntry_Object = MibTableRow
win32PrinterConfigurationEntry = _Win32PrinterConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1)
)
win32PrinterConfigurationEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32PrinterConfigurationKeyIndex"),
)
if mibBuilder.loadTexts:
    win32PrinterConfigurationEntry.setStatus("mandatory")
_Win32PrinterConfigurationKeyIndex_Type = String
_Win32PrinterConfigurationKeyIndex_Object = MibTableColumn
win32PrinterConfigurationKeyIndex = _Win32PrinterConfigurationKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 1),
    _Win32PrinterConfigurationKeyIndex_Type()
)
win32PrinterConfigurationKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationKeyIndex.setStatus("mandatory")
_Win32PrinterConfigurationBitsPerPel_Type = Uint32
_Win32PrinterConfigurationBitsPerPel_Object = MibTableColumn
win32PrinterConfigurationBitsPerPel = _Win32PrinterConfigurationBitsPerPel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 2),
    _Win32PrinterConfigurationBitsPerPel_Type()
)
win32PrinterConfigurationBitsPerPel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationBitsPerPel.setStatus("mandatory")
_Win32PrinterConfigurationCollate_Type = Boolean
_Win32PrinterConfigurationCollate_Object = MibTableColumn
win32PrinterConfigurationCollate = _Win32PrinterConfigurationCollate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 3),
    _Win32PrinterConfigurationCollate_Type()
)
win32PrinterConfigurationCollate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationCollate.setStatus("mandatory")
_Win32PrinterConfigurationColor_Type = Uint32
_Win32PrinterConfigurationColor_Object = MibTableColumn
win32PrinterConfigurationColor = _Win32PrinterConfigurationColor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 4),
    _Win32PrinterConfigurationColor_Type()
)
win32PrinterConfigurationColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationColor.setStatus("mandatory")
_Win32PrinterConfigurationCopies_Type = Uint32
_Win32PrinterConfigurationCopies_Object = MibTableColumn
win32PrinterConfigurationCopies = _Win32PrinterConfigurationCopies_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 5),
    _Win32PrinterConfigurationCopies_Type()
)
win32PrinterConfigurationCopies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationCopies.setStatus("mandatory")
_Win32PrinterConfigurationDeviceName_Type = String
_Win32PrinterConfigurationDeviceName_Object = MibTableColumn
win32PrinterConfigurationDeviceName = _Win32PrinterConfigurationDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 6),
    _Win32PrinterConfigurationDeviceName_Type()
)
win32PrinterConfigurationDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationDeviceName.setStatus("mandatory")
_Win32PrinterConfigurationDisplayFlags_Type = Uint32
_Win32PrinterConfigurationDisplayFlags_Object = MibTableColumn
win32PrinterConfigurationDisplayFlags = _Win32PrinterConfigurationDisplayFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 7),
    _Win32PrinterConfigurationDisplayFlags_Type()
)
win32PrinterConfigurationDisplayFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationDisplayFlags.setStatus("mandatory")
_Win32PrinterConfigurationDisplayFrequency_Type = Uint32
_Win32PrinterConfigurationDisplayFrequency_Object = MibTableColumn
win32PrinterConfigurationDisplayFrequency = _Win32PrinterConfigurationDisplayFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 8),
    _Win32PrinterConfigurationDisplayFrequency_Type()
)
win32PrinterConfigurationDisplayFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationDisplayFrequency.setStatus("mandatory")
_Win32PrinterConfigurationDitherType_Type = Uint32
_Win32PrinterConfigurationDitherType_Object = MibTableColumn
win32PrinterConfigurationDitherType = _Win32PrinterConfigurationDitherType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 9),
    _Win32PrinterConfigurationDitherType_Type()
)
win32PrinterConfigurationDitherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationDitherType.setStatus("mandatory")
_Win32PrinterConfigurationDriverVersion_Type = Uint32
_Win32PrinterConfigurationDriverVersion_Object = MibTableColumn
win32PrinterConfigurationDriverVersion = _Win32PrinterConfigurationDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 10),
    _Win32PrinterConfigurationDriverVersion_Type()
)
win32PrinterConfigurationDriverVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationDriverVersion.setStatus("mandatory")
_Win32PrinterConfigurationDuplex_Type = Boolean
_Win32PrinterConfigurationDuplex_Object = MibTableColumn
win32PrinterConfigurationDuplex = _Win32PrinterConfigurationDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 11),
    _Win32PrinterConfigurationDuplex_Type()
)
win32PrinterConfigurationDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationDuplex.setStatus("mandatory")
_Win32PrinterConfigurationFormName_Type = String
_Win32PrinterConfigurationFormName_Object = MibTableColumn
win32PrinterConfigurationFormName = _Win32PrinterConfigurationFormName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 12),
    _Win32PrinterConfigurationFormName_Type()
)
win32PrinterConfigurationFormName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationFormName.setStatus("mandatory")
_Win32PrinterConfigurationICMIntent_Type = Uint32
_Win32PrinterConfigurationICMIntent_Object = MibTableColumn
win32PrinterConfigurationICMIntent = _Win32PrinterConfigurationICMIntent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 13),
    _Win32PrinterConfigurationICMIntent_Type()
)
win32PrinterConfigurationICMIntent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationICMIntent.setStatus("mandatory")
_Win32PrinterConfigurationICMMethod_Type = Uint32
_Win32PrinterConfigurationICMMethod_Object = MibTableColumn
win32PrinterConfigurationICMMethod = _Win32PrinterConfigurationICMMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 14),
    _Win32PrinterConfigurationICMMethod_Type()
)
win32PrinterConfigurationICMMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationICMMethod.setStatus("mandatory")
_Win32PrinterConfigurationLogPixels_Type = Uint32
_Win32PrinterConfigurationLogPixels_Object = MibTableColumn
win32PrinterConfigurationLogPixels = _Win32PrinterConfigurationLogPixels_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 15),
    _Win32PrinterConfigurationLogPixels_Type()
)
win32PrinterConfigurationLogPixels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationLogPixels.setStatus("mandatory")
_Win32PrinterConfigurationMediaType_Type = Uint32
_Win32PrinterConfigurationMediaType_Object = MibTableColumn
win32PrinterConfigurationMediaType = _Win32PrinterConfigurationMediaType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 16),
    _Win32PrinterConfigurationMediaType_Type()
)
win32PrinterConfigurationMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationMediaType.setStatus("mandatory")
_Win32PrinterConfigurationName_Type = String
_Win32PrinterConfigurationName_Object = MibTableColumn
win32PrinterConfigurationName = _Win32PrinterConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 17),
    _Win32PrinterConfigurationName_Type()
)
win32PrinterConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationName.setStatus("mandatory")
_Win32PrinterConfigurationOrientation_Type = Uint32
_Win32PrinterConfigurationOrientation_Object = MibTableColumn
win32PrinterConfigurationOrientation = _Win32PrinterConfigurationOrientation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 18),
    _Win32PrinterConfigurationOrientation_Type()
)
win32PrinterConfigurationOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationOrientation.setStatus("mandatory")
_Win32PrinterConfigurationPaperLength_Type = Uint32
_Win32PrinterConfigurationPaperLength_Object = MibTableColumn
win32PrinterConfigurationPaperLength = _Win32PrinterConfigurationPaperLength_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 19),
    _Win32PrinterConfigurationPaperLength_Type()
)
win32PrinterConfigurationPaperLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationPaperLength.setStatus("mandatory")
_Win32PrinterConfigurationPaperSize_Type = String
_Win32PrinterConfigurationPaperSize_Object = MibTableColumn
win32PrinterConfigurationPaperSize = _Win32PrinterConfigurationPaperSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 20),
    _Win32PrinterConfigurationPaperSize_Type()
)
win32PrinterConfigurationPaperSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationPaperSize.setStatus("mandatory")
_Win32PrinterConfigurationPaperWidth_Type = Uint32
_Win32PrinterConfigurationPaperWidth_Object = MibTableColumn
win32PrinterConfigurationPaperWidth = _Win32PrinterConfigurationPaperWidth_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 21),
    _Win32PrinterConfigurationPaperWidth_Type()
)
win32PrinterConfigurationPaperWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationPaperWidth.setStatus("mandatory")
_Win32PrinterConfigurationPelsHeight_Type = Uint32
_Win32PrinterConfigurationPelsHeight_Object = MibTableColumn
win32PrinterConfigurationPelsHeight = _Win32PrinterConfigurationPelsHeight_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 22),
    _Win32PrinterConfigurationPelsHeight_Type()
)
win32PrinterConfigurationPelsHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationPelsHeight.setStatus("mandatory")
_Win32PrinterConfigurationPelsWidth_Type = Uint32
_Win32PrinterConfigurationPelsWidth_Object = MibTableColumn
win32PrinterConfigurationPelsWidth = _Win32PrinterConfigurationPelsWidth_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 23),
    _Win32PrinterConfigurationPelsWidth_Type()
)
win32PrinterConfigurationPelsWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationPelsWidth.setStatus("mandatory")
_Win32PrinterConfigurationPrintQuality_Type = Uint32
_Win32PrinterConfigurationPrintQuality_Object = MibTableColumn
win32PrinterConfigurationPrintQuality = _Win32PrinterConfigurationPrintQuality_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 24),
    _Win32PrinterConfigurationPrintQuality_Type()
)
win32PrinterConfigurationPrintQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationPrintQuality.setStatus("mandatory")
_Win32PrinterConfigurationScale_Type = Uint32
_Win32PrinterConfigurationScale_Object = MibTableColumn
win32PrinterConfigurationScale = _Win32PrinterConfigurationScale_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 25),
    _Win32PrinterConfigurationScale_Type()
)
win32PrinterConfigurationScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationScale.setStatus("mandatory")
_Win32PrinterConfigurationSpecificationVersion_Type = Uint32
_Win32PrinterConfigurationSpecificationVersion_Object = MibTableColumn
win32PrinterConfigurationSpecificationVersion = _Win32PrinterConfigurationSpecificationVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 26),
    _Win32PrinterConfigurationSpecificationVersion_Type()
)
win32PrinterConfigurationSpecificationVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationSpecificationVersion.setStatus("mandatory")
_Win32PrinterConfigurationTTOption_Type = Uint32
_Win32PrinterConfigurationTTOption_Object = MibTableColumn
win32PrinterConfigurationTTOption = _Win32PrinterConfigurationTTOption_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 27),
    _Win32PrinterConfigurationTTOption_Type()
)
win32PrinterConfigurationTTOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationTTOption.setStatus("mandatory")
_Win32PrinterConfigurationXResolution_Type = Uint32
_Win32PrinterConfigurationXResolution_Object = MibTableColumn
win32PrinterConfigurationXResolution = _Win32PrinterConfigurationXResolution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 28),
    _Win32PrinterConfigurationXResolution_Type()
)
win32PrinterConfigurationXResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationXResolution.setStatus("mandatory")
_Win32PrinterConfigurationYResolution_Type = Uint32
_Win32PrinterConfigurationYResolution_Object = MibTableColumn
win32PrinterConfigurationYResolution = _Win32PrinterConfigurationYResolution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 540, 1, 29),
    _Win32PrinterConfigurationYResolution_Type()
)
win32PrinterConfigurationYResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32PrinterConfigurationYResolution.setStatus("mandatory")
_Win32ProgramGroupTable_Object = MibTable
win32ProgramGroupTable = _Win32ProgramGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 550)
)
if mibBuilder.loadTexts:
    win32ProgramGroupTable.setStatus("mandatory")
_Win32ProgramGroupEntry_Object = MibTableRow
win32ProgramGroupEntry = _Win32ProgramGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 550, 1)
)
win32ProgramGroupEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32ProgramGroupKeyIndex"),
)
if mibBuilder.loadTexts:
    win32ProgramGroupEntry.setStatus("mandatory")
_Win32ProgramGroupKeyIndex_Type = String
_Win32ProgramGroupKeyIndex_Object = MibTableColumn
win32ProgramGroupKeyIndex = _Win32ProgramGroupKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 550, 1, 1),
    _Win32ProgramGroupKeyIndex_Type()
)
win32ProgramGroupKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProgramGroupKeyIndex.setStatus("mandatory")
_Win32ProgramGroupGroupName_Type = String
_Win32ProgramGroupGroupName_Object = MibTableColumn
win32ProgramGroupGroupName = _Win32ProgramGroupGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 550, 1, 2),
    _Win32ProgramGroupGroupName_Type()
)
win32ProgramGroupGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProgramGroupGroupName.setStatus("mandatory")
_Win32ProgramGroupName_Type = String
_Win32ProgramGroupName_Object = MibTableColumn
win32ProgramGroupName = _Win32ProgramGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 550, 1, 3),
    _Win32ProgramGroupName_Type()
)
win32ProgramGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProgramGroupName.setStatus("mandatory")
_Win32ProgramGroupUserName_Type = String
_Win32ProgramGroupUserName_Object = MibTableColumn
win32ProgramGroupUserName = _Win32ProgramGroupUserName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 550, 1, 4),
    _Win32ProgramGroupUserName_Type()
)
win32ProgramGroupUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32ProgramGroupUserName.setStatus("mandatory")
_Win32SerialPortConfigurationTable_Object = MibTable
win32SerialPortConfigurationTable = _Win32SerialPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560)
)
if mibBuilder.loadTexts:
    win32SerialPortConfigurationTable.setStatus("mandatory")
_Win32SerialPortConfigurationEntry_Object = MibTableRow
win32SerialPortConfigurationEntry = _Win32SerialPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1)
)
win32SerialPortConfigurationEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32SerialPortConfigurationKeyIndex"),
)
if mibBuilder.loadTexts:
    win32SerialPortConfigurationEntry.setStatus("mandatory")
_Win32SerialPortConfigurationKeyIndex_Type = String
_Win32SerialPortConfigurationKeyIndex_Object = MibTableColumn
win32SerialPortConfigurationKeyIndex = _Win32SerialPortConfigurationKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 1),
    _Win32SerialPortConfigurationKeyIndex_Type()
)
win32SerialPortConfigurationKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationKeyIndex.setStatus("mandatory")
_Win32SerialPortConfigurationAbortReadWriteOnError_Type = Boolean
_Win32SerialPortConfigurationAbortReadWriteOnError_Object = MibTableColumn
win32SerialPortConfigurationAbortReadWriteOnError = _Win32SerialPortConfigurationAbortReadWriteOnError_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 2),
    _Win32SerialPortConfigurationAbortReadWriteOnError_Type()
)
win32SerialPortConfigurationAbortReadWriteOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationAbortReadWriteOnError.setStatus("mandatory")
_Win32SerialPortConfigurationBaudRate_Type = Uint32
_Win32SerialPortConfigurationBaudRate_Object = MibTableColumn
win32SerialPortConfigurationBaudRate = _Win32SerialPortConfigurationBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 3),
    _Win32SerialPortConfigurationBaudRate_Type()
)
win32SerialPortConfigurationBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationBaudRate.setStatus("mandatory")
_Win32SerialPortConfigurationBinaryModeEnabled_Type = Boolean
_Win32SerialPortConfigurationBinaryModeEnabled_Object = MibTableColumn
win32SerialPortConfigurationBinaryModeEnabled = _Win32SerialPortConfigurationBinaryModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 4),
    _Win32SerialPortConfigurationBinaryModeEnabled_Type()
)
win32SerialPortConfigurationBinaryModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationBinaryModeEnabled.setStatus("mandatory")
_Win32SerialPortConfigurationBitsPerByte_Type = Uint32
_Win32SerialPortConfigurationBitsPerByte_Object = MibTableColumn
win32SerialPortConfigurationBitsPerByte = _Win32SerialPortConfigurationBitsPerByte_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 5),
    _Win32SerialPortConfigurationBitsPerByte_Type()
)
win32SerialPortConfigurationBitsPerByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationBitsPerByte.setStatus("mandatory")
_Win32SerialPortConfigurationContinueXMitOnXOff_Type = Boolean
_Win32SerialPortConfigurationContinueXMitOnXOff_Object = MibTableColumn
win32SerialPortConfigurationContinueXMitOnXOff = _Win32SerialPortConfigurationContinueXMitOnXOff_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 6),
    _Win32SerialPortConfigurationContinueXMitOnXOff_Type()
)
win32SerialPortConfigurationContinueXMitOnXOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationContinueXMitOnXOff.setStatus("mandatory")
_Win32SerialPortConfigurationCTSOutflowControl_Type = Boolean
_Win32SerialPortConfigurationCTSOutflowControl_Object = MibTableColumn
win32SerialPortConfigurationCTSOutflowControl = _Win32SerialPortConfigurationCTSOutflowControl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 7),
    _Win32SerialPortConfigurationCTSOutflowControl_Type()
)
win32SerialPortConfigurationCTSOutflowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationCTSOutflowControl.setStatus("mandatory")
_Win32SerialPortConfigurationDiscardNULLBytes_Type = Boolean
_Win32SerialPortConfigurationDiscardNULLBytes_Object = MibTableColumn
win32SerialPortConfigurationDiscardNULLBytes = _Win32SerialPortConfigurationDiscardNULLBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 8),
    _Win32SerialPortConfigurationDiscardNULLBytes_Type()
)
win32SerialPortConfigurationDiscardNULLBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationDiscardNULLBytes.setStatus("mandatory")
_Win32SerialPortConfigurationDSROutflowControl_Type = Boolean
_Win32SerialPortConfigurationDSROutflowControl_Object = MibTableColumn
win32SerialPortConfigurationDSROutflowControl = _Win32SerialPortConfigurationDSROutflowControl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 9),
    _Win32SerialPortConfigurationDSROutflowControl_Type()
)
win32SerialPortConfigurationDSROutflowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationDSROutflowControl.setStatus("mandatory")
_Win32SerialPortConfigurationDSRSensitivity_Type = Boolean
_Win32SerialPortConfigurationDSRSensitivity_Object = MibTableColumn
win32SerialPortConfigurationDSRSensitivity = _Win32SerialPortConfigurationDSRSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 10),
    _Win32SerialPortConfigurationDSRSensitivity_Type()
)
win32SerialPortConfigurationDSRSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationDSRSensitivity.setStatus("mandatory")
_Win32SerialPortConfigurationDTRFlowControlType_Type = String
_Win32SerialPortConfigurationDTRFlowControlType_Object = MibTableColumn
win32SerialPortConfigurationDTRFlowControlType = _Win32SerialPortConfigurationDTRFlowControlType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 11),
    _Win32SerialPortConfigurationDTRFlowControlType_Type()
)
win32SerialPortConfigurationDTRFlowControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationDTRFlowControlType.setStatus("mandatory")
_Win32SerialPortConfigurationEOFCharacter_Type = Uint32
_Win32SerialPortConfigurationEOFCharacter_Object = MibTableColumn
win32SerialPortConfigurationEOFCharacter = _Win32SerialPortConfigurationEOFCharacter_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 12),
    _Win32SerialPortConfigurationEOFCharacter_Type()
)
win32SerialPortConfigurationEOFCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationEOFCharacter.setStatus("mandatory")
_Win32SerialPortConfigurationErrorReplaceCharacter_Type = Uint32
_Win32SerialPortConfigurationErrorReplaceCharacter_Object = MibTableColumn
win32SerialPortConfigurationErrorReplaceCharacter = _Win32SerialPortConfigurationErrorReplaceCharacter_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 13),
    _Win32SerialPortConfigurationErrorReplaceCharacter_Type()
)
win32SerialPortConfigurationErrorReplaceCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationErrorReplaceCharacter.setStatus("mandatory")
_Win32SerialPortConfigurationErrorReplacementEnabled_Type = Boolean
_Win32SerialPortConfigurationErrorReplacementEnabled_Object = MibTableColumn
win32SerialPortConfigurationErrorReplacementEnabled = _Win32SerialPortConfigurationErrorReplacementEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 14),
    _Win32SerialPortConfigurationErrorReplacementEnabled_Type()
)
win32SerialPortConfigurationErrorReplacementEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationErrorReplacementEnabled.setStatus("mandatory")
_Win32SerialPortConfigurationEventCharacter_Type = Uint32
_Win32SerialPortConfigurationEventCharacter_Object = MibTableColumn
win32SerialPortConfigurationEventCharacter = _Win32SerialPortConfigurationEventCharacter_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 15),
    _Win32SerialPortConfigurationEventCharacter_Type()
)
win32SerialPortConfigurationEventCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationEventCharacter.setStatus("mandatory")
_Win32SerialPortConfigurationIsBusy_Type = Boolean
_Win32SerialPortConfigurationIsBusy_Object = MibTableColumn
win32SerialPortConfigurationIsBusy = _Win32SerialPortConfigurationIsBusy_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 16),
    _Win32SerialPortConfigurationIsBusy_Type()
)
win32SerialPortConfigurationIsBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationIsBusy.setStatus("mandatory")
_Win32SerialPortConfigurationName_Type = String
_Win32SerialPortConfigurationName_Object = MibTableColumn
win32SerialPortConfigurationName = _Win32SerialPortConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 17),
    _Win32SerialPortConfigurationName_Type()
)
win32SerialPortConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationName.setStatus("mandatory")
_Win32SerialPortConfigurationParity_Type = String
_Win32SerialPortConfigurationParity_Object = MibTableColumn
win32SerialPortConfigurationParity = _Win32SerialPortConfigurationParity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 18),
    _Win32SerialPortConfigurationParity_Type()
)
win32SerialPortConfigurationParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationParity.setStatus("mandatory")
_Win32SerialPortConfigurationParityCheckEnabled_Type = Boolean
_Win32SerialPortConfigurationParityCheckEnabled_Object = MibTableColumn
win32SerialPortConfigurationParityCheckEnabled = _Win32SerialPortConfigurationParityCheckEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 19),
    _Win32SerialPortConfigurationParityCheckEnabled_Type()
)
win32SerialPortConfigurationParityCheckEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationParityCheckEnabled.setStatus("mandatory")
_Win32SerialPortConfigurationRTSFlowControlType_Type = String
_Win32SerialPortConfigurationRTSFlowControlType_Object = MibTableColumn
win32SerialPortConfigurationRTSFlowControlType = _Win32SerialPortConfigurationRTSFlowControlType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 20),
    _Win32SerialPortConfigurationRTSFlowControlType_Type()
)
win32SerialPortConfigurationRTSFlowControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationRTSFlowControlType.setStatus("mandatory")
_Win32SerialPortConfigurationStopBits_Type = String
_Win32SerialPortConfigurationStopBits_Object = MibTableColumn
win32SerialPortConfigurationStopBits = _Win32SerialPortConfigurationStopBits_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 21),
    _Win32SerialPortConfigurationStopBits_Type()
)
win32SerialPortConfigurationStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationStopBits.setStatus("mandatory")
_Win32SerialPortConfigurationXOffCharacter_Type = Uint32
_Win32SerialPortConfigurationXOffCharacter_Object = MibTableColumn
win32SerialPortConfigurationXOffCharacter = _Win32SerialPortConfigurationXOffCharacter_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 22),
    _Win32SerialPortConfigurationXOffCharacter_Type()
)
win32SerialPortConfigurationXOffCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationXOffCharacter.setStatus("mandatory")
_Win32SerialPortConfigurationXOffXMitThreshold_Type = Uint32
_Win32SerialPortConfigurationXOffXMitThreshold_Object = MibTableColumn
win32SerialPortConfigurationXOffXMitThreshold = _Win32SerialPortConfigurationXOffXMitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 23),
    _Win32SerialPortConfigurationXOffXMitThreshold_Type()
)
win32SerialPortConfigurationXOffXMitThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationXOffXMitThreshold.setStatus("mandatory")
_Win32SerialPortConfigurationXOnCharacter_Type = Uint32
_Win32SerialPortConfigurationXOnCharacter_Object = MibTableColumn
win32SerialPortConfigurationXOnCharacter = _Win32SerialPortConfigurationXOnCharacter_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 24),
    _Win32SerialPortConfigurationXOnCharacter_Type()
)
win32SerialPortConfigurationXOnCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationXOnCharacter.setStatus("mandatory")
_Win32SerialPortConfigurationXOnXMitThreshold_Type = Uint32
_Win32SerialPortConfigurationXOnXMitThreshold_Object = MibTableColumn
win32SerialPortConfigurationXOnXMitThreshold = _Win32SerialPortConfigurationXOnXMitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 25),
    _Win32SerialPortConfigurationXOnXMitThreshold_Type()
)
win32SerialPortConfigurationXOnXMitThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationXOnXMitThreshold.setStatus("mandatory")
_Win32SerialPortConfigurationXOnXOffInFlowControl_Type = Uint32
_Win32SerialPortConfigurationXOnXOffInFlowControl_Object = MibTableColumn
win32SerialPortConfigurationXOnXOffInFlowControl = _Win32SerialPortConfigurationXOnXOffInFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 26),
    _Win32SerialPortConfigurationXOnXOffInFlowControl_Type()
)
win32SerialPortConfigurationXOnXOffInFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationXOnXOffInFlowControl.setStatus("mandatory")
_Win32SerialPortConfigurationXOnXOffOutFlowControl_Type = Uint32
_Win32SerialPortConfigurationXOnXOffOutFlowControl_Object = MibTableColumn
win32SerialPortConfigurationXOnXOffOutFlowControl = _Win32SerialPortConfigurationXOnXOffOutFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 560, 1, 27),
    _Win32SerialPortConfigurationXOnXOffOutFlowControl_Type()
)
win32SerialPortConfigurationXOnXOffOutFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32SerialPortConfigurationXOnXOffOutFlowControl.setStatus("mandatory")
_Win32TimeZoneTable_Object = MibTable
win32TimeZoneTable = _Win32TimeZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570)
)
if mibBuilder.loadTexts:
    win32TimeZoneTable.setStatus("mandatory")
_Win32TimeZoneEntry_Object = MibTableRow
win32TimeZoneEntry = _Win32TimeZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1)
)
win32TimeZoneEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32TimeZoneKeyIndex"),
)
if mibBuilder.loadTexts:
    win32TimeZoneEntry.setStatus("mandatory")
_Win32TimeZoneKeyIndex_Type = String
_Win32TimeZoneKeyIndex_Object = MibTableColumn
win32TimeZoneKeyIndex = _Win32TimeZoneKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 1),
    _Win32TimeZoneKeyIndex_Type()
)
win32TimeZoneKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneKeyIndex.setStatus("mandatory")
_Win32TimeZoneBias_Type = Sint32
_Win32TimeZoneBias_Object = MibTableColumn
win32TimeZoneBias = _Win32TimeZoneBias_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 2),
    _Win32TimeZoneBias_Type()
)
win32TimeZoneBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneBias.setStatus("mandatory")
_Win32TimeZoneDaylightBias_Type = Sint32
_Win32TimeZoneDaylightBias_Object = MibTableColumn
win32TimeZoneDaylightBias = _Win32TimeZoneDaylightBias_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 3),
    _Win32TimeZoneDaylightBias_Type()
)
win32TimeZoneDaylightBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneDaylightBias.setStatus("mandatory")
_Win32TimeZoneDaylightDay_Type = Uint32
_Win32TimeZoneDaylightDay_Object = MibTableColumn
win32TimeZoneDaylightDay = _Win32TimeZoneDaylightDay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 4),
    _Win32TimeZoneDaylightDay_Type()
)
win32TimeZoneDaylightDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneDaylightDay.setStatus("mandatory")
_Win32TimeZoneDaylightDayOfWeek_Type = Uint8
_Win32TimeZoneDaylightDayOfWeek_Object = MibTableColumn
win32TimeZoneDaylightDayOfWeek = _Win32TimeZoneDaylightDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 5),
    _Win32TimeZoneDaylightDayOfWeek_Type()
)
win32TimeZoneDaylightDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneDaylightDayOfWeek.setStatus("mandatory")
_Win32TimeZoneDaylightHour_Type = Uint32
_Win32TimeZoneDaylightHour_Object = MibTableColumn
win32TimeZoneDaylightHour = _Win32TimeZoneDaylightHour_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 6),
    _Win32TimeZoneDaylightHour_Type()
)
win32TimeZoneDaylightHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneDaylightHour.setStatus("mandatory")
_Win32TimeZoneDaylightMillisecond_Type = Uint32
_Win32TimeZoneDaylightMillisecond_Object = MibTableColumn
win32TimeZoneDaylightMillisecond = _Win32TimeZoneDaylightMillisecond_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 7),
    _Win32TimeZoneDaylightMillisecond_Type()
)
win32TimeZoneDaylightMillisecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneDaylightMillisecond.setStatus("mandatory")
_Win32TimeZoneDaylightMinute_Type = Uint32
_Win32TimeZoneDaylightMinute_Object = MibTableColumn
win32TimeZoneDaylightMinute = _Win32TimeZoneDaylightMinute_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 8),
    _Win32TimeZoneDaylightMinute_Type()
)
win32TimeZoneDaylightMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneDaylightMinute.setStatus("mandatory")
_Win32TimeZoneDaylightMonth_Type = Uint32
_Win32TimeZoneDaylightMonth_Object = MibTableColumn
win32TimeZoneDaylightMonth = _Win32TimeZoneDaylightMonth_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 9),
    _Win32TimeZoneDaylightMonth_Type()
)
win32TimeZoneDaylightMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneDaylightMonth.setStatus("mandatory")
_Win32TimeZoneDaylightName_Type = String
_Win32TimeZoneDaylightName_Object = MibTableColumn
win32TimeZoneDaylightName = _Win32TimeZoneDaylightName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 10),
    _Win32TimeZoneDaylightName_Type()
)
win32TimeZoneDaylightName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneDaylightName.setStatus("mandatory")
_Win32TimeZoneDaylightSecond_Type = Uint32
_Win32TimeZoneDaylightSecond_Object = MibTableColumn
win32TimeZoneDaylightSecond = _Win32TimeZoneDaylightSecond_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 11),
    _Win32TimeZoneDaylightSecond_Type()
)
win32TimeZoneDaylightSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneDaylightSecond.setStatus("mandatory")
_Win32TimeZoneDaylightYear_Type = Uint32
_Win32TimeZoneDaylightYear_Object = MibTableColumn
win32TimeZoneDaylightYear = _Win32TimeZoneDaylightYear_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 12),
    _Win32TimeZoneDaylightYear_Type()
)
win32TimeZoneDaylightYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneDaylightYear.setStatus("mandatory")
_Win32TimeZoneStandardBias_Type = Uint32
_Win32TimeZoneStandardBias_Object = MibTableColumn
win32TimeZoneStandardBias = _Win32TimeZoneStandardBias_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 13),
    _Win32TimeZoneStandardBias_Type()
)
win32TimeZoneStandardBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneStandardBias.setStatus("mandatory")
_Win32TimeZoneStandardDay_Type = Uint32
_Win32TimeZoneStandardDay_Object = MibTableColumn
win32TimeZoneStandardDay = _Win32TimeZoneStandardDay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 14),
    _Win32TimeZoneStandardDay_Type()
)
win32TimeZoneStandardDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneStandardDay.setStatus("mandatory")
_Win32TimeZoneStandardDayOfWeek_Type = Uint8
_Win32TimeZoneStandardDayOfWeek_Object = MibTableColumn
win32TimeZoneStandardDayOfWeek = _Win32TimeZoneStandardDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 15),
    _Win32TimeZoneStandardDayOfWeek_Type()
)
win32TimeZoneStandardDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneStandardDayOfWeek.setStatus("mandatory")
_Win32TimeZoneStandardHour_Type = Uint32
_Win32TimeZoneStandardHour_Object = MibTableColumn
win32TimeZoneStandardHour = _Win32TimeZoneStandardHour_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 16),
    _Win32TimeZoneStandardHour_Type()
)
win32TimeZoneStandardHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneStandardHour.setStatus("mandatory")
_Win32TimeZoneStandardMillisecond_Type = Uint32
_Win32TimeZoneStandardMillisecond_Object = MibTableColumn
win32TimeZoneStandardMillisecond = _Win32TimeZoneStandardMillisecond_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 17),
    _Win32TimeZoneStandardMillisecond_Type()
)
win32TimeZoneStandardMillisecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneStandardMillisecond.setStatus("mandatory")
_Win32TimeZoneStandardMinute_Type = Uint32
_Win32TimeZoneStandardMinute_Object = MibTableColumn
win32TimeZoneStandardMinute = _Win32TimeZoneStandardMinute_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 18),
    _Win32TimeZoneStandardMinute_Type()
)
win32TimeZoneStandardMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneStandardMinute.setStatus("mandatory")
_Win32TimeZoneStandardMonth_Type = Uint32
_Win32TimeZoneStandardMonth_Object = MibTableColumn
win32TimeZoneStandardMonth = _Win32TimeZoneStandardMonth_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 19),
    _Win32TimeZoneStandardMonth_Type()
)
win32TimeZoneStandardMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneStandardMonth.setStatus("mandatory")
_Win32TimeZoneStandardName_Type = String
_Win32TimeZoneStandardName_Object = MibTableColumn
win32TimeZoneStandardName = _Win32TimeZoneStandardName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 20),
    _Win32TimeZoneStandardName_Type()
)
win32TimeZoneStandardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneStandardName.setStatus("mandatory")
_Win32TimeZoneStandardSecond_Type = Uint32
_Win32TimeZoneStandardSecond_Object = MibTableColumn
win32TimeZoneStandardSecond = _Win32TimeZoneStandardSecond_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 21),
    _Win32TimeZoneStandardSecond_Type()
)
win32TimeZoneStandardSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneStandardSecond.setStatus("mandatory")
_Win32TimeZoneStandardYear_Type = Uint32
_Win32TimeZoneStandardYear_Object = MibTableColumn
win32TimeZoneStandardYear = _Win32TimeZoneStandardYear_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 570, 1, 22),
    _Win32TimeZoneStandardYear_Type()
)
win32TimeZoneStandardYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32TimeZoneStandardYear.setStatus("mandatory")
_Win32VideoConfigurationTable_Object = MibTable
win32VideoConfigurationTable = _Win32VideoConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580)
)
if mibBuilder.loadTexts:
    win32VideoConfigurationTable.setStatus("mandatory")
_Win32VideoConfigurationEntry_Object = MibTableRow
win32VideoConfigurationEntry = _Win32VideoConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1)
)
win32VideoConfigurationEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32VideoConfigurationKeyIndex"),
)
if mibBuilder.loadTexts:
    win32VideoConfigurationEntry.setStatus("mandatory")
_Win32VideoConfigurationKeyIndex_Type = String
_Win32VideoConfigurationKeyIndex_Object = MibTableColumn
win32VideoConfigurationKeyIndex = _Win32VideoConfigurationKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 1),
    _Win32VideoConfigurationKeyIndex_Type()
)
win32VideoConfigurationKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationKeyIndex.setStatus("mandatory")
_Win32VideoConfigurationActualColorResolution_Type = Uint32
_Win32VideoConfigurationActualColorResolution_Object = MibTableColumn
win32VideoConfigurationActualColorResolution = _Win32VideoConfigurationActualColorResolution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 2),
    _Win32VideoConfigurationActualColorResolution_Type()
)
win32VideoConfigurationActualColorResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationActualColorResolution.setStatus("mandatory")
_Win32VideoConfigurationAdapterChipType_Type = String
_Win32VideoConfigurationAdapterChipType_Object = MibTableColumn
win32VideoConfigurationAdapterChipType = _Win32VideoConfigurationAdapterChipType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 3),
    _Win32VideoConfigurationAdapterChipType_Type()
)
win32VideoConfigurationAdapterChipType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationAdapterChipType.setStatus("mandatory")
_Win32VideoConfigurationAdapterCompatibility_Type = String
_Win32VideoConfigurationAdapterCompatibility_Object = MibTableColumn
win32VideoConfigurationAdapterCompatibility = _Win32VideoConfigurationAdapterCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 4),
    _Win32VideoConfigurationAdapterCompatibility_Type()
)
win32VideoConfigurationAdapterCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationAdapterCompatibility.setStatus("mandatory")
_Win32VideoConfigurationAdapterDACType_Type = String
_Win32VideoConfigurationAdapterDACType_Object = MibTableColumn
win32VideoConfigurationAdapterDACType = _Win32VideoConfigurationAdapterDACType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 5),
    _Win32VideoConfigurationAdapterDACType_Type()
)
win32VideoConfigurationAdapterDACType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationAdapterDACType.setStatus("mandatory")
_Win32VideoConfigurationAdapterDescription_Type = String
_Win32VideoConfigurationAdapterDescription_Object = MibTableColumn
win32VideoConfigurationAdapterDescription = _Win32VideoConfigurationAdapterDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 6),
    _Win32VideoConfigurationAdapterDescription_Type()
)
win32VideoConfigurationAdapterDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationAdapterDescription.setStatus("mandatory")
_Win32VideoConfigurationAdapterRAM_Type = Uint32
_Win32VideoConfigurationAdapterRAM_Object = MibTableColumn
win32VideoConfigurationAdapterRAM = _Win32VideoConfigurationAdapterRAM_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 7),
    _Win32VideoConfigurationAdapterRAM_Type()
)
win32VideoConfigurationAdapterRAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationAdapterRAM.setStatus("mandatory")
_Win32VideoConfigurationAdapterType_Type = String
_Win32VideoConfigurationAdapterType_Object = MibTableColumn
win32VideoConfigurationAdapterType = _Win32VideoConfigurationAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 8),
    _Win32VideoConfigurationAdapterType_Type()
)
win32VideoConfigurationAdapterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationAdapterType.setStatus("mandatory")
_Win32VideoConfigurationBitsPerPixel_Type = Uint32
_Win32VideoConfigurationBitsPerPixel_Object = MibTableColumn
win32VideoConfigurationBitsPerPixel = _Win32VideoConfigurationBitsPerPixel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 9),
    _Win32VideoConfigurationBitsPerPixel_Type()
)
win32VideoConfigurationBitsPerPixel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationBitsPerPixel.setStatus("mandatory")
_Win32VideoConfigurationColorPlanes_Type = Uint32
_Win32VideoConfigurationColorPlanes_Object = MibTableColumn
win32VideoConfigurationColorPlanes = _Win32VideoConfigurationColorPlanes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 10),
    _Win32VideoConfigurationColorPlanes_Type()
)
win32VideoConfigurationColorPlanes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationColorPlanes.setStatus("mandatory")
_Win32VideoConfigurationColorTableEntries_Type = Uint32
_Win32VideoConfigurationColorTableEntries_Object = MibTableColumn
win32VideoConfigurationColorTableEntries = _Win32VideoConfigurationColorTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 11),
    _Win32VideoConfigurationColorTableEntries_Type()
)
win32VideoConfigurationColorTableEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationColorTableEntries.setStatus("mandatory")
_Win32VideoConfigurationDeviceSpecificPens_Type = Uint32
_Win32VideoConfigurationDeviceSpecificPens_Object = MibTableColumn
win32VideoConfigurationDeviceSpecificPens = _Win32VideoConfigurationDeviceSpecificPens_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 12),
    _Win32VideoConfigurationDeviceSpecificPens_Type()
)
win32VideoConfigurationDeviceSpecificPens.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationDeviceSpecificPens.setStatus("mandatory")
_Win32VideoConfigurationDriverDate_Type = Datetime
_Win32VideoConfigurationDriverDate_Object = MibTableColumn
win32VideoConfigurationDriverDate = _Win32VideoConfigurationDriverDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 13),
    _Win32VideoConfigurationDriverDate_Type()
)
win32VideoConfigurationDriverDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationDriverDate.setStatus("mandatory")
_Win32VideoConfigurationHorizontalResolution_Type = Uint32
_Win32VideoConfigurationHorizontalResolution_Object = MibTableColumn
win32VideoConfigurationHorizontalResolution = _Win32VideoConfigurationHorizontalResolution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 14),
    _Win32VideoConfigurationHorizontalResolution_Type()
)
win32VideoConfigurationHorizontalResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationHorizontalResolution.setStatus("mandatory")
_Win32VideoConfigurationInfFilename_Type = String
_Win32VideoConfigurationInfFilename_Object = MibTableColumn
win32VideoConfigurationInfFilename = _Win32VideoConfigurationInfFilename_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 15),
    _Win32VideoConfigurationInfFilename_Type()
)
win32VideoConfigurationInfFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationInfFilename.setStatus("mandatory")
_Win32VideoConfigurationInfSection_Type = String
_Win32VideoConfigurationInfSection_Object = MibTableColumn
win32VideoConfigurationInfSection = _Win32VideoConfigurationInfSection_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 16),
    _Win32VideoConfigurationInfSection_Type()
)
win32VideoConfigurationInfSection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationInfSection.setStatus("mandatory")
_Win32VideoConfigurationInstalledDisplayDrivers_Type = String
_Win32VideoConfigurationInstalledDisplayDrivers_Object = MibTableColumn
win32VideoConfigurationInstalledDisplayDrivers = _Win32VideoConfigurationInstalledDisplayDrivers_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 17),
    _Win32VideoConfigurationInstalledDisplayDrivers_Type()
)
win32VideoConfigurationInstalledDisplayDrivers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationInstalledDisplayDrivers.setStatus("mandatory")
_Win32VideoConfigurationMonitorManufacturer_Type = String
_Win32VideoConfigurationMonitorManufacturer_Object = MibTableColumn
win32VideoConfigurationMonitorManufacturer = _Win32VideoConfigurationMonitorManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 18),
    _Win32VideoConfigurationMonitorManufacturer_Type()
)
win32VideoConfigurationMonitorManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationMonitorManufacturer.setStatus("mandatory")
_Win32VideoConfigurationMonitorType_Type = String
_Win32VideoConfigurationMonitorType_Object = MibTableColumn
win32VideoConfigurationMonitorType = _Win32VideoConfigurationMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 19),
    _Win32VideoConfigurationMonitorType_Type()
)
win32VideoConfigurationMonitorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationMonitorType.setStatus("mandatory")
_Win32VideoConfigurationName_Type = String
_Win32VideoConfigurationName_Object = MibTableColumn
win32VideoConfigurationName = _Win32VideoConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 20),
    _Win32VideoConfigurationName_Type()
)
win32VideoConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationName.setStatus("mandatory")
_Win32VideoConfigurationPixelsPerXLogicalInch_Type = Uint32
_Win32VideoConfigurationPixelsPerXLogicalInch_Object = MibTableColumn
win32VideoConfigurationPixelsPerXLogicalInch = _Win32VideoConfigurationPixelsPerXLogicalInch_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 21),
    _Win32VideoConfigurationPixelsPerXLogicalInch_Type()
)
win32VideoConfigurationPixelsPerXLogicalInch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationPixelsPerXLogicalInch.setStatus("mandatory")
_Win32VideoConfigurationPixelsPerYLogicalInch_Type = Uint32
_Win32VideoConfigurationPixelsPerYLogicalInch_Object = MibTableColumn
win32VideoConfigurationPixelsPerYLogicalInch = _Win32VideoConfigurationPixelsPerYLogicalInch_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 22),
    _Win32VideoConfigurationPixelsPerYLogicalInch_Type()
)
win32VideoConfigurationPixelsPerYLogicalInch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationPixelsPerYLogicalInch.setStatus("mandatory")
_Win32VideoConfigurationRefreshRate_Type = Uint32
_Win32VideoConfigurationRefreshRate_Object = MibTableColumn
win32VideoConfigurationRefreshRate = _Win32VideoConfigurationRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 23),
    _Win32VideoConfigurationRefreshRate_Type()
)
win32VideoConfigurationRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationRefreshRate.setStatus("mandatory")
_Win32VideoConfigurationScanMode_Type = String
_Win32VideoConfigurationScanMode_Object = MibTableColumn
win32VideoConfigurationScanMode = _Win32VideoConfigurationScanMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 24),
    _Win32VideoConfigurationScanMode_Type()
)
win32VideoConfigurationScanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationScanMode.setStatus("mandatory")
_Win32VideoConfigurationScreenHeight_Type = Uint32
_Win32VideoConfigurationScreenHeight_Object = MibTableColumn
win32VideoConfigurationScreenHeight = _Win32VideoConfigurationScreenHeight_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 25),
    _Win32VideoConfigurationScreenHeight_Type()
)
win32VideoConfigurationScreenHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationScreenHeight.setStatus("mandatory")
_Win32VideoConfigurationScreenWidth_Type = Uint32
_Win32VideoConfigurationScreenWidth_Object = MibTableColumn
win32VideoConfigurationScreenWidth = _Win32VideoConfigurationScreenWidth_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 26),
    _Win32VideoConfigurationScreenWidth_Type()
)
win32VideoConfigurationScreenWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationScreenWidth.setStatus("mandatory")
_Win32VideoConfigurationSystemPaletteEntries_Type = Uint32
_Win32VideoConfigurationSystemPaletteEntries_Object = MibTableColumn
win32VideoConfigurationSystemPaletteEntries = _Win32VideoConfigurationSystemPaletteEntries_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 27),
    _Win32VideoConfigurationSystemPaletteEntries_Type()
)
win32VideoConfigurationSystemPaletteEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationSystemPaletteEntries.setStatus("mandatory")
_Win32VideoConfigurationVerticalResolution_Type = Uint32
_Win32VideoConfigurationVerticalResolution_Object = MibTableColumn
win32VideoConfigurationVerticalResolution = _Win32VideoConfigurationVerticalResolution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 580, 1, 28),
    _Win32VideoConfigurationVerticalResolution_Type()
)
win32VideoConfigurationVerticalResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32VideoConfigurationVerticalResolution.setStatus("mandatory")
_Win32LogicalDiskToPartitionTable_Object = MibTable
win32LogicalDiskToPartitionTable = _Win32LogicalDiskToPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 590)
)
if mibBuilder.loadTexts:
    win32LogicalDiskToPartitionTable.setStatus("mandatory")
_Win32LogicalDiskToPartitionEntry_Object = MibTableRow
win32LogicalDiskToPartitionEntry = _Win32LogicalDiskToPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 590, 1)
)
win32LogicalDiskToPartitionEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32LogicalDiskToPartitionKeyIndex"),
)
if mibBuilder.loadTexts:
    win32LogicalDiskToPartitionEntry.setStatus("mandatory")
_Win32LogicalDiskToPartitionKeyIndex_Type = String
_Win32LogicalDiskToPartitionKeyIndex_Object = MibTableColumn
win32LogicalDiskToPartitionKeyIndex = _Win32LogicalDiskToPartitionKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 590, 1, 1),
    _Win32LogicalDiskToPartitionKeyIndex_Type()
)
win32LogicalDiskToPartitionKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskToPartitionKeyIndex.setStatus("mandatory")
_Win32LogicalDiskToPartitionAntecedent_Type = String
_Win32LogicalDiskToPartitionAntecedent_Object = MibTableColumn
win32LogicalDiskToPartitionAntecedent = _Win32LogicalDiskToPartitionAntecedent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 590, 1, 2),
    _Win32LogicalDiskToPartitionAntecedent_Type()
)
win32LogicalDiskToPartitionAntecedent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskToPartitionAntecedent.setStatus("mandatory")
_Win32LogicalDiskToPartitionDependent_Type = String
_Win32LogicalDiskToPartitionDependent_Object = MibTableColumn
win32LogicalDiskToPartitionDependent = _Win32LogicalDiskToPartitionDependent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 590, 1, 3),
    _Win32LogicalDiskToPartitionDependent_Type()
)
win32LogicalDiskToPartitionDependent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32LogicalDiskToPartitionDependent.setStatus("mandatory")
_Win32DiskDriveToDiskPartitionTable_Object = MibTable
win32DiskDriveToDiskPartitionTable = _Win32DiskDriveToDiskPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 600)
)
if mibBuilder.loadTexts:
    win32DiskDriveToDiskPartitionTable.setStatus("mandatory")
_Win32DiskDriveToDiskPartitionEntry_Object = MibTableRow
win32DiskDriveToDiskPartitionEntry = _Win32DiskDriveToDiskPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 600, 1)
)
win32DiskDriveToDiskPartitionEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "win32DiskDriveToDiskPartitionKeyIndex"),
)
if mibBuilder.loadTexts:
    win32DiskDriveToDiskPartitionEntry.setStatus("mandatory")
_Win32DiskDriveToDiskPartitionKeyIndex_Type = String
_Win32DiskDriveToDiskPartitionKeyIndex_Object = MibTableColumn
win32DiskDriveToDiskPartitionKeyIndex = _Win32DiskDriveToDiskPartitionKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 600, 1, 1),
    _Win32DiskDriveToDiskPartitionKeyIndex_Type()
)
win32DiskDriveToDiskPartitionKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveToDiskPartitionKeyIndex.setStatus("mandatory")
_Win32DiskDriveToDiskPartitionAntecedent_Type = String
_Win32DiskDriveToDiskPartitionAntecedent_Object = MibTableColumn
win32DiskDriveToDiskPartitionAntecedent = _Win32DiskDriveToDiskPartitionAntecedent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 600, 1, 2),
    _Win32DiskDriveToDiskPartitionAntecedent_Type()
)
win32DiskDriveToDiskPartitionAntecedent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveToDiskPartitionAntecedent.setStatus("mandatory")
_Win32DiskDriveToDiskPartitionDependent_Type = String
_Win32DiskDriveToDiskPartitionDependent_Object = MibTableColumn
win32DiskDriveToDiskPartitionDependent = _Win32DiskDriveToDiskPartitionDependent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 600, 1, 3),
    _Win32DiskDriveToDiskPartitionDependent_Type()
)
win32DiskDriveToDiskPartitionDependent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32DiskDriveToDiskPartitionDependent.setStatus("mandatory")
_CimBIOSElementTable_Object = MibTable
cimBIOSElementTable = _CimBIOSElementTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 610)
)
if mibBuilder.loadTexts:
    cimBIOSElementTable.setStatus("mandatory")
_CimBIOSElementEntry_Object = MibTableRow
cimBIOSElementEntry = _CimBIOSElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 610, 1)
)
cimBIOSElementEntry.setIndexNames(
    (0, "CIMWIN32-MIB", "cimBIOSElementKeyIndex"),
)
if mibBuilder.loadTexts:
    cimBIOSElementEntry.setStatus("mandatory")
_CimBIOSElementKeyIndex_Type = String
_CimBIOSElementKeyIndex_Object = MibTableColumn
cimBIOSElementKeyIndex = _CimBIOSElementKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 610, 1, 1),
    _CimBIOSElementKeyIndex_Type()
)
cimBIOSElementKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimBIOSElementKeyIndex.setStatus("mandatory")
_CimBIOSElementName_Type = String
_CimBIOSElementName_Object = MibTableColumn
cimBIOSElementName = _CimBIOSElementName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 610, 1, 2),
    _CimBIOSElementName_Type()
)
cimBIOSElementName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimBIOSElementName.setStatus("mandatory")
_CimBIOSElementManufacturer_Type = String
_CimBIOSElementManufacturer_Object = MibTableColumn
cimBIOSElementManufacturer = _CimBIOSElementManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 610, 1, 3),
    _CimBIOSElementManufacturer_Type()
)
cimBIOSElementManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimBIOSElementManufacturer.setStatus("mandatory")
_CimBIOSElementDescription_Type = String
_CimBIOSElementDescription_Object = MibTableColumn
cimBIOSElementDescription = _CimBIOSElementDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 610, 1, 4),
    _CimBIOSElementDescription_Type()
)
cimBIOSElementDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimBIOSElementDescription.setStatus("mandatory")
_CimBIOSElementVersion_Type = String
_CimBIOSElementVersion_Object = MibTableColumn
cimBIOSElementVersion = _CimBIOSElementVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 610, 1, 5),
    _CimBIOSElementVersion_Type()
)
cimBIOSElementVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimBIOSElementVersion.setStatus("mandatory")
_CimBIOSElementBuildNumber_Type = String
_CimBIOSElementBuildNumber_Object = MibTableColumn
cimBIOSElementBuildNumber = _CimBIOSElementBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 610, 1, 6),
    _CimBIOSElementBuildNumber_Type()
)
cimBIOSElementBuildNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimBIOSElementBuildNumber.setStatus("mandatory")
_CimBIOSElementReleaseDate_Type = Datetime
_CimBIOSElementReleaseDate_Object = MibTableColumn
cimBIOSElementReleaseDate = _CimBIOSElementReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 2, 10, 610, 1, 7),
    _CimBIOSElementReleaseDate_Type()
)
cimBIOSElementReleaseDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cimBIOSElementReleaseDate.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIMWIN32-MIB",
    **{"win32ComputerSystemTable": win32ComputerSystemTable,
       "win32ComputerSystemEntry": win32ComputerSystemEntry,
       "win32ComputerSystemKeyIndex": win32ComputerSystemKeyIndex,
       "win32ComputerSystemAutomaticResetBootOption": win32ComputerSystemAutomaticResetBootOption,
       "win32ComputerSystemAutomaticResetCapability": win32ComputerSystemAutomaticResetCapability,
       "win32ComputerSystemBootROMSupported": win32ComputerSystemBootROMSupported,
       "win32ComputerSystemBootupState": win32ComputerSystemBootupState,
       "win32ComputerSystemCurrentTimeZone": win32ComputerSystemCurrentTimeZone,
       "win32ComputerSystemDomain": win32ComputerSystemDomain,
       "win32ComputerSystemInfraredSupported": win32ComputerSystemInfraredSupported,
       "win32ComputerSystemManufacturer": win32ComputerSystemManufacturer,
       "win32ComputerSystemModel": win32ComputerSystemModel,
       "win32ComputerSystemNetworkServerModeEnabled": win32ComputerSystemNetworkServerModeEnabled,
       "win32ComputerSystemOEMLogoBitmap": win32ComputerSystemOEMLogoBitmap,
       "win32ComputerSystemSupportContactDescription": win32ComputerSystemSupportContactDescription,
       "win32ComputerSystemSystemStartupDelay": win32ComputerSystemSystemStartupDelay,
       "win32ComputerSystemSystemStartupOptions": win32ComputerSystemSystemStartupOptions,
       "win32ComputerSystemSystemStartupSetting": win32ComputerSystemSystemStartupSetting,
       "win32ComputerSystemSystemType": win32ComputerSystemSystemType,
       "win32ComputerSystemUserName": win32ComputerSystemUserName,
       "win32ComputerSystemStatus": win32ComputerSystemStatus,
       "win32TapeDriveTable": win32TapeDriveTable,
       "win32TapeDriveEntry": win32TapeDriveEntry,
       "win32TapeDriveKeyIndex": win32TapeDriveKeyIndex,
       "win32TapeDriveCompression": win32TapeDriveCompression,
       "win32TapeDriveECC": win32TapeDriveECC,
       "win32TapeDriveFeaturesHigh": win32TapeDriveFeaturesHigh,
       "win32TapeDriveFeaturesLow": win32TapeDriveFeaturesLow,
       "win32TapeDriveMediaType": win32TapeDriveMediaType,
       "win32TapeDriveReportSetMarks": win32TapeDriveReportSetMarks,
       "win32TapeDriveStatus": win32TapeDriveStatus,
       "win32DiskDriveTable": win32DiskDriveTable,
       "win32DiskDriveEntry": win32DiskDriveEntry,
       "win32DiskDriveKeyIndex": win32DiskDriveKeyIndex,
       "win32DiskDriveBytesPerSector": win32DiskDriveBytesPerSector,
       "win32DiskDriveInterfaceType": win32DiskDriveInterfaceType,
       "win32DiskDrivePartitions": win32DiskDrivePartitions,
       "win32DiskDriveSectorsPerTrack": win32DiskDriveSectorsPerTrack,
       "win32DiskDriveTotalCylinders": win32DiskDriveTotalCylinders,
       "win32DiskDriveTotalHeads": win32DiskDriveTotalHeads,
       "win32DiskDriveTotalSectors": win32DiskDriveTotalSectors,
       "win32DiskDriveTotalTracks": win32DiskDriveTotalTracks,
       "win32DiskDriveTracksPerCylinder": win32DiskDriveTracksPerCylinder,
       "win32DiskDriveIndex": win32DiskDriveIndex,
       "win32DiskDriveManufacturer": win32DiskDriveManufacturer,
       "win32DiskDriveMediaLoaded": win32DiskDriveMediaLoaded,
       "win32DiskDriveMediaType": win32DiskDriveMediaType,
       "win32DiskDriveModel": win32DiskDriveModel,
       "win32DiskDriveSCSIBus": win32DiskDriveSCSIBus,
       "win32DiskDriveSCSILogicalUnit": win32DiskDriveSCSILogicalUnit,
       "win32DiskDriveSCSIPort": win32DiskDriveSCSIPort,
       "win32DiskDriveSCSITargetId": win32DiskDriveSCSITargetId,
       "win32DiskDriveSize": win32DiskDriveSize,
       "win32DiskDriveStatus": win32DiskDriveStatus,
       "win32CDROMDriveTable": win32CDROMDriveTable,
       "win32CDROMDriveEntry": win32CDROMDriveEntry,
       "win32CDROMDriveKeyIndex": win32CDROMDriveKeyIndex,
       "win32CDROMDriveDrive": win32CDROMDriveDrive,
       "win32CDROMDriveFileSystemFlags": win32CDROMDriveFileSystemFlags,
       "win32CDROMDriveId": win32CDROMDriveId,
       "win32CDROMDriveManufacturer": win32CDROMDriveManufacturer,
       "win32CDROMDriveMaximumComponentLength": win32CDROMDriveMaximumComponentLength,
       "win32CDROMDriveMediaType": win32CDROMDriveMediaType,
       "win32CDROMDriveRevisionLevel": win32CDROMDriveRevisionLevel,
       "win32CDROMDriveSCSITargetId": win32CDROMDriveSCSITargetId,
       "win32CDROMDriveVolumeName": win32CDROMDriveVolumeName,
       "win32CDROMDriveVolumeSerialNumber": win32CDROMDriveVolumeSerialNumber,
       "win32CDROMDriveTransferRate": win32CDROMDriveTransferRate,
       "win32CDROMDriveDriveIntegrity": win32CDROMDriveDriveIntegrity,
       "win32CDROMDriveMediaLoaded": win32CDROMDriveMediaLoaded,
       "win32CDROMDriveStatus": win32CDROMDriveStatus,
       "win32PointingDeviceTable": win32PointingDeviceTable,
       "win32PointingDeviceEntry": win32PointingDeviceEntry,
       "win32PointingDeviceKeyIndex": win32PointingDeviceKeyIndex,
       "win32PointingDeviceHardwareType": win32PointingDeviceHardwareType,
       "win32PointingDeviceInfFileName": win32PointingDeviceInfFileName,
       "win32PointingDeviceInfSection": win32PointingDeviceInfSection,
       "win32PointingDeviceSampleRate": win32PointingDeviceSampleRate,
       "win32PointingDeviceSynch": win32PointingDeviceSynch,
       "win32PointingDeviceDoubleSpeedThreshold": win32PointingDeviceDoubleSpeedThreshold,
       "win32PointingDeviceQuadSpeedThreshold": win32PointingDeviceQuadSpeedThreshold,
       "win32PointingDeviceStatus": win32PointingDeviceStatus,
       "win32LogicalDiskTable": win32LogicalDiskTable,
       "win32LogicalDiskEntry": win32LogicalDiskEntry,
       "win32LogicalDiskKeyIndex": win32LogicalDiskKeyIndex,
       "win32LogicalDiskCompressed": win32LogicalDiskCompressed,
       "win32LogicalDiskDriveType": win32LogicalDiskDriveType,
       "win32LogicalDiskFileSystem": win32LogicalDiskFileSystem,
       "win32LogicalDiskFreeSpace": win32LogicalDiskFreeSpace,
       "win32LogicalDiskMaximumComponentLength": win32LogicalDiskMaximumComponentLength,
       "win32LogicalDiskProviderName": win32LogicalDiskProviderName,
       "win32LogicalDiskSize": win32LogicalDiskSize,
       "win32LogicalDiskSupportsFileBasedCompression": win32LogicalDiskSupportsFileBasedCompression,
       "win32LogicalDiskVolumeName": win32LogicalDiskVolumeName,
       "win32LogicalDiskVolumeSerialNumber": win32LogicalDiskVolumeSerialNumber,
       "win32LogicalDiskMediaType": win32LogicalDiskMediaType,
       "win32LogicalDiskStatus": win32LogicalDiskStatus,
       "win32DiskPartitionTable": win32DiskPartitionTable,
       "win32DiskPartitionEntry": win32DiskPartitionEntry,
       "win32DiskPartitionKeyIndex": win32DiskPartitionKeyIndex,
       "win32DiskPartitionBootPartition": win32DiskPartitionBootPartition,
       "win32DiskPartitionDiskIndex": win32DiskPartitionDiskIndex,
       "win32DiskPartitionHiddenSectors": win32DiskPartitionHiddenSectors,
       "win32DiskPartitionIndex": win32DiskPartitionIndex,
       "win32DiskPartitionRewritePartition": win32DiskPartitionRewritePartition,
       "win32DiskPartitionSize": win32DiskPartitionSize,
       "win32DiskPartitionStartingOffset": win32DiskPartitionStartingOffset,
       "win32DiskPartitionType": win32DiskPartitionType,
       "win32DiskPartitionStatus": win32DiskPartitionStatus,
       "win32BatteryTable": win32BatteryTable,
       "win32BatteryEntry": win32BatteryEntry,
       "win32BatteryKeyIndex": win32BatteryKeyIndex,
       "win32BatteryExpectedBatteryLife": win32BatteryExpectedBatteryLife,
       "win32BatteryBatteryRechargeTime": win32BatteryBatteryRechargeTime,
       "win32BatteryBatteryStatus": win32BatteryBatteryStatus,
       "win32MotherboardDeviceTable": win32MotherboardDeviceTable,
       "win32MotherboardDeviceEntry": win32MotherboardDeviceEntry,
       "win32MotherboardDeviceKeyIndex": win32MotherboardDeviceKeyIndex,
       "win32MotherboardDevicePrimaryBusType": win32MotherboardDevicePrimaryBusType,
       "win32MotherboardDeviceRevisionNumber": win32MotherboardDeviceRevisionNumber,
       "win32MotherboardDeviceSecondaryBusType": win32MotherboardDeviceSecondaryBusType,
       "win32MotherboardDeviceStatus": win32MotherboardDeviceStatus,
       "win32ProcessorTable": win32ProcessorTable,
       "win32ProcessorEntry": win32ProcessorEntry,
       "win32ProcessorKeyIndex": win32ProcessorKeyIndex,
       "win32ProcessorVersion": win32ProcessorVersion,
       "win32ProcessorManufacturer": win32ProcessorManufacturer,
       "win32ProcessorL2CacheSize": win32ProcessorL2CacheSize,
       "win32ProcessorL2CacheSpeed": win32ProcessorL2CacheSpeed,
       "win32ProcessorArchitecture": win32ProcessorArchitecture,
       "win32ProcessorLevel": win32ProcessorLevel,
       "win32ProcessorRevision": win32ProcessorRevision,
       "win32ProcessorStatus": win32ProcessorStatus,
       "win32PrinterTable": win32PrinterTable,
       "win32PrinterEntry": win32PrinterEntry,
       "win32PrinterKeyIndex": win32PrinterKeyIndex,
       "win32PrinterAttributes": win32PrinterAttributes,
       "win32PrinterDriverName": win32PrinterDriverName,
       "win32PrinterLocation": win32PrinterLocation,
       "win32PrinterPrinterPaperNames": win32PrinterPrinterPaperNames,
       "win32PrinterPortName": win32PrinterPortName,
       "win32PrinterPrintJobDataType": win32PrinterPrintJobDataType,
       "win32PrinterSeparatorFile": win32PrinterSeparatorFile,
       "win32PrinterServerName": win32PrinterServerName,
       "win32PrinterShareName": win32PrinterShareName,
       "win32PrinterStartTime": win32PrinterStartTime,
       "win32PrinterUntilTime": win32PrinterUntilTime,
       "win32PrinterDefaultPriority": win32PrinterDefaultPriority,
       "win32PrinterAveragePagesPerMinute": win32PrinterAveragePagesPerMinute,
       "win32PrinterPrintProcessor": win32PrinterPrintProcessor,
       "win32PrinterStatus": win32PrinterStatus,
       "win32UninterruptiblePowerSupplyTable": win32UninterruptiblePowerSupplyTable,
       "win32UninterruptiblePowerSupplyEntry": win32UninterruptiblePowerSupplyEntry,
       "win32UninterruptiblePowerSupplyKeyIndex": win32UninterruptiblePowerSupplyKeyIndex,
       "win32UninterruptiblePowerSupplyBatteryInstalled": win32UninterruptiblePowerSupplyBatteryInstalled,
       "win32UninterruptiblePowerSupplyCanTurnOffRemotely": win32UninterruptiblePowerSupplyCanTurnOffRemotely,
       "win32UninterruptiblePowerSupplyCommandFile": win32UninterruptiblePowerSupplyCommandFile,
       "win32UninterruptiblePowerSupplyFirstMessageDelay": win32UninterruptiblePowerSupplyFirstMessageDelay,
       "win32UninterruptiblePowerSupplyLowBatterySignal": win32UninterruptiblePowerSupplyLowBatterySignal,
       "win32UninterruptiblePowerSupplyMessageInterval": win32UninterruptiblePowerSupplyMessageInterval,
       "win32UninterruptiblePowerSupplyPowerFailSignal": win32UninterruptiblePowerSupplyPowerFailSignal,
       "win32UninterruptiblePowerSupplyUPSPort": win32UninterruptiblePowerSupplyUPSPort,
       "win32UninterruptiblePowerSupplyStatus": win32UninterruptiblePowerSupplyStatus,
       "win32POTSModemTable": win32POTSModemTable,
       "win32POTSModemEntry": win32POTSModemEntry,
       "win32POTSModemKeyIndex": win32POTSModemKeyIndex,
       "win32POTSModemAttachedTo": win32POTSModemAttachedTo,
       "win32POTSModemBlindOff": win32POTSModemBlindOff,
       "win32POTSModemBlindOn": win32POTSModemBlindOn,
       "win32POTSModemCompatibilityFlags": win32POTSModemCompatibilityFlags,
       "win32POTSModemCompressionOff": win32POTSModemCompressionOff,
       "win32POTSModemCompressionOn": win32POTSModemCompressionOn,
       "win32POTSModemConfigurationDialog": win32POTSModemConfigurationDialog,
       "win32POTSModemDCB": win32POTSModemDCB,
       "win32POTSModemDefault": win32POTSModemDefault,
       "win32POTSModemDeviceLoader": win32POTSModemDeviceLoader,
       "win32POTSModemDeviceType": win32POTSModemDeviceType,
       "win32POTSModemDriverDate": win32POTSModemDriverDate,
       "win32POTSModemErrorControlForced": win32POTSModemErrorControlForced,
       "win32POTSModemErrorControlOff": win32POTSModemErrorControlOff,
       "win32POTSModemErrorControlOn": win32POTSModemErrorControlOn,
       "win32POTSModemFlowControlHard": win32POTSModemFlowControlHard,
       "win32POTSModemFlowControlSoft": win32POTSModemFlowControlSoft,
       "win32POTSModemFlowControlOff": win32POTSModemFlowControlOff,
       "win32POTSModemInactivityScale": win32POTSModemInactivityScale,
       "win32POTSModemIndex": win32POTSModemIndex,
       "win32POTSModemModel": win32POTSModemModel,
       "win32POTSModemModemInfPath": win32POTSModemModemInfPath,
       "win32POTSModemModemInfSection": win32POTSModemModemInfSection,
       "win32POTSModemModulationBell": win32POTSModemModulationBell,
       "win32POTSModemModulationCCITT": win32POTSModemModulationCCITT,
       "win32POTSModemPortSubClass": win32POTSModemPortSubClass,
       "win32POTSModemPrefix": win32POTSModemPrefix,
       "win32POTSModemProperties": win32POTSModemProperties,
       "win32POTSModemProviderName": win32POTSModemProviderName,
       "win32POTSModemPulse": win32POTSModemPulse,
       "win32POTSModemReset": win32POTSModemReset,
       "win32POTSModemResponsesKeyName": win32POTSModemResponsesKeyName,
       "win32POTSModemSpeakerModeDial": win32POTSModemSpeakerModeDial,
       "win32POTSModemSpeakerModeOff": win32POTSModemSpeakerModeOff,
       "win32POTSModemSpeakerModeOn": win32POTSModemSpeakerModeOn,
       "win32POTSModemSpeakerModeSetup": win32POTSModemSpeakerModeSetup,
       "win32POTSModemSpeakerVolumeHigh": win32POTSModemSpeakerVolumeHigh,
       "win32POTSModemSpeakerVolumeLow": win32POTSModemSpeakerVolumeLow,
       "win32POTSModemSpeakerVolumeMed": win32POTSModemSpeakerVolumeMed,
       "win32POTSModemStringFormat": win32POTSModemStringFormat,
       "win32POTSModemTerminator": win32POTSModemTerminator,
       "win32POTSModemTone": win32POTSModemTone,
       "win32POTSModemVoiceSwitchFeature": win32POTSModemVoiceSwitchFeature,
       "win32POTSModemStatus": win32POTSModemStatus,
       "win32SerialPortTable": win32SerialPortTable,
       "win32SerialPortEntry": win32SerialPortEntry,
       "win32SerialPortKeyIndex": win32SerialPortKeyIndex,
       "win32SerialPortBinary": win32SerialPortBinary,
       "win32SerialPortMaximumInputBufferSize": win32SerialPortMaximumInputBufferSize,
       "win32SerialPortMaximumOutputBufferSize": win32SerialPortMaximumOutputBufferSize,
       "win32SerialPortProviderType": win32SerialPortProviderType,
       "win32SerialPortSettableBaudRate": win32SerialPortSettableBaudRate,
       "win32SerialPortSettableDataBits": win32SerialPortSettableDataBits,
       "win32SerialPortSettableFlowControl": win32SerialPortSettableFlowControl,
       "win32SerialPortSettableParity": win32SerialPortSettableParity,
       "win32SerialPortSettableParityCheck": win32SerialPortSettableParityCheck,
       "win32SerialPortSettableRLSD": win32SerialPortSettableRLSD,
       "win32SerialPortSettableStopBits": win32SerialPortSettableStopBits,
       "win32SerialPortSupports16BitMode": win32SerialPortSupports16BitMode,
       "win32SerialPortSupportsDTRDSR": win32SerialPortSupportsDTRDSR,
       "win32SerialPortSupportsElapsedTimeouts": win32SerialPortSupportsElapsedTimeouts,
       "win32SerialPortSupportsIntTimeouts": win32SerialPortSupportsIntTimeouts,
       "win32SerialPortSupportsParityCheck": win32SerialPortSupportsParityCheck,
       "win32SerialPortSupportsRLSD": win32SerialPortSupportsRLSD,
       "win32SerialPortSupportsRTSCTS": win32SerialPortSupportsRTSCTS,
       "win32SerialPortSupportsSpecialCharacters": win32SerialPortSupportsSpecialCharacters,
       "win32SerialPortSupportsXOnXOff": win32SerialPortSupportsXOnXOff,
       "win32SerialPortSupportsXOnXOffSet": win32SerialPortSupportsXOnXOffSet,
       "win32SerialPortStatus": win32SerialPortStatus,
       "win32NetworkAdapterTable": win32NetworkAdapterTable,
       "win32NetworkAdapterEntry": win32NetworkAdapterEntry,
       "win32NetworkAdapterKeyIndex": win32NetworkAdapterKeyIndex,
       "win32NetworkAdapterProductName": win32NetworkAdapterProductName,
       "win32NetworkAdapterAdapterType": win32NetworkAdapterAdapterType,
       "win32NetworkAdapterMACAddress": win32NetworkAdapterMACAddress,
       "win32NetworkAdapterServiceName": win32NetworkAdapterServiceName,
       "win32NetworkAdapterManufacturer": win32NetworkAdapterManufacturer,
       "win32NetworkAdapterInstalled": win32NetworkAdapterInstalled,
       "win32NetworkAdapterIndex": win32NetworkAdapterIndex,
       "win32NetworkAdapterMaxNumberControlled": win32NetworkAdapterMaxNumberControlled,
       "win32NetworkAdapterTimeOfLastReset": win32NetworkAdapterTimeOfLastReset,
       "win32NetworkAdapterStatus": win32NetworkAdapterStatus,
       "win32SCSIControllerTable": win32SCSIControllerTable,
       "win32SCSIControllerEntry": win32SCSIControllerEntry,
       "win32SCSIControllerKeyIndex": win32SCSIControllerKeyIndex,
       "win32SCSIControllerIndex": win32SCSIControllerIndex,
       "win32SCSIControllerDriverName": win32SCSIControllerDriverName,
       "win32SCSIControllerDeviceMap": win32SCSIControllerDeviceMap,
       "win32SCSIControllerHardwareVersion": win32SCSIControllerHardwareVersion,
       "win32SCSIControllerManufacturer": win32SCSIControllerManufacturer,
       "win32SCSIControllerStatus": win32SCSIControllerStatus,
       "win32CodecFileTable": win32CodecFileTable,
       "win32CodecFileEntry": win32CodecFileEntry,
       "win32CodecFileKeyIndex": win32CodecFileKeyIndex,
       "win32CodecFileGroup": win32CodecFileGroup,
       "win32CodecFileDescription": win32CodecFileDescription,
       "win32CodecFileStatus": win32CodecFileStatus,
       "win32PageFileTable": win32PageFileTable,
       "win32PageFileEntry": win32PageFileEntry,
       "win32PageFileKeyIndex": win32PageFileKeyIndex,
       "win32PageFileName": win32PageFileName,
       "win32PageFileFreeSpace": win32PageFileFreeSpace,
       "win32PageFileInitialSize": win32PageFileInitialSize,
       "win32PageFileMaximumSize": win32PageFileMaximumSize,
       "win32PageFileStatus": win32PageFileStatus,
       "win32DriverVXDTable": win32DriverVXDTable,
       "win32DriverVXDEntry": win32DriverVXDEntry,
       "win32DriverVXDKeyIndex": win32DriverVXDKeyIndex,
       "win32DriverVXDControl": win32DriverVXDControl,
       "win32DriverVXDDeviceDescriptorBlock": win32DriverVXDDeviceDescriptorBlock,
       "win32DriverVXDPMAPI": win32DriverVXDPMAPI,
       "win32DriverVXDServiceTableSize": win32DriverVXDServiceTableSize,
       "win32DriverVXDV86API": win32DriverVXDV86API,
       "win32DriverVXDVersion": win32DriverVXDVersion,
       "win32DriverVXDStatus": win32DriverVXDStatus,
       "win32AccountTable": win32AccountTable,
       "win32AccountEntry": win32AccountEntry,
       "win32AccountKeyIndex": win32AccountKeyIndex,
       "win32AccountDomain": win32AccountDomain,
       "win32AccountSID": win32AccountSID,
       "win32AccountSIDType": win32AccountSIDType,
       "win32AccountStatus": win32AccountStatus,
       "win32SystemAccountTable": win32SystemAccountTable,
       "win32SystemAccountEntry": win32SystemAccountEntry,
       "win32SystemAccountKeyIndex": win32SystemAccountKeyIndex,
       "win32SystemAccountDomain": win32SystemAccountDomain,
       "win32SystemAccountName": win32SystemAccountName,
       "win32SystemAccountStatus": win32SystemAccountStatus,
       "win32GroupTable": win32GroupTable,
       "win32GroupEntry": win32GroupEntry,
       "win32GroupKeyIndex": win32GroupKeyIndex,
       "win32GroupDomain": win32GroupDomain,
       "win32GroupName": win32GroupName,
       "win32GroupStatus": win32GroupStatus,
       "win32UserAccountTable": win32UserAccountTable,
       "win32UserAccountEntry": win32UserAccountEntry,
       "win32UserAccountKeyIndex": win32UserAccountKeyIndex,
       "win32UserAccountAccountType": win32UserAccountAccountType,
       "win32UserAccountDisabled": win32UserAccountDisabled,
       "win32UserAccountDomain": win32UserAccountDomain,
       "win32UserAccountFullName": win32UserAccountFullName,
       "win32UserAccountLockout": win32UserAccountLockout,
       "win32UserAccountName": win32UserAccountName,
       "win32UserAccountPasswordChangeable": win32UserAccountPasswordChangeable,
       "win32UserAccountPasswordExpires": win32UserAccountPasswordExpires,
       "win32UserAccountPasswordRequired": win32UserAccountPasswordRequired,
       "win32UserAccountStatus": win32UserAccountStatus,
       "win32NetworkConnectionTable": win32NetworkConnectionTable,
       "win32NetworkConnectionEntry": win32NetworkConnectionEntry,
       "win32NetworkConnectionKeyIndex": win32NetworkConnectionKeyIndex,
       "win32NetworkConnectionComment": win32NetworkConnectionComment,
       "win32NetworkConnectionConnectionType": win32NetworkConnectionConnectionType,
       "win32NetworkConnectionDisplayType": win32NetworkConnectionDisplayType,
       "win32NetworkConnectionLocalName": win32NetworkConnectionLocalName,
       "win32NetworkConnectionName": win32NetworkConnectionName,
       "win32NetworkConnectionPersistent": win32NetworkConnectionPersistent,
       "win32NetworkConnectionProviderName": win32NetworkConnectionProviderName,
       "win32NetworkConnectionRemoteName": win32NetworkConnectionRemoteName,
       "win32NetworkConnectionRemotePath": win32NetworkConnectionRemotePath,
       "win32NetworkConnectionResourceType": win32NetworkConnectionResourceType,
       "win32NetworkConnectionUserName": win32NetworkConnectionUserName,
       "win32NetworkConnectionStatus": win32NetworkConnectionStatus,
       "win32DeviceMemoryAddressTable": win32DeviceMemoryAddressTable,
       "win32DeviceMemoryAddressEntry": win32DeviceMemoryAddressEntry,
       "win32DeviceMemoryAddressKeyIndex": win32DeviceMemoryAddressKeyIndex,
       "win32DeviceMemoryAddressMemoryType": win32DeviceMemoryAddressMemoryType,
       "win32DeviceMemoryAddressStatus": win32DeviceMemoryAddressStatus,
       "win32PortResourceTable": win32PortResourceTable,
       "win32PortResourceEntry": win32PortResourceEntry,
       "win32PortResourceKeyIndex": win32PortResourceKeyIndex,
       "win32PortResourceAlias": win32PortResourceAlias,
       "win32PortResourceStatus": win32PortResourceStatus,
       "win32DMAChannelTable": win32DMAChannelTable,
       "win32DMAChannelEntry": win32DMAChannelEntry,
       "win32DMAChannelKeyIndex": win32DMAChannelKeyIndex,
       "win32DMAChannelPort": win32DMAChannelPort,
       "win32DMAChannelStatus": win32DMAChannelStatus,
       "win32EnvironmentTable": win32EnvironmentTable,
       "win32EnvironmentEntry": win32EnvironmentEntry,
       "win32EnvironmentKeyIndex": win32EnvironmentKeyIndex,
       "win32EnvironmentName": win32EnvironmentName,
       "win32EnvironmentSystemVariable": win32EnvironmentSystemVariable,
       "win32EnvironmentUserName": win32EnvironmentUserName,
       "win32EnvironmentVariableValue": win32EnvironmentVariableValue,
       "win32EnvironmentStatus": win32EnvironmentStatus,
       "win32IRQResourceTable": win32IRQResourceTable,
       "win32IRQResourceEntry": win32IRQResourceEntry,
       "win32IRQResourceKeyIndex": win32IRQResourceKeyIndex,
       "win32IRQResourceVector": win32IRQResourceVector,
       "win32IRQResourceHardware": win32IRQResourceHardware,
       "win32IRQResourceStatus": win32IRQResourceStatus,
       "win32LoadOrderGroupTable": win32LoadOrderGroupTable,
       "win32LoadOrderGroupEntry": win32LoadOrderGroupEntry,
       "win32LoadOrderGroupKeyIndex": win32LoadOrderGroupKeyIndex,
       "win32LoadOrderGroupGroupOrder": win32LoadOrderGroupGroupOrder,
       "win32LoadOrderGroupName": win32LoadOrderGroupName,
       "win32LoadOrderGroupDriverEnabled": win32LoadOrderGroupDriverEnabled,
       "win32LoadOrderGroupStatus": win32LoadOrderGroupStatus,
       "win32NetworkClientTable": win32NetworkClientTable,
       "win32NetworkClientEntry": win32NetworkClientEntry,
       "win32NetworkClientKeyIndex": win32NetworkClientKeyIndex,
       "win32NetworkClientManufacturer": win32NetworkClientManufacturer,
       "win32NetworkClientName": win32NetworkClientName,
       "win32NetworkClientStatus": win32NetworkClientStatus,
       "win32ShareTable": win32ShareTable,
       "win32ShareEntry": win32ShareEntry,
       "win32ShareKeyIndex": win32ShareKeyIndex,
       "win32ShareAllowMaximum": win32ShareAllowMaximum,
       "win32ShareMaximumAllowed": win32ShareMaximumAllowed,
       "win32ShareName": win32ShareName,
       "win32SharePath": win32SharePath,
       "win32ShareType": win32ShareType,
       "win32ShareStatus": win32ShareStatus,
       "win32RegistryTable": win32RegistryTable,
       "win32RegistryEntry": win32RegistryEntry,
       "win32RegistryKeyIndex": win32RegistryKeyIndex,
       "win32RegistryCurrentSize": win32RegistryCurrentSize,
       "win32RegistryProposedSize": win32RegistryProposedSize,
       "win32RegistryMaximumSize": win32RegistryMaximumSize,
       "win32RegistryName": win32RegistryName,
       "win32RegistryStatus": win32RegistryStatus,
       "win32NetworkProtocolTable": win32NetworkProtocolTable,
       "win32NetworkProtocolEntry": win32NetworkProtocolEntry,
       "win32NetworkProtocolKeyIndex": win32NetworkProtocolKeyIndex,
       "win32NetworkProtocolConnectionlessService": win32NetworkProtocolConnectionlessService,
       "win32NetworkProtocolGuranteesDelivery": win32NetworkProtocolGuranteesDelivery,
       "win32NetworkProtocolGuranteesSequencing": win32NetworkProtocolGuranteesSequencing,
       "win32NetworkProtocolMaximumAddressSize": win32NetworkProtocolMaximumAddressSize,
       "win32NetworkProtocolMaximumMessageSize": win32NetworkProtocolMaximumMessageSize,
       "win32NetworkProtocolMessageOriented": win32NetworkProtocolMessageOriented,
       "win32NetworkProtocolMinimumAddressSize": win32NetworkProtocolMinimumAddressSize,
       "win32NetworkProtocolName": win32NetworkProtocolName,
       "win32NetworkProtocolPseudoStreamOriented": win32NetworkProtocolPseudoStreamOriented,
       "win32NetworkProtocolSupportsBroadcasting": win32NetworkProtocolSupportsBroadcasting,
       "win32NetworkProtocolSupportsConnectData": win32NetworkProtocolSupportsConnectData,
       "win32NetworkProtocolSupportsDisconnectData": win32NetworkProtocolSupportsDisconnectData,
       "win32NetworkProtocolSupportsEncryption": win32NetworkProtocolSupportsEncryption,
       "win32NetworkProtocolSupportsExpiditeData": win32NetworkProtocolSupportsExpiditeData,
       "win32NetworkProtocolSupportsFragmentation": win32NetworkProtocolSupportsFragmentation,
       "win32NetworkProtocolSupportsGracefulClosing": win32NetworkProtocolSupportsGracefulClosing,
       "win32NetworkProtocolSupportsGuaranteedBandwidth": win32NetworkProtocolSupportsGuaranteedBandwidth,
       "win32NetworkProtocolSupportsMulticasting": win32NetworkProtocolSupportsMulticasting,
       "win32NetworkProtocolStatus": win32NetworkProtocolStatus,
       "win32ProcessStartupTable": win32ProcessStartupTable,
       "win32ProcessStartupEntry": win32ProcessStartupEntry,
       "win32ProcessStartupKeyIndex": win32ProcessStartupKeyIndex,
       "win32ProcessStartupCreateFlags": win32ProcessStartupCreateFlags,
       "win32ProcessStartupPriorityClass": win32ProcessStartupPriorityClass,
       "win32ProcessStartupWinstationDesktop": win32ProcessStartupWinstationDesktop,
       "win32ProcessStartupTitle": win32ProcessStartupTitle,
       "win32ProcessStartupX": win32ProcessStartupX,
       "win32ProcessStartupY": win32ProcessStartupY,
       "win32ProcessStartupXSize": win32ProcessStartupXSize,
       "win32ProcessStartupYSize": win32ProcessStartupYSize,
       "win32ProcessStartupXCountChars": win32ProcessStartupXCountChars,
       "win32ProcessStartupYCountChars": win32ProcessStartupYCountChars,
       "win32ProcessStartupFillAttribute": win32ProcessStartupFillAttribute,
       "win32ProcessStartupShowWindow": win32ProcessStartupShowWindow,
       "win32ProcessStartupErrorMode": win32ProcessStartupErrorMode,
       "win32ProcessStartupStatus": win32ProcessStartupStatus,
       "win32ProcessTable": win32ProcessTable,
       "win32ProcessEntry": win32ProcessEntry,
       "win32ProcessKeyIndex": win32ProcessKeyIndex,
       "win32ProcessExecutablePath": win32ProcessExecutablePath,
       "win32ProcessMaximumWorkingSetSize": win32ProcessMaximumWorkingSetSize,
       "win32ProcessMinimumWorkingSetSize": win32ProcessMinimumWorkingSetSize,
       "win32ProcessPageFaults": win32ProcessPageFaults,
       "win32ProcessPageFileUsage": win32ProcessPageFileUsage,
       "win32ProcessPeakWorkingSetSize": win32ProcessPeakWorkingSetSize,
       "win32ProcessProcessId": win32ProcessProcessId,
       "win32ProcessQuotaNonPagedPoolUsage": win32ProcessQuotaNonPagedPoolUsage,
       "win32ProcessQuotaPagedPoolUsage": win32ProcessQuotaPagedPoolUsage,
       "win32ProcessQuotaPeakNonPagedPoolUsage": win32ProcessQuotaPeakNonPagedPoolUsage,
       "win32ProcessQuotaPeakPagedPoolUsage": win32ProcessQuotaPeakPagedPoolUsage,
       "win32ProcessWindowsVersion": win32ProcessWindowsVersion,
       "win32ProcessStatus": win32ProcessStatus,
       "win32ThreadTable": win32ThreadTable,
       "win32ThreadEntry": win32ThreadEntry,
       "win32ThreadKeyIndex": win32ThreadKeyIndex,
       "win32ThreadProcessHandle": win32ThreadProcessHandle,
       "win32ThreadHandle": win32ThreadHandle,
       "win32ThreadElapsedTime": win32ThreadElapsedTime,
       "win32ThreadPriorityBase": win32ThreadPriorityBase,
       "win32ThreadPriority": win32ThreadPriority,
       "win32ThreadStartAddress": win32ThreadStartAddress,
       "win32ThreadThreadState": win32ThreadThreadState,
       "win32ThreadThreadWaitReason": win32ThreadThreadWaitReason,
       "win32ThreadStatus": win32ThreadStatus,
       "win32OperatingSystemTable": win32OperatingSystemTable,
       "win32OperatingSystemEntry": win32OperatingSystemEntry,
       "win32OperatingSystemKeyIndex": win32OperatingSystemKeyIndex,
       "win32OperatingSystemBootDevice": win32OperatingSystemBootDevice,
       "win32OperatingSystemBuildNumber": win32OperatingSystemBuildNumber,
       "win32OperatingSystemBuildType": win32OperatingSystemBuildType,
       "win32OperatingSystemCodeSet": win32OperatingSystemCodeSet,
       "win32OperatingSystemCountryCode": win32OperatingSystemCountryCode,
       "win32OperatingSystemCSDVersion": win32OperatingSystemCSDVersion,
       "win32OperatingSystemDebug": win32OperatingSystemDebug,
       "win32OperatingSystemForegroundApplicationBoost": win32OperatingSystemForegroundApplicationBoost,
       "win32OperatingSystemLocale": win32OperatingSystemLocale,
       "win32OperatingSystemManufacturer": win32OperatingSystemManufacturer,
       "win32OperatingSystemOrganization": win32OperatingSystemOrganization,
       "win32OperatingSystemOSLanguage": win32OperatingSystemOSLanguage,
       "win32OperatingSystemPlusProductID": win32OperatingSystemPlusProductID,
       "win32OperatingSystemPlusVersionNumber": win32OperatingSystemPlusVersionNumber,
       "win32OperatingSystemPrimary": win32OperatingSystemPrimary,
       "win32OperatingSystemQuantumLength": win32OperatingSystemQuantumLength,
       "win32OperatingSystemQuantumType": win32OperatingSystemQuantumType,
       "win32OperatingSystemRegisteredUser": win32OperatingSystemRegisteredUser,
       "win32OperatingSystemSerialNumber": win32OperatingSystemSerialNumber,
       "win32OperatingSystemSystemDevice": win32OperatingSystemSystemDevice,
       "win32OperatingSystemSystemDirectory": win32OperatingSystemSystemDirectory,
       "win32OperatingSystemVersion": win32OperatingSystemVersion,
       "win32OperatingSystemWindowsDirectory": win32OperatingSystemWindowsDirectory,
       "win32OperatingSystemDescription": win32OperatingSystemDescription,
       "win32OperatingSystemStatus": win32OperatingSystemStatus,
       "win32PrintJobTable": win32PrintJobTable,
       "win32PrintJobEntry": win32PrintJobEntry,
       "win32PrintJobKeyIndex": win32PrintJobKeyIndex,
       "win32PrintJobName": win32PrintJobName,
       "win32PrintJobDataType": win32PrintJobDataType,
       "win32PrintJobDocument": win32PrintJobDocument,
       "win32PrintJobDriverName": win32PrintJobDriverName,
       "win32PrintJobHostPrintQueue": win32PrintJobHostPrintQueue,
       "win32PrintJobJobId": win32PrintJobJobId,
       "win32PrintJobPagesPrinted": win32PrintJobPagesPrinted,
       "win32PrintJobParameters": win32PrintJobParameters,
       "win32PrintJobPrintProcessor": win32PrintJobPrintProcessor,
       "win32PrintJobSize": win32PrintJobSize,
       "win32PrintJobTotalPages": win32PrintJobTotalPages,
       "win32PrintJobStatus": win32PrintJobStatus,
       "win32ScheduledJobTable": win32ScheduledJobTable,
       "win32ScheduledJobEntry": win32ScheduledJobEntry,
       "win32ScheduledJobKeyIndex": win32ScheduledJobKeyIndex,
       "win32ScheduledJobJobId": win32ScheduledJobJobId,
       "win32ScheduledJobCommand": win32ScheduledJobCommand,
       "win32ScheduledJobStartTime": win32ScheduledJobStartTime,
       "win32ScheduledJobRunRepeatedly": win32ScheduledJobRunRepeatedly,
       "win32ScheduledJobInteractWithDesktop": win32ScheduledJobInteractWithDesktop,
       "win32ScheduledJobDaysOfWeek": win32ScheduledJobDaysOfWeek,
       "win32ScheduledJobDaysOfMonth": win32ScheduledJobDaysOfMonth,
       "win32ScheduledJobJobStatus": win32ScheduledJobJobStatus,
       "win32ScheduledJobStatus": win32ScheduledJobStatus,
       "win32BIOSTable": win32BIOSTable,
       "win32BIOSEntry": win32BIOSEntry,
       "win32BIOSKeyIndex": win32BIOSKeyIndex,
       "win32BIOSReleaseDate": win32BIOSReleaseDate,
       "win32BIOSVersion": win32BIOSVersion,
       "win32BIOSStatus": win32BIOSStatus,
       "win32BootConfigurationTable": win32BootConfigurationTable,
       "win32BootConfigurationEntry": win32BootConfigurationEntry,
       "win32BootConfigurationKeyIndex": win32BootConfigurationKeyIndex,
       "win32BootConfigurationBootDirectory": win32BootConfigurationBootDirectory,
       "win32BootConfigurationConfigurationPath": win32BootConfigurationConfigurationPath,
       "win32BootConfigurationLastDrive": win32BootConfigurationLastDrive,
       "win32BootConfigurationName": win32BootConfigurationName,
       "win32BootConfigurationScratchDirectory": win32BootConfigurationScratchDirectory,
       "win32BootConfigurationTempDirectory": win32BootConfigurationTempDirectory,
       "win32DesktopTable": win32DesktopTable,
       "win32DesktopEntry": win32DesktopEntry,
       "win32DesktopKeyIndex": win32DesktopKeyIndex,
       "win32DesktopBorderWidth": win32DesktopBorderWidth,
       "win32DesktopCoolSwitch": win32DesktopCoolSwitch,
       "win32DesktopCursorBlinkRate": win32DesktopCursorBlinkRate,
       "win32DesktopDragFullWindows": win32DesktopDragFullWindows,
       "win32DesktopGridGranularity": win32DesktopGridGranularity,
       "win32DesktopIconSpacing": win32DesktopIconSpacing,
       "win32DesktopIconTitleFaceName": win32DesktopIconTitleFaceName,
       "win32DesktopIconTitleSize": win32DesktopIconTitleSize,
       "win32DesktopIconTitleWrap": win32DesktopIconTitleWrap,
       "win32DesktopName": win32DesktopName,
       "win32DesktopPattern": win32DesktopPattern,
       "win32DesktopScreenSaverActive": win32DesktopScreenSaverActive,
       "win32DesktopScreenSaverExecutable": win32DesktopScreenSaverExecutable,
       "win32DesktopScreenSaverSecure": win32DesktopScreenSaverSecure,
       "win32DesktopScreenSaverTimeout": win32DesktopScreenSaverTimeout,
       "win32DesktopWallpaper": win32DesktopWallpaper,
       "win32DesktopWallpaperTiled": win32DesktopWallpaperTiled,
       "win32DesktopWallpaperStretched": win32DesktopWallpaperStretched,
       "win32DisplayConfigurationTable": win32DisplayConfigurationTable,
       "win32DisplayConfigurationEntry": win32DisplayConfigurationEntry,
       "win32DisplayConfigurationKeyIndex": win32DisplayConfigurationKeyIndex,
       "win32DisplayConfigurationBitsPerPel": win32DisplayConfigurationBitsPerPel,
       "win32DisplayConfigurationDeviceName": win32DisplayConfigurationDeviceName,
       "win32DisplayConfigurationDisplayFlags": win32DisplayConfigurationDisplayFlags,
       "win32DisplayConfigurationDisplayFrequency": win32DisplayConfigurationDisplayFrequency,
       "win32DisplayConfigurationDitherType": win32DisplayConfigurationDitherType,
       "win32DisplayConfigurationDriverVersion": win32DisplayConfigurationDriverVersion,
       "win32DisplayConfigurationICMIntent": win32DisplayConfigurationICMIntent,
       "win32DisplayConfigurationICMMethod": win32DisplayConfigurationICMMethod,
       "win32DisplayConfigurationLogPixels": win32DisplayConfigurationLogPixels,
       "win32DisplayConfigurationPelsHeight": win32DisplayConfigurationPelsHeight,
       "win32DisplayConfigurationPelsWidth": win32DisplayConfigurationPelsWidth,
       "win32DisplayConfigurationSpecificationVersion": win32DisplayConfigurationSpecificationVersion,
       "win32DisplayControllerConfigurationTable": win32DisplayControllerConfigurationTable,
       "win32DisplayControllerConfigurationEntry": win32DisplayControllerConfigurationEntry,
       "win32DisplayControllerConfigurationKeyIndex": win32DisplayControllerConfigurationKeyIndex,
       "win32DisplayControllerConfigurationBitsPerPixel": win32DisplayControllerConfigurationBitsPerPixel,
       "win32DisplayControllerConfigurationColorPlanes": win32DisplayControllerConfigurationColorPlanes,
       "win32DisplayControllerConfigurationDeviceEntriesInAColorTable": win32DisplayControllerConfigurationDeviceEntriesInAColorTable,
       "win32DisplayControllerConfigurationDeviceSpecificPens": win32DisplayControllerConfigurationDeviceSpecificPens,
       "win32DisplayControllerConfigurationHorizontalResolution": win32DisplayControllerConfigurationHorizontalResolution,
       "win32DisplayControllerConfigurationName": win32DisplayControllerConfigurationName,
       "win32DisplayControllerConfigurationRefreshRate": win32DisplayControllerConfigurationRefreshRate,
       "win32DisplayControllerConfigurationReservedSystemPaletteEntries": win32DisplayControllerConfigurationReservedSystemPaletteEntries,
       "win32DisplayControllerConfigurationSystemPaletteEntries": win32DisplayControllerConfigurationSystemPaletteEntries,
       "win32DisplayControllerConfigurationVerticalResolution": win32DisplayControllerConfigurationVerticalResolution,
       "win32DisplayControllerConfigurationVideoMode": win32DisplayControllerConfigurationVideoMode,
       "win32LogicalMemoryConfigurationTable": win32LogicalMemoryConfigurationTable,
       "win32LogicalMemoryConfigurationEntry": win32LogicalMemoryConfigurationEntry,
       "win32LogicalMemoryConfigurationKeyIndex": win32LogicalMemoryConfigurationKeyIndex,
       "win32LogicalMemoryConfigurationAvailableVirtualMemory": win32LogicalMemoryConfigurationAvailableVirtualMemory,
       "win32LogicalMemoryConfigurationName": win32LogicalMemoryConfigurationName,
       "win32LogicalMemoryConfigurationTotalPageFileSpace": win32LogicalMemoryConfigurationTotalPageFileSpace,
       "win32LogicalMemoryConfigurationTotalPhysicalMemory": win32LogicalMemoryConfigurationTotalPhysicalMemory,
       "win32LogicalMemoryConfigurationTotalVirtualMemory": win32LogicalMemoryConfigurationTotalVirtualMemory,
       "win32NetworkLoginProfileTable": win32NetworkLoginProfileTable,
       "win32NetworkLoginProfileEntry": win32NetworkLoginProfileEntry,
       "win32NetworkLoginProfileKeyIndex": win32NetworkLoginProfileKeyIndex,
       "win32NetworkLoginProfileAccountExpires": win32NetworkLoginProfileAccountExpires,
       "win32NetworkLoginProfileAuthorizationFlags": win32NetworkLoginProfileAuthorizationFlags,
       "win32NetworkLoginProfileBadPasswordCount": win32NetworkLoginProfileBadPasswordCount,
       "win32NetworkLoginProfileCodePage": win32NetworkLoginProfileCodePage,
       "win32NetworkLoginProfileComment": win32NetworkLoginProfileComment,
       "win32NetworkLoginProfileCountryCode": win32NetworkLoginProfileCountryCode,
       "win32NetworkLoginProfileFlags": win32NetworkLoginProfileFlags,
       "win32NetworkLoginProfileFullName": win32NetworkLoginProfileFullName,
       "win32NetworkLoginProfileHomeDirectory": win32NetworkLoginProfileHomeDirectory,
       "win32NetworkLoginProfileHomeDirectoryDrive": win32NetworkLoginProfileHomeDirectoryDrive,
       "win32NetworkLoginProfileLastLogoff": win32NetworkLoginProfileLastLogoff,
       "win32NetworkLoginProfileLastLogon": win32NetworkLoginProfileLastLogon,
       "win32NetworkLoginProfileLogonHours": win32NetworkLoginProfileLogonHours,
       "win32NetworkLoginProfileLogonServer": win32NetworkLoginProfileLogonServer,
       "win32NetworkLoginProfileMaximumStorage": win32NetworkLoginProfileMaximumStorage,
       "win32NetworkLoginProfileName": win32NetworkLoginProfileName,
       "win32NetworkLoginProfileNumberOfLogons": win32NetworkLoginProfileNumberOfLogons,
       "win32NetworkLoginProfileParameters": win32NetworkLoginProfileParameters,
       "win32NetworkLoginProfilePasswordAge": win32NetworkLoginProfilePasswordAge,
       "win32NetworkLoginProfilePasswordExpires": win32NetworkLoginProfilePasswordExpires,
       "win32NetworkLoginProfilePrimaryGroupId": win32NetworkLoginProfilePrimaryGroupId,
       "win32NetworkLoginProfilePrivileges": win32NetworkLoginProfilePrivileges,
       "win32NetworkLoginProfileProfile": win32NetworkLoginProfileProfile,
       "win32NetworkLoginProfileScriptPath": win32NetworkLoginProfileScriptPath,
       "win32NetworkLoginProfileUnitsPerWeek": win32NetworkLoginProfileUnitsPerWeek,
       "win32NetworkLoginProfileUserComment": win32NetworkLoginProfileUserComment,
       "win32NetworkLoginProfileUserId": win32NetworkLoginProfileUserId,
       "win32NetworkLoginProfileUserType": win32NetworkLoginProfileUserType,
       "win32NetworkLoginProfileWorkstations": win32NetworkLoginProfileWorkstations,
       "win32OSRecoveryConfigurationTable": win32OSRecoveryConfigurationTable,
       "win32OSRecoveryConfigurationEntry": win32OSRecoveryConfigurationEntry,
       "win32OSRecoveryConfigurationKeyIndex": win32OSRecoveryConfigurationKeyIndex,
       "win32OSRecoveryConfigurationAutoReboot": win32OSRecoveryConfigurationAutoReboot,
       "win32OSRecoveryConfigurationDebugFilePath": win32OSRecoveryConfigurationDebugFilePath,
       "win32OSRecoveryConfigurationName": win32OSRecoveryConfigurationName,
       "win32OSRecoveryConfigurationOverwriteExistingDebugFile": win32OSRecoveryConfigurationOverwriteExistingDebugFile,
       "win32OSRecoveryConfigurationSendAdminAlert": win32OSRecoveryConfigurationSendAdminAlert,
       "win32OSRecoveryConfigurationWriteDebugInfo": win32OSRecoveryConfigurationWriteDebugInfo,
       "win32OSRecoveryConfigurationWriteToSystemLog": win32OSRecoveryConfigurationWriteToSystemLog,
       "win32PrinterConfigurationTable": win32PrinterConfigurationTable,
       "win32PrinterConfigurationEntry": win32PrinterConfigurationEntry,
       "win32PrinterConfigurationKeyIndex": win32PrinterConfigurationKeyIndex,
       "win32PrinterConfigurationBitsPerPel": win32PrinterConfigurationBitsPerPel,
       "win32PrinterConfigurationCollate": win32PrinterConfigurationCollate,
       "win32PrinterConfigurationColor": win32PrinterConfigurationColor,
       "win32PrinterConfigurationCopies": win32PrinterConfigurationCopies,
       "win32PrinterConfigurationDeviceName": win32PrinterConfigurationDeviceName,
       "win32PrinterConfigurationDisplayFlags": win32PrinterConfigurationDisplayFlags,
       "win32PrinterConfigurationDisplayFrequency": win32PrinterConfigurationDisplayFrequency,
       "win32PrinterConfigurationDitherType": win32PrinterConfigurationDitherType,
       "win32PrinterConfigurationDriverVersion": win32PrinterConfigurationDriverVersion,
       "win32PrinterConfigurationDuplex": win32PrinterConfigurationDuplex,
       "win32PrinterConfigurationFormName": win32PrinterConfigurationFormName,
       "win32PrinterConfigurationICMIntent": win32PrinterConfigurationICMIntent,
       "win32PrinterConfigurationICMMethod": win32PrinterConfigurationICMMethod,
       "win32PrinterConfigurationLogPixels": win32PrinterConfigurationLogPixels,
       "win32PrinterConfigurationMediaType": win32PrinterConfigurationMediaType,
       "win32PrinterConfigurationName": win32PrinterConfigurationName,
       "win32PrinterConfigurationOrientation": win32PrinterConfigurationOrientation,
       "win32PrinterConfigurationPaperLength": win32PrinterConfigurationPaperLength,
       "win32PrinterConfigurationPaperSize": win32PrinterConfigurationPaperSize,
       "win32PrinterConfigurationPaperWidth": win32PrinterConfigurationPaperWidth,
       "win32PrinterConfigurationPelsHeight": win32PrinterConfigurationPelsHeight,
       "win32PrinterConfigurationPelsWidth": win32PrinterConfigurationPelsWidth,
       "win32PrinterConfigurationPrintQuality": win32PrinterConfigurationPrintQuality,
       "win32PrinterConfigurationScale": win32PrinterConfigurationScale,
       "win32PrinterConfigurationSpecificationVersion": win32PrinterConfigurationSpecificationVersion,
       "win32PrinterConfigurationTTOption": win32PrinterConfigurationTTOption,
       "win32PrinterConfigurationXResolution": win32PrinterConfigurationXResolution,
       "win32PrinterConfigurationYResolution": win32PrinterConfigurationYResolution,
       "win32ProgramGroupTable": win32ProgramGroupTable,
       "win32ProgramGroupEntry": win32ProgramGroupEntry,
       "win32ProgramGroupKeyIndex": win32ProgramGroupKeyIndex,
       "win32ProgramGroupGroupName": win32ProgramGroupGroupName,
       "win32ProgramGroupName": win32ProgramGroupName,
       "win32ProgramGroupUserName": win32ProgramGroupUserName,
       "win32SerialPortConfigurationTable": win32SerialPortConfigurationTable,
       "win32SerialPortConfigurationEntry": win32SerialPortConfigurationEntry,
       "win32SerialPortConfigurationKeyIndex": win32SerialPortConfigurationKeyIndex,
       "win32SerialPortConfigurationAbortReadWriteOnError": win32SerialPortConfigurationAbortReadWriteOnError,
       "win32SerialPortConfigurationBaudRate": win32SerialPortConfigurationBaudRate,
       "win32SerialPortConfigurationBinaryModeEnabled": win32SerialPortConfigurationBinaryModeEnabled,
       "win32SerialPortConfigurationBitsPerByte": win32SerialPortConfigurationBitsPerByte,
       "win32SerialPortConfigurationContinueXMitOnXOff": win32SerialPortConfigurationContinueXMitOnXOff,
       "win32SerialPortConfigurationCTSOutflowControl": win32SerialPortConfigurationCTSOutflowControl,
       "win32SerialPortConfigurationDiscardNULLBytes": win32SerialPortConfigurationDiscardNULLBytes,
       "win32SerialPortConfigurationDSROutflowControl": win32SerialPortConfigurationDSROutflowControl,
       "win32SerialPortConfigurationDSRSensitivity": win32SerialPortConfigurationDSRSensitivity,
       "win32SerialPortConfigurationDTRFlowControlType": win32SerialPortConfigurationDTRFlowControlType,
       "win32SerialPortConfigurationEOFCharacter": win32SerialPortConfigurationEOFCharacter,
       "win32SerialPortConfigurationErrorReplaceCharacter": win32SerialPortConfigurationErrorReplaceCharacter,
       "win32SerialPortConfigurationErrorReplacementEnabled": win32SerialPortConfigurationErrorReplacementEnabled,
       "win32SerialPortConfigurationEventCharacter": win32SerialPortConfigurationEventCharacter,
       "win32SerialPortConfigurationIsBusy": win32SerialPortConfigurationIsBusy,
       "win32SerialPortConfigurationName": win32SerialPortConfigurationName,
       "win32SerialPortConfigurationParity": win32SerialPortConfigurationParity,
       "win32SerialPortConfigurationParityCheckEnabled": win32SerialPortConfigurationParityCheckEnabled,
       "win32SerialPortConfigurationRTSFlowControlType": win32SerialPortConfigurationRTSFlowControlType,
       "win32SerialPortConfigurationStopBits": win32SerialPortConfigurationStopBits,
       "win32SerialPortConfigurationXOffCharacter": win32SerialPortConfigurationXOffCharacter,
       "win32SerialPortConfigurationXOffXMitThreshold": win32SerialPortConfigurationXOffXMitThreshold,
       "win32SerialPortConfigurationXOnCharacter": win32SerialPortConfigurationXOnCharacter,
       "win32SerialPortConfigurationXOnXMitThreshold": win32SerialPortConfigurationXOnXMitThreshold,
       "win32SerialPortConfigurationXOnXOffInFlowControl": win32SerialPortConfigurationXOnXOffInFlowControl,
       "win32SerialPortConfigurationXOnXOffOutFlowControl": win32SerialPortConfigurationXOnXOffOutFlowControl,
       "win32TimeZoneTable": win32TimeZoneTable,
       "win32TimeZoneEntry": win32TimeZoneEntry,
       "win32TimeZoneKeyIndex": win32TimeZoneKeyIndex,
       "win32TimeZoneBias": win32TimeZoneBias,
       "win32TimeZoneDaylightBias": win32TimeZoneDaylightBias,
       "win32TimeZoneDaylightDay": win32TimeZoneDaylightDay,
       "win32TimeZoneDaylightDayOfWeek": win32TimeZoneDaylightDayOfWeek,
       "win32TimeZoneDaylightHour": win32TimeZoneDaylightHour,
       "win32TimeZoneDaylightMillisecond": win32TimeZoneDaylightMillisecond,
       "win32TimeZoneDaylightMinute": win32TimeZoneDaylightMinute,
       "win32TimeZoneDaylightMonth": win32TimeZoneDaylightMonth,
       "win32TimeZoneDaylightName": win32TimeZoneDaylightName,
       "win32TimeZoneDaylightSecond": win32TimeZoneDaylightSecond,
       "win32TimeZoneDaylightYear": win32TimeZoneDaylightYear,
       "win32TimeZoneStandardBias": win32TimeZoneStandardBias,
       "win32TimeZoneStandardDay": win32TimeZoneStandardDay,
       "win32TimeZoneStandardDayOfWeek": win32TimeZoneStandardDayOfWeek,
       "win32TimeZoneStandardHour": win32TimeZoneStandardHour,
       "win32TimeZoneStandardMillisecond": win32TimeZoneStandardMillisecond,
       "win32TimeZoneStandardMinute": win32TimeZoneStandardMinute,
       "win32TimeZoneStandardMonth": win32TimeZoneStandardMonth,
       "win32TimeZoneStandardName": win32TimeZoneStandardName,
       "win32TimeZoneStandardSecond": win32TimeZoneStandardSecond,
       "win32TimeZoneStandardYear": win32TimeZoneStandardYear,
       "win32VideoConfigurationTable": win32VideoConfigurationTable,
       "win32VideoConfigurationEntry": win32VideoConfigurationEntry,
       "win32VideoConfigurationKeyIndex": win32VideoConfigurationKeyIndex,
       "win32VideoConfigurationActualColorResolution": win32VideoConfigurationActualColorResolution,
       "win32VideoConfigurationAdapterChipType": win32VideoConfigurationAdapterChipType,
       "win32VideoConfigurationAdapterCompatibility": win32VideoConfigurationAdapterCompatibility,
       "win32VideoConfigurationAdapterDACType": win32VideoConfigurationAdapterDACType,
       "win32VideoConfigurationAdapterDescription": win32VideoConfigurationAdapterDescription,
       "win32VideoConfigurationAdapterRAM": win32VideoConfigurationAdapterRAM,
       "win32VideoConfigurationAdapterType": win32VideoConfigurationAdapterType,
       "win32VideoConfigurationBitsPerPixel": win32VideoConfigurationBitsPerPixel,
       "win32VideoConfigurationColorPlanes": win32VideoConfigurationColorPlanes,
       "win32VideoConfigurationColorTableEntries": win32VideoConfigurationColorTableEntries,
       "win32VideoConfigurationDeviceSpecificPens": win32VideoConfigurationDeviceSpecificPens,
       "win32VideoConfigurationDriverDate": win32VideoConfigurationDriverDate,
       "win32VideoConfigurationHorizontalResolution": win32VideoConfigurationHorizontalResolution,
       "win32VideoConfigurationInfFilename": win32VideoConfigurationInfFilename,
       "win32VideoConfigurationInfSection": win32VideoConfigurationInfSection,
       "win32VideoConfigurationInstalledDisplayDrivers": win32VideoConfigurationInstalledDisplayDrivers,
       "win32VideoConfigurationMonitorManufacturer": win32VideoConfigurationMonitorManufacturer,
       "win32VideoConfigurationMonitorType": win32VideoConfigurationMonitorType,
       "win32VideoConfigurationName": win32VideoConfigurationName,
       "win32VideoConfigurationPixelsPerXLogicalInch": win32VideoConfigurationPixelsPerXLogicalInch,
       "win32VideoConfigurationPixelsPerYLogicalInch": win32VideoConfigurationPixelsPerYLogicalInch,
       "win32VideoConfigurationRefreshRate": win32VideoConfigurationRefreshRate,
       "win32VideoConfigurationScanMode": win32VideoConfigurationScanMode,
       "win32VideoConfigurationScreenHeight": win32VideoConfigurationScreenHeight,
       "win32VideoConfigurationScreenWidth": win32VideoConfigurationScreenWidth,
       "win32VideoConfigurationSystemPaletteEntries": win32VideoConfigurationSystemPaletteEntries,
       "win32VideoConfigurationVerticalResolution": win32VideoConfigurationVerticalResolution,
       "win32LogicalDiskToPartitionTable": win32LogicalDiskToPartitionTable,
       "win32LogicalDiskToPartitionEntry": win32LogicalDiskToPartitionEntry,
       "win32LogicalDiskToPartitionKeyIndex": win32LogicalDiskToPartitionKeyIndex,
       "win32LogicalDiskToPartitionAntecedent": win32LogicalDiskToPartitionAntecedent,
       "win32LogicalDiskToPartitionDependent": win32LogicalDiskToPartitionDependent,
       "win32DiskDriveToDiskPartitionTable": win32DiskDriveToDiskPartitionTable,
       "win32DiskDriveToDiskPartitionEntry": win32DiskDriveToDiskPartitionEntry,
       "win32DiskDriveToDiskPartitionKeyIndex": win32DiskDriveToDiskPartitionKeyIndex,
       "win32DiskDriveToDiskPartitionAntecedent": win32DiskDriveToDiskPartitionAntecedent,
       "win32DiskDriveToDiskPartitionDependent": win32DiskDriveToDiskPartitionDependent,
       "cimBIOSElementTable": cimBIOSElementTable,
       "cimBIOSElementEntry": cimBIOSElementEntry,
       "cimBIOSElementKeyIndex": cimBIOSElementKeyIndex,
       "cimBIOSElementName": cimBIOSElementName,
       "cimBIOSElementManufacturer": cimBIOSElementManufacturer,
       "cimBIOSElementDescription": cimBIOSElementDescription,
       "cimBIOSElementVersion": cimBIOSElementVersion,
       "cimBIOSElementBuildNumber": cimBIOSElementBuildNumber,
       "cimBIOSElementReleaseDate": cimBIOSElementReleaseDate}
)
