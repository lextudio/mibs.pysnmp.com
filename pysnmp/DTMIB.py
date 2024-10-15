# SNMP MIB module (DTMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DTMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:47 2024
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
 NotificationType,
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
    "NotificationType",
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

_Nsi_ObjectIdentity = ObjectIdentity
nsi = _Nsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2592)
)
_NsiDoubleTake_ObjectIdentity = ObjectIdentity
nsiDoubleTake = _NsiDoubleTake_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2592, 3)
)
_DtTraps_ObjectIdentity = ObjectIdentity
dtTraps = _DtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2592, 3, 1)
)
_DtGeneral_ObjectIdentity = ObjectIdentity
dtGeneral = _DtGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2592, 3, 2)
)
_DtUpTime_Type = TimeTicks
_DtUpTime_Object = MibScalar
dtUpTime = _DtUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 2, 1),
    _DtUpTime_Type()
)
dtUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtUpTime.setStatus("mandatory")
_DtCurrentMemoryUsage_Type = Gauge32
_DtCurrentMemoryUsage_Object = MibScalar
dtCurrentMemoryUsage = _DtCurrentMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 2, 2),
    _DtCurrentMemoryUsage_Type()
)
dtCurrentMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtCurrentMemoryUsage.setStatus("mandatory")
_DtMirOpsGenerated_Type = Counter32
_DtMirOpsGenerated_Object = MibScalar
dtMirOpsGenerated = _DtMirOpsGenerated_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 2, 3),
    _DtMirOpsGenerated_Type()
)
dtMirOpsGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtMirOpsGenerated.setStatus("mandatory")
_DtMirBytesGenerated_Type = Counter32
_DtMirBytesGenerated_Object = MibScalar
dtMirBytesGenerated = _DtMirBytesGenerated_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 2, 4),
    _DtMirBytesGenerated_Type()
)
dtMirBytesGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtMirBytesGenerated.setStatus("mandatory")
_DtRepOpsGenerated_Type = Counter32
_DtRepOpsGenerated_Object = MibScalar
dtRepOpsGenerated = _DtRepOpsGenerated_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 2, 5),
    _DtRepOpsGenerated_Type()
)
dtRepOpsGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtRepOpsGenerated.setStatus("mandatory")
_DtRepBytesGenerated_Type = Counter32
_DtRepBytesGenerated_Object = MibScalar
dtRepBytesGenerated = _DtRepBytesGenerated_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 2, 6),
    _DtRepBytesGenerated_Type()
)
dtRepBytesGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtRepBytesGenerated.setStatus("mandatory")
_DtFailedMirrorCount_Type = Counter32
_DtFailedMirrorCount_Object = MibScalar
dtFailedMirrorCount = _DtFailedMirrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 2, 7),
    _DtFailedMirrorCount_Type()
)
dtFailedMirrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtFailedMirrorCount.setStatus("mandatory")
_DtFailedRepCount_Type = Counter32
_DtFailedRepCount_Object = MibScalar
dtFailedRepCount = _DtFailedRepCount_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 2, 8),
    _DtFailedRepCount_Type()
)
dtFailedRepCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtFailedRepCount.setStatus("mandatory")
_DtActFailCount_Type = Counter32
_DtActFailCount_Object = MibScalar
dtActFailCount = _DtActFailCount_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 2, 9),
    _DtActFailCount_Type()
)
dtActFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtActFailCount.setStatus("mandatory")
_DtAutoDisCount_Type = Counter32
_DtAutoDisCount_Object = MibScalar
dtAutoDisCount = _DtAutoDisCount_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 2, 10),
    _DtAutoDisCount_Type()
)
dtAutoDisCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtAutoDisCount.setStatus("mandatory")
_DtAutoReCount_Type = Counter32
_DtAutoReCount_Object = MibScalar
dtAutoReCount = _DtAutoReCount_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 2, 11),
    _DtAutoReCount_Type()
)
dtAutoReCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtAutoReCount.setStatus("mandatory")
_DtDriverQueuePercent_Type = Counter32
_DtDriverQueuePercent_Object = MibScalar
dtDriverQueuePercent = _DtDriverQueuePercent_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 2, 12),
    _DtDriverQueuePercent_Type()
)
dtDriverQueuePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtDriverQueuePercent.setStatus("mandatory")
_DtSource_ObjectIdentity = ObjectIdentity
dtSource = _DtSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2592, 3, 3)
)


