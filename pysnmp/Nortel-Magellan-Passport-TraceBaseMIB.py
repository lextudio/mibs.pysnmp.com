# SNMP MIB module (Nortel-Magellan-Passport-TraceBaseMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-TraceBaseMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:42 2024
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
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiStringIndex,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiStringIndex",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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

_Trace_ObjectIdentity = ObjectIdentity
trace = _Trace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106)
)
_TraceRowStatusTable_Object = MibTable
traceRowStatusTable = _TraceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 1)
)
if mibBuilder.loadTexts:
    traceRowStatusTable.setStatus("mandatory")
_TraceRowStatusEntry_Object = MibTableRow
traceRowStatusEntry = _TraceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 1, 1)
)
traceRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
)
if mibBuilder.loadTexts:
    traceRowStatusEntry.setStatus("mandatory")
_TraceRowStatus_Type = RowStatus
_TraceRowStatus_Object = MibTableColumn
traceRowStatus = _TraceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 1, 1, 1),
    _TraceRowStatus_Type()
)
traceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRowStatus.setStatus("mandatory")
_TraceComponentName_Type = DisplayString
_TraceComponentName_Object = MibTableColumn
traceComponentName = _TraceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 1, 1, 2),
    _TraceComponentName_Type()
)
traceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceComponentName.setStatus("mandatory")
_TraceStorageType_Type = StorageType
_TraceStorageType_Object = MibTableColumn
traceStorageType = _TraceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 1, 1, 4),
    _TraceStorageType_Type()
)
traceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceStorageType.setStatus("mandatory")
_TraceIndex_Type = NonReplicated
_TraceIndex_Object = MibTableColumn
traceIndex = _TraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 1, 1, 10),
    _TraceIndex_Type()
)
traceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceIndex.setStatus("mandatory")
_TraceRcvr_ObjectIdentity = ObjectIdentity
traceRcvr = _TraceRcvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2)
)
_TraceRcvrRowStatusTable_Object = MibTable
traceRcvrRowStatusTable = _TraceRcvrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 1)
)
if mibBuilder.loadTexts:
    traceRcvrRowStatusTable.setStatus("mandatory")
_TraceRcvrRowStatusEntry_Object = MibTableRow
traceRcvrRowStatusEntry = _TraceRcvrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 1, 1)
)
traceRcvrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceRcvrIndex"),
)
if mibBuilder.loadTexts:
    traceRcvrRowStatusEntry.setStatus("mandatory")
_TraceRcvrRowStatus_Type = RowStatus
_TraceRcvrRowStatus_Object = MibTableColumn
traceRcvrRowStatus = _TraceRcvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 1, 1, 1),
    _TraceRcvrRowStatus_Type()
)
traceRcvrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceRcvrRowStatus.setStatus("mandatory")
_TraceRcvrComponentName_Type = DisplayString
_TraceRcvrComponentName_Object = MibTableColumn
traceRcvrComponentName = _TraceRcvrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 1, 1, 2),
    _TraceRcvrComponentName_Type()
)
traceRcvrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrComponentName.setStatus("mandatory")
_TraceRcvrStorageType_Type = StorageType
_TraceRcvrStorageType_Object = MibTableColumn
traceRcvrStorageType = _TraceRcvrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 1, 1, 4),
    _TraceRcvrStorageType_Type()
)
traceRcvrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRcvrStorageType.setStatus("mandatory")


class _TraceRcvrIndex_Type(AsciiStringIndex):
    """Custom type traceRcvrIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_TraceRcvrIndex_Type.__name__ = "AsciiStringIndex"
_TraceRcvrIndex_Object = MibTableColumn
traceRcvrIndex = _TraceRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 2, 1, 1, 10),
    _TraceRcvrIndex_Type()
)
traceRcvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRcvrIndex.setStatus("mandatory")
_TraceSession_ObjectIdentity = ObjectIdentity
traceSession = _TraceSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3)
)
_TraceSessionRowStatusTable_Object = MibTable
traceSessionRowStatusTable = _TraceSessionRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 1)
)
if mibBuilder.loadTexts:
    traceSessionRowStatusTable.setStatus("mandatory")
_TraceSessionRowStatusEntry_Object = MibTableRow
traceSessionRowStatusEntry = _TraceSessionRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 1, 1)
)
traceSessionRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceSessionIndex"),
)
if mibBuilder.loadTexts:
    traceSessionRowStatusEntry.setStatus("mandatory")
_TraceSessionRowStatus_Type = RowStatus
_TraceSessionRowStatus_Object = MibTableColumn
traceSessionRowStatus = _TraceSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 1, 1, 1),
    _TraceSessionRowStatus_Type()
)
traceSessionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionRowStatus.setStatus("mandatory")
_TraceSessionComponentName_Type = DisplayString
_TraceSessionComponentName_Object = MibTableColumn
traceSessionComponentName = _TraceSessionComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 1, 1, 2),
    _TraceSessionComponentName_Type()
)
traceSessionComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionComponentName.setStatus("mandatory")
_TraceSessionStorageType_Type = StorageType
_TraceSessionStorageType_Object = MibTableColumn
traceSessionStorageType = _TraceSessionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 1, 1, 4),
    _TraceSessionStorageType_Type()
)
traceSessionStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionStorageType.setStatus("mandatory")


class _TraceSessionIndex_Type(Integer32):
    """Custom type traceSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TraceSessionIndex_Type.__name__ = "Integer32"
