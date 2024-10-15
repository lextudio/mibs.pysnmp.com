# SNMP MIB module (INFORMANT-SQLSERVER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INFORMANT-SQLSERVER
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

sqlServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3)
)
sqlServer.setRevisions(
        ("2004-09-10 20:47",
         "2004-02-29 06:23",
         "2004-01-20 08:55")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AnalysisServerAggCache_ObjectIdentity = ObjectIdentity
analysisServerAggCache = _AnalysisServerAggCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1)
)
if mibBuilder.loadTexts:
    analysisServerAggCache.setStatus("current")
_AsacBytesAddedPerSec_Type = Gauge32
_AsacBytesAddedPerSec_Object = MibScalar
asacBytesAddedPerSec = _AsacBytesAddedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 1),
    _AsacBytesAddedPerSec_Type()
)
asacBytesAddedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacBytesAddedPerSec.setStatus("current")
_AsacCurrentBytes_Type = Gauge32
_AsacCurrentBytes_Object = MibScalar
asacCurrentBytes = _AsacCurrentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 2),
    _AsacCurrentBytes_Type()
)
asacCurrentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacCurrentBytes.setStatus("current")
_AsacCurrentEntries_Type = Gauge32
_AsacCurrentEntries_Object = MibScalar
asacCurrentEntries = _AsacCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 3),
    _AsacCurrentEntries_Type()
)
asacCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacCurrentEntries.setStatus("current")
_AsacDirectHitRatio_Type = Gauge32
_AsacDirectHitRatio_Object = MibScalar
asacDirectHitRatio = _AsacDirectHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 4),
    _AsacDirectHitRatio_Type()
)
asacDirectHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacDirectHitRatio.setStatus("current")
_AsacDirectHitsPerSec_Type = Gauge32
_AsacDirectHitsPerSec_Object = MibScalar
asacDirectHitsPerSec = _AsacDirectHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 5),
    _AsacDirectHitsPerSec_Type()
)
asacDirectHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacDirectHitsPerSec.setStatus("current")
_AsacEvictionsPerSec_Type = Gauge32
_AsacEvictionsPerSec_Object = MibScalar
asacEvictionsPerSec = _AsacEvictionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 6),
    _AsacEvictionsPerSec_Type()
)
asacEvictionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacEvictionsPerSec.setStatus("current")
_AsacFilterHitRatio_Type = Gauge32
_AsacFilterHitRatio_Object = MibScalar
asacFilterHitRatio = _AsacFilterHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 7),
    _AsacFilterHitRatio_Type()
)
asacFilterHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacFilterHitRatio.setStatus("current")
_AsacFilterHitsPerSec_Type = Gauge32
_AsacFilterHitsPerSec_Object = MibScalar
asacFilterHitsPerSec = _AsacFilterHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 8),
    _AsacFilterHitsPerSec_Type()
)
asacFilterHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacFilterHitsPerSec.setStatus("current")
_AsacInsertsPerSec_Type = Gauge32
_AsacInsertsPerSec_Object = MibScalar
asacInsertsPerSec = _AsacInsertsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 9),
    _AsacInsertsPerSec_Type()
)
asacInsertsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacInsertsPerSec.setStatus("current")
_AsacLookupsPerSec_Type = Gauge32
_AsacLookupsPerSec_Object = MibScalar
asacLookupsPerSec = _AsacLookupsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 10),
    _AsacLookupsPerSec_Type()
)
asacLookupsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacLookupsPerSec.setStatus("current")
_AsacMissesPerSec_Type = Gauge32
_AsacMissesPerSec_Object = MibScalar
asacMissesPerSec = _AsacMissesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 11),
    _AsacMissesPerSec_Type()
)
asacMissesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacMissesPerSec.setStatus("current")
_AsacTotalDirectHits_Type = Gauge32
_AsacTotalDirectHits_Object = MibScalar
asacTotalDirectHits = _AsacTotalDirectHits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 12),
    _AsacTotalDirectHits_Type()
)
asacTotalDirectHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacTotalDirectHits.setStatus("current")
_AsacTotalEvictions_Type = Gauge32
_AsacTotalEvictions_Object = MibScalar
asacTotalEvictions = _AsacTotalEvictions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 13),
    _AsacTotalEvictions_Type()
)
asacTotalEvictions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacTotalEvictions.setStatus("current")
_AsacTotalFilterHits_Type = Gauge32
_AsacTotalFilterHits_Object = MibScalar
asacTotalFilterHits = _AsacTotalFilterHits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 14),
    _AsacTotalFilterHits_Type()
)
asacTotalFilterHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacTotalFilterHits.setStatus("current")
_AsacTotalInserts_Type = Gauge32
_AsacTotalInserts_Object = MibScalar
asacTotalInserts = _AsacTotalInserts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 15),
    _AsacTotalInserts_Type()
)
asacTotalInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacTotalInserts.setStatus("current")
_AsacTotalLookups_Type = Gauge32
_AsacTotalLookups_Object = MibScalar
asacTotalLookups = _AsacTotalLookups_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 16),
    _AsacTotalLookups_Type()
)
asacTotalLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacTotalLookups.setStatus("current")
_AsacTotalMisses_Type = Gauge32
_AsacTotalMisses_Object = MibScalar
asacTotalMisses = _AsacTotalMisses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 1, 17),
    _AsacTotalMisses_Type()
)
asacTotalMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asacTotalMisses.setStatus("current")
_AnalysisServerConnection_ObjectIdentity = ObjectIdentity
analysisServerConnection = _AnalysisServerConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2)
)
if mibBuilder.loadTexts:
    analysisServerConnection.setStatus("current")
_AscAuthenticationsPerSec_Type = Gauge32
_AscAuthenticationsPerSec_Object = MibScalar
ascAuthenticationsPerSec = _AscAuthenticationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 1),
    _AscAuthenticationsPerSec_Type()
)
ascAuthenticationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascAuthenticationsPerSec.setStatus("current")
_AscCompletionsPerSec_Type = Gauge32
_AscCompletionsPerSec_Object = MibScalar
ascCompletionsPerSec = _AscCompletionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 2),
    _AscCompletionsPerSec_Type()
)
ascCompletionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascCompletionsPerSec.setStatus("current")
_AscCurrentAgents_Type = Gauge32
_AscCurrentAgents_Object = MibScalar
ascCurrentAgents = _AscCurrentAgents_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 3),
    _AscCurrentAgents_Type()
)
ascCurrentAgents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascCurrentAgents.setStatus("current")
_AscCurrentAuthentications_Type = Gauge32
_AscCurrentAuthentications_Object = MibScalar
ascCurrentAuthentications = _AscCurrentAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 4),
    _AscCurrentAuthentications_Type()
)
ascCurrentAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascCurrentAuthentications.setStatus("current")
_AscCurrentConnections_Type = Gauge32
_AscCurrentConnections_Object = MibScalar
ascCurrentConnections = _AscCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 5),
    _AscCurrentConnections_Type()
)
ascCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascCurrentConnections.setStatus("current")
_AscCurrentConnectionsInProgress_Type = Gauge32
_AscCurrentConnectionsInProgress_Object = MibScalar
ascCurrentConnectionsInProgress = _AscCurrentConnectionsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 6),
    _AscCurrentConnectionsInProgress_Type()
)
ascCurrentConnectionsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascCurrentConnectionsInProgress.setStatus("current")
_AscCurrentHttpConnections_Type = Gauge32
_AscCurrentHttpConnections_Object = MibScalar
ascCurrentHttpConnections = _AscCurrentHttpConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 7),
    _AscCurrentHttpConnections_Type()
)
ascCurrentHttpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascCurrentHttpConnections.setStatus("current")
_AscFailuresPerSec_Type = Gauge32
_AscFailuresPerSec_Object = MibScalar
ascFailuresPerSec = _AscFailuresPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 8),
    _AscFailuresPerSec_Type()
)
ascFailuresPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascFailuresPerSec.setStatus("current")
_AscRequestsPerSec_Type = Gauge32
_AscRequestsPerSec_Object = MibScalar
ascRequestsPerSec = _AscRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 9),
    _AscRequestsPerSec_Type()
)
ascRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascRequestsPerSec.setStatus("current")
_AscSuccessesPerSec_Type = Gauge32
_AscSuccessesPerSec_Object = MibScalar
ascSuccessesPerSec = _AscSuccessesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 10),
    _AscSuccessesPerSec_Type()
)
ascSuccessesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascSuccessesPerSec.setStatus("current")
_AscTotalAuthentications_Type = Gauge32
_AscTotalAuthentications_Object = MibScalar
ascTotalAuthentications = _AscTotalAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 11),
    _AscTotalAuthentications_Type()
)
ascTotalAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascTotalAuthentications.setStatus("current")
_AscTotalCompletions_Type = Gauge32
_AscTotalCompletions_Object = MibScalar
ascTotalCompletions = _AscTotalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 12),
    _AscTotalCompletions_Type()
)
ascTotalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascTotalCompletions.setStatus("current")
_AscTotalFailures_Type = Gauge32
_AscTotalFailures_Object = MibScalar
ascTotalFailures = _AscTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 13),
    _AscTotalFailures_Type()
)
ascTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascTotalFailures.setStatus("current")
_AscTotalRequests_Type = Gauge32
_AscTotalRequests_Object = MibScalar
ascTotalRequests = _AscTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 14),
    _AscTotalRequests_Type()
)
ascTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascTotalRequests.setStatus("current")
_AscTotalSuccesses_Type = Gauge32
_AscTotalSuccesses_Object = MibScalar
ascTotalSuccesses = _AscTotalSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 2, 15),
    _AscTotalSuccesses_Type()
)
ascTotalSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ascTotalSuccesses.setStatus("current")
_AnalysisServerLastQuery_ObjectIdentity = ObjectIdentity
analysisServerLastQuery = _AnalysisServerLastQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3)
)
if mibBuilder.loadTexts:
    analysisServerLastQuery.setStatus("current")
_AslqAnswerFromCacheDirect_Type = Gauge32
_AslqAnswerFromCacheDirect_Object = MibScalar
aslqAnswerFromCacheDirect = _AslqAnswerFromCacheDirect_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 1),
    _AslqAnswerFromCacheDirect_Type()
)
aslqAnswerFromCacheDirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqAnswerFromCacheDirect.setStatus("current")
_AslqAnswerFromCacheFiltered_Type = Gauge32
_AslqAnswerFromCacheFiltered_Object = MibScalar
aslqAnswerFromCacheFiltered = _AslqAnswerFromCacheFiltered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 2),
    _AslqAnswerFromCacheFiltered_Type()
)
aslqAnswerFromCacheFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqAnswerFromCacheFiltered.setStatus("current")
_AslqAnswerFromFile_Type = Gauge32
_AslqAnswerFromFile_Object = MibScalar
aslqAnswerFromFile = _AslqAnswerFromFile_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 3),
    _AslqAnswerFromFile_Type()
)
aslqAnswerFromFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqAnswerFromFile.setStatus("current")
_AslqDSNRequested_Type = Gauge32
_AslqDSNRequested_Object = MibScalar
aslqDSNRequested = _AslqDSNRequested_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 4),
    _AslqDSNRequested_Type()
)
aslqDSNRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqDSNRequested.setStatus("current")
_AslqDSNUsed_Type = Gauge32
_AslqDSNUsed_Object = MibScalar
aslqDSNUsed = _AslqDSNUsed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 5),
    _AslqDSNUsed_Type()
)
aslqDSNUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqDSNUsed.setStatus("current")
_AslqDataAvgBytesPerRead_Type = Gauge32
_AslqDataAvgBytesPerRead_Object = MibScalar
aslqDataAvgBytesPerRead = _AslqDataAvgBytesPerRead_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 6),
    _AslqDataAvgBytesPerRead_Type()
)
aslqDataAvgBytesPerRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqDataAvgBytesPerRead.setStatus("current")
_AslqDataAvgBytesPerRow_Type = Gauge32
_AslqDataAvgBytesPerRow_Object = MibScalar
aslqDataAvgBytesPerRow = _AslqDataAvgBytesPerRow_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 7),
    _AslqDataAvgBytesPerRow_Type()
)
aslqDataAvgBytesPerRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqDataAvgBytesPerRow.setStatus("current")
_AslqDataAvgRowsPerRead_Type = Gauge32
_AslqDataAvgRowsPerRead_Object = MibScalar
aslqDataAvgRowsPerRead = _AslqDataAvgRowsPerRead_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 8),
    _AslqDataAvgRowsPerRead_Type()
)
aslqDataAvgRowsPerRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqDataAvgRowsPerRead.setStatus("current")
_AslqDataBytes_Type = Gauge32
_AslqDataBytes_Object = MibScalar
aslqDataBytes = _AslqDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 9),
    _AslqDataBytes_Type()
)
aslqDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqDataBytes.setStatus("current")
_AslqDataReads_Type = Gauge32
_AslqDataReads_Object = MibScalar
aslqDataReads = _AslqDataReads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 10),
    _AslqDataReads_Type()
)
aslqDataReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqDataReads.setStatus("current")
_AslqIndexBytes_Type = Gauge32
_AslqIndexBytes_Object = MibScalar
aslqIndexBytes = _AslqIndexBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 11),
    _AslqIndexBytes_Type()
)
aslqIndexBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqIndexBytes.setStatus("current")
_AslqIndexReads_Type = Gauge32
_AslqIndexReads_Object = MibScalar
aslqIndexReads = _AslqIndexReads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 12),
    _AslqIndexReads_Type()
)
aslqIndexReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqIndexReads.setStatus("current")
_AslqMapBytes_Type = Gauge32
_AslqMapBytes_Object = MibScalar
aslqMapBytes = _AslqMapBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 13),
    _AslqMapBytes_Type()
)
aslqMapBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqMapBytes.setStatus("current")
_AslqMapReads_Type = Gauge32
_AslqMapReads_Object = MibScalar
aslqMapReads = _AslqMapReads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 14),
    _AslqMapReads_Type()
)
aslqMapReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqMapReads.setStatus("current")
_AslqQueryNum_Type = Gauge32
_AslqQueryNum_Object = MibScalar
aslqQueryNum = _AslqQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 15),
    _AslqQueryNum_Type()
)
aslqQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqQueryNum.setStatus("current")
_AslqRowsCreated_Type = Gauge32
_AslqRowsCreated_Object = MibScalar
aslqRowsCreated = _AslqRowsCreated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 16),
    _AslqRowsCreated_Type()
)
aslqRowsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqRowsCreated.setStatus("current")
_AslqRowsFilterExcluded_Type = Gauge32
_AslqRowsFilterExcluded_Object = MibScalar
aslqRowsFilterExcluded = _AslqRowsFilterExcluded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 17),
    _AslqRowsFilterExcluded_Type()
)
aslqRowsFilterExcluded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqRowsFilterExcluded.setStatus("current")
_AslqRowsFilterIncluded_Type = Gauge32
_AslqRowsFilterIncluded_Object = MibScalar
aslqRowsFilterIncluded = _AslqRowsFilterIncluded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 18),
    _AslqRowsFilterIncluded_Type()
)
aslqRowsFilterIncluded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqRowsFilterIncluded.setStatus("current")
_AslqRowsFiltered_Type = Gauge32
_AslqRowsFiltered_Object = MibScalar
aslqRowsFiltered = _AslqRowsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 19),
    _AslqRowsFiltered_Type()
)
aslqRowsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqRowsFiltered.setStatus("current")
_AslqRowsRead_Type = Gauge32
_AslqRowsRead_Object = MibScalar
aslqRowsRead = _AslqRowsRead_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 20),
    _AslqRowsRead_Type()
)
aslqRowsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqRowsRead.setStatus("current")
_AslqTimeMs_Type = Gauge32
_AslqTimeMs_Object = MibScalar
aslqTimeMs = _AslqTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 21),
    _AslqTimeMs_Type()
)
aslqTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqTimeMs.setStatus("current")
_AslqTotalBytes_Type = Gauge32
_AslqTotalBytes_Object = MibScalar
aslqTotalBytes = _AslqTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 22),
    _AslqTotalBytes_Type()
)
aslqTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqTotalBytes.setStatus("current")
_AslqTotalReads_Type = Gauge32
_AslqTotalReads_Object = MibScalar
aslqTotalReads = _AslqTotalReads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 3, 23),
    _AslqTotalReads_Type()
)
aslqTotalReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslqTotalReads.setStatus("current")
_AnalysisServerLocks_ObjectIdentity = ObjectIdentity
analysisServerLocks = _AnalysisServerLocks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 4)
)
if mibBuilder.loadTexts:
    analysisServerLocks.setStatus("current")
_AslCurrentLatchWaits_Type = Gauge32
_AslCurrentLatchWaits_Object = MibScalar
aslCurrentLatchWaits = _AslCurrentLatchWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 4, 1),
    _AslCurrentLatchWaits_Type()
)
aslCurrentLatchWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslCurrentLatchWaits.setStatus("current")
_AslCurrentLockWaits_Type = Gauge32
_AslCurrentLockWaits_Object = MibScalar
aslCurrentLockWaits = _AslCurrentLockWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 4, 2),
    _AslCurrentLockWaits_Type()
)
aslCurrentLockWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslCurrentLockWaits.setStatus("current")
_AslCurrentLocks_Type = Gauge32
_AslCurrentLocks_Object = MibScalar
aslCurrentLocks = _AslCurrentLocks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 4, 3),
    _AslCurrentLocks_Type()
)
aslCurrentLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslCurrentLocks.setStatus("current")
_AslLatchWaitsPerSec_Type = Gauge32
_AslLatchWaitsPerSec_Object = MibScalar
aslLatchWaitsPerSec = _AslLatchWaitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 4, 4),
    _AslLatchWaitsPerSec_Type()
)
aslLatchWaitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslLatchWaitsPerSec.setStatus("current")
_AslLockDenialsPerSec_Type = Gauge32
_AslLockDenialsPerSec_Object = MibScalar
aslLockDenialsPerSec = _AslLockDenialsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 4, 5),
    _AslLockDenialsPerSec_Type()
)
aslLockDenialsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslLockDenialsPerSec.setStatus("current")
_AslLockGrantsPerSec_Type = Gauge32
_AslLockGrantsPerSec_Object = MibScalar
aslLockGrantsPerSec = _AslLockGrantsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 4, 6),
    _AslLockGrantsPerSec_Type()
)
aslLockGrantsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslLockGrantsPerSec.setStatus("current")
_AslLockRequestsPerSec_Type = Gauge32
_AslLockRequestsPerSec_Object = MibScalar
aslLockRequestsPerSec = _AslLockRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 4, 7),
    _AslLockRequestsPerSec_Type()
)
aslLockRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslLockRequestsPerSec.setStatus("current")
_AslLockWaitsPerSec_Type = Gauge32
_AslLockWaitsPerSec_Object = MibScalar
aslLockWaitsPerSec = _AslLockWaitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 4, 8),
    _AslLockWaitsPerSec_Type()
)
aslLockWaitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslLockWaitsPerSec.setStatus("current")
_AslUnlockRequestsPerSec_Type = Gauge32
_AslUnlockRequestsPerSec_Object = MibScalar
aslUnlockRequestsPerSec = _AslUnlockRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 4, 9),
    _AslUnlockRequestsPerSec_Type()
)
aslUnlockRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aslUnlockRequestsPerSec.setStatus("current")
_AnalysisServerProc_ObjectIdentity = ObjectIdentity
analysisServerProc = _AnalysisServerProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5)
)
if mibBuilder.loadTexts:
    analysisServerProc.setStatus("current")
_AspCurrentPartitions_Type = Gauge32
_AspCurrentPartitions_Object = MibScalar
aspCurrentPartitions = _AspCurrentPartitions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5, 1),
    _AspCurrentPartitions_Type()
)
aspCurrentPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspCurrentPartitions.setStatus("current")
_AspCurrentThreads_Type = Gauge32
_AspCurrentThreads_Object = MibScalar
aspCurrentThreads = _AspCurrentThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5, 2),
    _AspCurrentThreads_Type()
)
aspCurrentThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspCurrentThreads.setStatus("current")
_AspCurrentThreadsMerging_Type = Gauge32
_AspCurrentThreadsMerging_Object = MibScalar
aspCurrentThreadsMerging = _AspCurrentThreadsMerging_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5, 3),
    _AspCurrentThreadsMerging_Type()
)
aspCurrentThreadsMerging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspCurrentThreadsMerging.setStatus("current")
_AspCurrentThreadsReading_Type = Gauge32
_AspCurrentThreadsReading_Object = MibScalar
aspCurrentThreadsReading = _AspCurrentThreadsReading_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5, 4),
    _AspCurrentThreadsReading_Type()
)
aspCurrentThreadsReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspCurrentThreadsReading.setStatus("current")
_AspCurrentThreadsWriting_Type = Gauge32
_AspCurrentThreadsWriting_Object = MibScalar
aspCurrentThreadsWriting = _AspCurrentThreadsWriting_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5, 5),
    _AspCurrentThreadsWriting_Type()
)
aspCurrentThreadsWriting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspCurrentThreadsWriting.setStatus("current")
_AspFileBytesWrittenPerSec_Type = Gauge32
_AspFileBytesWrittenPerSec_Object = MibScalar
aspFileBytesWrittenPerSec = _AspFileBytesWrittenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5, 6),
    _AspFileBytesWrittenPerSec_Type()
)
aspFileBytesWrittenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspFileBytesWrittenPerSec.setStatus("current")
_AspFileRowsWrittenPerSec_Type = Gauge32
_AspFileRowsWrittenPerSec_Object = MibScalar
aspFileRowsWrittenPerSec = _AspFileRowsWrittenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5, 7),
    _AspFileRowsWrittenPerSec_Type()
)
aspFileRowsWrittenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspFileRowsWrittenPerSec.setStatus("current")
_AspMemorySizeBytes_Type = Gauge32
_AspMemorySizeBytes_Object = MibScalar
aspMemorySizeBytes = _AspMemorySizeBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5, 8),
    _AspMemorySizeBytes_Type()
)
aspMemorySizeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspMemorySizeBytes.setStatus("current")
_AspMemorySizeRows_Type = Gauge32
_AspMemorySizeRows_Object = MibScalar
aspMemorySizeRows = _AspMemorySizeRows_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5, 9),
    _AspMemorySizeRows_Type()
)
aspMemorySizeRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspMemorySizeRows.setStatus("current")
_AspRowsCreatedPerSec_Type = Gauge32
_AspRowsCreatedPerSec_Object = MibScalar
aspRowsCreatedPerSec = _AspRowsCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5, 10),
    _AspRowsCreatedPerSec_Type()
)
aspRowsCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspRowsCreatedPerSec.setStatus("current")
_AspRowsMergedPerSec_Type = Gauge32
_AspRowsMergedPerSec_Object = MibScalar
aspRowsMergedPerSec = _AspRowsMergedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5, 11),
    _AspRowsMergedPerSec_Type()
)
aspRowsMergedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspRowsMergedPerSec.setStatus("current")
_AspRowsReadPerSec_Type = Gauge32
_AspRowsReadPerSec_Object = MibScalar
aspRowsReadPerSec = _AspRowsReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5, 12),
    _AspRowsReadPerSec_Type()
)
aspRowsReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspRowsReadPerSec.setStatus("current")
_AspTotalPartitions_Type = Gauge32
_AspTotalPartitions_Object = MibScalar
aspTotalPartitions = _AspTotalPartitions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5, 13),
    _AspTotalPartitions_Type()
)
aspTotalPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspTotalPartitions.setStatus("current")
_AspTotalRows_Type = Gauge32
_AspTotalRows_Object = MibScalar
aspTotalRows = _AspTotalRows_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 5, 14),
    _AspTotalRows_Type()
)
aspTotalRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspTotalRows.setStatus("current")
_AnalysisServerProcAggs_ObjectIdentity = ObjectIdentity
analysisServerProcAggs = _AnalysisServerProcAggs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 6)
)
if mibBuilder.loadTexts:
    analysisServerProcAggs.setStatus("current")
_AspaCurrentPartitions_Type = Gauge32
_AspaCurrentPartitions_Object = MibScalar
aspaCurrentPartitions = _AspaCurrentPartitions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 6, 1),
    _AspaCurrentPartitions_Type()
)
aspaCurrentPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspaCurrentPartitions.setStatus("current")
_AspaMemorySizeBytes_Type = Gauge32
_AspaMemorySizeBytes_Object = MibScalar
aspaMemorySizeBytes = _AspaMemorySizeBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 6, 2),
    _AspaMemorySizeBytes_Type()
)
aspaMemorySizeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspaMemorySizeBytes.setStatus("current")
_AspaMemorySizeRows_Type = Gauge32
_AspaMemorySizeRows_Object = MibScalar
aspaMemorySizeRows = _AspaMemorySizeRows_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 6, 3),
    _AspaMemorySizeRows_Type()
)
aspaMemorySizeRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspaMemorySizeRows.setStatus("current")
_AspaRowsCreatedPerSec_Type = Gauge32
_AspaRowsCreatedPerSec_Object = MibScalar
aspaRowsCreatedPerSec = _AspaRowsCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 6, 4),
    _AspaRowsCreatedPerSec_Type()
)
aspaRowsCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspaRowsCreatedPerSec.setStatus("current")
_AspaRowsMergedPerSec_Type = Gauge32
_AspaRowsMergedPerSec_Object = MibScalar
aspaRowsMergedPerSec = _AspaRowsMergedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 6, 5),
    _AspaRowsMergedPerSec_Type()
)
aspaRowsMergedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspaRowsMergedPerSec.setStatus("current")
_AspaTempFileBytesWrittenPerSec_Type = Gauge32
_AspaTempFileBytesWrittenPerSec_Object = MibScalar
aspaTempFileBytesWrittenPerSec = _AspaTempFileBytesWrittenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 6, 6),
    _AspaTempFileBytesWrittenPerSec_Type()
)
aspaTempFileBytesWrittenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspaTempFileBytesWrittenPerSec.setStatus("current")
_AspaTempFileRowsWrittenPerSec_Type = Gauge32
_AspaTempFileRowsWrittenPerSec_Object = MibScalar
aspaTempFileRowsWrittenPerSec = _AspaTempFileRowsWrittenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 6, 7),
    _AspaTempFileRowsWrittenPerSec_Type()
)
aspaTempFileRowsWrittenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspaTempFileRowsWrittenPerSec.setStatus("current")
_AspaTotalPartitions_Type = Gauge32
_AspaTotalPartitions_Object = MibScalar
aspaTotalPartitions = _AspaTotalPartitions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 6, 8),
    _AspaTotalPartitions_Type()
)
aspaTotalPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspaTotalPartitions.setStatus("current")
_AnalysisServerProcIndexes_ObjectIdentity = ObjectIdentity
analysisServerProcIndexes = _AnalysisServerProcIndexes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 7)
)
if mibBuilder.loadTexts:
    analysisServerProcIndexes.setStatus("current")
_AspiCurrentPartitions_Type = Gauge32
_AspiCurrentPartitions_Object = MibScalar
aspiCurrentPartitions = _AspiCurrentPartitions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 7, 1),
    _AspiCurrentPartitions_Type()
)
aspiCurrentPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspiCurrentPartitions.setStatus("current")
_AspiRowsPerSec_Type = Gauge32
_AspiRowsPerSec_Object = MibScalar
aspiRowsPerSec = _AspiRowsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 7, 2),
    _AspiRowsPerSec_Type()
)
aspiRowsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspiRowsPerSec.setStatus("current")
_AspiTotalPartitions_Type = Gauge32
_AspiTotalPartitions_Object = MibScalar
aspiTotalPartitions = _AspiTotalPartitions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 7, 3),
    _AspiTotalPartitions_Type()
)
aspiTotalPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspiTotalPartitions.setStatus("current")
_AspiTotalRows_Type = Gauge32
_AspiTotalRows_Object = MibScalar
aspiTotalRows = _AspiTotalRows_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 7, 4),
    _AspiTotalRows_Type()
)
aspiTotalRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspiTotalRows.setStatus("current")
_AnalysisServerQuery_ObjectIdentity = ObjectIdentity
analysisServerQuery = _AnalysisServerQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8)
)
if mibBuilder.loadTexts:
    analysisServerQuery.setStatus("current")
