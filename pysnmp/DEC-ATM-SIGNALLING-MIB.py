# SNMP MIB module (DEC-ATM-SIGNALLING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEC-ATM-SIGNALLING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:32 2024
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

(decMIBextension,) = mibBuilder.importSymbols(
    "DECATM-MIB",
    "decMIBextension")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

_DecAtmSignallingMIB_ObjectIdentity = ObjectIdentity
decAtmSignallingMIB = _DecAtmSignallingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34)
)
_DecAtmSignallingMIBObjects_ObjectIdentity = ObjectIdentity
decAtmSignallingMIBObjects = _DecAtmSignallingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1)
)
_DecSignallingGroup_ObjectIdentity = ObjectIdentity
decSignallingGroup = _DecSignallingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 1)
)
_DecSignallingConfigTable_Object = MibTable
decSignallingConfigTable = _DecSignallingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 1, 1)
)
if mibBuilder.loadTexts:
    decSignallingConfigTable.setStatus("mandatory")
_DecSignallingConfigEntry_Object = MibTableRow
decSignallingConfigEntry = _DecSignallingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 1, 1, 1)
)
decSignallingConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DEC-ATM-SIGNALLING-MIB", "decAtmSignallingIndex"),
)
if mibBuilder.loadTexts:
    decSignallingConfigEntry.setStatus("mandatory")
_DecAtmSignallingIndex_Type = Integer32
_DecAtmSignallingIndex_Object = MibTableColumn
decAtmSignallingIndex = _DecAtmSignallingIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 1, 1, 1, 1),
    _DecAtmSignallingIndex_Type()
)
decAtmSignallingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmSignallingIndex.setStatus("mandatory")


