# SNMP MIB module (NMS510-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS510-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:07 2024
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

_Nms510_ObjectIdentity = ObjectIdentity
nms510 = _Nms510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6)
)


class _Nms510MIBversion_Type(DisplayString):
    """Custom type nms510MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Nms510MIBversion_Type.__name__ = "DisplayString"
_Nms510MIBversion_Object = MibScalar
nms510MIBversion = _Nms510MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 1),
    _Nms510MIBversion_Type()
)
nms510MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms510MIBversion.setStatus("mandatory")
_Nms510UnitCfgTable_Object = MibTable
nms510UnitCfgTable = _Nms510UnitCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 2)
)
if mibBuilder.loadTexts:
    nms510UnitCfgTable.setStatus("mandatory")
_Nms510UnitCfgEntry_Object = MibTableRow
nms510UnitCfgEntry = _Nms510UnitCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 2, 1)
)
nms510UnitCfgEntry.setIndexNames(
    (0, "NMS510-MIB", "nms510UnitCfgIndex"),
)
if mibBuilder.loadTexts:
    nms510UnitCfgEntry.setStatus("mandatory")
_Nms510UnitCfgIndex_Type = SCinstance
_Nms510UnitCfgIndex_Object = MibTableColumn
nms510UnitCfgIndex = _Nms510UnitCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 2, 1, 1),
    _Nms510UnitCfgIndex_Type()
)
nms510UnitCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms510UnitCfgIndex.setStatus("mandatory")


class _Nms510DteCtsDelay_Type(Integer32):
    """Custom type nms510DteCtsDelay based on Integer32"""
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


_Nms510DteCtsDelay_Type.__name__ = "Integer32"
_Nms510DteCtsDelay_Object = MibTableColumn
nms510DteCtsDelay = _Nms510DteCtsDelay_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 2, 1, 2),
    _Nms510DteCtsDelay_Type()
)
nms510DteCtsDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510DteCtsDelay.setStatus("mandatory")


class _Nms510DteCtsDelayExt_Type(Integer32):
    """Custom type nms510DteCtsDelayExt based on Integer32"""
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


_Nms510DteCtsDelayExt_Type.__name__ = "Integer32"
_Nms510DteCtsDelayExt_Object = MibTableColumn
nms510DteCtsDelayExt = _Nms510DteCtsDelayExt_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 2, 1, 3),
    _Nms510DteCtsDelayExt_Type()
)
nms510DteCtsDelayExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510DteCtsDelayExt.setStatus("mandatory")


class _Nms510FirmwareLevel_Type(DisplayString):
    """Custom type nms510FirmwareLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Nms510FirmwareLevel_Type.__name__ = "DisplayString"
_Nms510FirmwareLevel_Object = MibTableColumn
nms510FirmwareLevel = _Nms510FirmwareLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 2, 1, 4),
    _Nms510FirmwareLevel_Type()
)
nms510FirmwareLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms510FirmwareLevel.setStatus("mandatory")


