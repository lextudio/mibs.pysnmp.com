# SNMP MIB module (BGP4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BGP4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:53 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

bgp = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _BgpVersion_Type(OctetString):
    """Custom type bgpVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_BgpVersion_Type.__name__ = "OctetString"
_BgpVersion_Object = MibScalar
bgpVersion = _BgpVersion_Object(
    (1, 3, 6, 1, 2, 1, 15, 1),
    _BgpVersion_Type()
)
bgpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpVersion.setStatus("current")


class _BgpLocalAs_Type(Integer32):
    """Custom type bgpLocalAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BgpLocalAs_Type.__name__ = "Integer32"
_BgpLocalAs_Object = MibScalar
bgpLocalAs = _BgpLocalAs_Object(
    (1, 3, 6, 1, 2, 1, 15, 2),
    _BgpLocalAs_Type()
)
bgpLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpLocalAs.setStatus("current")
_BgpPeerTable_Object = MibTable
bgpPeerTable = _BgpPeerTable_Object(
    (1, 3, 6, 1, 2, 1, 15, 3)
)
if mibBuilder.loadTexts:
    bgpPeerTable.setStatus("current")
_BgpPeerEntry_Object = MibTableRow
bgpPeerEntry = _BgpPeerEntry_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1)
)
bgpPeerEntry.setIndexNames(
    (0, "BGP4-MIB", "bgpPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    bgpPeerEntry.setStatus("current")
_BgpPeerIdentifier_Type = IpAddress
_BgpPeerIdentifier_Object = MibTableColumn
bgpPeerIdentifier = _BgpPeerIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 1),
    _BgpPeerIdentifier_Type()
)
bgpPeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerIdentifier.setStatus("current")


class _BgpPeerState_Type(Integer32):
    """Custom type bgpPeerState based on Integer32"""
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


_BgpPeerState_Type.__name__ = "Integer32"
_BgpPeerState_Object = MibTableColumn
bgpPeerState = _BgpPeerState_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 2),
    _BgpPeerState_Type()
)
bgpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerState.setStatus("current")


class _BgpPeerAdminStatus_Type(Integer32):
    """Custom type bgpPeerAdminStatus based on Integer32"""
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


_BgpPeerAdminStatus_Type.__name__ = "Integer32"
_BgpPeerAdminStatus_Object = MibTableColumn
bgpPeerAdminStatus = _BgpPeerAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 3),
    _BgpPeerAdminStatus_Type()
)
bgpPeerAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerAdminStatus.setStatus("current")
_BgpPeerNegotiatedVersion_Type = Integer32
_BgpPeerNegotiatedVersion_Object = MibTableColumn
bgpPeerNegotiatedVersion = _BgpPeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 4),
    _BgpPeerNegotiatedVersion_Type()
)
bgpPeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerNegotiatedVersion.setStatus("current")
_BgpPeerLocalAddr_Type = IpAddress
_BgpPeerLocalAddr_Object = MibTableColumn
bgpPeerLocalAddr = _BgpPeerLocalAddr_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 5),
    _BgpPeerLocalAddr_Type()
)
bgpPeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLocalAddr.setStatus("current")


class _BgpPeerLocalPort_Type(Integer32):
    """Custom type bgpPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BgpPeerLocalPort_Type.__name__ = "Integer32"
_BgpPeerLocalPort_Object = MibTableColumn
bgpPeerLocalPort = _BgpPeerLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 6),
    _BgpPeerLocalPort_Type()
)
bgpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLocalPort.setStatus("current")
_BgpPeerRemoteAddr_Type = IpAddress
_BgpPeerRemoteAddr_Object = MibTableColumn
bgpPeerRemoteAddr = _BgpPeerRemoteAddr_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 7),
    _BgpPeerRemoteAddr_Type()
)
bgpPeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRemoteAddr.setStatus("current")


class _BgpPeerRemotePort_Type(Integer32):
    """Custom type bgpPeerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BgpPeerRemotePort_Type.__name__ = "Integer32"
_BgpPeerRemotePort_Object = MibTableColumn
bgpPeerRemotePort = _BgpPeerRemotePort_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 8),
    _BgpPeerRemotePort_Type()
)
bgpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRemotePort.setStatus("current")


