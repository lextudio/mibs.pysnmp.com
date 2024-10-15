# SNMP MIB module (FIBRONICS-PROPRIETARY-FX8210-B-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FIBRONICS-PROPRIETARY-FX8210-B-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:53 2024
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

_Spartacus_ObjectIdentity = ObjectIdentity
spartacus = _Spartacus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22)
)
_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 2)
)
_Decrun_ObjectIdentity = ObjectIdentity
decrun = _Decrun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 2, 1)
)
_Rcircs_ObjectIdentity = ObjectIdentity
rcircs = _Rcircs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1)
)
_RCircNum_Type = Integer32
_RCircNum_Object = MibScalar
rCircNum = _RCircNum_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 1),
    _RCircNum_Type()
)
rCircNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rCircNum.setStatus("mandatory")
_RccTable_Object = MibTable
rccTable = _RccTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rccTable.setStatus("mandatory")
_RccEntry_Object = MibTableRow
rccEntry = _RccEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 2, 1)
)
rccEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rccIndex"),
)
if mibBuilder.loadTexts:
    rccEntry.setStatus("mandatory")
_RccIndex_Type = Integer32
_RccIndex_Object = MibTableColumn
rccIndex = _RccIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 2, 1, 1),
    _RccIndex_Type()
)
rccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rccIndex.setStatus("mandatory")
_RccState_Type = Integer32
_RccState_Object = MibTableColumn
rccState = _RccState_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 2, 1, 2),
    _RccState_Type()
)
rccState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rccState.setStatus("mandatory")
_RccType_Type = Integer32
_RccType_Object = MibTableColumn
rccType = _RccType_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 2, 1, 3),
    _RccType_Type()
)
rccType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rccType.setStatus("mandatory")
_RccCost_Type = Integer32
_RccCost_Object = MibTableColumn
rccCost = _RccCost_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 2, 1, 4),
    _RccCost_Type()
)
rccCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rccCost.setStatus("mandatory")
_RccBSize_Type = Integer32
_RccBSize_Object = MibTableColumn
rccBSize = _RccBSize_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 2, 1, 5),
    _RccBSize_Type()
)
rccBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rccBSize.setStatus("mandatory")
_RccHTimer_Type = Integer32
_RccHTimer_Object = MibTableColumn
rccHTimer = _RccHTimer_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 2, 1, 6),
    _RccHTimer_Type()
)
rccHTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rccHTimer.setStatus("mandatory")
_RccLine_Type = Integer32
_RccLine_Object = MibTableColumn
rccLine = _RccLine_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 2, 1, 7),
    _RccLine_Type()
)
rccLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rccLine.setStatus("mandatory")
_RbcTable_Object = MibTable
rbcTable = _RbcTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rbcTable.setStatus("mandatory")
_RbcEntry_Object = MibTableRow
rbcEntry = _RbcEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 3, 1)
)
rbcEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    rbcEntry.setStatus("mandatory")
_RbcDrout_Type = OctetString
_RbcDrout_Object = MibTableColumn
rbcDrout = _RbcDrout_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 3, 1, 1),
    _RbcDrout_Type()
)
rbcDrout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbcDrout.setStatus("mandatory")
_RbcMrout_Type = Integer32
_RbcMrout_Object = MibTableColumn
rbcMrout = _RbcMrout_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 3, 1, 2),
    _RbcMrout_Type()
)
rbcMrout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbcMrout.setStatus("mandatory")
_RbcRpri_Type = Integer32
_RbcRpri_Object = MibTableColumn
rbcRpri = _RbcRpri_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 3, 1, 3),
    _RbcRpri_Type()
)
rbcRpri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbcRpri.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 3, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_RCCntrs_Object = MibTable
rCCntrs = _RCCntrs_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rCCntrs.setStatus("mandatory")
_RCCntrEntry_Object = MibTableRow
rCCntrEntry = _RCCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 4, 1)
)
rCCntrEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    rCCntrEntry.setStatus("mandatory")
_RCCntTePktsIn_Type = Counter32
_RCCntTePktsIn_Object = MibTableColumn
rCCntTePktsIn = _RCCntTePktsIn_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 4, 1, 1),
    _RCCntTePktsIn_Type()
)
rCCntTePktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rCCntTePktsIn.setStatus("mandatory")
_RCCntOPktsOut_Type = Counter32
_RCCntOPktsOut_Object = MibTableColumn
rCCntOPktsOut = _RCCntOPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 4, 1, 2),
    _RCCntOPktsOut_Type()
)
rCCntOPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rCCntOPktsOut.setStatus("mandatory")
_RCCntTrPktsIn_Type = Counter32
_RCCntTrPktsIn_Object = MibTableColumn
rCCntTrPktsIn = _RCCntTrPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 4, 1, 3),
    _RCCntTrPktsIn_Type()
)
rCCntTrPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rCCntTrPktsIn.setStatus("mandatory")
_RCCntTrPktsOut_Type = Counter32
_RCCntTrPktsOut_Object = MibTableColumn
rCCntTrPktsOut = _RCCntTrPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 4, 1, 4),
    _RCCntTrPktsOut_Type()
)
rCCntTrPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rCCntTrPktsOut.setStatus("mandatory")
_RCCntAdjDown_Type = Counter32
_RCCntAdjDown_Object = MibTableColumn
rCCntAdjDown = _RCCntAdjDown_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 4, 1, 5),
    _RCCntAdjDown_Type()
)
rCCntAdjDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rCCntAdjDown.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 1, 4, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")
_Rnodes_ObjectIdentity = ObjectIdentity
rnodes = _Rnodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2)
)
_RnNmParms_ObjectIdentity = ObjectIdentity
rnNmParms = _RnNmParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 1)
)
_RnNmId_Type = OctetString
_RnNmId_Object = MibScalar
rnNmId = _RnNmId_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 1, 1),
    _RnNmId_Type()
)
rnNmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnNmId.setStatus("mandatory")
_RnNmPaddr_Type = OctetString
_RnNmPaddr_Object = MibScalar
rnNmPaddr = _RnNmPaddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 1, 2),
    _RnNmPaddr_Type()
)
rnNmPaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnNmPaddr.setStatus("mandatory")
_RnRtParms_ObjectIdentity = ObjectIdentity
rnRtParms = _RnRtParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2)
)
_RnRpAMaxC_Type = Integer32
_RnRpAMaxC_Object = MibScalar
rnRpAMaxC = _RnRpAMaxC_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 1),
    _RnRpAMaxC_Type()
)
rnRpAMaxC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnRpAMaxC.setStatus("mandatory")
_RnRpAMaxH_Type = Integer32
_RnRpAMaxH_Object = MibScalar
rnRpAMaxH = _RnRpAMaxH_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 2),
    _RnRpAMaxH_Type()
)
rnRpAMaxH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnRpAMaxH.setStatus("mandatory")
_RnRpBRtTmr_Type = Integer32
_RnRpBRtTmr_Object = MibScalar
rnRpBRtTmr = _RnRpBRtTmr_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 3),
    _RnRpBRtTmr_Type()
)
rnRpBRtTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnRpBRtTmr.setStatus("mandatory")
_RnRpBSize_Type = Integer32
_RnRpBSize_Object = MibScalar
rnRpBSize = _RnRpBSize_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 4),
    _RnRpBSize_Type()
)
rnRpBSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnRpBSize.setStatus("mandatory")
_RnRpMAddr_Type = Integer32
_RnRpMAddr_Object = MibScalar
rnRpMAddr = _RnRpMAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 5),
    _RnRpMAddr_Type()
)
rnRpMAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnRpMAddr.setStatus("mandatory")
_RnRpMArea_Type = Integer32
_RnRpMArea_Object = MibScalar
rnRpMArea = _RnRpMArea_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 6),
    _RnRpMArea_Type()
)
rnRpMArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnRpMArea.setStatus("mandatory")
_RnRpMaxBNR_Type = Integer32
_RnRpMaxBNR_Object = MibScalar
rnRpMaxBNR = _RnRpMaxBNR_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 7),
    _RnRpMaxBNR_Type()
)
rnRpMaxBNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnRpMaxBNR.setStatus("mandatory")
_RnRpMaxBR_Type = Integer32
_RnRpMaxBR_Object = MibScalar
rnRpMaxBR = _RnRpMaxBR_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 8),
    _RnRpMaxBR_Type()
)
rnRpMaxBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnRpMaxBR.setStatus("mandatory")
_RnRpMaxCir_Type = Integer32
_RnRpMaxCir_Object = MibScalar
rnRpMaxCir = _RnRpMaxCir_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 9),
    _RnRpMaxCir_Type()
)
rnRpMaxCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnRpMaxCir.setStatus("mandatory")
_RnRpMaxCost_Type = Integer32
_RnRpMaxCost_Object = MibScalar
rnRpMaxCost = _RnRpMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 10),
    _RnRpMaxCost_Type()
)
rnRpMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnRpMaxCost.setStatus("mandatory")
_RnRpMaxHops_Type = Integer32
_RnRpMaxHops_Object = MibScalar
rnRpMaxHops = _RnRpMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 11),
    _RnRpMaxHops_Type()
)
rnRpMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnRpMaxHops.setStatus("mandatory")
_RnRpMaxV_Type = Integer32
_RnRpMaxV_Object = MibScalar
rnRpMaxV = _RnRpMaxV_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 12),
    _RnRpMaxV_Type()
)
rnRpMaxV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnRpMaxV.setStatus("mandatory")
_RnRpVers_Type = OctetString
_RnRpVers_Object = MibScalar
rnRpVers = _RnRpVers_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 13),
    _RnRpVers_Type()
)
rnRpVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnRpVers.setStatus("mandatory")
_RnRpSegBuf_Type = Integer32
_RnRpSegBuf_Object = MibScalar
rnRpSegBuf = _RnRpSegBuf_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 14),
    _RnRpSegBuf_Type()
)
rnRpSegBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnRpSegBuf.setStatus("mandatory")
_RnRpType_Type = Integer32
_RnRpType_Object = MibScalar
rnRpType = _RnRpType_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 15),
    _RnRpType_Type()
)
rnRpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnRpType.setStatus("mandatory")
_RnRpAddr_Type = OctetString
_RnRpAddr_Object = MibScalar
rnRpAddr = _RnRpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 16),
    _RnRpAddr_Type()
)
rnRpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnRpAddr.setStatus("mandatory")
_RnRpUseL2A_Type = Integer32
_RnRpUseL2A_Object = MibScalar
rnRpUseL2A = _RnRpUseL2A_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 2, 17),
    _RnRpUseL2A_Type()
)
rnRpUseL2A.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnRpUseL2A.setStatus("mandatory")
_RnRtCount_ObjectIdentity = ObjectIdentity
rnRtCount = _RnRtCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 3)
)
_RnRcAgedPkt_Type = Counter32
_RnRcAgedPkt_Object = MibScalar
rnRcAgedPkt = _RnRcAgedPkt_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 3, 1),
    _RnRcAgedPkt_Type()
)
rnRcAgedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnRcAgedPkt.setStatus("mandatory")
_RnRcUnReach_Type = Counter32
_RnRcUnReach_Object = MibScalar
rnRcUnReach = _RnRcUnReach_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 3, 2),
    _RnRcUnReach_Type()
)
rnRcUnReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnRcUnReach.setStatus("mandatory")
_RnRcBadRange_Type = Counter32
_RnRcBadRange_Object = MibScalar
rnRcBadRange = _RnRcBadRange_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 3, 3),
    _RnRcBadRange_Type()
)
rnRcBadRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnRcBadRange.setStatus("mandatory")
_RnRcOversize_Type = Counter32
_RnRcOversize_Object = MibScalar
rnRcOversize = _RnRcOversize_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 3, 4),
    _RnRcOversize_Type()
)
rnRcOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnRcOversize.setStatus("mandatory")
_RnRcFormErr_Type = Counter32
_RnRcFormErr_Object = MibScalar
rnRcFormErr = _RnRcFormErr_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 3, 5),
    _RnRcFormErr_Type()
)
rnRcFormErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnRcFormErr.setStatus("mandatory")
_RnRcRtUpLoss_Type = Counter32
_RnRcRtUpLoss_Object = MibScalar
rnRcRtUpLoss = _RnRcRtUpLoss_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 3, 6),
    _RnRcRtUpLoss_Type()
)
rnRcRtUpLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnRcRtUpLoss.setStatus("mandatory")
_RnAdjTbl_Object = MibTable
rnAdjTbl = _RnAdjTbl_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    rnAdjTbl.setStatus("mandatory")
_RnAdjEnt_Object = MibTableRow
rnAdjEnt = _RnAdjEnt_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 4, 1)
)
rnAdjEnt.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rnAdjAddr"),
)
if mibBuilder.loadTexts:
    rnAdjEnt.setStatus("mandatory")
