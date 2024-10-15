# SNMP MIB module (INFORMANT-ISASERVER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INFORMANT-ISASERVER
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:15 2024
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

isaServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6)
)
isaServer.setRevisions(
        ("2007-05-24 22:39",
         "2006-06-02 01:18",
         "2004-03-13 06:11")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H323Filter_ObjectIdentity = ObjectIdentity
h323Filter = _H323Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 1)
)
if mibBuilder.loadTexts:
    h323Filter.setStatus("current")
_H323FilterActiveH323Calls_Type = Gauge32
_H323FilterActiveH323Calls_Object = MibScalar
h323FilterActiveH323Calls = _H323FilterActiveH323Calls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 1, 1),
    _H323FilterActiveH323Calls_Type()
)
h323FilterActiveH323Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323FilterActiveH323Calls.setStatus("current")
_H323FilterTotalH323Calls_Type = Gauge32
_H323FilterTotalH323Calls_Object = MibScalar
h323FilterTotalH323Calls = _H323FilterTotalH323Calls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 1, 2),
    _H323FilterTotalH323Calls_Type()
)
h323FilterTotalH323Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323FilterTotalH323Calls.setStatus("current")
_BandwidthControlTable_Object = MibTable
bandwidthControlTable = _BandwidthControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 2)
)
if mibBuilder.loadTexts:
    bandwidthControlTable.setStatus("current")
_BandwidthControlEntry_Object = MibTableRow
bandwidthControlEntry = _BandwidthControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 2, 1)
)
bandwidthControlEntry.setIndexNames(
    (0, "INFORMANT-ISASERVER", "bwCtrlInstance"),
)
if mibBuilder.loadTexts:
    bandwidthControlEntry.setStatus("current")
_BwCtrlInstance_Type = InstanceName
_BwCtrlInstance_Object = MibTableColumn
bwCtrlInstance = _BwCtrlInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 2, 1, 1),
    _BwCtrlInstance_Type()
)
bwCtrlInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwCtrlInstance.setStatus("current")
_BwCtrlActualInboundBandwidth_Type = Gauge32
_BwCtrlActualInboundBandwidth_Object = MibTableColumn
bwCtrlActualInboundBandwidth = _BwCtrlActualInboundBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 2, 1, 2),
    _BwCtrlActualInboundBandwidth_Type()
)
bwCtrlActualInboundBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwCtrlActualInboundBandwidth.setStatus("current")
_BwCtrlActualOutboundBandwidth_Type = Gauge32
_BwCtrlActualOutboundBandwidth_Object = MibTableColumn
bwCtrlActualOutboundBandwidth = _BwCtrlActualOutboundBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 2, 1, 3),
    _BwCtrlActualOutboundBandwidth_Type()
)
bwCtrlActualOutboundBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwCtrlActualOutboundBandwidth.setStatus("current")
_BwCtrlAssignedConnections_Type = Gauge32
_BwCtrlAssignedConnections_Object = MibTableColumn
bwCtrlAssignedConnections = _BwCtrlAssignedConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 2, 1, 4),
    _BwCtrlAssignedConnections_Type()
)
bwCtrlAssignedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwCtrlAssignedConnections.setStatus("current")
_BwCtrlAssignedInboundBandwidth_Type = Gauge32
_BwCtrlAssignedInboundBandwidth_Object = MibTableColumn
bwCtrlAssignedInboundBandwidth = _BwCtrlAssignedInboundBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 2, 1, 5),
    _BwCtrlAssignedInboundBandwidth_Type()
)
bwCtrlAssignedInboundBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwCtrlAssignedInboundBandwidth.setStatus("current")
_BwCtrlAssignedOutboundBandwidth_Type = Gauge32
_BwCtrlAssignedOutboundBandwidth_Object = MibTableColumn
bwCtrlAssignedOutboundBandwidth = _BwCtrlAssignedOutboundBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 2, 1, 6),
    _BwCtrlAssignedOutboundBandwidth_Type()
)
bwCtrlAssignedOutboundBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwCtrlAssignedOutboundBandwidth.setStatus("current")
_Cache_ObjectIdentity = ObjectIdentity
cache = _Cache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cache.setStatus("current")
_CacheActiveRefreshKBPerSec_Type = Gauge32
_CacheActiveRefreshKBPerSec_Object = MibScalar
cacheActiveRefreshKBPerSec = _CacheActiveRefreshKBPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 1),
    _CacheActiveRefreshKBPerSec_Type()
)
cacheActiveRefreshKBPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheActiveRefreshKBPerSec.setStatus("current")
_CacheActiveRefreshURLPerSec_Type = Gauge32
_CacheActiveRefreshURLPerSec_Object = MibScalar
cacheActiveRefreshURLPerSec = _CacheActiveRefreshURLPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 2),
    _CacheActiveRefreshURLPerSec_Type()
)
cacheActiveRefreshURLPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheActiveRefreshURLPerSec.setStatus("current")
_CacheDiskRetrievedKBPerSec_Type = Gauge32
_CacheDiskRetrievedKBPerSec_Object = MibScalar
cacheDiskRetrievedKBPerSec = _CacheDiskRetrievedKBPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 3),
    _CacheDiskRetrievedKBPerSec_Type()
)
cacheDiskRetrievedKBPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDiskRetrievedKBPerSec.setStatus("current")
_CacheDiskCacheAllocatedSpaceKB_Type = Gauge32
_CacheDiskCacheAllocatedSpaceKB_Object = MibScalar
cacheDiskCacheAllocatedSpaceKB = _CacheDiskCacheAllocatedSpaceKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 4),
    _CacheDiskCacheAllocatedSpaceKB_Type()
)
cacheDiskCacheAllocatedSpaceKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDiskCacheAllocatedSpaceKB.setStatus("current")
_CacheDiskContentWritesPerSec_Type = Gauge32
_CacheDiskContentWritesPerSec_Object = MibScalar
cacheDiskContentWritesPerSec = _CacheDiskContentWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 5),
    _CacheDiskContentWritesPerSec_Type()
)
cacheDiskContentWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDiskContentWritesPerSec.setStatus("current")
_CacheDiskFailPerSec_Type = Gauge32
_CacheDiskFailPerSec_Object = MibScalar
cacheDiskFailPerSec = _CacheDiskFailPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 6),
    _CacheDiskFailPerSec_Type()
)
cacheDiskFailPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDiskFailPerSec.setStatus("current")
_CacheDiskRetrieveURLPerSec_Type = Gauge32
_CacheDiskRetrieveURLPerSec_Object = MibScalar
cacheDiskRetrieveURLPerSec = _CacheDiskRetrieveURLPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 7),
    _CacheDiskRetrieveURLPerSec_Type()
)
cacheDiskRetrieveURLPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDiskRetrieveURLPerSec.setStatus("current")
_CacheMaxURLsCached_Type = Gauge32
_CacheMaxURLsCached_Object = MibScalar
cacheMaxURLsCached = _CacheMaxURLsCached_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 8),
    _CacheMaxURLsCached_Type()
)
cacheMaxURLsCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMaxURLsCached.setStatus("current")
_CacheMemoryRetrievedKBPerSec_Type = Gauge32
_CacheMemoryRetrievedKBPerSec_Object = MibScalar
cacheMemoryRetrievedKBPerSec = _CacheMemoryRetrievedKBPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 9),
    _CacheMemoryRetrievedKBPerSec_Type()
)
cacheMemoryRetrievedKBPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMemoryRetrievedKBPerSec.setStatus("current")
_CacheMemoryCacheAllocatedSpaceKB_Type = Gauge32
_CacheMemoryCacheAllocatedSpaceKB_Object = MibScalar
cacheMemoryCacheAllocatedSpaceKB = _CacheMemoryCacheAllocatedSpaceKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 10),
    _CacheMemoryCacheAllocatedSpaceKB_Type()
)
cacheMemoryCacheAllocatedSpaceKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMemoryCacheAllocatedSpaceKB.setStatus("current")
_CacheMemoryRetrieveURLPerSec_Type = Gauge32
_CacheMemoryRetrieveURLPerSec_Object = MibScalar
cacheMemoryRetrieveURLPerSec = _CacheMemoryRetrieveURLPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 11),
    _CacheMemoryRetrieveURLPerSec_Type()
)
cacheMemoryRetrieveURLPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMemoryRetrieveURLPerSec.setStatus("current")
_CacheMemoryUsageRatioPercent_Type = Gauge32
_CacheMemoryUsageRatioPercent_Object = MibScalar
cacheMemoryUsageRatioPercent = _CacheMemoryUsageRatioPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 12),
    _CacheMemoryUsageRatioPercent_Type()
)
cacheMemoryUsageRatioPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMemoryUsageRatioPercent.setStatus("current")
_CacheTotalActivelyRefreshedURLs_Type = Gauge32
_CacheTotalActivelyRefreshedURLs_Object = MibScalar
cacheTotalActivelyRefreshedURLs = _CacheTotalActivelyRefreshedURLs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 13),
    _CacheTotalActivelyRefreshedURLs_Type()
)
cacheTotalActivelyRefreshedURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalActivelyRefreshedURLs.setStatus("current")
_CacheTotalBytesActiveRefreshedKB_Type = Gauge32
_CacheTotalBytesActiveRefreshedKB_Object = MibScalar
cacheTotalBytesActiveRefreshedKB = _CacheTotalBytesActiveRefreshedKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 14),
    _CacheTotalBytesActiveRefreshedKB_Type()
)
cacheTotalBytesActiveRefreshedKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalBytesActiveRefreshedKB.setStatus("current")
_CacheTotalDiskBytesRetrievedKB_Type = Gauge32
_CacheTotalDiskBytesRetrievedKB_Object = MibScalar
cacheTotalDiskBytesRetrievedKB = _CacheTotalDiskBytesRetrievedKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 15),
    _CacheTotalDiskBytesRetrievedKB_Type()
)
cacheTotalDiskBytesRetrievedKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalDiskBytesRetrievedKB.setStatus("current")
_CacheTotalDiskFailures_Type = Gauge32
_CacheTotalDiskFailures_Object = MibScalar
cacheTotalDiskFailures = _CacheTotalDiskFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 16),
    _CacheTotalDiskFailures_Type()
)
cacheTotalDiskFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalDiskFailures.setStatus("current")
_CacheTotalDiskURLsRetrieved_Type = Gauge32
_CacheTotalDiskURLsRetrieved_Object = MibScalar
cacheTotalDiskURLsRetrieved = _CacheTotalDiskURLsRetrieved_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 17),
    _CacheTotalDiskURLsRetrieved_Type()
)
cacheTotalDiskURLsRetrieved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalDiskURLsRetrieved.setStatus("current")
_CacheTotalMemoryBytesRetrievedKB_Type = Gauge32
_CacheTotalMemoryBytesRetrievedKB_Object = MibScalar
cacheTotalMemoryBytesRetrievedKB = _CacheTotalMemoryBytesRetrievedKB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 18),
    _CacheTotalMemoryBytesRetrievedKB_Type()
)
cacheTotalMemoryBytesRetrievedKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalMemoryBytesRetrievedKB.setStatus("current")
_CacheTotalMemoryURLsRetrieved_Type = Gauge32
_CacheTotalMemoryURLsRetrieved_Object = MibScalar
cacheTotalMemoryURLsRetrieved = _CacheTotalMemoryURLsRetrieved_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 19),
    _CacheTotalMemoryURLsRetrieved_Type()
)
cacheTotalMemoryURLsRetrieved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalMemoryURLsRetrieved.setStatus("current")
_CacheTotalURLsCached_Type = Gauge32
_CacheTotalURLsCached_Object = MibScalar
cacheTotalURLsCached = _CacheTotalURLsCached_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 20),
    _CacheTotalURLsCached_Type()
)
cacheTotalURLsCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalURLsCached.setStatus("current")
_CacheURLCommitPerSec_Type = Gauge32
_CacheURLCommitPerSec_Object = MibScalar
cacheURLCommitPerSec = _CacheURLCommitPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 21),
    _CacheURLCommitPerSec_Type()
)
cacheURLCommitPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheURLCommitPerSec.setStatus("current")
_CacheURLsInCache_Type = Gauge32
_CacheURLsInCache_Object = MibScalar
cacheURLsInCache = _CacheURLsInCache_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 3, 22),
    _CacheURLsInCache_Type()
)
cacheURLsInCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheURLsInCache.setStatus("current")
_FirewallService_ObjectIdentity = ObjectIdentity
firewallService = _FirewallService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4)
)
if mibBuilder.loadTexts:
    firewallService.setStatus("current")
