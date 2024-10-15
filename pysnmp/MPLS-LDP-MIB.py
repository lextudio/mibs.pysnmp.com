# SNMP MIB module (MPLS-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-LDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:13 2024
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

(AtmVpIdentifier,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVpIdentifier")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 experimental,
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
    "experimental",
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

mplsLdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 97)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsLsrIdentifier(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class MplsLdpGenAddr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class MplsLabel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class MplsLdpIdentifier(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class MplsLdpLabelTypes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("frameRelay", 3),
          ("generic", 1))
    )



class MplsAtmVcIdentifier(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_MplsLdpObjects_ObjectIdentity = ObjectIdentity
mplsLdpObjects = _MplsLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 1)
)
_MplsLdpLsrObjects_ObjectIdentity = ObjectIdentity
mplsLdpLsrObjects = _MplsLdpLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 1, 1)
)
_MplsLdpLsrId_Type = MplsLsrIdentifier
_MplsLdpLsrId_Object = MibScalar
mplsLdpLsrId = _MplsLdpLsrId_Object(
    (1, 3, 6, 1, 3, 97, 1, 1, 1),
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
    (1, 3, 6, 1, 3, 97, 1, 1, 2),
    _MplsLdpLsrLoopDetectionCapable_Type()
)
mplsLdpLsrLoopDetectionCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLsrLoopDetectionCapable.setStatus("current")
_MplsLdpEntityObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityObjects = _MplsLdpEntityObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 1, 2)
)


class _MplsLdpEntityIndexNext_Type(Unsigned32):
    """Custom type mplsLdpEntityIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsLdpEntityIndexNext_Type.__name__ = "Unsigned32"
_MplsLdpEntityIndexNext_Object = MibScalar
mplsLdpEntityIndexNext = _MplsLdpEntityIndexNext_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 1),
    _MplsLdpEntityIndexNext_Type()
)
mplsLdpEntityIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityIndexNext.setStatus("current")
_MplsLdpEntityTable_Object = MibTable
mplsLdpEntityTable = _MplsLdpEntityTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mplsLdpEntityTable.setStatus("current")
_MplsLdpEntityEntry_Object = MibTableRow
mplsLdpEntityEntry = _MplsLdpEntityEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1)
)
mplsLdpEntityEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityEntry.setStatus("current")
_MplsLdpEntityLdpId_Type = MplsLdpIdentifier
_MplsLdpEntityLdpId_Object = MibTableColumn
mplsLdpEntityLdpId = _MplsLdpEntityLdpId_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 1),
    _MplsLdpEntityLdpId_Type()
)
mplsLdpEntityLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityLdpId.setStatus("current")


class _MplsLdpEntityIndex_Type(Unsigned32):
    """Custom type mplsLdpEntityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsLdpEntityIndex_Type.__name__ = "Unsigned32"
_MplsLdpEntityIndex_Object = MibTableColumn
mplsLdpEntityIndex = _MplsLdpEntityIndex_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 2),
    _MplsLdpEntityIndex_Type()
)
mplsLdpEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityIndex.setStatus("current")


class _MplsLdpEntityProtocolVersion_Type(Integer32):
    """Custom type mplsLdpEntityProtocolVersion based on Integer32"""
    defaultValue = 1


_MplsLdpEntityProtocolVersion_Object = MibTableColumn
mplsLdpEntityProtocolVersion = _MplsLdpEntityProtocolVersion_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 3),
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
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 4),
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
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 0))
    )


_MplsLdpEntityOperStatus_Type.__name__ = "Integer32"
_MplsLdpEntityOperStatus_Object = MibTableColumn
mplsLdpEntityOperStatus = _MplsLdpEntityOperStatus_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 5),
    _MplsLdpEntityOperStatus_Type()
)
mplsLdpEntityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityOperStatus.setStatus("current")


class _MplsLdpEntityWellKnownTcpDiscoveryPort_Type(Unsigned32):
    """Custom type mplsLdpEntityWellKnownTcpDiscoveryPort based on Unsigned32"""
    defaultValue = 646


_MplsLdpEntityWellKnownTcpDiscoveryPort_Object = MibTableColumn
mplsLdpEntityWellKnownTcpDiscoveryPort = _MplsLdpEntityWellKnownTcpDiscoveryPort_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 6),
    _MplsLdpEntityWellKnownTcpDiscoveryPort_Type()
)
mplsLdpEntityWellKnownTcpDiscoveryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityWellKnownTcpDiscoveryPort.setStatus("current")


class _MplsLdpEntityWellKnownUdpDiscoveryPort_Type(Unsigned32):
    """Custom type mplsLdpEntityWellKnownUdpDiscoveryPort based on Unsigned32"""
    defaultValue = 646


_MplsLdpEntityWellKnownUdpDiscoveryPort_Object = MibTableColumn
mplsLdpEntityWellKnownUdpDiscoveryPort = _MplsLdpEntityWellKnownUdpDiscoveryPort_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 7),
    _MplsLdpEntityWellKnownUdpDiscoveryPort_Type()
)
mplsLdpEntityWellKnownUdpDiscoveryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityWellKnownUdpDiscoveryPort.setStatus("current")


class _MplsLdpEntityMaxPduLength_Type(Unsigned32):
    """Custom type mplsLdpEntityMaxPduLength based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsLdpEntityMaxPduLength_Type.__name__ = "Unsigned32"
_MplsLdpEntityMaxPduLength_Object = MibTableColumn
mplsLdpEntityMaxPduLength = _MplsLdpEntityMaxPduLength_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 8),
    _MplsLdpEntityMaxPduLength_Type()
)
mplsLdpEntityMaxPduLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityMaxPduLength.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpEntityMaxPduLength.setUnits("octets")


class _MplsLdpEntityKeepAliveHoldTimer_Type(Integer32):
    """Custom type mplsLdpEntityKeepAliveHoldTimer based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpEntityKeepAliveHoldTimer_Type.__name__ = "Integer32"
_MplsLdpEntityKeepAliveHoldTimer_Object = MibTableColumn
mplsLdpEntityKeepAliveHoldTimer = _MplsLdpEntityKeepAliveHoldTimer_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 9),
    _MplsLdpEntityKeepAliveHoldTimer_Type()
)
mplsLdpEntityKeepAliveHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityKeepAliveHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpEntityKeepAliveHoldTimer.setUnits("seconds")


class _MplsLdpEntityHelloHoldTimer_Type(Integer32):
    """Custom type mplsLdpEntityHelloHoldTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsLdpEntityHelloHoldTimer_Type.__name__ = "Integer32"
_MplsLdpEntityHelloHoldTimer_Object = MibTableColumn
mplsLdpEntityHelloHoldTimer = _MplsLdpEntityHelloHoldTimer_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 10),
    _MplsLdpEntityHelloHoldTimer_Type()
)
mplsLdpEntityHelloHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityHelloHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpEntityHelloHoldTimer.setUnits("seconds")


class _MplsLdpEntityFailedInitSessionTrapEnable_Type(Integer32):
    """Custom type mplsLdpEntityFailedInitSessionTrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MplsLdpEntityFailedInitSessionTrapEnable_Type.__name__ = "Integer32"
_MplsLdpEntityFailedInitSessionTrapEnable_Object = MibTableColumn
mplsLdpEntityFailedInitSessionTrapEnable = _MplsLdpEntityFailedInitSessionTrapEnable_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 11),
    _MplsLdpEntityFailedInitSessionTrapEnable_Type()
)
mplsLdpEntityFailedInitSessionTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFailedInitSessionTrapEnable.setStatus("current")


class _MplsLdpEntityFailedInitSessionThreshold_Type(Integer32):
    """Custom type mplsLdpEntityFailedInitSessionThreshold based on Integer32"""
    defaultValue = 8


_MplsLdpEntityFailedInitSessionThreshold_Object = MibTableColumn
mplsLdpEntityFailedInitSessionThreshold = _MplsLdpEntityFailedInitSessionThreshold_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 12),
    _MplsLdpEntityFailedInitSessionThreshold_Type()
)
mplsLdpEntityFailedInitSessionThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFailedInitSessionThreshold.setStatus("current")


class _MplsLdpEntityLabelDistributionMethod_Type(Integer32):
    """Custom type mplsLdpEntityLabelDistributionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstreamOnDemand", 1),
          ("downstreamUnsolicited", 2))
    )


_MplsLdpEntityLabelDistributionMethod_Type.__name__ = "Integer32"
_MplsLdpEntityLabelDistributionMethod_Object = MibTableColumn
mplsLdpEntityLabelDistributionMethod = _MplsLdpEntityLabelDistributionMethod_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 13),
    _MplsLdpEntityLabelDistributionMethod_Type()
)
mplsLdpEntityLabelDistributionMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityLabelDistributionMethod.setStatus("current")


class _MplsLdpEntityLabelRetentionMode_Type(Integer32):
    """Custom type mplsLdpEntityLabelRetentionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conservative", 1),
          ("liberal", 2))
    )


_MplsLdpEntityLabelRetentionMode_Type.__name__ = "Integer32"
_MplsLdpEntityLabelRetentionMode_Object = MibTableColumn
mplsLdpEntityLabelRetentionMode = _MplsLdpEntityLabelRetentionMode_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 14),
    _MplsLdpEntityLabelRetentionMode_Type()
)
mplsLdpEntityLabelRetentionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityLabelRetentionMode.setStatus("current")


class _MplsLdpEntityPVLimitMismatchTrapEnable_Type(Integer32):
    """Custom type mplsLdpEntityPVLimitMismatchTrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MplsLdpEntityPVLimitMismatchTrapEnable_Type.__name__ = "Integer32"
_MplsLdpEntityPVLimitMismatchTrapEnable_Object = MibTableColumn
mplsLdpEntityPVLimitMismatchTrapEnable = _MplsLdpEntityPVLimitMismatchTrapEnable_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 15),
    _MplsLdpEntityPVLimitMismatchTrapEnable_Type()
)
mplsLdpEntityPVLimitMismatchTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityPVLimitMismatchTrapEnable.setStatus("current")


class _MplsLdpEntityPathVectorLimit_Type(Integer32):
    """Custom type mplsLdpEntityPathVectorLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLdpEntityPathVectorLimit_Type.__name__ = "Integer32"
_MplsLdpEntityPathVectorLimit_Object = MibTableColumn
mplsLdpEntityPathVectorLimit = _MplsLdpEntityPathVectorLimit_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 16),
    _MplsLdpEntityPathVectorLimit_Type()
)
mplsLdpEntityPathVectorLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityPathVectorLimit.setStatus("current")


