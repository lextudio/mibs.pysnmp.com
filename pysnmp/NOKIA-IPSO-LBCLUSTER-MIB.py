# SNMP MIB module (NOKIA-IPSO-LBCLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-IPSO-LBCLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:40 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ipsoProducts,) = mibBuilder.importSymbols(
    "NOKIA-IPSO-REGISTRATION-MIB",
    "ipsoProducts")

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

(DisplayString,
 MacAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ipsoLBClusterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5)
)
ipsoLBClusterMIB.setRevisions(
        ("1901-05-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpsoLBClusterInfo_ObjectIdentity = ObjectIdentity
ipsoLBClusterInfo = _IpsoLBClusterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1)
)
_IpsoLBNumClusters_Type = Integer32
_IpsoLBNumClusters_Object = MibScalar
ipsoLBNumClusters = _IpsoLBNumClusters_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 1),
    _IpsoLBNumClusters_Type()
)
ipsoLBNumClusters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoLBNumClusters.setStatus("current")
_IpsoLBClusterInfoTable_Object = MibTable
ipsoLBClusterInfoTable = _IpsoLBClusterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ipsoLBClusterInfoTable.setStatus("current")
_IpsoLBClusterInfoEntry_Object = MibTableRow
ipsoLBClusterInfoEntry = _IpsoLBClusterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipsoLBClusterInfoEntry.setStatus("current")
_ClusterIndex_Type = Integer32
_ClusterIndex_Object = MibTableColumn
clusterIndex = _ClusterIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 1),
    _ClusterIndex_Type()
)
clusterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIndex.setStatus("current")
_ClusterID_Type = Integer32
_ClusterID_Object = MibTableColumn
clusterID = _ClusterID_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 2),
    _ClusterID_Type()
)
clusterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterID.setStatus("current")
_ClusterNumMembers_Type = Integer32
_ClusterNumMembers_Object = MibTableColumn
clusterNumMembers = _ClusterNumMembers_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 3),
    _ClusterNumMembers_Type()
)
clusterNumMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNumMembers.setStatus("current")
_ClusterNumInterfaces_Type = Integer32
_ClusterNumInterfaces_Object = MibTableColumn
clusterNumInterfaces = _ClusterNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 4),
    _ClusterNumInterfaces_Type()
)
clusterNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNumInterfaces.setStatus("current")
_ClusterUpTimeAtJoin_Type = TimeStamp
_ClusterUpTimeAtJoin_Object = MibTableColumn
clusterUpTimeAtJoin = _ClusterUpTimeAtJoin_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 5),
    _ClusterUpTimeAtJoin_Type()
)
clusterUpTimeAtJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterUpTimeAtJoin.setStatus("current")
_SystemUpTimeAtJoin_Type = TimeStamp
_SystemUpTimeAtJoin_Object = MibTableColumn
systemUpTimeAtJoin = _SystemUpTimeAtJoin_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 6),
    _SystemUpTimeAtJoin_Type()
)
systemUpTimeAtJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpTimeAtJoin.setStatus("current")
_ClusterTotalBuckets_Type = Integer32
_ClusterTotalBuckets_Object = MibTableColumn
clusterTotalBuckets = _ClusterTotalBuckets_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 7),
    _ClusterTotalBuckets_Type()
)
clusterTotalBuckets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterTotalBuckets.setStatus("current")
_ClusterBucketsAssigned_Type = Integer32
_ClusterBucketsAssigned_Object = MibTableColumn
clusterBucketsAssigned = _ClusterBucketsAssigned_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 8),
    _ClusterBucketsAssigned_Type()
)
clusterBucketsAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterBucketsAssigned.setStatus("current")
_IpsoLBClusterAddressTable_Object = MibTable
ipsoLBClusterAddressTable = _IpsoLBClusterAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3)
)
if mibBuilder.loadTexts:
    ipsoLBClusterAddressTable.setStatus("current")
