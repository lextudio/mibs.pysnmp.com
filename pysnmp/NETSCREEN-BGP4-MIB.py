# SNMP MIB module (NETSCREEN-BGP4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-BGP4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:42 2024
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

(netscreenVR,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenVR")

(netscreenTrapDesc,
 netscreenTrapType) = mibBuilder.importSymbols(
    "NETSCREEN-TRAP-MIB",
    "netscreenTrapDesc",
    "netscreenTrapType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nsBgp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsBgpInfoTable_Object = MibTable
nsBgpInfoTable = _NsBgpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 1)
)
if mibBuilder.loadTexts:
    nsBgpInfoTable.setStatus("deprecated")
_NsBgpInfoEntry_Object = MibTableRow
nsBgpInfoEntry = _NsBgpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 1, 1)
)
nsBgpInfoEntry.setIndexNames(
    (0, "NETSCREEN-BGP4-MIB", "nsBgpInfoVRID"),
)
if mibBuilder.loadTexts:
    nsBgpInfoEntry.setStatus("deprecated")


class _NsBgpInfoVersion_Type(OctetString):
    """Custom type nsBgpInfoVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NsBgpInfoVersion_Type.__name__ = "OctetString"
_NsBgpInfoVersion_Object = MibTableColumn
nsBgpInfoVersion = _NsBgpInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 1, 1, 1),
    _NsBgpInfoVersion_Type()
)
nsBgpInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpInfoVersion.setStatus("deprecated")


class _NsBgpInfoLocalAs_Type(Integer32):
    """Custom type nsBgpInfoLocalAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsBgpInfoLocalAs_Type.__name__ = "Integer32"
_NsBgpInfoLocalAs_Object = MibTableColumn
nsBgpInfoLocalAs = _NsBgpInfoLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 1, 1, 2),
    _NsBgpInfoLocalAs_Type()
)
nsBgpInfoLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpInfoLocalAs.setStatus("deprecated")
_NsBgpInfoIdentifier_Type = IpAddress
_NsBgpInfoIdentifier_Object = MibTableColumn
nsBgpInfoIdentifier = _NsBgpInfoIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 1, 1, 3),
    _NsBgpInfoIdentifier_Type()
)
nsBgpInfoIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpInfoIdentifier.setStatus("deprecated")


class _NsBgpInfoVRID_Type(Integer32):
    """Custom type nsBgpInfoVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsBgpInfoVRID_Type.__name__ = "Integer32"
_NsBgpInfoVRID_Object = MibTableColumn
nsBgpInfoVRID = _NsBgpInfoVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 1, 1, 4),
    _NsBgpInfoVRID_Type()
)
nsBgpInfoVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpInfoVRID.setStatus("deprecated")
_NsBgpPeerTable_Object = MibTable
nsBgpPeerTable = _NsBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3)
)
if mibBuilder.loadTexts:
    nsBgpPeerTable.setStatus("deprecated")
_NsBgpPeerEntry_Object = MibTableRow
nsBgpPeerEntry = _NsBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1)
)
nsBgpPeerEntry.setIndexNames(
    (0, "NETSCREEN-BGP4-MIB", "nsBgpPeerRemoteAddr"),
    (0, "NETSCREEN-BGP4-MIB", "nsBgpPeerVRID"),
)
if mibBuilder.loadTexts:
    nsBgpPeerEntry.setStatus("deprecated")
_NsBgpPeerIdentifier_Type = IpAddress
_NsBgpPeerIdentifier_Object = MibTableColumn
nsBgpPeerIdentifier = _NsBgpPeerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 1),
    _NsBgpPeerIdentifier_Type()
)
nsBgpPeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerIdentifier.setStatus("deprecated")


class _NsBgpPeerState_Type(Integer32):
    """Custom type nsBgpPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("connect", 2),
          ("established", 6),
          ("idle", 1),
          ("openconfirm", 5),
          ("opensent", 4))
    )


