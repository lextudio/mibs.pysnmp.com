# SNMP MIB module (WOWZA-STREAMING-ENGINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WOWZA-STREAMING-ENGINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:19 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

wowzaStreamingEngineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100)
)
wowzaStreamingEngineMIB.setRevisions(
        ("2016-03-21 00:00",
         "2016-03-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wowzamediasystems_ObjectIdentity = ObjectIdentity
wowzamediasystems = _Wowzamediasystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706)
)
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 1)
)
_GroupServer_ObjectIdentity = ObjectIdentity
groupServer = _GroupServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 1, 10)
)
_GroupServerInfo_ObjectIdentity = ObjectIdentity
groupServerInfo = _GroupServerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 1, 10, 1)
)
_ServerGroupTable_Object = MibTable
serverGroupTable = _ServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    serverGroupTable.setStatus("current")
_ServerGroupEntry_Object = MibTableRow
serverGroupEntry = _ServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 1, 10, 1, 1, 1)
)
serverGroupEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "streamIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "clientIndex"),
)
if mibBuilder.loadTexts:
    serverGroupEntry.setStatus("current")


class _ServerIndex_Type(Integer32):
    """Custom type serverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ServerIndex_Type.__name__ = "Integer32"
_ServerIndex_Object = MibTableColumn
serverIndex = _ServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 1, 10, 1, 1, 1, 1),
    _ServerIndex_Type()
)
serverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverIndex.setStatus("current")


class _VhostIndex_Type(Integer32):
    """Custom type vhostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VhostIndex_Type.__name__ = "Integer32"
_VhostIndex_Object = MibTableColumn
vhostIndex = _VhostIndex_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 1, 10, 1, 1, 1, 2),
    _VhostIndex_Type()
)
vhostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostIndex.setStatus("current")


class _ApplicationIndex_Type(Integer32):
    """Custom type applicationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApplicationIndex_Type.__name__ = "Integer32"
_ApplicationIndex_Object = MibTableColumn
applicationIndex = _ApplicationIndex_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 1, 10, 1, 1, 1, 3),
    _ApplicationIndex_Type()
)
applicationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationIndex.setStatus("current")


class _ApplicationInstanceIndex_Type(Integer32):
    """Custom type applicationInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApplicationInstanceIndex_Type.__name__ = "Integer32"
_ApplicationInstanceIndex_Object = MibTableColumn
applicationInstanceIndex = _ApplicationInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 1, 10, 1, 1, 1, 4),
    _ApplicationInstanceIndex_Type()
)
applicationInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceIndex.setStatus("current")


