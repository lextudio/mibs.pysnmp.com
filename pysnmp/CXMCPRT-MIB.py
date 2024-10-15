# SNMP MIB module (CXMCPRT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXMCPRT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:39 2024
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

(cxMc600,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxMc600")

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

_CxMcPrt_ObjectIdentity = ObjectIdentity
cxMcPrt = _CxMcPrt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1)
)
_CxMcPrtGlobal_ObjectIdentity = ObjectIdentity
cxMcPrtGlobal = _CxMcPrtGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 1)
)


class _CxMcPrtGlobalConsoleRate_Type(Integer32):
    """Custom type cxMcPrtGlobalConsoleRate based on Integer32"""
    defaultValue = 19200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 19200),
    )


_CxMcPrtGlobalConsoleRate_Type.__name__ = "Integer32"
_CxMcPrtGlobalConsoleRate_Object = MibScalar
cxMcPrtGlobalConsoleRate = _CxMcPrtGlobalConsoleRate_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 1, 1),
    _CxMcPrtGlobalConsoleRate_Type()
)
cxMcPrtGlobalConsoleRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtGlobalConsoleRate.setStatus("optional")


class _CxMcPrtGlobalResetStat_Type(Integer32):
    """Custom type cxMcPrtGlobalResetStat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtGlobalResetStat_Type.__name__ = "Integer32"
_CxMcPrtGlobalResetStat_Object = MibScalar
cxMcPrtGlobalResetStat = _CxMcPrtGlobalResetStat_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 1, 2),
    _CxMcPrtGlobalResetStat_Type()
)
cxMcPrtGlobalResetStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtGlobalResetStat.setStatus("optional")


class _CxMcPrtGlobalStationId_Type(DisplayString):
    """Custom type cxMcPrtGlobalStationId based on DisplayString"""
    defaultValue = OctetString("           ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_CxMcPrtGlobalStationId_Type.__name__ = "DisplayString"
_CxMcPrtGlobalStationId_Object = MibScalar
cxMcPrtGlobalStationId = _CxMcPrtGlobalStationId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 1, 3),
    _CxMcPrtGlobalStationId_Type()
)
cxMcPrtGlobalStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtGlobalStationId.setStatus("optional")
_CxMcPrtCfgTable_Object = MibTable
cxMcPrtCfgTable = _CxMcPrtCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cxMcPrtCfgTable.setStatus("mandatory")
_CxMcPrtCfgEntry_Object = MibTableRow
cxMcPrtCfgEntry = _CxMcPrtCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 2, 1)
)
cxMcPrtCfgEntry.setIndexNames(
    (0, "CXMCPRT-MIB", "cxMcPrtCfgPortIndex"),
)
if mibBuilder.loadTexts:
    cxMcPrtCfgEntry.setStatus("mandatory")


class _CxMcPrtCfgPortIndex_Type(Integer32):
    """Custom type cxMcPrtCfgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcPrtCfgPortIndex_Type.__name__ = "Integer32"
_CxMcPrtCfgPortIndex_Object = MibTableColumn
cxMcPrtCfgPortIndex = _CxMcPrtCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 2, 1, 1),
    _CxMcPrtCfgPortIndex_Type()
)
cxMcPrtCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtCfgPortIndex.setStatus("mandatory")
_CxMcPrtCfgDriverUsed_Type = Integer32
_CxMcPrtCfgDriverUsed_Object = MibTableColumn
cxMcPrtCfgDriverUsed = _CxMcPrtCfgDriverUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 2, 1, 2),
    _CxMcPrtCfgDriverUsed_Type()
)
cxMcPrtCfgDriverUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCfgDriverUsed.setStatus("mandatory")


class _CxMcPrtCfgReinitPort_Type(Integer32):
    """Custom type cxMcPrtCfgReinitPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCfgReinitPort_Type.__name__ = "Integer32"
_CxMcPrtCfgReinitPort_Object = MibTableColumn
cxMcPrtCfgReinitPort = _CxMcPrtCfgReinitPort_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 2, 1, 3),
    _CxMcPrtCfgReinitPort_Type()
)
cxMcPrtCfgReinitPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCfgReinitPort.setStatus("optional")


class _CxMcPrtCfgUpdated_Type(Integer32):
    """Custom type cxMcPrtCfgUpdated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCfgUpdated_Type.__name__ = "Integer32"
_CxMcPrtCfgUpdated_Object = MibTableColumn
cxMcPrtCfgUpdated = _CxMcPrtCfgUpdated_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 2, 1, 4),
    _CxMcPrtCfgUpdated_Type()
)
cxMcPrtCfgUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtCfgUpdated.setStatus("mandatory")
_CxMcPrtStatTable_Object = MibTable
cxMcPrtStatTable = _CxMcPrtStatTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cxMcPrtStatTable.setStatus("mandatory")
_CxMcPrtStatEntry_Object = MibTableRow
cxMcPrtStatEntry = _CxMcPrtStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1)
)
cxMcPrtStatEntry.setIndexNames(
    (0, "CXMCPRT-MIB", "cxMcPrtStatPortNumber"),
)
if mibBuilder.loadTexts:
    cxMcPrtStatEntry.setStatus("mandatory")


class _CxMcPrtStatPortNumber_Type(Integer32):
    """Custom type cxMcPrtStatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcPrtStatPortNumber_Type.__name__ = "Integer32"
_CxMcPrtStatPortNumber_Object = MibTableColumn
cxMcPrtStatPortNumber = _CxMcPrtStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 1),
    _CxMcPrtStatPortNumber_Type()
)
cxMcPrtStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatPortNumber.setStatus("mandatory")


class _CxMcPrtStatRts_Type(Integer32):
    """Custom type cxMcPrtStatRts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CxMcPrtStatRts_Type.__name__ = "Integer32"
_CxMcPrtStatRts_Object = MibTableColumn
cxMcPrtStatRts = _CxMcPrtStatRts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 2),
    _CxMcPrtStatRts_Type()
)
cxMcPrtStatRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatRts.setStatus("mandatory")


class _CxMcPrtStatDtr_Type(Integer32):
    """Custom type cxMcPrtStatDtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CxMcPrtStatDtr_Type.__name__ = "Integer32"
_CxMcPrtStatDtr_Object = MibTableColumn
cxMcPrtStatDtr = _CxMcPrtStatDtr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 3),
    _CxMcPrtStatDtr_Type()
)
cxMcPrtStatDtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatDtr.setStatus("mandatory")


class _CxMcPrtStatDsr_Type(Integer32):
    """Custom type cxMcPrtStatDsr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CxMcPrtStatDsr_Type.__name__ = "Integer32"
_CxMcPrtStatDsr_Object = MibTableColumn
cxMcPrtStatDsr = _CxMcPrtStatDsr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 4),
    _CxMcPrtStatDsr_Type()
)
cxMcPrtStatDsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatDsr.setStatus("mandatory")


class _CxMcPrtStatDcd_Type(Integer32):
    """Custom type cxMcPrtStatDcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CxMcPrtStatDcd_Type.__name__ = "Integer32"
_CxMcPrtStatDcd_Object = MibTableColumn
cxMcPrtStatDcd = _CxMcPrtStatDcd_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 5),
    _CxMcPrtStatDcd_Type()
)
cxMcPrtStatDcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatDcd.setStatus("mandatory")


class _CxMcPrtStatCts_Type(Integer32):
    """Custom type cxMcPrtStatCts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CxMcPrtStatCts_Type.__name__ = "Integer32"
_CxMcPrtStatCts_Object = MibTableColumn
cxMcPrtStatCts = _CxMcPrtStatCts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 6),
    _CxMcPrtStatCts_Type()
)
cxMcPrtStatCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatCts.setStatus("mandatory")
_CxMcPrtStatCntMsgTx_Type = Counter32
_CxMcPrtStatCntMsgTx_Object = MibTableColumn
cxMcPrtStatCntMsgTx = _CxMcPrtStatCntMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 7),
    _CxMcPrtStatCntMsgTx_Type()
)
cxMcPrtStatCntMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatCntMsgTx.setStatus("mandatory")
_CxMcPrtStatCntMsgRx_Type = Counter32
_CxMcPrtStatCntMsgRx_Object = MibTableColumn
cxMcPrtStatCntMsgRx = _CxMcPrtStatCntMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 8),
    _CxMcPrtStatCntMsgRx_Type()
)
cxMcPrtStatCntMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatCntMsgRx.setStatus("mandatory")
_CxMcPrtStatCntReinit_Type = Counter32
_CxMcPrtStatCntReinit_Object = MibTableColumn
cxMcPrtStatCntReinit = _CxMcPrtStatCntReinit_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 9),
    _CxMcPrtStatCntReinit_Type()
)
cxMcPrtStatCntReinit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatCntReinit.setStatus("mandatory")
_CxMcPrtStatCntFlowCtrlTx_Type = Counter32
_CxMcPrtStatCntFlowCtrlTx_Object = MibTableColumn
cxMcPrtStatCntFlowCtrlTx = _CxMcPrtStatCntFlowCtrlTx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 10),
    _CxMcPrtStatCntFlowCtrlTx_Type()
)
cxMcPrtStatCntFlowCtrlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatCntFlowCtrlTx.setStatus("mandatory")
_CxMcPrtStatCntFlowCtrlRx_Type = Counter32
_CxMcPrtStatCntFlowCtrlRx_Object = MibTableColumn
cxMcPrtStatCntFlowCtrlRx = _CxMcPrtStatCntFlowCtrlRx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 11),
    _CxMcPrtStatCntFlowCtrlRx_Type()
)
cxMcPrtStatCntFlowCtrlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatCntFlowCtrlRx.setStatus("mandatory")
_CxMcPrtStatCntErrTx_Type = Counter32
_CxMcPrtStatCntErrTx_Object = MibTableColumn
cxMcPrtStatCntErrTx = _CxMcPrtStatCntErrTx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 12),
    _CxMcPrtStatCntErrTx_Type()
)
cxMcPrtStatCntErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatCntErrTx.setStatus("mandatory")
_CxMcPrtStatCntErrRx_Type = Counter32
_CxMcPrtStatCntErrRx_Object = MibTableColumn
cxMcPrtStatCntErrRx = _CxMcPrtStatCntErrRx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 13),
    _CxMcPrtStatCntErrRx_Type()
)
cxMcPrtStatCntErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatCntErrRx.setStatus("mandatory")
_CxMcPrtStatCntConnect_Type = Counter32
_CxMcPrtStatCntConnect_Object = MibTableColumn
cxMcPrtStatCntConnect = _CxMcPrtStatCntConnect_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 14),
    _CxMcPrtStatCntConnect_Type()
)
cxMcPrtStatCntConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatCntConnect.setStatus("mandatory")
_CxMcPrtStatCntChrDecomp_Type = Counter32
_CxMcPrtStatCntChrDecomp_Object = MibTableColumn
cxMcPrtStatCntChrDecomp = _CxMcPrtStatCntChrDecomp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 15),
    _CxMcPrtStatCntChrDecomp_Type()
)
cxMcPrtStatCntChrDecomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatCntChrDecomp.setStatus("mandatory")
_CxMcPrtStatCntChrComp_Type = Counter32
_CxMcPrtStatCntChrComp_Object = MibTableColumn
cxMcPrtStatCntChrComp = _CxMcPrtStatCntChrComp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 16),
    _CxMcPrtStatCntChrComp_Type()
)
cxMcPrtStatCntChrComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatCntChrComp.setStatus("mandatory")
_CxMcPrtStatCntBitDecomp_Type = Counter32
_CxMcPrtStatCntBitDecomp_Object = MibTableColumn
cxMcPrtStatCntBitDecomp = _CxMcPrtStatCntBitDecomp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 17),
    _CxMcPrtStatCntBitDecomp_Type()
)
cxMcPrtStatCntBitDecomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatCntBitDecomp.setStatus("mandatory")
_CxMcPrtStatCntBitComp_Type = Counter32
_CxMcPrtStatCntBitComp_Object = MibTableColumn
cxMcPrtStatCntBitComp = _CxMcPrtStatCntBitComp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 18),
    _CxMcPrtStatCntBitComp_Type()
)
cxMcPrtStatCntBitComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatCntBitComp.setStatus("mandatory")


