# SNMP MIB module (NETSCREEN-VR-BGP4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-VR-BGP4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:08 2024
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

nsVrBgp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsVrBgpInfoTable_Object = MibTable
nsVrBgpInfoTable = _NsVrBgpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 1)
)
if mibBuilder.loadTexts:
    nsVrBgpInfoTable.setStatus("current")
_NsVrBgpInfoEntry_Object = MibTableRow
nsVrBgpInfoEntry = _NsVrBgpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 1, 1)
)
nsVrBgpInfoEntry.setIndexNames(
    (0, "NETSCREEN-VR-BGP4-MIB", "nsVrBgpInfoVRID"),
)
if mibBuilder.loadTexts:
    nsVrBgpInfoEntry.setStatus("current")


class _NsVrBgpInfoVersion_Type(OctetString):
    """Custom type nsVrBgpInfoVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NsVrBgpInfoVersion_Type.__name__ = "OctetString"
_NsVrBgpInfoVersion_Object = MibTableColumn
nsVrBgpInfoVersion = _NsVrBgpInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 1, 1, 1),
    _NsVrBgpInfoVersion_Type()
)
nsVrBgpInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpInfoVersion.setStatus("current")


class _NsVrBgpInfoLocalAs_Type(Integer32):
    """Custom type nsVrBgpInfoLocalAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrBgpInfoLocalAs_Type.__name__ = "Integer32"
_NsVrBgpInfoLocalAs_Object = MibTableColumn
nsVrBgpInfoLocalAs = _NsVrBgpInfoLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 1, 1, 2),
    _NsVrBgpInfoLocalAs_Type()
)
nsVrBgpInfoLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpInfoLocalAs.setStatus("current")
_NsVrBgpInfoIdentifier_Type = IpAddress
_NsVrBgpInfoIdentifier_Object = MibTableColumn
nsVrBgpInfoIdentifier = _NsVrBgpInfoIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 1, 1, 3),
    _NsVrBgpInfoIdentifier_Type()
)
nsVrBgpInfoIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpInfoIdentifier.setStatus("current")


class _NsVrBgpInfoVRID_Type(Integer32):
    """Custom type nsVrBgpInfoVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrBgpInfoVRID_Type.__name__ = "Integer32"
_NsVrBgpInfoVRID_Object = MibTableColumn
nsVrBgpInfoVRID = _NsVrBgpInfoVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 1, 1, 4),
    _NsVrBgpInfoVRID_Type()
)
nsVrBgpInfoVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpInfoVRID.setStatus("current")
_NsVrBgpPeerTable_Object = MibTable
nsVrBgpPeerTable = _NsVrBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3)
)
if mibBuilder.loadTexts:
    nsVrBgpPeerTable.setStatus("current")
_NsVrBgpPeerEntry_Object = MibTableRow
nsVrBgpPeerEntry = _NsVrBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1)
)
nsVrBgpPeerEntry.setIndexNames(
    (0, "NETSCREEN-VR-BGP4-MIB", "nsVrBgpPeerVRID"),
    (0, "NETSCREEN-VR-BGP4-MIB", "nsVrBgpPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    nsVrBgpPeerEntry.setStatus("current")
_NsVrBgpPeerIdentifier_Type = IpAddress
_NsVrBgpPeerIdentifier_Object = MibTableColumn
nsVrBgpPeerIdentifier = _NsVrBgpPeerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 1),
    _NsVrBgpPeerIdentifier_Type()
)
nsVrBgpPeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerIdentifier.setStatus("current")


class _NsVrBgpPeerState_Type(Integer32):
    """Custom type nsVrBgpPeerState based on Integer32"""
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


_NsVrBgpPeerState_Type.__name__ = "Integer32"
_NsVrBgpPeerState_Object = MibTableColumn
nsVrBgpPeerState = _NsVrBgpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 2),
    _NsVrBgpPeerState_Type()
)
nsVrBgpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerState.setStatus("current")


class _NsVrBgpPeerAdminStatus_Type(Integer32):
    """Custom type nsVrBgpPeerAdminStatus based on Integer32"""
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


_NsVrBgpPeerAdminStatus_Type.__name__ = "Integer32"
_NsVrBgpPeerAdminStatus_Object = MibTableColumn
nsVrBgpPeerAdminStatus = _NsVrBgpPeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 3),
    _NsVrBgpPeerAdminStatus_Type()
)
nsVrBgpPeerAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerAdminStatus.setStatus("current")
_NsVrBgpPeerNegotiatedVersion_Type = Integer32
_NsVrBgpPeerNegotiatedVersion_Object = MibTableColumn
nsVrBgpPeerNegotiatedVersion = _NsVrBgpPeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 4),
    _NsVrBgpPeerNegotiatedVersion_Type()
)
nsVrBgpPeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerNegotiatedVersion.setStatus("current")
_NsVrBgpPeerLocalAddr_Type = IpAddress
_NsVrBgpPeerLocalAddr_Object = MibTableColumn
nsVrBgpPeerLocalAddr = _NsVrBgpPeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 5),
    _NsVrBgpPeerLocalAddr_Type()
)
nsVrBgpPeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerLocalAddr.setStatus("current")


class _NsVrBgpPeerLocalPort_Type(Integer32):
    """Custom type nsVrBgpPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrBgpPeerLocalPort_Type.__name__ = "Integer32"