_RnAdjAddr_Type = OctetString
_RnAdjAddr_Object = MibTableColumn
rnAdjAddr = _RnAdjAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 4, 1, 1),
    _RnAdjAddr_Type()
)
rnAdjAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnAdjAddr.setStatus("mandatory")
_RnAdjState_Type = Integer32
_RnAdjState_Object = MibTableColumn
rnAdjState = _RnAdjState_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 4, 1, 2),
    _RnAdjState_Type()
)
rnAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnAdjState.setStatus("mandatory")
_RnAdjType_Type = Integer32
_RnAdjType_Object = MibTableColumn
rnAdjType = _RnAdjType_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 4, 1, 3),
    _RnAdjType_Type()
)
rnAdjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnAdjType.setStatus("mandatory")
_RnAdjCIdx_Type = Integer32
_RnAdjCIdx_Object = MibTableColumn
rnAdjCIdx = _RnAdjCIdx_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 4, 1, 4),
    _RnAdjCIdx_Type()
)
rnAdjCIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnAdjCIdx.setStatus("mandatory")
_RnAdjBSize_Type = Integer32
_RnAdjBSize_Object = MibTableColumn
rnAdjBSize = _RnAdjBSize_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 4, 1, 5),
    _RnAdjBSize_Type()
)
rnAdjBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnAdjBSize.setStatus("mandatory")
_RnAdjLTmr_Type = Integer32
_RnAdjLTmr_Object = MibTableColumn
rnAdjLTmr = _RnAdjLTmr_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 4, 1, 6),
    _RnAdjLTmr_Type()
)
rnAdjLTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnAdjLTmr.setStatus("mandatory")
_RnAdjPri_Type = Integer32
_RnAdjPri_Object = MibTableColumn
rnAdjPri = _RnAdjPri_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 4, 1, 7),
    _RnAdjPri_Type()
)
rnAdjPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnAdjPri.setStatus("mandatory")
_RnLvl1Tbl_Object = MibTable
rnLvl1Tbl = _RnLvl1Tbl_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    rnLvl1Tbl.setStatus("mandatory")
_RnLvl1Ent_Object = MibTableRow
rnLvl1Ent = _RnLvl1Ent_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 5, 1)
)
rnLvl1Ent.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rnLvl1Addr"),
)
if mibBuilder.loadTexts:
    rnLvl1Ent.setStatus("mandatory")
_RnLvl1Addr_Type = OctetString
_RnLvl1Addr_Object = MibTableColumn
rnLvl1Addr = _RnLvl1Addr_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 5, 1, 1),
    _RnLvl1Addr_Type()
)
rnLvl1Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnLvl1Addr.setStatus("mandatory")
_RnLvl1Cidx_Type = Integer32
_RnLvl1Cidx_Object = MibTableColumn
rnLvl1Cidx = _RnLvl1Cidx_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 5, 1, 2),
    _RnLvl1Cidx_Type()
)
rnLvl1Cidx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnLvl1Cidx.setStatus("mandatory")
_RnLvl1Cost_Type = Integer32
_RnLvl1Cost_Object = MibTableColumn
rnLvl1Cost = _RnLvl1Cost_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 5, 1, 3),
    _RnLvl1Cost_Type()
)
rnLvl1Cost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnLvl1Cost.setStatus("mandatory")
_RnLvl1Hops_Type = Integer32
_RnLvl1Hops_Object = MibTableColumn
rnLvl1Hops = _RnLvl1Hops_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 5, 1, 4),
    _RnLvl1Hops_Type()
)
rnLvl1Hops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnLvl1Hops.setStatus("mandatory")
_RnLvl1Next_Type = OctetString
_RnLvl1Next_Object = MibTableColumn
rnLvl1Next = _RnLvl1Next_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 2, 5, 1, 5),
    _RnLvl1Next_Type()
)
rnLvl1Next.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnLvl1Next.setStatus("mandatory")
_Rareas_ObjectIdentity = ObjectIdentity
rareas = _Rareas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 3)
)
_RaParmTbl_Object = MibTable
raParmTbl = _RaParmTbl_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    raParmTbl.setStatus("mandatory")
_RaParmEntry_Object = MibTableRow
raParmEntry = _RaParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 3, 1, 1)
)
raParmEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "raNum"),
)
if mibBuilder.loadTexts:
    raParmEntry.setStatus("mandatory")
_RaNum_Type = Integer32
_RaNum_Object = MibTableColumn
raNum = _RaNum_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 3, 1, 1, 1),
    _RaNum_Type()
)
raNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raNum.setStatus("mandatory")
_RaCIdx_Type = Integer32
_RaCIdx_Object = MibTableColumn
raCIdx = _RaCIdx_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 3, 1, 1, 2),
    _RaCIdx_Type()
)
raCIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raCIdx.setStatus("mandatory")
_RaCost_Type = Integer32
_RaCost_Object = MibTableColumn
raCost = _RaCost_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 3, 1, 1, 3),
    _RaCost_Type()
)
raCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raCost.setStatus("mandatory")
_RaHops_Type = Integer32
_RaHops_Object = MibTableColumn
raHops = _RaHops_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 3, 1, 1, 4),
    _RaHops_Type()
)
raHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raHops.setStatus("mandatory")
_RaNext_Type = OctetString
_RaNext_Object = MibTableColumn
raNext = _RaNext_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 1, 3, 1, 1, 5),
    _RaNext_Type()
)
raNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raNext.setStatus("mandatory")
_Decperm_ObjectIdentity = ObjectIdentity
decperm = _Decperm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 2, 2)
)
_Pcircs_ObjectIdentity = ObjectIdentity
pcircs = _Pcircs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 1)
)
_PccTable_Object = MibTable
pccTable = _PccTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pccTable.setStatus("mandatory")
_PccEntry_Object = MibTableRow
pccEntry = _PccEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 1, 1, 1)
)
pccEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pccIndex"),
)
if mibBuilder.loadTexts:
    pccEntry.setStatus("mandatory")
_PccIndex_Type = Integer32
_PccIndex_Object = MibTableColumn
pccIndex = _PccIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 1, 1, 1, 1),
    _PccIndex_Type()
)
pccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccIndex.setStatus("mandatory")
_PccState_Type = Integer32
_PccState_Object = MibTableColumn
pccState = _PccState_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 1, 1, 1, 2),
    _PccState_Type()
)
pccState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccState.setStatus("mandatory")
_PccCost_Type = Integer32
_PccCost_Object = MibTableColumn
pccCost = _PccCost_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 1, 1, 1, 3),
    _PccCost_Type()
)
pccCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccCost.setStatus("mandatory")
_PccHTimer_Type = Integer32
_PccHTimer_Object = MibTableColumn
pccHTimer = _PccHTimer_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 1, 1, 1, 4),
    _PccHTimer_Type()
)
pccHTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccHTimer.setStatus("mandatory")
_PbcTable_Object = MibTable
pbcTable = _PbcTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pbcTable.setStatus("mandatory")
_PbcEntry_Object = MibTableRow
pbcEntry = _PbcEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 1, 2, 1)
)
pbcEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pysmiFakeCol3"),
)
if mibBuilder.loadTexts:
    pbcEntry.setStatus("mandatory")
_PbcMrout_Type = Integer32
_PbcMrout_Object = MibTableColumn
pbcMrout = _PbcMrout_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 1, 2, 1, 1),
    _PbcMrout_Type()
)
pbcMrout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcMrout.setStatus("mandatory")
_PbcRpri_Type = Integer32
_PbcRpri_Object = MibTableColumn
pbcRpri = _PbcRpri_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 1, 2, 1, 2),
    _PbcRpri_Type()
)
pbcRpri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pbcRpri.setStatus("mandatory")
_PysmiFakeCol3_Type = Integer32
_PysmiFakeCol3_Object = MibTableColumn
pysmiFakeCol3 = _PysmiFakeCol3_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 1, 2, 1, 4294967295),
    _PysmiFakeCol3_Type()
)
pysmiFakeCol3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol3.setStatus("mandatory")
_Pnodes_ObjectIdentity = ObjectIdentity
pnodes = _Pnodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2)
)
_PnRtParms_ObjectIdentity = ObjectIdentity
pnRtParms = _PnRtParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1)
)
_PnRpAMaxC_Type = Integer32
_PnRpAMaxC_Object = MibScalar
pnRpAMaxC = _PnRpAMaxC_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 1),
    _PnRpAMaxC_Type()
)
pnRpAMaxC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpAMaxC.setStatus("mandatory")
_PnRpAMaxH_Type = Integer32
_PnRpAMaxH_Object = MibScalar
pnRpAMaxH = _PnRpAMaxH_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 2),
    _PnRpAMaxH_Type()
)
pnRpAMaxH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpAMaxH.setStatus("mandatory")
_PnRpBRtTmr_Type = Integer32
_PnRpBRtTmr_Object = MibScalar
pnRpBRtTmr = _PnRpBRtTmr_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 3),
    _PnRpBRtTmr_Type()
)
pnRpBRtTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpBRtTmr.setStatus("mandatory")
_PnRpBSize_Type = Integer32
_PnRpBSize_Object = MibScalar
pnRpBSize = _PnRpBSize_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 4),
    _PnRpBSize_Type()
)
pnRpBSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpBSize.setStatus("mandatory")
_PnRpMAddr_Type = Integer32
_PnRpMAddr_Object = MibScalar
pnRpMAddr = _PnRpMAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 5),
    _PnRpMAddr_Type()
)
pnRpMAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpMAddr.setStatus("mandatory")
_PnRpMArea_Type = Integer32
_PnRpMArea_Object = MibScalar
pnRpMArea = _PnRpMArea_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 6),
    _PnRpMArea_Type()
)
pnRpMArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpMArea.setStatus("mandatory")
_PnRpMaxBNR_Type = Integer32
_PnRpMaxBNR_Object = MibScalar
pnRpMaxBNR = _PnRpMaxBNR_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 7),
    _PnRpMaxBNR_Type()
)
pnRpMaxBNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpMaxBNR.setStatus("mandatory")
_PnRpMaxBR_Type = Integer32
_PnRpMaxBR_Object = MibScalar
pnRpMaxBR = _PnRpMaxBR_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 8),
    _PnRpMaxBR_Type()
)
pnRpMaxBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpMaxBR.setStatus("mandatory")
_PnRpMaxCost_Type = Integer32
_PnRpMaxCost_Object = MibScalar
pnRpMaxCost = _PnRpMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 9),
    _PnRpMaxCost_Type()
)
pnRpMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpMaxCost.setStatus("mandatory")
_PnRpMaxHops_Type = Integer32
_PnRpMaxHops_Object = MibScalar
pnRpMaxHops = _PnRpMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 10),
    _PnRpMaxHops_Type()
)
pnRpMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpMaxHops.setStatus("mandatory")
_PnRpMaxV_Type = Integer32
_PnRpMaxV_Object = MibScalar
pnRpMaxV = _PnRpMaxV_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 11),
    _PnRpMaxV_Type()
)
pnRpMaxV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpMaxV.setStatus("mandatory")
_PnRpType_Type = Integer32
_PnRpType_Object = MibScalar
pnRpType = _PnRpType_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 12),
    _PnRpType_Type()
)
pnRpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpType.setStatus("mandatory")
_PnRpAddr_Type = OctetString
_PnRpAddr_Object = MibScalar
pnRpAddr = _PnRpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 13),
    _PnRpAddr_Type()
)
pnRpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpAddr.setStatus("mandatory")
_PnRpUseL2A_Type = Integer32
_PnRpUseL2A_Object = MibScalar
pnRpUseL2A = _PnRpUseL2A_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 14),
    _PnRpUseL2A_Type()
)
pnRpUseL2A.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpUseL2A.setStatus("mandatory")
_PnRpRstDaddr_Type = Integer32
_PnRpRstDaddr_Object = MibScalar
pnRpRstDaddr = _PnRpRstDaddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 2, 1, 15),
    _PnRpRstDaddr_Type()
)
pnRpRstDaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnRpRstDaddr.setStatus("mandatory")