class _CxMcPrtStatStation_Type(Integer32):
    """Custom type cxMcPrtStatStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CxMcPrtStatStation_Type.__name__ = "Integer32"
_CxMcPrtStatStation_Object = MibTableColumn
cxMcPrtStatStation = _CxMcPrtStatStation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 19),
    _CxMcPrtStatStation_Type()
)
cxMcPrtStatStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatStation.setStatus("mandatory")


class _CxMcPrtStatRoute_Type(Integer32):
    """Custom type cxMcPrtStatRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CxMcPrtStatRoute_Type.__name__ = "Integer32"
_CxMcPrtStatRoute_Object = MibTableColumn
cxMcPrtStatRoute = _CxMcPrtStatRoute_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 20),
    _CxMcPrtStatRoute_Type()
)
cxMcPrtStatRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatRoute.setStatus("mandatory")


class _CxMcPrtStatHwInterface_Type(Integer32):
    """Custom type cxMcPrtStatHwInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_CxMcPrtStatHwInterface_Type.__name__ = "Integer32"
_CxMcPrtStatHwInterface_Object = MibTableColumn
cxMcPrtStatHwInterface = _CxMcPrtStatHwInterface_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 21),
    _CxMcPrtStatHwInterface_Type()
)
cxMcPrtStatHwInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatHwInterface.setStatus("mandatory")
_CxMcPrtStatTimeTicks_Type = TimeTicks
_CxMcPrtStatTimeTicks_Object = MibTableColumn
cxMcPrtStatTimeTicks = _CxMcPrtStatTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 3, 1, 22),
    _CxMcPrtStatTimeTicks_Type()
)
cxMcPrtStatTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtStatTimeTicks.setStatus("mandatory")
_CxMcPrtPath_ObjectIdentity = ObjectIdentity
cxMcPrtPath = _CxMcPrtPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 4)
)


class _CxMcPrtPathStationPri_Type(Integer32):
    """Custom type cxMcPrtPathStationPri based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CxMcPrtPathStationPri_Type.__name__ = "Integer32"
_CxMcPrtPathStationPri_Object = MibScalar
cxMcPrtPathStationPri = _CxMcPrtPathStationPri_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 4, 1),
    _CxMcPrtPathStationPri_Type()
)
cxMcPrtPathStationPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtPathStationPri.setStatus("mandatory")


class _CxMcPrtPathRoutePri_Type(Integer32):
    """Custom type cxMcPrtPathRoutePri based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CxMcPrtPathRoutePri_Type.__name__ = "Integer32"
_CxMcPrtPathRoutePri_Object = MibScalar
cxMcPrtPathRoutePri = _CxMcPrtPathRoutePri_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 4, 2),
    _CxMcPrtPathRoutePri_Type()
)
cxMcPrtPathRoutePri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtPathRoutePri.setStatus("mandatory")


class _CxMcPrtPathStationScd_Type(Integer32):
    """Custom type cxMcPrtPathStationScd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CxMcPrtPathStationScd_Type.__name__ = "Integer32"
_CxMcPrtPathStationScd_Object = MibScalar
cxMcPrtPathStationScd = _CxMcPrtPathStationScd_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 4, 3),
    _CxMcPrtPathStationScd_Type()
)
cxMcPrtPathStationScd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtPathStationScd.setStatus("mandatory")


class _CxMcPrtPathRouteScd_Type(Integer32):
    """Custom type cxMcPrtPathRouteScd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CxMcPrtPathRouteScd_Type.__name__ = "Integer32"
_CxMcPrtPathRouteScd_Object = MibScalar
cxMcPrtPathRouteScd = _CxMcPrtPathRouteScd_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 4, 4),
    _CxMcPrtPathRouteScd_Type()
)
cxMcPrtPathRouteScd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtPathRouteScd.setStatus("mandatory")
_CxMcPrtDriver_ObjectIdentity = ObjectIdentity
cxMcPrtDriver = _CxMcPrtDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5)
)
_CxMcPrtBopTable_Object = MibTable
cxMcPrtBopTable = _CxMcPrtBopTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cxMcPrtBopTable.setStatus("mandatory")
_CxMcPrtBopEntry_Object = MibTableRow
cxMcPrtBopEntry = _CxMcPrtBopEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1)
)
cxMcPrtBopEntry.setIndexNames(
    (0, "CXMCPRT-MIB", "cxMcPrtBopPortUsed"),
)
if mibBuilder.loadTexts:
    cxMcPrtBopEntry.setStatus("mandatory")


class _CxMcPrtBopPortUsed_Type(Integer32):
    """Custom type cxMcPrtBopPortUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcPrtBopPortUsed_Type.__name__ = "Integer32"
_CxMcPrtBopPortUsed_Object = MibTableColumn
cxMcPrtBopPortUsed = _CxMcPrtBopPortUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 1),
    _CxMcPrtBopPortUsed_Type()
)
cxMcPrtBopPortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtBopPortUsed.setStatus("mandatory")


class _CxMcPrtBopPortStatus_Type(Integer32):
    """Custom type cxMcPrtBopPortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcPrtBopPortStatus_Type.__name__ = "Integer32"
_CxMcPrtBopPortStatus_Object = MibTableColumn
cxMcPrtBopPortStatus = _CxMcPrtBopPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 2),
    _CxMcPrtBopPortStatus_Type()
)
cxMcPrtBopPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopPortStatus.setStatus("mandatory")
_CxMcPrtBopComRate_Type = Integer32
_CxMcPrtBopComRate_Object = MibTableColumn
cxMcPrtBopComRate = _CxMcPrtBopComRate_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 3),
    _CxMcPrtBopComRate_Type()
)
cxMcPrtBopComRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopComRate.setStatus("mandatory")


class _CxMcPrtBopUseLnkErrPassthro_Type(Integer32):
    """Custom type cxMcPrtBopUseLnkErrPassthro based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBopUseLnkErrPassthro_Type.__name__ = "Integer32"
_CxMcPrtBopUseLnkErrPassthro_Object = MibTableColumn
cxMcPrtBopUseLnkErrPassthro = _CxMcPrtBopUseLnkErrPassthro_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 4),
    _CxMcPrtBopUseLnkErrPassthro_Type()
)
cxMcPrtBopUseLnkErrPassthro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopUseLnkErrPassthro.setStatus("mandatory")


class _CxMcPrtBopInterface_Type(Integer32):
    """Custom type cxMcPrtBopInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_CxMcPrtBopInterface_Type.__name__ = "Integer32"
_CxMcPrtBopInterface_Object = MibTableColumn
cxMcPrtBopInterface = _CxMcPrtBopInterface_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 5),
    _CxMcPrtBopInterface_Type()
)
cxMcPrtBopInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopInterface.setStatus("mandatory")


class _CxMcPrtBopRtsDcdModemCtrl_Type(Integer32):
    """Custom type cxMcPrtBopRtsDcdModemCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("vary", 2))
    )


_CxMcPrtBopRtsDcdModemCtrl_Type.__name__ = "Integer32"
_CxMcPrtBopRtsDcdModemCtrl_Object = MibTableColumn
cxMcPrtBopRtsDcdModemCtrl = _CxMcPrtBopRtsDcdModemCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 6),
    _CxMcPrtBopRtsDcdModemCtrl_Type()
)
cxMcPrtBopRtsDcdModemCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopRtsDcdModemCtrl.setStatus("mandatory")


class _CxMcPrtBopUseRtsDcdCndDataTx_Type(Integer32):
    """Custom type cxMcPrtBopUseRtsDcdCndDataTx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBopUseRtsDcdCndDataTx_Type.__name__ = "Integer32"
_CxMcPrtBopUseRtsDcdCndDataTx_Object = MibTableColumn
cxMcPrtBopUseRtsDcdCndDataTx = _CxMcPrtBopUseRtsDcdCndDataTx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 7),
    _CxMcPrtBopUseRtsDcdCndDataTx_Type()
)
cxMcPrtBopUseRtsDcdCndDataTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopUseRtsDcdCndDataTx.setStatus("mandatory")


class _CxMcPrtBopUseRtsDcdCndLnk_Type(Integer32):
    """Custom type cxMcPrtBopUseRtsDcdCndLnk based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBopUseRtsDcdCndLnk_Type.__name__ = "Integer32"
_CxMcPrtBopUseRtsDcdCndLnk_Object = MibTableColumn
cxMcPrtBopUseRtsDcdCndLnk = _CxMcPrtBopUseRtsDcdCndLnk_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 8),
    _CxMcPrtBopUseRtsDcdCndLnk_Type()
)
cxMcPrtBopUseRtsDcdCndLnk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopUseRtsDcdCndLnk.setStatus("mandatory")


class _CxMcPrtBopUseRtsDcdCndRem_Type(Integer32):
    """Custom type cxMcPrtBopUseRtsDcdCndRem based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBopUseRtsDcdCndRem_Type.__name__ = "Integer32"
_CxMcPrtBopUseRtsDcdCndRem_Object = MibTableColumn
cxMcPrtBopUseRtsDcdCndRem = _CxMcPrtBopUseRtsDcdCndRem_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 9),
    _CxMcPrtBopUseRtsDcdCndRem_Type()
)
cxMcPrtBopUseRtsDcdCndRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopUseRtsDcdCndRem.setStatus("mandatory")


class _CxMcPrtBopDtrCtsModemCtrl_Type(Integer32):
    """Custom type cxMcPrtBopDtrCtsModemCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("vary", 2))
    )


_CxMcPrtBopDtrCtsModemCtrl_Type.__name__ = "Integer32"
_CxMcPrtBopDtrCtsModemCtrl_Object = MibTableColumn
cxMcPrtBopDtrCtsModemCtrl = _CxMcPrtBopDtrCtsModemCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 10),
    _CxMcPrtBopDtrCtsModemCtrl_Type()
)
cxMcPrtBopDtrCtsModemCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopDtrCtsModemCtrl.setStatus("mandatory")


class _CxMcPrtBopUseDtrCtsCndRts_Type(Integer32):
    """Custom type cxMcPrtBopUseDtrCtsCndRts based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBopUseDtrCtsCndRts_Type.__name__ = "Integer32"
_CxMcPrtBopUseDtrCtsCndRts_Object = MibTableColumn
cxMcPrtBopUseDtrCtsCndRts = _CxMcPrtBopUseDtrCtsCndRts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 11),
    _CxMcPrtBopUseDtrCtsCndRts_Type()
)
cxMcPrtBopUseDtrCtsCndRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopUseDtrCtsCndRts.setStatus("mandatory")


class _CxMcPrtBopUseDtrCtsCndLnk_Type(Integer32):
    """Custom type cxMcPrtBopUseDtrCtsCndLnk based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBopUseDtrCtsCndLnk_Type.__name__ = "Integer32"
_CxMcPrtBopUseDtrCtsCndLnk_Object = MibTableColumn
cxMcPrtBopUseDtrCtsCndLnk = _CxMcPrtBopUseDtrCtsCndLnk_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 12),
    _CxMcPrtBopUseDtrCtsCndLnk_Type()
)
cxMcPrtBopUseDtrCtsCndLnk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopUseDtrCtsCndLnk.setStatus("mandatory")


class _CxMcPrtBopUseDtrCtsCndRem_Type(Integer32):
    """Custom type cxMcPrtBopUseDtrCtsCndRem based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBopUseDtrCtsCndRem_Type.__name__ = "Integer32"
_CxMcPrtBopUseDtrCtsCndRem_Object = MibTableColumn
cxMcPrtBopUseDtrCtsCndRem = _CxMcPrtBopUseDtrCtsCndRem_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 13),
    _CxMcPrtBopUseDtrCtsCndRem_Type()
)
cxMcPrtBopUseDtrCtsCndRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopUseDtrCtsCndRem.setStatus("mandatory")
_CxMcPrtBopLimitBeforeOut_Type = Integer32
_CxMcPrtBopLimitBeforeOut_Object = MibTableColumn
cxMcPrtBopLimitBeforeOut = _CxMcPrtBopLimitBeforeOut_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 14),
    _CxMcPrtBopLimitBeforeOut_Type()
)
cxMcPrtBopLimitBeforeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopLimitBeforeOut.setStatus("mandatory")


class _CxMcPrtBopUseOutCndCtsDtrOn_Type(Integer32):
    """Custom type cxMcPrtBopUseOutCndCtsDtrOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBopUseOutCndCtsDtrOn_Type.__name__ = "Integer32"
