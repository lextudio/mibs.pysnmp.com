# SNMP MIB module (CISCO-BGP4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BGP4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:18 2024
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

(bgpPeerEntry,
 bgpPeerLastError,
 bgpPeerRemoteAddr,
 bgpPeerState) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgpPeerEntry",
    "bgpPeerLastError",
    "bgpPeerRemoteAddr",
    "bgpPeerState")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetAutonomousSystemNumber,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetAutonomousSystemNumber",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoBgp4MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 187)
)
ciscoBgp4MIB.setRevisions(
        ("2010-09-30 00:00",
         "2003-02-24 00:00",
         "2002-12-19 00:00",
         "2001-08-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CbgpSafi(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              128)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 2),
          ("unicast", 1),
          ("unicastAndMulticast", 3),
          ("vpn", 128))
    )



class CbgpNetworkAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoBgp4NotifyPrefix_ObjectIdentity = ObjectIdentity
ciscoBgp4NotifyPrefix = _CiscoBgp4NotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 0)
)
_CiscoBgp4MIBObjects_ObjectIdentity = ObjectIdentity
ciscoBgp4MIBObjects = _CiscoBgp4MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1)
)
_CbgpRoute_ObjectIdentity = ObjectIdentity
cbgpRoute = _CbgpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1)
)
_CbgpRouteTable_Object = MibTable
cbgpRouteTable = _CbgpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cbgpRouteTable.setStatus("current")
_CbgpRouteEntry_Object = MibTableRow
cbgpRouteEntry = _CbgpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1)
)
cbgpRouteEntry.setIndexNames(
    (0, "CISCO-BGP4-MIB", "cbgpRouteAfi"),
    (0, "CISCO-BGP4-MIB", "cbgpRouteSafi"),
    (0, "CISCO-BGP4-MIB", "cbgpRoutePeerType"),
    (0, "CISCO-BGP4-MIB", "cbgpRoutePeer"),
    (0, "CISCO-BGP4-MIB", "cbgpRouteAddrPrefix"),
    (0, "CISCO-BGP4-MIB", "cbgpRouteAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    cbgpRouteEntry.setStatus("current")
_CbgpRouteAfi_Type = InetAddressType
_CbgpRouteAfi_Object = MibTableColumn
cbgpRouteAfi = _CbgpRouteAfi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 1),
    _CbgpRouteAfi_Type()
)
cbgpRouteAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpRouteAfi.setStatus("current")
_CbgpRouteSafi_Type = CbgpSafi
_CbgpRouteSafi_Object = MibTableColumn
cbgpRouteSafi = _CbgpRouteSafi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 2),
    _CbgpRouteSafi_Type()
)
cbgpRouteSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpRouteSafi.setStatus("current")
_CbgpRoutePeerType_Type = InetAddressType
_CbgpRoutePeerType_Object = MibTableColumn
cbgpRoutePeerType = _CbgpRoutePeerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 3),
    _CbgpRoutePeerType_Type()
)
cbgpRoutePeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpRoutePeerType.setStatus("current")
_CbgpRoutePeer_Type = InetAddress
_CbgpRoutePeer_Object = MibTableColumn
cbgpRoutePeer = _CbgpRoutePeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 4),
    _CbgpRoutePeer_Type()
)
cbgpRoutePeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpRoutePeer.setStatus("current")
_CbgpRouteAddrPrefix_Type = CbgpNetworkAddress
_CbgpRouteAddrPrefix_Object = MibTableColumn
cbgpRouteAddrPrefix = _CbgpRouteAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 5),
    _CbgpRouteAddrPrefix_Type()
)
cbgpRouteAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpRouteAddrPrefix.setStatus("current")


class _CbgpRouteAddrPrefixLen_Type(Unsigned32):
    """Custom type cbgpRouteAddrPrefixLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2040),
    )


_CbgpRouteAddrPrefixLen_Type.__name__ = "Unsigned32"
_CbgpRouteAddrPrefixLen_Object = MibTableColumn
cbgpRouteAddrPrefixLen = _CbgpRouteAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 6),
    _CbgpRouteAddrPrefixLen_Type()
)
cbgpRouteAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpRouteAddrPrefixLen.setStatus("current")


class _CbgpRouteOrigin_Type(Integer32):
    """Custom type cbgpRouteOrigin based on Integer32"""
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


_CbgpRouteOrigin_Type.__name__ = "Integer32"
_CbgpRouteOrigin_Object = MibTableColumn
cbgpRouteOrigin = _CbgpRouteOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 7),
    _CbgpRouteOrigin_Type()
)
cbgpRouteOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpRouteOrigin.setStatus("current")


class _CbgpRouteASPathSegment_Type(OctetString):
    """Custom type cbgpRouteASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CbgpRouteASPathSegment_Type.__name__ = "OctetString"
_CbgpRouteASPathSegment_Object = MibTableColumn
cbgpRouteASPathSegment = _CbgpRouteASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 8),
    _CbgpRouteASPathSegment_Type()
)
cbgpRouteASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpRouteASPathSegment.setStatus("current")
_CbgpRouteNextHop_Type = CbgpNetworkAddress
_CbgpRouteNextHop_Object = MibTableColumn
cbgpRouteNextHop = _CbgpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 9),
    _CbgpRouteNextHop_Type()
)
cbgpRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpRouteNextHop.setStatus("current")
_CbgpRouteMedPresent_Type = TruthValue
_CbgpRouteMedPresent_Object = MibTableColumn
cbgpRouteMedPresent = _CbgpRouteMedPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 10),
    _CbgpRouteMedPresent_Type()
)
cbgpRouteMedPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpRouteMedPresent.setStatus("current")


class _CbgpRouteMultiExitDisc_Type(Unsigned32):
    """Custom type cbgpRouteMultiExitDisc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CbgpRouteMultiExitDisc_Type.__name__ = "Unsigned32"
_CbgpRouteMultiExitDisc_Object = MibTableColumn
cbgpRouteMultiExitDisc = _CbgpRouteMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 11),
    _CbgpRouteMultiExitDisc_Type()
)
cbgpRouteMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpRouteMultiExitDisc.setStatus("current")
_CbgpRouteLocalPrefPresent_Type = TruthValue
_CbgpRouteLocalPrefPresent_Object = MibTableColumn
cbgpRouteLocalPrefPresent = _CbgpRouteLocalPrefPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 12),
    _CbgpRouteLocalPrefPresent_Type()
)
cbgpRouteLocalPrefPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpRouteLocalPrefPresent.setStatus("current")


class _CbgpRouteLocalPref_Type(Unsigned32):
    """Custom type cbgpRouteLocalPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CbgpRouteLocalPref_Type.__name__ = "Unsigned32"
_CbgpRouteLocalPref_Object = MibTableColumn
cbgpRouteLocalPref = _CbgpRouteLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 13),
    _CbgpRouteLocalPref_Type()
)
cbgpRouteLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpRouteLocalPref.setStatus("current")


class _CbgpRouteAtomicAggregate_Type(Integer32):
    """Custom type cbgpRouteAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessSpecificRouteNotSelected", 1),
          ("lessSpecificRouteSelected", 2))
    )


_CbgpRouteAtomicAggregate_Type.__name__ = "Integer32"
_CbgpRouteAtomicAggregate_Object = MibTableColumn
cbgpRouteAtomicAggregate = _CbgpRouteAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 14),
    _CbgpRouteAtomicAggregate_Type()
)
cbgpRouteAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpRouteAtomicAggregate.setStatus("current")


class _CbgpRouteAggregatorAS_Type(Unsigned32):
    """Custom type cbgpRouteAggregatorAS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CbgpRouteAggregatorAS_Type.__name__ = "Unsigned32"
_CbgpRouteAggregatorAS_Object = MibTableColumn
cbgpRouteAggregatorAS = _CbgpRouteAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 15),
    _CbgpRouteAggregatorAS_Type()
)
cbgpRouteAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpRouteAggregatorAS.setStatus("current")
_CbgpRouteAggregatorAddrType_Type = InetAddressType
_CbgpRouteAggregatorAddrType_Object = MibTableColumn
cbgpRouteAggregatorAddrType = _CbgpRouteAggregatorAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 16),
    _CbgpRouteAggregatorAddrType_Type()
)
cbgpRouteAggregatorAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpRouteAggregatorAddrType.setStatus("current")
_CbgpRouteAggregatorAddr_Type = InetAddress
_CbgpRouteAggregatorAddr_Object = MibTableColumn
cbgpRouteAggregatorAddr = _CbgpRouteAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 17),
    _CbgpRouteAggregatorAddr_Type()
)
cbgpRouteAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpRouteAggregatorAddr.setStatus("current")
_CbgpRouteBest_Type = TruthValue
_CbgpRouteBest_Object = MibTableColumn
cbgpRouteBest = _CbgpRouteBest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 18),
    _CbgpRouteBest_Type()
)
cbgpRouteBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpRouteBest.setStatus("current")


