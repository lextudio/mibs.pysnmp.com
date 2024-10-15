# SNMP MIB module (ACC-QTP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-QTP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:50 2024
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
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccQtp_ObjectIdentity = ObjectIdentity
accQtp = _AccQtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82)
)
_AccQtpServer_ObjectIdentity = ObjectIdentity
accQtpServer = _AccQtpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1)
)
_AccQtpSrvParmsTable_Object = MibTable
accQtpSrvParmsTable = _AccQtpSrvParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 1)
)
if mibBuilder.loadTexts:
    accQtpSrvParmsTable.setStatus("mandatory")
_AccQtpSrvParEntry_Object = MibTableRow
accQtpSrvParEntry = _AccQtpSrvParEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 1, 1)
)
accQtpSrvParEntry.setIndexNames(
    (0, "ACC-QTP", "accQtpSrvAddr"),
)
if mibBuilder.loadTexts:
    accQtpSrvParEntry.setStatus("mandatory")
_AccQtpSrvAddr_Type = IpAddress
_AccQtpSrvAddr_Object = MibTableColumn
accQtpSrvAddr = _AccQtpSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 1, 1, 1),
    _AccQtpSrvAddr_Type()
)
accQtpSrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpSrvAddr.setStatus("mandatory")


class _AccQtpSrvEntryStatus_Type(Integer32):
    """Custom type accQtpSrvEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 2),
          ("valid", 1))
    )


_AccQtpSrvEntryStatus_Type.__name__ = "Integer32"
_AccQtpSrvEntryStatus_Object = MibTableColumn
accQtpSrvEntryStatus = _AccQtpSrvEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 1, 1, 2),
    _AccQtpSrvEntryStatus_Type()
)
accQtpSrvEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpSrvEntryStatus.setStatus("mandatory")
_AccQtpSrvPort_Type = Integer32
_AccQtpSrvPort_Object = MibTableColumn
accQtpSrvPort = _AccQtpSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 1, 1, 3),
    _AccQtpSrvPort_Type()
)
accQtpSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpSrvPort.setStatus("mandatory")


class _AccQtpSrvMaxMsg_Type(Integer32):
    """Custom type accQtpSrvMaxMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AccQtpSrvMaxMsg_Type.__name__ = "Integer32"
_AccQtpSrvMaxMsg_Object = MibTableColumn
accQtpSrvMaxMsg = _AccQtpSrvMaxMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 1, 1, 4),
    _AccQtpSrvMaxMsg_Type()
)
accQtpSrvMaxMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpSrvMaxMsg.setStatus("mandatory")


class _AccQtpSrvPkgInterval_Type(Integer32):
    """Custom type accQtpSrvPkgInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AccQtpSrvPkgInterval_Type.__name__ = "Integer32"
_AccQtpSrvPkgInterval_Object = MibTableColumn
accQtpSrvPkgInterval = _AccQtpSrvPkgInterval_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 1, 1, 5),
    _AccQtpSrvPkgInterval_Type()
)
accQtpSrvPkgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpSrvPkgInterval.setStatus("mandatory")
_AccQtpSrvStatusDelay_Type = TimeTicks
_AccQtpSrvStatusDelay_Object = MibTableColumn
accQtpSrvStatusDelay = _AccQtpSrvStatusDelay_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 1, 1, 6),
    _AccQtpSrvStatusDelay_Type()
)
accQtpSrvStatusDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpSrvStatusDelay.setStatus("mandatory")
_AccQtpSrvAckTimer_Type = TimeTicks
_AccQtpSrvAckTimer_Object = MibTableColumn
accQtpSrvAckTimer = _AccQtpSrvAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 1, 1, 7),
    _AccQtpSrvAckTimer_Type()
)
accQtpSrvAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpSrvAckTimer.setStatus("mandatory")


class _AccQtpSrvMaxCkt_Type(Integer32):
    """Custom type accQtpSrvMaxCkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccQtpSrvMaxCkt_Type.__name__ = "Integer32"
_AccQtpSrvMaxCkt_Object = MibTableColumn
accQtpSrvMaxCkt = _AccQtpSrvMaxCkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 1, 1, 8),
    _AccQtpSrvMaxCkt_Type()
)
accQtpSrvMaxCkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpSrvMaxCkt.setStatus("mandatory")