_CxMcPrtBopUseOutCndCtsDtrOn_Object = MibTableColumn
cxMcPrtBopUseOutCndCtsDtrOn = _CxMcPrtBopUseOutCndCtsDtrOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 15),
    _CxMcPrtBopUseOutCndCtsDtrOn_Type()
)
cxMcPrtBopUseOutCndCtsDtrOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopUseOutCndCtsDtrOn.setStatus("mandatory")


class _CxMcPrtBopUseInCndDcdRtsOn_Type(Integer32):
    """Custom type cxMcPrtBopUseInCndDcdRtsOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBopUseInCndDcdRtsOn_Type.__name__ = "Integer32"
_CxMcPrtBopUseInCndDcdRtsOn_Object = MibTableColumn
cxMcPrtBopUseInCndDcdRtsOn = _CxMcPrtBopUseInCndDcdRtsOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 16),
    _CxMcPrtBopUseInCndDcdRtsOn_Type()
)
cxMcPrtBopUseInCndDcdRtsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopUseInCndDcdRtsOn.setStatus("mandatory")


class _CxMcPrtBopSyncMode_Type(Integer32):
    """Custom type cxMcPrtBopSyncMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extern", 2),
          ("normal", 1))
    )


_CxMcPrtBopSyncMode_Type.__name__ = "Integer32"
_CxMcPrtBopSyncMode_Object = MibTableColumn
cxMcPrtBopSyncMode = _CxMcPrtBopSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 17),
    _CxMcPrtBopSyncMode_Type()
)
cxMcPrtBopSyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopSyncMode.setStatus("mandatory")


class _CxMcPrtBopDataLifetime_Type(Integer32):
    """Custom type cxMcPrtBopDataLifetime based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_CxMcPrtBopDataLifetime_Type.__name__ = "Integer32"
_CxMcPrtBopDataLifetime_Object = MibTableColumn
cxMcPrtBopDataLifetime = _CxMcPrtBopDataLifetime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 18),
    _CxMcPrtBopDataLifetime_Type()
)
cxMcPrtBopDataLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopDataLifetime.setStatus("mandatory")


class _CxMcPrtBopUseClockSync_Type(Integer32):
    """Custom type cxMcPrtBopUseClockSync based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBopUseClockSync_Type.__name__ = "Integer32"
_CxMcPrtBopUseClockSync_Object = MibTableColumn
cxMcPrtBopUseClockSync = _CxMcPrtBopUseClockSync_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 19),
    _CxMcPrtBopUseClockSync_Type()
)
cxMcPrtBopUseClockSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopUseClockSync.setStatus("mandatory")


class _CxMcPrtBopUseFlowCtrlClock_Type(Integer32):
    """Custom type cxMcPrtBopUseFlowCtrlClock based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBopUseFlowCtrlClock_Type.__name__ = "Integer32"
_CxMcPrtBopUseFlowCtrlClock_Object = MibTableColumn
cxMcPrtBopUseFlowCtrlClock = _CxMcPrtBopUseFlowCtrlClock_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 20),
    _CxMcPrtBopUseFlowCtrlClock_Type()
)
cxMcPrtBopUseFlowCtrlClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopUseFlowCtrlClock.setStatus("mandatory")
_CxMcPrtBopFlowCtrlRate_Type = Integer32
_CxMcPrtBopFlowCtrlRate_Object = MibTableColumn
cxMcPrtBopFlowCtrlRate = _CxMcPrtBopFlowCtrlRate_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 21),
    _CxMcPrtBopFlowCtrlRate_Type()
)
cxMcPrtBopFlowCtrlRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopFlowCtrlRate.setStatus("mandatory")
_CxMcPrtBopLimitOutFlowCtrl_Type = Integer32
_CxMcPrtBopLimitOutFlowCtrl_Object = MibTableColumn
cxMcPrtBopLimitOutFlowCtrl = _CxMcPrtBopLimitOutFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 22),
    _CxMcPrtBopLimitOutFlowCtrl_Type()
)
cxMcPrtBopLimitOutFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopLimitOutFlowCtrl.setStatus("mandatory")
_CxMcPrtBopLimitInFlowCtrl_Type = Integer32
_CxMcPrtBopLimitInFlowCtrl_Object = MibTableColumn
cxMcPrtBopLimitInFlowCtrl = _CxMcPrtBopLimitInFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 23),
    _CxMcPrtBopLimitInFlowCtrl_Type()
)
cxMcPrtBopLimitInFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopLimitInFlowCtrl.setStatus("mandatory")


class _CxMcPrtBopCoding_Type(Integer32):
    """Custom type cxMcPrtBopCoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("nrzi", 2))
    )


_CxMcPrtBopCoding_Type.__name__ = "Integer32"
_CxMcPrtBopCoding_Object = MibTableColumn
cxMcPrtBopCoding = _CxMcPrtBopCoding_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 24),
    _CxMcPrtBopCoding_Type()
)
cxMcPrtBopCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopCoding.setStatus("mandatory")


class _CxMcPrtBopOutIdleState_Type(Integer32):
    """Custom type cxMcPrtBopOutIdleState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flag", 1),
          ("mark", 2))
    )


_CxMcPrtBopOutIdleState_Type.__name__ = "Integer32"
_CxMcPrtBopOutIdleState_Object = MibTableColumn
cxMcPrtBopOutIdleState = _CxMcPrtBopOutIdleState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 25),
    _CxMcPrtBopOutIdleState_Type()
)
cxMcPrtBopOutIdleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopOutIdleState.setStatus("mandatory")


class _CxMcPrtBopDelayBeforeIdle_Type(Integer32):
    """Custom type cxMcPrtBopDelayBeforeIdle based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_CxMcPrtBopDelayBeforeIdle_Type.__name__ = "Integer32"
_CxMcPrtBopDelayBeforeIdle_Object = MibTableColumn
cxMcPrtBopDelayBeforeIdle = _CxMcPrtBopDelayBeforeIdle_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 26),
    _CxMcPrtBopDelayBeforeIdle_Type()
)
cxMcPrtBopDelayBeforeIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopDelayBeforeIdle.setStatus("mandatory")
_CxMcPrtBopOutPreambleLng_Type = Integer32
_CxMcPrtBopOutPreambleLng_Object = MibTableColumn
cxMcPrtBopOutPreambleLng = _CxMcPrtBopOutPreambleLng_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 1, 1, 27),
    _CxMcPrtBopOutPreambleLng_Type()
)
cxMcPrtBopOutPreambleLng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBopOutPreambleLng.setStatus("mandatory")
_CxMcPrtAsyTable_Object = MibTable
cxMcPrtAsyTable = _CxMcPrtAsyTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cxMcPrtAsyTable.setStatus("mandatory")
_CxMcPrtAsyEntry_Object = MibTableRow
cxMcPrtAsyEntry = _CxMcPrtAsyEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1)
)
cxMcPrtAsyEntry.setIndexNames(
    (0, "CXMCPRT-MIB", "cxMcPrtAsyPortUsed"),
)
if mibBuilder.loadTexts:
    cxMcPrtAsyEntry.setStatus("mandatory")
_CxMcPrtAsyPortUsed_Type = Integer32
_CxMcPrtAsyPortUsed_Object = MibTableColumn
cxMcPrtAsyPortUsed = _CxMcPrtAsyPortUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 1),
    _CxMcPrtAsyPortUsed_Type()
)
cxMcPrtAsyPortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtAsyPortUsed.setStatus("mandatory")


class _CxMcPrtAsyPortStatus_Type(Integer32):
    """Custom type cxMcPrtAsyPortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcPrtAsyPortStatus_Type.__name__ = "Integer32"
_CxMcPrtAsyPortStatus_Object = MibTableColumn
cxMcPrtAsyPortStatus = _CxMcPrtAsyPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 2),
    _CxMcPrtAsyPortStatus_Type()
)
cxMcPrtAsyPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyPortStatus.setStatus("mandatory")


class _CxMcPrtAsyComRate_Type(Integer32):
    """Custom type cxMcPrtAsyComRate based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(110, 128000),
    )


_CxMcPrtAsyComRate_Type.__name__ = "Integer32"
_CxMcPrtAsyComRate_Object = MibTableColumn
cxMcPrtAsyComRate = _CxMcPrtAsyComRate_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 3),
    _CxMcPrtAsyComRate_Type()
)
cxMcPrtAsyComRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyComRate.setStatus("mandatory")


class _CxMcPrtAsyUseLnkErrPassthro_Type(Integer32):
    """Custom type cxMcPrtAsyUseLnkErrPassthro based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtAsyUseLnkErrPassthro_Type.__name__ = "Integer32"
_CxMcPrtAsyUseLnkErrPassthro_Object = MibTableColumn
cxMcPrtAsyUseLnkErrPassthro = _CxMcPrtAsyUseLnkErrPassthro_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 4),
    _CxMcPrtAsyUseLnkErrPassthro_Type()
)
cxMcPrtAsyUseLnkErrPassthro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyUseLnkErrPassthro.setStatus("mandatory")


class _CxMcPrtAsyInterface_Type(Integer32):
    """Custom type cxMcPrtAsyInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_CxMcPrtAsyInterface_Type.__name__ = "Integer32"
_CxMcPrtAsyInterface_Object = MibTableColumn
cxMcPrtAsyInterface = _CxMcPrtAsyInterface_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 5),
    _CxMcPrtAsyInterface_Type()
)
cxMcPrtAsyInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyInterface.setStatus("mandatory")


class _CxMcPrtAsyRtsDcdModemCtrl_Type(Integer32):
    """Custom type cxMcPrtAsyRtsDcdModemCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("vary", 2))
    )


_CxMcPrtAsyRtsDcdModemCtrl_Type.__name__ = "Integer32"
_CxMcPrtAsyRtsDcdModemCtrl_Object = MibTableColumn
cxMcPrtAsyRtsDcdModemCtrl = _CxMcPrtAsyRtsDcdModemCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 6),
    _CxMcPrtAsyRtsDcdModemCtrl_Type()
)
cxMcPrtAsyRtsDcdModemCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyRtsDcdModemCtrl.setStatus("mandatory")


class _CxMcPrtAsyUseRtsDcdCndDataTx_Type(Integer32):
    """Custom type cxMcPrtAsyUseRtsDcdCndDataTx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtAsyUseRtsDcdCndDataTx_Type.__name__ = "Integer32"
_CxMcPrtAsyUseRtsDcdCndDataTx_Object = MibTableColumn
cxMcPrtAsyUseRtsDcdCndDataTx = _CxMcPrtAsyUseRtsDcdCndDataTx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 7),
    _CxMcPrtAsyUseRtsDcdCndDataTx_Type()
)
cxMcPrtAsyUseRtsDcdCndDataTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyUseRtsDcdCndDataTx.setStatus("mandatory")


class _CxMcPrtAsyUseRtsDcdCndLnk_Type(Integer32):
    """Custom type cxMcPrtAsyUseRtsDcdCndLnk based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtAsyUseRtsDcdCndLnk_Type.__name__ = "Integer32"
_CxMcPrtAsyUseRtsDcdCndLnk_Object = MibTableColumn
cxMcPrtAsyUseRtsDcdCndLnk = _CxMcPrtAsyUseRtsDcdCndLnk_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 8),
    _CxMcPrtAsyUseRtsDcdCndLnk_Type()
)
cxMcPrtAsyUseRtsDcdCndLnk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyUseRtsDcdCndLnk.setStatus("mandatory")


class _CxMcPrtAsyUseRtsDcdCndRem_Type(Integer32):
    """Custom type cxMcPrtAsyUseRtsDcdCndRem based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtAsyUseRtsDcdCndRem_Type.__name__ = "Integer32"
