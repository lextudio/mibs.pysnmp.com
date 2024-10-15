# SNMP MIB module (HUAWEI-E-TRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-E-TRUNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:37 2024
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

hwETrunkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwDatacomm_ObjectIdentity = ObjectIdentity
hwDatacomm = _HwDatacomm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25)
)
_HwETrunkObjects_ObjectIdentity = ObjectIdentity
hwETrunkObjects = _HwETrunkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1)
)
_HwETrunkTable_Object = MibTable
hwETrunkTable = _HwETrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1)
)
if mibBuilder.loadTexts:
    hwETrunkTable.setStatus("current")
_HwETrunkEntry_Object = MibTableRow
hwETrunkEntry = _HwETrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1)
)
hwETrunkEntry.setIndexNames(
    (0, "HUAWEI-E-TRUNK-MIB", "hwETrunkId"),
)
if mibBuilder.loadTexts:
    hwETrunkEntry.setStatus("current")


class _HwETrunkId_Type(Integer32):
    """Custom type hwETrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwETrunkId_Type.__name__ = "Integer32"
_HwETrunkId_Object = MibTableColumn
hwETrunkId = _HwETrunkId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 1),
    _HwETrunkId_Type()
)
hwETrunkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwETrunkId.setStatus("current")
_HwETrunkSystemId_Type = PhysAddress
_HwETrunkSystemId_Object = MibTableColumn
hwETrunkSystemId = _HwETrunkSystemId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 2),
    _HwETrunkSystemId_Type()
)
hwETrunkSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwETrunkSystemId.setStatus("current")


class _HwETrunkPri_Type(Integer32):
    """Custom type hwETrunkPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HwETrunkPri_Type.__name__ = "Integer32"
_HwETrunkPri_Object = MibTableColumn
hwETrunkPri = _HwETrunkPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 3),
    _HwETrunkPri_Type()
)
hwETrunkPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkPri.setStatus("current")


class _HwETrunkStatus_Type(Integer32):
    """Custom type hwETrunkStatus based on Integer32"""
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


_HwETrunkStatus_Type.__name__ = "Integer32"
_HwETrunkStatus_Object = MibTableColumn
hwETrunkStatus = _HwETrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 4),
    _HwETrunkStatus_Type()
)
hwETrunkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwETrunkStatus.setStatus("current")


class _HwETrunkStatusReason_Type(Integer32):
    """Custom type hwETrunkStatusReason based on Integer32"""
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


_HwETrunkStatusReason_Type.__name__ = "Integer32"
_HwETrunkStatusReason_Object = MibTableColumn
hwETrunkStatusReason = _HwETrunkStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 5),
    _HwETrunkStatusReason_Type()
)
hwETrunkStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwETrunkStatusReason.setStatus("current")
_HwETrunkPeerIpAddr_Type = IpAddress
_HwETrunkPeerIpAddr_Object = MibTableColumn
hwETrunkPeerIpAddr = _HwETrunkPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 6),
    _HwETrunkPeerIpAddr_Type()
)
hwETrunkPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkPeerIpAddr.setStatus("current")
_HwETrunkSourceIpAddr_Type = IpAddress
_HwETrunkSourceIpAddr_Object = MibTableColumn
hwETrunkSourceIpAddr = _HwETrunkSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 7),
    _HwETrunkSourceIpAddr_Type()
)
hwETrunkSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkSourceIpAddr.setStatus("current")


class _HwETrunkReceiveFailTimeMultiple_Type(Integer32):
    """Custom type hwETrunkReceiveFailTimeMultiple based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 300),
    )


_HwETrunkReceiveFailTimeMultiple_Type.__name__ = "Integer32"
_HwETrunkReceiveFailTimeMultiple_Object = MibTableColumn
hwETrunkReceiveFailTimeMultiple = _HwETrunkReceiveFailTimeMultiple_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 8),
    _HwETrunkReceiveFailTimeMultiple_Type()
)
hwETrunkReceiveFailTimeMultiple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkReceiveFailTimeMultiple.setStatus("current")


class _HwETrunkSendPeriod_Type(Integer32):
    """Custom type hwETrunkSendPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_HwETrunkSendPeriod_Type.__name__ = "Integer32"