class _CbgpRouteUnknownAttr_Type(OctetString):
    """Custom type cbgpRouteUnknownAttr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CbgpRouteUnknownAttr_Type.__name__ = "OctetString"
_CbgpRouteUnknownAttr_Object = MibTableColumn
cbgpRouteUnknownAttr = _CbgpRouteUnknownAttr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 1, 1, 1, 19),
    _CbgpRouteUnknownAttr_Type()
)
cbgpRouteUnknownAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpRouteUnknownAttr.setStatus("current")
_CbgpPeer_ObjectIdentity = ObjectIdentity
cbgpPeer = _CbgpPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2)
)
_CbgpPeerTable_Object = MibTable
cbgpPeerTable = _CbgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cbgpPeerTable.setStatus("current")
_CbgpPeerEntry_Object = MibTableRow
cbgpPeerEntry = _CbgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cbgpPeerEntry.setStatus("current")
_CbgpPeerPrefixAccepted_Type = Counter32
_CbgpPeerPrefixAccepted_Object = MibTableColumn
cbgpPeerPrefixAccepted = _CbgpPeerPrefixAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 1, 1, 1),
    _CbgpPeerPrefixAccepted_Type()
)
cbgpPeerPrefixAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerPrefixAccepted.setStatus("deprecated")
_CbgpPeerPrefixDenied_Type = Counter32
_CbgpPeerPrefixDenied_Object = MibTableColumn
cbgpPeerPrefixDenied = _CbgpPeerPrefixDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 1, 1, 2),
    _CbgpPeerPrefixDenied_Type()
)
cbgpPeerPrefixDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerPrefixDenied.setStatus("deprecated")


class _CbgpPeerPrefixLimit_Type(Unsigned32):
    """Custom type cbgpPeerPrefixLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CbgpPeerPrefixLimit_Type.__name__ = "Unsigned32"
_CbgpPeerPrefixLimit_Object = MibTableColumn
cbgpPeerPrefixLimit = _CbgpPeerPrefixLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 1, 1, 3),
    _CbgpPeerPrefixLimit_Type()
)
cbgpPeerPrefixLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbgpPeerPrefixLimit.setStatus("deprecated")
_CbgpPeerPrefixAdvertised_Type = Counter32
_CbgpPeerPrefixAdvertised_Object = MibTableColumn
cbgpPeerPrefixAdvertised = _CbgpPeerPrefixAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 1, 1, 4),
    _CbgpPeerPrefixAdvertised_Type()
)
cbgpPeerPrefixAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerPrefixAdvertised.setStatus("deprecated")
_CbgpPeerPrefixSuppressed_Type = Counter32
_CbgpPeerPrefixSuppressed_Object = MibTableColumn
cbgpPeerPrefixSuppressed = _CbgpPeerPrefixSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 1, 1, 5),
    _CbgpPeerPrefixSuppressed_Type()
)
cbgpPeerPrefixSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerPrefixSuppressed.setStatus("deprecated")
_CbgpPeerPrefixWithdrawn_Type = Counter32
_CbgpPeerPrefixWithdrawn_Object = MibTableColumn
cbgpPeerPrefixWithdrawn = _CbgpPeerPrefixWithdrawn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 1, 1, 6),
    _CbgpPeerPrefixWithdrawn_Type()
)
cbgpPeerPrefixWithdrawn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerPrefixWithdrawn.setStatus("deprecated")
_CbgpPeerLastErrorTxt_Type = SnmpAdminString
_CbgpPeerLastErrorTxt_Object = MibTableColumn
cbgpPeerLastErrorTxt = _CbgpPeerLastErrorTxt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 1, 1, 7),
    _CbgpPeerLastErrorTxt_Type()
)
cbgpPeerLastErrorTxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerLastErrorTxt.setStatus("current")


class _CbgpPeerPrevState_Type(Integer32):
    """Custom type cbgpPeerPrevState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
          ("none", 0),
          ("openconfirm", 5),
          ("opensent", 4))
    )


_CbgpPeerPrevState_Type.__name__ = "Integer32"
_CbgpPeerPrevState_Object = MibTableColumn
cbgpPeerPrevState = _CbgpPeerPrevState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 1, 1, 8),
    _CbgpPeerPrevState_Type()
)
cbgpPeerPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerPrevState.setStatus("current")
_CbgpPeerCapsTable_Object = MibTable
cbgpPeerCapsTable = _CbgpPeerCapsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cbgpPeerCapsTable.setStatus("current")
_CbgpPeerCapsEntry_Object = MibTableRow
cbgpPeerCapsEntry = _CbgpPeerCapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 2, 1)
)
cbgpPeerCapsEntry.setIndexNames(
    (0, "BGP4-MIB", "bgpPeerRemoteAddr"),
    (0, "CISCO-BGP4-MIB", "cbgpPeerCapCode"),
    (0, "CISCO-BGP4-MIB", "cbgpPeerCapIndex"),
)
if mibBuilder.loadTexts:
    cbgpPeerCapsEntry.setStatus("current")


class _CbgpPeerCapCode_Type(Integer32):
    """Custom type cbgpPeerCapCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("gracefulRestart", 64),
          ("multiProtocol", 1),
          ("routeRefresh", 2),
          ("routeRefreshOld", 128))
    )


_CbgpPeerCapCode_Type.__name__ = "Integer32"
_CbgpPeerCapCode_Object = MibTableColumn
cbgpPeerCapCode = _CbgpPeerCapCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 2, 1, 1),
    _CbgpPeerCapCode_Type()
)
cbgpPeerCapCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpPeerCapCode.setStatus("current")


class _CbgpPeerCapIndex_Type(Unsigned32):
    """Custom type cbgpPeerCapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CbgpPeerCapIndex_Type.__name__ = "Unsigned32"
_CbgpPeerCapIndex_Object = MibTableColumn
cbgpPeerCapIndex = _CbgpPeerCapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 2, 1, 2),
    _CbgpPeerCapIndex_Type()
)
cbgpPeerCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpPeerCapIndex.setStatus("current")


class _CbgpPeerCapValue_Type(OctetString):
    """Custom type cbgpPeerCapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CbgpPeerCapValue_Type.__name__ = "OctetString"
_CbgpPeerCapValue_Object = MibTableColumn
cbgpPeerCapValue = _CbgpPeerCapValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 2, 1, 3),
    _CbgpPeerCapValue_Type()
)
cbgpPeerCapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerCapValue.setStatus("current")
_CbgpPeerAddrFamilyTable_Object = MibTable
cbgpPeerAddrFamilyTable = _CbgpPeerAddrFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cbgpPeerAddrFamilyTable.setStatus("current")
_CbgpPeerAddrFamilyEntry_Object = MibTableRow
cbgpPeerAddrFamilyEntry = _CbgpPeerAddrFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 3, 1)
)
cbgpPeerAddrFamilyEntry.setIndexNames(
    (0, "BGP4-MIB", "bgpPeerRemoteAddr"),
    (0, "CISCO-BGP4-MIB", "cbgpPeerAddrFamilyAfi"),
    (0, "CISCO-BGP4-MIB", "cbgpPeerAddrFamilySafi"),
)
if mibBuilder.loadTexts:
    cbgpPeerAddrFamilyEntry.setStatus("current")
_CbgpPeerAddrFamilyAfi_Type = InetAddressType
_CbgpPeerAddrFamilyAfi_Object = MibTableColumn
cbgpPeerAddrFamilyAfi = _CbgpPeerAddrFamilyAfi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 3, 1, 1),
    _CbgpPeerAddrFamilyAfi_Type()
)
cbgpPeerAddrFamilyAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpPeerAddrFamilyAfi.setStatus("current")
_CbgpPeerAddrFamilySafi_Type = CbgpSafi
_CbgpPeerAddrFamilySafi_Object = MibTableColumn
cbgpPeerAddrFamilySafi = _CbgpPeerAddrFamilySafi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 3, 1, 2),
    _CbgpPeerAddrFamilySafi_Type()
)
cbgpPeerAddrFamilySafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpPeerAddrFamilySafi.setStatus("current")
_CbgpPeerAddrFamilyName_Type = SnmpAdminString
_CbgpPeerAddrFamilyName_Object = MibTableColumn
cbgpPeerAddrFamilyName = _CbgpPeerAddrFamilyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 3, 1, 3),
    _CbgpPeerAddrFamilyName_Type()
)
cbgpPeerAddrFamilyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerAddrFamilyName.setStatus("current")
_CbgpPeerAddrFamilyPrefixTable_Object = MibTable
cbgpPeerAddrFamilyPrefixTable = _CbgpPeerAddrFamilyPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cbgpPeerAddrFamilyPrefixTable.setStatus("current")
_CbgpPeerAddrFamilyPrefixEntry_Object = MibTableRow
cbgpPeerAddrFamilyPrefixEntry = _CbgpPeerAddrFamilyPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 4, 1)
)
cbgpPeerAddrFamilyPrefixEntry.setIndexNames(
    (0, "BGP4-MIB", "bgpPeerRemoteAddr"),
    (0, "CISCO-BGP4-MIB", "cbgpPeerAddrFamilyAfi"),
    (0, "CISCO-BGP4-MIB", "cbgpPeerAddrFamilySafi"),
)
if mibBuilder.loadTexts:
    cbgpPeerAddrFamilyPrefixEntry.setStatus("current")
