# SNMP MIB module (STN-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-BGP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:04 2024
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

(bgp4PathAttrEntry,) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgp4PathAttrEntry")

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

(stnNotification,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification")

(stnIpRouting,) = mibBuilder.importSymbols(
    "STN-IPROUTING-MIB",
    "stnIpRouting")


# MODULE-IDENTITY

stnBgp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnBgpObjects_ObjectIdentity = ObjectIdentity
stnBgpObjects = _StnBgpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1)
)
_StnBgpRouteAttrTable_Object = MibTable
stnBgpRouteAttrTable = _StnBgpRouteAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 1)
)
if mibBuilder.loadTexts:
    stnBgpRouteAttrTable.setStatus("current")
_StnBgpRouteAttrEntry_Object = MibTableRow
stnBgpRouteAttrEntry = _StnBgpRouteAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 1, 1)
)
stnBgpRouteAttrEntry.setIndexNames(
    (0, "STN-BGP-MIB", "stnBgpRouteAttrId"),
)
if mibBuilder.loadTexts:
    stnBgpRouteAttrEntry.setStatus("current")
_StnBgpRouteAttrId_Type = Integer32
_StnBgpRouteAttrId_Object = MibTableColumn
stnBgpRouteAttrId = _StnBgpRouteAttrId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 1, 1, 1),
    _StnBgpRouteAttrId_Type()
)
stnBgpRouteAttrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpRouteAttrId.setStatus("current")


class _StnBgpRouteAttrASPathSegment_Type(OctetString):
    """Custom type stnBgpRouteAttrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_StnBgpRouteAttrASPathSegment_Type.__name__ = "OctetString"
_StnBgpRouteAttrASPathSegment_Object = MibTableColumn
stnBgpRouteAttrASPathSegment = _StnBgpRouteAttrASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 1, 1, 2),
    _StnBgpRouteAttrASPathSegment_Type()
)
stnBgpRouteAttrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpRouteAttrASPathSegment.setStatus("current")
_StnBgpRouteAttrRefCount_Type = Integer32
_StnBgpRouteAttrRefCount_Object = MibTableColumn
stnBgpRouteAttrRefCount = _StnBgpRouteAttrRefCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 1, 1, 3),
    _StnBgpRouteAttrRefCount_Type()
)
stnBgpRouteAttrRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpRouteAttrRefCount.setStatus("current")
_StnBgpRouteAttrLocPref_Type = Integer32
_StnBgpRouteAttrLocPref_Object = MibTableColumn
stnBgpRouteAttrLocPref = _StnBgpRouteAttrLocPref_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 1, 1, 4),
    _StnBgpRouteAttrLocPref_Type()
)
stnBgpRouteAttrLocPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpRouteAttrLocPref.setStatus("current")
_StnBgpRouteAttrMultiExitDisc_Type = Integer32
_StnBgpRouteAttrMultiExitDisc_Object = MibTableColumn
stnBgpRouteAttrMultiExitDisc = _StnBgpRouteAttrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 1, 1, 5),
    _StnBgpRouteAttrMultiExitDisc_Type()
)
stnBgpRouteAttrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpRouteAttrMultiExitDisc.setStatus("current")


class _StnBgpRouteAttrOrigin_Type(Integer32):
    """Custom type stnBgpRouteAttrOrigin based on Integer32"""
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


_StnBgpRouteAttrOrigin_Type.__name__ = "Integer32"
_StnBgpRouteAttrOrigin_Object = MibTableColumn
stnBgpRouteAttrOrigin = _StnBgpRouteAttrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 1, 1, 6),
    _StnBgpRouteAttrOrigin_Type()
)
stnBgpRouteAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpRouteAttrOrigin.setStatus("current")
_StnBgpRouteAttrNextHop_Type = IpAddress
_StnBgpRouteAttrNextHop_Object = MibTableColumn
stnBgpRouteAttrNextHop = _StnBgpRouteAttrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 1, 1, 7),
    _StnBgpRouteAttrNextHop_Type()
)
stnBgpRouteAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpRouteAttrNextHop.setStatus("current")


class _StnBgpRouteAttrAtomicAggregate_Type(Integer32):
    """Custom type stnBgpRouteAttrAtomicAggregate based on Integer32"""
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


_StnBgpRouteAttrAtomicAggregate_Type.__name__ = "Integer32"
_StnBgpRouteAttrAtomicAggregate_Object = MibTableColumn
stnBgpRouteAttrAtomicAggregate = _StnBgpRouteAttrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 1, 1, 8),
    _StnBgpRouteAttrAtomicAggregate_Type()
)
stnBgpRouteAttrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpRouteAttrAtomicAggregate.setStatus("current")


class _StnBgpRouteAttrAggregatorAS_Type(Integer32):
    """Custom type stnBgpRouteAttrAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnBgpRouteAttrAggregatorAS_Type.__name__ = "Integer32"
