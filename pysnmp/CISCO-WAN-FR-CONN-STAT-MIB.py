# SNMP MIB module (CISCO-WAN-FR-CONN-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-FR-CONN-STAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:03 2024
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

(frChan,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "frChan")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoWanFrConnStatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 48)
)
ciscoWanFrConnStatMIB.setRevisions(
        ("2002-10-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrChanCntGrp_ObjectIdentity = ObjectIdentity
frChanCntGrp = _FrChanCntGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3)
)
_FrChanCntGrpTable_Object = MibTable
frChanCntGrpTable = _FrChanCntGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    frChanCntGrpTable.setStatus("current")
_FrChanCntGrpEntry_Object = MibTableRow
frChanCntGrpEntry = _FrChanCntGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1)
)
frChanCntGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-CONN-STAT-MIB", "cntChanNum"),
)
if mibBuilder.loadTexts:
    frChanCntGrpEntry.setStatus("current")


class _CntChanNum_Type(Integer32):
    """Custom type cntChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CntChanNum_Type.__name__ = "Integer32"
_CntChanNum_Object = MibTableColumn
cntChanNum = _CntChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 1),
    _CntChanNum_Type()
)
cntChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntChanNum.setStatus("current")
_RcvFrames_Type = Counter32
_RcvFrames_Object = MibTableColumn
rcvFrames = _RcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 2),
    _RcvFrames_Type()
)
rcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFrames.setStatus("current")
if mibBuilder.loadTexts:
    rcvFrames.setUnits("Frames")
_RcvBytes_Type = Counter32
_RcvBytes_Object = MibTableColumn
rcvBytes = _RcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 3),
    _RcvBytes_Type()
)
rcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvBytes.setStatus("current")
if mibBuilder.loadTexts:
    rcvBytes.setUnits("Bytes")
_RcvFramesDE_Type = Counter32
_RcvFramesDE_Object = MibTableColumn
rcvFramesDE = _RcvFramesDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 4),
    _RcvFramesDE_Type()
)
rcvFramesDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesDE.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesDE.setUnits("Frames")
_RcvBytesDE_Type = Counter32
_RcvBytesDE_Object = MibTableColumn
rcvBytesDE = _RcvBytesDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 5),
    _RcvBytesDE_Type()
)
rcvBytesDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvBytesDE.setStatus("current")
if mibBuilder.loadTexts:
    rcvBytesDE.setUnits("Bytes")
_RcvFramesDiscard_Type = Counter32
_RcvFramesDiscard_Object = MibTableColumn
rcvFramesDiscard = _RcvFramesDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 6),
    _RcvFramesDiscard_Type()
)
rcvFramesDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesDiscard.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesDiscard.setUnits("Frames")
_RcvBytesDiscard_Type = Counter32
_RcvBytesDiscard_Object = MibTableColumn
rcvBytesDiscard = _RcvBytesDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 7),
    _RcvBytesDiscard_Type()
)
rcvBytesDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvBytesDiscard.setStatus("current")
if mibBuilder.loadTexts:
    rcvBytesDiscard.setUnits("Bytes")
_RcvFramesDiscShelfAlarm_Type = Counter32
_RcvFramesDiscShelfAlarm_Object = MibTableColumn
rcvFramesDiscShelfAlarm = _RcvFramesDiscShelfAlarm_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 8),
    _RcvFramesDiscShelfAlarm_Type()
)
rcvFramesDiscShelfAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesDiscShelfAlarm.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesDiscShelfAlarm.setUnits("Frames")
_RcvFramesDiscXceedQDepth_Type = Counter32
_RcvFramesDiscXceedQDepth_Object = MibTableColumn
rcvFramesDiscXceedQDepth = _RcvFramesDiscXceedQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 9),
    _RcvFramesDiscXceedQDepth_Type()
)
rcvFramesDiscXceedQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesDiscXceedQDepth.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesDiscXceedQDepth.setUnits("Frames")
_RcvBytesDiscXceedQDepth_Type = Counter32
_RcvBytesDiscXceedQDepth_Object = MibTableColumn
rcvBytesDiscXceedQDepth = _RcvBytesDiscXceedQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 10),
    _RcvBytesDiscXceedQDepth_Type()
)
rcvBytesDiscXceedQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvBytesDiscXceedQDepth.setStatus("current")
if mibBuilder.loadTexts:
    rcvBytesDiscXceedQDepth.setUnits("Bytes")
_RcvFramesDiscXceedDEThresh_Type = Counter32
_RcvFramesDiscXceedDEThresh_Object = MibTableColumn
rcvFramesDiscXceedDEThresh = _RcvFramesDiscXceedDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 11),
    _RcvFramesDiscXceedDEThresh_Type()
)
rcvFramesDiscXceedDEThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesDiscXceedDEThresh.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesDiscXceedDEThresh.setUnits("Frames")
_RcvFramesFECN_Type = Counter32
_RcvFramesFECN_Object = MibTableColumn
rcvFramesFECN = _RcvFramesFECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 12),
    _RcvFramesFECN_Type()
)
rcvFramesFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesFECN.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesFECN.setUnits("Frames")
_RcvFramesBECN_Type = Counter32
_RcvFramesBECN_Object = MibTableColumn
rcvFramesBECN = _RcvFramesBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 13),
    _RcvFramesBECN_Type()
)
rcvFramesBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesBECN.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesBECN.setUnits("Frames")
_RcvFramesTaggedFECN_Type = Counter32
_RcvFramesTaggedFECN_Object = MibTableColumn
rcvFramesTaggedFECN = _RcvFramesTaggedFECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 14),
    _RcvFramesTaggedFECN_Type()
)
rcvFramesTaggedFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesTaggedFECN.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesTaggedFECN.setUnits("Frames")
_RcvFramesTaggedBECN_Type = Counter32
_RcvFramesTaggedBECN_Object = MibTableColumn
rcvFramesTaggedBECN = _RcvFramesTaggedBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 15),
    _RcvFramesTaggedBECN_Type()
)
rcvFramesTaggedBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesTaggedBECN.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesTaggedBECN.setUnits("Frames")
_RcvFramesTaggedDE_Type = Counter32
_RcvFramesTaggedDE_Object = MibTableColumn
rcvFramesTaggedDE = _RcvFramesTaggedDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 16),
    _RcvFramesTaggedDE_Type()
)
rcvFramesTaggedDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesTaggedDE.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesTaggedDE.setUnits("Frames")
_RcvBytesTaggedDE_Type = Counter32
_RcvBytesTaggedDE_Object = MibTableColumn
rcvBytesTaggedDE = _RcvBytesTaggedDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 17),
    _RcvBytesTaggedDE_Type()
)
rcvBytesTaggedDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvBytesTaggedDE.setStatus("current")
if mibBuilder.loadTexts:
    rcvBytesTaggedDE.setUnits("Bytes")
_RcvKbpsAIR_Type = Integer32
_RcvKbpsAIR_Object = MibTableColumn
rcvKbpsAIR = _RcvKbpsAIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 18),
    _RcvKbpsAIR_Type()
)
rcvKbpsAIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvKbpsAIR.setStatus("current")
if mibBuilder.loadTexts:
    rcvKbpsAIR.setUnits("kbps")
_XmtFrames_Type = Counter32
_XmtFrames_Object = MibTableColumn
xmtFrames = _XmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 19),
    _XmtFrames_Type()
)
xmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFrames.setStatus("current")
if mibBuilder.loadTexts:
    xmtFrames.setUnits("Frames")
_XmtBytes_Type = Counter32
_XmtBytes_Object = MibTableColumn
xmtBytes = _XmtBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 20),
    _XmtBytes_Type()
)
xmtBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtBytes.setStatus("current")
if mibBuilder.loadTexts:
    xmtBytes.setUnits("Bytes")
_XmtFramesFECN_Type = Counter32
_XmtFramesFECN_Object = MibTableColumn
xmtFramesFECN = _XmtFramesFECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 21),
    _XmtFramesFECN_Type()
)
xmtFramesFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesFECN.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesFECN.setUnits("Frames")
_XmtFramesBECN_Type = Counter32
_XmtFramesBECN_Object = MibTableColumn
xmtFramesBECN = _XmtFramesBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 22),
    _XmtFramesBECN_Type()
)
xmtFramesBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesBECN.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesBECN.setUnits("Frames")
_XmtFramesDE_Type = Counter32
_XmtFramesDE_Object = MibTableColumn
xmtFramesDE = _XmtFramesDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 23),
    _XmtFramesDE_Type()
)
xmtFramesDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesDE.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesDE.setUnits("Frames")
_XmtBytesDE_Type = Counter32
_XmtBytesDE_Object = MibTableColumn
xmtBytesDE = _XmtBytesDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 24),
    _XmtBytesDE_Type()
)
xmtBytesDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtBytesDE.setStatus("current")
if mibBuilder.loadTexts:
    xmtBytesDE.setUnits("Bytes")
_XmtFramesDiscard_Type = Counter32
_XmtFramesDiscard_Object = MibTableColumn
xmtFramesDiscard = _XmtFramesDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 25),
    _XmtFramesDiscard_Type()
)
xmtFramesDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesDiscard.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesDiscard.setUnits("Frames")
_XmtBytesDiscard_Type = Counter32
_XmtBytesDiscard_Object = MibTableColumn
xmtBytesDiscard = _XmtBytesDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 26),
    _XmtBytesDiscard_Type()
)
xmtBytesDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtBytesDiscard.setStatus("current")
if mibBuilder.loadTexts:
    xmtBytesDiscard.setUnits("Bytes")
_XmtFramesDiscXceedQDepth_Type = Counter32
_XmtFramesDiscXceedQDepth_Object = MibTableColumn
xmtFramesDiscXceedQDepth = _XmtFramesDiscXceedQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 27),
    _XmtFramesDiscXceedQDepth_Type()
)
xmtFramesDiscXceedQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesDiscXceedQDepth.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesDiscXceedQDepth.setUnits("Frames")
_XmtBytesDiscXceedQDepth_Type = Counter32
_XmtBytesDiscXceedQDepth_Object = MibTableColumn
xmtBytesDiscXceedQDepth = _XmtBytesDiscXceedQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 28),
    _XmtBytesDiscXceedQDepth_Type()
)
xmtBytesDiscXceedQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtBytesDiscXceedQDepth.setStatus("current")
if mibBuilder.loadTexts:
    xmtBytesDiscXceedQDepth.setUnits("Bytes")
_XmtFramesDiscXceedDEThresh_Type = Counter32
_XmtFramesDiscXceedDEThresh_Object = MibTableColumn
xmtFramesDiscXceedDEThresh = _XmtFramesDiscXceedDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 29),
    _XmtFramesDiscXceedDEThresh_Type()
)
xmtFramesDiscXceedDEThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesDiscXceedDEThresh.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesDiscXceedDEThresh.setUnits("Frames")
_XmtFramesDiscPhyLayerFail_Type = Counter32
_XmtFramesDiscPhyLayerFail_Object = MibTableColumn
xmtFramesDiscPhyLayerFail = _XmtFramesDiscPhyLayerFail_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 30),
    _XmtFramesDiscPhyLayerFail_Type()
)
xmtFramesDiscPhyLayerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesDiscPhyLayerFail.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesDiscPhyLayerFail.setUnits("Frames")
_XmtFramesDiscCRCError_Type = Counter32
_XmtFramesDiscCRCError_Object = MibTableColumn
xmtFramesDiscCRCError = _XmtFramesDiscCRCError_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 31),
    _XmtFramesDiscCRCError_Type()
)
xmtFramesDiscCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesDiscCRCError.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesDiscCRCError.setUnits("Frames")
_XmtFramesDiscReassmFail_Type = Counter32
_XmtFramesDiscReassmFail_Object = MibTableColumn
xmtFramesDiscReassmFail = _XmtFramesDiscReassmFail_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 32),
    _XmtFramesDiscReassmFail_Type()
)
xmtFramesDiscReassmFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesDiscReassmFail.setStatus("current")
_XmtFramesDiscSrcAbort_Type = Counter32
_XmtFramesDiscSrcAbort_Object = MibTableColumn
xmtFramesDiscSrcAbort = _XmtFramesDiscSrcAbort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 33),
    _XmtFramesDiscSrcAbort_Type()
)
xmtFramesDiscSrcAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesDiscSrcAbort.setStatus("current")
_XmtFramesDuringLMIAlarm_Type = Counter32
_XmtFramesDuringLMIAlarm_Object = MibTableColumn
xmtFramesDuringLMIAlarm = _XmtFramesDuringLMIAlarm_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 34),
    _XmtFramesDuringLMIAlarm_Type()
)
xmtFramesDuringLMIAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesDuringLMIAlarm.setStatus("current")
_XmtBytesDuringLMIAlarm_Type = Counter32
_XmtBytesDuringLMIAlarm_Object = MibTableColumn
xmtBytesDuringLMIAlarm = _XmtBytesDuringLMIAlarm_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 35),
    _XmtBytesDuringLMIAlarm_Type()
)
xmtBytesDuringLMIAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtBytesDuringLMIAlarm.setStatus("current")
_XmtFramesTaggedFECN_Type = Counter32
_XmtFramesTaggedFECN_Object = MibTableColumn
xmtFramesTaggedFECN = _XmtFramesTaggedFECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 36),
    _XmtFramesTaggedFECN_Type()
)
xmtFramesTaggedFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesTaggedFECN.setStatus("current")
_XmtFramesTaggedBECN_Type = Counter32
_XmtFramesTaggedBECN_Object = MibTableColumn
xmtFramesTaggedBECN = _XmtFramesTaggedBECN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 37),
    _XmtFramesTaggedBECN_Type()
)
xmtFramesTaggedBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesTaggedBECN.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesTaggedBECN.setUnits("Frames")
_XmtKbpsAIR_Type = Integer32
_XmtKbpsAIR_Object = MibTableColumn
xmtKbpsAIR = _XmtKbpsAIR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 38),
    _XmtKbpsAIR_Type()
)
xmtKbpsAIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtKbpsAIR.setStatus("current")
if mibBuilder.loadTexts:
    xmtKbpsAIR.setUnits("kbps")


class _ChanClrButton_Type(Integer32):
    """Custom type chanClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_ChanClrButton_Type.__name__ = "Integer32"
