# SNMP MIB module (SQUID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SQUID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:26 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

squid = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3495, 1)
)
squid.setRevisions(
        ("2008-12-24 02:00",
         "2007-12-14 00:00",
         "1999-01-01 00:00",
         "1998-09-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ValidPort(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class CachePeerTableIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Nlanr_ObjectIdentity = ObjectIdentity
nlanr = _Nlanr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3495)
)
_CacheSystem_ObjectIdentity = ObjectIdentity
cacheSystem = _CacheSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3495, 1, 1)
)
_CacheSysVMsize_Type = Integer32
_CacheSysVMsize_Object = MibScalar
cacheSysVMsize = _CacheSysVMsize_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 1, 1),
    _CacheSysVMsize_Type()
)
cacheSysVMsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSysVMsize.setStatus("current")
_CacheSysStorage_Type = Integer32
_CacheSysStorage_Object = MibScalar
cacheSysStorage = _CacheSysStorage_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 1, 2),
    _CacheSysStorage_Type()
)
cacheSysStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSysStorage.setStatus("current")
_CacheUptime_Type = TimeTicks
_CacheUptime_Object = MibScalar
cacheUptime = _CacheUptime_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 1, 3),
    _CacheUptime_Type()
)
cacheUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheUptime.setStatus("current")
_CacheConfig_ObjectIdentity = ObjectIdentity
cacheConfig = _CacheConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3495, 1, 2)
)
_CacheAdmin_Type = DisplayString
_CacheAdmin_Object = MibScalar
cacheAdmin = _CacheAdmin_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 2, 1),
    _CacheAdmin_Type()
)
cacheAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheAdmin.setStatus("current")
_CacheSoftware_Type = DisplayString
_CacheSoftware_Object = MibScalar
cacheSoftware = _CacheSoftware_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 2, 2),
    _CacheSoftware_Type()
)
cacheSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSoftware.setStatus("current")
_CacheVersionId_Type = OctetString
_CacheVersionId_Object = MibScalar
cacheVersionId = _CacheVersionId_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 2, 3),
    _CacheVersionId_Type()
)
cacheVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheVersionId.setStatus("current")
_CacheLoggingFacility_Type = DisplayString
_CacheLoggingFacility_Object = MibScalar
cacheLoggingFacility = _CacheLoggingFacility_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 2, 4),
    _CacheLoggingFacility_Type()
)
cacheLoggingFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacheLoggingFacility.setStatus("current")
_CacheStorageConfig_ObjectIdentity = ObjectIdentity
cacheStorageConfig = _CacheStorageConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3495, 1, 2, 5)
)
_CacheMemMaxSize_Type = Integer32
_CacheMemMaxSize_Object = MibScalar
cacheMemMaxSize = _CacheMemMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 2, 5, 1),
    _CacheMemMaxSize_Type()
)
cacheMemMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMemMaxSize.setStatus("current")
_CacheSwapMaxSize_Type = Integer32
_CacheSwapMaxSize_Object = MibScalar
cacheSwapMaxSize = _CacheSwapMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 2, 5, 2),
    _CacheSwapMaxSize_Type()
)
cacheSwapMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSwapMaxSize.setStatus("current")
_CacheSwapHighWM_Type = Integer32
_CacheSwapHighWM_Object = MibScalar
cacheSwapHighWM = _CacheSwapHighWM_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 2, 5, 3),
    _CacheSwapHighWM_Type()
)
cacheSwapHighWM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSwapHighWM.setStatus("current")
_CacheSwapLowWM_Type = Integer32
_CacheSwapLowWM_Object = MibScalar
cacheSwapLowWM = _CacheSwapLowWM_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 2, 5, 4),
    _CacheSwapLowWM_Type()
)
cacheSwapLowWM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSwapLowWM.setStatus("current")
_CacheUniqName_Type = DisplayString
_CacheUniqName_Object = MibScalar
cacheUniqName = _CacheUniqName_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 2, 6),
    _CacheUniqName_Type()
)
cacheUniqName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheUniqName.setStatus("current")
_CachePerf_ObjectIdentity = ObjectIdentity
cachePerf = _CachePerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3)
)
_CacheSysPerf_ObjectIdentity = ObjectIdentity
cacheSysPerf = _CacheSysPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 1)
)
_CacheSysPageFaults_Type = Counter32
_CacheSysPageFaults_Object = MibScalar
cacheSysPageFaults = _CacheSysPageFaults_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 1),
    _CacheSysPageFaults_Type()
)
cacheSysPageFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSysPageFaults.setStatus("current")
_CacheSysNumReads_Type = Counter32
_CacheSysNumReads_Object = MibScalar
cacheSysNumReads = _CacheSysNumReads_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 2),
    _CacheSysNumReads_Type()
)
cacheSysNumReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSysNumReads.setStatus("current")
_CacheMemUsage_Type = Integer32
_CacheMemUsage_Object = MibScalar
cacheMemUsage = _CacheMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 3),
    _CacheMemUsage_Type()
)
cacheMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMemUsage.setStatus("current")
_CacheCpuTime_Type = Integer32
_CacheCpuTime_Object = MibScalar
cacheCpuTime = _CacheCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 4),
    _CacheCpuTime_Type()
)
cacheCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCpuTime.setStatus("current")
_CacheCpuUsage_Type = Integer32
_CacheCpuUsage_Object = MibScalar
cacheCpuUsage = _CacheCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 5),
    _CacheCpuUsage_Type()
)
cacheCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCpuUsage.setStatus("current")
_CacheMaxResSize_Type = Integer32
_CacheMaxResSize_Object = MibScalar
cacheMaxResSize = _CacheMaxResSize_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 6),
    _CacheMaxResSize_Type()
)
cacheMaxResSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMaxResSize.setStatus("current")
_CacheNumObjCount_Type = Gauge32
_CacheNumObjCount_Object = MibScalar
cacheNumObjCount = _CacheNumObjCount_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 7),
    _CacheNumObjCount_Type()
)
cacheNumObjCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheNumObjCount.setStatus("current")
_CacheCurrentLRUExpiration_Type = TimeTicks
_CacheCurrentLRUExpiration_Object = MibScalar
cacheCurrentLRUExpiration = _CacheCurrentLRUExpiration_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 8),
    _CacheCurrentLRUExpiration_Type()
)
cacheCurrentLRUExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCurrentLRUExpiration.setStatus("current")
_CacheCurrentUnlinkRequests_Type = Gauge32
_CacheCurrentUnlinkRequests_Object = MibScalar
cacheCurrentUnlinkRequests = _CacheCurrentUnlinkRequests_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 9),
    _CacheCurrentUnlinkRequests_Type()
)
cacheCurrentUnlinkRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCurrentUnlinkRequests.setStatus("current")
_CacheCurrentUnusedFDescrCnt_Type = Gauge32
_CacheCurrentUnusedFDescrCnt_Object = MibScalar
cacheCurrentUnusedFDescrCnt = _CacheCurrentUnusedFDescrCnt_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 10),
    _CacheCurrentUnusedFDescrCnt_Type()
)
cacheCurrentUnusedFDescrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCurrentUnusedFDescrCnt.setStatus("current")
_CacheCurrentResFileDescrCnt_Type = Gauge32
_CacheCurrentResFileDescrCnt_Object = MibScalar
cacheCurrentResFileDescrCnt = _CacheCurrentResFileDescrCnt_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 11),
    _CacheCurrentResFileDescrCnt_Type()
)
cacheCurrentResFileDescrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCurrentResFileDescrCnt.setStatus("current")
_CacheCurrentFileDescrCnt_Type = Gauge32
_CacheCurrentFileDescrCnt_Object = MibScalar
cacheCurrentFileDescrCnt = _CacheCurrentFileDescrCnt_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 12),
    _CacheCurrentFileDescrCnt_Type()
)
cacheCurrentFileDescrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCurrentFileDescrCnt.setStatus("current")
_CacheCurrentFileDescrMax_Type = Gauge32
_CacheCurrentFileDescrMax_Object = MibScalar
cacheCurrentFileDescrMax = _CacheCurrentFileDescrMax_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 1, 13),
    _CacheCurrentFileDescrMax_Type()
)
cacheCurrentFileDescrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCurrentFileDescrMax.setStatus("current")
_CacheProtoStats_ObjectIdentity = ObjectIdentity
cacheProtoStats = _CacheProtoStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2)
)
_CacheProtoAggregateStats_ObjectIdentity = ObjectIdentity
cacheProtoAggregateStats = _CacheProtoAggregateStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1)
)
_CacheProtoClientHttpRequests_Type = Counter32
_CacheProtoClientHttpRequests_Object = MibScalar
cacheProtoClientHttpRequests = _CacheProtoClientHttpRequests_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 1),
    _CacheProtoClientHttpRequests_Type()
)
cacheProtoClientHttpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheProtoClientHttpRequests.setStatus("current")
_CacheHttpHits_Type = Counter32
_CacheHttpHits_Object = MibScalar
cacheHttpHits = _CacheHttpHits_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 2),
    _CacheHttpHits_Type()
)
cacheHttpHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHttpHits.setStatus("current")
_CacheHttpErrors_Type = Counter32
_CacheHttpErrors_Object = MibScalar
cacheHttpErrors = _CacheHttpErrors_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 3),
    _CacheHttpErrors_Type()
)
cacheHttpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHttpErrors.setStatus("current")
_CacheHttpInKb_Type = Counter32
_CacheHttpInKb_Object = MibScalar
cacheHttpInKb = _CacheHttpInKb_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 4),
    _CacheHttpInKb_Type()
)
cacheHttpInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHttpInKb.setStatus("current")
_CacheHttpOutKb_Type = Counter32
_CacheHttpOutKb_Object = MibScalar
cacheHttpOutKb = _CacheHttpOutKb_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 5),
    _CacheHttpOutKb_Type()
)
cacheHttpOutKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHttpOutKb.setStatus("current")
_CacheIcpPktsSent_Type = Counter32
_CacheIcpPktsSent_Object = MibScalar
cacheIcpPktsSent = _CacheIcpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 6),
    _CacheIcpPktsSent_Type()
)
cacheIcpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheIcpPktsSent.setStatus("current")
_CacheIcpPktsRecv_Type = Counter32
_CacheIcpPktsRecv_Object = MibScalar
cacheIcpPktsRecv = _CacheIcpPktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 7),
    _CacheIcpPktsRecv_Type()
)
cacheIcpPktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheIcpPktsRecv.setStatus("current")
_CacheIcpKbSent_Type = Counter32
_CacheIcpKbSent_Object = MibScalar
cacheIcpKbSent = _CacheIcpKbSent_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 8),
    _CacheIcpKbSent_Type()
)
cacheIcpKbSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheIcpKbSent.setStatus("current")
_CacheIcpKbRecv_Type = Counter32
_CacheIcpKbRecv_Object = MibScalar
cacheIcpKbRecv = _CacheIcpKbRecv_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 9),
    _CacheIcpKbRecv_Type()
)
cacheIcpKbRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheIcpKbRecv.setStatus("current")
_CacheServerRequests_Type = Integer32
_CacheServerRequests_Object = MibScalar
cacheServerRequests = _CacheServerRequests_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 10),
    _CacheServerRequests_Type()
)
cacheServerRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerRequests.setStatus("current")
_CacheServerErrors_Type = Integer32
_CacheServerErrors_Object = MibScalar
cacheServerErrors = _CacheServerErrors_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 11),
    _CacheServerErrors_Type()
)
cacheServerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerErrors.setStatus("current")
_CacheServerInKb_Type = Counter32
_CacheServerInKb_Object = MibScalar
cacheServerInKb = _CacheServerInKb_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 12),
    _CacheServerInKb_Type()
)
cacheServerInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerInKb.setStatus("current")
_CacheServerOutKb_Type = Counter32
_CacheServerOutKb_Object = MibScalar
cacheServerOutKb = _CacheServerOutKb_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 13),
    _CacheServerOutKb_Type()
)
cacheServerOutKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheServerOutKb.setStatus("current")
_CacheCurrentSwapSize_Type = Gauge32
_CacheCurrentSwapSize_Object = MibScalar
cacheCurrentSwapSize = _CacheCurrentSwapSize_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 14),
    _CacheCurrentSwapSize_Type()
)
cacheCurrentSwapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheCurrentSwapSize.setStatus("current")
_CacheClients_Type = Gauge32
_CacheClients_Object = MibScalar
cacheClients = _CacheClients_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 1, 15),
    _CacheClients_Type()
)
cacheClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClients.setStatus("current")
_CacheMedianSvcTable_Object = MibTable
cacheMedianSvcTable = _CacheMedianSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    cacheMedianSvcTable.setStatus("current")
_CacheMedianSvcEntry_Object = MibTableRow
cacheMedianSvcEntry = _CacheMedianSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1)
)
cacheMedianSvcEntry.setIndexNames(
    (0, "SQUID-MIB", "cacheMedianTime"),
)
if mibBuilder.loadTexts:
    cacheMedianSvcEntry.setStatus("current")