_StnBgpRouteAttrAggregatorAS_Object = MibTableColumn
stnBgpRouteAttrAggregatorAS = _StnBgpRouteAttrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 1, 1, 9),
    _StnBgpRouteAttrAggregatorAS_Type()
)
stnBgpRouteAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpRouteAttrAggregatorAS.setStatus("current")
_StnBgpRouteAttrAggregatorAddr_Type = IpAddress
_StnBgpRouteAttrAggregatorAddr_Object = MibTableColumn
stnBgpRouteAttrAggregatorAddr = _StnBgpRouteAttrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 1, 1, 10),
    _StnBgpRouteAttrAggregatorAddr_Type()
)
stnBgpRouteAttrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpRouteAttrAggregatorAddr.setStatus("current")
_StnBgpPrefixCount_Type = Counter32
_StnBgpPrefixCount_Object = MibScalar
stnBgpPrefixCount = _StnBgpPrefixCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 2),
    _StnBgpPrefixCount_Type()
)
stnBgpPrefixCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpPrefixCount.setStatus("current")
_StnBgpPathCount_Type = Counter32
_StnBgpPathCount_Object = MibScalar
stnBgpPathCount = _StnBgpPathCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 3),
    _StnBgpPathCount_Type()
)
stnBgpPathCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpPathCount.setStatus("current")
_StnBgpSelectedPathCount_Type = Counter32
_StnBgpSelectedPathCount_Object = MibScalar
stnBgpSelectedPathCount = _StnBgpSelectedPathCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 4),
    _StnBgpSelectedPathCount_Type()
)
stnBgpSelectedPathCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpSelectedPathCount.setStatus("current")
_StnBgpPathAttributeCount_Type = Counter32
_StnBgpPathAttributeCount_Object = MibScalar
stnBgpPathAttributeCount = _StnBgpPathAttributeCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 5),
    _StnBgpPathAttributeCount_Type()
)
stnBgpPathAttributeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpPathAttributeCount.setStatus("current")
_StnBgpPathAttributeTlvLength_Type = Counter32
_StnBgpPathAttributeTlvLength_Object = MibScalar
stnBgpPathAttributeTlvLength = _StnBgpPathAttributeTlvLength_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 6),
    _StnBgpPathAttributeTlvLength_Type()
)
stnBgpPathAttributeTlvLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgpPathAttributeTlvLength.setStatus("current")
_StnBgp4PathAttrTable_Object = MibTable
stnBgp4PathAttrTable = _StnBgp4PathAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 7)
)
if mibBuilder.loadTexts:
    stnBgp4PathAttrTable.setStatus("current")
_StnBgp4PathAttrEntry_Object = MibTableRow
stnBgp4PathAttrEntry = _StnBgp4PathAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 7, 1)
)
if mibBuilder.loadTexts:
    stnBgp4PathAttrEntry.setStatus("current")


class _StnBgp4PathAttrCommunities_Type(OctetString):
    """Custom type stnBgp4PathAttrCommunities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StnBgp4PathAttrCommunities_Type.__name__ = "OctetString"
_StnBgp4PathAttrCommunities_Object = MibTableColumn
stnBgp4PathAttrCommunities = _StnBgp4PathAttrCommunities_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 7, 1, 1),
    _StnBgp4PathAttrCommunities_Type()
)
stnBgp4PathAttrCommunities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgp4PathAttrCommunities.setStatus("current")
_StnBgp4PathAttrWeight_Type = Integer32
_StnBgp4PathAttrWeight_Object = MibTableColumn
stnBgp4PathAttrWeight = _StnBgp4PathAttrWeight_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 7, 1, 2),
    _StnBgp4PathAttrWeight_Type()
)
stnBgp4PathAttrWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgp4PathAttrWeight.setStatus("current")


class _StnBgp4PathAttrImported_Type(Integer32):
    """Custom type stnBgp4PathAttrImported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_StnBgp4PathAttrImported_Type.__name__ = "Integer32"
_StnBgp4PathAttrImported_Object = MibTableColumn
stnBgp4PathAttrImported = _StnBgp4PathAttrImported_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5, 1, 7, 1, 3),
    _StnBgp4PathAttrImported_Type()
)
stnBgp4PathAttrImported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnBgp4PathAttrImported.setStatus("current")
bgp4PathAttrEntry.registerAugmentions(
    ("STN-BGP-MIB",
     "stnBgp4PathAttrEntry")
)
stnBgp4PathAttrEntry.setIndexNames(*bgp4PathAttrEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-BGP-MIB",
    **{"stnBgp": stnBgp,
       "stnBgpObjects": stnBgpObjects,
       "stnBgpRouteAttrTable": stnBgpRouteAttrTable,
       "stnBgpRouteAttrEntry": stnBgpRouteAttrEntry,
       "stnBgpRouteAttrId": stnBgpRouteAttrId,
       "stnBgpRouteAttrASPathSegment": stnBgpRouteAttrASPathSegment,
       "stnBgpRouteAttrRefCount": stnBgpRouteAttrRefCount,
       "stnBgpRouteAttrLocPref": stnBgpRouteAttrLocPref,
       "stnBgpRouteAttrMultiExitDisc": stnBgpRouteAttrMultiExitDisc,
       "stnBgpRouteAttrOrigin": stnBgpRouteAttrOrigin,
       "stnBgpRouteAttrNextHop": stnBgpRouteAttrNextHop,
       "stnBgpRouteAttrAtomicAggregate": stnBgpRouteAttrAtomicAggregate,
       "stnBgpRouteAttrAggregatorAS": stnBgpRouteAttrAggregatorAS,
       "stnBgpRouteAttrAggregatorAddr": stnBgpRouteAttrAggregatorAddr,
       "stnBgpPrefixCount": stnBgpPrefixCount,
       "stnBgpPathCount": stnBgpPathCount,
       "stnBgpSelectedPathCount": stnBgpSelectedPathCount,
       "stnBgpPathAttributeCount": stnBgpPathAttributeCount,
       "stnBgpPathAttributeTlvLength": stnBgpPathAttributeTlvLength,
       "stnBgp4PathAttrTable": stnBgp4PathAttrTable,
       "stnBgp4PathAttrEntry": stnBgp4PathAttrEntry,
       "stnBgp4PathAttrCommunities": stnBgp4PathAttrCommunities,
       "stnBgp4PathAttrWeight": stnBgp4PathAttrWeight,
       "stnBgp4PathAttrImported": stnBgp4PathAttrImported}
)
