# SNMP MIB module (CISCO-MGX82XX-DSX3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MGX82XX-DSX3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:32 2024
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

(dsx3Framing,
 dsx3Line) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "dsx3Framing",
    "dsx3Line")

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

ciscoMgx82xxDsx3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 59)
)
ciscoMgx82xxDsx3MIB.setRevisions(
        ("2003-01-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dsx3Config_ObjectIdentity = ObjectIdentity
dsx3Config = _Dsx3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1)
)
_CwDsx3ConfigTable_Object = MibTable
cwDsx3ConfigTable = _CwDsx3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwDsx3ConfigTable.setStatus("current")
_CwDsx3ConfigEntry_Object = MibTableRow
cwDsx3ConfigEntry = _CwDsx3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1)
)
cwDsx3ConfigEntry.setIndexNames(
    (0, "CISCO-MGX82XX-DSX3-MIB", "dsx3LineNum"),
)
if mibBuilder.loadTexts:
    cwDsx3ConfigEntry.setStatus("current")


class _Dsx3LineNum_Type(Integer32):
    """Custom type dsx3LineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx3LineNum_Type.__name__ = "Integer32"
_Dsx3LineNum_Object = MibTableColumn
dsx3LineNum = _Dsx3LineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 1),
    _Dsx3LineNum_Type()
)
dsx3LineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LineNum.setStatus("current")


class _CwDsx3LineType_Type(Integer32):
    """Custom type cwDsx3LineType based on Integer32"""
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
        *(("dsx3CbitParity", 1),
          ("dsx3M23", 3),
          ("dsx3Unframed", 5),
          ("e3Unframed", 6),
          ("g751", 4),
          ("g832-g804", 2))
    )


_CwDsx3LineType_Type.__name__ = "Integer32"
_CwDsx3LineType_Object = MibTableColumn
cwDsx3LineType = _CwDsx3LineType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 2),
    _CwDsx3LineType_Type()
)
cwDsx3LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwDsx3LineType.setStatus("current")


class _CwDsx3LineCoding_Type(Integer32):
    """Custom type cwDsx3LineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsx3B3ZS", 1),
          ("e3HDB3", 2))
    )


_CwDsx3LineCoding_Type.__name__ = "Integer32"
_CwDsx3LineCoding_Object = MibTableColumn
cwDsx3LineCoding = _CwDsx3LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 3),
    _CwDsx3LineCoding_Type()
)
cwDsx3LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwDsx3LineCoding.setStatus("current")


class _CwDsx3LineLength_Type(Integer32):
    """Custom type cwDsx3LineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessThan225", 1),
          ("moreThan225", 2))
    )


_CwDsx3LineLength_Type.__name__ = "Integer32"
_CwDsx3LineLength_Object = MibTableColumn
cwDsx3LineLength = _CwDsx3LineLength_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 4),
    _CwDsx3LineLength_Type()
)
cwDsx3LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwDsx3LineLength.setStatus("current")


class _Dsx3LineOOFCriteria_Type(Integer32):
    """Custom type dsx3LineOOFCriteria based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fBits3Of16", 2),
          ("fBits3Of8", 1),
          ("notApplicable", 3))
    )


_Dsx3LineOOFCriteria_Type.__name__ = "Integer32"
_Dsx3LineOOFCriteria_Object = MibTableColumn
dsx3LineOOFCriteria = _Dsx3LineOOFCriteria_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 5),
    _Dsx3LineOOFCriteria_Type()
)
dsx3LineOOFCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineOOFCriteria.setStatus("current")


class _Dsx3LineAIScBitsCheck_Type(Integer32):
    """Custom type dsx3LineAIScBitsCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("checkCbits", 1),
          ("ignorebits", 2),
          ("notApplicable", 3))
    )


_Dsx3LineAIScBitsCheck_Type.__name__ = "Integer32"
_Dsx3LineAIScBitsCheck_Object = MibTableColumn
dsx3LineAIScBitsCheck = _Dsx3LineAIScBitsCheck_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 6),
    _Dsx3LineAIScBitsCheck_Type()
)
dsx3LineAIScBitsCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineAIScBitsCheck.setStatus("current")


class _Dsx3LineLoopbackCommand_Type(Integer32):
    """Custom type dsx3LineLoopbackCommand based on Integer32"""
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
        *(("dsx3InbndLocalLoopback", 4),
          ("dsx3LocalLineLoop", 3),
          ("dsx3NoLoop", 1),
          ("dsx3RemoteLineLoop", 2))
    )


_Dsx3LineLoopbackCommand_Type.__name__ = "Integer32"
_Dsx3LineLoopbackCommand_Object = MibTableColumn
dsx3LineLoopbackCommand = _Dsx3LineLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 7),
    _Dsx3LineLoopbackCommand_Type()
)
dsx3LineLoopbackCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineLoopbackCommand.setStatus("current")


class _Dsx3LineRcvFEACValidation_Type(Integer32):
    """Custom type dsx3LineRcvFEACValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fFEACCodes4Of5", 1),
          ("fFEACCodes8Of10", 2),
          ("fFEACCodesDisable", 3))
    )


_Dsx3LineRcvFEACValidation_Type.__name__ = "Integer32"
_Dsx3LineRcvFEACValidation_Object = MibTableColumn
dsx3LineRcvFEACValidation = _Dsx3LineRcvFEACValidation_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 8),
    _Dsx3LineRcvFEACValidation_Type()
)
dsx3LineRcvFEACValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineRcvFEACValidation.setStatus("current")


class _Dsx3LineXmtFEACCode_Type(Integer32):
    """Custom type dsx3LineXmtFEACCode based on Integer32"""
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
        *(("dsx3SendDS1LoopCode", 5),
          ("dsx3SendLineCode", 2),
          ("dsx3SendNoCode", 1),
          ("dsx3SendPayloadCode", 3),
          ("dsx3SendResetCode", 4),
          ("dsx3SendTestPattern", 6))
    )


_Dsx3LineXmtFEACCode_Type.__name__ = "Integer32"
_Dsx3LineXmtFEACCode_Object = MibTableColumn
dsx3LineXmtFEACCode = _Dsx3LineXmtFEACCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 9),
    _Dsx3LineXmtFEACCode_Type()
)
dsx3LineXmtFEACCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineXmtFEACCode.setStatus("current")


class _Dsx3LineBERTEnable_Type(Integer32):
    """Custom type dsx3LineBERTEnable based on Integer32"""
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


_Dsx3LineBERTEnable_Type.__name__ = "Integer32"
_Dsx3LineBERTEnable_Object = MibTableColumn
dsx3LineBERTEnable = _Dsx3LineBERTEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 10),
    _Dsx3LineBERTEnable_Type()
)
dsx3LineBERTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineBERTEnable.setStatus("current")


class _Dsx3LineBERTPattern_Type(Integer32):
    """Custom type dsx3LineBERTPattern based on Integer32"""
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
        *(("allOnes", 2),
          ("allZero", 1),
          ("alternateOneZero", 3),
          ("doubleOneZero", 4),
          ("pattern2p15minus1", 9),
          ("pattern2p20minus1", 10),
          ("pattern2p23minus1", 11),
          ("userFourWords", 8),
          ("userOneWord", 5),
          ("userThreeWords", 7),
          ("userTwoWords", 6))
    )


_Dsx3LineBERTPattern_Type.__name__ = "Integer32"
_Dsx3LineBERTPattern_Object = MibTableColumn
dsx3LineBERTPattern = _Dsx3LineBERTPattern_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 11),
    _Dsx3LineBERTPattern_Type()
)
dsx3LineBERTPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineBERTPattern.setStatus("current")


class _Dsx3LineBERTResult_Type(Integer32):
    """Custom type dsx3LineBERTResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bertFailed", 1),
          ("bertPassed", 2))
    )


_Dsx3LineBERTResult_Type.__name__ = "Integer32"
_Dsx3LineBERTResult_Object = MibTableColumn
dsx3LineBERTResult = _Dsx3LineBERTResult_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 12),
    _Dsx3LineBERTResult_Type()
)
dsx3LineBERTResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LineBERTResult.setStatus("current")


class _Dsx3BERTResultClrButton_Type(Integer32):
    """Custom type dsx3BERTResultClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_Dsx3BERTResultClrButton_Type.__name__ = "Integer32"
_Dsx3BERTResultClrButton_Object = MibTableColumn
dsx3BERTResultClrButton = _Dsx3BERTResultClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 13),
    _Dsx3BERTResultClrButton_Type()
)
dsx3BERTResultClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3BERTResultClrButton.setStatus("current")


class _Dsx3TrailTraceOption_Type(Integer32):
    """Custom type dsx3TrailTraceOption based on Integer32"""
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


_Dsx3TrailTraceOption_Type.__name__ = "Integer32"
_Dsx3TrailTraceOption_Object = MibTableColumn
dsx3TrailTraceOption = _Dsx3TrailTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 14),
    _Dsx3TrailTraceOption_Type()
)
dsx3TrailTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3TrailTraceOption.setStatus("current")


class _Dsx3TxTrailTrace_Type(DisplayString):
    """Custom type dsx3TxTrailTrace based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Dsx3TxTrailTrace_Type.__name__ = "DisplayString"
_Dsx3TxTrailTrace_Object = MibTableColumn
dsx3TxTrailTrace = _Dsx3TxTrailTrace_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 15),
    _Dsx3TxTrailTrace_Type()
)
dsx3TxTrailTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3TxTrailTrace.setStatus("current")


class _Dsx3RxTrailTrace_Type(DisplayString):
    """Custom type dsx3RxTrailTrace based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Dsx3RxTrailTrace_Type.__name__ = "DisplayString"
_Dsx3RxTrailTrace_Object = MibTableColumn
dsx3RxTrailTrace = _Dsx3RxTrailTrace_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 16),
    _Dsx3RxTrailTrace_Type()
)
dsx3RxTrailTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3RxTrailTrace.setStatus("current")


class _Dsx3TxTimingMarker_Type(Integer32):
    """Custom type dsx3TxTimingMarker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("traceable", 1),
          ("untraceable", 2))
    )


_Dsx3TxTimingMarker_Type.__name__ = "Integer32"
_Dsx3TxTimingMarker_Object = MibTableColumn
dsx3TxTimingMarker = _Dsx3TxTimingMarker_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 17),
    _Dsx3TxTimingMarker_Type()
)
dsx3TxTimingMarker.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3TxTimingMarker.setStatus("current")


class _Dsx3RxTimingMarker_Type(Integer32):
    """Custom type dsx3RxTimingMarker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("traceable", 1),
          ("untraceable", 2))
    )


_Dsx3RxTimingMarker_Type.__name__ = "Integer32"
_Dsx3RxTimingMarker_Object = MibTableColumn
dsx3RxTimingMarker = _Dsx3RxTimingMarker_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 18),
    _Dsx3RxTimingMarker_Type()
)
dsx3RxTimingMarker.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3RxTimingMarker.setStatus("current")


class _Dsx3TxPayloadType_Type(Integer32):
    """Custom type dsx3TxPayloadType based on Integer32"""
    defaultValue = 1

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
        *(("atm", 3),
          ("equipped", 2),
          ("sdhtu12s", 4),
          ("unequipped", 1))
    )


_Dsx3TxPayloadType_Type.__name__ = "Integer32"
_Dsx3TxPayloadType_Object = MibTableColumn
dsx3TxPayloadType = _Dsx3TxPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 19),
    _Dsx3TxPayloadType_Type()
)
dsx3TxPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3TxPayloadType.setStatus("current")


class _Dsx3RxPayloadType_Type(Integer32):
    """Custom type dsx3RxPayloadType based on Integer32"""
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
        *(("atm", 3),
          ("equipped", 2),
          ("sdhtu12s", 4),
          ("unequipped", 1))
    )


_Dsx3RxPayloadType_Type.__name__ = "Integer32"
_Dsx3RxPayloadType_Object = MibTableColumn
dsx3RxPayloadType = _Dsx3RxPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 20),
    _Dsx3RxPayloadType_Type()
)
dsx3RxPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3RxPayloadType.setStatus("current")


class _Dsx3TxTumf_Type(Integer32):
    """Custom type dsx3TxTumf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Dsx3TxTumf_Type.__name__ = "Integer32"
_Dsx3TxTumf_Object = MibTableColumn
dsx3TxTumf = _Dsx3TxTumf_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 21),
    _Dsx3TxTumf_Type()
)
dsx3TxTumf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3TxTumf.setStatus("current")


class _Dsx3RxTumf_Type(Integer32):
    """Custom type dsx3RxTumf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Dsx3RxTumf_Type.__name__ = "Integer32"
_Dsx3RxTumf_Object = MibTableColumn
dsx3RxTumf = _Dsx3RxTumf_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 22),
    _Dsx3RxTumf_Type()
)
dsx3RxTumf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3RxTumf.setStatus("current")


class _Dsx3LineEnable_Type(Integer32):
    """Custom type dsx3LineEnable based on Integer32"""
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
          ("enable", 2),
          ("modify", 3))
    )


_Dsx3LineEnable_Type.__name__ = "Integer32"
_Dsx3LineEnable_Object = MibTableColumn
dsx3LineEnable = _Dsx3LineEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 23),
    _Dsx3LineEnable_Type()
)
dsx3LineEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineEnable.setStatus("current")


class _Dsx3FarEndLoopbkLineNum_Type(Integer32):
    """Custom type dsx3FarEndLoopbkLineNum based on Integer32"""
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
              30)
        )
    )
    namedValues = NamedValues(
        *(("ds1line1", 1),
          ("ds1line10", 10),
          ("ds1line11", 11),
          ("ds1line12", 12),
          ("ds1line13", 13),
          ("ds1line14", 14),
          ("ds1line15", 15),
          ("ds1line16", 16),
          ("ds1line17", 17),
          ("ds1line18", 18),
          ("ds1line19", 19),
          ("ds1line2", 2),
          ("ds1line20", 20),
          ("ds1line21", 21),
          ("ds1line22", 22),
          ("ds1line23", 23),
          ("ds1line24", 24),
          ("ds1line25", 25),
          ("ds1line26", 26),
          ("ds1line27", 27),
          ("ds1line28", 28),
          ("ds1line29", 29),
          ("ds1line3", 3),
          ("ds1line4", 4),
          ("ds1line5", 5),
          ("ds1line6", 6),
          ("ds1line7", 7),
          ("ds1line8", 8),
          ("ds1line9", 9),
          ("ds3line", 30))
    )


