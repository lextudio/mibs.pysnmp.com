# SNMP MIB module (SUN-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUN-CLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:31 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

sunclustermod = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Prod_ObjectIdentity = ObjectIdentity
prod = _Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Suncluster_ObjectIdentity = ObjectIdentity
suncluster = _Suncluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80)
)
_Sunmc_ObjectIdentity = ObjectIdentity
sunmc = _Sunmc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1)
)
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1)
)
_ClusterInfo_ObjectIdentity = ObjectIdentity
clusterInfo = _ClusterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 1)
)
_ClusterStatus_ObjectIdentity = ObjectIdentity
clusterStatus = _ClusterStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 1, 1)
)
_ClsClusterName_Type = DisplayString
_ClsClusterName_Object = MibScalar
clsClusterName = _ClsClusterName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 1, 1, 1),
    _ClsClusterName_Type()
)
clsClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsClusterName.setStatus("current")
_ClsMinVotesRequired_Type = Integer32
_ClsMinVotesRequired_Object = MibScalar
clsMinVotesRequired = _ClsMinVotesRequired_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 1, 1, 2),
    _ClsMinVotesRequired_Type()
)
clsMinVotesRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsMinVotesRequired.setStatus("current")
_ClsCurrentVotes_Type = Integer32
_ClsCurrentVotes_Object = MibScalar
clsCurrentVotes = _ClsCurrentVotes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 1, 1, 3),
    _ClsCurrentVotes_Type()
)
clsCurrentVotes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsCurrentVotes.setStatus("current")
_ClusterConfiguration_ObjectIdentity = ObjectIdentity
clusterConfiguration = _ClusterConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 1, 2)
)
_ClcClusterName_Type = DisplayString
_ClcClusterName_Object = MibScalar
clcClusterName = _ClcClusterName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 1, 2, 1),
    _ClcClusterName_Type()
)
clcClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcClusterName.setStatus("current")
_ClcInstallMode_Type = DisplayString
_ClcInstallMode_Object = MibScalar
clcInstallMode = _ClcInstallMode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 1, 2, 2),
    _ClcInstallMode_Type()
)
clcInstallMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcInstallMode.setStatus("current")
_ClcPrivateNetAddr_Type = DisplayString
_ClcPrivateNetAddr_Object = MibScalar
clcPrivateNetAddr = _ClcPrivateNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 1, 2, 3),
    _ClcPrivateNetAddr_Type()
)
clcPrivateNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcPrivateNetAddr.setStatus("current")
_ClcPrivateNetMask_Type = DisplayString
_ClcPrivateNetMask_Object = MibScalar
clcPrivateNetMask = _ClcPrivateNetMask_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 1, 2, 4),
    _ClcPrivateNetMask_Type()
)
clcPrivateNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcPrivateNetMask.setStatus("current")
_ClcAddNodeAuthType_Type = DisplayString
_ClcAddNodeAuthType_Object = MibScalar
clcAddNodeAuthType = _ClcAddNodeAuthType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 1, 2, 5),
    _ClcAddNodeAuthType_Type()
)
clcAddNodeAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcAddNodeAuthType.setStatus("current")
_ClcAddNodeAuthList_Type = DisplayString
_ClcAddNodeAuthList_Object = MibScalar
clcAddNodeAuthList = _ClcAddNodeAuthList_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 1, 2, 6),
    _ClcAddNodeAuthList_Type()
)
clcAddNodeAuthList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcAddNodeAuthList.setStatus("current")
_Nodes_ObjectIdentity = ObjectIdentity
nodes = _Nodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2)
)
_NodeStatus_ObjectIdentity = ObjectIdentity
nodeStatus = _NodeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 1)
)
_NodeTable_Object = MibTable
nodeTable = _NodeTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nodeTable.setStatus("current")
_NodeTableEntry_Object = MibTableRow
nodeTableEntry = _NodeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 1, 1, 1)
)
nodeTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "ndsNodeName"),
)
if mibBuilder.loadTexts:
    nodeTableEntry.setStatus("current")
_NdsNodeName_Type = DisplayString
_NdsNodeName_Object = MibTableColumn
ndsNodeName = _NdsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 1, 1, 1, 1),
    _NdsNodeName_Type()
)
ndsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndsNodeName.setStatus("current")
_NdsStatus_Type = DisplayString
_NdsStatus_Object = MibTableColumn
ndsStatus = _NdsStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 1, 1, 1, 2),
    _NdsStatus_Type()
)
ndsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndsStatus.setStatus("current")
_NdsCurrentNodeVotes_Type = Integer32
_NdsCurrentNodeVotes_Object = MibTableColumn
ndsCurrentNodeVotes = _NdsCurrentNodeVotes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 1, 1, 1, 3),
    _NdsCurrentNodeVotes_Type()
)
ndsCurrentNodeVotes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndsCurrentNodeVotes.setStatus("current")
_NodeDeviceTable_Object = MibTable
nodeDeviceTable = _NodeDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    nodeDeviceTable.setStatus("current")
_NodeDeviceTableEntry_Object = MibTableRow
nodeDeviceTableEntry = _NodeDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 1, 2, 1)
)
nodeDeviceTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "ddsNodeName"),
)
if mibBuilder.loadTexts:
    nodeDeviceTableEntry.setStatus("current")
_DdsNodeName_Type = DisplayString
_DdsNodeName_Object = MibTableColumn
ddsNodeName = _DdsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 1, 2, 1, 1),
    _DdsNodeName_Type()
)
ddsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsNodeName.setStatus("current")
_DdsMasteredDeviceGroupList_Type = DisplayString
_DdsMasteredDeviceGroupList_Object = MibTableColumn
ddsMasteredDeviceGroupList = _DdsMasteredDeviceGroupList_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 1, 2, 1, 2),
    _DdsMasteredDeviceGroupList_Type()
)
ddsMasteredDeviceGroupList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsMasteredDeviceGroupList.setStatus("current")
_DdsMasteredRGList_Type = DisplayString
_DdsMasteredRGList_Object = MibTableColumn
ddsMasteredRGList = _DdsMasteredRGList_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 1, 2, 1, 3),
    _DdsMasteredRGList_Type()
)
ddsMasteredRGList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsMasteredRGList.setStatus("current")
_NodeConfiguration_ObjectIdentity = ObjectIdentity
nodeConfiguration = _NodeConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 2)
)
_NodeConfigTable_Object = MibTable
nodeConfigTable = _NodeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nodeConfigTable.setStatus("current")
_NodeConfigTableEntry_Object = MibTableRow
nodeConfigTableEntry = _NodeConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 2, 1, 1)
)
nodeConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "ndcNodeName"),
)
if mibBuilder.loadTexts:
    nodeConfigTableEntry.setStatus("current")
_NdcNodeName_Type = DisplayString
_NdcNodeName_Object = MibTableColumn
ndcNodeName = _NdcNodeName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 2, 1, 1, 1),
    _NdcNodeName_Type()
)
ndcNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndcNodeName.setStatus("current")
_NdcDefaultVotes_Type = Integer32
_NdcDefaultVotes_Object = MibTableColumn
ndcDefaultVotes = _NdcDefaultVotes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 2, 1, 1, 2),
    _NdcDefaultVotes_Type()
)
ndcDefaultVotes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndcDefaultVotes.setStatus("current")
_NdcPrivateNetHostname_Type = DisplayString
_NdcPrivateNetHostname_Object = MibTableColumn
ndcPrivateNetHostname = _NdcPrivateNetHostname_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 2, 1, 1, 3),
    _NdcPrivateNetHostname_Type()
)
ndcPrivateNetHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndcPrivateNetHostname.setStatus("current")
_NdcTransportAdapterList_Type = DisplayString
_NdcTransportAdapterList_Object = MibTableColumn
ndcTransportAdapterList = _NdcTransportAdapterList_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 2, 1, 1, 4),
    _NdcTransportAdapterList_Type()
)
ndcTransportAdapterList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndcTransportAdapterList.setStatus("current")
_NodeDeviceConfigTable_Object = MibTable
nodeDeviceConfigTable = _NodeDeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    nodeDeviceConfigTable.setStatus("current")
_NodeDeviceConfigTableEntry_Object = MibTableRow
nodeDeviceConfigTableEntry = _NodeDeviceConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 2, 2, 1)
)
nodeDeviceConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "ddcNodeName"),
)
if mibBuilder.loadTexts:
    nodeDeviceConfigTableEntry.setStatus("current")
_DdcNodeName_Type = DisplayString
_DdcNodeName_Object = MibTableColumn
ddcNodeName = _DdcNodeName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 2, 2, 1, 1),
    _DdcNodeName_Type()
)
ddcNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddcNodeName.setStatus("current")
_DdcQuorumDeviceList_Type = DisplayString
_DdcQuorumDeviceList_Object = MibTableColumn
ddcQuorumDeviceList = _DdcQuorumDeviceList_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 2, 2, 1, 2),
    _DdcQuorumDeviceList_Type()
)
ddcQuorumDeviceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddcQuorumDeviceList.setStatus("current")
_DdcPossibleMasteredDeviceGroupList_Type = DisplayString
_DdcPossibleMasteredDeviceGroupList_Object = MibTableColumn
ddcPossibleMasteredDeviceGroupList = _DdcPossibleMasteredDeviceGroupList_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 2, 2, 1, 3),
    _DdcPossibleMasteredDeviceGroupList_Type()
)
ddcPossibleMasteredDeviceGroupList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddcPossibleMasteredDeviceGroupList.setStatus("current")
_DdcPossibleMasteredRGList_Type = DisplayString
_DdcPossibleMasteredRGList_Object = MibTableColumn
ddcPossibleMasteredRGList = _DdcPossibleMasteredRGList_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 2, 2, 2, 1, 4),
    _DdcPossibleMasteredRGList_Type()
)
ddcPossibleMasteredRGList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddcPossibleMasteredRGList.setStatus("current")
_DeviceGroups_ObjectIdentity = ObjectIdentity
deviceGroups = _DeviceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3)
)
_DeviceGroupsStatus_ObjectIdentity = ObjectIdentity
deviceGroupsStatus = _DeviceGroupsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 1)
)
_DeviceGroupTable_Object = MibTable
deviceGroupTable = _DeviceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    deviceGroupTable.setStatus("current")
_DeviceGroupTableEntry_Object = MibTableRow
deviceGroupTableEntry = _DeviceGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 1, 1, 1)
)
deviceGroupTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "dgsDeviceGroupName"),
)
if mibBuilder.loadTexts:
    deviceGroupTableEntry.setStatus("current")
_DgsDeviceGroupName_Type = DisplayString
_DgsDeviceGroupName_Object = MibTableColumn
dgsDeviceGroupName = _DgsDeviceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 1, 1, 1, 1),
    _DgsDeviceGroupName_Type()
)
dgsDeviceGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgsDeviceGroupName.setStatus("current")
_DgsDeviceGroupStatus_Type = DisplayString
_DgsDeviceGroupStatus_Object = MibTableColumn
dgsDeviceGroupStatus = _DgsDeviceGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 1, 1, 1, 2),
    _DgsDeviceGroupStatus_Type()
)
dgsDeviceGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgsDeviceGroupStatus.setStatus("current")
_DgsDeviceGroupPrimaryList_Type = DisplayString
_DgsDeviceGroupPrimaryList_Object = MibTableColumn
dgsDeviceGroupPrimaryList = _DgsDeviceGroupPrimaryList_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 1, 1, 1, 3),
    _DgsDeviceGroupPrimaryList_Type()
)
dgsDeviceGroupPrimaryList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgsDeviceGroupPrimaryList.setStatus("current")
_ReplicaTable_Object = MibTable
replicaTable = _ReplicaTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    replicaTable.setStatus("current")
_ReplicaTableEntry_Object = MibTableRow
replicaTableEntry = _ReplicaTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 1, 2, 1)
)
replicaTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "rpsDeviceGroupName"),
    (0, "SUN-CLUSTER-MIB", "rpsNodeName"),
)
if mibBuilder.loadTexts:
    replicaTableEntry.setStatus("current")
