# SNMP MIB module (CACHE-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CACHE-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:19 2024
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
 enterprises,
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
    "enterprises",
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

_IbmCacheServer_ObjectIdentity = ObjectIdentity
ibmCacheServer = _IbmCacheServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8)
)
_IbmcacheserverCore_ObjectIdentity = ObjectIdentity
ibmcacheserverCore = _IbmcacheserverCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 1)
)
_IbmcacheserverCoreActivePartitions_Type = Gauge32
_IbmcacheserverCoreActivePartitions_Object = MibScalar
ibmcacheserverCoreActivePartitions = _IbmcacheserverCoreActivePartitions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 1, 1),
    _IbmcacheserverCoreActivePartitions_Type()
)
ibmcacheserverCoreActivePartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverCoreActivePartitions.setStatus("mandatory")


class _IbmcacheserverCoreECCPort_Type(Integer32):
    """Custom type ibmcacheserverCoreECCPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmcacheserverCoreECCPort_Type.__name__ = "Integer32"
_IbmcacheserverCoreECCPort_Object = MibScalar
ibmcacheserverCoreECCPort = _IbmcacheserverCoreECCPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 1, 2),
    _IbmcacheserverCoreECCPort_Type()
)
ibmcacheserverCoreECCPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverCoreECCPort.setStatus("mandatory")
_IbmcacheserverPartition_ObjectIdentity = ObjectIdentity
ibmcacheserverPartition = _IbmcacheserverPartition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2)
)
_IbmcacheserverPartitionTable_Object = MibTable
ibmcacheserverPartitionTable = _IbmcacheserverPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1)
)
if mibBuilder.loadTexts:
    ibmcacheserverPartitionTable.setStatus("mandatory")
_IbmcacheserverPartitionEntry_Object = MibTableRow
ibmcacheserverPartitionEntry = _IbmcacheserverPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1)
)
ibmcacheserverPartitionEntry.setIndexNames(
    (0, "CACHE-SERVER-MIB", "ibmcacheserverPartitionIndex"),
)
if mibBuilder.loadTexts:
    ibmcacheserverPartitionEntry.setStatus("mandatory")
_IbmcacheserverPartitionIndex_Type = Integer32
_IbmcacheserverPartitionIndex_Object = MibTableColumn
ibmcacheserverPartitionIndex = _IbmcacheserverPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 1),
    _IbmcacheserverPartitionIndex_Type()
)
ibmcacheserverPartitionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionIndex.setStatus("mandatory")


class _IbmcacheserverPartitionCacheControl_Type(Integer32):
    """Custom type ibmcacheserverPartitionCacheControl based on Integer32"""
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


_IbmcacheserverPartitionCacheControl_Type.__name__ = "Integer32"
_IbmcacheserverPartitionCacheControl_Object = MibTableColumn
ibmcacheserverPartitionCacheControl = _IbmcacheserverPartitionCacheControl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 2),
    _IbmcacheserverPartitionCacheControl_Type()
)
ibmcacheserverPartitionCacheControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionCacheControl.setStatus("mandatory")


class _IbmcacheserverPartitionCacheTransparent_Type(Integer32):
    """Custom type ibmcacheserverPartitionCacheTransparent based on Integer32"""
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


_IbmcacheserverPartitionCacheTransparent_Type.__name__ = "Integer32"
_IbmcacheserverPartitionCacheTransparent_Object = MibTableColumn
ibmcacheserverPartitionCacheTransparent = _IbmcacheserverPartitionCacheTransparent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 3),
    _IbmcacheserverPartitionCacheTransparent_Type()
)
ibmcacheserverPartitionCacheTransparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionCacheTransparent.setStatus("mandatory")


class _IbmcacheserverPartitionUseHTTPCacheHdrs_Type(Integer32):
    """Custom type ibmcacheserverPartitionUseHTTPCacheHdrs based on Integer32"""
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


_IbmcacheserverPartitionUseHTTPCacheHdrs_Type.__name__ = "Integer32"
_IbmcacheserverPartitionUseHTTPCacheHdrs_Object = MibTableColumn
ibmcacheserverPartitionUseHTTPCacheHdrs = _IbmcacheserverPartitionUseHTTPCacheHdrs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 4),
    _IbmcacheserverPartitionUseHTTPCacheHdrs_Type()
)
ibmcacheserverPartitionUseHTTPCacheHdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionUseHTTPCacheHdrs.setStatus("mandatory")


class _IbmcacheserverPartitionCacheDynamic_Type(Integer32):
    """Custom type ibmcacheserverPartitionCacheDynamic based on Integer32"""
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


_IbmcacheserverPartitionCacheDynamic_Type.__name__ = "Integer32"
_IbmcacheserverPartitionCacheDynamic_Object = MibTableColumn
ibmcacheserverPartitionCacheDynamic = _IbmcacheserverPartitionCacheDynamic_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 5),
    _IbmcacheserverPartitionCacheDynamic_Type()
)
ibmcacheserverPartitionCacheDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionCacheDynamic.setStatus("mandatory")


class _IbmcacheserverPartitionCacheDynamicURL_Type(DisplayString):
    """Custom type ibmcacheserverPartitionCacheDynamicURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_IbmcacheserverPartitionCacheDynamicURL_Type.__name__ = "DisplayString"
