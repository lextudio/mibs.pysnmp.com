# SNMP MIB module (DNS120005-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNS120005-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:25 2024
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

_D_link_ObjectIdentity = ObjectIdentity
d_link = _D_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_ProductID_ObjectIdentity = ObjectIdentity
productID = _ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50)
)
_ProjectID_ObjectIdentity = ObjectIdentity
projectID = _ProjectID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50, 1)
)
_ModelID_ObjectIdentity = ObjectIdentity
modelID = _ModelID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1)
)
_SubmodelID_ObjectIdentity = ObjectIdentity
submodelID = _SubmodelID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1)
)
_NasAgent1200_ObjectIdentity = ObjectIdentity
nasAgent1200 = _NasAgent1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1)
)
_NasAgentVer_Type = DisplayString
_NasAgentVer_Object = MibScalar
nasAgentVer = _NasAgentVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 1),
    _NasAgentVer_Type()
)
nasAgentVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasAgentVer.setStatus("current")
_SysTable_Object = MibTable
sysTable = _SysTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sysTable.setStatus("current")
_SysEntry_Object = MibTableRow
sysEntry = _SysEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1)
)
sysEntry.setIndexNames(
    (0, "DNS120005-MIB", "sysNum"),
)
if mibBuilder.loadTexts:
    sysEntry.setStatus("current")
_SysNum_Type = Integer32
_SysNum_Object = MibTableColumn
sysNum = _SysNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 1),
    _SysNum_Type()
)
sysNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNum.setStatus("current")
_SysName_Type = DisplayString
_SysName_Object = MibTableColumn
sysName = _SysName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 2),
    _SysName_Type()
)
sysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysName.setStatus("current")
_SysFWVer_Type = DisplayString
_SysFWVer_Object = MibTableColumn
sysFWVer = _SysFWVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 3),
    _SysFWVer_Type()
)
sysFWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFWVer.setStatus("current")
_SysNetType_Type = DisplayString
_SysNetType_Object = MibTableColumn
sysNetType = _SysNetType_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 4),
    _SysNetType_Type()
)
sysNetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetType.setStatus("current")
_SysFanSpeed_Type = DisplayString
_SysFanSpeed_Object = MibTableColumn
sysFanSpeed = _SysFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 5),
    _SysFanSpeed_Type()
)
sysFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanSpeed.setStatus("current")
_SysTemperature_Type = DisplayString
_SysTemperature_Object = MibTableColumn
sysTemperature = _SysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 6),
    _SysTemperature_Type()
)
sysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTemperature.setStatus("current")
_SysPrinterName_Type = DisplayString
_SysPrinterName_Object = MibTableColumn
sysPrinterName = _SysPrinterName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 7),
    _SysPrinterName_Type()
)
sysPrinterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPrinterName.setStatus("current")
_SysCIFS_Type = DisplayString
_SysCIFS_Object = MibTableColumn
sysCIFS = _SysCIFS_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 8),
    _SysCIFS_Type()
)
sysCIFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCIFS.setStatus("current")
_SysFtpServer_Type = DisplayString
_SysFtpServer_Object = MibTableColumn
sysFtpServer = _SysFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 9),
    _SysFtpServer_Type()
)
sysFtpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFtpServer.setStatus("current")
_SysNFSServer_Type = DisplayString
_SysNFSServer_Object = MibTableColumn
sysNFSServer = _SysNFSServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 10),
    _SysNFSServer_Type()
)
sysNFSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNFSServer.setStatus("current")
_SysDFSServer_Type = DisplayString
_SysDFSServer_Object = MibTableColumn
sysDFSServer = _SysDFSServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 11),
    _SysDFSServer_Type()
)
sysDFSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDFSServer.setStatus("current")
_SysQuota_Type = DisplayString
_SysQuota_Object = MibTableColumn
sysQuota = _SysQuota_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 12),
    _SysQuota_Type()
)
sysQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysQuota.setStatus("current")
_SysAFP_Type = DisplayString
_SysAFP_Object = MibTableColumn
sysAFP = _SysAFP_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 13),
    _SysAFP_Type()
)
sysAFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAFP.setStatus("current")
_SysWebDAV_Type = DisplayString
_SysWebDAV_Object = MibTableColumn
sysWebDAV = _SysWebDAV_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 14),
    _SysWebDAV_Type()
)
sysWebDAV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysWebDAV.setStatus("current")
_SysWebFileServer_Type = DisplayString
_SysWebFileServer_Object = MibTableColumn
sysWebFileServer = _SysWebFileServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 15),
    _SysWebFileServer_Type()
)
sysWebFileServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysWebFileServer.setStatus("current")
_SysiSCSITarget_Type = DisplayString
_SysiSCSITarget_Object = MibTableColumn
sysiSCSITarget = _SysiSCSITarget_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 16),
    _SysiSCSITarget_Type()
)
sysiSCSITarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysiSCSITarget.setStatus("current")
_SysiSNS_Type = DisplayString
_SysiSNS_Object = MibTableColumn
sysiSNS = _SysiSNS_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 2, 1, 17),
    _SysiSNS_Type()
)
sysiSNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysiSNS.setStatus("current")
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("current")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 3, 1)
)
diskEntry.setIndexNames(
    (0, "DNS120005-MIB", "diskNum"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("current")
_DiskNum_Type = Integer32
_DiskNum_Object = MibTableColumn
diskNum = _DiskNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 3, 1, 1),
    _DiskNum_Type()
)
diskNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskNum.setStatus("current")
_DiskName_Type = DisplayString
_DiskName_Object = MibTableColumn
diskName = _DiskName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 3, 1, 2),
    _DiskName_Type()
)
diskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskName.setStatus("current")
_DiskModel_Type = DisplayString
_DiskModel_Object = MibTableColumn
diskModel = _DiskModel_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 3, 1, 3),
    _DiskModel_Type()
)
diskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskModel.setStatus("current")
_DiskTemperature_Type = DisplayString
_DiskTemperature_Object = MibTableColumn
diskTemperature = _DiskTemperature_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 3, 1, 4),
    _DiskTemperature_Type()
)
diskTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTemperature.setStatus("current")
_DiskCapacity_Type = DisplayString
_DiskCapacity_Object = MibTableColumn
diskCapacity = _DiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 3, 1, 5),
    _DiskCapacity_Type()
)
diskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskCapacity.setStatus("current")
_DiskStatus_Type = DisplayString
_DiskStatus_Object = MibTableColumn
diskStatus = _DiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 3, 1, 6),
    _DiskStatus_Type()
)
diskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatus.setStatus("current")
_VolumeTable_Object = MibTable
volumeTable = _VolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    volumeTable.setStatus("current")
_VolumeEntry_Object = MibTableRow
volumeEntry = _VolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 4, 1)
)
volumeEntry.setIndexNames(
    (0, "DNS120005-MIB", "volumeNum"),
)
if mibBuilder.loadTexts:
    volumeEntry.setStatus("current")
