# SNMP MIB module (JUNIPER-MPLS-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MPLS-LDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:27 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

(MplsLabel,
 MplsLabelDistributionMethod,
 MplsLdpIdentifier,
 MplsLdpLabelType,
 MplsLspType,
 MplsLsrIdentifier,
 MplsRetentionMode) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLabel",
    "MplsLabelDistributionMethod",
    "MplsLdpIdentifier",
    "MplsLdpLabelType",
    "MplsLspType",
    "MplsLsrIdentifier",
    "MplsRetentionMode")

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
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

jnxMplsLdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36)
)
jnxMplsLdpMIB.setRevisions(
        ("2006-05-16 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMplsLdpObjects_ObjectIdentity = ObjectIdentity
jnxMplsLdpObjects = _JnxMplsLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1)
)
_JnxMplsLdpLsrObjects_ObjectIdentity = ObjectIdentity
jnxMplsLdpLsrObjects = _JnxMplsLdpLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 1)
)
_JnxMplsLdpLsrId_Type = MplsLsrIdentifier
_JnxMplsLdpLsrId_Object = MibScalar
jnxMplsLdpLsrId = _JnxMplsLdpLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 1, 1),
    _JnxMplsLdpLsrId_Type()
)
jnxMplsLdpLsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpLsrId.setStatus("current")


class _JnxMplsLdpLsrLoopDetectionCapable_Type(Integer32):
    """Custom type jnxMplsLdpLsrLoopDetectionCapable based on Integer32"""
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


_JnxMplsLdpLsrLoopDetectionCapable_Type.__name__ = "Integer32"
_JnxMplsLdpLsrLoopDetectionCapable_Object = MibScalar
jnxMplsLdpLsrLoopDetectionCapable = _JnxMplsLdpLsrLoopDetectionCapable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 1, 2),
    _JnxMplsLdpLsrLoopDetectionCapable_Type()
)
jnxMplsLdpLsrLoopDetectionCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpLsrLoopDetectionCapable.setStatus("current")
_JnxMplsLdpEntityObjects_ObjectIdentity = ObjectIdentity
jnxMplsLdpEntityObjects = _JnxMplsLdpEntityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2)
)
_JnxMplsLdpEntityLastChange_Type = TimeStamp
_JnxMplsLdpEntityLastChange_Object = MibScalar
jnxMplsLdpEntityLastChange = _JnxMplsLdpEntityLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 1),
    _JnxMplsLdpEntityLastChange_Type()
)
jnxMplsLdpEntityLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityLastChange.setStatus("current")


class _JnxMplsLdpEntityIndexNext_Type(Unsigned32):
    """Custom type jnxMplsLdpEntityIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxMplsLdpEntityIndexNext_Type.__name__ = "Unsigned32"
_JnxMplsLdpEntityIndexNext_Object = MibScalar
jnxMplsLdpEntityIndexNext = _JnxMplsLdpEntityIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 2),
    _JnxMplsLdpEntityIndexNext_Type()
)
jnxMplsLdpEntityIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityIndexNext.setStatus("current")
_JnxMplsLdpEntityTable_Object = MibTable
jnxMplsLdpEntityTable = _JnxMplsLdpEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxMplsLdpEntityTable.setStatus("current")
_JnxMplsLdpEntityEntry_Object = MibTableRow
jnxMplsLdpEntityEntry = _JnxMplsLdpEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1)
)
jnxMplsLdpEntityEntry.setIndexNames(
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityLdpId"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityIndex"),
)
if mibBuilder.loadTexts:
    jnxMplsLdpEntityEntry.setStatus("current")
_JnxMplsLdpEntityLdpId_Type = MplsLdpIdentifier
_JnxMplsLdpEntityLdpId_Object = MibTableColumn
jnxMplsLdpEntityLdpId = _JnxMplsLdpEntityLdpId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 1),
    _JnxMplsLdpEntityLdpId_Type()
)
jnxMplsLdpEntityLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityLdpId.setStatus("current")


class _JnxMplsLdpEntityIndex_Type(Unsigned32):
    """Custom type jnxMplsLdpEntityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxMplsLdpEntityIndex_Type.__name__ = "Unsigned32"
_JnxMplsLdpEntityIndex_Object = MibTableColumn
jnxMplsLdpEntityIndex = _JnxMplsLdpEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 2),
    _JnxMplsLdpEntityIndex_Type()
)
jnxMplsLdpEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityIndex.setStatus("current")


class _JnxMplsLdpEntityProtocolVersion_Type(Integer32):
    """Custom type jnxMplsLdpEntityProtocolVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxMplsLdpEntityProtocolVersion_Type.__name__ = "Integer32"
_JnxMplsLdpEntityProtocolVersion_Object = MibTableColumn
jnxMplsLdpEntityProtocolVersion = _JnxMplsLdpEntityProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 3),
    _JnxMplsLdpEntityProtocolVersion_Type()
)
jnxMplsLdpEntityProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityProtocolVersion.setStatus("current")


class _JnxMplsLdpEntityAdminStatus_Type(Integer32):
    """Custom type jnxMplsLdpEntityAdminStatus based on Integer32"""
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


_JnxMplsLdpEntityAdminStatus_Type.__name__ = "Integer32"
_JnxMplsLdpEntityAdminStatus_Object = MibTableColumn
jnxMplsLdpEntityAdminStatus = _JnxMplsLdpEntityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 4),
    _JnxMplsLdpEntityAdminStatus_Type()
)
jnxMplsLdpEntityAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityAdminStatus.setStatus("current")


class _JnxMplsLdpEntityOperStatus_Type(Integer32):
    """Custom type jnxMplsLdpEntityOperStatus based on Integer32"""
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


_JnxMplsLdpEntityOperStatus_Type.__name__ = "Integer32"
_JnxMplsLdpEntityOperStatus_Object = MibTableColumn
jnxMplsLdpEntityOperStatus = _JnxMplsLdpEntityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 5),
    _JnxMplsLdpEntityOperStatus_Type()
)
jnxMplsLdpEntityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityOperStatus.setStatus("current")


class _JnxMplsLdpEntityTcpDscPort_Type(InetPortNumber):
    """Custom type jnxMplsLdpEntityTcpDscPort based on InetPortNumber"""
    defaultValue = 646


_JnxMplsLdpEntityTcpDscPort_Object = MibTableColumn
jnxMplsLdpEntityTcpDscPort = _JnxMplsLdpEntityTcpDscPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 6),
    _JnxMplsLdpEntityTcpDscPort_Type()
)
jnxMplsLdpEntityTcpDscPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityTcpDscPort.setStatus("current")


class _JnxMplsLdpEntityUdpDscPort_Type(InetPortNumber):
    """Custom type jnxMplsLdpEntityUdpDscPort based on InetPortNumber"""
    defaultValue = 646


_JnxMplsLdpEntityUdpDscPort_Object = MibTableColumn
jnxMplsLdpEntityUdpDscPort = _JnxMplsLdpEntityUdpDscPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 7),
    _JnxMplsLdpEntityUdpDscPort_Type()
)
jnxMplsLdpEntityUdpDscPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityUdpDscPort.setStatus("current")


class _JnxMplsLdpEntityMaxPduLength_Type(Unsigned32):
    """Custom type jnxMplsLdpEntityMaxPduLength based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65535),
    )


_JnxMplsLdpEntityMaxPduLength_Type.__name__ = "Unsigned32"
_JnxMplsLdpEntityMaxPduLength_Object = MibTableColumn
jnxMplsLdpEntityMaxPduLength = _JnxMplsLdpEntityMaxPduLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 8),
    _JnxMplsLdpEntityMaxPduLength_Type()
)
jnxMplsLdpEntityMaxPduLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityMaxPduLength.setStatus("current")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityMaxPduLength.setUnits("octets")