_AsqAvgTimePerQuery_Type = Gauge32
_AsqAvgTimePerQuery_Object = MibScalar
asqAvgTimePerQuery = _AsqAvgTimePerQuery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 1),
    _AsqAvgTimePerQuery_Type()
)
asqAvgTimePerQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqAvgTimePerQuery.setStatus("current")
_AsqBytesSentPerSec_Type = Gauge32
_AsqBytesSentPerSec_Object = MibScalar
asqBytesSentPerSec = _AsqBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 2),
    _AsqBytesSentPerSec_Type()
)
asqBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqBytesSentPerSec.setStatus("current")
_AsqCurrentProcessThreadPool_Type = Gauge32
_AsqCurrentProcessThreadPool_Object = MibScalar
asqCurrentProcessThreadPool = _AsqCurrentProcessThreadPool_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 3),
    _AsqCurrentProcessThreadPool_Type()
)
asqCurrentProcessThreadPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqCurrentProcessThreadPool.setStatus("current")
_AsqCurrentProcessThreadQueueLen_Type = Gauge32
_AsqCurrentProcessThreadQueueLen_Object = MibScalar
asqCurrentProcessThreadQueueLen = _AsqCurrentProcessThreadQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 4),
    _AsqCurrentProcessThreadQueueLen_Type()
)
asqCurrentProcessThreadQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqCurrentProcessThreadQueueLen.setStatus("current")
_AsqCurrentProcessThreadsActive_Type = Gauge32
_AsqCurrentProcessThreadsActive_Object = MibScalar
asqCurrentProcessThreadsActive = _AsqCurrentProcessThreadsActive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 5),
    _AsqCurrentProcessThreadsActive_Type()
)
asqCurrentProcessThreadsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqCurrentProcessThreadsActive.setStatus("current")
_AsqCurrentPyramidOperations_Type = Gauge32
_AsqCurrentPyramidOperations_Object = MibScalar
asqCurrentPyramidOperations = _AsqCurrentPyramidOperations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 6),
    _AsqCurrentPyramidOperations_Type()
)
asqCurrentPyramidOperations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqCurrentPyramidOperations.setStatus("current")
_AsqCurrentQueries_Type = Gauge32
_AsqCurrentQueries_Object = MibScalar
asqCurrentQueries = _AsqCurrentQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 7),
    _AsqCurrentQueries_Type()
)
asqCurrentQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqCurrentQueries.setStatus("current")
_AsqCurrentThreads_Type = Gauge32
_AsqCurrentThreads_Object = MibScalar
asqCurrentThreads = _AsqCurrentThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 8),
    _AsqCurrentThreads_Type()
)
asqCurrentThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqCurrentThreads.setStatus("current")
_AsqCurrentWorkerThreadPool_Type = Gauge32
_AsqCurrentWorkerThreadPool_Object = MibScalar
asqCurrentWorkerThreadPool = _AsqCurrentWorkerThreadPool_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 9),
    _AsqCurrentWorkerThreadPool_Type()
)
asqCurrentWorkerThreadPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqCurrentWorkerThreadPool.setStatus("current")
_AsqCurrentWorkerThreadsActive_Type = Gauge32
_AsqCurrentWorkerThreadsActive_Object = MibScalar
asqCurrentWorkerThreadsActive = _AsqCurrentWorkerThreadsActive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 10),
    _AsqCurrentWorkerThreadsActive_Type()
)
asqCurrentWorkerThreadsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqCurrentWorkerThreadsActive.setStatus("current")
_AsqDataBytesPerSec_Type = Gauge32
_AsqDataBytesPerSec_Object = MibScalar
asqDataBytesPerSec = _AsqDataBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 11),
    _AsqDataBytesPerSec_Type()
)
asqDataBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqDataBytesPerSec.setStatus("current")
_AsqDataReadsPerSec_Type = Gauge32
_AsqDataReadsPerSec_Object = MibScalar
asqDataReadsPerSec = _AsqDataReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 12),
    _AsqDataReadsPerSec_Type()
)
asqDataReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqDataReadsPerSec.setStatus("current")
_AsqFilterRowsExcludedPerSec_Type = Gauge32
_AsqFilterRowsExcludedPerSec_Object = MibScalar
asqFilterRowsExcludedPerSec = _AsqFilterRowsExcludedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 13),
    _AsqFilterRowsExcludedPerSec_Type()
)
asqFilterRowsExcludedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqFilterRowsExcludedPerSec.setStatus("current")
_AsqFilterRowsIncludedPerSec_Type = Gauge32
_AsqFilterRowsIncludedPerSec_Object = MibScalar
asqFilterRowsIncludedPerSec = _AsqFilterRowsIncludedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 14),
    _AsqFilterRowsIncludedPerSec_Type()
)
asqFilterRowsIncludedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqFilterRowsIncludedPerSec.setStatus("current")
_AsqFilteredRowsPerSec_Type = Gauge32
_AsqFilteredRowsPerSec_Object = MibScalar
asqFilteredRowsPerSec = _AsqFilteredRowsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 15),
    _AsqFilteredRowsPerSec_Type()
)
asqFilteredRowsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqFilteredRowsPerSec.setStatus("current")
_AsqIndexBytesPerSec_Type = Gauge32
_AsqIndexBytesPerSec_Object = MibScalar
asqIndexBytesPerSec = _AsqIndexBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 16),
    _AsqIndexBytesPerSec_Type()
)
asqIndexBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqIndexBytesPerSec.setStatus("current")
_AsqIndexReadsPerSec_Type = Gauge32
_AsqIndexReadsPerSec_Object = MibScalar
asqIndexReadsPerSec = _AsqIndexReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 17),
    _AsqIndexReadsPerSec_Type()
)
asqIndexReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqIndexReadsPerSec.setStatus("current")
_AsqMapBytesPerSec_Type = Gauge32
_AsqMapBytesPerSec_Object = MibScalar
asqMapBytesPerSec = _AsqMapBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 18),
    _AsqMapBytesPerSec_Type()
)
asqMapBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqMapBytesPerSec.setStatus("current")
_AsqMapReadsPerSec_Type = Gauge32
_AsqMapReadsPerSec_Object = MibScalar
asqMapReadsPerSec = _AsqMapReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 19),
    _AsqMapReadsPerSec_Type()
)
asqMapReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqMapReadsPerSec.setStatus("current")
_AsqNetworkRoundTripsPerSec_Type = Gauge32
_AsqNetworkRoundTripsPerSec_Object = MibScalar
asqNetworkRoundTripsPerSec = _AsqNetworkRoundTripsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 20),
    _AsqNetworkRoundTripsPerSec_Type()
)
asqNetworkRoundTripsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqNetworkRoundTripsPerSec.setStatus("current")
_AsqPyramidOperationsPerSec_Type = Gauge32
_AsqPyramidOperationsPerSec_Object = MibScalar
asqPyramidOperationsPerSec = _AsqPyramidOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 21),
    _AsqPyramidOperationsPerSec_Type()
)
asqPyramidOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqPyramidOperationsPerSec.setStatus("current")
_AsqQueriesAnsweredPerSec_Type = Gauge32
_AsqQueriesAnsweredPerSec_Object = MibScalar
asqQueriesAnsweredPerSec = _AsqQueriesAnsweredPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 22),
    _AsqQueriesAnsweredPerSec_Type()
)
asqQueriesAnsweredPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqQueriesAnsweredPerSec.setStatus("current")
_AsqQueriesFromCacheDirectPerSec_Type = Gauge32
_AsqQueriesFromCacheDirectPerSec_Object = MibScalar
asqQueriesFromCacheDirectPerSec = _AsqQueriesFromCacheDirectPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 23),
    _AsqQueriesFromCacheDirectPerSec_Type()
)
asqQueriesFromCacheDirectPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqQueriesFromCacheDirectPerSec.setStatus("current")
_AsqQueriesFromCacheFilterPerSec_Type = Gauge32
_AsqQueriesFromCacheFilterPerSec_Object = MibScalar
asqQueriesFromCacheFilterPerSec = _AsqQueriesFromCacheFilterPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 24),
    _AsqQueriesFromCacheFilterPerSec_Type()
)
asqQueriesFromCacheFilterPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqQueriesFromCacheFilterPerSec.setStatus("current")
_AsqQueriesFromFilePerSec_Type = Gauge32
_AsqQueriesFromFilePerSec_Object = MibScalar
asqQueriesFromFilePerSec = _AsqQueriesFromFilePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 25),
    _AsqQueriesFromFilePerSec_Type()
)
asqQueriesFromFilePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqQueriesFromFilePerSec.setStatus("current")
_AsqQueriesRequestedPerSec_Type = Gauge32
_AsqQueriesRequestedPerSec_Object = MibScalar
asqQueriesRequestedPerSec = _AsqQueriesRequestedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 26),
    _AsqQueriesRequestedPerSec_Type()
)
asqQueriesRequestedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqQueriesRequestedPerSec.setStatus("current")
_AsqRowsReadPerSec_Type = Gauge32
_AsqRowsReadPerSec_Object = MibScalar
asqRowsReadPerSec = _AsqRowsReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 27),
    _AsqRowsReadPerSec_Type()
)
asqRowsReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqRowsReadPerSec.setStatus("current")
_AsqRowsSentPerSec_Type = Gauge32
_AsqRowsSentPerSec_Object = MibScalar
asqRowsSentPerSec = _AsqRowsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 28),
    _AsqRowsSentPerSec_Type()
)
asqRowsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqRowsSentPerSec.setStatus("current")
_AsqTotalBytesSent_Type = Gauge32
_AsqTotalBytesSent_Object = MibScalar
asqTotalBytesSent = _AsqTotalBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 29),
    _AsqTotalBytesSent_Type()
)
asqTotalBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqTotalBytesSent.setStatus("current")
_AsqTotalNetworkRoundTrips_Type = Gauge32
_AsqTotalNetworkRoundTrips_Object = MibScalar
asqTotalNetworkRoundTrips = _AsqTotalNetworkRoundTrips_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 30),
    _AsqTotalNetworkRoundTrips_Type()
)
asqTotalNetworkRoundTrips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqTotalNetworkRoundTrips.setStatus("current")
_AsqTotalPyramidOperations_Type = Gauge32
_AsqTotalPyramidOperations_Object = MibScalar
asqTotalPyramidOperations = _AsqTotalPyramidOperations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 31),
    _AsqTotalPyramidOperations_Type()
)
asqTotalPyramidOperations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqTotalPyramidOperations.setStatus("current")
_AsqTotalQueriesAnswered_Type = Gauge32
_AsqTotalQueriesAnswered_Object = MibScalar
asqTotalQueriesAnswered = _AsqTotalQueriesAnswered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 32),
    _AsqTotalQueriesAnswered_Type()
)
asqTotalQueriesAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqTotalQueriesAnswered.setStatus("current")
_AsqTotalQueriesFromCacheDirect_Type = Gauge32
_AsqTotalQueriesFromCacheDirect_Object = MibScalar
asqTotalQueriesFromCacheDirect = _AsqTotalQueriesFromCacheDirect_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 33),
    _AsqTotalQueriesFromCacheDirect_Type()
)
asqTotalQueriesFromCacheDirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqTotalQueriesFromCacheDirect.setStatus("current")
_AsqTotalQueriesFromCacheFiltered_Type = Gauge32
_AsqTotalQueriesFromCacheFiltered_Object = MibScalar
asqTotalQueriesFromCacheFiltered = _AsqTotalQueriesFromCacheFiltered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 34),
    _AsqTotalQueriesFromCacheFiltered_Type()
)
asqTotalQueriesFromCacheFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqTotalQueriesFromCacheFiltered.setStatus("current")
_AsqTotalQueriesFromFile_Type = Gauge32
_AsqTotalQueriesFromFile_Object = MibScalar
asqTotalQueriesFromFile = _AsqTotalQueriesFromFile_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 35),
    _AsqTotalQueriesFromFile_Type()
)
asqTotalQueriesFromFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqTotalQueriesFromFile.setStatus("current")
_AsqTotalQueriesRequested_Type = Gauge32
_AsqTotalQueriesRequested_Object = MibScalar
asqTotalQueriesRequested = _AsqTotalQueriesRequested_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 36),
    _AsqTotalQueriesRequested_Type()
)
asqTotalQueriesRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqTotalQueriesRequested.setStatus("current")
_AsqTotalRowsSent_Type = Gauge32
_AsqTotalRowsSent_Object = MibScalar
asqTotalRowsSent = _AsqTotalRowsSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 8, 37),
    _AsqTotalRowsSent_Type()
)
asqTotalRowsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqTotalRowsSent.setStatus("current")
_AnalysisServerQueryDims_ObjectIdentity = ObjectIdentity
analysisServerQueryDims = _AnalysisServerQueryDims_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 9)
)
if mibBuilder.loadTexts:
    analysisServerQueryDims.setStatus("current")
_AsqdBytesPerSec_Type = Gauge32
_AsqdBytesPerSec_Object = MibScalar
asqdBytesPerSec = _AsqdBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 9, 1),
    _AsqdBytesPerSec_Type()
)
asqdBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqdBytesPerSec.setStatus("current")
_AsqdCurrentRequests_Type = Gauge32
_AsqdCurrentRequests_Object = MibScalar
asqdCurrentRequests = _AsqdCurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 9, 2),
    _AsqdCurrentRequests_Type()
)
asqdCurrentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqdCurrentRequests.setStatus("current")
_AsqdMembersPerSec_Type = Gauge32
_AsqdMembersPerSec_Object = MibScalar
asqdMembersPerSec = _AsqdMembersPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 9, 3),
    _AsqdMembersPerSec_Type()
)
asqdMembersPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqdMembersPerSec.setStatus("current")
_AsqdRequestsPerSec_Type = Gauge32
_AsqdRequestsPerSec_Object = MibScalar
asqdRequestsPerSec = _AsqdRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 9, 4),
    _AsqdRequestsPerSec_Type()
)
asqdRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqdRequestsPerSec.setStatus("current")
_AsqdTotalVLDMRequests_Type = Gauge32
_AsqdTotalVLDMRequests_Object = MibScalar
asqdTotalVLDMRequests = _AsqdTotalVLDMRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 9, 5),
    _AsqdTotalVLDMRequests_Type()
)
asqdTotalVLDMRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqdTotalVLDMRequests.setStatus("current")
_AsqdTotalBytes_Type = Gauge32
_AsqdTotalBytes_Object = MibScalar
asqdTotalBytes = _AsqdTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 9, 6),
    _AsqdTotalBytes_Type()
)
asqdTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqdTotalBytes.setStatus("current")
_AsqdTotalMembers_Type = Gauge32
_AsqdTotalMembers_Object = MibScalar
asqdTotalMembers = _AsqdTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 9, 7),
    _AsqdTotalMembers_Type()
)
asqdTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqdTotalMembers.setStatus("current")
_AsqdTotalRequests_Type = Gauge32
_AsqdTotalRequests_Object = MibScalar
asqdTotalRequests = _AsqdTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 9, 8),
    _AsqdTotalRequests_Type()
)
asqdTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqdTotalRequests.setStatus("current")
_AsqdVLDMRequestsPerSec_Type = Gauge32
_AsqdVLDMRequestsPerSec_Object = MibScalar
asqdVLDMRequestsPerSec = _AsqdVLDMRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 9, 9),
    _AsqdVLDMRequestsPerSec_Type()
)
asqdVLDMRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asqdVLDMRequestsPerSec.setStatus("current")
_AnalysisServerStartup_ObjectIdentity = ObjectIdentity
analysisServerStartup = _AnalysisServerStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 10)
)
if mibBuilder.loadTexts:
    analysisServerStartup.setStatus("current")
_AssBytesPerSec_Type = Gauge32
_AssBytesPerSec_Object = MibScalar
assBytesPerSec = _AssBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 10, 1),
    _AssBytesPerSec_Type()
)
assBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assBytesPerSec.setStatus("current")
_AssMembersPerSec_Type = Gauge32
_AssMembersPerSec_Object = MibScalar
assMembersPerSec = _AssMembersPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 10, 2),
    _AssMembersPerSec_Type()
)
assMembersPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assMembersPerSec.setStatus("current")
_AssPropertiesPerSec_Type = Gauge32
_AssPropertiesPerSec_Object = MibScalar
assPropertiesPerSec = _AssPropertiesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 10, 3),
    _AssPropertiesPerSec_Type()
)
assPropertiesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assPropertiesPerSec.setStatus("current")
_AssServerUptime_Type = Gauge32
_AssServerUptime_Object = MibScalar
assServerUptime = _AssServerUptime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 10, 4),
    _AssServerUptime_Type()
)
assServerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assServerUptime.setStatus("current")
_AssTotalBytes_Type = Gauge32
_AssTotalBytes_Object = MibScalar
assTotalBytes = _AssTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 10, 5),
    _AssTotalBytes_Type()
)
assTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assTotalBytes.setStatus("current")
_AssTotalDimensions_Type = Gauge32
_AssTotalDimensions_Object = MibScalar
assTotalDimensions = _AssTotalDimensions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 10, 6),
    _AssTotalDimensions_Type()
)
assTotalDimensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assTotalDimensions.setStatus("current")
_AssTotalMembers_Type = Gauge32
_AssTotalMembers_Object = MibScalar
assTotalMembers = _AssTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 10, 7),
    _AssTotalMembers_Type()
)
assTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assTotalMembers.setStatus("current")
_AssTotalProperties_Type = Gauge32
_AssTotalProperties_Object = MibScalar
assTotalProperties = _AssTotalProperties_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 10, 8),
    _AssTotalProperties_Type()
)
assTotalProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assTotalProperties.setStatus("current")
_MicrosoftGatherer_ObjectIdentity = ObjectIdentity
microsoftGatherer = _MicrosoftGatherer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11)
)
_MgAccessingRobotsTxtFile_Type = Gauge32
_MgAccessingRobotsTxtFile_Object = MibScalar
mgAccessingRobotsTxtFile = _MgAccessingRobotsTxtFile_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 1),
    _MgAccessingRobotsTxtFile_Type()
)
mgAccessingRobotsTxtFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgAccessingRobotsTxtFile.setStatus("current")
_MgActiveQueueLength_Type = Gauge32
_MgActiveQueueLength_Object = MibScalar
mgActiveQueueLength = _MgActiveQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 2),
    _MgActiveQueueLength_Type()
)
mgActiveQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgActiveQueueLength.setStatus("current")
_MgAdminClients_Type = Gauge32
_MgAdminClients_Object = MibScalar
mgAdminClients = _MgAdminClients_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 3),
    _MgAdminClients_Type()
)
mgAdminClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgAdminClients.setStatus("current")
_MgAllNotificationsReceived_Type = Gauge32
_MgAllNotificationsReceived_Object = MibScalar
mgAllNotificationsReceived = _MgAllNotificationsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 4),
    _MgAllNotificationsReceived_Type()
)
mgAllNotificationsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgAllNotificationsReceived.setStatus("current")
_MgDelayedDocuments_Type = Gauge32
_MgDelayedDocuments_Object = MibScalar
mgDelayedDocuments = _MgDelayedDocuments_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 5),
    _MgDelayedDocuments_Type()
)
mgDelayedDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgDelayedDocuments.setStatus("current")
_MgDocumentEntries_Type = Gauge32
_MgDocumentEntries_Object = MibScalar
mgDocumentEntries = _MgDocumentEntries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 6),
    _MgDocumentEntries_Type()
)
mgDocumentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgDocumentEntries.setStatus("current")
_MgDocumentsDelayedRetry_Type = Gauge32
_MgDocumentsDelayedRetry_Object = MibScalar
mgDocumentsDelayedRetry = _MgDocumentsDelayedRetry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 7),
    _MgDocumentsDelayedRetry_Type()
)
mgDocumentsDelayedRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgDocumentsDelayedRetry.setStatus("current")
_MgDocumentsFiltered_Type = Gauge32
_MgDocumentsFiltered_Object = MibScalar
mgDocumentsFiltered = _MgDocumentsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 8),
    _MgDocumentsFiltered_Type()
)
mgDocumentsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgDocumentsFiltered.setStatus("current")
_MgDocumentsFilteredRate_Type = Gauge32
_MgDocumentsFilteredRate_Object = MibScalar
mgDocumentsFilteredRate = _MgDocumentsFilteredRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 9),
    _MgDocumentsFilteredRate_Type()
)
mgDocumentsFilteredRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgDocumentsFilteredRate.setStatus("current")
_MgDocumentsSuccessfullyFiltered_Type = Gauge32
_MgDocumentsSuccessfullyFiltered_Object = MibScalar
mgDocumentsSuccessfullyFiltered = _MgDocumentsSuccessfullyFiltered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 10),
    _MgDocumentsSuccessfullyFiltered_Type()
)
mgDocumentsSuccessfullyFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgDocumentsSuccessfullyFiltered.setStatus("current")
_MgDocumentsSuccessfulFilterRate_Type = Gauge32
_MgDocumentsSuccessfulFilterRate_Object = MibScalar
mgDocumentsSuccessfulFilterRate = _MgDocumentsSuccessfulFilterRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 11),
    _MgDocumentsSuccessfulFilterRate_Type()
)
mgDocumentsSuccessfulFilterRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgDocumentsSuccessfulFilterRate.setStatus("current")
_MgExtNotificationsRate_Type = Gauge32
_MgExtNotificationsRate_Object = MibScalar
mgExtNotificationsRate = _MgExtNotificationsRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 12),
    _MgExtNotificationsRate_Type()
)
mgExtNotificationsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgExtNotificationsRate.setStatus("current")
_MgExtNotificationsReceived_Type = Gauge32
_MgExtNotificationsReceived_Object = MibScalar
mgExtNotificationsReceived = _MgExtNotificationsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 13),
    _MgExtNotificationsReceived_Type()
)
mgExtNotificationsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgExtNotificationsReceived.setStatus("current")
_MgFilterObjects_Type = Gauge32
_MgFilterObjects_Object = MibScalar
mgFilterObjects = _MgFilterObjects_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 14),
    _MgFilterObjects_Type()
)
mgFilterObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgFilterObjects.setStatus("current")
_MgFilterProcessCreated_Type = Gauge32
_MgFilterProcessCreated_Object = MibScalar
mgFilterProcessCreated = _MgFilterProcessCreated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 15),
    _MgFilterProcessCreated_Type()
)
mgFilterProcessCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgFilterProcessCreated.setStatus("current")
_MgFilterProcesses_Type = Gauge32
_MgFilterProcesses_Object = MibScalar
mgFilterProcesses = _MgFilterProcesses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 16),
    _MgFilterProcesses_Type()
)
mgFilterProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgFilterProcesses.setStatus("current")
_MgFilterProcessesMax_Type = Gauge32
_MgFilterProcessesMax_Object = MibScalar
mgFilterProcessesMax = _MgFilterProcessesMax_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 17),
    _MgFilterProcessesMax_Type()
)
mgFilterProcessesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgFilterProcessesMax.setStatus("current")
_MgFilteringThreads_Type = Gauge32
_MgFilteringThreads_Object = MibScalar
mgFilteringThreads = _MgFilteringThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 18),
    _MgFilteringThreads_Type()
)
mgFilteringThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgFilteringThreads.setStatus("current")
_MgHeartbeats_Type = Gauge32
_MgHeartbeats_Object = MibScalar
mgHeartbeats = _MgHeartbeats_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 19),
    _MgHeartbeats_Type()
)
mgHeartbeats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgHeartbeats.setStatus("current")
_MgHeartbeatsRate_Type = Gauge32
_MgHeartbeatsRate_Object = MibScalar
mgHeartbeatsRate = _MgHeartbeatsRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 20),
    _MgHeartbeatsRate_Type()
)
mgHeartbeatsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgHeartbeatsRate.setStatus("current")
_MgIdleThreads_Type = Gauge32
_MgIdleThreads_Object = MibScalar
mgIdleThreads = _MgIdleThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 21),
    _MgIdleThreads_Type()
)
mgIdleThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgIdleThreads.setStatus("current")
_MgNotificationSources_Type = Gauge32
_MgNotificationSources_Object = MibScalar
mgNotificationSources = _MgNotificationSources_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 22),
    _MgNotificationSources_Type()
)
mgNotificationSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNotificationSources.setStatus("current")
_MgNotificationsRate_Type = Gauge32
_MgNotificationsRate_Object = MibScalar
mgNotificationsRate = _MgNotificationsRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 23),
    _MgNotificationsRate_Type()
)
mgNotificationsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNotificationsRate.setStatus("current")
_MgPerformanceLevel_Type = Gauge32
_MgPerformanceLevel_Object = MibScalar
mgPerformanceLevel = _MgPerformanceLevel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 24),
    _MgPerformanceLevel_Type()
)
mgPerformanceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgPerformanceLevel.setStatus("current")
_MgReasonToBackOff_Type = Gauge32
_MgReasonToBackOff_Object = MibScalar
mgReasonToBackOff = _MgReasonToBackOff_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 25),
    _MgReasonToBackOff_Type()
)
mgReasonToBackOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgReasonToBackOff.setStatus("current")
_MgRobotsTxtRequests_Type = Gauge32
_MgRobotsTxtRequests_Object = MibScalar
mgRobotsTxtRequests = _MgRobotsTxtRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 26),
    _MgRobotsTxtRequests_Type()
)
mgRobotsTxtRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgRobotsTxtRequests.setStatus("current")
_MgServerObjects_Type = Gauge32
_MgServerObjects_Object = MibScalar
mgServerObjects = _MgServerObjects_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 27),
    _MgServerObjects_Type()
)
mgServerObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgServerObjects.setStatus("current")
_MgServerObjectsCreated_Type = Gauge32
_MgServerObjectsCreated_Object = MibScalar
mgServerObjectsCreated = _MgServerObjectsCreated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 28),
    _MgServerObjectsCreated_Type()
)
mgServerObjectsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgServerObjectsCreated.setStatus("current")
_MgServersCurrentlyUnavailable_Type = Gauge32
_MgServersCurrentlyUnavailable_Object = MibScalar
mgServersCurrentlyUnavailable = _MgServersCurrentlyUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 29),
    _MgServersCurrentlyUnavailable_Type()
)
mgServersCurrentlyUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgServersCurrentlyUnavailable.setStatus("current")
_MgServersUnavailable_Type = Gauge32
_MgServersUnavailable_Object = MibScalar
mgServersUnavailable = _MgServersUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 30),
    _MgServersUnavailable_Type()
)
mgServersUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgServersUnavailable.setStatus("current")
_MgStemmersCached_Type = Gauge32
_MgStemmersCached_Object = MibScalar
mgStemmersCached = _MgStemmersCached_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 31),
    _MgStemmersCached_Type()
)
mgStemmersCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgStemmersCached.setStatus("current")
_MgSystemIOTrafficRate_Type = Gauge32
_MgSystemIOTrafficRate_Object = MibScalar
mgSystemIOTrafficRate = _MgSystemIOTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 32),
    _MgSystemIOTrafficRate_Type()
)
mgSystemIOTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgSystemIOTrafficRate.setStatus("current")
_MgThreadsAccessingNetwork_Type = Gauge32
_MgThreadsAccessingNetwork_Object = MibScalar
mgThreadsAccessingNetwork = _MgThreadsAccessingNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 33),
    _MgThreadsAccessingNetwork_Type()
)
mgThreadsAccessingNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgThreadsAccessingNetwork.setStatus("current")
_MgThreadsInPlugIns_Type = Gauge32
_MgThreadsInPlugIns_Object = MibScalar
mgThreadsInPlugIns = _MgThreadsInPlugIns_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 34),
    _MgThreadsInPlugIns_Type()
)
mgThreadsInPlugIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgThreadsInPlugIns.setStatus("current")
_MgThreadsBlockedDueToBackOff_Type = Gauge32
_MgThreadsBlockedDueToBackOff_Object = MibScalar
mgThreadsBlockedDueToBackOff = _MgThreadsBlockedDueToBackOff_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 35),
    _MgThreadsBlockedDueToBackOff_Type()
)
mgThreadsBlockedDueToBackOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgThreadsBlockedDueToBackOff.setStatus("current")
_MgTimeOuts_Type = Gauge32
_MgTimeOuts_Object = MibScalar
mgTimeOuts = _MgTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 36),
    _MgTimeOuts_Type()
)
mgTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgTimeOuts.setStatus("current")
_MgWordBreakersCached_Type = Gauge32
_MgWordBreakersCached_Object = MibScalar
mgWordBreakersCached = _MgWordBreakersCached_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 11, 37),
    _MgWordBreakersCached_Type()
)
mgWordBreakersCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgWordBreakersCached.setStatus("current")
_MicrosoftGathererProjectsTable_Object = MibTable
microsoftGathererProjectsTable = _MicrosoftGathererProjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12)
)
if mibBuilder.loadTexts:
    microsoftGathererProjectsTable.setStatus("current")
_MicrosoftGathererProjectsEntry_Object = MibTableRow
microsoftGathererProjectsEntry = _MicrosoftGathererProjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1)
)
microsoftGathererProjectsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "mgpInstance"),
)
if mibBuilder.loadTexts:
    microsoftGathererProjectsEntry.setStatus("current")