class _PDecDefaults_Type(Integer32):
    """Custom type pDecDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset-defaults", 1)
    )


_PDecDefaults_Type.__name__ = "Integer32"
_PDecDefaults_Object = MibScalar
pDecDefaults = _PDecDefaults_Object(
    (1, 3, 6, 1, 4, 1, 22, 2, 2, 3),
    _PDecDefaults_Type()
)
pDecDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pDecDefaults.setStatus("mandatory")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 3)
)
_Traprun_ObjectIdentity = ObjectIdentity
traprun = _Traprun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 3, 1)
)
_RTrapAddrTbl_Object = MibTable
rTrapAddrTbl = _RTrapAddrTbl_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rTrapAddrTbl.setStatus("mandatory")
_RTrapAddrEntry_Object = MibTableRow
rTrapAddrEntry = _RTrapAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1)
)
rTrapAddrEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rTrapAddrAddr"),
)
if mibBuilder.loadTexts:
    rTrapAddrEntry.setStatus("mandatory")
_RTrapAddrAddr_Type = IpAddress
_RTrapAddrAddr_Object = MibTableColumn
rTrapAddrAddr = _RTrapAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 1),
    _RTrapAddrAddr_Type()
)
rTrapAddrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTrapAddrAddr.setStatus("mandatory")
_RTrapAddrComm_Type = OctetString
_RTrapAddrComm_Object = MibTableColumn
rTrapAddrComm = _RTrapAddrComm_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 2),
    _RTrapAddrComm_Type()
)
rTrapAddrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTrapAddrComm.setStatus("mandatory")
_RTrapAddrVer_Type = Integer32
_RTrapAddrVer_Object = MibTableColumn
rTrapAddrVer = _RTrapAddrVer_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 3),
    _RTrapAddrVer_Type()
)
rTrapAddrVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTrapAddrVer.setStatus("mandatory")
_RTrapAddrType_Type = OctetString
_RTrapAddrType_Object = MibTableColumn
rTrapAddrType = _RTrapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 4),
    _RTrapAddrType_Type()
)
rTrapAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTrapAddrType.setStatus("mandatory")


class _RTrapAddrState_Type(Integer32):
    """Custom type rTrapAddrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RTrapAddrState_Type.__name__ = "Integer32"
_RTrapAddrState_Object = MibTableColumn
rTrapAddrState = _RTrapAddrState_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 1, 1, 1, 5),
    _RTrapAddrState_Type()
)
rTrapAddrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTrapAddrState.setStatus("mandatory")
_Traperm_ObjectIdentity = ObjectIdentity
traperm = _Traperm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 3, 2)
)
_PTrapAddrTbl_Object = MibTable
pTrapAddrTbl = _PTrapAddrTbl_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 1)
)
if mibBuilder.loadTexts:
    pTrapAddrTbl.setStatus("mandatory")
_PTrapAddrEntry_Object = MibTableRow
pTrapAddrEntry = _PTrapAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 1, 1)
)
pTrapAddrEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pTrapAddrAddr"),
)
if mibBuilder.loadTexts:
    pTrapAddrEntry.setStatus("mandatory")
_PTrapAddrAddr_Type = IpAddress
_PTrapAddrAddr_Object = MibTableColumn
pTrapAddrAddr = _PTrapAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 1, 1, 1),
    _PTrapAddrAddr_Type()
)
pTrapAddrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapAddrAddr.setStatus("mandatory")
_PTrapAddrComm_Type = OctetString
_PTrapAddrComm_Object = MibTableColumn
pTrapAddrComm = _PTrapAddrComm_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 1, 1, 2),
    _PTrapAddrComm_Type()
)
pTrapAddrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapAddrComm.setStatus("mandatory")
_PTrapAddrVer_Type = Integer32
_PTrapAddrVer_Object = MibTableColumn
pTrapAddrVer = _PTrapAddrVer_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 1, 1, 3),
    _PTrapAddrVer_Type()
)
pTrapAddrVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapAddrVer.setStatus("mandatory")
_PTrapAddrType_Type = OctetString
_PTrapAddrType_Object = MibTableColumn
pTrapAddrType = _PTrapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 1, 1, 4),
    _PTrapAddrType_Type()
)
pTrapAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapAddrType.setStatus("mandatory")
_PTrapAddrState_Type = Integer32
_PTrapAddrState_Object = MibTableColumn
pTrapAddrState = _PTrapAddrState_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 1, 1, 5),
    _PTrapAddrState_Type()
)
pTrapAddrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapAddrState.setStatus("mandatory")


class _PTrapDefaults_Type(Integer32):
    """Custom type pTrapDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset-defautls", 1)
    )


_PTrapDefaults_Type.__name__ = "Integer32"
_PTrapDefaults_Object = MibScalar
pTrapDefaults = _PTrapDefaults_Object(
    (1, 3, 6, 1, 4, 1, 22, 3, 2, 2),
    _PTrapDefaults_Type()
)
pTrapDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapDefaults.setStatus("mandatory")
_Dec2_ObjectIdentity = ObjectIdentity
dec2 = _Dec2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 4)
)
_Dec2run_ObjectIdentity = ObjectIdentity
dec2run = _Dec2run_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 4, 1)
)
_RClParmTbl_Object = MibTable
rClParmTbl = _RClParmTbl_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rClParmTbl.setStatus("mandatory")
_RClParmEntry_Object = MibTableRow
rClParmEntry = _RClParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 1, 1)
)
rClParmEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pysmiFakeCol4"),
)
if mibBuilder.loadTexts:
    rClParmEntry.setStatus("mandatory")
_RClState_Type = Integer32
_RClState_Object = MibTableColumn
rClState = _RClState_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 1, 1, 1),
    _RClState_Type()
)
rClState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rClState.setStatus("mandatory")
_RClSubSt_Type = Integer32
_RClSubSt_Object = MibTableColumn
rClSubSt = _RClSubSt_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 1, 1, 2),
    _RClSubSt_Type()
)
rClSubSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rClSubSt.setStatus("mandatory")
_PysmiFakeCol4_Type = Integer32
_PysmiFakeCol4_Object = MibTableColumn
pysmiFakeCol4 = _PysmiFakeCol4_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 1, 1, 4294967295),
    _PysmiFakeCol4_Type()
)
pysmiFakeCol4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol4.setStatus("mandatory")
_RBlParmTbl_Object = MibTable
rBlParmTbl = _RBlParmTbl_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 2)
)
if mibBuilder.loadTexts:
    rBlParmTbl.setStatus("mandatory")
_RBlParmEntry_Object = MibTableRow
rBlParmEntry = _RBlParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 2, 1)
)
rBlParmEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pysmiFakeCol5"),
)
if mibBuilder.loadTexts:
    rBlParmEntry.setStatus("mandatory")
_RBlHAddr_Type = OctetString
_RBlHAddr_Object = MibTableColumn
rBlHAddr = _RBlHAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 2, 1, 1),
    _RBlHAddr_Type()
)
rBlHAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rBlHAddr.setStatus("mandatory")
_PysmiFakeCol5_Type = Integer32
_PysmiFakeCol5_Object = MibTableColumn
pysmiFakeCol5 = _PysmiFakeCol5_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 2, 1, 4294967295),
    _PysmiFakeCol5_Type()
)
pysmiFakeCol5.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol5.setStatus("mandatory")
_RElCountTbl_Object = MibTable
rElCountTbl = _RElCountTbl_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3)
)
if mibBuilder.loadTexts:
    rElCountTbl.setStatus("mandatory")
_RElCountEntry_Object = MibTableRow
rElCountEntry = _RElCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1)
)
rElCountEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pysmiFakeCol6"),
)
if mibBuilder.loadTexts:
    rElCountEntry.setStatus("mandatory")
_RElFrIn_Type = Counter32
_RElFrIn_Object = MibTableColumn
rElFrIn = _RElFrIn_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 1),
    _RElFrIn_Type()
)
rElFrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElFrIn.setStatus("mandatory")
_RElFrOut_Type = Counter32
_RElFrOut_Object = MibTableColumn
rElFrOut = _RElFrOut_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 2),
    _RElFrOut_Type()
)
rElFrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElFrOut.setStatus("mandatory")
_RElBcBIn_Type = Counter32
_RElBcBIn_Object = MibScalar
rElBcBIn = _RElBcBIn_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 3),
    _RElBcBIn_Type()
)
rElBcBIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElBcBIn.setStatus("mandatory")
_RElBcFIn_Type = Counter32
_RElBcFIn_Object = MibTableColumn
rElBcFIn = _RElBcFIn_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 4),
    _RElBcFIn_Type()
)
rElBcFIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElBcFIn.setStatus("mandatory")
_RElMcBIn_Type = Counter32
_RElMcBIn_Object = MibTableColumn
rElMcBIn = _RElMcBIn_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 5),
    _RElMcBIn_Type()
)
rElMcBIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElMcBIn.setStatus("mandatory")
_RElMcFIn_Type = Counter32
_RElMcFIn_Object = MibTableColumn
rElMcFIn = _RElMcFIn_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 6),
    _RElMcFIn_Type()
)
rElMcFIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElMcFIn.setStatus("mandatory")
_RElFDef_Type = Counter32
_RElFDef_Object = MibTableColumn
rElFDef = _RElFDef_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 7),
    _RElFDef_Type()
)
rElFDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElFDef.setStatus("mandatory")
_RElF1Col_Type = Counter32
_RElF1Col_Object = MibTableColumn
rElF1Col = _RElF1Col_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 8),
    _RElF1Col_Type()
)
rElF1Col.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElF1Col.setStatus("mandatory")
_RElFMCol_Type = Counter32
_RElFMCol_Object = MibTableColumn
rElFMCol = _RElFMCol_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 9),
    _RElFMCol_Type()
)
rElFMCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElFMCol.setStatus("mandatory")
_RElOutF_Type = Counter32
_RElOutF_Object = MibTableColumn
rElOutF = _RElOutF_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 10),
    _RElOutF_Type()
)
rElOutF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElOutF.setStatus("mandatory")
_RElCDetF_Type = Counter32
_RElCDetF_Object = MibTableColumn
rElCDetF = _RElCDetF_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 11),
    _RElCDetF_Type()
)
rElCDetF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElCDetF.setStatus("mandatory")
_RElInF_Type = Counter32
_RElInF_Object = MibTableColumn
rElInF = _RElInF_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 12),
    _RElInF_Type()
)
rElInF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElInF.setStatus("mandatory")
_RElBadD_Type = Counter32
_RElBadD_Object = MibTableColumn
rElBadD = _RElBadD_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 13),
    _RElBadD_Type()
)
rElBadD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElBadD.setStatus("mandatory")
_RElOvRun_Type = Counter32
_RElOvRun_Object = MibTableColumn
rElOvRun = _RElOvRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 14),
    _RElOvRun_Type()
)
rElOvRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElOvRun.setStatus("mandatory")
_RElNoBuf_Type = Counter32
_RElNoBuf_Object = MibTableColumn
rElNoBuf = _RElNoBuf_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 15),
    _RElNoBuf_Type()
)
rElNoBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rElNoBuf.setStatus("mandatory")
_PysmiFakeCol6_Type = Integer32
_PysmiFakeCol6_Object = MibTableColumn
pysmiFakeCol6 = _PysmiFakeCol6_Object(
    (1, 3, 6, 1, 4, 1, 22, 4, 1, 3, 1, 4294967295),
    _PysmiFakeCol6_Type()
)
pysmiFakeCol6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol6.setStatus("mandatory")
_Dec2perm_ObjectIdentity = ObjectIdentity
dec2perm = _Dec2perm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 4, 2)
)
_PropSys_ObjectIdentity = ObjectIdentity
propSys = _PropSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 5)
)
_PropSysRun_ObjectIdentity = ObjectIdentity
propSysRun = _PropSysRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 5, 1)
)
_RTod_Type = OctetString
_RTod_Object = MibScalar
rTod = _RTod_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 1),
    _RTod_Type()
)
rTod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTod.setStatus("mandatory")
_RFddiIfIndex_Type = Integer32
_RFddiIfIndex_Object = MibScalar
rFddiIfIndex = _RFddiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 2),
    _RFddiIfIndex_Type()
)
rFddiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rFddiIfIndex.setStatus("mandatory")
_RPingTable_Object = MibTable
rPingTable = _RPingTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 3)
)
if mibBuilder.loadTexts:
    rPingTable.setStatus("mandatory")
_RPingEntry_Object = MibTableRow
rPingEntry = _RPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 3, 1)
)
rPingEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rPProto"),
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rPDest"),
)
if mibBuilder.loadTexts:
    rPingEntry.setStatus("mandatory")


class _RPProto_Type(Integer32):
    """Custom type rPProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("icmp-echo", 1)
    )


