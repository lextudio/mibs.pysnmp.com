# SNMP MIB module (NMS520-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS520-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:08 2024
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

(dsu,) = mibBuilder.importSymbols(
    "DDS-MIB",
    "dsu")

(gdc,) = mibBuilder.importSymbols(
    "GDCCMN-MIB",
    "gdc")

(SCinstance,) = mibBuilder.importSymbols(
    "GDCMACRO-MIB",
    "SCinstance")

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

_Nms520_ObjectIdentity = ObjectIdentity
nms520 = _Nms520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2)
)


class _Nms520MIBversion_Type(DisplayString):
    """Custom type nms520MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Nms520MIBversion_Type.__name__ = "DisplayString"
_Nms520MIBversion_Object = MibScalar
nms520MIBversion = _Nms520MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 1),
    _Nms520MIBversion_Type()
)
nms520MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520MIBversion.setStatus("mandatory")
_Nms520UnitCfgTable_Object = MibTable
nms520UnitCfgTable = _Nms520UnitCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2)
)
if mibBuilder.loadTexts:
    nms520UnitCfgTable.setStatus("mandatory")
_Nms520UnitCfgEntry_Object = MibTableRow
nms520UnitCfgEntry = _Nms520UnitCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1)
)
nms520UnitCfgEntry.setIndexNames(
    (0, "NMS520-MIB", "nms520UnitCfgIndex"),
)
if mibBuilder.loadTexts:
    nms520UnitCfgEntry.setStatus("mandatory")
_Nms520UnitCfgIndex_Type = SCinstance
_Nms520UnitCfgIndex_Object = MibTableColumn
nms520UnitCfgIndex = _Nms520UnitCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 1),
    _Nms520UnitCfgIndex_Type()
)
nms520UnitCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520UnitCfgIndex.setStatus("mandatory")


class _Nms520Nms510CompatibilityMode_Type(Integer32):
    """Custom type nms520Nms510CompatibilityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Nms520Nms510CompatibilityMode_Type.__name__ = "Integer32"
_Nms520Nms510CompatibilityMode_Object = MibTableColumn
nms520Nms510CompatibilityMode = _Nms520Nms510CompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 2),
    _Nms520Nms510CompatibilityMode_Type()
)
nms520Nms510CompatibilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520Nms510CompatibilityMode.setStatus("mandatory")


class _Nms520PtToPtSentryTime_Type(Integer32):
    """Custom type nms520PtToPtSentryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Nms520PtToPtSentryTime_Type.__name__ = "Integer32"
_Nms520PtToPtSentryTime_Object = MibTableColumn
nms520PtToPtSentryTime = _Nms520PtToPtSentryTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 3),
    _Nms520PtToPtSentryTime_Type()
)
nms520PtToPtSentryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520PtToPtSentryTime.setStatus("mandatory")


class _Nms520AlarmHystTime_Type(Integer32):
    """Custom type nms520AlarmHystTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Nms520AlarmHystTime_Type.__name__ = "Integer32"
_Nms520AlarmHystTime_Object = MibTableColumn
nms520AlarmHystTime = _Nms520AlarmHystTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 4),
    _Nms520AlarmHystTime_Type()
)
nms520AlarmHystTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520AlarmHystTime.setStatus("mandatory")


class _Nms520MtpointRmRspIntrvl_Type(Integer32):
    """Custom type nms520MtpointRmRspIntrvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Nms520MtpointRmRspIntrvl_Type.__name__ = "Integer32"
_Nms520MtpointRmRspIntrvl_Object = MibTableColumn
nms520MtpointRmRspIntrvl = _Nms520MtpointRmRspIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 5),
    _Nms520MtpointRmRspIntrvl_Type()
)
nms520MtpointRmRspIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520MtpointRmRspIntrvl.setStatus("mandatory")


class _Nms520DtePortType_Type(Integer32):
    """Custom type nms520DtePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("rs232", 1),
          ("v35", 2))
    )


_Nms520DtePortType_Type.__name__ = "Integer32"
_Nms520DtePortType_Object = MibTableColumn
nms520DtePortType = _Nms520DtePortType_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 6),
    _Nms520DtePortType_Type()
)
nms520DtePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520DtePortType.setStatus("mandatory")


class _Nms520DteCtsDelay_Type(Integer32):
    """Custom type nms520DteCtsDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cts0mSec", 2),
          ("ctsFixed3Char", 3),
          ("ctsOn", 1))
    )


_Nms520DteCtsDelay_Type.__name__ = "Integer32"
_Nms520DteCtsDelay_Object = MibTableColumn
nms520DteCtsDelay = _Nms520DteCtsDelay_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 7),
    _Nms520DteCtsDelay_Type()
)
nms520DteCtsDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520DteCtsDelay.setStatus("mandatory")


class _Nms520DteCtsDelayExt_Type(Integer32):
    """Custom type nms520DteCtsDelayExt based on Integer32"""
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
        *(("ext0mSec", 1),
          ("ext30mSec", 2),
          ("ext60mSec", 3),
          ("ext90mSec", 4))
    )


_Nms520DteCtsDelayExt_Type.__name__ = "Integer32"
_Nms520DteCtsDelayExt_Object = MibTableColumn
nms520DteCtsDelayExt = _Nms520DteCtsDelayExt_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 8),
    _Nms520DteCtsDelayExt_Type()
)
nms520DteCtsDelayExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520DteCtsDelayExt.setStatus("mandatory")


class _Nms520FirmwareLevel_Type(DisplayString):
    """Custom type nms520FirmwareLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Nms520FirmwareLevel_Type.__name__ = "DisplayString"