_NsBgpPeerState_Type.__name__ = "Integer32"
_NsBgpPeerState_Object = MibTableColumn
nsBgpPeerState = _NsBgpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 2),
    _NsBgpPeerState_Type()
)
nsBgpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerState.setStatus("deprecated")


class _NsBgpPeerAdminStatus_Type(Integer32):
    """Custom type nsBgpPeerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 2),
          ("stop", 1))
    )


_NsBgpPeerAdminStatus_Type.__name__ = "Integer32"
_NsBgpPeerAdminStatus_Object = MibTableColumn
nsBgpPeerAdminStatus = _NsBgpPeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 3),
    _NsBgpPeerAdminStatus_Type()
)
nsBgpPeerAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerAdminStatus.setStatus("deprecated")
_NsBgpPeerNegotiatedVersion_Type = Integer32
_NsBgpPeerNegotiatedVersion_Object = MibTableColumn
nsBgpPeerNegotiatedVersion = _NsBgpPeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 4),
    _NsBgpPeerNegotiatedVersion_Type()
)
nsBgpPeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerNegotiatedVersion.setStatus("deprecated")
_NsBgpPeerLocalAddr_Type = IpAddress
_NsBgpPeerLocalAddr_Object = MibTableColumn
nsBgpPeerLocalAddr = _NsBgpPeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 5),
    _NsBgpPeerLocalAddr_Type()
)
nsBgpPeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerLocalAddr.setStatus("deprecated")


class _NsBgpPeerLocalPort_Type(Integer32):
    """Custom type nsBgpPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsBgpPeerLocalPort_Type.__name__ = "Integer32"
_NsBgpPeerLocalPort_Object = MibTableColumn
nsBgpPeerLocalPort = _NsBgpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 6),
    _NsBgpPeerLocalPort_Type()
)
nsBgpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerLocalPort.setStatus("deprecated")
_NsBgpPeerRemoteAddr_Type = IpAddress
_NsBgpPeerRemoteAddr_Object = MibTableColumn
nsBgpPeerRemoteAddr = _NsBgpPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 7),
    _NsBgpPeerRemoteAddr_Type()
)
nsBgpPeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerRemoteAddr.setStatus("deprecated")


class _NsBgpPeerRemotePort_Type(Integer32):
    """Custom type nsBgpPeerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsBgpPeerRemotePort_Type.__name__ = "Integer32"
_NsBgpPeerRemotePort_Object = MibTableColumn
nsBgpPeerRemotePort = _NsBgpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 8),
    _NsBgpPeerRemotePort_Type()
)
nsBgpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerRemotePort.setStatus("deprecated")


class _NsBgpPeerRemoteAs_Type(Integer32):
    """Custom type nsBgpPeerRemoteAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsBgpPeerRemoteAs_Type.__name__ = "Integer32"
_NsBgpPeerRemoteAs_Object = MibTableColumn
nsBgpPeerRemoteAs = _NsBgpPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 9),
    _NsBgpPeerRemoteAs_Type()
)
nsBgpPeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerRemoteAs.setStatus("deprecated")
_NsBgpPeerInUpdates_Type = Counter32
_NsBgpPeerInUpdates_Object = MibTableColumn
nsBgpPeerInUpdates = _NsBgpPeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 10),
    _NsBgpPeerInUpdates_Type()
)
nsBgpPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerInUpdates.setStatus("deprecated")
_NsBgpPeerOutUpdates_Type = Counter32
_NsBgpPeerOutUpdates_Object = MibTableColumn
nsBgpPeerOutUpdates = _NsBgpPeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 11),
    _NsBgpPeerOutUpdates_Type()
)
nsBgpPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerOutUpdates.setStatus("deprecated")
_NsBgpPeerInTotalMessages_Type = Counter32
_NsBgpPeerInTotalMessages_Object = MibTableColumn
nsBgpPeerInTotalMessages = _NsBgpPeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 12),
    _NsBgpPeerInTotalMessages_Type()
)
nsBgpPeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerInTotalMessages.setStatus("deprecated")
_NsBgpPeerOutTotalMessages_Type = Counter32
_NsBgpPeerOutTotalMessages_Object = MibTableColumn
nsBgpPeerOutTotalMessages = _NsBgpPeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 13),
    _NsBgpPeerOutTotalMessages_Type()
)
nsBgpPeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerOutTotalMessages.setStatus("deprecated")


