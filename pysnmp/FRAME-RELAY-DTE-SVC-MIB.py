# SNMP MIB module (FRAME-RELAY-DTE-SVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FRAME-RELAY-DTE-SVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:19 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(DLCI,
 frame_relay) = mibBuilder.importSymbols(
    "RFC1315-MIB",
    "DLCI",
    "frame-relay")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(DisplayString,
 RowStatus,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString",
    "RowStatus",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrameRelayDteSvc_ObjectIdentity = ObjectIdentity
frameRelayDteSvc = _FrameRelayDteSvc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 32, 7)
)
_FrDteSvc_ObjectIdentity = ObjectIdentity
frDteSvc = _FrDteSvc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1)
)
_FrSvcDlcmiTable_Object = MibTable
frSvcDlcmiTable = _FrSvcDlcmiTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1)
)
if mibBuilder.loadTexts:
    frSvcDlcmiTable.setStatus("mandatory")
_FrSvcDlcmiEntry_Object = MibTableRow
frSvcDlcmiEntry = _FrSvcDlcmiEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1)
)
frSvcDlcmiEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-SVC-MIB", "frSvcDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    frSvcDlcmiEntry.setStatus("mandatory")
_FrSvcDlcmiIfIndex_Type = InterfaceIndex
_FrSvcDlcmiIfIndex_Object = MibTableColumn
frSvcDlcmiIfIndex = _FrSvcDlcmiIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 1),
    _FrSvcDlcmiIfIndex_Type()
)
frSvcDlcmiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcDlcmiIfIndex.setStatus("mandatory")


