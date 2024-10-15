# SNMP MIB module (DC-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DC-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:23 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatOtherStatsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatOtherStatsGroup = _Cdx6500StatOtherStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2)
)
_Cdx6500DCStatTable_ObjectIdentity = ObjectIdentity
cdx6500DCStatTable = _Cdx6500DCStatTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10)
)
_Cdx6500DCGenStatTable_ObjectIdentity = ObjectIdentity
cdx6500DCGenStatTable = _Cdx6500DCGenStatTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1)
)
_Cdx6500DCGenStatTableEntry_ObjectIdentity = ObjectIdentity
cdx6500DCGenStatTableEntry = _Cdx6500DCGenStatTableEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1)
)


class _Cdx6500DCGenStatDSPStatus_Type(Integer32):
    """Custom type cdx6500DCGenStatDSPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("missing", 3),
          ("up", 2))
    )


_Cdx6500DCGenStatDSPStatus_Type.__name__ = "Integer32"
_Cdx6500DCGenStatDSPStatus_Object = MibScalar
cdx6500DCGenStatDSPStatus = _Cdx6500DCGenStatDSPStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 1),
    _Cdx6500DCGenStatDSPStatus_Type()
)
cdx6500DCGenStatDSPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCGenStatDSPStatus.setStatus("mandatory")


class _Cdx6500DCGenStatHndlrSWRev_Type(Integer32):
    """Custom type cdx6500DCGenStatHndlrSWRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cdx6500DCGenStatHndlrSWRev_Type.__name__ = "Integer32"
_Cdx6500DCGenStatHndlrSWRev_Object = MibScalar
cdx6500DCGenStatHndlrSWRev = _Cdx6500DCGenStatHndlrSWRev_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 2),
    _Cdx6500DCGenStatHndlrSWRev_Type()
)
cdx6500DCGenStatHndlrSWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCGenStatHndlrSWRev.setStatus("mandatory")


class _Cdx6500DCGenStatFnctnSWRev_Type(Integer32):
    """Custom type cdx6500DCGenStatFnctnSWRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cdx6500DCGenStatFnctnSWRev_Type.__name__ = "Integer32"
_Cdx6500DCGenStatFnctnSWRev_Object = MibScalar
cdx6500DCGenStatFnctnSWRev = _Cdx6500DCGenStatFnctnSWRev_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 3),
    _Cdx6500DCGenStatFnctnSWRev_Type()
)
cdx6500DCGenStatFnctnSWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCGenStatFnctnSWRev.setStatus("mandatory")


class _Cdx6500DCGenStatMaxChannels_Type(Integer32):
    """Custom type cdx6500DCGenStatMaxChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cdx6500DCGenStatMaxChannels_Type.__name__ = "Integer32"
_Cdx6500DCGenStatMaxChannels_Object = MibScalar
cdx6500DCGenStatMaxChannels = _Cdx6500DCGenStatMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 4),
    _Cdx6500DCGenStatMaxChannels_Type()
)
cdx6500DCGenStatMaxChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCGenStatMaxChannels.setStatus("mandatory")


class _Cdx6500DCGenStatChanInUse_Type(Integer32):
    """Custom type cdx6500DCGenStatChanInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cdx6500DCGenStatChanInUse_Type.__name__ = "Integer32"
_Cdx6500DCGenStatChanInUse_Object = MibScalar
cdx6500DCGenStatChanInUse = _Cdx6500DCGenStatChanInUse_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 5),
    _Cdx6500DCGenStatChanInUse_Type()
)
cdx6500DCGenStatChanInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCGenStatChanInUse.setStatus("mandatory")


class _Cdx6500DCGenStatMaxSmltChanUse_Type(Integer32):
    """Custom type cdx6500DCGenStatMaxSmltChanUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cdx6500DCGenStatMaxSmltChanUse_Type.__name__ = "Integer32"