class _StreamIndex_Type(Integer32):
    """Custom type streamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_StreamIndex_Type.__name__ = "Integer32"
_StreamIndex_Object = MibTableColumn
streamIndex = _StreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 1, 10, 1, 1, 1, 5),
    _StreamIndex_Type()
)
streamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamIndex.setStatus("current")
_ClientIndex_Type = Counter32
_ClientIndex_Object = MibTableColumn
clientIndex = _ClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 1, 10, 1, 1, 1, 6),
    _ClientIndex_Type()
)
clientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientIndex.setStatus("current")
_GroupObject_ObjectIdentity = ObjectIdentity
groupObject = _GroupObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2)
)
_ServerGroupObject_ObjectIdentity = ObjectIdentity
serverGroupObject = _ServerGroupObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 10)
)
_VhostGroupObject_ObjectIdentity = ObjectIdentity
vhostGroupObject = _VhostGroupObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 20)
)
_ApplicationGroupObject_ObjectIdentity = ObjectIdentity
applicationGroupObject = _ApplicationGroupObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 30)
)
_ApplicationInstanceGroupObject_ObjectIdentity = ObjectIdentity
applicationInstanceGroupObject = _ApplicationInstanceGroupObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 40)
)
_StreamGroupObject_ObjectIdentity = ObjectIdentity
streamGroupObject = _StreamGroupObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 50)
)
_ClientGroupObject_ObjectIdentity = ObjectIdentity
clientGroupObject = _ClientGroupObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 60)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3)
)
_ComplianceServer_ObjectIdentity = ObjectIdentity
complianceServer = _ComplianceServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3, 10)
)
_ComplianceVhost_ObjectIdentity = ObjectIdentity
complianceVhost = _ComplianceVhost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3, 20)
)
_ComplianceApplication_ObjectIdentity = ObjectIdentity
complianceApplication = _ComplianceApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3, 30)
)
_ComplianceApplicationInstance_ObjectIdentity = ObjectIdentity
complianceApplicationInstance = _ComplianceApplicationInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3, 40)
)
_ComplianceStream_ObjectIdentity = ObjectIdentity
complianceStream = _ComplianceStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3, 50)
)
_ComplianceClient_ObjectIdentity = ObjectIdentity
complianceClient = _ComplianceClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3, 60)
)
_Servers_ObjectIdentity = ObjectIdentity
servers = _Servers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10)
)
_ServerInfo_ObjectIdentity = ObjectIdentity
serverInfo = _ServerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1)
)
_ServerCounterTable_Object = MibTable
serverCounterTable = _ServerCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1)
)
if mibBuilder.loadTexts:
    serverCounterTable.setStatus("current")
_ServerCounterEntry_Object = MibTableRow
serverCounterEntry = _ServerCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1)
)
serverCounterEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
)
if mibBuilder.loadTexts:
    serverCounterEntry.setStatus("current")
_ServerCounterCreationTime_Type = Counter64
_ServerCounterCreationTime_Object = MibTableColumn
serverCounterCreationTime = _ServerCounterCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 1),
    _ServerCounterCreationTime_Type()
)
serverCounterCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterCreationTime.setStatus("current")
_ServerCounterGetAdminGUID_Type = DisplayString
_ServerCounterGetAdminGUID_Object = MibTableColumn
serverCounterGetAdminGUID = _ServerCounterGetAdminGUID_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 2),
    _ServerCounterGetAdminGUID_Type()
)
serverCounterGetAdminGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetAdminGUID.setStatus("current")
_ServerCounterGetClientIdGeneratorRecycleDelaySize_Type = Integer32
_ServerCounterGetClientIdGeneratorRecycleDelaySize_Object = MibTableColumn
serverCounterGetClientIdGeneratorRecycleDelaySize = _ServerCounterGetClientIdGeneratorRecycleDelaySize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 3),
    _ServerCounterGetClientIdGeneratorRecycleDelaySize_Type()
)
serverCounterGetClientIdGeneratorRecycleDelaySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetClientIdGeneratorRecycleDelaySize.setStatus("current")
_ServerCounterGetClientIdGeneratorRecycleSize_Type = Integer32
_ServerCounterGetClientIdGeneratorRecycleSize_Object = MibTableColumn
serverCounterGetClientIdGeneratorRecycleSize = _ServerCounterGetClientIdGeneratorRecycleSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 4),
    _ServerCounterGetClientIdGeneratorRecycleSize_Type()
)
serverCounterGetClientIdGeneratorRecycleSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetClientIdGeneratorRecycleSize.setStatus("current")
_ServerCounterGetClientIdGeneratorTimeout_Type = Counter64
_ServerCounterGetClientIdGeneratorTimeout_Object = MibTableColumn
serverCounterGetClientIdGeneratorTimeout = _ServerCounterGetClientIdGeneratorTimeout_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 5),
    _ServerCounterGetClientIdGeneratorTimeout_Type()
)
serverCounterGetClientIdGeneratorTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetClientIdGeneratorTimeout.setStatus("current")
_ServerCounterGetCommittedVirtuallMemory_Type = Counter64
_ServerCounterGetCommittedVirtuallMemory_Object = MibTableColumn
serverCounterGetCommittedVirtuallMemory = _ServerCounterGetCommittedVirtuallMemory_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 6),
    _ServerCounterGetCommittedVirtuallMemory_Type()
)
serverCounterGetCommittedVirtuallMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetCommittedVirtuallMemory.setStatus("current")
_ServerCounterGetConnectionsMaximum_Type = Counter64
_ServerCounterGetConnectionsMaximum_Object = MibTableColumn
serverCounterGetConnectionsMaximum = _ServerCounterGetConnectionsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 7),
    _ServerCounterGetConnectionsMaximum_Type()
)
serverCounterGetConnectionsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetConnectionsMaximum.setStatus("current")
_ServerCounterGetCoreHandlerPoolSize_Type = Integer32
_ServerCounterGetCoreHandlerPoolSize_Object = MibTableColumn
serverCounterGetCoreHandlerPoolSize = _ServerCounterGetCoreHandlerPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 8),
    _ServerCounterGetCoreHandlerPoolSize_Type()
)
serverCounterGetCoreHandlerPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetCoreHandlerPoolSize.setStatus("current")
_ServerCounterGetCoreTransportPoolSize_Type = Integer32
_ServerCounterGetCoreTransportPoolSize_Object = MibTableColumn
serverCounterGetCoreTransportPoolSize = _ServerCounterGetCoreTransportPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 9),
    _ServerCounterGetCoreTransportPoolSize_Type()
)
serverCounterGetCoreTransportPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetCoreTransportPoolSize.setStatus("current")
_ServerCounterGetCryptoPoolActiveCount_Type = Integer32
_ServerCounterGetCryptoPoolActiveCount_Object = MibTableColumn
serverCounterGetCryptoPoolActiveCount = _ServerCounterGetCryptoPoolActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 10),
    _ServerCounterGetCryptoPoolActiveCount_Type()
)
serverCounterGetCryptoPoolActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetCryptoPoolActiveCount.setStatus("current")
_ServerCounterGetCryptoPoolMaxSize_Type = Integer32
_ServerCounterGetCryptoPoolMaxSize_Object = MibTableColumn
serverCounterGetCryptoPoolMaxSize = _ServerCounterGetCryptoPoolMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 11),
    _ServerCounterGetCryptoPoolMaxSize_Type()
)
serverCounterGetCryptoPoolMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetCryptoPoolMaxSize.setStatus("current")
_ServerCounterGetCurrentHeapSize_Type = Counter64
_ServerCounterGetCurrentHeapSize_Object = MibTableColumn
serverCounterGetCurrentHeapSize = _ServerCounterGetCurrentHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 12),
    _ServerCounterGetCurrentHeapSize_Type()
)
serverCounterGetCurrentHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetCurrentHeapSize.setStatus("current")
_ServerCounterGetDateStarted_Type = DisplayString
_ServerCounterGetDateStarted_Object = MibTableColumn
serverCounterGetDateStarted = _ServerCounterGetDateStarted_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 13),
    _ServerCounterGetDateStarted_Type()
)
serverCounterGetDateStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetDateStarted.setStatus("current")
_ServerCounterGetDefaultStreamPrefix_Type = DisplayString
_ServerCounterGetDefaultStreamPrefix_Object = MibTableColumn
serverCounterGetDefaultStreamPrefix = _ServerCounterGetDefaultStreamPrefix_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 14),
    _ServerCounterGetDefaultStreamPrefix_Type()
)
serverCounterGetDefaultStreamPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetDefaultStreamPrefix.setStatus("current")
_ServerCounterGetGUID_Type = DisplayString
_ServerCounterGetGUID_Object = MibTableColumn
serverCounterGetGUID = _ServerCounterGetGUID_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 15),
    _ServerCounterGetGUID_Type()
)
serverCounterGetGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetGUID.setStatus("current")
_ServerCounterGetHTTPHeaderServer_Type = DisplayString
_ServerCounterGetHTTPHeaderServer_Object = MibTableColumn
serverCounterGetHTTPHeaderServer = _ServerCounterGetHTTPHeaderServer_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 16),
    _ServerCounterGetHTTPHeaderServer_Type()
)
serverCounterGetHTTPHeaderServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetHTTPHeaderServer.setStatus("current")
_ServerCounterGetLiveStreamTranscoderSessionCount_Type = Counter64
_ServerCounterGetLiveStreamTranscoderSessionCount_Object = MibTableColumn
serverCounterGetLiveStreamTranscoderSessionCount = _ServerCounterGetLiveStreamTranscoderSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 17),
    _ServerCounterGetLiveStreamTranscoderSessionCount_Type()
)
serverCounterGetLiveStreamTranscoderSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetLiveStreamTranscoderSessionCount.setStatus("current")
_ServerCounterGetLiveThreads_Type = Counter64
_ServerCounterGetLiveThreads_Object = MibTableColumn
serverCounterGetLiveThreads = _ServerCounterGetLiveThreads_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 18),
    _ServerCounterGetLiveThreads_Type()
)
serverCounterGetLiveThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetLiveThreads.setStatus("current")
_ServerCounterGetMaxHeapSize_Type = Counter64
_ServerCounterGetMaxHeapSize_Object = MibTableColumn
serverCounterGetMaxHeapSize = _ServerCounterGetMaxHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 19),
    _ServerCounterGetMaxHeapSize_Type()
)
serverCounterGetMaxHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetMaxHeapSize.setStatus("current")
_ServerCounterGetPeakThreads_Type = Counter64
_ServerCounterGetPeakThreads_Object = MibTableColumn
serverCounterGetPeakThreads = _ServerCounterGetPeakThreads_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 20),
    _ServerCounterGetPeakThreads_Type()
)
serverCounterGetPeakThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetPeakThreads.setStatus("current")
_ServerCounterGetPublishersMaximum_Type = Counter64
_ServerCounterGetPublishersMaximum_Object = MibTableColumn
serverCounterGetPublishersMaximum = _ServerCounterGetPublishersMaximum_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 21),
    _ServerCounterGetPublishersMaximum_Type()
)
serverCounterGetPublishersMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetPublishersMaximum.setStatus("current")
_ServerCounterGetRTMPTHeaderServer_Type = DisplayString
_ServerCounterGetRTMPTHeaderServer_Object = MibTableColumn
serverCounterGetRTMPTHeaderServer = _ServerCounterGetRTMPTHeaderServer_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 22),
    _ServerCounterGetRTMPTHeaderServer_Type()
)
serverCounterGetRTMPTHeaderServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetRTMPTHeaderServer.setStatus("current")
_ServerCounterGetServerGUID_Type = DisplayString
_ServerCounterGetServerGUID_Object = MibTableColumn
serverCounterGetServerGUID = _ServerCounterGetServerGUID_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 23),
    _ServerCounterGetServerGUID_Type()
)
serverCounterGetServerGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetServerGUID.setStatus("current")
_ServerCounterGetSessionGUID_Type = DisplayString
_ServerCounterGetSessionGUID_Object = MibTableColumn
serverCounterGetSessionGUID = _ServerCounterGetSessionGUID_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 24),
    _ServerCounterGetSessionGUID_Type()
)
serverCounterGetSessionGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetSessionGUID.setStatus("current")
_ServerCounterGetTimeRunning_Type = DisplayString
_ServerCounterGetTimeRunning_Object = MibTableColumn
serverCounterGetTimeRunning = _ServerCounterGetTimeRunning_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 25),
    _ServerCounterGetTimeRunning_Type()
)
serverCounterGetTimeRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetTimeRunning.setStatus("current")
_ServerCounterGetTranscoderLicenseInUse_Type = Counter64
_ServerCounterGetTranscoderLicenseInUse_Object = MibTableColumn
serverCounterGetTranscoderLicenseInUse = _ServerCounterGetTranscoderLicenseInUse_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 26),
    _ServerCounterGetTranscoderLicenseInUse_Type()
)
serverCounterGetTranscoderLicenseInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetTranscoderLicenseInUse.setStatus("current")
_ServerCounterGetTranscoderLicenseTotal_Type = Counter64
_ServerCounterGetTranscoderLicenseTotal_Object = MibTableColumn
serverCounterGetTranscoderLicenseTotal = _ServerCounterGetTranscoderLicenseTotal_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 27),
    _ServerCounterGetTranscoderLicenseTotal_Type()
)
serverCounterGetTranscoderLicenseTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetTranscoderLicenseTotal.setStatus("current")
_ServerCounterGetVersion_Type = DisplayString
_ServerCounterGetVersion_Object = MibTableColumn
serverCounterGetVersion = _ServerCounterGetVersion_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 1, 1, 28),
    _ServerCounterGetVersion_Type()
)
serverCounterGetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCounterGetVersion.setStatus("current")
_ServerConnectTable_Object = MibTable
serverConnectTable = _ServerConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2)
)
if mibBuilder.loadTexts:
    serverConnectTable.setStatus("current")
_ServerConnectEntry_Object = MibTableRow
serverConnectEntry = _ServerConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1)
)
serverConnectEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
)
if mibBuilder.loadTexts:
    serverConnectEntry.setStatus("current")
_ServerConnectCreationTime_Type = Counter64
_ServerConnectCreationTime_Object = MibTableColumn
serverConnectCreationTime = _ServerConnectCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1, 1),
    _ServerConnectCreationTime_Type()
)
serverConnectCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnectCreationTime.setStatus("current")
_ServerConnectGetCurrent_Type = Counter64
_ServerConnectGetCurrent_Object = MibTableColumn
serverConnectGetCurrent = _ServerConnectGetCurrent_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1, 2),
    _ServerConnectGetCurrent_Type()
)
serverConnectGetCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnectGetCurrent.setStatus("current")
_ServerConnectGetLastConnectAcceptedStamp_Type = Counter64
_ServerConnectGetLastConnectAcceptedStamp_Object = MibTableColumn
serverConnectGetLastConnectAcceptedStamp = _ServerConnectGetLastConnectAcceptedStamp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1, 3),
    _ServerConnectGetLastConnectAcceptedStamp_Type()
)
serverConnectGetLastConnectAcceptedStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnectGetLastConnectAcceptedStamp.setStatus("current")
_ServerConnectGetLastConnectAcceptedStampString_Type = DisplayString
_ServerConnectGetLastConnectAcceptedStampString_Object = MibTableColumn
serverConnectGetLastConnectAcceptedStampString = _ServerConnectGetLastConnectAcceptedStampString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1, 4),
    _ServerConnectGetLastConnectAcceptedStampString_Type()
)
serverConnectGetLastConnectAcceptedStampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnectGetLastConnectAcceptedStampString.setStatus("current")
_ServerConnectGetLastConnectAcceptedTimeString_Type = DisplayString
_ServerConnectGetLastConnectAcceptedTimeString_Object = MibTableColumn
serverConnectGetLastConnectAcceptedTimeString = _ServerConnectGetLastConnectAcceptedTimeString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1, 5),
    _ServerConnectGetLastConnectAcceptedTimeString_Type()
)
serverConnectGetLastConnectAcceptedTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnectGetLastConnectAcceptedTimeString.setStatus("current")
_ServerConnectGetLastConnectRejectedStamp_Type = Counter64
_ServerConnectGetLastConnectRejectedStamp_Object = MibTableColumn
serverConnectGetLastConnectRejectedStamp = _ServerConnectGetLastConnectRejectedStamp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1, 6),
    _ServerConnectGetLastConnectRejectedStamp_Type()
)
serverConnectGetLastConnectRejectedStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnectGetLastConnectRejectedStamp.setStatus("current")
_ServerConnectGetLastConnectRejectedStampString_Type = DisplayString
_ServerConnectGetLastConnectRejectedStampString_Object = MibTableColumn
serverConnectGetLastConnectRejectedStampString = _ServerConnectGetLastConnectRejectedStampString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1, 7),
    _ServerConnectGetLastConnectRejectedStampString_Type()
)
serverConnectGetLastConnectRejectedStampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnectGetLastConnectRejectedStampString.setStatus("current")
_ServerConnectGetLastConnectRejectedTimeString_Type = DisplayString
_ServerConnectGetLastConnectRejectedTimeString_Object = MibTableColumn
serverConnectGetLastConnectRejectedTimeString = _ServerConnectGetLastConnectRejectedTimeString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1, 8),
    _ServerConnectGetLastConnectRejectedTimeString_Type()
)
serverConnectGetLastConnectRejectedTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnectGetLastConnectRejectedTimeString.setStatus("current")
_ServerConnectGetLastDisconnectStamp_Type = Counter64
_ServerConnectGetLastDisconnectStamp_Object = MibTableColumn
serverConnectGetLastDisconnectStamp = _ServerConnectGetLastDisconnectStamp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1, 9),
    _ServerConnectGetLastDisconnectStamp_Type()
)
serverConnectGetLastDisconnectStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnectGetLastDisconnectStamp.setStatus("current")
_ServerConnectGetLastDisconnectStampString_Type = DisplayString
_ServerConnectGetLastDisconnectStampString_Object = MibTableColumn
serverConnectGetLastDisconnectStampString = _ServerConnectGetLastDisconnectStampString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1, 10),
    _ServerConnectGetLastDisconnectStampString_Type()
)
serverConnectGetLastDisconnectStampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnectGetLastDisconnectStampString.setStatus("current")
_ServerConnectGetLastDisconnectTimeString_Type = DisplayString
_ServerConnectGetLastDisconnectTimeString_Object = MibTableColumn
serverConnectGetLastDisconnectTimeString = _ServerConnectGetLastDisconnectTimeString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1, 11),
    _ServerConnectGetLastDisconnectTimeString_Type()
)
serverConnectGetLastDisconnectTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnectGetLastDisconnectTimeString.setStatus("current")
_ServerConnectGetTotal_Type = Counter64
_ServerConnectGetTotal_Object = MibTableColumn
serverConnectGetTotal = _ServerConnectGetTotal_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1, 12),
    _ServerConnectGetTotal_Type()
)
serverConnectGetTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnectGetTotal.setStatus("current")
_ServerConnectGetTotalAccepted_Type = Counter64
_ServerConnectGetTotalAccepted_Object = MibTableColumn
serverConnectGetTotalAccepted = _ServerConnectGetTotalAccepted_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1, 13),
    _ServerConnectGetTotalAccepted_Type()
)
serverConnectGetTotalAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnectGetTotalAccepted.setStatus("current")
_ServerConnectGetTotalRejected_Type = Counter64
_ServerConnectGetTotalRejected_Object = MibTableColumn
serverConnectGetTotalRejected = _ServerConnectGetTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 2, 1, 14),
    _ServerConnectGetTotalRejected_Type()
)
serverConnectGetTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnectGetTotalRejected.setStatus("current")
_ServerPerformTable_Object = MibTable
serverPerformTable = _ServerPerformTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 3)
)
if mibBuilder.loadTexts:
    serverPerformTable.setStatus("current")
_ServerPerformEntry_Object = MibTableRow
serverPerformEntry = _ServerPerformEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 3, 1)
)
serverPerformEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
)
if mibBuilder.loadTexts:
    serverPerformEntry.setStatus("current")
_ServerPerformCreationTime_Type = Counter64
_ServerPerformCreationTime_Object = MibTableColumn
serverPerformCreationTime = _ServerPerformCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 3, 1, 1),
    _ServerPerformCreationTime_Type()
)
serverPerformCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPerformCreationTime.setStatus("current")
_ServerPerformGetFileInBytes_Type = Counter64
_ServerPerformGetFileInBytes_Object = MibTableColumn
serverPerformGetFileInBytes = _ServerPerformGetFileInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 3, 1, 2),
    _ServerPerformGetFileInBytes_Type()
)
serverPerformGetFileInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPerformGetFileInBytes.setStatus("current")
_ServerPerformGetFileOutBytes_Type = Counter64
_ServerPerformGetFileOutBytes_Object = MibTableColumn
serverPerformGetFileOutBytes = _ServerPerformGetFileOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 3, 1, 3),
    _ServerPerformGetFileOutBytes_Type()
)
serverPerformGetFileOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPerformGetFileOutBytes.setStatus("current")
_ServerPerformGetMessagesInBytes_Type = Counter64
_ServerPerformGetMessagesInBytes_Object = MibTableColumn
serverPerformGetMessagesInBytes = _ServerPerformGetMessagesInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 3, 1, 4),
    _ServerPerformGetMessagesInBytes_Type()
)
serverPerformGetMessagesInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPerformGetMessagesInBytes.setStatus("current")
_ServerPerformGetMessagesInCount_Type = Counter64
_ServerPerformGetMessagesInCount_Object = MibTableColumn
serverPerformGetMessagesInCount = _ServerPerformGetMessagesInCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 3, 1, 5),
    _ServerPerformGetMessagesInCount_Type()
)
serverPerformGetMessagesInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPerformGetMessagesInCount.setStatus("current")
_ServerPerformGetMessagesInCountRate_Type = Counter64
_ServerPerformGetMessagesInCountRate_Object = MibTableColumn
serverPerformGetMessagesInCountRate = _ServerPerformGetMessagesInCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 3, 1, 6),
    _ServerPerformGetMessagesInCountRate_Type()
)
serverPerformGetMessagesInCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPerformGetMessagesInCountRate.setStatus("current")
_ServerPerformGetMessagesLossBytes_Type = Counter64
_ServerPerformGetMessagesLossBytes_Object = MibTableColumn
serverPerformGetMessagesLossBytes = _ServerPerformGetMessagesLossBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 3, 1, 7),
    _ServerPerformGetMessagesLossBytes_Type()
)
serverPerformGetMessagesLossBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPerformGetMessagesLossBytes.setStatus("current")
_ServerPerformGetMessagesLossCount_Type = Counter64
_ServerPerformGetMessagesLossCount_Object = MibTableColumn
serverPerformGetMessagesLossCount = _ServerPerformGetMessagesLossCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 3, 1, 8),
    _ServerPerformGetMessagesLossCount_Type()
)
serverPerformGetMessagesLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPerformGetMessagesLossCount.setStatus("current")
_ServerPerformGetMessagesLossCountRate_Type = Counter64
_ServerPerformGetMessagesLossCountRate_Object = MibTableColumn
serverPerformGetMessagesLossCountRate = _ServerPerformGetMessagesLossCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 3, 1, 9),
    _ServerPerformGetMessagesLossCountRate_Type()
)
serverPerformGetMessagesLossCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPerformGetMessagesLossCountRate.setStatus("current")
_ServerPerformGetMessagesOutBytes_Type = Counter64
_ServerPerformGetMessagesOutBytes_Object = MibTableColumn
serverPerformGetMessagesOutBytes = _ServerPerformGetMessagesOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 3, 1, 10),
    _ServerPerformGetMessagesOutBytes_Type()
)
serverPerformGetMessagesOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPerformGetMessagesOutBytes.setStatus("current")
_ServerPerformGetMessagesOutCount_Type = Counter64
_ServerPerformGetMessagesOutCount_Object = MibTableColumn
serverPerformGetMessagesOutCount = _ServerPerformGetMessagesOutCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 3, 1, 11),
    _ServerPerformGetMessagesOutCount_Type()
)
serverPerformGetMessagesOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPerformGetMessagesOutCount.setStatus("current")
_ServerPerformGetMessagesOutCountRate_Type = Counter64
_ServerPerformGetMessagesOutCountRate_Object = MibTableColumn
serverPerformGetMessagesOutCountRate = _ServerPerformGetMessagesOutCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 10, 1, 3, 1, 12),
    _ServerPerformGetMessagesOutCountRate_Type()
)
serverPerformGetMessagesOutCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPerformGetMessagesOutCountRate.setStatus("current")
_Vhosts_ObjectIdentity = ObjectIdentity
vhosts = _Vhosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20)
)
_VhostInfo_ObjectIdentity = ObjectIdentity
vhostInfo = _VhostInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1)
)
_VhostCounterTable_Object = MibTable
vhostCounterTable = _VhostCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1)
)
if mibBuilder.loadTexts:
    vhostCounterTable.setStatus("current")
_VhostCounterEntry_Object = MibTableRow
vhostCounterEntry = _VhostCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1)
)
vhostCounterEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
)
if mibBuilder.loadTexts:
    vhostCounterEntry.setStatus("current")
_VhostCounterCreationTime_Type = Counter64
_VhostCounterCreationTime_Object = MibTableColumn
vhostCounterCreationTime = _VhostCounterCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 1),
    _VhostCounterCreationTime_Type()
)
vhostCounterCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterCreationTime.setStatus("current")
_VhostCounterGetApplicationTimeout_Type = Integer32
_VhostCounterGetApplicationTimeout_Object = MibTableColumn
vhostCounterGetApplicationTimeout = _VhostCounterGetApplicationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 2),
    _VhostCounterGetApplicationTimeout_Type()
)
vhostCounterGetApplicationTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetApplicationTimeout.setStatus("current")
_VhostCounterGetByteArrayOutputStreamBaseClassPath_Type = DisplayString
_VhostCounterGetByteArrayOutputStreamBaseClassPath_Object = MibTableColumn
vhostCounterGetByteArrayOutputStreamBaseClassPath = _VhostCounterGetByteArrayOutputStreamBaseClassPath_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 3),
    _VhostCounterGetByteArrayOutputStreamBaseClassPath_Type()
)
vhostCounterGetByteArrayOutputStreamBaseClassPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetByteArrayOutputStreamBaseClassPath.setStatus("current")
_VhostCounterGetClientCount_Type = Integer32
_VhostCounterGetClientCount_Object = MibTableColumn
vhostCounterGetClientCount = _VhostCounterGetClientCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 4),
    _VhostCounterGetClientCount_Type()
)
vhostCounterGetClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetClientCount.setStatus("current")
_VhostCounterGetClientIdleFrequency_Type = Integer32
_VhostCounterGetClientIdleFrequency_Object = MibTableColumn
vhostCounterGetClientIdleFrequency = _VhostCounterGetClientIdleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 5),
    _VhostCounterGetClientIdleFrequency_Type()
)
vhostCounterGetClientIdleFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetClientIdleFrequency.setStatus("current")
_VhostCounterGetClientTimeout_Type = Integer32
_VhostCounterGetClientTimeout_Object = MibTableColumn
vhostCounterGetClientTimeout = _VhostCounterGetClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 6),
    _VhostCounterGetClientTimeout_Type()
)
vhostCounterGetClientTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetClientTimeout.setStatus("current")
_VhostCounterGetConnectionLimit_Type = Integer32
_VhostCounterGetConnectionLimit_Object = MibTableColumn
vhostCounterGetConnectionLimit = _VhostCounterGetConnectionLimit_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 7),
    _VhostCounterGetConnectionLimit_Type()
)
vhostCounterGetConnectionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetConnectionLimit.setStatus("current")
_VhostCounterGetCoreHandlerPoolSize_Type = Integer32
_VhostCounterGetCoreHandlerPoolSize_Object = MibTableColumn
vhostCounterGetCoreHandlerPoolSize = _VhostCounterGetCoreHandlerPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 8),
    _VhostCounterGetCoreHandlerPoolSize_Type()
)
vhostCounterGetCoreHandlerPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetCoreHandlerPoolSize.setStatus("current")
_VhostCounterGetCoreTransportPoolSize_Type = Integer32
_VhostCounterGetCoreTransportPoolSize_Object = MibTableColumn
vhostCounterGetCoreTransportPoolSize = _VhostCounterGetCoreTransportPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 9),
    _VhostCounterGetCoreTransportPoolSize_Type()
)
vhostCounterGetCoreTransportPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetCoreTransportPoolSize.setStatus("current")
_VhostCounterGetDateStarted_Type = DisplayString
_VhostCounterGetDateStarted_Object = MibTableColumn
vhostCounterGetDateStarted = _VhostCounterGetDateStarted_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 10),
    _VhostCounterGetDateStarted_Type()
)
vhostCounterGetDateStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetDateStarted.setStatus("current")
_VhostCounterGetFileIOPoolSize_Type = Integer32
_VhostCounterGetFileIOPoolSize_Object = MibTableColumn
vhostCounterGetFileIOPoolSize = _VhostCounterGetFileIOPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 11),
    _VhostCounterGetFileIOPoolSize_Type()
)
vhostCounterGetFileIOPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetFileIOPoolSize.setStatus("current")
_VhostCounterGetHTTPStreamerMaxPathLen_Type = Integer32
_VhostCounterGetHTTPStreamerMaxPathLen_Object = MibTableColumn
vhostCounterGetHTTPStreamerMaxPathLen = _VhostCounterGetHTTPStreamerMaxPathLen_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 12),
    _VhostCounterGetHTTPStreamerMaxPathLen_Type()
)
vhostCounterGetHTTPStreamerMaxPathLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetHTTPStreamerMaxPathLen.setStatus("current")
_VhostCounterGetHomePath_Type = DisplayString
_VhostCounterGetHomePath_Object = MibTableColumn
vhostCounterGetHomePath = _VhostCounterGetHomePath_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 13),
    _VhostCounterGetHomePath_Type()
)
vhostCounterGetHomePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetHomePath.setStatus("current")
_VhostCounterGetIdleCheckFrequency_Type = Integer32
_VhostCounterGetIdleCheckFrequency_Object = MibTableColumn
vhostCounterGetIdleCheckFrequency = _VhostCounterGetIdleCheckFrequency_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 14),
    _VhostCounterGetIdleCheckFrequency_Type()
)
vhostCounterGetIdleCheckFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetIdleCheckFrequency.setStatus("current")
_VhostCounterGetIdleMinimumWaitTime_Type = Integer32
_VhostCounterGetIdleMinimumWaitTime_Object = MibTableColumn
vhostCounterGetIdleMinimumWaitTime = _VhostCounterGetIdleMinimumWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 15),
    _VhostCounterGetIdleMinimumWaitTime_Type()
)
vhostCounterGetIdleMinimumWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetIdleMinimumWaitTime.setStatus("current")
_VhostCounterGetIdleWorkerCount_Type = Integer32
_VhostCounterGetIdleWorkerCount_Object = MibTableColumn
vhostCounterGetIdleWorkerCount = _VhostCounterGetIdleWorkerCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 16),
    _VhostCounterGetIdleWorkerCount_Type()
)
vhostCounterGetIdleWorkerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetIdleWorkerCount.setStatus("current")
_VhostCounterGetKeepAliveTimeout_Type = Integer32
_VhostCounterGetKeepAliveTimeout_Object = MibTableColumn
vhostCounterGetKeepAliveTimeout = _VhostCounterGetKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 17),
    _VhostCounterGetKeepAliveTimeout_Type()
)
vhostCounterGetKeepAliveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetKeepAliveTimeout.setStatus("current")
_VhostCounterGetLiveStreamTranscoderSessionCount_Type = Counter64
_VhostCounterGetLiveStreamTranscoderSessionCount_Object = MibTableColumn
vhostCounterGetLiveStreamTranscoderSessionCount = _VhostCounterGetLiveStreamTranscoderSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 18),
    _VhostCounterGetLiveStreamTranscoderSessionCount_Type()
)
vhostCounterGetLiveStreamTranscoderSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetLiveStreamTranscoderSessionCount.setStatus("current")
_VhostCounterGetMaximumPendingReadBytes_Type = Integer32
_VhostCounterGetMaximumPendingReadBytes_Object = MibTableColumn
vhostCounterGetMaximumPendingReadBytes = _VhostCounterGetMaximumPendingReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 19),
    _VhostCounterGetMaximumPendingReadBytes_Type()
)
vhostCounterGetMaximumPendingReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetMaximumPendingReadBytes.setStatus("current")
_VhostCounterGetMaximumPendingWriteBytes_Type = Integer32
_VhostCounterGetMaximumPendingWriteBytes_Object = MibTableColumn
vhostCounterGetMaximumPendingWriteBytes = _VhostCounterGetMaximumPendingWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 20),
    _VhostCounterGetMaximumPendingWriteBytes_Type()
)
vhostCounterGetMaximumPendingWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetMaximumPendingWriteBytes.setStatus("current")
_VhostCounterGetMaximumSetBufferTime_Type = Integer32
_VhostCounterGetMaximumSetBufferTime_Object = MibTableColumn
vhostCounterGetMaximumSetBufferTime = _VhostCounterGetMaximumSetBufferTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 21),
    _VhostCounterGetMaximumSetBufferTime_Type()
)
vhostCounterGetMaximumSetBufferTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetMaximumSetBufferTime.setStatus("current")
_VhostCounterGetName_Type = DisplayString
_VhostCounterGetName_Object = MibTableColumn
vhostCounterGetName = _VhostCounterGetName_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 22),
    _VhostCounterGetName_Type()
)
vhostCounterGetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetName.setStatus("current")
_VhostCounterGetNetConnectionIdleFrequency_Type = Integer32
_VhostCounterGetNetConnectionIdleFrequency_Object = MibTableColumn
vhostCounterGetNetConnectionIdleFrequency = _VhostCounterGetNetConnectionIdleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 23),
    _VhostCounterGetNetConnectionIdleFrequency_Type()
)
vhostCounterGetNetConnectionIdleFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetNetConnectionIdleFrequency.setStatus("current")
_VhostCounterGetNetConnectionProcessorCount_Type = Integer32
_VhostCounterGetNetConnectionProcessorCount_Object = MibTableColumn
vhostCounterGetNetConnectionProcessorCount = _VhostCounterGetNetConnectionProcessorCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 24),
    _VhostCounterGetNetConnectionProcessorCount_Type()
)
vhostCounterGetNetConnectionProcessorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetNetConnectionProcessorCount.setStatus("current")
_VhostCounterGetNextMediaCasterId_Type = Integer32
_VhostCounterGetNextMediaCasterId_Object = MibTableColumn
vhostCounterGetNextMediaCasterId = _VhostCounterGetNextMediaCasterId_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 25),
    _VhostCounterGetNextMediaCasterId_Type()
)
vhostCounterGetNextMediaCasterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetNextMediaCasterId.setStatus("current")
_VhostCounterGetNextNetConnectionId_Type = Integer32
_VhostCounterGetNextNetConnectionId_Object = MibTableColumn
vhostCounterGetNextNetConnectionId = _VhostCounterGetNextNetConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 26),
    _VhostCounterGetNextNetConnectionId_Type()
)
vhostCounterGetNextNetConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetNextNetConnectionId.setStatus("current")
_VhostCounterGetPingTimeout_Type = Integer32
_VhostCounterGetPingTimeout_Object = MibTableColumn
vhostCounterGetPingTimeout = _VhostCounterGetPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 27),
    _VhostCounterGetPingTimeout_Type()
)
vhostCounterGetPingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetPingTimeout.setStatus("current")
_VhostCounterGetRTPIdleFrequency_Type = Integer32
_VhostCounterGetRTPIdleFrequency_Object = MibTableColumn
vhostCounterGetRTPIdleFrequency = _VhostCounterGetRTPIdleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 28),
    _VhostCounterGetRTPIdleFrequency_Type()
)
vhostCounterGetRTPIdleFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetRTPIdleFrequency.setStatus("current")
_VhostCounterGetRTSPMaxPathLen_Type = Integer32
_VhostCounterGetRTSPMaxPathLen_Object = MibTableColumn
vhostCounterGetRTSPMaxPathLen = _VhostCounterGetRTSPMaxPathLen_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 29),
    _VhostCounterGetRTSPMaxPathLen_Type()
)
vhostCounterGetRTSPMaxPathLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetRTSPMaxPathLen.setStatus("current")
_VhostCounterGetScheduledReadMaxSessionBytes_Type = Counter64
_VhostCounterGetScheduledReadMaxSessionBytes_Object = MibTableColumn
vhostCounterGetScheduledReadMaxSessionBytes = _VhostCounterGetScheduledReadMaxSessionBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 30),
    _VhostCounterGetScheduledReadMaxSessionBytes_Type()
)
vhostCounterGetScheduledReadMaxSessionBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetScheduledReadMaxSessionBytes.setStatus("current")
_VhostCounterGetScheduledWriteBytes_Type = Counter64
_VhostCounterGetScheduledWriteBytes_Object = MibTableColumn
vhostCounterGetScheduledWriteBytes = _VhostCounterGetScheduledWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 31),
    _VhostCounterGetScheduledWriteBytes_Type()
)
vhostCounterGetScheduledWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetScheduledWriteBytes.setStatus("current")
_VhostCounterGetScheduledWriteMaxSessionBytes_Type = Counter64
_VhostCounterGetScheduledWriteMaxSessionBytes_Object = MibTableColumn
vhostCounterGetScheduledWriteMaxSessionBytes = _VhostCounterGetScheduledWriteMaxSessionBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 32),
    _VhostCounterGetScheduledWriteMaxSessionBytes_Type()
)
vhostCounterGetScheduledWriteMaxSessionBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetScheduledWriteMaxSessionBytes.setStatus("current")
_VhostCounterGetScheduledWriteMaxSessionClientId_Type = Integer32
_VhostCounterGetScheduledWriteMaxSessionClientId_Object = MibTableColumn
vhostCounterGetScheduledWriteMaxSessionClientId = _VhostCounterGetScheduledWriteMaxSessionClientId_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 33),
    _VhostCounterGetScheduledWriteMaxSessionClientId_Type()
)
vhostCounterGetScheduledWriteMaxSessionClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetScheduledWriteMaxSessionClientId.setStatus("current")
_VhostCounterGetScheduledWriteRequests_Type = Counter64
_VhostCounterGetScheduledWriteRequests_Object = MibTableColumn
vhostCounterGetScheduledWriteRequests = _VhostCounterGetScheduledWriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 34),
    _VhostCounterGetScheduledWriteRequests_Type()
)
vhostCounterGetScheduledWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetScheduledWriteRequests.setStatus("current")
_VhostCounterGetScheduledWriteSessions_Type = Counter64
_VhostCounterGetScheduledWriteSessions_Object = MibTableColumn
vhostCounterGetScheduledWriteSessions = _VhostCounterGetScheduledWriteSessions_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 35),
    _VhostCounterGetScheduledWriteSessions_Type()
)
vhostCounterGetScheduledWriteSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetScheduledWriteSessions.setStatus("current")
_VhostCounterGetStartupStreamsDelayTime_Type = Integer32
_VhostCounterGetStartupStreamsDelayTime_Object = MibTableColumn
vhostCounterGetStartupStreamsDelayTime = _VhostCounterGetStartupStreamsDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 36),
    _VhostCounterGetStartupStreamsDelayTime_Type()
)
vhostCounterGetStartupStreamsDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetStartupStreamsDelayTime.setStatus("current")
_VhostCounterGetTimeRunning_Type = DisplayString
_VhostCounterGetTimeRunning_Object = MibTableColumn
vhostCounterGetTimeRunning = _VhostCounterGetTimeRunning_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 37),
    _VhostCounterGetTimeRunning_Type()
)
vhostCounterGetTimeRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetTimeRunning.setStatus("current")
_VhostCounterGetUnidentifiedSessionTimeout_Type = Integer32
_VhostCounterGetUnidentifiedSessionTimeout_Object = MibTableColumn
vhostCounterGetUnidentifiedSessionTimeout = _VhostCounterGetUnidentifiedSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 38),
    _VhostCounterGetUnidentifiedSessionTimeout_Type()
)
vhostCounterGetUnidentifiedSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetUnidentifiedSessionTimeout.setStatus("current")
_VhostCounterGetValidationFrequency_Type = Integer32
_VhostCounterGetValidationFrequency_Object = MibTableColumn
vhostCounterGetValidationFrequency = _VhostCounterGetValidationFrequency_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 39),
    _VhostCounterGetValidationFrequency_Type()
)
vhostCounterGetValidationFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetValidationFrequency.setStatus("current")
_VhostCounterGetWaitingReadBytes_Type = Counter64
_VhostCounterGetWaitingReadBytes_Object = MibTableColumn
vhostCounterGetWaitingReadBytes = _VhostCounterGetWaitingReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 40),
    _VhostCounterGetWaitingReadBytes_Type()
)
vhostCounterGetWaitingReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetWaitingReadBytes.setStatus("current")
_VhostCounterGetWebRTCIdleFrequency_Type = Integer32
_VhostCounterGetWebRTCIdleFrequency_Object = MibTableColumn
vhostCounterGetWebRTCIdleFrequency = _VhostCounterGetWebRTCIdleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 1, 1, 41),
    _VhostCounterGetWebRTCIdleFrequency_Type()
)
vhostCounterGetWebRTCIdleFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostCounterGetWebRTCIdleFrequency.setStatus("current")
_VhostConnectTable_Object = MibTable
vhostConnectTable = _VhostConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2)
)
if mibBuilder.loadTexts:
    vhostConnectTable.setStatus("current")
_VhostConnectEntry_Object = MibTableRow
vhostConnectEntry = _VhostConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1)
)
vhostConnectEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
)
if mibBuilder.loadTexts:
    vhostConnectEntry.setStatus("current")
_VhostConnectCreationTime_Type = Counter64
_VhostConnectCreationTime_Object = MibTableColumn
vhostConnectCreationTime = _VhostConnectCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1, 1),
    _VhostConnectCreationTime_Type()
)
vhostConnectCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostConnectCreationTime.setStatus("current")
_VhostConnectGetCurrent_Type = Counter64
_VhostConnectGetCurrent_Object = MibTableColumn
vhostConnectGetCurrent = _VhostConnectGetCurrent_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1, 2),
    _VhostConnectGetCurrent_Type()
)
vhostConnectGetCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostConnectGetCurrent.setStatus("current")
_VhostConnectGetLastConnectAcceptedStamp_Type = Counter64
_VhostConnectGetLastConnectAcceptedStamp_Object = MibTableColumn
vhostConnectGetLastConnectAcceptedStamp = _VhostConnectGetLastConnectAcceptedStamp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1, 3),
    _VhostConnectGetLastConnectAcceptedStamp_Type()
)
vhostConnectGetLastConnectAcceptedStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostConnectGetLastConnectAcceptedStamp.setStatus("current")
_VhostConnectGetLastConnectAcceptedStampString_Type = DisplayString
_VhostConnectGetLastConnectAcceptedStampString_Object = MibTableColumn
vhostConnectGetLastConnectAcceptedStampString = _VhostConnectGetLastConnectAcceptedStampString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1, 4),
    _VhostConnectGetLastConnectAcceptedStampString_Type()
)
vhostConnectGetLastConnectAcceptedStampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostConnectGetLastConnectAcceptedStampString.setStatus("current")
_VhostConnectGetLastConnectAcceptedTimeString_Type = DisplayString
_VhostConnectGetLastConnectAcceptedTimeString_Object = MibTableColumn
vhostConnectGetLastConnectAcceptedTimeString = _VhostConnectGetLastConnectAcceptedTimeString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1, 5),
    _VhostConnectGetLastConnectAcceptedTimeString_Type()
)
vhostConnectGetLastConnectAcceptedTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostConnectGetLastConnectAcceptedTimeString.setStatus("current")
_VhostConnectGetLastConnectRejectedStamp_Type = Counter64
_VhostConnectGetLastConnectRejectedStamp_Object = MibTableColumn
vhostConnectGetLastConnectRejectedStamp = _VhostConnectGetLastConnectRejectedStamp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1, 6),
    _VhostConnectGetLastConnectRejectedStamp_Type()
)
vhostConnectGetLastConnectRejectedStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostConnectGetLastConnectRejectedStamp.setStatus("current")
_VhostConnectGetLastConnectRejectedStampString_Type = DisplayString
_VhostConnectGetLastConnectRejectedStampString_Object = MibTableColumn
vhostConnectGetLastConnectRejectedStampString = _VhostConnectGetLastConnectRejectedStampString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1, 7),
    _VhostConnectGetLastConnectRejectedStampString_Type()
)
vhostConnectGetLastConnectRejectedStampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostConnectGetLastConnectRejectedStampString.setStatus("current")
_VhostConnectGetLastConnectRejectedTimeString_Type = DisplayString
_VhostConnectGetLastConnectRejectedTimeString_Object = MibTableColumn
vhostConnectGetLastConnectRejectedTimeString = _VhostConnectGetLastConnectRejectedTimeString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1, 8),
    _VhostConnectGetLastConnectRejectedTimeString_Type()
)
vhostConnectGetLastConnectRejectedTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostConnectGetLastConnectRejectedTimeString.setStatus("current")
_VhostConnectGetLastDisconnectStamp_Type = Counter64
_VhostConnectGetLastDisconnectStamp_Object = MibTableColumn
vhostConnectGetLastDisconnectStamp = _VhostConnectGetLastDisconnectStamp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1, 9),
    _VhostConnectGetLastDisconnectStamp_Type()
)
vhostConnectGetLastDisconnectStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostConnectGetLastDisconnectStamp.setStatus("current")
_VhostConnectGetLastDisconnectStampString_Type = DisplayString
_VhostConnectGetLastDisconnectStampString_Object = MibTableColumn
vhostConnectGetLastDisconnectStampString = _VhostConnectGetLastDisconnectStampString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1, 10),
    _VhostConnectGetLastDisconnectStampString_Type()
)
vhostConnectGetLastDisconnectStampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostConnectGetLastDisconnectStampString.setStatus("current")
_VhostConnectGetLastDisconnectTimeString_Type = DisplayString
_VhostConnectGetLastDisconnectTimeString_Object = MibTableColumn
vhostConnectGetLastDisconnectTimeString = _VhostConnectGetLastDisconnectTimeString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1, 11),
    _VhostConnectGetLastDisconnectTimeString_Type()
)
vhostConnectGetLastDisconnectTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostConnectGetLastDisconnectTimeString.setStatus("current")
_VhostConnectGetTotal_Type = Counter64
_VhostConnectGetTotal_Object = MibTableColumn
vhostConnectGetTotal = _VhostConnectGetTotal_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1, 12),
    _VhostConnectGetTotal_Type()
)
vhostConnectGetTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostConnectGetTotal.setStatus("current")
_VhostConnectGetTotalAccepted_Type = Counter64
_VhostConnectGetTotalAccepted_Object = MibTableColumn
vhostConnectGetTotalAccepted = _VhostConnectGetTotalAccepted_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1, 13),
    _VhostConnectGetTotalAccepted_Type()
)
vhostConnectGetTotalAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostConnectGetTotalAccepted.setStatus("current")
_VhostConnectGetTotalRejected_Type = Counter64
_VhostConnectGetTotalRejected_Object = MibTableColumn
vhostConnectGetTotalRejected = _VhostConnectGetTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 2, 1, 14),
    _VhostConnectGetTotalRejected_Type()
)
vhostConnectGetTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostConnectGetTotalRejected.setStatus("current")
_VhostPerformTable_Object = MibTable
vhostPerformTable = _VhostPerformTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 3)
)
if mibBuilder.loadTexts:
    vhostPerformTable.setStatus("current")
_VhostPerformEntry_Object = MibTableRow
vhostPerformEntry = _VhostPerformEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 3, 1)
)
vhostPerformEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
)
if mibBuilder.loadTexts:
    vhostPerformEntry.setStatus("current")
_VhostPerformCreationTime_Type = Counter64
_VhostPerformCreationTime_Object = MibTableColumn
vhostPerformCreationTime = _VhostPerformCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 3, 1, 1),
    _VhostPerformCreationTime_Type()
)
vhostPerformCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostPerformCreationTime.setStatus("current")
_VhostPerformGetFileInBytes_Type = Counter64
_VhostPerformGetFileInBytes_Object = MibTableColumn
vhostPerformGetFileInBytes = _VhostPerformGetFileInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 3, 1, 2),
    _VhostPerformGetFileInBytes_Type()
)
vhostPerformGetFileInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostPerformGetFileInBytes.setStatus("current")
_VhostPerformGetFileOutBytes_Type = Counter64
_VhostPerformGetFileOutBytes_Object = MibTableColumn
vhostPerformGetFileOutBytes = _VhostPerformGetFileOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 3, 1, 3),
    _VhostPerformGetFileOutBytes_Type()
)
vhostPerformGetFileOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostPerformGetFileOutBytes.setStatus("current")
_VhostPerformGetMessagesInBytes_Type = Counter64
_VhostPerformGetMessagesInBytes_Object = MibTableColumn
vhostPerformGetMessagesInBytes = _VhostPerformGetMessagesInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 3, 1, 4),
    _VhostPerformGetMessagesInBytes_Type()
)
vhostPerformGetMessagesInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostPerformGetMessagesInBytes.setStatus("current")
_VhostPerformGetMessagesInCount_Type = Counter64
_VhostPerformGetMessagesInCount_Object = MibTableColumn
vhostPerformGetMessagesInCount = _VhostPerformGetMessagesInCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 3, 1, 5),
    _VhostPerformGetMessagesInCount_Type()
)
vhostPerformGetMessagesInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostPerformGetMessagesInCount.setStatus("current")
_VhostPerformGetMessagesInCountRate_Type = Counter64
_VhostPerformGetMessagesInCountRate_Object = MibTableColumn
vhostPerformGetMessagesInCountRate = _VhostPerformGetMessagesInCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 3, 1, 6),
    _VhostPerformGetMessagesInCountRate_Type()
)
vhostPerformGetMessagesInCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostPerformGetMessagesInCountRate.setStatus("current")
_VhostPerformGetMessagesLossBytes_Type = Counter64
_VhostPerformGetMessagesLossBytes_Object = MibTableColumn
vhostPerformGetMessagesLossBytes = _VhostPerformGetMessagesLossBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 3, 1, 7),
    _VhostPerformGetMessagesLossBytes_Type()
)
vhostPerformGetMessagesLossBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostPerformGetMessagesLossBytes.setStatus("current")
_VhostPerformGetMessagesLossCount_Type = Counter64
_VhostPerformGetMessagesLossCount_Object = MibTableColumn
vhostPerformGetMessagesLossCount = _VhostPerformGetMessagesLossCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 3, 1, 8),
    _VhostPerformGetMessagesLossCount_Type()
)
vhostPerformGetMessagesLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostPerformGetMessagesLossCount.setStatus("current")
_VhostPerformGetMessagesLossCountRate_Type = Counter64
_VhostPerformGetMessagesLossCountRate_Object = MibTableColumn
vhostPerformGetMessagesLossCountRate = _VhostPerformGetMessagesLossCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 3, 1, 9),
    _VhostPerformGetMessagesLossCountRate_Type()
)
vhostPerformGetMessagesLossCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostPerformGetMessagesLossCountRate.setStatus("current")
_VhostPerformGetMessagesOutBytes_Type = Counter64
_VhostPerformGetMessagesOutBytes_Object = MibTableColumn
vhostPerformGetMessagesOutBytes = _VhostPerformGetMessagesOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 3, 1, 10),
    _VhostPerformGetMessagesOutBytes_Type()
)
vhostPerformGetMessagesOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostPerformGetMessagesOutBytes.setStatus("current")
_VhostPerformGetMessagesOutCount_Type = Counter64
_VhostPerformGetMessagesOutCount_Object = MibTableColumn
vhostPerformGetMessagesOutCount = _VhostPerformGetMessagesOutCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 3, 1, 11),
    _VhostPerformGetMessagesOutCount_Type()
)
vhostPerformGetMessagesOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostPerformGetMessagesOutCount.setStatus("current")
_VhostPerformGetMessagesOutCountRate_Type = Counter64
_VhostPerformGetMessagesOutCountRate_Object = MibTableColumn
vhostPerformGetMessagesOutCountRate = _VhostPerformGetMessagesOutCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 20, 1, 3, 1, 12),
    _VhostPerformGetMessagesOutCountRate_Type()
)
vhostPerformGetMessagesOutCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vhostPerformGetMessagesOutCountRate.setStatus("current")
_Applications_ObjectIdentity = ObjectIdentity
applications = _Applications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30)
)
_ApplicationInfo_ObjectIdentity = ObjectIdentity
applicationInfo = _ApplicationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1)
)
_ApplicationCounterTable_Object = MibTable
applicationCounterTable = _ApplicationCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1)
)
if mibBuilder.loadTexts:
    applicationCounterTable.setStatus("current")
_ApplicationCounterEntry_Object = MibTableRow
applicationCounterEntry = _ApplicationCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1, 1)
)
applicationCounterEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
)
if mibBuilder.loadTexts:
    applicationCounterEntry.setStatus("current")
_ApplicationCounterCreationTime_Type = Counter64
_ApplicationCounterCreationTime_Object = MibTableColumn
applicationCounterCreationTime = _ApplicationCounterCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1, 1, 1),
    _ApplicationCounterCreationTime_Type()
)
applicationCounterCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationCounterCreationTime.setStatus("current")
_ApplicationCounterGetApplicationPath_Type = DisplayString
_ApplicationCounterGetApplicationPath_Object = MibTableColumn
applicationCounterGetApplicationPath = _ApplicationCounterGetApplicationPath_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1, 1, 2),
    _ApplicationCounterGetApplicationPath_Type()
)
applicationCounterGetApplicationPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationCounterGetApplicationPath.setStatus("current")
_ApplicationCounterGetConfigPath_Type = DisplayString
_ApplicationCounterGetConfigPath_Object = MibTableColumn
applicationCounterGetConfigPath = _ApplicationCounterGetConfigPath_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1, 1, 3),
    _ApplicationCounterGetConfigPath_Type()
)
applicationCounterGetConfigPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationCounterGetConfigPath.setStatus("current")
_ApplicationCounterGetDateStarted_Type = DisplayString
_ApplicationCounterGetDateStarted_Object = MibTableColumn
applicationCounterGetDateStarted = _ApplicationCounterGetDateStarted_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1, 1, 4),
    _ApplicationCounterGetDateStarted_Type()
)
applicationCounterGetDateStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationCounterGetDateStarted.setStatus("current")
_ApplicationCounterGetInstanceCount_Type = Integer32
_ApplicationCounterGetInstanceCount_Object = MibTableColumn
applicationCounterGetInstanceCount = _ApplicationCounterGetInstanceCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1, 1, 5),
    _ApplicationCounterGetInstanceCount_Type()
)
applicationCounterGetInstanceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationCounterGetInstanceCount.setStatus("current")
_ApplicationCounterGetMessagesInBytes_Type = Counter64
_ApplicationCounterGetMessagesInBytes_Object = MibTableColumn
applicationCounterGetMessagesInBytes = _ApplicationCounterGetMessagesInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1, 1, 6),
    _ApplicationCounterGetMessagesInBytes_Type()
)
applicationCounterGetMessagesInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationCounterGetMessagesInBytes.setStatus("current")
_ApplicationCounterGetMessagesInCount_Type = Counter64
_ApplicationCounterGetMessagesInCount_Object = MibTableColumn
applicationCounterGetMessagesInCount = _ApplicationCounterGetMessagesInCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1, 1, 7),
    _ApplicationCounterGetMessagesInCount_Type()
)
applicationCounterGetMessagesInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationCounterGetMessagesInCount.setStatus("current")
_ApplicationCounterGetMessagesInCountRate_Type = Counter64
_ApplicationCounterGetMessagesInCountRate_Object = MibTableColumn
applicationCounterGetMessagesInCountRate = _ApplicationCounterGetMessagesInCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1, 1, 8),
    _ApplicationCounterGetMessagesInCountRate_Type()
)
applicationCounterGetMessagesInCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationCounterGetMessagesInCountRate.setStatus("current")
_ApplicationCounterGetMessagesOutBytes_Type = Counter64
_ApplicationCounterGetMessagesOutBytes_Object = MibTableColumn
applicationCounterGetMessagesOutBytes = _ApplicationCounterGetMessagesOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1, 1, 9),
    _ApplicationCounterGetMessagesOutBytes_Type()
)
applicationCounterGetMessagesOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationCounterGetMessagesOutBytes.setStatus("current")
_ApplicationCounterGetMessagesOutCount_Type = Counter64
_ApplicationCounterGetMessagesOutCount_Object = MibTableColumn
applicationCounterGetMessagesOutCount = _ApplicationCounterGetMessagesOutCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1, 1, 10),
    _ApplicationCounterGetMessagesOutCount_Type()
)
applicationCounterGetMessagesOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationCounterGetMessagesOutCount.setStatus("current")
_ApplicationCounterGetMessagesOutCountRate_Type = Counter64
_ApplicationCounterGetMessagesOutCountRate_Object = MibTableColumn
applicationCounterGetMessagesOutCountRate = _ApplicationCounterGetMessagesOutCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1, 1, 11),
    _ApplicationCounterGetMessagesOutCountRate_Type()
)
applicationCounterGetMessagesOutCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationCounterGetMessagesOutCountRate.setStatus("current")
_ApplicationCounterGetName_Type = DisplayString
_ApplicationCounterGetName_Object = MibTableColumn
applicationCounterGetName = _ApplicationCounterGetName_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1, 1, 12),
    _ApplicationCounterGetName_Type()
)
applicationCounterGetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationCounterGetName.setStatus("current")
_ApplicationCounterGetTimeRunning_Type = DisplayString
_ApplicationCounterGetTimeRunning_Object = MibTableColumn
applicationCounterGetTimeRunning = _ApplicationCounterGetTimeRunning_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 1, 1, 13),
    _ApplicationCounterGetTimeRunning_Type()
)
applicationCounterGetTimeRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationCounterGetTimeRunning.setStatus("current")
_ApplicationConnectTable_Object = MibTable
applicationConnectTable = _ApplicationConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2)
)
if mibBuilder.loadTexts:
    applicationConnectTable.setStatus("current")
_ApplicationConnectEntry_Object = MibTableRow
applicationConnectEntry = _ApplicationConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1)
)
applicationConnectEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
)
if mibBuilder.loadTexts:
    applicationConnectEntry.setStatus("current")
_ApplicationConnectCreationTime_Type = Counter64
_ApplicationConnectCreationTime_Object = MibTableColumn
applicationConnectCreationTime = _ApplicationConnectCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1, 1),
    _ApplicationConnectCreationTime_Type()
)
applicationConnectCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationConnectCreationTime.setStatus("current")
_ApplicationConnectGetCurrent_Type = Counter64
_ApplicationConnectGetCurrent_Object = MibTableColumn
applicationConnectGetCurrent = _ApplicationConnectGetCurrent_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1, 2),
    _ApplicationConnectGetCurrent_Type()
)
applicationConnectGetCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationConnectGetCurrent.setStatus("current")
_ApplicationConnectGetLastConnectAcceptedStamp_Type = Counter64
_ApplicationConnectGetLastConnectAcceptedStamp_Object = MibTableColumn
applicationConnectGetLastConnectAcceptedStamp = _ApplicationConnectGetLastConnectAcceptedStamp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1, 3),
    _ApplicationConnectGetLastConnectAcceptedStamp_Type()
)
applicationConnectGetLastConnectAcceptedStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationConnectGetLastConnectAcceptedStamp.setStatus("current")
_ApplicationConnectGetLastConnectAcceptedStampString_Type = DisplayString
_ApplicationConnectGetLastConnectAcceptedStampString_Object = MibTableColumn
applicationConnectGetLastConnectAcceptedStampString = _ApplicationConnectGetLastConnectAcceptedStampString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1, 4),
    _ApplicationConnectGetLastConnectAcceptedStampString_Type()
)
applicationConnectGetLastConnectAcceptedStampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationConnectGetLastConnectAcceptedStampString.setStatus("current")
_ApplicationConnectGetLastConnectAcceptedTimeString_Type = DisplayString
_ApplicationConnectGetLastConnectAcceptedTimeString_Object = MibTableColumn
applicationConnectGetLastConnectAcceptedTimeString = _ApplicationConnectGetLastConnectAcceptedTimeString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1, 5),
    _ApplicationConnectGetLastConnectAcceptedTimeString_Type()
)
applicationConnectGetLastConnectAcceptedTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationConnectGetLastConnectAcceptedTimeString.setStatus("current")
_ApplicationConnectGetLastConnectRejectedStamp_Type = Counter64
_ApplicationConnectGetLastConnectRejectedStamp_Object = MibTableColumn
applicationConnectGetLastConnectRejectedStamp = _ApplicationConnectGetLastConnectRejectedStamp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1, 6),
    _ApplicationConnectGetLastConnectRejectedStamp_Type()
)
applicationConnectGetLastConnectRejectedStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationConnectGetLastConnectRejectedStamp.setStatus("current")
_ApplicationConnectGetLastConnectRejectedStampString_Type = DisplayString
_ApplicationConnectGetLastConnectRejectedStampString_Object = MibTableColumn
applicationConnectGetLastConnectRejectedStampString = _ApplicationConnectGetLastConnectRejectedStampString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1, 7),
    _ApplicationConnectGetLastConnectRejectedStampString_Type()
)
applicationConnectGetLastConnectRejectedStampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationConnectGetLastConnectRejectedStampString.setStatus("current")
_ApplicationConnectGetLastConnectRejectedTimeString_Type = DisplayString
_ApplicationConnectGetLastConnectRejectedTimeString_Object = MibTableColumn
applicationConnectGetLastConnectRejectedTimeString = _ApplicationConnectGetLastConnectRejectedTimeString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1, 8),
    _ApplicationConnectGetLastConnectRejectedTimeString_Type()
)
applicationConnectGetLastConnectRejectedTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationConnectGetLastConnectRejectedTimeString.setStatus("current")
_ApplicationConnectGetLastDisconnectStamp_Type = Counter64
_ApplicationConnectGetLastDisconnectStamp_Object = MibTableColumn
applicationConnectGetLastDisconnectStamp = _ApplicationConnectGetLastDisconnectStamp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1, 9),
    _ApplicationConnectGetLastDisconnectStamp_Type()
)
applicationConnectGetLastDisconnectStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationConnectGetLastDisconnectStamp.setStatus("current")
_ApplicationConnectGetLastDisconnectStampString_Type = DisplayString
_ApplicationConnectGetLastDisconnectStampString_Object = MibTableColumn
applicationConnectGetLastDisconnectStampString = _ApplicationConnectGetLastDisconnectStampString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1, 10),
    _ApplicationConnectGetLastDisconnectStampString_Type()
)
applicationConnectGetLastDisconnectStampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationConnectGetLastDisconnectStampString.setStatus("current")
_ApplicationConnectGetLastDisconnectTimeString_Type = DisplayString
_ApplicationConnectGetLastDisconnectTimeString_Object = MibTableColumn
applicationConnectGetLastDisconnectTimeString = _ApplicationConnectGetLastDisconnectTimeString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1, 11),
    _ApplicationConnectGetLastDisconnectTimeString_Type()
)
applicationConnectGetLastDisconnectTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationConnectGetLastDisconnectTimeString.setStatus("current")
_ApplicationConnectGetTotal_Type = Counter64
_ApplicationConnectGetTotal_Object = MibTableColumn
applicationConnectGetTotal = _ApplicationConnectGetTotal_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1, 12),
    _ApplicationConnectGetTotal_Type()
)
applicationConnectGetTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationConnectGetTotal.setStatus("current")
_ApplicationConnectGetTotalAccepted_Type = Counter64
_ApplicationConnectGetTotalAccepted_Object = MibTableColumn
applicationConnectGetTotalAccepted = _ApplicationConnectGetTotalAccepted_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1, 13),
    _ApplicationConnectGetTotalAccepted_Type()
)
applicationConnectGetTotalAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationConnectGetTotalAccepted.setStatus("current")
_ApplicationConnectGetTotalRejected_Type = Counter64
_ApplicationConnectGetTotalRejected_Object = MibTableColumn
applicationConnectGetTotalRejected = _ApplicationConnectGetTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 2, 1, 14),
    _ApplicationConnectGetTotalRejected_Type()
)
applicationConnectGetTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationConnectGetTotalRejected.setStatus("current")
_ApplicationPerformTable_Object = MibTable
applicationPerformTable = _ApplicationPerformTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 3)
)
if mibBuilder.loadTexts:
    applicationPerformTable.setStatus("current")
_ApplicationPerformEntry_Object = MibTableRow
applicationPerformEntry = _ApplicationPerformEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 3, 1)
)
applicationPerformEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
)
if mibBuilder.loadTexts:
    applicationPerformEntry.setStatus("current")
_ApplicationPerformCreationTime_Type = Counter64
_ApplicationPerformCreationTime_Object = MibTableColumn
applicationPerformCreationTime = _ApplicationPerformCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 3, 1, 1),
    _ApplicationPerformCreationTime_Type()
)
applicationPerformCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationPerformCreationTime.setStatus("current")
_ApplicationPerformGetFileInBytes_Type = Counter64
_ApplicationPerformGetFileInBytes_Object = MibTableColumn
applicationPerformGetFileInBytes = _ApplicationPerformGetFileInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 3, 1, 2),
    _ApplicationPerformGetFileInBytes_Type()
)
applicationPerformGetFileInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationPerformGetFileInBytes.setStatus("current")
_ApplicationPerformGetFileOutBytes_Type = Counter64
_ApplicationPerformGetFileOutBytes_Object = MibTableColumn
applicationPerformGetFileOutBytes = _ApplicationPerformGetFileOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 3, 1, 3),
    _ApplicationPerformGetFileOutBytes_Type()
)
applicationPerformGetFileOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationPerformGetFileOutBytes.setStatus("current")
_ApplicationPerformGetMessagesInBytes_Type = Counter64
_ApplicationPerformGetMessagesInBytes_Object = MibTableColumn
applicationPerformGetMessagesInBytes = _ApplicationPerformGetMessagesInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 3, 1, 4),
    _ApplicationPerformGetMessagesInBytes_Type()
)
applicationPerformGetMessagesInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationPerformGetMessagesInBytes.setStatus("current")
_ApplicationPerformGetMessagesInCount_Type = Counter64
_ApplicationPerformGetMessagesInCount_Object = MibTableColumn
applicationPerformGetMessagesInCount = _ApplicationPerformGetMessagesInCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 3, 1, 5),
    _ApplicationPerformGetMessagesInCount_Type()
)
applicationPerformGetMessagesInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationPerformGetMessagesInCount.setStatus("current")
_ApplicationPerformGetMessagesInCountRate_Type = Counter64
_ApplicationPerformGetMessagesInCountRate_Object = MibTableColumn
applicationPerformGetMessagesInCountRate = _ApplicationPerformGetMessagesInCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 3, 1, 6),
    _ApplicationPerformGetMessagesInCountRate_Type()
)
applicationPerformGetMessagesInCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationPerformGetMessagesInCountRate.setStatus("current")
_ApplicationPerformGetMessagesLossBytes_Type = Counter64
_ApplicationPerformGetMessagesLossBytes_Object = MibTableColumn
applicationPerformGetMessagesLossBytes = _ApplicationPerformGetMessagesLossBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 3, 1, 7),
    _ApplicationPerformGetMessagesLossBytes_Type()
)
applicationPerformGetMessagesLossBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationPerformGetMessagesLossBytes.setStatus("current")
_ApplicationPerformGetMessagesLossCount_Type = Counter64
_ApplicationPerformGetMessagesLossCount_Object = MibTableColumn
applicationPerformGetMessagesLossCount = _ApplicationPerformGetMessagesLossCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 3, 1, 8),
    _ApplicationPerformGetMessagesLossCount_Type()
)
applicationPerformGetMessagesLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationPerformGetMessagesLossCount.setStatus("current")
_ApplicationPerformGetMessagesLossCountRate_Type = Counter64
_ApplicationPerformGetMessagesLossCountRate_Object = MibTableColumn
applicationPerformGetMessagesLossCountRate = _ApplicationPerformGetMessagesLossCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 3, 1, 9),
    _ApplicationPerformGetMessagesLossCountRate_Type()
)
applicationPerformGetMessagesLossCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationPerformGetMessagesLossCountRate.setStatus("current")
_ApplicationPerformGetMessagesOutBytes_Type = Counter64
_ApplicationPerformGetMessagesOutBytes_Object = MibTableColumn
applicationPerformGetMessagesOutBytes = _ApplicationPerformGetMessagesOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 3, 1, 10),
    _ApplicationPerformGetMessagesOutBytes_Type()
)
applicationPerformGetMessagesOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationPerformGetMessagesOutBytes.setStatus("current")
_ApplicationPerformGetMessagesOutCount_Type = Counter64
_ApplicationPerformGetMessagesOutCount_Object = MibTableColumn
applicationPerformGetMessagesOutCount = _ApplicationPerformGetMessagesOutCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 3, 1, 11),
    _ApplicationPerformGetMessagesOutCount_Type()
)
applicationPerformGetMessagesOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationPerformGetMessagesOutCount.setStatus("current")
_ApplicationPerformGetMessagesOutCountRate_Type = Counter64
_ApplicationPerformGetMessagesOutCountRate_Object = MibTableColumn
applicationPerformGetMessagesOutCountRate = _ApplicationPerformGetMessagesOutCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 30, 1, 3, 1, 12),
    _ApplicationPerformGetMessagesOutCountRate_Type()
)
applicationPerformGetMessagesOutCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationPerformGetMessagesOutCountRate.setStatus("current")
_ApplicationInstances_ObjectIdentity = ObjectIdentity
applicationInstances = _ApplicationInstances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40)
)
_ApplicationInstanceInfo_ObjectIdentity = ObjectIdentity
applicationInstanceInfo = _ApplicationInstanceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1)
)
_ApplicationInstanceCounterTable_Object = MibTable
applicationInstanceCounterTable = _ApplicationInstanceCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1)
)
if mibBuilder.loadTexts:
    applicationInstanceCounterTable.setStatus("current")
_ApplicationInstanceCounterEntry_Object = MibTableRow
applicationInstanceCounterEntry = _ApplicationInstanceCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1)
)
applicationInstanceCounterEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceIndex"),
)
if mibBuilder.loadTexts:
    applicationInstanceCounterEntry.setStatus("current")
_ApplicationInstanceCounterCreationTime_Type = Counter64
_ApplicationInstanceCounterCreationTime_Object = MibTableColumn
applicationInstanceCounterCreationTime = _ApplicationInstanceCounterCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 1),
    _ApplicationInstanceCounterCreationTime_Type()
)
applicationInstanceCounterCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterCreationTime.setStatus("current")
_ApplicationInstanceCounterGetApplicationInstanceTouchTimeout_Type = Integer32
_ApplicationInstanceCounterGetApplicationInstanceTouchTimeout_Object = MibTableColumn
applicationInstanceCounterGetApplicationInstanceTouchTimeout = _ApplicationInstanceCounterGetApplicationInstanceTouchTimeout_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 2),
    _ApplicationInstanceCounterGetApplicationInstanceTouchTimeout_Type()
)
applicationInstanceCounterGetApplicationInstanceTouchTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetApplicationInstanceTouchTimeout.setStatus("current")
_ApplicationInstanceCounterGetApplicationTimeout_Type = Integer32
_ApplicationInstanceCounterGetApplicationTimeout_Object = MibTableColumn
applicationInstanceCounterGetApplicationTimeout = _ApplicationInstanceCounterGetApplicationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 3),
    _ApplicationInstanceCounterGetApplicationTimeout_Type()
)
applicationInstanceCounterGetApplicationTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetApplicationTimeout.setStatus("current")
_ApplicationInstanceCounterGetClientCount_Type = Integer32
_ApplicationInstanceCounterGetClientCount_Object = MibTableColumn
applicationInstanceCounterGetClientCount = _ApplicationInstanceCounterGetClientCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 4),
    _ApplicationInstanceCounterGetClientCount_Type()
)
applicationInstanceCounterGetClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetClientCount.setStatus("current")
_ApplicationInstanceCounterGetClientCountTotal_Type = Integer32
_ApplicationInstanceCounterGetClientCountTotal_Object = MibTableColumn
applicationInstanceCounterGetClientCountTotal = _ApplicationInstanceCounterGetClientCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 5),
    _ApplicationInstanceCounterGetClientCountTotal_Type()
)
applicationInstanceCounterGetClientCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetClientCountTotal.setStatus("current")
_ApplicationInstanceCounterGetClientIdleFrequency_Type = Integer32
_ApplicationInstanceCounterGetClientIdleFrequency_Object = MibTableColumn
applicationInstanceCounterGetClientIdleFrequency = _ApplicationInstanceCounterGetClientIdleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 6),
    _ApplicationInstanceCounterGetClientIdleFrequency_Type()
)
applicationInstanceCounterGetClientIdleFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetClientIdleFrequency.setStatus("current")
_ApplicationInstanceCounterGetClientRemoveTime_Type = Counter64
_ApplicationInstanceCounterGetClientRemoveTime_Object = MibTableColumn
applicationInstanceCounterGetClientRemoveTime = _ApplicationInstanceCounterGetClientRemoveTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 7),
    _ApplicationInstanceCounterGetClientRemoveTime_Type()
)
applicationInstanceCounterGetClientRemoveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetClientRemoveTime.setStatus("current")
_ApplicationInstanceCounterGetContextStr_Type = DisplayString
_ApplicationInstanceCounterGetContextStr_Object = MibTableColumn
applicationInstanceCounterGetContextStr = _ApplicationInstanceCounterGetContextStr_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 8),
    _ApplicationInstanceCounterGetContextStr_Type()
)
applicationInstanceCounterGetContextStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetContextStr.setStatus("current")
_ApplicationInstanceCounterGetDateStarted_Type = DisplayString
_ApplicationInstanceCounterGetDateStarted_Object = MibTableColumn
applicationInstanceCounterGetDateStarted = _ApplicationInstanceCounterGetDateStarted_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 9),
    _ApplicationInstanceCounterGetDateStarted_Type()
)
applicationInstanceCounterGetDateStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetDateStarted.setStatus("current")
_ApplicationInstanceCounterGetDvrRecorderList_Type = DisplayString
_ApplicationInstanceCounterGetDvrRecorderList_Object = MibTableColumn
applicationInstanceCounterGetDvrRecorderList = _ApplicationInstanceCounterGetDvrRecorderList_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 10),
    _ApplicationInstanceCounterGetDvrRecorderList_Type()
)
applicationInstanceCounterGetDvrRecorderList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetDvrRecorderList.setStatus("current")
_ApplicationInstanceCounterGetHTTPStreamerList_Type = DisplayString
_ApplicationInstanceCounterGetHTTPStreamerList_Object = MibTableColumn
applicationInstanceCounterGetHTTPStreamerList = _ApplicationInstanceCounterGetHTTPStreamerList_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 11),
    _ApplicationInstanceCounterGetHTTPStreamerList_Type()
)
applicationInstanceCounterGetHTTPStreamerList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetHTTPStreamerList.setStatus("current")
_ApplicationInstanceCounterGetHTTPStreamerSessionCount_Type = Integer32
_ApplicationInstanceCounterGetHTTPStreamerSessionCount_Object = MibTableColumn
applicationInstanceCounterGetHTTPStreamerSessionCount = _ApplicationInstanceCounterGetHTTPStreamerSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 12),
    _ApplicationInstanceCounterGetHTTPStreamerSessionCount_Type()
)
applicationInstanceCounterGetHTTPStreamerSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetHTTPStreamerSessionCount.setStatus("current")
_ApplicationInstanceCounterGetLastTouchTime_Type = Counter64
_ApplicationInstanceCounterGetLastTouchTime_Object = MibTableColumn
applicationInstanceCounterGetLastTouchTime = _ApplicationInstanceCounterGetLastTouchTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 13),
    _ApplicationInstanceCounterGetLastTouchTime_Type()
)
applicationInstanceCounterGetLastTouchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetLastTouchTime.setStatus("current")
_ApplicationInstanceCounterGetLiveStreamPacketizerList_Type = DisplayString
_ApplicationInstanceCounterGetLiveStreamPacketizerList_Object = MibTableColumn
applicationInstanceCounterGetLiveStreamPacketizerList = _ApplicationInstanceCounterGetLiveStreamPacketizerList_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 14),
    _ApplicationInstanceCounterGetLiveStreamPacketizerList_Type()
)
applicationInstanceCounterGetLiveStreamPacketizerList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetLiveStreamPacketizerList.setStatus("current")
_ApplicationInstanceCounterGetLiveStreamTranscoderList_Type = DisplayString
_ApplicationInstanceCounterGetLiveStreamTranscoderList_Object = MibTableColumn
applicationInstanceCounterGetLiveStreamTranscoderList = _ApplicationInstanceCounterGetLiveStreamTranscoderList_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 15),
    _ApplicationInstanceCounterGetLiveStreamTranscoderList_Type()
)
applicationInstanceCounterGetLiveStreamTranscoderList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetLiveStreamTranscoderList.setStatus("current")
_ApplicationInstanceCounterGetMaxStorageDirDepth_Type = Integer32
_ApplicationInstanceCounterGetMaxStorageDirDepth_Object = MibTableColumn
applicationInstanceCounterGetMaxStorageDirDepth = _ApplicationInstanceCounterGetMaxStorageDirDepth_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 16),
    _ApplicationInstanceCounterGetMaxStorageDirDepth_Type()
)
applicationInstanceCounterGetMaxStorageDirDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetMaxStorageDirDepth.setStatus("current")
_ApplicationInstanceCounterGetMaximumPendingReadBytes_Type = Integer32
_ApplicationInstanceCounterGetMaximumPendingReadBytes_Object = MibTableColumn
applicationInstanceCounterGetMaximumPendingReadBytes = _ApplicationInstanceCounterGetMaximumPendingReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 17),
    _ApplicationInstanceCounterGetMaximumPendingReadBytes_Type()
)
applicationInstanceCounterGetMaximumPendingReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetMaximumPendingReadBytes.setStatus("current")
_ApplicationInstanceCounterGetMaximumPendingWriteBytes_Type = Integer32
_ApplicationInstanceCounterGetMaximumPendingWriteBytes_Object = MibTableColumn
applicationInstanceCounterGetMaximumPendingWriteBytes = _ApplicationInstanceCounterGetMaximumPendingWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 18),
    _ApplicationInstanceCounterGetMaximumPendingWriteBytes_Type()
)
applicationInstanceCounterGetMaximumPendingWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetMaximumPendingWriteBytes.setStatus("current")
_ApplicationInstanceCounterGetMaximumSetBufferTime_Type = Integer32
_ApplicationInstanceCounterGetMaximumSetBufferTime_Object = MibTableColumn
applicationInstanceCounterGetMaximumSetBufferTime = _ApplicationInstanceCounterGetMaximumSetBufferTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 19),
    _ApplicationInstanceCounterGetMaximumSetBufferTime_Type()
)
applicationInstanceCounterGetMaximumSetBufferTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetMaximumSetBufferTime.setStatus("current")
_ApplicationInstanceCounterGetMediacasterRTPRTSPRTPTransportMode_Type = Integer32
_ApplicationInstanceCounterGetMediacasterRTPRTSPRTPTransportMode_Object = MibTableColumn
applicationInstanceCounterGetMediacasterRTPRTSPRTPTransportMode = _ApplicationInstanceCounterGetMediacasterRTPRTSPRTPTransportMode_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 20),
    _ApplicationInstanceCounterGetMediacasterRTPRTSPRTPTransportMode_Type()
)
applicationInstanceCounterGetMediacasterRTPRTSPRTPTransportMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetMediacasterRTPRTSPRTPTransportMode.setStatus("current")
_ApplicationInstanceCounterGetMessagesInBytes_Type = Counter64
_ApplicationInstanceCounterGetMessagesInBytes_Object = MibTableColumn
applicationInstanceCounterGetMessagesInBytes = _ApplicationInstanceCounterGetMessagesInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 21),
    _ApplicationInstanceCounterGetMessagesInBytes_Type()
)
applicationInstanceCounterGetMessagesInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetMessagesInBytes.setStatus("current")
_ApplicationInstanceCounterGetMessagesInCount_Type = Counter64
_ApplicationInstanceCounterGetMessagesInCount_Object = MibTableColumn
applicationInstanceCounterGetMessagesInCount = _ApplicationInstanceCounterGetMessagesInCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 22),
    _ApplicationInstanceCounterGetMessagesInCount_Type()
)
applicationInstanceCounterGetMessagesInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetMessagesInCount.setStatus("current")
_ApplicationInstanceCounterGetMessagesInCountRate_Type = Counter64
_ApplicationInstanceCounterGetMessagesInCountRate_Object = MibTableColumn
applicationInstanceCounterGetMessagesInCountRate = _ApplicationInstanceCounterGetMessagesInCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 23),
    _ApplicationInstanceCounterGetMessagesInCountRate_Type()
)
applicationInstanceCounterGetMessagesInCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetMessagesInCountRate.setStatus("current")
_ApplicationInstanceCounterGetMessagesOutBytes_Type = Counter64
_ApplicationInstanceCounterGetMessagesOutBytes_Object = MibTableColumn
applicationInstanceCounterGetMessagesOutBytes = _ApplicationInstanceCounterGetMessagesOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 24),
    _ApplicationInstanceCounterGetMessagesOutBytes_Type()
)
applicationInstanceCounterGetMessagesOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetMessagesOutBytes.setStatus("current")
_ApplicationInstanceCounterGetMessagesOutCount_Type = Counter64
_ApplicationInstanceCounterGetMessagesOutCount_Object = MibTableColumn
applicationInstanceCounterGetMessagesOutCount = _ApplicationInstanceCounterGetMessagesOutCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 25),
    _ApplicationInstanceCounterGetMessagesOutCount_Type()
)
applicationInstanceCounterGetMessagesOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetMessagesOutCount.setStatus("current")
_ApplicationInstanceCounterGetMessagesOutCountRate_Type = Counter64
_ApplicationInstanceCounterGetMessagesOutCountRate_Object = MibTableColumn
applicationInstanceCounterGetMessagesOutCountRate = _ApplicationInstanceCounterGetMessagesOutCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 26),
    _ApplicationInstanceCounterGetMessagesOutCountRate_Type()
)
applicationInstanceCounterGetMessagesOutCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetMessagesOutCountRate.setStatus("current")
_ApplicationInstanceCounterGetName_Type = DisplayString
_ApplicationInstanceCounterGetName_Object = MibTableColumn
applicationInstanceCounterGetName = _ApplicationInstanceCounterGetName_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 27),
    _ApplicationInstanceCounterGetName_Type()
)
applicationInstanceCounterGetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetName.setStatus("current")
_ApplicationInstanceCounterGetPingTimeout_Type = Integer32
_ApplicationInstanceCounterGetPingTimeout_Object = MibTableColumn
applicationInstanceCounterGetPingTimeout = _ApplicationInstanceCounterGetPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 28),
    _ApplicationInstanceCounterGetPingTimeout_Type()
)
applicationInstanceCounterGetPingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetPingTimeout.setStatus("current")
_ApplicationInstanceCounterGetPublisherCount_Type = Integer32
_ApplicationInstanceCounterGetPublisherCount_Object = MibTableColumn
applicationInstanceCounterGetPublisherCount = _ApplicationInstanceCounterGetPublisherCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 29),
    _ApplicationInstanceCounterGetPublisherCount_Type()
)
applicationInstanceCounterGetPublisherCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetPublisherCount.setStatus("current")
_ApplicationInstanceCounterGetPushPublishSessionCount_Type = Integer32
_ApplicationInstanceCounterGetPushPublishSessionCount_Object = MibTableColumn
applicationInstanceCounterGetPushPublishSessionCount = _ApplicationInstanceCounterGetPushPublishSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 30),
    _ApplicationInstanceCounterGetPushPublishSessionCount_Type()
)
applicationInstanceCounterGetPushPublishSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetPushPublishSessionCount.setStatus("current")
_ApplicationInstanceCounterGetRTPAVSyncMethod_Type = Integer32
_ApplicationInstanceCounterGetRTPAVSyncMethod_Object = MibTableColumn
applicationInstanceCounterGetRTPAVSyncMethod = _ApplicationInstanceCounterGetRTPAVSyncMethod_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 31),
    _ApplicationInstanceCounterGetRTPAVSyncMethod_Type()
)
applicationInstanceCounterGetRTPAVSyncMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRTPAVSyncMethod.setStatus("current")
_ApplicationInstanceCounterGetRTPIdleFrequency_Type = Integer32
_ApplicationInstanceCounterGetRTPIdleFrequency_Object = MibTableColumn
applicationInstanceCounterGetRTPIdleFrequency = _ApplicationInstanceCounterGetRTPIdleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 32),
    _ApplicationInstanceCounterGetRTPIdleFrequency_Type()
)
applicationInstanceCounterGetRTPIdleFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRTPIdleFrequency.setStatus("current")
_ApplicationInstanceCounterGetRTPMaxRTCPWaitTime_Type = Integer32
_ApplicationInstanceCounterGetRTPMaxRTCPWaitTime_Object = MibTableColumn
applicationInstanceCounterGetRTPMaxRTCPWaitTime = _ApplicationInstanceCounterGetRTPMaxRTCPWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 33),
    _ApplicationInstanceCounterGetRTPMaxRTCPWaitTime_Type()
)
applicationInstanceCounterGetRTPMaxRTCPWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRTPMaxRTCPWaitTime.setStatus("current")
_ApplicationInstanceCounterGetRTPPlayAuthenticationMethod_Type = DisplayString
_ApplicationInstanceCounterGetRTPPlayAuthenticationMethod_Object = MibTableColumn
applicationInstanceCounterGetRTPPlayAuthenticationMethod = _ApplicationInstanceCounterGetRTPPlayAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 34),
    _ApplicationInstanceCounterGetRTPPlayAuthenticationMethod_Type()
)
applicationInstanceCounterGetRTPPlayAuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRTPPlayAuthenticationMethod.setStatus("current")
_ApplicationInstanceCounterGetRTPPublishAuthenticationMethod_Type = DisplayString
_ApplicationInstanceCounterGetRTPPublishAuthenticationMethod_Object = MibTableColumn
applicationInstanceCounterGetRTPPublishAuthenticationMethod = _ApplicationInstanceCounterGetRTPPublishAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 35),
    _ApplicationInstanceCounterGetRTPPublishAuthenticationMethod_Type()
)
applicationInstanceCounterGetRTPPublishAuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRTPPublishAuthenticationMethod.setStatus("current")
_ApplicationInstanceCounterGetRTPSessionCount_Type = Integer32
_ApplicationInstanceCounterGetRTPSessionCount_Object = MibTableColumn
applicationInstanceCounterGetRTPSessionCount = _ApplicationInstanceCounterGetRTPSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 36),
    _ApplicationInstanceCounterGetRTPSessionCount_Type()
)
applicationInstanceCounterGetRTPSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRTPSessionCount.setStatus("current")
_ApplicationInstanceCounterGetRTSPBindIpAddress_Type = DisplayString
_ApplicationInstanceCounterGetRTSPBindIpAddress_Object = MibTableColumn
applicationInstanceCounterGetRTSPBindIpAddress = _ApplicationInstanceCounterGetRTSPBindIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 37),
    _ApplicationInstanceCounterGetRTSPBindIpAddress_Type()
)
applicationInstanceCounterGetRTSPBindIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRTSPBindIpAddress.setStatus("current")
_ApplicationInstanceCounterGetRTSPConnectionAddressType_Type = DisplayString
_ApplicationInstanceCounterGetRTSPConnectionAddressType_Object = MibTableColumn
applicationInstanceCounterGetRTSPConnectionAddressType = _ApplicationInstanceCounterGetRTSPConnectionAddressType_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 38),
    _ApplicationInstanceCounterGetRTSPConnectionAddressType_Type()
)
applicationInstanceCounterGetRTSPConnectionAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRTSPConnectionAddressType.setStatus("current")
_ApplicationInstanceCounterGetRTSPConnectionIpAddress_Type = DisplayString
_ApplicationInstanceCounterGetRTSPConnectionIpAddress_Object = MibTableColumn
applicationInstanceCounterGetRTSPConnectionIpAddress = _ApplicationInstanceCounterGetRTSPConnectionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 39),
    _ApplicationInstanceCounterGetRTSPConnectionIpAddress_Type()
)
applicationInstanceCounterGetRTSPConnectionIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRTSPConnectionIpAddress.setStatus("current")
_ApplicationInstanceCounterGetRTSPMaximumPendingWriteBytes_Type = Integer32
_ApplicationInstanceCounterGetRTSPMaximumPendingWriteBytes_Object = MibTableColumn
applicationInstanceCounterGetRTSPMaximumPendingWriteBytes = _ApplicationInstanceCounterGetRTSPMaximumPendingWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 40),
    _ApplicationInstanceCounterGetRTSPMaximumPendingWriteBytes_Type()
)
applicationInstanceCounterGetRTSPMaximumPendingWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRTSPMaximumPendingWriteBytes.setStatus("current")
_ApplicationInstanceCounterGetRTSPOriginAddressType_Type = DisplayString
_ApplicationInstanceCounterGetRTSPOriginAddressType_Object = MibTableColumn
applicationInstanceCounterGetRTSPOriginAddressType = _ApplicationInstanceCounterGetRTSPOriginAddressType_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 41),
    _ApplicationInstanceCounterGetRTSPOriginAddressType_Type()
)
applicationInstanceCounterGetRTSPOriginAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRTSPOriginAddressType.setStatus("current")
_ApplicationInstanceCounterGetRTSPOriginIpAddress_Type = DisplayString
_ApplicationInstanceCounterGetRTSPOriginIpAddress_Object = MibTableColumn
applicationInstanceCounterGetRTSPOriginIpAddress = _ApplicationInstanceCounterGetRTSPOriginIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 42),
    _ApplicationInstanceCounterGetRTSPOriginIpAddress_Type()
)
applicationInstanceCounterGetRTSPOriginIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRTSPOriginIpAddress.setStatus("current")
_ApplicationInstanceCounterGetRTSPSessionTimeout_Type = Integer32
_ApplicationInstanceCounterGetRTSPSessionTimeout_Object = MibTableColumn
applicationInstanceCounterGetRTSPSessionTimeout = _ApplicationInstanceCounterGetRTSPSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 43),
    _ApplicationInstanceCounterGetRTSPSessionTimeout_Type()
)
applicationInstanceCounterGetRTSPSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRTSPSessionTimeout.setStatus("current")
_ApplicationInstanceCounterGetRepeaterOriginUrl_Type = DisplayString
_ApplicationInstanceCounterGetRepeaterOriginUrl_Object = MibTableColumn
applicationInstanceCounterGetRepeaterOriginUrl = _ApplicationInstanceCounterGetRepeaterOriginUrl_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 44),
    _ApplicationInstanceCounterGetRepeaterOriginUrl_Type()
)
applicationInstanceCounterGetRepeaterOriginUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRepeaterOriginUrl.setStatus("current")
_ApplicationInstanceCounterGetRepeaterQueryString_Type = DisplayString
_ApplicationInstanceCounterGetRepeaterQueryString_Object = MibTableColumn
applicationInstanceCounterGetRepeaterQueryString = _ApplicationInstanceCounterGetRepeaterQueryString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 45),
    _ApplicationInstanceCounterGetRepeaterQueryString_Type()
)
applicationInstanceCounterGetRepeaterQueryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRepeaterQueryString.setStatus("current")
_ApplicationInstanceCounterGetRsoStorageDir_Type = DisplayString
_ApplicationInstanceCounterGetRsoStorageDir_Object = MibTableColumn
applicationInstanceCounterGetRsoStorageDir = _ApplicationInstanceCounterGetRsoStorageDir_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 46),
    _ApplicationInstanceCounterGetRsoStorageDir_Type()
)
applicationInstanceCounterGetRsoStorageDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRsoStorageDir.setStatus("current")
_ApplicationInstanceCounterGetRsoStoragePath_Type = DisplayString
_ApplicationInstanceCounterGetRsoStoragePath_Object = MibTableColumn
applicationInstanceCounterGetRsoStoragePath = _ApplicationInstanceCounterGetRsoStoragePath_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 47),
    _ApplicationInstanceCounterGetRsoStoragePath_Type()
)
applicationInstanceCounterGetRsoStoragePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetRsoStoragePath.setStatus("current")
_ApplicationInstanceCounterGetSharedObjectReadAccess_Type = DisplayString
_ApplicationInstanceCounterGetSharedObjectReadAccess_Object = MibTableColumn
applicationInstanceCounterGetSharedObjectReadAccess = _ApplicationInstanceCounterGetSharedObjectReadAccess_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 48),
    _ApplicationInstanceCounterGetSharedObjectReadAccess_Type()
)
applicationInstanceCounterGetSharedObjectReadAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetSharedObjectReadAccess.setStatus("current")
_ApplicationInstanceCounterGetSharedObjectWriteAccess_Type = DisplayString
_ApplicationInstanceCounterGetSharedObjectWriteAccess_Object = MibTableColumn
applicationInstanceCounterGetSharedObjectWriteAccess = _ApplicationInstanceCounterGetSharedObjectWriteAccess_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 49),
    _ApplicationInstanceCounterGetSharedObjectWriteAccess_Type()
)
applicationInstanceCounterGetSharedObjectWriteAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetSharedObjectWriteAccess.setStatus("current")
_ApplicationInstanceCounterGetSourceControlSessionCount_Type = Integer32
_ApplicationInstanceCounterGetSourceControlSessionCount_Object = MibTableColumn
applicationInstanceCounterGetSourceControlSessionCount = _ApplicationInstanceCounterGetSourceControlSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 50),
    _ApplicationInstanceCounterGetSourceControlSessionCount_Type()
)
applicationInstanceCounterGetSourceControlSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetSourceControlSessionCount.setStatus("current")
_ApplicationInstanceCounterGetStreamAudioSampleAccess_Type = DisplayString
_ApplicationInstanceCounterGetStreamAudioSampleAccess_Object = MibTableColumn
applicationInstanceCounterGetStreamAudioSampleAccess = _ApplicationInstanceCounterGetStreamAudioSampleAccess_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 51),
    _ApplicationInstanceCounterGetStreamAudioSampleAccess_Type()
)
applicationInstanceCounterGetStreamAudioSampleAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetStreamAudioSampleAccess.setStatus("current")
_ApplicationInstanceCounterGetStreamCount_Type = Integer32
_ApplicationInstanceCounterGetStreamCount_Object = MibTableColumn
applicationInstanceCounterGetStreamCount = _ApplicationInstanceCounterGetStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 52),
    _ApplicationInstanceCounterGetStreamCount_Type()
)
applicationInstanceCounterGetStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetStreamCount.setStatus("current")
_ApplicationInstanceCounterGetStreamKeyDir_Type = DisplayString
_ApplicationInstanceCounterGetStreamKeyDir_Object = MibTableColumn
applicationInstanceCounterGetStreamKeyDir = _ApplicationInstanceCounterGetStreamKeyDir_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 53),
    _ApplicationInstanceCounterGetStreamKeyDir_Type()
)
applicationInstanceCounterGetStreamKeyDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetStreamKeyDir.setStatus("current")
_ApplicationInstanceCounterGetStreamKeyPath_Type = DisplayString
_ApplicationInstanceCounterGetStreamKeyPath_Object = MibTableColumn
applicationInstanceCounterGetStreamKeyPath = _ApplicationInstanceCounterGetStreamKeyPath_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 54),
    _ApplicationInstanceCounterGetStreamKeyPath_Type()
)
applicationInstanceCounterGetStreamKeyPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetStreamKeyPath.setStatus("current")
_ApplicationInstanceCounterGetStreamReadAccess_Type = DisplayString
_ApplicationInstanceCounterGetStreamReadAccess_Object = MibTableColumn
applicationInstanceCounterGetStreamReadAccess = _ApplicationInstanceCounterGetStreamReadAccess_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 55),
    _ApplicationInstanceCounterGetStreamReadAccess_Type()
)
applicationInstanceCounterGetStreamReadAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetStreamReadAccess.setStatus("current")
_ApplicationInstanceCounterGetStreamStorageDir_Type = DisplayString
_ApplicationInstanceCounterGetStreamStorageDir_Object = MibTableColumn
applicationInstanceCounterGetStreamStorageDir = _ApplicationInstanceCounterGetStreamStorageDir_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 56),
    _ApplicationInstanceCounterGetStreamStorageDir_Type()
)
applicationInstanceCounterGetStreamStorageDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetStreamStorageDir.setStatus("current")
_ApplicationInstanceCounterGetStreamStoragePath_Type = DisplayString
_ApplicationInstanceCounterGetStreamStoragePath_Object = MibTableColumn
applicationInstanceCounterGetStreamStoragePath = _ApplicationInstanceCounterGetStreamStoragePath_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 57),
    _ApplicationInstanceCounterGetStreamStoragePath_Type()
)
applicationInstanceCounterGetStreamStoragePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetStreamStoragePath.setStatus("current")
_ApplicationInstanceCounterGetStreamType_Type = DisplayString
_ApplicationInstanceCounterGetStreamType_Object = MibTableColumn
applicationInstanceCounterGetStreamType = _ApplicationInstanceCounterGetStreamType_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 58),
    _ApplicationInstanceCounterGetStreamType_Type()
)
applicationInstanceCounterGetStreamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetStreamType.setStatus("current")
_ApplicationInstanceCounterGetStreamVideoSampleAccess_Type = DisplayString
_ApplicationInstanceCounterGetStreamVideoSampleAccess_Object = MibTableColumn
applicationInstanceCounterGetStreamVideoSampleAccess = _ApplicationInstanceCounterGetStreamVideoSampleAccess_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 59),
    _ApplicationInstanceCounterGetStreamVideoSampleAccess_Type()
)
applicationInstanceCounterGetStreamVideoSampleAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetStreamVideoSampleAccess.setStatus("current")
_ApplicationInstanceCounterGetStreamWriteAccess_Type = DisplayString
_ApplicationInstanceCounterGetStreamWriteAccess_Object = MibTableColumn
applicationInstanceCounterGetStreamWriteAccess = _ApplicationInstanceCounterGetStreamWriteAccess_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 60),
    _ApplicationInstanceCounterGetStreamWriteAccess_Type()
)
applicationInstanceCounterGetStreamWriteAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetStreamWriteAccess.setStatus("current")
_ApplicationInstanceCounterGetTimeRunning_Type = DisplayString
_ApplicationInstanceCounterGetTimeRunning_Object = MibTableColumn
applicationInstanceCounterGetTimeRunning = _ApplicationInstanceCounterGetTimeRunning_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 61),
    _ApplicationInstanceCounterGetTimeRunning_Type()
)
applicationInstanceCounterGetTimeRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetTimeRunning.setStatus("current")
_ApplicationInstanceCounterGetVODTimedTextProviderList_Type = DisplayString
_ApplicationInstanceCounterGetVODTimedTextProviderList_Object = MibTableColumn
applicationInstanceCounterGetVODTimedTextProviderList = _ApplicationInstanceCounterGetVODTimedTextProviderList_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 62),
    _ApplicationInstanceCounterGetVODTimedTextProviderList_Type()
)
applicationInstanceCounterGetVODTimedTextProviderList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetVODTimedTextProviderList.setStatus("current")
_ApplicationInstanceCounterGetValidationFrequency_Type = Integer32
_ApplicationInstanceCounterGetValidationFrequency_Object = MibTableColumn
applicationInstanceCounterGetValidationFrequency = _ApplicationInstanceCounterGetValidationFrequency_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 1, 1, 63),
    _ApplicationInstanceCounterGetValidationFrequency_Type()
)
applicationInstanceCounterGetValidationFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceCounterGetValidationFrequency.setStatus("current")
_ApplicationInstanceConnectTable_Object = MibTable
applicationInstanceConnectTable = _ApplicationInstanceConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2)
)
if mibBuilder.loadTexts:
    applicationInstanceConnectTable.setStatus("current")
_ApplicationInstanceConnectEntry_Object = MibTableRow
applicationInstanceConnectEntry = _ApplicationInstanceConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1)
)
applicationInstanceConnectEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceIndex"),
)
if mibBuilder.loadTexts:
    applicationInstanceConnectEntry.setStatus("current")
_ApplicationInstanceConnectCreationTime_Type = Counter64
_ApplicationInstanceConnectCreationTime_Object = MibTableColumn
applicationInstanceConnectCreationTime = _ApplicationInstanceConnectCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1, 1),
    _ApplicationInstanceConnectCreationTime_Type()
)
applicationInstanceConnectCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceConnectCreationTime.setStatus("current")
_ApplicationInstanceConnectGetCurrent_Type = Counter64
_ApplicationInstanceConnectGetCurrent_Object = MibTableColumn
applicationInstanceConnectGetCurrent = _ApplicationInstanceConnectGetCurrent_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1, 2),
    _ApplicationInstanceConnectGetCurrent_Type()
)
applicationInstanceConnectGetCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceConnectGetCurrent.setStatus("current")
_ApplicationInstanceConnectGetLastConnectAcceptedStamp_Type = Counter64
_ApplicationInstanceConnectGetLastConnectAcceptedStamp_Object = MibTableColumn
applicationInstanceConnectGetLastConnectAcceptedStamp = _ApplicationInstanceConnectGetLastConnectAcceptedStamp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1, 3),
    _ApplicationInstanceConnectGetLastConnectAcceptedStamp_Type()
)
applicationInstanceConnectGetLastConnectAcceptedStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceConnectGetLastConnectAcceptedStamp.setStatus("current")
_ApplicationInstanceConnectGetLastConnectAcceptedStampString_Type = DisplayString
_ApplicationInstanceConnectGetLastConnectAcceptedStampString_Object = MibTableColumn
applicationInstanceConnectGetLastConnectAcceptedStampString = _ApplicationInstanceConnectGetLastConnectAcceptedStampString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1, 4),
    _ApplicationInstanceConnectGetLastConnectAcceptedStampString_Type()
)
applicationInstanceConnectGetLastConnectAcceptedStampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceConnectGetLastConnectAcceptedStampString.setStatus("current")
_ApplicationInstanceConnectGetLastConnectAcceptedTimeString_Type = DisplayString
_ApplicationInstanceConnectGetLastConnectAcceptedTimeString_Object = MibTableColumn
applicationInstanceConnectGetLastConnectAcceptedTimeString = _ApplicationInstanceConnectGetLastConnectAcceptedTimeString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1, 5),
    _ApplicationInstanceConnectGetLastConnectAcceptedTimeString_Type()
)
applicationInstanceConnectGetLastConnectAcceptedTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceConnectGetLastConnectAcceptedTimeString.setStatus("current")
_ApplicationInstanceConnectGetLastConnectRejectedStamp_Type = Counter64
_ApplicationInstanceConnectGetLastConnectRejectedStamp_Object = MibTableColumn
applicationInstanceConnectGetLastConnectRejectedStamp = _ApplicationInstanceConnectGetLastConnectRejectedStamp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1, 6),
    _ApplicationInstanceConnectGetLastConnectRejectedStamp_Type()
)
applicationInstanceConnectGetLastConnectRejectedStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceConnectGetLastConnectRejectedStamp.setStatus("current")
_ApplicationInstanceConnectGetLastConnectRejectedStampString_Type = DisplayString
_ApplicationInstanceConnectGetLastConnectRejectedStampString_Object = MibTableColumn
applicationInstanceConnectGetLastConnectRejectedStampString = _ApplicationInstanceConnectGetLastConnectRejectedStampString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1, 7),
    _ApplicationInstanceConnectGetLastConnectRejectedStampString_Type()
)
applicationInstanceConnectGetLastConnectRejectedStampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceConnectGetLastConnectRejectedStampString.setStatus("current")
_ApplicationInstanceConnectGetLastConnectRejectedTimeString_Type = DisplayString
_ApplicationInstanceConnectGetLastConnectRejectedTimeString_Object = MibTableColumn
applicationInstanceConnectGetLastConnectRejectedTimeString = _ApplicationInstanceConnectGetLastConnectRejectedTimeString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1, 8),
    _ApplicationInstanceConnectGetLastConnectRejectedTimeString_Type()
)
applicationInstanceConnectGetLastConnectRejectedTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceConnectGetLastConnectRejectedTimeString.setStatus("current")
_ApplicationInstanceConnectGetLastDisconnectStamp_Type = Counter64
_ApplicationInstanceConnectGetLastDisconnectStamp_Object = MibTableColumn
applicationInstanceConnectGetLastDisconnectStamp = _ApplicationInstanceConnectGetLastDisconnectStamp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1, 9),
    _ApplicationInstanceConnectGetLastDisconnectStamp_Type()
)
applicationInstanceConnectGetLastDisconnectStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceConnectGetLastDisconnectStamp.setStatus("current")
_ApplicationInstanceConnectGetLastDisconnectStampString_Type = DisplayString
_ApplicationInstanceConnectGetLastDisconnectStampString_Object = MibTableColumn
applicationInstanceConnectGetLastDisconnectStampString = _ApplicationInstanceConnectGetLastDisconnectStampString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1, 10),
    _ApplicationInstanceConnectGetLastDisconnectStampString_Type()
)
applicationInstanceConnectGetLastDisconnectStampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceConnectGetLastDisconnectStampString.setStatus("current")
_ApplicationInstanceConnectGetLastDisconnectTimeString_Type = DisplayString
_ApplicationInstanceConnectGetLastDisconnectTimeString_Object = MibTableColumn
applicationInstanceConnectGetLastDisconnectTimeString = _ApplicationInstanceConnectGetLastDisconnectTimeString_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1, 11),
    _ApplicationInstanceConnectGetLastDisconnectTimeString_Type()
)
applicationInstanceConnectGetLastDisconnectTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceConnectGetLastDisconnectTimeString.setStatus("current")
_ApplicationInstanceConnectGetTotal_Type = Counter64
_ApplicationInstanceConnectGetTotal_Object = MibTableColumn
applicationInstanceConnectGetTotal = _ApplicationInstanceConnectGetTotal_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1, 12),
    _ApplicationInstanceConnectGetTotal_Type()
)
applicationInstanceConnectGetTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceConnectGetTotal.setStatus("current")
_ApplicationInstanceConnectGetTotalAccepted_Type = Counter64
_ApplicationInstanceConnectGetTotalAccepted_Object = MibTableColumn
applicationInstanceConnectGetTotalAccepted = _ApplicationInstanceConnectGetTotalAccepted_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1, 13),
    _ApplicationInstanceConnectGetTotalAccepted_Type()
)
applicationInstanceConnectGetTotalAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceConnectGetTotalAccepted.setStatus("current")
_ApplicationInstanceConnectGetTotalRejected_Type = Counter64
_ApplicationInstanceConnectGetTotalRejected_Object = MibTableColumn
applicationInstanceConnectGetTotalRejected = _ApplicationInstanceConnectGetTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 2, 1, 14),
    _ApplicationInstanceConnectGetTotalRejected_Type()
)
applicationInstanceConnectGetTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstanceConnectGetTotalRejected.setStatus("current")
_ApplicationInstancePerformTable_Object = MibTable
applicationInstancePerformTable = _ApplicationInstancePerformTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 3)
)
if mibBuilder.loadTexts:
    applicationInstancePerformTable.setStatus("current")
_ApplicationInstancePerformEntry_Object = MibTableRow
applicationInstancePerformEntry = _ApplicationInstancePerformEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 3, 1)
)
applicationInstancePerformEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceIndex"),
)
if mibBuilder.loadTexts:
    applicationInstancePerformEntry.setStatus("current")
_ApplicationInstancePerformCreationTime_Type = Counter64
_ApplicationInstancePerformCreationTime_Object = MibTableColumn
applicationInstancePerformCreationTime = _ApplicationInstancePerformCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 3, 1, 1),
    _ApplicationInstancePerformCreationTime_Type()
)
applicationInstancePerformCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstancePerformCreationTime.setStatus("current")
_ApplicationInstancePerformGetFileInBytes_Type = Counter64
_ApplicationInstancePerformGetFileInBytes_Object = MibTableColumn
applicationInstancePerformGetFileInBytes = _ApplicationInstancePerformGetFileInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 3, 1, 2),
    _ApplicationInstancePerformGetFileInBytes_Type()
)
applicationInstancePerformGetFileInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstancePerformGetFileInBytes.setStatus("current")
_ApplicationInstancePerformGetFileOutBytes_Type = Counter64
_ApplicationInstancePerformGetFileOutBytes_Object = MibTableColumn
applicationInstancePerformGetFileOutBytes = _ApplicationInstancePerformGetFileOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 3, 1, 3),
    _ApplicationInstancePerformGetFileOutBytes_Type()
)
applicationInstancePerformGetFileOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstancePerformGetFileOutBytes.setStatus("current")
_ApplicationInstancePerformGetMessagesInBytes_Type = Counter64
_ApplicationInstancePerformGetMessagesInBytes_Object = MibTableColumn
applicationInstancePerformGetMessagesInBytes = _ApplicationInstancePerformGetMessagesInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 3, 1, 4),
    _ApplicationInstancePerformGetMessagesInBytes_Type()
)
applicationInstancePerformGetMessagesInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstancePerformGetMessagesInBytes.setStatus("current")
_ApplicationInstancePerformGetMessagesInCount_Type = Counter64
_ApplicationInstancePerformGetMessagesInCount_Object = MibTableColumn
applicationInstancePerformGetMessagesInCount = _ApplicationInstancePerformGetMessagesInCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 3, 1, 5),
    _ApplicationInstancePerformGetMessagesInCount_Type()
)
applicationInstancePerformGetMessagesInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstancePerformGetMessagesInCount.setStatus("current")
_ApplicationInstancePerformGetMessagesInCountRate_Type = Counter64
_ApplicationInstancePerformGetMessagesInCountRate_Object = MibTableColumn
applicationInstancePerformGetMessagesInCountRate = _ApplicationInstancePerformGetMessagesInCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 3, 1, 6),
    _ApplicationInstancePerformGetMessagesInCountRate_Type()
)
applicationInstancePerformGetMessagesInCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstancePerformGetMessagesInCountRate.setStatus("current")
_ApplicationInstancePerformGetMessagesLossBytes_Type = Counter64
_ApplicationInstancePerformGetMessagesLossBytes_Object = MibTableColumn
applicationInstancePerformGetMessagesLossBytes = _ApplicationInstancePerformGetMessagesLossBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 3, 1, 7),
    _ApplicationInstancePerformGetMessagesLossBytes_Type()
)
applicationInstancePerformGetMessagesLossBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstancePerformGetMessagesLossBytes.setStatus("current")
_ApplicationInstancePerformGetMessagesLossCount_Type = Counter64
_ApplicationInstancePerformGetMessagesLossCount_Object = MibTableColumn
applicationInstancePerformGetMessagesLossCount = _ApplicationInstancePerformGetMessagesLossCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 3, 1, 8),
    _ApplicationInstancePerformGetMessagesLossCount_Type()
)
applicationInstancePerformGetMessagesLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstancePerformGetMessagesLossCount.setStatus("current")
_ApplicationInstancePerformGetMessagesLossCountRate_Type = Counter64
_ApplicationInstancePerformGetMessagesLossCountRate_Object = MibTableColumn
applicationInstancePerformGetMessagesLossCountRate = _ApplicationInstancePerformGetMessagesLossCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 3, 1, 9),
    _ApplicationInstancePerformGetMessagesLossCountRate_Type()
)
applicationInstancePerformGetMessagesLossCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstancePerformGetMessagesLossCountRate.setStatus("current")
_ApplicationInstancePerformGetMessagesOutBytes_Type = Counter64
_ApplicationInstancePerformGetMessagesOutBytes_Object = MibTableColumn
applicationInstancePerformGetMessagesOutBytes = _ApplicationInstancePerformGetMessagesOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 3, 1, 10),
    _ApplicationInstancePerformGetMessagesOutBytes_Type()
)
applicationInstancePerformGetMessagesOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstancePerformGetMessagesOutBytes.setStatus("current")
_ApplicationInstancePerformGetMessagesOutCount_Type = Counter64
_ApplicationInstancePerformGetMessagesOutCount_Object = MibTableColumn
applicationInstancePerformGetMessagesOutCount = _ApplicationInstancePerformGetMessagesOutCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 3, 1, 11),
    _ApplicationInstancePerformGetMessagesOutCount_Type()
)
applicationInstancePerformGetMessagesOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstancePerformGetMessagesOutCount.setStatus("current")
_ApplicationInstancePerformGetMessagesOutCountRate_Type = Counter64
_ApplicationInstancePerformGetMessagesOutCountRate_Object = MibTableColumn
applicationInstancePerformGetMessagesOutCountRate = _ApplicationInstancePerformGetMessagesOutCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 40, 1, 3, 1, 12),
    _ApplicationInstancePerformGetMessagesOutCountRate_Type()
)
applicationInstancePerformGetMessagesOutCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationInstancePerformGetMessagesOutCountRate.setStatus("current")
_Streams_ObjectIdentity = ObjectIdentity
streams = _Streams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50)
)
_StreamInfo_ObjectIdentity = ObjectIdentity
streamInfo = _StreamInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1)
)
_StreamCountTable_Object = MibTable
streamCountTable = _StreamCountTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1)
)
if mibBuilder.loadTexts:
    streamCountTable.setStatus("current")
_StreamCountEntry_Object = MibTableRow
streamCountEntry = _StreamCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1)
)
streamCountEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "streamIndex"),
)
if mibBuilder.loadTexts:
    streamCountEntry.setStatus("current")
_StreamCountCreationTime_Type = Counter64
_StreamCountCreationTime_Object = MibTableColumn
streamCountCreationTime = _StreamCountCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 1),
    _StreamCountCreationTime_Type()
)
streamCountCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountCreationTime.setStatus("current")
_StreamCountGetAudioMissing_Type = Integer32
_StreamCountGetAudioMissing_Object = MibTableColumn
streamCountGetAudioMissing = _StreamCountGetAudioMissing_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 2),
    _StreamCountGetAudioMissing_Type()
)
streamCountGetAudioMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetAudioMissing.setStatus("current")
_StreamCountGetAudioSize_Type = Integer32
_StreamCountGetAudioSize_Object = MibTableColumn
streamCountGetAudioSize = _StreamCountGetAudioSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 3),
    _StreamCountGetAudioSize_Type()
)
streamCountGetAudioSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetAudioSize.setStatus("current")
_StreamCountGetAudioTC_Type = Counter64
_StreamCountGetAudioTC_Object = MibTableColumn
streamCountGetAudioTC = _StreamCountGetAudioTC_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 4),
    _StreamCountGetAudioTC_Type()
)
streamCountGetAudioTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetAudioTC.setStatus("current")
_StreamCountGetBufferTime_Type = Integer32
_StreamCountGetBufferTime_Object = MibTableColumn
streamCountGetBufferTime = _StreamCountGetBufferTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 5),
    _StreamCountGetBufferTime_Type()
)
streamCountGetBufferTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetBufferTime.setStatus("current")
_StreamCountGetCacheName_Type = DisplayString
_StreamCountGetCacheName_Object = MibTableColumn
streamCountGetCacheName = _StreamCountGetCacheName_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 6),
    _StreamCountGetCacheName_Type()
)
streamCountGetCacheName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetCacheName.setStatus("current")
_StreamCountGetClientId_Type = Integer32
_StreamCountGetClientId_Object = MibTableColumn
streamCountGetClientId = _StreamCountGetClientId_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 7),
    _StreamCountGetClientId_Type()
)
streamCountGetClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetClientId.setStatus("current")
_StreamCountGetContextStr_Type = DisplayString
_StreamCountGetContextStr_Object = MibTableColumn
streamCountGetContextStr = _StreamCountGetContextStr_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 8),
    _StreamCountGetContextStr_Type()
)
streamCountGetContextStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetContextStr.setStatus("current")
_StreamCountGetDataMissing_Type = Integer32
_StreamCountGetDataMissing_Object = MibTableColumn
streamCountGetDataMissing = _StreamCountGetDataMissing_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 9),
    _StreamCountGetDataMissing_Type()
)
streamCountGetDataMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetDataMissing.setStatus("current")
_StreamCountGetDataSize_Type = Integer32
_StreamCountGetDataSize_Object = MibTableColumn
streamCountGetDataSize = _StreamCountGetDataSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 10),
    _StreamCountGetDataSize_Type()
)
streamCountGetDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetDataSize.setStatus("current")
_StreamCountGetDataTC_Type = Counter64
_StreamCountGetDataTC_Object = MibTableColumn
streamCountGetDataTC = _StreamCountGetDataTC_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 11),
    _StreamCountGetDataTC_Type()
)
streamCountGetDataTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetDataTC.setStatus("current")
_StreamCountGetDataType_Type = Integer32
_StreamCountGetDataType_Object = MibTableColumn
streamCountGetDataType = _StreamCountGetDataType_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 12),
    _StreamCountGetDataType_Type()
)
streamCountGetDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetDataType.setStatus("current")
_StreamCountGetDvrRecorder_Type = DisplayString
_StreamCountGetDvrRecorder_Object = MibTableColumn
streamCountGetDvrRecorder = _StreamCountGetDvrRecorder_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 13),
    _StreamCountGetDvrRecorder_Type()
)
streamCountGetDvrRecorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetDvrRecorder.setStatus("current")
_StreamCountGetDvrRecorderList_Type = DisplayString
_StreamCountGetDvrRecorderList_Object = MibTableColumn
streamCountGetDvrRecorderList = _StreamCountGetDvrRecorderList_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 14),
    _StreamCountGetDvrRecorderList_Type()
)
streamCountGetDvrRecorderList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetDvrRecorderList.setStatus("current")
_StreamCountGetDvrRepeater_Type = DisplayString
_StreamCountGetDvrRepeater_Object = MibTableColumn
streamCountGetDvrRepeater = _StreamCountGetDvrRepeater_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 15),
    _StreamCountGetDvrRepeater_Type()
)
streamCountGetDvrRepeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetDvrRepeater.setStatus("current")
_StreamCountGetExt_Type = DisplayString
_StreamCountGetExt_Object = MibTableColumn
streamCountGetExt = _StreamCountGetExt_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 16),
    _StreamCountGetExt_Type()
)
streamCountGetExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetExt.setStatus("current")
_StreamCountGetFirstPacketTC_Type = Counter64
_StreamCountGetFirstPacketTC_Object = MibTableColumn
streamCountGetFirstPacketTC = _StreamCountGetFirstPacketTC_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 17),
    _StreamCountGetFirstPacketTC_Type()
)
streamCountGetFirstPacketTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetFirstPacketTC.setStatus("current")
_StreamCountGetHeaderSize_Type = Integer32
_StreamCountGetHeaderSize_Object = MibTableColumn
streamCountGetHeaderSize = _StreamCountGetHeaderSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 18),
    _StreamCountGetHeaderSize_Type()
)
streamCountGetHeaderSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetHeaderSize.setStatus("current")
_StreamCountGetLastFlushAudioTC_Type = Counter64
_StreamCountGetLastFlushAudioTC_Object = MibTableColumn
streamCountGetLastFlushAudioTC = _StreamCountGetLastFlushAudioTC_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 19),
    _StreamCountGetLastFlushAudioTC_Type()
)
streamCountGetLastFlushAudioTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLastFlushAudioTC.setStatus("current")
_StreamCountGetLastFlushDataTC_Type = Counter64
_StreamCountGetLastFlushDataTC_Object = MibTableColumn
streamCountGetLastFlushDataTC = _StreamCountGetLastFlushDataTC_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 20),
    _StreamCountGetLastFlushDataTC_Type()
)
streamCountGetLastFlushDataTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLastFlushDataTC.setStatus("current")
_StreamCountGetLastFlushRTTimecode_Type = Counter64
_StreamCountGetLastFlushRTTimecode_Object = MibTableColumn
streamCountGetLastFlushRTTimecode = _StreamCountGetLastFlushRTTimecode_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 21),
    _StreamCountGetLastFlushRTTimecode_Type()
)
streamCountGetLastFlushRTTimecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLastFlushRTTimecode.setStatus("current")
_StreamCountGetLastFlushTime_Type = Counter64
_StreamCountGetLastFlushTime_Object = MibTableColumn
streamCountGetLastFlushTime = _StreamCountGetLastFlushTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 22),
    _StreamCountGetLastFlushTime_Type()
)
streamCountGetLastFlushTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLastFlushTime.setStatus("current")
_StreamCountGetLastFlushTimecode_Type = Counter64
_StreamCountGetLastFlushTimecode_Object = MibTableColumn
streamCountGetLastFlushTimecode = _StreamCountGetLastFlushTimecode_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 23),
    _StreamCountGetLastFlushTimecode_Type()
)
streamCountGetLastFlushTimecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLastFlushTimecode.setStatus("current")
_StreamCountGetLastFlushVideoTC_Type = Counter64
_StreamCountGetLastFlushVideoTC_Object = MibTableColumn
streamCountGetLastFlushVideoTC = _StreamCountGetLastFlushVideoTC_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 24),
    _StreamCountGetLastFlushVideoTC_Type()
)
streamCountGetLastFlushVideoTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLastFlushVideoTC.setStatus("current")
_StreamCountGetLastPacketTC_Type = Counter64
_StreamCountGetLastPacketTC_Object = MibTableColumn
streamCountGetLastPacketTC = _StreamCountGetLastPacketTC_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 25),
    _StreamCountGetLastPacketTC_Type()
)
streamCountGetLastPacketTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLastPacketTC.setStatus("current")
_StreamCountGetLastReceivedAudioTC_Type = Counter64
_StreamCountGetLastReceivedAudioTC_Object = MibTableColumn
streamCountGetLastReceivedAudioTC = _StreamCountGetLastReceivedAudioTC_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 26),
    _StreamCountGetLastReceivedAudioTC_Type()
)
streamCountGetLastReceivedAudioTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLastReceivedAudioTC.setStatus("current")
_StreamCountGetLastReceivedDataTC_Type = Counter64
_StreamCountGetLastReceivedDataTC_Object = MibTableColumn
streamCountGetLastReceivedDataTC = _StreamCountGetLastReceivedDataTC_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 27),
    _StreamCountGetLastReceivedDataTC_Type()
)
streamCountGetLastReceivedDataTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLastReceivedDataTC.setStatus("current")
_StreamCountGetLastReceivedVideoTC_Type = Counter64
_StreamCountGetLastReceivedVideoTC_Object = MibTableColumn
streamCountGetLastReceivedVideoTC = _StreamCountGetLastReceivedVideoTC_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 28),
    _StreamCountGetLastReceivedVideoTC_Type()
)
streamCountGetLastReceivedVideoTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLastReceivedVideoTC.setStatus("current")
_StreamCountGetLastSentAudioTC_Type = Counter64
_StreamCountGetLastSentAudioTC_Object = MibTableColumn
streamCountGetLastSentAudioTC = _StreamCountGetLastSentAudioTC_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 29),
    _StreamCountGetLastSentAudioTC_Type()
)
streamCountGetLastSentAudioTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLastSentAudioTC.setStatus("current")
_StreamCountGetLastSentDataTC_Type = Counter64
_StreamCountGetLastSentDataTC_Object = MibTableColumn
streamCountGetLastSentDataTC = _StreamCountGetLastSentDataTC_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 30),
    _StreamCountGetLastSentDataTC_Type()
)
streamCountGetLastSentDataTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLastSentDataTC.setStatus("current")
_StreamCountGetLastSentVideoTC_Type = Counter64
_StreamCountGetLastSentVideoTC_Object = MibTableColumn
streamCountGetLastSentVideoTC = _StreamCountGetLastSentVideoTC_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 31),
    _StreamCountGetLastSentVideoTC_Type()
)
streamCountGetLastSentVideoTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLastSentVideoTC.setStatus("current")
_StreamCountGetLiveStreamPacketizer_Type = DisplayString
_StreamCountGetLiveStreamPacketizer_Object = MibTableColumn
streamCountGetLiveStreamPacketizer = _StreamCountGetLiveStreamPacketizer_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 32),
    _StreamCountGetLiveStreamPacketizer_Type()
)
streamCountGetLiveStreamPacketizer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLiveStreamPacketizer.setStatus("current")
_StreamCountGetLiveStreamPacketizerList_Type = DisplayString
_StreamCountGetLiveStreamPacketizerList_Object = MibTableColumn
streamCountGetLiveStreamPacketizerList = _StreamCountGetLiveStreamPacketizerList_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 33),
    _StreamCountGetLiveStreamPacketizerList_Type()
)
streamCountGetLiveStreamPacketizerList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLiveStreamPacketizerList.setStatus("current")
_StreamCountGetLiveStreamRepeater_Type = DisplayString
_StreamCountGetLiveStreamRepeater_Object = MibTableColumn
streamCountGetLiveStreamRepeater = _StreamCountGetLiveStreamRepeater_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 34),
    _StreamCountGetLiveStreamRepeater_Type()
)
streamCountGetLiveStreamRepeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLiveStreamRepeater.setStatus("current")
_StreamCountGetLiveStreamTranscoderList_Type = DisplayString
_StreamCountGetLiveStreamTranscoderList_Object = MibTableColumn
streamCountGetLiveStreamTranscoderList = _StreamCountGetLiveStreamTranscoderList_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 35),
    _StreamCountGetLiveStreamTranscoderList_Type()
)
streamCountGetLiveStreamTranscoderList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetLiveStreamTranscoderList.setStatus("current")
_StreamCountGetMaxTimecode_Type = Counter64
_StreamCountGetMaxTimecode_Object = MibTableColumn
streamCountGetMaxTimecode = _StreamCountGetMaxTimecode_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 36),
    _StreamCountGetMaxTimecode_Type()
)
streamCountGetMaxTimecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetMaxTimecode.setStatus("current")
_StreamCountGetName_Type = DisplayString
_StreamCountGetName_Object = MibTableColumn
streamCountGetName = _StreamCountGetName_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 37),
    _StreamCountGetName_Type()
)
streamCountGetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetName.setStatus("current")
_StreamCountGetPacketCount_Type = Integer32
_StreamCountGetPacketCount_Object = MibTableColumn
streamCountGetPacketCount = _StreamCountGetPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 38),
    _StreamCountGetPacketCount_Type()
)
streamCountGetPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetPacketCount.setStatus("current")
_StreamCountGetPublishAudioCodecId_Type = Integer32
_StreamCountGetPublishAudioCodecId_Object = MibTableColumn
streamCountGetPublishAudioCodecId = _StreamCountGetPublishAudioCodecId_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 39),
    _StreamCountGetPublishAudioCodecId_Type()
)
streamCountGetPublishAudioCodecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetPublishAudioCodecId.setStatus("current")
_StreamCountGetPublishBitrateAudio_Type = Integer32
_StreamCountGetPublishBitrateAudio_Object = MibTableColumn
streamCountGetPublishBitrateAudio = _StreamCountGetPublishBitrateAudio_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 40),
    _StreamCountGetPublishBitrateAudio_Type()
)
streamCountGetPublishBitrateAudio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetPublishBitrateAudio.setStatus("current")
_StreamCountGetPublishBitrateVideo_Type = Integer32
_StreamCountGetPublishBitrateVideo_Object = MibTableColumn
streamCountGetPublishBitrateVideo = _StreamCountGetPublishBitrateVideo_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 41),
    _StreamCountGetPublishBitrateVideo_Type()
)
streamCountGetPublishBitrateVideo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetPublishBitrateVideo.setStatus("current")
_StreamCountGetPublishFrameCountAudio_Type = Counter64
_StreamCountGetPublishFrameCountAudio_Object = MibTableColumn
streamCountGetPublishFrameCountAudio = _StreamCountGetPublishFrameCountAudio_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 42),
    _StreamCountGetPublishFrameCountAudio_Type()
)
streamCountGetPublishFrameCountAudio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetPublishFrameCountAudio.setStatus("current")
_StreamCountGetPublishFrameCountData_Type = Counter64
_StreamCountGetPublishFrameCountData_Object = MibTableColumn
streamCountGetPublishFrameCountData = _StreamCountGetPublishFrameCountData_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 43),
    _StreamCountGetPublishFrameCountData_Type()
)
streamCountGetPublishFrameCountData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetPublishFrameCountData.setStatus("current")
_StreamCountGetPublishFrameCountVideo_Type = Counter64
_StreamCountGetPublishFrameCountVideo_Object = MibTableColumn
streamCountGetPublishFrameCountVideo = _StreamCountGetPublishFrameCountVideo_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 44),
    _StreamCountGetPublishFrameCountVideo_Type()
)
streamCountGetPublishFrameCountVideo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetPublishFrameCountVideo.setStatus("current")
_StreamCountGetPublishVideoCodecId_Type = Integer32
_StreamCountGetPublishVideoCodecId_Object = MibTableColumn
streamCountGetPublishVideoCodecId = _StreamCountGetPublishVideoCodecId_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 45),
    _StreamCountGetPublishVideoCodecId_Type()
)
streamCountGetPublishVideoCodecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetPublishVideoCodecId.setStatus("current")
_StreamCountGetQueryStr_Type = DisplayString
_StreamCountGetQueryStr_Object = MibTableColumn
streamCountGetQueryStr = _StreamCountGetQueryStr_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 46),
    _StreamCountGetQueryStr_Type()
)
streamCountGetQueryStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetQueryStr.setStatus("current")
_StreamCountGetReceiveVideoFPS_Type = Integer32
_StreamCountGetReceiveVideoFPS_Object = MibTableColumn
streamCountGetReceiveVideoFPS = _StreamCountGetReceiveVideoFPS_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 47),
    _StreamCountGetReceiveVideoFPS_Type()
)
streamCountGetReceiveVideoFPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetReceiveVideoFPS.setStatus("current")
_StreamCountGetSrc_Type = Integer32
_StreamCountGetSrc_Object = MibTableColumn
streamCountGetSrc = _StreamCountGetSrc_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 48),
    _StreamCountGetSrc_Type()
)
streamCountGetSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetSrc.setStatus("current")
_StreamCountGetStreamType_Type = DisplayString
_StreamCountGetStreamType_Object = MibTableColumn
streamCountGetStreamType = _StreamCountGetStreamType_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 49),
    _StreamCountGetStreamType_Type()
)
streamCountGetStreamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetStreamType.setStatus("current")
_StreamCountGetTimecodeOffset_Type = Counter64
_StreamCountGetTimecodeOffset_Object = MibTableColumn
streamCountGetTimecodeOffset = _StreamCountGetTimecodeOffset_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 50),
    _StreamCountGetTimecodeOffset_Type()
)
streamCountGetTimecodeOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetTimecodeOffset.setStatus("current")
_StreamCountGetTss_Type = Counter64
_StreamCountGetTss_Object = MibTableColumn
streamCountGetTss = _StreamCountGetTss_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 51),
    _StreamCountGetTss_Type()
)
streamCountGetTss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetTss.setStatus("current")
_StreamCountGetUniqueStreamIdStr_Type = DisplayString
_StreamCountGetUniqueStreamIdStr_Object = MibTableColumn
streamCountGetUniqueStreamIdStr = _StreamCountGetUniqueStreamIdStr_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 52),
    _StreamCountGetUniqueStreamIdStr_Type()
)
streamCountGetUniqueStreamIdStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetUniqueStreamIdStr.setStatus("current")
_StreamCountGetVideoMissing_Type = Integer32
_StreamCountGetVideoMissing_Object = MibTableColumn
streamCountGetVideoMissing = _StreamCountGetVideoMissing_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 53),
    _StreamCountGetVideoMissing_Type()
)
streamCountGetVideoMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetVideoMissing.setStatus("current")
_StreamCountGetVideoSize_Type = Integer32
_StreamCountGetVideoSize_Object = MibTableColumn
streamCountGetVideoSize = _StreamCountGetVideoSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 54),
    _StreamCountGetVideoSize_Type()
)
streamCountGetVideoSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetVideoSize.setStatus("current")
_StreamCountGetVideoTC_Type = Counter64
_StreamCountGetVideoTC_Object = MibTableColumn
streamCountGetVideoTC = _StreamCountGetVideoTC_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 1, 1, 55),
    _StreamCountGetVideoTC_Type()
)
streamCountGetVideoTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamCountGetVideoTC.setStatus("current")
_StreamPerformTable_Object = MibTable
streamPerformTable = _StreamPerformTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 3)
)
if mibBuilder.loadTexts:
    streamPerformTable.setStatus("current")
_StreamPerformEntry_Object = MibTableRow
streamPerformEntry = _StreamPerformEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 3, 1)
)
streamPerformEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "streamIndex"),
)
if mibBuilder.loadTexts:
    streamPerformEntry.setStatus("current")
_StreamPerformCreationTime_Type = Counter64
_StreamPerformCreationTime_Object = MibTableColumn
streamPerformCreationTime = _StreamPerformCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 3, 1, 1),
    _StreamPerformCreationTime_Type()
)
streamPerformCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamPerformCreationTime.setStatus("current")
_StreamPerformGetFileInBytes_Type = Counter64
_StreamPerformGetFileInBytes_Object = MibTableColumn
streamPerformGetFileInBytes = _StreamPerformGetFileInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 3, 1, 2),
    _StreamPerformGetFileInBytes_Type()
)
streamPerformGetFileInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamPerformGetFileInBytes.setStatus("current")
_StreamPerformGetFileOutBytes_Type = Counter64
_StreamPerformGetFileOutBytes_Object = MibTableColumn
streamPerformGetFileOutBytes = _StreamPerformGetFileOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 3, 1, 3),
    _StreamPerformGetFileOutBytes_Type()
)
streamPerformGetFileOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamPerformGetFileOutBytes.setStatus("current")
_StreamPerformGetMessagesInBytes_Type = Counter64
_StreamPerformGetMessagesInBytes_Object = MibTableColumn
streamPerformGetMessagesInBytes = _StreamPerformGetMessagesInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 3, 1, 4),
    _StreamPerformGetMessagesInBytes_Type()
)
streamPerformGetMessagesInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamPerformGetMessagesInBytes.setStatus("current")
_StreamPerformGetMessagesInCount_Type = Counter64
_StreamPerformGetMessagesInCount_Object = MibTableColumn
streamPerformGetMessagesInCount = _StreamPerformGetMessagesInCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 3, 1, 5),
    _StreamPerformGetMessagesInCount_Type()
)
streamPerformGetMessagesInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamPerformGetMessagesInCount.setStatus("current")
_StreamPerformGetMessagesInCountRate_Type = Counter64
_StreamPerformGetMessagesInCountRate_Object = MibTableColumn
streamPerformGetMessagesInCountRate = _StreamPerformGetMessagesInCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 3, 1, 6),
    _StreamPerformGetMessagesInCountRate_Type()
)
streamPerformGetMessagesInCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamPerformGetMessagesInCountRate.setStatus("current")
_StreamPerformGetMessagesLossBytes_Type = Counter64
_StreamPerformGetMessagesLossBytes_Object = MibTableColumn
streamPerformGetMessagesLossBytes = _StreamPerformGetMessagesLossBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 3, 1, 7),
    _StreamPerformGetMessagesLossBytes_Type()
)
streamPerformGetMessagesLossBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamPerformGetMessagesLossBytes.setStatus("current")
_StreamPerformGetMessagesLossCount_Type = Counter64
_StreamPerformGetMessagesLossCount_Object = MibTableColumn
streamPerformGetMessagesLossCount = _StreamPerformGetMessagesLossCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 3, 1, 8),
    _StreamPerformGetMessagesLossCount_Type()
)
streamPerformGetMessagesLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamPerformGetMessagesLossCount.setStatus("current")
_StreamPerformGetMessagesLossCountRate_Type = Counter64
_StreamPerformGetMessagesLossCountRate_Object = MibTableColumn
streamPerformGetMessagesLossCountRate = _StreamPerformGetMessagesLossCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 3, 1, 9),
    _StreamPerformGetMessagesLossCountRate_Type()
)
streamPerformGetMessagesLossCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamPerformGetMessagesLossCountRate.setStatus("current")
_StreamPerformGetMessagesOutBytes_Type = Counter64
_StreamPerformGetMessagesOutBytes_Object = MibTableColumn
streamPerformGetMessagesOutBytes = _StreamPerformGetMessagesOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 3, 1, 10),
    _StreamPerformGetMessagesOutBytes_Type()
)
streamPerformGetMessagesOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamPerformGetMessagesOutBytes.setStatus("current")
_StreamPerformGetMessagesOutCount_Type = Counter64
_StreamPerformGetMessagesOutCount_Object = MibTableColumn
streamPerformGetMessagesOutCount = _StreamPerformGetMessagesOutCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 3, 1, 11),
    _StreamPerformGetMessagesOutCount_Type()
)
streamPerformGetMessagesOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamPerformGetMessagesOutCount.setStatus("current")
_StreamPerformGetMessagesOutCountRate_Type = Counter64
_StreamPerformGetMessagesOutCountRate_Object = MibTableColumn
streamPerformGetMessagesOutCountRate = _StreamPerformGetMessagesOutCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 50, 1, 3, 1, 12),
    _StreamPerformGetMessagesOutCountRate_Type()
)
streamPerformGetMessagesOutCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamPerformGetMessagesOutCountRate.setStatus("current")
_Rtmpclients_ObjectIdentity = ObjectIdentity
rtmpclients = _Rtmpclients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60)
)
_RtmpclientInfo_ObjectIdentity = ObjectIdentity
rtmpclientInfo = _RtmpclientInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1)
)
_RtmpClientCountTable_Object = MibTable
rtmpClientCountTable = _RtmpClientCountTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1)
)
if mibBuilder.loadTexts:
    rtmpClientCountTable.setStatus("current")
_RtmpClientCountEntry_Object = MibTableRow
rtmpClientCountEntry = _RtmpClientCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1)
)
rtmpClientCountEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "clientIndex"),
)
if mibBuilder.loadTexts:
    rtmpClientCountEntry.setStatus("current")
_RtmpClientCountCreationTime_Type = Counter64
_RtmpClientCountCreationTime_Object = MibTableColumn
rtmpClientCountCreationTime = _RtmpClientCountCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 1),
    _RtmpClientCountCreationTime_Type()
)
rtmpClientCountCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountCreationTime.setStatus("current")
_RtmpClientCountGetAcceptConnectionDescription_Type = DisplayString
_RtmpClientCountGetAcceptConnectionDescription_Object = MibTableColumn
rtmpClientCountGetAcceptConnectionDescription = _RtmpClientCountGetAcceptConnectionDescription_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 2),
    _RtmpClientCountGetAcceptConnectionDescription_Type()
)
rtmpClientCountGetAcceptConnectionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetAcceptConnectionDescription.setStatus("current")
_RtmpClientCountGetBufferTime_Type = Integer32
_RtmpClientCountGetBufferTime_Object = MibTableColumn
rtmpClientCountGetBufferTime = _RtmpClientCountGetBufferTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 3),
    _RtmpClientCountGetBufferTime_Type()
)
rtmpClientCountGetBufferTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetBufferTime.setStatus("current")
_RtmpClientCountGetClientId_Type = Integer32
_RtmpClientCountGetClientId_Object = MibTableColumn
rtmpClientCountGetClientId = _RtmpClientCountGetClientId_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 4),
    _RtmpClientCountGetClientId_Type()
)
rtmpClientCountGetClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetClientId.setStatus("current")
_RtmpClientCountGetConnectTime_Type = Counter64
_RtmpClientCountGetConnectTime_Object = MibTableColumn
rtmpClientCountGetConnectTime = _RtmpClientCountGetConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 5),
    _RtmpClientCountGetConnectTime_Type()
)
rtmpClientCountGetConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetConnectTime.setStatus("current")
_RtmpClientCountGetDateStarted_Type = DisplayString
_RtmpClientCountGetDateStarted_Object = MibTableColumn
rtmpClientCountGetDateStarted = _RtmpClientCountGetDateStarted_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 6),
    _RtmpClientCountGetDateStarted_Type()
)
rtmpClientCountGetDateStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetDateStarted.setStatus("current")
_RtmpClientCountGetDebugDumpData_Type = Integer32
_RtmpClientCountGetDebugDumpData_Object = MibTableColumn
rtmpClientCountGetDebugDumpData = _RtmpClientCountGetDebugDumpData_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 7),
    _RtmpClientCountGetDebugDumpData_Type()
)
rtmpClientCountGetDebugDumpData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetDebugDumpData.setStatus("current")
_RtmpClientCountGetFlashVer_Type = DisplayString
_RtmpClientCountGetFlashVer_Object = MibTableColumn
rtmpClientCountGetFlashVer = _RtmpClientCountGetFlashVer_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 8),
    _RtmpClientCountGetFlashVer_Type()
)
rtmpClientCountGetFlashVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetFlashVer.setStatus("current")
_RtmpClientCountGetHandshake_Type = Integer32
_RtmpClientCountGetHandshake_Object = MibTableColumn
rtmpClientCountGetHandshake = _RtmpClientCountGetHandshake_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 9),
    _RtmpClientCountGetHandshake_Type()
)
rtmpClientCountGetHandshake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetHandshake.setStatus("current")
_RtmpClientCountGetIdleFrequency_Type = Integer32
_RtmpClientCountGetIdleFrequency_Object = MibTableColumn
rtmpClientCountGetIdleFrequency = _RtmpClientCountGetIdleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 10),
    _RtmpClientCountGetIdleFrequency_Type()
)
rtmpClientCountGetIdleFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetIdleFrequency.setStatus("current")
_RtmpClientCountGetIp_Type = DisplayString
_RtmpClientCountGetIp_Object = MibTableColumn
rtmpClientCountGetIp = _RtmpClientCountGetIp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 11),
    _RtmpClientCountGetIp_Type()
)
rtmpClientCountGetIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetIp.setStatus("current")
_RtmpClientCountGetLastPingWriteId_Type = Counter64
_RtmpClientCountGetLastPingWriteId_Object = MibTableColumn
rtmpClientCountGetLastPingWriteId = _RtmpClientCountGetLastPingWriteId_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 12),
    _RtmpClientCountGetLastPingWriteId_Type()
)
rtmpClientCountGetLastPingWriteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetLastPingWriteId.setStatus("current")
_RtmpClientCountGetLastReqChunkCounter_Type = Counter64
_RtmpClientCountGetLastReqChunkCounter_Object = MibTableColumn
rtmpClientCountGetLastReqChunkCounter = _RtmpClientCountGetLastReqChunkCounter_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 13),
    _RtmpClientCountGetLastReqChunkCounter_Type()
)
rtmpClientCountGetLastReqChunkCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetLastReqChunkCounter.setStatus("current")
_RtmpClientCountGetLastRequestType_Type = Integer32
_RtmpClientCountGetLastRequestType_Object = MibTableColumn
rtmpClientCountGetLastRequestType = _RtmpClientCountGetLastRequestType_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 14),
    _RtmpClientCountGetLastRequestType_Type()
)
rtmpClientCountGetLastRequestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetLastRequestType.setStatus("current")
_RtmpClientCountGetLastStreamId_Type = Integer32
_RtmpClientCountGetLastStreamId_Object = MibTableColumn
rtmpClientCountGetLastStreamId = _RtmpClientCountGetLastStreamId_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 15),
    _RtmpClientCountGetLastStreamId_Type()
)
rtmpClientCountGetLastStreamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetLastStreamId.setStatus("current")
_RtmpClientCountGetLastValidateTime_Type = Counter64
_RtmpClientCountGetLastValidateTime_Object = MibTableColumn
rtmpClientCountGetLastValidateTime = _RtmpClientCountGetLastValidateTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 16),
    _RtmpClientCountGetLastValidateTime_Type()
)
rtmpClientCountGetLastValidateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetLastValidateTime.setStatus("current")
_RtmpClientCountGetLeftOverCID_Type = Integer32
_RtmpClientCountGetLeftOverCID_Object = MibTableColumn
rtmpClientCountGetLeftOverCID = _RtmpClientCountGetLeftOverCID_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 17),
    _RtmpClientCountGetLeftOverCID_Type()
)
rtmpClientCountGetLeftOverCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetLeftOverCID.setStatus("current")
_RtmpClientCountGetLeftOverMissing_Type = Integer32
_RtmpClientCountGetLeftOverMissing_Object = MibTableColumn
rtmpClientCountGetLeftOverMissing = _RtmpClientCountGetLeftOverMissing_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 18),
    _RtmpClientCountGetLeftOverMissing_Type()
)
rtmpClientCountGetLeftOverMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetLeftOverMissing.setStatus("current")
_RtmpClientCountGetLiveRepeaterCapabilities_Type = Integer32
_RtmpClientCountGetLiveRepeaterCapabilities_Object = MibTableColumn
rtmpClientCountGetLiveRepeaterCapabilities = _RtmpClientCountGetLiveRepeaterCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 19),
    _RtmpClientCountGetLiveRepeaterCapabilities_Type()
)
rtmpClientCountGetLiveRepeaterCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetLiveRepeaterCapabilities.setStatus("current")
_RtmpClientCountGetLiveStreamPacketizerList_Type = DisplayString
_RtmpClientCountGetLiveStreamPacketizerList_Object = MibTableColumn
rtmpClientCountGetLiveStreamPacketizerList = _RtmpClientCountGetLiveStreamPacketizerList_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 20),
    _RtmpClientCountGetLiveStreamPacketizerList_Type()
)
rtmpClientCountGetLiveStreamPacketizerList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetLiveStreamPacketizerList.setStatus("current")
_RtmpClientCountGetLiveStreamTranscoderList_Type = DisplayString
_RtmpClientCountGetLiveStreamTranscoderList_Object = MibTableColumn
rtmpClientCountGetLiveStreamTranscoderList = _RtmpClientCountGetLiveStreamTranscoderList_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 21),
    _RtmpClientCountGetLiveStreamTranscoderList_Type()
)
rtmpClientCountGetLiveStreamTranscoderList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetLiveStreamTranscoderList.setStatus("current")
_RtmpClientCountGetMaximumPendingReadBytes_Type = Integer32
_RtmpClientCountGetMaximumPendingReadBytes_Object = MibTableColumn
rtmpClientCountGetMaximumPendingReadBytes = _RtmpClientCountGetMaximumPendingReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 22),
    _RtmpClientCountGetMaximumPendingReadBytes_Type()
)
rtmpClientCountGetMaximumPendingReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetMaximumPendingReadBytes.setStatus("current")
_RtmpClientCountGetMaximumPendingWriteBytes_Type = Integer32
_RtmpClientCountGetMaximumPendingWriteBytes_Object = MibTableColumn
rtmpClientCountGetMaximumPendingWriteBytes = _RtmpClientCountGetMaximumPendingWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 23),
    _RtmpClientCountGetMaximumPendingWriteBytes_Type()
)
rtmpClientCountGetMaximumPendingWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetMaximumPendingWriteBytes.setStatus("current")
_RtmpClientCountGetMaximumSetBufferTime_Type = Integer32
_RtmpClientCountGetMaximumSetBufferTime_Object = MibTableColumn
rtmpClientCountGetMaximumSetBufferTime = _RtmpClientCountGetMaximumSetBufferTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 24),
    _RtmpClientCountGetMaximumSetBufferTime_Type()
)
rtmpClientCountGetMaximumSetBufferTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetMaximumSetBufferTime.setStatus("current")
_RtmpClientCountGetNextConfirmBytesReceived_Type = Counter64
_RtmpClientCountGetNextConfirmBytesReceived_Object = MibTableColumn
rtmpClientCountGetNextConfirmBytesReceived = _RtmpClientCountGetNextConfirmBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 25),
    _RtmpClientCountGetNextConfirmBytesReceived_Type()
)
rtmpClientCountGetNextConfirmBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetNextConfirmBytesReceived.setStatus("current")
_RtmpClientCountGetObjectEncoding_Type = Integer32
_RtmpClientCountGetObjectEncoding_Object = MibTableColumn
rtmpClientCountGetObjectEncoding = _RtmpClientCountGetObjectEncoding_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 26),
    _RtmpClientCountGetObjectEncoding_Type()
)
rtmpClientCountGetObjectEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetObjectEncoding.setStatus("current")
_RtmpClientCountGetPageUrl_Type = DisplayString
_RtmpClientCountGetPageUrl_Object = MibTableColumn
rtmpClientCountGetPageUrl = _RtmpClientCountGetPageUrl_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 27),
    _RtmpClientCountGetPageUrl_Type()
)
rtmpClientCountGetPageUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetPageUrl.setStatus("current")
_RtmpClientCountGetPingRoundTripTime_Type = Counter64
_RtmpClientCountGetPingRoundTripTime_Object = MibTableColumn
rtmpClientCountGetPingRoundTripTime = _RtmpClientCountGetPingRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 28),
    _RtmpClientCountGetPingRoundTripTime_Type()
)
rtmpClientCountGetPingRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetPingRoundTripTime.setStatus("current")
_RtmpClientCountGetPingTimeout_Type = Integer32
_RtmpClientCountGetPingTimeout_Object = MibTableColumn
rtmpClientCountGetPingTimeout = _RtmpClientCountGetPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 29),
    _RtmpClientCountGetPingTimeout_Type()
)
rtmpClientCountGetPingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetPingTimeout.setStatus("current")
_RtmpClientCountGetPlayResponse_Type = Integer32
_RtmpClientCountGetPlayResponse_Object = MibTableColumn
rtmpClientCountGetPlayResponse = _RtmpClientCountGetPlayResponse_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 30),
    _RtmpClientCountGetPlayResponse_Type()
)
rtmpClientCountGetPlayResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetPlayResponse.setStatus("current")
_RtmpClientCountGetPlayStreamCount_Type = Integer32
_RtmpClientCountGetPlayStreamCount_Object = MibTableColumn
rtmpClientCountGetPlayStreamCount = _RtmpClientCountGetPlayStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 31),
    _RtmpClientCountGetPlayStreamCount_Type()
)
rtmpClientCountGetPlayStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetPlayStreamCount.setStatus("current")
_RtmpClientCountGetProtocol_Type = Integer32
_RtmpClientCountGetProtocol_Object = MibTableColumn
rtmpClientCountGetProtocol = _RtmpClientCountGetProtocol_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 32),
    _RtmpClientCountGetProtocol_Type()
)
rtmpClientCountGetProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetProtocol.setStatus("current")
_RtmpClientCountGetPublishStreamCount_Type = Integer32
_RtmpClientCountGetPublishStreamCount_Object = MibTableColumn
rtmpClientCountGetPublishStreamCount = _RtmpClientCountGetPublishStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 33),
    _RtmpClientCountGetPublishStreamCount_Type()
)
rtmpClientCountGetPublishStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetPublishStreamCount.setStatus("current")
_RtmpClientCountGetQueryStr_Type = DisplayString
_RtmpClientCountGetQueryStr_Object = MibTableColumn
rtmpClientCountGetQueryStr = _RtmpClientCountGetQueryStr_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 34),
    _RtmpClientCountGetQueryStr_Type()
)
rtmpClientCountGetQueryStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetQueryStr.setStatus("current")
_RtmpClientCountGetReceiveChunkSize_Type = Integer32
_RtmpClientCountGetReceiveChunkSize_Object = MibTableColumn
rtmpClientCountGetReceiveChunkSize = _RtmpClientCountGetReceiveChunkSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 35),
    _RtmpClientCountGetReceiveChunkSize_Type()
)
rtmpClientCountGetReceiveChunkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetReceiveChunkSize.setStatus("current")
_RtmpClientCountGetReferrer_Type = DisplayString
_RtmpClientCountGetReferrer_Object = MibTableColumn
rtmpClientCountGetReferrer = _RtmpClientCountGetReferrer_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 36),
    _RtmpClientCountGetReferrer_Type()
)
rtmpClientCountGetReferrer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetReferrer.setStatus("current")
_RtmpClientCountGetRepeaterOriginUrl_Type = DisplayString
_RtmpClientCountGetRepeaterOriginUrl_Object = MibTableColumn
rtmpClientCountGetRepeaterOriginUrl = _RtmpClientCountGetRepeaterOriginUrl_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 37),
    _RtmpClientCountGetRepeaterOriginUrl_Type()
)
rtmpClientCountGetRepeaterOriginUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetRepeaterOriginUrl.setStatus("current")
_RtmpClientCountGetRequestDataSize_Type = Integer32
_RtmpClientCountGetRequestDataSize_Object = MibTableColumn
rtmpClientCountGetRequestDataSize = _RtmpClientCountGetRequestDataSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 38),
    _RtmpClientCountGetRequestDataSize_Type()
)
rtmpClientCountGetRequestDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetRequestDataSize.setStatus("current")
_RtmpClientCountGetRequestRTMPTSequence_Type = Counter64
_RtmpClientCountGetRequestRTMPTSequence_Object = MibTableColumn
rtmpClientCountGetRequestRTMPTSequence = _RtmpClientCountGetRequestRTMPTSequence_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 39),
    _RtmpClientCountGetRequestRTMPTSequence_Type()
)
rtmpClientCountGetRequestRTMPTSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetRequestRTMPTSequence.setStatus("current")
_RtmpClientCountGetResponseIndex_Type = Integer32
_RtmpClientCountGetResponseIndex_Object = MibTableColumn
rtmpClientCountGetResponseIndex = _RtmpClientCountGetResponseIndex_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 40),
    _RtmpClientCountGetResponseIndex_Type()
)
rtmpClientCountGetResponseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetResponseIndex.setStatus("current")
_RtmpClientCountGetSendChunkSize_Type = Integer32
_RtmpClientCountGetSendChunkSize_Object = MibTableColumn
rtmpClientCountGetSendChunkSize = _RtmpClientCountGetSendChunkSize_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 41),
    _RtmpClientCountGetSendChunkSize_Type()
)
rtmpClientCountGetSendChunkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetSendChunkSize.setStatus("current")
_RtmpClientCountGetSharedObjectReadAccess_Type = DisplayString
_RtmpClientCountGetSharedObjectReadAccess_Object = MibTableColumn
rtmpClientCountGetSharedObjectReadAccess = _RtmpClientCountGetSharedObjectReadAccess_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 42),
    _RtmpClientCountGetSharedObjectReadAccess_Type()
)
rtmpClientCountGetSharedObjectReadAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetSharedObjectReadAccess.setStatus("current")
_RtmpClientCountGetSharedObjectWriteAccess_Type = DisplayString
_RtmpClientCountGetSharedObjectWriteAccess_Object = MibTableColumn
rtmpClientCountGetSharedObjectWriteAccess = _RtmpClientCountGetSharedObjectWriteAccess_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 43),
    _RtmpClientCountGetSharedObjectWriteAccess_Type()
)
rtmpClientCountGetSharedObjectWriteAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetSharedObjectWriteAccess.setStatus("current")
_RtmpClientCountGetStreamAudioSampleAccess_Type = DisplayString
_RtmpClientCountGetStreamAudioSampleAccess_Object = MibTableColumn
rtmpClientCountGetStreamAudioSampleAccess = _RtmpClientCountGetStreamAudioSampleAccess_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 44),
    _RtmpClientCountGetStreamAudioSampleAccess_Type()
)
rtmpClientCountGetStreamAudioSampleAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetStreamAudioSampleAccess.setStatus("current")
_RtmpClientCountGetStreamReadAccess_Type = DisplayString
_RtmpClientCountGetStreamReadAccess_Object = MibTableColumn
rtmpClientCountGetStreamReadAccess = _RtmpClientCountGetStreamReadAccess_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 45),
    _RtmpClientCountGetStreamReadAccess_Type()
)
rtmpClientCountGetStreamReadAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetStreamReadAccess.setStatus("current")
_RtmpClientCountGetStreamType_Type = DisplayString
_RtmpClientCountGetStreamType_Object = MibTableColumn
rtmpClientCountGetStreamType = _RtmpClientCountGetStreamType_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 46),
    _RtmpClientCountGetStreamType_Type()
)
rtmpClientCountGetStreamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetStreamType.setStatus("current")
_RtmpClientCountGetStreamVideoSampleAccess_Type = DisplayString
_RtmpClientCountGetStreamVideoSampleAccess_Object = MibTableColumn
rtmpClientCountGetStreamVideoSampleAccess = _RtmpClientCountGetStreamVideoSampleAccess_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 47),
    _RtmpClientCountGetStreamVideoSampleAccess_Type()
)
rtmpClientCountGetStreamVideoSampleAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetStreamVideoSampleAccess.setStatus("current")
_RtmpClientCountGetStreamWriteAccess_Type = DisplayString
_RtmpClientCountGetStreamWriteAccess_Object = MibTableColumn
rtmpClientCountGetStreamWriteAccess = _RtmpClientCountGetStreamWriteAccess_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 48),
    _RtmpClientCountGetStreamWriteAccess_Type()
)
rtmpClientCountGetStreamWriteAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetStreamWriteAccess.setStatus("current")
_RtmpClientCountGetTimeRunning_Type = DisplayString
_RtmpClientCountGetTimeRunning_Object = MibTableColumn
rtmpClientCountGetTimeRunning = _RtmpClientCountGetTimeRunning_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 49),
    _RtmpClientCountGetTimeRunning_Type()
)
rtmpClientCountGetTimeRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetTimeRunning.setStatus("current")
_RtmpClientCountGetTimebase_Type = Counter64
_RtmpClientCountGetTimebase_Object = MibTableColumn
rtmpClientCountGetTimebase = _RtmpClientCountGetTimebase_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 50),
    _RtmpClientCountGetTimebase_Type()
)
rtmpClientCountGetTimebase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetTimebase.setStatus("current")
_RtmpClientCountGetTotalInBytes_Type = Counter64
_RtmpClientCountGetTotalInBytes_Object = MibTableColumn
rtmpClientCountGetTotalInBytes = _RtmpClientCountGetTotalInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 51),
    _RtmpClientCountGetTotalInBytes_Type()
)
rtmpClientCountGetTotalInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetTotalInBytes.setStatus("current")
_RtmpClientCountGetTouch_Type = Counter64
_RtmpClientCountGetTouch_Object = MibTableColumn
rtmpClientCountGetTouch = _RtmpClientCountGetTouch_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 52),
    _RtmpClientCountGetTouch_Type()
)
rtmpClientCountGetTouch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetTouch.setStatus("current")
_RtmpClientCountGetUri_Type = DisplayString
_RtmpClientCountGetUri_Object = MibTableColumn
rtmpClientCountGetUri = _RtmpClientCountGetUri_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 53),
    _RtmpClientCountGetUri_Type()
)
rtmpClientCountGetUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetUri.setStatus("current")
_RtmpClientCountGetValidationFrequency_Type = Integer32
_RtmpClientCountGetValidationFrequency_Object = MibTableColumn
rtmpClientCountGetValidationFrequency = _RtmpClientCountGetValidationFrequency_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 1, 1, 54),
    _RtmpClientCountGetValidationFrequency_Type()
)
rtmpClientCountGetValidationFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientCountGetValidationFrequency.setStatus("current")
_RtmpClientPerformTable_Object = MibTable
rtmpClientPerformTable = _RtmpClientPerformTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 3)
)
if mibBuilder.loadTexts:
    rtmpClientPerformTable.setStatus("current")
_RtmpClientPerformEntry_Object = MibTableRow
rtmpClientPerformEntry = _RtmpClientPerformEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 3, 1)
)
rtmpClientPerformEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "clientIndex"),
)
if mibBuilder.loadTexts:
    rtmpClientPerformEntry.setStatus("current")
_RtmpClientPerformCreationTime_Type = Counter64
_RtmpClientPerformCreationTime_Object = MibTableColumn
rtmpClientPerformCreationTime = _RtmpClientPerformCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 3, 1, 1),
    _RtmpClientPerformCreationTime_Type()
)
rtmpClientPerformCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientPerformCreationTime.setStatus("current")
_RtmpClientPerformGetFileInBytes_Type = Counter64
_RtmpClientPerformGetFileInBytes_Object = MibTableColumn
rtmpClientPerformGetFileInBytes = _RtmpClientPerformGetFileInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 3, 1, 2),
    _RtmpClientPerformGetFileInBytes_Type()
)
rtmpClientPerformGetFileInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientPerformGetFileInBytes.setStatus("current")
_RtmpClientPerformGetFileOutBytes_Type = Counter64
_RtmpClientPerformGetFileOutBytes_Object = MibTableColumn
rtmpClientPerformGetFileOutBytes = _RtmpClientPerformGetFileOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 3, 1, 3),
    _RtmpClientPerformGetFileOutBytes_Type()
)
rtmpClientPerformGetFileOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientPerformGetFileOutBytes.setStatus("current")
_RtmpClientPerformGetMessagesInBytes_Type = Counter64
_RtmpClientPerformGetMessagesInBytes_Object = MibTableColumn
rtmpClientPerformGetMessagesInBytes = _RtmpClientPerformGetMessagesInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 3, 1, 4),
    _RtmpClientPerformGetMessagesInBytes_Type()
)
rtmpClientPerformGetMessagesInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientPerformGetMessagesInBytes.setStatus("current")
_RtmpClientPerformGetMessagesInCount_Type = Counter64
_RtmpClientPerformGetMessagesInCount_Object = MibTableColumn
rtmpClientPerformGetMessagesInCount = _RtmpClientPerformGetMessagesInCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 3, 1, 5),
    _RtmpClientPerformGetMessagesInCount_Type()
)
rtmpClientPerformGetMessagesInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientPerformGetMessagesInCount.setStatus("current")
_RtmpClientPerformGetMessagesInCountRate_Type = Counter64
_RtmpClientPerformGetMessagesInCountRate_Object = MibTableColumn
rtmpClientPerformGetMessagesInCountRate = _RtmpClientPerformGetMessagesInCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 3, 1, 6),
    _RtmpClientPerformGetMessagesInCountRate_Type()
)
rtmpClientPerformGetMessagesInCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientPerformGetMessagesInCountRate.setStatus("current")
_RtmpClientPerformGetMessagesLossBytes_Type = Counter64
_RtmpClientPerformGetMessagesLossBytes_Object = MibTableColumn
rtmpClientPerformGetMessagesLossBytes = _RtmpClientPerformGetMessagesLossBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 3, 1, 7),
    _RtmpClientPerformGetMessagesLossBytes_Type()
)
rtmpClientPerformGetMessagesLossBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientPerformGetMessagesLossBytes.setStatus("current")
_RtmpClientPerformGetMessagesLossCount_Type = Counter64
_RtmpClientPerformGetMessagesLossCount_Object = MibTableColumn
rtmpClientPerformGetMessagesLossCount = _RtmpClientPerformGetMessagesLossCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 3, 1, 8),
    _RtmpClientPerformGetMessagesLossCount_Type()
)
rtmpClientPerformGetMessagesLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientPerformGetMessagesLossCount.setStatus("current")
_RtmpClientPerformGetMessagesLossCountRate_Type = Counter64
_RtmpClientPerformGetMessagesLossCountRate_Object = MibTableColumn
rtmpClientPerformGetMessagesLossCountRate = _RtmpClientPerformGetMessagesLossCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 3, 1, 9),
    _RtmpClientPerformGetMessagesLossCountRate_Type()
)
rtmpClientPerformGetMessagesLossCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientPerformGetMessagesLossCountRate.setStatus("current")
_RtmpClientPerformGetMessagesOutBytes_Type = Counter64
_RtmpClientPerformGetMessagesOutBytes_Object = MibTableColumn
rtmpClientPerformGetMessagesOutBytes = _RtmpClientPerformGetMessagesOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 3, 1, 10),
    _RtmpClientPerformGetMessagesOutBytes_Type()
)
rtmpClientPerformGetMessagesOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientPerformGetMessagesOutBytes.setStatus("current")
_RtmpClientPerformGetMessagesOutCount_Type = Counter64
_RtmpClientPerformGetMessagesOutCount_Object = MibTableColumn
rtmpClientPerformGetMessagesOutCount = _RtmpClientPerformGetMessagesOutCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 3, 1, 11),
    _RtmpClientPerformGetMessagesOutCount_Type()
)
rtmpClientPerformGetMessagesOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientPerformGetMessagesOutCount.setStatus("current")
_RtmpClientPerformGetMessagesOutCountRate_Type = Counter64
_RtmpClientPerformGetMessagesOutCountRate_Object = MibTableColumn
rtmpClientPerformGetMessagesOutCountRate = _RtmpClientPerformGetMessagesOutCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 60, 1, 3, 1, 12),
    _RtmpClientPerformGetMessagesOutCountRate_Type()
)
rtmpClientPerformGetMessagesOutCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmpClientPerformGetMessagesOutCountRate.setStatus("current")
_Httpclients_ObjectIdentity = ObjectIdentity
httpclients = _Httpclients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70)
)
_HttpclientInfo_ObjectIdentity = ObjectIdentity
httpclientInfo = _HttpclientInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1)
)
_HttpClientCountTable_Object = MibTable
httpClientCountTable = _HttpClientCountTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1)
)
if mibBuilder.loadTexts:
    httpClientCountTable.setStatus("current")
_HttpClientCountEntry_Object = MibTableRow
httpClientCountEntry = _HttpClientCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1)
)
httpClientCountEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "clientIndex"),
)
if mibBuilder.loadTexts:
    httpClientCountEntry.setStatus("current")
_HttpClientCountCreationTime_Type = Counter64
_HttpClientCountCreationTime_Object = MibTableColumn
httpClientCountCreationTime = _HttpClientCountCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 1),
    _HttpClientCountCreationTime_Type()
)
httpClientCountCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountCreationTime.setStatus("current")
_HttpClientCountGetCookieStr_Type = DisplayString
_HttpClientCountGetCookieStr_Object = MibTableColumn
httpClientCountGetCookieStr = _HttpClientCountGetCookieStr_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 2),
    _HttpClientCountGetCookieStr_Type()
)
httpClientCountGetCookieStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetCookieStr.setStatus("current")
_HttpClientCountGetHTTPDate_Type = DisplayString
_HttpClientCountGetHTTPDate_Object = MibTableColumn
httpClientCountGetHTTPDate = _HttpClientCountGetHTTPDate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 3),
    _HttpClientCountGetHTTPDate_Type()
)
httpClientCountGetHTTPDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetHTTPDate.setStatus("current")
_HttpClientCountGetIpAddress_Type = DisplayString
_HttpClientCountGetIpAddress_Object = MibTableColumn
httpClientCountGetIpAddress = _HttpClientCountGetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 4),
    _HttpClientCountGetIpAddress_Type()
)
httpClientCountGetIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetIpAddress.setStatus("current")
_HttpClientCountGetIsFirstChunk_Type = TruthValue
_HttpClientCountGetIsFirstChunk_Object = MibTableColumn
httpClientCountGetIsFirstChunk = _HttpClientCountGetIsFirstChunk_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 5),
    _HttpClientCountGetIsFirstChunk_Type()
)
httpClientCountGetIsFirstChunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetIsFirstChunk.setStatus("current")
_HttpClientCountGetLastRequest_Type = Counter64
_HttpClientCountGetLastRequest_Object = MibTableColumn
httpClientCountGetLastRequest = _HttpClientCountGetLastRequest_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 6),
    _HttpClientCountGetLastRequest_Type()
)
httpClientCountGetLastRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetLastRequest.setStatus("current")
_HttpClientCountGetLiveStreamingPacketizer_Type = DisplayString
_HttpClientCountGetLiveStreamingPacketizer_Object = MibTableColumn
httpClientCountGetLiveStreamingPacketizer = _HttpClientCountGetLiveStreamingPacketizer_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 7),
    _HttpClientCountGetLiveStreamingPacketizer_Type()
)
httpClientCountGetLiveStreamingPacketizer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetLiveStreamingPacketizer.setStatus("current")
_HttpClientCountGetPlayDuration_Type = Counter64
_HttpClientCountGetPlayDuration_Object = MibTableColumn
httpClientCountGetPlayDuration = _HttpClientCountGetPlayDuration_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 8),
    _HttpClientCountGetPlayDuration_Type()
)
httpClientCountGetPlayDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetPlayDuration.setStatus("current")
_HttpClientCountGetPlaySeek_Type = Counter64
_HttpClientCountGetPlaySeek_Object = MibTableColumn
httpClientCountGetPlaySeek = _HttpClientCountGetPlaySeek_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 9),
    _HttpClientCountGetPlaySeek_Type()
)
httpClientCountGetPlaySeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetPlaySeek.setStatus("current")
_HttpClientCountGetPlayStart_Type = Counter64
_HttpClientCountGetPlayStart_Object = MibTableColumn
httpClientCountGetPlayStart = _HttpClientCountGetPlayStart_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 10),
    _HttpClientCountGetPlayStart_Type()
)
httpClientCountGetPlayStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetPlayStart.setStatus("current")
_HttpClientCountGetQueryStr_Type = DisplayString
_HttpClientCountGetQueryStr_Object = MibTableColumn
httpClientCountGetQueryStr = _HttpClientCountGetQueryStr_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 11),
    _HttpClientCountGetQueryStr_Type()
)
httpClientCountGetQueryStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetQueryStr.setStatus("current")
_HttpClientCountGetRedirectSessionCode_Type = Integer32
_HttpClientCountGetRedirectSessionCode_Object = MibTableColumn
httpClientCountGetRedirectSessionCode = _HttpClientCountGetRedirectSessionCode_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 12),
    _HttpClientCountGetRedirectSessionCode_Type()
)
httpClientCountGetRedirectSessionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetRedirectSessionCode.setStatus("current")
_HttpClientCountGetRedirectSessionContentType_Type = DisplayString
_HttpClientCountGetRedirectSessionContentType_Object = MibTableColumn
httpClientCountGetRedirectSessionContentType = _HttpClientCountGetRedirectSessionContentType_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 13),
    _HttpClientCountGetRedirectSessionContentType_Type()
)
httpClientCountGetRedirectSessionContentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetRedirectSessionContentType.setStatus("current")
_HttpClientCountGetRedirectSessionURL_Type = DisplayString
_HttpClientCountGetRedirectSessionURL_Object = MibTableColumn
httpClientCountGetRedirectSessionURL = _HttpClientCountGetRedirectSessionURL_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 14),
    _HttpClientCountGetRedirectSessionURL_Type()
)
httpClientCountGetRedirectSessionURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetRedirectSessionURL.setStatus("current")
_HttpClientCountGetReferrer_Type = DisplayString
_HttpClientCountGetReferrer_Object = MibTableColumn
httpClientCountGetReferrer = _HttpClientCountGetReferrer_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 15),
    _HttpClientCountGetReferrer_Type()
)
httpClientCountGetReferrer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetReferrer.setStatus("current")
_HttpClientCountGetServerIp_Type = DisplayString
_HttpClientCountGetServerIp_Object = MibTableColumn
httpClientCountGetServerIp = _HttpClientCountGetServerIp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 16),
    _HttpClientCountGetServerIp_Type()
)
httpClientCountGetServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetServerIp.setStatus("current")
_HttpClientCountGetServerPort_Type = Integer32
_HttpClientCountGetServerPort_Object = MibTableColumn
httpClientCountGetServerPort = _HttpClientCountGetServerPort_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 17),
    _HttpClientCountGetServerPort_Type()
)
httpClientCountGetServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetServerPort.setStatus("current")
_HttpClientCountGetSessionId_Type = DisplayString
_HttpClientCountGetSessionId_Object = MibTableColumn
httpClientCountGetSessionId = _HttpClientCountGetSessionId_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 18),
    _HttpClientCountGetSessionId_Type()
)
httpClientCountGetSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetSessionId.setStatus("current")
_HttpClientCountGetSessionProtocol_Type = Integer32
_HttpClientCountGetSessionProtocol_Object = MibTableColumn
httpClientCountGetSessionProtocol = _HttpClientCountGetSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 19),
    _HttpClientCountGetSessionProtocol_Type()
)
httpClientCountGetSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetSessionProtocol.setStatus("current")
_HttpClientCountGetSessionTimeout_Type = Integer32
_HttpClientCountGetSessionTimeout_Object = MibTableColumn
httpClientCountGetSessionTimeout = _HttpClientCountGetSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 20),
    _HttpClientCountGetSessionTimeout_Type()
)
httpClientCountGetSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetSessionTimeout.setStatus("current")
_HttpClientCountGetSessionType_Type = Integer32
_HttpClientCountGetSessionType_Object = MibTableColumn
httpClientCountGetSessionType = _HttpClientCountGetSessionType_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 21),
    _HttpClientCountGetSessionType_Type()
)
httpClientCountGetSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetSessionType.setStatus("current")
_HttpClientCountGetStreamExt_Type = DisplayString
_HttpClientCountGetStreamExt_Object = MibTableColumn
httpClientCountGetStreamExt = _HttpClientCountGetStreamExt_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 22),
    _HttpClientCountGetStreamExt_Type()
)
httpClientCountGetStreamExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetStreamExt.setStatus("current")
_HttpClientCountGetStreamName_Type = DisplayString
_HttpClientCountGetStreamName_Object = MibTableColumn
httpClientCountGetStreamName = _HttpClientCountGetStreamName_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 23),
    _HttpClientCountGetStreamName_Type()
)
httpClientCountGetStreamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetStreamName.setStatus("current")
_HttpClientCountGetStreamPosition_Type = Counter64
_HttpClientCountGetStreamPosition_Object = MibTableColumn
httpClientCountGetStreamPosition = _HttpClientCountGetStreamPosition_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 24),
    _HttpClientCountGetStreamPosition_Type()
)
httpClientCountGetStreamPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetStreamPosition.setStatus("current")
_HttpClientCountGetTimeRunning_Type = DisplayString
_HttpClientCountGetTimeRunning_Object = MibTableColumn
httpClientCountGetTimeRunning = _HttpClientCountGetTimeRunning_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 25),
    _HttpClientCountGetTimeRunning_Type()
)
httpClientCountGetTimeRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetTimeRunning.setStatus("current")
_HttpClientCountGetUri_Type = DisplayString
_HttpClientCountGetUri_Object = MibTableColumn
httpClientCountGetUri = _HttpClientCountGetUri_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 26),
    _HttpClientCountGetUri_Type()
)
httpClientCountGetUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetUri.setStatus("current")
_HttpClientCountGetUserAgent_Type = DisplayString
_HttpClientCountGetUserAgent_Object = MibTableColumn
httpClientCountGetUserAgent = _HttpClientCountGetUserAgent_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 27),
    _HttpClientCountGetUserAgent_Type()
)
httpClientCountGetUserAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetUserAgent.setStatus("current")
_HttpClientCountGetUserQueryStr_Type = DisplayString
_HttpClientCountGetUserQueryStr_Object = MibTableColumn
httpClientCountGetUserQueryStr = _HttpClientCountGetUserQueryStr_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 28),
    _HttpClientCountGetUserQueryStr_Type()
)
httpClientCountGetUserQueryStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetUserQueryStr.setStatus("current")
_HttpClientCountGetVODTranscodeNGRP_Type = DisplayString
_HttpClientCountGetVODTranscodeNGRP_Object = MibTableColumn
httpClientCountGetVODTranscodeNGRP = _HttpClientCountGetVODTranscodeNGRP_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 1, 1, 29),
    _HttpClientCountGetVODTranscodeNGRP_Type()
)
httpClientCountGetVODTranscodeNGRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientCountGetVODTranscodeNGRP.setStatus("current")
_HttpClientPerformTable_Object = MibTable
httpClientPerformTable = _HttpClientPerformTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 3)
)
if mibBuilder.loadTexts:
    httpClientPerformTable.setStatus("current")
_HttpClientPerformEntry_Object = MibTableRow
httpClientPerformEntry = _HttpClientPerformEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 3, 1)
)
httpClientPerformEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "clientIndex"),
)
if mibBuilder.loadTexts:
    httpClientPerformEntry.setStatus("current")
_HttpClientPerformCreationTime_Type = Counter64
_HttpClientPerformCreationTime_Object = MibTableColumn
httpClientPerformCreationTime = _HttpClientPerformCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 3, 1, 1),
    _HttpClientPerformCreationTime_Type()
)
httpClientPerformCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientPerformCreationTime.setStatus("current")
_HttpClientPerformGetFileInBytes_Type = Counter64
_HttpClientPerformGetFileInBytes_Object = MibTableColumn
httpClientPerformGetFileInBytes = _HttpClientPerformGetFileInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 3, 1, 2),
    _HttpClientPerformGetFileInBytes_Type()
)
httpClientPerformGetFileInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientPerformGetFileInBytes.setStatus("current")
_HttpClientPerformGetFileOutBytes_Type = Counter64
_HttpClientPerformGetFileOutBytes_Object = MibTableColumn
httpClientPerformGetFileOutBytes = _HttpClientPerformGetFileOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 3, 1, 3),
    _HttpClientPerformGetFileOutBytes_Type()
)
httpClientPerformGetFileOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientPerformGetFileOutBytes.setStatus("current")
_HttpClientPerformGetMessagesInBytes_Type = Counter64
_HttpClientPerformGetMessagesInBytes_Object = MibTableColumn
httpClientPerformGetMessagesInBytes = _HttpClientPerformGetMessagesInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 3, 1, 4),
    _HttpClientPerformGetMessagesInBytes_Type()
)
httpClientPerformGetMessagesInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientPerformGetMessagesInBytes.setStatus("current")
_HttpClientPerformGetMessagesInCount_Type = Counter64
_HttpClientPerformGetMessagesInCount_Object = MibTableColumn
httpClientPerformGetMessagesInCount = _HttpClientPerformGetMessagesInCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 3, 1, 5),
    _HttpClientPerformGetMessagesInCount_Type()
)
httpClientPerformGetMessagesInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientPerformGetMessagesInCount.setStatus("current")
_HttpClientPerformGetMessagesInCountRate_Type = Counter64
_HttpClientPerformGetMessagesInCountRate_Object = MibTableColumn
httpClientPerformGetMessagesInCountRate = _HttpClientPerformGetMessagesInCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 3, 1, 6),
    _HttpClientPerformGetMessagesInCountRate_Type()
)
httpClientPerformGetMessagesInCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientPerformGetMessagesInCountRate.setStatus("current")
_HttpClientPerformGetMessagesLossBytes_Type = Counter64
_HttpClientPerformGetMessagesLossBytes_Object = MibTableColumn
httpClientPerformGetMessagesLossBytes = _HttpClientPerformGetMessagesLossBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 3, 1, 7),
    _HttpClientPerformGetMessagesLossBytes_Type()
)
httpClientPerformGetMessagesLossBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientPerformGetMessagesLossBytes.setStatus("current")
_HttpClientPerformGetMessagesLossCount_Type = Counter64
_HttpClientPerformGetMessagesLossCount_Object = MibTableColumn
httpClientPerformGetMessagesLossCount = _HttpClientPerformGetMessagesLossCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 3, 1, 8),
    _HttpClientPerformGetMessagesLossCount_Type()
)
httpClientPerformGetMessagesLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientPerformGetMessagesLossCount.setStatus("current")
_HttpClientPerformGetMessagesLossCountRate_Type = Counter64
_HttpClientPerformGetMessagesLossCountRate_Object = MibTableColumn
httpClientPerformGetMessagesLossCountRate = _HttpClientPerformGetMessagesLossCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 3, 1, 9),
    _HttpClientPerformGetMessagesLossCountRate_Type()
)
httpClientPerformGetMessagesLossCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientPerformGetMessagesLossCountRate.setStatus("current")
_HttpClientPerformGetMessagesOutBytes_Type = Counter64
_HttpClientPerformGetMessagesOutBytes_Object = MibTableColumn
httpClientPerformGetMessagesOutBytes = _HttpClientPerformGetMessagesOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 3, 1, 10),
    _HttpClientPerformGetMessagesOutBytes_Type()
)
httpClientPerformGetMessagesOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientPerformGetMessagesOutBytes.setStatus("current")
_HttpClientPerformGetMessagesOutCount_Type = Counter64
_HttpClientPerformGetMessagesOutCount_Object = MibTableColumn
httpClientPerformGetMessagesOutCount = _HttpClientPerformGetMessagesOutCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 3, 1, 11),
    _HttpClientPerformGetMessagesOutCount_Type()
)
httpClientPerformGetMessagesOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientPerformGetMessagesOutCount.setStatus("current")
_HttpClientPerformGetMessagesOutCountRate_Type = Counter64
_HttpClientPerformGetMessagesOutCountRate_Object = MibTableColumn
httpClientPerformGetMessagesOutCountRate = _HttpClientPerformGetMessagesOutCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 70, 1, 3, 1, 12),
    _HttpClientPerformGetMessagesOutCountRate_Type()
)
httpClientPerformGetMessagesOutCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpClientPerformGetMessagesOutCountRate.setStatus("current")
_Rtspclients_ObjectIdentity = ObjectIdentity
rtspclients = _Rtspclients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80)
)
_RtspclientInfo_ObjectIdentity = ObjectIdentity
rtspclientInfo = _RtspclientInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1)
)
_RtspClientCountTable_Object = MibTable
rtspClientCountTable = _RtspClientCountTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1)
)
if mibBuilder.loadTexts:
    rtspClientCountTable.setStatus("current")
_RtspClientCountEntry_Object = MibTableRow
rtspClientCountEntry = _RtspClientCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1)
)
rtspClientCountEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "clientIndex"),
)
if mibBuilder.loadTexts:
    rtspClientCountEntry.setStatus("current")
_RtspClientCountCreationTime_Type = Counter64
_RtspClientCountCreationTime_Object = MibTableColumn
rtspClientCountCreationTime = _RtspClientCountCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 1),
    _RtspClientCountCreationTime_Type()
)
rtspClientCountCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountCreationTime.setStatus("current")
_RtspClientCountGetCookieStr_Type = DisplayString
_RtspClientCountGetCookieStr_Object = MibTableColumn
rtspClientCountGetCookieStr = _RtspClientCountGetCookieStr_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 2),
    _RtspClientCountGetCookieStr_Type()
)
rtspClientCountGetCookieStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetCookieStr.setStatus("current")
_RtspClientCountGetIdleFrequency_Type = Integer32
_RtspClientCountGetIdleFrequency_Object = MibTableColumn
rtspClientCountGetIdleFrequency = _RtspClientCountGetIdleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 3),
    _RtspClientCountGetIdleFrequency_Type()
)
rtspClientCountGetIdleFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetIdleFrequency.setStatus("current")
_RtspClientCountGetIp_Type = DisplayString
_RtspClientCountGetIp_Object = MibTableColumn
rtspClientCountGetIp = _RtspClientCountGetIp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 4),
    _RtspClientCountGetIp_Type()
)
rtspClientCountGetIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetIp.setStatus("current")
_RtspClientCountGetLastAuthenticateMethod_Type = Integer32
_RtspClientCountGetLastAuthenticateMethod_Object = MibTableColumn
rtspClientCountGetLastAuthenticateMethod = _RtspClientCountGetLastAuthenticateMethod_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 5),
    _RtspClientCountGetLastAuthenticateMethod_Type()
)
rtspClientCountGetLastAuthenticateMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetLastAuthenticateMethod.setStatus("current")
_RtspClientCountGetQueryStr_Type = DisplayString
_RtspClientCountGetQueryStr_Object = MibTableColumn
rtspClientCountGetQueryStr = _RtspClientCountGetQueryStr_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 6),
    _RtspClientCountGetQueryStr_Type()
)
rtspClientCountGetQueryStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetQueryStr.setStatus("current")
_RtspClientCountGetRTSPTunnelingSessionId_Type = DisplayString
_RtspClientCountGetRTSPTunnelingSessionId_Object = MibTableColumn
rtspClientCountGetRTSPTunnelingSessionId = _RtspClientCountGetRTSPTunnelingSessionId_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 7),
    _RtspClientCountGetRTSPTunnelingSessionId_Type()
)
rtspClientCountGetRTSPTunnelingSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetRTSPTunnelingSessionId.setStatus("current")
_RtspClientCountGetRedirectSessionCode_Type = Integer32
_RtspClientCountGetRedirectSessionCode_Object = MibTableColumn
rtspClientCountGetRedirectSessionCode = _RtspClientCountGetRedirectSessionCode_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 8),
    _RtspClientCountGetRedirectSessionCode_Type()
)
rtspClientCountGetRedirectSessionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetRedirectSessionCode.setStatus("current")
_RtspClientCountGetRedirectSessionMessage_Type = DisplayString
_RtspClientCountGetRedirectSessionMessage_Object = MibTableColumn
rtspClientCountGetRedirectSessionMessage = _RtspClientCountGetRedirectSessionMessage_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 9),
    _RtspClientCountGetRedirectSessionMessage_Type()
)
rtspClientCountGetRedirectSessionMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetRedirectSessionMessage.setStatus("current")
_RtspClientCountGetRedirectSessionURL_Type = DisplayString
_RtspClientCountGetRedirectSessionURL_Object = MibTableColumn
rtspClientCountGetRedirectSessionURL = _RtspClientCountGetRedirectSessionURL_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 10),
    _RtspClientCountGetRedirectSessionURL_Type()
)
rtspClientCountGetRedirectSessionURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetRedirectSessionURL.setStatus("current")
_RtspClientCountGetReferrer_Type = DisplayString
_RtspClientCountGetReferrer_Object = MibTableColumn
rtspClientCountGetReferrer = _RtspClientCountGetReferrer_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 11),
    _RtspClientCountGetReferrer_Type()
)
rtspClientCountGetReferrer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetReferrer.setStatus("current")
_RtspClientCountGetServerIp_Type = DisplayString
_RtspClientCountGetServerIp_Object = MibTableColumn
rtspClientCountGetServerIp = _RtspClientCountGetServerIp_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 12),
    _RtspClientCountGetServerIp_Type()
)
rtspClientCountGetServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetServerIp.setStatus("current")
_RtspClientCountGetServerPort_Type = Integer32
_RtspClientCountGetServerPort_Object = MibTableColumn
rtspClientCountGetServerPort = _RtspClientCountGetServerPort_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 13),
    _RtspClientCountGetServerPort_Type()
)
rtspClientCountGetServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetServerPort.setStatus("current")
_RtspClientCountGetSessionId_Type = DisplayString
_RtspClientCountGetSessionId_Object = MibTableColumn
rtspClientCountGetSessionId = _RtspClientCountGetSessionId_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 14),
    _RtspClientCountGetSessionId_Type()
)
rtspClientCountGetSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetSessionId.setStatus("current")
_RtspClientCountGetTimeRunning_Type = DisplayString
_RtspClientCountGetTimeRunning_Object = MibTableColumn
rtspClientCountGetTimeRunning = _RtspClientCountGetTimeRunning_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 15),
    _RtspClientCountGetTimeRunning_Type()
)
rtspClientCountGetTimeRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetTimeRunning.setStatus("current")
_RtspClientCountGetUri_Type = DisplayString
_RtspClientCountGetUri_Object = MibTableColumn
rtspClientCountGetUri = _RtspClientCountGetUri_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 16),
    _RtspClientCountGetUri_Type()
)
rtspClientCountGetUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetUri.setStatus("current")
_RtspClientCountGetUserAgent_Type = DisplayString
_RtspClientCountGetUserAgent_Object = MibTableColumn
rtspClientCountGetUserAgent = _RtspClientCountGetUserAgent_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 1, 1, 17),
    _RtspClientCountGetUserAgent_Type()
)
rtspClientCountGetUserAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientCountGetUserAgent.setStatus("current")
_RtspClientPerformTable_Object = MibTable
rtspClientPerformTable = _RtspClientPerformTable_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 3)
)
if mibBuilder.loadTexts:
    rtspClientPerformTable.setStatus("current")
_RtspClientPerformEntry_Object = MibTableRow
rtspClientPerformEntry = _RtspClientPerformEntry_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 3, 1)
)
rtspClientPerformEntry.setIndexNames(
    (0, "WOWZA-STREAMING-ENGINE-MIB", "serverIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "vhostIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceIndex"),
    (0, "WOWZA-STREAMING-ENGINE-MIB", "clientIndex"),
)
if mibBuilder.loadTexts:
    rtspClientPerformEntry.setStatus("current")
_RtspClientPerformCreationTime_Type = Counter64
_RtspClientPerformCreationTime_Object = MibTableColumn
rtspClientPerformCreationTime = _RtspClientPerformCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 3, 1, 1),
    _RtspClientPerformCreationTime_Type()
)
rtspClientPerformCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientPerformCreationTime.setStatus("current")
_RtspClientPerformGetFileInBytes_Type = Counter64
_RtspClientPerformGetFileInBytes_Object = MibTableColumn
rtspClientPerformGetFileInBytes = _RtspClientPerformGetFileInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 3, 1, 2),
    _RtspClientPerformGetFileInBytes_Type()
)
rtspClientPerformGetFileInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientPerformGetFileInBytes.setStatus("current")
_RtspClientPerformGetFileOutBytes_Type = Counter64
_RtspClientPerformGetFileOutBytes_Object = MibTableColumn
rtspClientPerformGetFileOutBytes = _RtspClientPerformGetFileOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 3, 1, 3),
    _RtspClientPerformGetFileOutBytes_Type()
)
rtspClientPerformGetFileOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientPerformGetFileOutBytes.setStatus("current")
_RtspClientPerformGetMessagesInBytes_Type = Counter64
_RtspClientPerformGetMessagesInBytes_Object = MibTableColumn
rtspClientPerformGetMessagesInBytes = _RtspClientPerformGetMessagesInBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 3, 1, 4),
    _RtspClientPerformGetMessagesInBytes_Type()
)
rtspClientPerformGetMessagesInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientPerformGetMessagesInBytes.setStatus("current")
_RtspClientPerformGetMessagesInCount_Type = Counter64
_RtspClientPerformGetMessagesInCount_Object = MibTableColumn
rtspClientPerformGetMessagesInCount = _RtspClientPerformGetMessagesInCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 3, 1, 5),
    _RtspClientPerformGetMessagesInCount_Type()
)
rtspClientPerformGetMessagesInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientPerformGetMessagesInCount.setStatus("current")
_RtspClientPerformGetMessagesInCountRate_Type = Counter64
_RtspClientPerformGetMessagesInCountRate_Object = MibTableColumn
rtspClientPerformGetMessagesInCountRate = _RtspClientPerformGetMessagesInCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 3, 1, 6),
    _RtspClientPerformGetMessagesInCountRate_Type()
)
rtspClientPerformGetMessagesInCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientPerformGetMessagesInCountRate.setStatus("current")
_RtspClientPerformGetMessagesLossBytes_Type = Counter64
_RtspClientPerformGetMessagesLossBytes_Object = MibTableColumn
rtspClientPerformGetMessagesLossBytes = _RtspClientPerformGetMessagesLossBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 3, 1, 7),
    _RtspClientPerformGetMessagesLossBytes_Type()
)
rtspClientPerformGetMessagesLossBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientPerformGetMessagesLossBytes.setStatus("current")
_RtspClientPerformGetMessagesLossCount_Type = Counter64
_RtspClientPerformGetMessagesLossCount_Object = MibTableColumn
rtspClientPerformGetMessagesLossCount = _RtspClientPerformGetMessagesLossCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 3, 1, 8),
    _RtspClientPerformGetMessagesLossCount_Type()
)
rtspClientPerformGetMessagesLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientPerformGetMessagesLossCount.setStatus("current")
_RtspClientPerformGetMessagesLossCountRate_Type = Counter64
_RtspClientPerformGetMessagesLossCountRate_Object = MibTableColumn
rtspClientPerformGetMessagesLossCountRate = _RtspClientPerformGetMessagesLossCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 3, 1, 9),
    _RtspClientPerformGetMessagesLossCountRate_Type()
)
rtspClientPerformGetMessagesLossCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientPerformGetMessagesLossCountRate.setStatus("current")
_RtspClientPerformGetMessagesOutBytes_Type = Counter64
_RtspClientPerformGetMessagesOutBytes_Object = MibTableColumn
rtspClientPerformGetMessagesOutBytes = _RtspClientPerformGetMessagesOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 3, 1, 10),
    _RtspClientPerformGetMessagesOutBytes_Type()
)
rtspClientPerformGetMessagesOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientPerformGetMessagesOutBytes.setStatus("current")
_RtspClientPerformGetMessagesOutCount_Type = Counter64
_RtspClientPerformGetMessagesOutCount_Object = MibTableColumn
rtspClientPerformGetMessagesOutCount = _RtspClientPerformGetMessagesOutCount_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 3, 1, 11),
    _RtspClientPerformGetMessagesOutCount_Type()
)
rtspClientPerformGetMessagesOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientPerformGetMessagesOutCount.setStatus("current")
_RtspClientPerformGetMessagesOutCountRate_Type = Counter64
_RtspClientPerformGetMessagesOutCountRate_Object = MibTableColumn
rtspClientPerformGetMessagesOutCountRate = _RtspClientPerformGetMessagesOutCountRate_Object(
    (1, 3, 6, 1, 4, 1, 46706, 100, 80, 1, 3, 1, 12),
    _RtspClientPerformGetMessagesOutCountRate_Type()
)
rtspClientPerformGetMessagesOutCountRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspClientPerformGetMessagesOutCountRate.setStatus("current")

# Managed Objects groups

serverGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 10, 1)
)
serverGroupEntryConformanceTable.setObjects(
    ("WOWZA-STREAMING-ENGINE-MIB", "serverIndex")
)
if mibBuilder.loadTexts:
    serverGroupEntryConformanceTable.setStatus("current")

serverCounterGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 10, 2)
)
serverCounterGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "serverCounterCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetAdminGUID"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetClientIdGeneratorRecycleDelaySize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetClientIdGeneratorRecycleSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetClientIdGeneratorTimeout"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetCommittedVirtuallMemory"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetConnectionsMaximum"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetCoreHandlerPoolSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetCoreTransportPoolSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetCryptoPoolActiveCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetCryptoPoolMaxSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetCurrentHeapSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetDateStarted"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetDefaultStreamPrefix"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetGUID"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetHTTPHeaderServer"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetLiveStreamTranscoderSessionCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetLiveThreads"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetMaxHeapSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetPeakThreads"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetPublishersMaximum"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetRTMPTHeaderServer"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetServerGUID"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetSessionGUID"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetTimeRunning"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetTranscoderLicenseInUse"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetTranscoderLicenseTotal"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverCounterGetVersion"))
)
if mibBuilder.loadTexts:
    serverCounterGroupEntryConformanceTable.setStatus("current")

serverConnectGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 10, 3)
)
serverConnectGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "serverConnectCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverConnectGetCurrent"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverConnectGetLastConnectAcceptedStamp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverConnectGetLastConnectAcceptedStampString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverConnectGetLastConnectAcceptedTimeString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverConnectGetLastConnectRejectedStamp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverConnectGetLastConnectRejectedStampString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverConnectGetLastConnectRejectedTimeString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverConnectGetLastDisconnectStamp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverConnectGetLastDisconnectStampString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverConnectGetLastDisconnectTimeString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverConnectGetTotal"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverConnectGetTotalAccepted"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverConnectGetTotalRejected"))
)
if mibBuilder.loadTexts:
    serverConnectGroupEntryConformanceTable.setStatus("current")

serverPerformGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 10, 4)
)
serverPerformGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "serverPerformCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverPerformGetFileInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverPerformGetFileOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverPerformGetMessagesInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverPerformGetMessagesInCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverPerformGetMessagesInCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverPerformGetMessagesLossBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverPerformGetMessagesLossCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverPerformGetMessagesLossCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverPerformGetMessagesOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverPerformGetMessagesOutCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "serverPerformGetMessagesOutCountRate"))
)
if mibBuilder.loadTexts:
    serverPerformGroupEntryConformanceTable.setStatus("current")

vhostGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 20, 1)
)
vhostGroupEntryConformanceTable.setObjects(
    ("WOWZA-STREAMING-ENGINE-MIB", "vhostIndex")
)
if mibBuilder.loadTexts:
    vhostGroupEntryConformanceTable.setStatus("current")

vhostCounterGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 20, 2)
)
vhostCounterGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetApplicationTimeout"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetByteArrayOutputStreamBaseClassPath"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetClientCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetClientIdleFrequency"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetClientTimeout"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetConnectionLimit"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetCoreHandlerPoolSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetCoreTransportPoolSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetDateStarted"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetFileIOPoolSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetHTTPStreamerMaxPathLen"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetHomePath"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetIdleCheckFrequency"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetIdleMinimumWaitTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetIdleWorkerCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetKeepAliveTimeout"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetLiveStreamTranscoderSessionCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetMaximumPendingReadBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetMaximumPendingWriteBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetMaximumSetBufferTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetName"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetNetConnectionIdleFrequency"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetNetConnectionProcessorCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetNextMediaCasterId"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetNextNetConnectionId"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetPingTimeout"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetRTPIdleFrequency"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetRTSPMaxPathLen"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetScheduledReadMaxSessionBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetScheduledWriteBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetScheduledWriteMaxSessionBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetScheduledWriteMaxSessionClientId"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetScheduledWriteRequests"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetScheduledWriteSessions"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetStartupStreamsDelayTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetTimeRunning"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetUnidentifiedSessionTimeout"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetValidationFrequency"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetWaitingReadBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostCounterGetWebRTCIdleFrequency"))
)
if mibBuilder.loadTexts:
    vhostCounterGroupEntryConformanceTable.setStatus("current")

vhostConnectGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 20, 3)
)
vhostConnectGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "vhostConnectCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostConnectGetCurrent"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostConnectGetLastConnectAcceptedStamp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostConnectGetLastConnectAcceptedStampString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostConnectGetLastConnectAcceptedTimeString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostConnectGetLastConnectRejectedStamp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostConnectGetLastConnectRejectedStampString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostConnectGetLastConnectRejectedTimeString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostConnectGetLastDisconnectStamp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostConnectGetLastDisconnectStampString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostConnectGetLastDisconnectTimeString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostConnectGetTotal"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostConnectGetTotalAccepted"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostConnectGetTotalRejected"))
)
if mibBuilder.loadTexts:
    vhostConnectGroupEntryConformanceTable.setStatus("current")

vhostPerformGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 20, 4)
)
vhostPerformGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "vhostPerformCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostPerformGetFileInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostPerformGetFileOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostPerformGetMessagesInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostPerformGetMessagesInCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostPerformGetMessagesInCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostPerformGetMessagesLossBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostPerformGetMessagesLossCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostPerformGetMessagesLossCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostPerformGetMessagesOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostPerformGetMessagesOutCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "vhostPerformGetMessagesOutCountRate"))
)
if mibBuilder.loadTexts:
    vhostPerformGroupEntryConformanceTable.setStatus("current")

applicationGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 30, 1)
)
applicationGroupEntryConformanceTable.setObjects(
    ("WOWZA-STREAMING-ENGINE-MIB", "applicationIndex")
)
if mibBuilder.loadTexts:
    applicationGroupEntryConformanceTable.setStatus("current")

applicationCounterGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 30, 2)
)
applicationCounterGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "applicationCounterCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationCounterGetApplicationPath"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationCounterGetConfigPath"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationCounterGetDateStarted"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationCounterGetInstanceCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationCounterGetMessagesInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationCounterGetMessagesInCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationCounterGetMessagesInCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationCounterGetMessagesOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationCounterGetMessagesOutCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationCounterGetMessagesOutCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationCounterGetName"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationCounterGetTimeRunning"))
)
if mibBuilder.loadTexts:
    applicationCounterGroupEntryConformanceTable.setStatus("current")

applicationConnectGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 30, 3)
)
applicationConnectGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "applicationConnectCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationConnectGetCurrent"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationConnectGetLastConnectAcceptedStamp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationConnectGetLastConnectAcceptedStampString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationConnectGetLastConnectAcceptedTimeString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationConnectGetLastConnectRejectedStamp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationConnectGetLastConnectRejectedStampString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationConnectGetLastConnectRejectedTimeString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationConnectGetLastDisconnectStamp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationConnectGetLastDisconnectStampString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationConnectGetLastDisconnectTimeString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationConnectGetTotal"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationConnectGetTotalAccepted"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationConnectGetTotalRejected"))
)
if mibBuilder.loadTexts:
    applicationConnectGroupEntryConformanceTable.setStatus("current")

applicationPerformGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 30, 4)
)
applicationPerformGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "applicationPerformCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationPerformGetFileInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationPerformGetFileOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationPerformGetMessagesInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationPerformGetMessagesInCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationPerformGetMessagesInCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationPerformGetMessagesLossBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationPerformGetMessagesLossCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationPerformGetMessagesLossCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationPerformGetMessagesOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationPerformGetMessagesOutCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationPerformGetMessagesOutCountRate"))
)
if mibBuilder.loadTexts:
    applicationPerformGroupEntryConformanceTable.setStatus("current")

applicationInstanceGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 40, 1)
)
applicationInstanceGroupEntryConformanceTable.setObjects(
    ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceIndex")
)
if mibBuilder.loadTexts:
    applicationInstanceGroupEntryConformanceTable.setStatus("current")

applicationInstanceCounterGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 40, 2)
)
applicationInstanceCounterGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetApplicationInstanceTouchTimeout"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetApplicationTimeout"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetClientCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetClientCountTotal"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetClientIdleFrequency"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetClientRemoveTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetContextStr"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetDateStarted"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetDvrRecorderList"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetHTTPStreamerList"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetHTTPStreamerSessionCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetLastTouchTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetLiveStreamPacketizerList"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetLiveStreamTranscoderList"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetMaxStorageDirDepth"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetMaximumPendingReadBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetMaximumPendingWriteBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetMaximumSetBufferTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetMediacasterRTPRTSPRTPTransportMode"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetMessagesInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetMessagesInCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetMessagesInCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetMessagesOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetMessagesOutCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetMessagesOutCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetName"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetPingTimeout"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetPublisherCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetPushPublishSessionCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRTPAVSyncMethod"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRTPIdleFrequency"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRTPMaxRTCPWaitTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRTPPlayAuthenticationMethod"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRTPPublishAuthenticationMethod"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRTPSessionCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRTSPBindIpAddress"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRTSPConnectionAddressType"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRTSPConnectionIpAddress"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRTSPMaximumPendingWriteBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRTSPOriginAddressType"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRTSPOriginIpAddress"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRTSPSessionTimeout"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRepeaterOriginUrl"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRepeaterQueryString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRsoStorageDir"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetRsoStoragePath"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetSharedObjectReadAccess"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetSharedObjectWriteAccess"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetSourceControlSessionCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetStreamAudioSampleAccess"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetStreamCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetStreamKeyDir"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetStreamKeyPath"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetStreamReadAccess"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetStreamStorageDir"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetStreamStoragePath"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetStreamType"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetStreamVideoSampleAccess"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetStreamWriteAccess"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetTimeRunning"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetVODTimedTextProviderList"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceCounterGetValidationFrequency"))
)
if mibBuilder.loadTexts:
    applicationInstanceCounterGroupEntryConformanceTable.setStatus("current")

applicationInstanceConnectGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 40, 3)
)
applicationInstanceConnectGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceConnectCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceConnectGetCurrent"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceConnectGetLastConnectAcceptedStamp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceConnectGetLastConnectAcceptedStampString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceConnectGetLastConnectAcceptedTimeString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceConnectGetLastConnectRejectedStamp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceConnectGetLastConnectRejectedStampString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceConnectGetLastConnectRejectedTimeString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceConnectGetLastDisconnectStamp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceConnectGetLastDisconnectStampString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceConnectGetLastDisconnectTimeString"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceConnectGetTotal"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceConnectGetTotalAccepted"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstanceConnectGetTotalRejected"))
)
if mibBuilder.loadTexts:
    applicationInstanceConnectGroupEntryConformanceTable.setStatus("current")

applicationInstancePerformGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 40, 4)
)
applicationInstancePerformGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "applicationInstancePerformCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstancePerformGetFileInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstancePerformGetFileOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstancePerformGetMessagesInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstancePerformGetMessagesInCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstancePerformGetMessagesInCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstancePerformGetMessagesLossBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstancePerformGetMessagesLossCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstancePerformGetMessagesLossCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstancePerformGetMessagesOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstancePerformGetMessagesOutCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "applicationInstancePerformGetMessagesOutCountRate"))
)
if mibBuilder.loadTexts:
    applicationInstancePerformGroupEntryConformanceTable.setStatus("current")

streamGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 50, 1)
)
streamGroupEntryConformanceTable.setObjects(
    ("WOWZA-STREAMING-ENGINE-MIB", "streamIndex")
)
if mibBuilder.loadTexts:
    streamGroupEntryConformanceTable.setStatus("current")

streamCounterGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 50, 2)
)
streamCounterGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "streamCountCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetAudioMissing"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetAudioSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetAudioTC"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetBufferTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetCacheName"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetClientId"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetContextStr"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetDataMissing"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetDataSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetDataTC"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetDataType"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetDvrRecorder"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetDvrRecorderList"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetDvrRepeater"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetExt"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetFirstPacketTC"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetHeaderSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLastFlushAudioTC"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLastFlushDataTC"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLastFlushRTTimecode"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLastFlushTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLastFlushTimecode"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLastFlushVideoTC"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLastPacketTC"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLastReceivedAudioTC"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLastReceivedDataTC"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLastReceivedVideoTC"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLastSentAudioTC"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLastSentDataTC"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLastSentVideoTC"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLiveStreamPacketizer"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLiveStreamPacketizerList"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLiveStreamRepeater"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetLiveStreamTranscoderList"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetMaxTimecode"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetName"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetPacketCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetPublishAudioCodecId"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetPublishBitrateAudio"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetPublishBitrateVideo"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetPublishFrameCountAudio"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetPublishFrameCountData"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetPublishFrameCountVideo"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetPublishVideoCodecId"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetQueryStr"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetReceiveVideoFPS"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetSrc"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetStreamType"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetTimecodeOffset"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetTss"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetUniqueStreamIdStr"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetVideoMissing"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetVideoSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamCountGetVideoTC"))
)
if mibBuilder.loadTexts:
    streamCounterGroupEntryConformanceTable.setStatus("current")

streamPerformGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 50, 3)
)
streamPerformGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "streamPerformCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamPerformGetFileInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamPerformGetFileOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamPerformGetMessagesInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamPerformGetMessagesInCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamPerformGetMessagesInCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamPerformGetMessagesLossBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamPerformGetMessagesLossCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamPerformGetMessagesLossCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamPerformGetMessagesOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamPerformGetMessagesOutCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "streamPerformGetMessagesOutCountRate"))
)
if mibBuilder.loadTexts:
    streamPerformGroupEntryConformanceTable.setStatus("current")

clientGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 60, 1)
)
clientGroupEntryConformanceTable.setObjects(
    ("WOWZA-STREAMING-ENGINE-MIB", "clientIndex")
)
if mibBuilder.loadTexts:
    clientGroupEntryConformanceTable.setStatus("current")

rtmpClientCountGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 60, 2)
)
rtmpClientCountGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetAcceptConnectionDescription"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetBufferTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetClientId"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetConnectTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetDateStarted"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetDebugDumpData"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetFlashVer"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetHandshake"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetIdleFrequency"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetIp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetLastPingWriteId"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetLastReqChunkCounter"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetLastRequestType"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetLastStreamId"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetLastValidateTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetLeftOverCID"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetLeftOverMissing"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetLiveRepeaterCapabilities"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetLiveStreamPacketizerList"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetLiveStreamTranscoderList"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetMaximumPendingReadBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetMaximumPendingWriteBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetMaximumSetBufferTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetNextConfirmBytesReceived"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetObjectEncoding"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetPageUrl"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetPingRoundTripTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetPingTimeout"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetPlayResponse"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetPlayStreamCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetProtocol"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetPublishStreamCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetQueryStr"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetReceiveChunkSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetReferrer"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetRepeaterOriginUrl"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetRequestDataSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetRequestRTMPTSequence"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetResponseIndex"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetSendChunkSize"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetSharedObjectReadAccess"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetSharedObjectWriteAccess"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetStreamAudioSampleAccess"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetStreamReadAccess"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetStreamType"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetStreamVideoSampleAccess"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetStreamWriteAccess"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetTimeRunning"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetTimebase"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetTotalInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetTouch"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetUri"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientCountGetValidationFrequency"))
)
if mibBuilder.loadTexts:
    rtmpClientCountGroupEntryConformanceTable.setStatus("current")

rtmpClientPerformGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 60, 3)
)
rtmpClientPerformGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientPerformCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientPerformGetFileInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientPerformGetFileOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientPerformGetMessagesInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientPerformGetMessagesInCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientPerformGetMessagesInCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientPerformGetMessagesLossBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientPerformGetMessagesLossCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientPerformGetMessagesLossCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientPerformGetMessagesOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientPerformGetMessagesOutCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtmpClientPerformGetMessagesOutCountRate"))
)
if mibBuilder.loadTexts:
    rtmpClientPerformGroupEntryConformanceTable.setStatus("current")

rtspClientCountGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 60, 4)
)
rtspClientCountGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetCookieStr"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetIdleFrequency"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetIp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetLastAuthenticateMethod"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetQueryStr"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetRTSPTunnelingSessionId"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetRedirectSessionCode"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetRedirectSessionMessage"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetRedirectSessionURL"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetReferrer"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetServerIp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetServerPort"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetSessionId"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetTimeRunning"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetUri"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientCountGetUserAgent"))
)
if mibBuilder.loadTexts:
    rtspClientCountGroupEntryConformanceTable.setStatus("current")

rtspClientPerformGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 60, 5)
)
rtspClientPerformGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "rtspClientPerformCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientPerformGetFileInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientPerformGetFileOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientPerformGetMessagesInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientPerformGetMessagesInCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientPerformGetMessagesInCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientPerformGetMessagesLossBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientPerformGetMessagesLossCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientPerformGetMessagesLossCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientPerformGetMessagesOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientPerformGetMessagesOutCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "rtspClientPerformGetMessagesOutCountRate"))
)
if mibBuilder.loadTexts:
    rtspClientPerformGroupEntryConformanceTable.setStatus("current")

httpClientCountGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 60, 6)
)
httpClientCountGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetCookieStr"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetHTTPDate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetIpAddress"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetIsFirstChunk"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetLastRequest"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetLiveStreamingPacketizer"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetPlayDuration"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetPlaySeek"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetPlayStart"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetQueryStr"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetRedirectSessionCode"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetRedirectSessionContentType"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetRedirectSessionURL"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetReferrer"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetServerIp"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetServerPort"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetSessionId"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetSessionProtocol"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetSessionTimeout"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetSessionType"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetStreamExt"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetStreamName"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetStreamPosition"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetTimeRunning"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetUri"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetUserAgent"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetUserQueryStr"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientCountGetVODTranscodeNGRP"))
)
if mibBuilder.loadTexts:
    httpClientCountGroupEntryConformanceTable.setStatus("current")

httpClientPerformGroupEntryConformanceTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 2, 60, 7)
)
httpClientPerformGroupEntryConformanceTable.setObjects(
      *(("WOWZA-STREAMING-ENGINE-MIB", "httpClientPerformCreationTime"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientPerformGetFileInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientPerformGetFileOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientPerformGetMessagesInBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientPerformGetMessagesInCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientPerformGetMessagesInCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientPerformGetMessagesLossBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientPerformGetMessagesLossCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientPerformGetMessagesLossCountRate"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientPerformGetMessagesOutBytes"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientPerformGetMessagesOutCount"),
        ("WOWZA-STREAMING-ENGINE-MIB", "httpClientPerformGetMessagesOutCountRate"))
)
if mibBuilder.loadTexts:
    httpClientPerformGroupEntryConformanceTable.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wowzaEngineMIBComplianceServer = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3, 10, 1)
)
if mibBuilder.loadTexts:
    wowzaEngineMIBComplianceServer.setStatus(
        "current"
    )

wowzaEngineMIBComplianceVhost = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3, 20, 1)
)
if mibBuilder.loadTexts:
    wowzaEngineMIBComplianceVhost.setStatus(
        "current"
    )

wowzaEngineMIBComplianceApplication = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3, 30, 1)
)
if mibBuilder.loadTexts:
    wowzaEngineMIBComplianceApplication.setStatus(
        "current"
    )

wowzaEngineMIBComplianceApplicationInstance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3, 40, 1)
)
if mibBuilder.loadTexts:
    wowzaEngineMIBComplianceApplicationInstance.setStatus(
        "current"
    )

wowzaEngineMIBComplianceStream = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3, 50, 1)
)
if mibBuilder.loadTexts:
    wowzaEngineMIBComplianceStream.setStatus(
        "current"
    )

wowzaEngineMIBComplianceRTMPClient = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3, 60, 1)
)
if mibBuilder.loadTexts:
    wowzaEngineMIBComplianceRTMPClient.setStatus(
        "current"
    )

wowzaEngineMIBComplianceRTSPClient = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3, 60, 2)
)
if mibBuilder.loadTexts:
    wowzaEngineMIBComplianceRTSPClient.setStatus(
        "current"
    )

wowzaEngineMIBComplianceHTTPClient = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 46706, 100, 1, 3, 60, 3)
)
if mibBuilder.loadTexts:
    wowzaEngineMIBComplianceHTTPClient.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WOWZA-STREAMING-ENGINE-MIB",
    **{"wowzamediasystems": wowzamediasystems,
       "wowzaStreamingEngineMIB": wowzaStreamingEngineMIB,
       "conformance": conformance,
       "groups": groups,
       "groupServer": groupServer,
       "groupServerInfo": groupServerInfo,
       "serverGroupTable": serverGroupTable,
       "serverGroupEntry": serverGroupEntry,
       "serverIndex": serverIndex,
       "vhostIndex": vhostIndex,
       "applicationIndex": applicationIndex,
       "applicationInstanceIndex": applicationInstanceIndex,
       "streamIndex": streamIndex,
       "clientIndex": clientIndex,
       "groupObject": groupObject,
       "serverGroupObject": serverGroupObject,
       "serverGroupEntryConformanceTable": serverGroupEntryConformanceTable,
       "serverCounterGroupEntryConformanceTable": serverCounterGroupEntryConformanceTable,
       "serverConnectGroupEntryConformanceTable": serverConnectGroupEntryConformanceTable,
       "serverPerformGroupEntryConformanceTable": serverPerformGroupEntryConformanceTable,
       "vhostGroupObject": vhostGroupObject,
       "vhostGroupEntryConformanceTable": vhostGroupEntryConformanceTable,
       "vhostCounterGroupEntryConformanceTable": vhostCounterGroupEntryConformanceTable,
       "vhostConnectGroupEntryConformanceTable": vhostConnectGroupEntryConformanceTable,
       "vhostPerformGroupEntryConformanceTable": vhostPerformGroupEntryConformanceTable,
       "applicationGroupObject": applicationGroupObject,
       "applicationGroupEntryConformanceTable": applicationGroupEntryConformanceTable,
       "applicationCounterGroupEntryConformanceTable": applicationCounterGroupEntryConformanceTable,
       "applicationConnectGroupEntryConformanceTable": applicationConnectGroupEntryConformanceTable,
       "applicationPerformGroupEntryConformanceTable": applicationPerformGroupEntryConformanceTable,
       "applicationInstanceGroupObject": applicationInstanceGroupObject,
       "applicationInstanceGroupEntryConformanceTable": applicationInstanceGroupEntryConformanceTable,
       "applicationInstanceCounterGroupEntryConformanceTable": applicationInstanceCounterGroupEntryConformanceTable,
       "applicationInstanceConnectGroupEntryConformanceTable": applicationInstanceConnectGroupEntryConformanceTable,
       "applicationInstancePerformGroupEntryConformanceTable": applicationInstancePerformGroupEntryConformanceTable,
       "streamGroupObject": streamGroupObject,
       "streamGroupEntryConformanceTable": streamGroupEntryConformanceTable,
       "streamCounterGroupEntryConformanceTable": streamCounterGroupEntryConformanceTable,
       "streamPerformGroupEntryConformanceTable": streamPerformGroupEntryConformanceTable,
       "clientGroupObject": clientGroupObject,
       "clientGroupEntryConformanceTable": clientGroupEntryConformanceTable,
       "rtmpClientCountGroupEntryConformanceTable": rtmpClientCountGroupEntryConformanceTable,
       "rtmpClientPerformGroupEntryConformanceTable": rtmpClientPerformGroupEntryConformanceTable,
       "rtspClientCountGroupEntryConformanceTable": rtspClientCountGroupEntryConformanceTable,
       "rtspClientPerformGroupEntryConformanceTable": rtspClientPerformGroupEntryConformanceTable,
       "httpClientCountGroupEntryConformanceTable": httpClientCountGroupEntryConformanceTable,
       "httpClientPerformGroupEntryConformanceTable": httpClientPerformGroupEntryConformanceTable,
       "compliances": compliances,
       "complianceServer": complianceServer,
       "wowzaEngineMIBComplianceServer": wowzaEngineMIBComplianceServer,
       "complianceVhost": complianceVhost,
       "wowzaEngineMIBComplianceVhost": wowzaEngineMIBComplianceVhost,
       "complianceApplication": complianceApplication,
       "wowzaEngineMIBComplianceApplication": wowzaEngineMIBComplianceApplication,
       "complianceApplicationInstance": complianceApplicationInstance,
       "wowzaEngineMIBComplianceApplicationInstance": wowzaEngineMIBComplianceApplicationInstance,
       "complianceStream": complianceStream,
       "wowzaEngineMIBComplianceStream": wowzaEngineMIBComplianceStream,
       "complianceClient": complianceClient,
       "wowzaEngineMIBComplianceRTMPClient": wowzaEngineMIBComplianceRTMPClient,
       "wowzaEngineMIBComplianceRTSPClient": wowzaEngineMIBComplianceRTSPClient,
       "wowzaEngineMIBComplianceHTTPClient": wowzaEngineMIBComplianceHTTPClient,
       "servers": servers,
       "serverInfo": serverInfo,
       "serverCounterTable": serverCounterTable,
       "serverCounterEntry": serverCounterEntry,
       "serverCounterCreationTime": serverCounterCreationTime,
       "serverCounterGetAdminGUID": serverCounterGetAdminGUID,
       "serverCounterGetClientIdGeneratorRecycleDelaySize": serverCounterGetClientIdGeneratorRecycleDelaySize,
       "serverCounterGetClientIdGeneratorRecycleSize": serverCounterGetClientIdGeneratorRecycleSize,
       "serverCounterGetClientIdGeneratorTimeout": serverCounterGetClientIdGeneratorTimeout,
       "serverCounterGetCommittedVirtuallMemory": serverCounterGetCommittedVirtuallMemory,
       "serverCounterGetConnectionsMaximum": serverCounterGetConnectionsMaximum,
       "serverCounterGetCoreHandlerPoolSize": serverCounterGetCoreHandlerPoolSize,
       "serverCounterGetCoreTransportPoolSize": serverCounterGetCoreTransportPoolSize,
       "serverCounterGetCryptoPoolActiveCount": serverCounterGetCryptoPoolActiveCount,
       "serverCounterGetCryptoPoolMaxSize": serverCounterGetCryptoPoolMaxSize,
       "serverCounterGetCurrentHeapSize": serverCounterGetCurrentHeapSize,
       "serverCounterGetDateStarted": serverCounterGetDateStarted,
       "serverCounterGetDefaultStreamPrefix": serverCounterGetDefaultStreamPrefix,
       "serverCounterGetGUID": serverCounterGetGUID,
       "serverCounterGetHTTPHeaderServer": serverCounterGetHTTPHeaderServer,
       "serverCounterGetLiveStreamTranscoderSessionCount": serverCounterGetLiveStreamTranscoderSessionCount,
       "serverCounterGetLiveThreads": serverCounterGetLiveThreads,
       "serverCounterGetMaxHeapSize": serverCounterGetMaxHeapSize,
       "serverCounterGetPeakThreads": serverCounterGetPeakThreads,
       "serverCounterGetPublishersMaximum": serverCounterGetPublishersMaximum,
       "serverCounterGetRTMPTHeaderServer": serverCounterGetRTMPTHeaderServer,
       "serverCounterGetServerGUID": serverCounterGetServerGUID,
       "serverCounterGetSessionGUID": serverCounterGetSessionGUID,
       "serverCounterGetTimeRunning": serverCounterGetTimeRunning,
       "serverCounterGetTranscoderLicenseInUse": serverCounterGetTranscoderLicenseInUse,
       "serverCounterGetTranscoderLicenseTotal": serverCounterGetTranscoderLicenseTotal,
       "serverCounterGetVersion": serverCounterGetVersion,
       "serverConnectTable": serverConnectTable,
       "serverConnectEntry": serverConnectEntry,
       "serverConnectCreationTime": serverConnectCreationTime,
       "serverConnectGetCurrent": serverConnectGetCurrent,
       "serverConnectGetLastConnectAcceptedStamp": serverConnectGetLastConnectAcceptedStamp,
       "serverConnectGetLastConnectAcceptedStampString": serverConnectGetLastConnectAcceptedStampString,
       "serverConnectGetLastConnectAcceptedTimeString": serverConnectGetLastConnectAcceptedTimeString,
       "serverConnectGetLastConnectRejectedStamp": serverConnectGetLastConnectRejectedStamp,
       "serverConnectGetLastConnectRejectedStampString": serverConnectGetLastConnectRejectedStampString,
       "serverConnectGetLastConnectRejectedTimeString": serverConnectGetLastConnectRejectedTimeString,
       "serverConnectGetLastDisconnectStamp": serverConnectGetLastDisconnectStamp,
       "serverConnectGetLastDisconnectStampString": serverConnectGetLastDisconnectStampString,
       "serverConnectGetLastDisconnectTimeString": serverConnectGetLastDisconnectTimeString,
       "serverConnectGetTotal": serverConnectGetTotal,
       "serverConnectGetTotalAccepted": serverConnectGetTotalAccepted,
       "serverConnectGetTotalRejected": serverConnectGetTotalRejected,
       "serverPerformTable": serverPerformTable,
       "serverPerformEntry": serverPerformEntry,
       "serverPerformCreationTime": serverPerformCreationTime,
       "serverPerformGetFileInBytes": serverPerformGetFileInBytes,
       "serverPerformGetFileOutBytes": serverPerformGetFileOutBytes,
       "serverPerformGetMessagesInBytes": serverPerformGetMessagesInBytes,
       "serverPerformGetMessagesInCount": serverPerformGetMessagesInCount,
       "serverPerformGetMessagesInCountRate": serverPerformGetMessagesInCountRate,
       "serverPerformGetMessagesLossBytes": serverPerformGetMessagesLossBytes,
       "serverPerformGetMessagesLossCount": serverPerformGetMessagesLossCount,
       "serverPerformGetMessagesLossCountRate": serverPerformGetMessagesLossCountRate,
       "serverPerformGetMessagesOutBytes": serverPerformGetMessagesOutBytes,
       "serverPerformGetMessagesOutCount": serverPerformGetMessagesOutCount,
       "serverPerformGetMessagesOutCountRate": serverPerformGetMessagesOutCountRate,
       "vhosts": vhosts,
       "vhostInfo": vhostInfo,
       "vhostCounterTable": vhostCounterTable,
       "vhostCounterEntry": vhostCounterEntry,
       "vhostCounterCreationTime": vhostCounterCreationTime,
       "vhostCounterGetApplicationTimeout": vhostCounterGetApplicationTimeout,
       "vhostCounterGetByteArrayOutputStreamBaseClassPath": vhostCounterGetByteArrayOutputStreamBaseClassPath,
       "vhostCounterGetClientCount": vhostCounterGetClientCount,
       "vhostCounterGetClientIdleFrequency": vhostCounterGetClientIdleFrequency,
       "vhostCounterGetClientTimeout": vhostCounterGetClientTimeout,
       "vhostCounterGetConnectionLimit": vhostCounterGetConnectionLimit,
       "vhostCounterGetCoreHandlerPoolSize": vhostCounterGetCoreHandlerPoolSize,
       "vhostCounterGetCoreTransportPoolSize": vhostCounterGetCoreTransportPoolSize,
       "vhostCounterGetDateStarted": vhostCounterGetDateStarted,
       "vhostCounterGetFileIOPoolSize": vhostCounterGetFileIOPoolSize,
       "vhostCounterGetHTTPStreamerMaxPathLen": vhostCounterGetHTTPStreamerMaxPathLen,
       "vhostCounterGetHomePath": vhostCounterGetHomePath,
       "vhostCounterGetIdleCheckFrequency": vhostCounterGetIdleCheckFrequency,
       "vhostCounterGetIdleMinimumWaitTime": vhostCounterGetIdleMinimumWaitTime,
       "vhostCounterGetIdleWorkerCount": vhostCounterGetIdleWorkerCount,
       "vhostCounterGetKeepAliveTimeout": vhostCounterGetKeepAliveTimeout,
       "vhostCounterGetLiveStreamTranscoderSessionCount": vhostCounterGetLiveStreamTranscoderSessionCount,
       "vhostCounterGetMaximumPendingReadBytes": vhostCounterGetMaximumPendingReadBytes,
       "vhostCounterGetMaximumPendingWriteBytes": vhostCounterGetMaximumPendingWriteBytes,
       "vhostCounterGetMaximumSetBufferTime": vhostCounterGetMaximumSetBufferTime,
       "vhostCounterGetName": vhostCounterGetName,
       "vhostCounterGetNetConnectionIdleFrequency": vhostCounterGetNetConnectionIdleFrequency,
       "vhostCounterGetNetConnectionProcessorCount": vhostCounterGetNetConnectionProcessorCount,
       "vhostCounterGetNextMediaCasterId": vhostCounterGetNextMediaCasterId,
       "vhostCounterGetNextNetConnectionId": vhostCounterGetNextNetConnectionId,
       "vhostCounterGetPingTimeout": vhostCounterGetPingTimeout,
       "vhostCounterGetRTPIdleFrequency": vhostCounterGetRTPIdleFrequency,
       "vhostCounterGetRTSPMaxPathLen": vhostCounterGetRTSPMaxPathLen,
       "vhostCounterGetScheduledReadMaxSessionBytes": vhostCounterGetScheduledReadMaxSessionBytes,
       "vhostCounterGetScheduledWriteBytes": vhostCounterGetScheduledWriteBytes,
       "vhostCounterGetScheduledWriteMaxSessionBytes": vhostCounterGetScheduledWriteMaxSessionBytes,
       "vhostCounterGetScheduledWriteMaxSessionClientId": vhostCounterGetScheduledWriteMaxSessionClientId,
       "vhostCounterGetScheduledWriteRequests": vhostCounterGetScheduledWriteRequests,
       "vhostCounterGetScheduledWriteSessions": vhostCounterGetScheduledWriteSessions,
       "vhostCounterGetStartupStreamsDelayTime": vhostCounterGetStartupStreamsDelayTime,
       "vhostCounterGetTimeRunning": vhostCounterGetTimeRunning,
       "vhostCounterGetUnidentifiedSessionTimeout": vhostCounterGetUnidentifiedSessionTimeout,
       "vhostCounterGetValidationFrequency": vhostCounterGetValidationFrequency,
       "vhostCounterGetWaitingReadBytes": vhostCounterGetWaitingReadBytes,
       "vhostCounterGetWebRTCIdleFrequency": vhostCounterGetWebRTCIdleFrequency,
       "vhostConnectTable": vhostConnectTable,
       "vhostConnectEntry": vhostConnectEntry,
       "vhostConnectCreationTime": vhostConnectCreationTime,
       "vhostConnectGetCurrent": vhostConnectGetCurrent,
       "vhostConnectGetLastConnectAcceptedStamp": vhostConnectGetLastConnectAcceptedStamp,
       "vhostConnectGetLastConnectAcceptedStampString": vhostConnectGetLastConnectAcceptedStampString,
       "vhostConnectGetLastConnectAcceptedTimeString": vhostConnectGetLastConnectAcceptedTimeString,
       "vhostConnectGetLastConnectRejectedStamp": vhostConnectGetLastConnectRejectedStamp,
       "vhostConnectGetLastConnectRejectedStampString": vhostConnectGetLastConnectRejectedStampString,
       "vhostConnectGetLastConnectRejectedTimeString": vhostConnectGetLastConnectRejectedTimeString,
       "vhostConnectGetLastDisconnectStamp": vhostConnectGetLastDisconnectStamp,
       "vhostConnectGetLastDisconnectStampString": vhostConnectGetLastDisconnectStampString,
       "vhostConnectGetLastDisconnectTimeString": vhostConnectGetLastDisconnectTimeString,
       "vhostConnectGetTotal": vhostConnectGetTotal,
       "vhostConnectGetTotalAccepted": vhostConnectGetTotalAccepted,
       "vhostConnectGetTotalRejected": vhostConnectGetTotalRejected,
       "vhostPerformTable": vhostPerformTable,
       "vhostPerformEntry": vhostPerformEntry,
       "vhostPerformCreationTime": vhostPerformCreationTime,
       "vhostPerformGetFileInBytes": vhostPerformGetFileInBytes,
       "vhostPerformGetFileOutBytes": vhostPerformGetFileOutBytes,
       "vhostPerformGetMessagesInBytes": vhostPerformGetMessagesInBytes,
       "vhostPerformGetMessagesInCount": vhostPerformGetMessagesInCount,
       "vhostPerformGetMessagesInCountRate": vhostPerformGetMessagesInCountRate,
       "vhostPerformGetMessagesLossBytes": vhostPerformGetMessagesLossBytes,
       "vhostPerformGetMessagesLossCount": vhostPerformGetMessagesLossCount,
       "vhostPerformGetMessagesLossCountRate": vhostPerformGetMessagesLossCountRate,
       "vhostPerformGetMessagesOutBytes": vhostPerformGetMessagesOutBytes,
       "vhostPerformGetMessagesOutCount": vhostPerformGetMessagesOutCount,
       "vhostPerformGetMessagesOutCountRate": vhostPerformGetMessagesOutCountRate,
       "applications": applications,
       "applicationInfo": applicationInfo,
       "applicationCounterTable": applicationCounterTable,
       "applicationCounterEntry": applicationCounterEntry,
       "applicationCounterCreationTime": applicationCounterCreationTime,
       "applicationCounterGetApplicationPath": applicationCounterGetApplicationPath,
       "applicationCounterGetConfigPath": applicationCounterGetConfigPath,
       "applicationCounterGetDateStarted": applicationCounterGetDateStarted,
       "applicationCounterGetInstanceCount": applicationCounterGetInstanceCount,
       "applicationCounterGetMessagesInBytes": applicationCounterGetMessagesInBytes,
       "applicationCounterGetMessagesInCount": applicationCounterGetMessagesInCount,
       "applicationCounterGetMessagesInCountRate": applicationCounterGetMessagesInCountRate,
       "applicationCounterGetMessagesOutBytes": applicationCounterGetMessagesOutBytes,
       "applicationCounterGetMessagesOutCount": applicationCounterGetMessagesOutCount,
       "applicationCounterGetMessagesOutCountRate": applicationCounterGetMessagesOutCountRate,
       "applicationCounterGetName": applicationCounterGetName,
       "applicationCounterGetTimeRunning": applicationCounterGetTimeRunning,
       "applicationConnectTable": applicationConnectTable,
       "applicationConnectEntry": applicationConnectEntry,
       "applicationConnectCreationTime": applicationConnectCreationTime,
       "applicationConnectGetCurrent": applicationConnectGetCurrent,
       "applicationConnectGetLastConnectAcceptedStamp": applicationConnectGetLastConnectAcceptedStamp,
       "applicationConnectGetLastConnectAcceptedStampString": applicationConnectGetLastConnectAcceptedStampString,
       "applicationConnectGetLastConnectAcceptedTimeString": applicationConnectGetLastConnectAcceptedTimeString,
       "applicationConnectGetLastConnectRejectedStamp": applicationConnectGetLastConnectRejectedStamp,
       "applicationConnectGetLastConnectRejectedStampString": applicationConnectGetLastConnectRejectedStampString,
       "applicationConnectGetLastConnectRejectedTimeString": applicationConnectGetLastConnectRejectedTimeString,
       "applicationConnectGetLastDisconnectStamp": applicationConnectGetLastDisconnectStamp,
       "applicationConnectGetLastDisconnectStampString": applicationConnectGetLastDisconnectStampString,
       "applicationConnectGetLastDisconnectTimeString": applicationConnectGetLastDisconnectTimeString,
       "applicationConnectGetTotal": applicationConnectGetTotal,
       "applicationConnectGetTotalAccepted": applicationConnectGetTotalAccepted,
       "applicationConnectGetTotalRejected": applicationConnectGetTotalRejected,
       "applicationPerformTable": applicationPerformTable,
       "applicationPerformEntry": applicationPerformEntry,
       "applicationPerformCreationTime": applicationPerformCreationTime,
       "applicationPerformGetFileInBytes": applicationPerformGetFileInBytes,
       "applicationPerformGetFileOutBytes": applicationPerformGetFileOutBytes,
       "applicationPerformGetMessagesInBytes": applicationPerformGetMessagesInBytes,
       "applicationPerformGetMessagesInCount": applicationPerformGetMessagesInCount,
       "applicationPerformGetMessagesInCountRate": applicationPerformGetMessagesInCountRate,
       "applicationPerformGetMessagesLossBytes": applicationPerformGetMessagesLossBytes,
       "applicationPerformGetMessagesLossCount": applicationPerformGetMessagesLossCount,
       "applicationPerformGetMessagesLossCountRate": applicationPerformGetMessagesLossCountRate,
       "applicationPerformGetMessagesOutBytes": applicationPerformGetMessagesOutBytes,
       "applicationPerformGetMessagesOutCount": applicationPerformGetMessagesOutCount,
       "applicationPerformGetMessagesOutCountRate": applicationPerformGetMessagesOutCountRate,
       "applicationInstances": applicationInstances,
       "applicationInstanceInfo": applicationInstanceInfo,
       "applicationInstanceCounterTable": applicationInstanceCounterTable,
       "applicationInstanceCounterEntry": applicationInstanceCounterEntry,
       "applicationInstanceCounterCreationTime": applicationInstanceCounterCreationTime,
       "applicationInstanceCounterGetApplicationInstanceTouchTimeout": applicationInstanceCounterGetApplicationInstanceTouchTimeout,
       "applicationInstanceCounterGetApplicationTimeout": applicationInstanceCounterGetApplicationTimeout,
       "applicationInstanceCounterGetClientCount": applicationInstanceCounterGetClientCount,
       "applicationInstanceCounterGetClientCountTotal": applicationInstanceCounterGetClientCountTotal,
       "applicationInstanceCounterGetClientIdleFrequency": applicationInstanceCounterGetClientIdleFrequency,
       "applicationInstanceCounterGetClientRemoveTime": applicationInstanceCounterGetClientRemoveTime,
       "applicationInstanceCounterGetContextStr": applicationInstanceCounterGetContextStr,
       "applicationInstanceCounterGetDateStarted": applicationInstanceCounterGetDateStarted,
       "applicationInstanceCounterGetDvrRecorderList": applicationInstanceCounterGetDvrRecorderList,
       "applicationInstanceCounterGetHTTPStreamerList": applicationInstanceCounterGetHTTPStreamerList,
       "applicationInstanceCounterGetHTTPStreamerSessionCount": applicationInstanceCounterGetHTTPStreamerSessionCount,
       "applicationInstanceCounterGetLastTouchTime": applicationInstanceCounterGetLastTouchTime,
       "applicationInstanceCounterGetLiveStreamPacketizerList": applicationInstanceCounterGetLiveStreamPacketizerList,
       "applicationInstanceCounterGetLiveStreamTranscoderList": applicationInstanceCounterGetLiveStreamTranscoderList,
       "applicationInstanceCounterGetMaxStorageDirDepth": applicationInstanceCounterGetMaxStorageDirDepth,
       "applicationInstanceCounterGetMaximumPendingReadBytes": applicationInstanceCounterGetMaximumPendingReadBytes,
       "applicationInstanceCounterGetMaximumPendingWriteBytes": applicationInstanceCounterGetMaximumPendingWriteBytes,
       "applicationInstanceCounterGetMaximumSetBufferTime": applicationInstanceCounterGetMaximumSetBufferTime,
       "applicationInstanceCounterGetMediacasterRTPRTSPRTPTransportMode": applicationInstanceCounterGetMediacasterRTPRTSPRTPTransportMode,
       "applicationInstanceCounterGetMessagesInBytes": applicationInstanceCounterGetMessagesInBytes,
       "applicationInstanceCounterGetMessagesInCount": applicationInstanceCounterGetMessagesInCount,
       "applicationInstanceCounterGetMessagesInCountRate": applicationInstanceCounterGetMessagesInCountRate,
       "applicationInstanceCounterGetMessagesOutBytes": applicationInstanceCounterGetMessagesOutBytes,
       "applicationInstanceCounterGetMessagesOutCount": applicationInstanceCounterGetMessagesOutCount,
       "applicationInstanceCounterGetMessagesOutCountRate": applicationInstanceCounterGetMessagesOutCountRate,
       "applicationInstanceCounterGetName": applicationInstanceCounterGetName,
       "applicationInstanceCounterGetPingTimeout": applicationInstanceCounterGetPingTimeout,
       "applicationInstanceCounterGetPublisherCount": applicationInstanceCounterGetPublisherCount,
       "applicationInstanceCounterGetPushPublishSessionCount": applicationInstanceCounterGetPushPublishSessionCount,
       "applicationInstanceCounterGetRTPAVSyncMethod": applicationInstanceCounterGetRTPAVSyncMethod,
       "applicationInstanceCounterGetRTPIdleFrequency": applicationInstanceCounterGetRTPIdleFrequency,
       "applicationInstanceCounterGetRTPMaxRTCPWaitTime": applicationInstanceCounterGetRTPMaxRTCPWaitTime,
       "applicationInstanceCounterGetRTPPlayAuthenticationMethod": applicationInstanceCounterGetRTPPlayAuthenticationMethod,
       "applicationInstanceCounterGetRTPPublishAuthenticationMethod": applicationInstanceCounterGetRTPPublishAuthenticationMethod,
       "applicationInstanceCounterGetRTPSessionCount": applicationInstanceCounterGetRTPSessionCount,
       "applicationInstanceCounterGetRTSPBindIpAddress": applicationInstanceCounterGetRTSPBindIpAddress,
       "applicationInstanceCounterGetRTSPConnectionAddressType": applicationInstanceCounterGetRTSPConnectionAddressType,
       "applicationInstanceCounterGetRTSPConnectionIpAddress": applicationInstanceCounterGetRTSPConnectionIpAddress,
       "applicationInstanceCounterGetRTSPMaximumPendingWriteBytes": applicationInstanceCounterGetRTSPMaximumPendingWriteBytes,
       "applicationInstanceCounterGetRTSPOriginAddressType": applicationInstanceCounterGetRTSPOriginAddressType,
       "applicationInstanceCounterGetRTSPOriginIpAddress": applicationInstanceCounterGetRTSPOriginIpAddress,
       "applicationInstanceCounterGetRTSPSessionTimeout": applicationInstanceCounterGetRTSPSessionTimeout,
       "applicationInstanceCounterGetRepeaterOriginUrl": applicationInstanceCounterGetRepeaterOriginUrl,
       "applicationInstanceCounterGetRepeaterQueryString": applicationInstanceCounterGetRepeaterQueryString,
       "applicationInstanceCounterGetRsoStorageDir": applicationInstanceCounterGetRsoStorageDir,
       "applicationInstanceCounterGetRsoStoragePath": applicationInstanceCounterGetRsoStoragePath,
       "applicationInstanceCounterGetSharedObjectReadAccess": applicationInstanceCounterGetSharedObjectReadAccess,
       "applicationInstanceCounterGetSharedObjectWriteAccess": applicationInstanceCounterGetSharedObjectWriteAccess,
       "applicationInstanceCounterGetSourceControlSessionCount": applicationInstanceCounterGetSourceControlSessionCount,
       "applicationInstanceCounterGetStreamAudioSampleAccess": applicationInstanceCounterGetStreamAudioSampleAccess,
       "applicationInstanceCounterGetStreamCount": applicationInstanceCounterGetStreamCount,
       "applicationInstanceCounterGetStreamKeyDir": applicationInstanceCounterGetStreamKeyDir,
       "applicationInstanceCounterGetStreamKeyPath": applicationInstanceCounterGetStreamKeyPath,
       "applicationInstanceCounterGetStreamReadAccess": applicationInstanceCounterGetStreamReadAccess,
       "applicationInstanceCounterGetStreamStorageDir": applicationInstanceCounterGetStreamStorageDir,
       "applicationInstanceCounterGetStreamStoragePath": applicationInstanceCounterGetStreamStoragePath,
       "applicationInstanceCounterGetStreamType": applicationInstanceCounterGetStreamType,
       "applicationInstanceCounterGetStreamVideoSampleAccess": applicationInstanceCounterGetStreamVideoSampleAccess,
       "applicationInstanceCounterGetStreamWriteAccess": applicationInstanceCounterGetStreamWriteAccess,
       "applicationInstanceCounterGetTimeRunning": applicationInstanceCounterGetTimeRunning,
       "applicationInstanceCounterGetVODTimedTextProviderList": applicationInstanceCounterGetVODTimedTextProviderList,
       "applicationInstanceCounterGetValidationFrequency": applicationInstanceCounterGetValidationFrequency,
       "applicationInstanceConnectTable": applicationInstanceConnectTable,
       "applicationInstanceConnectEntry": applicationInstanceConnectEntry,
       "applicationInstanceConnectCreationTime": applicationInstanceConnectCreationTime,
       "applicationInstanceConnectGetCurrent": applicationInstanceConnectGetCurrent,
       "applicationInstanceConnectGetLastConnectAcceptedStamp": applicationInstanceConnectGetLastConnectAcceptedStamp,
       "applicationInstanceConnectGetLastConnectAcceptedStampString": applicationInstanceConnectGetLastConnectAcceptedStampString,
       "applicationInstanceConnectGetLastConnectAcceptedTimeString": applicationInstanceConnectGetLastConnectAcceptedTimeString,
       "applicationInstanceConnectGetLastConnectRejectedStamp": applicationInstanceConnectGetLastConnectRejectedStamp,
       "applicationInstanceConnectGetLastConnectRejectedStampString": applicationInstanceConnectGetLastConnectRejectedStampString,
       "applicationInstanceConnectGetLastConnectRejectedTimeString": applicationInstanceConnectGetLastConnectRejectedTimeString,
       "applicationInstanceConnectGetLastDisconnectStamp": applicationInstanceConnectGetLastDisconnectStamp,
       "applicationInstanceConnectGetLastDisconnectStampString": applicationInstanceConnectGetLastDisconnectStampString,
       "applicationInstanceConnectGetLastDisconnectTimeString": applicationInstanceConnectGetLastDisconnectTimeString,
       "applicationInstanceConnectGetTotal": applicationInstanceConnectGetTotal,
       "applicationInstanceConnectGetTotalAccepted": applicationInstanceConnectGetTotalAccepted,
       "applicationInstanceConnectGetTotalRejected": applicationInstanceConnectGetTotalRejected,
       "applicationInstancePerformTable": applicationInstancePerformTable,
       "applicationInstancePerformEntry": applicationInstancePerformEntry,
       "applicationInstancePerformCreationTime": applicationInstancePerformCreationTime,
       "applicationInstancePerformGetFileInBytes": applicationInstancePerformGetFileInBytes,
       "applicationInstancePerformGetFileOutBytes": applicationInstancePerformGetFileOutBytes,
       "applicationInstancePerformGetMessagesInBytes": applicationInstancePerformGetMessagesInBytes,
       "applicationInstancePerformGetMessagesInCount": applicationInstancePerformGetMessagesInCount,
       "applicationInstancePerformGetMessagesInCountRate": applicationInstancePerformGetMessagesInCountRate,
       "applicationInstancePerformGetMessagesLossBytes": applicationInstancePerformGetMessagesLossBytes,
       "applicationInstancePerformGetMessagesLossCount": applicationInstancePerformGetMessagesLossCount,
       "applicationInstancePerformGetMessagesLossCountRate": applicationInstancePerformGetMessagesLossCountRate,
       "applicationInstancePerformGetMessagesOutBytes": applicationInstancePerformGetMessagesOutBytes,
       "applicationInstancePerformGetMessagesOutCount": applicationInstancePerformGetMessagesOutCount,
       "applicationInstancePerformGetMessagesOutCountRate": applicationInstancePerformGetMessagesOutCountRate,
       "streams": streams,
       "streamInfo": streamInfo,
       "streamCountTable": streamCountTable,
       "streamCountEntry": streamCountEntry,
       "streamCountCreationTime": streamCountCreationTime,
       "streamCountGetAudioMissing": streamCountGetAudioMissing,
       "streamCountGetAudioSize": streamCountGetAudioSize,
       "streamCountGetAudioTC": streamCountGetAudioTC,
       "streamCountGetBufferTime": streamCountGetBufferTime,
       "streamCountGetCacheName": streamCountGetCacheName,
       "streamCountGetClientId": streamCountGetClientId,
       "streamCountGetContextStr": streamCountGetContextStr,
       "streamCountGetDataMissing": streamCountGetDataMissing,
       "streamCountGetDataSize": streamCountGetDataSize,
       "streamCountGetDataTC": streamCountGetDataTC,
       "streamCountGetDataType": streamCountGetDataType,
       "streamCountGetDvrRecorder": streamCountGetDvrRecorder,
       "streamCountGetDvrRecorderList": streamCountGetDvrRecorderList,
       "streamCountGetDvrRepeater": streamCountGetDvrRepeater,
       "streamCountGetExt": streamCountGetExt,
       "streamCountGetFirstPacketTC": streamCountGetFirstPacketTC,
       "streamCountGetHeaderSize": streamCountGetHeaderSize,
       "streamCountGetLastFlushAudioTC": streamCountGetLastFlushAudioTC,
       "streamCountGetLastFlushDataTC": streamCountGetLastFlushDataTC,
       "streamCountGetLastFlushRTTimecode": streamCountGetLastFlushRTTimecode,
       "streamCountGetLastFlushTime": streamCountGetLastFlushTime,
       "streamCountGetLastFlushTimecode": streamCountGetLastFlushTimecode,
       "streamCountGetLastFlushVideoTC": streamCountGetLastFlushVideoTC,
       "streamCountGetLastPacketTC": streamCountGetLastPacketTC,
       "streamCountGetLastReceivedAudioTC": streamCountGetLastReceivedAudioTC,
       "streamCountGetLastReceivedDataTC": streamCountGetLastReceivedDataTC,
       "streamCountGetLastReceivedVideoTC": streamCountGetLastReceivedVideoTC,
       "streamCountGetLastSentAudioTC": streamCountGetLastSentAudioTC,
       "streamCountGetLastSentDataTC": streamCountGetLastSentDataTC,
       "streamCountGetLastSentVideoTC": streamCountGetLastSentVideoTC,
       "streamCountGetLiveStreamPacketizer": streamCountGetLiveStreamPacketizer,
       "streamCountGetLiveStreamPacketizerList": streamCountGetLiveStreamPacketizerList,
       "streamCountGetLiveStreamRepeater": streamCountGetLiveStreamRepeater,
       "streamCountGetLiveStreamTranscoderList": streamCountGetLiveStreamTranscoderList,
       "streamCountGetMaxTimecode": streamCountGetMaxTimecode,
       "streamCountGetName": streamCountGetName,
       "streamCountGetPacketCount": streamCountGetPacketCount,
       "streamCountGetPublishAudioCodecId": streamCountGetPublishAudioCodecId,
       "streamCountGetPublishBitrateAudio": streamCountGetPublishBitrateAudio,
       "streamCountGetPublishBitrateVideo": streamCountGetPublishBitrateVideo,
       "streamCountGetPublishFrameCountAudio": streamCountGetPublishFrameCountAudio,
       "streamCountGetPublishFrameCountData": streamCountGetPublishFrameCountData,
       "streamCountGetPublishFrameCountVideo": streamCountGetPublishFrameCountVideo,
       "streamCountGetPublishVideoCodecId": streamCountGetPublishVideoCodecId,
       "streamCountGetQueryStr": streamCountGetQueryStr,
       "streamCountGetReceiveVideoFPS": streamCountGetReceiveVideoFPS,
       "streamCountGetSrc": streamCountGetSrc,
       "streamCountGetStreamType": streamCountGetStreamType,
       "streamCountGetTimecodeOffset": streamCountGetTimecodeOffset,
       "streamCountGetTss": streamCountGetTss,
       "streamCountGetUniqueStreamIdStr": streamCountGetUniqueStreamIdStr,
       "streamCountGetVideoMissing": streamCountGetVideoMissing,
       "streamCountGetVideoSize": streamCountGetVideoSize,
       "streamCountGetVideoTC": streamCountGetVideoTC,
       "streamPerformTable": streamPerformTable,
       "streamPerformEntry": streamPerformEntry,
       "streamPerformCreationTime": streamPerformCreationTime,
       "streamPerformGetFileInBytes": streamPerformGetFileInBytes,
       "streamPerformGetFileOutBytes": streamPerformGetFileOutBytes,
       "streamPerformGetMessagesInBytes": streamPerformGetMessagesInBytes,
       "streamPerformGetMessagesInCount": streamPerformGetMessagesInCount,
       "streamPerformGetMessagesInCountRate": streamPerformGetMessagesInCountRate,
       "streamPerformGetMessagesLossBytes": streamPerformGetMessagesLossBytes,
       "streamPerformGetMessagesLossCount": streamPerformGetMessagesLossCount,
       "streamPerformGetMessagesLossCountRate": streamPerformGetMessagesLossCountRate,
       "streamPerformGetMessagesOutBytes": streamPerformGetMessagesOutBytes,
       "streamPerformGetMessagesOutCount": streamPerformGetMessagesOutCount,
       "streamPerformGetMessagesOutCountRate": streamPerformGetMessagesOutCountRate,
       "rtmpclients": rtmpclients,
       "rtmpclientInfo": rtmpclientInfo,
       "rtmpClientCountTable": rtmpClientCountTable,
       "rtmpClientCountEntry": rtmpClientCountEntry,
       "rtmpClientCountCreationTime": rtmpClientCountCreationTime,
       "rtmpClientCountGetAcceptConnectionDescription": rtmpClientCountGetAcceptConnectionDescription,
       "rtmpClientCountGetBufferTime": rtmpClientCountGetBufferTime,
       "rtmpClientCountGetClientId": rtmpClientCountGetClientId,
       "rtmpClientCountGetConnectTime": rtmpClientCountGetConnectTime,
       "rtmpClientCountGetDateStarted": rtmpClientCountGetDateStarted,
       "rtmpClientCountGetDebugDumpData": rtmpClientCountGetDebugDumpData,
       "rtmpClientCountGetFlashVer": rtmpClientCountGetFlashVer,
       "rtmpClientCountGetHandshake": rtmpClientCountGetHandshake,
       "rtmpClientCountGetIdleFrequency": rtmpClientCountGetIdleFrequency,
       "rtmpClientCountGetIp": rtmpClientCountGetIp,
       "rtmpClientCountGetLastPingWriteId": rtmpClientCountGetLastPingWriteId,
       "rtmpClientCountGetLastReqChunkCounter": rtmpClientCountGetLastReqChunkCounter,
       "rtmpClientCountGetLastRequestType": rtmpClientCountGetLastRequestType,
       "rtmpClientCountGetLastStreamId": rtmpClientCountGetLastStreamId,
       "rtmpClientCountGetLastValidateTime": rtmpClientCountGetLastValidateTime,
       "rtmpClientCountGetLeftOverCID": rtmpClientCountGetLeftOverCID,
       "rtmpClientCountGetLeftOverMissing": rtmpClientCountGetLeftOverMissing,
       "rtmpClientCountGetLiveRepeaterCapabilities": rtmpClientCountGetLiveRepeaterCapabilities,
       "rtmpClientCountGetLiveStreamPacketizerList": rtmpClientCountGetLiveStreamPacketizerList,
       "rtmpClientCountGetLiveStreamTranscoderList": rtmpClientCountGetLiveStreamTranscoderList,
       "rtmpClientCountGetMaximumPendingReadBytes": rtmpClientCountGetMaximumPendingReadBytes,
       "rtmpClientCountGetMaximumPendingWriteBytes": rtmpClientCountGetMaximumPendingWriteBytes,
       "rtmpClientCountGetMaximumSetBufferTime": rtmpClientCountGetMaximumSetBufferTime,
       "rtmpClientCountGetNextConfirmBytesReceived": rtmpClientCountGetNextConfirmBytesReceived,
       "rtmpClientCountGetObjectEncoding": rtmpClientCountGetObjectEncoding,
       "rtmpClientCountGetPageUrl": rtmpClientCountGetPageUrl,
       "rtmpClientCountGetPingRoundTripTime": rtmpClientCountGetPingRoundTripTime,
       "rtmpClientCountGetPingTimeout": rtmpClientCountGetPingTimeout,
       "rtmpClientCountGetPlayResponse": rtmpClientCountGetPlayResponse,
       "rtmpClientCountGetPlayStreamCount": rtmpClientCountGetPlayStreamCount,
       "rtmpClientCountGetProtocol": rtmpClientCountGetProtocol,
       "rtmpClientCountGetPublishStreamCount": rtmpClientCountGetPublishStreamCount,
       "rtmpClientCountGetQueryStr": rtmpClientCountGetQueryStr,
       "rtmpClientCountGetReceiveChunkSize": rtmpClientCountGetReceiveChunkSize,
       "rtmpClientCountGetReferrer": rtmpClientCountGetReferrer,
       "rtmpClientCountGetRepeaterOriginUrl": rtmpClientCountGetRepeaterOriginUrl,
       "rtmpClientCountGetRequestDataSize": rtmpClientCountGetRequestDataSize,
       "rtmpClientCountGetRequestRTMPTSequence": rtmpClientCountGetRequestRTMPTSequence,
       "rtmpClientCountGetResponseIndex": rtmpClientCountGetResponseIndex,
       "rtmpClientCountGetSendChunkSize": rtmpClientCountGetSendChunkSize,
       "rtmpClientCountGetSharedObjectReadAccess": rtmpClientCountGetSharedObjectReadAccess,
       "rtmpClientCountGetSharedObjectWriteAccess": rtmpClientCountGetSharedObjectWriteAccess,
       "rtmpClientCountGetStreamAudioSampleAccess": rtmpClientCountGetStreamAudioSampleAccess,
       "rtmpClientCountGetStreamReadAccess": rtmpClientCountGetStreamReadAccess,
       "rtmpClientCountGetStreamType": rtmpClientCountGetStreamType,
       "rtmpClientCountGetStreamVideoSampleAccess": rtmpClientCountGetStreamVideoSampleAccess,
       "rtmpClientCountGetStreamWriteAccess": rtmpClientCountGetStreamWriteAccess,
       "rtmpClientCountGetTimeRunning": rtmpClientCountGetTimeRunning,
       "rtmpClientCountGetTimebase": rtmpClientCountGetTimebase,
       "rtmpClientCountGetTotalInBytes": rtmpClientCountGetTotalInBytes,
       "rtmpClientCountGetTouch": rtmpClientCountGetTouch,
       "rtmpClientCountGetUri": rtmpClientCountGetUri,
       "rtmpClientCountGetValidationFrequency": rtmpClientCountGetValidationFrequency,
       "rtmpClientPerformTable": rtmpClientPerformTable,
       "rtmpClientPerformEntry": rtmpClientPerformEntry,
       "rtmpClientPerformCreationTime": rtmpClientPerformCreationTime,
       "rtmpClientPerformGetFileInBytes": rtmpClientPerformGetFileInBytes,
       "rtmpClientPerformGetFileOutBytes": rtmpClientPerformGetFileOutBytes,
       "rtmpClientPerformGetMessagesInBytes": rtmpClientPerformGetMessagesInBytes,
       "rtmpClientPerformGetMessagesInCount": rtmpClientPerformGetMessagesInCount,
       "rtmpClientPerformGetMessagesInCountRate": rtmpClientPerformGetMessagesInCountRate,
       "rtmpClientPerformGetMessagesLossBytes": rtmpClientPerformGetMessagesLossBytes,
       "rtmpClientPerformGetMessagesLossCount": rtmpClientPerformGetMessagesLossCount,
       "rtmpClientPerformGetMessagesLossCountRate": rtmpClientPerformGetMessagesLossCountRate,
       "rtmpClientPerformGetMessagesOutBytes": rtmpClientPerformGetMessagesOutBytes,
       "rtmpClientPerformGetMessagesOutCount": rtmpClientPerformGetMessagesOutCount,
       "rtmpClientPerformGetMessagesOutCountRate": rtmpClientPerformGetMessagesOutCountRate,
       "httpclients": httpclients,
       "httpclientInfo": httpclientInfo,
       "httpClientCountTable": httpClientCountTable,
       "httpClientCountEntry": httpClientCountEntry,
       "httpClientCountCreationTime": httpClientCountCreationTime,
       "httpClientCountGetCookieStr": httpClientCountGetCookieStr,
       "httpClientCountGetHTTPDate": httpClientCountGetHTTPDate,
       "httpClientCountGetIpAddress": httpClientCountGetIpAddress,
       "httpClientCountGetIsFirstChunk": httpClientCountGetIsFirstChunk,
       "httpClientCountGetLastRequest": httpClientCountGetLastRequest,
       "httpClientCountGetLiveStreamingPacketizer": httpClientCountGetLiveStreamingPacketizer,
       "httpClientCountGetPlayDuration": httpClientCountGetPlayDuration,
       "httpClientCountGetPlaySeek": httpClientCountGetPlaySeek,
       "httpClientCountGetPlayStart": httpClientCountGetPlayStart,
       "httpClientCountGetQueryStr": httpClientCountGetQueryStr,
       "httpClientCountGetRedirectSessionCode": httpClientCountGetRedirectSessionCode,
       "httpClientCountGetRedirectSessionContentType": httpClientCountGetRedirectSessionContentType,
       "httpClientCountGetRedirectSessionURL": httpClientCountGetRedirectSessionURL,
       "httpClientCountGetReferrer": httpClientCountGetReferrer,
       "httpClientCountGetServerIp": httpClientCountGetServerIp,
       "httpClientCountGetServerPort": httpClientCountGetServerPort,
       "httpClientCountGetSessionId": httpClientCountGetSessionId,
       "httpClientCountGetSessionProtocol": httpClientCountGetSessionProtocol,
       "httpClientCountGetSessionTimeout": httpClientCountGetSessionTimeout,
       "httpClientCountGetSessionType": httpClientCountGetSessionType,
       "httpClientCountGetStreamExt": httpClientCountGetStreamExt,
       "httpClientCountGetStreamName": httpClientCountGetStreamName,
       "httpClientCountGetStreamPosition": httpClientCountGetStreamPosition,
       "httpClientCountGetTimeRunning": httpClientCountGetTimeRunning,
       "httpClientCountGetUri": httpClientCountGetUri,
       "httpClientCountGetUserAgent": httpClientCountGetUserAgent,
       "httpClientCountGetUserQueryStr": httpClientCountGetUserQueryStr,
       "httpClientCountGetVODTranscodeNGRP": httpClientCountGetVODTranscodeNGRP,
       "httpClientPerformTable": httpClientPerformTable,
       "httpClientPerformEntry": httpClientPerformEntry,
       "httpClientPerformCreationTime": httpClientPerformCreationTime,
       "httpClientPerformGetFileInBytes": httpClientPerformGetFileInBytes,
       "httpClientPerformGetFileOutBytes": httpClientPerformGetFileOutBytes,
       "httpClientPerformGetMessagesInBytes": httpClientPerformGetMessagesInBytes,
       "httpClientPerformGetMessagesInCount": httpClientPerformGetMessagesInCount,
       "httpClientPerformGetMessagesInCountRate": httpClientPerformGetMessagesInCountRate,
       "httpClientPerformGetMessagesLossBytes": httpClientPerformGetMessagesLossBytes,
       "httpClientPerformGetMessagesLossCount": httpClientPerformGetMessagesLossCount,
       "httpClientPerformGetMessagesLossCountRate": httpClientPerformGetMessagesLossCountRate,
       "httpClientPerformGetMessagesOutBytes": httpClientPerformGetMessagesOutBytes,
       "httpClientPerformGetMessagesOutCount": httpClientPerformGetMessagesOutCount,
       "httpClientPerformGetMessagesOutCountRate": httpClientPerformGetMessagesOutCountRate,
       "rtspclients": rtspclients,
       "rtspclientInfo": rtspclientInfo,
       "rtspClientCountTable": rtspClientCountTable,
       "rtspClientCountEntry": rtspClientCountEntry,
       "rtspClientCountCreationTime": rtspClientCountCreationTime,
       "rtspClientCountGetCookieStr": rtspClientCountGetCookieStr,
       "rtspClientCountGetIdleFrequency": rtspClientCountGetIdleFrequency,
       "rtspClientCountGetIp": rtspClientCountGetIp,
       "rtspClientCountGetLastAuthenticateMethod": rtspClientCountGetLastAuthenticateMethod,
       "rtspClientCountGetQueryStr": rtspClientCountGetQueryStr,
       "rtspClientCountGetRTSPTunnelingSessionId": rtspClientCountGetRTSPTunnelingSessionId,
       "rtspClientCountGetRedirectSessionCode": rtspClientCountGetRedirectSessionCode,
       "rtspClientCountGetRedirectSessionMessage": rtspClientCountGetRedirectSessionMessage,
       "rtspClientCountGetRedirectSessionURL": rtspClientCountGetRedirectSessionURL,
       "rtspClientCountGetReferrer": rtspClientCountGetReferrer,
       "rtspClientCountGetServerIp": rtspClientCountGetServerIp,
       "rtspClientCountGetServerPort": rtspClientCountGetServerPort,
       "rtspClientCountGetSessionId": rtspClientCountGetSessionId,
       "rtspClientCountGetTimeRunning": rtspClientCountGetTimeRunning,
       "rtspClientCountGetUri": rtspClientCountGetUri,
       "rtspClientCountGetUserAgent": rtspClientCountGetUserAgent,
       "rtspClientPerformTable": rtspClientPerformTable,
       "rtspClientPerformEntry": rtspClientPerformEntry,
       "rtspClientPerformCreationTime": rtspClientPerformCreationTime,
       "rtspClientPerformGetFileInBytes": rtspClientPerformGetFileInBytes,
       "rtspClientPerformGetFileOutBytes": rtspClientPerformGetFileOutBytes,
       "rtspClientPerformGetMessagesInBytes": rtspClientPerformGetMessagesInBytes,
       "rtspClientPerformGetMessagesInCount": rtspClientPerformGetMessagesInCount,
       "rtspClientPerformGetMessagesInCountRate": rtspClientPerformGetMessagesInCountRate,
       "rtspClientPerformGetMessagesLossBytes": rtspClientPerformGetMessagesLossBytes,
       "rtspClientPerformGetMessagesLossCount": rtspClientPerformGetMessagesLossCount,
       "rtspClientPerformGetMessagesLossCountRate": rtspClientPerformGetMessagesLossCountRate,
       "rtspClientPerformGetMessagesOutBytes": rtspClientPerformGetMessagesOutBytes,
       "rtspClientPerformGetMessagesOutCount": rtspClientPerformGetMessagesOutCount,
       "rtspClientPerformGetMessagesOutCountRate": rtspClientPerformGetMessagesOutCountRate}
)