_Nms520FirmwareLevel_Object = MibTableColumn
nms520FirmwareLevel = _Nms520FirmwareLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 9),
    _Nms520FirmwareLevel_Type()
)
nms520FirmwareLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520FirmwareLevel.setStatus("mandatory")


class _Nms520DaisyChainBps_Type(Integer32):
    """Custom type nms520DaisyChainBps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bps75", 1),
          ("bps9600", 2))
    )


_Nms520DaisyChainBps_Type.__name__ = "Integer32"
_Nms520DaisyChainBps_Object = MibTableColumn
nms520DaisyChainBps = _Nms520DaisyChainBps_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 10),
    _Nms520DaisyChainBps_Type()
)
nms520DaisyChainBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520DaisyChainBps.setStatus("mandatory")


class _Nms520AlarmCfgCountWindow_Type(Integer32):
    """Custom type nms520AlarmCfgCountWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Nms520AlarmCfgCountWindow_Type.__name__ = "Integer32"
_Nms520AlarmCfgCountWindow_Object = MibTableColumn
nms520AlarmCfgCountWindow = _Nms520AlarmCfgCountWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 11),
    _Nms520AlarmCfgCountWindow_Type()
)
nms520AlarmCfgCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520AlarmCfgCountWindow.setStatus("mandatory")


class _Nms520SoftReset_Type(Integer32):
    """Custom type nms520SoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_Nms520SoftReset_Type.__name__ = "Integer32"
_Nms520SoftReset_Object = MibTableColumn
nms520SoftReset = _Nms520SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 12),
    _Nms520SoftReset_Type()
)
nms520SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520SoftReset.setStatus("mandatory")


class _Nms520FrontPanelInhibit_Type(Integer32):
    """Custom type nms520FrontPanelInhibit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("execute", 3),
          ("fpEnabled", 2),
          ("fpInhibited", 1))
    )


_Nms520FrontPanelInhibit_Type.__name__ = "Integer32"
_Nms520FrontPanelInhibit_Object = MibTableColumn
nms520FrontPanelInhibit = _Nms520FrontPanelInhibit_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 13),
    _Nms520FrontPanelInhibit_Type()
)
nms520FrontPanelInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520FrontPanelInhibit.setStatus("mandatory")


class _Nms520FrontPanelEnable_Type(Integer32):
    """Custom type nms520FrontPanelEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("execute", 3),
          ("fpEnabled", 2),
          ("fpInhibited", 1))
    )


_Nms520FrontPanelEnable_Type.__name__ = "Integer32"
_Nms520FrontPanelEnable_Object = MibTableColumn
nms520FrontPanelEnable = _Nms520FrontPanelEnable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 14),
    _Nms520FrontPanelEnable_Type()
)
nms520FrontPanelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520FrontPanelEnable.setStatus("mandatory")


class _Nms520HdlcInvert_Type(Integer32):
    """Custom type nms520HdlcInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invert", 2),
          ("normal", 1))
    )


_Nms520HdlcInvert_Type.__name__ = "Integer32"
_Nms520HdlcInvert_Object = MibTableColumn
nms520HdlcInvert = _Nms520HdlcInvert_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 15),
    _Nms520HdlcInvert_Type()
)
nms520HdlcInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520HdlcInvert.setStatus("mandatory")


class _Nms520PiggyBackDetect_Type(Integer32):
    """Custom type nms520PiggyBackDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("not-installed", 1))
    )


_Nms520PiggyBackDetect_Type.__name__ = "Integer32"
_Nms520PiggyBackDetect_Object = MibTableColumn
nms520PiggyBackDetect = _Nms520PiggyBackDetect_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 16),
    _Nms520PiggyBackDetect_Type()
)
nms520PiggyBackDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520PiggyBackDetect.setStatus("mandatory")


class _Nms520UnitType_Type(Integer32):
    """Custom type nms520UnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleHeight", 1),
          ("withIFP", 2))
    )


_Nms520UnitType_Type.__name__ = "Integer32"
_Nms520UnitType_Object = MibTableColumn
nms520UnitType = _Nms520UnitType_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 17),
    _Nms520UnitType_Type()
)
nms520UnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520UnitType.setStatus("mandatory")


class _Nms520ExtPortCtrlOut1_Type(Integer32):
    """Custom type nms520ExtPortCtrlOut1 based on Integer32"""
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


_Nms520ExtPortCtrlOut1_Type.__name__ = "Integer32"
_Nms520ExtPortCtrlOut1_Object = MibTableColumn
nms520ExtPortCtrlOut1 = _Nms520ExtPortCtrlOut1_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 18),
    _Nms520ExtPortCtrlOut1_Type()
)
nms520ExtPortCtrlOut1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520ExtPortCtrlOut1.setStatus("mandatory")