class _Nms510AlarmCfgCountWindow_Type(Integer32):
    """Custom type nms510AlarmCfgCountWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Nms510AlarmCfgCountWindow_Type.__name__ = "Integer32"
_Nms510AlarmCfgCountWindow_Object = MibTableColumn
nms510AlarmCfgCountWindow = _Nms510AlarmCfgCountWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 2, 1, 5),
    _Nms510AlarmCfgCountWindow_Type()
)
nms510AlarmCfgCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510AlarmCfgCountWindow.setStatus("mandatory")


class _Nms510SoftReset_Type(Integer32):
    """Custom type nms510SoftReset based on Integer32"""
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


_Nms510SoftReset_Type.__name__ = "Integer32"
_Nms510SoftReset_Object = MibTableColumn
nms510SoftReset = _Nms510SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 2, 1, 6),
    _Nms510SoftReset_Type()
)
nms510SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510SoftReset.setStatus("mandatory")


class _Nms510FrontPanelInhibit_Type(Integer32):
    """Custom type nms510FrontPanelInhibit based on Integer32"""
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


_Nms510FrontPanelInhibit_Type.__name__ = "Integer32"
_Nms510FrontPanelInhibit_Object = MibTableColumn
nms510FrontPanelInhibit = _Nms510FrontPanelInhibit_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 2, 1, 7),
    _Nms510FrontPanelInhibit_Type()
)
nms510FrontPanelInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510FrontPanelInhibit.setStatus("mandatory")


class _Nms510FrontPanelEnable_Type(Integer32):
    """Custom type nms510FrontPanelEnable based on Integer32"""
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


_Nms510FrontPanelEnable_Type.__name__ = "Integer32"
_Nms510FrontPanelEnable_Object = MibTableColumn
nms510FrontPanelEnable = _Nms510FrontPanelEnable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 2, 1, 8),
    _Nms510FrontPanelEnable_Type()
)
nms510FrontPanelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510FrontPanelEnable.setStatus("mandatory")


class _Nms510HdlcInvert_Type(Integer32):
    """Custom type nms510HdlcInvert based on Integer32"""
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


_Nms510HdlcInvert_Type.__name__ = "Integer32"
_Nms510HdlcInvert_Object = MibTableColumn
nms510HdlcInvert = _Nms510HdlcInvert_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 2, 1, 9),
    _Nms510HdlcInvert_Type()
)
nms510HdlcInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510HdlcInvert.setStatus("mandatory")


class _Nms510PiggyBackDetect_Type(Integer32):
    """Custom type nms510PiggyBackDetect based on Integer32"""
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


_Nms510PiggyBackDetect_Type.__name__ = "Integer32"
_Nms510PiggyBackDetect_Object = MibTableColumn
nms510PiggyBackDetect = _Nms510PiggyBackDetect_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 2, 1, 10),
    _Nms510PiggyBackDetect_Type()
)
nms510PiggyBackDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms510PiggyBackDetect.setStatus("mandatory")


class _Nms510ExtPortCtrlOut1_Type(Integer32):
    """Custom type nms510ExtPortCtrlOut1 based on Integer32"""
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


_Nms510ExtPortCtrlOut1_Type.__name__ = "Integer32"
_Nms510ExtPortCtrlOut1_Object = MibTableColumn
nms510ExtPortCtrlOut1 = _Nms510ExtPortCtrlOut1_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 2, 1, 11),
    _Nms510ExtPortCtrlOut1_Type()
)
nms510ExtPortCtrlOut1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510ExtPortCtrlOut1.setStatus("mandatory")


class _Nms510ExtPortCtrlOut2_Type(Integer32):
    """Custom type nms510ExtPortCtrlOut2 based on Integer32"""
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


_Nms510ExtPortCtrlOut2_Type.__name__ = "Integer32"
_Nms510ExtPortCtrlOut2_Object = MibTableColumn
nms510ExtPortCtrlOut2 = _Nms510ExtPortCtrlOut2_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 2, 1, 12),
    _Nms510ExtPortCtrlOut2_Type()
)
nms510ExtPortCtrlOut2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510ExtPortCtrlOut2.setStatus("mandatory")
_Nms510AlarmData_ObjectIdentity = ObjectIdentity
nms510AlarmData = _Nms510AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4)
)
_Nms510NoResponseAlm_ObjectIdentity = ObjectIdentity
nms510NoResponseAlm = _Nms510NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 1)
)
_Nms510DiagRxErrAlm_ObjectIdentity = ObjectIdentity
nms510DiagRxErrAlm = _Nms510DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 2)
)
_Nms510PowerUpAlm_ObjectIdentity = ObjectIdentity
nms510PowerUpAlm = _Nms510PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 3)
)
_Nms510EEChkSumErrAlm_ObjectIdentity = ObjectIdentity
nms510EEChkSumErrAlm = _Nms510EEChkSumErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 4)
)
_Nms510StcLoopbackAlm_ObjectIdentity = ObjectIdentity
nms510StcLoopbackAlm = _Nms510StcLoopbackAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 5)
)
_Nms510NoSignalAlm_ObjectIdentity = ObjectIdentity
nms510NoSignalAlm = _Nms510NoSignalAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 6)
)
_Nms510FpTestAlm_ObjectIdentity = ObjectIdentity
nms510FpTestAlm = _Nms510FpTestAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 7)
)
_Nms510StreamingAlm_ObjectIdentity = ObjectIdentity
nms510StreamingAlm = _Nms510StreamingAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 8)
)
_Nms510DSRLossAlm_ObjectIdentity = ObjectIdentity
nms510DSRLossAlm = _Nms510DSRLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 9)
)
_Nms510DTRLossAlm_ObjectIdentity = ObjectIdentity
nms510DTRLossAlm = _Nms510DTRLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 10)
)
_Nms510DTPLossAlm_ObjectIdentity = ObjectIdentity
nms510DTPLossAlm = _Nms510DTPLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 11)
)
_Nms510DCDLossAlm_ObjectIdentity = ObjectIdentity
nms510DCDLossAlm = _Nms510DCDLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 12)
)
_Nms510RXDLossAlm_ObjectIdentity = ObjectIdentity
nms510RXDLossAlm = _Nms510RXDLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 13)
)
_Nms510TXDLossAlm_ObjectIdentity = ObjectIdentity
nms510TXDLossAlm = _Nms510TXDLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 14)
)
_Nms510DBURequestForScanAlm_ObjectIdentity = ObjectIdentity
nms510DBURequestForScanAlm = _Nms510DBURequestForScanAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 15)
)
_Nms510DBUOnalm_ObjectIdentity = ObjectIdentity
nms510DBUOnalm = _Nms510DBUOnalm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 16)
)
_Nms510DBUFailedAlm_ObjectIdentity = ObjectIdentity
nms510DBUFailedAlm = _Nms510DBUFailedAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 17)
)
_Nms510ExtInputChangeAlm_ObjectIdentity = ObjectIdentity
nms510ExtInputChangeAlm = _Nms510ExtInputChangeAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 18)
)
_Nms510ExtInputLowAlm_ObjectIdentity = ObjectIdentity
nms510ExtInputLowAlm = _Nms510ExtInputLowAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 19)
)
_Nms510FrameLossAlm_ObjectIdentity = ObjectIdentity
nms510FrameLossAlm = _Nms510FrameLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 4, 20)
)
_Nms510DiagCfgTable_Object = MibTable
nms510DiagCfgTable = _Nms510DiagCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 6)
)
if mibBuilder.loadTexts:
    nms510DiagCfgTable.setStatus("mandatory")
_Nms510DiagCfgEntry_Object = MibTableRow
nms510DiagCfgEntry = _Nms510DiagCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 6, 1)
)
nms510DiagCfgEntry.setIndexNames(
    (0, "NMS510-MIB", "nms510DiagCfgIndex"),
)
if mibBuilder.loadTexts:
    nms510DiagCfgEntry.setStatus("mandatory")
_Nms510DiagCfgIndex_Type = SCinstance
_Nms510DiagCfgIndex_Object = MibTableColumn
nms510DiagCfgIndex = _Nms510DiagCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 6, 1, 1),
    _Nms510DiagCfgIndex_Type()
)
nms510DiagCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms510DiagCfgIndex.setStatus("mandatory")


class _Nms510DiagSendCode_Type(Integer32):
    """Custom type nms510DiagSendCode based on Integer32"""
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


_Nms510DiagSendCode_Type.__name__ = "Integer32"
_Nms510DiagSendCode_Object = MibTableColumn
nms510DiagSendCode = _Nms510DiagSendCode_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 6, 1, 2),
    _Nms510DiagSendCode_Type()
)
nms510DiagSendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510DiagSendCode.setStatus("mandatory")


class _Nms510DiagTestExceptions_Type(Integer32):
    """Custom type nms510DiagTestExceptions based on Integer32"""
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


_Nms510DiagTestExceptions_Type.__name__ = "Integer32"
_Nms510DiagTestExceptions_Object = MibTableColumn
nms510DiagTestExceptions = _Nms510DiagTestExceptions_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 6, 1, 3),
    _Nms510DiagTestExceptions_Type()
)
nms510DiagTestExceptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms510DiagTestExceptions.setStatus("mandatory")


class _Nms510DiagBitErrors_Type(Integer32):
    """Custom type nms510DiagBitErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Nms510DiagBitErrors_Type.__name__ = "Integer32"
