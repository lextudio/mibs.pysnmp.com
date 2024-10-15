# SNMP MIB module (ADTX-RAID-AVCL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTX-RAID-AVCL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:38 2024
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

(adtx,
 adtxProducts) = mibBuilder.importSymbols(
    "ADTX-SMI",
    "adtx",
    "adtxProducts")

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


# MODULE-IDENTITY


# Types definitions



class AvcString(DisplayString):
    """Custom type AvcString based on DisplayString"""




class AvcLongString(OctetString):
    """Custom type AvcLongString based on OctetString"""




class AvcCounter(Counter32):
    """Custom type AvcCounter based on Counter32"""




class AvcInteger(Integer32):
    """Custom type AvcInteger based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Avc_ObjectIdentity = ObjectIdentity
avc = _Avc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1)
)
_Avcl_ObjectIdentity = ObjectIdentity
avcl = _Avcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1)
)
_AvclVersion_Type = AvcString
_AvclVersion_Object = MibScalar
avclVersion = _AvclVersion_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 1),
    _AvclVersion_Type()
)
avclVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclVersion.setStatus("mandatory")
_AvclOS_Type = AvcString
_AvclOS_Object = MibScalar
avclOS = _AvclOS_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 2),
    _AvclOS_Type()
)
avclOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclOS.setStatus("mandatory")
_AvclHost_Type = AvcString
_AvclHost_Object = MibScalar
avclHost = _AvclHost_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 3),
    _AvclHost_Type()
)
avclHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclHost.setStatus("mandatory")
_AvclNumOfDevices_Type = AvcCounter
_AvclNumOfDevices_Object = MibScalar
avclNumOfDevices = _AvclNumOfDevices_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 4),
    _AvclNumOfDevices_Type()
)
avclNumOfDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclNumOfDevices.setStatus("mandatory")
_AvclEventInfo_Type = AvcLongString
_AvclEventInfo_Object = MibScalar
avclEventInfo = _AvclEventInfo_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 5),
    _AvclEventInfo_Type()
)
avclEventInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclEventInfo.setStatus("mandatory")
_AvclDeviceInformationTable_Object = MibTable
avclDeviceInformationTable = _AvclDeviceInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    avclDeviceInformationTable.setStatus("mandatory")
_AvclDeviceInformationEntry_Object = MibTableRow
avclDeviceInformationEntry = _AvclDeviceInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1)
)
avclDeviceInformationEntry.setIndexNames(
    (0, "ADTX-RAID-AVCL-MIB", "avclDeviceIndex"),
)
if mibBuilder.loadTexts:
    avclDeviceInformationEntry.setStatus("mandatory")
_AvclDeviceIndex_Type = AvcCounter
_AvclDeviceIndex_Object = MibTableColumn
avclDeviceIndex = _AvclDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 1),
    _AvclDeviceIndex_Type()
)
avclDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceIndex.setStatus("mandatory")
_AvclDeviceIP_Type = AvcString
_AvclDeviceIP_Object = MibTableColumn
avclDeviceIP = _AvclDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 2),
    _AvclDeviceIP_Type()
)
avclDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceIP.setStatus("mandatory")
_AvclDeviceSystemVersion_Type = AvcString
_AvclDeviceSystemVersion_Object = MibTableColumn
avclDeviceSystemVersion = _AvclDeviceSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 3),
    _AvclDeviceSystemVersion_Type()
)
avclDeviceSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceSystemVersion.setStatus("mandatory")
_AvclDeviceManufacturer_Type = AvcString
_AvclDeviceManufacturer_Object = MibTableColumn
avclDeviceManufacturer = _AvclDeviceManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 4),
    _AvclDeviceManufacturer_Type()
)
avclDeviceManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceManufacturer.setStatus("mandatory")
_AvclDeviceProductName_Type = AvcString
_AvclDeviceProductName_Object = MibTableColumn
avclDeviceProductName = _AvclDeviceProductName_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 5),
    _AvclDeviceProductName_Type()
)
avclDeviceProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceProductName.setStatus("mandatory")
_AvclDeviceRevisionLevel_Type = AvcString
_AvclDeviceRevisionLevel_Object = MibTableColumn
avclDeviceRevisionLevel = _AvclDeviceRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 6),
    _AvclDeviceRevisionLevel_Type()
)
avclDeviceRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceRevisionLevel.setStatus("mandatory")
_AvclDeviceSerialNumber_Type = AvcString
_AvclDeviceSerialNumber_Object = MibTableColumn
avclDeviceSerialNumber = _AvclDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 7),
    _AvclDeviceSerialNumber_Type()
)
avclDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceSerialNumber.setStatus("mandatory")
_AvclDeviceDate_Type = AvcString
_AvclDeviceDate_Object = MibTableColumn
avclDeviceDate = _AvclDeviceDate_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 8),
    _AvclDeviceDate_Type()
)
avclDeviceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceDate.setStatus("mandatory")
_AvclDeviceTime_Type = AvcString
_AvclDeviceTime_Object = MibTableColumn
avclDeviceTime = _AvclDeviceTime_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 9),
    _AvclDeviceTime_Type()
)
avclDeviceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceTime.setStatus("mandatory")
_AvclDeviceAssignedSpare_Type = AvcString
_AvclDeviceAssignedSpare_Object = MibTableColumn
avclDeviceAssignedSpare = _AvclDeviceAssignedSpare_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 10),
    _AvclDeviceAssignedSpare_Type()
)
avclDeviceAssignedSpare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceAssignedSpare.setStatus("mandatory")
_AvclDeviceInitiatorMode_Type = AvcString
_AvclDeviceInitiatorMode_Object = MibTableColumn
avclDeviceInitiatorMode = _AvclDeviceInitiatorMode_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 11),
    _AvclDeviceInitiatorMode_Type()
)
avclDeviceInitiatorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceInitiatorMode.setStatus("mandatory")
_AvclDeviceInstantCopyLicense_Type = AvcString
_AvclDeviceInstantCopyLicense_Object = MibTableColumn
avclDeviceInstantCopyLicense = _AvclDeviceInstantCopyLicense_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 12),
    _AvclDeviceInstantCopyLicense_Type()
)
avclDeviceInstantCopyLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceInstantCopyLicense.setStatus("mandatory")
_AvclDeviceMirroringLicense_Type = AvcString
_AvclDeviceMirroringLicense_Object = MibTableColumn
avclDeviceMirroringLicense = _AvclDeviceMirroringLicense_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 13),
    _AvclDeviceMirroringLicense_Type()
)
avclDeviceMirroringLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceMirroringLicense.setStatus("mandatory")
_AvclDeviceWWNInfoCount_Type = AvcCounter
_AvclDeviceWWNInfoCount_Object = MibTableColumn
avclDeviceWWNInfoCount = _AvclDeviceWWNInfoCount_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 14),
    _AvclDeviceWWNInfoCount_Type()
)
avclDeviceWWNInfoCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceWWNInfoCount.setStatus("mandatory")
_AvclDeviceWWNInfo_Type = AvcString
_AvclDeviceWWNInfo_Object = MibTableColumn
avclDeviceWWNInfo = _AvclDeviceWWNInfo_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 15),
    _AvclDeviceWWNInfo_Type()
)
avclDeviceWWNInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceWWNInfo.setStatus("mandatory")
_AvclDeviceSurfaceSchedMode_Type = AvcLongString
_AvclDeviceSurfaceSchedMode_Object = MibTableColumn
avclDeviceSurfaceSchedMode = _AvclDeviceSurfaceSchedMode_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 16),
    _AvclDeviceSurfaceSchedMode_Type()
)
avclDeviceSurfaceSchedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceSurfaceSchedMode.setStatus("mandatory")
_AvclDeviceSurfaceSchedTime_Type = AvcString
_AvclDeviceSurfaceSchedTime_Object = MibTableColumn
avclDeviceSurfaceSchedTime = _AvclDeviceSurfaceSchedTime_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 17),
    _AvclDeviceSurfaceSchedTime_Type()
)
avclDeviceSurfaceSchedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceSurfaceSchedTime.setStatus("mandatory")
_AvclDeviceSurfaceVerifyDuration_Type = AvcCounter
_AvclDeviceSurfaceVerifyDuration_Object = MibTableColumn
avclDeviceSurfaceVerifyDuration = _AvclDeviceSurfaceVerifyDuration_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 18),
    _AvclDeviceSurfaceVerifyDuration_Type()
)
avclDeviceSurfaceVerifyDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceSurfaceVerifyDuration.setStatus("mandatory")
_AvclDeviceICSourceLU_Type = AvcInteger
_AvclDeviceICSourceLU_Object = MibTableColumn
avclDeviceICSourceLU = _AvclDeviceICSourceLU_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 19),
    _AvclDeviceICSourceLU_Type()
)
avclDeviceICSourceLU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceICSourceLU.setStatus("mandatory")
_AvclDeviceICTargetLU_Type = AvcInteger
_AvclDeviceICTargetLU_Object = MibTableColumn
avclDeviceICTargetLU = _AvclDeviceICTargetLU_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 20),
    _AvclDeviceICTargetLU_Type()
)
avclDeviceICTargetLU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceICTargetLU.setStatus("mandatory")
_AvclDeviceICFlag_Type = AvcString
_AvclDeviceICFlag_Object = MibTableColumn
avclDeviceICFlag = _AvclDeviceICFlag_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 21),
    _AvclDeviceICFlag_Type()
)
avclDeviceICFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceICFlag.setStatus("mandatory")
_AvclDeviceICProgress_Type = AvcCounter
_AvclDeviceICProgress_Object = MibTableColumn
avclDeviceICProgress = _AvclDeviceICProgress_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 22),
    _AvclDeviceICProgress_Type()
)
avclDeviceICProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceICProgress.setStatus("mandatory")
_AvclDeviceICPairWWN_Type = AvcString
_AvclDeviceICPairWWN_Object = MibTableColumn
avclDeviceICPairWWN = _AvclDeviceICPairWWN_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 23),
    _AvclDeviceICPairWWN_Type()
)
avclDeviceICPairWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceICPairWWN.setStatus("mandatory")
_AvclDeviceRegHostCount_Type = AvcCounter
_AvclDeviceRegHostCount_Object = MibTableColumn
avclDeviceRegHostCount = _AvclDeviceRegHostCount_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 24),
    _AvclDeviceRegHostCount_Type()
)
avclDeviceRegHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceRegHostCount.setStatus("mandatory")
_AvclDeviceRegHosts_Type = AvcLongString
_AvclDeviceRegHosts_Object = MibTableColumn
avclDeviceRegHosts = _AvclDeviceRegHosts_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 25),
    _AvclDeviceRegHosts_Type()
)
avclDeviceRegHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceRegHosts.setStatus("mandatory")
_AvclDeviceLuToMirrorCount_Type = AvcCounter
_AvclDeviceLuToMirrorCount_Object = MibTableColumn
avclDeviceLuToMirrorCount = _AvclDeviceLuToMirrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 26),
    _AvclDeviceLuToMirrorCount_Type()
)
avclDeviceLuToMirrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceLuToMirrorCount.setStatus("mandatory")
_AvclDeviceLunsToMirror_Type = AvcLongString
_AvclDeviceLunsToMirror_Object = MibTableColumn
avclDeviceLunsToMirror = _AvclDeviceLunsToMirror_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 27),
    _AvclDeviceLunsToMirror_Type()
)
avclDeviceLunsToMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceLunsToMirror.setStatus("mandatory")
_AvclDeviceRaidGrpCount_Type = AvcCounter
_AvclDeviceRaidGrpCount_Object = MibTableColumn
avclDeviceRaidGrpCount = _AvclDeviceRaidGrpCount_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 28),
    _AvclDeviceRaidGrpCount_Type()
)
avclDeviceRaidGrpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceRaidGrpCount.setStatus("mandatory")
_AvclDeviceRaidGrpsState_Type = AvcLongString
_AvclDeviceRaidGrpsState_Object = MibTableColumn
avclDeviceRaidGrpsState = _AvclDeviceRaidGrpsState_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 29),
    _AvclDeviceRaidGrpsState_Type()
)
avclDeviceRaidGrpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceRaidGrpsState.setStatus("mandatory")
_AvclDeviceRaidGrpsDriveCount_Type = AvcLongString
_AvclDeviceRaidGrpsDriveCount_Object = MibTableColumn
avclDeviceRaidGrpsDriveCount = _AvclDeviceRaidGrpsDriveCount_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 30),
    _AvclDeviceRaidGrpsDriveCount_Type()
)
avclDeviceRaidGrpsDriveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceRaidGrpsDriveCount.setStatus("mandatory")
_AvclDeviceRaidGrpsSize_Type = AvcLongString
_AvclDeviceRaidGrpsSize_Object = MibTableColumn
avclDeviceRaidGrpsSize = _AvclDeviceRaidGrpsSize_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 31),
    _AvclDeviceRaidGrpsSize_Type()
)
avclDeviceRaidGrpsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceRaidGrpsSize.setStatus("mandatory")
_AvclDeviceRaidGrpsLuUnderSurfaceVerify_Type = AvcLongString
_AvclDeviceRaidGrpsLuUnderSurfaceVerify_Object = MibTableColumn
avclDeviceRaidGrpsLuUnderSurfaceVerify = _AvclDeviceRaidGrpsLuUnderSurfaceVerify_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 32),
    _AvclDeviceRaidGrpsLuUnderSurfaceVerify_Type()
)
avclDeviceRaidGrpsLuUnderSurfaceVerify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceRaidGrpsLuUnderSurfaceVerify.setStatus("mandatory")
_AvclDeviceRaidGrpsSurfaceVerifyProgress_Type = AvcLongString
_AvclDeviceRaidGrpsSurfaceVerifyProgress_Object = MibTableColumn
avclDeviceRaidGrpsSurfaceVerifyProgress = _AvclDeviceRaidGrpsSurfaceVerifyProgress_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 33),
    _AvclDeviceRaidGrpsSurfaceVerifyProgress_Type()
)
avclDeviceRaidGrpsSurfaceVerifyProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceRaidGrpsSurfaceVerifyProgress.setStatus("mandatory")
_AvclDeviceRaidGrpsInitReconProgress_Type = AvcLongString
_AvclDeviceRaidGrpsInitReconProgress_Object = MibTableColumn
avclDeviceRaidGrpsInitReconProgress = _AvclDeviceRaidGrpsInitReconProgress_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 34),
    _AvclDeviceRaidGrpsInitReconProgress_Type()
)
avclDeviceRaidGrpsInitReconProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceRaidGrpsInitReconProgress.setStatus("mandatory")
_AvclDeviceRaidGrpsFreeSpace_Type = AvcLongString
_AvclDeviceRaidGrpsFreeSpace_Object = MibTableColumn
avclDeviceRaidGrpsFreeSpace = _AvclDeviceRaidGrpsFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 35),
    _AvclDeviceRaidGrpsFreeSpace_Type()
)
avclDeviceRaidGrpsFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceRaidGrpsFreeSpace.setStatus("mandatory")
_AvclDeviceSpareCount_Type = AvcCounter
_AvclDeviceSpareCount_Object = MibTableColumn
avclDeviceSpareCount = _AvclDeviceSpareCount_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 36),
    _AvclDeviceSpareCount_Type()
)
avclDeviceSpareCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceSpareCount.setStatus("mandatory")
_AvclDeviceSparesState_Type = AvcLongString
_AvclDeviceSparesState_Object = MibTableColumn
avclDeviceSparesState = _AvclDeviceSparesState_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 37),
    _AvclDeviceSparesState_Type()
)
avclDeviceSparesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceSparesState.setStatus("mandatory")
_AvclDeviceSparesRaidGrpNumber_Type = AvcLongString
_AvclDeviceSparesRaidGrpNumber_Object = MibTableColumn
avclDeviceSparesRaidGrpNumber = _AvclDeviceSparesRaidGrpNumber_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 38),
    _AvclDeviceSparesRaidGrpNumber_Type()
)
avclDeviceSparesRaidGrpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceSparesRaidGrpNumber.setStatus("mandatory")
_AvclDeviceVolumeCount_Type = AvcCounter
_AvclDeviceVolumeCount_Object = MibTableColumn
avclDeviceVolumeCount = _AvclDeviceVolumeCount_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 39),
    _AvclDeviceVolumeCount_Type()
)
avclDeviceVolumeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceVolumeCount.setStatus("mandatory")
_AvclDeviceVolumesState_Type = AvcLongString
_AvclDeviceVolumesState_Object = MibTableColumn
avclDeviceVolumesState = _AvclDeviceVolumesState_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 40),
    _AvclDeviceVolumesState_Type()
)
avclDeviceVolumesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceVolumesState.setStatus("mandatory")
_AvclDeviceVolumesRaidGrpNumber_Type = AvcLongString
_AvclDeviceVolumesRaidGrpNumber_Object = MibTableColumn
avclDeviceVolumesRaidGrpNumber = _AvclDeviceVolumesRaidGrpNumber_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 41),
    _AvclDeviceVolumesRaidGrpNumber_Type()
)
avclDeviceVolumesRaidGrpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceVolumesRaidGrpNumber.setStatus("mandatory")
_AvclDeviceVolumesRaidLevel_Type = AvcLongString
_AvclDeviceVolumesRaidLevel_Object = MibTableColumn
avclDeviceVolumesRaidLevel = _AvclDeviceVolumesRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 42),
    _AvclDeviceVolumesRaidLevel_Type()
)
avclDeviceVolumesRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceVolumesRaidLevel.setStatus("mandatory")
_AvclDeviceVolumesSize_Type = AvcLongString
_AvclDeviceVolumesSize_Object = MibTableColumn
avclDeviceVolumesSize = _AvclDeviceVolumesSize_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 43),
    _AvclDeviceVolumesSize_Type()
)
avclDeviceVolumesSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceVolumesSize.setStatus("mandatory")
_AvclDeviceVolumesInitProgress_Type = AvcLongString
_AvclDeviceVolumesInitProgress_Object = MibTableColumn
avclDeviceVolumesInitProgress = _AvclDeviceVolumesInitProgress_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 44),
    _AvclDeviceVolumesInitProgress_Type()
)
avclDeviceVolumesInitProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceVolumesInitProgress.setStatus("mandatory")
_AvclDeviceVolumesNickname_Type = AvcLongString
_AvclDeviceVolumesNickname_Object = MibTableColumn
avclDeviceVolumesNickname = _AvclDeviceVolumesNickname_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 45),
    _AvclDeviceVolumesNickname_Type()
)
avclDeviceVolumesNickname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceVolumesNickname.setStatus("mandatory")
_AvclDeviceDriveCount_Type = AvcCounter
_AvclDeviceDriveCount_Object = MibTableColumn
avclDeviceDriveCount = _AvclDeviceDriveCount_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 46),
    _AvclDeviceDriveCount_Type()
)
avclDeviceDriveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceDriveCount.setStatus("mandatory")
_AvclDeviceDrivesState_Type = AvcLongString
_AvclDeviceDrivesState_Object = MibTableColumn
avclDeviceDrivesState = _AvclDeviceDrivesState_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 47),
    _AvclDeviceDrivesState_Type()
)
avclDeviceDrivesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceDrivesState.setStatus("mandatory")
_AvclDeviceDrivesUsageType_Type = AvcLongString
_AvclDeviceDrivesUsageType_Object = MibTableColumn
avclDeviceDrivesUsageType = _AvclDeviceDrivesUsageType_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 48),
    _AvclDeviceDrivesUsageType_Type()
)
avclDeviceDrivesUsageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceDrivesUsageType.setStatus("mandatory")
_AvclDeviceDrivesRaidGrpOrSpareNumber_Type = AvcLongString
_AvclDeviceDrivesRaidGrpOrSpareNumber_Object = MibTableColumn
avclDeviceDrivesRaidGrpOrSpareNumber = _AvclDeviceDrivesRaidGrpOrSpareNumber_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 49),
    _AvclDeviceDrivesRaidGrpOrSpareNumber_Type()
)
avclDeviceDrivesRaidGrpOrSpareNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceDrivesRaidGrpOrSpareNumber.setStatus("mandatory")
_AvclDeviceComponentCount_Type = AvcCounter
_AvclDeviceComponentCount_Object = MibTableColumn
avclDeviceComponentCount = _AvclDeviceComponentCount_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 50),
    _AvclDeviceComponentCount_Type()
)
avclDeviceComponentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceComponentCount.setStatus("mandatory")
_AvclDeviceComponentsType_Type = AvcLongString
_AvclDeviceComponentsType_Object = MibTableColumn
avclDeviceComponentsType = _AvclDeviceComponentsType_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 51),
    _AvclDeviceComponentsType_Type()
)
avclDeviceComponentsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceComponentsType.setStatus("mandatory")
_AvclDeviceComponentsState_Type = AvcLongString
_AvclDeviceComponentsState_Object = MibTableColumn
avclDeviceComponentsState = _AvclDeviceComponentsState_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 52),
    _AvclDeviceComponentsState_Type()
)
avclDeviceComponentsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceComponentsState.setStatus("mandatory")
_AvclDeviceComponentsInstanceNumber_Type = AvcLongString
_AvclDeviceComponentsInstanceNumber_Object = MibTableColumn
avclDeviceComponentsInstanceNumber = _AvclDeviceComponentsInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2653, 3, 1, 1, 6, 1, 53),
    _AvclDeviceComponentsInstanceNumber_Type()
)
avclDeviceComponentsInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avclDeviceComponentsInstanceNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects

daemonEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2653, 0, 1)
)
daemonEvent.setObjects(
    ("ADTX-RAID-AVCL-MIB", "avclEventInfo")
)
if mibBuilder.loadTexts:
    daemonEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTX-RAID-AVCL-MIB",
    **{"AvcString": AvcString,
       "AvcLongString": AvcLongString,
       "AvcCounter": AvcCounter,
       "AvcInteger": AvcInteger,
       "daemonEvent": daemonEvent,
       "avc": avc,
       "avcl": avcl,
       "avclVersion": avclVersion,
       "avclOS": avclOS,
       "avclHost": avclHost,
       "avclNumOfDevices": avclNumOfDevices,
       "avclEventInfo": avclEventInfo,
       "avclDeviceInformationTable": avclDeviceInformationTable,
       "avclDeviceInformationEntry": avclDeviceInformationEntry,
       "avclDeviceIndex": avclDeviceIndex,
       "avclDeviceIP": avclDeviceIP,
       "avclDeviceSystemVersion": avclDeviceSystemVersion,
       "avclDeviceManufacturer": avclDeviceManufacturer,
       "avclDeviceProductName": avclDeviceProductName,
       "avclDeviceRevisionLevel": avclDeviceRevisionLevel,
       "avclDeviceSerialNumber": avclDeviceSerialNumber,
       "avclDeviceDate": avclDeviceDate,
       "avclDeviceTime": avclDeviceTime,
       "avclDeviceAssignedSpare": avclDeviceAssignedSpare,
       "avclDeviceInitiatorMode": avclDeviceInitiatorMode,
       "avclDeviceInstantCopyLicense": avclDeviceInstantCopyLicense,
       "avclDeviceMirroringLicense": avclDeviceMirroringLicense,
       "avclDeviceWWNInfoCount": avclDeviceWWNInfoCount,
       "avclDeviceWWNInfo": avclDeviceWWNInfo,
       "avclDeviceSurfaceSchedMode": avclDeviceSurfaceSchedMode,
       "avclDeviceSurfaceSchedTime": avclDeviceSurfaceSchedTime,
       "avclDeviceSurfaceVerifyDuration": avclDeviceSurfaceVerifyDuration,
       "avclDeviceICSourceLU": avclDeviceICSourceLU,
       "avclDeviceICTargetLU": avclDeviceICTargetLU,
       "avclDeviceICFlag": avclDeviceICFlag,
       "avclDeviceICProgress": avclDeviceICProgress,
       "avclDeviceICPairWWN": avclDeviceICPairWWN,
       "avclDeviceRegHostCount": avclDeviceRegHostCount,
       "avclDeviceRegHosts": avclDeviceRegHosts,
       "avclDeviceLuToMirrorCount": avclDeviceLuToMirrorCount,
       "avclDeviceLunsToMirror": avclDeviceLunsToMirror,
       "avclDeviceRaidGrpCount": avclDeviceRaidGrpCount,
       "avclDeviceRaidGrpsState": avclDeviceRaidGrpsState,
       "avclDeviceRaidGrpsDriveCount": avclDeviceRaidGrpsDriveCount,
       "avclDeviceRaidGrpsSize": avclDeviceRaidGrpsSize,
       "avclDeviceRaidGrpsLuUnderSurfaceVerify": avclDeviceRaidGrpsLuUnderSurfaceVerify,
       "avclDeviceRaidGrpsSurfaceVerifyProgress": avclDeviceRaidGrpsSurfaceVerifyProgress,
       "avclDeviceRaidGrpsInitReconProgress": avclDeviceRaidGrpsInitReconProgress,
       "avclDeviceRaidGrpsFreeSpace": avclDeviceRaidGrpsFreeSpace,
       "avclDeviceSpareCount": avclDeviceSpareCount,
       "avclDeviceSparesState": avclDeviceSparesState,
       "avclDeviceSparesRaidGrpNumber": avclDeviceSparesRaidGrpNumber,
       "avclDeviceVolumeCount": avclDeviceVolumeCount,
       "avclDeviceVolumesState": avclDeviceVolumesState,
       "avclDeviceVolumesRaidGrpNumber": avclDeviceVolumesRaidGrpNumber,
       "avclDeviceVolumesRaidLevel": avclDeviceVolumesRaidLevel,
       "avclDeviceVolumesSize": avclDeviceVolumesSize,
       "avclDeviceVolumesInitProgress": avclDeviceVolumesInitProgress,
       "avclDeviceVolumesNickname": avclDeviceVolumesNickname,
       "avclDeviceDriveCount": avclDeviceDriveCount,
       "avclDeviceDrivesState": avclDeviceDrivesState,
       "avclDeviceDrivesUsageType": avclDeviceDrivesUsageType,
       "avclDeviceDrivesRaidGrpOrSpareNumber": avclDeviceDrivesRaidGrpOrSpareNumber,
       "avclDeviceComponentCount": avclDeviceComponentCount,
       "avclDeviceComponentsType": avclDeviceComponentsType,
       "avclDeviceComponentsState": avclDeviceComponentsState,
       "avclDeviceComponentsInstanceNumber": avclDeviceComponentsInstanceNumber}
)