_MgpInstance_Type = InstanceName
_MgpInstance_Object = MibTableColumn
mgpInstance = _MgpInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 1),
    _MgpInstance_Type()
)
mgpInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpInstance.setStatus("current")
_MgpAccessedFileRate_Type = Gauge32
_MgpAccessedFileRate_Object = MibTableColumn
mgpAccessedFileRate = _MgpAccessedFileRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 2),
    _MgpAccessedFileRate_Type()
)
mgpAccessedFileRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpAccessedFileRate.setStatus("current")
_MgpAccessedFiles_Type = Gauge32
_MgpAccessedFiles_Object = MibTableColumn
mgpAccessedFiles = _MgpAccessedFiles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 3),
    _MgpAccessedFiles_Type()
)
mgpAccessedFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpAccessedFiles.setStatus("current")
_MgpAccessedHTTP_Type = Gauge32
_MgpAccessedHTTP_Object = MibTableColumn
mgpAccessedHTTP = _MgpAccessedHTTP_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 4),
    _MgpAccessedHTTP_Type()
)
mgpAccessedHTTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpAccessedHTTP.setStatus("current")
_MgpAccessedHTTPRate_Type = Gauge32
_MgpAccessedHTTPRate_Object = MibTableColumn
mgpAccessedHTTPRate = _MgpAccessedHTTPRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 5),
    _MgpAccessedHTTPRate_Type()
)
mgpAccessedHTTPRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpAccessedHTTPRate.setStatus("current")
_MgpAdaptiveCrawlAccepts_Type = Gauge32
_MgpAdaptiveCrawlAccepts_Object = MibTableColumn
mgpAdaptiveCrawlAccepts = _MgpAdaptiveCrawlAccepts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 6),
    _MgpAdaptiveCrawlAccepts_Type()
)
mgpAdaptiveCrawlAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpAdaptiveCrawlAccepts.setStatus("current")
_MgpAdaptiveCrawlErrorSamples_Type = Gauge32
_MgpAdaptiveCrawlErrorSamples_Object = MibTableColumn
mgpAdaptiveCrawlErrorSamples = _MgpAdaptiveCrawlErrorSamples_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 7),
    _MgpAdaptiveCrawlErrorSamples_Type()
)
mgpAdaptiveCrawlErrorSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpAdaptiveCrawlErrorSamples.setStatus("current")
_MgpAdaptiveCrawlErrors_Type = Gauge32
_MgpAdaptiveCrawlErrors_Object = MibTableColumn
mgpAdaptiveCrawlErrors = _MgpAdaptiveCrawlErrors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 8),
    _MgpAdaptiveCrawlErrors_Type()
)
mgpAdaptiveCrawlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpAdaptiveCrawlErrors.setStatus("current")
_MgpAdaptiveCrawlExcludes_Type = Gauge32
_MgpAdaptiveCrawlExcludes_Object = MibTableColumn
mgpAdaptiveCrawlExcludes = _MgpAdaptiveCrawlExcludes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 9),
    _MgpAdaptiveCrawlExcludes_Type()
)
mgpAdaptiveCrawlExcludes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpAdaptiveCrawlExcludes.setStatus("current")
_MgpAdaptiveCrawlFalsePositives_Type = Gauge32
_MgpAdaptiveCrawlFalsePositives_Object = MibTableColumn
mgpAdaptiveCrawlFalsePositives = _MgpAdaptiveCrawlFalsePositives_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 10),
    _MgpAdaptiveCrawlFalsePositives_Type()
)
mgpAdaptiveCrawlFalsePositives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpAdaptiveCrawlFalsePositives.setStatus("current")
_MgpAdaptiveCrawlTotal_Type = Gauge32
_MgpAdaptiveCrawlTotal_Object = MibTableColumn
mgpAdaptiveCrawlTotal = _MgpAdaptiveCrawlTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 11),
    _MgpAdaptiveCrawlTotal_Type()
)
mgpAdaptiveCrawlTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpAdaptiveCrawlTotal.setStatus("current")
_MgpChangedDocuments_Type = Gauge32
_MgpChangedDocuments_Object = MibTableColumn
mgpChangedDocuments = _MgpChangedDocuments_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 12),
    _MgpChangedDocuments_Type()
)
mgpChangedDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpChangedDocuments.setStatus("current")
_MgpDelayedDocuments_Type = Gauge32
_MgpDelayedDocuments_Object = MibTableColumn
mgpDelayedDocuments = _MgpDelayedDocuments_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 13),
    _MgpDelayedDocuments_Type()
)
mgpDelayedDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpDelayedDocuments.setStatus("current")
_MgpDocumentAddRate_Type = Gauge32
_MgpDocumentAddRate_Object = MibTableColumn
mgpDocumentAddRate = _MgpDocumentAddRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 14),
    _MgpDocumentAddRate_Type()
)
mgpDocumentAddRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpDocumentAddRate.setStatus("current")
_MgpDocumentAdditions_Type = Gauge32
_MgpDocumentAdditions_Object = MibTableColumn
mgpDocumentAdditions = _MgpDocumentAdditions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 15),
    _MgpDocumentAdditions_Type()
)
mgpDocumentAdditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpDocumentAdditions.setStatus("current")
_MgpDocumentDeleteRate_Type = Gauge32
_MgpDocumentDeleteRate_Object = MibTableColumn
mgpDocumentDeleteRate = _MgpDocumentDeleteRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 16),
    _MgpDocumentDeleteRate_Type()
)
mgpDocumentDeleteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpDocumentDeleteRate.setStatus("current")
_MgpDocumentDeletes_Type = Gauge32
_MgpDocumentDeletes_Object = MibTableColumn
mgpDocumentDeletes = _MgpDocumentDeletes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 17),
    _MgpDocumentDeletes_Type()
)
mgpDocumentDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpDocumentDeletes.setStatus("current")
_MgpDocumentModifies_Type = Gauge32
_MgpDocumentModifies_Object = MibTableColumn
mgpDocumentModifies = _MgpDocumentModifies_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 18),
    _MgpDocumentModifies_Type()
)
mgpDocumentModifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpDocumentModifies.setStatus("current")
_MgpDocumentModifiesRate_Type = Gauge32
_MgpDocumentModifiesRate_Object = MibTableColumn
mgpDocumentModifiesRate = _MgpDocumentModifiesRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 19),
    _MgpDocumentModifiesRate_Type()
)
mgpDocumentModifiesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpDocumentModifiesRate.setStatus("current")
_MgpDocumentMoveAndRenameRate_Type = Gauge32
_MgpDocumentMoveAndRenameRate_Object = MibTableColumn
mgpDocumentMoveAndRenameRate = _MgpDocumentMoveAndRenameRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 20),
    _MgpDocumentMoveAndRenameRate_Type()
)
mgpDocumentMoveAndRenameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpDocumentMoveAndRenameRate.setStatus("current")
_MgpDocumentMovesPerRenames_Type = Gauge32
_MgpDocumentMovesPerRenames_Object = MibTableColumn
mgpDocumentMovesPerRenames = _MgpDocumentMovesPerRenames_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 21),
    _MgpDocumentMovesPerRenames_Type()
)
mgpDocumentMovesPerRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpDocumentMovesPerRenames.setStatus("current")
_MgpDocumentsInProgress_Type = Gauge32
_MgpDocumentsInProgress_Object = MibTableColumn
mgpDocumentsInProgress = _MgpDocumentsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 22),
    _MgpDocumentsInProgress_Type()
)
mgpDocumentsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpDocumentsInProgress.setStatus("current")
_MgpDocumentsOnHold_Type = Gauge32
_MgpDocumentsOnHold_Object = MibTableColumn
mgpDocumentsOnHold = _MgpDocumentsOnHold_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 23),
    _MgpDocumentsOnHold_Type()
)
mgpDocumentsOnHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpDocumentsOnHold.setStatus("current")
_MgpErrorRate_Type = Gauge32
_MgpErrorRate_Object = MibTableColumn
mgpErrorRate = _MgpErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 24),
    _MgpErrorRate_Type()
)
mgpErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpErrorRate.setStatus("current")
_MgpFileErrors_Type = Gauge32
_MgpFileErrors_Object = MibTableColumn
mgpFileErrors = _MgpFileErrors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 25),
    _MgpFileErrors_Type()
)
mgpFileErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpFileErrors.setStatus("current")
_MgpFileErrorsRate_Type = Gauge32
_MgpFileErrorsRate_Object = MibTableColumn
mgpFileErrorsRate = _MgpFileErrorsRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 26),
    _MgpFileErrorsRate_Type()
)
mgpFileErrorsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpFileErrorsRate.setStatus("current")
_MgpFilteredHTML_Type = Gauge32
_MgpFilteredHTML_Object = MibTableColumn
mgpFilteredHTML = _MgpFilteredHTML_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 27),
    _MgpFilteredHTML_Type()
)
mgpFilteredHTML.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpFilteredHTML.setStatus("current")
_MgpFilteredHTMLRate_Type = Gauge32
_MgpFilteredHTMLRate_Object = MibTableColumn
mgpFilteredHTMLRate = _MgpFilteredHTMLRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 28),
    _MgpFilteredHTMLRate_Type()
)
mgpFilteredHTMLRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpFilteredHTMLRate.setStatus("current")
_MgpFilteredOffice_Type = Gauge32
_MgpFilteredOffice_Object = MibTableColumn
mgpFilteredOffice = _MgpFilteredOffice_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 29),
    _MgpFilteredOffice_Type()
)
mgpFilteredOffice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpFilteredOffice.setStatus("current")
_MgpFilteredOfficeRate_Type = Gauge32
_MgpFilteredOfficeRate_Object = MibTableColumn
mgpFilteredOfficeRate = _MgpFilteredOfficeRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 30),
    _MgpFilteredOfficeRate_Type()
)
mgpFilteredOfficeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpFilteredOfficeRate.setStatus("current")
_MgpFilteredText_Type = Gauge32
_MgpFilteredText_Object = MibTableColumn
mgpFilteredText = _MgpFilteredText_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 31),
    _MgpFilteredText_Type()
)
mgpFilteredText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpFilteredText.setStatus("current")
_MgpFilteredTextRate_Type = Gauge32
_MgpFilteredTextRate_Object = MibTableColumn
mgpFilteredTextRate = _MgpFilteredTextRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 32),
    _MgpFilteredTextRate_Type()
)
mgpFilteredTextRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpFilteredTextRate.setStatus("current")
_MgpFilteringDocuments_Type = Gauge32
_MgpFilteringDocuments_Object = MibTableColumn
mgpFilteringDocuments = _MgpFilteringDocuments_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 33),
    _MgpFilteringDocuments_Type()
)
mgpFilteringDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpFilteringDocuments.setStatus("current")
_MgpGathererPausedFlag_Type = Gauge32
_MgpGathererPausedFlag_Object = MibTableColumn
mgpGathererPausedFlag = _MgpGathererPausedFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 34),
    _MgpGathererPausedFlag_Type()
)
mgpGathererPausedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpGathererPausedFlag.setStatus("current")
_MgpHTTPErrors_Type = Gauge32
_MgpHTTPErrors_Object = MibTableColumn
mgpHTTPErrors = _MgpHTTPErrors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 35),
    _MgpHTTPErrors_Type()
)
mgpHTTPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpHTTPErrors.setStatus("current")
_MgpHTTPErrorsRate_Type = Gauge32
_MgpHTTPErrorsRate_Object = MibTableColumn
mgpHTTPErrorsRate = _MgpHTTPErrorsRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 36),
    _MgpHTTPErrorsRate_Type()
)
mgpHTTPErrorsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpHTTPErrorsRate.setStatus("current")
_MgpHistoryRecoveryProgress_Type = Gauge32
_MgpHistoryRecoveryProgress_Object = MibTableColumn
mgpHistoryRecoveryProgress = _MgpHistoryRecoveryProgress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 37),
    _MgpHistoryRecoveryProgress_Type()
)
mgpHistoryRecoveryProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpHistoryRecoveryProgress.setStatus("current")
_MgpIterateHistoryInProgressFlag_Type = Gauge32
_MgpIterateHistoryInProgressFlag_Object = MibTableColumn
mgpIterateHistoryInProgressFlag = _MgpIterateHistoryInProgressFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 38),
    _MgpIterateHistoryInProgressFlag_Type()
)
mgpIterateHistoryInProgressFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpIterateHistoryInProgressFlag.setStatus("current")
_MgpNotModified_Type = Gauge32
_MgpNotModified_Object = MibTableColumn
mgpNotModified = _MgpNotModified_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 39),
    _MgpNotModified_Type()
)
mgpNotModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpNotModified.setStatus("current")
_MgpProcessedDocuments_Type = Gauge32
_MgpProcessedDocuments_Object = MibTableColumn
mgpProcessedDocuments = _MgpProcessedDocuments_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 40),
    _MgpProcessedDocuments_Type()
)
mgpProcessedDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpProcessedDocuments.setStatus("current")
_MgpProcessedDocumentsRate_Type = Gauge32
_MgpProcessedDocumentsRate_Object = MibTableColumn
mgpProcessedDocumentsRate = _MgpProcessedDocumentsRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 41),
    _MgpProcessedDocumentsRate_Type()
)
mgpProcessedDocumentsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpProcessedDocumentsRate.setStatus("current")
_MgpRecoveryInProgressFlag_Type = Gauge32
_MgpRecoveryInProgressFlag_Object = MibTableColumn
mgpRecoveryInProgressFlag = _MgpRecoveryInProgressFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 42),
    _MgpRecoveryInProgressFlag_Type()
)
mgpRecoveryInProgressFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpRecoveryInProgressFlag.setStatus("current")
_MgpRetries_Type = Gauge32
_MgpRetries_Object = MibTableColumn
mgpRetries = _MgpRetries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 43),
    _MgpRetries_Type()
)
mgpRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpRetries.setStatus("current")
_MgpRetriesRate_Type = Gauge32
_MgpRetriesRate_Object = MibTableColumn
mgpRetriesRate = _MgpRetriesRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 44),
    _MgpRetriesRate_Type()
)
mgpRetriesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpRetriesRate.setStatus("current")
_MgpStartedDocuments_Type = Gauge32
_MgpStartedDocuments_Object = MibTableColumn
mgpStartedDocuments = _MgpStartedDocuments_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 45),
    _MgpStartedDocuments_Type()
)
mgpStartedDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpStartedDocuments.setStatus("current")
_MgpStatusError_Type = Gauge32
_MgpStatusError_Object = MibTableColumn
mgpStatusError = _MgpStatusError_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 46),
    _MgpStatusError_Type()
)
mgpStatusError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpStatusError.setStatus("current")
_MgpStatusSuccess_Type = Gauge32
_MgpStatusSuccess_Object = MibTableColumn
mgpStatusSuccess = _MgpStatusSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 47),
    _MgpStatusSuccess_Type()
)
mgpStatusSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpStatusSuccess.setStatus("current")
_MgpSuccessRate_Type = Gauge32
_MgpSuccessRate_Object = MibTableColumn
mgpSuccessRate = _MgpSuccessRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 48),
    _MgpSuccessRate_Type()
)
mgpSuccessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpSuccessRate.setStatus("current")
_MgpURLsInHistory_Type = Gauge32
_MgpURLsInHistory_Object = MibTableColumn
mgpURLsInHistory = _MgpURLsInHistory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 49),
    _MgpURLsInHistory_Type()
)
mgpURLsInHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpURLsInHistory.setStatus("current")
_MgpUniqueDocuments_Type = Gauge32
_MgpUniqueDocuments_Object = MibTableColumn
mgpUniqueDocuments = _MgpUniqueDocuments_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 50),
    _MgpUniqueDocuments_Type()
)
mgpUniqueDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpUniqueDocuments.setStatus("current")
_MgpWaitingDocuments_Type = Gauge32
_MgpWaitingDocuments_Object = MibTableColumn
mgpWaitingDocuments = _MgpWaitingDocuments_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 12, 1, 51),
    _MgpWaitingDocuments_Type()
)
mgpWaitingDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgpWaitingDocuments.setStatus("current")
_MicrosoftSearch_ObjectIdentity = ObjectIdentity
microsoftSearch = _MicrosoftSearch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 13)
)
if mibBuilder.loadTexts:
    microsoftSearch.setStatus("current")
_MsActiveThreads_Type = Gauge32
_MsActiveThreads_Object = MibScalar
msActiveThreads = _MsActiveThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 13, 1),
    _MsActiveThreads_Type()
)
msActiveThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msActiveThreads.setStatus("current")
_MsCurrentConnections_Type = Gauge32
_MsCurrentConnections_Object = MibScalar
msCurrentConnections = _MsCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 13, 2),
    _MsCurrentConnections_Type()
)
msCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msCurrentConnections.setStatus("current")
_MsFailedQueries_Type = Gauge32
_MsFailedQueries_Object = MibScalar
msFailedQueries = _MsFailedQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 13, 3),
    _MsFailedQueries_Type()
)
msFailedQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msFailedQueries.setStatus("current")
_MsFailedQueryRate_Type = Gauge32
_MsFailedQueryRate_Object = MibScalar
msFailedQueryRate = _MsFailedQueryRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 13, 4),
    _MsFailedQueryRate_Type()
)
msFailedQueryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msFailedQueryRate.setStatus("current")
_MsQueries_Type = Gauge32
_MsQueries_Object = MibScalar
msQueries = _MsQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 13, 5),
    _MsQueries_Type()
)
msQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msQueries.setStatus("current")
_MsQueryRate_Type = Gauge32
_MsQueryRate_Object = MibScalar
msQueryRate = _MsQueryRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 13, 6),
    _MsQueryRate_Type()
)
msQueryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msQueryRate.setStatus("current")
_MsResultRate_Type = Gauge32
_MsResultRate_Object = MibScalar
msResultRate = _MsResultRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 13, 7),
    _MsResultRate_Type()
)
msResultRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msResultRate.setStatus("current")
_MsResults_Type = Gauge32
_MsResults_Object = MibScalar
msResults = _MsResults_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 13, 8),
    _MsResults_Type()
)
msResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msResults.setStatus("current")
_MsSucceededQueries_Type = Gauge32
_MsSucceededQueries_Object = MibScalar
msSucceededQueries = _MsSucceededQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 13, 9),
    _MsSucceededQueries_Type()
)
msSucceededQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSucceededQueries.setStatus("current")
_MsSucceededQueryRate_Type = Gauge32
_MsSucceededQueryRate_Object = MibScalar
msSucceededQueryRate = _MsSucceededQueryRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 13, 10),
    _MsSucceededQueryRate_Type()
)
msSucceededQueryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSucceededQueryRate.setStatus("current")
_MsThreads_Type = Gauge32
_MsThreads_Object = MibScalar
msThreads = _MsThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 13, 11),
    _MsThreads_Type()
)
msThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msThreads.setStatus("current")
_MicrosoftSearchCatalogsTable_Object = MibTable
microsoftSearchCatalogsTable = _MicrosoftSearchCatalogsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14)
)
if mibBuilder.loadTexts:
    microsoftSearchCatalogsTable.setStatus("current")
_MicrosoftSearchCatalogsEntry_Object = MibTableRow
microsoftSearchCatalogsEntry = _MicrosoftSearchCatalogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14, 1)
)
microsoftSearchCatalogsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "mscInstance"),
)
if mibBuilder.loadTexts:
    microsoftSearchCatalogsEntry.setStatus("current")
_MscInstance_Type = InstanceName
_MscInstance_Object = MibTableColumn
mscInstance = _MscInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14, 1, 1),
    _MscInstance_Type()
)
mscInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscInstance.setStatus("current")
_MscCatalogSizeMBytes_Type = Gauge32
_MscCatalogSizeMBytes_Object = MibTableColumn
mscCatalogSizeMBytes = _MscCatalogSizeMBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14, 1, 2),
    _MscCatalogSizeMBytes_Type()
)
mscCatalogSizeMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscCatalogSizeMBytes.setStatus("current")
_MscFailedQueries_Type = Gauge32
_MscFailedQueries_Object = MibTableColumn
mscFailedQueries = _MscFailedQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14, 1, 3),
    _MscFailedQueries_Type()
)
mscFailedQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFailedQueries.setStatus("current")
_MscFailedQueriesRate_Type = Gauge32
_MscFailedQueriesRate_Object = MibTableColumn
mscFailedQueriesRate = _MscFailedQueriesRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14, 1, 4),
    _MscFailedQueriesRate_Type()
)
mscFailedQueriesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFailedQueriesRate.setStatus("current")
_MscNumberOfDocuments_Type = Gauge32
_MscNumberOfDocuments_Object = MibTableColumn
mscNumberOfDocuments = _MscNumberOfDocuments_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14, 1, 5),
    _MscNumberOfDocuments_Type()
)
mscNumberOfDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNumberOfDocuments.setStatus("current")
_MscPersistentIndexes_Type = Gauge32
_MscPersistentIndexes_Object = MibTableColumn
mscPersistentIndexes = _MscPersistentIndexes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14, 1, 6),
    _MscPersistentIndexes_Type()
)
mscPersistentIndexes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPersistentIndexes.setStatus("current")
_MscQueries_Type = Gauge32
_MscQueries_Object = MibTableColumn
mscQueries = _MscQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14, 1, 7),
    _MscQueries_Type()
)
mscQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscQueries.setStatus("current")
_MscQueriesRate_Type = Gauge32
_MscQueriesRate_Object = MibTableColumn
mscQueriesRate = _MscQueriesRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14, 1, 8),
    _MscQueriesRate_Type()
)
mscQueriesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscQueriesRate.setStatus("current")
_MscResults_Type = Gauge32
_MscResults_Object = MibTableColumn
mscResults = _MscResults_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14, 1, 9),
    _MscResults_Type()
)
mscResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscResults.setStatus("current")
_MscResultsRate_Type = Gauge32
_MscResultsRate_Object = MibTableColumn
mscResultsRate = _MscResultsRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14, 1, 10),
    _MscResultsRate_Type()
)
mscResultsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscResultsRate.setStatus("current")
_MscSuccessfulQueries_Type = Gauge32
_MscSuccessfulQueries_Object = MibTableColumn
mscSuccessfulQueries = _MscSuccessfulQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14, 1, 11),
    _MscSuccessfulQueries_Type()
)
mscSuccessfulQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSuccessfulQueries.setStatus("current")
_MscSuccessfulQueriesRate_Type = Gauge32
_MscSuccessfulQueriesRate_Object = MibTableColumn
mscSuccessfulQueriesRate = _MscSuccessfulQueriesRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14, 1, 12),
    _MscSuccessfulQueriesRate_Type()
)
mscSuccessfulQueriesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSuccessfulQueriesRate.setStatus("current")
_MscUniqueKeys_Type = Gauge32
_MscUniqueKeys_Object = MibTableColumn
mscUniqueKeys = _MscUniqueKeys_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 14, 1, 13),
    _MscUniqueKeys_Type()
)
mscUniqueKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscUniqueKeys.setStatus("current")
_MicrosoftSearchIndexCatalogTable_Object = MibTable
microsoftSearchIndexCatalogTable = _MicrosoftSearchIndexCatalogTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15)
)
if mibBuilder.loadTexts:
    microsoftSearchIndexCatalogTable.setStatus("current")
_MicrosoftSearchIndexCatalogEntry_Object = MibTableRow
microsoftSearchIndexCatalogEntry = _MicrosoftSearchIndexCatalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15, 1)
)
microsoftSearchIndexCatalogEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "msicInstance"),
)
if mibBuilder.loadTexts:
    microsoftSearchIndexCatalogEntry.setStatus("current")
_MsicInstance_Type = InstanceName
_MsicInstance_Object = MibTableColumn
msicInstance = _MsicInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15, 1, 1),
    _MsicInstance_Type()
)
msicInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msicInstance.setStatus("current")
_MsicActiveDocuments_Type = Gauge32
_MsicActiveDocuments_Object = MibTableColumn
msicActiveDocuments = _MsicActiveDocuments_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15, 1, 2),
    _MsicActiveDocuments_Type()
)
msicActiveDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msicActiveDocuments.setStatus("current")
_MsicBuildInProgress_Type = Gauge32
_MsicBuildInProgress_Object = MibTableColumn
msicBuildInProgress = _MsicBuildInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15, 1, 3),
    _MsicBuildInProgress_Type()
)
msicBuildInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msicBuildInProgress.setStatus("current")
_MsicDocumentsFiltered_Type = Gauge32
_MsicDocumentsFiltered_Object = MibTableColumn
msicDocumentsFiltered = _MsicDocumentsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15, 1, 4),
    _MsicDocumentsFiltered_Type()
)
msicDocumentsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msicDocumentsFiltered.setStatus("current")
_MsicDocumentsInProgress_Type = Gauge32
_MsicDocumentsInProgress_Object = MibTableColumn
msicDocumentsInProgress = _MsicDocumentsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15, 1, 5),
    _MsicDocumentsInProgress_Type()
)
msicDocumentsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msicDocumentsInProgress.setStatus("current")
_MsicFilesToBeFiltered_Type = Gauge32
_MsicFilesToBeFiltered_Object = MibTableColumn
msicFilesToBeFiltered = _MsicFilesToBeFiltered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15, 1, 6),
    _MsicFilesToBeFiltered_Type()
)
msicFilesToBeFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msicFilesToBeFiltered.setStatus("current")
_MsicIndexSizeMBytes_Type = Gauge32
_MsicIndexSizeMBytes_Object = MibTableColumn
msicIndexSizeMBytes = _MsicIndexSizeMBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15, 1, 7),
    _MsicIndexSizeMBytes_Type()
)
msicIndexSizeMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msicIndexSizeMBytes.setStatus("current")
_MsicMergeProgress_Type = Gauge32
_MsicMergeProgress_Object = MibTableColumn
msicMergeProgress = _MsicMergeProgress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15, 1, 8),
    _MsicMergeProgress_Type()
)
msicMergeProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msicMergeProgress.setStatus("current")
_MsicNumberOfPropagations_Type = Gauge32
_MsicNumberOfPropagations_Object = MibTableColumn
msicNumberOfPropagations = _MsicNumberOfPropagations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15, 1, 9),
    _MsicNumberOfPropagations_Type()
)
msicNumberOfPropagations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msicNumberOfPropagations.setStatus("current")
_MsicNumberOfDocuments_Type = Gauge32
_MsicNumberOfDocuments_Object = MibTableColumn
msicNumberOfDocuments = _MsicNumberOfDocuments_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15, 1, 10),
    _MsicNumberOfDocuments_Type()
)
msicNumberOfDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msicNumberOfDocuments.setStatus("current")
_MsicPersistentIndexes_Type = Gauge32
_MsicPersistentIndexes_Object = MibTableColumn
msicPersistentIndexes = _MsicPersistentIndexes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15, 1, 11),
    _MsicPersistentIndexes_Type()
)
msicPersistentIndexes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msicPersistentIndexes.setStatus("current")
_MsicUniqueKeys_Type = Gauge32
_MsicUniqueKeys_Object = MibTableColumn
msicUniqueKeys = _MsicUniqueKeys_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15, 1, 12),
    _MsicUniqueKeys_Type()
)
msicUniqueKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msicUniqueKeys.setStatus("current")
_MsicWordlists_Type = Gauge32
_MsicWordlists_Object = MibTableColumn
msicWordlists = _MsicWordlists_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 15, 1, 13),
    _MsicWordlists_Type()
)
msicWordlists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msicWordlists.setStatus("current")
_SqlServerNameTable_Object = MibTable
sqlServerNameTable = _SqlServerNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 16)
)
if mibBuilder.loadTexts:
    sqlServerNameTable.setStatus("current")
_SqlServerNameEntry_Object = MibTableRow
sqlServerNameEntry = _SqlServerNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 16, 1)
)
sqlServerNameEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
)
if mibBuilder.loadTexts:
    sqlServerNameEntry.setStatus("current")