class _FrSvcDlcmiState_Type(Integer32):
    """Custom type frSvcDlcmiState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("q933SVC", 1),
          ("x36", 2))
    )


_FrSvcDlcmiState_Type.__name__ = "Integer32"
_FrSvcDlcmiState_Object = MibTableColumn
frSvcDlcmiState = _FrSvcDlcmiState_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 2),
    _FrSvcDlcmiState_Type()
)
frSvcDlcmiState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcDlcmiState.setStatus("mandatory")
_FrSvcDlcmiMaxNumCalls_Type = Integer32
_FrSvcDlcmiMaxNumCalls_Object = MibTableColumn
frSvcDlcmiMaxNumCalls = _FrSvcDlcmiMaxNumCalls_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 3),
    _FrSvcDlcmiMaxNumCalls_Type()
)
frSvcDlcmiMaxNumCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcDlcmiMaxNumCalls.setStatus("mandatory")


class _FrSvcDlcmiCallSetupTimer_Type(Integer32):
    """Custom type frSvcDlcmiCallSetupTimer based on Integer32"""
    defaultValue = 4


_FrSvcDlcmiCallSetupTimer_Object = MibTableColumn
frSvcDlcmiCallSetupTimer = _FrSvcDlcmiCallSetupTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 4),
    _FrSvcDlcmiCallSetupTimer_Type()
)
frSvcDlcmiCallSetupTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcDlcmiCallSetupTimer.setStatus("mandatory")


class _FrSvcDlcmiCallProceedingTimer_Type(Integer32):
    """Custom type frSvcDlcmiCallProceedingTimer based on Integer32"""
    defaultValue = 10


_FrSvcDlcmiCallProceedingTimer_Object = MibTableColumn
frSvcDlcmiCallProceedingTimer = _FrSvcDlcmiCallProceedingTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 5),
    _FrSvcDlcmiCallProceedingTimer_Type()
)
frSvcDlcmiCallProceedingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcDlcmiCallProceedingTimer.setStatus("mandatory")


class _FrSvcDlcmiCallDisconnectTimer_Type(Integer32):
    """Custom type frSvcDlcmiCallDisconnectTimer based on Integer32"""
    defaultValue = 30


_FrSvcDlcmiCallDisconnectTimer_Object = MibTableColumn
frSvcDlcmiCallDisconnectTimer = _FrSvcDlcmiCallDisconnectTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 6),
    _FrSvcDlcmiCallDisconnectTimer_Type()
)
frSvcDlcmiCallDisconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcDlcmiCallDisconnectTimer.setStatus("mandatory")


class _FrSvcDlcmiCallReleaseTimer_Type(Integer32):
    """Custom type frSvcDlcmiCallReleaseTimer based on Integer32"""
    defaultValue = 4


_FrSvcDlcmiCallReleaseTimer_Object = MibTableColumn
frSvcDlcmiCallReleaseTimer = _FrSvcDlcmiCallReleaseTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 7),
    _FrSvcDlcmiCallReleaseTimer_Type()
)
frSvcDlcmiCallReleaseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcDlcmiCallReleaseTimer.setStatus("mandatory")


class _FrSvcDlcmiStatusEnquiryTimer_Type(Integer32):
    """Custom type frSvcDlcmiStatusEnquiryTimer based on Integer32"""
    defaultValue = 4


_FrSvcDlcmiStatusEnquiryTimer_Object = MibTableColumn
frSvcDlcmiStatusEnquiryTimer = _FrSvcDlcmiStatusEnquiryTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 8),
    _FrSvcDlcmiStatusEnquiryTimer_Type()
)
frSvcDlcmiStatusEnquiryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcDlcmiStatusEnquiryTimer.setStatus("mandatory")
_FrSvcDlcmiErrorThreshold_Type = Integer32
_FrSvcDlcmiErrorThreshold_Object = MibTableColumn
frSvcDlcmiErrorThreshold = _FrSvcDlcmiErrorThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 9),
    _FrSvcDlcmiErrorThreshold_Type()
)
frSvcDlcmiErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcDlcmiErrorThreshold.setStatus("mandatory")


class _FrSvcDlcmiResetSentTimer_Type(Integer32):
    """Custom type frSvcDlcmiResetSentTimer based on Integer32"""
    defaultValue = 120


_FrSvcDlcmiResetSentTimer_Object = MibTableColumn
frSvcDlcmiResetSentTimer = _FrSvcDlcmiResetSentTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 10),
    _FrSvcDlcmiResetSentTimer_Type()
)
frSvcDlcmiResetSentTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcDlcmiResetSentTimer.setStatus("mandatory")
_FrSvcDlcmiResetAckTimer_Type = Integer32
_FrSvcDlcmiResetAckTimer_Object = MibTableColumn
frSvcDlcmiResetAckTimer = _FrSvcDlcmiResetAckTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 11),
    _FrSvcDlcmiResetAckTimer_Type()
)
frSvcDlcmiResetAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcDlcmiResetAckTimer.setStatus("mandatory")


class _FrSvcDlcmiIdleTimer_Type(Integer32):
    """Custom type frSvcDlcmiIdleTimer based on Integer32"""
    defaultValue = 30


_FrSvcDlcmiIdleTimer_Object = MibTableColumn
frSvcDlcmiIdleTimer = _FrSvcDlcmiIdleTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 12),
    _FrSvcDlcmiIdleTimer_Type()
)
frSvcDlcmiIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcDlcmiIdleTimer.setStatus("mandatory")


class _FrSvcDlcmiRetransmissionTimer_Type(TimeTicks):
    """Custom type frSvcDlcmiRetransmissionTimer based on TimeTicks"""
    defaultValue = 1500


_FrSvcDlcmiRetransmissionTimer_Object = MibTableColumn
frSvcDlcmiRetransmissionTimer = _FrSvcDlcmiRetransmissionTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 13),
    _FrSvcDlcmiRetransmissionTimer_Type()
)
frSvcDlcmiRetransmissionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcDlcmiRetransmissionTimer.setStatus("mandatory")


class _FrSvcDlcmiNumRetransmissions_Type(Integer32):
    """Custom type frSvcDlcmiNumRetransmissions based on Integer32"""
    defaultValue = 3


_FrSvcDlcmiNumRetransmissions_Object = MibTableColumn
frSvcDlcmiNumRetransmissions = _FrSvcDlcmiNumRetransmissions_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 14),
    _FrSvcDlcmiNumRetransmissions_Type()
)
frSvcDlcmiNumRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcDlcmiNumRetransmissions.setStatus("mandatory")


class _FrSvcDlcmiMaxInfoFieldSize_Type(Integer32):
    """Custom type frSvcDlcmiMaxInfoFieldSize based on Integer32"""
    defaultValue = 260


_FrSvcDlcmiMaxInfoFieldSize_Object = MibTableColumn
frSvcDlcmiMaxInfoFieldSize = _FrSvcDlcmiMaxInfoFieldSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 15),
    _FrSvcDlcmiMaxInfoFieldSize_Type()
)
frSvcDlcmiMaxInfoFieldSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcDlcmiMaxInfoFieldSize.setStatus("mandatory")


class _FrSvcDlcmiMaxInfoFrames_Type(Integer32):
    """Custom type frSvcDlcmiMaxInfoFrames based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_FrSvcDlcmiMaxInfoFrames_Type.__name__ = "Integer32"
