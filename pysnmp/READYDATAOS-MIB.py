# SNMP MIB module (READYDATAOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/READYDATAOS-MIB
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
_NgNasManager_ObjectIdentity = ObjectIdentity
ngNasManager = _NgNasManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 22)
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
    (1, 3, 6, 1, 4, 1, 4526, 22, 1),
    _NasMgrSoftwareVersion_Type()
)
nasMgrSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasMgrSoftwareVersion.setStatus("current")
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 3)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("mandatory")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 3, 1)
)
diskEntry.setIndexNames(
    (0, "READYDATAOS-MIB", "diskNumber"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("mandatory")
_DiskNumber_Type = Integer32
_DiskNumber_Object = MibTableColumn
diskNumber = _DiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 1),
    _DiskNumber_Type()
)
diskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskNumber.setStatus("mandatory")
_DiskID_Type = DisplayString
_DiskID_Object = MibTableColumn
diskID = _DiskID_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 2),
    _DiskID_Type()
)
diskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskID.setStatus("mandatory")
_DiskSlotName_Type = DisplayString
_DiskSlotName_Object = MibTableColumn
diskSlotName = _DiskSlotName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 3),
    _DiskSlotName_Type()
)
diskSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSlotName.setStatus("mandatory")
_DiskSerial_Type = DisplayString
_DiskSerial_Object = MibTableColumn
diskSerial = _DiskSerial_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 4),
    _DiskSerial_Type()
)
diskSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSerial.setStatus("mandatory")
_DiskModel_Type = DisplayString
_DiskModel_Object = MibTableColumn
diskModel = _DiskModel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 5),
    _DiskModel_Type()
)
diskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskModel.setStatus("mandatory")
_AtaError_Type = Integer32
_AtaError_Object = MibTableColumn
ataError = _AtaError_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 6),
    _AtaError_Type()
)
ataError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ataError.setStatus("mandatory")
_DiskCapacity_Type = DisplayString
_DiskCapacity_Object = MibTableColumn
diskCapacity = _DiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 7),
    _DiskCapacity_Type()
)
diskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskCapacity.setStatus("mandatory")
_DiskInterface_Type = DisplayString
_DiskInterface_Object = MibTableColumn
diskInterface = _DiskInterface_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 8),
    _DiskInterface_Type()
)
diskInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskInterface.setStatus("mandatory")
_DiskState_Type = DisplayString
_DiskState_Object = MibTableColumn
diskState = _DiskState_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 9),
    _DiskState_Type()
)
diskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskState.setStatus("mandatory")
_DiskTemperature_Type = Integer32
_DiskTemperature_Object = MibTableColumn
diskTemperature = _DiskTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 3, 1, 10),
    _DiskTemperature_Type()
)
diskTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTemperature.setStatus("mandatory")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 4)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 4, 1)
)
fanEntry.setIndexNames(
    (0, "READYDATAOS-MIB", "fanNumber"),
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
    (1, 3, 6, 1, 4, 1, 4526, 22, 4, 1, 1),
    _FanNumber_Type()
)
fanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNumber.setStatus("mandatory")
_FanRPM_Type = Integer32
_FanRPM_Object = MibTableColumn
fanRPM = _FanRPM_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 4, 1, 2),
    _FanRPM_Type()
)
fanRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRPM.setStatus("mandatory")
_FanStatus_Type = DisplayString
_FanStatus_Object = MibTableColumn
fanStatus = _FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 4, 1, 3),
    _FanStatus_Type()
)
fanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanStatus.setStatus("mandatory")
_FanType_Type = DisplayString
_FanType_Object = MibTableColumn
fanType = _FanType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 4, 1, 4),
    _FanType_Type()
)
fanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanType.setStatus("mandatory")
_TemperatureTable_Object = MibTable
temperatureTable = _TemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 5)
)
if mibBuilder.loadTexts:
    temperatureTable.setStatus("mandatory")
_TemperatureEntry_Object = MibTableRow
temperatureEntry = _TemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 5, 1)
)
temperatureEntry.setIndexNames(
    (0, "READYDATAOS-MIB", "temperatureNumber"),
)
if mibBuilder.loadTexts:
    temperatureEntry.setStatus("mandatory")
