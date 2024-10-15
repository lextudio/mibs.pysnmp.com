# SNMP MIB module (GDCMDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCMDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:16 2024
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
 NotificationType,
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
    "NotificationType",
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

_Gdc_ObjectIdentity = ObjectIdentity
gdc = _Gdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498)
)
_Mdm_ObjectIdentity = ObjectIdentity
mdm = _Mdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 4)
)
_MdmNetworkConfigTable_Object = MibTable
mdmNetworkConfigTable = _MdmNetworkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 1)
)
if mibBuilder.loadTexts:
    mdmNetworkConfigTable.setStatus("mandatory")
_MdmNetworkEntry_Object = MibTableRow
mdmNetworkEntry = _MdmNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 1, 1)
)
mdmNetworkEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmNetworkIndex"),
)
if mibBuilder.loadTexts:
    mdmNetworkEntry.setStatus("mandatory")
_MdmNetworkIndex_Type = SCinstance
_MdmNetworkIndex_Object = MibTableColumn
mdmNetworkIndex = _MdmNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 1, 1, 1),
    _MdmNetworkIndex_Type()
)
mdmNetworkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmNetworkIndex.setStatus("mandatory")


class _MdmNetworkType_Type(Integer32):
    """Custom type mdmNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("privateLine2Wire", 2),
          ("privateLine4Wire", 3),
          ("switchedNetwork", 1))
    )


_MdmNetworkType_Type.__name__ = "Integer32"
_MdmNetworkType_Object = MibTableColumn
mdmNetworkType = _MdmNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 1, 1, 2),
    _MdmNetworkType_Type()
)
mdmNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmNetworkType.setStatus("mandatory")


class _MdmSNTxType_Type(Integer32):
    """Custom type mdmSNTxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adjustable", 3),
          ("permissive", 1),
          ("programmable", 2))
    )


_MdmSNTxType_Type.__name__ = "Integer32"
_MdmSNTxType_Object = MibTableColumn
mdmSNTxType = _MdmSNTxType_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 1, 1, 3),
    _MdmSNTxType_Type()
)
mdmSNTxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmSNTxType.setStatus("mandatory")


class _MdmSNTxLevel_Type(Integer32):
    """Custom type mdmSNTxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MdmSNTxLevel_Type.__name__ = "Integer32"
_MdmSNTxLevel_Object = MibTableColumn
mdmSNTxLevel = _MdmSNTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 1, 1, 4),
    _MdmSNTxLevel_Type()
)
mdmSNTxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmSNTxLevel.setStatus("mandatory")


class _MdmSNHandshakeMode_Type(Integer32):
    """Custom type mdmSNHandshakeMode based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("bell103", 10),
          ("bell212", 9),
          ("gdcVfastAuto", 1),
          ("gdcVfastOnly", 2),
          ("v21", 11),
          ("v22Only", 8),
          ("v22bis", 7),
          ("v32Auto", 5),
          ("v32Only", 6),
          ("v32bisAuto", 3),
          ("v32bisOnly", 4))
    )


_MdmSNHandshakeMode_Type.__name__ = "Integer32"
_MdmSNHandshakeMode_Object = MibTableColumn
mdmSNHandshakeMode = _MdmSNHandshakeMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 1, 1, 5),
    _MdmSNHandshakeMode_Type()
)
mdmSNHandshakeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmSNHandshakeMode.setStatus("mandatory")
_MdmDTEConfigTable_Object = MibTable
mdmDTEConfigTable = _MdmDTEConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2)
)
if mibBuilder.loadTexts:
    mdmDTEConfigTable.setStatus("mandatory")
_MdmDTEntry_Object = MibTableRow
mdmDTEntry = _MdmDTEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1)
)
mdmDTEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmDTEIndex"),
)
if mibBuilder.loadTexts:
    mdmDTEntry.setStatus("mandatory")
_MdmDTEIndex_Type = SCinstance
_MdmDTEIndex_Object = MibTableColumn
mdmDTEIndex = _MdmDTEIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 1),
    _MdmDTEIndex_Type()
)
mdmDTEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDTEIndex.setStatus("mandatory")


class _MdmDTESpeed_Type(Integer32):
    """Custom type mdmDTESpeed based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("autobaud", 1),
          ("bps115200", 20),
          ("bps1200", 4),
          ("bps12000", 9),
          ("bps128000", 21),
          ("bps14400", 10),
          ("bps16800", 11),
          ("bps19200", 12),
          ("bps21600", 13),
          ("bps2400", 5),
          ("bps24000", 14),
          ("bps26400", 15),
          ("bps28800", 16),
          ("bps300", 3),
          ("bps38400", 17),
          ("bps4800", 6),
          ("bps57600", 18),
          ("bps7200", 7),
          ("bps76800", 19),
          ("bps9600", 8),
          ("lastAT", 2))
    )


_MdmDTESpeed_Type.__name__ = "Integer32"
_MdmDTESpeed_Object = MibTableColumn
mdmDTESpeed = _MdmDTESpeed_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 2),
    _MdmDTESpeed_Type()
)
mdmDTESpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDTESpeed.setStatus("mandatory")


class _MdmCPMResp_Type(Integer32):
    """Custom type mdmCPMResp based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("autobaud", 1),
          ("bps115200", 20),
          ("bps1200", 4),
          ("bps12000", 9),
          ("bps128000", 21),
          ("bps14400", 10),
          ("bps16800", 11),
          ("bps19200", 12),
          ("bps21600", 13),
          ("bps2400", 5),
          ("bps24000", 14),
          ("bps26400", 15),
          ("bps28800", 16),
          ("bps300", 3),
          ("bps38400", 17),
          ("bps4800", 6),
          ("bps57600", 18),
          ("bps7200", 7),
          ("bps76800", 19),
          ("bps9600", 8),
          ("lastConnectSpeed", 2))
    )


_MdmCPMResp_Type.__name__ = "Integer32"
_MdmCPMResp_Object = MibTableColumn
mdmCPMResp = _MdmCPMResp_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 3),
    _MdmCPMResp_Type()
)
mdmCPMResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCPMResp.setStatus("mandatory")


class _MdmCharLength_Type(Integer32):
    """Custom type mdmCharLength based on Integer32"""
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
        *(("data6Stop1", 1),
          ("data7ParityStop1", 3),
          ("data7ParityStop2", 5),
          ("data7Stop1", 2),
          ("data8ParityStop1", 6),
          ("data8Stop1", 4))
    )


_MdmCharLength_Type.__name__ = "Integer32"
_MdmCharLength_Object = MibTableColumn
mdmCharLength = _MdmCharLength_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 4),
    _MdmCharLength_Type()
)
mdmCharLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCharLength.setStatus("mandatory")


class _MdmParity_Type(Integer32):
    """Custom type mdmParity based on Integer32"""
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
        *(("auto", 5),
          ("even", 1),
          ("mark", 4),
          ("odd", 3),
          ("space", 2))
    )


_MdmParity_Type.__name__ = "Integer32"
_MdmParity_Object = MibTableColumn
mdmParity = _MdmParity_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 5),
    _MdmParity_Type()
)
mdmParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmParity.setStatus("mandatory")


class _MdmOverspeed_Type(Integer32):
    """Custom type mdmOverspeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("nominal", 1))
    )


_MdmOverspeed_Type.__name__ = "Integer32"
_MdmOverspeed_Object = MibTableColumn
mdmOverspeed = _MdmOverspeed_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 6),
    _MdmOverspeed_Type()
)
mdmOverspeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmOverspeed.setStatus("mandatory")


class _MdmFlowCntrl_Type(Integer32):
    """Custom type mdmFlowCntrl based on Integer32"""
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
        *(("cts", 3),
          ("disabled", 1),
          ("rtsCts", 4),
          ("xonXoff", 5),
          ("xonXoffSig", 2))
    )


_MdmFlowCntrl_Type.__name__ = "Integer32"
_MdmFlowCntrl_Object = MibTableColumn
mdmFlowCntrl = _MdmFlowCntrl_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 7),
    _MdmFlowCntrl_Type()
)
mdmFlowCntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmFlowCntrl.setStatus("mandatory")


class _MdmTermEcho_Type(Integer32):
    """Custom type mdmTermEcho based on Integer32"""
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


_MdmTermEcho_Type.__name__ = "Integer32"
_MdmTermEcho_Object = MibTableColumn
mdmTermEcho = _MdmTermEcho_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 8),
    _MdmTermEcho_Type()
)
mdmTermEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTermEcho.setStatus("mandatory")


class _MdmDCDCntrl_Type(Integer32):
    """Custom type mdmDCDCntrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forceOn", 1),
          ("forceOnToggleDisc", 3),
          ("real", 2))
    )


_MdmDCDCntrl_Type.__name__ = "Integer32"
_MdmDCDCntrl_Object = MibTableColumn
mdmDCDCntrl = _MdmDCDCntrl_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 9),
    _MdmDCDCntrl_Type()
)
mdmDCDCntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDCDCntrl.setStatus("mandatory")


class _MdmCTSCntrl_Type(Integer32):
    """Custom type mdmCTSCntrl based on Integer32"""
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
        *(("cmdOnDataRTS", 1),
          ("cmdOnDataReal", 2),
          ("forceOn", 4),
          ("realCCITT", 3))
    )


_MdmCTSCntrl_Type.__name__ = "Integer32"
_MdmCTSCntrl_Object = MibTableColumn
mdmCTSCntrl = _MdmCTSCntrl_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 10),
    _MdmCTSCntrl_Type()
)
mdmCTSCntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCTSCntrl.setStatus("mandatory")


class _MdmDTRTrans_Type(Integer32):
    """Custom type mdmDTRTrans based on Integer32"""
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
        *(("forceon", 1),
          ("offDisc", 3),
          ("offDiscRecallUser", 4),
          ("offInCmdMode", 2))
    )


_MdmDTRTrans_Type.__name__ = "Integer32"
_MdmDTRTrans_Object = MibTableColumn
mdmDTRTrans = _MdmDTRTrans_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 11),
    _MdmDTRTrans_Type()
)
mdmDTRTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDTRTrans.setStatus("mandatory")


class _MdmDSRCntrl_Type(Integer32):
    """Custom type mdmDSRCntrl based on Integer32"""
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
        *(("followDCD", 3),
          ("forceOn", 4),
          ("normal", 2),
          ("onUntilDisc", 1))
    )


_MdmDSRCntrl_Type.__name__ = "Integer32"
_MdmDSRCntrl_Object = MibTableColumn
mdmDSRCntrl = _MdmDSRCntrl_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 12),
    _MdmDSRCntrl_Type()
)
mdmDSRCntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDSRCntrl.setStatus("mandatory")


class _MdmDSRCntrlAL_Type(Integer32):
    """Custom type mdmDSRCntrlAL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offAnaloop", 2),
          ("onAnaloop", 1))
    )


_MdmDSRCntrlAL_Type.__name__ = "Integer32"
_MdmDSRCntrlAL_Object = MibTableColumn
mdmDSRCntrlAL = _MdmDSRCntrlAL_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 13),
    _MdmDSRCntrlAL_Type()
)
mdmDSRCntrlAL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDSRCntrlAL.setStatus("mandatory")


class _MdmTXClockSource_Type(Integer32):
    """Custom type mdmTXClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("receiverwrap", 3))
    )


_MdmTXClockSource_Type.__name__ = "Integer32"
_MdmTXClockSource_Object = MibTableColumn
mdmTXClockSource = _MdmTXClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 14),
    _MdmTXClockSource_Type()
)
mdmTXClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTXClockSource.setStatus("mandatory")


