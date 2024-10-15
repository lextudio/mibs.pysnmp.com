# SNMP MIB module (DX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:34:01 2024
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

dxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3327, 21)
)
dxMIB.setRevisions(
        ("2005-11-08 15:36",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ETrustDirectory_ObjectIdentity = ObjectIdentity
eTrustDirectory = _ETrustDirectory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3327)
)
_Dx_MULTIWRITE_MIB_ObjectIdentity = ObjectIdentity
dx_MULTIWRITE_MIB = _Dx_MULTIWRITE_MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3327, 21, 1)
)
_DxMWTable_Object = MibTable
dxMWTable = _DxMWTable_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 1, 1)
)
if mibBuilder.loadTexts:
    dxMWTable.setStatus("current")
_DxMWEntry_Object = MibTableRow
dxMWEntry = _DxMWEntry_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 1, 1, 1)
)
dxMWEntry.setIndexNames(
    (0, "DX-MIB", "dxMWIndex"),
)
if mibBuilder.loadTexts:
    dxMWEntry.setStatus("current")


class _DxMWIndex_Type(Integer32):
    """Custom type dxMWIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DxMWIndex_Type.__name__ = "Integer32"
_DxMWIndex_Object = MibTableColumn
dxMWIndex = _DxMWIndex_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 1, 1, 1, 1),
    _DxMWIndex_Type()
)
dxMWIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxMWIndex.setStatus("current")
_DxRemoteDsaName_Type = OctetString
_DxRemoteDsaName_Object = MibTableColumn
dxRemoteDsaName = _DxRemoteDsaName_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 1, 1, 1, 2),
    _DxRemoteDsaName_Type()
)
dxRemoteDsaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxRemoteDsaName.setStatus("current")
_DxMWQueueLength_Type = Gauge32
_DxMWQueueLength_Object = MibTableColumn
dxMWQueueLength = _DxMWQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 1, 1, 1, 3),
    _DxMWQueueLength_Type()
)
dxMWQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxMWQueueLength.setStatus("current")


class _DxMWStatus_Type(Integer32):
    """Custom type dxMWStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disp-failed", 6),
          ("failed", 2),
          ("failed-no-dsa", 3),
          ("failed-sent", 9),
          ("internal-error", 0),
          ("non-existent", 4),
          ("ok", 1),
          ("q-purged", 8),
          ("recovering", 5),
          ("wait-disp", 7))
    )


_DxMWStatus_Type.__name__ = "Integer32"
_DxMWStatus_Object = MibTableColumn
dxMWStatus = _DxMWStatus_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 1, 1, 1, 4),
    _DxMWStatus_Type()
)
dxMWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxMWStatus.setStatus("current")
_DxMWPendingRemote_Type = Gauge32
_DxMWPendingRemote_Object = MibTableColumn
dxMWPendingRemote = _DxMWPendingRemote_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 1, 1, 1, 5),
    _DxMWPendingRemote_Type()
)
dxMWPendingRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxMWPendingRemote.setStatus("current")
_DxMWConfirmedLocal_Type = Gauge32
_DxMWConfirmedLocal_Object = MibTableColumn
dxMWConfirmedLocal = _DxMWConfirmedLocal_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 1, 1, 1, 6),
    _DxMWConfirmedLocal_Type()
)
dxMWConfirmedLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxMWConfirmedLocal.setStatus("current")
_Dx_STATISTICS_MIB_ObjectIdentity = ObjectIdentity
dx_STATISTICS_MIB = _Dx_STATISTICS_MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3327, 21, 2)
)
_DxStatsAssocs_Type = Gauge32
_DxStatsAssocs_Object = MibScalar
dxStatsAssocs = _DxStatsAssocs_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 2, 1),
    _DxStatsAssocs_Type()
)
dxStatsAssocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxStatsAssocs.setStatus("current")
_DxStatsNilCredit_Type = Counter32
_DxStatsNilCredit_Object = MibScalar
dxStatsNilCredit = _DxStatsNilCredit_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 2, 2),
    _DxStatsNilCredit_Type()
)
dxStatsNilCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxStatsNilCredit.setStatus("current")
_DxStatsNoTicks_Type = Gauge32
_DxStatsNoTicks_Object = MibScalar
dxStatsNoTicks = _DxStatsNoTicks_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 2, 3),
    _DxStatsNoTicks_Type()
)
dxStatsNoTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxStatsNoTicks.setStatus("current")
_DxStatsQueue_Type = Gauge32
_DxStatsQueue_Object = MibScalar
dxStatsQueue = _DxStatsQueue_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 2, 4),
    _DxStatsQueue_Type()
)
dxStatsQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxStatsQueue.setStatus("current")
_DxStatsBusy_Type = Gauge32
_DxStatsBusy_Object = MibScalar
dxStatsBusy = _DxStatsBusy_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 2, 5),
    _DxStatsBusy_Type()
)
dxStatsBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxStatsBusy.setStatus("current")
_DxStatsOps_Type = Counter32
_DxStatsOps_Object = MibScalar
dxStatsOps = _DxStatsOps_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 2, 6),
    _DxStatsOps_Type()
)
dxStatsOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxStatsOps.setStatus("current")
_DxStatsEntries_Type = Counter32
_DxStatsEntries_Object = MibScalar
dxStatsEntries = _DxStatsEntries_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 2, 7),
    _DxStatsEntries_Type()
)
dxStatsEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxStatsEntries.setStatus("current")
_DxStatsMWQ_Type = Gauge32
_DxStatsMWQ_Object = MibScalar
dxStatsMWQ = _DxStatsMWQ_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 2, 8),
    _DxStatsMWQ_Type()
)
dxStatsMWQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxStatsMWQ.setStatus("current")
_Dx_CACHE_MIB_ObjectIdentity = ObjectIdentity
dx_CACHE_MIB = _Dx_CACHE_MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3327, 21, 3)
)