class _JnxMplsLdpEntityKeepAliveHoldTimer_Type(Integer32):
    """Custom type jnxMplsLdpEntityKeepAliveHoldTimer based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxMplsLdpEntityKeepAliveHoldTimer_Type.__name__ = "Integer32"
_JnxMplsLdpEntityKeepAliveHoldTimer_Object = MibTableColumn
jnxMplsLdpEntityKeepAliveHoldTimer = _JnxMplsLdpEntityKeepAliveHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 9),
    _JnxMplsLdpEntityKeepAliveHoldTimer_Type()
)
jnxMplsLdpEntityKeepAliveHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityKeepAliveHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityKeepAliveHoldTimer.setUnits("seconds")


class _JnxMplsLdpEntityHelloHoldTimer_Type(Integer32):
    """Custom type jnxMplsLdpEntityHelloHoldTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxMplsLdpEntityHelloHoldTimer_Type.__name__ = "Integer32"
_JnxMplsLdpEntityHelloHoldTimer_Object = MibTableColumn
jnxMplsLdpEntityHelloHoldTimer = _JnxMplsLdpEntityHelloHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 10),
    _JnxMplsLdpEntityHelloHoldTimer_Type()
)
jnxMplsLdpEntityHelloHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityHelloHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityHelloHoldTimer.setUnits("seconds")


class _JnxMplsLdpEntityInitSesThreshold_Type(Integer32):
    """Custom type jnxMplsLdpEntityInitSesThreshold based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxMplsLdpEntityInitSesThreshold_Type.__name__ = "Integer32"
_JnxMplsLdpEntityInitSesThreshold_Object = MibTableColumn
jnxMplsLdpEntityInitSesThreshold = _JnxMplsLdpEntityInitSesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 11),
    _JnxMplsLdpEntityInitSesThreshold_Type()
)
jnxMplsLdpEntityInitSesThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityInitSesThreshold.setStatus("current")
_JnxMplsLdpEntityLabelDistMethod_Type = MplsLabelDistributionMethod
_JnxMplsLdpEntityLabelDistMethod_Object = MibTableColumn
jnxMplsLdpEntityLabelDistMethod = _JnxMplsLdpEntityLabelDistMethod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 12),
    _JnxMplsLdpEntityLabelDistMethod_Type()
)
jnxMplsLdpEntityLabelDistMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityLabelDistMethod.setStatus("current")
_JnxMplsLdpEntityLabelRetentionMode_Type = MplsRetentionMode
_JnxMplsLdpEntityLabelRetentionMode_Object = MibTableColumn
jnxMplsLdpEntityLabelRetentionMode = _JnxMplsLdpEntityLabelRetentionMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 13),
    _JnxMplsLdpEntityLabelRetentionMode_Type()
)
jnxMplsLdpEntityLabelRetentionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityLabelRetentionMode.setStatus("current")


class _JnxMplsLdpEntityPathVectorLimit_Type(Integer32):
    """Custom type jnxMplsLdpEntityPathVectorLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxMplsLdpEntityPathVectorLimit_Type.__name__ = "Integer32"
_JnxMplsLdpEntityPathVectorLimit_Object = MibTableColumn
jnxMplsLdpEntityPathVectorLimit = _JnxMplsLdpEntityPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 14),
    _JnxMplsLdpEntityPathVectorLimit_Type()
)
jnxMplsLdpEntityPathVectorLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityPathVectorLimit.setStatus("current")