_HwETrunkSendPeriod_Object = MibTableColumn
hwETrunkSendPeriod = _HwETrunkSendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 9),
    _HwETrunkSendPeriod_Type()
)
hwETrunkSendPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkSendPeriod.setStatus("current")
_HwETrunkPacketReceive_Type = Counter64
_HwETrunkPacketReceive_Object = MibTableColumn
hwETrunkPacketReceive = _HwETrunkPacketReceive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 10),
    _HwETrunkPacketReceive_Type()
)
hwETrunkPacketReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwETrunkPacketReceive.setStatus("current")
_HwETrunkPacketSend_Type = Counter64
_HwETrunkPacketSend_Object = MibTableColumn
hwETrunkPacketSend = _HwETrunkPacketSend_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 11),
    _HwETrunkPacketSend_Type()
)
hwETrunkPacketSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwETrunkPacketSend.setStatus("current")
_HwETrunkPacketRecDrop_Type = Counter64
_HwETrunkPacketRecDrop_Object = MibTableColumn
hwETrunkPacketRecDrop = _HwETrunkPacketRecDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 12),
    _HwETrunkPacketRecDrop_Type()
)
hwETrunkPacketRecDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwETrunkPacketRecDrop.setStatus("current")
_HwETrunkPacketSndDrop_Type = Counter64
_HwETrunkPacketSndDrop_Object = MibTableColumn
hwETrunkPacketSndDrop = _HwETrunkPacketSndDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 13),
    _HwETrunkPacketSndDrop_Type()
)
hwETrunkPacketSndDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwETrunkPacketSndDrop.setStatus("current")
_HwETrunkPeerSystemId_Type = PhysAddress
_HwETrunkPeerSystemId_Object = MibTableColumn
hwETrunkPeerSystemId = _HwETrunkPeerSystemId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 14),
    _HwETrunkPeerSystemId_Type()
)
hwETrunkPeerSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwETrunkPeerSystemId.setStatus("current")


class _HwETrunkPeerPri_Type(Integer32):
    """Custom type hwETrunkPeerPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HwETrunkPeerPri_Type.__name__ = "Integer32"
_HwETrunkPeerPri_Object = MibTableColumn
hwETrunkPeerPri = _HwETrunkPeerPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 15),
    _HwETrunkPeerPri_Type()
)
hwETrunkPeerPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwETrunkPeerPri.setStatus("current")


class _HwETrunkPeerReceiveFailTime_Type(Integer32):
    """Custom type hwETrunkPeerReceiveFailTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 30000),
    )


_HwETrunkPeerReceiveFailTime_Type.__name__ = "Integer32"
_HwETrunkPeerReceiveFailTime_Object = MibTableColumn
hwETrunkPeerReceiveFailTime = _HwETrunkPeerReceiveFailTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 16),
    _HwETrunkPeerReceiveFailTime_Type()
)
hwETrunkPeerReceiveFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwETrunkPeerReceiveFailTime.setStatus("current")


class _HwETrunkSecurityKeyType_Type(Integer32):
    """Custom type hwETrunkSecurityKeyType based on Integer32"""
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


_HwETrunkSecurityKeyType_Type.__name__ = "Integer32"
_HwETrunkSecurityKeyType_Object = MibTableColumn
hwETrunkSecurityKeyType = _HwETrunkSecurityKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 17),
    _HwETrunkSecurityKeyType_Type()
)
hwETrunkSecurityKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkSecurityKeyType.setStatus("current")


class _HwETrunkSecurityKey_Type(OctetString):
    """Custom type hwETrunkSecurityKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 392),
    )


_HwETrunkSecurityKey_Type.__name__ = "OctetString"
_HwETrunkSecurityKey_Object = MibTableColumn
hwETrunkSecurityKey = _HwETrunkSecurityKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 18),
    _HwETrunkSecurityKey_Type()
)
hwETrunkSecurityKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkSecurityKey.setStatus("current")


class _HwETrunkBfdSessId_Type(Integer32):
    """Custom type hwETrunkBfdSessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_HwETrunkBfdSessId_Type.__name__ = "Integer32"
_HwETrunkBfdSessId_Object = MibTableColumn
hwETrunkBfdSessId = _HwETrunkBfdSessId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 19),
    _HwETrunkBfdSessId_Type()
)
hwETrunkBfdSessId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkBfdSessId.setStatus("current")


