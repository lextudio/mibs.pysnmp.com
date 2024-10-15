# SNMP MIB module (INFORMANT-PERF-CITRIX) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INFORMANT-PERF-CITRIX
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:18 2024
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

citrixPerformance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41)
)
citrixPerformance.setRevisions(
        ("2008-06-13 22:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtxCPUUtilizationMgmtUserTable_Object = MibTable
ctxCPUUtilizationMgmtUserTable = _CtxCPUUtilizationMgmtUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 1)
)
if mibBuilder.loadTexts:
    ctxCPUUtilizationMgmtUserTable.setStatus("current")
_CtxCPUUtilizationMgmtUserEntry_Object = MibTableRow
ctxCPUUtilizationMgmtUserEntry = _CtxCPUUtilizationMgmtUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 1, 1)
)
ctxCPUUtilizationMgmtUserEntry.setIndexNames(
    (0, "INFORMANT-PERF-CITRIX", "ctxcumuInstance"),
)
if mibBuilder.loadTexts:
    ctxCPUUtilizationMgmtUserEntry.setStatus("current")
_CtxcumuInstance_Type = InstanceName
_CtxcumuInstance_Object = MibTableColumn
ctxcumuInstance = _CtxcumuInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 1, 1, 1),
    _CtxcumuInstance_Type()
)
ctxcumuInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxcumuInstance.setStatus("current")
_CtxcumuCPUEntitlement_Type = Gauge32
_CtxcumuCPUEntitlement_Object = MibTableColumn
ctxcumuCPUEntitlement = _CtxcumuCPUEntitlement_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 1, 1, 2),
    _CtxcumuCPUEntitlement_Type()
)
ctxcumuCPUEntitlement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxcumuCPUEntitlement.setStatus("current")
_CtxcumuCPUReservation_Type = Gauge32
_CtxcumuCPUReservation_Object = MibTableColumn
ctxcumuCPUReservation = _CtxcumuCPUReservation_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 1, 1, 3),
    _CtxcumuCPUReservation_Type()
)
ctxcumuCPUReservation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxcumuCPUReservation.setStatus("current")
_CtxcumuCPUShares_Type = Gauge32
_CtxcumuCPUShares_Object = MibTableColumn
ctxcumuCPUShares = _CtxcumuCPUShares_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 1, 1, 4),
    _CtxcumuCPUShares_Type()
)
ctxcumuCPUShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxcumuCPUShares.setStatus("current")
_CtxcumuCPUUsage_Type = Gauge32
_CtxcumuCPUUsage_Object = MibTableColumn
ctxcumuCPUUsage = _CtxcumuCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 1, 1, 5),
    _CtxcumuCPUUsage_Type()
)
ctxcumuCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxcumuCPUUsage.setStatus("current")
_CtxcumuLongTermCPUUsage_Type = Gauge32
_CtxcumuLongTermCPUUsage_Object = MibTableColumn
ctxcumuLongTermCPUUsage = _CtxcumuLongTermCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 1, 1, 6),
    _CtxcumuLongTermCPUUsage_Type()
)
ctxcumuLongTermCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxcumuLongTermCPUUsage.setStatus("current")
_CtxDataLayerTable_Object = MibTable
ctxDataLayerTable = _CtxDataLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2)
)
if mibBuilder.loadTexts:
    ctxDataLayerTable.setStatus("current")
_CtxDataLayerEntry_Object = MibTableRow
ctxDataLayerEntry = _CtxDataLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2, 1)
)
ctxDataLayerEntry.setIndexNames(
    (0, "INFORMANT-PERF-CITRIX", "ctxdlInstance"),
)
if mibBuilder.loadTexts:
    ctxDataLayerEntry.setStatus("current")
_CtxdlInstance_Type = InstanceName
_CtxdlInstance_Object = MibTableColumn
ctxdlInstance = _CtxdlInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2, 1, 1),
    _CtxdlInstance_Type()
)
ctxdlInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdlInstance.setStatus("current")
_CtxdlCommitsPerSec_Type = Gauge32
_CtxdlCommitsPerSec_Object = MibTableColumn
ctxdlCommitsPerSec = _CtxdlCommitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2, 1, 2),
    _CtxdlCommitsPerSec_Type()
)
ctxdlCommitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdlCommitsPerSec.setStatus("current")
_CtxdlContextsPerSec_Type = Gauge32
_CtxdlContextsPerSec_Object = MibTableColumn
ctxdlContextsPerSec = _CtxdlContextsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2, 1, 3),
    _CtxdlContextsPerSec_Type()
)
ctxdlContextsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdlContextsPerSec.setStatus("current")
_CtxdlDeletesPerSec_Type = Gauge32
_CtxdlDeletesPerSec_Object = MibTableColumn
ctxdlDeletesPerSec = _CtxdlDeletesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2, 1, 4),
    _CtxdlDeletesPerSec_Type()
)
ctxdlDeletesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdlDeletesPerSec.setStatus("current")
_CtxdlInsertsPerSec_Type = Gauge32
_CtxdlInsertsPerSec_Object = MibTableColumn
ctxdlInsertsPerSec = _CtxdlInsertsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2, 1, 5),
    _CtxdlInsertsPerSec_Type()
)
ctxdlInsertsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdlInsertsPerSec.setStatus("current")
_CtxdlNumberOfContextsInThePool_Type = Gauge32
_CtxdlNumberOfContextsInThePool_Object = MibTableColumn
ctxdlNumberOfContextsInThePool = _CtxdlNumberOfContextsInThePool_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2, 1, 6),
    _CtxdlNumberOfContextsInThePool_Type()
)
ctxdlNumberOfContextsInThePool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdlNumberOfContextsInThePool.setStatus("current")
_CtxdlNumOfCntxtRequestsWaiting_Type = Gauge32
_CtxdlNumOfCntxtRequestsWaiting_Object = MibTableColumn
ctxdlNumOfCntxtRequestsWaiting = _CtxdlNumOfCntxtRequestsWaiting_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2, 1, 7),
    _CtxdlNumOfCntxtRequestsWaiting_Type()
)
ctxdlNumOfCntxtRequestsWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdlNumOfCntxtRequestsWaiting.setStatus("current")
_CtxdlReadStreamsCreatedPerSec_Type = Gauge32
_CtxdlReadStreamsCreatedPerSec_Object = MibTableColumn
ctxdlReadStreamsCreatedPerSec = _CtxdlReadStreamsCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2, 1, 8),
    _CtxdlReadStreamsCreatedPerSec_Type()
)
ctxdlReadStreamsCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdlReadStreamsCreatedPerSec.setStatus("current")
_CtxdlStreamBytesReadPerSec_Type = Gauge32
_CtxdlStreamBytesReadPerSec_Object = MibTableColumn
ctxdlStreamBytesReadPerSec = _CtxdlStreamBytesReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2, 1, 9),
    _CtxdlStreamBytesReadPerSec_Type()
)
ctxdlStreamBytesReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdlStreamBytesReadPerSec.setStatus("current")
_CtxdlStreamBytesWrittenPerSec_Type = Gauge32
_CtxdlStreamBytesWrittenPerSec_Object = MibTableColumn
ctxdlStreamBytesWrittenPerSec = _CtxdlStreamBytesWrittenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2, 1, 10),
    _CtxdlStreamBytesWrittenPerSec_Type()
)
ctxdlStreamBytesWrittenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdlStreamBytesWrittenPerSec.setStatus("current")
_CtxdlStreamsCreatedPerSec_Type = Gauge32
_CtxdlStreamsCreatedPerSec_Object = MibTableColumn
ctxdlStreamsCreatedPerSec = _CtxdlStreamsCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2, 1, 11),
    _CtxdlStreamsCreatedPerSec_Type()
)
ctxdlStreamsCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdlStreamsCreatedPerSec.setStatus("current")
_CtxdlUpdatesPerSec_Type = Gauge32
_CtxdlUpdatesPerSec_Object = MibTableColumn
ctxdlUpdatesPerSec = _CtxdlUpdatesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2, 1, 12),
    _CtxdlUpdatesPerSec_Type()
)
ctxdlUpdatesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdlUpdatesPerSec.setStatus("current")
_CtxdlWriteStreamsCreatedPerSec_Type = Gauge32
_CtxdlWriteStreamsCreatedPerSec_Object = MibTableColumn
ctxdlWriteStreamsCreatedPerSec = _CtxdlWriteStreamsCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 2, 1, 13),
    _CtxdlWriteStreamsCreatedPerSec_Type()
)
ctxdlWriteStreamsCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdlWriteStreamsCreatedPerSec.setStatus("current")
_CtxIMANetworkingTable_Object = MibTable
ctxIMANetworkingTable = _CtxIMANetworkingTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 3)
)
if mibBuilder.loadTexts:
    ctxIMANetworkingTable.setStatus("current")