class _JnxMplsLdpEntityHopCountLimit_Type(Integer32):
    """Custom type jnxMplsLdpEntityHopCountLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxMplsLdpEntityHopCountLimit_Type.__name__ = "Integer32"
_JnxMplsLdpEntityHopCountLimit_Object = MibTableColumn
jnxMplsLdpEntityHopCountLimit = _JnxMplsLdpEntityHopCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 15),
    _JnxMplsLdpEntityHopCountLimit_Type()
)
jnxMplsLdpEntityHopCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityHopCountLimit.setStatus("current")


class _JnxMplsLdpEntityTargetPeer_Type(TruthValue):
    """Custom type jnxMplsLdpEntityTargetPeer based on TruthValue"""


_JnxMplsLdpEntityTargetPeer_Object = MibTableColumn
jnxMplsLdpEntityTargetPeer = _JnxMplsLdpEntityTargetPeer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 16),
    _JnxMplsLdpEntityTargetPeer_Type()
)
jnxMplsLdpEntityTargetPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityTargetPeer.setStatus("current")
_JnxMplsLdpEntityTargetPeerAddrType_Type = InetAddressType
_JnxMplsLdpEntityTargetPeerAddrType_Object = MibTableColumn
jnxMplsLdpEntityTargetPeerAddrType = _JnxMplsLdpEntityTargetPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 17),
    _JnxMplsLdpEntityTargetPeerAddrType_Type()
)
jnxMplsLdpEntityTargetPeerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityTargetPeerAddrType.setStatus("current")
_JnxMplsLdpEntityTargetPeerAddr_Type = InetAddress
_JnxMplsLdpEntityTargetPeerAddr_Object = MibTableColumn
jnxMplsLdpEntityTargetPeerAddr = _JnxMplsLdpEntityTargetPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 18),
    _JnxMplsLdpEntityTargetPeerAddr_Type()
)
jnxMplsLdpEntityTargetPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityTargetPeerAddr.setStatus("current")
_JnxMplsLdpEntityLabelType_Type = MplsLdpLabelType
_JnxMplsLdpEntityLabelType_Object = MibTableColumn
jnxMplsLdpEntityLabelType = _JnxMplsLdpEntityLabelType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 19),
    _JnxMplsLdpEntityLabelType_Type()
)
jnxMplsLdpEntityLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityLabelType.setStatus("current")
_JnxMplsLdpEntityDiscontinuityTime_Type = TimeStamp
_JnxMplsLdpEntityDiscontinuityTime_Object = MibTableColumn
jnxMplsLdpEntityDiscontinuityTime = _JnxMplsLdpEntityDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 20),
    _JnxMplsLdpEntityDiscontinuityTime_Type()
)
jnxMplsLdpEntityDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityDiscontinuityTime.setStatus("current")
_JnxMplsLdpEntityStorageType_Type = StorageType
_JnxMplsLdpEntityStorageType_Object = MibTableColumn
jnxMplsLdpEntityStorageType = _JnxMplsLdpEntityStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 21),
    _JnxMplsLdpEntityStorageType_Type()
)
jnxMplsLdpEntityStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityStorageType.setStatus("current")
_JnxMplsLdpEntityRowStatus_Type = RowStatus
_JnxMplsLdpEntityRowStatus_Object = MibTableColumn
jnxMplsLdpEntityRowStatus = _JnxMplsLdpEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 3, 1, 22),
    _JnxMplsLdpEntityRowStatus_Type()
)
jnxMplsLdpEntityRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpEntityRowStatus.setStatus("current")
_JnxMplsLdpEntityStatsTable_Object = MibTable
jnxMplsLdpEntityStatsTable = _JnxMplsLdpEntityStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4)
)
if mibBuilder.loadTexts:
    jnxMplsLdpEntityStatsTable.setStatus("current")
_JnxMplsLdpEntityStatsEntry_Object = MibTableRow
jnxMplsLdpEntityStatsEntry = _JnxMplsLdpEntityStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    jnxMplsLdpEntityStatsEntry.setStatus("current")
_JnxMplsLdpAttemptedSessions_Type = Counter32
_JnxMplsLdpAttemptedSessions_Object = MibTableColumn
jnxMplsLdpAttemptedSessions = _JnxMplsLdpAttemptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4, 1, 1),
    _JnxMplsLdpAttemptedSessions_Type()
)
jnxMplsLdpAttemptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpAttemptedSessions.setStatus("current")
_JnxMplsLdpSesRejectedNoHelloErrors_Type = Counter32
_JnxMplsLdpSesRejectedNoHelloErrors_Object = MibTableColumn
jnxMplsLdpSesRejectedNoHelloErrors = _JnxMplsLdpSesRejectedNoHelloErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4, 1, 2),
    _JnxMplsLdpSesRejectedNoHelloErrors_Type()
)
jnxMplsLdpSesRejectedNoHelloErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpSesRejectedNoHelloErrors.setStatus("current")
_JnxMplsLdpSesRejectedAdErrors_Type = Counter32
_JnxMplsLdpSesRejectedAdErrors_Object = MibTableColumn
jnxMplsLdpSesRejectedAdErrors = _JnxMplsLdpSesRejectedAdErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4, 1, 3),
    _JnxMplsLdpSesRejectedAdErrors_Type()
)
jnxMplsLdpSesRejectedAdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpSesRejectedAdErrors.setStatus("current")
_JnxMplsLdpSesRejectedMaxPduErrors_Type = Counter32
_JnxMplsLdpSesRejectedMaxPduErrors_Object = MibTableColumn
jnxMplsLdpSesRejectedMaxPduErrors = _JnxMplsLdpSesRejectedMaxPduErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4, 1, 4),
    _JnxMplsLdpSesRejectedMaxPduErrors_Type()
)
jnxMplsLdpSesRejectedMaxPduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpSesRejectedMaxPduErrors.setStatus("current")
_JnxMplsLdpSesRejectedLRErrors_Type = Counter32
_JnxMplsLdpSesRejectedLRErrors_Object = MibTableColumn
jnxMplsLdpSesRejectedLRErrors = _JnxMplsLdpSesRejectedLRErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4, 1, 5),
    _JnxMplsLdpSesRejectedLRErrors_Type()
)
jnxMplsLdpSesRejectedLRErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpSesRejectedLRErrors.setStatus("current")
_JnxMplsLdpBadLdpIdentifierErrors_Type = Counter32
_JnxMplsLdpBadLdpIdentifierErrors_Object = MibTableColumn
jnxMplsLdpBadLdpIdentifierErrors = _JnxMplsLdpBadLdpIdentifierErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4, 1, 6),
    _JnxMplsLdpBadLdpIdentifierErrors_Type()
)
jnxMplsLdpBadLdpIdentifierErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpBadLdpIdentifierErrors.setStatus("current")
_JnxMplsLdpBadPduLengthErrors_Type = Counter32
_JnxMplsLdpBadPduLengthErrors_Object = MibTableColumn
jnxMplsLdpBadPduLengthErrors = _JnxMplsLdpBadPduLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4, 1, 7),
    _JnxMplsLdpBadPduLengthErrors_Type()
)
jnxMplsLdpBadPduLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpBadPduLengthErrors.setStatus("current")
_JnxMplsLdpBadMessageLengthErrors_Type = Counter32
_JnxMplsLdpBadMessageLengthErrors_Object = MibTableColumn
jnxMplsLdpBadMessageLengthErrors = _JnxMplsLdpBadMessageLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4, 1, 8),
    _JnxMplsLdpBadMessageLengthErrors_Type()
)
jnxMplsLdpBadMessageLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpBadMessageLengthErrors.setStatus("current")
_JnxMplsLdpBadTlvLengthErrors_Type = Counter32
_JnxMplsLdpBadTlvLengthErrors_Object = MibTableColumn
jnxMplsLdpBadTlvLengthErrors = _JnxMplsLdpBadTlvLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4, 1, 9),
    _JnxMplsLdpBadTlvLengthErrors_Type()
)
jnxMplsLdpBadTlvLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpBadTlvLengthErrors.setStatus("current")
_JnxMplsLdpMalformedTlvValueErrors_Type = Counter32
_JnxMplsLdpMalformedTlvValueErrors_Object = MibTableColumn
jnxMplsLdpMalformedTlvValueErrors = _JnxMplsLdpMalformedTlvValueErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4, 1, 10),
    _JnxMplsLdpMalformedTlvValueErrors_Type()
)
jnxMplsLdpMalformedTlvValueErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpMalformedTlvValueErrors.setStatus("current")
_JnxMplsLdpKeepAliveTimerExpErrors_Type = Counter32
_JnxMplsLdpKeepAliveTimerExpErrors_Object = MibTableColumn
jnxMplsLdpKeepAliveTimerExpErrors = _JnxMplsLdpKeepAliveTimerExpErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4, 1, 11),
    _JnxMplsLdpKeepAliveTimerExpErrors_Type()
)
jnxMplsLdpKeepAliveTimerExpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpKeepAliveTimerExpErrors.setStatus("current")
_JnxMplsLdpShutdownNotifReceived_Type = Counter32
_JnxMplsLdpShutdownNotifReceived_Object = MibTableColumn
jnxMplsLdpShutdownNotifReceived = _JnxMplsLdpShutdownNotifReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4, 1, 12),
    _JnxMplsLdpShutdownNotifReceived_Type()
)
jnxMplsLdpShutdownNotifReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpShutdownNotifReceived.setStatus("current")
_JnxMplsLdpShutdownNotifSent_Type = Counter32
_JnxMplsLdpShutdownNotifSent_Object = MibTableColumn
jnxMplsLdpShutdownNotifSent = _JnxMplsLdpShutdownNotifSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 2, 4, 1, 13),
    _JnxMplsLdpShutdownNotifSent_Type()
)
jnxMplsLdpShutdownNotifSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpShutdownNotifSent.setStatus("current")
_JnxMplsLdpSessionObjects_ObjectIdentity = ObjectIdentity
jnxMplsLdpSessionObjects = _JnxMplsLdpSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3)
)
_JnxMplsLdpPeerLastChange_Type = TimeStamp
_JnxMplsLdpPeerLastChange_Object = MibScalar
jnxMplsLdpPeerLastChange = _JnxMplsLdpPeerLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 1),
    _JnxMplsLdpPeerLastChange_Type()
)
jnxMplsLdpPeerLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpPeerLastChange.setStatus("current")
_JnxMplsLdpPeerTable_Object = MibTable
jnxMplsLdpPeerTable = _JnxMplsLdpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 2)
)
if mibBuilder.loadTexts:
    jnxMplsLdpPeerTable.setStatus("current")
_JnxMplsLdpPeerEntry_Object = MibTableRow
jnxMplsLdpPeerEntry = _JnxMplsLdpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 2, 1)
)
jnxMplsLdpPeerEntry.setIndexNames(
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityLdpId"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityIndex"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    jnxMplsLdpPeerEntry.setStatus("current")
_JnxMplsLdpPeerLdpId_Type = MplsLdpIdentifier
_JnxMplsLdpPeerLdpId_Object = MibTableColumn
jnxMplsLdpPeerLdpId = _JnxMplsLdpPeerLdpId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 2, 1, 1),
    _JnxMplsLdpPeerLdpId_Type()
)
jnxMplsLdpPeerLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsLdpPeerLdpId.setStatus("current")
_JnxMplsLdpPeerLabelDistMethod_Type = MplsLabelDistributionMethod
_JnxMplsLdpPeerLabelDistMethod_Object = MibTableColumn
jnxMplsLdpPeerLabelDistMethod = _JnxMplsLdpPeerLabelDistMethod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 2, 1, 2),
    _JnxMplsLdpPeerLabelDistMethod_Type()
)
jnxMplsLdpPeerLabelDistMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpPeerLabelDistMethod.setStatus("current")


class _JnxMplsLdpPeerPathVectorLimit_Type(Integer32):
    """Custom type jnxMplsLdpPeerPathVectorLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxMplsLdpPeerPathVectorLimit_Type.__name__ = "Integer32"
