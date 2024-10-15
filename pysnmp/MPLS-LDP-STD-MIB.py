# SNMP MIB module (MPLS-LDP-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-LDP-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:11 2024
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

(IndexInteger,
 IndexIntegerNextFree) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexInteger",
    "IndexIntegerNextFree")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(MplsIndexType,) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "MplsIndexType")

(MplsLabelDistributionMethod,
 MplsLdpIdentifier,
 MplsLdpLabelType,
 MplsLspType,
 MplsLsrIdentifier,
 MplsRetentionMode,
 mplsStdMIB) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLabelDistributionMethod",
    "MplsLdpIdentifier",
    "MplsLdpLabelType",
    "MplsLspType",
    "MplsLsrIdentifier",
    "MplsRetentionMode",
    "mplsStdMIB")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mplsLdpStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 4)
)
mplsLdpStdMIB.setRevisions(
        ("2004-06-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsLdpNotifications_ObjectIdentity = ObjectIdentity
mplsLdpNotifications = _MplsLdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 0)
)
_MplsLdpObjects_ObjectIdentity = ObjectIdentity
mplsLdpObjects = _MplsLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1)
)
_MplsLdpLsrObjects_ObjectIdentity = ObjectIdentity
mplsLdpLsrObjects = _MplsLdpLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 1)
)
_MplsLdpLsrId_Type = MplsLsrIdentifier
_MplsLdpLsrId_Object = MibScalar
mplsLdpLsrId = _MplsLdpLsrId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 1, 1),
    _MplsLdpLsrId_Type()
)
mplsLdpLsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLsrId.setStatus("current")


class _MplsLdpLsrLoopDetectionCapable_Type(Integer32):
    """Custom type mplsLdpLsrLoopDetectionCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("hopCount", 3),
          ("hopCountAndPathVector", 5),
          ("none", 1),
          ("other", 2),
          ("pathVector", 4))
    )


_MplsLdpLsrLoopDetectionCapable_Type.__name__ = "Integer32"
_MplsLdpLsrLoopDetectionCapable_Object = MibScalar
mplsLdpLsrLoopDetectionCapable = _MplsLdpLsrLoopDetectionCapable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 1, 2),
    _MplsLdpLsrLoopDetectionCapable_Type()
)
mplsLdpLsrLoopDetectionCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLsrLoopDetectionCapable.setStatus("current")
_MplsLdpEntityObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityObjects = _MplsLdpEntityObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2)
)
_MplsLdpEntityLastChange_Type = TimeStamp
_MplsLdpEntityLastChange_Object = MibScalar
mplsLdpEntityLastChange = _MplsLdpEntityLastChange_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 1),
    _MplsLdpEntityLastChange_Type()
)
mplsLdpEntityLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityLastChange.setStatus("current")
_MplsLdpEntityIndexNext_Type = IndexIntegerNextFree
_MplsLdpEntityIndexNext_Object = MibScalar
mplsLdpEntityIndexNext = _MplsLdpEntityIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 2),
    _MplsLdpEntityIndexNext_Type()
)
mplsLdpEntityIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityIndexNext.setStatus("current")
_MplsLdpEntityTable_Object = MibTable
mplsLdpEntityTable = _MplsLdpEntityTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mplsLdpEntityTable.setStatus("current")
_MplsLdpEntityEntry_Object = MibTableRow
mplsLdpEntityEntry = _MplsLdpEntityEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1)
)
mplsLdpEntityEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityEntry.setStatus("current")
_MplsLdpEntityLdpId_Type = MplsLdpIdentifier
_MplsLdpEntityLdpId_Object = MibTableColumn
mplsLdpEntityLdpId = _MplsLdpEntityLdpId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 1),
    _MplsLdpEntityLdpId_Type()
)
mplsLdpEntityLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityLdpId.setStatus("current")
_MplsLdpEntityIndex_Type = IndexInteger
_MplsLdpEntityIndex_Object = MibTableColumn
mplsLdpEntityIndex = _MplsLdpEntityIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 2),
    _MplsLdpEntityIndex_Type()
)
mplsLdpEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityIndex.setStatus("current")


class _MplsLdpEntityProtocolVersion_Type(Unsigned32):
    """Custom type mplsLdpEntityProtocolVersion based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpEntityProtocolVersion_Type.__name__ = "Unsigned32"
_MplsLdpEntityProtocolVersion_Object = MibTableColumn
mplsLdpEntityProtocolVersion = _MplsLdpEntityProtocolVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 3),
    _MplsLdpEntityProtocolVersion_Type()
)
mplsLdpEntityProtocolVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityProtocolVersion.setStatus("current")


class _MplsLdpEntityAdminStatus_Type(Integer32):
    """Custom type mplsLdpEntityAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MplsLdpEntityAdminStatus_Type.__name__ = "Integer32"
_MplsLdpEntityAdminStatus_Object = MibTableColumn
mplsLdpEntityAdminStatus = _MplsLdpEntityAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 4),
    _MplsLdpEntityAdminStatus_Type()
)
mplsLdpEntityAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAdminStatus.setStatus("current")


class _MplsLdpEntityOperStatus_Type(Integer32):
    """Custom type mplsLdpEntityOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("unknown", 1))
    )


_MplsLdpEntityOperStatus_Type.__name__ = "Integer32"
_MplsLdpEntityOperStatus_Object = MibTableColumn
mplsLdpEntityOperStatus = _MplsLdpEntityOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 5),
    _MplsLdpEntityOperStatus_Type()
)
mplsLdpEntityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityOperStatus.setStatus("current")


class _MplsLdpEntityTcpPort_Type(InetPortNumber):
    """Custom type mplsLdpEntityTcpPort based on InetPortNumber"""
    defaultValue = 646


_MplsLdpEntityTcpPort_Object = MibTableColumn
mplsLdpEntityTcpPort = _MplsLdpEntityTcpPort_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 6),
    _MplsLdpEntityTcpPort_Type()
)
mplsLdpEntityTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTcpPort.setStatus("current")


class _MplsLdpEntityUdpDscPort_Type(InetPortNumber):
    """Custom type mplsLdpEntityUdpDscPort based on InetPortNumber"""
    defaultValue = 646


_MplsLdpEntityUdpDscPort_Object = MibTableColumn
mplsLdpEntityUdpDscPort = _MplsLdpEntityUdpDscPort_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 7),
    _MplsLdpEntityUdpDscPort_Type()
)
mplsLdpEntityUdpDscPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityUdpDscPort.setStatus("current")


class _MplsLdpEntityMaxPduLength_Type(Unsigned32):
    """Custom type mplsLdpEntityMaxPduLength based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65535),
    )


_MplsLdpEntityMaxPduLength_Type.__name__ = "Unsigned32"
_MplsLdpEntityMaxPduLength_Object = MibTableColumn
mplsLdpEntityMaxPduLength = _MplsLdpEntityMaxPduLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 8),
    _MplsLdpEntityMaxPduLength_Type()
)
mplsLdpEntityMaxPduLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityMaxPduLength.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpEntityMaxPduLength.setUnits("octets")


class _MplsLdpEntityKeepAliveHoldTimer_Type(Unsigned32):
    """Custom type mplsLdpEntityKeepAliveHoldTimer based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpEntityKeepAliveHoldTimer_Type.__name__ = "Unsigned32"
_MplsLdpEntityKeepAliveHoldTimer_Object = MibTableColumn
mplsLdpEntityKeepAliveHoldTimer = _MplsLdpEntityKeepAliveHoldTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 9),
    _MplsLdpEntityKeepAliveHoldTimer_Type()
)
mplsLdpEntityKeepAliveHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityKeepAliveHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpEntityKeepAliveHoldTimer.setUnits("seconds")


