# SNMP MIB module (READYNAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/READYNAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:24 2024
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Netgear_ObjectIdentity = ObjectIdentity
netgear = _Netgear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526)
)
_NasManager_ObjectIdentity = ObjectIdentity
nasManager = _NasManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 18)
)


class _NasMgrSoftwareVersion_Type(DisplayString):
    """Custom type nasMgrSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NasMgrSoftwareVersion_Type.__name__ = "DisplayString"
_NasMgrSoftwareVersion_Object = MibScalar
nasMgrSoftwareVersion = _NasMgrSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 1),
    _NasMgrSoftwareVersion_Type()
)
nasMgrSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasMgrSoftwareVersion.setStatus("current")
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 3)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("mandatory")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 3, 1)
)
diskEntry.setIndexNames(
    (0, "READYNAS-MIB", "diskNumber"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("mandatory")
_DiskNumber_Type = Integer32
_DiskNumber_Object = MibTableColumn
diskNumber = _DiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 3, 1, 1),
    _DiskNumber_Type()
)
diskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskNumber.setStatus("mandatory")
_DiskChannel_Type = Integer32
_DiskChannel_Object = MibTableColumn
diskChannel = _DiskChannel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 3, 1, 2),
    _DiskChannel_Type()
)
diskChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskChannel.setStatus("mandatory")
_DiskModel_Type = DisplayString
_DiskModel_Object = MibTableColumn
diskModel = _DiskModel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 3, 1, 3),
    _DiskModel_Type()
)
diskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskModel.setStatus("mandatory")
_DiskState_Type = DisplayString
_DiskState_Object = MibTableColumn
diskState = _DiskState_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 3, 1, 4),
    _DiskState_Type()
)
diskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskState.setStatus("mandatory")
_DiskTemperature_Type = DisplayString
_DiskTemperature_Object = MibTableColumn
diskTemperature = _DiskTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 3, 1, 5),
    _DiskTemperature_Type()
)
diskTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTemperature.setStatus("mandatory")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 4)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 4, 1)
)
fanEntry.setIndexNames(
    (0, "READYNAS-MIB", "fanNumber"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")


class _FanNumber_Type(Integer32):
    """Custom type fanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_FanNumber_Type.__name__ = "Integer32"
_FanNumber_Object = MibTableColumn
fanNumber = _FanNumber_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 4, 1, 1),
    _FanNumber_Type()
)
fanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNumber.setStatus("mandatory")
_FanRPM_Type = Integer32
_FanRPM_Object = MibTableColumn
fanRPM = _FanRPM_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 4, 1, 2),
    _FanRPM_Type()
)
fanRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRPM.setStatus("mandatory")
_TemperatureTable_Object = MibTable
temperatureTable = _TemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 5)
)
if mibBuilder.loadTexts:
    temperatureTable.setStatus("mandatory")
_TemperatureEntry_Object = MibTableRow
temperatureEntry = _TemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 5, 1)
)
temperatureEntry.setIndexNames(
    (0, "READYNAS-MIB", "temperatureNumber"),
)
if mibBuilder.loadTexts:
    temperatureEntry.setStatus("mandatory")
_TemperatureNumber_Type = Integer32
_TemperatureNumber_Object = MibTableColumn
temperatureNumber = _TemperatureNumber_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 5, 1, 1),
    _TemperatureNumber_Type()
)
temperatureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureNumber.setStatus("mandatory")
_TemperatureValue_Type = DisplayString
_TemperatureValue_Object = MibTableColumn
temperatureValue = _TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 5, 1, 2),
    _TemperatureValue_Type()
)
temperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureValue.setStatus("mandatory")
_TemperatureStatus_Type = DisplayString
_TemperatureStatus_Object = MibTableColumn
temperatureStatus = _TemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 5, 1, 3),
    _TemperatureStatus_Type()
)
temperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureStatus.setStatus("mandatory")
_VolumeTable_Object = MibTable
volumeTable = _VolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 7)
)
if mibBuilder.loadTexts:
    volumeTable.setStatus("mandatory")
_VolumeEntry_Object = MibTableRow
volumeEntry = _VolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 7, 1)
)
volumeEntry.setIndexNames(
    (0, "READYNAS-MIB", "volumeNumber"),
)
if mibBuilder.loadTexts:
    volumeEntry.setStatus("mandatory")