_CbgpPeerAcceptedPrefixes_Type = Counter32
_CbgpPeerAcceptedPrefixes_Object = MibTableColumn
cbgpPeerAcceptedPrefixes = _CbgpPeerAcceptedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 4, 1, 1),
    _CbgpPeerAcceptedPrefixes_Type()
)
cbgpPeerAcceptedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerAcceptedPrefixes.setStatus("current")
_CbgpPeerDeniedPrefixes_Type = Gauge32
_CbgpPeerDeniedPrefixes_Object = MibTableColumn
cbgpPeerDeniedPrefixes = _CbgpPeerDeniedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 4, 1, 2),
    _CbgpPeerDeniedPrefixes_Type()
)
cbgpPeerDeniedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerDeniedPrefixes.setStatus("current")


class _CbgpPeerPrefixAdminLimit_Type(Unsigned32):
    """Custom type cbgpPeerPrefixAdminLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CbgpPeerPrefixAdminLimit_Type.__name__ = "Unsigned32"
_CbgpPeerPrefixAdminLimit_Object = MibTableColumn
cbgpPeerPrefixAdminLimit = _CbgpPeerPrefixAdminLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 4, 1, 3),
    _CbgpPeerPrefixAdminLimit_Type()
)
cbgpPeerPrefixAdminLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbgpPeerPrefixAdminLimit.setStatus("current")


class _CbgpPeerPrefixThreshold_Type(Unsigned32):
    """Custom type cbgpPeerPrefixThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CbgpPeerPrefixThreshold_Type.__name__ = "Unsigned32"
_CbgpPeerPrefixThreshold_Object = MibTableColumn
cbgpPeerPrefixThreshold = _CbgpPeerPrefixThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 4, 1, 4),
    _CbgpPeerPrefixThreshold_Type()
)
cbgpPeerPrefixThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbgpPeerPrefixThreshold.setStatus("current")


class _CbgpPeerPrefixClearThreshold_Type(Unsigned32):
    """Custom type cbgpPeerPrefixClearThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CbgpPeerPrefixClearThreshold_Type.__name__ = "Unsigned32"
_CbgpPeerPrefixClearThreshold_Object = MibTableColumn
cbgpPeerPrefixClearThreshold = _CbgpPeerPrefixClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 4, 1, 5),
    _CbgpPeerPrefixClearThreshold_Type()
)
cbgpPeerPrefixClearThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerPrefixClearThreshold.setStatus("current")
_CbgpPeerAdvertisedPrefixes_Type = Gauge32
_CbgpPeerAdvertisedPrefixes_Object = MibTableColumn
cbgpPeerAdvertisedPrefixes = _CbgpPeerAdvertisedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 4, 1, 6),
    _CbgpPeerAdvertisedPrefixes_Type()
)
cbgpPeerAdvertisedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerAdvertisedPrefixes.setStatus("current")
_CbgpPeerSuppressedPrefixes_Type = Gauge32
_CbgpPeerSuppressedPrefixes_Object = MibTableColumn
cbgpPeerSuppressedPrefixes = _CbgpPeerSuppressedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 4, 1, 7),
    _CbgpPeerSuppressedPrefixes_Type()
)
cbgpPeerSuppressedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerSuppressedPrefixes.setStatus("current")
_CbgpPeerWithdrawnPrefixes_Type = Gauge32
_CbgpPeerWithdrawnPrefixes_Object = MibTableColumn
cbgpPeerWithdrawnPrefixes = _CbgpPeerWithdrawnPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 4, 1, 8),
    _CbgpPeerWithdrawnPrefixes_Type()
)
cbgpPeerWithdrawnPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeerWithdrawnPrefixes.setStatus("current")
_CbgpPeer2Table_Object = MibTable
cbgpPeer2Table = _CbgpPeer2Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cbgpPeer2Table.setStatus("current")
_CbgpPeer2Entry_Object = MibTableRow
cbgpPeer2Entry = _CbgpPeer2Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1)
)
cbgpPeer2Entry.setIndexNames(
    (0, "CISCO-BGP4-MIB", "cbgpPeer2Type"),
    (0, "CISCO-BGP4-MIB", "cbgpPeer2RemoteAddr"),
)
if mibBuilder.loadTexts:
    cbgpPeer2Entry.setStatus("current")
_CbgpPeer2Type_Type = InetAddressType
_CbgpPeer2Type_Object = MibTableColumn
cbgpPeer2Type = _CbgpPeer2Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 1),
    _CbgpPeer2Type_Type()
)
cbgpPeer2Type.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpPeer2Type.setStatus("current")
_CbgpPeer2RemoteAddr_Type = InetAddress
_CbgpPeer2RemoteAddr_Object = MibTableColumn
cbgpPeer2RemoteAddr = _CbgpPeer2RemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 2),
    _CbgpPeer2RemoteAddr_Type()
)
cbgpPeer2RemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpPeer2RemoteAddr.setStatus("current")


class _CbgpPeer2State_Type(Integer32):
    """Custom type cbgpPeer2State based on Integer32"""
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


_CbgpPeer2State_Type.__name__ = "Integer32"
_CbgpPeer2State_Object = MibTableColumn
cbgpPeer2State = _CbgpPeer2State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 3),
    _CbgpPeer2State_Type()
)
cbgpPeer2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2State.setStatus("current")


class _CbgpPeer2AdminStatus_Type(Integer32):
    """Custom type cbgpPeer2AdminStatus based on Integer32"""
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


_CbgpPeer2AdminStatus_Type.__name__ = "Integer32"
_CbgpPeer2AdminStatus_Object = MibTableColumn
cbgpPeer2AdminStatus = _CbgpPeer2AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 4),
    _CbgpPeer2AdminStatus_Type()
)
cbgpPeer2AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbgpPeer2AdminStatus.setStatus("current")
_CbgpPeer2NegotiatedVersion_Type = Integer32
_CbgpPeer2NegotiatedVersion_Object = MibTableColumn
cbgpPeer2NegotiatedVersion = _CbgpPeer2NegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 5),
    _CbgpPeer2NegotiatedVersion_Type()
)
cbgpPeer2NegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2NegotiatedVersion.setStatus("current")
_CbgpPeer2LocalAddr_Type = InetAddress
_CbgpPeer2LocalAddr_Object = MibTableColumn
cbgpPeer2LocalAddr = _CbgpPeer2LocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 6),
    _CbgpPeer2LocalAddr_Type()
)
cbgpPeer2LocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2LocalAddr.setStatus("current")
_CbgpPeer2LocalPort_Type = InetPortNumber
_CbgpPeer2LocalPort_Object = MibTableColumn
cbgpPeer2LocalPort = _CbgpPeer2LocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 7),
    _CbgpPeer2LocalPort_Type()
)
cbgpPeer2LocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2LocalPort.setStatus("current")
_CbgpPeer2LocalAs_Type = InetAutonomousSystemNumber
_CbgpPeer2LocalAs_Object = MibTableColumn
cbgpPeer2LocalAs = _CbgpPeer2LocalAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 8),
    _CbgpPeer2LocalAs_Type()
)
cbgpPeer2LocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2LocalAs.setStatus("current")
_CbgpPeer2LocalIdentifier_Type = IpAddress
_CbgpPeer2LocalIdentifier_Object = MibTableColumn
cbgpPeer2LocalIdentifier = _CbgpPeer2LocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 9),
    _CbgpPeer2LocalIdentifier_Type()
)
cbgpPeer2LocalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2LocalIdentifier.setStatus("current")
_CbgpPeer2RemotePort_Type = InetPortNumber
_CbgpPeer2RemotePort_Object = MibTableColumn
cbgpPeer2RemotePort = _CbgpPeer2RemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 10),
    _CbgpPeer2RemotePort_Type()
)
cbgpPeer2RemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2RemotePort.setStatus("current")
_CbgpPeer2RemoteAs_Type = InetAutonomousSystemNumber
_CbgpPeer2RemoteAs_Object = MibTableColumn
cbgpPeer2RemoteAs = _CbgpPeer2RemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 11),
    _CbgpPeer2RemoteAs_Type()
)
cbgpPeer2RemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2RemoteAs.setStatus("current")
_CbgpPeer2RemoteIdentifier_Type = IpAddress
_CbgpPeer2RemoteIdentifier_Object = MibTableColumn
cbgpPeer2RemoteIdentifier = _CbgpPeer2RemoteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 12),
    _CbgpPeer2RemoteIdentifier_Type()
)
cbgpPeer2RemoteIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2RemoteIdentifier.setStatus("current")
_CbgpPeer2InUpdates_Type = Counter32
_CbgpPeer2InUpdates_Object = MibTableColumn
cbgpPeer2InUpdates = _CbgpPeer2InUpdates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 13),
    _CbgpPeer2InUpdates_Type()
)
cbgpPeer2InUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2InUpdates.setStatus("current")
_CbgpPeer2OutUpdates_Type = Counter32
_CbgpPeer2OutUpdates_Object = MibTableColumn
cbgpPeer2OutUpdates = _CbgpPeer2OutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 14),
    _CbgpPeer2OutUpdates_Type()
)
cbgpPeer2OutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2OutUpdates.setStatus("current")
_CbgpPeer2InTotalMessages_Type = Counter32
_CbgpPeer2InTotalMessages_Object = MibTableColumn
cbgpPeer2InTotalMessages = _CbgpPeer2InTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 15),
    _CbgpPeer2InTotalMessages_Type()
)
cbgpPeer2InTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2InTotalMessages.setStatus("current")
_CbgpPeer2OutTotalMessages_Type = Counter32
_CbgpPeer2OutTotalMessages_Object = MibTableColumn
cbgpPeer2OutTotalMessages = _CbgpPeer2OutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 16),
    _CbgpPeer2OutTotalMessages_Type()
)
cbgpPeer2OutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2OutTotalMessages.setStatus("current")


class _CbgpPeer2LastError_Type(OctetString):
    """Custom type cbgpPeer2LastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CbgpPeer2LastError_Type.__name__ = "OctetString"