class _MplsLdpEntityHelloHoldTimer_Type(Unsigned32):
    """Custom type mplsLdpEntityHelloHoldTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsLdpEntityHelloHoldTimer_Type.__name__ = "Unsigned32"
_MplsLdpEntityHelloHoldTimer_Object = MibTableColumn
mplsLdpEntityHelloHoldTimer = _MplsLdpEntityHelloHoldTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 10),
    _MplsLdpEntityHelloHoldTimer_Type()
)
mplsLdpEntityHelloHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityHelloHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpEntityHelloHoldTimer.setUnits("seconds")


class _MplsLdpEntityInitSessionThreshold_Type(Integer32):
    """Custom type mplsLdpEntityInitSessionThreshold based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MplsLdpEntityInitSessionThreshold_Type.__name__ = "Integer32"
_MplsLdpEntityInitSessionThreshold_Object = MibTableColumn
mplsLdpEntityInitSessionThreshold = _MplsLdpEntityInitSessionThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 11),
    _MplsLdpEntityInitSessionThreshold_Type()
)
mplsLdpEntityInitSessionThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityInitSessionThreshold.setStatus("current")
_MplsLdpEntityLabelDistMethod_Type = MplsLabelDistributionMethod
_MplsLdpEntityLabelDistMethod_Object = MibTableColumn
mplsLdpEntityLabelDistMethod = _MplsLdpEntityLabelDistMethod_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 12),
    _MplsLdpEntityLabelDistMethod_Type()
)
mplsLdpEntityLabelDistMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityLabelDistMethod.setStatus("current")
_MplsLdpEntityLabelRetentionMode_Type = MplsRetentionMode
_MplsLdpEntityLabelRetentionMode_Object = MibTableColumn
mplsLdpEntityLabelRetentionMode = _MplsLdpEntityLabelRetentionMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 13),
    _MplsLdpEntityLabelRetentionMode_Type()
)
mplsLdpEntityLabelRetentionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityLabelRetentionMode.setStatus("current")


class _MplsLdpEntityPathVectorLimit_Type(Integer32):
    """Custom type mplsLdpEntityPathVectorLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLdpEntityPathVectorLimit_Type.__name__ = "Integer32"
_MplsLdpEntityPathVectorLimit_Object = MibTableColumn
mplsLdpEntityPathVectorLimit = _MplsLdpEntityPathVectorLimit_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 14),
    _MplsLdpEntityPathVectorLimit_Type()
)
mplsLdpEntityPathVectorLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityPathVectorLimit.setStatus("current")


class _MplsLdpEntityHopCountLimit_Type(Integer32):
    """Custom type mplsLdpEntityHopCountLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLdpEntityHopCountLimit_Type.__name__ = "Integer32"
_MplsLdpEntityHopCountLimit_Object = MibTableColumn
mplsLdpEntityHopCountLimit = _MplsLdpEntityHopCountLimit_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 15),
    _MplsLdpEntityHopCountLimit_Type()
)
mplsLdpEntityHopCountLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityHopCountLimit.setStatus("current")


