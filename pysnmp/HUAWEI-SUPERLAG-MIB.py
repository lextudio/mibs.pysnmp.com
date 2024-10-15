# SNMP MIB module (HUAWEI-SUPERLAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SUPERLAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:02 2024
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

hwSuperLagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwDatacomm_ObjectIdentity = ObjectIdentity
hwDatacomm = _HwDatacomm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25)
)
_HwSuperLagObjects_ObjectIdentity = ObjectIdentity
hwSuperLagObjects = _HwSuperLagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1)
)
_HwSuperLagTable_Object = MibTable
hwSuperLagTable = _HwSuperLagTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1)
)
if mibBuilder.loadTexts:
    hwSuperLagTable.setStatus("current")
_HwSuperLagEntry_Object = MibTableRow
hwSuperLagEntry = _HwSuperLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1)
)
hwSuperLagEntry.setIndexNames(
    (0, "HUAWEI-SUPERLAG-MIB", "hwSuperLagId"),
)
if mibBuilder.loadTexts:
    hwSuperLagEntry.setStatus("current")


class _HwSuperLagId_Type(Integer32):
    """Custom type hwSuperLagId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwSuperLagId_Type.__name__ = "Integer32"
_HwSuperLagId_Object = MibTableColumn
hwSuperLagId = _HwSuperLagId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 1),
    _HwSuperLagId_Type()
)
hwSuperLagId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSuperLagId.setStatus("current")
_HwSuperLagSystemId_Type = PhysAddress
_HwSuperLagSystemId_Object = MibTableColumn
hwSuperLagSystemId = _HwSuperLagSystemId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 2),
    _HwSuperLagSystemId_Type()
)
hwSuperLagSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSuperLagSystemId.setStatus("current")


class _HwSuperLagPri_Type(Integer32):
    """Custom type hwSuperLagPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HwSuperLagPri_Type.__name__ = "Integer32"
_HwSuperLagPri_Object = MibTableColumn
hwSuperLagPri = _HwSuperLagPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 3),
    _HwSuperLagPri_Type()
)
hwSuperLagPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSuperLagPri.setStatus("current")


class _HwSuperLagStatus_Type(Integer32):
    """Custom type hwSuperLagStatus based on Integer32"""
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


_HwSuperLagStatus_Type.__name__ = "Integer32"
_HwSuperLagStatus_Object = MibTableColumn
hwSuperLagStatus = _HwSuperLagStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 4),
    _HwSuperLagStatus_Type()
)
hwSuperLagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSuperLagStatus.setStatus("current")


class _HwSuperLagStatusReason_Type(Integer32):
    """Custom type hwSuperLagStatusReason based on Integer32"""
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


_HwSuperLagStatusReason_Type.__name__ = "Integer32"
_HwSuperLagStatusReason_Object = MibTableColumn
hwSuperLagStatusReason = _HwSuperLagStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 5),
    _HwSuperLagStatusReason_Type()
)
hwSuperLagStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSuperLagStatusReason.setStatus("current")
_HwSuperLagPeerIpAddr_Type = IpAddress
_HwSuperLagPeerIpAddr_Object = MibTableColumn
hwSuperLagPeerIpAddr = _HwSuperLagPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 6),
    _HwSuperLagPeerIpAddr_Type()
)
hwSuperLagPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSuperLagPeerIpAddr.setStatus("current")
_HwSuperLagSourceIpAddr_Type = IpAddress
_HwSuperLagSourceIpAddr_Object = MibTableColumn
hwSuperLagSourceIpAddr = _HwSuperLagSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 7),
    _HwSuperLagSourceIpAddr_Type()
)
hwSuperLagSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSuperLagSourceIpAddr.setStatus("current")


class _HwSuperLagReceiveFailTimeMultiple_Type(Integer32):
    """Custom type hwSuperLagReceiveFailTimeMultiple based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_HwSuperLagReceiveFailTimeMultiple_Type.__name__ = "Integer32"
_HwSuperLagReceiveFailTimeMultiple_Object = MibTableColumn
hwSuperLagReceiveFailTimeMultiple = _HwSuperLagReceiveFailTimeMultiple_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 8),
    _HwSuperLagReceiveFailTimeMultiple_Type()
)
hwSuperLagReceiveFailTimeMultiple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSuperLagReceiveFailTimeMultiple.setStatus("current")


class _HwSuperLagSendPeriod_Type(Integer32):
    """Custom type hwSuperLagSendPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_HwSuperLagSendPeriod_Type.__name__ = "Integer32"
