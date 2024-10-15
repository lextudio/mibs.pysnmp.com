# SNMP MIB module (INFORMANT-SQLSERVER-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INFORMANT-SQLSERVER-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:19 2024
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

(InstanceName,
 informant) = mibBuilder.importSymbols(
    "WTCS",
    "InstanceName",
    "informant")


# MODULE-IDENTITY

sqlServerV2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13)
)
sqlServerV2.setRevisions(
        ("2008-04-27 06:06",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AnalysisServicesV2_ObjectIdentity = ObjectIdentity
analysisServicesV2 = _AnalysisServicesV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1)
)
_As2NameTable_Object = MibTable
as2NameTable = _As2NameTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    as2NameTable.setStatus("current")
_As2NameEntry_Object = MibTableRow
as2NameEntry = _As2NameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 1, 1)
)
as2NameEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "as2NameIndex"),
)
if mibBuilder.loadTexts:
    as2NameEntry.setStatus("current")


class _As2NameIndex_Type(Integer32):
    """Custom type as2NameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_As2NameIndex_Type.__name__ = "Integer32"
_As2NameIndex_Object = MibTableColumn
as2NameIndex = _As2NameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 1, 1, 1),
    _As2NameIndex_Type()
)
as2NameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2NameIndex.setStatus("current")
_As2NameInstance_Type = InstanceName
_As2NameInstance_Object = MibTableColumn
as2NameInstance = _As2NameInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 1, 1, 2),
    _As2NameInstance_Type()
)
as2NameInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2NameInstance.setStatus("current")
_As2CacheTable_Object = MibTable
as2CacheTable = _As2CacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    as2CacheTable.setStatus("current")
_As2CacheEntry_Object = MibTableRow
as2CacheEntry = _As2CacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1)
)
as2CacheEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "as2NameIndex"),
)
if mibBuilder.loadTexts:
    as2CacheEntry.setStatus("current")
_As2CacheCurrentKB_Type = Gauge32
_As2CacheCurrentKB_Object = MibTableColumn
as2CacheCurrentKB = _As2CacheCurrentKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 1),
    _As2CacheCurrentKB_Type()
)
as2CacheCurrentKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheCurrentKB.setStatus("current")
_As2CacheCurrentEntries_Type = Gauge32
_As2CacheCurrentEntries_Object = MibTableColumn
as2CacheCurrentEntries = _As2CacheCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 2),
    _As2CacheCurrentEntries_Type()
)
as2CacheCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheCurrentEntries.setStatus("current")
_As2CacheDirectHitRatio_Type = Gauge32
_As2CacheDirectHitRatio_Object = MibTableColumn
as2CacheDirectHitRatio = _As2CacheDirectHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 3),
    _As2CacheDirectHitRatio_Type()
)
as2CacheDirectHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheDirectHitRatio.setStatus("current")
_As2CacheDirectHitsPerSec_Type = Gauge32
_As2CacheDirectHitsPerSec_Object = MibTableColumn
as2CacheDirectHitsPerSec = _As2CacheDirectHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 4),
    _As2CacheDirectHitsPerSec_Type()
)
as2CacheDirectHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheDirectHitsPerSec.setStatus("current")
_As2CacheEvictionsPerSec_Type = Gauge32
_As2CacheEvictionsPerSec_Object = MibTableColumn
as2CacheEvictionsPerSec = _As2CacheEvictionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 5),
    _As2CacheEvictionsPerSec_Type()
)
as2CacheEvictionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheEvictionsPerSec.setStatus("current")
_As2CacheInsertsPerSec_Type = Gauge32
_As2CacheInsertsPerSec_Object = MibTableColumn
as2CacheInsertsPerSec = _As2CacheInsertsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 6),
    _As2CacheInsertsPerSec_Type()
)
as2CacheInsertsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheInsertsPerSec.setStatus("current")
_As2CacheKBAddedPerSec_Type = Gauge32
_As2CacheKBAddedPerSec_Object = MibTableColumn
as2CacheKBAddedPerSec = _As2CacheKBAddedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 7),
    _As2CacheKBAddedPerSec_Type()
)
as2CacheKBAddedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheKBAddedPerSec.setStatus("current")
_As2CacheLookupsPerSec_Type = Gauge32
_As2CacheLookupsPerSec_Object = MibTableColumn
as2CacheLookupsPerSec = _As2CacheLookupsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 8),
    _As2CacheLookupsPerSec_Type()
)
as2CacheLookupsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheLookupsPerSec.setStatus("current")
_As2CacheMissesPerSec_Type = Gauge32
_As2CacheMissesPerSec_Object = MibTableColumn
as2CacheMissesPerSec = _As2CacheMissesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 9),
    _As2CacheMissesPerSec_Type()
)
as2CacheMissesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheMissesPerSec.setStatus("current")
_As2CacheTotalDirectHits_Type = Gauge32
_As2CacheTotalDirectHits_Object = MibTableColumn
as2CacheTotalDirectHits = _As2CacheTotalDirectHits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 10),
    _As2CacheTotalDirectHits_Type()
)
as2CacheTotalDirectHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheTotalDirectHits.setStatus("current")
_As2CacheTotalEvictions_Type = Gauge32
_As2CacheTotalEvictions_Object = MibTableColumn
as2CacheTotalEvictions = _As2CacheTotalEvictions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 11),
    _As2CacheTotalEvictions_Type()
)
as2CacheTotalEvictions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheTotalEvictions.setStatus("current")
_As2CacheTotalFiltIteratorCachHit_Type = Gauge32
_As2CacheTotalFiltIteratorCachHit_Object = MibTableColumn
as2CacheTotalFiltIteratorCachHit = _As2CacheTotalFiltIteratorCachHit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 12),
    _As2CacheTotalFiltIteratorCachHit_Type()
)
as2CacheTotalFiltIteratorCachHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheTotalFiltIteratorCachHit.setStatus("current")
_As2CacheTotalFiltIteratorCachMis_Type = Gauge32
_As2CacheTotalFiltIteratorCachMis_Object = MibTableColumn
as2CacheTotalFiltIteratorCachMis = _As2CacheTotalFiltIteratorCachMis_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 13),
    _As2CacheTotalFiltIteratorCachMis_Type()
)
as2CacheTotalFiltIteratorCachMis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheTotalFiltIteratorCachMis.setStatus("current")
_As2CacheTotalInserts_Type = Gauge32
_As2CacheTotalInserts_Object = MibTableColumn
as2CacheTotalInserts = _As2CacheTotalInserts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 14),
    _As2CacheTotalInserts_Type()
)
as2CacheTotalInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheTotalInserts.setStatus("current")
_As2CacheTotalLookups_Type = Gauge32
_As2CacheTotalLookups_Object = MibTableColumn
as2CacheTotalLookups = _As2CacheTotalLookups_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 15),
    _As2CacheTotalLookups_Type()
)
as2CacheTotalLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheTotalLookups.setStatus("current")
_As2CacheTotalMisses_Type = Gauge32
_As2CacheTotalMisses_Object = MibTableColumn
as2CacheTotalMisses = _As2CacheTotalMisses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 2, 1, 16),
    _As2CacheTotalMisses_Type()
)
as2CacheTotalMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2CacheTotalMisses.setStatus("current")
_As2ConnectionTable_Object = MibTable
as2ConnectionTable = _As2ConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 3)
)
if mibBuilder.loadTexts:
    as2ConnectionTable.setStatus("current")
_As2ConnectionEntry_Object = MibTableRow
as2ConnectionEntry = _As2ConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 3, 1)
)
as2ConnectionEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "as2NameIndex"),
)
if mibBuilder.loadTexts:
    as2ConnectionEntry.setStatus("current")
_As2ConnectionCurrentConnections_Type = Gauge32
_As2ConnectionCurrentConnections_Object = MibTableColumn
as2ConnectionCurrentConnections = _As2ConnectionCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 3, 1, 1),
    _As2ConnectionCurrentConnections_Type()
)
as2ConnectionCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ConnectionCurrentConnections.setStatus("current")
_As2ConnectionCurrentUserSessions_Type = Gauge32
_As2ConnectionCurrentUserSessions_Object = MibTableColumn
as2ConnectionCurrentUserSessions = _As2ConnectionCurrentUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 3, 1, 2),
    _As2ConnectionCurrentUserSessions_Type()
)
as2ConnectionCurrentUserSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ConnectionCurrentUserSessions.setStatus("current")
_As2ConnectionFailuresPerSec_Type = Gauge32
_As2ConnectionFailuresPerSec_Object = MibTableColumn
as2ConnectionFailuresPerSec = _As2ConnectionFailuresPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 3, 1, 3),
    _As2ConnectionFailuresPerSec_Type()
)
as2ConnectionFailuresPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ConnectionFailuresPerSec.setStatus("current")
_As2ConnectionRequestsPerSec_Type = Gauge32
_As2ConnectionRequestsPerSec_Object = MibTableColumn
as2ConnectionRequestsPerSec = _As2ConnectionRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 3, 1, 4),
    _As2ConnectionRequestsPerSec_Type()
)
as2ConnectionRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ConnectionRequestsPerSec.setStatus("current")
_As2ConnectionSuccessesPerSec_Type = Gauge32
_As2ConnectionSuccessesPerSec_Object = MibTableColumn
as2ConnectionSuccessesPerSec = _As2ConnectionSuccessesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 3, 1, 5),
    _As2ConnectionSuccessesPerSec_Type()
)
as2ConnectionSuccessesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ConnectionSuccessesPerSec.setStatus("current")
_As2ConnectionTotalFailures_Type = Gauge32
_As2ConnectionTotalFailures_Object = MibTableColumn
as2ConnectionTotalFailures = _As2ConnectionTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 3, 1, 6),
    _As2ConnectionTotalFailures_Type()
)
as2ConnectionTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ConnectionTotalFailures.setStatus("current")
_As2ConnectionTotalRequests_Type = Gauge32
_As2ConnectionTotalRequests_Object = MibTableColumn
as2ConnectionTotalRequests = _As2ConnectionTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 3, 1, 7),
    _As2ConnectionTotalRequests_Type()
)
as2ConnectionTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ConnectionTotalRequests.setStatus("current")
_As2ConnectionTotalSuccesses_Type = Gauge32
_As2ConnectionTotalSuccesses_Object = MibTableColumn
as2ConnectionTotalSuccesses = _As2ConnectionTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 3, 1, 8),
    _As2ConnectionTotalSuccesses_Type()
)
as2ConnectionTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ConnectionTotalSuccesses.setStatus("current")
_As2DataMiningModelProcessTable_Object = MibTable
as2DataMiningModelProcessTable = _As2DataMiningModelProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 4)
)
if mibBuilder.loadTexts:
    as2DataMiningModelProcessTable.setStatus("current")
_As2DataMiningModelProcessEntry_Object = MibTableRow
as2DataMiningModelProcessEntry = _As2DataMiningModelProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 4, 1)
)
as2DataMiningModelProcessEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "as2NameIndex"),
)
if mibBuilder.loadTexts:
    as2DataMiningModelProcessEntry.setStatus("current")
_As2dmmpCasesPerSec_Type = Gauge32
_As2dmmpCasesPerSec_Object = MibTableColumn
as2dmmpCasesPerSec = _As2dmmpCasesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 4, 1, 1),
    _As2dmmpCasesPerSec_Type()
)
as2dmmpCasesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2dmmpCasesPerSec.setStatus("current")
_As2dmmpCurrentModelsProcessing_Type = Gauge32
_As2dmmpCurrentModelsProcessing_Object = MibTableColumn
as2dmmpCurrentModelsProcessing = _As2dmmpCurrentModelsProcessing_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 4, 1, 2),
    _As2dmmpCurrentModelsProcessing_Type()
)
as2dmmpCurrentModelsProcessing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2dmmpCurrentModelsProcessing.setStatus("current")
_As2DataMiningPredictionTable_Object = MibTable
as2DataMiningPredictionTable = _As2DataMiningPredictionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 5)
)
if mibBuilder.loadTexts:
    as2DataMiningPredictionTable.setStatus("current")
_As2DataMiningPredictionEntry_Object = MibTableRow
as2DataMiningPredictionEntry = _As2DataMiningPredictionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 5, 1)
)
as2DataMiningPredictionEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "as2NameIndex"),
)
if mibBuilder.loadTexts:
    as2DataMiningPredictionEntry.setStatus("current")
_As2dmpConcurrentDMQueries_Type = Gauge32
_As2dmpConcurrentDMQueries_Object = MibTableColumn
as2dmpConcurrentDMQueries = _As2dmpConcurrentDMQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 5, 1, 1),
    _As2dmpConcurrentDMQueries_Type()
)
as2dmpConcurrentDMQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2dmpConcurrentDMQueries.setStatus("current")
_As2dmpPredictionsPerSec_Type = Gauge32
_As2dmpPredictionsPerSec_Object = MibTableColumn
as2dmpPredictionsPerSec = _As2dmpPredictionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 5, 1, 2),
    _As2dmpPredictionsPerSec_Type()
)
as2dmpPredictionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2dmpPredictionsPerSec.setStatus("current")
_As2dmpQueriesPerSec_Type = Gauge32
_As2dmpQueriesPerSec_Object = MibTableColumn
as2dmpQueriesPerSec = _As2dmpQueriesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 5, 1, 3),
    _As2dmpQueriesPerSec_Type()
)
as2dmpQueriesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2dmpQueriesPerSec.setStatus("current")
_As2dmpRowsPerSec_Type = Gauge32
_As2dmpRowsPerSec_Object = MibTableColumn
as2dmpRowsPerSec = _As2dmpRowsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 5, 1, 4),
    _As2dmpRowsPerSec_Type()
)
as2dmpRowsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2dmpRowsPerSec.setStatus("current")
_As2dmpTotalPredictions_Type = Gauge32
_As2dmpTotalPredictions_Object = MibTableColumn
as2dmpTotalPredictions = _As2dmpTotalPredictions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 5, 1, 5),
    _As2dmpTotalPredictions_Type()
)
as2dmpTotalPredictions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2dmpTotalPredictions.setStatus("current")
_As2dmpTotalQueries_Type = Gauge32
_As2dmpTotalQueries_Object = MibTableColumn
as2dmpTotalQueries = _As2dmpTotalQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 5, 1, 6),
    _As2dmpTotalQueries_Type()
)
as2dmpTotalQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2dmpTotalQueries.setStatus("current")
_As2dmpTotalRows_Type = Gauge32
_As2dmpTotalRows_Object = MibTableColumn
as2dmpTotalRows = _As2dmpTotalRows_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 5, 1, 7),
    _As2dmpTotalRows_Type()
)
as2dmpTotalRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2dmpTotalRows.setStatus("current")
_As2LocksTable_Object = MibTable
as2LocksTable = _As2LocksTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 6)
)
if mibBuilder.loadTexts:
    as2LocksTable.setStatus("current")
_As2LocksEntry_Object = MibTableRow
as2LocksEntry = _As2LocksEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 6, 1)
)
as2LocksEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "as2NameIndex"),
)
if mibBuilder.loadTexts:
    as2LocksEntry.setStatus("current")
_As2LocksCurrentLatchWaits_Type = Gauge32
_As2LocksCurrentLatchWaits_Object = MibTableColumn
as2LocksCurrentLatchWaits = _As2LocksCurrentLatchWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 6, 1, 1),
    _As2LocksCurrentLatchWaits_Type()
)
as2LocksCurrentLatchWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2LocksCurrentLatchWaits.setStatus("current")
_As2LocksCurrentLockWaits_Type = Gauge32
_As2LocksCurrentLockWaits_Object = MibTableColumn
as2LocksCurrentLockWaits = _As2LocksCurrentLockWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 6, 1, 2),
    _As2LocksCurrentLockWaits_Type()
)
as2LocksCurrentLockWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2LocksCurrentLockWaits.setStatus("current")
_As2LocksCurrentLocks_Type = Gauge32
_As2LocksCurrentLocks_Object = MibTableColumn
as2LocksCurrentLocks = _As2LocksCurrentLocks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 6, 1, 3),
    _As2LocksCurrentLocks_Type()
)
as2LocksCurrentLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2LocksCurrentLocks.setStatus("current")
_As2LocksLatchWaitsPerSec_Type = Gauge32
_As2LocksLatchWaitsPerSec_Object = MibTableColumn
as2LocksLatchWaitsPerSec = _As2LocksLatchWaitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 6, 1, 4),
    _As2LocksLatchWaitsPerSec_Type()
)
as2LocksLatchWaitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2LocksLatchWaitsPerSec.setStatus("current")
_As2LocksLockDenialsPerSec_Type = Gauge32
_As2LocksLockDenialsPerSec_Object = MibTableColumn
as2LocksLockDenialsPerSec = _As2LocksLockDenialsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 6, 1, 5),
    _As2LocksLockDenialsPerSec_Type()
)
as2LocksLockDenialsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2LocksLockDenialsPerSec.setStatus("current")
_As2LocksLockGrantsPerSec_Type = Gauge32
_As2LocksLockGrantsPerSec_Object = MibTableColumn
as2LocksLockGrantsPerSec = _As2LocksLockGrantsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 6, 1, 6),
    _As2LocksLockGrantsPerSec_Type()
)
as2LocksLockGrantsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2LocksLockGrantsPerSec.setStatus("current")
_As2LocksLockRequestsPerSec_Type = Gauge32
_As2LocksLockRequestsPerSec_Object = MibTableColumn
as2LocksLockRequestsPerSec = _As2LocksLockRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 6, 1, 7),
    _As2LocksLockRequestsPerSec_Type()
)
as2LocksLockRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2LocksLockRequestsPerSec.setStatus("current")
_As2LocksLockWaitsPerSec_Type = Gauge32
_As2LocksLockWaitsPerSec_Object = MibTableColumn
as2LocksLockWaitsPerSec = _As2LocksLockWaitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 6, 1, 8),
    _As2LocksLockWaitsPerSec_Type()
)
as2LocksLockWaitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2LocksLockWaitsPerSec.setStatus("current")
_As2LocksTotalDeadlocksDetected_Type = Gauge32
_As2LocksTotalDeadlocksDetected_Object = MibTableColumn
as2LocksTotalDeadlocksDetected = _As2LocksTotalDeadlocksDetected_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 6, 1, 9),
    _As2LocksTotalDeadlocksDetected_Type()
)
as2LocksTotalDeadlocksDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2LocksTotalDeadlocksDetected.setStatus("current")
_As2LocksUnlockRequestsPerSec_Type = Gauge32
_As2LocksUnlockRequestsPerSec_Object = MibTableColumn
as2LocksUnlockRequestsPerSec = _As2LocksUnlockRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 6, 1, 10),
    _As2LocksUnlockRequestsPerSec_Type()
)
as2LocksUnlockRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2LocksUnlockRequestsPerSec.setStatus("current")
_As2MDXTable_Object = MibTable
as2MDXTable = _As2MDXTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7)
)
if mibBuilder.loadTexts:
    as2MDXTable.setStatus("current")
_As2MDXEntry_Object = MibTableRow
as2MDXEntry = _As2MDXEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1)
)
as2MDXEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "as2NameIndex"),
)
if mibBuilder.loadTexts:
    as2MDXEntry.setStatus("current")
_As2MDXCurrentNumOfCachedEvalNode_Type = Gauge32
_As2MDXCurrentNumOfCachedEvalNode_Object = MibTableColumn
as2MDXCurrentNumOfCachedEvalNode = _As2MDXCurrentNumOfCachedEvalNode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 1),
    _As2MDXCurrentNumOfCachedEvalNode_Type()
)
as2MDXCurrentNumOfCachedEvalNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXCurrentNumOfCachedEvalNode.setStatus("current")
_As2MDXCurrentNumOfEvalNode_Type = Gauge32
_As2MDXCurrentNumOfEvalNode_Object = MibTableColumn
as2MDXCurrentNumOfEvalNode = _As2MDXCurrentNumOfEvalNode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 2),
    _As2MDXCurrentNumOfEvalNode_Type()
)
as2MDXCurrentNumOfEvalNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXCurrentNumOfEvalNode.setStatus("current")
_As2MDXNumOfStorageEngineEvalNode_Type = Gauge32
_As2MDXNumOfStorageEngineEvalNode_Object = MibTableColumn
as2MDXNumOfStorageEngineEvalNode = _As2MDXNumOfStorageEngineEvalNode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 3),
    _As2MDXNumOfStorageEngineEvalNode_Type()
)
as2MDXNumOfStorageEngineEvalNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumOfStorageEngineEvalNode.setStatus("current")
_As2MDXNumOfBulkModeEvalNode_Type = Gauge32
_As2MDXNumOfBulkModeEvalNode_Object = MibTableColumn
as2MDXNumOfBulkModeEvalNode = _As2MDXNumOfBulkModeEvalNode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 4),
    _As2MDXNumOfBulkModeEvalNode_Type()
)
as2MDXNumOfBulkModeEvalNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumOfBulkModeEvalNode.setStatus("current")
_As2MDXNumOfCachedotherEvalNode_Type = Gauge32
_As2MDXNumOfCachedotherEvalNode_Object = MibTableColumn
as2MDXNumOfCachedotherEvalNode = _As2MDXNumOfCachedotherEvalNode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 5),
    _As2MDXNumOfCachedotherEvalNode_Type()
)
as2MDXNumOfCachedotherEvalNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumOfCachedotherEvalNode.setStatus("current")
_As2MDXNumCacheStorEngineEvalNode_Type = Gauge32
_As2MDXNumCacheStorEngineEvalNode_Object = MibTableColumn
as2MDXNumCacheStorEngineEvalNode = _As2MDXNumCacheStorEngineEvalNode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 6),
    _As2MDXNumCacheStorEngineEvalNode_Type()
)
as2MDXNumCacheStorEngineEvalNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumCacheStorEngineEvalNode.setStatus("current")
_As2MDXNumOfCacheBulkModeEvalNode_Type = Gauge32
_As2MDXNumOfCacheBulkModeEvalNode_Object = MibTableColumn
as2MDXNumOfCacheBulkModeEvalNode = _As2MDXNumOfCacheBulkModeEvalNode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 7),
    _As2MDXNumOfCacheBulkModeEvalNode_Type()
)
as2MDXNumOfCacheBulkModeEvalNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumOfCacheBulkModeEvalNode.setStatus("current")
_As2MDXNumberOfCalculationCovers_Type = Gauge32
_As2MDXNumberOfCalculationCovers_Object = MibTableColumn
as2MDXNumberOfCalculationCovers = _As2MDXNumberOfCalculationCovers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 8),
    _As2MDXNumberOfCalculationCovers_Type()
)
as2MDXNumberOfCalculationCovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumberOfCalculationCovers.setStatus("current")
_As2MDXNumOfCellByCellEvalNode_Type = Gauge32
_As2MDXNumOfCellByCellEvalNode_Object = MibTableColumn
as2MDXNumOfCellByCellEvalNode = _As2MDXNumOfCellByCellEvalNode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 9),
    _As2MDXNumOfCellByCellEvalNode_Type()
)
as2MDXNumOfCellByCellEvalNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumOfCellByCellEvalNode.setStatus("current")
_As2MDXNumCellCellHitCacheEvalNod_Type = Gauge32
_As2MDXNumCellCellHitCacheEvalNod_Object = MibTableColumn
as2MDXNumCellCellHitCacheEvalNod = _As2MDXNumCellCellHitCacheEvalNod_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 10),
    _As2MDXNumCellCellHitCacheEvalNod_Type()
)
as2MDXNumCellCellHitCacheEvalNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumCellCellHitCacheEvalNod.setStatus("current")
_As2MDXNumCellCellMissCachEvalNod_Type = Gauge32
_As2MDXNumCellCellMissCachEvalNod_Object = MibTableColumn
as2MDXNumCellCellMissCachEvalNod = _As2MDXNumCellCellMissCachEvalNod_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 11),
    _As2MDXNumCellCellMissCachEvalNod_Type()
)
as2MDXNumCellCellMissCachEvalNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumCellCellMissCachEvalNod.setStatus("current")
_As2MDXNumEvalNodThatCovASglCell_Type = Gauge32
_As2MDXNumEvalNodThatCovASglCell_Object = MibTableColumn
as2MDXNumEvalNodThatCovASglCell = _As2MDXNumEvalNodThatCovASglCell_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 12),
    _As2MDXNumEvalNodThatCovASglCell_Type()
)
as2MDXNumEvalNodThatCovASglCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumEvalNodThatCovASglCell.setStatus("current")
_As2MDXNumEvalNodeCalcSameGranula_Type = Gauge32
_As2MDXNumEvalNodeCalcSameGranula_Object = MibTableColumn
as2MDXNumEvalNodeCalcSameGranula = _As2MDXNumEvalNodeCalcSameGranula_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 13),
    _As2MDXNumEvalNodeCalcSameGranula_Type()
)
as2MDXNumEvalNodeCalcSameGranula.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumEvalNodeCalcSameGranula.setStatus("current")
_As2MDXNumEvictionsEvalNode_Type = Gauge32
_As2MDXNumEvictionsEvalNode_Object = MibTableColumn
as2MDXNumEvictionsEvalNode = _As2MDXNumEvictionsEvalNode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 14),
    _As2MDXNumEvictionsEvalNode_Type()
)
as2MDXNumEvictionsEvalNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumEvictionsEvalNode.setStatus("current")
_As2MDXNumHashdexHitsCacheEvalNod_Type = Gauge32
_As2MDXNumHashdexHitsCacheEvalNod_Object = MibTableColumn
as2MDXNumHashdexHitsCacheEvalNod = _As2MDXNumHashdexHitsCacheEvalNod_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 15),
    _As2MDXNumHashdexHitsCacheEvalNod_Type()
)
as2MDXNumHashdexHitsCacheEvalNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumHashdexHitsCacheEvalNod.setStatus("current")
_As2MDXNumSubcubeHitsCacheEvalNod_Type = Gauge32
_As2MDXNumSubcubeHitsCacheEvalNod_Object = MibTableColumn
as2MDXNumSubcubeHitsCacheEvalNod = _As2MDXNumSubcubeHitsCacheEvalNod_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 16),
    _As2MDXNumSubcubeHitsCacheEvalNod_Type()
)
as2MDXNumSubcubeHitsCacheEvalNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumSubcubeHitsCacheEvalNod.setStatus("current")
_As2MDXNumSubcubeMissCacheEvalNod_Type = Gauge32
_As2MDXNumSubcubeMissCacheEvalNod_Object = MibTableColumn
as2MDXNumSubcubeMissCacheEvalNod = _As2MDXNumSubcubeMissCacheEvalNod_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 17),
    _As2MDXNumSubcubeMissCacheEvalNod_Type()
)
as2MDXNumSubcubeMissCacheEvalNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXNumSubcubeMissCacheEvalNod.setStatus("current")
_As2MDXTotalAutoexist_Type = Gauge32
_As2MDXTotalAutoexist_Object = MibTableColumn
as2MDXTotalAutoexist = _As2MDXTotalAutoexist_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 18),
    _As2MDXTotalAutoexist_Type()
)
as2MDXTotalAutoexist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXTotalAutoexist.setStatus("current")
_As2MDXTotalEXISTING_Type = Gauge32
_As2MDXTotalEXISTING_Object = MibTableColumn
as2MDXTotalEXISTING = _As2MDXTotalEXISTING_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 19),
    _As2MDXTotalEXISTING_Type()
)
as2MDXTotalEXISTING.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXTotalEXISTING.setStatus("current")
_As2MDXTotalNONEMPTY_Type = Gauge32
_As2MDXTotalNONEMPTY_Object = MibTableColumn
as2MDXTotalNONEMPTY = _As2MDXTotalNONEMPTY_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 20),
    _As2MDXTotalNONEMPTY_Type()
)
as2MDXTotalNONEMPTY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXTotalNONEMPTY.setStatus("current")
_As2MDXTotalNONEMPTYCalculatMemb_Type = Gauge32
_As2MDXTotalNONEMPTYCalculatMemb_Object = MibTableColumn
as2MDXTotalNONEMPTYCalculatMemb = _As2MDXTotalNONEMPTYCalculatMemb_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 21),
    _As2MDXTotalNONEMPTYCalculatMemb_Type()
)
as2MDXTotalNONEMPTYCalculatMemb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXTotalNONEMPTYCalculatMemb.setStatus("current")
_As2MDXTotalNONEMPTYUnoptimized_Type = Gauge32
_As2MDXTotalNONEMPTYUnoptimized_Object = MibTableColumn
as2MDXTotalNONEMPTYUnoptimized = _As2MDXTotalNONEMPTYUnoptimized_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 22),
    _As2MDXTotalNONEMPTYUnoptimized_Type()
)
as2MDXTotalNONEMPTYUnoptimized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXTotalNONEMPTYUnoptimized.setStatus("current")
_As2MDXTotalSonarSubcubes_Type = Gauge32
_As2MDXTotalSonarSubcubes_Object = MibTableColumn
as2MDXTotalSonarSubcubes = _As2MDXTotalSonarSubcubes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 23),
    _As2MDXTotalSonarSubcubes_Type()
)
as2MDXTotalSonarSubcubes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXTotalSonarSubcubes.setStatus("current")
_As2MDXTotalCellsCalculated_Type = Gauge32
_As2MDXTotalCellsCalculated_Object = MibTableColumn
as2MDXTotalCellsCalculated = _As2MDXTotalCellsCalculated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 24),
    _As2MDXTotalCellsCalculated_Type()
)
as2MDXTotalCellsCalculated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXTotalCellsCalculated.setStatus("current")
_As2MDXTotalFlatCacheInserts_Type = Gauge32
_As2MDXTotalFlatCacheInserts_Object = MibTableColumn
as2MDXTotalFlatCacheInserts = _As2MDXTotalFlatCacheInserts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 25),
    _As2MDXTotalFlatCacheInserts_Type()
)
as2MDXTotalFlatCacheInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXTotalFlatCacheInserts.setStatus("current")
_As2MDXTotalRecomputes_Type = Gauge32
_As2MDXTotalRecomputes_Object = MibTableColumn
as2MDXTotalRecomputes = _As2MDXTotalRecomputes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 7, 1, 26),
    _As2MDXTotalRecomputes_Type()
)
as2MDXTotalRecomputes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2MDXTotalRecomputes.setStatus("current")
_As2MemoryTable_Object = MibTable
as2MemoryTable = _As2MemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8)
)
if mibBuilder.loadTexts:
    as2MemoryTable.setStatus("current")
_As2MemoryEntry_Object = MibTableRow
as2MemoryEntry = _As2MemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1)
)
as2MemoryEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "as2NameIndex"),
)
if mibBuilder.loadTexts:
    as2MemoryEntry.setStatus("current")
_As2memAggCacheKB_Type = Gauge32
_As2memAggCacheKB_Object = MibTableColumn
as2memAggCacheKB = _As2memAggCacheKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 1),
    _As2memAggCacheKB_Type()
)
as2memAggCacheKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memAggCacheKB.setStatus("current")
_As2memAggregationMapFiles_Type = Gauge32
_As2memAggregationMapFiles_Object = MibTableColumn
as2memAggregationMapFiles = _As2memAggregationMapFiles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 2),
    _As2memAggregationMapFiles_Type()
)
as2memAggregationMapFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memAggregationMapFiles.setStatus("current")
_As2memCleanerBalancePerSec_Type = Gauge32
_As2memCleanerBalancePerSec_Object = MibTableColumn
as2memCleanerBalancePerSec = _As2memCleanerBalancePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 3),
    _As2memCleanerBalancePerSec_Type()
)
as2memCleanerBalancePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memCleanerBalancePerSec.setStatus("current")
_As2memCleanerCurrentPrice_Type = Gauge32
_As2memCleanerCurrentPrice_Object = MibTableColumn
as2memCleanerCurrentPrice = _As2memCleanerCurrentPrice_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 4),
    _As2memCleanerCurrentPrice_Type()
)
as2memCleanerCurrentPrice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memCleanerCurrentPrice.setStatus("current")
_As2memCleanerMemoryKB_Type = Gauge32
_As2memCleanerMemoryKB_Object = MibTableColumn
as2memCleanerMemoryKB = _As2memCleanerMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 5),
    _As2memCleanerMemoryKB_Type()
)
as2memCleanerMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memCleanerMemoryKB.setStatus("current")
_As2memCleanerMemNonshrinkableKB_Type = Gauge32
_As2memCleanerMemNonshrinkableKB_Object = MibTableColumn
as2memCleanerMemNonshrinkableKB = _As2memCleanerMemNonshrinkableKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 6),
    _As2memCleanerMemNonshrinkableKB_Type()
)
as2memCleanerMemNonshrinkableKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memCleanerMemNonshrinkableKB.setStatus("current")
_As2memCleanerMemoryShrinkableKB_Type = Gauge32
_As2memCleanerMemoryShrinkableKB_Object = MibTableColumn
as2memCleanerMemoryShrinkableKB = _As2memCleanerMemoryShrinkableKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 7),
    _As2memCleanerMemoryShrinkableKB_Type()
)
as2memCleanerMemoryShrinkableKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memCleanerMemoryShrinkableKB.setStatus("current")
_As2memCleanerMemShrunkKBSec_Type = Gauge32
_As2memCleanerMemShrunkKBSec_Object = MibTableColumn
as2memCleanerMemShrunkKBSec = _As2memCleanerMemShrunkKBSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 8),
    _As2memCleanerMemShrunkKBSec_Type()
)
as2memCleanerMemShrunkKBSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memCleanerMemShrunkKBSec.setStatus("current")
_As2memDimensionIndexHashFiles_Type = Gauge32
_As2memDimensionIndexHashFiles_Object = MibTableColumn
as2memDimensionIndexHashFiles = _As2memDimensionIndexHashFiles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 9),
    _As2memDimensionIndexHashFiles_Type()
)
as2memDimensionIndexHashFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memDimensionIndexHashFiles.setStatus("current")
_As2memDimensionPropertyFiles_Type = Gauge32
_As2memDimensionPropertyFiles_Object = MibTableColumn
as2memDimensionPropertyFiles = _As2memDimensionPropertyFiles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 10),
    _As2memDimensionPropertyFiles_Type()
)
as2memDimensionPropertyFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memDimensionPropertyFiles.setStatus("current")
_As2memDimensionStringFiles_Type = Gauge32
_As2memDimensionStringFiles_Object = MibTableColumn
as2memDimensionStringFiles = _As2memDimensionStringFiles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 11),
    _As2memDimensionStringFiles_Type()
)
as2memDimensionStringFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memDimensionStringFiles.setStatus("current")
_As2memFactAggregationFiles_Type = Gauge32
_As2memFactAggregationFiles_Object = MibTableColumn
as2memFactAggregationFiles = _As2memFactAggregationFiles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 12),
    _As2memFactAggregationFiles_Type()
)
as2memFactAggregationFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFactAggregationFiles.setStatus("current")
_As2memFactDataFiles_Type = Gauge32
_As2memFactDataFiles_Object = MibTableColumn
as2memFactDataFiles = _As2memFactDataFiles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 13),
    _As2memFactDataFiles_Type()
)
as2memFactDataFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFactDataFiles.setStatus("current")
_As2memFactStringFiles_Type = Gauge32
_As2memFactStringFiles_Object = MibTableColumn
as2memFactStringFiles = _As2memFactStringFiles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 14),
    _As2memFactStringFiles_Type()
)
as2memFactStringFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFactStringFiles.setStatus("current")
_As2memFilestoreClockPgExamineSec_Type = Gauge32
_As2memFilestoreClockPgExamineSec_Object = MibTableColumn
as2memFilestoreClockPgExamineSec = _As2memFilestoreClockPgExamineSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 15),
    _As2memFilestoreClockPgExamineSec_Type()
)
as2memFilestoreClockPgExamineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFilestoreClockPgExamineSec.setStatus("current")
_As2memFilestoreClockPgHaveRefSec_Type = Gauge32
_As2memFilestoreClockPgHaveRefSec_Object = MibTableColumn
as2memFilestoreClockPgHaveRefSec = _As2memFilestoreClockPgHaveRefSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 16),
    _As2memFilestoreClockPgHaveRefSec_Type()
)
as2memFilestoreClockPgHaveRefSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFilestoreClockPgHaveRefSec.setStatus("current")
_As2memFilestoreClockPgValidSec_Type = Gauge32
_As2memFilestoreClockPgValidSec_Object = MibTableColumn
as2memFilestoreClockPgValidSec = _As2memFilestoreClockPgValidSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 17),
    _As2memFilestoreClockPgValidSec_Type()
)
as2memFilestoreClockPgValidSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFilestoreClockPgValidSec.setStatus("current")
_As2memFilestoreIOErrors_Type = Gauge32
_As2memFilestoreIOErrors_Object = MibTableColumn
as2memFilestoreIOErrors = _As2memFilestoreIOErrors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 18),
    _As2memFilestoreIOErrors_Type()
)
as2memFilestoreIOErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFilestoreIOErrors.setStatus("current")
_As2memFilestoreIOErrorsPerSec_Type = Gauge32
_As2memFilestoreIOErrorsPerSec_Object = MibTableColumn
as2memFilestoreIOErrorsPerSec = _As2memFilestoreIOErrorsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 19),
    _As2memFilestoreIOErrorsPerSec_Type()
)
as2memFilestoreIOErrorsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFilestoreIOErrorsPerSec.setStatus("current")
_As2memFilestoreKB_Type = Gauge32
_As2memFilestoreKB_Object = MibTableColumn
as2memFilestoreKB = _As2memFilestoreKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 20),
    _As2memFilestoreKB_Type()
)
as2memFilestoreKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFilestoreKB.setStatus("current")
_As2memFilestoreKBReadsPerSec_Type = Gauge32
_As2memFilestoreKBReadsPerSec_Object = MibTableColumn
as2memFilestoreKBReadsPerSec = _As2memFilestoreKBReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 21),
    _As2memFilestoreKBReadsPerSec_Type()
)
as2memFilestoreKBReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFilestoreKBReadsPerSec.setStatus("current")
_As2memFilestoreKBWritePerSec_Type = Gauge32
_As2memFilestoreKBWritePerSec_Object = MibTableColumn
as2memFilestoreKBWritePerSec = _As2memFilestoreKBWritePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 22),
    _As2memFilestoreKBWritePerSec_Type()
)
as2memFilestoreKBWritePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFilestoreKBWritePerSec.setStatus("current")
_As2memFilestoreMemoryPinnedKB_Type = Gauge32
_As2memFilestoreMemoryPinnedKB_Object = MibTableColumn
as2memFilestoreMemoryPinnedKB = _As2memFilestoreMemoryPinnedKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 23),
    _As2memFilestoreMemoryPinnedKB_Type()
)
as2memFilestoreMemoryPinnedKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFilestoreMemoryPinnedKB.setStatus("current")
_As2memFilestorePageFaultsPerSec_Type = Gauge32
_As2memFilestorePageFaultsPerSec_Object = MibTableColumn
as2memFilestorePageFaultsPerSec = _As2memFilestorePageFaultsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 24),
    _As2memFilestorePageFaultsPerSec_Type()
)
as2memFilestorePageFaultsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFilestorePageFaultsPerSec.setStatus("current")
_As2memFilestoreReadsPerSec_Type = Gauge32
_As2memFilestoreReadsPerSec_Object = MibTableColumn
as2memFilestoreReadsPerSec = _As2memFilestoreReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 25),
    _As2memFilestoreReadsPerSec_Type()
)
as2memFilestoreReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFilestoreReadsPerSec.setStatus("current")
_As2memFilestoreWritesPerSec_Type = Gauge32
_As2memFilestoreWritesPerSec_Object = MibTableColumn
as2memFilestoreWritesPerSec = _As2memFilestoreWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 26),
    _As2memFilestoreWritesPerSec_Type()
)
as2memFilestoreWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memFilestoreWritesPerSec.setStatus("current")
_As2memInMemAggregationMapFileKB_Type = Gauge32
_As2memInMemAggregationMapFileKB_Object = MibTableColumn
as2memInMemAggregationMapFileKB = _As2memInMemAggregationMapFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 27),
    _As2memInMemAggregationMapFileKB_Type()
)
as2memInMemAggregationMapFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemAggregationMapFileKB.setStatus("current")
_As2memInMemAggregateMapFileKBSec_Type = Gauge32
_As2memInMemAggregateMapFileKBSec_Object = MibTableColumn
as2memInMemAggregateMapFileKBSec = _As2memInMemAggregateMapFileKBSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 28),
    _As2memInMemAggregateMapFileKBSec_Type()
)
as2memInMemAggregateMapFileKBSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemAggregateMapFileKBSec.setStatus("current")
_As2memInMemDimenIndexHashFileKB_Type = Gauge32
_As2memInMemDimenIndexHashFileKB_Object = MibTableColumn
as2memInMemDimenIndexHashFileKB = _As2memInMemDimenIndexHashFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 29),
    _As2memInMemDimenIndexHashFileKB_Type()
)
as2memInMemDimenIndexHashFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemDimenIndexHashFileKB.setStatus("current")
_As2memInMemDimenIndHashFileKBSec_Type = Gauge32
_As2memInMemDimenIndHashFileKBSec_Object = MibTableColumn
as2memInMemDimenIndHashFileKBSec = _As2memInMemDimenIndHashFileKBSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 30),
    _As2memInMemDimenIndHashFileKBSec_Type()
)
as2memInMemDimenIndHashFileKBSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemDimenIndHashFileKBSec.setStatus("current")
_As2memInMemDimenProtyFileKB_Type = Gauge32
_As2memInMemDimenProtyFileKB_Object = MibTableColumn
as2memInMemDimenProtyFileKB = _As2memInMemDimenProtyFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 31),
    _As2memInMemDimenProtyFileKB_Type()
)
as2memInMemDimenProtyFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemDimenProtyFileKB.setStatus("current")
_As2memInMemDimenProtyFileKBSec_Type = Gauge32
_As2memInMemDimenProtyFileKBSec_Object = MibTableColumn
as2memInMemDimenProtyFileKBSec = _As2memInMemDimenProtyFileKBSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 32),
    _As2memInMemDimenProtyFileKBSec_Type()
)
as2memInMemDimenProtyFileKBSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemDimenProtyFileKBSec.setStatus("current")
_As2memInMemDimenStringFileKB_Type = Gauge32
_As2memInMemDimenStringFileKB_Object = MibTableColumn
as2memInMemDimenStringFileKB = _As2memInMemDimenStringFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 33),
    _As2memInMemDimenStringFileKB_Type()
)
as2memInMemDimenStringFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemDimenStringFileKB.setStatus("current")
_As2memInMemDimenStringFileKBSec_Type = Gauge32
_As2memInMemDimenStringFileKBSec_Object = MibTableColumn
as2memInMemDimenStringFileKBSec = _As2memInMemDimenStringFileKBSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 34),
    _As2memInMemDimenStringFileKBSec_Type()
)
as2memInMemDimenStringFileKBSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemDimenStringFileKBSec.setStatus("current")
_As2memInMemFactAggregationFileKB_Type = Gauge32
_As2memInMemFactAggregationFileKB_Object = MibTableColumn
as2memInMemFactAggregationFileKB = _As2memInMemFactAggregationFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 35),
    _As2memInMemFactAggregationFileKB_Type()
)
as2memInMemFactAggregationFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemFactAggregationFileKB.setStatus("current")
_As2memInMemFactAggregatFileKBSec_Type = Gauge32
_As2memInMemFactAggregatFileKBSec_Object = MibTableColumn
as2memInMemFactAggregatFileKBSec = _As2memInMemFactAggregatFileKBSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 36),
    _As2memInMemFactAggregatFileKBSec_Type()
)
as2memInMemFactAggregatFileKBSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemFactAggregatFileKBSec.setStatus("current")
_As2memInMemoryFactDataFileKB_Type = Gauge32
_As2memInMemoryFactDataFileKB_Object = MibTableColumn
as2memInMemoryFactDataFileKB = _As2memInMemoryFactDataFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 37),
    _As2memInMemoryFactDataFileKB_Type()
)
as2memInMemoryFactDataFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemoryFactDataFileKB.setStatus("current")
_As2memInMemFactDataFileKBSec_Type = Gauge32
_As2memInMemFactDataFileKBSec_Object = MibTableColumn
as2memInMemFactDataFileKBSec = _As2memInMemFactDataFileKBSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 38),
    _As2memInMemFactDataFileKBSec_Type()
)
as2memInMemFactDataFileKBSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemFactDataFileKBSec.setStatus("current")
_As2memInMemoryFactStringFileKB_Type = Gauge32
_As2memInMemoryFactStringFileKB_Object = MibTableColumn
as2memInMemoryFactStringFileKB = _As2memInMemoryFactStringFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 39),
    _As2memInMemoryFactStringFileKB_Type()
)
as2memInMemoryFactStringFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemoryFactStringFileKB.setStatus("current")
_As2memInMemFactStringFileKBSec_Type = Gauge32
_As2memInMemFactStringFileKBSec_Object = MibTableColumn
as2memInMemFactStringFileKBSec = _As2memInMemFactStringFileKBSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 40),
    _As2memInMemFactStringFileKBSec_Type()
)
as2memInMemFactStringFileKBSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemFactStringFileKBSec.setStatus("current")
_As2memInMemoryMapFileKB_Type = Gauge32
_As2memInMemoryMapFileKB_Object = MibTableColumn
as2memInMemoryMapFileKB = _As2memInMemoryMapFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 41),
    _As2memInMemoryMapFileKB_Type()
)
as2memInMemoryMapFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemoryMapFileKB.setStatus("current")
_As2memInMemoryMapFileKBPerSec_Type = Gauge32
_As2memInMemoryMapFileKBPerSec_Object = MibTableColumn
as2memInMemoryMapFileKBPerSec = _As2memInMemoryMapFileKBPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 42),
    _As2memInMemoryMapFileKBPerSec_Type()
)
as2memInMemoryMapFileKBPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemoryMapFileKBPerSec.setStatus("current")
_As2memInMemoryOtherFileKB_Type = Gauge32
_As2memInMemoryOtherFileKB_Object = MibTableColumn
as2memInMemoryOtherFileKB = _As2memInMemoryOtherFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 43),
    _As2memInMemoryOtherFileKB_Type()
)
as2memInMemoryOtherFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemoryOtherFileKB.setStatus("current")
_As2memInMemoryOtherFileKBPerSec_Type = Gauge32
_As2memInMemoryOtherFileKBPerSec_Object = MibTableColumn
as2memInMemoryOtherFileKBPerSec = _As2memInMemoryOtherFileKBPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 44),
    _As2memInMemoryOtherFileKBPerSec_Type()
)
as2memInMemoryOtherFileKBPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memInMemoryOtherFileKBPerSec.setStatus("current")
_As2memMapFiles_Type = Gauge32
_As2memMapFiles_Object = MibTableColumn
as2memMapFiles = _As2memMapFiles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 45),
    _As2memMapFiles_Type()
)
as2memMapFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memMapFiles.setStatus("current")
_As2memMemoryLimitHighKB_Type = Gauge32
_As2memMemoryLimitHighKB_Object = MibTableColumn
as2memMemoryLimitHighKB = _As2memMemoryLimitHighKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 46),
    _As2memMemoryLimitHighKB_Type()
)
as2memMemoryLimitHighKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memMemoryLimitHighKB.setStatus("current")
_As2memMemoryLimitLowKB_Type = Gauge32
_As2memMemoryLimitLowKB_Object = MibTableColumn
as2memMemoryLimitLowKB = _As2memMemoryLimitLowKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 47),
    _As2memMemoryLimitLowKB_Type()
)
as2memMemoryLimitLowKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memMemoryLimitLowKB.setStatus("current")
_As2memMemoryUsageKB_Type = Gauge32
_As2memMemoryUsageKB_Object = MibTableColumn
as2memMemoryUsageKB = _As2memMemoryUsageKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 48),
    _As2memMemoryUsageKB_Type()
)
as2memMemoryUsageKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memMemoryUsageKB.setStatus("current")
_As2memOtherFiles_Type = Gauge32
_As2memOtherFiles_Object = MibTableColumn
as2memOtherFiles = _As2memOtherFiles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 49),
    _As2memOtherFiles_Type()
)
as2memOtherFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memOtherFiles.setStatus("current")
_As2memPagePool1AllocKB_Type = Gauge32
_As2memPagePool1AllocKB_Object = MibTableColumn
as2memPagePool1AllocKB = _As2memPagePool1AllocKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 50),
    _As2memPagePool1AllocKB_Type()
)
as2memPagePool1AllocKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPagePool1AllocKB.setStatus("current")
_As2memPagePool1LookasideKB_Type = Gauge32
_As2memPagePool1LookasideKB_Object = MibTableColumn
as2memPagePool1LookasideKB = _As2memPagePool1LookasideKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 51),
    _As2memPagePool1LookasideKB_Type()
)
as2memPagePool1LookasideKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPagePool1LookasideKB.setStatus("current")
_As2memPagePool64AllocKB_Type = Gauge32
_As2memPagePool64AllocKB_Object = MibTableColumn
as2memPagePool64AllocKB = _As2memPagePool64AllocKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 52),
    _As2memPagePool64AllocKB_Type()
)
as2memPagePool64AllocKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPagePool64AllocKB.setStatus("current")
_As2memPagePool64LookasideKB_Type = Gauge32
_As2memPagePool64LookasideKB_Object = MibTableColumn
as2memPagePool64LookasideKB = _As2memPagePool64LookasideKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 53),
    _As2memPagePool64LookasideKB_Type()
)
as2memPagePool64LookasideKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPagePool64LookasideKB.setStatus("current")
_As2memPagePool8AllocKB_Type = Gauge32
_As2memPagePool8AllocKB_Object = MibTableColumn
as2memPagePool8AllocKB = _As2memPagePool8AllocKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 54),
    _As2memPagePool8AllocKB_Type()
)
as2memPagePool8AllocKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPagePool8AllocKB.setStatus("current")
_As2memPagePool8LookasideKB_Type = Gauge32
_As2memPagePool8LookasideKB_Object = MibTableColumn
as2memPagePool8LookasideKB = _As2memPagePool8LookasideKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 55),
    _As2memPagePool8LookasideKB_Type()
)
as2memPagePool8LookasideKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPagePool8LookasideKB.setStatus("current")
_As2memPotenMemAggregatMapFileKB_Type = Gauge32
_As2memPotenMemAggregatMapFileKB_Object = MibTableColumn
as2memPotenMemAggregatMapFileKB = _As2memPotenMemAggregatMapFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 56),
    _As2memPotenMemAggregatMapFileKB_Type()
)
as2memPotenMemAggregatMapFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPotenMemAggregatMapFileKB.setStatus("current")
_As2memPotenMemDimenIndHashFilKB_Type = Gauge32
_As2memPotenMemDimenIndHashFilKB_Object = MibTableColumn
as2memPotenMemDimenIndHashFilKB = _As2memPotenMemDimenIndHashFilKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 57),
    _As2memPotenMemDimenIndHashFilKB_Type()
)
as2memPotenMemDimenIndHashFilKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPotenMemDimenIndHashFilKB.setStatus("current")
_As2memPotenMemDimenProFileKB_Type = Gauge32
_As2memPotenMemDimenProFileKB_Object = MibTableColumn
as2memPotenMemDimenProFileKB = _As2memPotenMemDimenProFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 58),
    _As2memPotenMemDimenProFileKB_Type()
)
as2memPotenMemDimenProFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPotenMemDimenProFileKB.setStatus("current")
_As2memPotenMemDimenStringFileKB_Type = Gauge32
_As2memPotenMemDimenStringFileKB_Object = MibTableColumn
as2memPotenMemDimenStringFileKB = _As2memPotenMemDimenStringFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 59),
    _As2memPotenMemDimenStringFileKB_Type()
)
as2memPotenMemDimenStringFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPotenMemDimenStringFileKB.setStatus("current")
_As2memPotenMemFactAggregFileKB_Type = Gauge32
_As2memPotenMemFactAggregFileKB_Object = MibTableColumn
as2memPotenMemFactAggregFileKB = _As2memPotenMemFactAggregFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 60),
    _As2memPotenMemFactAggregFileKB_Type()
)
as2memPotenMemFactAggregFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPotenMemFactAggregFileKB.setStatus("current")
_As2memPotenMemFactDataFileKB_Type = Gauge32
_As2memPotenMemFactDataFileKB_Object = MibTableColumn
as2memPotenMemFactDataFileKB = _As2memPotenMemFactDataFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 61),
    _As2memPotenMemFactDataFileKB_Type()
)
as2memPotenMemFactDataFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPotenMemFactDataFileKB.setStatus("current")
_As2memPotenMemFactStringFileKB_Type = Gauge32
_As2memPotenMemFactStringFileKB_Object = MibTableColumn
as2memPotenMemFactStringFileKB = _As2memPotenMemFactStringFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 62),
    _As2memPotenMemFactStringFileKB_Type()
)
as2memPotenMemFactStringFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPotenMemFactStringFileKB.setStatus("current")
_As2memPotentialInMemoryMapFileKB_Type = Gauge32
_As2memPotentialInMemoryMapFileKB_Object = MibTableColumn
as2memPotentialInMemoryMapFileKB = _As2memPotentialInMemoryMapFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 63),
    _As2memPotentialInMemoryMapFileKB_Type()
)
as2memPotentialInMemoryMapFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPotentialInMemoryMapFileKB.setStatus("current")
_As2memPotenMemOtherFileKB_Type = Gauge32
_As2memPotenMemOtherFileKB_Object = MibTableColumn
as2memPotenMemOtherFileKB = _As2memPotenMemOtherFileKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 64),
    _As2memPotenMemOtherFileKB_Type()
)
as2memPotenMemOtherFileKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memPotenMemOtherFileKB.setStatus("current")
_As2memQuotaBlocked_Type = Gauge32
_As2memQuotaBlocked_Object = MibTableColumn
as2memQuotaBlocked = _As2memQuotaBlocked_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 65),
    _As2memQuotaBlocked_Type()
)
as2memQuotaBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memQuotaBlocked.setStatus("current")
_As2memQuotaKB_Type = Gauge32
_As2memQuotaKB_Object = MibTableColumn
as2memQuotaKB = _As2memQuotaKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 8, 1, 66),
    _As2memQuotaKB_Type()
)
as2memQuotaKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2memQuotaKB.setStatus("current")
_As2ProactiveCachingTable_Object = MibTable
as2ProactiveCachingTable = _As2ProactiveCachingTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 9)
)
if mibBuilder.loadTexts:
    as2ProactiveCachingTable.setStatus("current")
_As2ProactiveCachingEntry_Object = MibTableRow
as2ProactiveCachingEntry = _As2ProactiveCachingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 9, 1)
)
as2ProactiveCachingEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "as2NameIndex"),
)
if mibBuilder.loadTexts:
    as2ProactiveCachingEntry.setStatus("current")
_As2pcNotificationsPerSec_Type = Gauge32
_As2pcNotificationsPerSec_Object = MibTableColumn
as2pcNotificationsPerSec = _As2pcNotificationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 9, 1, 1),
    _As2pcNotificationsPerSec_Type()
)
as2pcNotificationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2pcNotificationsPerSec.setStatus("current")
_As2pcProactiveCachingBeginPerSec_Type = Gauge32
_As2pcProactiveCachingBeginPerSec_Object = MibTableColumn
as2pcProactiveCachingBeginPerSec = _As2pcProactiveCachingBeginPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 9, 1, 2),
    _As2pcProactiveCachingBeginPerSec_Type()
)
as2pcProactiveCachingBeginPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2pcProactiveCachingBeginPerSec.setStatus("current")
_As2pcProactiveCachCompSec_Type = Gauge32
_As2pcProactiveCachCompSec_Object = MibTableColumn
as2pcProactiveCachCompSec = _As2pcProactiveCachCompSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 9, 1, 3),
    _As2pcProactiveCachCompSec_Type()
)
as2pcProactiveCachCompSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2pcProactiveCachCompSec.setStatus("current")
_As2pcProcessCancellationsSec_Type = Gauge32
_As2pcProcessCancellationsSec_Object = MibTableColumn
as2pcProcessCancellationsSec = _As2pcProcessCancellationsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 9, 1, 4),
    _As2pcProcessCancellationsSec_Type()
)
as2pcProcessCancellationsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2pcProcessCancellationsSec.setStatus("current")
_As2ProcAggregationsTable_Object = MibTable
as2ProcAggregationsTable = _As2ProcAggregationsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 10)
)
if mibBuilder.loadTexts:
    as2ProcAggregationsTable.setStatus("current")
_As2ProcAggregationsEntry_Object = MibTableRow
as2ProcAggregationsEntry = _As2ProcAggregationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 10, 1)
)
as2ProcAggregationsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "as2NameIndex"),
)
if mibBuilder.loadTexts:
    as2ProcAggregationsEntry.setStatus("current")
_As2paCurrentPartitions_Type = Gauge32
_As2paCurrentPartitions_Object = MibTableColumn
as2paCurrentPartitions = _As2paCurrentPartitions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 10, 1, 1),
    _As2paCurrentPartitions_Type()
)
as2paCurrentPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2paCurrentPartitions.setStatus("current")
_As2paMemorySizeBytes_Type = Gauge32
_As2paMemorySizeBytes_Object = MibTableColumn
as2paMemorySizeBytes = _As2paMemorySizeBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 10, 1, 2),
    _As2paMemorySizeBytes_Type()
)
as2paMemorySizeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2paMemorySizeBytes.setStatus("current")
_As2paMemorySizeRows_Type = Gauge32
_As2paMemorySizeRows_Object = MibTableColumn
as2paMemorySizeRows = _As2paMemorySizeRows_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 10, 1, 3),
    _As2paMemorySizeRows_Type()
)
as2paMemorySizeRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2paMemorySizeRows.setStatus("current")
_As2paRowsCreatedPerSec_Type = Gauge32
_As2paRowsCreatedPerSec_Object = MibTableColumn
as2paRowsCreatedPerSec = _As2paRowsCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 10, 1, 4),
    _As2paRowsCreatedPerSec_Type()
)
as2paRowsCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2paRowsCreatedPerSec.setStatus("current")
_As2paRowsMergedPerSec_Type = Gauge32
_As2paRowsMergedPerSec_Object = MibTableColumn
as2paRowsMergedPerSec = _As2paRowsMergedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 10, 1, 5),
    _As2paRowsMergedPerSec_Type()
)
as2paRowsMergedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2paRowsMergedPerSec.setStatus("current")
_As2paTempFileBytesWrittenPerSec_Type = Gauge32
_As2paTempFileBytesWrittenPerSec_Object = MibTableColumn
as2paTempFileBytesWrittenPerSec = _As2paTempFileBytesWrittenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 10, 1, 6),
    _As2paTempFileBytesWrittenPerSec_Type()
)
as2paTempFileBytesWrittenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2paTempFileBytesWrittenPerSec.setStatus("current")
_As2paTempFileRowsWrittenPerSec_Type = Gauge32
_As2paTempFileRowsWrittenPerSec_Object = MibTableColumn
as2paTempFileRowsWrittenPerSec = _As2paTempFileRowsWrittenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 10, 1, 7),
    _As2paTempFileRowsWrittenPerSec_Type()
)
as2paTempFileRowsWrittenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2paTempFileRowsWrittenPerSec.setStatus("current")
_As2paTotalPartitions_Type = Gauge32
_As2paTotalPartitions_Object = MibTableColumn
as2paTotalPartitions = _As2paTotalPartitions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 10, 1, 8),
    _As2paTotalPartitions_Type()
)
as2paTotalPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2paTotalPartitions.setStatus("current")
_As2ProcIndexesTable_Object = MibTable
as2ProcIndexesTable = _As2ProcIndexesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 11)
)
if mibBuilder.loadTexts:
    as2ProcIndexesTable.setStatus("current")
_As2ProcIndexesEntry_Object = MibTableRow
as2ProcIndexesEntry = _As2ProcIndexesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 11, 1)
)
as2ProcIndexesEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "as2NameIndex"),
)
if mibBuilder.loadTexts:
    as2ProcIndexesEntry.setStatus("current")
_As2ProcIndexesCurrentPartitions_Type = Gauge32
_As2ProcIndexesCurrentPartitions_Object = MibTableColumn
as2ProcIndexesCurrentPartitions = _As2ProcIndexesCurrentPartitions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 11, 1, 1),
    _As2ProcIndexesCurrentPartitions_Type()
)
as2ProcIndexesCurrentPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ProcIndexesCurrentPartitions.setStatus("current")
_As2ProcIndexesRowsPerSec_Type = Gauge32
_As2ProcIndexesRowsPerSec_Object = MibTableColumn
as2ProcIndexesRowsPerSec = _As2ProcIndexesRowsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 11, 1, 2),
    _As2ProcIndexesRowsPerSec_Type()
)
as2ProcIndexesRowsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ProcIndexesRowsPerSec.setStatus("current")
_As2ProcIndexesTotalPartitions_Type = Gauge32
_As2ProcIndexesTotalPartitions_Object = MibTableColumn
as2ProcIndexesTotalPartitions = _As2ProcIndexesTotalPartitions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 11, 1, 3),
    _As2ProcIndexesTotalPartitions_Type()
)
as2ProcIndexesTotalPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ProcIndexesTotalPartitions.setStatus("current")
_As2ProcIndexesTotalRows_Type = Gauge32
_As2ProcIndexesTotalRows_Object = MibTableColumn
as2ProcIndexesTotalRows = _As2ProcIndexesTotalRows_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 11, 1, 4),
    _As2ProcIndexesTotalRows_Type()
)
as2ProcIndexesTotalRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ProcIndexesTotalRows.setStatus("current")
_As2ProcessingTable_Object = MibTable
as2ProcessingTable = _As2ProcessingTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 12)
)
if mibBuilder.loadTexts:
    as2ProcessingTable.setStatus("current")
_As2ProcessingEntry_Object = MibTableRow
as2ProcessingEntry = _As2ProcessingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 12, 1)
)
as2ProcessingEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "as2NameIndex"),
)
if mibBuilder.loadTexts:
    as2ProcessingEntry.setStatus("current")
_As2ProcessingRowsConvertedPerSec_Type = Gauge32
_As2ProcessingRowsConvertedPerSec_Object = MibTableColumn
as2ProcessingRowsConvertedPerSec = _As2ProcessingRowsConvertedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 12, 1, 1),
    _As2ProcessingRowsConvertedPerSec_Type()
)
as2ProcessingRowsConvertedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ProcessingRowsConvertedPerSec.setStatus("current")
_As2ProcessingRowsReadPerSec_Type = Gauge32
_As2ProcessingRowsReadPerSec_Object = MibTableColumn
as2ProcessingRowsReadPerSec = _As2ProcessingRowsReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 12, 1, 2),
    _As2ProcessingRowsReadPerSec_Type()
)
as2ProcessingRowsReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ProcessingRowsReadPerSec.setStatus("current")
_As2ProcessingRowsWrittenPerSec_Type = Gauge32
_As2ProcessingRowsWrittenPerSec_Object = MibTableColumn
as2ProcessingRowsWrittenPerSec = _As2ProcessingRowsWrittenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 12, 1, 3),
    _As2ProcessingRowsWrittenPerSec_Type()
)
as2ProcessingRowsWrittenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ProcessingRowsWrittenPerSec.setStatus("current")
_As2ProcessingTotalRowsConverted_Type = Gauge32
_As2ProcessingTotalRowsConverted_Object = MibTableColumn
as2ProcessingTotalRowsConverted = _As2ProcessingTotalRowsConverted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 12, 1, 4),
    _As2ProcessingTotalRowsConverted_Type()
)
as2ProcessingTotalRowsConverted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ProcessingTotalRowsConverted.setStatus("current")
_As2ProcessingTotalRowsRead_Type = Gauge32
_As2ProcessingTotalRowsRead_Object = MibTableColumn
as2ProcessingTotalRowsRead = _As2ProcessingTotalRowsRead_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 12, 1, 5),
    _As2ProcessingTotalRowsRead_Type()
)
as2ProcessingTotalRowsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ProcessingTotalRowsRead.setStatus("current")
_As2ProcessingTotalRowsWritten_Type = Gauge32
_As2ProcessingTotalRowsWritten_Object = MibTableColumn
as2ProcessingTotalRowsWritten = _As2ProcessingTotalRowsWritten_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 12, 1, 6),
    _As2ProcessingTotalRowsWritten_Type()
)
as2ProcessingTotalRowsWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ProcessingTotalRowsWritten.setStatus("current")
_As2StorageEngineQueryTable_Object = MibTable
as2StorageEngineQueryTable = _As2StorageEngineQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13)
)
if mibBuilder.loadTexts:
    as2StorageEngineQueryTable.setStatus("current")
_As2StorageEngineQueryEntry_Object = MibTableRow
as2StorageEngineQueryEntry = _As2StorageEngineQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1)
)
as2StorageEngineQueryEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "as2NameIndex"),
)
if mibBuilder.loadTexts:
    as2StorageEngineQueryEntry.setStatus("current")
_As2seqAggregationHitsPerSec_Type = Gauge32
_As2seqAggregationHitsPerSec_Object = MibTableColumn
as2seqAggregationHitsPerSec = _As2seqAggregationHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 1),
    _As2seqAggregationHitsPerSec_Type()
)
as2seqAggregationHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqAggregationHitsPerSec.setStatus("current")
_As2seqAggregationLookupsPerSec_Type = Gauge32
_As2seqAggregationLookupsPerSec_Object = MibTableColumn
as2seqAggregationLookupsPerSec = _As2seqAggregationLookupsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 2),
    _As2seqAggregationLookupsPerSec_Type()
)
as2seqAggregationLookupsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqAggregationLookupsPerSec.setStatus("current")
_As2seqAvgTimePerQuery_Type = Gauge32
_As2seqAvgTimePerQuery_Object = MibTableColumn
as2seqAvgTimePerQuery = _As2seqAvgTimePerQuery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 3),
    _As2seqAvgTimePerQuery_Type()
)
as2seqAvgTimePerQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqAvgTimePerQuery.setStatus("current")
_As2seqBytesSentPerSec_Type = Gauge32
_As2seqBytesSentPerSec_Object = MibTableColumn
as2seqBytesSentPerSec = _As2seqBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 4),
    _As2seqBytesSentPerSec_Type()
)
as2seqBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqBytesSentPerSec.setStatus("current")
_As2seqCalculationCacheHitsPerSec_Type = Gauge32
_As2seqCalculationCacheHitsPerSec_Object = MibTableColumn
as2seqCalculationCacheHitsPerSec = _As2seqCalculationCacheHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 5),
    _As2seqCalculationCacheHitsPerSec_Type()
)
as2seqCalculationCacheHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqCalculationCacheHitsPerSec.setStatus("current")
_As2seqCalculationCacheLookupsSec_Type = Gauge32
_As2seqCalculationCacheLookupsSec_Object = MibTableColumn
as2seqCalculationCacheLookupsSec = _As2seqCalculationCacheLookupsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 6),
    _As2seqCalculationCacheLookupsSec_Type()
)
as2seqCalculationCacheLookupsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqCalculationCacheLookupsSec.setStatus("current")
_As2seqCurrentDimensionQueries_Type = Gauge32
_As2seqCurrentDimensionQueries_Object = MibTableColumn
as2seqCurrentDimensionQueries = _As2seqCurrentDimensionQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 7),
    _As2seqCurrentDimensionQueries_Type()
)
as2seqCurrentDimensionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqCurrentDimensionQueries.setStatus("current")
_As2seqCurrentMeasureGroupQueries_Type = Gauge32
_As2seqCurrentMeasureGroupQueries_Object = MibTableColumn
as2seqCurrentMeasureGroupQueries = _As2seqCurrentMeasureGroupQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 8),
    _As2seqCurrentMeasureGroupQueries_Type()
)
as2seqCurrentMeasureGroupQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqCurrentMeasureGroupQueries.setStatus("current")
_As2seqDataBytesPerSec_Type = Gauge32
_As2seqDataBytesPerSec_Object = MibTableColumn
as2seqDataBytesPerSec = _As2seqDataBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 9),
    _As2seqDataBytesPerSec_Type()
)
as2seqDataBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqDataBytesPerSec.setStatus("current")
_As2seqDataReadsPerSec_Type = Gauge32
_As2seqDataReadsPerSec_Object = MibTableColumn
as2seqDataReadsPerSec = _As2seqDataReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 10),
    _As2seqDataReadsPerSec_Type()
)
as2seqDataReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqDataReadsPerSec.setStatus("current")
_As2seqDimensionCacheHitsPerSec_Type = Gauge32
_As2seqDimensionCacheHitsPerSec_Object = MibTableColumn
as2seqDimensionCacheHitsPerSec = _As2seqDimensionCacheHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 11),
    _As2seqDimensionCacheHitsPerSec_Type()
)
as2seqDimensionCacheHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqDimensionCacheHitsPerSec.setStatus("current")
_As2seqDimensionCacheLookupSec_Type = Gauge32
_As2seqDimensionCacheLookupSec_Object = MibTableColumn
as2seqDimensionCacheLookupSec = _As2seqDimensionCacheLookupSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 12),
    _As2seqDimensionCacheLookupSec_Type()
)
as2seqDimensionCacheLookupSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqDimensionCacheLookupSec.setStatus("current")
_As2seqDimensionQueriesPerSec_Type = Gauge32
_As2seqDimensionQueriesPerSec_Object = MibTableColumn
as2seqDimensionQueriesPerSec = _As2seqDimensionQueriesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 13),
    _As2seqDimensionQueriesPerSec_Type()
)
as2seqDimensionQueriesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqDimensionQueriesPerSec.setStatus("current")
_As2seqFlatCacheHitsPerSec_Type = Gauge32
_As2seqFlatCacheHitsPerSec_Object = MibTableColumn
as2seqFlatCacheHitsPerSec = _As2seqFlatCacheHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 14),
    _As2seqFlatCacheHitsPerSec_Type()
)
as2seqFlatCacheHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqFlatCacheHitsPerSec.setStatus("current")
_As2seqFlatCacheLookupsPerSec_Type = Gauge32
_As2seqFlatCacheLookupsPerSec_Object = MibTableColumn
as2seqFlatCacheLookupsPerSec = _As2seqFlatCacheLookupsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 15),
    _As2seqFlatCacheLookupsPerSec_Type()
)
as2seqFlatCacheLookupsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqFlatCacheLookupsPerSec.setStatus("current")
_As2seqMapBytesPerSec_Type = Gauge32
_As2seqMapBytesPerSec_Object = MibTableColumn
as2seqMapBytesPerSec = _As2seqMapBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 16),
    _As2seqMapBytesPerSec_Type()
)
as2seqMapBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqMapBytesPerSec.setStatus("current")
_As2seqMapReadsPerSec_Type = Gauge32
_As2seqMapReadsPerSec_Object = MibTableColumn
as2seqMapReadsPerSec = _As2seqMapReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 17),
    _As2seqMapReadsPerSec_Type()
)
as2seqMapReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqMapReadsPerSec.setStatus("current")
_As2seqMeasureGroupCacheHitsSec_Type = Gauge32
_As2seqMeasureGroupCacheHitsSec_Object = MibTableColumn
as2seqMeasureGroupCacheHitsSec = _As2seqMeasureGroupCacheHitsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 18),
    _As2seqMeasureGroupCacheHitsSec_Type()
)
as2seqMeasureGroupCacheHitsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqMeasureGroupCacheHitsSec.setStatus("current")
_As2seqMeasureGroupCacheLookupSec_Type = Gauge32
_As2seqMeasureGroupCacheLookupSec_Object = MibTableColumn
as2seqMeasureGroupCacheLookupSec = _As2seqMeasureGroupCacheLookupSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 19),
    _As2seqMeasureGroupCacheLookupSec_Type()
)
as2seqMeasureGroupCacheLookupSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqMeasureGroupCacheLookupSec.setStatus("current")
_As2seqMeasureGroupQueriesPerSec_Type = Gauge32
_As2seqMeasureGroupQueriesPerSec_Object = MibTableColumn
as2seqMeasureGroupQueriesPerSec = _As2seqMeasureGroupQueriesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 20),
    _As2seqMeasureGroupQueriesPerSec_Type()
)
as2seqMeasureGroupQueriesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqMeasureGroupQueriesPerSec.setStatus("current")
_As2seqNetworkRoundTripsPerSec_Type = Gauge32
_As2seqNetworkRoundTripsPerSec_Object = MibTableColumn
as2seqNetworkRoundTripsPerSec = _As2seqNetworkRoundTripsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 21),
    _As2seqNetworkRoundTripsPerSec_Type()
)
as2seqNetworkRoundTripsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqNetworkRoundTripsPerSec.setStatus("current")
_As2seqPersistedCacheHitsPerSec_Type = Gauge32
_As2seqPersistedCacheHitsPerSec_Object = MibTableColumn
as2seqPersistedCacheHitsPerSec = _As2seqPersistedCacheHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 22),
    _As2seqPersistedCacheHitsPerSec_Type()
)
as2seqPersistedCacheHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqPersistedCacheHitsPerSec.setStatus("current")
_As2seqsistedCacheLookupsSec_Type = Gauge32
_As2seqsistedCacheLookupsSec_Object = MibTableColumn
as2seqsistedCacheLookupsSec = _As2seqsistedCacheLookupsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 23),
    _As2seqsistedCacheLookupsSec_Type()
)
as2seqsistedCacheLookupsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqsistedCacheLookupsSec.setStatus("current")
_As2seqQueriesAnsweredPerSec_Type = Gauge32
_As2seqQueriesAnsweredPerSec_Object = MibTableColumn
as2seqQueriesAnsweredPerSec = _As2seqQueriesAnsweredPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 24),
    _As2seqQueriesAnsweredPerSec_Type()
)
as2seqQueriesAnsweredPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqQueriesAnsweredPerSec.setStatus("current")
_As2seqQueryFromCacheDirectSec_Type = Gauge32
_As2seqQueryFromCacheDirectSec_Object = MibTableColumn
as2seqQueryFromCacheDirectSec = _As2seqQueryFromCacheDirectSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 25),
    _As2seqQueryFromCacheDirectSec_Type()
)
as2seqQueryFromCacheDirectSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqQueryFromCacheDirectSec.setStatus("current")
_As2seqQueryFromCacheFilteredSec_Type = Gauge32
_As2seqQueryFromCacheFilteredSec_Object = MibTableColumn
as2seqQueryFromCacheFilteredSec = _As2seqQueryFromCacheFilteredSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 26),
    _As2seqQueryFromCacheFilteredSec_Type()
)
as2seqQueryFromCacheFilteredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqQueryFromCacheFilteredSec.setStatus("current")
_As2seqQueriesFromFilePerSec_Type = Gauge32
_As2seqQueriesFromFilePerSec_Object = MibTableColumn
as2seqQueriesFromFilePerSec = _As2seqQueriesFromFilePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 27),
    _As2seqQueriesFromFilePerSec_Type()
)
as2seqQueriesFromFilePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqQueriesFromFilePerSec.setStatus("current")
_As2seqRowsSentPerSec_Type = Gauge32
_As2seqRowsSentPerSec_Object = MibTableColumn
as2seqRowsSentPerSec = _As2seqRowsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 28),
    _As2seqRowsSentPerSec_Type()
)
as2seqRowsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqRowsSentPerSec.setStatus("current")
_As2seqTotalBytesSent_Type = Gauge32
_As2seqTotalBytesSent_Object = MibTableColumn
as2seqTotalBytesSent = _As2seqTotalBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 29),
    _As2seqTotalBytesSent_Type()
)
as2seqTotalBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqTotalBytesSent.setStatus("current")
_As2seqTotalDimensionQueries_Type = Gauge32
_As2seqTotalDimensionQueries_Object = MibTableColumn
as2seqTotalDimensionQueries = _As2seqTotalDimensionQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 30),
    _As2seqTotalDimensionQueries_Type()
)
as2seqTotalDimensionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqTotalDimensionQueries.setStatus("current")
_As2seqTotalMeasureGroupQueries_Type = Gauge32
_As2seqTotalMeasureGroupQueries_Object = MibTableColumn
as2seqTotalMeasureGroupQueries = _As2seqTotalMeasureGroupQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 31),
    _As2seqTotalMeasureGroupQueries_Type()
)
as2seqTotalMeasureGroupQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqTotalMeasureGroupQueries.setStatus("current")
_As2seqTotalNetworkRoundTrips_Type = Gauge32
_As2seqTotalNetworkRoundTrips_Object = MibTableColumn
as2seqTotalNetworkRoundTrips = _As2seqTotalNetworkRoundTrips_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 32),
    _As2seqTotalNetworkRoundTrips_Type()
)
as2seqTotalNetworkRoundTrips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqTotalNetworkRoundTrips.setStatus("current")
_As2seqTotalQueriesAnswered_Type = Gauge32
_As2seqTotalQueriesAnswered_Object = MibTableColumn
as2seqTotalQueriesAnswered = _As2seqTotalQueriesAnswered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 33),
    _As2seqTotalQueriesAnswered_Type()
)
as2seqTotalQueriesAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqTotalQueriesAnswered.setStatus("current")
_As2seqTotalQueryFromCacheDirect_Type = Gauge32
_As2seqTotalQueryFromCacheDirect_Object = MibTableColumn
as2seqTotalQueryFromCacheDirect = _As2seqTotalQueryFromCacheDirect_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 34),
    _As2seqTotalQueryFromCacheDirect_Type()
)
as2seqTotalQueryFromCacheDirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqTotalQueryFromCacheDirect.setStatus("current")
_As2seqTotalQueryFromCachFiltered_Type = Gauge32
_As2seqTotalQueryFromCachFiltered_Object = MibTableColumn
as2seqTotalQueryFromCachFiltered = _As2seqTotalQueryFromCachFiltered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 35),
    _As2seqTotalQueryFromCachFiltered_Type()
)
as2seqTotalQueryFromCachFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqTotalQueryFromCachFiltered.setStatus("current")
_As2seqTotalQueriesFromFile_Type = Gauge32
_As2seqTotalQueriesFromFile_Object = MibTableColumn
as2seqTotalQueriesFromFile = _As2seqTotalQueriesFromFile_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 36),
    _As2seqTotalQueriesFromFile_Type()
)
as2seqTotalQueriesFromFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqTotalQueriesFromFile.setStatus("current")
_As2seqTotalRowsSent_Type = Gauge32
_As2seqTotalRowsSent_Object = MibTableColumn
as2seqTotalRowsSent = _As2seqTotalRowsSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 13, 1, 37),
    _As2seqTotalRowsSent_Type()
)
as2seqTotalRowsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2seqTotalRowsSent.setStatus("current")
_As2ThreadsTable_Object = MibTable
as2ThreadsTable = _As2ThreadsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14)
)
if mibBuilder.loadTexts:
    as2ThreadsTable.setStatus("current")
_As2ThreadsEntry_Object = MibTableRow
as2ThreadsEntry = _As2ThreadsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1)
)
as2ThreadsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "as2NameIndex"),
)
if mibBuilder.loadTexts:
    as2ThreadsEntry.setStatus("current")
_As2ThdsLongParsingBusyThreads_Type = Gauge32
_As2ThdsLongParsingBusyThreads_Object = MibTableColumn
as2ThdsLongParsingBusyThreads = _As2ThdsLongParsingBusyThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 1),
    _As2ThdsLongParsingBusyThreads_Type()
)
as2ThdsLongParsingBusyThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsLongParsingBusyThreads.setStatus("current")
_As2ThdsLongParsingIdleThreads_Type = Gauge32
_As2ThdsLongParsingIdleThreads_Object = MibTableColumn
as2ThdsLongParsingIdleThreads = _As2ThdsLongParsingIdleThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 2),
    _As2ThdsLongParsingIdleThreads_Type()
)
as2ThdsLongParsingIdleThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsLongParsingIdleThreads.setStatus("current")
_As2ThdsLongParsingJobQueueLength_Type = Gauge32
_As2ThdsLongParsingJobQueueLength_Object = MibTableColumn
as2ThdsLongParsingJobQueueLength = _As2ThdsLongParsingJobQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 3),
    _As2ThdsLongParsingJobQueueLength_Type()
)
as2ThdsLongParsingJobQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsLongParsingJobQueueLength.setStatus("current")
_As2ThdsLongParsingJobRate_Type = Gauge32
_As2ThdsLongParsingJobRate_Object = MibTableColumn
as2ThdsLongParsingJobRate = _As2ThdsLongParsingJobRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 4),
    _As2ThdsLongParsingJobRate_Type()
)
as2ThdsLongParsingJobRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsLongParsingJobRate.setStatus("current")
_As2ThdsProcessingPoolBusyThreads_Type = Gauge32
_As2ThdsProcessingPoolBusyThreads_Object = MibTableColumn
as2ThdsProcessingPoolBusyThreads = _As2ThdsProcessingPoolBusyThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 5),
    _As2ThdsProcessingPoolBusyThreads_Type()
)
as2ThdsProcessingPoolBusyThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsProcessingPoolBusyThreads.setStatus("current")
_As2ThdsProcessingPoolIdleThreads_Type = Gauge32
_As2ThdsProcessingPoolIdleThreads_Object = MibTableColumn
as2ThdsProcessingPoolIdleThreads = _As2ThdsProcessingPoolIdleThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 6),
    _As2ThdsProcessingPoolIdleThreads_Type()
)
as2ThdsProcessingPoolIdleThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsProcessingPoolIdleThreads.setStatus("current")
_As2ThdsProcessPoolJobQueueLength_Type = Gauge32
_As2ThdsProcessPoolJobQueueLength_Object = MibTableColumn
as2ThdsProcessPoolJobQueueLength = _As2ThdsProcessPoolJobQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 7),
    _As2ThdsProcessPoolJobQueueLength_Type()
)
as2ThdsProcessPoolJobQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsProcessPoolJobQueueLength.setStatus("current")
_As2ThdsProcessingPoolJobRate_Type = Gauge32
_As2ThdsProcessingPoolJobRate_Object = MibTableColumn
as2ThdsProcessingPoolJobRate = _As2ThdsProcessingPoolJobRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 8),
    _As2ThdsProcessingPoolJobRate_Type()
)
as2ThdsProcessingPoolJobRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsProcessingPoolJobRate.setStatus("current")
_As2ThdsQueryPoolBusyThreads_Type = Gauge32
_As2ThdsQueryPoolBusyThreads_Object = MibTableColumn
as2ThdsQueryPoolBusyThreads = _As2ThdsQueryPoolBusyThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 9),
    _As2ThdsQueryPoolBusyThreads_Type()
)
as2ThdsQueryPoolBusyThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsQueryPoolBusyThreads.setStatus("current")
_As2ThdsQueryPoolIdleThreads_Type = Gauge32
_As2ThdsQueryPoolIdleThreads_Object = MibTableColumn
as2ThdsQueryPoolIdleThreads = _As2ThdsQueryPoolIdleThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 10),
    _As2ThdsQueryPoolIdleThreads_Type()
)
as2ThdsQueryPoolIdleThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsQueryPoolIdleThreads.setStatus("current")
_As2ThdsQueryPoolJobQueueLength_Type = Gauge32
_As2ThdsQueryPoolJobQueueLength_Object = MibTableColumn
as2ThdsQueryPoolJobQueueLength = _As2ThdsQueryPoolJobQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 11),
    _As2ThdsQueryPoolJobQueueLength_Type()
)
as2ThdsQueryPoolJobQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsQueryPoolJobQueueLength.setStatus("current")
_As2ThdsQueryPoolJobRate_Type = Gauge32
_As2ThdsQueryPoolJobRate_Object = MibTableColumn
as2ThdsQueryPoolJobRate = _As2ThdsQueryPoolJobRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 12),
    _As2ThdsQueryPoolJobRate_Type()
)
as2ThdsQueryPoolJobRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsQueryPoolJobRate.setStatus("current")
_As2ThdsShortParsingBusyThreads_Type = Gauge32
_As2ThdsShortParsingBusyThreads_Object = MibTableColumn
as2ThdsShortParsingBusyThreads = _As2ThdsShortParsingBusyThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 13),
    _As2ThdsShortParsingBusyThreads_Type()
)
as2ThdsShortParsingBusyThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsShortParsingBusyThreads.setStatus("current")
_As2ThdsShortParsingIdleThreads_Type = Gauge32
_As2ThdsShortParsingIdleThreads_Object = MibTableColumn
as2ThdsShortParsingIdleThreads = _As2ThdsShortParsingIdleThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 14),
    _As2ThdsShortParsingIdleThreads_Type()
)
as2ThdsShortParsingIdleThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsShortParsingIdleThreads.setStatus("current")
_As2ThdsShortParsingJobQueueLeng_Type = Gauge32
_As2ThdsShortParsingJobQueueLeng_Object = MibTableColumn
as2ThdsShortParsingJobQueueLeng = _As2ThdsShortParsingJobQueueLeng_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 15),
    _As2ThdsShortParsingJobQueueLeng_Type()
)
as2ThdsShortParsingJobQueueLeng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsShortParsingJobQueueLeng.setStatus("current")
_As2ThdsShortParsingJobRate_Type = Gauge32
_As2ThdsShortParsingJobRate_Object = MibTableColumn
as2ThdsShortParsingJobRate = _As2ThdsShortParsingJobRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 1, 14, 1, 16),
    _As2ThdsShortParsingJobRate_Type()
)
as2ThdsShortParsingJobRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    as2ThdsShortParsingJobRate.setStatus("current")
_SqlServerEngineV2_ObjectIdentity = ObjectIdentity
sqlServerEngineV2 = _SqlServerEngineV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2)
)
_Ss2NameTable_Object = MibTable
ss2NameTable = _Ss2NameTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 1)
)
if mibBuilder.loadTexts:
    ss2NameTable.setStatus("current")
_Ss2NameEntry_Object = MibTableRow
ss2NameEntry = _Ss2NameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 1, 1)
)
ss2NameEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2NameEntry.setStatus("current")


class _Ss2NameIndex_Type(Integer32):
    """Custom type ss2NameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ss2NameIndex_Type.__name__ = "Integer32"
_Ss2NameIndex_Object = MibTableColumn
ss2NameIndex = _Ss2NameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 1, 1, 1),
    _Ss2NameIndex_Type()
)
ss2NameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2NameIndex.setStatus("current")
_Ss2NameInstance_Type = InstanceName
_Ss2NameInstance_Object = MibTableColumn
ss2NameInstance = _Ss2NameInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 1, 1, 2),
    _Ss2NameInstance_Type()
)
ss2NameInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2NameInstance.setStatus("current")
_Ss2AccessMethodsTable_Object = MibTable
ss2AccessMethodsTable = _Ss2AccessMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2)
)
if mibBuilder.loadTexts:
    ss2AccessMethodsTable.setStatus("current")
_Ss2AccessMethodsEntry_Object = MibTableRow
ss2AccessMethodsEntry = _Ss2AccessMethodsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1)
)
ss2AccessMethodsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2AccessMethodsEntry.setStatus("current")
_Ss2amAUCleanupBatchesPerSec_Type = Gauge32
_Ss2amAUCleanupBatchesPerSec_Object = MibTableColumn
ss2amAUCleanupBatchesPerSec = _Ss2amAUCleanupBatchesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 1),
    _Ss2amAUCleanupBatchesPerSec_Type()
)
ss2amAUCleanupBatchesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amAUCleanupBatchesPerSec.setStatus("current")
_Ss2amAUCleanupsPerSec_Type = Gauge32
_Ss2amAUCleanupsPerSec_Object = MibTableColumn
ss2amAUCleanupsPerSec = _Ss2amAUCleanupsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 2),
    _Ss2amAUCleanupsPerSec_Type()
)
ss2amAUCleanupsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amAUCleanupsPerSec.setStatus("current")
_Ss2amByReferenceLobCreateCount_Type = Gauge32
_Ss2amByReferenceLobCreateCount_Object = MibTableColumn
ss2amByReferenceLobCreateCount = _Ss2amByReferenceLobCreateCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 3),
    _Ss2amByReferenceLobCreateCount_Type()
)
ss2amByReferenceLobCreateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amByReferenceLobCreateCount.setStatus("current")
_Ss2amByReferenceLobUseCount_Type = Gauge32
_Ss2amByReferenceLobUseCount_Object = MibTableColumn
ss2amByReferenceLobUseCount = _Ss2amByReferenceLobUseCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 4),
    _Ss2amByReferenceLobUseCount_Type()
)
ss2amByReferenceLobUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amByReferenceLobUseCount.setStatus("current")
_Ss2amCountLobReadahead_Type = Gauge32
_Ss2amCountLobReadahead_Object = MibTableColumn
ss2amCountLobReadahead = _Ss2amCountLobReadahead_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 5),
    _Ss2amCountLobReadahead_Type()
)
ss2amCountLobReadahead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amCountLobReadahead.setStatus("current")
_Ss2amCountPullInRow_Type = Gauge32
_Ss2amCountPullInRow_Object = MibTableColumn
ss2amCountPullInRow = _Ss2amCountPullInRow_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 6),
    _Ss2amCountPullInRow_Type()
)
ss2amCountPullInRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amCountPullInRow.setStatus("current")
_Ss2amCountPushOffRow_Type = Gauge32
_Ss2amCountPushOffRow_Object = MibTableColumn
ss2amCountPushOffRow = _Ss2amCountPushOffRow_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 7),
    _Ss2amCountPushOffRow_Type()
)
ss2amCountPushOffRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amCountPushOffRow.setStatus("current")
_Ss2amDeferredDroppedRowsets_Type = Gauge32
_Ss2amDeferredDroppedRowsets_Object = MibTableColumn
ss2amDeferredDroppedRowsets = _Ss2amDeferredDroppedRowsets_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 8),
    _Ss2amDeferredDroppedRowsets_Type()
)
ss2amDeferredDroppedRowsets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amDeferredDroppedRowsets.setStatus("current")
_Ss2amDeferredDroppedAUs_Type = Gauge32
_Ss2amDeferredDroppedAUs_Object = MibTableColumn
ss2amDeferredDroppedAUs = _Ss2amDeferredDroppedAUs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 9),
    _Ss2amDeferredDroppedAUs_Type()
)
ss2amDeferredDroppedAUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amDeferredDroppedAUs.setStatus("current")
_Ss2amDroppedRowsetCleanupsPerSec_Type = Gauge32
_Ss2amDroppedRowsetCleanupsPerSec_Object = MibTableColumn
ss2amDroppedRowsetCleanupsPerSec = _Ss2amDroppedRowsetCleanupsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 10),
    _Ss2amDroppedRowsetCleanupsPerSec_Type()
)
ss2amDroppedRowsetCleanupsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amDroppedRowsetCleanupsPerSec.setStatus("current")
_Ss2amDroppedRowsetsSkippedPerSec_Type = Gauge32
_Ss2amDroppedRowsetsSkippedPerSec_Object = MibTableColumn
ss2amDroppedRowsetsSkippedPerSec = _Ss2amDroppedRowsetsSkippedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 11),
    _Ss2amDroppedRowsetsSkippedPerSec_Type()
)
ss2amDroppedRowsetsSkippedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amDroppedRowsetsSkippedPerSec.setStatus("current")
_Ss2amExtentDeallocationsPerSec_Type = Gauge32
_Ss2amExtentDeallocationsPerSec_Object = MibTableColumn
ss2amExtentDeallocationsPerSec = _Ss2amExtentDeallocationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 12),
    _Ss2amExtentDeallocationsPerSec_Type()
)
ss2amExtentDeallocationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amExtentDeallocationsPerSec.setStatus("current")
_Ss2amExtentsAllocatedPerSec_Type = Gauge32
_Ss2amExtentsAllocatedPerSec_Object = MibTableColumn
ss2amExtentsAllocatedPerSec = _Ss2amExtentsAllocatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 13),
    _Ss2amExtentsAllocatedPerSec_Type()
)
ss2amExtentsAllocatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amExtentsAllocatedPerSec.setStatus("current")
_Ss2amFailedAUCleanupBatchesSec_Type = Gauge32
_Ss2amFailedAUCleanupBatchesSec_Object = MibTableColumn
ss2amFailedAUCleanupBatchesSec = _Ss2amFailedAUCleanupBatchesSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 14),
    _Ss2amFailedAUCleanupBatchesSec_Type()
)
ss2amFailedAUCleanupBatchesSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amFailedAUCleanupBatchesSec.setStatus("current")
_Ss2amFailedLeafPageCookie_Type = Gauge32
_Ss2amFailedLeafPageCookie_Object = MibTableColumn
ss2amFailedLeafPageCookie = _Ss2amFailedLeafPageCookie_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 15),
    _Ss2amFailedLeafPageCookie_Type()
)
ss2amFailedLeafPageCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amFailedLeafPageCookie.setStatus("current")
_Ss2amFailedTreePageCookie_Type = Gauge32
_Ss2amFailedTreePageCookie_Object = MibTableColumn
ss2amFailedTreePageCookie = _Ss2amFailedTreePageCookie_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 16),
    _Ss2amFailedTreePageCookie_Type()
)
ss2amFailedTreePageCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amFailedTreePageCookie.setStatus("current")
_Ss2amForwardedRecordsPerSec_Type = Gauge32
_Ss2amForwardedRecordsPerSec_Object = MibTableColumn
ss2amForwardedRecordsPerSec = _Ss2amForwardedRecordsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 17),
    _Ss2amForwardedRecordsPerSec_Type()
)
ss2amForwardedRecordsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amForwardedRecordsPerSec.setStatus("current")
_Ss2amFreeSpacePageFetchesPerSec_Type = Gauge32
_Ss2amFreeSpacePageFetchesPerSec_Object = MibTableColumn
ss2amFreeSpacePageFetchesPerSec = _Ss2amFreeSpacePageFetchesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 18),
    _Ss2amFreeSpacePageFetchesPerSec_Type()
)
ss2amFreeSpacePageFetchesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amFreeSpacePageFetchesPerSec.setStatus("current")
_Ss2amFreeSpaceScansPerSec_Type = Gauge32
_Ss2amFreeSpaceScansPerSec_Object = MibTableColumn
ss2amFreeSpaceScansPerSec = _Ss2amFreeSpaceScansPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 19),
    _Ss2amFreeSpaceScansPerSec_Type()
)
ss2amFreeSpaceScansPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amFreeSpaceScansPerSec.setStatus("current")
_Ss2amFullScansPerSec_Type = Gauge32
_Ss2amFullScansPerSec_Object = MibTableColumn
ss2amFullScansPerSec = _Ss2amFullScansPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 20),
    _Ss2amFullScansPerSec_Type()
)
ss2amFullScansPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amFullScansPerSec.setStatus("current")
_Ss2amIndexSearchesPerSec_Type = Gauge32
_Ss2amIndexSearchesPerSec_Object = MibTableColumn
ss2amIndexSearchesPerSec = _Ss2amIndexSearchesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 21),
    _Ss2amIndexSearchesPerSec_Type()
)
ss2amIndexSearchesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amIndexSearchesPerSec.setStatus("current")
_Ss2amLobHandleCreateCount_Type = Gauge32
_Ss2amLobHandleCreateCount_Object = MibTableColumn
ss2amLobHandleCreateCount = _Ss2amLobHandleCreateCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 22),
    _Ss2amLobHandleCreateCount_Type()
)
ss2amLobHandleCreateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amLobHandleCreateCount.setStatus("current")
_Ss2amLobHandleDestroyCount_Type = Gauge32
_Ss2amLobHandleDestroyCount_Object = MibTableColumn
ss2amLobHandleDestroyCount = _Ss2amLobHandleDestroyCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 23),
    _Ss2amLobHandleDestroyCount_Type()
)
ss2amLobHandleDestroyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amLobHandleDestroyCount.setStatus("current")
_Ss2amLobSSProviderCreateCount_Type = Gauge32
_Ss2amLobSSProviderCreateCount_Object = MibTableColumn
ss2amLobSSProviderCreateCount = _Ss2amLobSSProviderCreateCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 24),
    _Ss2amLobSSProviderCreateCount_Type()
)
ss2amLobSSProviderCreateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amLobSSProviderCreateCount.setStatus("current")
_Ss2amLobSSProviderDestroyCount_Type = Gauge32
_Ss2amLobSSProviderDestroyCount_Object = MibTableColumn
ss2amLobSSProviderDestroyCount = _Ss2amLobSSProviderDestroyCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 25),
    _Ss2amLobSSProviderDestroyCount_Type()
)
ss2amLobSSProviderDestroyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amLobSSProviderDestroyCount.setStatus("current")
_Ss2amLobSSProvideTruncationCount_Type = Gauge32
_Ss2amLobSSProvideTruncationCount_Object = MibTableColumn
ss2amLobSSProvideTruncationCount = _Ss2amLobSSProvideTruncationCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 26),
    _Ss2amLobSSProvideTruncationCount_Type()
)
ss2amLobSSProvideTruncationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amLobSSProvideTruncationCount.setStatus("current")
_Ss2amMixedPageAllocationsPerSec_Type = Gauge32
_Ss2amMixedPageAllocationsPerSec_Object = MibTableColumn
ss2amMixedPageAllocationsPerSec = _Ss2amMixedPageAllocationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 27),
    _Ss2amMixedPageAllocationsPerSec_Type()
)
ss2amMixedPageAllocationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amMixedPageAllocationsPerSec.setStatus("current")
_Ss2amPageDeallocationsPerSec_Type = Gauge32
_Ss2amPageDeallocationsPerSec_Object = MibTableColumn
ss2amPageDeallocationsPerSec = _Ss2amPageDeallocationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 28),
    _Ss2amPageDeallocationsPerSec_Type()
)
ss2amPageDeallocationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amPageDeallocationsPerSec.setStatus("current")
_Ss2amPageSplitsPerSec_Type = Gauge32
_Ss2amPageSplitsPerSec_Object = MibTableColumn
ss2amPageSplitsPerSec = _Ss2amPageSplitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 29),
    _Ss2amPageSplitsPerSec_Type()
)
ss2amPageSplitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amPageSplitsPerSec.setStatus("current")
_Ss2amPageCompressionAttemptsSec_Type = Gauge32
_Ss2amPageCompressionAttemptsSec_Object = MibTableColumn
ss2amPageCompressionAttemptsSec = _Ss2amPageCompressionAttemptsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 30),
    _Ss2amPageCompressionAttemptsSec_Type()
)
ss2amPageCompressionAttemptsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amPageCompressionAttemptsSec.setStatus("current")
_Ss2amPagesAllocatedPerSec_Type = Gauge32
_Ss2amPagesAllocatedPerSec_Object = MibTableColumn
ss2amPagesAllocatedPerSec = _Ss2amPagesAllocatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 31),
    _Ss2amPagesAllocatedPerSec_Type()
)
ss2amPagesAllocatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amPagesAllocatedPerSec.setStatus("current")
_Ss2amPagesCompressedPerSec_Type = Gauge32
_Ss2amPagesCompressedPerSec_Object = MibTableColumn
ss2amPagesCompressedPerSec = _Ss2amPagesCompressedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 32),
    _Ss2amPagesCompressedPerSec_Type()
)
ss2amPagesCompressedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amPagesCompressedPerSec.setStatus("current")
_Ss2amProbeScansPerSec_Type = Gauge32
_Ss2amProbeScansPerSec_Object = MibTableColumn
ss2amProbeScansPerSec = _Ss2amProbeScansPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 33),
    _Ss2amProbeScansPerSec_Type()
)
ss2amProbeScansPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amProbeScansPerSec.setStatus("current")
_Ss2amRangeScansPerSec_Type = Gauge32
_Ss2amRangeScansPerSec_Object = MibTableColumn
ss2amRangeScansPerSec = _Ss2amRangeScansPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 34),
    _Ss2amRangeScansPerSec_Type()
)
ss2amRangeScansPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amRangeScansPerSec.setStatus("current")
_Ss2amScanPointRevalidationsSec_Type = Gauge32
_Ss2amScanPointRevalidationsSec_Object = MibTableColumn
ss2amScanPointRevalidationsSec = _Ss2amScanPointRevalidationsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 35),
    _Ss2amScanPointRevalidationsSec_Type()
)
ss2amScanPointRevalidationsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amScanPointRevalidationsSec.setStatus("current")
_Ss2amSkippedGhostedRecordsPerSec_Type = Gauge32
_Ss2amSkippedGhostedRecordsPerSec_Object = MibTableColumn
ss2amSkippedGhostedRecordsPerSec = _Ss2amSkippedGhostedRecordsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 36),
    _Ss2amSkippedGhostedRecordsPerSec_Type()
)
ss2amSkippedGhostedRecordsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amSkippedGhostedRecordsPerSec.setStatus("current")
_Ss2amTableLockEscalationsPerSec_Type = Gauge32
_Ss2amTableLockEscalationsPerSec_Object = MibTableColumn
ss2amTableLockEscalationsPerSec = _Ss2amTableLockEscalationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 37),
    _Ss2amTableLockEscalationsPerSec_Type()
)
ss2amTableLockEscalationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amTableLockEscalationsPerSec.setStatus("current")
_Ss2amUsedLeafPageCookie_Type = Gauge32
_Ss2amUsedLeafPageCookie_Object = MibTableColumn
ss2amUsedLeafPageCookie = _Ss2amUsedLeafPageCookie_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 38),
    _Ss2amUsedLeafPageCookie_Type()
)
ss2amUsedLeafPageCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amUsedLeafPageCookie.setStatus("current")
_Ss2amUsedTreePageCookie_Type = Gauge32
_Ss2amUsedTreePageCookie_Object = MibTableColumn
ss2amUsedTreePageCookie = _Ss2amUsedTreePageCookie_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 39),
    _Ss2amUsedTreePageCookie_Type()
)
ss2amUsedTreePageCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amUsedTreePageCookie.setStatus("current")
_Ss2amWorkfilesCreatedPerSec_Type = Gauge32
_Ss2amWorkfilesCreatedPerSec_Object = MibTableColumn
ss2amWorkfilesCreatedPerSec = _Ss2amWorkfilesCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 40),
    _Ss2amWorkfilesCreatedPerSec_Type()
)
ss2amWorkfilesCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amWorkfilesCreatedPerSec.setStatus("current")
_Ss2amWorktablesCreatedPerSec_Type = Gauge32
_Ss2amWorktablesCreatedPerSec_Object = MibTableColumn
ss2amWorktablesCreatedPerSec = _Ss2amWorktablesCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 41),
    _Ss2amWorktablesCreatedPerSec_Type()
)
ss2amWorktablesCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amWorktablesCreatedPerSec.setStatus("current")
_Ss2amWorktablesFromCacheRatio_Type = Gauge32
_Ss2amWorktablesFromCacheRatio_Object = MibTableColumn
ss2amWorktablesFromCacheRatio = _Ss2amWorktablesFromCacheRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 2, 1, 42),
    _Ss2amWorktablesFromCacheRatio_Type()
)
ss2amWorktablesFromCacheRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2amWorktablesFromCacheRatio.setStatus("current")
_Ss2BackupDeviceTable_Object = MibTable
ss2BackupDeviceTable = _Ss2BackupDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 3)
)
if mibBuilder.loadTexts:
    ss2BackupDeviceTable.setStatus("current")
_Ss2BackupDeviceEntry_Object = MibTableRow
ss2BackupDeviceEntry = _Ss2BackupDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 3, 1)
)
ss2BackupDeviceEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2BackupDeviceInstance"),
)
if mibBuilder.loadTexts:
    ss2BackupDeviceEntry.setStatus("current")
_Ss2BackupDeviceInstance_Type = InstanceName
_Ss2BackupDeviceInstance_Object = MibTableColumn
ss2BackupDeviceInstance = _Ss2BackupDeviceInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 3, 1, 1),
    _Ss2BackupDeviceInstance_Type()
)
ss2BackupDeviceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2BackupDeviceInstance.setStatus("current")
_Ss2BackupDeviceDeviceputBytesSec_Type = Gauge32
_Ss2BackupDeviceDeviceputBytesSec_Object = MibTableColumn
ss2BackupDeviceDeviceputBytesSec = _Ss2BackupDeviceDeviceputBytesSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 3, 1, 2),
    _Ss2BackupDeviceDeviceputBytesSec_Type()
)
ss2BackupDeviceDeviceputBytesSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2BackupDeviceDeviceputBytesSec.setStatus("current")
_Ss2BrokerActivationTable_Object = MibTable
ss2BrokerActivationTable = _Ss2BrokerActivationTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 4)
)
if mibBuilder.loadTexts:
    ss2BrokerActivationTable.setStatus("current")
_Ss2BrokerActivationEntry_Object = MibTableRow
ss2BrokerActivationEntry = _Ss2BrokerActivationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 4, 1)
)
ss2BrokerActivationEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2baInstance"),
)
if mibBuilder.loadTexts:
    ss2BrokerActivationEntry.setStatus("current")
_Ss2baInstance_Type = InstanceName
_Ss2baInstance_Object = MibTableColumn
ss2baInstance = _Ss2baInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 4, 1, 1),
    _Ss2baInstance_Type()
)
ss2baInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2baInstance.setStatus("current")
_Ss2baStoredProceduresInvokedSec_Type = Gauge32
_Ss2baStoredProceduresInvokedSec_Object = MibTableColumn
ss2baStoredProceduresInvokedSec = _Ss2baStoredProceduresInvokedSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 4, 1, 2),
    _Ss2baStoredProceduresInvokedSec_Type()
)
ss2baStoredProceduresInvokedSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2baStoredProceduresInvokedSec.setStatus("current")
_Ss2baTaskLimitReached_Type = Gauge32
_Ss2baTaskLimitReached_Object = MibTableColumn
ss2baTaskLimitReached = _Ss2baTaskLimitReached_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 4, 1, 3),
    _Ss2baTaskLimitReached_Type()
)
ss2baTaskLimitReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2baTaskLimitReached.setStatus("current")
_Ss2baTaskLimitReachedPerSec_Type = Gauge32
_Ss2baTaskLimitReachedPerSec_Object = MibTableColumn
ss2baTaskLimitReachedPerSec = _Ss2baTaskLimitReachedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 4, 1, 4),
    _Ss2baTaskLimitReachedPerSec_Type()
)
ss2baTaskLimitReachedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2baTaskLimitReachedPerSec.setStatus("current")
_Ss2baTasksAbortedPerSec_Type = Gauge32
_Ss2baTasksAbortedPerSec_Object = MibTableColumn
ss2baTasksAbortedPerSec = _Ss2baTasksAbortedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 4, 1, 5),
    _Ss2baTasksAbortedPerSec_Type()
)
ss2baTasksAbortedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2baTasksAbortedPerSec.setStatus("current")
_Ss2baTasksRunning_Type = Gauge32
_Ss2baTasksRunning_Object = MibTableColumn
ss2baTasksRunning = _Ss2baTasksRunning_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 4, 1, 6),
    _Ss2baTasksRunning_Type()
)
ss2baTasksRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2baTasksRunning.setStatus("current")
_Ss2baTasksStartedPerSec_Type = Gauge32
_Ss2baTasksStartedPerSec_Object = MibTableColumn
ss2baTasksStartedPerSec = _Ss2baTasksStartedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 4, 1, 7),
    _Ss2baTasksStartedPerSec_Type()
)
ss2baTasksStartedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2baTasksStartedPerSec.setStatus("current")
_Ss2BrokerStatisticsTable_Object = MibTable
ss2BrokerStatisticsTable = _Ss2BrokerStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5)
)
if mibBuilder.loadTexts:
    ss2BrokerStatisticsTable.setStatus("current")
_Ss2BrokerStatisticsEntry_Object = MibTableRow
ss2BrokerStatisticsEntry = _Ss2BrokerStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1)
)
ss2BrokerStatisticsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2BrokerStatisticsEntry.setStatus("current")
_Ss2bsActivationErrorsTotal_Type = Gauge32
_Ss2bsActivationErrorsTotal_Object = MibTableColumn
ss2bsActivationErrorsTotal = _Ss2bsActivationErrorsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 1),
    _Ss2bsActivationErrorsTotal_Type()
)
ss2bsActivationErrorsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsActivationErrorsTotal.setStatus("current")
_Ss2bsBrokerTransactionRollbacks_Type = Gauge32
_Ss2bsBrokerTransactionRollbacks_Object = MibTableColumn
ss2bsBrokerTransactionRollbacks = _Ss2bsBrokerTransactionRollbacks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 2),
    _Ss2bsBrokerTransactionRollbacks_Type()
)
ss2bsBrokerTransactionRollbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsBrokerTransactionRollbacks.setStatus("current")
_Ss2bsCorruptedMessagesTotal_Type = Gauge32
_Ss2bsCorruptedMessagesTotal_Object = MibTableColumn
ss2bsCorruptedMessagesTotal = _Ss2bsCorruptedMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 3),
    _Ss2bsCorruptedMessagesTotal_Type()
)
ss2bsCorruptedMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsCorruptedMessagesTotal.setStatus("current")
_Ss2bsDequeuedTransmissionQMsgSec_Type = Gauge32
_Ss2bsDequeuedTransmissionQMsgSec_Object = MibTableColumn
ss2bsDequeuedTransmissionQMsgSec = _Ss2bsDequeuedTransmissionQMsgSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 4),
    _Ss2bsDequeuedTransmissionQMsgSec_Type()
)
ss2bsDequeuedTransmissionQMsgSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsDequeuedTransmissionQMsgSec.setStatus("current")
_Ss2bsDialogTimerEventCount_Type = Gauge32
_Ss2bsDialogTimerEventCount_Object = MibTableColumn
ss2bsDialogTimerEventCount = _Ss2bsDialogTimerEventCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 5),
    _Ss2bsDialogTimerEventCount_Type()
)
ss2bsDialogTimerEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsDialogTimerEventCount.setStatus("current")
_Ss2bsDroppedMessagesTotal_Type = Gauge32
_Ss2bsDroppedMessagesTotal_Object = MibTableColumn
ss2bsDroppedMessagesTotal = _Ss2bsDroppedMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 6),
    _Ss2bsDroppedMessagesTotal_Type()
)
ss2bsDroppedMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsDroppedMessagesTotal.setStatus("current")
_Ss2bsEnqueuedLocalMessagesTotal_Type = Gauge32
_Ss2bsEnqueuedLocalMessagesTotal_Object = MibTableColumn
ss2bsEnqueuedLocalMessagesTotal = _Ss2bsEnqueuedLocalMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 7),
    _Ss2bsEnqueuedLocalMessagesTotal_Type()
)
ss2bsEnqueuedLocalMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedLocalMessagesTotal.setStatus("current")
_Ss2bsEnqueuedLocalMessagesPerSec_Type = Gauge32
_Ss2bsEnqueuedLocalMessagesPerSec_Object = MibTableColumn
ss2bsEnqueuedLocalMessagesPerSec = _Ss2bsEnqueuedLocalMessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 8),
    _Ss2bsEnqueuedLocalMessagesPerSec_Type()
)
ss2bsEnqueuedLocalMessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedLocalMessagesPerSec.setStatus("current")
_Ss2bsEnqueuedMessagesTotal_Type = Gauge32
_Ss2bsEnqueuedMessagesTotal_Object = MibTableColumn
ss2bsEnqueuedMessagesTotal = _Ss2bsEnqueuedMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 9),
    _Ss2bsEnqueuedMessagesTotal_Type()
)
ss2bsEnqueuedMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedMessagesTotal.setStatus("current")
_Ss2bsEnqueuedMessagesPerSec_Type = Gauge32
_Ss2bsEnqueuedMessagesPerSec_Object = MibTableColumn
ss2bsEnqueuedMessagesPerSec = _Ss2bsEnqueuedMessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 10),
    _Ss2bsEnqueuedMessagesPerSec_Type()
)
ss2bsEnqueuedMessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedMessagesPerSec.setStatus("current")
_Ss2bsEnqueuedP1MessagesPerSec_Type = Gauge32
_Ss2bsEnqueuedP1MessagesPerSec_Object = MibTableColumn
ss2bsEnqueuedP1MessagesPerSec = _Ss2bsEnqueuedP1MessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 11),
    _Ss2bsEnqueuedP1MessagesPerSec_Type()
)
ss2bsEnqueuedP1MessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedP1MessagesPerSec.setStatus("current")
_Ss2bsEnqueuedP10MessagesPerSec_Type = Gauge32
_Ss2bsEnqueuedP10MessagesPerSec_Object = MibTableColumn
ss2bsEnqueuedP10MessagesPerSec = _Ss2bsEnqueuedP10MessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 12),
    _Ss2bsEnqueuedP10MessagesPerSec_Type()
)
ss2bsEnqueuedP10MessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedP10MessagesPerSec.setStatus("current")
_Ss2bsEnqueuedP2MessagesPerSec_Type = Gauge32
_Ss2bsEnqueuedP2MessagesPerSec_Object = MibTableColumn
ss2bsEnqueuedP2MessagesPerSec = _Ss2bsEnqueuedP2MessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 13),
    _Ss2bsEnqueuedP2MessagesPerSec_Type()
)
ss2bsEnqueuedP2MessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedP2MessagesPerSec.setStatus("current")
_Ss2bsEnqueuedP3MessagesPerSec_Type = Gauge32
_Ss2bsEnqueuedP3MessagesPerSec_Object = MibTableColumn
ss2bsEnqueuedP3MessagesPerSec = _Ss2bsEnqueuedP3MessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 14),
    _Ss2bsEnqueuedP3MessagesPerSec_Type()
)
ss2bsEnqueuedP3MessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedP3MessagesPerSec.setStatus("current")
_Ss2bsEnqueuedP4MessagesPerSec_Type = Gauge32
_Ss2bsEnqueuedP4MessagesPerSec_Object = MibTableColumn
ss2bsEnqueuedP4MessagesPerSec = _Ss2bsEnqueuedP4MessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 15),
    _Ss2bsEnqueuedP4MessagesPerSec_Type()
)
ss2bsEnqueuedP4MessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedP4MessagesPerSec.setStatus("current")
_Ss2bsEnqueuedP5MessagesPerSec_Type = Gauge32
_Ss2bsEnqueuedP5MessagesPerSec_Object = MibTableColumn
ss2bsEnqueuedP5MessagesPerSec = _Ss2bsEnqueuedP5MessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 16),
    _Ss2bsEnqueuedP5MessagesPerSec_Type()
)
ss2bsEnqueuedP5MessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedP5MessagesPerSec.setStatus("current")
_Ss2bsEnqueuedP6MessagesPerSec_Type = Gauge32
_Ss2bsEnqueuedP6MessagesPerSec_Object = MibTableColumn
ss2bsEnqueuedP6MessagesPerSec = _Ss2bsEnqueuedP6MessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 17),
    _Ss2bsEnqueuedP6MessagesPerSec_Type()
)
ss2bsEnqueuedP6MessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedP6MessagesPerSec.setStatus("current")
_Ss2bsEnqueuedP7MessagesPerSec_Type = Gauge32
_Ss2bsEnqueuedP7MessagesPerSec_Object = MibTableColumn
ss2bsEnqueuedP7MessagesPerSec = _Ss2bsEnqueuedP7MessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 18),
    _Ss2bsEnqueuedP7MessagesPerSec_Type()
)
ss2bsEnqueuedP7MessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedP7MessagesPerSec.setStatus("current")
_Ss2bsEnqueuedP8MessagesPerSec_Type = Gauge32
_Ss2bsEnqueuedP8MessagesPerSec_Object = MibTableColumn
ss2bsEnqueuedP8MessagesPerSec = _Ss2bsEnqueuedP8MessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 19),
    _Ss2bsEnqueuedP8MessagesPerSec_Type()
)
ss2bsEnqueuedP8MessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedP8MessagesPerSec.setStatus("current")
_Ss2bsEnqueuedP9MessagesPerSec_Type = Gauge32
_Ss2bsEnqueuedP9MessagesPerSec_Object = MibTableColumn
ss2bsEnqueuedP9MessagesPerSec = _Ss2bsEnqueuedP9MessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 20),
    _Ss2bsEnqueuedP9MessagesPerSec_Type()
)
ss2bsEnqueuedP9MessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedP9MessagesPerSec.setStatus("current")
_Ss2bsEnqueuedTransmissionQMsgSec_Type = Gauge32
_Ss2bsEnqueuedTransmissionQMsgSec_Object = MibTableColumn
ss2bsEnqueuedTransmissionQMsgSec = _Ss2bsEnqueuedTransmissionQMsgSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 21),
    _Ss2bsEnqueuedTransmissionQMsgSec_Type()
)
ss2bsEnqueuedTransmissionQMsgSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedTransmissionQMsgSec.setStatus("current")
_Ss2bsEnqueuedTransportMsgFragTot_Type = Gauge32
_Ss2bsEnqueuedTransportMsgFragTot_Object = MibTableColumn
ss2bsEnqueuedTransportMsgFragTot = _Ss2bsEnqueuedTransportMsgFragTot_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 22),
    _Ss2bsEnqueuedTransportMsgFragTot_Type()
)
ss2bsEnqueuedTransportMsgFragTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedTransportMsgFragTot.setStatus("current")
_Ss2bsEnqueuedTransportMsgFragSec_Type = Gauge32
_Ss2bsEnqueuedTransportMsgFragSec_Object = MibTableColumn
ss2bsEnqueuedTransportMsgFragSec = _Ss2bsEnqueuedTransportMsgFragSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 23),
    _Ss2bsEnqueuedTransportMsgFragSec_Type()
)
ss2bsEnqueuedTransportMsgFragSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedTransportMsgFragSec.setStatus("current")
_Ss2bsEnqueuedTransportMsgsTotal_Type = Gauge32
_Ss2bsEnqueuedTransportMsgsTotal_Object = MibTableColumn
ss2bsEnqueuedTransportMsgsTotal = _Ss2bsEnqueuedTransportMsgsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 24),
    _Ss2bsEnqueuedTransportMsgsTotal_Type()
)
ss2bsEnqueuedTransportMsgsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedTransportMsgsTotal.setStatus("current")
_Ss2bsEnqueuedTransportMsgsPerSec_Type = Gauge32
_Ss2bsEnqueuedTransportMsgsPerSec_Object = MibTableColumn
ss2bsEnqueuedTransportMsgsPerSec = _Ss2bsEnqueuedTransportMsgsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 25),
    _Ss2bsEnqueuedTransportMsgsPerSec_Type()
)
ss2bsEnqueuedTransportMsgsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsEnqueuedTransportMsgsPerSec.setStatus("current")
_Ss2bsForwardedMessagesTotal_Type = Gauge32
_Ss2bsForwardedMessagesTotal_Object = MibTableColumn
ss2bsForwardedMessagesTotal = _Ss2bsForwardedMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 26),
    _Ss2bsForwardedMessagesTotal_Type()
)
ss2bsForwardedMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsForwardedMessagesTotal.setStatus("current")
_Ss2bsForwardedMessagesPerSec_Type = Gauge32
_Ss2bsForwardedMessagesPerSec_Object = MibTableColumn
ss2bsForwardedMessagesPerSec = _Ss2bsForwardedMessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 27),
    _Ss2bsForwardedMessagesPerSec_Type()
)
ss2bsForwardedMessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsForwardedMessagesPerSec.setStatus("current")
_Ss2bsForwardedMsgByteTotal_Type = Gauge32
_Ss2bsForwardedMsgByteTotal_Object = MibTableColumn
ss2bsForwardedMsgByteTotal = _Ss2bsForwardedMsgByteTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 28),
    _Ss2bsForwardedMsgByteTotal_Type()
)
ss2bsForwardedMsgByteTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsForwardedMsgByteTotal.setStatus("current")
_Ss2bsForwardedMsgBytesPerSec_Type = Gauge32
_Ss2bsForwardedMsgBytesPerSec_Object = MibTableColumn
ss2bsForwardedMsgBytesPerSec = _Ss2bsForwardedMsgBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 29),
    _Ss2bsForwardedMsgBytesPerSec_Type()
)
ss2bsForwardedMsgBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsForwardedMsgBytesPerSec.setStatus("current")
_Ss2bsForwardedMsgDiscardedTotal_Type = Gauge32
_Ss2bsForwardedMsgDiscardedTotal_Object = MibTableColumn
ss2bsForwardedMsgDiscardedTotal = _Ss2bsForwardedMsgDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 30),
    _Ss2bsForwardedMsgDiscardedTotal_Type()
)
ss2bsForwardedMsgDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsForwardedMsgDiscardedTotal.setStatus("current")
_Ss2bsForwardedMsgsDiscardedSec_Type = Gauge32
_Ss2bsForwardedMsgsDiscardedSec_Object = MibTableColumn
ss2bsForwardedMsgsDiscardedSec = _Ss2bsForwardedMsgsDiscardedSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 31),
    _Ss2bsForwardedMsgsDiscardedSec_Type()
)
ss2bsForwardedMsgsDiscardedSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsForwardedMsgsDiscardedSec.setStatus("current")
_Ss2bsForwardedPendingMsgBytes_Type = Gauge32
_Ss2bsForwardedPendingMsgBytes_Object = MibTableColumn
ss2bsForwardedPendingMsgBytes = _Ss2bsForwardedPendingMsgBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 32),
    _Ss2bsForwardedPendingMsgBytes_Type()
)
ss2bsForwardedPendingMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsForwardedPendingMsgBytes.setStatus("current")
_Ss2bsForwardedPendingMsgCount_Type = Gauge32
_Ss2bsForwardedPendingMsgCount_Object = MibTableColumn
ss2bsForwardedPendingMsgCount = _Ss2bsForwardedPendingMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 33),
    _Ss2bsForwardedPendingMsgCount_Type()
)
ss2bsForwardedPendingMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsForwardedPendingMsgCount.setStatus("current")
_Ss2bsSQLReceiveTotal_Type = Gauge32
_Ss2bsSQLReceiveTotal_Object = MibTableColumn
ss2bsSQLReceiveTotal = _Ss2bsSQLReceiveTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 34),
    _Ss2bsSQLReceiveTotal_Type()
)
ss2bsSQLReceiveTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsSQLReceiveTotal.setStatus("current")
_Ss2bsSQLReceivesPerSec_Type = Gauge32
_Ss2bsSQLReceivesPerSec_Object = MibTableColumn
ss2bsSQLReceivesPerSec = _Ss2bsSQLReceivesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 35),
    _Ss2bsSQLReceivesPerSec_Type()
)
ss2bsSQLReceivesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsSQLReceivesPerSec.setStatus("current")
_Ss2bsSQLSendTotal_Type = Gauge32
_Ss2bsSQLSendTotal_Object = MibTableColumn
ss2bsSQLSendTotal = _Ss2bsSQLSendTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 36),
    _Ss2bsSQLSendTotal_Type()
)
ss2bsSQLSendTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsSQLSendTotal.setStatus("current")
_Ss2bsSQLSendsPerSec_Type = Gauge32
_Ss2bsSQLSendsPerSec_Object = MibTableColumn
ss2bsSQLSendsPerSec = _Ss2bsSQLSendsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 5, 1, 37),
    _Ss2bsSQLSendsPerSec_Type()
)
ss2bsSQLSendsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bsSQLSendsPerSec.setStatus("current")
_Ss2BrokerTOStatisticsTable_Object = MibTable
ss2BrokerTOStatisticsTable = _Ss2BrokerTOStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 6)
)
if mibBuilder.loadTexts:
    ss2BrokerTOStatisticsTable.setStatus("current")
_Ss2BrokerTOStatisticsEntry_Object = MibTableRow
ss2BrokerTOStatisticsEntry = _Ss2BrokerTOStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 6, 1)
)
ss2BrokerTOStatisticsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2BrokerTOStatisticsEntry.setStatus("current")
_Ss2btosAvgLengthOfBatchedWrites_Type = Gauge32
_Ss2btosAvgLengthOfBatchedWrites_Object = MibTableColumn
ss2btosAvgLengthOfBatchedWrites = _Ss2btosAvgLengthOfBatchedWrites_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 6, 1, 1),
    _Ss2btosAvgLengthOfBatchedWrites_Type()
)
ss2btosAvgLengthOfBatchedWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2btosAvgLengthOfBatchedWrites.setStatus("current")
_Ss2btosAvgTimeBetweenBatchesMs_Type = Gauge32
_Ss2btosAvgTimeBetweenBatchesMs_Object = MibTableColumn
ss2btosAvgTimeBetweenBatchesMs = _Ss2btosAvgTimeBetweenBatchesMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 6, 1, 2),
    _Ss2btosAvgTimeBetweenBatchesMs_Type()
)
ss2btosAvgTimeBetweenBatchesMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2btosAvgTimeBetweenBatchesMs.setStatus("current")
_Ss2btosAvgTimeToWriteBatchMs_Type = Gauge32
_Ss2btosAvgTimeToWriteBatchMs_Object = MibTableColumn
ss2btosAvgTimeToWriteBatchMs = _Ss2btosAvgTimeToWriteBatchMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 6, 1, 3),
    _Ss2btosAvgTimeToWriteBatchMs_Type()
)
ss2btosAvgTimeToWriteBatchMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2btosAvgTimeToWriteBatchMs.setStatus("current")
_Ss2btosTransmissionObjGetsPerSec_Type = Gauge32
_Ss2btosTransmissionObjGetsPerSec_Object = MibTableColumn
ss2btosTransmissionObjGetsPerSec = _Ss2btosTransmissionObjGetsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 6, 1, 4),
    _Ss2btosTransmissionObjGetsPerSec_Type()
)
ss2btosTransmissionObjGetsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2btosTransmissionObjGetsPerSec.setStatus("current")
_Ss2btosTransmissionObjSetDirtSec_Type = Gauge32
_Ss2btosTransmissionObjSetDirtSec_Object = MibTableColumn
ss2btosTransmissionObjSetDirtSec = _Ss2btosTransmissionObjSetDirtSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 6, 1, 5),
    _Ss2btosTransmissionObjSetDirtSec_Type()
)
ss2btosTransmissionObjSetDirtSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2btosTransmissionObjSetDirtSec.setStatus("current")
_Ss2btosTransmissionObjWritesSec_Type = Gauge32
_Ss2btosTransmissionObjWritesSec_Object = MibTableColumn
ss2btosTransmissionObjWritesSec = _Ss2btosTransmissionObjWritesSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 6, 1, 6),
    _Ss2btosTransmissionObjWritesSec_Type()
)
ss2btosTransmissionObjWritesSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2btosTransmissionObjWritesSec.setStatus("current")
_Ss2BrokerPerDBMTransportTable_Object = MibTable
ss2BrokerPerDBMTransportTable = _Ss2BrokerPerDBMTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7)
)
if mibBuilder.loadTexts:
    ss2BrokerPerDBMTransportTable.setStatus("current")
_Ss2BrokerPerDBMTransportEntry_Object = MibTableRow
ss2BrokerPerDBMTransportEntry = _Ss2BrokerPerDBMTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1)
)
ss2BrokerPerDBMTransportEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2BrokerPerDBMTransportEntry.setStatus("current")
_Ss2bdtCurrentBytesForRecvIPerO_Type = Gauge32
_Ss2bdtCurrentBytesForRecvIPerO_Object = MibTableColumn
ss2bdtCurrentBytesForRecvIPerO = _Ss2bdtCurrentBytesForRecvIPerO_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 1),
    _Ss2bdtCurrentBytesForRecvIPerO_Type()
)
ss2bdtCurrentBytesForRecvIPerO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtCurrentBytesForRecvIPerO.setStatus("current")
_Ss2bdtCurrentBytesForSendIPerO_Type = Gauge32
_Ss2bdtCurrentBytesForSendIPerO_Object = MibTableColumn
ss2bdtCurrentBytesForSendIPerO = _Ss2bdtCurrentBytesForSendIPerO_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 2),
    _Ss2bdtCurrentBytesForSendIPerO_Type()
)
ss2bdtCurrentBytesForSendIPerO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtCurrentBytesForSendIPerO.setStatus("current")
_Ss2bdtCurrentMsgFragForSendIO_Type = Gauge32
_Ss2bdtCurrentMsgFragForSendIO_Object = MibTableColumn
ss2bdtCurrentMsgFragForSendIO = _Ss2bdtCurrentMsgFragForSendIO_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 3),
    _Ss2bdtCurrentMsgFragForSendIO_Type()
)
ss2bdtCurrentMsgFragForSendIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtCurrentMsgFragForSendIO.setStatus("current")
_Ss2bdtMessageFragmentP1SenSec_Type = Gauge32
_Ss2bdtMessageFragmentP1SenSec_Object = MibTableColumn
ss2bdtMessageFragmentP1SenSec = _Ss2bdtMessageFragmentP1SenSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 4),
    _Ss2bdtMessageFragmentP1SenSec_Type()
)
ss2bdtMessageFragmentP1SenSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtMessageFragmentP1SenSec.setStatus("current")
_Ss2bdtMsgFragmentP10SendsSec_Type = Gauge32
_Ss2bdtMsgFragmentP10SendsSec_Object = MibTableColumn
ss2bdtMsgFragmentP10SendsSec = _Ss2bdtMsgFragmentP10SendsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 5),
    _Ss2bdtMsgFragmentP10SendsSec_Type()
)
ss2bdtMsgFragmentP10SendsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtMsgFragmentP10SendsSec.setStatus("current")
_Ss2bdtMsgFragmentP2SendsSec_Type = Gauge32
_Ss2bdtMsgFragmentP2SendsSec_Object = MibTableColumn
ss2bdtMsgFragmentP2SendsSec = _Ss2bdtMsgFragmentP2SendsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 6),
    _Ss2bdtMsgFragmentP2SendsSec_Type()
)
ss2bdtMsgFragmentP2SendsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtMsgFragmentP2SendsSec.setStatus("current")
_Ss2bdtMsgFragmentP3SendsSec_Type = Gauge32
_Ss2bdtMsgFragmentP3SendsSec_Object = MibTableColumn
ss2bdtMsgFragmentP3SendsSec = _Ss2bdtMsgFragmentP3SendsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 7),
    _Ss2bdtMsgFragmentP3SendsSec_Type()
)
ss2bdtMsgFragmentP3SendsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtMsgFragmentP3SendsSec.setStatus("current")
_Ss2bdtMsgFragmentP4SendsSec_Type = Gauge32
_Ss2bdtMsgFragmentP4SendsSec_Object = MibTableColumn
ss2bdtMsgFragmentP4SendsSec = _Ss2bdtMsgFragmentP4SendsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 8),
    _Ss2bdtMsgFragmentP4SendsSec_Type()
)
ss2bdtMsgFragmentP4SendsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtMsgFragmentP4SendsSec.setStatus("current")
_Ss2bdtMsgFragmentP5SendsSec_Type = Gauge32
_Ss2bdtMsgFragmentP5SendsSec_Object = MibTableColumn
ss2bdtMsgFragmentP5SendsSec = _Ss2bdtMsgFragmentP5SendsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 9),
    _Ss2bdtMsgFragmentP5SendsSec_Type()
)
ss2bdtMsgFragmentP5SendsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtMsgFragmentP5SendsSec.setStatus("current")
_Ss2bdtMsgFragmentP6SendsSec_Type = Gauge32
_Ss2bdtMsgFragmentP6SendsSec_Object = MibTableColumn
ss2bdtMsgFragmentP6SendsSec = _Ss2bdtMsgFragmentP6SendsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 10),
    _Ss2bdtMsgFragmentP6SendsSec_Type()
)
ss2bdtMsgFragmentP6SendsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtMsgFragmentP6SendsSec.setStatus("current")
_Ss2bdtMsgFragmentP7SendsSec_Type = Gauge32
_Ss2bdtMsgFragmentP7SendsSec_Object = MibTableColumn
ss2bdtMsgFragmentP7SendsSec = _Ss2bdtMsgFragmentP7SendsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 11),
    _Ss2bdtMsgFragmentP7SendsSec_Type()
)
ss2bdtMsgFragmentP7SendsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtMsgFragmentP7SendsSec.setStatus("current")
_Ss2bdtMsgFragmentP8SendsSec_Type = Gauge32
_Ss2bdtMsgFragmentP8SendsSec_Object = MibTableColumn
ss2bdtMsgFragmentP8SendsSec = _Ss2bdtMsgFragmentP8SendsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 12),
    _Ss2bdtMsgFragmentP8SendsSec_Type()
)
ss2bdtMsgFragmentP8SendsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtMsgFragmentP8SendsSec.setStatus("current")
_Ss2bdtMsgFragmentP9SendsSec_Type = Gauge32
_Ss2bdtMsgFragmentP9SendsSec_Object = MibTableColumn
ss2bdtMsgFragmentP9SendsSec = _Ss2bdtMsgFragmentP9SendsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 13),
    _Ss2bdtMsgFragmentP9SendsSec_Type()
)
ss2bdtMsgFragmentP9SendsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtMsgFragmentP9SendsSec.setStatus("current")
_Ss2bdtMsgFragmentReceivesSec_Type = Gauge32
_Ss2bdtMsgFragmentReceivesSec_Object = MibTableColumn
ss2bdtMsgFragmentReceivesSec = _Ss2bdtMsgFragmentReceivesSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 14),
    _Ss2bdtMsgFragmentReceivesSec_Type()
)
ss2bdtMsgFragmentReceivesSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtMsgFragmentReceivesSec.setStatus("current")
_Ss2bdtMessageFragmentSendsPerSec_Type = Gauge32
_Ss2bdtMessageFragmentSendsPerSec_Object = MibTableColumn
ss2bdtMessageFragmentSendsPerSec = _Ss2bdtMessageFragmentSendsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 15),
    _Ss2bdtMessageFragmentSendsPerSec_Type()
)
ss2bdtMessageFragmentSendsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtMessageFragmentSendsPerSec.setStatus("current")
_Ss2bdtMsgFragmentRecvSizeAvg_Type = Gauge32
_Ss2bdtMsgFragmentRecvSizeAvg_Object = MibTableColumn
ss2bdtMsgFragmentRecvSizeAvg = _Ss2bdtMsgFragmentRecvSizeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 16),
    _Ss2bdtMsgFragmentRecvSizeAvg_Type()
)
ss2bdtMsgFragmentRecvSizeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtMsgFragmentRecvSizeAvg.setStatus("current")
_Ss2bdtMsgFragmentSendSizeAvg_Type = Gauge32
_Ss2bdtMsgFragmentSendSizeAvg_Object = MibTableColumn
ss2bdtMsgFragmentSendSizeAvg = _Ss2bdtMsgFragmentSendSizeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 17),
    _Ss2bdtMsgFragmentSendSizeAvg_Type()
)
ss2bdtMsgFragmentSendSizeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtMsgFragmentSendSizeAvg.setStatus("current")
_Ss2bdtOpenConnectionCount_Type = Gauge32
_Ss2bdtOpenConnectionCount_Object = MibTableColumn
ss2bdtOpenConnectionCount = _Ss2bdtOpenConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 18),
    _Ss2bdtOpenConnectionCount_Type()
)
ss2bdtOpenConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtOpenConnectionCount.setStatus("current")
_Ss2bdtPendingBytesForRecvIPerO_Type = Gauge32
_Ss2bdtPendingBytesForRecvIPerO_Object = MibTableColumn
ss2bdtPendingBytesForRecvIPerO = _Ss2bdtPendingBytesForRecvIPerO_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 19),
    _Ss2bdtPendingBytesForRecvIPerO_Type()
)
ss2bdtPendingBytesForRecvIPerO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtPendingBytesForRecvIPerO.setStatus("current")
_Ss2bdtPendingBytesForSendIPerO_Type = Gauge32
_Ss2bdtPendingBytesForSendIPerO_Object = MibTableColumn
ss2bdtPendingBytesForSendIPerO = _Ss2bdtPendingBytesForSendIPerO_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 20),
    _Ss2bdtPendingBytesForSendIPerO_Type()
)
ss2bdtPendingBytesForSendIPerO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtPendingBytesForSendIPerO.setStatus("current")
_Ss2bdtPendingMsgFragForRecvIO_Type = Gauge32
_Ss2bdtPendingMsgFragForRecvIO_Object = MibTableColumn
ss2bdtPendingMsgFragForRecvIO = _Ss2bdtPendingMsgFragForRecvIO_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 21),
    _Ss2bdtPendingMsgFragForRecvIO_Type()
)
ss2bdtPendingMsgFragForRecvIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtPendingMsgFragForRecvIO.setStatus("current")
_Ss2bdtPendingMsgFragForSendIO_Type = Gauge32
_Ss2bdtPendingMsgFragForSendIO_Object = MibTableColumn
ss2bdtPendingMsgFragForSendIO = _Ss2bdtPendingMsgFragForSendIO_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 22),
    _Ss2bdtPendingMsgFragForSendIO_Type()
)
ss2bdtPendingMsgFragForSendIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtPendingMsgFragForSendIO.setStatus("current")
_Ss2bdtReceiveIPerOLenAvg_Type = Gauge32
_Ss2bdtReceiveIPerOLenAvg_Object = MibTableColumn
ss2bdtReceiveIPerOLenAvg = _Ss2bdtReceiveIPerOLenAvg_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 23),
    _Ss2bdtReceiveIPerOLenAvg_Type()
)
ss2bdtReceiveIPerOLenAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtReceiveIPerOLenAvg.setStatus("current")
_Ss2bdtReceiveIPerOBytesPerSec_Type = Gauge32
_Ss2bdtReceiveIPerOBytesPerSec_Object = MibTableColumn
ss2bdtReceiveIPerOBytesPerSec = _Ss2bdtReceiveIPerOBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 24),
    _Ss2bdtReceiveIPerOBytesPerSec_Type()
)
ss2bdtReceiveIPerOBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtReceiveIPerOBytesPerSec.setStatus("current")
_Ss2bdtReceiveIPerOsPerSec_Type = Gauge32
_Ss2bdtReceiveIPerOsPerSec_Object = MibTableColumn
ss2bdtReceiveIPerOsPerSec = _Ss2bdtReceiveIPerOsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 25),
    _Ss2bdtReceiveIPerOsPerSec_Type()
)
ss2bdtReceiveIPerOsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtReceiveIPerOsPerSec.setStatus("current")
_Ss2bdtRecvIPerOBufferCopiesCount_Type = Gauge32
_Ss2bdtRecvIPerOBufferCopiesCount_Object = MibTableColumn
ss2bdtRecvIPerOBufferCopiesCount = _Ss2bdtRecvIPerOBufferCopiesCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 26),
    _Ss2bdtRecvIPerOBufferCopiesCount_Type()
)
ss2bdtRecvIPerOBufferCopiesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtRecvIPerOBufferCopiesCount.setStatus("current")
_Ss2bdtRecvIOBufferCopiesBytesSec_Type = Gauge32
_Ss2bdtRecvIOBufferCopiesBytesSec_Object = MibTableColumn
ss2bdtRecvIOBufferCopiesBytesSec = _Ss2bdtRecvIOBufferCopiesBytesSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 27),
    _Ss2bdtRecvIOBufferCopiesBytesSec_Type()
)
ss2bdtRecvIOBufferCopiesBytesSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtRecvIOBufferCopiesBytesSec.setStatus("current")
_Ss2bdtSendIPerOLenAvg_Type = Gauge32
_Ss2bdtSendIPerOLenAvg_Object = MibTableColumn
ss2bdtSendIPerOLenAvg = _Ss2bdtSendIPerOLenAvg_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 28),
    _Ss2bdtSendIPerOLenAvg_Type()
)
ss2bdtSendIPerOLenAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtSendIPerOLenAvg.setStatus("current")
_Ss2bdtSendIPerOBytesPerSec_Type = Gauge32
_Ss2bdtSendIPerOBytesPerSec_Object = MibTableColumn
ss2bdtSendIPerOBytesPerSec = _Ss2bdtSendIPerOBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 29),
    _Ss2bdtSendIPerOBytesPerSec_Type()
)
ss2bdtSendIPerOBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtSendIPerOBytesPerSec.setStatus("current")
_Ss2bdtSendIPerOsPerSec_Type = Gauge32
_Ss2bdtSendIPerOsPerSec_Object = MibTableColumn
ss2bdtSendIPerOsPerSec = _Ss2bdtSendIPerOsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 7, 1, 30),
    _Ss2bdtSendIPerOsPerSec_Type()
)
ss2bdtSendIPerOsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bdtSendIPerOsPerSec.setStatus("current")
_Ss2BufferManagerTable_Object = MibTable
ss2BufferManagerTable = _Ss2BufferManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8)
)
if mibBuilder.loadTexts:
    ss2BufferManagerTable.setStatus("current")
_Ss2BufferManagerEntry_Object = MibTableRow
ss2BufferManagerEntry = _Ss2BufferManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1)
)
ss2BufferManagerEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2BufferManagerEntry.setStatus("current")
_Ss2bmAWELookupMapsPerSec_Type = Gauge32
_Ss2bmAWELookupMapsPerSec_Object = MibTableColumn
ss2bmAWELookupMapsPerSec = _Ss2bmAWELookupMapsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 1),
    _Ss2bmAWELookupMapsPerSec_Type()
)
ss2bmAWELookupMapsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmAWELookupMapsPerSec.setStatus("current")
_Ss2bmAWEStolenMapsPerSec_Type = Gauge32
_Ss2bmAWEStolenMapsPerSec_Object = MibTableColumn
ss2bmAWEStolenMapsPerSec = _Ss2bmAWEStolenMapsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 2),
    _Ss2bmAWEStolenMapsPerSec_Type()
)
ss2bmAWEStolenMapsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmAWEStolenMapsPerSec.setStatus("current")
_Ss2bmAWEUnmapCallsPerSec_Type = Gauge32
_Ss2bmAWEUnmapCallsPerSec_Object = MibTableColumn
ss2bmAWEUnmapCallsPerSec = _Ss2bmAWEUnmapCallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 3),
    _Ss2bmAWEUnmapCallsPerSec_Type()
)
ss2bmAWEUnmapCallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmAWEUnmapCallsPerSec.setStatus("current")
_Ss2bmAWEUnmapPagesPerSec_Type = Gauge32
_Ss2bmAWEUnmapPagesPerSec_Object = MibTableColumn
ss2bmAWEUnmapPagesPerSec = _Ss2bmAWEUnmapPagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 4),
    _Ss2bmAWEUnmapPagesPerSec_Type()
)
ss2bmAWEUnmapPagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmAWEUnmapPagesPerSec.setStatus("current")
_Ss2bmAWEWriteMapsPerSec_Type = Gauge32
_Ss2bmAWEWriteMapsPerSec_Object = MibTableColumn
ss2bmAWEWriteMapsPerSec = _Ss2bmAWEWriteMapsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 5),
    _Ss2bmAWEWriteMapsPerSec_Type()
)
ss2bmAWEWriteMapsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmAWEWriteMapsPerSec.setStatus("current")
_Ss2bmBufferCacheHitRatio_Type = Gauge32
_Ss2bmBufferCacheHitRatio_Object = MibTableColumn
ss2bmBufferCacheHitRatio = _Ss2bmBufferCacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 6),
    _Ss2bmBufferCacheHitRatio_Type()
)
ss2bmBufferCacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmBufferCacheHitRatio.setStatus("current")
_Ss2bmCheckpointPagesPerSec_Type = Gauge32
_Ss2bmCheckpointPagesPerSec_Object = MibTableColumn
ss2bmCheckpointPagesPerSec = _Ss2bmCheckpointPagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 7),
    _Ss2bmCheckpointPagesPerSec_Type()
)
ss2bmCheckpointPagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmCheckpointPagesPerSec.setStatus("current")
_Ss2bmDatabasePages_Type = Gauge32
_Ss2bmDatabasePages_Object = MibTableColumn
ss2bmDatabasePages = _Ss2bmDatabasePages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 8),
    _Ss2bmDatabasePages_Type()
)
ss2bmDatabasePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmDatabasePages.setStatus("current")
_Ss2bmFreeListStallsPerSec_Type = Gauge32
_Ss2bmFreeListStallsPerSec_Object = MibTableColumn
ss2bmFreeListStallsPerSec = _Ss2bmFreeListStallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 9),
    _Ss2bmFreeListStallsPerSec_Type()
)
ss2bmFreeListStallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmFreeListStallsPerSec.setStatus("current")
_Ss2bmFreePages_Type = Gauge32
_Ss2bmFreePages_Object = MibTableColumn
ss2bmFreePages = _Ss2bmFreePages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 10),
    _Ss2bmFreePages_Type()
)
ss2bmFreePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmFreePages.setStatus("current")
_Ss2bmLazyWritesPerSec_Type = Gauge32
_Ss2bmLazyWritesPerSec_Object = MibTableColumn
ss2bmLazyWritesPerSec = _Ss2bmLazyWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 11),
    _Ss2bmLazyWritesPerSec_Type()
)
ss2bmLazyWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmLazyWritesPerSec.setStatus("current")
_Ss2bmPageLifeExpectancy_Type = Gauge32
_Ss2bmPageLifeExpectancy_Object = MibTableColumn
ss2bmPageLifeExpectancy = _Ss2bmPageLifeExpectancy_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 12),
    _Ss2bmPageLifeExpectancy_Type()
)
ss2bmPageLifeExpectancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmPageLifeExpectancy.setStatus("current")
_Ss2bmPageLookupsPerSec_Type = Gauge32
_Ss2bmPageLookupsPerSec_Object = MibTableColumn
ss2bmPageLookupsPerSec = _Ss2bmPageLookupsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 13),
    _Ss2bmPageLookupsPerSec_Type()
)
ss2bmPageLookupsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmPageLookupsPerSec.setStatus("current")
_Ss2bmPageReadsPerSec_Type = Gauge32
_Ss2bmPageReadsPerSec_Object = MibTableColumn
ss2bmPageReadsPerSec = _Ss2bmPageReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 14),
    _Ss2bmPageReadsPerSec_Type()
)
ss2bmPageReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmPageReadsPerSec.setStatus("current")
_Ss2bmPageWritesPerSec_Type = Gauge32
_Ss2bmPageWritesPerSec_Object = MibTableColumn
ss2bmPageWritesPerSec = _Ss2bmPageWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 15),
    _Ss2bmPageWritesPerSec_Type()
)
ss2bmPageWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmPageWritesPerSec.setStatus("current")
_Ss2bmReadaheadPagesPerSec_Type = Gauge32
_Ss2bmReadaheadPagesPerSec_Object = MibTableColumn
ss2bmReadaheadPagesPerSec = _Ss2bmReadaheadPagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 16),
    _Ss2bmReadaheadPagesPerSec_Type()
)
ss2bmReadaheadPagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmReadaheadPagesPerSec.setStatus("current")
_Ss2bmReservedPages_Type = Gauge32
_Ss2bmReservedPages_Object = MibTableColumn
ss2bmReservedPages = _Ss2bmReservedPages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 17),
    _Ss2bmReservedPages_Type()
)
ss2bmReservedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmReservedPages.setStatus("current")
_Ss2bmStolenPages_Type = Gauge32
_Ss2bmStolenPages_Object = MibTableColumn
ss2bmStolenPages = _Ss2bmStolenPages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 18),
    _Ss2bmStolenPages_Type()
)
ss2bmStolenPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmStolenPages.setStatus("current")
_Ss2bmTargetPages_Type = Gauge32
_Ss2bmTargetPages_Object = MibTableColumn
ss2bmTargetPages = _Ss2bmTargetPages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 19),
    _Ss2bmTargetPages_Type()
)
ss2bmTargetPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmTargetPages.setStatus("current")
_Ss2bmTotalPages_Type = Gauge32
_Ss2bmTotalPages_Object = MibTableColumn
ss2bmTotalPages = _Ss2bmTotalPages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 8, 1, 20),
    _Ss2bmTotalPages_Type()
)
ss2bmTotalPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bmTotalPages.setStatus("current")
_Ss2BufferNodeTable_Object = MibTable
ss2BufferNodeTable = _Ss2BufferNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 9)
)
if mibBuilder.loadTexts:
    ss2BufferNodeTable.setStatus("current")
_Ss2BufferNodeEntry_Object = MibTableRow
ss2BufferNodeEntry = _Ss2BufferNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 9, 1)
)
ss2BufferNodeEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2bnInstance"),
)
if mibBuilder.loadTexts:
    ss2BufferNodeEntry.setStatus("current")
_Ss2bnInstance_Type = InstanceName
_Ss2bnInstance_Object = MibTableColumn
ss2bnInstance = _Ss2bnInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 9, 1, 1),
    _Ss2bnInstance_Type()
)
ss2bnInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bnInstance.setStatus("current")
_Ss2bnDatabasePages_Type = Gauge32
_Ss2bnDatabasePages_Object = MibTableColumn
ss2bnDatabasePages = _Ss2bnDatabasePages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 9, 1, 2),
    _Ss2bnDatabasePages_Type()
)
ss2bnDatabasePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bnDatabasePages.setStatus("current")
_Ss2bnForeignPages_Type = Gauge32
_Ss2bnForeignPages_Object = MibTableColumn
ss2bnForeignPages = _Ss2bnForeignPages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 9, 1, 3),
    _Ss2bnForeignPages_Type()
)
ss2bnForeignPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bnForeignPages.setStatus("current")
_Ss2bnFreePages_Type = Gauge32
_Ss2bnFreePages_Object = MibTableColumn
ss2bnFreePages = _Ss2bnFreePages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 9, 1, 4),
    _Ss2bnFreePages_Type()
)
ss2bnFreePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bnFreePages.setStatus("current")
_Ss2bnLocalNodePageLookupsPerSec_Type = Gauge32
_Ss2bnLocalNodePageLookupsPerSec_Object = MibTableColumn
ss2bnLocalNodePageLookupsPerSec = _Ss2bnLocalNodePageLookupsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 9, 1, 5),
    _Ss2bnLocalNodePageLookupsPerSec_Type()
)
ss2bnLocalNodePageLookupsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bnLocalNodePageLookupsPerSec.setStatus("current")
_Ss2bnPageLifeExpectancy_Type = Gauge32
_Ss2bnPageLifeExpectancy_Object = MibTableColumn
ss2bnPageLifeExpectancy = _Ss2bnPageLifeExpectancy_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 9, 1, 6),
    _Ss2bnPageLifeExpectancy_Type()
)
ss2bnPageLifeExpectancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bnPageLifeExpectancy.setStatus("current")
_Ss2bnRemoteNodePageLookupsPerSec_Type = Gauge32
_Ss2bnRemoteNodePageLookupsPerSec_Object = MibTableColumn
ss2bnRemoteNodePageLookupsPerSec = _Ss2bnRemoteNodePageLookupsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 9, 1, 7),
    _Ss2bnRemoteNodePageLookupsPerSec_Type()
)
ss2bnRemoteNodePageLookupsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bnRemoteNodePageLookupsPerSec.setStatus("current")
_Ss2bnStolenPages_Type = Gauge32
_Ss2bnStolenPages_Object = MibTableColumn
ss2bnStolenPages = _Ss2bnStolenPages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 9, 1, 8),
    _Ss2bnStolenPages_Type()
)
ss2bnStolenPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bnStolenPages.setStatus("current")
_Ss2bnTargetPages_Type = Gauge32
_Ss2bnTargetPages_Object = MibTableColumn
ss2bnTargetPages = _Ss2bnTargetPages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 9, 1, 9),
    _Ss2bnTargetPages_Type()
)
ss2bnTargetPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bnTargetPages.setStatus("current")
_Ss2bnTotalPages_Type = Gauge32
_Ss2bnTotalPages_Object = MibTableColumn
ss2bnTotalPages = _Ss2bnTotalPages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 9, 1, 10),
    _Ss2bnTotalPages_Type()
)
ss2bnTotalPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bnTotalPages.setStatus("current")
_Ss2BufferPartitionTable_Object = MibTable
ss2BufferPartitionTable = _Ss2BufferPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 10)
)
if mibBuilder.loadTexts:
    ss2BufferPartitionTable.setStatus("current")
_Ss2BufferPartitionEntry_Object = MibTableRow
ss2BufferPartitionEntry = _Ss2BufferPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 10, 1)
)
ss2BufferPartitionEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2bpInstance"),
)
if mibBuilder.loadTexts:
    ss2BufferPartitionEntry.setStatus("current")
_Ss2bpInstance_Type = InstanceName
_Ss2bpInstance_Object = MibTableColumn
ss2bpInstance = _Ss2bpInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 10, 1, 1),
    _Ss2bpInstance_Type()
)
ss2bpInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bpInstance.setStatus("current")
_Ss2bpFreeListEmptyPerSec_Type = Gauge32
_Ss2bpFreeListEmptyPerSec_Object = MibTableColumn
ss2bpFreeListEmptyPerSec = _Ss2bpFreeListEmptyPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 10, 1, 2),
    _Ss2bpFreeListEmptyPerSec_Type()
)
ss2bpFreeListEmptyPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bpFreeListEmptyPerSec.setStatus("current")
_Ss2bpFreeListRequestsPerSec_Type = Gauge32
_Ss2bpFreeListRequestsPerSec_Object = MibTableColumn
ss2bpFreeListRequestsPerSec = _Ss2bpFreeListRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 10, 1, 3),
    _Ss2bpFreeListRequestsPerSec_Type()
)
ss2bpFreeListRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bpFreeListRequestsPerSec.setStatus("current")
_Ss2bpFreePages_Type = Gauge32
_Ss2bpFreePages_Object = MibTableColumn
ss2bpFreePages = _Ss2bpFreePages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 10, 1, 4),
    _Ss2bpFreePages_Type()
)
ss2bpFreePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2bpFreePages.setStatus("current")
_Ss2CLRTable_Object = MibTable
ss2CLRTable = _Ss2CLRTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 11)
)
if mibBuilder.loadTexts:
    ss2CLRTable.setStatus("current")
_Ss2CLREntry_Object = MibTableRow
ss2CLREntry = _Ss2CLREntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 11, 1)
)
ss2CLREntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2CLREntry.setStatus("current")
_Ss2CLRCLRExecution_Type = Gauge32
_Ss2CLRCLRExecution_Object = MibTableColumn
ss2CLRCLRExecution = _Ss2CLRCLRExecution_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 11, 1, 1),
    _Ss2CLRCLRExecution_Type()
)
ss2CLRCLRExecution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2CLRCLRExecution.setStatus("current")
_Ss2CatalogMetadataTable_Object = MibTable
ss2CatalogMetadataTable = _Ss2CatalogMetadataTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 12)
)
if mibBuilder.loadTexts:
    ss2CatalogMetadataTable.setStatus("current")
_Ss2CatalogMetadataEntry_Object = MibTableRow
ss2CatalogMetadataEntry = _Ss2CatalogMetadataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 12, 1)
)
ss2CatalogMetadataEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2cmdInstance"),
)
if mibBuilder.loadTexts:
    ss2CatalogMetadataEntry.setStatus("current")
_Ss2cmdInstance_Type = InstanceName
_Ss2cmdInstance_Object = MibTableColumn
ss2cmdInstance = _Ss2cmdInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 12, 1, 1),
    _Ss2cmdInstance_Type()
)
ss2cmdInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmdInstance.setStatus("current")
_Ss2cmdCacheEntriesCount_Type = Gauge32
_Ss2cmdCacheEntriesCount_Object = MibTableColumn
ss2cmdCacheEntriesCount = _Ss2cmdCacheEntriesCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 12, 1, 2),
    _Ss2cmdCacheEntriesCount_Type()
)
ss2cmdCacheEntriesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmdCacheEntriesCount.setStatus("current")
_Ss2cmdCacheEntriesPinnedCount_Type = Gauge32
_Ss2cmdCacheEntriesPinnedCount_Object = MibTableColumn
ss2cmdCacheEntriesPinnedCount = _Ss2cmdCacheEntriesPinnedCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 12, 1, 3),
    _Ss2cmdCacheEntriesPinnedCount_Type()
)
ss2cmdCacheEntriesPinnedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmdCacheEntriesPinnedCount.setStatus("current")
_Ss2cmdCacheHitRatio_Type = Gauge32
_Ss2cmdCacheHitRatio_Object = MibTableColumn
ss2cmdCacheHitRatio = _Ss2cmdCacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 12, 1, 4),
    _Ss2cmdCacheHitRatio_Type()
)
ss2cmdCacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmdCacheHitRatio.setStatus("current")
_Ss2CursorManagerTotalTable_Object = MibTable
ss2CursorManagerTotalTable = _Ss2CursorManagerTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 13)
)
if mibBuilder.loadTexts:
    ss2CursorManagerTotalTable.setStatus("current")
_Ss2CursorManagerTotalEntry_Object = MibTableRow
ss2CursorManagerTotalEntry = _Ss2CursorManagerTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 13, 1)
)
ss2CursorManagerTotalEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2CursorManagerTotalEntry.setStatus("current")
_Ss2cmtAsyncPopulationCount_Type = Gauge32
_Ss2cmtAsyncPopulationCount_Object = MibTableColumn
ss2cmtAsyncPopulationCount = _Ss2cmtAsyncPopulationCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 13, 1, 1),
    _Ss2cmtAsyncPopulationCount_Type()
)
ss2cmtAsyncPopulationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmtAsyncPopulationCount.setStatus("current")
_Ss2cmtCursorConversionRate_Type = Gauge32
_Ss2cmtCursorConversionRate_Object = MibTableColumn
ss2cmtCursorConversionRate = _Ss2cmtCursorConversionRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 13, 1, 2),
    _Ss2cmtCursorConversionRate_Type()
)
ss2cmtCursorConversionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmtCursorConversionRate.setStatus("current")
_Ss2cmtCursorFlushes_Type = Gauge32
_Ss2cmtCursorFlushes_Object = MibTableColumn
ss2cmtCursorFlushes = _Ss2cmtCursorFlushes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 13, 1, 3),
    _Ss2cmtCursorFlushes_Type()
)
ss2cmtCursorFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmtCursorFlushes.setStatus("current")
_Ss2CursorManagerByTypeTable_Object = MibTable
ss2CursorManagerByTypeTable = _Ss2CursorManagerByTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 14)
)
if mibBuilder.loadTexts:
    ss2CursorManagerByTypeTable.setStatus("current")
_Ss2CursorManagerByTypeEntry_Object = MibTableRow
ss2CursorManagerByTypeEntry = _Ss2CursorManagerByTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 14, 1)
)
ss2CursorManagerByTypeEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2cmbtInstance"),
)
if mibBuilder.loadTexts:
    ss2CursorManagerByTypeEntry.setStatus("current")
_Ss2cmbtInstance_Type = InstanceName
_Ss2cmbtInstance_Object = MibTableColumn
ss2cmbtInstance = _Ss2cmbtInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 14, 1, 1),
    _Ss2cmbtInstance_Type()
)
ss2cmbtInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmbtInstance.setStatus("current")
_Ss2cmbtActiveCursors_Type = Gauge32
_Ss2cmbtActiveCursors_Object = MibTableColumn
ss2cmbtActiveCursors = _Ss2cmbtActiveCursors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 14, 1, 2),
    _Ss2cmbtActiveCursors_Type()
)
ss2cmbtActiveCursors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmbtActiveCursors.setStatus("current")
_Ss2cmbtCacheHitRatio_Type = Gauge32
_Ss2cmbtCacheHitRatio_Object = MibTableColumn
ss2cmbtCacheHitRatio = _Ss2cmbtCacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 14, 1, 3),
    _Ss2cmbtCacheHitRatio_Type()
)
ss2cmbtCacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmbtCacheHitRatio.setStatus("current")
_Ss2cmbtCachedCursorCounts_Type = Gauge32
_Ss2cmbtCachedCursorCounts_Object = MibTableColumn
ss2cmbtCachedCursorCounts = _Ss2cmbtCachedCursorCounts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 14, 1, 4),
    _Ss2cmbtCachedCursorCounts_Type()
)
ss2cmbtCachedCursorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmbtCachedCursorCounts.setStatus("current")
_Ss2cmbtCursorCacheUseCountsSec_Type = Gauge32
_Ss2cmbtCursorCacheUseCountsSec_Object = MibTableColumn
ss2cmbtCursorCacheUseCountsSec = _Ss2cmbtCursorCacheUseCountsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 14, 1, 5),
    _Ss2cmbtCursorCacheUseCountsSec_Type()
)
ss2cmbtCursorCacheUseCountsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmbtCursorCacheUseCountsSec.setStatus("current")
_Ss2cmbtCursorRequestsPerSec_Type = Gauge32
_Ss2cmbtCursorRequestsPerSec_Object = MibTableColumn
ss2cmbtCursorRequestsPerSec = _Ss2cmbtCursorRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 14, 1, 6),
    _Ss2cmbtCursorRequestsPerSec_Type()
)
ss2cmbtCursorRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmbtCursorRequestsPerSec.setStatus("current")
_Ss2cmbtCursorMemoryUsage_Type = Gauge32
_Ss2cmbtCursorMemoryUsage_Object = MibTableColumn
ss2cmbtCursorMemoryUsage = _Ss2cmbtCursorMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 14, 1, 7),
    _Ss2cmbtCursorMemoryUsage_Type()
)
ss2cmbtCursorMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmbtCursorMemoryUsage.setStatus("current")
_Ss2cmbtCursorWorktableUsage_Type = Gauge32
_Ss2cmbtCursorWorktableUsage_Object = MibTableColumn
ss2cmbtCursorWorktableUsage = _Ss2cmbtCursorWorktableUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 14, 1, 8),
    _Ss2cmbtCursorWorktableUsage_Type()
)
ss2cmbtCursorWorktableUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmbtCursorWorktableUsage.setStatus("current")
_Ss2cmbtNumberOfActiveCursorPlans_Type = Gauge32
_Ss2cmbtNumberOfActiveCursorPlans_Object = MibTableColumn
ss2cmbtNumberOfActiveCursorPlans = _Ss2cmbtNumberOfActiveCursorPlans_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 14, 1, 9),
    _Ss2cmbtNumberOfActiveCursorPlans_Type()
)
ss2cmbtNumberOfActiveCursorPlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2cmbtNumberOfActiveCursorPlans.setStatus("current")
_Ss2DatabaseMirroringTable_Object = MibTable
ss2DatabaseMirroringTable = _Ss2DatabaseMirroringTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15)
)
if mibBuilder.loadTexts:
    ss2DatabaseMirroringTable.setStatus("current")
_Ss2DatabaseMirroringEntry_Object = MibTableRow
ss2DatabaseMirroringEntry = _Ss2DatabaseMirroringEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1)
)
ss2DatabaseMirroringEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2dmInstance"),
)
if mibBuilder.loadTexts:
    ss2DatabaseMirroringEntry.setStatus("current")
_Ss2dmInstance_Type = InstanceName
_Ss2dmInstance_Object = MibTableColumn
ss2dmInstance = _Ss2dmInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 1),
    _Ss2dmInstance_Type()
)
ss2dmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmInstance.setStatus("current")
_Ss2dmBytesReceivedPerSec_Type = Gauge32
_Ss2dmBytesReceivedPerSec_Object = MibTableColumn
ss2dmBytesReceivedPerSec = _Ss2dmBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 2),
    _Ss2dmBytesReceivedPerSec_Type()
)
ss2dmBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmBytesReceivedPerSec.setStatus("current")
_Ss2dmBytesSentPerSec_Type = Gauge32
_Ss2dmBytesSentPerSec_Object = MibTableColumn
ss2dmBytesSentPerSec = _Ss2dmBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 3),
    _Ss2dmBytesSentPerSec_Type()
)
ss2dmBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmBytesSentPerSec.setStatus("current")
_Ss2dmLogBytesReceivedPerSec_Type = Gauge32
_Ss2dmLogBytesReceivedPerSec_Object = MibTableColumn
ss2dmLogBytesReceivedPerSec = _Ss2dmLogBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 4),
    _Ss2dmLogBytesReceivedPerSec_Type()
)
ss2dmLogBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmLogBytesReceivedPerSec.setStatus("current")
_Ss2dmLogBytesRedoneFromCacheSec_Type = Gauge32
_Ss2dmLogBytesRedoneFromCacheSec_Object = MibTableColumn
ss2dmLogBytesRedoneFromCacheSec = _Ss2dmLogBytesRedoneFromCacheSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 5),
    _Ss2dmLogBytesRedoneFromCacheSec_Type()
)
ss2dmLogBytesRedoneFromCacheSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmLogBytesRedoneFromCacheSec.setStatus("current")
_Ss2dmLogBytesSentFromCachePerSec_Type = Gauge32
_Ss2dmLogBytesSentFromCachePerSec_Object = MibTableColumn
ss2dmLogBytesSentFromCachePerSec = _Ss2dmLogBytesSentFromCachePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 6),
    _Ss2dmLogBytesSentFromCachePerSec_Type()
)
ss2dmLogBytesSentFromCachePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmLogBytesSentFromCachePerSec.setStatus("current")
_Ss2dmLogBytesSentPerSec_Type = Gauge32
_Ss2dmLogBytesSentPerSec_Object = MibTableColumn
ss2dmLogBytesSentPerSec = _Ss2dmLogBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 7),
    _Ss2dmLogBytesSentPerSec_Type()
)
ss2dmLogBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmLogBytesSentPerSec.setStatus("current")
_Ss2dmLogCompressedBytesRcvdSec_Type = Gauge32
_Ss2dmLogCompressedBytesRcvdSec_Object = MibTableColumn
ss2dmLogCompressedBytesRcvdSec = _Ss2dmLogCompressedBytesRcvdSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 8),
    _Ss2dmLogCompressedBytesRcvdSec_Type()
)
ss2dmLogCompressedBytesRcvdSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmLogCompressedBytesRcvdSec.setStatus("current")
_Ss2dmLogCompressedBytesSentSec_Type = Gauge32
_Ss2dmLogCompressedBytesSentSec_Object = MibTableColumn
ss2dmLogCompressedBytesSentSec = _Ss2dmLogCompressedBytesSentSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 9),
    _Ss2dmLogCompressedBytesSentSec_Type()
)
ss2dmLogCompressedBytesSentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmLogCompressedBytesSentSec.setStatus("current")
_Ss2dmLogHardenTimeMs_Type = Gauge32
_Ss2dmLogHardenTimeMs_Object = MibTableColumn
ss2dmLogHardenTimeMs = _Ss2dmLogHardenTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 10),
    _Ss2dmLogHardenTimeMs_Type()
)
ss2dmLogHardenTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmLogHardenTimeMs.setStatus("current")
_Ss2dmLogRemainingForUndoKB_Type = Gauge32
_Ss2dmLogRemainingForUndoKB_Object = MibTableColumn
ss2dmLogRemainingForUndoKB = _Ss2dmLogRemainingForUndoKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 11),
    _Ss2dmLogRemainingForUndoKB_Type()
)
ss2dmLogRemainingForUndoKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmLogRemainingForUndoKB.setStatus("current")
_Ss2dmLogScannedForUndoKB_Type = Gauge32
_Ss2dmLogScannedForUndoKB_Object = MibTableColumn
ss2dmLogScannedForUndoKB = _Ss2dmLogScannedForUndoKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 12),
    _Ss2dmLogScannedForUndoKB_Type()
)
ss2dmLogScannedForUndoKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmLogScannedForUndoKB.setStatus("current")
_Ss2dmLogSendFlowControlTimeMs_Type = Gauge32
_Ss2dmLogSendFlowControlTimeMs_Object = MibTableColumn
ss2dmLogSendFlowControlTimeMs = _Ss2dmLogSendFlowControlTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 13),
    _Ss2dmLogSendFlowControlTimeMs_Type()
)
ss2dmLogSendFlowControlTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmLogSendFlowControlTimeMs.setStatus("current")
_Ss2dmLogSendQueueKB_Type = Gauge32
_Ss2dmLogSendQueueKB_Object = MibTableColumn
ss2dmLogSendQueueKB = _Ss2dmLogSendQueueKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 14),
    _Ss2dmLogSendQueueKB_Type()
)
ss2dmLogSendQueueKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmLogSendQueueKB.setStatus("current")
_Ss2dmMirroredWritTransactionsSec_Type = Gauge32
_Ss2dmMirroredWritTransactionsSec_Object = MibTableColumn
ss2dmMirroredWritTransactionsSec = _Ss2dmMirroredWritTransactionsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 15),
    _Ss2dmMirroredWritTransactionsSec_Type()
)
ss2dmMirroredWritTransactionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmMirroredWritTransactionsSec.setStatus("current")
_Ss2dmPagesSentPerSec_Type = Gauge32
_Ss2dmPagesSentPerSec_Object = MibTableColumn
ss2dmPagesSentPerSec = _Ss2dmPagesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 16),
    _Ss2dmPagesSentPerSec_Type()
)
ss2dmPagesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmPagesSentPerSec.setStatus("current")
_Ss2dmReceivesPerSec_Type = Gauge32
_Ss2dmReceivesPerSec_Object = MibTableColumn
ss2dmReceivesPerSec = _Ss2dmReceivesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 17),
    _Ss2dmReceivesPerSec_Type()
)
ss2dmReceivesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmReceivesPerSec.setStatus("current")
_Ss2dmRedoBytesPerSec_Type = Gauge32
_Ss2dmRedoBytesPerSec_Object = MibTableColumn
ss2dmRedoBytesPerSec = _Ss2dmRedoBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 18),
    _Ss2dmRedoBytesPerSec_Type()
)
ss2dmRedoBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmRedoBytesPerSec.setStatus("current")
_Ss2dmRedoQueueKB_Type = Gauge32
_Ss2dmRedoQueueKB_Object = MibTableColumn
ss2dmRedoQueueKB = _Ss2dmRedoQueueKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 19),
    _Ss2dmRedoQueueKB_Type()
)
ss2dmRedoQueueKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmRedoQueueKB.setStatus("current")
_Ss2dmSendPerReceiveAckTime_Type = Gauge32
_Ss2dmSendPerReceiveAckTime_Object = MibTableColumn
ss2dmSendPerReceiveAckTime = _Ss2dmSendPerReceiveAckTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 20),
    _Ss2dmSendPerReceiveAckTime_Type()
)
ss2dmSendPerReceiveAckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmSendPerReceiveAckTime.setStatus("current")
_Ss2dmSendsPerSec_Type = Gauge32
_Ss2dmSendsPerSec_Object = MibTableColumn
ss2dmSendsPerSec = _Ss2dmSendsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 21),
    _Ss2dmSendsPerSec_Type()
)
ss2dmSendsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmSendsPerSec.setStatus("current")
_Ss2dmTransactionDelay_Type = Gauge32
_Ss2dmTransactionDelay_Object = MibTableColumn
ss2dmTransactionDelay = _Ss2dmTransactionDelay_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 15, 1, 22),
    _Ss2dmTransactionDelay_Type()
)
ss2dmTransactionDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dmTransactionDelay.setStatus("current")
_Ss2DatabasesTable_Object = MibTable
ss2DatabasesTable = _Ss2DatabasesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16)
)
if mibBuilder.loadTexts:
    ss2DatabasesTable.setStatus("current")
_Ss2DatabasesEntry_Object = MibTableRow
ss2DatabasesEntry = _Ss2DatabasesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1)
)
ss2DatabasesEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2dbInstance"),
)
if mibBuilder.loadTexts:
    ss2DatabasesEntry.setStatus("current")
_Ss2dbInstance_Type = InstanceName
_Ss2dbInstance_Object = MibTableColumn
ss2dbInstance = _Ss2dbInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 1),
    _Ss2dbInstance_Type()
)
ss2dbInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbInstance.setStatus("current")
_Ss2dbActiveTransactions_Type = Gauge32
_Ss2dbActiveTransactions_Object = MibTableColumn
ss2dbActiveTransactions = _Ss2dbActiveTransactions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 2),
    _Ss2dbActiveTransactions_Type()
)
ss2dbActiveTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbActiveTransactions.setStatus("current")
_Ss2dbBackupRestoreThroughputSec_Type = Gauge32
_Ss2dbBackupRestoreThroughputSec_Object = MibTableColumn
ss2dbBackupRestoreThroughputSec = _Ss2dbBackupRestoreThroughputSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 3),
    _Ss2dbBackupRestoreThroughputSec_Type()
)
ss2dbBackupRestoreThroughputSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbBackupRestoreThroughputSec.setStatus("current")
_Ss2dbBulkCopyRowsPerSec_Type = Gauge32
_Ss2dbBulkCopyRowsPerSec_Object = MibTableColumn
ss2dbBulkCopyRowsPerSec = _Ss2dbBulkCopyRowsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 4),
    _Ss2dbBulkCopyRowsPerSec_Type()
)
ss2dbBulkCopyRowsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbBulkCopyRowsPerSec.setStatus("current")
_Ss2dbBulkCopyThroughputPerSec_Type = Gauge32
_Ss2dbBulkCopyThroughputPerSec_Object = MibTableColumn
ss2dbBulkCopyThroughputPerSec = _Ss2dbBulkCopyThroughputPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 5),
    _Ss2dbBulkCopyThroughputPerSec_Type()
)
ss2dbBulkCopyThroughputPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbBulkCopyThroughputPerSec.setStatus("current")
_Ss2dbCommitTableEntries_Type = Gauge32
_Ss2dbCommitTableEntries_Object = MibTableColumn
ss2dbCommitTableEntries = _Ss2dbCommitTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 6),
    _Ss2dbCommitTableEntries_Type()
)
ss2dbCommitTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbCommitTableEntries.setStatus("current")
_Ss2dbDBCCLogicalScanBytesPerSec_Type = Gauge32
_Ss2dbDBCCLogicalScanBytesPerSec_Object = MibTableColumn
ss2dbDBCCLogicalScanBytesPerSec = _Ss2dbDBCCLogicalScanBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 7),
    _Ss2dbDBCCLogicalScanBytesPerSec_Type()
)
ss2dbDBCCLogicalScanBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbDBCCLogicalScanBytesPerSec.setStatus("current")
_Ss2dbDataFileSSizeKB_Type = Gauge32
_Ss2dbDataFileSSizeKB_Object = MibTableColumn
ss2dbDataFileSSizeKB = _Ss2dbDataFileSSizeKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 8),
    _Ss2dbDataFileSSizeKB_Type()
)
ss2dbDataFileSSizeKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbDataFileSSizeKB.setStatus("current")
_Ss2dbLogBytesFlushedPerSec_Type = Gauge32
_Ss2dbLogBytesFlushedPerSec_Object = MibTableColumn
ss2dbLogBytesFlushedPerSec = _Ss2dbLogBytesFlushedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 9),
    _Ss2dbLogBytesFlushedPerSec_Type()
)
ss2dbLogBytesFlushedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbLogBytesFlushedPerSec.setStatus("current")
_Ss2dbLogCacheHitRatio_Type = Gauge32
_Ss2dbLogCacheHitRatio_Object = MibTableColumn
ss2dbLogCacheHitRatio = _Ss2dbLogCacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 10),
    _Ss2dbLogCacheHitRatio_Type()
)
ss2dbLogCacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbLogCacheHitRatio.setStatus("current")
_Ss2dbLogCacheReadsPerSec_Type = Gauge32
_Ss2dbLogCacheReadsPerSec_Object = MibTableColumn
ss2dbLogCacheReadsPerSec = _Ss2dbLogCacheReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 11),
    _Ss2dbLogCacheReadsPerSec_Type()
)
ss2dbLogCacheReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbLogCacheReadsPerSec.setStatus("current")
_Ss2dbLogFileSSizeKB_Type = Gauge32
_Ss2dbLogFileSSizeKB_Object = MibTableColumn
ss2dbLogFileSSizeKB = _Ss2dbLogFileSSizeKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 12),
    _Ss2dbLogFileSSizeKB_Type()
)
ss2dbLogFileSSizeKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbLogFileSSizeKB.setStatus("current")
_Ss2dbLogFileSUsedSizeKB_Type = Gauge32
_Ss2dbLogFileSUsedSizeKB_Object = MibTableColumn
ss2dbLogFileSUsedSizeKB = _Ss2dbLogFileSUsedSizeKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 13),
    _Ss2dbLogFileSUsedSizeKB_Type()
)
ss2dbLogFileSUsedSizeKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbLogFileSUsedSizeKB.setStatus("current")
_Ss2dbLogFlushWaitTime_Type = Gauge32
_Ss2dbLogFlushWaitTime_Object = MibTableColumn
ss2dbLogFlushWaitTime = _Ss2dbLogFlushWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 14),
    _Ss2dbLogFlushWaitTime_Type()
)
ss2dbLogFlushWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbLogFlushWaitTime.setStatus("current")
_Ss2dbLogFlushWaitsPerSec_Type = Gauge32
_Ss2dbLogFlushWaitsPerSec_Object = MibTableColumn
ss2dbLogFlushWaitsPerSec = _Ss2dbLogFlushWaitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 15),
    _Ss2dbLogFlushWaitsPerSec_Type()
)
ss2dbLogFlushWaitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbLogFlushWaitsPerSec.setStatus("current")
_Ss2dbLogFlushesPerSec_Type = Gauge32
_Ss2dbLogFlushesPerSec_Object = MibTableColumn
ss2dbLogFlushesPerSec = _Ss2dbLogFlushesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 16),
    _Ss2dbLogFlushesPerSec_Type()
)
ss2dbLogFlushesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbLogFlushesPerSec.setStatus("current")
_Ss2dbLogGrowths_Type = Gauge32
_Ss2dbLogGrowths_Object = MibTableColumn
ss2dbLogGrowths = _Ss2dbLogGrowths_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 17),
    _Ss2dbLogGrowths_Type()
)
ss2dbLogGrowths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbLogGrowths.setStatus("current")
_Ss2dbLogShrinks_Type = Gauge32
_Ss2dbLogShrinks_Object = MibTableColumn
ss2dbLogShrinks = _Ss2dbLogShrinks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 18),
    _Ss2dbLogShrinks_Type()
)
ss2dbLogShrinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbLogShrinks.setStatus("current")
_Ss2dbLogTruncations_Type = Gauge32
_Ss2dbLogTruncations_Object = MibTableColumn
ss2dbLogTruncations = _Ss2dbLogTruncations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 19),
    _Ss2dbLogTruncations_Type()
)
ss2dbLogTruncations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbLogTruncations.setStatus("current")
_Ss2dbPercentLogUsed_Type = Gauge32
_Ss2dbPercentLogUsed_Object = MibTableColumn
ss2dbPercentLogUsed = _Ss2dbPercentLogUsed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 20),
    _Ss2dbPercentLogUsed_Type()
)
ss2dbPercentLogUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbPercentLogUsed.setStatus("current")
_Ss2dbReplPendingXacts_Type = Gauge32
_Ss2dbReplPendingXacts_Object = MibTableColumn
ss2dbReplPendingXacts = _Ss2dbReplPendingXacts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 21),
    _Ss2dbReplPendingXacts_Type()
)
ss2dbReplPendingXacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbReplPendingXacts.setStatus("current")
_Ss2dbReplTransRate_Type = Gauge32
_Ss2dbReplTransRate_Object = MibTableColumn
ss2dbReplTransRate = _Ss2dbReplTransRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 22),
    _Ss2dbReplTransRate_Type()
)
ss2dbReplTransRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbReplTransRate.setStatus("current")
_Ss2dbShrinkDataMovementBytesSec_Type = Gauge32
_Ss2dbShrinkDataMovementBytesSec_Object = MibTableColumn
ss2dbShrinkDataMovementBytesSec = _Ss2dbShrinkDataMovementBytesSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 23),
    _Ss2dbShrinkDataMovementBytesSec_Type()
)
ss2dbShrinkDataMovementBytesSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbShrinkDataMovementBytesSec.setStatus("current")
_Ss2dbTrackedTransactionsPerSec_Type = Gauge32
_Ss2dbTrackedTransactionsPerSec_Object = MibTableColumn
ss2dbTrackedTransactionsPerSec = _Ss2dbTrackedTransactionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 24),
    _Ss2dbTrackedTransactionsPerSec_Type()
)
ss2dbTrackedTransactionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbTrackedTransactionsPerSec.setStatus("current")
_Ss2dbTransactionsPerSec_Type = Gauge32
_Ss2dbTransactionsPerSec_Object = MibTableColumn
ss2dbTransactionsPerSec = _Ss2dbTransactionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 25),
    _Ss2dbTransactionsPerSec_Type()
)
ss2dbTransactionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbTransactionsPerSec.setStatus("current")
_Ss2dbWriteTransactionsPerSec_Type = Gauge32
_Ss2dbWriteTransactionsPerSec_Object = MibTableColumn
ss2dbWriteTransactionsPerSec = _Ss2dbWriteTransactionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 16, 1, 26),
    _Ss2dbWriteTransactionsPerSec_Type()
)
ss2dbWriteTransactionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2dbWriteTransactionsPerSec.setStatus("current")
_Ss2DeprecatedFeaturesTable_Object = MibTable
ss2DeprecatedFeaturesTable = _Ss2DeprecatedFeaturesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 17)
)
if mibBuilder.loadTexts:
    ss2DeprecatedFeaturesTable.setStatus("current")
_Ss2DeprecatedFeaturesEntry_Object = MibTableRow
ss2DeprecatedFeaturesEntry = _Ss2DeprecatedFeaturesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 17, 1)
)
ss2DeprecatedFeaturesEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2DeprecatedFeaturesInstance"),
)
if mibBuilder.loadTexts:
    ss2DeprecatedFeaturesEntry.setStatus("current")
_Ss2DeprecatedFeaturesInstance_Type = InstanceName
_Ss2DeprecatedFeaturesInstance_Object = MibTableColumn
ss2DeprecatedFeaturesInstance = _Ss2DeprecatedFeaturesInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 17, 1, 1),
    _Ss2DeprecatedFeaturesInstance_Type()
)
ss2DeprecatedFeaturesInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2DeprecatedFeaturesInstance.setStatus("current")
_Ss2DeprecatedFeaturesUsage_Type = Gauge32
_Ss2DeprecatedFeaturesUsage_Object = MibTableColumn
ss2DeprecatedFeaturesUsage = _Ss2DeprecatedFeaturesUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 17, 1, 2),
    _Ss2DeprecatedFeaturesUsage_Type()
)
ss2DeprecatedFeaturesUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2DeprecatedFeaturesUsage.setStatus("current")
_Ss2ExecStatisticsTable_Object = MibTable
ss2ExecStatisticsTable = _Ss2ExecStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 18)
)
if mibBuilder.loadTexts:
    ss2ExecStatisticsTable.setStatus("current")
_Ss2ExecStatisticsEntry_Object = MibTableRow
ss2ExecStatisticsEntry = _Ss2ExecStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 18, 1)
)
ss2ExecStatisticsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2ExecStatisticsInstance"),
)
if mibBuilder.loadTexts:
    ss2ExecStatisticsEntry.setStatus("current")
_Ss2ExecStatisticsInstance_Type = InstanceName
_Ss2ExecStatisticsInstance_Object = MibTableColumn
ss2ExecStatisticsInstance = _Ss2ExecStatisticsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 18, 1, 1),
    _Ss2ExecStatisticsInstance_Type()
)
ss2ExecStatisticsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2ExecStatisticsInstance.setStatus("current")
_Ss2ExecStatisticsDTCCalls_Type = Gauge32
_Ss2ExecStatisticsDTCCalls_Object = MibTableColumn
ss2ExecStatisticsDTCCalls = _Ss2ExecStatisticsDTCCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 18, 1, 2),
    _Ss2ExecStatisticsDTCCalls_Type()
)
ss2ExecStatisticsDTCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2ExecStatisticsDTCCalls.setStatus("current")
_Ss2ExecStatisticDistributedQuery_Type = Gauge32
_Ss2ExecStatisticDistributedQuery_Object = MibTableColumn
ss2ExecStatisticDistributedQuery = _Ss2ExecStatisticDistributedQuery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 18, 1, 3),
    _Ss2ExecStatisticDistributedQuery_Type()
)
ss2ExecStatisticDistributedQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2ExecStatisticDistributedQuery.setStatus("current")
_Ss2ExecStatistExtendedProcedures_Type = Gauge32
_Ss2ExecStatistExtendedProcedures_Object = MibTableColumn
ss2ExecStatistExtendedProcedures = _Ss2ExecStatistExtendedProcedures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 18, 1, 4),
    _Ss2ExecStatistExtendedProcedures_Type()
)
ss2ExecStatistExtendedProcedures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2ExecStatistExtendedProcedures.setStatus("current")
_Ss2ExecStatisticsOLEDBCalls_Type = Gauge32
_Ss2ExecStatisticsOLEDBCalls_Object = MibTableColumn
ss2ExecStatisticsOLEDBCalls = _Ss2ExecStatisticsOLEDBCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 18, 1, 5),
    _Ss2ExecStatisticsOLEDBCalls_Type()
)
ss2ExecStatisticsOLEDBCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2ExecStatisticsOLEDBCalls.setStatus("current")
_Ss2GeneralStatisticsTable_Object = MibTable
ss2GeneralStatisticsTable = _Ss2GeneralStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19)
)
if mibBuilder.loadTexts:
    ss2GeneralStatisticsTable.setStatus("current")
_Ss2GeneralStatisticsEntry_Object = MibTableRow
ss2GeneralStatisticsEntry = _Ss2GeneralStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1)
)
ss2GeneralStatisticsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2GeneralStatisticsEntry.setStatus("current")
_Ss2gsActiveTempTables_Type = Gauge32
_Ss2gsActiveTempTables_Object = MibTableColumn
ss2gsActiveTempTables = _Ss2gsActiveTempTables_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 1),
    _Ss2gsActiveTempTables_Type()
)
ss2gsActiveTempTables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsActiveTempTables.setStatus("current")
_Ss2gsConnectionResetPerSec_Type = Gauge32
_Ss2gsConnectionResetPerSec_Object = MibTableColumn
ss2gsConnectionResetPerSec = _Ss2gsConnectionResetPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 2),
    _Ss2gsConnectionResetPerSec_Type()
)
ss2gsConnectionResetPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsConnectionResetPerSec.setStatus("current")
_Ss2gsEventNotificationsDelayDrop_Type = Gauge32
_Ss2gsEventNotificationsDelayDrop_Object = MibTableColumn
ss2gsEventNotificationsDelayDrop = _Ss2gsEventNotificationsDelayDrop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 3),
    _Ss2gsEventNotificationsDelayDrop_Type()
)
ss2gsEventNotificationsDelayDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsEventNotificationsDelayDrop.setStatus("current")
_Ss2gsHTTPAuthenticatedRequests_Type = Gauge32
_Ss2gsHTTPAuthenticatedRequests_Object = MibTableColumn
ss2gsHTTPAuthenticatedRequests = _Ss2gsHTTPAuthenticatedRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 4),
    _Ss2gsHTTPAuthenticatedRequests_Type()
)
ss2gsHTTPAuthenticatedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsHTTPAuthenticatedRequests.setStatus("current")
_Ss2gsLogicalConnections_Type = Gauge32
_Ss2gsLogicalConnections_Object = MibTableColumn
ss2gsLogicalConnections = _Ss2gsLogicalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 5),
    _Ss2gsLogicalConnections_Type()
)
ss2gsLogicalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsLogicalConnections.setStatus("current")
_Ss2gsLoginsPerSec_Type = Gauge32
_Ss2gsLoginsPerSec_Object = MibTableColumn
ss2gsLoginsPerSec = _Ss2gsLoginsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 6),
    _Ss2gsLoginsPerSec_Type()
)
ss2gsLoginsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsLoginsPerSec.setStatus("current")
_Ss2gsLogoutsPerSec_Type = Gauge32
_Ss2gsLogoutsPerSec_Object = MibTableColumn
ss2gsLogoutsPerSec = _Ss2gsLogoutsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 7),
    _Ss2gsLogoutsPerSec_Type()
)
ss2gsLogoutsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsLogoutsPerSec.setStatus("current")
_Ss2gsMarsDeadlocks_Type = Gauge32
_Ss2gsMarsDeadlocks_Object = MibTableColumn
ss2gsMarsDeadlocks = _Ss2gsMarsDeadlocks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 8),
    _Ss2gsMarsDeadlocks_Type()
)
ss2gsMarsDeadlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsMarsDeadlocks.setStatus("current")
_Ss2gsNonAtomicYieldRate_Type = Gauge32
_Ss2gsNonAtomicYieldRate_Object = MibTableColumn
ss2gsNonAtomicYieldRate = _Ss2gsNonAtomicYieldRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 9),
    _Ss2gsNonAtomicYieldRate_Type()
)
ss2gsNonAtomicYieldRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsNonAtomicYieldRate.setStatus("current")
_Ss2gsProcessesBlocked_Type = Gauge32
_Ss2gsProcessesBlocked_Object = MibTableColumn
ss2gsProcessesBlocked = _Ss2gsProcessesBlocked_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 10),
    _Ss2gsProcessesBlocked_Type()
)
ss2gsProcessesBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsProcessesBlocked.setStatus("current")
_Ss2gsSOAPEmptyRequests_Type = Gauge32
_Ss2gsSOAPEmptyRequests_Object = MibTableColumn
ss2gsSOAPEmptyRequests = _Ss2gsSOAPEmptyRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 11),
    _Ss2gsSOAPEmptyRequests_Type()
)
ss2gsSOAPEmptyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsSOAPEmptyRequests.setStatus("current")
_Ss2gsSOAPMethodInvocations_Type = Gauge32
_Ss2gsSOAPMethodInvocations_Object = MibTableColumn
ss2gsSOAPMethodInvocations = _Ss2gsSOAPMethodInvocations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 12),
    _Ss2gsSOAPMethodInvocations_Type()
)
ss2gsSOAPMethodInvocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsSOAPMethodInvocations.setStatus("current")
_Ss2gsSOAPSQLRequests_Type = Gauge32
_Ss2gsSOAPSQLRequests_Object = MibTableColumn
ss2gsSOAPSQLRequests = _Ss2gsSOAPSQLRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 13),
    _Ss2gsSOAPSQLRequests_Type()
)
ss2gsSOAPSQLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsSOAPSQLRequests.setStatus("current")
_Ss2gsSOAPSessionInitiateRequests_Type = Gauge32
_Ss2gsSOAPSessionInitiateRequests_Object = MibTableColumn
ss2gsSOAPSessionInitiateRequests = _Ss2gsSOAPSessionInitiateRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 14),
    _Ss2gsSOAPSessionInitiateRequests_Type()
)
ss2gsSOAPSessionInitiateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsSOAPSessionInitiateRequests.setStatus("current")
_Ss2gsSOAPSessionTerminateRequest_Type = Gauge32
_Ss2gsSOAPSessionTerminateRequest_Object = MibTableColumn
ss2gsSOAPSessionTerminateRequest = _Ss2gsSOAPSessionTerminateRequest_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 15),
    _Ss2gsSOAPSessionTerminateRequest_Type()
)
ss2gsSOAPSessionTerminateRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsSOAPSessionTerminateRequest.setStatus("current")
_Ss2gsSOAPWSDLRequests_Type = Gauge32
_Ss2gsSOAPWSDLRequests_Object = MibTableColumn
ss2gsSOAPWSDLRequests = _Ss2gsSOAPWSDLRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 16),
    _Ss2gsSOAPWSDLRequests_Type()
)
ss2gsSOAPWSDLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsSOAPWSDLRequests.setStatus("current")
_Ss2gsSQLTraceIOProviderLockWaits_Type = Gauge32
_Ss2gsSQLTraceIOProviderLockWaits_Object = MibTableColumn
ss2gsSQLTraceIOProviderLockWaits = _Ss2gsSQLTraceIOProviderLockWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 17),
    _Ss2gsSQLTraceIOProviderLockWaits_Type()
)
ss2gsSQLTraceIOProviderLockWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsSQLTraceIOProviderLockWaits.setStatus("current")
_Ss2gsTempTablesCreationRate_Type = Gauge32
_Ss2gsTempTablesCreationRate_Object = MibTableColumn
ss2gsTempTablesCreationRate = _Ss2gsTempTablesCreationRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 18),
    _Ss2gsTempTablesCreationRate_Type()
)
ss2gsTempTablesCreationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsTempTablesCreationRate.setStatus("current")
_Ss2gsTempTablesForDestruction_Type = Gauge32
_Ss2gsTempTablesForDestruction_Object = MibTableColumn
ss2gsTempTablesForDestruction = _Ss2gsTempTablesForDestruction_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 19),
    _Ss2gsTempTablesForDestruction_Type()
)
ss2gsTempTablesForDestruction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsTempTablesForDestruction.setStatus("current")
_Ss2gsTempdbRecoveryUnitId_Type = Gauge32
_Ss2gsTempdbRecoveryUnitId_Object = MibTableColumn
ss2gsTempdbRecoveryUnitId = _Ss2gsTempdbRecoveryUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 20),
    _Ss2gsTempdbRecoveryUnitId_Type()
)
ss2gsTempdbRecoveryUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsTempdbRecoveryUnitId.setStatus("current")
_Ss2gsTempdbRowsetId_Type = Gauge32
_Ss2gsTempdbRowsetId_Object = MibTableColumn
ss2gsTempdbRowsetId = _Ss2gsTempdbRowsetId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 21),
    _Ss2gsTempdbRowsetId_Type()
)
ss2gsTempdbRowsetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsTempdbRowsetId.setStatus("current")
_Ss2gsTraceEventNotificationQueue_Type = Gauge32
_Ss2gsTraceEventNotificationQueue_Object = MibTableColumn
ss2gsTraceEventNotificationQueue = _Ss2gsTraceEventNotificationQueue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 22),
    _Ss2gsTraceEventNotificationQueue_Type()
)
ss2gsTraceEventNotificationQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsTraceEventNotificationQueue.setStatus("current")
_Ss2gsTransactions_Type = Gauge32
_Ss2gsTransactions_Object = MibTableColumn
ss2gsTransactions = _Ss2gsTransactions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 23),
    _Ss2gsTransactions_Type()
)
ss2gsTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsTransactions.setStatus("current")
_Ss2gsUserConnections_Type = Gauge32
_Ss2gsUserConnections_Object = MibTableColumn
ss2gsUserConnections = _Ss2gsUserConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 19, 1, 24),
    _Ss2gsUserConnections_Type()
)
ss2gsUserConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2gsUserConnections.setStatus("current")
_Ss2LatchesTable_Object = MibTable
ss2LatchesTable = _Ss2LatchesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 20)
)
if mibBuilder.loadTexts:
    ss2LatchesTable.setStatus("current")
_Ss2LatchesEntry_Object = MibTableRow
ss2LatchesEntry = _Ss2LatchesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 20, 1)
)
ss2LatchesEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2LatchesEntry.setStatus("current")
_Ss2LatchesAverageLatchWaitTimeMs_Type = Gauge32
_Ss2LatchesAverageLatchWaitTimeMs_Object = MibTableColumn
ss2LatchesAverageLatchWaitTimeMs = _Ss2LatchesAverageLatchWaitTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 20, 1, 1),
    _Ss2LatchesAverageLatchWaitTimeMs_Type()
)
ss2LatchesAverageLatchWaitTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2LatchesAverageLatchWaitTimeMs.setStatus("current")
_Ss2LatchesLatchWaitsPerSec_Type = Gauge32
_Ss2LatchesLatchWaitsPerSec_Object = MibTableColumn
ss2LatchesLatchWaitsPerSec = _Ss2LatchesLatchWaitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 20, 1, 2),
    _Ss2LatchesLatchWaitsPerSec_Type()
)
ss2LatchesLatchWaitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2LatchesLatchWaitsPerSec.setStatus("current")
_Ss2LatchesNumberOfSuperLatches_Type = Gauge32
_Ss2LatchesNumberOfSuperLatches_Object = MibTableColumn
ss2LatchesNumberOfSuperLatches = _Ss2LatchesNumberOfSuperLatches_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 20, 1, 3),
    _Ss2LatchesNumberOfSuperLatches_Type()
)
ss2LatchesNumberOfSuperLatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2LatchesNumberOfSuperLatches.setStatus("current")
_Ss2LatchesSuLatchDemotionsSec_Type = Gauge32
_Ss2LatchesSuLatchDemotionsSec_Object = MibTableColumn
ss2LatchesSuLatchDemotionsSec = _Ss2LatchesSuLatchDemotionsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 20, 1, 4),
    _Ss2LatchesSuLatchDemotionsSec_Type()
)
ss2LatchesSuLatchDemotionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2LatchesSuLatchDemotionsSec.setStatus("current")
_Ss2LatchesSuLatchPromotionsSec_Type = Gauge32
_Ss2LatchesSuLatchPromotionsSec_Object = MibTableColumn
ss2LatchesSuLatchPromotionsSec = _Ss2LatchesSuLatchPromotionsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 20, 1, 5),
    _Ss2LatchesSuLatchPromotionsSec_Type()
)
ss2LatchesSuLatchPromotionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2LatchesSuLatchPromotionsSec.setStatus("current")
_Ss2LatchesTotalLatchWaitTimeMs_Type = Gauge32
_Ss2LatchesTotalLatchWaitTimeMs_Object = MibTableColumn
ss2LatchesTotalLatchWaitTimeMs = _Ss2LatchesTotalLatchWaitTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 20, 1, 6),
    _Ss2LatchesTotalLatchWaitTimeMs_Type()
)
ss2LatchesTotalLatchWaitTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2LatchesTotalLatchWaitTimeMs.setStatus("current")
_Ss2LocksTable_Object = MibTable
ss2LocksTable = _Ss2LocksTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 21)
)
if mibBuilder.loadTexts:
    ss2LocksTable.setStatus("current")
_Ss2LocksEntry_Object = MibTableRow
ss2LocksEntry = _Ss2LocksEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 21, 1)
)
ss2LocksEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2LocksInstance"),
)
if mibBuilder.loadTexts:
    ss2LocksEntry.setStatus("current")
_Ss2LocksInstance_Type = InstanceName
_Ss2LocksInstance_Object = MibTableColumn
ss2LocksInstance = _Ss2LocksInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 21, 1, 1),
    _Ss2LocksInstance_Type()
)
ss2LocksInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2LocksInstance.setStatus("current")
_Ss2LocksAverageWaitTimeMs_Type = Gauge32
_Ss2LocksAverageWaitTimeMs_Object = MibTableColumn
ss2LocksAverageWaitTimeMs = _Ss2LocksAverageWaitTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 21, 1, 2),
    _Ss2LocksAverageWaitTimeMs_Type()
)
ss2LocksAverageWaitTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2LocksAverageWaitTimeMs.setStatus("current")
_Ss2LocksLockRequestsPerSec_Type = Gauge32
_Ss2LocksLockRequestsPerSec_Object = MibTableColumn
ss2LocksLockRequestsPerSec = _Ss2LocksLockRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 21, 1, 3),
    _Ss2LocksLockRequestsPerSec_Type()
)
ss2LocksLockRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2LocksLockRequestsPerSec.setStatus("current")
_Ss2LocksTimeoutsGreaterThan0Sec_Type = Gauge32
_Ss2LocksTimeoutsGreaterThan0Sec_Object = MibTableColumn
ss2LocksTimeoutsGreaterThan0Sec = _Ss2LocksTimeoutsGreaterThan0Sec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 21, 1, 4),
    _Ss2LocksTimeoutsGreaterThan0Sec_Type()
)
ss2LocksTimeoutsGreaterThan0Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2LocksTimeoutsGreaterThan0Sec.setStatus("current")
_Ss2LocksLockTimeoutsPerSec_Type = Gauge32
_Ss2LocksLockTimeoutsPerSec_Object = MibTableColumn
ss2LocksLockTimeoutsPerSec = _Ss2LocksLockTimeoutsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 21, 1, 5),
    _Ss2LocksLockTimeoutsPerSec_Type()
)
ss2LocksLockTimeoutsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2LocksLockTimeoutsPerSec.setStatus("current")
_Ss2LocksLockWaitTimeMs_Type = Gauge32
_Ss2LocksLockWaitTimeMs_Object = MibTableColumn
ss2LocksLockWaitTimeMs = _Ss2LocksLockWaitTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 21, 1, 6),
    _Ss2LocksLockWaitTimeMs_Type()
)
ss2LocksLockWaitTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2LocksLockWaitTimeMs.setStatus("current")
_Ss2LocksLockWaitsPerSec_Type = Gauge32
_Ss2LocksLockWaitsPerSec_Object = MibTableColumn
ss2LocksLockWaitsPerSec = _Ss2LocksLockWaitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 21, 1, 7),
    _Ss2LocksLockWaitsPerSec_Type()
)
ss2LocksLockWaitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2LocksLockWaitsPerSec.setStatus("current")
_Ss2LocksNumberOfDeadlocksPerSec_Type = Gauge32
_Ss2LocksNumberOfDeadlocksPerSec_Object = MibTableColumn
ss2LocksNumberOfDeadlocksPerSec = _Ss2LocksNumberOfDeadlocksPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 21, 1, 8),
    _Ss2LocksNumberOfDeadlocksPerSec_Type()
)
ss2LocksNumberOfDeadlocksPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2LocksNumberOfDeadlocksPerSec.setStatus("current")
_Ss2MemoryManagerTable_Object = MibTable
ss2MemoryManagerTable = _Ss2MemoryManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22)
)
if mibBuilder.loadTexts:
    ss2MemoryManagerTable.setStatus("current")
_Ss2MemoryManagerEntry_Object = MibTableRow
ss2MemoryManagerEntry = _Ss2MemoryManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1)
)
ss2MemoryManagerEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2MemoryManagerEntry.setStatus("current")
_Ss2mmConnectionMemoryKB_Type = Gauge32
_Ss2mmConnectionMemoryKB_Object = MibTableColumn
ss2mmConnectionMemoryKB = _Ss2mmConnectionMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1, 1),
    _Ss2mmConnectionMemoryKB_Type()
)
ss2mmConnectionMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2mmConnectionMemoryKB.setStatus("current")
_Ss2mmGrantedWorkspaceMemoryKB_Type = Gauge32
_Ss2mmGrantedWorkspaceMemoryKB_Object = MibTableColumn
ss2mmGrantedWorkspaceMemoryKB = _Ss2mmGrantedWorkspaceMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1, 2),
    _Ss2mmGrantedWorkspaceMemoryKB_Type()
)
ss2mmGrantedWorkspaceMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2mmGrantedWorkspaceMemoryKB.setStatus("current")
_Ss2mmLockBlocks_Type = Gauge32
_Ss2mmLockBlocks_Object = MibTableColumn
ss2mmLockBlocks = _Ss2mmLockBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1, 3),
    _Ss2mmLockBlocks_Type()
)
ss2mmLockBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2mmLockBlocks.setStatus("current")
_Ss2mmLockBlocksAllocated_Type = Gauge32
_Ss2mmLockBlocksAllocated_Object = MibTableColumn
ss2mmLockBlocksAllocated = _Ss2mmLockBlocksAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1, 4),
    _Ss2mmLockBlocksAllocated_Type()
)
ss2mmLockBlocksAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2mmLockBlocksAllocated.setStatus("current")
_Ss2mmLockMemoryKB_Type = Gauge32
_Ss2mmLockMemoryKB_Object = MibTableColumn
ss2mmLockMemoryKB = _Ss2mmLockMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1, 5),
    _Ss2mmLockMemoryKB_Type()
)
ss2mmLockMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2mmLockMemoryKB.setStatus("current")
_Ss2mmLockOwnerBlocks_Type = Gauge32
_Ss2mmLockOwnerBlocks_Object = MibTableColumn
ss2mmLockOwnerBlocks = _Ss2mmLockOwnerBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1, 6),
    _Ss2mmLockOwnerBlocks_Type()
)
ss2mmLockOwnerBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2mmLockOwnerBlocks.setStatus("current")
_Ss2mmLockOwnerBlocksAllocated_Type = Gauge32
_Ss2mmLockOwnerBlocksAllocated_Object = MibTableColumn
ss2mmLockOwnerBlocksAllocated = _Ss2mmLockOwnerBlocksAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1, 7),
    _Ss2mmLockOwnerBlocksAllocated_Type()
)
ss2mmLockOwnerBlocksAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2mmLockOwnerBlocksAllocated.setStatus("current")
_Ss2mmMaximumWorkspaceMemoryKB_Type = Gauge32
_Ss2mmMaximumWorkspaceMemoryKB_Object = MibTableColumn
ss2mmMaximumWorkspaceMemoryKB = _Ss2mmMaximumWorkspaceMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1, 8),
    _Ss2mmMaximumWorkspaceMemoryKB_Type()
)
ss2mmMaximumWorkspaceMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2mmMaximumWorkspaceMemoryKB.setStatus("current")
_Ss2mmMemoryGrantsOutstanding_Type = Gauge32
_Ss2mmMemoryGrantsOutstanding_Object = MibTableColumn
ss2mmMemoryGrantsOutstanding = _Ss2mmMemoryGrantsOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1, 9),
    _Ss2mmMemoryGrantsOutstanding_Type()
)
ss2mmMemoryGrantsOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2mmMemoryGrantsOutstanding.setStatus("current")
_Ss2mmMemoryGrantsPending_Type = Gauge32
_Ss2mmMemoryGrantsPending_Object = MibTableColumn
ss2mmMemoryGrantsPending = _Ss2mmMemoryGrantsPending_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1, 10),
    _Ss2mmMemoryGrantsPending_Type()
)
ss2mmMemoryGrantsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2mmMemoryGrantsPending.setStatus("current")
_Ss2mmOptimizerMemoryKB_Type = Gauge32
_Ss2mmOptimizerMemoryKB_Object = MibTableColumn
ss2mmOptimizerMemoryKB = _Ss2mmOptimizerMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1, 11),
    _Ss2mmOptimizerMemoryKB_Type()
)
ss2mmOptimizerMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2mmOptimizerMemoryKB.setStatus("current")
_Ss2mmSQLCacheMemoryKB_Type = Gauge32
_Ss2mmSQLCacheMemoryKB_Object = MibTableColumn
ss2mmSQLCacheMemoryKB = _Ss2mmSQLCacheMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1, 12),
    _Ss2mmSQLCacheMemoryKB_Type()
)
ss2mmSQLCacheMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2mmSQLCacheMemoryKB.setStatus("current")
_Ss2mmTargetServerMemoryKB_Type = Gauge32
_Ss2mmTargetServerMemoryKB_Object = MibTableColumn
ss2mmTargetServerMemoryKB = _Ss2mmTargetServerMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1, 13),
    _Ss2mmTargetServerMemoryKB_Type()
)
ss2mmTargetServerMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2mmTargetServerMemoryKB.setStatus("current")
_Ss2mmTotalServerMemoryKB_Type = Gauge32
_Ss2mmTotalServerMemoryKB_Object = MibTableColumn
ss2mmTotalServerMemoryKB = _Ss2mmTotalServerMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 22, 1, 14),
    _Ss2mmTotalServerMemoryKB_Type()
)
ss2mmTotalServerMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2mmTotalServerMemoryKB.setStatus("current")
_Ss2PlanCacheTable_Object = MibTable
ss2PlanCacheTable = _Ss2PlanCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 23)
)
if mibBuilder.loadTexts:
    ss2PlanCacheTable.setStatus("current")
_Ss2PlanCacheEntry_Object = MibTableRow
ss2PlanCacheEntry = _Ss2PlanCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 23, 1)
)
ss2PlanCacheEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2PlanCacheInstance"),
)
if mibBuilder.loadTexts:
    ss2PlanCacheEntry.setStatus("current")
_Ss2PlanCacheInstance_Type = InstanceName
_Ss2PlanCacheInstance_Object = MibTableColumn
ss2PlanCacheInstance = _Ss2PlanCacheInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 23, 1, 1),
    _Ss2PlanCacheInstance_Type()
)
ss2PlanCacheInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2PlanCacheInstance.setStatus("current")
_Ss2PlanCacheCacheHitRatio_Type = Gauge32
_Ss2PlanCacheCacheHitRatio_Object = MibTableColumn
ss2PlanCacheCacheHitRatio = _Ss2PlanCacheCacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 23, 1, 2),
    _Ss2PlanCacheCacheHitRatio_Type()
)
ss2PlanCacheCacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2PlanCacheCacheHitRatio.setStatus("current")
_Ss2PlanCacheCacheObjectCounts_Type = Gauge32
_Ss2PlanCacheCacheObjectCounts_Object = MibTableColumn
ss2PlanCacheCacheObjectCounts = _Ss2PlanCacheCacheObjectCounts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 23, 1, 3),
    _Ss2PlanCacheCacheObjectCounts_Type()
)
ss2PlanCacheCacheObjectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2PlanCacheCacheObjectCounts.setStatus("current")
_Ss2PlanCacheCacheObjectsInUse_Type = Gauge32
_Ss2PlanCacheCacheObjectsInUse_Object = MibTableColumn
ss2PlanCacheCacheObjectsInUse = _Ss2PlanCacheCacheObjectsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 23, 1, 4),
    _Ss2PlanCacheCacheObjectsInUse_Type()
)
ss2PlanCacheCacheObjectsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2PlanCacheCacheObjectsInUse.setStatus("current")
_Ss2PlanCacheCachePages_Type = Gauge32
_Ss2PlanCacheCachePages_Object = MibTableColumn
ss2PlanCacheCachePages = _Ss2PlanCacheCachePages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 23, 1, 5),
    _Ss2PlanCacheCachePages_Type()
)
ss2PlanCacheCachePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2PlanCacheCachePages.setStatus("current")
_Ss2ReplicationAgentsTable_Object = MibTable
ss2ReplicationAgentsTable = _Ss2ReplicationAgentsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 24)
)
if mibBuilder.loadTexts:
    ss2ReplicationAgentsTable.setStatus("current")
_Ss2ReplicationAgentsEntry_Object = MibTableRow
ss2ReplicationAgentsEntry = _Ss2ReplicationAgentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 24, 1)
)
ss2ReplicationAgentsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2ReplicationAgentsInstance"),
)
if mibBuilder.loadTexts:
    ss2ReplicationAgentsEntry.setStatus("current")
_Ss2ReplicationAgentsInstance_Type = InstanceName
_Ss2ReplicationAgentsInstance_Object = MibTableColumn
ss2ReplicationAgentsInstance = _Ss2ReplicationAgentsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 24, 1, 1),
    _Ss2ReplicationAgentsInstance_Type()
)
ss2ReplicationAgentsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2ReplicationAgentsInstance.setStatus("current")
_Ss2ReplicationAgentsRunning_Type = Gauge32
_Ss2ReplicationAgentsRunning_Object = MibTableColumn
ss2ReplicationAgentsRunning = _Ss2ReplicationAgentsRunning_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 24, 1, 2),
    _Ss2ReplicationAgentsRunning_Type()
)
ss2ReplicationAgentsRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2ReplicationAgentsRunning.setStatus("current")
_Ss2ReplicationDistTable_Object = MibTable
ss2ReplicationDistTable = _Ss2ReplicationDistTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 25)
)
if mibBuilder.loadTexts:
    ss2ReplicationDistTable.setStatus("current")
_Ss2ReplicationDistEntry_Object = MibTableRow
ss2ReplicationDistEntry = _Ss2ReplicationDistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 25, 1)
)
ss2ReplicationDistEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2rdInstance"),
)
if mibBuilder.loadTexts:
    ss2ReplicationDistEntry.setStatus("current")
_Ss2rdInstance_Type = InstanceName
_Ss2rdInstance_Object = MibTableColumn
ss2rdInstance = _Ss2rdInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 25, 1, 1),
    _Ss2rdInstance_Type()
)
ss2rdInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rdInstance.setStatus("current")
_Ss2rdDistDeliveredCmdsPerSec_Type = Gauge32
_Ss2rdDistDeliveredCmdsPerSec_Object = MibTableColumn
ss2rdDistDeliveredCmdsPerSec = _Ss2rdDistDeliveredCmdsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 25, 1, 2),
    _Ss2rdDistDeliveredCmdsPerSec_Type()
)
ss2rdDistDeliveredCmdsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rdDistDeliveredCmdsPerSec.setStatus("current")
_Ss2rdDistDeliveredTransPerSec_Type = Gauge32
_Ss2rdDistDeliveredTransPerSec_Object = MibTableColumn
ss2rdDistDeliveredTransPerSec = _Ss2rdDistDeliveredTransPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 25, 1, 3),
    _Ss2rdDistDeliveredTransPerSec_Type()
)
ss2rdDistDeliveredTransPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rdDistDeliveredTransPerSec.setStatus("current")
_Ss2rdDistDeliveryLatency_Type = Gauge32
_Ss2rdDistDeliveryLatency_Object = MibTableColumn
ss2rdDistDeliveryLatency = _Ss2rdDistDeliveryLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 25, 1, 4),
    _Ss2rdDistDeliveryLatency_Type()
)
ss2rdDistDeliveryLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rdDistDeliveryLatency.setStatus("current")
_Ss2ReplicationLogreaderTable_Object = MibTable
ss2ReplicationLogreaderTable = _Ss2ReplicationLogreaderTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 26)
)
if mibBuilder.loadTexts:
    ss2ReplicationLogreaderTable.setStatus("current")
_Ss2ReplicationLogreaderEntry_Object = MibTableRow
ss2ReplicationLogreaderEntry = _Ss2ReplicationLogreaderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 26, 1)
)
ss2ReplicationLogreaderEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2rlInstance"),
)
if mibBuilder.loadTexts:
    ss2ReplicationLogreaderEntry.setStatus("current")
_Ss2rlInstance_Type = InstanceName
_Ss2rlInstance_Object = MibTableColumn
ss2rlInstance = _Ss2rlInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 26, 1, 1),
    _Ss2rlInstance_Type()
)
ss2rlInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rlInstance.setStatus("current")
_Ss2rlLogreaderDeliveredCmdsSec_Type = Gauge32
_Ss2rlLogreaderDeliveredCmdsSec_Object = MibTableColumn
ss2rlLogreaderDeliveredCmdsSec = _Ss2rlLogreaderDeliveredCmdsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 26, 1, 2),
    _Ss2rlLogreaderDeliveredCmdsSec_Type()
)
ss2rlLogreaderDeliveredCmdsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rlLogreaderDeliveredCmdsSec.setStatus("current")
_Ss2rlLogreaderDeliveredTransSec_Type = Gauge32
_Ss2rlLogreaderDeliveredTransSec_Object = MibTableColumn
ss2rlLogreaderDeliveredTransSec = _Ss2rlLogreaderDeliveredTransSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 26, 1, 3),
    _Ss2rlLogreaderDeliveredTransSec_Type()
)
ss2rlLogreaderDeliveredTransSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rlLogreaderDeliveredTransSec.setStatus("current")
_Ss2rlLogreaderDeliveryLatency_Type = Gauge32
_Ss2rlLogreaderDeliveryLatency_Object = MibTableColumn
ss2rlLogreaderDeliveryLatency = _Ss2rlLogreaderDeliveryLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 26, 1, 4),
    _Ss2rlLogreaderDeliveryLatency_Type()
)
ss2rlLogreaderDeliveryLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rlLogreaderDeliveryLatency.setStatus("current")
_Ss2ReplicationMergeTable_Object = MibTable
ss2ReplicationMergeTable = _Ss2ReplicationMergeTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 27)
)
if mibBuilder.loadTexts:
    ss2ReplicationMergeTable.setStatus("current")
_Ss2ReplicationMergeEntry_Object = MibTableRow
ss2ReplicationMergeEntry = _Ss2ReplicationMergeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 27, 1)
)
ss2ReplicationMergeEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2rmInstance"),
)
if mibBuilder.loadTexts:
    ss2ReplicationMergeEntry.setStatus("current")
_Ss2rmInstance_Type = InstanceName
_Ss2rmInstance_Object = MibTableColumn
ss2rmInstance = _Ss2rmInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 27, 1, 1),
    _Ss2rmInstance_Type()
)
ss2rmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rmInstance.setStatus("current")
_Ss2rmConflictsPerSec_Type = Gauge32
_Ss2rmConflictsPerSec_Object = MibTableColumn
ss2rmConflictsPerSec = _Ss2rmConflictsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 27, 1, 2),
    _Ss2rmConflictsPerSec_Type()
)
ss2rmConflictsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rmConflictsPerSec.setStatus("current")
_Ss2rmDownloadedChangesPerSec_Type = Gauge32
_Ss2rmDownloadedChangesPerSec_Object = MibTableColumn
ss2rmDownloadedChangesPerSec = _Ss2rmDownloadedChangesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 27, 1, 3),
    _Ss2rmDownloadedChangesPerSec_Type()
)
ss2rmDownloadedChangesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rmDownloadedChangesPerSec.setStatus("current")
_Ss2rmUploadedChangesPerSec_Type = Gauge32
_Ss2rmUploadedChangesPerSec_Object = MibTableColumn
ss2rmUploadedChangesPerSec = _Ss2rmUploadedChangesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 27, 1, 4),
    _Ss2rmUploadedChangesPerSec_Type()
)
ss2rmUploadedChangesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rmUploadedChangesPerSec.setStatus("current")
_Ss2ReplicationSnapshotTable_Object = MibTable
ss2ReplicationSnapshotTable = _Ss2ReplicationSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 28)
)
if mibBuilder.loadTexts:
    ss2ReplicationSnapshotTable.setStatus("current")
_Ss2ReplicationSnapshotEntry_Object = MibTableRow
ss2ReplicationSnapshotEntry = _Ss2ReplicationSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 28, 1)
)
ss2ReplicationSnapshotEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2rsInstance"),
)
if mibBuilder.loadTexts:
    ss2ReplicationSnapshotEntry.setStatus("current")
_Ss2rsInstance_Type = InstanceName
_Ss2rsInstance_Object = MibTableColumn
ss2rsInstance = _Ss2rsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 28, 1, 1),
    _Ss2rsInstance_Type()
)
ss2rsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rsInstance.setStatus("current")
_Ss2rsSnapshotDeliveredCmdsPerSec_Type = Gauge32
_Ss2rsSnapshotDeliveredCmdsPerSec_Object = MibTableColumn
ss2rsSnapshotDeliveredCmdsPerSec = _Ss2rsSnapshotDeliveredCmdsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 28, 1, 2),
    _Ss2rsSnapshotDeliveredCmdsPerSec_Type()
)
ss2rsSnapshotDeliveredCmdsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rsSnapshotDeliveredCmdsPerSec.setStatus("current")
_Ss2rsSnapshotDeliveredTransSec_Type = Gauge32
_Ss2rsSnapshotDeliveredTransSec_Object = MibTableColumn
ss2rsSnapshotDeliveredTransSec = _Ss2rsSnapshotDeliveredTransSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 28, 1, 3),
    _Ss2rsSnapshotDeliveredTransSec_Type()
)
ss2rsSnapshotDeliveredTransSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rsSnapshotDeliveredTransSec.setStatus("current")
_Ss2ResourcePoolStatsTable_Object = MibTable
ss2ResourcePoolStatsTable = _Ss2ResourcePoolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29)
)
if mibBuilder.loadTexts:
    ss2ResourcePoolStatsTable.setStatus("current")
_Ss2ResourcePoolStatsEntry_Object = MibTableRow
ss2ResourcePoolStatsEntry = _Ss2ResourcePoolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1)
)
ss2ResourcePoolStatsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2rpsInstance"),
)
if mibBuilder.loadTexts:
    ss2ResourcePoolStatsEntry.setStatus("current")
_Ss2rpsInstance_Type = InstanceName
_Ss2rpsInstance_Object = MibTableColumn
ss2rpsInstance = _Ss2rpsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 1),
    _Ss2rpsInstance_Type()
)
ss2rpsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsInstance.setStatus("current")
_Ss2rpsActiveMemoryGrantAmountKB_Type = Gauge32
_Ss2rpsActiveMemoryGrantAmountKB_Object = MibTableColumn
ss2rpsActiveMemoryGrantAmountKB = _Ss2rpsActiveMemoryGrantAmountKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 2),
    _Ss2rpsActiveMemoryGrantAmountKB_Type()
)
ss2rpsActiveMemoryGrantAmountKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsActiveMemoryGrantAmountKB.setStatus("current")
_Ss2rpsActiveMemoryGrantsCount_Type = Gauge32
_Ss2rpsActiveMemoryGrantsCount_Object = MibTableColumn
ss2rpsActiveMemoryGrantsCount = _Ss2rpsActiveMemoryGrantsCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 3),
    _Ss2rpsActiveMemoryGrantsCount_Type()
)
ss2rpsActiveMemoryGrantsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsActiveMemoryGrantsCount.setStatus("current")
_Ss2rpsCPUControlEffectPercent_Type = Gauge32
_Ss2rpsCPUControlEffectPercent_Object = MibTableColumn
ss2rpsCPUControlEffectPercent = _Ss2rpsCPUControlEffectPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 4),
    _Ss2rpsCPUControlEffectPercent_Type()
)
ss2rpsCPUControlEffectPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsCPUControlEffectPercent.setStatus("current")
_Ss2rpsCPUUsagePercent_Type = Gauge32
_Ss2rpsCPUUsagePercent_Object = MibTableColumn
ss2rpsCPUUsagePercent = _Ss2rpsCPUUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 5),
    _Ss2rpsCPUUsagePercent_Type()
)
ss2rpsCPUUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsCPUUsagePercent.setStatus("current")
_Ss2rpsCPUUsageTargetPercent_Type = Gauge32
_Ss2rpsCPUUsageTargetPercent_Object = MibTableColumn
ss2rpsCPUUsageTargetPercent = _Ss2rpsCPUUsageTargetPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 6),
    _Ss2rpsCPUUsageTargetPercent_Type()
)
ss2rpsCPUUsageTargetPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsCPUUsageTargetPercent.setStatus("current")
_Ss2rpsCacheMemoryTargetKB_Type = Gauge32
_Ss2rpsCacheMemoryTargetKB_Object = MibTableColumn
ss2rpsCacheMemoryTargetKB = _Ss2rpsCacheMemoryTargetKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 7),
    _Ss2rpsCacheMemoryTargetKB_Type()
)
ss2rpsCacheMemoryTargetKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsCacheMemoryTargetKB.setStatus("current")
_Ss2rpsCompileMemoryTargetKB_Type = Gauge32
_Ss2rpsCompileMemoryTargetKB_Object = MibTableColumn
ss2rpsCompileMemoryTargetKB = _Ss2rpsCompileMemoryTargetKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 8),
    _Ss2rpsCompileMemoryTargetKB_Type()
)
ss2rpsCompileMemoryTargetKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsCompileMemoryTargetKB.setStatus("current")
_Ss2rpsMaxMemoryKB_Type = Gauge32
_Ss2rpsMaxMemoryKB_Object = MibTableColumn
ss2rpsMaxMemoryKB = _Ss2rpsMaxMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 9),
    _Ss2rpsMaxMemoryKB_Type()
)
ss2rpsMaxMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsMaxMemoryKB.setStatus("current")
_Ss2rpsMemoryGrantTimeoutsPerSec_Type = Gauge32
_Ss2rpsMemoryGrantTimeoutsPerSec_Object = MibTableColumn
ss2rpsMemoryGrantTimeoutsPerSec = _Ss2rpsMemoryGrantTimeoutsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 10),
    _Ss2rpsMemoryGrantTimeoutsPerSec_Type()
)
ss2rpsMemoryGrantTimeoutsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsMemoryGrantTimeoutsPerSec.setStatus("current")
_Ss2rpsMemoryGrantsPerSec_Type = Gauge32
_Ss2rpsMemoryGrantsPerSec_Object = MibTableColumn
ss2rpsMemoryGrantsPerSec = _Ss2rpsMemoryGrantsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 11),
    _Ss2rpsMemoryGrantsPerSec_Type()
)
ss2rpsMemoryGrantsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsMemoryGrantsPerSec.setStatus("current")
_Ss2rpsPendingMemoryGrantsCount_Type = Gauge32
_Ss2rpsPendingMemoryGrantsCount_Object = MibTableColumn
ss2rpsPendingMemoryGrantsCount = _Ss2rpsPendingMemoryGrantsCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 12),
    _Ss2rpsPendingMemoryGrantsCount_Type()
)
ss2rpsPendingMemoryGrantsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsPendingMemoryGrantsCount.setStatus("current")
_Ss2rpsQueryExecMemoryTargetKB_Type = Gauge32
_Ss2rpsQueryExecMemoryTargetKB_Object = MibTableColumn
ss2rpsQueryExecMemoryTargetKB = _Ss2rpsQueryExecMemoryTargetKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 13),
    _Ss2rpsQueryExecMemoryTargetKB_Type()
)
ss2rpsQueryExecMemoryTargetKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsQueryExecMemoryTargetKB.setStatus("current")
_Ss2rpsTargetMemoryKB_Type = Gauge32
_Ss2rpsTargetMemoryKB_Object = MibTableColumn
ss2rpsTargetMemoryKB = _Ss2rpsTargetMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 14),
    _Ss2rpsTargetMemoryKB_Type()
)
ss2rpsTargetMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsTargetMemoryKB.setStatus("current")
_Ss2rpsUsedMemoryKB_Type = Gauge32
_Ss2rpsUsedMemoryKB_Object = MibTableColumn
ss2rpsUsedMemoryKB = _Ss2rpsUsedMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 29, 1, 15),
    _Ss2rpsUsedMemoryKB_Type()
)
ss2rpsUsedMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2rpsUsedMemoryKB.setStatus("current")
_Ss2SQLErrorsTable_Object = MibTable
ss2SQLErrorsTable = _Ss2SQLErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 30)
)
if mibBuilder.loadTexts:
    ss2SQLErrorsTable.setStatus("current")
_Ss2SQLErrorsEntry_Object = MibTableRow
ss2SQLErrorsEntry = _Ss2SQLErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 30, 1)
)
ss2SQLErrorsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2SQLErrorsInstance"),
)
if mibBuilder.loadTexts:
    ss2SQLErrorsEntry.setStatus("current")
_Ss2SQLErrorsInstance_Type = InstanceName
_Ss2SQLErrorsInstance_Object = MibTableColumn
ss2SQLErrorsInstance = _Ss2SQLErrorsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 30, 1, 1),
    _Ss2SQLErrorsInstance_Type()
)
ss2SQLErrorsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SQLErrorsInstance.setStatus("current")
_Ss2SQLErrorsErrorsPerSec_Type = Gauge32
_Ss2SQLErrorsErrorsPerSec_Object = MibTableColumn
ss2SQLErrorsErrorsPerSec = _Ss2SQLErrorsErrorsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 30, 1, 2),
    _Ss2SQLErrorsErrorsPerSec_Type()
)
ss2SQLErrorsErrorsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SQLErrorsErrorsPerSec.setStatus("current")
_Ss2SQLStatisticsTable_Object = MibTable
ss2SQLStatisticsTable = _Ss2SQLStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 31)
)
if mibBuilder.loadTexts:
    ss2SQLStatisticsTable.setStatus("current")
_Ss2SQLStatisticsEntry_Object = MibTableRow
ss2SQLStatisticsEntry = _Ss2SQLStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 31, 1)
)
ss2SQLStatisticsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2SQLStatisticsEntry.setStatus("current")
_Ss2sqsAutoParamAttemptsPerSec_Type = Gauge32
_Ss2sqsAutoParamAttemptsPerSec_Object = MibTableColumn
ss2sqsAutoParamAttemptsPerSec = _Ss2sqsAutoParamAttemptsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 31, 1, 1),
    _Ss2sqsAutoParamAttemptsPerSec_Type()
)
ss2sqsAutoParamAttemptsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2sqsAutoParamAttemptsPerSec.setStatus("current")
_Ss2sqsBatchRequestsPerSec_Type = Gauge32
_Ss2sqsBatchRequestsPerSec_Object = MibTableColumn
ss2sqsBatchRequestsPerSec = _Ss2sqsBatchRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 31, 1, 2),
    _Ss2sqsBatchRequestsPerSec_Type()
)
ss2sqsBatchRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2sqsBatchRequestsPerSec.setStatus("current")
_Ss2sqsFailedAutoParamsPerSec_Type = Gauge32
_Ss2sqsFailedAutoParamsPerSec_Object = MibTableColumn
ss2sqsFailedAutoParamsPerSec = _Ss2sqsFailedAutoParamsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 31, 1, 3),
    _Ss2sqsFailedAutoParamsPerSec_Type()
)
ss2sqsFailedAutoParamsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2sqsFailedAutoParamsPerSec.setStatus("current")
_Ss2sqsForcedParameterizationsSec_Type = Gauge32
_Ss2sqsForcedParameterizationsSec_Object = MibTableColumn
ss2sqsForcedParameterizationsSec = _Ss2sqsForcedParameterizationsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 31, 1, 4),
    _Ss2sqsForcedParameterizationsSec_Type()
)
ss2sqsForcedParameterizationsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2sqsForcedParameterizationsSec.setStatus("current")
_Ss2sqsGuidedPlanExecutionsPerSec_Type = Gauge32
_Ss2sqsGuidedPlanExecutionsPerSec_Object = MibTableColumn
ss2sqsGuidedPlanExecutionsPerSec = _Ss2sqsGuidedPlanExecutionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 31, 1, 5),
    _Ss2sqsGuidedPlanExecutionsPerSec_Type()
)
ss2sqsGuidedPlanExecutionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2sqsGuidedPlanExecutionsPerSec.setStatus("current")
_Ss2sqsMisguidedPlanExecutionsSec_Type = Gauge32
_Ss2sqsMisguidedPlanExecutionsSec_Object = MibTableColumn
ss2sqsMisguidedPlanExecutionsSec = _Ss2sqsMisguidedPlanExecutionsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 31, 1, 6),
    _Ss2sqsMisguidedPlanExecutionsSec_Type()
)
ss2sqsMisguidedPlanExecutionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2sqsMisguidedPlanExecutionsSec.setStatus("current")
_Ss2sqsSQLAttentionRate_Type = Gauge32
_Ss2sqsSQLAttentionRate_Object = MibTableColumn
ss2sqsSQLAttentionRate = _Ss2sqsSQLAttentionRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 31, 1, 7),
    _Ss2sqsSQLAttentionRate_Type()
)
ss2sqsSQLAttentionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2sqsSQLAttentionRate.setStatus("current")
_Ss2sqsSQLCompilationsPerSec_Type = Gauge32
_Ss2sqsSQLCompilationsPerSec_Object = MibTableColumn
ss2sqsSQLCompilationsPerSec = _Ss2sqsSQLCompilationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 31, 1, 8),
    _Ss2sqsSQLCompilationsPerSec_Type()
)
ss2sqsSQLCompilationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2sqsSQLCompilationsPerSec.setStatus("current")
_Ss2sqsSQLReCompilationsPerSec_Type = Gauge32
_Ss2sqsSQLReCompilationsPerSec_Object = MibTableColumn
ss2sqsSQLReCompilationsPerSec = _Ss2sqsSQLReCompilationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 31, 1, 9),
    _Ss2sqsSQLReCompilationsPerSec_Type()
)
ss2sqsSQLReCompilationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2sqsSQLReCompilationsPerSec.setStatus("current")
_Ss2sqsSafeAutoParamsPerSec_Type = Gauge32
_Ss2sqsSafeAutoParamsPerSec_Object = MibTableColumn
ss2sqsSafeAutoParamsPerSec = _Ss2sqsSafeAutoParamsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 31, 1, 10),
    _Ss2sqsSafeAutoParamsPerSec_Type()
)
ss2sqsSafeAutoParamsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2sqsSafeAutoParamsPerSec.setStatus("current")
_Ss2sqsUnsafeAutoParamsPerSec_Type = Gauge32
_Ss2sqsUnsafeAutoParamsPerSec_Object = MibTableColumn
ss2sqsUnsafeAutoParamsPerSec = _Ss2sqsUnsafeAutoParamsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 31, 1, 11),
    _Ss2sqsUnsafeAutoParamsPerSec_Type()
)
ss2sqsUnsafeAutoParamsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2sqsUnsafeAutoParamsPerSec.setStatus("current")
_Ss2SSISPipelineTable_Object = MibTable
ss2SSISPipelineTable = _Ss2SSISPipelineTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 32)
)
if mibBuilder.loadTexts:
    ss2SSISPipelineTable.setStatus("current")
_Ss2SSISPipelineEntry_Object = MibTableRow
ss2SSISPipelineEntry = _Ss2SSISPipelineEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 32, 1)
)
ss2SSISPipelineEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2SSISPipelineEntry.setStatus("current")
_Ss2SSISPipelineBLOBBytesRead_Type = Gauge32
_Ss2SSISPipelineBLOBBytesRead_Object = MibTableColumn
ss2SSISPipelineBLOBBytesRead = _Ss2SSISPipelineBLOBBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 32, 1, 1),
    _Ss2SSISPipelineBLOBBytesRead_Type()
)
ss2SSISPipelineBLOBBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SSISPipelineBLOBBytesRead.setStatus("current")
_Ss2SSISPipelineBLOBBytesWritten_Type = Gauge32
_Ss2SSISPipelineBLOBBytesWritten_Object = MibTableColumn
ss2SSISPipelineBLOBBytesWritten = _Ss2SSISPipelineBLOBBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 32, 1, 2),
    _Ss2SSISPipelineBLOBBytesWritten_Type()
)
ss2SSISPipelineBLOBBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SSISPipelineBLOBBytesWritten.setStatus("current")
_Ss2SSISPipelineBLOBFilesInUse_Type = Gauge32
_Ss2SSISPipelineBLOBFilesInUse_Object = MibTableColumn
ss2SSISPipelineBLOBFilesInUse = _Ss2SSISPipelineBLOBFilesInUse_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 32, 1, 3),
    _Ss2SSISPipelineBLOBFilesInUse_Type()
)
ss2SSISPipelineBLOBFilesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SSISPipelineBLOBFilesInUse.setStatus("current")
_Ss2SSISPipelineBufferMemory_Type = Gauge32
_Ss2SSISPipelineBufferMemory_Object = MibTableColumn
ss2SSISPipelineBufferMemory = _Ss2SSISPipelineBufferMemory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 32, 1, 4),
    _Ss2SSISPipelineBufferMemory_Type()
)
ss2SSISPipelineBufferMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SSISPipelineBufferMemory.setStatus("current")
_Ss2SSISPipelineBuffersInUse_Type = Gauge32
_Ss2SSISPipelineBuffersInUse_Object = MibTableColumn
ss2SSISPipelineBuffersInUse = _Ss2SSISPipelineBuffersInUse_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 32, 1, 5),
    _Ss2SSISPipelineBuffersInUse_Type()
)
ss2SSISPipelineBuffersInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SSISPipelineBuffersInUse.setStatus("current")
_Ss2SSISPipelineBuffersSpooled_Type = Gauge32
_Ss2SSISPipelineBuffersSpooled_Object = MibTableColumn
ss2SSISPipelineBuffersSpooled = _Ss2SSISPipelineBuffersSpooled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 32, 1, 6),
    _Ss2SSISPipelineBuffersSpooled_Type()
)
ss2SSISPipelineBuffersSpooled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SSISPipelineBuffersSpooled.setStatus("current")
_Ss2SSISPipelineFlatBufferMemory_Type = Gauge32
_Ss2SSISPipelineFlatBufferMemory_Object = MibTableColumn
ss2SSISPipelineFlatBufferMemory = _Ss2SSISPipelineFlatBufferMemory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 32, 1, 7),
    _Ss2SSISPipelineFlatBufferMemory_Type()
)
ss2SSISPipelineFlatBufferMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SSISPipelineFlatBufferMemory.setStatus("current")
_Ss2SSISPipelineFlatBuffersInUse_Type = Gauge32
_Ss2SSISPipelineFlatBuffersInUse_Object = MibTableColumn
ss2SSISPipelineFlatBuffersInUse = _Ss2SSISPipelineFlatBuffersInUse_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 32, 1, 8),
    _Ss2SSISPipelineFlatBuffersInUse_Type()
)
ss2SSISPipelineFlatBuffersInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SSISPipelineFlatBuffersInUse.setStatus("current")
_Ss2SSISPipelinePrivateBuffMemory_Type = Gauge32
_Ss2SSISPipelinePrivateBuffMemory_Object = MibTableColumn
ss2SSISPipelinePrivateBuffMemory = _Ss2SSISPipelinePrivateBuffMemory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 32, 1, 9),
    _Ss2SSISPipelinePrivateBuffMemory_Type()
)
ss2SSISPipelinePrivateBuffMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SSISPipelinePrivateBuffMemory.setStatus("current")
_Ss2SSISPipelinePrivateBuffersUse_Type = Gauge32
_Ss2SSISPipelinePrivateBuffersUse_Object = MibTableColumn
ss2SSISPipelinePrivateBuffersUse = _Ss2SSISPipelinePrivateBuffersUse_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 32, 1, 10),
    _Ss2SSISPipelinePrivateBuffersUse_Type()
)
ss2SSISPipelinePrivateBuffersUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SSISPipelinePrivateBuffersUse.setStatus("current")
_Ss2SSISPipelineRowsRead_Type = Gauge32
_Ss2SSISPipelineRowsRead_Object = MibTableColumn
ss2SSISPipelineRowsRead = _Ss2SSISPipelineRowsRead_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 32, 1, 11),
    _Ss2SSISPipelineRowsRead_Type()
)
ss2SSISPipelineRowsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SSISPipelineRowsRead.setStatus("current")
_Ss2SSISPipelineRowsWritten_Type = Gauge32
_Ss2SSISPipelineRowsWritten_Object = MibTableColumn
ss2SSISPipelineRowsWritten = _Ss2SSISPipelineRowsWritten_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 32, 1, 12),
    _Ss2SSISPipelineRowsWritten_Type()
)
ss2SSISPipelineRowsWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SSISPipelineRowsWritten.setStatus("current")
_Ss2SSISServiceTable_Object = MibTable
ss2SSISServiceTable = _Ss2SSISServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 33)
)
if mibBuilder.loadTexts:
    ss2SSISServiceTable.setStatus("current")
_Ss2SSISServiceEntry_Object = MibTableRow
ss2SSISServiceEntry = _Ss2SSISServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 33, 1)
)
ss2SSISServiceEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2SSISServiceEntry.setStatus("current")
_Ss2SSISServiceSSISPackageInstanc_Type = Gauge32
_Ss2SSISServiceSSISPackageInstanc_Object = MibTableColumn
ss2SSISServiceSSISPackageInstanc = _Ss2SSISServiceSSISPackageInstanc_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 33, 1, 1),
    _Ss2SSISServiceSSISPackageInstanc_Type()
)
ss2SSISServiceSSISPackageInstanc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2SSISServiceSSISPackageInstanc.setStatus("current")
_Ss2TraceEventStatisticsTable_Object = MibTable
ss2TraceEventStatisticsTable = _Ss2TraceEventStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 34)
)
if mibBuilder.loadTexts:
    ss2TraceEventStatisticsTable.setStatus("current")
_Ss2TraceEventStatisticsEntry_Object = MibTableRow
ss2TraceEventStatisticsEntry = _Ss2TraceEventStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 34, 1)
)
ss2TraceEventStatisticsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2tesInstance"),
)
if mibBuilder.loadTexts:
    ss2TraceEventStatisticsEntry.setStatus("current")
_Ss2tesInstance_Type = InstanceName
_Ss2tesInstance_Object = MibTableColumn
ss2tesInstance = _Ss2tesInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 34, 1, 1),
    _Ss2tesInstance_Type()
)
ss2tesInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2tesInstance.setStatus("current")
_Ss2tesBytesPerSec_Type = Gauge32
_Ss2tesBytesPerSec_Object = MibTableColumn
ss2tesBytesPerSec = _Ss2tesBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 34, 1, 2),
    _Ss2tesBytesPerSec_Type()
)
ss2tesBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2tesBytesPerSec.setStatus("current")
_Ss2tesCPUTicksPerSec_Type = Gauge32
_Ss2tesCPUTicksPerSec_Object = MibTableColumn
ss2tesCPUTicksPerSec = _Ss2tesCPUTicksPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 34, 1, 3),
    _Ss2tesCPUTicksPerSec_Type()
)
ss2tesCPUTicksPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2tesCPUTicksPerSec.setStatus("current")
_Ss2tesEventsFilteredPerSec_Type = Gauge32
_Ss2tesEventsFilteredPerSec_Object = MibTableColumn
ss2tesEventsFilteredPerSec = _Ss2tesEventsFilteredPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 34, 1, 4),
    _Ss2tesEventsFilteredPerSec_Type()
)
ss2tesEventsFilteredPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2tesEventsFilteredPerSec.setStatus("current")
_Ss2tesEventsFiredPerSec_Type = Gauge32
_Ss2tesEventsFiredPerSec_Object = MibTableColumn
ss2tesEventsFiredPerSec = _Ss2tesEventsFiredPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 34, 1, 5),
    _Ss2tesEventsFiredPerSec_Type()
)
ss2tesEventsFiredPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2tesEventsFiredPerSec.setStatus("current")
_Ss2tesEventsPrefilteredPerSec_Type = Gauge32
_Ss2tesEventsPrefilteredPerSec_Object = MibTableColumn
ss2tesEventsPrefilteredPerSec = _Ss2tesEventsPrefilteredPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 34, 1, 6),
    _Ss2tesEventsPrefilteredPerSec_Type()
)
ss2tesEventsPrefilteredPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2tesEventsPrefilteredPerSec.setStatus("current")
_Ss2TraceStatisticsTable_Object = MibTable
ss2TraceStatisticsTable = _Ss2TraceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 35)
)
if mibBuilder.loadTexts:
    ss2TraceStatisticsTable.setStatus("current")
_Ss2TraceStatisticsEntry_Object = MibTableRow
ss2TraceStatisticsEntry = _Ss2TraceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 35, 1)
)
ss2TraceStatisticsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2tstInstance"),
)
if mibBuilder.loadTexts:
    ss2TraceStatisticsEntry.setStatus("current")
_Ss2tstInstance_Type = InstanceName
_Ss2tstInstance_Object = MibTableColumn
ss2tstInstance = _Ss2tstInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 35, 1, 1),
    _Ss2tstInstance_Type()
)
ss2tstInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2tstInstance.setStatus("current")
_Ss2tstBytesPerSec_Type = Gauge32
_Ss2tstBytesPerSec_Object = MibTableColumn
ss2tstBytesPerSec = _Ss2tstBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 35, 1, 2),
    _Ss2tstBytesPerSec_Type()
)
ss2tstBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2tstBytesPerSec.setStatus("current")
_Ss2tstDroppedEventsPerSec_Type = Gauge32
_Ss2tstDroppedEventsPerSec_Object = MibTableColumn
ss2tstDroppedEventsPerSec = _Ss2tstDroppedEventsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 35, 1, 3),
    _Ss2tstDroppedEventsPerSec_Type()
)
ss2tstDroppedEventsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2tstDroppedEventsPerSec.setStatus("current")
_Ss2tstEventsFilteredPerSec_Type = Gauge32
_Ss2tstEventsFilteredPerSec_Object = MibTableColumn
ss2tstEventsFilteredPerSec = _Ss2tstEventsFilteredPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 35, 1, 4),
    _Ss2tstEventsFilteredPerSec_Type()
)
ss2tstEventsFilteredPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2tstEventsFilteredPerSec.setStatus("current")
_Ss2tstEventsFiredPerSec_Type = Gauge32
_Ss2tstEventsFiredPerSec_Object = MibTableColumn
ss2tstEventsFiredPerSec = _Ss2tstEventsFiredPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 35, 1, 5),
    _Ss2tstEventsFiredPerSec_Type()
)
ss2tstEventsFiredPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2tstEventsFiredPerSec.setStatus("current")
_Ss2TransactionsTable_Object = MibTable
ss2TransactionsTable = _Ss2TransactionsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36)
)
if mibBuilder.loadTexts:
    ss2TransactionsTable.setStatus("current")
_Ss2TransactionsEntry_Object = MibTableRow
ss2TransactionsEntry = _Ss2TransactionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36, 1)
)
ss2TransactionsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
)
if mibBuilder.loadTexts:
    ss2TransactionsEntry.setStatus("current")
_Ss2trnFreeSpaceInTempdbKB_Type = Gauge32
_Ss2trnFreeSpaceInTempdbKB_Object = MibTableColumn
ss2trnFreeSpaceInTempdbKB = _Ss2trnFreeSpaceInTempdbKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36, 1, 1),
    _Ss2trnFreeSpaceInTempdbKB_Type()
)
ss2trnFreeSpaceInTempdbKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2trnFreeSpaceInTempdbKB.setStatus("current")
_Ss2trnLongestTransactRunningTime_Type = Gauge32
_Ss2trnLongestTransactRunningTime_Object = MibTableColumn
ss2trnLongestTransactRunningTime = _Ss2trnLongestTransactRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36, 1, 2),
    _Ss2trnLongestTransactRunningTime_Type()
)
ss2trnLongestTransactRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2trnLongestTransactRunningTime.setStatus("current")
_Ss2trnNonSnapshotVersionTransact_Type = Gauge32
_Ss2trnNonSnapshotVersionTransact_Object = MibTableColumn
ss2trnNonSnapshotVersionTransact = _Ss2trnNonSnapshotVersionTransact_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36, 1, 3),
    _Ss2trnNonSnapshotVersionTransact_Type()
)
ss2trnNonSnapshotVersionTransact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2trnNonSnapshotVersionTransact.setStatus("current")
_Ss2trnSnapshotTransactions_Type = Gauge32
_Ss2trnSnapshotTransactions_Object = MibTableColumn
ss2trnSnapshotTransactions = _Ss2trnSnapshotTransactions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36, 1, 4),
    _Ss2trnSnapshotTransactions_Type()
)
ss2trnSnapshotTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2trnSnapshotTransactions.setStatus("current")
_Ss2trnTransactions_Type = Gauge32
_Ss2trnTransactions_Object = MibTableColumn
ss2trnTransactions = _Ss2trnTransactions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36, 1, 5),
    _Ss2trnTransactions_Type()
)
ss2trnTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2trnTransactions.setStatus("current")
_Ss2trnUpdateSnapshotTransactions_Type = Gauge32
_Ss2trnUpdateSnapshotTransactions_Object = MibTableColumn
ss2trnUpdateSnapshotTransactions = _Ss2trnUpdateSnapshotTransactions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36, 1, 6),
    _Ss2trnUpdateSnapshotTransactions_Type()
)
ss2trnUpdateSnapshotTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2trnUpdateSnapshotTransactions.setStatus("current")
_Ss2trnUpdateConflictRatio_Type = Gauge32
_Ss2trnUpdateConflictRatio_Object = MibTableColumn
ss2trnUpdateConflictRatio = _Ss2trnUpdateConflictRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36, 1, 7),
    _Ss2trnUpdateConflictRatio_Type()
)
ss2trnUpdateConflictRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2trnUpdateConflictRatio.setStatus("current")
_Ss2trnVersionCleanupRateKBPerS_Type = Gauge32
_Ss2trnVersionCleanupRateKBPerS_Object = MibTableColumn
ss2trnVersionCleanupRateKBPerS = _Ss2trnVersionCleanupRateKBPerS_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36, 1, 8),
    _Ss2trnVersionCleanupRateKBPerS_Type()
)
ss2trnVersionCleanupRateKBPerS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2trnVersionCleanupRateKBPerS.setStatus("current")
_Ss2trnVersionGenerationRateKBS_Type = Gauge32
_Ss2trnVersionGenerationRateKBS_Object = MibTableColumn
ss2trnVersionGenerationRateKBS = _Ss2trnVersionGenerationRateKBS_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36, 1, 9),
    _Ss2trnVersionGenerationRateKBS_Type()
)
ss2trnVersionGenerationRateKBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2trnVersionGenerationRateKBS.setStatus("current")
_Ss2trnVersionStoreSizeKB_Type = Gauge32
_Ss2trnVersionStoreSizeKB_Object = MibTableColumn
ss2trnVersionStoreSizeKB = _Ss2trnVersionStoreSizeKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36, 1, 10),
    _Ss2trnVersionStoreSizeKB_Type()
)
ss2trnVersionStoreSizeKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2trnVersionStoreSizeKB.setStatus("current")
_Ss2trnVersionStoreUnitCount_Type = Gauge32
_Ss2trnVersionStoreUnitCount_Object = MibTableColumn
ss2trnVersionStoreUnitCount = _Ss2trnVersionStoreUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36, 1, 11),
    _Ss2trnVersionStoreUnitCount_Type()
)
ss2trnVersionStoreUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2trnVersionStoreUnitCount.setStatus("current")
_Ss2trnVersionStoreUnitCreation_Type = Gauge32
_Ss2trnVersionStoreUnitCreation_Object = MibTableColumn
ss2trnVersionStoreUnitCreation = _Ss2trnVersionStoreUnitCreation_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36, 1, 12),
    _Ss2trnVersionStoreUnitCreation_Type()
)
ss2trnVersionStoreUnitCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2trnVersionStoreUnitCreation.setStatus("current")
_Ss2trnVersionStoreUnitTruncation_Type = Gauge32
_Ss2trnVersionStoreUnitTruncation_Object = MibTableColumn
ss2trnVersionStoreUnitTruncation = _Ss2trnVersionStoreUnitTruncation_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 36, 1, 13),
    _Ss2trnVersionStoreUnitTruncation_Type()
)
ss2trnVersionStoreUnitTruncation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2trnVersionStoreUnitTruncation.setStatus("current")
_Ss2UserSettableTable_Object = MibTable
ss2UserSettableTable = _Ss2UserSettableTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 37)
)
if mibBuilder.loadTexts:
    ss2UserSettableTable.setStatus("current")
_Ss2UserSettableEntry_Object = MibTableRow
ss2UserSettableEntry = _Ss2UserSettableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 37, 1)
)
ss2UserSettableEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2UserSettableInstance"),
)
if mibBuilder.loadTexts:
    ss2UserSettableEntry.setStatus("current")
_Ss2UserSettableInstance_Type = InstanceName
_Ss2UserSettableInstance_Object = MibTableColumn
ss2UserSettableInstance = _Ss2UserSettableInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 37, 1, 1),
    _Ss2UserSettableInstance_Type()
)
ss2UserSettableInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2UserSettableInstance.setStatus("current")
_Ss2UserSettableQuery_Type = Gauge32
_Ss2UserSettableQuery_Object = MibTableColumn
ss2UserSettableQuery = _Ss2UserSettableQuery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 37, 1, 2),
    _Ss2UserSettableQuery_Type()
)
ss2UserSettableQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2UserSettableQuery.setStatus("current")
_Ss2WaitStatisticsTable_Object = MibTable
ss2WaitStatisticsTable = _Ss2WaitStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38)
)
if mibBuilder.loadTexts:
    ss2WaitStatisticsTable.setStatus("current")
_Ss2WaitStatisticsEntry_Object = MibTableRow
ss2WaitStatisticsEntry = _Ss2WaitStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38, 1)
)
ss2WaitStatisticsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2wsInstance"),
)
if mibBuilder.loadTexts:
    ss2WaitStatisticsEntry.setStatus("current")
_Ss2wsInstance_Type = InstanceName
_Ss2wsInstance_Object = MibTableColumn
ss2wsInstance = _Ss2wsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38, 1, 1),
    _Ss2wsInstance_Type()
)
ss2wsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wsInstance.setStatus("current")
_Ss2wsLockWaits_Type = Gauge32
_Ss2wsLockWaits_Object = MibTableColumn
ss2wsLockWaits = _Ss2wsLockWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38, 1, 2),
    _Ss2wsLockWaits_Type()
)
ss2wsLockWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wsLockWaits.setStatus("current")
_Ss2wsLogBufferWaits_Type = Gauge32
_Ss2wsLogBufferWaits_Object = MibTableColumn
ss2wsLogBufferWaits = _Ss2wsLogBufferWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38, 1, 3),
    _Ss2wsLogBufferWaits_Type()
)
ss2wsLogBufferWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wsLogBufferWaits.setStatus("current")
_Ss2wsLogWriteWaits_Type = Gauge32
_Ss2wsLogWriteWaits_Object = MibTableColumn
ss2wsLogWriteWaits = _Ss2wsLogWriteWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38, 1, 4),
    _Ss2wsLogWriteWaits_Type()
)
ss2wsLogWriteWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wsLogWriteWaits.setStatus("current")
_Ss2wsMemoryGrantQueueWaits_Type = Gauge32
_Ss2wsMemoryGrantQueueWaits_Object = MibTableColumn
ss2wsMemoryGrantQueueWaits = _Ss2wsMemoryGrantQueueWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38, 1, 5),
    _Ss2wsMemoryGrantQueueWaits_Type()
)
ss2wsMemoryGrantQueueWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wsMemoryGrantQueueWaits.setStatus("current")
_Ss2wsNetworkIOWaits_Type = Gauge32
_Ss2wsNetworkIOWaits_Object = MibTableColumn
ss2wsNetworkIOWaits = _Ss2wsNetworkIOWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38, 1, 6),
    _Ss2wsNetworkIOWaits_Type()
)
ss2wsNetworkIOWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wsNetworkIOWaits.setStatus("current")
_Ss2wsNonPageLatchWaits_Type = Gauge32
_Ss2wsNonPageLatchWaits_Object = MibTableColumn
ss2wsNonPageLatchWaits = _Ss2wsNonPageLatchWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38, 1, 7),
    _Ss2wsNonPageLatchWaits_Type()
)
ss2wsNonPageLatchWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wsNonPageLatchWaits.setStatus("current")
_Ss2wsPageIOLatchWaits_Type = Gauge32
_Ss2wsPageIOLatchWaits_Object = MibTableColumn
ss2wsPageIOLatchWaits = _Ss2wsPageIOLatchWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38, 1, 8),
    _Ss2wsPageIOLatchWaits_Type()
)
ss2wsPageIOLatchWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wsPageIOLatchWaits.setStatus("current")
_Ss2wsPageLatchWaits_Type = Gauge32
_Ss2wsPageLatchWaits_Object = MibTableColumn
ss2wsPageLatchWaits = _Ss2wsPageLatchWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38, 1, 9),
    _Ss2wsPageLatchWaits_Type()
)
ss2wsPageLatchWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wsPageLatchWaits.setStatus("current")
_Ss2wsThreadSafeMemoryObjectsWait_Type = Gauge32
_Ss2wsThreadSafeMemoryObjectsWait_Object = MibTableColumn
ss2wsThreadSafeMemoryObjectsWait = _Ss2wsThreadSafeMemoryObjectsWait_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38, 1, 10),
    _Ss2wsThreadSafeMemoryObjectsWait_Type()
)
ss2wsThreadSafeMemoryObjectsWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wsThreadSafeMemoryObjectsWait.setStatus("current")
_Ss2wsTransactionOwnershipWaits_Type = Gauge32
_Ss2wsTransactionOwnershipWaits_Object = MibTableColumn
ss2wsTransactionOwnershipWaits = _Ss2wsTransactionOwnershipWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38, 1, 11),
    _Ss2wsTransactionOwnershipWaits_Type()
)
ss2wsTransactionOwnershipWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wsTransactionOwnershipWaits.setStatus("current")
_Ss2wsWaitForTheWorker_Type = Gauge32
_Ss2wsWaitForTheWorker_Object = MibTableColumn
ss2wsWaitForTheWorker = _Ss2wsWaitForTheWorker_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38, 1, 12),
    _Ss2wsWaitForTheWorker_Type()
)
ss2wsWaitForTheWorker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wsWaitForTheWorker.setStatus("current")
_Ss2wsWorkspaceSynchronizatWaits_Type = Gauge32
_Ss2wsWorkspaceSynchronizatWaits_Object = MibTableColumn
ss2wsWorkspaceSynchronizatWaits = _Ss2wsWorkspaceSynchronizatWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 38, 1, 13),
    _Ss2wsWorkspaceSynchronizatWaits_Type()
)
ss2wsWorkspaceSynchronizatWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wsWorkspaceSynchronizatWaits.setStatus("current")
_Ss2WorkloadGroupStatsTable_Object = MibTable
ss2WorkloadGroupStatsTable = _Ss2WorkloadGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 39)
)
if mibBuilder.loadTexts:
    ss2WorkloadGroupStatsTable.setStatus("current")
_Ss2WorkloadGroupStatsEntry_Object = MibTableRow
ss2WorkloadGroupStatsEntry = _Ss2WorkloadGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 39, 1)
)
ss2WorkloadGroupStatsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "ss2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "ss2wgsInstance"),
)
if mibBuilder.loadTexts:
    ss2WorkloadGroupStatsEntry.setStatus("current")
_Ss2wgsInstance_Type = InstanceName
_Ss2wgsInstance_Object = MibTableColumn
ss2wgsInstance = _Ss2wgsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 39, 1, 1),
    _Ss2wgsInstance_Type()
)
ss2wgsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wgsInstance.setStatus("current")
_Ss2wgsActiveParallelThreads_Type = Gauge32
_Ss2wgsActiveParallelThreads_Object = MibTableColumn
ss2wgsActiveParallelThreads = _Ss2wgsActiveParallelThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 39, 1, 2),
    _Ss2wgsActiveParallelThreads_Type()
)
ss2wgsActiveParallelThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wgsActiveParallelThreads.setStatus("current")
_Ss2wgsActiveRequests_Type = Gauge32
_Ss2wgsActiveRequests_Object = MibTableColumn
ss2wgsActiveRequests = _Ss2wgsActiveRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 39, 1, 3),
    _Ss2wgsActiveRequests_Type()
)
ss2wgsActiveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wgsActiveRequests.setStatus("current")
_Ss2wgsBlockedTasks_Type = Gauge32
_Ss2wgsBlockedTasks_Object = MibTableColumn
ss2wgsBlockedTasks = _Ss2wgsBlockedTasks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 39, 1, 4),
    _Ss2wgsBlockedTasks_Type()
)
ss2wgsBlockedTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wgsBlockedTasks.setStatus("current")
_Ss2wgsCPUUsagePercent_Type = Gauge32
_Ss2wgsCPUUsagePercent_Object = MibTableColumn
ss2wgsCPUUsagePercent = _Ss2wgsCPUUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 39, 1, 5),
    _Ss2wgsCPUUsagePercent_Type()
)
ss2wgsCPUUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wgsCPUUsagePercent.setStatus("current")
_Ss2wgsMaxRequestCpuTimeMs_Type = Gauge32
_Ss2wgsMaxRequestCpuTimeMs_Object = MibTableColumn
ss2wgsMaxRequestCpuTimeMs = _Ss2wgsMaxRequestCpuTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 39, 1, 6),
    _Ss2wgsMaxRequestCpuTimeMs_Type()
)
ss2wgsMaxRequestCpuTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wgsMaxRequestCpuTimeMs.setStatus("current")
_Ss2wgsMaxRequestMemoryGrantKB_Type = Gauge32
_Ss2wgsMaxRequestMemoryGrantKB_Object = MibTableColumn
ss2wgsMaxRequestMemoryGrantKB = _Ss2wgsMaxRequestMemoryGrantKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 39, 1, 7),
    _Ss2wgsMaxRequestMemoryGrantKB_Type()
)
ss2wgsMaxRequestMemoryGrantKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wgsMaxRequestMemoryGrantKB.setStatus("current")
_Ss2wgsQueryOptimizationsPerSec_Type = Gauge32
_Ss2wgsQueryOptimizationsPerSec_Object = MibTableColumn
ss2wgsQueryOptimizationsPerSec = _Ss2wgsQueryOptimizationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 39, 1, 8),
    _Ss2wgsQueryOptimizationsPerSec_Type()
)
ss2wgsQueryOptimizationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wgsQueryOptimizationsPerSec.setStatus("current")
_Ss2wgsQueuedRequests_Type = Gauge32
_Ss2wgsQueuedRequests_Object = MibTableColumn
ss2wgsQueuedRequests = _Ss2wgsQueuedRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 39, 1, 9),
    _Ss2wgsQueuedRequests_Type()
)
ss2wgsQueuedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wgsQueuedRequests.setStatus("current")
_Ss2wgsReducedMemoryGrantsPerSec_Type = Gauge32
_Ss2wgsReducedMemoryGrantsPerSec_Object = MibTableColumn
ss2wgsReducedMemoryGrantsPerSec = _Ss2wgsReducedMemoryGrantsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 39, 1, 10),
    _Ss2wgsReducedMemoryGrantsPerSec_Type()
)
ss2wgsReducedMemoryGrantsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wgsReducedMemoryGrantsPerSec.setStatus("current")
_Ss2wgsRequestsCompletedPerSec_Type = Gauge32
_Ss2wgsRequestsCompletedPerSec_Object = MibTableColumn
ss2wgsRequestsCompletedPerSec = _Ss2wgsRequestsCompletedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 39, 1, 11),
    _Ss2wgsRequestsCompletedPerSec_Type()
)
ss2wgsRequestsCompletedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wgsRequestsCompletedPerSec.setStatus("current")
_Ss2wgsSuboptimalPlansPerSec_Type = Gauge32
_Ss2wgsSuboptimalPlansPerSec_Object = MibTableColumn
ss2wgsSuboptimalPlansPerSec = _Ss2wgsSuboptimalPlansPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 2, 39, 1, 12),
    _Ss2wgsSuboptimalPlansPerSec_Type()
)
ss2wgsSuboptimalPlansPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss2wgsSuboptimalPlansPerSec.setStatus("current")
_SqlServerAgentV2_ObjectIdentity = ObjectIdentity
sqlServerAgentV2 = _SqlServerAgentV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3)
)
_Sa2NameTable_Object = MibTable
sa2NameTable = _Sa2NameTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    sa2NameTable.setStatus("current")
_Sa2NameEntry_Object = MibTableRow
sa2NameEntry = _Sa2NameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 1, 1)
)
sa2NameEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "sa2NameIndex"),
)
if mibBuilder.loadTexts:
    sa2NameEntry.setStatus("current")


class _Sa2NameIndex_Type(Integer32):
    """Custom type sa2NameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sa2NameIndex_Type.__name__ = "Integer32"
_Sa2NameIndex_Object = MibTableColumn
sa2NameIndex = _Sa2NameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 1, 1, 1),
    _Sa2NameIndex_Type()
)
sa2NameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2NameIndex.setStatus("current")
_Sa2NameInstance_Type = InstanceName
_Sa2NameInstance_Object = MibTableColumn
sa2NameInstance = _Sa2NameInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 1, 1, 2),
    _Sa2NameInstance_Type()
)
sa2NameInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2NameInstance.setStatus("current")
_Sa2AlertsTable_Object = MibTable
sa2AlertsTable = _Sa2AlertsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 2)
)
if mibBuilder.loadTexts:
    sa2AlertsTable.setStatus("current")
_Sa2AlertsEntry_Object = MibTableRow
sa2AlertsEntry = _Sa2AlertsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 2, 1)
)
sa2AlertsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "sa2NameIndex"),
)
if mibBuilder.loadTexts:
    sa2AlertsEntry.setStatus("current")
_Sa2AlertsActivatedAlerts_Type = Gauge32
_Sa2AlertsActivatedAlerts_Object = MibTableColumn
sa2AlertsActivatedAlerts = _Sa2AlertsActivatedAlerts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 2, 1, 1),
    _Sa2AlertsActivatedAlerts_Type()
)
sa2AlertsActivatedAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2AlertsActivatedAlerts.setStatus("current")
_Sa2AlertsAlertsActivatedMinute_Type = Gauge32
_Sa2AlertsAlertsActivatedMinute_Object = MibTableColumn
sa2AlertsAlertsActivatedMinute = _Sa2AlertsAlertsActivatedMinute_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 2, 1, 2),
    _Sa2AlertsAlertsActivatedMinute_Type()
)
sa2AlertsAlertsActivatedMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2AlertsAlertsActivatedMinute.setStatus("current")
_Sa2JobsTable_Object = MibTable
sa2JobsTable = _Sa2JobsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 3)
)
if mibBuilder.loadTexts:
    sa2JobsTable.setStatus("current")
_Sa2JobsEntry_Object = MibTableRow
sa2JobsEntry = _Sa2JobsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 3, 1)
)
sa2JobsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "sa2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "sa2JobsInstance"),
)
if mibBuilder.loadTexts:
    sa2JobsEntry.setStatus("current")
_Sa2JobsInstance_Type = InstanceName
_Sa2JobsInstance_Object = MibTableColumn
sa2JobsInstance = _Sa2JobsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 3, 1, 1),
    _Sa2JobsInstance_Type()
)
sa2JobsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2JobsInstance.setStatus("current")
_Sa2JobsActiveJobs_Type = Gauge32
_Sa2JobsActiveJobs_Object = MibTableColumn
sa2JobsActiveJobs = _Sa2JobsActiveJobs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 3, 1, 2),
    _Sa2JobsActiveJobs_Type()
)
sa2JobsActiveJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2JobsActiveJobs.setStatus("current")
_Sa2JobsFailedJobs_Type = Gauge32
_Sa2JobsFailedJobs_Object = MibTableColumn
sa2JobsFailedJobs = _Sa2JobsFailedJobs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 3, 1, 3),
    _Sa2JobsFailedJobs_Type()
)
sa2JobsFailedJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2JobsFailedJobs.setStatus("current")
_Sa2JobsJobSuccessRate_Type = Gauge32
_Sa2JobsJobSuccessRate_Object = MibTableColumn
sa2JobsJobSuccessRate = _Sa2JobsJobSuccessRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 3, 1, 4),
    _Sa2JobsJobSuccessRate_Type()
)
sa2JobsJobSuccessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2JobsJobSuccessRate.setStatus("current")
_Sa2JobsJobsActivatedPerMinute_Type = Gauge32
_Sa2JobsJobsActivatedPerMinute_Object = MibTableColumn
sa2JobsJobsActivatedPerMinute = _Sa2JobsJobsActivatedPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 3, 1, 5),
    _Sa2JobsJobsActivatedPerMinute_Type()
)
sa2JobsJobsActivatedPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2JobsJobsActivatedPerMinute.setStatus("current")
_Sa2JobsQueuedJobs_Type = Gauge32
_Sa2JobsQueuedJobs_Object = MibTableColumn
sa2JobsQueuedJobs = _Sa2JobsQueuedJobs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 3, 1, 6),
    _Sa2JobsQueuedJobs_Type()
)
sa2JobsQueuedJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2JobsQueuedJobs.setStatus("current")
_Sa2JobsSuccessfulJobs_Type = Gauge32
_Sa2JobsSuccessfulJobs_Object = MibTableColumn
sa2JobsSuccessfulJobs = _Sa2JobsSuccessfulJobs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 3, 1, 7),
    _Sa2JobsSuccessfulJobs_Type()
)
sa2JobsSuccessfulJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2JobsSuccessfulJobs.setStatus("current")
_Sa2JobStepsTable_Object = MibTable
sa2JobStepsTable = _Sa2JobStepsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 4)
)
if mibBuilder.loadTexts:
    sa2JobStepsTable.setStatus("current")
_Sa2JobStepsEntry_Object = MibTableRow
sa2JobStepsEntry = _Sa2JobStepsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 4, 1)
)
sa2JobStepsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "sa2NameIndex"),
    (0, "INFORMANT-SQLSERVER-V2", "sa2JobStepsInstance"),
)
if mibBuilder.loadTexts:
    sa2JobStepsEntry.setStatus("current")
_Sa2JobStepsInstance_Type = InstanceName
_Sa2JobStepsInstance_Object = MibTableColumn
sa2JobStepsInstance = _Sa2JobStepsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 4, 1, 1),
    _Sa2JobStepsInstance_Type()
)
sa2JobStepsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2JobStepsInstance.setStatus("current")
_Sa2JobStepsActiveSteps_Type = Gauge32
_Sa2JobStepsActiveSteps_Object = MibTableColumn
sa2JobStepsActiveSteps = _Sa2JobStepsActiveSteps_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 4, 1, 2),
    _Sa2JobStepsActiveSteps_Type()
)
sa2JobStepsActiveSteps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2JobStepsActiveSteps.setStatus("current")
_Sa2JobStepsQueuedSteps_Type = Gauge32
_Sa2JobStepsQueuedSteps_Object = MibTableColumn
sa2JobStepsQueuedSteps = _Sa2JobStepsQueuedSteps_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 4, 1, 3),
    _Sa2JobStepsQueuedSteps_Type()
)
sa2JobStepsQueuedSteps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2JobStepsQueuedSteps.setStatus("current")
_Sa2JobStepsTotalStepRetries_Type = Gauge32
_Sa2JobStepsTotalStepRetries_Object = MibTableColumn
sa2JobStepsTotalStepRetries = _Sa2JobStepsTotalStepRetries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 4, 1, 4),
    _Sa2JobStepsTotalStepRetries_Type()
)
sa2JobStepsTotalStepRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2JobStepsTotalStepRetries.setStatus("current")
_Sa2StatisticsTable_Object = MibTable
sa2StatisticsTable = _Sa2StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 5)
)
if mibBuilder.loadTexts:
    sa2StatisticsTable.setStatus("current")
_Sa2StatisticsEntry_Object = MibTableRow
sa2StatisticsEntry = _Sa2StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 5, 1)
)
sa2StatisticsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "sa2NameIndex"),
)
if mibBuilder.loadTexts:
    sa2StatisticsEntry.setStatus("current")
_Sa2StatisticsSQLServerRestarted_Type = Gauge32
_Sa2StatisticsSQLServerRestarted_Object = MibTableColumn
sa2StatisticsSQLServerRestarted = _Sa2StatisticsSQLServerRestarted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 3, 5, 1, 1),
    _Sa2StatisticsSQLServerRestarted_Type()
)
sa2StatisticsSQLServerRestarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sa2StatisticsSQLServerRestarted.setStatus("current")
_ReportingServicesV2_ObjectIdentity = ObjectIdentity
reportingServicesV2 = _ReportingServicesV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4)
)
_Rs2WebService_ObjectIdentity = ObjectIdentity
rs2WebService = _Rs2WebService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1)
)
_Rs2wbsActiveSessions_Type = Gauge32
_Rs2wbsActiveSessions_Object = MibScalar
rs2wbsActiveSessions = _Rs2wbsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 1),
    _Rs2wbsActiveSessions_Type()
)
rs2wbsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsActiveSessions.setStatus("current")
_Rs2wbsCacheHitsPerSec_Type = Gauge32
_Rs2wbsCacheHitsPerSec_Object = MibScalar
rs2wbsCacheHitsPerSec = _Rs2wbsCacheHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 2),
    _Rs2wbsCacheHitsPerSec_Type()
)
rs2wbsCacheHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsCacheHitsPerSec.setStatus("current")
_Rs2wbsCacheHitsSecSemanticModels_Type = Gauge32
_Rs2wbsCacheHitsSecSemanticModels_Object = MibScalar
rs2wbsCacheHitsSecSemanticModels = _Rs2wbsCacheHitsSecSemanticModels_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 3),
    _Rs2wbsCacheHitsSecSemanticModels_Type()
)
rs2wbsCacheHitsSecSemanticModels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsCacheHitsSecSemanticModels.setStatus("current")
_Rs2wbsCacheMissesPerSec_Type = Gauge32
_Rs2wbsCacheMissesPerSec_Object = MibScalar
rs2wbsCacheMissesPerSec = _Rs2wbsCacheMissesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 4),
    _Rs2wbsCacheMissesPerSec_Type()
)
rs2wbsCacheMissesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsCacheMissesPerSec.setStatus("current")
_Rs2wbsCacheMissesSecSemantModels_Type = Gauge32
_Rs2wbsCacheMissesSecSemantModels_Object = MibScalar
rs2wbsCacheMissesSecSemantModels = _Rs2wbsCacheMissesSecSemantModels_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 5),
    _Rs2wbsCacheMissesSecSemantModels_Type()
)
rs2wbsCacheMissesSecSemantModels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsCacheMissesSecSemantModels.setStatus("current")
_Rs2wbsFirstSessionRequestsPerSec_Type = Gauge32
_Rs2wbsFirstSessionRequestsPerSec_Object = MibScalar
rs2wbsFirstSessionRequestsPerSec = _Rs2wbsFirstSessionRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 6),
    _Rs2wbsFirstSessionRequestsPerSec_Type()
)
rs2wbsFirstSessionRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsFirstSessionRequestsPerSec.setStatus("current")
_Rs2wbsMemoryCacheHitsPerSec_Type = Gauge32
_Rs2wbsMemoryCacheHitsPerSec_Object = MibScalar
rs2wbsMemoryCacheHitsPerSec = _Rs2wbsMemoryCacheHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 7),
    _Rs2wbsMemoryCacheHitsPerSec_Type()
)
rs2wbsMemoryCacheHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsMemoryCacheHitsPerSec.setStatus("current")
_Rs2wbsMemoryCacheMissPerSec_Type = Gauge32
_Rs2wbsMemoryCacheMissPerSec_Object = MibScalar
rs2wbsMemoryCacheMissPerSec = _Rs2wbsMemoryCacheMissPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 8),
    _Rs2wbsMemoryCacheMissPerSec_Type()
)
rs2wbsMemoryCacheMissPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsMemoryCacheMissPerSec.setStatus("current")
_Rs2wbsNextSessionRequestsPerSec_Type = Gauge32
_Rs2wbsNextSessionRequestsPerSec_Object = MibScalar
rs2wbsNextSessionRequestsPerSec = _Rs2wbsNextSessionRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 9),
    _Rs2wbsNextSessionRequestsPerSec_Type()
)
rs2wbsNextSessionRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsNextSessionRequestsPerSec.setStatus("current")
_Rs2wbsReportRequests_Type = Gauge32
_Rs2wbsReportRequests_Object = MibScalar
rs2wbsReportRequests = _Rs2wbsReportRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 10),
    _Rs2wbsReportRequests_Type()
)
rs2wbsReportRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsReportRequests.setStatus("current")
_Rs2wbsReportsExecutedPerSec_Type = Gauge32
_Rs2wbsReportsExecutedPerSec_Object = MibScalar
rs2wbsReportsExecutedPerSec = _Rs2wbsReportsExecutedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 11),
    _Rs2wbsReportsExecutedPerSec_Type()
)
rs2wbsReportsExecutedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsReportsExecutedPerSec.setStatus("current")
_Rs2wbsRequestsPerSec_Type = Gauge32
_Rs2wbsRequestsPerSec_Object = MibScalar
rs2wbsRequestsPerSec = _Rs2wbsRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 12),
    _Rs2wbsRequestsPerSec_Type()
)
rs2wbsRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsRequestsPerSec.setStatus("current")
_Rs2wbsTotalCacheHits_Type = Gauge32
_Rs2wbsTotalCacheHits_Object = MibScalar
rs2wbsTotalCacheHits = _Rs2wbsTotalCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 13),
    _Rs2wbsTotalCacheHits_Type()
)
rs2wbsTotalCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsTotalCacheHits.setStatus("current")
_Rs2wbsTotalCacheHitSemanticModel_Type = Gauge32
_Rs2wbsTotalCacheHitSemanticModel_Object = MibScalar
rs2wbsTotalCacheHitSemanticModel = _Rs2wbsTotalCacheHitSemanticModel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 14),
    _Rs2wbsTotalCacheHitSemanticModel_Type()
)
rs2wbsTotalCacheHitSemanticModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsTotalCacheHitSemanticModel.setStatus("current")
_Rs2wbsTotalCacheMisses_Type = Gauge32
_Rs2wbsTotalCacheMisses_Object = MibScalar
rs2wbsTotalCacheMisses = _Rs2wbsTotalCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 15),
    _Rs2wbsTotalCacheMisses_Type()
)
rs2wbsTotalCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsTotalCacheMisses.setStatus("current")
_Rs2wbsTotalCachMissSemanticModel_Type = Gauge32
_Rs2wbsTotalCachMissSemanticModel_Object = MibScalar
rs2wbsTotalCachMissSemanticModel = _Rs2wbsTotalCachMissSemanticModel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 16),
    _Rs2wbsTotalCachMissSemanticModel_Type()
)
rs2wbsTotalCachMissSemanticModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsTotalCachMissSemanticModel.setStatus("current")
_Rs2wbsTotalMemoryCacheHits_Type = Gauge32
_Rs2wbsTotalMemoryCacheHits_Object = MibScalar
rs2wbsTotalMemoryCacheHits = _Rs2wbsTotalMemoryCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 17),
    _Rs2wbsTotalMemoryCacheHits_Type()
)
rs2wbsTotalMemoryCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsTotalMemoryCacheHits.setStatus("current")
_Rs2wbsTotalMemoryCacheMisses_Type = Gauge32
_Rs2wbsTotalMemoryCacheMisses_Object = MibScalar
rs2wbsTotalMemoryCacheMisses = _Rs2wbsTotalMemoryCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 18),
    _Rs2wbsTotalMemoryCacheMisses_Type()
)
rs2wbsTotalMemoryCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsTotalMemoryCacheMisses.setStatus("current")
_Rs2wbsTotalProcessingFailures_Type = Gauge32
_Rs2wbsTotalProcessingFailures_Object = MibScalar
rs2wbsTotalProcessingFailures = _Rs2wbsTotalProcessingFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 19),
    _Rs2wbsTotalProcessingFailures_Type()
)
rs2wbsTotalProcessingFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsTotalProcessingFailures.setStatus("current")
_Rs2wbsTotalRejectedThreads_Type = Gauge32
_Rs2wbsTotalRejectedThreads_Object = MibScalar
rs2wbsTotalRejectedThreads = _Rs2wbsTotalRejectedThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 20),
    _Rs2wbsTotalRejectedThreads_Type()
)
rs2wbsTotalRejectedThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsTotalRejectedThreads.setStatus("current")
_Rs2wbsTotalReportsExecute_Type = Gauge32
_Rs2wbsTotalReportsExecute_Object = MibScalar
rs2wbsTotalReportsExecute = _Rs2wbsTotalReportsExecute_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 21),
    _Rs2wbsTotalReportsExecute_Type()
)
rs2wbsTotalReportsExecute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsTotalReportsExecute.setStatus("current")
_Rs2wbsTotalRequests_Type = Gauge32
_Rs2wbsTotalRequests_Object = MibScalar
rs2wbsTotalRequests = _Rs2wbsTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 1, 22),
    _Rs2wbsTotalRequests_Type()
)
rs2wbsTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wbsTotalRequests.setStatus("current")
_Rs2WindowsServiceTable_Object = MibTable
rs2WindowsServiceTable = _Rs2WindowsServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2)
)
if mibBuilder.loadTexts:
    rs2WindowsServiceTable.setStatus("current")
_Rs2WindowsServiceEntry_Object = MibTableRow
rs2WindowsServiceEntry = _Rs2WindowsServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1)
)
rs2WindowsServiceEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "rs2wnsInstance"),
)
if mibBuilder.loadTexts:
    rs2WindowsServiceEntry.setStatus("current")
_Rs2wnsInstance_Type = InstanceName
_Rs2wnsInstance_Object = MibTableColumn
rs2wnsInstance = _Rs2wnsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 1),
    _Rs2wnsInstance_Type()
)
rs2wnsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsInstance.setStatus("current")
_Rs2wnsActiveSessions_Type = Gauge32
_Rs2wnsActiveSessions_Object = MibTableColumn
rs2wnsActiveSessions = _Rs2wnsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 2),
    _Rs2wnsActiveSessions_Type()
)
rs2wnsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsActiveSessions.setStatus("current")
_Rs2wnsCacheFlushesPerSec_Type = Gauge32
_Rs2wnsCacheFlushesPerSec_Object = MibTableColumn
rs2wnsCacheFlushesPerSec = _Rs2wnsCacheFlushesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 3),
    _Rs2wnsCacheFlushesPerSec_Type()
)
rs2wnsCacheFlushesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsCacheFlushesPerSec.setStatus("current")
_Rs2wnsCacheHitsPerSec_Type = Gauge32
_Rs2wnsCacheHitsPerSec_Object = MibTableColumn
rs2wnsCacheHitsPerSec = _Rs2wnsCacheHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 4),
    _Rs2wnsCacheHitsPerSec_Type()
)
rs2wnsCacheHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsCacheHitsPerSec.setStatus("current")
_Rs2wnsCacheHitsSecSemanticModels_Type = Gauge32
_Rs2wnsCacheHitsSecSemanticModels_Object = MibTableColumn
rs2wnsCacheHitsSecSemanticModels = _Rs2wnsCacheHitsSecSemanticModels_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 5),
    _Rs2wnsCacheHitsSecSemanticModels_Type()
)
rs2wnsCacheHitsSecSemanticModels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsCacheHitsSecSemanticModels.setStatus("current")
_Rs2wnsCacheMissesPerSec_Type = Gauge32
_Rs2wnsCacheMissesPerSec_Object = MibTableColumn
rs2wnsCacheMissesPerSec = _Rs2wnsCacheMissesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 6),
    _Rs2wnsCacheMissesPerSec_Type()
)
rs2wnsCacheMissesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsCacheMissesPerSec.setStatus("current")
_Rs2wnsCacheMissSecSemanticModels_Type = Gauge32
_Rs2wnsCacheMissSecSemanticModels_Object = MibTableColumn
rs2wnsCacheMissSecSemanticModels = _Rs2wnsCacheMissSecSemanticModels_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 7),
    _Rs2wnsCacheMissSecSemanticModels_Type()
)
rs2wnsCacheMissSecSemanticModels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsCacheMissSecSemanticModels.setStatus("current")
_Rs2wnsDeliversPerSec_Type = Gauge32
_Rs2wnsDeliversPerSec_Object = MibTableColumn
rs2wnsDeliversPerSec = _Rs2wnsDeliversPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 8),
    _Rs2wnsDeliversPerSec_Type()
)
rs2wnsDeliversPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsDeliversPerSec.setStatus("current")
_Rs2wnsEventsPerSec_Type = Gauge32
_Rs2wnsEventsPerSec_Object = MibTableColumn
rs2wnsEventsPerSec = _Rs2wnsEventsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 9),
    _Rs2wnsEventsPerSec_Type()
)
rs2wnsEventsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsEventsPerSec.setStatus("current")
_Rs2wnsFirstSessionRequestsPerSec_Type = Gauge32
_Rs2wnsFirstSessionRequestsPerSec_Object = MibTableColumn
rs2wnsFirstSessionRequestsPerSec = _Rs2wnsFirstSessionRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 10),
    _Rs2wnsFirstSessionRequestsPerSec_Type()
)
rs2wnsFirstSessionRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsFirstSessionRequestsPerSec.setStatus("current")
_Rs2wnsMemoryCacheHitsPerSec_Type = Gauge32
_Rs2wnsMemoryCacheHitsPerSec_Object = MibTableColumn
rs2wnsMemoryCacheHitsPerSec = _Rs2wnsMemoryCacheHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 11),
    _Rs2wnsMemoryCacheHitsPerSec_Type()
)
rs2wnsMemoryCacheHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsMemoryCacheHitsPerSec.setStatus("current")
_Rs2wnsMemoryCacheMissPerSec_Type = Gauge32
_Rs2wnsMemoryCacheMissPerSec_Object = MibTableColumn
rs2wnsMemoryCacheMissPerSec = _Rs2wnsMemoryCacheMissPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 12),
    _Rs2wnsMemoryCacheMissPerSec_Type()
)
rs2wnsMemoryCacheMissPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsMemoryCacheMissPerSec.setStatus("current")
_Rs2wnsNextSessionRequestsPerSec_Type = Gauge32
_Rs2wnsNextSessionRequestsPerSec_Object = MibTableColumn
rs2wnsNextSessionRequestsPerSec = _Rs2wnsNextSessionRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 13),
    _Rs2wnsNextSessionRequestsPerSec_Type()
)
rs2wnsNextSessionRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsNextSessionRequestsPerSec.setStatus("current")
_Rs2wnsReportRequests_Type = Gauge32
_Rs2wnsReportRequests_Object = MibTableColumn
rs2wnsReportRequests = _Rs2wnsReportRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 14),
    _Rs2wnsReportRequests_Type()
)
rs2wnsReportRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsReportRequests.setStatus("current")
_Rs2wnsReportsExecutedPerSec_Type = Gauge32
_Rs2wnsReportsExecutedPerSec_Object = MibTableColumn
rs2wnsReportsExecutedPerSec = _Rs2wnsReportsExecutedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 15),
    _Rs2wnsReportsExecutedPerSec_Type()
)
rs2wnsReportsExecutedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsReportsExecutedPerSec.setStatus("current")
_Rs2wnsRequestsPerSec_Type = Gauge32
_Rs2wnsRequestsPerSec_Object = MibTableColumn
rs2wnsRequestsPerSec = _Rs2wnsRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 16),
    _Rs2wnsRequestsPerSec_Type()
)
rs2wnsRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsRequestsPerSec.setStatus("current")
_Rs2wnsSnapshotUpdatesPerSec_Type = Gauge32
_Rs2wnsSnapshotUpdatesPerSec_Object = MibTableColumn
rs2wnsSnapshotUpdatesPerSec = _Rs2wnsSnapshotUpdatesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 17),
    _Rs2wnsSnapshotUpdatesPerSec_Type()
)
rs2wnsSnapshotUpdatesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsSnapshotUpdatesPerSec.setStatus("current")
_Rs2wnsTotalAppDomainRecycles_Type = Gauge32
_Rs2wnsTotalAppDomainRecycles_Object = MibTableColumn
rs2wnsTotalAppDomainRecycles = _Rs2wnsTotalAppDomainRecycles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 18),
    _Rs2wnsTotalAppDomainRecycles_Type()
)
rs2wnsTotalAppDomainRecycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalAppDomainRecycles.setStatus("current")
_Rs2wnsTotalCacheFlushes_Type = Gauge32
_Rs2wnsTotalCacheFlushes_Object = MibTableColumn
rs2wnsTotalCacheFlushes = _Rs2wnsTotalCacheFlushes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 19),
    _Rs2wnsTotalCacheFlushes_Type()
)
rs2wnsTotalCacheFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalCacheFlushes.setStatus("current")
_Rs2wnsTotalCacheHits_Type = Gauge32
_Rs2wnsTotalCacheHits_Object = MibTableColumn
rs2wnsTotalCacheHits = _Rs2wnsTotalCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 20),
    _Rs2wnsTotalCacheHits_Type()
)
rs2wnsTotalCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalCacheHits.setStatus("current")
_Rs2wnsTotalCacheHitSemanticModel_Type = Gauge32
_Rs2wnsTotalCacheHitSemanticModel_Object = MibTableColumn
rs2wnsTotalCacheHitSemanticModel = _Rs2wnsTotalCacheHitSemanticModel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 21),
    _Rs2wnsTotalCacheHitSemanticModel_Type()
)
rs2wnsTotalCacheHitSemanticModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalCacheHitSemanticModel.setStatus("current")
_Rs2wnsTotalCacheMisses_Type = Gauge32
_Rs2wnsTotalCacheMisses_Object = MibTableColumn
rs2wnsTotalCacheMisses = _Rs2wnsTotalCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 22),
    _Rs2wnsTotalCacheMisses_Type()
)
rs2wnsTotalCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalCacheMisses.setStatus("current")
_Rs2wnsTotalCachMissSemanticModel_Type = Gauge32
_Rs2wnsTotalCachMissSemanticModel_Object = MibTableColumn
rs2wnsTotalCachMissSemanticModel = _Rs2wnsTotalCachMissSemanticModel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 23),
    _Rs2wnsTotalCachMissSemanticModel_Type()
)
rs2wnsTotalCachMissSemanticModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalCachMissSemanticModel.setStatus("current")
_Rs2wnsTotalDeliveries_Type = Gauge32
_Rs2wnsTotalDeliveries_Object = MibTableColumn
rs2wnsTotalDeliveries = _Rs2wnsTotalDeliveries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 24),
    _Rs2wnsTotalDeliveries_Type()
)
rs2wnsTotalDeliveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalDeliveries.setStatus("current")
_Rs2wnsTotalEvents_Type = Gauge32
_Rs2wnsTotalEvents_Object = MibTableColumn
rs2wnsTotalEvents = _Rs2wnsTotalEvents_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 25),
    _Rs2wnsTotalEvents_Type()
)
rs2wnsTotalEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalEvents.setStatus("current")
_Rs2wnsTotalMemoryCacheHits_Type = Gauge32
_Rs2wnsTotalMemoryCacheHits_Object = MibTableColumn
rs2wnsTotalMemoryCacheHits = _Rs2wnsTotalMemoryCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 26),
    _Rs2wnsTotalMemoryCacheHits_Type()
)
rs2wnsTotalMemoryCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalMemoryCacheHits.setStatus("current")
_Rs2wnsTotalMemoryCacheMisses_Type = Gauge32
_Rs2wnsTotalMemoryCacheMisses_Object = MibTableColumn
rs2wnsTotalMemoryCacheMisses = _Rs2wnsTotalMemoryCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 27),
    _Rs2wnsTotalMemoryCacheMisses_Type()
)
rs2wnsTotalMemoryCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalMemoryCacheMisses.setStatus("current")
_Rs2wnsTotalProcessingFailures_Type = Gauge32
_Rs2wnsTotalProcessingFailures_Object = MibTableColumn
rs2wnsTotalProcessingFailures = _Rs2wnsTotalProcessingFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 28),
    _Rs2wnsTotalProcessingFailures_Type()
)
rs2wnsTotalProcessingFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalProcessingFailures.setStatus("current")
_Rs2wnsTotalRejectedThreads_Type = Gauge32
_Rs2wnsTotalRejectedThreads_Object = MibTableColumn
rs2wnsTotalRejectedThreads = _Rs2wnsTotalRejectedThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 29),
    _Rs2wnsTotalRejectedThreads_Type()
)
rs2wnsTotalRejectedThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalRejectedThreads.setStatus("current")
_Rs2wnsTotalReportsExecuted_Type = Gauge32
_Rs2wnsTotalReportsExecuted_Object = MibTableColumn
rs2wnsTotalReportsExecuted = _Rs2wnsTotalReportsExecuted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 30),
    _Rs2wnsTotalReportsExecuted_Type()
)
rs2wnsTotalReportsExecuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalReportsExecuted.setStatus("current")
_Rs2wnsTotalRequests_Type = Gauge32
_Rs2wnsTotalRequests_Object = MibTableColumn
rs2wnsTotalRequests = _Rs2wnsTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 31),
    _Rs2wnsTotalRequests_Type()
)
rs2wnsTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalRequests.setStatus("current")
_Rs2wnsTotalSnapshotUpdates_Type = Gauge32
_Rs2wnsTotalSnapshotUpdates_Object = MibTableColumn
rs2wnsTotalSnapshotUpdates = _Rs2wnsTotalSnapshotUpdates_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 2, 1, 32),
    _Rs2wnsTotalSnapshotUpdates_Type()
)
rs2wnsTotalSnapshotUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2wnsTotalSnapshotUpdates.setStatus("current")
_Rs2ReportServerHTTPTable_Object = MibTable
rs2ReportServerHTTPTable = _Rs2ReportServerHTTPTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 3)
)
if mibBuilder.loadTexts:
    rs2ReportServerHTTPTable.setStatus("current")
_Rs2ReportServerHTTPEntry_Object = MibTableRow
rs2ReportServerHTTPEntry = _Rs2ReportServerHTTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 3, 1)
)
rs2ReportServerHTTPEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER-V2", "rs2HTTPNameIndex"),
)
if mibBuilder.loadTexts:
    rs2ReportServerHTTPEntry.setStatus("current")


class _Rs2HTTPNameIndex_Type(Integer32):
    """Custom type rs2HTTPNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Rs2HTTPNameIndex_Type.__name__ = "Integer32"
_Rs2HTTPNameIndex_Object = MibTableColumn
rs2HTTPNameIndex = _Rs2HTTPNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 3, 1, 1),
    _Rs2HTTPNameIndex_Type()
)
rs2HTTPNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2HTTPNameIndex.setStatus("current")
_Rs2HTTPNameInstance_Type = InstanceName
_Rs2HTTPNameInstance_Object = MibTableColumn
rs2HTTPNameInstance = _Rs2HTTPNameInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 3, 1, 2),
    _Rs2HTTPNameInstance_Type()
)
rs2HTTPNameInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2HTTPNameInstance.setStatus("current")
_Rs2HTTPRequestsPerSec_Type = Gauge32
_Rs2HTTPRequestsPerSec_Object = MibTableColumn
rs2HTTPRequestsPerSec = _Rs2HTTPRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 3, 1, 3),
    _Rs2HTTPRequestsPerSec_Type()
)
rs2HTTPRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2HTTPRequestsPerSec.setStatus("current")
_Rs2HTTPTotalRequests_Type = Gauge32
_Rs2HTTPTotalRequests_Object = MibTableColumn
rs2HTTPTotalRequests = _Rs2HTTPTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 13, 4, 3, 1, 4),
    _Rs2HTTPTotalRequests_Type()
)
rs2HTTPTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs2HTTPTotalRequests.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFORMANT-SQLSERVER-V2",
    **{"sqlServerV2": sqlServerV2,
       "analysisServicesV2": analysisServicesV2,
       "as2NameTable": as2NameTable,
       "as2NameEntry": as2NameEntry,
       "as2NameIndex": as2NameIndex,
       "as2NameInstance": as2NameInstance,
       "as2CacheTable": as2CacheTable,
       "as2CacheEntry": as2CacheEntry,
       "as2CacheCurrentKB": as2CacheCurrentKB,
       "as2CacheCurrentEntries": as2CacheCurrentEntries,
       "as2CacheDirectHitRatio": as2CacheDirectHitRatio,
       "as2CacheDirectHitsPerSec": as2CacheDirectHitsPerSec,
       "as2CacheEvictionsPerSec": as2CacheEvictionsPerSec,
       "as2CacheInsertsPerSec": as2CacheInsertsPerSec,
       "as2CacheKBAddedPerSec": as2CacheKBAddedPerSec,
       "as2CacheLookupsPerSec": as2CacheLookupsPerSec,
       "as2CacheMissesPerSec": as2CacheMissesPerSec,
       "as2CacheTotalDirectHits": as2CacheTotalDirectHits,
       "as2CacheTotalEvictions": as2CacheTotalEvictions,
       "as2CacheTotalFiltIteratorCachHit": as2CacheTotalFiltIteratorCachHit,
       "as2CacheTotalFiltIteratorCachMis": as2CacheTotalFiltIteratorCachMis,
       "as2CacheTotalInserts": as2CacheTotalInserts,
       "as2CacheTotalLookups": as2CacheTotalLookups,
       "as2CacheTotalMisses": as2CacheTotalMisses,
       "as2ConnectionTable": as2ConnectionTable,
       "as2ConnectionEntry": as2ConnectionEntry,
       "as2ConnectionCurrentConnections": as2ConnectionCurrentConnections,
       "as2ConnectionCurrentUserSessions": as2ConnectionCurrentUserSessions,
       "as2ConnectionFailuresPerSec": as2ConnectionFailuresPerSec,
       "as2ConnectionRequestsPerSec": as2ConnectionRequestsPerSec,
       "as2ConnectionSuccessesPerSec": as2ConnectionSuccessesPerSec,
       "as2ConnectionTotalFailures": as2ConnectionTotalFailures,
       "as2ConnectionTotalRequests": as2ConnectionTotalRequests,
       "as2ConnectionTotalSuccesses": as2ConnectionTotalSuccesses,
       "as2DataMiningModelProcessTable": as2DataMiningModelProcessTable,
       "as2DataMiningModelProcessEntry": as2DataMiningModelProcessEntry,
       "as2dmmpCasesPerSec": as2dmmpCasesPerSec,
       "as2dmmpCurrentModelsProcessing": as2dmmpCurrentModelsProcessing,
       "as2DataMiningPredictionTable": as2DataMiningPredictionTable,
       "as2DataMiningPredictionEntry": as2DataMiningPredictionEntry,
       "as2dmpConcurrentDMQueries": as2dmpConcurrentDMQueries,
       "as2dmpPredictionsPerSec": as2dmpPredictionsPerSec,
       "as2dmpQueriesPerSec": as2dmpQueriesPerSec,
       "as2dmpRowsPerSec": as2dmpRowsPerSec,
       "as2dmpTotalPredictions": as2dmpTotalPredictions,
       "as2dmpTotalQueries": as2dmpTotalQueries,
       "as2dmpTotalRows": as2dmpTotalRows,
       "as2LocksTable": as2LocksTable,
       "as2LocksEntry": as2LocksEntry,
       "as2LocksCurrentLatchWaits": as2LocksCurrentLatchWaits,
       "as2LocksCurrentLockWaits": as2LocksCurrentLockWaits,
       "as2LocksCurrentLocks": as2LocksCurrentLocks,
       "as2LocksLatchWaitsPerSec": as2LocksLatchWaitsPerSec,
       "as2LocksLockDenialsPerSec": as2LocksLockDenialsPerSec,
       "as2LocksLockGrantsPerSec": as2LocksLockGrantsPerSec,
       "as2LocksLockRequestsPerSec": as2LocksLockRequestsPerSec,
       "as2LocksLockWaitsPerSec": as2LocksLockWaitsPerSec,
       "as2LocksTotalDeadlocksDetected": as2LocksTotalDeadlocksDetected,
       "as2LocksUnlockRequestsPerSec": as2LocksUnlockRequestsPerSec,
       "as2MDXTable": as2MDXTable,
       "as2MDXEntry": as2MDXEntry,
       "as2MDXCurrentNumOfCachedEvalNode": as2MDXCurrentNumOfCachedEvalNode,
       "as2MDXCurrentNumOfEvalNode": as2MDXCurrentNumOfEvalNode,
       "as2MDXNumOfStorageEngineEvalNode": as2MDXNumOfStorageEngineEvalNode,
       "as2MDXNumOfBulkModeEvalNode": as2MDXNumOfBulkModeEvalNode,
       "as2MDXNumOfCachedotherEvalNode": as2MDXNumOfCachedotherEvalNode,
       "as2MDXNumCacheStorEngineEvalNode": as2MDXNumCacheStorEngineEvalNode,
       "as2MDXNumOfCacheBulkModeEvalNode": as2MDXNumOfCacheBulkModeEvalNode,
       "as2MDXNumberOfCalculationCovers": as2MDXNumberOfCalculationCovers,
       "as2MDXNumOfCellByCellEvalNode": as2MDXNumOfCellByCellEvalNode,
       "as2MDXNumCellCellHitCacheEvalNod": as2MDXNumCellCellHitCacheEvalNod,
       "as2MDXNumCellCellMissCachEvalNod": as2MDXNumCellCellMissCachEvalNod,
       "as2MDXNumEvalNodThatCovASglCell": as2MDXNumEvalNodThatCovASglCell,
       "as2MDXNumEvalNodeCalcSameGranula": as2MDXNumEvalNodeCalcSameGranula,
       "as2MDXNumEvictionsEvalNode": as2MDXNumEvictionsEvalNode,
       "as2MDXNumHashdexHitsCacheEvalNod": as2MDXNumHashdexHitsCacheEvalNod,
       "as2MDXNumSubcubeHitsCacheEvalNod": as2MDXNumSubcubeHitsCacheEvalNod,
       "as2MDXNumSubcubeMissCacheEvalNod": as2MDXNumSubcubeMissCacheEvalNod,
       "as2MDXTotalAutoexist": as2MDXTotalAutoexist,
       "as2MDXTotalEXISTING": as2MDXTotalEXISTING,
       "as2MDXTotalNONEMPTY": as2MDXTotalNONEMPTY,
       "as2MDXTotalNONEMPTYCalculatMemb": as2MDXTotalNONEMPTYCalculatMemb,
       "as2MDXTotalNONEMPTYUnoptimized": as2MDXTotalNONEMPTYUnoptimized,
       "as2MDXTotalSonarSubcubes": as2MDXTotalSonarSubcubes,
       "as2MDXTotalCellsCalculated": as2MDXTotalCellsCalculated,
       "as2MDXTotalFlatCacheInserts": as2MDXTotalFlatCacheInserts,
       "as2MDXTotalRecomputes": as2MDXTotalRecomputes,
       "as2MemoryTable": as2MemoryTable,
       "as2MemoryEntry": as2MemoryEntry,
       "as2memAggCacheKB": as2memAggCacheKB,
       "as2memAggregationMapFiles": as2memAggregationMapFiles,
       "as2memCleanerBalancePerSec": as2memCleanerBalancePerSec,
       "as2memCleanerCurrentPrice": as2memCleanerCurrentPrice,
       "as2memCleanerMemoryKB": as2memCleanerMemoryKB,
       "as2memCleanerMemNonshrinkableKB": as2memCleanerMemNonshrinkableKB,
       "as2memCleanerMemoryShrinkableKB": as2memCleanerMemoryShrinkableKB,
       "as2memCleanerMemShrunkKBSec": as2memCleanerMemShrunkKBSec,
       "as2memDimensionIndexHashFiles": as2memDimensionIndexHashFiles,
       "as2memDimensionPropertyFiles": as2memDimensionPropertyFiles,
       "as2memDimensionStringFiles": as2memDimensionStringFiles,
       "as2memFactAggregationFiles": as2memFactAggregationFiles,
       "as2memFactDataFiles": as2memFactDataFiles,
       "as2memFactStringFiles": as2memFactStringFiles,
       "as2memFilestoreClockPgExamineSec": as2memFilestoreClockPgExamineSec,
       "as2memFilestoreClockPgHaveRefSec": as2memFilestoreClockPgHaveRefSec,
       "as2memFilestoreClockPgValidSec": as2memFilestoreClockPgValidSec,
       "as2memFilestoreIOErrors": as2memFilestoreIOErrors,
       "as2memFilestoreIOErrorsPerSec": as2memFilestoreIOErrorsPerSec,
       "as2memFilestoreKB": as2memFilestoreKB,
       "as2memFilestoreKBReadsPerSec": as2memFilestoreKBReadsPerSec,
       "as2memFilestoreKBWritePerSec": as2memFilestoreKBWritePerSec,
       "as2memFilestoreMemoryPinnedKB": as2memFilestoreMemoryPinnedKB,
       "as2memFilestorePageFaultsPerSec": as2memFilestorePageFaultsPerSec,
       "as2memFilestoreReadsPerSec": as2memFilestoreReadsPerSec,
       "as2memFilestoreWritesPerSec": as2memFilestoreWritesPerSec,
       "as2memInMemAggregationMapFileKB": as2memInMemAggregationMapFileKB,
       "as2memInMemAggregateMapFileKBSec": as2memInMemAggregateMapFileKBSec,
       "as2memInMemDimenIndexHashFileKB": as2memInMemDimenIndexHashFileKB,
       "as2memInMemDimenIndHashFileKBSec": as2memInMemDimenIndHashFileKBSec,
       "as2memInMemDimenProtyFileKB": as2memInMemDimenProtyFileKB,
       "as2memInMemDimenProtyFileKBSec": as2memInMemDimenProtyFileKBSec,
       "as2memInMemDimenStringFileKB": as2memInMemDimenStringFileKB,
       "as2memInMemDimenStringFileKBSec": as2memInMemDimenStringFileKBSec,
       "as2memInMemFactAggregationFileKB": as2memInMemFactAggregationFileKB,
       "as2memInMemFactAggregatFileKBSec": as2memInMemFactAggregatFileKBSec,
       "as2memInMemoryFactDataFileKB": as2memInMemoryFactDataFileKB,
       "as2memInMemFactDataFileKBSec": as2memInMemFactDataFileKBSec,
       "as2memInMemoryFactStringFileKB": as2memInMemoryFactStringFileKB,
       "as2memInMemFactStringFileKBSec": as2memInMemFactStringFileKBSec,
       "as2memInMemoryMapFileKB": as2memInMemoryMapFileKB,
       "as2memInMemoryMapFileKBPerSec": as2memInMemoryMapFileKBPerSec,
       "as2memInMemoryOtherFileKB": as2memInMemoryOtherFileKB,
       "as2memInMemoryOtherFileKBPerSec": as2memInMemoryOtherFileKBPerSec,
       "as2memMapFiles": as2memMapFiles,
       "as2memMemoryLimitHighKB": as2memMemoryLimitHighKB,
       "as2memMemoryLimitLowKB": as2memMemoryLimitLowKB,
       "as2memMemoryUsageKB": as2memMemoryUsageKB,
       "as2memOtherFiles": as2memOtherFiles,
       "as2memPagePool1AllocKB": as2memPagePool1AllocKB,
       "as2memPagePool1LookasideKB": as2memPagePool1LookasideKB,
       "as2memPagePool64AllocKB": as2memPagePool64AllocKB,
       "as2memPagePool64LookasideKB": as2memPagePool64LookasideKB,
       "as2memPagePool8AllocKB": as2memPagePool8AllocKB,
       "as2memPagePool8LookasideKB": as2memPagePool8LookasideKB,
       "as2memPotenMemAggregatMapFileKB": as2memPotenMemAggregatMapFileKB,
       "as2memPotenMemDimenIndHashFilKB": as2memPotenMemDimenIndHashFilKB,
       "as2memPotenMemDimenProFileKB": as2memPotenMemDimenProFileKB,
       "as2memPotenMemDimenStringFileKB": as2memPotenMemDimenStringFileKB,
       "as2memPotenMemFactAggregFileKB": as2memPotenMemFactAggregFileKB,
       "as2memPotenMemFactDataFileKB": as2memPotenMemFactDataFileKB,
       "as2memPotenMemFactStringFileKB": as2memPotenMemFactStringFileKB,
       "as2memPotentialInMemoryMapFileKB": as2memPotentialInMemoryMapFileKB,
       "as2memPotenMemOtherFileKB": as2memPotenMemOtherFileKB,
       "as2memQuotaBlocked": as2memQuotaBlocked,
       "as2memQuotaKB": as2memQuotaKB,
       "as2ProactiveCachingTable": as2ProactiveCachingTable,
       "as2ProactiveCachingEntry": as2ProactiveCachingEntry,
       "as2pcNotificationsPerSec": as2pcNotificationsPerSec,
       "as2pcProactiveCachingBeginPerSec": as2pcProactiveCachingBeginPerSec,
       "as2pcProactiveCachCompSec": as2pcProactiveCachCompSec,
       "as2pcProcessCancellationsSec": as2pcProcessCancellationsSec,
       "as2ProcAggregationsTable": as2ProcAggregationsTable,
       "as2ProcAggregationsEntry": as2ProcAggregationsEntry,
       "as2paCurrentPartitions": as2paCurrentPartitions,
       "as2paMemorySizeBytes": as2paMemorySizeBytes,
       "as2paMemorySizeRows": as2paMemorySizeRows,
       "as2paRowsCreatedPerSec": as2paRowsCreatedPerSec,
       "as2paRowsMergedPerSec": as2paRowsMergedPerSec,
       "as2paTempFileBytesWrittenPerSec": as2paTempFileBytesWrittenPerSec,
       "as2paTempFileRowsWrittenPerSec": as2paTempFileRowsWrittenPerSec,
       "as2paTotalPartitions": as2paTotalPartitions,
       "as2ProcIndexesTable": as2ProcIndexesTable,
       "as2ProcIndexesEntry": as2ProcIndexesEntry,
       "as2ProcIndexesCurrentPartitions": as2ProcIndexesCurrentPartitions,
       "as2ProcIndexesRowsPerSec": as2ProcIndexesRowsPerSec,
       "as2ProcIndexesTotalPartitions": as2ProcIndexesTotalPartitions,
       "as2ProcIndexesTotalRows": as2ProcIndexesTotalRows,
       "as2ProcessingTable": as2ProcessingTable,
       "as2ProcessingEntry": as2ProcessingEntry,
       "as2ProcessingRowsConvertedPerSec": as2ProcessingRowsConvertedPerSec,
       "as2ProcessingRowsReadPerSec": as2ProcessingRowsReadPerSec,
       "as2ProcessingRowsWrittenPerSec": as2ProcessingRowsWrittenPerSec,
       "as2ProcessingTotalRowsConverted": as2ProcessingTotalRowsConverted,
       "as2ProcessingTotalRowsRead": as2ProcessingTotalRowsRead,
       "as2ProcessingTotalRowsWritten": as2ProcessingTotalRowsWritten,
       "as2StorageEngineQueryTable": as2StorageEngineQueryTable,
       "as2StorageEngineQueryEntry": as2StorageEngineQueryEntry,
       "as2seqAggregationHitsPerSec": as2seqAggregationHitsPerSec,
       "as2seqAggregationLookupsPerSec": as2seqAggregationLookupsPerSec,
       "as2seqAvgTimePerQuery": as2seqAvgTimePerQuery,
       "as2seqBytesSentPerSec": as2seqBytesSentPerSec,
       "as2seqCalculationCacheHitsPerSec": as2seqCalculationCacheHitsPerSec,
       "as2seqCalculationCacheLookupsSec": as2seqCalculationCacheLookupsSec,
       "as2seqCurrentDimensionQueries": as2seqCurrentDimensionQueries,
       "as2seqCurrentMeasureGroupQueries": as2seqCurrentMeasureGroupQueries,
       "as2seqDataBytesPerSec": as2seqDataBytesPerSec,
       "as2seqDataReadsPerSec": as2seqDataReadsPerSec,
       "as2seqDimensionCacheHitsPerSec": as2seqDimensionCacheHitsPerSec,
       "as2seqDimensionCacheLookupSec": as2seqDimensionCacheLookupSec,
       "as2seqDimensionQueriesPerSec": as2seqDimensionQueriesPerSec,
       "as2seqFlatCacheHitsPerSec": as2seqFlatCacheHitsPerSec,
       "as2seqFlatCacheLookupsPerSec": as2seqFlatCacheLookupsPerSec,
       "as2seqMapBytesPerSec": as2seqMapBytesPerSec,
       "as2seqMapReadsPerSec": as2seqMapReadsPerSec,
       "as2seqMeasureGroupCacheHitsSec": as2seqMeasureGroupCacheHitsSec,
       "as2seqMeasureGroupCacheLookupSec": as2seqMeasureGroupCacheLookupSec,
       "as2seqMeasureGroupQueriesPerSec": as2seqMeasureGroupQueriesPerSec,
       "as2seqNetworkRoundTripsPerSec": as2seqNetworkRoundTripsPerSec,
       "as2seqPersistedCacheHitsPerSec": as2seqPersistedCacheHitsPerSec,
       "as2seqsistedCacheLookupsSec": as2seqsistedCacheLookupsSec,
       "as2seqQueriesAnsweredPerSec": as2seqQueriesAnsweredPerSec,
       "as2seqQueryFromCacheDirectSec": as2seqQueryFromCacheDirectSec,
       "as2seqQueryFromCacheFilteredSec": as2seqQueryFromCacheFilteredSec,
       "as2seqQueriesFromFilePerSec": as2seqQueriesFromFilePerSec,
       "as2seqRowsSentPerSec": as2seqRowsSentPerSec,
       "as2seqTotalBytesSent": as2seqTotalBytesSent,
       "as2seqTotalDimensionQueries": as2seqTotalDimensionQueries,
       "as2seqTotalMeasureGroupQueries": as2seqTotalMeasureGroupQueries,
       "as2seqTotalNetworkRoundTrips": as2seqTotalNetworkRoundTrips,
       "as2seqTotalQueriesAnswered": as2seqTotalQueriesAnswered,
       "as2seqTotalQueryFromCacheDirect": as2seqTotalQueryFromCacheDirect,
       "as2seqTotalQueryFromCachFiltered": as2seqTotalQueryFromCachFiltered,
       "as2seqTotalQueriesFromFile": as2seqTotalQueriesFromFile,
       "as2seqTotalRowsSent": as2seqTotalRowsSent,
       "as2ThreadsTable": as2ThreadsTable,
       "as2ThreadsEntry": as2ThreadsEntry,
       "as2ThdsLongParsingBusyThreads": as2ThdsLongParsingBusyThreads,
       "as2ThdsLongParsingIdleThreads": as2ThdsLongParsingIdleThreads,
       "as2ThdsLongParsingJobQueueLength": as2ThdsLongParsingJobQueueLength,
       "as2ThdsLongParsingJobRate": as2ThdsLongParsingJobRate,
       "as2ThdsProcessingPoolBusyThreads": as2ThdsProcessingPoolBusyThreads,
       "as2ThdsProcessingPoolIdleThreads": as2ThdsProcessingPoolIdleThreads,
       "as2ThdsProcessPoolJobQueueLength": as2ThdsProcessPoolJobQueueLength,
       "as2ThdsProcessingPoolJobRate": as2ThdsProcessingPoolJobRate,
       "as2ThdsQueryPoolBusyThreads": as2ThdsQueryPoolBusyThreads,
       "as2ThdsQueryPoolIdleThreads": as2ThdsQueryPoolIdleThreads,
       "as2ThdsQueryPoolJobQueueLength": as2ThdsQueryPoolJobQueueLength,
       "as2ThdsQueryPoolJobRate": as2ThdsQueryPoolJobRate,
       "as2ThdsShortParsingBusyThreads": as2ThdsShortParsingBusyThreads,
       "as2ThdsShortParsingIdleThreads": as2ThdsShortParsingIdleThreads,
       "as2ThdsShortParsingJobQueueLeng": as2ThdsShortParsingJobQueueLeng,
       "as2ThdsShortParsingJobRate": as2ThdsShortParsingJobRate,
       "sqlServerEngineV2": sqlServerEngineV2,
       "ss2NameTable": ss2NameTable,
       "ss2NameEntry": ss2NameEntry,
       "ss2NameIndex": ss2NameIndex,
       "ss2NameInstance": ss2NameInstance,
       "ss2AccessMethodsTable": ss2AccessMethodsTable,
       "ss2AccessMethodsEntry": ss2AccessMethodsEntry,
       "ss2amAUCleanupBatchesPerSec": ss2amAUCleanupBatchesPerSec,
       "ss2amAUCleanupsPerSec": ss2amAUCleanupsPerSec,
       "ss2amByReferenceLobCreateCount": ss2amByReferenceLobCreateCount,
       "ss2amByReferenceLobUseCount": ss2amByReferenceLobUseCount,
       "ss2amCountLobReadahead": ss2amCountLobReadahead,
       "ss2amCountPullInRow": ss2amCountPullInRow,
       "ss2amCountPushOffRow": ss2amCountPushOffRow,
       "ss2amDeferredDroppedRowsets": ss2amDeferredDroppedRowsets,
       "ss2amDeferredDroppedAUs": ss2amDeferredDroppedAUs,
       "ss2amDroppedRowsetCleanupsPerSec": ss2amDroppedRowsetCleanupsPerSec,
       "ss2amDroppedRowsetsSkippedPerSec": ss2amDroppedRowsetsSkippedPerSec,
       "ss2amExtentDeallocationsPerSec": ss2amExtentDeallocationsPerSec,
       "ss2amExtentsAllocatedPerSec": ss2amExtentsAllocatedPerSec,
       "ss2amFailedAUCleanupBatchesSec": ss2amFailedAUCleanupBatchesSec,
       "ss2amFailedLeafPageCookie": ss2amFailedLeafPageCookie,
       "ss2amFailedTreePageCookie": ss2amFailedTreePageCookie,
       "ss2amForwardedRecordsPerSec": ss2amForwardedRecordsPerSec,
       "ss2amFreeSpacePageFetchesPerSec": ss2amFreeSpacePageFetchesPerSec,
       "ss2amFreeSpaceScansPerSec": ss2amFreeSpaceScansPerSec,
       "ss2amFullScansPerSec": ss2amFullScansPerSec,
       "ss2amIndexSearchesPerSec": ss2amIndexSearchesPerSec,
       "ss2amLobHandleCreateCount": ss2amLobHandleCreateCount,
       "ss2amLobHandleDestroyCount": ss2amLobHandleDestroyCount,
       "ss2amLobSSProviderCreateCount": ss2amLobSSProviderCreateCount,
       "ss2amLobSSProviderDestroyCount": ss2amLobSSProviderDestroyCount,
       "ss2amLobSSProvideTruncationCount": ss2amLobSSProvideTruncationCount,
       "ss2amMixedPageAllocationsPerSec": ss2amMixedPageAllocationsPerSec,
       "ss2amPageDeallocationsPerSec": ss2amPageDeallocationsPerSec,
       "ss2amPageSplitsPerSec": ss2amPageSplitsPerSec,
       "ss2amPageCompressionAttemptsSec": ss2amPageCompressionAttemptsSec,
       "ss2amPagesAllocatedPerSec": ss2amPagesAllocatedPerSec,
       "ss2amPagesCompressedPerSec": ss2amPagesCompressedPerSec,
       "ss2amProbeScansPerSec": ss2amProbeScansPerSec,
       "ss2amRangeScansPerSec": ss2amRangeScansPerSec,
       "ss2amScanPointRevalidationsSec": ss2amScanPointRevalidationsSec,
       "ss2amSkippedGhostedRecordsPerSec": ss2amSkippedGhostedRecordsPerSec,
       "ss2amTableLockEscalationsPerSec": ss2amTableLockEscalationsPerSec,
       "ss2amUsedLeafPageCookie": ss2amUsedLeafPageCookie,
       "ss2amUsedTreePageCookie": ss2amUsedTreePageCookie,
       "ss2amWorkfilesCreatedPerSec": ss2amWorkfilesCreatedPerSec,
       "ss2amWorktablesCreatedPerSec": ss2amWorktablesCreatedPerSec,
       "ss2amWorktablesFromCacheRatio": ss2amWorktablesFromCacheRatio,
       "ss2BackupDeviceTable": ss2BackupDeviceTable,
       "ss2BackupDeviceEntry": ss2BackupDeviceEntry,
       "ss2BackupDeviceInstance": ss2BackupDeviceInstance,
       "ss2BackupDeviceDeviceputBytesSec": ss2BackupDeviceDeviceputBytesSec,
       "ss2BrokerActivationTable": ss2BrokerActivationTable,
       "ss2BrokerActivationEntry": ss2BrokerActivationEntry,
       "ss2baInstance": ss2baInstance,
       "ss2baStoredProceduresInvokedSec": ss2baStoredProceduresInvokedSec,
       "ss2baTaskLimitReached": ss2baTaskLimitReached,
       "ss2baTaskLimitReachedPerSec": ss2baTaskLimitReachedPerSec,
       "ss2baTasksAbortedPerSec": ss2baTasksAbortedPerSec,
       "ss2baTasksRunning": ss2baTasksRunning,
       "ss2baTasksStartedPerSec": ss2baTasksStartedPerSec,
       "ss2BrokerStatisticsTable": ss2BrokerStatisticsTable,
       "ss2BrokerStatisticsEntry": ss2BrokerStatisticsEntry,
       "ss2bsActivationErrorsTotal": ss2bsActivationErrorsTotal,
       "ss2bsBrokerTransactionRollbacks": ss2bsBrokerTransactionRollbacks,
       "ss2bsCorruptedMessagesTotal": ss2bsCorruptedMessagesTotal,
       "ss2bsDequeuedTransmissionQMsgSec": ss2bsDequeuedTransmissionQMsgSec,
       "ss2bsDialogTimerEventCount": ss2bsDialogTimerEventCount,
       "ss2bsDroppedMessagesTotal": ss2bsDroppedMessagesTotal,
       "ss2bsEnqueuedLocalMessagesTotal": ss2bsEnqueuedLocalMessagesTotal,
       "ss2bsEnqueuedLocalMessagesPerSec": ss2bsEnqueuedLocalMessagesPerSec,
       "ss2bsEnqueuedMessagesTotal": ss2bsEnqueuedMessagesTotal,
       "ss2bsEnqueuedMessagesPerSec": ss2bsEnqueuedMessagesPerSec,
       "ss2bsEnqueuedP1MessagesPerSec": ss2bsEnqueuedP1MessagesPerSec,
       "ss2bsEnqueuedP10MessagesPerSec": ss2bsEnqueuedP10MessagesPerSec,
       "ss2bsEnqueuedP2MessagesPerSec": ss2bsEnqueuedP2MessagesPerSec,
       "ss2bsEnqueuedP3MessagesPerSec": ss2bsEnqueuedP3MessagesPerSec,
       "ss2bsEnqueuedP4MessagesPerSec": ss2bsEnqueuedP4MessagesPerSec,
       "ss2bsEnqueuedP5MessagesPerSec": ss2bsEnqueuedP5MessagesPerSec,
       "ss2bsEnqueuedP6MessagesPerSec": ss2bsEnqueuedP6MessagesPerSec,
       "ss2bsEnqueuedP7MessagesPerSec": ss2bsEnqueuedP7MessagesPerSec,
       "ss2bsEnqueuedP8MessagesPerSec": ss2bsEnqueuedP8MessagesPerSec,
       "ss2bsEnqueuedP9MessagesPerSec": ss2bsEnqueuedP9MessagesPerSec,
       "ss2bsEnqueuedTransmissionQMsgSec": ss2bsEnqueuedTransmissionQMsgSec,
       "ss2bsEnqueuedTransportMsgFragTot": ss2bsEnqueuedTransportMsgFragTot,
       "ss2bsEnqueuedTransportMsgFragSec": ss2bsEnqueuedTransportMsgFragSec,
       "ss2bsEnqueuedTransportMsgsTotal": ss2bsEnqueuedTransportMsgsTotal,
       "ss2bsEnqueuedTransportMsgsPerSec": ss2bsEnqueuedTransportMsgsPerSec,
       "ss2bsForwardedMessagesTotal": ss2bsForwardedMessagesTotal,
       "ss2bsForwardedMessagesPerSec": ss2bsForwardedMessagesPerSec,
       "ss2bsForwardedMsgByteTotal": ss2bsForwardedMsgByteTotal,
       "ss2bsForwardedMsgBytesPerSec": ss2bsForwardedMsgBytesPerSec,
       "ss2bsForwardedMsgDiscardedTotal": ss2bsForwardedMsgDiscardedTotal,
       "ss2bsForwardedMsgsDiscardedSec": ss2bsForwardedMsgsDiscardedSec,
       "ss2bsForwardedPendingMsgBytes": ss2bsForwardedPendingMsgBytes,
       "ss2bsForwardedPendingMsgCount": ss2bsForwardedPendingMsgCount,
       "ss2bsSQLReceiveTotal": ss2bsSQLReceiveTotal,
       "ss2bsSQLReceivesPerSec": ss2bsSQLReceivesPerSec,
       "ss2bsSQLSendTotal": ss2bsSQLSendTotal,
       "ss2bsSQLSendsPerSec": ss2bsSQLSendsPerSec,
       "ss2BrokerTOStatisticsTable": ss2BrokerTOStatisticsTable,
       "ss2BrokerTOStatisticsEntry": ss2BrokerTOStatisticsEntry,
       "ss2btosAvgLengthOfBatchedWrites": ss2btosAvgLengthOfBatchedWrites,
       "ss2btosAvgTimeBetweenBatchesMs": ss2btosAvgTimeBetweenBatchesMs,
       "ss2btosAvgTimeToWriteBatchMs": ss2btosAvgTimeToWriteBatchMs,
       "ss2btosTransmissionObjGetsPerSec": ss2btosTransmissionObjGetsPerSec,
       "ss2btosTransmissionObjSetDirtSec": ss2btosTransmissionObjSetDirtSec,
       "ss2btosTransmissionObjWritesSec": ss2btosTransmissionObjWritesSec,
       "ss2BrokerPerDBMTransportTable": ss2BrokerPerDBMTransportTable,
       "ss2BrokerPerDBMTransportEntry": ss2BrokerPerDBMTransportEntry,
       "ss2bdtCurrentBytesForRecvIPerO": ss2bdtCurrentBytesForRecvIPerO,
       "ss2bdtCurrentBytesForSendIPerO": ss2bdtCurrentBytesForSendIPerO,
       "ss2bdtCurrentMsgFragForSendIO": ss2bdtCurrentMsgFragForSendIO,
       "ss2bdtMessageFragmentP1SenSec": ss2bdtMessageFragmentP1SenSec,
       "ss2bdtMsgFragmentP10SendsSec": ss2bdtMsgFragmentP10SendsSec,
       "ss2bdtMsgFragmentP2SendsSec": ss2bdtMsgFragmentP2SendsSec,
       "ss2bdtMsgFragmentP3SendsSec": ss2bdtMsgFragmentP3SendsSec,
       "ss2bdtMsgFragmentP4SendsSec": ss2bdtMsgFragmentP4SendsSec,
       "ss2bdtMsgFragmentP5SendsSec": ss2bdtMsgFragmentP5SendsSec,
       "ss2bdtMsgFragmentP6SendsSec": ss2bdtMsgFragmentP6SendsSec,
       "ss2bdtMsgFragmentP7SendsSec": ss2bdtMsgFragmentP7SendsSec,
       "ss2bdtMsgFragmentP8SendsSec": ss2bdtMsgFragmentP8SendsSec,
       "ss2bdtMsgFragmentP9SendsSec": ss2bdtMsgFragmentP9SendsSec,
       "ss2bdtMsgFragmentReceivesSec": ss2bdtMsgFragmentReceivesSec,
       "ss2bdtMessageFragmentSendsPerSec": ss2bdtMessageFragmentSendsPerSec,
       "ss2bdtMsgFragmentRecvSizeAvg": ss2bdtMsgFragmentRecvSizeAvg,
       "ss2bdtMsgFragmentSendSizeAvg": ss2bdtMsgFragmentSendSizeAvg,
       "ss2bdtOpenConnectionCount": ss2bdtOpenConnectionCount,
       "ss2bdtPendingBytesForRecvIPerO": ss2bdtPendingBytesForRecvIPerO,
       "ss2bdtPendingBytesForSendIPerO": ss2bdtPendingBytesForSendIPerO,
       "ss2bdtPendingMsgFragForRecvIO": ss2bdtPendingMsgFragForRecvIO,
       "ss2bdtPendingMsgFragForSendIO": ss2bdtPendingMsgFragForSendIO,
       "ss2bdtReceiveIPerOLenAvg": ss2bdtReceiveIPerOLenAvg,
       "ss2bdtReceiveIPerOBytesPerSec": ss2bdtReceiveIPerOBytesPerSec,
       "ss2bdtReceiveIPerOsPerSec": ss2bdtReceiveIPerOsPerSec,
       "ss2bdtRecvIPerOBufferCopiesCount": ss2bdtRecvIPerOBufferCopiesCount,
       "ss2bdtRecvIOBufferCopiesBytesSec": ss2bdtRecvIOBufferCopiesBytesSec,
       "ss2bdtSendIPerOLenAvg": ss2bdtSendIPerOLenAvg,
       "ss2bdtSendIPerOBytesPerSec": ss2bdtSendIPerOBytesPerSec,
       "ss2bdtSendIPerOsPerSec": ss2bdtSendIPerOsPerSec,
       "ss2BufferManagerTable": ss2BufferManagerTable,
       "ss2BufferManagerEntry": ss2BufferManagerEntry,
       "ss2bmAWELookupMapsPerSec": ss2bmAWELookupMapsPerSec,
       "ss2bmAWEStolenMapsPerSec": ss2bmAWEStolenMapsPerSec,
       "ss2bmAWEUnmapCallsPerSec": ss2bmAWEUnmapCallsPerSec,
       "ss2bmAWEUnmapPagesPerSec": ss2bmAWEUnmapPagesPerSec,
       "ss2bmAWEWriteMapsPerSec": ss2bmAWEWriteMapsPerSec,
       "ss2bmBufferCacheHitRatio": ss2bmBufferCacheHitRatio,
       "ss2bmCheckpointPagesPerSec": ss2bmCheckpointPagesPerSec,
       "ss2bmDatabasePages": ss2bmDatabasePages,
       "ss2bmFreeListStallsPerSec": ss2bmFreeListStallsPerSec,
       "ss2bmFreePages": ss2bmFreePages,
       "ss2bmLazyWritesPerSec": ss2bmLazyWritesPerSec,
       "ss2bmPageLifeExpectancy": ss2bmPageLifeExpectancy,
       "ss2bmPageLookupsPerSec": ss2bmPageLookupsPerSec,
       "ss2bmPageReadsPerSec": ss2bmPageReadsPerSec,
       "ss2bmPageWritesPerSec": ss2bmPageWritesPerSec,
       "ss2bmReadaheadPagesPerSec": ss2bmReadaheadPagesPerSec,
       "ss2bmReservedPages": ss2bmReservedPages,
       "ss2bmStolenPages": ss2bmStolenPages,
       "ss2bmTargetPages": ss2bmTargetPages,
       "ss2bmTotalPages": ss2bmTotalPages,
       "ss2BufferNodeTable": ss2BufferNodeTable,
       "ss2BufferNodeEntry": ss2BufferNodeEntry,
       "ss2bnInstance": ss2bnInstance,
       "ss2bnDatabasePages": ss2bnDatabasePages,
       "ss2bnForeignPages": ss2bnForeignPages,
       "ss2bnFreePages": ss2bnFreePages,
       "ss2bnLocalNodePageLookupsPerSec": ss2bnLocalNodePageLookupsPerSec,
       "ss2bnPageLifeExpectancy": ss2bnPageLifeExpectancy,
       "ss2bnRemoteNodePageLookupsPerSec": ss2bnRemoteNodePageLookupsPerSec,
       "ss2bnStolenPages": ss2bnStolenPages,
       "ss2bnTargetPages": ss2bnTargetPages,
       "ss2bnTotalPages": ss2bnTotalPages,
       "ss2BufferPartitionTable": ss2BufferPartitionTable,
       "ss2BufferPartitionEntry": ss2BufferPartitionEntry,
       "ss2bpInstance": ss2bpInstance,
       "ss2bpFreeListEmptyPerSec": ss2bpFreeListEmptyPerSec,
       "ss2bpFreeListRequestsPerSec": ss2bpFreeListRequestsPerSec,
       "ss2bpFreePages": ss2bpFreePages,
       "ss2CLRTable": ss2CLRTable,
       "ss2CLREntry": ss2CLREntry,
       "ss2CLRCLRExecution": ss2CLRCLRExecution,
       "ss2CatalogMetadataTable": ss2CatalogMetadataTable,
       "ss2CatalogMetadataEntry": ss2CatalogMetadataEntry,
       "ss2cmdInstance": ss2cmdInstance,
       "ss2cmdCacheEntriesCount": ss2cmdCacheEntriesCount,
       "ss2cmdCacheEntriesPinnedCount": ss2cmdCacheEntriesPinnedCount,
       "ss2cmdCacheHitRatio": ss2cmdCacheHitRatio,
       "ss2CursorManagerTotalTable": ss2CursorManagerTotalTable,
       "ss2CursorManagerTotalEntry": ss2CursorManagerTotalEntry,
       "ss2cmtAsyncPopulationCount": ss2cmtAsyncPopulationCount,
       "ss2cmtCursorConversionRate": ss2cmtCursorConversionRate,
       "ss2cmtCursorFlushes": ss2cmtCursorFlushes,
       "ss2CursorManagerByTypeTable": ss2CursorManagerByTypeTable,
       "ss2CursorManagerByTypeEntry": ss2CursorManagerByTypeEntry,
       "ss2cmbtInstance": ss2cmbtInstance,
       "ss2cmbtActiveCursors": ss2cmbtActiveCursors,
       "ss2cmbtCacheHitRatio": ss2cmbtCacheHitRatio,
       "ss2cmbtCachedCursorCounts": ss2cmbtCachedCursorCounts,
       "ss2cmbtCursorCacheUseCountsSec": ss2cmbtCursorCacheUseCountsSec,
       "ss2cmbtCursorRequestsPerSec": ss2cmbtCursorRequestsPerSec,
       "ss2cmbtCursorMemoryUsage": ss2cmbtCursorMemoryUsage,
       "ss2cmbtCursorWorktableUsage": ss2cmbtCursorWorktableUsage,
       "ss2cmbtNumberOfActiveCursorPlans": ss2cmbtNumberOfActiveCursorPlans,
       "ss2DatabaseMirroringTable": ss2DatabaseMirroringTable,
       "ss2DatabaseMirroringEntry": ss2DatabaseMirroringEntry,
       "ss2dmInstance": ss2dmInstance,
       "ss2dmBytesReceivedPerSec": ss2dmBytesReceivedPerSec,
       "ss2dmBytesSentPerSec": ss2dmBytesSentPerSec,
       "ss2dmLogBytesReceivedPerSec": ss2dmLogBytesReceivedPerSec,
       "ss2dmLogBytesRedoneFromCacheSec": ss2dmLogBytesRedoneFromCacheSec,
       "ss2dmLogBytesSentFromCachePerSec": ss2dmLogBytesSentFromCachePerSec,
       "ss2dmLogBytesSentPerSec": ss2dmLogBytesSentPerSec,
       "ss2dmLogCompressedBytesRcvdSec": ss2dmLogCompressedBytesRcvdSec,
       "ss2dmLogCompressedBytesSentSec": ss2dmLogCompressedBytesSentSec,
       "ss2dmLogHardenTimeMs": ss2dmLogHardenTimeMs,
       "ss2dmLogRemainingForUndoKB": ss2dmLogRemainingForUndoKB,
       "ss2dmLogScannedForUndoKB": ss2dmLogScannedForUndoKB,
       "ss2dmLogSendFlowControlTimeMs": ss2dmLogSendFlowControlTimeMs,
       "ss2dmLogSendQueueKB": ss2dmLogSendQueueKB,
       "ss2dmMirroredWritTransactionsSec": ss2dmMirroredWritTransactionsSec,
       "ss2dmPagesSentPerSec": ss2dmPagesSentPerSec,
       "ss2dmReceivesPerSec": ss2dmReceivesPerSec,
       "ss2dmRedoBytesPerSec": ss2dmRedoBytesPerSec,
       "ss2dmRedoQueueKB": ss2dmRedoQueueKB,
       "ss2dmSendPerReceiveAckTime": ss2dmSendPerReceiveAckTime,
       "ss2dmSendsPerSec": ss2dmSendsPerSec,
       "ss2dmTransactionDelay": ss2dmTransactionDelay,
       "ss2DatabasesTable": ss2DatabasesTable,
       "ss2DatabasesEntry": ss2DatabasesEntry,
       "ss2dbInstance": ss2dbInstance,
       "ss2dbActiveTransactions": ss2dbActiveTransactions,
       "ss2dbBackupRestoreThroughputSec": ss2dbBackupRestoreThroughputSec,
       "ss2dbBulkCopyRowsPerSec": ss2dbBulkCopyRowsPerSec,
       "ss2dbBulkCopyThroughputPerSec": ss2dbBulkCopyThroughputPerSec,
       "ss2dbCommitTableEntries": ss2dbCommitTableEntries,
       "ss2dbDBCCLogicalScanBytesPerSec": ss2dbDBCCLogicalScanBytesPerSec,
       "ss2dbDataFileSSizeKB": ss2dbDataFileSSizeKB,
       "ss2dbLogBytesFlushedPerSec": ss2dbLogBytesFlushedPerSec,
       "ss2dbLogCacheHitRatio": ss2dbLogCacheHitRatio,
       "ss2dbLogCacheReadsPerSec": ss2dbLogCacheReadsPerSec,
       "ss2dbLogFileSSizeKB": ss2dbLogFileSSizeKB,
       "ss2dbLogFileSUsedSizeKB": ss2dbLogFileSUsedSizeKB,
       "ss2dbLogFlushWaitTime": ss2dbLogFlushWaitTime,
       "ss2dbLogFlushWaitsPerSec": ss2dbLogFlushWaitsPerSec,
       "ss2dbLogFlushesPerSec": ss2dbLogFlushesPerSec,
       "ss2dbLogGrowths": ss2dbLogGrowths,
       "ss2dbLogShrinks": ss2dbLogShrinks,
       "ss2dbLogTruncations": ss2dbLogTruncations,
       "ss2dbPercentLogUsed": ss2dbPercentLogUsed,
       "ss2dbReplPendingXacts": ss2dbReplPendingXacts,
       "ss2dbReplTransRate": ss2dbReplTransRate,
       "ss2dbShrinkDataMovementBytesSec": ss2dbShrinkDataMovementBytesSec,
       "ss2dbTrackedTransactionsPerSec": ss2dbTrackedTransactionsPerSec,
       "ss2dbTransactionsPerSec": ss2dbTransactionsPerSec,
       "ss2dbWriteTransactionsPerSec": ss2dbWriteTransactionsPerSec,
       "ss2DeprecatedFeaturesTable": ss2DeprecatedFeaturesTable,
       "ss2DeprecatedFeaturesEntry": ss2DeprecatedFeaturesEntry,
       "ss2DeprecatedFeaturesInstance": ss2DeprecatedFeaturesInstance,
       "ss2DeprecatedFeaturesUsage": ss2DeprecatedFeaturesUsage,
       "ss2ExecStatisticsTable": ss2ExecStatisticsTable,
       "ss2ExecStatisticsEntry": ss2ExecStatisticsEntry,
       "ss2ExecStatisticsInstance": ss2ExecStatisticsInstance,
       "ss2ExecStatisticsDTCCalls": ss2ExecStatisticsDTCCalls,
       "ss2ExecStatisticDistributedQuery": ss2ExecStatisticDistributedQuery,
       "ss2ExecStatistExtendedProcedures": ss2ExecStatistExtendedProcedures,
       "ss2ExecStatisticsOLEDBCalls": ss2ExecStatisticsOLEDBCalls,
       "ss2GeneralStatisticsTable": ss2GeneralStatisticsTable,
       "ss2GeneralStatisticsEntry": ss2GeneralStatisticsEntry,
       "ss2gsActiveTempTables": ss2gsActiveTempTables,
       "ss2gsConnectionResetPerSec": ss2gsConnectionResetPerSec,
       "ss2gsEventNotificationsDelayDrop": ss2gsEventNotificationsDelayDrop,
       "ss2gsHTTPAuthenticatedRequests": ss2gsHTTPAuthenticatedRequests,
       "ss2gsLogicalConnections": ss2gsLogicalConnections,
       "ss2gsLoginsPerSec": ss2gsLoginsPerSec,
       "ss2gsLogoutsPerSec": ss2gsLogoutsPerSec,
       "ss2gsMarsDeadlocks": ss2gsMarsDeadlocks,
       "ss2gsNonAtomicYieldRate": ss2gsNonAtomicYieldRate,
       "ss2gsProcessesBlocked": ss2gsProcessesBlocked,
       "ss2gsSOAPEmptyRequests": ss2gsSOAPEmptyRequests,
       "ss2gsSOAPMethodInvocations": ss2gsSOAPMethodInvocations,
       "ss2gsSOAPSQLRequests": ss2gsSOAPSQLRequests,
       "ss2gsSOAPSessionInitiateRequests": ss2gsSOAPSessionInitiateRequests,
       "ss2gsSOAPSessionTerminateRequest": ss2gsSOAPSessionTerminateRequest,
       "ss2gsSOAPWSDLRequests": ss2gsSOAPWSDLRequests,
       "ss2gsSQLTraceIOProviderLockWaits": ss2gsSQLTraceIOProviderLockWaits,
       "ss2gsTempTablesCreationRate": ss2gsTempTablesCreationRate,
       "ss2gsTempTablesForDestruction": ss2gsTempTablesForDestruction,
       "ss2gsTempdbRecoveryUnitId": ss2gsTempdbRecoveryUnitId,
       "ss2gsTempdbRowsetId": ss2gsTempdbRowsetId,
       "ss2gsTraceEventNotificationQueue": ss2gsTraceEventNotificationQueue,
       "ss2gsTransactions": ss2gsTransactions,
       "ss2gsUserConnections": ss2gsUserConnections,
       "ss2LatchesTable": ss2LatchesTable,
       "ss2LatchesEntry": ss2LatchesEntry,
       "ss2LatchesAverageLatchWaitTimeMs": ss2LatchesAverageLatchWaitTimeMs,
       "ss2LatchesLatchWaitsPerSec": ss2LatchesLatchWaitsPerSec,
       "ss2LatchesNumberOfSuperLatches": ss2LatchesNumberOfSuperLatches,
       "ss2LatchesSuLatchDemotionsSec": ss2LatchesSuLatchDemotionsSec,
       "ss2LatchesSuLatchPromotionsSec": ss2LatchesSuLatchPromotionsSec,
       "ss2LatchesTotalLatchWaitTimeMs": ss2LatchesTotalLatchWaitTimeMs,
       "ss2LocksTable": ss2LocksTable,
       "ss2LocksEntry": ss2LocksEntry,
       "ss2LocksInstance": ss2LocksInstance,
       "ss2LocksAverageWaitTimeMs": ss2LocksAverageWaitTimeMs,
       "ss2LocksLockRequestsPerSec": ss2LocksLockRequestsPerSec,
       "ss2LocksTimeoutsGreaterThan0Sec": ss2LocksTimeoutsGreaterThan0Sec,
       "ss2LocksLockTimeoutsPerSec": ss2LocksLockTimeoutsPerSec,
       "ss2LocksLockWaitTimeMs": ss2LocksLockWaitTimeMs,
       "ss2LocksLockWaitsPerSec": ss2LocksLockWaitsPerSec,
       "ss2LocksNumberOfDeadlocksPerSec": ss2LocksNumberOfDeadlocksPerSec,
       "ss2MemoryManagerTable": ss2MemoryManagerTable,
       "ss2MemoryManagerEntry": ss2MemoryManagerEntry,
       "ss2mmConnectionMemoryKB": ss2mmConnectionMemoryKB,
       "ss2mmGrantedWorkspaceMemoryKB": ss2mmGrantedWorkspaceMemoryKB,
       "ss2mmLockBlocks": ss2mmLockBlocks,
       "ss2mmLockBlocksAllocated": ss2mmLockBlocksAllocated,
       "ss2mmLockMemoryKB": ss2mmLockMemoryKB,
       "ss2mmLockOwnerBlocks": ss2mmLockOwnerBlocks,
       "ss2mmLockOwnerBlocksAllocated": ss2mmLockOwnerBlocksAllocated,
       "ss2mmMaximumWorkspaceMemoryKB": ss2mmMaximumWorkspaceMemoryKB,
       "ss2mmMemoryGrantsOutstanding": ss2mmMemoryGrantsOutstanding,
       "ss2mmMemoryGrantsPending": ss2mmMemoryGrantsPending,
       "ss2mmOptimizerMemoryKB": ss2mmOptimizerMemoryKB,
       "ss2mmSQLCacheMemoryKB": ss2mmSQLCacheMemoryKB,
       "ss2mmTargetServerMemoryKB": ss2mmTargetServerMemoryKB,
       "ss2mmTotalServerMemoryKB": ss2mmTotalServerMemoryKB,
       "ss2PlanCacheTable": ss2PlanCacheTable,
       "ss2PlanCacheEntry": ss2PlanCacheEntry,
       "ss2PlanCacheInstance": ss2PlanCacheInstance,
       "ss2PlanCacheCacheHitRatio": ss2PlanCacheCacheHitRatio,
       "ss2PlanCacheCacheObjectCounts": ss2PlanCacheCacheObjectCounts,
       "ss2PlanCacheCacheObjectsInUse": ss2PlanCacheCacheObjectsInUse,
       "ss2PlanCacheCachePages": ss2PlanCacheCachePages,
       "ss2ReplicationAgentsTable": ss2ReplicationAgentsTable,
       "ss2ReplicationAgentsEntry": ss2ReplicationAgentsEntry,
       "ss2ReplicationAgentsInstance": ss2ReplicationAgentsInstance,
       "ss2ReplicationAgentsRunning": ss2ReplicationAgentsRunning,
       "ss2ReplicationDistTable": ss2ReplicationDistTable,
       "ss2ReplicationDistEntry": ss2ReplicationDistEntry,
       "ss2rdInstance": ss2rdInstance,
       "ss2rdDistDeliveredCmdsPerSec": ss2rdDistDeliveredCmdsPerSec,
       "ss2rdDistDeliveredTransPerSec": ss2rdDistDeliveredTransPerSec,
       "ss2rdDistDeliveryLatency": ss2rdDistDeliveryLatency,
       "ss2ReplicationLogreaderTable": ss2ReplicationLogreaderTable,
       "ss2ReplicationLogreaderEntry": ss2ReplicationLogreaderEntry,
       "ss2rlInstance": ss2rlInstance,
       "ss2rlLogreaderDeliveredCmdsSec": ss2rlLogreaderDeliveredCmdsSec,
       "ss2rlLogreaderDeliveredTransSec": ss2rlLogreaderDeliveredTransSec,
       "ss2rlLogreaderDeliveryLatency": ss2rlLogreaderDeliveryLatency,
       "ss2ReplicationMergeTable": ss2ReplicationMergeTable,
       "ss2ReplicationMergeEntry": ss2ReplicationMergeEntry,
       "ss2rmInstance": ss2rmInstance,
       "ss2rmConflictsPerSec": ss2rmConflictsPerSec,
       "ss2rmDownloadedChangesPerSec": ss2rmDownloadedChangesPerSec,
       "ss2rmUploadedChangesPerSec": ss2rmUploadedChangesPerSec,
       "ss2ReplicationSnapshotTable": ss2ReplicationSnapshotTable,
       "ss2ReplicationSnapshotEntry": ss2ReplicationSnapshotEntry,
       "ss2rsInstance": ss2rsInstance,
       "ss2rsSnapshotDeliveredCmdsPerSec": ss2rsSnapshotDeliveredCmdsPerSec,
       "ss2rsSnapshotDeliveredTransSec": ss2rsSnapshotDeliveredTransSec,
       "ss2ResourcePoolStatsTable": ss2ResourcePoolStatsTable,
       "ss2ResourcePoolStatsEntry": ss2ResourcePoolStatsEntry,
       "ss2rpsInstance": ss2rpsInstance,
       "ss2rpsActiveMemoryGrantAmountKB": ss2rpsActiveMemoryGrantAmountKB,
       "ss2rpsActiveMemoryGrantsCount": ss2rpsActiveMemoryGrantsCount,
       "ss2rpsCPUControlEffectPercent": ss2rpsCPUControlEffectPercent,
       "ss2rpsCPUUsagePercent": ss2rpsCPUUsagePercent,
       "ss2rpsCPUUsageTargetPercent": ss2rpsCPUUsageTargetPercent,
       "ss2rpsCacheMemoryTargetKB": ss2rpsCacheMemoryTargetKB,
       "ss2rpsCompileMemoryTargetKB": ss2rpsCompileMemoryTargetKB,
       "ss2rpsMaxMemoryKB": ss2rpsMaxMemoryKB,
       "ss2rpsMemoryGrantTimeoutsPerSec": ss2rpsMemoryGrantTimeoutsPerSec,
       "ss2rpsMemoryGrantsPerSec": ss2rpsMemoryGrantsPerSec,
       "ss2rpsPendingMemoryGrantsCount": ss2rpsPendingMemoryGrantsCount,
       "ss2rpsQueryExecMemoryTargetKB": ss2rpsQueryExecMemoryTargetKB,
       "ss2rpsTargetMemoryKB": ss2rpsTargetMemoryKB,
       "ss2rpsUsedMemoryKB": ss2rpsUsedMemoryKB,
       "ss2SQLErrorsTable": ss2SQLErrorsTable,
       "ss2SQLErrorsEntry": ss2SQLErrorsEntry,
       "ss2SQLErrorsInstance": ss2SQLErrorsInstance,
       "ss2SQLErrorsErrorsPerSec": ss2SQLErrorsErrorsPerSec,
       "ss2SQLStatisticsTable": ss2SQLStatisticsTable,
       "ss2SQLStatisticsEntry": ss2SQLStatisticsEntry,
       "ss2sqsAutoParamAttemptsPerSec": ss2sqsAutoParamAttemptsPerSec,
       "ss2sqsBatchRequestsPerSec": ss2sqsBatchRequestsPerSec,
       "ss2sqsFailedAutoParamsPerSec": ss2sqsFailedAutoParamsPerSec,
       "ss2sqsForcedParameterizationsSec": ss2sqsForcedParameterizationsSec,
       "ss2sqsGuidedPlanExecutionsPerSec": ss2sqsGuidedPlanExecutionsPerSec,
       "ss2sqsMisguidedPlanExecutionsSec": ss2sqsMisguidedPlanExecutionsSec,
       "ss2sqsSQLAttentionRate": ss2sqsSQLAttentionRate,
       "ss2sqsSQLCompilationsPerSec": ss2sqsSQLCompilationsPerSec,
       "ss2sqsSQLReCompilationsPerSec": ss2sqsSQLReCompilationsPerSec,
       "ss2sqsSafeAutoParamsPerSec": ss2sqsSafeAutoParamsPerSec,
       "ss2sqsUnsafeAutoParamsPerSec": ss2sqsUnsafeAutoParamsPerSec,
       "ss2SSISPipelineTable": ss2SSISPipelineTable,
       "ss2SSISPipelineEntry": ss2SSISPipelineEntry,
       "ss2SSISPipelineBLOBBytesRead": ss2SSISPipelineBLOBBytesRead,
       "ss2SSISPipelineBLOBBytesWritten": ss2SSISPipelineBLOBBytesWritten,
       "ss2SSISPipelineBLOBFilesInUse": ss2SSISPipelineBLOBFilesInUse,
       "ss2SSISPipelineBufferMemory": ss2SSISPipelineBufferMemory,
       "ss2SSISPipelineBuffersInUse": ss2SSISPipelineBuffersInUse,
       "ss2SSISPipelineBuffersSpooled": ss2SSISPipelineBuffersSpooled,
       "ss2SSISPipelineFlatBufferMemory": ss2SSISPipelineFlatBufferMemory,
       "ss2SSISPipelineFlatBuffersInUse": ss2SSISPipelineFlatBuffersInUse,
       "ss2SSISPipelinePrivateBuffMemory": ss2SSISPipelinePrivateBuffMemory,
       "ss2SSISPipelinePrivateBuffersUse": ss2SSISPipelinePrivateBuffersUse,
       "ss2SSISPipelineRowsRead": ss2SSISPipelineRowsRead,
       "ss2SSISPipelineRowsWritten": ss2SSISPipelineRowsWritten,
       "ss2SSISServiceTable": ss2SSISServiceTable,
       "ss2SSISServiceEntry": ss2SSISServiceEntry,
       "ss2SSISServiceSSISPackageInstanc": ss2SSISServiceSSISPackageInstanc,
       "ss2TraceEventStatisticsTable": ss2TraceEventStatisticsTable,
       "ss2TraceEventStatisticsEntry": ss2TraceEventStatisticsEntry,
       "ss2tesInstance": ss2tesInstance,
       "ss2tesBytesPerSec": ss2tesBytesPerSec,
       "ss2tesCPUTicksPerSec": ss2tesCPUTicksPerSec,
       "ss2tesEventsFilteredPerSec": ss2tesEventsFilteredPerSec,
       "ss2tesEventsFiredPerSec": ss2tesEventsFiredPerSec,
       "ss2tesEventsPrefilteredPerSec": ss2tesEventsPrefilteredPerSec,
       "ss2TraceStatisticsTable": ss2TraceStatisticsTable,
       "ss2TraceStatisticsEntry": ss2TraceStatisticsEntry,
       "ss2tstInstance": ss2tstInstance,
       "ss2tstBytesPerSec": ss2tstBytesPerSec,
       "ss2tstDroppedEventsPerSec": ss2tstDroppedEventsPerSec,
       "ss2tstEventsFilteredPerSec": ss2tstEventsFilteredPerSec,
       "ss2tstEventsFiredPerSec": ss2tstEventsFiredPerSec,
       "ss2TransactionsTable": ss2TransactionsTable,
       "ss2TransactionsEntry": ss2TransactionsEntry,
       "ss2trnFreeSpaceInTempdbKB": ss2trnFreeSpaceInTempdbKB,
       "ss2trnLongestTransactRunningTime": ss2trnLongestTransactRunningTime,
       "ss2trnNonSnapshotVersionTransact": ss2trnNonSnapshotVersionTransact,
       "ss2trnSnapshotTransactions": ss2trnSnapshotTransactions,
       "ss2trnTransactions": ss2trnTransactions,
       "ss2trnUpdateSnapshotTransactions": ss2trnUpdateSnapshotTransactions,
       "ss2trnUpdateConflictRatio": ss2trnUpdateConflictRatio,
       "ss2trnVersionCleanupRateKBPerS": ss2trnVersionCleanupRateKBPerS,
       "ss2trnVersionGenerationRateKBS": ss2trnVersionGenerationRateKBS,
       "ss2trnVersionStoreSizeKB": ss2trnVersionStoreSizeKB,
       "ss2trnVersionStoreUnitCount": ss2trnVersionStoreUnitCount,
       "ss2trnVersionStoreUnitCreation": ss2trnVersionStoreUnitCreation,
       "ss2trnVersionStoreUnitTruncation": ss2trnVersionStoreUnitTruncation,
       "ss2UserSettableTable": ss2UserSettableTable,
       "ss2UserSettableEntry": ss2UserSettableEntry,
       "ss2UserSettableInstance": ss2UserSettableInstance,
       "ss2UserSettableQuery": ss2UserSettableQuery,
       "ss2WaitStatisticsTable": ss2WaitStatisticsTable,
       "ss2WaitStatisticsEntry": ss2WaitStatisticsEntry,
       "ss2wsInstance": ss2wsInstance,
       "ss2wsLockWaits": ss2wsLockWaits,
       "ss2wsLogBufferWaits": ss2wsLogBufferWaits,
       "ss2wsLogWriteWaits": ss2wsLogWriteWaits,
       "ss2wsMemoryGrantQueueWaits": ss2wsMemoryGrantQueueWaits,
       "ss2wsNetworkIOWaits": ss2wsNetworkIOWaits,
       "ss2wsNonPageLatchWaits": ss2wsNonPageLatchWaits,
       "ss2wsPageIOLatchWaits": ss2wsPageIOLatchWaits,
       "ss2wsPageLatchWaits": ss2wsPageLatchWaits,
       "ss2wsThreadSafeMemoryObjectsWait": ss2wsThreadSafeMemoryObjectsWait,
       "ss2wsTransactionOwnershipWaits": ss2wsTransactionOwnershipWaits,
       "ss2wsWaitForTheWorker": ss2wsWaitForTheWorker,
       "ss2wsWorkspaceSynchronizatWaits": ss2wsWorkspaceSynchronizatWaits,
       "ss2WorkloadGroupStatsTable": ss2WorkloadGroupStatsTable,
       "ss2WorkloadGroupStatsEntry": ss2WorkloadGroupStatsEntry,
       "ss2wgsInstance": ss2wgsInstance,
       "ss2wgsActiveParallelThreads": ss2wgsActiveParallelThreads,
       "ss2wgsActiveRequests": ss2wgsActiveRequests,
       "ss2wgsBlockedTasks": ss2wgsBlockedTasks,
       "ss2wgsCPUUsagePercent": ss2wgsCPUUsagePercent,
       "ss2wgsMaxRequestCpuTimeMs": ss2wgsMaxRequestCpuTimeMs,
       "ss2wgsMaxRequestMemoryGrantKB": ss2wgsMaxRequestMemoryGrantKB,
       "ss2wgsQueryOptimizationsPerSec": ss2wgsQueryOptimizationsPerSec,
       "ss2wgsQueuedRequests": ss2wgsQueuedRequests,
       "ss2wgsReducedMemoryGrantsPerSec": ss2wgsReducedMemoryGrantsPerSec,
       "ss2wgsRequestsCompletedPerSec": ss2wgsRequestsCompletedPerSec,
       "ss2wgsSuboptimalPlansPerSec": ss2wgsSuboptimalPlansPerSec,
       "sqlServerAgentV2": sqlServerAgentV2,
       "sa2NameTable": sa2NameTable,
       "sa2NameEntry": sa2NameEntry,
       "sa2NameIndex": sa2NameIndex,
       "sa2NameInstance": sa2NameInstance,
       "sa2AlertsTable": sa2AlertsTable,
       "sa2AlertsEntry": sa2AlertsEntry,
       "sa2AlertsActivatedAlerts": sa2AlertsActivatedAlerts,
       "sa2AlertsAlertsActivatedMinute": sa2AlertsAlertsActivatedMinute,
       "sa2JobsTable": sa2JobsTable,
       "sa2JobsEntry": sa2JobsEntry,
       "sa2JobsInstance": sa2JobsInstance,
       "sa2JobsActiveJobs": sa2JobsActiveJobs,
       "sa2JobsFailedJobs": sa2JobsFailedJobs,
       "sa2JobsJobSuccessRate": sa2JobsJobSuccessRate,
       "sa2JobsJobsActivatedPerMinute": sa2JobsJobsActivatedPerMinute,
       "sa2JobsQueuedJobs": sa2JobsQueuedJobs,
       "sa2JobsSuccessfulJobs": sa2JobsSuccessfulJobs,
       "sa2JobStepsTable": sa2JobStepsTable,
       "sa2JobStepsEntry": sa2JobStepsEntry,
       "sa2JobStepsInstance": sa2JobStepsInstance,
       "sa2JobStepsActiveSteps": sa2JobStepsActiveSteps,
       "sa2JobStepsQueuedSteps": sa2JobStepsQueuedSteps,
       "sa2JobStepsTotalStepRetries": sa2JobStepsTotalStepRetries,
       "sa2StatisticsTable": sa2StatisticsTable,
       "sa2StatisticsEntry": sa2StatisticsEntry,
       "sa2StatisticsSQLServerRestarted": sa2StatisticsSQLServerRestarted,
       "reportingServicesV2": reportingServicesV2,
       "rs2WebService": rs2WebService,
       "rs2wbsActiveSessions": rs2wbsActiveSessions,
       "rs2wbsCacheHitsPerSec": rs2wbsCacheHitsPerSec,
       "rs2wbsCacheHitsSecSemanticModels": rs2wbsCacheHitsSecSemanticModels,
       "rs2wbsCacheMissesPerSec": rs2wbsCacheMissesPerSec,
       "rs2wbsCacheMissesSecSemantModels": rs2wbsCacheMissesSecSemantModels,
       "rs2wbsFirstSessionRequestsPerSec": rs2wbsFirstSessionRequestsPerSec,
       "rs2wbsMemoryCacheHitsPerSec": rs2wbsMemoryCacheHitsPerSec,
       "rs2wbsMemoryCacheMissPerSec": rs2wbsMemoryCacheMissPerSec,
       "rs2wbsNextSessionRequestsPerSec": rs2wbsNextSessionRequestsPerSec,
       "rs2wbsReportRequests": rs2wbsReportRequests,
       "rs2wbsReportsExecutedPerSec": rs2wbsReportsExecutedPerSec,
       "rs2wbsRequestsPerSec": rs2wbsRequestsPerSec,
       "rs2wbsTotalCacheHits": rs2wbsTotalCacheHits,
       "rs2wbsTotalCacheHitSemanticModel": rs2wbsTotalCacheHitSemanticModel,
       "rs2wbsTotalCacheMisses": rs2wbsTotalCacheMisses,
       "rs2wbsTotalCachMissSemanticModel": rs2wbsTotalCachMissSemanticModel,
       "rs2wbsTotalMemoryCacheHits": rs2wbsTotalMemoryCacheHits,
       "rs2wbsTotalMemoryCacheMisses": rs2wbsTotalMemoryCacheMisses,
       "rs2wbsTotalProcessingFailures": rs2wbsTotalProcessingFailures,
       "rs2wbsTotalRejectedThreads": rs2wbsTotalRejectedThreads,
       "rs2wbsTotalReportsExecute": rs2wbsTotalReportsExecute,
       "rs2wbsTotalRequests": rs2wbsTotalRequests,
       "rs2WindowsServiceTable": rs2WindowsServiceTable,
       "rs2WindowsServiceEntry": rs2WindowsServiceEntry,
       "rs2wnsInstance": rs2wnsInstance,
       "rs2wnsActiveSessions": rs2wnsActiveSessions,
       "rs2wnsCacheFlushesPerSec": rs2wnsCacheFlushesPerSec,
       "rs2wnsCacheHitsPerSec": rs2wnsCacheHitsPerSec,
       "rs2wnsCacheHitsSecSemanticModels": rs2wnsCacheHitsSecSemanticModels,
       "rs2wnsCacheMissesPerSec": rs2wnsCacheMissesPerSec,
       "rs2wnsCacheMissSecSemanticModels": rs2wnsCacheMissSecSemanticModels,
       "rs2wnsDeliversPerSec": rs2wnsDeliversPerSec,
       "rs2wnsEventsPerSec": rs2wnsEventsPerSec,
       "rs2wnsFirstSessionRequestsPerSec": rs2wnsFirstSessionRequestsPerSec,
       "rs2wnsMemoryCacheHitsPerSec": rs2wnsMemoryCacheHitsPerSec,
       "rs2wnsMemoryCacheMissPerSec": rs2wnsMemoryCacheMissPerSec,
       "rs2wnsNextSessionRequestsPerSec": rs2wnsNextSessionRequestsPerSec,
       "rs2wnsReportRequests": rs2wnsReportRequests,
       "rs2wnsReportsExecutedPerSec": rs2wnsReportsExecutedPerSec,
       "rs2wnsRequestsPerSec": rs2wnsRequestsPerSec,
       "rs2wnsSnapshotUpdatesPerSec": rs2wnsSnapshotUpdatesPerSec,
       "rs2wnsTotalAppDomainRecycles": rs2wnsTotalAppDomainRecycles,
       "rs2wnsTotalCacheFlushes": rs2wnsTotalCacheFlushes,
       "rs2wnsTotalCacheHits": rs2wnsTotalCacheHits,
       "rs2wnsTotalCacheHitSemanticModel": rs2wnsTotalCacheHitSemanticModel,
       "rs2wnsTotalCacheMisses": rs2wnsTotalCacheMisses,
       "rs2wnsTotalCachMissSemanticModel": rs2wnsTotalCachMissSemanticModel,
       "rs2wnsTotalDeliveries": rs2wnsTotalDeliveries,
       "rs2wnsTotalEvents": rs2wnsTotalEvents,
       "rs2wnsTotalMemoryCacheHits": rs2wnsTotalMemoryCacheHits,
       "rs2wnsTotalMemoryCacheMisses": rs2wnsTotalMemoryCacheMisses,
       "rs2wnsTotalProcessingFailures": rs2wnsTotalProcessingFailures,
       "rs2wnsTotalRejectedThreads": rs2wnsTotalRejectedThreads,
       "rs2wnsTotalReportsExecuted": rs2wnsTotalReportsExecuted,
       "rs2wnsTotalRequests": rs2wnsTotalRequests,
       "rs2wnsTotalSnapshotUpdates": rs2wnsTotalSnapshotUpdates,
       "rs2ReportServerHTTPTable": rs2ReportServerHTTPTable,
       "rs2ReportServerHTTPEntry": rs2ReportServerHTTPEntry,
       "rs2HTTPNameIndex": rs2HTTPNameIndex,
       "rs2HTTPNameInstance": rs2HTTPNameInstance,
       "rs2HTTPRequestsPerSec": rs2HTTPRequestsPerSec,
       "rs2HTTPTotalRequests": rs2HTTPTotalRequests}
)