_NsVrBgpPeerLocalPort_Object = MibTableColumn
nsVrBgpPeerLocalPort = _NsVrBgpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 6),
    _NsVrBgpPeerLocalPort_Type()
)
nsVrBgpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerLocalPort.setStatus("current")
_NsVrBgpPeerRemoteAddr_Type = IpAddress
_NsVrBgpPeerRemoteAddr_Object = MibTableColumn
nsVrBgpPeerRemoteAddr = _NsVrBgpPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 7),
    _NsVrBgpPeerRemoteAddr_Type()
)
nsVrBgpPeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerRemoteAddr.setStatus("current")


class _NsVrBgpPeerRemotePort_Type(Integer32):
    """Custom type nsVrBgpPeerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrBgpPeerRemotePort_Type.__name__ = "Integer32"
_NsVrBgpPeerRemotePort_Object = MibTableColumn
nsVrBgpPeerRemotePort = _NsVrBgpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 8),
    _NsVrBgpPeerRemotePort_Type()
)
nsVrBgpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerRemotePort.setStatus("current")


class _NsVrBgpPeerRemoteAs_Type(Integer32):
    """Custom type nsVrBgpPeerRemoteAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrBgpPeerRemoteAs_Type.__name__ = "Integer32"
_NsVrBgpPeerRemoteAs_Object = MibTableColumn
nsVrBgpPeerRemoteAs = _NsVrBgpPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 9),
    _NsVrBgpPeerRemoteAs_Type()
)
nsVrBgpPeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerRemoteAs.setStatus("current")
_NsVrBgpPeerInUpdates_Type = Counter32
_NsVrBgpPeerInUpdates_Object = MibTableColumn
nsVrBgpPeerInUpdates = _NsVrBgpPeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 10),
    _NsVrBgpPeerInUpdates_Type()
)
nsVrBgpPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerInUpdates.setStatus("current")
_NsVrBgpPeerOutUpdates_Type = Counter32
_NsVrBgpPeerOutUpdates_Object = MibTableColumn
nsVrBgpPeerOutUpdates = _NsVrBgpPeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 11),
    _NsVrBgpPeerOutUpdates_Type()
)
nsVrBgpPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerOutUpdates.setStatus("current")
_NsVrBgpPeerInTotalMessages_Type = Counter32
_NsVrBgpPeerInTotalMessages_Object = MibTableColumn
nsVrBgpPeerInTotalMessages = _NsVrBgpPeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 12),
    _NsVrBgpPeerInTotalMessages_Type()
)
nsVrBgpPeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerInTotalMessages.setStatus("current")
_NsVrBgpPeerOutTotalMessages_Type = Counter32
_NsVrBgpPeerOutTotalMessages_Object = MibTableColumn
nsVrBgpPeerOutTotalMessages = _NsVrBgpPeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 13),
    _NsVrBgpPeerOutTotalMessages_Type()
)
nsVrBgpPeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerOutTotalMessages.setStatus("current")