_JnxMplsLdpPeerPathVectorLimit_Object = MibTableColumn
jnxMplsLdpPeerPathVectorLimit = _JnxMplsLdpPeerPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 2, 1, 3),
    _JnxMplsLdpPeerPathVectorLimit_Type()
)
jnxMplsLdpPeerPathVectorLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpPeerPathVectorLimit.setStatus("current")
_JnxMplsLdpSessionTable_Object = MibTable
jnxMplsLdpSessionTable = _JnxMplsLdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 3)
)
if mibBuilder.loadTexts:
    jnxMplsLdpSessionTable.setStatus("current")
_JnxMplsLdpSessionEntry_Object = MibTableRow
jnxMplsLdpSessionEntry = _JnxMplsLdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    jnxMplsLdpSessionEntry.setStatus("current")
_JnxMplsLdpSesStateLastChange_Type = TimeStamp
_JnxMplsLdpSesStateLastChange_Object = MibTableColumn
jnxMplsLdpSesStateLastChange = _JnxMplsLdpSesStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 3, 1, 1),
    _JnxMplsLdpSesStateLastChange_Type()
)
jnxMplsLdpSesStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpSesStateLastChange.setStatus("current")


class _JnxMplsLdpSesState_Type(Integer32):
    """Custom type jnxMplsLdpSesState based on Integer32"""
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


_JnxMplsLdpSesState_Type.__name__ = "Integer32"
_JnxMplsLdpSesState_Object = MibTableColumn
jnxMplsLdpSesState = _JnxMplsLdpSesState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 3, 1, 2),
    _JnxMplsLdpSesState_Type()
)
jnxMplsLdpSesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpSesState.setStatus("current")


class _JnxMplsLdpSesProtocolVersion_Type(Integer32):
    """Custom type jnxMplsLdpSesProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxMplsLdpSesProtocolVersion_Type.__name__ = "Integer32"
_JnxMplsLdpSesProtocolVersion_Object = MibTableColumn
jnxMplsLdpSesProtocolVersion = _JnxMplsLdpSesProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 3, 1, 3),
    _JnxMplsLdpSesProtocolVersion_Type()
)
jnxMplsLdpSesProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpSesProtocolVersion.setStatus("current")
_JnxMplsLdpSesKeepAliveHoldTimeRem_Type = TimeInterval
_JnxMplsLdpSesKeepAliveHoldTimeRem_Object = MibTableColumn
jnxMplsLdpSesKeepAliveHoldTimeRem = _JnxMplsLdpSesKeepAliveHoldTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 3, 1, 4),
    _JnxMplsLdpSesKeepAliveHoldTimeRem_Type()
)
jnxMplsLdpSesKeepAliveHoldTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpSesKeepAliveHoldTimeRem.setStatus("current")


class _JnxMplsLdpSesMaxPduLength_Type(Unsigned32):
    """Custom type jnxMplsLdpSesMaxPduLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxMplsLdpSesMaxPduLength_Type.__name__ = "Unsigned32"
_JnxMplsLdpSesMaxPduLength_Object = MibTableColumn
jnxMplsLdpSesMaxPduLength = _JnxMplsLdpSesMaxPduLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 3, 1, 5),
    _JnxMplsLdpSesMaxPduLength_Type()
)
jnxMplsLdpSesMaxPduLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpSesMaxPduLength.setStatus("current")
if mibBuilder.loadTexts:
    jnxMplsLdpSesMaxPduLength.setUnits("octets")
_JnxMplsLdpSesDiscontinuityTime_Type = TimeStamp
_JnxMplsLdpSesDiscontinuityTime_Object = MibTableColumn
jnxMplsLdpSesDiscontinuityTime = _JnxMplsLdpSesDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 3, 1, 6),
    _JnxMplsLdpSesDiscontinuityTime_Type()
)
jnxMplsLdpSesDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpSesDiscontinuityTime.setStatus("current")
_JnxMplsLdpSesStatsTable_Object = MibTable
jnxMplsLdpSesStatsTable = _JnxMplsLdpSesStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 4)
)
if mibBuilder.loadTexts:
    jnxMplsLdpSesStatsTable.setStatus("current")
_JnxMplsLdpSesStatsEntry_Object = MibTableRow
jnxMplsLdpSesStatsEntry = _JnxMplsLdpSesStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    jnxMplsLdpSesStatsEntry.setStatus("current")
_JnxMplsLdpSesStatsUnkMesTypeErrors_Type = Counter32
_JnxMplsLdpSesStatsUnkMesTypeErrors_Object = MibTableColumn
jnxMplsLdpSesStatsUnkMesTypeErrors = _JnxMplsLdpSesStatsUnkMesTypeErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 4, 1, 1),
    _JnxMplsLdpSesStatsUnkMesTypeErrors_Type()
)
jnxMplsLdpSesStatsUnkMesTypeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpSesStatsUnkMesTypeErrors.setStatus("current")
_JnxMplsLdpSesStatsUnkTlvErrors_Type = Counter32
_JnxMplsLdpSesStatsUnkTlvErrors_Object = MibTableColumn
jnxMplsLdpSesStatsUnkTlvErrors = _JnxMplsLdpSesStatsUnkTlvErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 4, 1, 2),
    _JnxMplsLdpSesStatsUnkTlvErrors_Type()
)
jnxMplsLdpSesStatsUnkTlvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpSesStatsUnkTlvErrors.setStatus("current")
_JnxMplsLdpHelloAdjacencyObjects_ObjectIdentity = ObjectIdentity
jnxMplsLdpHelloAdjacencyObjects = _JnxMplsLdpHelloAdjacencyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 5)
)
_JnxMplsLdpHelloAdjacencyTable_Object = MibTable
jnxMplsLdpHelloAdjacencyTable = _JnxMplsLdpHelloAdjacencyTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    jnxMplsLdpHelloAdjacencyTable.setStatus("current")
_JnxMplsLdpHelloAdjacencyEntry_Object = MibTableRow
jnxMplsLdpHelloAdjacencyEntry = _JnxMplsLdpHelloAdjacencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 5, 1, 1)
)
jnxMplsLdpHelloAdjacencyEntry.setIndexNames(
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityLdpId"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityIndex"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpPeerLdpId"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpHelloAdjIndex"),
)
if mibBuilder.loadTexts:
    jnxMplsLdpHelloAdjacencyEntry.setStatus("current")