class _DtSourceState_Type(Integer32):
    """Custom type dtSourceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadedNoDriver", 1),
          ("loadedWithDriver", 2),
          ("notLoaded", 0))
    )


_DtSourceState_Type.__name__ = "Integer32"
_DtSourceState_Object = MibScalar
dtSourceState = _DtSourceState_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 3, 1),
    _DtSourceState_Type()
)
dtSourceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtSourceState.setStatus("mandatory")
_DtTarget_ObjectIdentity = ObjectIdentity
dtTarget = _DtTarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2592, 3, 4)
)


class _DtTargetState_Type(Integer32):
    """Custom type dtTargetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("notLoaded", 0))
    )


_DtTargetState_Type.__name__ = "Integer32"
_DtTargetState_Object = MibScalar
dtTargetState = _DtTargetState_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 4, 1),
    _DtTargetState_Type()
)
dtTargetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtTargetState.setStatus("mandatory")
_DtRetryCount_Type = Counter32
_DtRetryCount_Object = MibScalar
dtRetryCount = _DtRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 4, 2),
    _DtRetryCount_Type()
)
dtRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtRetryCount.setStatus("mandatory")
_DtOpsDroppedCount_Type = Counter32
_DtOpsDroppedCount_Object = MibScalar
dtOpsDroppedCount = _DtOpsDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 4, 3),
    _DtOpsDroppedCount_Type()
)
dtOpsDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtOpsDroppedCount.setStatus("mandatory")
_DtSecurity_ObjectIdentity = ObjectIdentity
dtSecurity = _DtSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2592, 3, 5)
)
_DtLoginCount_Type = Counter32
_DtLoginCount_Object = MibScalar
dtLoginCount = _DtLoginCount_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 5, 1),
    _DtLoginCount_Type()
)
dtLoginCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtLoginCount.setStatus("mandatory")
_DtFailedLoginCount_Type = Counter32
_DtFailedLoginCount_Object = MibScalar
dtFailedLoginCount = _DtFailedLoginCount_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 5, 2),
    _DtFailedLoginCount_Type()
)
dtFailedLoginCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtFailedLoginCount.setStatus("mandatory")
_DtConnection_ObjectIdentity = ObjectIdentity
dtConnection = _DtConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6)
)
_DtConnectionCount_Type = Counter32
_DtConnectionCount_Object = MibScalar
dtConnectionCount = _DtConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 1),
    _DtConnectionCount_Type()
)
dtConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtConnectionCount.setStatus("mandatory")
_DtConnectionTable_Object = MibTable
dtConnectionTable = _DtConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2)
)
if mibBuilder.loadTexts:
    dtConnectionTable.setStatus("mandatory")
_DtConnectionEntry_Object = MibTableRow
dtConnectionEntry = _DtConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1)
)
dtConnectionEntry.setIndexNames(
    (0, "DTMIB", "dtConnectionIndex"),
)
if mibBuilder.loadTexts:
    dtConnectionEntry.setStatus("mandatory")