class _NsVrBgpPeerLastError_Type(OctetString):
    """Custom type nsVrBgpPeerLastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NsVrBgpPeerLastError_Type.__name__ = "OctetString"
_NsVrBgpPeerLastError_Object = MibTableColumn
nsVrBgpPeerLastError = _NsVrBgpPeerLastError_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 14),
    _NsVrBgpPeerLastError_Type()
)
nsVrBgpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerLastError.setStatus("current")
_NsVrBgpPeerFsmEstablishedTransitions_Type = Counter32
_NsVrBgpPeerFsmEstablishedTransitions_Object = MibTableColumn
nsVrBgpPeerFsmEstablishedTransitions = _NsVrBgpPeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 15),
    _NsVrBgpPeerFsmEstablishedTransitions_Type()
)
nsVrBgpPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerFsmEstablishedTransitions.setStatus("current")
_NsVrBgpPeerFsmEstablishedTime_Type = Gauge32
_NsVrBgpPeerFsmEstablishedTime_Object = MibTableColumn
nsVrBgpPeerFsmEstablishedTime = _NsVrBgpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 16),
    _NsVrBgpPeerFsmEstablishedTime_Type()
)
nsVrBgpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerFsmEstablishedTime.setStatus("current")


class _NsVrBgpPeerConnectRetryInterval_Type(Integer32):
    """Custom type nsVrBgpPeerConnectRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NsVrBgpPeerConnectRetryInterval_Type.__name__ = "Integer32"
_NsVrBgpPeerConnectRetryInterval_Object = MibTableColumn
nsVrBgpPeerConnectRetryInterval = _NsVrBgpPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 17),
    _NsVrBgpPeerConnectRetryInterval_Type()
)
nsVrBgpPeerConnectRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerConnectRetryInterval.setStatus("current")


class _NsVrBgpPeerHoldTime_Type(Integer32):
    """Custom type nsVrBgpPeerHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_NsVrBgpPeerHoldTime_Type.__name__ = "Integer32"
_NsVrBgpPeerHoldTime_Object = MibTableColumn
nsVrBgpPeerHoldTime = _NsVrBgpPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 18),
    _NsVrBgpPeerHoldTime_Type()
)
nsVrBgpPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerHoldTime.setStatus("current")


class _NsVrBgpPeerKeepAlive_Type(Integer32):
    """Custom type nsVrBgpPeerKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_NsVrBgpPeerKeepAlive_Type.__name__ = "Integer32"
_NsVrBgpPeerKeepAlive_Object = MibTableColumn
nsVrBgpPeerKeepAlive = _NsVrBgpPeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 19),
    _NsVrBgpPeerKeepAlive_Type()
)
nsVrBgpPeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerKeepAlive.setStatus("current")


class _NsVrBgpPeerHoldTimeConfigured_Type(Integer32):
    """Custom type nsVrBgpPeerHoldTimeConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_NsVrBgpPeerHoldTimeConfigured_Type.__name__ = "Integer32"
_NsVrBgpPeerHoldTimeConfigured_Object = MibTableColumn
nsVrBgpPeerHoldTimeConfigured = _NsVrBgpPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 20),
    _NsVrBgpPeerHoldTimeConfigured_Type()
)
nsVrBgpPeerHoldTimeConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerHoldTimeConfigured.setStatus("current")


class _NsVrBgpPeerKeepAliveConfigured_Type(Integer32):
    """Custom type nsVrBgpPeerKeepAliveConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_NsVrBgpPeerKeepAliveConfigured_Type.__name__ = "Integer32"
_NsVrBgpPeerKeepAliveConfigured_Object = MibTableColumn
nsVrBgpPeerKeepAliveConfigured = _NsVrBgpPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 21),
    _NsVrBgpPeerKeepAliveConfigured_Type()
)
nsVrBgpPeerKeepAliveConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerKeepAliveConfigured.setStatus("current")