_IpsoLBClusterAddressEntry_Object = MibTableRow
ipsoLBClusterAddressEntry = _IpsoLBClusterAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ipsoLBClusterAddressEntry.setStatus("current")
_ClusterIndex2_Type = Integer32
_ClusterIndex2_Object = MibScalar
clusterIndex2 = _ClusterIndex2_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3, 1, 1),
    _ClusterIndex2_Type()
)
clusterIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIndex2.setStatus("current")
_ClusterAddress_Type = IpAddress
_ClusterAddress_Object = MibTableColumn
clusterAddress = _ClusterAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3, 1, 2),
    _ClusterAddress_Type()
)
clusterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterAddress.setStatus("current")
_ClusterMACAddress_Type = MacAddress
_ClusterMACAddress_Object = MibTableColumn
clusterMACAddress = _ClusterMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3, 1, 3),
    _ClusterMACAddress_Type()
)
clusterMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMACAddress.setStatus("current")
_IpsoLBClusterMemberTable_Object = MibTable
ipsoLBClusterMemberTable = _IpsoLBClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4)
)
if mibBuilder.loadTexts:
    ipsoLBClusterMemberTable.setStatus("current")
_IpsoLBClusterMemberEntry_Object = MibTableRow
ipsoLBClusterMemberEntry = _IpsoLBClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipsoLBClusterMemberEntry.setStatus("current")
_ClusterIndex3_Type = Integer32
_ClusterIndex3_Object = MibScalar
clusterIndex3 = _ClusterIndex3_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 1),
    _ClusterIndex3_Type()
)
clusterIndex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIndex3.setStatus("current")
_MemberID_Type = Integer32
_MemberID_Object = MibTableColumn
memberID = _MemberID_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 2),
    _MemberID_Type()
)
memberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberID.setStatus("current")
_MemberPercentageBucketsAssigned_Type = Integer32
_MemberPercentageBucketsAssigned_Object = MibTableColumn
memberPercentageBucketsAssigned = _MemberPercentageBucketsAssigned_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 3),
    _MemberPercentageBucketsAssigned_Type()
)
memberPercentageBucketsAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberPercentageBucketsAssigned.setStatus("current")
_MemberRating_Type = OctetString
_MemberRating_Object = MibTableColumn
memberRating = _MemberRating_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 4),
    _MemberRating_Type()
)
memberRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberRating.setStatus("current")
_MemberPrimaryAddress_Type = IpAddress
_MemberPrimaryAddress_Object = MibTableColumn
memberPrimaryAddress = _MemberPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 5),
    _MemberPrimaryAddress_Type()
)
memberPrimaryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberPrimaryAddress.setStatus("current")
_IpsoLBClusterNodeSpecificInfo_ObjectIdentity = ObjectIdentity
ipsoLBClusterNodeSpecificInfo = _IpsoLBClusterNodeSpecificInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2)
)
_IpsoLBClusterNodeSpecificTable_Object = MibTable
ipsoLBClusterNodeSpecificTable = _IpsoLBClusterNodeSpecificTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1)
)
if mibBuilder.loadTexts:
    ipsoLBClusterNodeSpecificTable.setStatus("current")
_IpsoLBClusterNodeSpecificEntry_Object = MibTableRow
ipsoLBClusterNodeSpecificEntry = _IpsoLBClusterNodeSpecificEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipsoLBClusterNodeSpecificEntry.setStatus("current")
_ClusterIndex4_Type = Integer32
_ClusterIndex4_Object = MibScalar
clusterIndex4 = _ClusterIndex4_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 1),
    _ClusterIndex4_Type()
)
clusterIndex4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIndex4.setStatus("current")
_MemberID2_Type = Integer32
_MemberID2_Object = MibScalar
memberID2 = _MemberID2_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 2),
    _MemberID2_Type()
)
memberID2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberID2.setStatus("current")
_PercentageBucketsAssigned_Type = Integer32
_PercentageBucketsAssigned_Object = MibTableColumn
percentageBucketsAssigned = _PercentageBucketsAssigned_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 3),
    _PercentageBucketsAssigned_Type()
)
percentageBucketsAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    percentageBucketsAssigned.setStatus("current")