_FrSvcDlcmiMaxInfoFrames_Object = MibTableColumn
frSvcDlcmiMaxInfoFrames = _FrSvcDlcmiMaxInfoFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 16),
    _FrSvcDlcmiMaxInfoFrames_Type()
)
frSvcDlcmiMaxInfoFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcDlcmiMaxInfoFrames.setStatus("mandatory")


class _FrSvcDlcmiQ922State_Type(Integer32):
    """Custom type frSvcDlcmiQ922State based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("assignAwaitingTei", 2),
          ("awaitingEstablishment", 5),
          ("awaitingRelease", 6),
          ("establishingAwaitingTei", 3),
          ("multipleFrameEstablished", 7),
          ("teiAssigned", 4),
          ("teiUnassigned", 1),
          ("timerRecovery", 8))
    )


_FrSvcDlcmiQ922State_Type.__name__ = "Integer32"
_FrSvcDlcmiQ922State_Object = MibTableColumn
frSvcDlcmiQ922State = _FrSvcDlcmiQ922State_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 1, 1, 17),
    _FrSvcDlcmiQ922State_Type()
)
frSvcDlcmiQ922State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcDlcmiQ922State.setStatus("mandatory")
_FrSvcTable_Object = MibTable
frSvcTable = _FrSvcTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2)
)
if mibBuilder.loadTexts:
    frSvcTable.setStatus("mandatory")
_FrSvcEntry_Object = MibTableRow
frSvcEntry = _FrSvcEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1)
)
frSvcEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-SVC-MIB", "frSvcIfIndex"),
    (0, "FRAME-RELAY-DTE-SVC-MIB", "frSvcDlci"),
)
if mibBuilder.loadTexts:
    frSvcEntry.setStatus("mandatory")
_FrSvcIfIndex_Type = InterfaceIndex
_FrSvcIfIndex_Object = MibTableColumn
frSvcIfIndex = _FrSvcIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 1),
    _FrSvcIfIndex_Type()
)
frSvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcIfIndex.setStatus("mandatory")
_FrSvcDlci_Type = DLCI
_FrSvcDlci_Object = MibTableColumn
frSvcDlci = _FrSvcDlci_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 2),
    _FrSvcDlci_Type()
)
frSvcDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcDlci.setStatus("mandatory")
_FrSvcReceivedFECNs_Type = Counter32
_FrSvcReceivedFECNs_Object = MibTableColumn
frSvcReceivedFECNs = _FrSvcReceivedFECNs_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 3),
    _FrSvcReceivedFECNs_Type()
)
frSvcReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcReceivedFECNs.setStatus("mandatory")
_FrSvcReceivedBECNs_Type = Counter32
_FrSvcReceivedBECNs_Object = MibTableColumn
frSvcReceivedBECNs = _FrSvcReceivedBECNs_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 4),
    _FrSvcReceivedBECNs_Type()
)
frSvcReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcReceivedBECNs.setStatus("mandatory")
_FrSvcSentFrames_Type = Counter32
_FrSvcSentFrames_Object = MibTableColumn
frSvcSentFrames = _FrSvcSentFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 5),
    _FrSvcSentFrames_Type()
)
frSvcSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcSentFrames.setStatus("mandatory")
_FrSvcSentOctets_Type = Counter32
_FrSvcSentOctets_Object = MibTableColumn
frSvcSentOctets = _FrSvcSentOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 6),
    _FrSvcSentOctets_Type()
)
frSvcSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcSentOctets.setStatus("mandatory")
_FrSvcReceivedFrames_Type = Counter32
_FrSvcReceivedFrames_Object = MibTableColumn
frSvcReceivedFrames = _FrSvcReceivedFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 7),
    _FrSvcReceivedFrames_Type()
)
frSvcReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcReceivedFrames.setStatus("mandatory")
_FrSvcReceivedOctets_Type = Counter32
_FrSvcReceivedOctets_Object = MibTableColumn
frSvcReceivedOctets = _FrSvcReceivedOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 8),
    _FrSvcReceivedOctets_Type()
)
frSvcReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcReceivedOctets.setStatus("mandatory")
_FrSvcCreationTime_Type = TimeTicks
_FrSvcCreationTime_Object = MibTableColumn
frSvcCreationTime = _FrSvcCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 9),
    _FrSvcCreationTime_Type()
)
frSvcCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcCreationTime.setStatus("mandatory")


class _FrSvcInMaxFmifSize_Type(Integer32):
    """Custom type frSvcInMaxFmifSize based on Integer32"""
    defaultValue = 262


_FrSvcInMaxFmifSize_Object = MibTableColumn
frSvcInMaxFmifSize = _FrSvcInMaxFmifSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 10),
    _FrSvcInMaxFmifSize_Type()
)
frSvcInMaxFmifSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcInMaxFmifSize.setStatus("mandatory")


class _FrSvcOutMaxFmifSize_Type(Integer32):
    """Custom type frSvcOutMaxFmifSize based on Integer32"""
    defaultValue = 262


_FrSvcOutMaxFmifSize_Object = MibTableColumn
frSvcOutMaxFmifSize = _FrSvcOutMaxFmifSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 11),
    _FrSvcOutMaxFmifSize_Type()
)
frSvcOutMaxFmifSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcOutMaxFmifSize.setStatus("mandatory")


class _FrSvcInCommittedBurst_Type(Integer32):
    """Custom type frSvcInCommittedBurst based on Integer32"""
    defaultValue = 0


_FrSvcInCommittedBurst_Object = MibTableColumn
frSvcInCommittedBurst = _FrSvcInCommittedBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 12),
    _FrSvcInCommittedBurst_Type()
)
frSvcInCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcInCommittedBurst.setStatus("mandatory")


class _FrSvcOutCommittedBurst_Type(Integer32):
    """Custom type frSvcOutCommittedBurst based on Integer32"""
    defaultValue = 0


_FrSvcOutCommittedBurst_Object = MibTableColumn
frSvcOutCommittedBurst = _FrSvcOutCommittedBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 13),
    _FrSvcOutCommittedBurst_Type()
)
frSvcOutCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcOutCommittedBurst.setStatus("mandatory")
_FrSvcInExcessBurst_Type = Integer32
_FrSvcInExcessBurst_Object = MibTableColumn
frSvcInExcessBurst = _FrSvcInExcessBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 14),
    _FrSvcInExcessBurst_Type()
)
frSvcInExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcInExcessBurst.setStatus("mandatory")
_FrSvcOutExcessBurst_Type = Integer32
_FrSvcOutExcessBurst_Object = MibTableColumn
frSvcOutExcessBurst = _FrSvcOutExcessBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 15),
    _FrSvcOutExcessBurst_Type()
)
frSvcOutExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcOutExcessBurst.setStatus("mandatory")


class _FrSvcInCIR_Type(Integer32):
    """Custom type frSvcInCIR based on Integer32"""
    defaultValue = 0


_FrSvcInCIR_Object = MibTableColumn
frSvcInCIR = _FrSvcInCIR_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 16),
    _FrSvcInCIR_Type()
)
frSvcInCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcInCIR.setStatus("mandatory")


class _FrSvcOutCIR_Type(Integer32):
    """Custom type frSvcOutCIR based on Integer32"""
    defaultValue = 0


_FrSvcOutCIR_Object = MibTableColumn
frSvcOutCIR = _FrSvcOutCIR_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 17),
    _FrSvcOutCIR_Type()
)
frSvcOutCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcOutCIR.setStatus("mandatory")


class _FrSvcInMinCIR_Type(Integer32):
    """Custom type frSvcInMinCIR based on Integer32"""
    defaultValue = 0


_FrSvcInMinCIR_Object = MibTableColumn
frSvcInMinCIR = _FrSvcInMinCIR_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 18),
    _FrSvcInMinCIR_Type()
)
frSvcInMinCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcInMinCIR.setStatus("mandatory")


class _FrSvcOutMinCIR_Type(Integer32):
    """Custom type frSvcOutMinCIR based on Integer32"""
    defaultValue = 0


_FrSvcOutMinCIR_Object = MibTableColumn
frSvcOutMinCIR = _FrSvcOutMinCIR_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 19),
    _FrSvcOutMinCIR_Type()
)
frSvcOutMinCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcOutMinCIR.setStatus("mandatory")


class _FrSvcState_Type(Integer32):
    """Custom type frSvcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("inProcess", 1))
    )