_Dsx3FarEndLoopbkLineNum_Type.__name__ = "Integer32"
_Dsx3FarEndLoopbkLineNum_Object = MibTableColumn
dsx3FarEndLoopbkLineNum = _Dsx3FarEndLoopbkLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 24),
    _Dsx3FarEndLoopbkLineNum_Type()
)
dsx3FarEndLoopbkLineNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3FarEndLoopbkLineNum.setStatus("current")


class _Dsx3LineXmtClockSrc_Type(Integer32):
    """Custom type dsx3LineXmtClockSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backplaneClk", 1),
          ("localClk", 3),
          ("recoverClk", 2))
    )


_Dsx3LineXmtClockSrc_Type.__name__ = "Integer32"
_Dsx3LineXmtClockSrc_Object = MibTableColumn
dsx3LineXmtClockSrc = _Dsx3LineXmtClockSrc_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 25),
    _Dsx3LineXmtClockSrc_Type()
)
dsx3LineXmtClockSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineXmtClockSrc.setStatus("current")


class _Dsx3FarEndLoopbkLineStatus_Type(Integer32):
    """Custom type dsx3FarEndLoopbkLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3FarEndLoopbkLineStatus_Type.__name__ = "Integer32"
_Dsx3FarEndLoopbkLineStatus_Object = MibTableColumn
dsx3FarEndLoopbkLineStatus = _Dsx3FarEndLoopbkLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 26),
    _Dsx3FarEndLoopbkLineStatus_Type()
)
dsx3FarEndLoopbkLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FarEndLoopbkLineStatus.setStatus("current")


class _Dsx3LineEqualizer_Type(Integer32):
    """Custom type dsx3LineEqualizer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extequalizer", 2),
          ("intrnlequalizer", 1))
    )


_Dsx3LineEqualizer_Type.__name__ = "Integer32"
_Dsx3LineEqualizer_Object = MibTableColumn
dsx3LineEqualizer = _Dsx3LineEqualizer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 27),
    _Dsx3LineEqualizer_Type()
)
dsx3LineEqualizer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineEqualizer.setStatus("current")


class _Dsx3NearEndLoopbkLineStatus_Type(Integer32):
    """Custom type dsx3NearEndLoopbkLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3NearEndLoopbkLineStatus_Type.__name__ = "Integer32"
_Dsx3NearEndLoopbkLineStatus_Object = MibTableColumn
dsx3NearEndLoopbkLineStatus = _Dsx3NearEndLoopbkLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 28),
    _Dsx3NearEndLoopbkLineStatus_Type()
)
dsx3NearEndLoopbkLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3NearEndLoopbkLineStatus.setStatus("current")


class _Dsx3SubRateEnable_Type(Integer32):
    """Custom type dsx3SubRateEnable based on Integer32"""
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


_Dsx3SubRateEnable_Type.__name__ = "Integer32"
_Dsx3SubRateEnable_Object = MibTableColumn
dsx3SubRateEnable = _Dsx3SubRateEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 29),
    _Dsx3SubRateEnable_Type()
)
dsx3SubRateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3SubRateEnable.setStatus("current")


class _Dsx3DsuSelect_Type(Integer32):
    """Custom type dsx3DsuSelect based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("adcKentroxMode", 2),
          ("clearChannel", 4),
          ("dl3100Mode", 1),
          ("dsuAlgorithm2", 5),
          ("dsuAlgorithm3", 6),
          ("dsuAlgorithm4", 7),
          ("dsuAlgorithm5", 8),
          ("larsCom", 3))
    )


_Dsx3DsuSelect_Type.__name__ = "Integer32"
_Dsx3DsuSelect_Object = MibTableColumn
dsx3DsuSelect = _Dsx3DsuSelect_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 30),
    _Dsx3DsuSelect_Type()
)
dsx3DsuSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3DsuSelect.setStatus("current")


class _Dsx3LineRate_Type(Integer32):
    """Custom type dsx3LineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 44736),
    )


_Dsx3LineRate_Type.__name__ = "Integer32"
_Dsx3LineRate_Object = MibTableColumn
dsx3LineRate = _Dsx3LineRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 31),
    _Dsx3LineRate_Type()
)
dsx3LineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineRate.setStatus("current")
if mibBuilder.loadTexts:
    dsx3LineRate.setUnits("kbps")


class _Dsx3LineScrambleEnable_Type(Integer32):
    """Custom type dsx3LineScrambleEnable based on Integer32"""
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


_Dsx3LineScrambleEnable_Type.__name__ = "Integer32"
_Dsx3LineScrambleEnable_Object = MibTableColumn
dsx3LineScrambleEnable = _Dsx3LineScrambleEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 1, 1, 32),
    _Dsx3LineScrambleEnable_Type()
)
dsx3LineScrambleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineScrambleEnable.setStatus("current")


class _Dsx3LineNumOfValidEntries_Type(Integer32):
    """Custom type dsx3LineNumOfValidEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3LineNumOfValidEntries_Type.__name__ = "Integer32"
_Dsx3LineNumOfValidEntries_Object = MibScalar
dsx3LineNumOfValidEntries = _Dsx3LineNumOfValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 1, 2),
    _Dsx3LineNumOfValidEntries_Type()
)
dsx3LineNumOfValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LineNumOfValidEntries.setStatus("current")
_Dsx3AlarmConfig_ObjectIdentity = ObjectIdentity
dsx3AlarmConfig = _Dsx3AlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2)
)
_Dsx3AlarmConfigTable_Object = MibTable
dsx3AlarmConfigTable = _Dsx3AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dsx3AlarmConfigTable.setStatus("current")
_Dsx3AlarmConfigEntry_Object = MibTableRow
dsx3AlarmConfigEntry = _Dsx3AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1)
)
dsx3AlarmConfigEntry.setIndexNames(
    (0, "CISCO-MGX82XX-DSX3-MIB", "dsx3LineNum"),
)
if mibBuilder.loadTexts:
    dsx3AlarmConfigEntry.setStatus("current")


class _Dsx3RedSeverity_Type(Integer32):
    """Custom type dsx3RedSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1))
    )


_Dsx3RedSeverity_Type.__name__ = "Integer32"
_Dsx3RedSeverity_Object = MibTableColumn
dsx3RedSeverity = _Dsx3RedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 1),
    _Dsx3RedSeverity_Type()
)
dsx3RedSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3RedSeverity.setStatus("current")


class _Dsx3RAISeverity_Type(Integer32):
    """Custom type dsx3RAISeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1))
    )


_Dsx3RAISeverity_Type.__name__ = "Integer32"
_Dsx3RAISeverity_Object = MibTableColumn
dsx3RAISeverity = _Dsx3RAISeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 2),
    _Dsx3RAISeverity_Type()
)
dsx3RAISeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3RAISeverity.setStatus("current")


class _Dsx3NEAlarmUpCount_Type(Integer32):
    """Custom type dsx3NEAlarmUpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3NEAlarmUpCount_Type.__name__ = "Integer32"
_Dsx3NEAlarmUpCount_Object = MibTableColumn
dsx3NEAlarmUpCount = _Dsx3NEAlarmUpCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 3),
    _Dsx3NEAlarmUpCount_Type()
)
dsx3NEAlarmUpCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3NEAlarmUpCount.setStatus("current")


class _Dsx3NEAlarmDownCount_Type(Integer32):
    """Custom type dsx3NEAlarmDownCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3NEAlarmDownCount_Type.__name__ = "Integer32"
_Dsx3NEAlarmDownCount_Object = MibTableColumn
dsx3NEAlarmDownCount = _Dsx3NEAlarmDownCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 4),
    _Dsx3NEAlarmDownCount_Type()
)
dsx3NEAlarmDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3NEAlarmDownCount.setStatus("current")


class _Dsx3NEAlarmThreshold_Type(Integer32):
    """Custom type dsx3NEAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3NEAlarmThreshold_Type.__name__ = "Integer32"
_Dsx3NEAlarmThreshold_Object = MibTableColumn
dsx3NEAlarmThreshold = _Dsx3NEAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 5),
    _Dsx3NEAlarmThreshold_Type()
)
dsx3NEAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3NEAlarmThreshold.setStatus("current")


class _Dsx3FEAlarmUpCount_Type(Integer32):
    """Custom type dsx3FEAlarmUpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3FEAlarmUpCount_Type.__name__ = "Integer32"
_Dsx3FEAlarmUpCount_Object = MibTableColumn
dsx3FEAlarmUpCount = _Dsx3FEAlarmUpCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 6),
    _Dsx3FEAlarmUpCount_Type()
)
dsx3FEAlarmUpCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3FEAlarmUpCount.setStatus("current")


class _Dsx3FEAlarmDownCount_Type(Integer32):
    """Custom type dsx3FEAlarmDownCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3FEAlarmDownCount_Type.__name__ = "Integer32"
_Dsx3FEAlarmDownCount_Object = MibTableColumn
dsx3FEAlarmDownCount = _Dsx3FEAlarmDownCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 7),
    _Dsx3FEAlarmDownCount_Type()
)
dsx3FEAlarmDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3FEAlarmDownCount.setStatus("current")


class _Dsx3FEAlarmThreshold_Type(Integer32):
    """Custom type dsx3FEAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3FEAlarmThreshold_Type.__name__ = "Integer32"
_Dsx3FEAlarmThreshold_Object = MibTableColumn
dsx3FEAlarmThreshold = _Dsx3FEAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 8),
    _Dsx3FEAlarmThreshold_Type()
)
dsx3FEAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3FEAlarmThreshold.setStatus("current")


class _Dsx3StatisticalAlarmSeverity_Type(Integer32):
    """Custom type dsx3StatisticalAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1))
    )


_Dsx3StatisticalAlarmSeverity_Type.__name__ = "Integer32"
_Dsx3StatisticalAlarmSeverity_Object = MibTableColumn
dsx3StatisticalAlarmSeverity = _Dsx3StatisticalAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 9),
    _Dsx3StatisticalAlarmSeverity_Type()
)
dsx3StatisticalAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3StatisticalAlarmSeverity.setStatus("current")


class _Dsx3LCV15MinThreshold_Type(Integer32):
    """Custom type dsx3LCV15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3LCV15MinThreshold_Type.__name__ = "Integer32"
_Dsx3LCV15MinThreshold_Object = MibTableColumn
dsx3LCV15MinThreshold = _Dsx3LCV15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 10),
    _Dsx3LCV15MinThreshold_Type()
)
dsx3LCV15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LCV15MinThreshold.setStatus("current")


class _Dsx3LCV24HrThreshold_Type(Integer32):
    """Custom type dsx3LCV24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3LCV24HrThreshold_Type.__name__ = "Integer32"
_Dsx3LCV24HrThreshold_Object = MibTableColumn
dsx3LCV24HrThreshold = _Dsx3LCV24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 11),
    _Dsx3LCV24HrThreshold_Type()
)
dsx3LCV24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LCV24HrThreshold.setStatus("current")


class _Dsx3LES15MinThreshold_Type(Integer32):
    """Custom type dsx3LES15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3LES15MinThreshold_Type.__name__ = "Integer32"
_Dsx3LES15MinThreshold_Object = MibTableColumn
dsx3LES15MinThreshold = _Dsx3LES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 12),
    _Dsx3LES15MinThreshold_Type()
)
dsx3LES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LES15MinThreshold.setStatus("current")


class _Dsx3LES24HrThreshold_Type(Integer32):
    """Custom type dsx3LES24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3LES24HrThreshold_Type.__name__ = "Integer32"
_Dsx3LES24HrThreshold_Object = MibTableColumn
dsx3LES24HrThreshold = _Dsx3LES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 13),
    _Dsx3LES24HrThreshold_Type()
)
dsx3LES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LES24HrThreshold.setStatus("current")


class _Dsx3LSES15MinThreshold_Type(Integer32):
    """Custom type dsx3LSES15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3LSES15MinThreshold_Type.__name__ = "Integer32"
_Dsx3LSES15MinThreshold_Object = MibTableColumn
dsx3LSES15MinThreshold = _Dsx3LSES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 14),
    _Dsx3LSES15MinThreshold_Type()
)
dsx3LSES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LSES15MinThreshold.setStatus("current")


class _Dsx3LSES24HrThreshold_Type(Integer32):
    """Custom type dsx3LSES24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3LSES24HrThreshold_Type.__name__ = "Integer32"
_Dsx3LSES24HrThreshold_Object = MibTableColumn
dsx3LSES24HrThreshold = _Dsx3LSES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 15),
    _Dsx3LSES24HrThreshold_Type()
)
dsx3LSES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LSES24HrThreshold.setStatus("current")


class _Dsx3PCV15MinThreshold_Type(Integer32):
    """Custom type dsx3PCV15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PCV15MinThreshold_Type.__name__ = "Integer32"
_Dsx3PCV15MinThreshold_Object = MibTableColumn
dsx3PCV15MinThreshold = _Dsx3PCV15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 16),
    _Dsx3PCV15MinThreshold_Type()
)
dsx3PCV15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PCV15MinThreshold.setStatus("current")


class _Dsx3PCV24HrThreshold_Type(Integer32):
    """Custom type dsx3PCV24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PCV24HrThreshold_Type.__name__ = "Integer32"
_Dsx3PCV24HrThreshold_Object = MibTableColumn
dsx3PCV24HrThreshold = _Dsx3PCV24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 17),
    _Dsx3PCV24HrThreshold_Type()
)
dsx3PCV24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PCV24HrThreshold.setStatus("current")


class _Dsx3PES15MinThreshold_Type(Integer32):
    """Custom type dsx3PES15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PES15MinThreshold_Type.__name__ = "Integer32"
_Dsx3PES15MinThreshold_Object = MibTableColumn
dsx3PES15MinThreshold = _Dsx3PES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 18),
    _Dsx3PES15MinThreshold_Type()
)
dsx3PES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PES15MinThreshold.setStatus("current")


class _Dsx3PES24HrThreshold_Type(Integer32):
    """Custom type dsx3PES24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PES24HrThreshold_Type.__name__ = "Integer32"
_Dsx3PES24HrThreshold_Object = MibTableColumn
dsx3PES24HrThreshold = _Dsx3PES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 19),
    _Dsx3PES24HrThreshold_Type()
)
dsx3PES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PES24HrThreshold.setStatus("current")