class _MdmRTSCTSDelay_Type(Integer32):
    """Custom type mdmRTSCTSDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmRTSCTSDelay_Type.__name__ = "Integer32"
_MdmRTSCTSDelay_Object = MibTableColumn
mdmRTSCTSDelay = _MdmRTSCTSDelay_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 15),
    _MdmRTSCTSDelay_Type()
)
mdmRTSCTSDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmRTSCTSDelay.setStatus("mandatory")


class _MdmCarriageReturnCharacter_Type(Integer32):
    """Custom type mdmCarriageReturnCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MdmCarriageReturnCharacter_Type.__name__ = "Integer32"
_MdmCarriageReturnCharacter_Object = MibTableColumn
mdmCarriageReturnCharacter = _MdmCarriageReturnCharacter_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 16),
    _MdmCarriageReturnCharacter_Type()
)
mdmCarriageReturnCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCarriageReturnCharacter.setStatus("mandatory")


class _MdmCharacterAbortDialing_Type(Integer32):
    """Custom type mdmCharacterAbortDialing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MdmCharacterAbortDialing_Type.__name__ = "Integer32"
_MdmCharacterAbortDialing_Object = MibTableColumn
mdmCharacterAbortDialing = _MdmCharacterAbortDialing_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 17),
    _MdmCharacterAbortDialing_Type()
)
mdmCharacterAbortDialing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCharacterAbortDialing.setStatus("mandatory")


class _MdmDelayDTR_Type(Integer32):
    """Custom type mdmDelayDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmDelayDTR_Type.__name__ = "Integer32"
_MdmDelayDTR_Object = MibTableColumn
mdmDelayDTR = _MdmDelayDTR_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 18),
    _MdmDelayDTR_Type()
)
mdmDelayDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDelayDTR.setStatus("mandatory")


class _MdmEscapeCharacter_Type(Integer32):
    """Custom type mdmEscapeCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MdmEscapeCharacter_Type.__name__ = "Integer32"
_MdmEscapeCharacter_Object = MibTableColumn
mdmEscapeCharacter = _MdmEscapeCharacter_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 19),
    _MdmEscapeCharacter_Type()
)
mdmEscapeCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmEscapeCharacter.setStatus("mandatory")


class _MdmLineFeedCharacter_Type(Integer32):
    """Custom type mdmLineFeedCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MdmLineFeedCharacter_Type.__name__ = "Integer32"
_MdmLineFeedCharacter_Object = MibTableColumn
mdmLineFeedCharacter = _MdmLineFeedCharacter_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 20),
    _MdmLineFeedCharacter_Type()
)
mdmLineFeedCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLineFeedCharacter.setStatus("mandatory")


class _MdmHangUpDelay_Type(Integer32):
    """Custom type mdmHangUpDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmHangUpDelay_Type.__name__ = "Integer32"
_MdmHangUpDelay_Object = MibTableColumn
mdmHangUpDelay = _MdmHangUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 21),
    _MdmHangUpDelay_Type()
)
mdmHangUpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmHangUpDelay.setStatus("mandatory")


class _MdmEscapeCharacterGuardTime_Type(Integer32):
    """Custom type mdmEscapeCharacterGuardTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmEscapeCharacterGuardTime_Type.__name__ = "Integer32"
_MdmEscapeCharacterGuardTime_Object = MibTableColumn
mdmEscapeCharacterGuardTime = _MdmEscapeCharacterGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 22),
    _MdmEscapeCharacterGuardTime_Type()
)
mdmEscapeCharacterGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmEscapeCharacterGuardTime.setStatus("mandatory")


class _MdmOperatingMode_Type(Integer32):
    """Custom type mdmOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asyncCmdsyncData", 2),
          ("asyncDataMode", 1))
    )


_MdmOperatingMode_Type.__name__ = "Integer32"
_MdmOperatingMode_Object = MibTableColumn
mdmOperatingMode = _MdmOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 23),
    _MdmOperatingMode_Type()
)
mdmOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmOperatingMode.setStatus("mandatory")


class _MdmBackSpaceCharacter_Type(Integer32):
    """Custom type mdmBackSpaceCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MdmBackSpaceCharacter_Type.__name__ = "Integer32"
_MdmBackSpaceCharacter_Object = MibTableColumn
mdmBackSpaceCharacter = _MdmBackSpaceCharacter_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 2, 1, 24),
    _MdmBackSpaceCharacter_Type()
)
mdmBackSpaceCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmBackSpaceCharacter.setStatus("mandatory")
_MdmModemConfigTable_Object = MibTable
mdmModemConfigTable = _MdmModemConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3)
)
if mibBuilder.loadTexts:
    mdmModemConfigTable.setStatus("mandatory")
_MdmModemEntry_Object = MibTableRow
mdmModemEntry = _MdmModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1)
)
mdmModemEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmModemIndex"),
)
if mibBuilder.loadTexts:
    mdmModemEntry.setStatus("mandatory")
_MdmModemIndex_Type = SCinstance
_MdmModemIndex_Object = MibTableColumn
mdmModemIndex = _MdmModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1, 1),
    _MdmModemIndex_Type()
)
mdmModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModemIndex.setStatus("mandatory")


class _MdmRingsToAns_Type(Integer32):
    """Custom type mdmRingsToAns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmRingsToAns_Type.__name__ = "Integer32"
_MdmRingsToAns_Object = MibTableColumn
mdmRingsToAns = _MdmRingsToAns_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1, 2),
    _MdmRingsToAns_Type()
)
mdmRingsToAns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmRingsToAns.setStatus("mandatory")


class _MdmFallFwrdBack_Type(Integer32):
    """Custom type mdmFallFwrdBack based on Integer32"""
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


_MdmFallFwrdBack_Type.__name__ = "Integer32"
_MdmFallFwrdBack_Object = MibTableColumn
mdmFallFwrdBack = _MdmFallFwrdBack_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1, 3),
    _MdmFallFwrdBack_Type()
)
mdmFallFwrdBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmFallFwrdBack.setStatus("mandatory")


class _MdmTrellis_Type(Integer32):
    """Custom type mdmTrellis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MdmTrellis_Type.__name__ = "Integer32"
_MdmTrellis_Object = MibTableColumn
mdmTrellis = _MdmTrellis_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1, 4),
    _MdmTrellis_Type()
)
mdmTrellis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTrellis.setStatus("mandatory")


class _MdmSQRetrain_Type(Integer32):
    """Custom type mdmSQRetrain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sQForever", 3),
          ("sQThree", 2))
    )


_MdmSQRetrain_Type.__name__ = "Integer32"
_MdmSQRetrain_Object = MibTableColumn
mdmSQRetrain = _MdmSQRetrain_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1, 5),
    _MdmSQRetrain_Type()
)
mdmSQRetrain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmSQRetrain.setStatus("mandatory")


class _MdmLongSpaceDisc_Type(Integer32):
    """Custom type mdmLongSpaceDisc based on Integer32"""
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


_MdmLongSpaceDisc_Type.__name__ = "Integer32"
_MdmLongSpaceDisc_Object = MibTableColumn
mdmLongSpaceDisc = _MdmLongSpaceDisc_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1, 6),
    _MdmLongSpaceDisc_Type()
)
mdmLongSpaceDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLongSpaceDisc.setStatus("mandatory")


class _MdmMakeBusy_Type(Integer32):
    """Custom type mdmMakeBusy based on Integer32"""
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
        *(("disabled", 1),
          ("inAL", 3),
          ("inALorLossRTSorDTR", 4),
          ("onLossDTR", 2),
          ("onLossRTS", 5))
    )


_MdmMakeBusy_Type.__name__ = "Integer32"
_MdmMakeBusy_Object = MibTableColumn
mdmMakeBusy = _MdmMakeBusy_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1, 7),
    _MdmMakeBusy_Type()
)
mdmMakeBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmMakeBusy.setStatus("mandatory")


class _MdmRDLOptions_Type(Integer32):
    """Custom type mdmRDLOptions based on Integer32"""
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


_MdmRDLOptions_Type.__name__ = "Integer32"
_MdmRDLOptions_Object = MibTableColumn
mdmRDLOptions = _MdmRDLOptions_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1, 8),
    _MdmRDLOptions_Type()
)
mdmRDLOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmRDLOptions.setStatus("mandatory")


class _MdmTestTimer_Type(Integer32):
    """Custom type mdmTestTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmTestTimer_Type.__name__ = "Integer32"
_MdmTestTimer_Object = MibTableColumn
mdmTestTimer = _MdmTestTimer_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1, 9),
    _MdmTestTimer_Type()
)
mdmTestTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTestTimer.setStatus("mandatory")


class _MdmDTETestCntrl_Type(Integer32):
    """Custom type mdmDTETestCntrl based on Integer32"""
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


_MdmDTETestCntrl_Type.__name__ = "Integer32"
_MdmDTETestCntrl_Object = MibTableColumn
mdmDTETestCntrl = _MdmDTETestCntrl_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1, 10),
    _MdmDTETestCntrl_Type()
)
mdmDTETestCntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDTETestCntrl.setStatus("mandatory")


class _MdmDCDLossDisc_Type(Integer32):
    """Custom type mdmDCDLossDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmDCDLossDisc_Type.__name__ = "Integer32"
_MdmDCDLossDisc_Object = MibTableColumn
mdmDCDLossDisc = _MdmDCDLossDisc_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1, 11),
    _MdmDCDLossDisc_Type()
)
mdmDCDLossDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDCDLossDisc.setStatus("mandatory")


class _MdmCDRespTime_Type(Integer32):
    """Custom type mdmCDRespTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmCDRespTime_Type.__name__ = "Integer32"
_MdmCDRespTime_Object = MibTableColumn
mdmCDRespTime = _MdmCDRespTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1, 12),
    _MdmCDRespTime_Type()
)
mdmCDRespTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCDRespTime.setStatus("mandatory")


class _MdmAnswerOriginate_Type(Integer32):
    """Custom type mdmAnswerOriginate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("answerIfRingDetect", 1),
          ("autoAnswerInOriginate", 3),
          ("forceAnswer", 2))
    )


_MdmAnswerOriginate_Type.__name__ = "Integer32"
_MdmAnswerOriginate_Object = MibTableColumn
mdmAnswerOriginate = _MdmAnswerOriginate_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1, 13),
    _MdmAnswerOriginate_Type()
)
mdmAnswerOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmAnswerOriginate.setStatus("mandatory")


class _MdmWaitForDCD_Type(Integer32):
    """Custom type mdmWaitForDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_MdmWaitForDCD_Type.__name__ = "Integer32"
_MdmWaitForDCD_Object = MibTableColumn
mdmWaitForDCD = _MdmWaitForDCD_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 3, 1, 14),
    _MdmWaitForDCD_Type()
)
mdmWaitForDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmWaitForDCD.setStatus("mandatory")
_MdmDialerConfigTable_Object = MibTable
mdmDialerConfigTable = _MdmDialerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 4)
)
if mibBuilder.loadTexts:
    mdmDialerConfigTable.setStatus("mandatory")
_MdmDialerEntry_Object = MibTableRow
mdmDialerEntry = _MdmDialerEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 4, 1)
)
mdmDialerEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmDialerIndex"),
)
if mibBuilder.loadTexts:
    mdmDialerEntry.setStatus("mandatory")
_MdmDialerIndex_Type = SCinstance
_MdmDialerIndex_Object = MibTableColumn
mdmDialerIndex = _MdmDialerIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 4, 1, 1),
    _MdmDialerIndex_Type()
)
mdmDialerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDialerIndex.setStatus("mandatory")


class _MdmCPMMonitor_Type(Integer32):
    """Custom type mdmCPMMonitor based on Integer32"""
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
        *(("basic", 1),
          ("extendedBusy", 4),
          ("extendedDialtone", 3),
          ("extendedFullCPM", 5),
          ("extendedFullCPMRingback", 6),
          ("extendedNoCPM", 2))
    )


_MdmCPMMonitor_Type.__name__ = "Integer32"
_MdmCPMMonitor_Object = MibTableColumn
mdmCPMMonitor = _MdmCPMMonitor_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 4, 1, 2),
    _MdmCPMMonitor_Type()
)
mdmCPMMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCPMMonitor.setStatus("mandatory")


