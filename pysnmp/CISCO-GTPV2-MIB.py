# SNMP MIB module (CISCO-GTPV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GTPV2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:06 2024
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

(cGtpHistIndex,
 cGtpHistRemoteAddrType,
 cGtpHistRemoteAddress,
 cGtpHistRemotePort,
 cGtpPathAddress,
 cGtpPathAddressType,
 cGtpPathPort,
 cGtpPathStatisticsEntry,
 cGtpPathStatisticsHistEntry) = mibBuilder.importSymbols(
    "CISCO-GTP-MIB",
    "cGtpHistIndex",
    "cGtpHistRemoteAddrType",
    "cGtpHistRemoteAddress",
    "cGtpHistRemotePort",
    "cGtpPathAddress",
    "cGtpPathAddressType",
    "cGtpPathPort",
    "cGtpPathStatisticsEntry",
    "cGtpPathStatisticsHistEntry")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoGtpv2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 734)
)
ciscoGtpv2MIB.setRevisions(
        ("2010-05-24 00:00",
         "2010-04-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CGtpv2Action(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cGtpv2Received", 2),
          ("cGtpv2Rejected", 3),
          ("cGtpv2Sent", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CGtpv2MIBObjects_ObjectIdentity = ObjectIdentity
cGtpv2MIBObjects = _CGtpv2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1)
)
_CGtpv2Statistics_ObjectIdentity = ObjectIdentity
cGtpv2Statistics = _CGtpv2Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1)
)
_CGtpv2SystemStatistics_ObjectIdentity = ObjectIdentity
cGtpv2SystemStatistics = _CGtpv2SystemStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1)
)
_CGtpv2DroppedSigMsgs_Type = Counter32
_CGtpv2DroppedSigMsgs_Object = MibScalar
cGtpv2DroppedSigMsgs = _CGtpv2DroppedSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 1),
    _CGtpv2DroppedSigMsgs_Type()
)
cGtpv2DroppedSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2DroppedSigMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2DroppedSigMsgs.setUnits("messages")
_CGtpv2ReservedValueIeMsgs_Type = Counter32
_CGtpv2ReservedValueIeMsgs_Object = MibScalar
cGtpv2ReservedValueIeMsgs = _CGtpv2ReservedValueIeMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 2),
    _CGtpv2ReservedValueIeMsgs_Type()
)
cGtpv2ReservedValueIeMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2ReservedValueIeMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2ReservedValueIeMsgs.setUnits("messages")
_CGtpv2ReqMsgStatsTable_Object = MibTable
cGtpv2ReqMsgStatsTable = _CGtpv2ReqMsgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cGtpv2ReqMsgStatsTable.setStatus("current")
_CGtpv2ReqMsgStatsEntry_Object = MibTableRow
cGtpv2ReqMsgStatsEntry = _CGtpv2ReqMsgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1)
)
cGtpv2ReqMsgStatsEntry.setIndexNames(
    (0, "CISCO-GTPV2-MIB", "cGtpv2MsgReqAction"),
)
if mibBuilder.loadTexts:
    cGtpv2ReqMsgStatsEntry.setStatus("current")
_CGtpv2MsgReqAction_Type = CGtpv2Action
_CGtpv2MsgReqAction_Object = MibTableColumn
cGtpv2MsgReqAction = _CGtpv2MsgReqAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 1),
    _CGtpv2MsgReqAction_Type()
)
cGtpv2MsgReqAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpv2MsgReqAction.setStatus("current")
_CGtpv2CreateSessReqs_Type = Counter32
_CGtpv2CreateSessReqs_Object = MibTableColumn
cGtpv2CreateSessReqs = _CGtpv2CreateSessReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 2),
    _CGtpv2CreateSessReqs_Type()
)
cGtpv2CreateSessReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2CreateSessReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2CreateSessReqs.setUnits("messages")
_CGtpv2DeleteSessReqs_Type = Counter32
_CGtpv2DeleteSessReqs_Object = MibTableColumn
cGtpv2DeleteSessReqs = _CGtpv2DeleteSessReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 3),
    _CGtpv2DeleteSessReqs_Type()
)
cGtpv2DeleteSessReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2DeleteSessReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2DeleteSessReqs.setUnits("messages")
_CGtpv2CreateBearerReqs_Type = Counter32
_CGtpv2CreateBearerReqs_Object = MibTableColumn
cGtpv2CreateBearerReqs = _CGtpv2CreateBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 4),
    _CGtpv2CreateBearerReqs_Type()
)
cGtpv2CreateBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2CreateBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2CreateBearerReqs.setUnits("messages")
_CGtpv2ModifyBearerReqs_Type = Counter32
_CGtpv2ModifyBearerReqs_Object = MibTableColumn
cGtpv2ModifyBearerReqs = _CGtpv2ModifyBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 5),
    _CGtpv2ModifyBearerReqs_Type()
)
cGtpv2ModifyBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2ModifyBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2ModifyBearerReqs.setUnits("messages")
_CGtpv2UpdateBearerReqs_Type = Counter32
_CGtpv2UpdateBearerReqs_Object = MibTableColumn
cGtpv2UpdateBearerReqs = _CGtpv2UpdateBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 6),
    _CGtpv2UpdateBearerReqs_Type()
)
cGtpv2UpdateBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2UpdateBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2UpdateBearerReqs.setUnits("messages")
_CGtpv2DeleteBearerReqs_Type = Counter32
_CGtpv2DeleteBearerReqs_Object = MibTableColumn
cGtpv2DeleteBearerReqs = _CGtpv2DeleteBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 7),
    _CGtpv2DeleteBearerReqs_Type()
)
cGtpv2DeleteBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2DeleteBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2DeleteBearerReqs.setUnits("messages")
_CGtpv2ChangeNotifReqs_Type = Counter32
_CGtpv2ChangeNotifReqs_Object = MibTableColumn
cGtpv2ChangeNotifReqs = _CGtpv2ChangeNotifReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 8),
    _CGtpv2ChangeNotifReqs_Type()
)
cGtpv2ChangeNotifReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2ChangeNotifReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2ChangeNotifReqs.setUnits("messages")
_CGtpv2ModifyBearerCmds_Type = Counter32
_CGtpv2ModifyBearerCmds_Object = MibTableColumn
cGtpv2ModifyBearerCmds = _CGtpv2ModifyBearerCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 9),
    _CGtpv2ModifyBearerCmds_Type()
)
cGtpv2ModifyBearerCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2ModifyBearerCmds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2ModifyBearerCmds.setUnits("messages")
_CGtpv2DeleteBearerCmds_Type = Counter32
_CGtpv2DeleteBearerCmds_Object = MibTableColumn
cGtpv2DeleteBearerCmds = _CGtpv2DeleteBearerCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 10),
    _CGtpv2DeleteBearerCmds_Type()
)
cGtpv2DeleteBearerCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2DeleteBearerCmds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2DeleteBearerCmds.setUnits("messages")
_CGtpv2BearerResrcCmds_Type = Counter32
_CGtpv2BearerResrcCmds_Object = MibTableColumn
cGtpv2BearerResrcCmds = _CGtpv2BearerResrcCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 11),
    _CGtpv2BearerResrcCmds_Type()
)
cGtpv2BearerResrcCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2BearerResrcCmds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2BearerResrcCmds.setUnits("messages")
_CGtpv2DeletePdnConnSetReqs_Type = Counter32
_CGtpv2DeletePdnConnSetReqs_Object = MibTableColumn
cGtpv2DeletePdnConnSetReqs = _CGtpv2DeletePdnConnSetReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 12),
    _CGtpv2DeletePdnConnSetReqs_Type()
)
cGtpv2DeletePdnConnSetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2DeletePdnConnSetReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2DeletePdnConnSetReqs.setUnits("messages")
_CGtpv2RelAccessBearerReqs_Type = Counter32
_CGtpv2RelAccessBearerReqs_Object = MibTableColumn
cGtpv2RelAccessBearerReqs = _CGtpv2RelAccessBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 13),
    _CGtpv2RelAccessBearerReqs_Type()
)
cGtpv2RelAccessBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2RelAccessBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2RelAccessBearerReqs.setUnits("messages")
_CGtpv2DownlinkDataNotifs_Type = Counter32
_CGtpv2DownlinkDataNotifs_Object = MibTableColumn
cGtpv2DownlinkDataNotifs = _CGtpv2DownlinkDataNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 14),
    _CGtpv2DownlinkDataNotifs_Type()
)
cGtpv2DownlinkDataNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2DownlinkDataNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2DownlinkDataNotifs.setUnits("messages")
_CGtpv2CreateIndirectTunnelReqs_Type = Counter32
_CGtpv2CreateIndirectTunnelReqs_Object = MibTableColumn
cGtpv2CreateIndirectTunnelReqs = _CGtpv2CreateIndirectTunnelReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 15),
    _CGtpv2CreateIndirectTunnelReqs_Type()
)
cGtpv2CreateIndirectTunnelReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2CreateIndirectTunnelReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2CreateIndirectTunnelReqs.setUnits("messages")
_CGtpv2DeleteIndirectTunnelReqs_Type = Counter32
_CGtpv2DeleteIndirectTunnelReqs_Object = MibTableColumn
cGtpv2DeleteIndirectTunnelReqs = _CGtpv2DeleteIndirectTunnelReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 16),
    _CGtpv2DeleteIndirectTunnelReqs_Type()
)
cGtpv2DeleteIndirectTunnelReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2DeleteIndirectTunnelReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2DeleteIndirectTunnelReqs.setUnits("messages")
_CGtpv2SuspendNotifs_Type = Counter32
_CGtpv2SuspendNotifs_Object = MibTableColumn
cGtpv2SuspendNotifs = _CGtpv2SuspendNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 17),
    _CGtpv2SuspendNotifs_Type()
)
cGtpv2SuspendNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2SuspendNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2SuspendNotifs.setUnits("messages")
_CGtpv2ResumeNotifs_Type = Counter32
_CGtpv2ResumeNotifs_Object = MibTableColumn
cGtpv2ResumeNotifs = _CGtpv2ResumeNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 18),
    _CGtpv2ResumeNotifs_Type()
)
cGtpv2ResumeNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2ResumeNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2ResumeNotifs.setUnits("messages")
_CGtpv2EchoReqs_Type = Counter32
_CGtpv2EchoReqs_Object = MibTableColumn
cGtpv2EchoReqs = _CGtpv2EchoReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 3, 1, 19),
    _CGtpv2EchoReqs_Type()
)
cGtpv2EchoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2EchoReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2EchoReqs.setUnits("messages")
_CGtpv2RspMsgStatsTable_Object = MibTable
cGtpv2RspMsgStatsTable = _CGtpv2RspMsgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cGtpv2RspMsgStatsTable.setStatus("current")
_CGtpv2RspMsgStatsEntry_Object = MibTableRow
cGtpv2RspMsgStatsEntry = _CGtpv2RspMsgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1)
)
cGtpv2RspMsgStatsEntry.setIndexNames(
    (0, "CISCO-GTPV2-MIB", "cGtpv2MsgRspAction"),
)
if mibBuilder.loadTexts:
    cGtpv2RspMsgStatsEntry.setStatus("current")