class _MplsLdpEntityTransportAddrKind_Type(Integer32):
    """Custom type mplsLdpEntityTransportAddrKind based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("loopback", 2))
    )


_MplsLdpEntityTransportAddrKind_Type.__name__ = "Integer32"
_MplsLdpEntityTransportAddrKind_Object = MibTableColumn
mplsLdpEntityTransportAddrKind = _MplsLdpEntityTransportAddrKind_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 16),
    _MplsLdpEntityTransportAddrKind_Type()
)
mplsLdpEntityTransportAddrKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTransportAddrKind.setStatus("current")


class _MplsLdpEntityTargetPeer_Type(TruthValue):
    """Custom type mplsLdpEntityTargetPeer based on TruthValue"""


_MplsLdpEntityTargetPeer_Object = MibTableColumn
mplsLdpEntityTargetPeer = _MplsLdpEntityTargetPeer_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 17),
    _MplsLdpEntityTargetPeer_Type()
)
mplsLdpEntityTargetPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTargetPeer.setStatus("current")
_MplsLdpEntityTargetPeerAddrType_Type = InetAddressType
_MplsLdpEntityTargetPeerAddrType_Object = MibTableColumn
mplsLdpEntityTargetPeerAddrType = _MplsLdpEntityTargetPeerAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 18),
    _MplsLdpEntityTargetPeerAddrType_Type()
)
mplsLdpEntityTargetPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTargetPeerAddrType.setStatus("current")
_MplsLdpEntityTargetPeerAddr_Type = InetAddress
_MplsLdpEntityTargetPeerAddr_Object = MibTableColumn
mplsLdpEntityTargetPeerAddr = _MplsLdpEntityTargetPeerAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 19),
    _MplsLdpEntityTargetPeerAddr_Type()
)
mplsLdpEntityTargetPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTargetPeerAddr.setStatus("current")
_MplsLdpEntityLabelType_Type = MplsLdpLabelType
_MplsLdpEntityLabelType_Object = MibTableColumn
mplsLdpEntityLabelType = _MplsLdpEntityLabelType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 20),
    _MplsLdpEntityLabelType_Type()
)
mplsLdpEntityLabelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityLabelType.setStatus("current")
_MplsLdpEntityDiscontinuityTime_Type = TimeStamp
_MplsLdpEntityDiscontinuityTime_Object = MibTableColumn
mplsLdpEntityDiscontinuityTime = _MplsLdpEntityDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 21),
    _MplsLdpEntityDiscontinuityTime_Type()
)
mplsLdpEntityDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityDiscontinuityTime.setStatus("current")


class _MplsLdpEntityStorageType_Type(StorageType):
    """Custom type mplsLdpEntityStorageType based on StorageType"""


_MplsLdpEntityStorageType_Object = MibTableColumn
mplsLdpEntityStorageType = _MplsLdpEntityStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 22),
    _MplsLdpEntityStorageType_Type()
)
mplsLdpEntityStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityStorageType.setStatus("current")
_MplsLdpEntityRowStatus_Type = RowStatus
_MplsLdpEntityRowStatus_Object = MibTableColumn
mplsLdpEntityRowStatus = _MplsLdpEntityRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 3, 1, 23),
    _MplsLdpEntityRowStatus_Type()
)
mplsLdpEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityRowStatus.setStatus("current")
_MplsLdpEntityStatsTable_Object = MibTable
mplsLdpEntityStatsTable = _MplsLdpEntityStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4)
)
if mibBuilder.loadTexts:
    mplsLdpEntityStatsTable.setStatus("current")
_MplsLdpEntityStatsEntry_Object = MibTableRow
mplsLdpEntityStatsEntry = _MplsLdpEntityStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityStatsEntry.setStatus("current")
_MplsLdpEntityStatsSessionAttempts_Type = Counter32
_MplsLdpEntityStatsSessionAttempts_Object = MibTableColumn
mplsLdpEntityStatsSessionAttempts = _MplsLdpEntityStatsSessionAttempts_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 1),
    _MplsLdpEntityStatsSessionAttempts_Type()
)
mplsLdpEntityStatsSessionAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsSessionAttempts.setStatus("current")
_MplsLdpEntityStatsSessionRejectedNoHelloErrors_Type = Counter32
_MplsLdpEntityStatsSessionRejectedNoHelloErrors_Object = MibTableColumn
mplsLdpEntityStatsSessionRejectedNoHelloErrors = _MplsLdpEntityStatsSessionRejectedNoHelloErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 2),
    _MplsLdpEntityStatsSessionRejectedNoHelloErrors_Type()
)
mplsLdpEntityStatsSessionRejectedNoHelloErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsSessionRejectedNoHelloErrors.setStatus("current")
_MplsLdpEntityStatsSessionRejectedAdErrors_Type = Counter32
_MplsLdpEntityStatsSessionRejectedAdErrors_Object = MibTableColumn
mplsLdpEntityStatsSessionRejectedAdErrors = _MplsLdpEntityStatsSessionRejectedAdErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 3),
    _MplsLdpEntityStatsSessionRejectedAdErrors_Type()
)
mplsLdpEntityStatsSessionRejectedAdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsSessionRejectedAdErrors.setStatus("current")
_MplsLdpEntityStatsSessionRejectedMaxPduErrors_Type = Counter32
_MplsLdpEntityStatsSessionRejectedMaxPduErrors_Object = MibTableColumn
mplsLdpEntityStatsSessionRejectedMaxPduErrors = _MplsLdpEntityStatsSessionRejectedMaxPduErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 4),
    _MplsLdpEntityStatsSessionRejectedMaxPduErrors_Type()
)
mplsLdpEntityStatsSessionRejectedMaxPduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsSessionRejectedMaxPduErrors.setStatus("current")
_MplsLdpEntityStatsSessionRejectedLRErrors_Type = Counter32
_MplsLdpEntityStatsSessionRejectedLRErrors_Object = MibTableColumn
mplsLdpEntityStatsSessionRejectedLRErrors = _MplsLdpEntityStatsSessionRejectedLRErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 5),
    _MplsLdpEntityStatsSessionRejectedLRErrors_Type()
)
mplsLdpEntityStatsSessionRejectedLRErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsSessionRejectedLRErrors.setStatus("current")
_MplsLdpEntityStatsBadLdpIdentifierErrors_Type = Counter32
_MplsLdpEntityStatsBadLdpIdentifierErrors_Object = MibTableColumn
mplsLdpEntityStatsBadLdpIdentifierErrors = _MplsLdpEntityStatsBadLdpIdentifierErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 6),
    _MplsLdpEntityStatsBadLdpIdentifierErrors_Type()
)
mplsLdpEntityStatsBadLdpIdentifierErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsBadLdpIdentifierErrors.setStatus("current")
_MplsLdpEntityStatsBadPduLengthErrors_Type = Counter32
_MplsLdpEntityStatsBadPduLengthErrors_Object = MibTableColumn
mplsLdpEntityStatsBadPduLengthErrors = _MplsLdpEntityStatsBadPduLengthErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 7),
    _MplsLdpEntityStatsBadPduLengthErrors_Type()
)
mplsLdpEntityStatsBadPduLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsBadPduLengthErrors.setStatus("current")
_MplsLdpEntityStatsBadMessageLengthErrors_Type = Counter32
_MplsLdpEntityStatsBadMessageLengthErrors_Object = MibTableColumn
mplsLdpEntityStatsBadMessageLengthErrors = _MplsLdpEntityStatsBadMessageLengthErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 8),
    _MplsLdpEntityStatsBadMessageLengthErrors_Type()
)
mplsLdpEntityStatsBadMessageLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsBadMessageLengthErrors.setStatus("current")
_MplsLdpEntityStatsBadTlvLengthErrors_Type = Counter32
_MplsLdpEntityStatsBadTlvLengthErrors_Object = MibTableColumn
mplsLdpEntityStatsBadTlvLengthErrors = _MplsLdpEntityStatsBadTlvLengthErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 9),
    _MplsLdpEntityStatsBadTlvLengthErrors_Type()
)
mplsLdpEntityStatsBadTlvLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsBadTlvLengthErrors.setStatus("current")
_MplsLdpEntityStatsMalformedTlvValueErrors_Type = Counter32
_MplsLdpEntityStatsMalformedTlvValueErrors_Object = MibTableColumn
mplsLdpEntityStatsMalformedTlvValueErrors = _MplsLdpEntityStatsMalformedTlvValueErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 10),
    _MplsLdpEntityStatsMalformedTlvValueErrors_Type()
)
mplsLdpEntityStatsMalformedTlvValueErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsMalformedTlvValueErrors.setStatus("current")
_MplsLdpEntityStatsKeepAliveTimerExpErrors_Type = Counter32
_MplsLdpEntityStatsKeepAliveTimerExpErrors_Object = MibTableColumn
mplsLdpEntityStatsKeepAliveTimerExpErrors = _MplsLdpEntityStatsKeepAliveTimerExpErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 11),
    _MplsLdpEntityStatsKeepAliveTimerExpErrors_Type()
)
mplsLdpEntityStatsKeepAliveTimerExpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsKeepAliveTimerExpErrors.setStatus("current")
_MplsLdpEntityStatsShutdownReceivedNotifications_Type = Counter32
_MplsLdpEntityStatsShutdownReceivedNotifications_Object = MibTableColumn
mplsLdpEntityStatsShutdownReceivedNotifications = _MplsLdpEntityStatsShutdownReceivedNotifications_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 12),
    _MplsLdpEntityStatsShutdownReceivedNotifications_Type()
)
mplsLdpEntityStatsShutdownReceivedNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsShutdownReceivedNotifications.setStatus("current")
_MplsLdpEntityStatsShutdownSentNotifications_Type = Counter32
_MplsLdpEntityStatsShutdownSentNotifications_Object = MibTableColumn
mplsLdpEntityStatsShutdownSentNotifications = _MplsLdpEntityStatsShutdownSentNotifications_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 2, 4, 1, 13),
    _MplsLdpEntityStatsShutdownSentNotifications_Type()
)
mplsLdpEntityStatsShutdownSentNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityStatsShutdownSentNotifications.setStatus("current")
_MplsLdpSessionObjects_ObjectIdentity = ObjectIdentity
mplsLdpSessionObjects = _MplsLdpSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3)
)
_MplsLdpPeerLastChange_Type = TimeStamp
_MplsLdpPeerLastChange_Object = MibScalar
mplsLdpPeerLastChange = _MplsLdpPeerLastChange_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 1),
    _MplsLdpPeerLastChange_Type()
)
mplsLdpPeerLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerLastChange.setStatus("current")
_MplsLdpPeerTable_Object = MibTable
mplsLdpPeerTable = _MplsLdpPeerTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mplsLdpPeerTable.setStatus("current")
_MplsLdpPeerEntry_Object = MibTableRow
mplsLdpPeerEntry = _MplsLdpPeerEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 2, 1)
)
mplsLdpPeerEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    mplsLdpPeerEntry.setStatus("current")
_MplsLdpPeerLdpId_Type = MplsLdpIdentifier
_MplsLdpPeerLdpId_Object = MibTableColumn
mplsLdpPeerLdpId = _MplsLdpPeerLdpId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 2, 1, 1),
    _MplsLdpPeerLdpId_Type()
)
mplsLdpPeerLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpPeerLdpId.setStatus("current")
_MplsLdpPeerLabelDistMethod_Type = MplsLabelDistributionMethod
_MplsLdpPeerLabelDistMethod_Object = MibTableColumn
mplsLdpPeerLabelDistMethod = _MplsLdpPeerLabelDistMethod_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 2, 1, 2),
    _MplsLdpPeerLabelDistMethod_Type()
)
mplsLdpPeerLabelDistMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerLabelDistMethod.setStatus("current")


class _MplsLdpPeerPathVectorLimit_Type(Integer32):
    """Custom type mplsLdpPeerPathVectorLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLdpPeerPathVectorLimit_Type.__name__ = "Integer32"
_MplsLdpPeerPathVectorLimit_Object = MibTableColumn
mplsLdpPeerPathVectorLimit = _MplsLdpPeerPathVectorLimit_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 2, 1, 3),
    _MplsLdpPeerPathVectorLimit_Type()
)
mplsLdpPeerPathVectorLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerPathVectorLimit.setStatus("current")
_MplsLdpPeerTransportAddrType_Type = InetAddressType
_MplsLdpPeerTransportAddrType_Object = MibTableColumn
mplsLdpPeerTransportAddrType = _MplsLdpPeerTransportAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 2, 1, 4),
    _MplsLdpPeerTransportAddrType_Type()
)
mplsLdpPeerTransportAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerTransportAddrType.setStatus("current")
_MplsLdpPeerTransportAddr_Type = InetAddress
_MplsLdpPeerTransportAddr_Object = MibTableColumn
mplsLdpPeerTransportAddr = _MplsLdpPeerTransportAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 2, 1, 5),
    _MplsLdpPeerTransportAddr_Type()
)
mplsLdpPeerTransportAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerTransportAddr.setStatus("current")
_MplsLdpSessionTable_Object = MibTable
mplsLdpSessionTable = _MplsLdpSessionTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    mplsLdpSessionTable.setStatus("current")
_MplsLdpSessionEntry_Object = MibTableRow
mplsLdpSessionEntry = _MplsLdpSessionEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mplsLdpSessionEntry.setStatus("current")
_MplsLdpSessionStateLastChange_Type = TimeStamp
_MplsLdpSessionStateLastChange_Object = MibTableColumn
mplsLdpSessionStateLastChange = _MplsLdpSessionStateLastChange_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 1),
    _MplsLdpSessionStateLastChange_Type()
)
mplsLdpSessionStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionStateLastChange.setStatus("current")