_TemperatureNumber_Type = Integer32
_TemperatureNumber_Object = MibTableColumn
temperatureNumber = _TemperatureNumber_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 5, 1, 1),
    _TemperatureNumber_Type()
)
temperatureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureNumber.setStatus("mandatory")
_TemperatureValue_Type = Integer32
_TemperatureValue_Object = MibTableColumn
temperatureValue = _TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 5, 1, 2),
    _TemperatureValue_Type()
)
temperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureValue.setStatus("mandatory")
_TemperatureTyoe_Type = DisplayString
_TemperatureTyoe_Object = MibScalar
temperatureTyoe = _TemperatureTyoe_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 5, 1, 3),
    _TemperatureTyoe_Type()
)
temperatureTyoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureTyoe.setStatus("mandatory")
_TemperatureMin_Type = Integer32
_TemperatureMin_Object = MibTableColumn
temperatureMin = _TemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 5, 1, 4),
    _TemperatureMin_Type()
)
temperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureMin.setStatus("mandatory")
_TemperatureMax_Type = Integer32
_TemperatureMax_Object = MibTableColumn
temperatureMax = _TemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 5, 1, 5),
    _TemperatureMax_Type()
)
temperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureMax.setStatus("mandatory")
_VolumeTable_Object = MibTable
volumeTable = _VolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 7)
)
if mibBuilder.loadTexts:
    volumeTable.setStatus("mandatory")
_VolumeEntry_Object = MibTableRow
volumeEntry = _VolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 7, 1)
)
volumeEntry.setIndexNames(
    (0, "READYDATAOS-MIB", "volumeNumber"),
)
if mibBuilder.loadTexts:
    volumeEntry.setStatus("mandatory")
_VolumeNumber_Type = Integer32
_VolumeNumber_Object = MibTableColumn
volumeNumber = _VolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 7, 1, 1),
    _VolumeNumber_Type()
)
volumeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeNumber.setStatus("mandatory")
_VolumeName_Type = DisplayString
_VolumeName_Object = MibTableColumn
volumeName = _VolumeName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 7, 1, 2),
    _VolumeName_Type()
)
volumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeName.setStatus("mandatory")
_VolumeRAIDLevel_Type = DisplayString
_VolumeRAIDLevel_Object = MibTableColumn
volumeRAIDLevel = _VolumeRAIDLevel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 7, 1, 3),
    _VolumeRAIDLevel_Type()
)
volumeRAIDLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeRAIDLevel.setStatus("mandatory")
_VolumeStatus_Type = DisplayString
_VolumeStatus_Object = MibTableColumn
volumeStatus = _VolumeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 7, 1, 4),
    _VolumeStatus_Type()
)
volumeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeStatus.setStatus("mandatory")
_VolumeSize_Type = Integer32
_VolumeSize_Object = MibTableColumn
volumeSize = _VolumeSize_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 7, 1, 5),
    _VolumeSize_Type()
)
volumeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeSize.setStatus("mandatory")
_VolumeFreeSpace_Type = Integer32
_VolumeFreeSpace_Object = MibTableColumn
volumeFreeSpace = _VolumeFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 7, 1, 6),
    _VolumeFreeSpace_Type()
)
volumeFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeFreeSpace.setStatus("mandatory")
_PsuTable_Object = MibTable
psuTable = _PsuTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 8)
)
if mibBuilder.loadTexts:
    psuTable.setStatus("mandatory")
_PsuEntry_Object = MibTableRow
psuEntry = _PsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 8, 1)
)
psuEntry.setIndexNames(
    (0, "READYDATAOS-MIB", "psuNumber"),
)
if mibBuilder.loadTexts:
    psuEntry.setStatus("mandatory")