_IbmcacheserverPartitionCacheDynamicURL_Object = MibTableColumn
ibmcacheserverPartitionCacheDynamicURL = _IbmcacheserverPartitionCacheDynamicURL_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 6),
    _IbmcacheserverPartitionCacheDynamicURL_Type()
)
ibmcacheserverPartitionCacheDynamicURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionCacheDynamicURL.setStatus("mandatory")


class _IbmcacheserverPartitionCacheImage_Type(Integer32):
    """Custom type ibmcacheserverPartitionCacheImage based on Integer32"""
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


_IbmcacheserverPartitionCacheImage_Type.__name__ = "Integer32"
_IbmcacheserverPartitionCacheImage_Object = MibTableColumn
ibmcacheserverPartitionCacheImage = _IbmcacheserverPartitionCacheImage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 7),
    _IbmcacheserverPartitionCacheImage_Type()
)
ibmcacheserverPartitionCacheImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionCacheImage.setStatus("mandatory")


class _IbmcacheserverPartitionCacheStatic_Type(Integer32):
    """Custom type ibmcacheserverPartitionCacheStatic based on Integer32"""
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


_IbmcacheserverPartitionCacheStatic_Type.__name__ = "Integer32"
_IbmcacheserverPartitionCacheStatic_Object = MibTableColumn
ibmcacheserverPartitionCacheStatic = _IbmcacheserverPartitionCacheStatic_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 8),
    _IbmcacheserverPartitionCacheStatic_Type()
)
ibmcacheserverPartitionCacheStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionCacheStatic.setStatus("mandatory")
_IbmcacheserverPartitionMaxSize_Type = Integer32
_IbmcacheserverPartitionMaxSize_Object = MibTableColumn
ibmcacheserverPartitionMaxSize = _IbmcacheserverPartitionMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 9),
    _IbmcacheserverPartitionMaxSize_Type()
)
ibmcacheserverPartitionMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionMaxSize.setStatus("mandatory")
_IbmcacheserverPartitionMaxObjects_Type = Integer32
_IbmcacheserverPartitionMaxObjects_Object = MibTableColumn
ibmcacheserverPartitionMaxObjects = _IbmcacheserverPartitionMaxObjects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 10),
    _IbmcacheserverPartitionMaxObjects_Type()
)
ibmcacheserverPartitionMaxObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionMaxObjects.setStatus("mandatory")
_IbmcacheserverPartitionMaxObjectSize_Type = Integer32
_IbmcacheserverPartitionMaxObjectSize_Object = MibTableColumn
ibmcacheserverPartitionMaxObjectSize = _IbmcacheserverPartitionMaxObjectSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 11),
    _IbmcacheserverPartitionMaxObjectSize_Type()
)
ibmcacheserverPartitionMaxObjectSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionMaxObjectSize.setStatus("mandatory")
_IbmcacheserverPartitionDynamicDefaultLifetime_Type = Integer32
_IbmcacheserverPartitionDynamicDefaultLifetime_Object = MibTableColumn
ibmcacheserverPartitionDynamicDefaultLifetime = _IbmcacheserverPartitionDynamicDefaultLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 12),
    _IbmcacheserverPartitionDynamicDefaultLifetime_Type()
)
ibmcacheserverPartitionDynamicDefaultLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionDynamicDefaultLifetime.setStatus("mandatory")
_IbmcacheserverPartitionImageDefaultLifetime_Type = Integer32
_IbmcacheserverPartitionImageDefaultLifetime_Object = MibTableColumn
ibmcacheserverPartitionImageDefaultLifetime = _IbmcacheserverPartitionImageDefaultLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 13),
    _IbmcacheserverPartitionImageDefaultLifetime_Type()
)
ibmcacheserverPartitionImageDefaultLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionImageDefaultLifetime.setStatus("mandatory")
_IbmcacheserverPartitionStaticDefaultLifetime_Type = Integer32
_IbmcacheserverPartitionStaticDefaultLifetime_Object = MibTableColumn
ibmcacheserverPartitionStaticDefaultLifetime = _IbmcacheserverPartitionStaticDefaultLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 14),
    _IbmcacheserverPartitionStaticDefaultLifetime_Type()
)
ibmcacheserverPartitionStaticDefaultLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionStaticDefaultLifetime.setStatus("mandatory")
_IbmcacheserverPartitionCachePurgeInterval_Type = Integer32
_IbmcacheserverPartitionCachePurgeInterval_Object = MibTableColumn
ibmcacheserverPartitionCachePurgeInterval = _IbmcacheserverPartitionCachePurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 15),
    _IbmcacheserverPartitionCachePurgeInterval_Type()
)
ibmcacheserverPartitionCachePurgeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionCachePurgeInterval.setStatus("mandatory")
_IbmcacheserverPartitionNumBytesCurrent_Type = Gauge32
_IbmcacheserverPartitionNumBytesCurrent_Object = MibTableColumn
ibmcacheserverPartitionNumBytesCurrent = _IbmcacheserverPartitionNumBytesCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 16),
    _IbmcacheserverPartitionNumBytesCurrent_Type()
)
ibmcacheserverPartitionNumBytesCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionNumBytesCurrent.setStatus("mandatory")
_IbmcacheserverPartitionNumBytesHiWater_Type = Gauge32
_IbmcacheserverPartitionNumBytesHiWater_Object = MibTableColumn
ibmcacheserverPartitionNumBytesHiWater = _IbmcacheserverPartitionNumBytesHiWater_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 17),
    _IbmcacheserverPartitionNumBytesHiWater_Type()
)
ibmcacheserverPartitionNumBytesHiWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionNumBytesHiWater.setStatus("mandatory")
_IbmcacheserverPartitionNumObjectsCurrent_Type = Gauge32
_IbmcacheserverPartitionNumObjectsCurrent_Object = MibTableColumn
ibmcacheserverPartitionNumObjectsCurrent = _IbmcacheserverPartitionNumObjectsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 18),
    _IbmcacheserverPartitionNumObjectsCurrent_Type()
)
ibmcacheserverPartitionNumObjectsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionNumObjectsCurrent.setStatus("mandatory")
_IbmcacheserverPartitionNumObjectsHiWater_Type = Gauge32
_IbmcacheserverPartitionNumObjectsHiWater_Object = MibTableColumn
ibmcacheserverPartitionNumObjectsHiWater = _IbmcacheserverPartitionNumObjectsHiWater_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 19),
    _IbmcacheserverPartitionNumObjectsHiWater_Type()
)
ibmcacheserverPartitionNumObjectsHiWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionNumObjectsHiWater.setStatus("mandatory")
_IbmcacheserverPartitionHitTotal_Type = Counter32
_IbmcacheserverPartitionHitTotal_Object = MibTableColumn
ibmcacheserverPartitionHitTotal = _IbmcacheserverPartitionHitTotal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 20),
    _IbmcacheserverPartitionHitTotal_Type()
)
ibmcacheserverPartitionHitTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionHitTotal.setStatus("mandatory")
_IbmcacheserverPartitionMissTotal_Type = Counter32
_IbmcacheserverPartitionMissTotal_Object = MibTableColumn
ibmcacheserverPartitionMissTotal = _IbmcacheserverPartitionMissTotal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 21),
    _IbmcacheserverPartitionMissTotal_Type()
)
ibmcacheserverPartitionMissTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionMissTotal.setStatus("mandatory")
_IbmcacheserverPartitionAddInclude_Type = Counter32
_IbmcacheserverPartitionAddInclude_Object = MibTableColumn
ibmcacheserverPartitionAddInclude = _IbmcacheserverPartitionAddInclude_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 22),
    _IbmcacheserverPartitionAddInclude_Type()
)
ibmcacheserverPartitionAddInclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionAddInclude.setStatus("mandatory")
_IbmcacheserverPartitionNotAddCacheOff_Type = Counter32
_IbmcacheserverPartitionNotAddCacheOff_Object = MibTableColumn
ibmcacheserverPartitionNotAddCacheOff = _IbmcacheserverPartitionNotAddCacheOff_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 23),
    _IbmcacheserverPartitionNotAddCacheOff_Type()
)
ibmcacheserverPartitionNotAddCacheOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionNotAddCacheOff.setStatus("mandatory")
_IbmcacheserverPartitionNotAddTooLarge_Type = Counter32
_IbmcacheserverPartitionNotAddTooLarge_Object = MibTableColumn
ibmcacheserverPartitionNotAddTooLarge = _IbmcacheserverPartitionNotAddTooLarge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 24),
    _IbmcacheserverPartitionNotAddTooLarge_Type()
)
ibmcacheserverPartitionNotAddTooLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionNotAddTooLarge.setStatus("mandatory")
_IbmcacheserverPartitionNotAddHTTPHdr_Type = Counter32
_IbmcacheserverPartitionNotAddHTTPHdr_Object = MibTableColumn
ibmcacheserverPartitionNotAddHTTPHdr = _IbmcacheserverPartitionNotAddHTTPHdr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 25),
    _IbmcacheserverPartitionNotAddHTTPHdr_Type()
)
ibmcacheserverPartitionNotAddHTTPHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionNotAddHTTPHdr.setStatus("mandatory")
_IbmcacheserverPartitionNotAddExclude_Type = Counter32
_IbmcacheserverPartitionNotAddExclude_Object = MibTableColumn
ibmcacheserverPartitionNotAddExclude = _IbmcacheserverPartitionNotAddExclude_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 26),
    _IbmcacheserverPartitionNotAddExclude_Type()
)
ibmcacheserverPartitionNotAddExclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionNotAddExclude.setStatus("mandatory")
_IbmcacheserverPartitionNotAddExpire_Type = Counter32
_IbmcacheserverPartitionNotAddExpire_Object = MibTableColumn
ibmcacheserverPartitionNotAddExpire = _IbmcacheserverPartitionNotAddExpire_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 27),
    _IbmcacheserverPartitionNotAddExpire_Type()
)
ibmcacheserverPartitionNotAddExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionNotAddExpire.setStatus("mandatory")
_IbmcacheserverPartitionNotAddImage_Type = Counter32
_IbmcacheserverPartitionNotAddImage_Object = MibTableColumn
ibmcacheserverPartitionNotAddImage = _IbmcacheserverPartitionNotAddImage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 28),
    _IbmcacheserverPartitionNotAddImage_Type()
)
ibmcacheserverPartitionNotAddImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionNotAddImage.setStatus("mandatory")
_IbmcacheserverPartitionNotAddStatic_Type = Counter32
_IbmcacheserverPartitionNotAddStatic_Object = MibTableColumn
ibmcacheserverPartitionNotAddStatic = _IbmcacheserverPartitionNotAddStatic_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 29),
    _IbmcacheserverPartitionNotAddStatic_Type()
)
ibmcacheserverPartitionNotAddStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionNotAddStatic.setStatus("mandatory")
_IbmcacheserverPartitionNotAddDynamic_Type = Counter32
_IbmcacheserverPartitionNotAddDynamic_Object = MibTableColumn
ibmcacheserverPartitionNotAddDynamic = _IbmcacheserverPartitionNotAddDynamic_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 30),
    _IbmcacheserverPartitionNotAddDynamic_Type()
)
ibmcacheserverPartitionNotAddDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionNotAddDynamic.setStatus("mandatory")
_IbmcacheserverPartitionPurgeCacheFull_Type = Counter32
_IbmcacheserverPartitionPurgeCacheFull_Object = MibTableColumn
ibmcacheserverPartitionPurgeCacheFull = _IbmcacheserverPartitionPurgeCacheFull_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 31),
    _IbmcacheserverPartitionPurgeCacheFull_Type()
)
ibmcacheserverPartitionPurgeCacheFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionPurgeCacheFull.setStatus("mandatory")
_IbmcacheserverPartitionPurgeItemStale_Type = Counter32
_IbmcacheserverPartitionPurgeItemStale_Object = MibTableColumn
ibmcacheserverPartitionPurgeItemStale = _IbmcacheserverPartitionPurgeItemStale_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 32),
    _IbmcacheserverPartitionPurgeItemStale_Type()
)
ibmcacheserverPartitionPurgeItemStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionPurgeItemStale.setStatus("mandatory")
_IbmcacheserverPartitionPurgeItemExplicit_Type = Counter32
_IbmcacheserverPartitionPurgeItemExplicit_Object = MibTableColumn
ibmcacheserverPartitionPurgeItemExplicit = _IbmcacheserverPartitionPurgeItemExplicit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 33),
    _IbmcacheserverPartitionPurgeItemExplicit_Type()
)
ibmcacheserverPartitionPurgeItemExplicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverPartitionPurgeItemExplicit.setStatus("mandatory")
_IbmcacheserverURL_ObjectIdentity = ObjectIdentity
ibmcacheserverURL = _IbmcacheserverURL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 3)
)
_IbmcacheserverURLTable_Object = MibTable
ibmcacheserverURLTable = _IbmcacheserverURLTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 3, 1)
)
if mibBuilder.loadTexts:
    ibmcacheserverURLTable.setStatus("mandatory")