_CxMcPrtAsyUseRtsDcdCndRem_Object = MibTableColumn
cxMcPrtAsyUseRtsDcdCndRem = _CxMcPrtAsyUseRtsDcdCndRem_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 9),
    _CxMcPrtAsyUseRtsDcdCndRem_Type()
)
cxMcPrtAsyUseRtsDcdCndRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyUseRtsDcdCndRem.setStatus("mandatory")


class _CxMcPrtAsyDtrCtsModemCtrl_Type(Integer32):
    """Custom type cxMcPrtAsyDtrCtsModemCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("vary", 2))
    )


_CxMcPrtAsyDtrCtsModemCtrl_Type.__name__ = "Integer32"
_CxMcPrtAsyDtrCtsModemCtrl_Object = MibTableColumn
cxMcPrtAsyDtrCtsModemCtrl = _CxMcPrtAsyDtrCtsModemCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 10),
    _CxMcPrtAsyDtrCtsModemCtrl_Type()
)
cxMcPrtAsyDtrCtsModemCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyDtrCtsModemCtrl.setStatus("mandatory")


class _CxMcPrtAsyUseDtrCtsCndRts_Type(Integer32):
    """Custom type cxMcPrtAsyUseDtrCtsCndRts based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtAsyUseDtrCtsCndRts_Type.__name__ = "Integer32"
_CxMcPrtAsyUseDtrCtsCndRts_Object = MibTableColumn
cxMcPrtAsyUseDtrCtsCndRts = _CxMcPrtAsyUseDtrCtsCndRts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 11),
    _CxMcPrtAsyUseDtrCtsCndRts_Type()
)
cxMcPrtAsyUseDtrCtsCndRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyUseDtrCtsCndRts.setStatus("mandatory")


class _CxMcPrtAsyUseDtrCtsCndLnk_Type(Integer32):
    """Custom type cxMcPrtAsyUseDtrCtsCndLnk based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtAsyUseDtrCtsCndLnk_Type.__name__ = "Integer32"
_CxMcPrtAsyUseDtrCtsCndLnk_Object = MibTableColumn
cxMcPrtAsyUseDtrCtsCndLnk = _CxMcPrtAsyUseDtrCtsCndLnk_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 12),
    _CxMcPrtAsyUseDtrCtsCndLnk_Type()
)
cxMcPrtAsyUseDtrCtsCndLnk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyUseDtrCtsCndLnk.setStatus("mandatory")


class _CxMcPrtAsyUseDtrCtsCndRem_Type(Integer32):
    """Custom type cxMcPrtAsyUseDtrCtsCndRem based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtAsyUseDtrCtsCndRem_Type.__name__ = "Integer32"
_CxMcPrtAsyUseDtrCtsCndRem_Object = MibTableColumn
cxMcPrtAsyUseDtrCtsCndRem = _CxMcPrtAsyUseDtrCtsCndRem_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 13),
    _CxMcPrtAsyUseDtrCtsCndRem_Type()
)
cxMcPrtAsyUseDtrCtsCndRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyUseDtrCtsCndRem.setStatus("mandatory")


class _CxMcPrtAsyLimitBeforeOut_Type(Integer32):
    """Custom type cxMcPrtAsyLimitBeforeOut based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CxMcPrtAsyLimitBeforeOut_Type.__name__ = "Integer32"
_CxMcPrtAsyLimitBeforeOut_Object = MibTableColumn
cxMcPrtAsyLimitBeforeOut = _CxMcPrtAsyLimitBeforeOut_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 14),
    _CxMcPrtAsyLimitBeforeOut_Type()
)
cxMcPrtAsyLimitBeforeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyLimitBeforeOut.setStatus("mandatory")


class _CxMcPrtAsyOutCndCtsDtrOn_Type(Integer32):
    """Custom type cxMcPrtAsyOutCndCtsDtrOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtAsyOutCndCtsDtrOn_Type.__name__ = "Integer32"
_CxMcPrtAsyOutCndCtsDtrOn_Object = MibTableColumn
cxMcPrtAsyOutCndCtsDtrOn = _CxMcPrtAsyOutCndCtsDtrOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 15),
    _CxMcPrtAsyOutCndCtsDtrOn_Type()
)
cxMcPrtAsyOutCndCtsDtrOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyOutCndCtsDtrOn.setStatus("mandatory")


class _CxMcPrtAsyInCndDcdRtsOn_Type(Integer32):
    """Custom type cxMcPrtAsyInCndDcdRtsOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtAsyInCndDcdRtsOn_Type.__name__ = "Integer32"
_CxMcPrtAsyInCndDcdRtsOn_Object = MibTableColumn
cxMcPrtAsyInCndDcdRtsOn = _CxMcPrtAsyInCndDcdRtsOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 16),
    _CxMcPrtAsyInCndDcdRtsOn_Type()
)
cxMcPrtAsyInCndDcdRtsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyInCndDcdRtsOn.setStatus("mandatory")


class _CxMcPrtAsySyncMode_Type(Integer32):
    """Custom type cxMcPrtAsySyncMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extern", 2),
          ("normal", 1))
    )


_CxMcPrtAsySyncMode_Type.__name__ = "Integer32"
_CxMcPrtAsySyncMode_Object = MibTableColumn
cxMcPrtAsySyncMode = _CxMcPrtAsySyncMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 17),
    _CxMcPrtAsySyncMode_Type()
)
cxMcPrtAsySyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsySyncMode.setStatus("mandatory")


class _CxMcPrtAsyUseDataLifeLimited_Type(Integer32):
    """Custom type cxMcPrtAsyUseDataLifeLimited based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtAsyUseDataLifeLimited_Type.__name__ = "Integer32"
_CxMcPrtAsyUseDataLifeLimited_Object = MibTableColumn
cxMcPrtAsyUseDataLifeLimited = _CxMcPrtAsyUseDataLifeLimited_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 18),
    _CxMcPrtAsyUseDataLifeLimited_Type()
)
cxMcPrtAsyUseDataLifeLimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyUseDataLifeLimited.setStatus("mandatory")


class _CxMcPrtAsyDataLifetime_Type(Integer32):
    """Custom type cxMcPrtAsyDataLifetime based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_CxMcPrtAsyDataLifetime_Type.__name__ = "Integer32"
_CxMcPrtAsyDataLifetime_Object = MibTableColumn
cxMcPrtAsyDataLifetime = _CxMcPrtAsyDataLifetime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 19),
    _CxMcPrtAsyDataLifetime_Type()
)
cxMcPrtAsyDataLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyDataLifetime.setStatus("mandatory")


class _CxMcPrtAsyOutFlowCtrl_Type(Integer32):
    """Custom type cxMcPrtAsyOutFlowCtrl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ctsdtr", 3),
          ("disable", 1),
          ("xonxoff", 2))
    )


_CxMcPrtAsyOutFlowCtrl_Type.__name__ = "Integer32"
_CxMcPrtAsyOutFlowCtrl_Object = MibTableColumn
cxMcPrtAsyOutFlowCtrl = _CxMcPrtAsyOutFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 20),
    _CxMcPrtAsyOutFlowCtrl_Type()
)
cxMcPrtAsyOutFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyOutFlowCtrl.setStatus("mandatory")


class _CxMcPrtAsyInFlowCtrl_Type(Integer32):
    """Custom type cxMcPrtAsyInFlowCtrl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ctsdtr", 3),
          ("disable", 1),
          ("xonxoff", 2))
    )


_CxMcPrtAsyInFlowCtrl_Type.__name__ = "Integer32"
_CxMcPrtAsyInFlowCtrl_Object = MibTableColumn
cxMcPrtAsyInFlowCtrl = _CxMcPrtAsyInFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 21),
    _CxMcPrtAsyInFlowCtrl_Type()
)
cxMcPrtAsyInFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyInFlowCtrl.setStatus("mandatory")


class _CxMcPrtAsyXonChr_Type(Integer32):
    """Custom type cxMcPrtAsyXonChr based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxMcPrtAsyXonChr_Type.__name__ = "Integer32"
_CxMcPrtAsyXonChr_Object = MibTableColumn
cxMcPrtAsyXonChr = _CxMcPrtAsyXonChr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 22),
    _CxMcPrtAsyXonChr_Type()
)
cxMcPrtAsyXonChr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyXonChr.setStatus("mandatory")


class _CxMcPrtAsyXoffChr_Type(Integer32):
    """Custom type cxMcPrtAsyXoffChr based on Integer32"""
    defaultValue = 19

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxMcPrtAsyXoffChr_Type.__name__ = "Integer32"
_CxMcPrtAsyXoffChr_Object = MibTableColumn
cxMcPrtAsyXoffChr = _CxMcPrtAsyXoffChr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 23),
    _CxMcPrtAsyXoffChr_Type()
)
cxMcPrtAsyXoffChr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyXoffChr.setStatus("mandatory")


class _CxMcPrtAsyNbBitPerChr_Type(Integer32):
    """Custom type cxMcPrtAsyNbBitPerChr based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eight", 3),
          ("seven", 2),
          ("six", 1))
    )


_CxMcPrtAsyNbBitPerChr_Type.__name__ = "Integer32"
_CxMcPrtAsyNbBitPerChr_Object = MibTableColumn
cxMcPrtAsyNbBitPerChr = _CxMcPrtAsyNbBitPerChr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 24),
    _CxMcPrtAsyNbBitPerChr_Type()
)
cxMcPrtAsyNbBitPerChr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyNbBitPerChr.setStatus("mandatory")


class _CxMcPrtAsyParity_Type(Integer32):
    """Custom type cxMcPrtAsyParity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 1),
          ("odd", 3))
    )


_CxMcPrtAsyParity_Type.__name__ = "Integer32"
_CxMcPrtAsyParity_Object = MibTableColumn
cxMcPrtAsyParity = _CxMcPrtAsyParity_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 25),
    _CxMcPrtAsyParity_Type()
)
cxMcPrtAsyParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyParity.setStatus("mandatory")


class _CxMcPrtAsyNbStopBit_Type(Integer32):
    """Custom type cxMcPrtAsyNbStopBit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("onehalf", 2),
          ("two", 3))
    )


_CxMcPrtAsyNbStopBit_Type.__name__ = "Integer32"
_CxMcPrtAsyNbStopBit_Object = MibTableColumn
cxMcPrtAsyNbStopBit = _CxMcPrtAsyNbStopBit_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 26),
    _CxMcPrtAsyNbStopBit_Type()
)
cxMcPrtAsyNbStopBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyNbStopBit.setStatus("mandatory")


class _CxMcPrtAsyUseFlushOutChr_Type(Integer32):
    """Custom type cxMcPrtAsyUseFlushOutChr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtAsyUseFlushOutChr_Type.__name__ = "Integer32"
_CxMcPrtAsyUseFlushOutChr_Object = MibTableColumn
cxMcPrtAsyUseFlushOutChr = _CxMcPrtAsyUseFlushOutChr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 27),
    _CxMcPrtAsyUseFlushOutChr_Type()
)
cxMcPrtAsyUseFlushOutChr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyUseFlushOutChr.setStatus("mandatory")


class _CxMcPrtAsyFlushOutChr_Type(Integer32):
    """Custom type cxMcPrtAsyFlushOutChr based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxMcPrtAsyFlushOutChr_Type.__name__ = "Integer32"
_CxMcPrtAsyFlushOutChr_Object = MibTableColumn
cxMcPrtAsyFlushOutChr = _CxMcPrtAsyFlushOutChr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 2, 1, 28),
    _CxMcPrtAsyFlushOutChr_Type()
)
cxMcPrtAsyFlushOutChr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtAsyFlushOutChr.setStatus("mandatory")
_CxMcPrtCopTable_Object = MibTable
cxMcPrtCopTable = _CxMcPrtCopTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cxMcPrtCopTable.setStatus("mandatory")
_CxMcPrtCopEntry_Object = MibTableRow
cxMcPrtCopEntry = _CxMcPrtCopEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1)
)
cxMcPrtCopEntry.setIndexNames(
    (0, "CXMCPRT-MIB", "cxMcPrtCopPortUsed"),
)
if mibBuilder.loadTexts:
    cxMcPrtCopEntry.setStatus("mandatory")


