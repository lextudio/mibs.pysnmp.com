# SNMP MIB module (RADLAN-BGP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-BGP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:41 2024
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

(bgp4PathAttrEntry,
 bgp4PathAttrIpAddrPrefix,
 bgp4PathAttrIpAddrPrefixLen,
 bgp4PathAttrPeer,
 bgpPeerEntry,
 bgpPeerRemoteAddr) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgp4PathAttrEntry",
    "bgp4PathAttrIpAddrPrefix",
    "bgp4PathAttrIpAddrPrefixLen",
    "bgp4PathAttrPeer",
    "bgpPeerEntry",
    "bgpPeerRemoteAddr")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlBgp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 71)
)
rlBgp.setRevisions(
        ("2004-06-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlBgpMibVersion_Type = Integer32
_RlBgpMibVersion_Object = MibScalar
rlBgpMibVersion = _RlBgpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 1),
    _RlBgpMibVersion_Type()
)
rlBgpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBgpMibVersion.setStatus("current")
_RlBgpPeersExtTable_Object = MibTable
rlBgpPeersExtTable = _RlBgpPeersExtTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 2)
)
if mibBuilder.loadTexts:
    rlBgpPeersExtTable.setStatus("current")
_RlBgpPeersExtEntry_Object = MibTableRow
rlBgpPeersExtEntry = _RlBgpPeersExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 2, 1)
)
if mibBuilder.loadTexts:
    rlBgpPeersExtEntry.setStatus("current")


class _RlBgpPeersExtRowStatus_Type(RowStatus):
    """Custom type rlBgpPeersExtRowStatus based on RowStatus"""


_RlBgpPeersExtRowStatus_Object = MibTableColumn
rlBgpPeersExtRowStatus = _RlBgpPeersExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 2, 1, 1),
    _RlBgpPeersExtRowStatus_Type()
)
rlBgpPeersExtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpPeersExtRowStatus.setStatus("current")


class _RlBgpPeersExtIsReflectorClient_Type(Integer32):
    """Custom type rlBgpPeersExtIsReflectorClient based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("meshedClient", 2),
          ("nonClient", 0))
    )


_RlBgpPeersExtIsReflectorClient_Type.__name__ = "Integer32"
_RlBgpPeersExtIsReflectorClient_Object = MibTableColumn
rlBgpPeersExtIsReflectorClient = _RlBgpPeersExtIsReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 2, 1, 2),
    _RlBgpPeersExtIsReflectorClient_Type()
)
rlBgpPeersExtIsReflectorClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpPeersExtIsReflectorClient.setStatus("current")


class _RlBgpPeersExtInConfederation_Type(TruthValue):
    """Custom type rlBgpPeersExtInConfederation based on TruthValue"""


_RlBgpPeersExtInConfederation_Object = MibTableColumn
rlBgpPeersExtInConfederation = _RlBgpPeersExtInConfederation_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 2, 1, 3),
    _RlBgpPeersExtInConfederation_Type()
)
rlBgpPeersExtInConfederation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpPeersExtInConfederation.setStatus("current")


class _RlBgpPeersExtRemAS_Type(Integer32):
    """Custom type rlBgpPeersExtRemAS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlBgpPeersExtRemAS_Type.__name__ = "Integer32"
_RlBgpPeersExtRemAS_Object = MibTableColumn
rlBgpPeersExtRemAS = _RlBgpPeersExtRemAS_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 2, 1, 4),
    _RlBgpPeersExtRemAS_Type()
)
rlBgpPeersExtRemAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpPeersExtRemAS.setStatus("current")
_RlBgpClusterId_Type = IpAddress
_RlBgpClusterId_Object = MibScalar
rlBgpClusterId = _RlBgpClusterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 3),
    _RlBgpClusterId_Type()
)
rlBgpClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpClusterId.setStatus("current")