_VolumeNum_Type = Integer32
_VolumeNum_Object = MibTableColumn
volumeNum = _VolumeNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 4, 1, 1),
    _VolumeNum_Type()
)
volumeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeNum.setStatus("current")
_VolumeName_Type = DisplayString
_VolumeName_Object = MibTableColumn
volumeName = _VolumeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 4, 1, 2),
    _VolumeName_Type()
)
volumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeName.setStatus("current")
_VolumeEncryption_Type = DisplayString
_VolumeEncryption_Object = MibTableColumn
volumeEncryption = _VolumeEncryption_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 4, 1, 3),
    _VolumeEncryption_Type()
)
volumeEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeEncryption.setStatus("current")
_VolumeFsType_Type = DisplayString
_VolumeFsType_Object = MibTableColumn
volumeFsType = _VolumeFsType_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 4, 1, 4),
    _VolumeFsType_Type()
)
volumeFsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeFsType.setStatus("current")
_VolumeRaidLevel_Type = DisplayString
_VolumeRaidLevel_Object = MibTableColumn
volumeRaidLevel = _VolumeRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 4, 1, 5),
    _VolumeRaidLevel_Type()
)
volumeRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeRaidLevel.setStatus("current")
_VolumeSize_Type = DisplayString
_VolumeSize_Object = MibTableColumn
volumeSize = _VolumeSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 4, 1, 6),
    _VolumeSize_Type()
)
volumeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeSize.setStatus("current")
_VolumeFreeSpace_Type = DisplayString
_VolumeFreeSpace_Object = MibTableColumn
volumeFreeSpace = _VolumeFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 4, 1, 7),
    _VolumeFreeSpace_Type()
)
volumeFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeFreeSpace.setStatus("current")
_VolumeState_Type = DisplayString
_VolumeState_Object = MibTableColumn
volumeState = _VolumeState_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 4, 1, 8),
    _VolumeState_Type()
)
volumeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeState.setStatus("current")
_SnapShotTable_Object = MibTable
snapShotTable = _SnapShotTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    snapShotTable.setStatus("current")
_SnapShotEntry_Object = MibTableRow
snapShotEntry = _SnapShotEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 5, 1)
)
snapShotEntry.setIndexNames(
    (0, "DNS120005-MIB", "snapShotNum"),
)
if mibBuilder.loadTexts:
    snapShotEntry.setStatus("current")
_SnapShotNum_Type = Integer32
_SnapShotNum_Object = MibTableColumn
snapShotNum = _SnapShotNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 5, 1, 1),
    _SnapShotNum_Type()
)
snapShotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapShotNum.setStatus("current")
_SnapShotVolume_Type = DisplayString
_SnapShotVolume_Object = MibTableColumn
snapShotVolume = _SnapShotVolume_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 5, 1, 2),
    _SnapShotVolume_Type()
)
snapShotVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapShotVolume.setStatus("current")
_SnapShotName_Type = DisplayString
_SnapShotName_Object = MibTableColumn
snapShotName = _SnapShotName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 5, 1, 3),
    _SnapShotName_Type()
)
snapShotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapShotName.setStatus("current")
_SnapShotSchedule_Type = DisplayString
_SnapShotSchedule_Object = MibTableColumn
snapShotSchedule = _SnapShotSchedule_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 5, 1, 4),
    _SnapShotSchedule_Type()
)
snapShotSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapShotSchedule.setStatus("current")
_SnapShotCount_Type = DisplayString
_SnapShotCount_Object = MibTableColumn
snapShotCount = _SnapShotCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 5, 1, 5),
    _SnapShotCount_Type()
)
snapShotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapShotCount.setStatus("current")
_SnapShotState_Type = DisplayString
_SnapShotState_Object = MibTableColumn
snapShotState = _SnapShotState_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 5, 1, 6),
    _SnapShotState_Type()
)
snapShotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapShotState.setStatus("current")
_SnapShotPath_Type = DisplayString
_SnapShotPath_Object = MibTableColumn
snapShotPath = _SnapShotPath_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 5, 1, 7),
    _SnapShotPath_Type()
)
snapShotPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapShotPath.setStatus("current")
_DFSTable_Object = MibTable
dFSTable = _DFSTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    dFSTable.setStatus("current")
_DFSEntry_Object = MibTableRow
dFSEntry = _DFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 6, 1)
)
dFSEntry.setIndexNames(
    (0, "DNS120005-MIB", "dFSNum"),
)
if mibBuilder.loadTexts:
    dFSEntry.setStatus("current")