_CGtpv2MsgRspAction_Type = CGtpv2Action
_CGtpv2MsgRspAction_Object = MibTableColumn
cGtpv2MsgRspAction = _CGtpv2MsgRspAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 1),
    _CGtpv2MsgRspAction_Type()
)
cGtpv2MsgRspAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpv2MsgRspAction.setStatus("current")
_CGtpv2CreateSessRsps_Type = Counter32
_CGtpv2CreateSessRsps_Object = MibTableColumn
cGtpv2CreateSessRsps = _CGtpv2CreateSessRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 2),
    _CGtpv2CreateSessRsps_Type()
)
cGtpv2CreateSessRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2CreateSessRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2CreateSessRsps.setUnits("messages")
_CGtpv2DeleteSessRsps_Type = Counter32
_CGtpv2DeleteSessRsps_Object = MibTableColumn
cGtpv2DeleteSessRsps = _CGtpv2DeleteSessRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 3),
    _CGtpv2DeleteSessRsps_Type()
)
cGtpv2DeleteSessRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2DeleteSessRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2DeleteSessRsps.setUnits("messages")
_CGtpv2CreateBearerRsps_Type = Counter32
_CGtpv2CreateBearerRsps_Object = MibTableColumn
cGtpv2CreateBearerRsps = _CGtpv2CreateBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 4),
    _CGtpv2CreateBearerRsps_Type()
)
cGtpv2CreateBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2CreateBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2CreateBearerRsps.setUnits("messages")
_CGtpv2ModifyBearerRsps_Type = Counter32
_CGtpv2ModifyBearerRsps_Object = MibTableColumn
cGtpv2ModifyBearerRsps = _CGtpv2ModifyBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 5),
    _CGtpv2ModifyBearerRsps_Type()
)
cGtpv2ModifyBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2ModifyBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2ModifyBearerRsps.setUnits("messages")
_CGtpv2UpdateBearerRsps_Type = Counter32
_CGtpv2UpdateBearerRsps_Object = MibTableColumn
cGtpv2UpdateBearerRsps = _CGtpv2UpdateBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 6),
    _CGtpv2UpdateBearerRsps_Type()
)
cGtpv2UpdateBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2UpdateBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2UpdateBearerRsps.setUnits("messages")
_CGtpv2DeleteBearerRsps_Type = Counter32
_CGtpv2DeleteBearerRsps_Object = MibTableColumn
cGtpv2DeleteBearerRsps = _CGtpv2DeleteBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 7),
    _CGtpv2DeleteBearerRsps_Type()
)
cGtpv2DeleteBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2DeleteBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2DeleteBearerRsps.setUnits("messages")
_CGtpv2ModifyBearerFailInds_Type = Counter32
_CGtpv2ModifyBearerFailInds_Object = MibTableColumn
cGtpv2ModifyBearerFailInds = _CGtpv2ModifyBearerFailInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 8),
    _CGtpv2ModifyBearerFailInds_Type()
)
cGtpv2ModifyBearerFailInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2ModifyBearerFailInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2ModifyBearerFailInds.setUnits("messages")
_CGtpv2DeleteBearerFailInds_Type = Counter32
_CGtpv2DeleteBearerFailInds_Object = MibTableColumn
cGtpv2DeleteBearerFailInds = _CGtpv2DeleteBearerFailInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 9),
    _CGtpv2DeleteBearerFailInds_Type()
)
cGtpv2DeleteBearerFailInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2DeleteBearerFailInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2DeleteBearerFailInds.setUnits("messages")
_CGtpv2BearerResrcFailInds_Type = Counter32
_CGtpv2BearerResrcFailInds_Object = MibTableColumn
cGtpv2BearerResrcFailInds = _CGtpv2BearerResrcFailInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 10),
    _CGtpv2BearerResrcFailInds_Type()
)
cGtpv2BearerResrcFailInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2BearerResrcFailInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2BearerResrcFailInds.setUnits("messages")
_CGtpv2DeletePdnConnSetRsps_Type = Counter32
_CGtpv2DeletePdnConnSetRsps_Object = MibTableColumn
cGtpv2DeletePdnConnSetRsps = _CGtpv2DeletePdnConnSetRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 11),
    _CGtpv2DeletePdnConnSetRsps_Type()
)
cGtpv2DeletePdnConnSetRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2DeletePdnConnSetRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2DeletePdnConnSetRsps.setUnits("messages")
_CGtpv2RelAccessBearerRsps_Type = Counter32
_CGtpv2RelAccessBearerRsps_Object = MibTableColumn
cGtpv2RelAccessBearerRsps = _CGtpv2RelAccessBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 12),
    _CGtpv2RelAccessBearerRsps_Type()
)
cGtpv2RelAccessBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2RelAccessBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2RelAccessBearerRsps.setUnits("messages")
_CGtpv2DownlinkDataNotifAcks_Type = Counter32
_CGtpv2DownlinkDataNotifAcks_Object = MibTableColumn
cGtpv2DownlinkDataNotifAcks = _CGtpv2DownlinkDataNotifAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 13),
    _CGtpv2DownlinkDataNotifAcks_Type()
)
cGtpv2DownlinkDataNotifAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2DownlinkDataNotifAcks.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2DownlinkDataNotifAcks.setUnits("messages")
_CGtpv2DownlinkDataNotifFailInds_Type = Counter32
_CGtpv2DownlinkDataNotifFailInds_Object = MibTableColumn
cGtpv2DownlinkDataNotifFailInds = _CGtpv2DownlinkDataNotifFailInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 14),
    _CGtpv2DownlinkDataNotifFailInds_Type()
)
cGtpv2DownlinkDataNotifFailInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2DownlinkDataNotifFailInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2DownlinkDataNotifFailInds.setUnits("messages")
_CGtpv2CreateIndirectTunnelRsps_Type = Counter32
_CGtpv2CreateIndirectTunnelRsps_Object = MibTableColumn
cGtpv2CreateIndirectTunnelRsps = _CGtpv2CreateIndirectTunnelRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 15),
    _CGtpv2CreateIndirectTunnelRsps_Type()
)
cGtpv2CreateIndirectTunnelRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2CreateIndirectTunnelRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2CreateIndirectTunnelRsps.setUnits("messages")
_CGtpv2DeleteIndirectTunnelRsps_Type = Counter32
_CGtpv2DeleteIndirectTunnelRsps_Object = MibTableColumn
cGtpv2DeleteIndirectTunnelRsps = _CGtpv2DeleteIndirectTunnelRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 16),
    _CGtpv2DeleteIndirectTunnelRsps_Type()
)
cGtpv2DeleteIndirectTunnelRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2DeleteIndirectTunnelRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2DeleteIndirectTunnelRsps.setUnits("messages")
_CGtpv2SuspendNotifAcks_Type = Counter32
_CGtpv2SuspendNotifAcks_Object = MibTableColumn
cGtpv2SuspendNotifAcks = _CGtpv2SuspendNotifAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 17),
    _CGtpv2SuspendNotifAcks_Type()
)
cGtpv2SuspendNotifAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2SuspendNotifAcks.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2SuspendNotifAcks.setUnits("messages")
_CGtpv2ResumeNotifAck_Type = Counter32
_CGtpv2ResumeNotifAck_Object = MibTableColumn
cGtpv2ResumeNotifAck = _CGtpv2ResumeNotifAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 18),
    _CGtpv2ResumeNotifAck_Type()
)
cGtpv2ResumeNotifAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2ResumeNotifAck.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2ResumeNotifAck.setUnits("messages")
_CGtpv2EchoRsps_Type = Counter32
_CGtpv2EchoRsps_Object = MibTableColumn
cGtpv2EchoRsps = _CGtpv2EchoRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 4, 1, 19),
    _CGtpv2EchoRsps_Type()
)
cGtpv2EchoRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2EchoRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2EchoRsps.setUnits("messages")
_CGtpv2SentStopPageInds_Type = Counter32
_CGtpv2SentStopPageInds_Object = MibScalar
cGtpv2SentStopPageInds = _CGtpv2SentStopPageInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 5),
    _CGtpv2SentStopPageInds_Type()
)
cGtpv2SentStopPageInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2SentStopPageInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2SentStopPageInds.setUnits("messages")
_CGtpv2Initv2tov1Handoffs_Type = Counter32
_CGtpv2Initv2tov1Handoffs_Object = MibScalar
cGtpv2Initv2tov1Handoffs = _CGtpv2Initv2tov1Handoffs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 6),
    _CGtpv2Initv2tov1Handoffs_Type()
)
cGtpv2Initv2tov1Handoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2Initv2tov1Handoffs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2Initv2tov1Handoffs.setUnits("messages")
_CGtpv2Succv2tov1Handoffs_Type = Counter32
_CGtpv2Succv2tov1Handoffs_Object = MibScalar
cGtpv2Succv2tov1Handoffs = _CGtpv2Succv2tov1Handoffs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 7),
    _CGtpv2Succv2tov1Handoffs_Type()
)
cGtpv2Succv2tov1Handoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2Succv2tov1Handoffs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2Succv2tov1Handoffs.setUnits("messages")
_CGtpv2Initv1tov2Handoffs_Type = Counter32
_CGtpv2Initv1tov2Handoffs_Object = MibScalar
cGtpv2Initv1tov2Handoffs = _CGtpv2Initv1tov2Handoffs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 8),
    _CGtpv2Initv1tov2Handoffs_Type()
)
cGtpv2Initv1tov2Handoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2Initv1tov2Handoffs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2Initv1tov2Handoffs.setUnits("messages")
_CGtpv2Succv1tov2Handoffs_Type = Counter32
_CGtpv2Succv1tov2Handoffs_Object = MibScalar
cGtpv2Succv1tov2Handoffs = _CGtpv2Succv1tov2Handoffs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 9),
    _CGtpv2Succv1tov2Handoffs_Type()
)
cGtpv2Succv1tov2Handoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2Succv1tov2Handoffs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2Succv1tov2Handoffs.setUnits("messages")
_CGtpv2TotalN3Retransmits_Type = Counter32
_CGtpv2TotalN3Retransmits_Object = MibScalar
cGtpv2TotalN3Retransmits = _CGtpv2TotalN3Retransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 1, 10),
    _CGtpv2TotalN3Retransmits_Type()
)
cGtpv2TotalN3Retransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv2TotalN3Retransmits.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv2TotalN3Retransmits.setUnits("messages")
_CGtpPathGtpv2Statistics_ObjectIdentity = ObjectIdentity
cGtpPathGtpv2Statistics = _CGtpPathGtpv2Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2)
)
_CGtpPathGtpv2StatisticsTable_Object = MibTable
cGtpPathGtpv2StatisticsTable = _CGtpPathGtpv2StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cGtpPathGtpv2StatisticsTable.setStatus("current")
_CGtpPathGtpv2StatisticsEntry_Object = MibTableRow
cGtpPathGtpv2StatisticsEntry = _CGtpPathGtpv2StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cGtpPathGtpv2StatisticsEntry.setStatus("current")
_CGtpPathDroppedSigMsgs_Type = Counter32
_CGtpPathDroppedSigMsgs_Object = MibTableColumn
cGtpPathDroppedSigMsgs = _CGtpPathDroppedSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 1, 1, 1),
    _CGtpPathDroppedSigMsgs_Type()
)
cGtpPathDroppedSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathDroppedSigMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathDroppedSigMsgs.setUnits("messages")
_CGtpPathSentStopPageInds_Type = Counter32
_CGtpPathSentStopPageInds_Object = MibTableColumn
cGtpPathSentStopPageInds = _CGtpPathSentStopPageInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 1, 1, 2),
    _CGtpPathSentStopPageInds_Type()
)
cGtpPathSentStopPageInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathSentStopPageInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathSentStopPageInds.setUnits("messages")
_CGtpPathGtpv2ReqMsgTable_Object = MibTable
cGtpPathGtpv2ReqMsgTable = _CGtpPathGtpv2ReqMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cGtpPathGtpv2ReqMsgTable.setStatus("current")
_CGtpPathGtpv2ReqMsgEntry_Object = MibTableRow
cGtpPathGtpv2ReqMsgEntry = _CGtpPathGtpv2ReqMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1)
)
cGtpPathGtpv2ReqMsgEntry.setIndexNames(
    (0, "CISCO-GTP-MIB", "cGtpPathAddressType"),
    (0, "CISCO-GTP-MIB", "cGtpPathAddress"),
    (0, "CISCO-GTP-MIB", "cGtpPathPort"),
    (0, "CISCO-GTPV2-MIB", "cGtpPathMsgReqAction"),
)
if mibBuilder.loadTexts:
    cGtpPathGtpv2ReqMsgEntry.setStatus("current")
