# SNMP MIB module (Nortel-MsCarrier-MscPassport-TraceBaseMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-TraceBaseMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:22 2024
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

(DisplayString,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiStringIndex,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiStringIndex",
    "NonReplicated")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MscTrace_ObjectIdentity = ObjectIdentity
mscTrace = _MscTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106)
)
_MscTraceRowStatusTable_Object = MibTable
mscTraceRowStatusTable = _MscTraceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 1)
)
if mibBuilder.loadTexts:
    mscTraceRowStatusTable.setStatus("mandatory")
_MscTraceRowStatusEntry_Object = MibTableRow
mscTraceRowStatusEntry = _MscTraceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 1, 1)
)
mscTraceRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRowStatusEntry.setStatus("mandatory")
_MscTraceRowStatus_Type = RowStatus
_MscTraceRowStatus_Object = MibTableColumn
mscTraceRowStatus = _MscTraceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 1, 1, 1),
    _MscTraceRowStatus_Type()
)
mscTraceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRowStatus.setStatus("mandatory")
_MscTraceComponentName_Type = DisplayString
_MscTraceComponentName_Object = MibTableColumn
mscTraceComponentName = _MscTraceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 1, 1, 2),
    _MscTraceComponentName_Type()
)
mscTraceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceComponentName.setStatus("mandatory")
_MscTraceStorageType_Type = StorageType
_MscTraceStorageType_Object = MibTableColumn
mscTraceStorageType = _MscTraceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 1, 1, 4),
    _MscTraceStorageType_Type()
)
mscTraceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceStorageType.setStatus("mandatory")
_MscTraceIndex_Type = NonReplicated
_MscTraceIndex_Object = MibTableColumn
mscTraceIndex = _MscTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 1, 1, 10),
    _MscTraceIndex_Type()
)
mscTraceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceIndex.setStatus("mandatory")
_MscTraceRcvr_ObjectIdentity = ObjectIdentity
mscTraceRcvr = _MscTraceRcvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2)
)
_MscTraceRcvrRowStatusTable_Object = MibTable
mscTraceRcvrRowStatusTable = _MscTraceRcvrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 1)
)
if mibBuilder.loadTexts:
    mscTraceRcvrRowStatusTable.setStatus("mandatory")
_MscTraceRcvrRowStatusEntry_Object = MibTableRow
mscTraceRcvrRowStatusEntry = _MscTraceRcvrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 1, 1)
)
mscTraceRcvrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceRcvrIndex"),
)
if mibBuilder.loadTexts:
    mscTraceRcvrRowStatusEntry.setStatus("mandatory")
_MscTraceRcvrRowStatus_Type = RowStatus
_MscTraceRcvrRowStatus_Object = MibTableColumn
mscTraceRcvrRowStatus = _MscTraceRcvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 1, 1, 1),
    _MscTraceRcvrRowStatus_Type()
)
mscTraceRcvrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTraceRcvrRowStatus.setStatus("mandatory")
_MscTraceRcvrComponentName_Type = DisplayString
_MscTraceRcvrComponentName_Object = MibTableColumn
mscTraceRcvrComponentName = _MscTraceRcvrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 1, 1, 2),
    _MscTraceRcvrComponentName_Type()
)
mscTraceRcvrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrComponentName.setStatus("mandatory")
_MscTraceRcvrStorageType_Type = StorageType
_MscTraceRcvrStorageType_Object = MibTableColumn
mscTraceRcvrStorageType = _MscTraceRcvrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 1, 1, 4),
    _MscTraceRcvrStorageType_Type()
)
mscTraceRcvrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceRcvrStorageType.setStatus("mandatory")