class _MdmParserSelection_Type(Integer32):
    """Custom type mdmParserSelection based on Integer32"""
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
        *(("at", 1),
          ("noparser", 5),
          ("v25HDLC", 3),
          ("v25async", 2),
          ("v25bisync", 4))
    )


_MdmParserSelection_Type.__name__ = "Integer32"
_MdmParserSelection_Object = MibTableColumn
mdmParserSelection = _MdmParserSelection_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 4, 1, 3),
    _MdmParserSelection_Type()
)
mdmParserSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmParserSelection.setStatus("mandatory")


class _MdmDTRDial_Type(Integer32):
    """Custom type mdmDTRDial based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("cellNumber0", 2),
          ("cellNumber1", 3),
          ("cellNumber2", 4),
          ("cellNumber3", 5),
          ("cellNumber4", 6),
          ("cellNumber5", 7),
          ("cellNumber6", 8),
          ("cellNumber7", 9),
          ("cellNumber8", 10),
          ("cellNumber9", 11),
          ("disable", 1),
          ("talkData", 12))
    )


_MdmDTRDial_Type.__name__ = "Integer32"
_MdmDTRDial_Object = MibTableColumn
mdmDTRDial = _MdmDTRDial_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 4, 1, 4),
    _MdmDTRDial_Type()
)
mdmDTRDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDTRDial.setStatus("mandatory")


class _MdmDialType_Type(Integer32):
    """Custom type mdmDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 2),
          ("pulse", 1))
    )


_MdmDialType_Type.__name__ = "Integer32"
_MdmDialType_Object = MibTableColumn
mdmDialType = _MdmDialType_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 4, 1, 5),
    _MdmDialType_Type()
)
mdmDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDialType.setStatus("mandatory")


class _MdmResponseMode_Type(Integer32):
    """Custom type mdmResponseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enableInOriginate", 3),
          ("enabled", 1))
    )


_MdmResponseMode_Type.__name__ = "Integer32"
_MdmResponseMode_Object = MibTableColumn
mdmResponseMode = _MdmResponseMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 4, 1, 6),
    _MdmResponseMode_Type()
)
mdmResponseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmResponseMode.setStatus("mandatory")


class _MdmResponseType_Type(Integer32):
    """Custom type mdmResponseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alpha", 2),
          ("numeric", 1))
    )


_MdmResponseType_Type.__name__ = "Integer32"
_MdmResponseType_Object = MibTableColumn
mdmResponseType = _MdmResponseType_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 4, 1, 7),
    _MdmResponseType_Type()
)
mdmResponseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmResponseType.setStatus("mandatory")


class _MdmPauseTime_Type(Integer32):
    """Custom type mdmPauseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmPauseTime_Type.__name__ = "Integer32"
_MdmPauseTime_Object = MibTableColumn
mdmPauseTime = _MdmPauseTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 4, 1, 8),
    _MdmPauseTime_Type()
)
mdmPauseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmPauseTime.setStatus("mandatory")


class _MdmWaitForDialtoneTime_Type(Integer32):
    """Custom type mdmWaitForDialtoneTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmWaitForDialtoneTime_Type.__name__ = "Integer32"
_MdmWaitForDialtoneTime_Object = MibTableColumn
mdmWaitForDialtoneTime = _MdmWaitForDialtoneTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 4, 1, 9),
    _MdmWaitForDialtoneTime_Type()
)
mdmWaitForDialtoneTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmWaitForDialtoneTime.setStatus("mandatory")
_MdmProtocolConfigTable_Object = MibTable
mdmProtocolConfigTable = _MdmProtocolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 5)
)
if mibBuilder.loadTexts:
    mdmProtocolConfigTable.setStatus("mandatory")
_MdmProtocolEntry_Object = MibTableRow
mdmProtocolEntry = _MdmProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 5, 1)
)
mdmProtocolEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmProtocolIndex"),
)
if mibBuilder.loadTexts:
    mdmProtocolEntry.setStatus("mandatory")
_MdmProtocolIndex_Type = SCinstance
_MdmProtocolIndex_Object = MibTableColumn
mdmProtocolIndex = _MdmProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 5, 1, 1),
    _MdmProtocolIndex_Type()
)
mdmProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmProtocolIndex.setStatus("mandatory")


class _MdmCompression_Type(Integer32):
    """Custom type mdmCompression based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("rxpathonly", 4),
          ("txpathonly", 3))
    )


_MdmCompression_Type.__name__ = "Integer32"
_MdmCompression_Object = MibTableColumn
mdmCompression = _MdmCompression_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 5, 1, 2),
    _MdmCompression_Type()
)
mdmCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCompression.setStatus("mandatory")


class _MdmAsyncProtocol_Type(Integer32):
    """Custom type mdmAsyncProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("autoreliable", 4),
          ("direct", 2),
          ("mnpreliable", 3),
          ("reliableLAPMorMNP", 6),
          ("v13", 7),
          ("v42reliable", 5),
          ("wire", 1))
    )


_MdmAsyncProtocol_Type.__name__ = "Integer32"
_MdmAsyncProtocol_Object = MibTableColumn
mdmAsyncProtocol = _MdmAsyncProtocol_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 5, 1, 3),
    _MdmAsyncProtocol_Type()
)
mdmAsyncProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmAsyncProtocol.setStatus("mandatory")


class _MdmFlowControl_Type(Integer32):
    """Custom type mdmFlowControl based on Integer32"""
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
        *(("bidirectional", 4),
          ("disabled", 1),
          ("enabled", 2),
          ("unidirectional", 3))
    )


_MdmFlowControl_Type.__name__ = "Integer32"
_MdmFlowControl_Object = MibTableColumn
mdmFlowControl = _MdmFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 5, 1, 4),
    _MdmFlowControl_Type()
)
mdmFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmFlowControl.setStatus("mandatory")


class _MdmBreakHandling_Type(Integer32):
    """Custom type mdmBreakHandling based on Integer32"""
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
        *(("expediteDest", 1),
          ("expediteNonDest", 2),
          ("ignored", 4),
          ("nonExpediteNonDest", 3),
          ("timedNonExpediteNonDest", 5),
          ("timedNonExpediteNonDest2", 6))
    )


_MdmBreakHandling_Type.__name__ = "Integer32"
_MdmBreakHandling_Object = MibTableColumn
mdmBreakHandling = _MdmBreakHandling_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 5, 1, 5),
    _MdmBreakHandling_Type()
)
mdmBreakHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmBreakHandling.setStatus("mandatory")


class _MdmConnAndLinkMessages_Type(Integer32):
    """Custom type mdmConnAndLinkMessages based on Integer32"""
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
        *(("bothAfterLink", 2),
          ("connectAfterLink", 4),
          ("microcomCompatible", 3),
          ("separateMessages", 1))
    )


_MdmConnAndLinkMessages_Type.__name__ = "Integer32"
_MdmConnAndLinkMessages_Object = MibTableColumn
mdmConnAndLinkMessages = _MdmConnAndLinkMessages_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 5, 1, 6),
    _MdmConnAndLinkMessages_Type()
)
mdmConnAndLinkMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmConnAndLinkMessages.setStatus("mandatory")


class _MdmErrorCorrection_Type(Integer32):
    """Custom type mdmErrorCorrection based on Integer32"""
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
        *(("bufferRxData", 2),
          ("fallbackV14Buffer", 4),
          ("fallbackV14WithFallbackChar", 5),
          ("fallbackWithFallbackChar", 3),
          ("noBuffer", 1))
    )


_MdmErrorCorrection_Type.__name__ = "Integer32"
_MdmErrorCorrection_Object = MibTableColumn
mdmErrorCorrection = _MdmErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 5, 1, 7),
    _MdmErrorCorrection_Type()
)
mdmErrorCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmErrorCorrection.setStatus("mandatory")


class _MdmV13Mode_Type(Integer32):
    """Custom type mdmV13Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("rxEnable", 3),
          ("txEnable", 2))
    )


_MdmV13Mode_Type.__name__ = "Integer32"
_MdmV13Mode_Object = MibTableColumn
mdmV13Mode = _MdmV13Mode_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 5, 1, 8),
    _MdmV13Mode_Type()
)
mdmV13Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmV13Mode.setStatus("mandatory")


class _MdmSyncProtocol_Type(Integer32):
    """Custom type mdmSyncProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalsync", 1),
          ("v13sync", 2))
    )


_MdmSyncProtocol_Type.__name__ = "Integer32"
_MdmSyncProtocol_Object = MibTableColumn
mdmSyncProtocol = _MdmSyncProtocol_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 5, 1, 9),
    _MdmSyncProtocol_Type()
)
mdmSyncProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmSyncProtocol.setStatus("mandatory")


class _MdmFrameRetransLimit_Type(Integer32):
    """Custom type mdmFrameRetransLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmFrameRetransLimit_Type.__name__ = "Integer32"
_MdmFrameRetransLimit_Object = MibTableColumn
mdmFrameRetransLimit = _MdmFrameRetransLimit_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 5, 1, 10),
    _MdmFrameRetransLimit_Type()
)
mdmFrameRetransLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmFrameRetransLimit.setStatus("mandatory")
_MdmPrivateLineConfigTable_Object = MibTable
mdmPrivateLineConfigTable = _MdmPrivateLineConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 6)
)
if mibBuilder.loadTexts:
    mdmPrivateLineConfigTable.setStatus("mandatory")
_MdmPrivateLineEntry_Object = MibTableRow
mdmPrivateLineEntry = _MdmPrivateLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 6, 1)
)
mdmPrivateLineEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmPrivateLineIndex"),
)
if mibBuilder.loadTexts:
    mdmPrivateLineEntry.setStatus("mandatory")
_MdmPrivateLineIndex_Type = SCinstance
_MdmPrivateLineIndex_Object = MibTableColumn
mdmPrivateLineIndex = _MdmPrivateLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 6, 1, 1),
    _MdmPrivateLineIndex_Type()
)
mdmPrivateLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPrivateLineIndex.setStatus("mandatory")


class _MdmPrivateLineTxLevel_Type(Integer32):
    """Custom type mdmPrivateLineTxLevel based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("dBm0", 1),
          ("dBm1", 2),
          ("dBm10", 11),
          ("dBm11", 12),
          ("dBm12", 13),
          ("dBm13", 14),
          ("dBm14", 15),
          ("dBm15", 16),
          ("dBm2", 3),
          ("dBm3", 4),
          ("dBm4", 5),
          ("dBm5", 6),
          ("dBm6", 7),
          ("dBm7", 8),
          ("dBm8", 9),
          ("dBm9", 10))
    )


_MdmPrivateLineTxLevel_Type.__name__ = "Integer32"
_MdmPrivateLineTxLevel_Object = MibTableColumn
mdmPrivateLineTxLevel = _MdmPrivateLineTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 6, 1, 2),
    _MdmPrivateLineTxLevel_Type()
)
mdmPrivateLineTxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmPrivateLineTxLevel.setStatus("mandatory")


class _MdmPrivateLineHandshakeMode_Type(Integer32):
    """Custom type mdmPrivateLineHandshakeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gdcVfastonly", 1),
          ("v32bisonly", 2),
          ("v32only", 3))
    )


_MdmPrivateLineHandshakeMode_Type.__name__ = "Integer32"
_MdmPrivateLineHandshakeMode_Object = MibTableColumn
mdmPrivateLineHandshakeMode = _MdmPrivateLineHandshakeMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 6, 1, 3),
    _MdmPrivateLineHandshakeMode_Type()
)
mdmPrivateLineHandshakeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmPrivateLineHandshakeMode.setStatus("mandatory")


class _MdmAutoDialRestoral_Type(Integer32):
    """Custom type mdmAutoDialRestoral based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enableWithEndOfSession", 2),
          ("enableWithoutEndOfSession", 3))
    )