_FsAcceptingTCPConnections_Type = Gauge32
_FsAcceptingTCPConnections_Object = MibScalar
fsAcceptingTCPConnections = _FsAcceptingTCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 1),
    _FsAcceptingTCPConnections_Type()
)
fsAcceptingTCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAcceptingTCPConnections.setStatus("current")
_FsActiveSessions_Type = Gauge32
_FsActiveSessions_Object = MibScalar
fsActiveSessions = _FsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 2),
    _FsActiveSessions_Type()
)
fsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsActiveSessions.setStatus("current")
_FsActiveTCPConnections_Type = Gauge32
_FsActiveTCPConnections_Object = MibScalar
fsActiveTCPConnections = _FsActiveTCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 3),
    _FsActiveTCPConnections_Type()
)
fsActiveTCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsActiveTCPConnections.setStatus("current")
_FsActiveUDPConnections_Type = Gauge32
_FsActiveUDPConnections_Object = MibScalar
fsActiveUDPConnections = _FsActiveUDPConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 4),
    _FsActiveUDPConnections_Type()
)
fsActiveUDPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsActiveUDPConnections.setStatus("current")
_FsAvailableWorkerThreads_Type = Gauge32
_FsAvailableWorkerThreads_Object = MibScalar
fsAvailableWorkerThreads = _FsAvailableWorkerThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 5),
    _FsAvailableWorkerThreads_Type()
)
fsAvailableWorkerThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAvailableWorkerThreads.setStatus("current")
_FsBackConnectingTCPConnections_Type = Gauge32
_FsBackConnectingTCPConnections_Object = MibScalar
fsBackConnectingTCPConnections = _FsBackConnectingTCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 6),
    _FsBackConnectingTCPConnections_Type()
)
fsBackConnectingTCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBackConnectingTCPConnections.setStatus("current")
_FsBytesReadPerSec_Type = Gauge32
_FsBytesReadPerSec_Object = MibScalar
fsBytesReadPerSec = _FsBytesReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 7),
    _FsBytesReadPerSec_Type()
)
fsBytesReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBytesReadPerSec.setStatus("current")
_FsBytesWrittenPerSec_Type = Gauge32
_FsBytesWrittenPerSec_Object = MibScalar
fsBytesWrittenPerSec = _FsBytesWrittenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 8),
    _FsBytesWrittenPerSec_Type()
)
fsBytesWrittenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBytesWrittenPerSec.setStatus("current")
_FsConnectingTCPConnections_Type = Gauge32
_FsConnectingTCPConnections_Object = MibScalar
fsConnectingTCPConnections = _FsConnectingTCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 9),
    _FsConnectingTCPConnections_Type()
)
fsConnectingTCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsConnectingTCPConnections.setStatus("current")
_FsDNSCacheEntries_Type = Gauge32
_FsDNSCacheEntries_Object = MibScalar
fsDNSCacheEntries = _FsDNSCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 10),
    _FsDNSCacheEntries_Type()
)
fsDNSCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDNSCacheEntries.setStatus("current")
_FsDNSCacheFlushes_Type = Gauge32
_FsDNSCacheFlushes_Object = MibScalar
fsDNSCacheFlushes = _FsDNSCacheFlushes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 11),
    _FsDNSCacheFlushes_Type()
)
fsDNSCacheFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDNSCacheFlushes.setStatus("current")
_FsDNSCacheHits_Type = Gauge32
_FsDNSCacheHits_Object = MibScalar
fsDNSCacheHits = _FsDNSCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 12),
    _FsDNSCacheHits_Type()
)
fsDNSCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDNSCacheHits.setStatus("current")
_FsDNSCacheHitsPercent_Type = Gauge32
_FsDNSCacheHitsPercent_Object = MibScalar
fsDNSCacheHitsPercent = _FsDNSCacheHitsPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 13),
    _FsDNSCacheHitsPercent_Type()
)
fsDNSCacheHitsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDNSCacheHitsPercent.setStatus("current")
_FsDNSRetrievals_Type = Gauge32
_FsDNSRetrievals_Object = MibScalar
fsDNSRetrievals = _FsDNSRetrievals_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 14),
    _FsDNSRetrievals_Type()
)
fsDNSRetrievals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDNSRetrievals.setStatus("current")
_FsFailedDNSResolutions_Type = Gauge32
_FsFailedDNSResolutions_Object = MibScalar
fsFailedDNSResolutions = _FsFailedDNSResolutions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 15),
    _FsFailedDNSResolutions_Type()
)
fsFailedDNSResolutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFailedDNSResolutions.setStatus("current")
_FsKernelModeDataPumps_Type = Gauge32
_FsKernelModeDataPumps_Object = MibScalar
fsKernelModeDataPumps = _FsKernelModeDataPumps_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 16),
    _FsKernelModeDataPumps_Type()
)
fsKernelModeDataPumps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsKernelModeDataPumps.setStatus("current")
_FsListeningTCPConnections_Type = Gauge32
_FsListeningTCPConnections_Object = MibScalar
fsListeningTCPConnections = _FsListeningTCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 17),
    _FsListeningTCPConnections_Type()
)
fsListeningTCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsListeningTCPConnections.setStatus("current")
_FsNonConnectedUDPMappings_Type = Gauge32
_FsNonConnectedUDPMappings_Object = MibScalar
fsNonConnectedUDPMappings = _FsNonConnectedUDPMappings_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 18),
    _FsNonConnectedUDPMappings_Type()
)
fsNonConnectedUDPMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNonConnectedUDPMappings.setStatus("current")
_FsPendingDNSResolutions_Type = Gauge32
_FsPendingDNSResolutions_Object = MibScalar
fsPendingDNSResolutions = _FsPendingDNSResolutions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 19),
    _FsPendingDNSResolutions_Type()
)
fsPendingDNSResolutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPendingDNSResolutions.setStatus("current")
_FsSecureNATMappings_Type = Gauge32
_FsSecureNATMappings_Object = MibScalar
fsSecureNATMappings = _FsSecureNATMappings_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 20),
    _FsSecureNATMappings_Type()
)
fsSecureNATMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSecureNATMappings.setStatus("current")
_FsSuccessfulDNSResolutions_Type = Gauge32
_FsSuccessfulDNSResolutions_Object = MibScalar
fsSuccessfulDNSResolutions = _FsSuccessfulDNSResolutions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 21),
    _FsSuccessfulDNSResolutions_Type()
)
fsSuccessfulDNSResolutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSuccessfulDNSResolutions.setStatus("current")
_FsTCPBytesXferPerSecByKernelMode_Type = Gauge32
_FsTCPBytesXferPerSecByKernelMode_Object = MibScalar
fsTCPBytesXferPerSecByKernelMode = _FsTCPBytesXferPerSecByKernelMode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 22),
    _FsTCPBytesXferPerSecByKernelMode_Type()
)
fsTCPBytesXferPerSecByKernelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTCPBytesXferPerSecByKernelMode.setStatus("current")
_FsUDPBytesXferPerSecByKernelMode_Type = Gauge32
_FsUDPBytesXferPerSecByKernelMode_Object = MibScalar
fsUDPBytesXferPerSecByKernelMode = _FsUDPBytesXferPerSecByKernelMode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 23),
    _FsUDPBytesXferPerSecByKernelMode_Type()
)
fsUDPBytesXferPerSecByKernelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUDPBytesXferPerSecByKernelMode.setStatus("current")
_FsWorkerThreads_Type = Gauge32
_FsWorkerThreads_Object = MibScalar
fsWorkerThreads = _FsWorkerThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 24),
    _FsWorkerThreads_Type()
)
fsWorkerThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWorkerThreads.setStatus("current")
_FsAvailableUDPMappings_Type = Gauge32
_FsAvailableUDPMappings_Object = MibScalar
fsAvailableUDPMappings = _FsAvailableUDPMappings_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 25),
    _FsAvailableUDPMappings_Type()
)
fsAvailableUDPMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAvailableUDPMappings.setStatus("current")
_FsDNSCacheLockFailures_Type = Gauge32
_FsDNSCacheLockFailures_Object = MibScalar
fsDNSCacheLockFailures = _FsDNSCacheLockFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 26),
    _FsDNSCacheLockFailures_Type()
)
fsDNSCacheLockFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDNSCacheLockFailures.setStatus("current")
_FsPendingTCPConnections_Type = Gauge32
_FsPendingTCPConnections_Object = MibScalar
fsPendingTCPConnections = _FsPendingTCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 27),
    _FsPendingTCPConnections_Type()
)
fsPendingTCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPendingTCPConnections.setStatus("current")
_FsTCPAwaitInConnectCallToFinish_Type = Gauge32
_FsTCPAwaitInConnectCallToFinish_Object = MibScalar
fsTCPAwaitInConnectCallToFinish = _FsTCPAwaitInConnectCallToFinish_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 4, 28),
    _FsTCPAwaitInConnectCallToFinish_Type()
)
fsTCPAwaitInConnectCallToFinish.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTCPAwaitInConnectCallToFinish.setStatus("current")
_FirewallEngine_ObjectIdentity = ObjectIdentity
firewallEngine = _FirewallEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 5)
)
if mibBuilder.loadTexts:
    firewallEngine.setStatus("current")
_FeActiveConnections_Type = Gauge32
_FeActiveConnections_Object = MibScalar
feActiveConnections = _FeActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 5, 1),
    _FeActiveConnections_Type()
)
feActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feActiveConnections.setStatus("current")
_FeAllowedPackets_Type = Gauge32
_FeAllowedPackets_Object = MibScalar
feAllowedPackets = _FeAllowedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 5, 2),
    _FeAllowedPackets_Type()
)
feAllowedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAllowedPackets.setStatus("current")
_FeAllowedPacketsPerSec_Type = Gauge32
_FeAllowedPacketsPerSec_Object = MibScalar
feAllowedPacketsPerSec = _FeAllowedPacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 5, 3),
    _FeAllowedPacketsPerSec_Type()
)
feAllowedPacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAllowedPacketsPerSec.setStatus("current")
_FeBackloggedPackets_Type = Gauge32
_FeBackloggedPackets_Object = MibScalar
feBackloggedPackets = _FeBackloggedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 5, 4),
    _FeBackloggedPackets_Type()
)
feBackloggedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feBackloggedPackets.setStatus("current")
_FeBytes_Type = Gauge32
_FeBytes_Object = MibScalar
feBytes = _FeBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 5, 5),
    _FeBytes_Type()
)
feBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feBytes.setStatus("current")
_FeBytesPerSec_Type = Gauge32
_FeBytesPerSec_Object = MibScalar
feBytesPerSec = _FeBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 5, 6),
    _FeBytesPerSec_Type()
)
feBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feBytesPerSec.setStatus("current")
_FeConnectionsPerSec_Type = Gauge32
_FeConnectionsPerSec_Object = MibScalar
feConnectionsPerSec = _FeConnectionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 5, 7),
    _FeConnectionsPerSec_Type()
)
feConnectionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feConnectionsPerSec.setStatus("current")
_FeDroppedPackets_Type = Gauge32
_FeDroppedPackets_Object = MibScalar
feDroppedPackets = _FeDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 5, 8),
    _FeDroppedPackets_Type()
)
feDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDroppedPackets.setStatus("current")
_FeDroppedPacketsPerSec_Type = Gauge32
_FeDroppedPacketsPerSec_Object = MibScalar
feDroppedPacketsPerSec = _FeDroppedPacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 5, 9),
    _FeDroppedPacketsPerSec_Type()
)
feDroppedPacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDroppedPacketsPerSec.setStatus("current")
_FePackets_Type = Gauge32
_FePackets_Object = MibScalar
fePackets = _FePackets_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 5, 10),
    _FePackets_Type()
)
fePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePackets.setStatus("current")
_FePacketsPerSec_Type = Gauge32
_FePacketsPerSec_Object = MibScalar
fePacketsPerSec = _FePacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 5, 11),
    _FePacketsPerSec_Type()
)
fePacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePacketsPerSec.setStatus("current")
_FeTCPEstablishedConnsPerSec_Type = Gauge32
_FeTCPEstablishedConnsPerSec_Object = MibScalar
feTCPEstablishedConnsPerSec = _FeTCPEstablishedConnsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 5, 12),
    _FeTCPEstablishedConnsPerSec_Type()
)
feTCPEstablishedConnsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTCPEstablishedConnsPerSec.setStatus("current")
_FeTCPEstablishedConns_Type = Gauge32
_FeTCPEstablishedConns_Object = MibScalar
feTCPEstablishedConns = _FeTCPEstablishedConns_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 5, 13),
    _FeTCPEstablishedConns_Type()
)
feTCPEstablishedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTCPEstablishedConns.setStatus("current")
_PacketFilter_ObjectIdentity = ObjectIdentity
packetFilter = _PacketFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 6)
)
_PacketsDroppedFilterDenial_Type = Gauge32
_PacketsDroppedFilterDenial_Object = MibScalar
packetsDroppedFilterDenial = _PacketsDroppedFilterDenial_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 6, 1),
    _PacketsDroppedFilterDenial_Type()
)
packetsDroppedFilterDenial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetsDroppedFilterDenial.setStatus("current")
_PacketsDroppedProtocolViolation_Type = Gauge32
_PacketsDroppedProtocolViolation_Object = MibScalar
packetsDroppedProtocolViolation = _PacketsDroppedProtocolViolation_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 6, 2),
    _PacketsDroppedProtocolViolation_Type()
)
packetsDroppedProtocolViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetsDroppedProtocolViolation.setStatus("current")
_TotalDroppedPackets_Type = Gauge32
_TotalDroppedPackets_Object = MibScalar
totalDroppedPackets = _TotalDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 6, 3),
    _TotalDroppedPackets_Type()
)
totalDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalDroppedPackets.setStatus("current")
_TotalLoggingPacketsLost_Type = Gauge32
_TotalLoggingPacketsLost_Object = MibScalar
totalLoggingPacketsLost = _TotalLoggingPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 6, 4),
    _TotalLoggingPacketsLost_Type()
)
totalLoggingPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalLoggingPacketsLost.setStatus("current")
_TotalIncomingConn_Type = Gauge32
_TotalIncomingConn_Object = MibScalar
totalIncomingConn = _TotalIncomingConn_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 6, 5),
    _TotalIncomingConn_Type()
)
totalIncomingConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalIncomingConn.setStatus("current")
_WebProxyService_ObjectIdentity = ObjectIdentity
webProxyService = _WebProxyService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7)
)
if mibBuilder.loadTexts:
    webProxyService.setStatus("current")