class _Dsx3PSES15MinThreshold_Type(Integer32):
    """Custom type dsx3PSES15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PSES15MinThreshold_Type.__name__ = "Integer32"
_Dsx3PSES15MinThreshold_Object = MibTableColumn
dsx3PSES15MinThreshold = _Dsx3PSES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 20),
    _Dsx3PSES15MinThreshold_Type()
)
dsx3PSES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PSES15MinThreshold.setStatus("current")


class _Dsx3PSES24HrThreshold_Type(Integer32):
    """Custom type dsx3PSES24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PSES24HrThreshold_Type.__name__ = "Integer32"
_Dsx3PSES24HrThreshold_Object = MibTableColumn
dsx3PSES24HrThreshold = _Dsx3PSES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 21),
    _Dsx3PSES24HrThreshold_Type()
)
dsx3PSES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PSES24HrThreshold.setStatus("current")


class _Dsx3SEFS15MinThreshold_Type(Integer32):
    """Custom type dsx3SEFS15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3SEFS15MinThreshold_Type.__name__ = "Integer32"
_Dsx3SEFS15MinThreshold_Object = MibTableColumn
dsx3SEFS15MinThreshold = _Dsx3SEFS15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 22),
    _Dsx3SEFS15MinThreshold_Type()
)
dsx3SEFS15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3SEFS15MinThreshold.setStatus("current")


class _Dsx3SEFS24HrThreshold_Type(Integer32):
    """Custom type dsx3SEFS24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3SEFS24HrThreshold_Type.__name__ = "Integer32"
_Dsx3SEFS24HrThreshold_Object = MibTableColumn
dsx3SEFS24HrThreshold = _Dsx3SEFS24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 23),
    _Dsx3SEFS24HrThreshold_Type()
)
dsx3SEFS24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3SEFS24HrThreshold.setStatus("current")


class _Dsx3AISS15MinThreshold_Type(Integer32):
    """Custom type dsx3AISS15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3AISS15MinThreshold_Type.__name__ = "Integer32"
_Dsx3AISS15MinThreshold_Object = MibTableColumn
dsx3AISS15MinThreshold = _Dsx3AISS15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 24),
    _Dsx3AISS15MinThreshold_Type()
)
dsx3AISS15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3AISS15MinThreshold.setStatus("current")


class _Dsx3AISS24HrThreshold_Type(Integer32):
    """Custom type dsx3AISS24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3AISS24HrThreshold_Type.__name__ = "Integer32"
_Dsx3AISS24HrThreshold_Object = MibTableColumn
dsx3AISS24HrThreshold = _Dsx3AISS24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 25),
    _Dsx3AISS24HrThreshold_Type()
)
dsx3AISS24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3AISS24HrThreshold.setStatus("current")


class _Dsx3UAS15MinThreshold_Type(Integer32):
    """Custom type dsx3UAS15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3UAS15MinThreshold_Type.__name__ = "Integer32"
_Dsx3UAS15MinThreshold_Object = MibTableColumn
dsx3UAS15MinThreshold = _Dsx3UAS15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 26),
    _Dsx3UAS15MinThreshold_Type()
)
dsx3UAS15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3UAS15MinThreshold.setStatus("current")


class _Dsx3UAS24HrThreshold_Type(Integer32):
    """Custom type dsx3UAS24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3UAS24HrThreshold_Type.__name__ = "Integer32"
_Dsx3UAS24HrThreshold_Object = MibTableColumn
dsx3UAS24HrThreshold = _Dsx3UAS24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 27),
    _Dsx3UAS24HrThreshold_Type()
)
dsx3UAS24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3UAS24HrThreshold.setStatus("current")


class _Dsx3E3BIP8CV15MinThreshold_Type(Integer32):
    """Custom type dsx3E3BIP8CV15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3E3BIP8CV15MinThreshold_Type.__name__ = "Integer32"
_Dsx3E3BIP8CV15MinThreshold_Object = MibTableColumn
dsx3E3BIP8CV15MinThreshold = _Dsx3E3BIP8CV15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 28),
    _Dsx3E3BIP8CV15MinThreshold_Type()
)
dsx3E3BIP8CV15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3E3BIP8CV15MinThreshold.setStatus("current")


class _Dsx3E3BIP8CV24HrThreshold_Type(Integer32):
    """Custom type dsx3E3BIP8CV24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3E3BIP8CV24HrThreshold_Type.__name__ = "Integer32"
_Dsx3E3BIP8CV24HrThreshold_Object = MibTableColumn
dsx3E3BIP8CV24HrThreshold = _Dsx3E3BIP8CV24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 29),
    _Dsx3E3BIP8CV24HrThreshold_Type()
)
dsx3E3BIP8CV24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3E3BIP8CV24HrThreshold.setStatus("current")


class _Dsx3E3BIP8ES15MinThreshold_Type(Integer32):
    """Custom type dsx3E3BIP8ES15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3E3BIP8ES15MinThreshold_Type.__name__ = "Integer32"
_Dsx3E3BIP8ES15MinThreshold_Object = MibTableColumn
dsx3E3BIP8ES15MinThreshold = _Dsx3E3BIP8ES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 30),
    _Dsx3E3BIP8ES15MinThreshold_Type()
)
dsx3E3BIP8ES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3E3BIP8ES15MinThreshold.setStatus("current")


class _Dsx3E3BIP8ES24HrThreshold_Type(Integer32):
    """Custom type dsx3E3BIP8ES24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3E3BIP8ES24HrThreshold_Type.__name__ = "Integer32"
_Dsx3E3BIP8ES24HrThreshold_Object = MibTableColumn
dsx3E3BIP8ES24HrThreshold = _Dsx3E3BIP8ES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 31),
    _Dsx3E3BIP8ES24HrThreshold_Type()
)
dsx3E3BIP8ES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3E3BIP8ES24HrThreshold.setStatus("current")


class _Dsx3E3BIP8SES15MinThreshold_Type(Integer32):
    """Custom type dsx3E3BIP8SES15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3E3BIP8SES15MinThreshold_Type.__name__ = "Integer32"
_Dsx3E3BIP8SES15MinThreshold_Object = MibTableColumn
dsx3E3BIP8SES15MinThreshold = _Dsx3E3BIP8SES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 32),
    _Dsx3E3BIP8SES15MinThreshold_Type()
)
dsx3E3BIP8SES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3E3BIP8SES15MinThreshold.setStatus("current")


class _Dsx3E3BIP8SES24HrThreshold_Type(Integer32):
    """Custom type dsx3E3BIP8SES24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3E3BIP8SES24HrThreshold_Type.__name__ = "Integer32"
_Dsx3E3BIP8SES24HrThreshold_Object = MibTableColumn
dsx3E3BIP8SES24HrThreshold = _Dsx3E3BIP8SES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 33),
    _Dsx3E3BIP8SES24HrThreshold_Type()
)
dsx3E3BIP8SES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3E3BIP8SES24HrThreshold.setStatus("current")


class _Dsx3CCV15MinThreshold_Type(Integer32):
    """Custom type dsx3CCV15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3CCV15MinThreshold_Type.__name__ = "Integer32"
_Dsx3CCV15MinThreshold_Object = MibTableColumn
dsx3CCV15MinThreshold = _Dsx3CCV15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 34),
    _Dsx3CCV15MinThreshold_Type()
)
dsx3CCV15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3CCV15MinThreshold.setStatus("current")


class _Dsx3CCV24HrThreshold_Type(Integer32):
    """Custom type dsx3CCV24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3CCV24HrThreshold_Type.__name__ = "Integer32"
_Dsx3CCV24HrThreshold_Object = MibTableColumn
dsx3CCV24HrThreshold = _Dsx3CCV24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 35),
    _Dsx3CCV24HrThreshold_Type()
)
dsx3CCV24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3CCV24HrThreshold.setStatus("current")


class _Dsx3CES15MinThreshold_Type(Integer32):
    """Custom type dsx3CES15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3CES15MinThreshold_Type.__name__ = "Integer32"
_Dsx3CES15MinThreshold_Object = MibTableColumn
dsx3CES15MinThreshold = _Dsx3CES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 36),
    _Dsx3CES15MinThreshold_Type()
)
dsx3CES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3CES15MinThreshold.setStatus("current")


class _Dsx3CES24HrThreshold_Type(Integer32):
    """Custom type dsx3CES24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3CES24HrThreshold_Type.__name__ = "Integer32"
_Dsx3CES24HrThreshold_Object = MibTableColumn
dsx3CES24HrThreshold = _Dsx3CES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 37),
    _Dsx3CES24HrThreshold_Type()
)
dsx3CES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3CES24HrThreshold.setStatus("current")


class _Dsx3CSES15MinThreshold_Type(Integer32):
    """Custom type dsx3CSES15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3CSES15MinThreshold_Type.__name__ = "Integer32"
_Dsx3CSES15MinThreshold_Object = MibTableColumn
dsx3CSES15MinThreshold = _Dsx3CSES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 38),
    _Dsx3CSES15MinThreshold_Type()
)
dsx3CSES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3CSES15MinThreshold.setStatus("current")


class _Dsx3CSES24HrThreshold_Type(Integer32):
    """Custom type dsx3CSES24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3CSES24HrThreshold_Type.__name__ = "Integer32"
_Dsx3CSES24HrThreshold_Object = MibTableColumn
dsx3CSES24HrThreshold = _Dsx3CSES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 2, 1, 1, 39),
    _Dsx3CSES24HrThreshold_Type()
)
dsx3CSES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3CSES24HrThreshold.setStatus("current")
_Dsx3Alarm_ObjectIdentity = ObjectIdentity
dsx3Alarm = _Dsx3Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3)
)
_Dsx3AlarmTable_Object = MibTable
dsx3AlarmTable = _Dsx3AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dsx3AlarmTable.setStatus("current")
_Dsx3AlarmEntry_Object = MibTableRow
dsx3AlarmEntry = _Dsx3AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1)
)
dsx3AlarmEntry.setIndexNames(
    (0, "CISCO-MGX82XX-DSX3-MIB", "dsx3LineNum"),
)
if mibBuilder.loadTexts:
    dsx3AlarmEntry.setStatus("current")


class _Dsx3LineAlarmState_Type(Integer32):
    """Custom type dsx3LineAlarmState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3LineAlarmState_Type.__name__ = "Integer32"
_Dsx3LineAlarmState_Object = MibTableColumn
dsx3LineAlarmState = _Dsx3LineAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 1),
    _Dsx3LineAlarmState_Type()
)
dsx3LineAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LineAlarmState.setStatus("current")


class _Dsx3LineStatisticalAlarmState_Type(Integer32):
    """Custom type dsx3LineStatisticalAlarmState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3LineStatisticalAlarmState_Type.__name__ = "Integer32"