_DFSNum_Type = Integer32
_DFSNum_Object = MibTableColumn
dFSNum = _DFSNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 6, 1, 1),
    _DFSNum_Type()
)
dFSNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFSNum.setStatus("current")
_DFSLShareName_Type = DisplayString
_DFSLShareName_Object = MibTableColumn
dFSLShareName = _DFSLShareName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 6, 1, 2),
    _DFSLShareName_Type()
)
dFSLShareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFSLShareName.setStatus("current")
_DFSHost_Type = DisplayString
_DFSHost_Object = MibTableColumn
dFSHost = _DFSHost_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 6, 1, 3),
    _DFSHost_Type()
)
dFSHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFSHost.setStatus("current")
_DFSRSharefolder_Type = DisplayString
_DFSRSharefolder_Object = MibTableColumn
dFSRSharefolder = _DFSRSharefolder_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 6, 1, 4),
    _DFSRSharefolder_Type()
)
dFSRSharefolder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFSRSharefolder.setStatus("current")
_NFSTable_Object = MibTable
nFSTable = _NFSTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    nFSTable.setStatus("current")
_NFSEntry_Object = MibTableRow
nFSEntry = _NFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 7, 1)
)
nFSEntry.setIndexNames(
    (0, "DNS120005-MIB", "nFSNum"),
)
if mibBuilder.loadTexts:
    nFSEntry.setStatus("current")
_NFSNum_Type = Integer32
_NFSNum_Object = MibTableColumn
nFSNum = _NFSNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 7, 1, 1),
    _NFSNum_Type()
)
nFSNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nFSNum.setStatus("current")
_NFSMountPath_Type = DisplayString
_NFSMountPath_Object = MibTableColumn
nFSMountPath = _NFSMountPath_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 7, 1, 2),
    _NFSMountPath_Type()
)
nFSMountPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nFSMountPath.setStatus("current")
_NFSHost_Type = DisplayString
_NFSHost_Object = MibTableColumn
nFSHost = _NFSHost_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 7, 1, 3),
    _NFSHost_Type()
)
nFSHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nFSHost.setStatus("current")
_NFSPermission_Type = DisplayString
_NFSPermission_Object = MibTableColumn
nFSPermission = _NFSPermission_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 7, 1, 4),
    _NFSPermission_Type()
)
nFSPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nFSPermission.setStatus("current")
_NFSRootSquash_Type = DisplayString
_NFSRootSquash_Object = MibTableColumn
nFSRootSquash = _NFSRootSquash_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 7, 1, 5),
    _NFSRootSquash_Type()
)
nFSRootSquash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nFSRootSquash.setStatus("current")
_NFSStatus_Type = DisplayString
_NFSStatus_Object = MibTableColumn
nFSStatus = _NFSStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 7, 1, 6),
    _NFSStatus_Type()
)
nFSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nFSStatus.setStatus("current")
_ISOTable_Object = MibTable
iSOTable = _ISOTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    iSOTable.setStatus("current")
_ISOEntry_Object = MibTableRow
iSOEntry = _ISOEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 8, 1)
)
iSOEntry.setIndexNames(
    (0, "DNS120005-MIB", "iSONum"),
)
if mibBuilder.loadTexts:
    iSOEntry.setStatus("current")
_ISONum_Type = Integer32
_ISONum_Object = MibTableColumn
iSONum = _ISONum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 8, 1, 1),
    _ISONum_Type()
)
iSONum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSONum.setStatus("current")
_ISOShareName_Type = DisplayString
_ISOShareName_Object = MibTableColumn
iSOShareName = _ISOShareName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 8, 1, 2),
    _ISOShareName_Type()
)
iSOShareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSOShareName.setStatus("current")
_ISOPath_Type = DisplayString
_ISOPath_Object = MibTableColumn
iSOPath = _ISOPath_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 8, 1, 3),
    _ISOPath_Type()
)
iSOPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSOPath.setStatus("current")
_ISOStatus_Type = DisplayString
_ISOStatus_Object = MibTableColumn
iSOStatus = _ISOStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 8, 1, 4),
    _ISOStatus_Type()
)
iSOStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSOStatus.setStatus("current")
_LogServerTable_Object = MibTable
logServerTable = _LogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    logServerTable.setStatus("current")
_LogServerEntry_Object = MibTableRow
logServerEntry = _LogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 9, 1)
)
logServerEntry.setIndexNames(
    (0, "DNS120005-MIB", "logServerNum"),
)
if mibBuilder.loadTexts:
    logServerEntry.setStatus("current")