class _NsBgpPeerLastError_Type(OctetString):
    """Custom type nsBgpPeerLastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NsBgpPeerLastError_Type.__name__ = "OctetString"
_NsBgpPeerLastError_Object = MibTableColumn
nsBgpPeerLastError = _NsBgpPeerLastError_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 14),
    _NsBgpPeerLastError_Type()
)
nsBgpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerLastError.setStatus("deprecated")
_NsBgpPeerFsmEstablishedTransitions_Type = Counter32
_NsBgpPeerFsmEstablishedTransitions_Object = MibTableColumn
nsBgpPeerFsmEstablishedTransitions = _NsBgpPeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 15),
    _NsBgpPeerFsmEstablishedTransitions_Type()
)
nsBgpPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerFsmEstablishedTransitions.setStatus("deprecated")
_NsBgpPeerFsmEstablishedTime_Type = Gauge32
_NsBgpPeerFsmEstablishedTime_Object = MibTableColumn
nsBgpPeerFsmEstablishedTime = _NsBgpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 16),
    _NsBgpPeerFsmEstablishedTime_Type()
)
nsBgpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerFsmEstablishedTime.setStatus("deprecated")


class _NsBgpPeerConnectRetryInterval_Type(Integer32):
    """Custom type nsBgpPeerConnectRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NsBgpPeerConnectRetryInterval_Type.__name__ = "Integer32"
_NsBgpPeerConnectRetryInterval_Object = MibTableColumn
nsBgpPeerConnectRetryInterval = _NsBgpPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 17),
    _NsBgpPeerConnectRetryInterval_Type()
)
nsBgpPeerConnectRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerConnectRetryInterval.setStatus("deprecated")


class _NsBgpPeerHoldTime_Type(Integer32):
    """Custom type nsBgpPeerHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_NsBgpPeerHoldTime_Type.__name__ = "Integer32"
_NsBgpPeerHoldTime_Object = MibTableColumn
nsBgpPeerHoldTime = _NsBgpPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 18),
    _NsBgpPeerHoldTime_Type()
)
nsBgpPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerHoldTime.setStatus("deprecated")


class _NsBgpPeerKeepAlive_Type(Integer32):
    """Custom type nsBgpPeerKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_NsBgpPeerKeepAlive_Type.__name__ = "Integer32"
_NsBgpPeerKeepAlive_Object = MibTableColumn
nsBgpPeerKeepAlive = _NsBgpPeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 19),
    _NsBgpPeerKeepAlive_Type()
)
nsBgpPeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerKeepAlive.setStatus("deprecated")


class _NsBgpPeerHoldTimeConfigured_Type(Integer32):
    """Custom type nsBgpPeerHoldTimeConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_NsBgpPeerHoldTimeConfigured_Type.__name__ = "Integer32"
_NsBgpPeerHoldTimeConfigured_Object = MibTableColumn
nsBgpPeerHoldTimeConfigured = _NsBgpPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 20),
    _NsBgpPeerHoldTimeConfigured_Type()
)
nsBgpPeerHoldTimeConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerHoldTimeConfigured.setStatus("deprecated")


class _NsBgpPeerKeepAliveConfigured_Type(Integer32):
    """Custom type nsBgpPeerKeepAliveConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_NsBgpPeerKeepAliveConfigured_Type.__name__ = "Integer32"
_NsBgpPeerKeepAliveConfigured_Object = MibTableColumn
nsBgpPeerKeepAliveConfigured = _NsBgpPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 21),
    _NsBgpPeerKeepAliveConfigured_Type()
)
nsBgpPeerKeepAliveConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerKeepAliveConfigured.setStatus("deprecated")