class _CacheMedianTime_Type(Integer32):
    """Custom type cacheMedianTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(60, 60),
    )


_CacheMedianTime_Type.__name__ = "Integer32"
_CacheMedianTime_Object = MibTableColumn
cacheMedianTime = _CacheMedianTime_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 1),
    _CacheMedianTime_Type()
)
cacheMedianTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cacheMedianTime.setStatus("current")
_CacheHttpAllSvcTime_Type = Integer32
_CacheHttpAllSvcTime_Object = MibTableColumn
cacheHttpAllSvcTime = _CacheHttpAllSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 2),
    _CacheHttpAllSvcTime_Type()
)
cacheHttpAllSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHttpAllSvcTime.setStatus("current")
_CacheHttpMissSvcTime_Type = Integer32
_CacheHttpMissSvcTime_Object = MibTableColumn
cacheHttpMissSvcTime = _CacheHttpMissSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 3),
    _CacheHttpMissSvcTime_Type()
)
cacheHttpMissSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHttpMissSvcTime.setStatus("current")
_CacheHttpNmSvcTime_Type = Integer32
_CacheHttpNmSvcTime_Object = MibTableColumn
cacheHttpNmSvcTime = _CacheHttpNmSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 4),
    _CacheHttpNmSvcTime_Type()
)
cacheHttpNmSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHttpNmSvcTime.setStatus("current")
_CacheHttpHitSvcTime_Type = Integer32
_CacheHttpHitSvcTime_Object = MibTableColumn
cacheHttpHitSvcTime = _CacheHttpHitSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 5),
    _CacheHttpHitSvcTime_Type()
)
cacheHttpHitSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHttpHitSvcTime.setStatus("current")
_CacheIcpQuerySvcTime_Type = Integer32
_CacheIcpQuerySvcTime_Object = MibTableColumn
cacheIcpQuerySvcTime = _CacheIcpQuerySvcTime_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 6),
    _CacheIcpQuerySvcTime_Type()
)
cacheIcpQuerySvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheIcpQuerySvcTime.setStatus("current")
_CacheIcpReplySvcTime_Type = Integer32
_CacheIcpReplySvcTime_Object = MibTableColumn
cacheIcpReplySvcTime = _CacheIcpReplySvcTime_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 7),
    _CacheIcpReplySvcTime_Type()
)
cacheIcpReplySvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheIcpReplySvcTime.setStatus("current")
_CacheDnsSvcTime_Type = Integer32
_CacheDnsSvcTime_Object = MibTableColumn
cacheDnsSvcTime = _CacheDnsSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 8),
    _CacheDnsSvcTime_Type()
)
cacheDnsSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDnsSvcTime.setStatus("current")
_CacheRequestHitRatio_Type = Integer32
_CacheRequestHitRatio_Object = MibTableColumn
cacheRequestHitRatio = _CacheRequestHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 9),
    _CacheRequestHitRatio_Type()
)
cacheRequestHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheRequestHitRatio.setStatus("current")
_CacheRequestByteRatio_Type = Integer32
_CacheRequestByteRatio_Object = MibTableColumn
cacheRequestByteRatio = _CacheRequestByteRatio_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 10),
    _CacheRequestByteRatio_Type()
)
cacheRequestByteRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheRequestByteRatio.setStatus("current")
_CacheHttpNhSvcTime_Type = Integer32
_CacheHttpNhSvcTime_Object = MibTableColumn
cacheHttpNhSvcTime = _CacheHttpNhSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 3, 2, 2, 1, 11),
    _CacheHttpNhSvcTime_Type()
)
cacheHttpNhSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHttpNhSvcTime.setStatus("current")
_CacheNetwork_ObjectIdentity = ObjectIdentity
cacheNetwork = _CacheNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4)
)
_CacheIpCache_ObjectIdentity = ObjectIdentity
cacheIpCache = _CacheIpCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 1)
)
_CacheIpEntries_Type = Gauge32
_CacheIpEntries_Object = MibScalar
cacheIpEntries = _CacheIpEntries_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 1),
    _CacheIpEntries_Type()
)
cacheIpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheIpEntries.setStatus("current")
_CacheIpRequests_Type = Counter32
_CacheIpRequests_Object = MibScalar
cacheIpRequests = _CacheIpRequests_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 2),
    _CacheIpRequests_Type()
)
cacheIpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheIpRequests.setStatus("current")
_CacheIpHits_Type = Counter32
_CacheIpHits_Object = MibScalar
cacheIpHits = _CacheIpHits_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 3),
    _CacheIpHits_Type()
)
cacheIpHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheIpHits.setStatus("current")
_CacheIpPendingHits_Type = Gauge32
_CacheIpPendingHits_Object = MibScalar
cacheIpPendingHits = _CacheIpPendingHits_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 4),
    _CacheIpPendingHits_Type()
)
cacheIpPendingHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheIpPendingHits.setStatus("current")
_CacheIpNegativeHits_Type = Counter32
_CacheIpNegativeHits_Object = MibScalar
cacheIpNegativeHits = _CacheIpNegativeHits_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 5),
    _CacheIpNegativeHits_Type()
)
cacheIpNegativeHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheIpNegativeHits.setStatus("current")
_CacheIpMisses_Type = Counter32
_CacheIpMisses_Object = MibScalar
cacheIpMisses = _CacheIpMisses_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 6),
    _CacheIpMisses_Type()
)
cacheIpMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheIpMisses.setStatus("current")
_CacheBlockingGetHostByName_Type = Counter32
_CacheBlockingGetHostByName_Object = MibScalar
cacheBlockingGetHostByName = _CacheBlockingGetHostByName_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 7),
    _CacheBlockingGetHostByName_Type()
)
cacheBlockingGetHostByName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBlockingGetHostByName.setStatus("current")
_CacheAttemptReleaseLckEntries_Type = Counter32
_CacheAttemptReleaseLckEntries_Object = MibScalar
cacheAttemptReleaseLckEntries = _CacheAttemptReleaseLckEntries_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 1, 8),
    _CacheAttemptReleaseLckEntries_Type()
)
cacheAttemptReleaseLckEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheAttemptReleaseLckEntries.setStatus("current")
_CacheFqdnCache_ObjectIdentity = ObjectIdentity
cacheFqdnCache = _CacheFqdnCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 2)
)
_CacheFqdnEntries_Type = Gauge32
_CacheFqdnEntries_Object = MibScalar
cacheFqdnEntries = _CacheFqdnEntries_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 2, 1),
    _CacheFqdnEntries_Type()
)
cacheFqdnEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheFqdnEntries.setStatus("current")
_CacheFqdnRequests_Type = Counter32
_CacheFqdnRequests_Object = MibScalar
cacheFqdnRequests = _CacheFqdnRequests_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 2, 2),
    _CacheFqdnRequests_Type()
)
cacheFqdnRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheFqdnRequests.setStatus("current")
_CacheFqdnHits_Type = Counter32
_CacheFqdnHits_Object = MibScalar
cacheFqdnHits = _CacheFqdnHits_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 2, 3),
    _CacheFqdnHits_Type()
)
cacheFqdnHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheFqdnHits.setStatus("current")
_CacheFqdnPendingHits_Type = Gauge32
_CacheFqdnPendingHits_Object = MibScalar
cacheFqdnPendingHits = _CacheFqdnPendingHits_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 2, 4),
    _CacheFqdnPendingHits_Type()
)
cacheFqdnPendingHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheFqdnPendingHits.setStatus("current")
_CacheFqdnNegativeHits_Type = Counter32
_CacheFqdnNegativeHits_Object = MibScalar
cacheFqdnNegativeHits = _CacheFqdnNegativeHits_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 2, 5),
    _CacheFqdnNegativeHits_Type()
)
cacheFqdnNegativeHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheFqdnNegativeHits.setStatus("current")
_CacheFqdnMisses_Type = Counter32
_CacheFqdnMisses_Object = MibScalar
cacheFqdnMisses = _CacheFqdnMisses_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 2, 6),
    _CacheFqdnMisses_Type()
)
cacheFqdnMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheFqdnMisses.setStatus("current")
_CacheBlockingGetHostByAddr_Type = Counter32
_CacheBlockingGetHostByAddr_Object = MibScalar
cacheBlockingGetHostByAddr = _CacheBlockingGetHostByAddr_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 2, 7),
    _CacheBlockingGetHostByAddr_Type()
)
cacheBlockingGetHostByAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBlockingGetHostByAddr.setStatus("current")
_CacheDns_ObjectIdentity = ObjectIdentity
cacheDns = _CacheDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 3)
)
_CacheDnsRequests_Type = Counter32
_CacheDnsRequests_Object = MibScalar
cacheDnsRequests = _CacheDnsRequests_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 3, 1),
    _CacheDnsRequests_Type()
)
cacheDnsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDnsRequests.setStatus("current")
_CacheDnsReplies_Type = Counter32
_CacheDnsReplies_Object = MibScalar
cacheDnsReplies = _CacheDnsReplies_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 3, 2),
    _CacheDnsReplies_Type()
)
cacheDnsReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDnsReplies.setStatus("current")
_CacheDnsNumberServers_Type = Counter32
_CacheDnsNumberServers_Object = MibScalar
cacheDnsNumberServers = _CacheDnsNumberServers_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 4, 3, 3),
    _CacheDnsNumberServers_Type()
)
cacheDnsNumberServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDnsNumberServers.setStatus("current")
_CacheMesh_ObjectIdentity = ObjectIdentity
cacheMesh = _CacheMesh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5)
)
_CachePeerTable_Object = MibTable
cachePeerTable = _CachePeerTable_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cachePeerTable.setStatus("current")
_CachePeerEntry_Object = MibTableRow
cachePeerEntry = _CachePeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3)
)
cachePeerEntry.setIndexNames(
    (0, "SQUID-MIB", "cachePeerIndex"),
)
if mibBuilder.loadTexts:
    cachePeerEntry.setStatus("current")
_CachePeerIndex_Type = CachePeerTableIndex
_CachePeerIndex_Object = MibTableColumn
cachePeerIndex = _CachePeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 1),
    _CachePeerIndex_Type()
)
cachePeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerIndex.setStatus("current")
_CachePeerName_Type = DisplayString
_CachePeerName_Object = MibTableColumn
cachePeerName = _CachePeerName_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 2),
    _CachePeerName_Type()
)
cachePeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerName.setStatus("current")
_CachePeerAddressType_Type = InetAddressType
_CachePeerAddressType_Object = MibTableColumn
cachePeerAddressType = _CachePeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 3),
    _CachePeerAddressType_Type()
)
cachePeerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerAddressType.setStatus("current")


class _CachePeerAddress_Type(InetAddress):
    """Custom type cachePeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CachePeerAddress_Type.__name__ = "InetAddress"