_CGtpPathMsgReqAction_Type = CGtpv2Action
_CGtpPathMsgReqAction_Object = MibTableColumn
cGtpPathMsgReqAction = _CGtpPathMsgReqAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 1),
    _CGtpPathMsgReqAction_Type()
)
cGtpPathMsgReqAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpPathMsgReqAction.setStatus("current")
_CGtpPathCreateSessReqs_Type = Counter32
_CGtpPathCreateSessReqs_Object = MibTableColumn
cGtpPathCreateSessReqs = _CGtpPathCreateSessReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 2),
    _CGtpPathCreateSessReqs_Type()
)
cGtpPathCreateSessReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathCreateSessReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathCreateSessReqs.setUnits("messages")
_CGtpPathDeleteSessReqs_Type = Counter32
_CGtpPathDeleteSessReqs_Object = MibTableColumn
cGtpPathDeleteSessReqs = _CGtpPathDeleteSessReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 3),
    _CGtpPathDeleteSessReqs_Type()
)
cGtpPathDeleteSessReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathDeleteSessReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathDeleteSessReqs.setUnits("messages")
_CGtpPathCreateBearerReqs_Type = Counter32
_CGtpPathCreateBearerReqs_Object = MibTableColumn
cGtpPathCreateBearerReqs = _CGtpPathCreateBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 4),
    _CGtpPathCreateBearerReqs_Type()
)
cGtpPathCreateBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathCreateBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathCreateBearerReqs.setUnits("messages")
_CGtpPathModifyBearerReqs_Type = Counter32
_CGtpPathModifyBearerReqs_Object = MibTableColumn
cGtpPathModifyBearerReqs = _CGtpPathModifyBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 5),
    _CGtpPathModifyBearerReqs_Type()
)
cGtpPathModifyBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathModifyBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathModifyBearerReqs.setUnits("messages")
_CGtpPathUpdateBearerReqs_Type = Counter32
_CGtpPathUpdateBearerReqs_Object = MibTableColumn
cGtpPathUpdateBearerReqs = _CGtpPathUpdateBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 6),
    _CGtpPathUpdateBearerReqs_Type()
)
cGtpPathUpdateBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathUpdateBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathUpdateBearerReqs.setUnits("messages")
_CGtpPathDeleteBearerReqs_Type = Counter32
_CGtpPathDeleteBearerReqs_Object = MibTableColumn
cGtpPathDeleteBearerReqs = _CGtpPathDeleteBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 7),
    _CGtpPathDeleteBearerReqs_Type()
)
cGtpPathDeleteBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathDeleteBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathDeleteBearerReqs.setUnits("messages")
_CGtpPathChangeNotifReqs_Type = Counter32
_CGtpPathChangeNotifReqs_Object = MibTableColumn
cGtpPathChangeNotifReqs = _CGtpPathChangeNotifReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 8),
    _CGtpPathChangeNotifReqs_Type()
)
cGtpPathChangeNotifReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathChangeNotifReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathChangeNotifReqs.setUnits("messages")
_CGtpPathModifyBearerCmds_Type = Counter32
_CGtpPathModifyBearerCmds_Object = MibTableColumn
cGtpPathModifyBearerCmds = _CGtpPathModifyBearerCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 9),
    _CGtpPathModifyBearerCmds_Type()
)
cGtpPathModifyBearerCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathModifyBearerCmds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathModifyBearerCmds.setUnits("messages")
_CGtpPathDeleteBearerCmds_Type = Counter32
_CGtpPathDeleteBearerCmds_Object = MibTableColumn
cGtpPathDeleteBearerCmds = _CGtpPathDeleteBearerCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 10),
    _CGtpPathDeleteBearerCmds_Type()
)
cGtpPathDeleteBearerCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathDeleteBearerCmds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathDeleteBearerCmds.setUnits("messages")
_CGtpPathBearerResrcCmds_Type = Counter32
_CGtpPathBearerResrcCmds_Object = MibTableColumn
cGtpPathBearerResrcCmds = _CGtpPathBearerResrcCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 11),
    _CGtpPathBearerResrcCmds_Type()
)
cGtpPathBearerResrcCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathBearerResrcCmds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathBearerResrcCmds.setUnits("messages")
_CGtpPathDeletePdnConnSetReqs_Type = Counter32
_CGtpPathDeletePdnConnSetReqs_Object = MibTableColumn
cGtpPathDeletePdnConnSetReqs = _CGtpPathDeletePdnConnSetReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 12),
    _CGtpPathDeletePdnConnSetReqs_Type()
)
cGtpPathDeletePdnConnSetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathDeletePdnConnSetReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathDeletePdnConnSetReqs.setUnits("messages")
_CGtpPathRelAccessBearerReqs_Type = Counter32
_CGtpPathRelAccessBearerReqs_Object = MibTableColumn
cGtpPathRelAccessBearerReqs = _CGtpPathRelAccessBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 13),
    _CGtpPathRelAccessBearerReqs_Type()
)
cGtpPathRelAccessBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathRelAccessBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathRelAccessBearerReqs.setUnits("messages")
_CGtpPathDownlinkDataNotifs_Type = Counter32
_CGtpPathDownlinkDataNotifs_Object = MibTableColumn
cGtpPathDownlinkDataNotifs = _CGtpPathDownlinkDataNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 14),
    _CGtpPathDownlinkDataNotifs_Type()
)
cGtpPathDownlinkDataNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathDownlinkDataNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathDownlinkDataNotifs.setUnits("messages")
_CGtpPathSuspendNotifs_Type = Counter32
_CGtpPathSuspendNotifs_Object = MibTableColumn
cGtpPathSuspendNotifs = _CGtpPathSuspendNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 15),
    _CGtpPathSuspendNotifs_Type()
)
cGtpPathSuspendNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathSuspendNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathSuspendNotifs.setUnits("messages")
_CGtpPathResumeNotifs_Type = Counter32
_CGtpPathResumeNotifs_Object = MibTableColumn
cGtpPathResumeNotifs = _CGtpPathResumeNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 16),
    _CGtpPathResumeNotifs_Type()
)
cGtpPathResumeNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathResumeNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathResumeNotifs.setUnits("messages")
_CGtpPathEchoReqs_Type = Counter32
_CGtpPathEchoReqs_Object = MibTableColumn
cGtpPathEchoReqs = _CGtpPathEchoReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 17),
    _CGtpPathEchoReqs_Type()
)
cGtpPathEchoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathEchoReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathEchoReqs.setUnits("messages")
_CGtpPathVerNotSupported_Type = Counter32
_CGtpPathVerNotSupported_Object = MibTableColumn
cGtpPathVerNotSupported = _CGtpPathVerNotSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 2, 1, 18),
    _CGtpPathVerNotSupported_Type()
)
cGtpPathVerNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathVerNotSupported.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathVerNotSupported.setUnits("messages")
_CGtpPathGtpv2RspMsgTable_Object = MibTable
cGtpPathGtpv2RspMsgTable = _CGtpPathGtpv2RspMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cGtpPathGtpv2RspMsgTable.setStatus("current")
_CGtpPathGtpv2RspMsgEntry_Object = MibTableRow
cGtpPathGtpv2RspMsgEntry = _CGtpPathGtpv2RspMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1)
)
cGtpPathGtpv2RspMsgEntry.setIndexNames(
    (0, "CISCO-GTP-MIB", "cGtpPathAddressType"),
    (0, "CISCO-GTP-MIB", "cGtpPathAddress"),
    (0, "CISCO-GTP-MIB", "cGtpPathPort"),
    (0, "CISCO-GTPV2-MIB", "cGtpPathMsgRspAction"),
)
if mibBuilder.loadTexts:
    cGtpPathGtpv2RspMsgEntry.setStatus("current")
