# SNMP MIB module (ASYNCOSWEBSECURITYAPPLIANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASYNCOSWEBSECURITYAPPLIANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:56 2024
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

(connectionURL,) = mibBuilder.importSymbols(
    "ASYNCOS-MAIL-MIB",
    "connectionURL")

(asyncOSAppliances,) = mibBuilder.importSymbols(
    "IRONPORT-SMI",
    "asyncOSAppliances")

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

asyncOSWebSecurityAppliance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2)
)
asyncOSWebSecurityAppliance.setRevisions(
        ("2013-08-09 00:00",
         "2010-04-20 00:00",
         "2010-04-15 00:00",
         "2009-07-13 00:00",
         "2007-03-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ProxySystem_ObjectIdentity = ObjectIdentity
proxySystem = _ProxySystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 1)
)
_CacheUptime_Type = TimeTicks
_CacheUptime_Object = MibScalar
cacheUptime = _CacheUptime_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 1, 1),
    _CacheUptime_Type()
)
cacheUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheUptime.setStatus("current")
_CacheMemory_Type = Integer32
_CacheMemory_Object = MibScalar
cacheMemory = _CacheMemory_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 1, 2),
    _CacheMemory_Type()
)
cacheMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMemory.setStatus("current")
_CacheSysStorage_Type = Integer32
_CacheSysStorage_Object = MibScalar
cacheSysStorage = _CacheSysStorage_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 1, 3),
    _CacheSysStorage_Type()
)
cacheSysStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSysStorage.setStatus("current")
_ProxyConfig_ObjectIdentity = ObjectIdentity
proxyConfig = _ProxyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 2)
)
_CacheAdmin_Type = DisplayString
_CacheAdmin_Object = MibScalar
cacheAdmin = _CacheAdmin_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 2, 1),
    _CacheAdmin_Type()
)
cacheAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheAdmin.setStatus("current")
_CacheSoftware_Type = DisplayString
_CacheSoftware_Object = MibScalar
cacheSoftware = _CacheSoftware_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 2, 2),
    _CacheSoftware_Type()
)
cacheSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSoftware.setStatus("current")
_CacheVersion_Type = DisplayString
_CacheVersion_Object = MibScalar
cacheVersion = _CacheVersion_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 2, 3),
    _CacheVersion_Type()
)
cacheVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheVersion.setStatus("current")
_LicenseExpiration_Type = Integer32
_LicenseExpiration_Object = MibScalar
licenseExpiration = _LicenseExpiration_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 2, 4),
    _LicenseExpiration_Type()
)
licenseExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseExpiration.setStatus("current")
_ProxyPerf_ObjectIdentity = ObjectIdentity
proxyPerf = _ProxyPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3)
)
_ProxySysPerf_ObjectIdentity = ObjectIdentity
proxySysPerf = _ProxySysPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 1)
)
_CacheCpuTime_Type = Integer32
_CacheCpuTime_Object = MibScalar
cacheCpuTime = _CacheCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 1, 1),
    _CacheCpuTime_Type()
)
cacheCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCpuTime.setStatus("current")
_CacheCpuUsage_Type = Integer32
_CacheCpuUsage_Object = MibScalar
cacheCpuUsage = _CacheCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 1, 2),
    _CacheCpuUsage_Type()
)
cacheCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCpuUsage.setStatus("current")
_CacheMaxResSize_Type = Integer32
_CacheMaxResSize_Object = MibScalar
cacheMaxResSize = _CacheMaxResSize_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 1, 3),
    _CacheMaxResSize_Type()
)
cacheMaxResSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMaxResSize.setStatus("current")
_CacheUsedStoragePct_Type = Integer32
_CacheUsedStoragePct_Object = MibScalar
cacheUsedStoragePct = _CacheUsedStoragePct_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 1, 4),
    _CacheUsedStoragePct_Type()
)
cacheUsedStoragePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheUsedStoragePct.setStatus("current")
_CacheBusyCPUPct_Type = Integer32
_CacheBusyCPUPct_Object = MibScalar
cacheBusyCPUPct = _CacheBusyCPUPct_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 1, 5),
    _CacheBusyCPUPct_Type()
)
cacheBusyCPUPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBusyCPUPct.setStatus("current")
_CacheMemoryBufferUsagePct_Type = Integer32
_CacheMemoryBufferUsagePct_Object = MibScalar
cacheMemoryBufferUsagePct = _CacheMemoryBufferUsagePct_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 1, 6),
    _CacheMemoryBufferUsagePct_Type()
)
cacheMemoryBufferUsagePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMemoryBufferUsagePct.setStatus("current")
_ProxyClientSidePerf_ObjectIdentity = ObjectIdentity
proxyClientSidePerf = _ProxyClientSidePerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2)
)
_CacheClientSizeHistTable_Object = MibTable
cacheClientSizeHistTable = _CacheClientSizeHistTable_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cacheClientSizeHistTable.setStatus("current")
_CacheClientSizeHistEntry_Object = MibTableRow
cacheClientSizeHistEntry = _CacheClientSizeHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 1, 1)
)
cacheClientSizeHistEntry.setIndexNames(
    (0, "ASYNCOSWEBSECURITYAPPLIANCE-MIB", "cacheClientSizeHistBinNumber"),
)
if mibBuilder.loadTexts:
    cacheClientSizeHistEntry.setStatus("current")


class _CacheClientSizeHistBinNumber_Type(Integer32):
    """Custom type cacheClientSizeHistBinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CacheClientSizeHistBinNumber_Type.__name__ = "Integer32"
_CacheClientSizeHistBinNumber_Object = MibTableColumn
cacheClientSizeHistBinNumber = _CacheClientSizeHistBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 1, 1, 1),
    _CacheClientSizeHistBinNumber_Type()
)
cacheClientSizeHistBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientSizeHistBinNumber.setStatus("current")
_CacheClientReqSize_Type = Integer32
_CacheClientReqSize_Object = MibTableColumn
cacheClientReqSize = _CacheClientReqSize_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 1, 1, 2),
    _CacheClientReqSize_Type()
)
cacheClientReqSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientReqSize.setStatus("current")
_CacheClientRequests_Type = Counter32
_CacheClientRequests_Object = MibScalar
cacheClientRequests = _CacheClientRequests_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 2),
    _CacheClientRequests_Type()
)
cacheClientRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientRequests.setStatus("current")
_CacheClientHits_Type = Counter32
_CacheClientHits_Object = MibScalar
cacheClientHits = _CacheClientHits_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 3),
    _CacheClientHits_Type()
)
cacheClientHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientHits.setStatus("current")
_CacheClientErrors_Type = Counter32
_CacheClientErrors_Object = MibScalar
cacheClientErrors = _CacheClientErrors_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 4),
    _CacheClientErrors_Type()
)
cacheClientErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientErrors.setStatus("current")
_CacheClientInKb_Type = Counter32
_CacheClientInKb_Object = MibScalar
cacheClientInKb = _CacheClientInKb_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 5),
    _CacheClientInKb_Type()
)
cacheClientInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientInKb.setStatus("current")
_CacheClientOutKb_Type = Counter32
_CacheClientOutKb_Object = MibScalar
cacheClientOutKb = _CacheClientOutKb_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 6),
    _CacheClientOutKb_Type()
)
cacheClientOutKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientOutKb.setStatus("current")
_CacheClientIdleConns_Type = Counter32
_CacheClientIdleConns_Object = MibScalar
cacheClientIdleConns = _CacheClientIdleConns_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 7),
    _CacheClientIdleConns_Type()
)
cacheClientIdleConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientIdleConns.setStatus("current")
_CacheClientTotalConns_Type = Integer32
_CacheClientTotalConns_Object = MibScalar
cacheClientTotalConns = _CacheClientTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 8),
    _CacheClientTotalConns_Type()
)
cacheClientTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientTotalConns.setStatus("current")
_CacheClientMaxConns_Type = Counter32
_CacheClientMaxConns_Object = MibScalar
cacheClientMaxConns = _CacheClientMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 9),
    _CacheClientMaxConns_Type()
)
cacheClientMaxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientMaxConns.setStatus("current")
_CacheClientAccepts_Type = Counter32
_CacheClientAccepts_Object = MibScalar
cacheClientAccepts = _CacheClientAccepts_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 10),
    _CacheClientAccepts_Type()
)
cacheClientAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientAccepts.setStatus("current")
_CacheClientICPRequests_Type = Counter32
_CacheClientICPRequests_Object = MibScalar
cacheClientICPRequests = _CacheClientICPRequests_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 11),
    _CacheClientICPRequests_Type()
)
cacheClientICPRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientICPRequests.setStatus("current")
_CacheClientICPHits_Type = Counter32
_CacheClientICPHits_Object = MibScalar
cacheClientICPHits = _CacheClientICPHits_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 12),
    _CacheClientICPHits_Type()
)
cacheClientICPHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientICPHits.setStatus("current")
_CacheClientICPMisses_Type = Counter32
_CacheClientICPMisses_Object = MibScalar
cacheClientICPMisses = _CacheClientICPMisses_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 13),
    _CacheClientICPMisses_Type()
)
cacheClientICPMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientICPMisses.setStatus("current")
_CacheClientICPErrors_Type = Counter32
_CacheClientICPErrors_Object = MibScalar
cacheClientICPErrors = _CacheClientICPErrors_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 14),
    _CacheClientICPErrors_Type()
)
cacheClientICPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientICPErrors.setStatus("current")
_CacheClientICPDenials_Type = Counter32
_CacheClientICPDenials_Object = MibScalar
cacheClientICPDenials = _CacheClientICPDenials_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 15),
    _CacheClientICPDenials_Type()
)
cacheClientICPDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientICPDenials.setStatus("current")
_CacheClientReqMisses_Type = Counter32
_CacheClientReqMisses_Object = MibScalar
cacheClientReqMisses = _CacheClientReqMisses_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 16),
    _CacheClientReqMisses_Type()
)
cacheClientReqMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientReqMisses.setStatus("current")
_CacheClientReqDenials_Type = Counter32
_CacheClientReqDenials_Object = MibScalar
cacheClientReqDenials = _CacheClientReqDenials_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 2, 17),
    _CacheClientReqDenials_Type()
)
cacheClientReqDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientReqDenials.setStatus("current")
_ProxyServerSidePerf_ObjectIdentity = ObjectIdentity
proxyServerSidePerf = _ProxyServerSidePerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3)
)
_CacheServerSizeHistTable_Object = MibTable
cacheServerSizeHistTable = _CacheServerSizeHistTable_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cacheServerSizeHistTable.setStatus("current")
_CacheServerSizeHistEntry_Object = MibTableRow
cacheServerSizeHistEntry = _CacheServerSizeHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 1, 1)
)
cacheServerSizeHistEntry.setIndexNames(
    (0, "ASYNCOSWEBSECURITYAPPLIANCE-MIB", "cacheServerSizeHistBinNumber"),
)
if mibBuilder.loadTexts:
    cacheServerSizeHistEntry.setStatus("current")


class _CacheServerSizeHistBinNumber_Type(Integer32):
    """Custom type cacheServerSizeHistBinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CacheServerSizeHistBinNumber_Type.__name__ = "Integer32"