_CbgpPeer2LastError_Object = MibTableColumn
cbgpPeer2LastError = _CbgpPeer2LastError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 17),
    _CbgpPeer2LastError_Type()
)
cbgpPeer2LastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2LastError.setStatus("current")
_CbgpPeer2FsmEstablishedTransitions_Type = Counter32
_CbgpPeer2FsmEstablishedTransitions_Object = MibTableColumn
cbgpPeer2FsmEstablishedTransitions = _CbgpPeer2FsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 18),
    _CbgpPeer2FsmEstablishedTransitions_Type()
)
cbgpPeer2FsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2FsmEstablishedTransitions.setStatus("current")
_CbgpPeer2FsmEstablishedTime_Type = Gauge32
_CbgpPeer2FsmEstablishedTime_Object = MibTableColumn
cbgpPeer2FsmEstablishedTime = _CbgpPeer2FsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 19),
    _CbgpPeer2FsmEstablishedTime_Type()
)
cbgpPeer2FsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2FsmEstablishedTime.setStatus("current")
if mibBuilder.loadTexts:
    cbgpPeer2FsmEstablishedTime.setUnits("seconds")


class _CbgpPeer2ConnectRetryInterval_Type(Integer32):
    """Custom type cbgpPeer2ConnectRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CbgpPeer2ConnectRetryInterval_Type.__name__ = "Integer32"
_CbgpPeer2ConnectRetryInterval_Object = MibTableColumn
cbgpPeer2ConnectRetryInterval = _CbgpPeer2ConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 20),
    _CbgpPeer2ConnectRetryInterval_Type()
)
cbgpPeer2ConnectRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbgpPeer2ConnectRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cbgpPeer2ConnectRetryInterval.setUnits("seconds")


class _CbgpPeer2HoldTime_Type(Integer32):
    """Custom type cbgpPeer2HoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_CbgpPeer2HoldTime_Type.__name__ = "Integer32"
_CbgpPeer2HoldTime_Object = MibTableColumn
cbgpPeer2HoldTime = _CbgpPeer2HoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 21),
    _CbgpPeer2HoldTime_Type()
)
cbgpPeer2HoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2HoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cbgpPeer2HoldTime.setUnits("seconds")


class _CbgpPeer2KeepAlive_Type(Integer32):
    """Custom type cbgpPeer2KeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_CbgpPeer2KeepAlive_Type.__name__ = "Integer32"
_CbgpPeer2KeepAlive_Object = MibTableColumn
cbgpPeer2KeepAlive = _CbgpPeer2KeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 22),
    _CbgpPeer2KeepAlive_Type()
)
cbgpPeer2KeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2KeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    cbgpPeer2KeepAlive.setUnits("seconds")


class _CbgpPeer2HoldTimeConfigured_Type(Integer32):
    """Custom type cbgpPeer2HoldTimeConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_CbgpPeer2HoldTimeConfigured_Type.__name__ = "Integer32"
_CbgpPeer2HoldTimeConfigured_Object = MibTableColumn
cbgpPeer2HoldTimeConfigured = _CbgpPeer2HoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 23),
    _CbgpPeer2HoldTimeConfigured_Type()
)
cbgpPeer2HoldTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbgpPeer2HoldTimeConfigured.setStatus("current")
if mibBuilder.loadTexts:
    cbgpPeer2HoldTimeConfigured.setUnits("seconds")


class _CbgpPeer2KeepAliveConfigured_Type(Integer32):
    """Custom type cbgpPeer2KeepAliveConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_CbgpPeer2KeepAliveConfigured_Type.__name__ = "Integer32"
_CbgpPeer2KeepAliveConfigured_Object = MibTableColumn
cbgpPeer2KeepAliveConfigured = _CbgpPeer2KeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 24),
    _CbgpPeer2KeepAliveConfigured_Type()
)
cbgpPeer2KeepAliveConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbgpPeer2KeepAliveConfigured.setStatus("current")
if mibBuilder.loadTexts:
    cbgpPeer2KeepAliveConfigured.setUnits("seconds")


class _CbgpPeer2MinASOriginationInterval_Type(Integer32):
    """Custom type cbgpPeer2MinASOriginationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CbgpPeer2MinASOriginationInterval_Type.__name__ = "Integer32"
_CbgpPeer2MinASOriginationInterval_Object = MibTableColumn
cbgpPeer2MinASOriginationInterval = _CbgpPeer2MinASOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 25),
    _CbgpPeer2MinASOriginationInterval_Type()
)
cbgpPeer2MinASOriginationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbgpPeer2MinASOriginationInterval.setStatus("current")
if mibBuilder.loadTexts:
    cbgpPeer2MinASOriginationInterval.setUnits("seconds")


class _CbgpPeer2MinRouteAdvertisementInterval_Type(Integer32):
    """Custom type cbgpPeer2MinRouteAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CbgpPeer2MinRouteAdvertisementInterval_Type.__name__ = "Integer32"
_CbgpPeer2MinRouteAdvertisementInterval_Object = MibTableColumn
cbgpPeer2MinRouteAdvertisementInterval = _CbgpPeer2MinRouteAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 26),
    _CbgpPeer2MinRouteAdvertisementInterval_Type()
)
cbgpPeer2MinRouteAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbgpPeer2MinRouteAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    cbgpPeer2MinRouteAdvertisementInterval.setUnits("seconds")
_CbgpPeer2InUpdateElapsedTime_Type = Gauge32
_CbgpPeer2InUpdateElapsedTime_Object = MibTableColumn
cbgpPeer2InUpdateElapsedTime = _CbgpPeer2InUpdateElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 27),
    _CbgpPeer2InUpdateElapsedTime_Type()
)
cbgpPeer2InUpdateElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2InUpdateElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    cbgpPeer2InUpdateElapsedTime.setUnits("seconds")
_CbgpPeer2LastErrorTxt_Type = SnmpAdminString
_CbgpPeer2LastErrorTxt_Object = MibTableColumn
cbgpPeer2LastErrorTxt = _CbgpPeer2LastErrorTxt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 28),
    _CbgpPeer2LastErrorTxt_Type()
)
cbgpPeer2LastErrorTxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2LastErrorTxt.setStatus("current")


class _CbgpPeer2PrevState_Type(Integer32):
    """Custom type cbgpPeer2PrevState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
          ("none", 0),
          ("openconfirm", 5),
          ("opensent", 4))
    )


_CbgpPeer2PrevState_Type.__name__ = "Integer32"
_CbgpPeer2PrevState_Object = MibTableColumn
cbgpPeer2PrevState = _CbgpPeer2PrevState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 5, 1, 29),
    _CbgpPeer2PrevState_Type()
)
cbgpPeer2PrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2PrevState.setStatus("current")
_CbgpPeer2CapsTable_Object = MibTable
cbgpPeer2CapsTable = _CbgpPeer2CapsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cbgpPeer2CapsTable.setStatus("current")
_CbgpPeer2CapsEntry_Object = MibTableRow
cbgpPeer2CapsEntry = _CbgpPeer2CapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 6, 1)
)
cbgpPeer2CapsEntry.setIndexNames(
    (0, "CISCO-BGP4-MIB", "cbgpPeer2Type"),
    (0, "CISCO-BGP4-MIB", "cbgpPeer2RemoteAddr"),
    (0, "CISCO-BGP4-MIB", "cbgpPeer2CapCode"),
    (0, "CISCO-BGP4-MIB", "cbgpPeer2CapIndex"),
)
if mibBuilder.loadTexts:
    cbgpPeer2CapsEntry.setStatus("current")