_HwSuperLagSendPeriod_Object = MibTableColumn
hwSuperLagSendPeriod = _HwSuperLagSendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 9),
    _HwSuperLagSendPeriod_Type()
)
hwSuperLagSendPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSuperLagSendPeriod.setStatus("current")
_HwSuperLagPacketReceive_Type = Counter64
_HwSuperLagPacketReceive_Object = MibTableColumn
hwSuperLagPacketReceive = _HwSuperLagPacketReceive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 10),
    _HwSuperLagPacketReceive_Type()
)
hwSuperLagPacketReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSuperLagPacketReceive.setStatus("current")
_HwSuperLagPacketSend_Type = Counter64
_HwSuperLagPacketSend_Object = MibTableColumn
hwSuperLagPacketSend = _HwSuperLagPacketSend_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 11),
    _HwSuperLagPacketSend_Type()
)
hwSuperLagPacketSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSuperLagPacketSend.setStatus("current")
_HwSuperLagPacketRecDrop_Type = Counter64
_HwSuperLagPacketRecDrop_Object = MibTableColumn
hwSuperLagPacketRecDrop = _HwSuperLagPacketRecDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 12),
    _HwSuperLagPacketRecDrop_Type()
)
hwSuperLagPacketRecDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSuperLagPacketRecDrop.setStatus("current")
_HwSuperLagPacketSndDrop_Type = Counter64
_HwSuperLagPacketSndDrop_Object = MibTableColumn
hwSuperLagPacketSndDrop = _HwSuperLagPacketSndDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 13),
    _HwSuperLagPacketSndDrop_Type()
)
hwSuperLagPacketSndDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSuperLagPacketSndDrop.setStatus("current")
_HwSuperLagPeerSystemId_Type = PhysAddress
_HwSuperLagPeerSystemId_Object = MibTableColumn
hwSuperLagPeerSystemId = _HwSuperLagPeerSystemId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 14),
    _HwSuperLagPeerSystemId_Type()
)
hwSuperLagPeerSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSuperLagPeerSystemId.setStatus("current")


class _HwSuperLagPeerPri_Type(Integer32):
    """Custom type hwSuperLagPeerPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HwSuperLagPeerPri_Type.__name__ = "Integer32"
_HwSuperLagPeerPri_Object = MibTableColumn
hwSuperLagPeerPri = _HwSuperLagPeerPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 15),
    _HwSuperLagPeerPri_Type()
)
hwSuperLagPeerPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSuperLagPeerPri.setStatus("current")


class _HwSuperLagPeerReceiveFailTime_Type(Integer32):
    """Custom type hwSuperLagPeerReceiveFailTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 5000),
    )


_HwSuperLagPeerReceiveFailTime_Type.__name__ = "Integer32"
_HwSuperLagPeerReceiveFailTime_Object = MibTableColumn
hwSuperLagPeerReceiveFailTime = _HwSuperLagPeerReceiveFailTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 16),
    _HwSuperLagPeerReceiveFailTime_Type()
)
hwSuperLagPeerReceiveFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSuperLagPeerReceiveFailTime.setStatus("current")


class _HwSuperLagSecurityKeyType_Type(Integer32):
    """Custom type hwSuperLagSecurityKeyType based on Integer32"""
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


_HwSuperLagSecurityKeyType_Type.__name__ = "Integer32"
_HwSuperLagSecurityKeyType_Object = MibTableColumn
hwSuperLagSecurityKeyType = _HwSuperLagSecurityKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 17),
    _HwSuperLagSecurityKeyType_Type()
)
hwSuperLagSecurityKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSuperLagSecurityKeyType.setStatus("current")