_CacheServerSizeHistBinNumber_Object = MibTableColumn
cacheServerSizeHistBinNumber = _CacheServerSizeHistBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 1, 1, 1),
    _CacheServerSizeHistBinNumber_Type()
)
cacheServerSizeHistBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerSizeHistBinNumber.setStatus("current")
_CacheServerReplySize_Type = Integer32
_CacheServerReplySize_Object = MibTableColumn
cacheServerReplySize = _CacheServerReplySize_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 1, 1, 2),
    _CacheServerReplySize_Type()
)
cacheServerReplySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerReplySize.setStatus("current")
_CacheServerRequests_Type = Counter32
_CacheServerRequests_Object = MibScalar
cacheServerRequests = _CacheServerRequests_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 2),
    _CacheServerRequests_Type()
)
cacheServerRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerRequests.setStatus("current")
_CacheServerSockets_Type = Counter32
_CacheServerSockets_Object = MibScalar
cacheServerSockets = _CacheServerSockets_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 3),
    _CacheServerSockets_Type()
)
cacheServerSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerSockets.setStatus("current")
_CacheServerErrors_Type = Counter32
_CacheServerErrors_Object = MibScalar
cacheServerErrors = _CacheServerErrors_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 4),
    _CacheServerErrors_Type()
)
cacheServerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerErrors.setStatus("current")
_CacheServerInKb_Type = Counter32
_CacheServerInKb_Object = MibScalar
cacheServerInKb = _CacheServerInKb_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 5),
    _CacheServerInKb_Type()
)
cacheServerInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerInKb.setStatus("current")
_CacheServerOutKb_Type = Counter32
_CacheServerOutKb_Object = MibScalar
cacheServerOutKb = _CacheServerOutKb_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 6),
    _CacheServerOutKb_Type()
)
cacheServerOutKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerOutKb.setStatus("current")
_CacheServerIdleConns_Type = Counter32
_CacheServerIdleConns_Object = MibScalar
cacheServerIdleConns = _CacheServerIdleConns_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 7),
    _CacheServerIdleConns_Type()
)
cacheServerIdleConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerIdleConns.setStatus("current")
_CacheServerTotalConns_Type = Counter32
_CacheServerTotalConns_Object = MibScalar
cacheServerTotalConns = _CacheServerTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 8),
    _CacheServerTotalConns_Type()
)
cacheServerTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerTotalConns.setStatus("current")
_CacheServerCloseIdleConns_Type = Counter32
_CacheServerCloseIdleConns_Object = MibScalar
cacheServerCloseIdleConns = _CacheServerCloseIdleConns_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 9),
    _CacheServerCloseIdleConns_Type()
)
cacheServerCloseIdleConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerCloseIdleConns.setStatus("current")
_CacheServerLimitIdleConns_Type = Counter32
_CacheServerLimitIdleConns_Object = MibScalar
cacheServerLimitIdleConns = _CacheServerLimitIdleConns_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 10),
    _CacheServerLimitIdleConns_Type()
)
cacheServerLimitIdleConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerLimitIdleConns.setStatus("current")
_CacheServerConnsThresh_Type = Counter32
_CacheServerConnsThresh_Object = MibScalar
cacheServerConnsThresh = _CacheServerConnsThresh_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 11),
    _CacheServerConnsThresh_Type()
)
cacheServerConnsThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerConnsThresh.setStatus("current")
_CacheServerPersisConnsRetries_Type = Counter32
_CacheServerPersisConnsRetries_Object = MibScalar
cacheServerPersisConnsRetries = _CacheServerPersisConnsRetries_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 12),
    _CacheServerPersisConnsRetries_Type()
)
cacheServerPersisConnsRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerPersisConnsRetries.setStatus("current")
_CacheServerRegConnsRetries_Type = Counter32
_CacheServerRegConnsRetries_Object = MibScalar
cacheServerRegConnsRetries = _CacheServerRegConnsRetries_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 13),
    _CacheServerRegConnsRetries_Type()
)
cacheServerRegConnsRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerRegConnsRetries.setStatus("current")
_CacheServerRWErrorRetries_Type = Counter32
_CacheServerRWErrorRetries_Object = MibScalar
cacheServerRWErrorRetries = _CacheServerRWErrorRetries_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 14),
    _CacheServerRWErrorRetries_Type()
)
cacheServerRWErrorRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerRWErrorRetries.setStatus("current")
_CacheServerEarlyCloseRetries_Type = Counter32
_CacheServerEarlyCloseRetries_Object = MibScalar
cacheServerEarlyCloseRetries = _CacheServerEarlyCloseRetries_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 15),
    _CacheServerEarlyCloseRetries_Type()
)
cacheServerEarlyCloseRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerEarlyCloseRetries.setStatus("current")
_CacheServerICPRequests_Type = Counter32
_CacheServerICPRequests_Object = MibScalar
cacheServerICPRequests = _CacheServerICPRequests_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 16),
    _CacheServerICPRequests_Type()
)
cacheServerICPRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerICPRequests.setStatus("current")
_CacheServerICPHits_Type = Counter32
_CacheServerICPHits_Object = MibScalar
cacheServerICPHits = _CacheServerICPHits_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 17),
    _CacheServerICPHits_Type()
)
cacheServerICPHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerICPHits.setStatus("current")
_CacheServerICPMisses_Type = Counter32
_CacheServerICPMisses_Object = MibScalar
cacheServerICPMisses = _CacheServerICPMisses_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 18),
    _CacheServerICPMisses_Type()
)
cacheServerICPMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerICPMisses.setStatus("current")
_CacheServerICPErrors_Type = Counter32
_CacheServerICPErrors_Object = MibScalar
cacheServerICPErrors = _CacheServerICPErrors_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 19),
    _CacheServerICPErrors_Type()
)
cacheServerICPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerICPErrors.setStatus("current")
_CacheServerICPDenials_Type = Counter32
_CacheServerICPDenials_Object = MibScalar
cacheServerICPDenials = _CacheServerICPDenials_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 3, 20),
    _CacheServerICPDenials_Type()
)
cacheServerICPDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerICPDenials.setStatus("current")
_ProxyCachePerf_ObjectIdentity = ObjectIdentity
proxyCachePerf = _ProxyCachePerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 4)
)
_CacheCacheSizeHistTable_Object = MibTable
cacheCacheSizeHistTable = _CacheCacheSizeHistTable_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    cacheCacheSizeHistTable.setStatus("current")
_CacheCacheSizeHistEntry_Object = MibTableRow
cacheCacheSizeHistEntry = _CacheCacheSizeHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 4, 1, 1)
)
cacheCacheSizeHistEntry.setIndexNames(
    (0, "ASYNCOSWEBSECURITYAPPLIANCE-MIB", "cacheSizeHistBinNumber"),
)
if mibBuilder.loadTexts:
    cacheCacheSizeHistEntry.setStatus("current")


class _CacheSizeHistBinNumber_Type(Integer32):
    """Custom type cacheSizeHistBinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CacheSizeHistBinNumber_Type.__name__ = "Integer32"
_CacheSizeHistBinNumber_Object = MibTableColumn
cacheSizeHistBinNumber = _CacheSizeHistBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 4, 1, 1, 1),
    _CacheSizeHistBinNumber_Type()
)
cacheSizeHistBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSizeHistBinNumber.setStatus("current")
_CacheCacheActiveObjs_Type = Integer32
_CacheCacheActiveObjs_Object = MibTableColumn
cacheCacheActiveObjs = _CacheCacheActiveObjs_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 4, 1, 1, 2),
    _CacheCacheActiveObjs_Type()
)
cacheCacheActiveObjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCacheActiveObjs.setStatus("current")
_CacheCacheAllObjs_Type = Integer32
_CacheCacheAllObjs_Object = MibTableColumn
cacheCacheAllObjs = _CacheCacheAllObjs_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 4, 1, 1, 3),
    _CacheCacheAllObjs_Type()
)
cacheCacheAllObjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCacheAllObjs.setStatus("current")
_CacheCacheLiveCachedObjs_Type = Counter32
_CacheCacheLiveCachedObjs_Object = MibScalar
cacheCacheLiveCachedObjs = _CacheCacheLiveCachedObjs_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 4, 2),
    _CacheCacheLiveCachedObjs_Type()
)
cacheCacheLiveCachedObjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCacheLiveCachedObjs.setStatus("current")
_CacheCacheLiveCachedObjSizes_Type = Counter32
_CacheCacheLiveCachedObjSizes_Object = MibScalar
cacheCacheLiveCachedObjSizes = _CacheCacheLiveCachedObjSizes_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 4, 3),
    _CacheCacheLiveCachedObjSizes_Type()
)
cacheCacheLiveCachedObjSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCacheLiveCachedObjSizes.setStatus("current")
_CacheCacheTotalCachedObjs_Type = Counter32
_CacheCacheTotalCachedObjs_Object = MibScalar
cacheCacheTotalCachedObjs = _CacheCacheTotalCachedObjs_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 4, 4),
    _CacheCacheTotalCachedObjs_Type()
)
cacheCacheTotalCachedObjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCacheTotalCachedObjs.setStatus("current")
_CacheCacheTotalCachedObjSizes_Type = Counter32
_CacheCacheTotalCachedObjSizes_Object = MibScalar
cacheCacheTotalCachedObjSizes = _CacheCacheTotalCachedObjSizes_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 4, 5),
    _CacheCacheTotalCachedObjSizes_Type()
)
cacheCacheTotalCachedObjSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCacheTotalCachedObjSizes.setStatus("current")
_ProxyMedianSvcTime_ObjectIdentity = ObjectIdentity
proxyMedianSvcTime = _ProxyMedianSvcTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 5)
)
_CacheMedianSvcTable_Object = MibTable
cacheMedianSvcTable = _CacheMedianSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    cacheMedianSvcTable.setStatus("current")
_CacheMedianSvcEntry_Object = MibTableRow
cacheMedianSvcEntry = _CacheMedianSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 5, 1, 1)
)
cacheMedianSvcEntry.setIndexNames(
    (0, "ASYNCOSWEBSECURITYAPPLIANCE-MIB", "cacheMedianTime"),
)
if mibBuilder.loadTexts:
    cacheMedianSvcEntry.setStatus("current")


class _CacheMedianTime_Type(Integer32):
    """Custom type cacheMedianTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CacheMedianTime_Type.__name__ = "Integer32"
