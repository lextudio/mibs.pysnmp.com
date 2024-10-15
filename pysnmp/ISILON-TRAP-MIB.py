# SNMP MIB module (ISILON-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISILON-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:47 2024
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

(isilon,) = mibBuilder.importSymbols(
    "ISILON-MIB",
    "isilon")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

isilonTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250)
)
isilonTraps.setRevisions(
        ("2015-04-08 00:00",
         "2013-06-21 00:00",
         "2013-03-21 00:00",
         "2012-09-21 00:00",
         "2012-08-01 00:00",
         "2012-05-23 00:00",
         "2012-04-30 00:00",
         "2011-09-29 00:00",
         "2009-11-12 00:00",
         "2009-11-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GroupStateTraps_ObjectIdentity = ObjectIdentity
groupStateTraps = _GroupStateTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10)
)
_NodeStatus_ObjectIdentity = ObjectIdentity
nodeStatus = _NodeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10, 1)
)
_NodeExpStatus_ObjectIdentity = ObjectIdentity
nodeExpStatus = _NodeExpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10, 2)
)
_NodeShutdown_ObjectIdentity = ObjectIdentity
nodeShutdown = _NodeShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10, 3)
)
_NodeShutdownFail_ObjectIdentity = ObjectIdentity
nodeShutdownFail = _NodeShutdownFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10, 4)
)
_NodeRebootCoalesced_ObjectIdentity = ObjectIdentity
nodeRebootCoalesced = _NodeRebootCoalesced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10, 20)
)
_NodeStatusCoalescing_ObjectIdentity = ObjectIdentity
nodeStatusCoalescing = _NodeStatusCoalescing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10, 21)
)
_FilesystemTraps_ObjectIdentity = ObjectIdentity
filesystemTraps = _FilesystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11)
)
_PartitionUsage_ObjectIdentity = ObjectIdentity
partitionUsage = _PartitionUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 1)
)
_ClusterStorageUsage_ObjectIdentity = ObjectIdentity
clusterStorageUsage = _ClusterStorageUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 2)
)
_FilesysError_ObjectIdentity = ObjectIdentity
filesysError = _FilesysError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 3)
)
_DiskPoolUsage_ObjectIdentity = ObjectIdentity
diskPoolUsage = _DiskPoolUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 4)
)
_DiskPoolOldDbVersion_ObjectIdentity = ObjectIdentity
diskPoolOldDbVersion = _DiskPoolOldDbVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 5)
)
_SsdUsage_ObjectIdentity = ObjectIdentity
ssdUsage = _SsdUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 6)
)
_FilesysCoalesce_ObjectIdentity = ObjectIdentity
filesysCoalesce = _FilesysCoalesce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 20)
)
_SmartQuotaTraps_ObjectIdentity = ObjectIdentity
smartQuotaTraps = _SmartQuotaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 12)
)
_QuotaThreshError_ObjectIdentity = ObjectIdentity
quotaThreshError = _QuotaThreshError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 12, 1)
)
_QuotaNotifyError_ObjectIdentity = ObjectIdentity
quotaNotifyError = _QuotaNotifyError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 12, 2)
)
_QuotaError_ObjectIdentity = ObjectIdentity
quotaError = _QuotaError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 12, 3)
)
_SnapshotTraps_ObjectIdentity = ObjectIdentity
snapshotTraps = _SnapshotTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 13)
)
_SnapshotError_ObjectIdentity = ObjectIdentity
snapshotError = _SnapshotError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 13, 1)
)
_SnapshotReserve_ObjectIdentity = ObjectIdentity
snapshotReserve = _SnapshotReserve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 13, 2)
)
_SyncIQTraps_ObjectIdentity = ObjectIdentity
syncIQTraps = _SyncIQTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 14)
)
_SiqEvent_ObjectIdentity = ObjectIdentity
siqEvent = _SiqEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 14, 1)
)
_SiqError_ObjectIdentity = ObjectIdentity
siqError = _SiqError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 14, 2)
)
_SiqPolicyCoalesced_ObjectIdentity = ObjectIdentity
siqPolicyCoalesced = _SiqPolicyCoalesced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 14, 20)
)
_SiqTargetCoalesced_ObjectIdentity = ObjectIdentity
siqTargetCoalesced = _SiqTargetCoalesced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 14, 21)
)
_SoftwareTraps_ObjectIdentity = ObjectIdentity
softwareTraps = _SoftwareTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15)
)
_JobEngineError_ObjectIdentity = ObjectIdentity
jobEngineError = _JobEngineError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 1)
)
_FlexProtectRunning_ObjectIdentity = ObjectIdentity
flexProtectRunning = _FlexProtectRunning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 2)
)
_AvscanInfectedFile_ObjectIdentity = ObjectIdentity
avscanInfectedFile = _AvscanInfectedFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 3)
)
_McpProcFailed_ObjectIdentity = ObjectIdentity
mcpProcFailed = _McpProcFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 5)
)
_McpProcKilled_ObjectIdentity = ObjectIdentity
mcpProcKilled = _McpProcKilled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 6)
)
_LicenseExpiration_ObjectIdentity = ObjectIdentity
licenseExpiration = _LicenseExpiration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 7)
)
_FirmwareUpdateIncomplete_ObjectIdentity = ObjectIdentity
firmwareUpdateIncomplete = _FirmwareUpdateIncomplete_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 8)
)
_TestEvent_ObjectIdentity = ObjectIdentity
testEvent = _TestEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 9)
)
_NodeCPU_ObjectIdentity = ObjectIdentity
nodeCPU = _NodeCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 10)
)
_MountdClientMountFailed_ObjectIdentity = ObjectIdentity
mountdClientMountFailed = _MountdClientMountFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 11)
)
_MountdHostLookupFailed_ObjectIdentity = ObjectIdentity
mountdHostLookupFailed = _MountdHostLookupFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 12)
)
_MixedSedNonSedCluster_ObjectIdentity = ObjectIdentity
mixedSedNonSedCluster = _MixedSedNonSedCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 13)
)
_NfsCookieTranslationFailed_ObjectIdentity = ObjectIdentity
nfsCookieTranslationFailed = _NfsCookieTranslationFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 15)
)
_AvscanTraps_ObjectIdentity = ObjectIdentity
avscanTraps = _AvscanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 16)
)
_AvscanNoServersConf_ObjectIdentity = ObjectIdentity
avscanNoServersConf = _AvscanNoServersConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 16, 1)
)
_AvscanError_ObjectIdentity = ObjectIdentity
avscanError = _AvscanError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 16, 2)
)
_AvscanCoalesced_ObjectIdentity = ObjectIdentity
avscanCoalesced = _AvscanCoalesced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 16, 20)
)
_NetProtoTraps_ObjectIdentity = ObjectIdentity
netProtoTraps = _NetProtoTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17)
)
_ClockSkew_ObjectIdentity = ObjectIdentity
clockSkew = _ClockSkew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 1)
)
_SharePermsUpgradeFail_ObjectIdentity = ObjectIdentity
sharePermsUpgradeFail = _SharePermsUpgradeFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 2)
)
_WinTimeConnectivityLost_ObjectIdentity = ObjectIdentity
winTimeConnectivityLost = _WinTimeConnectivityLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 3)
)
_WinNetMapFull_ObjectIdentity = ObjectIdentity
winNetMapFull = _WinNetMapFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 4)
)
_WinNetAuth_ObjectIdentity = ObjectIdentity
winNetAuth = _WinNetAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 5)
)
_LwioParam_ObjectIdentity = ObjectIdentity
lwioParam = _LwioParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 6)
)
_WinSmbUpgrade_ObjectIdentity = ObjectIdentity
winSmbUpgrade = _WinSmbUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 7)
)
_WinNetworkCoalesce_ObjectIdentity = ObjectIdentity
winNetworkCoalesce = _WinNetworkCoalesce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 20)
)
_WinIDmapCoalesce_ObjectIdentity = ObjectIdentity
winIDmapCoalesce = _WinIDmapCoalesce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 21)
)
_WinAuthCoalesce_ObjectIdentity = ObjectIdentity
winAuthCoalesce = _WinAuthCoalesce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 22)
)
_WinAuthUpgrade_ObjectIdentity = ObjectIdentity
winAuthUpgrade = _WinAuthUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 23)
)
_NetworkingTraps_ObjectIdentity = ObjectIdentity
networkingTraps = _NetworkingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 18)
)
_NetStatus_ObjectIdentity = ObjectIdentity
netStatus = _NetStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 18, 1)
)
_NetStatusCoalescing_ObjectIdentity = ObjectIdentity
netStatusCoalescing = _NetStatusCoalescing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 18, 20)
)
_HardwareTraps_ObjectIdentity = ObjectIdentity
hardwareTraps = _HardwareTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19)
)
_HardwareError_ObjectIdentity = ObjectIdentity
hardwareError = _HardwareError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 1)
)
_HardwareErrorMsg_ObjectIdentity = ObjectIdentity
hardwareErrorMsg = _HardwareErrorMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 1, 1)
)
_HwError_ObjectIdentity = ObjectIdentity
hwError = _HwError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 2)
)
_DiskNodeOffline_ObjectIdentity = ObjectIdentity
diskNodeOffline = _DiskNodeOffline_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 10)
)
_HardwareCoalesced_ObjectIdentity = ObjectIdentity
hardwareCoalesced = _HardwareCoalesced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 20)
)
_SensorCoalesced_ObjectIdentity = ObjectIdentity
sensorCoalesced = _SensorCoalesced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 50)
)
_FanCoalesced_ObjectIdentity = ObjectIdentity
fanCoalesced = _FanCoalesced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 51)
)
_TempCoalesced_ObjectIdentity = ObjectIdentity
tempCoalesced = _TempCoalesced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 52)
)
_VoltsCoalesced_ObjectIdentity = ObjectIdentity
voltsCoalesced = _VoltsCoalesced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 53)
)
_SystemDiskTraps_ObjectIdentity = ObjectIdentity
systemDiskTraps = _SystemDiskTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20)
)
_DriveStatus_ObjectIdentity = ObjectIdentity
driveStatus = _DriveStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20, 1)
)
_BootDiskFail_ObjectIdentity = ObjectIdentity
bootDiskFail = _BootDiskFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20, 2)
)
_DiskError_ObjectIdentity = ObjectIdentity
diskError = _DiskError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20, 3)
)
_BootDiskMirrorReqMissing_ObjectIdentity = ObjectIdentity
bootDiskMirrorReqMissing = _BootDiskMirrorReqMissing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20, 4)
)
_DiskErrorCoalesced_ObjectIdentity = ObjectIdentity
diskErrorCoalesced = _DiskErrorCoalesced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20, 20)
)
_SensorTraps_ObjectIdentity = ObjectIdentity
sensorTraps = _SensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21)
)
_HwPwrSupply_ObjectIdentity = ObjectIdentity
hwPwrSupply = _HwPwrSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 1)
)
_HwPwrSupplyOver_ObjectIdentity = ObjectIdentity
hwPwrSupplyOver = _HwPwrSupplyOver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 1, 1)
)
_HwPwrSupplyUnder_ObjectIdentity = ObjectIdentity
hwPwrSupplyUnder = _HwPwrSupplyUnder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 1, 2)
)
_HwFan_ObjectIdentity = ObjectIdentity
hwFan = _HwFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 2)
)
_HwFanOver_ObjectIdentity = ObjectIdentity
hwFanOver = _HwFanOver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 2, 1)
)
_HwFanUnder_ObjectIdentity = ObjectIdentity
hwFanUnder = _HwFanUnder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 2, 2)
)
_HwVoltage_ObjectIdentity = ObjectIdentity
hwVoltage = _HwVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 10)
)
_HwVoltageOver_ObjectIdentity = ObjectIdentity
hwVoltageOver = _HwVoltageOver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 10, 1)
)
_HwVoltageUnder_ObjectIdentity = ObjectIdentity
hwVoltageUnder = _HwVoltageUnder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 10, 2)
)
_HwTemp_ObjectIdentity = ObjectIdentity
hwTemp = _HwTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 11)
)
_HwTempOver_ObjectIdentity = ObjectIdentity
hwTempOver = _HwTempOver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 11, 1)
)
_HwTempUnder_ObjectIdentity = ObjectIdentity
hwTempUnder = _HwTempUnder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 11, 2)
)
_HwPower_ObjectIdentity = ObjectIdentity
hwPower = _HwPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 12)
)
_HwMem_ObjectIdentity = ObjectIdentity
hwMem = _HwMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 13)
)
_HwCpuThrottle_ObjectIdentity = ObjectIdentity
hwCpuThrottle = _HwCpuThrottle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 14)
)
_SensorMonitor_ObjectIdentity = ObjectIdentity
sensorMonitor = _SensorMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 15)
)
_HwCurrent_ObjectIdentity = ObjectIdentity
hwCurrent = _HwCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 16)
)
_HwCurrentOver_ObjectIdentity = ObjectIdentity
hwCurrentOver = _HwCurrentOver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 16, 1)
)
_HwCurrentUnder_ObjectIdentity = ObjectIdentity
hwCurrentUnder = _HwCurrentUnder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 16, 2)
)
_StorageTransportTraps_ObjectIdentity = ObjectIdentity
storageTransportTraps = _StorageTransportTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 22)
)
_SasPhyError_ObjectIdentity = ObjectIdentity
sasPhyError = _SasPhyError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 22, 1)
)
_StorageTransportCoalesced_ObjectIdentity = ObjectIdentity
storageTransportCoalesced = _StorageTransportCoalesced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 22, 2)
)
_CloudPoolsTraps_ObjectIdentity = ObjectIdentity
cloudPoolsTraps = _CloudPoolsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23)
)
_CloudpoolNetworkError_ObjectIdentity = ObjectIdentity
cloudpoolNetworkError = _CloudpoolNetworkError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 1)
)
_CloudpoolAuthenticationError_ObjectIdentity = ObjectIdentity
cloudpoolAuthenticationError = _CloudpoolAuthenticationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 2)
)
_CloudpoolAuthorizationError_ObjectIdentity = ObjectIdentity
cloudpoolAuthorizationError = _CloudpoolAuthorizationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 3)
)
_CloudpoolBucketNotFoundError_ObjectIdentity = ObjectIdentity
cloudpoolBucketNotFoundError = _CloudpoolBucketNotFoundError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 4)
)
_CloudpoolObjectNotFoundError_ObjectIdentity = ObjectIdentity
cloudpoolObjectNotFoundError = _CloudpoolObjectNotFoundError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 5)
)
_CloudpoolDataCorruptionIntegrityError_ObjectIdentity = ObjectIdentity
cloudpoolDataCorruptionIntegrityError = _CloudpoolDataCorruptionIntegrityError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 6)
)
_CloudpoolNoUsableAccountFoundError_ObjectIdentity = ObjectIdentity
cloudpoolNoUsableAccountFoundError = _CloudpoolNoUsableAccountFoundError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 7)
)
_CloudpoolCertificateError_ObjectIdentity = ObjectIdentity
cloudpoolCertificateError = _CloudpoolCertificateError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 8)
)
_UpgradeTraps_ObjectIdentity = ObjectIdentity
upgradeTraps = _UpgradeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24)
)
_UpgradeStart_ObjectIdentity = ObjectIdentity
upgradeStart = _UpgradeStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24, 1)
)
_UpgradeFinish_ObjectIdentity = ObjectIdentity
upgradeFinish = _UpgradeFinish_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24, 2)
)
_UpgradeClusterEvent_ObjectIdentity = ObjectIdentity
upgradeClusterEvent = _UpgradeClusterEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24, 3)
)
_UpgradeNodeEvent_ObjectIdentity = ObjectIdentity
upgradeNodeEvent = _UpgradeNodeEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24, 4)
)
_UpgradeRollbackStart_ObjectIdentity = ObjectIdentity
upgradeRollbackStart = _UpgradeRollbackStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24, 5)
)
_Variables_ObjectIdentity = ObjectIdentity
variables = _Variables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50)
)
_NodeIdentifier_Type = Integer32
_NodeIdentifier_Object = MibScalar
nodeIdentifier = _NodeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 1),
    _NodeIdentifier_Type()
)
nodeIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nodeIdentifier.setStatus("current")
_MeasuredValue_Type = Integer32
_MeasuredValue_Object = MibScalar
measuredValue = _MeasuredValue_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 2),
    _MeasuredValue_Type()
)
measuredValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    measuredValue.setStatus("current")
_Units_Type = OctetString
_Units_Object = MibScalar
units = _Units_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 3),
    _Units_Type()
)
units.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    units.setStatus("current")
_Oid_Type = ObjectIdentifier
_Oid_Object = MibScalar
oid = _Oid_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 4),
    _Oid_Type()
)
oid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    oid.setStatus("current")
_Bay_Type = Integer32
_Bay_Object = MibScalar
bay = _Bay_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 5),
    _Bay_Type()
)
bay.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bay.setStatus("current")
_IfName_Type = OctetString
_IfName_Object = MibScalar
ifName = _IfName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 6),
    _IfName_Type()
)
ifName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ifName.setStatus("current")
_Phy_Type = Integer32
_Phy_Object = MibScalar
phy = _Phy_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 7),
    _Phy_Type()
)
phy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    phy.setStatus("current")
_ErrorMessage_Type = OctetString
_ErrorMessage_Object = MibScalar
errorMessage = _ErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 8),
    _ErrorMessage_Type()
)
errorMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    errorMessage.setStatus("current")
_Errno_Type = Integer32
_Errno_Object = MibScalar
errno = _Errno_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 9),
    _Errno_Type()
)
errno.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    errno.setStatus("current")
_StringArg_Type = OctetString
_StringArg_Object = MibScalar
stringArg = _StringArg_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 10),
    _StringArg_Type()
)
stringArg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    stringArg.setStatus("current")
_Message_Type = OctetString
_Message_Object = MibScalar
message = _Message_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 11),
    _Message_Type()
)
message.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    message.setStatus("current")
_I64Arg_Type = Counter64
_I64Arg_Object = MibScalar
i64Arg = _I64Arg_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 12),
    _I64Arg_Type()
)
i64Arg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    i64Arg.setStatus("current")
_I32Arg_Type = Integer32
_I32Arg_Object = MibScalar
i32Arg = _I32Arg_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 13),
    _I32Arg_Type()
)
i32Arg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    i32Arg.setStatus("current")
_MeasuredValueStr_Type = OctetString
_MeasuredValueStr_Object = MibScalar
measuredValueStr = _MeasuredValueStr_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 14),
    _MeasuredValueStr_Type()
)
measuredValueStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    measuredValueStr.setStatus("current")
_InstanceIdentifier_Type = OctetString
_InstanceIdentifier_Object = MibScalar
instanceIdentifier = _InstanceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 15),
    _InstanceIdentifier_Type()
)
instanceIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    instanceIdentifier.setStatus("current")
_DeviceIdentifier_Type = Integer32
_DeviceIdentifier_Object = MibScalar
deviceIdentifier = _DeviceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 12124, 250, 50, 16),
    _DeviceIdentifier_Type()
)
deviceIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    deviceIdentifier.setStatus("current")
_TrapConformance_ObjectIdentity = ObjectIdentity
trapConformance = _TrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51)
)
_TrapCompliance_ObjectIdentity = ObjectIdentity
trapCompliance = _TrapCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 250, 52)
)