class _Nms520ExtPortCtrlOut2_Type(Integer32):
    """Custom type nms520ExtPortCtrlOut2 based on Integer32"""
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


_Nms520ExtPortCtrlOut2_Type.__name__ = "Integer32"
_Nms520ExtPortCtrlOut2_Object = MibTableColumn
nms520ExtPortCtrlOut2 = _Nms520ExtPortCtrlOut2_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 2, 1, 19),
    _Nms520ExtPortCtrlOut2_Type()
)
nms520ExtPortCtrlOut2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520ExtPortCtrlOut2.setStatus("mandatory")
_Nms520AlarmData_ObjectIdentity = ObjectIdentity
nms520AlarmData = _Nms520AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4)
)
_Nms520NoResponseAlm_ObjectIdentity = ObjectIdentity
nms520NoResponseAlm = _Nms520NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 1)
)
_Nms520DiagRxErrAlm_ObjectIdentity = ObjectIdentity
nms520DiagRxErrAlm = _Nms520DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 2)
)
_Nms520PowerUpAlm_ObjectIdentity = ObjectIdentity
nms520PowerUpAlm = _Nms520PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 3)
)
_Nms520EEChkSumErrAlm_ObjectIdentity = ObjectIdentity
nms520EEChkSumErrAlm = _Nms520EEChkSumErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 4)
)
_Nms520StcLoopbackAlm_ObjectIdentity = ObjectIdentity
nms520StcLoopbackAlm = _Nms520StcLoopbackAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 5)
)
_Nms520NoNtwkLoopCurrentAlm_ObjectIdentity = ObjectIdentity
nms520NoNtwkLoopCurrentAlm = _Nms520NoNtwkLoopCurrentAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 6)
)
_Nms520LinePairsReversedAlm_ObjectIdentity = ObjectIdentity
nms520LinePairsReversedAlm = _Nms520LinePairsReversedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 7)
)
_Nms520NoSignalAlm_ObjectIdentity = ObjectIdentity
nms520NoSignalAlm = _Nms520NoSignalAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 8)
)
_Nms520FpTestAlm_ObjectIdentity = ObjectIdentity
nms520FpTestAlm = _Nms520FpTestAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 9)
)
_Nms520StreamingAlm_ObjectIdentity = ObjectIdentity
nms520StreamingAlm = _Nms520StreamingAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 10)
)
_Nms520DSRLossAlm_ObjectIdentity = ObjectIdentity
nms520DSRLossAlm = _Nms520DSRLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 11)
)
_Nms520DTRLossAlm_ObjectIdentity = ObjectIdentity
nms520DTRLossAlm = _Nms520DTRLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 12)
)
_Nms520DTPLossAlm_ObjectIdentity = ObjectIdentity
nms520DTPLossAlm = _Nms520DTPLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 13)
)
_Nms520DCDLossAlm_ObjectIdentity = ObjectIdentity
nms520DCDLossAlm = _Nms520DCDLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 14)
)
_Nms520RXDLossAlm_ObjectIdentity = ObjectIdentity
nms520RXDLossAlm = _Nms520RXDLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 15)
)
_Nms520TXDLossAlm_ObjectIdentity = ObjectIdentity
nms520TXDLossAlm = _Nms520TXDLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 16)
)
_Nms520TmShortedAlm_ObjectIdentity = ObjectIdentity
nms520TmShortedAlm = _Nms520TmShortedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 17)
)
_Nms520DcdShortedAlm_ObjectIdentity = ObjectIdentity
nms520DcdShortedAlm = _Nms520DcdShortedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 18)
)
_Nms520DsrShortedAlm_ObjectIdentity = ObjectIdentity
nms520DsrShortedAlm = _Nms520DsrShortedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 19)
)
_Nms520CtsShortedAlm_ObjectIdentity = ObjectIdentity
nms520CtsShortedAlm = _Nms520CtsShortedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 20)
)
_Nms520RxdShortedAlm_ObjectIdentity = ObjectIdentity
nms520RxdShortedAlm = _Nms520RxdShortedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 21)
)
_Nms520RxcShortedAlm_ObjectIdentity = ObjectIdentity
nms520RxcShortedAlm = _Nms520RxcShortedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 22)
)
_Nms520TxcShortedAlm_ObjectIdentity = ObjectIdentity
nms520TxcShortedAlm = _Nms520TxcShortedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 23)
)
_Nms520DBURequestForScanAlm_ObjectIdentity = ObjectIdentity
nms520DBURequestForScanAlm = _Nms520DBURequestForScanAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 24)
)
_Nms520DBUOnalm_ObjectIdentity = ObjectIdentity
nms520DBUOnalm = _Nms520DBUOnalm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 25)
)
_Nms520DBUFailedAlm_ObjectIdentity = ObjectIdentity
nms520DBUFailedAlm = _Nms520DBUFailedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 26)
)
_Nms520NoDSUResponseAlm_ObjectIdentity = ObjectIdentity
nms520NoDSUResponseAlm = _Nms520NoDSUResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 27)
)
_Nms520NoDTEPollingAlm_ObjectIdentity = ObjectIdentity
nms520NoDTEPollingAlm = _Nms520NoDTEPollingAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 28)
)
_Nms520JitterAlm_ObjectIdentity = ObjectIdentity
nms520JitterAlm = _Nms520JitterAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 29)
)
_Nms520BpvAlm_ObjectIdentity = ObjectIdentity
nms520BpvAlm = _Nms520BpvAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 30)
)
_Nms520FrameLossAlm_ObjectIdentity = ObjectIdentity
nms520FrameLossAlm = _Nms520FrameLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 31)
)
_Nms520SignalToNoiseAlm_ObjectIdentity = ObjectIdentity
nms520SignalToNoiseAlm = _Nms520SignalToNoiseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 32)
)
_Nms520RxSignalLowAlm_ObjectIdentity = ObjectIdentity
nms520RxSignalLowAlm = _Nms520RxSignalLowAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 33)
)
_Nms520ExtInputChangeAlm_ObjectIdentity = ObjectIdentity
nms520ExtInputChangeAlm = _Nms520ExtInputChangeAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 34)
)
_Nms520ExtInputLowAlm_ObjectIdentity = ObjectIdentity
nms520ExtInputLowAlm = _Nms520ExtInputLowAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 4, 35)
)
_Nms520LineStatsTable_Object = MibTable
nms520LineStatsTable = _Nms520LineStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 5)
)
if mibBuilder.loadTexts:
    nms520LineStatsTable.setStatus("mandatory")