_CacheMedianTime_Object = MibTableColumn
cacheMedianTime = _CacheMedianTime_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 5, 1, 1, 1),
    _CacheMedianTime_Type()
)
cacheMedianTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMedianTime.setStatus("current")
_CacheHTTPCltSvcTime_Type = Integer32
_CacheHTTPCltSvcTime_Object = MibTableColumn
cacheHTTPCltSvcTime = _CacheHTTPCltSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 5, 1, 1, 2),
    _CacheHTTPCltSvcTime_Type()
)
cacheHTTPCltSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHTTPCltSvcTime.setStatus("current")
_CacheHTTPMissSvcTime_Type = Integer32
_CacheHTTPMissSvcTime_Object = MibTableColumn
cacheHTTPMissSvcTime = _CacheHTTPMissSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 5, 1, 1, 3),
    _CacheHTTPMissSvcTime_Type()
)
cacheHTTPMissSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHTTPMissSvcTime.setStatus("current")
_CacheHTTPHitSvcTime_Type = Integer32
_CacheHTTPHitSvcTime_Object = MibTableColumn
cacheHTTPHitSvcTime = _CacheHTTPHitSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 5, 1, 1, 4),
    _CacheHTTPHitSvcTime_Type()
)
cacheHTTPHitSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHTTPHitSvcTime.setStatus("current")
_CacheHTTPSrvSvcTime_Type = Integer32
_CacheHTTPSrvSvcTime_Object = MibTableColumn
cacheHTTPSrvSvcTime = _CacheHTTPSrvSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 5, 1, 1, 5),
    _CacheHTTPSrvSvcTime_Type()
)
cacheHTTPSrvSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHTTPSrvSvcTime.setStatus("current")
_CacheDnsSvcTime_Type = Integer32
_CacheDnsSvcTime_Object = MibTableColumn
cacheDnsSvcTime = _CacheDnsSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 5, 1, 1, 6),
    _CacheDnsSvcTime_Type()
)
cacheDnsSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDnsSvcTime.setStatus("current")
_CacheHTTPSvcWaitTime_Type = Integer32
_CacheHTTPSvcWaitTime_Object = MibScalar
cacheHTTPSvcWaitTime = _CacheHTTPSvcWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 5, 1, 1, 7),
    _CacheHTTPSvcWaitTime_Type()
)
cacheHTTPSvcWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHTTPSvcWaitTime.setStatus("current")
_ProxyExecutiveSummary_ObjectIdentity = ObjectIdentity
proxyExecutiveSummary = _ProxyExecutiveSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 6)
)
_CacheTotalHttpReqs_Type = Integer32
_CacheTotalHttpReqs_Object = MibScalar
cacheTotalHttpReqs = _CacheTotalHttpReqs_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 6, 1),
    _CacheTotalHttpReqs_Type()
)
cacheTotalHttpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalHttpReqs.setStatus("current")
_CacheMeanRespTime_Type = Integer32
_CacheMeanRespTime_Object = MibScalar
cacheMeanRespTime = _CacheMeanRespTime_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 6, 2),
    _CacheMeanRespTime_Type()
)
cacheMeanRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMeanRespTime.setStatus("current")
_CacheMeanMissRespTime_Type = Integer32
_CacheMeanMissRespTime_Object = MibScalar
cacheMeanMissRespTime = _CacheMeanMissRespTime_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 6, 3),
    _CacheMeanMissRespTime_Type()
)
cacheMeanMissRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMeanMissRespTime.setStatus("current")
_CacheMeanHitRespTime_Type = Integer32
_CacheMeanHitRespTime_Object = MibScalar
cacheMeanHitRespTime = _CacheMeanHitRespTime_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 6, 4),
    _CacheMeanHitRespTime_Type()
)
cacheMeanHitRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMeanHitRespTime.setStatus("current")
_CacheMeanHitRatio_Type = Integer32
_CacheMeanHitRatio_Object = MibScalar
cacheMeanHitRatio = _CacheMeanHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 6, 5),
    _CacheMeanHitRatio_Type()
)
cacheMeanHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMeanHitRatio.setStatus("current")
_CacheMeanByteHitRatio_Type = Integer32
_CacheMeanByteHitRatio_Object = MibScalar
cacheMeanByteHitRatio = _CacheMeanByteHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 6, 6),
    _CacheMeanByteHitRatio_Type()
)
cacheMeanByteHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMeanByteHitRatio.setStatus("current")
_CacheTotalBandwidthSaving_Type = Integer32
_CacheTotalBandwidthSaving_Object = MibScalar
cacheTotalBandwidthSaving = _CacheTotalBandwidthSaving_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 6, 7),
    _CacheTotalBandwidthSaving_Type()
)
cacheTotalBandwidthSaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalBandwidthSaving.setStatus("current")
_CacheDuration_Type = Integer32
_CacheDuration_Object = MibScalar
cacheDuration = _CacheDuration_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 6, 8),
    _CacheDuration_Type()
)
cacheDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDuration.setStatus("current")
_CacheCltReplyErrPct_Type = Integer32
_CacheCltReplyErrPct_Object = MibScalar
cacheCltReplyErrPct = _CacheCltReplyErrPct_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 6, 9),
    _CacheCltReplyErrPct_Type()
)
cacheCltReplyErrPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCltReplyErrPct.setStatus("current")
_ProxyRecentPerf_ObjectIdentity = ObjectIdentity
proxyRecentPerf = _ProxyRecentPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7)
)
_ProxyRecentThruputPerf_ObjectIdentity = ObjectIdentity
proxyRecentThruputPerf = _ProxyRecentThruputPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 1)
)
_CacheThruputNow_Type = Integer32
_CacheThruputNow_Object = MibScalar
cacheThruputNow = _CacheThruputNow_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 1, 1),
    _CacheThruputNow_Type()
)
cacheThruputNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheThruputNow.setStatus("current")
_CacheThruput1hrPeak_Type = Integer32
_CacheThruput1hrPeak_Object = MibScalar
cacheThruput1hrPeak = _CacheThruput1hrPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 1, 2),
    _CacheThruput1hrPeak_Type()
)
cacheThruput1hrPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheThruput1hrPeak.setStatus("current")
_CacheThruput1hrMean_Type = Integer32
_CacheThruput1hrMean_Object = MibScalar
cacheThruput1hrMean = _CacheThruput1hrMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 1, 3),
    _CacheThruput1hrMean_Type()
)
cacheThruput1hrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheThruput1hrMean.setStatus("current")
_CacheThruput1dayPeak_Type = Integer32
_CacheThruput1dayPeak_Object = MibScalar
cacheThruput1dayPeak = _CacheThruput1dayPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 1, 4),
    _CacheThruput1dayPeak_Type()
)
cacheThruput1dayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheThruput1dayPeak.setStatus("current")
_CacheThruput1dayMean_Type = Integer32
_CacheThruput1dayMean_Object = MibScalar
cacheThruput1dayMean = _CacheThruput1dayMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 1, 5),
    _CacheThruput1dayMean_Type()
)
cacheThruput1dayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheThruput1dayMean.setStatus("current")
_CacheThruput1weekPeak_Type = Integer32
_CacheThruput1weekPeak_Object = MibScalar
cacheThruput1weekPeak = _CacheThruput1weekPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 1, 6),
    _CacheThruput1weekPeak_Type()
)
cacheThruput1weekPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheThruput1weekPeak.setStatus("current")
_CacheThruput1weekMean_Type = Integer32
_CacheThruput1weekMean_Object = MibScalar
cacheThruput1weekMean = _CacheThruput1weekMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 1, 7),
    _CacheThruput1weekMean_Type()
)
cacheThruput1weekMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheThruput1weekMean.setStatus("current")
_CacheThruputLifePeak_Type = Integer32
_CacheThruputLifePeak_Object = MibScalar
cacheThruputLifePeak = _CacheThruputLifePeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 1, 8),
    _CacheThruputLifePeak_Type()
)
cacheThruputLifePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheThruputLifePeak.setStatus("current")
_CacheThruputLifeMean_Type = Integer32
_CacheThruputLifeMean_Object = MibScalar
cacheThruputLifeMean = _CacheThruputLifeMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 1, 9),
    _CacheThruputLifeMean_Type()
)
cacheThruputLifeMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheThruputLifeMean.setStatus("current")
_ProxyRecentBandWSavPerf_ObjectIdentity = ObjectIdentity
proxyRecentBandWSavPerf = _ProxyRecentBandWSavPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 2)
)
_CacheBwidthSavingNow_Type = Integer32
_CacheBwidthSavingNow_Object = MibScalar
cacheBwidthSavingNow = _CacheBwidthSavingNow_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 2, 1),
    _CacheBwidthSavingNow_Type()
)
cacheBwidthSavingNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSavingNow.setStatus("current")
_CacheBwidthSaving1hrPeak_Type = Integer32
_CacheBwidthSaving1hrPeak_Object = MibScalar
cacheBwidthSaving1hrPeak = _CacheBwidthSaving1hrPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 2, 2),
    _CacheBwidthSaving1hrPeak_Type()
)
cacheBwidthSaving1hrPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSaving1hrPeak.setStatus("current")
_CacheBwidthSaving1hrMean_Type = Integer32
_CacheBwidthSaving1hrMean_Object = MibScalar
cacheBwidthSaving1hrMean = _CacheBwidthSaving1hrMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 2, 3),
    _CacheBwidthSaving1hrMean_Type()
)
cacheBwidthSaving1hrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSaving1hrMean.setStatus("current")
_CacheBwidthSaving1dayPeak_Type = Integer32
_CacheBwidthSaving1dayPeak_Object = MibScalar
cacheBwidthSaving1dayPeak = _CacheBwidthSaving1dayPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 2, 4),
    _CacheBwidthSaving1dayPeak_Type()
)
cacheBwidthSaving1dayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSaving1dayPeak.setStatus("current")
_CacheBwidthSaving1dayMean_Type = Integer32
_CacheBwidthSaving1dayMean_Object = MibScalar
cacheBwidthSaving1dayMean = _CacheBwidthSaving1dayMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 2, 5),
    _CacheBwidthSaving1dayMean_Type()
)
cacheBwidthSaving1dayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSaving1dayMean.setStatus("current")
_CacheBwidthSaving1weekPeak_Type = Integer32
_CacheBwidthSaving1weekPeak_Object = MibScalar
cacheBwidthSaving1weekPeak = _CacheBwidthSaving1weekPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 2, 6),
    _CacheBwidthSaving1weekPeak_Type()
)
cacheBwidthSaving1weekPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSaving1weekPeak.setStatus("current")
_CacheBwidthSaving1weekMean_Type = Integer32
_CacheBwidthSaving1weekMean_Object = MibScalar
cacheBwidthSaving1weekMean = _CacheBwidthSaving1weekMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 2, 7),
    _CacheBwidthSaving1weekMean_Type()
)
cacheBwidthSaving1weekMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSaving1weekMean.setStatus("current")
_CacheBwidthSavingLifePeak_Type = Integer32
_CacheBwidthSavingLifePeak_Object = MibScalar
cacheBwidthSavingLifePeak = _CacheBwidthSavingLifePeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 2, 8),
    _CacheBwidthSavingLifePeak_Type()
)
cacheBwidthSavingLifePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSavingLifePeak.setStatus("current")
_CacheBwidthSavingLifeMean_Type = Integer32
_CacheBwidthSavingLifeMean_Object = MibScalar
cacheBwidthSavingLifeMean = _CacheBwidthSavingLifeMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 2, 9),
    _CacheBwidthSavingLifeMean_Type()
)
cacheBwidthSavingLifeMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSavingLifeMean.setStatus("current")
_ProxyRecentBandWSpntPerf_ObjectIdentity = ObjectIdentity
proxyRecentBandWSpntPerf = _ProxyRecentBandWSpntPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 3)
)
_CacheBwidthSpentNow_Type = Integer32
_CacheBwidthSpentNow_Object = MibScalar
cacheBwidthSpentNow = _CacheBwidthSpentNow_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 3, 1),
    _CacheBwidthSpentNow_Type()
)
cacheBwidthSpentNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSpentNow.setStatus("current")
_CacheBwidthSpent1hrPeak_Type = Integer32
_CacheBwidthSpent1hrPeak_Object = MibScalar
cacheBwidthSpent1hrPeak = _CacheBwidthSpent1hrPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 3, 2),
    _CacheBwidthSpent1hrPeak_Type()
)
cacheBwidthSpent1hrPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSpent1hrPeak.setStatus("current")
_CacheBwidthSpent1hrMean_Type = Integer32
_CacheBwidthSpent1hrMean_Object = MibScalar
cacheBwidthSpent1hrMean = _CacheBwidthSpent1hrMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 3, 3),
    _CacheBwidthSpent1hrMean_Type()
)
cacheBwidthSpent1hrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSpent1hrMean.setStatus("current")
_CacheBwidthSpent1dayPeak_Type = Integer32
_CacheBwidthSpent1dayPeak_Object = MibScalar
cacheBwidthSpent1dayPeak = _CacheBwidthSpent1dayPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 3, 4),
    _CacheBwidthSpent1dayPeak_Type()
)
cacheBwidthSpent1dayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSpent1dayPeak.setStatus("current")
_CacheBwidthSpent1dayMean_Type = Integer32
_CacheBwidthSpent1dayMean_Object = MibScalar
cacheBwidthSpent1dayMean = _CacheBwidthSpent1dayMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 3, 5),
    _CacheBwidthSpent1dayMean_Type()
)
cacheBwidthSpent1dayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSpent1dayMean.setStatus("current")
_CacheBwidthSpent1weekPeak_Type = Integer32
_CacheBwidthSpent1weekPeak_Object = MibScalar
cacheBwidthSpent1weekPeak = _CacheBwidthSpent1weekPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 3, 6),
    _CacheBwidthSpent1weekPeak_Type()
)
cacheBwidthSpent1weekPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSpent1weekPeak.setStatus("current")
_CacheBwidthSpent1weekMean_Type = Integer32
_CacheBwidthSpent1weekMean_Object = MibScalar
cacheBwidthSpent1weekMean = _CacheBwidthSpent1weekMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 3, 7),
    _CacheBwidthSpent1weekMean_Type()
)
cacheBwidthSpent1weekMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSpent1weekMean.setStatus("current")
_CacheBwidthSpentLifePeak_Type = Integer32
_CacheBwidthSpentLifePeak_Object = MibScalar
cacheBwidthSpentLifePeak = _CacheBwidthSpentLifePeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 3, 8),
    _CacheBwidthSpentLifePeak_Type()
)
cacheBwidthSpentLifePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSpentLifePeak.setStatus("current")
_CacheBwidthSpentLifeMean_Type = Integer32
_CacheBwidthSpentLifeMean_Object = MibScalar
cacheBwidthSpentLifeMean = _CacheBwidthSpentLifeMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 3, 9),
    _CacheBwidthSpentLifeMean_Type()
)
cacheBwidthSpentLifeMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthSpentLifeMean.setStatus("current")
_ProxyRecentBandWTotPerf_ObjectIdentity = ObjectIdentity
proxyRecentBandWTotPerf = _ProxyRecentBandWTotPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 4)
)
_CacheBwidthTotalNow_Type = Integer32
_CacheBwidthTotalNow_Object = MibScalar
cacheBwidthTotalNow = _CacheBwidthTotalNow_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 4, 1),
    _CacheBwidthTotalNow_Type()
)
cacheBwidthTotalNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthTotalNow.setStatus("current")
_CacheBwidthTotal1hrPeak_Type = Integer32
_CacheBwidthTotal1hrPeak_Object = MibScalar
cacheBwidthTotal1hrPeak = _CacheBwidthTotal1hrPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 4, 2),
    _CacheBwidthTotal1hrPeak_Type()
)
cacheBwidthTotal1hrPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthTotal1hrPeak.setStatus("current")
_CacheBwidthTotal1hrMean_Type = Integer32
_CacheBwidthTotal1hrMean_Object = MibScalar
cacheBwidthTotal1hrMean = _CacheBwidthTotal1hrMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 4, 3),
    _CacheBwidthTotal1hrMean_Type()
)
cacheBwidthTotal1hrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthTotal1hrMean.setStatus("current")
_CacheBwidthTotal1dayPeak_Type = Integer32
_CacheBwidthTotal1dayPeak_Object = MibScalar
cacheBwidthTotal1dayPeak = _CacheBwidthTotal1dayPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 4, 4),
    _CacheBwidthTotal1dayPeak_Type()
)
cacheBwidthTotal1dayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthTotal1dayPeak.setStatus("current")
_CacheBwidthTotal1dayMean_Type = Integer32
_CacheBwidthTotal1dayMean_Object = MibScalar
cacheBwidthTotal1dayMean = _CacheBwidthTotal1dayMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 4, 5),
    _CacheBwidthTotal1dayMean_Type()
)
cacheBwidthTotal1dayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthTotal1dayMean.setStatus("current")
_CacheBwidthTotal1weekPeak_Type = Integer32
_CacheBwidthTotal1weekPeak_Object = MibScalar
cacheBwidthTotal1weekPeak = _CacheBwidthTotal1weekPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 4, 6),
    _CacheBwidthTotal1weekPeak_Type()
)
cacheBwidthTotal1weekPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthTotal1weekPeak.setStatus("current")
_CacheBwidthTotal1weekMean_Type = Integer32
_CacheBwidthTotal1weekMean_Object = MibScalar
cacheBwidthTotal1weekMean = _CacheBwidthTotal1weekMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 4, 7),
    _CacheBwidthTotal1weekMean_Type()
)
cacheBwidthTotal1weekMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthTotal1weekMean.setStatus("current")
_CacheBwidthTotalLifePeak_Type = Integer32
_CacheBwidthTotalLifePeak_Object = MibScalar
cacheBwidthTotalLifePeak = _CacheBwidthTotalLifePeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 4, 8),
    _CacheBwidthTotalLifePeak_Type()
)
cacheBwidthTotalLifePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthTotalLifePeak.setStatus("current")
_CacheBwidthTotalLifeMean_Type = Integer32
_CacheBwidthTotalLifeMean_Object = MibScalar
cacheBwidthTotalLifeMean = _CacheBwidthTotalLifeMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 4, 9),
    _CacheBwidthTotalLifeMean_Type()
)
cacheBwidthTotalLifeMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBwidthTotalLifeMean.setStatus("current")
_ProxyRecentHitsPerf_ObjectIdentity = ObjectIdentity
proxyRecentHitsPerf = _ProxyRecentHitsPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 5)
)
_CacheHitsNow_Type = Integer32
_CacheHitsNow_Object = MibScalar
cacheHitsNow = _CacheHitsNow_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 5, 1),
    _CacheHitsNow_Type()
)
cacheHitsNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHitsNow.setStatus("current")
_CacheHits1hrPeak_Type = Integer32
_CacheHits1hrPeak_Object = MibScalar
cacheHits1hrPeak = _CacheHits1hrPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 5, 2),
    _CacheHits1hrPeak_Type()
)
cacheHits1hrPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHits1hrPeak.setStatus("current")
_CacheHits1hrMean_Type = Integer32
_CacheHits1hrMean_Object = MibScalar
cacheHits1hrMean = _CacheHits1hrMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 5, 3),
    _CacheHits1hrMean_Type()
)
cacheHits1hrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHits1hrMean.setStatus("current")
_CacheHits1dayPeak_Type = Integer32
_CacheHits1dayPeak_Object = MibScalar
cacheHits1dayPeak = _CacheHits1dayPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 5, 4),
    _CacheHits1dayPeak_Type()
)
cacheHits1dayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHits1dayPeak.setStatus("current")
_CacheHits1dayMean_Type = Integer32
_CacheHits1dayMean_Object = MibScalar
cacheHits1dayMean = _CacheHits1dayMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 5, 5),
    _CacheHits1dayMean_Type()
)
cacheHits1dayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHits1dayMean.setStatus("current")
_CacheHits1weekPeak_Type = Integer32
_CacheHits1weekPeak_Object = MibScalar
cacheHits1weekPeak = _CacheHits1weekPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 5, 6),
    _CacheHits1weekPeak_Type()
)
cacheHits1weekPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHits1weekPeak.setStatus("current")
_CacheHits1weekMean_Type = Integer32
_CacheHits1weekMean_Object = MibScalar
cacheHits1weekMean = _CacheHits1weekMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 5, 7),
    _CacheHits1weekMean_Type()
)
cacheHits1weekMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHits1weekMean.setStatus("current")
_CacheHitsLifePeak_Type = Integer32
_CacheHitsLifePeak_Object = MibScalar
cacheHitsLifePeak = _CacheHitsLifePeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 5, 8),
    _CacheHitsLifePeak_Type()
)
cacheHitsLifePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHitsLifePeak.setStatus("current")
_CacheHitsLifeMean_Type = Integer32
_CacheHitsLifeMean_Object = MibScalar
cacheHitsLifeMean = _CacheHitsLifeMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 5, 9),
    _CacheHitsLifeMean_Type()
)
cacheHitsLifeMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHitsLifeMean.setStatus("current")
_ProxyRecentMissesPerf_ObjectIdentity = ObjectIdentity
proxyRecentMissesPerf = _ProxyRecentMissesPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 6)
)
_CacheMissesNow_Type = Integer32
_CacheMissesNow_Object = MibScalar
cacheMissesNow = _CacheMissesNow_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 6, 1),
    _CacheMissesNow_Type()
)
cacheMissesNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissesNow.setStatus("current")
_CacheMisses1hrPeak_Type = Integer32
_CacheMisses1hrPeak_Object = MibScalar
cacheMisses1hrPeak = _CacheMisses1hrPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 6, 2),
    _CacheMisses1hrPeak_Type()
)
cacheMisses1hrPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMisses1hrPeak.setStatus("current")
_CacheMisses1hrMean_Type = Integer32
_CacheMisses1hrMean_Object = MibScalar
cacheMisses1hrMean = _CacheMisses1hrMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 6, 3),
    _CacheMisses1hrMean_Type()
)
cacheMisses1hrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMisses1hrMean.setStatus("current")
_CacheMisses1dayPeak_Type = Integer32
_CacheMisses1dayPeak_Object = MibScalar
cacheMisses1dayPeak = _CacheMisses1dayPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 6, 4),
    _CacheMisses1dayPeak_Type()
)
cacheMisses1dayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMisses1dayPeak.setStatus("current")
_CacheMisses1dayMean_Type = Integer32
_CacheMisses1dayMean_Object = MibScalar
cacheMisses1dayMean = _CacheMisses1dayMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 6, 5),
    _CacheMisses1dayMean_Type()
)
cacheMisses1dayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMisses1dayMean.setStatus("current")
_CacheMisses1weekPeak_Type = Integer32
_CacheMisses1weekPeak_Object = MibScalar
cacheMisses1weekPeak = _CacheMisses1weekPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 6, 6),
    _CacheMisses1weekPeak_Type()
)
cacheMisses1weekPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMisses1weekPeak.setStatus("current")
_CacheMisses1weekMean_Type = Integer32
_CacheMisses1weekMean_Object = MibScalar
cacheMisses1weekMean = _CacheMisses1weekMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 6, 7),
    _CacheMisses1weekMean_Type()
)
cacheMisses1weekMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMisses1weekMean.setStatus("current")
_CacheMissesLifePeak_Type = Integer32
_CacheMissesLifePeak_Object = MibScalar
cacheMissesLifePeak = _CacheMissesLifePeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 6, 8),
    _CacheMissesLifePeak_Type()
)
cacheMissesLifePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissesLifePeak.setStatus("current")
_CacheMissesLifeMean_Type = Integer32
_CacheMissesLifeMean_Object = MibScalar
cacheMissesLifeMean = _CacheMissesLifeMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 6, 9),
    _CacheMissesLifeMean_Type()
)
cacheMissesLifeMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissesLifeMean.setStatus("current")
_ProxyRecentHitRespTimePerf_ObjectIdentity = ObjectIdentity
proxyRecentHitRespTimePerf = _ProxyRecentHitRespTimePerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 7)
)
_CacheHitRespTimeNow_Type = Integer32
_CacheHitRespTimeNow_Object = MibScalar
cacheHitRespTimeNow = _CacheHitRespTimeNow_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 7, 1),
    _CacheHitRespTimeNow_Type()
)
cacheHitRespTimeNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHitRespTimeNow.setStatus("current")
_CacheHitRespTime1hrPeak_Type = Integer32
_CacheHitRespTime1hrPeak_Object = MibScalar
cacheHitRespTime1hrPeak = _CacheHitRespTime1hrPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 7, 2),
    _CacheHitRespTime1hrPeak_Type()
)
cacheHitRespTime1hrPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHitRespTime1hrPeak.setStatus("current")
_CacheHitRespTime1hrMean_Type = Integer32
_CacheHitRespTime1hrMean_Object = MibScalar
cacheHitRespTime1hrMean = _CacheHitRespTime1hrMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 7, 3),
    _CacheHitRespTime1hrMean_Type()
)
cacheHitRespTime1hrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHitRespTime1hrMean.setStatus("current")
_CacheHitRespTime1dayPeak_Type = Integer32
_CacheHitRespTime1dayPeak_Object = MibScalar
cacheHitRespTime1dayPeak = _CacheHitRespTime1dayPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 7, 4),
    _CacheHitRespTime1dayPeak_Type()
)
cacheHitRespTime1dayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHitRespTime1dayPeak.setStatus("current")
_CacheHitRespTime1dayMean_Type = Integer32
_CacheHitRespTime1dayMean_Object = MibScalar
cacheHitRespTime1dayMean = _CacheHitRespTime1dayMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 7, 5),
    _CacheHitRespTime1dayMean_Type()
)
cacheHitRespTime1dayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHitRespTime1dayMean.setStatus("current")
_CacheHitRespTime1weekPeak_Type = Integer32
_CacheHitRespTime1weekPeak_Object = MibScalar
cacheHitRespTime1weekPeak = _CacheHitRespTime1weekPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 7, 6),
    _CacheHitRespTime1weekPeak_Type()
)
cacheHitRespTime1weekPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHitRespTime1weekPeak.setStatus("current")
_CacheHitRespTime1weekMean_Type = Integer32
_CacheHitRespTime1weekMean_Object = MibScalar
cacheHitRespTime1weekMean = _CacheHitRespTime1weekMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 7, 7),
    _CacheHitRespTime1weekMean_Type()
)
cacheHitRespTime1weekMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHitRespTime1weekMean.setStatus("current")
_CacheHitRespTimeLifePeak_Type = Integer32
_CacheHitRespTimeLifePeak_Object = MibScalar
cacheHitRespTimeLifePeak = _CacheHitRespTimeLifePeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 7, 8),
    _CacheHitRespTimeLifePeak_Type()
)
cacheHitRespTimeLifePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHitRespTimeLifePeak.setStatus("current")
_CacheHitRespTimeLifeMean_Type = Integer32
_CacheHitRespTimeLifeMean_Object = MibScalar
cacheHitRespTimeLifeMean = _CacheHitRespTimeLifeMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 7, 9),
    _CacheHitRespTimeLifeMean_Type()
)
cacheHitRespTimeLifeMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHitRespTimeLifeMean.setStatus("current")
_ProxyRecentMissRespTimePerf_ObjectIdentity = ObjectIdentity
proxyRecentMissRespTimePerf = _ProxyRecentMissRespTimePerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 8)
)
_CacheMissRespTimeNow_Type = Integer32
_CacheMissRespTimeNow_Object = MibScalar
cacheMissRespTimeNow = _CacheMissRespTimeNow_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 8, 1),
    _CacheMissRespTimeNow_Type()
)
cacheMissRespTimeNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissRespTimeNow.setStatus("current")
_CacheMissRespTime1hrPeak_Type = Integer32
_CacheMissRespTime1hrPeak_Object = MibScalar
cacheMissRespTime1hrPeak = _CacheMissRespTime1hrPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 8, 2),
    _CacheMissRespTime1hrPeak_Type()
)
cacheMissRespTime1hrPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissRespTime1hrPeak.setStatus("current")
_CacheMissRespTime1hrMean_Type = Integer32
_CacheMissRespTime1hrMean_Object = MibScalar
cacheMissRespTime1hrMean = _CacheMissRespTime1hrMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 8, 3),
    _CacheMissRespTime1hrMean_Type()
)
cacheMissRespTime1hrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissRespTime1hrMean.setStatus("current")
_CacheMissRespTime1dayPeak_Type = Integer32
_CacheMissRespTime1dayPeak_Object = MibScalar
cacheMissRespTime1dayPeak = _CacheMissRespTime1dayPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 8, 4),
    _CacheMissRespTime1dayPeak_Type()
)
cacheMissRespTime1dayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissRespTime1dayPeak.setStatus("current")
_CacheMissRespTime1dayMean_Type = Integer32
_CacheMissRespTime1dayMean_Object = MibScalar
cacheMissRespTime1dayMean = _CacheMissRespTime1dayMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 8, 5),
    _CacheMissRespTime1dayMean_Type()
)
cacheMissRespTime1dayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissRespTime1dayMean.setStatus("current")
_CacheMissRespTime1weekPeak_Type = Integer32
_CacheMissRespTime1weekPeak_Object = MibScalar
cacheMissRespTime1weekPeak = _CacheMissRespTime1weekPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 8, 6),
    _CacheMissRespTime1weekPeak_Type()
)
cacheMissRespTime1weekPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissRespTime1weekPeak.setStatus("current")
_CacheMissRespTime1weekMean_Type = Integer32
_CacheMissRespTime1weekMean_Object = MibScalar
cacheMissRespTime1weekMean = _CacheMissRespTime1weekMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 8, 7),
    _CacheMissRespTime1weekMean_Type()
)
cacheMissRespTime1weekMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissRespTime1weekMean.setStatus("current")
_CacheMissRespTimeLifePeak_Type = Integer32
_CacheMissRespTimeLifePeak_Object = MibScalar
cacheMissRespTimeLifePeak = _CacheMissRespTimeLifePeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 8, 8),
    _CacheMissRespTimeLifePeak_Type()
)
cacheMissRespTimeLifePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissRespTimeLifePeak.setStatus("current")
_CacheMissRespTimeLifeMean_Type = Integer32
_CacheMissRespTimeLifeMean_Object = MibScalar
cacheMissRespTimeLifeMean = _CacheMissRespTimeLifeMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 8, 9),
    _CacheMissRespTimeLifeMean_Type()
)
cacheMissRespTimeLifeMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissRespTimeLifeMean.setStatus("current")
_ProxyRecentTotalRespTimePerf_ObjectIdentity = ObjectIdentity
proxyRecentTotalRespTimePerf = _ProxyRecentTotalRespTimePerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 9)
)
_CacheTotalRespTimeNow_Type = Integer32
_CacheTotalRespTimeNow_Object = MibScalar
cacheTotalRespTimeNow = _CacheTotalRespTimeNow_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 9, 1),
    _CacheTotalRespTimeNow_Type()
)
cacheTotalRespTimeNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalRespTimeNow.setStatus("current")
_CacheTotalRespTime1hrPeak_Type = Integer32
_CacheTotalRespTime1hrPeak_Object = MibScalar
cacheTotalRespTime1hrPeak = _CacheTotalRespTime1hrPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 9, 2),
    _CacheTotalRespTime1hrPeak_Type()
)
cacheTotalRespTime1hrPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalRespTime1hrPeak.setStatus("current")
_CacheTotalRespTime1hrMean_Type = Integer32
_CacheTotalRespTime1hrMean_Object = MibScalar
cacheTotalRespTime1hrMean = _CacheTotalRespTime1hrMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 9, 3),
    _CacheTotalRespTime1hrMean_Type()
)
cacheTotalRespTime1hrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalRespTime1hrMean.setStatus("current")
_CacheTotalRespTime1dayPeak_Type = Integer32
_CacheTotalRespTime1dayPeak_Object = MibScalar
cacheTotalRespTime1dayPeak = _CacheTotalRespTime1dayPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 9, 4),
    _CacheTotalRespTime1dayPeak_Type()
)
cacheTotalRespTime1dayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalRespTime1dayPeak.setStatus("current")
_CacheTotalRespTime1dayMean_Type = Integer32
_CacheTotalRespTime1dayMean_Object = MibScalar
cacheTotalRespTime1dayMean = _CacheTotalRespTime1dayMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 9, 5),
    _CacheTotalRespTime1dayMean_Type()
)
cacheTotalRespTime1dayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalRespTime1dayMean.setStatus("current")
_CacheTotalRespTime1weekPeak_Type = Integer32
_CacheTotalRespTime1weekPeak_Object = MibScalar
cacheTotalRespTime1weekPeak = _CacheTotalRespTime1weekPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 9, 6),
    _CacheTotalRespTime1weekPeak_Type()
)
cacheTotalRespTime1weekPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalRespTime1weekPeak.setStatus("current")
_CacheTotalRespTime1weekMean_Type = Integer32
_CacheTotalRespTime1weekMean_Object = MibScalar
cacheTotalRespTime1weekMean = _CacheTotalRespTime1weekMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 9, 7),
    _CacheTotalRespTime1weekMean_Type()
)
cacheTotalRespTime1weekMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalRespTime1weekMean.setStatus("current")
_CacheTotalRespTimeLifePeak_Type = Integer32
_CacheTotalRespTimeLifePeak_Object = MibScalar
cacheTotalRespTimeLifePeak = _CacheTotalRespTimeLifePeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 9, 8),
    _CacheTotalRespTimeLifePeak_Type()
)
cacheTotalRespTimeLifePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalRespTimeLifePeak.setStatus("current")
_CacheTotalRespTimeLifeMean_Type = Integer32
_CacheTotalRespTimeLifeMean_Object = MibScalar
cacheTotalRespTimeLifeMean = _CacheTotalRespTimeLifeMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 9, 9),
    _CacheTotalRespTimeLifeMean_Type()
)
cacheTotalRespTimeLifeMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotalRespTimeLifeMean.setStatus("current")
_ProxyRecentErrsPerf_ObjectIdentity = ObjectIdentity
proxyRecentErrsPerf = _ProxyRecentErrsPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 10)
)
_CacheErrsNow_Type = Integer32
_CacheErrsNow_Object = MibScalar
cacheErrsNow = _CacheErrsNow_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 10, 1),
    _CacheErrsNow_Type()
)
cacheErrsNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrsNow.setStatus("current")
_CacheErrs1hrPeak_Type = Integer32
_CacheErrs1hrPeak_Object = MibScalar
cacheErrs1hrPeak = _CacheErrs1hrPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 10, 2),
    _CacheErrs1hrPeak_Type()
)
cacheErrs1hrPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrs1hrPeak.setStatus("current")
_CacheErrs1hrMean_Type = Integer32
_CacheErrs1hrMean_Object = MibScalar
cacheErrs1hrMean = _CacheErrs1hrMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 10, 3),
    _CacheErrs1hrMean_Type()
)
cacheErrs1hrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrs1hrMean.setStatus("current")
_CacheErrs1dayPeak_Type = Integer32
_CacheErrs1dayPeak_Object = MibScalar
cacheErrs1dayPeak = _CacheErrs1dayPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 10, 4),
    _CacheErrs1dayPeak_Type()
)
cacheErrs1dayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrs1dayPeak.setStatus("current")
_CacheErrs1dayMean_Type = Integer32
_CacheErrs1dayMean_Object = MibScalar
cacheErrs1dayMean = _CacheErrs1dayMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 10, 5),
    _CacheErrs1dayMean_Type()
)
cacheErrs1dayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrs1dayMean.setStatus("current")
_CacheErrs1weekPeak_Type = Integer32
_CacheErrs1weekPeak_Object = MibScalar
cacheErrs1weekPeak = _CacheErrs1weekPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 10, 6),
    _CacheErrs1weekPeak_Type()
)
cacheErrs1weekPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrs1weekPeak.setStatus("current")
_CacheErrs1weekMean_Type = Integer32
_CacheErrs1weekMean_Object = MibScalar
cacheErrs1weekMean = _CacheErrs1weekMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 10, 7),
    _CacheErrs1weekMean_Type()
)
cacheErrs1weekMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrs1weekMean.setStatus("current")
_CacheErrsLifePeak_Type = Integer32
_CacheErrsLifePeak_Object = MibScalar
cacheErrsLifePeak = _CacheErrsLifePeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 10, 8),
    _CacheErrsLifePeak_Type()
)
cacheErrsLifePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrsLifePeak.setStatus("current")
_CacheErrsLifeMean_Type = Integer32
_CacheErrsLifeMean_Object = MibScalar
cacheErrsLifeMean = _CacheErrsLifeMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 10, 9),
    _CacheErrsLifeMean_Type()
)
cacheErrsLifeMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrsLifeMean.setStatus("current")
_ProxyRecentDeniedPerf_ObjectIdentity = ObjectIdentity
proxyRecentDeniedPerf = _ProxyRecentDeniedPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 11)
)
_CacheDeniedNow_Type = Integer32
_CacheDeniedNow_Object = MibScalar
cacheDeniedNow = _CacheDeniedNow_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 11, 1),
    _CacheDeniedNow_Type()
)
cacheDeniedNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeniedNow.setStatus("current")
_CacheDenied1hrPeak_Type = Integer32
_CacheDenied1hrPeak_Object = MibScalar
cacheDenied1hrPeak = _CacheDenied1hrPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 11, 2),
    _CacheDenied1hrPeak_Type()
)
cacheDenied1hrPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDenied1hrPeak.setStatus("current")
_CacheDenied1hrMean_Type = Integer32
_CacheDenied1hrMean_Object = MibScalar
cacheDenied1hrMean = _CacheDenied1hrMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 11, 3),
    _CacheDenied1hrMean_Type()
)
cacheDenied1hrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDenied1hrMean.setStatus("current")
_CacheDenied1dayPeak_Type = Integer32
_CacheDenied1dayPeak_Object = MibScalar
cacheDenied1dayPeak = _CacheDenied1dayPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 11, 4),
    _CacheDenied1dayPeak_Type()
)
cacheDenied1dayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDenied1dayPeak.setStatus("current")
_CacheDenied1dayMean_Type = Integer32
_CacheDenied1dayMean_Object = MibScalar
cacheDenied1dayMean = _CacheDenied1dayMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 11, 5),
    _CacheDenied1dayMean_Type()
)
cacheDenied1dayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDenied1dayMean.setStatus("current")
_CacheDenied1weekPeak_Type = Integer32
_CacheDenied1weekPeak_Object = MibScalar
cacheDenied1weekPeak = _CacheDenied1weekPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 11, 6),
    _CacheDenied1weekPeak_Type()
)
cacheDenied1weekPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDenied1weekPeak.setStatus("current")
_CacheDenied1weekMean_Type = Integer32
_CacheDenied1weekMean_Object = MibScalar
cacheDenied1weekMean = _CacheDenied1weekMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 11, 7),
    _CacheDenied1weekMean_Type()
)
cacheDenied1weekMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDenied1weekMean.setStatus("current")
_CacheDeniedLifePeak_Type = Integer32
_CacheDeniedLifePeak_Object = MibScalar
cacheDeniedLifePeak = _CacheDeniedLifePeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 11, 8),
    _CacheDeniedLifePeak_Type()
)
cacheDeniedLifePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeniedLifePeak.setStatus("current")
_CacheDeniedLifeMean_Type = Integer32
_CacheDeniedLifeMean_Object = MibScalar
cacheDeniedLifeMean = _CacheDeniedLifeMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 11, 9),
    _CacheDeniedLifeMean_Type()
)
cacheDeniedLifeMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeniedLifeMean.setStatus("current")
_ProxyRecentErrRespTimePerf_ObjectIdentity = ObjectIdentity
proxyRecentErrRespTimePerf = _ProxyRecentErrRespTimePerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 12)
)
_CacheErrRespTimeNow_Type = Integer32
_CacheErrRespTimeNow_Object = MibScalar
cacheErrRespTimeNow = _CacheErrRespTimeNow_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 12, 1),
    _CacheErrRespTimeNow_Type()
)
cacheErrRespTimeNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrRespTimeNow.setStatus("current")
_CacheErrRespTime1hrPeak_Type = Integer32
_CacheErrRespTime1hrPeak_Object = MibScalar
cacheErrRespTime1hrPeak = _CacheErrRespTime1hrPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 12, 2),
    _CacheErrRespTime1hrPeak_Type()
)
cacheErrRespTime1hrPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrRespTime1hrPeak.setStatus("current")
_CacheErrRespTime1hrMean_Type = Integer32
_CacheErrRespTime1hrMean_Object = MibScalar
cacheErrRespTime1hrMean = _CacheErrRespTime1hrMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 12, 3),
    _CacheErrRespTime1hrMean_Type()
)
cacheErrRespTime1hrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrRespTime1hrMean.setStatus("current")
_CacheErrRespTime1dayPeak_Type = Integer32
_CacheErrRespTime1dayPeak_Object = MibScalar
cacheErrRespTime1dayPeak = _CacheErrRespTime1dayPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 12, 4),
    _CacheErrRespTime1dayPeak_Type()
)
cacheErrRespTime1dayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrRespTime1dayPeak.setStatus("current")
_CacheErrRespTime1dayMean_Type = Integer32
_CacheErrRespTime1dayMean_Object = MibScalar
cacheErrRespTime1dayMean = _CacheErrRespTime1dayMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 12, 5),
    _CacheErrRespTime1dayMean_Type()
)
cacheErrRespTime1dayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrRespTime1dayMean.setStatus("current")
_CacheErrRespTime1weekPeak_Type = Integer32
_CacheErrRespTime1weekPeak_Object = MibScalar
cacheErrRespTime1weekPeak = _CacheErrRespTime1weekPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 12, 6),
    _CacheErrRespTime1weekPeak_Type()
)
cacheErrRespTime1weekPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrRespTime1weekPeak.setStatus("current")
_CacheErrRespTime1weekMean_Type = Integer32
_CacheErrRespTime1weekMean_Object = MibScalar
cacheErrRespTime1weekMean = _CacheErrRespTime1weekMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 12, 7),
    _CacheErrRespTime1weekMean_Type()
)
cacheErrRespTime1weekMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrRespTime1weekMean.setStatus("current")
_CacheErrRespTimeLifePeak_Type = Integer32
_CacheErrRespTimeLifePeak_Object = MibScalar
cacheErrRespTimeLifePeak = _CacheErrRespTimeLifePeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 12, 8),
    _CacheErrRespTimeLifePeak_Type()
)
cacheErrRespTimeLifePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrRespTimeLifePeak.setStatus("current")
_CacheErrRespTimeLifeMean_Type = Integer32
_CacheErrRespTimeLifeMean_Object = MibScalar
cacheErrRespTimeLifeMean = _CacheErrRespTimeLifeMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 12, 9),
    _CacheErrRespTimeLifeMean_Type()
)
cacheErrRespTimeLifeMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheErrRespTimeLifeMean.setStatus("current")
_ProxyRecentDeniedRespTimePerf_ObjectIdentity = ObjectIdentity
proxyRecentDeniedRespTimePerf = _ProxyRecentDeniedRespTimePerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 13)
)
_CacheDeniedRespTimeNow_Type = Integer32
_CacheDeniedRespTimeNow_Object = MibScalar
cacheDeniedRespTimeNow = _CacheDeniedRespTimeNow_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 13, 1),
    _CacheDeniedRespTimeNow_Type()
)
cacheDeniedRespTimeNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeniedRespTimeNow.setStatus("current")
_CacheDeniedRespTime1hrPeak_Type = Integer32
_CacheDeniedRespTime1hrPeak_Object = MibScalar
cacheDeniedRespTime1hrPeak = _CacheDeniedRespTime1hrPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 13, 2),
    _CacheDeniedRespTime1hrPeak_Type()
)
cacheDeniedRespTime1hrPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeniedRespTime1hrPeak.setStatus("current")
_CacheDeniedRespTime1hrMean_Type = Integer32
_CacheDeniedRespTime1hrMean_Object = MibScalar
cacheDeniedRespTime1hrMean = _CacheDeniedRespTime1hrMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 13, 3),
    _CacheDeniedRespTime1hrMean_Type()
)
cacheDeniedRespTime1hrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeniedRespTime1hrMean.setStatus("current")
_CacheDeniedRespTime1dayPeak_Type = Integer32
_CacheDeniedRespTime1dayPeak_Object = MibScalar
cacheDeniedRespTime1dayPeak = _CacheDeniedRespTime1dayPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 13, 4),
    _CacheDeniedRespTime1dayPeak_Type()
)
cacheDeniedRespTime1dayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeniedRespTime1dayPeak.setStatus("current")
_CacheDeniedRespTime1dayMean_Type = Integer32
_CacheDeniedRespTime1dayMean_Object = MibScalar
cacheDeniedRespTime1dayMean = _CacheDeniedRespTime1dayMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 13, 5),
    _CacheDeniedRespTime1dayMean_Type()
)
cacheDeniedRespTime1dayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeniedRespTime1dayMean.setStatus("current")
_CacheDeniedRespTime1weekPeak_Type = Integer32
_CacheDeniedRespTime1weekPeak_Object = MibScalar
cacheDeniedRespTime1weekPeak = _CacheDeniedRespTime1weekPeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 13, 6),
    _CacheDeniedRespTime1weekPeak_Type()
)
cacheDeniedRespTime1weekPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeniedRespTime1weekPeak.setStatus("current")
_CacheDeniedRespTime1weekMean_Type = Integer32
_CacheDeniedRespTime1weekMean_Object = MibScalar
cacheDeniedRespTime1weekMean = _CacheDeniedRespTime1weekMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 13, 7),
    _CacheDeniedRespTime1weekMean_Type()
)
cacheDeniedRespTime1weekMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeniedRespTime1weekMean.setStatus("current")
_CacheDeniedRespTimeLifePeak_Type = Integer32
_CacheDeniedRespTimeLifePeak_Object = MibScalar
cacheDeniedRespTimeLifePeak = _CacheDeniedRespTimeLifePeak_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 13, 8),
    _CacheDeniedRespTimeLifePeak_Type()
)
cacheDeniedRespTimeLifePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeniedRespTimeLifePeak.setStatus("current")
_CacheDeniedRespTimeLifeMean_Type = Integer32
_CacheDeniedRespTimeLifeMean_Object = MibScalar
cacheDeniedRespTimeLifeMean = _CacheDeniedRespTimeLifeMean_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 3, 7, 13, 9),
    _CacheDeniedRespTimeLifeMean_Type()
)
cacheDeniedRespTimeLifeMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDeniedRespTimeLifeMean.setStatus("current")
_ProxyHardware_ObjectIdentity = ObjectIdentity
proxyHardware = _ProxyHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 4)
)
_ProxyHardwareDisk_ObjectIdentity = ObjectIdentity
proxyHardwareDisk = _ProxyHardwareDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 4, 1)
)
_HardwareDiskStatTable_Object = MibTable
hardwareDiskStatTable = _HardwareDiskStatTable_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hardwareDiskStatTable.setStatus("current")
_DiskStatEntry_Object = MibTableRow
diskStatEntry = _DiskStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 4, 1, 1, 1)
)
diskStatEntry.setIndexNames(
    (0, "ASYNCOSWEBSECURITYAPPLIANCE-MIB", "diskStatEntryNumber"),
)
if mibBuilder.loadTexts:
    diskStatEntry.setStatus("current")