_LogServerNum_Type = Integer32
_LogServerNum_Object = MibTableColumn
logServerNum = _LogServerNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 9, 1, 1),
    _LogServerNum_Type()
)
logServerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logServerNum.setStatus("current")
_LogServerRuleName_Type = DisplayString
_LogServerRuleName_Object = MibTableColumn
logServerRuleName = _LogServerRuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 9, 1, 2),
    _LogServerRuleName_Type()
)
logServerRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logServerRuleName.setStatus("current")
_LogServerLogfiles_Type = DisplayString
_LogServerLogfiles_Object = MibTableColumn
logServerLogfiles = _LogServerLogfiles_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 9, 1, 3),
    _LogServerLogfiles_Type()
)
logServerLogfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logServerLogfiles.setStatus("current")
_LogServerStatus_Type = DisplayString
_LogServerStatus_Object = MibTableColumn
logServerStatus = _LogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 9, 1, 4),
    _LogServerStatus_Type()
)
logServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logServerStatus.setStatus("current")
_UPSTable_Object = MibTable
uPSTable = _UPSTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    uPSTable.setStatus("current")
_UPSEntry_Object = MibTableRow
uPSEntry = _UPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 10, 1)
)
uPSEntry.setIndexNames(
    (0, "DNS120005-MIB", "uPSNum"),
)
if mibBuilder.loadTexts:
    uPSEntry.setStatus("current")
_UPSNum_Type = Integer32
_UPSNum_Object = MibTableColumn
uPSNum = _UPSNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 10, 1, 1),
    _UPSNum_Type()
)
uPSNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSNum.setStatus("current")
_UPSDeviceInfo_Type = DisplayString
_UPSDeviceInfo_Object = MibTableColumn
uPSDeviceInfo = _UPSDeviceInfo_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 10, 1, 2),
    _UPSDeviceInfo_Type()
)
uPSDeviceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSDeviceInfo.setStatus("current")
_UPSProduct_Type = DisplayString
_UPSProduct_Object = MibTableColumn
uPSProduct = _UPSProduct_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 10, 1, 3),
    _UPSProduct_Type()
)
uPSProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSProduct.setStatus("current")
_UPSManufacturer_Type = DisplayString
_UPSManufacturer_Object = MibTableColumn
uPSManufacturer = _UPSManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 10, 1, 4),
    _UPSManufacturer_Type()
)
uPSManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSManufacturer.setStatus("current")
_UPSBattery_Type = DisplayString
_UPSBattery_Object = MibTableColumn
uPSBattery = _UPSBattery_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 10, 1, 5),
    _UPSBattery_Type()
)
uPSBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSBattery.setStatus("current")
_UPSState_Type = DisplayString
_UPSState_Object = MibTableColumn
uPSState = _UPSState_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 10, 1, 6),
    _UPSState_Type()
)
uPSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSState.setStatus("current")
_UPSServerIP_Type = DisplayString
_UPSServerIP_Object = MibTableColumn
uPSServerIP = _UPSServerIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 10, 1, 7),
    _UPSServerIP_Type()
)
uPSServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSServerIP.setStatus("current")
_UPSAllowedIP_Type = DisplayString
_UPSAllowedIP_Object = MibTableColumn
uPSAllowedIP = _UPSAllowedIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 10, 1, 8),
    _UPSAllowedIP_Type()
)
uPSAllowedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uPSAllowedIP.setStatus("current")
_VVTable_Object = MibTable
vVTable = _VVTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    vVTable.setStatus("current")
_VVEntry_Object = MibTableRow
vVEntry = _VVEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 11, 1)
)
vVEntry.setIndexNames(
    (0, "DNS120005-MIB", "vVNum"),
)
if mibBuilder.loadTexts:
    vVEntry.setStatus("current")
_VVNum_Type = Integer32
_VVNum_Object = MibTableColumn
vVNum = _VVNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 11, 1, 1),
    _VVNum_Type()
)
vVNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vVNum.setStatus("current")
_VVTargetName_Type = DisplayString
_VVTargetName_Object = MibTableColumn
vVTargetName = _VVTargetName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 11, 1, 2),
    _VVTargetName_Type()
)
vVTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vVTargetName.setStatus("current")
_VVSharefolder_Type = DisplayString
_VVSharefolder_Object = MibTableColumn
vVSharefolder = _VVSharefolder_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 11, 1, 3),
    _VVSharefolder_Type()
)
vVSharefolder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vVSharefolder.setStatus("current")
_VVStatus_Type = DisplayString
_VVStatus_Object = MibTableColumn
vVStatus = _VVStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 11, 1, 4),
    _VVStatus_Type()
)
vVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vVStatus.setStatus("current")
_VVSize_Type = DisplayString
_VVSize_Object = MibTableColumn
vVSize = _VVSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 11, 1, 5),
    _VVSize_Type()
)
vVSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vVSize.setStatus("current")
_ISCSITargetTable_Object = MibTable
iSCSITargetTable = _ISCSITargetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    iSCSITargetTable.setStatus("current")
_ISCSITargetEntry_Object = MibTableRow
iSCSITargetEntry = _ISCSITargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 12, 1)
)
iSCSITargetEntry.setIndexNames(
    (0, "DNS120005-MIB", "iSCSITargetNum"),
)
if mibBuilder.loadTexts:
    iSCSITargetEntry.setStatus("current")
_ISCSITargetNum_Type = Integer32
_ISCSITargetNum_Object = MibTableColumn
iSCSITargetNum = _ISCSITargetNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 12, 1, 1),
    _ISCSITargetNum_Type()
)
iSCSITargetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSITargetNum.setStatus("current")
_ISCSITargetIQN_Type = DisplayString
_ISCSITargetIQN_Object = MibTableColumn
iSCSITargetIQN = _ISCSITargetIQN_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 12, 1, 2),
    _ISCSITargetIQN_Type()
)
iSCSITargetIQN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSITargetIQN.setStatus("current")
_ISCSITargetStatus_Type = DisplayString
_ISCSITargetStatus_Object = MibTableColumn
iSCSITargetStatus = _ISCSITargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 12, 1, 3),
    _ISCSITargetStatus_Type()
)
iSCSITargetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSITargetStatus.setStatus("current")
_ISCSILUNTable_Object = MibTable
iSCSILUNTable = _ISCSILUNTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    iSCSILUNTable.setStatus("current")
_ISCSILUNEntry_Object = MibTableRow
iSCSILUNEntry = _ISCSILUNEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 13, 1)
)
iSCSILUNEntry.setIndexNames(
    (0, "DNS120005-MIB", "iSCSILUNNum"),
)
if mibBuilder.loadTexts:
    iSCSILUNEntry.setStatus("current")