_RPProto_Type.__name__ = "Integer32"
_RPProto_Object = MibTableColumn
rPProto = _RPProto_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 3, 1, 1),
    _RPProto_Type()
)
rPProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPProto.setStatus("mandatory")
_RPDest_Type = IpAddress
_RPDest_Object = MibTableColumn
rPDest = _RPDest_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 3, 1, 2),
    _RPDest_Type()
)
rPDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPDest.setStatus("mandatory")
_RPTimeOut_Type = Integer32
_RPTimeOut_Object = MibTableColumn
rPTimeOut = _RPTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 3, 1, 3),
    _RPTimeOut_Type()
)
rPTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPTimeOut.setStatus("mandatory")


class _RPReply_Type(Integer32):
    """Custom type rPReply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("in-process", 3),
          ("no-response", 2))
    )


_RPReply_Type.__name__ = "Integer32"
_RPReply_Object = MibTableColumn
rPReply = _RPReply_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 3, 1, 4),
    _RPReply_Type()
)
rPReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPReply.setStatus("mandatory")


class _RPState_Type(Integer32):
    """Custom type rPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RPState_Type.__name__ = "Integer32"
_RPState_Object = MibTableColumn
rPState = _RPState_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 3, 1, 5),
    _RPState_Type()
)
rPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rPState.setStatus("mandatory")
_RDebugTable_Object = MibTable
rDebugTable = _RDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 4)
)
if mibBuilder.loadTexts:
    rDebugTable.setStatus("mandatory")
_RDebugEntry_Object = MibTableRow
rDebugEntry = _RDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 4, 1)
)
rDebugEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rDTaskId"),
)
if mibBuilder.loadTexts:
    rDebugEntry.setStatus("mandatory")
_RDTaskId_Type = Integer32
_RDTaskId_Object = MibTableColumn
rDTaskId = _RDTaskId_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 4, 1, 1),
    _RDTaskId_Type()
)
rDTaskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rDTaskId.setStatus("mandatory")


class _RDDevStat_Type(Integer32):
    """Custom type rDDevStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_RDDevStat_Type.__name__ = "Integer32"
_RDDevStat_Object = MibTableColumn
rDDevStat = _RDDevStat_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 4, 1, 2),
    _RDDevStat_Type()
)
rDDevStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rDDevStat.setStatus("mandatory")


class _RDRunStat_Type(Integer32):
    """Custom type rDRunStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_RDRunStat_Type.__name__ = "Integer32"
_RDRunStat_Object = MibTableColumn
rDRunStat = _RDRunStat_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 4, 1, 3),
    _RDRunStat_Type()
)
rDRunStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rDRunStat.setStatus("mandatory")
_RUDnld_Type = Integer32
_RUDnld_Object = MibScalar
rUDnld = _RUDnld_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 7),
    _RUDnld_Type()
)
rUDnld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rUDnld.setStatus("mandatory")
_RURset_Type = Integer32
_RURset_Object = MibScalar
rURset = _RURset_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 8),
    _RURset_Type()
)
rURset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rURset.setStatus("mandatory")


class _RUIpSw_Type(Integer32):
    """Custom type rUIpSw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_RUIpSw_Type.__name__ = "Integer32"
_RUIpSw_Object = MibScalar
rUIpSw = _RUIpSw_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 10),
    _RUIpSw_Type()
)
rUIpSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rUIpSw.setStatus("mandatory")


class _RUDecSw_Type(Integer32):
    """Custom type rUDecSw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_RUDecSw_Type.__name__ = "Integer32"
_RUDecSw_Object = MibScalar
rUDecSw = _RUDecSw_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 11),
    _RUDecSw_Type()
)
rUDecSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rUDecSw.setStatus("mandatory")


class _RUBrSw_Type(Integer32):
    """Custom type rUBrSw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_RUBrSw_Type.__name__ = "Integer32"
_RUBrSw_Object = MibScalar
rUBrSw = _RUBrSw_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 12),
    _RUBrSw_Type()
)
rUBrSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rUBrSw.setStatus("mandatory")


class _RUIpCfg_Type(Integer32):
    """Custom type rUIpCfg based on Integer32"""
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
        *(("rt-cfg-br-all", 3),
          ("rt-cfg-br-ether", 2),
          ("rt-cfg-host-only", 1),
          ("rt-cfg-rte-all", 4))
    )


_RUIpCfg_Type.__name__ = "Integer32"
_RUIpCfg_Object = MibScalar
rUIpCfg = _RUIpCfg_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 13),
    _RUIpCfg_Type()
)
rUIpCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rUIpCfg.setStatus("mandatory")
_RURunningVersion_Type = OctetString
_RURunningVersion_Object = MibScalar
rURunningVersion = _RURunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 14),
    _RURunningVersion_Type()
)
rURunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rURunningVersion.setStatus("mandatory")


class _RUDnldAllowed_Type(Integer32):
    """Custom type rUDnldAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_RUDnldAllowed_Type.__name__ = "Integer32"
_RUDnldAllowed_Object = MibScalar
rUDnldAllowed = _RUDnldAllowed_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 15),
    _RUDnldAllowed_Type()
)
rUDnldAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rUDnldAllowed.setStatus("mandatory")


class _RUInitFlash_Type(Integer32):
    """Custom type rUInitFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_RUInitFlash_Type.__name__ = "Integer32"
_RUInitFlash_Object = MibScalar
rUInitFlash = _RUInitFlash_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 1, 16),
    _RUInitFlash_Type()
)
rUInitFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rUInitFlash.setStatus("mandatory")
_PropSysPerm_ObjectIdentity = ObjectIdentity
propSysPerm = _PropSysPerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 5, 2)
)
_PPMibVer_Type = Integer32
_PPMibVer_Object = MibScalar
pPMibVer = _PPMibVer_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 2),
    _PPMibVer_Type()
)
pPMibVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPMibVer.setStatus("mandatory")


class _PEepVer_Type(Integer32):
    """Custom type pEepVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("brouter", 3),
          ("dual-eth", 2),
          ("single-eth", 1))
    )


_PEepVer_Type.__name__ = "Integer32"
_PEepVer_Object = MibScalar
pEepVer = _PEepVer_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 4),
    _PEepVer_Type()
)
pEepVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pEepVer.setStatus("mandatory")


class _PUIpSw_Type(Integer32):
    """Custom type pUIpSw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_PUIpSw_Type.__name__ = "Integer32"
_PUIpSw_Object = MibScalar
pUIpSw = _PUIpSw_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 6),
    _PUIpSw_Type()
)
pUIpSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pUIpSw.setStatus("mandatory")


class _PUDecSw_Type(Integer32):
    """Custom type pUDecSw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_PUDecSw_Type.__name__ = "Integer32"
_PUDecSw_Object = MibScalar
pUDecSw = _PUDecSw_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 7),
    _PUDecSw_Type()
)
pUDecSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pUDecSw.setStatus("mandatory")


class _PUBrSw_Type(Integer32):
    """Custom type pUBrSw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_PUBrSw_Type.__name__ = "Integer32"
_PUBrSw_Object = MibScalar
pUBrSw = _PUBrSw_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 8),
    _PUBrSw_Type()
)
pUBrSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pUBrSw.setStatus("mandatory")
_PUIpCfg_Type = Integer32
_PUIpCfg_Object = MibScalar
pUIpCfg = _PUIpCfg_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 9),
    _PUIpCfg_Type()
)
pUIpCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pUIpCfg.setStatus("mandatory")
_PULoadVersion_Type = OctetString
_PULoadVersion_Object = MibScalar
pULoadVersion = _PULoadVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 10),
    _PULoadVersion_Type()
)
pULoadVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pULoadVersion.setStatus("mandatory")
_PUDefaults_Type = Integer32
_PUDefaults_Object = MibScalar
pUDefaults = _PUDefaults_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 11),
    _PUDefaults_Type()
)
pUDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pUDefaults.setStatus("mandatory")
_PUFlashTable_Object = MibTable
pUFlashTable = _PUFlashTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 12)
)
if mibBuilder.loadTexts:
    pUFlashTable.setStatus("mandatory")
_PUFlashEntry_Object = MibTableRow
pUFlashEntry = _PUFlashEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 12, 1)
)
pUFlashEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "FlashIndex"),
)
if mibBuilder.loadTexts:
    pUFlashEntry.setStatus("mandatory")
_FlashIndex_Type = Integer32
_FlashIndex_Object = MibTableColumn
flashIndex = _FlashIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 12, 1, 1),
    _FlashIndex_Type()
)
flashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashIndex.setStatus("mandatory")
_FlashVersion_Type = OctetString
_FlashVersion_Object = MibTableColumn
flashVersion = _FlashVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 12, 1, 2),
    _FlashVersion_Type()
)
flashVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashVersion.setStatus("mandatory")


class _FlashState_Type(Integer32):
    """Custom type flashState based on Integer32"""
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
        *(("dnloading-in-process", 3),
          ("invalid", 2),
          ("reset-complete", 5),
          ("reset-in-progress", 4),
          ("valid", 1))
    )


_FlashState_Type.__name__ = "Integer32"
_FlashState_Object = MibTableColumn
flashState = _FlashState_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 12, 1, 3),
    _FlashState_Type()
)
flashState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashState.setStatus("mandatory")


class _SysPermBridgeAvailable_Type(Integer32):
    """Custom type sysPermBridgeAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SysPermBridgeAvailable_Type.__name__ = "Integer32"
_SysPermBridgeAvailable_Object = MibScalar
sysPermBridgeAvailable = _SysPermBridgeAvailable_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 13),
    _SysPermBridgeAvailable_Type()
)
sysPermBridgeAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPermBridgeAvailable.setStatus("mandatory")


class _SysPermIpAvailable_Type(Integer32):
    """Custom type sysPermIpAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SysPermIpAvailable_Type.__name__ = "Integer32"
_SysPermIpAvailable_Object = MibScalar
sysPermIpAvailable = _SysPermIpAvailable_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 14),
    _SysPermIpAvailable_Type()
)
sysPermIpAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPermIpAvailable.setStatus("mandatory")


class _SysPermDecAvailable_Type(Integer32):
    """Custom type sysPermDecAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SysPermDecAvailable_Type.__name__ = "Integer32"
_SysPermDecAvailable_Object = MibScalar
sysPermDecAvailable = _SysPermDecAvailable_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 15),
    _SysPermDecAvailable_Type()
)
sysPermDecAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPermDecAvailable.setStatus("mandatory")
_PUloadType_Type = Integer32
_PUloadType_Object = MibScalar
pUloadType = _PUloadType_Object(
    (1, 3, 6, 1, 4, 1, 22, 5, 2, 50),
    _PUloadType_Type()
)
pUloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pUloadType.setStatus("mandatory")
_PropIp_ObjectIdentity = ObjectIdentity
propIp = _PropIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 6)
)
_PropIpRun_ObjectIdentity = ObjectIdentity
propIpRun = _PropIpRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 6, 1)
)
_RIpMaskTable_Object = MibTable
rIpMaskTable = _RIpMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 1)
)
if mibBuilder.loadTexts:
    rIpMaskTable.setStatus("mandatory")
_RIpMaskEntry_Object = MibTableRow
rIpMaskEntry = _RIpMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 1, 1)
)
rIpMaskEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rMaskNet"),
)
if mibBuilder.loadTexts:
    rIpMaskEntry.setStatus("mandatory")
_RMaskNet_Type = IpAddress
_RMaskNet_Object = MibTableColumn
rMaskNet = _RMaskNet_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 1, 1, 1),
    _RMaskNet_Type()
)
rMaskNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rMaskNet.setStatus("mandatory")
_RMask_Type = IpAddress
_RMask_Object = MibTableColumn
rMask = _RMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 1, 1, 2),
    _RMask_Type()
)
rMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rMask.setStatus("mandatory")