_PsuNumber_Type = Integer32
_PsuNumber_Object = MibTableColumn
psuNumber = _PsuNumber_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 8, 1, 1),
    _PsuNumber_Type()
)
psuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuNumber.setStatus("mandatory")
_PsuDesc_Type = DisplayString
_PsuDesc_Object = MibTableColumn
psuDesc = _PsuDesc_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 8, 1, 2),
    _PsuDesc_Type()
)
psuDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuDesc.setStatus("mandatory")
_PsuStatus_Type = DisplayString
_PsuStatus_Object = MibTableColumn
psuStatus = _PsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 8, 1, 3),
    _PsuStatus_Type()
)
psuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuStatus.setStatus("mandatory")
_AryMgrEvts_ObjectIdentity = ObjectIdentity
aryMgrEvts = _AryMgrEvts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 22, 200)
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
    (1, 3, 6, 1, 4, 1, 4526, 22, 200, 201),
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
    (1, 3, 6, 1, 4, 1, 4526, 22, 200, 202),
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
    (1, 3, 6, 1, 4, 1, 4526, 22, 200, 203),
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
    (1, 3, 6, 1, 4, 1, 4526, 22, 200, 204),
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
    (1, 3, 6, 1, 4, 1, 4526, 22, 200, 205),
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
    (1, 3, 6, 1, 4, 1, 4526, 22, 200, 206),
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
    (1, 3, 6, 1, 4, 1, 4526, 22, 200, 207),
    _NewVDConfigEv_Type()
)
newVDConfigEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newVDConfigEv.setStatus("mandatory")
_EnclosureNumberEv_Type = Integer32
_EnclosureNumberEv_Object = MibScalar
enclosureNumberEv = _EnclosureNumberEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 200, 208),
    _EnclosureNumberEv_Type()
)
enclosureNumberEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureNumberEv.setStatus("mandatory")
_UnitNumberEv_Type = Integer32
_UnitNumberEv_Object = MibScalar
unitNumberEv = _UnitNumberEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 200, 209),
    _UnitNumberEv_Type()
)
unitNumberEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitNumberEv.setStatus("mandatory")
_EnclosureNameEv_Type = DisplayString
_EnclosureNameEv_Object = MibScalar
enclosureNameEv = _EnclosureNameEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 200, 210),
    _EnclosureNameEv_Type()
)
enclosureNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureNameEv.setStatus("mandatory")
_UnitNameEv_Type = DisplayString
_UnitNameEv_Object = MibScalar
unitNameEv = _UnitNameEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 200, 211),
    _UnitNameEv_Type()
)
unitNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitNameEv.setStatus("mandatory")
_TimeEv_Type = Integer32
_TimeEv_Object = MibScalar
timeEv = _TimeEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 200, 212),
    _TimeEv_Type()
)
timeEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeEv.setStatus("mandatory")
_VolumeNameEv_Type = DisplayString
_VolumeNameEv_Object = MibScalar
volumeNameEv = _VolumeNameEv_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 200, 213),
    _VolumeNameEv_Type()
)
volumeNameEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeNameEv.setStatus("mandatory")
_NasTraps_ObjectIdentity = ObjectIdentity
nasTraps = _NasTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 22, 300)
)
_FanFailureMesg_Type = DisplayString
_FanFailureMesg_Object = MibScalar
fanFailureMesg = _FanFailureMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 400),
    _FanFailureMesg_Type()
)
fanFailureMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFailureMesg.setStatus("current")
_TempFailureMesg_Type = DisplayString
_TempFailureMesg_Object = MibScalar
tempFailureMesg = _TempFailureMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 401),
    _TempFailureMesg_Type()
)
tempFailureMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempFailureMesg.setStatus("current")
_PowerVoltageMesg_Type = DisplayString
_PowerVoltageMesg_Object = MibScalar
powerVoltageMesg = _PowerVoltageMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 402),
    _PowerVoltageMesg_Type()
)
powerVoltageMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerVoltageMesg.setStatus("current")
_RaidEventNoticeMesg_Type = DisplayString
_RaidEventNoticeMesg_Object = MibScalar
raidEventNoticeMesg = _RaidEventNoticeMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 403),
    _RaidEventNoticeMesg_Type()
)
raidEventNoticeMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidEventNoticeMesg.setStatus("current")
_SnapshotEventNoticeMesg_Type = DisplayString
_SnapshotEventNoticeMesg_Object = MibScalar
snapshotEventNoticeMesg = _SnapshotEventNoticeMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 404),
    _SnapshotEventNoticeMesg_Type()
)
snapshotEventNoticeMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotEventNoticeMesg.setStatus("current")
_UpsEventNoticeMesg_Type = DisplayString
_UpsEventNoticeMesg_Object = MibScalar
upsEventNoticeMesg = _UpsEventNoticeMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 405),
    _UpsEventNoticeMesg_Type()
)
upsEventNoticeMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventNoticeMesg.setStatus("current")
_HotplugDiskNoticeMesg_Type = DisplayString
_HotplugDiskNoticeMesg_Object = MibScalar
hotplugDiskNoticeMesg = _HotplugDiskNoticeMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 406),
    _HotplugDiskNoticeMesg_Type()
)
hotplugDiskNoticeMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotplugDiskNoticeMesg.setStatus("current")
_VolumeNoticeMesg_Type = DisplayString
_VolumeNoticeMesg_Object = MibScalar
volumeNoticeMesg = _VolumeNoticeMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 407),
    _VolumeNoticeMesg_Type()
)
volumeNoticeMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeNoticeMesg.setStatus("current")
_DiskTempWarningMesg_Type = DisplayString
_DiskTempWarningMesg_Object = MibScalar
diskTempWarningMesg = _DiskTempWarningMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 408),
    _DiskTempWarningMesg_Type()
)
diskTempWarningMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTempWarningMesg.setStatus("current")
_BackupNoticeMesg_Type = DisplayString
_BackupNoticeMesg_Object = MibScalar
backupNoticeMesg = _BackupNoticeMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 409),
    _BackupNoticeMesg_Type()
)
backupNoticeMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupNoticeMesg.setStatus("current")
_DiskSmartWarningMesg_Type = DisplayString
_DiskSmartWarningMesg_Object = MibScalar
diskSmartWarningMesg = _DiskSmartWarningMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 410),
    _DiskSmartWarningMesg_Type()
)
diskSmartWarningMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSmartWarningMesg.setStatus("current")
_PsuWarningMesg_Type = DisplayString
_PsuWarningMesg_Object = MibScalar
psuWarningMesg = _PsuWarningMesg_Object(
    (1, 3, 6, 1, 4, 1, 4526, 22, 411),
    _PsuWarningMesg_Type()
)
psuWarningMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuWarningMesg.setStatus("current")
_ProductID_ObjectIdentity = ObjectIdentity
productID = _ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100)
)
_ReadyDATAOS_ObjectIdentity = ObjectIdentity
ReadyDATAOS = _ReadyDATAOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 15)
)

