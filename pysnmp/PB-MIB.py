# SNMP MIB module (PB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:57 2024
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
 enterprises,
 experimental,
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
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Pb_ObjectIdentity = ObjectIdentity
pb = _Pb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 12)
)
_PbCfg_ObjectIdentity = ObjectIdentity
pbCfg = _PbCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 1)
)
_PbCfgTable_Object = MibTable
pbCfgTable = _PbCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    pbCfgTable.setStatus("mandatory")
_PbCfgEntry_Object = MibTableRow
pbCfgEntry = _PbCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 1, 1, 1)
)
pbCfgEntry.setIndexNames(
    (0, "PB-MIB", "pbCfgIndex"),
)
if mibBuilder.loadTexts:
    pbCfgEntry.setStatus("mandatory")
_PbCfgIndex_Type = Integer32
_PbCfgIndex_Object = MibTableColumn
pbCfgIndex = _PbCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 1, 1, 1, 1),
    _PbCfgIndex_Type()
)
pbCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbCfgIndex.setStatus("mandatory")
_PbCfgMaxSessions_Type = Integer32
_PbCfgMaxSessions_Object = MibTableColumn
pbCfgMaxSessions = _PbCfgMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 1, 1, 1, 2),
    _PbCfgMaxSessions_Type()
)
pbCfgMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbCfgMaxSessions.setStatus("mandatory")
_PbSession_ObjectIdentity = ObjectIdentity
pbSession = _PbSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2)
)
_PbSessionTable_Object = MibTable
pbSessionTable = _PbSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1)
)
if mibBuilder.loadTexts:
    pbSessionTable.setStatus("mandatory")
_PbSessionEntry_Object = MibTableRow
pbSessionEntry = _PbSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1)
)
pbSessionEntry.setIndexNames(
    (0, "PB-MIB", "pbSessionEntityIndex"),
    (0, "PB-MIB", "pbSessionIndex"),
)
if mibBuilder.loadTexts:
    pbSessionEntry.setStatus("mandatory")
_PbSessionEntityIndex_Type = Integer32
_PbSessionEntityIndex_Object = MibTableColumn
pbSessionEntityIndex = _PbSessionEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1, 1),
    _PbSessionEntityIndex_Type()
)
pbSessionEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbSessionEntityIndex.setStatus("mandatory")
_PbSessionIndex_Type = Integer32
_PbSessionIndex_Object = MibTableColumn
pbSessionIndex = _PbSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1, 2),
    _PbSessionIndex_Type()
)
pbSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbSessionIndex.setStatus("mandatory")


class _PbSessionDestSlot_Type(Integer32):
    """Custom type pbSessionDestSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PbSessionDestSlot_Type.__name__ = "Integer32"
_PbSessionDestSlot_Object = MibTableColumn
pbSessionDestSlot = _PbSessionDestSlot_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1, 3),
    _PbSessionDestSlot_Type()
)
pbSessionDestSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbSessionDestSlot.setStatus("mandatory")


class _PbSessionDestChan_Type(Integer32):
    """Custom type pbSessionDestChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PbSessionDestChan_Type.__name__ = "Integer32"
_PbSessionDestChan_Object = MibTableColumn
pbSessionDestChan = _PbSessionDestChan_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1, 4),
    _PbSessionDestChan_Type()
)
pbSessionDestChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbSessionDestChan.setStatus("mandatory")


class _PbSessionDestSess_Type(Integer32):
    """Custom type pbSessionDestSess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PbSessionDestSess_Type.__name__ = "Integer32"
_PbSessionDestSess_Object = MibTableColumn
pbSessionDestSess = _PbSessionDestSess_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1, 5),
    _PbSessionDestSess_Type()
)
pbSessionDestSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbSessionDestSess.setStatus("mandatory")


class _PbSessionRowState_Type(Integer32):
    """Custom type pbSessionRowState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("free", 1),
          ("used", 2))
    )