_TraceSessionIndex_Object = MibTableColumn
traceSessionIndex = _TraceSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 1, 1, 10),
    _TraceSessionIndex_Type()
)
traceSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceSessionIndex.setStatus("mandatory")
_TraceSessionOperationalTable_Object = MibTable
traceSessionOperationalTable = _TraceSessionOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 100)
)
if mibBuilder.loadTexts:
    traceSessionOperationalTable.setStatus("mandatory")
_TraceSessionOperationalEntry_Object = MibTableRow
traceSessionOperationalEntry = _TraceSessionOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 100, 1)
)
traceSessionOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceIndex"),
    (0, "Nortel-Magellan-Passport-TraceBaseMIB", "traceSessionIndex"),
)
if mibBuilder.loadTexts:
    traceSessionOperationalEntry.setStatus("mandatory")
_TraceSessionServiceTraced_Type = RowPointer
_TraceSessionServiceTraced_Object = MibTableColumn
traceSessionServiceTraced = _TraceSessionServiceTraced_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 100, 1, 2),
    _TraceSessionServiceTraced_Type()
)
traceSessionServiceTraced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionServiceTraced.setStatus("mandatory")
_TraceSessionReceiver_Type = RowPointer
_TraceSessionReceiver_Object = MibTableColumn
traceSessionReceiver = _TraceSessionReceiver_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 100, 1, 3),
    _TraceSessionReceiver_Type()
)
traceSessionReceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionReceiver.setStatus("mandatory")


class _TraceSessionSessionState_Type(Integer32):
    """Custom type traceSessionSessionState based on Integer32"""
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


_TraceSessionSessionState_Type.__name__ = "Integer32"
_TraceSessionSessionState_Object = MibTableColumn
traceSessionSessionState = _TraceSessionSessionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 100, 1, 4),
    _TraceSessionSessionState_Type()
)
traceSessionSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionSessionState.setStatus("mandatory")


class _TraceSessionCallState_Type(Integer32):
    """Custom type traceSessionCallState based on Integer32"""
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


_TraceSessionCallState_Type.__name__ = "Integer32"
_TraceSessionCallState_Object = MibTableColumn
traceSessionCallState = _TraceSessionCallState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 100, 1, 5),
    _TraceSessionCallState_Type()
)
traceSessionCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionCallState.setStatus("mandatory")


class _TraceSessionQueueState_Type(Integer32):
    """Custom type traceSessionQueueState based on Integer32"""
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


_TraceSessionQueueState_Type.__name__ = "Integer32"
_TraceSessionQueueState_Object = MibTableColumn
traceSessionQueueState = _TraceSessionQueueState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 100, 1, 6),
    _TraceSessionQueueState_Type()
)
traceSessionQueueState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionQueueState.setStatus("mandatory")


class _TraceSessionFramesQueued_Type(Unsigned32):
    """Custom type traceSessionFramesQueued based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TraceSessionFramesQueued_Type.__name__ = "Unsigned32"
_TraceSessionFramesQueued_Object = MibTableColumn
traceSessionFramesQueued = _TraceSessionFramesQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 100, 1, 7),
    _TraceSessionFramesQueued_Type()
)
traceSessionFramesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFramesQueued.setStatus("mandatory")


class _TraceSessionFramesSent_Type(Unsigned32):
    """Custom type traceSessionFramesSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TraceSessionFramesSent_Type.__name__ = "Unsigned32"
_TraceSessionFramesSent_Object = MibTableColumn
traceSessionFramesSent = _TraceSessionFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 100, 1, 8),
    _TraceSessionFramesSent_Type()
)
traceSessionFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFramesSent.setStatus("mandatory")