class _CxMcPrtCopPortUsed_Type(Integer32):
    """Custom type cxMcPrtCopPortUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcPrtCopPortUsed_Type.__name__ = "Integer32"
_CxMcPrtCopPortUsed_Object = MibTableColumn
cxMcPrtCopPortUsed = _CxMcPrtCopPortUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 1),
    _CxMcPrtCopPortUsed_Type()
)
cxMcPrtCopPortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtCopPortUsed.setStatus("mandatory")


class _CxMcPrtCopPortStatus_Type(Integer32):
    """Custom type cxMcPrtCopPortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcPrtCopPortStatus_Type.__name__ = "Integer32"
_CxMcPrtCopPortStatus_Object = MibTableColumn
cxMcPrtCopPortStatus = _CxMcPrtCopPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 2),
    _CxMcPrtCopPortStatus_Type()
)
cxMcPrtCopPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopPortStatus.setStatus("mandatory")


class _CxMcPrtCopComRate_Type(Integer32):
    """Custom type cxMcPrtCopComRate based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(110, 128000),
    )


_CxMcPrtCopComRate_Type.__name__ = "Integer32"
_CxMcPrtCopComRate_Object = MibTableColumn
cxMcPrtCopComRate = _CxMcPrtCopComRate_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 3),
    _CxMcPrtCopComRate_Type()
)
cxMcPrtCopComRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopComRate.setStatus("mandatory")


class _CxMcPrtCopUseLnkErrPassthro_Type(Integer32):
    """Custom type cxMcPrtCopUseLnkErrPassthro based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCopUseLnkErrPassthro_Type.__name__ = "Integer32"
_CxMcPrtCopUseLnkErrPassthro_Object = MibTableColumn
cxMcPrtCopUseLnkErrPassthro = _CxMcPrtCopUseLnkErrPassthro_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 4),
    _CxMcPrtCopUseLnkErrPassthro_Type()
)
cxMcPrtCopUseLnkErrPassthro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopUseLnkErrPassthro.setStatus("mandatory")


class _CxMcPrtCopInterfaceType_Type(Integer32):
    """Custom type cxMcPrtCopInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_CxMcPrtCopInterfaceType_Type.__name__ = "Integer32"
_CxMcPrtCopInterfaceType_Object = MibTableColumn
cxMcPrtCopInterfaceType = _CxMcPrtCopInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 5),
    _CxMcPrtCopInterfaceType_Type()
)
cxMcPrtCopInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopInterfaceType.setStatus("mandatory")


class _CxMcPrtCopRtsDcdModemCtrl_Type(Integer32):
    """Custom type cxMcPrtCopRtsDcdModemCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("vary", 2))
    )


_CxMcPrtCopRtsDcdModemCtrl_Type.__name__ = "Integer32"
_CxMcPrtCopRtsDcdModemCtrl_Object = MibTableColumn
cxMcPrtCopRtsDcdModemCtrl = _CxMcPrtCopRtsDcdModemCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 6),
    _CxMcPrtCopRtsDcdModemCtrl_Type()
)
cxMcPrtCopRtsDcdModemCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopRtsDcdModemCtrl.setStatus("mandatory")


class _CxMcPrtCopUseRtsDcdCndDataTx_Type(Integer32):
    """Custom type cxMcPrtCopUseRtsDcdCndDataTx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCopUseRtsDcdCndDataTx_Type.__name__ = "Integer32"
_CxMcPrtCopUseRtsDcdCndDataTx_Object = MibTableColumn
cxMcPrtCopUseRtsDcdCndDataTx = _CxMcPrtCopUseRtsDcdCndDataTx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 7),
    _CxMcPrtCopUseRtsDcdCndDataTx_Type()
)
cxMcPrtCopUseRtsDcdCndDataTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopUseRtsDcdCndDataTx.setStatus("mandatory")


class _CxMcPrtCopUseRtsDcdCndLnk_Type(Integer32):
    """Custom type cxMcPrtCopUseRtsDcdCndLnk based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCopUseRtsDcdCndLnk_Type.__name__ = "Integer32"
_CxMcPrtCopUseRtsDcdCndLnk_Object = MibTableColumn
cxMcPrtCopUseRtsDcdCndLnk = _CxMcPrtCopUseRtsDcdCndLnk_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 8),
    _CxMcPrtCopUseRtsDcdCndLnk_Type()
)
cxMcPrtCopUseRtsDcdCndLnk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopUseRtsDcdCndLnk.setStatus("mandatory")


class _CxMcPrtCopUseRtsDcdCndRem_Type(Integer32):
    """Custom type cxMcPrtCopUseRtsDcdCndRem based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCopUseRtsDcdCndRem_Type.__name__ = "Integer32"
_CxMcPrtCopUseRtsDcdCndRem_Object = MibTableColumn
cxMcPrtCopUseRtsDcdCndRem = _CxMcPrtCopUseRtsDcdCndRem_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 9),
    _CxMcPrtCopUseRtsDcdCndRem_Type()
)
cxMcPrtCopUseRtsDcdCndRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopUseRtsDcdCndRem.setStatus("mandatory")


class _CxMcPrtCopDtrCtsModemCtrl_Type(Integer32):
    """Custom type cxMcPrtCopDtrCtsModemCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("vary", 2))
    )


_CxMcPrtCopDtrCtsModemCtrl_Type.__name__ = "Integer32"
_CxMcPrtCopDtrCtsModemCtrl_Object = MibTableColumn
cxMcPrtCopDtrCtsModemCtrl = _CxMcPrtCopDtrCtsModemCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 10),
    _CxMcPrtCopDtrCtsModemCtrl_Type()
)
cxMcPrtCopDtrCtsModemCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopDtrCtsModemCtrl.setStatus("mandatory")


class _CxMcPrtCopUseDtrCtsCndRts_Type(Integer32):
    """Custom type cxMcPrtCopUseDtrCtsCndRts based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCopUseDtrCtsCndRts_Type.__name__ = "Integer32"
_CxMcPrtCopUseDtrCtsCndRts_Object = MibTableColumn
cxMcPrtCopUseDtrCtsCndRts = _CxMcPrtCopUseDtrCtsCndRts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 11),
    _CxMcPrtCopUseDtrCtsCndRts_Type()
)
cxMcPrtCopUseDtrCtsCndRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopUseDtrCtsCndRts.setStatus("mandatory")


class _CxMcPrtCopUseDtrCtsCndLnk_Type(Integer32):
    """Custom type cxMcPrtCopUseDtrCtsCndLnk based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCopUseDtrCtsCndLnk_Type.__name__ = "Integer32"
_CxMcPrtCopUseDtrCtsCndLnk_Object = MibTableColumn
cxMcPrtCopUseDtrCtsCndLnk = _CxMcPrtCopUseDtrCtsCndLnk_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 12),
    _CxMcPrtCopUseDtrCtsCndLnk_Type()
)
cxMcPrtCopUseDtrCtsCndLnk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopUseDtrCtsCndLnk.setStatus("mandatory")


class _CxMcPrtCopUseDtrCtsCndRem_Type(Integer32):
    """Custom type cxMcPrtCopUseDtrCtsCndRem based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCopUseDtrCtsCndRem_Type.__name__ = "Integer32"
_CxMcPrtCopUseDtrCtsCndRem_Object = MibTableColumn
cxMcPrtCopUseDtrCtsCndRem = _CxMcPrtCopUseDtrCtsCndRem_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 13),
    _CxMcPrtCopUseDtrCtsCndRem_Type()
)
cxMcPrtCopUseDtrCtsCndRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopUseDtrCtsCndRem.setStatus("mandatory")


class _CxMcPrtCopLimitBeforeOut_Type(Integer32):
    """Custom type cxMcPrtCopLimitBeforeOut based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 4000),
    )


_CxMcPrtCopLimitBeforeOut_Type.__name__ = "Integer32"
_CxMcPrtCopLimitBeforeOut_Object = MibTableColumn
cxMcPrtCopLimitBeforeOut = _CxMcPrtCopLimitBeforeOut_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 14),
    _CxMcPrtCopLimitBeforeOut_Type()
)
cxMcPrtCopLimitBeforeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopLimitBeforeOut.setStatus("mandatory")


class _CxMcPrtCopUseOutCndCtsDtrOn_Type(Integer32):
    """Custom type cxMcPrtCopUseOutCndCtsDtrOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCopUseOutCndCtsDtrOn_Type.__name__ = "Integer32"
_CxMcPrtCopUseOutCndCtsDtrOn_Object = MibTableColumn
cxMcPrtCopUseOutCndCtsDtrOn = _CxMcPrtCopUseOutCndCtsDtrOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 15),
    _CxMcPrtCopUseOutCndCtsDtrOn_Type()
)
cxMcPrtCopUseOutCndCtsDtrOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopUseOutCndCtsDtrOn.setStatus("mandatory")


class _CxMcPrtCopUseInCndDcdRtsOn_Type(Integer32):
    """Custom type cxMcPrtCopUseInCndDcdRtsOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCopUseInCndDcdRtsOn_Type.__name__ = "Integer32"
_CxMcPrtCopUseInCndDcdRtsOn_Object = MibTableColumn
cxMcPrtCopUseInCndDcdRtsOn = _CxMcPrtCopUseInCndDcdRtsOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 16),
    _CxMcPrtCopUseInCndDcdRtsOn_Type()
)
cxMcPrtCopUseInCndDcdRtsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopUseInCndDcdRtsOn.setStatus("mandatory")


class _CxMcPrtCopSyncMode_Type(Integer32):
    """Custom type cxMcPrtCopSyncMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extern", 2),
          ("normal", 1))
    )


_CxMcPrtCopSyncMode_Type.__name__ = "Integer32"
_CxMcPrtCopSyncMode_Object = MibTableColumn
cxMcPrtCopSyncMode = _CxMcPrtCopSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 17),
    _CxMcPrtCopSyncMode_Type()
)
cxMcPrtCopSyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopSyncMode.setStatus("mandatory")


class _CxMcPrtCopDataLifetime_Type(Integer32):
    """Custom type cxMcPrtCopDataLifetime based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_CxMcPrtCopDataLifetime_Type.__name__ = "Integer32"
_CxMcPrtCopDataLifetime_Object = MibTableColumn
cxMcPrtCopDataLifetime = _CxMcPrtCopDataLifetime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 18),
    _CxMcPrtCopDataLifetime_Type()
)
cxMcPrtCopDataLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopDataLifetime.setStatus("mandatory")


class _CxMcPrtCopUseClockSync_Type(Integer32):
    """Custom type cxMcPrtCopUseClockSync based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCopUseClockSync_Type.__name__ = "Integer32"
_CxMcPrtCopUseClockSync_Object = MibTableColumn
cxMcPrtCopUseClockSync = _CxMcPrtCopUseClockSync_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 19),
    _CxMcPrtCopUseClockSync_Type()
)
cxMcPrtCopUseClockSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopUseClockSync.setStatus("mandatory")


class _CxMcPrtCopUseFlowCtrlClock_Type(Integer32):
    """Custom type cxMcPrtCopUseFlowCtrlClock based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCopUseFlowCtrlClock_Type.__name__ = "Integer32"
_CxMcPrtCopUseFlowCtrlClock_Object = MibTableColumn
cxMcPrtCopUseFlowCtrlClock = _CxMcPrtCopUseFlowCtrlClock_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 20),
    _CxMcPrtCopUseFlowCtrlClock_Type()
)
cxMcPrtCopUseFlowCtrlClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopUseFlowCtrlClock.setStatus("mandatory")


class _CxMcPrtCopFlowCtrlRate_Type(Integer32):
    """Custom type cxMcPrtCopFlowCtrlRate based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(110, 9600),
    )


_CxMcPrtCopFlowCtrlRate_Type.__name__ = "Integer32"
_CxMcPrtCopFlowCtrlRate_Object = MibTableColumn
cxMcPrtCopFlowCtrlRate = _CxMcPrtCopFlowCtrlRate_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 21),
    _CxMcPrtCopFlowCtrlRate_Type()
)
cxMcPrtCopFlowCtrlRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopFlowCtrlRate.setStatus("mandatory")


class _CxMcPrtCopLimitOutFlowCtrl_Type(Integer32):
    """Custom type cxMcPrtCopLimitOutFlowCtrl based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_CxMcPrtCopLimitOutFlowCtrl_Type.__name__ = "Integer32"