_ISCSILUNNum_Type = Integer32
_ISCSILUNNum_Object = MibTableColumn
iSCSILUNNum = _ISCSILUNNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 13, 1, 1),
    _ISCSILUNNum_Type()
)
iSCSILUNNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNNum.setStatus("current")
_ISCSILUNName_Type = DisplayString
_ISCSILUNName_Object = MibTableColumn
iSCSILUNName = _ISCSILUNName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 13, 1, 2),
    _ISCSILUNName_Type()
)
iSCSILUNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNName.setStatus("current")
_ISCSILUNVolume_Type = DisplayString
_ISCSILUNVolume_Object = MibTableColumn
iSCSILUNVolume = _ISCSILUNVolume_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 13, 1, 3),
    _ISCSILUNVolume_Type()
)
iSCSILUNVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNVolume.setStatus("current")
_ISCSILUNSize_Type = DisplayString
_ISCSILUNSize_Object = MibTableColumn
iSCSILUNSize = _ISCSILUNSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 13, 1, 4),
    _ISCSILUNSize_Type()
)
iSCSILUNSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNSize.setStatus("current")
_ISCSILUNStatus_Type = DisplayString
_ISCSILUNStatus_Object = MibTableColumn
iSCSILUNStatus = _ISCSILUNStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 13, 1, 5),
    _ISCSILUNStatus_Type()
)
iSCSILUNStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNStatus.setStatus("current")
_ISCSILUNMapping_Type = DisplayString
_ISCSILUNMapping_Object = MibTableColumn
iSCSILUNMapping = _ISCSILUNMapping_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 13, 1, 6),
    _ISCSILUNMapping_Type()
)
iSCSILUNMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNMapping.setStatus("current")
_ISCSIACLTable_Object = MibTable
iSCSIACLTable = _ISCSIACLTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    iSCSIACLTable.setStatus("current")
_ISCSIACLEntry_Object = MibTableRow
iSCSIACLEntry = _ISCSIACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 14, 1)
)
iSCSIACLEntry.setIndexNames(
    (0, "DNS120005-MIB", "iSCSIACLNum"),
)
if mibBuilder.loadTexts:
    iSCSIACLEntry.setStatus("current")
_ISCSIACLNum_Type = Integer32
_ISCSIACLNum_Object = MibTableColumn
iSCSIACLNum = _ISCSIACLNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 14, 1, 1),
    _ISCSIACLNum_Type()
)
iSCSIACLNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSIACLNum.setStatus("current")
_ISCSIACLName_Type = DisplayString
_ISCSIACLName_Object = MibTableColumn
iSCSIACLName = _ISCSIACLName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 14, 1, 2),
    _ISCSIACLName_Type()
)
iSCSIACLName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSIACLName.setStatus("current")
_ISCSIACLInitiator_Type = DisplayString
_ISCSIACLInitiator_Object = MibTableColumn
iSCSIACLInitiator = _ISCSIACLInitiator_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 14, 1, 3),
    _ISCSIACLInitiator_Type()
)
iSCSIACLInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSIACLInitiator.setStatus("current")
_AMAZONS3Table_Object = MibTable
aMAZONS3Table = _AMAZONS3Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    aMAZONS3Table.setStatus("current")
_AMAZONS3Entry_Object = MibTableRow
aMAZONS3Entry = _AMAZONS3Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 15, 1)
)
aMAZONS3Entry.setIndexNames(
    (0, "DNS120005-MIB", "aMAZONS3Num"),
)
if mibBuilder.loadTexts:
    aMAZONS3Entry.setStatus("current")
_AMAZONS3Num_Type = Integer32
_AMAZONS3Num_Object = MibTableColumn
aMAZONS3Num = _AMAZONS3Num_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 15, 1, 1),
    _AMAZONS3Num_Type()
)
aMAZONS3Num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMAZONS3Num.setStatus("current")
_AMAZONS3Task_Type = DisplayString
_AMAZONS3Task_Object = MibTableColumn
aMAZONS3Task = _AMAZONS3Task_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 15, 1, 2),
    _AMAZONS3Task_Type()
)
aMAZONS3Task.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMAZONS3Task.setStatus("current")
_AMAZONS3Schedule_Type = DisplayString
_AMAZONS3Schedule_Object = MibTableColumn
aMAZONS3Schedule = _AMAZONS3Schedule_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 15, 1, 3),
    _AMAZONS3Schedule_Type()
)
aMAZONS3Schedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMAZONS3Schedule.setStatus("current")
_AMAZONS3Status_Type = DisplayString
_AMAZONS3Status_Object = MibTableColumn
aMAZONS3Status = _AMAZONS3Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 15, 1, 4),
    _AMAZONS3Status_Type()
)
aMAZONS3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMAZONS3Status.setStatus("current")
_AMAZONS3Enable_Type = DisplayString
_AMAZONS3Enable_Object = MibTableColumn
aMAZONS3Enable = _AMAZONS3Enable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 15, 1, 5),
    _AMAZONS3Enable_Type()
)
aMAZONS3Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMAZONS3Enable.setStatus("current")
_AMAZONS3BackupNow_Type = DisplayString
_AMAZONS3BackupNow_Object = MibTableColumn
aMAZONS3BackupNow = _AMAZONS3BackupNow_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 15, 1, 6),
    _AMAZONS3BackupNow_Type()
)
aMAZONS3BackupNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMAZONS3BackupNow.setStatus("current")
_AMAZONS3Restore_Type = DisplayString
_AMAZONS3Restore_Object = MibTableColumn
aMAZONS3Restore = _AMAZONS3Restore_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 15, 1, 7),
    _AMAZONS3Restore_Type()
)
aMAZONS3Restore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMAZONS3Restore.setStatus("current")
_ConnectionTable_Object = MibTable
connectionTable = _ConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    connectionTable.setStatus("current")
_ConnectionEntry_Object = MibTableRow
connectionEntry = _ConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 16, 1)
)
connectionEntry.setIndexNames(
    (0, "DNS120005-MIB", "connectionNum"),
)
if mibBuilder.loadTexts:
    connectionEntry.setStatus("current")