class _NsVrBgpPeerMinASOriginationInterval_Type(Integer32):
    """Custom type nsVrBgpPeerMinASOriginationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NsVrBgpPeerMinASOriginationInterval_Type.__name__ = "Integer32"
_NsVrBgpPeerMinASOriginationInterval_Object = MibTableColumn
nsVrBgpPeerMinASOriginationInterval = _NsVrBgpPeerMinASOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 22),
    _NsVrBgpPeerMinASOriginationInterval_Type()
)
nsVrBgpPeerMinASOriginationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerMinASOriginationInterval.setStatus("current")


class _NsVrBgpPeerMinRouteAdvertisementInterval_Type(Integer32):
    """Custom type nsVrBgpPeerMinRouteAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NsVrBgpPeerMinRouteAdvertisementInterval_Type.__name__ = "Integer32"
_NsVrBgpPeerMinRouteAdvertisementInterval_Object = MibTableColumn
nsVrBgpPeerMinRouteAdvertisementInterval = _NsVrBgpPeerMinRouteAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 23),
    _NsVrBgpPeerMinRouteAdvertisementInterval_Type()
)
nsVrBgpPeerMinRouteAdvertisementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerMinRouteAdvertisementInterval.setStatus("current")
_NsVrBgpPeerInUpdateElapsedTime_Type = Gauge32
_NsVrBgpPeerInUpdateElapsedTime_Object = MibTableColumn
nsVrBgpPeerInUpdateElapsedTime = _NsVrBgpPeerInUpdateElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 24),
    _NsVrBgpPeerInUpdateElapsedTime_Type()
)
nsVrBgpPeerInUpdateElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerInUpdateElapsedTime.setStatus("current")


class _NsVrBgpPeerVRID_Type(Integer32):
    """Custom type nsVrBgpPeerVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrBgpPeerVRID_Type.__name__ = "Integer32"
_NsVrBgpPeerVRID_Object = MibTableColumn
nsVrBgpPeerVRID = _NsVrBgpPeerVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 3, 1, 25),
    _NsVrBgpPeerVRID_Type()
)
nsVrBgpPeerVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgpPeerVRID.setStatus("current")
_NsVrBgp4PathAttrTable_Object = MibTable
nsVrBgp4PathAttrTable = _NsVrBgp4PathAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6)
)
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrTable.setStatus("current")
_NsVrBgp4PathAttrEntry_Object = MibTableRow
nsVrBgp4PathAttrEntry = _NsVrBgp4PathAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1)
)
nsVrBgp4PathAttrEntry.setIndexNames(
    (0, "NETSCREEN-VR-BGP4-MIB", "nsVrBgp4PathAttrVRID"),
    (0, "NETSCREEN-VR-BGP4-MIB", "nsVrBgp4PathAttrIpAddrPrefix"),
    (0, "NETSCREEN-VR-BGP4-MIB", "nsVrBgp4PathAttrIpAddrPrefixLen"),
    (0, "NETSCREEN-VR-BGP4-MIB", "nsVrBgp4PathAttrPeer"),
)
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrEntry.setStatus("current")
_NsVrBgp4PathAttrPeer_Type = IpAddress
_NsVrBgp4PathAttrPeer_Object = MibTableColumn
nsVrBgp4PathAttrPeer = _NsVrBgp4PathAttrPeer_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 1),
    _NsVrBgp4PathAttrPeer_Type()
)
nsVrBgp4PathAttrPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrPeer.setStatus("current")


class _NsVrBgp4PathAttrIpAddrPrefixLen_Type(Integer32):
    """Custom type nsVrBgp4PathAttrIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_NsVrBgp4PathAttrIpAddrPrefixLen_Type.__name__ = "Integer32"
_NsVrBgp4PathAttrIpAddrPrefixLen_Object = MibTableColumn
nsVrBgp4PathAttrIpAddrPrefixLen = _NsVrBgp4PathAttrIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 2),
    _NsVrBgp4PathAttrIpAddrPrefixLen_Type()
)
nsVrBgp4PathAttrIpAddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrIpAddrPrefixLen.setStatus("current")
_NsVrBgp4PathAttrIpAddrPrefix_Type = IpAddress
_NsVrBgp4PathAttrIpAddrPrefix_Object = MibTableColumn
nsVrBgp4PathAttrIpAddrPrefix = _NsVrBgp4PathAttrIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 3),
    _NsVrBgp4PathAttrIpAddrPrefix_Type()
)
nsVrBgp4PathAttrIpAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrIpAddrPrefix.setStatus("current")