_MdmAutoDialRestoral_Type.__name__ = "Integer32"
_MdmAutoDialRestoral_Object = MibTableColumn
mdmAutoDialRestoral = _MdmAutoDialRestoral_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 6, 1, 4),
    _MdmAutoDialRestoral_Type()
)
mdmAutoDialRestoral.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmAutoDialRestoral.setStatus("mandatory")


class _MdmPrivateLineDownTime_Type(Integer32):
    """Custom type mdmPrivateLineDownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmPrivateLineDownTime_Type.__name__ = "Integer32"
_MdmPrivateLineDownTime_Object = MibTableColumn
mdmPrivateLineDownTime = _MdmPrivateLineDownTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 6, 1, 5),
    _MdmPrivateLineDownTime_Type()
)
mdmPrivateLineDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmPrivateLineDownTime.setStatus("mandatory")


class _MdmDBUtoPLLookbackTime_Type(Integer32):
    """Custom type mdmDBUtoPLLookbackTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmDBUtoPLLookbackTime_Type.__name__ = "Integer32"
_MdmDBUtoPLLookbackTime_Object = MibTableColumn
mdmDBUtoPLLookbackTime = _MdmDBUtoPLLookbackTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 6, 1, 6),
    _MdmDBUtoPLLookbackTime_Type()
)
mdmDBUtoPLLookbackTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDBUtoPLLookbackTime.setStatus("mandatory")
_MdmAlarmScanTable_Object = MibTable
mdmAlarmScanTable = _MdmAlarmScanTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 7)
)
if mibBuilder.loadTexts:
    mdmAlarmScanTable.setStatus("mandatory")
_MdmAlarmScanEntry_Object = MibTableRow
mdmAlarmScanEntry = _MdmAlarmScanEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 7, 1)
)
mdmAlarmScanEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmAlarmScanIndex"),
)
if mibBuilder.loadTexts:
    mdmAlarmScanEntry.setStatus("mandatory")
_MdmAlarmScanIndex_Type = SCinstance
_MdmAlarmScanIndex_Object = MibTableColumn
mdmAlarmScanIndex = _MdmAlarmScanIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 7, 1, 1),
    _MdmAlarmScanIndex_Type()
)
mdmAlarmScanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmAlarmScanIndex.setStatus("mandatory")


class _MdmAlarmScan_Type(OctetString):
    """Custom type mdmAlarmScan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MdmAlarmScan_Type.__name__ = "OctetString"
_MdmAlarmScan_Object = MibTableColumn
mdmAlarmScan = _MdmAlarmScan_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 7, 1, 2),
    _MdmAlarmScan_Type()
)
mdmAlarmScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmAlarmScan.setStatus("mandatory")


class _MdmResetSelfPowerBit_Type(Integer32):
    """Custom type mdmResetSelfPowerBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_MdmResetSelfPowerBit_Type.__name__ = "Integer32"
_MdmResetSelfPowerBit_Object = MibTableColumn
mdmResetSelfPowerBit = _MdmResetSelfPowerBit_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 7, 1, 3),
    _MdmResetSelfPowerBit_Type()
)
mdmResetSelfPowerBit.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mdmResetSelfPowerBit.setStatus("mandatory")
_MdmMaskAlarmTable_Object = MibTable
mdmMaskAlarmTable = _MdmMaskAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8)
)
if mibBuilder.loadTexts:
    mdmMaskAlarmTable.setStatus("mandatory")
_MdmMaskAlarmEntry_Object = MibTableRow
mdmMaskAlarmEntry = _MdmMaskAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1)
)
mdmMaskAlarmEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmMaskAlarmIndex"),
)
if mibBuilder.loadTexts:
    mdmMaskAlarmEntry.setStatus("mandatory")
_MdmMaskAlarmIndex_Type = SCinstance
_MdmMaskAlarmIndex_Object = MibTableColumn
mdmMaskAlarmIndex = _MdmMaskAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 1),
    _MdmMaskAlarmIndex_Type()
)
mdmMaskAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmMaskAlarmIndex.setStatus("mandatory")


class _MdmDTRLoss_Type(Integer32):
    """Custom type mdmDTRLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_MdmDTRLoss_Type.__name__ = "Integer32"
_MdmDTRLoss_Object = MibTableColumn
mdmDTRLoss = _MdmDTRLoss_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 2),
    _MdmDTRLoss_Type()
)
mdmDTRLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDTRLoss.setStatus("mandatory")


class _MdmFallback_Type(Integer32):
    """Custom type mdmFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_MdmFallback_Type.__name__ = "Integer32"
_MdmFallback_Object = MibTableColumn
mdmFallback = _MdmFallback_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 3),
    _MdmFallback_Type()
)
mdmFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmFallback.setStatus("mandatory")


class _MdmRxdTran_Type(Integer32):
    """Custom type mdmRxdTran based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_MdmRxdTran_Type.__name__ = "Integer32"
_MdmRxdTran_Object = MibTableColumn
mdmRxdTran = _MdmRxdTran_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 4),
    _MdmRxdTran_Type()
)
mdmRxdTran.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmRxdTran.setStatus("mandatory")


class _MdmTxdTran_Type(Integer32):
    """Custom type mdmTxdTran based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_MdmTxdTran_Type.__name__ = "Integer32"
_MdmTxdTran_Object = MibTableColumn
mdmTxdTran = _MdmTxdTran_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 5),
    _MdmTxdTran_Type()
)
mdmTxdTran.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTxdTran.setStatus("mandatory")


class _MdmDCDLoss_Type(Integer32):
    """Custom type mdmDCDLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_MdmDCDLoss_Type.__name__ = "Integer32"
_MdmDCDLoss_Object = MibTableColumn
mdmDCDLoss = _MdmDCDLoss_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 6),
    _MdmDCDLoss_Type()
)
mdmDCDLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDCDLoss.setStatus("mandatory")


class _MdmRingNoAnswer_Type(Integer32):
    """Custom type mdmRingNoAnswer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_MdmRingNoAnswer_Type.__name__ = "Integer32"
_MdmRingNoAnswer_Object = MibTableColumn
mdmRingNoAnswer = _MdmRingNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 7),
    _MdmRingNoAnswer_Type()
)
mdmRingNoAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmRingNoAnswer.setStatus("mandatory")


class _MdmRetrain_Type(Integer32):
    """Custom type mdmRetrain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_MdmRetrain_Type.__name__ = "Integer32"
_MdmRetrain_Object = MibTableColumn
mdmRetrain = _MdmRetrain_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 8),
    _MdmRetrain_Type()
)
mdmRetrain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmRetrain.setStatus("mandatory")


class _MdmCallLength_Type(Integer32):
    """Custom type mdmCallLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_MdmCallLength_Type.__name__ = "Integer32"
_MdmCallLength_Object = MibTableColumn
mdmCallLength = _MdmCallLength_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 9),
    _MdmCallLength_Type()
)
mdmCallLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCallLength.setStatus("mandatory")


class _MdmCallFail_Type(Integer32):
    """Custom type mdmCallFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_MdmCallFail_Type.__name__ = "Integer32"
_MdmCallFail_Object = MibTableColumn
mdmCallFail = _MdmCallFail_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 10),
    _MdmCallFail_Type()
)
mdmCallFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCallFail.setStatus("mandatory")


class _MdmConfigErr_Type(Integer32):
    """Custom type mdmConfigErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_MdmConfigErr_Type.__name__ = "Integer32"
_MdmConfigErr_Object = MibTableColumn
mdmConfigErr = _MdmConfigErr_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 11),
    _MdmConfigErr_Type()
)
mdmConfigErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmConfigErr.setStatus("mandatory")


class _MdmSignalQuality_Type(Integer32):
    """Custom type mdmSignalQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_MdmSignalQuality_Type.__name__ = "Integer32"
_MdmSignalQuality_Object = MibTableColumn
mdmSignalQuality = _MdmSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 12),
    _MdmSignalQuality_Type()
)
mdmSignalQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmSignalQuality.setStatus("mandatory")


class _MdmOnDBU_Type(Integer32):
    """Custom type mdmOnDBU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_MdmOnDBU_Type.__name__ = "Integer32"
_MdmOnDBU_Object = MibTableColumn
mdmOnDBU = _MdmOnDBU_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 13),
    _MdmOnDBU_Type()
)
mdmOnDBU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmOnDBU.setStatus("mandatory")


class _MdmRemoteConfigMask_Type(Integer32):
    """Custom type mdmRemoteConfigMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_MdmRemoteConfigMask_Type.__name__ = "Integer32"
_MdmRemoteConfigMask_Object = MibTableColumn
mdmRemoteConfigMask = _MdmRemoteConfigMask_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 14),
    _MdmRemoteConfigMask_Type()
)
mdmRemoteConfigMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmRemoteConfigMask.setStatus("mandatory")


class _MdmTestTimeout_Type(Integer32):
    """Custom type mdmTestTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mask", 1),
          ("unmask", 2))
    )


_MdmTestTimeout_Type.__name__ = "Integer32"
_MdmTestTimeout_Object = MibTableColumn
mdmTestTimeout = _MdmTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 8, 1, 15),
    _MdmTestTimeout_Type()
)
mdmTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTestTimeout.setStatus("mandatory")
_MdmThresholdsTable_Object = MibTable
mdmThresholdsTable = _MdmThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 9)
)
if mibBuilder.loadTexts:
    mdmThresholdsTable.setStatus("mandatory")
_MdmThresholdsEntry_Object = MibTableRow
mdmThresholdsEntry = _MdmThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 9, 1)
)
mdmThresholdsEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmThresholdsIndex"),
)
if mibBuilder.loadTexts:
    mdmThresholdsEntry.setStatus("mandatory")
_MdmThresholdsIndex_Type = SCinstance
_MdmThresholdsIndex_Object = MibTableColumn
mdmThresholdsIndex = _MdmThresholdsIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 9, 1, 1),
    _MdmThresholdsIndex_Type()
)
mdmThresholdsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmThresholdsIndex.setStatus("mandatory")
_MdmCallDuration_Type = TimeTicks
_MdmCallDuration_Object = MibTableColumn
mdmCallDuration = _MdmCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 9, 1, 2),
    _MdmCallDuration_Type()
)
mdmCallDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCallDuration.setStatus("mandatory")


class _MdmRetrainThreshold_Type(Integer32):
    """Custom type mdmRetrainThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmRetrainThreshold_Type.__name__ = "Integer32"
_MdmRetrainThreshold_Object = MibTableColumn
mdmRetrainThreshold = _MdmRetrainThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 9, 1, 3),
    _MdmRetrainThreshold_Type()
)
mdmRetrainThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmRetrainThreshold.setStatus("mandatory")
_MdmStatusTable_Object = MibTable
mdmStatusTable = _MdmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10)
)
if mibBuilder.loadTexts:
    mdmStatusTable.setStatus("mandatory")
_MdmStatusEntry_Object = MibTableRow
mdmStatusEntry = _MdmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1)
)
mdmStatusEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmStatusIndex"),
)
if mibBuilder.loadTexts:
    mdmStatusEntry.setStatus("mandatory")
_MdmStatusIndex_Type = SCinstance
_MdmStatusIndex_Object = MibTableColumn
mdmStatusIndex = _MdmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 1),
    _MdmStatusIndex_Type()
)
mdmStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatusIndex.setStatus("mandatory")


class _MdmPLLookbackStatus_Type(Integer32):
    """Custom type mdmPLLookbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_MdmPLLookbackStatus_Type.__name__ = "Integer32"
_MdmPLLookbackStatus_Object = MibTableColumn
mdmPLLookbackStatus = _MdmPLLookbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 2),
    _MdmPLLookbackStatus_Type()
)
mdmPLLookbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPLLookbackStatus.setStatus("mandatory")