class _NsBgpPeerMinASOriginationInterval_Type(Integer32):
    """Custom type nsBgpPeerMinASOriginationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NsBgpPeerMinASOriginationInterval_Type.__name__ = "Integer32"
_NsBgpPeerMinASOriginationInterval_Object = MibTableColumn
nsBgpPeerMinASOriginationInterval = _NsBgpPeerMinASOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 22),
    _NsBgpPeerMinASOriginationInterval_Type()
)
nsBgpPeerMinASOriginationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerMinASOriginationInterval.setStatus("deprecated")


class _NsBgpPeerMinRouteAdvertisementInterval_Type(Integer32):
    """Custom type nsBgpPeerMinRouteAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NsBgpPeerMinRouteAdvertisementInterval_Type.__name__ = "Integer32"
_NsBgpPeerMinRouteAdvertisementInterval_Object = MibTableColumn
nsBgpPeerMinRouteAdvertisementInterval = _NsBgpPeerMinRouteAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 23),
    _NsBgpPeerMinRouteAdvertisementInterval_Type()
)
nsBgpPeerMinRouteAdvertisementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerMinRouteAdvertisementInterval.setStatus("deprecated")
_NsBgpPeerInUpdateElapsedTime_Type = Gauge32
_NsBgpPeerInUpdateElapsedTime_Object = MibTableColumn
nsBgpPeerInUpdateElapsedTime = _NsBgpPeerInUpdateElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 24),
    _NsBgpPeerInUpdateElapsedTime_Type()
)
nsBgpPeerInUpdateElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerInUpdateElapsedTime.setStatus("deprecated")


class _NsBgpPeerVRID_Type(Integer32):
    """Custom type nsBgpPeerVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsBgpPeerVRID_Type.__name__ = "Integer32"
_NsBgpPeerVRID_Object = MibTableColumn
nsBgpPeerVRID = _NsBgpPeerVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 3, 1, 25),
    _NsBgpPeerVRID_Type()
)
nsBgpPeerVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgpPeerVRID.setStatus("deprecated")
_NsBgp4PathAttrTable_Object = MibTable
nsBgp4PathAttrTable = _NsBgp4PathAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6)
)
if mibBuilder.loadTexts:
    nsBgp4PathAttrTable.setStatus("deprecated")
_NsBgp4PathAttrEntry_Object = MibTableRow
nsBgp4PathAttrEntry = _NsBgp4PathAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1)
)
nsBgp4PathAttrEntry.setIndexNames(
    (0, "NETSCREEN-BGP4-MIB", "nsBgp4PathAttrIpAddrPrefix"),
    (0, "NETSCREEN-BGP4-MIB", "nsBgp4PathAttrIpAddrPrefixLen"),
    (0, "NETSCREEN-BGP4-MIB", "nsBgp4PathAttrPeer"),
    (0, "NETSCREEN-BGP4-MIB", "nsBgp4PathAttrVRID"),
)
if mibBuilder.loadTexts:
    nsBgp4PathAttrEntry.setStatus("deprecated")
_NsBgp4PathAttrPeer_Type = IpAddress
_NsBgp4PathAttrPeer_Object = MibTableColumn
nsBgp4PathAttrPeer = _NsBgp4PathAttrPeer_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 1),
    _NsBgp4PathAttrPeer_Type()
)
nsBgp4PathAttrPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrPeer.setStatus("deprecated")


class _NsBgp4PathAttrIpAddrPrefixLen_Type(Integer32):
    """Custom type nsBgp4PathAttrIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_NsBgp4PathAttrIpAddrPrefixLen_Type.__name__ = "Integer32"