_WpsArrayBytesReceivedPerSec_Type = Gauge32
_WpsArrayBytesReceivedPerSec_Object = MibScalar
wpsArrayBytesReceivedPerSec = _WpsArrayBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 1),
    _WpsArrayBytesReceivedPerSec_Type()
)
wpsArrayBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsArrayBytesReceivedPerSec.setStatus("current")
_WpsArrayBytesSentPerSec_Type = Gauge32
_WpsArrayBytesSentPerSec_Object = MibScalar
wpsArrayBytesSentPerSec = _WpsArrayBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 2),
    _WpsArrayBytesSentPerSec_Type()
)
wpsArrayBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsArrayBytesSentPerSec.setStatus("current")
_WpsArrayBytesTotalPerSec_Type = Gauge32
_WpsArrayBytesTotalPerSec_Object = MibScalar
wpsArrayBytesTotalPerSec = _WpsArrayBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 3),
    _WpsArrayBytesTotalPerSec_Type()
)
wpsArrayBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsArrayBytesTotalPerSec.setStatus("current")
_WpsCacheHitRatioPercent_Type = Gauge32
_WpsCacheHitRatioPercent_Object = MibScalar
wpsCacheHitRatioPercent = _WpsCacheHitRatioPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 4),
    _WpsCacheHitRatioPercent_Type()
)
wpsCacheHitRatioPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsCacheHitRatioPercent.setStatus("current")
_WpsCacheRunningHitRatioPercent_Type = Gauge32
_WpsCacheRunningHitRatioPercent_Object = MibScalar
wpsCacheRunningHitRatioPercent = _WpsCacheRunningHitRatioPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 5),
    _WpsCacheRunningHitRatioPercent_Type()
)
wpsCacheRunningHitRatioPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsCacheRunningHitRatioPercent.setStatus("current")
_WpsClientBytesReceivedPerSec_Type = Gauge32
_WpsClientBytesReceivedPerSec_Object = MibScalar
wpsClientBytesReceivedPerSec = _WpsClientBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 6),
    _WpsClientBytesReceivedPerSec_Type()
)
wpsClientBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsClientBytesReceivedPerSec.setStatus("current")
_WpsClientBytesSentPerSec_Type = Gauge32
_WpsClientBytesSentPerSec_Object = MibScalar
wpsClientBytesSentPerSec = _WpsClientBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 7),
    _WpsClientBytesSentPerSec_Type()
)
wpsClientBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsClientBytesSentPerSec.setStatus("current")
_WpsClientBytesTotalPerSec_Type = Gauge32
_WpsClientBytesTotalPerSec_Object = MibScalar
wpsClientBytesTotalPerSec = _WpsClientBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 8),
    _WpsClientBytesTotalPerSec_Type()
)
wpsClientBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsClientBytesTotalPerSec.setStatus("current")
_WpsConnectErrors_Type = Gauge32
_WpsConnectErrors_Object = MibScalar
wpsConnectErrors = _WpsConnectErrors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 9),
    _WpsConnectErrors_Type()
)
wpsConnectErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsConnectErrors.setStatus("current")
_WpsConnErrsPerTotalErrsPercent_Type = Gauge32
_WpsConnErrsPerTotalErrsPercent_Object = MibScalar
wpsConnErrsPerTotalErrsPercent = _WpsConnErrsPerTotalErrsPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 10),
    _WpsConnErrsPerTotalErrsPercent_Type()
)
wpsConnErrsPerTotalErrsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsConnErrsPerTotalErrsPercent.setStatus("current")
_WpsCurArrayFetchAvgMSPerRequest_Type = Gauge32
_WpsCurArrayFetchAvgMSPerRequest_Object = MibScalar
wpsCurArrayFetchAvgMSPerRequest = _WpsCurArrayFetchAvgMSPerRequest_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 11),
    _WpsCurArrayFetchAvgMSPerRequest_Type()
)
wpsCurArrayFetchAvgMSPerRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsCurArrayFetchAvgMSPerRequest.setStatus("current")
_WpsCurAvgMSPerRequest_Type = Gauge32
_WpsCurAvgMSPerRequest_Object = MibScalar
wpsCurAvgMSPerRequest = _WpsCurAvgMSPerRequest_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 12),
    _WpsCurAvgMSPerRequest_Type()
)
wpsCurAvgMSPerRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsCurAvgMSPerRequest.setStatus("current")
_WpsCurCacheFetchAvgMSPerRequest_Type = Gauge32
_WpsCurCacheFetchAvgMSPerRequest_Object = MibScalar
wpsCurCacheFetchAvgMSPerRequest = _WpsCurCacheFetchAvgMSPerRequest_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 13),
    _WpsCurCacheFetchAvgMSPerRequest_Type()
)
wpsCurCacheFetchAvgMSPerRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsCurCacheFetchAvgMSPerRequest.setStatus("current")
_WpsCurDirectFetchAvgMSPerRequest_Type = Gauge32
_WpsCurDirectFetchAvgMSPerRequest_Object = MibScalar
wpsCurDirectFetchAvgMSPerRequest = _WpsCurDirectFetchAvgMSPerRequest_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 14),
    _WpsCurDirectFetchAvgMSPerRequest_Type()
)
wpsCurDirectFetchAvgMSPerRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsCurDirectFetchAvgMSPerRequest.setStatus("current")
_WpsCurrentUsers_Type = Gauge32
_WpsCurrentUsers_Object = MibScalar
wpsCurrentUsers = _WpsCurrentUsers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 15),
    _WpsCurrentUsers_Type()
)
wpsCurrentUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsCurrentUsers.setStatus("current")
_WpsDNSCacheEntries_Type = Gauge32
_WpsDNSCacheEntries_Object = MibScalar
wpsDNSCacheEntries = _WpsDNSCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 16),
    _WpsDNSCacheEntries_Type()
)
wpsDNSCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsDNSCacheEntries.setStatus("current")
_WpsDNSCacheFlushes_Type = Gauge32
_WpsDNSCacheFlushes_Object = MibScalar
wpsDNSCacheFlushes = _WpsDNSCacheFlushes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 17),
    _WpsDNSCacheFlushes_Type()
)
wpsDNSCacheFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsDNSCacheFlushes.setStatus("current")
_WpsDNSCacheHits_Type = Gauge32
_WpsDNSCacheHits_Object = MibScalar
wpsDNSCacheHits = _WpsDNSCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 18),
    _WpsDNSCacheHits_Type()
)
wpsDNSCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsDNSCacheHits.setStatus("current")
_WpsDNSCacheHitsPercent_Type = Gauge32
_WpsDNSCacheHitsPercent_Object = MibScalar
wpsDNSCacheHitsPercent = _WpsDNSCacheHitsPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 19),
    _WpsDNSCacheHitsPercent_Type()
)
wpsDNSCacheHitsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsDNSCacheHitsPercent.setStatus("current")
_WpsDNSRetrievals_Type = Gauge32
_WpsDNSRetrievals_Object = MibScalar
wpsDNSRetrievals = _WpsDNSRetrievals_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 20),
    _WpsDNSRetrievals_Type()
)
wpsDNSRetrievals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsDNSRetrievals.setStatus("current")
_WpsFailRqstsPerTotalRqstsPercent_Type = Gauge32
_WpsFailRqstsPerTotalRqstsPercent_Object = MibScalar
wpsFailRqstsPerTotalRqstsPercent = _WpsFailRqstsPerTotalRqstsPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 21),
    _WpsFailRqstsPerTotalRqstsPercent_Type()
)
wpsFailRqstsPerTotalRqstsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsFailRqstsPerTotalRqstsPercent.setStatus("current")
_WpsFailRqstsPerSec_Type = Gauge32
_WpsFailRqstsPerSec_Object = MibScalar
wpsFailRqstsPerSec = _WpsFailRqstsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 22),
    _WpsFailRqstsPerSec_Type()
)
wpsFailRqstsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsFailRqstsPerSec.setStatus("current")
_WpsFailRqstsFromArrayMbr_Type = Gauge32
_WpsFailRqstsFromArrayMbr_Object = MibScalar
wpsFailRqstsFromArrayMbr = _WpsFailRqstsFromArrayMbr_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 23),
    _WpsFailRqstsFromArrayMbr_Type()
)
wpsFailRqstsFromArrayMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsFailRqstsFromArrayMbr.setStatus("current")
_WpsFailRqstsFromArrayMbrPerErrs_Type = Gauge32
_WpsFailRqstsFromArrayMbrPerErrs_Object = MibScalar
wpsFailRqstsFromArrayMbrPerErrs = _WpsFailRqstsFromArrayMbrPerErrs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 24),
    _WpsFailRqstsFromArrayMbrPerErrs_Type()
)
wpsFailRqstsFromArrayMbrPerErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsFailRqstsFromArrayMbrPerErrs.setStatus("current")
_WpsFailRqstsToArrayMbr_Type = Gauge32
_WpsFailRqstsToArrayMbr_Object = MibScalar
wpsFailRqstsToArrayMbr = _WpsFailRqstsToArrayMbr_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 25),
    _WpsFailRqstsToArrayMbr_Type()
)
wpsFailRqstsToArrayMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsFailRqstsToArrayMbr.setStatus("current")
_WpsFailRqstsToArrayMbrPerErrs_Type = Gauge32
_WpsFailRqstsToArrayMbrPerErrs_Object = MibScalar
wpsFailRqstsToArrayMbrPerErrs = _WpsFailRqstsToArrayMbrPerErrs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 26),
    _WpsFailRqstsToArrayMbrPerErrs_Type()
)
wpsFailRqstsToArrayMbrPerErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsFailRqstsToArrayMbrPerErrs.setStatus("current")
_WpsFailRqstsKAToArrayMbr_Type = Gauge32
_WpsFailRqstsKAToArrayMbr_Object = MibScalar
wpsFailRqstsKAToArrayMbr = _WpsFailRqstsKAToArrayMbr_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 27),
    _WpsFailRqstsKAToArrayMbr_Type()
)
wpsFailRqstsKAToArrayMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsFailRqstsKAToArrayMbr.setStatus("current")
_WpsFailRqstsKAToArrayMbrPerErrs_Type = Gauge32
_WpsFailRqstsKAToArrayMbrPerErrs_Object = MibScalar
wpsFailRqstsKAToArrayMbrPerErrs = _WpsFailRqstsKAToArrayMbrPerErrs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 28),
    _WpsFailRqstsKAToArrayMbrPerErrs_Type()
)
wpsFailRqstsKAToArrayMbrPerErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsFailRqstsKAToArrayMbrPerErrs.setStatus("current")
_WpsFailRqstsKAToClient_Type = Gauge32
_WpsFailRqstsKAToClient_Object = MibScalar
wpsFailRqstsKAToClient = _WpsFailRqstsKAToClient_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 29),
    _WpsFailRqstsKAToClient_Type()
)
wpsFailRqstsKAToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsFailRqstsKAToClient.setStatus("current")
_WpsFailRqstsKAToClientPerErrs_Type = Gauge32
_WpsFailRqstsKAToClientPerErrs_Object = MibScalar
wpsFailRqstsKAToClientPerErrs = _WpsFailRqstsKAToClientPerErrs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 30),
    _WpsFailRqstsKAToClientPerErrs_Type()
)
wpsFailRqstsKAToClientPerErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsFailRqstsKAToClientPerErrs.setStatus("current")
_WpsFailRqstsKAToServer_Type = Gauge32
_WpsFailRqstsKAToServer_Object = MibScalar
wpsFailRqstsKAToServer = _WpsFailRqstsKAToServer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 31),
    _WpsFailRqstsKAToServer_Type()
)
wpsFailRqstsKAToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsFailRqstsKAToServer.setStatus("current")
_WpsFailRqstsKAToServerPerErrs_Type = Gauge32
_WpsFailRqstsKAToServerPerErrs_Object = MibScalar
wpsFailRqstsKAToServerPerErrs = _WpsFailRqstsKAToServerPerErrs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 32),
    _WpsFailRqstsKAToServerPerErrs_Type()
)
wpsFailRqstsKAToServerPerErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsFailRqstsKAToServerPerErrs.setStatus("current")
_WpsFtpRequests_Type = Gauge32
_WpsFtpRequests_Object = MibScalar
wpsFtpRequests = _WpsFtpRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 33),
    _WpsFtpRequests_Type()
)
wpsFtpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsFtpRequests.setStatus("current")
_WpsHTTPSSessions_Type = Gauge32
_WpsHTTPSSessions_Object = MibScalar
wpsHTTPSSessions = _WpsHTTPSSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 34),
    _WpsHTTPSSessions_Type()
)
wpsHTTPSSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsHTTPSSessions.setStatus("current")
_WpsHttpRequests_Type = Gauge32
_WpsHttpRequests_Object = MibScalar
wpsHttpRequests = _WpsHttpRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 35),
    _WpsHttpRequests_Type()
)
wpsHttpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsHttpRequests.setStatus("current")
_WpsIOErrorsToArrayMember_Type = Gauge32
_WpsIOErrorsToArrayMember_Object = MibScalar
wpsIOErrorsToArrayMember = _WpsIOErrorsToArrayMember_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 36),
    _WpsIOErrorsToArrayMember_Type()
)
wpsIOErrorsToArrayMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsIOErrorsToArrayMember.setStatus("current")
_WpsIOErrorsToArrayMemberPerErrs_Type = Gauge32
_WpsIOErrorsToArrayMemberPerErrs_Object = MibScalar
wpsIOErrorsToArrayMemberPerErrs = _WpsIOErrorsToArrayMemberPerErrs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 37),
    _WpsIOErrorsToArrayMemberPerErrs_Type()
)
wpsIOErrorsToArrayMemberPerErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsIOErrorsToArrayMemberPerErrs.setStatus("current")
_WpsIOErrorsToClient_Type = Gauge32
_WpsIOErrorsToClient_Object = MibScalar
wpsIOErrorsToClient = _WpsIOErrorsToClient_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 38),
    _WpsIOErrorsToClient_Type()
)
wpsIOErrorsToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsIOErrorsToClient.setStatus("current")
_WpsIOErrorsToClientPerErrs_Type = Gauge32
_WpsIOErrorsToClientPerErrs_Object = MibScalar
wpsIOErrorsToClientPerErrs = _WpsIOErrorsToClientPerErrs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 39),
    _WpsIOErrorsToClientPerErrs_Type()
)
wpsIOErrorsToClientPerErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsIOErrorsToClientPerErrs.setStatus("current")
_WpsIOErrorsToServer_Type = Gauge32
_WpsIOErrorsToServer_Object = MibScalar
wpsIOErrorsToServer = _WpsIOErrorsToServer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 40),
    _WpsIOErrorsToServer_Type()
)
wpsIOErrorsToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsIOErrorsToServer.setStatus("current")
_WpsIOErrorsToServerPerErrs_Type = Gauge32
_WpsIOErrorsToServerPerErrs_Object = MibScalar
wpsIOErrorsToServerPerErrs = _WpsIOErrorsToServerPerErrs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 41),
    _WpsIOErrorsToServerPerErrs_Type()
)
wpsIOErrorsToServerPerErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsIOErrorsToServerPerErrs.setStatus("current")
_WpsIncomingConnectionsPerSec_Type = Gauge32
_WpsIncomingConnectionsPerSec_Object = MibScalar
wpsIncomingConnectionsPerSec = _WpsIncomingConnectionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 42),
    _WpsIncomingConnectionsPerSec_Type()
)
wpsIncomingConnectionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsIncomingConnectionsPerSec.setStatus("current")
_WpsMaximumUsers_Type = Gauge32
_WpsMaximumUsers_Object = MibScalar
wpsMaximumUsers = _WpsMaximumUsers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 43),
    _WpsMaximumUsers_Type()
)
wpsMaximumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsMaximumUsers.setStatus("current")
_WpsOutgoingConnectionsPerSec_Type = Gauge32
_WpsOutgoingConnectionsPerSec_Object = MibScalar
wpsOutgoingConnectionsPerSec = _WpsOutgoingConnectionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 44),
    _WpsOutgoingConnectionsPerSec_Type()
)
wpsOutgoingConnectionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsOutgoingConnectionsPerSec.setStatus("current")
_WpsRequestsPerSec_Type = Gauge32
_WpsRequestsPerSec_Object = MibScalar
wpsRequestsPerSec = _WpsRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 45),
    _WpsRequestsPerSec_Type()
)
wpsRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsRequestsPerSec.setStatus("current")
_WpsReverseBytesReceivedPerSec_Type = Gauge32
_WpsReverseBytesReceivedPerSec_Object = MibScalar
wpsReverseBytesReceivedPerSec = _WpsReverseBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 46),
    _WpsReverseBytesReceivedPerSec_Type()
)
wpsReverseBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsReverseBytesReceivedPerSec.setStatus("current")
_WpsReverseBytesSentPerSec_Type = Gauge32
_WpsReverseBytesSentPerSec_Object = MibScalar
wpsReverseBytesSentPerSec = _WpsReverseBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 47),
    _WpsReverseBytesSentPerSec_Type()
)
wpsReverseBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsReverseBytesSentPerSec.setStatus("current")
_WpsReverseBytesTotalPerSec_Type = Gauge32
_WpsReverseBytesTotalPerSec_Object = MibScalar
wpsReverseBytesTotalPerSec = _WpsReverseBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 48),
    _WpsReverseBytesTotalPerSec_Type()
)
wpsReverseBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsReverseBytesTotalPerSec.setStatus("current")
_WpsSNEWSSessions_Type = Gauge32
_WpsSNEWSSessions_Object = MibScalar
wpsSNEWSSessions = _WpsSNEWSSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 49),
    _WpsSNEWSSessions_Type()
)
wpsSNEWSSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsSNEWSSessions.setStatus("current")
_WpsSSLClientBytesReceivedPerSec_Type = Gauge32
_WpsSSLClientBytesReceivedPerSec_Object = MibScalar
wpsSSLClientBytesReceivedPerSec = _WpsSSLClientBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 50),
    _WpsSSLClientBytesReceivedPerSec_Type()
)
wpsSSLClientBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsSSLClientBytesReceivedPerSec.setStatus("current")
_WpsSSLClientBytesSentPerSec_Type = Gauge32
_WpsSSLClientBytesSentPerSec_Object = MibScalar
wpsSSLClientBytesSentPerSec = _WpsSSLClientBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 51),
    _WpsSSLClientBytesSentPerSec_Type()
)
wpsSSLClientBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsSSLClientBytesSentPerSec.setStatus("current")
_WpsSSLClientBytesTotalPerSec_Type = Gauge32
_WpsSSLClientBytesTotalPerSec_Object = MibScalar
wpsSSLClientBytesTotalPerSec = _WpsSSLClientBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 52),
    _WpsSSLClientBytesTotalPerSec_Type()
)
wpsSSLClientBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsSSLClientBytesTotalPerSec.setStatus("current")
_WpsSitesDenied_Type = Gauge32
_WpsSitesDenied_Object = MibScalar
wpsSitesDenied = _WpsSitesDenied_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 53),
    _WpsSitesDenied_Type()
)
wpsSitesDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsSitesDenied.setStatus("current")
_WpsSitesGranted_Type = Gauge32
_WpsSitesGranted_Object = MibScalar
wpsSitesGranted = _WpsSitesGranted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 54),
    _WpsSitesGranted_Type()
)
wpsSitesGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsSitesGranted.setStatus("current")
_WpsThreadPoolFailures_Type = Gauge32
_WpsThreadPoolFailures_Object = MibScalar
wpsThreadPoolFailures = _WpsThreadPoolFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 55),
    _WpsThreadPoolFailures_Type()
)
wpsThreadPoolFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsThreadPoolFailures.setStatus("current")
_WpsThreadPoolSize_Type = Gauge32
_WpsThreadPoolSize_Object = MibScalar
wpsThreadPoolSize = _WpsThreadPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 56),
    _WpsThreadPoolSize_Type()
)
wpsThreadPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsThreadPoolSize.setStatus("current")
_WpsThreadPoolActiveSessions_Type = Gauge32
_WpsThreadPoolActiveSessions_Object = MibScalar
wpsThreadPoolActiveSessions = _WpsThreadPoolActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 57),
    _WpsThreadPoolActiveSessions_Type()
)
wpsThreadPoolActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsThreadPoolActiveSessions.setStatus("current")
_WpsTotalArrayFetches_Type = Gauge32
_WpsTotalArrayFetches_Object = MibScalar
wpsTotalArrayFetches = _WpsTotalArrayFetches_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 58),
    _WpsTotalArrayFetches_Type()
)
wpsTotalArrayFetches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsTotalArrayFetches.setStatus("current")
_WpsTotalCacheFetches_Type = Gauge32
_WpsTotalCacheFetches_Object = MibScalar
wpsTotalCacheFetches = _WpsTotalCacheFetches_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 59),
    _WpsTotalCacheFetches_Type()
)
wpsTotalCacheFetches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsTotalCacheFetches.setStatus("current")
_WpsTotalFailingRequests_Type = Gauge32
_WpsTotalFailingRequests_Object = MibScalar
wpsTotalFailingRequests = _WpsTotalFailingRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 60),
    _WpsTotalFailingRequests_Type()
)
wpsTotalFailingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsTotalFailingRequests.setStatus("current")
_WpsTotalPendingConnects_Type = Gauge32
_WpsTotalPendingConnects_Object = MibScalar
wpsTotalPendingConnects = _WpsTotalPendingConnects_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 61),
    _WpsTotalPendingConnects_Type()
)
wpsTotalPendingConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsTotalPendingConnects.setStatus("current")
_WpsTotalRequests_Type = Gauge32
_WpsTotalRequests_Object = MibScalar
wpsTotalRequests = _WpsTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 62),
    _WpsTotalRequests_Type()
)
wpsTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsTotalRequests.setStatus("current")
_WpsTotalReverseFetches_Type = Gauge32
_WpsTotalReverseFetches_Object = MibScalar
wpsTotalReverseFetches = _WpsTotalReverseFetches_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 63),
    _WpsTotalReverseFetches_Type()
)
wpsTotalReverseFetches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsTotalReverseFetches.setStatus("current")
_WpsTotalSSLSessions_Type = Gauge32
_WpsTotalSSLSessions_Object = MibScalar
wpsTotalSSLSessions = _WpsTotalSSLSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 64),
    _WpsTotalSSLSessions_Type()
)
wpsTotalSSLSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsTotalSSLSessions.setStatus("current")
_WpsTotalSuccessfulRequests_Type = Gauge32
_WpsTotalSuccessfulRequests_Object = MibScalar
wpsTotalSuccessfulRequests = _WpsTotalSuccessfulRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 65),
    _WpsTotalSuccessfulRequests_Type()
)
wpsTotalSuccessfulRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsTotalSuccessfulRequests.setStatus("current")
_WpsTotalUpstreamFetches_Type = Gauge32
_WpsTotalUpstreamFetches_Object = MibScalar
wpsTotalUpstreamFetches = _WpsTotalUpstreamFetches_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 66),
    _WpsTotalUpstreamFetches_Type()
)
wpsTotalUpstreamFetches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsTotalUpstreamFetches.setStatus("current")
_WpsTotalUsers_Type = Gauge32
_WpsTotalUsers_Object = MibScalar
wpsTotalUsers = _WpsTotalUsers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 67),
    _WpsTotalUsers_Type()
)
wpsTotalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsTotalUsers.setStatus("current")
_WpsUnknownSSLSessions_Type = Gauge32
_WpsUnknownSSLSessions_Object = MibScalar
wpsUnknownSSLSessions = _WpsUnknownSSLSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 68),
    _WpsUnknownSSLSessions_Type()
)
wpsUnknownSSLSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsUnknownSSLSessions.setStatus("current")
_WpsUpstreamBytesReceivedPerSec_Type = Gauge32
_WpsUpstreamBytesReceivedPerSec_Object = MibScalar
wpsUpstreamBytesReceivedPerSec = _WpsUpstreamBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 69),
    _WpsUpstreamBytesReceivedPerSec_Type()
)
wpsUpstreamBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsUpstreamBytesReceivedPerSec.setStatus("current")
_WpsUpstreamBytesSentPerSec_Type = Gauge32
_WpsUpstreamBytesSentPerSec_Object = MibScalar
wpsUpstreamBytesSentPerSec = _WpsUpstreamBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 70),
    _WpsUpstreamBytesSentPerSec_Type()
)
wpsUpstreamBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsUpstreamBytesSentPerSec.setStatus("current")
_WpsUpstreamBytesTotalPerSec_Type = Gauge32
_WpsUpstreamBytesTotalPerSec_Object = MibScalar
wpsUpstreamBytesTotalPerSec = _WpsUpstreamBytesTotalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 71),
    _WpsUpstreamBytesTotalPerSec_Type()
)
wpsUpstreamBytesTotalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsUpstreamBytesTotalPerSec.setStatus("current")
_WpsActiveWebSessions_Type = Gauge32
_WpsActiveWebSessions_Object = MibScalar
wpsActiveWebSessions = _WpsActiveWebSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 72),
    _WpsActiveWebSessions_Type()
)
wpsActiveWebSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsActiveWebSessions.setStatus("current")
_WpsAverageMillisecondsPerRequest_Type = Gauge32
_WpsAverageMillisecondsPerRequest_Object = MibScalar
wpsAverageMillisecondsPerRequest = _WpsAverageMillisecondsPerRequest_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 73),
    _WpsAverageMillisecondsPerRequest_Type()
)
wpsAverageMillisecondsPerRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsAverageMillisecondsPerRequest.setStatus("current")
_WpsBytesRtnPtlCntRsps_Type = Gauge32
_WpsBytesRtnPtlCntRsps_Object = MibScalar
wpsBytesRtnPtlCntRsps = _WpsBytesRtnPtlCntRsps_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 74),
    _WpsBytesRtnPtlCntRsps_Type()
)
wpsBytesRtnPtlCntRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsBytesRtnPtlCntRsps.setStatus("current")
_WpsBytesRtnPtlCntRspsRqstdServer_Type = Gauge32
_WpsBytesRtnPtlCntRspsRqstdServer_Object = MibScalar
wpsBytesRtnPtlCntRspsRqstdServer = _WpsBytesRtnPtlCntRspsRqstdServer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 75),
    _WpsBytesRtnPtlCntRspsRqstdServer_Type()
)
wpsBytesRtnPtlCntRspsRqstdServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsBytesRtnPtlCntRspsRqstdServer.setStatus("current")
_WpsBytesRtnPtlCntRspsSvdCh_Type = Gauge32
_WpsBytesRtnPtlCntRspsSvdCh_Object = MibScalar
wpsBytesRtnPtlCntRspsSvdCh = _WpsBytesRtnPtlCntRspsSvdCh_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 76),
    _WpsBytesRtnPtlCntRspsSvdCh_Type()
)
wpsBytesRtnPtlCntRspsSvdCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsBytesRtnPtlCntRspsSvdCh.setStatus("current")
_WpsBytesRtnPtlCntRspsSvdChHr_Type = Gauge32
_WpsBytesRtnPtlCntRspsSvdChHr_Object = MibScalar
wpsBytesRtnPtlCntRspsSvdChHr = _WpsBytesRtnPtlCntRspsSvdChHr_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 77),
    _WpsBytesRtnPtlCntRspsSvdChHr_Type()
)
wpsBytesRtnPtlCntRspsSvdChHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsBytesRtnPtlCntRspsSvdChHr.setStatus("current")
_WpsBytesRtnPtlCntRspsBITSEnChRule_Type = Gauge32
_WpsBytesRtnPtlCntRspsBITSEnChRule_Object = MibScalar
wpsBytesRtnPtlCntRspsBITSEnChRule = _WpsBytesRtnPtlCntRspsBITSEnChRule_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 78),
    _WpsBytesRtnPtlCntRspsBITSEnChRule_Type()
)
wpsBytesRtnPtlCntRspsBITSEnChRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsBytesRtnPtlCntRspsBITSEnChRule.setStatus("current")
_WpsBytesRtnPtlCntRspsBITSEnChRuleHr_Type = Gauge32
_WpsBytesRtnPtlCntRspsBITSEnChRuleHr_Object = MibScalar
wpsBytesRtnPtlCntRspsBITSEnChRuleHr = _WpsBytesRtnPtlCntRspsBITSEnChRuleHr_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 79),
    _WpsBytesRtnPtlCntRspsBITSEnChRuleHr_Type()
)
wpsBytesRtnPtlCntRspsBITSEnChRuleHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsBytesRtnPtlCntRspsBITSEnChRuleHr.setStatus("current")
_WpsBytesRtnPtlCntRspsInLastHour_Type = Gauge32
_WpsBytesRtnPtlCntRspsInLastHour_Object = MibScalar
wpsBytesRtnPtlCntRspsInLastHour = _WpsBytesRtnPtlCntRspsInLastHour_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 80),
    _WpsBytesRtnPtlCntRspsInLastHour_Type()
)
wpsBytesRtnPtlCntRspsInLastHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsBytesRtnPtlCntRspsInLastHour.setStatus("current")
_WpsBytesARqstSvrRngRqstRngRqst_Type = Gauge32
_WpsBytesARqstSvrRngRqstRngRqst_Object = MibScalar
wpsBytesARqstSvrRngRqstRngRqst = _WpsBytesARqstSvrRngRqstRngRqst_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 81),
    _WpsBytesARqstSvrRngRqstRngRqst_Type()
)
wpsBytesARqstSvrRngRqstRngRqst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsBytesARqstSvrRngRqstRngRqst.setStatus("current")
_WpsCacheHitPctForRangeRequests_Type = Gauge32
_WpsCacheHitPctForRangeRequests_Object = MibScalar
wpsCacheHitPctForRangeRequests = _WpsCacheHitPctForRangeRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 82),
    _WpsCacheHitPctForRangeRequests_Type()
)
wpsCacheHitPctForRangeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsCacheHitPctForRangeRequests.setStatus("current")
_WpscAccumulatedCompressionRatio_Type = Gauge32
_WpscAccumulatedCompressionRatio_Object = MibScalar
wpscAccumulatedCompressionRatio = _WpscAccumulatedCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 83),
    _WpscAccumulatedCompressionRatio_Type()
)
wpscAccumulatedCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpscAccumulatedCompressionRatio.setStatus("current")
_WpscAccumulatedPctRspsCompressed_Type = Gauge32
_WpscAccumulatedPctRspsCompressed_Object = MibScalar
wpscAccumulatedPctRspsCompressed = _WpscAccumulatedPctRspsCompressed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 84),
    _WpscAccumulatedPctRspsCompressed_Type()
)
wpscAccumulatedPctRspsCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpscAccumulatedPctRspsCompressed.setStatus("current")
_WpscAccumulatedPctRspsDecompress_Type = Gauge32
_WpscAccumulatedPctRspsDecompress_Object = MibScalar
wpscAccumulatedPctRspsDecompress = _WpscAccumulatedPctRspsDecompress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 85),
    _WpscAccumulatedPctRspsDecompress_Type()
)
wpscAccumulatedPctRspsDecompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpscAccumulatedPctRspsDecompress.setStatus("current")
_WpscSampledCompressionRatio_Type = Gauge32
_WpscSampledCompressionRatio_Object = MibScalar
wpscSampledCompressionRatio = _WpscSampledCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 86),
    _WpscSampledCompressionRatio_Type()
)
wpscSampledCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpscSampledCompressionRatio.setStatus("current")
_WpscSampledPctRspsCompressed_Type = Gauge32
_WpscSampledPctRspsCompressed_Object = MibScalar
wpscSampledPctRspsCompressed = _WpscSampledPctRspsCompressed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 87),
    _WpscSampledPctRspsCompressed_Type()
)
wpscSampledPctRspsCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpscSampledPctRspsCompressed.setStatus("current")
_WpscSampledPctRspsDecompressed_Type = Gauge32
_WpscSampledPctRspsDecompressed_Object = MibScalar
wpscSampledPctRspsDecompressed = _WpscSampledPctRspsDecompressed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 88),
    _WpscSampledPctRspsDecompressed_Type()
)
wpscSampledPctRspsDecompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpscSampledPctRspsDecompressed.setStatus("current")
_WpscTotalFailures_Type = Gauge32
_WpscTotalFailures_Object = MibScalar
wpscTotalFailures = _WpscTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 89),
    _WpscTotalFailures_Type()
)
wpscTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpscTotalFailures.setStatus("current")
_WpsDNSCacheLockFailures_Type = Gauge32
_WpsDNSCacheLockFailures_Object = MibScalar
wpsDNSCacheLockFailures = _WpsDNSCacheLockFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 90),
    _WpsDNSCacheLockFailures_Type()
)
wpsDNSCacheLockFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsDNSCacheLockFailures.setStatus("current")
_Wpsdrq1stPriorityRatioToTotal_Type = Gauge32
_Wpsdrq1stPriorityRatioToTotal_Object = MibScalar
wpsdrq1stPriorityRatioToTotal = _Wpsdrq1stPriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 91),
    _Wpsdrq1stPriorityRatioToTotal_Type()
)
wpsdrq1stPriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrq1stPriorityRatioToTotal.setStatus("current")
_Wpsdrq1stPriority_Type = Gauge32
_Wpsdrq1stPriority_Object = MibScalar
wpsdrq1stPriority = _Wpsdrq1stPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 92),
    _Wpsdrq1stPriority_Type()
)
wpsdrq1stPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrq1stPriority.setStatus("current")
_Wpsdrq2ndPriorityRatioToTotal_Type = Gauge32
_Wpsdrq2ndPriorityRatioToTotal_Object = MibScalar
wpsdrq2ndPriorityRatioToTotal = _Wpsdrq2ndPriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 93),
    _Wpsdrq2ndPriorityRatioToTotal_Type()
)
wpsdrq2ndPriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrq2ndPriorityRatioToTotal.setStatus("current")
_Wpsdrq2ndPriority_Type = Gauge32
_Wpsdrq2ndPriority_Object = MibScalar
wpsdrq2ndPriority = _Wpsdrq2ndPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 94),
    _Wpsdrq2ndPriority_Type()
)
wpsdrq2ndPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrq2ndPriority.setStatus("current")
_Wpsdrq3rdPriorityRatioToTotal_Type = Gauge32
_Wpsdrq3rdPriorityRatioToTotal_Object = MibScalar
wpsdrq3rdPriorityRatioToTotal = _Wpsdrq3rdPriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 95),
    _Wpsdrq3rdPriorityRatioToTotal_Type()
)
wpsdrq3rdPriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrq3rdPriorityRatioToTotal.setStatus("current")
_Wpsdrq3rdPriority_Type = Gauge32
_Wpsdrq3rdPriority_Object = MibScalar
wpsdrq3rdPriority = _Wpsdrq3rdPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 96),
    _Wpsdrq3rdPriority_Type()
)
wpsdrq3rdPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrq3rdPriority.setStatus("current")
_Wpsdrq4thPriorityRatioToTotal_Type = Gauge32
_Wpsdrq4thPriorityRatioToTotal_Object = MibScalar
wpsdrq4thPriorityRatioToTotal = _Wpsdrq4thPriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 97),
    _Wpsdrq4thPriorityRatioToTotal_Type()
)
wpsdrq4thPriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrq4thPriorityRatioToTotal.setStatus("current")
_Wpsdrq4thPriority_Type = Gauge32
_Wpsdrq4thPriority_Object = MibScalar
wpsdrq4thPriority = _Wpsdrq4thPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 98),
    _Wpsdrq4thPriority_Type()
)
wpsdrq4thPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrq4thPriority.setStatus("current")
_Wpsdrq5thPriorityRatioToTotal_Type = Gauge32
_Wpsdrq5thPriorityRatioToTotal_Object = MibScalar
wpsdrq5thPriorityRatioToTotal = _Wpsdrq5thPriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 99),
    _Wpsdrq5thPriorityRatioToTotal_Type()
)
wpsdrq5thPriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrq5thPriorityRatioToTotal.setStatus("current")
_Wpsdrq5thPriority_Type = Gauge32
_Wpsdrq5thPriority_Object = MibScalar
wpsdrq5thPriority = _Wpsdrq5thPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 100),
    _Wpsdrq5thPriority_Type()
)
wpsdrq5thPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrq5thPriority.setStatus("current")
_WpsdrqLowPriorityRatioToTotal_Type = Gauge32
_WpsdrqLowPriorityRatioToTotal_Object = MibScalar
wpsdrqLowPriorityRatioToTotal = _WpsdrqLowPriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 101),
    _WpsdrqLowPriorityRatioToTotal_Type()
)
wpsdrqLowPriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrqLowPriorityRatioToTotal.setStatus("current")
_WpsdrqLowerPriority_Type = Gauge32
_WpsdrqLowerPriority_Object = MibScalar
wpsdrqLowerPriority = _WpsdrqLowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 102),
    _WpsdrqLowerPriority_Type()
)
wpsdrqLowerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrqLowerPriority.setStatus("current")
_WpsdrqNon_PriorityRatioToTotal_Type = Gauge32
_WpsdrqNon_PriorityRatioToTotal_Object = MibScalar
wpsdrqNon_PriorityRatioToTotal = _WpsdrqNon_PriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 103),
    _WpsdrqNon_PriorityRatioToTotal_Type()
)
wpsdrqNon_PriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrqNon_PriorityRatioToTotal.setStatus("current")
_WpsdrqNon_priority_Type = Gauge32
_WpsdrqNon_priority_Object = MibScalar
wpsdrqNon_priority = _WpsdrqNon_priority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 104),
    _WpsdrqNon_priority_Type()
)
wpsdrqNon_priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrqNon_priority.setStatus("current")
_WpsdrqPriorityRatioToTotal_Type = Gauge32
_WpsdrqPriorityRatioToTotal_Object = MibScalar
wpsdrqPriorityRatioToTotal = _WpsdrqPriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 105),
    _WpsdrqPriorityRatioToTotal_Type()
)
wpsdrqPriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrqPriorityRatioToTotal.setStatus("current")
_WpsdrqTotalPriority_Type = Gauge32
_WpsdrqTotalPriority_Object = MibScalar
wpsdrqTotalPriority = _WpsdrqTotalPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 106),
    _WpsdrqTotalPriority_Type()
)
wpsdrqTotalPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrqTotalPriority.setStatus("current")
_Wpsdrs1stPriorityRatioToTotal_Type = Gauge32
_Wpsdrs1stPriorityRatioToTotal_Object = MibScalar
wpsdrs1stPriorityRatioToTotal = _Wpsdrs1stPriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 107),
    _Wpsdrs1stPriorityRatioToTotal_Type()
)
wpsdrs1stPriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrs1stPriorityRatioToTotal.setStatus("current")
_Wpsdrs1stPriority_Type = Gauge32
_Wpsdrs1stPriority_Object = MibScalar
wpsdrs1stPriority = _Wpsdrs1stPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 108),
    _Wpsdrs1stPriority_Type()
)
wpsdrs1stPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrs1stPriority.setStatus("current")
_Wpsdrs2ndPriorityRatioToTotal_Type = Gauge32
_Wpsdrs2ndPriorityRatioToTotal_Object = MibScalar
wpsdrs2ndPriorityRatioToTotal = _Wpsdrs2ndPriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 109),
    _Wpsdrs2ndPriorityRatioToTotal_Type()
)
wpsdrs2ndPriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrs2ndPriorityRatioToTotal.setStatus("current")
_Wpsdrs2ndPriority_Type = Gauge32
_Wpsdrs2ndPriority_Object = MibScalar
wpsdrs2ndPriority = _Wpsdrs2ndPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 110),
    _Wpsdrs2ndPriority_Type()
)
wpsdrs2ndPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrs2ndPriority.setStatus("current")
_Wpsdrs3rdPriorityRatioToTotal_Type = Gauge32
_Wpsdrs3rdPriorityRatioToTotal_Object = MibScalar
wpsdrs3rdPriorityRatioToTotal = _Wpsdrs3rdPriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 111),
    _Wpsdrs3rdPriorityRatioToTotal_Type()
)
wpsdrs3rdPriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrs3rdPriorityRatioToTotal.setStatus("current")
_Wpsdrs3rdPriority_Type = Gauge32
_Wpsdrs3rdPriority_Object = MibScalar
wpsdrs3rdPriority = _Wpsdrs3rdPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 112),
    _Wpsdrs3rdPriority_Type()
)
wpsdrs3rdPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrs3rdPriority.setStatus("current")
_Wpsdrs4thPriorityRatioToTotal_Type = Gauge32
_Wpsdrs4thPriorityRatioToTotal_Object = MibScalar
wpsdrs4thPriorityRatioToTotal = _Wpsdrs4thPriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 113),
    _Wpsdrs4thPriorityRatioToTotal_Type()
)
wpsdrs4thPriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrs4thPriorityRatioToTotal.setStatus("current")
_Wpsdrs4thPriority_Type = Gauge32
_Wpsdrs4thPriority_Object = MibScalar
wpsdrs4thPriority = _Wpsdrs4thPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 114),
    _Wpsdrs4thPriority_Type()
)
wpsdrs4thPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrs4thPriority.setStatus("current")
_Wpsdrs5thPriorityRatioToTotal_Type = Gauge32
_Wpsdrs5thPriorityRatioToTotal_Object = MibScalar
wpsdrs5thPriorityRatioToTotal = _Wpsdrs5thPriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 115),
    _Wpsdrs5thPriorityRatioToTotal_Type()
)
wpsdrs5thPriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrs5thPriorityRatioToTotal.setStatus("current")
_Wpsdrs5thPriority_Type = Gauge32
_Wpsdrs5thPriority_Object = MibScalar
wpsdrs5thPriority = _Wpsdrs5thPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 116),
    _Wpsdrs5thPriority_Type()
)
wpsdrs5thPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrs5thPriority.setStatus("current")
_WpsdrsLowPriorityRatioToTotal_Type = Gauge32
_WpsdrsLowPriorityRatioToTotal_Object = MibScalar
wpsdrsLowPriorityRatioToTotal = _WpsdrsLowPriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 117),
    _WpsdrsLowPriorityRatioToTotal_Type()
)
wpsdrsLowPriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrsLowPriorityRatioToTotal.setStatus("current")
_WpsdrsLowerPriority_Type = Gauge32
_WpsdrsLowerPriority_Object = MibScalar
wpsdrsLowerPriority = _WpsdrsLowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 118),
    _WpsdrsLowerPriority_Type()
)
wpsdrsLowerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrsLowerPriority.setStatus("current")
_WpsdrsNon_PriorityRatioToTotal_Type = Gauge32
_WpsdrsNon_PriorityRatioToTotal_Object = MibScalar
wpsdrsNon_PriorityRatioToTotal = _WpsdrsNon_PriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 119),
    _WpsdrsNon_PriorityRatioToTotal_Type()
)
wpsdrsNon_PriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrsNon_PriorityRatioToTotal.setStatus("current")
_WpsdrsNon_priority_Type = Gauge32
_WpsdrsNon_priority_Object = MibScalar
wpsdrsNon_priority = _WpsdrsNon_priority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 120),
    _WpsdrsNon_priority_Type()
)
wpsdrsNon_priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrsNon_priority.setStatus("current")
_WpsdrsPriorityRatioToTotal_Type = Gauge32
_WpsdrsPriorityRatioToTotal_Object = MibScalar
wpsdrsPriorityRatioToTotal = _WpsdrsPriorityRatioToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 121),
    _WpsdrsPriorityRatioToTotal_Type()
)
wpsdrsPriorityRatioToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrsPriorityRatioToTotal.setStatus("current")
_WpsdrsTotalPriority_Type = Gauge32
_WpsdrsTotalPriority_Object = MibScalar
wpsdrsTotalPriority = _WpsdrsTotalPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 122),
    _WpsdrsTotalPriority_Type()
)
wpsdrsTotalPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsdrsTotalPriority.setStatus("current")
_WpsRqstFromAryMember_Type = Gauge32
_WpsRqstFromAryMember_Object = MibScalar
wpsRqstFromAryMember = _WpsRqstFromAryMember_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 123),
    _WpsRqstFromAryMember_Type()
)
wpsRqstFromAryMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsRqstFromAryMember.setStatus("current")
_WpsRqstFromAryMemberPerErrs_Type = Gauge32
_WpsRqstFromAryMemberPerErrs_Object = MibScalar
wpsRqstFromAryMemberPerErrs = _WpsRqstFromAryMemberPerErrs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 124),
    _WpsRqstFromAryMemberPerErrs_Type()
)
wpsRqstFromAryMemberPerErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsRqstFromAryMemberPerErrs.setStatus("current")
_WpsRqstToAryMember_Type = Gauge32
_WpsRqstToAryMember_Object = MibScalar
wpsRqstToAryMember = _WpsRqstToAryMember_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 125),
    _WpsRqstToAryMember_Type()
)
wpsRqstToAryMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsRqstToAryMember.setStatus("current")
_WpsRqstToAryMemberPerErrs_Type = Gauge32
_WpsRqstToAryMemberPerErrs_Object = MibScalar
wpsRqstToAryMemberPerErrs = _WpsRqstToAryMemberPerErrs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 126),
    _WpsRqstToAryMemberPerErrs_Type()
)
wpsRqstToAryMemberPerErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsRqstToAryMemberPerErrs.setStatus("current")
_WpsRqstKeepAliveToAryMember_Type = Gauge32
_WpsRqstKeepAliveToAryMember_Object = MibScalar
wpsRqstKeepAliveToAryMember = _WpsRqstKeepAliveToAryMember_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 127),
    _WpsRqstKeepAliveToAryMember_Type()
)
wpsRqstKeepAliveToAryMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsRqstKeepAliveToAryMember.setStatus("current")
_WpsRqstKeepAliveToAryMbrPerErrs_Type = Gauge32
_WpsRqstKeepAliveToAryMbrPerErrs_Object = MibScalar
wpsRqstKeepAliveToAryMbrPerErrs = _WpsRqstKeepAliveToAryMbrPerErrs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 128),
    _WpsRqstKeepAliveToAryMbrPerErrs_Type()
)
wpsRqstKeepAliveToAryMbrPerErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsRqstKeepAliveToAryMbrPerErrs.setStatus("current")
_WpsRqstKeepAliveToClient_Type = Gauge32
_WpsRqstKeepAliveToClient_Object = MibScalar
wpsRqstKeepAliveToClient = _WpsRqstKeepAliveToClient_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 129),
    _WpsRqstKeepAliveToClient_Type()
)
wpsRqstKeepAliveToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsRqstKeepAliveToClient.setStatus("current")
_WpsRqstKeepAliveToClientPerErrs_Type = Gauge32
_WpsRqstKeepAliveToClientPerErrs_Object = MibScalar
wpsRqstKeepAliveToClientPerErrs = _WpsRqstKeepAliveToClientPerErrs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 130),
    _WpsRqstKeepAliveToClientPerErrs_Type()
)
wpsRqstKeepAliveToClientPerErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsRqstKeepAliveToClientPerErrs.setStatus("current")
_WpsRqstKeepAliveToServer_Type = Gauge32
_WpsRqstKeepAliveToServer_Object = MibScalar
wpsRqstKeepAliveToServer = _WpsRqstKeepAliveToServer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 131),
    _WpsRqstKeepAliveToServer_Type()
)
wpsRqstKeepAliveToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsRqstKeepAliveToServer.setStatus("current")
_WpsRqstKeepAliveToServerPerErrs_Type = Gauge32
_WpsRqstKeepAliveToServerPerErrs_Object = MibScalar
wpsRqstKeepAliveToServerPerErrs = _WpsRqstKeepAliveToServerPerErrs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 132),
    _WpsRqstKeepAliveToServerPerErrs_Type()
)
wpsRqstKeepAliveToServerPerErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsRqstKeepAliveToServerPerErrs.setStatus("current")
_WpsRqstWithMultipleRanges_Type = Gauge32
_WpsRqstWithMultipleRanges_Object = MibScalar
wpsRqstWithMultipleRanges = _WpsRqstWithMultipleRanges_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 133),
    _WpsRqstWithMultipleRanges_Type()
)
wpsRqstWithMultipleRanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsRqstWithMultipleRanges.setStatus("current")
_WpsAverageRequestSpeed_Type = Gauge32
_WpsAverageRequestSpeed_Object = MibScalar
wpsAverageRequestSpeed = _WpsAverageRequestSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 134),
    _WpsAverageRequestSpeed_Type()
)
wpsAverageRequestSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsAverageRequestSpeed.setStatus("current")
_WpsBytesRequestedFromServerInRanges_Type = Gauge32
_WpsBytesRequestedFromServerInRanges_Object = MibScalar
wpsBytesRequestedFromServerInRanges = _WpsBytesRequestedFromServerInRanges_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 135),
    _WpsBytesRequestedFromServerInRanges_Type()
)
wpsBytesRequestedFromServerInRanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsBytesRequestedFromServerInRanges.setStatus("current")
_WpsBytesServedLastHourFromCacheInRanges_Type = Gauge32
_WpsBytesServedLastHourFromCacheInRanges_Object = MibScalar
wpsBytesServedLastHourFromCacheInRanges = _WpsBytesServedLastHourFromCacheInRanges_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 136),
    _WpsBytesServedLastHourFromCacheInRanges_Type()
)
wpsBytesServedLastHourFromCacheInRanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsBytesServedLastHourFromCacheInRanges.setStatus("current")
_WpsBytesServedLastHourInRanges_Type = Gauge32
_WpsBytesServedLastHourInRanges_Object = MibScalar
wpsBytesServedLastHourInRanges = _WpsBytesServedLastHourInRanges_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 137),
    _WpsBytesServedLastHourInRanges_Type()
)
wpsBytesServedLastHourInRanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsBytesServedLastHourInRanges.setStatus("current")
_WpsBytesServedFromCacheInRanges_Type = Gauge32
_WpsBytesServedFromCacheInRanges_Object = MibScalar
wpsBytesServedFromCacheInRanges = _WpsBytesServedFromCacheInRanges_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 138),
    _WpsBytesServedFromCacheInRanges_Type()
)
wpsBytesServedFromCacheInRanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsBytesServedFromCacheInRanges.setStatus("current")
_WpsBytesServedInRanges_Type = Gauge32
_WpsBytesServedInRanges_Object = MibScalar
wpsBytesServedInRanges = _WpsBytesServedInRanges_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 139),
    _WpsBytesServedInRanges_Type()
)
wpsBytesServedInRanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsBytesServedInRanges.setStatus("current")
_WpsCompCurrentCompressionRatio_Type = Gauge32
_WpsCompCurrentCompressionRatio_Object = MibScalar
wpsCompCurrentCompressionRatio = _WpsCompCurrentCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 140),
    _WpsCompCurrentCompressionRatio_Type()
)
wpsCompCurrentCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsCompCurrentCompressionRatio.setStatus("current")
_WpsCompCurRatioOfRspsCompressed_Type = Gauge32
_WpsCompCurRatioOfRspsCompressed_Object = MibScalar
wpsCompCurRatioOfRspsCompressed = _WpsCompCurRatioOfRspsCompressed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 141),
    _WpsCompCurRatioOfRspsCompressed_Type()
)
wpsCompCurRatioOfRspsCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsCompCurRatioOfRspsCompressed.setStatus("current")
_WpsCompCurRatioOfRspsDecompress_Type = Gauge32
_WpsCompCurRatioOfRspsDecompress_Object = MibScalar
wpsCompCurRatioOfRspsDecompress = _WpsCompCurRatioOfRspsDecompress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 142),
    _WpsCompCurRatioOfRspsDecompress_Type()
)
wpsCompCurRatioOfRspsDecompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsCompCurRatioOfRspsDecompress.setStatus("current")
_WpsCompRatioOfSizeReduction_Type = Gauge32
_WpsCompRatioOfSizeReduction_Object = MibScalar
wpsCompRatioOfSizeReduction = _WpsCompRatioOfSizeReduction_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 143),
    _WpsCompRatioOfSizeReduction_Type()
)
wpsCompRatioOfSizeReduction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsCompRatioOfSizeReduction.setStatus("current")
_WpsCompRspsCompAccumulatedRatio_Type = Gauge32
_WpsCompRspsCompAccumulatedRatio_Object = MibScalar
wpsCompRspsCompAccumulatedRatio = _WpsCompRspsCompAccumulatedRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 144),
    _WpsCompRspsCompAccumulatedRatio_Type()
)
wpsCompRspsCompAccumulatedRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsCompRspsCompAccumulatedRatio.setStatus("current")
_WpsCompRspsDcompAccumulatedRatio_Type = Gauge32
_WpsCompRspsDcompAccumulatedRatio_Object = MibScalar
wpsCompRspsDcompAccumulatedRatio = _WpsCompRspsDcompAccumulatedRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 145),
    _WpsCompRspsDcompAccumulatedRatio_Type()
)
wpsCompRspsDcompAccumulatedRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsCompRspsDcompAccumulatedRatio.setStatus("current")
_WpsMemoryPoolForHTTPRqstPercent_Type = Gauge32
_WpsMemoryPoolForHTTPRqstPercent_Object = MibScalar
wpsMemoryPoolForHTTPRqstPercent = _WpsMemoryPoolForHTTPRqstPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 146),
    _WpsMemoryPoolForHTTPRqstPercent_Type()
)
wpsMemoryPoolForHTTPRqstPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsMemoryPoolForHTTPRqstPercent.setStatus("current")
_WpsMemoryPoolForSSLRqstPercent_Type = Gauge32
_WpsMemoryPoolForSSLRqstPercent_Object = MibScalar
wpsMemoryPoolForSSLRqstPercent = _WpsMemoryPoolForSSLRqstPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 7, 147),
    _WpsMemoryPoolForSSLRqstPercent_Type()
)
wpsMemoryPoolForSSLRqstPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wpsMemoryPoolForSSLRqstPercent.setStatus("current")
_SocksFilter_ObjectIdentity = ObjectIdentity
socksFilter = _SocksFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 8)
)
if mibBuilder.loadTexts:
    socksFilter.setStatus("current")