class _RMaskState_Type(Integer32):
    """Custom type rMaskState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RMaskState_Type.__name__ = "Integer32"
_RMaskState_Object = MibTableColumn
rMaskState = _RMaskState_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 1, 1, 3),
    _RMaskState_Type()
)
rMaskState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rMaskState.setStatus("mandatory")
_RIpOurAddrTable_Object = MibTable
rIpOurAddrTable = _RIpOurAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 2)
)
if mibBuilder.loadTexts:
    rIpOurAddrTable.setStatus("mandatory")
_RIpOurAddrEntry_Object = MibTableRow
rIpOurAddrEntry = _RIpOurAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 2, 1)
)
rIpOurAddrEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pysmiFakeCol7"),
)
if mibBuilder.loadTexts:
    rIpOurAddrEntry.setStatus("mandatory")


class _RAddrDbcast_Type(Integer32):
    """Custom type rAddrDbcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bdcst-host", 2),
          ("bdcst-net", 3),
          ("no-directed-bdcst", 1))
    )


_RAddrDbcast_Type.__name__ = "Integer32"
_RAddrDbcast_Object = MibTableColumn
rAddrDbcast = _RAddrDbcast_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 2, 1, 1),
    _RAddrDbcast_Type()
)
rAddrDbcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAddrDbcast.setStatus("mandatory")
_RAddrRipMetric_Type = Integer32
_RAddrRipMetric_Object = MibTableColumn
rAddrRipMetric = _RAddrRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 2, 1, 2),
    _RAddrRipMetric_Type()
)
rAddrRipMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAddrRipMetric.setStatus("mandatory")


class _RAddrRipState_Type(Integer32):
    """Custom type rAddrRipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("quiet", 3))
    )


_RAddrRipState_Type.__name__ = "Integer32"
_RAddrRipState_Object = MibTableColumn
rAddrRipState = _RAddrRipState_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 2, 1, 3),
    _RAddrRipState_Type()
)
rAddrRipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAddrRipState.setStatus("mandatory")


class _RAddrState_Type(Integer32):
    """Custom type rAddrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RAddrState_Type.__name__ = "Integer32"
_RAddrState_Object = MibTableColumn
rAddrState = _RAddrState_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 2, 1, 4),
    _RAddrState_Type()
)
rAddrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAddrState.setStatus("mandatory")
_PysmiFakeCol7_Type = IpAddress
_PysmiFakeCol7_Object = MibTableColumn
pysmiFakeCol7 = _PysmiFakeCol7_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 2, 1, 4294967295),
    _PysmiFakeCol7_Type()
)
pysmiFakeCol7.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol7.setStatus("mandatory")
_RIpIfTable_Object = MibTable
rIpIfTable = _RIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 3)
)
if mibBuilder.loadTexts:
    rIpIfTable.setStatus("mandatory")
_RIpIfEntry_Object = MibTableRow
rIpIfEntry = _RIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 3, 1)
)
rIpIfEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pysmiFakeCol8"),
)
if mibBuilder.loadTexts:
    rIpIfEntry.setStatus("mandatory")


class _RIfArpStat_Type(Integer32):
    """Custom type rIfArpStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_RIfArpStat_Type.__name__ = "Integer32"
_RIfArpStat_Object = MibTableColumn
rIfArpStat = _RIfArpStat_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 3, 1, 1),
    _RIfArpStat_Type()
)
rIfArpStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rIfArpStat.setStatus("mandatory")


class _RIfPArpStat_Type(Integer32):
    """Custom type rIfPArpStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_RIfPArpStat_Type.__name__ = "Integer32"
_RIfPArpStat_Object = MibTableColumn
rIfPArpStat = _RIfPArpStat_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 3, 1, 2),
    _RIfPArpStat_Type()
)
rIfPArpStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rIfPArpStat.setStatus("mandatory")


class _RIfBcMask_Type(Integer32):
    """Custom type rIfBcMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_RIfBcMask_Type.__name__ = "Integer32"
_RIfBcMask_Object = MibTableColumn
rIfBcMask = _RIfBcMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 3, 1, 3),
    _RIfBcMask_Type()
)
rIfBcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rIfBcMask.setStatus("mandatory")
_PysmiFakeCol8_Type = Integer32
_PysmiFakeCol8_Object = MibTableColumn
pysmiFakeCol8 = _PysmiFakeCol8_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 3, 1, 4294967295),
    _PysmiFakeCol8_Type()
)
pysmiFakeCol8.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol8.setStatus("mandatory")
_RDftGw_Type = IpAddress
_RDftGw_Object = MibScalar
rDftGw = _RDftGw_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 4),
    _RDftGw_Type()
)
rDftGw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rDftGw.setStatus("mandatory")
_RIpAtTable_Object = MibTable
rIpAtTable = _RIpAtTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 5)
)
if mibBuilder.loadTexts:
    rIpAtTable.setStatus("mandatory")
_RIpAtEntry_Object = MibTableRow
rIpAtEntry = _RIpAtEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 5, 1)
)
rIpAtEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pysmiFakeCol9"),
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pysmiFakeCol10"),
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pysmiFakeCol11"),
)
if mibBuilder.loadTexts:
    rIpAtEntry.setStatus("mandatory")


class _RAtStatic_Type(Integer32):
    """Custom type rAtStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_RAtStatic_Type.__name__ = "Integer32"
_RAtStatic_Object = MibTableColumn
rAtStatic = _RAtStatic_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 5, 1, 1),
    _RAtStatic_Type()
)
rAtStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rAtStatic.setStatus("mandatory")
_RAtAge_Type = Integer32
_RAtAge_Object = MibTableColumn
rAtAge = _RAtAge_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 5, 1, 2),
    _RAtAge_Type()
)
rAtAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rAtAge.setStatus("mandatory")
_PysmiFakeCol11_Type = IpAddress
_PysmiFakeCol11_Object = MibTableColumn
pysmiFakeCol11 = _PysmiFakeCol11_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 5, 1, 4294967293),
    _PysmiFakeCol11_Type()
)
pysmiFakeCol11.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol11.setStatus("mandatory")
_PysmiFakeCol10_Type = Integer32
_PysmiFakeCol10_Object = MibTableColumn
pysmiFakeCol10 = _PysmiFakeCol10_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 5, 1, 4294967294),
    _PysmiFakeCol10_Type()
)
pysmiFakeCol10.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol10.setStatus("mandatory")
_PysmiFakeCol9_Type = Integer32
_PysmiFakeCol9_Object = MibTableColumn
pysmiFakeCol9 = _PysmiFakeCol9_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 5, 1, 4294967295),
    _PysmiFakeCol9_Type()
)
pysmiFakeCol9.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol9.setStatus("mandatory")
_RIpRtTable_Object = MibTable
rIpRtTable = _RIpRtTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 6)
)
if mibBuilder.loadTexts:
    rIpRtTable.setStatus("mandatory")
_RIpRtEntry_Object = MibTableRow
rIpRtEntry = _RIpRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 6, 1)
)
rIpRtEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pysmiFakeCol12"),
)
if mibBuilder.loadTexts:
    rIpRtEntry.setStatus("mandatory")


class _RRtStatic_Type(Integer32):
    """Custom type rRtStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_RRtStatic_Type.__name__ = "Integer32"
_RRtStatic_Object = MibTableColumn
rRtStatic = _RRtStatic_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 6, 1, 1),
    _RRtStatic_Type()
)
rRtStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rRtStatic.setStatus("mandatory")
_PysmiFakeCol12_Type = IpAddress
_PysmiFakeCol12_Object = MibTableColumn
pysmiFakeCol12 = _PysmiFakeCol12_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 6, 1, 4294967295),
    _PysmiFakeCol12_Type()
)
pysmiFakeCol12.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol12.setStatus("mandatory")


class _RRipTrInd_Type(Integer32):
    """Custom type rRipTrInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("not-trusted", 4),
          ("off", 2),
          ("trusted", 3))
    )


_RRipTrInd_Type.__name__ = "Integer32"
_RRipTrInd_Object = MibScalar
rRipTrInd = _RRipTrInd_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 7),
    _RRipTrInd_Type()
)
rRipTrInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rRipTrInd.setStatus("mandatory")
_RRipTrustTable_Object = MibTable
rRipTrustTable = _RRipTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 8)
)
if mibBuilder.loadTexts:
    rRipTrustTable.setStatus("mandatory")
_RRipTrustEntry_Object = MibTableRow
rRipTrustEntry = _RRipTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 8, 1)
)
rRipTrustEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rTrRestGw"),
)
if mibBuilder.loadTexts:
    rRipTrustEntry.setStatus("mandatory")
_RTrRestGw_Type = IpAddress
_RTrRestGw_Object = MibTableColumn
rTrRestGw = _RTrRestGw_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 8, 1, 1),
    _RTrRestGw_Type()
)
rTrRestGw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTrRestGw.setStatus("mandatory")


class _RTrRestState_Type(Integer32):
    """Custom type rTrRestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RTrRestState_Type.__name__ = "Integer32"
_RTrRestState_Object = MibTableColumn
rTrRestState = _RTrRestState_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 8, 1, 2),
    _RTrRestState_Type()
)
rTrRestState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTrRestState.setStatus("mandatory")
_RRipLsnIndTable_Object = MibTable
rRipLsnIndTable = _RRipLsnIndTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 9)
)
if mibBuilder.loadTexts:
    rRipLsnIndTable.setStatus("mandatory")
_RRipLsnIndEntry_Object = MibTableRow
rRipLsnIndEntry = _RRipLsnIndEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 9, 1)
)
rRipLsnIndEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rRipLsnIndDest"),
)
if mibBuilder.loadTexts:
    rRipLsnIndEntry.setStatus("mandatory")
_RRipLsnIndDest_Type = IpAddress
_RRipLsnIndDest_Object = MibTableColumn
rRipLsnIndDest = _RRipLsnIndDest_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 9, 1, 1),
    _RRipLsnIndDest_Type()
)
rRipLsnIndDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rRipLsnIndDest.setStatus("mandatory")


class _RRipLsnType_Type(Integer32):
    """Custom type rRipLsnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("do-not-listen", 4),
          ("listen", 3),
          ("off", 2))
    )


_RRipLsnType_Type.__name__ = "Integer32"
_RRipLsnType_Object = MibTableColumn
rRipLsnType = _RRipLsnType_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 9, 1, 2),
    _RRipLsnType_Type()
)
rRipLsnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rRipLsnType.setStatus("mandatory")
_RRipLsnTable_Object = MibTable
rRipLsnTable = _RRipLsnTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 10)
)
if mibBuilder.loadTexts:
    rRipLsnTable.setStatus("mandatory")
_RRipLsnEntry_Object = MibTableRow
rRipLsnEntry = _RRipLsnEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 10, 1)
)
rRipLsnEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rLsnAddr"),
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rLsnRstAddr"),
)
if mibBuilder.loadTexts:
    rRipLsnEntry.setStatus("mandatory")
_RLsnAddr_Type = IpAddress
_RLsnAddr_Object = MibTableColumn
rLsnAddr = _RLsnAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 10, 1, 1),
    _RLsnAddr_Type()
)
rLsnAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rLsnAddr.setStatus("mandatory")
_RLsnRstAddr_Type = IpAddress
_RLsnRstAddr_Object = MibTableColumn
rLsnRstAddr = _RLsnRstAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 10, 1, 2),
    _RLsnRstAddr_Type()
)
rLsnRstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rLsnRstAddr.setStatus("mandatory")


class _RLsnRstState_Type(Integer32):
    """Custom type rLsnRstState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RLsnRstState_Type.__name__ = "Integer32"
_RLsnRstState_Object = MibTableColumn
rLsnRstState = _RLsnRstState_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 10, 1, 3),
    _RLsnRstState_Type()
)
rLsnRstState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rLsnRstState.setStatus("mandatory")
_RRipAnncIndTable_Object = MibTable
rRipAnncIndTable = _RRipAnncIndTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 11)
)
if mibBuilder.loadTexts:
    rRipAnncIndTable.setStatus("mandatory")
_RRipAnncIndEntry_Object = MibTableRow
rRipAnncIndEntry = _RRipAnncIndEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 11, 1)
)
rRipAnncIndEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rRipAnncIndNet"),
)
if mibBuilder.loadTexts:
    rRipAnncIndEntry.setStatus("mandatory")
_RRipAnncIndNet_Type = IpAddress
_RRipAnncIndNet_Object = MibTableColumn
rRipAnncIndNet = _RRipAnncIndNet_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 11, 1, 1),
    _RRipAnncIndNet_Type()
)
rRipAnncIndNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rRipAnncIndNet.setStatus("mandatory")


class _RRipAnncType_Type(Integer32):
    """Custom type rRipAnncType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("announce", 3),
          ("do-not-announce", 4),
          ("off", 2))
    )