_CtxIMANetworkingEntry_Object = MibTableRow
ctxIMANetworkingEntry = _CtxIMANetworkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 3, 1)
)
ctxIMANetworkingEntry.setIndexNames(
    (0, "INFORMANT-PERF-CITRIX", "ctximanInstance"),
)
if mibBuilder.loadTexts:
    ctxIMANetworkingEntry.setStatus("current")
_CtximanInstance_Type = InstanceName
_CtximanInstance_Object = MibTableColumn
ctximanInstance = _CtximanInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 3, 1, 1),
    _CtximanInstance_Type()
)
ctximanInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctximanInstance.setStatus("current")
_CtximanBytesReceivedPerSec_Type = Gauge32
_CtximanBytesReceivedPerSec_Object = MibTableColumn
ctximanBytesReceivedPerSec = _CtximanBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 3, 1, 2),
    _CtximanBytesReceivedPerSec_Type()
)
ctximanBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctximanBytesReceivedPerSec.setStatus("current")
_CtximanBytesSentPerSec_Type = Gauge32
_CtximanBytesSentPerSec_Object = MibTableColumn
ctximanBytesSentPerSec = _CtximanBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 3, 1, 3),
    _CtximanBytesSentPerSec_Type()
)
ctximanBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctximanBytesSentPerSec.setStatus("current")
_CtximanNetworkConnections_Type = Gauge32
_CtximanNetworkConnections_Object = MibTableColumn
ctximanNetworkConnections = _CtximanNetworkConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 3, 1, 4),
    _CtximanNetworkConnections_Type()
)
ctximanNetworkConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctximanNetworkConnections.setStatus("current")
_CitrixLicensing_ObjectIdentity = ObjectIdentity
citrixLicensing = _CitrixLicensing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 4)
)
_CtxlAverageCheckInRspTimeMs_Type = Gauge32
_CtxlAverageCheckInRspTimeMs_Object = MibScalar
ctxlAverageCheckInRspTimeMs = _CtxlAverageCheckInRspTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 4, 1),
    _CtxlAverageCheckInRspTimeMs_Type()
)
ctxlAverageCheckInRspTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxlAverageCheckInRspTimeMs.setStatus("current")
_CtxlAverageCheckOutRspTimeMs_Type = Gauge32
_CtxlAverageCheckOutRspTimeMs_Object = MibScalar
ctxlAverageCheckOutRspTimeMs = _CtxlAverageCheckOutRspTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 4, 2),
    _CtxlAverageCheckOutRspTimeMs_Type()
)
ctxlAverageCheckOutRspTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxlAverageCheckOutRspTimeMs.setStatus("current")
_CtxlLastRecordCheckInRspTimeMs_Type = Gauge32
_CtxlLastRecordCheckInRspTimeMs_Object = MibScalar
ctxlLastRecordCheckInRspTimeMs = _CtxlLastRecordCheckInRspTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 4, 3),
    _CtxlLastRecordCheckInRspTimeMs_Type()
)
ctxlLastRecordCheckInRspTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxlLastRecordCheckInRspTimeMs.setStatus("current")
_CtxlLastRecordCheckOutRspTimeMs_Type = Gauge32
_CtxlLastRecordCheckOutRspTimeMs_Object = MibScalar
ctxlLastRecordCheckOutRspTimeMs = _CtxlLastRecordCheckOutRspTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 4, 4),
    _CtxlLastRecordCheckOutRspTimeMs_Type()
)
ctxlLastRecordCheckOutRspTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxlLastRecordCheckOutRspTimeMs.setStatus("current")
_CtxlServerConnectionFailure_Type = Gauge32
_CtxlServerConnectionFailure_Object = MibScalar
ctxlServerConnectionFailure = _CtxlServerConnectionFailure_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 4, 5),
    _CtxlServerConnectionFailure_Type()
)
ctxlServerConnectionFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxlServerConnectionFailure.setStatus("current")
_CtxlMaximumCheckInRspTimeMs_Type = Gauge32
_CtxlMaximumCheckInRspTimeMs_Object = MibScalar
ctxlMaximumCheckInRspTimeMs = _CtxlMaximumCheckInRspTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 4, 6),
    _CtxlMaximumCheckInRspTimeMs_Type()
)
ctxlMaximumCheckInRspTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxlMaximumCheckInRspTimeMs.setStatus("current")
_CtxlMaximumCheckOutRspTimeMs_Type = Gauge32
_CtxlMaximumCheckOutRspTimeMs_Object = MibScalar
ctxlMaximumCheckOutRspTimeMs = _CtxlMaximumCheckOutRspTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 4, 7),
    _CtxlMaximumCheckOutRspTimeMs_Type()
)
ctxlMaximumCheckOutRspTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxlMaximumCheckOutRspTimeMs.setStatus("current")
_CitrixMetaFramePresentationSvr_ObjectIdentity = ObjectIdentity
citrixMetaFramePresentationSvr = _CitrixMetaFramePresentationSvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5)
)
if mibBuilder.loadTexts:
    citrixMetaFramePresentationSvr.setStatus("current")