class _DxCacheStatus_Type(Integer32):
    """Custom type dxCacheStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cache-building", 2),
          ("cache-dirty", 4),
          ("cache-disabled", 1),
          ("cache-ok", 3),
          ("internal-error", 0))
    )


_DxCacheStatus_Type.__name__ = "Integer32"
_DxCacheStatus_Object = MibScalar
dxCacheStatus = _DxCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 3, 1),
    _DxCacheStatus_Type()
)
dxCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxCacheStatus.setStatus("current")
_DxCacheSize_Type = Gauge32
_DxCacheSize_Object = MibScalar
dxCacheSize = _DxCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 3, 2),
    _DxCacheSize_Type()
)
dxCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxCacheSize.setStatus("current")
_DxCacheSearchHits_Type = Counter32
_DxCacheSearchHits_Object = MibScalar
dxCacheSearchHits = _DxCacheSearchHits_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 3, 3),
    _DxCacheSearchHits_Type()
)
dxCacheSearchHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxCacheSearchHits.setStatus("current")
_DxCacheSearchMisses_Type = Counter32
_DxCacheSearchMisses_Object = MibScalar
dxCacheSearchMisses = _DxCacheSearchMisses_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 3, 4),
    _DxCacheSearchMisses_Type()
)
dxCacheSearchMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxCacheSearchMisses.setStatus("current")
_DxCacheSequentialScans_Type = Counter32
_DxCacheSequentialScans_Object = MibScalar
dxCacheSequentialScans = _DxCacheSequentialScans_Object(
    (1, 3, 6, 1, 4, 1, 3327, 21, 3, 5),
    _DxCacheSequentialScans_Type()
)
dxCacheSequentialScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxCacheSequentialScans.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DX-MIB",
    **{"eTrustDirectory": eTrustDirectory,
       "dxMIB": dxMIB,
       "dx-MULTIWRITE-MIB": dx_MULTIWRITE_MIB,
       "dxMWTable": dxMWTable,
       "dxMWEntry": dxMWEntry,
       "dxMWIndex": dxMWIndex,
       "dxRemoteDsaName": dxRemoteDsaName,
       "dxMWQueueLength": dxMWQueueLength,
       "dxMWStatus": dxMWStatus,
       "dxMWPendingRemote": dxMWPendingRemote,
       "dxMWConfirmedLocal": dxMWConfirmedLocal,
       "dx-STATISTICS-MIB": dx_STATISTICS_MIB,
       "dxStatsAssocs": dxStatsAssocs,
       "dxStatsNilCredit": dxStatsNilCredit,
       "dxStatsNoTicks": dxStatsNoTicks,
       "dxStatsQueue": dxStatsQueue,
       "dxStatsBusy": dxStatsBusy,
       "dxStatsOps": dxStatsOps,
       "dxStatsEntries": dxStatsEntries,
       "dxStatsMWQ": dxStatsMWQ,
       "dx-CACHE-MIB": dx_CACHE_MIB,
       "dxCacheStatus": dxCacheStatus,
       "dxCacheSize": dxCacheSize,
       "dxCacheSearchHits": dxCacheSearchHits,
       "dxCacheSearchMisses": dxCacheSearchMisses,
       "dxCacheSequentialScans": dxCacheSequentialScans}
)