class _NsVrBgp4PathAttrOrigin_Type(Integer32):
    """Custom type nsVrBgp4PathAttrOrigin based on Integer32"""
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


_NsVrBgp4PathAttrOrigin_Type.__name__ = "Integer32"
_NsVrBgp4PathAttrOrigin_Object = MibTableColumn
nsVrBgp4PathAttrOrigin = _NsVrBgp4PathAttrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 4),
    _NsVrBgp4PathAttrOrigin_Type()
)
nsVrBgp4PathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrOrigin.setStatus("current")


class _NsVrBgp4PathAttrASPathSegment_Type(OctetString):
    """Custom type nsVrBgp4PathAttrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_NsVrBgp4PathAttrASPathSegment_Type.__name__ = "OctetString"
_NsVrBgp4PathAttrASPathSegment_Object = MibTableColumn
nsVrBgp4PathAttrASPathSegment = _NsVrBgp4PathAttrASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 5),
    _NsVrBgp4PathAttrASPathSegment_Type()
)
nsVrBgp4PathAttrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrASPathSegment.setStatus("current")
_NsVrBgp4PathAttrNextHop_Type = IpAddress
_NsVrBgp4PathAttrNextHop_Object = MibTableColumn
nsVrBgp4PathAttrNextHop = _NsVrBgp4PathAttrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 6),
    _NsVrBgp4PathAttrNextHop_Type()
)
nsVrBgp4PathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrNextHop.setStatus("current")


class _NsVrBgp4PathAttrMultiExitDisc_Type(Integer32):
    """Custom type nsVrBgp4PathAttrMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_NsVrBgp4PathAttrMultiExitDisc_Type.__name__ = "Integer32"
_NsVrBgp4PathAttrMultiExitDisc_Object = MibTableColumn
nsVrBgp4PathAttrMultiExitDisc = _NsVrBgp4PathAttrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 7),
    _NsVrBgp4PathAttrMultiExitDisc_Type()
)
nsVrBgp4PathAttrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrMultiExitDisc.setStatus("current")


class _NsVrBgp4PathAttrLocalPref_Type(Integer32):
    """Custom type nsVrBgp4PathAttrLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_NsVrBgp4PathAttrLocalPref_Type.__name__ = "Integer32"
_NsVrBgp4PathAttrLocalPref_Object = MibTableColumn
nsVrBgp4PathAttrLocalPref = _NsVrBgp4PathAttrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 8),
    _NsVrBgp4PathAttrLocalPref_Type()
)
nsVrBgp4PathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrLocalPref.setStatus("current")


class _NsVrBgp4PathAttrAtomicAggregate_Type(Integer32):
    """Custom type nsVrBgp4PathAttrAtomicAggregate based on Integer32"""
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


_NsVrBgp4PathAttrAtomicAggregate_Type.__name__ = "Integer32"
_NsVrBgp4PathAttrAtomicAggregate_Object = MibTableColumn
nsVrBgp4PathAttrAtomicAggregate = _NsVrBgp4PathAttrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 9),
    _NsVrBgp4PathAttrAtomicAggregate_Type()
)
nsVrBgp4PathAttrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrAtomicAggregate.setStatus("current")


class _NsVrBgp4PathAttrAggregatorAS_Type(Integer32):
    """Custom type nsVrBgp4PathAttrAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrBgp4PathAttrAggregatorAS_Type.__name__ = "Integer32"
_NsVrBgp4PathAttrAggregatorAS_Object = MibTableColumn
nsVrBgp4PathAttrAggregatorAS = _NsVrBgp4PathAttrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 10),
    _NsVrBgp4PathAttrAggregatorAS_Type()
)
nsVrBgp4PathAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrAggregatorAS.setStatus("current")
_NsVrBgp4PathAttrAggregatorAddr_Type = IpAddress
_NsVrBgp4PathAttrAggregatorAddr_Object = MibTableColumn
nsVrBgp4PathAttrAggregatorAddr = _NsVrBgp4PathAttrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 11),
    _NsVrBgp4PathAttrAggregatorAddr_Type()
)
nsVrBgp4PathAttrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrAggregatorAddr.setStatus("current")