_RpsDeviceGroupName_Type = DisplayString
_RpsDeviceGroupName_Object = MibTableColumn
rpsDeviceGroupName = _RpsDeviceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 1, 2, 1, 1),
    _RpsDeviceGroupName_Type()
)
rpsDeviceGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpsDeviceGroupName.setStatus("current")
_RpsNodeName_Type = DisplayString
_RpsNodeName_Object = MibTableColumn
rpsNodeName = _RpsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 1, 2, 1, 2),
    _RpsNodeName_Type()
)
rpsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpsNodeName.setStatus("current")
_RpsStatus_Type = DisplayString
_RpsStatus_Object = MibTableColumn
rpsStatus = _RpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 1, 2, 1, 3),
    _RpsStatus_Type()
)
rpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpsStatus.setStatus("current")
_DeviceGroupsConfiguration_ObjectIdentity = ObjectIdentity
deviceGroupsConfiguration = _DeviceGroupsConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 2)
)
_DeviceGroupConfigTable_Object = MibTable
deviceGroupConfigTable = _DeviceGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    deviceGroupConfigTable.setStatus("current")
_DeviceGroupConfigTableEntry_Object = MibTableRow
deviceGroupConfigTableEntry = _DeviceGroupConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 2, 1, 1)
)
deviceGroupConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "dgcDeviceGroupName"),
)
if mibBuilder.loadTexts:
    deviceGroupConfigTableEntry.setStatus("current")
_DgcDeviceGroupName_Type = DisplayString
_DgcDeviceGroupName_Object = MibTableColumn
dgcDeviceGroupName = _DgcDeviceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 2, 1, 1, 1),
    _DgcDeviceGroupName_Type()
)
dgcDeviceGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgcDeviceGroupName.setStatus("current")
_DgcServiceType_Type = DisplayString
_DgcServiceType_Object = MibTableColumn
dgcServiceType = _DgcServiceType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 2, 1, 1, 2),
    _DgcServiceType_Type()
)
dgcServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgcServiceType.setStatus("current")
_DgcFailback_Type = DisplayString
_DgcFailback_Object = MibTableColumn
dgcFailback = _DgcFailback_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 2, 1, 1, 3),
    _DgcFailback_Type()
)
dgcFailback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgcFailback.setStatus("current")
_DgcNodeList_Type = DisplayString
_DgcNodeList_Object = MibTableColumn
dgcNodeList = _DgcNodeList_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 2, 1, 1, 4),
    _DgcNodeList_Type()
)
dgcNodeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgcNodeList.setStatus("current")
_DgcNodeOrder_Type = DisplayString
_DgcNodeOrder_Object = MibTableColumn
dgcNodeOrder = _DgcNodeOrder_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 2, 1, 1, 5),
    _DgcNodeOrder_Type()
)
dgcNodeOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgcNodeOrder.setStatus("current")
_DgcDeviceList_Type = DisplayString
_DgcDeviceList_Object = MibTableColumn
dgcDeviceList = _DgcDeviceList_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 3, 2, 1, 1, 6),
    _DgcDeviceList_Type()
)
dgcDeviceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dgcDeviceList.setStatus("current")
_QuorumDevices_ObjectIdentity = ObjectIdentity
quorumDevices = _QuorumDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4)
)
_QuorumDevicesStatus_ObjectIdentity = ObjectIdentity
quorumDevicesStatus = _QuorumDevicesStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 1)
)
_QuorumDeviceTable_Object = MibTable
quorumDeviceTable = _QuorumDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    quorumDeviceTable.setStatus("current")
_QuorumDeviceTableEntry_Object = MibTableRow
quorumDeviceTableEntry = _QuorumDeviceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 1, 1, 1)
)
quorumDeviceTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "qdsQuorumDeviceName"),
)
if mibBuilder.loadTexts:
    quorumDeviceTableEntry.setStatus("current")
_QdsQuorumDeviceName_Type = DisplayString
_QdsQuorumDeviceName_Object = MibTableColumn
qdsQuorumDeviceName = _QdsQuorumDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 1, 1, 1, 1),
    _QdsQuorumDeviceName_Type()
)
qdsQuorumDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdsQuorumDeviceName.setStatus("current")
_QdsStatus_Type = DisplayString
_QdsStatus_Object = MibTableColumn
qdsStatus = _QdsStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 1, 1, 1, 2),
    _QdsStatus_Type()
)
qdsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdsStatus.setStatus("current")
_QdsCurrentVotes_Type = Integer32
_QdsCurrentVotes_Object = MibTableColumn
qdsCurrentVotes = _QdsCurrentVotes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 1, 1, 1, 3),
    _QdsCurrentVotes_Type()
)
qdsCurrentVotes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdsCurrentVotes.setStatus("current")
_QdsOwnerNode_Type = DisplayString
_QdsOwnerNode_Object = MibTableColumn
qdsOwnerNode = _QdsOwnerNode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 1, 1, 1, 4),
    _QdsOwnerNode_Type()
)
qdsOwnerNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdsOwnerNode.setStatus("current")
_QuorumDevicesConfiguration_ObjectIdentity = ObjectIdentity
quorumDevicesConfiguration = _QuorumDevicesConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 2)
)
_QuorumDeviceConfigTable_Object = MibTable
quorumDeviceConfigTable = _QuorumDeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    quorumDeviceConfigTable.setStatus("current")
_QuorumDeviceConfigTableEntry_Object = MibTableRow
quorumDeviceConfigTableEntry = _QuorumDeviceConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 2, 1, 1)
)
quorumDeviceConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "qdcQuorumDeviceName"),
)
if mibBuilder.loadTexts:
    quorumDeviceConfigTableEntry.setStatus("current")
_QdcQuorumDeviceName_Type = DisplayString
_QdcQuorumDeviceName_Object = MibTableColumn
qdcQuorumDeviceName = _QdcQuorumDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 2, 1, 1, 1),
    _QdcQuorumDeviceName_Type()
)
qdcQuorumDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdcQuorumDeviceName.setStatus("current")
_QdcQuorumDevicePath_Type = DisplayString
_QdcQuorumDevicePath_Object = MibTableColumn
qdcQuorumDevicePath = _QdcQuorumDevicePath_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 2, 1, 1, 2),
    _QdcQuorumDevicePath_Type()
)
qdcQuorumDevicePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdcQuorumDevicePath.setStatus("current")
_QdcEnabled_Type = DisplayString
_QdcEnabled_Object = MibTableColumn
qdcEnabled = _QdcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 2, 1, 1, 3),
    _QdcEnabled_Type()
)
qdcEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdcEnabled.setStatus("current")
_QdcDefaultVotes_Type = Integer32
_QdcDefaultVotes_Object = MibTableColumn
qdcDefaultVotes = _QdcDefaultVotes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 2, 1, 1, 4),
    _QdcDefaultVotes_Type()
)
qdcDefaultVotes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdcDefaultVotes.setStatus("current")
_QdcPortList_Type = DisplayString
_QdcPortList_Object = MibTableColumn
qdcPortList = _QdcPortList_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 2, 1, 1, 5),
    _QdcPortList_Type()
)
qdcPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qdcPortList.setStatus("current")
_QuorumDevicePortConfigTable_Object = MibTable
quorumDevicePortConfigTable = _QuorumDevicePortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    quorumDevicePortConfigTable.setStatus("current")
_QuorumDevicePortConfigTableEntry_Object = MibTableRow
quorumDevicePortConfigTableEntry = _QuorumDevicePortConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 2, 2, 1)
)
quorumDevicePortConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "qpcQuorumDeviceName"),
    (0, "SUN-CLUSTER-MIB", "qpcQuorumDeviceHost"),
)
if mibBuilder.loadTexts:
    quorumDevicePortConfigTableEntry.setStatus("current")
_QpcQuorumDeviceName_Type = DisplayString
_QpcQuorumDeviceName_Object = MibTableColumn
qpcQuorumDeviceName = _QpcQuorumDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 2, 2, 1, 1),
    _QpcQuorumDeviceName_Type()
)
qpcQuorumDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qpcQuorumDeviceName.setStatus("current")
_QpcQuorumDeviceHost_Type = DisplayString
_QpcQuorumDeviceHost_Object = MibTableColumn
qpcQuorumDeviceHost = _QpcQuorumDeviceHost_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 2, 2, 1, 2),
    _QpcQuorumDeviceHost_Type()
)
qpcQuorumDeviceHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qpcQuorumDeviceHost.setStatus("current")
_QpcEnabled_Type = DisplayString
_QpcEnabled_Object = MibTableColumn
qpcEnabled = _QpcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 4, 2, 2, 1, 3),
    _QpcEnabled_Type()
)
qpcEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qpcEnabled.setStatus("current")
_Transport_ObjectIdentity = ObjectIdentity
transport = _Transport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5)
)
_TransportStatus_ObjectIdentity = ObjectIdentity
transportStatus = _TransportStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 1)
)
_PathTable_Object = MibTable
pathTable = _PathTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    pathTable.setStatus("current")
_PathTableEntry_Object = MibTableRow
pathTableEntry = _PathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 1, 1, 1)
)
pathTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "ptsAdapterName1"),
    (0, "SUN-CLUSTER-MIB", "ptsAdapterName2"),
)
if mibBuilder.loadTexts:
    pathTableEntry.setStatus("current")
_PtsAdapterName1_Type = DisplayString
_PtsAdapterName1_Object = MibTableColumn
ptsAdapterName1 = _PtsAdapterName1_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 1, 1, 1, 1),
    _PtsAdapterName1_Type()
)
ptsAdapterName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptsAdapterName1.setStatus("current")
_PtsAdapterName2_Type = DisplayString
_PtsAdapterName2_Object = MibTableColumn
ptsAdapterName2 = _PtsAdapterName2_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 1, 1, 1, 2),
    _PtsAdapterName2_Type()
)
ptsAdapterName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptsAdapterName2.setStatus("current")
_PtsStatus_Type = DisplayString
_PtsStatus_Object = MibTableColumn
ptsStatus = _PtsStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 1, 1, 1, 3),
    _PtsStatus_Type()
)
ptsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptsStatus.setStatus("current")
_TransportConfiguration_ObjectIdentity = ObjectIdentity
transportConfiguration = _TransportConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2)
)
_AdapterConfigTable_Object = MibTable
adapterConfigTable = _AdapterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    adapterConfigTable.setStatus("current")
_AdapterConfigTableEntry_Object = MibTableRow
adapterConfigTableEntry = _AdapterConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 1, 1)
)
adapterConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "adcNodeName"),
    (0, "SUN-CLUSTER-MIB", "adcAdapterName"),
)
if mibBuilder.loadTexts:
    adapterConfigTableEntry.setStatus("current")
_AdcNodeName_Type = DisplayString
_AdcNodeName_Object = MibTableColumn
adcNodeName = _AdcNodeName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 1, 1, 1),
    _AdcNodeName_Type()
)
adcNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adcNodeName.setStatus("current")
_AdcAdapterName_Type = DisplayString
_AdcAdapterName_Object = MibTableColumn
adcAdapterName = _AdcAdapterName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 1, 1, 2),
    _AdcAdapterName_Type()
)
adcAdapterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adcAdapterName.setStatus("current")
_AdcType_Type = DisplayString
_AdcType_Object = MibTableColumn
adcType = _AdcType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 1, 1, 3),
    _AdcType_Type()
)
adcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adcType.setStatus("current")
_AdcEnabled_Type = DisplayString
_AdcEnabled_Object = MibTableColumn
adcEnabled = _AdcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 1, 1, 4),
    _AdcEnabled_Type()
)
adcEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adcEnabled.setStatus("current")
_JunctionConfigTable_Object = MibTable
junctionConfigTable = _JunctionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    junctionConfigTable.setStatus("current")
_JunctionConfigTableEntry_Object = MibTableRow
junctionConfigTableEntry = _JunctionConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 2, 1)
)
junctionConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "jncJunctionName"),
)
if mibBuilder.loadTexts:
    junctionConfigTableEntry.setStatus("current")