_Nms510DiagBitErrors_Object = MibTableColumn
nms510DiagBitErrors = _Nms510DiagBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 6, 1, 4),
    _Nms510DiagBitErrors_Type()
)
nms510DiagBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms510DiagBitErrors.setStatus("mandatory")


class _Nms510DiagBlockErrors_Type(Integer32):
    """Custom type nms510DiagBlockErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Nms510DiagBlockErrors_Type.__name__ = "Integer32"
_Nms510DiagBlockErrors_Object = MibTableColumn
nms510DiagBlockErrors = _Nms510DiagBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 6, 1, 5),
    _Nms510DiagBlockErrors_Type()
)
nms510DiagBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms510DiagBlockErrors.setStatus("mandatory")


class _Nms510DiagTestReset_Type(Integer32):
    """Custom type nms510DiagTestReset based on Integer32"""
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


_Nms510DiagTestReset_Type.__name__ = "Integer32"
_Nms510DiagTestReset_Object = MibTableColumn
nms510DiagTestReset = _Nms510DiagTestReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 6, 1, 6),
    _Nms510DiagTestReset_Type()
)
nms510DiagTestReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510DiagTestReset.setStatus("mandatory")
_Nms510DiagExcTable_Object = MibTable
nms510DiagExcTable = _Nms510DiagExcTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 7)
)
if mibBuilder.loadTexts:
    nms510DiagExcTable.setStatus("mandatory")
_Nms510DiagExcEntry_Object = MibTableRow
nms510DiagExcEntry = _Nms510DiagExcEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 7, 1)
)
nms510DiagExcEntry.setIndexNames(
    (0, "NMS510-MIB", "nms510DiagExcIndex"),
)
if mibBuilder.loadTexts:
    nms510DiagExcEntry.setStatus("mandatory")
_Nms510DiagExcIndex_Type = SCinstance
_Nms510DiagExcIndex_Object = MibTableColumn
nms510DiagExcIndex = _Nms510DiagExcIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 7, 1, 1),
    _Nms510DiagExcIndex_Type()
)
nms510DiagExcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms510DiagExcIndex.setStatus("mandatory")


class _Nms510DiagIntLineloop_Type(Integer32):
    """Custom type nms510DiagIntLineloop based on Integer32"""
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


_Nms510DiagIntLineloop_Type.__name__ = "Integer32"
_Nms510DiagIntLineloop_Object = MibTableColumn
nms510DiagIntLineloop = _Nms510DiagIntLineloop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 7, 1, 2),
    _Nms510DiagIntLineloop_Type()
)
nms510DiagIntLineloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510DiagIntLineloop.setStatus("mandatory")


class _Nms510DiagIntDataloop_Type(Integer32):
    """Custom type nms510DiagIntDataloop based on Integer32"""
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


_Nms510DiagIntDataloop_Type.__name__ = "Integer32"
_Nms510DiagIntDataloop_Object = MibTableColumn
nms510DiagIntDataloop = _Nms510DiagIntDataloop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 7, 1, 3),
    _Nms510DiagIntDataloop_Type()
)
nms510DiagIntDataloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510DiagIntDataloop.setStatus("mandatory")


class _Nms510DiagEndToEndSelftest_Type(Integer32):
    """Custom type nms510DiagEndToEndSelftest based on Integer32"""
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


_Nms510DiagEndToEndSelftest_Type.__name__ = "Integer32"
_Nms510DiagEndToEndSelftest_Object = MibTableColumn
nms510DiagEndToEndSelftest = _Nms510DiagEndToEndSelftest_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 7, 1, 4),
    _Nms510DiagEndToEndSelftest_Type()
)
nms510DiagEndToEndSelftest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510DiagEndToEndSelftest.setStatus("mandatory")


class _Nms510DiagNetworkDelay_Type(Integer32):
    """Custom type nms510DiagNetworkDelay based on Integer32"""
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


_Nms510DiagNetworkDelay_Type.__name__ = "Integer32"
_Nms510DiagNetworkDelay_Object = MibTableColumn
nms510DiagNetworkDelay = _Nms510DiagNetworkDelay_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 7, 1, 5),
    _Nms510DiagNetworkDelay_Type()
)
nms510DiagNetworkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510DiagNetworkDelay.setStatus("mandatory")


class _Nms510DiagTestStatus_Type(Integer32):
    """Custom type nms510DiagTestStatus based on Integer32"""
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


_Nms510DiagTestStatus_Type.__name__ = "Integer32"
_Nms510DiagTestStatus_Object = MibTableColumn
nms510DiagTestStatus = _Nms510DiagTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 7, 1, 6),
    _Nms510DiagTestStatus_Type()
)
nms510DiagTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms510DiagTestStatus.setStatus("mandatory")


class _Nms510DiagExtDataloop_Type(Integer32):
    """Custom type nms510DiagExtDataloop based on Integer32"""
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


_Nms510DiagExtDataloop_Type.__name__ = "Integer32"
_Nms510DiagExtDataloop_Object = MibTableColumn
nms510DiagExtDataloop = _Nms510DiagExtDataloop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 7, 1, 7),
    _Nms510DiagExtDataloop_Type()
)
nms510DiagExtDataloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510DiagExtDataloop.setStatus("mandatory")
_Nms510AlarmCfgTable_Object = MibTable
nms510AlarmCfgTable = _Nms510AlarmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 8)
)
if mibBuilder.loadTexts:
    nms510AlarmCfgTable.setStatus("mandatory")
_Nms510AlarmCfgEntry_Object = MibTableRow
nms510AlarmCfgEntry = _Nms510AlarmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 8, 1)
)
nms510AlarmCfgEntry.setIndexNames(
    (0, "NMS510-MIB", "nms510AlarmCfgIndex"),
    (0, "NMS510-MIB", "nms510AlarmCfgIdentifier"),
)
if mibBuilder.loadTexts:
    nms510AlarmCfgEntry.setStatus("mandatory")
_Nms510AlarmCfgIndex_Type = SCinstance
_Nms510AlarmCfgIndex_Object = MibTableColumn
nms510AlarmCfgIndex = _Nms510AlarmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 8, 1, 1),
    _Nms510AlarmCfgIndex_Type()
)
nms510AlarmCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms510AlarmCfgIndex.setStatus("mandatory")
_Nms510AlarmCfgIdentifier_Type = ObjectIdentifier
_Nms510AlarmCfgIdentifier_Object = MibTableColumn
nms510AlarmCfgIdentifier = _Nms510AlarmCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 8, 1, 2),
    _Nms510AlarmCfgIdentifier_Type()
)
nms510AlarmCfgIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms510AlarmCfgIdentifier.setStatus("mandatory")


class _Nms510AlarmCfgThreshold_Type(Integer32):
    """Custom type nms510AlarmCfgThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Nms510AlarmCfgThreshold_Type.__name__ = "Integer32"