_ConnectionNum_Type = Integer32
_ConnectionNum_Object = MibTableColumn
connectionNum = _ConnectionNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 16, 1, 1),
    _ConnectionNum_Type()
)
connectionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionNum.setStatus("current")
_ConnectionDateTime_Type = DisplayString
_ConnectionDateTime_Object = MibTableColumn
connectionDateTime = _ConnectionDateTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 16, 1, 2),
    _ConnectionDateTime_Type()
)
connectionDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionDateTime.setStatus("current")
_ConnectionServiceType_Type = DisplayString
_ConnectionServiceType_Object = MibTableColumn
connectionServiceType = _ConnectionServiceType_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 16, 1, 3),
    _ConnectionServiceType_Type()
)
connectionServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionServiceType.setStatus("current")
_ConnectionIPAddress_Type = DisplayString
_ConnectionIPAddress_Object = MibTableColumn
connectionIPAddress = _ConnectionIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 16, 1, 4),
    _ConnectionIPAddress_Type()
)
connectionIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionIPAddress.setStatus("current")
_ConnectionUser_Type = DisplayString
_ConnectionUser_Object = MibTableColumn
connectionUser = _ConnectionUser_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 16, 1, 5),
    _ConnectionUser_Type()
)
connectionUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionUser.setStatus("current")
_ConnectionComputerName_Type = DisplayString
_ConnectionComputerName_Object = MibTableColumn
connectionComputerName = _ConnectionComputerName_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 16, 1, 6),
    _ConnectionComputerName_Type()
)
connectionComputerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionComputerName.setStatus("current")
_ConnectionUsedResources_Type = DisplayString
_ConnectionUsedResources_Object = MibTableColumn
connectionUsedResources = _ConnectionUsedResources_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 16, 1, 7),
    _ConnectionUsedResources_Type()
)
connectionUsedResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionUsedResources.setStatus("current")
_PortForwardingTable_Object = MibTable
portForwardingTable = _PortForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 17)
)
if mibBuilder.loadTexts:
    portForwardingTable.setStatus("current")
_PortForwardingEntry_Object = MibTableRow
portForwardingEntry = _PortForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 17, 1)
)
portForwardingEntry.setIndexNames(
    (0, "DNS120005-MIB", "portForwardingNum"),
)
if mibBuilder.loadTexts:
    portForwardingEntry.setStatus("current")
_PortForwardingNum_Type = Integer32
_PortForwardingNum_Object = MibTableColumn
portForwardingNum = _PortForwardingNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 17, 1, 1),
    _PortForwardingNum_Type()
)
portForwardingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portForwardingNum.setStatus("current")
_PortForwardingEnable_Type = DisplayString
_PortForwardingEnable_Object = MibTableColumn
portForwardingEnable = _PortForwardingEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 17, 1, 2),
    _PortForwardingEnable_Type()
)
portForwardingEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portForwardingEnable.setStatus("current")
_PortForwardingStatus_Type = DisplayString
_PortForwardingStatus_Object = MibTableColumn
portForwardingStatus = _PortForwardingStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 17, 1, 3),
    _PortForwardingStatus_Type()
)
portForwardingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portForwardingStatus.setStatus("current")
_PortForwardingService_Type = DisplayString
_PortForwardingService_Object = MibTableColumn
portForwardingService = _PortForwardingService_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 17, 1, 4),
    _PortForwardingService_Type()
)
portForwardingService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portForwardingService.setStatus("current")
_PortForwardingProtocol_Type = DisplayString
_PortForwardingProtocol_Object = MibTableColumn
portForwardingProtocol = _PortForwardingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 17, 1, 5),
    _PortForwardingProtocol_Type()
)
portForwardingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portForwardingProtocol.setStatus("current")
_PortForwardingExternalPort_Type = DisplayString
_PortForwardingExternalPort_Object = MibTableColumn
portForwardingExternalPort = _PortForwardingExternalPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 17, 1, 6),
    _PortForwardingExternalPort_Type()
)
portForwardingExternalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portForwardingExternalPort.setStatus("current")
_PortForwardingInternalPort_Type = DisplayString
_PortForwardingInternalPort_Object = MibTableColumn
portForwardingInternalPort = _PortForwardingInternalPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 17, 1, 7),
    _PortForwardingInternalPort_Type()
)
portForwardingInternalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portForwardingInternalPort.setStatus("current")
_NotifyEvts_ObjectIdentity = ObjectIdentity
notifyEvts = _NotifyEvts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200)
)