_ChanClrButton_Object = MibTableColumn
chanClrButton = _ChanClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 39),
    _ChanClrButton_Type()
)
chanClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanClrButton.setStatus("current")
_XmtFramesTaggedDE_Type = Counter32
_XmtFramesTaggedDE_Object = MibTableColumn
xmtFramesTaggedDE = _XmtFramesTaggedDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 40),
    _XmtFramesTaggedDE_Type()
)
xmtFramesTaggedDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesTaggedDE.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesTaggedDE.setUnits("Frames")
_XmtBytesTaggedDE_Type = Counter32
_XmtBytesTaggedDE_Object = MibTableColumn
xmtBytesTaggedDE = _XmtBytesTaggedDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 41),
    _XmtBytesTaggedDE_Type()
)
xmtBytesTaggedDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtBytesTaggedDE.setStatus("current")
if mibBuilder.loadTexts:
    xmtBytesTaggedDE.setUnits("Bytes")
_RcvFramesDiscUPC_Type = Counter32
_RcvFramesDiscUPC_Object = MibTableColumn
rcvFramesDiscUPC = _RcvFramesDiscUPC_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 42),
    _RcvFramesDiscUPC_Type()
)
rcvFramesDiscUPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesDiscUPC.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesDiscUPC.setUnits("Frames")
_ChanSecUpTime_Type = Counter32
_ChanSecUpTime_Object = MibTableColumn
chanSecUpTime = _ChanSecUpTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 43),
    _ChanSecUpTime_Type()
)
chanSecUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanSecUpTime.setStatus("current")
if mibBuilder.loadTexts:
    chanSecUpTime.setUnits("seconds")