class _CbgpPeer2CapCode_Type(Integer32):
    """Custom type cbgpPeer2CapCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              64,
              65,
              69,
              128)
        )
    )
    namedValues = NamedValues(
        *(("addPath", 69),
          ("fourByteAs", 65),
          ("gracefulRestart", 64),
          ("multiProtocol", 1),
          ("routeRefresh", 2),
          ("routeRefreshOld", 128))
    )


_CbgpPeer2CapCode_Type.__name__ = "Integer32"
_CbgpPeer2CapCode_Object = MibTableColumn
cbgpPeer2CapCode = _CbgpPeer2CapCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 6, 1, 1),
    _CbgpPeer2CapCode_Type()
)
cbgpPeer2CapCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpPeer2CapCode.setStatus("current")


class _CbgpPeer2CapIndex_Type(Unsigned32):
    """Custom type cbgpPeer2CapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CbgpPeer2CapIndex_Type.__name__ = "Unsigned32"
_CbgpPeer2CapIndex_Object = MibTableColumn
cbgpPeer2CapIndex = _CbgpPeer2CapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 6, 1, 2),
    _CbgpPeer2CapIndex_Type()
)
cbgpPeer2CapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpPeer2CapIndex.setStatus("current")


class _CbgpPeer2CapValue_Type(OctetString):
    """Custom type cbgpPeer2CapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CbgpPeer2CapValue_Type.__name__ = "OctetString"
_CbgpPeer2CapValue_Object = MibTableColumn
cbgpPeer2CapValue = _CbgpPeer2CapValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 6, 1, 3),
    _CbgpPeer2CapValue_Type()
)
cbgpPeer2CapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2CapValue.setStatus("current")
_CbgpPeer2AddrFamilyTable_Object = MibTable
cbgpPeer2AddrFamilyTable = _CbgpPeer2AddrFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cbgpPeer2AddrFamilyTable.setStatus("current")
_CbgpPeer2AddrFamilyEntry_Object = MibTableRow
cbgpPeer2AddrFamilyEntry = _CbgpPeer2AddrFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 7, 1)
)
cbgpPeer2AddrFamilyEntry.setIndexNames(
    (0, "CISCO-BGP4-MIB", "cbgpPeer2Type"),
    (0, "CISCO-BGP4-MIB", "cbgpPeer2RemoteAddr"),
    (0, "CISCO-BGP4-MIB", "cbgpPeer2AddrFamilyAfi"),
    (0, "CISCO-BGP4-MIB", "cbgpPeer2AddrFamilySafi"),
)
if mibBuilder.loadTexts:
    cbgpPeer2AddrFamilyEntry.setStatus("current")
_CbgpPeer2AddrFamilyAfi_Type = InetAddressType
_CbgpPeer2AddrFamilyAfi_Object = MibTableColumn
cbgpPeer2AddrFamilyAfi = _CbgpPeer2AddrFamilyAfi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 7, 1, 1),
    _CbgpPeer2AddrFamilyAfi_Type()
)
cbgpPeer2AddrFamilyAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpPeer2AddrFamilyAfi.setStatus("current")
_CbgpPeer2AddrFamilySafi_Type = CbgpSafi
_CbgpPeer2AddrFamilySafi_Object = MibTableColumn
cbgpPeer2AddrFamilySafi = _CbgpPeer2AddrFamilySafi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 7, 1, 2),
    _CbgpPeer2AddrFamilySafi_Type()
)
cbgpPeer2AddrFamilySafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbgpPeer2AddrFamilySafi.setStatus("current")
_CbgpPeer2AddrFamilyName_Type = SnmpAdminString
_CbgpPeer2AddrFamilyName_Object = MibTableColumn
cbgpPeer2AddrFamilyName = _CbgpPeer2AddrFamilyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 7, 1, 3),
    _CbgpPeer2AddrFamilyName_Type()
)
cbgpPeer2AddrFamilyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2AddrFamilyName.setStatus("current")
_CbgpPeer2AddrFamilyPrefixTable_Object = MibTable
cbgpPeer2AddrFamilyPrefixTable = _CbgpPeer2AddrFamilyPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cbgpPeer2AddrFamilyPrefixTable.setStatus("current")
_CbgpPeer2AddrFamilyPrefixEntry_Object = MibTableRow
cbgpPeer2AddrFamilyPrefixEntry = _CbgpPeer2AddrFamilyPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 8, 1)
)
cbgpPeer2AddrFamilyPrefixEntry.setIndexNames(
    (0, "CISCO-BGP4-MIB", "cbgpPeer2Type"),
    (0, "CISCO-BGP4-MIB", "cbgpPeer2RemoteAddr"),
    (0, "CISCO-BGP4-MIB", "cbgpPeer2AddrFamilyAfi"),
    (0, "CISCO-BGP4-MIB", "cbgpPeer2AddrFamilySafi"),
)
if mibBuilder.loadTexts:
    cbgpPeer2AddrFamilyPrefixEntry.setStatus("current")
_CbgpPeer2AcceptedPrefixes_Type = Counter32
_CbgpPeer2AcceptedPrefixes_Object = MibTableColumn
cbgpPeer2AcceptedPrefixes = _CbgpPeer2AcceptedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 8, 1, 1),
    _CbgpPeer2AcceptedPrefixes_Type()
)
cbgpPeer2AcceptedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2AcceptedPrefixes.setStatus("current")
_CbgpPeer2DeniedPrefixes_Type = Gauge32
_CbgpPeer2DeniedPrefixes_Object = MibTableColumn
cbgpPeer2DeniedPrefixes = _CbgpPeer2DeniedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 8, 1, 2),
    _CbgpPeer2DeniedPrefixes_Type()
)
cbgpPeer2DeniedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2DeniedPrefixes.setStatus("current")


class _CbgpPeer2PrefixAdminLimit_Type(Unsigned32):
    """Custom type cbgpPeer2PrefixAdminLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CbgpPeer2PrefixAdminLimit_Type.__name__ = "Unsigned32"
_CbgpPeer2PrefixAdminLimit_Object = MibTableColumn
cbgpPeer2PrefixAdminLimit = _CbgpPeer2PrefixAdminLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 8, 1, 3),
    _CbgpPeer2PrefixAdminLimit_Type()
)
cbgpPeer2PrefixAdminLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbgpPeer2PrefixAdminLimit.setStatus("current")


class _CbgpPeer2PrefixThreshold_Type(Unsigned32):
    """Custom type cbgpPeer2PrefixThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CbgpPeer2PrefixThreshold_Type.__name__ = "Unsigned32"
_CbgpPeer2PrefixThreshold_Object = MibTableColumn
cbgpPeer2PrefixThreshold = _CbgpPeer2PrefixThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 8, 1, 4),
    _CbgpPeer2PrefixThreshold_Type()
)
cbgpPeer2PrefixThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbgpPeer2PrefixThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cbgpPeer2PrefixThreshold.setUnits("percent")


class _CbgpPeer2PrefixClearThreshold_Type(Unsigned32):
    """Custom type cbgpPeer2PrefixClearThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CbgpPeer2PrefixClearThreshold_Type.__name__ = "Unsigned32"
_CbgpPeer2PrefixClearThreshold_Object = MibTableColumn
cbgpPeer2PrefixClearThreshold = _CbgpPeer2PrefixClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 8, 1, 5),
    _CbgpPeer2PrefixClearThreshold_Type()
)
cbgpPeer2PrefixClearThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2PrefixClearThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cbgpPeer2PrefixClearThreshold.setUnits("percent")
_CbgpPeer2AdvertisedPrefixes_Type = Gauge32
_CbgpPeer2AdvertisedPrefixes_Object = MibTableColumn
cbgpPeer2AdvertisedPrefixes = _CbgpPeer2AdvertisedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 8, 1, 6),
    _CbgpPeer2AdvertisedPrefixes_Type()
)
cbgpPeer2AdvertisedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2AdvertisedPrefixes.setStatus("current")
_CbgpPeer2SuppressedPrefixes_Type = Gauge32
_CbgpPeer2SuppressedPrefixes_Object = MibTableColumn
cbgpPeer2SuppressedPrefixes = _CbgpPeer2SuppressedPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 8, 1, 7),
    _CbgpPeer2SuppressedPrefixes_Type()
)
cbgpPeer2SuppressedPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2SuppressedPrefixes.setStatus("current")
_CbgpPeer2WithdrawnPrefixes_Type = Gauge32
_CbgpPeer2WithdrawnPrefixes_Object = MibTableColumn
cbgpPeer2WithdrawnPrefixes = _CbgpPeer2WithdrawnPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 2, 8, 1, 8),
    _CbgpPeer2WithdrawnPrefixes_Type()
)
cbgpPeer2WithdrawnPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpPeer2WithdrawnPrefixes.setStatus("current")
_CbgpGlobal_ObjectIdentity = ObjectIdentity
cbgpGlobal = _CbgpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 3)
)