_RRipAnncType_Type.__name__ = "Integer32"
_RRipAnncType_Object = MibTableColumn
rRipAnncType = _RRipAnncType_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 11, 1, 2),
    _RRipAnncType_Type()
)
rRipAnncType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rRipAnncType.setStatus("mandatory")
_RRipAnncTable_Object = MibTable
rRipAnncTable = _RRipAnncTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 12)
)
if mibBuilder.loadTexts:
    rRipAnncTable.setStatus("mandatory")
_RRipAnncEntry_Object = MibTableRow
rRipAnncEntry = _RRipAnncEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 12, 1)
)
rRipAnncEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rAnncDestAddr"),
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rAnncNet"),
)
if mibBuilder.loadTexts:
    rRipAnncEntry.setStatus("mandatory")
_RAnncNet_Type = IpAddress
_RAnncNet_Object = MibTableColumn
rAnncNet = _RAnncNet_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 12, 1, 1),
    _RAnncNet_Type()
)
rAnncNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAnncNet.setStatus("mandatory")
_RAnncDestAddr_Type = IpAddress
_RAnncDestAddr_Object = MibTableColumn
rAnncDestAddr = _RAnncDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 12, 1, 2),
    _RAnncDestAddr_Type()
)
rAnncDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAnncDestAddr.setStatus("mandatory")


class _RAnncRstState_Type(Integer32):
    """Custom type rAnncRstState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RAnncRstState_Type.__name__ = "Integer32"
_RAnncRstState_Object = MibTableColumn
rAnncRstState = _RAnncRstState_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 12, 1, 3),
    _RAnncRstState_Type()
)
rAnncRstState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAnncRstState.setStatus("mandatory")
_RRipSrcTable_Object = MibTable
rRipSrcTable = _RRipSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 13)
)
if mibBuilder.loadTexts:
    rRipSrcTable.setStatus("mandatory")
_RRipSrcEntry_Object = MibTableRow
rRipSrcEntry = _RRipSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 13, 1)
)
rRipSrcEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rSrcAddr"),
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rSrcRstGw"),
)
if mibBuilder.loadTexts:
    rRipSrcEntry.setStatus("mandatory")
_RSrcAddr_Type = IpAddress
_RSrcAddr_Object = MibTableColumn
rSrcAddr = _RSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 13, 1, 1),
    _RSrcAddr_Type()
)
rSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rSrcAddr.setStatus("mandatory")
_RSrcRstGw_Type = IpAddress
_RSrcRstGw_Object = MibTableColumn
rSrcRstGw = _RSrcRstGw_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 13, 1, 2),
    _RSrcRstGw_Type()
)
rSrcRstGw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rSrcRstGw.setStatus("mandatory")


class _RSrcRstState_Type(Integer32):
    """Custom type rSrcRstState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RSrcRstState_Type.__name__ = "Integer32"
_RSrcRstState_Object = MibTableColumn
rSrcRstState = _RSrcRstState_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 13, 1, 3),
    _RSrcRstState_Type()
)
rSrcRstState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rSrcRstState.setStatus("mandatory")
_RIpRtEvTable_Object = MibTable
rIpRtEvTable = _RIpRtEvTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 14)
)
if mibBuilder.loadTexts:
    rIpRtEvTable.setStatus("mandatory")
_RIpRtEvEntry_Object = MibTableRow
rIpRtEvEntry = _RIpRtEvEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 14, 1)
)
rIpRtEvEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rRtEvTskId"),
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "rRtEvCode"),
)
if mibBuilder.loadTexts:
    rIpRtEvEntry.setStatus("mandatory")
_RRtEvTskId_Type = Integer32
_RRtEvTskId_Object = MibTableColumn
rRtEvTskId = _RRtEvTskId_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 14, 1, 1),
    _RRtEvTskId_Type()
)
rRtEvTskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rRtEvTskId.setStatus("mandatory")
_RRtEvCode_Type = Integer32
_RRtEvCode_Object = MibTableColumn
rRtEvCode = _RRtEvCode_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 14, 1, 2),
    _RRtEvCode_Type()
)
rRtEvCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rRtEvCode.setStatus("mandatory")


class _RRtEvStatus_Type(Integer32):
    """Custom type rRtEvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_RRtEvStatus_Type.__name__ = "Integer32"
_RRtEvStatus_Object = MibTableColumn
rRtEvStatus = _RRtEvStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 14, 1, 3),
    _RRtEvStatus_Type()
)
rRtEvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rRtEvStatus.setStatus("mandatory")
_RIpRipStats_ObjectIdentity = ObjectIdentity
rIpRipStats = _RIpRipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 15)
)
_RRipTotRef_Type = Counter32
_RRipTotRef_Object = MibScalar
rRipTotRef = _RRipTotRef_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 15, 1),
    _RRipTotRef_Type()
)
rRipTotRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rRipTotRef.setStatus("mandatory")
_RRipTotFnd_Type = Counter32
_RRipTotFnd_Object = MibScalar
rRipTotFnd = _RRipTotFnd_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 15, 2),
    _RRipTotFnd_Type()
)
rRipTotFnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rRipTotFnd.setStatus("mandatory")
_RRipUdpRcv_Type = Counter32
_RRipUdpRcv_Object = MibScalar
rRipUdpRcv = _RRipUdpRcv_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 15, 3),
    _RRipUdpRcv_Type()
)
rRipUdpRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rRipUdpRcv.setStatus("mandatory")
_RRipUdpXmt_Type = Counter32
_RRipUdpXmt_Object = MibScalar
rRipUdpXmt = _RRipUdpXmt_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 15, 4),
    _RRipUdpXmt_Type()
)
rRipUdpXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rRipUdpXmt.setStatus("mandatory")
_RRipUdpTrig_Type = Counter32
_RRipUdpTrig_Object = MibScalar
rRipUdpTrig = _RRipUdpTrig_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 15, 5),
    _RRipUdpTrig_Type()
)
rRipUdpTrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rRipUdpTrig.setStatus("mandatory")
_RRipReqRcv_Type = Counter32
_RRipReqRcv_Object = MibScalar
rRipReqRcv = _RRipReqRcv_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 15, 6),
    _RRipReqRcv_Type()
)
rRipReqRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rRipReqRcv.setStatus("mandatory")
_RRipReqXmt_Type = Counter32
_RRipReqXmt_Object = MibScalar
rRipReqXmt = _RRipReqXmt_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 15, 7),
    _RRipReqXmt_Type()
)
rRipReqXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rRipReqXmt.setStatus("mandatory")
_RRipInvRcv_Type = Counter32
_RRipInvRcv_Object = MibScalar
rRipInvRcv = _RRipInvRcv_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 15, 8),
    _RRipInvRcv_Type()
)
rRipInvRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rRipInvRcv.setStatus("mandatory")
_RIpArpStats_ObjectIdentity = ObjectIdentity
rIpArpStats = _RIpArpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 16)
)
_RArpInMsgs_Type = Counter32
_RArpInMsgs_Object = MibScalar
rArpInMsgs = _RArpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 16, 1),
    _RArpInMsgs_Type()
)
rArpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rArpInMsgs.setStatus("mandatory")
_RArpInErr_Type = Counter32
_RArpInErr_Object = MibScalar
rArpInErr = _RArpInErr_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 16, 2),
    _RArpInErr_Type()
)
rArpInErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rArpInErr.setStatus("mandatory")
_RArpInIll_Type = Counter32
_RArpInIll_Object = MibScalar
rArpInIll = _RArpInIll_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 16, 3),
    _RArpInIll_Type()
)
rArpInIll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rArpInIll.setStatus("mandatory")
_RArpInOpCd_Type = Counter32
_RArpInOpCd_Object = MibScalar
rArpInOpCd = _RArpInOpCd_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 16, 4),
    _RArpInOpCd_Type()
)
rArpInOpCd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rArpInOpCd.setStatus("mandatory")
_RArpInReq_Type = Counter32
_RArpInReq_Object = MibScalar
rArpInReq = _RArpInReq_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 16, 5),
    _RArpInReq_Type()
)
rArpInReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rArpInReq.setStatus("mandatory")
_RArpInRep_Type = Counter32
_RArpInRep_Object = MibScalar
rArpInRep = _RArpInRep_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 16, 6),
    _RArpInRep_Type()
)
rArpInRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rArpInRep.setStatus("mandatory")
_RArpInNotMe_Type = Counter32
_RArpInNotMe_Object = MibScalar
rArpInNotMe = _RArpInNotMe_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 16, 7),
    _RArpInNotMe_Type()
)
rArpInNotMe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rArpInNotMe.setStatus("mandatory")
_RArpOutMsgs_Type = Counter32
_RArpOutMsgs_Object = MibScalar
rArpOutMsgs = _RArpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 16, 8),
    _RArpOutMsgs_Type()
)
rArpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rArpOutMsgs.setStatus("mandatory")
_RArpOutErr_Type = Counter32
_RArpOutErr_Object = MibScalar
rArpOutErr = _RArpOutErr_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 16, 9),
    _RArpOutErr_Type()
)
rArpOutErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rArpOutErr.setStatus("mandatory")
_RArpOutReq_Type = Counter32
_RArpOutReq_Object = MibScalar
rArpOutReq = _RArpOutReq_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 16, 10),
    _RArpOutReq_Type()
)
rArpOutReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rArpOutReq.setStatus("mandatory")
_RArpOutRep_Type = Counter32
_RArpOutRep_Object = MibScalar
rArpOutRep = _RArpOutRep_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 16, 11),
    _RArpOutRep_Type()
)
rArpOutRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rArpOutRep.setStatus("mandatory")
_RArpResReq_Type = Counter32
_RArpResReq_Object = MibScalar
rArpResReq = _RArpResReq_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 16, 12),
    _RArpResReq_Type()
)
rArpResReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rArpResReq.setStatus("mandatory")
_RIpPArp_ObjectIdentity = ObjectIdentity
rIpPArp = _RIpPArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 17)
)
_RPArpInRep_Type = Counter32
_RPArpInRep_Object = MibScalar
rPArpInRep = _RPArpInRep_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 17, 1),
    _RPArpInRep_Type()
)
rPArpInRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPArpInRep.setStatus("mandatory")
_RPArpInReqSrch_Type = Counter32
_RPArpInReqSrch_Object = MibScalar
rPArpInReqSrch = _RPArpInReqSrch_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 17, 2),
    _RPArpInReqSrch_Type()
)
rPArpInReqSrch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPArpInReqSrch.setStatus("mandatory")
_RPArpOutReq_Type = Counter32
_RPArpOutReq_Object = MibScalar
rPArpOutReq = _RPArpOutReq_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 17, 3),
    _RPArpOutReq_Type()
)
rPArpOutReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPArpOutReq.setStatus("mandatory")
_RPArpOutRep_Type = Counter32
_RPArpOutRep_Object = MibScalar
rPArpOutRep = _RPArpOutRep_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 17, 4),
    _RPArpOutRep_Type()
)
rPArpOutRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPArpOutRep.setStatus("mandatory")
_RPArpOutActRep_Type = Counter32
_RPArpOutActRep_Object = MibScalar
rPArpOutActRep = _RPArpOutActRep_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 17, 5),
    _RPArpOutActRep_Type()
)
rPArpOutActRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPArpOutActRep.setStatus("mandatory")
_RPArpToutSrch_Type = Counter32
_RPArpToutSrch_Object = MibScalar
rPArpToutSrch = _RPArpToutSrch_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 17, 6),
    _RPArpToutSrch_Type()
)
rPArpToutSrch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPArpToutSrch.setStatus("mandatory")
_RPArpNaiveReq_Type = Counter32
_RPArpNaiveReq_Object = MibScalar
rPArpNaiveReq = _RPArpNaiveReq_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 1, 17, 7),
    _RPArpNaiveReq_Type()
)
rPArpNaiveReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rPArpNaiveReq.setStatus("mandatory")
_PropIpPerm_ObjectIdentity = ObjectIdentity
propIpPerm = _PropIpPerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 6, 2)
)
_PIpMaskTable_Object = MibTable
pIpMaskTable = _PIpMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 1)
)
if mibBuilder.loadTexts:
    pIpMaskTable.setStatus("mandatory")
_PIpMaskEntry_Object = MibTableRow
pIpMaskEntry = _PIpMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 1, 1)
)
pIpMaskEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pMaskNet"),
)
if mibBuilder.loadTexts:
    pIpMaskEntry.setStatus("mandatory")
_PMaskNet_Type = IpAddress
_PMaskNet_Object = MibTableColumn
pMaskNet = _PMaskNet_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 1, 1, 1),
    _PMaskNet_Type()
)
pMaskNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaskNet.setStatus("mandatory")
_PMask_Type = IpAddress
_PMask_Object = MibTableColumn
pMask = _PMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 1, 1, 2),
    _PMask_Type()
)
pMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMask.setStatus("mandatory")


class _PMaskState_Type(Integer32):
    """Custom type pMaskState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_PMaskState_Type.__name__ = "Integer32"