class _MplsLdpEntityHopCountLimit_Type(Integer32):
    """Custom type mplsLdpEntityHopCountLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLdpEntityHopCountLimit_Type.__name__ = "Integer32"
_MplsLdpEntityHopCountLimit_Object = MibTableColumn
mplsLdpEntityHopCountLimit = _MplsLdpEntityHopCountLimit_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 17),
    _MplsLdpEntityHopCountLimit_Type()
)
mplsLdpEntityHopCountLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityHopCountLimit.setStatus("current")


class _MplsLdpEntityTargetedPeer_Type(TruthValue):
    """Custom type mplsLdpEntityTargetedPeer based on TruthValue"""


_MplsLdpEntityTargetedPeer_Object = MibTableColumn
mplsLdpEntityTargetedPeer = _MplsLdpEntityTargetedPeer_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 18),
    _MplsLdpEntityTargetedPeer_Type()
)
mplsLdpEntityTargetedPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTargetedPeer.setStatus("current")
_MplsLdpEntityTargetedPeerAddrType_Type = AddressFamilyNumbers
_MplsLdpEntityTargetedPeerAddrType_Object = MibTableColumn
mplsLdpEntityTargetedPeerAddrType = _MplsLdpEntityTargetedPeerAddrType_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 19),
    _MplsLdpEntityTargetedPeerAddrType_Type()
)
mplsLdpEntityTargetedPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTargetedPeerAddrType.setStatus("current")
_MplsLdpEntityTargetedPeerAddr_Type = MplsLdpGenAddr
_MplsLdpEntityTargetedPeerAddr_Object = MibTableColumn
mplsLdpEntityTargetedPeerAddr = _MplsLdpEntityTargetedPeerAddr_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 20),
    _MplsLdpEntityTargetedPeerAddr_Type()
)
mplsLdpEntityTargetedPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTargetedPeerAddr.setStatus("current")
_MplsLdpEntityOptionalParameters_Type = MplsLdpLabelTypes
_MplsLdpEntityOptionalParameters_Object = MibTableColumn
mplsLdpEntityOptionalParameters = _MplsLdpEntityOptionalParameters_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 21),
    _MplsLdpEntityOptionalParameters_Type()
)
mplsLdpEntityOptionalParameters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityOptionalParameters.setStatus("current")
_MplsLdpEntityDiscontinuityTime_Type = TimeStamp
_MplsLdpEntityDiscontinuityTime_Object = MibTableColumn
mplsLdpEntityDiscontinuityTime = _MplsLdpEntityDiscontinuityTime_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 22),
    _MplsLdpEntityDiscontinuityTime_Type()
)
mplsLdpEntityDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityDiscontinuityTime.setStatus("current")
_MplsLdpEntityStorageType_Type = StorageType
_MplsLdpEntityStorageType_Object = MibTableColumn
mplsLdpEntityStorageType = _MplsLdpEntityStorageType_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 23),
    _MplsLdpEntityStorageType_Type()
)
mplsLdpEntityStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityStorageType.setStatus("current")
_MplsLdpEntityRowStatus_Type = RowStatus
_MplsLdpEntityRowStatus_Object = MibTableColumn
mplsLdpEntityRowStatus = _MplsLdpEntityRowStatus_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 2, 1, 24),
    _MplsLdpEntityRowStatus_Type()
)
mplsLdpEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityRowStatus.setStatus("current")
_MplsLdpEntityGenericObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityGenericObjects = _MplsLdpEntityGenericObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 1, 2, 3)
)
_MplsLdpEntityConfGenericLabelRangeTable_Object = MibTable
mplsLdpEntityConfGenericLabelRangeTable = _MplsLdpEntityConfGenericLabelRangeTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityConfGenericLabelRangeTable.setStatus("current")
_MplsLdpEntityConfGenericLabelRangeEntry_Object = MibTableRow
mplsLdpEntityConfGenericLabelRangeEntry = _MplsLdpEntityConfGenericLabelRangeEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 3, 1, 1)
)
mplsLdpEntityConfGenericLabelRangeEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityConfGenericLabelRangeMinimum"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityConfGenericLabelRangeMaximum"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityConfGenericLabelRangeEntry.setStatus("current")


class _MplsLdpEntityConfGenericLabelRangeMinimum_Type(Unsigned32):
    """Custom type mplsLdpEntityConfGenericLabelRangeMinimum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_MplsLdpEntityConfGenericLabelRangeMinimum_Type.__name__ = "Unsigned32"
_MplsLdpEntityConfGenericLabelRangeMinimum_Object = MibTableColumn
mplsLdpEntityConfGenericLabelRangeMinimum = _MplsLdpEntityConfGenericLabelRangeMinimum_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 3, 1, 1, 1),
    _MplsLdpEntityConfGenericLabelRangeMinimum_Type()
)
mplsLdpEntityConfGenericLabelRangeMinimum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityConfGenericLabelRangeMinimum.setStatus("current")


class _MplsLdpEntityConfGenericLabelRangeMaximum_Type(Unsigned32):
    """Custom type mplsLdpEntityConfGenericLabelRangeMaximum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_MplsLdpEntityConfGenericLabelRangeMaximum_Type.__name__ = "Unsigned32"
_MplsLdpEntityConfGenericLabelRangeMaximum_Object = MibTableColumn
mplsLdpEntityConfGenericLabelRangeMaximum = _MplsLdpEntityConfGenericLabelRangeMaximum_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 3, 1, 1, 2),
    _MplsLdpEntityConfGenericLabelRangeMaximum_Type()
)
mplsLdpEntityConfGenericLabelRangeMaximum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityConfGenericLabelRangeMaximum.setStatus("current")
_MplsLdpEntityConfGenericIfIndexOrZero_Type = InterfaceIndexOrZero
_MplsLdpEntityConfGenericIfIndexOrZero_Object = MibTableColumn
mplsLdpEntityConfGenericIfIndexOrZero = _MplsLdpEntityConfGenericIfIndexOrZero_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 3, 1, 1, 3),
    _MplsLdpEntityConfGenericIfIndexOrZero_Type()
)
mplsLdpEntityConfGenericIfIndexOrZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityConfGenericIfIndexOrZero.setStatus("current")
_MplsLdpEntityConfGenericLabelRangeStorageType_Type = StorageType
_MplsLdpEntityConfGenericLabelRangeStorageType_Object = MibTableColumn
mplsLdpEntityConfGenericLabelRangeStorageType = _MplsLdpEntityConfGenericLabelRangeStorageType_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 3, 1, 1, 4),
    _MplsLdpEntityConfGenericLabelRangeStorageType_Type()
)
mplsLdpEntityConfGenericLabelRangeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityConfGenericLabelRangeStorageType.setStatus("current")
_MplsLdpEntityConfGenericLabelRangeRowStatus_Type = RowStatus
_MplsLdpEntityConfGenericLabelRangeRowStatus_Object = MibTableColumn
mplsLdpEntityConfGenericLabelRangeRowStatus = _MplsLdpEntityConfGenericLabelRangeRowStatus_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 3, 1, 1, 5),
    _MplsLdpEntityConfGenericLabelRangeRowStatus_Type()
)
mplsLdpEntityConfGenericLabelRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityConfGenericLabelRangeRowStatus.setStatus("current")
_MplsLdpEntityAtmObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityAtmObjects = _MplsLdpEntityAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 1, 2, 4)
)
_MplsLdpEntityAtmParmsTable_Object = MibTable
mplsLdpEntityAtmParmsTable = _MplsLdpEntityAtmParmsTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityAtmParmsTable.setStatus("current")
_MplsLdpEntityAtmParmsEntry_Object = MibTableRow
mplsLdpEntityAtmParmsEntry = _MplsLdpEntityAtmParmsEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 1, 1)
)
mplsLdpEntityAtmParmsEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityAtmParmsEntry.setStatus("current")
_MplsLdpEntityAtmIfIndexOrZero_Type = InterfaceIndexOrZero
_MplsLdpEntityAtmIfIndexOrZero_Object = MibTableColumn
mplsLdpEntityAtmIfIndexOrZero = _MplsLdpEntityAtmIfIndexOrZero_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 1, 1, 1),
    _MplsLdpEntityAtmIfIndexOrZero_Type()
)
mplsLdpEntityAtmIfIndexOrZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmIfIndexOrZero.setStatus("current")


class _MplsLdpEntityAtmMergeCap_Type(Integer32):
    """Custom type mplsLdpEntityAtmMergeCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("vcMerge", 2))
    )


_MplsLdpEntityAtmMergeCap_Type.__name__ = "Integer32"
_MplsLdpEntityAtmMergeCap_Object = MibTableColumn
mplsLdpEntityAtmMergeCap = _MplsLdpEntityAtmMergeCap_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 1, 1, 2),
    _MplsLdpEntityAtmMergeCap_Type()
)
mplsLdpEntityAtmMergeCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmMergeCap.setStatus("current")


class _MplsLdpEntityAtmLabelRangeComponents_Type(Unsigned32):
    """Custom type mplsLdpEntityAtmLabelRangeComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpEntityAtmLabelRangeComponents_Type.__name__ = "Unsigned32"
_MplsLdpEntityAtmLabelRangeComponents_Object = MibTableColumn
mplsLdpEntityAtmLabelRangeComponents = _MplsLdpEntityAtmLabelRangeComponents_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 1, 1, 3),
    _MplsLdpEntityAtmLabelRangeComponents_Type()
)
mplsLdpEntityAtmLabelRangeComponents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLabelRangeComponents.setStatus("current")


class _MplsLdpEntityAtmVcDirectionality_Type(Integer32):
    """Custom type mplsLdpEntityAtmVcDirectionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 0),
          ("unidirectional", 1))
    )


_MplsLdpEntityAtmVcDirectionality_Type.__name__ = "Integer32"
_MplsLdpEntityAtmVcDirectionality_Object = MibTableColumn
mplsLdpEntityAtmVcDirectionality = _MplsLdpEntityAtmVcDirectionality_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 1, 1, 4),
    _MplsLdpEntityAtmVcDirectionality_Type()
)
mplsLdpEntityAtmVcDirectionality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmVcDirectionality.setStatus("current")