class _HwETrunkResetCounter_Type(Integer32):
    """Custom type hwETrunkResetCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_HwETrunkResetCounter_Type.__name__ = "Integer32"
_HwETrunkResetCounter_Object = MibTableColumn
hwETrunkResetCounter = _HwETrunkResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 20),
    _HwETrunkResetCounter_Type()
)
hwETrunkResetCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkResetCounter.setStatus("current")


class _HwETrunkRevertTime_Type(Integer32):
    """Custom type hwETrunkRevertTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_HwETrunkRevertTime_Type.__name__ = "Integer32"
_HwETrunkRevertTime_Object = MibTableColumn
hwETrunkRevertTime = _HwETrunkRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 21),
    _HwETrunkRevertTime_Type()
)
hwETrunkRevertTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkRevertTime.setStatus("current")


class _HwETrunkBfdSessName_Type(OctetString):
    """Custom type hwETrunkBfdSessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HwETrunkBfdSessName_Type.__name__ = "OctetString"
_HwETrunkBfdSessName_Object = MibTableColumn
hwETrunkBfdSessName = _HwETrunkBfdSessName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 22),
    _HwETrunkBfdSessName_Type()
)
hwETrunkBfdSessName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkBfdSessName.setStatus("current")


class _HwETrunkDescription_Type(OctetString):
    """Custom type hwETrunkDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 242),
    )


_HwETrunkDescription_Type.__name__ = "OctetString"
_HwETrunkDescription_Object = MibTableColumn
hwETrunkDescription = _HwETrunkDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 23),
    _HwETrunkDescription_Type()
)
hwETrunkDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkDescription.setStatus("current")
_HwETrunkRowStatus_Type = RowStatus
_HwETrunkRowStatus_Object = MibTableColumn
hwETrunkRowStatus = _HwETrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 50),
    _HwETrunkRowStatus_Type()
)
hwETrunkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkRowStatus.setStatus("current")
_HwETrunkMemberTable_Object = MibTable
hwETrunkMemberTable = _HwETrunkMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2)
)
if mibBuilder.loadTexts:
    hwETrunkMemberTable.setStatus("current")
_HwETrunkMemberEntry_Object = MibTableRow
hwETrunkMemberEntry = _HwETrunkMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1)
)
hwETrunkMemberEntry.setIndexNames(
    (0, "HUAWEI-E-TRUNK-MIB", "hwETrunkMemberParentId"),
    (0, "HUAWEI-E-TRUNK-MIB", "hwETrunkMemberType"),
    (0, "HUAWEI-E-TRUNK-MIB", "hwETrunkMemberId"),
)
if mibBuilder.loadTexts:
    hwETrunkMemberEntry.setStatus("current")


class _HwETrunkMemberParentId_Type(Integer32):
    """Custom type hwETrunkMemberParentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwETrunkMemberParentId_Type.__name__ = "Integer32"
_HwETrunkMemberParentId_Object = MibTableColumn
hwETrunkMemberParentId = _HwETrunkMemberParentId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 1),
    _HwETrunkMemberParentId_Type()
)
hwETrunkMemberParentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwETrunkMemberParentId.setStatus("current")


class _HwETrunkMemberType_Type(Integer32):
    """Custom type hwETrunkMemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwETrunkMemberType_Type.__name__ = "Integer32"
_HwETrunkMemberType_Object = MibTableColumn
hwETrunkMemberType = _HwETrunkMemberType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 2),
    _HwETrunkMemberType_Type()
)
hwETrunkMemberType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwETrunkMemberType.setStatus("current")
_HwETrunkMemberId_Type = Unsigned32
_HwETrunkMemberId_Object = MibTableColumn
hwETrunkMemberId = _HwETrunkMemberId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 3),
    _HwETrunkMemberId_Type()
)
hwETrunkMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwETrunkMemberId.setStatus("current")


class _HwETrunkMemberStatus_Type(Integer32):
    """Custom type hwETrunkMemberStatus based on Integer32"""
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


_HwETrunkMemberStatus_Type.__name__ = "Integer32"
_HwETrunkMemberStatus_Object = MibTableColumn
hwETrunkMemberStatus = _HwETrunkMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 4),
    _HwETrunkMemberStatus_Type()
)
hwETrunkMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwETrunkMemberStatus.setStatus("current")


