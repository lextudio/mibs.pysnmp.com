# SNMP MIB module (HUAWEI-MC-TRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MC-TRUNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:53 2024
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

(huaweiMgmt,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiMgmt")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hwMcTrunkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwDatacomm_ObjectIdentity = ObjectIdentity
hwDatacomm = _HwDatacomm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25)
)
_HwMcTrunkObjects_ObjectIdentity = ObjectIdentity
hwMcTrunkObjects = _HwMcTrunkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1)
)
_HwMcTrunkTable_Object = MibTable
hwMcTrunkTable = _HwMcTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1)
)
if mibBuilder.loadTexts:
    hwMcTrunkTable.setStatus("current")
_HwMcTrunkEntry_Object = MibTableRow
hwMcTrunkEntry = _HwMcTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1)
)
hwMcTrunkEntry.setIndexNames(
    (0, "HUAWEI-MC-TRUNK-MIB", "hwMcTrunkId"),
)
if mibBuilder.loadTexts:
    hwMcTrunkEntry.setStatus("current")


class _HwMcTrunkId_Type(Integer32):
    """Custom type hwMcTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwMcTrunkId_Type.__name__ = "Integer32"
_HwMcTrunkId_Object = MibTableColumn
hwMcTrunkId = _HwMcTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 1),
    _HwMcTrunkId_Type()
)
hwMcTrunkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMcTrunkId.setStatus("current")
_HwMcTrunkSystemId_Type = PhysAddress
_HwMcTrunkSystemId_Object = MibTableColumn
hwMcTrunkSystemId = _HwMcTrunkSystemId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 2),
    _HwMcTrunkSystemId_Type()
)
hwMcTrunkSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMcTrunkSystemId.setStatus("current")


class _HwMcTrunkPri_Type(Integer32):
    """Custom type hwMcTrunkPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HwMcTrunkPri_Type.__name__ = "Integer32"
_HwMcTrunkPri_Object = MibTableColumn
hwMcTrunkPri = _HwMcTrunkPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 3),
    _HwMcTrunkPri_Type()
)
hwMcTrunkPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcTrunkPri.setStatus("current")


class _HwMcTrunkStatus_Type(Integer32):
    """Custom type hwMcTrunkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("initialize", 1),
          ("master", 3))
    )


_HwMcTrunkStatus_Type.__name__ = "Integer32"
_HwMcTrunkStatus_Object = MibTableColumn
hwMcTrunkStatus = _HwMcTrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 4),
    _HwMcTrunkStatus_Type()
)
hwMcTrunkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMcTrunkStatus.setStatus("current")


class _HwMcTrunkStatusReason_Type(Integer32):
    """Custom type hwMcTrunkStatusReason based on Integer32"""
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
        *(("allMemberDown", 6),
          ("bfdDown", 3),
          ("init", 7),
          ("peerBfdDown", 5),
          ("peerTimeout", 4),
          ("pri", 1),
          ("timeout", 2))
    )


_HwMcTrunkStatusReason_Type.__name__ = "Integer32"
_HwMcTrunkStatusReason_Object = MibTableColumn
hwMcTrunkStatusReason = _HwMcTrunkStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 5),
    _HwMcTrunkStatusReason_Type()
)
hwMcTrunkStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMcTrunkStatusReason.setStatus("current")
_HwMcTrunkPeerIpAddr_Type = IpAddress
_HwMcTrunkPeerIpAddr_Object = MibTableColumn
hwMcTrunkPeerIpAddr = _HwMcTrunkPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 6),
    _HwMcTrunkPeerIpAddr_Type()
)
hwMcTrunkPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcTrunkPeerIpAddr.setStatus("current")
_HwMcTrunkSourceIpAddr_Type = IpAddress
_HwMcTrunkSourceIpAddr_Object = MibTableColumn
hwMcTrunkSourceIpAddr = _HwMcTrunkSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 7),
    _HwMcTrunkSourceIpAddr_Type()
)
hwMcTrunkSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcTrunkSourceIpAddr.setStatus("current")


class _HwMcTrunkReceiveFailTimeMultiple_Type(Integer32):
    """Custom type hwMcTrunkReceiveFailTimeMultiple based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_HwMcTrunkReceiveFailTimeMultiple_Type.__name__ = "Integer32"