class _AccQtpSrvAdStatus_Type(Integer32):
    """Custom type accQtpSrvAdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busyout", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_AccQtpSrvAdStatus_Type.__name__ = "Integer32"
_AccQtpSrvAdStatus_Object = MibTableColumn
accQtpSrvAdStatus = _AccQtpSrvAdStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 1, 1, 9),
    _AccQtpSrvAdStatus_Type()
)
accQtpSrvAdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpSrvAdStatus.setStatus("mandatory")
_AccQtpSrvIdleTime_Type = TimeTicks
_AccQtpSrvIdleTime_Object = MibTableColumn
accQtpSrvIdleTime = _AccQtpSrvIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 1, 1, 10),
    _AccQtpSrvIdleTime_Type()
)
accQtpSrvIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpSrvIdleTime.setStatus("mandatory")


class _AccQtpSrvMsgLvl_Type(Integer32):
    """Custom type accQtpSrvMsgLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccQtpSrvMsgLvl_Type.__name__ = "Integer32"
_AccQtpSrvMsgLvl_Object = MibTableColumn
accQtpSrvMsgLvl = _AccQtpSrvMsgLvl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 1, 1, 11),
    _AccQtpSrvMsgLvl_Type()
)
accQtpSrvMsgLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpSrvMsgLvl.setStatus("mandatory")
_AccQtpSrvStatusTable_Object = MibTable
accQtpSrvStatusTable = _AccQtpSrvStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 2)
)
if mibBuilder.loadTexts:
    accQtpSrvStatusTable.setStatus("mandatory")
_AccQtpSrvStatusEntry_Object = MibTableRow
accQtpSrvStatusEntry = _AccQtpSrvStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 2, 1)
)
accQtpSrvStatusEntry.setIndexNames(
    (0, "ACC-QTP", "accQtpSrvAddr"),
)
if mibBuilder.loadTexts:
    accQtpSrvStatusEntry.setStatus("mandatory")
_AccQtpSrvActiveChnls_Type = Gauge32
_AccQtpSrvActiveChnls_Object = MibTableColumn
accQtpSrvActiveChnls = _AccQtpSrvActiveChnls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 2, 1, 1),
    _AccQtpSrvActiveChnls_Type()
)
accQtpSrvActiveChnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvActiveChnls.setStatus("mandatory")


class _AccQtpSrvClrCauseTx_Type(Integer32):
    """Custom type accQtpSrvClrCauseTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccQtpSrvClrCauseTx_Type.__name__ = "Integer32"
_AccQtpSrvClrCauseTx_Object = MibTableColumn
accQtpSrvClrCauseTx = _AccQtpSrvClrCauseTx_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 2, 1, 2),
    _AccQtpSrvClrCauseTx_Type()
)
accQtpSrvClrCauseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvClrCauseTx.setStatus("mandatory")
_AccQtpSrvClrTxLcn_Type = Integer32
_AccQtpSrvClrTxLcn_Object = MibTableColumn
accQtpSrvClrTxLcn = _AccQtpSrvClrTxLcn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 2, 1, 3),
    _AccQtpSrvClrTxLcn_Type()
)
accQtpSrvClrTxLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvClrTxLcn.setStatus("mandatory")


class _AccQtpSrvClrCauseRx_Type(Integer32):
    """Custom type accQtpSrvClrCauseRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccQtpSrvClrCauseRx_Type.__name__ = "Integer32"
_AccQtpSrvClrCauseRx_Object = MibTableColumn
accQtpSrvClrCauseRx = _AccQtpSrvClrCauseRx_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 2, 1, 4),
    _AccQtpSrvClrCauseRx_Type()
)
accQtpSrvClrCauseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvClrCauseRx.setStatus("mandatory")
_AccQtpSrvClrRxLcn_Type = Integer32
_AccQtpSrvClrRxLcn_Object = MibTableColumn
accQtpSrvClrRxLcn = _AccQtpSrvClrRxLcn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 2, 1, 5),
    _AccQtpSrvClrRxLcn_Type()
)
accQtpSrvClrRxLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvClrRxLcn.setStatus("mandatory")