_Nms520LineStatsEntry_Object = MibTableRow
nms520LineStatsEntry = _Nms520LineStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 5, 1)
)
nms520LineStatsEntry.setIndexNames(
    (0, "NMS520-MIB", "nms520LineStatsIndex"),
    (0, "NMS520-MIB", "nms520LineStatsInterval"),
)
if mibBuilder.loadTexts:
    nms520LineStatsEntry.setStatus("mandatory")
_Nms520LineStatsIndex_Type = SCinstance
_Nms520LineStatsIndex_Object = MibTableColumn
nms520LineStatsIndex = _Nms520LineStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 5, 1, 1),
    _Nms520LineStatsIndex_Type()
)
nms520LineStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520LineStatsIndex.setStatus("mandatory")


class _Nms520LineStatsInterval_Type(Integer32):
    """Custom type nms520LineStatsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Nms520LineStatsInterval_Type.__name__ = "Integer32"
_Nms520LineStatsInterval_Object = MibTableColumn
nms520LineStatsInterval = _Nms520LineStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 5, 1, 2),
    _Nms520LineStatsInterval_Type()
)
nms520LineStatsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520LineStatsInterval.setStatus("mandatory")


class _Nms520LineStatsTxInterpretation_Type(Integer32):
    """Custom type nms520LineStatsTxInterpretation based on Integer32"""
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
        *(("noSignal", 2),
          ("normal", 1),
          ("notAvailable", 3),
          ("overRange", 4))
    )


_Nms520LineStatsTxInterpretation_Type.__name__ = "Integer32"
_Nms520LineStatsTxInterpretation_Object = MibTableColumn
nms520LineStatsTxInterpretation = _Nms520LineStatsTxInterpretation_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 5, 1, 3),
    _Nms520LineStatsTxInterpretation_Type()
)
nms520LineStatsTxInterpretation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520LineStatsTxInterpretation.setStatus("mandatory")


class _Nms520LineStatsTxLevel_Type(Integer32):
    """Custom type nms520LineStatsTxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("txLevel0dB", 1),
          ("txLevel6dB", 2))
    )


_Nms520LineStatsTxLevel_Type.__name__ = "Integer32"
_Nms520LineStatsTxLevel_Object = MibTableColumn
nms520LineStatsTxLevel = _Nms520LineStatsTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 5, 1, 4),
    _Nms520LineStatsTxLevel_Type()
)
nms520LineStatsTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520LineStatsTxLevel.setStatus("mandatory")


class _Nms520LineStatsRxLevel_Type(Integer32):
    """Custom type nms520LineStatsRxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 6),
    )


_Nms520LineStatsRxLevel_Type.__name__ = "Integer32"
_Nms520LineStatsRxLevel_Object = MibTableColumn
nms520LineStatsRxLevel = _Nms520LineStatsRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 5, 1, 5),
    _Nms520LineStatsRxLevel_Type()
)
nms520LineStatsRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520LineStatsRxLevel.setStatus("mandatory")


class _Nms520LineStatsSignalToNoiseRatio_Type(Integer32):
    """Custom type nms520LineStatsSignalToNoiseRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_Nms520LineStatsSignalToNoiseRatio_Type.__name__ = "Integer32"
_Nms520LineStatsSignalToNoiseRatio_Object = MibTableColumn
nms520LineStatsSignalToNoiseRatio = _Nms520LineStatsSignalToNoiseRatio_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 5, 1, 6),
    _Nms520LineStatsSignalToNoiseRatio_Type()
)
nms520LineStatsSignalToNoiseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520LineStatsSignalToNoiseRatio.setStatus("mandatory")