class _MplsLdpSessionState_Type(Integer32):
    """Custom type mplsLdpSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("initialized", 2),
          ("nonexistent", 1),
          ("openrec", 3),
          ("opensent", 4),
          ("operational", 5))
    )


_MplsLdpSessionState_Type.__name__ = "Integer32"
_MplsLdpSessionState_Object = MibTableColumn
mplsLdpSessionState = _MplsLdpSessionState_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 2),
    _MplsLdpSessionState_Type()
)
mplsLdpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionState.setStatus("current")


class _MplsLdpSessionRole_Type(Integer32):
    """Custom type mplsLdpSessionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("passive", 3),
          ("unknown", 1))
    )


_MplsLdpSessionRole_Type.__name__ = "Integer32"
_MplsLdpSessionRole_Object = MibTableColumn
mplsLdpSessionRole = _MplsLdpSessionRole_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 3),
    _MplsLdpSessionRole_Type()
)
mplsLdpSessionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionRole.setStatus("current")


class _MplsLdpSessionProtocolVersion_Type(Unsigned32):
    """Custom type mplsLdpSessionProtocolVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpSessionProtocolVersion_Type.__name__ = "Unsigned32"
_MplsLdpSessionProtocolVersion_Object = MibTableColumn
mplsLdpSessionProtocolVersion = _MplsLdpSessionProtocolVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 4),
    _MplsLdpSessionProtocolVersion_Type()
)
mplsLdpSessionProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionProtocolVersion.setStatus("current")
_MplsLdpSessionKeepAliveHoldTimeRem_Type = TimeInterval
_MplsLdpSessionKeepAliveHoldTimeRem_Object = MibTableColumn
mplsLdpSessionKeepAliveHoldTimeRem = _MplsLdpSessionKeepAliveHoldTimeRem_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 5),
    _MplsLdpSessionKeepAliveHoldTimeRem_Type()
)
mplsLdpSessionKeepAliveHoldTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionKeepAliveHoldTimeRem.setStatus("current")


class _MplsLdpSessionKeepAliveTime_Type(Unsigned32):
    """Custom type mplsLdpSessionKeepAliveTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpSessionKeepAliveTime_Type.__name__ = "Unsigned32"
_MplsLdpSessionKeepAliveTime_Object = MibTableColumn
mplsLdpSessionKeepAliveTime = _MplsLdpSessionKeepAliveTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 6),
    _MplsLdpSessionKeepAliveTime_Type()
)
mplsLdpSessionKeepAliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionKeepAliveTime.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpSessionKeepAliveTime.setUnits("seconds")


class _MplsLdpSessionMaxPduLength_Type(Unsigned32):
    """Custom type mplsLdpSessionMaxPduLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpSessionMaxPduLength_Type.__name__ = "Unsigned32"
_MplsLdpSessionMaxPduLength_Object = MibTableColumn
mplsLdpSessionMaxPduLength = _MplsLdpSessionMaxPduLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 7),
    _MplsLdpSessionMaxPduLength_Type()
)
mplsLdpSessionMaxPduLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionMaxPduLength.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpSessionMaxPduLength.setUnits("octets")
_MplsLdpSessionDiscontinuityTime_Type = TimeStamp
_MplsLdpSessionDiscontinuityTime_Object = MibTableColumn
mplsLdpSessionDiscontinuityTime = _MplsLdpSessionDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 3, 1, 8),
    _MplsLdpSessionDiscontinuityTime_Type()
)
mplsLdpSessionDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionDiscontinuityTime.setStatus("current")
_MplsLdpSessionStatsTable_Object = MibTable
mplsLdpSessionStatsTable = _MplsLdpSessionStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 4)
)
if mibBuilder.loadTexts:
    mplsLdpSessionStatsTable.setStatus("current")
_MplsLdpSessionStatsEntry_Object = MibTableRow
mplsLdpSessionStatsEntry = _MplsLdpSessionStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    mplsLdpSessionStatsEntry.setStatus("current")
_MplsLdpSessionStatsUnknownMesTypeErrors_Type = Counter32
_MplsLdpSessionStatsUnknownMesTypeErrors_Object = MibTableColumn
mplsLdpSessionStatsUnknownMesTypeErrors = _MplsLdpSessionStatsUnknownMesTypeErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 4, 1, 1),
    _MplsLdpSessionStatsUnknownMesTypeErrors_Type()
)
mplsLdpSessionStatsUnknownMesTypeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionStatsUnknownMesTypeErrors.setStatus("current")
_MplsLdpSessionStatsUnknownTlvErrors_Type = Counter32
_MplsLdpSessionStatsUnknownTlvErrors_Object = MibTableColumn
mplsLdpSessionStatsUnknownTlvErrors = _MplsLdpSessionStatsUnknownTlvErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 4, 1, 2),
    _MplsLdpSessionStatsUnknownTlvErrors_Type()
)
mplsLdpSessionStatsUnknownTlvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionStatsUnknownTlvErrors.setStatus("current")
_MplsLdpHelloAdjacencyObjects_ObjectIdentity = ObjectIdentity
mplsLdpHelloAdjacencyObjects = _MplsLdpHelloAdjacencyObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 5)
)
_MplsLdpHelloAdjacencyTable_Object = MibTable
mplsLdpHelloAdjacencyTable = _MplsLdpHelloAdjacencyTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyTable.setStatus("current")
_MplsLdpHelloAdjacencyEntry_Object = MibTableRow
mplsLdpHelloAdjacencyEntry = _MplsLdpHelloAdjacencyEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 5, 1, 1)
)
mplsLdpHelloAdjacencyEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpHelloAdjacencyIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyEntry.setStatus("current")


class _MplsLdpHelloAdjacencyIndex_Type(Unsigned32):
    """Custom type mplsLdpHelloAdjacencyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsLdpHelloAdjacencyIndex_Type.__name__ = "Unsigned32"
_MplsLdpHelloAdjacencyIndex_Object = MibTableColumn
mplsLdpHelloAdjacencyIndex = _MplsLdpHelloAdjacencyIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 5, 1, 1, 1),
    _MplsLdpHelloAdjacencyIndex_Type()
)
mplsLdpHelloAdjacencyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyIndex.setStatus("current")
_MplsLdpHelloAdjacencyHoldTimeRem_Type = TimeInterval
_MplsLdpHelloAdjacencyHoldTimeRem_Object = MibTableColumn
mplsLdpHelloAdjacencyHoldTimeRem = _MplsLdpHelloAdjacencyHoldTimeRem_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 5, 1, 1, 2),
    _MplsLdpHelloAdjacencyHoldTimeRem_Type()
)
mplsLdpHelloAdjacencyHoldTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyHoldTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyHoldTimeRem.setUnits("seconds")


class _MplsLdpHelloAdjacencyHoldTime_Type(Unsigned32):
    """Custom type mplsLdpHelloAdjacencyHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsLdpHelloAdjacencyHoldTime_Type.__name__ = "Unsigned32"
_MplsLdpHelloAdjacencyHoldTime_Object = MibTableColumn
mplsLdpHelloAdjacencyHoldTime = _MplsLdpHelloAdjacencyHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 5, 1, 1, 3),
    _MplsLdpHelloAdjacencyHoldTime_Type()
)
mplsLdpHelloAdjacencyHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyHoldTime.setStatus("current")


class _MplsLdpHelloAdjacencyType_Type(Integer32):
    """Custom type mplsLdpHelloAdjacencyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("targeted", 2))
    )