class _MscTraceRcvrIndex_Type(AsciiStringIndex):
    """Custom type mscTraceRcvrIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscTraceRcvrIndex_Type.__name__ = "AsciiStringIndex"
_MscTraceRcvrIndex_Object = MibTableColumn
mscTraceRcvrIndex = _MscTraceRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 2, 1, 1, 10),
    _MscTraceRcvrIndex_Type()
)
mscTraceRcvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceRcvrIndex.setStatus("mandatory")
_MscTraceSession_ObjectIdentity = ObjectIdentity
mscTraceSession = _MscTraceSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3)
)
_MscTraceSessionRowStatusTable_Object = MibTable
mscTraceSessionRowStatusTable = _MscTraceSessionRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 1)
)
if mibBuilder.loadTexts:
    mscTraceSessionRowStatusTable.setStatus("mandatory")
_MscTraceSessionRowStatusEntry_Object = MibTableRow
mscTraceSessionRowStatusEntry = _MscTraceSessionRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 1, 1)
)
mscTraceSessionRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceSessionIndex"),
)
if mibBuilder.loadTexts:
    mscTraceSessionRowStatusEntry.setStatus("mandatory")
_MscTraceSessionRowStatus_Type = RowStatus
_MscTraceSessionRowStatus_Object = MibTableColumn
mscTraceSessionRowStatus = _MscTraceSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 1, 1, 1),
    _MscTraceSessionRowStatus_Type()
)
mscTraceSessionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionRowStatus.setStatus("mandatory")
_MscTraceSessionComponentName_Type = DisplayString
_MscTraceSessionComponentName_Object = MibTableColumn
mscTraceSessionComponentName = _MscTraceSessionComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 1, 1, 2),
    _MscTraceSessionComponentName_Type()
)
mscTraceSessionComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionComponentName.setStatus("mandatory")
_MscTraceSessionStorageType_Type = StorageType
_MscTraceSessionStorageType_Object = MibTableColumn
mscTraceSessionStorageType = _MscTraceSessionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 1, 1, 4),
    _MscTraceSessionStorageType_Type()
)
mscTraceSessionStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionStorageType.setStatus("mandatory")


class _MscTraceSessionIndex_Type(Integer32):
    """Custom type mscTraceSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_MscTraceSessionIndex_Type.__name__ = "Integer32"
_MscTraceSessionIndex_Object = MibTableColumn
mscTraceSessionIndex = _MscTraceSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 1, 1, 10),
    _MscTraceSessionIndex_Type()
)
mscTraceSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTraceSessionIndex.setStatus("mandatory")
_MscTraceSessionOperationalTable_Object = MibTable
mscTraceSessionOperationalTable = _MscTraceSessionOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 100)
)
if mibBuilder.loadTexts:
    mscTraceSessionOperationalTable.setStatus("mandatory")
_MscTraceSessionOperationalEntry_Object = MibTableRow
mscTraceSessionOperationalEntry = _MscTraceSessionOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 100, 1)
)
mscTraceSessionOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-TraceBaseMIB", "mscTraceSessionIndex"),
)
if mibBuilder.loadTexts:
    mscTraceSessionOperationalEntry.setStatus("mandatory")
_MscTraceSessionServiceTraced_Type = RowPointer
_MscTraceSessionServiceTraced_Object = MibTableColumn
mscTraceSessionServiceTraced = _MscTraceSessionServiceTraced_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 100, 1, 2),
    _MscTraceSessionServiceTraced_Type()
)
mscTraceSessionServiceTraced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionServiceTraced.setStatus("mandatory")
_MscTraceSessionReceiver_Type = RowPointer
_MscTraceSessionReceiver_Object = MibTableColumn
mscTraceSessionReceiver = _MscTraceSessionReceiver_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 100, 1, 3),
    _MscTraceSessionReceiver_Type()
)
mscTraceSessionReceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionReceiver.setStatus("mandatory")