# Managed Objects groups


# Notification objects

notifyPasswdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 1)
)
if mibBuilder.loadTexts:
    notifyPasswdChanged.setStatus(
        "current"
    )

notifyNetworketh0Changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 2)
)
if mibBuilder.loadTexts:
    notifyNetworketh0Changed.setStatus(
        "current"
    )

notifyNetworketh1Changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 3)
)
if mibBuilder.loadTexts:
    notifyNetworketh1Changed.setStatus(
        "current"
    )

notifyTemperatureExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 4)
)
if mibBuilder.loadTexts:
    notifyTemperatureExceeded.setStatus(
        "current"
    )

notifyPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 5)
)
if mibBuilder.loadTexts:
    notifyPowerFailure.setStatus(
        "current"
    )

notifyFirmwareUpgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 6)
)
if mibBuilder.loadTexts:
    notifyFirmwareUpgraded.setStatus(
        "current"
    )

notifyDiskLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 7)
)
if mibBuilder.loadTexts:
    notifyDiskLost.setStatus(
        "current"
    )

notifyDiskInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 8)
)
if mibBuilder.loadTexts:
    notifyDiskInsertion.setStatus(
        "current"
    )

notifyRaidFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 9)
)
if mibBuilder.loadTexts:
    notifyRaidFailed.setStatus(
        "current"
    )

notifyVolumeCreateSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 10)
)
if mibBuilder.loadTexts:
    notifyVolumeCreateSuccess.setStatus(
        "current"
    )

notifyVolumeCreateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 11)
)
if mibBuilder.loadTexts:
    notifyVolumeCreateFailed.setStatus(
        "current"
    )

notifyVolumeRemoveSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 12)
)
if mibBuilder.loadTexts:
    notifyVolumeRemoveSuccess.setStatus(
        "current"
    )

notifyVolumeRemoveFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 13)
)
if mibBuilder.loadTexts:
    notifyVolumeRemoveFailed.setStatus(
        "current"
    )

notifyVolumeStatusCrashed = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 14)
)
if mibBuilder.loadTexts:
    notifyVolumeStatusCrashed.setStatus(
        "current"
    )

notifyVolumeStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 15)
)
if mibBuilder.loadTexts:
    notifyVolumeStatusDegraded.setStatus(
        "current"
    )

notifyVolumeStatusREBUILD = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 16)
)
if mibBuilder.loadTexts:
    notifyVolumeStatusREBUILD.setStatus(
        "current"
    )

notifyVolumeStatusREBUILT = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 17)
)
if mibBuilder.loadTexts:
    notifyVolumeStatusREBUILT.setStatus(
        "current"
    )

notifyHDFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 18)
)
if mibBuilder.loadTexts:
    notifyHDFull.setStatus(
        "current"
    )

notifyVolumeSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 19)
)
if mibBuilder.loadTexts:
    notifyVolumeSpace.setStatus(
        "current"
    )

