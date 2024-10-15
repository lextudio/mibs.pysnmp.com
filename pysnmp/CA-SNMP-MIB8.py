# SNMP MIB module (CA-SNMP-MIB8) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CA-SNMP-MIB8
# Produced by pysmi-1.5.4 at Mon Oct 14 20:51:56 2024
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

arrayNetworks = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7564)
)
arrayNetworks.setRevisions(
        ("2005-09-14 00:00",
         "1999-12-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Float(Opaque, TextualConvention):
    status = "current"
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )



class SyslogSeverity(Integer32, TextualConvention):
    status = "current"
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )



# MIB Managed Objects in the order of their OIDs

_SystemInfo_ObjectIdentity = ObjectIdentity
systemInfo = _SystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 3)
)
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7564, 3, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 4)
)
_SysMemory_Type = Counter64
_SysMemory_Object = MibScalar
sysMemory = _SysMemory_Object(
    (1, 3, 6, 1, 4, 1, 7564, 4, 1),
    _SysMemory_Type()
)
sysMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemory.setStatus("current")
_SysMemoryUtilization_Type = Gauge32
_SysMemoryUtilization_Object = MibScalar
sysMemoryUtilization = _SysMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 7564, 4, 2),
    _SysMemoryUtilization_Type()
)
sysMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemoryUtilization.setStatus("current")
_SysSwapUsed_Type = Gauge32
_SysSwapUsed_Object = MibScalar
sysSwapUsed = _SysSwapUsed_Object(
    (1, 3, 6, 1, 4, 1, 7564, 4, 3),
    _SysSwapUsed_Type()
)
sysSwapUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwapUsed.setStatus("current")
_SysSwapCapacity_Type = Gauge32
_SysSwapCapacity_Object = MibScalar
sysSwapCapacity = _SysSwapCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7564, 4, 4),
    _SysSwapCapacity_Type()
)
sysSwapCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwapCapacity.setStatus("current")
_RevProxyCache_ObjectIdentity = ObjectIdentity
revProxyCache = _RevProxyCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 16)
)
_CacheBasicStats_ObjectIdentity = ObjectIdentity
cacheBasicStats = _CacheBasicStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1)
)


class _CacheStatus_Type(Integer32):
    """Custom type cacheStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CacheStatus_Type.__name__ = "Integer32"
_CacheStatus_Object = MibScalar
cacheStatus = _CacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 1),
    _CacheStatus_Type()
)
cacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheStatus.setStatus("current")
_RequestsReceived_Type = Counter32
_RequestsReceived_Object = MibScalar
requestsReceived = _RequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 2),
    _RequestsReceived_Type()
)
requestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    requestsReceived.setStatus("current")
_GetRequests_Type = Counter32
_GetRequests_Object = MibScalar
getRequests = _GetRequests_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 3),
    _GetRequests_Type()
)
getRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    getRequests.setStatus("current")
_HeadRequests_Type = Counter32
_HeadRequests_Object = MibScalar
headRequests = _HeadRequests_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 4),
    _HeadRequests_Type()
)
headRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    headRequests.setStatus("current")
_PurgeRequests_Type = Counter32
_PurgeRequests_Object = MibScalar
purgeRequests = _PurgeRequests_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 5),
    _PurgeRequests_Type()
)
purgeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    purgeRequests.setStatus("current")
_PostRequests_Type = Counter32
_PostRequests_Object = MibScalar
postRequests = _PostRequests_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 6),
    _PostRequests_Type()
)
postRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postRequests.setStatus("current")
_ClientEstabConn_Type = Gauge32
_ClientEstabConn_Object = MibScalar
clientEstabConn = _ClientEstabConn_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 7),
    _ClientEstabConn_Type()
)
clientEstabConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientEstabConn.setStatus("current")
_ServerEstabConn_Type = Gauge32
_ServerEstabConn_Object = MibScalar
serverEstabConn = _ServerEstabConn_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 8),
    _ServerEstabConn_Type()
)
serverEstabConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverEstabConn.setStatus("current")
_RequestsToHttps_Type = Counter32
_RequestsToHttps_Object = MibScalar
requestsToHttps = _RequestsToHttps_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 9),
    _RequestsToHttps_Type()
)
requestsToHttps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    requestsToHttps.setStatus("current")
_RequestsOnRegex_Type = Counter32
_RequestsOnRegex_Object = MibScalar
requestsOnRegex = _RequestsOnRegex_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 10),
    _RequestsOnRegex_Type()
)
requestsOnRegex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    requestsOnRegex.setStatus("current")
_RequestsToUrl_Type = Counter32
_RequestsToUrl_Object = MibScalar
requestsToUrl = _RequestsToUrl_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 11),
    _RequestsToUrl_Type()
)
requestsToUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    requestsToUrl.setStatus("current")
_ResponsesToHttps_Type = Counter32
_ResponsesToHttps_Object = MibScalar
responsesToHttps = _ResponsesToHttps_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 12),
    _ResponsesToHttps_Type()
)
responsesToHttps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    responsesToHttps.setStatus("current")
_ResponsesOnRegex_Type = Counter32
_ResponsesOnRegex_Object = MibScalar
responsesOnRegex = _ResponsesOnRegex_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 13),
    _ResponsesOnRegex_Type()
)
responsesOnRegex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    responsesOnRegex.setStatus("current")
_CacheSkip_Type = Counter32
_CacheSkip_Object = MibScalar
cacheSkip = _CacheSkip_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 14),
    _CacheSkip_Type()
)
cacheSkip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSkip.setStatus("current")
_HitsReply_Type = Counter32
_HitsReply_Object = MibScalar
hitsReply = _HitsReply_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 15),
    _HitsReply_Type()
)
hitsReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hitsReply.setStatus("current")
_HitsReplyWNotModified_Type = Counter32
_HitsReplyWNotModified_Object = MibScalar
hitsReplyWNotModified = _HitsReplyWNotModified_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 16),
    _HitsReplyWNotModified_Type()
)
hitsReplyWNotModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hitsReplyWNotModified.setStatus("current")
_HitsReplyWPreFailed_Type = Counter32
_HitsReplyWPreFailed_Object = MibScalar
hitsReplyWPreFailed = _HitsReplyWPreFailed_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 17),
    _HitsReplyWPreFailed_Type()
)
hitsReplyWPreFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hitsReplyWPreFailed.setStatus("current")
_HitRevalidate_Type = Counter32
_HitRevalidate_Object = MibScalar
hitRevalidate = _HitRevalidate_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 18),
    _HitRevalidate_Type()
)
hitRevalidate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hitRevalidate.setStatus("current")
_CacheMissWNoncacheReq_Type = Counter32
_CacheMissWNoncacheReq_Object = MibScalar
cacheMissWNoncacheReq = _CacheMissWNoncacheReq_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 19),
    _CacheMissWNoncacheReq_Type()
)
cacheMissWNoncacheReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissWNoncacheReq.setStatus("current")
_CacheMissWNewEntry_Type = Counter32
_CacheMissWNewEntry_Object = MibScalar
cacheMissWNewEntry = _CacheMissWNewEntry_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 20),
    _CacheMissWNewEntry_Type()
)
cacheMissWNewEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissWNewEntry.setStatus("current")
_CacheMissWRespNo_Type = Counter32
_CacheMissWRespNo_Object = MibScalar
cacheMissWRespNo = _CacheMissWRespNo_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 21),
    _CacheMissWRespNo_Type()
)
cacheMissWRespNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheMissWRespNo.setStatus("current")
_CacheHitRatio_Type = Counter32
_CacheHitRatio_Object = MibScalar
cacheHitRatio = _CacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 7564, 16, 1, 22),
    _CacheHitRatio_Type()
)
cacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheHitRatio.setStatus("current")
_Vrrp_ObjectIdentity = ObjectIdentity
vrrp = _Vrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 18)
)
_ClusterVrrp_ObjectIdentity = ObjectIdentity
clusterVrrp = _ClusterVrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1)
)
_MaxCluster_Type = Integer32
_MaxCluster_Object = MibScalar
maxCluster = _MaxCluster_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 1),
    _MaxCluster_Type()
)
maxCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxCluster.setStatus("current")
_ClusterNum_Type = Integer32
_ClusterNum_Object = MibScalar
clusterNum = _ClusterNum_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 2),
    _ClusterNum_Type()
)
clusterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNum.setStatus("current")
_VrrpTable_Object = MibTable
vrrpTable = _VrrpTable_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 3)
)
if mibBuilder.loadTexts:
    vrrpTable.setStatus("current")
_VrrpEntry_Object = MibTableRow
vrrpEntry = _VrrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 3, 1)
)
vrrpEntry.setIndexNames(
    (0, "CA-SNMP-MIB8", "clusterVirIndex"),
)
if mibBuilder.loadTexts:
    vrrpEntry.setStatus("current")
_ClusterVirIndex_Type = Integer32
_ClusterVirIndex_Object = MibTableColumn
clusterVirIndex = _ClusterVirIndex_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 3, 1, 1),
    _ClusterVirIndex_Type()
)
clusterVirIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVirIndex.setStatus("current")


class _ClusterId_Type(Integer32):
    """Custom type clusterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClusterId_Type.__name__ = "Integer32"
_ClusterId_Object = MibTableColumn
clusterId = _ClusterId_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 3, 1, 2),
    _ClusterId_Type()
)
clusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterId.setStatus("current")


class _ClusterVirState_Type(Integer32):
    """Custom type clusterVirState based on Integer32"""
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
        *(("backup", 3),
          ("incomplete", 0),
          ("init", 2),
          ("master", 4),
          ("reserverd", 1))
    )


_ClusterVirState_Type.__name__ = "Integer32"
_ClusterVirState_Object = MibTableColumn
clusterVirState = _ClusterVirState_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 3, 1, 3),
    _ClusterVirState_Type()
)
clusterVirState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVirState.setStatus("current")
_ClusterVirIfname_Type = DisplayString
_ClusterVirIfname_Object = MibTableColumn
clusterVirIfname = _ClusterVirIfname_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 3, 1, 4),
    _ClusterVirIfname_Type()
)
clusterVirIfname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVirIfname.setStatus("current")
_ClusterVirAddr_Type = IpAddress
_ClusterVirAddr_Object = MibTableColumn
clusterVirAddr = _ClusterVirAddr_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 3, 1, 5),
    _ClusterVirAddr_Type()
)
clusterVirAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVirAddr.setStatus("current")


class _ClusterVirAuthType_Type(Integer32):
    """Custom type clusterVirAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("simple-text-password", 1))
    )


_ClusterVirAuthType_Type.__name__ = "Integer32"
_ClusterVirAuthType_Object = MibTableColumn
clusterVirAuthType = _ClusterVirAuthType_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 3, 1, 6),
    _ClusterVirAuthType_Type()
)
clusterVirAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVirAuthType.setStatus("current")
_ClusterVirAuthPasswd_Type = DisplayString
_ClusterVirAuthPasswd_Object = MibTableColumn
clusterVirAuthPasswd = _ClusterVirAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 3, 1, 7),
    _ClusterVirAuthPasswd_Type()
)
clusterVirAuthPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVirAuthPasswd.setStatus("current")


class _ClusterVirPreempt_Type(Integer32):
    """Custom type clusterVirPreempt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ClusterVirPreempt_Type.__name__ = "Integer32"