class _MdmAutoDialRestoralStatus_Type(Integer32):
    """Custom type mdmAutoDialRestoralStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_MdmAutoDialRestoralStatus_Type.__name__ = "Integer32"
_MdmAutoDialRestoralStatus_Object = MibTableColumn
mdmAutoDialRestoralStatus = _MdmAutoDialRestoralStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 3),
    _MdmAutoDialRestoralStatus_Type()
)
mdmAutoDialRestoralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmAutoDialRestoralStatus.setStatus("mandatory")


class _MdmTXDtransitions_Type(Integer32):
    """Custom type mdmTXDtransitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notransition", 1),
          ("transition", 2))
    )


_MdmTXDtransitions_Type.__name__ = "Integer32"
_MdmTXDtransitions_Object = MibTableColumn
mdmTXDtransitions = _MdmTXDtransitions_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 4),
    _MdmTXDtransitions_Type()
)
mdmTXDtransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTXDtransitions.setStatus("mandatory")


class _MdmRXDtransitions_Type(Integer32):
    """Custom type mdmRXDtransitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notransition", 1),
          ("transition", 2))
    )


_MdmRXDtransitions_Type.__name__ = "Integer32"
_MdmRXDtransitions_Object = MibTableColumn
mdmRXDtransitions = _MdmRXDtransitions_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 5),
    _MdmRXDtransitions_Type()
)
mdmRXDtransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRXDtransitions.setStatus("mandatory")


class _MdmRTStransitions_Type(Integer32):
    """Custom type mdmRTStransitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notransition", 1),
          ("transition", 2))
    )


_MdmRTStransitions_Type.__name__ = "Integer32"
_MdmRTStransitions_Object = MibTableColumn
mdmRTStransitions = _MdmRTStransitions_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 6),
    _MdmRTStransitions_Type()
)
mdmRTStransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRTStransitions.setStatus("mandatory")


class _MdmDTRtransitions_Type(Integer32):
    """Custom type mdmDTRtransitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notransition", 1),
          ("transition", 2))
    )


_MdmDTRtransitions_Type.__name__ = "Integer32"
_MdmDTRtransitions_Object = MibTableColumn
mdmDTRtransitions = _MdmDTRtransitions_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 7),
    _MdmDTRtransitions_Type()
)
mdmDTRtransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDTRtransitions.setStatus("mandatory")


class _MdmDCDtransitions_Type(Integer32):
    """Custom type mdmDCDtransitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notransition", 1),
          ("transition", 2))
    )


_MdmDCDtransitions_Type.__name__ = "Integer32"
_MdmDCDtransitions_Object = MibTableColumn
mdmDCDtransitions = _MdmDCDtransitions_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 8),
    _MdmDCDtransitions_Type()
)
mdmDCDtransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDCDtransitions.setStatus("mandatory")


class _MdmTXCLKtransitions_Type(Integer32):
    """Custom type mdmTXCLKtransitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notransition", 1),
          ("transition", 2))
    )


_MdmTXCLKtransitions_Type.__name__ = "Integer32"
_MdmTXCLKtransitions_Object = MibTableColumn
mdmTXCLKtransitions = _MdmTXCLKtransitions_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 9),
    _MdmTXCLKtransitions_Type()
)
mdmTXCLKtransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTXCLKtransitions.setStatus("mandatory")


class _MdmDTR_Type(Integer32):
    """Custom type mdmDTR based on Integer32"""
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


_MdmDTR_Type.__name__ = "Integer32"
_MdmDTR_Object = MibTableColumn
mdmDTR = _MdmDTR_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 10),
    _MdmDTR_Type()
)
mdmDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDTR.setStatus("mandatory")


class _MdmCTS_Type(Integer32):
    """Custom type mdmCTS based on Integer32"""
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


_MdmCTS_Type.__name__ = "Integer32"
_MdmCTS_Object = MibTableColumn
mdmCTS = _MdmCTS_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 11),
    _MdmCTS_Type()
)
mdmCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCTS.setStatus("mandatory")


class _MdmDSR_Type(Integer32):
    """Custom type mdmDSR based on Integer32"""
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


_MdmDSR_Type.__name__ = "Integer32"
_MdmDSR_Object = MibTableColumn
mdmDSR = _MdmDSR_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 12),
    _MdmDSR_Type()
)
mdmDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDSR.setStatus("mandatory")


class _MdmDCD_Type(Integer32):
    """Custom type mdmDCD based on Integer32"""
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


_MdmDCD_Type.__name__ = "Integer32"
_MdmDCD_Object = MibTableColumn
mdmDCD = _MdmDCD_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 13),
    _MdmDCD_Type()
)
mdmDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDCD.setStatus("mandatory")


class _MdmSQM_Type(Integer32):
    """Custom type mdmSQM based on Integer32"""
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


_MdmSQM_Type.__name__ = "Integer32"
_MdmSQM_Object = MibTableColumn
mdmSQM = _MdmSQM_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 14),
    _MdmSQM_Type()
)
mdmSQM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmSQM.setStatus("mandatory")


class _MdmRTS_Type(Integer32):
    """Custom type mdmRTS based on Integer32"""
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


_MdmRTS_Type.__name__ = "Integer32"
_MdmRTS_Object = MibTableColumn
mdmRTS = _MdmRTS_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 15),
    _MdmRTS_Type()
)
mdmRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRTS.setStatus("mandatory")


class _MdmSwitchedPrivate_Type(Integer32):
    """Custom type mdmSwitchedPrivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("privateLine", 2),
          ("switchedNetwork", 1))
    )


_MdmSwitchedPrivate_Type.__name__ = "Integer32"
_MdmSwitchedPrivate_Object = MibTableColumn
mdmSwitchedPrivate = _MdmSwitchedPrivate_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 10, 1, 16),
    _MdmSwitchedPrivate_Type()
)
mdmSwitchedPrivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmSwitchedPrivate.setStatus("mandatory")
_MdmControlTable_Object = MibTable
mdmControlTable = _MdmControlTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 11)
)
if mibBuilder.loadTexts:
    mdmControlTable.setStatus("mandatory")
_MdmControlEntry_Object = MibTableRow
mdmControlEntry = _MdmControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 11, 1)
)
mdmControlEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmControlIndex"),
)
if mibBuilder.loadTexts:
    mdmControlEntry.setStatus("mandatory")
_MdmControlIndex_Type = SCinstance
_MdmControlIndex_Object = MibTableColumn
mdmControlIndex = _MdmControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 11, 1, 1),
    _MdmControlIndex_Type()
)
mdmControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmControlIndex.setStatus("mandatory")


class _MdmSoftReset_Type(Integer32):
    """Custom type mdmSoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_MdmSoftReset_Type.__name__ = "Integer32"
_MdmSoftReset_Object = MibTableColumn
mdmSoftReset = _MdmSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 11, 1, 2),
    _MdmSoftReset_Type()
)
mdmSoftReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mdmSoftReset.setStatus("mandatory")


class _MdmFrontPanel_Type(Integer32):
    """Custom type mdmFrontPanel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("inhibit", 1))
    )


_MdmFrontPanel_Type.__name__ = "Integer32"
_MdmFrontPanel_Object = MibTableColumn
mdmFrontPanel = _MdmFrontPanel_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 11, 1, 3),
    _MdmFrontPanel_Type()
)
mdmFrontPanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmFrontPanel.setStatus("mandatory")


class _MdmMakeClearBusy_Type(Integer32):
    """Custom type mdmMakeClearBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offHook", 2),
          ("onHook", 1))
    )


_MdmMakeClearBusy_Type.__name__ = "Integer32"
_MdmMakeClearBusy_Object = MibTableColumn
mdmMakeClearBusy = _MdmMakeClearBusy_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 11, 1, 4),
    _MdmMakeClearBusy_Type()
)
mdmMakeClearBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmMakeClearBusy.setStatus("mandatory")


class _MdmPLTalkData_Type(Integer32):
    """Custom type mdmPLTalkData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 2),
          ("idle", 1))
    )


_MdmPLTalkData_Type.__name__ = "Integer32"
_MdmPLTalkData_Object = MibTableColumn
mdmPLTalkData = _MdmPLTalkData_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 11, 1, 5),
    _MdmPLTalkData_Type()
)
mdmPLTalkData.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mdmPLTalkData.setStatus("mandatory")
_MdmWhatAreYouTable_Object = MibTable
mdmWhatAreYouTable = _MdmWhatAreYouTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 12)
)
if mibBuilder.loadTexts:
    mdmWhatAreYouTable.setStatus("mandatory")
_MdmWhatAreYouEntry_Object = MibTableRow
mdmWhatAreYouEntry = _MdmWhatAreYouEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 12, 1)
)
mdmWhatAreYouEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmWhatAreYouIndex"),
)
if mibBuilder.loadTexts:
    mdmWhatAreYouEntry.setStatus("mandatory")
_MdmWhatAreYouIndex_Type = SCinstance
_MdmWhatAreYouIndex_Object = MibTableColumn
mdmWhatAreYouIndex = _MdmWhatAreYouIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 12, 1, 1),
    _MdmWhatAreYouIndex_Type()
)
mdmWhatAreYouIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmWhatAreYouIndex.setStatus("mandatory")


class _MdmVFCard_Type(Integer32):
    """Custom type mdmVFCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              74,
              75,
              76,
              77,
              78,
              80,
              82,
              127)
        )
    )
    namedValues = NamedValues(
        *(("cardA", 65),
          ("cardB", 66),
          ("cardC", 67),
          ("cardD", 68),
          ("cardE", 69),
          ("cardF", 70),
          ("cardG", 71),
          ("cardH", 72),
          ("cardJ", 74),
          ("cardK", 75),
          ("cardL", 76),
          ("cardM", 77),
          ("cardN", 78),
          ("cardP", 80),
          ("cardR", 82),
          ("domestic", 1),
          ("noCard", 127))
    )


_MdmVFCard_Type.__name__ = "Integer32"
_MdmVFCard_Object = MibTableColumn
mdmVFCard = _MdmVFCard_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 12, 1, 2),
    _MdmVFCard_Type()
)
mdmVFCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmVFCard.setStatus("mandatory")


class _MdmDTECard_Type(Integer32):
    """Custom type mdmDTECard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eia232", 3),
          ("eia530", 2),
          ("v35", 1))
    )


_MdmDTECard_Type.__name__ = "Integer32"
_MdmDTECard_Object = MibTableColumn
mdmDTECard = _MdmDTECard_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 12, 1, 3),
    _MdmDTECard_Type()
)
mdmDTECard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDTECard.setStatus("mandatory")


class _MdmProductCode_Type(Integer32):
    """Custom type mdmProductCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            23
        )
    )
    namedValues = NamedValues(
        ("dmsVfast", 23)
    )


_MdmProductCode_Type.__name__ = "Integer32"
_MdmProductCode_Object = MibTableColumn
mdmProductCode = _MdmProductCode_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 12, 1, 4),
    _MdmProductCode_Type()
)
mdmProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmProductCode.setStatus("mandatory")


class _MdmCodeRev_Type(DisplayString):
    """Custom type mdmCodeRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MdmCodeRev_Type.__name__ = "DisplayString"
_MdmCodeRev_Object = MibTableColumn
mdmCodeRev = _MdmCodeRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 12, 1, 5),
    _MdmCodeRev_Type()
)
mdmCodeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCodeRev.setStatus("mandatory")


class _MdmBootRev_Type(DisplayString):
    """Custom type mdmBootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MdmBootRev_Type.__name__ = "DisplayString"
_MdmBootRev_Object = MibTableColumn
mdmBootRev = _MdmBootRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 12, 1, 6),
    _MdmBootRev_Type()
)
mdmBootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmBootRev.setStatus("mandatory")


class _MdmCountryCode_Type(DisplayString):
    """Custom type mdmCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_MdmCountryCode_Type.__name__ = "DisplayString"