class _Nms520LineStatsSignalQuality_Type(Integer32):
    """Custom type nms520LineStatsSignalQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 3),
          ("fair", 2),
          ("good", 1))
    )


_Nms520LineStatsSignalQuality_Type.__name__ = "Integer32"
_Nms520LineStatsSignalQuality_Object = MibTableColumn
nms520LineStatsSignalQuality = _Nms520LineStatsSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 5, 1, 7),
    _Nms520LineStatsSignalQuality_Type()
)
nms520LineStatsSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520LineStatsSignalQuality.setStatus("mandatory")


class _Nms520LineStatsJitter_Type(Integer32):
    """Custom type nms520LineStatsJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Nms520LineStatsJitter_Type.__name__ = "Integer32"
_Nms520LineStatsJitter_Object = MibTableColumn
nms520LineStatsJitter = _Nms520LineStatsJitter_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 5, 1, 8),
    _Nms520LineStatsJitter_Type()
)
nms520LineStatsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520LineStatsJitter.setStatus("mandatory")


class _Nms520LineStatsBpvCount_Type(Integer32):
    """Custom type nms520LineStatsBpvCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Nms520LineStatsBpvCount_Type.__name__ = "Integer32"
_Nms520LineStatsBpvCount_Object = MibTableColumn
nms520LineStatsBpvCount = _Nms520LineStatsBpvCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 5, 1, 9),
    _Nms520LineStatsBpvCount_Type()
)
nms520LineStatsBpvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520LineStatsBpvCount.setStatus("mandatory")


class _Nms520LineStatsFrameLossCount_Type(Integer32):
    """Custom type nms520LineStatsFrameLossCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Nms520LineStatsFrameLossCount_Type.__name__ = "Integer32"
_Nms520LineStatsFrameLossCount_Object = MibTableColumn
nms520LineStatsFrameLossCount = _Nms520LineStatsFrameLossCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 5, 1, 10),
    _Nms520LineStatsFrameLossCount_Type()
)
nms520LineStatsFrameLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520LineStatsFrameLossCount.setStatus("mandatory")
_Nms520DiagCfgTable_Object = MibTable
nms520DiagCfgTable = _Nms520DiagCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 6)
)
if mibBuilder.loadTexts:
    nms520DiagCfgTable.setStatus("mandatory")
_Nms520DiagCfgEntry_Object = MibTableRow
nms520DiagCfgEntry = _Nms520DiagCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 6, 1)
)
nms520DiagCfgEntry.setIndexNames(
    (0, "NMS520-MIB", "nms520DiagCfgIndex"),
)
if mibBuilder.loadTexts:
    nms520DiagCfgEntry.setStatus("mandatory")
_Nms520DiagCfgIndex_Type = SCinstance
_Nms520DiagCfgIndex_Object = MibTableColumn
nms520DiagCfgIndex = _Nms520DiagCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 6, 1, 1),
    _Nms520DiagCfgIndex_Type()
)
nms520DiagCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520DiagCfgIndex.setStatus("mandatory")


class _Nms520DiagSendCode_Type(Integer32):
    """Custom type nms520DiagSendCode based on Integer32"""
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
        *(("send15BitPattern", 4),
          ("send2047Pattern", 3),
          ("send511Pattern", 2),
          ("sendOtherPattern", 1))
    )


_Nms520DiagSendCode_Type.__name__ = "Integer32"
_Nms520DiagSendCode_Object = MibTableColumn
nms520DiagSendCode = _Nms520DiagSendCode_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 6, 1, 2),
    _Nms520DiagSendCode_Type()
)
nms520DiagSendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520DiagSendCode.setStatus("mandatory")


class _Nms520DiagTestExceptions_Type(Integer32):
    """Custom type nms520DiagTestExceptions based on Integer32"""
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
        *(("bitsOutOfRange", 3),
          ("blocksAndBitsOutOfRange", 4),
          ("blocksOutOfRange", 2),
          ("noExceptions", 1))
    )


_Nms520DiagTestExceptions_Type.__name__ = "Integer32"
_Nms520DiagTestExceptions_Object = MibTableColumn
nms520DiagTestExceptions = _Nms520DiagTestExceptions_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 6, 1, 3),
    _Nms520DiagTestExceptions_Type()
)
nms520DiagTestExceptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520DiagTestExceptions.setStatus("mandatory")


class _Nms520DiagBitErrors_Type(Integer32):
    """Custom type nms520DiagBitErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Nms520DiagBitErrors_Type.__name__ = "Integer32"
_Nms520DiagBitErrors_Object = MibTableColumn
nms520DiagBitErrors = _Nms520DiagBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 6, 1, 4),
    _Nms520DiagBitErrors_Type()
)
nms520DiagBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520DiagBitErrors.setStatus("mandatory")


class _Nms520DiagBlockErrors_Type(Integer32):
    """Custom type nms520DiagBlockErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Nms520DiagBlockErrors_Type.__name__ = "Integer32"
_Nms520DiagBlockErrors_Object = MibTableColumn
nms520DiagBlockErrors = _Nms520DiagBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 6, 1, 5),
    _Nms520DiagBlockErrors_Type()
)
nms520DiagBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520DiagBlockErrors.setStatus("mandatory")