class _NsVrBgp4PathAttrCalcLocalPref_Type(Integer32):
    """Custom type nsVrBgp4PathAttrCalcLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_NsVrBgp4PathAttrCalcLocalPref_Type.__name__ = "Integer32"
_NsVrBgp4PathAttrCalcLocalPref_Object = MibTableColumn
nsVrBgp4PathAttrCalcLocalPref = _NsVrBgp4PathAttrCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 12),
    _NsVrBgp4PathAttrCalcLocalPref_Type()
)
nsVrBgp4PathAttrCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrCalcLocalPref.setStatus("current")


class _NsVrBgp4PathAttrBest_Type(Integer32):
    """Custom type nsVrBgp4PathAttrBest based on Integer32"""
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


_NsVrBgp4PathAttrBest_Type.__name__ = "Integer32"
_NsVrBgp4PathAttrBest_Object = MibTableColumn
nsVrBgp4PathAttrBest = _NsVrBgp4PathAttrBest_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 13),
    _NsVrBgp4PathAttrBest_Type()
)
nsVrBgp4PathAttrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrBest.setStatus("current")


class _NsVrBgp4PathAttrUnknown_Type(OctetString):
    """Custom type nsVrBgp4PathAttrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsVrBgp4PathAttrUnknown_Type.__name__ = "OctetString"
_NsVrBgp4PathAttrUnknown_Object = MibTableColumn
nsVrBgp4PathAttrUnknown = _NsVrBgp4PathAttrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 14),
    _NsVrBgp4PathAttrUnknown_Type()
)
nsVrBgp4PathAttrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrUnknown.setStatus("current")