class _MscTraceSessionSessionState_Type(Integer32):
    """Custom type mscTraceSessionSessionState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("abortingDueToCallFailure", 7),
          ("active", 10),
          ("binding", 8),
          ("callingReceiver", 5),
          ("clearingCallToReceiver", 6),
          ("idle", 1),
          ("initializing", 0),
          ("releasingSession", 3),
          ("unbinding", 9),
          ("waitingForProvisioningData", 4),
          ("waitingForSession", 2))
    )


_MscTraceSessionSessionState_Type.__name__ = "Integer32"
_MscTraceSessionSessionState_Object = MibTableColumn
mscTraceSessionSessionState = _MscTraceSessionSessionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 100, 1, 4),
    _MscTraceSessionSessionState_Type()
)
mscTraceSessionSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionSessionState.setStatus("mandatory")


class _MscTraceSessionCallState_Type(Integer32):
    """Custom type mscTraceSessionCallState based on Integer32"""
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
        *(("calling", 2),
          ("clearing", 3),
          ("creatingVc", 1),
          ("dataTransfer", 6),
          ("enteringDataTransfer", 4),
          ("initializing", 0),
          ("reseting", 7),
          ("terminated", 9),
          ("terminating", 8),
          ("terminatingVc", 5))
    )


_MscTraceSessionCallState_Type.__name__ = "Integer32"
_MscTraceSessionCallState_Object = MibTableColumn
mscTraceSessionCallState = _MscTraceSessionCallState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 100, 1, 5),
    _MscTraceSessionCallState_Type()
)
mscTraceSessionCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionCallState.setStatus("mandatory")


class _MscTraceSessionQueueState_Type(Integer32):
    """Custom type mscTraceSessionQueueState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 2),
          ("full", 1),
          ("normal", 0))
    )


_MscTraceSessionQueueState_Type.__name__ = "Integer32"
_MscTraceSessionQueueState_Object = MibTableColumn
mscTraceSessionQueueState = _MscTraceSessionQueueState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 100, 1, 6),
    _MscTraceSessionQueueState_Type()
)
mscTraceSessionQueueState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionQueueState.setStatus("mandatory")


class _MscTraceSessionFramesQueued_Type(Unsigned32):
    """Custom type mscTraceSessionFramesQueued based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTraceSessionFramesQueued_Type.__name__ = "Unsigned32"
_MscTraceSessionFramesQueued_Object = MibTableColumn
mscTraceSessionFramesQueued = _MscTraceSessionFramesQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 100, 1, 7),
    _MscTraceSessionFramesQueued_Type()
)
mscTraceSessionFramesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFramesQueued.setStatus("mandatory")


class _MscTraceSessionFramesSent_Type(Unsigned32):
    """Custom type mscTraceSessionFramesSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTraceSessionFramesSent_Type.__name__ = "Unsigned32"
_MscTraceSessionFramesSent_Object = MibTableColumn
mscTraceSessionFramesSent = _MscTraceSessionFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 100, 1, 8),
    _MscTraceSessionFramesSent_Type()
)
mscTraceSessionFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFramesSent.setStatus("mandatory")