_PbSessionRowState_Type.__name__ = "Integer32"
_PbSessionRowState_Object = MibTableColumn
pbSessionRowState = _PbSessionRowState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1, 6),
    _PbSessionRowState_Type()
)
pbSessionRowState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbSessionRowState.setStatus("mandatory")


class _PbSessionStatus_Type(Integer32):
    """Custom type pbSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 2),
          ("connected", 3),
          ("unassigned", 1))
    )


_PbSessionStatus_Type.__name__ = "Integer32"
_PbSessionStatus_Object = MibTableColumn
pbSessionStatus = _PbSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1, 7),
    _PbSessionStatus_Type()
)
pbSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbSessionStatus.setStatus("mandatory")


class _PbSessionReqStatus_Type(Integer32):
    """Custom type pbSessionReqStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 1))
    )


_PbSessionReqStatus_Type.__name__ = "Integer32"
_PbSessionReqStatus_Object = MibTableColumn
pbSessionReqStatus = _PbSessionReqStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1, 8),
    _PbSessionReqStatus_Type()
)
pbSessionReqStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbSessionReqStatus.setStatus("mandatory")


class _PbSessionLastRequest_Type(Integer32):
    """Custom type pbSessionLastRequest based on Integer32"""
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("answer", 14),
          ("attach", 15),
          ("close", 3),
          ("dial", 5),
          ("disconnect", 6),
          ("flush", 11),
          ("kill", 12),
          ("listen", 4),
          ("open", 2),
          ("query", 10),
          ("receive", 8),
          ("reserve", 13),
          ("setMode", 9),
          ("transmit", 7),
          ("unknown", 1))
    )


_PbSessionLastRequest_Type.__name__ = "Integer32"
_PbSessionLastRequest_Object = MibTableColumn
pbSessionLastRequest = _PbSessionLastRequest_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1, 9),
    _PbSessionLastRequest_Type()
)
pbSessionLastRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbSessionLastRequest.setStatus("optional")
_PbSessionPktSents_Type = Counter32
_PbSessionPktSents_Object = MibTableColumn
pbSessionPktSents = _PbSessionPktSents_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1, 10),
    _PbSessionPktSents_Type()
)
pbSessionPktSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbSessionPktSents.setStatus("mandatory")
_PbSessionPktRcvds_Type = Counter32
_PbSessionPktRcvds_Object = MibTableColumn
pbSessionPktRcvds = _PbSessionPktRcvds_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1, 11),
    _PbSessionPktRcvds_Type()
)
pbSessionPktRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbSessionPktRcvds.setStatus("mandatory")
_PbSessionPktSize_Type = Integer32
_PbSessionPktSize_Object = MibTableColumn
pbSessionPktSize = _PbSessionPktSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1, 12),
    _PbSessionPktSize_Type()
)
pbSessionPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbSessionPktSize.setStatus("mandatory")
_PbSessionBusTimeOuts_Type = Counter32
_PbSessionBusTimeOuts_Object = MibTableColumn
pbSessionBusTimeOuts = _PbSessionBusTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1, 13),
    _PbSessionBusTimeOuts_Type()
)
pbSessionBusTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbSessionBusTimeOuts.setStatus("mandatory")