_VolumeNumber_Type = Integer32
_VolumeNumber_Object = MibTableColumn
volumeNumber = _VolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 7, 1, 1),
    _VolumeNumber_Type()
)
volumeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeNumber.setStatus("mandatory")
_VolumeName_Type = DisplayString
_VolumeName_Object = MibTableColumn
volumeName = _VolumeName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 7, 1, 2),
    _VolumeName_Type()
)
volumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeName.setStatus("mandatory")
_VolumeRAIDLevel_Type = DisplayString
_VolumeRAIDLevel_Object = MibTableColumn
volumeRAIDLevel = _VolumeRAIDLevel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 7, 1, 3),
    _VolumeRAIDLevel_Type()
)
volumeRAIDLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeRAIDLevel.setStatus("mandatory")
_VolumeStatus_Type = DisplayString
_VolumeStatus_Object = MibTableColumn
volumeStatus = _VolumeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 7, 1, 4),
    _VolumeStatus_Type()
)
volumeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeStatus.setStatus("mandatory")
_VolumeSize_Type = Integer32
_VolumeSize_Object = MibTableColumn
volumeSize = _VolumeSize_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 7, 1, 5),
    _VolumeSize_Type()
)
volumeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeSize.setStatus("mandatory")
_VolumeFreeSpace_Type = Integer32
_VolumeFreeSpace_Object = MibTableColumn
volumeFreeSpace = _VolumeFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 7, 1, 6),
    _VolumeFreeSpace_Type()
)
volumeFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeFreeSpace.setStatus("mandatory")
_AryMgrEvts_ObjectIdentity = ObjectIdentity
aryMgrEvts = _AryMgrEvts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 18, 200)
)


class _ControllerNameEv_Type(DisplayString):
    """Custom type controllerNameEv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ControllerNameEv_Type.__name__ = "DisplayString"
_ControllerNameEv_Object = MibScalar
controllerNameEv = _ControllerNameEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 200, 201),
    _ControllerNameEv_Type()
)
controllerNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerNameEv.setStatus("mandatory")


class _ChannelNumberEv_Type(Integer32):
    """Custom type channelNumberEv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ChannelNumberEv_Type.__name__ = "Integer32"
_ChannelNumberEv_Object = MibScalar
channelNumberEv = _ChannelNumberEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 200, 202),
    _ChannelNumberEv_Type()
)
channelNumberEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelNumberEv.setStatus("mandatory")


class _TargetIDEv_Type(Integer32):
    """Custom type targetIDEv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TargetIDEv_Type.__name__ = "Integer32"
_TargetIDEv_Object = MibScalar
targetIDEv = _TargetIDEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 200, 203),
    _TargetIDEv_Type()
)
targetIDEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetIDEv.setStatus("mandatory")


class _VirtualDiskNameEv_Type(DisplayString):
    """Custom type virtualDiskNameEv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VirtualDiskNameEv_Type.__name__ = "DisplayString"
_VirtualDiskNameEv_Object = MibScalar
virtualDiskNameEv = _VirtualDiskNameEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 200, 204),
    _VirtualDiskNameEv_Type()
)
virtualDiskNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualDiskNameEv.setStatus("mandatory")


class _ArrayDiskNameEv_Type(DisplayString):
    """Custom type arrayDiskNameEv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ArrayDiskNameEv_Type.__name__ = "DisplayString"
_ArrayDiskNameEv_Object = MibScalar
arrayDiskNameEv = _ArrayDiskNameEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 200, 205),
    _ArrayDiskNameEv_Type()
)
arrayDiskNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayDiskNameEv.setStatus("mandatory")


class _OldVDConfigEv_Type(DisplayString):
    """Custom type oldVDConfigEv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_OldVDConfigEv_Type.__name__ = "DisplayString"
_OldVDConfigEv_Object = MibScalar
oldVDConfigEv = _OldVDConfigEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 200, 206),
    _OldVDConfigEv_Type()
)
oldVDConfigEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oldVDConfigEv.setStatus("mandatory")