_ClusterVirPreempt_Object = MibTableColumn
clusterVirPreempt = _ClusterVirPreempt_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 3, 1, 8),
    _ClusterVirPreempt_Type()
)
clusterVirPreempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVirPreempt.setStatus("current")


class _ClusterVirInterval_Type(Integer32):
    """Custom type clusterVirInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_ClusterVirInterval_Type.__name__ = "Integer32"
_ClusterVirInterval_Object = MibTableColumn
clusterVirInterval = _ClusterVirInterval_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 3, 1, 9),
    _ClusterVirInterval_Type()
)
clusterVirInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVirInterval.setStatus("current")


class _ClusterVirPriority_Type(Integer32):
    """Custom type clusterVirPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ClusterVirPriority_Type.__name__ = "Integer32"
_ClusterVirPriority_Object = MibTableColumn
clusterVirPriority = _ClusterVirPriority_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 3, 1, 10),
    _ClusterVirPriority_Type()
)
clusterVirPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVirPriority.setStatus("current")
_ClusterVirAddressType_Type = InetAddressType
_ClusterVirAddressType_Object = MibTableColumn
clusterVirAddressType = _ClusterVirAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 3, 1, 11),
    _ClusterVirAddressType_Type()
)
clusterVirAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVirAddressType.setStatus("current")
_ClusterVirAddress_Type = InetAddress
_ClusterVirAddress_Object = MibTableColumn
clusterVirAddress = _ClusterVirAddress_Object(
    (1, 3, 6, 1, 4, 1, 7564, 18, 1, 3, 1, 12),
    _ClusterVirAddress_Type()
)
clusterVirAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVirAddress.setStatus("current")
_SlbMIB_ObjectIdentity = ObjectIdentity
slbMIB = _SlbMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 19)
)
_SlbGeneral_ObjectIdentity = ObjectIdentity
slbGeneral = _SlbGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1)
)
_RealServer_ObjectIdentity = ObjectIdentity
realServer = _RealServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 1)
)
_RsCount_Type = Integer32
_RsCount_Object = MibScalar
rsCount = _RsCount_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 1, 1),
    _RsCount_Type()
)
rsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCount.setStatus("current")
_RsTable_Object = MibTable
rsTable = _RsTable_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rsTable.setStatus("current")
_RsEntry_Object = MibTableRow
rsEntry = _RsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 1, 2, 1)
)
rsEntry.setIndexNames(
    (0, "CA-SNMP-MIB8", "rsIndex"),
)
if mibBuilder.loadTexts:
    rsEntry.setStatus("current")
_RsIndex_Type = Integer32
_RsIndex_Object = MibTableColumn
rsIndex = _RsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 1, 2, 1, 1),
    _RsIndex_Type()
)
rsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIndex.setStatus("current")
_RsID_Type = DisplayString
_RsID_Object = MibTableColumn
rsID = _RsID_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 1, 2, 1, 2),
    _RsID_Type()
)
rsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsID.setStatus("current")


class _RsProtocol_Type(Integer32):
    """Custom type rsProtocol based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("dns", 7),
          ("ftp", 2),
          ("ftps", 3),
          ("http", 4),
          ("https", 5),
          ("ip", 10),
          ("l2ip", 8),
          ("l2mac", 9),
          ("radacct", 13),
          ("radauth", 14),
          ("rdp", 17),
          ("rtsp", 15),
          ("siptcp", 11),
          ("sipudp", 12),
          ("tcp", 0),
          ("tcps", 6),
          ("udp", 1),
          ("vlink", 16))
    )


_RsProtocol_Type.__name__ = "Integer32"
_RsProtocol_Object = MibTableColumn
rsProtocol = _RsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 1, 2, 1, 3),
    _RsProtocol_Type()
)
rsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsProtocol.setStatus("current")
_RsIpAddr_Type = IpAddress
_RsIpAddr_Object = MibTableColumn
rsIpAddr = _RsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 1, 2, 1, 4),
    _RsIpAddr_Type()
)
rsIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpAddr.setStatus("current")


class _RsPort_Type(Integer32):
    """Custom type rsPort based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsPort_Type.__name__ = "Integer32"
_RsPort_Object = MibTableColumn
rsPort = _RsPort_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 1, 2, 1, 5),
    _RsPort_Type()
)
rsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPort.setStatus("current")


class _RsMaxConn_Type(Integer32):
    """Custom type rsMaxConn based on Integer32"""
    defaultValue = 1000


_RsMaxConn_Object = MibTableColumn
rsMaxConn = _RsMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 1, 2, 1, 6),
    _RsMaxConn_Type()
)
rsMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxConn.setStatus("current")


class _RsStatus_Type(Integer32):
    """Custom type rsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_RsStatus_Type.__name__ = "Integer32"
_RsStatus_Object = MibTableColumn
rsStatus = _RsStatus_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 1, 2, 1, 8),
    _RsStatus_Type()
)
rsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStatus.setStatus("current")
_RsAvgRespTime_Type = Integer32
_RsAvgRespTime_Object = MibTableColumn
rsAvgRespTime = _RsAvgRespTime_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 1, 2, 1, 9),
    _RsAvgRespTime_Type()
)
rsAvgRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAvgRespTime.setStatus("current")
_RsIpAddressType_Type = InetAddressType
_RsIpAddressType_Object = MibTableColumn
rsIpAddressType = _RsIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 1, 2, 1, 10),
    _RsIpAddressType_Type()
)
rsIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpAddressType.setStatus("current")
_RsIpAddress_Type = InetAddress
_RsIpAddress_Object = MibTableColumn
rsIpAddress = _RsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 1, 2, 1, 11),
    _RsIpAddress_Type()
)
rsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpAddress.setStatus("current")
_VirtualServer_ObjectIdentity = ObjectIdentity
virtualServer = _VirtualServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 2)
)
_VsCount_Type = Integer32
_VsCount_Object = MibScalar
vsCount = _VsCount_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 2, 1),
    _VsCount_Type()
)
vsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsCount.setStatus("current")
_VsTable_Object = MibTable
vsTable = _VsTable_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 2, 2)
)
if mibBuilder.loadTexts:
    vsTable.setStatus("current")
_VsEntry_Object = MibTableRow
vsEntry = _VsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 2, 2, 1)
)
vsEntry.setIndexNames(
    (0, "CA-SNMP-MIB8", "vsIndex"),
)
if mibBuilder.loadTexts:
    vsEntry.setStatus("current")
_VsIndex_Type = Integer32
_VsIndex_Object = MibTableColumn
vsIndex = _VsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 2, 2, 1, 1),
    _VsIndex_Type()
)
vsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsIndex.setStatus("current")
_VsID_Type = DisplayString
_VsID_Object = MibTableColumn
vsID = _VsID_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 2, 2, 1, 2),
    _VsID_Type()
)
vsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsID.setStatus("current")


class _VsProtocol_Type(Integer32):
    """Custom type vsProtocol based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("dns", 7),
          ("ftp", 2),
          ("ftps", 3),
          ("http", 4),
          ("https", 5),
          ("ip", 10),
          ("l2ip", 8),
          ("l2mac", 9),
          ("radacct", 13),
          ("radauth", 14),
          ("rdp", 17),
          ("rtsp", 15),
          ("siptcp", 11),
          ("sipudp", 12),
          ("tcp", 0),
          ("tcps", 6),
          ("udp", 1),
          ("vlink", 16))
    )


_VsProtocol_Type.__name__ = "Integer32"
_VsProtocol_Object = MibTableColumn
vsProtocol = _VsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 2, 2, 1, 3),
    _VsProtocol_Type()
)
vsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsProtocol.setStatus("current")
_VsIpAddr_Type = IpAddress
_VsIpAddr_Object = MibTableColumn
vsIpAddr = _VsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 2, 2, 1, 4),
    _VsIpAddr_Type()
)
vsIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsIpAddr.setStatus("current")


class _VsPort_Type(Integer32):
    """Custom type vsPort based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsPort_Type.__name__ = "Integer32"
_VsPort_Object = MibTableColumn
vsPort = _VsPort_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 2, 2, 1, 5),
    _VsPort_Type()
)
vsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsPort.setStatus("current")


class _VsMaxConn_Type(Integer32):
    """Custom type vsMaxConn based on Integer32"""
    defaultValue = 0


_VsMaxConn_Object = MibTableColumn
vsMaxConn = _VsMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 2, 2, 1, 6),
    _VsMaxConn_Type()
)
vsMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsMaxConn.setStatus("current")
_VsIpAddressType_Type = InetAddressType
_VsIpAddressType_Object = MibTableColumn
vsIpAddressType = _VsIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 2, 2, 1, 7),
    _VsIpAddressType_Type()
)
vsIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsIpAddressType.setStatus("current")
_VsIpAddress_Type = InetAddress
_VsIpAddress_Object = MibTableColumn
vsIpAddress = _VsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 2, 2, 1, 8),
    _VsIpAddress_Type()
)
vsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsIpAddress.setStatus("current")
_GroupCurCfg_ObjectIdentity = ObjectIdentity
groupCurCfg = _GroupCurCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 3)
)
_GroupCount_Type = Integer32
_GroupCount_Object = MibScalar
groupCount = _GroupCount_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 3, 1),
    _GroupCount_Type()
)
groupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupCount.setStatus("current")
_GpTable_Object = MibTable
gpTable = _GpTable_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gpTable.setStatus("current")
_GpEntry_Object = MibTableRow
gpEntry = _GpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 3, 2, 1)
)
gpEntry.setIndexNames(
    (0, "CA-SNMP-MIB8", "gpIndex"),
)
if mibBuilder.loadTexts:
    gpEntry.setStatus("current")
_GpIndex_Type = Integer32
_GpIndex_Object = MibTableColumn
gpIndex = _GpIndex_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 3, 2, 1, 1),
    _GpIndex_Type()
)
gpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpIndex.setStatus("current")
_GpID_Type = DisplayString
_GpID_Object = MibTableColumn
gpID = _GpID_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 3, 2, 1, 2),
    _GpID_Type()
)
gpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpID.setStatus("current")
_RealID_Type = DisplayString
_RealID_Object = MibTableColumn
realID = _RealID_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 3, 2, 1, 3),
    _RealID_Type()
)
realID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realID.setStatus("current")


class _GpMetrics_Type(Integer32):
    """Custom type gpMetrics based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("chh", 21),
          ("chi", 15),
          ("ec", 20),
          ("hc", 8),
          ("hh", 9),
          ("hi", 13),
          ("hip", 14),
          ("hq", 24),
          ("ic", 10),
          ("invalid", 0),
          ("lc", 2),
          ("pc", 7),
          ("persistence", 26),
          ("ph", 5),
          ("pi", 6),
          ("prox", 16),
          ("pu", 4),
          ("radchs", 23),
          ("radchu", 22),
          ("rc", 11),
          ("rdprt", 25),
          ("rr", 1),
          ("sipcid", 18),
          ("sipuid", 19),
          ("snmp", 17),
          ("sr", 3),
          ("sslsid", 12))
    )