# Managed Objects groups

variablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 50)
)
variablesGroup.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "measuredValue"),
        ("ISILON-TRAP-MIB", "units"),
        ("ISILON-TRAP-MIB", "oid"),
        ("ISILON-TRAP-MIB", "bay"),
        ("ISILON-TRAP-MIB", "ifName"),
        ("ISILON-TRAP-MIB", "phy"),
        ("ISILON-TRAP-MIB", "errorMessage"),
        ("ISILON-TRAP-MIB", "errno"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "message"),
        ("ISILON-TRAP-MIB", "i64Arg"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"),
        ("ISILON-TRAP-MIB", "deviceIdentifier"))
)
if mibBuilder.loadTexts:
    variablesGroup.setStatus("current")


# Notification objects

nodeStatusCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10, 1, 3)
)
nodeStatusCrit.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    nodeStatusCrit.setStatus(
        "current"
    )

nodeStatusInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10, 1, 7)
)
nodeStatusInfo.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    nodeStatusInfo.setStatus(
        "current"
    )

nodeExpStatusCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10, 2, 3)
)
nodeExpStatusCrit.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    nodeExpStatusCrit.setStatus(
        "current"
    )

nodeShutdownInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10, 3, 7)
)
nodeShutdownInfo.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    nodeShutdownInfo.setStatus(
        "current"
    )

nodeShutdownFailCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10, 4, 3)
)
nodeShutdownFailCrit.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    nodeShutdownFailCrit.setStatus(
        "current"
    )

nodeRebootCoalescedInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10, 20, 7)
)
nodeRebootCoalescedInfo.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    nodeRebootCoalescedInfo.setStatus(
        "current"
    )

nodeStatusCoalescingCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10, 21, 3)
)
nodeStatusCoalescingCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    nodeStatusCoalescingCrit.setStatus(
        "current"
    )

nodeStatusCoalescingWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 10, 21, 5)
)
nodeStatusCoalescingWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    nodeStatusCoalescingWarn.setStatus(
        "current"
    )

partitionUsageCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 1, 3)
)
partitionUsageCrit.setObjects(
      *(("ISILON-TRAP-MIB", "units"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    partitionUsageCrit.setStatus(
        "current"
    )

partitionUsageWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 1, 5)
)
partitionUsageWarn.setObjects(
      *(("ISILON-TRAP-MIB", "units"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    partitionUsageWarn.setStatus(
        "current"
    )

partitionUsageInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 1, 7)
)
partitionUsageInfo.setObjects(
      *(("ISILON-TRAP-MIB", "units"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    partitionUsageInfo.setStatus(
        "current"
    )

clusterStorageUsageCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 2, 3)
)
clusterStorageUsageCrit.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    clusterStorageUsageCrit.setStatus(
        "current"
    )

clusterStorageUsageWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 2, 5)
)
clusterStorageUsageWarn.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    clusterStorageUsageWarn.setStatus(
        "current"
    )

filesysErrorCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 3, 3)
)
filesysErrorCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    filesysErrorCrit.setStatus(
        "current"
    )

filesysErrorWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 3, 5)
)
filesysErrorWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    filesysErrorWarn.setStatus(
        "current"
    )

filesysErrorInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 3, 7)
)
filesysErrorInfo.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    filesysErrorInfo.setStatus(
        "current"
    )

diskPoolUsageCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 4, 3)
)
diskPoolUsageCrit.setObjects(
      *(("ISILON-TRAP-MIB", "units"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    diskPoolUsageCrit.setStatus(
        "current"
    )

diskPoolUsageWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 4, 5)
)
diskPoolUsageWarn.setObjects(
      *(("ISILON-TRAP-MIB", "units"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    diskPoolUsageWarn.setStatus(
        "current"
    )

diskPoolOldDbVersionWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 5, 5)
)
diskPoolOldDbVersionWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    diskPoolOldDbVersionWarn.setStatus(
        "current"
    )

ssdUsageCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 6, 1)
)
ssdUsageCrit.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "units"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    ssdUsageCrit.setStatus(
        "current"
    )

ssdUsageWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 6, 2)
)
ssdUsageWarn.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "units"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    ssdUsageWarn.setStatus(
        "current"
    )

ssdUsageInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 6, 3)
)
ssdUsageInfo.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "units"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    ssdUsageInfo.setStatus(
        "current"
    )

filesysCoalesceCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 20, 3)
)
filesysCoalesceCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    filesysCoalesceCrit.setStatus(
        "current"
    )

filesysCoalesceWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 11, 20, 5)
)
filesysCoalesceWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    filesysCoalesceWarn.setStatus(
        "current"
    )

quotaThreshErrorInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 12, 1, 7)
)
quotaThreshErrorInfo.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    quotaThreshErrorInfo.setStatus(
        "current"
    )

quotaNotifyErrorWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 12, 2, 5)
)
quotaNotifyErrorWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    quotaNotifyErrorWarn.setStatus(
        "current"
    )

quotaErrorWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 12, 3, 5)
)
quotaErrorWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    quotaErrorWarn.setStatus(
        "current"
    )

snapshotErrorWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 13, 1, 5)
)
snapshotErrorWarn.setObjects(
      *(("ISILON-TRAP-MIB", "errno"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    snapshotErrorWarn.setStatus(
        "current"
    )

snapshotReserveCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 13, 2, 3)
)
snapshotReserveCrit.setObjects(
      *(("ISILON-TRAP-MIB", "units"),
        ("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    snapshotReserveCrit.setStatus(
        "current"
    )

snapshotReserveWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 13, 2, 5)
)
snapshotReserveWarn.setObjects(
      *(("ISILON-TRAP-MIB", "units"),
        ("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    snapshotReserveWarn.setStatus(
        "current"
    )

siqEventCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 14, 1, 3)
)
siqEventCrit.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    siqEventCrit.setStatus(
        "current"
    )

siqEventWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 14, 1, 5)
)
siqEventWarn.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    siqEventWarn.setStatus(
        "current"
    )

siqErrorWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 14, 2, 5)
)
siqErrorWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    siqErrorWarn.setStatus(
        "current"
    )

siqPolicyCoalescedCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 14, 20, 3)
)
siqPolicyCoalescedCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    siqPolicyCoalescedCrit.setStatus(
        "current"
    )

siqPolicyCoalescedWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 14, 20, 5)
)
siqPolicyCoalescedWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    siqPolicyCoalescedWarn.setStatus(
        "current"
    )

siqTargetCoalescedCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 14, 21, 3)
)
siqTargetCoalescedCrit.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    siqTargetCoalescedCrit.setStatus(
        "current"
    )

siqTargetCoalescedWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 14, 21, 5)
)
siqTargetCoalescedWarn.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    siqTargetCoalescedWarn.setStatus(
        "current"
    )

jobEngineErrorEmerg = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 1, 1)
)
jobEngineErrorEmerg.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    jobEngineErrorEmerg.setStatus(
        "current"
    )

jobEngineErrorCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 1, 3)
)
jobEngineErrorCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    jobEngineErrorCrit.setStatus(
        "current"
    )

jobEngineErrorWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 1, 5)
)
jobEngineErrorWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    jobEngineErrorWarn.setStatus(
        "current"
    )

jobEngineErrorInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 1, 7)
)
jobEngineErrorInfo.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    jobEngineErrorInfo.setStatus(
        "current"
    )

flexProtectRunningCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 2, 3)
)
flexProtectRunningCrit.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    flexProtectRunningCrit.setStatus(
        "current"
    )

flexProtectRunningWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 2, 5)
)
flexProtectRunningWarn.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    flexProtectRunningWarn.setStatus(
        "current"
    )

flexProtectRunningInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 2, 7)
)
flexProtectRunningInfo.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    flexProtectRunningInfo.setStatus(
        "current"
    )

avscanInfectedFileCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 3, 3)
)
avscanInfectedFileCrit.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    avscanInfectedFileCrit.setStatus(
        "current"
    )

avscanInfectedFileWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 3, 5)
)
avscanInfectedFileWarn.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    avscanInfectedFileWarn.setStatus(
        "current"
    )

avscanInfectedFileInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 3, 7)
)
avscanInfectedFileInfo.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    avscanInfectedFileInfo.setStatus(
        "current"
    )

mcpProcFailedWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 5, 5)
)
mcpProcFailedWarn.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    mcpProcFailedWarn.setStatus(
        "current"
    )

mcpProcKilledWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 6, 5)
)
mcpProcKilledWarn.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    mcpProcKilledWarn.setStatus(
        "current"
    )

licenseExpirationWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 7, 5)
)
licenseExpirationWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    licenseExpirationWarn.setStatus(
        "current"
    )

licenseExpirationInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 7, 7)
)
licenseExpirationInfo.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    licenseExpirationInfo.setStatus(
        "current"
    )

firmwareUpdateIncompleteWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 8, 5)
)
firmwareUpdateIncompleteWarn.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    firmwareUpdateIncompleteWarn.setStatus(
        "current"
    )

testEventCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 9, 3)
)
testEventCrit.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    testEventCrit.setStatus(
        "current"
    )

nodeCPUWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 10, 5)
)
nodeCPUWarn.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    nodeCPUWarn.setStatus(
        "current"
    )

nodeCPUInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 10, 7)
)
nodeCPUInfo.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    nodeCPUInfo.setStatus(
        "current"
    )

mountdClientMountFailedInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 11, 7)
)
mountdClientMountFailedInfo.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    mountdClientMountFailedInfo.setStatus(
        "current"
    )

mountdHostLookupFailedInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 12, 7)
)
mountdHostLookupFailedInfo.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    mountdHostLookupFailedInfo.setStatus(
        "current"
    )

mixedSedNonSedClusterCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 13, 3)
)
mixedSedNonSedClusterCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    mixedSedNonSedClusterCrit.setStatus(
        "current"
    )

nfsCookieTranslationFailedInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 15, 15, 1)
)
nfsCookieTranslationFailedInfo.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    nfsCookieTranslationFailedInfo.setStatus(
        "current"
    )

avscanNoServersConfCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 16, 1, 3)
)
avscanNoServersConfCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    avscanNoServersConfCrit.setStatus(
        "current"
    )

avscanNoServersConfWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 16, 1, 5)
)
avscanNoServersConfWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    avscanNoServersConfWarn.setStatus(
        "current"
    )

avscanNoServersConfInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 16, 1, 7)
)
avscanNoServersConfInfo.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    avscanNoServersConfInfo.setStatus(
        "current"
    )

avscanErrorCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 16, 2, 3)
)
avscanErrorCrit.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    avscanErrorCrit.setStatus(
        "current"
    )

avscanErrorWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 16, 2, 5)
)
avscanErrorWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    avscanErrorWarn.setStatus(
        "current"
    )

avscanErrorInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 16, 2, 7)
)
avscanErrorInfo.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    avscanErrorInfo.setStatus(
        "current"
    )

avscanCoalescedInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 16, 20, 3)
)
avscanCoalescedInfo.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    avscanCoalescedInfo.setStatus(
        "current"
    )

avscanCoalescedWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 16, 20, 5)
)
avscanCoalescedWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    avscanCoalescedWarn.setStatus(
        "current"
    )

avscanCoalescedCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 16, 20, 7)
)
avscanCoalescedCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    avscanCoalescedCrit.setStatus(
        "current"
    )

clockSkewCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 1, 3)
)
clockSkewCrit.setObjects(
      *(("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    clockSkewCrit.setStatus(
        "current"
    )

sharePermsUpgradeFailCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 2, 3)
)
sharePermsUpgradeFailCrit.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    sharePermsUpgradeFailCrit.setStatus(
        "current"
    )

winTimeConnectivityLostWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 3, 5)
)
winTimeConnectivityLostWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    winTimeConnectivityLostWarn.setStatus(
        "current"
    )

winNetMapFullCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 4, 3)
)
winNetMapFullCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    winNetMapFullCrit.setStatus(
        "current"
    )

winNetAuthCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 5, 3)
)
winNetAuthCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    winNetAuthCrit.setStatus(
        "current"
    )

winNetAuthWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 5, 5)
)
winNetAuthWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    winNetAuthWarn.setStatus(
        "current"
    )

lwioParamCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 6, 3)
)
lwioParamCrit.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    lwioParamCrit.setStatus(
        "current"
    )

winSmbUpgradeWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 7, 2)
)
winSmbUpgradeWarn.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    winSmbUpgradeWarn.setStatus(
        "current"
    )

winSmbUpgradeCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 7, 3)
)
winSmbUpgradeCrit.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    winSmbUpgradeCrit.setStatus(
        "current"
    )

winNetworkCoalesceCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 20, 3)
)
winNetworkCoalesceCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    winNetworkCoalesceCrit.setStatus(
        "current"
    )

winNetworkCoalesceWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 20, 5)
)
winNetworkCoalesceWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    winNetworkCoalesceWarn.setStatus(
        "current"
    )

winIDmapCoalesceCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 21, 3)
)
winIDmapCoalesceCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    winIDmapCoalesceCrit.setStatus(
        "current"
    )

winIDmapCoalesceWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 21, 5)
)
winIDmapCoalesceWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    winIDmapCoalesceWarn.setStatus(
        "current"
    )

winAuthCoalesceCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 22, 3)
)
winAuthCoalesceCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    winAuthCoalesceCrit.setStatus(
        "current"
    )

winAuthCoalesceWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 22, 5)
)
winAuthCoalesceWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    winAuthCoalesceWarn.setStatus(
        "current"
    )

winAuthUpgradeCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 17, 23, 3)
)
winAuthUpgradeCrit.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    winAuthUpgradeCrit.setStatus(
        "current"
    )

netStatusCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 18, 1, 3)
)
netStatusCrit.setObjects(
      *(("ISILON-TRAP-MIB", "ifName"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    netStatusCrit.setStatus(
        "current"
    )

netStatusWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 18, 1, 5)
)
netStatusWarn.setObjects(
      *(("ISILON-TRAP-MIB", "ifName"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    netStatusWarn.setStatus(
        "current"
    )

netStatusCoalescingCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 18, 20, 3)
)
netStatusCoalescingCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    netStatusCoalescingCrit.setStatus(
        "current"
    )

netStatusCoalescingWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 18, 20, 5)
)
netStatusCoalescingWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    netStatusCoalescingWarn.setStatus(
        "current"
    )

hardwareErrorMsgCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 1, 1, 3)
)
hardwareErrorMsgCrit.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "errorMessage"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hardwareErrorMsgCrit.setStatus(
        "current"
    )

hardwareErrorMsgWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 1, 1, 5)
)
hardwareErrorMsgWarn.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "errorMessage"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hardwareErrorMsgWarn.setStatus(
        "current"
    )

hardwareErrorCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 1, 3)
)
hardwareErrorCrit.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hardwareErrorCrit.setStatus(
        "current"
    )

hardwareErrorWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 1, 5)
)
hardwareErrorWarn.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hardwareErrorWarn.setStatus(
        "current"
    )

hardwareErrorInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 1, 7)
)
hardwareErrorInfo.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hardwareErrorInfo.setStatus(
        "current"
    )

hwErrorCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 2, 3)
)
hwErrorCrit.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwErrorCrit.setStatus(
        "current"
    )

diskNodeOfflineCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 10, 3)
)
diskNodeOfflineCrit.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    diskNodeOfflineCrit.setStatus(
        "current"
    )

hardwareCoalescedEmerg = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 20, 1)
)
hardwareCoalescedEmerg.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hardwareCoalescedEmerg.setStatus(
        "current"
    )

hardwareCoalescedCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 20, 3)
)
hardwareCoalescedCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hardwareCoalescedCrit.setStatus(
        "current"
    )

hardwareCoalescedWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 20, 5)
)
hardwareCoalescedWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hardwareCoalescedWarn.setStatus(
        "current"
    )

sensorCoalescedEmerg = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 50, 1)
)
sensorCoalescedEmerg.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    sensorCoalescedEmerg.setStatus(
        "current"
    )

sensorCoalescedCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 50, 3)
)
sensorCoalescedCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    sensorCoalescedCrit.setStatus(
        "current"
    )

sensorCoalescedWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 50, 5)
)
sensorCoalescedWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    sensorCoalescedWarn.setStatus(
        "current"
    )

fanCoalescedEmerg = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 51, 1)
)
fanCoalescedEmerg.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    fanCoalescedEmerg.setStatus(
        "current"
    )

fanCoalescedCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 51, 3)
)
fanCoalescedCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    fanCoalescedCrit.setStatus(
        "current"
    )

fanCoalescedWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 51, 5)
)
fanCoalescedWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    fanCoalescedWarn.setStatus(
        "current"
    )

tempCoalescedEmerg = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 52, 1)
)
tempCoalescedEmerg.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    tempCoalescedEmerg.setStatus(
        "current"
    )

tempCoalescedCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 52, 3)
)
tempCoalescedCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    tempCoalescedCrit.setStatus(
        "current"
    )

tempCoalescedWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 52, 5)
)
tempCoalescedWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    tempCoalescedWarn.setStatus(
        "current"
    )

voltsCoalescedEmerg = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 53, 1)
)
voltsCoalescedEmerg.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    voltsCoalescedEmerg.setStatus(
        "current"
    )

voltsCoalescedCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 53, 3)
)
voltsCoalescedCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    voltsCoalescedCrit.setStatus(
        "current"
    )

voltsCoalescedWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 19, 53, 5)
)
voltsCoalescedWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    voltsCoalescedWarn.setStatus(
        "current"
    )

driveStatusInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20, 1, 1)
)
driveStatusInfo.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "bay"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    driveStatusInfo.setStatus(
        "current"
    )

driveStatusCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20, 1, 3)
)
driveStatusCrit.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "bay"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    driveStatusCrit.setStatus(
        "current"
    )

driveStatusWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20, 1, 5)
)
driveStatusWarn.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "bay"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    driveStatusWarn.setStatus(
        "current"
    )

bootDiskFailCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20, 2, 3)
)
bootDiskFailCrit.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    bootDiskFailCrit.setStatus(
        "current"
    )

bootDiskFailWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20, 2, 5)
)
bootDiskFailWarn.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    bootDiskFailWarn.setStatus(
        "current"
    )

diskErrorWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20, 3, 3)
)
diskErrorWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    diskErrorWarn.setStatus(
        "current"
    )

bootdiskMirrorReqMissingCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20, 4, 3)
)
bootdiskMirrorReqMissingCrit.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"))
)
if mibBuilder.loadTexts:
    bootdiskMirrorReqMissingCrit.setStatus(
        "current"
    )

diskErrorCoalescedCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20, 20, 3)
)
diskErrorCoalescedCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    diskErrorCoalescedCrit.setStatus(
        "current"
    )

diskErrorCoalescedWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 20, 20, 5)
)
diskErrorCoalescedWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    diskErrorCoalescedWarn.setStatus(
        "current"
    )

hwPwrSupplyOverCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 1, 1, 3)
)
hwPwrSupplyOverCrit.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwPwrSupplyOverCrit.setStatus(
        "current"
    )

hwPwrSupplyOverWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 1, 1, 5)
)
hwPwrSupplyOverWarn.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwPwrSupplyOverWarn.setStatus(
        "current"
    )

hwPwrSupplyUnderCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 1, 2, 3)
)
hwPwrSupplyUnderCrit.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwPwrSupplyUnderCrit.setStatus(
        "current"
    )

hwPwrSupplyUnderWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 1, 2, 5)
)
hwPwrSupplyUnderWarn.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwPwrSupplyUnderWarn.setStatus(
        "current"
    )

hwFanOverCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 2, 1, 3)
)
hwFanOverCrit.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwFanOverCrit.setStatus(
        "current"
    )

hwFanOverWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 2, 1, 5)
)
hwFanOverWarn.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwFanOverWarn.setStatus(
        "current"
    )

hwFanOverInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 2, 1, 7)
)
hwFanOverInfo.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwFanOverInfo.setStatus(
        "current"
    )

hwFanUnderCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 2, 2, 3)
)
hwFanUnderCrit.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwFanUnderCrit.setStatus(
        "current"
    )

hwFanUnderWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 2, 2, 5)
)
hwFanUnderWarn.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwFanUnderWarn.setStatus(
        "current"
    )

hwFanUnderInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 2, 2, 7)
)
hwFanUnderInfo.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwFanUnderInfo.setStatus(
        "current"
    )

hwFanCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 2, 3)
)
hwFanCrit.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwFanCrit.setStatus(
        "current"
    )

hwFanWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 2, 5)
)
hwFanWarn.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwFanWarn.setStatus(
        "current"
    )

hwVoltageOverCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 10, 1, 3)
)
hwVoltageOverCrit.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwVoltageOverCrit.setStatus(
        "current"
    )

hwVoltageOverWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 10, 1, 5)
)
hwVoltageOverWarn.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwVoltageOverWarn.setStatus(
        "current"
    )

hwVoltageOverInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 10, 1, 7)
)
hwVoltageOverInfo.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwVoltageOverInfo.setStatus(
        "current"
    )

hwVoltageUnderCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 10, 2, 3)
)
hwVoltageUnderCrit.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwVoltageUnderCrit.setStatus(
        "current"
    )

hwVoltageUnderWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 10, 2, 5)
)
hwVoltageUnderWarn.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwVoltageUnderWarn.setStatus(
        "current"
    )

hwVoltageUnderInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 10, 2, 7)
)
hwVoltageUnderInfo.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwVoltageUnderInfo.setStatus(
        "current"
    )

hwTempOverEmerg = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 11, 1, 1)
)
hwTempOverEmerg.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwTempOverEmerg.setStatus(
        "current"
    )

hwTempOverCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 11, 1, 3)
)
hwTempOverCrit.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwTempOverCrit.setStatus(
        "current"
    )

hwTempOverWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 11, 1, 5)
)
hwTempOverWarn.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwTempOverWarn.setStatus(
        "current"
    )

hwTempOverInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 11, 1, 7)
)
hwTempOverInfo.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwTempOverInfo.setStatus(
        "current"
    )

hwTempUnderEmerg = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 11, 2, 1)
)
hwTempUnderEmerg.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwTempUnderEmerg.setStatus(
        "current"
    )

hwTempUnderCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 11, 2, 3)
)
hwTempUnderCrit.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwTempUnderCrit.setStatus(
        "current"
    )

hwTempUnderWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 11, 2, 5)
)
hwTempUnderWarn.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwTempUnderWarn.setStatus(
        "current"
    )

hwTempUnderInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 11, 2, 7)
)
hwTempUnderInfo.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "i32Arg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwTempUnderInfo.setStatus(
        "current"
    )

hwPowerCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 12, 3)
)
hwPowerCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwPowerCrit.setStatus(
        "current"
    )

hwPowerWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 12, 5)
)
hwPowerWarn.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    hwPowerWarn.setStatus(
        "current"
    )

hwMemCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 13, 3)
)
hwMemCrit.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwMemCrit.setStatus(
        "current"
    )

hwCpuThrottleCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 14, 3)
)
hwCpuThrottleCrit.setObjects(
      *(("ISILON-TRAP-MIB", "measuredValueStr"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    hwCpuThrottleCrit.setStatus(
        "current"
    )

sensorMonitorCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 15, 1)
)
sensorMonitorCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    sensorMonitorCrit.setStatus(
        "current"
    )

sensorMonitorWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 15, 2)
)
sensorMonitorWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    sensorMonitorWarn.setStatus(
        "current"
    )