class _CbgpNotifsEnable_Type(Bits):
    """Custom type cbgpNotifsEnable based on Bits"""
    namedValues = NamedValues(
        *(("notifsEnable", 0),
          ("notifsPeer2Enable", 1))
    )

_CbgpNotifsEnable_Type.__name__ = "Bits"
_CbgpNotifsEnable_Object = MibScalar
cbgpNotifsEnable = _CbgpNotifsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 3, 1),
    _CbgpNotifsEnable_Type()
)
cbgpNotifsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbgpNotifsEnable.setStatus("current")
_CbgpLocalAs_Type = InetAutonomousSystemNumber
_CbgpLocalAs_Object = MibScalar
cbgpLocalAs = _CbgpLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 1, 3, 2),
    _CbgpLocalAs_Type()
)
cbgpLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbgpLocalAs.setStatus("current")
_CiscoBgp4NotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoBgp4NotificationPrefix = _CiscoBgp4NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 2)
)
_CiscoBgp4MIBConformance_ObjectIdentity = ObjectIdentity
ciscoBgp4MIBConformance = _CiscoBgp4MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3)
)
_CiscoBgp4MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoBgp4MIBCompliances = _CiscoBgp4MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3, 1)
)
_CiscoBgp4MIBGroups_ObjectIdentity = ObjectIdentity
ciscoBgp4MIBGroups = _CiscoBgp4MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3, 2)
)
bgpPeerEntry.registerAugmentions(
    ("CISCO-BGP4-MIB",
     "cbgpPeerEntry")
)
cbgpPeerEntry.setIndexNames(*bgpPeerEntry.getIndexNames())

# Managed Objects groups

ciscoBgp4RouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3, 2, 1)
)
ciscoBgp4RouteGroup.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpRouteOrigin"),
        ("CISCO-BGP4-MIB", "cbgpRouteASPathSegment"),
        ("CISCO-BGP4-MIB", "cbgpRouteNextHop"),
        ("CISCO-BGP4-MIB", "cbgpRouteMedPresent"),
        ("CISCO-BGP4-MIB", "cbgpRouteMultiExitDisc"),
        ("CISCO-BGP4-MIB", "cbgpRouteLocalPrefPresent"),
        ("CISCO-BGP4-MIB", "cbgpRouteLocalPref"),
        ("CISCO-BGP4-MIB", "cbgpRouteAtomicAggregate"),
        ("CISCO-BGP4-MIB", "cbgpRouteAggregatorAS"),
        ("CISCO-BGP4-MIB", "cbgpRouteAggregatorAddrType"),
        ("CISCO-BGP4-MIB", "cbgpRouteAggregatorAddr"),
        ("CISCO-BGP4-MIB", "cbgpRouteBest"),
        ("CISCO-BGP4-MIB", "cbgpRouteUnknownAttr"))
)
if mibBuilder.loadTexts:
    ciscoBgp4RouteGroup.setStatus("current")

ciscoBgp4PeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3, 2, 2)
)
ciscoBgp4PeerGroup.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpPeerPrefixAccepted"),
        ("CISCO-BGP4-MIB", "cbgpPeerPrefixDenied"),
        ("CISCO-BGP4-MIB", "cbgpPeerPrefixLimit"),
        ("CISCO-BGP4-MIB", "cbgpPeerPrefixAdvertised"),
        ("CISCO-BGP4-MIB", "cbgpPeerPrefixSuppressed"),
        ("CISCO-BGP4-MIB", "cbgpPeerPrefixWithdrawn"))
)
if mibBuilder.loadTexts:
    ciscoBgp4PeerGroup.setStatus("deprecated")

ciscoBgp4PeerGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3, 2, 4)
)
ciscoBgp4PeerGroup1.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpPeerPrevState"),
        ("CISCO-BGP4-MIB", "cbgpPeerLastErrorTxt"),
        ("CISCO-BGP4-MIB", "cbgpPeerCapValue"),
        ("CISCO-BGP4-MIB", "cbgpPeerAddrFamilyName"),
        ("CISCO-BGP4-MIB", "cbgpPeerAcceptedPrefixes"),
        ("CISCO-BGP4-MIB", "cbgpPeerDeniedPrefixes"),
        ("CISCO-BGP4-MIB", "cbgpPeerPrefixAdminLimit"),
        ("CISCO-BGP4-MIB", "cbgpPeerPrefixThreshold"),
        ("CISCO-BGP4-MIB", "cbgpPeerPrefixClearThreshold"),
        ("CISCO-BGP4-MIB", "cbgpPeerAdvertisedPrefixes"),
        ("CISCO-BGP4-MIB", "cbgpPeerSuppressedPrefixes"),
        ("CISCO-BGP4-MIB", "cbgpPeerWithdrawnPrefixes"))
)
if mibBuilder.loadTexts:
    ciscoBgp4PeerGroup1.setStatus("current")

ciscoBgp4Peer2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3, 2, 6)
)
ciscoBgp4Peer2Group.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpPeer2State"),
        ("CISCO-BGP4-MIB", "cbgpPeer2AdminStatus"),
        ("CISCO-BGP4-MIB", "cbgpPeer2NegotiatedVersion"),
        ("CISCO-BGP4-MIB", "cbgpPeer2LocalAddr"),
        ("CISCO-BGP4-MIB", "cbgpPeer2LocalPort"),
        ("CISCO-BGP4-MIB", "cbgpPeer2LocalAs"),
        ("CISCO-BGP4-MIB", "cbgpPeer2LocalIdentifier"),
        ("CISCO-BGP4-MIB", "cbgpPeer2RemotePort"),
        ("CISCO-BGP4-MIB", "cbgpPeer2RemoteAs"),
        ("CISCO-BGP4-MIB", "cbgpPeer2RemoteIdentifier"),
        ("CISCO-BGP4-MIB", "cbgpPeer2InUpdates"),
        ("CISCO-BGP4-MIB", "cbgpPeer2OutUpdates"),
        ("CISCO-BGP4-MIB", "cbgpPeer2InTotalMessages"),
        ("CISCO-BGP4-MIB", "cbgpPeer2OutTotalMessages"),
        ("CISCO-BGP4-MIB", "cbgpPeer2LastError"),
        ("CISCO-BGP4-MIB", "cbgpPeer2FsmEstablishedTransitions"),
        ("CISCO-BGP4-MIB", "cbgpPeer2FsmEstablishedTime"),
        ("CISCO-BGP4-MIB", "cbgpPeer2ConnectRetryInterval"),
        ("CISCO-BGP4-MIB", "cbgpPeer2HoldTime"),
        ("CISCO-BGP4-MIB", "cbgpPeer2KeepAlive"),
        ("CISCO-BGP4-MIB", "cbgpPeer2HoldTimeConfigured"),
        ("CISCO-BGP4-MIB", "cbgpPeer2KeepAliveConfigured"),
        ("CISCO-BGP4-MIB", "cbgpPeer2MinASOriginationInterval"),
        ("CISCO-BGP4-MIB", "cbgpPeer2MinRouteAdvertisementInterval"),
        ("CISCO-BGP4-MIB", "cbgpPeer2InUpdateElapsedTime"),
        ("CISCO-BGP4-MIB", "cbgpPeer2LastErrorTxt"),
        ("CISCO-BGP4-MIB", "cbgpPeer2PrevState"),
        ("CISCO-BGP4-MIB", "cbgpPeer2CapValue"),
        ("CISCO-BGP4-MIB", "cbgpPeer2AddrFamilyName"),
        ("CISCO-BGP4-MIB", "cbgpPeer2AcceptedPrefixes"),
        ("CISCO-BGP4-MIB", "cbgpPeer2DeniedPrefixes"),
        ("CISCO-BGP4-MIB", "cbgpPeer2PrefixAdminLimit"),
        ("CISCO-BGP4-MIB", "cbgpPeer2PrefixThreshold"),
        ("CISCO-BGP4-MIB", "cbgpPeer2PrefixClearThreshold"),
        ("CISCO-BGP4-MIB", "cbgpPeer2AdvertisedPrefixes"),
        ("CISCO-BGP4-MIB", "cbgpPeer2SuppressedPrefixes"),
        ("CISCO-BGP4-MIB", "cbgpPeer2WithdrawnPrefixes"))
)
if mibBuilder.loadTexts:
    ciscoBgp4Peer2Group.setStatus("current")

ciscoBgp4GlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3, 2, 8)
)
ciscoBgp4GlobalGroup.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpNotifsEnable"),
        ("CISCO-BGP4-MIB", "cbgpLocalAs"))
)
if mibBuilder.loadTexts:
    ciscoBgp4GlobalGroup.setStatus("current")