class _MplsLdpEntityAtmLsrConnectivity_Type(Integer32):
    """Custom type mplsLdpEntityAtmLsrConnectivity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("indirect", 2))
    )


_MplsLdpEntityAtmLsrConnectivity_Type.__name__ = "Integer32"
_MplsLdpEntityAtmLsrConnectivity_Object = MibTableColumn
mplsLdpEntityAtmLsrConnectivity = _MplsLdpEntityAtmLsrConnectivity_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 1, 1, 5),
    _MplsLdpEntityAtmLsrConnectivity_Type()
)
mplsLdpEntityAtmLsrConnectivity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLsrConnectivity.setStatus("current")


class _MplsLdpEntityDefaultControlVpi_Type(AtmVpIdentifier):
    """Custom type mplsLdpEntityDefaultControlVpi based on AtmVpIdentifier"""
    defaultValue = 0


_MplsLdpEntityDefaultControlVpi_Object = MibTableColumn
mplsLdpEntityDefaultControlVpi = _MplsLdpEntityDefaultControlVpi_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 1, 1, 6),
    _MplsLdpEntityDefaultControlVpi_Type()
)
mplsLdpEntityDefaultControlVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityDefaultControlVpi.setStatus("current")


class _MplsLdpEntityDefaultControlVci_Type(MplsAtmVcIdentifier):
    """Custom type mplsLdpEntityDefaultControlVci based on MplsAtmVcIdentifier"""
    defaultValue = 32


_MplsLdpEntityDefaultControlVci_Object = MibTableColumn
mplsLdpEntityDefaultControlVci = _MplsLdpEntityDefaultControlVci_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 1, 1, 7),
    _MplsLdpEntityDefaultControlVci_Type()
)
mplsLdpEntityDefaultControlVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityDefaultControlVci.setStatus("current")


class _MplsLdpEntityUnlabTrafVpi_Type(AtmVpIdentifier):
    """Custom type mplsLdpEntityUnlabTrafVpi based on AtmVpIdentifier"""
    defaultValue = 0


_MplsLdpEntityUnlabTrafVpi_Object = MibTableColumn
mplsLdpEntityUnlabTrafVpi = _MplsLdpEntityUnlabTrafVpi_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 1, 1, 8),
    _MplsLdpEntityUnlabTrafVpi_Type()
)
mplsLdpEntityUnlabTrafVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityUnlabTrafVpi.setStatus("current")


class _MplsLdpEntityUnlabTrafVci_Type(MplsAtmVcIdentifier):
    """Custom type mplsLdpEntityUnlabTrafVci based on MplsAtmVcIdentifier"""
    defaultValue = 32


_MplsLdpEntityUnlabTrafVci_Object = MibTableColumn
mplsLdpEntityUnlabTrafVci = _MplsLdpEntityUnlabTrafVci_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 1, 1, 9),
    _MplsLdpEntityUnlabTrafVci_Type()
)
mplsLdpEntityUnlabTrafVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityUnlabTrafVci.setStatus("current")
_MplsLdpEntityAtmStorageType_Type = StorageType
_MplsLdpEntityAtmStorageType_Object = MibTableColumn
mplsLdpEntityAtmStorageType = _MplsLdpEntityAtmStorageType_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 1, 1, 10),
    _MplsLdpEntityAtmStorageType_Type()
)
mplsLdpEntityAtmStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmStorageType.setStatus("current")
_MplsLdpEntityAtmRowStatus_Type = RowStatus
_MplsLdpEntityAtmRowStatus_Object = MibTableColumn
mplsLdpEntityAtmRowStatus = _MplsLdpEntityAtmRowStatus_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 1, 1, 11),
    _MplsLdpEntityAtmRowStatus_Type()
)
mplsLdpEntityAtmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmRowStatus.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeTable_Object = MibTable
mplsLdpEntityConfAtmLabelRangeTable = _MplsLdpEntityConfAtmLabelRangeTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeTable.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeEntry_Object = MibTableRow
mplsLdpEntityConfAtmLabelRangeEntry = _MplsLdpEntityConfAtmLabelRangeEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 2, 1)
)
mplsLdpEntityConfAtmLabelRangeEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityConfAtmLabelRangeMinimumVpi"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityConfAtmLabelRangeMinimumVci"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeEntry.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeMinimumVpi_Type = AtmVpIdentifier
_MplsLdpEntityConfAtmLabelRangeMinimumVpi_Object = MibTableColumn
mplsLdpEntityConfAtmLabelRangeMinimumVpi = _MplsLdpEntityConfAtmLabelRangeMinimumVpi_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 2, 1, 1),
    _MplsLdpEntityConfAtmLabelRangeMinimumVpi_Type()
)
mplsLdpEntityConfAtmLabelRangeMinimumVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeMinimumVpi.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeMinimumVci_Type = MplsAtmVcIdentifier
_MplsLdpEntityConfAtmLabelRangeMinimumVci_Object = MibTableColumn
mplsLdpEntityConfAtmLabelRangeMinimumVci = _MplsLdpEntityConfAtmLabelRangeMinimumVci_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 2, 1, 2),
    _MplsLdpEntityConfAtmLabelRangeMinimumVci_Type()
)
mplsLdpEntityConfAtmLabelRangeMinimumVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeMinimumVci.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeMaximumVpi_Type = AtmVpIdentifier
_MplsLdpEntityConfAtmLabelRangeMaximumVpi_Object = MibTableColumn
mplsLdpEntityConfAtmLabelRangeMaximumVpi = _MplsLdpEntityConfAtmLabelRangeMaximumVpi_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 2, 1, 3),
    _MplsLdpEntityConfAtmLabelRangeMaximumVpi_Type()
)
mplsLdpEntityConfAtmLabelRangeMaximumVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeMaximumVpi.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeMaximumVci_Type = MplsAtmVcIdentifier
_MplsLdpEntityConfAtmLabelRangeMaximumVci_Object = MibTableColumn
mplsLdpEntityConfAtmLabelRangeMaximumVci = _MplsLdpEntityConfAtmLabelRangeMaximumVci_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 2, 1, 4),
    _MplsLdpEntityConfAtmLabelRangeMaximumVci_Type()
)
mplsLdpEntityConfAtmLabelRangeMaximumVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeMaximumVci.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeStorageType_Type = StorageType
_MplsLdpEntityConfAtmLabelRangeStorageType_Object = MibTableColumn
mplsLdpEntityConfAtmLabelRangeStorageType = _MplsLdpEntityConfAtmLabelRangeStorageType_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 2, 1, 5),
    _MplsLdpEntityConfAtmLabelRangeStorageType_Type()
)
mplsLdpEntityConfAtmLabelRangeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeStorageType.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeRowStatus_Type = RowStatus
_MplsLdpEntityConfAtmLabelRangeRowStatus_Object = MibTableColumn
mplsLdpEntityConfAtmLabelRangeRowStatus = _MplsLdpEntityConfAtmLabelRangeRowStatus_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 4, 2, 1, 6),
    _MplsLdpEntityConfAtmLabelRangeRowStatus_Type()
)
mplsLdpEntityConfAtmLabelRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeRowStatus.setStatus("current")
_MplsLdpEntityFrameRelayObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityFrameRelayObjects = _MplsLdpEntityFrameRelayObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 1, 2, 5)
)
_MplsLdpEntityFrameRelayParmsTable_Object = MibTable
mplsLdpEntityFrameRelayParmsTable = _MplsLdpEntityFrameRelayParmsTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayParmsTable.setStatus("current")
_MplsLdpEntityFrameRelayParmsEntry_Object = MibTableRow
mplsLdpEntityFrameRelayParmsEntry = _MplsLdpEntityFrameRelayParmsEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1)
)
mplsLdpEntityFrameRelayParmsEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayParmsEntry.setStatus("current")
_MplsLdpEntityFrIfIndexOrZero_Type = InterfaceIndexOrZero
_MplsLdpEntityFrIfIndexOrZero_Object = MibTableColumn
mplsLdpEntityFrIfIndexOrZero = _MplsLdpEntityFrIfIndexOrZero_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 1),
    _MplsLdpEntityFrIfIndexOrZero_Type()
)
mplsLdpEntityFrIfIndexOrZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrIfIndexOrZero.setStatus("current")


class _MplsLdpEntityFrMergeCap_Type(Integer32):
    """Custom type mplsLdpEntityFrMergeCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("supported", 1))
    )


_MplsLdpEntityFrMergeCap_Type.__name__ = "Integer32"
_MplsLdpEntityFrMergeCap_Object = MibTableColumn
mplsLdpEntityFrMergeCap = _MplsLdpEntityFrMergeCap_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 2),
    _MplsLdpEntityFrMergeCap_Type()
)
mplsLdpEntityFrMergeCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrMergeCap.setStatus("current")


class _MplsLdpEntityFrLabelRangeComponents_Type(Unsigned32):
    """Custom type mplsLdpEntityFrLabelRangeComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpEntityFrLabelRangeComponents_Type.__name__ = "Unsigned32"
_MplsLdpEntityFrLabelRangeComponents_Object = MibTableColumn
mplsLdpEntityFrLabelRangeComponents = _MplsLdpEntityFrLabelRangeComponents_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 3),
    _MplsLdpEntityFrLabelRangeComponents_Type()
)
mplsLdpEntityFrLabelRangeComponents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrLabelRangeComponents.setStatus("current")


class _MplsLdpEntityFrLen_Type(Integer32):
    """Custom type mplsLdpEntityFrLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenDlciBits", 0),
          ("twentyThreeDlciBits", 2))
    )


_MplsLdpEntityFrLen_Type.__name__ = "Integer32"
_MplsLdpEntityFrLen_Object = MibTableColumn
mplsLdpEntityFrLen = _MplsLdpEntityFrLen_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 4),
    _MplsLdpEntityFrLen_Type()
)
mplsLdpEntityFrLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrLen.setStatus("current")


class _MplsLdpEntityFrVcDirectionality_Type(Integer32):
    """Custom type mplsLdpEntityFrVcDirectionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 0),
          ("unidirection", 1))
    )


_MplsLdpEntityFrVcDirectionality_Type.__name__ = "Integer32"
_MplsLdpEntityFrVcDirectionality_Object = MibTableColumn
mplsLdpEntityFrVcDirectionality = _MplsLdpEntityFrVcDirectionality_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 5),
    _MplsLdpEntityFrVcDirectionality_Type()
)
mplsLdpEntityFrVcDirectionality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrVcDirectionality.setStatus("current")
_MplsLdpEntityFrParmsStorageType_Type = StorageType
_MplsLdpEntityFrParmsStorageType_Object = MibTableColumn
mplsLdpEntityFrParmsStorageType = _MplsLdpEntityFrParmsStorageType_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 6),
    _MplsLdpEntityFrParmsStorageType_Type()
)
mplsLdpEntityFrParmsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrParmsStorageType.setStatus("current")
_MplsLdpEntityFrParmsRowStatus_Type = RowStatus
_MplsLdpEntityFrParmsRowStatus_Object = MibTableColumn
mplsLdpEntityFrParmsRowStatus = _MplsLdpEntityFrParmsRowStatus_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 1, 1, 7),
    _MplsLdpEntityFrParmsRowStatus_Type()
)
mplsLdpEntityFrParmsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrParmsRowStatus.setStatus("current")
_MplsLdpEntityConfFrLabelRangeTable_Object = MibTable
mplsLdpEntityConfFrLabelRangeTable = _MplsLdpEntityConfFrLabelRangeTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    mplsLdpEntityConfFrLabelRangeTable.setStatus("current")
_MplsLdpEntityConfFrLabelRangeEntry_Object = MibTableRow
mplsLdpEntityConfFrLabelRangeEntry = _MplsLdpEntityConfFrLabelRangeEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 2, 1)
)
mplsLdpEntityConfFrLabelRangeEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpConfFrMinimumDlci"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityConfFrLabelRangeEntry.setStatus("current")


class _MplsLdpConfFrMinimumDlci_Type(Integer32):
    """Custom type mplsLdpConfFrMinimumDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_MplsLdpConfFrMinimumDlci_Type.__name__ = "Integer32"
_MplsLdpConfFrMinimumDlci_Object = MibTableColumn
mplsLdpConfFrMinimumDlci = _MplsLdpConfFrMinimumDlci_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 2, 1, 1),
    _MplsLdpConfFrMinimumDlci_Type()
)
mplsLdpConfFrMinimumDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpConfFrMinimumDlci.setStatus("current")