_Dsx3LineStatisticalAlarmState_Object = MibTableColumn
dsx3LineStatisticalAlarmState = _Dsx3LineStatisticalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 2),
    _Dsx3LineStatisticalAlarmState_Type()
)
dsx3LineStatisticalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LineStatisticalAlarmState.setStatus("current")
_Dsx3LCVCurrent_Type = Counter32
_Dsx3LCVCurrent_Object = MibTableColumn
dsx3LCVCurrent = _Dsx3LCVCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 3),
    _Dsx3LCVCurrent_Type()
)
dsx3LCVCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LCVCurrent.setStatus("current")
_Dsx3LCV15MinBucket_Type = Counter32
_Dsx3LCV15MinBucket_Object = MibTableColumn
dsx3LCV15MinBucket = _Dsx3LCV15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 4),
    _Dsx3LCV15MinBucket_Type()
)
dsx3LCV15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LCV15MinBucket.setStatus("current")
_Dsx3LCV24HrBucket_Type = Counter32
_Dsx3LCV24HrBucket_Object = MibTableColumn
dsx3LCV24HrBucket = _Dsx3LCV24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 5),
    _Dsx3LCV24HrBucket_Type()
)
dsx3LCV24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LCV24HrBucket.setStatus("current")
_Dsx3LESCurrent_Type = Counter32
_Dsx3LESCurrent_Object = MibTableColumn
dsx3LESCurrent = _Dsx3LESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 6),
    _Dsx3LESCurrent_Type()
)
dsx3LESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LESCurrent.setStatus("current")
_Dsx3LES15MinBucket_Type = Counter32
_Dsx3LES15MinBucket_Object = MibTableColumn
dsx3LES15MinBucket = _Dsx3LES15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 7),
    _Dsx3LES15MinBucket_Type()
)
dsx3LES15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LES15MinBucket.setStatus("current")
_Dsx3LES24HrBucket_Type = Counter32
_Dsx3LES24HrBucket_Object = MibTableColumn
dsx3LES24HrBucket = _Dsx3LES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 8),
    _Dsx3LES24HrBucket_Type()
)
dsx3LES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LES24HrBucket.setStatus("current")
_Dsx3LSESCurrent_Type = Counter32
_Dsx3LSESCurrent_Object = MibTableColumn
dsx3LSESCurrent = _Dsx3LSESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 9),
    _Dsx3LSESCurrent_Type()
)
dsx3LSESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LSESCurrent.setStatus("current")
_Dsx3LSES15MinBucket_Type = Counter32
_Dsx3LSES15MinBucket_Object = MibTableColumn
dsx3LSES15MinBucket = _Dsx3LSES15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 10),
    _Dsx3LSES15MinBucket_Type()
)
dsx3LSES15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LSES15MinBucket.setStatus("current")
_Dsx3LSES24HrBucket_Type = Counter32
_Dsx3LSES24HrBucket_Object = MibTableColumn
dsx3LSES24HrBucket = _Dsx3LSES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 11),
    _Dsx3LSES24HrBucket_Type()
)
dsx3LSES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LSES24HrBucket.setStatus("current")
_Dsx3PCVCurrent_Type = Counter32
_Dsx3PCVCurrent_Object = MibTableColumn
dsx3PCVCurrent = _Dsx3PCVCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 12),
    _Dsx3PCVCurrent_Type()
)
dsx3PCVCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PCVCurrent.setStatus("current")
_Dsx3PCV15MinBucket_Type = Counter32
_Dsx3PCV15MinBucket_Object = MibTableColumn
dsx3PCV15MinBucket = _Dsx3PCV15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 13),
    _Dsx3PCV15MinBucket_Type()
)
dsx3PCV15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PCV15MinBucket.setStatus("current")
_Dsx3PCV24HrBucket_Type = Counter32
_Dsx3PCV24HrBucket_Object = MibTableColumn
dsx3PCV24HrBucket = _Dsx3PCV24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 14),
    _Dsx3PCV24HrBucket_Type()
)
dsx3PCV24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PCV24HrBucket.setStatus("current")
_Dsx3PESCurrent_Type = Counter32
_Dsx3PESCurrent_Object = MibTableColumn
dsx3PESCurrent = _Dsx3PESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 15),
    _Dsx3PESCurrent_Type()
)
dsx3PESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PESCurrent.setStatus("current")
_Dsx3PES15MinBucket_Type = Counter32
_Dsx3PES15MinBucket_Object = MibTableColumn
dsx3PES15MinBucket = _Dsx3PES15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 16),
    _Dsx3PES15MinBucket_Type()
)
dsx3PES15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PES15MinBucket.setStatus("current")
_Dsx3PES24HrBucket_Type = Counter32
_Dsx3PES24HrBucket_Object = MibTableColumn
dsx3PES24HrBucket = _Dsx3PES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 17),
    _Dsx3PES24HrBucket_Type()
)
dsx3PES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PES24HrBucket.setStatus("current")
_Dsx3PSESCurrent_Type = Counter32
_Dsx3PSESCurrent_Object = MibTableColumn
dsx3PSESCurrent = _Dsx3PSESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 18),
    _Dsx3PSESCurrent_Type()
)
dsx3PSESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PSESCurrent.setStatus("current")
_Dsx3PSES15MinBucket_Type = Counter32
_Dsx3PSES15MinBucket_Object = MibTableColumn
dsx3PSES15MinBucket = _Dsx3PSES15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 19),
    _Dsx3PSES15MinBucket_Type()
)
dsx3PSES15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PSES15MinBucket.setStatus("current")
_Dsx3PSES24HrBucket_Type = Counter32
_Dsx3PSES24HrBucket_Object = MibTableColumn
dsx3PSES24HrBucket = _Dsx3PSES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 20),
    _Dsx3PSES24HrBucket_Type()
)
dsx3PSES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PSES24HrBucket.setStatus("current")
_Dsx3SEFSCurrent_Type = Counter32
_Dsx3SEFSCurrent_Object = MibTableColumn
dsx3SEFSCurrent = _Dsx3SEFSCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 21),
    _Dsx3SEFSCurrent_Type()
)
dsx3SEFSCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3SEFSCurrent.setStatus("current")
_Dsx3SEFS15MinBucket_Type = Counter32
_Dsx3SEFS15MinBucket_Object = MibTableColumn
dsx3SEFS15MinBucket = _Dsx3SEFS15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 22),
    _Dsx3SEFS15MinBucket_Type()
)
dsx3SEFS15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3SEFS15MinBucket.setStatus("current")
_Dsx3SEFS24HrBucket_Type = Counter32
_Dsx3SEFS24HrBucket_Object = MibTableColumn
dsx3SEFS24HrBucket = _Dsx3SEFS24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 23),
    _Dsx3SEFS24HrBucket_Type()
)
dsx3SEFS24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3SEFS24HrBucket.setStatus("current")
_Dsx3AISSCurrent_Type = Counter32
_Dsx3AISSCurrent_Object = MibTableColumn
dsx3AISSCurrent = _Dsx3AISSCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 24),
    _Dsx3AISSCurrent_Type()
)
dsx3AISSCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3AISSCurrent.setStatus("current")
_Dsx3AISS15MinBucket_Type = Counter32
_Dsx3AISS15MinBucket_Object = MibTableColumn
dsx3AISS15MinBucket = _Dsx3AISS15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 25),
    _Dsx3AISS15MinBucket_Type()
)
dsx3AISS15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3AISS15MinBucket.setStatus("current")
_Dsx3AISS24HrBucket_Type = Counter32
_Dsx3AISS24HrBucket_Object = MibTableColumn
dsx3AISS24HrBucket = _Dsx3AISS24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 26),
    _Dsx3AISS24HrBucket_Type()
)
dsx3AISS24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3AISS24HrBucket.setStatus("current")
_Dsx3UASCurrent_Type = Counter32
_Dsx3UASCurrent_Object = MibTableColumn
dsx3UASCurrent = _Dsx3UASCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 27),
    _Dsx3UASCurrent_Type()
)
dsx3UASCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3UASCurrent.setStatus("current")
_Dsx3UAS15MinBucket_Type = Counter32
_Dsx3UAS15MinBucket_Object = MibTableColumn
dsx3UAS15MinBucket = _Dsx3UAS15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 28),
    _Dsx3UAS15MinBucket_Type()
)
dsx3UAS15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3UAS15MinBucket.setStatus("current")
_Dsx3UAS24HrBucket_Type = Counter32
_Dsx3UAS24HrBucket_Object = MibTableColumn
dsx3UAS24HrBucket = _Dsx3UAS24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 29),
    _Dsx3UAS24HrBucket_Type()
)
dsx3UAS24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3UAS24HrBucket.setStatus("current")


class _Dsx3PercentLcvEFS_Type(Integer32):
    """Custom type dsx3PercentLcvEFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Dsx3PercentLcvEFS_Type.__name__ = "Integer32"
_Dsx3PercentLcvEFS_Object = MibTableColumn
dsx3PercentLcvEFS = _Dsx3PercentLcvEFS_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 30),
    _Dsx3PercentLcvEFS_Type()
)
dsx3PercentLcvEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PercentLcvEFS.setStatus("current")
_Dsx3E3BIP8CVCurrent_Type = Counter32
_Dsx3E3BIP8CVCurrent_Object = MibTableColumn
dsx3E3BIP8CVCurrent = _Dsx3E3BIP8CVCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 31),
    _Dsx3E3BIP8CVCurrent_Type()
)
dsx3E3BIP8CVCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3E3BIP8CVCurrent.setStatus("current")
_Dsx3E3BIP8CV15MinBucket_Type = Counter32
_Dsx3E3BIP8CV15MinBucket_Object = MibTableColumn
dsx3E3BIP8CV15MinBucket = _Dsx3E3BIP8CV15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 32),
    _Dsx3E3BIP8CV15MinBucket_Type()
)
dsx3E3BIP8CV15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3E3BIP8CV15MinBucket.setStatus("current")
_Dsx3E3BIP8CV24HrBucket_Type = Counter32
_Dsx3E3BIP8CV24HrBucket_Object = MibTableColumn
dsx3E3BIP8CV24HrBucket = _Dsx3E3BIP8CV24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 33),
    _Dsx3E3BIP8CV24HrBucket_Type()
)
dsx3E3BIP8CV24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3E3BIP8CV24HrBucket.setStatus("current")
_Dsx3E3BIP8ESCurrent_Type = Counter32
_Dsx3E3BIP8ESCurrent_Object = MibTableColumn
dsx3E3BIP8ESCurrent = _Dsx3E3BIP8ESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 34),
    _Dsx3E3BIP8ESCurrent_Type()
)
dsx3E3BIP8ESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3E3BIP8ESCurrent.setStatus("current")
_Dsx3E3BIP8ES15MinBucket_Type = Counter32
_Dsx3E3BIP8ES15MinBucket_Object = MibTableColumn
dsx3E3BIP8ES15MinBucket = _Dsx3E3BIP8ES15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 35),
    _Dsx3E3BIP8ES15MinBucket_Type()
)
dsx3E3BIP8ES15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3E3BIP8ES15MinBucket.setStatus("current")
_Dsx3E3BIP8ES24HrBucket_Type = Counter32
_Dsx3E3BIP8ES24HrBucket_Object = MibTableColumn
dsx3E3BIP8ES24HrBucket = _Dsx3E3BIP8ES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 36),
    _Dsx3E3BIP8ES24HrBucket_Type()
)
dsx3E3BIP8ES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3E3BIP8ES24HrBucket.setStatus("current")
_Dsx3E3BIP8SESCurrent_Type = Counter32
_Dsx3E3BIP8SESCurrent_Object = MibTableColumn
dsx3E3BIP8SESCurrent = _Dsx3E3BIP8SESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 37),
    _Dsx3E3BIP8SESCurrent_Type()
)
dsx3E3BIP8SESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3E3BIP8SESCurrent.setStatus("current")
_Dsx3E3BIP8SES15MinBucket_Type = Counter32
_Dsx3E3BIP8SES15MinBucket_Object = MibTableColumn
dsx3E3BIP8SES15MinBucket = _Dsx3E3BIP8SES15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 38),
    _Dsx3E3BIP8SES15MinBucket_Type()
)
dsx3E3BIP8SES15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3E3BIP8SES15MinBucket.setStatus("current")
_Dsx3E3BIP8SES24HrBucket_Type = Counter32
_Dsx3E3BIP8SES24HrBucket_Object = MibTableColumn
dsx3E3BIP8SES24HrBucket = _Dsx3E3BIP8SES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 39),
    _Dsx3E3BIP8SES24HrBucket_Type()
)
dsx3E3BIP8SES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3E3BIP8SES24HrBucket.setStatus("current")


class _Dsx3LineAlarmClrButton_Type(Integer32):
    """Custom type dsx3LineAlarmClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_Dsx3LineAlarmClrButton_Type.__name__ = "Integer32"
_Dsx3LineAlarmClrButton_Object = MibTableColumn
dsx3LineAlarmClrButton = _Dsx3LineAlarmClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 40),
    _Dsx3LineAlarmClrButton_Type()
)
dsx3LineAlarmClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3LineAlarmClrButton.setStatus("current")
_Dsx3CCVCurrent_Type = Counter32
_Dsx3CCVCurrent_Object = MibTableColumn
dsx3CCVCurrent = _Dsx3CCVCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 41),
    _Dsx3CCVCurrent_Type()
)
dsx3CCVCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CCVCurrent.setStatus("current")
_Dsx3CCV15MinBucket_Type = Counter32
_Dsx3CCV15MinBucket_Object = MibTableColumn
dsx3CCV15MinBucket = _Dsx3CCV15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 42),
    _Dsx3CCV15MinBucket_Type()
)
dsx3CCV15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CCV15MinBucket.setStatus("current")
_Dsx3CCV24HrBucket_Type = Counter32
_Dsx3CCV24HrBucket_Object = MibTableColumn
dsx3CCV24HrBucket = _Dsx3CCV24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 43),
    _Dsx3CCV24HrBucket_Type()
)
dsx3CCV24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CCV24HrBucket.setStatus("current")
_Dsx3CESCurrent_Type = Counter32
_Dsx3CESCurrent_Object = MibTableColumn
dsx3CESCurrent = _Dsx3CESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 44),
    _Dsx3CESCurrent_Type()
)
dsx3CESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CESCurrent.setStatus("current")
_Dsx3CES15MinBucket_Type = Counter32
_Dsx3CES15MinBucket_Object = MibTableColumn
dsx3CES15MinBucket = _Dsx3CES15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 45),
    _Dsx3CES15MinBucket_Type()
)
dsx3CES15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CES15MinBucket.setStatus("current")
_Dsx3CES24HrBucket_Type = Counter32
_Dsx3CES24HrBucket_Object = MibTableColumn
dsx3CES24HrBucket = _Dsx3CES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 46),
    _Dsx3CES24HrBucket_Type()
)
dsx3CES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CES24HrBucket.setStatus("current")
_Dsx3CSESCurrent_Type = Counter32
_Dsx3CSESCurrent_Object = MibTableColumn
dsx3CSESCurrent = _Dsx3CSESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 47),
    _Dsx3CSESCurrent_Type()
)
dsx3CSESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CSESCurrent.setStatus("current")
_Dsx3CSES15MinBucket_Type = Counter32
_Dsx3CSES15MinBucket_Object = MibTableColumn
dsx3CSES15MinBucket = _Dsx3CSES15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 48),
    _Dsx3CSES15MinBucket_Type()
)
dsx3CSES15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CSES15MinBucket.setStatus("current")
_Dsx3CSES24HrBucket_Type = Counter32
_Dsx3CSES24HrBucket_Object = MibTableColumn
dsx3CSES24HrBucket = _Dsx3CSES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 3, 1, 1, 49),
    _Dsx3CSES24HrBucket_Type()
)
dsx3CSES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CSES24HrBucket.setStatus("current")
_Dsx3Counter_ObjectIdentity = ObjectIdentity
dsx3Counter = _Dsx3Counter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4)
)
_Dsx3CounterTable_Object = MibTable
dsx3CounterTable = _Dsx3CounterTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dsx3CounterTable.setStatus("current")
_Dsx3CounterEntry_Object = MibTableRow
dsx3CounterEntry = _Dsx3CounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1, 1)
)
dsx3CounterEntry.setIndexNames(
    (0, "CISCO-MGX82XX-DSX3-MIB", "dsx3LineNum"),
)
if mibBuilder.loadTexts:
    dsx3CounterEntry.setStatus("current")
_Dsx3RcvLOSCount_Type = Counter32
_Dsx3RcvLOSCount_Object = MibTableColumn
dsx3RcvLOSCount = _Dsx3RcvLOSCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1, 1, 1),
    _Dsx3RcvLOSCount_Type()
)
dsx3RcvLOSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3RcvLOSCount.setStatus("current")
_Dsx3RcvOOFCount_Type = Counter32
_Dsx3RcvOOFCount_Object = MibTableColumn
dsx3RcvOOFCount = _Dsx3RcvOOFCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1, 1, 2),
    _Dsx3RcvOOFCount_Type()
)
dsx3RcvOOFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3RcvOOFCount.setStatus("current")
_Dsx3RAICount_Type = Counter32
_Dsx3RAICount_Object = MibTableColumn
dsx3RAICount = _Dsx3RAICount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1, 1, 3),
    _Dsx3RAICount_Type()
)
dsx3RAICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3RAICount.setStatus("current")
_Dsx3CCVCount_Type = Counter32
_Dsx3CCVCount_Object = MibTableColumn
dsx3CCVCount = _Dsx3CCVCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1, 1, 4),
    _Dsx3CCVCount_Type()
)
dsx3CCVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3CCVCount.setStatus("current")
_Dsx3FECount_Type = Counter32
_Dsx3FECount_Object = MibTableColumn
dsx3FECount = _Dsx3FECount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1, 1, 5),
    _Dsx3FECount_Type()
)
dsx3FECount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3FECount.setStatus("current")
_Dsx3AtmHECCount_Type = Counter32
_Dsx3AtmHECCount_Object = MibTableColumn
dsx3AtmHECCount = _Dsx3AtmHECCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1, 1, 6),
    _Dsx3AtmHECCount_Type()
)
dsx3AtmHECCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3AtmHECCount.setStatus("current")
_Dsx3AtmHECSecCount_Type = Counter32
_Dsx3AtmHECSecCount_Object = MibTableColumn
dsx3AtmHECSecCount = _Dsx3AtmHECSecCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1, 1, 7),
    _Dsx3AtmHECSecCount_Type()
)
dsx3AtmHECSecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3AtmHECSecCount.setStatus("current")
_Dsx3AtmSEHECSecCount_Type = Counter32
_Dsx3AtmSEHECSecCount_Object = MibTableColumn
dsx3AtmSEHECSecCount = _Dsx3AtmSEHECSecCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1, 1, 8),
    _Dsx3AtmSEHECSecCount_Type()
)
dsx3AtmSEHECSecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3AtmSEHECSecCount.setStatus("current")