_CGtpPathMsgRspAction_Type = CGtpv2Action
_CGtpPathMsgRspAction_Object = MibTableColumn
cGtpPathMsgRspAction = _CGtpPathMsgRspAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 1),
    _CGtpPathMsgRspAction_Type()
)
cGtpPathMsgRspAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpPathMsgRspAction.setStatus("current")
_CGtpPathCreateSessRsps_Type = Counter32
_CGtpPathCreateSessRsps_Object = MibTableColumn
cGtpPathCreateSessRsps = _CGtpPathCreateSessRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 2),
    _CGtpPathCreateSessRsps_Type()
)
cGtpPathCreateSessRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathCreateSessRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathCreateSessRsps.setUnits("messages")
_CGtpPathDeleteSessRsps_Type = Counter32
_CGtpPathDeleteSessRsps_Object = MibTableColumn
cGtpPathDeleteSessRsps = _CGtpPathDeleteSessRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 3),
    _CGtpPathDeleteSessRsps_Type()
)
cGtpPathDeleteSessRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathDeleteSessRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathDeleteSessRsps.setUnits("messages")
_CGtpPathCreateBearerRsps_Type = Counter32
_CGtpPathCreateBearerRsps_Object = MibTableColumn
cGtpPathCreateBearerRsps = _CGtpPathCreateBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 4),
    _CGtpPathCreateBearerRsps_Type()
)
cGtpPathCreateBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathCreateBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathCreateBearerRsps.setUnits("messages")
_CGtpPathModifyBearerRsps_Type = Counter32
_CGtpPathModifyBearerRsps_Object = MibTableColumn
cGtpPathModifyBearerRsps = _CGtpPathModifyBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 5),
    _CGtpPathModifyBearerRsps_Type()
)
cGtpPathModifyBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathModifyBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathModifyBearerRsps.setUnits("messages")
_CGtpPathUpdateBearerRsps_Type = Counter32
_CGtpPathUpdateBearerRsps_Object = MibTableColumn
cGtpPathUpdateBearerRsps = _CGtpPathUpdateBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 6),
    _CGtpPathUpdateBearerRsps_Type()
)
cGtpPathUpdateBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathUpdateBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathUpdateBearerRsps.setUnits("messages")
_CGtpPathDeleteBearerRsps_Type = Counter32
_CGtpPathDeleteBearerRsps_Object = MibTableColumn
cGtpPathDeleteBearerRsps = _CGtpPathDeleteBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 7),
    _CGtpPathDeleteBearerRsps_Type()
)
cGtpPathDeleteBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathDeleteBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathDeleteBearerRsps.setUnits("messages")
_CGtpPathModifyBearerFailInds_Type = Counter32
_CGtpPathModifyBearerFailInds_Object = MibTableColumn
cGtpPathModifyBearerFailInds = _CGtpPathModifyBearerFailInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 8),
    _CGtpPathModifyBearerFailInds_Type()
)
cGtpPathModifyBearerFailInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathModifyBearerFailInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathModifyBearerFailInds.setUnits("messages")
_CGtpPathDeleteBearerFailInds_Type = Counter32
_CGtpPathDeleteBearerFailInds_Object = MibTableColumn
cGtpPathDeleteBearerFailInds = _CGtpPathDeleteBearerFailInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 9),
    _CGtpPathDeleteBearerFailInds_Type()
)
cGtpPathDeleteBearerFailInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathDeleteBearerFailInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathDeleteBearerFailInds.setUnits("messages")
_CGtpPathBearerResrcFailInds_Type = Counter32
_CGtpPathBearerResrcFailInds_Object = MibTableColumn
cGtpPathBearerResrcFailInds = _CGtpPathBearerResrcFailInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 10),
    _CGtpPathBearerResrcFailInds_Type()
)
cGtpPathBearerResrcFailInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathBearerResrcFailInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathBearerResrcFailInds.setUnits("messages")
_CGtpPathDeletePdnConnSetRsps_Type = Counter32
_CGtpPathDeletePdnConnSetRsps_Object = MibTableColumn
cGtpPathDeletePdnConnSetRsps = _CGtpPathDeletePdnConnSetRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 11),
    _CGtpPathDeletePdnConnSetRsps_Type()
)
cGtpPathDeletePdnConnSetRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathDeletePdnConnSetRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathDeletePdnConnSetRsps.setUnits("messages")
_CGtpPathRelAccessBearerRsps_Type = Counter32
_CGtpPathRelAccessBearerRsps_Object = MibTableColumn
cGtpPathRelAccessBearerRsps = _CGtpPathRelAccessBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 12),
    _CGtpPathRelAccessBearerRsps_Type()
)
cGtpPathRelAccessBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathRelAccessBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathRelAccessBearerRsps.setUnits("messages")
_CGtpPathDownlinkDataNotifAcks_Type = Counter32
_CGtpPathDownlinkDataNotifAcks_Object = MibTableColumn
cGtpPathDownlinkDataNotifAcks = _CGtpPathDownlinkDataNotifAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 13),
    _CGtpPathDownlinkDataNotifAcks_Type()
)
cGtpPathDownlinkDataNotifAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathDownlinkDataNotifAcks.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathDownlinkDataNotifAcks.setUnits("messages")
_CGtpPathDownlinkDataNotifFailInds_Type = Counter32
_CGtpPathDownlinkDataNotifFailInds_Object = MibTableColumn
cGtpPathDownlinkDataNotifFailInds = _CGtpPathDownlinkDataNotifFailInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 14),
    _CGtpPathDownlinkDataNotifFailInds_Type()
)
cGtpPathDownlinkDataNotifFailInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathDownlinkDataNotifFailInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathDownlinkDataNotifFailInds.setUnits("messages")
_CGtpPathSuspendNotifAcks_Type = Counter32
_CGtpPathSuspendNotifAcks_Object = MibTableColumn
cGtpPathSuspendNotifAcks = _CGtpPathSuspendNotifAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 15),
    _CGtpPathSuspendNotifAcks_Type()
)
cGtpPathSuspendNotifAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathSuspendNotifAcks.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathSuspendNotifAcks.setUnits("messages")
_CGtpPathResumeNotifAcks_Type = Counter32
_CGtpPathResumeNotifAcks_Object = MibTableColumn
cGtpPathResumeNotifAcks = _CGtpPathResumeNotifAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 16),
    _CGtpPathResumeNotifAcks_Type()
)
cGtpPathResumeNotifAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathResumeNotifAcks.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathResumeNotifAcks.setUnits("messages")
_CGtpPathEchoRsps_Type = Counter32
_CGtpPathEchoRsps_Object = MibTableColumn
cGtpPathEchoRsps = _CGtpPathEchoRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 2, 3, 1, 17),
    _CGtpPathEchoRsps_Type()
)
cGtpPathEchoRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathEchoRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathEchoRsps.setUnits("messages")
_CGtpPathHistGtpv2Statistics_ObjectIdentity = ObjectIdentity
cGtpPathHistGtpv2Statistics = _CGtpPathHistGtpv2Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3)
)
_CGtpPathHistGtpv2StatisticsTable_Object = MibTable
cGtpPathHistGtpv2StatisticsTable = _CGtpPathHistGtpv2StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cGtpPathHistGtpv2StatisticsTable.setStatus("current")
_CGtpPathHistGtpv2StatisticsEntry_Object = MibTableRow
cGtpPathHistGtpv2StatisticsEntry = _CGtpPathHistGtpv2StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cGtpPathHistGtpv2StatisticsEntry.setStatus("current")
_CGtpPathHistDroppedSigMsgs_Type = Counter32
_CGtpPathHistDroppedSigMsgs_Object = MibTableColumn
cGtpPathHistDroppedSigMsgs = _CGtpPathHistDroppedSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 1, 1, 1),
    _CGtpPathHistDroppedSigMsgs_Type()
)
cGtpPathHistDroppedSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistDroppedSigMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistDroppedSigMsgs.setUnits("messages")
_CGtpPathHistSentStopPageInds_Type = Counter32
_CGtpPathHistSentStopPageInds_Object = MibTableColumn
cGtpPathHistSentStopPageInds = _CGtpPathHistSentStopPageInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 1, 1, 2),
    _CGtpPathHistSentStopPageInds_Type()
)
cGtpPathHistSentStopPageInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistSentStopPageInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistSentStopPageInds.setUnits("messages")
_CGtpPathHistGtpv2ReqMsgTable_Object = MibTable
cGtpPathHistGtpv2ReqMsgTable = _CGtpPathHistGtpv2ReqMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cGtpPathHistGtpv2ReqMsgTable.setStatus("current")
_CGtpPathHistGtpv2ReqMsgEntry_Object = MibTableRow
cGtpPathHistGtpv2ReqMsgEntry = _CGtpPathHistGtpv2ReqMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1)
)
cGtpPathHistGtpv2ReqMsgEntry.setIndexNames(
    (0, "CISCO-GTP-MIB", "cGtpHistIndex"),
    (0, "CISCO-GTP-MIB", "cGtpHistRemoteAddrType"),
    (0, "CISCO-GTP-MIB", "cGtpHistRemoteAddress"),
    (0, "CISCO-GTP-MIB", "cGtpHistRemotePort"),
    (0, "CISCO-GTPV2-MIB", "cGtpPathHistMsgReqAction"),
)
if mibBuilder.loadTexts:
    cGtpPathHistGtpv2ReqMsgEntry.setStatus("current")