_HwMcTrunkReceiveFailTimeMultiple_Object = MibTableColumn
hwMcTrunkReceiveFailTimeMultiple = _HwMcTrunkReceiveFailTimeMultiple_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 8),
    _HwMcTrunkReceiveFailTimeMultiple_Type()
)
hwMcTrunkReceiveFailTimeMultiple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcTrunkReceiveFailTimeMultiple.setStatus("current")


class _HwMcTrunkSendPeriod_Type(Integer32):
    """Custom type hwMcTrunkSendPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_HwMcTrunkSendPeriod_Type.__name__ = "Integer32"
_HwMcTrunkSendPeriod_Object = MibTableColumn
hwMcTrunkSendPeriod = _HwMcTrunkSendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 9),
    _HwMcTrunkSendPeriod_Type()
)
hwMcTrunkSendPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcTrunkSendPeriod.setStatus("current")
_HwMcTrunkPacketReceive_Type = Counter64
_HwMcTrunkPacketReceive_Object = MibTableColumn
hwMcTrunkPacketReceive = _HwMcTrunkPacketReceive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 10),
    _HwMcTrunkPacketReceive_Type()
)
hwMcTrunkPacketReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMcTrunkPacketReceive.setStatus("current")
_HwMcTrunkPacketSend_Type = Counter64
_HwMcTrunkPacketSend_Object = MibTableColumn
hwMcTrunkPacketSend = _HwMcTrunkPacketSend_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 11),
    _HwMcTrunkPacketSend_Type()
)
hwMcTrunkPacketSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMcTrunkPacketSend.setStatus("current")
_HwMcTrunkPacketRecDrop_Type = Counter64
_HwMcTrunkPacketRecDrop_Object = MibTableColumn
hwMcTrunkPacketRecDrop = _HwMcTrunkPacketRecDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 12),
    _HwMcTrunkPacketRecDrop_Type()
)
hwMcTrunkPacketRecDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMcTrunkPacketRecDrop.setStatus("current")
_HwMcTrunkPacketSndDrop_Type = Counter64
_HwMcTrunkPacketSndDrop_Object = MibTableColumn
hwMcTrunkPacketSndDrop = _HwMcTrunkPacketSndDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 13),
    _HwMcTrunkPacketSndDrop_Type()
)
hwMcTrunkPacketSndDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMcTrunkPacketSndDrop.setStatus("current")
_HwMcTrunkPeerSystemId_Type = PhysAddress
_HwMcTrunkPeerSystemId_Object = MibTableColumn
hwMcTrunkPeerSystemId = _HwMcTrunkPeerSystemId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 14),
    _HwMcTrunkPeerSystemId_Type()
)
hwMcTrunkPeerSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMcTrunkPeerSystemId.setStatus("current")


class _HwMcTrunkPeerPri_Type(Integer32):
    """Custom type hwMcTrunkPeerPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HwMcTrunkPeerPri_Type.__name__ = "Integer32"
_HwMcTrunkPeerPri_Object = MibTableColumn
hwMcTrunkPeerPri = _HwMcTrunkPeerPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 15),
    _HwMcTrunkPeerPri_Type()
)
hwMcTrunkPeerPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMcTrunkPeerPri.setStatus("current")


class _HwMcTrunkPeerReceiveFailTime_Type(Integer32):
    """Custom type hwMcTrunkPeerReceiveFailTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 5000),
    )


_HwMcTrunkPeerReceiveFailTime_Type.__name__ = "Integer32"
_HwMcTrunkPeerReceiveFailTime_Object = MibTableColumn
hwMcTrunkPeerReceiveFailTime = _HwMcTrunkPeerReceiveFailTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 16),
    _HwMcTrunkPeerReceiveFailTime_Type()
)
hwMcTrunkPeerReceiveFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMcTrunkPeerReceiveFailTime.setStatus("current")


class _HwMcTrunkSecurityKeyType_Type(Integer32):
    """Custom type hwMcTrunkSecurityKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 2),
          ("simple", 1))
    )


_HwMcTrunkSecurityKeyType_Type.__name__ = "Integer32"
_HwMcTrunkSecurityKeyType_Object = MibTableColumn
hwMcTrunkSecurityKeyType = _HwMcTrunkSecurityKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 17),
    _HwMcTrunkSecurityKeyType_Type()
)
hwMcTrunkSecurityKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcTrunkSecurityKeyType.setStatus("current")