class _Dsx3CounterClrButton_Type(Integer32):
    """Custom type dsx3CounterClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_Dsx3CounterClrButton_Type.__name__ = "Integer32"
_Dsx3CounterClrButton_Object = MibTableColumn
dsx3CounterClrButton = _Dsx3CounterClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1, 1, 9),
    _Dsx3CounterClrButton_Type()
)
dsx3CounterClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3CounterClrButton.setStatus("current")
_Dsx3RcvPERRCounter_Type = Counter32
_Dsx3RcvPERRCounter_Object = MibTableColumn
dsx3RcvPERRCounter = _Dsx3RcvPERRCounter_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1, 1, 10),
    _Dsx3RcvPERRCounter_Type()
)
dsx3RcvPERRCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3RcvPERRCounter.setStatus("current")
_Dsx3RcvFEBECounter_Type = Counter32
_Dsx3RcvFEBECounter_Object = MibTableColumn
dsx3RcvFEBECounter = _Dsx3RcvFEBECounter_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1, 1, 11),
    _Dsx3RcvFEBECounter_Type()
)
dsx3RcvFEBECounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3RcvFEBECounter.setStatus("current")
_Dsx3RcvEXZCounter_Type = Counter32
_Dsx3RcvEXZCounter_Object = MibTableColumn
dsx3RcvEXZCounter = _Dsx3RcvEXZCounter_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1, 1, 12),
    _Dsx3RcvEXZCounter_Type()
)
dsx3RcvEXZCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3RcvEXZCounter.setStatus("current")
_Dsx3LCVCount_Type = Counter32
_Dsx3LCVCount_Object = MibTableColumn
dsx3LCVCount = _Dsx3LCVCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1, 4, 1, 1, 13),
    _Dsx3LCVCount_Type()
)
dsx3LCVCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3LCVCount.setStatus("current")
_Dsx3PlcpConfig_ObjectIdentity = ObjectIdentity
dsx3PlcpConfig = _Dsx3PlcpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 1)
)
_Dsx3PlcpConfigTable_Object = MibTable
dsx3PlcpConfigTable = _Dsx3PlcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dsx3PlcpConfigTable.setStatus("current")
_Dsx3PlcpConfigEntry_Object = MibTableRow
dsx3PlcpConfigEntry = _Dsx3PlcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 1, 1, 1)
)
dsx3PlcpConfigEntry.setIndexNames(
    (0, "CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpNum"),
)
if mibBuilder.loadTexts:
    dsx3PlcpConfigEntry.setStatus("current")


class _Dsx3PlcpNum_Type(Integer32):
    """Custom type dsx3PlcpNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx3PlcpNum_Type.__name__ = "Integer32"
_Dsx3PlcpNum_Object = MibTableColumn
dsx3PlcpNum = _Dsx3PlcpNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 1, 1, 1, 1),
    _Dsx3PlcpNum_Type()
)
dsx3PlcpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpNum.setStatus("current")


class _Dsx3PlcpCellFraming_Type(Integer32):
    """Custom type dsx3PlcpCellFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("framingByPlcp", 1),
          ("framingbyAtmHec", 2))
    )


_Dsx3PlcpCellFraming_Type.__name__ = "Integer32"
_Dsx3PlcpCellFraming_Object = MibTableColumn
dsx3PlcpCellFraming = _Dsx3PlcpCellFraming_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 1, 1, 1, 2),
    _Dsx3PlcpCellFraming_Type()
)
dsx3PlcpCellFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpCellFraming.setStatus("current")


class _Dsx3PlcpPayloadScramble_Type(Integer32):
    """Custom type dsx3PlcpPayloadScramble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableScrambling", 2),
          ("enableScrambling", 1))
    )


_Dsx3PlcpPayloadScramble_Type.__name__ = "Integer32"
_Dsx3PlcpPayloadScramble_Object = MibTableColumn
dsx3PlcpPayloadScramble = _Dsx3PlcpPayloadScramble_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 1, 1, 1, 3),
    _Dsx3PlcpPayloadScramble_Type()
)
dsx3PlcpPayloadScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpPayloadScramble.setStatus("current")


class _Dsx3PlcpLoopCommand_Type(Integer32):
    """Custom type dsx3PlcpLoopCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localLineLoop", 3),
          ("noLoop", 1),
          ("remoteLineLoop", 2))
    )


_Dsx3PlcpLoopCommand_Type.__name__ = "Integer32"
_Dsx3PlcpLoopCommand_Object = MibTableColumn
dsx3PlcpLoopCommand = _Dsx3PlcpLoopCommand_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 1, 1, 1, 4),
    _Dsx3PlcpLoopCommand_Type()
)
dsx3PlcpLoopCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpLoopCommand.setStatus("current")


class _Dsx3PlcpNumOfValidEntries_Type(Integer32):
    """Custom type dsx3PlcpNumOfValidEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpNumOfValidEntries_Type.__name__ = "Integer32"
_Dsx3PlcpNumOfValidEntries_Object = MibScalar
dsx3PlcpNumOfValidEntries = _Dsx3PlcpNumOfValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 1, 2),
    _Dsx3PlcpNumOfValidEntries_Type()
)
dsx3PlcpNumOfValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpNumOfValidEntries.setStatus("current")
_Dsx3PlcpAlarmConfig_ObjectIdentity = ObjectIdentity
dsx3PlcpAlarmConfig = _Dsx3PlcpAlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2)
)
_Dsx3PlcpAlarmConfigTable_Object = MibTable
dsx3PlcpAlarmConfigTable = _Dsx3PlcpAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dsx3PlcpAlarmConfigTable.setStatus("current")
_Dsx3PlcpAlarmConfigEntry_Object = MibTableRow
dsx3PlcpAlarmConfigEntry = _Dsx3PlcpAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1)
)
dsx3PlcpAlarmConfigEntry.setIndexNames(
    (0, "CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpNum"),
)
if mibBuilder.loadTexts:
    dsx3PlcpAlarmConfigEntry.setStatus("current")


class _Dsx3PlcpRedSeverity_Type(Integer32):
    """Custom type dsx3PlcpRedSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1))
    )


_Dsx3PlcpRedSeverity_Type.__name__ = "Integer32"
_Dsx3PlcpRedSeverity_Object = MibTableColumn
dsx3PlcpRedSeverity = _Dsx3PlcpRedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 1),
    _Dsx3PlcpRedSeverity_Type()
)
dsx3PlcpRedSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpRedSeverity.setStatus("current")


class _Dsx3PlcpRAISeverity_Type(Integer32):
    """Custom type dsx3PlcpRAISeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1))
    )


_Dsx3PlcpRAISeverity_Type.__name__ = "Integer32"
_Dsx3PlcpRAISeverity_Object = MibTableColumn
dsx3PlcpRAISeverity = _Dsx3PlcpRAISeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 2),
    _Dsx3PlcpRAISeverity_Type()
)
dsx3PlcpRAISeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpRAISeverity.setStatus("current")


class _Dsx3PlcpLssSeverity_Type(Integer32):
    """Custom type dsx3PlcpLssSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1))
    )


_Dsx3PlcpLssSeverity_Type.__name__ = "Integer32"
_Dsx3PlcpLssSeverity_Object = MibTableColumn
dsx3PlcpLssSeverity = _Dsx3PlcpLssSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 3),
    _Dsx3PlcpLssSeverity_Type()
)
dsx3PlcpLssSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpLssSeverity.setStatus("current")


class _Dsx3PlcpLssEnable_Type(Integer32):
    """Custom type dsx3PlcpLssEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lssDisable", 2),
          ("lssEnable", 1))
    )


_Dsx3PlcpLssEnable_Type.__name__ = "Integer32"
_Dsx3PlcpLssEnable_Object = MibTableColumn
dsx3PlcpLssEnable = _Dsx3PlcpLssEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 4),
    _Dsx3PlcpLssEnable_Type()
)
dsx3PlcpLssEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpLssEnable.setStatus("current")


class _Dsx3PlcpLssCodeConnected_Type(Integer32):
    """Custom type dsx3PlcpLssCodeConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpLssCodeConnected_Type.__name__ = "Integer32"
_Dsx3PlcpLssCodeConnected_Object = MibTableColumn
dsx3PlcpLssCodeConnected = _Dsx3PlcpLssCodeConnected_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 5),
    _Dsx3PlcpLssCodeConnected_Type()
)
dsx3PlcpLssCodeConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpLssCodeConnected.setStatus("current")


class _Dsx3PlcpLssCodeRxLinkDn_Type(Integer32):
    """Custom type dsx3PlcpLssCodeRxLinkDn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpLssCodeRxLinkDn_Type.__name__ = "Integer32"
_Dsx3PlcpLssCodeRxLinkDn_Object = MibTableColumn
dsx3PlcpLssCodeRxLinkDn = _Dsx3PlcpLssCodeRxLinkDn_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 6),
    _Dsx3PlcpLssCodeRxLinkDn_Type()
)
dsx3PlcpLssCodeRxLinkDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpLssCodeRxLinkDn.setStatus("current")


class _Dsx3PlcpLssCodeRxLinkUp_Type(Integer32):
    """Custom type dsx3PlcpLssCodeRxLinkUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpLssCodeRxLinkUp_Type.__name__ = "Integer32"
_Dsx3PlcpLssCodeRxLinkUp_Object = MibTableColumn
dsx3PlcpLssCodeRxLinkUp = _Dsx3PlcpLssCodeRxLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 7),
    _Dsx3PlcpLssCodeRxLinkUp_Type()
)
dsx3PlcpLssCodeRxLinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpLssCodeRxLinkUp.setStatus("current")


class _Dsx3PlcpStatisticalAlarmSeverity_Type(Integer32):
    """Custom type dsx3PlcpStatisticalAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1))
    )


_Dsx3PlcpStatisticalAlarmSeverity_Type.__name__ = "Integer32"
_Dsx3PlcpStatisticalAlarmSeverity_Object = MibTableColumn
dsx3PlcpStatisticalAlarmSeverity = _Dsx3PlcpStatisticalAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 8),
    _Dsx3PlcpStatisticalAlarmSeverity_Type()
)
dsx3PlcpStatisticalAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpStatisticalAlarmSeverity.setStatus("current")


class _Dsx3PlcpBip8CV15MinThreshold_Type(Integer32):
    """Custom type dsx3PlcpBip8CV15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpBip8CV15MinThreshold_Type.__name__ = "Integer32"
_Dsx3PlcpBip8CV15MinThreshold_Object = MibTableColumn
dsx3PlcpBip8CV15MinThreshold = _Dsx3PlcpBip8CV15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 9),
    _Dsx3PlcpBip8CV15MinThreshold_Type()
)
dsx3PlcpBip8CV15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpBip8CV15MinThreshold.setStatus("current")


class _Dsx3PlcpBip8CV24HrThreshold_Type(Integer32):
    """Custom type dsx3PlcpBip8CV24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpBip8CV24HrThreshold_Type.__name__ = "Integer32"
_Dsx3PlcpBip8CV24HrThreshold_Object = MibTableColumn
dsx3PlcpBip8CV24HrThreshold = _Dsx3PlcpBip8CV24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 10),
    _Dsx3PlcpBip8CV24HrThreshold_Type()
)
dsx3PlcpBip8CV24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpBip8CV24HrThreshold.setStatus("current")


class _Dsx3PlcpBip8ES15MinThreshold_Type(Integer32):
    """Custom type dsx3PlcpBip8ES15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpBip8ES15MinThreshold_Type.__name__ = "Integer32"
_Dsx3PlcpBip8ES15MinThreshold_Object = MibTableColumn
dsx3PlcpBip8ES15MinThreshold = _Dsx3PlcpBip8ES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 11),
    _Dsx3PlcpBip8ES15MinThreshold_Type()
)
dsx3PlcpBip8ES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpBip8ES15MinThreshold.setStatus("current")


class _Dsx3PlcpBip8ES24HrThreshold_Type(Integer32):
    """Custom type dsx3PlcpBip8ES24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpBip8ES24HrThreshold_Type.__name__ = "Integer32"
_Dsx3PlcpBip8ES24HrThreshold_Object = MibTableColumn
dsx3PlcpBip8ES24HrThreshold = _Dsx3PlcpBip8ES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 12),
    _Dsx3PlcpBip8ES24HrThreshold_Type()
)
dsx3PlcpBip8ES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpBip8ES24HrThreshold.setStatus("current")


class _Dsx3PlcpBip8SES15MinThreshold_Type(Integer32):
    """Custom type dsx3PlcpBip8SES15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpBip8SES15MinThreshold_Type.__name__ = "Integer32"
_Dsx3PlcpBip8SES15MinThreshold_Object = MibTableColumn
dsx3PlcpBip8SES15MinThreshold = _Dsx3PlcpBip8SES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 13),
    _Dsx3PlcpBip8SES15MinThreshold_Type()
)
dsx3PlcpBip8SES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpBip8SES15MinThreshold.setStatus("current")


class _Dsx3PlcpBip8SES24HrThreshold_Type(Integer32):
    """Custom type dsx3PlcpBip8SES24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpBip8SES24HrThreshold_Type.__name__ = "Integer32"
_Dsx3PlcpBip8SES24HrThreshold_Object = MibTableColumn
dsx3PlcpBip8SES24HrThreshold = _Dsx3PlcpBip8SES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 14),
    _Dsx3PlcpBip8SES24HrThreshold_Type()
)
dsx3PlcpBip8SES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpBip8SES24HrThreshold.setStatus("current")