_GpMetrics_Type.__name__ = "Integer32"
_GpMetrics_Object = MibTableColumn
gpMetrics = _GpMetrics_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 1, 3, 2, 1, 4),
    _GpMetrics_Type()
)
gpMetrics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpMetrics.setStatus("current")
_SlbStats_ObjectIdentity = ObjectIdentity
slbStats = _SlbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2)
)
_RealStats_ObjectIdentity = ObjectIdentity
realStats = _RealStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 1)
)
_RsStatsTable_Object = MibTable
rsStatsTable = _RsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rsStatsTable.setStatus("current")
_RsStatsEntry_Object = MibTableRow
rsStatsEntry = _RsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 1, 1, 1)
)
rsStatsEntry.setIndexNames(
    (0, "CA-SNMP-MIB8", "realIndex"),
)
if mibBuilder.loadTexts:
    rsStatsEntry.setStatus("current")
_RealIndex_Type = Integer32
_RealIndex_Object = MibTableColumn
realIndex = _RealIndex_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 1, 1, 1, 1),
    _RealIndex_Type()
)
realIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realIndex.setStatus("current")
_RealServerID_Type = DisplayString
_RealServerID_Object = MibTableColumn
realServerID = _RealServerID_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 1, 1, 1, 2),
    _RealServerID_Type()
)
realServerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerID.setStatus("current")
_RealAddr_Type = IpAddress
_RealAddr_Object = MibTableColumn
realAddr = _RealAddr_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 1, 1, 1, 3),
    _RealAddr_Type()
)
realAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realAddr.setStatus("current")


class _RealPort_Type(Integer32):
    """Custom type realPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RealPort_Type.__name__ = "Integer32"
_RealPort_Object = MibTableColumn
realPort = _RealPort_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 1, 1, 1, 4),
    _RealPort_Type()
)
realPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realPort.setStatus("current")
_RsCntOfReq_Type = Integer32
_RsCntOfReq_Object = MibTableColumn
rsCntOfReq = _RsCntOfReq_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 1, 1, 1, 5),
    _RsCntOfReq_Type()
)
rsCntOfReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCntOfReq.setStatus("current")
_RsConnCnt_Type = Integer32
_RsConnCnt_Object = MibTableColumn
rsConnCnt = _RsConnCnt_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 1, 1, 1, 6),
    _RsConnCnt_Type()
)
rsConnCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsConnCnt.setStatus("current")
_RsTotalHits_Type = Integer32
_RsTotalHits_Object = MibTableColumn
rsTotalHits = _RsTotalHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 1, 1, 1, 7),
    _RsTotalHits_Type()
)
rsTotalHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTotalHits.setStatus("current")


class _RealStatus_Type(Integer32):
    """Custom type realStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_RealStatus_Type.__name__ = "Integer32"
_RealStatus_Object = MibTableColumn
realStatus = _RealStatus_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 1, 1, 1, 8),
    _RealStatus_Type()
)
realStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realStatus.setStatus("current")
_RealAddressType_Type = InetAddressType
_RealAddressType_Object = MibTableColumn
realAddressType = _RealAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 1, 1, 1, 9),
    _RealAddressType_Type()
)
realAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realAddressType.setStatus("current")
_RealAddress_Type = InetAddress
_RealAddress_Object = MibTableColumn
realAddress = _RealAddress_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 1, 1, 1, 10),
    _RealAddress_Type()
)
realAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realAddress.setStatus("current")
_VirtualStats_ObjectIdentity = ObjectIdentity
virtualStats = _VirtualStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2)
)
_VsStatsTable_Object = MibTable
vsStatsTable = _VsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vsStatsTable.setStatus("current")
_VsStatsEntry_Object = MibTableRow
vsStatsEntry = _VsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1)
)
vsStatsEntry.setIndexNames(
    (0, "CA-SNMP-MIB8", "virtualIndex"),
)
if mibBuilder.loadTexts:
    vsStatsEntry.setStatus("current")
_VirtualIndex_Type = Integer32
_VirtualIndex_Object = MibTableColumn
virtualIndex = _VirtualIndex_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 1),
    _VirtualIndex_Type()
)
virtualIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualIndex.setStatus("current")
_VirtServerID_Type = DisplayString
_VirtServerID_Object = MibTableColumn
virtServerID = _VirtServerID_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 2),
    _VirtServerID_Type()
)
virtServerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtServerID.setStatus("current")
_VirtualAddr_Type = IpAddress
_VirtualAddr_Object = MibTableColumn
virtualAddr = _VirtualAddr_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 3),
    _VirtualAddr_Type()
)
virtualAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddr.setStatus("current")


class _VirtualPort_Type(Integer32):
    """Custom type virtualPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualPort_Type.__name__ = "Integer32"
_VirtualPort_Object = MibTableColumn
virtualPort = _VirtualPort_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 4),
    _VirtualPort_Type()
)
virtualPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualPort.setStatus("current")
_VsURLHits_Type = Integer32
_VsURLHits_Object = MibTableColumn
vsURLHits = _VsURLHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 5),
    _VsURLHits_Type()
)
vsURLHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsURLHits.setStatus("current")
_VsHostnameHits_Type = Integer32
_VsHostnameHits_Object = MibTableColumn
vsHostnameHits = _VsHostnameHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 6),
    _VsHostnameHits_Type()
)
vsHostnameHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsHostnameHits.setStatus("current")
_VsPerstntCookieHits_Type = Integer32
_VsPerstntCookieHits_Object = MibTableColumn
vsPerstntCookieHits = _VsPerstntCookieHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 7),
    _VsPerstntCookieHits_Type()
)
vsPerstntCookieHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsPerstntCookieHits.setStatus("current")
_VsQosCookieHits_Type = Integer32
_VsQosCookieHits_Object = MibTableColumn
vsQosCookieHits = _VsQosCookieHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 8),
    _VsQosCookieHits_Type()
)
vsQosCookieHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsQosCookieHits.setStatus("current")
_VsDefaultHits_Type = Integer32
_VsDefaultHits_Object = MibTableColumn
vsDefaultHits = _VsDefaultHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 9),
    _VsDefaultHits_Type()
)
vsDefaultHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsDefaultHits.setStatus("current")
_VsPerstntURLHits_Type = Integer32
_VsPerstntURLHits_Object = MibTableColumn
vsPerstntURLHits = _VsPerstntURLHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 10),
    _VsPerstntURLHits_Type()
)
vsPerstntURLHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsPerstntURLHits.setStatus("current")
_VsStaticHits_Type = Integer32
_VsStaticHits_Object = MibTableColumn
vsStaticHits = _VsStaticHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 11),
    _VsStaticHits_Type()
)
vsStaticHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsStaticHits.setStatus("current")
_VsQosNetworkHits_Type = Integer32
_VsQosNetworkHits_Object = MibTableColumn
vsQosNetworkHits = _VsQosNetworkHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 12),
    _VsQosNetworkHits_Type()
)
vsQosNetworkHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsQosNetworkHits.setStatus("current")
_VsQosURLHits_Type = Integer32
_VsQosURLHits_Object = MibTableColumn
vsQosURLHits = _VsQosURLHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 13),
    _VsQosURLHits_Type()
)
vsQosURLHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsQosURLHits.setStatus("current")
_VsBackupHits_Type = Integer32
_VsBackupHits_Object = MibTableColumn
vsBackupHits = _VsBackupHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 14),
    _VsBackupHits_Type()
)
vsBackupHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsBackupHits.setStatus("current")
_VsCacheHits_Type = Integer32
_VsCacheHits_Object = MibTableColumn
vsCacheHits = _VsCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 15),
    _VsCacheHits_Type()
)
vsCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsCacheHits.setStatus("current")
_VsRegexHits_Type = Integer32
_VsRegexHits_Object = MibTableColumn
vsRegexHits = _VsRegexHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 16),
    _VsRegexHits_Type()
)
vsRegexHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsRegexHits.setStatus("current")
_VsRCookieHits_Type = Integer32
_VsRCookieHits_Object = MibTableColumn
vsRCookieHits = _VsRCookieHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 17),
    _VsRCookieHits_Type()
)
vsRCookieHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsRCookieHits.setStatus("current")
_VsICookieHits_Type = Integer32
_VsICookieHits_Object = MibTableColumn
vsICookieHits = _VsICookieHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 18),
    _VsICookieHits_Type()
)
vsICookieHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsICookieHits.setStatus("current")
_VsConnCnt_Type = Integer32
_VsConnCnt_Object = MibTableColumn
vsConnCnt = _VsConnCnt_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 19),
    _VsConnCnt_Type()
)
vsConnCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsConnCnt.setStatus("current")
_VirtualAddressType_Type = InetAddressType
_VirtualAddressType_Object = MibTableColumn
virtualAddressType = _VirtualAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 20),
    _VirtualAddressType_Type()
)
virtualAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressType.setStatus("current")
_VirtualAddress_Type = InetAddress
_VirtualAddress_Object = MibTableColumn
virtualAddress = _VirtualAddress_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 21),
    _VirtualAddress_Type()
)
virtualAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddress.setStatus("current")
_VsQosClientPortHits_Type = Integer32
_VsQosClientPortHits_Object = MibTableColumn
vsQosClientPortHits = _VsQosClientPortHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 22),
    _VsQosClientPortHits_Type()
)
vsQosClientPortHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsQosClientPortHits.setStatus("current")
_VsQosBodyHits_Type = Integer32
_VsQosBodyHits_Object = MibTableColumn
vsQosBodyHits = _VsQosBodyHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 23),
    _VsQosBodyHits_Type()
)
vsQosBodyHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsQosBodyHits.setStatus("current")
_VsHeaderHits_Type = Integer32
_VsHeaderHits_Object = MibTableColumn
vsHeaderHits = _VsHeaderHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 24),
    _VsHeaderHits_Type()
)
vsHeaderHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsHeaderHits.setStatus("current")
_VsHashURLHits_Type = Integer32
_VsHashURLHits_Object = MibTableColumn
vsHashURLHits = _VsHashURLHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 25),
    _VsHashURLHits_Type()
)
vsHashURLHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsHashURLHits.setStatus("current")
_VsRedirectHits_Type = Integer32
_VsRedirectHits_Object = MibTableColumn
vsRedirectHits = _VsRedirectHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 2, 1, 1, 26),
    _VsRedirectHits_Type()
)
vsRedirectHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsRedirectHits.setStatus("current")
_GroupStats_ObjectIdentity = ObjectIdentity
groupStats = _GroupStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 3)
)
_GpStatsTable_Object = MibTable
gpStatsTable = _GpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 3, 1)
)
if mibBuilder.loadTexts:
    gpStatsTable.setStatus("current")
_GpStatsEntry_Object = MibTableRow
gpStatsEntry = _GpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 3, 1, 1)
)
gpStatsEntry.setIndexNames(
    (0, "CA-SNMP-MIB8", "groupIndex"),
)
if mibBuilder.loadTexts:
    gpStatsEntry.setStatus("current")
_GroupIndex_Type = Integer32
_GroupIndex_Object = MibTableColumn
groupIndex = _GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 3, 1, 1, 1),
    _GroupIndex_Type()
)
groupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupIndex.setStatus("current")
_GroupID_Type = DisplayString
_GroupID_Object = MibTableColumn
groupID = _GroupID_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 3, 1, 1, 2),
    _GroupID_Type()
)
groupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupID.setStatus("current")
_GpTotalHits_Type = Integer32
_GpTotalHits_Object = MibTableColumn
gpTotalHits = _GpTotalHits_Object(
    (1, 3, 6, 1, 4, 1, 7564, 19, 2, 3, 1, 1, 3),
    _GpTotalHits_Type()
)
gpTotalHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpTotalHits.setStatus("current")
_SslMIB_ObjectIdentity = ObjectIdentity
sslMIB = _SslMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 20)
)
_SslGeneral_ObjectIdentity = ObjectIdentity
sslGeneral = _SslGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 20, 1)
)


class _VhostNum_Type(Integer32):
    """Custom type vhostNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_VhostNum_Type.__name__ = "Integer32"