class _MscTraceSessionFramesDiscarded_Type(Unsigned32):
    """Custom type mscTraceSessionFramesDiscarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscTraceSessionFramesDiscarded_Type.__name__ = "Unsigned32"
_MscTraceSessionFramesDiscarded_Object = MibTableColumn
mscTraceSessionFramesDiscarded = _MscTraceSessionFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 106, 3, 100, 1, 9),
    _MscTraceSessionFramesDiscarded_Type()
)
mscTraceSessionFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTraceSessionFramesDiscarded.setStatus("mandatory")
_TraceBaseMIB_ObjectIdentity = ObjectIdentity
traceBaseMIB = _TraceBaseMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 60)
)
_TraceBaseGroup_ObjectIdentity = ObjectIdentity
traceBaseGroup = _TraceBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 60, 1)
)
_TraceBaseGroupCA_ObjectIdentity = ObjectIdentity
traceBaseGroupCA = _TraceBaseGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 60, 1, 1)
)
_TraceBaseGroupCA02_ObjectIdentity = ObjectIdentity
traceBaseGroupCA02 = _TraceBaseGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 60, 1, 1, 3)
)
_TraceBaseGroupCA02A_ObjectIdentity = ObjectIdentity
traceBaseGroupCA02A = _TraceBaseGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 60, 1, 1, 3, 2)
)
_TraceBaseCapabilities_ObjectIdentity = ObjectIdentity
traceBaseCapabilities = _TraceBaseCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 60, 3)
)
_TraceBaseCapabilitiesCA_ObjectIdentity = ObjectIdentity
traceBaseCapabilitiesCA = _TraceBaseCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 60, 3, 1)
)
_TraceBaseCapabilitiesCA02_ObjectIdentity = ObjectIdentity
traceBaseCapabilitiesCA02 = _TraceBaseCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 60, 3, 1, 3)
)
_TraceBaseCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
traceBaseCapabilitiesCA02A = _TraceBaseCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 60, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-TraceBaseMIB",
    **{"mscTrace": mscTrace,
       "mscTraceRowStatusTable": mscTraceRowStatusTable,
       "mscTraceRowStatusEntry": mscTraceRowStatusEntry,
       "mscTraceRowStatus": mscTraceRowStatus,
       "mscTraceComponentName": mscTraceComponentName,
       "mscTraceStorageType": mscTraceStorageType,
       "mscTraceIndex": mscTraceIndex,
       "mscTraceRcvr": mscTraceRcvr,
       "mscTraceRcvrRowStatusTable": mscTraceRcvrRowStatusTable,
       "mscTraceRcvrRowStatusEntry": mscTraceRcvrRowStatusEntry,
       "mscTraceRcvrRowStatus": mscTraceRcvrRowStatus,
       "mscTraceRcvrComponentName": mscTraceRcvrComponentName,
       "mscTraceRcvrStorageType": mscTraceRcvrStorageType,
       "mscTraceRcvrIndex": mscTraceRcvrIndex,
       "mscTraceSession": mscTraceSession,
       "mscTraceSessionRowStatusTable": mscTraceSessionRowStatusTable,
       "mscTraceSessionRowStatusEntry": mscTraceSessionRowStatusEntry,
       "mscTraceSessionRowStatus": mscTraceSessionRowStatus,
       "mscTraceSessionComponentName": mscTraceSessionComponentName,
       "mscTraceSessionStorageType": mscTraceSessionStorageType,
       "mscTraceSessionIndex": mscTraceSessionIndex,
       "mscTraceSessionOperationalTable": mscTraceSessionOperationalTable,
       "mscTraceSessionOperationalEntry": mscTraceSessionOperationalEntry,
       "mscTraceSessionServiceTraced": mscTraceSessionServiceTraced,
       "mscTraceSessionReceiver": mscTraceSessionReceiver,
       "mscTraceSessionSessionState": mscTraceSessionSessionState,
       "mscTraceSessionCallState": mscTraceSessionCallState,
       "mscTraceSessionQueueState": mscTraceSessionQueueState,
       "mscTraceSessionFramesQueued": mscTraceSessionFramesQueued,
       "mscTraceSessionFramesSent": mscTraceSessionFramesSent,
       "mscTraceSessionFramesDiscarded": mscTraceSessionFramesDiscarded,
       "traceBaseMIB": traceBaseMIB,
       "traceBaseGroup": traceBaseGroup,
       "traceBaseGroupCA": traceBaseGroupCA,
       "traceBaseGroupCA02": traceBaseGroupCA02,
       "traceBaseGroupCA02A": traceBaseGroupCA02A,
       "traceBaseCapabilities": traceBaseCapabilities,
       "traceBaseCapabilitiesCA": traceBaseCapabilitiesCA,
       "traceBaseCapabilitiesCA02": traceBaseCapabilitiesCA02,
       "traceBaseCapabilitiesCA02A": traceBaseCapabilitiesCA02A}
)