notifySeleftest = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 50, 1, 1, 1, 1, 200, 20)
)
if mibBuilder.loadTexts:
    notifySeleftest.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNS120005-MIB",
    **{"d-link": d_link,
       "productID": productID,
       "projectID": projectID,
       "modelID": modelID,
       "submodelID": submodelID,
       "nasAgent1200": nasAgent1200,
       "nasAgentVer": nasAgentVer,
       "sysTable": sysTable,
       "sysEntry": sysEntry,
       "sysNum": sysNum,
       "sysName": sysName,
       "sysFWVer": sysFWVer,
       "sysNetType": sysNetType,
       "sysFanSpeed": sysFanSpeed,
       "sysTemperature": sysTemperature,
       "sysPrinterName": sysPrinterName,
       "sysCIFS": sysCIFS,
       "sysFtpServer": sysFtpServer,
       "sysNFSServer": sysNFSServer,
       "sysDFSServer": sysDFSServer,
       "sysQuota": sysQuota,
       "sysAFP": sysAFP,
       "sysWebDAV": sysWebDAV,
       "sysWebFileServer": sysWebFileServer,
       "sysiSCSITarget": sysiSCSITarget,
       "sysiSNS": sysiSNS,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskNum": diskNum,
       "diskName": diskName,
       "diskModel": diskModel,
       "diskTemperature": diskTemperature,
       "diskCapacity": diskCapacity,
       "diskStatus": diskStatus,
       "volumeTable": volumeTable,
       "volumeEntry": volumeEntry,
       "volumeNum": volumeNum,
       "volumeName": volumeName,
       "volumeEncryption": volumeEncryption,
       "volumeFsType": volumeFsType,
       "volumeRaidLevel": volumeRaidLevel,
       "volumeSize": volumeSize,
       "volumeFreeSpace": volumeFreeSpace,
       "volumeState": volumeState,
       "snapShotTable": snapShotTable,
       "snapShotEntry": snapShotEntry,
       "snapShotNum": snapShotNum,
       "snapShotVolume": snapShotVolume,
       "snapShotName": snapShotName,
       "snapShotSchedule": snapShotSchedule,
       "snapShotCount": snapShotCount,
       "snapShotState": snapShotState,
       "snapShotPath": snapShotPath,
       "dFSTable": dFSTable,
       "dFSEntry": dFSEntry,
       "dFSNum": dFSNum,
       "dFSLShareName": dFSLShareName,
       "dFSHost": dFSHost,
       "dFSRSharefolder": dFSRSharefolder,
       "nFSTable": nFSTable,
       "nFSEntry": nFSEntry,
       "nFSNum": nFSNum,
       "nFSMountPath": nFSMountPath,
       "nFSHost": nFSHost,
       "nFSPermission": nFSPermission,
       "nFSRootSquash": nFSRootSquash,
       "nFSStatus": nFSStatus,
       "iSOTable": iSOTable,
       "iSOEntry": iSOEntry,
       "iSONum": iSONum,
       "iSOShareName": iSOShareName,
       "iSOPath": iSOPath,
       "iSOStatus": iSOStatus,
       "logServerTable": logServerTable,
       "logServerEntry": logServerEntry,
       "logServerNum": logServerNum,
       "logServerRuleName": logServerRuleName,
       "logServerLogfiles": logServerLogfiles,
       "logServerStatus": logServerStatus,
       "uPSTable": uPSTable,
       "uPSEntry": uPSEntry,
       "uPSNum": uPSNum,
       "uPSDeviceInfo": uPSDeviceInfo,
       "uPSProduct": uPSProduct,
       "uPSManufacturer": uPSManufacturer,
       "uPSBattery": uPSBattery,
       "uPSState": uPSState,
       "uPSServerIP": uPSServerIP,
       "uPSAllowedIP": uPSAllowedIP,
       "vVTable": vVTable,
       "vVEntry": vVEntry,
       "vVNum": vVNum,
       "vVTargetName": vVTargetName,
       "vVSharefolder": vVSharefolder,
       "vVStatus": vVStatus,
       "vVSize": vVSize,
       "iSCSITargetTable": iSCSITargetTable,
       "iSCSITargetEntry": iSCSITargetEntry,
       "iSCSITargetNum": iSCSITargetNum,
       "iSCSITargetIQN": iSCSITargetIQN,
       "iSCSITargetStatus": iSCSITargetStatus,
       "iSCSILUNTable": iSCSILUNTable,
       "iSCSILUNEntry": iSCSILUNEntry,
       "iSCSILUNNum": iSCSILUNNum,
       "iSCSILUNName": iSCSILUNName,
       "iSCSILUNVolume": iSCSILUNVolume,
       "iSCSILUNSize": iSCSILUNSize,
       "iSCSILUNStatus": iSCSILUNStatus,
       "iSCSILUNMapping": iSCSILUNMapping,
       "iSCSIACLTable": iSCSIACLTable,
       "iSCSIACLEntry": iSCSIACLEntry,
       "iSCSIACLNum": iSCSIACLNum,
       "iSCSIACLName": iSCSIACLName,
       "iSCSIACLInitiator": iSCSIACLInitiator,
       "aMAZONS3Table": aMAZONS3Table,
       "aMAZONS3Entry": aMAZONS3Entry,
       "aMAZONS3Num": aMAZONS3Num,
       "aMAZONS3Task": aMAZONS3Task,
       "aMAZONS3Schedule": aMAZONS3Schedule,
       "aMAZONS3Status": aMAZONS3Status,
       "aMAZONS3Enable": aMAZONS3Enable,
       "aMAZONS3BackupNow": aMAZONS3BackupNow,
       "aMAZONS3Restore": aMAZONS3Restore,
       "connectionTable": connectionTable,
       "connectionEntry": connectionEntry,
       "connectionNum": connectionNum,
       "connectionDateTime": connectionDateTime,
       "connectionServiceType": connectionServiceType,
       "connectionIPAddress": connectionIPAddress,
       "connectionUser": connectionUser,
       "connectionComputerName": connectionComputerName,
       "connectionUsedResources": connectionUsedResources,
       "portForwardingTable": portForwardingTable,
       "portForwardingEntry": portForwardingEntry,
       "portForwardingNum": portForwardingNum,
       "portForwardingEnable": portForwardingEnable,
       "portForwardingStatus": portForwardingStatus,
       "portForwardingService": portForwardingService,
       "portForwardingProtocol": portForwardingProtocol,
       "portForwardingExternalPort": portForwardingExternalPort,
       "portForwardingInternalPort": portForwardingInternalPort,
       "notifyEvts": notifyEvts,
       "notifyPasswdChanged": notifyPasswdChanged,
       "notifyNetworketh0Changed": notifyNetworketh0Changed,
       "notifyNetworketh1Changed": notifyNetworketh1Changed,
       "notifyTemperatureExceeded": notifyTemperatureExceeded,
       "notifyPowerFailure": notifyPowerFailure,
       "notifyFirmwareUpgraded": notifyFirmwareUpgraded,
       "notifyDiskLost": notifyDiskLost,
       "notifyDiskInsertion": notifyDiskInsertion,
       "notifyRaidFailed": notifyRaidFailed,
       "notifyVolumeCreateSuccess": notifyVolumeCreateSuccess,
       "notifyVolumeCreateFailed": notifyVolumeCreateFailed,
       "notifyVolumeRemoveSuccess": notifyVolumeRemoveSuccess,
       "notifyVolumeRemoveFailed": notifyVolumeRemoveFailed,
       "notifyVolumeStatusCrashed": notifyVolumeStatusCrashed,
       "notifyVolumeStatusDegraded": notifyVolumeStatusDegraded,
       "notifyVolumeStatusREBUILD": notifyVolumeStatusREBUILD,
       "notifyVolumeStatusREBUILT": notifyVolumeStatusREBUILT,
       "notifyHDFull": notifyHDFull,
       "notifyVolumeSpace": notifyVolumeSpace,
       "notifySeleftest": notifySeleftest}
)