_VhostNum_Object = MibScalar
vhostNum = _VhostNum_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 1, 2),
    _VhostNum_Type()
)
vhostNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostNum.setStatus("current")
_SslStats_ObjectIdentity = ObjectIdentity
sslStats = _SslStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2)
)
_TotalOpenSSLConns_Type = Integer32
_TotalOpenSSLConns_Object = MibScalar
totalOpenSSLConns = _TotalOpenSSLConns_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2, 1),
    _TotalOpenSSLConns_Type()
)
totalOpenSSLConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOpenSSLConns.setStatus("current")
_TotalAcceptedConns_Type = Integer32
_TotalAcceptedConns_Object = MibScalar
totalAcceptedConns = _TotalAcceptedConns_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2, 2),
    _TotalAcceptedConns_Type()
)
totalAcceptedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalAcceptedConns.setStatus("current")
_TotalRequestedConns_Type = Integer32
_TotalRequestedConns_Object = MibScalar
totalRequestedConns = _TotalRequestedConns_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2, 3),
    _TotalRequestedConns_Type()
)
totalRequestedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRequestedConns.setStatus("current")
_SslTable_Object = MibTable
sslTable = _SslTable_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2, 4)
)
if mibBuilder.loadTexts:
    sslTable.setStatus("current")
_SslEntry_Object = MibTableRow
sslEntry = _SslEntry_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2, 4, 1)
)
sslEntry.setIndexNames(
    (0, "CA-SNMP-MIB8", "sslIndex"),
)
if mibBuilder.loadTexts:
    sslEntry.setStatus("current")
_SslIndex_Type = Integer32
_SslIndex_Object = MibTableColumn
sslIndex = _SslIndex_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2, 4, 1, 1),
    _SslIndex_Type()
)
sslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslIndex.setStatus("current")
_VhostName_Type = DisplayString
_VhostName_Object = MibTableColumn
vhostName = _VhostName_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2, 4, 1, 2),
    _VhostName_Type()
)
vhostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostName.setStatus("current")
_OpenSSLConns_Type = Integer32
_OpenSSLConns_Object = MibTableColumn
openSSLConns = _OpenSSLConns_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2, 4, 1, 3),
    _OpenSSLConns_Type()
)
openSSLConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openSSLConns.setStatus("current")
_AcceptedConns_Type = Integer32
_AcceptedConns_Object = MibTableColumn
acceptedConns = _AcceptedConns_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2, 4, 1, 4),
    _AcceptedConns_Type()
)
acceptedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptedConns.setStatus("current")
_RequestedConns_Type = Integer32
_RequestedConns_Object = MibTableColumn
requestedConns = _RequestedConns_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2, 4, 1, 5),
    _RequestedConns_Type()
)
requestedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    requestedConns.setStatus("current")
_ResumedSess_Type = Integer32
_ResumedSess_Object = MibTableColumn
resumedSess = _ResumedSess_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2, 4, 1, 6),
    _ResumedSess_Type()
)
resumedSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resumedSess.setStatus("current")
_ResumableSess_Type = Integer32
_ResumableSess_Object = MibTableColumn
resumableSess = _ResumableSess_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2, 4, 1, 7),
    _ResumableSess_Type()
)
resumableSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resumableSess.setStatus("current")
_MissSess_Type = Integer32
_MissSess_Object = MibTableColumn
missSess = _MissSess_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2, 4, 1, 8),
    _MissSess_Type()
)
missSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    missSess.setStatus("current")
_ConnsPerSec_Type = Integer32
_ConnsPerSec_Object = MibTableColumn
connsPerSec = _ConnsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 7564, 20, 2, 4, 1, 9),
    _ConnsPerSec_Type()
)
connsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connsPerSec.setStatus("current")
_VipStats_ObjectIdentity = ObjectIdentity
vipStats = _VipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 22)
)


class _VipStatus_Type(Integer32):
    """Custom type vipStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_VipStatus_Type.__name__ = "Integer32"
_VipStatus_Object = MibScalar
vipStatus = _VipStatus_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 1),
    _VipStatus_Type()
)
vipStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipStatus.setStatus("current")
_HostName_Type = DisplayString
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("current")
_CurrentTime_Type = DisplayString
_CurrentTime_Object = MibScalar
currentTime = _CurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 3),
    _CurrentTime_Type()
)
currentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentTime.setStatus("current")
_TotalIPPktsIn_Type = Counter64
_TotalIPPktsIn_Object = MibScalar
totalIPPktsIn = _TotalIPPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 4),
    _TotalIPPktsIn_Type()
)
totalIPPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalIPPktsIn.setStatus("current")
_TotalIPPktsOut_Type = Counter64
_TotalIPPktsOut_Object = MibScalar
totalIPPktsOut = _TotalIPPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 5),
    _TotalIPPktsOut_Type()
)
totalIPPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalIPPktsOut.setStatus("current")
_TotalIPBytesIn_Type = Counter64
_TotalIPBytesIn_Object = MibScalar
totalIPBytesIn = _TotalIPBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 6),
    _TotalIPBytesIn_Type()
)
totalIPBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalIPBytesIn.setStatus("current")
_TotalIPBytesOut_Type = Counter64
_TotalIPBytesOut_Object = MibScalar
totalIPBytesOut = _TotalIPBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 7),
    _TotalIPBytesOut_Type()
)
totalIPBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalIPBytesOut.setStatus("current")
_IpStatsTable_Object = MibTable
ipStatsTable = _IpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 8)
)
if mibBuilder.loadTexts:
    ipStatsTable.setStatus("current")
_IpStatsEntry_Object = MibTableRow
ipStatsEntry = _IpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 8, 1)
)
ipStatsEntry.setIndexNames(
    (0, "CA-SNMP-MIB8", "ipAddrType"),
    (0, "CA-SNMP-MIB8", "ipAddr"),
)
if mibBuilder.loadTexts:
    ipStatsEntry.setStatus("current")
_IpIndex_Type = Integer32
_IpIndex_Object = MibTableColumn
ipIndex = _IpIndex_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 8, 1, 1),
    _IpIndex_Type()
)
ipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIndex.setStatus("current")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibTableColumn
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 8, 1, 2),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_IpPktsIn_Type = Counter64
_IpPktsIn_Object = MibTableColumn
ipPktsIn = _IpPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 8, 1, 3),
    _IpPktsIn_Type()
)
ipPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPktsIn.setStatus("current")
_IpBytesIn_Type = Counter64
_IpBytesIn_Object = MibTableColumn
ipBytesIn = _IpBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 8, 1, 4),
    _IpBytesIn_Type()
)
ipBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBytesIn.setStatus("current")
_IpPktsOut_Type = Counter64
_IpPktsOut_Object = MibTableColumn
ipPktsOut = _IpPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 8, 1, 5),
    _IpPktsOut_Type()
)
ipPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPktsOut.setStatus("current")
_IpBytesOut_Type = Counter64
_IpBytesOut_Object = MibTableColumn
ipBytesOut = _IpBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 8, 1, 6),
    _IpBytesOut_Type()
)
ipBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBytesOut.setStatus("current")
_StartTime_Type = DisplayString
_StartTime_Object = MibTableColumn
startTime = _StartTime_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 8, 1, 7),
    _StartTime_Type()
)
startTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startTime.setStatus("current")
_IpAddrType_Type = InetAddressType
_IpAddrType_Object = MibTableColumn
ipAddrType = _IpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 8, 1, 8),
    _IpAddrType_Type()
)
ipAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddrType.setStatus("current")
_IpAddr_Type = InetAddress
_IpAddr_Object = MibTableColumn
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7564, 22, 8, 1, 9),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddr.setStatus("current")
_IfTraffic_ObjectIdentity = ObjectIdentity
ifTraffic = _IfTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 23)
)
_InfNumber_Type = Integer32
_InfNumber_Object = MibScalar
infNumber = _InfNumber_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 1),
    _InfNumber_Type()
)
infNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infNumber.setStatus("current")
_InfTotalInOctets_Type = Counter64
_InfTotalInOctets_Object = MibScalar
infTotalInOctets = _InfTotalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 2),
    _InfTotalInOctets_Type()
)
infTotalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infTotalInOctets.setStatus("current")
_InfTotalOutOctets_Type = Counter64
_InfTotalOutOctets_Object = MibScalar
infTotalOutOctets = _InfTotalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 3),
    _InfTotalOutOctets_Type()
)
infTotalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infTotalOutOctets.setStatus("current")
_InfTable_Object = MibTable
infTable = _InfTable_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4)
)
if mibBuilder.loadTexts:
    infTable.setStatus("current")
_InfEntry_Object = MibTableRow
infEntry = _InfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1)
)
infEntry.setIndexNames(
    (0, "CA-SNMP-MIB8", "infIndex"),
)
if mibBuilder.loadTexts:
    infEntry.setStatus("current")
_InfIndex_Type = Integer32
_InfIndex_Object = MibTableColumn
infIndex = _InfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 1),
    _InfIndex_Type()
)
infIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infIndex.setStatus("current")


class _InfDescr_Type(DisplayString):
    """Custom type infDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InfDescr_Type.__name__ = "DisplayString"
_InfDescr_Object = MibTableColumn
infDescr = _InfDescr_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 2),
    _InfDescr_Type()
)
infDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infDescr.setStatus("current")