class _MplsLdpConfFrMaximumDlci_Type(Integer32):
    """Custom type mplsLdpConfFrMaximumDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_MplsLdpConfFrMaximumDlci_Type.__name__ = "Integer32"
_MplsLdpConfFrMaximumDlci_Object = MibTableColumn
mplsLdpConfFrMaximumDlci = _MplsLdpConfFrMaximumDlci_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 2, 1, 2),
    _MplsLdpConfFrMaximumDlci_Type()
)
mplsLdpConfFrMaximumDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpConfFrMaximumDlci.setStatus("current")
_MplsLdpConfFrStorageType_Type = StorageType
_MplsLdpConfFrStorageType_Object = MibTableColumn
mplsLdpConfFrStorageType = _MplsLdpConfFrStorageType_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 2, 1, 3),
    _MplsLdpConfFrStorageType_Type()
)
mplsLdpConfFrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpConfFrStorageType.setStatus("current")
_MplsLdpConfFrRowStatus_Type = RowStatus
_MplsLdpConfFrRowStatus_Object = MibTableColumn
mplsLdpConfFrRowStatus = _MplsLdpConfFrRowStatus_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 5, 2, 1, 4),
    _MplsLdpConfFrRowStatus_Type()
)
mplsLdpConfFrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpConfFrRowStatus.setStatus("current")
_MplsLdpEntityStatsTable_Object = MibTable
mplsLdpEntityStatsTable = _MplsLdpEntityStatsTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mplsLdpEntityStatsTable.setStatus("current")
_MplsLdpEntityStatsEntry_Object = MibTableRow
mplsLdpEntityStatsEntry = _MplsLdpEntityStatsEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityStatsEntry.setStatus("current")
_MplsLdpAttemptedSessions_Type = Counter32
_MplsLdpAttemptedSessions_Object = MibTableColumn
mplsLdpAttemptedSessions = _MplsLdpAttemptedSessions_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6, 1, 1),
    _MplsLdpAttemptedSessions_Type()
)
mplsLdpAttemptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpAttemptedSessions.setStatus("current")
_MplsLdpSessionRejectedNoHelloErrors_Type = Counter32
_MplsLdpSessionRejectedNoHelloErrors_Object = MibTableColumn
mplsLdpSessionRejectedNoHelloErrors = _MplsLdpSessionRejectedNoHelloErrors_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6, 1, 2),
    _MplsLdpSessionRejectedNoHelloErrors_Type()
)
mplsLdpSessionRejectedNoHelloErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionRejectedNoHelloErrors.setStatus("current")
_MplsLdpSessionRejectedAdvertisementErrors_Type = Counter32
_MplsLdpSessionRejectedAdvertisementErrors_Object = MibTableColumn
mplsLdpSessionRejectedAdvertisementErrors = _MplsLdpSessionRejectedAdvertisementErrors_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6, 1, 3),
    _MplsLdpSessionRejectedAdvertisementErrors_Type()
)
mplsLdpSessionRejectedAdvertisementErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionRejectedAdvertisementErrors.setStatus("current")
_MplsLdpSessionRejectedMaxPduErrors_Type = Counter32
_MplsLdpSessionRejectedMaxPduErrors_Object = MibTableColumn
mplsLdpSessionRejectedMaxPduErrors = _MplsLdpSessionRejectedMaxPduErrors_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6, 1, 4),
    _MplsLdpSessionRejectedMaxPduErrors_Type()
)
mplsLdpSessionRejectedMaxPduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionRejectedMaxPduErrors.setStatus("current")
_MplsLdpSessionRejectedLabelRangeErrors_Type = Counter32
_MplsLdpSessionRejectedLabelRangeErrors_Object = MibTableColumn
mplsLdpSessionRejectedLabelRangeErrors = _MplsLdpSessionRejectedLabelRangeErrors_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6, 1, 5),
    _MplsLdpSessionRejectedLabelRangeErrors_Type()
)
mplsLdpSessionRejectedLabelRangeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionRejectedLabelRangeErrors.setStatus("current")
_MplsLdpBadLdpIdentifierErrors_Type = Counter32
_MplsLdpBadLdpIdentifierErrors_Object = MibTableColumn
mplsLdpBadLdpIdentifierErrors = _MplsLdpBadLdpIdentifierErrors_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6, 1, 6),
    _MplsLdpBadLdpIdentifierErrors_Type()
)
mplsLdpBadLdpIdentifierErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpBadLdpIdentifierErrors.setStatus("current")
_MplsLdpBadPduLengthErrors_Type = Counter32
_MplsLdpBadPduLengthErrors_Object = MibTableColumn
mplsLdpBadPduLengthErrors = _MplsLdpBadPduLengthErrors_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6, 1, 7),
    _MplsLdpBadPduLengthErrors_Type()
)
mplsLdpBadPduLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpBadPduLengthErrors.setStatus("current")
_MplsLdpBadMessageLengthErrors_Type = Counter32
_MplsLdpBadMessageLengthErrors_Object = MibTableColumn
mplsLdpBadMessageLengthErrors = _MplsLdpBadMessageLengthErrors_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6, 1, 8),
    _MplsLdpBadMessageLengthErrors_Type()
)
mplsLdpBadMessageLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpBadMessageLengthErrors.setStatus("current")
_MplsLdpBadTlvLengthErrors_Type = Counter32
_MplsLdpBadTlvLengthErrors_Object = MibTableColumn
mplsLdpBadTlvLengthErrors = _MplsLdpBadTlvLengthErrors_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6, 1, 9),
    _MplsLdpBadTlvLengthErrors_Type()
)
mplsLdpBadTlvLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpBadTlvLengthErrors.setStatus("current")
_MplsLdpMalformedTlvValueErrors_Type = Counter32
_MplsLdpMalformedTlvValueErrors_Object = MibTableColumn
mplsLdpMalformedTlvValueErrors = _MplsLdpMalformedTlvValueErrors_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6, 1, 10),
    _MplsLdpMalformedTlvValueErrors_Type()
)
mplsLdpMalformedTlvValueErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpMalformedTlvValueErrors.setStatus("current")
_MplsLdpKeepAliveTimerExpiredErrors_Type = Counter32
_MplsLdpKeepAliveTimerExpiredErrors_Object = MibTableColumn
mplsLdpKeepAliveTimerExpiredErrors = _MplsLdpKeepAliveTimerExpiredErrors_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6, 1, 11),
    _MplsLdpKeepAliveTimerExpiredErrors_Type()
)
mplsLdpKeepAliveTimerExpiredErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpKeepAliveTimerExpiredErrors.setStatus("current")
_MplsLdpShutdownNotifReceived_Type = Counter32
_MplsLdpShutdownNotifReceived_Object = MibTableColumn
mplsLdpShutdownNotifReceived = _MplsLdpShutdownNotifReceived_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6, 1, 12),
    _MplsLdpShutdownNotifReceived_Type()
)
mplsLdpShutdownNotifReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpShutdownNotifReceived.setStatus("current")
_MplsLdpShutdownNotifSent_Type = Counter32
_MplsLdpShutdownNotifSent_Object = MibTableColumn
mplsLdpShutdownNotifSent = _MplsLdpShutdownNotifSent_Object(
    (1, 3, 6, 1, 3, 97, 1, 2, 6, 1, 13),
    _MplsLdpShutdownNotifSent_Type()
)
mplsLdpShutdownNotifSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpShutdownNotifSent.setStatus("current")
_MplsLdpSessionObjects_ObjectIdentity = ObjectIdentity
mplsLdpSessionObjects = _MplsLdpSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 1, 3)
)
_MplsLdpPeerTable_Object = MibTable
mplsLdpPeerTable = _MplsLdpPeerTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mplsLdpPeerTable.setStatus("current")
_MplsLdpPeerEntry_Object = MibTableRow
mplsLdpPeerEntry = _MplsLdpPeerEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 1, 1)
)
mplsLdpPeerEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    mplsLdpPeerEntry.setStatus("current")
_MplsLdpPeerLdpId_Type = MplsLdpIdentifier
_MplsLdpPeerLdpId_Object = MibTableColumn
mplsLdpPeerLdpId = _MplsLdpPeerLdpId_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 1, 1, 1),
    _MplsLdpPeerLdpId_Type()
)
mplsLdpPeerLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpPeerLdpId.setStatus("current")


class _MplsLdpPeerLabelDistributionMethod_Type(Integer32):
    """Custom type mplsLdpPeerLabelDistributionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstreamOnDemand", 1),
          ("downstreamUnsolicited", 2))
    )


_MplsLdpPeerLabelDistributionMethod_Type.__name__ = "Integer32"
_MplsLdpPeerLabelDistributionMethod_Object = MibTableColumn
mplsLdpPeerLabelDistributionMethod = _MplsLdpPeerLabelDistributionMethod_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 1, 1, 2),
    _MplsLdpPeerLabelDistributionMethod_Type()
)
mplsLdpPeerLabelDistributionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerLabelDistributionMethod.setStatus("current")


class _MplsLdpPeerLoopDetectionForPV_Type(Integer32):
    """Custom type mplsLdpPeerLoopDetectionForPV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MplsLdpPeerLoopDetectionForPV_Type.__name__ = "Integer32"
_MplsLdpPeerLoopDetectionForPV_Object = MibTableColumn
mplsLdpPeerLoopDetectionForPV = _MplsLdpPeerLoopDetectionForPV_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 1, 1, 3),
    _MplsLdpPeerLoopDetectionForPV_Type()
)
mplsLdpPeerLoopDetectionForPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerLoopDetectionForPV.setStatus("current")


class _MplsLdpPeerPathVectorLimit_Type(Integer32):
    """Custom type mplsLdpPeerPathVectorLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLdpPeerPathVectorLimit_Type.__name__ = "Integer32"
_MplsLdpPeerPathVectorLimit_Object = MibTableColumn
mplsLdpPeerPathVectorLimit = _MplsLdpPeerPathVectorLimit_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 1, 1, 4),
    _MplsLdpPeerPathVectorLimit_Type()
)
mplsLdpPeerPathVectorLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerPathVectorLimit.setStatus("current")
_MplsLdpHelloAdjacencyObjects_ObjectIdentity = ObjectIdentity
mplsLdpHelloAdjacencyObjects = _MplsLdpHelloAdjacencyObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 1, 3, 2)
)
_MplsLdpHelloAdjacencyTable_Object = MibTable
mplsLdpHelloAdjacencyTable = _MplsLdpHelloAdjacencyTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyTable.setStatus("current")
_MplsLdpHelloAdjacencyEntry_Object = MibTableRow
mplsLdpHelloAdjacencyEntry = _MplsLdpHelloAdjacencyEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 2, 1, 1)
)
mplsLdpHelloAdjacencyEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpHelloAdjacencyIndex"),
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
    (1, 3, 6, 1, 3, 97, 1, 3, 2, 1, 1, 1),
    _MplsLdpHelloAdjacencyIndex_Type()
)
mplsLdpHelloAdjacencyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyIndex.setStatus("current")
_MplsLdpHelloAdjacencyHoldTimeRemaining_Type = TimeInterval
_MplsLdpHelloAdjacencyHoldTimeRemaining_Object = MibTableColumn
mplsLdpHelloAdjacencyHoldTimeRemaining = _MplsLdpHelloAdjacencyHoldTimeRemaining_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 2, 1, 1, 2),
    _MplsLdpHelloAdjacencyHoldTimeRemaining_Type()
)
mplsLdpHelloAdjacencyHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyHoldTimeRemaining.setStatus("current")


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
    (1, 3, 6, 1, 3, 97, 1, 3, 2, 1, 1, 3),
    _MplsLdpHelloAdjacencyType_Type()
)
mplsLdpHelloAdjacencyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyType.setStatus("current")


class _MplsLdpSessionUpDownTrapEnable_Type(Integer32):
    """Custom type mplsLdpSessionUpDownTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MplsLdpSessionUpDownTrapEnable_Type.__name__ = "Integer32"
_MplsLdpSessionUpDownTrapEnable_Object = MibScalar
mplsLdpSessionUpDownTrapEnable = _MplsLdpSessionUpDownTrapEnable_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 3),
    _MplsLdpSessionUpDownTrapEnable_Type()
)
mplsLdpSessionUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsLdpSessionUpDownTrapEnable.setStatus("current")
_MplsLdpSessionTable_Object = MibTable
mplsLdpSessionTable = _MplsLdpSessionTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 4)
)
if mibBuilder.loadTexts:
    mplsLdpSessionTable.setStatus("current")
_MplsLdpSessionEntry_Object = MibTableRow
mplsLdpSessionEntry = _MplsLdpSessionEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    mplsLdpSessionEntry.setStatus("current")


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
    (1, 3, 6, 1, 3, 97, 1, 3, 4, 1, 1),
    _MplsLdpSessionState_Type()
)
mplsLdpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionState.setStatus("current")


class _MplsLdpSessionProtocolVersion_Type(Integer32):
    """Custom type mplsLdpSessionProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpSessionProtocolVersion_Type.__name__ = "Integer32"
_MplsLdpSessionProtocolVersion_Object = MibTableColumn
mplsLdpSessionProtocolVersion = _MplsLdpSessionProtocolVersion_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 4, 1, 2),
    _MplsLdpSessionProtocolVersion_Type()
)
mplsLdpSessionProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionProtocolVersion.setStatus("current")
_MplsLdpSessionKeepAliveHoldTimeRemaining_Type = TimeInterval
_MplsLdpSessionKeepAliveHoldTimeRemaining_Object = MibTableColumn
mplsLdpSessionKeepAliveHoldTimeRemaining = _MplsLdpSessionKeepAliveHoldTimeRemaining_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 4, 1, 3),
    _MplsLdpSessionKeepAliveHoldTimeRemaining_Type()
)
mplsLdpSessionKeepAliveHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionKeepAliveHoldTimeRemaining.setStatus("current")


class _MplsLdpSessionMaxPduLength_Type(Unsigned32):
    """Custom type mplsLdpSessionMaxPduLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpSessionMaxPduLength_Type.__name__ = "Unsigned32"
_MplsLdpSessionMaxPduLength_Object = MibTableColumn
mplsLdpSessionMaxPduLength = _MplsLdpSessionMaxPduLength_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 4, 1, 4),
    _MplsLdpSessionMaxPduLength_Type()
)
mplsLdpSessionMaxPduLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionMaxPduLength.setStatus("current")
_MplsLdpSessionDiscontinuityTime_Type = TimeStamp
_MplsLdpSessionDiscontinuityTime_Object = MibTableColumn
mplsLdpSessionDiscontinuityTime = _MplsLdpSessionDiscontinuityTime_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 4, 1, 5),
    _MplsLdpSessionDiscontinuityTime_Type()
)
mplsLdpSessionDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionDiscontinuityTime.setStatus("current")
_MplsLdpAtmSessionTable_Object = MibTable
mplsLdpAtmSessionTable = _MplsLdpAtmSessionTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 5)
)
if mibBuilder.loadTexts:
    mplsLdpAtmSessionTable.setStatus("current")
_MplsLdpAtmSessionEntry_Object = MibTableRow
mplsLdpAtmSessionEntry = _MplsLdpAtmSessionEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 5, 1)
)
mplsLdpAtmSessionEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionAtmLabelRangeLowerBoundVpi"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionAtmLabelRangeLowerBoundVci"),
)
if mibBuilder.loadTexts:
    mplsLdpAtmSessionEntry.setStatus("current")
_MplsLdpSessionAtmLabelRangeLowerBoundVpi_Type = AtmVpIdentifier
_MplsLdpSessionAtmLabelRangeLowerBoundVpi_Object = MibTableColumn
mplsLdpSessionAtmLabelRangeLowerBoundVpi = _MplsLdpSessionAtmLabelRangeLowerBoundVpi_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 5, 1, 1),
    _MplsLdpSessionAtmLabelRangeLowerBoundVpi_Type()
)
mplsLdpSessionAtmLabelRangeLowerBoundVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLabelRangeLowerBoundVpi.setStatus("current")
_MplsLdpSessionAtmLabelRangeLowerBoundVci_Type = MplsAtmVcIdentifier
_MplsLdpSessionAtmLabelRangeLowerBoundVci_Object = MibTableColumn
mplsLdpSessionAtmLabelRangeLowerBoundVci = _MplsLdpSessionAtmLabelRangeLowerBoundVci_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 5, 1, 2),
    _MplsLdpSessionAtmLabelRangeLowerBoundVci_Type()
)
mplsLdpSessionAtmLabelRangeLowerBoundVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLabelRangeLowerBoundVci.setStatus("current")
_MplsLdpSessionAtmLabelRangeUpperBoundVpi_Type = AtmVpIdentifier
_MplsLdpSessionAtmLabelRangeUpperBoundVpi_Object = MibTableColumn
mplsLdpSessionAtmLabelRangeUpperBoundVpi = _MplsLdpSessionAtmLabelRangeUpperBoundVpi_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 5, 1, 3),
    _MplsLdpSessionAtmLabelRangeUpperBoundVpi_Type()
)
mplsLdpSessionAtmLabelRangeUpperBoundVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLabelRangeUpperBoundVpi.setStatus("current")
_MplsLdpSessionAtmLabelRangeUpperBoundVci_Type = MplsAtmVcIdentifier
_MplsLdpSessionAtmLabelRangeUpperBoundVci_Object = MibTableColumn
mplsLdpSessionAtmLabelRangeUpperBoundVci = _MplsLdpSessionAtmLabelRangeUpperBoundVci_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 5, 1, 4),
    _MplsLdpSessionAtmLabelRangeUpperBoundVci_Type()
)
mplsLdpSessionAtmLabelRangeUpperBoundVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLabelRangeUpperBoundVci.setStatus("current")
_MplsLdpFrameRelaySessionTable_Object = MibTable
mplsLdpFrameRelaySessionTable = _MplsLdpFrameRelaySessionTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 6)
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelaySessionTable.setStatus("current")
_MplsLdpFrameRelaySessionEntry_Object = MibTableRow
mplsLdpFrameRelaySessionEntry = _MplsLdpFrameRelaySessionEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 6, 1)
)
mplsLdpFrameRelaySessionEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpFrSessionMinDlci"),
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelaySessionEntry.setStatus("current")


class _MplsLdpFrSessionMinDlci_Type(Integer32):
    """Custom type mplsLdpFrSessionMinDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_MplsLdpFrSessionMinDlci_Type.__name__ = "Integer32"