_CGtpPathHistMsgReqAction_Type = CGtpv2Action
_CGtpPathHistMsgReqAction_Object = MibTableColumn
cGtpPathHistMsgReqAction = _CGtpPathHistMsgReqAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 1),
    _CGtpPathHistMsgReqAction_Type()
)
cGtpPathHistMsgReqAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpPathHistMsgReqAction.setStatus("current")
_CGtpPathHistCreateSessReqs_Type = Counter32
_CGtpPathHistCreateSessReqs_Object = MibTableColumn
cGtpPathHistCreateSessReqs = _CGtpPathHistCreateSessReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 2),
    _CGtpPathHistCreateSessReqs_Type()
)
cGtpPathHistCreateSessReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistCreateSessReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistCreateSessReqs.setUnits("messages")
_CGtpPathHistDeleteSessReqs_Type = Counter32
_CGtpPathHistDeleteSessReqs_Object = MibTableColumn
cGtpPathHistDeleteSessReqs = _CGtpPathHistDeleteSessReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 3),
    _CGtpPathHistDeleteSessReqs_Type()
)
cGtpPathHistDeleteSessReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistDeleteSessReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistDeleteSessReqs.setUnits("messages")
_CGtpPathHistCreateBearerReqs_Type = Counter32
_CGtpPathHistCreateBearerReqs_Object = MibTableColumn
cGtpPathHistCreateBearerReqs = _CGtpPathHistCreateBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 4),
    _CGtpPathHistCreateBearerReqs_Type()
)
cGtpPathHistCreateBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistCreateBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistCreateBearerReqs.setUnits("messages")
_CGtpPathHistModifyBearerReqs_Type = Counter32
_CGtpPathHistModifyBearerReqs_Object = MibTableColumn
cGtpPathHistModifyBearerReqs = _CGtpPathHistModifyBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 5),
    _CGtpPathHistModifyBearerReqs_Type()
)
cGtpPathHistModifyBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistModifyBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistModifyBearerReqs.setUnits("messages")
_CGtpPathHistUpdateBearerReqs_Type = Counter32
_CGtpPathHistUpdateBearerReqs_Object = MibTableColumn
cGtpPathHistUpdateBearerReqs = _CGtpPathHistUpdateBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 6),
    _CGtpPathHistUpdateBearerReqs_Type()
)
cGtpPathHistUpdateBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistUpdateBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistUpdateBearerReqs.setUnits("messages")
_CGtpPathHistDeleteBearerReqs_Type = Counter32
_CGtpPathHistDeleteBearerReqs_Object = MibTableColumn
cGtpPathHistDeleteBearerReqs = _CGtpPathHistDeleteBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 7),
    _CGtpPathHistDeleteBearerReqs_Type()
)
cGtpPathHistDeleteBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistDeleteBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistDeleteBearerReqs.setUnits("messages")
_CGtpPathHistChangeNotifReqs_Type = Counter32
_CGtpPathHistChangeNotifReqs_Object = MibTableColumn
cGtpPathHistChangeNotifReqs = _CGtpPathHistChangeNotifReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 8),
    _CGtpPathHistChangeNotifReqs_Type()
)
cGtpPathHistChangeNotifReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistChangeNotifReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistChangeNotifReqs.setUnits("messages")
_CGtpPathHistModifyBearerCmds_Type = Counter32
_CGtpPathHistModifyBearerCmds_Object = MibTableColumn
cGtpPathHistModifyBearerCmds = _CGtpPathHistModifyBearerCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 9),
    _CGtpPathHistModifyBearerCmds_Type()
)
cGtpPathHistModifyBearerCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistModifyBearerCmds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistModifyBearerCmds.setUnits("messages")
_CGtpPathHistDeleteBearerCmds_Type = Counter32
_CGtpPathHistDeleteBearerCmds_Object = MibTableColumn
cGtpPathHistDeleteBearerCmds = _CGtpPathHistDeleteBearerCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 10),
    _CGtpPathHistDeleteBearerCmds_Type()
)
cGtpPathHistDeleteBearerCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistDeleteBearerCmds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistDeleteBearerCmds.setUnits("messages")
_CGtpPathHistBearerResrcCmds_Type = Counter32
_CGtpPathHistBearerResrcCmds_Object = MibTableColumn
cGtpPathHistBearerResrcCmds = _CGtpPathHistBearerResrcCmds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 11),
    _CGtpPathHistBearerResrcCmds_Type()
)
cGtpPathHistBearerResrcCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistBearerResrcCmds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistBearerResrcCmds.setUnits("messages")
_CGtpPathHistDeletePdnConnSetReqs_Type = Counter32
_CGtpPathHistDeletePdnConnSetReqs_Object = MibTableColumn
cGtpPathHistDeletePdnConnSetReqs = _CGtpPathHistDeletePdnConnSetReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 12),
    _CGtpPathHistDeletePdnConnSetReqs_Type()
)
cGtpPathHistDeletePdnConnSetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistDeletePdnConnSetReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistDeletePdnConnSetReqs.setUnits("messages")
_CGtpPathHistRelAccessBearerReqs_Type = Counter32
_CGtpPathHistRelAccessBearerReqs_Object = MibTableColumn
cGtpPathHistRelAccessBearerReqs = _CGtpPathHistRelAccessBearerReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 13),
    _CGtpPathHistRelAccessBearerReqs_Type()
)
cGtpPathHistRelAccessBearerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistRelAccessBearerReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistRelAccessBearerReqs.setUnits("messages")
_CGtpPathHistDownlinkDataNotifs_Type = Counter32
_CGtpPathHistDownlinkDataNotifs_Object = MibTableColumn
cGtpPathHistDownlinkDataNotifs = _CGtpPathHistDownlinkDataNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 14),
    _CGtpPathHistDownlinkDataNotifs_Type()
)
cGtpPathHistDownlinkDataNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistDownlinkDataNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistDownlinkDataNotifs.setUnits("messages")
_CGtpPathHistSuspendNotifs_Type = Counter32
_CGtpPathHistSuspendNotifs_Object = MibTableColumn
cGtpPathHistSuspendNotifs = _CGtpPathHistSuspendNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 15),
    _CGtpPathHistSuspendNotifs_Type()
)
cGtpPathHistSuspendNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistSuspendNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistSuspendNotifs.setUnits("messages")
_CGtpPathHistResumeNotifs_Type = Counter32
_CGtpPathHistResumeNotifs_Object = MibTableColumn
cGtpPathHistResumeNotifs = _CGtpPathHistResumeNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 16),
    _CGtpPathHistResumeNotifs_Type()
)
cGtpPathHistResumeNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistResumeNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistResumeNotifs.setUnits("messages")
_CGtpPathHistEchoReqs_Type = Counter32
_CGtpPathHistEchoReqs_Object = MibTableColumn
cGtpPathHistEchoReqs = _CGtpPathHistEchoReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 17),
    _CGtpPathHistEchoReqs_Type()
)
cGtpPathHistEchoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistEchoReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistEchoReqs.setUnits("messages")
_CGtpPathHistVerNotSupported_Type = Counter32
_CGtpPathHistVerNotSupported_Object = MibTableColumn
cGtpPathHistVerNotSupported = _CGtpPathHistVerNotSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 2, 1, 18),
    _CGtpPathHistVerNotSupported_Type()
)
cGtpPathHistVerNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistVerNotSupported.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistVerNotSupported.setUnits("messages")
_CGtpPathHistGtpv2RspMsgTable_Object = MibTable
cGtpPathHistGtpv2RspMsgTable = _CGtpPathHistGtpv2RspMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cGtpPathHistGtpv2RspMsgTable.setStatus("current")
_CGtpPathHistGtpv2RspMsgEntry_Object = MibTableRow
cGtpPathHistGtpv2RspMsgEntry = _CGtpPathHistGtpv2RspMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1)
)
cGtpPathHistGtpv2RspMsgEntry.setIndexNames(
    (0, "CISCO-GTP-MIB", "cGtpHistIndex"),
    (0, "CISCO-GTP-MIB", "cGtpHistRemoteAddrType"),
    (0, "CISCO-GTP-MIB", "cGtpHistRemoteAddress"),
    (0, "CISCO-GTP-MIB", "cGtpHistRemotePort"),
    (0, "CISCO-GTPV2-MIB", "cGtpPathHistMsgRspAction"),
)
if mibBuilder.loadTexts:
    cGtpPathHistGtpv2RspMsgEntry.setStatus("current")