_NsBgp4PathAttrIpAddrPrefixLen_Object = MibTableColumn
nsBgp4PathAttrIpAddrPrefixLen = _NsBgp4PathAttrIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 2),
    _NsBgp4PathAttrIpAddrPrefixLen_Type()
)
nsBgp4PathAttrIpAddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrIpAddrPrefixLen.setStatus("deprecated")
_NsBgp4PathAttrIpAddrPrefix_Type = IpAddress
_NsBgp4PathAttrIpAddrPrefix_Object = MibTableColumn
nsBgp4PathAttrIpAddrPrefix = _NsBgp4PathAttrIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 3),
    _NsBgp4PathAttrIpAddrPrefix_Type()
)
nsBgp4PathAttrIpAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrIpAddrPrefix.setStatus("deprecated")


class _NsBgp4PathAttrOrigin_Type(Integer32):
    """Custom type nsBgp4PathAttrOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3))
    )


_NsBgp4PathAttrOrigin_Type.__name__ = "Integer32"
_NsBgp4PathAttrOrigin_Object = MibTableColumn
nsBgp4PathAttrOrigin = _NsBgp4PathAttrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 4),
    _NsBgp4PathAttrOrigin_Type()
)
nsBgp4PathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrOrigin.setStatus("deprecated")


class _NsBgp4PathAttrASPathSegment_Type(OctetString):
    """Custom type nsBgp4PathAttrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_NsBgp4PathAttrASPathSegment_Type.__name__ = "OctetString"
_NsBgp4PathAttrASPathSegment_Object = MibTableColumn
nsBgp4PathAttrASPathSegment = _NsBgp4PathAttrASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 5),
    _NsBgp4PathAttrASPathSegment_Type()
)
nsBgp4PathAttrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrASPathSegment.setStatus("deprecated")
_NsBgp4PathAttrNextHop_Type = IpAddress
_NsBgp4PathAttrNextHop_Object = MibTableColumn
nsBgp4PathAttrNextHop = _NsBgp4PathAttrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 6),
    _NsBgp4PathAttrNextHop_Type()
)
nsBgp4PathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrNextHop.setStatus("deprecated")


class _NsBgp4PathAttrMultiExitDisc_Type(Integer32):
    """Custom type nsBgp4PathAttrMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_NsBgp4PathAttrMultiExitDisc_Type.__name__ = "Integer32"
_NsBgp4PathAttrMultiExitDisc_Object = MibTableColumn
nsBgp4PathAttrMultiExitDisc = _NsBgp4PathAttrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 7),
    _NsBgp4PathAttrMultiExitDisc_Type()
)
nsBgp4PathAttrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrMultiExitDisc.setStatus("deprecated")


class _NsBgp4PathAttrLocalPref_Type(Integer32):
    """Custom type nsBgp4PathAttrLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_NsBgp4PathAttrLocalPref_Type.__name__ = "Integer32"
_NsBgp4PathAttrLocalPref_Object = MibTableColumn
nsBgp4PathAttrLocalPref = _NsBgp4PathAttrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 8),
    _NsBgp4PathAttrLocalPref_Type()
)
nsBgp4PathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrLocalPref.setStatus("deprecated")


class _NsBgp4PathAttrAtomicAggregate_Type(Integer32):
    """Custom type nsBgp4PathAttrAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessSpecificRouteSelected", 2),
          ("lessSpecificRrouteNotSelected", 1))
    )


_NsBgp4PathAttrAtomicAggregate_Type.__name__ = "Integer32"
_NsBgp4PathAttrAtomicAggregate_Object = MibTableColumn
nsBgp4PathAttrAtomicAggregate = _NsBgp4PathAttrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 9),
    _NsBgp4PathAttrAtomicAggregate_Type()
)
nsBgp4PathAttrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrAtomicAggregate.setStatus("deprecated")


class _NsBgp4PathAttrAggregatorAS_Type(Integer32):
    """Custom type nsBgp4PathAttrAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsBgp4PathAttrAggregatorAS_Type.__name__ = "Integer32"