_CtxmpsApplEnumerationsPerSec_Type = Gauge32
_CtxmpsApplEnumerationsPerSec_Object = MibScalar
ctxmpsApplEnumerationsPerSec = _CtxmpsApplEnumerationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 1),
    _CtxmpsApplEnumerationsPerSec_Type()
)
ctxmpsApplEnumerationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsApplEnumerationsPerSec.setStatus("current")
_CtxmpsApplResolutionTimeMs_Type = Gauge32
_CtxmpsApplResolutionTimeMs_Object = MibScalar
ctxmpsApplResolutionTimeMs = _CtxmpsApplResolutionTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 2),
    _CtxmpsApplResolutionTimeMs_Type()
)
ctxmpsApplResolutionTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsApplResolutionTimeMs.setStatus("current")
_CtxmpsApplResolutionFailedPerSec_Type = Gauge32
_CtxmpsApplResolutionFailedPerSec_Object = MibScalar
ctxmpsApplResolutionFailedPerSec = _CtxmpsApplResolutionFailedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 3),
    _CtxmpsApplResolutionFailedPerSec_Type()
)
ctxmpsApplResolutionFailedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsApplResolutionFailedPerSec.setStatus("current")
_CtxmpsApplResolutionsPerSec_Type = Gauge32
_CtxmpsApplResolutionsPerSec_Object = MibScalar
ctxmpsApplResolutionsPerSec = _CtxmpsApplResolutionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 4),
    _CtxmpsApplResolutionsPerSec_Type()
)
ctxmpsApplResolutionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsApplResolutionsPerSec.setStatus("current")
_CtxmpsDataStoreConnectionFailure_Type = Gauge32
_CtxmpsDataStoreConnectionFailure_Object = MibScalar
ctxmpsDataStoreConnectionFailure = _CtxmpsDataStoreConnectionFailure_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 5),
    _CtxmpsDataStoreConnectionFailure_Type()
)
ctxmpsDataStoreConnectionFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDataStoreConnectionFailure.setStatus("current")
_CtxmpsDataStoreBytesRead_Type = Gauge32
_CtxmpsDataStoreBytesRead_Object = MibScalar
ctxmpsDataStoreBytesRead = _CtxmpsDataStoreBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 6),
    _CtxmpsDataStoreBytesRead_Type()
)
ctxmpsDataStoreBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDataStoreBytesRead.setStatus("current")
_CtxmpsDataStoreBytesReadPerSec_Type = Gauge32
_CtxmpsDataStoreBytesReadPerSec_Object = MibScalar
ctxmpsDataStoreBytesReadPerSec = _CtxmpsDataStoreBytesReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 7),
    _CtxmpsDataStoreBytesReadPerSec_Type()
)
ctxmpsDataStoreBytesReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDataStoreBytesReadPerSec.setStatus("current")
_CtxmpsDataStoreBytesWritePerSec_Type = Gauge32
_CtxmpsDataStoreBytesWritePerSec_Object = MibScalar
ctxmpsDataStoreBytesWritePerSec = _CtxmpsDataStoreBytesWritePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 8),
    _CtxmpsDataStoreBytesWritePerSec_Type()
)
ctxmpsDataStoreBytesWritePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDataStoreBytesWritePerSec.setStatus("current")
_CtxmpsDataStoreReads_Type = Gauge32
_CtxmpsDataStoreReads_Object = MibScalar
ctxmpsDataStoreReads = _CtxmpsDataStoreReads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 9),
    _CtxmpsDataStoreReads_Type()
)
ctxmpsDataStoreReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDataStoreReads.setStatus("current")
_CtxmpsDataStoreReadsPerSec_Type = Gauge32
_CtxmpsDataStoreReadsPerSec_Object = MibScalar
ctxmpsDataStoreReadsPerSec = _CtxmpsDataStoreReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 10),
    _CtxmpsDataStoreReadsPerSec_Type()
)
ctxmpsDataStoreReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDataStoreReadsPerSec.setStatus("current")
_CtxmpsDataStoreWritesPerSec_Type = Gauge32
_CtxmpsDataStoreWritesPerSec_Object = MibScalar
ctxmpsDataStoreWritesPerSec = _CtxmpsDataStoreWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 11),
    _CtxmpsDataStoreWritesPerSec_Type()
)
ctxmpsDataStoreWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDataStoreWritesPerSec.setStatus("current")
_CtxmpsDSGatewayUpdateCount_Type = Gauge32
_CtxmpsDSGatewayUpdateCount_Object = MibScalar
ctxmpsDSGatewayUpdateCount = _CtxmpsDSGatewayUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 12),
    _CtxmpsDSGatewayUpdateCount_Type()
)
ctxmpsDSGatewayUpdateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDSGatewayUpdateCount.setStatus("current")
_CtxmpsDSGatewayUpdateBytesSent_Type = Gauge32
_CtxmpsDSGatewayUpdateBytesSent_Object = MibScalar
ctxmpsDSGatewayUpdateBytesSent = _CtxmpsDSGatewayUpdateBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 13),
    _CtxmpsDSGatewayUpdateBytesSent_Type()
)
ctxmpsDSGatewayUpdateBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDSGatewayUpdateBytesSent.setStatus("current")
_CtxmpsDSQueryCount_Type = Gauge32
_CtxmpsDSQueryCount_Object = MibScalar
ctxmpsDSQueryCount = _CtxmpsDSQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 14),
    _CtxmpsDSQueryCount_Type()
)
ctxmpsDSQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDSQueryCount.setStatus("current")
_CtxmpsDSQueryRequestBytesReceive_Type = Gauge32
_CtxmpsDSQueryRequestBytesReceive_Object = MibScalar
ctxmpsDSQueryRequestBytesReceive = _CtxmpsDSQueryRequestBytesReceive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 15),
    _CtxmpsDSQueryRequestBytesReceive_Type()
)
ctxmpsDSQueryRequestBytesReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDSQueryRequestBytesReceive.setStatus("current")
_CtxmpsDSQueryResponseBytesSent_Type = Gauge32
_CtxmpsDSQueryResponseBytesSent_Object = MibScalar
ctxmpsDSQueryResponseBytesSent = _CtxmpsDSQueryResponseBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 16),
    _CtxmpsDSQueryResponseBytesSent_Type()
)
ctxmpsDSQueryResponseBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDSQueryResponseBytesSent.setStatus("current")
_CtxmpsDSUpdateBytesReceived_Type = Gauge32
_CtxmpsDSUpdateBytesReceived_Object = MibScalar
ctxmpsDSUpdateBytesReceived = _CtxmpsDSUpdateBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 17),
    _CtxmpsDSUpdateBytesReceived_Type()
)
ctxmpsDSUpdateBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDSUpdateBytesReceived.setStatus("current")
_CtxmpsDSUpdatePacketsReceived_Type = Gauge32
_CtxmpsDSUpdatePacketsReceived_Object = MibScalar
ctxmpsDSUpdatePacketsReceived = _CtxmpsDSUpdatePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 18),
    _CtxmpsDSUpdatePacketsReceived_Type()
)
ctxmpsDSUpdatePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDSUpdatePacketsReceived.setStatus("current")
_CtxmpsDSUpdateResponseBytesSent_Type = Gauge32
_CtxmpsDSUpdateResponseBytesSent_Object = MibScalar
ctxmpsDSUpdateResponseBytesSent = _CtxmpsDSUpdateResponseBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 19),
    _CtxmpsDSUpdateResponseBytesSent_Type()
)
ctxmpsDSUpdateResponseBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDSUpdateResponseBytesSent.setStatus("current")
_CtxmpsDSBytesReadPerSec_Type = Gauge32
_CtxmpsDSBytesReadPerSec_Object = MibScalar
ctxmpsDSBytesReadPerSec = _CtxmpsDSBytesReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 20),
    _CtxmpsDSBytesReadPerSec_Type()
)
ctxmpsDSBytesReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDSBytesReadPerSec.setStatus("current")
_CtxmpsDSBytesWrittenPerSec_Type = Gauge32
_CtxmpsDSBytesWrittenPerSec_Object = MibScalar
ctxmpsDSBytesWrittenPerSec = _CtxmpsDSBytesWrittenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 21),
    _CtxmpsDSBytesWrittenPerSec_Type()
)
ctxmpsDSBytesWrittenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDSBytesWrittenPerSec.setStatus("current")
_CtxmpsDSReadsPerSec_Type = Gauge32
_CtxmpsDSReadsPerSec_Object = MibScalar
ctxmpsDSReadsPerSec = _CtxmpsDSReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 22),
    _CtxmpsDSReadsPerSec_Type()
)
ctxmpsDSReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDSReadsPerSec.setStatus("current")
_CtxmpsDSWritesPerSec_Type = Gauge32
_CtxmpsDSWritesPerSec_Object = MibScalar
ctxmpsDSWritesPerSec = _CtxmpsDSWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 23),
    _CtxmpsDSWritesPerSec_Type()
)
ctxmpsDSWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsDSWritesPerSec.setStatus("current")
_CtxmpsFilteredApplEnumsPerSec_Type = Gauge32
_CtxmpsFilteredApplEnumsPerSec_Object = MibScalar
ctxmpsFilteredApplEnumsPerSec = _CtxmpsFilteredApplEnumsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 24),
    _CtxmpsFilteredApplEnumsPerSec_Type()
)
ctxmpsFilteredApplEnumsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsFilteredApplEnumsPerSec.setStatus("current")
_CtxmpsLCCacheBytesReadPerSec_Type = Gauge32
_CtxmpsLCCacheBytesReadPerSec_Object = MibScalar
ctxmpsLCCacheBytesReadPerSec = _CtxmpsLCCacheBytesReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 25),
    _CtxmpsLCCacheBytesReadPerSec_Type()
)
ctxmpsLCCacheBytesReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsLCCacheBytesReadPerSec.setStatus("current")
_CtxmpsLCCacheBytesWrittenPerSec_Type = Gauge32
_CtxmpsLCCacheBytesWrittenPerSec_Object = MibScalar
ctxmpsLCCacheBytesWrittenPerSec = _CtxmpsLCCacheBytesWrittenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 26),
    _CtxmpsLCCacheBytesWrittenPerSec_Type()
)
ctxmpsLCCacheBytesWrittenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsLCCacheBytesWrittenPerSec.setStatus("current")
_CtxmpsLCCacheReadsPerSec_Type = Gauge32
_CtxmpsLCCacheReadsPerSec_Object = MibScalar
ctxmpsLCCacheReadsPerSec = _CtxmpsLCCacheReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 27),
    _CtxmpsLCCacheReadsPerSec_Type()
)
ctxmpsLCCacheReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsLCCacheReadsPerSec.setStatus("current")
_CtxmpsLCCacheWritesPerSec_Type = Gauge32
_CtxmpsLCCacheWritesPerSec_Object = MibScalar
ctxmpsLCCacheWritesPerSec = _CtxmpsLCCacheWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 28),
    _CtxmpsLCCacheWritesPerSec_Type()
)
ctxmpsLCCacheWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsLCCacheWritesPerSec.setStatus("current")
_CtxmpsMaximumNumberOfXMLThreads_Type = Gauge32
_CtxmpsMaximumNumberOfXMLThreads_Object = MibScalar
ctxmpsMaximumNumberOfXMLThreads = _CtxmpsMaximumNumberOfXMLThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 29),
    _CtxmpsMaximumNumberOfXMLThreads_Type()
)
ctxmpsMaximumNumberOfXMLThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsMaximumNumberOfXMLThreads.setStatus("current")
_CtxmpsNumberOfXMLThreads_Type = Gauge32
_CtxmpsNumberOfXMLThreads_Object = MibScalar
ctxmpsNumberOfXMLThreads = _CtxmpsNumberOfXMLThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 30),
    _CtxmpsNumberOfXMLThreads_Type()
)
ctxmpsNumberOfXMLThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsNumberOfXMLThreads.setStatus("current")
_CtxmpsNumberOfBusyXMLThreads_Type = Gauge32
_CtxmpsNumberOfBusyXMLThreads_Object = MibScalar
ctxmpsNumberOfBusyXMLThreads = _CtxmpsNumberOfBusyXMLThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 31),
    _CtxmpsNumberOfBusyXMLThreads_Type()
)
ctxmpsNumberOfBusyXMLThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsNumberOfBusyXMLThreads.setStatus("current")
_CtxmpsResWorkItemQueueExecuteCnt_Type = Gauge32
_CtxmpsResWorkItemQueueExecuteCnt_Object = MibScalar
ctxmpsResWorkItemQueueExecuteCnt = _CtxmpsResWorkItemQueueExecuteCnt_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 32),
    _CtxmpsResWorkItemQueueExecuteCnt_Type()
)
ctxmpsResWorkItemQueueExecuteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsResWorkItemQueueExecuteCnt.setStatus("current")
_CtxmpsResWorkItemQueueReadyCount_Type = Gauge32
_CtxmpsResWorkItemQueueReadyCount_Object = MibScalar
ctxmpsResWorkItemQueueReadyCount = _CtxmpsResWorkItemQueueReadyCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 33),
    _CtxmpsResWorkItemQueueReadyCount_Type()
)
ctxmpsResWorkItemQueueReadyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsResWorkItemQueueReadyCount.setStatus("current")
_CtxmpsWorkItemQueueExecuteCount_Type = Gauge32
_CtxmpsWorkItemQueueExecuteCount_Object = MibScalar
ctxmpsWorkItemQueueExecuteCount = _CtxmpsWorkItemQueueExecuteCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 34),
    _CtxmpsWorkItemQueueExecuteCount_Type()
)
ctxmpsWorkItemQueueExecuteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsWorkItemQueueExecuteCount.setStatus("current")
_CtxmpsWorkItemQueuePendingCount_Type = Gauge32
_CtxmpsWorkItemQueuePendingCount_Object = MibScalar
ctxmpsWorkItemQueuePendingCount = _CtxmpsWorkItemQueuePendingCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 35),
    _CtxmpsWorkItemQueuePendingCount_Type()
)
ctxmpsWorkItemQueuePendingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsWorkItemQueuePendingCount.setStatus("current")
_CtxmpsWorkItemQueueReadyCount_Type = Gauge32
_CtxmpsWorkItemQueueReadyCount_Object = MibScalar
ctxmpsWorkItemQueueReadyCount = _CtxmpsWorkItemQueueReadyCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 36),
    _CtxmpsWorkItemQueueReadyCount_Type()
)
ctxmpsWorkItemQueueReadyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsWorkItemQueueReadyCount.setStatus("current")
_CtxmpsZoneElections_Type = Gauge32
_CtxmpsZoneElections_Object = MibScalar
ctxmpsZoneElections = _CtxmpsZoneElections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 37),
    _CtxmpsZoneElections_Type()
)
ctxmpsZoneElections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsZoneElections.setStatus("current")
_CtxmpsZoneElectionsWon_Type = Gauge32
_CtxmpsZoneElectionsWon_Object = MibScalar
ctxmpsZoneElectionsWon = _CtxmpsZoneElectionsWon_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 5, 38),
    _CtxmpsZoneElectionsWon_Type()
)
ctxmpsZoneElectionsWon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxmpsZoneElectionsWon.setStatus("current")
_CtxSmartAuditorAgent_ObjectIdentity = ObjectIdentity
ctxSmartAuditorAgent = _CtxSmartAuditorAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 6)
)
_CtxsaaActiveRecordingCount_Type = Gauge32
_CtxsaaActiveRecordingCount_Object = MibScalar
ctxsaaActiveRecordingCount = _CtxsaaActiveRecordingCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 6, 1),
    _CtxsaaActiveRecordingCount_Type()
)
ctxsaaActiveRecordingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxsaaActiveRecordingCount.setStatus("current")
_CtxsaaReadSmartAuditorDriverSec_Type = Gauge32
_CtxsaaReadSmartAuditorDriverSec_Object = MibScalar
ctxsaaReadSmartAuditorDriverSec = _CtxsaaReadSmartAuditorDriverSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 6, 2),
    _CtxsaaReadSmartAuditorDriverSec_Type()
)
ctxsaaReadSmartAuditorDriverSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxsaaReadSmartAuditorDriverSec.setStatus("current")
_CtxSmartAuditorStorageManager_ObjectIdentity = ObjectIdentity
ctxSmartAuditorStorageManager = _CtxSmartAuditorStorageManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 7)
)
_CtxsasmActiveRecordingCount_Type = Gauge32
_CtxsasmActiveRecordingCount_Object = MibScalar
ctxsasmActiveRecordingCount = _CtxsasmActiveRecordingCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 7, 1),
    _CtxsasmActiveRecordingCount_Type()
)
ctxsasmActiveRecordingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxsasmActiveRecordingCount.setStatus("current")
_CtxsasmMessageBytesPerSec_Type = Gauge32
_CtxsasmMessageBytesPerSec_Object = MibScalar
ctxsasmMessageBytesPerSec = _CtxsasmMessageBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 7, 2),
    _CtxsasmMessageBytesPerSec_Type()
)
ctxsasmMessageBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxsasmMessageBytesPerSec.setStatus("current")
_CtxsasmMessagesPerSec_Type = Gauge32
_CtxsasmMessagesPerSec_Object = MibScalar
ctxsasmMessagesPerSec = _CtxsasmMessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 7, 3),
    _CtxsasmMessagesPerSec_Type()
)
ctxsasmMessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxsasmMessagesPerSec.setStatus("current")
_CtxDesktopBrokerDatabaseService_ObjectIdentity = ObjectIdentity
ctxDesktopBrokerDatabaseService = _CtxDesktopBrokerDatabaseService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 8)
)
_CtxdbdsHostedDesktopReleasesSec_Type = Gauge32
_CtxdbdsHostedDesktopReleasesSec_Object = MibScalar
ctxdbdsHostedDesktopReleasesSec = _CtxdbdsHostedDesktopReleasesSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 8, 1),
    _CtxdbdsHostedDesktopReleasesSec_Type()
)
ctxdbdsHostedDesktopReleasesSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdbdsHostedDesktopReleasesSec.setStatus("current")
_CtxdbdsHostedDesktopRequestsSec_Type = Gauge32
_CtxdbdsHostedDesktopRequestsSec_Object = MibScalar
ctxdbdsHostedDesktopRequestsSec = _CtxdbdsHostedDesktopRequestsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 8, 2),
    _CtxdbdsHostedDesktopRequestsSec_Type()
)
ctxdbdsHostedDesktopRequestsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdbdsHostedDesktopRequestsSec.setStatus("current")
_CtxdbdsHostedDesktopStateUpdSec_Type = Gauge32
_CtxdbdsHostedDesktopStateUpdSec_Object = MibScalar
ctxdbdsHostedDesktopStateUpdSec = _CtxdbdsHostedDesktopStateUpdSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 8, 3),
    _CtxdbdsHostedDesktopStateUpdSec_Type()
)
ctxdbdsHostedDesktopStateUpdSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxdbdsHostedDesktopStateUpdSec.setStatus("current")
_CtxICASessionTable_Object = MibTable
ctxICASessionTable = _CtxICASessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9)
)
if mibBuilder.loadTexts:
    ctxICASessionTable.setStatus("current")