_CxMcPrtCopLimitOutFlowCtrl_Object = MibTableColumn
cxMcPrtCopLimitOutFlowCtrl = _CxMcPrtCopLimitOutFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 22),
    _CxMcPrtCopLimitOutFlowCtrl_Type()
)
cxMcPrtCopLimitOutFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopLimitOutFlowCtrl.setStatus("mandatory")


class _CxMcPrtCopLimitInFlowCtrl_Type(Integer32):
    """Custom type cxMcPrtCopLimitInFlowCtrl based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_CxMcPrtCopLimitInFlowCtrl_Type.__name__ = "Integer32"
_CxMcPrtCopLimitInFlowCtrl_Object = MibTableColumn
cxMcPrtCopLimitInFlowCtrl = _CxMcPrtCopLimitInFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 23),
    _CxMcPrtCopLimitInFlowCtrl_Type()
)
cxMcPrtCopLimitInFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopLimitInFlowCtrl.setStatus("mandatory")


class _CxMcPrtCopOutIdleState_Type(Integer32):
    """Custom type cxMcPrtCopOutIdleState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mark", 2),
          ("space", 1))
    )


_CxMcPrtCopOutIdleState_Type.__name__ = "Integer32"
_CxMcPrtCopOutIdleState_Object = MibTableColumn
cxMcPrtCopOutIdleState = _CxMcPrtCopOutIdleState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 24),
    _CxMcPrtCopOutIdleState_Type()
)
cxMcPrtCopOutIdleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopOutIdleState.setStatus("mandatory")


class _CxMcPrtCopNbBitPerChr_Type(Integer32):
    """Custom type cxMcPrtCopNbBitPerChr based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eight", 3),
          ("seven", 2),
          ("six", 1))
    )


_CxMcPrtCopNbBitPerChr_Type.__name__ = "Integer32"
_CxMcPrtCopNbBitPerChr_Object = MibTableColumn
cxMcPrtCopNbBitPerChr = _CxMcPrtCopNbBitPerChr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 25),
    _CxMcPrtCopNbBitPerChr_Type()
)
cxMcPrtCopNbBitPerChr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopNbBitPerChr.setStatus("mandatory")


class _CxMcPrtCopParity_Type(Integer32):
    """Custom type cxMcPrtCopParity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 1),
          ("odd", 3))
    )


_CxMcPrtCopParity_Type.__name__ = "Integer32"
_CxMcPrtCopParity_Object = MibTableColumn
cxMcPrtCopParity = _CxMcPrtCopParity_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 26),
    _CxMcPrtCopParity_Type()
)
cxMcPrtCopParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopParity.setStatus("mandatory")


class _CxMcPrtCopSyncChrOne_Type(Integer32):
    """Custom type cxMcPrtCopSyncChrOne based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxMcPrtCopSyncChrOne_Type.__name__ = "Integer32"
_CxMcPrtCopSyncChrOne_Object = MibTableColumn
cxMcPrtCopSyncChrOne = _CxMcPrtCopSyncChrOne_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 27),
    _CxMcPrtCopSyncChrOne_Type()
)
cxMcPrtCopSyncChrOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopSyncChrOne.setStatus("mandatory")


class _CxMcPrtCopSyncChrTwo_Type(Integer32):
    """Custom type cxMcPrtCopSyncChrTwo based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxMcPrtCopSyncChrTwo_Type.__name__ = "Integer32"
_CxMcPrtCopSyncChrTwo_Object = MibTableColumn
cxMcPrtCopSyncChrTwo = _CxMcPrtCopSyncChrTwo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 28),
    _CxMcPrtCopSyncChrTwo_Type()
)
cxMcPrtCopSyncChrTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopSyncChrTwo.setStatus("mandatory")


class _CxMcPrtCopNbSyncChr_Type(Integer32):
    """Custom type cxMcPrtCopNbSyncChr based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxMcPrtCopNbSyncChr_Type.__name__ = "Integer32"
_CxMcPrtCopNbSyncChr_Object = MibTableColumn
cxMcPrtCopNbSyncChr = _CxMcPrtCopNbSyncChr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 29),
    _CxMcPrtCopNbSyncChr_Type()
)
cxMcPrtCopNbSyncChr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopNbSyncChr.setStatus("mandatory")


class _CxMcPrtCopUseDesyncChr_Type(Integer32):
    """Custom type cxMcPrtCopUseDesyncChr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCopUseDesyncChr_Type.__name__ = "Integer32"
_CxMcPrtCopUseDesyncChr_Object = MibTableColumn
cxMcPrtCopUseDesyncChr = _CxMcPrtCopUseDesyncChr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 30),
    _CxMcPrtCopUseDesyncChr_Type()
)
cxMcPrtCopUseDesyncChr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopUseDesyncChr.setStatus("mandatory")


class _CxMcPrtCopDesyncChr_Type(Integer32):
    """Custom type cxMcPrtCopDesyncChr based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxMcPrtCopDesyncChr_Type.__name__ = "Integer32"
_CxMcPrtCopDesyncChr_Object = MibTableColumn
cxMcPrtCopDesyncChr = _CxMcPrtCopDesyncChr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 31),
    _CxMcPrtCopDesyncChr_Type()
)
cxMcPrtCopDesyncChr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopDesyncChr.setStatus("mandatory")


class _CxMcPrtCopNbDesyncChr_Type(Integer32):
    """Custom type cxMcPrtCopNbDesyncChr based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxMcPrtCopNbDesyncChr_Type.__name__ = "Integer32"
_CxMcPrtCopNbDesyncChr_Object = MibTableColumn
cxMcPrtCopNbDesyncChr = _CxMcPrtCopNbDesyncChr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 32),
    _CxMcPrtCopNbDesyncChr_Type()
)
cxMcPrtCopNbDesyncChr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopNbDesyncChr.setStatus("mandatory")


class _CxMcPrtCopUseDesyncRtsFall_Type(Integer32):
    """Custom type cxMcPrtCopUseDesyncRtsFall based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtCopUseDesyncRtsFall_Type.__name__ = "Integer32"
_CxMcPrtCopUseDesyncRtsFall_Object = MibTableColumn
cxMcPrtCopUseDesyncRtsFall = _CxMcPrtCopUseDesyncRtsFall_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 33),
    _CxMcPrtCopUseDesyncRtsFall_Type()
)
cxMcPrtCopUseDesyncRtsFall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopUseDesyncRtsFall.setStatus("mandatory")


class _CxMcPrtCopBitSense_Type(Integer32):
    """Custom type cxMcPrtCopBitSense based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("normal", 1))
    )


_CxMcPrtCopBitSense_Type.__name__ = "Integer32"
_CxMcPrtCopBitSense_Object = MibTableColumn
cxMcPrtCopBitSense = _CxMcPrtCopBitSense_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 3, 1, 34),
    _CxMcPrtCopBitSense_Type()
)
cxMcPrtCopBitSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtCopBitSense.setStatus("mandatory")
_CxMcPrtBsyTable_Object = MibTable
cxMcPrtBsyTable = _CxMcPrtBsyTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    cxMcPrtBsyTable.setStatus("mandatory")
_CxMcPrtBsyEntry_Object = MibTableRow
cxMcPrtBsyEntry = _CxMcPrtBsyEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1)
)
cxMcPrtBsyEntry.setIndexNames(
    (0, "CXMCPRT-MIB", "cxMcPrtBsyPortUsed"),
)
if mibBuilder.loadTexts:
    cxMcPrtBsyEntry.setStatus("mandatory")


class _CxMcPrtBsyPortUsed_Type(Integer32):
    """Custom type cxMcPrtBsyPortUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CxMcPrtBsyPortUsed_Type.__name__ = "Integer32"
_CxMcPrtBsyPortUsed_Object = MibTableColumn
cxMcPrtBsyPortUsed = _CxMcPrtBsyPortUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 1),
    _CxMcPrtBsyPortUsed_Type()
)
cxMcPrtBsyPortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxMcPrtBsyPortUsed.setStatus("mandatory")


class _CxMcPrtBsyPortStatus_Type(Integer32):
    """Custom type cxMcPrtBsyPortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CxMcPrtBsyPortStatus_Type.__name__ = "Integer32"
_CxMcPrtBsyPortStatus_Object = MibTableColumn
cxMcPrtBsyPortStatus = _CxMcPrtBsyPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 2),
    _CxMcPrtBsyPortStatus_Type()
)
cxMcPrtBsyPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyPortStatus.setStatus("mandatory")


class _CxMcPrtBsyComRate_Type(Integer32):
    """Custom type cxMcPrtBsyComRate based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(110, 64000),
    )


_CxMcPrtBsyComRate_Type.__name__ = "Integer32"
_CxMcPrtBsyComRate_Object = MibTableColumn
cxMcPrtBsyComRate = _CxMcPrtBsyComRate_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 3),
    _CxMcPrtBsyComRate_Type()
)
cxMcPrtBsyComRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyComRate.setStatus("mandatory")


class _CxMcPrtBsyUseLnkErrPassthro_Type(Integer32):
    """Custom type cxMcPrtBsyUseLnkErrPassthro based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBsyUseLnkErrPassthro_Type.__name__ = "Integer32"
_CxMcPrtBsyUseLnkErrPassthro_Object = MibTableColumn
cxMcPrtBsyUseLnkErrPassthro = _CxMcPrtBsyUseLnkErrPassthro_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 4),
    _CxMcPrtBsyUseLnkErrPassthro_Type()
)
cxMcPrtBsyUseLnkErrPassthro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyUseLnkErrPassthro.setStatus("mandatory")


class _CxMcPrtBsyInterface_Type(Integer32):
    """Custom type cxMcPrtBsyInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_CxMcPrtBsyInterface_Type.__name__ = "Integer32"
_CxMcPrtBsyInterface_Object = MibTableColumn
cxMcPrtBsyInterface = _CxMcPrtBsyInterface_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 5),
    _CxMcPrtBsyInterface_Type()
)
cxMcPrtBsyInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyInterface.setStatus("mandatory")


class _CxMcPrtBsyRtsDcdModemCtrl_Type(Integer32):
    """Custom type cxMcPrtBsyRtsDcdModemCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("vary", 2))
    )


_CxMcPrtBsyRtsDcdModemCtrl_Type.__name__ = "Integer32"
_CxMcPrtBsyRtsDcdModemCtrl_Object = MibTableColumn
cxMcPrtBsyRtsDcdModemCtrl = _CxMcPrtBsyRtsDcdModemCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 6),
    _CxMcPrtBsyRtsDcdModemCtrl_Type()
)
cxMcPrtBsyRtsDcdModemCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyRtsDcdModemCtrl.setStatus("mandatory")


class _CxMcPrtBsyUseRtsDcdCndDataTx_Type(Integer32):
    """Custom type cxMcPrtBsyUseRtsDcdCndDataTx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBsyUseRtsDcdCndDataTx_Type.__name__ = "Integer32"
_CxMcPrtBsyUseRtsDcdCndDataTx_Object = MibTableColumn
cxMcPrtBsyUseRtsDcdCndDataTx = _CxMcPrtBsyUseRtsDcdCndDataTx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 7),
    _CxMcPrtBsyUseRtsDcdCndDataTx_Type()
)
cxMcPrtBsyUseRtsDcdCndDataTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyUseRtsDcdCndDataTx.setStatus("mandatory")


class _CxMcPrtBsyUseRtsDcdCndLnk_Type(Integer32):
    """Custom type cxMcPrtBsyUseRtsDcdCndLnk based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBsyUseRtsDcdCndLnk_Type.__name__ = "Integer32"
_CxMcPrtBsyUseRtsDcdCndLnk_Object = MibTableColumn
cxMcPrtBsyUseRtsDcdCndLnk = _CxMcPrtBsyUseRtsDcdCndLnk_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 8),
    _CxMcPrtBsyUseRtsDcdCndLnk_Type()
)
cxMcPrtBsyUseRtsDcdCndLnk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyUseRtsDcdCndLnk.setStatus("mandatory")