_PMaskState_Object = MibTableColumn
pMaskState = _PMaskState_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 1, 1, 3),
    _PMaskState_Type()
)
pMaskState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaskState.setStatus("mandatory")
_PIpOurAddrTable_Object = MibTable
pIpOurAddrTable = _PIpOurAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 2)
)
if mibBuilder.loadTexts:
    pIpOurAddrTable.setStatus("mandatory")
_PIpOurAddrEntry_Object = MibTableRow
pIpOurAddrEntry = _PIpOurAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 2, 1)
)
pIpOurAddrEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pAddrOurAddr"),
)
if mibBuilder.loadTexts:
    pIpOurAddrEntry.setStatus("mandatory")
_PAddrOurAddr_Type = IpAddress
_PAddrOurAddr_Object = MibTableColumn
pAddrOurAddr = _PAddrOurAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 2, 1, 1),
    _PAddrOurAddr_Type()
)
pAddrOurAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAddrOurAddr.setStatus("mandatory")
_PAddrIfIndex_Type = Integer32
_PAddrIfIndex_Object = MibTableColumn
pAddrIfIndex = _PAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 2, 1, 2),
    _PAddrIfIndex_Type()
)
pAddrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAddrIfIndex.setStatus("mandatory")
_PAddrBcAddr_Type = Integer32
_PAddrBcAddr_Object = MibTableColumn
pAddrBcAddr = _PAddrBcAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 2, 1, 3),
    _PAddrBcAddr_Type()
)
pAddrBcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAddrBcAddr.setStatus("mandatory")
_PAddrDbcast_Type = Integer32
_PAddrDbcast_Object = MibTableColumn
pAddrDbcast = _PAddrDbcast_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 2, 1, 4),
    _PAddrDbcast_Type()
)
pAddrDbcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAddrDbcast.setStatus("mandatory")
_PAddrRipMetric_Type = Integer32
_PAddrRipMetric_Object = MibTableColumn
pAddrRipMetric = _PAddrRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 2, 1, 5),
    _PAddrRipMetric_Type()
)
pAddrRipMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAddrRipMetric.setStatus("mandatory")


class _PAddrState_Type(Integer32):
    """Custom type pAddrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_PAddrState_Type.__name__ = "Integer32"
_PAddrState_Object = MibTableColumn
pAddrState = _PAddrState_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 2, 1, 6),
    _PAddrState_Type()
)
pAddrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAddrState.setStatus("mandatory")


class _PAddrRipState_Type(Integer32):
    """Custom type pAddrRipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("quiet", 3))
    )


_PAddrRipState_Type.__name__ = "Integer32"
_PAddrRipState_Object = MibTableColumn
pAddrRipState = _PAddrRipState_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 2, 1, 7),
    _PAddrRipState_Type()
)
pAddrRipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAddrRipState.setStatus("mandatory")
_PIpIfTable_Object = MibTable
pIpIfTable = _PIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 3)
)
if mibBuilder.loadTexts:
    pIpIfTable.setStatus("mandatory")
_PIpIfEntry_Object = MibTableRow
pIpIfEntry = _PIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 3, 1)
)
pIpIfEntry.setIndexNames(
    (0, "FIBRONICS-PROPRIETARY-FX8210-B-MIB", "pIfIndex"),
)
if mibBuilder.loadTexts:
    pIpIfEntry.setStatus("mandatory")
_PIfIndex_Type = Integer32
_PIfIndex_Object = MibTableColumn
pIfIndex = _PIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 3, 1, 1),
    _PIfIndex_Type()
)
pIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pIfIndex.setStatus("mandatory")
_PIfType_Type = Integer32
_PIfType_Object = MibTableColumn
pIfType = _PIfType_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 3, 1, 2),
    _PIfType_Type()
)
pIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pIfType.setStatus("mandatory")
_PIfMtu_Type = Integer32
_PIfMtu_Object = MibTableColumn
pIfMtu = _PIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 3, 1, 3),
    _PIfMtu_Type()
)
pIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pIfMtu.setStatus("mandatory")


class _PIfArpStat_Type(Integer32):
    """Custom type pIfArpStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_PIfArpStat_Type.__name__ = "Integer32"
_PIfArpStat_Object = MibTableColumn
pIfArpStat = _PIfArpStat_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 3, 1, 4),
    _PIfArpStat_Type()
)
pIfArpStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pIfArpStat.setStatus("mandatory")


class _PIfPArpStat_Type(Integer32):
    """Custom type pIfPArpStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_PIfPArpStat_Type.__name__ = "Integer32"
_PIfPArpStat_Object = MibTableColumn
pIfPArpStat = _PIfPArpStat_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 3, 1, 5),
    _PIfPArpStat_Type()
)
pIfPArpStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pIfPArpStat.setStatus("mandatory")
_PIfAdminStat_Type = Integer32
_PIfAdminStat_Object = MibTableColumn
pIfAdminStat = _PIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 3, 1, 6),
    _PIfAdminStat_Type()
)
pIfAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pIfAdminStat.setStatus("mandatory")


class _PIfBcMask_Type(Integer32):
    """Custom type pIfBcMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_PIfBcMask_Type.__name__ = "Integer32"
_PIfBcMask_Object = MibTableColumn
pIfBcMask = _PIfBcMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 3, 1, 7),
    _PIfBcMask_Type()
)
pIfBcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pIfBcMask.setStatus("mandatory")
_PDftGw_Type = IpAddress
_PDftGw_Object = MibScalar
pDftGw = _PDftGw_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 4),
    _PDftGw_Type()
)
pDftGw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pDftGw.setStatus("mandatory")


class _PIpDefaults_Type(Integer32):
    """Custom type pIpDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset-defaults", 1)
    )


_PIpDefaults_Type.__name__ = "Integer32"
_PIpDefaults_Object = MibScalar
pIpDefaults = _PIpDefaults_Object(
    (1, 3, 6, 1, 4, 1, 22, 6, 2, 5),
    _PIpDefaults_Type()
)
pIpDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pIpDefaults.setStatus("mandatory")
_PropFddi_ObjectIdentity = ObjectIdentity
propFddi = _PropFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 7)
)


class _FddiSmtChge_Type(Integer32):
    """Custom type fddiSmtChge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddiSmtChge_Type.__name__ = "Integer32"
_FddiSmtChge_Object = MibScalar
fddiSmtChge = _FddiSmtChge_Object(
    (1, 3, 6, 1, 4, 1, 22, 7, 1),
    _FddiSmtChge_Type()
)
fddiSmtChge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiSmtChge.setStatus("mandatory")


class _FddiMacChge_Type(Integer32):
    """Custom type fddiMacChge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddiMacChge_Type.__name__ = "Integer32"
_FddiMacChge_Object = MibScalar
fddiMacChge = _FddiMacChge_Object(
    (1, 3, 6, 1, 4, 1, 22, 7, 2),
    _FddiMacChge_Type()
)
fddiMacChge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiMacChge.setStatus("mandatory")


class _FddiPortChge_Type(Integer32):
    """Custom type fddiPortChge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddiPortChge_Type.__name__ = "Integer32"
_FddiPortChge_Object = MibScalar
fddiPortChge = _FddiPortChge_Object(
    (1, 3, 6, 1, 4, 1, 22, 7, 3),
    _FddiPortChge_Type()
)
fddiPortChge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiPortChge.setStatus("mandatory")


class _FddiAttachChge_Type(Integer32):
    """Custom type fddiAttachChge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddiAttachChge_Type.__name__ = "Integer32"