class _Dsx3PlcpSEFS15MinThreshold_Type(Integer32):
    """Custom type dsx3PlcpSEFS15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpSEFS15MinThreshold_Type.__name__ = "Integer32"
_Dsx3PlcpSEFS15MinThreshold_Object = MibTableColumn
dsx3PlcpSEFS15MinThreshold = _Dsx3PlcpSEFS15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 15),
    _Dsx3PlcpSEFS15MinThreshold_Type()
)
dsx3PlcpSEFS15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpSEFS15MinThreshold.setStatus("current")


class _Dsx3PlcpSEFS24HrThreshold_Type(Integer32):
    """Custom type dsx3PlcpSEFS24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpSEFS24HrThreshold_Type.__name__ = "Integer32"
_Dsx3PlcpSEFS24HrThreshold_Object = MibTableColumn
dsx3PlcpSEFS24HrThreshold = _Dsx3PlcpSEFS24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 16),
    _Dsx3PlcpSEFS24HrThreshold_Type()
)
dsx3PlcpSEFS24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpSEFS24HrThreshold.setStatus("current")


class _Dsx3PlcpUAS15MinThreshold_Type(Integer32):
    """Custom type dsx3PlcpUAS15MinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpUAS15MinThreshold_Type.__name__ = "Integer32"
_Dsx3PlcpUAS15MinThreshold_Object = MibTableColumn
dsx3PlcpUAS15MinThreshold = _Dsx3PlcpUAS15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 17),
    _Dsx3PlcpUAS15MinThreshold_Type()
)
dsx3PlcpUAS15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpUAS15MinThreshold.setStatus("current")


class _Dsx3PlcpUAS24HrThreshold_Type(Integer32):
    """Custom type dsx3PlcpUAS24HrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpUAS24HrThreshold_Type.__name__ = "Integer32"
_Dsx3PlcpUAS24HrThreshold_Object = MibTableColumn
dsx3PlcpUAS24HrThreshold = _Dsx3PlcpUAS24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 2, 1, 1, 18),
    _Dsx3PlcpUAS24HrThreshold_Type()
)
dsx3PlcpUAS24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpUAS24HrThreshold.setStatus("current")
_Dsx3PlcpAlarm_ObjectIdentity = ObjectIdentity
dsx3PlcpAlarm = _Dsx3PlcpAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3)
)
_Dsx3PlcpAlarmTable_Object = MibTable
dsx3PlcpAlarmTable = _Dsx3PlcpAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dsx3PlcpAlarmTable.setStatus("current")
_Dsx3PlcpAlarmEntry_Object = MibTableRow
dsx3PlcpAlarmEntry = _Dsx3PlcpAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1)
)
dsx3PlcpAlarmEntry.setIndexNames(
    (0, "CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpNum"),
)
if mibBuilder.loadTexts:
    dsx3PlcpAlarmEntry.setStatus("current")


class _Dsx3PlcpLineAlarmState_Type(Integer32):
    """Custom type dsx3PlcpLineAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_Dsx3PlcpLineAlarmState_Type.__name__ = "Integer32"
_Dsx3PlcpLineAlarmState_Object = MibTableColumn
dsx3PlcpLineAlarmState = _Dsx3PlcpLineAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 1),
    _Dsx3PlcpLineAlarmState_Type()
)
dsx3PlcpLineAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpLineAlarmState.setStatus("current")


class _Dsx3PlcpLineStatisticalAlarmState_Type(Integer32):
    """Custom type dsx3PlcpLineStatisticalAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpLineStatisticalAlarmState_Type.__name__ = "Integer32"
_Dsx3PlcpLineStatisticalAlarmState_Object = MibTableColumn
dsx3PlcpLineStatisticalAlarmState = _Dsx3PlcpLineStatisticalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 2),
    _Dsx3PlcpLineStatisticalAlarmState_Type()
)
dsx3PlcpLineStatisticalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpLineStatisticalAlarmState.setStatus("current")
_Dsx3PlcpBip8CVCurrent_Type = Counter32
_Dsx3PlcpBip8CVCurrent_Object = MibTableColumn
dsx3PlcpBip8CVCurrent = _Dsx3PlcpBip8CVCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 3),
    _Dsx3PlcpBip8CVCurrent_Type()
)
dsx3PlcpBip8CVCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpBip8CVCurrent.setStatus("current")
_Dsx3PlcpBip8CV15MinBucket_Type = Counter32
_Dsx3PlcpBip8CV15MinBucket_Object = MibTableColumn
dsx3PlcpBip8CV15MinBucket = _Dsx3PlcpBip8CV15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 4),
    _Dsx3PlcpBip8CV15MinBucket_Type()
)
dsx3PlcpBip8CV15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpBip8CV15MinBucket.setStatus("current")
_Dsx3PlcpBip8CV24HrBucket_Type = Counter32
_Dsx3PlcpBip8CV24HrBucket_Object = MibTableColumn
dsx3PlcpBip8CV24HrBucket = _Dsx3PlcpBip8CV24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 5),
    _Dsx3PlcpBip8CV24HrBucket_Type()
)
dsx3PlcpBip8CV24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpBip8CV24HrBucket.setStatus("current")
_Dsx3PlcpBip8ESCurrent_Type = Counter32
_Dsx3PlcpBip8ESCurrent_Object = MibTableColumn
dsx3PlcpBip8ESCurrent = _Dsx3PlcpBip8ESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 6),
    _Dsx3PlcpBip8ESCurrent_Type()
)
dsx3PlcpBip8ESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpBip8ESCurrent.setStatus("current")
_Dsx3PlcpBip8ES15MinBucket_Type = Counter32
_Dsx3PlcpBip8ES15MinBucket_Object = MibTableColumn
dsx3PlcpBip8ES15MinBucket = _Dsx3PlcpBip8ES15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 7),
    _Dsx3PlcpBip8ES15MinBucket_Type()
)
dsx3PlcpBip8ES15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpBip8ES15MinBucket.setStatus("current")
_Dsx3PlcpBip8ES24HrBucket_Type = Counter32
_Dsx3PlcpBip8ES24HrBucket_Object = MibTableColumn
dsx3PlcpBip8ES24HrBucket = _Dsx3PlcpBip8ES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 8),
    _Dsx3PlcpBip8ES24HrBucket_Type()
)
dsx3PlcpBip8ES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpBip8ES24HrBucket.setStatus("current")
_Dsx3PlcpBip8SESCurrent_Type = Counter32
_Dsx3PlcpBip8SESCurrent_Object = MibTableColumn
dsx3PlcpBip8SESCurrent = _Dsx3PlcpBip8SESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 9),
    _Dsx3PlcpBip8SESCurrent_Type()
)
dsx3PlcpBip8SESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpBip8SESCurrent.setStatus("current")
_Dsx3PlcpBip8SES15MinBucket_Type = Counter32
_Dsx3PlcpBip8SES15MinBucket_Object = MibTableColumn
dsx3PlcpBip8SES15MinBucket = _Dsx3PlcpBip8SES15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 10),
    _Dsx3PlcpBip8SES15MinBucket_Type()
)
dsx3PlcpBip8SES15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpBip8SES15MinBucket.setStatus("current")
_Dsx3PlcpBip8SES24HrBucket_Type = Counter32
_Dsx3PlcpBip8SES24HrBucket_Object = MibTableColumn
dsx3PlcpBip8SES24HrBucket = _Dsx3PlcpBip8SES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 11),
    _Dsx3PlcpBip8SES24HrBucket_Type()
)
dsx3PlcpBip8SES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpBip8SES24HrBucket.setStatus("current")
_Dsx3PlcpSEFSCurrent_Type = Counter32
_Dsx3PlcpSEFSCurrent_Object = MibTableColumn
dsx3PlcpSEFSCurrent = _Dsx3PlcpSEFSCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 12),
    _Dsx3PlcpSEFSCurrent_Type()
)
dsx3PlcpSEFSCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpSEFSCurrent.setStatus("current")
_Dsx3PlcpSEFS15MinBucket_Type = Counter32
_Dsx3PlcpSEFS15MinBucket_Object = MibTableColumn
dsx3PlcpSEFS15MinBucket = _Dsx3PlcpSEFS15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 13),
    _Dsx3PlcpSEFS15MinBucket_Type()
)
dsx3PlcpSEFS15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpSEFS15MinBucket.setStatus("current")
_Dsx3PlcpSEFS24HrBucket_Type = Counter32
_Dsx3PlcpSEFS24HrBucket_Object = MibTableColumn
dsx3PlcpSEFS24HrBucket = _Dsx3PlcpSEFS24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 14),
    _Dsx3PlcpSEFS24HrBucket_Type()
)
dsx3PlcpSEFS24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpSEFS24HrBucket.setStatus("current")
_Dsx3PlcpUASCurrent_Type = Counter32
_Dsx3PlcpUASCurrent_Object = MibTableColumn
dsx3PlcpUASCurrent = _Dsx3PlcpUASCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 15),
    _Dsx3PlcpUASCurrent_Type()
)
dsx3PlcpUASCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpUASCurrent.setStatus("current")
_Dsx3PlcpUAS15MinBucket_Type = Counter32
_Dsx3PlcpUAS15MinBucket_Object = MibTableColumn
dsx3PlcpUAS15MinBucket = _Dsx3PlcpUAS15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 16),
    _Dsx3PlcpUAS15MinBucket_Type()
)
dsx3PlcpUAS15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpUAS15MinBucket.setStatus("current")
_Dsx3PlcpUAS24HrBucket_Type = Counter32
_Dsx3PlcpUAS24HrBucket_Object = MibTableColumn
dsx3PlcpUAS24HrBucket = _Dsx3PlcpUAS24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 17),
    _Dsx3PlcpUAS24HrBucket_Type()
)
dsx3PlcpUAS24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpUAS24HrBucket.setStatus("current")


class _Dsx3PlcpAlarmClrButton_Type(Integer32):
    """Custom type dsx3PlcpAlarmClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsx3PlcpAlarmClear", 2),
          ("dsx3PlcpAlarmNoAction", 1))
    )


_Dsx3PlcpAlarmClrButton_Type.__name__ = "Integer32"
_Dsx3PlcpAlarmClrButton_Object = MibTableColumn
dsx3PlcpAlarmClrButton = _Dsx3PlcpAlarmClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 3, 1, 1, 18),
    _Dsx3PlcpAlarmClrButton_Type()
)
dsx3PlcpAlarmClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpAlarmClrButton.setStatus("current")
_Dsx3PlcpCounter_ObjectIdentity = ObjectIdentity
dsx3PlcpCounter = _Dsx3PlcpCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4)
)
_Dsx3PlcpCounterTable_Object = MibTable
dsx3PlcpCounterTable = _Dsx3PlcpCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    dsx3PlcpCounterTable.setStatus("current")
_Dsx3PlcpCounterEntry_Object = MibTableRow
dsx3PlcpCounterEntry = _Dsx3PlcpCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1, 1)
)
dsx3PlcpCounterEntry.setIndexNames(
    (0, "CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpNum"),
)
if mibBuilder.loadTexts:
    dsx3PlcpCounterEntry.setStatus("current")
_Dsx3PlcpRcvBip8Count_Type = Counter32
_Dsx3PlcpRcvBip8Count_Object = MibTableColumn
dsx3PlcpRcvBip8Count = _Dsx3PlcpRcvBip8Count_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1, 1, 1),
    _Dsx3PlcpRcvBip8Count_Type()
)
dsx3PlcpRcvBip8Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpRcvBip8Count.setStatus("current")
_Dsx3PlcpRcvOOFCount_Type = Counter32
_Dsx3PlcpRcvOOFCount_Object = MibTableColumn
dsx3PlcpRcvOOFCount = _Dsx3PlcpRcvOOFCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1, 1, 2),
    _Dsx3PlcpRcvOOFCount_Type()
)
dsx3PlcpRcvOOFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpRcvOOFCount.setStatus("current")
_Dsx3PlcpRcvRAICount_Type = Counter32
_Dsx3PlcpRcvRAICount_Object = MibTableColumn
dsx3PlcpRcvRAICount = _Dsx3PlcpRcvRAICount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1, 1, 3),
    _Dsx3PlcpRcvRAICount_Type()
)
dsx3PlcpRcvRAICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpRcvRAICount.setStatus("current")
_Dsx3PlcpFECount_Type = Counter32
_Dsx3PlcpFECount_Object = MibTableColumn
dsx3PlcpFECount = _Dsx3PlcpFECount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1, 1, 4),
    _Dsx3PlcpFECount_Type()
)
dsx3PlcpFECount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpFECount.setStatus("current")
_Dsx3PlcpFESecCount_Type = Counter32
_Dsx3PlcpFESecCount_Object = MibTableColumn
dsx3PlcpFESecCount = _Dsx3PlcpFESecCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1, 1, 5),
    _Dsx3PlcpFESecCount_Type()
)
dsx3PlcpFESecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpFESecCount.setStatus("current")
_Dsx3PlcpSEFESecCount_Type = Counter32
_Dsx3PlcpSEFESecCount_Object = MibTableColumn
dsx3PlcpSEFESecCount = _Dsx3PlcpSEFESecCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1, 1, 6),
    _Dsx3PlcpSEFESecCount_Type()
)
dsx3PlcpSEFESecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpSEFESecCount.setStatus("current")
_Dsx3PlcpFEBECount_Type = Counter32
_Dsx3PlcpFEBECount_Object = MibTableColumn
dsx3PlcpFEBECount = _Dsx3PlcpFEBECount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1, 1, 7),
    _Dsx3PlcpFEBECount_Type()
)
dsx3PlcpFEBECount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpFEBECount.setStatus("current")
_Dsx3PlcpFEBESecCount_Type = Counter32
_Dsx3PlcpFEBESecCount_Object = MibTableColumn
dsx3PlcpFEBESecCount = _Dsx3PlcpFEBESecCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1, 1, 8),
    _Dsx3PlcpFEBESecCount_Type()
)
dsx3PlcpFEBESecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpFEBESecCount.setStatus("current")
_Dsx3PlcpSEFEBESecCount_Type = Counter32
_Dsx3PlcpSEFEBESecCount_Object = MibTableColumn
dsx3PlcpSEFEBESecCount = _Dsx3PlcpSEFEBESecCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1, 1, 9),
    _Dsx3PlcpSEFEBESecCount_Type()
)
dsx3PlcpSEFEBESecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpSEFEBESecCount.setStatus("current")
_Dsx3PlcpHECCount_Type = Counter32
_Dsx3PlcpHECCount_Object = MibTableColumn
dsx3PlcpHECCount = _Dsx3PlcpHECCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1, 1, 10),
    _Dsx3PlcpHECCount_Type()
)
dsx3PlcpHECCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpHECCount.setStatus("current")
_Dsx3PlcpHECSecCount_Type = Counter32
_Dsx3PlcpHECSecCount_Object = MibTableColumn
dsx3PlcpHECSecCount = _Dsx3PlcpHECSecCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1, 1, 11),
    _Dsx3PlcpHECSecCount_Type()
)
dsx3PlcpHECSecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpHECSecCount.setStatus("current")
_Dsx3PlcpSEHECSecCount_Type = Counter32
_Dsx3PlcpSEHECSecCount_Object = MibTableColumn
dsx3PlcpSEHECSecCount = _Dsx3PlcpSEHECSecCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1, 1, 12),
    _Dsx3PlcpSEHECSecCount_Type()
)
dsx3PlcpSEHECSecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpSEHECSecCount.setStatus("current")


class _Dsx3PlcpCounterClrButton_Type(Integer32):
    """Custom type dsx3PlcpCounterClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsx3PlcpCounterClear", 2),
          ("dsx3PlcpCounterNoAction", 1))
    )