class _Nms520DiagTestReset_Type(Integer32):
    """Custom type nms520DiagTestReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diagnostic", 2),
          ("normal", 1),
          ("resetTest", 3))
    )


_Nms520DiagTestReset_Type.__name__ = "Integer32"
_Nms520DiagTestReset_Object = MibTableColumn
nms520DiagTestReset = _Nms520DiagTestReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 6, 1, 6),
    _Nms520DiagTestReset_Type()
)
nms520DiagTestReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520DiagTestReset.setStatus("mandatory")


class _Nms520DiagTimeDelay_Type(Integer32):
    """Custom type nms520DiagTimeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Nms520DiagTimeDelay_Type.__name__ = "Integer32"
_Nms520DiagTimeDelay_Object = MibTableColumn
nms520DiagTimeDelay = _Nms520DiagTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 6, 1, 7),
    _Nms520DiagTimeDelay_Type()
)
nms520DiagTimeDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520DiagTimeDelay.setStatus("mandatory")
_Nms520DiagExcTable_Object = MibTable
nms520DiagExcTable = _Nms520DiagExcTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 7)
)
if mibBuilder.loadTexts:
    nms520DiagExcTable.setStatus("mandatory")
_Nms520DiagExcEntry_Object = MibTableRow
nms520DiagExcEntry = _Nms520DiagExcEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 7, 1)
)
nms520DiagExcEntry.setIndexNames(
    (0, "NMS520-MIB", "nms520DiagExcIndex"),
)
if mibBuilder.loadTexts:
    nms520DiagExcEntry.setStatus("mandatory")
_Nms520DiagExcIndex_Type = SCinstance
_Nms520DiagExcIndex_Object = MibTableColumn
nms520DiagExcIndex = _Nms520DiagExcIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 7, 1, 1),
    _Nms520DiagExcIndex_Type()
)
nms520DiagExcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520DiagExcIndex.setStatus("mandatory")


class _Nms520DiagExtLineloop_Type(Integer32):
    """Custom type nms520DiagExtLineloop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("lineloopOff", 1),
          ("lineloopOn", 2))
    )


_Nms520DiagExtLineloop_Type.__name__ = "Integer32"
_Nms520DiagExtLineloop_Object = MibTableColumn
nms520DiagExtLineloop = _Nms520DiagExtLineloop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 7, 1, 2),
    _Nms520DiagExtLineloop_Type()
)
nms520DiagExtLineloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520DiagExtLineloop.setStatus("obsolete")


class _Nms520DiagIntLineloop_Type(Integer32):
    """Custom type nms520DiagIntLineloop based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("blocks1", 3),
          ("blocks10", 4),
          ("blocks100", 5),
          ("blocks1000", 7),
          ("blocks10000", 9),
          ("blocks500", 6),
          ("blocks5000", 8),
          ("blocks50000", 10),
          ("lineloopOff", 1),
          ("lineloopOn", 2))
    )


_Nms520DiagIntLineloop_Type.__name__ = "Integer32"
_Nms520DiagIntLineloop_Object = MibTableColumn
nms520DiagIntLineloop = _Nms520DiagIntLineloop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 7, 1, 3),
    _Nms520DiagIntLineloop_Type()
)
nms520DiagIntLineloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520DiagIntLineloop.setStatus("mandatory")


class _Nms520DiagIntDataloop_Type(Integer32):
    """Custom type nms520DiagIntDataloop based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("blocks1", 3),
          ("blocks10", 4),
          ("blocks100", 5),
          ("blocks1000", 7),
          ("blocks10000", 9),
          ("blocks500", 6),
          ("blocks5000", 8),
          ("blocks50000", 10),
          ("dataloopOff", 1),
          ("dataloopOn", 2))
    )


_Nms520DiagIntDataloop_Type.__name__ = "Integer32"
_Nms520DiagIntDataloop_Object = MibTableColumn
nms520DiagIntDataloop = _Nms520DiagIntDataloop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 7, 1, 4),
    _Nms520DiagIntDataloop_Type()
)
nms520DiagIntDataloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520DiagIntDataloop.setStatus("mandatory")


class _Nms520DiagEndToEndSelftest_Type(Integer32):
    """Custom type nms520DiagEndToEndSelftest based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("blocks1", 3),
          ("blocks10", 4),
          ("blocks100", 5),
          ("blocks1000", 7),
          ("blocks10000", 9),
          ("blocks500", 6),
          ("blocks5000", 8),
          ("blocks50000", 10),
          ("endToEndOff", 1),
          ("endToEndOn", 2))
    )


_Nms520DiagEndToEndSelftest_Type.__name__ = "Integer32"
_Nms520DiagEndToEndSelftest_Object = MibTableColumn
nms520DiagEndToEndSelftest = _Nms520DiagEndToEndSelftest_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 7, 1, 5),
    _Nms520DiagEndToEndSelftest_Type()
)
nms520DiagEndToEndSelftest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520DiagEndToEndSelftest.setStatus("mandatory")