_CachePeerAddress_Object = MibTableColumn
cachePeerAddress = _CachePeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 4),
    _CachePeerAddress_Type()
)
cachePeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerAddress.setStatus("current")
_CachePeerPortHttp_Type = ValidPort
_CachePeerPortHttp_Object = MibTableColumn
cachePeerPortHttp = _CachePeerPortHttp_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 5),
    _CachePeerPortHttp_Type()
)
cachePeerPortHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerPortHttp.setStatus("current")
_CachePeerPortIcp_Type = ValidPort
_CachePeerPortIcp_Object = MibTableColumn
cachePeerPortIcp = _CachePeerPortIcp_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 6),
    _CachePeerPortIcp_Type()
)
cachePeerPortIcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerPortIcp.setStatus("current")
_CachePeerType_Type = Integer32
_CachePeerType_Object = MibTableColumn
cachePeerType = _CachePeerType_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 7),
    _CachePeerType_Type()
)
cachePeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerType.setStatus("current")
_CachePeerState_Type = Integer32
_CachePeerState_Object = MibTableColumn
cachePeerState = _CachePeerState_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 8),
    _CachePeerState_Type()
)
cachePeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerState.setStatus("current")
_CachePeerPingsSent_Type = Counter32
_CachePeerPingsSent_Object = MibTableColumn
cachePeerPingsSent = _CachePeerPingsSent_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 9),
    _CachePeerPingsSent_Type()
)
cachePeerPingsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerPingsSent.setStatus("current")
_CachePeerPingsAcked_Type = Counter32
_CachePeerPingsAcked_Object = MibTableColumn
cachePeerPingsAcked = _CachePeerPingsAcked_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 10),
    _CachePeerPingsAcked_Type()
)
cachePeerPingsAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerPingsAcked.setStatus("current")
_CachePeerFetches_Type = Counter32
_CachePeerFetches_Object = MibTableColumn
cachePeerFetches = _CachePeerFetches_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 11),
    _CachePeerFetches_Type()
)
cachePeerFetches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerFetches.setStatus("current")
_CachePeerRtt_Type = Integer32
_CachePeerRtt_Object = MibTableColumn
cachePeerRtt = _CachePeerRtt_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 12),
    _CachePeerRtt_Type()
)
cachePeerRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerRtt.setStatus("current")
_CachePeerIgnored_Type = Counter32
_CachePeerIgnored_Object = MibTableColumn
cachePeerIgnored = _CachePeerIgnored_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 13),
    _CachePeerIgnored_Type()
)
cachePeerIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerIgnored.setStatus("current")
_CachePeerKeepAlSent_Type = Counter32
_CachePeerKeepAlSent_Object = MibTableColumn
cachePeerKeepAlSent = _CachePeerKeepAlSent_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 14),
    _CachePeerKeepAlSent_Type()
)
cachePeerKeepAlSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerKeepAlSent.setStatus("current")
_CachePeerKeepAlRecv_Type = Counter32
_CachePeerKeepAlRecv_Object = MibTableColumn
cachePeerKeepAlRecv = _CachePeerKeepAlRecv_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 1, 3, 15),
    _CachePeerKeepAlRecv_Type()
)
cachePeerKeepAlRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cachePeerKeepAlRecv.setStatus("current")
_CacheClientTable_Object = MibTable
cacheClientTable = _CacheClientTable_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cacheClientTable.setStatus("current")
_CacheClientEntry_Object = MibTableRow
cacheClientEntry = _CacheClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2)
)
cacheClientEntry.setIndexNames(
    (0, "SQUID-MIB", "cacheClientAddress"),
)
if mibBuilder.loadTexts:
    cacheClientEntry.setStatus("current")