class _DecAtmSignallingMode_Type(Integer32):
    """Custom type decAtmSignallingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("autoConfigure", 1),
          ("pnni", 2),
          ("uni30", 3),
          ("uni31", 4),
          ("uni40", 5))
    )


_DecAtmSignallingMode_Type.__name__ = "Integer32"
_DecAtmSignallingMode_Object = MibTableColumn
decAtmSignallingMode = _DecAtmSignallingMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 1, 1, 1, 2),
    _DecAtmSignallingMode_Type()
)
decAtmSignallingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decAtmSignallingMode.setStatus("mandatory")
_DecQ2931Group_ObjectIdentity = ObjectIdentity
decQ2931Group = _DecQ2931Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2)
)
_DecQ2931MsgTable_Object = MibTable
decQ2931MsgTable = _DecQ2931MsgTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1)
)
if mibBuilder.loadTexts:
    decQ2931MsgTable.setStatus("mandatory")
_DecQ2931MsgEntry_Object = MibTableRow
decQ2931MsgEntry = _DecQ2931MsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1)
)
decQ2931MsgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DEC-ATM-SIGNALLING-MIB", "decAtmSignallingIndex"),
)
if mibBuilder.loadTexts:
    decQ2931MsgEntry.setStatus("mandatory")
_CallProceedingTx_Type = Counter32
_CallProceedingTx_Object = MibTableColumn
callProceedingTx = _CallProceedingTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 1),
    _CallProceedingTx_Type()
)
callProceedingTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callProceedingTx.setStatus("mandatory")
_CallProceedingRx_Type = Counter32
_CallProceedingRx_Object = MibTableColumn
callProceedingRx = _CallProceedingRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 2),
    _CallProceedingRx_Type()
)
callProceedingRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callProceedingRx.setStatus("mandatory")
_ConnectTx_Type = Counter32
_ConnectTx_Object = MibTableColumn
connectTx = _ConnectTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 3),
    _ConnectTx_Type()
)
connectTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectTx.setStatus("mandatory")
_ConnectRx_Type = Counter32
_ConnectRx_Object = MibTableColumn
connectRx = _ConnectRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 4),
    _ConnectRx_Type()
)
connectRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectRx.setStatus("mandatory")
_ConnectAcknowledgeTx_Type = Counter32
_ConnectAcknowledgeTx_Object = MibTableColumn
connectAcknowledgeTx = _ConnectAcknowledgeTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 5),
    _ConnectAcknowledgeTx_Type()
)
connectAcknowledgeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectAcknowledgeTx.setStatus("mandatory")
_ConnectAcknowledgeRx_Type = Counter32
_ConnectAcknowledgeRx_Object = MibTableColumn
connectAcknowledgeRx = _ConnectAcknowledgeRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 6),
    _ConnectAcknowledgeRx_Type()
)
connectAcknowledgeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectAcknowledgeRx.setStatus("mandatory")
_SetupTx_Type = Counter32
_SetupTx_Object = MibTableColumn
setupTx = _SetupTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 7),
    _SetupTx_Type()
)
setupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setupTx.setStatus("mandatory")
_SetupRx_Type = Counter32
_SetupRx_Object = MibTableColumn
setupRx = _SetupRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 8),
    _SetupRx_Type()
)
setupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setupRx.setStatus("mandatory")
_ReleaseTx_Type = Counter32
_ReleaseTx_Object = MibTableColumn
releaseTx = _ReleaseTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 9),
    _ReleaseTx_Type()
)
releaseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    releaseTx.setStatus("mandatory")
_ReleaseRx_Type = Counter32
_ReleaseRx_Object = MibTableColumn
releaseRx = _ReleaseRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 10),
    _ReleaseRx_Type()
)
releaseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    releaseRx.setStatus("mandatory")
_ReleaseCompleteTx_Type = Counter32
_ReleaseCompleteTx_Object = MibTableColumn
releaseCompleteTx = _ReleaseCompleteTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 11),
    _ReleaseCompleteTx_Type()
)
releaseCompleteTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    releaseCompleteTx.setStatus("mandatory")
_ReleaseCompleteRx_Type = Counter32
_ReleaseCompleteRx_Object = MibTableColumn
releaseCompleteRx = _ReleaseCompleteRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 12),
    _ReleaseCompleteRx_Type()
)
releaseCompleteRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    releaseCompleteRx.setStatus("mandatory")
_RestartTx_Type = Counter32
_RestartTx_Object = MibTableColumn
restartTx = _RestartTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 13),
    _RestartTx_Type()
)
restartTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restartTx.setStatus("mandatory")
_RestartRx_Type = Counter32
_RestartRx_Object = MibTableColumn
restartRx = _RestartRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 14),
    _RestartRx_Type()
)
restartRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restartRx.setStatus("mandatory")
_RestartAcknowledgeTx_Type = Counter32
_RestartAcknowledgeTx_Object = MibTableColumn
restartAcknowledgeTx = _RestartAcknowledgeTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 15),
    _RestartAcknowledgeTx_Type()
)
restartAcknowledgeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restartAcknowledgeTx.setStatus("mandatory")
_RestartAcknowledgeRx_Type = Counter32
_RestartAcknowledgeRx_Object = MibTableColumn
restartAcknowledgeRx = _RestartAcknowledgeRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 16),
    _RestartAcknowledgeRx_Type()
)
restartAcknowledgeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restartAcknowledgeRx.setStatus("mandatory")
_StatusTx_Type = Counter32
_StatusTx_Object = MibTableColumn
statusTx = _StatusTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 17),
    _StatusTx_Type()
)
statusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusTx.setStatus("mandatory")
_StatusRx_Type = Counter32
_StatusRx_Object = MibTableColumn
statusRx = _StatusRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 18),
    _StatusRx_Type()
)
statusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRx.setStatus("mandatory")
_StatusEnquiryTx_Type = Counter32
_StatusEnquiryTx_Object = MibTableColumn
statusEnquiryTx = _StatusEnquiryTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 19),
    _StatusEnquiryTx_Type()
)
statusEnquiryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEnquiryTx.setStatus("mandatory")
_StatusEnquiryRx_Type = Counter32
_StatusEnquiryRx_Object = MibTableColumn
statusEnquiryRx = _StatusEnquiryRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 20),
    _StatusEnquiryRx_Type()
)
statusEnquiryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEnquiryRx.setStatus("mandatory")
_AddPartyTx_Type = Counter32
_AddPartyTx_Object = MibTableColumn
addPartyTx = _AddPartyTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 21),
    _AddPartyTx_Type()
)
addPartyTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addPartyTx.setStatus("mandatory")
_AddPartyRx_Type = Counter32
_AddPartyRx_Object = MibTableColumn
addPartyRx = _AddPartyRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 22),
    _AddPartyRx_Type()
)
addPartyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addPartyRx.setStatus("mandatory")
_AddPartyAcknowledgeTx_Type = Counter32
_AddPartyAcknowledgeTx_Object = MibTableColumn
addPartyAcknowledgeTx = _AddPartyAcknowledgeTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 23),
    _AddPartyAcknowledgeTx_Type()
)
addPartyAcknowledgeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addPartyAcknowledgeTx.setStatus("mandatory")
_AddPartyAcknowledgeRx_Type = Counter32
_AddPartyAcknowledgeRx_Object = MibTableColumn
addPartyAcknowledgeRx = _AddPartyAcknowledgeRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 24),
    _AddPartyAcknowledgeRx_Type()
)
addPartyAcknowledgeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addPartyAcknowledgeRx.setStatus("mandatory")
_AddPartyRejectTx_Type = Counter32
_AddPartyRejectTx_Object = MibTableColumn
addPartyRejectTx = _AddPartyRejectTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 25),
    _AddPartyRejectTx_Type()
)
addPartyRejectTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addPartyRejectTx.setStatus("mandatory")
_AddPartyRejectRx_Type = Counter32
_AddPartyRejectRx_Object = MibTableColumn
addPartyRejectRx = _AddPartyRejectRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 26),
    _AddPartyRejectRx_Type()
)
addPartyRejectRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addPartyRejectRx.setStatus("mandatory")
_DropPartyTx_Type = Counter32
_DropPartyTx_Object = MibTableColumn
dropPartyTx = _DropPartyTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 27),
    _DropPartyTx_Type()
)
dropPartyTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropPartyTx.setStatus("mandatory")
_DropPartyRx_Type = Counter32
_DropPartyRx_Object = MibTableColumn
dropPartyRx = _DropPartyRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 28),
    _DropPartyRx_Type()
)
dropPartyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropPartyRx.setStatus("mandatory")
_DropPartyAcknowledgeTx_Type = Counter32
_DropPartyAcknowledgeTx_Object = MibTableColumn
dropPartyAcknowledgeTx = _DropPartyAcknowledgeTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 29),
    _DropPartyAcknowledgeTx_Type()
)
dropPartyAcknowledgeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropPartyAcknowledgeTx.setStatus("mandatory")
_DropPartyAcknowledgeRx_Type = Counter32
_DropPartyAcknowledgeRx_Object = MibTableColumn
dropPartyAcknowledgeRx = _DropPartyAcknowledgeRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 1, 1, 30),
    _DropPartyAcknowledgeRx_Type()
)
dropPartyAcknowledgeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropPartyAcknowledgeRx.setStatus("mandatory")
_DecQ2931StatusTable_Object = MibTable
decQ2931StatusTable = _DecQ2931StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 2)
)
if mibBuilder.loadTexts:
    decQ2931StatusTable.setStatus("mandatory")
_DecQ2931StatusEntry_Object = MibTableRow
decQ2931StatusEntry = _DecQ2931StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 2, 1)
)
decQ2931StatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DEC-ATM-SIGNALLING-MIB", "decAtmSignallingIndex"),
)
if mibBuilder.loadTexts:
    decQ2931StatusEntry.setStatus("mandatory")
_TotalConns_Type = Integer32
_TotalConns_Object = MibTableColumn
totalConns = _TotalConns_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 2, 1, 1),
    _TotalConns_Type()
)
totalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalConns.setStatus("mandatory")
_ActiveConns_Type = Integer32
_ActiveConns_Object = MibTableColumn
activeConns = _ActiveConns_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 2, 1, 2),
    _ActiveConns_Type()
)
activeConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeConns.setStatus("mandatory")
_LastTxCause_Type = Integer32
_LastTxCause_Object = MibTableColumn
lastTxCause = _LastTxCause_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 2, 1, 3),
    _LastTxCause_Type()
)
lastTxCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTxCause.setStatus("mandatory")
_LastTxDiagnostic_Type = Integer32
_LastTxDiagnostic_Object = MibTableColumn
lastTxDiagnostic = _LastTxDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 2, 1, 4),
    _LastTxDiagnostic_Type()
)
lastTxDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTxDiagnostic.setStatus("mandatory")
_LastRxCause_Type = Integer32
_LastRxCause_Object = MibTableColumn
lastRxCause = _LastRxCause_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 2, 1, 5),
    _LastRxCause_Type()
)
lastRxCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastRxCause.setStatus("mandatory")
_LastRxDiagnostic_Type = Integer32
_LastRxDiagnostic_Object = MibTableColumn
lastRxDiagnostic = _LastRxDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 2, 1, 6),
    _LastRxDiagnostic_Type()
)
lastRxDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastRxDiagnostic.setStatus("mandatory")
_DecQ2931TimerTable_Object = MibTable
decQ2931TimerTable = _DecQ2931TimerTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 3)
)
if mibBuilder.loadTexts:
    decQ2931TimerTable.setStatus("mandatory")
_DecQ2931TimerEntry_Object = MibTableRow
decQ2931TimerEntry = _DecQ2931TimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 3, 1)
)
decQ2931TimerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DEC-ATM-SIGNALLING-MIB", "decAtmSignallingIndex"),
)
if mibBuilder.loadTexts:
    decQ2931TimerEntry.setStatus("mandatory")


class _T303_Type(Integer32):
    """Custom type t303 based on Integer32"""
    defaultValue = 4


_T303_Object = MibTableColumn
t303 = _T303_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 3, 1, 1),
    _T303_Type()
)
t303.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t303.setStatus("mandatory")


class _T308_Type(Integer32):
    """Custom type t308 based on Integer32"""
    defaultValue = 30


_T308_Object = MibTableColumn
t308 = _T308_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 3, 1, 2),
    _T308_Type()
)
t308.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t308.setStatus("mandatory")


class _T309_Type(Integer32):
    """Custom type t309 based on Integer32"""
    defaultValue = 90


_T309_Object = MibTableColumn
t309 = _T309_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 3, 1, 3),
    _T309_Type()
)
t309.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t309.setStatus("mandatory")


class _T310_Type(Integer32):
    """Custom type t310 based on Integer32"""
    defaultValue = 10


_T310_Object = MibTableColumn
t310 = _T310_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 3, 1, 4),
    _T310_Type()
)
t310.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t310.setStatus("mandatory")


class _T313_Type(Integer32):
    """Custom type t313 based on Integer32"""
    defaultValue = 4


_T313_Object = MibTableColumn
t313 = _T313_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 3, 1, 5),
    _T313_Type()
)
t313.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t313.setStatus("mandatory")


class _T316_Type(Integer32):
    """Custom type t316 based on Integer32"""
    defaultValue = 120


_T316_Object = MibTableColumn
t316 = _T316_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 3, 1, 6),
    _T316_Type()
)
t316.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t316.setStatus("mandatory")
_T317_Type = Integer32
_T317_Object = MibTableColumn
t317 = _T317_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 3, 1, 7),
    _T317_Type()
)
t317.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t317.setStatus("mandatory")


class _T322_Type(Integer32):
    """Custom type t322 based on Integer32"""
    defaultValue = 4


_T322_Object = MibTableColumn
t322 = _T322_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 3, 1, 8),
    _T322_Type()
)
t322.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t322.setStatus("mandatory")


class _T398_Type(Integer32):
    """Custom type t398 based on Integer32"""
    defaultValue = 4


_T398_Object = MibTableColumn
t398 = _T398_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 3, 1, 9),
    _T398_Type()
)
t398.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t398.setStatus("mandatory")


class _T399_Type(Integer32):
    """Custom type t399 based on Integer32"""
    defaultValue = 14


_T399_Object = MibTableColumn
t399 = _T399_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 2, 3, 1, 10),
    _T399_Type()
)
t399.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t399.setStatus("mandatory")
_DecQSaalGroup_ObjectIdentity = ObjectIdentity
decQSaalGroup = _DecQSaalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3)
)
_DecQSaalMsgTable_Object = MibTable
decQSaalMsgTable = _DecQSaalMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1)
)
if mibBuilder.loadTexts:
    decQSaalMsgTable.setStatus("mandatory")
_DecQSaalMsgEntry_Object = MibTableRow
decQSaalMsgEntry = _DecQSaalMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1)
)
decQSaalMsgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DEC-ATM-SIGNALLING-MIB", "decAtmSignallingIndex"),
)
if mibBuilder.loadTexts:
    decQSaalMsgEntry.setStatus("mandatory")
_TxDiscardedSdus_Type = Counter32
_TxDiscardedSdus_Object = MibTableColumn
txDiscardedSdus = _TxDiscardedSdus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 1),
    _TxDiscardedSdus_Type()
)
txDiscardedSdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDiscardedSdus.setStatus("mandatory")
_RxErrorPdus_Type = Counter32
_RxErrorPdus_Object = MibTableColumn
rxErrorPdus = _RxErrorPdus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 2),
    _RxErrorPdus_Type()
)
rxErrorPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxErrorPdus.setStatus("mandatory")
_TxErrorPdus_Type = Counter32
_TxErrorPdus_Object = MibTableColumn
txErrorPdus = _TxErrorPdus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 3),
    _TxErrorPdus_Type()
)
txErrorPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txErrorPdus.setStatus("mandatory")
_RxDiscardedPdus_Type = Counter32
_RxDiscardedPdus_Object = MibTableColumn
rxDiscardedPdus = _RxDiscardedPdus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 4),
    _RxDiscardedPdus_Type()
)
rxDiscardedPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDiscardedPdus.setStatus("mandatory")
_TxDiscardedPdus_Type = Counter32
_TxDiscardedPdus_Object = MibTableColumn
txDiscardedPdus = _TxDiscardedPdus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 5),
    _TxDiscardedPdus_Type()
)
txDiscardedPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDiscardedPdus.setStatus("mandatory")
_BgnTx_Type = Counter32
_BgnTx_Object = MibTableColumn
bgnTx = _BgnTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 6),
    _BgnTx_Type()
)
bgnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgnTx.setStatus("mandatory")
_BgnRx_Type = Counter32
_BgnRx_Object = MibTableColumn
bgnRx = _BgnRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 7),
    _BgnRx_Type()
)
bgnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgnRx.setStatus("mandatory")
_BgakTx_Type = Counter32
_BgakTx_Object = MibTableColumn
bgakTx = _BgakTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 8),
    _BgakTx_Type()
)
bgakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgakTx.setStatus("mandatory")
_BgakRx_Type = Counter32
_BgakRx_Object = MibTableColumn
bgakRx = _BgakRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 9),
    _BgakRx_Type()
)
bgakRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgakRx.setStatus("mandatory")
_EndTx_Type = Counter32
_EndTx_Object = MibTableColumn
endTx = _EndTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 10),
    _EndTx_Type()
)
endTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endTx.setStatus("mandatory")
_EndRx_Type = Counter32
_EndRx_Object = MibTableColumn
endRx = _EndRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 11),
    _EndRx_Type()
)
endRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endRx.setStatus("mandatory")
_EndakTx_Type = Counter32
_EndakTx_Object = MibTableColumn
endakTx = _EndakTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 12),
    _EndakTx_Type()
)
endakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endakTx.setStatus("mandatory")
_EndakRx_Type = Counter32
_EndakRx_Object = MibTableColumn
endakRx = _EndakRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 13),
    _EndakRx_Type()
)
endakRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endakRx.setStatus("mandatory")
_RsTx_Type = Counter32
_RsTx_Object = MibTableColumn
rsTx = _RsTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 14),
    _RsTx_Type()
)
rsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTx.setStatus("mandatory")
_RsRx_Type = Counter32
_RsRx_Object = MibTableColumn
rsRx = _RsRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 15),
    _RsRx_Type()
)
rsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRx.setStatus("mandatory")
_RsakTx_Type = Counter32
_RsakTx_Object = MibTableColumn
rsakTx = _RsakTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 16),
    _RsakTx_Type()
)
rsakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsakTx.setStatus("mandatory")
_RsakRx_Type = Counter32
_RsakRx_Object = MibTableColumn
rsakRx = _RsakRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 17),
    _RsakRx_Type()
)
rsakRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsakRx.setStatus("mandatory")
_BgrejTx_Type = Counter32
_BgrejTx_Object = MibTableColumn
bgrejTx = _BgrejTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 18),
    _BgrejTx_Type()
)
bgrejTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgrejTx.setStatus("mandatory")
_BgrejRx_Type = Counter32
_BgrejRx_Object = MibTableColumn
bgrejRx = _BgrejRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 19),
    _BgrejRx_Type()
)
bgrejRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgrejRx.setStatus("mandatory")
_SdTx_Type = Counter32
_SdTx_Object = MibTableColumn
sdTx = _SdTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 20),
    _SdTx_Type()
)
sdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdTx.setStatus("mandatory")
_SdRx_Type = Counter32
_SdRx_Object = MibTableColumn
sdRx = _SdRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 21),
    _SdRx_Type()
)
sdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdRx.setStatus("mandatory")
_SdpTx_Type = Counter32
_SdpTx_Object = MibTableColumn
sdpTx = _SdpTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 22),
    _SdpTx_Type()
)
sdpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpTx.setStatus("mandatory")
_SdpRx_Type = Counter32
_SdpRx_Object = MibTableColumn
sdpRx = _SdpRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 23),
    _SdpRx_Type()
)
sdpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpRx.setStatus("mandatory")
_ErTx_Type = Counter32
_ErTx_Object = MibTableColumn
erTx = _ErTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 24),
    _ErTx_Type()
)
erTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erTx.setStatus("mandatory")
_ErRx_Type = Counter32
_ErRx_Object = MibTableColumn
erRx = _ErRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 25),
    _ErRx_Type()
)
erRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erRx.setStatus("mandatory")
_PollTx_Type = Counter32
_PollTx_Object = MibTableColumn
pollTx = _PollTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 26),
    _PollTx_Type()
)
pollTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollTx.setStatus("mandatory")
_PollRx_Type = Counter32
_PollRx_Object = MibTableColumn
pollRx = _PollRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 27),
    _PollRx_Type()
)
pollRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollRx.setStatus("mandatory")
_StatTx_Type = Counter32
_StatTx_Object = MibTableColumn
statTx = _StatTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 28),
    _StatTx_Type()
)
statTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTx.setStatus("mandatory")
_StatRx_Type = Counter32
_StatRx_Object = MibTableColumn
statRx = _StatRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 29),
    _StatRx_Type()
)
statRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRx.setStatus("mandatory")
_UstatTx_Type = Counter32
_UstatTx_Object = MibTableColumn
ustatTx = _UstatTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 30),
    _UstatTx_Type()
)
ustatTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ustatTx.setStatus("mandatory")
_UstatRx_Type = Counter32
_UstatRx_Object = MibTableColumn
ustatRx = _UstatRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 31),
    _UstatRx_Type()
)
ustatRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ustatRx.setStatus("mandatory")
_UdTx_Type = Counter32
_UdTx_Object = MibTableColumn
udTx = _UdTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 32),
    _UdTx_Type()
)
udTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udTx.setStatus("mandatory")
_UdRx_Type = Counter32
_UdRx_Object = MibTableColumn
udRx = _UdRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 33),
    _UdRx_Type()
)
udRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udRx.setStatus("mandatory")
_MdTx_Type = Counter32
_MdTx_Object = MibTableColumn
mdTx = _MdTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 34),
    _MdTx_Type()
)
mdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdTx.setStatus("mandatory")
_MdRx_Type = Counter32
_MdRx_Object = MibTableColumn
mdRx = _MdRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 35),
    _MdRx_Type()
)
mdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRx.setStatus("mandatory")
_ErakTx_Type = Counter32
_ErakTx_Object = MibTableColumn
erakTx = _ErakTx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 36),
    _ErakTx_Type()
)
erakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erakTx.setStatus("mandatory")
_ErakRx_Type = Counter32
_ErakRx_Object = MibTableColumn
erakRx = _ErakRx_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 34, 1, 3, 1, 1, 37),
    _ErakRx_Type()
)
erakRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erakRx.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEC-ATM-SIGNALLING-MIB",
    **{"decAtmSignallingMIB": decAtmSignallingMIB,
       "decAtmSignallingMIBObjects": decAtmSignallingMIBObjects,
       "decSignallingGroup": decSignallingGroup,
       "decSignallingConfigTable": decSignallingConfigTable,
       "decSignallingConfigEntry": decSignallingConfigEntry,
       "decAtmSignallingIndex": decAtmSignallingIndex,
       "decAtmSignallingMode": decAtmSignallingMode,
       "decQ2931Group": decQ2931Group,
       "decQ2931MsgTable": decQ2931MsgTable,
       "decQ2931MsgEntry": decQ2931MsgEntry,
       "callProceedingTx": callProceedingTx,
       "callProceedingRx": callProceedingRx,
       "connectTx": connectTx,
       "connectRx": connectRx,
       "connectAcknowledgeTx": connectAcknowledgeTx,
       "connectAcknowledgeRx": connectAcknowledgeRx,
       "setupTx": setupTx,
       "setupRx": setupRx,
       "releaseTx": releaseTx,
       "releaseRx": releaseRx,
       "releaseCompleteTx": releaseCompleteTx,
       "releaseCompleteRx": releaseCompleteRx,
       "restartTx": restartTx,
       "restartRx": restartRx,
       "restartAcknowledgeTx": restartAcknowledgeTx,
       "restartAcknowledgeRx": restartAcknowledgeRx,
       "statusTx": statusTx,
       "statusRx": statusRx,
       "statusEnquiryTx": statusEnquiryTx,
       "statusEnquiryRx": statusEnquiryRx,
       "addPartyTx": addPartyTx,
       "addPartyRx": addPartyRx,
       "addPartyAcknowledgeTx": addPartyAcknowledgeTx,
       "addPartyAcknowledgeRx": addPartyAcknowledgeRx,
       "addPartyRejectTx": addPartyRejectTx,
       "addPartyRejectRx": addPartyRejectRx,
       "dropPartyTx": dropPartyTx,
       "dropPartyRx": dropPartyRx,
       "dropPartyAcknowledgeTx": dropPartyAcknowledgeTx,
       "dropPartyAcknowledgeRx": dropPartyAcknowledgeRx,
       "decQ2931StatusTable": decQ2931StatusTable,
       "decQ2931StatusEntry": decQ2931StatusEntry,
       "totalConns": totalConns,
       "activeConns": activeConns,
       "lastTxCause": lastTxCause,
       "lastTxDiagnostic": lastTxDiagnostic,
       "lastRxCause": lastRxCause,
       "lastRxDiagnostic": lastRxDiagnostic,
       "decQ2931TimerTable": decQ2931TimerTable,
       "decQ2931TimerEntry": decQ2931TimerEntry,
       "t303": t303,
       "t308": t308,
       "t309": t309,
       "t310": t310,
       "t313": t313,
       "t316": t316,
       "t317": t317,
       "t322": t322,
       "t398": t398,
       "t399": t399,
       "decQSaalGroup": decQSaalGroup,
       "decQSaalMsgTable": decQSaalMsgTable,
       "decQSaalMsgEntry": decQSaalMsgEntry,
       "txDiscardedSdus": txDiscardedSdus,
       "rxErrorPdus": rxErrorPdus,
       "txErrorPdus": txErrorPdus,
       "rxDiscardedPdus": rxDiscardedPdus,
       "txDiscardedPdus": txDiscardedPdus,
       "bgnTx": bgnTx,
       "bgnRx": bgnRx,
       "bgakTx": bgakTx,
       "bgakRx": bgakRx,
       "endTx": endTx,
       "endRx": endRx,
       "endakTx": endakTx,
       "endakRx": endakRx,
       "rsTx": rsTx,
       "rsRx": rsRx,
       "rsakTx": rsakTx,
       "rsakRx": rsakRx,
       "bgrejTx": bgrejTx,
       "bgrejRx": bgrejRx,
       "sdTx": sdTx,
       "sdRx": sdRx,
       "sdpTx": sdpTx,
       "sdpRx": sdpRx,
       "erTx": erTx,
       "erRx": erRx,
       "pollTx": pollTx,
       "pollRx": pollRx,
       "statTx": statTx,
       "statRx": statRx,
       "ustatTx": ustatTx,
       "ustatRx": ustatRx,
       "udTx": udTx,
       "udRx": udRx,
       "mdTx": mdTx,
       "mdRx": mdRx,
       "erakTx": erakTx,
       "erakRx": erakRx}
)