class _InfOperStatus_Type(Integer32):
    """Custom type infOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_InfOperStatus_Type.__name__ = "Integer32"
_InfOperStatus_Object = MibTableColumn
infOperStatus = _InfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 3),
    _InfOperStatus_Type()
)
infOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infOperStatus.setStatus("current")
_InfAddress_Type = IpAddress
_InfAddress_Object = MibTableColumn
infAddress = _InfAddress_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 4),
    _InfAddress_Type()
)
infAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infAddress.setStatus("current")
_InfInOctets_Type = Counter64
_InfInOctets_Object = MibTableColumn
infInOctets = _InfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 5),
    _InfInOctets_Type()
)
infInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infInOctets.setStatus("current")
_InfInUcastPkts_Type = Counter64
_InfInUcastPkts_Object = MibTableColumn
infInUcastPkts = _InfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 6),
    _InfInUcastPkts_Type()
)
infInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infInUcastPkts.setStatus("current")
_InfInNUcastPkts_Type = Counter64
_InfInNUcastPkts_Object = MibTableColumn
infInNUcastPkts = _InfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 7),
    _InfInNUcastPkts_Type()
)
infInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infInNUcastPkts.setStatus("deprecated")
_InfInDiscards_Type = Counter64
_InfInDiscards_Object = MibTableColumn
infInDiscards = _InfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 8),
    _InfInDiscards_Type()
)
infInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infInDiscards.setStatus("current")
_InfInErrors_Type = Counter64
_InfInErrors_Object = MibTableColumn
infInErrors = _InfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 9),
    _InfInErrors_Type()
)
infInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infInErrors.setStatus("current")
_InfInUnknownProtos_Type = Counter64
_InfInUnknownProtos_Object = MibTableColumn
infInUnknownProtos = _InfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 10),
    _InfInUnknownProtos_Type()
)
infInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infInUnknownProtos.setStatus("current")
_InfOutOctets_Type = Counter64
_InfOutOctets_Object = MibTableColumn
infOutOctets = _InfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 11),
    _InfOutOctets_Type()
)
infOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infOutOctets.setStatus("current")
_InfOutUcastPkts_Type = Counter64
_InfOutUcastPkts_Object = MibTableColumn
infOutUcastPkts = _InfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 12),
    _InfOutUcastPkts_Type()
)
infOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infOutUcastPkts.setStatus("current")
_InfOutNUcastPkts_Type = Counter64
_InfOutNUcastPkts_Object = MibTableColumn
infOutNUcastPkts = _InfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 13),
    _InfOutNUcastPkts_Type()
)
infOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infOutNUcastPkts.setStatus("deprecated")
_InfOutErrors_Type = Counter64
_InfOutErrors_Object = MibTableColumn
infOutErrors = _InfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 14),
    _InfOutErrors_Type()
)
infOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infOutErrors.setStatus("current")
_InfIpv4AddressType_Type = InetAddressType
_InfIpv4AddressType_Object = MibTableColumn
infIpv4AddressType = _InfIpv4AddressType_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 15),
    _InfIpv4AddressType_Type()
)
infIpv4AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infIpv4AddressType.setStatus("current")
_InfIpv4Address_Type = InetAddress
_InfIpv4Address_Object = MibTableColumn
infIpv4Address = _InfIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 16),
    _InfIpv4Address_Type()
)
infIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infIpv4Address.setStatus("current")
_InfIpv6AddressType_Type = InetAddressType
_InfIpv6AddressType_Object = MibTableColumn
infIpv6AddressType = _InfIpv6AddressType_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 17),
    _InfIpv6AddressType_Type()
)
infIpv6AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infIpv6AddressType.setStatus("current")
_InfIpv6Address_Type = InetAddress
_InfIpv6Address_Object = MibTableColumn
infIpv6Address = _InfIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 18),
    _InfIpv6Address_Type()
)
infIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infIpv6Address.setStatus("current")
_InfInBandwidth_Type = Counter64
_InfInBandwidth_Object = MibTableColumn
infInBandwidth = _InfInBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 19),
    _InfInBandwidth_Type()
)
infInBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infInBandwidth.setStatus("deprecated")
_InfOutBandwidth_Type = Counter64
_InfOutBandwidth_Object = MibTableColumn
infOutBandwidth = _InfOutBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 20),
    _InfOutBandwidth_Type()
)
infOutBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infOutBandwidth.setStatus("deprecated")
_InfInMcastPkts_Type = Counter64
_InfInMcastPkts_Object = MibTableColumn
infInMcastPkts = _InfInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 21),
    _InfInMcastPkts_Type()
)
infInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infInMcastPkts.setStatus("current")
_InfOutMcastPkts_Type = Counter64
_InfOutMcastPkts_Object = MibTableColumn
infOutMcastPkts = _InfOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 22),
    _InfOutMcastPkts_Type()
)
infOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infOutMcastPkts.setStatus("current")
_InfInBcastPkts_Type = Counter64
_InfInBcastPkts_Object = MibTableColumn
infInBcastPkts = _InfInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 23),
    _InfInBcastPkts_Type()
)
infInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infInBcastPkts.setStatus("current")
_InfOutBcastPkts_Type = Counter64
_InfOutBcastPkts_Object = MibTableColumn
infOutBcastPkts = _InfOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7564, 23, 4, 1, 24),
    _InfOutBcastPkts_Type()
)
infOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infOutBcastPkts.setStatus("current")
_CaSyslog_ObjectIdentity = ObjectIdentity
caSyslog = _CaSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 24)
)
_LogBasic_ObjectIdentity = ObjectIdentity
logBasic = _LogBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 24, 1)
)
_LogNotificationsSent_Type = Counter32
_LogNotificationsSent_Object = MibScalar
logNotificationsSent = _LogNotificationsSent_Object(
    (1, 3, 6, 1, 4, 1, 7564, 24, 1, 1),
    _LogNotificationsSent_Type()
)
logNotificationsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logNotificationsSent.setStatus("current")
if mibBuilder.loadTexts:
    logNotificationsSent.setUnits("notifications")


class _LogNotificationsEnabled_Type(Integer32):
    """Custom type logNotificationsEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LogNotificationsEnabled_Type.__name__ = "Integer32"
_LogNotificationsEnabled_Object = MibScalar
logNotificationsEnabled = _LogNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7564, 24, 1, 2),
    _LogNotificationsEnabled_Type()
)
logNotificationsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logNotificationsEnabled.setStatus("current")


class _LogMaxSeverity_Type(SyslogSeverity):
    """Custom type logMaxSeverity based on SyslogSeverity"""


_LogMaxSeverity_Object = MibScalar
logMaxSeverity = _LogMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7564, 24, 1, 3),
    _LogMaxSeverity_Type()
)
logMaxSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMaxSeverity.setStatus("current")
_LogHistory_ObjectIdentity = ObjectIdentity
logHistory = _LogHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 24, 2)
)


class _LogHistTableMaxLength_Type(Integer32):
    """Custom type logHistTableMaxLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_LogHistTableMaxLength_Type.__name__ = "Integer32"
_LogHistTableMaxLength_Object = MibScalar
logHistTableMaxLength = _LogHistTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 7564, 24, 2, 1),
    _LogHistTableMaxLength_Type()
)
logHistTableMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logHistTableMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    logHistTableMaxLength.setUnits("entries")
_LogHistoryTable_Object = MibTable
logHistoryTable = _LogHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 7564, 24, 2, 2)
)
if mibBuilder.loadTexts:
    logHistoryTable.setStatus("current")
_LogHistoryEntry_Object = MibTableRow
logHistoryEntry = _LogHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 7564, 24, 2, 2, 1)
)
logHistoryEntry.setIndexNames(
    (0, "CA-SNMP-MIB8", "index"),
)
if mibBuilder.loadTexts:
    logHistoryEntry.setStatus("current")
_Index_Type = Integer32
_Index_Object = MibTableColumn
index = _Index_Object(
    (1, 3, 6, 1, 4, 1, 7564, 24, 2, 2, 1, 1),
    _Index_Type()
)
index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    index.setStatus("current")
_Severity_Type = SyslogSeverity
_Severity_Object = MibTableColumn
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 7564, 24, 2, 2, 1, 2),
    _Severity_Type()
)
severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severity.setStatus("current")


class _MsgText_Type(DisplayString):
    """Custom type msgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MsgText_Type.__name__ = "DisplayString"
_MsgText_Object = MibTableColumn
msgText = _MsgText_Object(
    (1, 3, 6, 1, 4, 1, 7564, 24, 2, 2, 1, 3),
    _MsgText_Type()
)
msgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgText.setStatus("current")
_CaSyslogTrap_ObjectIdentity = ObjectIdentity
caSyslogTrap = _CaSyslogTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 24, 3)
)
_ClickTcp_ObjectIdentity = ObjectIdentity
clickTcp = _ClickTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 25)
)
_CtcpActiveOpens_Type = Counter32
_CtcpActiveOpens_Object = MibScalar
ctcpActiveOpens = _CtcpActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 1),
    _CtcpActiveOpens_Type()
)
ctcpActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpActiveOpens.setStatus("current")
_CtcpPassiveOpens_Type = Counter32
_CtcpPassiveOpens_Object = MibScalar
ctcpPassiveOpens = _CtcpPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 2),
    _CtcpPassiveOpens_Type()
)
ctcpPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpPassiveOpens.setStatus("current")
_CtcpAttemptFails_Type = Counter32
_CtcpAttemptFails_Object = MibScalar
ctcpAttemptFails = _CtcpAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 3),
    _CtcpAttemptFails_Type()
)
ctcpAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpAttemptFails.setStatus("current")
_CtcpEstabResets_Type = Counter32
_CtcpEstabResets_Object = MibScalar
ctcpEstabResets = _CtcpEstabResets_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 4),
    _CtcpEstabResets_Type()
)
ctcpEstabResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpEstabResets.setStatus("current")
_CtcpCurrEstab_Type = Gauge32
_CtcpCurrEstab_Object = MibScalar
ctcpCurrEstab = _CtcpCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 5),
    _CtcpCurrEstab_Type()
)
ctcpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpCurrEstab.setStatus("current")
_CtcpInSegs_Type = Counter32
_CtcpInSegs_Object = MibScalar
ctcpInSegs = _CtcpInSegs_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 6),
    _CtcpInSegs_Type()
)
ctcpInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpInSegs.setStatus("current")
_CtcpOutSegs_Type = Counter32
_CtcpOutSegs_Object = MibScalar
ctcpOutSegs = _CtcpOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 7),
    _CtcpOutSegs_Type()
)
ctcpOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpOutSegs.setStatus("current")
_CtcpRetransSegs_Type = Counter32
_CtcpRetransSegs_Object = MibScalar
ctcpRetransSegs = _CtcpRetransSegs_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 8),
    _CtcpRetransSegs_Type()
)
ctcpRetransSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpRetransSegs.setStatus("current")
_CtcpInErrs_Type = Counter32
_CtcpInErrs_Object = MibScalar
ctcpInErrs = _CtcpInErrs_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 9),
    _CtcpInErrs_Type()
)
ctcpInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpInErrs.setStatus("current")
_CtcpOutRsts_Type = Counter32
_CtcpOutRsts_Object = MibScalar
ctcpOutRsts = _CtcpOutRsts_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 10),
    _CtcpOutRsts_Type()
)
ctcpOutRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpOutRsts.setStatus("current")
_CtcpConnTable_Object = MibTable
ctcpConnTable = _CtcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 11)
)
if mibBuilder.loadTexts:
    ctcpConnTable.setStatus("current")