_Nms510AlarmCfgThreshold_Object = MibTableColumn
nms510AlarmCfgThreshold = _Nms510AlarmCfgThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 6, 8, 1, 3),
    _Nms510AlarmCfgThreshold_Type()
)
nms510AlarmCfgThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms510AlarmCfgThreshold.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS510-MIB",
    **{"nms510": nms510,
       "nms510MIBversion": nms510MIBversion,
       "nms510UnitCfgTable": nms510UnitCfgTable,
       "nms510UnitCfgEntry": nms510UnitCfgEntry,
       "nms510UnitCfgIndex": nms510UnitCfgIndex,
       "nms510DteCtsDelay": nms510DteCtsDelay,
       "nms510DteCtsDelayExt": nms510DteCtsDelayExt,
       "nms510FirmwareLevel": nms510FirmwareLevel,
       "nms510AlarmCfgCountWindow": nms510AlarmCfgCountWindow,
       "nms510SoftReset": nms510SoftReset,
       "nms510FrontPanelInhibit": nms510FrontPanelInhibit,
       "nms510FrontPanelEnable": nms510FrontPanelEnable,
       "nms510HdlcInvert": nms510HdlcInvert,
       "nms510PiggyBackDetect": nms510PiggyBackDetect,
       "nms510ExtPortCtrlOut1": nms510ExtPortCtrlOut1,
       "nms510ExtPortCtrlOut2": nms510ExtPortCtrlOut2,
       "nms510AlarmData": nms510AlarmData,
       "nms510NoResponseAlm": nms510NoResponseAlm,
       "nms510DiagRxErrAlm": nms510DiagRxErrAlm,
       "nms510PowerUpAlm": nms510PowerUpAlm,
       "nms510EEChkSumErrAlm": nms510EEChkSumErrAlm,
       "nms510StcLoopbackAlm": nms510StcLoopbackAlm,
       "nms510NoSignalAlm": nms510NoSignalAlm,
       "nms510FpTestAlm": nms510FpTestAlm,
       "nms510StreamingAlm": nms510StreamingAlm,
       "nms510DSRLossAlm": nms510DSRLossAlm,
       "nms510DTRLossAlm": nms510DTRLossAlm,
       "nms510DTPLossAlm": nms510DTPLossAlm,
       "nms510DCDLossAlm": nms510DCDLossAlm,
       "nms510RXDLossAlm": nms510RXDLossAlm,
       "nms510TXDLossAlm": nms510TXDLossAlm,
       "nms510DBURequestForScanAlm": nms510DBURequestForScanAlm,
       "nms510DBUOnalm": nms510DBUOnalm,
       "nms510DBUFailedAlm": nms510DBUFailedAlm,
       "nms510ExtInputChangeAlm": nms510ExtInputChangeAlm,
       "nms510ExtInputLowAlm": nms510ExtInputLowAlm,
       "nms510FrameLossAlm": nms510FrameLossAlm,
       "nms510DiagCfgTable": nms510DiagCfgTable,
       "nms510DiagCfgEntry": nms510DiagCfgEntry,
       "nms510DiagCfgIndex": nms510DiagCfgIndex,
       "nms510DiagSendCode": nms510DiagSendCode,
       "nms510DiagTestExceptions": nms510DiagTestExceptions,
       "nms510DiagBitErrors": nms510DiagBitErrors,
       "nms510DiagBlockErrors": nms510DiagBlockErrors,
       "nms510DiagTestReset": nms510DiagTestReset,
       "nms510DiagExcTable": nms510DiagExcTable,
       "nms510DiagExcEntry": nms510DiagExcEntry,
       "nms510DiagExcIndex": nms510DiagExcIndex,
       "nms510DiagIntLineloop": nms510DiagIntLineloop,
       "nms510DiagIntDataloop": nms510DiagIntDataloop,
       "nms510DiagEndToEndSelftest": nms510DiagEndToEndSelftest,
       "nms510DiagNetworkDelay": nms510DiagNetworkDelay,
       "nms510DiagTestStatus": nms510DiagTestStatus,
       "nms510DiagExtDataloop": nms510DiagExtDataloop,
       "nms510AlarmCfgTable": nms510AlarmCfgTable,
       "nms510AlarmCfgEntry": nms510AlarmCfgEntry,
       "nms510AlarmCfgIndex": nms510AlarmCfgIndex,
       "nms510AlarmCfgIdentifier": nms510AlarmCfgIdentifier,
       "nms510AlarmCfgThreshold": nms510AlarmCfgThreshold}
)