class _PbSessionErrorStatus_Type(Integer32):
    """Custom type pbSessionErrorStatus based on Integer32"""
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
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58)
        )
    )
    namedValues = NamedValues(
        *(("ackWaitTimeout", 9),
          ("answerFailed", 49),
          ("autoParityFailed", 54),
          ("badDataBase", 56),
          ("clkReturned", 38),
          ("clkVanished", 37),
          ("closeFailed", 51),
          ("connectionExist", 5),
          ("connectionFailed", 6),
          ("connectionReset", 21),
          ("dtrDrop", 48),
          ("exceedMaxSends", 20),
          ("failedToRecv", 18),
          ("frameError", 40),
          ("heartbeatTimeout", 24),
          ("hwNakRcvd", 10),
          ("invalidBlock", 16),
          ("invalidMsgType", 19),
          ("invalidParm", 2),
          ("linkDown", 45),
          ("linkStartRcvd", 12),
          ("linkdownNoTx", 28),
          ("listenFailed", 46),
          ("listenRcvFailed", 47),
          ("localBusy", 26),
          ("noActiveConn", 8),
          ("noDataToTx", 29),
          ("noError", 1),
          ("noMemory", 14),
          ("noMoreConnObj", 7),
          ("noMoreSocket", 4),
          ("noResponse", 27),
          ("notInitialized", 17),
          ("nullPointer", 15),
          ("openFailed", 50),
          ("otherBusError", 11),
          ("outOfSeqFrame", 13),
          ("padError", 58),
          ("padStreamsError", 57),
          ("readFailed", 52),
          ("recvIFrameWithWrongSeq", 43),
          ("recvLSinInfoTransferState", 42),
          ("remoteBusy", 25),
          ("rxBusTimeOut", 33),
          ("rxMsgBufferOverflow", 44),
          ("rxTAL", 35),
          ("setmodeFailed", 55),
          ("shutdown", 39),
          ("socketClosed", 22),
          ("socketNotOpened", 3),
          ("txBusTimeOut", 32),
          ("txMasterTimeOut", 36),
          ("txPreAck", 30),
          ("txTAL", 34),
          ("txTardyAck", 31),
          ("uiReqPending", 23),
          ("writeFailed", 53),
          ("xIDTimeOut", 41))
    )


_PbSessionErrorStatus_Type.__name__ = "Integer32"
_PbSessionErrorStatus_Object = MibTableColumn
pbSessionErrorStatus = _PbSessionErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 2, 1, 1, 14),
    _PbSessionErrorStatus_Type()
)
pbSessionErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbSessionErrorStatus.setStatus("mandatory")
_PbTrapEna_ObjectIdentity = ObjectIdentity
pbTrapEna = _PbTrapEna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 3)
)
_PbTrapEnaTable_Object = MibTable
pbTrapEnaTable = _PbTrapEnaTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 3, 1)
)
if mibBuilder.loadTexts:
    pbTrapEnaTable.setStatus("mandatory")
_PbTrapEnaEntry_Object = MibTableRow
pbTrapEnaEntry = _PbTrapEnaEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 3, 1, 1)
)
pbTrapEnaEntry.setIndexNames(
    (0, "PB-MIB", "pbTrapEnaIndex"),
    (0, "PB-MIB", "pbTrapSessionIndex"),
)
if mibBuilder.loadTexts:
    pbTrapEnaEntry.setStatus("mandatory")
_PbTrapEnaIndex_Type = Integer32
_PbTrapEnaIndex_Object = MibTableColumn
pbTrapEnaIndex = _PbTrapEnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 3, 1, 1, 1),
    _PbTrapEnaIndex_Type()
)
pbTrapEnaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbTrapEnaIndex.setStatus("mandatory")
_PbTrapSessionIndex_Type = Integer32
_PbTrapSessionIndex_Object = MibTableColumn
pbTrapSessionIndex = _PbTrapSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 3, 1, 1, 2),
    _PbTrapSessionIndex_Type()
)
pbTrapSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbTrapSessionIndex.setStatus("mandatory")


class _PbTrapEnaSessActive_Type(Integer32):
    """Custom type pbTrapEnaSessActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PbTrapEnaSessActive_Type.__name__ = "Integer32"
_PbTrapEnaSessActive_Object = MibTableColumn
pbTrapEnaSessActive = _PbTrapEnaSessActive_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 3, 1, 1, 3),
    _PbTrapEnaSessActive_Type()
)
pbTrapEnaSessActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbTrapEnaSessActive.setStatus("mandatory")


class _PbTrapEnaPktBusCongest_Type(Integer32):
    """Custom type pbTrapEnaPktBusCongest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PbTrapEnaPktBusCongest_Type.__name__ = "Integer32"