_CtxICASessionEntry_Object = MibTableRow
ctxICASessionEntry = _CtxICASessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1)
)
ctxICASessionEntry.setIndexNames(
    (0, "INFORMANT-PERF-CITRIX", "ctxisInstance"),
)
if mibBuilder.loadTexts:
    ctxICASessionEntry.setStatus("current")
_CtxisInstance_Type = InstanceName
_CtxisInstance_Object = MibTableColumn
ctxisInstance = _CtxisInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 1),
    _CtxisInstance_Type()
)
ctxisInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInstance.setStatus("current")
_CtxisInputAudioBandwidth_Type = Gauge32
_CtxisInputAudioBandwidth_Object = MibTableColumn
ctxisInputAudioBandwidth = _CtxisInputAudioBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 2),
    _CtxisInputAudioBandwidth_Type()
)
ctxisInputAudioBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputAudioBandwidth.setStatus("current")
_CtxisInputCOM1Bandwidth_Type = Gauge32
_CtxisInputCOM1Bandwidth_Object = MibTableColumn
ctxisInputCOM1Bandwidth = _CtxisInputCOM1Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 3),
    _CtxisInputCOM1Bandwidth_Type()
)
ctxisInputCOM1Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputCOM1Bandwidth.setStatus("current")
_CtxisInputCOM2Bandwidth_Type = Gauge32
_CtxisInputCOM2Bandwidth_Object = MibTableColumn
ctxisInputCOM2Bandwidth = _CtxisInputCOM2Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 4),
    _CtxisInputCOM2Bandwidth_Type()
)
ctxisInputCOM2Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputCOM2Bandwidth.setStatus("current")
_CtxisInputCOMBandwidth_Type = Gauge32
_CtxisInputCOMBandwidth_Object = MibTableColumn
ctxisInputCOMBandwidth = _CtxisInputCOMBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 5),
    _CtxisInputCOMBandwidth_Type()
)
ctxisInputCOMBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputCOMBandwidth.setStatus("current")
_CtxisInputClipboardBandwidt_Type = Gauge32
_CtxisInputClipboardBandwidt_Object = MibTableColumn
ctxisInputClipboardBandwidt = _CtxisInputClipboardBandwidt_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 6),
    _CtxisInputClipboardBandwidt_Type()
)
ctxisInputClipboardBandwidt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputClipboardBandwidt.setStatus("current")
_CtxisInputControlChanBandwidth_Type = Gauge32
_CtxisInputControlChanBandwidth_Object = MibTableColumn
ctxisInputControlChanBandwidth = _CtxisInputControlChanBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 7),
    _CtxisInputControlChanBandwidth_Type()
)
ctxisInputControlChanBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputControlChanBandwidth.setStatus("current")
_CtxisInputDriveBandwidth_Type = Gauge32
_CtxisInputDriveBandwidth_Object = MibTableColumn
ctxisInputDriveBandwidth = _CtxisInputDriveBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 8),
    _CtxisInputDriveBandwidth_Type()
)
ctxisInputDriveBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputDriveBandwidth.setStatus("current")
_CtxisInputFontDataBandwidth_Type = Gauge32
_CtxisInputFontDataBandwidth_Object = MibTableColumn
ctxisInputFontDataBandwidth = _CtxisInputFontDataBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 9),
    _CtxisInputFontDataBandwidth_Type()
)
ctxisInputFontDataBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputFontDataBandwidth.setStatus("current")
_CtxisInputLPT1Bandwidth_Type = Gauge32
_CtxisInputLPT1Bandwidth_Object = MibTableColumn
ctxisInputLPT1Bandwidth = _CtxisInputLPT1Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 10),
    _CtxisInputLPT1Bandwidth_Type()
)
ctxisInputLPT1Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputLPT1Bandwidth.setStatus("current")
_CtxisInputLPT2Bandwidth_Type = Gauge32
_CtxisInputLPT2Bandwidth_Object = MibTableColumn
ctxisInputLPT2Bandwidth = _CtxisInputLPT2Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 11),
    _CtxisInputLPT2Bandwidth_Type()
)
ctxisInputLPT2Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputLPT2Bandwidth.setStatus("current")
_CtxisInputLicensingBandwidth_Type = Gauge32
_CtxisInputLicensingBandwidth_Object = MibTableColumn
ctxisInputLicensingBandwidth = _CtxisInputLicensingBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 12),
    _CtxisInputLicensingBandwidth_Type()
)
ctxisInputLicensingBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputLicensingBandwidth.setStatus("current")
_CtxisInputManagementBandwidth_Type = Gauge32
_CtxisInputManagementBandwidth_Object = MibTableColumn
ctxisInputManagementBandwidth = _CtxisInputManagementBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 13),
    _CtxisInputManagementBandwidth_Type()
)
ctxisInputManagementBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputManagementBandwidth.setStatus("current")
_CtxisInputPNBandwidth_Type = Gauge32
_CtxisInputPNBandwidth_Object = MibTableColumn
ctxisInputPNBandwidth = _CtxisInputPNBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 14),
    _CtxisInputPNBandwidth_Type()
)
ctxisInputPNBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputPNBandwidth.setStatus("current")
_CtxisInputPrinterBandwidth_Type = Gauge32
_CtxisInputPrinterBandwidth_Object = MibTableColumn
ctxisInputPrinterBandwidth = _CtxisInputPrinterBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 15),
    _CtxisInputPrinterBandwidth_Type()
)
ctxisInputPrinterBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputPrinterBandwidth.setStatus("current")
_CtxisInputSeamlessBandwidth_Type = Gauge32
_CtxisInputSeamlessBandwidth_Object = MibTableColumn
ctxisInputSeamlessBandwidth = _CtxisInputSeamlessBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 16),
    _CtxisInputSeamlessBandwidth_Type()
)
ctxisInputSeamlessBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputSeamlessBandwidth.setStatus("current")
_CtxisInputSessionBandwidth_Type = Gauge32
_CtxisInputSessionBandwidth_Object = MibTableColumn
ctxisInputSessionBandwidth = _CtxisInputSessionBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 17),
    _CtxisInputSessionBandwidth_Type()
)
ctxisInputSessionBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputSessionBandwidth.setStatus("current")
_CtxisInputSessionCompression_Type = Gauge32
_CtxisInputSessionCompression_Object = MibTableColumn
ctxisInputSessionCompression = _CtxisInputSessionCompression_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 18),
    _CtxisInputSessionCompression_Type()
)
ctxisInputSessionCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputSessionCompression.setStatus("current")
_CtxisInputSessionLineSpeed_Type = Gauge32
_CtxisInputSessionLineSpeed_Object = MibTableColumn
ctxisInputSessionLineSpeed = _CtxisInputSessionLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 19),
    _CtxisInputSessionLineSpeed_Type()
)
ctxisInputSessionLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputSessionLineSpeed.setStatus("current")
_CtxisInputSpeedScreenDataChanBW_Type = Gauge32
_CtxisInputSpeedScreenDataChanBW_Object = MibTableColumn
ctxisInputSpeedScreenDataChanBW = _CtxisInputSpeedScreenDataChanBW_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 20),
    _CtxisInputSpeedScreenDataChanBW_Type()
)
ctxisInputSpeedScreenDataChanBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputSpeedScreenDataChanBW.setStatus("current")
_CtxisInputTextEchoBandwidth_Type = Gauge32
_CtxisInputTextEchoBandwidth_Object = MibTableColumn
ctxisInputTextEchoBandwidth = _CtxisInputTextEchoBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 21),
    _CtxisInputTextEchoBandwidth_Type()
)
ctxisInputTextEchoBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputTextEchoBandwidth.setStatus("current")
_CtxisInputThinWireBandwidth_Type = Gauge32
_CtxisInputThinWireBandwidth_Object = MibTableColumn
ctxisInputThinWireBandwidth = _CtxisInputThinWireBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 22),
    _CtxisInputThinWireBandwidth_Type()
)
ctxisInputThinWireBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputThinWireBandwidth.setStatus("current")
_CtxisInputVideoFrameBandwidth_Type = Gauge32
_CtxisInputVideoFrameBandwidth_Object = MibTableColumn
ctxisInputVideoFrameBandwidth = _CtxisInputVideoFrameBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 23),
    _CtxisInputVideoFrameBandwidth_Type()
)
ctxisInputVideoFrameBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisInputVideoFrameBandwidth.setStatus("current")
_CtxisLatencyLastRecorded_Type = Gauge32
_CtxisLatencyLastRecorded_Object = MibTableColumn
ctxisLatencyLastRecorded = _CtxisLatencyLastRecorded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 24),
    _CtxisLatencyLastRecorded_Type()
)
ctxisLatencyLastRecorded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisLatencyLastRecorded.setStatus("current")
_CtxisLatencySessionAverage_Type = Gauge32
_CtxisLatencySessionAverage_Object = MibTableColumn
ctxisLatencySessionAverage = _CtxisLatencySessionAverage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 25),
    _CtxisLatencySessionAverage_Type()
)
ctxisLatencySessionAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisLatencySessionAverage.setStatus("current")
_CtxisLatencySessionDeviation_Type = Gauge32
_CtxisLatencySessionDeviation_Object = MibTableColumn
ctxisLatencySessionDeviation = _CtxisLatencySessionDeviation_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 26),
    _CtxisLatencySessionDeviation_Type()
)
ctxisLatencySessionDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisLatencySessionDeviation.setStatus("current")
_CtxisOutputAudioBandwidth_Type = Gauge32
_CtxisOutputAudioBandwidth_Object = MibTableColumn
ctxisOutputAudioBandwidth = _CtxisOutputAudioBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 27),
    _CtxisOutputAudioBandwidth_Type()
)
ctxisOutputAudioBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputAudioBandwidth.setStatus("current")
_CtxisOutputCOM1Bandwidth_Type = Gauge32
_CtxisOutputCOM1Bandwidth_Object = MibTableColumn
ctxisOutputCOM1Bandwidth = _CtxisOutputCOM1Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 28),
    _CtxisOutputCOM1Bandwidth_Type()
)
ctxisOutputCOM1Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputCOM1Bandwidth.setStatus("current")
_CtxisOutputCOM2Bandwidth_Type = Gauge32
_CtxisOutputCOM2Bandwidth_Object = MibTableColumn
ctxisOutputCOM2Bandwidth = _CtxisOutputCOM2Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 29),
    _CtxisOutputCOM2Bandwidth_Type()
)
ctxisOutputCOM2Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputCOM2Bandwidth.setStatus("current")
_CtxisOutputCOMBandwidth_Type = Gauge32
_CtxisOutputCOMBandwidth_Object = MibTableColumn
ctxisOutputCOMBandwidth = _CtxisOutputCOMBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 30),
    _CtxisOutputCOMBandwidth_Type()
)
ctxisOutputCOMBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputCOMBandwidth.setStatus("current")
_CtxisOutputClipboardBandwidth_Type = Gauge32
_CtxisOutputClipboardBandwidth_Object = MibTableColumn
ctxisOutputClipboardBandwidth = _CtxisOutputClipboardBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 31),
    _CtxisOutputClipboardBandwidth_Type()
)
ctxisOutputClipboardBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputClipboardBandwidth.setStatus("current")
_CtxisOutputControlChannBandwidth_Type = Gauge32
_CtxisOutputControlChannBandwidth_Object = MibTableColumn
ctxisOutputControlChannBandwidth = _CtxisOutputControlChannBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 32),
    _CtxisOutputControlChannBandwidth_Type()
)
ctxisOutputControlChannBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputControlChannBandwidth.setStatus("current")
_CtxisOutputDriveBandwidth_Type = Gauge32
_CtxisOutputDriveBandwidth_Object = MibTableColumn
ctxisOutputDriveBandwidth = _CtxisOutputDriveBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 33),
    _CtxisOutputDriveBandwidth_Type()
)
ctxisOutputDriveBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputDriveBandwidth.setStatus("current")
_CtxisOutputFontDataBandwidth_Type = Gauge32
_CtxisOutputFontDataBandwidth_Object = MibTableColumn
ctxisOutputFontDataBandwidth = _CtxisOutputFontDataBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 34),
    _CtxisOutputFontDataBandwidth_Type()
)
ctxisOutputFontDataBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputFontDataBandwidth.setStatus("current")
_CtxisOutputLPT1Bandwidth_Type = Gauge32
_CtxisOutputLPT1Bandwidth_Object = MibTableColumn
ctxisOutputLPT1Bandwidth = _CtxisOutputLPT1Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 35),
    _CtxisOutputLPT1Bandwidth_Type()
)
ctxisOutputLPT1Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputLPT1Bandwidth.setStatus("current")
_CtxisOutputLPT2Bandwidth_Type = Gauge32
_CtxisOutputLPT2Bandwidth_Object = MibTableColumn
ctxisOutputLPT2Bandwidth = _CtxisOutputLPT2Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 36),
    _CtxisOutputLPT2Bandwidth_Type()
)
ctxisOutputLPT2Bandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputLPT2Bandwidth.setStatus("current")
_CtxisOutputLicensingBandwidth_Type = Gauge32
_CtxisOutputLicensingBandwidth_Object = MibTableColumn
ctxisOutputLicensingBandwidth = _CtxisOutputLicensingBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 37),
    _CtxisOutputLicensingBandwidth_Type()
)
ctxisOutputLicensingBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputLicensingBandwidth.setStatus("current")
_CtxisOutputManagementBandwidth_Type = Gauge32
_CtxisOutputManagementBandwidth_Object = MibTableColumn
ctxisOutputManagementBandwidth = _CtxisOutputManagementBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 38),
    _CtxisOutputManagementBandwidth_Type()
)
ctxisOutputManagementBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputManagementBandwidth.setStatus("current")
_CtxisOutputPNBandwidth_Type = Gauge32
_CtxisOutputPNBandwidth_Object = MibTableColumn
ctxisOutputPNBandwidth = _CtxisOutputPNBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 39),
    _CtxisOutputPNBandwidth_Type()
)
ctxisOutputPNBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputPNBandwidth.setStatus("current")
_CtxisOutputPrinterBandwidth_Type = Gauge32
_CtxisOutputPrinterBandwidth_Object = MibTableColumn
ctxisOutputPrinterBandwidth = _CtxisOutputPrinterBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 40),
    _CtxisOutputPrinterBandwidth_Type()
)
ctxisOutputPrinterBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputPrinterBandwidth.setStatus("current")
_CtxisOutputSeamlessBandwidth_Type = Gauge32
_CtxisOutputSeamlessBandwidth_Object = MibTableColumn
ctxisOutputSeamlessBandwidth = _CtxisOutputSeamlessBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 41),
    _CtxisOutputSeamlessBandwidth_Type()
)
ctxisOutputSeamlessBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputSeamlessBandwidth.setStatus("current")
_CtxisOutputSessionBandwidth_Type = Gauge32
_CtxisOutputSessionBandwidth_Object = MibTableColumn
ctxisOutputSessionBandwidth = _CtxisOutputSessionBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 42),
    _CtxisOutputSessionBandwidth_Type()
)
ctxisOutputSessionBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputSessionBandwidth.setStatus("current")
_CtxisOutputSessionCompression_Type = Gauge32
_CtxisOutputSessionCompression_Object = MibTableColumn
ctxisOutputSessionCompression = _CtxisOutputSessionCompression_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 43),
    _CtxisOutputSessionCompression_Type()
)
ctxisOutputSessionCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputSessionCompression.setStatus("current")
_CtxisOutputSessionLineSpeed_Type = Gauge32
_CtxisOutputSessionLineSpeed_Object = MibTableColumn
ctxisOutputSessionLineSpeed = _CtxisOutputSessionLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 44),
    _CtxisOutputSessionLineSpeed_Type()
)
ctxisOutputSessionLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputSessionLineSpeed.setStatus("current")
_CtxisOutputSpeedScreenDataChanBW_Type = Gauge32
_CtxisOutputSpeedScreenDataChanBW_Object = MibTableColumn
ctxisOutputSpeedScreenDataChanBW = _CtxisOutputSpeedScreenDataChanBW_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 45),
    _CtxisOutputSpeedScreenDataChanBW_Type()
)
ctxisOutputSpeedScreenDataChanBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputSpeedScreenDataChanBW.setStatus("current")
_CtxisOutputTextEchoBandwidth_Type = Gauge32
_CtxisOutputTextEchoBandwidth_Object = MibTableColumn
ctxisOutputTextEchoBandwidth = _CtxisOutputTextEchoBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 46),
    _CtxisOutputTextEchoBandwidth_Type()
)
ctxisOutputTextEchoBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputTextEchoBandwidth.setStatus("current")
_CtxisOutputThinWireBandwidth_Type = Gauge32
_CtxisOutputThinWireBandwidth_Object = MibTableColumn
ctxisOutputThinWireBandwidth = _CtxisOutputThinWireBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 47),
    _CtxisOutputThinWireBandwidth_Type()
)
ctxisOutputThinWireBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputThinWireBandwidth.setStatus("current")
_CtxisOutputVideoFrameBandwidth_Type = Gauge32
_CtxisOutputVideoFrameBandwidth_Object = MibTableColumn
ctxisOutputVideoFrameBandwidth = _CtxisOutputVideoFrameBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 9, 1, 48),
    _CtxisOutputVideoFrameBandwidth_Type()
)
ctxisOutputVideoFrameBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxisOutputVideoFrameBandwidth.setStatus("current")
_CtxSecureTicketAuthority_ObjectIdentity = ObjectIdentity
ctxSecureTicketAuthority = _CtxSecureTicketAuthority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 10)
)
if mibBuilder.loadTexts:
    ctxSecureTicketAuthority.setStatus("current")