_MplsLdpFrSessionMinDlci_Object = MibTableColumn
mplsLdpFrSessionMinDlci = _MplsLdpFrSessionMinDlci_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 6, 1, 1),
    _MplsLdpFrSessionMinDlci_Type()
)
mplsLdpFrSessionMinDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpFrSessionMinDlci.setStatus("current")


class _MplsLdpFrSessionMaxDlci_Type(Integer32):
    """Custom type mplsLdpFrSessionMaxDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_MplsLdpFrSessionMaxDlci_Type.__name__ = "Integer32"
_MplsLdpFrSessionMaxDlci_Object = MibTableColumn
mplsLdpFrSessionMaxDlci = _MplsLdpFrSessionMaxDlci_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 6, 1, 2),
    _MplsLdpFrSessionMaxDlci_Type()
)
mplsLdpFrSessionMaxDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpFrSessionMaxDlci.setStatus("current")


class _MplsLdpFrSessionLen_Type(Integer32):
    """Custom type mplsLdpFrSessionLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenDlciBits", 0),
          ("twentyThreeDlciBits", 2))
    )


_MplsLdpFrSessionLen_Type.__name__ = "Integer32"
_MplsLdpFrSessionLen_Object = MibTableColumn
mplsLdpFrSessionLen = _MplsLdpFrSessionLen_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 6, 1, 3),
    _MplsLdpFrSessionLen_Type()
)
mplsLdpFrSessionLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpFrSessionLen.setStatus("current")
_MplsLdpSessionStatsTable_Object = MibTable
mplsLdpSessionStatsTable = _MplsLdpSessionStatsTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 7)
)
if mibBuilder.loadTexts:
    mplsLdpSessionStatsTable.setStatus("current")
_MplsLdpSessionStatsEntry_Object = MibTableRow
mplsLdpSessionStatsEntry = _MplsLdpSessionStatsEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 7, 1)
)
if mibBuilder.loadTexts:
    mplsLdpSessionStatsEntry.setStatus("current")
_MplsLdpSessionStatsUnknownMessageTypeErrors_Type = Counter32
_MplsLdpSessionStatsUnknownMessageTypeErrors_Object = MibTableColumn
mplsLdpSessionStatsUnknownMessageTypeErrors = _MplsLdpSessionStatsUnknownMessageTypeErrors_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 7, 1, 1),
    _MplsLdpSessionStatsUnknownMessageTypeErrors_Type()
)
mplsLdpSessionStatsUnknownMessageTypeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionStatsUnknownMessageTypeErrors.setStatus("current")
_MplsLdpSessionStatsUnknownTlvErrors_Type = Counter32
_MplsLdpSessionStatsUnknownTlvErrors_Object = MibTableColumn
mplsLdpSessionStatsUnknownTlvErrors = _MplsLdpSessionStatsUnknownTlvErrors_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 7, 1, 2),
    _MplsLdpSessionStatsUnknownTlvErrors_Type()
)
mplsLdpSessionStatsUnknownTlvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionStatsUnknownTlvErrors.setStatus("current")
_MplsFecObjects_ObjectIdentity = ObjectIdentity
mplsFecObjects = _MplsFecObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 1, 3, 8)
)


class _MplsFecIndexNext_Type(Unsigned32):
    """Custom type mplsFecIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsFecIndexNext_Type.__name__ = "Unsigned32"
_MplsFecIndexNext_Object = MibScalar
mplsFecIndexNext = _MplsFecIndexNext_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 8, 1),
    _MplsFecIndexNext_Type()
)
mplsFecIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFecIndexNext.setStatus("current")
_MplsFecTable_Object = MibTable
mplsFecTable = _MplsFecTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 8, 2)
)
if mibBuilder.loadTexts:
    mplsFecTable.setStatus("current")
_MplsFecEntry_Object = MibTableRow
mplsFecEntry = _MplsFecEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 8, 2, 1)
)
mplsFecEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsFecIndex"),
)
if mibBuilder.loadTexts:
    mplsFecEntry.setStatus("current")


class _MplsFecIndex_Type(Unsigned32):
    """Custom type mplsFecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsFecIndex_Type.__name__ = "Unsigned32"
_MplsFecIndex_Object = MibTableColumn
mplsFecIndex = _MplsFecIndex_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 8, 2, 1, 1),
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
    (1, 3, 6, 1, 3, 97, 1, 3, 8, 2, 1, 2),
    _MplsFecType_Type()
)
mplsFecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFecType.setStatus("current")


class _MplsFecAddressLength_Type(Integer32):
    """Custom type mplsFecAddressLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsFecAddressLength_Type.__name__ = "Integer32"
_MplsFecAddressLength_Object = MibTableColumn
mplsFecAddressLength = _MplsFecAddressLength_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 8, 2, 1, 3),
    _MplsFecAddressLength_Type()
)
mplsFecAddressLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFecAddressLength.setStatus("current")
_MplsFecAddressFamily_Type = AddressFamilyNumbers
_MplsFecAddressFamily_Object = MibTableColumn
mplsFecAddressFamily = _MplsFecAddressFamily_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 8, 2, 1, 4),
    _MplsFecAddressFamily_Type()
)
mplsFecAddressFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFecAddressFamily.setStatus("current")
_MplsFecAddress_Type = MplsLdpGenAddr
_MplsFecAddress_Object = MibTableColumn
mplsFecAddress = _MplsFecAddress_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 8, 2, 1, 5),
    _MplsFecAddress_Type()
)
mplsFecAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFecAddress.setStatus("current")
_MplsFecStorageType_Type = StorageType
_MplsFecStorageType_Object = MibTableColumn
mplsFecStorageType = _MplsFecStorageType_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 8, 2, 1, 6),
    _MplsFecStorageType_Type()
)
mplsFecStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFecStorageType.setStatus("current")
_MplsFecRowStatus_Type = RowStatus
_MplsFecRowStatus_Object = MibTableColumn
mplsFecRowStatus = _MplsFecRowStatus_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 8, 2, 1, 7),
    _MplsFecRowStatus_Type()
)
mplsFecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFecRowStatus.setStatus("current")
_MplsLdpSessionInLabelMapTable_Object = MibTable
mplsLdpSessionInLabelMapTable = _MplsLdpSessionInLabelMapTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 9)
)
if mibBuilder.loadTexts:
    mplsLdpSessionInLabelMapTable.setStatus("current")
_MplsLdpSessionInLabelMapEntry_Object = MibTableRow
mplsLdpSessionInLabelMapEntry = _MplsLdpSessionInLabelMapEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 9, 1)
)
mplsLdpSessionInLabelMapEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionInLabelIfIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionInLabel"),
)
if mibBuilder.loadTexts:
    mplsLdpSessionInLabelMapEntry.setStatus("current")
_MplsLdpSessionInLabelIfIndex_Type = InterfaceIndex
_MplsLdpSessionInLabelIfIndex_Object = MibTableColumn
mplsLdpSessionInLabelIfIndex = _MplsLdpSessionInLabelIfIndex_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 9, 1, 1),
    _MplsLdpSessionInLabelIfIndex_Type()
)
mplsLdpSessionInLabelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionInLabelIfIndex.setStatus("current")
_MplsLdpSessionInLabel_Type = MplsLabel
_MplsLdpSessionInLabel_Object = MibTableColumn
mplsLdpSessionInLabel = _MplsLdpSessionInLabel_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 9, 1, 2),
    _MplsLdpSessionInLabel_Type()
)
mplsLdpSessionInLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionInLabel.setStatus("current")
_MplsLdpSessionInLabelType_Type = MplsLdpLabelTypes
_MplsLdpSessionInLabelType_Object = MibTableColumn
mplsLdpSessionInLabelType = _MplsLdpSessionInLabelType_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 9, 1, 3),
    _MplsLdpSessionInLabelType_Type()
)
mplsLdpSessionInLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionInLabelType.setStatus("current")


class _MplsLdpSessionInLabelConnectionType_Type(Integer32):
    """Custom type mplsLdpSessionInLabelConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("terminates", 3),
          ("unknown", 1),
          ("xconnect", 2))
    )


_MplsLdpSessionInLabelConnectionType_Type.__name__ = "Integer32"
_MplsLdpSessionInLabelConnectionType_Object = MibTableColumn
mplsLdpSessionInLabelConnectionType = _MplsLdpSessionInLabelConnectionType_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 9, 1, 4),
    _MplsLdpSessionInLabelConnectionType_Type()
)
mplsLdpSessionInLabelConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionInLabelConnectionType.setStatus("current")
_MplsLdpSessionOutLabelMapTable_Object = MibTable
mplsLdpSessionOutLabelMapTable = _MplsLdpSessionOutLabelMapTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 10)
)
if mibBuilder.loadTexts:
    mplsLdpSessionOutLabelMapTable.setStatus("current")
_MplsLdpSessionOutLabelMapEntry_Object = MibTableRow
mplsLdpSessionOutLabelMapEntry = _MplsLdpSessionOutLabelMapEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 10, 1)
)
mplsLdpSessionOutLabelMapEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionOutLabelIfIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionOutLabel"),
)
if mibBuilder.loadTexts:
    mplsLdpSessionOutLabelMapEntry.setStatus("current")
_MplsLdpSessionOutLabelIfIndex_Type = InterfaceIndex
_MplsLdpSessionOutLabelIfIndex_Object = MibTableColumn
mplsLdpSessionOutLabelIfIndex = _MplsLdpSessionOutLabelIfIndex_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 10, 1, 1),
    _MplsLdpSessionOutLabelIfIndex_Type()
)
mplsLdpSessionOutLabelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionOutLabelIfIndex.setStatus("current")
_MplsLdpSessionOutLabel_Type = MplsLabel
_MplsLdpSessionOutLabel_Object = MibTableColumn
mplsLdpSessionOutLabel = _MplsLdpSessionOutLabel_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 10, 1, 2),
    _MplsLdpSessionOutLabel_Type()
)
mplsLdpSessionOutLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionOutLabel.setStatus("current")
_MplsLdpSessionOutLabelType_Type = MplsLdpLabelTypes
_MplsLdpSessionOutLabelType_Object = MibTableColumn
mplsLdpSessionOutLabelType = _MplsLdpSessionOutLabelType_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 10, 1, 3),
    _MplsLdpSessionOutLabelType_Type()
)
mplsLdpSessionOutLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionOutLabelType.setStatus("current")