_IbmcacheserverURLEntry_Object = MibTableRow
ibmcacheserverURLEntry = _IbmcacheserverURLEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 3, 1, 1)
)
ibmcacheserverURLEntry.setIndexNames(
    (0, "CACHE-SERVER-MIB", "ibmcacheserverPartitionIndex"),
    (0, "CACHE-SERVER-MIB", "ibmcacheserverURLIndex"),
)
if mibBuilder.loadTexts:
    ibmcacheserverURLEntry.setStatus("mandatory")
_IbmcacheserverURLIndex_Type = Integer32
_IbmcacheserverURLIndex_Object = MibTableColumn
ibmcacheserverURLIndex = _IbmcacheserverURLIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 3, 1, 1, 1),
    _IbmcacheserverURLIndex_Type()
)
ibmcacheserverURLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmcacheserverURLIndex.setStatus("mandatory")


class _IbmcacheserverURLContent_Type(Integer32):
    """Custom type ibmcacheserverURLContent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_IbmcacheserverURLContent_Type.__name__ = "Integer32"
_IbmcacheserverURLContent_Object = MibTableColumn
ibmcacheserverURLContent = _IbmcacheserverURLContent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 3, 1, 1, 2),
    _IbmcacheserverURLContent_Type()
)
ibmcacheserverURLContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverURLContent.setStatus("mandatory")


class _IbmcacheserverURLMask_Type(DisplayString):
    """Custom type ibmcacheserverURLMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_IbmcacheserverURLMask_Type.__name__ = "DisplayString"
