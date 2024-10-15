# SNMP MIB module (BIANCA-BRICK-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-DNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:24 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Biboip_ObjectIdentity = ObjectIdentity
biboip = _Biboip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5)
)
_IpDns_ObjectIdentity = ObjectIdentity
ipDns = _IpDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20)
)


class _IpDnsDhcpAssign_Type(Integer32):
    """Custom type ipDnsDhcpAssign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 3),
          ("none", 1),
          ("self", 2))
    )


_IpDnsDhcpAssign_Type.__name__ = "Integer32"
_IpDnsDhcpAssign_Object = MibScalar
ipDnsDhcpAssign = _IpDnsDhcpAssign_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 1),
    _IpDnsDhcpAssign_Type()
)
ipDnsDhcpAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsDhcpAssign.setStatus("mandatory")


class _IpDnsIpcpAssign_Type(Integer32):
    """Custom type ipDnsIpcpAssign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 3),
          ("none", 1),
          ("self", 2))
    )


_IpDnsIpcpAssign_Type.__name__ = "Integer32"
_IpDnsIpcpAssign_Object = MibScalar
ipDnsIpcpAssign = _IpDnsIpcpAssign_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 2),
    _IpDnsIpcpAssign_Type()
)
ipDnsIpcpAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsIpcpAssign.setStatus("mandatory")


class _IpDnsUsePosCache_Type(Integer32):
    """Custom type ipDnsUsePosCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpDnsUsePosCache_Type.__name__ = "Integer32"
_IpDnsUsePosCache_Object = MibScalar
ipDnsUsePosCache = _IpDnsUsePosCache_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 3),
    _IpDnsUsePosCache_Type()
)
ipDnsUsePosCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsUsePosCache.setStatus("mandatory")


class _IpDnsUseNegCache_Type(Integer32):
    """Custom type ipDnsUseNegCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpDnsUseNegCache_Type.__name__ = "Integer32"
_IpDnsUseNegCache_Object = MibScalar
ipDnsUseNegCache = _IpDnsUseNegCache_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 4),
    _IpDnsUseNegCache_Type()
)
ipDnsUseNegCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsUseNegCache.setStatus("mandatory")
_IpDnsMaxCacheSize_Type = Integer32
_IpDnsMaxCacheSize_Object = MibScalar
ipDnsMaxCacheSize = _IpDnsMaxCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 5),
    _IpDnsMaxCacheSize_Type()
)
ipDnsMaxCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsMaxCacheSize.setStatus("mandatory")
_IpDnsPositiveTtl_Type = Integer32
_IpDnsPositiveTtl_Object = MibScalar
ipDnsPositiveTtl = _IpDnsPositiveTtl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 6),
    _IpDnsPositiveTtl_Type()
)
ipDnsPositiveTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsPositiveTtl.setStatus("mandatory")
_IpDnsNegativeTtl_Type = Integer32
_IpDnsNegativeTtl_Object = MibScalar
ipDnsNegativeTtl = _IpDnsNegativeTtl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 7),
    _IpDnsNegativeTtl_Type()
)
ipDnsNegativeTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsNegativeTtl.setStatus("mandatory")
_IpDnsDefaultIfIndex_Type = Integer32
_IpDnsDefaultIfIndex_Object = MibScalar
ipDnsDefaultIfIndex = _IpDnsDefaultIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 8),
    _IpDnsDefaultIfIndex_Type()
)
ipDnsDefaultIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsDefaultIfIndex.setStatus("mandatory")
_IpDnsNumReceives_Type = Integer32
_IpDnsNumReceives_Object = MibScalar
ipDnsNumReceives = _IpDnsNumReceives_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 9),
    _IpDnsNumReceives_Type()
)
ipDnsNumReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDnsNumReceives.setStatus("mandatory")
_IpDnsNumInvalids_Type = Integer32
_IpDnsNumInvalids_Object = MibScalar
ipDnsNumInvalids = _IpDnsNumInvalids_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 10),
    _IpDnsNumInvalids_Type()
)
ipDnsNumInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDnsNumInvalids.setStatus("mandatory")
_IpDnsNumRequests_Type = Integer32
_IpDnsNumRequests_Object = MibScalar
ipDnsNumRequests = _IpDnsNumRequests_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 11),
    _IpDnsNumRequests_Type()
)
ipDnsNumRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDnsNumRequests.setStatus("mandatory")
_IpDnsNumCacheHits_Type = Integer32
_IpDnsNumCacheHits_Object = MibScalar
ipDnsNumCacheHits = _IpDnsNumCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 12),
    _IpDnsNumCacheHits_Type()
)
ipDnsNumCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDnsNumCacheHits.setStatus("mandatory")
_IpDnsNumForwards_Type = Integer32
_IpDnsNumForwards_Object = MibScalar
ipDnsNumForwards = _IpDnsNumForwards_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 13),
    _IpDnsNumForwards_Type()
)
ipDnsNumForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDnsNumForwards.setStatus("mandatory")
_IpDnsNumOks_Type = Integer32
_IpDnsNumOks_Object = MibScalar
ipDnsNumOks = _IpDnsNumOks_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 14),
    _IpDnsNumOks_Type()
)
ipDnsNumOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDnsNumOks.setStatus("mandatory")
_IpDnsNumFails_Type = Integer32
_IpDnsNumFails_Object = MibScalar
ipDnsNumFails = _IpDnsNumFails_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 15),
    _IpDnsNumFails_Type()
)
ipDnsNumFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDnsNumFails.setStatus("mandatory")
_IpDnsTable_Object = MibTable
ipDnsTable = _IpDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 16)
)
if mibBuilder.loadTexts:
    ipDnsTable.setStatus("mandatory")