class _MemberMode_Type(Integer32):
    """Custom type memberMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("becomingmaster", 4),
          ("initialized", 2),
          ("joining", 3),
          ("master", 5),
          ("member", 6),
          ("uninitialized", 1),
          ("unknown", 7))
    )


_MemberMode_Type.__name__ = "Integer32"
_MemberMode_Object = MibTableColumn
memberMode = _MemberMode_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 4),
    _MemberMode_Type()
)
memberMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberMode.setStatus("current")
_MemberRating2_Type = Integer32
_MemberRating2_Object = MibScalar
memberRating2 = _MemberRating2_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 5),
    _MemberRating2_Type()
)
memberRating2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberRating2.setStatus("current")
_MemberPrimaryAddress2_Type = IpAddress
_MemberPrimaryAddress2_Object = MibScalar
memberPrimaryAddress2 = _MemberPrimaryAddress2_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 6),
    _MemberPrimaryAddress2_Type()
)
memberPrimaryAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberPrimaryAddress2.setStatus("current")
_IpsoLBClusterNodeSpecificInterfaceTable_Object = MibTable
ipsoLBClusterNodeSpecificInterfaceTable = _IpsoLBClusterNodeSpecificInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2)
)
if mibBuilder.loadTexts:
    ipsoLBClusterNodeSpecificInterfaceTable.setStatus("current")
_IpsoLBClusterNodeSpecificInterfaceEntry_Object = MibTableRow
ipsoLBClusterNodeSpecificInterfaceEntry = _IpsoLBClusterNodeSpecificInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ipsoLBClusterNodeSpecificInterfaceEntry.setStatus("current")
_ClusterIndex5_Type = Integer32
_ClusterIndex5_Object = MibScalar
clusterIndex5 = _ClusterIndex5_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 1),
    _ClusterIndex5_Type()
)
clusterIndex5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIndex5.setStatus("current")
_MemberID3_Type = Integer32
_MemberID3_Object = MibScalar
memberID3 = _MemberID3_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 2),
    _MemberID3_Type()
)
memberID3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberID3.setStatus("current")
_IfIndex_Type = InterfaceIndex
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 3),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndex.setStatus("current")
_ClusterIPAddress_Type = IpAddress
_ClusterIPAddress_Object = MibTableColumn
clusterIPAddress = _ClusterIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 4),
    _ClusterIPAddress_Type()
)
clusterIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIPAddress.setStatus("current")
_ClusterNetMask_Type = IpAddress
_ClusterNetMask_Object = MibTableColumn
clusterNetMask = _ClusterNetMask_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 5),
    _ClusterNetMask_Type()
)
clusterNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNetMask.setStatus("current")
_ClusterBroadcastAddress_Type = IpAddress
_ClusterBroadcastAddress_Object = MibTableColumn
clusterBroadcastAddress = _ClusterBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 6),
    _ClusterBroadcastAddress_Type()
)
clusterBroadcastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterBroadcastAddress.setStatus("current")
_RealIPAddress_Type = IpAddress
_RealIPAddress_Object = MibTableColumn
realIPAddress = _RealIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 7),
    _RealIPAddress_Type()
)
realIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realIPAddress.setStatus("current")
_MasterIPAddress_Type = IpAddress
_MasterIPAddress_Object = MibTableColumn
masterIPAddress = _MasterIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 8),
    _MasterIPAddress_Type()
)
masterIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterIPAddress.setStatus("current")
_IpsoLBClusterNotificationGroup_ObjectIdentity = ObjectIdentity
ipsoLBClusterNotificationGroup = _IpsoLBClusterNotificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3)
)


class _IpsoLBMemberJoinRejectReason_Type(Integer32):
    """Custom type ipsoLBMemberJoinRejectReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fewinterface", 1),
          ("illegallicence", 2))
    )


_IpsoLBMemberJoinRejectReason_Type.__name__ = "Integer32"
_IpsoLBMemberJoinRejectReason_Object = MibScalar
ipsoLBMemberJoinRejectReason = _IpsoLBMemberJoinRejectReason_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 0),
    _IpsoLBMemberJoinRejectReason_Type()
)
ipsoLBMemberJoinRejectReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsoLBMemberJoinRejectReason.setStatus("current")


class _IpsoLBClusterNewMasterReason_Type(Integer32):
    """Custom type ipsoLBClusterNewMasterReason based on Integer32"""
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
        *(("iamBetterMaster", 2),
          ("initalizedAsMaster", 3),
          ("oldMasterHelloTimeout", 1),
          ("unknown", 4))
    )