class _HwSuperLagSecurityKey_Type(OctetString):
    """Custom type hwSuperLagSecurityKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_HwSuperLagSecurityKey_Type.__name__ = "OctetString"
_HwSuperLagSecurityKey_Object = MibTableColumn
hwSuperLagSecurityKey = _HwSuperLagSecurityKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 18),
    _HwSuperLagSecurityKey_Type()
)
hwSuperLagSecurityKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSuperLagSecurityKey.setStatus("current")


class _HwSuperLagBfdSessId_Type(Integer32):
    """Custom type hwSuperLagBfdSessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_HwSuperLagBfdSessId_Type.__name__ = "Integer32"
_HwSuperLagBfdSessId_Object = MibTableColumn
hwSuperLagBfdSessId = _HwSuperLagBfdSessId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 19),
    _HwSuperLagBfdSessId_Type()
)
hwSuperLagBfdSessId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSuperLagBfdSessId.setStatus("current")


class _HwSuperLagResetCounter_Type(Integer32):
    """Custom type hwSuperLagResetCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_HwSuperLagResetCounter_Type.__name__ = "Integer32"
_HwSuperLagResetCounter_Object = MibTableColumn
hwSuperLagResetCounter = _HwSuperLagResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 20),
    _HwSuperLagResetCounter_Type()
)
hwSuperLagResetCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSuperLagResetCounter.setStatus("current")
_HwSuperLagRowStatus_Type = RowStatus
_HwSuperLagRowStatus_Object = MibTableColumn
hwSuperLagRowStatus = _HwSuperLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 50),
    _HwSuperLagRowStatus_Type()
)
hwSuperLagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSuperLagRowStatus.setStatus("current")
_HwSuperLagMemberTable_Object = MibTable
hwSuperLagMemberTable = _HwSuperLagMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2)
)
if mibBuilder.loadTexts:
    hwSuperLagMemberTable.setStatus("current")
_HwSuperLagMemberEntry_Object = MibTableRow
hwSuperLagMemberEntry = _HwSuperLagMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1)
)
hwSuperLagMemberEntry.setIndexNames(
    (0, "HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberParentSuperLagId"),
    (0, "HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberType"),
    (0, "HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberId"),
)
if mibBuilder.loadTexts:
    hwSuperLagMemberEntry.setStatus("current")


class _HwSuperLagMemberParentSuperLagId_Type(Integer32):
    """Custom type hwSuperLagMemberParentSuperLagId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwSuperLagMemberParentSuperLagId_Type.__name__ = "Integer32"
_HwSuperLagMemberParentSuperLagId_Object = MibTableColumn
hwSuperLagMemberParentSuperLagId = _HwSuperLagMemberParentSuperLagId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 1),
    _HwSuperLagMemberParentSuperLagId_Type()
)
hwSuperLagMemberParentSuperLagId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSuperLagMemberParentSuperLagId.setStatus("current")