class _JnxMplsLdpHelloAdjIndex_Type(Unsigned32):
    """Custom type jnxMplsLdpHelloAdjIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxMplsLdpHelloAdjIndex_Type.__name__ = "Unsigned32"
_JnxMplsLdpHelloAdjIndex_Object = MibTableColumn
jnxMplsLdpHelloAdjIndex = _JnxMplsLdpHelloAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 5, 1, 1, 1),
    _JnxMplsLdpHelloAdjIndex_Type()
)
jnxMplsLdpHelloAdjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsLdpHelloAdjIndex.setStatus("current")
_JnxMplsLdpHelloAdjHoldTimeRem_Type = TimeInterval
_JnxMplsLdpHelloAdjHoldTimeRem_Object = MibTableColumn
jnxMplsLdpHelloAdjHoldTimeRem = _JnxMplsLdpHelloAdjHoldTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 5, 1, 1, 2),
    _JnxMplsLdpHelloAdjHoldTimeRem_Type()
)
jnxMplsLdpHelloAdjHoldTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpHelloAdjHoldTimeRem.setStatus("current")


class _JnxMplsLdpHelloAdjType_Type(Integer32):
    """Custom type jnxMplsLdpHelloAdjType based on Integer32"""
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


_JnxMplsLdpHelloAdjType_Type.__name__ = "Integer32"
_JnxMplsLdpHelloAdjType_Object = MibTableColumn
jnxMplsLdpHelloAdjType = _JnxMplsLdpHelloAdjType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 5, 1, 1, 3),
    _JnxMplsLdpHelloAdjType_Type()
)
jnxMplsLdpHelloAdjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpHelloAdjType.setStatus("current")
_JnxMplsLdpLspTable_Object = MibTable
jnxMplsLdpLspTable = _JnxMplsLdpLspTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 6)
)
if mibBuilder.loadTexts:
    jnxMplsLdpLspTable.setStatus("current")
_JnxMplsLdpLspEntry_Object = MibTableRow
jnxMplsLdpLspEntry = _JnxMplsLdpLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 6, 1)
)
jnxMplsLdpLspEntry.setIndexNames(
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityLdpId"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityIndex"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpPeerLdpId"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpLspIfIndex"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpLspLabel"),
)
if mibBuilder.loadTexts:
    jnxMplsLdpLspEntry.setStatus("current")
_JnxMplsLdpLspIfIndex_Type = InterfaceIndex
_JnxMplsLdpLspIfIndex_Object = MibTableColumn
jnxMplsLdpLspIfIndex = _JnxMplsLdpLspIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 6, 1, 1),
    _JnxMplsLdpLspIfIndex_Type()
)
jnxMplsLdpLspIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsLdpLspIfIndex.setStatus("current")
_JnxMplsLdpLspLabel_Type = MplsLabel
_JnxMplsLdpLspLabel_Object = MibTableColumn
jnxMplsLdpLspLabel = _JnxMplsLdpLspLabel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 6, 1, 2),
    _JnxMplsLdpLspLabel_Type()
)
jnxMplsLdpLspLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsLdpLspLabel.setStatus("current")
_JnxMplsLdpLspLabelType_Type = MplsLdpLabelType
_JnxMplsLdpLspLabelType_Object = MibTableColumn
jnxMplsLdpLspLabelType = _JnxMplsLdpLspLabelType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 6, 1, 3),
    _JnxMplsLdpLspLabelType_Type()
)
jnxMplsLdpLspLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpLspLabelType.setStatus("current")
_JnxMplsLdpLspType_Type = MplsLspType
_JnxMplsLdpLspType_Object = MibTableColumn
jnxMplsLdpLspType = _JnxMplsLdpLspType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 6, 1, 4),
    _JnxMplsLdpLspType_Type()
)
jnxMplsLdpLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpLspType.setStatus("current")
_JnxMplsLdpLspLsrInSegmentPointer_Type = RowPointer
_JnxMplsLdpLspLsrInSegmentPointer_Object = MibTableColumn
jnxMplsLdpLspLsrInSegmentPointer = _JnxMplsLdpLspLsrInSegmentPointer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 6, 1, 5),
    _JnxMplsLdpLspLsrInSegmentPointer_Type()
)
jnxMplsLdpLspLsrInSegmentPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpLspLsrInSegmentPointer.setStatus("current")
_JnxMplsLdpLspLsrOutSegmentPointer_Type = RowPointer
_JnxMplsLdpLspLsrOutSegmentPointer_Object = MibTableColumn
jnxMplsLdpLspLsrOutSegmentPointer = _JnxMplsLdpLspLsrOutSegmentPointer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 6, 1, 6),
    _JnxMplsLdpLspLsrOutSegmentPointer_Type()
)
jnxMplsLdpLspLsrOutSegmentPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpLspLsrOutSegmentPointer.setStatus("current")
_JnxMplsLdpLspLsrXCPointer_Type = RowPointer
_JnxMplsLdpLspLsrXCPointer_Object = MibTableColumn
jnxMplsLdpLspLsrXCPointer = _JnxMplsLdpLspLsrXCPointer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 6, 1, 7),
    _JnxMplsLdpLspLsrXCPointer_Type()
)
jnxMplsLdpLspLsrXCPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpLspLsrXCPointer.setStatus("current")
_JnxMplsFecObjects_ObjectIdentity = ObjectIdentity
jnxMplsFecObjects = _JnxMplsFecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 7)
)


class _JnxMplsFecIndexNext_Type(Unsigned32):
    """Custom type jnxMplsFecIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxMplsFecIndexNext_Type.__name__ = "Unsigned32"
_JnxMplsFecIndexNext_Object = MibScalar
jnxMplsFecIndexNext = _JnxMplsFecIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 7, 1),
    _JnxMplsFecIndexNext_Type()
)
jnxMplsFecIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsFecIndexNext.setStatus("current")
_JnxMplsFecTable_Object = MibTable
jnxMplsFecTable = _JnxMplsFecTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 7, 2)
)
if mibBuilder.loadTexts:
    jnxMplsFecTable.setStatus("current")
_JnxMplsFecEntry_Object = MibTableRow
jnxMplsFecEntry = _JnxMplsFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 7, 2, 1)
)
jnxMplsFecEntry.setIndexNames(
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsFecIndex"),
)
if mibBuilder.loadTexts:
    jnxMplsFecEntry.setStatus("current")


class _JnxMplsFecIndex_Type(Unsigned32):
    """Custom type jnxMplsFecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxMplsFecIndex_Type.__name__ = "Unsigned32"
_JnxMplsFecIndex_Object = MibTableColumn
jnxMplsFecIndex = _JnxMplsFecIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 7, 2, 1, 1),
    _JnxMplsFecIndex_Type()
)
jnxMplsFecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsFecIndex.setStatus("current")


class _JnxMplsFecType_Type(Integer32):
    """Custom type jnxMplsFecType based on Integer32"""
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


_JnxMplsFecType_Type.__name__ = "Integer32"
_JnxMplsFecType_Object = MibTableColumn
jnxMplsFecType = _JnxMplsFecType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 7, 2, 1, 2),
    _JnxMplsFecType_Type()
)
jnxMplsFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsFecType.setStatus("current")


class _JnxMplsFecAddrLength_Type(Integer32):
    """Custom type jnxMplsFecAddrLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxMplsFecAddrLength_Type.__name__ = "Integer32"
_JnxMplsFecAddrLength_Object = MibTableColumn
jnxMplsFecAddrLength = _JnxMplsFecAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 7, 2, 1, 3),
    _JnxMplsFecAddrLength_Type()
)
jnxMplsFecAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsFecAddrLength.setStatus("current")
_JnxMplsFecAddrFamily_Type = InetAddressType
_JnxMplsFecAddrFamily_Object = MibTableColumn
jnxMplsFecAddrFamily = _JnxMplsFecAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 7, 2, 1, 4),
    _JnxMplsFecAddrFamily_Type()
)
jnxMplsFecAddrFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsFecAddrFamily.setStatus("current")
_JnxMplsFecAddr_Type = InetAddress
_JnxMplsFecAddr_Object = MibTableColumn
jnxMplsFecAddr = _JnxMplsFecAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 7, 2, 1, 5),
    _JnxMplsFecAddr_Type()
)
jnxMplsFecAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsFecAddr.setStatus("current")
_JnxMplsFecStorageType_Type = StorageType
_JnxMplsFecStorageType_Object = MibTableColumn
jnxMplsFecStorageType = _JnxMplsFecStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 7, 2, 1, 6),
    _JnxMplsFecStorageType_Type()
)
jnxMplsFecStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsFecStorageType.setStatus("current")
_JnxMplsFecRowStatus_Type = RowStatus
_JnxMplsFecRowStatus_Object = MibTableColumn
jnxMplsFecRowStatus = _JnxMplsFecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 7, 2, 1, 7),
    _JnxMplsFecRowStatus_Type()
)
jnxMplsFecRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsFecRowStatus.setStatus("current")
_JnxMplsLdpLspFecTable_Object = MibTable
jnxMplsLdpLspFecTable = _JnxMplsLdpLspFecTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 8)
)
if mibBuilder.loadTexts:
    jnxMplsLdpLspFecTable.setStatus("current")