_IpsoLBClusterNewMasterReason_Type.__name__ = "Integer32"
_IpsoLBClusterNewMasterReason_Object = MibScalar
ipsoLBClusterNewMasterReason = _IpsoLBClusterNewMasterReason_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 1),
    _IpsoLBClusterNewMasterReason_Type()
)
ipsoLBClusterNewMasterReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsoLBClusterNewMasterReason.setStatus("current")


class _IpsoMemberRejectErcode_Type(Integer32):
    """Custom type ipsoMemberRejectErcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              22,
              55,
              61,
              65)
        )
    )
    namedValues = NamedValues(
        *(("configurationmismatch", 6),
          ("internalerroronmaster", 55),
          ("nodeunreachableononeoftheselectedinterfaces", 65),
          ("numberofmembersclustercansupportexceeded", 22),
          ("protocolversionmismatch", 61))
    )


_IpsoMemberRejectErcode_Type.__name__ = "Integer32"
_IpsoMemberRejectErcode_Object = MibScalar
ipsoMemberRejectErcode = _IpsoMemberRejectErcode_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 6),
    _IpsoMemberRejectErcode_Type()
)
ipsoMemberRejectErcode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsoMemberRejectErcode.setStatus("current")
_IpsoMemberRejectWrongIntf_Type = OctetString
_IpsoMemberRejectWrongIntf_Object = MibScalar
ipsoMemberRejectWrongIntf = _IpsoMemberRejectWrongIntf_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 7),
    _IpsoMemberRejectWrongIntf_Type()
)
ipsoMemberRejectWrongIntf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsoMemberRejectWrongIntf.setStatus("current")
_IpsoMemberRejectprimaryintf_Type = OctetString
_IpsoMemberRejectprimaryintf_Object = MibScalar
ipsoMemberRejectprimaryintf = _IpsoMemberRejectprimaryintf_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 8),
    _IpsoMemberRejectprimaryintf_Type()
)
ipsoMemberRejectprimaryintf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsoMemberRejectprimaryintf.setStatus("current")
_IpsoMemberRejectCip_Type = OctetString
_IpsoMemberRejectCip_Object = MibScalar
ipsoMemberRejectCip = _IpsoMemberRejectCip_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 9),
    _IpsoMemberRejectCip_Type()
)
ipsoMemberRejectCip.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsoMemberRejectCip.setStatus("current")
_IpsoMemberRejectHash_Type = OctetString
_IpsoMemberRejectHash_Object = MibScalar
ipsoMemberRejectHash = _IpsoMemberRejectHash_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 10),
    _IpsoMemberRejectHash_Type()
)
ipsoMemberRejectHash.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsoMemberRejectHash.setStatus("current")
_IpsoMemberIPAddress_Type = IpAddress
_IpsoMemberIPAddress_Object = MibScalar
ipsoMemberIPAddress = _IpsoMemberIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 11),
    _IpsoMemberIPAddress_Type()
)
ipsoMemberIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsoMemberIPAddress.setStatus("current")

# Managed Objects groups


# Notification objects

ipsoLBClusterMemberJoin = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 2)
)
ipsoLBClusterMemberJoin.setObjects(
      *(("NOKIA-IPSO-LBCLUSTER-MIB", "clusterID"),
        ("NOKIA-IPSO-LBCLUSTER-MIB", "memberID"),
        ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberIPAddress"))
)
if mibBuilder.loadTexts:
    ipsoLBClusterMemberJoin.setStatus(
        "current"
    )

ipsoLBClusterMemberLeft = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 3)
)
ipsoLBClusterMemberLeft.setObjects(
      *(("NOKIA-IPSO-LBCLUSTER-MIB", "clusterID"),
        ("NOKIA-IPSO-LBCLUSTER-MIB", "memberID"),
        ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberIPAddress"))
)
if mibBuilder.loadTexts:
    ipsoLBClusterMemberLeft.setStatus(
        "current"
    )

ipsoLBClusterNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 4)
)
ipsoLBClusterNewMaster.setObjects(
      *(("NOKIA-IPSO-LBCLUSTER-MIB", "clusterID"),
        ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoLBClusterNewMasterReason"))
)
if mibBuilder.loadTexts:
    ipsoLBClusterNewMaster.setStatus(
        "current"
    )

ipsoLBJoinReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 5)
)
ipsoLBJoinReject.setObjects(
      *(("NOKIA-IPSO-LBCLUSTER-MIB", "clusterID"),
        ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberIPAddress"),
        ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectErcode"),
        ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectWrongIntf"),
        ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectprimaryintf"),
        ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectCip"),
        ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectHash"))
)
if mibBuilder.loadTexts:
    ipsoLBJoinReject.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-IPSO-LBCLUSTER-MIB",
    **{"ipsoLBClusterMIB": ipsoLBClusterMIB,
       "ipsoLBClusterInfo": ipsoLBClusterInfo,
       "ipsoLBNumClusters": ipsoLBNumClusters,
       "ipsoLBClusterInfoTable": ipsoLBClusterInfoTable,
       "ipsoLBClusterInfoEntry": ipsoLBClusterInfoEntry,
       "clusterIndex": clusterIndex,
       "clusterID": clusterID,
       "clusterNumMembers": clusterNumMembers,
       "clusterNumInterfaces": clusterNumInterfaces,
       "clusterUpTimeAtJoin": clusterUpTimeAtJoin,
       "systemUpTimeAtJoin": systemUpTimeAtJoin,
       "clusterTotalBuckets": clusterTotalBuckets,
       "clusterBucketsAssigned": clusterBucketsAssigned,
       "ipsoLBClusterAddressTable": ipsoLBClusterAddressTable,
       "ipsoLBClusterAddressEntry": ipsoLBClusterAddressEntry,
       "clusterIndex2": clusterIndex2,
       "clusterAddress": clusterAddress,
       "clusterMACAddress": clusterMACAddress,
       "ipsoLBClusterMemberTable": ipsoLBClusterMemberTable,
       "ipsoLBClusterMemberEntry": ipsoLBClusterMemberEntry,
       "clusterIndex3": clusterIndex3,
       "memberID": memberID,
       "memberPercentageBucketsAssigned": memberPercentageBucketsAssigned,
       "memberRating": memberRating,
       "memberPrimaryAddress": memberPrimaryAddress,
       "ipsoLBClusterNodeSpecificInfo": ipsoLBClusterNodeSpecificInfo,
       "ipsoLBClusterNodeSpecificTable": ipsoLBClusterNodeSpecificTable,
       "ipsoLBClusterNodeSpecificEntry": ipsoLBClusterNodeSpecificEntry,
       "clusterIndex4": clusterIndex4,
       "memberID2": memberID2,
       "percentageBucketsAssigned": percentageBucketsAssigned,
       "memberMode": memberMode,
       "memberRating2": memberRating2,
       "memberPrimaryAddress2": memberPrimaryAddress2,
       "ipsoLBClusterNodeSpecificInterfaceTable": ipsoLBClusterNodeSpecificInterfaceTable,
       "ipsoLBClusterNodeSpecificInterfaceEntry": ipsoLBClusterNodeSpecificInterfaceEntry,
       "clusterIndex5": clusterIndex5,
       "memberID3": memberID3,
       "ifIndex": ifIndex,
       "clusterIPAddress": clusterIPAddress,
       "clusterNetMask": clusterNetMask,
       "clusterBroadcastAddress": clusterBroadcastAddress,
       "realIPAddress": realIPAddress,
       "masterIPAddress": masterIPAddress,
       "ipsoLBClusterNotificationGroup": ipsoLBClusterNotificationGroup,
       "ipsoLBMemberJoinRejectReason": ipsoLBMemberJoinRejectReason,
       "ipsoLBClusterNewMasterReason": ipsoLBClusterNewMasterReason,
       "ipsoLBClusterMemberJoin": ipsoLBClusterMemberJoin,
       "ipsoLBClusterMemberLeft": ipsoLBClusterMemberLeft,
       "ipsoLBClusterNewMaster": ipsoLBClusterNewMaster,
       "ipsoLBJoinReject": ipsoLBJoinReject,
       "ipsoMemberRejectErcode": ipsoMemberRejectErcode,
       "ipsoMemberRejectWrongIntf": ipsoMemberRejectWrongIntf,
       "ipsoMemberRejectprimaryintf": ipsoMemberRejectprimaryintf,
       "ipsoMemberRejectCip": ipsoMemberRejectCip,
       "ipsoMemberRejectHash": ipsoMemberRejectHash,
       "ipsoMemberIPAddress": ipsoMemberIPAddress}
)