class _Nms520DiagNetworkDelay_Type(Integer32):
    """Custom type nms520DiagNetworkDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delayTestOff", 1),
          ("delayTestOn", 2),
          ("runDelayTest", 3))
    )


_Nms520DiagNetworkDelay_Type.__name__ = "Integer32"
_Nms520DiagNetworkDelay_Object = MibTableColumn
nms520DiagNetworkDelay = _Nms520DiagNetworkDelay_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 7, 1, 6),
    _Nms520DiagNetworkDelay_Type()
)
nms520DiagNetworkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520DiagNetworkDelay.setStatus("mandatory")


class _Nms520DiagTestStatus_Type(Integer32):
    """Custom type nms520DiagTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("endToend", 6),
          ("externalDataloop", 3),
          ("internalDataloop", 4),
          ("internalLineloop", 2),
          ("noTest", 1),
          ("serviceTestCenterLoop", 5))
    )


_Nms520DiagTestStatus_Type.__name__ = "Integer32"
_Nms520DiagTestStatus_Object = MibTableColumn
nms520DiagTestStatus = _Nms520DiagTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 7, 1, 7),
    _Nms520DiagTestStatus_Type()
)
nms520DiagTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520DiagTestStatus.setStatus("mandatory")


class _Nms520DiagExtDataloop_Type(Integer32):
    """Custom type nms520DiagExtDataloop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dataloopOff", 1),
          ("dataloopOn", 2),
          ("external", 3))
    )


_Nms520DiagExtDataloop_Type.__name__ = "Integer32"
_Nms520DiagExtDataloop_Object = MibTableColumn
nms520DiagExtDataloop = _Nms520DiagExtDataloop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 7, 1, 8),
    _Nms520DiagExtDataloop_Type()
)
nms520DiagExtDataloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520DiagExtDataloop.setStatus("mandatory")
_Nms520AlarmCfgTable_Object = MibTable
nms520AlarmCfgTable = _Nms520AlarmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 8)
)
if mibBuilder.loadTexts:
    nms520AlarmCfgTable.setStatus("mandatory")
_Nms520AlarmCfgEntry_Object = MibTableRow
nms520AlarmCfgEntry = _Nms520AlarmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 8, 1)
)
nms520AlarmCfgEntry.setIndexNames(
    (0, "NMS520-MIB", "nms520AlarmCfgIndex"),
    (0, "NMS520-MIB", "nms520AlarmCfgIdentifier"),
)
if mibBuilder.loadTexts:
    nms520AlarmCfgEntry.setStatus("mandatory")
_Nms520AlarmCfgIndex_Type = SCinstance
_Nms520AlarmCfgIndex_Object = MibTableColumn
nms520AlarmCfgIndex = _Nms520AlarmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 8, 1, 1),
    _Nms520AlarmCfgIndex_Type()
)
nms520AlarmCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520AlarmCfgIndex.setStatus("mandatory")
_Nms520AlarmCfgIdentifier_Type = ObjectIdentifier
_Nms520AlarmCfgIdentifier_Object = MibTableColumn
nms520AlarmCfgIdentifier = _Nms520AlarmCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 8, 1, 2),
    _Nms520AlarmCfgIdentifier_Type()
)
nms520AlarmCfgIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms520AlarmCfgIdentifier.setStatus("mandatory")


class _Nms520AlarmCfgThreshold_Type(Integer32):
    """Custom type nms520AlarmCfgThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 99),
    )