_IbmcacheserverURLMask_Object = MibTableColumn
ibmcacheserverURLMask = _IbmcacheserverURLMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 3, 1, 1, 3),
    _IbmcacheserverURLMask_Type()
)
ibmcacheserverURLMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverURLMask.setStatus("mandatory")
_IbmcacheserverProxy_ObjectIdentity = ObjectIdentity
ibmcacheserverProxy = _IbmcacheserverProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4)
)
_IbmcacheserverProxyTable_Object = MibTable
ibmcacheserverProxyTable = _IbmcacheserverProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1)
)
if mibBuilder.loadTexts:
    ibmcacheserverProxyTable.setStatus("mandatory")
_IbmcacheserverProxyEntry_Object = MibTableRow
ibmcacheserverProxyEntry = _IbmcacheserverProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1)
)
ibmcacheserverProxyEntry.setIndexNames(
    (0, "CACHE-SERVER-MIB", "ibmcacheserverProxyClusterAddr"),
    (0, "CACHE-SERVER-MIB", "ibmcacheserverProxyPort"),
)
if mibBuilder.loadTexts:
    ibmcacheserverProxyEntry.setStatus("mandatory")
_IbmcacheserverProxyClusterAddr_Type = IpAddress
_IbmcacheserverProxyClusterAddr_Object = MibTableColumn
ibmcacheserverProxyClusterAddr = _IbmcacheserverProxyClusterAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 1),
    _IbmcacheserverProxyClusterAddr_Type()
)
ibmcacheserverProxyClusterAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmcacheserverProxyClusterAddr.setStatus("mandatory")