class _HwMcTrunkSecurityKey_Type(OctetString):
    """Custom type hwMcTrunkSecurityKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_HwMcTrunkSecurityKey_Type.__name__ = "OctetString"
_HwMcTrunkSecurityKey_Object = MibTableColumn
hwMcTrunkSecurityKey = _HwMcTrunkSecurityKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 18),
    _HwMcTrunkSecurityKey_Type()
)
hwMcTrunkSecurityKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcTrunkSecurityKey.setStatus("current")


class _HwMcTrunkBfdSessId_Type(Integer32):
    """Custom type hwMcTrunkBfdSessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_HwMcTrunkBfdSessId_Type.__name__ = "Integer32"
_HwMcTrunkBfdSessId_Object = MibTableColumn
hwMcTrunkBfdSessId = _HwMcTrunkBfdSessId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 19),
    _HwMcTrunkBfdSessId_Type()
)
hwMcTrunkBfdSessId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcTrunkBfdSessId.setStatus("current")


class _HwMcTrunkResetCounter_Type(Integer32):
    """Custom type hwMcTrunkResetCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_HwMcTrunkResetCounter_Type.__name__ = "Integer32"
_HwMcTrunkResetCounter_Object = MibTableColumn
hwMcTrunkResetCounter = _HwMcTrunkResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 20),
    _HwMcTrunkResetCounter_Type()
)
hwMcTrunkResetCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcTrunkResetCounter.setStatus("current")


class _HwMcTrunkRevertTime_Type(Integer32):
    """Custom type hwMcTrunkRevertTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwMcTrunkRevertTime_Type.__name__ = "Integer32"
_HwMcTrunkRevertTime_Object = MibTableColumn
hwMcTrunkRevertTime = _HwMcTrunkRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 21),
    _HwMcTrunkRevertTime_Type()
)
hwMcTrunkRevertTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcTrunkRevertTime.setStatus("current")
_HwMcTrunkRowStatus_Type = RowStatus
_HwMcTrunkRowStatus_Object = MibTableColumn
hwMcTrunkRowStatus = _HwMcTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 50),
    _HwMcTrunkRowStatus_Type()
)
hwMcTrunkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcTrunkRowStatus.setStatus("current")
_HwMcTrunkMemberTable_Object = MibTable
hwMcTrunkMemberTable = _HwMcTrunkMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2)
)
if mibBuilder.loadTexts:
    hwMcTrunkMemberTable.setStatus("current")
_HwMcTrunkMemberEntry_Object = MibTableRow
hwMcTrunkMemberEntry = _HwMcTrunkMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1)
)
hwMcTrunkMemberEntry.setIndexNames(
    (0, "HUAWEI-MC-TRUNK-MIB", "hwMcTrunkMemberParentId"),
    (0, "HUAWEI-MC-TRUNK-MIB", "hwMcTrunkMemberType"),
    (0, "HUAWEI-MC-TRUNK-MIB", "hwMcTrunkMemberId"),
)
if mibBuilder.loadTexts:
    hwMcTrunkMemberEntry.setStatus("current")


class _HwMcTrunkMemberParentId_Type(Integer32):
    """Custom type hwMcTrunkMemberParentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwMcTrunkMemberParentId_Type.__name__ = "Integer32"
_HwMcTrunkMemberParentId_Object = MibTableColumn
hwMcTrunkMemberParentId = _HwMcTrunkMemberParentId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 1),
    _HwMcTrunkMemberParentId_Type()
)
hwMcTrunkMemberParentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMcTrunkMemberParentId.setStatus("current")


class _HwMcTrunkMemberType_Type(Integer32):
    """Custom type hwMcTrunkMemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwMcTrunkMemberType_Type.__name__ = "Integer32"
_HwMcTrunkMemberType_Object = MibTableColumn
hwMcTrunkMemberType = _HwMcTrunkMemberType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 2),
    _HwMcTrunkMemberType_Type()
)
hwMcTrunkMemberType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMcTrunkMemberType.setStatus("current")
_HwMcTrunkMemberId_Type = Unsigned32
_HwMcTrunkMemberId_Object = MibTableColumn
hwMcTrunkMemberId = _HwMcTrunkMemberId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 3),
    _HwMcTrunkMemberId_Type()
)
hwMcTrunkMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMcTrunkMemberId.setStatus("current")