_CGtpPathHistMsgRspAction_Type = CGtpv2Action
_CGtpPathHistMsgRspAction_Object = MibTableColumn
cGtpPathHistMsgRspAction = _CGtpPathHistMsgRspAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 1),
    _CGtpPathHistMsgRspAction_Type()
)
cGtpPathHistMsgRspAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpPathHistMsgRspAction.setStatus("current")
_CGtpPathHistCreateSessRsps_Type = Counter32
_CGtpPathHistCreateSessRsps_Object = MibTableColumn
cGtpPathHistCreateSessRsps = _CGtpPathHistCreateSessRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 2),
    _CGtpPathHistCreateSessRsps_Type()
)
cGtpPathHistCreateSessRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistCreateSessRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistCreateSessRsps.setUnits("messages")
_CGtpPathHistDeleteSessRsps_Type = Counter32
_CGtpPathHistDeleteSessRsps_Object = MibTableColumn
cGtpPathHistDeleteSessRsps = _CGtpPathHistDeleteSessRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 3),
    _CGtpPathHistDeleteSessRsps_Type()
)
cGtpPathHistDeleteSessRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistDeleteSessRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistDeleteSessRsps.setUnits("messages")
_CGtpPathHistCreateBearerRsps_Type = Counter32
_CGtpPathHistCreateBearerRsps_Object = MibTableColumn
cGtpPathHistCreateBearerRsps = _CGtpPathHistCreateBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 4),
    _CGtpPathHistCreateBearerRsps_Type()
)
cGtpPathHistCreateBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistCreateBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistCreateBearerRsps.setUnits("messages")
_CGtpPathHistModifyBearerRsps_Type = Counter32
_CGtpPathHistModifyBearerRsps_Object = MibTableColumn
cGtpPathHistModifyBearerRsps = _CGtpPathHistModifyBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 5),
    _CGtpPathHistModifyBearerRsps_Type()
)
cGtpPathHistModifyBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistModifyBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistModifyBearerRsps.setUnits("messages")
_CGtpPathHistUpdateBearerRsps_Type = Counter32
_CGtpPathHistUpdateBearerRsps_Object = MibTableColumn
cGtpPathHistUpdateBearerRsps = _CGtpPathHistUpdateBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 6),
    _CGtpPathHistUpdateBearerRsps_Type()
)
cGtpPathHistUpdateBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistUpdateBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistUpdateBearerRsps.setUnits("messages")
_CGtpPathHistDeleteBearerRsps_Type = Counter32
_CGtpPathHistDeleteBearerRsps_Object = MibTableColumn
cGtpPathHistDeleteBearerRsps = _CGtpPathHistDeleteBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 7),
    _CGtpPathHistDeleteBearerRsps_Type()
)
cGtpPathHistDeleteBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistDeleteBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistDeleteBearerRsps.setUnits("messages")
_CGtpPathHistModifyBearerFailInds_Type = Counter32
_CGtpPathHistModifyBearerFailInds_Object = MibTableColumn
cGtpPathHistModifyBearerFailInds = _CGtpPathHistModifyBearerFailInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 8),
    _CGtpPathHistModifyBearerFailInds_Type()
)
cGtpPathHistModifyBearerFailInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistModifyBearerFailInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistModifyBearerFailInds.setUnits("messages")
_CGtpPathHistDeleteBearerFailInds_Type = Counter32
_CGtpPathHistDeleteBearerFailInds_Object = MibTableColumn
cGtpPathHistDeleteBearerFailInds = _CGtpPathHistDeleteBearerFailInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 9),
    _CGtpPathHistDeleteBearerFailInds_Type()
)
cGtpPathHistDeleteBearerFailInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistDeleteBearerFailInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistDeleteBearerFailInds.setUnits("messages")
_CGtpPathHistBearerResrcFailInds_Type = Counter32
_CGtpPathHistBearerResrcFailInds_Object = MibTableColumn
cGtpPathHistBearerResrcFailInds = _CGtpPathHistBearerResrcFailInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 10),
    _CGtpPathHistBearerResrcFailInds_Type()
)
cGtpPathHistBearerResrcFailInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistBearerResrcFailInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistBearerResrcFailInds.setUnits("messages")
_CGtpPathHistDeletePdnConnSetRsps_Type = Counter32
_CGtpPathHistDeletePdnConnSetRsps_Object = MibTableColumn
cGtpPathHistDeletePdnConnSetRsps = _CGtpPathHistDeletePdnConnSetRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 11),
    _CGtpPathHistDeletePdnConnSetRsps_Type()
)
cGtpPathHistDeletePdnConnSetRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistDeletePdnConnSetRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistDeletePdnConnSetRsps.setUnits("messages")
_CGtpPathHistRelAccessBearerRsps_Type = Counter32
_CGtpPathHistRelAccessBearerRsps_Object = MibTableColumn
cGtpPathHistRelAccessBearerRsps = _CGtpPathHistRelAccessBearerRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 12),
    _CGtpPathHistRelAccessBearerRsps_Type()
)
cGtpPathHistRelAccessBearerRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistRelAccessBearerRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistRelAccessBearerRsps.setUnits("messages")
_CGtpPathHistDownlinkDataNotifAcks_Type = Counter32
_CGtpPathHistDownlinkDataNotifAcks_Object = MibTableColumn
cGtpPathHistDownlinkDataNotifAcks = _CGtpPathHistDownlinkDataNotifAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 13),
    _CGtpPathHistDownlinkDataNotifAcks_Type()
)
cGtpPathHistDownlinkDataNotifAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistDownlinkDataNotifAcks.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistDownlinkDataNotifAcks.setUnits("messages")
_CGtpPathHistDownlinkDataNotifFailInds_Type = Counter32
_CGtpPathHistDownlinkDataNotifFailInds_Object = MibTableColumn
cGtpPathHistDownlinkDataNotifFailInds = _CGtpPathHistDownlinkDataNotifFailInds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 14),
    _CGtpPathHistDownlinkDataNotifFailInds_Type()
)
cGtpPathHistDownlinkDataNotifFailInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistDownlinkDataNotifFailInds.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistDownlinkDataNotifFailInds.setUnits("messages")
_CGtpPathHistSuspendNotifAcks_Type = Counter32
_CGtpPathHistSuspendNotifAcks_Object = MibTableColumn
cGtpPathHistSuspendNotifAcks = _CGtpPathHistSuspendNotifAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 15),
    _CGtpPathHistSuspendNotifAcks_Type()
)
cGtpPathHistSuspendNotifAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistSuspendNotifAcks.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistSuspendNotifAcks.setUnits("messages")
_CGtpPathHistResumeNotifAcks_Type = Counter32
_CGtpPathHistResumeNotifAcks_Object = MibTableColumn
cGtpPathHistResumeNotifAcks = _CGtpPathHistResumeNotifAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 16),
    _CGtpPathHistResumeNotifAcks_Type()
)
cGtpPathHistResumeNotifAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistResumeNotifAcks.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistResumeNotifAcks.setUnits("messages")
_CGtpPathHistEchoRsps_Type = Counter32
_CGtpPathHistEchoRsps_Object = MibTableColumn
cGtpPathHistEchoRsps = _CGtpPathHistEchoRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 1, 1, 3, 3, 1, 17),
    _CGtpPathHistEchoRsps_Type()
)
cGtpPathHistEchoRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathHistEchoRsps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathHistEchoRsps.setUnits("messages")
_CGtpv2MIBConformances_ObjectIdentity = ObjectIdentity
cGtpv2MIBConformances = _CGtpv2MIBConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 2)
)
_CGtpv2MIBCompliances_ObjectIdentity = ObjectIdentity
cGtpv2MIBCompliances = _CGtpv2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 2, 1)
)
_CGtpv2MIBGroups_ObjectIdentity = ObjectIdentity
cGtpv2MIBGroups = _CGtpv2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 2, 2)
)
cGtpPathStatisticsEntry.registerAugmentions(
    ("CISCO-GTPV2-MIB",
     "cGtpPathGtpv2StatisticsEntry")
)
cGtpPathGtpv2StatisticsEntry.setIndexNames(*cGtpPathStatisticsEntry.getIndexNames())
cGtpPathStatisticsHistEntry.registerAugmentions(
    ("CISCO-GTPV2-MIB",
     "cGtpPathHistGtpv2StatisticsEntry")
)
cGtpPathHistGtpv2StatisticsEntry.setIndexNames(*cGtpPathStatisticsHistEntry.getIndexNames())

# Managed Objects groups

cGtpv2MIBSystemStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 2, 2, 1)
)
cGtpv2MIBSystemStatisticsGroup.setObjects(
      *(("CISCO-GTPV2-MIB", "cGtpv2DroppedSigMsgs"),
        ("CISCO-GTPV2-MIB", "cGtpv2ReservedValueIeMsgs"),
        ("CISCO-GTPV2-MIB", "cGtpv2CreateSessReqs"),
        ("CISCO-GTPV2-MIB", "cGtpv2DeleteSessReqs"),
        ("CISCO-GTPV2-MIB", "cGtpv2CreateBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpv2ModifyBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpv2UpdateBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpv2DeleteBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpv2ChangeNotifReqs"),
        ("CISCO-GTPV2-MIB", "cGtpv2ModifyBearerCmds"),
        ("CISCO-GTPV2-MIB", "cGtpv2DeleteBearerCmds"),
        ("CISCO-GTPV2-MIB", "cGtpv2BearerResrcCmds"),
        ("CISCO-GTPV2-MIB", "cGtpv2CreateSessRsps"),
        ("CISCO-GTPV2-MIB", "cGtpv2DeleteSessRsps"),
        ("CISCO-GTPV2-MIB", "cGtpv2CreateBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpv2ModifyBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpv2UpdateBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpv2DeleteBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpv2ModifyBearerFailInds"),
        ("CISCO-GTPV2-MIB", "cGtpv2DeleteBearerFailInds"),
        ("CISCO-GTPV2-MIB", "cGtpv2BearerResrcFailInds"))
)
if mibBuilder.loadTexts:
    cGtpv2MIBSystemStatisticsGroup.setStatus("current")

cGtpv2MIBGtpPathStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 2, 2, 2)
)
cGtpv2MIBGtpPathStatisticsGroup.setObjects(
      *(("CISCO-GTPV2-MIB", "cGtpPathDroppedSigMsgs"),
        ("CISCO-GTPV2-MIB", "cGtpPathCreateSessReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathDeleteSessReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathCreateBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathModifyBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathUpdateBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathDeleteBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathCreateSessRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathDeleteSessRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathCreateBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathModifyBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathUpdateBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathDeleteBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathChangeNotifReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathModifyBearerCmds"),
        ("CISCO-GTPV2-MIB", "cGtpPathModifyBearerFailInds"),
        ("CISCO-GTPV2-MIB", "cGtpPathDeleteBearerCmds"),
        ("CISCO-GTPV2-MIB", "cGtpPathDeleteBearerFailInds"),
        ("CISCO-GTPV2-MIB", "cGtpPathBearerResrcCmds"),
        ("CISCO-GTPV2-MIB", "cGtpPathBearerResrcFailInds"))
)
if mibBuilder.loadTexts:
    cGtpv2MIBGtpPathStatisticsGroup.setStatus("current")