_JncJunctionName_Type = DisplayString
_JncJunctionName_Object = MibTableColumn
jncJunctionName = _JncJunctionName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 2, 1, 1),
    _JncJunctionName_Type()
)
jncJunctionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jncJunctionName.setStatus("current")
_JncType_Type = DisplayString
_JncType_Object = MibTableColumn
jncType = _JncType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 2, 1, 2),
    _JncType_Type()
)
jncType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jncType.setStatus("current")
_JncEnabled_Type = DisplayString
_JncEnabled_Object = MibTableColumn
jncEnabled = _JncEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 2, 1, 3),
    _JncEnabled_Type()
)
jncEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jncEnabled.setStatus("current")
_JncPortList_Type = DisplayString
_JncPortList_Object = MibTableColumn
jncPortList = _JncPortList_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 2, 1, 4),
    _JncPortList_Type()
)
jncPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jncPortList.setStatus("current")
_CableConfigTable_Object = MibTable
cableConfigTable = _CableConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    cableConfigTable.setStatus("current")
_CableConfigTableEntry_Object = MibTableRow
cableConfigTableEntry = _CableConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 3, 1)
)
cableConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "cbcEndType1"),
    (0, "SUN-CLUSTER-MIB", "cbcEndpoint1"),
    (0, "SUN-CLUSTER-MIB", "cbcEndType2"),
    (0, "SUN-CLUSTER-MIB", "cbcEndpoint2"),
)
if mibBuilder.loadTexts:
    cableConfigTableEntry.setStatus("current")
_CbcEndType1_Type = DisplayString
_CbcEndType1_Object = MibTableColumn
cbcEndType1 = _CbcEndType1_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 3, 1, 1),
    _CbcEndType1_Type()
)
cbcEndType1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbcEndType1.setStatus("current")
_CbcEndpoint1_Type = DisplayString
_CbcEndpoint1_Object = MibTableColumn
cbcEndpoint1 = _CbcEndpoint1_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 3, 1, 2),
    _CbcEndpoint1_Type()
)
cbcEndpoint1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbcEndpoint1.setStatus("current")
_CbcEndType2_Type = DisplayString
_CbcEndType2_Object = MibTableColumn
cbcEndType2 = _CbcEndType2_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 3, 1, 3),
    _CbcEndType2_Type()
)
cbcEndType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbcEndType2.setStatus("current")
_CbcEndpoint2_Type = DisplayString
_CbcEndpoint2_Object = MibTableColumn
cbcEndpoint2 = _CbcEndpoint2_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 3, 1, 4),
    _CbcEndpoint2_Type()
)
cbcEndpoint2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbcEndpoint2.setStatus("current")
_CbcEnabled_Type = DisplayString
_CbcEnabled_Object = MibTableColumn
cbcEnabled = _CbcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 5, 2, 3, 1, 5),
    _CbcEnabled_Type()
)
cbcEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbcEnabled.setStatus("current")
_ResourceGroups_ObjectIdentity = ObjectIdentity
resourceGroups = _ResourceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6)
)
_RgStatus_ObjectIdentity = ObjectIdentity
rgStatus = _RgStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1)
)
_FoRgStatusBranch_ObjectIdentity = ObjectIdentity
foRgStatusBranch = _FoRgStatusBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1)
)
_ForgStatusTable_Object = MibTable
forgStatusTable = _ForgStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    forgStatusTable.setStatus("current")
_ForgStatusTableEntry_Object = MibTableRow
forgStatusTableEntry = _ForgStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 1, 1)
)
forgStatusTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "frgName"),
    (0, "SUN-CLUSTER-MIB", "frgPrim"),
)
if mibBuilder.loadTexts:
    forgStatusTableEntry.setStatus("current")
_FrgRowStatus_Type = DisplayString
_FrgRowStatus_Object = MibTableColumn
frgRowStatus = _FrgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 1, 1, 1),
    _FrgRowStatus_Type()
)
frgRowStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frgRowStatus.setStatus("current")
_FrgName_Type = DisplayString
_FrgName_Object = MibTableColumn
frgName = _FrgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 1, 1, 2),
    _FrgName_Type()
)
frgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgName.setStatus("current")
_FrgPrim_Type = DisplayString
_FrgPrim_Object = MibTableColumn
frgPrim = _FrgPrim_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 1, 1, 3),
    _FrgPrim_Type()
)
frgPrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgPrim.setStatus("current")
_FrgPrimStatus_Type = DisplayString
_FrgPrimStatus_Object = MibTableColumn
frgPrimStatus = _FrgPrimStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 1, 1, 4),
    _FrgPrimStatus_Type()
)
frgPrimStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgPrimStatus.setStatus("current")
_FrgState_Type = DisplayString
_FrgState_Object = MibTableColumn
frgState = _FrgState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 1, 1, 5),
    _FrgState_Type()
)
frgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgState.setStatus("current")
_FrsStatusTable_Object = MibTable
frsStatusTable = _FrsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    frsStatusTable.setStatus("current")
_FrsStatusTableEntry_Object = MibTableRow
frsStatusTableEntry = _FrsStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 2, 1)
)
frsStatusTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "frsRgName"),
    (0, "SUN-CLUSTER-MIB", "frsRsName"),
    (0, "SUN-CLUSTER-MIB", "frsRsPrim"),
)
if mibBuilder.loadTexts:
    frsStatusTableEntry.setStatus("current")
_FrsRowstatus_Type = RowStatus
_FrsRowstatus_Object = MibTableColumn
frsRowstatus = _FrsRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 2, 1, 1),
    _FrsRowstatus_Type()
)
frsRowstatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frsRowstatus.setStatus("current")
_FrsRgName_Type = DisplayString
_FrsRgName_Object = MibTableColumn
frsRgName = _FrsRgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 2, 1, 2),
    _FrsRgName_Type()
)
frsRgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsRgName.setStatus("current")
_FrsRsName_Type = DisplayString
_FrsRsName_Object = MibTableColumn
frsRsName = _FrsRsName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 2, 1, 3),
    _FrsRsName_Type()
)
frsRsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsRsName.setStatus("current")
_FrsRsPrim_Type = DisplayString
_FrsRsPrim_Object = MibTableColumn
frsRsPrim = _FrsRsPrim_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 2, 1, 4),
    _FrsRsPrim_Type()
)
frsRsPrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsRsPrim.setStatus("current")
_FrsRsPrimStatus_Type = DisplayString
_FrsRsPrimStatus_Object = MibTableColumn
frsRsPrimStatus = _FrsRsPrimStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 2, 1, 5),
    _FrsRsPrimStatus_Type()
)
frsRsPrimStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsRsPrimStatus.setStatus("current")
_FrsRsFMStatus_Type = DisplayString
_FrsRsFMStatus_Object = MibTableColumn
frsRsFMStatus = _FrsRsFMStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 2, 1, 6),
    _FrsRsFMStatus_Type()
)
frsRsFMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsRsFMStatus.setStatus("current")
_FrsRsRGMState_Type = DisplayString
_FrsRsRGMState_Object = MibTableColumn
frsRsRGMState = _FrsRsRGMState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 1, 2, 1, 7),
    _FrsRsRGMState_Type()
)
frsRsRGMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frsRsRGMState.setStatus("current")
_ScRgStatusBranch_ObjectIdentity = ObjectIdentity
scRgStatusBranch = _ScRgStatusBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2)
)
_ScrgStatusTable_Object = MibTable
scrgStatusTable = _ScrgStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    scrgStatusTable.setStatus("current")
_ScrgStatusTableEntry_Object = MibTableRow
scrgStatusTableEntry = _ScrgStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 1, 1)
)
scrgStatusTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "srgName"),
    (0, "SUN-CLUSTER-MIB", "srgPrim"),
)
if mibBuilder.loadTexts:
    scrgStatusTableEntry.setStatus("current")
_SrgRowstatus_Type = RowStatus
_SrgRowstatus_Object = MibTableColumn
srgRowstatus = _SrgRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 1, 1, 1),
    _SrgRowstatus_Type()
)
srgRowstatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srgRowstatus.setStatus("current")
_SrgName_Type = DisplayString
_SrgName_Object = MibTableColumn
srgName = _SrgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 1, 1, 2),
    _SrgName_Type()
)
srgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgName.setStatus("current")
_SrgPrim_Type = DisplayString
_SrgPrim_Object = MibTableColumn
srgPrim = _SrgPrim_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 1, 1, 3),
    _SrgPrim_Type()
)
srgPrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgPrim.setStatus("current")
_SrgPrimStatus_Type = DisplayString
_SrgPrimStatus_Object = MibTableColumn
srgPrimStatus = _SrgPrimStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 1, 1, 4),
    _SrgPrimStatus_Type()
)
srgPrimStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgPrimStatus.setStatus("current")
_SrgState_Type = DisplayString
_SrgState_Object = MibTableColumn
srgState = _SrgState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 1, 1, 5),
    _SrgState_Type()
)
srgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgState.setStatus("current")
_SrsStatusTable_Object = MibTable
srsStatusTable = _SrsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    srsStatusTable.setStatus("current")
_SrsStatusTableEntry_Object = MibTableRow
srsStatusTableEntry = _SrsStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 2, 1)
)
srsStatusTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "srsRgName"),
    (0, "SUN-CLUSTER-MIB", "srsRsName"),
    (0, "SUN-CLUSTER-MIB", "srsRsPrim"),
)
if mibBuilder.loadTexts:
    srsStatusTableEntry.setStatus("current")
_SrsRowstatus_Type = RowStatus
_SrsRowstatus_Object = MibTableColumn
srsRowstatus = _SrsRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 2, 1, 1),
    _SrsRowstatus_Type()
)
srsRowstatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srsRowstatus.setStatus("current")
_SrsRgName_Type = DisplayString
_SrsRgName_Object = MibTableColumn
srsRgName = _SrsRgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 2, 1, 2),
    _SrsRgName_Type()
)
srsRgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsRgName.setStatus("current")
_SrsRsName_Type = DisplayString
_SrsRsName_Object = MibTableColumn
srsRsName = _SrsRsName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 2, 1, 3),
    _SrsRsName_Type()
)
srsRsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsRsName.setStatus("current")
_SrsRsPrim_Type = DisplayString
_SrsRsPrim_Object = MibTableColumn
srsRsPrim = _SrsRsPrim_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 2, 1, 4),
    _SrsRsPrim_Type()
)
srsRsPrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsRsPrim.setStatus("current")
_SrsRsPrimStatus_Type = DisplayString
_SrsRsPrimStatus_Object = MibTableColumn
srsRsPrimStatus = _SrsRsPrimStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 2, 1, 5),
    _SrsRsPrimStatus_Type()
)
srsRsPrimStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsRsPrimStatus.setStatus("current")
_SrsRsFMStatus_Type = DisplayString
_SrsRsFMStatus_Object = MibTableColumn
srsRsFMStatus = _SrsRsFMStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 2, 1, 6),
    _SrsRsFMStatus_Type()
)
srsRsFMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsRsFMStatus.setStatus("current")
_SrsRsRGMState_Type = DisplayString
_SrsRsRGMState_Object = MibTableColumn
srsRsRGMState = _SrsRsRGMState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 1, 2, 2, 1, 7),
    _SrsRsRGMState_Type()
)
srsRsRGMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srsRsRGMState.setStatus("current")
_RgConfiguration_ObjectIdentity = ObjectIdentity
rgConfiguration = _RgConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2)
)
_FoRgConfigBranch_ObjectIdentity = ObjectIdentity
foRgConfigBranch = _FoRgConfigBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1)
)
_ForgConfigInfo_ObjectIdentity = ObjectIdentity
forgConfigInfo = _ForgConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3)
)
_ForgConfigTable_Object = MibTable
forgConfigTable = _ForgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    forgConfigTable.setStatus("current")
_ForgConfigTableEntry_Object = MibTableRow
forgConfigTableEntry = _ForgConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3, 1, 1)
)
forgConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "frgcRgName"),
)
if mibBuilder.loadTexts:
    forgConfigTableEntry.setStatus("current")