_Cdx6500DCGenStatMaxSmltChanUse_Object = MibScalar
cdx6500DCGenStatMaxSmltChanUse = _Cdx6500DCGenStatMaxSmltChanUse_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 6),
    _Cdx6500DCGenStatMaxSmltChanUse_Type()
)
cdx6500DCGenStatMaxSmltChanUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCGenStatMaxSmltChanUse.setStatus("mandatory")
_Cdx6500DCGenStatRejectConn_Type = Integer32
_Cdx6500DCGenStatRejectConn_Object = MibScalar
cdx6500DCGenStatRejectConn = _Cdx6500DCGenStatRejectConn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 7),
    _Cdx6500DCGenStatRejectConn_Type()
)
cdx6500DCGenStatRejectConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCGenStatRejectConn.setStatus("mandatory")
_Cdx6500DCGenStatAggCRatio_Type = DisplayString
_Cdx6500DCGenStatAggCRatio_Object = MibScalar
cdx6500DCGenStatAggCRatio = _Cdx6500DCGenStatAggCRatio_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 8),
    _Cdx6500DCGenStatAggCRatio_Type()
)
cdx6500DCGenStatAggCRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCGenStatAggCRatio.setStatus("mandatory")


class _Cdx6500DCGenStatCurrEncQDepth_Type(Integer32):
    """Custom type cdx6500DCGenStatCurrEncQDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500DCGenStatCurrEncQDepth_Type.__name__ = "Integer32"
_Cdx6500DCGenStatCurrEncQDepth_Object = MibScalar
cdx6500DCGenStatCurrEncQDepth = _Cdx6500DCGenStatCurrEncQDepth_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 9),
    _Cdx6500DCGenStatCurrEncQDepth_Type()
)
cdx6500DCGenStatCurrEncQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCGenStatCurrEncQDepth.setStatus("mandatory")
_Cdx6500DCGenStatMaxEncQDepth_Type = Integer32
_Cdx6500DCGenStatMaxEncQDepth_Object = MibScalar
cdx6500DCGenStatMaxEncQDepth = _Cdx6500DCGenStatMaxEncQDepth_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 10),
    _Cdx6500DCGenStatMaxEncQDepth_Type()
)
cdx6500DCGenStatMaxEncQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCGenStatMaxEncQDepth.setStatus("mandatory")
_Cdx6500DCGenStatTmOfMaxEncQDepth_Type = DisplayString
_Cdx6500DCGenStatTmOfMaxEncQDepth_Object = MibScalar
cdx6500DCGenStatTmOfMaxEncQDepth = _Cdx6500DCGenStatTmOfMaxEncQDepth_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 11),
    _Cdx6500DCGenStatTmOfMaxEncQDepth_Type()
)
cdx6500DCGenStatTmOfMaxEncQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCGenStatTmOfMaxEncQDepth.setStatus("mandatory")


class _Cdx6500DCGenStatCurrDecQDepth_Type(Integer32):
    """Custom type cdx6500DCGenStatCurrDecQDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500DCGenStatCurrDecQDepth_Type.__name__ = "Integer32"
_Cdx6500DCGenStatCurrDecQDepth_Object = MibScalar
cdx6500DCGenStatCurrDecQDepth = _Cdx6500DCGenStatCurrDecQDepth_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 12),
    _Cdx6500DCGenStatCurrDecQDepth_Type()
)
cdx6500DCGenStatCurrDecQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCGenStatCurrDecQDepth.setStatus("mandatory")
_Cdx6500DCGenStatMaxDecQDepth_Type = Integer32
_Cdx6500DCGenStatMaxDecQDepth_Object = MibScalar
cdx6500DCGenStatMaxDecQDepth = _Cdx6500DCGenStatMaxDecQDepth_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 13),
    _Cdx6500DCGenStatMaxDecQDepth_Type()
)
cdx6500DCGenStatMaxDecQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCGenStatMaxDecQDepth.setStatus("mandatory")
_Cdx6500DCGenStatTmOfMaxDecQDepth_Type = DisplayString
_Cdx6500DCGenStatTmOfMaxDecQDepth_Object = MibScalar
cdx6500DCGenStatTmOfMaxDecQDepth = _Cdx6500DCGenStatTmOfMaxDecQDepth_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 14),
    _Cdx6500DCGenStatTmOfMaxDecQDepth_Type()
)
cdx6500DCGenStatTmOfMaxDecQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCGenStatTmOfMaxDecQDepth.setStatus("mandatory")
_Cdx6500DCChanStatTable_Object = MibTable
cdx6500DCChanStatTable = _Cdx6500DCChanStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2)
)
if mibBuilder.loadTexts:
    cdx6500DCChanStatTable.setStatus("mandatory")