class _HwMcTrunkMemberStatus_Type(Integer32):
    """Custom type hwMcTrunkMemberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("master", 2))
    )


_HwMcTrunkMemberStatus_Type.__name__ = "Integer32"
_HwMcTrunkMemberStatus_Object = MibTableColumn
hwMcTrunkMemberStatus = _HwMcTrunkMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 4),
    _HwMcTrunkMemberStatus_Type()
)
hwMcTrunkMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMcTrunkMemberStatus.setStatus("current")


class _HwMcTrunkMemberStatusReason_Type(Integer32):
    """Custom type hwMcTrunkMemberStatusReason based on Integer32"""
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
        *(("forceBackup", 1),
          ("forceMaster", 2),
          ("mctrunkBackup", 4),
          ("mctrunkInit", 3),
          ("mctrunkMaster", 5),
          ("peerMemberDown", 6),
          ("peerMemberUp", 7))
    )


_HwMcTrunkMemberStatusReason_Type.__name__ = "Integer32"
_HwMcTrunkMemberStatusReason_Object = MibTableColumn
hwMcTrunkMemberStatusReason = _HwMcTrunkMemberStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 5),
    _HwMcTrunkMemberStatusReason_Type()
)
hwMcTrunkMemberStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMcTrunkMemberStatusReason.setStatus("current")


class _HwMcTrunkMemberWorkMode_Type(Integer32):
    """Custom type hwMcTrunkMemberWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forceBackup", 2),
          ("forceMaster", 3))
    )


_HwMcTrunkMemberWorkMode_Type.__name__ = "Integer32"
_HwMcTrunkMemberWorkMode_Object = MibTableColumn
hwMcTrunkMemberWorkMode = _HwMcTrunkMemberWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 6),
    _HwMcTrunkMemberWorkMode_Type()
)
hwMcTrunkMemberWorkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcTrunkMemberWorkMode.setStatus("current")