class _AccQtpSrvRemFlowCntl_Type(Integer32):
    """Custom type accQtpSrvRemFlowCntl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("congested", 3),
          ("partially-congested", 2),
          ("shutdown", 4))
    )


_AccQtpSrvRemFlowCntl_Type.__name__ = "Integer32"
_AccQtpSrvRemFlowCntl_Object = MibTableColumn
accQtpSrvRemFlowCntl = _AccQtpSrvRemFlowCntl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 2, 1, 6),
    _AccQtpSrvRemFlowCntl_Type()
)
accQtpSrvRemFlowCntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvRemFlowCntl.setStatus("mandatory")


class _AccQtpSrvLclFlowCntl_Type(Integer32):
    """Custom type accQtpSrvLclFlowCntl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("congested", 3),
          ("partially-congested", 2),
          ("shutdown", 4))
    )


_AccQtpSrvLclFlowCntl_Type.__name__ = "Integer32"
_AccQtpSrvLclFlowCntl_Object = MibTableColumn
accQtpSrvLclFlowCntl = _AccQtpSrvLclFlowCntl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 2, 1, 7),
    _AccQtpSrvLclFlowCntl_Type()
)
accQtpSrvLclFlowCntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvLclFlowCntl.setStatus("mandatory")


class _AccQtpSrvOpStatus_Type(Integer32):
    """Custom type accQtpSrvOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("disabled", 3),
          ("initializing", 1))
    )


_AccQtpSrvOpStatus_Type.__name__ = "Integer32"
_AccQtpSrvOpStatus_Object = MibTableColumn
accQtpSrvOpStatus = _AccQtpSrvOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 2, 1, 8),
    _AccQtpSrvOpStatus_Type()
)
accQtpSrvOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvOpStatus.setStatus("mandatory")
_AccQtpSrvStatsTable_Object = MibTable
accQtpSrvStatsTable = _AccQtpSrvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 3)
)
if mibBuilder.loadTexts:
    accQtpSrvStatsTable.setStatus("mandatory")
_AccQtpSrvStatsEntry_Object = MibTableRow
accQtpSrvStatsEntry = _AccQtpSrvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 3, 1)
)
accQtpSrvStatsEntry.setIndexNames(
    (0, "ACC-QTP", "accQtpSrvAddr"),
)
if mibBuilder.loadTexts:
    accQtpSrvStatsEntry.setStatus("mandatory")
_AccQtpSrvOKCalls_Type = Counter32
_AccQtpSrvOKCalls_Object = MibTableColumn
accQtpSrvOKCalls = _AccQtpSrvOKCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 3, 1, 1),
    _AccQtpSrvOKCalls_Type()
)
accQtpSrvOKCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvOKCalls.setStatus("mandatory")
_AccQtpSrvFailCalls_Type = Counter32
_AccQtpSrvFailCalls_Object = MibTableColumn
accQtpSrvFailCalls = _AccQtpSrvFailCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 3, 1, 2),
    _AccQtpSrvFailCalls_Type()
)
accQtpSrvFailCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvFailCalls.setStatus("mandatory")
_AccQtpSrvTxDataMsgs_Type = Counter32
_AccQtpSrvTxDataMsgs_Object = MibTableColumn
accQtpSrvTxDataMsgs = _AccQtpSrvTxDataMsgs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 3, 1, 3),
    _AccQtpSrvTxDataMsgs_Type()
)
accQtpSrvTxDataMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvTxDataMsgs.setStatus("mandatory")
_AccQtpSrvRxDataMsgs_Type = Counter32
_AccQtpSrvRxDataMsgs_Object = MibTableColumn
accQtpSrvRxDataMsgs = _AccQtpSrvRxDataMsgs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 3, 1, 4),
    _AccQtpSrvRxDataMsgs_Type()
)
accQtpSrvRxDataMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvRxDataMsgs.setStatus("mandatory")
_AccQtpSrvAckTimouts_Type = Counter32
_AccQtpSrvAckTimouts_Object = MibTableColumn
accQtpSrvAckTimouts = _AccQtpSrvAckTimouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 3, 1, 5),
    _AccQtpSrvAckTimouts_Type()
)
accQtpSrvAckTimouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvAckTimouts.setStatus("mandatory")
_AccQtpSrvProtoErrs_Type = Counter32
_AccQtpSrvProtoErrs_Object = MibTableColumn
accQtpSrvProtoErrs = _AccQtpSrvProtoErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 3, 1, 6),
    _AccQtpSrvProtoErrs_Type()
)
accQtpSrvProtoErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvProtoErrs.setStatus("mandatory")
_AccQtpSrvTxStatMsgs_Type = Counter32
_AccQtpSrvTxStatMsgs_Object = MibTableColumn
accQtpSrvTxStatMsgs = _AccQtpSrvTxStatMsgs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 3, 1, 7),
    _AccQtpSrvTxStatMsgs_Type()
)
accQtpSrvTxStatMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvTxStatMsgs.setStatus("mandatory")
_AccQtpSrvRxStatMsgs_Type = Counter32
_AccQtpSrvRxStatMsgs_Object = MibTableColumn
accQtpSrvRxStatMsgs = _AccQtpSrvRxStatMsgs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 3, 1, 8),
    _AccQtpSrvRxStatMsgs_Type()
)
accQtpSrvRxStatMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvRxStatMsgs.setStatus("mandatory")
_AccQtpSrvTxDgrms_Type = Counter32
_AccQtpSrvTxDgrms_Object = MibTableColumn
accQtpSrvTxDgrms = _AccQtpSrvTxDgrms_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 3, 1, 9),
    _AccQtpSrvTxDgrms_Type()
)
accQtpSrvTxDgrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvTxDgrms.setStatus("mandatory")
_AccQtpSrvRxDgrms_Type = Counter32
_AccQtpSrvRxDgrms_Object = MibTableColumn
accQtpSrvRxDgrms = _AccQtpSrvRxDgrms_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 3, 1, 10),
    _AccQtpSrvRxDgrms_Type()
)
accQtpSrvRxDgrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvRxDgrms.setStatus("mandatory")
_AccQtpSrvTxOctets_Type = Counter32
_AccQtpSrvTxOctets_Object = MibTableColumn
accQtpSrvTxOctets = _AccQtpSrvTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 3, 1, 11),
    _AccQtpSrvTxOctets_Type()
)
accQtpSrvTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvTxOctets.setStatus("mandatory")
_AccQtpSrvRxOctets_Type = Counter32
_AccQtpSrvRxOctets_Object = MibTableColumn
accQtpSrvRxOctets = _AccQtpSrvRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 1, 3, 1, 12),
    _AccQtpSrvRxOctets_Type()
)
accQtpSrvRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpSrvRxOctets.setStatus("mandatory")
_AccQtpRouting_ObjectIdentity = ObjectIdentity
accQtpRouting = _AccQtpRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 2)
)
_AccQtpRtCalls_Type = Counter32
_AccQtpRtCalls_Object = MibScalar
accQtpRtCalls = _AccQtpRtCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 2, 1),
    _AccQtpRtCalls_Type()
)
accQtpRtCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpRtCalls.setStatus("mandatory")
_AccQtpRtSecCalls_Type = Counter32
_AccQtpRtSecCalls_Object = MibScalar
accQtpRtSecCalls = _AccQtpRtSecCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 2, 2),
    _AccQtpRtSecCalls_Type()
)
accQtpRtSecCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpRtSecCalls.setStatus("mandatory")
_AccQtpRtNotConfigs_Type = Counter32
_AccQtpRtNotConfigs_Object = MibScalar
accQtpRtNotConfigs = _AccQtpRtNotConfigs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 2, 3),
    _AccQtpRtNotConfigs_Type()
)
accQtpRtNotConfigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpRtNotConfigs.setStatus("mandatory")
_AccQtpRtNoRts_Type = Counter32
_AccQtpRtNoRts_Object = MibScalar
accQtpRtNoRts = _AccQtpRtNoRts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 2, 4),
    _AccQtpRtNoRts_Type()
)
accQtpRtNoRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpRtNoRts.setStatus("mandatory")
_AccQtpRtToQTPFrms_Type = Counter32
_AccQtpRtToQTPFrms_Object = MibScalar
accQtpRtToQTPFrms = _AccQtpRtToQTPFrms_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 2, 5),
    _AccQtpRtToQTPFrms_Type()
)
accQtpRtToQTPFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpRtToQTPFrms.setStatus("mandatory")
_AccQtpRtToQTPOcts_Type = Counter32
_AccQtpRtToQTPOcts_Object = MibScalar
accQtpRtToQTPOcts = _AccQtpRtToQTPOcts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 2, 6),
    _AccQtpRtToQTPOcts_Type()
)
accQtpRtToQTPOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpRtToQTPOcts.setStatus("mandatory")
_AccQtpRtToMdmFrms_Type = Counter32
_AccQtpRtToMdmFrms_Object = MibScalar
accQtpRtToMdmFrms = _AccQtpRtToMdmFrms_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 2, 7),
    _AccQtpRtToMdmFrms_Type()
)
accQtpRtToMdmFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpRtToMdmFrms.setStatus("mandatory")
_AccQtpRtToMdmOcts_Type = Counter32
_AccQtpRtToMdmOcts_Object = MibScalar
accQtpRtToMdmOcts = _AccQtpRtToMdmOcts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 2, 8),
    _AccQtpRtToMdmOcts_Type()
)
accQtpRtToMdmOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpRtToMdmOcts.setStatus("mandatory")
_AccQtpRtDropQtpFrms_Type = Counter32
_AccQtpRtDropQtpFrms_Object = MibScalar
accQtpRtDropQtpFrms = _AccQtpRtDropQtpFrms_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 2, 9),
    _AccQtpRtDropQtpFrms_Type()
)
accQtpRtDropQtpFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpRtDropQtpFrms.setStatus("mandatory")
_AccQtpRtDropMdmFrms_Type = Counter32
_AccQtpRtDropMdmFrms_Object = MibScalar
accQtpRtDropMdmFrms = _AccQtpRtDropMdmFrms_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 2, 10),
    _AccQtpRtDropMdmFrms_Type()
)
accQtpRtDropMdmFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accQtpRtDropMdmFrms.setStatus("mandatory")
_AccQtpServerPool_ObjectIdentity = ObjectIdentity
accQtpServerPool = _AccQtpServerPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 3)
)
_AccQtpSrvPoolTable_Object = MibTable
accQtpSrvPoolTable = _AccQtpSrvPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 3, 1)
)
if mibBuilder.loadTexts:
    accQtpSrvPoolTable.setStatus("mandatory")
_AccQtpSrvPoolEntry_Object = MibTableRow
accQtpSrvPoolEntry = _AccQtpSrvPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 3, 1, 1)
)
accQtpSrvPoolEntry.setIndexNames(
    (0, "ACC-QTP", "accQtpPoolSrvAddr"),
    (0, "ACC-QTP", "accQtpPoolSvcProfile"),
)
if mibBuilder.loadTexts:
    accQtpSrvPoolEntry.setStatus("mandatory")
_AccQtpPoolSrvAddr_Type = IpAddress
_AccQtpPoolSrvAddr_Object = MibTableColumn
accQtpPoolSrvAddr = _AccQtpPoolSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 3, 1, 1, 1),
    _AccQtpPoolSrvAddr_Type()
)
accQtpPoolSrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpPoolSrvAddr.setStatus("mandatory")
_AccQtpPoolSvcProfile_Type = DisplayString
_AccQtpPoolSvcProfile_Object = MibTableColumn
accQtpPoolSvcProfile = _AccQtpPoolSvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 3, 1, 1, 2),
    _AccQtpPoolSvcProfile_Type()
)
accQtpPoolSvcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpPoolSvcProfile.setStatus("mandatory")


class _AccQtpPoolEntryStatus_Type(Integer32):
    """Custom type accQtpPoolEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 2),
          ("valid", 1))
    )