class _HwSuperLagMemberType_Type(Integer32):
    """Custom type hwSuperLagMemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwSuperLagMemberType_Type.__name__ = "Integer32"
_HwSuperLagMemberType_Object = MibTableColumn
hwSuperLagMemberType = _HwSuperLagMemberType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 2),
    _HwSuperLagMemberType_Type()
)
hwSuperLagMemberType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSuperLagMemberType.setStatus("current")
_HwSuperLagMemberId_Type = Unsigned32
_HwSuperLagMemberId_Object = MibTableColumn
hwSuperLagMemberId = _HwSuperLagMemberId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 3),
    _HwSuperLagMemberId_Type()
)
hwSuperLagMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSuperLagMemberId.setStatus("current")


class _HwSuperLagMemberStatus_Type(Integer32):
    """Custom type hwSuperLagMemberStatus based on Integer32"""
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


_HwSuperLagMemberStatus_Type.__name__ = "Integer32"
_HwSuperLagMemberStatus_Object = MibTableColumn
hwSuperLagMemberStatus = _HwSuperLagMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 4),
    _HwSuperLagMemberStatus_Type()
)
hwSuperLagMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSuperLagMemberStatus.setStatus("current")


class _HwSuperLagMemberStatusReason_Type(Integer32):
    """Custom type hwSuperLagMemberStatusReason based on Integer32"""
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
          ("peerMemberDown", 6),
          ("peerMemberUp", 7),
          ("suplagBackup", 4),
          ("suplagInit", 3),
          ("suplagMaster", 5))
    )


_HwSuperLagMemberStatusReason_Type.__name__ = "Integer32"
_HwSuperLagMemberStatusReason_Object = MibTableColumn
hwSuperLagMemberStatusReason = _HwSuperLagMemberStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 5),
    _HwSuperLagMemberStatusReason_Type()
)
hwSuperLagMemberStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSuperLagMemberStatusReason.setStatus("current")


class _HwSuperLagMemberWorkMode_Type(Integer32):
    """Custom type hwSuperLagMemberWorkMode based on Integer32"""
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


_HwSuperLagMemberWorkMode_Type.__name__ = "Integer32"
_HwSuperLagMemberWorkMode_Object = MibTableColumn
hwSuperLagMemberWorkMode = _HwSuperLagMemberWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 6),
    _HwSuperLagMemberWorkMode_Type()
)
hwSuperLagMemberWorkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSuperLagMemberWorkMode.setStatus("current")


class _HwSuperLagMemberLocaPhylLinkStatus_Type(Integer32):
    """Custom type hwSuperLagMemberLocaPhylLinkStatus based on Integer32"""
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


_HwSuperLagMemberLocaPhylLinkStatus_Type.__name__ = "Integer32"
_HwSuperLagMemberLocaPhylLinkStatus_Object = MibTableColumn
hwSuperLagMemberLocaPhylLinkStatus = _HwSuperLagMemberLocaPhylLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 7),
    _HwSuperLagMemberLocaPhylLinkStatus_Type()
)
hwSuperLagMemberLocaPhylLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSuperLagMemberLocaPhylLinkStatus.setStatus("current")
_HwSuperLagMemberRowStatus_Type = RowStatus
_HwSuperLagMemberRowStatus_Object = MibTableColumn
hwSuperLagMemberRowStatus = _HwSuperLagMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 50),
    _HwSuperLagMemberRowStatus_Type()
)
hwSuperLagMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSuperLagMemberRowStatus.setStatus("current")
_HwSuperLagTraps_ObjectIdentity = ObjectIdentity
hwSuperLagTraps = _HwSuperLagTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2)
)
_HwSuperLagConformance_ObjectIdentity = ObjectIdentity
hwSuperLagConformance = _HwSuperLagConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3)
)
_HwSuperLagCompliances_ObjectIdentity = ObjectIdentity
hwSuperLagCompliances = _HwSuperLagCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 1)
)
_HwSuperLagGroups_ObjectIdentity = ObjectIdentity
hwSuperLagGroups = _HwSuperLagGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2)
)

# Managed Objects groups

hwSuperLagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 1)
)
hwSuperLagGroup.setObjects(
      *(("HUAWEI-SUPERLAG-MIB", "hwSuperLagSystemId"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPri"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatus"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatusReason"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPeerIpAddr"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagSourceIpAddr"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagReceiveFailTimeMultiple"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagSendPeriod"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPacketReceive"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPacketSend"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPacketRecDrop"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPacketSndDrop"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPeerSystemId"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPeerPri"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagPeerReceiveFailTime"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagSecurityKeyType"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagSecurityKey"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagBfdSessId"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagResetCounter"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagRowStatus"))
)
if mibBuilder.loadTexts:
    hwSuperLagGroup.setStatus("current")

hwSuperLagMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 2)
)
hwSuperLagMemberGroup.setObjects(
      *(("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatus"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatusReason"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberWorkMode"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberLocaPhylLinkStatus"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberRowStatus"))
)
if mibBuilder.loadTexts:
    hwSuperLagMemberGroup.setStatus("current")


# Notification objects

hwSuperLagStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2, 1)
)
hwSuperLagStatusChange.setObjects(
      *(("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatus"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatusReason"))
)
if mibBuilder.loadTexts:
    hwSuperLagStatusChange.setStatus(
        "current"
    )

hwSuperLagMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2, 2)
)
hwSuperLagMemberStatusChange.setObjects(
      *(("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatus"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatusReason"))
)
if mibBuilder.loadTexts:
    hwSuperLagMemberStatusChange.setStatus(
        "current"
    )


# Notifications groups

hwSuperLagNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 3)
)
hwSuperLagNotificationGroup.setObjects(
      *(("HUAWEI-SUPERLAG-MIB", "hwSuperLagStatusChange"),
        ("HUAWEI-SUPERLAG-MIB", "hwSuperLagMemberStatusChange"))
)
if mibBuilder.loadTexts:
    hwSuperLagNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwSuperLagFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwSuperLagFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SUPERLAG-MIB",
    **{"hwDatacomm": hwDatacomm,
       "hwSuperLagMIB": hwSuperLagMIB,
       "hwSuperLagObjects": hwSuperLagObjects,
       "hwSuperLagTable": hwSuperLagTable,
       "hwSuperLagEntry": hwSuperLagEntry,
       "hwSuperLagId": hwSuperLagId,
       "hwSuperLagSystemId": hwSuperLagSystemId,
       "hwSuperLagPri": hwSuperLagPri,
       "hwSuperLagStatus": hwSuperLagStatus,
       "hwSuperLagStatusReason": hwSuperLagStatusReason,
       "hwSuperLagPeerIpAddr": hwSuperLagPeerIpAddr,
       "hwSuperLagSourceIpAddr": hwSuperLagSourceIpAddr,
       "hwSuperLagReceiveFailTimeMultiple": hwSuperLagReceiveFailTimeMultiple,
       "hwSuperLagSendPeriod": hwSuperLagSendPeriod,
       "hwSuperLagPacketReceive": hwSuperLagPacketReceive,
       "hwSuperLagPacketSend": hwSuperLagPacketSend,
       "hwSuperLagPacketRecDrop": hwSuperLagPacketRecDrop,
       "hwSuperLagPacketSndDrop": hwSuperLagPacketSndDrop,
       "hwSuperLagPeerSystemId": hwSuperLagPeerSystemId,
       "hwSuperLagPeerPri": hwSuperLagPeerPri,
       "hwSuperLagPeerReceiveFailTime": hwSuperLagPeerReceiveFailTime,
       "hwSuperLagSecurityKeyType": hwSuperLagSecurityKeyType,
       "hwSuperLagSecurityKey": hwSuperLagSecurityKey,
       "hwSuperLagBfdSessId": hwSuperLagBfdSessId,
       "hwSuperLagResetCounter": hwSuperLagResetCounter,
       "hwSuperLagRowStatus": hwSuperLagRowStatus,
       "hwSuperLagMemberTable": hwSuperLagMemberTable,
       "hwSuperLagMemberEntry": hwSuperLagMemberEntry,
       "hwSuperLagMemberParentSuperLagId": hwSuperLagMemberParentSuperLagId,
       "hwSuperLagMemberType": hwSuperLagMemberType,
       "hwSuperLagMemberId": hwSuperLagMemberId,
       "hwSuperLagMemberStatus": hwSuperLagMemberStatus,
       "hwSuperLagMemberStatusReason": hwSuperLagMemberStatusReason,
       "hwSuperLagMemberWorkMode": hwSuperLagMemberWorkMode,
       "hwSuperLagMemberLocaPhylLinkStatus": hwSuperLagMemberLocaPhylLinkStatus,
       "hwSuperLagMemberRowStatus": hwSuperLagMemberRowStatus,
       "hwSuperLagTraps": hwSuperLagTraps,
       "hwSuperLagStatusChange": hwSuperLagStatusChange,
       "hwSuperLagMemberStatusChange": hwSuperLagMemberStatusChange,
       "hwSuperLagConformance": hwSuperLagConformance,
       "hwSuperLagCompliances": hwSuperLagCompliances,
       "hwSuperLagFullCompliance": hwSuperLagFullCompliance,
       "hwSuperLagGroups": hwSuperLagGroups,
       "hwSuperLagGroup": hwSuperLagGroup,
       "hwSuperLagMemberGroup": hwSuperLagMemberGroup,
       "hwSuperLagNotificationGroup": hwSuperLagNotificationGroup}
)