_XmtFramesInvalidCPIs_Type = Counter32
_XmtFramesInvalidCPIs_Object = MibTableColumn
xmtFramesInvalidCPIs = _XmtFramesInvalidCPIs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 44),
    _XmtFramesInvalidCPIs_Type()
)
xmtFramesInvalidCPIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesInvalidCPIs.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesInvalidCPIs.setUnits("Frames")
_XmtFramesLengthViolations_Type = Counter32
_XmtFramesLengthViolations_Object = MibTableColumn
xmtFramesLengthViolations = _XmtFramesLengthViolations_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 45),
    _XmtFramesLengthViolations_Type()
)
xmtFramesLengthViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesLengthViolations.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesLengthViolations.setUnits("Frames")
_XmtFramesOversizedSDUs_Type = Counter32
_XmtFramesOversizedSDUs_Object = MibTableColumn
xmtFramesOversizedSDUs = _XmtFramesOversizedSDUs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 46),
    _XmtFramesOversizedSDUs_Type()
)
xmtFramesOversizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesOversizedSDUs.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesOversizedSDUs.setUnits("Frames")
_XmtFramesUnknownProtocols_Type = Counter32
_XmtFramesUnknownProtocols_Object = MibTableColumn
xmtFramesUnknownProtocols = _XmtFramesUnknownProtocols_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 47),
    _XmtFramesUnknownProtocols_Type()
)
xmtFramesUnknownProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesUnknownProtocols.setStatus("current")
_RcvFramesUnknownProtocols_Type = Counter32
_RcvFramesUnknownProtocols_Object = MibTableColumn
rcvFramesUnknownProtocols = _RcvFramesUnknownProtocols_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 48),
    _RcvFramesUnknownProtocols_Type()
)
rcvFramesUnknownProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesUnknownProtocols.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesUnknownProtocols.setUnits("Frames")
_XmtBytesDEDiscard_Type = Counter32
_XmtBytesDEDiscard_Object = MibTableColumn
xmtBytesDEDiscard = _XmtBytesDEDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 49),
    _XmtBytesDEDiscard_Type()
)
xmtBytesDEDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtBytesDEDiscard.setStatus("current")
if mibBuilder.loadTexts:
    xmtBytesDEDiscard.setUnits("Bytes")