_CtcpConnEntry_Object = MibTableRow
ctcpConnEntry = _CtcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 11, 1)
)
ctcpConnEntry.setIndexNames(
    (0, "CA-SNMP-MIB8", "ctcpIndex"),
)
if mibBuilder.loadTexts:
    ctcpConnEntry.setStatus("current")
_CtcpIndex_Type = Integer32
_CtcpIndex_Object = MibTableColumn
ctcpIndex = _CtcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 11, 1, 1),
    _CtcpIndex_Type()
)
ctcpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpIndex.setStatus("current")


class _CtcpConnState_Type(Integer32):
    """Custom type ctcpConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("closeWait", 8),
          ("closed", 1),
          ("closing", 10),
          ("deleteTCB", 12),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("lastAck", 9),
          ("listen", 2),
          ("synReceived", 4),
          ("synSent", 3),
          ("timeWait", 11))
    )


_CtcpConnState_Type.__name__ = "Integer32"
_CtcpConnState_Object = MibTableColumn
ctcpConnState = _CtcpConnState_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 11, 1, 2),
    _CtcpConnState_Type()
)
ctcpConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpConnState.setStatus("current")
_CtcpConnLocalAddress_Type = IpAddress
_CtcpConnLocalAddress_Object = MibTableColumn
ctcpConnLocalAddress = _CtcpConnLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 11, 1, 3),
    _CtcpConnLocalAddress_Type()
)
ctcpConnLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpConnLocalAddress.setStatus("current")


class _CtcpConnLocalPort_Type(Integer32):
    """Custom type ctcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CtcpConnLocalPort_Type.__name__ = "Integer32"
_CtcpConnLocalPort_Object = MibTableColumn
ctcpConnLocalPort = _CtcpConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 11, 1, 4),
    _CtcpConnLocalPort_Type()
)
ctcpConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpConnLocalPort.setStatus("current")
_CtcpConnRemAddress_Type = IpAddress
_CtcpConnRemAddress_Object = MibTableColumn
ctcpConnRemAddress = _CtcpConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 11, 1, 5),
    _CtcpConnRemAddress_Type()
)
ctcpConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpConnRemAddress.setStatus("current")


class _CtcpConnRemPort_Type(Integer32):
    """Custom type ctcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CtcpConnRemPort_Type.__name__ = "Integer32"
_CtcpConnRemPort_Object = MibTableColumn
ctcpConnRemPort = _CtcpConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 11, 1, 6),
    _CtcpConnRemPort_Type()
)
ctcpConnRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpConnRemPort.setStatus("current")
_CtcpConnLocalAddrType_Type = InetAddressType
_CtcpConnLocalAddrType_Object = MibTableColumn
ctcpConnLocalAddrType = _CtcpConnLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 11, 1, 7),
    _CtcpConnLocalAddrType_Type()
)
ctcpConnLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpConnLocalAddrType.setStatus("current")
_CtcpConnLocalAddr_Type = InetAddress
_CtcpConnLocalAddr_Object = MibTableColumn
ctcpConnLocalAddr = _CtcpConnLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 11, 1, 8),
    _CtcpConnLocalAddr_Type()
)
ctcpConnLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpConnLocalAddr.setStatus("current")
_CtcpConnRemAddrType_Type = InetAddressType
_CtcpConnRemAddrType_Object = MibTableColumn
ctcpConnRemAddrType = _CtcpConnRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 11, 1, 9),
    _CtcpConnRemAddrType_Type()
)
ctcpConnRemAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpConnRemAddrType.setStatus("current")
_CtcpConnRemAddr_Type = InetAddress
_CtcpConnRemAddr_Object = MibTableColumn
ctcpConnRemAddr = _CtcpConnRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 7564, 25, 11, 1, 10),
    _CtcpConnRemAddr_Type()
)
ctcpConnRemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcpConnRemAddr.setStatus("current")
_HealthCheck_ObjectIdentity = ObjectIdentity
healthCheck = _HealthCheck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 27)
)
_HcStats_ObjectIdentity = ObjectIdentity
hcStats = _HcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1)
)
_HcRSCount_Type = Integer32
_HcRSCount_Object = MibScalar
hcRSCount = _HcRSCount_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 1),
    _HcRSCount_Type()
)
hcRSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcRSCount.setStatus("current")
_HcStatsTable_Object = MibTable
hcStatsTable = _HcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2)
)
if mibBuilder.loadTexts:
    hcStatsTable.setStatus("current")
_HcStatsEntry_Object = MibTableRow
hcStatsEntry = _HcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2, 1)
)
hcStatsEntry.setIndexNames(
    (0, "CA-SNMP-MIB8", "hcIndex"),
)
if mibBuilder.loadTexts:
    hcStatsEntry.setStatus("current")
_HcIndex_Type = Integer32
_HcIndex_Object = MibTableColumn
hcIndex = _HcIndex_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2, 1, 1),
    _HcIndex_Type()
)
hcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcIndex.setStatus("current")
_HcName_Type = DisplayString
_HcName_Object = MibTableColumn
hcName = _HcName_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2, 1, 2),
    _HcName_Type()
)
hcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcName.setStatus("current")
_HcAddr_Type = IpAddress
_HcAddr_Object = MibTableColumn
hcAddr = _HcAddr_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2, 1, 3),
    _HcAddr_Type()
)
hcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcAddr.setStatus("current")


class _HcPort_Type(Integer32):
    """Custom type hcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HcPort_Type.__name__ = "Integer32"
_HcPort_Object = MibTableColumn
hcPort = _HcPort_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2, 1, 4),
    _HcPort_Type()
)
hcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcPort.setStatus("current")