_FrSvcState_Type.__name__ = "Integer32"
_FrSvcState_Object = MibTableColumn
frSvcState = _FrSvcState_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 20),
    _FrSvcState_Type()
)
frSvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcState.setStatus("mandatory")
_FrSvcCallReferenceValue_Type = Integer32
_FrSvcCallReferenceValue_Object = MibTableColumn
frSvcCallReferenceValue = _FrSvcCallReferenceValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 21),
    _FrSvcCallReferenceValue_Type()
)
frSvcCallReferenceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcCallReferenceValue.setStatus("mandatory")
_FrSvcCallingAddr_Type = DisplayString
_FrSvcCallingAddr_Object = MibTableColumn
frSvcCallingAddr = _FrSvcCallingAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 22),
    _FrSvcCallingAddr_Type()
)
frSvcCallingAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcCallingAddr.setStatus("mandatory")
_FrSvcCallingSubAddr_Type = DisplayString
_FrSvcCallingSubAddr_Object = MibTableColumn
frSvcCallingSubAddr = _FrSvcCallingSubAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 23),
    _FrSvcCallingSubAddr_Type()
)
frSvcCallingSubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcCallingSubAddr.setStatus("mandatory")
_FrSvcCalledAddr_Type = DisplayString
_FrSvcCalledAddr_Object = MibTableColumn
frSvcCalledAddr = _FrSvcCalledAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 24),
    _FrSvcCalledAddr_Type()
)
frSvcCalledAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcCalledAddr.setStatus("mandatory")
_FrSvcCalledSubAddr_Type = DisplayString
_FrSvcCalledSubAddr_Object = MibTableColumn
frSvcCalledSubAddr = _FrSvcCalledSubAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 25),
    _FrSvcCalledSubAddr_Type()
)
frSvcCalledSubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcCalledSubAddr.setStatus("mandatory")