class _TraceSessionFramesDiscarded_Type(Unsigned32):
    """Custom type traceSessionFramesDiscarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TraceSessionFramesDiscarded_Type.__name__ = "Unsigned32"
_TraceSessionFramesDiscarded_Object = MibTableColumn
traceSessionFramesDiscarded = _TraceSessionFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 106, 3, 100, 1, 9),
    _TraceSessionFramesDiscarded_Type()
)
traceSessionFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceSessionFramesDiscarded.setStatus("mandatory")
_TraceBaseMIB_ObjectIdentity = ObjectIdentity
traceBaseMIB = _TraceBaseMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 60)
)
_TraceBaseGroup_ObjectIdentity = ObjectIdentity
traceBaseGroup = _TraceBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 60, 1)
)
_TraceBaseGroupBD_ObjectIdentity = ObjectIdentity
traceBaseGroupBD = _TraceBaseGroupBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 60, 1, 4)
)
_TraceBaseGroupBD00_ObjectIdentity = ObjectIdentity
traceBaseGroupBD00 = _TraceBaseGroupBD00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 60, 1, 4, 1)
)
_TraceBaseGroupBD00A_ObjectIdentity = ObjectIdentity
traceBaseGroupBD00A = _TraceBaseGroupBD00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 60, 1, 4, 1, 2)
)
_TraceBaseCapabilities_ObjectIdentity = ObjectIdentity
traceBaseCapabilities = _TraceBaseCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 60, 3)
)
_TraceBaseCapabilitiesBD_ObjectIdentity = ObjectIdentity
traceBaseCapabilitiesBD = _TraceBaseCapabilitiesBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 60, 3, 4)
)
_TraceBaseCapabilitiesBD00_ObjectIdentity = ObjectIdentity
traceBaseCapabilitiesBD00 = _TraceBaseCapabilitiesBD00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 60, 3, 4, 1)
)
_TraceBaseCapabilitiesBD00A_ObjectIdentity = ObjectIdentity
traceBaseCapabilitiesBD00A = _TraceBaseCapabilitiesBD00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 60, 3, 4, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-TraceBaseMIB",
    **{"trace": trace,
       "traceRowStatusTable": traceRowStatusTable,
       "traceRowStatusEntry": traceRowStatusEntry,
       "traceRowStatus": traceRowStatus,
       "traceComponentName": traceComponentName,
       "traceStorageType": traceStorageType,
       "traceIndex": traceIndex,
       "traceRcvr": traceRcvr,
       "traceRcvrRowStatusTable": traceRcvrRowStatusTable,
       "traceRcvrRowStatusEntry": traceRcvrRowStatusEntry,
       "traceRcvrRowStatus": traceRcvrRowStatus,
       "traceRcvrComponentName": traceRcvrComponentName,
       "traceRcvrStorageType": traceRcvrStorageType,
       "traceRcvrIndex": traceRcvrIndex,
       "traceSession": traceSession,
       "traceSessionRowStatusTable": traceSessionRowStatusTable,
       "traceSessionRowStatusEntry": traceSessionRowStatusEntry,
       "traceSessionRowStatus": traceSessionRowStatus,
       "traceSessionComponentName": traceSessionComponentName,
       "traceSessionStorageType": traceSessionStorageType,
       "traceSessionIndex": traceSessionIndex,
       "traceSessionOperationalTable": traceSessionOperationalTable,
       "traceSessionOperationalEntry": traceSessionOperationalEntry,
       "traceSessionServiceTraced": traceSessionServiceTraced,
       "traceSessionReceiver": traceSessionReceiver,
       "traceSessionSessionState": traceSessionSessionState,
       "traceSessionCallState": traceSessionCallState,
       "traceSessionQueueState": traceSessionQueueState,
       "traceSessionFramesQueued": traceSessionFramesQueued,
       "traceSessionFramesSent": traceSessionFramesSent,
       "traceSessionFramesDiscarded": traceSessionFramesDiscarded,
       "traceBaseMIB": traceBaseMIB,
       "traceBaseGroup": traceBaseGroup,
       "traceBaseGroupBD": traceBaseGroupBD,
       "traceBaseGroupBD00": traceBaseGroupBD00,
       "traceBaseGroupBD00A": traceBaseGroupBD00A,
       "traceBaseCapabilities": traceBaseCapabilities,
       "traceBaseCapabilitiesBD": traceBaseCapabilitiesBD,
       "traceBaseCapabilitiesBD00": traceBaseCapabilitiesBD00,
       "traceBaseCapabilitiesBD00A": traceBaseCapabilitiesBD00A}
)