_FrgcRowstatus_Type = RowStatus
_FrgcRowstatus_Object = MibTableColumn
frgcRowstatus = _FrgcRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3, 1, 1, 1),
    _FrgcRowstatus_Type()
)
frgcRowstatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frgcRowstatus.setStatus("current")
_FrgcRgName_Type = DisplayString
_FrgcRgName_Object = MibTableColumn
frgcRgName = _FrgcRgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3, 1, 1, 2),
    _FrgcRgName_Type()
)
frgcRgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgcRgName.setStatus("current")
_FrgcRgPrimaries_Type = DisplayString
_FrgcRgPrimaries_Object = MibTableColumn
frgcRgPrimaries = _FrgcRgPrimaries_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3, 1, 1, 3),
    _FrgcRgPrimaries_Type()
)
frgcRgPrimaries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgcRgPrimaries.setStatus("current")
_FrgcRgDesc_Type = DisplayString
_FrgcRgDesc_Object = MibTableColumn
frgcRgDesc = _FrgcRgDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3, 1, 1, 4),
    _FrgcRgDesc_Type()
)
frgcRgDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgcRgDesc.setStatus("current")
_FrgcRsList_Type = DisplayString
_FrgcRsList_Object = MibTableColumn
frgcRsList = _FrgcRsList_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3, 1, 1, 5),
    _FrgcRsList_Type()
)
frgcRsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgcRsList.setStatus("current")
_FrgcRgMaxPrim_Type = Integer32
_FrgcRgMaxPrim_Object = MibTableColumn
frgcRgMaxPrim = _FrgcRgMaxPrim_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3, 1, 1, 6),
    _FrgcRgMaxPrim_Type()
)
frgcRgMaxPrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgcRgMaxPrim.setStatus("current")
_FrgcRgDesPrim_Type = Integer32
_FrgcRgDesPrim_Object = MibTableColumn
frgcRgDesPrim = _FrgcRgDesPrim_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3, 1, 1, 7),
    _FrgcRgDesPrim_Type()
)
frgcRgDesPrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgcRgDesPrim.setStatus("current")
_FrgcRgFailbackFlag_Type = DisplayString
_FrgcRgFailbackFlag_Object = MibTableColumn
frgcRgFailbackFlag = _FrgcRgFailbackFlag_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3, 1, 1, 8),
    _FrgcRgFailbackFlag_Type()
)
frgcRgFailbackFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgcRgFailbackFlag.setStatus("current")
_FrgcNetDepend_Type = DisplayString
_FrgcNetDepend_Object = MibTableColumn
frgcNetDepend = _FrgcNetDepend_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3, 1, 1, 9),
    _FrgcNetDepend_Type()
)
frgcNetDepend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgcNetDepend.setStatus("current")
_FrgcRgDepend_Type = DisplayString
_FrgcRgDepend_Object = MibTableColumn
frgcRgDepend = _FrgcRgDepend_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3, 1, 1, 10),
    _FrgcRgDepend_Type()
)
frgcRgDepend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgcRgDepend.setStatus("current")
_FrgcRgGlobRUsed_Type = DisplayString
_FrgcRgGlobRUsed_Object = MibTableColumn
frgcRgGlobRUsed = _FrgcRgGlobRUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3, 1, 1, 11),
    _FrgcRgGlobRUsed_Type()
)
frgcRgGlobRUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgcRgGlobRUsed.setStatus("current")
_FrgcRgPathPrefix_Type = DisplayString
_FrgcRgPathPrefix_Object = MibTableColumn
frgcRgPathPrefix = _FrgcRgPathPrefix_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 3, 1, 1, 12),
    _FrgcRgPathPrefix_Type()
)
frgcRgPathPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frgcRgPathPrefix.setStatus("current")
_FoRsConfigBranch_ObjectIdentity = ObjectIdentity
foRsConfigBranch = _FoRsConfigBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4)
)
_FoRsConfigGen_ObjectIdentity = ObjectIdentity
foRsConfigGen = _FoRsConfigGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 1)
)
_ForsGenConfigTable_Object = MibTable
forsGenConfigTable = _ForsGenConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    forsGenConfigTable.setStatus("current")
_ForsGenConfigTableEntry_Object = MibTableRow
forsGenConfigTableEntry = _ForsGenConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 1, 1, 1)
)
forsGenConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "frcRgName"),
    (0, "SUN-CLUSTER-MIB", "frcRsName"),
)
if mibBuilder.loadTexts:
    forsGenConfigTableEntry.setStatus("current")
_FrcRowstatus_Type = RowStatus
_FrcRowstatus_Object = MibTableColumn
frcRowstatus = _FrcRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 1, 1, 1, 1),
    _FrcRowstatus_Type()
)
frcRowstatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frcRowstatus.setStatus("current")
_FrcRgName_Type = DisplayString
_FrcRgName_Object = MibTableColumn
frcRgName = _FrcRgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 1, 1, 1, 2),
    _FrcRgName_Type()
)
frcRgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frcRgName.setStatus("current")
_FrcRsName_Type = DisplayString
_FrcRsName_Object = MibTableColumn
frcRsName = _FrcRsName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 1, 1, 1, 3),
    _FrcRsName_Type()
)
frcRsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frcRsName.setStatus("current")
_FrcRsType_Type = DisplayString
_FrcRsType_Object = MibTableColumn
frcRsType = _FrcRsType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 1, 1, 1, 4),
    _FrcRsType_Type()
)
frcRsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frcRsType.setStatus("current")
_FrcRsEnabled_Type = DisplayString
_FrcRsEnabled_Object = MibTableColumn
frcRsEnabled = _FrcRsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 1, 1, 1, 5),
    _FrcRsEnabled_Type()
)
frcRsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frcRsEnabled.setStatus("current")
_FrcRsMonitored_Type = DisplayString
_FrcRsMonitored_Object = MibTableColumn
frcRsMonitored = _FrcRsMonitored_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 1, 1, 1, 6),
    _FrcRsMonitored_Type()
)
frcRsMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frcRsMonitored.setStatus("current")
_FrcRsStrongDepend_Type = DisplayString
_FrcRsStrongDepend_Object = MibTableColumn
frcRsStrongDepend = _FrcRsStrongDepend_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 1, 1, 1, 7),
    _FrcRsStrongDepend_Type()
)
frcRsStrongDepend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frcRsStrongDepend.setStatus("current")
_FrcRsWeakDepend_Type = DisplayString
_FrcRsWeakDepend_Object = MibTableColumn
frcRsWeakDepend = _FrcRsWeakDepend_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 1, 1, 1, 8),
    _FrcRsWeakDepend_Type()
)
frcRsWeakDepend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frcRsWeakDepend.setStatus("current")
_FoRsConfigStandProps_ObjectIdentity = ObjectIdentity
foRsConfigStandProps = _FoRsConfigStandProps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 2)
)
_ForsComPropConfigTable_Object = MibTable
forsComPropConfigTable = _ForsComPropConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    forsComPropConfigTable.setStatus("current")
_ForsComPropConfigTableEntry_Object = MibTableRow
forsComPropConfigTableEntry = _ForsComPropConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 2, 1, 1)
)
forsComPropConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "frstRgName"),
    (0, "SUN-CLUSTER-MIB", "frstRsName"),
    (0, "SUN-CLUSTER-MIB", "frstRsPropName"),
)
if mibBuilder.loadTexts:
    forsComPropConfigTableEntry.setStatus("current")
_FrstRowstatus_Type = RowStatus
_FrstRowstatus_Object = MibTableColumn
frstRowstatus = _FrstRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 2, 1, 1, 1),
    _FrstRowstatus_Type()
)
frstRowstatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frstRowstatus.setStatus("current")
_FrstRgName_Type = DisplayString
_FrstRgName_Object = MibTableColumn
frstRgName = _FrstRgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 2, 1, 1, 2),
    _FrstRgName_Type()
)
frstRgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frstRgName.setStatus("current")
_FrstRsName_Type = DisplayString
_FrstRsName_Object = MibTableColumn
frstRsName = _FrstRsName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 2, 1, 1, 3),
    _FrstRsName_Type()
)
frstRsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frstRsName.setStatus("current")
_FrstRsPropName_Type = DisplayString
_FrstRsPropName_Object = MibTableColumn
frstRsPropName = _FrstRsPropName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 2, 1, 1, 4),
    _FrstRsPropName_Type()
)
frstRsPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frstRsPropName.setStatus("current")
_FrstRsPropValue_Type = DisplayString
_FrstRsPropValue_Object = MibTableColumn
frstRsPropValue = _FrstRsPropValue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 2, 1, 1, 5),
    _FrstRsPropValue_Type()
)
frstRsPropValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frstRsPropValue.setStatus("current")
_FrstRsPropDesc_Type = DisplayString
_FrstRsPropDesc_Object = MibTableColumn
frstRsPropDesc = _FrstRsPropDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 2, 1, 1, 6),
    _FrstRsPropDesc_Type()
)
frstRsPropDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frstRsPropDesc.setStatus("current")
_FoRsConfigExtProps_ObjectIdentity = ObjectIdentity
foRsConfigExtProps = _FoRsConfigExtProps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 3)
)
_ForsExtPropConfigTable_Object = MibTable
forsExtPropConfigTable = _ForsExtPropConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    forsExtPropConfigTable.setStatus("current")
_ForsExtPropConfigTableEntry_Object = MibTableRow
forsExtPropConfigTableEntry = _ForsExtPropConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 3, 1, 1)
)
forsExtPropConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "frexRgName"),
    (0, "SUN-CLUSTER-MIB", "frexRsName"),
    (0, "SUN-CLUSTER-MIB", "frexRsPropName"),
)
if mibBuilder.loadTexts:
    forsExtPropConfigTableEntry.setStatus("current")
_FrexRowstatus_Type = RowStatus
_FrexRowstatus_Object = MibTableColumn
frexRowstatus = _FrexRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 3, 1, 1, 1),
    _FrexRowstatus_Type()
)
frexRowstatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frexRowstatus.setStatus("current")
_FrexRgName_Type = DisplayString
_FrexRgName_Object = MibTableColumn
frexRgName = _FrexRgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 3, 1, 1, 2),
    _FrexRgName_Type()
)
frexRgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frexRgName.setStatus("current")
_FrexRsName_Type = DisplayString
_FrexRsName_Object = MibTableColumn
frexRsName = _FrexRsName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 3, 1, 1, 3),
    _FrexRsName_Type()
)
frexRsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frexRsName.setStatus("current")
_FrexRsPropName_Type = DisplayString
_FrexRsPropName_Object = MibTableColumn
frexRsPropName = _FrexRsPropName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 3, 1, 1, 4),
    _FrexRsPropName_Type()
)
frexRsPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frexRsPropName.setStatus("current")
_FrexRsPropValue_Type = DisplayString
_FrexRsPropValue_Object = MibTableColumn
frexRsPropValue = _FrexRsPropValue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 3, 1, 1, 5),
    _FrexRsPropValue_Type()
)
frexRsPropValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frexRsPropValue.setStatus("current")
_FrexRsPropDesc_Type = DisplayString
_FrexRsPropDesc_Object = MibTableColumn
frexRsPropDesc = _FrexRsPropDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 3, 1, 1, 6),
    _FrexRsPropDesc_Type()
)
frexRsPropDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frexRsPropDesc.setStatus("current")
_FoRsConfigMethods_ObjectIdentity = ObjectIdentity
foRsConfigMethods = _FoRsConfigMethods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 4)
)
_ForsTimeoutConfigTable_Object = MibTable
forsTimeoutConfigTable = _ForsTimeoutConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    forsTimeoutConfigTable.setStatus("current")
_ForsTimeoutConfigTableEntry_Object = MibTableRow
forsTimeoutConfigTableEntry = _ForsTimeoutConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 4, 1, 1)
)
forsTimeoutConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "frtoRgName"),
    (0, "SUN-CLUSTER-MIB", "frtoRsName"),
    (0, "SUN-CLUSTER-MIB", "frtoRsPropName"),
)
if mibBuilder.loadTexts:
    forsTimeoutConfigTableEntry.setStatus("current")