_MplsLdpHelloAdjacencyType_Type.__name__ = "Integer32"
_MplsLdpHelloAdjacencyType_Object = MibTableColumn
mplsLdpHelloAdjacencyType = _MplsLdpHelloAdjacencyType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 5, 1, 1, 4),
    _MplsLdpHelloAdjacencyType_Type()
)
mplsLdpHelloAdjacencyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyType.setStatus("current")
_MplsInSegmentLdpLspTable_Object = MibTable
mplsInSegmentLdpLspTable = _MplsInSegmentLdpLspTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 6)
)
if mibBuilder.loadTexts:
    mplsInSegmentLdpLspTable.setStatus("current")
_MplsInSegmentLdpLspEntry_Object = MibTableRow
mplsInSegmentLdpLspEntry = _MplsInSegmentLdpLspEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 6, 1)
)
mplsInSegmentLdpLspEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsInSegmentLdpLspIndex"),
)
if mibBuilder.loadTexts:
    mplsInSegmentLdpLspEntry.setStatus("current")
_MplsInSegmentLdpLspIndex_Type = MplsIndexType
_MplsInSegmentLdpLspIndex_Object = MibTableColumn
mplsInSegmentLdpLspIndex = _MplsInSegmentLdpLspIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 6, 1, 1),
    _MplsInSegmentLdpLspIndex_Type()
)
mplsInSegmentLdpLspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsInSegmentLdpLspIndex.setStatus("current")
_MplsInSegmentLdpLspLabelType_Type = MplsLdpLabelType
_MplsInSegmentLdpLspLabelType_Object = MibTableColumn
mplsInSegmentLdpLspLabelType = _MplsInSegmentLdpLspLabelType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 6, 1, 2),
    _MplsInSegmentLdpLspLabelType_Type()
)
mplsInSegmentLdpLspLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentLdpLspLabelType.setStatus("current")
_MplsInSegmentLdpLspType_Type = MplsLspType
_MplsInSegmentLdpLspType_Object = MibTableColumn
mplsInSegmentLdpLspType = _MplsInSegmentLdpLspType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 6, 1, 3),
    _MplsInSegmentLdpLspType_Type()
)
mplsInSegmentLdpLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsInSegmentLdpLspType.setStatus("current")
_MplsOutSegmentLdpLspTable_Object = MibTable
mplsOutSegmentLdpLspTable = _MplsOutSegmentLdpLspTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 7)
)
if mibBuilder.loadTexts:
    mplsOutSegmentLdpLspTable.setStatus("current")
_MplsOutSegmentLdpLspEntry_Object = MibTableRow
mplsOutSegmentLdpLspEntry = _MplsOutSegmentLdpLspEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 7, 1)
)
mplsOutSegmentLdpLspEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsOutSegmentLdpLspIndex"),
)
if mibBuilder.loadTexts:
    mplsOutSegmentLdpLspEntry.setStatus("current")
_MplsOutSegmentLdpLspIndex_Type = MplsIndexType
_MplsOutSegmentLdpLspIndex_Object = MibTableColumn
mplsOutSegmentLdpLspIndex = _MplsOutSegmentLdpLspIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 7, 1, 1),
    _MplsOutSegmentLdpLspIndex_Type()
)
mplsOutSegmentLdpLspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsOutSegmentLdpLspIndex.setStatus("current")
_MplsOutSegmentLdpLspLabelType_Type = MplsLdpLabelType
_MplsOutSegmentLdpLspLabelType_Object = MibTableColumn
mplsOutSegmentLdpLspLabelType = _MplsOutSegmentLdpLspLabelType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 7, 1, 2),
    _MplsOutSegmentLdpLspLabelType_Type()
)
mplsOutSegmentLdpLspLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentLdpLspLabelType.setStatus("current")
_MplsOutSegmentLdpLspType_Type = MplsLspType
_MplsOutSegmentLdpLspType_Object = MibTableColumn
mplsOutSegmentLdpLspType = _MplsOutSegmentLdpLspType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 7, 1, 3),
    _MplsOutSegmentLdpLspType_Type()
)
mplsOutSegmentLdpLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOutSegmentLdpLspType.setStatus("current")
_MplsFecObjects_ObjectIdentity = ObjectIdentity
mplsFecObjects = _MplsFecObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8)
)
_MplsFecLastChange_Type = TimeStamp
_MplsFecLastChange_Object = MibScalar
mplsFecLastChange = _MplsFecLastChange_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 1),
    _MplsFecLastChange_Type()
)
mplsFecLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFecLastChange.setStatus("current")
_MplsFecIndexNext_Type = IndexIntegerNextFree
_MplsFecIndexNext_Object = MibScalar
mplsFecIndexNext = _MplsFecIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 2),
    _MplsFecIndexNext_Type()
)
mplsFecIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFecIndexNext.setStatus("current")
_MplsFecTable_Object = MibTable
mplsFecTable = _MplsFecTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3)
)
if mibBuilder.loadTexts:
    mplsFecTable.setStatus("current")
_MplsFecEntry_Object = MibTableRow
mplsFecEntry = _MplsFecEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1)
)
mplsFecEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsFecIndex"),
)
if mibBuilder.loadTexts:
    mplsFecEntry.setStatus("current")
_MplsFecIndex_Type = IndexInteger
_MplsFecIndex_Object = MibTableColumn
mplsFecIndex = _MplsFecIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1, 1),
    _MplsFecIndex_Type()
)
mplsFecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFecIndex.setStatus("current")


class _MplsFecType_Type(Integer32):
    """Custom type mplsFecType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hostAddress", 2),
          ("prefix", 1))
    )


_MplsFecType_Type.__name__ = "Integer32"
_MplsFecType_Object = MibTableColumn
mplsFecType = _MplsFecType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1, 2),
    _MplsFecType_Type()
)
mplsFecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFecType.setStatus("current")


class _MplsFecAddrPrefixLength_Type(InetAddressPrefixLength):
    """Custom type mplsFecAddrPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_MplsFecAddrPrefixLength_Object = MibTableColumn
mplsFecAddrPrefixLength = _MplsFecAddrPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1, 3),
    _MplsFecAddrPrefixLength_Type()
)
mplsFecAddrPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFecAddrPrefixLength.setStatus("current")
_MplsFecAddrType_Type = InetAddressType
_MplsFecAddrType_Object = MibTableColumn
mplsFecAddrType = _MplsFecAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1, 4),
    _MplsFecAddrType_Type()
)
mplsFecAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFecAddrType.setStatus("current")
_MplsFecAddr_Type = InetAddress
_MplsFecAddr_Object = MibTableColumn
mplsFecAddr = _MplsFecAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1, 5),
    _MplsFecAddr_Type()
)
mplsFecAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFecAddr.setStatus("current")


class _MplsFecStorageType_Type(StorageType):
    """Custom type mplsFecStorageType based on StorageType"""


_MplsFecStorageType_Object = MibTableColumn
mplsFecStorageType = _MplsFecStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1, 6),
    _MplsFecStorageType_Type()
)
mplsFecStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFecStorageType.setStatus("current")
_MplsFecRowStatus_Type = RowStatus
_MplsFecRowStatus_Object = MibTableColumn
mplsFecRowStatus = _MplsFecRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 8, 3, 1, 7),
    _MplsFecRowStatus_Type()
)
mplsFecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFecRowStatus.setStatus("current")
_MplsLdpLspFecLastChange_Type = TimeStamp
_MplsLdpLspFecLastChange_Object = MibScalar
mplsLdpLspFecLastChange = _MplsLdpLspFecLastChange_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 9),
    _MplsLdpLspFecLastChange_Type()
)
mplsLdpLspFecLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLspFecLastChange.setStatus("current")
_MplsLdpLspFecTable_Object = MibTable
mplsLdpLspFecTable = _MplsLdpLspFecTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 10)
)
if mibBuilder.loadTexts:
    mplsLdpLspFecTable.setStatus("current")