class _DtConnectionIndex_Type(Integer32):
    """Custom type dtConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DtConnectionIndex_Type.__name__ = "Integer32"
_DtConnectionIndex_Object = MibTableColumn
dtConnectionIndex = _DtConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 1),
    _DtConnectionIndex_Type()
)
dtConnectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dtConnectionIndex.setStatus("mandatory")
_DtconIpAddress_Type = IpAddress
_DtconIpAddress_Object = MibTableColumn
dtconIpAddress = _DtconIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 2),
    _DtconIpAddress_Type()
)
dtconIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtconIpAddress.setStatus("mandatory")
_DtconConnectTime_Type = TimeTicks
_DtconConnectTime_Object = MibTableColumn
dtconConnectTime = _DtconConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 3),
    _DtconConnectTime_Type()
)
dtconConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtconConnectTime.setStatus("mandatory")


class _DtconState_Type(Integer32):
    """Custom type dtconState based on Integer32"""
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
        *(("conActive", 1),
          ("conError", 0),
          ("conNone", 4),
          ("conPaused", 2),
          ("conScheduled", 3))
    )


_DtconState_Type.__name__ = "Integer32"
_DtconState_Object = MibTableColumn
dtconState = _DtconState_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 4),
    _DtconState_Type()
)
dtconState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtconState.setStatus("mandatory")
_DtconOpsInCmdQueue_Type = Gauge32
_DtconOpsInCmdQueue_Object = MibTableColumn
dtconOpsInCmdQueue = _DtconOpsInCmdQueue_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 5),
    _DtconOpsInCmdQueue_Type()
)
dtconOpsInCmdQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtconOpsInCmdQueue.setStatus("mandatory")
_DtconOpsInAckQueue_Type = Gauge32
_DtconOpsInAckQueue_Object = MibTableColumn
dtconOpsInAckQueue = _DtconOpsInAckQueue_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 6),
    _DtconOpsInAckQueue_Type()
)
dtconOpsInAckQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtconOpsInAckQueue.setStatus("mandatory")
_DtconOpsInRepQueue_Type = Gauge32
_DtconOpsInRepQueue_Object = MibTableColumn
dtconOpsInRepQueue = _DtconOpsInRepQueue_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 7),
    _DtconOpsInRepQueue_Type()
)
dtconOpsInRepQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtconOpsInRepQueue.setStatus("mandatory")
_DtconOpsInMirQueue_Type = Gauge32
_DtconOpsInMirQueue_Object = MibTableColumn
dtconOpsInMirQueue = _DtconOpsInMirQueue_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 8),
    _DtconOpsInMirQueue_Type()
)
dtconOpsInMirQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtconOpsInMirQueue.setStatus("mandatory")
_DtconBytesInRepQueue_Type = Gauge32
_DtconBytesInRepQueue_Object = MibTableColumn
dtconBytesInRepQueue = _DtconBytesInRepQueue_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 9),
    _DtconBytesInRepQueue_Type()
)
dtconBytesInRepQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtconBytesInRepQueue.setStatus("mandatory")
_DtconBytesInMirQueue_Type = Gauge32
_DtconBytesInMirQueue_Object = MibTableColumn
dtconBytesInMirQueue = _DtconBytesInMirQueue_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 10),
    _DtconBytesInMirQueue_Type()
)
dtconBytesInMirQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtconBytesInMirQueue.setStatus("mandatory")
_DtconOpsTx_Type = Counter32
_DtconOpsTx_Object = MibTableColumn
dtconOpsTx = _DtconOpsTx_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 11),
    _DtconOpsTx_Type()
)
dtconOpsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtconOpsTx.setStatus("mandatory")
_DtconBytesTx_Type = Counter32
_DtconBytesTx_Object = MibTableColumn
dtconBytesTx = _DtconBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 12),
    _DtconBytesTx_Type()
)
dtconBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtconBytesTx.setStatus("mandatory")
_DtconOpsRx_Type = Counter32
_DtconOpsRx_Object = MibTableColumn
dtconOpsRx = _DtconOpsRx_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 13),
    _DtconOpsRx_Type()
)
dtconOpsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtconOpsRx.setStatus("mandatory")
_DtconBytesRx_Type = Counter32
_DtconBytesRx_Object = MibTableColumn
dtconBytesRx = _DtconBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 14),
    _DtconBytesRx_Type()
)
dtconBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtconBytesRx.setStatus("mandatory")
_DtconResentOpCount_Type = Counter32
_DtconResentOpCount_Object = MibTableColumn
dtconResentOpCount = _DtconResentOpCount_Object(
    (1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 15),
    _DtconResentOpCount_Type()
)
dtconResentOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtconResentOpCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dttrapKernelStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 1)
)
if mibBuilder.loadTexts:
    dttrapKernelStarted.setStatus(
        ""
    )

dttrapKernelStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 2)
)
if mibBuilder.loadTexts:
    dttrapKernelStopped.setStatus(
        ""
    )

dttrapLicenseViolationStartingSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 3)
)
if mibBuilder.loadTexts:
    dttrapLicenseViolationStartingSource.setStatus(
        ""
    )

dttrapLicenseViolationOnNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 4)
)
if mibBuilder.loadTexts:
    dttrapLicenseViolationOnNetwork.setStatus(
        ""
    )

dttrapSourceStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 5)
)
if mibBuilder.loadTexts:
    dttrapSourceStarted.setStatus(
        ""
    )

dttrapSourceStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 6)
)
if mibBuilder.loadTexts:
    dttrapSourceStopped.setStatus(
        ""
    )

dttrapTargetStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 7)
)
if mibBuilder.loadTexts:
    dttrapTargetStarted.setStatus(
        ""
    )

dttrapTargetStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 8)
)
if mibBuilder.loadTexts:
    dttrapTargetStopped.setStatus(
        ""
    )

dttrapConnectionRequested = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 9)
)
if mibBuilder.loadTexts:
    dttrapConnectionRequested.setStatus(
        ""
    )

dttrapConnectionRequestReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 10)
)
if mibBuilder.loadTexts:
    dttrapConnectionRequestReceived.setStatus(
        ""
    )

dttrapConnectionSucceded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 11)
)
if mibBuilder.loadTexts:
    dttrapConnectionSucceded.setStatus(
        ""
    )

dttrapConnectionPause = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 12)
)
if mibBuilder.loadTexts:
    dttrapConnectionPause.setStatus(
        ""
    )

dttrapConnectionResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 13)
)
if mibBuilder.loadTexts:
    dttrapConnectionResume.setStatus(
        ""
    )

dttrapConnectionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 14)
)
if mibBuilder.loadTexts:
    dttrapConnectionFailed.setStatus(
        ""
    )

dttrapConnectionLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 15)
)
if mibBuilder.loadTexts:
    dttrapConnectionLost.setStatus(
        ""
    )

dttrapMemoryLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 16)
)
if mibBuilder.loadTexts:
    dttrapMemoryLimitReached.setStatus(
        ""
    )

dttrapMemoryLimitRemedied = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 17)
)
if mibBuilder.loadTexts:
    dttrapMemoryLimitRemedied.setStatus(
        ""
    )

dttrapAutoReconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 18)
)
if mibBuilder.loadTexts:
    dttrapAutoReconnect.setStatus(
        ""
    )

dttrapScheduledConnectStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 19)
)
if mibBuilder.loadTexts:
    dttrapScheduledConnectStart.setStatus(
        ""
    )

dttrapScheduledConnectEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 20)
)
if mibBuilder.loadTexts:
    dttrapScheduledConnectEnd.setStatus(
        ""
    )

dttrapAutoDisconnectWriteQueue = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 21)
)
if mibBuilder.loadTexts:
    dttrapAutoDisconnectWriteQueue.setStatus(
        ""
    )

dttrapAutoDisconnectPauseTransmission = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 22)
)
if mibBuilder.loadTexts:
    dttrapAutoDisconnectPauseTransmission.setStatus(
        ""
    )

dttrapAutoDisconnectEndConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 23)
)
if mibBuilder.loadTexts:
    dttrapAutoDisconnectEndConnection.setStatus(
        ""
    )

dttrapAutoDisconnectShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 24)
)
if mibBuilder.loadTexts:
    dttrapAutoDisconnectShutdown.setStatus(
        ""
    )

dttrapReplicationStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 25)
)
if mibBuilder.loadTexts:
    dttrapReplicationStart.setStatus(
        ""
    )

dttrapReplicationStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 26)
)
if mibBuilder.loadTexts:
    dttrapReplicationStop.setStatus(
        ""
    )

dttrapMirrorStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 27)
)
if mibBuilder.loadTexts:
    dttrapMirrorStart.setStatus(
        ""
    )

dttrapMirrorStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 28)
)
if mibBuilder.loadTexts:
    dttrapMirrorStop.setStatus(
        ""
    )

dttrapMirrorPause = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 29)
)
if mibBuilder.loadTexts:
    dttrapMirrorPause.setStatus(
        ""
    )

dttrapMirrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 30)
)
if mibBuilder.loadTexts:
    dttrapMirrorResume.setStatus(
        ""
    )

dttrapMirrorEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 31)
)
if mibBuilder.loadTexts:
    dttrapMirrorEnd.setStatus(
        ""
    )

dttrapVerificationStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 32)
)
if mibBuilder.loadTexts:
    dttrapVerificationStart.setStatus(
        ""
    )

dttrapVerificationEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 33)
)
if mibBuilder.loadTexts:
    dttrapVerificationEnd.setStatus(
        ""
    )

dttrapVerficationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 34)
)
if mibBuilder.loadTexts:
    dttrapVerficationFailure.setStatus(
        ""
    )

dttrapRestoreStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 35)
)
if mibBuilder.loadTexts:
    dttrapRestoreStarted.setStatus(
        ""
    )

dttrapRestoreComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 36)
)
if mibBuilder.loadTexts:
    dttrapRestoreComplete.setStatus(
        ""
    )

dttrapRepSetModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 37)
)
if mibBuilder.loadTexts:
    dttrapRepSetModified.setStatus(
        ""
    )

dttrapFailoverConditionMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 38)
)
if mibBuilder.loadTexts:
    dttrapFailoverConditionMet.setStatus(
        ""
    )

dttrapFailoverInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 39)
)
if mibBuilder.loadTexts:
    dttrapFailoverInProgress.setStatus(
        ""
    )

dttrapTargetFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2592, 0, 40)
)
if mibBuilder.loadTexts:
    dttrapTargetFull.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DTMIB",
    **{"nsi": nsi,
       "dttrapKernelStarted": dttrapKernelStarted,
       "dttrapKernelStopped": dttrapKernelStopped,
       "dttrapLicenseViolationStartingSource": dttrapLicenseViolationStartingSource,
       "dttrapLicenseViolationOnNetwork": dttrapLicenseViolationOnNetwork,
       "dttrapSourceStarted": dttrapSourceStarted,
       "dttrapSourceStopped": dttrapSourceStopped,
       "dttrapTargetStarted": dttrapTargetStarted,
       "dttrapTargetStopped": dttrapTargetStopped,
       "dttrapConnectionRequested": dttrapConnectionRequested,
       "dttrapConnectionRequestReceived": dttrapConnectionRequestReceived,
       "dttrapConnectionSucceded": dttrapConnectionSucceded,
       "dttrapConnectionPause": dttrapConnectionPause,
       "dttrapConnectionResume": dttrapConnectionResume,
       "dttrapConnectionFailed": dttrapConnectionFailed,
       "dttrapConnectionLost": dttrapConnectionLost,
       "dttrapMemoryLimitReached": dttrapMemoryLimitReached,
       "dttrapMemoryLimitRemedied": dttrapMemoryLimitRemedied,
       "dttrapAutoReconnect": dttrapAutoReconnect,
       "dttrapScheduledConnectStart": dttrapScheduledConnectStart,
       "dttrapScheduledConnectEnd": dttrapScheduledConnectEnd,
       "dttrapAutoDisconnectWriteQueue": dttrapAutoDisconnectWriteQueue,
       "dttrapAutoDisconnectPauseTransmission": dttrapAutoDisconnectPauseTransmission,
       "dttrapAutoDisconnectEndConnection": dttrapAutoDisconnectEndConnection,
       "dttrapAutoDisconnectShutdown": dttrapAutoDisconnectShutdown,
       "dttrapReplicationStart": dttrapReplicationStart,
       "dttrapReplicationStop": dttrapReplicationStop,
       "dttrapMirrorStart": dttrapMirrorStart,
       "dttrapMirrorStop": dttrapMirrorStop,
       "dttrapMirrorPause": dttrapMirrorPause,
       "dttrapMirrorResume": dttrapMirrorResume,
       "dttrapMirrorEnd": dttrapMirrorEnd,
       "dttrapVerificationStart": dttrapVerificationStart,
       "dttrapVerificationEnd": dttrapVerificationEnd,
       "dttrapVerficationFailure": dttrapVerficationFailure,
       "dttrapRestoreStarted": dttrapRestoreStarted,
       "dttrapRestoreComplete": dttrapRestoreComplete,
       "dttrapRepSetModified": dttrapRepSetModified,
       "dttrapFailoverConditionMet": dttrapFailoverConditionMet,
       "dttrapFailoverInProgress": dttrapFailoverInProgress,
       "dttrapTargetFull": dttrapTargetFull,
       "nsiDoubleTake": nsiDoubleTake,
       "dtTraps": dtTraps,
       "dtGeneral": dtGeneral,
       "dtUpTime": dtUpTime,
       "dtCurrentMemoryUsage": dtCurrentMemoryUsage,
       "dtMirOpsGenerated": dtMirOpsGenerated,
       "dtMirBytesGenerated": dtMirBytesGenerated,
       "dtRepOpsGenerated": dtRepOpsGenerated,
       "dtRepBytesGenerated": dtRepBytesGenerated,
       "dtFailedMirrorCount": dtFailedMirrorCount,
       "dtFailedRepCount": dtFailedRepCount,
       "dtActFailCount": dtActFailCount,
       "dtAutoDisCount": dtAutoDisCount,
       "dtAutoReCount": dtAutoReCount,
       "dtDriverQueuePercent": dtDriverQueuePercent,
       "dtSource": dtSource,
       "dtSourceState": dtSourceState,
       "dtTarget": dtTarget,
       "dtTargetState": dtTargetState,
       "dtRetryCount": dtRetryCount,
       "dtOpsDroppedCount": dtOpsDroppedCount,
       "dtSecurity": dtSecurity,
       "dtLoginCount": dtLoginCount,
       "dtFailedLoginCount": dtFailedLoginCount,
       "dtConnection": dtConnection,
       "dtConnectionCount": dtConnectionCount,
       "dtConnectionTable": dtConnectionTable,
       "dtConnectionEntry": dtConnectionEntry,
       "dtConnectionIndex": dtConnectionIndex,
       "dtconIpAddress": dtconIpAddress,
       "dtconConnectTime": dtconConnectTime,
       "dtconState": dtconState,
       "dtconOpsInCmdQueue": dtconOpsInCmdQueue,
       "dtconOpsInAckQueue": dtconOpsInAckQueue,
       "dtconOpsInRepQueue": dtconOpsInRepQueue,
       "dtconOpsInMirQueue": dtconOpsInMirQueue,
       "dtconBytesInRepQueue": dtconBytesInRepQueue,
       "dtconBytesInMirQueue": dtconBytesInMirQueue,
       "dtconOpsTx": dtconOpsTx,
       "dtconBytesTx": dtconBytesTx,
       "dtconOpsRx": dtconOpsRx,
       "dtconBytesRx": dtconBytesRx,
       "dtconResentOpCount": dtconResentOpCount}
)