class _HwETrunkMemberStatusReason_Type(Integer32):
    """Custom type hwETrunkMemberStatusReason based on Integer32"""
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
        *(("etrunkBackup", 4),
          ("etrunkInit", 3),
          ("etrunkMaster", 5),
          ("forceBackup", 1),
          ("forceMaster", 2),
          ("peerMemberDown", 6),
          ("peerMemberUp", 7))
    )


_HwETrunkMemberStatusReason_Type.__name__ = "Integer32"
_HwETrunkMemberStatusReason_Object = MibTableColumn
hwETrunkMemberStatusReason = _HwETrunkMemberStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 5),
    _HwETrunkMemberStatusReason_Type()
)
hwETrunkMemberStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwETrunkMemberStatusReason.setStatus("current")


class _HwETrunkMemberWorkMode_Type(Integer32):
    """Custom type hwETrunkMemberWorkMode based on Integer32"""
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


_HwETrunkMemberWorkMode_Type.__name__ = "Integer32"
_HwETrunkMemberWorkMode_Object = MibTableColumn
hwETrunkMemberWorkMode = _HwETrunkMemberWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 6),
    _HwETrunkMemberWorkMode_Type()
)
hwETrunkMemberWorkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkMemberWorkMode.setStatus("current")


class _HwETrunkMemberPhyStatus_Type(Integer32):
    """Custom type hwETrunkMemberPhyStatus based on Integer32"""
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


_HwETrunkMemberPhyStatus_Type.__name__ = "Integer32"
_HwETrunkMemberPhyStatus_Object = MibTableColumn
hwETrunkMemberPhyStatus = _HwETrunkMemberPhyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 7),
    _HwETrunkMemberPhyStatus_Type()
)
hwETrunkMemberPhyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwETrunkMemberPhyStatus.setStatus("current")
_HwETrunkMemberRemoteId_Type = Unsigned32
_HwETrunkMemberRemoteId_Object = MibTableColumn
hwETrunkMemberRemoteId = _HwETrunkMemberRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 8),
    _HwETrunkMemberRemoteId_Type()
)
hwETrunkMemberRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkMemberRemoteId.setStatus("current")
_HwETrunkMemberRowStatus_Type = RowStatus
_HwETrunkMemberRowStatus_Object = MibTableColumn
hwETrunkMemberRowStatus = _HwETrunkMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 50),
    _HwETrunkMemberRowStatus_Type()
)
hwETrunkMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwETrunkMemberRowStatus.setStatus("current")
_HwETrunkTraps_ObjectIdentity = ObjectIdentity
hwETrunkTraps = _HwETrunkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2)
)
_HwETrunkConformance_ObjectIdentity = ObjectIdentity
hwETrunkConformance = _HwETrunkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3)
)
_HwETrunkCompliances_ObjectIdentity = ObjectIdentity
hwETrunkCompliances = _HwETrunkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 1)
)
_HwETrunkGroups_ObjectIdentity = ObjectIdentity
hwETrunkGroups = _HwETrunkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2)
)

# Managed Objects groups

hwETrunkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 1)
)
hwETrunkGroup.setObjects(
      *(("HUAWEI-E-TRUNK-MIB", "hwETrunkSystemId"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkPri"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkStatus"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkStatusReason"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkPeerIpAddr"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkSourceIpAddr"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkReceiveFailTimeMultiple"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkSendPeriod"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkPacketReceive"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkPacketSend"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkPacketRecDrop"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkPacketSndDrop"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkPeerSystemId"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkPeerPri"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkPeerReceiveFailTime"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkSecurityKeyType"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkSecurityKey"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkBfdSessId"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkResetCounter"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkRevertTime"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkBfdSessName"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkDescription"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkRowStatus"))
)
if mibBuilder.loadTexts:
    hwETrunkGroup.setStatus("current")

hwETrunkMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 2)
)
hwETrunkMemberGroup.setObjects(
      *(("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatus"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatusReason"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberWorkMode"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberPhyStatus"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberRemoteId"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberRowStatus"))
)
if mibBuilder.loadTexts:
    hwETrunkMemberGroup.setStatus("current")


# Notification objects

hwETrunkStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2, 1)
)
hwETrunkStatusChange.setObjects(
      *(("HUAWEI-E-TRUNK-MIB", "hwETrunkStatus"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkStatusReason"))
)
if mibBuilder.loadTexts:
    hwETrunkStatusChange.setStatus(
        "current"
    )

hwETrunkMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2, 2)
)
hwETrunkMemberStatusChange.setObjects(
      *(("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatus"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatusReason"))
)
if mibBuilder.loadTexts:
    hwETrunkMemberStatusChange.setStatus(
        "current"
    )


# Notifications groups

hwETrunkNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 3)
)
hwETrunkNotificationGroup.setObjects(
      *(("HUAWEI-E-TRUNK-MIB", "hwETrunkStatusChange"),
        ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatusChange"))
)
if mibBuilder.loadTexts:
    hwETrunkNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwETrunkFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwETrunkFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-E-TRUNK-MIB",
    **{"hwDatacomm": hwDatacomm,
       "hwETrunkMIB": hwETrunkMIB,
       "hwETrunkObjects": hwETrunkObjects,
       "hwETrunkTable": hwETrunkTable,
       "hwETrunkEntry": hwETrunkEntry,
       "hwETrunkId": hwETrunkId,
       "hwETrunkSystemId": hwETrunkSystemId,
       "hwETrunkPri": hwETrunkPri,
       "hwETrunkStatus": hwETrunkStatus,
       "hwETrunkStatusReason": hwETrunkStatusReason,
       "hwETrunkPeerIpAddr": hwETrunkPeerIpAddr,
       "hwETrunkSourceIpAddr": hwETrunkSourceIpAddr,
       "hwETrunkReceiveFailTimeMultiple": hwETrunkReceiveFailTimeMultiple,
       "hwETrunkSendPeriod": hwETrunkSendPeriod,
       "hwETrunkPacketReceive": hwETrunkPacketReceive,
       "hwETrunkPacketSend": hwETrunkPacketSend,
       "hwETrunkPacketRecDrop": hwETrunkPacketRecDrop,
       "hwETrunkPacketSndDrop": hwETrunkPacketSndDrop,
       "hwETrunkPeerSystemId": hwETrunkPeerSystemId,
       "hwETrunkPeerPri": hwETrunkPeerPri,
       "hwETrunkPeerReceiveFailTime": hwETrunkPeerReceiveFailTime,
       "hwETrunkSecurityKeyType": hwETrunkSecurityKeyType,
       "hwETrunkSecurityKey": hwETrunkSecurityKey,
       "hwETrunkBfdSessId": hwETrunkBfdSessId,
       "hwETrunkResetCounter": hwETrunkResetCounter,
       "hwETrunkRevertTime": hwETrunkRevertTime,
       "hwETrunkBfdSessName": hwETrunkBfdSessName,
       "hwETrunkDescription": hwETrunkDescription,
       "hwETrunkRowStatus": hwETrunkRowStatus,
       "hwETrunkMemberTable": hwETrunkMemberTable,
       "hwETrunkMemberEntry": hwETrunkMemberEntry,
       "hwETrunkMemberParentId": hwETrunkMemberParentId,
       "hwETrunkMemberType": hwETrunkMemberType,
       "hwETrunkMemberId": hwETrunkMemberId,
       "hwETrunkMemberStatus": hwETrunkMemberStatus,
       "hwETrunkMemberStatusReason": hwETrunkMemberStatusReason,
       "hwETrunkMemberWorkMode": hwETrunkMemberWorkMode,
       "hwETrunkMemberPhyStatus": hwETrunkMemberPhyStatus,
       "hwETrunkMemberRemoteId": hwETrunkMemberRemoteId,
       "hwETrunkMemberRowStatus": hwETrunkMemberRowStatus,
       "hwETrunkTraps": hwETrunkTraps,
       "hwETrunkStatusChange": hwETrunkStatusChange,
       "hwETrunkMemberStatusChange": hwETrunkMemberStatusChange,
       "hwETrunkConformance": hwETrunkConformance,
       "hwETrunkCompliances": hwETrunkCompliances,
       "hwETrunkFullCompliance": hwETrunkFullCompliance,
       "hwETrunkGroups": hwETrunkGroups,
       "hwETrunkGroup": hwETrunkGroup,
       "hwETrunkMemberGroup": hwETrunkMemberGroup,
       "hwETrunkNotificationGroup": hwETrunkNotificationGroup}
)