_AccQtpPoolEntryStatus_Type.__name__ = "Integer32"
_AccQtpPoolEntryStatus_Object = MibTableColumn
accQtpPoolEntryStatus = _AccQtpPoolEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 3, 1, 1, 3),
    _AccQtpPoolEntryStatus_Type()
)
accQtpPoolEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpPoolEntryStatus.setStatus("mandatory")


class _AccQtpPoolPriority_Type(Integer32):
    """Custom type accQtpPoolPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_AccQtpPoolPriority_Type.__name__ = "Integer32"
_AccQtpPoolPriority_Object = MibTableColumn
accQtpPoolPriority = _AccQtpPoolPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 82, 3, 1, 1, 4),
    _AccQtpPoolPriority_Type()
)
accQtpPoolPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accQtpPoolPriority.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-QTP",
    **{"accQtp": accQtp,
       "accQtpServer": accQtpServer,
       "accQtpSrvParmsTable": accQtpSrvParmsTable,
       "accQtpSrvParEntry": accQtpSrvParEntry,
       "accQtpSrvAddr": accQtpSrvAddr,
       "accQtpSrvEntryStatus": accQtpSrvEntryStatus,
       "accQtpSrvPort": accQtpSrvPort,
       "accQtpSrvMaxMsg": accQtpSrvMaxMsg,
       "accQtpSrvPkgInterval": accQtpSrvPkgInterval,
       "accQtpSrvStatusDelay": accQtpSrvStatusDelay,
       "accQtpSrvAckTimer": accQtpSrvAckTimer,
       "accQtpSrvMaxCkt": accQtpSrvMaxCkt,
       "accQtpSrvAdStatus": accQtpSrvAdStatus,
       "accQtpSrvIdleTime": accQtpSrvIdleTime,
       "accQtpSrvMsgLvl": accQtpSrvMsgLvl,
       "accQtpSrvStatusTable": accQtpSrvStatusTable,
       "accQtpSrvStatusEntry": accQtpSrvStatusEntry,
       "accQtpSrvActiveChnls": accQtpSrvActiveChnls,
       "accQtpSrvClrCauseTx": accQtpSrvClrCauseTx,
       "accQtpSrvClrTxLcn": accQtpSrvClrTxLcn,
       "accQtpSrvClrCauseRx": accQtpSrvClrCauseRx,
       "accQtpSrvClrRxLcn": accQtpSrvClrRxLcn,
       "accQtpSrvRemFlowCntl": accQtpSrvRemFlowCntl,
       "accQtpSrvLclFlowCntl": accQtpSrvLclFlowCntl,
       "accQtpSrvOpStatus": accQtpSrvOpStatus,
       "accQtpSrvStatsTable": accQtpSrvStatsTable,
       "accQtpSrvStatsEntry": accQtpSrvStatsEntry,
       "accQtpSrvOKCalls": accQtpSrvOKCalls,
       "accQtpSrvFailCalls": accQtpSrvFailCalls,
       "accQtpSrvTxDataMsgs": accQtpSrvTxDataMsgs,
       "accQtpSrvRxDataMsgs": accQtpSrvRxDataMsgs,
       "accQtpSrvAckTimouts": accQtpSrvAckTimouts,
       "accQtpSrvProtoErrs": accQtpSrvProtoErrs,
       "accQtpSrvTxStatMsgs": accQtpSrvTxStatMsgs,
       "accQtpSrvRxStatMsgs": accQtpSrvRxStatMsgs,
       "accQtpSrvTxDgrms": accQtpSrvTxDgrms,
       "accQtpSrvRxDgrms": accQtpSrvRxDgrms,
       "accQtpSrvTxOctets": accQtpSrvTxOctets,
       "accQtpSrvRxOctets": accQtpSrvRxOctets,
       "accQtpRouting": accQtpRouting,
       "accQtpRtCalls": accQtpRtCalls,
       "accQtpRtSecCalls": accQtpRtSecCalls,
       "accQtpRtNotConfigs": accQtpRtNotConfigs,
       "accQtpRtNoRts": accQtpRtNoRts,
       "accQtpRtToQTPFrms": accQtpRtToQTPFrms,
       "accQtpRtToQTPOcts": accQtpRtToQTPOcts,
       "accQtpRtToMdmFrms": accQtpRtToMdmFrms,
       "accQtpRtToMdmOcts": accQtpRtToMdmOcts,
       "accQtpRtDropQtpFrms": accQtpRtDropQtpFrms,
       "accQtpRtDropMdmFrms": accQtpRtDropMdmFrms,
       "accQtpServerPool": accQtpServerPool,
       "accQtpSrvPoolTable": accQtpSrvPoolTable,
       "accQtpSrvPoolEntry": accQtpSrvPoolEntry,
       "accQtpPoolSrvAddr": accQtpPoolSrvAddr,
       "accQtpPoolSvcProfile": accQtpPoolSvcProfile,
       "accQtpPoolEntryStatus": accQtpPoolEntryStatus,
       "accQtpPoolPriority": accQtpPoolPriority}
)