_MdmCountryCode_Object = MibTableColumn
mdmCountryCode = _MdmCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 12, 1, 7),
    _MdmCountryCode_Type()
)
mdmCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCountryCode.setStatus("mandatory")
_MdmDiagnosticTable_Object = MibTable
mdmDiagnosticTable = _MdmDiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 13)
)
if mibBuilder.loadTexts:
    mdmDiagnosticTable.setStatus("mandatory")
_MdmDiagnosticEntry_Object = MibTableRow
mdmDiagnosticEntry = _MdmDiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 13, 1)
)
mdmDiagnosticEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmDiagnosticIndex"),
)
if mibBuilder.loadTexts:
    mdmDiagnosticEntry.setStatus("mandatory")
_MdmDiagnosticIndex_Type = SCinstance
_MdmDiagnosticIndex_Object = MibTableColumn
mdmDiagnosticIndex = _MdmDiagnosticIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 13, 1, 1),
    _MdmDiagnosticIndex_Type()
)
mdmDiagnosticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDiagnosticIndex.setStatus("mandatory")


class _MdmDiagnosticTest_Type(Integer32):
    """Custom type mdmDiagnosticTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("analoop", 2),
          ("analoopSelfTest", 3),
          ("digitalLoop", 7),
          ("remoteDigitalLoop", 4),
          ("remoteDigitalLoopSelfTest", 5),
          ("selfTest", 6),
          ("terminateTest", 1))
    )


_MdmDiagnosticTest_Type.__name__ = "Integer32"
_MdmDiagnosticTest_Object = MibTableColumn
mdmDiagnosticTest = _MdmDiagnosticTest_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 13, 1, 2),
    _MdmDiagnosticTest_Type()
)
mdmDiagnosticTest.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mdmDiagnosticTest.setStatus("mandatory")


class _MdmDiagnosticResults_Type(Integer32):
    """Custom type mdmDiagnosticResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmDiagnosticResults_Type.__name__ = "Integer32"
_MdmDiagnosticResults_Object = MibTableColumn
mdmDiagnosticResults = _MdmDiagnosticResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 13, 1, 3),
    _MdmDiagnosticResults_Type()
)
mdmDiagnosticResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDiagnosticResults.setStatus("mandatory")


class _MdmDiagnosticStatus_Type(Integer32):
    """Custom type mdmDiagnosticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              68,
              96,
              97)
        )
    )
    namedValues = NamedValues(
        *(("analoop", 32),
          ("analoopHsk", 16),
          ("analoopSelftest", 96),
          ("inboundRmtDigLp", 2),
          ("localDigLp", 8),
          ("notInTest", 97),
          ("rmtDigLp", 4),
          ("rmtDigLpHsk", 1),
          ("rmtDigLpSelftest", 68),
          ("selftest", 64))
    )


_MdmDiagnosticStatus_Type.__name__ = "Integer32"
_MdmDiagnosticStatus_Object = MibTableColumn
mdmDiagnosticStatus = _MdmDiagnosticStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 13, 1, 4),
    _MdmDiagnosticStatus_Type()
)
mdmDiagnosticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDiagnosticStatus.setStatus("mandatory")


class _MdmTestStatus_Type(Integer32):
    """Custom type mdmTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              8,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("canNotBeDone", 4),
          ("noPrevStatus", 17),
          ("terminated", 8),
          ("timedout", 16))
    )


_MdmTestStatus_Type.__name__ = "Integer32"
_MdmTestStatus_Object = MibTableColumn
mdmTestStatus = _MdmTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 13, 1, 5),
    _MdmTestStatus_Type()
)
mdmTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTestStatus.setStatus("mandatory")
_MdmTestDuration_Type = TimeTicks
_MdmTestDuration_Object = MibTableColumn
mdmTestDuration = _MdmTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 13, 1, 6),
    _MdmTestDuration_Type()
)
mdmTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTestDuration.setStatus("mandatory")
_MdmDialingFunctionTable_Object = MibTable
mdmDialingFunctionTable = _MdmDialingFunctionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 14)
)
if mibBuilder.loadTexts:
    mdmDialingFunctionTable.setStatus("mandatory")
_MdmDialingFunctionEntry_Object = MibTableRow
mdmDialingFunctionEntry = _MdmDialingFunctionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 14, 1)
)
mdmDialingFunctionEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmDialFunctionIndex"),
)
if mibBuilder.loadTexts:
    mdmDialingFunctionEntry.setStatus("mandatory")
_MdmDialFunctionIndex_Type = SCinstance
_MdmDialFunctionIndex_Object = MibTableColumn
mdmDialFunctionIndex = _MdmDialFunctionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 14, 1, 1),
    _MdmDialFunctionIndex_Type()
)
mdmDialFunctionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDialFunctionIndex.setStatus("mandatory")


class _MdmManualDial_Type(DisplayString):
    """Custom type mdmManualDial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_MdmManualDial_Type.__name__ = "DisplayString"
_MdmManualDial_Object = MibTableColumn
mdmManualDial = _MdmManualDial_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 14, 1, 2),
    _MdmManualDial_Type()
)
mdmManualDial.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mdmManualDial.setStatus("mandatory")


class _MdmTerminateCall_Type(Integer32):
    """Custom type mdmTerminateCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("goOnhook", 1)
    )


_MdmTerminateCall_Type.__name__ = "Integer32"
_MdmTerminateCall_Object = MibTableColumn
mdmTerminateCall = _MdmTerminateCall_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 14, 1, 3),
    _MdmTerminateCall_Type()
)
mdmTerminateCall.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mdmTerminateCall.setStatus("mandatory")


class _MdmDialStatus_Type(Integer32):
    """Custom type mdmDialStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("data", 32),
          ("dial", 4),
          ("disconnect", 1),
          ("idle", 2),
          ("inTest", 33),
          ("retrain", 16),
          ("training", 8))
    )


_MdmDialStatus_Type.__name__ = "Integer32"
_MdmDialStatus_Object = MibTableColumn
mdmDialStatus = _MdmDialStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 14, 1, 4),
    _MdmDialStatus_Type()
)
mdmDialStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDialStatus.setStatus("mandatory")


class _MdmCallProgressStatus_Type(Integer32):
    """Custom type mdmCallProgressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              16,
              17,
              18,
              19,
              32,
              64,
              128,
              256,
              257,
              258,
              259,
              260)
        )
    )
    namedValues = NamedValues(
        *(("busy", 4),
          ("connect", 256),
          ("connectIncomingRing", 258),
          ("connectIncomingRing2", 259),
          ("connectRingback", 257),
          ("incomingRing", 2),
          ("noAnswer", 8),
          ("noCarrier", 16),
          ("noDialtone", 32),
          ("noLoopCurrent", 64),
          ("noPrevStatus", 260),
          ("ringAndNoAnswer", 10),
          ("ringNoCarrier", 18),
          ("ringNoCarrier2", 19),
          ("ringback", 1),
          ("ringbackNoCarrier", 17),
          ("unobtainableNumber", 128))
    )


_MdmCallProgressStatus_Type.__name__ = "Integer32"
_MdmCallProgressStatus_Object = MibTableColumn
mdmCallProgressStatus = _MdmCallProgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 14, 1, 5),
    _MdmCallProgressStatus_Type()
)
mdmCallProgressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCallProgressStatus.setStatus("mandatory")
_MdmDialingCellsFunctionTable_Object = MibTable
mdmDialingCellsFunctionTable = _MdmDialingCellsFunctionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 15)
)
if mibBuilder.loadTexts:
    mdmDialingCellsFunctionTable.setStatus("mandatory")
_MdmDialingCellsFunctionEntry_Object = MibTableRow
mdmDialingCellsFunctionEntry = _MdmDialingCellsFunctionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 15, 1)
)
mdmDialingCellsFunctionEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmDialCellFunctionIndex"),
    (0, "GDCMDM-MIB", "mdmCellNumber"),
)
if mibBuilder.loadTexts:
    mdmDialingCellsFunctionEntry.setStatus("mandatory")
_MdmDialCellFunctionIndex_Type = SCinstance
_MdmDialCellFunctionIndex_Object = MibTableColumn
mdmDialCellFunctionIndex = _MdmDialCellFunctionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 15, 1, 1),
    _MdmDialCellFunctionIndex_Type()
)
mdmDialCellFunctionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDialCellFunctionIndex.setStatus("mandatory")
_MdmCellNumber_Type = Integer32
_MdmCellNumber_Object = MibTableColumn
mdmCellNumber = _MdmCellNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 15, 1, 2),
    _MdmCellNumber_Type()
)
mdmCellNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCellNumber.setStatus("mandatory")


class _MdmDial_Type(Integer32):
    """Custom type mdmDial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("goDial", 1)
    )


_MdmDial_Type.__name__ = "Integer32"
_MdmDial_Object = MibTableColumn
mdmDial = _MdmDial_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 15, 1, 3),
    _MdmDial_Type()
)
mdmDial.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mdmDial.setStatus("mandatory")


class _MdmCellPhoneNumber_Type(DisplayString):
    """Custom type mdmCellPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_MdmCellPhoneNumber_Type.__name__ = "DisplayString"
_MdmCellPhoneNumber_Object = MibTableColumn
mdmCellPhoneNumber = _MdmCellPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 15, 1, 4),
    _MdmCellPhoneNumber_Type()
)
mdmCellPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCellPhoneNumber.setStatus("mandatory")


class _MdmTerminateCellCall_Type(Integer32):
    """Custom type mdmTerminateCellCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("goOnhook", 1)
    )


_MdmTerminateCellCall_Type.__name__ = "Integer32"
_MdmTerminateCellCall_Object = MibTableColumn
mdmTerminateCellCall = _MdmTerminateCellCall_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 15, 1, 5),
    _MdmTerminateCellCall_Type()
)
mdmTerminateCellCall.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mdmTerminateCellCall.setStatus("mandatory")
_MdmMaintenanceTable_Object = MibTable
mdmMaintenanceTable = _MdmMaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 16)
)
if mibBuilder.loadTexts:
    mdmMaintenanceTable.setStatus("mandatory")
_MdmMaintenanceEntry_Object = MibTableRow
mdmMaintenanceEntry = _MdmMaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 16, 1)
)
mdmMaintenanceEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmMaintenanceIndex"),
)
if mibBuilder.loadTexts:
    mdmMaintenanceEntry.setStatus("mandatory")
_MdmMaintenanceIndex_Type = SCinstance
_MdmMaintenanceIndex_Object = MibTableColumn
mdmMaintenanceIndex = _MdmMaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 16, 1, 1),
    _MdmMaintenanceIndex_Type()
)
mdmMaintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmMaintenanceIndex.setStatus("mandatory")


class _MdmSaveRecallConfig_Type(Integer32):
    """Custom type mdmSaveRecallConfig based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("recallFactoryDefault0", 1),
          ("recallFactoryDefault1", 2),
          ("recallFactoryDefault2", 3),
          ("recallFactoryDefault3", 4),
          ("recallUserProfile0", 5),
          ("recallUserProfile1", 6),
          ("recallUserProfile2", 7),
          ("recallUserProfile3", 8),
          ("saveUserProfile0", 9),
          ("saveUserProfile1", 10),
          ("saveUserProfile2", 11),
          ("saveUserProfile3", 12))
    )


_MdmSaveRecallConfig_Type.__name__ = "Integer32"
_MdmSaveRecallConfig_Object = MibTableColumn
mdmSaveRecallConfig = _MdmSaveRecallConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 16, 1, 2),
    _MdmSaveRecallConfig_Type()
)
mdmSaveRecallConfig.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mdmSaveRecallConfig.setStatus("mandatory")