cGtpv2MIBGtpPathHistStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 2, 2, 3)
)
cGtpv2MIBGtpPathHistStatsGroup.setObjects(
      *(("CISCO-GTPV2-MIB", "cGtpPathHistDroppedSigMsgs"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistCreateSessReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistDeleteSessReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistCreateBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistModifyBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistUpdateBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistDeleteBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistCreateSessRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistDeleteSessRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistCreateBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistModifyBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistUpdateBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistDeleteBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistChangeNotifReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistModifyBearerCmds"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistModifyBearerFailInds"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistDeleteBearerCmds"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistDeleteBearerFailInds"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistBearerResrcCmds"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistBearerResrcFailInds"))
)
if mibBuilder.loadTexts:
    cGtpv2MIBGtpPathHistStatsGroup.setStatus("current")

cGtpv2MIBSystemStatisticsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 2, 2, 4)
)
cGtpv2MIBSystemStatisticsGroupSup1.setObjects(
      *(("CISCO-GTPV2-MIB", "cGtpv2SentStopPageInds"),
        ("CISCO-GTPV2-MIB", "cGtpv2Initv2tov1Handoffs"),
        ("CISCO-GTPV2-MIB", "cGtpv2Succv2tov1Handoffs"),
        ("CISCO-GTPV2-MIB", "cGtpv2Initv1tov2Handoffs"),
        ("CISCO-GTPV2-MIB", "cGtpv2Succv1tov2Handoffs"),
        ("CISCO-GTPV2-MIB", "cGtpv2TotalN3Retransmits"),
        ("CISCO-GTPV2-MIB", "cGtpv2DeletePdnConnSetReqs"),
        ("CISCO-GTPV2-MIB", "cGtpv2RelAccessBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpv2DownlinkDataNotifs"),
        ("CISCO-GTPV2-MIB", "cGtpv2CreateIndirectTunnelReqs"),
        ("CISCO-GTPV2-MIB", "cGtpv2DeleteIndirectTunnelReqs"),
        ("CISCO-GTPV2-MIB", "cGtpv2SuspendNotifs"),
        ("CISCO-GTPV2-MIB", "cGtpv2ResumeNotifs"),
        ("CISCO-GTPV2-MIB", "cGtpv2EchoReqs"),
        ("CISCO-GTPV2-MIB", "cGtpv2DeletePdnConnSetRsps"),
        ("CISCO-GTPV2-MIB", "cGtpv2RelAccessBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpv2DownlinkDataNotifAcks"),
        ("CISCO-GTPV2-MIB", "cGtpv2DownlinkDataNotifFailInds"),
        ("CISCO-GTPV2-MIB", "cGtpv2CreateIndirectTunnelRsps"),
        ("CISCO-GTPV2-MIB", "cGtpv2DeleteIndirectTunnelRsps"),
        ("CISCO-GTPV2-MIB", "cGtpv2SuspendNotifAcks"),
        ("CISCO-GTPV2-MIB", "cGtpv2ResumeNotifAck"),
        ("CISCO-GTPV2-MIB", "cGtpv2EchoRsps"))
)
if mibBuilder.loadTexts:
    cGtpv2MIBSystemStatisticsGroupSup1.setStatus("current")

cGtpv2MIBGtpPathStatisticsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 2, 2, 5)
)
cGtpv2MIBGtpPathStatisticsGroupSup1.setObjects(
      *(("CISCO-GTPV2-MIB", "cGtpPathSentStopPageInds"),
        ("CISCO-GTPV2-MIB", "cGtpPathDeletePdnConnSetReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathRelAccessBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathDownlinkDataNotifs"),
        ("CISCO-GTPV2-MIB", "cGtpPathSuspendNotifs"),
        ("CISCO-GTPV2-MIB", "cGtpPathResumeNotifs"),
        ("CISCO-GTPV2-MIB", "cGtpPathEchoReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathVerNotSupported"),
        ("CISCO-GTPV2-MIB", "cGtpPathDeletePdnConnSetRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathRelAccessBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathDownlinkDataNotifAcks"),
        ("CISCO-GTPV2-MIB", "cGtpPathDownlinkDataNotifFailInds"),
        ("CISCO-GTPV2-MIB", "cGtpPathSuspendNotifAcks"),
        ("CISCO-GTPV2-MIB", "cGtpPathResumeNotifAcks"),
        ("CISCO-GTPV2-MIB", "cGtpPathEchoRsps"))
)
if mibBuilder.loadTexts:
    cGtpv2MIBGtpPathStatisticsGroupSup1.setStatus("current")

cGtpv2MIBGtpPathHistStatsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 2, 2, 6)
)
cGtpv2MIBGtpPathHistStatsGroupSup1.setObjects(
      *(("CISCO-GTPV2-MIB", "cGtpPathHistSentStopPageInds"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistDeletePdnConnSetReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistRelAccessBearerReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistDownlinkDataNotifs"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistSuspendNotifs"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistResumeNotifs"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistEchoReqs"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistVerNotSupported"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistDeletePdnConnSetRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistRelAccessBearerRsps"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistDownlinkDataNotifAcks"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistDownlinkDataNotifFailInds"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistSuspendNotifAcks"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistResumeNotifAcks"),
        ("CISCO-GTPV2-MIB", "cGtpPathHistEchoRsps"))
)
if mibBuilder.loadTexts:
    cGtpv2MIBGtpPathHistStatsGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cGtpv2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cGtpv2MIBCompliance.setStatus(
        "deprecated"
    )