class _HcStatus_Type(Integer32):
    """Custom type hcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_HcStatus_Type.__name__ = "Integer32"
_HcStatus_Object = MibTableColumn
hcStatus = _HcStatus_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2, 1, 5),
    _HcStatus_Type()
)
hcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcStatus.setStatus("current")
_HcCause_Type = DisplayString
_HcCause_Object = MibTableColumn
hcCause = _HcCause_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2, 1, 6),
    _HcCause_Type()
)
hcCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcCause.setStatus("current")
_HcNumDowns_Type = Integer32
_HcNumDowns_Object = MibTableColumn
hcNumDowns = _HcNumDowns_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2, 1, 7),
    _HcNumDowns_Type()
)
hcNumDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcNumDowns.setStatus("current")
_HcNumUps_Type = Integer32
_HcNumUps_Object = MibTableColumn
hcNumUps = _HcNumUps_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2, 1, 8),
    _HcNumUps_Type()
)
hcNumUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcNumUps.setStatus("current")
_HcConnAttempt_Type = Integer32
_HcConnAttempt_Object = MibTableColumn
hcConnAttempt = _HcConnAttempt_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2, 1, 9),
    _HcConnAttempt_Type()
)
hcConnAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcConnAttempt.setStatus("current")
_HcConnSuccess_Type = Integer32
_HcConnSuccess_Object = MibTableColumn
hcConnSuccess = _HcConnSuccess_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2, 1, 10),
    _HcConnSuccess_Type()
)
hcConnSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcConnSuccess.setStatus("current")
_HcConnFail_Type = Integer32
_HcConnFail_Object = MibTableColumn
hcConnFail = _HcConnFail_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2, 1, 11),
    _HcConnFail_Type()
)
hcConnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcConnFail.setStatus("current")
_HcAddressType_Type = InetAddressType
_HcAddressType_Object = MibTableColumn
hcAddressType = _HcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2, 1, 12),
    _HcAddressType_Type()
)
hcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcAddressType.setStatus("current")
_HcAddress_Type = InetAddress
_HcAddress_Object = MibTableColumn
hcAddress = _HcAddress_Object(
    (1, 3, 6, 1, 4, 1, 7564, 27, 1, 2, 1, 13),
    _HcAddress_Type()
)
hcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcAddress.setStatus("current")
_Compression_ObjectIdentity = ObjectIdentity
compression = _Compression_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 28)
)
_TotalBytesRcvd_Type = Counter64
_TotalBytesRcvd_Object = MibScalar
totalBytesRcvd = _TotalBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 7564, 28, 1),
    _TotalBytesRcvd_Type()
)
totalBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesRcvd.setStatus("current")
_TotalBytesSent_Type = Counter64
_TotalBytesSent_Object = MibScalar
totalBytesSent = _TotalBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 7564, 28, 2),
    _TotalBytesSent_Type()
)
totalBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalBytesSent.setStatus("current")
_RcvdBytesPerSec_Type = Counter64
_RcvdBytesPerSec_Object = MibScalar
rcvdBytesPerSec = _RcvdBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 7564, 28, 3),
    _RcvdBytesPerSec_Type()
)
rcvdBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvdBytesPerSec.setStatus("current")
_SentBytesPerSec_Type = Counter64
_SentBytesPerSec_Object = MibScalar
sentBytesPerSec = _SentBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 7564, 28, 4),
    _SentBytesPerSec_Type()
)
sentBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sentBytesPerSec.setStatus("current")
_PeakRcvdBytesPerSec_Type = Counter64
_PeakRcvdBytesPerSec_Object = MibScalar
peakRcvdBytesPerSec = _PeakRcvdBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 7564, 28, 5),
    _PeakRcvdBytesPerSec_Type()
)
peakRcvdBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakRcvdBytesPerSec.setStatus("current")
_PeakSentBytesPerSec_Type = Counter64
_PeakSentBytesPerSec_Object = MibScalar
peakSentBytesPerSec = _PeakSentBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 7564, 28, 6),
    _PeakSentBytesPerSec_Type()
)
peakSentBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakSentBytesPerSec.setStatus("current")
_ActiveTransac_Type = Counter64
_ActiveTransac_Object = MibScalar
activeTransac = _ActiveTransac_Object(
    (1, 3, 6, 1, 4, 1, 7564, 28, 7),
    _ActiveTransac_Type()
)
activeTransac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTransac.setStatus("current")
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 30)
)
_CpuUtilization_Type = Gauge32
_CpuUtilization_Object = MibScalar
cpuUtilization = _CpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 7564, 30, 1),
    _CpuUtilization_Type()
)
cpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilization.setStatus("current")
_ConnectionsPerSec_Type = Gauge32
_ConnectionsPerSec_Object = MibScalar
connectionsPerSec = _ConnectionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 7564, 30, 2),
    _ConnectionsPerSec_Type()
)
connectionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionsPerSec.setStatus("current")
_RequestsPerSec_Type = Gauge32
_RequestsPerSec_Object = MibScalar
requestsPerSec = _RequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 7564, 30, 3),
    _RequestsPerSec_Type()
)
requestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    requestsPerSec.setStatus("current")
_Sdns_ObjectIdentity = ObjectIdentity
sdns = _Sdns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 31)
)
_TotalReq_Type = Counter32
_TotalReq_Object = MibScalar
totalReq = _TotalReq_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 1),
    _TotalReq_Type()
)
totalReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalReq.setStatus("current")
_TotalSucc_Type = Counter32
_TotalSucc_Object = MibScalar
totalSucc = _TotalSucc_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 2),
    _TotalSucc_Type()
)
totalSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalSucc.setStatus("current")
_TotalFail_Type = Counter32
_TotalFail_Object = MibScalar
totalFail = _TotalFail_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 3),
    _TotalFail_Type()
)
totalFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalFail.setStatus("current")
_ReqLastSec_Type = Counter32
_ReqLastSec_Object = MibScalar
reqLastSec = _ReqLastSec_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 4),
    _ReqLastSec_Type()
)
reqLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqLastSec.setStatus("current")
_SuccLastSec_Type = Counter32
_SuccLastSec_Object = MibScalar
succLastSec = _SuccLastSec_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 5),
    _SuccLastSec_Type()
)
succLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    succLastSec.setStatus("current")
_FailLastSec_Type = Counter32
_FailLastSec_Object = MibScalar
failLastSec = _FailLastSec_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 6),
    _FailLastSec_Type()
)
failLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLastSec.setStatus("current")
_ReqPeakSec_Type = Counter32
_ReqPeakSec_Object = MibScalar
reqPeakSec = _ReqPeakSec_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 7),
    _ReqPeakSec_Type()
)
reqPeakSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqPeakSec.setStatus("current")
_SuccPeakSec_Type = Counter32
_SuccPeakSec_Object = MibScalar
succPeakSec = _SuccPeakSec_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 8),
    _SuccPeakSec_Type()
)
succPeakSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    succPeakSec.setStatus("current")
_ReqLastMin_Type = Counter32
_ReqLastMin_Object = MibScalar
reqLastMin = _ReqLastMin_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 9),
    _ReqLastMin_Type()
)
reqLastMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqLastMin.setStatus("current")
_SuccLastMin_Type = Counter32
_SuccLastMin_Object = MibScalar
succLastMin = _SuccLastMin_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 10),
    _SuccLastMin_Type()
)
succLastMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    succLastMin.setStatus("current")
_FailLastMin_Type = Counter32
_FailLastMin_Object = MibScalar
failLastMin = _FailLastMin_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 11),
    _FailLastMin_Type()
)
failLastMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLastMin.setStatus("current")
_ReqPeakMin_Type = Counter32
_ReqPeakMin_Object = MibScalar
reqPeakMin = _ReqPeakMin_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 12),
    _ReqPeakMin_Type()
)
reqPeakMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqPeakMin.setStatus("current")
_SuccPeakMin_Type = Counter32
_SuccPeakMin_Object = MibScalar
succPeakMin = _SuccPeakMin_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 13),
    _SuccPeakMin_Type()
)
succPeakMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    succPeakMin.setStatus("current")
_ReqLastHour_Type = Counter32
_ReqLastHour_Object = MibScalar
reqLastHour = _ReqLastHour_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 14),
    _ReqLastHour_Type()
)
reqLastHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqLastHour.setStatus("current")
_SuccLastHour_Type = Counter32
_SuccLastHour_Object = MibScalar
succLastHour = _SuccLastHour_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 15),
    _SuccLastHour_Type()
)
succLastHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    succLastHour.setStatus("current")
_FailLastHour_Type = Counter32
_FailLastHour_Object = MibScalar
failLastHour = _FailLastHour_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 16),
    _FailLastHour_Type()
)
failLastHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLastHour.setStatus("current")
_ReqPeakHour_Type = Counter32
_ReqPeakHour_Object = MibScalar
reqPeakHour = _ReqPeakHour_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 17),
    _ReqPeakHour_Type()
)
reqPeakHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqPeakHour.setStatus("current")
_SuccPeakHour_Type = Counter32
_SuccPeakHour_Object = MibScalar
succPeakHour = _SuccPeakHour_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 18),
    _SuccPeakHour_Type()
)
succPeakHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    succPeakHour.setStatus("current")
_ReqLastDay_Type = Counter32
_ReqLastDay_Object = MibScalar
reqLastDay = _ReqLastDay_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 19),
    _ReqLastDay_Type()
)
reqLastDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqLastDay.setStatus("current")
_SuccLastDay_Type = Counter32
_SuccLastDay_Object = MibScalar
succLastDay = _SuccLastDay_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 20),
    _SuccLastDay_Type()
)
succLastDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    succLastDay.setStatus("current")
_FailLastDay_Type = Counter32
_FailLastDay_Object = MibScalar
failLastDay = _FailLastDay_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 21),
    _FailLastDay_Type()
)
failLastDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLastDay.setStatus("current")
_ReqPeakDay_Type = Counter32
_ReqPeakDay_Object = MibScalar
reqPeakDay = _ReqPeakDay_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 22),
    _ReqPeakDay_Type()
)
reqPeakDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqPeakDay.setStatus("current")
_SuccPeakDay_Type = Counter32
_SuccPeakDay_Object = MibScalar
succPeakDay = _SuccPeakDay_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 23),
    _SuccPeakDay_Type()
)
succPeakDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    succPeakDay.setStatus("current")
_ReqLastSec5_Type = Counter32
_ReqLastSec5_Object = MibScalar
reqLastSec5 = _ReqLastSec5_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 24),
    _ReqLastSec5_Type()
)
reqLastSec5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqLastSec5.setStatus("current")
_SuccLastSec5_Type = Counter32
_SuccLastSec5_Object = MibScalar
succLastSec5 = _SuccLastSec5_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 25),
    _SuccLastSec5_Type()
)
succLastSec5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    succLastSec5.setStatus("current")
_FailLastSec5_Type = Counter32
_FailLastSec5_Object = MibScalar
failLastSec5 = _FailLastSec5_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 26),
    _FailLastSec5_Type()
)
failLastSec5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failLastSec5.setStatus("current")
_ReqPeakSec5_Type = Counter32
_ReqPeakSec5_Object = MibScalar
reqPeakSec5 = _ReqPeakSec5_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 27),
    _ReqPeakSec5_Type()
)
reqPeakSec5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqPeakSec5.setStatus("current")
_SuccPeakSec5_Type = Counter32
_SuccPeakSec5_Object = MibScalar
succPeakSec5 = _SuccPeakSec5_Object(
    (1, 3, 6, 1, 4, 1, 7564, 31, 28),
    _SuccPeakSec5_Type()
)
succPeakSec5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    succPeakSec5.setStatus("current")
_Monitor_ObjectIdentity = ObjectIdentity
monitor = _Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 32)
)


class _Cputemp_Type(DisplayString):
    """Custom type cputemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_Cputemp_Type.__name__ = "DisplayString"
_Cputemp_Object = MibScalar
cputemp = _Cputemp_Object(
    (1, 3, 6, 1, 4, 1, 7564, 32, 1),
    _Cputemp_Type()
)
cputemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cputemp.setStatus("current")


class _Fanspeed_Type(DisplayString):
    """Custom type fanspeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_Fanspeed_Type.__name__ = "DisplayString"
_Fanspeed_Object = MibScalar
fanspeed = _Fanspeed_Object(
    (1, 3, 6, 1, 4, 1, 7564, 32, 2),
    _Fanspeed_Type()
)
fanspeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanspeed.setStatus("current")


class _Powerstate_Type(Integer32):
    """Custom type powerstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("one-of-the-power-supply-modules-has-failed", 1))
    )


_Powerstate_Type.__name__ = "Integer32"
_Powerstate_Object = MibScalar
powerstate = _Powerstate_Object(
    (1, 3, 6, 1, 4, 1, 7564, 32, 3),
    _Powerstate_Type()
)
powerstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerstate.setStatus("current")
_CaTraps_ObjectIdentity = ObjectIdentity
caTraps = _CaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7564, 251)
)

# Managed Objects groups


# Notification objects

syslogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7564, 24, 3, 1)
)
syslogTrap.setObjects(
      *(("CA-SNMP-MIB8", "severity"),
        ("CA-SNMP-MIB8", "msgText"))
)
if mibBuilder.loadTexts:
    syslogTrap.setStatus(
        "current"
    )

caStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 7564, 251, 1)
)
if mibBuilder.loadTexts:
    caStart.setStatus(
        "current"
    )

caShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 7564, 251, 2)
)
if mibBuilder.loadTexts:
    caShutdown.setStatus(
        "current"
    )