class _CxMcPrtBsyUseRtsDcdCndRem_Type(Integer32):
    """Custom type cxMcPrtBsyUseRtsDcdCndRem based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBsyUseRtsDcdCndRem_Type.__name__ = "Integer32"
_CxMcPrtBsyUseRtsDcdCndRem_Object = MibTableColumn
cxMcPrtBsyUseRtsDcdCndRem = _CxMcPrtBsyUseRtsDcdCndRem_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 9),
    _CxMcPrtBsyUseRtsDcdCndRem_Type()
)
cxMcPrtBsyUseRtsDcdCndRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyUseRtsDcdCndRem.setStatus("mandatory")


class _CxMcPrtBsyDtrCtsModemCtrl_Type(Integer32):
    """Custom type cxMcPrtBsyDtrCtsModemCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("vary", 2))
    )


_CxMcPrtBsyDtrCtsModemCtrl_Type.__name__ = "Integer32"
_CxMcPrtBsyDtrCtsModemCtrl_Object = MibTableColumn
cxMcPrtBsyDtrCtsModemCtrl = _CxMcPrtBsyDtrCtsModemCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 10),
    _CxMcPrtBsyDtrCtsModemCtrl_Type()
)
cxMcPrtBsyDtrCtsModemCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyDtrCtsModemCtrl.setStatus("mandatory")


class _CxMcPrtBsyUseDtrCtsCndRts_Type(Integer32):
    """Custom type cxMcPrtBsyUseDtrCtsCndRts based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBsyUseDtrCtsCndRts_Type.__name__ = "Integer32"
_CxMcPrtBsyUseDtrCtsCndRts_Object = MibTableColumn
cxMcPrtBsyUseDtrCtsCndRts = _CxMcPrtBsyUseDtrCtsCndRts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 11),
    _CxMcPrtBsyUseDtrCtsCndRts_Type()
)
cxMcPrtBsyUseDtrCtsCndRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyUseDtrCtsCndRts.setStatus("mandatory")


class _CxMcPrtBsyUseDtrCtsCndLnk_Type(Integer32):
    """Custom type cxMcPrtBsyUseDtrCtsCndLnk based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBsyUseDtrCtsCndLnk_Type.__name__ = "Integer32"
_CxMcPrtBsyUseDtrCtsCndLnk_Object = MibTableColumn
cxMcPrtBsyUseDtrCtsCndLnk = _CxMcPrtBsyUseDtrCtsCndLnk_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 12),
    _CxMcPrtBsyUseDtrCtsCndLnk_Type()
)
cxMcPrtBsyUseDtrCtsCndLnk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyUseDtrCtsCndLnk.setStatus("mandatory")


class _CxMcPrtBsyUseDtrCtsCndRem_Type(Integer32):
    """Custom type cxMcPrtBsyUseDtrCtsCndRem based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBsyUseDtrCtsCndRem_Type.__name__ = "Integer32"
_CxMcPrtBsyUseDtrCtsCndRem_Object = MibTableColumn
cxMcPrtBsyUseDtrCtsCndRem = _CxMcPrtBsyUseDtrCtsCndRem_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 13),
    _CxMcPrtBsyUseDtrCtsCndRem_Type()
)
cxMcPrtBsyUseDtrCtsCndRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyUseDtrCtsCndRem.setStatus("mandatory")


class _CxMcPrtBsyLimitBeforeOut_Type(Integer32):
    """Custom type cxMcPrtBsyLimitBeforeOut based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 4000),
    )


_CxMcPrtBsyLimitBeforeOut_Type.__name__ = "Integer32"
_CxMcPrtBsyLimitBeforeOut_Object = MibTableColumn
cxMcPrtBsyLimitBeforeOut = _CxMcPrtBsyLimitBeforeOut_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 14),
    _CxMcPrtBsyLimitBeforeOut_Type()
)
cxMcPrtBsyLimitBeforeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyLimitBeforeOut.setStatus("mandatory")


class _CxMcPrtBsyUseOutCndCtsDtrOn_Type(Integer32):
    """Custom type cxMcPrtBsyUseOutCndCtsDtrOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBsyUseOutCndCtsDtrOn_Type.__name__ = "Integer32"
_CxMcPrtBsyUseOutCndCtsDtrOn_Object = MibTableColumn
cxMcPrtBsyUseOutCndCtsDtrOn = _CxMcPrtBsyUseOutCndCtsDtrOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 15),
    _CxMcPrtBsyUseOutCndCtsDtrOn_Type()
)
cxMcPrtBsyUseOutCndCtsDtrOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyUseOutCndCtsDtrOn.setStatus("mandatory")


class _CxMcPrtBsyUseInCndDcdRtsOn_Type(Integer32):
    """Custom type cxMcPrtBsyUseInCndDcdRtsOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxMcPrtBsyUseInCndDcdRtsOn_Type.__name__ = "Integer32"
_CxMcPrtBsyUseInCndDcdRtsOn_Object = MibTableColumn
cxMcPrtBsyUseInCndDcdRtsOn = _CxMcPrtBsyUseInCndDcdRtsOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 16),
    _CxMcPrtBsyUseInCndDcdRtsOn_Type()
)
cxMcPrtBsyUseInCndDcdRtsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyUseInCndDcdRtsOn.setStatus("mandatory")


class _CxMcPrtBsySyncMode_Type(Integer32):
    """Custom type cxMcPrtBsySyncMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extern", 2),
          ("normal", 1))
    )


_CxMcPrtBsySyncMode_Type.__name__ = "Integer32"
_CxMcPrtBsySyncMode_Object = MibTableColumn
cxMcPrtBsySyncMode = _CxMcPrtBsySyncMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 17),
    _CxMcPrtBsySyncMode_Type()
)
cxMcPrtBsySyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsySyncMode.setStatus("mandatory")


class _CxMcPrtBsyDataLifetime_Type(Integer32):
    """Custom type cxMcPrtBsyDataLifetime based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_CxMcPrtBsyDataLifetime_Type.__name__ = "Integer32"
_CxMcPrtBsyDataLifetime_Object = MibTableColumn
cxMcPrtBsyDataLifetime = _CxMcPrtBsyDataLifetime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 18),
    _CxMcPrtBsyDataLifetime_Type()
)
cxMcPrtBsyDataLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyDataLifetime.setStatus("mandatory")


class _CxMcPrtBsyChrSet_Type(Integer32):
    """Custom type cxMcPrtBsyChrSet based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ebcdic", 1),
          ("trans", 3),
          ("usaascii", 2))
    )


_CxMcPrtBsyChrSet_Type.__name__ = "Integer32"
_CxMcPrtBsyChrSet_Object = MibTableColumn
cxMcPrtBsyChrSet = _CxMcPrtBsyChrSet_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 19),
    _CxMcPrtBsyChrSet_Type()
)
cxMcPrtBsyChrSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyChrSet.setStatus("mandatory")


class _CxMcPrtBsyParity_Type(Integer32):
    """Custom type cxMcPrtBsyParity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 1),
          ("odd", 3))
    )


_CxMcPrtBsyParity_Type.__name__ = "Integer32"
_CxMcPrtBsyParity_Object = MibTableColumn
cxMcPrtBsyParity = _CxMcPrtBsyParity_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 20),
    _CxMcPrtBsyParity_Type()
)
cxMcPrtBsyParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyParity.setStatus("mandatory")


class _CxMcPrtBsyBlkChkChr_Type(Integer32):
    """Custom type cxMcPrtBsyBlkChkChr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc", 1),
          ("lrc", 2))
    )


_CxMcPrtBsyBlkChkChr_Type.__name__ = "Integer32"
_CxMcPrtBsyBlkChkChr_Object = MibTableColumn
cxMcPrtBsyBlkChkChr = _CxMcPrtBsyBlkChkChr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 21),
    _CxMcPrtBsyBlkChkChr_Type()
)
cxMcPrtBsyBlkChkChr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyBlkChkChr.setStatus("mandatory")


class _CxMcPrtBsyNbSyncChr_Type(Integer32):
    """Custom type cxMcPrtBsyNbSyncChr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_CxMcPrtBsyNbSyncChr_Type.__name__ = "Integer32"
_CxMcPrtBsyNbSyncChr_Object = MibTableColumn
cxMcPrtBsyNbSyncChr = _CxMcPrtBsyNbSyncChr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 22),
    _CxMcPrtBsyNbSyncChr_Type()
)
cxMcPrtBsyNbSyncChr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyNbSyncChr.setStatus("mandatory")