cGtpv2MIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 734, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cGtpv2MIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GTPV2-MIB",
    **{"CGtpv2Action": CGtpv2Action,
       "ciscoGtpv2MIB": ciscoGtpv2MIB,
       "cGtpv2MIBObjects": cGtpv2MIBObjects,
       "cGtpv2Statistics": cGtpv2Statistics,
       "cGtpv2SystemStatistics": cGtpv2SystemStatistics,
       "cGtpv2DroppedSigMsgs": cGtpv2DroppedSigMsgs,
       "cGtpv2ReservedValueIeMsgs": cGtpv2ReservedValueIeMsgs,
       "cGtpv2ReqMsgStatsTable": cGtpv2ReqMsgStatsTable,
       "cGtpv2ReqMsgStatsEntry": cGtpv2ReqMsgStatsEntry,
       "cGtpv2MsgReqAction": cGtpv2MsgReqAction,
       "cGtpv2CreateSessReqs": cGtpv2CreateSessReqs,
       "cGtpv2DeleteSessReqs": cGtpv2DeleteSessReqs,
       "cGtpv2CreateBearerReqs": cGtpv2CreateBearerReqs,
       "cGtpv2ModifyBearerReqs": cGtpv2ModifyBearerReqs,
       "cGtpv2UpdateBearerReqs": cGtpv2UpdateBearerReqs,
       "cGtpv2DeleteBearerReqs": cGtpv2DeleteBearerReqs,
       "cGtpv2ChangeNotifReqs": cGtpv2ChangeNotifReqs,
       "cGtpv2ModifyBearerCmds": cGtpv2ModifyBearerCmds,
       "cGtpv2DeleteBearerCmds": cGtpv2DeleteBearerCmds,
       "cGtpv2BearerResrcCmds": cGtpv2BearerResrcCmds,
       "cGtpv2DeletePdnConnSetReqs": cGtpv2DeletePdnConnSetReqs,
       "cGtpv2RelAccessBearerReqs": cGtpv2RelAccessBearerReqs,
       "cGtpv2DownlinkDataNotifs": cGtpv2DownlinkDataNotifs,
       "cGtpv2CreateIndirectTunnelReqs": cGtpv2CreateIndirectTunnelReqs,
       "cGtpv2DeleteIndirectTunnelReqs": cGtpv2DeleteIndirectTunnelReqs,
       "cGtpv2SuspendNotifs": cGtpv2SuspendNotifs,
       "cGtpv2ResumeNotifs": cGtpv2ResumeNotifs,
       "cGtpv2EchoReqs": cGtpv2EchoReqs,
       "cGtpv2RspMsgStatsTable": cGtpv2RspMsgStatsTable,
       "cGtpv2RspMsgStatsEntry": cGtpv2RspMsgStatsEntry,
       "cGtpv2MsgRspAction": cGtpv2MsgRspAction,
       "cGtpv2CreateSessRsps": cGtpv2CreateSessRsps,
       "cGtpv2DeleteSessRsps": cGtpv2DeleteSessRsps,
       "cGtpv2CreateBearerRsps": cGtpv2CreateBearerRsps,
       "cGtpv2ModifyBearerRsps": cGtpv2ModifyBearerRsps,
       "cGtpv2UpdateBearerRsps": cGtpv2UpdateBearerRsps,
       "cGtpv2DeleteBearerRsps": cGtpv2DeleteBearerRsps,
       "cGtpv2ModifyBearerFailInds": cGtpv2ModifyBearerFailInds,
       "cGtpv2DeleteBearerFailInds": cGtpv2DeleteBearerFailInds,
       "cGtpv2BearerResrcFailInds": cGtpv2BearerResrcFailInds,
       "cGtpv2DeletePdnConnSetRsps": cGtpv2DeletePdnConnSetRsps,
       "cGtpv2RelAccessBearerRsps": cGtpv2RelAccessBearerRsps,
       "cGtpv2DownlinkDataNotifAcks": cGtpv2DownlinkDataNotifAcks,
       "cGtpv2DownlinkDataNotifFailInds": cGtpv2DownlinkDataNotifFailInds,
       "cGtpv2CreateIndirectTunnelRsps": cGtpv2CreateIndirectTunnelRsps,
       "cGtpv2DeleteIndirectTunnelRsps": cGtpv2DeleteIndirectTunnelRsps,
       "cGtpv2SuspendNotifAcks": cGtpv2SuspendNotifAcks,
       "cGtpv2ResumeNotifAck": cGtpv2ResumeNotifAck,
       "cGtpv2EchoRsps": cGtpv2EchoRsps,
       "cGtpv2SentStopPageInds": cGtpv2SentStopPageInds,
       "cGtpv2Initv2tov1Handoffs": cGtpv2Initv2tov1Handoffs,
       "cGtpv2Succv2tov1Handoffs": cGtpv2Succv2tov1Handoffs,
       "cGtpv2Initv1tov2Handoffs": cGtpv2Initv1tov2Handoffs,
       "cGtpv2Succv1tov2Handoffs": cGtpv2Succv1tov2Handoffs,
       "cGtpv2TotalN3Retransmits": cGtpv2TotalN3Retransmits,
       "cGtpPathGtpv2Statistics": cGtpPathGtpv2Statistics,
       "cGtpPathGtpv2StatisticsTable": cGtpPathGtpv2StatisticsTable,
       "cGtpPathGtpv2StatisticsEntry": cGtpPathGtpv2StatisticsEntry,
       "cGtpPathDroppedSigMsgs": cGtpPathDroppedSigMsgs,
       "cGtpPathSentStopPageInds": cGtpPathSentStopPageInds,
       "cGtpPathGtpv2ReqMsgTable": cGtpPathGtpv2ReqMsgTable,
       "cGtpPathGtpv2ReqMsgEntry": cGtpPathGtpv2ReqMsgEntry,
       "cGtpPathMsgReqAction": cGtpPathMsgReqAction,
       "cGtpPathCreateSessReqs": cGtpPathCreateSessReqs,
       "cGtpPathDeleteSessReqs": cGtpPathDeleteSessReqs,
       "cGtpPathCreateBearerReqs": cGtpPathCreateBearerReqs,
       "cGtpPathModifyBearerReqs": cGtpPathModifyBearerReqs,
       "cGtpPathUpdateBearerReqs": cGtpPathUpdateBearerReqs,
       "cGtpPathDeleteBearerReqs": cGtpPathDeleteBearerReqs,
       "cGtpPathChangeNotifReqs": cGtpPathChangeNotifReqs,
       "cGtpPathModifyBearerCmds": cGtpPathModifyBearerCmds,
       "cGtpPathDeleteBearerCmds": cGtpPathDeleteBearerCmds,
       "cGtpPathBearerResrcCmds": cGtpPathBearerResrcCmds,
       "cGtpPathDeletePdnConnSetReqs": cGtpPathDeletePdnConnSetReqs,
       "cGtpPathRelAccessBearerReqs": cGtpPathRelAccessBearerReqs,
       "cGtpPathDownlinkDataNotifs": cGtpPathDownlinkDataNotifs,
       "cGtpPathSuspendNotifs": cGtpPathSuspendNotifs,
       "cGtpPathResumeNotifs": cGtpPathResumeNotifs,
       "cGtpPathEchoReqs": cGtpPathEchoReqs,
       "cGtpPathVerNotSupported": cGtpPathVerNotSupported,
       "cGtpPathGtpv2RspMsgTable": cGtpPathGtpv2RspMsgTable,
       "cGtpPathGtpv2RspMsgEntry": cGtpPathGtpv2RspMsgEntry,
       "cGtpPathMsgRspAction": cGtpPathMsgRspAction,
       "cGtpPathCreateSessRsps": cGtpPathCreateSessRsps,
       "cGtpPathDeleteSessRsps": cGtpPathDeleteSessRsps,
       "cGtpPathCreateBearerRsps": cGtpPathCreateBearerRsps,
       "cGtpPathModifyBearerRsps": cGtpPathModifyBearerRsps,
       "cGtpPathUpdateBearerRsps": cGtpPathUpdateBearerRsps,
       "cGtpPathDeleteBearerRsps": cGtpPathDeleteBearerRsps,
       "cGtpPathModifyBearerFailInds": cGtpPathModifyBearerFailInds,
       "cGtpPathDeleteBearerFailInds": cGtpPathDeleteBearerFailInds,
       "cGtpPathBearerResrcFailInds": cGtpPathBearerResrcFailInds,
       "cGtpPathDeletePdnConnSetRsps": cGtpPathDeletePdnConnSetRsps,
       "cGtpPathRelAccessBearerRsps": cGtpPathRelAccessBearerRsps,
       "cGtpPathDownlinkDataNotifAcks": cGtpPathDownlinkDataNotifAcks,
       "cGtpPathDownlinkDataNotifFailInds": cGtpPathDownlinkDataNotifFailInds,
       "cGtpPathSuspendNotifAcks": cGtpPathSuspendNotifAcks,
       "cGtpPathResumeNotifAcks": cGtpPathResumeNotifAcks,
       "cGtpPathEchoRsps": cGtpPathEchoRsps,
       "cGtpPathHistGtpv2Statistics": cGtpPathHistGtpv2Statistics,
       "cGtpPathHistGtpv2StatisticsTable": cGtpPathHistGtpv2StatisticsTable,
       "cGtpPathHistGtpv2StatisticsEntry": cGtpPathHistGtpv2StatisticsEntry,
       "cGtpPathHistDroppedSigMsgs": cGtpPathHistDroppedSigMsgs,
       "cGtpPathHistSentStopPageInds": cGtpPathHistSentStopPageInds,
       "cGtpPathHistGtpv2ReqMsgTable": cGtpPathHistGtpv2ReqMsgTable,
       "cGtpPathHistGtpv2ReqMsgEntry": cGtpPathHistGtpv2ReqMsgEntry,
       "cGtpPathHistMsgReqAction": cGtpPathHistMsgReqAction,
       "cGtpPathHistCreateSessReqs": cGtpPathHistCreateSessReqs,
       "cGtpPathHistDeleteSessReqs": cGtpPathHistDeleteSessReqs,
       "cGtpPathHistCreateBearerReqs": cGtpPathHistCreateBearerReqs,
       "cGtpPathHistModifyBearerReqs": cGtpPathHistModifyBearerReqs,
       "cGtpPathHistUpdateBearerReqs": cGtpPathHistUpdateBearerReqs,
       "cGtpPathHistDeleteBearerReqs": cGtpPathHistDeleteBearerReqs,
       "cGtpPathHistChangeNotifReqs": cGtpPathHistChangeNotifReqs,
       "cGtpPathHistModifyBearerCmds": cGtpPathHistModifyBearerCmds,
       "cGtpPathHistDeleteBearerCmds": cGtpPathHistDeleteBearerCmds,
       "cGtpPathHistBearerResrcCmds": cGtpPathHistBearerResrcCmds,
       "cGtpPathHistDeletePdnConnSetReqs": cGtpPathHistDeletePdnConnSetReqs,
       "cGtpPathHistRelAccessBearerReqs": cGtpPathHistRelAccessBearerReqs,
       "cGtpPathHistDownlinkDataNotifs": cGtpPathHistDownlinkDataNotifs,
       "cGtpPathHistSuspendNotifs": cGtpPathHistSuspendNotifs,
       "cGtpPathHistResumeNotifs": cGtpPathHistResumeNotifs,
       "cGtpPathHistEchoReqs": cGtpPathHistEchoReqs,
       "cGtpPathHistVerNotSupported": cGtpPathHistVerNotSupported,
       "cGtpPathHistGtpv2RspMsgTable": cGtpPathHistGtpv2RspMsgTable,
       "cGtpPathHistGtpv2RspMsgEntry": cGtpPathHistGtpv2RspMsgEntry,
       "cGtpPathHistMsgRspAction": cGtpPathHistMsgRspAction,
       "cGtpPathHistCreateSessRsps": cGtpPathHistCreateSessRsps,
       "cGtpPathHistDeleteSessRsps": cGtpPathHistDeleteSessRsps,
       "cGtpPathHistCreateBearerRsps": cGtpPathHistCreateBearerRsps,
       "cGtpPathHistModifyBearerRsps": cGtpPathHistModifyBearerRsps,
       "cGtpPathHistUpdateBearerRsps": cGtpPathHistUpdateBearerRsps,
       "cGtpPathHistDeleteBearerRsps": cGtpPathHistDeleteBearerRsps,
       "cGtpPathHistModifyBearerFailInds": cGtpPathHistModifyBearerFailInds,
       "cGtpPathHistDeleteBearerFailInds": cGtpPathHistDeleteBearerFailInds,
       "cGtpPathHistBearerResrcFailInds": cGtpPathHistBearerResrcFailInds,
       "cGtpPathHistDeletePdnConnSetRsps": cGtpPathHistDeletePdnConnSetRsps,
       "cGtpPathHistRelAccessBearerRsps": cGtpPathHistRelAccessBearerRsps,
       "cGtpPathHistDownlinkDataNotifAcks": cGtpPathHistDownlinkDataNotifAcks,
       "cGtpPathHistDownlinkDataNotifFailInds": cGtpPathHistDownlinkDataNotifFailInds,
       "cGtpPathHistSuspendNotifAcks": cGtpPathHistSuspendNotifAcks,
       "cGtpPathHistResumeNotifAcks": cGtpPathHistResumeNotifAcks,
       "cGtpPathHistEchoRsps": cGtpPathHistEchoRsps,
       "cGtpv2MIBConformances": cGtpv2MIBConformances,
       "cGtpv2MIBCompliances": cGtpv2MIBCompliances,
       "cGtpv2MIBCompliance": cGtpv2MIBCompliance,
       "cGtpv2MIBComplianceRev1": cGtpv2MIBComplianceRev1,
       "cGtpv2MIBGroups": cGtpv2MIBGroups,
       "cGtpv2MIBSystemStatisticsGroup": cGtpv2MIBSystemStatisticsGroup,
       "cGtpv2MIBGtpPathStatisticsGroup": cGtpv2MIBGtpPathStatisticsGroup,
       "cGtpv2MIBGtpPathHistStatsGroup": cGtpv2MIBGtpPathHistStatsGroup,
       "cGtpv2MIBSystemStatisticsGroupSup1": cGtpv2MIBSystemStatisticsGroupSup1,
       "cGtpv2MIBGtpPathStatisticsGroupSup1": cGtpv2MIBGtpPathStatisticsGroupSup1,
       "cGtpv2MIBGtpPathHistStatsGroupSup1": cGtpv2MIBGtpPathHistStatsGroupSup1}
)