class _BgpPeerRemoteAs_Type(Integer32):
    """Custom type bgpPeerRemoteAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BgpPeerRemoteAs_Type.__name__ = "Integer32"
_BgpPeerRemoteAs_Object = MibTableColumn
bgpPeerRemoteAs = _BgpPeerRemoteAs_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 9),
    _BgpPeerRemoteAs_Type()
)
bgpPeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRemoteAs.setStatus("current")
_BgpPeerInUpdates_Type = Counter32
_BgpPeerInUpdates_Object = MibTableColumn
bgpPeerInUpdates = _BgpPeerInUpdates_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 10),
    _BgpPeerInUpdates_Type()
)
bgpPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerInUpdates.setStatus("current")
_BgpPeerOutUpdates_Type = Counter32
_BgpPeerOutUpdates_Object = MibTableColumn
bgpPeerOutUpdates = _BgpPeerOutUpdates_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 11),
    _BgpPeerOutUpdates_Type()
)
bgpPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerOutUpdates.setStatus("current")
_BgpPeerInTotalMessages_Type = Counter32
_BgpPeerInTotalMessages_Object = MibTableColumn
bgpPeerInTotalMessages = _BgpPeerInTotalMessages_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 12),
    _BgpPeerInTotalMessages_Type()
)
bgpPeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerInTotalMessages.setStatus("current")
_BgpPeerOutTotalMessages_Type = Counter32
_BgpPeerOutTotalMessages_Object = MibTableColumn
bgpPeerOutTotalMessages = _BgpPeerOutTotalMessages_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 13),
    _BgpPeerOutTotalMessages_Type()
)
bgpPeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerOutTotalMessages.setStatus("current")


class _BgpPeerLastError_Type(OctetString):
    """Custom type bgpPeerLastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BgpPeerLastError_Type.__name__ = "OctetString"
_BgpPeerLastError_Object = MibTableColumn
bgpPeerLastError = _BgpPeerLastError_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 14),
    _BgpPeerLastError_Type()
)
bgpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLastError.setStatus("current")
_BgpPeerFsmEstablishedTransitions_Type = Counter32
_BgpPeerFsmEstablishedTransitions_Object = MibTableColumn
bgpPeerFsmEstablishedTransitions = _BgpPeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 15),
    _BgpPeerFsmEstablishedTransitions_Type()
)
bgpPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerFsmEstablishedTransitions.setStatus("current")
_BgpPeerFsmEstablishedTime_Type = Gauge32
_BgpPeerFsmEstablishedTime_Object = MibTableColumn
bgpPeerFsmEstablishedTime = _BgpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 16),
    _BgpPeerFsmEstablishedTime_Type()
)
bgpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerFsmEstablishedTime.setStatus("current")


class _BgpPeerConnectRetryInterval_Type(Integer32):
    """Custom type bgpPeerConnectRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BgpPeerConnectRetryInterval_Type.__name__ = "Integer32"
_BgpPeerConnectRetryInterval_Object = MibTableColumn
bgpPeerConnectRetryInterval = _BgpPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 17),
    _BgpPeerConnectRetryInterval_Type()
)
bgpPeerConnectRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerConnectRetryInterval.setStatus("current")


class _BgpPeerHoldTime_Type(Integer32):
    """Custom type bgpPeerHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_BgpPeerHoldTime_Type.__name__ = "Integer32"
_BgpPeerHoldTime_Object = MibTableColumn
bgpPeerHoldTime = _BgpPeerHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 18),
    _BgpPeerHoldTime_Type()
)
bgpPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerHoldTime.setStatus("current")


class _BgpPeerKeepAlive_Type(Integer32):
    """Custom type bgpPeerKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_BgpPeerKeepAlive_Type.__name__ = "Integer32"
_BgpPeerKeepAlive_Object = MibTableColumn
bgpPeerKeepAlive = _BgpPeerKeepAlive_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 19),
    _BgpPeerKeepAlive_Type()
)
bgpPeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerKeepAlive.setStatus("current")


class _BgpPeerHoldTimeConfigured_Type(Integer32):
    """Custom type bgpPeerHoldTimeConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_BgpPeerHoldTimeConfigured_Type.__name__ = "Integer32"
_BgpPeerHoldTimeConfigured_Object = MibTableColumn
bgpPeerHoldTimeConfigured = _BgpPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 20),
    _BgpPeerHoldTimeConfigured_Type()
)
bgpPeerHoldTimeConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerHoldTimeConfigured.setStatus("current")


class _BgpPeerKeepAliveConfigured_Type(Integer32):
    """Custom type bgpPeerKeepAliveConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_BgpPeerKeepAliveConfigured_Type.__name__ = "Integer32"
_BgpPeerKeepAliveConfigured_Object = MibTableColumn
bgpPeerKeepAliveConfigured = _BgpPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 21),
    _BgpPeerKeepAliveConfigured_Type()
)
bgpPeerKeepAliveConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerKeepAliveConfigured.setStatus("current")


class _BgpPeerMinASOriginationInterval_Type(Integer32):
    """Custom type bgpPeerMinASOriginationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BgpPeerMinASOriginationInterval_Type.__name__ = "Integer32"