class _RlBgpConfederationId_Type(Integer32):
    """Custom type rlBgpConfederationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlBgpConfederationId_Type.__name__ = "Integer32"
_RlBgpConfederationId_Object = MibScalar
rlBgpConfederationId = _RlBgpConfederationId_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 4),
    _RlBgpConfederationId_Type()
)
rlBgpConfederationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpConfederationId.setStatus("current")


class _RlBgpEnable_Type(Integer32):
    """Custom type rlBgpEnable based on Integer32"""
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


_RlBgpEnable_Type.__name__ = "Integer32"
_RlBgpEnable_Object = MibScalar
rlBgpEnable = _RlBgpEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 5),
    _RlBgpEnable_Type()
)
rlBgpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpEnable.setStatus("current")


class _RlBgpRouteReflectionEnable_Type(Integer32):
    """Custom type rlBgpRouteReflectionEnable based on Integer32"""
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


_RlBgpRouteReflectionEnable_Type.__name__ = "Integer32"
_RlBgpRouteReflectionEnable_Object = MibScalar
rlBgpRouteReflectionEnable = _RlBgpRouteReflectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 6),
    _RlBgpRouteReflectionEnable_Type()
)
rlBgpRouteReflectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpRouteReflectionEnable.setStatus("current")


class _RlBgpASConfederationEnable_Type(Integer32):
    """Custom type rlBgpASConfederationEnable based on Integer32"""
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


_RlBgpASConfederationEnable_Type.__name__ = "Integer32"
_RlBgpASConfederationEnable_Object = MibScalar
rlBgpASConfederationEnable = _RlBgpASConfederationEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 7),
    _RlBgpASConfederationEnable_Type()
)
rlBgpASConfederationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpASConfederationEnable.setStatus("current")


class _RlBgpRouteFlapDampeningEnable_Type(Integer32):
    """Custom type rlBgpRouteFlapDampeningEnable based on Integer32"""
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


_RlBgpRouteFlapDampeningEnable_Type.__name__ = "Integer32"
_RlBgpRouteFlapDampeningEnable_Object = MibScalar
rlBgpRouteFlapDampeningEnable = _RlBgpRouteFlapDampeningEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 8),
    _RlBgpRouteFlapDampeningEnable_Type()
)
rlBgpRouteFlapDampeningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpRouteFlapDampeningEnable.setStatus("current")


class _RlBgpCommunitiesEnable_Type(Integer32):
    """Custom type rlBgpCommunitiesEnable based on Integer32"""
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


_RlBgpCommunitiesEnable_Type.__name__ = "Integer32"
_RlBgpCommunitiesEnable_Object = MibScalar
rlBgpCommunitiesEnable = _RlBgpCommunitiesEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 9),
    _RlBgpCommunitiesEnable_Type()
)
rlBgpCommunitiesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpCommunitiesEnable.setStatus("current")


class _RlBgpCapabilNegotEnable_Type(Integer32):
    """Custom type rlBgpCapabilNegotEnable based on Integer32"""
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


_RlBgpCapabilNegotEnable_Type.__name__ = "Integer32"
_RlBgpCapabilNegotEnable_Object = MibScalar
rlBgpCapabilNegotEnable = _RlBgpCapabilNegotEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 10),
    _RlBgpCapabilNegotEnable_Type()
)
rlBgpCapabilNegotEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpCapabilNegotEnable.setStatus("current")


class _RlBgpMedConf_Type(Integer32):
    """Custom type rlBgpMedConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_RlBgpMedConf_Type.__name__ = "Integer32"
_RlBgpMedConf_Object = MibScalar
rlBgpMedConf = _RlBgpMedConf_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 11),
    _RlBgpMedConf_Type()
)
rlBgpMedConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpMedConf.setStatus("current")


class _RlBgpLocalPrefConf_Type(Integer32):
    """Custom type rlBgpLocalPrefConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_RlBgpLocalPrefConf_Type.__name__ = "Integer32"
_RlBgpLocalPrefConf_Object = MibScalar
rlBgpLocalPrefConf = _RlBgpLocalPrefConf_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 12),
    _RlBgpLocalPrefConf_Type()
)
rlBgpLocalPrefConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpLocalPrefConf.setStatus("current")


class _RlBgpLocalAsConf_Type(Integer32):
    """Custom type rlBgpLocalAsConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlBgpLocalAsConf_Type.__name__ = "Integer32"
_RlBgpLocalAsConf_Object = MibScalar
rlBgpLocalAsConf = _RlBgpLocalAsConf_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 13),
    _RlBgpLocalAsConf_Type()
)
rlBgpLocalAsConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpLocalAsConf.setStatus("current")
_RlBgp4PathAttrExtTable_Object = MibTable
rlBgp4PathAttrExtTable = _RlBgp4PathAttrExtTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 14)
)
if mibBuilder.loadTexts:
    rlBgp4PathAttrExtTable.setStatus("current")
_RlBgp4PathAttrExtEntry_Object = MibTableRow
rlBgp4PathAttrExtEntry = _RlBgp4PathAttrExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 14, 1)
)
if mibBuilder.loadTexts:
    rlBgp4PathAttrExtEntry.setStatus("current")
_RlBgp4PathAttrOriginatorId_Type = IpAddress
_RlBgp4PathAttrOriginatorId_Object = MibTableColumn
rlBgp4PathAttrOriginatorId = _RlBgp4PathAttrOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 14, 1, 1),
    _RlBgp4PathAttrOriginatorId_Type()
)
rlBgp4PathAttrOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBgp4PathAttrOriginatorId.setStatus("current")


class _RlBgp4PathAttrClusterList_Type(OctetString):
    """Custom type rlBgp4PathAttrClusterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_RlBgp4PathAttrClusterList_Type.__name__ = "OctetString"
_RlBgp4PathAttrClusterList_Object = MibTableColumn
rlBgp4PathAttrClusterList = _RlBgp4PathAttrClusterList_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 14, 1, 2),
    _RlBgp4PathAttrClusterList_Type()
)
rlBgp4PathAttrClusterList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBgp4PathAttrClusterList.setStatus("current")


class _RlBgp4PathAttrCommunities_Type(OctetString):
    """Custom type rlBgp4PathAttrCommunities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_RlBgp4PathAttrCommunities_Type.__name__ = "OctetString"