_Nms520AlarmCfgThreshold_Type.__name__ = "Integer32"
_Nms520AlarmCfgThreshold_Object = MibTableColumn
nms520AlarmCfgThreshold = _Nms520AlarmCfgThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 2, 8, 1, 3),
    _Nms520AlarmCfgThreshold_Type()
)
nms520AlarmCfgThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms520AlarmCfgThreshold.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS520-MIB",
    **{"nms520": nms520,
       "nms520MIBversion": nms520MIBversion,
       "nms520UnitCfgTable": nms520UnitCfgTable,
       "nms520UnitCfgEntry": nms520UnitCfgEntry,
       "nms520UnitCfgIndex": nms520UnitCfgIndex,
       "nms520Nms510CompatibilityMode": nms520Nms510CompatibilityMode,
       "nms520PtToPtSentryTime": nms520PtToPtSentryTime,
       "nms520AlarmHystTime": nms520AlarmHystTime,
       "nms520MtpointRmRspIntrvl": nms520MtpointRmRspIntrvl,
       "nms520DtePortType": nms520DtePortType,
       "nms520DteCtsDelay": nms520DteCtsDelay,
       "nms520DteCtsDelayExt": nms520DteCtsDelayExt,
       "nms520FirmwareLevel": nms520FirmwareLevel,
       "nms520DaisyChainBps": nms520DaisyChainBps,
       "nms520AlarmCfgCountWindow": nms520AlarmCfgCountWindow,
       "nms520SoftReset": nms520SoftReset,
       "nms520FrontPanelInhibit": nms520FrontPanelInhibit,
       "nms520FrontPanelEnable": nms520FrontPanelEnable,
       "nms520HdlcInvert": nms520HdlcInvert,
       "nms520PiggyBackDetect": nms520PiggyBackDetect,
       "nms520UnitType": nms520UnitType,
       "nms520ExtPortCtrlOut1": nms520ExtPortCtrlOut1,
       "nms520ExtPortCtrlOut2": nms520ExtPortCtrlOut2,
       "nms520AlarmData": nms520AlarmData,
       "nms520NoResponseAlm": nms520NoResponseAlm,
       "nms520DiagRxErrAlm": nms520DiagRxErrAlm,
       "nms520PowerUpAlm": nms520PowerUpAlm,
       "nms520EEChkSumErrAlm": nms520EEChkSumErrAlm,
       "nms520StcLoopbackAlm": nms520StcLoopbackAlm,
       "nms520NoNtwkLoopCurrentAlm": nms520NoNtwkLoopCurrentAlm,
       "nms520LinePairsReversedAlm": nms520LinePairsReversedAlm,
       "nms520NoSignalAlm": nms520NoSignalAlm,
       "nms520FpTestAlm": nms520FpTestAlm,
       "nms520StreamingAlm": nms520StreamingAlm,
       "nms520DSRLossAlm": nms520DSRLossAlm,
       "nms520DTRLossAlm": nms520DTRLossAlm,
       "nms520DTPLossAlm": nms520DTPLossAlm,
       "nms520DCDLossAlm": nms520DCDLossAlm,
       "nms520RXDLossAlm": nms520RXDLossAlm,
       "nms520TXDLossAlm": nms520TXDLossAlm,
       "nms520TmShortedAlm": nms520TmShortedAlm,
       "nms520DcdShortedAlm": nms520DcdShortedAlm,
       "nms520DsrShortedAlm": nms520DsrShortedAlm,
       "nms520CtsShortedAlm": nms520CtsShortedAlm,
       "nms520RxdShortedAlm": nms520RxdShortedAlm,
       "nms520RxcShortedAlm": nms520RxcShortedAlm,
       "nms520TxcShortedAlm": nms520TxcShortedAlm,
       "nms520DBURequestForScanAlm": nms520DBURequestForScanAlm,
       "nms520DBUOnalm": nms520DBUOnalm,
       "nms520DBUFailedAlm": nms520DBUFailedAlm,
       "nms520NoDSUResponseAlm": nms520NoDSUResponseAlm,
       "nms520NoDTEPollingAlm": nms520NoDTEPollingAlm,
       "nms520JitterAlm": nms520JitterAlm,
       "nms520BpvAlm": nms520BpvAlm,
       "nms520FrameLossAlm": nms520FrameLossAlm,
       "nms520SignalToNoiseAlm": nms520SignalToNoiseAlm,
       "nms520RxSignalLowAlm": nms520RxSignalLowAlm,
       "nms520ExtInputChangeAlm": nms520ExtInputChangeAlm,
       "nms520ExtInputLowAlm": nms520ExtInputLowAlm,
       "nms520LineStatsTable": nms520LineStatsTable,
       "nms520LineStatsEntry": nms520LineStatsEntry,
       "nms520LineStatsIndex": nms520LineStatsIndex,
       "nms520LineStatsInterval": nms520LineStatsInterval,
       "nms520LineStatsTxInterpretation": nms520LineStatsTxInterpretation,
       "nms520LineStatsTxLevel": nms520LineStatsTxLevel,
       "nms520LineStatsRxLevel": nms520LineStatsRxLevel,
       "nms520LineStatsSignalToNoiseRatio": nms520LineStatsSignalToNoiseRatio,
       "nms520LineStatsSignalQuality": nms520LineStatsSignalQuality,
       "nms520LineStatsJitter": nms520LineStatsJitter,
       "nms520LineStatsBpvCount": nms520LineStatsBpvCount,
       "nms520LineStatsFrameLossCount": nms520LineStatsFrameLossCount,
       "nms520DiagCfgTable": nms520DiagCfgTable,
       "nms520DiagCfgEntry": nms520DiagCfgEntry,
       "nms520DiagCfgIndex": nms520DiagCfgIndex,
       "nms520DiagSendCode": nms520DiagSendCode,
       "nms520DiagTestExceptions": nms520DiagTestExceptions,
       "nms520DiagBitErrors": nms520DiagBitErrors,
       "nms520DiagBlockErrors": nms520DiagBlockErrors,
       "nms520DiagTestReset": nms520DiagTestReset,
       "nms520DiagTimeDelay": nms520DiagTimeDelay,
       "nms520DiagExcTable": nms520DiagExcTable,
       "nms520DiagExcEntry": nms520DiagExcEntry,
       "nms520DiagExcIndex": nms520DiagExcIndex,
       "nms520DiagExtLineloop": nms520DiagExtLineloop,
       "nms520DiagIntLineloop": nms520DiagIntLineloop,
       "nms520DiagIntDataloop": nms520DiagIntDataloop,
       "nms520DiagEndToEndSelftest": nms520DiagEndToEndSelftest,
       "nms520DiagNetworkDelay": nms520DiagNetworkDelay,
       "nms520DiagTestStatus": nms520DiagTestStatus,
       "nms520DiagExtDataloop": nms520DiagExtDataloop,
       "nms520AlarmCfgTable": nms520AlarmCfgTable,
       "nms520AlarmCfgEntry": nms520AlarmCfgEntry,
       "nms520AlarmCfgIndex": nms520AlarmCfgIndex,
       "nms520AlarmCfgIdentifier": nms520AlarmCfgIdentifier,
       "nms520AlarmCfgThreshold": nms520AlarmCfgThreshold}
)