_FrtoRowstatus_Type = RowStatus
_FrtoRowstatus_Object = MibTableColumn
frtoRowstatus = _FrtoRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 4, 1, 1, 1),
    _FrtoRowstatus_Type()
)
frtoRowstatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frtoRowstatus.setStatus("current")
_FrtoRgName_Type = DisplayString
_FrtoRgName_Object = MibTableColumn
frtoRgName = _FrtoRgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 4, 1, 1, 2),
    _FrtoRgName_Type()
)
frtoRgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frtoRgName.setStatus("current")
_FrtoRsName_Type = DisplayString
_FrtoRsName_Object = MibTableColumn
frtoRsName = _FrtoRsName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 4, 1, 1, 3),
    _FrtoRsName_Type()
)
frtoRsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frtoRsName.setStatus("current")
_FrtoRsPropName_Type = DisplayString
_FrtoRsPropName_Object = MibTableColumn
frtoRsPropName = _FrtoRsPropName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 4, 1, 1, 4),
    _FrtoRsPropName_Type()
)
frtoRsPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frtoRsPropName.setStatus("current")
_FrtoRsPropValue_Type = DisplayString
_FrtoRsPropValue_Object = MibTableColumn
frtoRsPropValue = _FrtoRsPropValue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 4, 1, 1, 5),
    _FrtoRsPropValue_Type()
)
frtoRsPropValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frtoRsPropValue.setStatus("current")
_FrtoRsPropDesc_Type = DisplayString
_FrtoRsPropDesc_Object = MibTableColumn
frtoRsPropDesc = _FrtoRsPropDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 1, 4, 4, 1, 1, 6),
    _FrtoRsPropDesc_Type()
)
frtoRsPropDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frtoRsPropDesc.setStatus("current")
_ScRgConfigBranch_ObjectIdentity = ObjectIdentity
scRgConfigBranch = _ScRgConfigBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2)
)
_ScrgConfigInfo_ObjectIdentity = ObjectIdentity
scrgConfigInfo = _ScrgConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3)
)
_ScrgConfigTable_Object = MibTable
scrgConfigTable = _ScrgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    scrgConfigTable.setStatus("current")
_ScrgConfigTableEntry_Object = MibTableRow
scrgConfigTableEntry = _ScrgConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3, 1, 1)
)
scrgConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "srgcRgName"),
)
if mibBuilder.loadTexts:
    scrgConfigTableEntry.setStatus("current")
_SrgcRowstatus_Type = RowStatus
_SrgcRowstatus_Object = MibTableColumn
srgcRowstatus = _SrgcRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3, 1, 1, 1),
    _SrgcRowstatus_Type()
)
srgcRowstatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srgcRowstatus.setStatus("current")
_SrgcRgName_Type = DisplayString
_SrgcRgName_Object = MibTableColumn
srgcRgName = _SrgcRgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3, 1, 1, 2),
    _SrgcRgName_Type()
)
srgcRgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgcRgName.setStatus("current")
_SrgcRgPrimaries_Type = DisplayString
_SrgcRgPrimaries_Object = MibTableColumn
srgcRgPrimaries = _SrgcRgPrimaries_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3, 1, 1, 3),
    _SrgcRgPrimaries_Type()
)
srgcRgPrimaries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgcRgPrimaries.setStatus("current")
_SrgcRgDesc_Type = DisplayString
_SrgcRgDesc_Object = MibTableColumn
srgcRgDesc = _SrgcRgDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3, 1, 1, 4),
    _SrgcRgDesc_Type()
)
srgcRgDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgcRgDesc.setStatus("current")
_SrgcRsList_Type = DisplayString
_SrgcRsList_Object = MibTableColumn
srgcRsList = _SrgcRsList_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3, 1, 1, 5),
    _SrgcRsList_Type()
)
srgcRsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgcRsList.setStatus("current")
_SrgcRgMaxPrim_Type = Integer32
_SrgcRgMaxPrim_Object = MibTableColumn
srgcRgMaxPrim = _SrgcRgMaxPrim_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3, 1, 1, 6),
    _SrgcRgMaxPrim_Type()
)
srgcRgMaxPrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgcRgMaxPrim.setStatus("current")
_SrgcRgDesPrim_Type = Integer32
_SrgcRgDesPrim_Object = MibTableColumn
srgcRgDesPrim = _SrgcRgDesPrim_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3, 1, 1, 7),
    _SrgcRgDesPrim_Type()
)
srgcRgDesPrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgcRgDesPrim.setStatus("current")
_SrgcRgFailbackFlag_Type = DisplayString
_SrgcRgFailbackFlag_Object = MibTableColumn
srgcRgFailbackFlag = _SrgcRgFailbackFlag_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3, 1, 1, 8),
    _SrgcRgFailbackFlag_Type()
)
srgcRgFailbackFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgcRgFailbackFlag.setStatus("current")
_SrgcNetDepend_Type = DisplayString
_SrgcNetDepend_Object = MibTableColumn
srgcNetDepend = _SrgcNetDepend_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3, 1, 1, 9),
    _SrgcNetDepend_Type()
)
srgcNetDepend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgcNetDepend.setStatus("current")
_SrgcRgDepend_Type = DisplayString
_SrgcRgDepend_Object = MibTableColumn
srgcRgDepend = _SrgcRgDepend_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3, 1, 1, 10),
    _SrgcRgDepend_Type()
)
srgcRgDepend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgcRgDepend.setStatus("current")
_SrgcRgGlobRUsed_Type = DisplayString
_SrgcRgGlobRUsed_Object = MibTableColumn
srgcRgGlobRUsed = _SrgcRgGlobRUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3, 1, 1, 11),
    _SrgcRgGlobRUsed_Type()
)
srgcRgGlobRUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgcRgGlobRUsed.setStatus("current")
_SrgcRgPathPrefix_Type = DisplayString
_SrgcRgPathPrefix_Object = MibTableColumn
srgcRgPathPrefix = _SrgcRgPathPrefix_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 3, 1, 1, 12),
    _SrgcRgPathPrefix_Type()
)
srgcRgPathPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srgcRgPathPrefix.setStatus("current")
_ScRsConfigBranch_ObjectIdentity = ObjectIdentity
scRsConfigBranch = _ScRsConfigBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4)
)
_ScRsConfigGen_ObjectIdentity = ObjectIdentity
scRsConfigGen = _ScRsConfigGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 1)
)
_ScrsGenConfigTable_Object = MibTable
scrsGenConfigTable = _ScrsGenConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    scrsGenConfigTable.setStatus("current")
_ScrsGenConfigTableEntry_Object = MibTableRow
scrsGenConfigTableEntry = _ScrsGenConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 1, 1, 1)
)
scrsGenConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "srcRgName"),
    (0, "SUN-CLUSTER-MIB", "srcRsName"),
)
if mibBuilder.loadTexts:
    scrsGenConfigTableEntry.setStatus("current")
_SrcRowstatus_Type = RowStatus
_SrcRowstatus_Object = MibTableColumn
srcRowstatus = _SrcRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 1, 1, 1, 1),
    _SrcRowstatus_Type()
)
srcRowstatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srcRowstatus.setStatus("current")
_SrcRgName_Type = DisplayString
_SrcRgName_Object = MibTableColumn
srcRgName = _SrcRgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 1, 1, 1, 2),
    _SrcRgName_Type()
)
srcRgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcRgName.setStatus("current")
_SrcRsName_Type = DisplayString
_SrcRsName_Object = MibTableColumn
srcRsName = _SrcRsName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 1, 1, 1, 3),
    _SrcRsName_Type()
)
srcRsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcRsName.setStatus("current")
_SrcRsType_Type = DisplayString
_SrcRsType_Object = MibTableColumn
srcRsType = _SrcRsType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 1, 1, 1, 4),
    _SrcRsType_Type()
)
srcRsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcRsType.setStatus("current")
_SrcRsEnabled_Type = DisplayString
_SrcRsEnabled_Object = MibTableColumn
srcRsEnabled = _SrcRsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 1, 1, 1, 5),
    _SrcRsEnabled_Type()
)
srcRsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcRsEnabled.setStatus("current")
_SrcRsMonitored_Type = Integer32
_SrcRsMonitored_Object = MibTableColumn
srcRsMonitored = _SrcRsMonitored_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 1, 1, 1, 6),
    _SrcRsMonitored_Type()
)
srcRsMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcRsMonitored.setStatus("current")
_SrcRsStrongDepend_Type = DisplayString
_SrcRsStrongDepend_Object = MibTableColumn
srcRsStrongDepend = _SrcRsStrongDepend_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 1, 1, 1, 7),
    _SrcRsStrongDepend_Type()
)
srcRsStrongDepend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcRsStrongDepend.setStatus("current")
_SrcRsWeakDepend_Type = DisplayString
_SrcRsWeakDepend_Object = MibTableColumn
srcRsWeakDepend = _SrcRsWeakDepend_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 1, 1, 1, 8),
    _SrcRsWeakDepend_Type()
)
srcRsWeakDepend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcRsWeakDepend.setStatus("current")
_ScRsConfigStandProps_ObjectIdentity = ObjectIdentity
scRsConfigStandProps = _ScRsConfigStandProps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 2)
)
_ScrsComPropConfigTable_Object = MibTable
scrsComPropConfigTable = _ScrsComPropConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    scrsComPropConfigTable.setStatus("current")
_ScrsComPropConfigTableEntry_Object = MibTableRow
scrsComPropConfigTableEntry = _ScrsComPropConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 2, 1, 1)
)
scrsComPropConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "srstRgName"),
    (0, "SUN-CLUSTER-MIB", "srstRsName"),
    (0, "SUN-CLUSTER-MIB", "srstRsPropName"),
)
if mibBuilder.loadTexts:
    scrsComPropConfigTableEntry.setStatus("current")