_Cdx6500DCChanStatTableEntry_Object = MibTableRow
cdx6500DCChanStatTableEntry = _Cdx6500DCChanStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1)
)
cdx6500DCChanStatTableEntry.setIndexNames(
    (0, "DC-OPT-MIB", "cdx6500DCChanStatChanNum"),
)
if mibBuilder.loadTexts:
    cdx6500DCChanStatTableEntry.setStatus("mandatory")


class _Cdx6500DCChanStatChanNum_Type(Integer32):
    """Custom type cdx6500DCChanStatChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cdx6500DCChanStatChanNum_Type.__name__ = "Integer32"
_Cdx6500DCChanStatChanNum_Object = MibTableColumn
cdx6500DCChanStatChanNum = _Cdx6500DCChanStatChanNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 1),
    _Cdx6500DCChanStatChanNum_Type()
)
cdx6500DCChanStatChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatChanNum.setStatus("mandatory")
_Cdx6500DCChanStatTmOfLastStatRst_Type = DisplayString
_Cdx6500DCChanStatTmOfLastStatRst_Object = MibTableColumn
cdx6500DCChanStatTmOfLastStatRst = _Cdx6500DCChanStatTmOfLastStatRst_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 2),
    _Cdx6500DCChanStatTmOfLastStatRst_Type()
)
cdx6500DCChanStatTmOfLastStatRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatTmOfLastStatRst.setStatus("mandatory")


class _Cdx6500DCChanStatChanState_Type(Integer32):
    """Custom type cdx6500DCChanStatChanState based on Integer32"""
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
        *(("apClearing", 7),
          ("clearing", 11),
          ("clearingCall", 9),
          ("dataPassing", 4),
          ("dspDown", 1),
          ("flushingDCRing", 6),
          ("flushingData", 5),
          ("flushingOnClr", 10),
          ("idle", 2),
          ("negotiating", 3),
          ("npClearing", 8))
    )


_Cdx6500DCChanStatChanState_Type.__name__ = "Integer32"
_Cdx6500DCChanStatChanState_Object = MibTableColumn
cdx6500DCChanStatChanState = _Cdx6500DCChanStatChanState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 3),
    _Cdx6500DCChanStatChanState_Type()
)
cdx6500DCChanStatChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatChanState.setStatus("mandatory")
_Cdx6500DCChanStatSourceChan_Type = DisplayString
_Cdx6500DCChanStatSourceChan_Object = MibTableColumn
cdx6500DCChanStatSourceChan = _Cdx6500DCChanStatSourceChan_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 4),
    _Cdx6500DCChanStatSourceChan_Type()
)
cdx6500DCChanStatSourceChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatSourceChan.setStatus("mandatory")
_Cdx6500DCChanStatDestChan_Type = DisplayString
_Cdx6500DCChanStatDestChan_Object = MibTableColumn
cdx6500DCChanStatDestChan = _Cdx6500DCChanStatDestChan_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 5),
    _Cdx6500DCChanStatDestChan_Type()
)
cdx6500DCChanStatDestChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatDestChan.setStatus("mandatory")
_Cdx6500DCChanStatXmitCRatio_Type = DisplayString
_Cdx6500DCChanStatXmitCRatio_Object = MibTableColumn
cdx6500DCChanStatXmitCRatio = _Cdx6500DCChanStatXmitCRatio_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 6),
    _Cdx6500DCChanStatXmitCRatio_Type()
)
cdx6500DCChanStatXmitCRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatXmitCRatio.setStatus("mandatory")
_Cdx6500DCChanStatNumOfEncFrames_Type = Counter32
_Cdx6500DCChanStatNumOfEncFrames_Object = MibTableColumn
cdx6500DCChanStatNumOfEncFrames = _Cdx6500DCChanStatNumOfEncFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 7),
    _Cdx6500DCChanStatNumOfEncFrames_Type()
)
cdx6500DCChanStatNumOfEncFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatNumOfEncFrames.setStatus("mandatory")
_Cdx6500DCChanStatNumOfCharInToEnc_Type = Counter32
_Cdx6500DCChanStatNumOfCharInToEnc_Object = MibTableColumn
cdx6500DCChanStatNumOfCharInToEnc = _Cdx6500DCChanStatNumOfCharInToEnc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 8),
    _Cdx6500DCChanStatNumOfCharInToEnc_Type()
)
cdx6500DCChanStatNumOfCharInToEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatNumOfCharInToEnc.setStatus("mandatory")
_Cdx6500DCChanStatNumOfCharOutOfEnc_Type = Counter32
_Cdx6500DCChanStatNumOfCharOutOfEnc_Object = MibTableColumn
cdx6500DCChanStatNumOfCharOutOfEnc = _Cdx6500DCChanStatNumOfCharOutOfEnc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 9),
    _Cdx6500DCChanStatNumOfCharOutOfEnc_Type()
)
cdx6500DCChanStatNumOfCharOutOfEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatNumOfCharOutOfEnc.setStatus("mandatory")
_Cdx6500DCChanStatNumOfDecFrames_Type = Counter32
_Cdx6500DCChanStatNumOfDecFrames_Object = MibTableColumn
cdx6500DCChanStatNumOfDecFrames = _Cdx6500DCChanStatNumOfDecFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 10),
    _Cdx6500DCChanStatNumOfDecFrames_Type()
)
cdx6500DCChanStatNumOfDecFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatNumOfDecFrames.setStatus("mandatory")
_Cdx6500DCChanStatNumOfCharInToDec_Type = Counter32
_Cdx6500DCChanStatNumOfCharInToDec_Object = MibTableColumn
cdx6500DCChanStatNumOfCharInToDec = _Cdx6500DCChanStatNumOfCharInToDec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 11),
    _Cdx6500DCChanStatNumOfCharInToDec_Type()
)
cdx6500DCChanStatNumOfCharInToDec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatNumOfCharInToDec.setStatus("mandatory")
_Cdx6500DCChanStatNumOfCharOutOfDec_Type = Counter32
_Cdx6500DCChanStatNumOfCharOutOfDec_Object = MibTableColumn
cdx6500DCChanStatNumOfCharOutOfDec = _Cdx6500DCChanStatNumOfCharOutOfDec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 12),
    _Cdx6500DCChanStatNumOfCharOutOfDec_Type()
)
cdx6500DCChanStatNumOfCharOutOfDec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatNumOfCharOutOfDec.setStatus("mandatory")
_Cdx6500DCChanStatEncAETrnstnCnt_Type = Counter32
_Cdx6500DCChanStatEncAETrnstnCnt_Object = MibTableColumn
cdx6500DCChanStatEncAETrnstnCnt = _Cdx6500DCChanStatEncAETrnstnCnt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 13),
    _Cdx6500DCChanStatEncAETrnstnCnt_Type()
)
cdx6500DCChanStatEncAETrnstnCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatEncAETrnstnCnt.setStatus("mandatory")
_Cdx6500DCChanStatEncAEFrameCnt_Type = Counter32
_Cdx6500DCChanStatEncAEFrameCnt_Object = MibTableColumn
cdx6500DCChanStatEncAEFrameCnt = _Cdx6500DCChanStatEncAEFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 14),
    _Cdx6500DCChanStatEncAEFrameCnt_Type()
)
cdx6500DCChanStatEncAEFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatEncAEFrameCnt.setStatus("mandatory")


class _Cdx6500DCChanStatEncAEModeStatus_Type(Integer32):
    """Custom type cdx6500DCChanStatEncAEModeStatus based on Integer32"""
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


_Cdx6500DCChanStatEncAEModeStatus_Type.__name__ = "Integer32"
_Cdx6500DCChanStatEncAEModeStatus_Object = MibTableColumn
cdx6500DCChanStatEncAEModeStatus = _Cdx6500DCChanStatEncAEModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 15),
    _Cdx6500DCChanStatEncAEModeStatus_Type()
)
cdx6500DCChanStatEncAEModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatEncAEModeStatus.setStatus("mandatory")
_Cdx6500DCChanStatDecAETrnstnCnt_Type = Counter32
_Cdx6500DCChanStatDecAETrnstnCnt_Object = MibTableColumn
cdx6500DCChanStatDecAETrnstnCnt = _Cdx6500DCChanStatDecAETrnstnCnt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 16),
    _Cdx6500DCChanStatDecAETrnstnCnt_Type()
)
cdx6500DCChanStatDecAETrnstnCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatDecAETrnstnCnt.setStatus("mandatory")
_Cdx6500DCChanStatDecAEFrameCnt_Type = Counter32
_Cdx6500DCChanStatDecAEFrameCnt_Object = MibTableColumn
cdx6500DCChanStatDecAEFrameCnt = _Cdx6500DCChanStatDecAEFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 17),
    _Cdx6500DCChanStatDecAEFrameCnt_Type()
)
cdx6500DCChanStatDecAEFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatDecAEFrameCnt.setStatus("mandatory")


class _Cdx6500DCChanStatDecAEModeStatus_Type(Integer32):
    """Custom type cdx6500DCChanStatDecAEModeStatus based on Integer32"""
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


_Cdx6500DCChanStatDecAEModeStatus_Type.__name__ = "Integer32"
_Cdx6500DCChanStatDecAEModeStatus_Object = MibTableColumn
cdx6500DCChanStatDecAEModeStatus = _Cdx6500DCChanStatDecAEModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 18),
    _Cdx6500DCChanStatDecAEModeStatus_Type()
)
cdx6500DCChanStatDecAEModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatDecAEModeStatus.setStatus("mandatory")
_Cdx6500DCChanStatDSWithBadFrames_Type = Counter32
_Cdx6500DCChanStatDSWithBadFrames_Object = MibTableColumn
cdx6500DCChanStatDSWithBadFrames = _Cdx6500DCChanStatDSWithBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 19),
    _Cdx6500DCChanStatDSWithBadFrames_Type()
)
cdx6500DCChanStatDSWithBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatDSWithBadFrames.setStatus("mandatory")
_Cdx6500DCChanStatDSWithBadHeaders_Type = Counter32
_Cdx6500DCChanStatDSWithBadHeaders_Object = MibTableColumn
cdx6500DCChanStatDSWithBadHeaders = _Cdx6500DCChanStatDSWithBadHeaders_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 20),
    _Cdx6500DCChanStatDSWithBadHeaders_Type()
)
cdx6500DCChanStatDSWithBadHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatDSWithBadHeaders.setStatus("mandatory")
_Cdx6500DCChanStatDSDueToRstOrCng_Type = Counter32
_Cdx6500DCChanStatDSDueToRstOrCng_Object = MibTableColumn
cdx6500DCChanStatDSDueToRstOrCng = _Cdx6500DCChanStatDSDueToRstOrCng_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 21),
    _Cdx6500DCChanStatDSDueToRstOrCng_Type()
)
cdx6500DCChanStatDSDueToRstOrCng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCChanStatDSDueToRstOrCng.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContDC_ObjectIdentity = ObjectIdentity
cdx6500ContDC = _Cdx6500ContDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9)
)


class _Cdx6500ContResetAllDCStats_Type(Integer32):
    """Custom type cdx6500ContResetAllDCStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 2),
          ("reset", 1))
    )