class _IbmcacheserverProxyPort_Type(Integer32):
    """Custom type ibmcacheserverProxyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmcacheserverProxyPort_Type.__name__ = "Integer32"
_IbmcacheserverProxyPort_Object = MibTableColumn
ibmcacheserverProxyPort = _IbmcacheserverProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 2),
    _IbmcacheserverProxyPort_Type()
)
ibmcacheserverProxyPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmcacheserverProxyPort.setStatus("mandatory")
_IbmcacheserverProxyPartition_Type = Integer32
_IbmcacheserverProxyPartition_Object = MibTableColumn
ibmcacheserverProxyPartition = _IbmcacheserverProxyPartition_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 3),
    _IbmcacheserverProxyPartition_Type()
)
ibmcacheserverProxyPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverProxyPartition.setStatus("mandatory")
_IbmcacheserverProxyClientCount_Type = Gauge32
_IbmcacheserverProxyClientCount_Object = MibTableColumn
ibmcacheserverProxyClientCount = _IbmcacheserverProxyClientCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 4),
    _IbmcacheserverProxyClientCount_Type()
)
ibmcacheserverProxyClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverProxyClientCount.setStatus("mandatory")
_IbmcacheserverProxyServerCount_Type = Gauge32
_IbmcacheserverProxyServerCount_Object = MibTableColumn
ibmcacheserverProxyServerCount = _IbmcacheserverProxyServerCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 5),
    _IbmcacheserverProxyServerCount_Type()
)
ibmcacheserverProxyServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverProxyServerCount.setStatus("mandatory")
_IbmcacheserverProxyClientMaxCount_Type = Gauge32
_IbmcacheserverProxyClientMaxCount_Object = MibTableColumn
ibmcacheserverProxyClientMaxCount = _IbmcacheserverProxyClientMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 6),
    _IbmcacheserverProxyClientMaxCount_Type()
)
ibmcacheserverProxyClientMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverProxyClientMaxCount.setStatus("mandatory")
_IbmcacheserverProxyServerMaxCount_Type = Gauge32
_IbmcacheserverProxyServerMaxCount_Object = MibTableColumn
ibmcacheserverProxyServerMaxCount = _IbmcacheserverProxyServerMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 7),
    _IbmcacheserverProxyServerMaxCount_Type()
)
ibmcacheserverProxyServerMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverProxyServerMaxCount.setStatus("mandatory")
_IbmcacheserverProxyCacheHits_Type = Counter32
_IbmcacheserverProxyCacheHits_Object = MibTableColumn
ibmcacheserverProxyCacheHits = _IbmcacheserverProxyCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 8),
    _IbmcacheserverProxyCacheHits_Type()
)
ibmcacheserverProxyCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverProxyCacheHits.setStatus("mandatory")
_IbmcacheserverProxyCacheMissMethod_Type = Counter32
_IbmcacheserverProxyCacheMissMethod_Object = MibTableColumn
ibmcacheserverProxyCacheMissMethod = _IbmcacheserverProxyCacheMissMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 9),
    _IbmcacheserverProxyCacheMissMethod_Type()
)
ibmcacheserverProxyCacheMissMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverProxyCacheMissMethod.setStatus("mandatory")
_IbmcacheserverProxyCacheMissStorage_Type = Counter32
_IbmcacheserverProxyCacheMissStorage_Object = MibTableColumn
ibmcacheserverProxyCacheMissStorage = _IbmcacheserverProxyCacheMissStorage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 10),
    _IbmcacheserverProxyCacheMissStorage_Type()
)
ibmcacheserverProxyCacheMissStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverProxyCacheMissStorage.setStatus("mandatory")
_IbmcacheserverProxyCacheMissNotInCache_Type = Counter32
_IbmcacheserverProxyCacheMissNotInCache_Object = MibTableColumn
ibmcacheserverProxyCacheMissNotInCache = _IbmcacheserverProxyCacheMissNotInCache_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 11),
    _IbmcacheserverProxyCacheMissNotInCache_Type()
)
ibmcacheserverProxyCacheMissNotInCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverProxyCacheMissNotInCache.setStatus("mandatory")
_IbmcacheserverProxyCacheMissHeaders_Type = Counter32
_IbmcacheserverProxyCacheMissHeaders_Object = MibTableColumn
ibmcacheserverProxyCacheMissHeaders = _IbmcacheserverProxyCacheMissHeaders_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 12),
    _IbmcacheserverProxyCacheMissHeaders_Type()
)
ibmcacheserverProxyCacheMissHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmcacheserverProxyCacheMissHeaders.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CACHE-SERVER-MIB",
    **{"ibmCacheServer": ibmCacheServer,
       "ibmcacheserverCore": ibmcacheserverCore,
       "ibmcacheserverCoreActivePartitions": ibmcacheserverCoreActivePartitions,
       "ibmcacheserverCoreECCPort": ibmcacheserverCoreECCPort,
       "ibmcacheserverPartition": ibmcacheserverPartition,
       "ibmcacheserverPartitionTable": ibmcacheserverPartitionTable,
       "ibmcacheserverPartitionEntry": ibmcacheserverPartitionEntry,
       "ibmcacheserverPartitionIndex": ibmcacheserverPartitionIndex,
       "ibmcacheserverPartitionCacheControl": ibmcacheserverPartitionCacheControl,
       "ibmcacheserverPartitionCacheTransparent": ibmcacheserverPartitionCacheTransparent,
       "ibmcacheserverPartitionUseHTTPCacheHdrs": ibmcacheserverPartitionUseHTTPCacheHdrs,
       "ibmcacheserverPartitionCacheDynamic": ibmcacheserverPartitionCacheDynamic,
       "ibmcacheserverPartitionCacheDynamicURL": ibmcacheserverPartitionCacheDynamicURL,
       "ibmcacheserverPartitionCacheImage": ibmcacheserverPartitionCacheImage,
       "ibmcacheserverPartitionCacheStatic": ibmcacheserverPartitionCacheStatic,
       "ibmcacheserverPartitionMaxSize": ibmcacheserverPartitionMaxSize,
       "ibmcacheserverPartitionMaxObjects": ibmcacheserverPartitionMaxObjects,
       "ibmcacheserverPartitionMaxObjectSize": ibmcacheserverPartitionMaxObjectSize,
       "ibmcacheserverPartitionDynamicDefaultLifetime": ibmcacheserverPartitionDynamicDefaultLifetime,
       "ibmcacheserverPartitionImageDefaultLifetime": ibmcacheserverPartitionImageDefaultLifetime,
       "ibmcacheserverPartitionStaticDefaultLifetime": ibmcacheserverPartitionStaticDefaultLifetime,
       "ibmcacheserverPartitionCachePurgeInterval": ibmcacheserverPartitionCachePurgeInterval,
       "ibmcacheserverPartitionNumBytesCurrent": ibmcacheserverPartitionNumBytesCurrent,
       "ibmcacheserverPartitionNumBytesHiWater": ibmcacheserverPartitionNumBytesHiWater,
       "ibmcacheserverPartitionNumObjectsCurrent": ibmcacheserverPartitionNumObjectsCurrent,
       "ibmcacheserverPartitionNumObjectsHiWater": ibmcacheserverPartitionNumObjectsHiWater,
       "ibmcacheserverPartitionHitTotal": ibmcacheserverPartitionHitTotal,
       "ibmcacheserverPartitionMissTotal": ibmcacheserverPartitionMissTotal,
       "ibmcacheserverPartitionAddInclude": ibmcacheserverPartitionAddInclude,
       "ibmcacheserverPartitionNotAddCacheOff": ibmcacheserverPartitionNotAddCacheOff,
       "ibmcacheserverPartitionNotAddTooLarge": ibmcacheserverPartitionNotAddTooLarge,
       "ibmcacheserverPartitionNotAddHTTPHdr": ibmcacheserverPartitionNotAddHTTPHdr,
       "ibmcacheserverPartitionNotAddExclude": ibmcacheserverPartitionNotAddExclude,
       "ibmcacheserverPartitionNotAddExpire": ibmcacheserverPartitionNotAddExpire,
       "ibmcacheserverPartitionNotAddImage": ibmcacheserverPartitionNotAddImage,
       "ibmcacheserverPartitionNotAddStatic": ibmcacheserverPartitionNotAddStatic,
       "ibmcacheserverPartitionNotAddDynamic": ibmcacheserverPartitionNotAddDynamic,
       "ibmcacheserverPartitionPurgeCacheFull": ibmcacheserverPartitionPurgeCacheFull,
       "ibmcacheserverPartitionPurgeItemStale": ibmcacheserverPartitionPurgeItemStale,
       "ibmcacheserverPartitionPurgeItemExplicit": ibmcacheserverPartitionPurgeItemExplicit,
       "ibmcacheserverURL": ibmcacheserverURL,
       "ibmcacheserverURLTable": ibmcacheserverURLTable,
       "ibmcacheserverURLEntry": ibmcacheserverURLEntry,
       "ibmcacheserverURLIndex": ibmcacheserverURLIndex,
       "ibmcacheserverURLContent": ibmcacheserverURLContent,
       "ibmcacheserverURLMask": ibmcacheserverURLMask,
       "ibmcacheserverProxy": ibmcacheserverProxy,
       "ibmcacheserverProxyTable": ibmcacheserverProxyTable,
       "ibmcacheserverProxyEntry": ibmcacheserverProxyEntry,
       "ibmcacheserverProxyClusterAddr": ibmcacheserverProxyClusterAddr,
       "ibmcacheserverProxyPort": ibmcacheserverProxyPort,
       "ibmcacheserverProxyPartition": ibmcacheserverProxyPartition,
       "ibmcacheserverProxyClientCount": ibmcacheserverProxyClientCount,
       "ibmcacheserverProxyServerCount": ibmcacheserverProxyServerCount,
       "ibmcacheserverProxyClientMaxCount": ibmcacheserverProxyClientMaxCount,
       "ibmcacheserverProxyServerMaxCount": ibmcacheserverProxyServerMaxCount,
       "ibmcacheserverProxyCacheHits": ibmcacheserverProxyCacheHits,
       "ibmcacheserverProxyCacheMissMethod": ibmcacheserverProxyCacheMissMethod,
       "ibmcacheserverProxyCacheMissStorage": ibmcacheserverProxyCacheMissStorage,
       "ibmcacheserverProxyCacheMissNotInCache": ibmcacheserverProxyCacheMissNotInCache,
       "ibmcacheserverProxyCacheMissHeaders": ibmcacheserverProxyCacheMissHeaders}
)