class _MplsLdpSessionOutLabelConnectionType_Type(Integer32):
    """Custom type mplsLdpSessionOutLabelConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("starts", 3),
          ("unknown", 1),
          ("xconnect", 2))
    )


_MplsLdpSessionOutLabelConnectionType_Type.__name__ = "Integer32"
_MplsLdpSessionOutLabelConnectionType_Object = MibTableColumn
mplsLdpSessionOutLabelConnectionType = _MplsLdpSessionOutLabelConnectionType_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 10, 1, 4),
    _MplsLdpSessionOutLabelConnectionType_Type()
)
mplsLdpSessionOutLabelConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionOutLabelConnectionType.setStatus("current")


class _MplsLdpSessionOutSegmentIndex_Type(Integer32):
    """Custom type mplsLdpSessionOutSegmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsLdpSessionOutSegmentIndex_Type.__name__ = "Integer32"
_MplsLdpSessionOutSegmentIndex_Object = MibTableColumn
mplsLdpSessionOutSegmentIndex = _MplsLdpSessionOutSegmentIndex_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 10, 1, 5),
    _MplsLdpSessionOutSegmentIndex_Type()
)
mplsLdpSessionOutSegmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionOutSegmentIndex.setStatus("current")
_MplsLdpSessionXCMapTable_Object = MibTable
mplsLdpSessionXCMapTable = _MplsLdpSessionXCMapTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 11)
)
if mibBuilder.loadTexts:
    mplsLdpSessionXCMapTable.setStatus("current")
_MplsLdpSessionXCMapEntry_Object = MibTableRow
mplsLdpSessionXCMapEntry = _MplsLdpSessionXCMapEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 11, 1)
)
mplsLdpSessionXCMapEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionInLabelIfIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionInLabel"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionOutLabelIfIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionOutLabel"),
)
if mibBuilder.loadTexts:
    mplsLdpSessionXCMapEntry.setStatus("current")


class _MplsLdpSessionXCIndex_Type(Integer32):
    """Custom type mplsLdpSessionXCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsLdpSessionXCIndex_Type.__name__ = "Integer32"
_MplsLdpSessionXCIndex_Object = MibTableColumn
mplsLdpSessionXCIndex = _MplsLdpSessionXCIndex_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 11, 1, 1),
    _MplsLdpSessionXCIndex_Type()
)
mplsLdpSessionXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionXCIndex.setStatus("current")
_MplsLdpSessionPeerAddressTable_Object = MibTable
mplsLdpSessionPeerAddressTable = _MplsLdpSessionPeerAddressTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 12)
)
if mibBuilder.loadTexts:
    mplsLdpSessionPeerAddressTable.setStatus("current")
_MplsLdpSessionPeerAddressEntry_Object = MibTableRow
mplsLdpSessionPeerAddressEntry = _MplsLdpSessionPeerAddressEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 12, 1)
)
mplsLdpSessionPeerAddressEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionPeerAddressIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpSessionPeerAddressEntry.setStatus("current")


class _MplsLdpSessionPeerAddressIndex_Type(Unsigned32):
    """Custom type mplsLdpSessionPeerAddressIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsLdpSessionPeerAddressIndex_Type.__name__ = "Unsigned32"
_MplsLdpSessionPeerAddressIndex_Object = MibTableColumn
mplsLdpSessionPeerAddressIndex = _MplsLdpSessionPeerAddressIndex_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 12, 1, 1),
    _MplsLdpSessionPeerAddressIndex_Type()
)
mplsLdpSessionPeerAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionPeerAddressIndex.setStatus("current")
_MplsLdpSessionPeerNextHopAddressType_Type = AddressFamilyNumbers
_MplsLdpSessionPeerNextHopAddressType_Object = MibTableColumn
mplsLdpSessionPeerNextHopAddressType = _MplsLdpSessionPeerNextHopAddressType_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 12, 1, 2),
    _MplsLdpSessionPeerNextHopAddressType_Type()
)
mplsLdpSessionPeerNextHopAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionPeerNextHopAddressType.setStatus("current")
_MplsLdpSessionPeerNextHopAddress_Type = MplsLdpGenAddr
_MplsLdpSessionPeerNextHopAddress_Object = MibTableColumn
mplsLdpSessionPeerNextHopAddress = _MplsLdpSessionPeerNextHopAddress_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 12, 1, 3),
    _MplsLdpSessionPeerNextHopAddress_Type()
)
mplsLdpSessionPeerNextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionPeerNextHopAddress.setStatus("current")
_MplsXCsFecsTable_Object = MibTable
mplsXCsFecsTable = _MplsXCsFecsTable_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 13)
)
if mibBuilder.loadTexts:
    mplsXCsFecsTable.setStatus("current")
_MplsXCsFecsEntry_Object = MibTableRow
mplsXCsFecsEntry = _MplsXCsFecsEntry_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 13, 1)
)
mplsXCsFecsEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionInLabelIfIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionInLabel"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionOutLabelIfIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionOutLabel"),
    (0, "MPLS-LDP-MIB", "mplsFecIndex"),
)
if mibBuilder.loadTexts:
    mplsXCsFecsEntry.setStatus("current")