_CtxstaSTABadDataRequestCount_Type = Gauge32
_CtxstaSTABadDataRequestCount_Object = MibScalar
ctxstaSTABadDataRequestCount = _CtxstaSTABadDataRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 10, 1),
    _CtxstaSTABadDataRequestCount_Type()
)
ctxstaSTABadDataRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxstaSTABadDataRequestCount.setStatus("current")
_CtxstaSTABadRefreshRequestCount_Type = Gauge32
_CtxstaSTABadRefreshRequestCount_Object = MibScalar
ctxstaSTABadRefreshRequestCount = _CtxstaSTABadRefreshRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 10, 2),
    _CtxstaSTABadRefreshRequestCount_Type()
)
ctxstaSTABadRefreshRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxstaSTABadRefreshRequestCount.setStatus("current")
_CtxstaSTABadTicketRequestCount_Type = Gauge32
_CtxstaSTABadTicketRequestCount_Object = MibScalar
ctxstaSTABadTicketRequestCount = _CtxstaSTABadTicketRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 10, 3),
    _CtxstaSTABadTicketRequestCount_Type()
)
ctxstaSTABadTicketRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxstaSTABadTicketRequestCount.setStatus("current")
_CtxstaSTACountOfActiveTickets_Type = Gauge32
_CtxstaSTACountOfActiveTickets_Object = MibScalar
ctxstaSTACountOfActiveTickets = _CtxstaSTACountOfActiveTickets_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 10, 4),
    _CtxstaSTACountOfActiveTickets_Type()
)
ctxstaSTACountOfActiveTickets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxstaSTACountOfActiveTickets.setStatus("current")
_CtxstaSTAGoodDataRequestCount_Type = Gauge32
_CtxstaSTAGoodDataRequestCount_Object = MibScalar
ctxstaSTAGoodDataRequestCount = _CtxstaSTAGoodDataRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 10, 5),
    _CtxstaSTAGoodDataRequestCount_Type()
)
ctxstaSTAGoodDataRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxstaSTAGoodDataRequestCount.setStatus("current")
_CtxstaSTAGoodRefreshRequestCount_Type = Gauge32
_CtxstaSTAGoodRefreshRequestCount_Object = MibScalar
ctxstaSTAGoodRefreshRequestCount = _CtxstaSTAGoodRefreshRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 10, 6),
    _CtxstaSTAGoodRefreshRequestCount_Type()
)
ctxstaSTAGoodRefreshRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxstaSTAGoodRefreshRequestCount.setStatus("current")
_CtxstaSTAGoodTicketRequestCount_Type = Gauge32
_CtxstaSTAGoodTicketRequestCount_Object = MibScalar
ctxstaSTAGoodTicketRequestCount = _CtxstaSTAGoodTicketRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 10, 7),
    _CtxstaSTAGoodTicketRequestCount_Type()
)
ctxstaSTAGoodTicketRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxstaSTAGoodTicketRequestCount.setStatus("current")
_CtxstaSTAPeakAllRequestRate_Type = Gauge32
_CtxstaSTAPeakAllRequestRate_Object = MibScalar
ctxstaSTAPeakAllRequestRate = _CtxstaSTAPeakAllRequestRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 10, 8),
    _CtxstaSTAPeakAllRequestRate_Type()
)
ctxstaSTAPeakAllRequestRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxstaSTAPeakAllRequestRate.setStatus("current")
_CtxstaSTAPeakDataRequestRate_Type = Gauge32
_CtxstaSTAPeakDataRequestRate_Object = MibScalar
ctxstaSTAPeakDataRequestRate = _CtxstaSTAPeakDataRequestRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 10, 9),
    _CtxstaSTAPeakDataRequestRate_Type()
)
ctxstaSTAPeakDataRequestRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxstaSTAPeakDataRequestRate.setStatus("current")
_CtxstaSTAPeakTicketRefreshRate_Type = Gauge32
_CtxstaSTAPeakTicketRefreshRate_Object = MibScalar
ctxstaSTAPeakTicketRefreshRate = _CtxstaSTAPeakTicketRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 10, 10),
    _CtxstaSTAPeakTicketRefreshRate_Type()
)
ctxstaSTAPeakTicketRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxstaSTAPeakTicketRefreshRate.setStatus("current")
_CtxstaSTAPeakTicketRequestRate_Type = Gauge32
_CtxstaSTAPeakTicketRequestRate_Object = MibScalar
ctxstaSTAPeakTicketRequestRate = _CtxstaSTAPeakTicketRequestRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 10, 11),
    _CtxstaSTAPeakTicketRequestRate_Type()
)
ctxstaSTAPeakTicketRequestRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxstaSTAPeakTicketRequestRate.setStatus("current")
_CtxstaSTATicketTimeoutCount_Type = Gauge32
_CtxstaSTATicketTimeoutCount_Object = MibScalar
ctxstaSTATicketTimeoutCount = _CtxstaSTATicketTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 41, 10, 12),
    _CtxstaSTATicketTimeoutCount_Type()
)
ctxstaSTATicketTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctxstaSTATicketTimeoutCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFORMANT-PERF-CITRIX",
    **{"citrixPerformance": citrixPerformance,
       "ctxCPUUtilizationMgmtUserTable": ctxCPUUtilizationMgmtUserTable,
       "ctxCPUUtilizationMgmtUserEntry": ctxCPUUtilizationMgmtUserEntry,
       "ctxcumuInstance": ctxcumuInstance,
       "ctxcumuCPUEntitlement": ctxcumuCPUEntitlement,
       "ctxcumuCPUReservation": ctxcumuCPUReservation,
       "ctxcumuCPUShares": ctxcumuCPUShares,
       "ctxcumuCPUUsage": ctxcumuCPUUsage,
       "ctxcumuLongTermCPUUsage": ctxcumuLongTermCPUUsage,
       "ctxDataLayerTable": ctxDataLayerTable,
       "ctxDataLayerEntry": ctxDataLayerEntry,
       "ctxdlInstance": ctxdlInstance,
       "ctxdlCommitsPerSec": ctxdlCommitsPerSec,
       "ctxdlContextsPerSec": ctxdlContextsPerSec,
       "ctxdlDeletesPerSec": ctxdlDeletesPerSec,
       "ctxdlInsertsPerSec": ctxdlInsertsPerSec,
       "ctxdlNumberOfContextsInThePool": ctxdlNumberOfContextsInThePool,
       "ctxdlNumOfCntxtRequestsWaiting": ctxdlNumOfCntxtRequestsWaiting,
       "ctxdlReadStreamsCreatedPerSec": ctxdlReadStreamsCreatedPerSec,
       "ctxdlStreamBytesReadPerSec": ctxdlStreamBytesReadPerSec,
       "ctxdlStreamBytesWrittenPerSec": ctxdlStreamBytesWrittenPerSec,
       "ctxdlStreamsCreatedPerSec": ctxdlStreamsCreatedPerSec,
       "ctxdlUpdatesPerSec": ctxdlUpdatesPerSec,
       "ctxdlWriteStreamsCreatedPerSec": ctxdlWriteStreamsCreatedPerSec,
       "ctxIMANetworkingTable": ctxIMANetworkingTable,
       "ctxIMANetworkingEntry": ctxIMANetworkingEntry,
       "ctximanInstance": ctximanInstance,
       "ctximanBytesReceivedPerSec": ctximanBytesReceivedPerSec,
       "ctximanBytesSentPerSec": ctximanBytesSentPerSec,
       "ctximanNetworkConnections": ctximanNetworkConnections,
       "citrixLicensing": citrixLicensing,
       "ctxlAverageCheckInRspTimeMs": ctxlAverageCheckInRspTimeMs,
       "ctxlAverageCheckOutRspTimeMs": ctxlAverageCheckOutRspTimeMs,
       "ctxlLastRecordCheckInRspTimeMs": ctxlLastRecordCheckInRspTimeMs,
       "ctxlLastRecordCheckOutRspTimeMs": ctxlLastRecordCheckOutRspTimeMs,
       "ctxlServerConnectionFailure": ctxlServerConnectionFailure,
       "ctxlMaximumCheckInRspTimeMs": ctxlMaximumCheckInRspTimeMs,
       "ctxlMaximumCheckOutRspTimeMs": ctxlMaximumCheckOutRspTimeMs,
       "citrixMetaFramePresentationSvr": citrixMetaFramePresentationSvr,
       "ctxmpsApplEnumerationsPerSec": ctxmpsApplEnumerationsPerSec,
       "ctxmpsApplResolutionTimeMs": ctxmpsApplResolutionTimeMs,
       "ctxmpsApplResolutionFailedPerSec": ctxmpsApplResolutionFailedPerSec,
       "ctxmpsApplResolutionsPerSec": ctxmpsApplResolutionsPerSec,
       "ctxmpsDataStoreConnectionFailure": ctxmpsDataStoreConnectionFailure,
       "ctxmpsDataStoreBytesRead": ctxmpsDataStoreBytesRead,
       "ctxmpsDataStoreBytesReadPerSec": ctxmpsDataStoreBytesReadPerSec,
       "ctxmpsDataStoreBytesWritePerSec": ctxmpsDataStoreBytesWritePerSec,
       "ctxmpsDataStoreReads": ctxmpsDataStoreReads,
       "ctxmpsDataStoreReadsPerSec": ctxmpsDataStoreReadsPerSec,
       "ctxmpsDataStoreWritesPerSec": ctxmpsDataStoreWritesPerSec,
       "ctxmpsDSGatewayUpdateCount": ctxmpsDSGatewayUpdateCount,
       "ctxmpsDSGatewayUpdateBytesSent": ctxmpsDSGatewayUpdateBytesSent,
       "ctxmpsDSQueryCount": ctxmpsDSQueryCount,
       "ctxmpsDSQueryRequestBytesReceive": ctxmpsDSQueryRequestBytesReceive,
       "ctxmpsDSQueryResponseBytesSent": ctxmpsDSQueryResponseBytesSent,
       "ctxmpsDSUpdateBytesReceived": ctxmpsDSUpdateBytesReceived,
       "ctxmpsDSUpdatePacketsReceived": ctxmpsDSUpdatePacketsReceived,
       "ctxmpsDSUpdateResponseBytesSent": ctxmpsDSUpdateResponseBytesSent,
       "ctxmpsDSBytesReadPerSec": ctxmpsDSBytesReadPerSec,
       "ctxmpsDSBytesWrittenPerSec": ctxmpsDSBytesWrittenPerSec,
       "ctxmpsDSReadsPerSec": ctxmpsDSReadsPerSec,
       "ctxmpsDSWritesPerSec": ctxmpsDSWritesPerSec,
       "ctxmpsFilteredApplEnumsPerSec": ctxmpsFilteredApplEnumsPerSec,
       "ctxmpsLCCacheBytesReadPerSec": ctxmpsLCCacheBytesReadPerSec,
       "ctxmpsLCCacheBytesWrittenPerSec": ctxmpsLCCacheBytesWrittenPerSec,
       "ctxmpsLCCacheReadsPerSec": ctxmpsLCCacheReadsPerSec,
       "ctxmpsLCCacheWritesPerSec": ctxmpsLCCacheWritesPerSec,
       "ctxmpsMaximumNumberOfXMLThreads": ctxmpsMaximumNumberOfXMLThreads,
       "ctxmpsNumberOfXMLThreads": ctxmpsNumberOfXMLThreads,
       "ctxmpsNumberOfBusyXMLThreads": ctxmpsNumberOfBusyXMLThreads,
       "ctxmpsResWorkItemQueueExecuteCnt": ctxmpsResWorkItemQueueExecuteCnt,
       "ctxmpsResWorkItemQueueReadyCount": ctxmpsResWorkItemQueueReadyCount,
       "ctxmpsWorkItemQueueExecuteCount": ctxmpsWorkItemQueueExecuteCount,
       "ctxmpsWorkItemQueuePendingCount": ctxmpsWorkItemQueuePendingCount,
       "ctxmpsWorkItemQueueReadyCount": ctxmpsWorkItemQueueReadyCount,
       "ctxmpsZoneElections": ctxmpsZoneElections,
       "ctxmpsZoneElectionsWon": ctxmpsZoneElectionsWon,
       "ctxSmartAuditorAgent": ctxSmartAuditorAgent,
       "ctxsaaActiveRecordingCount": ctxsaaActiveRecordingCount,
       "ctxsaaReadSmartAuditorDriverSec": ctxsaaReadSmartAuditorDriverSec,
       "ctxSmartAuditorStorageManager": ctxSmartAuditorStorageManager,
       "ctxsasmActiveRecordingCount": ctxsasmActiveRecordingCount,
       "ctxsasmMessageBytesPerSec": ctxsasmMessageBytesPerSec,
       "ctxsasmMessagesPerSec": ctxsasmMessagesPerSec,
       "ctxDesktopBrokerDatabaseService": ctxDesktopBrokerDatabaseService,
       "ctxdbdsHostedDesktopReleasesSec": ctxdbdsHostedDesktopReleasesSec,
       "ctxdbdsHostedDesktopRequestsSec": ctxdbdsHostedDesktopRequestsSec,
       "ctxdbdsHostedDesktopStateUpdSec": ctxdbdsHostedDesktopStateUpdSec,
       "ctxICASessionTable": ctxICASessionTable,
       "ctxICASessionEntry": ctxICASessionEntry,
       "ctxisInstance": ctxisInstance,
       "ctxisInputAudioBandwidth": ctxisInputAudioBandwidth,
       "ctxisInputCOM1Bandwidth": ctxisInputCOM1Bandwidth,
       "ctxisInputCOM2Bandwidth": ctxisInputCOM2Bandwidth,
       "ctxisInputCOMBandwidth": ctxisInputCOMBandwidth,
       "ctxisInputClipboardBandwidt": ctxisInputClipboardBandwidt,
       "ctxisInputControlChanBandwidth": ctxisInputControlChanBandwidth,
       "ctxisInputDriveBandwidth": ctxisInputDriveBandwidth,
       "ctxisInputFontDataBandwidth": ctxisInputFontDataBandwidth,
       "ctxisInputLPT1Bandwidth": ctxisInputLPT1Bandwidth,
       "ctxisInputLPT2Bandwidth": ctxisInputLPT2Bandwidth,
       "ctxisInputLicensingBandwidth": ctxisInputLicensingBandwidth,
       "ctxisInputManagementBandwidth": ctxisInputManagementBandwidth,
       "ctxisInputPNBandwidth": ctxisInputPNBandwidth,
       "ctxisInputPrinterBandwidth": ctxisInputPrinterBandwidth,
       "ctxisInputSeamlessBandwidth": ctxisInputSeamlessBandwidth,
       "ctxisInputSessionBandwidth": ctxisInputSessionBandwidth,
       "ctxisInputSessionCompression": ctxisInputSessionCompression,
       "ctxisInputSessionLineSpeed": ctxisInputSessionLineSpeed,
       "ctxisInputSpeedScreenDataChanBW": ctxisInputSpeedScreenDataChanBW,
       "ctxisInputTextEchoBandwidth": ctxisInputTextEchoBandwidth,
       "ctxisInputThinWireBandwidth": ctxisInputThinWireBandwidth,
       "ctxisInputVideoFrameBandwidth": ctxisInputVideoFrameBandwidth,
       "ctxisLatencyLastRecorded": ctxisLatencyLastRecorded,
       "ctxisLatencySessionAverage": ctxisLatencySessionAverage,
       "ctxisLatencySessionDeviation": ctxisLatencySessionDeviation,
       "ctxisOutputAudioBandwidth": ctxisOutputAudioBandwidth,
       "ctxisOutputCOM1Bandwidth": ctxisOutputCOM1Bandwidth,
       "ctxisOutputCOM2Bandwidth": ctxisOutputCOM2Bandwidth,
       "ctxisOutputCOMBandwidth": ctxisOutputCOMBandwidth,
       "ctxisOutputClipboardBandwidth": ctxisOutputClipboardBandwidth,
       "ctxisOutputControlChannBandwidth": ctxisOutputControlChannBandwidth,
       "ctxisOutputDriveBandwidth": ctxisOutputDriveBandwidth,
       "ctxisOutputFontDataBandwidth": ctxisOutputFontDataBandwidth,
       "ctxisOutputLPT1Bandwidth": ctxisOutputLPT1Bandwidth,
       "ctxisOutputLPT2Bandwidth": ctxisOutputLPT2Bandwidth,
       "ctxisOutputLicensingBandwidth": ctxisOutputLicensingBandwidth,
       "ctxisOutputManagementBandwidth": ctxisOutputManagementBandwidth,
       "ctxisOutputPNBandwidth": ctxisOutputPNBandwidth,
       "ctxisOutputPrinterBandwidth": ctxisOutputPrinterBandwidth,
       "ctxisOutputSeamlessBandwidth": ctxisOutputSeamlessBandwidth,
       "ctxisOutputSessionBandwidth": ctxisOutputSessionBandwidth,
       "ctxisOutputSessionCompression": ctxisOutputSessionCompression,
       "ctxisOutputSessionLineSpeed": ctxisOutputSessionLineSpeed,
       "ctxisOutputSpeedScreenDataChanBW": ctxisOutputSpeedScreenDataChanBW,
       "ctxisOutputTextEchoBandwidth": ctxisOutputTextEchoBandwidth,
       "ctxisOutputThinWireBandwidth": ctxisOutputThinWireBandwidth,
       "ctxisOutputVideoFrameBandwidth": ctxisOutputVideoFrameBandwidth,
       "ctxSecureTicketAuthority": ctxSecureTicketAuthority,
       "ctxstaSTABadDataRequestCount": ctxstaSTABadDataRequestCount,
       "ctxstaSTABadRefreshRequestCount": ctxstaSTABadRefreshRequestCount,
       "ctxstaSTABadTicketRequestCount": ctxstaSTABadTicketRequestCount,
       "ctxstaSTACountOfActiveTickets": ctxstaSTACountOfActiveTickets,
       "ctxstaSTAGoodDataRequestCount": ctxstaSTAGoodDataRequestCount,
       "ctxstaSTAGoodRefreshRequestCount": ctxstaSTAGoodRefreshRequestCount,
       "ctxstaSTAGoodTicketRequestCount": ctxstaSTAGoodTicketRequestCount,
       "ctxstaSTAPeakAllRequestRate": ctxstaSTAPeakAllRequestRate,
       "ctxstaSTAPeakDataRequestRate": ctxstaSTAPeakDataRequestRate,
       "ctxstaSTAPeakTicketRefreshRate": ctxstaSTAPeakTicketRefreshRate,
       "ctxstaSTAPeakTicketRequestRate": ctxstaSTAPeakTicketRequestRate,
       "ctxstaSTATicketTimeoutCount": ctxstaSTATicketTimeoutCount}
)