_RcvBytesDEDiscard_Type = Counter32
_RcvBytesDEDiscard_Object = MibTableColumn
rcvBytesDEDiscard = _RcvBytesDEDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 1, 1, 50),
    _RcvBytesDEDiscard_Type()
)
rcvBytesDEDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvBytesDEDiscard.setStatus("current")
if mibBuilder.loadTexts:
    rcvBytesDEDiscard.setUnits("Bytes")
_FrstdABRCntGrpTable_Object = MibTable
frstdABRCntGrpTable = _FrstdABRCntGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    frstdABRCntGrpTable.setStatus("current")
_FrstdABRCntGrpEntry_Object = MibTableRow
frstdABRCntGrpEntry = _FrstdABRCntGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1)
)
frstdABRCntGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-CONN-STAT-MIB", "frstdABRcntChanNum"),
)
if mibBuilder.loadTexts:
    frstdABRCntGrpEntry.setStatus("current")


class _FrstdABRcntChanNum_Type(Integer32):
    """Custom type frstdABRcntChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrstdABRcntChanNum_Type.__name__ = "Integer32"
_FrstdABRcntChanNum_Object = MibTableColumn
frstdABRcntChanNum = _FrstdABRcntChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1, 1),
    _FrstdABRcntChanNum_Type()
)
frstdABRcntChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frstdABRcntChanNum.setStatus("current")
_FrChanFrmXmtToNetworkCnt_Type = Counter32
_FrChanFrmXmtToNetworkCnt_Object = MibTableColumn
frChanFrmXmtToNetworkCnt = _FrChanFrmXmtToNetworkCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1, 2),
    _FrChanFrmXmtToNetworkCnt_Type()
)
frChanFrmXmtToNetworkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frChanFrmXmtToNetworkCnt.setStatus("current")
_FrChanBrmXmtToNetworkCnt_Type = Counter32
_FrChanBrmXmtToNetworkCnt_Object = MibTableColumn
frChanBrmXmtToNetworkCnt = _FrChanBrmXmtToNetworkCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1, 3),
    _FrChanBrmXmtToNetworkCnt_Type()
)
frChanBrmXmtToNetworkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frChanBrmXmtToNetworkCnt.setStatus("current")
_FrChanCrcErrRmRcvFromNetworkCnt_Type = Counter32
_FrChanCrcErrRmRcvFromNetworkCnt_Object = MibTableColumn
frChanCrcErrRmRcvFromNetworkCnt = _FrChanCrcErrRmRcvFromNetworkCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1, 4),
    _FrChanCrcErrRmRcvFromNetworkCnt_Type()
)
frChanCrcErrRmRcvFromNetworkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frChanCrcErrRmRcvFromNetworkCnt.setStatus("current")
_FrChanFrmRcvFromNetworkCnt_Type = Counter32
_FrChanFrmRcvFromNetworkCnt_Object = MibTableColumn
frChanFrmRcvFromNetworkCnt = _FrChanFrmRcvFromNetworkCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1, 5),
    _FrChanFrmRcvFromNetworkCnt_Type()
)
frChanFrmRcvFromNetworkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frChanFrmRcvFromNetworkCnt.setStatus("current")
_FrChanBrmRcvFromNetworkCnt_Type = Counter32
_FrChanBrmRcvFromNetworkCnt_Object = MibTableColumn
frChanBrmRcvFromNetworkCnt = _FrChanBrmRcvFromNetworkCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1, 6),
    _FrChanBrmRcvFromNetworkCnt_Type()
)
frChanBrmRcvFromNetworkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frChanBrmRcvFromNetworkCnt.setStatus("current")
_FrChanFrmNotTurnedAroundCnt_Type = Counter32
_FrChanFrmNotTurnedAroundCnt_Object = MibTableColumn
frChanFrmNotTurnedAroundCnt = _FrChanFrmNotTurnedAroundCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 3, 2, 1, 7),
    _FrChanFrmNotTurnedAroundCnt_Type()
)
frChanFrmNotTurnedAroundCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frChanFrmNotTurnedAroundCnt.setStatus("current")
_CwfConnStatMIBConformance_ObjectIdentity = ObjectIdentity
cwfConnStatMIBConformance = _CwfConnStatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 48, 2)
)
_CwfConnStatMIBGroups_ObjectIdentity = ObjectIdentity
cwfConnStatMIBGroups = _CwfConnStatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 48, 2, 1)
)
_CwfConnStatMIBCompliances_ObjectIdentity = ObjectIdentity
cwfConnStatMIBCompliances = _CwfConnStatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 48, 2, 2)
)

# Managed Objects groups

ciscoWanFrConnStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 48, 2, 1, 1)
)
ciscoWanFrConnStatsGroup.setObjects(
      *(("CISCO-WAN-FR-CONN-STAT-MIB", "cntChanNum"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFrames"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvBytes"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesDE"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvBytesDE"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesDiscard"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvBytesDiscard"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesDiscShelfAlarm"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesFECN"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesBECN"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesTaggedFECN"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesTaggedBECN"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesTaggedDE"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvBytesTaggedDE"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvKbpsAIR"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFrames"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtBytes"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesFECN"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesBECN"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDE"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtBytesDE"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDiscard"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtBytesDiscard"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDiscPhyLayerFail"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDiscCRCError"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDiscReassmFail"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDiscSrcAbort"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDuringLMIAlarm"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtBytesDuringLMIAlarm"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesTaggedFECN"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesTaggedBECN"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtKbpsAIR"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "chanClrButton"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "chanSecUpTime"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesDiscUPC"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtBytesTaggedDE"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesTaggedDE"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesInvalidCPIs"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesLengthViolations"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesOversizedSDUs"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesUnknownProtocols"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesUnknownProtocols"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtBytesDEDiscard"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvBytesDEDiscard"))
)
if mibBuilder.loadTexts:
    ciscoWanFrConnStatsGroup.setStatus("current")

ciscoWanFrConnQueueStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 48, 2, 1, 2)
)
ciscoWanFrConnQueueStatsGroup.setObjects(
      *(("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesDiscXceedQDepth"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvBytesDiscXceedQDepth"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "rcvFramesDiscXceedDEThresh"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDiscXceedQDepth"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtBytesDiscXceedQDepth"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "xmtFramesDiscXceedDEThresh"))
)
if mibBuilder.loadTexts:
    ciscoWanFrConnQueueStatsGroup.setStatus("current")

ciscoWanFrConnABRStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 48, 2, 1, 3)
)
ciscoWanFrConnABRStatsGroup.setObjects(
      *(("CISCO-WAN-FR-CONN-STAT-MIB", "frstdABRcntChanNum"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "frChanFrmXmtToNetworkCnt"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "frChanBrmXmtToNetworkCnt"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "frChanCrcErrRmRcvFromNetworkCnt"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "frChanFrmRcvFromNetworkCnt"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "frChanBrmRcvFromNetworkCnt"),
        ("CISCO-WAN-FR-CONN-STAT-MIB", "frChanFrmNotTurnedAroundCnt"))
)
if mibBuilder.loadTexts:
    ciscoWanFrConnABRStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanFrConnStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 48, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoWanFrConnStatCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-FR-CONN-STAT-MIB",
    **{"frChanCntGrp": frChanCntGrp,
       "frChanCntGrpTable": frChanCntGrpTable,
       "frChanCntGrpEntry": frChanCntGrpEntry,
       "cntChanNum": cntChanNum,
       "rcvFrames": rcvFrames,
       "rcvBytes": rcvBytes,
       "rcvFramesDE": rcvFramesDE,
       "rcvBytesDE": rcvBytesDE,
       "rcvFramesDiscard": rcvFramesDiscard,
       "rcvBytesDiscard": rcvBytesDiscard,
       "rcvFramesDiscShelfAlarm": rcvFramesDiscShelfAlarm,
       "rcvFramesDiscXceedQDepth": rcvFramesDiscXceedQDepth,
       "rcvBytesDiscXceedQDepth": rcvBytesDiscXceedQDepth,
       "rcvFramesDiscXceedDEThresh": rcvFramesDiscXceedDEThresh,
       "rcvFramesFECN": rcvFramesFECN,
       "rcvFramesBECN": rcvFramesBECN,
       "rcvFramesTaggedFECN": rcvFramesTaggedFECN,
       "rcvFramesTaggedBECN": rcvFramesTaggedBECN,
       "rcvFramesTaggedDE": rcvFramesTaggedDE,
       "rcvBytesTaggedDE": rcvBytesTaggedDE,
       "rcvKbpsAIR": rcvKbpsAIR,
       "xmtFrames": xmtFrames,
       "xmtBytes": xmtBytes,
       "xmtFramesFECN": xmtFramesFECN,
       "xmtFramesBECN": xmtFramesBECN,
       "xmtFramesDE": xmtFramesDE,
       "xmtBytesDE": xmtBytesDE,
       "xmtFramesDiscard": xmtFramesDiscard,
       "xmtBytesDiscard": xmtBytesDiscard,
       "xmtFramesDiscXceedQDepth": xmtFramesDiscXceedQDepth,
       "xmtBytesDiscXceedQDepth": xmtBytesDiscXceedQDepth,
       "xmtFramesDiscXceedDEThresh": xmtFramesDiscXceedDEThresh,
       "xmtFramesDiscPhyLayerFail": xmtFramesDiscPhyLayerFail,
       "xmtFramesDiscCRCError": xmtFramesDiscCRCError,
       "xmtFramesDiscReassmFail": xmtFramesDiscReassmFail,
       "xmtFramesDiscSrcAbort": xmtFramesDiscSrcAbort,
       "xmtFramesDuringLMIAlarm": xmtFramesDuringLMIAlarm,
       "xmtBytesDuringLMIAlarm": xmtBytesDuringLMIAlarm,
       "xmtFramesTaggedFECN": xmtFramesTaggedFECN,
       "xmtFramesTaggedBECN": xmtFramesTaggedBECN,
       "xmtKbpsAIR": xmtKbpsAIR,
       "chanClrButton": chanClrButton,
       "xmtFramesTaggedDE": xmtFramesTaggedDE,
       "xmtBytesTaggedDE": xmtBytesTaggedDE,
       "rcvFramesDiscUPC": rcvFramesDiscUPC,
       "chanSecUpTime": chanSecUpTime,
       "xmtFramesInvalidCPIs": xmtFramesInvalidCPIs,
       "xmtFramesLengthViolations": xmtFramesLengthViolations,
       "xmtFramesOversizedSDUs": xmtFramesOversizedSDUs,
       "xmtFramesUnknownProtocols": xmtFramesUnknownProtocols,
       "rcvFramesUnknownProtocols": rcvFramesUnknownProtocols,
       "xmtBytesDEDiscard": xmtBytesDEDiscard,
       "rcvBytesDEDiscard": rcvBytesDEDiscard,
       "frstdABRCntGrpTable": frstdABRCntGrpTable,
       "frstdABRCntGrpEntry": frstdABRCntGrpEntry,
       "frstdABRcntChanNum": frstdABRcntChanNum,
       "frChanFrmXmtToNetworkCnt": frChanFrmXmtToNetworkCnt,
       "frChanBrmXmtToNetworkCnt": frChanBrmXmtToNetworkCnt,
       "frChanCrcErrRmRcvFromNetworkCnt": frChanCrcErrRmRcvFromNetworkCnt,
       "frChanFrmRcvFromNetworkCnt": frChanFrmRcvFromNetworkCnt,
       "frChanBrmRcvFromNetworkCnt": frChanBrmRcvFromNetworkCnt,
       "frChanFrmNotTurnedAroundCnt": frChanFrmNotTurnedAroundCnt,
       "ciscoWanFrConnStatMIB": ciscoWanFrConnStatMIB,
       "cwfConnStatMIBConformance": cwfConnStatMIBConformance,
       "cwfConnStatMIBGroups": cwfConnStatMIBGroups,
       "ciscoWanFrConnStatsGroup": ciscoWanFrConnStatsGroup,
       "ciscoWanFrConnQueueStatsGroup": ciscoWanFrConnQueueStatsGroup,
       "ciscoWanFrConnABRStatsGroup": ciscoWanFrConnABRStatsGroup,
       "cwfConnStatMIBCompliances": cwfConnStatMIBCompliances,
       "ciscoWanFrConnStatCompliance": ciscoWanFrConnStatCompliance}
)