class _DiskStatEntryNumber_Type(Integer32):
    """Custom type diskStatEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_DiskStatEntryNumber_Type.__name__ = "Integer32"
_DiskStatEntryNumber_Object = MibTableColumn
diskStatEntryNumber = _DiskStatEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 4, 1, 1, 1, 1),
    _DiskStatEntryNumber_Type()
)
diskStatEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatEntryNumber.setStatus("current")
_DiskStatWrites_Type = Integer32
_DiskStatWrites_Object = MibTableColumn
diskStatWrites = _DiskStatWrites_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 4, 1, 1, 1, 2),
    _DiskStatWrites_Type()
)
diskStatWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatWrites.setStatus("current")
_DiskStatWriteErrs_Type = Integer32
_DiskStatWriteErrs_Object = MibTableColumn
diskStatWriteErrs = _DiskStatWriteErrs_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 4, 1, 1, 1, 3),
    _DiskStatWriteErrs_Type()
)
diskStatWriteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatWriteErrs.setStatus("current")
_DiskStatReads_Type = Integer32
_DiskStatReads_Object = MibTableColumn
diskStatReads = _DiskStatReads_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 4, 1, 1, 1, 4),
    _DiskStatReads_Type()
)
diskStatReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatReads.setStatus("current")
_DiskStatReadErrs_Type = Integer32
_DiskStatReadErrs_Object = MibTableColumn
diskStatReadErrs = _DiskStatReadErrs_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 4, 1, 1, 1, 5),
    _DiskStatReadErrs_Type()
)
diskStatReadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatReadErrs.setStatus("current")
_ProxyTraps_ObjectIdentity = ObjectIdentity
proxyTraps = _ProxyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 5)
)

# Managed Objects groups


# Notification objects

upstreamProxyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15497, 1, 2, 5, 1)
)
upstreamProxyFailure.setObjects(
    ("ASYNCOS-MAIL-MIB", "connectionURL")
)
if mibBuilder.loadTexts:
    upstreamProxyFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASYNCOSWEBSECURITYAPPLIANCE-MIB",
    **{"asyncOSWebSecurityAppliance": asyncOSWebSecurityAppliance,
       "proxySystem": proxySystem,
       "cacheUptime": cacheUptime,
       "cacheMemory": cacheMemory,
       "cacheSysStorage": cacheSysStorage,
       "proxyConfig": proxyConfig,
       "cacheAdmin": cacheAdmin,
       "cacheSoftware": cacheSoftware,
       "cacheVersion": cacheVersion,
       "licenseExpiration": licenseExpiration,
       "proxyPerf": proxyPerf,
       "proxySysPerf": proxySysPerf,
       "cacheCpuTime": cacheCpuTime,
       "cacheCpuUsage": cacheCpuUsage,
       "cacheMaxResSize": cacheMaxResSize,
       "cacheUsedStoragePct": cacheUsedStoragePct,
       "cacheBusyCPUPct": cacheBusyCPUPct,
       "cacheMemoryBufferUsagePct": cacheMemoryBufferUsagePct,
       "proxyClientSidePerf": proxyClientSidePerf,
       "cacheClientSizeHistTable": cacheClientSizeHistTable,
       "cacheClientSizeHistEntry": cacheClientSizeHistEntry,
       "cacheClientSizeHistBinNumber": cacheClientSizeHistBinNumber,
       "cacheClientReqSize": cacheClientReqSize,
       "cacheClientRequests": cacheClientRequests,
       "cacheClientHits": cacheClientHits,
       "cacheClientErrors": cacheClientErrors,
       "cacheClientInKb": cacheClientInKb,
       "cacheClientOutKb": cacheClientOutKb,
       "cacheClientIdleConns": cacheClientIdleConns,
       "cacheClientTotalConns": cacheClientTotalConns,
       "cacheClientMaxConns": cacheClientMaxConns,
       "cacheClientAccepts": cacheClientAccepts,
       "cacheClientICPRequests": cacheClientICPRequests,
       "cacheClientICPHits": cacheClientICPHits,
       "cacheClientICPMisses": cacheClientICPMisses,
       "cacheClientICPErrors": cacheClientICPErrors,
       "cacheClientICPDenials": cacheClientICPDenials,
       "cacheClientReqMisses": cacheClientReqMisses,
       "cacheClientReqDenials": cacheClientReqDenials,
       "proxyServerSidePerf": proxyServerSidePerf,
       "cacheServerSizeHistTable": cacheServerSizeHistTable,
       "cacheServerSizeHistEntry": cacheServerSizeHistEntry,
       "cacheServerSizeHistBinNumber": cacheServerSizeHistBinNumber,
       "cacheServerReplySize": cacheServerReplySize,
       "cacheServerRequests": cacheServerRequests,
       "cacheServerSockets": cacheServerSockets,
       "cacheServerErrors": cacheServerErrors,
       "cacheServerInKb": cacheServerInKb,
       "cacheServerOutKb": cacheServerOutKb,
       "cacheServerIdleConns": cacheServerIdleConns,
       "cacheServerTotalConns": cacheServerTotalConns,
       "cacheServerCloseIdleConns": cacheServerCloseIdleConns,
       "cacheServerLimitIdleConns": cacheServerLimitIdleConns,
       "cacheServerConnsThresh": cacheServerConnsThresh,
       "cacheServerPersisConnsRetries": cacheServerPersisConnsRetries,
       "cacheServerRegConnsRetries": cacheServerRegConnsRetries,
       "cacheServerRWErrorRetries": cacheServerRWErrorRetries,
       "cacheServerEarlyCloseRetries": cacheServerEarlyCloseRetries,
       "cacheServerICPRequests": cacheServerICPRequests,
       "cacheServerICPHits": cacheServerICPHits,
       "cacheServerICPMisses": cacheServerICPMisses,
       "cacheServerICPErrors": cacheServerICPErrors,
       "cacheServerICPDenials": cacheServerICPDenials,
       "proxyCachePerf": proxyCachePerf,
       "cacheCacheSizeHistTable": cacheCacheSizeHistTable,
       "cacheCacheSizeHistEntry": cacheCacheSizeHistEntry,
       "cacheSizeHistBinNumber": cacheSizeHistBinNumber,
       "cacheCacheActiveObjs": cacheCacheActiveObjs,
       "cacheCacheAllObjs": cacheCacheAllObjs,
       "cacheCacheLiveCachedObjs": cacheCacheLiveCachedObjs,
       "cacheCacheLiveCachedObjSizes": cacheCacheLiveCachedObjSizes,
       "cacheCacheTotalCachedObjs": cacheCacheTotalCachedObjs,
       "cacheCacheTotalCachedObjSizes": cacheCacheTotalCachedObjSizes,
       "proxyMedianSvcTime": proxyMedianSvcTime,
       "cacheMedianSvcTable": cacheMedianSvcTable,
       "cacheMedianSvcEntry": cacheMedianSvcEntry,
       "cacheMedianTime": cacheMedianTime,
       "cacheHTTPCltSvcTime": cacheHTTPCltSvcTime,
       "cacheHTTPMissSvcTime": cacheHTTPMissSvcTime,
       "cacheHTTPHitSvcTime": cacheHTTPHitSvcTime,
       "cacheHTTPSrvSvcTime": cacheHTTPSrvSvcTime,
       "cacheDnsSvcTime": cacheDnsSvcTime,
       "cacheHTTPSvcWaitTime": cacheHTTPSvcWaitTime,
       "proxyExecutiveSummary": proxyExecutiveSummary,
       "cacheTotalHttpReqs": cacheTotalHttpReqs,
       "cacheMeanRespTime": cacheMeanRespTime,
       "cacheMeanMissRespTime": cacheMeanMissRespTime,
       "cacheMeanHitRespTime": cacheMeanHitRespTime,
       "cacheMeanHitRatio": cacheMeanHitRatio,
       "cacheMeanByteHitRatio": cacheMeanByteHitRatio,
       "cacheTotalBandwidthSaving": cacheTotalBandwidthSaving,
       "cacheDuration": cacheDuration,
       "cacheCltReplyErrPct": cacheCltReplyErrPct,
       "proxyRecentPerf": proxyRecentPerf,
       "proxyRecentThruputPerf": proxyRecentThruputPerf,
       "cacheThruputNow": cacheThruputNow,
       "cacheThruput1hrPeak": cacheThruput1hrPeak,
       "cacheThruput1hrMean": cacheThruput1hrMean,
       "cacheThruput1dayPeak": cacheThruput1dayPeak,
       "cacheThruput1dayMean": cacheThruput1dayMean,
       "cacheThruput1weekPeak": cacheThruput1weekPeak,
       "cacheThruput1weekMean": cacheThruput1weekMean,
       "cacheThruputLifePeak": cacheThruputLifePeak,
       "cacheThruputLifeMean": cacheThruputLifeMean,
       "proxyRecentBandWSavPerf": proxyRecentBandWSavPerf,
       "cacheBwidthSavingNow": cacheBwidthSavingNow,
       "cacheBwidthSaving1hrPeak": cacheBwidthSaving1hrPeak,
       "cacheBwidthSaving1hrMean": cacheBwidthSaving1hrMean,
       "cacheBwidthSaving1dayPeak": cacheBwidthSaving1dayPeak,
       "cacheBwidthSaving1dayMean": cacheBwidthSaving1dayMean,
       "cacheBwidthSaving1weekPeak": cacheBwidthSaving1weekPeak,
       "cacheBwidthSaving1weekMean": cacheBwidthSaving1weekMean,
       "cacheBwidthSavingLifePeak": cacheBwidthSavingLifePeak,
       "cacheBwidthSavingLifeMean": cacheBwidthSavingLifeMean,
       "proxyRecentBandWSpntPerf": proxyRecentBandWSpntPerf,
       "cacheBwidthSpentNow": cacheBwidthSpentNow,
       "cacheBwidthSpent1hrPeak": cacheBwidthSpent1hrPeak,
       "cacheBwidthSpent1hrMean": cacheBwidthSpent1hrMean,
       "cacheBwidthSpent1dayPeak": cacheBwidthSpent1dayPeak,
       "cacheBwidthSpent1dayMean": cacheBwidthSpent1dayMean,
       "cacheBwidthSpent1weekPeak": cacheBwidthSpent1weekPeak,
       "cacheBwidthSpent1weekMean": cacheBwidthSpent1weekMean,
       "cacheBwidthSpentLifePeak": cacheBwidthSpentLifePeak,
       "cacheBwidthSpentLifeMean": cacheBwidthSpentLifeMean,
       "proxyRecentBandWTotPerf": proxyRecentBandWTotPerf,
       "cacheBwidthTotalNow": cacheBwidthTotalNow,
       "cacheBwidthTotal1hrPeak": cacheBwidthTotal1hrPeak,
       "cacheBwidthTotal1hrMean": cacheBwidthTotal1hrMean,
       "cacheBwidthTotal1dayPeak": cacheBwidthTotal1dayPeak,
       "cacheBwidthTotal1dayMean": cacheBwidthTotal1dayMean,
       "cacheBwidthTotal1weekPeak": cacheBwidthTotal1weekPeak,
       "cacheBwidthTotal1weekMean": cacheBwidthTotal1weekMean,
       "cacheBwidthTotalLifePeak": cacheBwidthTotalLifePeak,
       "cacheBwidthTotalLifeMean": cacheBwidthTotalLifeMean,
       "proxyRecentHitsPerf": proxyRecentHitsPerf,
       "cacheHitsNow": cacheHitsNow,
       "cacheHits1hrPeak": cacheHits1hrPeak,
       "cacheHits1hrMean": cacheHits1hrMean,
       "cacheHits1dayPeak": cacheHits1dayPeak,
       "cacheHits1dayMean": cacheHits1dayMean,
       "cacheHits1weekPeak": cacheHits1weekPeak,
       "cacheHits1weekMean": cacheHits1weekMean,
       "cacheHitsLifePeak": cacheHitsLifePeak,
       "cacheHitsLifeMean": cacheHitsLifeMean,
       "proxyRecentMissesPerf": proxyRecentMissesPerf,
       "cacheMissesNow": cacheMissesNow,
       "cacheMisses1hrPeak": cacheMisses1hrPeak,
       "cacheMisses1hrMean": cacheMisses1hrMean,
       "cacheMisses1dayPeak": cacheMisses1dayPeak,
       "cacheMisses1dayMean": cacheMisses1dayMean,
       "cacheMisses1weekPeak": cacheMisses1weekPeak,
       "cacheMisses1weekMean": cacheMisses1weekMean,
       "cacheMissesLifePeak": cacheMissesLifePeak,
       "cacheMissesLifeMean": cacheMissesLifeMean,
       "proxyRecentHitRespTimePerf": proxyRecentHitRespTimePerf,
       "cacheHitRespTimeNow": cacheHitRespTimeNow,
       "cacheHitRespTime1hrPeak": cacheHitRespTime1hrPeak,
       "cacheHitRespTime1hrMean": cacheHitRespTime1hrMean,
       "cacheHitRespTime1dayPeak": cacheHitRespTime1dayPeak,
       "cacheHitRespTime1dayMean": cacheHitRespTime1dayMean,
       "cacheHitRespTime1weekPeak": cacheHitRespTime1weekPeak,
       "cacheHitRespTime1weekMean": cacheHitRespTime1weekMean,
       "cacheHitRespTimeLifePeak": cacheHitRespTimeLifePeak,
       "cacheHitRespTimeLifeMean": cacheHitRespTimeLifeMean,
       "proxyRecentMissRespTimePerf": proxyRecentMissRespTimePerf,
       "cacheMissRespTimeNow": cacheMissRespTimeNow,
       "cacheMissRespTime1hrPeak": cacheMissRespTime1hrPeak,
       "cacheMissRespTime1hrMean": cacheMissRespTime1hrMean,
       "cacheMissRespTime1dayPeak": cacheMissRespTime1dayPeak,
       "cacheMissRespTime1dayMean": cacheMissRespTime1dayMean,
       "cacheMissRespTime1weekPeak": cacheMissRespTime1weekPeak,
       "cacheMissRespTime1weekMean": cacheMissRespTime1weekMean,
       "cacheMissRespTimeLifePeak": cacheMissRespTimeLifePeak,
       "cacheMissRespTimeLifeMean": cacheMissRespTimeLifeMean,
       "proxyRecentTotalRespTimePerf": proxyRecentTotalRespTimePerf,
       "cacheTotalRespTimeNow": cacheTotalRespTimeNow,
       "cacheTotalRespTime1hrPeak": cacheTotalRespTime1hrPeak,
       "cacheTotalRespTime1hrMean": cacheTotalRespTime1hrMean,
       "cacheTotalRespTime1dayPeak": cacheTotalRespTime1dayPeak,
       "cacheTotalRespTime1dayMean": cacheTotalRespTime1dayMean,
       "cacheTotalRespTime1weekPeak": cacheTotalRespTime1weekPeak,
       "cacheTotalRespTime1weekMean": cacheTotalRespTime1weekMean,
       "cacheTotalRespTimeLifePeak": cacheTotalRespTimeLifePeak,
       "cacheTotalRespTimeLifeMean": cacheTotalRespTimeLifeMean,
       "proxyRecentErrsPerf": proxyRecentErrsPerf,
       "cacheErrsNow": cacheErrsNow,
       "cacheErrs1hrPeak": cacheErrs1hrPeak,
       "cacheErrs1hrMean": cacheErrs1hrMean,
       "cacheErrs1dayPeak": cacheErrs1dayPeak,
       "cacheErrs1dayMean": cacheErrs1dayMean,
       "cacheErrs1weekPeak": cacheErrs1weekPeak,
       "cacheErrs1weekMean": cacheErrs1weekMean,
       "cacheErrsLifePeak": cacheErrsLifePeak,
       "cacheErrsLifeMean": cacheErrsLifeMean,
       "proxyRecentDeniedPerf": proxyRecentDeniedPerf,
       "cacheDeniedNow": cacheDeniedNow,
       "cacheDenied1hrPeak": cacheDenied1hrPeak,
       "cacheDenied1hrMean": cacheDenied1hrMean,
       "cacheDenied1dayPeak": cacheDenied1dayPeak,
       "cacheDenied1dayMean": cacheDenied1dayMean,
       "cacheDenied1weekPeak": cacheDenied1weekPeak,
       "cacheDenied1weekMean": cacheDenied1weekMean,
       "cacheDeniedLifePeak": cacheDeniedLifePeak,
       "cacheDeniedLifeMean": cacheDeniedLifeMean,
       "proxyRecentErrRespTimePerf": proxyRecentErrRespTimePerf,
       "cacheErrRespTimeNow": cacheErrRespTimeNow,
       "cacheErrRespTime1hrPeak": cacheErrRespTime1hrPeak,
       "cacheErrRespTime1hrMean": cacheErrRespTime1hrMean,
       "cacheErrRespTime1dayPeak": cacheErrRespTime1dayPeak,
       "cacheErrRespTime1dayMean": cacheErrRespTime1dayMean,
       "cacheErrRespTime1weekPeak": cacheErrRespTime1weekPeak,
       "cacheErrRespTime1weekMean": cacheErrRespTime1weekMean,
       "cacheErrRespTimeLifePeak": cacheErrRespTimeLifePeak,
       "cacheErrRespTimeLifeMean": cacheErrRespTimeLifeMean,
       "proxyRecentDeniedRespTimePerf": proxyRecentDeniedRespTimePerf,
       "cacheDeniedRespTimeNow": cacheDeniedRespTimeNow,
       "cacheDeniedRespTime1hrPeak": cacheDeniedRespTime1hrPeak,
       "cacheDeniedRespTime1hrMean": cacheDeniedRespTime1hrMean,
       "cacheDeniedRespTime1dayPeak": cacheDeniedRespTime1dayPeak,
       "cacheDeniedRespTime1dayMean": cacheDeniedRespTime1dayMean,
       "cacheDeniedRespTime1weekPeak": cacheDeniedRespTime1weekPeak,
       "cacheDeniedRespTime1weekMean": cacheDeniedRespTime1weekMean,
       "cacheDeniedRespTimeLifePeak": cacheDeniedRespTimeLifePeak,
       "cacheDeniedRespTimeLifeMean": cacheDeniedRespTimeLifeMean,
       "proxyHardware": proxyHardware,
       "proxyHardwareDisk": proxyHardwareDisk,
       "hardwareDiskStatTable": hardwareDiskStatTable,
       "diskStatEntry": diskStatEntry,
       "diskStatEntryNumber": diskStatEntryNumber,
       "diskStatWrites": diskStatWrites,
       "diskStatWriteErrs": diskStatWriteErrs,
       "diskStatReads": diskStatReads,
       "diskStatReadErrs": diskStatReadErrs,
       "proxyTraps": proxyTraps,
       "upstreamProxyFailure": upstreamProxyFailure}
)