class _MdmConfigCksum_Type(OctetString):
    """Custom type mdmConfigCksum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MdmConfigCksum_Type.__name__ = "OctetString"
_MdmConfigCksum_Object = MibTableColumn
mdmConfigCksum = _MdmConfigCksum_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 16, 1, 3),
    _MdmConfigCksum_Type()
)
mdmConfigCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmConfigCksum.setStatus("mandatory")


class _MdmPassword_Type(DisplayString):
    """Custom type mdmPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MdmPassword_Type.__name__ = "DisplayString"
_MdmPassword_Object = MibTableColumn
mdmPassword = _MdmPassword_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 16, 1, 4),
    _MdmPassword_Type()
)
mdmPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mdmPassword.setStatus("mandatory")


class _MdmSerialNumber_Type(DisplayString):
    """Custom type mdmSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_MdmSerialNumber_Type.__name__ = "DisplayString"
_MdmSerialNumber_Object = MibTableColumn
mdmSerialNumber = _MdmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 16, 1, 5),
    _MdmSerialNumber_Type()
)
mdmSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmSerialNumber.setStatus("mandatory")


class _MdmPowerUpProfile_Type(Integer32):
    """Custom type mdmPowerUpProfile based on Integer32"""
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
        *(("one", 2),
          ("three", 4),
          ("two", 3),
          ("zero", 1))
    )


_MdmPowerUpProfile_Type.__name__ = "Integer32"
_MdmPowerUpProfile_Object = MibTableColumn
mdmPowerUpProfile = _MdmPowerUpProfile_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 16, 1, 6),
    _MdmPowerUpProfile_Type()
)
mdmPowerUpProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmPowerUpProfile.setStatus("mandatory")


class _MdmPasswordOperation_Type(Integer32):
    """Custom type mdmPasswordOperation based on Integer32"""
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
        *(("disabled", 1),
          ("enable", 4),
          ("enablehandshake", 2),
          ("enableonline", 3))
    )


_MdmPasswordOperation_Type.__name__ = "Integer32"
_MdmPasswordOperation_Object = MibTableColumn
mdmPasswordOperation = _MdmPasswordOperation_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 16, 1, 7),
    _MdmPasswordOperation_Type()
)
mdmPasswordOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmPasswordOperation.setStatus("mandatory")
_MdmStatisticsTable_Object = MibTable
mdmStatisticsTable = _MdmStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 17)
)
if mibBuilder.loadTexts:
    mdmStatisticsTable.setStatus("mandatory")
_MdmStatisticsEntry_Object = MibTableRow
mdmStatisticsEntry = _MdmStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 17, 1)
)
mdmStatisticsEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmStatisticsIndex"),
)
if mibBuilder.loadTexts:
    mdmStatisticsEntry.setStatus("mandatory")
_MdmStatisticsIndex_Type = SCinstance
_MdmStatisticsIndex_Object = MibTableColumn
mdmStatisticsIndex = _MdmStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 17, 1, 1),
    _MdmStatisticsIndex_Type()
)
mdmStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatisticsIndex.setStatus("mandatory")


class _MdmDCERate_Type(Integer32):
    """Custom type mdmDCERate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("bps1200", 3),
          ("bps12000", 8),
          ("bps14400", 9),
          ("bps16800", 10),
          ("bps19200", 11),
          ("bps21600", 12),
          ("bps2400", 4),
          ("bps24000", 13),
          ("bps26400", 14),
          ("bps28800", 15),
          ("bps300", 2),
          ("bps4800", 5),
          ("bps7200", 6),
          ("bps9600", 7))
    )


_MdmDCERate_Type.__name__ = "Integer32"
_MdmDCERate_Object = MibTableColumn
mdmDCERate = _MdmDCERate_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 17, 1, 2),
    _MdmDCERate_Type()
)
mdmDCERate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDCERate.setStatus("mandatory")
_MdmCallDurationStat_Type = TimeTicks
_MdmCallDurationStat_Object = MibTableColumn
mdmCallDurationStat = _MdmCallDurationStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 17, 1, 3),
    _MdmCallDurationStat_Type()
)
mdmCallDurationStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCallDurationStat.setStatus("mandatory")


class _MdmRetrainCount_Type(Integer32):
    """Custom type mdmRetrainCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MdmRetrainCount_Type.__name__ = "Integer32"
_MdmRetrainCount_Object = MibTableColumn
mdmRetrainCount = _MdmRetrainCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 17, 1, 4),
    _MdmRetrainCount_Type()
)
mdmRetrainCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRetrainCount.setStatus("mandatory")


class _MdmFallbackCount_Type(Integer32):
    """Custom type mdmFallbackCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MdmFallbackCount_Type.__name__ = "Integer32"
_MdmFallbackCount_Object = MibTableColumn
mdmFallbackCount = _MdmFallbackCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 17, 1, 5),
    _MdmFallbackCount_Type()
)
mdmFallbackCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmFallbackCount.setStatus("mandatory")


class _MdmFallforwardCount_Type(Integer32):
    """Custom type mdmFallforwardCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MdmFallforwardCount_Type.__name__ = "Integer32"
_MdmFallforwardCount_Object = MibTableColumn
mdmFallforwardCount = _MdmFallforwardCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 17, 1, 6),
    _MdmFallforwardCount_Type()
)
mdmFallforwardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmFallforwardCount.setStatus("mandatory")


class _MdmRxSignalLevel_Type(Integer32):
    """Custom type mdmRxSignalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MdmRxSignalLevel_Type.__name__ = "Integer32"
_MdmRxSignalLevel_Object = MibTableColumn
mdmRxSignalLevel = _MdmRxSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 17, 1, 7),
    _MdmRxSignalLevel_Type()
)
mdmRxSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRxSignalLevel.setStatus("mandatory")


class _MdmSignaltoNoiseRatio_Type(Integer32):
    """Custom type mdmSignaltoNoiseRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MdmSignaltoNoiseRatio_Type.__name__ = "Integer32"
_MdmSignaltoNoiseRatio_Object = MibTableColumn
mdmSignaltoNoiseRatio = _MdmSignaltoNoiseRatio_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 17, 1, 8),
    _MdmSignaltoNoiseRatio_Type()
)
mdmSignaltoNoiseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmSignaltoNoiseRatio.setStatus("mandatory")


class _MdmAnswerOriginateStat_Type(Integer32):
    """Custom type mdmAnswerOriginateStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("originate", 1))
    )


_MdmAnswerOriginateStat_Type.__name__ = "Integer32"
_MdmAnswerOriginateStat_Object = MibTableColumn
mdmAnswerOriginateStat = _MdmAnswerOriginateStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 17, 1, 9),
    _MdmAnswerOriginateStat_Type()
)
mdmAnswerOriginateStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmAnswerOriginateStat.setStatus("mandatory")


class _MdmDiscReason_Type(Integer32):
    """Custom type mdmDiscReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 2),
          ("usertimeout", 1))
    )


_MdmDiscReason_Type.__name__ = "Integer32"
_MdmDiscReason_Object = MibTableColumn
mdmDiscReason = _MdmDiscReason_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 17, 1, 10),
    _MdmDiscReason_Type()
)
mdmDiscReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDiscReason.setStatus("mandatory")


class _MdmCompressionEfficiency_Type(Integer32):
    """Custom type mdmCompressionEfficiency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmCompressionEfficiency_Type.__name__ = "Integer32"
_MdmCompressionEfficiency_Object = MibTableColumn
mdmCompressionEfficiency = _MdmCompressionEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 17, 1, 11),
    _MdmCompressionEfficiency_Type()
)
mdmCompressionEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCompressionEfficiency.setStatus("mandatory")


class _MdmThruput_Type(Integer32):
    """Custom type mdmThruput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmThruput_Type.__name__ = "Integer32"
_MdmThruput_Object = MibTableColumn
mdmThruput = _MdmThruput_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 17, 1, 12),
    _MdmThruput_Type()
)
mdmThruput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmThruput.setStatus("mandatory")
_MdmRemoteConfigTable_Object = MibTable
mdmRemoteConfigTable = _MdmRemoteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 18)
)
if mibBuilder.loadTexts:
    mdmRemoteConfigTable.setStatus("mandatory")
_MdmRemoteConfigEntry_Object = MibTableRow
mdmRemoteConfigEntry = _MdmRemoteConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 18, 1)
)
mdmRemoteConfigEntry.setIndexNames(
    (0, "GDCMDM-MIB", "mdmRemoteConfigIndex"),
)
if mibBuilder.loadTexts:
    mdmRemoteConfigEntry.setStatus("mandatory")
_MdmRemoteConfigIndex_Type = SCinstance
_MdmRemoteConfigIndex_Object = MibTableColumn
mdmRemoteConfigIndex = _MdmRemoteConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 18, 1, 1),
    _MdmRemoteConfigIndex_Type()
)
mdmRemoteConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRemoteConfigIndex.setStatus("mandatory")


class _MdmRemoteConfiguration_Type(Integer32):
    """Custom type mdmRemoteConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enableDMS", 3),
          ("enableDTE", 2))
    )


_MdmRemoteConfiguration_Type.__name__ = "Integer32"
_MdmRemoteConfiguration_Object = MibTableColumn
mdmRemoteConfiguration = _MdmRemoteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 18, 1, 2),
    _MdmRemoteConfiguration_Type()
)
mdmRemoteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmRemoteConfiguration.setStatus("mandatory")


class _MdmEndRemoteConfiguration_Type(Integer32):
    """Custom type mdmEndRemoteConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noUpdate", 1),
          ("update", 2))
    )


_MdmEndRemoteConfiguration_Type.__name__ = "Integer32"
_MdmEndRemoteConfiguration_Object = MibTableColumn
mdmEndRemoteConfiguration = _MdmEndRemoteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 18, 1, 3),
    _MdmEndRemoteConfiguration_Type()
)
mdmEndRemoteConfiguration.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mdmEndRemoteConfiguration.setStatus("mandatory")


class _MdmPasswordRemoteConfiguration_Type(DisplayString):
    """Custom type mdmPasswordRemoteConfiguration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MdmPasswordRemoteConfiguration_Type.__name__ = "DisplayString"
_MdmPasswordRemoteConfiguration_Object = MibTableColumn
mdmPasswordRemoteConfiguration = _MdmPasswordRemoteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 18, 1, 4),
    _MdmPasswordRemoteConfiguration_Type()
)
mdmPasswordRemoteConfiguration.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mdmPasswordRemoteConfiguration.setStatus("mandatory")