_SocksFilterActiveConnections_Type = Gauge32
_SocksFilterActiveConnections_Object = MibScalar
socksFilterActiveConnections = _SocksFilterActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 8, 1),
    _SocksFilterActiveConnections_Type()
)
socksFilterActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksFilterActiveConnections.setStatus("current")
_SocksFilterActiveSessions_Type = Gauge32
_SocksFilterActiveSessions_Object = MibScalar
socksFilterActiveSessions = _SocksFilterActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 8, 2),
    _SocksFilterActiveSessions_Type()
)
socksFilterActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksFilterActiveSessions.setStatus("current")
_SocksFilterBytesReadPerSec_Type = Gauge32
_SocksFilterBytesReadPerSec_Object = MibScalar
socksFilterBytesReadPerSec = _SocksFilterBytesReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 8, 3),
    _SocksFilterBytesReadPerSec_Type()
)
socksFilterBytesReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksFilterBytesReadPerSec.setStatus("current")
_SocksFilterBytesWrittenPerSec_Type = Gauge32
_SocksFilterBytesWrittenPerSec_Object = MibScalar
socksFilterBytesWrittenPerSec = _SocksFilterBytesWrittenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 8, 4),
    _SocksFilterBytesWrittenPerSec_Type()
)
socksFilterBytesWrittenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksFilterBytesWrittenPerSec.setStatus("current")
_SocksFilterConnectingConnections_Type = Gauge32
_SocksFilterConnectingConnections_Object = MibScalar
socksFilterConnectingConnections = _SocksFilterConnectingConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 8, 5),
    _SocksFilterConnectingConnections_Type()
)
socksFilterConnectingConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksFilterConnectingConnections.setStatus("current")
_SocksFilterListeningConnections_Type = Gauge32
_SocksFilterListeningConnections_Object = MibScalar
socksFilterListeningConnections = _SocksFilterListeningConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 8, 6),
    _SocksFilterListeningConnections_Type()
)
socksFilterListeningConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksFilterListeningConnections.setStatus("current")
_SocksFilterPendingDNSResolutions_Type = Gauge32
_SocksFilterPendingDNSResolutions_Object = MibScalar
socksFilterPendingDNSResolutions = _SocksFilterPendingDNSResolutions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 8, 7),
    _SocksFilterPendingDNSResolutions_Type()
)
socksFilterPendingDNSResolutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksFilterPendingDNSResolutions.setStatus("current")
_SocksFilterSuccessDNSResolutions_Type = Gauge32
_SocksFilterSuccessDNSResolutions_Object = MibScalar
socksFilterSuccessDNSResolutions = _SocksFilterSuccessDNSResolutions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 6, 8, 8),
    _SocksFilterSuccessDNSResolutions_Type()
)
socksFilterSuccessDNSResolutions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socksFilterSuccessDNSResolutions.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFORMANT-ISASERVER",
    **{"isaServer": isaServer,
       "h323Filter": h323Filter,
       "h323FilterActiveH323Calls": h323FilterActiveH323Calls,
       "h323FilterTotalH323Calls": h323FilterTotalH323Calls,
       "bandwidthControlTable": bandwidthControlTable,
       "bandwidthControlEntry": bandwidthControlEntry,
       "bwCtrlInstance": bwCtrlInstance,
       "bwCtrlActualInboundBandwidth": bwCtrlActualInboundBandwidth,
       "bwCtrlActualOutboundBandwidth": bwCtrlActualOutboundBandwidth,
       "bwCtrlAssignedConnections": bwCtrlAssignedConnections,
       "bwCtrlAssignedInboundBandwidth": bwCtrlAssignedInboundBandwidth,
       "bwCtrlAssignedOutboundBandwidth": bwCtrlAssignedOutboundBandwidth,
       "cache": cache,
       "cacheActiveRefreshKBPerSec": cacheActiveRefreshKBPerSec,
       "cacheActiveRefreshURLPerSec": cacheActiveRefreshURLPerSec,
       "cacheDiskRetrievedKBPerSec": cacheDiskRetrievedKBPerSec,
       "cacheDiskCacheAllocatedSpaceKB": cacheDiskCacheAllocatedSpaceKB,
       "cacheDiskContentWritesPerSec": cacheDiskContentWritesPerSec,
       "cacheDiskFailPerSec": cacheDiskFailPerSec,
       "cacheDiskRetrieveURLPerSec": cacheDiskRetrieveURLPerSec,
       "cacheMaxURLsCached": cacheMaxURLsCached,
       "cacheMemoryRetrievedKBPerSec": cacheMemoryRetrievedKBPerSec,
       "cacheMemoryCacheAllocatedSpaceKB": cacheMemoryCacheAllocatedSpaceKB,
       "cacheMemoryRetrieveURLPerSec": cacheMemoryRetrieveURLPerSec,
       "cacheMemoryUsageRatioPercent": cacheMemoryUsageRatioPercent,
       "cacheTotalActivelyRefreshedURLs": cacheTotalActivelyRefreshedURLs,
       "cacheTotalBytesActiveRefreshedKB": cacheTotalBytesActiveRefreshedKB,
       "cacheTotalDiskBytesRetrievedKB": cacheTotalDiskBytesRetrievedKB,
       "cacheTotalDiskFailures": cacheTotalDiskFailures,
       "cacheTotalDiskURLsRetrieved": cacheTotalDiskURLsRetrieved,
       "cacheTotalMemoryBytesRetrievedKB": cacheTotalMemoryBytesRetrievedKB,
       "cacheTotalMemoryURLsRetrieved": cacheTotalMemoryURLsRetrieved,
       "cacheTotalURLsCached": cacheTotalURLsCached,
       "cacheURLCommitPerSec": cacheURLCommitPerSec,
       "cacheURLsInCache": cacheURLsInCache,
       "firewallService": firewallService,
       "fsAcceptingTCPConnections": fsAcceptingTCPConnections,
       "fsActiveSessions": fsActiveSessions,
       "fsActiveTCPConnections": fsActiveTCPConnections,
       "fsActiveUDPConnections": fsActiveUDPConnections,
       "fsAvailableWorkerThreads": fsAvailableWorkerThreads,
       "fsBackConnectingTCPConnections": fsBackConnectingTCPConnections,
       "fsBytesReadPerSec": fsBytesReadPerSec,
       "fsBytesWrittenPerSec": fsBytesWrittenPerSec,
       "fsConnectingTCPConnections": fsConnectingTCPConnections,
       "fsDNSCacheEntries": fsDNSCacheEntries,
       "fsDNSCacheFlushes": fsDNSCacheFlushes,
       "fsDNSCacheHits": fsDNSCacheHits,
       "fsDNSCacheHitsPercent": fsDNSCacheHitsPercent,
       "fsDNSRetrievals": fsDNSRetrievals,
       "fsFailedDNSResolutions": fsFailedDNSResolutions,
       "fsKernelModeDataPumps": fsKernelModeDataPumps,
       "fsListeningTCPConnections": fsListeningTCPConnections,
       "fsNonConnectedUDPMappings": fsNonConnectedUDPMappings,
       "fsPendingDNSResolutions": fsPendingDNSResolutions,
       "fsSecureNATMappings": fsSecureNATMappings,
       "fsSuccessfulDNSResolutions": fsSuccessfulDNSResolutions,
       "fsTCPBytesXferPerSecByKernelMode": fsTCPBytesXferPerSecByKernelMode,
       "fsUDPBytesXferPerSecByKernelMode": fsUDPBytesXferPerSecByKernelMode,
       "fsWorkerThreads": fsWorkerThreads,
       "fsAvailableUDPMappings": fsAvailableUDPMappings,
       "fsDNSCacheLockFailures": fsDNSCacheLockFailures,
       "fsPendingTCPConnections": fsPendingTCPConnections,
       "fsTCPAwaitInConnectCallToFinish": fsTCPAwaitInConnectCallToFinish,
       "firewallEngine": firewallEngine,
       "feActiveConnections": feActiveConnections,
       "feAllowedPackets": feAllowedPackets,
       "feAllowedPacketsPerSec": feAllowedPacketsPerSec,
       "feBackloggedPackets": feBackloggedPackets,
       "feBytes": feBytes,
       "feBytesPerSec": feBytesPerSec,
       "feConnectionsPerSec": feConnectionsPerSec,
       "feDroppedPackets": feDroppedPackets,
       "feDroppedPacketsPerSec": feDroppedPacketsPerSec,
       "fePackets": fePackets,
       "fePacketsPerSec": fePacketsPerSec,
       "feTCPEstablishedConnsPerSec": feTCPEstablishedConnsPerSec,
       "feTCPEstablishedConns": feTCPEstablishedConns,
       "packetFilter": packetFilter,
       "packetsDroppedFilterDenial": packetsDroppedFilterDenial,
       "packetsDroppedProtocolViolation": packetsDroppedProtocolViolation,
       "totalDroppedPackets": totalDroppedPackets,
       "totalLoggingPacketsLost": totalLoggingPacketsLost,
       "totalIncomingConn": totalIncomingConn,
       "webProxyService": webProxyService,
       "wpsArrayBytesReceivedPerSec": wpsArrayBytesReceivedPerSec,
       "wpsArrayBytesSentPerSec": wpsArrayBytesSentPerSec,
       "wpsArrayBytesTotalPerSec": wpsArrayBytesTotalPerSec,
       "wpsCacheHitRatioPercent": wpsCacheHitRatioPercent,
       "wpsCacheRunningHitRatioPercent": wpsCacheRunningHitRatioPercent,
       "wpsClientBytesReceivedPerSec": wpsClientBytesReceivedPerSec,
       "wpsClientBytesSentPerSec": wpsClientBytesSentPerSec,
       "wpsClientBytesTotalPerSec": wpsClientBytesTotalPerSec,
       "wpsConnectErrors": wpsConnectErrors,
       "wpsConnErrsPerTotalErrsPercent": wpsConnErrsPerTotalErrsPercent,
       "wpsCurArrayFetchAvgMSPerRequest": wpsCurArrayFetchAvgMSPerRequest,
       "wpsCurAvgMSPerRequest": wpsCurAvgMSPerRequest,
       "wpsCurCacheFetchAvgMSPerRequest": wpsCurCacheFetchAvgMSPerRequest,
       "wpsCurDirectFetchAvgMSPerRequest": wpsCurDirectFetchAvgMSPerRequest,
       "wpsCurrentUsers": wpsCurrentUsers,
       "wpsDNSCacheEntries": wpsDNSCacheEntries,
       "wpsDNSCacheFlushes": wpsDNSCacheFlushes,
       "wpsDNSCacheHits": wpsDNSCacheHits,
       "wpsDNSCacheHitsPercent": wpsDNSCacheHitsPercent,
       "wpsDNSRetrievals": wpsDNSRetrievals,
       "wpsFailRqstsPerTotalRqstsPercent": wpsFailRqstsPerTotalRqstsPercent,
       "wpsFailRqstsPerSec": wpsFailRqstsPerSec,
       "wpsFailRqstsFromArrayMbr": wpsFailRqstsFromArrayMbr,
       "wpsFailRqstsFromArrayMbrPerErrs": wpsFailRqstsFromArrayMbrPerErrs,
       "wpsFailRqstsToArrayMbr": wpsFailRqstsToArrayMbr,
       "wpsFailRqstsToArrayMbrPerErrs": wpsFailRqstsToArrayMbrPerErrs,
       "wpsFailRqstsKAToArrayMbr": wpsFailRqstsKAToArrayMbr,
       "wpsFailRqstsKAToArrayMbrPerErrs": wpsFailRqstsKAToArrayMbrPerErrs,
       "wpsFailRqstsKAToClient": wpsFailRqstsKAToClient,
       "wpsFailRqstsKAToClientPerErrs": wpsFailRqstsKAToClientPerErrs,
       "wpsFailRqstsKAToServer": wpsFailRqstsKAToServer,
       "wpsFailRqstsKAToServerPerErrs": wpsFailRqstsKAToServerPerErrs,
       "wpsFtpRequests": wpsFtpRequests,
       "wpsHTTPSSessions": wpsHTTPSSessions,
       "wpsHttpRequests": wpsHttpRequests,
       "wpsIOErrorsToArrayMember": wpsIOErrorsToArrayMember,
       "wpsIOErrorsToArrayMemberPerErrs": wpsIOErrorsToArrayMemberPerErrs,
       "wpsIOErrorsToClient": wpsIOErrorsToClient,
       "wpsIOErrorsToClientPerErrs": wpsIOErrorsToClientPerErrs,
       "wpsIOErrorsToServer": wpsIOErrorsToServer,
       "wpsIOErrorsToServerPerErrs": wpsIOErrorsToServerPerErrs,
       "wpsIncomingConnectionsPerSec": wpsIncomingConnectionsPerSec,
       "wpsMaximumUsers": wpsMaximumUsers,
       "wpsOutgoingConnectionsPerSec": wpsOutgoingConnectionsPerSec,
       "wpsRequestsPerSec": wpsRequestsPerSec,
       "wpsReverseBytesReceivedPerSec": wpsReverseBytesReceivedPerSec,
       "wpsReverseBytesSentPerSec": wpsReverseBytesSentPerSec,
       "wpsReverseBytesTotalPerSec": wpsReverseBytesTotalPerSec,
       "wpsSNEWSSessions": wpsSNEWSSessions,
       "wpsSSLClientBytesReceivedPerSec": wpsSSLClientBytesReceivedPerSec,
       "wpsSSLClientBytesSentPerSec": wpsSSLClientBytesSentPerSec,
       "wpsSSLClientBytesTotalPerSec": wpsSSLClientBytesTotalPerSec,
       "wpsSitesDenied": wpsSitesDenied,
       "wpsSitesGranted": wpsSitesGranted,
       "wpsThreadPoolFailures": wpsThreadPoolFailures,
       "wpsThreadPoolSize": wpsThreadPoolSize,
       "wpsThreadPoolActiveSessions": wpsThreadPoolActiveSessions,
       "wpsTotalArrayFetches": wpsTotalArrayFetches,
       "wpsTotalCacheFetches": wpsTotalCacheFetches,
       "wpsTotalFailingRequests": wpsTotalFailingRequests,
       "wpsTotalPendingConnects": wpsTotalPendingConnects,
       "wpsTotalRequests": wpsTotalRequests,
       "wpsTotalReverseFetches": wpsTotalReverseFetches,
       "wpsTotalSSLSessions": wpsTotalSSLSessions,
       "wpsTotalSuccessfulRequests": wpsTotalSuccessfulRequests,
       "wpsTotalUpstreamFetches": wpsTotalUpstreamFetches,
       "wpsTotalUsers": wpsTotalUsers,
       "wpsUnknownSSLSessions": wpsUnknownSSLSessions,
       "wpsUpstreamBytesReceivedPerSec": wpsUpstreamBytesReceivedPerSec,
       "wpsUpstreamBytesSentPerSec": wpsUpstreamBytesSentPerSec,
       "wpsUpstreamBytesTotalPerSec": wpsUpstreamBytesTotalPerSec,
       "wpsActiveWebSessions": wpsActiveWebSessions,
       "wpsAverageMillisecondsPerRequest": wpsAverageMillisecondsPerRequest,
       "wpsBytesRtnPtlCntRsps": wpsBytesRtnPtlCntRsps,
       "wpsBytesRtnPtlCntRspsRqstdServer": wpsBytesRtnPtlCntRspsRqstdServer,
       "wpsBytesRtnPtlCntRspsSvdCh": wpsBytesRtnPtlCntRspsSvdCh,
       "wpsBytesRtnPtlCntRspsSvdChHr": wpsBytesRtnPtlCntRspsSvdChHr,
       "wpsBytesRtnPtlCntRspsBITSEnChRule": wpsBytesRtnPtlCntRspsBITSEnChRule,
       "wpsBytesRtnPtlCntRspsBITSEnChRuleHr": wpsBytesRtnPtlCntRspsBITSEnChRuleHr,
       "wpsBytesRtnPtlCntRspsInLastHour": wpsBytesRtnPtlCntRspsInLastHour,
       "wpsBytesARqstSvrRngRqstRngRqst": wpsBytesARqstSvrRngRqstRngRqst,
       "wpsCacheHitPctForRangeRequests": wpsCacheHitPctForRangeRequests,
       "wpscAccumulatedCompressionRatio": wpscAccumulatedCompressionRatio,
       "wpscAccumulatedPctRspsCompressed": wpscAccumulatedPctRspsCompressed,
       "wpscAccumulatedPctRspsDecompress": wpscAccumulatedPctRspsDecompress,
       "wpscSampledCompressionRatio": wpscSampledCompressionRatio,
       "wpscSampledPctRspsCompressed": wpscSampledPctRspsCompressed,
       "wpscSampledPctRspsDecompressed": wpscSampledPctRspsDecompressed,
       "wpscTotalFailures": wpscTotalFailures,
       "wpsDNSCacheLockFailures": wpsDNSCacheLockFailures,
       "wpsdrq1stPriorityRatioToTotal": wpsdrq1stPriorityRatioToTotal,
       "wpsdrq1stPriority": wpsdrq1stPriority,
       "wpsdrq2ndPriorityRatioToTotal": wpsdrq2ndPriorityRatioToTotal,
       "wpsdrq2ndPriority": wpsdrq2ndPriority,
       "wpsdrq3rdPriorityRatioToTotal": wpsdrq3rdPriorityRatioToTotal,
       "wpsdrq3rdPriority": wpsdrq3rdPriority,
       "wpsdrq4thPriorityRatioToTotal": wpsdrq4thPriorityRatioToTotal,
       "wpsdrq4thPriority": wpsdrq4thPriority,
       "wpsdrq5thPriorityRatioToTotal": wpsdrq5thPriorityRatioToTotal,
       "wpsdrq5thPriority": wpsdrq5thPriority,
       "wpsdrqLowPriorityRatioToTotal": wpsdrqLowPriorityRatioToTotal,
       "wpsdrqLowerPriority": wpsdrqLowerPriority,
       "wpsdrqNon-PriorityRatioToTotal": wpsdrqNon_PriorityRatioToTotal,
       "wpsdrqNon-priority": wpsdrqNon_priority,
       "wpsdrqPriorityRatioToTotal": wpsdrqPriorityRatioToTotal,
       "wpsdrqTotalPriority": wpsdrqTotalPriority,
       "wpsdrs1stPriorityRatioToTotal": wpsdrs1stPriorityRatioToTotal,
       "wpsdrs1stPriority": wpsdrs1stPriority,
       "wpsdrs2ndPriorityRatioToTotal": wpsdrs2ndPriorityRatioToTotal,
       "wpsdrs2ndPriority": wpsdrs2ndPriority,
       "wpsdrs3rdPriorityRatioToTotal": wpsdrs3rdPriorityRatioToTotal,
       "wpsdrs3rdPriority": wpsdrs3rdPriority,
       "wpsdrs4thPriorityRatioToTotal": wpsdrs4thPriorityRatioToTotal,
       "wpsdrs4thPriority": wpsdrs4thPriority,
       "wpsdrs5thPriorityRatioToTotal": wpsdrs5thPriorityRatioToTotal,
       "wpsdrs5thPriority": wpsdrs5thPriority,
       "wpsdrsLowPriorityRatioToTotal": wpsdrsLowPriorityRatioToTotal,
       "wpsdrsLowerPriority": wpsdrsLowerPriority,
       "wpsdrsNon-PriorityRatioToTotal": wpsdrsNon_PriorityRatioToTotal,
       "wpsdrsNon-priority": wpsdrsNon_priority,
       "wpsdrsPriorityRatioToTotal": wpsdrsPriorityRatioToTotal,
       "wpsdrsTotalPriority": wpsdrsTotalPriority,
       "wpsRqstFromAryMember": wpsRqstFromAryMember,
       "wpsRqstFromAryMemberPerErrs": wpsRqstFromAryMemberPerErrs,
       "wpsRqstToAryMember": wpsRqstToAryMember,
       "wpsRqstToAryMemberPerErrs": wpsRqstToAryMemberPerErrs,
       "wpsRqstKeepAliveToAryMember": wpsRqstKeepAliveToAryMember,
       "wpsRqstKeepAliveToAryMbrPerErrs": wpsRqstKeepAliveToAryMbrPerErrs,
       "wpsRqstKeepAliveToClient": wpsRqstKeepAliveToClient,
       "wpsRqstKeepAliveToClientPerErrs": wpsRqstKeepAliveToClientPerErrs,
       "wpsRqstKeepAliveToServer": wpsRqstKeepAliveToServer,
       "wpsRqstKeepAliveToServerPerErrs": wpsRqstKeepAliveToServerPerErrs,
       "wpsRqstWithMultipleRanges": wpsRqstWithMultipleRanges,
       "wpsAverageRequestSpeed": wpsAverageRequestSpeed,
       "wpsBytesRequestedFromServerInRanges": wpsBytesRequestedFromServerInRanges,
       "wpsBytesServedLastHourFromCacheInRanges": wpsBytesServedLastHourFromCacheInRanges,
       "wpsBytesServedLastHourInRanges": wpsBytesServedLastHourInRanges,
       "wpsBytesServedFromCacheInRanges": wpsBytesServedFromCacheInRanges,
       "wpsBytesServedInRanges": wpsBytesServedInRanges,
       "wpsCompCurrentCompressionRatio": wpsCompCurrentCompressionRatio,
       "wpsCompCurRatioOfRspsCompressed": wpsCompCurRatioOfRspsCompressed,
       "wpsCompCurRatioOfRspsDecompress": wpsCompCurRatioOfRspsDecompress,
       "wpsCompRatioOfSizeReduction": wpsCompRatioOfSizeReduction,
       "wpsCompRspsCompAccumulatedRatio": wpsCompRspsCompAccumulatedRatio,
       "wpsCompRspsDcompAccumulatedRatio": wpsCompRspsDcompAccumulatedRatio,
       "wpsMemoryPoolForHTTPRqstPercent": wpsMemoryPoolForHTTPRqstPercent,
       "wpsMemoryPoolForSSLRqstPercent": wpsMemoryPoolForSSLRqstPercent,
       "socksFilter": socksFilter,
       "socksFilterActiveConnections": socksFilterActiveConnections,
       "socksFilterActiveSessions": socksFilterActiveSessions,
       "socksFilterBytesReadPerSec": socksFilterBytesReadPerSec,
       "socksFilterBytesWrittenPerSec": socksFilterBytesWrittenPerSec,
       "socksFilterConnectingConnections": socksFilterConnectingConnections,
       "socksFilterListeningConnections": socksFilterListeningConnections,
       "socksFilterPendingDNSResolutions": socksFilterPendingDNSResolutions,
       "socksFilterSuccessDNSResolutions": socksFilterSuccessDNSResolutions}
)