licenseRemainingDays = NotificationType(
    (1, 3, 6, 1, 4, 1, 7564, 251, 3)
)
if mibBuilder.loadTexts:
    licenseRemainingDays.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CA-SNMP-MIB8",
    **{"Float": Float,
       "SyslogSeverity": SyslogSeverity,
       "arrayNetworks": arrayNetworks,
       "systemInfo": systemInfo,
       "serialNumber": serialNumber,
       "memory": memory,
       "sysMemory": sysMemory,
       "sysMemoryUtilization": sysMemoryUtilization,
       "sysSwapUsed": sysSwapUsed,
       "sysSwapCapacity": sysSwapCapacity,
       "revProxyCache": revProxyCache,
       "cacheBasicStats": cacheBasicStats,
       "cacheStatus": cacheStatus,
       "requestsReceived": requestsReceived,
       "getRequests": getRequests,
       "headRequests": headRequests,
       "purgeRequests": purgeRequests,
       "postRequests": postRequests,
       "clientEstabConn": clientEstabConn,
       "serverEstabConn": serverEstabConn,
       "requestsToHttps": requestsToHttps,
       "requestsOnRegex": requestsOnRegex,
       "requestsToUrl": requestsToUrl,
       "responsesToHttps": responsesToHttps,
       "responsesOnRegex": responsesOnRegex,
       "cacheSkip": cacheSkip,
       "hitsReply": hitsReply,
       "hitsReplyWNotModified": hitsReplyWNotModified,
       "hitsReplyWPreFailed": hitsReplyWPreFailed,
       "hitRevalidate": hitRevalidate,
       "cacheMissWNoncacheReq": cacheMissWNoncacheReq,
       "cacheMissWNewEntry": cacheMissWNewEntry,
       "cacheMissWRespNo": cacheMissWRespNo,
       "cacheHitRatio": cacheHitRatio,
       "vrrp": vrrp,
       "clusterVrrp": clusterVrrp,
       "maxCluster": maxCluster,
       "clusterNum": clusterNum,
       "vrrpTable": vrrpTable,
       "vrrpEntry": vrrpEntry,
       "clusterVirIndex": clusterVirIndex,
       "clusterId": clusterId,
       "clusterVirState": clusterVirState,
       "clusterVirIfname": clusterVirIfname,
       "clusterVirAddr": clusterVirAddr,
       "clusterVirAuthType": clusterVirAuthType,
       "clusterVirAuthPasswd": clusterVirAuthPasswd,
       "clusterVirPreempt": clusterVirPreempt,
       "clusterVirInterval": clusterVirInterval,
       "clusterVirPriority": clusterVirPriority,
       "clusterVirAddressType": clusterVirAddressType,
       "clusterVirAddress": clusterVirAddress,
       "slbMIB": slbMIB,
       "slbGeneral": slbGeneral,
       "realServer": realServer,
       "rsCount": rsCount,
       "rsTable": rsTable,
       "rsEntry": rsEntry,
       "rsIndex": rsIndex,
       "rsID": rsID,
       "rsProtocol": rsProtocol,
       "rsIpAddr": rsIpAddr,
       "rsPort": rsPort,
       "rsMaxConn": rsMaxConn,
       "rsStatus": rsStatus,
       "rsAvgRespTime": rsAvgRespTime,
       "rsIpAddressType": rsIpAddressType,
       "rsIpAddress": rsIpAddress,
       "virtualServer": virtualServer,
       "vsCount": vsCount,
       "vsTable": vsTable,
       "vsEntry": vsEntry,
       "vsIndex": vsIndex,
       "vsID": vsID,
       "vsProtocol": vsProtocol,
       "vsIpAddr": vsIpAddr,
       "vsPort": vsPort,
       "vsMaxConn": vsMaxConn,
       "vsIpAddressType": vsIpAddressType,
       "vsIpAddress": vsIpAddress,
       "groupCurCfg": groupCurCfg,
       "groupCount": groupCount,
       "gpTable": gpTable,
       "gpEntry": gpEntry,
       "gpIndex": gpIndex,
       "gpID": gpID,
       "realID": realID,
       "gpMetrics": gpMetrics,
       "slbStats": slbStats,
       "realStats": realStats,
       "rsStatsTable": rsStatsTable,
       "rsStatsEntry": rsStatsEntry,
       "realIndex": realIndex,
       "realServerID": realServerID,
       "realAddr": realAddr,
       "realPort": realPort,
       "rsCntOfReq": rsCntOfReq,
       "rsConnCnt": rsConnCnt,
       "rsTotalHits": rsTotalHits,
       "realStatus": realStatus,
       "realAddressType": realAddressType,
       "realAddress": realAddress,
       "virtualStats": virtualStats,
       "vsStatsTable": vsStatsTable,
       "vsStatsEntry": vsStatsEntry,
       "virtualIndex": virtualIndex,
       "virtServerID": virtServerID,
       "virtualAddr": virtualAddr,
       "virtualPort": virtualPort,
       "vsURLHits": vsURLHits,
       "vsHostnameHits": vsHostnameHits,
       "vsPerstntCookieHits": vsPerstntCookieHits,
       "vsQosCookieHits": vsQosCookieHits,
       "vsDefaultHits": vsDefaultHits,
       "vsPerstntURLHits": vsPerstntURLHits,
       "vsStaticHits": vsStaticHits,
       "vsQosNetworkHits": vsQosNetworkHits,
       "vsQosURLHits": vsQosURLHits,
       "vsBackupHits": vsBackupHits,
       "vsCacheHits": vsCacheHits,
       "vsRegexHits": vsRegexHits,
       "vsRCookieHits": vsRCookieHits,
       "vsICookieHits": vsICookieHits,
       "vsConnCnt": vsConnCnt,
       "virtualAddressType": virtualAddressType,
       "virtualAddress": virtualAddress,
       "vsQosClientPortHits": vsQosClientPortHits,
       "vsQosBodyHits": vsQosBodyHits,
       "vsHeaderHits": vsHeaderHits,
       "vsHashURLHits": vsHashURLHits,
       "vsRedirectHits": vsRedirectHits,
       "groupStats": groupStats,
       "gpStatsTable": gpStatsTable,
       "gpStatsEntry": gpStatsEntry,
       "groupIndex": groupIndex,
       "groupID": groupID,
       "gpTotalHits": gpTotalHits,
       "sslMIB": sslMIB,
       "sslGeneral": sslGeneral,
       "vhostNum": vhostNum,
       "sslStats": sslStats,
       "totalOpenSSLConns": totalOpenSSLConns,
       "totalAcceptedConns": totalAcceptedConns,
       "totalRequestedConns": totalRequestedConns,
       "sslTable": sslTable,
       "sslEntry": sslEntry,
       "sslIndex": sslIndex,
       "vhostName": vhostName,
       "openSSLConns": openSSLConns,
       "acceptedConns": acceptedConns,
       "requestedConns": requestedConns,
       "resumedSess": resumedSess,
       "resumableSess": resumableSess,
       "missSess": missSess,
       "connsPerSec": connsPerSec,
       "vipStats": vipStats,
       "vipStatus": vipStatus,
       "hostName": hostName,
       "currentTime": currentTime,
       "totalIPPktsIn": totalIPPktsIn,
       "totalIPPktsOut": totalIPPktsOut,
       "totalIPBytesIn": totalIPBytesIn,
       "totalIPBytesOut": totalIPBytesOut,
       "ipStatsTable": ipStatsTable,
       "ipStatsEntry": ipStatsEntry,
       "ipIndex": ipIndex,
       "ipAddress": ipAddress,
       "ipPktsIn": ipPktsIn,
       "ipBytesIn": ipBytesIn,
       "ipPktsOut": ipPktsOut,
       "ipBytesOut": ipBytesOut,
       "startTime": startTime,
       "ipAddrType": ipAddrType,
       "ipAddr": ipAddr,
       "ifTraffic": ifTraffic,
       "infNumber": infNumber,
       "infTotalInOctets": infTotalInOctets,
       "infTotalOutOctets": infTotalOutOctets,
       "infTable": infTable,
       "infEntry": infEntry,
       "infIndex": infIndex,
       "infDescr": infDescr,
       "infOperStatus": infOperStatus,
       "infAddress": infAddress,
       "infInOctets": infInOctets,
       "infInUcastPkts": infInUcastPkts,
       "infInNUcastPkts": infInNUcastPkts,
       "infInDiscards": infInDiscards,
       "infInErrors": infInErrors,
       "infInUnknownProtos": infInUnknownProtos,
       "infOutOctets": infOutOctets,
       "infOutUcastPkts": infOutUcastPkts,
       "infOutNUcastPkts": infOutNUcastPkts,
       "infOutErrors": infOutErrors,
       "infIpv4AddressType": infIpv4AddressType,
       "infIpv4Address": infIpv4Address,
       "infIpv6AddressType": infIpv6AddressType,
       "infIpv6Address": infIpv6Address,
       "infInBandwidth": infInBandwidth,
       "infOutBandwidth": infOutBandwidth,
       "infInMcastPkts": infInMcastPkts,
       "infOutMcastPkts": infOutMcastPkts,
       "infInBcastPkts": infInBcastPkts,
       "infOutBcastPkts": infOutBcastPkts,
       "caSyslog": caSyslog,
       "logBasic": logBasic,
       "logNotificationsSent": logNotificationsSent,
       "logNotificationsEnabled": logNotificationsEnabled,
       "logMaxSeverity": logMaxSeverity,
       "logHistory": logHistory,
       "logHistTableMaxLength": logHistTableMaxLength,
       "logHistoryTable": logHistoryTable,
       "logHistoryEntry": logHistoryEntry,
       "index": index,
       "severity": severity,
       "msgText": msgText,
       "caSyslogTrap": caSyslogTrap,
       "syslogTrap": syslogTrap,
       "clickTcp": clickTcp,
       "ctcpActiveOpens": ctcpActiveOpens,
       "ctcpPassiveOpens": ctcpPassiveOpens,
       "ctcpAttemptFails": ctcpAttemptFails,
       "ctcpEstabResets": ctcpEstabResets,
       "ctcpCurrEstab": ctcpCurrEstab,
       "ctcpInSegs": ctcpInSegs,
       "ctcpOutSegs": ctcpOutSegs,
       "ctcpRetransSegs": ctcpRetransSegs,
       "ctcpInErrs": ctcpInErrs,
       "ctcpOutRsts": ctcpOutRsts,
       "ctcpConnTable": ctcpConnTable,
       "ctcpConnEntry": ctcpConnEntry,
       "ctcpIndex": ctcpIndex,
       "ctcpConnState": ctcpConnState,
       "ctcpConnLocalAddress": ctcpConnLocalAddress,
       "ctcpConnLocalPort": ctcpConnLocalPort,
       "ctcpConnRemAddress": ctcpConnRemAddress,
       "ctcpConnRemPort": ctcpConnRemPort,
       "ctcpConnLocalAddrType": ctcpConnLocalAddrType,
       "ctcpConnLocalAddr": ctcpConnLocalAddr,
       "ctcpConnRemAddrType": ctcpConnRemAddrType,
       "ctcpConnRemAddr": ctcpConnRemAddr,
       "healthCheck": healthCheck,
       "hcStats": hcStats,
       "hcRSCount": hcRSCount,
       "hcStatsTable": hcStatsTable,
       "hcStatsEntry": hcStatsEntry,
       "hcIndex": hcIndex,
       "hcName": hcName,
       "hcAddr": hcAddr,
       "hcPort": hcPort,
       "hcStatus": hcStatus,
       "hcCause": hcCause,
       "hcNumDowns": hcNumDowns,
       "hcNumUps": hcNumUps,
       "hcConnAttempt": hcConnAttempt,
       "hcConnSuccess": hcConnSuccess,
       "hcConnFail": hcConnFail,
       "hcAddressType": hcAddressType,
       "hcAddress": hcAddress,
       "compression": compression,
       "totalBytesRcvd": totalBytesRcvd,
       "totalBytesSent": totalBytesSent,
       "rcvdBytesPerSec": rcvdBytesPerSec,
       "sentBytesPerSec": sentBytesPerSec,
       "peakRcvdBytesPerSec": peakRcvdBytesPerSec,
       "peakSentBytesPerSec": peakSentBytesPerSec,
       "activeTransac": activeTransac,
       "performance": performance,
       "cpuUtilization": cpuUtilization,
       "connectionsPerSec": connectionsPerSec,
       "requestsPerSec": requestsPerSec,
       "sdns": sdns,
       "totalReq": totalReq,
       "totalSucc": totalSucc,
       "totalFail": totalFail,
       "reqLastSec": reqLastSec,
       "succLastSec": succLastSec,
       "failLastSec": failLastSec,
       "reqPeakSec": reqPeakSec,
       "succPeakSec": succPeakSec,
       "reqLastMin": reqLastMin,
       "succLastMin": succLastMin,
       "failLastMin": failLastMin,
       "reqPeakMin": reqPeakMin,
       "succPeakMin": succPeakMin,
       "reqLastHour": reqLastHour,
       "succLastHour": succLastHour,
       "failLastHour": failLastHour,
       "reqPeakHour": reqPeakHour,
       "succPeakHour": succPeakHour,
       "reqLastDay": reqLastDay,
       "succLastDay": succLastDay,
       "failLastDay": failLastDay,
       "reqPeakDay": reqPeakDay,
       "succPeakDay": succPeakDay,
       "reqLastSec5": reqLastSec5,
       "succLastSec5": succLastSec5,
       "failLastSec5": failLastSec5,
       "reqPeakSec5": reqPeakSec5,
       "succPeakSec5": succPeakSec5,
       "monitor": monitor,
       "cputemp": cputemp,
       "fanspeed": fanspeed,
       "powerstate": powerstate,
       "caTraps": caTraps,
       "caStart": caStart,
       "caShutdown": caShutdown,
       "licenseRemainingDays": licenseRemainingDays}
)