_NsBgp4PathAttrAggregatorAS_Object = MibTableColumn
nsBgp4PathAttrAggregatorAS = _NsBgp4PathAttrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 10),
    _NsBgp4PathAttrAggregatorAS_Type()
)
nsBgp4PathAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrAggregatorAS.setStatus("deprecated")
_NsBgp4PathAttrAggregatorAddr_Type = IpAddress
_NsBgp4PathAttrAggregatorAddr_Object = MibTableColumn
nsBgp4PathAttrAggregatorAddr = _NsBgp4PathAttrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 11),
    _NsBgp4PathAttrAggregatorAddr_Type()
)
nsBgp4PathAttrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrAggregatorAddr.setStatus("deprecated")


class _NsBgp4PathAttrCalcLocalPref_Type(Integer32):
    """Custom type nsBgp4PathAttrCalcLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_NsBgp4PathAttrCalcLocalPref_Type.__name__ = "Integer32"
_NsBgp4PathAttrCalcLocalPref_Object = MibTableColumn
nsBgp4PathAttrCalcLocalPref = _NsBgp4PathAttrCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 12),
    _NsBgp4PathAttrCalcLocalPref_Type()
)
nsBgp4PathAttrCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrCalcLocalPref.setStatus("deprecated")


class _NsBgp4PathAttrBest_Type(Integer32):
    """Custom type nsBgp4PathAttrBest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_NsBgp4PathAttrBest_Type.__name__ = "Integer32"
_NsBgp4PathAttrBest_Object = MibTableColumn
nsBgp4PathAttrBest = _NsBgp4PathAttrBest_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 13),
    _NsBgp4PathAttrBest_Type()
)
nsBgp4PathAttrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrBest.setStatus("deprecated")


class _NsBgp4PathAttrUnknown_Type(OctetString):
    """Custom type nsBgp4PathAttrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsBgp4PathAttrUnknown_Type.__name__ = "OctetString"
_NsBgp4PathAttrUnknown_Object = MibTableColumn
nsBgp4PathAttrUnknown = _NsBgp4PathAttrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 14),
    _NsBgp4PathAttrUnknown_Type()
)
nsBgp4PathAttrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrUnknown.setStatus("deprecated")


class _NsBgp4PathAttrVRID_Type(Integer32):
    """Custom type nsBgp4PathAttrVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsBgp4PathAttrVRID_Type.__name__ = "Integer32"
_NsBgp4PathAttrVRID_Object = MibTableColumn
nsBgp4PathAttrVRID = _NsBgp4PathAttrVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 6, 1, 15),
    _NsBgp4PathAttrVRID_Type()
)
nsBgp4PathAttrVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsBgp4PathAttrVRID.setStatus("deprecated")
_NsBgpTraps_ObjectIdentity = ObjectIdentity
nsBgpTraps = _NsBgpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 7)
)

# Managed Objects groups


# Notification objects

nsBgpEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 3, 7, 1)
)
nsBgpEstablished.setObjects(
      *(("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-BGP4-MIB", "nsBgpPeerIdentifier"),
        ("NETSCREEN-BGP4-MIB", "nsBgpPeerVRID"),
        ("NETSCREEN-BGP4-MIB", "nsBgpPeerLastError"),
        ("NETSCREEN-BGP4-MIB", "nsBgpPeerState"))
)
if mibBuilder.loadTexts:
    nsBgpEstablished.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-BGP4-MIB",
    **{"nsBgp": nsBgp,
       "nsBgpInfoTable": nsBgpInfoTable,
       "nsBgpInfoEntry": nsBgpInfoEntry,
       "nsBgpInfoVersion": nsBgpInfoVersion,
       "nsBgpInfoLocalAs": nsBgpInfoLocalAs,
       "nsBgpInfoIdentifier": nsBgpInfoIdentifier,
       "nsBgpInfoVRID": nsBgpInfoVRID,
       "nsBgpPeerTable": nsBgpPeerTable,
       "nsBgpPeerEntry": nsBgpPeerEntry,
       "nsBgpPeerIdentifier": nsBgpPeerIdentifier,
       "nsBgpPeerState": nsBgpPeerState,
       "nsBgpPeerAdminStatus": nsBgpPeerAdminStatus,
       "nsBgpPeerNegotiatedVersion": nsBgpPeerNegotiatedVersion,
       "nsBgpPeerLocalAddr": nsBgpPeerLocalAddr,
       "nsBgpPeerLocalPort": nsBgpPeerLocalPort,
       "nsBgpPeerRemoteAddr": nsBgpPeerRemoteAddr,
       "nsBgpPeerRemotePort": nsBgpPeerRemotePort,
       "nsBgpPeerRemoteAs": nsBgpPeerRemoteAs,
       "nsBgpPeerInUpdates": nsBgpPeerInUpdates,
       "nsBgpPeerOutUpdates": nsBgpPeerOutUpdates,
       "nsBgpPeerInTotalMessages": nsBgpPeerInTotalMessages,
       "nsBgpPeerOutTotalMessages": nsBgpPeerOutTotalMessages,
       "nsBgpPeerLastError": nsBgpPeerLastError,
       "nsBgpPeerFsmEstablishedTransitions": nsBgpPeerFsmEstablishedTransitions,
       "nsBgpPeerFsmEstablishedTime": nsBgpPeerFsmEstablishedTime,
       "nsBgpPeerConnectRetryInterval": nsBgpPeerConnectRetryInterval,
       "nsBgpPeerHoldTime": nsBgpPeerHoldTime,
       "nsBgpPeerKeepAlive": nsBgpPeerKeepAlive,
       "nsBgpPeerHoldTimeConfigured": nsBgpPeerHoldTimeConfigured,
       "nsBgpPeerKeepAliveConfigured": nsBgpPeerKeepAliveConfigured,
       "nsBgpPeerMinASOriginationInterval": nsBgpPeerMinASOriginationInterval,
       "nsBgpPeerMinRouteAdvertisementInterval": nsBgpPeerMinRouteAdvertisementInterval,
       "nsBgpPeerInUpdateElapsedTime": nsBgpPeerInUpdateElapsedTime,
       "nsBgpPeerVRID": nsBgpPeerVRID,
       "nsBgp4PathAttrTable": nsBgp4PathAttrTable,
       "nsBgp4PathAttrEntry": nsBgp4PathAttrEntry,
       "nsBgp4PathAttrPeer": nsBgp4PathAttrPeer,
       "nsBgp4PathAttrIpAddrPrefixLen": nsBgp4PathAttrIpAddrPrefixLen,
       "nsBgp4PathAttrIpAddrPrefix": nsBgp4PathAttrIpAddrPrefix,
       "nsBgp4PathAttrOrigin": nsBgp4PathAttrOrigin,
       "nsBgp4PathAttrASPathSegment": nsBgp4PathAttrASPathSegment,
       "nsBgp4PathAttrNextHop": nsBgp4PathAttrNextHop,
       "nsBgp4PathAttrMultiExitDisc": nsBgp4PathAttrMultiExitDisc,
       "nsBgp4PathAttrLocalPref": nsBgp4PathAttrLocalPref,
       "nsBgp4PathAttrAtomicAggregate": nsBgp4PathAttrAtomicAggregate,
       "nsBgp4PathAttrAggregatorAS": nsBgp4PathAttrAggregatorAS,
       "nsBgp4PathAttrAggregatorAddr": nsBgp4PathAttrAggregatorAddr,
       "nsBgp4PathAttrCalcLocalPref": nsBgp4PathAttrCalcLocalPref,
       "nsBgp4PathAttrBest": nsBgp4PathAttrBest,
       "nsBgp4PathAttrUnknown": nsBgp4PathAttrUnknown,
       "nsBgp4PathAttrVRID": nsBgp4PathAttrVRID,
       "nsBgpTraps": nsBgpTraps,
       "nsBgpEstablished": nsBgpEstablished}
)