_Cdx6500ContResetAllDCStats_Type.__name__ = "Integer32"
_Cdx6500ContResetAllDCStats_Object = MibScalar
cdx6500ContResetAllDCStats = _Cdx6500ContResetAllDCStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 1),
    _Cdx6500ContResetAllDCStats_Type()
)
cdx6500ContResetAllDCStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContResetAllDCStats.setStatus("mandatory")
_Cdx6500ContDCTable_Object = MibTable
cdx6500ContDCTable = _Cdx6500ContDCTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2)
)
if mibBuilder.loadTexts:
    cdx6500ContDCTable.setStatus("mandatory")
_Cdx6500ContDCTableEntry_Object = MibTableRow
cdx6500ContDCTableEntry = _Cdx6500ContDCTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2, 1)
)
cdx6500ContDCTableEntry.setIndexNames(
    (0, "DC-OPT-MIB", "cdx6500ContDCChanNum"),
)
if mibBuilder.loadTexts:
    cdx6500ContDCTableEntry.setStatus("mandatory")


class _Cdx6500ContDCChanNum_Type(Integer32):
    """Custom type cdx6500ContDCChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cdx6500ContDCChanNum_Type.__name__ = "Integer32"
_Cdx6500ContDCChanNum_Object = MibTableColumn
cdx6500ContDCChanNum = _Cdx6500ContDCChanNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2, 1, 1),
    _Cdx6500ContDCChanNum_Type()
)
cdx6500ContDCChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ContDCChanNum.setStatus("mandatory")


class _Cdx6500ContResetDCChanStats_Type(Integer32):
    """Custom type cdx6500ContResetDCChanStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 2),
          ("reset", 1))
    )