_JnxMplsLdpLspFecEntry_Object = MibTableRow
jnxMplsLdpLspFecEntry = _JnxMplsLdpLspFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 8, 1)
)
jnxMplsLdpLspFecEntry.setIndexNames(
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityLdpId"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityIndex"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpPeerLdpId"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpLspIfIndex"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpLspLabel"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsFecIndex"),
)
if mibBuilder.loadTexts:
    jnxMplsLdpLspFecEntry.setStatus("current")


class _JnxMplsLdpLspFecOperStatus_Type(Integer32):
    """Custom type jnxMplsLdpLspFecOperStatus based on Integer32"""
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


_JnxMplsLdpLspFecOperStatus_Type.__name__ = "Integer32"
_JnxMplsLdpLspFecOperStatus_Object = MibTableColumn
jnxMplsLdpLspFecOperStatus = _JnxMplsLdpLspFecOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 8, 1, 1),
    _JnxMplsLdpLspFecOperStatus_Type()
)
jnxMplsLdpLspFecOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpLspFecOperStatus.setStatus("current")
_JnxMplsLdpLspFecLastChange_Type = TimeStamp
_JnxMplsLdpLspFecLastChange_Object = MibTableColumn
jnxMplsLdpLspFecLastChange = _JnxMplsLdpLspFecLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 8, 1, 2),
    _JnxMplsLdpLspFecLastChange_Type()
)
jnxMplsLdpLspFecLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpLspFecLastChange.setStatus("current")
_JnxMplsLdpLspFecRowStatus_Type = RowStatus
_JnxMplsLdpLspFecRowStatus_Object = MibTableColumn
jnxMplsLdpLspFecRowStatus = _JnxMplsLdpLspFecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 8, 1, 3),
    _JnxMplsLdpLspFecRowStatus_Type()
)
jnxMplsLdpLspFecRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpLspFecRowStatus.setStatus("current")
_JnxMplsLdpSesPeerAddrTable_Object = MibTable
jnxMplsLdpSesPeerAddrTable = _JnxMplsLdpSesPeerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 9)
)
if mibBuilder.loadTexts:
    jnxMplsLdpSesPeerAddrTable.setStatus("current")
_JnxMplsLdpSesPeerAddrEntry_Object = MibTableRow
jnxMplsLdpSesPeerAddrEntry = _JnxMplsLdpSesPeerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 9, 1)
)
jnxMplsLdpSesPeerAddrEntry.setIndexNames(
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityLdpId"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityIndex"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpPeerLdpId"),
    (0, "JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesPeerAddrIndex"),
)
if mibBuilder.loadTexts:
    jnxMplsLdpSesPeerAddrEntry.setStatus("current")