_MplsLdpLspFecEntry_Object = MibTableRow
mplsLdpLspFecEntry = _MplsLdpLspFecEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 10, 1)
)
mplsLdpLspFecEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpLspFecSegment"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpLspFecSegmentIndex"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpLspFecIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpLspFecEntry.setStatus("current")


class _MplsLdpLspFecSegment_Type(Integer32):
    """Custom type mplsLdpLspFecSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inSegment", 1),
          ("outSegment", 2))
    )


_MplsLdpLspFecSegment_Type.__name__ = "Integer32"
_MplsLdpLspFecSegment_Object = MibTableColumn
mplsLdpLspFecSegment = _MplsLdpLspFecSegment_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 10, 1, 1),
    _MplsLdpLspFecSegment_Type()
)
mplsLdpLspFecSegment.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpLspFecSegment.setStatus("current")
_MplsLdpLspFecSegmentIndex_Type = MplsIndexType
_MplsLdpLspFecSegmentIndex_Object = MibTableColumn
mplsLdpLspFecSegmentIndex = _MplsLdpLspFecSegmentIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 10, 1, 2),
    _MplsLdpLspFecSegmentIndex_Type()
)
mplsLdpLspFecSegmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpLspFecSegmentIndex.setStatus("current")
_MplsLdpLspFecIndex_Type = IndexInteger
_MplsLdpLspFecIndex_Object = MibTableColumn
mplsLdpLspFecIndex = _MplsLdpLspFecIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 10, 1, 3),
    _MplsLdpLspFecIndex_Type()
)
mplsLdpLspFecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpLspFecIndex.setStatus("current")


class _MplsLdpLspFecStorageType_Type(StorageType):
    """Custom type mplsLdpLspFecStorageType based on StorageType"""


_MplsLdpLspFecStorageType_Object = MibTableColumn
mplsLdpLspFecStorageType = _MplsLdpLspFecStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 10, 1, 4),
    _MplsLdpLspFecStorageType_Type()
)
mplsLdpLspFecStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpLspFecStorageType.setStatus("current")
_MplsLdpLspFecRowStatus_Type = RowStatus
_MplsLdpLspFecRowStatus_Object = MibTableColumn
mplsLdpLspFecRowStatus = _MplsLdpLspFecRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 10, 1, 5),
    _MplsLdpLspFecRowStatus_Type()
)
mplsLdpLspFecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpLspFecRowStatus.setStatus("current")
_MplsLdpSessionPeerAddrTable_Object = MibTable
mplsLdpSessionPeerAddrTable = _MplsLdpSessionPeerAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 11)
)
if mibBuilder.loadTexts:
    mplsLdpSessionPeerAddrTable.setStatus("current")
_MplsLdpSessionPeerAddrEntry_Object = MibTableRow
mplsLdpSessionPeerAddrEntry = _MplsLdpSessionPeerAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 11, 1)
)
mplsLdpSessionPeerAddrEntry.setIndexNames(
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-STD-MIB", "mplsLdpSessionPeerAddrIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpSessionPeerAddrEntry.setStatus("current")


class _MplsLdpSessionPeerAddrIndex_Type(Unsigned32):
    """Custom type mplsLdpSessionPeerAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsLdpSessionPeerAddrIndex_Type.__name__ = "Unsigned32"
_MplsLdpSessionPeerAddrIndex_Object = MibTableColumn
mplsLdpSessionPeerAddrIndex = _MplsLdpSessionPeerAddrIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 11, 1, 1),
    _MplsLdpSessionPeerAddrIndex_Type()
)
mplsLdpSessionPeerAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionPeerAddrIndex.setStatus("current")
_MplsLdpSessionPeerNextHopAddrType_Type = InetAddressType
_MplsLdpSessionPeerNextHopAddrType_Object = MibTableColumn
mplsLdpSessionPeerNextHopAddrType = _MplsLdpSessionPeerNextHopAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 11, 1, 2),
    _MplsLdpSessionPeerNextHopAddrType_Type()
)
mplsLdpSessionPeerNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionPeerNextHopAddrType.setStatus("current")
_MplsLdpSessionPeerNextHopAddr_Type = InetAddress
_MplsLdpSessionPeerNextHopAddr_Object = MibTableColumn
mplsLdpSessionPeerNextHopAddr = _MplsLdpSessionPeerNextHopAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 1, 3, 11, 1, 3),
    _MplsLdpSessionPeerNextHopAddr_Type()
)
mplsLdpSessionPeerNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionPeerNextHopAddr.setStatus("current")
_MplsLdpConformance_ObjectIdentity = ObjectIdentity
mplsLdpConformance = _MplsLdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 2)
)
_MplsLdpGroups_ObjectIdentity = ObjectIdentity
mplsLdpGroups = _MplsLdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 2, 1)
)
_MplsLdpCompliances_ObjectIdentity = ObjectIdentity
mplsLdpCompliances = _MplsLdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 2, 2)
)
mplsLdpEntityEntry.registerAugmentions(
    ("MPLS-LDP-STD-MIB",
     "mplsLdpEntityStatsEntry")
)
mplsLdpEntityStatsEntry.setIndexNames(*mplsLdpEntityEntry.getIndexNames())
mplsLdpPeerEntry.registerAugmentions(
    ("MPLS-LDP-STD-MIB",
     "mplsLdpSessionEntry")
)
mplsLdpSessionEntry.setIndexNames(*mplsLdpPeerEntry.getIndexNames())
mplsLdpPeerEntry.registerAugmentions(
    ("MPLS-LDP-STD-MIB",
     "mplsLdpSessionStatsEntry")
)
mplsLdpSessionStatsEntry.setIndexNames(*mplsLdpPeerEntry.getIndexNames())

# Managed Objects groups

mplsLdpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 2, 1, 1)
)
mplsLdpGeneralGroup.setObjects(
      *(("MPLS-LDP-STD-MIB", "mplsLdpLsrId"),
        ("MPLS-LDP-STD-MIB", "mplsLdpLsrLoopDetectionCapable"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityLastChange"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityIndexNext"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityProtocolVersion"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityAdminStatus"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityOperStatus"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityTcpPort"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityUdpDscPort"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityMaxPduLength"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityKeepAliveHoldTimer"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityHelloHoldTimer"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityInitSessionThreshold"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityLabelDistMethod"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityLabelRetentionMode"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityPathVectorLimit"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityHopCountLimit"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityTransportAddrKind"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityTargetPeer"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityTargetPeerAddrType"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityTargetPeerAddr"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityLabelType"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityDiscontinuityTime"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityStorageType"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityRowStatus"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsSessionAttempts"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsSessionRejectedNoHelloErrors"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsSessionRejectedAdErrors"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsSessionRejectedMaxPduErrors"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsSessionRejectedLRErrors"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsBadLdpIdentifierErrors"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsBadPduLengthErrors"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsBadMessageLengthErrors"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsBadTlvLengthErrors"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsMalformedTlvValueErrors"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsKeepAliveTimerExpErrors"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsShutdownReceivedNotifications"),
        ("MPLS-LDP-STD-MIB", "mplsLdpEntityStatsShutdownSentNotifications"),
        ("MPLS-LDP-STD-MIB", "mplsLdpPeerLastChange"),
        ("MPLS-LDP-STD-MIB", "mplsLdpPeerLabelDistMethod"),
        ("MPLS-LDP-STD-MIB", "mplsLdpPeerPathVectorLimit"),
        ("MPLS-LDP-STD-MIB", "mplsLdpPeerTransportAddrType"),
        ("MPLS-LDP-STD-MIB", "mplsLdpPeerTransportAddr"),
        ("MPLS-LDP-STD-MIB", "mplsLdpHelloAdjacencyHoldTimeRem"),
        ("MPLS-LDP-STD-MIB", "mplsLdpHelloAdjacencyHoldTime"),
        ("MPLS-LDP-STD-MIB", "mplsLdpHelloAdjacencyType"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionStateLastChange"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionState"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionRole"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionProtocolVersion"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionKeepAliveHoldTimeRem"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionKeepAliveTime"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionMaxPduLength"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionDiscontinuityTime"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionStatsUnknownMesTypeErrors"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionStatsUnknownTlvErrors"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionPeerNextHopAddrType"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionPeerNextHopAddr"),
        ("MPLS-LDP-STD-MIB", "mplsFecLastChange"),
        ("MPLS-LDP-STD-MIB", "mplsFecIndexNext"),
        ("MPLS-LDP-STD-MIB", "mplsFecType"),
        ("MPLS-LDP-STD-MIB", "mplsFecAddrType"),
        ("MPLS-LDP-STD-MIB", "mplsFecAddr"),
        ("MPLS-LDP-STD-MIB", "mplsFecAddrPrefixLength"),
        ("MPLS-LDP-STD-MIB", "mplsFecStorageType"),
        ("MPLS-LDP-STD-MIB", "mplsFecRowStatus"))
)
if mibBuilder.loadTexts:
    mplsLdpGeneralGroup.setStatus("current")

mplsLdpLspGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 2, 1, 2)
)
mplsLdpLspGroup.setObjects(
      *(("MPLS-LDP-STD-MIB", "mplsInSegmentLdpLspLabelType"),
        ("MPLS-LDP-STD-MIB", "mplsInSegmentLdpLspType"),
        ("MPLS-LDP-STD-MIB", "mplsOutSegmentLdpLspLabelType"),
        ("MPLS-LDP-STD-MIB", "mplsOutSegmentLdpLspType"),
        ("MPLS-LDP-STD-MIB", "mplsLdpLspFecLastChange"),
        ("MPLS-LDP-STD-MIB", "mplsLdpLspFecStorageType"),
        ("MPLS-LDP-STD-MIB", "mplsLdpLspFecRowStatus"))
)
if mibBuilder.loadTexts:
    mplsLdpLspGroup.setStatus("current")


# Notification objects

mplsLdpInitSessionThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 0, 1)
)
mplsLdpInitSessionThresholdExceeded.setObjects(
    ("MPLS-LDP-STD-MIB", "mplsLdpEntityInitSessionThreshold")
)
if mibBuilder.loadTexts:
    mplsLdpInitSessionThresholdExceeded.setStatus(
        "current"
    )

mplsLdpPathVectorLimitMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 0, 2)
)
mplsLdpPathVectorLimitMismatch.setObjects(
      *(("MPLS-LDP-STD-MIB", "mplsLdpEntityPathVectorLimit"),
        ("MPLS-LDP-STD-MIB", "mplsLdpPeerPathVectorLimit"))
)
if mibBuilder.loadTexts:
    mplsLdpPathVectorLimitMismatch.setStatus(
        "current"
    )

mplsLdpSessionUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 0, 3)
)
mplsLdpSessionUp.setObjects(
      *(("MPLS-LDP-STD-MIB", "mplsLdpSessionState"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionDiscontinuityTime"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionStatsUnknownMesTypeErrors"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionStatsUnknownTlvErrors"))
)
if mibBuilder.loadTexts:
    mplsLdpSessionUp.setStatus(
        "current"
    )

mplsLdpSessionDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 0, 4)
)
mplsLdpSessionDown.setObjects(
      *(("MPLS-LDP-STD-MIB", "mplsLdpSessionState"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionDiscontinuityTime"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionStatsUnknownMesTypeErrors"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionStatsUnknownTlvErrors"))
)
if mibBuilder.loadTexts:
    mplsLdpSessionDown.setStatus(
        "current"
    )


# Notifications groups

mplsLdpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 2, 1, 3)
)
mplsLdpNotificationsGroup.setObjects(
      *(("MPLS-LDP-STD-MIB", "mplsLdpInitSessionThresholdExceeded"),
        ("MPLS-LDP-STD-MIB", "mplsLdpPathVectorLimitMismatch"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionUp"),
        ("MPLS-LDP-STD-MIB", "mplsLdpSessionDown"))
)
if mibBuilder.loadTexts:
    mplsLdpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsLdpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLdpModuleFullCompliance.setStatus(
        "current"
    )

mplsLdpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mplsLdpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-LDP-STD-MIB",
    **{"mplsLdpStdMIB": mplsLdpStdMIB,
       "mplsLdpNotifications": mplsLdpNotifications,
       "mplsLdpInitSessionThresholdExceeded": mplsLdpInitSessionThresholdExceeded,
       "mplsLdpPathVectorLimitMismatch": mplsLdpPathVectorLimitMismatch,
       "mplsLdpSessionUp": mplsLdpSessionUp,
       "mplsLdpSessionDown": mplsLdpSessionDown,
       "mplsLdpObjects": mplsLdpObjects,
       "mplsLdpLsrObjects": mplsLdpLsrObjects,
       "mplsLdpLsrId": mplsLdpLsrId,
       "mplsLdpLsrLoopDetectionCapable": mplsLdpLsrLoopDetectionCapable,
       "mplsLdpEntityObjects": mplsLdpEntityObjects,
       "mplsLdpEntityLastChange": mplsLdpEntityLastChange,
       "mplsLdpEntityIndexNext": mplsLdpEntityIndexNext,
       "mplsLdpEntityTable": mplsLdpEntityTable,
       "mplsLdpEntityEntry": mplsLdpEntityEntry,
       "mplsLdpEntityLdpId": mplsLdpEntityLdpId,
       "mplsLdpEntityIndex": mplsLdpEntityIndex,
       "mplsLdpEntityProtocolVersion": mplsLdpEntityProtocolVersion,
       "mplsLdpEntityAdminStatus": mplsLdpEntityAdminStatus,
       "mplsLdpEntityOperStatus": mplsLdpEntityOperStatus,
       "mplsLdpEntityTcpPort": mplsLdpEntityTcpPort,
       "mplsLdpEntityUdpDscPort": mplsLdpEntityUdpDscPort,
       "mplsLdpEntityMaxPduLength": mplsLdpEntityMaxPduLength,
       "mplsLdpEntityKeepAliveHoldTimer": mplsLdpEntityKeepAliveHoldTimer,
       "mplsLdpEntityHelloHoldTimer": mplsLdpEntityHelloHoldTimer,
       "mplsLdpEntityInitSessionThreshold": mplsLdpEntityInitSessionThreshold,
       "mplsLdpEntityLabelDistMethod": mplsLdpEntityLabelDistMethod,
       "mplsLdpEntityLabelRetentionMode": mplsLdpEntityLabelRetentionMode,
       "mplsLdpEntityPathVectorLimit": mplsLdpEntityPathVectorLimit,
       "mplsLdpEntityHopCountLimit": mplsLdpEntityHopCountLimit,
       "mplsLdpEntityTransportAddrKind": mplsLdpEntityTransportAddrKind,
       "mplsLdpEntityTargetPeer": mplsLdpEntityTargetPeer,
       "mplsLdpEntityTargetPeerAddrType": mplsLdpEntityTargetPeerAddrType,
       "mplsLdpEntityTargetPeerAddr": mplsLdpEntityTargetPeerAddr,
       "mplsLdpEntityLabelType": mplsLdpEntityLabelType,
       "mplsLdpEntityDiscontinuityTime": mplsLdpEntityDiscontinuityTime,
       "mplsLdpEntityStorageType": mplsLdpEntityStorageType,
       "mplsLdpEntityRowStatus": mplsLdpEntityRowStatus,
       "mplsLdpEntityStatsTable": mplsLdpEntityStatsTable,
       "mplsLdpEntityStatsEntry": mplsLdpEntityStatsEntry,
       "mplsLdpEntityStatsSessionAttempts": mplsLdpEntityStatsSessionAttempts,
       "mplsLdpEntityStatsSessionRejectedNoHelloErrors": mplsLdpEntityStatsSessionRejectedNoHelloErrors,
       "mplsLdpEntityStatsSessionRejectedAdErrors": mplsLdpEntityStatsSessionRejectedAdErrors,
       "mplsLdpEntityStatsSessionRejectedMaxPduErrors": mplsLdpEntityStatsSessionRejectedMaxPduErrors,
       "mplsLdpEntityStatsSessionRejectedLRErrors": mplsLdpEntityStatsSessionRejectedLRErrors,
       "mplsLdpEntityStatsBadLdpIdentifierErrors": mplsLdpEntityStatsBadLdpIdentifierErrors,
       "mplsLdpEntityStatsBadPduLengthErrors": mplsLdpEntityStatsBadPduLengthErrors,
       "mplsLdpEntityStatsBadMessageLengthErrors": mplsLdpEntityStatsBadMessageLengthErrors,
       "mplsLdpEntityStatsBadTlvLengthErrors": mplsLdpEntityStatsBadTlvLengthErrors,
       "mplsLdpEntityStatsMalformedTlvValueErrors": mplsLdpEntityStatsMalformedTlvValueErrors,
       "mplsLdpEntityStatsKeepAliveTimerExpErrors": mplsLdpEntityStatsKeepAliveTimerExpErrors,
       "mplsLdpEntityStatsShutdownReceivedNotifications": mplsLdpEntityStatsShutdownReceivedNotifications,
       "mplsLdpEntityStatsShutdownSentNotifications": mplsLdpEntityStatsShutdownSentNotifications,
       "mplsLdpSessionObjects": mplsLdpSessionObjects,
       "mplsLdpPeerLastChange": mplsLdpPeerLastChange,
       "mplsLdpPeerTable": mplsLdpPeerTable,
       "mplsLdpPeerEntry": mplsLdpPeerEntry,
       "mplsLdpPeerLdpId": mplsLdpPeerLdpId,
       "mplsLdpPeerLabelDistMethod": mplsLdpPeerLabelDistMethod,
       "mplsLdpPeerPathVectorLimit": mplsLdpPeerPathVectorLimit,
       "mplsLdpPeerTransportAddrType": mplsLdpPeerTransportAddrType,
       "mplsLdpPeerTransportAddr": mplsLdpPeerTransportAddr,
       "mplsLdpSessionTable": mplsLdpSessionTable,
       "mplsLdpSessionEntry": mplsLdpSessionEntry,
       "mplsLdpSessionStateLastChange": mplsLdpSessionStateLastChange,
       "mplsLdpSessionState": mplsLdpSessionState,
       "mplsLdpSessionRole": mplsLdpSessionRole,
       "mplsLdpSessionProtocolVersion": mplsLdpSessionProtocolVersion,
       "mplsLdpSessionKeepAliveHoldTimeRem": mplsLdpSessionKeepAliveHoldTimeRem,
       "mplsLdpSessionKeepAliveTime": mplsLdpSessionKeepAliveTime,
       "mplsLdpSessionMaxPduLength": mplsLdpSessionMaxPduLength,
       "mplsLdpSessionDiscontinuityTime": mplsLdpSessionDiscontinuityTime,
       "mplsLdpSessionStatsTable": mplsLdpSessionStatsTable,
       "mplsLdpSessionStatsEntry": mplsLdpSessionStatsEntry,
       "mplsLdpSessionStatsUnknownMesTypeErrors": mplsLdpSessionStatsUnknownMesTypeErrors,
       "mplsLdpSessionStatsUnknownTlvErrors": mplsLdpSessionStatsUnknownTlvErrors,
       "mplsLdpHelloAdjacencyObjects": mplsLdpHelloAdjacencyObjects,
       "mplsLdpHelloAdjacencyTable": mplsLdpHelloAdjacencyTable,
       "mplsLdpHelloAdjacencyEntry": mplsLdpHelloAdjacencyEntry,
       "mplsLdpHelloAdjacencyIndex": mplsLdpHelloAdjacencyIndex,
       "mplsLdpHelloAdjacencyHoldTimeRem": mplsLdpHelloAdjacencyHoldTimeRem,
       "mplsLdpHelloAdjacencyHoldTime": mplsLdpHelloAdjacencyHoldTime,
       "mplsLdpHelloAdjacencyType": mplsLdpHelloAdjacencyType,
       "mplsInSegmentLdpLspTable": mplsInSegmentLdpLspTable,
       "mplsInSegmentLdpLspEntry": mplsInSegmentLdpLspEntry,
       "mplsInSegmentLdpLspIndex": mplsInSegmentLdpLspIndex,
       "mplsInSegmentLdpLspLabelType": mplsInSegmentLdpLspLabelType,
       "mplsInSegmentLdpLspType": mplsInSegmentLdpLspType,
       "mplsOutSegmentLdpLspTable": mplsOutSegmentLdpLspTable,
       "mplsOutSegmentLdpLspEntry": mplsOutSegmentLdpLspEntry,
       "mplsOutSegmentLdpLspIndex": mplsOutSegmentLdpLspIndex,
       "mplsOutSegmentLdpLspLabelType": mplsOutSegmentLdpLspLabelType,
       "mplsOutSegmentLdpLspType": mplsOutSegmentLdpLspType,
       "mplsFecObjects": mplsFecObjects,
       "mplsFecLastChange": mplsFecLastChange,
       "mplsFecIndexNext": mplsFecIndexNext,
       "mplsFecTable": mplsFecTable,
       "mplsFecEntry": mplsFecEntry,
       "mplsFecIndex": mplsFecIndex,
       "mplsFecType": mplsFecType,
       "mplsFecAddrPrefixLength": mplsFecAddrPrefixLength,
       "mplsFecAddrType": mplsFecAddrType,
       "mplsFecAddr": mplsFecAddr,
       "mplsFecStorageType": mplsFecStorageType,
       "mplsFecRowStatus": mplsFecRowStatus,
       "mplsLdpLspFecLastChange": mplsLdpLspFecLastChange,
       "mplsLdpLspFecTable": mplsLdpLspFecTable,
       "mplsLdpLspFecEntry": mplsLdpLspFecEntry,
       "mplsLdpLspFecSegment": mplsLdpLspFecSegment,
       "mplsLdpLspFecSegmentIndex": mplsLdpLspFecSegmentIndex,
       "mplsLdpLspFecIndex": mplsLdpLspFecIndex,
       "mplsLdpLspFecStorageType": mplsLdpLspFecStorageType,
       "mplsLdpLspFecRowStatus": mplsLdpLspFecRowStatus,
       "mplsLdpSessionPeerAddrTable": mplsLdpSessionPeerAddrTable,
       "mplsLdpSessionPeerAddrEntry": mplsLdpSessionPeerAddrEntry,
       "mplsLdpSessionPeerAddrIndex": mplsLdpSessionPeerAddrIndex,
       "mplsLdpSessionPeerNextHopAddrType": mplsLdpSessionPeerNextHopAddrType,
       "mplsLdpSessionPeerNextHopAddr": mplsLdpSessionPeerNextHopAddr,
       "mplsLdpConformance": mplsLdpConformance,
       "mplsLdpGroups": mplsLdpGroups,
       "mplsLdpGeneralGroup": mplsLdpGeneralGroup,
       "mplsLdpLspGroup": mplsLdpLspGroup,
       "mplsLdpNotificationsGroup": mplsLdpNotificationsGroup,
       "mplsLdpCompliances": mplsLdpCompliances,
       "mplsLdpModuleFullCompliance": mplsLdpModuleFullCompliance,
       "mplsLdpModuleReadOnlyCompliance": mplsLdpModuleReadOnlyCompliance}
)