_PbTrapEnaPktBusCongest_Object = MibTableColumn
pbTrapEnaPktBusCongest = _PbTrapEnaPktBusCongest_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 3, 1, 1, 4),
    _PbTrapEnaPktBusCongest_Type()
)
pbTrapEnaPktBusCongest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbTrapEnaPktBusCongest.setStatus("mandatory")


class _PbTrapEnaPktBusSessLost_Type(Integer32):
    """Custom type pbTrapEnaPktBusSessLost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PbTrapEnaPktBusSessLost_Type.__name__ = "Integer32"
_PbTrapEnaPktBusSessLost_Object = MibTableColumn
pbTrapEnaPktBusSessLost = _PbTrapEnaPktBusSessLost_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 3, 1, 1, 5),
    _PbTrapEnaPktBusSessLost_Type()
)
pbTrapEnaPktBusSessLost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbTrapEnaPktBusSessLost.setStatus("mandatory")


class _PbTrapEnaSessionInactive_Type(Integer32):
    """Custom type pbTrapEnaSessionInactive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PbTrapEnaSessionInactive_Type.__name__ = "Integer32"
_PbTrapEnaSessionInactive_Object = MibTableColumn
pbTrapEnaSessionInactive = _PbTrapEnaSessionInactive_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 3, 1, 1, 6),
    _PbTrapEnaSessionInactive_Type()
)
pbTrapEnaSessionInactive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbTrapEnaSessionInactive.setStatus("mandatory")


class _PbTrapEnaSessionError_Type(Integer32):
    """Custom type pbTrapEnaSessionError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PbTrapEnaSessionError_Type.__name__ = "Integer32"
_PbTrapEnaSessionError_Object = MibTableColumn
pbTrapEnaSessionError = _PbTrapEnaSessionError_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 12, 3, 1, 1, 7),
    _PbTrapEnaSessionError_Type()
)
pbTrapEnaSessionError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbTrapEnaSessionError.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PB-MIB",
    **{"usr": usr,
       "nas": nas,
       "pb": pb,
       "pbCfg": pbCfg,
       "pbCfgTable": pbCfgTable,
       "pbCfgEntry": pbCfgEntry,
       "pbCfgIndex": pbCfgIndex,
       "pbCfgMaxSessions": pbCfgMaxSessions,
       "pbSession": pbSession,
       "pbSessionTable": pbSessionTable,
       "pbSessionEntry": pbSessionEntry,
       "pbSessionEntityIndex": pbSessionEntityIndex,
       "pbSessionIndex": pbSessionIndex,
       "pbSessionDestSlot": pbSessionDestSlot,
       "pbSessionDestChan": pbSessionDestChan,
       "pbSessionDestSess": pbSessionDestSess,
       "pbSessionRowState": pbSessionRowState,
       "pbSessionStatus": pbSessionStatus,
       "pbSessionReqStatus": pbSessionReqStatus,
       "pbSessionLastRequest": pbSessionLastRequest,
       "pbSessionPktSents": pbSessionPktSents,
       "pbSessionPktRcvds": pbSessionPktRcvds,
       "pbSessionPktSize": pbSessionPktSize,
       "pbSessionBusTimeOuts": pbSessionBusTimeOuts,
       "pbSessionErrorStatus": pbSessionErrorStatus,
       "pbTrapEna": pbTrapEna,
       "pbTrapEnaTable": pbTrapEnaTable,
       "pbTrapEnaEntry": pbTrapEnaEntry,
       "pbTrapEnaIndex": pbTrapEnaIndex,
       "pbTrapSessionIndex": pbTrapSessionIndex,
       "pbTrapEnaSessActive": pbTrapEnaSessActive,
       "pbTrapEnaPktBusCongest": pbTrapEnaPktBusCongest,
       "pbTrapEnaPktBusSessLost": pbTrapEnaPktBusSessLost,
       "pbTrapEnaSessionInactive": pbTrapEnaSessionInactive,
       "pbTrapEnaSessionError": pbTrapEnaSessionError}
)