class _NsVrBgp4PathAttrVRID_Type(Integer32):
    """Custom type nsVrBgp4PathAttrVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrBgp4PathAttrVRID_Type.__name__ = "Integer32"
_NsVrBgp4PathAttrVRID_Object = MibTableColumn
nsVrBgp4PathAttrVRID = _NsVrBgp4PathAttrVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 6, 1, 15),
    _NsVrBgp4PathAttrVRID_Type()
)
nsVrBgp4PathAttrVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrBgp4PathAttrVRID.setStatus("current")
_NsVrBgpTraps_ObjectIdentity = ObjectIdentity
nsVrBgpTraps = _NsVrBgpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 7)
)

# Managed Objects groups


# Notification objects

nsVrBgpEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3224, 18, 6, 7, 1)
)
nsVrBgpEstablished.setObjects(
      *(("NETSCREEN-VR-BGP4-MIB", "nsVrBgp4PathAttrVRID"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapType"),
        ("NETSCREEN-TRAP-MIB", "netscreenTrapDesc"),
        ("NETSCREEN-VR-BGP4-MIB", "nsVrBgpPeerIdentifier"),
        ("NETSCREEN-VR-BGP4-MIB", "nsVrBgpPeerLastError"),
        ("NETSCREEN-VR-BGP4-MIB", "nsVrBgpPeerState"))
)
if mibBuilder.loadTexts:
    nsVrBgpEstablished.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VR-BGP4-MIB",
    **{"nsVrBgp": nsVrBgp,
       "nsVrBgpInfoTable": nsVrBgpInfoTable,
       "nsVrBgpInfoEntry": nsVrBgpInfoEntry,
       "nsVrBgpInfoVersion": nsVrBgpInfoVersion,
       "nsVrBgpInfoLocalAs": nsVrBgpInfoLocalAs,
       "nsVrBgpInfoIdentifier": nsVrBgpInfoIdentifier,
       "nsVrBgpInfoVRID": nsVrBgpInfoVRID,
       "nsVrBgpPeerTable": nsVrBgpPeerTable,
       "nsVrBgpPeerEntry": nsVrBgpPeerEntry,
       "nsVrBgpPeerIdentifier": nsVrBgpPeerIdentifier,
       "nsVrBgpPeerState": nsVrBgpPeerState,
       "nsVrBgpPeerAdminStatus": nsVrBgpPeerAdminStatus,
       "nsVrBgpPeerNegotiatedVersion": nsVrBgpPeerNegotiatedVersion,
       "nsVrBgpPeerLocalAddr": nsVrBgpPeerLocalAddr,
       "nsVrBgpPeerLocalPort": nsVrBgpPeerLocalPort,
       "nsVrBgpPeerRemoteAddr": nsVrBgpPeerRemoteAddr,
       "nsVrBgpPeerRemotePort": nsVrBgpPeerRemotePort,
       "nsVrBgpPeerRemoteAs": nsVrBgpPeerRemoteAs,
       "nsVrBgpPeerInUpdates": nsVrBgpPeerInUpdates,
       "nsVrBgpPeerOutUpdates": nsVrBgpPeerOutUpdates,
       "nsVrBgpPeerInTotalMessages": nsVrBgpPeerInTotalMessages,
       "nsVrBgpPeerOutTotalMessages": nsVrBgpPeerOutTotalMessages,
       "nsVrBgpPeerLastError": nsVrBgpPeerLastError,
       "nsVrBgpPeerFsmEstablishedTransitions": nsVrBgpPeerFsmEstablishedTransitions,
       "nsVrBgpPeerFsmEstablishedTime": nsVrBgpPeerFsmEstablishedTime,
       "nsVrBgpPeerConnectRetryInterval": nsVrBgpPeerConnectRetryInterval,
       "nsVrBgpPeerHoldTime": nsVrBgpPeerHoldTime,
       "nsVrBgpPeerKeepAlive": nsVrBgpPeerKeepAlive,
       "nsVrBgpPeerHoldTimeConfigured": nsVrBgpPeerHoldTimeConfigured,
       "nsVrBgpPeerKeepAliveConfigured": nsVrBgpPeerKeepAliveConfigured,
       "nsVrBgpPeerMinASOriginationInterval": nsVrBgpPeerMinASOriginationInterval,
       "nsVrBgpPeerMinRouteAdvertisementInterval": nsVrBgpPeerMinRouteAdvertisementInterval,
       "nsVrBgpPeerInUpdateElapsedTime": nsVrBgpPeerInUpdateElapsedTime,
       "nsVrBgpPeerVRID": nsVrBgpPeerVRID,
       "nsVrBgp4PathAttrTable": nsVrBgp4PathAttrTable,
       "nsVrBgp4PathAttrEntry": nsVrBgp4PathAttrEntry,
       "nsVrBgp4PathAttrPeer": nsVrBgp4PathAttrPeer,
       "nsVrBgp4PathAttrIpAddrPrefixLen": nsVrBgp4PathAttrIpAddrPrefixLen,
       "nsVrBgp4PathAttrIpAddrPrefix": nsVrBgp4PathAttrIpAddrPrefix,
       "nsVrBgp4PathAttrOrigin": nsVrBgp4PathAttrOrigin,
       "nsVrBgp4PathAttrASPathSegment": nsVrBgp4PathAttrASPathSegment,
       "nsVrBgp4PathAttrNextHop": nsVrBgp4PathAttrNextHop,
       "nsVrBgp4PathAttrMultiExitDisc": nsVrBgp4PathAttrMultiExitDisc,
       "nsVrBgp4PathAttrLocalPref": nsVrBgp4PathAttrLocalPref,
       "nsVrBgp4PathAttrAtomicAggregate": nsVrBgp4PathAttrAtomicAggregate,
       "nsVrBgp4PathAttrAggregatorAS": nsVrBgp4PathAttrAggregatorAS,
       "nsVrBgp4PathAttrAggregatorAddr": nsVrBgp4PathAttrAggregatorAddr,
       "nsVrBgp4PathAttrCalcLocalPref": nsVrBgp4PathAttrCalcLocalPref,
       "nsVrBgp4PathAttrBest": nsVrBgp4PathAttrBest,
       "nsVrBgp4PathAttrUnknown": nsVrBgp4PathAttrUnknown,
       "nsVrBgp4PathAttrVRID": nsVrBgp4PathAttrVRID,
       "nsVrBgpTraps": nsVrBgpTraps,
       "nsVrBgpEstablished": nsVrBgpEstablished}
)