class _SqlServerNameIndex_Type(Integer32):
    """Custom type sqlServerNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SqlServerNameIndex_Type.__name__ = "Integer32"
_SqlServerNameIndex_Object = MibTableColumn
sqlServerNameIndex = _SqlServerNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 16, 1, 1),
    _SqlServerNameIndex_Type()
)
sqlServerNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlServerNameIndex.setStatus("current")
_SqlServerNameInstance_Type = InstanceName
_SqlServerNameInstance_Object = MibTableColumn
sqlServerNameInstance = _SqlServerNameInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 16, 1, 2),
    _SqlServerNameInstance_Type()
)
sqlServerNameInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlServerNameInstance.setStatus("current")
_SqlServerAccessMethodsTable_Object = MibTable
sqlServerAccessMethodsTable = _SqlServerAccessMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17)
)
if mibBuilder.loadTexts:
    sqlServerAccessMethodsTable.setStatus("current")
_SqlServerAccessMethodsEntry_Object = MibTableRow
sqlServerAccessMethodsEntry = _SqlServerAccessMethodsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1)
)
sqlServerAccessMethodsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
)
if mibBuilder.loadTexts:
    sqlServerAccessMethodsEntry.setStatus("current")
_SsamAUCleanupBatchesPerSec_Type = Gauge32
_SsamAUCleanupBatchesPerSec_Object = MibTableColumn
ssamAUCleanupBatchesPerSec = _SsamAUCleanupBatchesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 1),
    _SsamAUCleanupBatchesPerSec_Type()
)
ssamAUCleanupBatchesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamAUCleanupBatchesPerSec.setStatus("current")
_SsamAUCleanupsPerSec_Type = Gauge32
_SsamAUCleanupsPerSec_Object = MibTableColumn
ssamAUCleanupsPerSec = _SsamAUCleanupsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 2),
    _SsamAUCleanupsPerSec_Type()
)
ssamAUCleanupsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamAUCleanupsPerSec.setStatus("current")
_SsamDeferredDroppedRowsets_Type = Gauge32
_SsamDeferredDroppedRowsets_Object = MibTableColumn
ssamDeferredDroppedRowsets = _SsamDeferredDroppedRowsets_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 3),
    _SsamDeferredDroppedRowsets_Type()
)
ssamDeferredDroppedRowsets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamDeferredDroppedRowsets.setStatus("current")
_SsamDeferredDroppedAUs_Type = Gauge32
_SsamDeferredDroppedAUs_Object = MibTableColumn
ssamDeferredDroppedAUs = _SsamDeferredDroppedAUs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 4),
    _SsamDeferredDroppedAUs_Type()
)
ssamDeferredDroppedAUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamDeferredDroppedAUs.setStatus("current")
_SsamDroppedRowsetCleanupsPerSec_Type = Gauge32
_SsamDroppedRowsetCleanupsPerSec_Object = MibTableColumn
ssamDroppedRowsetCleanupsPerSec = _SsamDroppedRowsetCleanupsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 5),
    _SsamDroppedRowsetCleanupsPerSec_Type()
)
ssamDroppedRowsetCleanupsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamDroppedRowsetCleanupsPerSec.setStatus("current")
_SsamDroppedRowsetsSkippedPerSec_Type = Gauge32
_SsamDroppedRowsetsSkippedPerSec_Object = MibTableColumn
ssamDroppedRowsetsSkippedPerSec = _SsamDroppedRowsetsSkippedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 6),
    _SsamDroppedRowsetsSkippedPerSec_Type()
)
ssamDroppedRowsetsSkippedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamDroppedRowsetsSkippedPerSec.setStatus("current")
_SsamExtentDeallocationsPerSec_Type = Gauge32
_SsamExtentDeallocationsPerSec_Object = MibTableColumn
ssamExtentDeallocationsPerSec = _SsamExtentDeallocationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 7),
    _SsamExtentDeallocationsPerSec_Type()
)
ssamExtentDeallocationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamExtentDeallocationsPerSec.setStatus("current")
_SsamExtentsAllocatedPerSec_Type = Gauge32
_SsamExtentsAllocatedPerSec_Object = MibTableColumn
ssamExtentsAllocatedPerSec = _SsamExtentsAllocatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 8),
    _SsamExtentsAllocatedPerSec_Type()
)
ssamExtentsAllocatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamExtentsAllocatedPerSec.setStatus("current")
_SsamFailedAUCleanupBatchesPerSec_Type = Gauge32
_SsamFailedAUCleanupBatchesPerSec_Object = MibTableColumn
ssamFailedAUCleanupBatchesPerSec = _SsamFailedAUCleanupBatchesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 9),
    _SsamFailedAUCleanupBatchesPerSec_Type()
)
ssamFailedAUCleanupBatchesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamFailedAUCleanupBatchesPerSec.setStatus("current")
_SsamFailedLeafPageCookie_Type = Gauge32
_SsamFailedLeafPageCookie_Object = MibTableColumn
ssamFailedLeafPageCookie = _SsamFailedLeafPageCookie_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 10),
    _SsamFailedLeafPageCookie_Type()
)
ssamFailedLeafPageCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamFailedLeafPageCookie.setStatus("current")
_SsamFailedTreePageCookie_Type = Gauge32
_SsamFailedTreePageCookie_Object = MibTableColumn
ssamFailedTreePageCookie = _SsamFailedTreePageCookie_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 11),
    _SsamFailedTreePageCookie_Type()
)
ssamFailedTreePageCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamFailedTreePageCookie.setStatus("current")
_SsamForwardedRecordsPerSec_Type = Gauge32
_SsamForwardedRecordsPerSec_Object = MibTableColumn
ssamForwardedRecordsPerSec = _SsamForwardedRecordsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 12),
    _SsamForwardedRecordsPerSec_Type()
)
ssamForwardedRecordsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamForwardedRecordsPerSec.setStatus("current")
_SsamFreeSpacePageFetchesPerSec_Type = Gauge32
_SsamFreeSpacePageFetchesPerSec_Object = MibTableColumn
ssamFreeSpacePageFetchesPerSec = _SsamFreeSpacePageFetchesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 13),
    _SsamFreeSpacePageFetchesPerSec_Type()
)
ssamFreeSpacePageFetchesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamFreeSpacePageFetchesPerSec.setStatus("current")
_SsamFreeSpaceScansPerSec_Type = Gauge32
_SsamFreeSpaceScansPerSec_Object = MibTableColumn
ssamFreeSpaceScansPerSec = _SsamFreeSpaceScansPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 14),
    _SsamFreeSpaceScansPerSec_Type()
)
ssamFreeSpaceScansPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamFreeSpaceScansPerSec.setStatus("current")
_SsamFullScansPerSec_Type = Gauge32
_SsamFullScansPerSec_Object = MibTableColumn
ssamFullScansPerSec = _SsamFullScansPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 15),
    _SsamFullScansPerSec_Type()
)
ssamFullScansPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamFullScansPerSec.setStatus("current")
_SsamIndexSearchesPerSec_Type = Gauge32
_SsamIndexSearchesPerSec_Object = MibTableColumn
ssamIndexSearchesPerSec = _SsamIndexSearchesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 16),
    _SsamIndexSearchesPerSec_Type()
)
ssamIndexSearchesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamIndexSearchesPerSec.setStatus("current")
_SsamMixedPageAllocationsPerSec_Type = Gauge32
_SsamMixedPageAllocationsPerSec_Object = MibTableColumn
ssamMixedPageAllocationsPerSec = _SsamMixedPageAllocationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 17),
    _SsamMixedPageAllocationsPerSec_Type()
)
ssamMixedPageAllocationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamMixedPageAllocationsPerSec.setStatus("current")
_SsamPageDeallocationsPerSec_Type = Gauge32
_SsamPageDeallocationsPerSec_Object = MibTableColumn
ssamPageDeallocationsPerSec = _SsamPageDeallocationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 18),
    _SsamPageDeallocationsPerSec_Type()
)
ssamPageDeallocationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamPageDeallocationsPerSec.setStatus("current")
_SsamPageSplitsPerSec_Type = Gauge32
_SsamPageSplitsPerSec_Object = MibTableColumn
ssamPageSplitsPerSec = _SsamPageSplitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 19),
    _SsamPageSplitsPerSec_Type()
)
ssamPageSplitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamPageSplitsPerSec.setStatus("current")
_SsamPagesAllocatedPerSec_Type = Gauge32
_SsamPagesAllocatedPerSec_Object = MibTableColumn
ssamPagesAllocatedPerSec = _SsamPagesAllocatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 20),
    _SsamPagesAllocatedPerSec_Type()
)
ssamPagesAllocatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamPagesAllocatedPerSec.setStatus("current")
_SsamProbeScansPerSec_Type = Gauge32
_SsamProbeScansPerSec_Object = MibTableColumn
ssamProbeScansPerSec = _SsamProbeScansPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 21),
    _SsamProbeScansPerSec_Type()
)
ssamProbeScansPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamProbeScansPerSec.setStatus("current")
_SsamRangeScansPerSec_Type = Gauge32
_SsamRangeScansPerSec_Object = MibTableColumn
ssamRangeScansPerSec = _SsamRangeScansPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 22),
    _SsamRangeScansPerSec_Type()
)
ssamRangeScansPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamRangeScansPerSec.setStatus("current")
_SsamScanPointRevalidationsPerSec_Type = Gauge32
_SsamScanPointRevalidationsPerSec_Object = MibTableColumn
ssamScanPointRevalidationsPerSec = _SsamScanPointRevalidationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 23),
    _SsamScanPointRevalidationsPerSec_Type()
)
ssamScanPointRevalidationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamScanPointRevalidationsPerSec.setStatus("current")
_SsamSkippedGhostedRecordsPerSec_Type = Gauge32
_SsamSkippedGhostedRecordsPerSec_Object = MibTableColumn
ssamSkippedGhostedRecordsPerSec = _SsamSkippedGhostedRecordsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 24),
    _SsamSkippedGhostedRecordsPerSec_Type()
)
ssamSkippedGhostedRecordsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamSkippedGhostedRecordsPerSec.setStatus("current")
_SsamTableLockEscalationsPerSec_Type = Gauge32
_SsamTableLockEscalationsPerSec_Object = MibTableColumn
ssamTableLockEscalationsPerSec = _SsamTableLockEscalationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 25),
    _SsamTableLockEscalationsPerSec_Type()
)
ssamTableLockEscalationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamTableLockEscalationsPerSec.setStatus("current")
_SsamUsedLeafPageCookie_Type = Gauge32
_SsamUsedLeafPageCookie_Object = MibTableColumn
ssamUsedLeafPageCookie = _SsamUsedLeafPageCookie_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 26),
    _SsamUsedLeafPageCookie_Type()
)
ssamUsedLeafPageCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamUsedLeafPageCookie.setStatus("current")
_SsamUsedTreePageCookie_Type = Gauge32
_SsamUsedTreePageCookie_Object = MibTableColumn
ssamUsedTreePageCookie = _SsamUsedTreePageCookie_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 27),
    _SsamUsedTreePageCookie_Type()
)
ssamUsedTreePageCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamUsedTreePageCookie.setStatus("current")
_SsamWorkfilesCreatedPerSec_Type = Gauge32
_SsamWorkfilesCreatedPerSec_Object = MibTableColumn
ssamWorkfilesCreatedPerSec = _SsamWorkfilesCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 28),
    _SsamWorkfilesCreatedPerSec_Type()
)
ssamWorkfilesCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamWorkfilesCreatedPerSec.setStatus("current")
_SsamWorktablesCreatedPerSec_Type = Gauge32
_SsamWorktablesCreatedPerSec_Object = MibTableColumn
ssamWorktablesCreatedPerSec = _SsamWorktablesCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 29),
    _SsamWorktablesCreatedPerSec_Type()
)
ssamWorktablesCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamWorktablesCreatedPerSec.setStatus("current")
_SsamWorktablesFromCacheRatio_Type = Gauge32
_SsamWorktablesFromCacheRatio_Object = MibTableColumn
ssamWorktablesFromCacheRatio = _SsamWorktablesFromCacheRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 17, 1, 30),
    _SsamWorktablesFromCacheRatio_Type()
)
ssamWorktablesFromCacheRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssamWorktablesFromCacheRatio.setStatus("current")
_SqlServerBackupDeviceTable_Object = MibTable
sqlServerBackupDeviceTable = _SqlServerBackupDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 18)
)
if mibBuilder.loadTexts:
    sqlServerBackupDeviceTable.setStatus("current")
_SqlServerBackupDeviceEntry_Object = MibTableRow
sqlServerBackupDeviceEntry = _SqlServerBackupDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 18, 1)
)
sqlServerBackupDeviceEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "ssbdInstance"),
)
if mibBuilder.loadTexts:
    sqlServerBackupDeviceEntry.setStatus("current")
_SsbdInstance_Type = InstanceName
_SsbdInstance_Object = MibTableColumn
ssbdInstance = _SsbdInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 18, 1, 1),
    _SsbdInstance_Type()
)
ssbdInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbdInstance.setStatus("current")
_SsbdDeviceThroughputBytesPerSec_Type = Gauge32
_SsbdDeviceThroughputBytesPerSec_Object = MibTableColumn
ssbdDeviceThroughputBytesPerSec = _SsbdDeviceThroughputBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 18, 1, 2),
    _SsbdDeviceThroughputBytesPerSec_Type()
)
ssbdDeviceThroughputBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbdDeviceThroughputBytesPerSec.setStatus("current")
_SqlServerBrokerActivationTable_Object = MibTable
sqlServerBrokerActivationTable = _SqlServerBrokerActivationTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 19)
)
if mibBuilder.loadTexts:
    sqlServerBrokerActivationTable.setStatus("current")
_SqlServerBrokerActivationEntry_Object = MibTableRow
sqlServerBrokerActivationEntry = _SqlServerBrokerActivationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 19, 1)
)
sqlServerBrokerActivationEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "ssbaInstance"),
)
if mibBuilder.loadTexts:
    sqlServerBrokerActivationEntry.setStatus("current")
_SsbaInstance_Type = InstanceName
_SsbaInstance_Object = MibTableColumn
ssbaInstance = _SsbaInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 19, 1, 1),
    _SsbaInstance_Type()
)
ssbaInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbaInstance.setStatus("current")
_SsbaStoredProceduresInvokedPerSec_Type = Gauge32
_SsbaStoredProceduresInvokedPerSec_Object = MibTableColumn
ssbaStoredProceduresInvokedPerSec = _SsbaStoredProceduresInvokedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 19, 1, 2),
    _SsbaStoredProceduresInvokedPerSec_Type()
)
ssbaStoredProceduresInvokedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbaStoredProceduresInvokedPerSec.setStatus("current")
_SsbaTaskLimitReached_Type = Gauge32
_SsbaTaskLimitReached_Object = MibTableColumn
ssbaTaskLimitReached = _SsbaTaskLimitReached_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 19, 1, 3),
    _SsbaTaskLimitReached_Type()
)
ssbaTaskLimitReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbaTaskLimitReached.setStatus("current")
_SsbaTaskLimitReachedPerSec_Type = Gauge32
_SsbaTaskLimitReachedPerSec_Object = MibTableColumn
ssbaTaskLimitReachedPerSec = _SsbaTaskLimitReachedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 19, 1, 4),
    _SsbaTaskLimitReachedPerSec_Type()
)
ssbaTaskLimitReachedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbaTaskLimitReachedPerSec.setStatus("current")
_SsbaTasksAbortedPerSec_Type = Gauge32
_SsbaTasksAbortedPerSec_Object = MibTableColumn
ssbaTasksAbortedPerSec = _SsbaTasksAbortedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 19, 1, 5),
    _SsbaTasksAbortedPerSec_Type()
)
ssbaTasksAbortedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbaTasksAbortedPerSec.setStatus("current")
_SsbaTasksRunning_Type = Gauge32
_SsbaTasksRunning_Object = MibTableColumn
ssbaTasksRunning = _SsbaTasksRunning_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 19, 1, 6),
    _SsbaTasksRunning_Type()
)
ssbaTasksRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbaTasksRunning.setStatus("current")
_SsbaTasksStartedPerSec_Type = Gauge32
_SsbaTasksStartedPerSec_Object = MibTableColumn
ssbaTasksStartedPerSec = _SsbaTasksStartedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 19, 1, 7),
    _SsbaTasksStartedPerSec_Type()
)
ssbaTasksStartedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbaTasksStartedPerSec.setStatus("current")
_SqlServerBrokerStatisticsTable_Object = MibTable
sqlServerBrokerStatisticsTable = _SqlServerBrokerStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20)
)
if mibBuilder.loadTexts:
    sqlServerBrokerStatisticsTable.setStatus("current")
_SqlServerBrokerStatisticsEntry_Object = MibTableRow
sqlServerBrokerStatisticsEntry = _SqlServerBrokerStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1)
)
sqlServerBrokerStatisticsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
)
if mibBuilder.loadTexts:
    sqlServerBrokerStatisticsEntry.setStatus("current")
_SsbsBrokerTransactionRollbacks_Type = Gauge32
_SsbsBrokerTransactionRollbacks_Object = MibTableColumn
ssbsBrokerTransactionRollbacks = _SsbsBrokerTransactionRollbacks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 1),
    _SsbsBrokerTransactionRollbacks_Type()
)
ssbsBrokerTransactionRollbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsBrokerTransactionRollbacks.setStatus("current")
_SsbsDialogTimerEventCount_Type = Gauge32
_SsbsDialogTimerEventCount_Object = MibTableColumn
ssbsDialogTimerEventCount = _SsbsDialogTimerEventCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 2),
    _SsbsDialogTimerEventCount_Type()
)
ssbsDialogTimerEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsDialogTimerEventCount.setStatus("current")
_SsbsEnqueuedLocalMessagesTotal_Type = Gauge32
_SsbsEnqueuedLocalMessagesTotal_Object = MibTableColumn
ssbsEnqueuedLocalMessagesTotal = _SsbsEnqueuedLocalMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 3),
    _SsbsEnqueuedLocalMessagesTotal_Type()
)
ssbsEnqueuedLocalMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsEnqueuedLocalMessagesTotal.setStatus("current")
_SsbsEnqueuedLocalMessagesPerSec_Type = Gauge32
_SsbsEnqueuedLocalMessagesPerSec_Object = MibTableColumn
ssbsEnqueuedLocalMessagesPerSec = _SsbsEnqueuedLocalMessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 4),
    _SsbsEnqueuedLocalMessagesPerSec_Type()
)
ssbsEnqueuedLocalMessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsEnqueuedLocalMessagesPerSec.setStatus("current")
_SsbsEnqueuedMessagesTotal_Type = Gauge32
_SsbsEnqueuedMessagesTotal_Object = MibTableColumn
ssbsEnqueuedMessagesTotal = _SsbsEnqueuedMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 5),
    _SsbsEnqueuedMessagesTotal_Type()
)
ssbsEnqueuedMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsEnqueuedMessagesTotal.setStatus("current")
_SsbsEnqueuedMessagesPerSec_Type = Gauge32
_SsbsEnqueuedMessagesPerSec_Object = MibTableColumn
ssbsEnqueuedMessagesPerSec = _SsbsEnqueuedMessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 6),
    _SsbsEnqueuedMessagesPerSec_Type()
)
ssbsEnqueuedMessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsEnqueuedMessagesPerSec.setStatus("current")
_SsbsEnqueuedTransportMsgFragTot_Type = Gauge32
_SsbsEnqueuedTransportMsgFragTot_Object = MibTableColumn
ssbsEnqueuedTransportMsgFragTot = _SsbsEnqueuedTransportMsgFragTot_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 7),
    _SsbsEnqueuedTransportMsgFragTot_Type()
)
ssbsEnqueuedTransportMsgFragTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsEnqueuedTransportMsgFragTot.setStatus("current")
_SsbsEnqueuedTransportMsgFragsPerSec_Type = Gauge32
_SsbsEnqueuedTransportMsgFragsPerSec_Object = MibTableColumn
ssbsEnqueuedTransportMsgFragsPerSec = _SsbsEnqueuedTransportMsgFragsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 8),
    _SsbsEnqueuedTransportMsgFragsPerSec_Type()
)
ssbsEnqueuedTransportMsgFragsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsEnqueuedTransportMsgFragsPerSec.setStatus("current")
_SsbsEnqueuedTransportMsgsTotal_Type = Gauge32
_SsbsEnqueuedTransportMsgsTotal_Object = MibTableColumn
ssbsEnqueuedTransportMsgsTotal = _SsbsEnqueuedTransportMsgsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 9),
    _SsbsEnqueuedTransportMsgsTotal_Type()
)
ssbsEnqueuedTransportMsgsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsEnqueuedTransportMsgsTotal.setStatus("current")
_SsbsEnqueuedTransportMsgsPerSec_Type = Gauge32
_SsbsEnqueuedTransportMsgsPerSec_Object = MibTableColumn
ssbsEnqueuedTransportMsgsPerSec = _SsbsEnqueuedTransportMsgsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 10),
    _SsbsEnqueuedTransportMsgsPerSec_Type()
)
ssbsEnqueuedTransportMsgsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsEnqueuedTransportMsgsPerSec.setStatus("current")
_SsbsForwardedMessagesTotal_Type = Gauge32
_SsbsForwardedMessagesTotal_Object = MibTableColumn
ssbsForwardedMessagesTotal = _SsbsForwardedMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 11),
    _SsbsForwardedMessagesTotal_Type()
)
ssbsForwardedMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsForwardedMessagesTotal.setStatus("current")
_SsbsForwardedMessagesPerSec_Type = Gauge32
_SsbsForwardedMessagesPerSec_Object = MibTableColumn
ssbsForwardedMessagesPerSec = _SsbsForwardedMessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 12),
    _SsbsForwardedMessagesPerSec_Type()
)
ssbsForwardedMessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsForwardedMessagesPerSec.setStatus("current")
_SsbsForwardedMsgByteTotal_Type = Gauge32
_SsbsForwardedMsgByteTotal_Object = MibTableColumn
ssbsForwardedMsgByteTotal = _SsbsForwardedMsgByteTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 13),
    _SsbsForwardedMsgByteTotal_Type()
)
ssbsForwardedMsgByteTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsForwardedMsgByteTotal.setStatus("current")
_SsbsForwardedMsgBytesPerSec_Type = Gauge32
_SsbsForwardedMsgBytesPerSec_Object = MibTableColumn
ssbsForwardedMsgBytesPerSec = _SsbsForwardedMsgBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 14),
    _SsbsForwardedMsgBytesPerSec_Type()
)
ssbsForwardedMsgBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsForwardedMsgBytesPerSec.setStatus("current")
_SsbsForwardedMsgDiscardedTotal_Type = Gauge32
_SsbsForwardedMsgDiscardedTotal_Object = MibTableColumn
ssbsForwardedMsgDiscardedTotal = _SsbsForwardedMsgDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 15),
    _SsbsForwardedMsgDiscardedTotal_Type()
)
ssbsForwardedMsgDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsForwardedMsgDiscardedTotal.setStatus("current")
_SsbsForwardedMsgsDiscardedPerSec_Type = Gauge32
_SsbsForwardedMsgsDiscardedPerSec_Object = MibTableColumn
ssbsForwardedMsgsDiscardedPerSec = _SsbsForwardedMsgsDiscardedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 16),
    _SsbsForwardedMsgsDiscardedPerSec_Type()
)
ssbsForwardedMsgsDiscardedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsForwardedMsgsDiscardedPerSec.setStatus("current")
_SsbsForwardedPendingMsgBytes_Type = Gauge32
_SsbsForwardedPendingMsgBytes_Object = MibTableColumn
ssbsForwardedPendingMsgBytes = _SsbsForwardedPendingMsgBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 17),
    _SsbsForwardedPendingMsgBytes_Type()
)
ssbsForwardedPendingMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsForwardedPendingMsgBytes.setStatus("current")
_SsbsForwardedPendingMsgCount_Type = Gauge32
_SsbsForwardedPendingMsgCount_Object = MibTableColumn
ssbsForwardedPendingMsgCount = _SsbsForwardedPendingMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 18),
    _SsbsForwardedPendingMsgCount_Type()
)
ssbsForwardedPendingMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsForwardedPendingMsgCount.setStatus("current")
_SsbsSQLRECEIVETotal_Type = Gauge32
_SsbsSQLRECEIVETotal_Object = MibTableColumn
ssbsSQLRECEIVETotal = _SsbsSQLRECEIVETotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 19),
    _SsbsSQLRECEIVETotal_Type()
)
ssbsSQLRECEIVETotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsSQLRECEIVETotal.setStatus("current")
_SsbsSQLRECEIVEsPerSec_Type = Gauge32
_SsbsSQLRECEIVEsPerSec_Object = MibTableColumn
ssbsSQLRECEIVEsPerSec = _SsbsSQLRECEIVEsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 20),
    _SsbsSQLRECEIVEsPerSec_Type()
)
ssbsSQLRECEIVEsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsSQLRECEIVEsPerSec.setStatus("current")
_SsbsSQLSENDTotal_Type = Gauge32
_SsbsSQLSENDTotal_Object = MibTableColumn
ssbsSQLSENDTotal = _SsbsSQLSENDTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 21),
    _SsbsSQLSENDTotal_Type()
)
ssbsSQLSENDTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsSQLSENDTotal.setStatus("current")
_SsbsSQLSENDsPerSec_Type = Gauge32
_SsbsSQLSENDsPerSec_Object = MibTableColumn
ssbsSQLSENDsPerSec = _SsbsSQLSENDsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 22),
    _SsbsSQLSENDsPerSec_Type()
)
ssbsSQLSENDsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsSQLSENDsPerSec.setStatus("current")
_SsbsTransportTimerEventCount_Type = Gauge32
_SsbsTransportTimerEventCount_Object = MibTableColumn
ssbsTransportTimerEventCount = _SsbsTransportTimerEventCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 20, 1, 23),
    _SsbsTransportTimerEventCount_Type()
)
ssbsTransportTimerEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbsTransportTimerEventCount.setStatus("current")
_SqlServerBrokerTransportTable_Object = MibTable
sqlServerBrokerTransportTable = _SqlServerBrokerTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21)
)
if mibBuilder.loadTexts:
    sqlServerBrokerTransportTable.setStatus("current")
_SqlServerBrokerTransportEntry_Object = MibTableRow
sqlServerBrokerTransportEntry = _SqlServerBrokerTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1)
)
sqlServerBrokerTransportEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
)
if mibBuilder.loadTexts:
    sqlServerBrokerTransportEntry.setStatus("current")
_SsbtCurrentBytesForRecvIO_Type = Gauge32
_SsbtCurrentBytesForRecvIO_Object = MibTableColumn
ssbtCurrentBytesForRecvIO = _SsbtCurrentBytesForRecvIO_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 1),
    _SsbtCurrentBytesForRecvIO_Type()
)
ssbtCurrentBytesForRecvIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtCurrentBytesForRecvIO.setStatus("current")
_SsbtCurrentBytesForSendIO_Type = Gauge32
_SsbtCurrentBytesForSendIO_Object = MibTableColumn
ssbtCurrentBytesForSendIO = _SsbtCurrentBytesForSendIO_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 2),
    _SsbtCurrentBytesForSendIO_Type()
)
ssbtCurrentBytesForSendIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtCurrentBytesForSendIO.setStatus("current")
_SsbtCurrentMsgFragsForSendIO_Type = Gauge32
_SsbtCurrentMsgFragsForSendIO_Object = MibTableColumn
ssbtCurrentMsgFragsForSendIO = _SsbtCurrentMsgFragsForSendIO_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 3),
    _SsbtCurrentMsgFragsForSendIO_Type()
)
ssbtCurrentMsgFragsForSendIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtCurrentMsgFragsForSendIO.setStatus("current")
_SsbtMessageFragmentReceiveTotal_Type = Gauge32
_SsbtMessageFragmentReceiveTotal_Object = MibTableColumn
ssbtMessageFragmentReceiveTotal = _SsbtMessageFragmentReceiveTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 4),
    _SsbtMessageFragmentReceiveTotal_Type()
)
ssbtMessageFragmentReceiveTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtMessageFragmentReceiveTotal.setStatus("current")
_SsbtMessageFragmentReceivesPerSec_Type = Gauge32
_SsbtMessageFragmentReceivesPerSec_Object = MibTableColumn
ssbtMessageFragmentReceivesPerSec = _SsbtMessageFragmentReceivesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 5),
    _SsbtMessageFragmentReceivesPerSec_Type()
)
ssbtMessageFragmentReceivesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtMessageFragmentReceivesPerSec.setStatus("current")
_SsbtMessageFragmentSendTotal_Type = Gauge32
_SsbtMessageFragmentSendTotal_Object = MibTableColumn
ssbtMessageFragmentSendTotal = _SsbtMessageFragmentSendTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 6),
    _SsbtMessageFragmentSendTotal_Type()
)
ssbtMessageFragmentSendTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtMessageFragmentSendTotal.setStatus("current")
_SsbtMessageFragmentSendsPerSec_Type = Gauge32
_SsbtMessageFragmentSendsPerSec_Object = MibTableColumn
ssbtMessageFragmentSendsPerSec = _SsbtMessageFragmentSendsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 7),
    _SsbtMessageFragmentSendsPerSec_Type()
)
ssbtMessageFragmentSendsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtMessageFragmentSendsPerSec.setStatus("current")
_SsbtMsgFragmentRecvSizeAvg_Type = Gauge32
_SsbtMsgFragmentRecvSizeAvg_Object = MibTableColumn
ssbtMsgFragmentRecvSizeAvg = _SsbtMsgFragmentRecvSizeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 8),
    _SsbtMsgFragmentRecvSizeAvg_Type()
)
ssbtMsgFragmentRecvSizeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtMsgFragmentRecvSizeAvg.setStatus("current")
_SsbtMsgFragmentSendSizeAvg_Type = Gauge32
_SsbtMsgFragmentSendSizeAvg_Object = MibTableColumn
ssbtMsgFragmentSendSizeAvg = _SsbtMsgFragmentSendSizeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 9),
    _SsbtMsgFragmentSendSizeAvg_Type()
)
ssbtMsgFragmentSendSizeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtMsgFragmentSendSizeAvg.setStatus("current")
_SsbtOpenConnectionCount_Type = Gauge32
_SsbtOpenConnectionCount_Object = MibTableColumn
ssbtOpenConnectionCount = _SsbtOpenConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 10),
    _SsbtOpenConnectionCount_Type()
)
ssbtOpenConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtOpenConnectionCount.setStatus("current")
_SsbtPendingBytesForRecvIO_Type = Gauge32
_SsbtPendingBytesForRecvIO_Object = MibTableColumn
ssbtPendingBytesForRecvIO = _SsbtPendingBytesForRecvIO_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 11),
    _SsbtPendingBytesForRecvIO_Type()
)
ssbtPendingBytesForRecvIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtPendingBytesForRecvIO.setStatus("current")
_SsbtPendingBytesForSendIO_Type = Gauge32
_SsbtPendingBytesForSendIO_Object = MibTableColumn
ssbtPendingBytesForSendIO = _SsbtPendingBytesForSendIO_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 12),
    _SsbtPendingBytesForSendIO_Type()
)
ssbtPendingBytesForSendIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtPendingBytesForSendIO.setStatus("current")
_SsbtPendingMsgFragsForRecvIO_Type = Gauge32
_SsbtPendingMsgFragsForRecvIO_Object = MibTableColumn
ssbtPendingMsgFragsForRecvIO = _SsbtPendingMsgFragsForRecvIO_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 13),
    _SsbtPendingMsgFragsForRecvIO_Type()
)
ssbtPendingMsgFragsForRecvIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtPendingMsgFragsForRecvIO.setStatus("current")
_SsbtPendingMsgFragsForSendIO_Type = Gauge32
_SsbtPendingMsgFragsForSendIO_Object = MibTableColumn
ssbtPendingMsgFragsForSendIO = _SsbtPendingMsgFragsForSendIO_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 14),
    _SsbtPendingMsgFragsForSendIO_Type()
)
ssbtPendingMsgFragsForSendIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtPendingMsgFragsForSendIO.setStatus("current")
_SsbtReceiveIOBytesTotal_Type = Gauge32
_SsbtReceiveIOBytesTotal_Object = MibTableColumn
ssbtReceiveIOBytesTotal = _SsbtReceiveIOBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 15),
    _SsbtReceiveIOBytesTotal_Type()
)
ssbtReceiveIOBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtReceiveIOBytesTotal.setStatus("current")
_SsbtReceiveIOLenAvg_Type = Gauge32
_SsbtReceiveIOLenAvg_Object = MibTableColumn
ssbtReceiveIOLenAvg = _SsbtReceiveIOLenAvg_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 16),
    _SsbtReceiveIOLenAvg_Type()
)
ssbtReceiveIOLenAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtReceiveIOLenAvg.setStatus("current")
_SsbtReceiveIOBytesPerSec_Type = Gauge32
_SsbtReceiveIOBytesPerSec_Object = MibTableColumn
ssbtReceiveIOBytesPerSec = _SsbtReceiveIOBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 17),
    _SsbtReceiveIOBytesPerSec_Type()
)
ssbtReceiveIOBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtReceiveIOBytesPerSec.setStatus("current")
_SsbtReceiveIOsPerSec_Type = Gauge32
_SsbtReceiveIOsPerSec_Object = MibTableColumn
ssbtReceiveIOsPerSec = _SsbtReceiveIOsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 18),
    _SsbtReceiveIOsPerSec_Type()
)
ssbtReceiveIOsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtReceiveIOsPerSec.setStatus("current")
_SsbtSendIOBytesTotal_Type = Gauge32
_SsbtSendIOBytesTotal_Object = MibTableColumn
ssbtSendIOBytesTotal = _SsbtSendIOBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 19),
    _SsbtSendIOBytesTotal_Type()
)
ssbtSendIOBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtSendIOBytesTotal.setStatus("current")
_SsbtSendIOLenAvg_Type = Gauge32
_SsbtSendIOLenAvg_Object = MibTableColumn
ssbtSendIOLenAvg = _SsbtSendIOLenAvg_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 20),
    _SsbtSendIOLenAvg_Type()
)
ssbtSendIOLenAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtSendIOLenAvg.setStatus("current")
_SsbtSendIOBytesPerSec_Type = Gauge32
_SsbtSendIOBytesPerSec_Object = MibTableColumn
ssbtSendIOBytesPerSec = _SsbtSendIOBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 21),
    _SsbtSendIOBytesPerSec_Type()
)
ssbtSendIOBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtSendIOBytesPerSec.setStatus("current")
_SsbtSendIOsPerSec_Type = Gauge32
_SsbtSendIOsPerSec_Object = MibTableColumn
ssbtSendIOsPerSec = _SsbtSendIOsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 21, 1, 22),
    _SsbtSendIOsPerSec_Type()
)
ssbtSendIOsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbtSendIOsPerSec.setStatus("current")
_SqlServerBufferManagerTable_Object = MibTable
sqlServerBufferManagerTable = _SqlServerBufferManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22)
)
if mibBuilder.loadTexts:
    sqlServerBufferManagerTable.setStatus("current")
_SqlServerBufferManagerEntry_Object = MibTableRow
sqlServerBufferManagerEntry = _SqlServerBufferManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1)
)
sqlServerBufferManagerEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
)
if mibBuilder.loadTexts:
    sqlServerBufferManagerEntry.setStatus("current")
_SsbmAWELookupMapsPerSec_Type = Gauge32
_SsbmAWELookupMapsPerSec_Object = MibTableColumn
ssbmAWELookupMapsPerSec = _SsbmAWELookupMapsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 1),
    _SsbmAWELookupMapsPerSec_Type()
)
ssbmAWELookupMapsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmAWELookupMapsPerSec.setStatus("current")
_SsbmAWEStolenMapsPerSec_Type = Gauge32
_SsbmAWEStolenMapsPerSec_Object = MibTableColumn
ssbmAWEStolenMapsPerSec = _SsbmAWEStolenMapsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 2),
    _SsbmAWEStolenMapsPerSec_Type()
)
ssbmAWEStolenMapsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmAWEStolenMapsPerSec.setStatus("current")
_SsbmAWEUnmapCallsPerSec_Type = Gauge32
_SsbmAWEUnmapCallsPerSec_Object = MibTableColumn
ssbmAWEUnmapCallsPerSec = _SsbmAWEUnmapCallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 3),
    _SsbmAWEUnmapCallsPerSec_Type()
)
ssbmAWEUnmapCallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmAWEUnmapCallsPerSec.setStatus("current")
_SsbmAWEUnmapPagesPerSec_Type = Gauge32
_SsbmAWEUnmapPagesPerSec_Object = MibTableColumn
ssbmAWEUnmapPagesPerSec = _SsbmAWEUnmapPagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 4),
    _SsbmAWEUnmapPagesPerSec_Type()
)
ssbmAWEUnmapPagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmAWEUnmapPagesPerSec.setStatus("current")
_SsbmAWEWriteMapsPerSec_Type = Gauge32
_SsbmAWEWriteMapsPerSec_Object = MibTableColumn
ssbmAWEWriteMapsPerSec = _SsbmAWEWriteMapsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 5),
    _SsbmAWEWriteMapsPerSec_Type()
)
ssbmAWEWriteMapsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmAWEWriteMapsPerSec.setStatus("current")
_SsbmBufferCacheHitRatio_Type = Gauge32
_SsbmBufferCacheHitRatio_Object = MibTableColumn
ssbmBufferCacheHitRatio = _SsbmBufferCacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 6),
    _SsbmBufferCacheHitRatio_Type()
)
ssbmBufferCacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmBufferCacheHitRatio.setStatus("current")
_SsbmCheckpointPagesPerSec_Type = Gauge32
_SsbmCheckpointPagesPerSec_Object = MibTableColumn
ssbmCheckpointPagesPerSec = _SsbmCheckpointPagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 7),
    _SsbmCheckpointPagesPerSec_Type()
)
ssbmCheckpointPagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmCheckpointPagesPerSec.setStatus("current")
_SsbmDatabasePages_Type = Gauge32
_SsbmDatabasePages_Object = MibTableColumn
ssbmDatabasePages = _SsbmDatabasePages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 8),
    _SsbmDatabasePages_Type()
)
ssbmDatabasePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmDatabasePages.setStatus("current")
_SsbmFreeListStallsPerSec_Type = Gauge32
_SsbmFreeListStallsPerSec_Object = MibTableColumn
ssbmFreeListStallsPerSec = _SsbmFreeListStallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 9),
    _SsbmFreeListStallsPerSec_Type()
)
ssbmFreeListStallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmFreeListStallsPerSec.setStatus("current")
_SsbmFreePages_Type = Gauge32
_SsbmFreePages_Object = MibTableColumn
ssbmFreePages = _SsbmFreePages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 10),
    _SsbmFreePages_Type()
)
ssbmFreePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmFreePages.setStatus("current")
_SsbmLazyWritesPerSec_Type = Gauge32
_SsbmLazyWritesPerSec_Object = MibTableColumn
ssbmLazyWritesPerSec = _SsbmLazyWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 11),
    _SsbmLazyWritesPerSec_Type()
)
ssbmLazyWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmLazyWritesPerSec.setStatus("current")
_SsbmPageLifeExpectancy_Type = Gauge32
_SsbmPageLifeExpectancy_Object = MibTableColumn
ssbmPageLifeExpectancy = _SsbmPageLifeExpectancy_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 12),
    _SsbmPageLifeExpectancy_Type()
)
ssbmPageLifeExpectancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmPageLifeExpectancy.setStatus("current")
_SsbmPageLookupsPerSec_Type = Gauge32
_SsbmPageLookupsPerSec_Object = MibTableColumn
ssbmPageLookupsPerSec = _SsbmPageLookupsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 13),
    _SsbmPageLookupsPerSec_Type()
)
ssbmPageLookupsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmPageLookupsPerSec.setStatus("current")
_SsbmPageReadsPerSec_Type = Gauge32
_SsbmPageReadsPerSec_Object = MibTableColumn
ssbmPageReadsPerSec = _SsbmPageReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 14),
    _SsbmPageReadsPerSec_Type()
)
ssbmPageReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmPageReadsPerSec.setStatus("current")
_SsbmPageWritesPerSec_Type = Gauge32
_SsbmPageWritesPerSec_Object = MibTableColumn
ssbmPageWritesPerSec = _SsbmPageWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 15),
    _SsbmPageWritesPerSec_Type()
)
ssbmPageWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmPageWritesPerSec.setStatus("current")
_SsbmProcedureCachePages_Type = Gauge32
_SsbmProcedureCachePages_Object = MibTableColumn
ssbmProcedureCachePages = _SsbmProcedureCachePages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 16),
    _SsbmProcedureCachePages_Type()
)
ssbmProcedureCachePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmProcedureCachePages.setStatus("current")
_SsbmReadaheadPagesPerSec_Type = Gauge32
_SsbmReadaheadPagesPerSec_Object = MibTableColumn
ssbmReadaheadPagesPerSec = _SsbmReadaheadPagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 17),
    _SsbmReadaheadPagesPerSec_Type()
)
ssbmReadaheadPagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmReadaheadPagesPerSec.setStatus("current")
_SsbmReservedPages_Type = Gauge32
_SsbmReservedPages_Object = MibTableColumn
ssbmReservedPages = _SsbmReservedPages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 18),
    _SsbmReservedPages_Type()
)
ssbmReservedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmReservedPages.setStatus("current")
_SsbmStolenPages_Type = Gauge32
_SsbmStolenPages_Object = MibTableColumn
ssbmStolenPages = _SsbmStolenPages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 19),
    _SsbmStolenPages_Type()
)
ssbmStolenPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmStolenPages.setStatus("current")
_SsbmTargetPages_Type = Gauge32
_SsbmTargetPages_Object = MibTableColumn
ssbmTargetPages = _SsbmTargetPages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 20),
    _SsbmTargetPages_Type()
)
ssbmTargetPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmTargetPages.setStatus("current")
_SsbmTotalPages_Type = Gauge32
_SsbmTotalPages_Object = MibTableColumn
ssbmTotalPages = _SsbmTotalPages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 22, 1, 21),
    _SsbmTotalPages_Type()
)
ssbmTotalPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbmTotalPages.setStatus("current")
_SqlServerBufferPartitionTable_Object = MibTable
sqlServerBufferPartitionTable = _SqlServerBufferPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 23)
)
if mibBuilder.loadTexts:
    sqlServerBufferPartitionTable.setStatus("current")
_SqlServerBufferPartitionEntry_Object = MibTableRow
sqlServerBufferPartitionEntry = _SqlServerBufferPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 23, 1)
)
sqlServerBufferPartitionEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "ssbpInstance"),
)
if mibBuilder.loadTexts:
    sqlServerBufferPartitionEntry.setStatus("current")
_SsbpInstance_Type = InstanceName
_SsbpInstance_Object = MibTableColumn
ssbpInstance = _SsbpInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 23, 1, 1),
    _SsbpInstance_Type()
)
ssbpInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbpInstance.setStatus("current")
_SsbpFreeListEmptyPerSec_Type = Gauge32
_SsbpFreeListEmptyPerSec_Object = MibTableColumn
ssbpFreeListEmptyPerSec = _SsbpFreeListEmptyPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 23, 1, 2),
    _SsbpFreeListEmptyPerSec_Type()
)
ssbpFreeListEmptyPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbpFreeListEmptyPerSec.setStatus("current")
_SsbpFreeListRequestsPerSec_Type = Gauge32
_SsbpFreeListRequestsPerSec_Object = MibTableColumn
ssbpFreeListRequestsPerSec = _SsbpFreeListRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 23, 1, 3),
    _SsbpFreeListRequestsPerSec_Type()
)
ssbpFreeListRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbpFreeListRequestsPerSec.setStatus("current")
_SsbpFreePages_Type = Gauge32
_SsbpFreePages_Object = MibTableColumn
ssbpFreePages = _SsbpFreePages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 23, 1, 4),
    _SsbpFreePages_Type()
)
ssbpFreePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssbpFreePages.setStatus("current")
_SqlServerCacheManagerTable_Object = MibTable
sqlServerCacheManagerTable = _SqlServerCacheManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 24)
)
if mibBuilder.loadTexts:
    sqlServerCacheManagerTable.setStatus("current")
_SqlServerCacheManagerEntry_Object = MibTableRow
sqlServerCacheManagerEntry = _SqlServerCacheManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 24, 1)
)
sqlServerCacheManagerEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "sscmInstance"),
)
if mibBuilder.loadTexts:
    sqlServerCacheManagerEntry.setStatus("current")
_SscmInstance_Type = InstanceName
_SscmInstance_Object = MibTableColumn
sscmInstance = _SscmInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 24, 1, 1),
    _SscmInstance_Type()
)
sscmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmInstance.setStatus("current")
_SscmCacheHitRatio_Type = Gauge32
_SscmCacheHitRatio_Object = MibTableColumn
sscmCacheHitRatio = _SscmCacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 24, 1, 2),
    _SscmCacheHitRatio_Type()
)
sscmCacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmCacheHitRatio.setStatus("current")
_SscmCacheObjectCounts_Type = Gauge32
_SscmCacheObjectCounts_Object = MibTableColumn
sscmCacheObjectCounts = _SscmCacheObjectCounts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 24, 1, 3),
    _SscmCacheObjectCounts_Type()
)
sscmCacheObjectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmCacheObjectCounts.setStatus("current")
_SscmCachePages_Type = Gauge32
_SscmCachePages_Object = MibTableColumn
sscmCachePages = _SscmCachePages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 24, 1, 4),
    _SscmCachePages_Type()
)
sscmCachePages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmCachePages.setStatus("current")
_SscmCacheUseCountsPerSec_Type = Gauge32
_SscmCacheUseCountsPerSec_Object = MibTableColumn
sscmCacheUseCountsPerSec = _SscmCacheUseCountsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 24, 1, 5),
    _SscmCacheUseCountsPerSec_Type()
)
sscmCacheUseCountsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmCacheUseCountsPerSec.setStatus("current")
_SqlServerCursorManagerTotalTable_Object = MibTable
sqlServerCursorManagerTotalTable = _SqlServerCursorManagerTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 25)
)
if mibBuilder.loadTexts:
    sqlServerCursorManagerTotalTable.setStatus("current")
_SqlServerCursorManagerTotalEntry_Object = MibTableRow
sqlServerCursorManagerTotalEntry = _SqlServerCursorManagerTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 25, 1)
)
sqlServerCursorManagerTotalEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
)
if mibBuilder.loadTexts:
    sqlServerCursorManagerTotalEntry.setStatus("current")
_SscmtAsyncPopulationCount_Type = Gauge32
_SscmtAsyncPopulationCount_Object = MibTableColumn
sscmtAsyncPopulationCount = _SscmtAsyncPopulationCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 25, 1, 1),
    _SscmtAsyncPopulationCount_Type()
)
sscmtAsyncPopulationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmtAsyncPopulationCount.setStatus("current")
_SscmtCursorConversionRate_Type = Gauge32
_SscmtCursorConversionRate_Object = MibTableColumn
sscmtCursorConversionRate = _SscmtCursorConversionRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 25, 1, 2),
    _SscmtCursorConversionRate_Type()
)
sscmtCursorConversionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmtCursorConversionRate.setStatus("current")
_SscmtCursorFlushes_Type = Gauge32
_SscmtCursorFlushes_Object = MibTableColumn
sscmtCursorFlushes = _SscmtCursorFlushes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 25, 1, 3),
    _SscmtCursorFlushes_Type()
)
sscmtCursorFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmtCursorFlushes.setStatus("current")
_SqlServerCursorManagerByTypeTable_Object = MibTable
sqlServerCursorManagerByTypeTable = _SqlServerCursorManagerByTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 26)
)
if mibBuilder.loadTexts:
    sqlServerCursorManagerByTypeTable.setStatus("current")
_SqlServerCursorManagerByTypeEntry_Object = MibTableRow
sqlServerCursorManagerByTypeEntry = _SqlServerCursorManagerByTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 26, 1)
)
sqlServerCursorManagerByTypeEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "sscmbtInstance"),
)
if mibBuilder.loadTexts:
    sqlServerCursorManagerByTypeEntry.setStatus("current")
_SscmbtInstance_Type = InstanceName
_SscmbtInstance_Object = MibTableColumn
sscmbtInstance = _SscmbtInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 26, 1, 1),
    _SscmbtInstance_Type()
)
sscmbtInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmbtInstance.setStatus("current")
_SscmbtActiveCursors_Type = Gauge32
_SscmbtActiveCursors_Object = MibTableColumn
sscmbtActiveCursors = _SscmbtActiveCursors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 26, 1, 2),
    _SscmbtActiveCursors_Type()
)
sscmbtActiveCursors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmbtActiveCursors.setStatus("current")
_SscmbtCacheHitRatio_Type = Gauge32
_SscmbtCacheHitRatio_Object = MibTableColumn
sscmbtCacheHitRatio = _SscmbtCacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 26, 1, 3),
    _SscmbtCacheHitRatio_Type()
)
sscmbtCacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmbtCacheHitRatio.setStatus("current")
_SscmbtCachedCursorCounts_Type = Gauge32
_SscmbtCachedCursorCounts_Object = MibTableColumn
sscmbtCachedCursorCounts = _SscmbtCachedCursorCounts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 26, 1, 4),
    _SscmbtCachedCursorCounts_Type()
)
sscmbtCachedCursorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmbtCachedCursorCounts.setStatus("current")
_SscmbtCursorCacheUseCountsPerSec_Type = Gauge32
_SscmbtCursorCacheUseCountsPerSec_Object = MibTableColumn
sscmbtCursorCacheUseCountsPerSec = _SscmbtCursorCacheUseCountsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 26, 1, 5),
    _SscmbtCursorCacheUseCountsPerSec_Type()
)
sscmbtCursorCacheUseCountsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmbtCursorCacheUseCountsPerSec.setStatus("current")
_SscmbtCursorRequestsPerSec_Type = Gauge32
_SscmbtCursorRequestsPerSec_Object = MibTableColumn
sscmbtCursorRequestsPerSec = _SscmbtCursorRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 26, 1, 6),
    _SscmbtCursorRequestsPerSec_Type()
)
sscmbtCursorRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmbtCursorRequestsPerSec.setStatus("current")
_SscmbtCursorMemoryUsage_Type = Gauge32
_SscmbtCursorMemoryUsage_Object = MibTableColumn
sscmbtCursorMemoryUsage = _SscmbtCursorMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 26, 1, 7),
    _SscmbtCursorMemoryUsage_Type()
)
sscmbtCursorMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmbtCursorMemoryUsage.setStatus("current")
_SscmbtCursorWorktableUsage_Type = Gauge32
_SscmbtCursorWorktableUsage_Object = MibTableColumn
sscmbtCursorWorktableUsage = _SscmbtCursorWorktableUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 26, 1, 8),
    _SscmbtCursorWorktableUsage_Type()
)
sscmbtCursorWorktableUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmbtCursorWorktableUsage.setStatus("current")
_SscmbtNumberOfActiveCursorPlans_Type = Gauge32
_SscmbtNumberOfActiveCursorPlans_Object = MibTableColumn
sscmbtNumberOfActiveCursorPlans = _SscmbtNumberOfActiveCursorPlans_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 26, 1, 9),
    _SscmbtNumberOfActiveCursorPlans_Type()
)
sscmbtNumberOfActiveCursorPlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sscmbtNumberOfActiveCursorPlans.setStatus("current")
_SqlServerDatabasesTable_Object = MibTable
sqlServerDatabasesTable = _SqlServerDatabasesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27)
)
if mibBuilder.loadTexts:
    sqlServerDatabasesTable.setStatus("current")
_SqlServerDatabasesEntry_Object = MibTableRow
sqlServerDatabasesEntry = _SqlServerDatabasesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1)
)
sqlServerDatabasesEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "ssdInstance"),
)
if mibBuilder.loadTexts:
    sqlServerDatabasesEntry.setStatus("current")
_SsdInstance_Type = InstanceName
_SsdInstance_Object = MibTableColumn
ssdInstance = _SsdInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 1),
    _SsdInstance_Type()
)
ssdInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdInstance.setStatus("current")
_SsdActiveTransactions_Type = Gauge32
_SsdActiveTransactions_Object = MibTableColumn
ssdActiveTransactions = _SsdActiveTransactions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 2),
    _SsdActiveTransactions_Type()
)
ssdActiveTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdActiveTransactions.setStatus("current")
_SsdBackupPerRestoreThroughputPerSec_Type = Gauge32
_SsdBackupPerRestoreThroughputPerSec_Object = MibTableColumn
ssdBackupPerRestoreThroughputPerSec = _SsdBackupPerRestoreThroughputPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 3),
    _SsdBackupPerRestoreThroughputPerSec_Type()
)
ssdBackupPerRestoreThroughputPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdBackupPerRestoreThroughputPerSec.setStatus("current")
_SsdBulkCopyRowsPerSec_Type = Gauge32
_SsdBulkCopyRowsPerSec_Object = MibTableColumn
ssdBulkCopyRowsPerSec = _SsdBulkCopyRowsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 4),
    _SsdBulkCopyRowsPerSec_Type()
)
ssdBulkCopyRowsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdBulkCopyRowsPerSec.setStatus("current")
_SsdBulkCopyThroughputPerSec_Type = Gauge32
_SsdBulkCopyThroughputPerSec_Object = MibTableColumn
ssdBulkCopyThroughputPerSec = _SsdBulkCopyThroughputPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 5),
    _SsdBulkCopyThroughputPerSec_Type()
)
ssdBulkCopyThroughputPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdBulkCopyThroughputPerSec.setStatus("current")
_SsdDBCCLogicalScanBytesPerSec_Type = Gauge32
_SsdDBCCLogicalScanBytesPerSec_Object = MibTableColumn
ssdDBCCLogicalScanBytesPerSec = _SsdDBCCLogicalScanBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 6),
    _SsdDBCCLogicalScanBytesPerSec_Type()
)
ssdDBCCLogicalScanBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdDBCCLogicalScanBytesPerSec.setStatus("current")
_SsdDataFileSSizeKB_Type = Gauge32
_SsdDataFileSSizeKB_Object = MibTableColumn
ssdDataFileSSizeKB = _SsdDataFileSSizeKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 7),
    _SsdDataFileSSizeKB_Type()
)
ssdDataFileSSizeKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdDataFileSSizeKB.setStatus("current")
_SsdLogBytesFlushedPerSec_Type = Gauge32
_SsdLogBytesFlushedPerSec_Object = MibTableColumn
ssdLogBytesFlushedPerSec = _SsdLogBytesFlushedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 8),
    _SsdLogBytesFlushedPerSec_Type()
)
ssdLogBytesFlushedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdLogBytesFlushedPerSec.setStatus("current")
_SsdLogCacheHitRatio_Type = Gauge32
_SsdLogCacheHitRatio_Object = MibTableColumn
ssdLogCacheHitRatio = _SsdLogCacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 9),
    _SsdLogCacheHitRatio_Type()
)
ssdLogCacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdLogCacheHitRatio.setStatus("current")
_SsdLogCacheReadsPerSec_Type = Gauge32
_SsdLogCacheReadsPerSec_Object = MibTableColumn
ssdLogCacheReadsPerSec = _SsdLogCacheReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 10),
    _SsdLogCacheReadsPerSec_Type()
)
ssdLogCacheReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdLogCacheReadsPerSec.setStatus("current")
_SsdLogFileSSizeKB_Type = Gauge32
_SsdLogFileSSizeKB_Object = MibTableColumn
ssdLogFileSSizeKB = _SsdLogFileSSizeKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 11),
    _SsdLogFileSSizeKB_Type()
)
ssdLogFileSSizeKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdLogFileSSizeKB.setStatus("current")
_SsdLogFileSUsedSizeKB_Type = Gauge32
_SsdLogFileSUsedSizeKB_Object = MibTableColumn
ssdLogFileSUsedSizeKB = _SsdLogFileSUsedSizeKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 12),
    _SsdLogFileSUsedSizeKB_Type()
)
ssdLogFileSUsedSizeKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdLogFileSUsedSizeKB.setStatus("current")
_SsdLogFlushWaitTime_Type = Gauge32
_SsdLogFlushWaitTime_Object = MibTableColumn
ssdLogFlushWaitTime = _SsdLogFlushWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 13),
    _SsdLogFlushWaitTime_Type()
)
ssdLogFlushWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdLogFlushWaitTime.setStatus("current")
_SsdLogFlushWaitsPerSec_Type = Gauge32
_SsdLogFlushWaitsPerSec_Object = MibTableColumn
ssdLogFlushWaitsPerSec = _SsdLogFlushWaitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 14),
    _SsdLogFlushWaitsPerSec_Type()
)
ssdLogFlushWaitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdLogFlushWaitsPerSec.setStatus("current")
_SsdLogFlushesPerSec_Type = Gauge32
_SsdLogFlushesPerSec_Object = MibTableColumn
ssdLogFlushesPerSec = _SsdLogFlushesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 15),
    _SsdLogFlushesPerSec_Type()
)
ssdLogFlushesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdLogFlushesPerSec.setStatus("current")
_SsdLogGrowths_Type = Gauge32
_SsdLogGrowths_Object = MibTableColumn
ssdLogGrowths = _SsdLogGrowths_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 16),
    _SsdLogGrowths_Type()
)
ssdLogGrowths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdLogGrowths.setStatus("current")
_SsdLogShrinks_Type = Gauge32
_SsdLogShrinks_Object = MibTableColumn
ssdLogShrinks = _SsdLogShrinks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 17),
    _SsdLogShrinks_Type()
)
ssdLogShrinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdLogShrinks.setStatus("current")
_SsdLogTruncations_Type = Gauge32
_SsdLogTruncations_Object = MibTableColumn
ssdLogTruncations = _SsdLogTruncations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 18),
    _SsdLogTruncations_Type()
)
ssdLogTruncations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdLogTruncations.setStatus("current")
_SsdMirroringAcksReceivedPerSec_Type = Gauge32
_SsdMirroringAcksReceivedPerSec_Object = MibTableColumn
ssdMirroringAcksReceivedPerSec = _SsdMirroringAcksReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 19),
    _SsdMirroringAcksReceivedPerSec_Type()
)
ssdMirroringAcksReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdMirroringAcksReceivedPerSec.setStatus("current")
_SsdMirroringBytesSentPerSec_Type = Gauge32
_SsdMirroringBytesSentPerSec_Object = MibTableColumn
ssdMirroringBytesSentPerSec = _SsdMirroringBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 20),
    _SsdMirroringBytesSentPerSec_Type()
)
ssdMirroringBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdMirroringBytesSentPerSec.setStatus("current")
_SsdMirroringPagesSentPerSec_Type = Gauge32
_SsdMirroringPagesSentPerSec_Object = MibTableColumn
ssdMirroringPagesSentPerSec = _SsdMirroringPagesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 21),
    _SsdMirroringPagesSentPerSec_Type()
)
ssdMirroringPagesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdMirroringPagesSentPerSec.setStatus("current")
_SsdMirroringSendsPerSec_Type = Gauge32
_SsdMirroringSendsPerSec_Object = MibTableColumn
ssdMirroringSendsPerSec = _SsdMirroringSendsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 22),
    _SsdMirroringSendsPerSec_Type()
)
ssdMirroringSendsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdMirroringSendsPerSec.setStatus("current")
_SsdMirroringTotalAcksReceived_Type = Gauge32
_SsdMirroringTotalAcksReceived_Object = MibTableColumn
ssdMirroringTotalAcksReceived = _SsdMirroringTotalAcksReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 23),
    _SsdMirroringTotalAcksReceived_Type()
)
ssdMirroringTotalAcksReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdMirroringTotalAcksReceived.setStatus("current")
_SsdMirroringTotalBytesSent_Type = Gauge32
_SsdMirroringTotalBytesSent_Object = MibTableColumn
ssdMirroringTotalBytesSent = _SsdMirroringTotalBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 24),
    _SsdMirroringTotalBytesSent_Type()
)
ssdMirroringTotalBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdMirroringTotalBytesSent.setStatus("current")
_SsdMirroringTotalPagesSent_Type = Gauge32
_SsdMirroringTotalPagesSent_Object = MibTableColumn
ssdMirroringTotalPagesSent = _SsdMirroringTotalPagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 25),
    _SsdMirroringTotalPagesSent_Type()
)
ssdMirroringTotalPagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdMirroringTotalPagesSent.setStatus("current")
_SsdMirroringTotalSends_Type = Gauge32
_SsdMirroringTotalSends_Object = MibTableColumn
ssdMirroringTotalSends = _SsdMirroringTotalSends_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 26),
    _SsdMirroringTotalSends_Type()
)
ssdMirroringTotalSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdMirroringTotalSends.setStatus("current")
_SsdMirroringTransactionDelay_Type = Gauge32
_SsdMirroringTransactionDelay_Object = MibTableColumn
ssdMirroringTransactionDelay = _SsdMirroringTransactionDelay_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 27),
    _SsdMirroringTransactionDelay_Type()
)
ssdMirroringTransactionDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdMirroringTransactionDelay.setStatus("current")
_SsdPercentLogUsed_Type = Gauge32
_SsdPercentLogUsed_Object = MibTableColumn
ssdPercentLogUsed = _SsdPercentLogUsed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 28),
    _SsdPercentLogUsed_Type()
)
ssdPercentLogUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdPercentLogUsed.setStatus("current")
_SsdReplPendingXacts_Type = Gauge32
_SsdReplPendingXacts_Object = MibTableColumn
ssdReplPendingXacts = _SsdReplPendingXacts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 29),
    _SsdReplPendingXacts_Type()
)
ssdReplPendingXacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdReplPendingXacts.setStatus("current")
_SsdReplTransRate_Type = Gauge32
_SsdReplTransRate_Object = MibTableColumn
ssdReplTransRate = _SsdReplTransRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 30),
    _SsdReplTransRate_Type()
)
ssdReplTransRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdReplTransRate.setStatus("current")
_SsdShrinkDataMovementBytesPerSec_Type = Gauge32
_SsdShrinkDataMovementBytesPerSec_Object = MibTableColumn
ssdShrinkDataMovementBytesPerSec = _SsdShrinkDataMovementBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 31),
    _SsdShrinkDataMovementBytesPerSec_Type()
)
ssdShrinkDataMovementBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdShrinkDataMovementBytesPerSec.setStatus("current")
_SsdTransactionsPerSec_Type = Gauge32
_SsdTransactionsPerSec_Object = MibTableColumn
ssdTransactionsPerSec = _SsdTransactionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 27, 1, 32),
    _SsdTransactionsPerSec_Type()
)
ssdTransactionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssdTransactionsPerSec.setStatus("current")
_SqlServerExecStatisticsTable_Object = MibTable
sqlServerExecStatisticsTable = _SqlServerExecStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 28)
)
if mibBuilder.loadTexts:
    sqlServerExecStatisticsTable.setStatus("current")
_SqlServerExecStatisticsEntry_Object = MibTableRow
sqlServerExecStatisticsEntry = _SqlServerExecStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 28, 1)
)
sqlServerExecStatisticsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "ssesInstance"),
)
if mibBuilder.loadTexts:
    sqlServerExecStatisticsEntry.setStatus("current")
_SsesInstance_Type = InstanceName
_SsesInstance_Object = MibTableColumn
ssesInstance = _SsesInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 28, 1, 1),
    _SsesInstance_Type()
)
ssesInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssesInstance.setStatus("current")
_SsesDTCCalls_Type = Gauge32
_SsesDTCCalls_Object = MibTableColumn
ssesDTCCalls = _SsesDTCCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 28, 1, 2),
    _SsesDTCCalls_Type()
)
ssesDTCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssesDTCCalls.setStatus("current")
_SsesDistributedQuery_Type = Gauge32
_SsesDistributedQuery_Object = MibTableColumn
ssesDistributedQuery = _SsesDistributedQuery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 28, 1, 3),
    _SsesDistributedQuery_Type()
)
ssesDistributedQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssesDistributedQuery.setStatus("current")
_SsesExtendedProcedures_Type = Gauge32
_SsesExtendedProcedures_Object = MibTableColumn
ssesExtendedProcedures = _SsesExtendedProcedures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 28, 1, 4),
    _SsesExtendedProcedures_Type()
)
ssesExtendedProcedures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssesExtendedProcedures.setStatus("current")
_SsesOLEDBCalls_Type = Gauge32
_SsesOLEDBCalls_Object = MibTableColumn
ssesOLEDBCalls = _SsesOLEDBCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 28, 1, 5),
    _SsesOLEDBCalls_Type()
)
ssesOLEDBCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssesOLEDBCalls.setStatus("current")
_SqlServerGeneralStatisticsTable_Object = MibTable
sqlServerGeneralStatisticsTable = _SqlServerGeneralStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29)
)
if mibBuilder.loadTexts:
    sqlServerGeneralStatisticsTable.setStatus("current")
_SqlServerGeneralStatisticsEntry_Object = MibTableRow
sqlServerGeneralStatisticsEntry = _SqlServerGeneralStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1)
)
sqlServerGeneralStatisticsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
)
if mibBuilder.loadTexts:
    sqlServerGeneralStatisticsEntry.setStatus("current")
_SsgsHTTPAnonymousRequests_Type = Gauge32
_SsgsHTTPAnonymousRequests_Object = MibTableColumn
ssgsHTTPAnonymousRequests = _SsgsHTTPAnonymousRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 1),
    _SsgsHTTPAnonymousRequests_Type()
)
ssgsHTTPAnonymousRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsHTTPAnonymousRequests.setStatus("current")
_SsgsHTTPAuthenticatedRequests_Type = Gauge32
_SsgsHTTPAuthenticatedRequests_Object = MibTableColumn
ssgsHTTPAuthenticatedRequests = _SsgsHTTPAuthenticatedRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 2),
    _SsgsHTTPAuthenticatedRequests_Type()
)
ssgsHTTPAuthenticatedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsHTTPAuthenticatedRequests.setStatus("current")
_SsgsLogicalConnections_Type = Gauge32
_SsgsLogicalConnections_Object = MibTableColumn
ssgsLogicalConnections = _SsgsLogicalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 3),
    _SsgsLogicalConnections_Type()
)
ssgsLogicalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsLogicalConnections.setStatus("current")
_SsgsLoginsPerSec_Type = Gauge32
_SsgsLoginsPerSec_Object = MibTableColumn
ssgsLoginsPerSec = _SsgsLoginsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 4),
    _SsgsLoginsPerSec_Type()
)
ssgsLoginsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsLoginsPerSec.setStatus("current")
_SsgsLogoutsPerSec_Type = Gauge32
_SsgsLogoutsPerSec_Object = MibTableColumn
ssgsLogoutsPerSec = _SsgsLogoutsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 5),
    _SsgsLogoutsPerSec_Type()
)
ssgsLogoutsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsLogoutsPerSec.setStatus("current")
_SsgsMarsDeadlocks_Type = Gauge32
_SsgsMarsDeadlocks_Object = MibTableColumn
ssgsMarsDeadlocks = _SsgsMarsDeadlocks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 6),
    _SsgsMarsDeadlocks_Type()
)
ssgsMarsDeadlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsMarsDeadlocks.setStatus("current")
_SsgsNonAtomicYieldRate_Type = Gauge32
_SsgsNonAtomicYieldRate_Object = MibTableColumn
ssgsNonAtomicYieldRate = _SsgsNonAtomicYieldRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 7),
    _SsgsNonAtomicYieldRate_Type()
)
ssgsNonAtomicYieldRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsNonAtomicYieldRate.setStatus("current")
_SsgsProcessesBlocked_Type = Gauge32
_SsgsProcessesBlocked_Object = MibTableColumn
ssgsProcessesBlocked = _SsgsProcessesBlocked_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 8),
    _SsgsProcessesBlocked_Type()
)
ssgsProcessesBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsProcessesBlocked.setStatus("current")
_SsgsSOAPEmptyRequests_Type = Gauge32
_SsgsSOAPEmptyRequests_Object = MibTableColumn
ssgsSOAPEmptyRequests = _SsgsSOAPEmptyRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 9),
    _SsgsSOAPEmptyRequests_Type()
)
ssgsSOAPEmptyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsSOAPEmptyRequests.setStatus("current")
_SsgsSOAPMethodInvocations_Type = Gauge32
_SsgsSOAPMethodInvocations_Object = MibTableColumn
ssgsSOAPMethodInvocations = _SsgsSOAPMethodInvocations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 10),
    _SsgsSOAPMethodInvocations_Type()
)
ssgsSOAPMethodInvocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsSOAPMethodInvocations.setStatus("current")
_SsgsSOAPSQLRequests_Type = Gauge32
_SsgsSOAPSQLRequests_Object = MibTableColumn
ssgsSOAPSQLRequests = _SsgsSOAPSQLRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 11),
    _SsgsSOAPSQLRequests_Type()
)
ssgsSOAPSQLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsSOAPSQLRequests.setStatus("current")
_SsgsSOAPSessionInitiateRequests_Type = Gauge32
_SsgsSOAPSessionInitiateRequests_Object = MibTableColumn
ssgsSOAPSessionInitiateRequests = _SsgsSOAPSessionInitiateRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 12),
    _SsgsSOAPSessionInitiateRequests_Type()
)
ssgsSOAPSessionInitiateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsSOAPSessionInitiateRequests.setStatus("current")
_SsgsSOAPSessionTerminateRequests_Type = Gauge32
_SsgsSOAPSessionTerminateRequests_Object = MibTableColumn
ssgsSOAPSessionTerminateRequests = _SsgsSOAPSessionTerminateRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 13),
    _SsgsSOAPSessionTerminateRequests_Type()
)
ssgsSOAPSessionTerminateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsSOAPSessionTerminateRequests.setStatus("current")
_SsgsSOAPWSDLRequests_Type = Gauge32
_SsgsSOAPWSDLRequests_Object = MibTableColumn
ssgsSOAPWSDLRequests = _SsgsSOAPWSDLRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 14),
    _SsgsSOAPWSDLRequests_Type()
)
ssgsSOAPWSDLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsSOAPWSDLRequests.setStatus("current")
_SsgsTempTablesCreationRate_Type = Gauge32
_SsgsTempTablesCreationRate_Object = MibTableColumn
ssgsTempTablesCreationRate = _SsgsTempTablesCreationRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 15),
    _SsgsTempTablesCreationRate_Type()
)
ssgsTempTablesCreationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsTempTablesCreationRate.setStatus("current")
_SsgsTransactions_Type = Gauge32
_SsgsTransactions_Object = MibTableColumn
ssgsTransactions = _SsgsTransactions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 16),
    _SsgsTransactions_Type()
)
ssgsTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsTransactions.setStatus("current")
_SsgsUserConnections_Type = Gauge32
_SsgsUserConnections_Object = MibTableColumn
ssgsUserConnections = _SsgsUserConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 29, 1, 17),
    _SsgsUserConnections_Type()
)
ssgsUserConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssgsUserConnections.setStatus("current")
_SqlServerLatchesTable_Object = MibTable
sqlServerLatchesTable = _SqlServerLatchesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 30)
)
if mibBuilder.loadTexts:
    sqlServerLatchesTable.setStatus("current")
_SqlServerLatchesEntry_Object = MibTableRow
sqlServerLatchesEntry = _SqlServerLatchesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 30, 1)
)
sqlServerLatchesEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
)
if mibBuilder.loadTexts:
    sqlServerLatchesEntry.setStatus("current")
_SsltAverageLatchWaitTimeMs_Type = Gauge32
_SsltAverageLatchWaitTimeMs_Object = MibTableColumn
ssltAverageLatchWaitTimeMs = _SsltAverageLatchWaitTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 30, 1, 1),
    _SsltAverageLatchWaitTimeMs_Type()
)
ssltAverageLatchWaitTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssltAverageLatchWaitTimeMs.setStatus("current")
_SsltLatchWaitsPerSec_Type = Gauge32
_SsltLatchWaitsPerSec_Object = MibTableColumn
ssltLatchWaitsPerSec = _SsltLatchWaitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 30, 1, 2),
    _SsltLatchWaitsPerSec_Type()
)
ssltLatchWaitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssltLatchWaitsPerSec.setStatus("current")
_SsltTotalLatchWaitTimeMs_Type = Gauge32
_SsltTotalLatchWaitTimeMs_Object = MibTableColumn
ssltTotalLatchWaitTimeMs = _SsltTotalLatchWaitTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 30, 1, 3),
    _SsltTotalLatchWaitTimeMs_Type()
)
ssltTotalLatchWaitTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssltTotalLatchWaitTimeMs.setStatus("current")
_SqlServerLocksTable_Object = MibTable
sqlServerLocksTable = _SqlServerLocksTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 31)
)
if mibBuilder.loadTexts:
    sqlServerLocksTable.setStatus("current")
_SqlServerLocksEntry_Object = MibTableRow
sqlServerLocksEntry = _SqlServerLocksEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 31, 1)
)
sqlServerLocksEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "sslkInstance"),
)
if mibBuilder.loadTexts:
    sqlServerLocksEntry.setStatus("current")
_SslkInstance_Type = InstanceName
_SslkInstance_Object = MibTableColumn
sslkInstance = _SslkInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 31, 1, 1),
    _SslkInstance_Type()
)
sslkInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslkInstance.setStatus("current")
_SslkAverageWaitTimeMs_Type = Gauge32
_SslkAverageWaitTimeMs_Object = MibTableColumn
sslkAverageWaitTimeMs = _SslkAverageWaitTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 31, 1, 2),
    _SslkAverageWaitTimeMs_Type()
)
sslkAverageWaitTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslkAverageWaitTimeMs.setStatus("current")
_SslkLockRequestsPerSec_Type = Gauge32
_SslkLockRequestsPerSec_Object = MibTableColumn
sslkLockRequestsPerSec = _SslkLockRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 31, 1, 3),
    _SslkLockRequestsPerSec_Type()
)
sslkLockRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslkLockRequestsPerSec.setStatus("current")
_SslkLockTimeoutsTimeoutGT0PerSec_Type = Gauge32
_SslkLockTimeoutsTimeoutGT0PerSec_Object = MibTableColumn
sslkLockTimeoutsTimeoutGT0PerSec = _SslkLockTimeoutsTimeoutGT0PerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 31, 1, 4),
    _SslkLockTimeoutsTimeoutGT0PerSec_Type()
)
sslkLockTimeoutsTimeoutGT0PerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslkLockTimeoutsTimeoutGT0PerSec.setStatus("current")
_SslkLockTimeoutsPerSec_Type = Gauge32
_SslkLockTimeoutsPerSec_Object = MibTableColumn
sslkLockTimeoutsPerSec = _SslkLockTimeoutsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 31, 1, 5),
    _SslkLockTimeoutsPerSec_Type()
)
sslkLockTimeoutsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslkLockTimeoutsPerSec.setStatus("current")
_SslkLockWaitTimeMs_Type = Gauge32
_SslkLockWaitTimeMs_Object = MibTableColumn
sslkLockWaitTimeMs = _SslkLockWaitTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 31, 1, 6),
    _SslkLockWaitTimeMs_Type()
)
sslkLockWaitTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslkLockWaitTimeMs.setStatus("current")
_SslkLockWaitsPerSec_Type = Gauge32
_SslkLockWaitsPerSec_Object = MibTableColumn
sslkLockWaitsPerSec = _SslkLockWaitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 31, 1, 7),
    _SslkLockWaitsPerSec_Type()
)
sslkLockWaitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslkLockWaitsPerSec.setStatus("current")
_SslkNumberOfDeadlocksPerSec_Type = Gauge32
_SslkNumberOfDeadlocksPerSec_Object = MibTableColumn
sslkNumberOfDeadlocksPerSec = _SslkNumberOfDeadlocksPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 31, 1, 8),
    _SslkNumberOfDeadlocksPerSec_Type()
)
sslkNumberOfDeadlocksPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslkNumberOfDeadlocksPerSec.setStatus("current")
_SqlServerMemoryManagerTable_Object = MibTable
sqlServerMemoryManagerTable = _SqlServerMemoryManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32)
)
if mibBuilder.loadTexts:
    sqlServerMemoryManagerTable.setStatus("current")
_SqlServerMemoryManagerEntry_Object = MibTableRow
sqlServerMemoryManagerEntry = _SqlServerMemoryManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1)
)
sqlServerMemoryManagerEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
)
if mibBuilder.loadTexts:
    sqlServerMemoryManagerEntry.setStatus("current")
_SsmmConnectionMemoryKB_Type = Gauge32
_SsmmConnectionMemoryKB_Object = MibTableColumn
ssmmConnectionMemoryKB = _SsmmConnectionMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1, 1),
    _SsmmConnectionMemoryKB_Type()
)
ssmmConnectionMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmmConnectionMemoryKB.setStatus("current")
_SsmmGrantedWorkspaceMemoryKB_Type = Gauge32
_SsmmGrantedWorkspaceMemoryKB_Object = MibTableColumn
ssmmGrantedWorkspaceMemoryKB = _SsmmGrantedWorkspaceMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1, 2),
    _SsmmGrantedWorkspaceMemoryKB_Type()
)
ssmmGrantedWorkspaceMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmmGrantedWorkspaceMemoryKB.setStatus("current")
_SsmmLockBlocks_Type = Gauge32
_SsmmLockBlocks_Object = MibTableColumn
ssmmLockBlocks = _SsmmLockBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1, 3),
    _SsmmLockBlocks_Type()
)
ssmmLockBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmmLockBlocks.setStatus("current")
_SsmmLockBlocksAllocated_Type = Gauge32
_SsmmLockBlocksAllocated_Object = MibTableColumn
ssmmLockBlocksAllocated = _SsmmLockBlocksAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1, 4),
    _SsmmLockBlocksAllocated_Type()
)
ssmmLockBlocksAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmmLockBlocksAllocated.setStatus("current")
_SsmmLockMemoryKB_Type = Gauge32
_SsmmLockMemoryKB_Object = MibTableColumn
ssmmLockMemoryKB = _SsmmLockMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1, 5),
    _SsmmLockMemoryKB_Type()
)
ssmmLockMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmmLockMemoryKB.setStatus("current")
_SsmmLockOwnerBlocks_Type = Gauge32
_SsmmLockOwnerBlocks_Object = MibTableColumn
ssmmLockOwnerBlocks = _SsmmLockOwnerBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1, 6),
    _SsmmLockOwnerBlocks_Type()
)
ssmmLockOwnerBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmmLockOwnerBlocks.setStatus("current")
_SsmmLockOwnerBlocksAllocated_Type = Gauge32
_SsmmLockOwnerBlocksAllocated_Object = MibTableColumn
ssmmLockOwnerBlocksAllocated = _SsmmLockOwnerBlocksAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1, 7),
    _SsmmLockOwnerBlocksAllocated_Type()
)
ssmmLockOwnerBlocksAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmmLockOwnerBlocksAllocated.setStatus("current")
_SsmmMaximumWorkspaceMemoryKB_Type = Gauge32
_SsmmMaximumWorkspaceMemoryKB_Object = MibTableColumn
ssmmMaximumWorkspaceMemoryKB = _SsmmMaximumWorkspaceMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1, 8),
    _SsmmMaximumWorkspaceMemoryKB_Type()
)
ssmmMaximumWorkspaceMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmmMaximumWorkspaceMemoryKB.setStatus("current")
_SsmmMemoryGrantsOutstanding_Type = Gauge32
_SsmmMemoryGrantsOutstanding_Object = MibTableColumn
ssmmMemoryGrantsOutstanding = _SsmmMemoryGrantsOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1, 9),
    _SsmmMemoryGrantsOutstanding_Type()
)
ssmmMemoryGrantsOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmmMemoryGrantsOutstanding.setStatus("current")
_SsmmMemoryGrantsPending_Type = Gauge32
_SsmmMemoryGrantsPending_Object = MibTableColumn
ssmmMemoryGrantsPending = _SsmmMemoryGrantsPending_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1, 10),
    _SsmmMemoryGrantsPending_Type()
)
ssmmMemoryGrantsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmmMemoryGrantsPending.setStatus("current")
_SsmmOptimizerMemoryKB_Type = Gauge32
_SsmmOptimizerMemoryKB_Object = MibTableColumn
ssmmOptimizerMemoryKB = _SsmmOptimizerMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1, 11),
    _SsmmOptimizerMemoryKB_Type()
)
ssmmOptimizerMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmmOptimizerMemoryKB.setStatus("current")
_SsmmSQLCacheMemoryKB_Type = Gauge32
_SsmmSQLCacheMemoryKB_Object = MibTableColumn
ssmmSQLCacheMemoryKB = _SsmmSQLCacheMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1, 12),
    _SsmmSQLCacheMemoryKB_Type()
)
ssmmSQLCacheMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmmSQLCacheMemoryKB.setStatus("current")
_SsmmTargetServerMemoryKB_Type = Gauge32
_SsmmTargetServerMemoryKB_Object = MibTableColumn
ssmmTargetServerMemoryKB = _SsmmTargetServerMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1, 13),
    _SsmmTargetServerMemoryKB_Type()
)
ssmmTargetServerMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmmTargetServerMemoryKB.setStatus("current")
_SsmmTotalServerMemoryKB_Type = Gauge32
_SsmmTotalServerMemoryKB_Object = MibTableColumn
ssmmTotalServerMemoryKB = _SsmmTotalServerMemoryKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 32, 1, 14),
    _SsmmTotalServerMemoryKB_Type()
)
ssmmTotalServerMemoryKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmmTotalServerMemoryKB.setStatus("current")
_SqlServerReplicateLogreaderTable_Object = MibTable
sqlServerReplicateLogreaderTable = _SqlServerReplicateLogreaderTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 33)
)
if mibBuilder.loadTexts:
    sqlServerReplicateLogreaderTable.setStatus("current")
_SqlServerReplicateLogreaderEntry_Object = MibTableRow
sqlServerReplicateLogreaderEntry = _SqlServerReplicateLogreaderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 33, 1)
)
sqlServerReplicateLogreaderEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "ssrlInstance"),
)
if mibBuilder.loadTexts:
    sqlServerReplicateLogreaderEntry.setStatus("current")
_SsrlInstance_Type = InstanceName
_SsrlInstance_Object = MibTableColumn
ssrlInstance = _SsrlInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 33, 1, 1),
    _SsrlInstance_Type()
)
ssrlInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrlInstance.setStatus("current")
_SsrlLogreaderDeliveredCmdsPerSec_Type = Gauge32
_SsrlLogreaderDeliveredCmdsPerSec_Object = MibTableColumn
ssrlLogreaderDeliveredCmdsPerSec = _SsrlLogreaderDeliveredCmdsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 33, 1, 2),
    _SsrlLogreaderDeliveredCmdsPerSec_Type()
)
ssrlLogreaderDeliveredCmdsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrlLogreaderDeliveredCmdsPerSec.setStatus("current")
_SsrlLogreaderDelivereTransPerSec_Type = Gauge32
_SsrlLogreaderDelivereTransPerSec_Object = MibTableColumn
ssrlLogreaderDelivereTransPerSec = _SsrlLogreaderDelivereTransPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 33, 1, 3),
    _SsrlLogreaderDelivereTransPerSec_Type()
)
ssrlLogreaderDelivereTransPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrlLogreaderDelivereTransPerSec.setStatus("current")
_SsrlLogreaderDeliveryLatency_Type = Gauge32
_SsrlLogreaderDeliveryLatency_Object = MibTableColumn
ssrlLogreaderDeliveryLatency = _SsrlLogreaderDeliveryLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 33, 1, 4),
    _SsrlLogreaderDeliveryLatency_Type()
)
ssrlLogreaderDeliveryLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrlLogreaderDeliveryLatency.setStatus("current")
_SqlServerReplicateSnapshotTable_Object = MibTable
sqlServerReplicateSnapshotTable = _SqlServerReplicateSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 34)
)
if mibBuilder.loadTexts:
    sqlServerReplicateSnapshotTable.setStatus("current")
_SqlServerReplicateSnapshotEntry_Object = MibTableRow
sqlServerReplicateSnapshotEntry = _SqlServerReplicateSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 34, 1)
)
sqlServerReplicateSnapshotEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "ssrsInstance"),
)
if mibBuilder.loadTexts:
    sqlServerReplicateSnapshotEntry.setStatus("current")
_SsrsInstance_Type = InstanceName
_SsrsInstance_Object = MibTableColumn
ssrsInstance = _SsrsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 34, 1, 1),
    _SsrsInstance_Type()
)
ssrsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrsInstance.setStatus("current")
_SsrsSnapshotDeliveredCmdsPerSec_Type = Gauge32
_SsrsSnapshotDeliveredCmdsPerSec_Object = MibTableColumn
ssrsSnapshotDeliveredCmdsPerSec = _SsrsSnapshotDeliveredCmdsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 34, 1, 2),
    _SsrsSnapshotDeliveredCmdsPerSec_Type()
)
ssrsSnapshotDeliveredCmdsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrsSnapshotDeliveredCmdsPerSec.setStatus("current")
_SsrsSnapshotDeliveredTransPerSec_Type = Gauge32
_SsrsSnapshotDeliveredTransPerSec_Object = MibTableColumn
ssrsSnapshotDeliveredTransPerSec = _SsrsSnapshotDeliveredTransPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 34, 1, 3),
    _SsrsSnapshotDeliveredTransPerSec_Type()
)
ssrsSnapshotDeliveredTransPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrsSnapshotDeliveredTransPerSec.setStatus("current")
_SqlServerReplicationAgentsTable_Object = MibTable
sqlServerReplicationAgentsTable = _SqlServerReplicationAgentsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 35)
)
if mibBuilder.loadTexts:
    sqlServerReplicationAgentsTable.setStatus("current")
_SqlServerReplicationAgentsEntry_Object = MibTableRow
sqlServerReplicationAgentsEntry = _SqlServerReplicationAgentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 35, 1)
)
sqlServerReplicationAgentsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "ssraInstance"),
)
if mibBuilder.loadTexts:
    sqlServerReplicationAgentsEntry.setStatus("current")
_SsraInstance_Type = InstanceName
_SsraInstance_Object = MibTableColumn
ssraInstance = _SsraInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 35, 1, 1),
    _SsraInstance_Type()
)
ssraInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssraInstance.setStatus("current")
_SsraRunning_Type = Gauge32
_SsraRunning_Object = MibTableColumn
ssraRunning = _SsraRunning_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 35, 1, 2),
    _SsraRunning_Type()
)
ssraRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssraRunning.setStatus("current")
_SqlServerReplicationDistTable_Object = MibTable
sqlServerReplicationDistTable = _SqlServerReplicationDistTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 36)
)
if mibBuilder.loadTexts:
    sqlServerReplicationDistTable.setStatus("current")
_SqlServerReplicationDistEntry_Object = MibTableRow
sqlServerReplicationDistEntry = _SqlServerReplicationDistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 36, 1)
)
sqlServerReplicationDistEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "ssrdInstance"),
)
if mibBuilder.loadTexts:
    sqlServerReplicationDistEntry.setStatus("current")
_SsrdInstance_Type = InstanceName
_SsrdInstance_Object = MibTableColumn
ssrdInstance = _SsrdInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 36, 1, 1),
    _SsrdInstance_Type()
)
ssrdInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrdInstance.setStatus("current")
_SsrdDistDeliveredCmdsPerSec_Type = Gauge32
_SsrdDistDeliveredCmdsPerSec_Object = MibTableColumn
ssrdDistDeliveredCmdsPerSec = _SsrdDistDeliveredCmdsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 36, 1, 2),
    _SsrdDistDeliveredCmdsPerSec_Type()
)
ssrdDistDeliveredCmdsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrdDistDeliveredCmdsPerSec.setStatus("current")
_SsrdDistDeliveredTransPerSec_Type = Gauge32
_SsrdDistDeliveredTransPerSec_Object = MibTableColumn
ssrdDistDeliveredTransPerSec = _SsrdDistDeliveredTransPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 36, 1, 3),
    _SsrdDistDeliveredTransPerSec_Type()
)
ssrdDistDeliveredTransPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrdDistDeliveredTransPerSec.setStatus("current")
_SsrdDistDeliveryLatency_Type = Gauge32
_SsrdDistDeliveryLatency_Object = MibTableColumn
ssrdDistDeliveryLatency = _SsrdDistDeliveryLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 36, 1, 4),
    _SsrdDistDeliveryLatency_Type()
)
ssrdDistDeliveryLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrdDistDeliveryLatency.setStatus("current")
_SqlServerReplicationMergeTable_Object = MibTable
sqlServerReplicationMergeTable = _SqlServerReplicationMergeTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 37)
)
if mibBuilder.loadTexts:
    sqlServerReplicationMergeTable.setStatus("current")
_SqlServerReplicationMergeEntry_Object = MibTableRow
sqlServerReplicationMergeEntry = _SqlServerReplicationMergeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 37, 1)
)
sqlServerReplicationMergeEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "ssrmInstance"),
)
if mibBuilder.loadTexts:
    sqlServerReplicationMergeEntry.setStatus("current")
_SsrmInstance_Type = InstanceName
_SsrmInstance_Object = MibTableColumn
ssrmInstance = _SsrmInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 37, 1, 1),
    _SsrmInstance_Type()
)
ssrmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrmInstance.setStatus("current")
_SsrmConflictsPerSec_Type = Gauge32
_SsrmConflictsPerSec_Object = MibTableColumn
ssrmConflictsPerSec = _SsrmConflictsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 37, 1, 2),
    _SsrmConflictsPerSec_Type()
)
ssrmConflictsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrmConflictsPerSec.setStatus("current")
_SsrmDownloadedChangesPerSec_Type = Gauge32
_SsrmDownloadedChangesPerSec_Object = MibTableColumn
ssrmDownloadedChangesPerSec = _SsrmDownloadedChangesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 37, 1, 3),
    _SsrmDownloadedChangesPerSec_Type()
)
ssrmDownloadedChangesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrmDownloadedChangesPerSec.setStatus("current")
_SsrmUploadedChangesPerSec_Type = Gauge32
_SsrmUploadedChangesPerSec_Object = MibTableColumn
ssrmUploadedChangesPerSec = _SsrmUploadedChangesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 37, 1, 4),
    _SsrmUploadedChangesPerSec_Type()
)
ssrmUploadedChangesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssrmUploadedChangesPerSec.setStatus("current")
_SqlServerSQLErrorsTable_Object = MibTable
sqlServerSQLErrorsTable = _SqlServerSQLErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 38)
)
if mibBuilder.loadTexts:
    sqlServerSQLErrorsTable.setStatus("current")
_SqlServerSQLErrorsEntry_Object = MibTableRow
sqlServerSQLErrorsEntry = _SqlServerSQLErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 38, 1)
)
sqlServerSQLErrorsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "sseInstance"),
)
if mibBuilder.loadTexts:
    sqlServerSQLErrorsEntry.setStatus("current")
_SseInstance_Type = InstanceName
_SseInstance_Object = MibTableColumn
sseInstance = _SseInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 38, 1, 1),
    _SseInstance_Type()
)
sseInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sseInstance.setStatus("current")
_SseErrorsPerSec_Type = Gauge32
_SseErrorsPerSec_Object = MibTableColumn
sseErrorsPerSec = _SseErrorsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 38, 1, 2),
    _SseErrorsPerSec_Type()
)
sseErrorsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sseErrorsPerSec.setStatus("current")
_SqlServerSQLStatisticsTable_Object = MibTable
sqlServerSQLStatisticsTable = _SqlServerSQLStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 39)
)
if mibBuilder.loadTexts:
    sqlServerSQLStatisticsTable.setStatus("current")
_SqlServerSQLStatisticsEntry_Object = MibTableRow
sqlServerSQLStatisticsEntry = _SqlServerSQLStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 39, 1)
)
sqlServerSQLStatisticsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
)
if mibBuilder.loadTexts:
    sqlServerSQLStatisticsEntry.setStatus("current")
_SsssAutoParamAttemptsPerSec_Type = Gauge32
_SsssAutoParamAttemptsPerSec_Object = MibTableColumn
ssssAutoParamAttemptsPerSec = _SsssAutoParamAttemptsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 39, 1, 1),
    _SsssAutoParamAttemptsPerSec_Type()
)
ssssAutoParamAttemptsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssssAutoParamAttemptsPerSec.setStatus("current")
_SsssBatchRequestsPerSec_Type = Gauge32
_SsssBatchRequestsPerSec_Object = MibTableColumn
ssssBatchRequestsPerSec = _SsssBatchRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 39, 1, 2),
    _SsssBatchRequestsPerSec_Type()
)
ssssBatchRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssssBatchRequestsPerSec.setStatus("current")
_SsssFailedAutoParamsPerSec_Type = Gauge32
_SsssFailedAutoParamsPerSec_Object = MibTableColumn
ssssFailedAutoParamsPerSec = _SsssFailedAutoParamsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 39, 1, 3),
    _SsssFailedAutoParamsPerSec_Type()
)
ssssFailedAutoParamsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssssFailedAutoParamsPerSec.setStatus("current")
_SsssSQLAttentionRate_Type = Gauge32
_SsssSQLAttentionRate_Object = MibTableColumn
ssssSQLAttentionRate = _SsssSQLAttentionRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 39, 1, 4),
    _SsssSQLAttentionRate_Type()
)
ssssSQLAttentionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssssSQLAttentionRate.setStatus("current")
_SsssSQLCompilationsPerSec_Type = Gauge32
_SsssSQLCompilationsPerSec_Object = MibTableColumn
ssssSQLCompilationsPerSec = _SsssSQLCompilationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 39, 1, 5),
    _SsssSQLCompilationsPerSec_Type()
)
ssssSQLCompilationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssssSQLCompilationsPerSec.setStatus("current")
_SsssSQLReCompilationsPerSec_Type = Gauge32
_SsssSQLReCompilationsPerSec_Object = MibTableColumn
ssssSQLReCompilationsPerSec = _SsssSQLReCompilationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 39, 1, 6),
    _SsssSQLReCompilationsPerSec_Type()
)
ssssSQLReCompilationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssssSQLReCompilationsPerSec.setStatus("current")
_SsssSafeAutoParamsPerSec_Type = Gauge32
_SsssSafeAutoParamsPerSec_Object = MibTableColumn
ssssSafeAutoParamsPerSec = _SsssSafeAutoParamsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 39, 1, 7),
    _SsssSafeAutoParamsPerSec_Type()
)
ssssSafeAutoParamsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssssSafeAutoParamsPerSec.setStatus("current")
_SsssUnsafeAutoParamsPerSec_Type = Gauge32
_SsssUnsafeAutoParamsPerSec_Object = MibTableColumn
ssssUnsafeAutoParamsPerSec = _SsssUnsafeAutoParamsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 39, 1, 8),
    _SsssUnsafeAutoParamsPerSec_Type()
)
ssssUnsafeAutoParamsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssssUnsafeAutoParamsPerSec.setStatus("current")
_SqlServerTransactionsTable_Object = MibTable
sqlServerTransactionsTable = _SqlServerTransactionsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40)
)
if mibBuilder.loadTexts:
    sqlServerTransactionsTable.setStatus("current")
_SqlServerTransactionsEntry_Object = MibTableRow
sqlServerTransactionsEntry = _SqlServerTransactionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40, 1)
)
sqlServerTransactionsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
)
if mibBuilder.loadTexts:
    sqlServerTransactionsEntry.setStatus("current")
_SstFreeSpaceInTempdbKB_Type = Gauge32
_SstFreeSpaceInTempdbKB_Object = MibTableColumn
sstFreeSpaceInTempdbKB = _SstFreeSpaceInTempdbKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40, 1, 1),
    _SstFreeSpaceInTempdbKB_Type()
)
sstFreeSpaceInTempdbKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstFreeSpaceInTempdbKB.setStatus("current")
_SstLongestTransactionRunningTime_Type = Gauge32
_SstLongestTransactionRunningTime_Object = MibTableColumn
sstLongestTransactionRunningTime = _SstLongestTransactionRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40, 1, 2),
    _SstLongestTransactionRunningTime_Type()
)
sstLongestTransactionRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstLongestTransactionRunningTime.setStatus("current")
_SstNonSnapshotVersionTransactions_Type = Gauge32
_SstNonSnapshotVersionTransactions_Object = MibTableColumn
sstNonSnapshotVersionTransactions = _SstNonSnapshotVersionTransactions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40, 1, 3),
    _SstNonSnapshotVersionTransactions_Type()
)
sstNonSnapshotVersionTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstNonSnapshotVersionTransactions.setStatus("current")
_SstSnapshotTransactions_Type = Gauge32
_SstSnapshotTransactions_Object = MibTableColumn
sstSnapshotTransactions = _SstSnapshotTransactions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40, 1, 4),
    _SstSnapshotTransactions_Type()
)
sstSnapshotTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstSnapshotTransactions.setStatus("current")
_SstTransactions_Type = Gauge32
_SstTransactions_Object = MibTableColumn
sstTransactions = _SstTransactions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40, 1, 5),
    _SstTransactions_Type()
)
sstTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstTransactions.setStatus("current")
_SstUpdateSnapshotTransactions_Type = Gauge32
_SstUpdateSnapshotTransactions_Object = MibTableColumn
sstUpdateSnapshotTransactions = _SstUpdateSnapshotTransactions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40, 1, 6),
    _SstUpdateSnapshotTransactions_Type()
)
sstUpdateSnapshotTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstUpdateSnapshotTransactions.setStatus("current")
_SstUpdateConflictRatio_Type = Gauge32
_SstUpdateConflictRatio_Object = MibTableColumn
sstUpdateConflictRatio = _SstUpdateConflictRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40, 1, 7),
    _SstUpdateConflictRatio_Type()
)
sstUpdateConflictRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstUpdateConflictRatio.setStatus("current")
_SstVersionCleanupRateKBPerS_Type = Gauge32
_SstVersionCleanupRateKBPerS_Object = MibTableColumn
sstVersionCleanupRateKBPerS = _SstVersionCleanupRateKBPerS_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40, 1, 8),
    _SstVersionCleanupRateKBPerS_Type()
)
sstVersionCleanupRateKBPerS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstVersionCleanupRateKBPerS.setStatus("current")
_SstVersionGenerationRateKBPerS_Type = Gauge32
_SstVersionGenerationRateKBPerS_Object = MibTableColumn
sstVersionGenerationRateKBPerS = _SstVersionGenerationRateKBPerS_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40, 1, 9),
    _SstVersionGenerationRateKBPerS_Type()
)
sstVersionGenerationRateKBPerS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstVersionGenerationRateKBPerS.setStatus("current")
_SstVersionStoreSizeKB_Type = Gauge32
_SstVersionStoreSizeKB_Object = MibTableColumn
sstVersionStoreSizeKB = _SstVersionStoreSizeKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40, 1, 10),
    _SstVersionStoreSizeKB_Type()
)
sstVersionStoreSizeKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstVersionStoreSizeKB.setStatus("current")
_SstVersionStoreUnitCount_Type = Gauge32
_SstVersionStoreUnitCount_Object = MibTableColumn
sstVersionStoreUnitCount = _SstVersionStoreUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40, 1, 11),
    _SstVersionStoreUnitCount_Type()
)
sstVersionStoreUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstVersionStoreUnitCount.setStatus("current")
_SstVersionStoreUnitCreation_Type = Gauge32
_SstVersionStoreUnitCreation_Object = MibTableColumn
sstVersionStoreUnitCreation = _SstVersionStoreUnitCreation_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40, 1, 12),
    _SstVersionStoreUnitCreation_Type()
)
sstVersionStoreUnitCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstVersionStoreUnitCreation.setStatus("current")
_SstVersionStoreUnitTruncation_Type = Gauge32
_SstVersionStoreUnitTruncation_Object = MibTableColumn
sstVersionStoreUnitTruncation = _SstVersionStoreUnitTruncation_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 40, 1, 13),
    _SstVersionStoreUnitTruncation_Type()
)
sstVersionStoreUnitTruncation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstVersionStoreUnitTruncation.setStatus("current")
_SqlServerUserSettableTable_Object = MibTable
sqlServerUserSettableTable = _SqlServerUserSettableTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 41)
)
if mibBuilder.loadTexts:
    sqlServerUserSettableTable.setStatus("current")
_SqlServerUserSettableEntry_Object = MibTableRow
sqlServerUserSettableEntry = _SqlServerUserSettableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 41, 1)
)
sqlServerUserSettableEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "ssusInstance"),
)
if mibBuilder.loadTexts:
    sqlServerUserSettableEntry.setStatus("current")
_SsusInstance_Type = InstanceName
_SsusInstance_Object = MibTableColumn
ssusInstance = _SsusInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 41, 1, 1),
    _SsusInstance_Type()
)
ssusInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssusInstance.setStatus("current")
_SsusQuery_Type = Gauge32
_SsusQuery_Object = MibTableColumn
ssusQuery = _SsusQuery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 41, 1, 2),
    _SsusQuery_Type()
)
ssusQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssusQuery.setStatus("current")
_SqlServerWaitStatisticsTable_Object = MibTable
sqlServerWaitStatisticsTable = _SqlServerWaitStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42)
)
if mibBuilder.loadTexts:
    sqlServerWaitStatisticsTable.setStatus("current")
_SqlServerWaitStatisticsEntry_Object = MibTableRow
sqlServerWaitStatisticsEntry = _SqlServerWaitStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42, 1)
)
sqlServerWaitStatisticsEntry.setIndexNames(
    (0, "INFORMANT-SQLSERVER", "sqlServerNameIndex"),
    (0, "INFORMANT-SQLSERVER", "sswsInstance"),
)
if mibBuilder.loadTexts:
    sqlServerWaitStatisticsEntry.setStatus("current")
_SswsInstance_Type = InstanceName
_SswsInstance_Object = MibTableColumn
sswsInstance = _SswsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42, 1, 1),
    _SswsInstance_Type()
)
sswsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sswsInstance.setStatus("current")
_SswsLockWaits_Type = Gauge32
_SswsLockWaits_Object = MibTableColumn
sswsLockWaits = _SswsLockWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42, 1, 2),
    _SswsLockWaits_Type()
)
sswsLockWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sswsLockWaits.setStatus("current")
_SswsLogBufferWaits_Type = Gauge32
_SswsLogBufferWaits_Object = MibTableColumn
sswsLogBufferWaits = _SswsLogBufferWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42, 1, 3),
    _SswsLogBufferWaits_Type()
)
sswsLogBufferWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sswsLogBufferWaits.setStatus("current")
_SswsLogWriteWaits_Type = Gauge32
_SswsLogWriteWaits_Object = MibTableColumn
sswsLogWriteWaits = _SswsLogWriteWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42, 1, 4),
    _SswsLogWriteWaits_Type()
)
sswsLogWriteWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sswsLogWriteWaits.setStatus("current")
_SswsMemoryGrantQueueWaits_Type = Gauge32
_SswsMemoryGrantQueueWaits_Object = MibTableColumn
sswsMemoryGrantQueueWaits = _SswsMemoryGrantQueueWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42, 1, 5),
    _SswsMemoryGrantQueueWaits_Type()
)
sswsMemoryGrantQueueWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sswsMemoryGrantQueueWaits.setStatus("current")
_SswsNetworkIOWaits_Type = Gauge32
_SswsNetworkIOWaits_Object = MibTableColumn
sswsNetworkIOWaits = _SswsNetworkIOWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42, 1, 6),
    _SswsNetworkIOWaits_Type()
)
sswsNetworkIOWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sswsNetworkIOWaits.setStatus("current")
_SswsNonPageLatchWaits_Type = Gauge32
_SswsNonPageLatchWaits_Object = MibTableColumn
sswsNonPageLatchWaits = _SswsNonPageLatchWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42, 1, 7),
    _SswsNonPageLatchWaits_Type()
)
sswsNonPageLatchWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sswsNonPageLatchWaits.setStatus("current")
_SswsPageIOLatchWaits_Type = Gauge32
_SswsPageIOLatchWaits_Object = MibTableColumn
sswsPageIOLatchWaits = _SswsPageIOLatchWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42, 1, 8),
    _SswsPageIOLatchWaits_Type()
)
sswsPageIOLatchWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sswsPageIOLatchWaits.setStatus("current")
_SswsPageLatchWaits_Type = Gauge32
_SswsPageLatchWaits_Object = MibTableColumn
sswsPageLatchWaits = _SswsPageLatchWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42, 1, 9),
    _SswsPageLatchWaits_Type()
)
sswsPageLatchWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sswsPageLatchWaits.setStatus("current")
_SswsThreadSafeMemoryObjectsWaits_Type = Gauge32
_SswsThreadSafeMemoryObjectsWaits_Object = MibTableColumn
sswsThreadSafeMemoryObjectsWaits = _SswsThreadSafeMemoryObjectsWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42, 1, 10),
    _SswsThreadSafeMemoryObjectsWaits_Type()
)
sswsThreadSafeMemoryObjectsWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sswsThreadSafeMemoryObjectsWaits.setStatus("current")
_SswsTransactionOwnershipWaits_Type = Gauge32
_SswsTransactionOwnershipWaits_Object = MibTableColumn
sswsTransactionOwnershipWaits = _SswsTransactionOwnershipWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42, 1, 11),
    _SswsTransactionOwnershipWaits_Type()
)
sswsTransactionOwnershipWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sswsTransactionOwnershipWaits.setStatus("current")
_SswsWaitForTheWorker_Type = Gauge32
_SswsWaitForTheWorker_Object = MibTableColumn
sswsWaitForTheWorker = _SswsWaitForTheWorker_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42, 1, 12),
    _SswsWaitForTheWorker_Type()
)
sswsWaitForTheWorker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sswsWaitForTheWorker.setStatus("current")
_SswsWorkspaceSyncronizationWaits_Type = Gauge32
_SswsWorkspaceSyncronizationWaits_Object = MibTableColumn
sswsWorkspaceSyncronizationWaits = _SswsWorkspaceSyncronizationWaits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 3, 42, 1, 13),
    _SswsWorkspaceSyncronizationWaits_Type()
)
sswsWorkspaceSyncronizationWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sswsWorkspaceSyncronizationWaits.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFORMANT-SQLSERVER",
    **{"sqlServer": sqlServer,
       "analysisServerAggCache": analysisServerAggCache,
       "asacBytesAddedPerSec": asacBytesAddedPerSec,
       "asacCurrentBytes": asacCurrentBytes,
       "asacCurrentEntries": asacCurrentEntries,
       "asacDirectHitRatio": asacDirectHitRatio,
       "asacDirectHitsPerSec": asacDirectHitsPerSec,
       "asacEvictionsPerSec": asacEvictionsPerSec,
       "asacFilterHitRatio": asacFilterHitRatio,
       "asacFilterHitsPerSec": asacFilterHitsPerSec,
       "asacInsertsPerSec": asacInsertsPerSec,
       "asacLookupsPerSec": asacLookupsPerSec,
       "asacMissesPerSec": asacMissesPerSec,
       "asacTotalDirectHits": asacTotalDirectHits,
       "asacTotalEvictions": asacTotalEvictions,
       "asacTotalFilterHits": asacTotalFilterHits,
       "asacTotalInserts": asacTotalInserts,
       "asacTotalLookups": asacTotalLookups,
       "asacTotalMisses": asacTotalMisses,
       "analysisServerConnection": analysisServerConnection,
       "ascAuthenticationsPerSec": ascAuthenticationsPerSec,
       "ascCompletionsPerSec": ascCompletionsPerSec,
       "ascCurrentAgents": ascCurrentAgents,
       "ascCurrentAuthentications": ascCurrentAuthentications,
       "ascCurrentConnections": ascCurrentConnections,
       "ascCurrentConnectionsInProgress": ascCurrentConnectionsInProgress,
       "ascCurrentHttpConnections": ascCurrentHttpConnections,
       "ascFailuresPerSec": ascFailuresPerSec,
       "ascRequestsPerSec": ascRequestsPerSec,
       "ascSuccessesPerSec": ascSuccessesPerSec,
       "ascTotalAuthentications": ascTotalAuthentications,
       "ascTotalCompletions": ascTotalCompletions,
       "ascTotalFailures": ascTotalFailures,
       "ascTotalRequests": ascTotalRequests,
       "ascTotalSuccesses": ascTotalSuccesses,
       "analysisServerLastQuery": analysisServerLastQuery,
       "aslqAnswerFromCacheDirect": aslqAnswerFromCacheDirect,
       "aslqAnswerFromCacheFiltered": aslqAnswerFromCacheFiltered,
       "aslqAnswerFromFile": aslqAnswerFromFile,
       "aslqDSNRequested": aslqDSNRequested,
       "aslqDSNUsed": aslqDSNUsed,
       "aslqDataAvgBytesPerRead": aslqDataAvgBytesPerRead,
       "aslqDataAvgBytesPerRow": aslqDataAvgBytesPerRow,
       "aslqDataAvgRowsPerRead": aslqDataAvgRowsPerRead,
       "aslqDataBytes": aslqDataBytes,
       "aslqDataReads": aslqDataReads,
       "aslqIndexBytes": aslqIndexBytes,
       "aslqIndexReads": aslqIndexReads,
       "aslqMapBytes": aslqMapBytes,
       "aslqMapReads": aslqMapReads,
       "aslqQueryNum": aslqQueryNum,
       "aslqRowsCreated": aslqRowsCreated,
       "aslqRowsFilterExcluded": aslqRowsFilterExcluded,
       "aslqRowsFilterIncluded": aslqRowsFilterIncluded,
       "aslqRowsFiltered": aslqRowsFiltered,
       "aslqRowsRead": aslqRowsRead,
       "aslqTimeMs": aslqTimeMs,
       "aslqTotalBytes": aslqTotalBytes,
       "aslqTotalReads": aslqTotalReads,
       "analysisServerLocks": analysisServerLocks,
       "aslCurrentLatchWaits": aslCurrentLatchWaits,
       "aslCurrentLockWaits": aslCurrentLockWaits,
       "aslCurrentLocks": aslCurrentLocks,
       "aslLatchWaitsPerSec": aslLatchWaitsPerSec,
       "aslLockDenialsPerSec": aslLockDenialsPerSec,
       "aslLockGrantsPerSec": aslLockGrantsPerSec,
       "aslLockRequestsPerSec": aslLockRequestsPerSec,
       "aslLockWaitsPerSec": aslLockWaitsPerSec,
       "aslUnlockRequestsPerSec": aslUnlockRequestsPerSec,
       "analysisServerProc": analysisServerProc,
       "aspCurrentPartitions": aspCurrentPartitions,
       "aspCurrentThreads": aspCurrentThreads,
       "aspCurrentThreadsMerging": aspCurrentThreadsMerging,
       "aspCurrentThreadsReading": aspCurrentThreadsReading,
       "aspCurrentThreadsWriting": aspCurrentThreadsWriting,
       "aspFileBytesWrittenPerSec": aspFileBytesWrittenPerSec,
       "aspFileRowsWrittenPerSec": aspFileRowsWrittenPerSec,
       "aspMemorySizeBytes": aspMemorySizeBytes,
       "aspMemorySizeRows": aspMemorySizeRows,
       "aspRowsCreatedPerSec": aspRowsCreatedPerSec,
       "aspRowsMergedPerSec": aspRowsMergedPerSec,
       "aspRowsReadPerSec": aspRowsReadPerSec,
       "aspTotalPartitions": aspTotalPartitions,
       "aspTotalRows": aspTotalRows,
       "analysisServerProcAggs": analysisServerProcAggs,
       "aspaCurrentPartitions": aspaCurrentPartitions,
       "aspaMemorySizeBytes": aspaMemorySizeBytes,
       "aspaMemorySizeRows": aspaMemorySizeRows,
       "aspaRowsCreatedPerSec": aspaRowsCreatedPerSec,
       "aspaRowsMergedPerSec": aspaRowsMergedPerSec,
       "aspaTempFileBytesWrittenPerSec": aspaTempFileBytesWrittenPerSec,
       "aspaTempFileRowsWrittenPerSec": aspaTempFileRowsWrittenPerSec,
       "aspaTotalPartitions": aspaTotalPartitions,
       "analysisServerProcIndexes": analysisServerProcIndexes,
       "aspiCurrentPartitions": aspiCurrentPartitions,
       "aspiRowsPerSec": aspiRowsPerSec,
       "aspiTotalPartitions": aspiTotalPartitions,
       "aspiTotalRows": aspiTotalRows,
       "analysisServerQuery": analysisServerQuery,
       "asqAvgTimePerQuery": asqAvgTimePerQuery,
       "asqBytesSentPerSec": asqBytesSentPerSec,
       "asqCurrentProcessThreadPool": asqCurrentProcessThreadPool,
       "asqCurrentProcessThreadQueueLen": asqCurrentProcessThreadQueueLen,
       "asqCurrentProcessThreadsActive": asqCurrentProcessThreadsActive,
       "asqCurrentPyramidOperations": asqCurrentPyramidOperations,
       "asqCurrentQueries": asqCurrentQueries,
       "asqCurrentThreads": asqCurrentThreads,
       "asqCurrentWorkerThreadPool": asqCurrentWorkerThreadPool,
       "asqCurrentWorkerThreadsActive": asqCurrentWorkerThreadsActive,
       "asqDataBytesPerSec": asqDataBytesPerSec,
       "asqDataReadsPerSec": asqDataReadsPerSec,
       "asqFilterRowsExcludedPerSec": asqFilterRowsExcludedPerSec,
       "asqFilterRowsIncludedPerSec": asqFilterRowsIncludedPerSec,
       "asqFilteredRowsPerSec": asqFilteredRowsPerSec,
       "asqIndexBytesPerSec": asqIndexBytesPerSec,
       "asqIndexReadsPerSec": asqIndexReadsPerSec,
       "asqMapBytesPerSec": asqMapBytesPerSec,
       "asqMapReadsPerSec": asqMapReadsPerSec,
       "asqNetworkRoundTripsPerSec": asqNetworkRoundTripsPerSec,
       "asqPyramidOperationsPerSec": asqPyramidOperationsPerSec,
       "asqQueriesAnsweredPerSec": asqQueriesAnsweredPerSec,
       "asqQueriesFromCacheDirectPerSec": asqQueriesFromCacheDirectPerSec,
       "asqQueriesFromCacheFilterPerSec": asqQueriesFromCacheFilterPerSec,
       "asqQueriesFromFilePerSec": asqQueriesFromFilePerSec,
       "asqQueriesRequestedPerSec": asqQueriesRequestedPerSec,
       "asqRowsReadPerSec": asqRowsReadPerSec,
       "asqRowsSentPerSec": asqRowsSentPerSec,
       "asqTotalBytesSent": asqTotalBytesSent,
       "asqTotalNetworkRoundTrips": asqTotalNetworkRoundTrips,
       "asqTotalPyramidOperations": asqTotalPyramidOperations,
       "asqTotalQueriesAnswered": asqTotalQueriesAnswered,
       "asqTotalQueriesFromCacheDirect": asqTotalQueriesFromCacheDirect,
       "asqTotalQueriesFromCacheFiltered": asqTotalQueriesFromCacheFiltered,
       "asqTotalQueriesFromFile": asqTotalQueriesFromFile,
       "asqTotalQueriesRequested": asqTotalQueriesRequested,
       "asqTotalRowsSent": asqTotalRowsSent,
       "analysisServerQueryDims": analysisServerQueryDims,
       "asqdBytesPerSec": asqdBytesPerSec,
       "asqdCurrentRequests": asqdCurrentRequests,
       "asqdMembersPerSec": asqdMembersPerSec,
       "asqdRequestsPerSec": asqdRequestsPerSec,
       "asqdTotalVLDMRequests": asqdTotalVLDMRequests,
       "asqdTotalBytes": asqdTotalBytes,
       "asqdTotalMembers": asqdTotalMembers,
       "asqdTotalRequests": asqdTotalRequests,
       "asqdVLDMRequestsPerSec": asqdVLDMRequestsPerSec,
       "analysisServerStartup": analysisServerStartup,
       "assBytesPerSec": assBytesPerSec,
       "assMembersPerSec": assMembersPerSec,
       "assPropertiesPerSec": assPropertiesPerSec,
       "assServerUptime": assServerUptime,
       "assTotalBytes": assTotalBytes,
       "assTotalDimensions": assTotalDimensions,
       "assTotalMembers": assTotalMembers,
       "assTotalProperties": assTotalProperties,
       "microsoftGatherer": microsoftGatherer,
       "mgAccessingRobotsTxtFile": mgAccessingRobotsTxtFile,
       "mgActiveQueueLength": mgActiveQueueLength,
       "mgAdminClients": mgAdminClients,
       "mgAllNotificationsReceived": mgAllNotificationsReceived,
       "mgDelayedDocuments": mgDelayedDocuments,
       "mgDocumentEntries": mgDocumentEntries,
       "mgDocumentsDelayedRetry": mgDocumentsDelayedRetry,
       "mgDocumentsFiltered": mgDocumentsFiltered,
       "mgDocumentsFilteredRate": mgDocumentsFilteredRate,
       "mgDocumentsSuccessfullyFiltered": mgDocumentsSuccessfullyFiltered,
       "mgDocumentsSuccessfulFilterRate": mgDocumentsSuccessfulFilterRate,
       "mgExtNotificationsRate": mgExtNotificationsRate,
       "mgExtNotificationsReceived": mgExtNotificationsReceived,
       "mgFilterObjects": mgFilterObjects,
       "mgFilterProcessCreated": mgFilterProcessCreated,
       "mgFilterProcesses": mgFilterProcesses,
       "mgFilterProcessesMax": mgFilterProcessesMax,
       "mgFilteringThreads": mgFilteringThreads,
       "mgHeartbeats": mgHeartbeats,
       "mgHeartbeatsRate": mgHeartbeatsRate,
       "mgIdleThreads": mgIdleThreads,
       "mgNotificationSources": mgNotificationSources,
       "mgNotificationsRate": mgNotificationsRate,
       "mgPerformanceLevel": mgPerformanceLevel,
       "mgReasonToBackOff": mgReasonToBackOff,
       "mgRobotsTxtRequests": mgRobotsTxtRequests,
       "mgServerObjects": mgServerObjects,
       "mgServerObjectsCreated": mgServerObjectsCreated,
       "mgServersCurrentlyUnavailable": mgServersCurrentlyUnavailable,
       "mgServersUnavailable": mgServersUnavailable,
       "mgStemmersCached": mgStemmersCached,
       "mgSystemIOTrafficRate": mgSystemIOTrafficRate,
       "mgThreadsAccessingNetwork": mgThreadsAccessingNetwork,
       "mgThreadsInPlugIns": mgThreadsInPlugIns,
       "mgThreadsBlockedDueToBackOff": mgThreadsBlockedDueToBackOff,
       "mgTimeOuts": mgTimeOuts,
       "mgWordBreakersCached": mgWordBreakersCached,
       "microsoftGathererProjectsTable": microsoftGathererProjectsTable,
       "microsoftGathererProjectsEntry": microsoftGathererProjectsEntry,
       "mgpInstance": mgpInstance,
       "mgpAccessedFileRate": mgpAccessedFileRate,
       "mgpAccessedFiles": mgpAccessedFiles,
       "mgpAccessedHTTP": mgpAccessedHTTP,
       "mgpAccessedHTTPRate": mgpAccessedHTTPRate,
       "mgpAdaptiveCrawlAccepts": mgpAdaptiveCrawlAccepts,
       "mgpAdaptiveCrawlErrorSamples": mgpAdaptiveCrawlErrorSamples,
       "mgpAdaptiveCrawlErrors": mgpAdaptiveCrawlErrors,
       "mgpAdaptiveCrawlExcludes": mgpAdaptiveCrawlExcludes,
       "mgpAdaptiveCrawlFalsePositives": mgpAdaptiveCrawlFalsePositives,
       "mgpAdaptiveCrawlTotal": mgpAdaptiveCrawlTotal,
       "mgpChangedDocuments": mgpChangedDocuments,
       "mgpDelayedDocuments": mgpDelayedDocuments,
       "mgpDocumentAddRate": mgpDocumentAddRate,
       "mgpDocumentAdditions": mgpDocumentAdditions,
       "mgpDocumentDeleteRate": mgpDocumentDeleteRate,
       "mgpDocumentDeletes": mgpDocumentDeletes,
       "mgpDocumentModifies": mgpDocumentModifies,
       "mgpDocumentModifiesRate": mgpDocumentModifiesRate,
       "mgpDocumentMoveAndRenameRate": mgpDocumentMoveAndRenameRate,
       "mgpDocumentMovesPerRenames": mgpDocumentMovesPerRenames,
       "mgpDocumentsInProgress": mgpDocumentsInProgress,
       "mgpDocumentsOnHold": mgpDocumentsOnHold,
       "mgpErrorRate": mgpErrorRate,
       "mgpFileErrors": mgpFileErrors,
       "mgpFileErrorsRate": mgpFileErrorsRate,
       "mgpFilteredHTML": mgpFilteredHTML,
       "mgpFilteredHTMLRate": mgpFilteredHTMLRate,
       "mgpFilteredOffice": mgpFilteredOffice,
       "mgpFilteredOfficeRate": mgpFilteredOfficeRate,
       "mgpFilteredText": mgpFilteredText,
       "mgpFilteredTextRate": mgpFilteredTextRate,
       "mgpFilteringDocuments": mgpFilteringDocuments,
       "mgpGathererPausedFlag": mgpGathererPausedFlag,
       "mgpHTTPErrors": mgpHTTPErrors,
       "mgpHTTPErrorsRate": mgpHTTPErrorsRate,
       "mgpHistoryRecoveryProgress": mgpHistoryRecoveryProgress,
       "mgpIterateHistoryInProgressFlag": mgpIterateHistoryInProgressFlag,
       "mgpNotModified": mgpNotModified,
       "mgpProcessedDocuments": mgpProcessedDocuments,
       "mgpProcessedDocumentsRate": mgpProcessedDocumentsRate,
       "mgpRecoveryInProgressFlag": mgpRecoveryInProgressFlag,
       "mgpRetries": mgpRetries,
       "mgpRetriesRate": mgpRetriesRate,
       "mgpStartedDocuments": mgpStartedDocuments,
       "mgpStatusError": mgpStatusError,
       "mgpStatusSuccess": mgpStatusSuccess,
       "mgpSuccessRate": mgpSuccessRate,
       "mgpURLsInHistory": mgpURLsInHistory,
       "mgpUniqueDocuments": mgpUniqueDocuments,
       "mgpWaitingDocuments": mgpWaitingDocuments,
       "microsoftSearch": microsoftSearch,
       "msActiveThreads": msActiveThreads,
       "msCurrentConnections": msCurrentConnections,
       "msFailedQueries": msFailedQueries,
       "msFailedQueryRate": msFailedQueryRate,
       "msQueries": msQueries,
       "msQueryRate": msQueryRate,
       "msResultRate": msResultRate,
       "msResults": msResults,
       "msSucceededQueries": msSucceededQueries,
       "msSucceededQueryRate": msSucceededQueryRate,
       "msThreads": msThreads,
       "microsoftSearchCatalogsTable": microsoftSearchCatalogsTable,
       "microsoftSearchCatalogsEntry": microsoftSearchCatalogsEntry,
       "mscInstance": mscInstance,
       "mscCatalogSizeMBytes": mscCatalogSizeMBytes,
       "mscFailedQueries": mscFailedQueries,
       "mscFailedQueriesRate": mscFailedQueriesRate,
       "mscNumberOfDocuments": mscNumberOfDocuments,
       "mscPersistentIndexes": mscPersistentIndexes,
       "mscQueries": mscQueries,
       "mscQueriesRate": mscQueriesRate,
       "mscResults": mscResults,
       "mscResultsRate": mscResultsRate,
       "mscSuccessfulQueries": mscSuccessfulQueries,
       "mscSuccessfulQueriesRate": mscSuccessfulQueriesRate,
       "mscUniqueKeys": mscUniqueKeys,
       "microsoftSearchIndexCatalogTable": microsoftSearchIndexCatalogTable,
       "microsoftSearchIndexCatalogEntry": microsoftSearchIndexCatalogEntry,
       "msicInstance": msicInstance,
       "msicActiveDocuments": msicActiveDocuments,
       "msicBuildInProgress": msicBuildInProgress,
       "msicDocumentsFiltered": msicDocumentsFiltered,
       "msicDocumentsInProgress": msicDocumentsInProgress,
       "msicFilesToBeFiltered": msicFilesToBeFiltered,
       "msicIndexSizeMBytes": msicIndexSizeMBytes,
       "msicMergeProgress": msicMergeProgress,
       "msicNumberOfPropagations": msicNumberOfPropagations,
       "msicNumberOfDocuments": msicNumberOfDocuments,
       "msicPersistentIndexes": msicPersistentIndexes,
       "msicUniqueKeys": msicUniqueKeys,
       "msicWordlists": msicWordlists,
       "sqlServerNameTable": sqlServerNameTable,
       "sqlServerNameEntry": sqlServerNameEntry,
       "sqlServerNameIndex": sqlServerNameIndex,
       "sqlServerNameInstance": sqlServerNameInstance,
       "sqlServerAccessMethodsTable": sqlServerAccessMethodsTable,
       "sqlServerAccessMethodsEntry": sqlServerAccessMethodsEntry,
       "ssamAUCleanupBatchesPerSec": ssamAUCleanupBatchesPerSec,
       "ssamAUCleanupsPerSec": ssamAUCleanupsPerSec,
       "ssamDeferredDroppedRowsets": ssamDeferredDroppedRowsets,
       "ssamDeferredDroppedAUs": ssamDeferredDroppedAUs,
       "ssamDroppedRowsetCleanupsPerSec": ssamDroppedRowsetCleanupsPerSec,
       "ssamDroppedRowsetsSkippedPerSec": ssamDroppedRowsetsSkippedPerSec,
       "ssamExtentDeallocationsPerSec": ssamExtentDeallocationsPerSec,
       "ssamExtentsAllocatedPerSec": ssamExtentsAllocatedPerSec,
       "ssamFailedAUCleanupBatchesPerSec": ssamFailedAUCleanupBatchesPerSec,
       "ssamFailedLeafPageCookie": ssamFailedLeafPageCookie,
       "ssamFailedTreePageCookie": ssamFailedTreePageCookie,
       "ssamForwardedRecordsPerSec": ssamForwardedRecordsPerSec,
       "ssamFreeSpacePageFetchesPerSec": ssamFreeSpacePageFetchesPerSec,
       "ssamFreeSpaceScansPerSec": ssamFreeSpaceScansPerSec,
       "ssamFullScansPerSec": ssamFullScansPerSec,
       "ssamIndexSearchesPerSec": ssamIndexSearchesPerSec,
       "ssamMixedPageAllocationsPerSec": ssamMixedPageAllocationsPerSec,
       "ssamPageDeallocationsPerSec": ssamPageDeallocationsPerSec,
       "ssamPageSplitsPerSec": ssamPageSplitsPerSec,
       "ssamPagesAllocatedPerSec": ssamPagesAllocatedPerSec,
       "ssamProbeScansPerSec": ssamProbeScansPerSec,
       "ssamRangeScansPerSec": ssamRangeScansPerSec,
       "ssamScanPointRevalidationsPerSec": ssamScanPointRevalidationsPerSec,
       "ssamSkippedGhostedRecordsPerSec": ssamSkippedGhostedRecordsPerSec,
       "ssamTableLockEscalationsPerSec": ssamTableLockEscalationsPerSec,
       "ssamUsedLeafPageCookie": ssamUsedLeafPageCookie,
       "ssamUsedTreePageCookie": ssamUsedTreePageCookie,
       "ssamWorkfilesCreatedPerSec": ssamWorkfilesCreatedPerSec,
       "ssamWorktablesCreatedPerSec": ssamWorktablesCreatedPerSec,
       "ssamWorktablesFromCacheRatio": ssamWorktablesFromCacheRatio,
       "sqlServerBackupDeviceTable": sqlServerBackupDeviceTable,
       "sqlServerBackupDeviceEntry": sqlServerBackupDeviceEntry,
       "ssbdInstance": ssbdInstance,
       "ssbdDeviceThroughputBytesPerSec": ssbdDeviceThroughputBytesPerSec,
       "sqlServerBrokerActivationTable": sqlServerBrokerActivationTable,
       "sqlServerBrokerActivationEntry": sqlServerBrokerActivationEntry,
       "ssbaInstance": ssbaInstance,
       "ssbaStoredProceduresInvokedPerSec": ssbaStoredProceduresInvokedPerSec,
       "ssbaTaskLimitReached": ssbaTaskLimitReached,
       "ssbaTaskLimitReachedPerSec": ssbaTaskLimitReachedPerSec,
       "ssbaTasksAbortedPerSec": ssbaTasksAbortedPerSec,
       "ssbaTasksRunning": ssbaTasksRunning,
       "ssbaTasksStartedPerSec": ssbaTasksStartedPerSec,
       "sqlServerBrokerStatisticsTable": sqlServerBrokerStatisticsTable,
       "sqlServerBrokerStatisticsEntry": sqlServerBrokerStatisticsEntry,
       "ssbsBrokerTransactionRollbacks": ssbsBrokerTransactionRollbacks,
       "ssbsDialogTimerEventCount": ssbsDialogTimerEventCount,
       "ssbsEnqueuedLocalMessagesTotal": ssbsEnqueuedLocalMessagesTotal,
       "ssbsEnqueuedLocalMessagesPerSec": ssbsEnqueuedLocalMessagesPerSec,
       "ssbsEnqueuedMessagesTotal": ssbsEnqueuedMessagesTotal,
       "ssbsEnqueuedMessagesPerSec": ssbsEnqueuedMessagesPerSec,
       "ssbsEnqueuedTransportMsgFragTot": ssbsEnqueuedTransportMsgFragTot,
       "ssbsEnqueuedTransportMsgFragsPerSec": ssbsEnqueuedTransportMsgFragsPerSec,
       "ssbsEnqueuedTransportMsgsTotal": ssbsEnqueuedTransportMsgsTotal,
       "ssbsEnqueuedTransportMsgsPerSec": ssbsEnqueuedTransportMsgsPerSec,
       "ssbsForwardedMessagesTotal": ssbsForwardedMessagesTotal,
       "ssbsForwardedMessagesPerSec": ssbsForwardedMessagesPerSec,
       "ssbsForwardedMsgByteTotal": ssbsForwardedMsgByteTotal,
       "ssbsForwardedMsgBytesPerSec": ssbsForwardedMsgBytesPerSec,
       "ssbsForwardedMsgDiscardedTotal": ssbsForwardedMsgDiscardedTotal,
       "ssbsForwardedMsgsDiscardedPerSec": ssbsForwardedMsgsDiscardedPerSec,
       "ssbsForwardedPendingMsgBytes": ssbsForwardedPendingMsgBytes,
       "ssbsForwardedPendingMsgCount": ssbsForwardedPendingMsgCount,
       "ssbsSQLRECEIVETotal": ssbsSQLRECEIVETotal,
       "ssbsSQLRECEIVEsPerSec": ssbsSQLRECEIVEsPerSec,
       "ssbsSQLSENDTotal": ssbsSQLSENDTotal,
       "ssbsSQLSENDsPerSec": ssbsSQLSENDsPerSec,
       "ssbsTransportTimerEventCount": ssbsTransportTimerEventCount,
       "sqlServerBrokerTransportTable": sqlServerBrokerTransportTable,
       "sqlServerBrokerTransportEntry": sqlServerBrokerTransportEntry,
       "ssbtCurrentBytesForRecvIO": ssbtCurrentBytesForRecvIO,
       "ssbtCurrentBytesForSendIO": ssbtCurrentBytesForSendIO,
       "ssbtCurrentMsgFragsForSendIO": ssbtCurrentMsgFragsForSendIO,
       "ssbtMessageFragmentReceiveTotal": ssbtMessageFragmentReceiveTotal,
       "ssbtMessageFragmentReceivesPerSec": ssbtMessageFragmentReceivesPerSec,
       "ssbtMessageFragmentSendTotal": ssbtMessageFragmentSendTotal,
       "ssbtMessageFragmentSendsPerSec": ssbtMessageFragmentSendsPerSec,
       "ssbtMsgFragmentRecvSizeAvg": ssbtMsgFragmentRecvSizeAvg,
       "ssbtMsgFragmentSendSizeAvg": ssbtMsgFragmentSendSizeAvg,
       "ssbtOpenConnectionCount": ssbtOpenConnectionCount,
       "ssbtPendingBytesForRecvIO": ssbtPendingBytesForRecvIO,
       "ssbtPendingBytesForSendIO": ssbtPendingBytesForSendIO,
       "ssbtPendingMsgFragsForRecvIO": ssbtPendingMsgFragsForRecvIO,
       "ssbtPendingMsgFragsForSendIO": ssbtPendingMsgFragsForSendIO,
       "ssbtReceiveIOBytesTotal": ssbtReceiveIOBytesTotal,
       "ssbtReceiveIOLenAvg": ssbtReceiveIOLenAvg,
       "ssbtReceiveIOBytesPerSec": ssbtReceiveIOBytesPerSec,
       "ssbtReceiveIOsPerSec": ssbtReceiveIOsPerSec,
       "ssbtSendIOBytesTotal": ssbtSendIOBytesTotal,
       "ssbtSendIOLenAvg": ssbtSendIOLenAvg,
       "ssbtSendIOBytesPerSec": ssbtSendIOBytesPerSec,
       "ssbtSendIOsPerSec": ssbtSendIOsPerSec,
       "sqlServerBufferManagerTable": sqlServerBufferManagerTable,
       "sqlServerBufferManagerEntry": sqlServerBufferManagerEntry,
       "ssbmAWELookupMapsPerSec": ssbmAWELookupMapsPerSec,
       "ssbmAWEStolenMapsPerSec": ssbmAWEStolenMapsPerSec,
       "ssbmAWEUnmapCallsPerSec": ssbmAWEUnmapCallsPerSec,
       "ssbmAWEUnmapPagesPerSec": ssbmAWEUnmapPagesPerSec,
       "ssbmAWEWriteMapsPerSec": ssbmAWEWriteMapsPerSec,
       "ssbmBufferCacheHitRatio": ssbmBufferCacheHitRatio,
       "ssbmCheckpointPagesPerSec": ssbmCheckpointPagesPerSec,
       "ssbmDatabasePages": ssbmDatabasePages,
       "ssbmFreeListStallsPerSec": ssbmFreeListStallsPerSec,
       "ssbmFreePages": ssbmFreePages,
       "ssbmLazyWritesPerSec": ssbmLazyWritesPerSec,
       "ssbmPageLifeExpectancy": ssbmPageLifeExpectancy,
       "ssbmPageLookupsPerSec": ssbmPageLookupsPerSec,
       "ssbmPageReadsPerSec": ssbmPageReadsPerSec,
       "ssbmPageWritesPerSec": ssbmPageWritesPerSec,
       "ssbmProcedureCachePages": ssbmProcedureCachePages,
       "ssbmReadaheadPagesPerSec": ssbmReadaheadPagesPerSec,
       "ssbmReservedPages": ssbmReservedPages,
       "ssbmStolenPages": ssbmStolenPages,
       "ssbmTargetPages": ssbmTargetPages,
       "ssbmTotalPages": ssbmTotalPages,
       "sqlServerBufferPartitionTable": sqlServerBufferPartitionTable,
       "sqlServerBufferPartitionEntry": sqlServerBufferPartitionEntry,
       "ssbpInstance": ssbpInstance,
       "ssbpFreeListEmptyPerSec": ssbpFreeListEmptyPerSec,
       "ssbpFreeListRequestsPerSec": ssbpFreeListRequestsPerSec,
       "ssbpFreePages": ssbpFreePages,
       "sqlServerCacheManagerTable": sqlServerCacheManagerTable,
       "sqlServerCacheManagerEntry": sqlServerCacheManagerEntry,
       "sscmInstance": sscmInstance,
       "sscmCacheHitRatio": sscmCacheHitRatio,
       "sscmCacheObjectCounts": sscmCacheObjectCounts,
       "sscmCachePages": sscmCachePages,
       "sscmCacheUseCountsPerSec": sscmCacheUseCountsPerSec,
       "sqlServerCursorManagerTotalTable": sqlServerCursorManagerTotalTable,
       "sqlServerCursorManagerTotalEntry": sqlServerCursorManagerTotalEntry,
       "sscmtAsyncPopulationCount": sscmtAsyncPopulationCount,
       "sscmtCursorConversionRate": sscmtCursorConversionRate,
       "sscmtCursorFlushes": sscmtCursorFlushes,
       "sqlServerCursorManagerByTypeTable": sqlServerCursorManagerByTypeTable,
       "sqlServerCursorManagerByTypeEntry": sqlServerCursorManagerByTypeEntry,
       "sscmbtInstance": sscmbtInstance,
       "sscmbtActiveCursors": sscmbtActiveCursors,
       "sscmbtCacheHitRatio": sscmbtCacheHitRatio,
       "sscmbtCachedCursorCounts": sscmbtCachedCursorCounts,
       "sscmbtCursorCacheUseCountsPerSec": sscmbtCursorCacheUseCountsPerSec,
       "sscmbtCursorRequestsPerSec": sscmbtCursorRequestsPerSec,
       "sscmbtCursorMemoryUsage": sscmbtCursorMemoryUsage,
       "sscmbtCursorWorktableUsage": sscmbtCursorWorktableUsage,
       "sscmbtNumberOfActiveCursorPlans": sscmbtNumberOfActiveCursorPlans,
       "sqlServerDatabasesTable": sqlServerDatabasesTable,
       "sqlServerDatabasesEntry": sqlServerDatabasesEntry,
       "ssdInstance": ssdInstance,
       "ssdActiveTransactions": ssdActiveTransactions,
       "ssdBackupPerRestoreThroughputPerSec": ssdBackupPerRestoreThroughputPerSec,
       "ssdBulkCopyRowsPerSec": ssdBulkCopyRowsPerSec,
       "ssdBulkCopyThroughputPerSec": ssdBulkCopyThroughputPerSec,
       "ssdDBCCLogicalScanBytesPerSec": ssdDBCCLogicalScanBytesPerSec,
       "ssdDataFileSSizeKB": ssdDataFileSSizeKB,
       "ssdLogBytesFlushedPerSec": ssdLogBytesFlushedPerSec,
       "ssdLogCacheHitRatio": ssdLogCacheHitRatio,
       "ssdLogCacheReadsPerSec": ssdLogCacheReadsPerSec,
       "ssdLogFileSSizeKB": ssdLogFileSSizeKB,
       "ssdLogFileSUsedSizeKB": ssdLogFileSUsedSizeKB,
       "ssdLogFlushWaitTime": ssdLogFlushWaitTime,
       "ssdLogFlushWaitsPerSec": ssdLogFlushWaitsPerSec,
       "ssdLogFlushesPerSec": ssdLogFlushesPerSec,
       "ssdLogGrowths": ssdLogGrowths,
       "ssdLogShrinks": ssdLogShrinks,
       "ssdLogTruncations": ssdLogTruncations,
       "ssdMirroringAcksReceivedPerSec": ssdMirroringAcksReceivedPerSec,
       "ssdMirroringBytesSentPerSec": ssdMirroringBytesSentPerSec,
       "ssdMirroringPagesSentPerSec": ssdMirroringPagesSentPerSec,
       "ssdMirroringSendsPerSec": ssdMirroringSendsPerSec,
       "ssdMirroringTotalAcksReceived": ssdMirroringTotalAcksReceived,
       "ssdMirroringTotalBytesSent": ssdMirroringTotalBytesSent,
       "ssdMirroringTotalPagesSent": ssdMirroringTotalPagesSent,
       "ssdMirroringTotalSends": ssdMirroringTotalSends,
       "ssdMirroringTransactionDelay": ssdMirroringTransactionDelay,
       "ssdPercentLogUsed": ssdPercentLogUsed,
       "ssdReplPendingXacts": ssdReplPendingXacts,
       "ssdReplTransRate": ssdReplTransRate,
       "ssdShrinkDataMovementBytesPerSec": ssdShrinkDataMovementBytesPerSec,
       "ssdTransactionsPerSec": ssdTransactionsPerSec,
       "sqlServerExecStatisticsTable": sqlServerExecStatisticsTable,
       "sqlServerExecStatisticsEntry": sqlServerExecStatisticsEntry,
       "ssesInstance": ssesInstance,
       "ssesDTCCalls": ssesDTCCalls,
       "ssesDistributedQuery": ssesDistributedQuery,
       "ssesExtendedProcedures": ssesExtendedProcedures,
       "ssesOLEDBCalls": ssesOLEDBCalls,
       "sqlServerGeneralStatisticsTable": sqlServerGeneralStatisticsTable,
       "sqlServerGeneralStatisticsEntry": sqlServerGeneralStatisticsEntry,
       "ssgsHTTPAnonymousRequests": ssgsHTTPAnonymousRequests,
       "ssgsHTTPAuthenticatedRequests": ssgsHTTPAuthenticatedRequests,
       "ssgsLogicalConnections": ssgsLogicalConnections,
       "ssgsLoginsPerSec": ssgsLoginsPerSec,
       "ssgsLogoutsPerSec": ssgsLogoutsPerSec,
       "ssgsMarsDeadlocks": ssgsMarsDeadlocks,
       "ssgsNonAtomicYieldRate": ssgsNonAtomicYieldRate,
       "ssgsProcessesBlocked": ssgsProcessesBlocked,
       "ssgsSOAPEmptyRequests": ssgsSOAPEmptyRequests,
       "ssgsSOAPMethodInvocations": ssgsSOAPMethodInvocations,
       "ssgsSOAPSQLRequests": ssgsSOAPSQLRequests,
       "ssgsSOAPSessionInitiateRequests": ssgsSOAPSessionInitiateRequests,
       "ssgsSOAPSessionTerminateRequests": ssgsSOAPSessionTerminateRequests,
       "ssgsSOAPWSDLRequests": ssgsSOAPWSDLRequests,
       "ssgsTempTablesCreationRate": ssgsTempTablesCreationRate,
       "ssgsTransactions": ssgsTransactions,
       "ssgsUserConnections": ssgsUserConnections,
       "sqlServerLatchesTable": sqlServerLatchesTable,
       "sqlServerLatchesEntry": sqlServerLatchesEntry,
       "ssltAverageLatchWaitTimeMs": ssltAverageLatchWaitTimeMs,
       "ssltLatchWaitsPerSec": ssltLatchWaitsPerSec,
       "ssltTotalLatchWaitTimeMs": ssltTotalLatchWaitTimeMs,
       "sqlServerLocksTable": sqlServerLocksTable,
       "sqlServerLocksEntry": sqlServerLocksEntry,
       "sslkInstance": sslkInstance,
       "sslkAverageWaitTimeMs": sslkAverageWaitTimeMs,
       "sslkLockRequestsPerSec": sslkLockRequestsPerSec,
       "sslkLockTimeoutsTimeoutGT0PerSec": sslkLockTimeoutsTimeoutGT0PerSec,
       "sslkLockTimeoutsPerSec": sslkLockTimeoutsPerSec,
       "sslkLockWaitTimeMs": sslkLockWaitTimeMs,
       "sslkLockWaitsPerSec": sslkLockWaitsPerSec,
       "sslkNumberOfDeadlocksPerSec": sslkNumberOfDeadlocksPerSec,
       "sqlServerMemoryManagerTable": sqlServerMemoryManagerTable,
       "sqlServerMemoryManagerEntry": sqlServerMemoryManagerEntry,
       "ssmmConnectionMemoryKB": ssmmConnectionMemoryKB,
       "ssmmGrantedWorkspaceMemoryKB": ssmmGrantedWorkspaceMemoryKB,
       "ssmmLockBlocks": ssmmLockBlocks,
       "ssmmLockBlocksAllocated": ssmmLockBlocksAllocated,
       "ssmmLockMemoryKB": ssmmLockMemoryKB,
       "ssmmLockOwnerBlocks": ssmmLockOwnerBlocks,
       "ssmmLockOwnerBlocksAllocated": ssmmLockOwnerBlocksAllocated,
       "ssmmMaximumWorkspaceMemoryKB": ssmmMaximumWorkspaceMemoryKB,
       "ssmmMemoryGrantsOutstanding": ssmmMemoryGrantsOutstanding,
       "ssmmMemoryGrantsPending": ssmmMemoryGrantsPending,
       "ssmmOptimizerMemoryKB": ssmmOptimizerMemoryKB,
       "ssmmSQLCacheMemoryKB": ssmmSQLCacheMemoryKB,
       "ssmmTargetServerMemoryKB": ssmmTargetServerMemoryKB,
       "ssmmTotalServerMemoryKB": ssmmTotalServerMemoryKB,
       "sqlServerReplicateLogreaderTable": sqlServerReplicateLogreaderTable,
       "sqlServerReplicateLogreaderEntry": sqlServerReplicateLogreaderEntry,
       "ssrlInstance": ssrlInstance,
       "ssrlLogreaderDeliveredCmdsPerSec": ssrlLogreaderDeliveredCmdsPerSec,
       "ssrlLogreaderDelivereTransPerSec": ssrlLogreaderDelivereTransPerSec,
       "ssrlLogreaderDeliveryLatency": ssrlLogreaderDeliveryLatency,
       "sqlServerReplicateSnapshotTable": sqlServerReplicateSnapshotTable,
       "sqlServerReplicateSnapshotEntry": sqlServerReplicateSnapshotEntry,
       "ssrsInstance": ssrsInstance,
       "ssrsSnapshotDeliveredCmdsPerSec": ssrsSnapshotDeliveredCmdsPerSec,
       "ssrsSnapshotDeliveredTransPerSec": ssrsSnapshotDeliveredTransPerSec,
       "sqlServerReplicationAgentsTable": sqlServerReplicationAgentsTable,
       "sqlServerReplicationAgentsEntry": sqlServerReplicationAgentsEntry,
       "ssraInstance": ssraInstance,
       "ssraRunning": ssraRunning,
       "sqlServerReplicationDistTable": sqlServerReplicationDistTable,
       "sqlServerReplicationDistEntry": sqlServerReplicationDistEntry,
       "ssrdInstance": ssrdInstance,
       "ssrdDistDeliveredCmdsPerSec": ssrdDistDeliveredCmdsPerSec,
       "ssrdDistDeliveredTransPerSec": ssrdDistDeliveredTransPerSec,
       "ssrdDistDeliveryLatency": ssrdDistDeliveryLatency,
       "sqlServerReplicationMergeTable": sqlServerReplicationMergeTable,
       "sqlServerReplicationMergeEntry": sqlServerReplicationMergeEntry,
       "ssrmInstance": ssrmInstance,
       "ssrmConflictsPerSec": ssrmConflictsPerSec,
       "ssrmDownloadedChangesPerSec": ssrmDownloadedChangesPerSec,
       "ssrmUploadedChangesPerSec": ssrmUploadedChangesPerSec,
       "sqlServerSQLErrorsTable": sqlServerSQLErrorsTable,
       "sqlServerSQLErrorsEntry": sqlServerSQLErrorsEntry,
       "sseInstance": sseInstance,
       "sseErrorsPerSec": sseErrorsPerSec,
       "sqlServerSQLStatisticsTable": sqlServerSQLStatisticsTable,
       "sqlServerSQLStatisticsEntry": sqlServerSQLStatisticsEntry,
       "ssssAutoParamAttemptsPerSec": ssssAutoParamAttemptsPerSec,
       "ssssBatchRequestsPerSec": ssssBatchRequestsPerSec,
       "ssssFailedAutoParamsPerSec": ssssFailedAutoParamsPerSec,
       "ssssSQLAttentionRate": ssssSQLAttentionRate,
       "ssssSQLCompilationsPerSec": ssssSQLCompilationsPerSec,
       "ssssSQLReCompilationsPerSec": ssssSQLReCompilationsPerSec,
       "ssssSafeAutoParamsPerSec": ssssSafeAutoParamsPerSec,
       "ssssUnsafeAutoParamsPerSec": ssssUnsafeAutoParamsPerSec,
       "sqlServerTransactionsTable": sqlServerTransactionsTable,
       "sqlServerTransactionsEntry": sqlServerTransactionsEntry,
       "sstFreeSpaceInTempdbKB": sstFreeSpaceInTempdbKB,
       "sstLongestTransactionRunningTime": sstLongestTransactionRunningTime,
       "sstNonSnapshotVersionTransactions": sstNonSnapshotVersionTransactions,
       "sstSnapshotTransactions": sstSnapshotTransactions,
       "sstTransactions": sstTransactions,
       "sstUpdateSnapshotTransactions": sstUpdateSnapshotTransactions,
       "sstUpdateConflictRatio": sstUpdateConflictRatio,
       "sstVersionCleanupRateKBPerS": sstVersionCleanupRateKBPerS,
       "sstVersionGenerationRateKBPerS": sstVersionGenerationRateKBPerS,
       "sstVersionStoreSizeKB": sstVersionStoreSizeKB,
       "sstVersionStoreUnitCount": sstVersionStoreUnitCount,
       "sstVersionStoreUnitCreation": sstVersionStoreUnitCreation,
       "sstVersionStoreUnitTruncation": sstVersionStoreUnitTruncation,
       "sqlServerUserSettableTable": sqlServerUserSettableTable,
       "sqlServerUserSettableEntry": sqlServerUserSettableEntry,
       "ssusInstance": ssusInstance,
       "ssusQuery": ssusQuery,
       "sqlServerWaitStatisticsTable": sqlServerWaitStatisticsTable,
       "sqlServerWaitStatisticsEntry": sqlServerWaitStatisticsEntry,
       "sswsInstance": sswsInstance,
       "sswsLockWaits": sswsLockWaits,
       "sswsLogBufferWaits": sswsLogBufferWaits,
       "sswsLogWriteWaits": sswsLogWriteWaits,
       "sswsMemoryGrantQueueWaits": sswsMemoryGrantQueueWaits,
       "sswsNetworkIOWaits": sswsNetworkIOWaits,
       "sswsNonPageLatchWaits": sswsNonPageLatchWaits,
       "sswsPageIOLatchWaits": sswsPageIOLatchWaits,
       "sswsPageLatchWaits": sswsPageLatchWaits,
       "sswsThreadSafeMemoryObjectsWaits": sswsThreadSafeMemoryObjectsWaits,
       "sswsTransactionOwnershipWaits": sswsTransactionOwnershipWaits,
       "sswsWaitForTheWorker": sswsWaitForTheWorker,
       "sswsWorkspaceSyncronizationWaits": sswsWorkspaceSyncronizationWaits}
)