_IpDnsEntry_Object = MibTableRow
ipDnsEntry = _IpDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 16, 1)
)
ipDnsEntry.setIndexNames(
    (0, "BIANCA-BRICK-DNS-MIB", "ipDnsEntName"),
)
if mibBuilder.loadTexts:
    ipDnsEntry.setStatus("mandatory")
_IpDnsEntName_Type = DisplayString
_IpDnsEntName_Object = MibTableColumn
ipDnsEntName = _IpDnsEntName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 16, 1, 1),
    _IpDnsEntName_Type()
)
ipDnsEntName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsEntName.setStatus("mandatory")
_IpDnsEntIpaddr_Type = IpAddress
_IpDnsEntIpaddr_Object = MibTableColumn
ipDnsEntIpaddr = _IpDnsEntIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 16, 1, 2),
    _IpDnsEntIpaddr_Type()
)
ipDnsEntIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsEntIpaddr.setStatus("mandatory")
_IpDnsEntIfIndex_Type = Integer32
_IpDnsEntIfIndex_Object = MibTableColumn
ipDnsEntIfIndex = _IpDnsEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 16, 1, 3),
    _IpDnsEntIfIndex_Type()
)
ipDnsEntIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsEntIfIndex.setStatus("mandatory")


class _IpDnsEntResponse_Type(Integer32):
    """Custom type ipDnsEntResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("negative", 2),
          ("positive", 3))
    )


_IpDnsEntResponse_Type.__name__ = "Integer32"
_IpDnsEntResponse_Object = MibTableColumn
ipDnsEntResponse = _IpDnsEntResponse_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 16, 1, 4),
    _IpDnsEntResponse_Type()
)
ipDnsEntResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsEntResponse.setStatus("mandatory")


class _IpDnsEntStatic_Type(Integer32):
    """Custom type ipDnsEntStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("no", 1),
          ("yes", 2))
    )


_IpDnsEntStatic_Type.__name__ = "Integer32"
_IpDnsEntStatic_Object = MibTableColumn
ipDnsEntStatic = _IpDnsEntStatic_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 16, 1, 5),
    _IpDnsEntStatic_Type()
)
ipDnsEntStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsEntStatic.setStatus("mandatory")
_IpDnsEntTtl_Type = Integer32
_IpDnsEntTtl_Object = MibTableColumn
ipDnsEntTtl = _IpDnsEntTtl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 16, 1, 6),
    _IpDnsEntTtl_Type()
)
ipDnsEntTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsEntTtl.setStatus("mandatory")
_IpDnsEntLru_Type = Integer32
_IpDnsEntLru_Object = MibTableColumn
ipDnsEntLru = _IpDnsEntLru_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 16, 1, 7),
    _IpDnsEntLru_Type()
)
ipDnsEntLru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsEntLru.setStatus("mandatory")
_IpDnsEntHash_Type = Integer32
_IpDnsEntHash_Object = MibTableColumn
ipDnsEntHash = _IpDnsEntHash_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 16, 1, 8),
    _IpDnsEntHash_Type()
)
ipDnsEntHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDnsEntHash.setStatus("mandatory")
_IpDnsEntRefCount_Type = Integer32
_IpDnsEntRefCount_Object = MibTableColumn
ipDnsEntRefCount = _IpDnsEntRefCount_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 16, 1, 9),
    _IpDnsEntRefCount_Type()
)
ipDnsEntRefCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsEntRefCount.setStatus("mandatory")


class _IpDnsDynamicGlobals_Type(Integer32):
    """Custom type ipDnsDynamicGlobals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IpDnsDynamicGlobals_Type.__name__ = "Integer32"
_IpDnsDynamicGlobals_Object = MibScalar
ipDnsDynamicGlobals = _IpDnsDynamicGlobals_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 20, 17),
    _IpDnsDynamicGlobals_Type()
)
ipDnsDynamicGlobals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDnsDynamicGlobals.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-DNS-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "biboip": biboip,
       "ipDns": ipDns,
       "ipDnsDhcpAssign": ipDnsDhcpAssign,
       "ipDnsIpcpAssign": ipDnsIpcpAssign,
       "ipDnsUsePosCache": ipDnsUsePosCache,
       "ipDnsUseNegCache": ipDnsUseNegCache,
       "ipDnsMaxCacheSize": ipDnsMaxCacheSize,
       "ipDnsPositiveTtl": ipDnsPositiveTtl,
       "ipDnsNegativeTtl": ipDnsNegativeTtl,
       "ipDnsDefaultIfIndex": ipDnsDefaultIfIndex,
       "ipDnsNumReceives": ipDnsNumReceives,
       "ipDnsNumInvalids": ipDnsNumInvalids,
       "ipDnsNumRequests": ipDnsNumRequests,
       "ipDnsNumCacheHits": ipDnsNumCacheHits,
       "ipDnsNumForwards": ipDnsNumForwards,
       "ipDnsNumOks": ipDnsNumOks,
       "ipDnsNumFails": ipDnsNumFails,
       "ipDnsTable": ipDnsTable,
       "ipDnsEntry": ipDnsEntry,
       "ipDnsEntName": ipDnsEntName,
       "ipDnsEntIpaddr": ipDnsEntIpaddr,
       "ipDnsEntIfIndex": ipDnsEntIfIndex,
       "ipDnsEntResponse": ipDnsEntResponse,
       "ipDnsEntStatic": ipDnsEntStatic,
       "ipDnsEntTtl": ipDnsEntTtl,
       "ipDnsEntLru": ipDnsEntLru,
       "ipDnsEntHash": ipDnsEntHash,
       "ipDnsEntRefCount": ipDnsEntRefCount,
       "ipDnsDynamicGlobals": ipDnsDynamicGlobals}
)