_RlBgp4PathAttrCommunities_Object = MibTableColumn
rlBgp4PathAttrCommunities = _RlBgp4PathAttrCommunities_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 14, 1, 3),
    _RlBgp4PathAttrCommunities_Type()
)
rlBgp4PathAttrCommunities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBgp4PathAttrCommunities.setStatus("current")


class _RlBgpSuppressLimit_Type(Integer32):
    """Custom type rlBgpSuppressLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_RlBgpSuppressLimit_Type.__name__ = "Integer32"
_RlBgpSuppressLimit_Object = MibScalar
rlBgpSuppressLimit = _RlBgpSuppressLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 15),
    _RlBgpSuppressLimit_Type()
)
rlBgpSuppressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpSuppressLimit.setStatus("current")


class _RlBgpReuseLimit_Type(Integer32):
    """Custom type rlBgpReuseLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_RlBgpReuseLimit_Type.__name__ = "Integer32"
_RlBgpReuseLimit_Object = MibScalar
rlBgpReuseLimit = _RlBgpReuseLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 16),
    _RlBgpReuseLimit_Type()
)
rlBgpReuseLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpReuseLimit.setStatus("current")


class _RlBgpHalfLifeTime_Type(Integer32):
    """Custom type rlBgpHalfLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45),
    )


_RlBgpHalfLifeTime_Type.__name__ = "Integer32"
_RlBgpHalfLifeTime_Object = MibScalar
rlBgpHalfLifeTime = _RlBgpHalfLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 17),
    _RlBgpHalfLifeTime_Type()
)
rlBgpHalfLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpHalfLifeTime.setStatus("current")


class _RlBgpMaxSuppressTime_Type(Integer32):
    """Custom type rlBgpMaxSuppressTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RlBgpMaxSuppressTime_Type.__name__ = "Integer32"
_RlBgpMaxSuppressTime_Object = MibScalar
rlBgpMaxSuppressTime = _RlBgpMaxSuppressTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 71, 18),
    _RlBgpMaxSuppressTime_Type()
)
rlBgpMaxSuppressTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBgpMaxSuppressTime.setStatus("current")
bgpPeerEntry.registerAugmentions(
    ("RADLAN-BGP",
     "rlBgpPeersExtEntry")
)
rlBgpPeersExtEntry.setIndexNames(*bgpPeerEntry.getIndexNames())
bgp4PathAttrEntry.registerAugmentions(
    ("RADLAN-BGP",
     "rlBgp4PathAttrExtEntry")
)
rlBgp4PathAttrExtEntry.setIndexNames(*bgp4PathAttrEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-BGP",
    **{"rlBgp": rlBgp,
       "rlBgpMibVersion": rlBgpMibVersion,
       "rlBgpPeersExtTable": rlBgpPeersExtTable,
       "rlBgpPeersExtEntry": rlBgpPeersExtEntry,
       "rlBgpPeersExtRowStatus": rlBgpPeersExtRowStatus,
       "rlBgpPeersExtIsReflectorClient": rlBgpPeersExtIsReflectorClient,
       "rlBgpPeersExtInConfederation": rlBgpPeersExtInConfederation,
       "rlBgpPeersExtRemAS": rlBgpPeersExtRemAS,
       "rlBgpClusterId": rlBgpClusterId,
       "rlBgpConfederationId": rlBgpConfederationId,
       "rlBgpEnable": rlBgpEnable,
       "rlBgpRouteReflectionEnable": rlBgpRouteReflectionEnable,
       "rlBgpASConfederationEnable": rlBgpASConfederationEnable,
       "rlBgpRouteFlapDampeningEnable": rlBgpRouteFlapDampeningEnable,
       "rlBgpCommunitiesEnable": rlBgpCommunitiesEnable,
       "rlBgpCapabilNegotEnable": rlBgpCapabilNegotEnable,
       "rlBgpMedConf": rlBgpMedConf,
       "rlBgpLocalPrefConf": rlBgpLocalPrefConf,
       "rlBgpLocalAsConf": rlBgpLocalAsConf,
       "rlBgp4PathAttrExtTable": rlBgp4PathAttrExtTable,
       "rlBgp4PathAttrExtEntry": rlBgp4PathAttrExtEntry,
       "rlBgp4PathAttrOriginatorId": rlBgp4PathAttrOriginatorId,
       "rlBgp4PathAttrClusterList": rlBgp4PathAttrClusterList,
       "rlBgp4PathAttrCommunities": rlBgp4PathAttrCommunities,
       "rlBgpSuppressLimit": rlBgpSuppressLimit,
       "rlBgpReuseLimit": rlBgpReuseLimit,
       "rlBgpHalfLifeTime": rlBgpHalfLifeTime,
       "rlBgpMaxSuppressTime": rlBgpMaxSuppressTime}
)