# Managed Objects groups


# Notification objects

fanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 22, 300, 0, 10)
)
fanFailure.setObjects(
    ("READYDATAOS-MIB", "fanFailureMesg")
)
if mibBuilder.loadTexts:
    fanFailure.setStatus(
        ""
    )

tempFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 22, 300, 0, 20)
)
tempFailure.setObjects(
    ("READYDATAOS-MIB", "tempFailureMesg")
)
if mibBuilder.loadTexts:
    tempFailure.setStatus(
        ""
    )

powerVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 22, 300, 0, 30)
)
powerVoltage.setObjects(
    ("READYDATAOS-MIB", "powerVoltageMesg")
)
if mibBuilder.loadTexts:
    powerVoltage.setStatus(
        ""
    )

raidEventNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 22, 300, 0, 40)
)
raidEventNotice.setObjects(
    ("READYDATAOS-MIB", "raidEventNoticeMesg")
)
if mibBuilder.loadTexts:
    raidEventNotice.setStatus(
        ""
    )

snapshotEventNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 22, 300, 0, 50)
)
snapshotEventNotice.setObjects(
    ("READYDATAOS-MIB", "snapshotEventNoticeMesg")
)
if mibBuilder.loadTexts:
    snapshotEventNotice.setStatus(
        ""
    )

hotplugDiskNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 22, 300, 0, 60)
)
hotplugDiskNotice.setObjects(
    ("READYDATAOS-MIB", "hotplugDiskNoticeMesg")
)
if mibBuilder.loadTexts:
    hotplugDiskNotice.setStatus(
        ""
    )

upsEventNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 22, 300, 0, 70)
)
upsEventNotice.setObjects(
    ("READYDATAOS-MIB", "upsEventNoticeMesg")
)
if mibBuilder.loadTexts:
    upsEventNotice.setStatus(
        ""
    )

volumeNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 22, 300, 0, 80)
)
volumeNotice.setObjects(
    ("READYDATAOS-MIB", "volumeNoticeMesg")
)
if mibBuilder.loadTexts:
    volumeNotice.setStatus(
        ""
    )

diskTempWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 22, 300, 0, 90)
)
diskTempWarning.setObjects(
    ("READYDATAOS-MIB", "diskTempWarningMesg")
)
if mibBuilder.loadTexts:
    diskTempWarning.setStatus(
        ""
    )

backupNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 22, 300, 0, 100)
)
backupNotice.setObjects(
    ("READYDATAOS-MIB", "backupNoticeMesg")
)
if mibBuilder.loadTexts:
    backupNotice.setStatus(
        ""
    )

diskSmartWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 22, 300, 0, 110)
)
diskSmartWarning.setObjects(
    ("READYDATAOS-MIB", "diskSmartWarningMesg")
)
if mibBuilder.loadTexts:
    diskSmartWarning.setStatus(
        ""
    )

psuWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 4526, 22, 300, 0, 120)
)
psuWarning.setObjects(
    ("READYDATAOS-MIB", "psuWarningMesg")
)
if mibBuilder.loadTexts:
    psuWarning.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "READYDATAOS-MIB",
    **{"netgear": netgear,
       "ngNasManager": ngNasManager,
       "nasMgrSoftwareVersion": nasMgrSoftwareVersion,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskNumber": diskNumber,
       "diskID": diskID,
       "diskSlotName": diskSlotName,
       "diskSerial": diskSerial,
       "diskModel": diskModel,
       "ataError": ataError,
       "diskCapacity": diskCapacity,
       "diskInterface": diskInterface,
       "diskState": diskState,
       "diskTemperature": diskTemperature,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanNumber": fanNumber,
       "fanRPM": fanRPM,
       "fanStatus": fanStatus,
       "fanType": fanType,
       "temperatureTable": temperatureTable,
       "temperatureEntry": temperatureEntry,
       "temperatureNumber": temperatureNumber,
       "temperatureValue": temperatureValue,
       "temperatureTyoe": temperatureTyoe,
       "temperatureMin": temperatureMin,
       "temperatureMax": temperatureMax,
       "volumeTable": volumeTable,
       "volumeEntry": volumeEntry,
       "volumeNumber": volumeNumber,
       "volumeName": volumeName,
       "volumeRAIDLevel": volumeRAIDLevel,
       "volumeStatus": volumeStatus,
       "volumeSize": volumeSize,
       "volumeFreeSpace": volumeFreeSpace,
       "psuTable": psuTable,
       "psuEntry": psuEntry,
       "psuNumber": psuNumber,
       "psuDesc": psuDesc,
       "psuStatus": psuStatus,
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
       "diskSmartWarning": diskSmartWarning,
       "psuWarning": psuWarning,
       "fanFailureMesg": fanFailureMesg,
       "tempFailureMesg": tempFailureMesg,
       "powerVoltageMesg": powerVoltageMesg,
       "raidEventNoticeMesg": raidEventNoticeMesg,
       "snapshotEventNoticeMesg": snapshotEventNoticeMesg,
       "upsEventNoticeMesg": upsEventNoticeMesg,
       "hotplugDiskNoticeMesg": hotplugDiskNoticeMesg,
       "volumeNoticeMesg": volumeNoticeMesg,
       "diskTempWarningMesg": diskTempWarningMesg,
       "backupNoticeMesg": backupNoticeMesg,
       "diskSmartWarningMesg": diskSmartWarningMesg,
       "psuWarningMesg": psuWarningMesg,
       "productID": productID,
       "ReadyDATAOS": ReadyDATAOS}
)