class _MdmMIBVersion_Type(DisplayString):
    """Custom type mdmMIBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_MdmMIBVersion_Type.__name__ = "DisplayString"
_MdmMIBVersion_Object = MibScalar
mdmMIBVersion = _MdmMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 498, 4, 19),
    _MdmMIBVersion_Type()
)
mdmMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmMIBVersion.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mdmCallStatsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 498, 4, 0, 1)
)
mdmCallStatsTrap.setObjects(
      *(("GDCMDM-MIB", "mdmDCERate"),
        ("GDCMDM-MIB", "mdmRetrainCount"),
        ("GDCMDM-MIB", "mdmFallbackCount"),
        ("GDCMDM-MIB", "mdmFallforwardCount"),
        ("GDCMDM-MIB", "mdmRxSignalLevel"),
        ("GDCMDM-MIB", "mdmSignaltoNoiseRatio"),
        ("GDCMDM-MIB", "mdmAnswerOriginateStat"),
        ("GDCMDM-MIB", "mdmCallDurationStat"),
        ("GDCMDM-MIB", "mdmDiscReason"),
        ("GDCMDM-MIB", "mdmCompressionEfficiency"),
        ("GDCMDM-MIB", "mdmThruput"))
)
if mibBuilder.loadTexts:
    mdmCallStatsTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCMDM-MIB",
    **{"gdc": gdc,
       "mdm": mdm,
       "mdmCallStatsTrap": mdmCallStatsTrap,
       "mdmNetworkConfigTable": mdmNetworkConfigTable,
       "mdmNetworkEntry": mdmNetworkEntry,
       "mdmNetworkIndex": mdmNetworkIndex,
       "mdmNetworkType": mdmNetworkType,
       "mdmSNTxType": mdmSNTxType,
       "mdmSNTxLevel": mdmSNTxLevel,
       "mdmSNHandshakeMode": mdmSNHandshakeMode,
       "mdmDTEConfigTable": mdmDTEConfigTable,
       "mdmDTEntry": mdmDTEntry,
       "mdmDTEIndex": mdmDTEIndex,
       "mdmDTESpeed": mdmDTESpeed,
       "mdmCPMResp": mdmCPMResp,
       "mdmCharLength": mdmCharLength,
       "mdmParity": mdmParity,
       "mdmOverspeed": mdmOverspeed,
       "mdmFlowCntrl": mdmFlowCntrl,
       "mdmTermEcho": mdmTermEcho,
       "mdmDCDCntrl": mdmDCDCntrl,
       "mdmCTSCntrl": mdmCTSCntrl,
       "mdmDTRTrans": mdmDTRTrans,
       "mdmDSRCntrl": mdmDSRCntrl,
       "mdmDSRCntrlAL": mdmDSRCntrlAL,
       "mdmTXClockSource": mdmTXClockSource,
       "mdmRTSCTSDelay": mdmRTSCTSDelay,
       "mdmCarriageReturnCharacter": mdmCarriageReturnCharacter,
       "mdmCharacterAbortDialing": mdmCharacterAbortDialing,
       "mdmDelayDTR": mdmDelayDTR,
       "mdmEscapeCharacter": mdmEscapeCharacter,
       "mdmLineFeedCharacter": mdmLineFeedCharacter,
       "mdmHangUpDelay": mdmHangUpDelay,
       "mdmEscapeCharacterGuardTime": mdmEscapeCharacterGuardTime,
       "mdmOperatingMode": mdmOperatingMode,
       "mdmBackSpaceCharacter": mdmBackSpaceCharacter,
       "mdmModemConfigTable": mdmModemConfigTable,
       "mdmModemEntry": mdmModemEntry,
       "mdmModemIndex": mdmModemIndex,
       "mdmRingsToAns": mdmRingsToAns,
       "mdmFallFwrdBack": mdmFallFwrdBack,
       "mdmTrellis": mdmTrellis,
       "mdmSQRetrain": mdmSQRetrain,
       "mdmLongSpaceDisc": mdmLongSpaceDisc,
       "mdmMakeBusy": mdmMakeBusy,
       "mdmRDLOptions": mdmRDLOptions,
       "mdmTestTimer": mdmTestTimer,
       "mdmDTETestCntrl": mdmDTETestCntrl,
       "mdmDCDLossDisc": mdmDCDLossDisc,
       "mdmCDRespTime": mdmCDRespTime,
       "mdmAnswerOriginate": mdmAnswerOriginate,
       "mdmWaitForDCD": mdmWaitForDCD,
       "mdmDialerConfigTable": mdmDialerConfigTable,
       "mdmDialerEntry": mdmDialerEntry,
       "mdmDialerIndex": mdmDialerIndex,
       "mdmCPMMonitor": mdmCPMMonitor,
       "mdmParserSelection": mdmParserSelection,
       "mdmDTRDial": mdmDTRDial,
       "mdmDialType": mdmDialType,
       "mdmResponseMode": mdmResponseMode,
       "mdmResponseType": mdmResponseType,
       "mdmPauseTime": mdmPauseTime,
       "mdmWaitForDialtoneTime": mdmWaitForDialtoneTime,
       "mdmProtocolConfigTable": mdmProtocolConfigTable,
       "mdmProtocolEntry": mdmProtocolEntry,
       "mdmProtocolIndex": mdmProtocolIndex,
       "mdmCompression": mdmCompression,
       "mdmAsyncProtocol": mdmAsyncProtocol,
       "mdmFlowControl": mdmFlowControl,
       "mdmBreakHandling": mdmBreakHandling,
       "mdmConnAndLinkMessages": mdmConnAndLinkMessages,
       "mdmErrorCorrection": mdmErrorCorrection,
       "mdmV13Mode": mdmV13Mode,
       "mdmSyncProtocol": mdmSyncProtocol,
       "mdmFrameRetransLimit": mdmFrameRetransLimit,
       "mdmPrivateLineConfigTable": mdmPrivateLineConfigTable,
       "mdmPrivateLineEntry": mdmPrivateLineEntry,
       "mdmPrivateLineIndex": mdmPrivateLineIndex,
       "mdmPrivateLineTxLevel": mdmPrivateLineTxLevel,
       "mdmPrivateLineHandshakeMode": mdmPrivateLineHandshakeMode,
       "mdmAutoDialRestoral": mdmAutoDialRestoral,
       "mdmPrivateLineDownTime": mdmPrivateLineDownTime,
       "mdmDBUtoPLLookbackTime": mdmDBUtoPLLookbackTime,
       "mdmAlarmScanTable": mdmAlarmScanTable,
       "mdmAlarmScanEntry": mdmAlarmScanEntry,
       "mdmAlarmScanIndex": mdmAlarmScanIndex,
       "mdmAlarmScan": mdmAlarmScan,
       "mdmResetSelfPowerBit": mdmResetSelfPowerBit,
       "mdmMaskAlarmTable": mdmMaskAlarmTable,
       "mdmMaskAlarmEntry": mdmMaskAlarmEntry,
       "mdmMaskAlarmIndex": mdmMaskAlarmIndex,
       "mdmDTRLoss": mdmDTRLoss,
       "mdmFallback": mdmFallback,
       "mdmRxdTran": mdmRxdTran,
       "mdmTxdTran": mdmTxdTran,
       "mdmDCDLoss": mdmDCDLoss,
       "mdmRingNoAnswer": mdmRingNoAnswer,
       "mdmRetrain": mdmRetrain,
       "mdmCallLength": mdmCallLength,
       "mdmCallFail": mdmCallFail,
       "mdmConfigErr": mdmConfigErr,
       "mdmSignalQuality": mdmSignalQuality,
       "mdmOnDBU": mdmOnDBU,
       "mdmRemoteConfigMask": mdmRemoteConfigMask,
       "mdmTestTimeout": mdmTestTimeout,
       "mdmThresholdsTable": mdmThresholdsTable,
       "mdmThresholdsEntry": mdmThresholdsEntry,
       "mdmThresholdsIndex": mdmThresholdsIndex,
       "mdmCallDuration": mdmCallDuration,
       "mdmRetrainThreshold": mdmRetrainThreshold,
       "mdmStatusTable": mdmStatusTable,
       "mdmStatusEntry": mdmStatusEntry,
       "mdmStatusIndex": mdmStatusIndex,
       "mdmPLLookbackStatus": mdmPLLookbackStatus,
       "mdmAutoDialRestoralStatus": mdmAutoDialRestoralStatus,
       "mdmTXDtransitions": mdmTXDtransitions,
       "mdmRXDtransitions": mdmRXDtransitions,
       "mdmRTStransitions": mdmRTStransitions,
       "mdmDTRtransitions": mdmDTRtransitions,
       "mdmDCDtransitions": mdmDCDtransitions,
       "mdmTXCLKtransitions": mdmTXCLKtransitions,
       "mdmDTR": mdmDTR,
       "mdmCTS": mdmCTS,
       "mdmDSR": mdmDSR,
       "mdmDCD": mdmDCD,
       "mdmSQM": mdmSQM,
       "mdmRTS": mdmRTS,
       "mdmSwitchedPrivate": mdmSwitchedPrivate,
       "mdmControlTable": mdmControlTable,
       "mdmControlEntry": mdmControlEntry,
       "mdmControlIndex": mdmControlIndex,
       "mdmSoftReset": mdmSoftReset,
       "mdmFrontPanel": mdmFrontPanel,
       "mdmMakeClearBusy": mdmMakeClearBusy,
       "mdmPLTalkData": mdmPLTalkData,
       "mdmWhatAreYouTable": mdmWhatAreYouTable,
       "mdmWhatAreYouEntry": mdmWhatAreYouEntry,
       "mdmWhatAreYouIndex": mdmWhatAreYouIndex,
       "mdmVFCard": mdmVFCard,
       "mdmDTECard": mdmDTECard,
       "mdmProductCode": mdmProductCode,
       "mdmCodeRev": mdmCodeRev,
       "mdmBootRev": mdmBootRev,
       "mdmCountryCode": mdmCountryCode,
       "mdmDiagnosticTable": mdmDiagnosticTable,
       "mdmDiagnosticEntry": mdmDiagnosticEntry,
       "mdmDiagnosticIndex": mdmDiagnosticIndex,
       "mdmDiagnosticTest": mdmDiagnosticTest,
       "mdmDiagnosticResults": mdmDiagnosticResults,
       "mdmDiagnosticStatus": mdmDiagnosticStatus,
       "mdmTestStatus": mdmTestStatus,
       "mdmTestDuration": mdmTestDuration,
       "mdmDialingFunctionTable": mdmDialingFunctionTable,
       "mdmDialingFunctionEntry": mdmDialingFunctionEntry,
       "mdmDialFunctionIndex": mdmDialFunctionIndex,
       "mdmManualDial": mdmManualDial,
       "mdmTerminateCall": mdmTerminateCall,
       "mdmDialStatus": mdmDialStatus,
       "mdmCallProgressStatus": mdmCallProgressStatus,
       "mdmDialingCellsFunctionTable": mdmDialingCellsFunctionTable,
       "mdmDialingCellsFunctionEntry": mdmDialingCellsFunctionEntry,
       "mdmDialCellFunctionIndex": mdmDialCellFunctionIndex,
       "mdmCellNumber": mdmCellNumber,
       "mdmDial": mdmDial,
       "mdmCellPhoneNumber": mdmCellPhoneNumber,
       "mdmTerminateCellCall": mdmTerminateCellCall,
       "mdmMaintenanceTable": mdmMaintenanceTable,
       "mdmMaintenanceEntry": mdmMaintenanceEntry,
       "mdmMaintenanceIndex": mdmMaintenanceIndex,
       "mdmSaveRecallConfig": mdmSaveRecallConfig,
       "mdmConfigCksum": mdmConfigCksum,
       "mdmPassword": mdmPassword,
       "mdmSerialNumber": mdmSerialNumber,
       "mdmPowerUpProfile": mdmPowerUpProfile,
       "mdmPasswordOperation": mdmPasswordOperation,
       "mdmStatisticsTable": mdmStatisticsTable,
       "mdmStatisticsEntry": mdmStatisticsEntry,
       "mdmStatisticsIndex": mdmStatisticsIndex,
       "mdmDCERate": mdmDCERate,
       "mdmCallDurationStat": mdmCallDurationStat,
       "mdmRetrainCount": mdmRetrainCount,
       "mdmFallbackCount": mdmFallbackCount,
       "mdmFallforwardCount": mdmFallforwardCount,
       "mdmRxSignalLevel": mdmRxSignalLevel,
       "mdmSignaltoNoiseRatio": mdmSignaltoNoiseRatio,
       "mdmAnswerOriginateStat": mdmAnswerOriginateStat,
       "mdmDiscReason": mdmDiscReason,
       "mdmCompressionEfficiency": mdmCompressionEfficiency,
       "mdmThruput": mdmThruput,
       "mdmRemoteConfigTable": mdmRemoteConfigTable,
       "mdmRemoteConfigEntry": mdmRemoteConfigEntry,
       "mdmRemoteConfigIndex": mdmRemoteConfigIndex,
       "mdmRemoteConfiguration": mdmRemoteConfiguration,
       "mdmEndRemoteConfiguration": mdmEndRemoteConfiguration,
       "mdmPasswordRemoteConfiguration": mdmPasswordRemoteConfiguration,
       "mdmMIBVersion": mdmMIBVersion}
)