_Cdx6500ContResetDCChanStats_Type.__name__ = "Integer32"
_Cdx6500ContResetDCChanStats_Object = MibTableColumn
cdx6500ContResetDCChanStats = _Cdx6500ContResetDCChanStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2, 1, 2),
    _Cdx6500ContResetDCChanStats_Type()
)
cdx6500ContResetDCChanStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContResetDCChanStats.setStatus("mandatory")


class _Cdx6500ContResetDCChanVocab_Type(Integer32):
    """Custom type cdx6500ContResetDCChanVocab based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 2),
          ("reset", 1))
    )


_Cdx6500ContResetDCChanVocab_Type.__name__ = "Integer32"
_Cdx6500ContResetDCChanVocab_Object = MibTableColumn
cdx6500ContResetDCChanVocab = _Cdx6500ContResetDCChanVocab_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2, 1, 3),
    _Cdx6500ContResetDCChanVocab_Type()
)
cdx6500ContResetDCChanVocab.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContResetDCChanVocab.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatOtherStatsGroup": cdx6500StatOtherStatsGroup,
       "cdx6500DCStatTable": cdx6500DCStatTable,
       "cdx6500DCGenStatTable": cdx6500DCGenStatTable,
       "cdx6500DCGenStatTableEntry": cdx6500DCGenStatTableEntry,
       "cdx6500DCGenStatDSPStatus": cdx6500DCGenStatDSPStatus,
       "cdx6500DCGenStatHndlrSWRev": cdx6500DCGenStatHndlrSWRev,
       "cdx6500DCGenStatFnctnSWRev": cdx6500DCGenStatFnctnSWRev,
       "cdx6500DCGenStatMaxChannels": cdx6500DCGenStatMaxChannels,
       "cdx6500DCGenStatChanInUse": cdx6500DCGenStatChanInUse,
       "cdx6500DCGenStatMaxSmltChanUse": cdx6500DCGenStatMaxSmltChanUse,
       "cdx6500DCGenStatRejectConn": cdx6500DCGenStatRejectConn,
       "cdx6500DCGenStatAggCRatio": cdx6500DCGenStatAggCRatio,
       "cdx6500DCGenStatCurrEncQDepth": cdx6500DCGenStatCurrEncQDepth,
       "cdx6500DCGenStatMaxEncQDepth": cdx6500DCGenStatMaxEncQDepth,
       "cdx6500DCGenStatTmOfMaxEncQDepth": cdx6500DCGenStatTmOfMaxEncQDepth,
       "cdx6500DCGenStatCurrDecQDepth": cdx6500DCGenStatCurrDecQDepth,
       "cdx6500DCGenStatMaxDecQDepth": cdx6500DCGenStatMaxDecQDepth,
       "cdx6500DCGenStatTmOfMaxDecQDepth": cdx6500DCGenStatTmOfMaxDecQDepth,
       "cdx6500DCChanStatTable": cdx6500DCChanStatTable,
       "cdx6500DCChanStatTableEntry": cdx6500DCChanStatTableEntry,
       "cdx6500DCChanStatChanNum": cdx6500DCChanStatChanNum,
       "cdx6500DCChanStatTmOfLastStatRst": cdx6500DCChanStatTmOfLastStatRst,
       "cdx6500DCChanStatChanState": cdx6500DCChanStatChanState,
       "cdx6500DCChanStatSourceChan": cdx6500DCChanStatSourceChan,
       "cdx6500DCChanStatDestChan": cdx6500DCChanStatDestChan,
       "cdx6500DCChanStatXmitCRatio": cdx6500DCChanStatXmitCRatio,
       "cdx6500DCChanStatNumOfEncFrames": cdx6500DCChanStatNumOfEncFrames,
       "cdx6500DCChanStatNumOfCharInToEnc": cdx6500DCChanStatNumOfCharInToEnc,
       "cdx6500DCChanStatNumOfCharOutOfEnc": cdx6500DCChanStatNumOfCharOutOfEnc,
       "cdx6500DCChanStatNumOfDecFrames": cdx6500DCChanStatNumOfDecFrames,
       "cdx6500DCChanStatNumOfCharInToDec": cdx6500DCChanStatNumOfCharInToDec,
       "cdx6500DCChanStatNumOfCharOutOfDec": cdx6500DCChanStatNumOfCharOutOfDec,
       "cdx6500DCChanStatEncAETrnstnCnt": cdx6500DCChanStatEncAETrnstnCnt,
       "cdx6500DCChanStatEncAEFrameCnt": cdx6500DCChanStatEncAEFrameCnt,
       "cdx6500DCChanStatEncAEModeStatus": cdx6500DCChanStatEncAEModeStatus,
       "cdx6500DCChanStatDecAETrnstnCnt": cdx6500DCChanStatDecAETrnstnCnt,
       "cdx6500DCChanStatDecAEFrameCnt": cdx6500DCChanStatDecAEFrameCnt,
       "cdx6500DCChanStatDecAEModeStatus": cdx6500DCChanStatDecAEModeStatus,
       "cdx6500DCChanStatDSWithBadFrames": cdx6500DCChanStatDSWithBadFrames,
       "cdx6500DCChanStatDSWithBadHeaders": cdx6500DCChanStatDSWithBadHeaders,
       "cdx6500DCChanStatDSDueToRstOrCng": cdx6500DCChanStatDSDueToRstOrCng,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContDC": cdx6500ContDC,
       "cdx6500ContResetAllDCStats": cdx6500ContResetAllDCStats,
       "cdx6500ContDCTable": cdx6500ContDCTable,
       "cdx6500ContDCTableEntry": cdx6500ContDCTableEntry,
       "cdx6500ContDCChanNum": cdx6500ContDCChanNum,
       "cdx6500ContResetDCChanStats": cdx6500ContResetDCChanStats,
       "cdx6500ContResetDCChanVocab": cdx6500ContResetDCChanVocab}
)