_BgpPeerMinASOriginationInterval_Object = MibTableColumn
bgpPeerMinASOriginationInterval = _BgpPeerMinASOriginationInterval_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 22),
    _BgpPeerMinASOriginationInterval_Type()
)
bgpPeerMinASOriginationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerMinASOriginationInterval.setStatus("current")


class _BgpPeerMinRouteAdvertisementInterval_Type(Integer32):
    """Custom type bgpPeerMinRouteAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BgpPeerMinRouteAdvertisementInterval_Type.__name__ = "Integer32"
_BgpPeerMinRouteAdvertisementInterval_Object = MibTableColumn
bgpPeerMinRouteAdvertisementInterval = _BgpPeerMinRouteAdvertisementInterval_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 23),
    _BgpPeerMinRouteAdvertisementInterval_Type()
)
bgpPeerMinRouteAdvertisementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerMinRouteAdvertisementInterval.setStatus("current")
_BgpPeerInUpdateElapsedTime_Type = Gauge32
_BgpPeerInUpdateElapsedTime_Object = MibTableColumn
bgpPeerInUpdateElapsedTime = _BgpPeerInUpdateElapsedTime_Object(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 24),
    _BgpPeerInUpdateElapsedTime_Type()
)
bgpPeerInUpdateElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerInUpdateElapsedTime.setStatus("current")
_BgpIdentifier_Type = IpAddress
_BgpIdentifier_Object = MibScalar
bgpIdentifier = _BgpIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 15, 4),
    _BgpIdentifier_Type()
)
bgpIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpIdentifier.setStatus("current")
_Bgp4PathAttrTable_Object = MibTable
bgp4PathAttrTable = _Bgp4PathAttrTable_Object(
    (1, 3, 6, 1, 2, 1, 15, 6)
)
if mibBuilder.loadTexts:
    bgp4PathAttrTable.setStatus("current")
_Bgp4PathAttrEntry_Object = MibTableRow
bgp4PathAttrEntry = _Bgp4PathAttrEntry_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1)
)
bgp4PathAttrEntry.setIndexNames(
    (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefix"),
    (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefixLen"),
    (0, "BGP4-MIB", "bgp4PathAttrPeer"),
)
if mibBuilder.loadTexts:
    bgp4PathAttrEntry.setStatus("current")
_Bgp4PathAttrPeer_Type = IpAddress
_Bgp4PathAttrPeer_Object = MibTableColumn
bgp4PathAttrPeer = _Bgp4PathAttrPeer_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1, 1),
    _Bgp4PathAttrPeer_Type()
)
bgp4PathAttrPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathAttrPeer.setStatus("current")


class _Bgp4PathAttrIpAddrPrefixLen_Type(Integer32):
    """Custom type bgp4PathAttrIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Bgp4PathAttrIpAddrPrefixLen_Type.__name__ = "Integer32"
_Bgp4PathAttrIpAddrPrefixLen_Object = MibTableColumn
bgp4PathAttrIpAddrPrefixLen = _Bgp4PathAttrIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1, 2),
    _Bgp4PathAttrIpAddrPrefixLen_Type()
)
bgp4PathAttrIpAddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathAttrIpAddrPrefixLen.setStatus("current")
_Bgp4PathAttrIpAddrPrefix_Type = IpAddress
_Bgp4PathAttrIpAddrPrefix_Object = MibTableColumn
bgp4PathAttrIpAddrPrefix = _Bgp4PathAttrIpAddrPrefix_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1, 3),
    _Bgp4PathAttrIpAddrPrefix_Type()
)
bgp4PathAttrIpAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathAttrIpAddrPrefix.setStatus("current")


class _Bgp4PathAttrOrigin_Type(Integer32):
    """Custom type bgp4PathAttrOrigin based on Integer32"""
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


_Bgp4PathAttrOrigin_Type.__name__ = "Integer32"
_Bgp4PathAttrOrigin_Object = MibTableColumn
bgp4PathAttrOrigin = _Bgp4PathAttrOrigin_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1, 4),
    _Bgp4PathAttrOrigin_Type()
)
bgp4PathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathAttrOrigin.setStatus("current")