# Notification objects

cbgpFsmStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 0, 1)
)
cbgpFsmStateChange.setObjects(
      *(("BGP4-MIB", "bgpPeerLastError"),
        ("BGP4-MIB", "bgpPeerState"),
        ("CISCO-BGP4-MIB", "cbgpPeerLastErrorTxt"),
        ("CISCO-BGP4-MIB", "cbgpPeerPrevState"))
)
if mibBuilder.loadTexts:
    cbgpFsmStateChange.setStatus(
        "current"
    )

cbgpBackwardTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 0, 2)
)
cbgpBackwardTransition.setObjects(
      *(("BGP4-MIB", "bgpPeerLastError"),
        ("BGP4-MIB", "bgpPeerState"),
        ("CISCO-BGP4-MIB", "cbgpPeerLastErrorTxt"),
        ("CISCO-BGP4-MIB", "cbgpPeerPrevState"))
)
if mibBuilder.loadTexts:
    cbgpBackwardTransition.setStatus(
        "current"
    )

cbgpPrefixThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 0, 3)
)
cbgpPrefixThresholdExceeded.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpPeerPrefixAdminLimit"),
        ("CISCO-BGP4-MIB", "cbgpPeerPrefixThreshold"))
)
if mibBuilder.loadTexts:
    cbgpPrefixThresholdExceeded.setStatus(
        "current"
    )

cbgpPrefixThresholdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 0, 4)
)
cbgpPrefixThresholdClear.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpPeerPrefixAdminLimit"),
        ("CISCO-BGP4-MIB", "cbgpPeerPrefixClearThreshold"))
)
if mibBuilder.loadTexts:
    cbgpPrefixThresholdClear.setStatus(
        "current"
    )

cbgpPeer2EstablishedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 0, 5)
)
cbgpPeer2EstablishedNotification.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpPeer2LastError"),
        ("CISCO-BGP4-MIB", "cbgpPeer2State"))
)
if mibBuilder.loadTexts:
    cbgpPeer2EstablishedNotification.setStatus(
        "current"
    )

cbgpPeer2BackwardTransNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 0, 6)
)
cbgpPeer2BackwardTransNotification.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpPeer2LastError"),
        ("CISCO-BGP4-MIB", "cbgpPeer2State"))
)
if mibBuilder.loadTexts:
    cbgpPeer2BackwardTransNotification.setStatus(
        "current"
    )

cbgpPeer2FsmStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 0, 7)
)
cbgpPeer2FsmStateChange.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpPeer2LastError"),
        ("CISCO-BGP4-MIB", "cbgpPeer2State"),
        ("CISCO-BGP4-MIB", "cbgpPeer2LastErrorTxt"),
        ("CISCO-BGP4-MIB", "cbgpPeer2PrevState"))
)
if mibBuilder.loadTexts:
    cbgpPeer2FsmStateChange.setStatus(
        "current"
    )

cbgpPeer2BackwardTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 0, 8)
)
cbgpPeer2BackwardTransition.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpPeer2LastError"),
        ("CISCO-BGP4-MIB", "cbgpPeer2State"),
        ("CISCO-BGP4-MIB", "cbgpPeer2LastErrorTxt"),
        ("CISCO-BGP4-MIB", "cbgpPeer2PrevState"))
)
if mibBuilder.loadTexts:
    cbgpPeer2BackwardTransition.setStatus(
        "current"
    )

cbgpPeer2PrefixThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 0, 9)
)
cbgpPeer2PrefixThresholdExceeded.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpPeer2PrefixAdminLimit"),
        ("CISCO-BGP4-MIB", "cbgpPeer2PrefixThreshold"))
)
if mibBuilder.loadTexts:
    cbgpPeer2PrefixThresholdExceeded.setStatus(
        "current"
    )

cbgpPeer2PrefixThresholdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 0, 10)
)
cbgpPeer2PrefixThresholdClear.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpPeer2PrefixAdminLimit"),
        ("CISCO-BGP4-MIB", "cbgpPeer2PrefixClearThreshold"))
)
if mibBuilder.loadTexts:
    cbgpPeer2PrefixThresholdClear.setStatus(
        "current"
    )


# Notifications groups

ciscoBgp4NotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3, 2, 3)
)
ciscoBgp4NotificationsGroup.setObjects(
    ("CISCO-BGP4-MIB", "cbgpFsmStateChange")
)
if mibBuilder.loadTexts:
    ciscoBgp4NotificationsGroup.setStatus(
        "deprecated"
    )

ciscoBgp4NotificationsGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3, 2, 5)
)
ciscoBgp4NotificationsGroup1.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpFsmStateChange"),
        ("CISCO-BGP4-MIB", "cbgpBackwardTransition"),
        ("CISCO-BGP4-MIB", "cbgpPrefixThresholdExceeded"),
        ("CISCO-BGP4-MIB", "cbgpPrefixThresholdClear"))
)
if mibBuilder.loadTexts:
    ciscoBgp4NotificationsGroup1.setStatus(
        "current"
    )

ciscoBgp4Peer2NotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3, 2, 7)
)
ciscoBgp4Peer2NotificationsGroup.setObjects(
      *(("CISCO-BGP4-MIB", "cbgpPeer2EstablishedNotification"),
        ("CISCO-BGP4-MIB", "cbgpPeer2BackwardTransNotification"),
        ("CISCO-BGP4-MIB", "cbgpPeer2FsmStateChange"),
        ("CISCO-BGP4-MIB", "cbgpPeer2BackwardTransition"),
        ("CISCO-BGP4-MIB", "cbgpPeer2PrefixThresholdExceeded"),
        ("CISCO-BGP4-MIB", "cbgpPeer2PrefixThresholdClear"))
)
if mibBuilder.loadTexts:
    ciscoBgp4Peer2NotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoBgp4MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoBgp4MIBCompliance.setStatus(
        "deprecated"
    )