class _FrSvcCallSetup_Type(Integer32):
    """Custom type frSvcCallSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 2),
          ("setup", 1))
    )


_FrSvcCallSetup_Type.__name__ = "Integer32"
_FrSvcCallSetup_Object = MibTableColumn
frSvcCallSetup = _FrSvcCallSetup_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 26),
    _FrSvcCallSetup_Type()
)
frSvcCallSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frSvcCallSetup.setStatus("mandatory")


class _FrSvcCallOrigination_Type(Integer32):
    """Custom type frSvcCallOrigination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("remote", 1))
    )


_FrSvcCallOrigination_Type.__name__ = "Integer32"
_FrSvcCallOrigination_Object = MibTableColumn
frSvcCallOrigination = _FrSvcCallOrigination_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 7, 1, 2, 1, 27),
    _FrSvcCallOrigination_Type()
)
frSvcCallOrigination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSvcCallOrigination.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FRAME-RELAY-DTE-SVC-MIB",
    **{"frameRelayDteSvc": frameRelayDteSvc,
       "frDteSvc": frDteSvc,
       "frSvcDlcmiTable": frSvcDlcmiTable,
       "frSvcDlcmiEntry": frSvcDlcmiEntry,
       "frSvcDlcmiIfIndex": frSvcDlcmiIfIndex,
       "frSvcDlcmiState": frSvcDlcmiState,
       "frSvcDlcmiMaxNumCalls": frSvcDlcmiMaxNumCalls,
       "frSvcDlcmiCallSetupTimer": frSvcDlcmiCallSetupTimer,
       "frSvcDlcmiCallProceedingTimer": frSvcDlcmiCallProceedingTimer,
       "frSvcDlcmiCallDisconnectTimer": frSvcDlcmiCallDisconnectTimer,
       "frSvcDlcmiCallReleaseTimer": frSvcDlcmiCallReleaseTimer,
       "frSvcDlcmiStatusEnquiryTimer": frSvcDlcmiStatusEnquiryTimer,
       "frSvcDlcmiErrorThreshold": frSvcDlcmiErrorThreshold,
       "frSvcDlcmiResetSentTimer": frSvcDlcmiResetSentTimer,
       "frSvcDlcmiResetAckTimer": frSvcDlcmiResetAckTimer,
       "frSvcDlcmiIdleTimer": frSvcDlcmiIdleTimer,
       "frSvcDlcmiRetransmissionTimer": frSvcDlcmiRetransmissionTimer,
       "frSvcDlcmiNumRetransmissions": frSvcDlcmiNumRetransmissions,
       "frSvcDlcmiMaxInfoFieldSize": frSvcDlcmiMaxInfoFieldSize,
       "frSvcDlcmiMaxInfoFrames": frSvcDlcmiMaxInfoFrames,
       "frSvcDlcmiQ922State": frSvcDlcmiQ922State,
       "frSvcTable": frSvcTable,
       "frSvcEntry": frSvcEntry,
       "frSvcIfIndex": frSvcIfIndex,
       "frSvcDlci": frSvcDlci,
       "frSvcReceivedFECNs": frSvcReceivedFECNs,
       "frSvcReceivedBECNs": frSvcReceivedBECNs,
       "frSvcSentFrames": frSvcSentFrames,
       "frSvcSentOctets": frSvcSentOctets,
       "frSvcReceivedFrames": frSvcReceivedFrames,
       "frSvcReceivedOctets": frSvcReceivedOctets,
       "frSvcCreationTime": frSvcCreationTime,
       "frSvcInMaxFmifSize": frSvcInMaxFmifSize,
       "frSvcOutMaxFmifSize": frSvcOutMaxFmifSize,
       "frSvcInCommittedBurst": frSvcInCommittedBurst,
       "frSvcOutCommittedBurst": frSvcOutCommittedBurst,
       "frSvcInExcessBurst": frSvcInExcessBurst,
       "frSvcOutExcessBurst": frSvcOutExcessBurst,
       "frSvcInCIR": frSvcInCIR,
       "frSvcOutCIR": frSvcOutCIR,
       "frSvcInMinCIR": frSvcInMinCIR,
       "frSvcOutMinCIR": frSvcOutMinCIR,
       "frSvcState": frSvcState,
       "frSvcCallReferenceValue": frSvcCallReferenceValue,
       "frSvcCallingAddr": frSvcCallingAddr,
       "frSvcCallingSubAddr": frSvcCallingSubAddr,
       "frSvcCalledAddr": frSvcCalledAddr,
       "frSvcCalledSubAddr": frSvcCalledSubAddr,
       "frSvcCallSetup": frSvcCallSetup,
       "frSvcCallOrigination": frSvcCallOrigination}
)