class _Bgp4PathAttrASPathSegment_Type(OctetString):
    """Custom type bgp4PathAttrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_Bgp4PathAttrASPathSegment_Type.__name__ = "OctetString"
_Bgp4PathAttrASPathSegment_Object = MibTableColumn
bgp4PathAttrASPathSegment = _Bgp4PathAttrASPathSegment_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1, 5),
    _Bgp4PathAttrASPathSegment_Type()
)
bgp4PathAttrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathAttrASPathSegment.setStatus("current")
_Bgp4PathAttrNextHop_Type = IpAddress
_Bgp4PathAttrNextHop_Object = MibTableColumn
bgp4PathAttrNextHop = _Bgp4PathAttrNextHop_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1, 6),
    _Bgp4PathAttrNextHop_Type()
)
bgp4PathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathAttrNextHop.setStatus("current")


class _Bgp4PathAttrMultiExitDisc_Type(Integer32):
    """Custom type bgp4PathAttrMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Bgp4PathAttrMultiExitDisc_Type.__name__ = "Integer32"
_Bgp4PathAttrMultiExitDisc_Object = MibTableColumn
bgp4PathAttrMultiExitDisc = _Bgp4PathAttrMultiExitDisc_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1, 7),
    _Bgp4PathAttrMultiExitDisc_Type()
)
bgp4PathAttrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathAttrMultiExitDisc.setStatus("current")


class _Bgp4PathAttrLocalPref_Type(Integer32):
    """Custom type bgp4PathAttrLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Bgp4PathAttrLocalPref_Type.__name__ = "Integer32"
_Bgp4PathAttrLocalPref_Object = MibTableColumn
bgp4PathAttrLocalPref = _Bgp4PathAttrLocalPref_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1, 8),
    _Bgp4PathAttrLocalPref_Type()
)
bgp4PathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathAttrLocalPref.setStatus("current")


class _Bgp4PathAttrAtomicAggregate_Type(Integer32):
    """Custom type bgp4PathAttrAtomicAggregate based on Integer32"""
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


_Bgp4PathAttrAtomicAggregate_Type.__name__ = "Integer32"
_Bgp4PathAttrAtomicAggregate_Object = MibTableColumn
bgp4PathAttrAtomicAggregate = _Bgp4PathAttrAtomicAggregate_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1, 9),
    _Bgp4PathAttrAtomicAggregate_Type()
)
bgp4PathAttrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathAttrAtomicAggregate.setStatus("current")


class _Bgp4PathAttrAggregatorAS_Type(Integer32):
    """Custom type bgp4PathAttrAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Bgp4PathAttrAggregatorAS_Type.__name__ = "Integer32"
_Bgp4PathAttrAggregatorAS_Object = MibTableColumn
bgp4PathAttrAggregatorAS = _Bgp4PathAttrAggregatorAS_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1, 10),
    _Bgp4PathAttrAggregatorAS_Type()
)
bgp4PathAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathAttrAggregatorAS.setStatus("current")
_Bgp4PathAttrAggregatorAddr_Type = IpAddress
_Bgp4PathAttrAggregatorAddr_Object = MibTableColumn
bgp4PathAttrAggregatorAddr = _Bgp4PathAttrAggregatorAddr_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1, 11),
    _Bgp4PathAttrAggregatorAddr_Type()
)
bgp4PathAttrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathAttrAggregatorAddr.setStatus("current")


class _Bgp4PathAttrCalcLocalPref_Type(Integer32):
    """Custom type bgp4PathAttrCalcLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Bgp4PathAttrCalcLocalPref_Type.__name__ = "Integer32"
_Bgp4PathAttrCalcLocalPref_Object = MibTableColumn
bgp4PathAttrCalcLocalPref = _Bgp4PathAttrCalcLocalPref_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1, 12),
    _Bgp4PathAttrCalcLocalPref_Type()
)
bgp4PathAttrCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathAttrCalcLocalPref.setStatus("current")


class _Bgp4PathAttrBest_Type(Integer32):
    """Custom type bgp4PathAttrBest based on Integer32"""
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


_Bgp4PathAttrBest_Type.__name__ = "Integer32"
_Bgp4PathAttrBest_Object = MibTableColumn
bgp4PathAttrBest = _Bgp4PathAttrBest_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1, 13),
    _Bgp4PathAttrBest_Type()
)
bgp4PathAttrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathAttrBest.setStatus("current")


class _Bgp4PathAttrUnknown_Type(OctetString):
    """Custom type bgp4PathAttrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Bgp4PathAttrUnknown_Type.__name__ = "OctetString"
_Bgp4PathAttrUnknown_Object = MibTableColumn
bgp4PathAttrUnknown = _Bgp4PathAttrUnknown_Object(
    (1, 3, 6, 1, 2, 1, 15, 6, 1, 14),
    _Bgp4PathAttrUnknown_Type()
)
bgp4PathAttrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4PathAttrUnknown.setStatus("current")
_BgpTraps_ObjectIdentity = ObjectIdentity
bgpTraps = _BgpTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 15, 7)
)