class _HwMcTrunkMemberPhyStatus_Type(Integer32):
    """Custom type hwMcTrunkMemberPhyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HwMcTrunkMemberPhyStatus_Type.__name__ = "Integer32"
_HwMcTrunkMemberPhyStatus_Object = MibTableColumn
hwMcTrunkMemberPhyStatus = _HwMcTrunkMemberPhyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 7),
    _HwMcTrunkMemberPhyStatus_Type()
)
hwMcTrunkMemberPhyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMcTrunkMemberPhyStatus.setStatus("current")
_HwMcTrunkMemberRowStatus_Type = RowStatus
_HwMcTrunkMemberRowStatus_Object = MibTableColumn
hwMcTrunkMemberRowStatus = _HwMcTrunkMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 50),
    _HwMcTrunkMemberRowStatus_Type()
)
hwMcTrunkMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcTrunkMemberRowStatus.setStatus("current")
_HwMcTrunkTraps_ObjectIdentity = ObjectIdentity
hwMcTrunkTraps = _HwMcTrunkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2)
)
_HwMcTrunkConformance_ObjectIdentity = ObjectIdentity
hwMcTrunkConformance = _HwMcTrunkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3)
)
_HwMcTrunkCompliances_ObjectIdentity = ObjectIdentity
hwMcTrunkCompliances = _HwMcTrunkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 1)
)
_HwMcTrunkGroups_ObjectIdentity = ObjectIdentity
hwMcTrunkGroups = _HwMcTrunkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2)
)

# Managed Objects groups

hwMcTrunkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 1)
)
hwMcTrunkGroup.setObjects(
      *(("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkSystemId"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkPri"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkStatus"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkStatusReason"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkPeerIpAddr"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkSourceIpAddr"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkReceiveFailTimeMultiple"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkSendPeriod"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkPacketReceive"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkPacketSend"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkPacketRecDrop"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkPacketSndDrop"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkPeerSystemId"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkPeerPri"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkPeerReceiveFailTime"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkSecurityKeyType"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkSecurityKey"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkBfdSessId"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkResetCounter"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkRevertTime"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkRowStatus"))
)
if mibBuilder.loadTexts:
    hwMcTrunkGroup.setStatus("current")

hwMcTrunkMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 2)
)
hwMcTrunkMemberGroup.setObjects(
      *(("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkMemberStatus"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkMemberStatusReason"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkMemberWorkMode"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkMemberPhyStatus"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkMemberRowStatus"))
)
if mibBuilder.loadTexts:
    hwMcTrunkMemberGroup.setStatus("current")


# Notification objects

hwMcTrunkStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2, 1)
)
hwMcTrunkStatusChange.setObjects(
      *(("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkStatus"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkStatusReason"))
)
if mibBuilder.loadTexts:
    hwMcTrunkStatusChange.setStatus(
        "current"
    )

hwMcTrunkMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2, 2)
)
hwMcTrunkMemberStatusChange.setObjects(
      *(("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkMemberStatus"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkMemberStatusReason"))
)
if mibBuilder.loadTexts:
    hwMcTrunkMemberStatusChange.setStatus(
        "current"
    )


# Notifications groups

hwMcTrunkNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 3)
)
hwMcTrunkNotificationGroup.setObjects(
      *(("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkStatusChange"),
        ("HUAWEI-MC-TRUNK-MIB", "hwMcTrunkMemberStatusChange"))
)
if mibBuilder.loadTexts:
    hwMcTrunkNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwMcTrunkFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwMcTrunkFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MC-TRUNK-MIB",
    **{"hwDatacomm": hwDatacomm,
       "hwMcTrunkMIB": hwMcTrunkMIB,
       "hwMcTrunkObjects": hwMcTrunkObjects,
       "hwMcTrunkTable": hwMcTrunkTable,
       "hwMcTrunkEntry": hwMcTrunkEntry,
       "hwMcTrunkId": hwMcTrunkId,
       "hwMcTrunkSystemId": hwMcTrunkSystemId,
       "hwMcTrunkPri": hwMcTrunkPri,
       "hwMcTrunkStatus": hwMcTrunkStatus,
       "hwMcTrunkStatusReason": hwMcTrunkStatusReason,
       "hwMcTrunkPeerIpAddr": hwMcTrunkPeerIpAddr,
       "hwMcTrunkSourceIpAddr": hwMcTrunkSourceIpAddr,
       "hwMcTrunkReceiveFailTimeMultiple": hwMcTrunkReceiveFailTimeMultiple,
       "hwMcTrunkSendPeriod": hwMcTrunkSendPeriod,
       "hwMcTrunkPacketReceive": hwMcTrunkPacketReceive,
       "hwMcTrunkPacketSend": hwMcTrunkPacketSend,
       "hwMcTrunkPacketRecDrop": hwMcTrunkPacketRecDrop,
       "hwMcTrunkPacketSndDrop": hwMcTrunkPacketSndDrop,
       "hwMcTrunkPeerSystemId": hwMcTrunkPeerSystemId,
       "hwMcTrunkPeerPri": hwMcTrunkPeerPri,
       "hwMcTrunkPeerReceiveFailTime": hwMcTrunkPeerReceiveFailTime,
       "hwMcTrunkSecurityKeyType": hwMcTrunkSecurityKeyType,
       "hwMcTrunkSecurityKey": hwMcTrunkSecurityKey,
       "hwMcTrunkBfdSessId": hwMcTrunkBfdSessId,
       "hwMcTrunkResetCounter": hwMcTrunkResetCounter,
       "hwMcTrunkRevertTime": hwMcTrunkRevertTime,
       "hwMcTrunkRowStatus": hwMcTrunkRowStatus,
       "hwMcTrunkMemberTable": hwMcTrunkMemberTable,
       "hwMcTrunkMemberEntry": hwMcTrunkMemberEntry,
       "hwMcTrunkMemberParentId": hwMcTrunkMemberParentId,
       "hwMcTrunkMemberType": hwMcTrunkMemberType,
       "hwMcTrunkMemberId": hwMcTrunkMemberId,
       "hwMcTrunkMemberStatus": hwMcTrunkMemberStatus,
       "hwMcTrunkMemberStatusReason": hwMcTrunkMemberStatusReason,
       "hwMcTrunkMemberWorkMode": hwMcTrunkMemberWorkMode,
       "hwMcTrunkMemberPhyStatus": hwMcTrunkMemberPhyStatus,
       "hwMcTrunkMemberRowStatus": hwMcTrunkMemberRowStatus,
       "hwMcTrunkTraps": hwMcTrunkTraps,
       "hwMcTrunkStatusChange": hwMcTrunkStatusChange,
       "hwMcTrunkMemberStatusChange": hwMcTrunkMemberStatusChange,
       "hwMcTrunkConformance": hwMcTrunkConformance,
       "hwMcTrunkCompliances": hwMcTrunkCompliances,
       "hwMcTrunkFullCompliance": hwMcTrunkFullCompliance,
       "hwMcTrunkGroups": hwMcTrunkGroups,
       "hwMcTrunkGroup": hwMcTrunkGroup,
       "hwMcTrunkMemberGroup": hwMcTrunkMemberGroup,
       "hwMcTrunkNotificationGroup": hwMcTrunkNotificationGroup}
)