_SrstRowstatus_Type = RowStatus
_SrstRowstatus_Object = MibTableColumn
srstRowstatus = _SrstRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 2, 1, 1, 1),
    _SrstRowstatus_Type()
)
srstRowstatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srstRowstatus.setStatus("current")
_SrstRgName_Type = DisplayString
_SrstRgName_Object = MibTableColumn
srstRgName = _SrstRgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 2, 1, 1, 2),
    _SrstRgName_Type()
)
srstRgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srstRgName.setStatus("current")
_SrstRsName_Type = DisplayString
_SrstRsName_Object = MibTableColumn
srstRsName = _SrstRsName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 2, 1, 1, 3),
    _SrstRsName_Type()
)
srstRsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srstRsName.setStatus("current")
_SrstRsPropName_Type = DisplayString
_SrstRsPropName_Object = MibTableColumn
srstRsPropName = _SrstRsPropName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 2, 1, 1, 4),
    _SrstRsPropName_Type()
)
srstRsPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srstRsPropName.setStatus("current")
_SrstRsPropValue_Type = DisplayString
_SrstRsPropValue_Object = MibTableColumn
srstRsPropValue = _SrstRsPropValue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 2, 1, 1, 5),
    _SrstRsPropValue_Type()
)
srstRsPropValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srstRsPropValue.setStatus("current")
_SrstRsPropDesc_Type = DisplayString
_SrstRsPropDesc_Object = MibTableColumn
srstRsPropDesc = _SrstRsPropDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 2, 1, 1, 6),
    _SrstRsPropDesc_Type()
)
srstRsPropDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srstRsPropDesc.setStatus("current")
_ScRsConfigExtProps_ObjectIdentity = ObjectIdentity
scRsConfigExtProps = _ScRsConfigExtProps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 3)
)
_ScrsExtPropConfigTable_Object = MibTable
scrsExtPropConfigTable = _ScrsExtPropConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    scrsExtPropConfigTable.setStatus("current")
_ScrsExtPropConfigTableEntry_Object = MibTableRow
scrsExtPropConfigTableEntry = _ScrsExtPropConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 3, 1, 1)
)
scrsExtPropConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "srexRgName"),
    (0, "SUN-CLUSTER-MIB", "srexRsName"),
    (0, "SUN-CLUSTER-MIB", "frexRsPropName"),
)
if mibBuilder.loadTexts:
    scrsExtPropConfigTableEntry.setStatus("current")
_SrexRowstatus_Type = RowStatus
_SrexRowstatus_Object = MibTableColumn
srexRowstatus = _SrexRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 3, 1, 1, 1),
    _SrexRowstatus_Type()
)
srexRowstatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srexRowstatus.setStatus("current")
_SrexRgName_Type = DisplayString
_SrexRgName_Object = MibTableColumn
srexRgName = _SrexRgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 3, 1, 1, 2),
    _SrexRgName_Type()
)
srexRgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srexRgName.setStatus("current")
_SrexRsName_Type = DisplayString
_SrexRsName_Object = MibTableColumn
srexRsName = _SrexRsName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 3, 1, 1, 3),
    _SrexRsName_Type()
)
srexRsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srexRsName.setStatus("current")
_SrexRsPropName_Type = DisplayString
_SrexRsPropName_Object = MibTableColumn
srexRsPropName = _SrexRsPropName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 3, 1, 1, 4),
    _SrexRsPropName_Type()
)
srexRsPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srexRsPropName.setStatus("current")
_SrexRsPropValue_Type = DisplayString
_SrexRsPropValue_Object = MibTableColumn
srexRsPropValue = _SrexRsPropValue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 3, 1, 1, 5),
    _SrexRsPropValue_Type()
)
srexRsPropValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srexRsPropValue.setStatus("current")
_SrexRsPropDesc_Type = DisplayString
_SrexRsPropDesc_Object = MibTableColumn
srexRsPropDesc = _SrexRsPropDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 3, 1, 1, 6),
    _SrexRsPropDesc_Type()
)
srexRsPropDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srexRsPropDesc.setStatus("current")
_ScRsConfigMethods_ObjectIdentity = ObjectIdentity
scRsConfigMethods = _ScRsConfigMethods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 4)
)
_ScrsTimeoutConfigTable_Object = MibTable
scrsTimeoutConfigTable = _ScrsTimeoutConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 4, 1)
)
if mibBuilder.loadTexts:
    scrsTimeoutConfigTable.setStatus("current")
_ScrsTimeoutConfigTableEntry_Object = MibTableRow
scrsTimeoutConfigTableEntry = _ScrsTimeoutConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 4, 1, 1)
)
scrsTimeoutConfigTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "srtoRgName"),
    (0, "SUN-CLUSTER-MIB", "srtoRsName"),
    (0, "SUN-CLUSTER-MIB", "srtoRsPropName"),
)
if mibBuilder.loadTexts:
    scrsTimeoutConfigTableEntry.setStatus("current")
_SrtoRowstatus_Type = RowStatus
_SrtoRowstatus_Object = MibTableColumn
srtoRowstatus = _SrtoRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 4, 1, 1, 1),
    _SrtoRowstatus_Type()
)
srtoRowstatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srtoRowstatus.setStatus("current")
_SrtoRgName_Type = DisplayString
_SrtoRgName_Object = MibTableColumn
srtoRgName = _SrtoRgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 4, 1, 1, 2),
    _SrtoRgName_Type()
)
srtoRgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtoRgName.setStatus("current")
_SrtoRsName_Type = DisplayString
_SrtoRsName_Object = MibTableColumn
srtoRsName = _SrtoRsName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 4, 1, 1, 3),
    _SrtoRsName_Type()
)
srtoRsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtoRsName.setStatus("current")
_SrtoRsPropName_Type = DisplayString
_SrtoRsPropName_Object = MibTableColumn
srtoRsPropName = _SrtoRsPropName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 4, 1, 1, 4),
    _SrtoRsPropName_Type()
)
srtoRsPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtoRsPropName.setStatus("current")
_SrtoRsPropValue_Type = DisplayString
_SrtoRsPropValue_Object = MibTableColumn
srtoRsPropValue = _SrtoRsPropValue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 4, 1, 1, 5),
    _SrtoRsPropValue_Type()
)
srtoRsPropValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtoRsPropValue.setStatus("current")
_SrtoRsPropDesc_Type = DisplayString
_SrtoRsPropDesc_Object = MibTableColumn
srtoRsPropDesc = _SrtoRsPropDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 6, 2, 2, 4, 4, 1, 1, 6),
    _SrtoRsPropDesc_Type()
)
srtoRsPropDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtoRsPropDesc.setStatus("current")
_ResourceTypes_ObjectIdentity = ObjectIdentity
resourceTypes = _ResourceTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7)
)
_DefinitionBranch_ObjectIdentity = ObjectIdentity
definitionBranch = _DefinitionBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1)
)
_RtOverview_ObjectIdentity = ObjectIdentity
rtOverview = _RtOverview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1)
)
_RtOverviewTable_Object = MibTable
rtOverviewTable = _RtOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rtOverviewTable.setStatus("current")
_RtOverviewTableEntry_Object = MibTableRow
rtOverviewTableEntry = _RtOverviewTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1, 1, 1)
)
rtOverviewTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "rtoName"),
)
if mibBuilder.loadTexts:
    rtOverviewTableEntry.setStatus("current")
_RtoName_Type = DisplayString
_RtoName_Object = MibTableColumn
rtoName = _RtoName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1, 1, 1, 1),
    _RtoName_Type()
)
rtoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtoName.setStatus("current")
_RtoNodes_Type = DisplayString
_RtoNodes_Object = MibTableColumn
rtoNodes = _RtoNodes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1, 1, 1, 2),
    _RtoNodes_Type()
)
rtoNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtoNodes.setStatus("current")
_RtoDesc_Type = DisplayString
_RtoDesc_Object = MibTableColumn
rtoDesc = _RtoDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1, 1, 1, 3),
    _RtoDesc_Type()
)
rtoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtoDesc.setStatus("current")
_RtoBaseDir_Type = DisplayString
_RtoBaseDir_Object = MibTableColumn
rtoBaseDir = _RtoBaseDir_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1, 1, 1, 4),
    _RtoBaseDir_Type()
)
rtoBaseDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtoBaseDir.setStatus("current")
_RtoSingleInst_Type = DisplayString
_RtoSingleInst_Object = MibTableColumn
rtoSingleInst = _RtoSingleInst_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1, 1, 1, 5),
    _RtoSingleInst_Type()
)
rtoSingleInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtoSingleInst.setStatus("current")
_RtoInitNodes_Type = DisplayString
_RtoInitNodes_Object = MibTableColumn
rtoInitNodes = _RtoInitNodes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1, 1, 1, 6),
    _RtoInitNodes_Type()
)
rtoInitNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtoInitNodes.setStatus("current")
_RtoFailover_Type = DisplayString
_RtoFailover_Object = MibTableColumn
rtoFailover = _RtoFailover_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1, 1, 1, 7),
    _RtoFailover_Type()
)
rtoFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtoFailover.setStatus("current")
_RtoSysDefType_Type = DisplayString
_RtoSysDefType_Object = MibTableColumn
rtoSysDefType = _RtoSysDefType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1, 1, 1, 8),
    _RtoSysDefType_Type()
)
rtoSysDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtoSysDefType.setStatus("current")
_RtoDepend_Type = DisplayString
_RtoDepend_Object = MibTableColumn
rtoDepend = _RtoDepend_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1, 1, 1, 9),
    _RtoDepend_Type()
)
rtoDepend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtoDepend.setStatus("current")
_RtoApiVersion_Type = Integer32
_RtoApiVersion_Object = MibTableColumn
rtoApiVersion = _RtoApiVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1, 1, 1, 10),
    _RtoApiVersion_Type()
)
rtoApiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtoApiVersion.setStatus("current")
_RtoVersion_Type = DisplayString
_RtoVersion_Object = MibTableColumn
rtoVersion = _RtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1, 1, 1, 11),
    _RtoVersion_Type()
)
rtoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtoVersion.setStatus("current")
_RtoPkglist_Type = DisplayString
_RtoPkglist_Object = MibTableColumn
rtoPkglist = _RtoPkglist_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 1, 1, 1, 12),
    _RtoPkglist_Type()
)
rtoPkglist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtoPkglist.setStatus("current")
_RtMethodProps_ObjectIdentity = ObjectIdentity
rtMethodProps = _RtMethodProps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2)
)
_RtMethodTable_Object = MibTable
rtMethodTable = _RtMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rtMethodTable.setStatus("current")
_RtMethodTableEntry_Object = MibTableRow
rtMethodTableEntry = _RtMethodTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1)
)
rtMethodTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "rtmName"),
)
if mibBuilder.loadTexts:
    rtMethodTableEntry.setStatus("current")