# Managed Objects groups


# Notification objects

bgpEstablished = NotificationType(
    (1, 3, 6, 1, 2, 1, 15, 7, 1)
)
bgpEstablished.setObjects(
      *(("BGP4-MIB", "bgpPeerLastError"),
        ("BGP4-MIB", "bgpPeerState"))
)
if mibBuilder.loadTexts:
    bgpEstablished.setStatus(
        "current"
    )

bgpBackwardTransition = NotificationType(
    (1, 3, 6, 1, 2, 1, 15, 7, 2)
)
bgpBackwardTransition.setObjects(
      *(("BGP4-MIB", "bgpPeerLastError"),
        ("BGP4-MIB", "bgpPeerState"))
)
if mibBuilder.loadTexts:
    bgpBackwardTransition.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BGP4-MIB",
    **{"bgp": bgp,
       "bgpVersion": bgpVersion,
       "bgpLocalAs": bgpLocalAs,
       "bgpPeerTable": bgpPeerTable,
       "bgpPeerEntry": bgpPeerEntry,
       "bgpPeerIdentifier": bgpPeerIdentifier,
       "bgpPeerState": bgpPeerState,
       "bgpPeerAdminStatus": bgpPeerAdminStatus,
       "bgpPeerNegotiatedVersion": bgpPeerNegotiatedVersion,
       "bgpPeerLocalAddr": bgpPeerLocalAddr,
       "bgpPeerLocalPort": bgpPeerLocalPort,
       "bgpPeerRemoteAddr": bgpPeerRemoteAddr,
       "bgpPeerRemotePort": bgpPeerRemotePort,
       "bgpPeerRemoteAs": bgpPeerRemoteAs,
       "bgpPeerInUpdates": bgpPeerInUpdates,
       "bgpPeerOutUpdates": bgpPeerOutUpdates,
       "bgpPeerInTotalMessages": bgpPeerInTotalMessages,
       "bgpPeerOutTotalMessages": bgpPeerOutTotalMessages,
       "bgpPeerLastError": bgpPeerLastError,
       "bgpPeerFsmEstablishedTransitions": bgpPeerFsmEstablishedTransitions,
       "bgpPeerFsmEstablishedTime": bgpPeerFsmEstablishedTime,
       "bgpPeerConnectRetryInterval": bgpPeerConnectRetryInterval,
       "bgpPeerHoldTime": bgpPeerHoldTime,
       "bgpPeerKeepAlive": bgpPeerKeepAlive,
       "bgpPeerHoldTimeConfigured": bgpPeerHoldTimeConfigured,
       "bgpPeerKeepAliveConfigured": bgpPeerKeepAliveConfigured,
       "bgpPeerMinASOriginationInterval": bgpPeerMinASOriginationInterval,
       "bgpPeerMinRouteAdvertisementInterval": bgpPeerMinRouteAdvertisementInterval,
       "bgpPeerInUpdateElapsedTime": bgpPeerInUpdateElapsedTime,
       "bgpIdentifier": bgpIdentifier,
       "bgp4PathAttrTable": bgp4PathAttrTable,
       "bgp4PathAttrEntry": bgp4PathAttrEntry,
       "bgp4PathAttrPeer": bgp4PathAttrPeer,
       "bgp4PathAttrIpAddrPrefixLen": bgp4PathAttrIpAddrPrefixLen,
       "bgp4PathAttrIpAddrPrefix": bgp4PathAttrIpAddrPrefix,
       "bgp4PathAttrOrigin": bgp4PathAttrOrigin,
       "bgp4PathAttrASPathSegment": bgp4PathAttrASPathSegment,
       "bgp4PathAttrNextHop": bgp4PathAttrNextHop,
       "bgp4PathAttrMultiExitDisc": bgp4PathAttrMultiExitDisc,
       "bgp4PathAttrLocalPref": bgp4PathAttrLocalPref,
       "bgp4PathAttrAtomicAggregate": bgp4PathAttrAtomicAggregate,
       "bgp4PathAttrAggregatorAS": bgp4PathAttrAggregatorAS,
       "bgp4PathAttrAggregatorAddr": bgp4PathAttrAggregatorAddr,
       "bgp4PathAttrCalcLocalPref": bgp4PathAttrCalcLocalPref,
       "bgp4PathAttrBest": bgp4PathAttrBest,
       "bgp4PathAttrUnknown": bgp4PathAttrUnknown,
       "bgpTraps": bgpTraps,
       "bgpEstablished": bgpEstablished,
       "bgpBackwardTransition": bgpBackwardTransition}
)