class _CxMcPrtBsyMaxFrameSize_Type(Integer32):
    """Custom type cxMcPrtBsyMaxFrameSize based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_CxMcPrtBsyMaxFrameSize_Type.__name__ = "Integer32"
_CxMcPrtBsyMaxFrameSize_Object = MibTableColumn
cxMcPrtBsyMaxFrameSize = _CxMcPrtBsyMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 1, 5, 4, 1, 23),
    _CxMcPrtBsyMaxFrameSize_Type()
)
cxMcPrtBsyMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxMcPrtBsyMaxFrameSize.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXMCPRT-MIB",
    **{"cxMcPrt": cxMcPrt,
       "cxMcPrtGlobal": cxMcPrtGlobal,
       "cxMcPrtGlobalConsoleRate": cxMcPrtGlobalConsoleRate,
       "cxMcPrtGlobalResetStat": cxMcPrtGlobalResetStat,
       "cxMcPrtGlobalStationId": cxMcPrtGlobalStationId,
       "cxMcPrtCfgTable": cxMcPrtCfgTable,
       "cxMcPrtCfgEntry": cxMcPrtCfgEntry,
       "cxMcPrtCfgPortIndex": cxMcPrtCfgPortIndex,
       "cxMcPrtCfgDriverUsed": cxMcPrtCfgDriverUsed,
       "cxMcPrtCfgReinitPort": cxMcPrtCfgReinitPort,
       "cxMcPrtCfgUpdated": cxMcPrtCfgUpdated,
       "cxMcPrtStatTable": cxMcPrtStatTable,
       "cxMcPrtStatEntry": cxMcPrtStatEntry,
       "cxMcPrtStatPortNumber": cxMcPrtStatPortNumber,
       "cxMcPrtStatRts": cxMcPrtStatRts,
       "cxMcPrtStatDtr": cxMcPrtStatDtr,
       "cxMcPrtStatDsr": cxMcPrtStatDsr,
       "cxMcPrtStatDcd": cxMcPrtStatDcd,
       "cxMcPrtStatCts": cxMcPrtStatCts,
       "cxMcPrtStatCntMsgTx": cxMcPrtStatCntMsgTx,
       "cxMcPrtStatCntMsgRx": cxMcPrtStatCntMsgRx,
       "cxMcPrtStatCntReinit": cxMcPrtStatCntReinit,
       "cxMcPrtStatCntFlowCtrlTx": cxMcPrtStatCntFlowCtrlTx,
       "cxMcPrtStatCntFlowCtrlRx": cxMcPrtStatCntFlowCtrlRx,
       "cxMcPrtStatCntErrTx": cxMcPrtStatCntErrTx,
       "cxMcPrtStatCntErrRx": cxMcPrtStatCntErrRx,
       "cxMcPrtStatCntConnect": cxMcPrtStatCntConnect,
       "cxMcPrtStatCntChrDecomp": cxMcPrtStatCntChrDecomp,
       "cxMcPrtStatCntChrComp": cxMcPrtStatCntChrComp,
       "cxMcPrtStatCntBitDecomp": cxMcPrtStatCntBitDecomp,
       "cxMcPrtStatCntBitComp": cxMcPrtStatCntBitComp,
       "cxMcPrtStatStation": cxMcPrtStatStation,
       "cxMcPrtStatRoute": cxMcPrtStatRoute,
       "cxMcPrtStatHwInterface": cxMcPrtStatHwInterface,
       "cxMcPrtStatTimeTicks": cxMcPrtStatTimeTicks,
       "cxMcPrtPath": cxMcPrtPath,
       "cxMcPrtPathStationPri": cxMcPrtPathStationPri,
       "cxMcPrtPathRoutePri": cxMcPrtPathRoutePri,
       "cxMcPrtPathStationScd": cxMcPrtPathStationScd,
       "cxMcPrtPathRouteScd": cxMcPrtPathRouteScd,
       "cxMcPrtDriver": cxMcPrtDriver,
       "cxMcPrtBopTable": cxMcPrtBopTable,
       "cxMcPrtBopEntry": cxMcPrtBopEntry,
       "cxMcPrtBopPortUsed": cxMcPrtBopPortUsed,
       "cxMcPrtBopPortStatus": cxMcPrtBopPortStatus,
       "cxMcPrtBopComRate": cxMcPrtBopComRate,
       "cxMcPrtBopUseLnkErrPassthro": cxMcPrtBopUseLnkErrPassthro,
       "cxMcPrtBopInterface": cxMcPrtBopInterface,
       "cxMcPrtBopRtsDcdModemCtrl": cxMcPrtBopRtsDcdModemCtrl,
       "cxMcPrtBopUseRtsDcdCndDataTx": cxMcPrtBopUseRtsDcdCndDataTx,
       "cxMcPrtBopUseRtsDcdCndLnk": cxMcPrtBopUseRtsDcdCndLnk,
       "cxMcPrtBopUseRtsDcdCndRem": cxMcPrtBopUseRtsDcdCndRem,
       "cxMcPrtBopDtrCtsModemCtrl": cxMcPrtBopDtrCtsModemCtrl,
       "cxMcPrtBopUseDtrCtsCndRts": cxMcPrtBopUseDtrCtsCndRts,
       "cxMcPrtBopUseDtrCtsCndLnk": cxMcPrtBopUseDtrCtsCndLnk,
       "cxMcPrtBopUseDtrCtsCndRem": cxMcPrtBopUseDtrCtsCndRem,
       "cxMcPrtBopLimitBeforeOut": cxMcPrtBopLimitBeforeOut,
       "cxMcPrtBopUseOutCndCtsDtrOn": cxMcPrtBopUseOutCndCtsDtrOn,
       "cxMcPrtBopUseInCndDcdRtsOn": cxMcPrtBopUseInCndDcdRtsOn,
       "cxMcPrtBopSyncMode": cxMcPrtBopSyncMode,
       "cxMcPrtBopDataLifetime": cxMcPrtBopDataLifetime,
       "cxMcPrtBopUseClockSync": cxMcPrtBopUseClockSync,
       "cxMcPrtBopUseFlowCtrlClock": cxMcPrtBopUseFlowCtrlClock,
       "cxMcPrtBopFlowCtrlRate": cxMcPrtBopFlowCtrlRate,
       "cxMcPrtBopLimitOutFlowCtrl": cxMcPrtBopLimitOutFlowCtrl,
       "cxMcPrtBopLimitInFlowCtrl": cxMcPrtBopLimitInFlowCtrl,
       "cxMcPrtBopCoding": cxMcPrtBopCoding,
       "cxMcPrtBopOutIdleState": cxMcPrtBopOutIdleState,
       "cxMcPrtBopDelayBeforeIdle": cxMcPrtBopDelayBeforeIdle,
       "cxMcPrtBopOutPreambleLng": cxMcPrtBopOutPreambleLng,
       "cxMcPrtAsyTable": cxMcPrtAsyTable,
       "cxMcPrtAsyEntry": cxMcPrtAsyEntry,
       "cxMcPrtAsyPortUsed": cxMcPrtAsyPortUsed,
       "cxMcPrtAsyPortStatus": cxMcPrtAsyPortStatus,
       "cxMcPrtAsyComRate": cxMcPrtAsyComRate,
       "cxMcPrtAsyUseLnkErrPassthro": cxMcPrtAsyUseLnkErrPassthro,
       "cxMcPrtAsyInterface": cxMcPrtAsyInterface,
       "cxMcPrtAsyRtsDcdModemCtrl": cxMcPrtAsyRtsDcdModemCtrl,
       "cxMcPrtAsyUseRtsDcdCndDataTx": cxMcPrtAsyUseRtsDcdCndDataTx,
       "cxMcPrtAsyUseRtsDcdCndLnk": cxMcPrtAsyUseRtsDcdCndLnk,
       "cxMcPrtAsyUseRtsDcdCndRem": cxMcPrtAsyUseRtsDcdCndRem,
       "cxMcPrtAsyDtrCtsModemCtrl": cxMcPrtAsyDtrCtsModemCtrl,
       "cxMcPrtAsyUseDtrCtsCndRts": cxMcPrtAsyUseDtrCtsCndRts,
       "cxMcPrtAsyUseDtrCtsCndLnk": cxMcPrtAsyUseDtrCtsCndLnk,
       "cxMcPrtAsyUseDtrCtsCndRem": cxMcPrtAsyUseDtrCtsCndRem,
       "cxMcPrtAsyLimitBeforeOut": cxMcPrtAsyLimitBeforeOut,
       "cxMcPrtAsyOutCndCtsDtrOn": cxMcPrtAsyOutCndCtsDtrOn,
       "cxMcPrtAsyInCndDcdRtsOn": cxMcPrtAsyInCndDcdRtsOn,
       "cxMcPrtAsySyncMode": cxMcPrtAsySyncMode,
       "cxMcPrtAsyUseDataLifeLimited": cxMcPrtAsyUseDataLifeLimited,
       "cxMcPrtAsyDataLifetime": cxMcPrtAsyDataLifetime,
       "cxMcPrtAsyOutFlowCtrl": cxMcPrtAsyOutFlowCtrl,
       "cxMcPrtAsyInFlowCtrl": cxMcPrtAsyInFlowCtrl,
       "cxMcPrtAsyXonChr": cxMcPrtAsyXonChr,
       "cxMcPrtAsyXoffChr": cxMcPrtAsyXoffChr,
       "cxMcPrtAsyNbBitPerChr": cxMcPrtAsyNbBitPerChr,
       "cxMcPrtAsyParity": cxMcPrtAsyParity,
       "cxMcPrtAsyNbStopBit": cxMcPrtAsyNbStopBit,
       "cxMcPrtAsyUseFlushOutChr": cxMcPrtAsyUseFlushOutChr,
       "cxMcPrtAsyFlushOutChr": cxMcPrtAsyFlushOutChr,
       "cxMcPrtCopTable": cxMcPrtCopTable,
       "cxMcPrtCopEntry": cxMcPrtCopEntry,
       "cxMcPrtCopPortUsed": cxMcPrtCopPortUsed,
       "cxMcPrtCopPortStatus": cxMcPrtCopPortStatus,
       "cxMcPrtCopComRate": cxMcPrtCopComRate,
       "cxMcPrtCopUseLnkErrPassthro": cxMcPrtCopUseLnkErrPassthro,
       "cxMcPrtCopInterfaceType": cxMcPrtCopInterfaceType,
       "cxMcPrtCopRtsDcdModemCtrl": cxMcPrtCopRtsDcdModemCtrl,
       "cxMcPrtCopUseRtsDcdCndDataTx": cxMcPrtCopUseRtsDcdCndDataTx,
       "cxMcPrtCopUseRtsDcdCndLnk": cxMcPrtCopUseRtsDcdCndLnk,
       "cxMcPrtCopUseRtsDcdCndRem": cxMcPrtCopUseRtsDcdCndRem,
       "cxMcPrtCopDtrCtsModemCtrl": cxMcPrtCopDtrCtsModemCtrl,
       "cxMcPrtCopUseDtrCtsCndRts": cxMcPrtCopUseDtrCtsCndRts,
       "cxMcPrtCopUseDtrCtsCndLnk": cxMcPrtCopUseDtrCtsCndLnk,
       "cxMcPrtCopUseDtrCtsCndRem": cxMcPrtCopUseDtrCtsCndRem,
       "cxMcPrtCopLimitBeforeOut": cxMcPrtCopLimitBeforeOut,
       "cxMcPrtCopUseOutCndCtsDtrOn": cxMcPrtCopUseOutCndCtsDtrOn,
       "cxMcPrtCopUseInCndDcdRtsOn": cxMcPrtCopUseInCndDcdRtsOn,
       "cxMcPrtCopSyncMode": cxMcPrtCopSyncMode,
       "cxMcPrtCopDataLifetime": cxMcPrtCopDataLifetime,
       "cxMcPrtCopUseClockSync": cxMcPrtCopUseClockSync,
       "cxMcPrtCopUseFlowCtrlClock": cxMcPrtCopUseFlowCtrlClock,
       "cxMcPrtCopFlowCtrlRate": cxMcPrtCopFlowCtrlRate,
       "cxMcPrtCopLimitOutFlowCtrl": cxMcPrtCopLimitOutFlowCtrl,
       "cxMcPrtCopLimitInFlowCtrl": cxMcPrtCopLimitInFlowCtrl,
       "cxMcPrtCopOutIdleState": cxMcPrtCopOutIdleState,
       "cxMcPrtCopNbBitPerChr": cxMcPrtCopNbBitPerChr,
       "cxMcPrtCopParity": cxMcPrtCopParity,
       "cxMcPrtCopSyncChrOne": cxMcPrtCopSyncChrOne,
       "cxMcPrtCopSyncChrTwo": cxMcPrtCopSyncChrTwo,
       "cxMcPrtCopNbSyncChr": cxMcPrtCopNbSyncChr,
       "cxMcPrtCopUseDesyncChr": cxMcPrtCopUseDesyncChr,
       "cxMcPrtCopDesyncChr": cxMcPrtCopDesyncChr,
       "cxMcPrtCopNbDesyncChr": cxMcPrtCopNbDesyncChr,
       "cxMcPrtCopUseDesyncRtsFall": cxMcPrtCopUseDesyncRtsFall,
       "cxMcPrtCopBitSense": cxMcPrtCopBitSense,
       "cxMcPrtBsyTable": cxMcPrtBsyTable,
       "cxMcPrtBsyEntry": cxMcPrtBsyEntry,
       "cxMcPrtBsyPortUsed": cxMcPrtBsyPortUsed,
       "cxMcPrtBsyPortStatus": cxMcPrtBsyPortStatus,
       "cxMcPrtBsyComRate": cxMcPrtBsyComRate,
       "cxMcPrtBsyUseLnkErrPassthro": cxMcPrtBsyUseLnkErrPassthro,
       "cxMcPrtBsyInterface": cxMcPrtBsyInterface,
       "cxMcPrtBsyRtsDcdModemCtrl": cxMcPrtBsyRtsDcdModemCtrl,
       "cxMcPrtBsyUseRtsDcdCndDataTx": cxMcPrtBsyUseRtsDcdCndDataTx,
       "cxMcPrtBsyUseRtsDcdCndLnk": cxMcPrtBsyUseRtsDcdCndLnk,
       "cxMcPrtBsyUseRtsDcdCndRem": cxMcPrtBsyUseRtsDcdCndRem,
       "cxMcPrtBsyDtrCtsModemCtrl": cxMcPrtBsyDtrCtsModemCtrl,
       "cxMcPrtBsyUseDtrCtsCndRts": cxMcPrtBsyUseDtrCtsCndRts,
       "cxMcPrtBsyUseDtrCtsCndLnk": cxMcPrtBsyUseDtrCtsCndLnk,
       "cxMcPrtBsyUseDtrCtsCndRem": cxMcPrtBsyUseDtrCtsCndRem,
       "cxMcPrtBsyLimitBeforeOut": cxMcPrtBsyLimitBeforeOut,
       "cxMcPrtBsyUseOutCndCtsDtrOn": cxMcPrtBsyUseOutCndCtsDtrOn,
       "cxMcPrtBsyUseInCndDcdRtsOn": cxMcPrtBsyUseInCndDcdRtsOn,
       "cxMcPrtBsySyncMode": cxMcPrtBsySyncMode,
       "cxMcPrtBsyDataLifetime": cxMcPrtBsyDataLifetime,
       "cxMcPrtBsyChrSet": cxMcPrtBsyChrSet,
       "cxMcPrtBsyParity": cxMcPrtBsyParity,
       "cxMcPrtBsyBlkChkChr": cxMcPrtBsyBlkChkChr,
       "cxMcPrtBsyNbSyncChr": cxMcPrtBsyNbSyncChr,
       "cxMcPrtBsyMaxFrameSize": cxMcPrtBsyMaxFrameSize}
)