class _JnxMplsLdpSesPeerAddrIndex_Type(Unsigned32):
    """Custom type jnxMplsLdpSesPeerAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxMplsLdpSesPeerAddrIndex_Type.__name__ = "Unsigned32"
_JnxMplsLdpSesPeerAddrIndex_Object = MibTableColumn
jnxMplsLdpSesPeerAddrIndex = _JnxMplsLdpSesPeerAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 9, 1, 1),
    _JnxMplsLdpSesPeerAddrIndex_Type()
)
jnxMplsLdpSesPeerAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMplsLdpSesPeerAddrIndex.setStatus("current")
_JnxMplsLdpSesPeerNextHopAddrType_Type = InetAddressType
_JnxMplsLdpSesPeerNextHopAddrType_Object = MibTableColumn
jnxMplsLdpSesPeerNextHopAddrType = _JnxMplsLdpSesPeerNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 9, 1, 2),
    _JnxMplsLdpSesPeerNextHopAddrType_Type()
)
jnxMplsLdpSesPeerNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpSesPeerNextHopAddrType.setStatus("current")
_JnxMplsLdpSesPeerNextHopAddr_Type = InetAddress
_JnxMplsLdpSesPeerNextHopAddr_Object = MibTableColumn
jnxMplsLdpSesPeerNextHopAddr = _JnxMplsLdpSesPeerNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 1, 3, 9, 1, 3),
    _JnxMplsLdpSesPeerNextHopAddr_Type()
)
jnxMplsLdpSesPeerNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMplsLdpSesPeerNextHopAddr.setStatus("current")
_JnxMplsLdpNotifications_ObjectIdentity = ObjectIdentity
jnxMplsLdpNotifications = _JnxMplsLdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 2)
)
_JnxMplsLdpNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxMplsLdpNotificationPrefix = _JnxMplsLdpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 2, 0)
)
_JnxMplsLdpConformance_ObjectIdentity = ObjectIdentity
jnxMplsLdpConformance = _JnxMplsLdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 3)
)
_JnxMplsLdpGroups_ObjectIdentity = ObjectIdentity
jnxMplsLdpGroups = _JnxMplsLdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 3, 1)
)
_JnxMplsLdpCompliances_ObjectIdentity = ObjectIdentity
jnxMplsLdpCompliances = _JnxMplsLdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 3, 2)
)
jnxMplsLdpEntityEntry.registerAugmentions(
    ("JUNIPER-MPLS-LDP-MIB",
     "jnxMplsLdpEntityStatsEntry")
)
jnxMplsLdpEntityStatsEntry.setIndexNames(*jnxMplsLdpEntityEntry.getIndexNames())
jnxMplsLdpPeerEntry.registerAugmentions(
    ("JUNIPER-MPLS-LDP-MIB",
     "jnxMplsLdpSessionEntry")
)
jnxMplsLdpSessionEntry.setIndexNames(*jnxMplsLdpPeerEntry.getIndexNames())
jnxMplsLdpPeerEntry.registerAugmentions(
    ("JUNIPER-MPLS-LDP-MIB",
     "jnxMplsLdpSesStatsEntry")
)
jnxMplsLdpSesStatsEntry.setIndexNames(*jnxMplsLdpPeerEntry.getIndexNames())

# Managed Objects groups

jnxMplsLdpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 3, 1, 1)
)
jnxMplsLdpGeneralGroup.setObjects(
      *(("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpLsrId"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpLsrLoopDetectionCapable"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityLastChange"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityIndexNext"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityProtocolVersion"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityAdminStatus"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityOperStatus"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityTcpDscPort"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityUdpDscPort"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityMaxPduLength"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityKeepAliveHoldTimer"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityHelloHoldTimer"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityInitSesThreshold"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityLabelDistMethod"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityLabelRetentionMode"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityPathVectorLimit"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityHopCountLimit"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityTargetPeer"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityTargetPeerAddrType"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityTargetPeerAddr"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityLabelType"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityDiscontinuityTime"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityStorageType"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityRowStatus"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpAttemptedSessions"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesRejectedNoHelloErrors"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesRejectedAdErrors"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesRejectedMaxPduErrors"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesRejectedLRErrors"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpBadLdpIdentifierErrors"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpBadPduLengthErrors"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpBadMessageLengthErrors"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpBadTlvLengthErrors"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpMalformedTlvValueErrors"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpKeepAliveTimerExpErrors"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpShutdownNotifReceived"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpShutdownNotifSent"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpPeerLastChange"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpPeerLabelDistMethod"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpPeerPathVectorLimit"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpHelloAdjHoldTimeRem"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpHelloAdjType"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesStateLastChange"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesState"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesProtocolVersion"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesKeepAliveHoldTimeRem"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesMaxPduLength"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesDiscontinuityTime"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesStatsUnkMesTypeErrors"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesStatsUnkTlvErrors"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesPeerNextHopAddrType"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesPeerNextHopAddr"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsFecIndexNext"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsFecType"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsFecAddrFamily"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsFecAddrLength"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsFecAddr"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsFecStorageType"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsFecRowStatus"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpLspFecOperStatus"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpLspFecLastChange"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpLspFecRowStatus"))
)
if mibBuilder.loadTexts:
    jnxMplsLdpGeneralGroup.setStatus("current")

jnxMplsLdpLspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 3, 1, 2)
)
jnxMplsLdpLspGroup.setObjects(
      *(("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpLspLabelType"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpLspType"))
)
if mibBuilder.loadTexts:
    jnxMplsLdpLspGroup.setStatus("current")

jnxMplsLdpLsrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 3, 1, 3)
)
jnxMplsLdpLsrGroup.setObjects(
      *(("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpLspLsrInSegmentPointer"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpLspLsrOutSegmentPointer"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpLspLsrXCPointer"))
)
if mibBuilder.loadTexts:
    jnxMplsLdpLsrGroup.setStatus("current")


# Notification objects

jnxMplsLdpInitSesThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 2, 0, 1)
)
jnxMplsLdpInitSesThresholdExceeded.setObjects(
    ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityInitSesThreshold")
)
if mibBuilder.loadTexts:
    jnxMplsLdpInitSesThresholdExceeded.setStatus(
        "current"
    )

jnxMplsLdpPathVectorLimitMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 2, 0, 2)
)
jnxMplsLdpPathVectorLimitMismatch.setObjects(
      *(("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpEntityPathVectorLimit"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpPeerPathVectorLimit"))
)
if mibBuilder.loadTexts:
    jnxMplsLdpPathVectorLimitMismatch.setStatus(
        "current"
    )

jnxMplsLdpSessionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 2, 0, 3)
)
jnxMplsLdpSessionUp.setObjects(
      *(("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesState"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesDiscontinuityTime"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesStatsUnkMesTypeErrors"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesStatsUnkTlvErrors"))
)
if mibBuilder.loadTexts:
    jnxMplsLdpSessionUp.setStatus(
        "current"
    )

jnxMplsLdpSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 2, 0, 4)
)
jnxMplsLdpSessionDown.setObjects(
      *(("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesState"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesDiscontinuityTime"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesStatsUnkMesTypeErrors"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSesStatsUnkTlvErrors"))
)
if mibBuilder.loadTexts:
    jnxMplsLdpSessionDown.setStatus(
        "current"
    )


# Notifications groups

jnxMplsLdpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 3, 1, 4)
)
jnxMplsLdpNotificationsGroup.setObjects(
      *(("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpInitSesThresholdExceeded"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpPathVectorLimitMismatch"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSessionUp"),
        ("JUNIPER-MPLS-LDP-MIB", "jnxMplsLdpSessionDown"))
)
if mibBuilder.loadTexts:
    jnxMplsLdpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

jnxMplsLdpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 3, 2, 1)
)
if mibBuilder.loadTexts:
    jnxMplsLdpModuleFullCompliance.setStatus(
        "current"
    )

jnxMplsLdpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2636, 3, 36, 3, 2, 2)
)
if mibBuilder.loadTexts:
    jnxMplsLdpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MPLS-LDP-MIB",
    **{"jnxMplsLdpMIB": jnxMplsLdpMIB,
       "jnxMplsLdpObjects": jnxMplsLdpObjects,
       "jnxMplsLdpLsrObjects": jnxMplsLdpLsrObjects,
       "jnxMplsLdpLsrId": jnxMplsLdpLsrId,
       "jnxMplsLdpLsrLoopDetectionCapable": jnxMplsLdpLsrLoopDetectionCapable,
       "jnxMplsLdpEntityObjects": jnxMplsLdpEntityObjects,
       "jnxMplsLdpEntityLastChange": jnxMplsLdpEntityLastChange,
       "jnxMplsLdpEntityIndexNext": jnxMplsLdpEntityIndexNext,
       "jnxMplsLdpEntityTable": jnxMplsLdpEntityTable,
       "jnxMplsLdpEntityEntry": jnxMplsLdpEntityEntry,
       "jnxMplsLdpEntityLdpId": jnxMplsLdpEntityLdpId,
       "jnxMplsLdpEntityIndex": jnxMplsLdpEntityIndex,
       "jnxMplsLdpEntityProtocolVersion": jnxMplsLdpEntityProtocolVersion,
       "jnxMplsLdpEntityAdminStatus": jnxMplsLdpEntityAdminStatus,
       "jnxMplsLdpEntityOperStatus": jnxMplsLdpEntityOperStatus,
       "jnxMplsLdpEntityTcpDscPort": jnxMplsLdpEntityTcpDscPort,
       "jnxMplsLdpEntityUdpDscPort": jnxMplsLdpEntityUdpDscPort,
       "jnxMplsLdpEntityMaxPduLength": jnxMplsLdpEntityMaxPduLength,
       "jnxMplsLdpEntityKeepAliveHoldTimer": jnxMplsLdpEntityKeepAliveHoldTimer,
       "jnxMplsLdpEntityHelloHoldTimer": jnxMplsLdpEntityHelloHoldTimer,
       "jnxMplsLdpEntityInitSesThreshold": jnxMplsLdpEntityInitSesThreshold,
       "jnxMplsLdpEntityLabelDistMethod": jnxMplsLdpEntityLabelDistMethod,
       "jnxMplsLdpEntityLabelRetentionMode": jnxMplsLdpEntityLabelRetentionMode,
       "jnxMplsLdpEntityPathVectorLimit": jnxMplsLdpEntityPathVectorLimit,
       "jnxMplsLdpEntityHopCountLimit": jnxMplsLdpEntityHopCountLimit,
       "jnxMplsLdpEntityTargetPeer": jnxMplsLdpEntityTargetPeer,
       "jnxMplsLdpEntityTargetPeerAddrType": jnxMplsLdpEntityTargetPeerAddrType,
       "jnxMplsLdpEntityTargetPeerAddr": jnxMplsLdpEntityTargetPeerAddr,
       "jnxMplsLdpEntityLabelType": jnxMplsLdpEntityLabelType,
       "jnxMplsLdpEntityDiscontinuityTime": jnxMplsLdpEntityDiscontinuityTime,
       "jnxMplsLdpEntityStorageType": jnxMplsLdpEntityStorageType,
       "jnxMplsLdpEntityRowStatus": jnxMplsLdpEntityRowStatus,
       "jnxMplsLdpEntityStatsTable": jnxMplsLdpEntityStatsTable,
       "jnxMplsLdpEntityStatsEntry": jnxMplsLdpEntityStatsEntry,
       "jnxMplsLdpAttemptedSessions": jnxMplsLdpAttemptedSessions,
       "jnxMplsLdpSesRejectedNoHelloErrors": jnxMplsLdpSesRejectedNoHelloErrors,
       "jnxMplsLdpSesRejectedAdErrors": jnxMplsLdpSesRejectedAdErrors,
       "jnxMplsLdpSesRejectedMaxPduErrors": jnxMplsLdpSesRejectedMaxPduErrors,
       "jnxMplsLdpSesRejectedLRErrors": jnxMplsLdpSesRejectedLRErrors,
       "jnxMplsLdpBadLdpIdentifierErrors": jnxMplsLdpBadLdpIdentifierErrors,
       "jnxMplsLdpBadPduLengthErrors": jnxMplsLdpBadPduLengthErrors,
       "jnxMplsLdpBadMessageLengthErrors": jnxMplsLdpBadMessageLengthErrors,
       "jnxMplsLdpBadTlvLengthErrors": jnxMplsLdpBadTlvLengthErrors,
       "jnxMplsLdpMalformedTlvValueErrors": jnxMplsLdpMalformedTlvValueErrors,
       "jnxMplsLdpKeepAliveTimerExpErrors": jnxMplsLdpKeepAliveTimerExpErrors,
       "jnxMplsLdpShutdownNotifReceived": jnxMplsLdpShutdownNotifReceived,
       "jnxMplsLdpShutdownNotifSent": jnxMplsLdpShutdownNotifSent,
       "jnxMplsLdpSessionObjects": jnxMplsLdpSessionObjects,
       "jnxMplsLdpPeerLastChange": jnxMplsLdpPeerLastChange,
       "jnxMplsLdpPeerTable": jnxMplsLdpPeerTable,
       "jnxMplsLdpPeerEntry": jnxMplsLdpPeerEntry,
       "jnxMplsLdpPeerLdpId": jnxMplsLdpPeerLdpId,
       "jnxMplsLdpPeerLabelDistMethod": jnxMplsLdpPeerLabelDistMethod,
       "jnxMplsLdpPeerPathVectorLimit": jnxMplsLdpPeerPathVectorLimit,
       "jnxMplsLdpSessionTable": jnxMplsLdpSessionTable,
       "jnxMplsLdpSessionEntry": jnxMplsLdpSessionEntry,
       "jnxMplsLdpSesStateLastChange": jnxMplsLdpSesStateLastChange,
       "jnxMplsLdpSesState": jnxMplsLdpSesState,
       "jnxMplsLdpSesProtocolVersion": jnxMplsLdpSesProtocolVersion,
       "jnxMplsLdpSesKeepAliveHoldTimeRem": jnxMplsLdpSesKeepAliveHoldTimeRem,
       "jnxMplsLdpSesMaxPduLength": jnxMplsLdpSesMaxPduLength,
       "jnxMplsLdpSesDiscontinuityTime": jnxMplsLdpSesDiscontinuityTime,
       "jnxMplsLdpSesStatsTable": jnxMplsLdpSesStatsTable,
       "jnxMplsLdpSesStatsEntry": jnxMplsLdpSesStatsEntry,
       "jnxMplsLdpSesStatsUnkMesTypeErrors": jnxMplsLdpSesStatsUnkMesTypeErrors,
       "jnxMplsLdpSesStatsUnkTlvErrors": jnxMplsLdpSesStatsUnkTlvErrors,
       "jnxMplsLdpHelloAdjacencyObjects": jnxMplsLdpHelloAdjacencyObjects,
       "jnxMplsLdpHelloAdjacencyTable": jnxMplsLdpHelloAdjacencyTable,
       "jnxMplsLdpHelloAdjacencyEntry": jnxMplsLdpHelloAdjacencyEntry,
       "jnxMplsLdpHelloAdjIndex": jnxMplsLdpHelloAdjIndex,
       "jnxMplsLdpHelloAdjHoldTimeRem": jnxMplsLdpHelloAdjHoldTimeRem,
       "jnxMplsLdpHelloAdjType": jnxMplsLdpHelloAdjType,
       "jnxMplsLdpLspTable": jnxMplsLdpLspTable,
       "jnxMplsLdpLspEntry": jnxMplsLdpLspEntry,
       "jnxMplsLdpLspIfIndex": jnxMplsLdpLspIfIndex,
       "jnxMplsLdpLspLabel": jnxMplsLdpLspLabel,
       "jnxMplsLdpLspLabelType": jnxMplsLdpLspLabelType,
       "jnxMplsLdpLspType": jnxMplsLdpLspType,
       "jnxMplsLdpLspLsrInSegmentPointer": jnxMplsLdpLspLsrInSegmentPointer,
       "jnxMplsLdpLspLsrOutSegmentPointer": jnxMplsLdpLspLsrOutSegmentPointer,
       "jnxMplsLdpLspLsrXCPointer": jnxMplsLdpLspLsrXCPointer,
       "jnxMplsFecObjects": jnxMplsFecObjects,
       "jnxMplsFecIndexNext": jnxMplsFecIndexNext,
       "jnxMplsFecTable": jnxMplsFecTable,
       "jnxMplsFecEntry": jnxMplsFecEntry,
       "jnxMplsFecIndex": jnxMplsFecIndex,
       "jnxMplsFecType": jnxMplsFecType,
       "jnxMplsFecAddrLength": jnxMplsFecAddrLength,
       "jnxMplsFecAddrFamily": jnxMplsFecAddrFamily,
       "jnxMplsFecAddr": jnxMplsFecAddr,
       "jnxMplsFecStorageType": jnxMplsFecStorageType,
       "jnxMplsFecRowStatus": jnxMplsFecRowStatus,
       "jnxMplsLdpLspFecTable": jnxMplsLdpLspFecTable,
       "jnxMplsLdpLspFecEntry": jnxMplsLdpLspFecEntry,
       "jnxMplsLdpLspFecOperStatus": jnxMplsLdpLspFecOperStatus,
       "jnxMplsLdpLspFecLastChange": jnxMplsLdpLspFecLastChange,
       "jnxMplsLdpLspFecRowStatus": jnxMplsLdpLspFecRowStatus,
       "jnxMplsLdpSesPeerAddrTable": jnxMplsLdpSesPeerAddrTable,
       "jnxMplsLdpSesPeerAddrEntry": jnxMplsLdpSesPeerAddrEntry,
       "jnxMplsLdpSesPeerAddrIndex": jnxMplsLdpSesPeerAddrIndex,
       "jnxMplsLdpSesPeerNextHopAddrType": jnxMplsLdpSesPeerNextHopAddrType,
       "jnxMplsLdpSesPeerNextHopAddr": jnxMplsLdpSesPeerNextHopAddr,
       "jnxMplsLdpNotifications": jnxMplsLdpNotifications,
       "jnxMplsLdpNotificationPrefix": jnxMplsLdpNotificationPrefix,
       "jnxMplsLdpInitSesThresholdExceeded": jnxMplsLdpInitSesThresholdExceeded,
       "jnxMplsLdpPathVectorLimitMismatch": jnxMplsLdpPathVectorLimitMismatch,
       "jnxMplsLdpSessionUp": jnxMplsLdpSessionUp,
       "jnxMplsLdpSessionDown": jnxMplsLdpSessionDown,
       "jnxMplsLdpConformance": jnxMplsLdpConformance,
       "jnxMplsLdpGroups": jnxMplsLdpGroups,
       "jnxMplsLdpGeneralGroup": jnxMplsLdpGeneralGroup,
       "jnxMplsLdpLspGroup": jnxMplsLdpLspGroup,
       "jnxMplsLdpLsrGroup": jnxMplsLdpLsrGroup,
       "jnxMplsLdpNotificationsGroup": jnxMplsLdpNotificationsGroup,
       "jnxMplsLdpCompliances": jnxMplsLdpCompliances,
       "jnxMplsLdpModuleFullCompliance": jnxMplsLdpModuleFullCompliance,
       "jnxMplsLdpModuleReadOnlyCompliance": jnxMplsLdpModuleReadOnlyCompliance}
)