_RtmName_Type = DisplayString
_RtmName_Object = MibTableColumn
rtmName = _RtmName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 1),
    _RtmName_Type()
)
rtmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmName.setStatus("current")
_RtmSTART_Type = DisplayString
_RtmSTART_Object = MibTableColumn
rtmSTART = _RtmSTART_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 2),
    _RtmSTART_Type()
)
rtmSTART.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmSTART.setStatus("current")
_RtmSTOP_Type = DisplayString
_RtmSTOP_Object = MibTableColumn
rtmSTOP = _RtmSTOP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 3),
    _RtmSTOP_Type()
)
rtmSTOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmSTOP.setStatus("current")
_RtmPRIMCHANGE_Type = DisplayString
_RtmPRIMCHANGE_Object = MibTableColumn
rtmPRIMCHANGE = _RtmPRIMCHANGE_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 4),
    _RtmPRIMCHANGE_Type()
)
rtmPRIMCHANGE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmPRIMCHANGE.setStatus("current")
_RtmVALIDATE_Type = DisplayString
_RtmVALIDATE_Object = MibTableColumn
rtmVALIDATE = _RtmVALIDATE_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 5),
    _RtmVALIDATE_Type()
)
rtmVALIDATE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmVALIDATE.setStatus("current")
_RtmUPDATE_Type = DisplayString
_RtmUPDATE_Object = MibTableColumn
rtmUPDATE = _RtmUPDATE_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 6),
    _RtmUPDATE_Type()
)
rtmUPDATE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmUPDATE.setStatus("current")
_RtmINIT_Type = DisplayString
_RtmINIT_Object = MibTableColumn
rtmINIT = _RtmINIT_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 7),
    _RtmINIT_Type()
)
rtmINIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmINIT.setStatus("current")
_RtmFINI_Type = DisplayString
_RtmFINI_Object = MibTableColumn
rtmFINI = _RtmFINI_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 8),
    _RtmFINI_Type()
)
rtmFINI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmFINI.setStatus("current")
_RtmBOOT_Type = DisplayString
_RtmBOOT_Object = MibTableColumn
rtmBOOT = _RtmBOOT_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 9),
    _RtmBOOT_Type()
)
rtmBOOT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmBOOT.setStatus("current")
_RtmMONINIT_Type = DisplayString
_RtmMONINIT_Object = MibTableColumn
rtmMONINIT = _RtmMONINIT_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 10),
    _RtmMONINIT_Type()
)
rtmMONINIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmMONINIT.setStatus("current")
_RtmMONSTART_Type = DisplayString
_RtmMONSTART_Object = MibTableColumn
rtmMONSTART = _RtmMONSTART_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 11),
    _RtmMONSTART_Type()
)
rtmMONSTART.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmMONSTART.setStatus("current")
_RtmMONSTOP_Type = DisplayString
_RtmMONSTOP_Object = MibTableColumn
rtmMONSTOP = _RtmMONSTOP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 12),
    _RtmMONSTOP_Type()
)
rtmMONSTOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmMONSTOP.setStatus("current")
_RtmMONCHECK_Type = DisplayString
_RtmMONCHECK_Object = MibTableColumn
rtmMONCHECK = _RtmMONCHECK_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 13),
    _RtmMONCHECK_Type()
)
rtmMONCHECK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmMONCHECK.setStatus("current")
_RtmPRENETSTART_Type = DisplayString
_RtmPRENETSTART_Object = MibTableColumn
rtmPRENETSTART = _RtmPRENETSTART_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 14),
    _RtmPRENETSTART_Type()
)
rtmPRENETSTART.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmPRENETSTART.setStatus("current")
_RtmPOSTNETSTOP_Type = DisplayString
_RtmPOSTNETSTOP_Object = MibTableColumn
rtmPOSTNETSTOP = _RtmPOSTNETSTOP_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 2, 1, 1, 15),
    _RtmPOSTNETSTOP_Type()
)
rtmPOSTNETSTOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmPOSTNETSTOP.setStatus("current")
_RtParams_ObjectIdentity = ObjectIdentity
rtParams = _RtParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 3)
)
_RtParamTable_Object = MibTable
rtParamTable = _RtParamTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rtParamTable.setStatus("current")
_RtParamTableEntry_Object = MibTableRow
rtParamTableEntry = _RtParamTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 3, 1, 1)
)
rtParamTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "rtpName"),
    (0, "SUN-CLUSTER-MIB", "rtpPropName"),
)
if mibBuilder.loadTexts:
    rtParamTableEntry.setStatus("current")
_RtpName_Type = DisplayString
_RtpName_Object = MibTableColumn
rtpName = _RtpName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 3, 1, 1, 1),
    _RtpName_Type()
)
rtpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpName.setStatus("current")
_RtpPropName_Type = DisplayString
_RtpPropName_Object = MibTableColumn
rtpPropName = _RtpPropName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 3, 1, 1, 2),
    _RtpPropName_Type()
)
rtpPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpPropName.setStatus("current")
_RtpPropExt_Type = DisplayString
_RtpPropExt_Object = MibTableColumn
rtpPropExt = _RtpPropExt_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 3, 1, 1, 3),
    _RtpPropExt_Type()
)
rtpPropExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpPropExt.setStatus("current")
_RtpPropTunable_Type = DisplayString
_RtpPropTunable_Object = MibTableColumn
rtpPropTunable = _RtpPropTunable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 3, 1, 1, 4),
    _RtpPropTunable_Type()
)
rtpPropTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpPropTunable.setStatus("current")
_RtpPropType_Type = DisplayString
_RtpPropType_Object = MibTableColumn
rtpPropType = _RtpPropType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 3, 1, 1, 5),
    _RtpPropType_Type()
)
rtpPropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpPropType.setStatus("current")
_RtpPropDefault_Type = DisplayString
_RtpPropDefault_Object = MibTableColumn
rtpPropDefault = _RtpPropDefault_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 3, 1, 1, 6),
    _RtpPropDefault_Type()
)
rtpPropDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpPropDefault.setStatus("current")
_RtpPropMin_Type = DisplayString
_RtpPropMin_Object = MibTableColumn
rtpPropMin = _RtpPropMin_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 3, 1, 1, 7),
    _RtpPropMin_Type()
)
rtpPropMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpPropMin.setStatus("current")
_RtpPropMax_Type = DisplayString
_RtpPropMax_Object = MibTableColumn
rtpPropMax = _RtpPropMax_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 3, 1, 1, 8),
    _RtpPropMax_Type()
)
rtpPropMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpPropMax.setStatus("current")
_RtpPropArrayMin_Type = DisplayString
_RtpPropArrayMin_Object = MibTableColumn
rtpPropArrayMin = _RtpPropArrayMin_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 3, 1, 1, 9),
    _RtpPropArrayMin_Type()
)
rtpPropArrayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpPropArrayMin.setStatus("current")
_RtpPropArrayMax_Type = DisplayString
_RtpPropArrayMax_Object = MibTableColumn
rtpPropArrayMax = _RtpPropArrayMax_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 3, 1, 1, 10),
    _RtpPropArrayMax_Type()
)
rtpPropArrayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpPropArrayMax.setStatus("current")
_RtpPropDesc_Type = DisplayString
_RtpPropDesc_Object = MibTableColumn
rtpPropDesc = _RtpPropDesc_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 1, 3, 1, 1, 11),
    _RtpPropDesc_Type()
)
rtpPropDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpPropDesc.setStatus("current")
_ResourceList_ObjectIdentity = ObjectIdentity
resourceList = _ResourceList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 2)
)
_RtrsTable_Object = MibTable
rtrsTable = _RtrsTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    rtrsTable.setStatus("current")
_RtrsTableEntry_Object = MibTableRow
rtrsTableEntry = _RtrsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 2, 1, 1)
)
rtrsTableEntry.setIndexNames(
    (0, "SUN-CLUSTER-MIB", "rtrsRtName"),
    (0, "SUN-CLUSTER-MIB", "rtrsRgName"),
    (0, "SUN-CLUSTER-MIB", "rtrsRsName"),
)
if mibBuilder.loadTexts:
    rtrsTableEntry.setStatus("current")