class _NewVDConfigEv_Type(DisplayString):
    """Custom type newVDConfigEv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_NewVDConfigEv_Type.__name__ = "DisplayString"
_NewVDConfigEv_Object = MibScalar
newVDConfigEv = _NewVDConfigEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 200, 207),
    _NewVDConfigEv_Type()
)
newVDConfigEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newVDConfigEv.setStatus("mandatory")
_EnclosureNumberEv_Type = Integer32
_EnclosureNumberEv_Object = MibScalar
enclosureNumberEv = _EnclosureNumberEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 200, 208),
    _EnclosureNumberEv_Type()
)
enclosureNumberEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureNumberEv.setStatus("mandatory")
_UnitNumberEv_Type = Integer32
_UnitNumberEv_Object = MibScalar
unitNumberEv = _UnitNumberEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 200, 209),
    _UnitNumberEv_Type()
)
unitNumberEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitNumberEv.setStatus("mandatory")
_EnclosureNameEv_Type = DisplayString
_EnclosureNameEv_Object = MibScalar
enclosureNameEv = _EnclosureNameEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 200, 210),
    _EnclosureNameEv_Type()
)
enclosureNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureNameEv.setStatus("mandatory")
_UnitNameEv_Type = DisplayString
_UnitNameEv_Object = MibScalar
unitNameEv = _UnitNameEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 200, 211),
    _UnitNameEv_Type()
)
unitNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitNameEv.setStatus("mandatory")
_TimeEv_Type = Integer32
_TimeEv_Object = MibScalar
timeEv = _TimeEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 200, 212),
    _TimeEv_Type()
)
timeEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeEv.setStatus("mandatory")
_VolumeNameEv_Type = DisplayString
_VolumeNameEv_Object = MibScalar
volumeNameEv = _VolumeNameEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 200, 213),
    _VolumeNameEv_Type()
)
volumeNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeNameEv.setStatus("mandatory")
_NasTraps_ObjectIdentity = ObjectIdentity
nasTraps = _NasTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 18, 300)
)
_FanFailureMesg_Type = DisplayString
_FanFailureMesg_Object = MibScalar
fanFailureMesg = _FanFailureMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 400),
    _FanFailureMesg_Type()
)
fanFailureMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFailureMesg.setStatus("current")
_TempFailureMesg_Type = DisplayString
_TempFailureMesg_Object = MibScalar
tempFailureMesg = _TempFailureMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 401),
    _TempFailureMesg_Type()
)
tempFailureMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempFailureMesg.setStatus("current")
_PowerFailureMesg_Type = DisplayString
_PowerFailureMesg_Object = MibScalar
powerFailureMesg = _PowerFailureMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 402),
    _PowerFailureMesg_Type()
)
powerFailureMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerFailureMesg.setStatus("current")
_RaidMesg_Type = DisplayString
_RaidMesg_Object = MibScalar
raidMesg = _RaidMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 403),
    _RaidMesg_Type()
)
raidMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidMesg.setStatus("current")
_SnapshotMesg_Type = DisplayString
_SnapshotMesg_Object = MibScalar
snapshotMesg = _SnapshotMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 404),
    _SnapshotMesg_Type()
)
snapshotMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotMesg.setStatus("current")
_UpsMesg_Type = DisplayString
_UpsMesg_Object = MibScalar
upsMesg = _UpsMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 405),
    _UpsMesg_Type()
)
upsMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMesg.setStatus("current")
_SataMesg_Type = DisplayString
_SataMesg_Object = MibScalar
sataMesg = _SataMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 406),
    _SataMesg_Type()
)
sataMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sataMesg.setStatus("current")
_VolumeMesg_Type = DisplayString
_VolumeMesg_Object = MibScalar
volumeMesg = _VolumeMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 407),
    _VolumeMesg_Type()
)
volumeMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeMesg.setStatus("current")
_DiskTempWarningMesg_Type = DisplayString
_DiskTempWarningMesg_Object = MibScalar
diskTempWarningMesg = _DiskTempWarningMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 408),
    _DiskTempWarningMesg_Type()
)
diskTempWarningMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTempWarningMesg.setStatus("current")
_BackupMesg_Type = DisplayString
_BackupMesg_Object = MibScalar
backupMesg = _BackupMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 18, 409),
    _BackupMesg_Type()
)
backupMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupMesg.setStatus("current")
_ProductID_ObjectIdentity = ObjectIdentity
productID = _ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100)
)
_ReadyNAS_ObjectIdentity = ObjectIdentity
readyNAS = _ReadyNAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 12)
)

# Managed Objects groups


# Notification objects

fanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 18, 300, 0, 10)
)
fanFailure.setObjects(
    ("READYNAS-MIB", "fanFailureMesg")
)
if mibBuilder.loadTexts:
    fanFailure.setStatus(
        ""
    )

tempFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 18, 300, 0, 20)
)
tempFailure.setObjects(
    ("READYNAS-MIB", "tempFailureMesg")
)
if mibBuilder.loadTexts:
    tempFailure.setStatus(
        ""
    )

powerVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 18, 300, 0, 30)
)
powerVoltage.setObjects(
    ("READYNAS-MIB", "powerFailureMesg")
)
if mibBuilder.loadTexts:
    powerVoltage.setStatus(
        ""
    )

raidEventNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 18, 300, 0, 40)
)
raidEventNotice.setObjects(
    ("READYNAS-MIB", "raidMesg")
)
if mibBuilder.loadTexts:
    raidEventNotice.setStatus(
        ""
    )

snapshotEventNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 18, 300, 0, 50)
)
snapshotEventNotice.setObjects(
    ("READYNAS-MIB", "snapshotMesg")
)
if mibBuilder.loadTexts:
    snapshotEventNotice.setStatus(
        ""
    )

hotplugDiskNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 18, 300, 0, 60)
)
hotplugDiskNotice.setObjects(
    ("READYNAS-MIB", "sataMesg")
)
if mibBuilder.loadTexts:
    hotplugDiskNotice.setStatus(
        ""
    )

upsEventNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 18, 300, 0, 70)
)
upsEventNotice.setObjects(
    ("READYNAS-MIB", "upsMesg")
)
if mibBuilder.loadTexts:
    upsEventNotice.setStatus(
        ""
    )

volumeNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 18, 300, 0, 80)
)
volumeNotice.setObjects(
    ("READYNAS-MIB", "volumeMesg")
)
if mibBuilder.loadTexts:
    volumeNotice.setStatus(
        ""
    )

diskTempWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 18, 300, 0, 90)
)
diskTempWarning.setObjects(
    ("READYNAS-MIB", "volumeMesg")
)
if mibBuilder.loadTexts:
    diskTempWarning.setStatus(
        ""
    )

backupNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 18, 300, 0, 100)
)
backupNotice.setObjects(
    ("READYNAS-MIB", "backupMesg")
)
if mibBuilder.loadTexts:
    backupNotice.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "READYNAS-MIB",
    **{"netgear": netgear,
       "nasManager": nasManager,
       "nasMgrSoftwareVersion": nasMgrSoftwareVersion,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskNumber": diskNumber,
       "diskChannel": diskChannel,
       "diskModel": diskModel,
       "diskState": diskState,
       "diskTemperature": diskTemperature,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanNumber": fanNumber,
       "fanRPM": fanRPM,
       "temperatureTable": temperatureTable,
       "temperatureEntry": temperatureEntry,
       "temperatureNumber": temperatureNumber,
       "temperatureValue": temperatureValue,
       "temperatureStatus": temperatureStatus,
       "volumeTable": volumeTable,
       "volumeEntry": volumeEntry,
       "volumeNumber": volumeNumber,
       "volumeName": volumeName,
       "volumeRAIDLevel": volumeRAIDLevel,
       "volumeStatus": volumeStatus,
       "volumeSize": volumeSize,
       "volumeFreeSpace": volumeFreeSpace,
       "aryMgrEvts": aryMgrEvts,
       "controllerNameEv": controllerNameEv,
       "channelNumberEv": channelNumberEv,
       "targetIDEv": targetIDEv,
       "virtualDiskNameEv": virtualDiskNameEv,
       "arrayDiskNameEv": arrayDiskNameEv,
       "oldVDConfigEv": oldVDConfigEv,
       "newVDConfigEv": newVDConfigEv,
       "enclosureNumberEv": enclosureNumberEv,
       "unitNumberEv": unitNumberEv,
       "enclosureNameEv": enclosureNameEv,
       "unitNameEv": unitNameEv,
       "timeEv": timeEv,
       "volumeNameEv": volumeNameEv,
       "nasTraps": nasTraps,
       "fanFailure": fanFailure,
       "tempFailure": tempFailure,
       "powerVoltage": powerVoltage,
       "raidEventNotice": raidEventNotice,
       "snapshotEventNotice": snapshotEventNotice,
       "hotplugDiskNotice": hotplugDiskNotice,
       "upsEventNotice": upsEventNotice,
       "volumeNotice": volumeNotice,
       "diskTempWarning": diskTempWarning,
       "backupNotice": backupNotice,
       "fanFailureMesg": fanFailureMesg,
       "tempFailureMesg": tempFailureMesg,
       "powerFailureMesg": powerFailureMesg,
       "raidMesg": raidMesg,
       "snapshotMesg": snapshotMesg,
       "upsMesg": upsMesg,
       "sataMesg": sataMesg,
       "volumeMesg": volumeMesg,
       "diskTempWarningMesg": diskTempWarningMesg,
       "backupMesg": backupMesg,
       "productID": productID,
       "readyNAS": readyNAS}
)