_FddiAttachChge_Object = MibScalar
fddiAttachChge = _FddiAttachChge_Object(
    (1, 3, 6, 1, 4, 1, 22, 7, 4),
    _FddiAttachChge_Type()
)
fddiAttachChge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiAttachChge.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBRONICS-PROPRIETARY-FX8210-B-MIB",
    **{"spartacus": spartacus,
       "dec": dec,
       "decrun": decrun,
       "rcircs": rcircs,
       "rCircNum": rCircNum,
       "rccTable": rccTable,
       "rccEntry": rccEntry,
       "rccIndex": rccIndex,
       "rccState": rccState,
       "rccType": rccType,
       "rccCost": rccCost,
       "rccBSize": rccBSize,
       "rccHTimer": rccHTimer,
       "rccLine": rccLine,
       "rbcTable": rbcTable,
       "rbcEntry": rbcEntry,
       "rbcDrout": rbcDrout,
       "rbcMrout": rbcMrout,
       "rbcRpri": rbcRpri,
       "pysmiFakeCol1": pysmiFakeCol1,
       "rCCntrs": rCCntrs,
       "rCCntrEntry": rCCntrEntry,
       "rCCntTePktsIn": rCCntTePktsIn,
       "rCCntOPktsOut": rCCntOPktsOut,
       "rCCntTrPktsIn": rCCntTrPktsIn,
       "rCCntTrPktsOut": rCCntTrPktsOut,
       "rCCntAdjDown": rCCntAdjDown,
       "pysmiFakeCol2": pysmiFakeCol2,
       "rnodes": rnodes,
       "rnNmParms": rnNmParms,
       "rnNmId": rnNmId,
       "rnNmPaddr": rnNmPaddr,
       "rnRtParms": rnRtParms,
       "rnRpAMaxC": rnRpAMaxC,
       "rnRpAMaxH": rnRpAMaxH,
       "rnRpBRtTmr": rnRpBRtTmr,
       "rnRpBSize": rnRpBSize,
       "rnRpMAddr": rnRpMAddr,
       "rnRpMArea": rnRpMArea,
       "rnRpMaxBNR": rnRpMaxBNR,
       "rnRpMaxBR": rnRpMaxBR,
       "rnRpMaxCir": rnRpMaxCir,
       "rnRpMaxCost": rnRpMaxCost,
       "rnRpMaxHops": rnRpMaxHops,
       "rnRpMaxV": rnRpMaxV,
       "rnRpVers": rnRpVers,
       "rnRpSegBuf": rnRpSegBuf,
       "rnRpType": rnRpType,
       "rnRpAddr": rnRpAddr,
       "rnRpUseL2A": rnRpUseL2A,
       "rnRtCount": rnRtCount,
       "rnRcAgedPkt": rnRcAgedPkt,
       "rnRcUnReach": rnRcUnReach,
       "rnRcBadRange": rnRcBadRange,
       "rnRcOversize": rnRcOversize,
       "rnRcFormErr": rnRcFormErr,
       "rnRcRtUpLoss": rnRcRtUpLoss,
       "rnAdjTbl": rnAdjTbl,
       "rnAdjEnt": rnAdjEnt,
       "rnAdjAddr": rnAdjAddr,
       "rnAdjState": rnAdjState,
       "rnAdjType": rnAdjType,
       "rnAdjCIdx": rnAdjCIdx,
       "rnAdjBSize": rnAdjBSize,
       "rnAdjLTmr": rnAdjLTmr,
       "rnAdjPri": rnAdjPri,
       "rnLvl1Tbl": rnLvl1Tbl,
       "rnLvl1Ent": rnLvl1Ent,
       "rnLvl1Addr": rnLvl1Addr,
       "rnLvl1Cidx": rnLvl1Cidx,
       "rnLvl1Cost": rnLvl1Cost,
       "rnLvl1Hops": rnLvl1Hops,
       "rnLvl1Next": rnLvl1Next,
       "rareas": rareas,
       "raParmTbl": raParmTbl,
       "raParmEntry": raParmEntry,
       "raNum": raNum,
       "raCIdx": raCIdx,
       "raCost": raCost,
       "raHops": raHops,
       "raNext": raNext,
       "decperm": decperm,
       "pcircs": pcircs,
       "pccTable": pccTable,
       "pccEntry": pccEntry,
       "pccIndex": pccIndex,
       "pccState": pccState,
       "pccCost": pccCost,
       "pccHTimer": pccHTimer,
       "pbcTable": pbcTable,
       "pbcEntry": pbcEntry,
       "pbcMrout": pbcMrout,
       "pbcRpri": pbcRpri,
       "pysmiFakeCol3": pysmiFakeCol3,
       "pnodes": pnodes,
       "pnRtParms": pnRtParms,
       "pnRpAMaxC": pnRpAMaxC,
       "pnRpAMaxH": pnRpAMaxH,
       "pnRpBRtTmr": pnRpBRtTmr,
       "pnRpBSize": pnRpBSize,
       "pnRpMAddr": pnRpMAddr,
       "pnRpMArea": pnRpMArea,
       "pnRpMaxBNR": pnRpMaxBNR,
       "pnRpMaxBR": pnRpMaxBR,
       "pnRpMaxCost": pnRpMaxCost,
       "pnRpMaxHops": pnRpMaxHops,
       "pnRpMaxV": pnRpMaxV,
       "pnRpType": pnRpType,
       "pnRpAddr": pnRpAddr,
       "pnRpUseL2A": pnRpUseL2A,
       "pnRpRstDaddr": pnRpRstDaddr,
       "pDecDefaults": pDecDefaults,
       "trap": trap,
       "traprun": traprun,
       "rTrapAddrTbl": rTrapAddrTbl,
       "rTrapAddrEntry": rTrapAddrEntry,
       "rTrapAddrAddr": rTrapAddrAddr,
       "rTrapAddrComm": rTrapAddrComm,
       "rTrapAddrVer": rTrapAddrVer,
       "rTrapAddrType": rTrapAddrType,
       "rTrapAddrState": rTrapAddrState,
       "traperm": traperm,
       "pTrapAddrTbl": pTrapAddrTbl,
       "pTrapAddrEntry": pTrapAddrEntry,
       "pTrapAddrAddr": pTrapAddrAddr,
       "pTrapAddrComm": pTrapAddrComm,
       "pTrapAddrVer": pTrapAddrVer,
       "pTrapAddrType": pTrapAddrType,
       "pTrapAddrState": pTrapAddrState,
       "pTrapDefaults": pTrapDefaults,
       "dec2": dec2,
       "dec2run": dec2run,
       "rClParmTbl": rClParmTbl,
       "rClParmEntry": rClParmEntry,
       "rClState": rClState,
       "rClSubSt": rClSubSt,
       "pysmiFakeCol4": pysmiFakeCol4,
       "rBlParmTbl": rBlParmTbl,
       "rBlParmEntry": rBlParmEntry,
       "rBlHAddr": rBlHAddr,
       "pysmiFakeCol5": pysmiFakeCol5,
       "rElCountTbl": rElCountTbl,
       "rElCountEntry": rElCountEntry,
       "rElFrIn": rElFrIn,
       "rElFrOut": rElFrOut,
       "rElBcBIn": rElBcBIn,
       "rElBcFIn": rElBcFIn,
       "rElMcBIn": rElMcBIn,
       "rElMcFIn": rElMcFIn,
       "rElFDef": rElFDef,
       "rElF1Col": rElF1Col,
       "rElFMCol": rElFMCol,
       "rElOutF": rElOutF,
       "rElCDetF": rElCDetF,
       "rElInF": rElInF,
       "rElBadD": rElBadD,
       "rElOvRun": rElOvRun,
       "rElNoBuf": rElNoBuf,
       "pysmiFakeCol6": pysmiFakeCol6,
       "dec2perm": dec2perm,
       "propSys": propSys,
       "propSysRun": propSysRun,
       "rTod": rTod,
       "rFddiIfIndex": rFddiIfIndex,
       "rPingTable": rPingTable,
       "rPingEntry": rPingEntry,
       "rPProto": rPProto,
       "rPDest": rPDest,
       "rPTimeOut": rPTimeOut,
       "rPReply": rPReply,
       "rPState": rPState,
       "rDebugTable": rDebugTable,
       "rDebugEntry": rDebugEntry,
       "rDTaskId": rDTaskId,
       "rDDevStat": rDDevStat,
       "rDRunStat": rDRunStat,
       "rUDnld": rUDnld,
       "rURset": rURset,
       "rUIpSw": rUIpSw,
       "rUDecSw": rUDecSw,
       "rUBrSw": rUBrSw,
       "rUIpCfg": rUIpCfg,
       "rURunningVersion": rURunningVersion,
       "rUDnldAllowed": rUDnldAllowed,
       "rUInitFlash": rUInitFlash,
       "propSysPerm": propSysPerm,
       "pPMibVer": pPMibVer,
       "pEepVer": pEepVer,
       "pUIpSw": pUIpSw,
       "pUDecSw": pUDecSw,
       "pUBrSw": pUBrSw,
       "pUIpCfg": pUIpCfg,
       "pULoadVersion": pULoadVersion,
       "pUDefaults": pUDefaults,
       "pUFlashTable": pUFlashTable,
       "pUFlashEntry": pUFlashEntry,
       "flashIndex": flashIndex,
       "flashVersion": flashVersion,
       "flashState": flashState,
       "sysPermBridgeAvailable": sysPermBridgeAvailable,
       "sysPermIpAvailable": sysPermIpAvailable,
       "sysPermDecAvailable": sysPermDecAvailable,
       "pUloadType": pUloadType,
       "propIp": propIp,
       "propIpRun": propIpRun,
       "rIpMaskTable": rIpMaskTable,
       "rIpMaskEntry": rIpMaskEntry,
       "rMaskNet": rMaskNet,
       "rMask": rMask,
       "rMaskState": rMaskState,
       "rIpOurAddrTable": rIpOurAddrTable,
       "rIpOurAddrEntry": rIpOurAddrEntry,
       "rAddrDbcast": rAddrDbcast,
       "rAddrRipMetric": rAddrRipMetric,
       "rAddrRipState": rAddrRipState,
       "rAddrState": rAddrState,
       "pysmiFakeCol7": pysmiFakeCol7,
       "rIpIfTable": rIpIfTable,
       "rIpIfEntry": rIpIfEntry,
       "rIfArpStat": rIfArpStat,
       "rIfPArpStat": rIfPArpStat,
       "rIfBcMask": rIfBcMask,
       "pysmiFakeCol8": pysmiFakeCol8,
       "rDftGw": rDftGw,
       "rIpAtTable": rIpAtTable,
       "rIpAtEntry": rIpAtEntry,
       "rAtStatic": rAtStatic,
       "rAtAge": rAtAge,
       "pysmiFakeCol11": pysmiFakeCol11,
       "pysmiFakeCol10": pysmiFakeCol10,
       "pysmiFakeCol9": pysmiFakeCol9,
       "rIpRtTable": rIpRtTable,
       "rIpRtEntry": rIpRtEntry,
       "rRtStatic": rRtStatic,
       "pysmiFakeCol12": pysmiFakeCol12,
       "rRipTrInd": rRipTrInd,
       "rRipTrustTable": rRipTrustTable,
       "rRipTrustEntry": rRipTrustEntry,
       "rTrRestGw": rTrRestGw,
       "rTrRestState": rTrRestState,
       "rRipLsnIndTable": rRipLsnIndTable,
       "rRipLsnIndEntry": rRipLsnIndEntry,
       "rRipLsnIndDest": rRipLsnIndDest,
       "rRipLsnType": rRipLsnType,
       "rRipLsnTable": rRipLsnTable,
       "rRipLsnEntry": rRipLsnEntry,
       "rLsnAddr": rLsnAddr,
       "rLsnRstAddr": rLsnRstAddr,
       "rLsnRstState": rLsnRstState,
       "rRipAnncIndTable": rRipAnncIndTable,
       "rRipAnncIndEntry": rRipAnncIndEntry,
       "rRipAnncIndNet": rRipAnncIndNet,
       "rRipAnncType": rRipAnncType,
       "rRipAnncTable": rRipAnncTable,
       "rRipAnncEntry": rRipAnncEntry,
       "rAnncNet": rAnncNet,
       "rAnncDestAddr": rAnncDestAddr,
       "rAnncRstState": rAnncRstState,
       "rRipSrcTable": rRipSrcTable,
       "rRipSrcEntry": rRipSrcEntry,
       "rSrcAddr": rSrcAddr,
       "rSrcRstGw": rSrcRstGw,
       "rSrcRstState": rSrcRstState,
       "rIpRtEvTable": rIpRtEvTable,
       "rIpRtEvEntry": rIpRtEvEntry,
       "rRtEvTskId": rRtEvTskId,
       "rRtEvCode": rRtEvCode,
       "rRtEvStatus": rRtEvStatus,
       "rIpRipStats": rIpRipStats,
       "rRipTotRef": rRipTotRef,
       "rRipTotFnd": rRipTotFnd,
       "rRipUdpRcv": rRipUdpRcv,
       "rRipUdpXmt": rRipUdpXmt,
       "rRipUdpTrig": rRipUdpTrig,
       "rRipReqRcv": rRipReqRcv,
       "rRipReqXmt": rRipReqXmt,
       "rRipInvRcv": rRipInvRcv,
       "rIpArpStats": rIpArpStats,
       "rArpInMsgs": rArpInMsgs,
       "rArpInErr": rArpInErr,
       "rArpInIll": rArpInIll,
       "rArpInOpCd": rArpInOpCd,
       "rArpInReq": rArpInReq,
       "rArpInRep": rArpInRep,
       "rArpInNotMe": rArpInNotMe,
       "rArpOutMsgs": rArpOutMsgs,
       "rArpOutErr": rArpOutErr,
       "rArpOutReq": rArpOutReq,
       "rArpOutRep": rArpOutRep,
       "rArpResReq": rArpResReq,
       "rIpPArp": rIpPArp,
       "rPArpInRep": rPArpInRep,
       "rPArpInReqSrch": rPArpInReqSrch,
       "rPArpOutReq": rPArpOutReq,
       "rPArpOutRep": rPArpOutRep,
       "rPArpOutActRep": rPArpOutActRep,
       "rPArpToutSrch": rPArpToutSrch,
       "rPArpNaiveReq": rPArpNaiveReq,
       "propIpPerm": propIpPerm,
       "pIpMaskTable": pIpMaskTable,
       "pIpMaskEntry": pIpMaskEntry,
       "pMaskNet": pMaskNet,
       "pMask": pMask,
       "pMaskState": pMaskState,
       "pIpOurAddrTable": pIpOurAddrTable,
       "pIpOurAddrEntry": pIpOurAddrEntry,
       "pAddrOurAddr": pAddrOurAddr,
       "pAddrIfIndex": pAddrIfIndex,
       "pAddrBcAddr": pAddrBcAddr,
       "pAddrDbcast": pAddrDbcast,
       "pAddrRipMetric": pAddrRipMetric,
       "pAddrState": pAddrState,
       "pAddrRipState": pAddrRipState,
       "pIpIfTable": pIpIfTable,
       "pIpIfEntry": pIpIfEntry,
       "pIfIndex": pIfIndex,
       "pIfType": pIfType,
       "pIfMtu": pIfMtu,
       "pIfArpStat": pIfArpStat,
       "pIfPArpStat": pIfPArpStat,
       "pIfAdminStat": pIfAdminStat,
       "pIfBcMask": pIfBcMask,
       "pDftGw": pDftGw,
       "pIpDefaults": pIpDefaults,
       "propFddi": propFddi,
       "fddiSmtChge": fddiSmtChge,
       "fddiMacChge": fddiMacChge,
       "fddiPortChge": fddiPortChge,
       "fddiAttachChge": fddiAttachChge}
)