ciscoBgp4MIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoBgp4MIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoBgp4MIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoBgp4MIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoBgp4MIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 187, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoBgp4MIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BGP4-MIB",
    **{"CbgpSafi": CbgpSafi,
       "CbgpNetworkAddress": CbgpNetworkAddress,
       "ciscoBgp4MIB": ciscoBgp4MIB,
       "ciscoBgp4NotifyPrefix": ciscoBgp4NotifyPrefix,
       "cbgpFsmStateChange": cbgpFsmStateChange,
       "cbgpBackwardTransition": cbgpBackwardTransition,
       "cbgpPrefixThresholdExceeded": cbgpPrefixThresholdExceeded,
       "cbgpPrefixThresholdClear": cbgpPrefixThresholdClear,
       "cbgpPeer2EstablishedNotification": cbgpPeer2EstablishedNotification,
       "cbgpPeer2BackwardTransNotification": cbgpPeer2BackwardTransNotification,
       "cbgpPeer2FsmStateChange": cbgpPeer2FsmStateChange,
       "cbgpPeer2BackwardTransition": cbgpPeer2BackwardTransition,
       "cbgpPeer2PrefixThresholdExceeded": cbgpPeer2PrefixThresholdExceeded,
       "cbgpPeer2PrefixThresholdClear": cbgpPeer2PrefixThresholdClear,
       "ciscoBgp4MIBObjects": ciscoBgp4MIBObjects,
       "cbgpRoute": cbgpRoute,
       "cbgpRouteTable": cbgpRouteTable,
       "cbgpRouteEntry": cbgpRouteEntry,
       "cbgpRouteAfi": cbgpRouteAfi,
       "cbgpRouteSafi": cbgpRouteSafi,
       "cbgpRoutePeerType": cbgpRoutePeerType,
       "cbgpRoutePeer": cbgpRoutePeer,
       "cbgpRouteAddrPrefix": cbgpRouteAddrPrefix,
       "cbgpRouteAddrPrefixLen": cbgpRouteAddrPrefixLen,
       "cbgpRouteOrigin": cbgpRouteOrigin,
       "cbgpRouteASPathSegment": cbgpRouteASPathSegment,
       "cbgpRouteNextHop": cbgpRouteNextHop,
       "cbgpRouteMedPresent": cbgpRouteMedPresent,
       "cbgpRouteMultiExitDisc": cbgpRouteMultiExitDisc,
       "cbgpRouteLocalPrefPresent": cbgpRouteLocalPrefPresent,
       "cbgpRouteLocalPref": cbgpRouteLocalPref,
       "cbgpRouteAtomicAggregate": cbgpRouteAtomicAggregate,
       "cbgpRouteAggregatorAS": cbgpRouteAggregatorAS,
       "cbgpRouteAggregatorAddrType": cbgpRouteAggregatorAddrType,
       "cbgpRouteAggregatorAddr": cbgpRouteAggregatorAddr,
       "cbgpRouteBest": cbgpRouteBest,
       "cbgpRouteUnknownAttr": cbgpRouteUnknownAttr,
       "cbgpPeer": cbgpPeer,
       "cbgpPeerTable": cbgpPeerTable,
       "cbgpPeerEntry": cbgpPeerEntry,
       "cbgpPeerPrefixAccepted": cbgpPeerPrefixAccepted,
       "cbgpPeerPrefixDenied": cbgpPeerPrefixDenied,
       "cbgpPeerPrefixLimit": cbgpPeerPrefixLimit,
       "cbgpPeerPrefixAdvertised": cbgpPeerPrefixAdvertised,
       "cbgpPeerPrefixSuppressed": cbgpPeerPrefixSuppressed,
       "cbgpPeerPrefixWithdrawn": cbgpPeerPrefixWithdrawn,
       "cbgpPeerLastErrorTxt": cbgpPeerLastErrorTxt,
       "cbgpPeerPrevState": cbgpPeerPrevState,
       "cbgpPeerCapsTable": cbgpPeerCapsTable,
       "cbgpPeerCapsEntry": cbgpPeerCapsEntry,
       "cbgpPeerCapCode": cbgpPeerCapCode,
       "cbgpPeerCapIndex": cbgpPeerCapIndex,
       "cbgpPeerCapValue": cbgpPeerCapValue,
       "cbgpPeerAddrFamilyTable": cbgpPeerAddrFamilyTable,
       "cbgpPeerAddrFamilyEntry": cbgpPeerAddrFamilyEntry,
       "cbgpPeerAddrFamilyAfi": cbgpPeerAddrFamilyAfi,
       "cbgpPeerAddrFamilySafi": cbgpPeerAddrFamilySafi,
       "cbgpPeerAddrFamilyName": cbgpPeerAddrFamilyName,
       "cbgpPeerAddrFamilyPrefixTable": cbgpPeerAddrFamilyPrefixTable,
       "cbgpPeerAddrFamilyPrefixEntry": cbgpPeerAddrFamilyPrefixEntry,
       "cbgpPeerAcceptedPrefixes": cbgpPeerAcceptedPrefixes,
       "cbgpPeerDeniedPrefixes": cbgpPeerDeniedPrefixes,
       "cbgpPeerPrefixAdminLimit": cbgpPeerPrefixAdminLimit,
       "cbgpPeerPrefixThreshold": cbgpPeerPrefixThreshold,
       "cbgpPeerPrefixClearThreshold": cbgpPeerPrefixClearThreshold,
       "cbgpPeerAdvertisedPrefixes": cbgpPeerAdvertisedPrefixes,
       "cbgpPeerSuppressedPrefixes": cbgpPeerSuppressedPrefixes,
       "cbgpPeerWithdrawnPrefixes": cbgpPeerWithdrawnPrefixes,
       "cbgpPeer2Table": cbgpPeer2Table,
       "cbgpPeer2Entry": cbgpPeer2Entry,
       "cbgpPeer2Type": cbgpPeer2Type,
       "cbgpPeer2RemoteAddr": cbgpPeer2RemoteAddr,
       "cbgpPeer2State": cbgpPeer2State,
       "cbgpPeer2AdminStatus": cbgpPeer2AdminStatus,
       "cbgpPeer2NegotiatedVersion": cbgpPeer2NegotiatedVersion,
       "cbgpPeer2LocalAddr": cbgpPeer2LocalAddr,
       "cbgpPeer2LocalPort": cbgpPeer2LocalPort,
       "cbgpPeer2LocalAs": cbgpPeer2LocalAs,
       "cbgpPeer2LocalIdentifier": cbgpPeer2LocalIdentifier,
       "cbgpPeer2RemotePort": cbgpPeer2RemotePort,
       "cbgpPeer2RemoteAs": cbgpPeer2RemoteAs,
       "cbgpPeer2RemoteIdentifier": cbgpPeer2RemoteIdentifier,
       "cbgpPeer2InUpdates": cbgpPeer2InUpdates,
       "cbgpPeer2OutUpdates": cbgpPeer2OutUpdates,
       "cbgpPeer2InTotalMessages": cbgpPeer2InTotalMessages,
       "cbgpPeer2OutTotalMessages": cbgpPeer2OutTotalMessages,
       "cbgpPeer2LastError": cbgpPeer2LastError,
       "cbgpPeer2FsmEstablishedTransitions": cbgpPeer2FsmEstablishedTransitions,
       "cbgpPeer2FsmEstablishedTime": cbgpPeer2FsmEstablishedTime,
       "cbgpPeer2ConnectRetryInterval": cbgpPeer2ConnectRetryInterval,
       "cbgpPeer2HoldTime": cbgpPeer2HoldTime,
       "cbgpPeer2KeepAlive": cbgpPeer2KeepAlive,
       "cbgpPeer2HoldTimeConfigured": cbgpPeer2HoldTimeConfigured,
       "cbgpPeer2KeepAliveConfigured": cbgpPeer2KeepAliveConfigured,
       "cbgpPeer2MinASOriginationInterval": cbgpPeer2MinASOriginationInterval,
       "cbgpPeer2MinRouteAdvertisementInterval": cbgpPeer2MinRouteAdvertisementInterval,
       "cbgpPeer2InUpdateElapsedTime": cbgpPeer2InUpdateElapsedTime,
       "cbgpPeer2LastErrorTxt": cbgpPeer2LastErrorTxt,
       "cbgpPeer2PrevState": cbgpPeer2PrevState,
       "cbgpPeer2CapsTable": cbgpPeer2CapsTable,
       "cbgpPeer2CapsEntry": cbgpPeer2CapsEntry,
       "cbgpPeer2CapCode": cbgpPeer2CapCode,
       "cbgpPeer2CapIndex": cbgpPeer2CapIndex,
       "cbgpPeer2CapValue": cbgpPeer2CapValue,
       "cbgpPeer2AddrFamilyTable": cbgpPeer2AddrFamilyTable,
       "cbgpPeer2AddrFamilyEntry": cbgpPeer2AddrFamilyEntry,
       "cbgpPeer2AddrFamilyAfi": cbgpPeer2AddrFamilyAfi,
       "cbgpPeer2AddrFamilySafi": cbgpPeer2AddrFamilySafi,
       "cbgpPeer2AddrFamilyName": cbgpPeer2AddrFamilyName,
       "cbgpPeer2AddrFamilyPrefixTable": cbgpPeer2AddrFamilyPrefixTable,
       "cbgpPeer2AddrFamilyPrefixEntry": cbgpPeer2AddrFamilyPrefixEntry,
       "cbgpPeer2AcceptedPrefixes": cbgpPeer2AcceptedPrefixes,
       "cbgpPeer2DeniedPrefixes": cbgpPeer2DeniedPrefixes,
       "cbgpPeer2PrefixAdminLimit": cbgpPeer2PrefixAdminLimit,
       "cbgpPeer2PrefixThreshold": cbgpPeer2PrefixThreshold,
       "cbgpPeer2PrefixClearThreshold": cbgpPeer2PrefixClearThreshold,
       "cbgpPeer2AdvertisedPrefixes": cbgpPeer2AdvertisedPrefixes,
       "cbgpPeer2SuppressedPrefixes": cbgpPeer2SuppressedPrefixes,
       "cbgpPeer2WithdrawnPrefixes": cbgpPeer2WithdrawnPrefixes,
       "cbgpGlobal": cbgpGlobal,
       "cbgpNotifsEnable": cbgpNotifsEnable,
       "cbgpLocalAs": cbgpLocalAs,
       "ciscoBgp4NotificationPrefix": ciscoBgp4NotificationPrefix,
       "ciscoBgp4MIBConformance": ciscoBgp4MIBConformance,
       "ciscoBgp4MIBCompliances": ciscoBgp4MIBCompliances,
       "ciscoBgp4MIBCompliance": ciscoBgp4MIBCompliance,
       "ciscoBgp4MIBComplianceRev1": ciscoBgp4MIBComplianceRev1,
       "ciscoBgp4MIBComplianceRev2": ciscoBgp4MIBComplianceRev2,
       "ciscoBgp4MIBComplianceRev3": ciscoBgp4MIBComplianceRev3,
       "ciscoBgp4MIBGroups": ciscoBgp4MIBGroups,
       "ciscoBgp4RouteGroup": ciscoBgp4RouteGroup,
       "ciscoBgp4PeerGroup": ciscoBgp4PeerGroup,
       "ciscoBgp4NotificationsGroup": ciscoBgp4NotificationsGroup,
       "ciscoBgp4PeerGroup1": ciscoBgp4PeerGroup1,
       "ciscoBgp4NotificationsGroup1": ciscoBgp4NotificationsGroup1,
       "ciscoBgp4Peer2Group": ciscoBgp4Peer2Group,
       "ciscoBgp4Peer2NotificationsGroup": ciscoBgp4Peer2NotificationsGroup,
       "ciscoBgp4GlobalGroup": ciscoBgp4GlobalGroup}
)