_Dsx3PlcpCounterClrButton_Type.__name__ = "Integer32"
_Dsx3PlcpCounterClrButton_Object = MibTableColumn
dsx3PlcpCounterClrButton = _Dsx3PlcpCounterClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 1, 1, 13),
    _Dsx3PlcpCounterClrButton_Type()
)
dsx3PlcpCounterClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PlcpCounterClrButton.setStatus("current")


class _Dsx3PlcpCounterValidEntries_Type(Integer32):
    """Custom type dsx3PlcpCounterValidEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx3PlcpCounterValidEntries_Type.__name__ = "Integer32"
_Dsx3PlcpCounterValidEntries_Object = MibScalar
dsx3PlcpCounterValidEntries = _Dsx3PlcpCounterValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2, 4, 2),
    _Dsx3PlcpCounterValidEntries_Type()
)
dsx3PlcpCounterValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PlcpCounterValidEntries.setStatus("current")
_CmDsx3MIBConformance_ObjectIdentity = ObjectIdentity
cmDsx3MIBConformance = _CmDsx3MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2)
)
_CmDsx3MIBGroups_ObjectIdentity = ObjectIdentity
cmDsx3MIBGroups = _CmDsx3MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1)
)
_CmDsx3MIBCompliances_ObjectIdentity = ObjectIdentity
cmDsx3MIBCompliances = _CmDsx3MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 2)
)

# Managed Objects groups

cmDsx3GeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 1)
)
cmDsx3GeneralGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3LineNumOfValidEntries"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpNumOfValidEntries"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpCounterValidEntries"))
)
if mibBuilder.loadTexts:
    cmDsx3GeneralGroup.setStatus("current")

cmDsx3ConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 2)
)
cmDsx3ConfGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3LineNum"),
        ("CISCO-MGX82XX-DSX3-MIB", "cwDsx3LineType"),
        ("CISCO-MGX82XX-DSX3-MIB", "cwDsx3LineCoding"),
        ("CISCO-MGX82XX-DSX3-MIB", "cwDsx3LineLength"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LineOOFCriteria"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LineAIScBitsCheck"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LineLoopbackCommand"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LineXmtFEACCode"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LineEnable"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3FarEndLoopbkLineNum"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LineXmtClockSrc"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3FarEndLoopbkLineStatus"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LineEqualizer"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3NearEndLoopbkLineStatus"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3SubRateEnable"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3DsuSelect"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LineRate"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LineScrambleEnable"))
)
if mibBuilder.loadTexts:
    cmDsx3ConfGroup.setStatus("current")

cmDsx3E3ConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 3)
)
cmDsx3E3ConfGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3LineRcvFEACValidation"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3TrailTraceOption"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3TxTrailTrace"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3RxTrailTrace"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3TxTimingMarker"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3RxTimingMarker"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3TxPayloadType"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3RxPayloadType"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3TxTumf"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3RxTumf"))
)
if mibBuilder.loadTexts:
    cmDsx3E3ConfGroup.setStatus("current")

cmDsx3BertConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 4)
)
cmDsx3BertConfigGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3LineBERTEnable"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LineBERTPattern"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LineBERTResult"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3BERTResultClrButton"))
)
if mibBuilder.loadTexts:
    cmDsx3BertConfigGroup.setStatus("current")

cmDsx3StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 5)
)
cmDsx3StatsGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3RcvLOSCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3RcvOOFCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3RAICount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CCVCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3FECount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3AtmHECCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3AtmHECSecCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3AtmSEHECSecCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CounterClrButton"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3RcvPERRCounter"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3RcvFEBECounter"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3RcvEXZCounter"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LCVCount"))
)
if mibBuilder.loadTexts:
    cmDsx3StatsGroup.setStatus("current")

cmDsx3E3AlarmConfGenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 6)
)
cmDsx3E3AlarmConfGenGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3RedSeverity"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3RAISeverity"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3NEAlarmUpCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3NEAlarmDownCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3NEAlarmThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3FEAlarmUpCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3FEAlarmDownCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3FEAlarmThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3StatisticalAlarmSeverity"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LCV15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LCV24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LES15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LES24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LSES15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LSES24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3SEFS15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3SEFS24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3UAS15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3UAS24HrThreshold"))
)
if mibBuilder.loadTexts:
    cmDsx3E3AlarmConfGenGroup.setStatus("current")

cmDsx3AlarmConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 7)
)
cmDsx3AlarmConfGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3PCV15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PCV24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PES15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PES24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PSES15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PSES24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3AISS15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3AISS24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CCV15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CCV24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CES15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CES24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CSES15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CSES24HrThreshold"))
)
if mibBuilder.loadTexts:
    cmDsx3AlarmConfGroup.setStatus("current")

cmDsx3E3AlarmConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 8)
)
cmDsx3E3AlarmConfGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8CV15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8CV24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8ES15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8ES24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8SES15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8SES24HrThreshold"))
)
if mibBuilder.loadTexts:
    cmDsx3E3AlarmConfGroup.setStatus("current")

cmDsx3AlarmStatsGenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 9)
)
cmDsx3AlarmStatsGenGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3LineAlarmState"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LineStatisticalAlarmState"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LCVCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LCV15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LCV24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LESCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LES15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LES24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LSESCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LSES15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LSES24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3SEFSCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3SEFS15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3SEFS24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3UASCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3UAS15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3UAS24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PercentLcvEFS"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3LineAlarmClrButton"))
)
if mibBuilder.loadTexts:
    cmDsx3AlarmStatsGenGroup.setStatus("current")

cmDsx3AlarmStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 10)
)
cmDsx3AlarmStatsGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3PCVCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PCV15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PCV24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PESCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PES15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PES24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PSESCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PSES15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PSES24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3AISSCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3AISS15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3AISS24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CCVCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CCV15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CCV24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CESCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CES15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CES24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CSESCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CSES15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3CSES24HrBucket"))
)
if mibBuilder.loadTexts:
    cmDsx3AlarmStatsGroup.setStatus("current")

cmDsx3E3AlarmStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 11)
)
cmDsx3E3AlarmStatsGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8CVCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8CV15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8CV24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8ESCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8ES15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8ES24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8SESCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8SES15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3E3BIP8SES24HrBucket"))
)
if mibBuilder.loadTexts:
    cmDsx3E3AlarmStatsGroup.setStatus("current")

cmDsx3PlcpConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 12)
)
cmDsx3PlcpConfGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpNum"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpCellFraming"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpPayloadScramble"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpLoopCommand"))
)
if mibBuilder.loadTexts:
    cmDsx3PlcpConfGroup.setStatus("current")

cmDsx3PlcpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 13)
)
cmDsx3PlcpStatsGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpRcvBip8Count"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpRcvOOFCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpRcvRAICount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpFECount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpFESecCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpSEFESecCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpFEBECount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpFEBESecCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpSEFEBESecCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpHECCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpHECSecCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpSEHECSecCount"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpCounterClrButton"))
)
if mibBuilder.loadTexts:
    cmDsx3PlcpStatsGroup.setStatus("current")

cmDsx3PlcpAlarmConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 14)
)
cmDsx3PlcpAlarmConfGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpRedSeverity"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpRAISeverity"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpLssSeverity"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpLssEnable"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpLssCodeConnected"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpLssCodeRxLinkDn"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpLssCodeRxLinkUp"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpStatisticalAlarmSeverity"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8CV15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8CV24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8ES15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8ES24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8SES15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8SES24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpSEFS15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpSEFS24HrThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpUAS15MinThreshold"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpUAS24HrThreshold"))
)
if mibBuilder.loadTexts:
    cmDsx3PlcpAlarmConfGroup.setStatus("current")

cmDsx3PlcpAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 1, 15)
)
cmDsx3PlcpAlarmGroup.setObjects(
      *(("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpLineAlarmState"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpLineStatisticalAlarmState"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8CVCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8CV15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8CV24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8ESCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8ES15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8ES24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8SESCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8SES15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpBip8SES24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpSEFSCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpSEFS15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpSEFS24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpUASCurrent"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpUAS15MinBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpUAS24HrBucket"),
        ("CISCO-MGX82XX-DSX3-MIB", "dsx3PlcpAlarmClrButton"))
)
if mibBuilder.loadTexts:
    cmDsx3PlcpAlarmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmDsx3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 59, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cmDsx3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGX82XX-DSX3-MIB",
    **{"dsx3Config": dsx3Config,
       "cwDsx3ConfigTable": cwDsx3ConfigTable,
       "cwDsx3ConfigEntry": cwDsx3ConfigEntry,
       "dsx3LineNum": dsx3LineNum,
       "cwDsx3LineType": cwDsx3LineType,
       "cwDsx3LineCoding": cwDsx3LineCoding,
       "cwDsx3LineLength": cwDsx3LineLength,
       "dsx3LineOOFCriteria": dsx3LineOOFCriteria,
       "dsx3LineAIScBitsCheck": dsx3LineAIScBitsCheck,
       "dsx3LineLoopbackCommand": dsx3LineLoopbackCommand,
       "dsx3LineRcvFEACValidation": dsx3LineRcvFEACValidation,
       "dsx3LineXmtFEACCode": dsx3LineXmtFEACCode,
       "dsx3LineBERTEnable": dsx3LineBERTEnable,
       "dsx3LineBERTPattern": dsx3LineBERTPattern,
       "dsx3LineBERTResult": dsx3LineBERTResult,
       "dsx3BERTResultClrButton": dsx3BERTResultClrButton,
       "dsx3TrailTraceOption": dsx3TrailTraceOption,
       "dsx3TxTrailTrace": dsx3TxTrailTrace,
       "dsx3RxTrailTrace": dsx3RxTrailTrace,
       "dsx3TxTimingMarker": dsx3TxTimingMarker,
       "dsx3RxTimingMarker": dsx3RxTimingMarker,
       "dsx3TxPayloadType": dsx3TxPayloadType,
       "dsx3RxPayloadType": dsx3RxPayloadType,
       "dsx3TxTumf": dsx3TxTumf,
       "dsx3RxTumf": dsx3RxTumf,
       "dsx3LineEnable": dsx3LineEnable,
       "dsx3FarEndLoopbkLineNum": dsx3FarEndLoopbkLineNum,
       "dsx3LineXmtClockSrc": dsx3LineXmtClockSrc,
       "dsx3FarEndLoopbkLineStatus": dsx3FarEndLoopbkLineStatus,
       "dsx3LineEqualizer": dsx3LineEqualizer,
       "dsx3NearEndLoopbkLineStatus": dsx3NearEndLoopbkLineStatus,
       "dsx3SubRateEnable": dsx3SubRateEnable,
       "dsx3DsuSelect": dsx3DsuSelect,
       "dsx3LineRate": dsx3LineRate,
       "dsx3LineScrambleEnable": dsx3LineScrambleEnable,
       "dsx3LineNumOfValidEntries": dsx3LineNumOfValidEntries,
       "dsx3AlarmConfig": dsx3AlarmConfig,
       "dsx3AlarmConfigTable": dsx3AlarmConfigTable,
       "dsx3AlarmConfigEntry": dsx3AlarmConfigEntry,
       "dsx3RedSeverity": dsx3RedSeverity,
       "dsx3RAISeverity": dsx3RAISeverity,
       "dsx3NEAlarmUpCount": dsx3NEAlarmUpCount,
       "dsx3NEAlarmDownCount": dsx3NEAlarmDownCount,
       "dsx3NEAlarmThreshold": dsx3NEAlarmThreshold,
       "dsx3FEAlarmUpCount": dsx3FEAlarmUpCount,
       "dsx3FEAlarmDownCount": dsx3FEAlarmDownCount,
       "dsx3FEAlarmThreshold": dsx3FEAlarmThreshold,
       "dsx3StatisticalAlarmSeverity": dsx3StatisticalAlarmSeverity,
       "dsx3LCV15MinThreshold": dsx3LCV15MinThreshold,
       "dsx3LCV24HrThreshold": dsx3LCV24HrThreshold,
       "dsx3LES15MinThreshold": dsx3LES15MinThreshold,
       "dsx3LES24HrThreshold": dsx3LES24HrThreshold,
       "dsx3LSES15MinThreshold": dsx3LSES15MinThreshold,
       "dsx3LSES24HrThreshold": dsx3LSES24HrThreshold,
       "dsx3PCV15MinThreshold": dsx3PCV15MinThreshold,
       "dsx3PCV24HrThreshold": dsx3PCV24HrThreshold,
       "dsx3PES15MinThreshold": dsx3PES15MinThreshold,
       "dsx3PES24HrThreshold": dsx3PES24HrThreshold,
       "dsx3PSES15MinThreshold": dsx3PSES15MinThreshold,
       "dsx3PSES24HrThreshold": dsx3PSES24HrThreshold,
       "dsx3SEFS15MinThreshold": dsx3SEFS15MinThreshold,
       "dsx3SEFS24HrThreshold": dsx3SEFS24HrThreshold,
       "dsx3AISS15MinThreshold": dsx3AISS15MinThreshold,
       "dsx3AISS24HrThreshold": dsx3AISS24HrThreshold,
       "dsx3UAS15MinThreshold": dsx3UAS15MinThreshold,
       "dsx3UAS24HrThreshold": dsx3UAS24HrThreshold,
       "dsx3E3BIP8CV15MinThreshold": dsx3E3BIP8CV15MinThreshold,
       "dsx3E3BIP8CV24HrThreshold": dsx3E3BIP8CV24HrThreshold,
       "dsx3E3BIP8ES15MinThreshold": dsx3E3BIP8ES15MinThreshold,
       "dsx3E3BIP8ES24HrThreshold": dsx3E3BIP8ES24HrThreshold,
       "dsx3E3BIP8SES15MinThreshold": dsx3E3BIP8SES15MinThreshold,
       "dsx3E3BIP8SES24HrThreshold": dsx3E3BIP8SES24HrThreshold,
       "dsx3CCV15MinThreshold": dsx3CCV15MinThreshold,
       "dsx3CCV24HrThreshold": dsx3CCV24HrThreshold,
       "dsx3CES15MinThreshold": dsx3CES15MinThreshold,
       "dsx3CES24HrThreshold": dsx3CES24HrThreshold,
       "dsx3CSES15MinThreshold": dsx3CSES15MinThreshold,
       "dsx3CSES24HrThreshold": dsx3CSES24HrThreshold,
       "dsx3Alarm": dsx3Alarm,
       "dsx3AlarmTable": dsx3AlarmTable,
       "dsx3AlarmEntry": dsx3AlarmEntry,
       "dsx3LineAlarmState": dsx3LineAlarmState,
       "dsx3LineStatisticalAlarmState": dsx3LineStatisticalAlarmState,
       "dsx3LCVCurrent": dsx3LCVCurrent,
       "dsx3LCV15MinBucket": dsx3LCV15MinBucket,
       "dsx3LCV24HrBucket": dsx3LCV24HrBucket,
       "dsx3LESCurrent": dsx3LESCurrent,
       "dsx3LES15MinBucket": dsx3LES15MinBucket,
       "dsx3LES24HrBucket": dsx3LES24HrBucket,
       "dsx3LSESCurrent": dsx3LSESCurrent,
       "dsx3LSES15MinBucket": dsx3LSES15MinBucket,
       "dsx3LSES24HrBucket": dsx3LSES24HrBucket,
       "dsx3PCVCurrent": dsx3PCVCurrent,
       "dsx3PCV15MinBucket": dsx3PCV15MinBucket,
       "dsx3PCV24HrBucket": dsx3PCV24HrBucket,
       "dsx3PESCurrent": dsx3PESCurrent,
       "dsx3PES15MinBucket": dsx3PES15MinBucket,
       "dsx3PES24HrBucket": dsx3PES24HrBucket,
       "dsx3PSESCurrent": dsx3PSESCurrent,
       "dsx3PSES15MinBucket": dsx3PSES15MinBucket,
       "dsx3PSES24HrBucket": dsx3PSES24HrBucket,
       "dsx3SEFSCurrent": dsx3SEFSCurrent,
       "dsx3SEFS15MinBucket": dsx3SEFS15MinBucket,
       "dsx3SEFS24HrBucket": dsx3SEFS24HrBucket,
       "dsx3AISSCurrent": dsx3AISSCurrent,
       "dsx3AISS15MinBucket": dsx3AISS15MinBucket,
       "dsx3AISS24HrBucket": dsx3AISS24HrBucket,
       "dsx3UASCurrent": dsx3UASCurrent,
       "dsx3UAS15MinBucket": dsx3UAS15MinBucket,
       "dsx3UAS24HrBucket": dsx3UAS24HrBucket,
       "dsx3PercentLcvEFS": dsx3PercentLcvEFS,
       "dsx3E3BIP8CVCurrent": dsx3E3BIP8CVCurrent,
       "dsx3E3BIP8CV15MinBucket": dsx3E3BIP8CV15MinBucket,
       "dsx3E3BIP8CV24HrBucket": dsx3E3BIP8CV24HrBucket,
       "dsx3E3BIP8ESCurrent": dsx3E3BIP8ESCurrent,
       "dsx3E3BIP8ES15MinBucket": dsx3E3BIP8ES15MinBucket,
       "dsx3E3BIP8ES24HrBucket": dsx3E3BIP8ES24HrBucket,
       "dsx3E3BIP8SESCurrent": dsx3E3BIP8SESCurrent,
       "dsx3E3BIP8SES15MinBucket": dsx3E3BIP8SES15MinBucket,
       "dsx3E3BIP8SES24HrBucket": dsx3E3BIP8SES24HrBucket,
       "dsx3LineAlarmClrButton": dsx3LineAlarmClrButton,
       "dsx3CCVCurrent": dsx3CCVCurrent,
       "dsx3CCV15MinBucket": dsx3CCV15MinBucket,
       "dsx3CCV24HrBucket": dsx3CCV24HrBucket,
       "dsx3CESCurrent": dsx3CESCurrent,
       "dsx3CES15MinBucket": dsx3CES15MinBucket,
       "dsx3CES24HrBucket": dsx3CES24HrBucket,
       "dsx3CSESCurrent": dsx3CSESCurrent,
       "dsx3CSES15MinBucket": dsx3CSES15MinBucket,
       "dsx3CSES24HrBucket": dsx3CSES24HrBucket,
       "dsx3Counter": dsx3Counter,
       "dsx3CounterTable": dsx3CounterTable,
       "dsx3CounterEntry": dsx3CounterEntry,
       "dsx3RcvLOSCount": dsx3RcvLOSCount,
       "dsx3RcvOOFCount": dsx3RcvOOFCount,
       "dsx3RAICount": dsx3RAICount,
       "dsx3CCVCount": dsx3CCVCount,
       "dsx3FECount": dsx3FECount,
       "dsx3AtmHECCount": dsx3AtmHECCount,
       "dsx3AtmHECSecCount": dsx3AtmHECSecCount,
       "dsx3AtmSEHECSecCount": dsx3AtmSEHECSecCount,
       "dsx3CounterClrButton": dsx3CounterClrButton,
       "dsx3RcvPERRCounter": dsx3RcvPERRCounter,
       "dsx3RcvFEBECounter": dsx3RcvFEBECounter,
       "dsx3RcvEXZCounter": dsx3RcvEXZCounter,
       "dsx3LCVCount": dsx3LCVCount,
       "dsx3PlcpConfig": dsx3PlcpConfig,
       "dsx3PlcpConfigTable": dsx3PlcpConfigTable,
       "dsx3PlcpConfigEntry": dsx3PlcpConfigEntry,
       "dsx3PlcpNum": dsx3PlcpNum,
       "dsx3PlcpCellFraming": dsx3PlcpCellFraming,
       "dsx3PlcpPayloadScramble": dsx3PlcpPayloadScramble,
       "dsx3PlcpLoopCommand": dsx3PlcpLoopCommand,
       "dsx3PlcpNumOfValidEntries": dsx3PlcpNumOfValidEntries,
       "dsx3PlcpAlarmConfig": dsx3PlcpAlarmConfig,
       "dsx3PlcpAlarmConfigTable": dsx3PlcpAlarmConfigTable,
       "dsx3PlcpAlarmConfigEntry": dsx3PlcpAlarmConfigEntry,
       "dsx3PlcpRedSeverity": dsx3PlcpRedSeverity,
       "dsx3PlcpRAISeverity": dsx3PlcpRAISeverity,
       "dsx3PlcpLssSeverity": dsx3PlcpLssSeverity,
       "dsx3PlcpLssEnable": dsx3PlcpLssEnable,
       "dsx3PlcpLssCodeConnected": dsx3PlcpLssCodeConnected,
       "dsx3PlcpLssCodeRxLinkDn": dsx3PlcpLssCodeRxLinkDn,
       "dsx3PlcpLssCodeRxLinkUp": dsx3PlcpLssCodeRxLinkUp,
       "dsx3PlcpStatisticalAlarmSeverity": dsx3PlcpStatisticalAlarmSeverity,
       "dsx3PlcpBip8CV15MinThreshold": dsx3PlcpBip8CV15MinThreshold,
       "dsx3PlcpBip8CV24HrThreshold": dsx3PlcpBip8CV24HrThreshold,
       "dsx3PlcpBip8ES15MinThreshold": dsx3PlcpBip8ES15MinThreshold,
       "dsx3PlcpBip8ES24HrThreshold": dsx3PlcpBip8ES24HrThreshold,
       "dsx3PlcpBip8SES15MinThreshold": dsx3PlcpBip8SES15MinThreshold,
       "dsx3PlcpBip8SES24HrThreshold": dsx3PlcpBip8SES24HrThreshold,
       "dsx3PlcpSEFS15MinThreshold": dsx3PlcpSEFS15MinThreshold,
       "dsx3PlcpSEFS24HrThreshold": dsx3PlcpSEFS24HrThreshold,
       "dsx3PlcpUAS15MinThreshold": dsx3PlcpUAS15MinThreshold,
       "dsx3PlcpUAS24HrThreshold": dsx3PlcpUAS24HrThreshold,
       "dsx3PlcpAlarm": dsx3PlcpAlarm,
       "dsx3PlcpAlarmTable": dsx3PlcpAlarmTable,
       "dsx3PlcpAlarmEntry": dsx3PlcpAlarmEntry,
       "dsx3PlcpLineAlarmState": dsx3PlcpLineAlarmState,
       "dsx3PlcpLineStatisticalAlarmState": dsx3PlcpLineStatisticalAlarmState,
       "dsx3PlcpBip8CVCurrent": dsx3PlcpBip8CVCurrent,
       "dsx3PlcpBip8CV15MinBucket": dsx3PlcpBip8CV15MinBucket,
       "dsx3PlcpBip8CV24HrBucket": dsx3PlcpBip8CV24HrBucket,
       "dsx3PlcpBip8ESCurrent": dsx3PlcpBip8ESCurrent,
       "dsx3PlcpBip8ES15MinBucket": dsx3PlcpBip8ES15MinBucket,
       "dsx3PlcpBip8ES24HrBucket": dsx3PlcpBip8ES24HrBucket,
       "dsx3PlcpBip8SESCurrent": dsx3PlcpBip8SESCurrent,
       "dsx3PlcpBip8SES15MinBucket": dsx3PlcpBip8SES15MinBucket,
       "dsx3PlcpBip8SES24HrBucket": dsx3PlcpBip8SES24HrBucket,
       "dsx3PlcpSEFSCurrent": dsx3PlcpSEFSCurrent,
       "dsx3PlcpSEFS15MinBucket": dsx3PlcpSEFS15MinBucket,
       "dsx3PlcpSEFS24HrBucket": dsx3PlcpSEFS24HrBucket,
       "dsx3PlcpUASCurrent": dsx3PlcpUASCurrent,
       "dsx3PlcpUAS15MinBucket": dsx3PlcpUAS15MinBucket,
       "dsx3PlcpUAS24HrBucket": dsx3PlcpUAS24HrBucket,
       "dsx3PlcpAlarmClrButton": dsx3PlcpAlarmClrButton,
       "dsx3PlcpCounter": dsx3PlcpCounter,
       "dsx3PlcpCounterTable": dsx3PlcpCounterTable,
       "dsx3PlcpCounterEntry": dsx3PlcpCounterEntry,
       "dsx3PlcpRcvBip8Count": dsx3PlcpRcvBip8Count,
       "dsx3PlcpRcvOOFCount": dsx3PlcpRcvOOFCount,
       "dsx3PlcpRcvRAICount": dsx3PlcpRcvRAICount,
       "dsx3PlcpFECount": dsx3PlcpFECount,
       "dsx3PlcpFESecCount": dsx3PlcpFESecCount,
       "dsx3PlcpSEFESecCount": dsx3PlcpSEFESecCount,
       "dsx3PlcpFEBECount": dsx3PlcpFEBECount,
       "dsx3PlcpFEBESecCount": dsx3PlcpFEBESecCount,
       "dsx3PlcpSEFEBESecCount": dsx3PlcpSEFEBESecCount,
       "dsx3PlcpHECCount": dsx3PlcpHECCount,
       "dsx3PlcpHECSecCount": dsx3PlcpHECSecCount,
       "dsx3PlcpSEHECSecCount": dsx3PlcpSEHECSecCount,
       "dsx3PlcpCounterClrButton": dsx3PlcpCounterClrButton,
       "dsx3PlcpCounterValidEntries": dsx3PlcpCounterValidEntries,
       "ciscoMgx82xxDsx3MIB": ciscoMgx82xxDsx3MIB,
       "cmDsx3MIBConformance": cmDsx3MIBConformance,
       "cmDsx3MIBGroups": cmDsx3MIBGroups,
       "cmDsx3GeneralGroup": cmDsx3GeneralGroup,
       "cmDsx3ConfGroup": cmDsx3ConfGroup,
       "cmDsx3E3ConfGroup": cmDsx3E3ConfGroup,
       "cmDsx3BertConfigGroup": cmDsx3BertConfigGroup,
       "cmDsx3StatsGroup": cmDsx3StatsGroup,
       "cmDsx3E3AlarmConfGenGroup": cmDsx3E3AlarmConfGenGroup,
       "cmDsx3AlarmConfGroup": cmDsx3AlarmConfGroup,
       "cmDsx3E3AlarmConfGroup": cmDsx3E3AlarmConfGroup,
       "cmDsx3AlarmStatsGenGroup": cmDsx3AlarmStatsGenGroup,
       "cmDsx3AlarmStatsGroup": cmDsx3AlarmStatsGroup,
       "cmDsx3E3AlarmStatsGroup": cmDsx3E3AlarmStatsGroup,
       "cmDsx3PlcpConfGroup": cmDsx3PlcpConfGroup,
       "cmDsx3PlcpStatsGroup": cmDsx3PlcpStatsGroup,
       "cmDsx3PlcpAlarmConfGroup": cmDsx3PlcpAlarmConfGroup,
       "cmDsx3PlcpAlarmGroup": cmDsx3PlcpAlarmGroup,
       "cmDsx3MIBCompliances": cmDsx3MIBCompliances,
       "cmDsx3Compliance": cmDsx3Compliance}
)