class _MplsXCFecOperStatus_Type(Integer32):
    """Custom type mplsXCFecOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 2),
          ("notInUse", 3),
          ("unknown", 1))
    )


_MplsXCFecOperStatus_Type.__name__ = "Integer32"
_MplsXCFecOperStatus_Object = MibTableColumn
mplsXCFecOperStatus = _MplsXCFecOperStatus_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 13, 1, 1),
    _MplsXCFecOperStatus_Type()
)
mplsXCFecOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsXCFecOperStatus.setStatus("current")
_MplsXCFecOperStatusLastChange_Type = TimeStamp
_MplsXCFecOperStatusLastChange_Object = MibTableColumn
mplsXCFecOperStatusLastChange = _MplsXCFecOperStatusLastChange_Object(
    (1, 3, 6, 1, 3, 97, 1, 3, 13, 1, 2),
    _MplsXCFecOperStatusLastChange_Type()
)
mplsXCFecOperStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsXCFecOperStatusLastChange.setStatus("current")
_MplsLdpNotifications_ObjectIdentity = ObjectIdentity
mplsLdpNotifications = _MplsLdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 2)
)
_MplsLdpNotificationPrefix_ObjectIdentity = ObjectIdentity
mplsLdpNotificationPrefix = _MplsLdpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 2, 0)
)
_MplsLdpConformance_ObjectIdentity = ObjectIdentity
mplsLdpConformance = _MplsLdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 3)
)
_MplsLdpGroups_ObjectIdentity = ObjectIdentity
mplsLdpGroups = _MplsLdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 3, 1)
)
_MplsLdpCompliances_ObjectIdentity = ObjectIdentity
mplsLdpCompliances = _MplsLdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 97, 3, 2)
)
mplsLdpEntityEntry.registerAugmentions(
    ("MPLS-LDP-MIB",
     "mplsLdpEntityStatsEntry")
)
mplsLdpEntityStatsEntry.setIndexNames(*mplsLdpEntityEntry.getIndexNames())
mplsLdpPeerEntry.registerAugmentions(
    ("MPLS-LDP-MIB",
     "mplsLdpSessionEntry")
)
mplsLdpSessionEntry.setIndexNames(*mplsLdpPeerEntry.getIndexNames())
mplsLdpPeerEntry.registerAugmentions(
    ("MPLS-LDP-MIB",
     "mplsLdpSessionStatsEntry")
)
mplsLdpSessionStatsEntry.setIndexNames(*mplsLdpPeerEntry.getIndexNames())

# Managed Objects groups

mplsLdpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 97, 3, 1, 1)
)
mplsLdpGeneralGroup.setObjects(
      *(("MPLS-LDP-MIB", "mplsLdpLsrId"),
        ("MPLS-LDP-MIB", "mplsLdpLsrLoopDetectionCapable"),
        ("MPLS-LDP-MIB", "mplsLdpEntityIndexNext"),
        ("MPLS-LDP-MIB", "mplsLdpEntityProtocolVersion"),
        ("MPLS-LDP-MIB", "mplsLdpEntityAdminStatus"),
        ("MPLS-LDP-MIB", "mplsLdpEntityOperStatus"),
        ("MPLS-LDP-MIB", "mplsLdpEntityWellKnownTcpDiscoveryPort"),
        ("MPLS-LDP-MIB", "mplsLdpEntityWellKnownUdpDiscoveryPort"),
        ("MPLS-LDP-MIB", "mplsLdpEntityMaxPduLength"),
        ("MPLS-LDP-MIB", "mplsLdpEntityKeepAliveHoldTimer"),
        ("MPLS-LDP-MIB", "mplsLdpEntityHelloHoldTimer"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFailedInitSessionTrapEnable"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFailedInitSessionThreshold"),
        ("MPLS-LDP-MIB", "mplsLdpEntityLabelDistributionMethod"),
        ("MPLS-LDP-MIB", "mplsLdpEntityLabelRetentionMode"),
        ("MPLS-LDP-MIB", "mplsLdpEntityPVLimitMismatchTrapEnable"),
        ("MPLS-LDP-MIB", "mplsLdpEntityPathVectorLimit"),
        ("MPLS-LDP-MIB", "mplsLdpEntityHopCountLimit"),
        ("MPLS-LDP-MIB", "mplsLdpEntityTargetedPeer"),
        ("MPLS-LDP-MIB", "mplsLdpEntityTargetedPeerAddrType"),
        ("MPLS-LDP-MIB", "mplsLdpEntityTargetedPeerAddr"),
        ("MPLS-LDP-MIB", "mplsLdpEntityOptionalParameters"),
        ("MPLS-LDP-MIB", "mplsLdpEntityDiscontinuityTime"),
        ("MPLS-LDP-MIB", "mplsLdpEntityStorageType"),
        ("MPLS-LDP-MIB", "mplsLdpEntityRowStatus"),
        ("MPLS-LDP-MIB", "mplsLdpAttemptedSessions"),
        ("MPLS-LDP-MIB", "mplsLdpSessionRejectedNoHelloErrors"),
        ("MPLS-LDP-MIB", "mplsLdpSessionRejectedAdvertisementErrors"),
        ("MPLS-LDP-MIB", "mplsLdpSessionRejectedMaxPduErrors"),
        ("MPLS-LDP-MIB", "mplsLdpSessionRejectedLabelRangeErrors"),
        ("MPLS-LDP-MIB", "mplsLdpBadLdpIdentifierErrors"),
        ("MPLS-LDP-MIB", "mplsLdpBadPduLengthErrors"),
        ("MPLS-LDP-MIB", "mplsLdpBadMessageLengthErrors"),
        ("MPLS-LDP-MIB", "mplsLdpBadTlvLengthErrors"),
        ("MPLS-LDP-MIB", "mplsLdpMalformedTlvValueErrors"),
        ("MPLS-LDP-MIB", "mplsLdpKeepAliveTimerExpiredErrors"),
        ("MPLS-LDP-MIB", "mplsLdpShutdownNotifReceived"),
        ("MPLS-LDP-MIB", "mplsLdpShutdownNotifSent"),
        ("MPLS-LDP-MIB", "mplsLdpPeerLabelDistributionMethod"),
        ("MPLS-LDP-MIB", "mplsLdpPeerLoopDetectionForPV"),
        ("MPLS-LDP-MIB", "mplsLdpPeerPathVectorLimit"),
        ("MPLS-LDP-MIB", "mplsLdpHelloAdjacencyHoldTimeRemaining"),
        ("MPLS-LDP-MIB", "mplsLdpHelloAdjacencyType"),
        ("MPLS-LDP-MIB", "mplsLdpSessionUpDownTrapEnable"),
        ("MPLS-LDP-MIB", "mplsLdpSessionState"),
        ("MPLS-LDP-MIB", "mplsLdpSessionProtocolVersion"),
        ("MPLS-LDP-MIB", "mplsLdpSessionKeepAliveHoldTimeRemaining"),
        ("MPLS-LDP-MIB", "mplsLdpSessionMaxPduLength"),
        ("MPLS-LDP-MIB", "mplsLdpSessionDiscontinuityTime"),
        ("MPLS-LDP-MIB", "mplsLdpSessionStatsUnknownMessageTypeErrors"),
        ("MPLS-LDP-MIB", "mplsLdpSessionStatsUnknownTlvErrors"),
        ("MPLS-LDP-MIB", "mplsLdpSessionPeerNextHopAddressType"),
        ("MPLS-LDP-MIB", "mplsLdpSessionPeerNextHopAddress"),
        ("MPLS-LDP-MIB", "mplsFecIndexNext"),
        ("MPLS-LDP-MIB", "mplsFecType"),
        ("MPLS-LDP-MIB", "mplsFecAddressFamily"),
        ("MPLS-LDP-MIB", "mplsFecAddressLength"),
        ("MPLS-LDP-MIB", "mplsFecAddress"),
        ("MPLS-LDP-MIB", "mplsFecStorageType"),
        ("MPLS-LDP-MIB", "mplsFecRowStatus"))
)
if mibBuilder.loadTexts:
    mplsLdpGeneralGroup.setStatus("current")

mplsLdpGenericGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 97, 3, 1, 2)
)
mplsLdpGenericGroup.setObjects(
      *(("MPLS-LDP-MIB", "mplsLdpEntityConfGenericIfIndexOrZero"),
        ("MPLS-LDP-MIB", "mplsLdpEntityConfGenericLabelRangeStorageType"),
        ("MPLS-LDP-MIB", "mplsLdpEntityConfGenericLabelRangeRowStatus"))
)
if mibBuilder.loadTexts:
    mplsLdpGenericGroup.setStatus("current")

mplsLdpAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 97, 3, 1, 3)
)
mplsLdpAtmGroup.setObjects(
      *(("MPLS-LDP-MIB", "mplsLdpEntityAtmIfIndexOrZero"),
        ("MPLS-LDP-MIB", "mplsLdpEntityAtmMergeCap"),
        ("MPLS-LDP-MIB", "mplsLdpEntityAtmLabelRangeComponents"),
        ("MPLS-LDP-MIB", "mplsLdpEntityAtmVcDirectionality"),
        ("MPLS-LDP-MIB", "mplsLdpEntityAtmLsrConnectivity"),
        ("MPLS-LDP-MIB", "mplsLdpEntityDefaultControlVpi"),
        ("MPLS-LDP-MIB", "mplsLdpEntityDefaultControlVci"),
        ("MPLS-LDP-MIB", "mplsLdpEntityUnlabTrafVpi"),
        ("MPLS-LDP-MIB", "mplsLdpEntityUnlabTrafVci"),
        ("MPLS-LDP-MIB", "mplsLdpEntityAtmStorageType"),
        ("MPLS-LDP-MIB", "mplsLdpEntityAtmRowStatus"),
        ("MPLS-LDP-MIB", "mplsLdpEntityConfAtmLabelRangeMaximumVpi"),
        ("MPLS-LDP-MIB", "mplsLdpEntityConfAtmLabelRangeMaximumVci"),
        ("MPLS-LDP-MIB", "mplsLdpEntityConfAtmLabelRangeStorageType"),
        ("MPLS-LDP-MIB", "mplsLdpEntityConfAtmLabelRangeRowStatus"),
        ("MPLS-LDP-MIB", "mplsLdpSessionAtmLabelRangeUpperBoundVpi"),
        ("MPLS-LDP-MIB", "mplsLdpSessionAtmLabelRangeUpperBoundVci"))
)
if mibBuilder.loadTexts:
    mplsLdpAtmGroup.setStatus("current")

mplsLdpFrameRelayGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 97, 3, 1, 4)
)
mplsLdpFrameRelayGroup.setObjects(
      *(("MPLS-LDP-MIB", "mplsLdpEntityFrIfIndexOrZero"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFrMergeCap"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFrLabelRangeComponents"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFrLen"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFrVcDirectionality"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFrParmsStorageType"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFrParmsRowStatus"),
        ("MPLS-LDP-MIB", "mplsLdpConfFrMaximumDlci"),
        ("MPLS-LDP-MIB", "mplsLdpConfFrStorageType"),
        ("MPLS-LDP-MIB", "mplsLdpConfFrRowStatus"),
        ("MPLS-LDP-MIB", "mplsLdpFrSessionMaxDlci"),
        ("MPLS-LDP-MIB", "mplsLdpFrSessionLen"))
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelayGroup.setStatus("current")

mplsLdpMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 97, 3, 1, 5)
)
mplsLdpMappingGroup.setObjects(
      *(("MPLS-LDP-MIB", "mplsLdpSessionInLabelType"),
        ("MPLS-LDP-MIB", "mplsLdpSessionInLabelConnectionType"),
        ("MPLS-LDP-MIB", "mplsLdpSessionOutLabelType"),
        ("MPLS-LDP-MIB", "mplsLdpSessionOutLabelConnectionType"),
        ("MPLS-LDP-MIB", "mplsLdpSessionOutSegmentIndex"),
        ("MPLS-LDP-MIB", "mplsLdpSessionXCIndex"),
        ("MPLS-LDP-MIB", "mplsXCFecOperStatus"),
        ("MPLS-LDP-MIB", "mplsXCFecOperStatusLastChange"))
)
if mibBuilder.loadTexts:
    mplsLdpMappingGroup.setStatus("current")


# Notification objects

mplsLdpFailedInitSessionThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 3, 97, 2, 0, 1)
)
mplsLdpFailedInitSessionThresholdExceeded.setObjects(
    ("MPLS-LDP-MIB", "mplsLdpEntityFailedInitSessionThreshold")
)
if mibBuilder.loadTexts:
    mplsLdpFailedInitSessionThresholdExceeded.setStatus(
        "current"
    )

mplsLdpPathVectorLimitMismatch = NotificationType(
    (1, 3, 6, 1, 3, 97, 2, 0, 2)
)
mplsLdpPathVectorLimitMismatch.setObjects(
      *(("MPLS-LDP-MIB", "mplsLdpEntityPathVectorLimit"),
        ("MPLS-LDP-MIB", "mplsLdpPeerPathVectorLimit"))
)
if mibBuilder.loadTexts:
    mplsLdpPathVectorLimitMismatch.setStatus(
        "current"
    )

mplsLdpSessionUp = NotificationType(
    (1, 3, 6, 1, 3, 97, 2, 0, 3)
)
mplsLdpSessionUp.setObjects(
    ("MPLS-LDP-MIB", "mplsLdpSessionState")
)
if mibBuilder.loadTexts:
    mplsLdpSessionUp.setStatus(
        "current"
    )

mplsLdpSessionDown = NotificationType(
    (1, 3, 6, 1, 3, 97, 2, 0, 4)
)
mplsLdpSessionDown.setObjects(
    ("MPLS-LDP-MIB", "mplsLdpSessionState")
)
if mibBuilder.loadTexts:
    mplsLdpSessionDown.setStatus(
        "current"
    )


# Notifications groups

mplsLdpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 97, 3, 1, 6)
)
mplsLdpNotificationsGroup.setObjects(
      *(("MPLS-LDP-MIB", "mplsLdpFailedInitSessionThresholdExceeded"),
        ("MPLS-LDP-MIB", "mplsLdpPathVectorLimitMismatch"),
        ("MPLS-LDP-MIB", "mplsLdpSessionUp"),
        ("MPLS-LDP-MIB", "mplsLdpSessionDown"))
)
if mibBuilder.loadTexts:
    mplsLdpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsLdpModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 97, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLdpModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-LDP-MIB",
    **{"MplsLsrIdentifier": MplsLsrIdentifier,
       "MplsLdpGenAddr": MplsLdpGenAddr,
       "MplsLabel": MplsLabel,
       "MplsLdpIdentifier": MplsLdpIdentifier,
       "MplsLdpLabelTypes": MplsLdpLabelTypes,
       "MplsAtmVcIdentifier": MplsAtmVcIdentifier,
       "mplsLdpMIB": mplsLdpMIB,
       "mplsLdpObjects": mplsLdpObjects,
       "mplsLdpLsrObjects": mplsLdpLsrObjects,
       "mplsLdpLsrId": mplsLdpLsrId,
       "mplsLdpLsrLoopDetectionCapable": mplsLdpLsrLoopDetectionCapable,
       "mplsLdpEntityObjects": mplsLdpEntityObjects,
       "mplsLdpEntityIndexNext": mplsLdpEntityIndexNext,
       "mplsLdpEntityTable": mplsLdpEntityTable,
       "mplsLdpEntityEntry": mplsLdpEntityEntry,
       "mplsLdpEntityLdpId": mplsLdpEntityLdpId,
       "mplsLdpEntityIndex": mplsLdpEntityIndex,
       "mplsLdpEntityProtocolVersion": mplsLdpEntityProtocolVersion,
       "mplsLdpEntityAdminStatus": mplsLdpEntityAdminStatus,
       "mplsLdpEntityOperStatus": mplsLdpEntityOperStatus,
       "mplsLdpEntityWellKnownTcpDiscoveryPort": mplsLdpEntityWellKnownTcpDiscoveryPort,
       "mplsLdpEntityWellKnownUdpDiscoveryPort": mplsLdpEntityWellKnownUdpDiscoveryPort,
       "mplsLdpEntityMaxPduLength": mplsLdpEntityMaxPduLength,
       "mplsLdpEntityKeepAliveHoldTimer": mplsLdpEntityKeepAliveHoldTimer,
       "mplsLdpEntityHelloHoldTimer": mplsLdpEntityHelloHoldTimer,
       "mplsLdpEntityFailedInitSessionTrapEnable": mplsLdpEntityFailedInitSessionTrapEnable,
       "mplsLdpEntityFailedInitSessionThreshold": mplsLdpEntityFailedInitSessionThreshold,
       "mplsLdpEntityLabelDistributionMethod": mplsLdpEntityLabelDistributionMethod,
       "mplsLdpEntityLabelRetentionMode": mplsLdpEntityLabelRetentionMode,
       "mplsLdpEntityPVLimitMismatchTrapEnable": mplsLdpEntityPVLimitMismatchTrapEnable,
       "mplsLdpEntityPathVectorLimit": mplsLdpEntityPathVectorLimit,
       "mplsLdpEntityHopCountLimit": mplsLdpEntityHopCountLimit,
       "mplsLdpEntityTargetedPeer": mplsLdpEntityTargetedPeer,
       "mplsLdpEntityTargetedPeerAddrType": mplsLdpEntityTargetedPeerAddrType,
       "mplsLdpEntityTargetedPeerAddr": mplsLdpEntityTargetedPeerAddr,
       "mplsLdpEntityOptionalParameters": mplsLdpEntityOptionalParameters,
       "mplsLdpEntityDiscontinuityTime": mplsLdpEntityDiscontinuityTime,
       "mplsLdpEntityStorageType": mplsLdpEntityStorageType,
       "mplsLdpEntityRowStatus": mplsLdpEntityRowStatus,
       "mplsLdpEntityGenericObjects": mplsLdpEntityGenericObjects,
       "mplsLdpEntityConfGenericLabelRangeTable": mplsLdpEntityConfGenericLabelRangeTable,
       "mplsLdpEntityConfGenericLabelRangeEntry": mplsLdpEntityConfGenericLabelRangeEntry,
       "mplsLdpEntityConfGenericLabelRangeMinimum": mplsLdpEntityConfGenericLabelRangeMinimum,
       "mplsLdpEntityConfGenericLabelRangeMaximum": mplsLdpEntityConfGenericLabelRangeMaximum,
       "mplsLdpEntityConfGenericIfIndexOrZero": mplsLdpEntityConfGenericIfIndexOrZero,
       "mplsLdpEntityConfGenericLabelRangeStorageType": mplsLdpEntityConfGenericLabelRangeStorageType,
       "mplsLdpEntityConfGenericLabelRangeRowStatus": mplsLdpEntityConfGenericLabelRangeRowStatus,
       "mplsLdpEntityAtmObjects": mplsLdpEntityAtmObjects,
       "mplsLdpEntityAtmParmsTable": mplsLdpEntityAtmParmsTable,
       "mplsLdpEntityAtmParmsEntry": mplsLdpEntityAtmParmsEntry,
       "mplsLdpEntityAtmIfIndexOrZero": mplsLdpEntityAtmIfIndexOrZero,
       "mplsLdpEntityAtmMergeCap": mplsLdpEntityAtmMergeCap,
       "mplsLdpEntityAtmLabelRangeComponents": mplsLdpEntityAtmLabelRangeComponents,
       "mplsLdpEntityAtmVcDirectionality": mplsLdpEntityAtmVcDirectionality,
       "mplsLdpEntityAtmLsrConnectivity": mplsLdpEntityAtmLsrConnectivity,
       "mplsLdpEntityDefaultControlVpi": mplsLdpEntityDefaultControlVpi,
       "mplsLdpEntityDefaultControlVci": mplsLdpEntityDefaultControlVci,
       "mplsLdpEntityUnlabTrafVpi": mplsLdpEntityUnlabTrafVpi,
       "mplsLdpEntityUnlabTrafVci": mplsLdpEntityUnlabTrafVci,
       "mplsLdpEntityAtmStorageType": mplsLdpEntityAtmStorageType,
       "mplsLdpEntityAtmRowStatus": mplsLdpEntityAtmRowStatus,
       "mplsLdpEntityConfAtmLabelRangeTable": mplsLdpEntityConfAtmLabelRangeTable,
       "mplsLdpEntityConfAtmLabelRangeEntry": mplsLdpEntityConfAtmLabelRangeEntry,
       "mplsLdpEntityConfAtmLabelRangeMinimumVpi": mplsLdpEntityConfAtmLabelRangeMinimumVpi,
       "mplsLdpEntityConfAtmLabelRangeMinimumVci": mplsLdpEntityConfAtmLabelRangeMinimumVci,
       "mplsLdpEntityConfAtmLabelRangeMaximumVpi": mplsLdpEntityConfAtmLabelRangeMaximumVpi,
       "mplsLdpEntityConfAtmLabelRangeMaximumVci": mplsLdpEntityConfAtmLabelRangeMaximumVci,
       "mplsLdpEntityConfAtmLabelRangeStorageType": mplsLdpEntityConfAtmLabelRangeStorageType,
       "mplsLdpEntityConfAtmLabelRangeRowStatus": mplsLdpEntityConfAtmLabelRangeRowStatus,
       "mplsLdpEntityFrameRelayObjects": mplsLdpEntityFrameRelayObjects,
       "mplsLdpEntityFrameRelayParmsTable": mplsLdpEntityFrameRelayParmsTable,
       "mplsLdpEntityFrameRelayParmsEntry": mplsLdpEntityFrameRelayParmsEntry,
       "mplsLdpEntityFrIfIndexOrZero": mplsLdpEntityFrIfIndexOrZero,
       "mplsLdpEntityFrMergeCap": mplsLdpEntityFrMergeCap,
       "mplsLdpEntityFrLabelRangeComponents": mplsLdpEntityFrLabelRangeComponents,
       "mplsLdpEntityFrLen": mplsLdpEntityFrLen,
       "mplsLdpEntityFrVcDirectionality": mplsLdpEntityFrVcDirectionality,
       "mplsLdpEntityFrParmsStorageType": mplsLdpEntityFrParmsStorageType,
       "mplsLdpEntityFrParmsRowStatus": mplsLdpEntityFrParmsRowStatus,
       "mplsLdpEntityConfFrLabelRangeTable": mplsLdpEntityConfFrLabelRangeTable,
       "mplsLdpEntityConfFrLabelRangeEntry": mplsLdpEntityConfFrLabelRangeEntry,
       "mplsLdpConfFrMinimumDlci": mplsLdpConfFrMinimumDlci,
       "mplsLdpConfFrMaximumDlci": mplsLdpConfFrMaximumDlci,
       "mplsLdpConfFrStorageType": mplsLdpConfFrStorageType,
       "mplsLdpConfFrRowStatus": mplsLdpConfFrRowStatus,
       "mplsLdpEntityStatsTable": mplsLdpEntityStatsTable,
       "mplsLdpEntityStatsEntry": mplsLdpEntityStatsEntry,
       "mplsLdpAttemptedSessions": mplsLdpAttemptedSessions,
       "mplsLdpSessionRejectedNoHelloErrors": mplsLdpSessionRejectedNoHelloErrors,
       "mplsLdpSessionRejectedAdvertisementErrors": mplsLdpSessionRejectedAdvertisementErrors,
       "mplsLdpSessionRejectedMaxPduErrors": mplsLdpSessionRejectedMaxPduErrors,
       "mplsLdpSessionRejectedLabelRangeErrors": mplsLdpSessionRejectedLabelRangeErrors,
       "mplsLdpBadLdpIdentifierErrors": mplsLdpBadLdpIdentifierErrors,
       "mplsLdpBadPduLengthErrors": mplsLdpBadPduLengthErrors,
       "mplsLdpBadMessageLengthErrors": mplsLdpBadMessageLengthErrors,
       "mplsLdpBadTlvLengthErrors": mplsLdpBadTlvLengthErrors,
       "mplsLdpMalformedTlvValueErrors": mplsLdpMalformedTlvValueErrors,
       "mplsLdpKeepAliveTimerExpiredErrors": mplsLdpKeepAliveTimerExpiredErrors,
       "mplsLdpShutdownNotifReceived": mplsLdpShutdownNotifReceived,
       "mplsLdpShutdownNotifSent": mplsLdpShutdownNotifSent,
       "mplsLdpSessionObjects": mplsLdpSessionObjects,
       "mplsLdpPeerTable": mplsLdpPeerTable,
       "mplsLdpPeerEntry": mplsLdpPeerEntry,
       "mplsLdpPeerLdpId": mplsLdpPeerLdpId,
       "mplsLdpPeerLabelDistributionMethod": mplsLdpPeerLabelDistributionMethod,
       "mplsLdpPeerLoopDetectionForPV": mplsLdpPeerLoopDetectionForPV,
       "mplsLdpPeerPathVectorLimit": mplsLdpPeerPathVectorLimit,
       "mplsLdpHelloAdjacencyObjects": mplsLdpHelloAdjacencyObjects,
       "mplsLdpHelloAdjacencyTable": mplsLdpHelloAdjacencyTable,
       "mplsLdpHelloAdjacencyEntry": mplsLdpHelloAdjacencyEntry,
       "mplsLdpHelloAdjacencyIndex": mplsLdpHelloAdjacencyIndex,
       "mplsLdpHelloAdjacencyHoldTimeRemaining": mplsLdpHelloAdjacencyHoldTimeRemaining,
       "mplsLdpHelloAdjacencyType": mplsLdpHelloAdjacencyType,
       "mplsLdpSessionUpDownTrapEnable": mplsLdpSessionUpDownTrapEnable,
       "mplsLdpSessionTable": mplsLdpSessionTable,
       "mplsLdpSessionEntry": mplsLdpSessionEntry,
       "mplsLdpSessionState": mplsLdpSessionState,
       "mplsLdpSessionProtocolVersion": mplsLdpSessionProtocolVersion,
       "mplsLdpSessionKeepAliveHoldTimeRemaining": mplsLdpSessionKeepAliveHoldTimeRemaining,
       "mplsLdpSessionMaxPduLength": mplsLdpSessionMaxPduLength,
       "mplsLdpSessionDiscontinuityTime": mplsLdpSessionDiscontinuityTime,
       "mplsLdpAtmSessionTable": mplsLdpAtmSessionTable,
       "mplsLdpAtmSessionEntry": mplsLdpAtmSessionEntry,
       "mplsLdpSessionAtmLabelRangeLowerBoundVpi": mplsLdpSessionAtmLabelRangeLowerBoundVpi,
       "mplsLdpSessionAtmLabelRangeLowerBoundVci": mplsLdpSessionAtmLabelRangeLowerBoundVci,
       "mplsLdpSessionAtmLabelRangeUpperBoundVpi": mplsLdpSessionAtmLabelRangeUpperBoundVpi,
       "mplsLdpSessionAtmLabelRangeUpperBoundVci": mplsLdpSessionAtmLabelRangeUpperBoundVci,
       "mplsLdpFrameRelaySessionTable": mplsLdpFrameRelaySessionTable,
       "mplsLdpFrameRelaySessionEntry": mplsLdpFrameRelaySessionEntry,
       "mplsLdpFrSessionMinDlci": mplsLdpFrSessionMinDlci,
       "mplsLdpFrSessionMaxDlci": mplsLdpFrSessionMaxDlci,
       "mplsLdpFrSessionLen": mplsLdpFrSessionLen,
       "mplsLdpSessionStatsTable": mplsLdpSessionStatsTable,
       "mplsLdpSessionStatsEntry": mplsLdpSessionStatsEntry,
       "mplsLdpSessionStatsUnknownMessageTypeErrors": mplsLdpSessionStatsUnknownMessageTypeErrors,
       "mplsLdpSessionStatsUnknownTlvErrors": mplsLdpSessionStatsUnknownTlvErrors,
       "mplsFecObjects": mplsFecObjects,
       "mplsFecIndexNext": mplsFecIndexNext,
       "mplsFecTable": mplsFecTable,
       "mplsFecEntry": mplsFecEntry,
       "mplsFecIndex": mplsFecIndex,
       "mplsFecType": mplsFecType,
       "mplsFecAddressLength": mplsFecAddressLength,
       "mplsFecAddressFamily": mplsFecAddressFamily,
       "mplsFecAddress": mplsFecAddress,
       "mplsFecStorageType": mplsFecStorageType,
       "mplsFecRowStatus": mplsFecRowStatus,
       "mplsLdpSessionInLabelMapTable": mplsLdpSessionInLabelMapTable,
       "mplsLdpSessionInLabelMapEntry": mplsLdpSessionInLabelMapEntry,
       "mplsLdpSessionInLabelIfIndex": mplsLdpSessionInLabelIfIndex,
       "mplsLdpSessionInLabel": mplsLdpSessionInLabel,
       "mplsLdpSessionInLabelType": mplsLdpSessionInLabelType,
       "mplsLdpSessionInLabelConnectionType": mplsLdpSessionInLabelConnectionType,
       "mplsLdpSessionOutLabelMapTable": mplsLdpSessionOutLabelMapTable,
       "mplsLdpSessionOutLabelMapEntry": mplsLdpSessionOutLabelMapEntry,
       "mplsLdpSessionOutLabelIfIndex": mplsLdpSessionOutLabelIfIndex,
       "mplsLdpSessionOutLabel": mplsLdpSessionOutLabel,
       "mplsLdpSessionOutLabelType": mplsLdpSessionOutLabelType,
       "mplsLdpSessionOutLabelConnectionType": mplsLdpSessionOutLabelConnectionType,
       "mplsLdpSessionOutSegmentIndex": mplsLdpSessionOutSegmentIndex,
       "mplsLdpSessionXCMapTable": mplsLdpSessionXCMapTable,
       "mplsLdpSessionXCMapEntry": mplsLdpSessionXCMapEntry,
       "mplsLdpSessionXCIndex": mplsLdpSessionXCIndex,
       "mplsLdpSessionPeerAddressTable": mplsLdpSessionPeerAddressTable,
       "mplsLdpSessionPeerAddressEntry": mplsLdpSessionPeerAddressEntry,
       "mplsLdpSessionPeerAddressIndex": mplsLdpSessionPeerAddressIndex,
       "mplsLdpSessionPeerNextHopAddressType": mplsLdpSessionPeerNextHopAddressType,
       "mplsLdpSessionPeerNextHopAddress": mplsLdpSessionPeerNextHopAddress,
       "mplsXCsFecsTable": mplsXCsFecsTable,
       "mplsXCsFecsEntry": mplsXCsFecsEntry,
       "mplsXCFecOperStatus": mplsXCFecOperStatus,
       "mplsXCFecOperStatusLastChange": mplsXCFecOperStatusLastChange,
       "mplsLdpNotifications": mplsLdpNotifications,
       "mplsLdpNotificationPrefix": mplsLdpNotificationPrefix,
       "mplsLdpFailedInitSessionThresholdExceeded": mplsLdpFailedInitSessionThresholdExceeded,
       "mplsLdpPathVectorLimitMismatch": mplsLdpPathVectorLimitMismatch,
       "mplsLdpSessionUp": mplsLdpSessionUp,
       "mplsLdpSessionDown": mplsLdpSessionDown,
       "mplsLdpConformance": mplsLdpConformance,
       "mplsLdpGroups": mplsLdpGroups,
       "mplsLdpGeneralGroup": mplsLdpGeneralGroup,
       "mplsLdpGenericGroup": mplsLdpGenericGroup,
       "mplsLdpAtmGroup": mplsLdpAtmGroup,
       "mplsLdpFrameRelayGroup": mplsLdpFrameRelayGroup,
       "mplsLdpMappingGroup": mplsLdpMappingGroup,
       "mplsLdpNotificationsGroup": mplsLdpNotificationsGroup,
       "mplsLdpCompliances": mplsLdpCompliances,
       "mplsLdpModuleCompliance": mplsLdpModuleCompliance}
)