_CacheClientAddressType_Type = InetAddressType
_CacheClientAddressType_Object = MibTableColumn
cacheClientAddressType = _CacheClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 1),
    _CacheClientAddressType_Type()
)
cacheClientAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientAddressType.setStatus("current")


class _CacheClientAddress_Type(InetAddress):
    """Custom type cacheClientAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CacheClientAddress_Type.__name__ = "InetAddress"
_CacheClientAddress_Object = MibTableColumn
cacheClientAddress = _CacheClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 2),
    _CacheClientAddress_Type()
)
cacheClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientAddress.setStatus("current")
_CacheClientHttpRequests_Type = Counter32
_CacheClientHttpRequests_Object = MibTableColumn
cacheClientHttpRequests = _CacheClientHttpRequests_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 3),
    _CacheClientHttpRequests_Type()
)
cacheClientHttpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientHttpRequests.setStatus("current")
_CacheClientHttpKb_Type = Counter32
_CacheClientHttpKb_Object = MibTableColumn
cacheClientHttpKb = _CacheClientHttpKb_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 4),
    _CacheClientHttpKb_Type()
)
cacheClientHttpKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientHttpKb.setStatus("current")
_CacheClientHttpHits_Type = Counter32
_CacheClientHttpHits_Object = MibTableColumn
cacheClientHttpHits = _CacheClientHttpHits_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 5),
    _CacheClientHttpHits_Type()
)
cacheClientHttpHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientHttpHits.setStatus("current")
_CacheClientHTTPHitKb_Type = Counter32
_CacheClientHTTPHitKb_Object = MibTableColumn
cacheClientHTTPHitKb = _CacheClientHTTPHitKb_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 6),
    _CacheClientHTTPHitKb_Type()
)
cacheClientHTTPHitKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientHTTPHitKb.setStatus("current")
_CacheClientIcpRequests_Type = Counter32
_CacheClientIcpRequests_Object = MibTableColumn
cacheClientIcpRequests = _CacheClientIcpRequests_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 7),
    _CacheClientIcpRequests_Type()
)
cacheClientIcpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientIcpRequests.setStatus("current")
_CacheClientIcpKb_Type = Counter32
_CacheClientIcpKb_Object = MibTableColumn
cacheClientIcpKb = _CacheClientIcpKb_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 8),
    _CacheClientIcpKb_Type()
)
cacheClientIcpKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientIcpKb.setStatus("current")
_CacheClientIcpHits_Type = Counter32
_CacheClientIcpHits_Object = MibTableColumn
cacheClientIcpHits = _CacheClientIcpHits_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 9),
    _CacheClientIcpHits_Type()
)
cacheClientIcpHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientIcpHits.setStatus("current")
_CacheClientIcpHitKb_Type = Counter32
_CacheClientIcpHitKb_Object = MibTableColumn
cacheClientIcpHitKb = _CacheClientIcpHitKb_Object(
    (1, 3, 6, 1, 4, 1, 3495, 1, 5, 2, 2, 10),
    _CacheClientIcpHitKb_Type()
)
cacheClientIcpHitKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheClientIcpHitKb.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SQUID-MIB",
    **{"ValidPort": ValidPort,
       "CachePeerTableIndex": CachePeerTableIndex,
       "nlanr": nlanr,
       "squid": squid,
       "cacheSystem": cacheSystem,
       "cacheSysVMsize": cacheSysVMsize,
       "cacheSysStorage": cacheSysStorage,
       "cacheUptime": cacheUptime,
       "cacheConfig": cacheConfig,
       "cacheAdmin": cacheAdmin,
       "cacheSoftware": cacheSoftware,
       "cacheVersionId": cacheVersionId,
       "cacheLoggingFacility": cacheLoggingFacility,
       "cacheStorageConfig": cacheStorageConfig,
       "cacheMemMaxSize": cacheMemMaxSize,
       "cacheSwapMaxSize": cacheSwapMaxSize,
       "cacheSwapHighWM": cacheSwapHighWM,
       "cacheSwapLowWM": cacheSwapLowWM,
       "cacheUniqName": cacheUniqName,
       "cachePerf": cachePerf,
       "cacheSysPerf": cacheSysPerf,
       "cacheSysPageFaults": cacheSysPageFaults,
       "cacheSysNumReads": cacheSysNumReads,
       "cacheMemUsage": cacheMemUsage,
       "cacheCpuTime": cacheCpuTime,
       "cacheCpuUsage": cacheCpuUsage,
       "cacheMaxResSize": cacheMaxResSize,
       "cacheNumObjCount": cacheNumObjCount,
       "cacheCurrentLRUExpiration": cacheCurrentLRUExpiration,
       "cacheCurrentUnlinkRequests": cacheCurrentUnlinkRequests,
       "cacheCurrentUnusedFDescrCnt": cacheCurrentUnusedFDescrCnt,
       "cacheCurrentResFileDescrCnt": cacheCurrentResFileDescrCnt,
       "cacheCurrentFileDescrCnt": cacheCurrentFileDescrCnt,
       "cacheCurrentFileDescrMax": cacheCurrentFileDescrMax,
       "cacheProtoStats": cacheProtoStats,
       "cacheProtoAggregateStats": cacheProtoAggregateStats,
       "cacheProtoClientHttpRequests": cacheProtoClientHttpRequests,
       "cacheHttpHits": cacheHttpHits,
       "cacheHttpErrors": cacheHttpErrors,
       "cacheHttpInKb": cacheHttpInKb,
       "cacheHttpOutKb": cacheHttpOutKb,
       "cacheIcpPktsSent": cacheIcpPktsSent,
       "cacheIcpPktsRecv": cacheIcpPktsRecv,
       "cacheIcpKbSent": cacheIcpKbSent,
       "cacheIcpKbRecv": cacheIcpKbRecv,
       "cacheServerRequests": cacheServerRequests,
       "cacheServerErrors": cacheServerErrors,
       "cacheServerInKb": cacheServerInKb,
       "cacheServerOutKb": cacheServerOutKb,
       "cacheCurrentSwapSize": cacheCurrentSwapSize,
       "cacheClients": cacheClients,
       "cacheMedianSvcTable": cacheMedianSvcTable,
       "cacheMedianSvcEntry": cacheMedianSvcEntry,
       "cacheMedianTime": cacheMedianTime,
       "cacheHttpAllSvcTime": cacheHttpAllSvcTime,
       "cacheHttpMissSvcTime": cacheHttpMissSvcTime,
       "cacheHttpNmSvcTime": cacheHttpNmSvcTime,
       "cacheHttpHitSvcTime": cacheHttpHitSvcTime,
       "cacheIcpQuerySvcTime": cacheIcpQuerySvcTime,
       "cacheIcpReplySvcTime": cacheIcpReplySvcTime,
       "cacheDnsSvcTime": cacheDnsSvcTime,
       "cacheRequestHitRatio": cacheRequestHitRatio,
       "cacheRequestByteRatio": cacheRequestByteRatio,
       "cacheHttpNhSvcTime": cacheHttpNhSvcTime,
       "cacheNetwork": cacheNetwork,
       "cacheIpCache": cacheIpCache,
       "cacheIpEntries": cacheIpEntries,
       "cacheIpRequests": cacheIpRequests,
       "cacheIpHits": cacheIpHits,
       "cacheIpPendingHits": cacheIpPendingHits,
       "cacheIpNegativeHits": cacheIpNegativeHits,
       "cacheIpMisses": cacheIpMisses,
       "cacheBlockingGetHostByName": cacheBlockingGetHostByName,
       "cacheAttemptReleaseLckEntries": cacheAttemptReleaseLckEntries,
       "cacheFqdnCache": cacheFqdnCache,
       "cacheFqdnEntries": cacheFqdnEntries,
       "cacheFqdnRequests": cacheFqdnRequests,
       "cacheFqdnHits": cacheFqdnHits,
       "cacheFqdnPendingHits": cacheFqdnPendingHits,
       "cacheFqdnNegativeHits": cacheFqdnNegativeHits,
       "cacheFqdnMisses": cacheFqdnMisses,
       "cacheBlockingGetHostByAddr": cacheBlockingGetHostByAddr,
       "cacheDns": cacheDns,
       "cacheDnsRequests": cacheDnsRequests,
       "cacheDnsReplies": cacheDnsReplies,
       "cacheDnsNumberServers": cacheDnsNumberServers,
       "cacheMesh": cacheMesh,
       "cachePeerTable": cachePeerTable,
       "cachePeerEntry": cachePeerEntry,
       "cachePeerIndex": cachePeerIndex,
       "cachePeerName": cachePeerName,
       "cachePeerAddressType": cachePeerAddressType,
       "cachePeerAddress": cachePeerAddress,
       "cachePeerPortHttp": cachePeerPortHttp,
       "cachePeerPortIcp": cachePeerPortIcp,
       "cachePeerType": cachePeerType,
       "cachePeerState": cachePeerState,
       "cachePeerPingsSent": cachePeerPingsSent,
       "cachePeerPingsAcked": cachePeerPingsAcked,
       "cachePeerFetches": cachePeerFetches,
       "cachePeerRtt": cachePeerRtt,
       "cachePeerIgnored": cachePeerIgnored,
       "cachePeerKeepAlSent": cachePeerKeepAlSent,
       "cachePeerKeepAlRecv": cachePeerKeepAlRecv,
       "cacheClientTable": cacheClientTable,
       "cacheClientEntry": cacheClientEntry,
       "cacheClientAddressType": cacheClientAddressType,
       "cacheClientAddress": cacheClientAddress,
       "cacheClientHttpRequests": cacheClientHttpRequests,
       "cacheClientHttpKb": cacheClientHttpKb,
       "cacheClientHttpHits": cacheClientHttpHits,
       "cacheClientHTTPHitKb": cacheClientHTTPHitKb,
       "cacheClientIcpRequests": cacheClientIcpRequests,
       "cacheClientIcpKb": cacheClientIcpKb,
       "cacheClientIcpHits": cacheClientIcpHits,
       "cacheClientIcpHitKb": cacheClientIcpHitKb}
)