_RtrsRtName_Type = DisplayString
_RtrsRtName_Object = MibTableColumn
rtrsRtName = _RtrsRtName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 2, 1, 1, 1),
    _RtrsRtName_Type()
)
rtrsRtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrsRtName.setStatus("current")
_RtrsRgName_Type = DisplayString
_RtrsRgName_Object = MibTableColumn
rtrsRgName = _RtrsRgName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 2, 1, 1, 2),
    _RtrsRgName_Type()
)
rtrsRgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrsRgName.setStatus("current")
_RtrsRsName_Type = DisplayString
_RtrsRsName_Object = MibTableColumn
rtrsRsName = _RtrsRsName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 80, 1, 1, 1, 7, 2, 1, 1, 3),
    _RtrsRsName_Type()
)
rtrsRsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrsRsName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUN-CLUSTER-MIB",
    **{"sun": sun,
       "prod": prod,
       "suncluster": suncluster,
       "sunmc": sunmc,
       "modules": modules,
       "sunclustermod": sunclustermod,
       "clusterInfo": clusterInfo,
       "clusterStatus": clusterStatus,
       "clsClusterName": clsClusterName,
       "clsMinVotesRequired": clsMinVotesRequired,
       "clsCurrentVotes": clsCurrentVotes,
       "clusterConfiguration": clusterConfiguration,
       "clcClusterName": clcClusterName,
       "clcInstallMode": clcInstallMode,
       "clcPrivateNetAddr": clcPrivateNetAddr,
       "clcPrivateNetMask": clcPrivateNetMask,
       "clcAddNodeAuthType": clcAddNodeAuthType,
       "clcAddNodeAuthList": clcAddNodeAuthList,
       "nodes": nodes,
       "nodeStatus": nodeStatus,
       "nodeTable": nodeTable,
       "nodeTableEntry": nodeTableEntry,
       "ndsNodeName": ndsNodeName,
       "ndsStatus": ndsStatus,
       "ndsCurrentNodeVotes": ndsCurrentNodeVotes,
       "nodeDeviceTable": nodeDeviceTable,
       "nodeDeviceTableEntry": nodeDeviceTableEntry,
       "ddsNodeName": ddsNodeName,
       "ddsMasteredDeviceGroupList": ddsMasteredDeviceGroupList,
       "ddsMasteredRGList": ddsMasteredRGList,
       "nodeConfiguration": nodeConfiguration,
       "nodeConfigTable": nodeConfigTable,
       "nodeConfigTableEntry": nodeConfigTableEntry,
       "ndcNodeName": ndcNodeName,
       "ndcDefaultVotes": ndcDefaultVotes,
       "ndcPrivateNetHostname": ndcPrivateNetHostname,
       "ndcTransportAdapterList": ndcTransportAdapterList,
       "nodeDeviceConfigTable": nodeDeviceConfigTable,
       "nodeDeviceConfigTableEntry": nodeDeviceConfigTableEntry,
       "ddcNodeName": ddcNodeName,
       "ddcQuorumDeviceList": ddcQuorumDeviceList,
       "ddcPossibleMasteredDeviceGroupList": ddcPossibleMasteredDeviceGroupList,
       "ddcPossibleMasteredRGList": ddcPossibleMasteredRGList,
       "deviceGroups": deviceGroups,
       "deviceGroupsStatus": deviceGroupsStatus,
       "deviceGroupTable": deviceGroupTable,
       "deviceGroupTableEntry": deviceGroupTableEntry,
       "dgsDeviceGroupName": dgsDeviceGroupName,
       "dgsDeviceGroupStatus": dgsDeviceGroupStatus,
       "dgsDeviceGroupPrimaryList": dgsDeviceGroupPrimaryList,
       "replicaTable": replicaTable,
       "replicaTableEntry": replicaTableEntry,
       "rpsDeviceGroupName": rpsDeviceGroupName,
       "rpsNodeName": rpsNodeName,
       "rpsStatus": rpsStatus,
       "deviceGroupsConfiguration": deviceGroupsConfiguration,
       "deviceGroupConfigTable": deviceGroupConfigTable,
       "deviceGroupConfigTableEntry": deviceGroupConfigTableEntry,
       "dgcDeviceGroupName": dgcDeviceGroupName,
       "dgcServiceType": dgcServiceType,
       "dgcFailback": dgcFailback,
       "dgcNodeList": dgcNodeList,
       "dgcNodeOrder": dgcNodeOrder,
       "dgcDeviceList": dgcDeviceList,
       "quorumDevices": quorumDevices,
       "quorumDevicesStatus": quorumDevicesStatus,
       "quorumDeviceTable": quorumDeviceTable,
       "quorumDeviceTableEntry": quorumDeviceTableEntry,
       "qdsQuorumDeviceName": qdsQuorumDeviceName,
       "qdsStatus": qdsStatus,
       "qdsCurrentVotes": qdsCurrentVotes,
       "qdsOwnerNode": qdsOwnerNode,
       "quorumDevicesConfiguration": quorumDevicesConfiguration,
       "quorumDeviceConfigTable": quorumDeviceConfigTable,
       "quorumDeviceConfigTableEntry": quorumDeviceConfigTableEntry,
       "qdcQuorumDeviceName": qdcQuorumDeviceName,
       "qdcQuorumDevicePath": qdcQuorumDevicePath,
       "qdcEnabled": qdcEnabled,
       "qdcDefaultVotes": qdcDefaultVotes,
       "qdcPortList": qdcPortList,
       "quorumDevicePortConfigTable": quorumDevicePortConfigTable,
       "quorumDevicePortConfigTableEntry": quorumDevicePortConfigTableEntry,
       "qpcQuorumDeviceName": qpcQuorumDeviceName,
       "qpcQuorumDeviceHost": qpcQuorumDeviceHost,
       "qpcEnabled": qpcEnabled,
       "transport": transport,
       "transportStatus": transportStatus,
       "pathTable": pathTable,
       "pathTableEntry": pathTableEntry,
       "ptsAdapterName1": ptsAdapterName1,
       "ptsAdapterName2": ptsAdapterName2,
       "ptsStatus": ptsStatus,
       "transportConfiguration": transportConfiguration,
       "adapterConfigTable": adapterConfigTable,
       "adapterConfigTableEntry": adapterConfigTableEntry,
       "adcNodeName": adcNodeName,
       "adcAdapterName": adcAdapterName,
       "adcType": adcType,
       "adcEnabled": adcEnabled,
       "junctionConfigTable": junctionConfigTable,
       "junctionConfigTableEntry": junctionConfigTableEntry,
       "jncJunctionName": jncJunctionName,
       "jncType": jncType,
       "jncEnabled": jncEnabled,
       "jncPortList": jncPortList,
       "cableConfigTable": cableConfigTable,
       "cableConfigTableEntry": cableConfigTableEntry,
       "cbcEndType1": cbcEndType1,
       "cbcEndpoint1": cbcEndpoint1,
       "cbcEndType2": cbcEndType2,
       "cbcEndpoint2": cbcEndpoint2,
       "cbcEnabled": cbcEnabled,
       "resourceGroups": resourceGroups,
       "rgStatus": rgStatus,
       "foRgStatusBranch": foRgStatusBranch,
       "forgStatusTable": forgStatusTable,
       "forgStatusTableEntry": forgStatusTableEntry,
       "frgRowStatus": frgRowStatus,
       "frgName": frgName,
       "frgPrim": frgPrim,
       "frgPrimStatus": frgPrimStatus,
       "frgState": frgState,
       "frsStatusTable": frsStatusTable,
       "frsStatusTableEntry": frsStatusTableEntry,
       "frsRowstatus": frsRowstatus,
       "frsRgName": frsRgName,
       "frsRsName": frsRsName,
       "frsRsPrim": frsRsPrim,
       "frsRsPrimStatus": frsRsPrimStatus,
       "frsRsFMStatus": frsRsFMStatus,
       "frsRsRGMState": frsRsRGMState,
       "scRgStatusBranch": scRgStatusBranch,
       "scrgStatusTable": scrgStatusTable,
       "scrgStatusTableEntry": scrgStatusTableEntry,
       "srgRowstatus": srgRowstatus,
       "srgName": srgName,
       "srgPrim": srgPrim,
       "srgPrimStatus": srgPrimStatus,
       "srgState": srgState,
       "srsStatusTable": srsStatusTable,
       "srsStatusTableEntry": srsStatusTableEntry,
       "srsRowstatus": srsRowstatus,
       "srsRgName": srsRgName,
       "srsRsName": srsRsName,
       "srsRsPrim": srsRsPrim,
       "srsRsPrimStatus": srsRsPrimStatus,
       "srsRsFMStatus": srsRsFMStatus,
       "srsRsRGMState": srsRsRGMState,
       "rgConfiguration": rgConfiguration,
       "foRgConfigBranch": foRgConfigBranch,
       "forgConfigInfo": forgConfigInfo,
       "forgConfigTable": forgConfigTable,
       "forgConfigTableEntry": forgConfigTableEntry,
       "frgcRowstatus": frgcRowstatus,
       "frgcRgName": frgcRgName,
       "frgcRgPrimaries": frgcRgPrimaries,
       "frgcRgDesc": frgcRgDesc,
       "frgcRsList": frgcRsList,
       "frgcRgMaxPrim": frgcRgMaxPrim,
       "frgcRgDesPrim": frgcRgDesPrim,
       "frgcRgFailbackFlag": frgcRgFailbackFlag,
       "frgcNetDepend": frgcNetDepend,
       "frgcRgDepend": frgcRgDepend,
       "frgcRgGlobRUsed": frgcRgGlobRUsed,
       "frgcRgPathPrefix": frgcRgPathPrefix,
       "foRsConfigBranch": foRsConfigBranch,
       "foRsConfigGen": foRsConfigGen,
       "forsGenConfigTable": forsGenConfigTable,
       "forsGenConfigTableEntry": forsGenConfigTableEntry,
       "frcRowstatus": frcRowstatus,
       "frcRgName": frcRgName,
       "frcRsName": frcRsName,
       "frcRsType": frcRsType,
       "frcRsEnabled": frcRsEnabled,
       "frcRsMonitored": frcRsMonitored,
       "frcRsStrongDepend": frcRsStrongDepend,
       "frcRsWeakDepend": frcRsWeakDepend,
       "foRsConfigStandProps": foRsConfigStandProps,
       "forsComPropConfigTable": forsComPropConfigTable,
       "forsComPropConfigTableEntry": forsComPropConfigTableEntry,
       "frstRowstatus": frstRowstatus,
       "frstRgName": frstRgName,
       "frstRsName": frstRsName,
       "frstRsPropName": frstRsPropName,
       "frstRsPropValue": frstRsPropValue,
       "frstRsPropDesc": frstRsPropDesc,
       "foRsConfigExtProps": foRsConfigExtProps,
       "forsExtPropConfigTable": forsExtPropConfigTable,
       "forsExtPropConfigTableEntry": forsExtPropConfigTableEntry,
       "frexRowstatus": frexRowstatus,
       "frexRgName": frexRgName,
       "frexRsName": frexRsName,
       "frexRsPropName": frexRsPropName,
       "frexRsPropValue": frexRsPropValue,
       "frexRsPropDesc": frexRsPropDesc,
       "foRsConfigMethods": foRsConfigMethods,
       "forsTimeoutConfigTable": forsTimeoutConfigTable,
       "forsTimeoutConfigTableEntry": forsTimeoutConfigTableEntry,
       "frtoRowstatus": frtoRowstatus,
       "frtoRgName": frtoRgName,
       "frtoRsName": frtoRsName,
       "frtoRsPropName": frtoRsPropName,
       "frtoRsPropValue": frtoRsPropValue,
       "frtoRsPropDesc": frtoRsPropDesc,
       "scRgConfigBranch": scRgConfigBranch,
       "scrgConfigInfo": scrgConfigInfo,
       "scrgConfigTable": scrgConfigTable,
       "scrgConfigTableEntry": scrgConfigTableEntry,
       "srgcRowstatus": srgcRowstatus,
       "srgcRgName": srgcRgName,
       "srgcRgPrimaries": srgcRgPrimaries,
       "srgcRgDesc": srgcRgDesc,
       "srgcRsList": srgcRsList,
       "srgcRgMaxPrim": srgcRgMaxPrim,
       "srgcRgDesPrim": srgcRgDesPrim,
       "srgcRgFailbackFlag": srgcRgFailbackFlag,
       "srgcNetDepend": srgcNetDepend,
       "srgcRgDepend": srgcRgDepend,
       "srgcRgGlobRUsed": srgcRgGlobRUsed,
       "srgcRgPathPrefix": srgcRgPathPrefix,
       "scRsConfigBranch": scRsConfigBranch,
       "scRsConfigGen": scRsConfigGen,
       "scrsGenConfigTable": scrsGenConfigTable,
       "scrsGenConfigTableEntry": scrsGenConfigTableEntry,
       "srcRowstatus": srcRowstatus,
       "srcRgName": srcRgName,
       "srcRsName": srcRsName,
       "srcRsType": srcRsType,
       "srcRsEnabled": srcRsEnabled,
       "srcRsMonitored": srcRsMonitored,
       "srcRsStrongDepend": srcRsStrongDepend,
       "srcRsWeakDepend": srcRsWeakDepend,
       "scRsConfigStandProps": scRsConfigStandProps,
       "scrsComPropConfigTable": scrsComPropConfigTable,
       "scrsComPropConfigTableEntry": scrsComPropConfigTableEntry,
       "srstRowstatus": srstRowstatus,
       "srstRgName": srstRgName,
       "srstRsName": srstRsName,
       "srstRsPropName": srstRsPropName,
       "srstRsPropValue": srstRsPropValue,
       "srstRsPropDesc": srstRsPropDesc,
       "scRsConfigExtProps": scRsConfigExtProps,
       "scrsExtPropConfigTable": scrsExtPropConfigTable,
       "scrsExtPropConfigTableEntry": scrsExtPropConfigTableEntry,
       "srexRowstatus": srexRowstatus,
       "srexRgName": srexRgName,
       "srexRsName": srexRsName,
       "srexRsPropName": srexRsPropName,
       "srexRsPropValue": srexRsPropValue,
       "srexRsPropDesc": srexRsPropDesc,
       "scRsConfigMethods": scRsConfigMethods,
       "scrsTimeoutConfigTable": scrsTimeoutConfigTable,
       "scrsTimeoutConfigTableEntry": scrsTimeoutConfigTableEntry,
       "srtoRowstatus": srtoRowstatus,
       "srtoRgName": srtoRgName,
       "srtoRsName": srtoRsName,
       "srtoRsPropName": srtoRsPropName,
       "srtoRsPropValue": srtoRsPropValue,
       "srtoRsPropDesc": srtoRsPropDesc,
       "resourceTypes": resourceTypes,
       "definitionBranch": definitionBranch,
       "rtOverview": rtOverview,
       "rtOverviewTable": rtOverviewTable,
       "rtOverviewTableEntry": rtOverviewTableEntry,
       "rtoName": rtoName,
       "rtoNodes": rtoNodes,
       "rtoDesc": rtoDesc,
       "rtoBaseDir": rtoBaseDir,
       "rtoSingleInst": rtoSingleInst,
       "rtoInitNodes": rtoInitNodes,
       "rtoFailover": rtoFailover,
       "rtoSysDefType": rtoSysDefType,
       "rtoDepend": rtoDepend,
       "rtoApiVersion": rtoApiVersion,
       "rtoVersion": rtoVersion,
       "rtoPkglist": rtoPkglist,
       "rtMethodProps": rtMethodProps,
       "rtMethodTable": rtMethodTable,
       "rtMethodTableEntry": rtMethodTableEntry,
       "rtmName": rtmName,
       "rtmSTART": rtmSTART,
       "rtmSTOP": rtmSTOP,
       "rtmPRIMCHANGE": rtmPRIMCHANGE,
       "rtmVALIDATE": rtmVALIDATE,
       "rtmUPDATE": rtmUPDATE,
       "rtmINIT": rtmINIT,
       "rtmFINI": rtmFINI,
       "rtmBOOT": rtmBOOT,
       "rtmMONINIT": rtmMONINIT,
       "rtmMONSTART": rtmMONSTART,
       "rtmMONSTOP": rtmMONSTOP,
       "rtmMONCHECK": rtmMONCHECK,
       "rtmPRENETSTART": rtmPRENETSTART,
       "rtmPOSTNETSTOP": rtmPOSTNETSTOP,
       "rtParams": rtParams,
       "rtParamTable": rtParamTable,
       "rtParamTableEntry": rtParamTableEntry,
       "rtpName": rtpName,
       "rtpPropName": rtpPropName,
       "rtpPropExt": rtpPropExt,
       "rtpPropTunable": rtpPropTunable,
       "rtpPropType": rtpPropType,
       "rtpPropDefault": rtpPropDefault,
       "rtpPropMin": rtpPropMin,
       "rtpPropMax": rtpPropMax,
       "rtpPropArrayMin": rtpPropArrayMin,
       "rtpPropArrayMax": rtpPropArrayMax,
       "rtpPropDesc": rtpPropDesc,
       "resourceList": resourceList,
       "rtrsTable": rtrsTable,
       "rtrsTableEntry": rtrsTableEntry,
       "rtrsRtName": rtrsRtName,
       "rtrsRgName": rtrsRgName,
       "rtrsRsName": rtrsRsName}
)