hwCurrentOverEmerg = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 16, 1, 1)
)
hwCurrentOverEmerg.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    hwCurrentOverEmerg.setStatus(
        "current"
    )

hwCurrentOverCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 16, 1, 3)
)
hwCurrentOverCrit.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    hwCurrentOverCrit.setStatus(
        "current"
    )

hwCurrentOverWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 16, 1, 5)
)
hwCurrentOverWarn.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    hwCurrentOverWarn.setStatus(
        "current"
    )

hwCurrentOverInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 16, 1, 7)
)
hwCurrentOverInfo.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    hwCurrentOverInfo.setStatus(
        "current"
    )

hwCurrentUnderEmerg = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 16, 2, 1)
)
hwCurrentUnderEmerg.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    hwCurrentUnderEmerg.setStatus(
        "current"
    )

hwCurrentUnderCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 16, 2, 3)
)
hwCurrentUnderCrit.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    hwCurrentUnderCrit.setStatus(
        "current"
    )

hwCurrentUnderWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 16, 2, 5)
)
hwCurrentUnderWarn.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    hwCurrentUnderWarn.setStatus(
        "current"
    )

hwCurrentUnderInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 21, 16, 2, 7)
)
hwCurrentUnderInfo.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    hwCurrentUnderInfo.setStatus(
        "current"
    )

sasPhyErrorExpanderWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 22, 1, 5)
)
sasPhyErrorExpanderWarn.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    sasPhyErrorExpanderWarn.setStatus(
        "current"
    )

sasPhyErrorControllerWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 22, 1, 7)
)
sasPhyErrorControllerWarn.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    sasPhyErrorControllerWarn.setStatus(
        "current"
    )

storageTransportCoalescedEmerg = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 22, 2, 1)
)
storageTransportCoalescedEmerg.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    storageTransportCoalescedEmerg.setStatus(
        "current"
    )

storageCoalescedCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 22, 2, 3)
)
storageCoalescedCrit.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    storageCoalescedCrit.setStatus(
        "current"
    )

storageCoalescedWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 22, 2, 5)
)
storageCoalescedWarn.setObjects(
    ("ISILON-TRAP-MIB", "instanceIdentifier")
)
if mibBuilder.loadTexts:
    storageCoalescedWarn.setStatus(
        "current"
    )

cloudpoolNetworkErrorCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 1, 3)
)
cloudpoolNetworkErrorCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "deviceIdentifier"),
        ("ISILON-TRAP-MIB", "errorMessage"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    cloudpoolNetworkErrorCrit.setStatus(
        "current"
    )

cloudpoolAuthenticationErrorCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 2, 3)
)
cloudpoolAuthenticationErrorCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "errorMessage"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    cloudpoolAuthenticationErrorCrit.setStatus(
        "current"
    )

cloudpoolAuthorizationErrorCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 3, 3)
)
cloudpoolAuthorizationErrorCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "errorMessage"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    cloudpoolAuthorizationErrorCrit.setStatus(
        "current"
    )

cloudpoolBucketNotFoundErrorCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 4, 3)
)
cloudpoolBucketNotFoundErrorCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "errorMessage"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    cloudpoolBucketNotFoundErrorCrit.setStatus(
        "current"
    )

cloudpoolObjectNotFoundErrorCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 5, 3)
)
cloudpoolObjectNotFoundErrorCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "errorMessage"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    cloudpoolObjectNotFoundErrorCrit.setStatus(
        "current"
    )

cloudpoolDataCorruptionIntegrityErrorEmerg = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 6, 1)
)
cloudpoolDataCorruptionIntegrityErrorEmerg.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "errorMessage"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    cloudpoolDataCorruptionIntegrityErrorEmerg.setStatus(
        "current"
    )

cloudpoolNoUsableAccountFoundErrorCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 7, 3)
)
cloudpoolNoUsableAccountFoundErrorCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    cloudpoolNoUsableAccountFoundErrorCrit.setStatus(
        "current"
    )

cloudpoolCertificateErrorCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 23, 8, 3)
)
cloudpoolCertificateErrorCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "errorMessage"),
        ("ISILON-TRAP-MIB", "instanceIdentifier"))
)
if mibBuilder.loadTexts:
    cloudpoolCertificateErrorCrit.setStatus(
        "current"
    )

upgradeStartInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24, 1, 7)
)
upgradeStartInfo.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"))
)
if mibBuilder.loadTexts:
    upgradeStartInfo.setStatus(
        "current"
    )

upgradeFinishInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24, 2, 7)
)
upgradeFinishInfo.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"))
)
if mibBuilder.loadTexts:
    upgradeFinishInfo.setStatus(
        "current"
    )

upgradeClusterEventCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24, 3, 3)
)
upgradeClusterEventCrit.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"))
)
if mibBuilder.loadTexts:
    upgradeClusterEventCrit.setStatus(
        "current"
    )

upgradeClusterEventWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24, 3, 5)
)
upgradeClusterEventWarn.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"))
)
if mibBuilder.loadTexts:
    upgradeClusterEventWarn.setStatus(
        "current"
    )

upgradeClusterEventInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24, 3, 7)
)
upgradeClusterEventInfo.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"))
)
if mibBuilder.loadTexts:
    upgradeClusterEventInfo.setStatus(
        "current"
    )

upgradeNodeEventCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24, 4, 3)
)
upgradeNodeEventCrit.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"))
)
if mibBuilder.loadTexts:
    upgradeNodeEventCrit.setStatus(
        "current"
    )

upgradeNodeEventWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24, 4, 5)
)
upgradeNodeEventWarn.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"))
)
if mibBuilder.loadTexts:
    upgradeNodeEventWarn.setStatus(
        "current"
    )

upgradeNodeEventInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24, 4, 7)
)
upgradeNodeEventInfo.setObjects(
      *(("ISILON-TRAP-MIB", "nodeIdentifier"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"))
)
if mibBuilder.loadTexts:
    upgradeNodeEventInfo.setStatus(
        "current"
    )

upgradeRollbackStartInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 12124, 250, 24, 5, 7)
)
upgradeRollbackStartInfo.setObjects(
      *(("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"),
        ("ISILON-TRAP-MIB", "stringArg"))
)
if mibBuilder.loadTexts:
    upgradeRollbackStartInfo.setStatus(
        "current"
    )


# Notifications groups

groupStateTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 1)
)
groupStateTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "nodeStatusCrit"),
        ("ISILON-TRAP-MIB", "nodeStatusInfo"),
        ("ISILON-TRAP-MIB", "nodeExpStatusCrit"),
        ("ISILON-TRAP-MIB", "nodeShutdownInfo"),
        ("ISILON-TRAP-MIB", "nodeShutdownFailCrit"),
        ("ISILON-TRAP-MIB", "nodeRebootCoalescedInfo"),
        ("ISILON-TRAP-MIB", "nodeStatusCoalescingCrit"),
        ("ISILON-TRAP-MIB", "nodeStatusCoalescingWarn"))
)
if mibBuilder.loadTexts:
    groupStateTrapsGroup.setStatus(
        "current"
    )

filesystemTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 11)
)
filesystemTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "partitionUsageCrit"),
        ("ISILON-TRAP-MIB", "partitionUsageWarn"),
        ("ISILON-TRAP-MIB", "partitionUsageInfo"),
        ("ISILON-TRAP-MIB", "clusterStorageUsageCrit"),
        ("ISILON-TRAP-MIB", "clusterStorageUsageWarn"),
        ("ISILON-TRAP-MIB", "filesysErrorCrit"),
        ("ISILON-TRAP-MIB", "filesysErrorWarn"),
        ("ISILON-TRAP-MIB", "filesysErrorInfo"),
        ("ISILON-TRAP-MIB", "diskPoolUsageCrit"),
        ("ISILON-TRAP-MIB", "diskPoolUsageWarn"),
        ("ISILON-TRAP-MIB", "diskPoolOldDbVersionWarn"),
        ("ISILON-TRAP-MIB", "ssdUsageCrit"),
        ("ISILON-TRAP-MIB", "ssdUsageWarn"),
        ("ISILON-TRAP-MIB", "ssdUsageInfo"),
        ("ISILON-TRAP-MIB", "filesysCoalesceCrit"),
        ("ISILON-TRAP-MIB", "filesysCoalesceWarn"))
)
if mibBuilder.loadTexts:
    filesystemTrapsGroup.setStatus(
        "current"
    )

smartQuotaTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 12)
)
smartQuotaTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "quotaThreshErrorInfo"),
        ("ISILON-TRAP-MIB", "quotaNotifyErrorWarn"),
        ("ISILON-TRAP-MIB", "quotaErrorWarn"))
)
if mibBuilder.loadTexts:
    smartQuotaTrapsGroup.setStatus(
        "current"
    )

snapshotTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 13)
)
snapshotTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "snapshotErrorWarn"),
        ("ISILON-TRAP-MIB", "snapshotReserveCrit"),
        ("ISILON-TRAP-MIB", "snapshotReserveWarn"))
)
if mibBuilder.loadTexts:
    snapshotTrapsGroup.setStatus(
        "current"
    )

syncIQTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 14)
)
syncIQTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "siqEventCrit"),
        ("ISILON-TRAP-MIB", "siqEventWarn"),
        ("ISILON-TRAP-MIB", "siqErrorWarn"),
        ("ISILON-TRAP-MIB", "siqPolicyCoalescedCrit"),
        ("ISILON-TRAP-MIB", "siqPolicyCoalescedWarn"),
        ("ISILON-TRAP-MIB", "siqTargetCoalescedCrit"),
        ("ISILON-TRAP-MIB", "siqTargetCoalescedWarn"))
)
if mibBuilder.loadTexts:
    syncIQTrapsGroup.setStatus(
        "current"
    )

softwareTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 15)
)
softwareTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "jobEngineErrorEmerg"),
        ("ISILON-TRAP-MIB", "jobEngineErrorCrit"),
        ("ISILON-TRAP-MIB", "jobEngineErrorWarn"),
        ("ISILON-TRAP-MIB", "jobEngineErrorInfo"),
        ("ISILON-TRAP-MIB", "flexProtectRunningCrit"),
        ("ISILON-TRAP-MIB", "flexProtectRunningWarn"),
        ("ISILON-TRAP-MIB", "flexProtectRunningInfo"),
        ("ISILON-TRAP-MIB", "mcpProcFailedWarn"),
        ("ISILON-TRAP-MIB", "mcpProcKilledWarn"),
        ("ISILON-TRAP-MIB", "licenseExpirationWarn"),
        ("ISILON-TRAP-MIB", "licenseExpirationInfo"),
        ("ISILON-TRAP-MIB", "firmwareUpdateIncompleteWarn"),
        ("ISILON-TRAP-MIB", "testEventCrit"),
        ("ISILON-TRAP-MIB", "nodeCPUWarn"),
        ("ISILON-TRAP-MIB", "nodeCPUInfo"),
        ("ISILON-TRAP-MIB", "mountdClientMountFailedInfo"),
        ("ISILON-TRAP-MIB", "mountdHostLookupFailedInfo"),
        ("ISILON-TRAP-MIB", "nfsCookieTranslationFailedInfo"),
        ("ISILON-TRAP-MIB", "mixedSedNonSedClusterCrit"))
)
if mibBuilder.loadTexts:
    softwareTrapsGroup.setStatus(
        "current"
    )

avscanTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 16)
)
avscanTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "avscanNoServersConfCrit"),
        ("ISILON-TRAP-MIB", "avscanNoServersConfWarn"),
        ("ISILON-TRAP-MIB", "avscanNoServersConfInfo"),
        ("ISILON-TRAP-MIB", "avscanErrorCrit"),
        ("ISILON-TRAP-MIB", "avscanErrorWarn"),
        ("ISILON-TRAP-MIB", "avscanErrorInfo"),
        ("ISILON-TRAP-MIB", "avscanInfectedFileCrit"),
        ("ISILON-TRAP-MIB", "avscanInfectedFileWarn"),
        ("ISILON-TRAP-MIB", "avscanInfectedFileInfo"),
        ("ISILON-TRAP-MIB", "avscanCoalescedInfo"),
        ("ISILON-TRAP-MIB", "avscanCoalescedWarn"),
        ("ISILON-TRAP-MIB", "avscanCoalescedCrit"))
)
if mibBuilder.loadTexts:
    avscanTrapsGroup.setStatus(
        "current"
    )

netProtoTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 17)
)
netProtoTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "clockSkewCrit"),
        ("ISILON-TRAP-MIB", "sharePermsUpgradeFailCrit"),
        ("ISILON-TRAP-MIB", "winTimeConnectivityLostWarn"),
        ("ISILON-TRAP-MIB", "winNetMapFullCrit"),
        ("ISILON-TRAP-MIB", "winNetAuthCrit"),
        ("ISILON-TRAP-MIB", "winNetAuthWarn"),
        ("ISILON-TRAP-MIB", "lwioParamCrit"),
        ("ISILON-TRAP-MIB", "winSmbUpgradeWarn"),
        ("ISILON-TRAP-MIB", "winSmbUpgradeCrit"),
        ("ISILON-TRAP-MIB", "winNetworkCoalesceCrit"),
        ("ISILON-TRAP-MIB", "winNetworkCoalesceWarn"),
        ("ISILON-TRAP-MIB", "winIDmapCoalesceCrit"),
        ("ISILON-TRAP-MIB", "winIDmapCoalesceWarn"),
        ("ISILON-TRAP-MIB", "winAuthUpgradeCrit"),
        ("ISILON-TRAP-MIB", "winAuthCoalesceCrit"),
        ("ISILON-TRAP-MIB", "winAuthCoalesceWarn"))
)
if mibBuilder.loadTexts:
    netProtoTrapsGroup.setStatus(
        "current"
    )

networkingTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 18)
)
networkingTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "netStatusCrit"),
        ("ISILON-TRAP-MIB", "netStatusWarn"),
        ("ISILON-TRAP-MIB", "netStatusCoalescingCrit"),
        ("ISILON-TRAP-MIB", "netStatusCoalescingWarn"))
)
if mibBuilder.loadTexts:
    networkingTrapsGroup.setStatus(
        "current"
    )

hardwareTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 19)
)
hardwareTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "hardwareErrorMsgCrit"),
        ("ISILON-TRAP-MIB", "hardwareErrorMsgWarn"),
        ("ISILON-TRAP-MIB", "hardwareErrorCrit"),
        ("ISILON-TRAP-MIB", "hardwareErrorWarn"),
        ("ISILON-TRAP-MIB", "hardwareErrorInfo"),
        ("ISILON-TRAP-MIB", "hwErrorCrit"),
        ("ISILON-TRAP-MIB", "diskNodeOfflineCrit"),
        ("ISILON-TRAP-MIB", "hardwareCoalescedEmerg"),
        ("ISILON-TRAP-MIB", "hardwareCoalescedCrit"),
        ("ISILON-TRAP-MIB", "hardwareCoalescedWarn"),
        ("ISILON-TRAP-MIB", "sensorCoalescedEmerg"),
        ("ISILON-TRAP-MIB", "sensorCoalescedCrit"),
        ("ISILON-TRAP-MIB", "sensorCoalescedWarn"),
        ("ISILON-TRAP-MIB", "fanCoalescedEmerg"),
        ("ISILON-TRAP-MIB", "fanCoalescedCrit"),
        ("ISILON-TRAP-MIB", "fanCoalescedWarn"),
        ("ISILON-TRAP-MIB", "tempCoalescedEmerg"),
        ("ISILON-TRAP-MIB", "tempCoalescedCrit"),
        ("ISILON-TRAP-MIB", "tempCoalescedWarn"),
        ("ISILON-TRAP-MIB", "voltsCoalescedEmerg"),
        ("ISILON-TRAP-MIB", "voltsCoalescedCrit"),
        ("ISILON-TRAP-MIB", "voltsCoalescedWarn"))
)
if mibBuilder.loadTexts:
    hardwareTrapsGroup.setStatus(
        "current"
    )

systemDiskTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 20)
)
systemDiskTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "driveStatusInfo"),
        ("ISILON-TRAP-MIB", "driveStatusCrit"),
        ("ISILON-TRAP-MIB", "driveStatusWarn"),
        ("ISILON-TRAP-MIB", "bootDiskFailCrit"),
        ("ISILON-TRAP-MIB", "bootDiskFailWarn"),
        ("ISILON-TRAP-MIB", "diskErrorWarn"),
        ("ISILON-TRAP-MIB", "bootdiskMirrorReqMissingCrit"),
        ("ISILON-TRAP-MIB", "diskErrorCoalescedCrit"),
        ("ISILON-TRAP-MIB", "diskErrorCoalescedWarn"))
)
if mibBuilder.loadTexts:
    systemDiskTrapsGroup.setStatus(
        "current"
    )

sensorTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 21)
)
sensorTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "hwPwrSupplyOverCrit"),
        ("ISILON-TRAP-MIB", "hwPwrSupplyOverWarn"),
        ("ISILON-TRAP-MIB", "hwPwrSupplyUnderCrit"),
        ("ISILON-TRAP-MIB", "hwPwrSupplyUnderWarn"),
        ("ISILON-TRAP-MIB", "hwFanOverCrit"),
        ("ISILON-TRAP-MIB", "hwFanOverWarn"),
        ("ISILON-TRAP-MIB", "hwFanOverInfo"),
        ("ISILON-TRAP-MIB", "hwFanUnderCrit"),
        ("ISILON-TRAP-MIB", "hwFanUnderWarn"),
        ("ISILON-TRAP-MIB", "hwFanUnderInfo"),
        ("ISILON-TRAP-MIB", "hwVoltageOverCrit"),
        ("ISILON-TRAP-MIB", "hwVoltageOverWarn"),
        ("ISILON-TRAP-MIB", "hwVoltageOverInfo"),
        ("ISILON-TRAP-MIB", "hwVoltageUnderCrit"),
        ("ISILON-TRAP-MIB", "hwVoltageUnderWarn"),
        ("ISILON-TRAP-MIB", "hwVoltageUnderInfo"),
        ("ISILON-TRAP-MIB", "hwTempOverEmerg"),
        ("ISILON-TRAP-MIB", "hwTempOverCrit"),
        ("ISILON-TRAP-MIB", "hwTempOverWarn"),
        ("ISILON-TRAP-MIB", "hwTempOverInfo"),
        ("ISILON-TRAP-MIB", "hwTempUnderEmerg"),
        ("ISILON-TRAP-MIB", "hwTempUnderCrit"),
        ("ISILON-TRAP-MIB", "hwTempUnderWarn"),
        ("ISILON-TRAP-MIB", "hwTempUnderInfo"),
        ("ISILON-TRAP-MIB", "hwPowerCrit"),
        ("ISILON-TRAP-MIB", "hwPowerWarn"),
        ("ISILON-TRAP-MIB", "hwMemCrit"),
        ("ISILON-TRAP-MIB", "hwFanCrit"),
        ("ISILON-TRAP-MIB", "hwFanWarn"),
        ("ISILON-TRAP-MIB", "hwCpuThrottleCrit"),
        ("ISILON-TRAP-MIB", "sensorMonitorCrit"),
        ("ISILON-TRAP-MIB", "sensorMonitorWarn"),
        ("ISILON-TRAP-MIB", "hwCurrentOverEmerg"),
        ("ISILON-TRAP-MIB", "hwCurrentOverCrit"),
        ("ISILON-TRAP-MIB", "hwCurrentOverWarn"),
        ("ISILON-TRAP-MIB", "hwCurrentOverInfo"),
        ("ISILON-TRAP-MIB", "hwCurrentUnderEmerg"),
        ("ISILON-TRAP-MIB", "hwCurrentUnderCrit"),
        ("ISILON-TRAP-MIB", "hwCurrentUnderWarn"),
        ("ISILON-TRAP-MIB", "hwCurrentUnderInfo"))
)
if mibBuilder.loadTexts:
    sensorTrapsGroup.setStatus(
        "current"
    )

storageTransportTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 22)
)
storageTransportTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "sasPhyErrorExpanderWarn"),
        ("ISILON-TRAP-MIB", "sasPhyErrorControllerWarn"),
        ("ISILON-TRAP-MIB", "storageTransportCoalescedEmerg"),
        ("ISILON-TRAP-MIB", "storageCoalescedCrit"),
        ("ISILON-TRAP-MIB", "storageCoalescedWarn"))
)
if mibBuilder.loadTexts:
    storageTransportTrapsGroup.setStatus(
        "current"
    )

cloudPoolsTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 23)
)
cloudPoolsTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "cloudpoolNetworkErrorCrit"),
        ("ISILON-TRAP-MIB", "cloudpoolAuthenticationErrorCrit"),
        ("ISILON-TRAP-MIB", "cloudpoolAuthorizationErrorCrit"),
        ("ISILON-TRAP-MIB", "cloudpoolBucketNotFoundErrorCrit"),
        ("ISILON-TRAP-MIB", "cloudpoolObjectNotFoundErrorCrit"),
        ("ISILON-TRAP-MIB", "cloudpoolDataCorruptionIntegrityErrorEmerg"),
        ("ISILON-TRAP-MIB", "cloudpoolNoUsableAccountFoundErrorCrit"),
        ("ISILON-TRAP-MIB", "cloudpoolCertificateErrorCrit"))
)
if mibBuilder.loadTexts:
    cloudPoolsTrapsGroup.setStatus(
        "current"
    )

upgradeTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12124, 250, 51, 24)
)
upgradeTrapsGroup.setObjects(
      *(("ISILON-TRAP-MIB", "upgradeStartInfo"),
        ("ISILON-TRAP-MIB", "upgradeFinishInfo"),
        ("ISILON-TRAP-MIB", "upgradeClusterEventCrit"),
        ("ISILON-TRAP-MIB", "upgradeClusterEventWarn"),
        ("ISILON-TRAP-MIB", "upgradeClusterEventInfo"),
        ("ISILON-TRAP-MIB", "upgradeNodeEventCrit"),
        ("ISILON-TRAP-MIB", "upgradeNodeEventWarn"),
        ("ISILON-TRAP-MIB", "upgradeNodeEventInfo"),
        ("ISILON-TRAP-MIB", "upgradeRollbackStartInfo"))
)
if mibBuilder.loadTexts:
    upgradeTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

trapGroupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12124, 250, 52, 1)
)
if mibBuilder.loadTexts:
    trapGroupCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISILON-TRAP-MIB",
    **{"isilonTraps": isilonTraps,
       "groupStateTraps": groupStateTraps,
       "nodeStatus": nodeStatus,
       "nodeStatusCrit": nodeStatusCrit,
       "nodeStatusInfo": nodeStatusInfo,
       "nodeExpStatus": nodeExpStatus,
       "nodeExpStatusCrit": nodeExpStatusCrit,
       "nodeShutdown": nodeShutdown,
       "nodeShutdownInfo": nodeShutdownInfo,
       "nodeShutdownFail": nodeShutdownFail,
       "nodeShutdownFailCrit": nodeShutdownFailCrit,
       "nodeRebootCoalesced": nodeRebootCoalesced,
       "nodeRebootCoalescedInfo": nodeRebootCoalescedInfo,
       "nodeStatusCoalescing": nodeStatusCoalescing,
       "nodeStatusCoalescingCrit": nodeStatusCoalescingCrit,
       "nodeStatusCoalescingWarn": nodeStatusCoalescingWarn,
       "filesystemTraps": filesystemTraps,
       "partitionUsage": partitionUsage,
       "partitionUsageCrit": partitionUsageCrit,
       "partitionUsageWarn": partitionUsageWarn,
       "partitionUsageInfo": partitionUsageInfo,
       "clusterStorageUsage": clusterStorageUsage,
       "clusterStorageUsageCrit": clusterStorageUsageCrit,
       "clusterStorageUsageWarn": clusterStorageUsageWarn,
       "filesysError": filesysError,
       "filesysErrorCrit": filesysErrorCrit,
       "filesysErrorWarn": filesysErrorWarn,
       "filesysErrorInfo": filesysErrorInfo,
       "diskPoolUsage": diskPoolUsage,
       "diskPoolUsageCrit": diskPoolUsageCrit,
       "diskPoolUsageWarn": diskPoolUsageWarn,
       "diskPoolOldDbVersion": diskPoolOldDbVersion,
       "diskPoolOldDbVersionWarn": diskPoolOldDbVersionWarn,
       "ssdUsage": ssdUsage,
       "ssdUsageCrit": ssdUsageCrit,
       "ssdUsageWarn": ssdUsageWarn,
       "ssdUsageInfo": ssdUsageInfo,
       "filesysCoalesce": filesysCoalesce,
       "filesysCoalesceCrit": filesysCoalesceCrit,
       "filesysCoalesceWarn": filesysCoalesceWarn,
       "smartQuotaTraps": smartQuotaTraps,
       "quotaThreshError": quotaThreshError,
       "quotaThreshErrorInfo": quotaThreshErrorInfo,
       "quotaNotifyError": quotaNotifyError,
       "quotaNotifyErrorWarn": quotaNotifyErrorWarn,
       "quotaError": quotaError,
       "quotaErrorWarn": quotaErrorWarn,
       "snapshotTraps": snapshotTraps,
       "snapshotError": snapshotError,
       "snapshotErrorWarn": snapshotErrorWarn,
       "snapshotReserve": snapshotReserve,
       "snapshotReserveCrit": snapshotReserveCrit,
       "snapshotReserveWarn": snapshotReserveWarn,
       "syncIQTraps": syncIQTraps,
       "siqEvent": siqEvent,
       "siqEventCrit": siqEventCrit,
       "siqEventWarn": siqEventWarn,
       "siqError": siqError,
       "siqErrorWarn": siqErrorWarn,
       "siqPolicyCoalesced": siqPolicyCoalesced,
       "siqPolicyCoalescedCrit": siqPolicyCoalescedCrit,
       "siqPolicyCoalescedWarn": siqPolicyCoalescedWarn,
       "siqTargetCoalesced": siqTargetCoalesced,
       "siqTargetCoalescedCrit": siqTargetCoalescedCrit,
       "siqTargetCoalescedWarn": siqTargetCoalescedWarn,
       "softwareTraps": softwareTraps,
       "jobEngineError": jobEngineError,
       "jobEngineErrorEmerg": jobEngineErrorEmerg,
       "jobEngineErrorCrit": jobEngineErrorCrit,
       "jobEngineErrorWarn": jobEngineErrorWarn,
       "jobEngineErrorInfo": jobEngineErrorInfo,
       "flexProtectRunning": flexProtectRunning,
       "flexProtectRunningCrit": flexProtectRunningCrit,
       "flexProtectRunningWarn": flexProtectRunningWarn,
       "flexProtectRunningInfo": flexProtectRunningInfo,
       "avscanInfectedFile": avscanInfectedFile,
       "avscanInfectedFileCrit": avscanInfectedFileCrit,
       "avscanInfectedFileWarn": avscanInfectedFileWarn,
       "avscanInfectedFileInfo": avscanInfectedFileInfo,
       "mcpProcFailed": mcpProcFailed,
       "mcpProcFailedWarn": mcpProcFailedWarn,
       "mcpProcKilled": mcpProcKilled,
       "mcpProcKilledWarn": mcpProcKilledWarn,
       "licenseExpiration": licenseExpiration,
       "licenseExpirationWarn": licenseExpirationWarn,
       "licenseExpirationInfo": licenseExpirationInfo,
       "firmwareUpdateIncomplete": firmwareUpdateIncomplete,
       "firmwareUpdateIncompleteWarn": firmwareUpdateIncompleteWarn,
       "testEvent": testEvent,
       "testEventCrit": testEventCrit,
       "nodeCPU": nodeCPU,
       "nodeCPUWarn": nodeCPUWarn,
       "nodeCPUInfo": nodeCPUInfo,
       "mountdClientMountFailed": mountdClientMountFailed,
       "mountdClientMountFailedInfo": mountdClientMountFailedInfo,
       "mountdHostLookupFailed": mountdHostLookupFailed,
       "mountdHostLookupFailedInfo": mountdHostLookupFailedInfo,
       "mixedSedNonSedCluster": mixedSedNonSedCluster,
       "mixedSedNonSedClusterCrit": mixedSedNonSedClusterCrit,
       "nfsCookieTranslationFailed": nfsCookieTranslationFailed,
       "nfsCookieTranslationFailedInfo": nfsCookieTranslationFailedInfo,
       "avscanTraps": avscanTraps,
       "avscanNoServersConf": avscanNoServersConf,
       "avscanNoServersConfCrit": avscanNoServersConfCrit,
       "avscanNoServersConfWarn": avscanNoServersConfWarn,
       "avscanNoServersConfInfo": avscanNoServersConfInfo,
       "avscanError": avscanError,
       "avscanErrorCrit": avscanErrorCrit,
       "avscanErrorWarn": avscanErrorWarn,
       "avscanErrorInfo": avscanErrorInfo,
       "avscanCoalesced": avscanCoalesced,
       "avscanCoalescedInfo": avscanCoalescedInfo,
       "avscanCoalescedWarn": avscanCoalescedWarn,
       "avscanCoalescedCrit": avscanCoalescedCrit,
       "netProtoTraps": netProtoTraps,
       "clockSkew": clockSkew,
       "clockSkewCrit": clockSkewCrit,
       "sharePermsUpgradeFail": sharePermsUpgradeFail,
       "sharePermsUpgradeFailCrit": sharePermsUpgradeFailCrit,
       "winTimeConnectivityLost": winTimeConnectivityLost,
       "winTimeConnectivityLostWarn": winTimeConnectivityLostWarn,
       "winNetMapFull": winNetMapFull,
       "winNetMapFullCrit": winNetMapFullCrit,
       "winNetAuth": winNetAuth,
       "winNetAuthCrit": winNetAuthCrit,
       "winNetAuthWarn": winNetAuthWarn,
       "lwioParam": lwioParam,
       "lwioParamCrit": lwioParamCrit,
       "winSmbUpgrade": winSmbUpgrade,
       "winSmbUpgradeWarn": winSmbUpgradeWarn,
       "winSmbUpgradeCrit": winSmbUpgradeCrit,
       "winNetworkCoalesce": winNetworkCoalesce,
       "winNetworkCoalesceCrit": winNetworkCoalesceCrit,
       "winNetworkCoalesceWarn": winNetworkCoalesceWarn,
       "winIDmapCoalesce": winIDmapCoalesce,
       "winIDmapCoalesceCrit": winIDmapCoalesceCrit,
       "winIDmapCoalesceWarn": winIDmapCoalesceWarn,
       "winAuthCoalesce": winAuthCoalesce,
       "winAuthCoalesceCrit": winAuthCoalesceCrit,
       "winAuthCoalesceWarn": winAuthCoalesceWarn,
       "winAuthUpgrade": winAuthUpgrade,
       "winAuthUpgradeCrit": winAuthUpgradeCrit,
       "networkingTraps": networkingTraps,
       "netStatus": netStatus,
       "netStatusCrit": netStatusCrit,
       "netStatusWarn": netStatusWarn,
       "netStatusCoalescing": netStatusCoalescing,
       "netStatusCoalescingCrit": netStatusCoalescingCrit,
       "netStatusCoalescingWarn": netStatusCoalescingWarn,
       "hardwareTraps": hardwareTraps,
       "hardwareError": hardwareError,
       "hardwareErrorMsg": hardwareErrorMsg,
       "hardwareErrorMsgCrit": hardwareErrorMsgCrit,
       "hardwareErrorMsgWarn": hardwareErrorMsgWarn,
       "hardwareErrorCrit": hardwareErrorCrit,
       "hardwareErrorWarn": hardwareErrorWarn,
       "hardwareErrorInfo": hardwareErrorInfo,
       "hwError": hwError,
       "hwErrorCrit": hwErrorCrit,
       "diskNodeOffline": diskNodeOffline,
       "diskNodeOfflineCrit": diskNodeOfflineCrit,
       "hardwareCoalesced": hardwareCoalesced,
       "hardwareCoalescedEmerg": hardwareCoalescedEmerg,
       "hardwareCoalescedCrit": hardwareCoalescedCrit,
       "hardwareCoalescedWarn": hardwareCoalescedWarn,
       "sensorCoalesced": sensorCoalesced,
       "sensorCoalescedEmerg": sensorCoalescedEmerg,
       "sensorCoalescedCrit": sensorCoalescedCrit,
       "sensorCoalescedWarn": sensorCoalescedWarn,
       "fanCoalesced": fanCoalesced,
       "fanCoalescedEmerg": fanCoalescedEmerg,
       "fanCoalescedCrit": fanCoalescedCrit,
       "fanCoalescedWarn": fanCoalescedWarn,
       "tempCoalesced": tempCoalesced,
       "tempCoalescedEmerg": tempCoalescedEmerg,
       "tempCoalescedCrit": tempCoalescedCrit,
       "tempCoalescedWarn": tempCoalescedWarn,
       "voltsCoalesced": voltsCoalesced,
       "voltsCoalescedEmerg": voltsCoalescedEmerg,
       "voltsCoalescedCrit": voltsCoalescedCrit,
       "voltsCoalescedWarn": voltsCoalescedWarn,
       "systemDiskTraps": systemDiskTraps,
       "driveStatus": driveStatus,
       "driveStatusInfo": driveStatusInfo,
       "driveStatusCrit": driveStatusCrit,
       "driveStatusWarn": driveStatusWarn,
       "bootDiskFail": bootDiskFail,
       "bootDiskFailCrit": bootDiskFailCrit,
       "bootDiskFailWarn": bootDiskFailWarn,
       "diskError": diskError,
       "diskErrorWarn": diskErrorWarn,
       "bootDiskMirrorReqMissing": bootDiskMirrorReqMissing,
       "bootdiskMirrorReqMissingCrit": bootdiskMirrorReqMissingCrit,
       "diskErrorCoalesced": diskErrorCoalesced,
       "diskErrorCoalescedCrit": diskErrorCoalescedCrit,
       "diskErrorCoalescedWarn": diskErrorCoalescedWarn,
       "sensorTraps": sensorTraps,
       "hwPwrSupply": hwPwrSupply,
       "hwPwrSupplyOver": hwPwrSupplyOver,
       "hwPwrSupplyOverCrit": hwPwrSupplyOverCrit,
       "hwPwrSupplyOverWarn": hwPwrSupplyOverWarn,
       "hwPwrSupplyUnder": hwPwrSupplyUnder,
       "hwPwrSupplyUnderCrit": hwPwrSupplyUnderCrit,
       "hwPwrSupplyUnderWarn": hwPwrSupplyUnderWarn,
       "hwFan": hwFan,
       "hwFanOver": hwFanOver,
       "hwFanOverCrit": hwFanOverCrit,
       "hwFanOverWarn": hwFanOverWarn,
       "hwFanOverInfo": hwFanOverInfo,
       "hwFanUnder": hwFanUnder,
       "hwFanUnderCrit": hwFanUnderCrit,
       "hwFanUnderWarn": hwFanUnderWarn,
       "hwFanUnderInfo": hwFanUnderInfo,
       "hwFanCrit": hwFanCrit,
       "hwFanWarn": hwFanWarn,
       "hwVoltage": hwVoltage,
       "hwVoltageOver": hwVoltageOver,
       "hwVoltageOverCrit": hwVoltageOverCrit,
       "hwVoltageOverWarn": hwVoltageOverWarn,
       "hwVoltageOverInfo": hwVoltageOverInfo,
       "hwVoltageUnder": hwVoltageUnder,
       "hwVoltageUnderCrit": hwVoltageUnderCrit,
       "hwVoltageUnderWarn": hwVoltageUnderWarn,
       "hwVoltageUnderInfo": hwVoltageUnderInfo,
       "hwTemp": hwTemp,
       "hwTempOver": hwTempOver,
       "hwTempOverEmerg": hwTempOverEmerg,
       "hwTempOverCrit": hwTempOverCrit,
       "hwTempOverWarn": hwTempOverWarn,
       "hwTempOverInfo": hwTempOverInfo,
       "hwTempUnder": hwTempUnder,
       "hwTempUnderEmerg": hwTempUnderEmerg,
       "hwTempUnderCrit": hwTempUnderCrit,
       "hwTempUnderWarn": hwTempUnderWarn,
       "hwTempUnderInfo": hwTempUnderInfo,
       "hwPower": hwPower,
       "hwPowerCrit": hwPowerCrit,
       "hwPowerWarn": hwPowerWarn,
       "hwMem": hwMem,
       "hwMemCrit": hwMemCrit,
       "hwCpuThrottle": hwCpuThrottle,
       "hwCpuThrottleCrit": hwCpuThrottleCrit,
       "sensorMonitor": sensorMonitor,
       "sensorMonitorCrit": sensorMonitorCrit,
       "sensorMonitorWarn": sensorMonitorWarn,
       "hwCurrent": hwCurrent,
       "hwCurrentOver": hwCurrentOver,
       "hwCurrentOverEmerg": hwCurrentOverEmerg,
       "hwCurrentOverCrit": hwCurrentOverCrit,
       "hwCurrentOverWarn": hwCurrentOverWarn,
       "hwCurrentOverInfo": hwCurrentOverInfo,
       "hwCurrentUnder": hwCurrentUnder,
       "hwCurrentUnderEmerg": hwCurrentUnderEmerg,
       "hwCurrentUnderCrit": hwCurrentUnderCrit,
       "hwCurrentUnderWarn": hwCurrentUnderWarn,
       "hwCurrentUnderInfo": hwCurrentUnderInfo,
       "storageTransportTraps": storageTransportTraps,
       "sasPhyError": sasPhyError,
       "sasPhyErrorExpanderWarn": sasPhyErrorExpanderWarn,
       "sasPhyErrorControllerWarn": sasPhyErrorControllerWarn,
       "storageTransportCoalesced": storageTransportCoalesced,
       "storageTransportCoalescedEmerg": storageTransportCoalescedEmerg,
       "storageCoalescedCrit": storageCoalescedCrit,
       "storageCoalescedWarn": storageCoalescedWarn,
       "cloudPoolsTraps": cloudPoolsTraps,
       "cloudpoolNetworkError": cloudpoolNetworkError,
       "cloudpoolNetworkErrorCrit": cloudpoolNetworkErrorCrit,
       "cloudpoolAuthenticationError": cloudpoolAuthenticationError,
       "cloudpoolAuthenticationErrorCrit": cloudpoolAuthenticationErrorCrit,
       "cloudpoolAuthorizationError": cloudpoolAuthorizationError,
       "cloudpoolAuthorizationErrorCrit": cloudpoolAuthorizationErrorCrit,
       "cloudpoolBucketNotFoundError": cloudpoolBucketNotFoundError,
       "cloudpoolBucketNotFoundErrorCrit": cloudpoolBucketNotFoundErrorCrit,
       "cloudpoolObjectNotFoundError": cloudpoolObjectNotFoundError,
       "cloudpoolObjectNotFoundErrorCrit": cloudpoolObjectNotFoundErrorCrit,
       "cloudpoolDataCorruptionIntegrityError": cloudpoolDataCorruptionIntegrityError,
       "cloudpoolDataCorruptionIntegrityErrorEmerg": cloudpoolDataCorruptionIntegrityErrorEmerg,
       "cloudpoolNoUsableAccountFoundError": cloudpoolNoUsableAccountFoundError,
       "cloudpoolNoUsableAccountFoundErrorCrit": cloudpoolNoUsableAccountFoundErrorCrit,
       "cloudpoolCertificateError": cloudpoolCertificateError,
       "cloudpoolCertificateErrorCrit": cloudpoolCertificateErrorCrit,
       "upgradeTraps": upgradeTraps,
       "upgradeStart": upgradeStart,
       "upgradeStartInfo": upgradeStartInfo,
       "upgradeFinish": upgradeFinish,
       "upgradeFinishInfo": upgradeFinishInfo,
       "upgradeClusterEvent": upgradeClusterEvent,
       "upgradeClusterEventCrit": upgradeClusterEventCrit,
       "upgradeClusterEventWarn": upgradeClusterEventWarn,
       "upgradeClusterEventInfo": upgradeClusterEventInfo,
       "upgradeNodeEvent": upgradeNodeEvent,
       "upgradeNodeEventCrit": upgradeNodeEventCrit,
       "upgradeNodeEventWarn": upgradeNodeEventWarn,
       "upgradeNodeEventInfo": upgradeNodeEventInfo,
       "upgradeRollbackStart": upgradeRollbackStart,
       "upgradeRollbackStartInfo": upgradeRollbackStartInfo,
       "variables": variables,
       "nodeIdentifier": nodeIdentifier,
       "measuredValue": measuredValue,
       "units": units,
       "oid": oid,
       "bay": bay,
       "ifName": ifName,
       "phy": phy,
       "errorMessage": errorMessage,
       "errno": errno,
       "stringArg": stringArg,
       "message": message,
       "i64Arg": i64Arg,
       "i32Arg": i32Arg,
       "measuredValueStr": measuredValueStr,
       "instanceIdentifier": instanceIdentifier,
       "deviceIdentifier": deviceIdentifier,
       "trapConformance": trapConformance,
       "groupStateTrapsGroup": groupStateTrapsGroup,
       "filesystemTrapsGroup": filesystemTrapsGroup,
       "smartQuotaTrapsGroup": smartQuotaTrapsGroup,
       "snapshotTrapsGroup": snapshotTrapsGroup,
       "syncIQTrapsGroup": syncIQTrapsGroup,
       "softwareTrapsGroup": softwareTrapsGroup,
       "avscanTrapsGroup": avscanTrapsGroup,
       "netProtoTrapsGroup": netProtoTrapsGroup,
       "networkingTrapsGroup": networkingTrapsGroup,
       "hardwareTrapsGroup": hardwareTrapsGroup,
       "systemDiskTrapsGroup": systemDiskTrapsGroup,
       "sensorTrapsGroup": sensorTrapsGroup,
       "storageTransportTrapsGroup": storageTransportTrapsGroup,
       "cloudPoolsTrapsGroup": cloudPoolsTrapsGroup,
       "upgradeTrapsGroup": upgradeTrapsGroup,
       "variablesGroup": variablesGroup,
       "trapCompliance": trapCompliance,
       "trapGroupCompliance": trapGroupCompliance}
)
