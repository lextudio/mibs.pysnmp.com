# SNMP MIB module (Fore-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:54 2024
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

(asx,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "asx")

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

foreDs1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ds1ConfGroup_ObjectIdentity = ObjectIdentity
ds1ConfGroup = _Ds1ConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1)
)
_Ds1ConfTable_Object = MibTable
ds1ConfTable = _Ds1ConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    ds1ConfTable.setStatus("current")
_Ds1ConfEntry_Object = MibTableRow
ds1ConfEntry = _Ds1ConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1)
)
ds1ConfEntry.setIndexNames(
    (0, "Fore-DS1-MIB", "ds1ConfBoard"),
    (0, "Fore-DS1-MIB", "ds1ConfModule"),
    (0, "Fore-DS1-MIB", "ds1ConfPort"),
)
if mibBuilder.loadTexts:
    ds1ConfEntry.setStatus("current")
_Ds1ConfBoard_Type = Integer32
_Ds1ConfBoard_Object = MibTableColumn
ds1ConfBoard = _Ds1ConfBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 1),
    _Ds1ConfBoard_Type()
)
ds1ConfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1ConfBoard.setStatus("current")
_Ds1ConfModule_Type = Integer32
_Ds1ConfModule_Object = MibTableColumn
ds1ConfModule = _Ds1ConfModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 2),
    _Ds1ConfModule_Type()
)
ds1ConfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1ConfModule.setStatus("current")
_Ds1ConfPort_Type = Integer32
_Ds1ConfPort_Object = MibTableColumn
ds1ConfPort = _Ds1ConfPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 3),
    _Ds1ConfPort_Type()
)
ds1ConfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1ConfPort.setStatus("current")


class _Ds1LineType_Type(Integer32):
    """Custom type ds1LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds1D4", 3),
          ("ds1ESF", 2),
          ("ds1Other", 1))
    )


_Ds1LineType_Type.__name__ = "Integer32"
_Ds1LineType_Object = MibTableColumn
ds1LineType = _Ds1LineType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 4),
    _Ds1LineType_Type()
)
ds1LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1LineType.setStatus("current")


class _Ds1LineCoding_Type(Integer32):
    """Custom type ds1LineCoding based on Integer32"""
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
        *(("ds1AMI", 6),
          ("ds1B8ZS", 3),
          ("ds1HDB3", 4),
          ("ds1JBZS", 2),
          ("ds1Other", 1),
          ("ds1ZBTSI", 5))
    )


_Ds1LineCoding_Type.__name__ = "Integer32"
_Ds1LineCoding_Object = MibTableColumn
ds1LineCoding = _Ds1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 5),
    _Ds1LineCoding_Type()
)
ds1LineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1LineCoding.setStatus("current")


class _Ds1SendCode_Type(Integer32):
    """Custom type ds1SendCode based on Integer32"""
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
        *(("ds1Send3in24Pattern", 7),
          ("ds1Send511Pattern", 6),
          ("ds1SendLineCode", 2),
          ("ds1SendNoCode", 1),
          ("ds1SendOtherTestPattern", 8),
          ("ds1SendPayloadCode", 3),
          ("ds1SendQRS", 5),
          ("ds1SendResetCode", 4))
    )


_Ds1SendCode_Type.__name__ = "Integer32"
_Ds1SendCode_Object = MibTableColumn
ds1SendCode = _Ds1SendCode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 6),
    _Ds1SendCode_Type()
)
ds1SendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1SendCode.setStatus("current")


class _Ds1ReceiveCode_Type(Integer32):
    """Custom type ds1ReceiveCode based on Integer32"""
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
        *(("ds1ReceiveLineCode", 2),
          ("ds1ReceiveNoCode", 1),
          ("ds1ReceivePayloadCode", 3),
          ("ds1ReceiveResetCode", 4),
          ("ds1Send3in24Pattern", 7),
          ("ds1Send511Pattern", 6),
          ("ds1SendOtherTestPattern", 8),
          ("ds1SendQRS", 5))
    )


_Ds1ReceiveCode_Type.__name__ = "Integer32"
_Ds1ReceiveCode_Object = MibTableColumn
ds1ReceiveCode = _Ds1ReceiveCode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 7),
    _Ds1ReceiveCode_Type()
)
ds1ReceiveCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1ReceiveCode.setStatus("current")


class _Ds1LoopbackConfig_Type(Integer32):
    """Custom type ds1LoopbackConfig based on Integer32"""
    defaultValue = 1

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
        *(("ds1DiagLoop", 4),
          ("ds1LineLoop", 2),
          ("ds1NoLoop", 1),
          ("ds1OtherLoop", 5),
          ("ds1PayloadLoop", 3))
    )


_Ds1LoopbackConfig_Type.__name__ = "Integer32"
_Ds1LoopbackConfig_Object = MibTableColumn
ds1LoopbackConfig = _Ds1LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 8),
    _Ds1LoopbackConfig_Type()
)
ds1LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1LoopbackConfig.setStatus("current")


class _Ds1TxClockSource_Type(Integer32):
    """Custom type ds1TxClockSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("rxTiming", 1))
    )


_Ds1TxClockSource_Type.__name__ = "Integer32"
_Ds1TxClockSource_Object = MibTableColumn
ds1TxClockSource = _Ds1TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 9),
    _Ds1TxClockSource_Type()
)
ds1TxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1TxClockSource.setStatus("current")


class _Ds1LineStatus_Type(Integer32):
    """Custom type ds1LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_Ds1LineStatus_Type.__name__ = "Integer32"
_Ds1LineStatus_Object = MibTableColumn
ds1LineStatus = _Ds1LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 12),
    _Ds1LineStatus_Type()
)
ds1LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1LineStatus.setStatus("current")


class _Ds1IdleUnassignedCells_Type(Integer32):
    """Custom type ds1IdleUnassignedCells based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 2),
          ("unassigned", 1))
    )


_Ds1IdleUnassignedCells_Type.__name__ = "Integer32"
_Ds1IdleUnassignedCells_Object = MibTableColumn
ds1IdleUnassignedCells = _Ds1IdleUnassignedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 13),
    _Ds1IdleUnassignedCells_Type()
)
ds1IdleUnassignedCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1IdleUnassignedCells.setStatus("current")


class _Ds1LineTypeFraming_Type(Integer32):
    """Custom type ds1LineTypeFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds1Hcs", 2),
          ("ds1Plcp", 3),
          ("other", 1))
    )


_Ds1LineTypeFraming_Type.__name__ = "Integer32"
_Ds1LineTypeFraming_Object = MibTableColumn
ds1LineTypeFraming = _Ds1LineTypeFraming_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 14),
    _Ds1LineTypeFraming_Type()
)
ds1LineTypeFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1LineTypeFraming.setStatus("current")


class _Ds1LineLength_Type(Integer32):
    """Custom type ds1LineLength based on Integer32"""
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
        *(("ds1Line110-220", 2),
          ("ds1Line110-220Alt", 10),
          ("ds1Line220-330", 3),
          ("ds1Line220-330Alt", 11),
          ("ds1Line330-440", 4),
          ("ds1Line330-440Alt", 12),
          ("ds1Line440-550", 5),
          ("ds1Line440-550Alt", 13),
          ("ds1Line550-660", 6),
          ("ds1Line550-660Alt", 14),
          ("ds1LineGt655", 7),
          ("ds1LineGt655Alt", 15),
          ("ds1LineLt110", 1),
          ("ds1LineLt110Alt", 9))
    )


_Ds1LineLength_Type.__name__ = "Integer32"
_Ds1LineLength_Object = MibTableColumn
ds1LineLength = _Ds1LineLength_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 15),
    _Ds1LineLength_Type()
)
ds1LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1LineLength.setStatus("current")


class _Ds1RxScrambling_Type(Integer32):
    """Custom type ds1RxScrambling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("descrambling", 1),
          ("noDescrambling", 2))
    )


_Ds1RxScrambling_Type.__name__ = "Integer32"
_Ds1RxScrambling_Object = MibTableColumn
ds1RxScrambling = _Ds1RxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 16),
    _Ds1RxScrambling_Type()
)
ds1RxScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1RxScrambling.setStatus("current")


class _Ds1TxScrambling_Type(Integer32):
    """Custom type ds1TxScrambling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noScrambling", 2),
          ("scrambling", 1))
    )


_Ds1TxScrambling_Type.__name__ = "Integer32"
_Ds1TxScrambling_Object = MibTableColumn
ds1TxScrambling = _Ds1TxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 17),
    _Ds1TxScrambling_Type()
)
ds1TxScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1TxScrambling.setStatus("current")


class _Ds1TxPRBS_Type(Integer32):
    """Custom type ds1TxPRBS based on Integer32"""
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
        *(("invert", 3),
          ("off", 1),
          ("on", 2))
    )


_Ds1TxPRBS_Type.__name__ = "Integer32"
_Ds1TxPRBS_Object = MibTableColumn
ds1TxPRBS = _Ds1TxPRBS_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 18),
    _Ds1TxPRBS_Type()
)
ds1TxPRBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1TxPRBS.setStatus("current")


class _Ds1CRCErrThrSeconds_Type(Integer32):
    """Custom type ds1CRCErrThrSeconds based on Integer32"""
    defaultValue = 10


_Ds1CRCErrThrSeconds_Object = MibTableColumn
ds1CRCErrThrSeconds = _Ds1CRCErrThrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 19),
    _Ds1CRCErrThrSeconds_Type()
)
ds1CRCErrThrSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1CRCErrThrSeconds.setStatus("current")
_Ds1CRCErrThrErrors_Type = Integer32
_Ds1CRCErrThrErrors_Object = MibTableColumn
ds1CRCErrThrErrors = _Ds1CRCErrThrErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 20),
    _Ds1CRCErrThrErrors_Type()
)
ds1CRCErrThrErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1CRCErrThrErrors.setStatus("current")


class _Ds1CRCErrFailEnable_Type(Integer32):
    """Custom type ds1CRCErrFailEnable based on Integer32"""
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


_Ds1CRCErrFailEnable_Type.__name__ = "Integer32"
_Ds1CRCErrFailEnable_Object = MibTableColumn
ds1CRCErrFailEnable = _Ds1CRCErrFailEnable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 21),
    _Ds1CRCErrFailEnable_Type()
)
ds1CRCErrFailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1CRCErrFailEnable.setStatus("current")
_Ds1SigFailBer_Type = Integer32
_Ds1SigFailBer_Object = MibTableColumn
ds1SigFailBer = _Ds1SigFailBer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 22),
    _Ds1SigFailBer_Type()
)
ds1SigFailBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1SigFailBer.setStatus("current")
_Ds1SigDegradeBer_Type = Integer32
_Ds1SigDegradeBer_Object = MibTableColumn
ds1SigDegradeBer = _Ds1SigDegradeBer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 23),
    _Ds1SigDegradeBer_Type()
)
ds1SigDegradeBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1SigDegradeBer.setStatus("current")


class _Ds1BerErrorModel_Type(Integer32):
    """Custom type ds1BerErrorModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("errorModelBurst", 2),
          ("errorModelNone", 0),
          ("errorModelRandom", 1))
    )


_Ds1BerErrorModel_Type.__name__ = "Integer32"
_Ds1BerErrorModel_Object = MibTableColumn
ds1BerErrorModel = _Ds1BerErrorModel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 24),
    _Ds1BerErrorModel_Type()
)
ds1BerErrorModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1BerErrorModel.setStatus("current")


class _Ds1BerState_Type(Integer32):
    """Custom type ds1BerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("berStateOk", 0),
          ("berStateSigDegrade", 1),
          ("berStateSigFail", 2))
    )


_Ds1BerState_Type.__name__ = "Integer32"
_Ds1BerState_Object = MibTableColumn
ds1BerState = _Ds1BerState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 25),
    _Ds1BerState_Type()
)
ds1BerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1BerState.setStatus("current")
_Ds1StatsGroup_ObjectIdentity = ObjectIdentity
ds1StatsGroup = _Ds1StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2)
)
_Ds1FramingTable_Object = MibTable
ds1FramingTable = _Ds1FramingTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    ds1FramingTable.setStatus("current")
_Ds1FramingEntry_Object = MibTableRow
ds1FramingEntry = _Ds1FramingEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1)
)
ds1FramingEntry.setIndexNames(
    (0, "Fore-DS1-MIB", "ds1FramingBoard"),
    (0, "Fore-DS1-MIB", "ds1FramingModule"),
    (0, "Fore-DS1-MIB", "ds1FramingPort"),
)
if mibBuilder.loadTexts:
    ds1FramingEntry.setStatus("current")
_Ds1FramingBoard_Type = Integer32
_Ds1FramingBoard_Object = MibTableColumn
ds1FramingBoard = _Ds1FramingBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 1),
    _Ds1FramingBoard_Type()
)
ds1FramingBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FramingBoard.setStatus("current")
_Ds1FramingModule_Type = Integer32
_Ds1FramingModule_Object = MibTableColumn
ds1FramingModule = _Ds1FramingModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 2),
    _Ds1FramingModule_Type()
)
ds1FramingModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FramingModule.setStatus("current")
_Ds1FramingPort_Type = Integer32
_Ds1FramingPort_Object = MibTableColumn
ds1FramingPort = _Ds1FramingPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 3),
    _Ds1FramingPort_Type()
)
ds1FramingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FramingPort.setStatus("current")
_Ds1FramingLOSs_Type = Counter32
_Ds1FramingLOSs_Object = MibTableColumn
ds1FramingLOSs = _Ds1FramingLOSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 4),
    _Ds1FramingLOSs_Type()
)
ds1FramingLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FramingLOSs.setStatus("current")
_Ds1FramingLCVs_Type = Counter32
_Ds1FramingLCVs_Object = MibTableColumn
ds1FramingLCVs = _Ds1FramingLCVs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 5),
    _Ds1FramingLCVs_Type()
)
ds1FramingLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FramingLCVs.setStatus("current")
_Ds1FramingFERRs_Type = Counter32
_Ds1FramingFERRs_Object = MibTableColumn
ds1FramingFERRs = _Ds1FramingFERRs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 6),
    _Ds1FramingFERRs_Type()
)
ds1FramingFERRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FramingFERRs.setStatus("current")
_Ds1FramingOOFs_Type = Counter32
_Ds1FramingOOFs_Object = MibTableColumn
ds1FramingOOFs = _Ds1FramingOOFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 7),
    _Ds1FramingOOFs_Type()
)
ds1FramingOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FramingOOFs.setStatus("current")
_Ds1FramingAISs_Type = Counter32
_Ds1FramingAISs_Object = MibTableColumn
ds1FramingAISs = _Ds1FramingAISs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 8),
    _Ds1FramingAISs_Type()
)
ds1FramingAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FramingAISs.setStatus("current")
_Ds1FramingB8ZSPatterns_Type = Counter32
_Ds1FramingB8ZSPatterns_Object = MibTableColumn
ds1FramingB8ZSPatterns = _Ds1FramingB8ZSPatterns_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 9),
    _Ds1FramingB8ZSPatterns_Type()
)
ds1FramingB8ZSPatterns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FramingB8ZSPatterns.setStatus("deprecated")
_Ds1Framing8Zeros_Type = Counter32
_Ds1Framing8Zeros_Object = MibTableColumn
ds1Framing8Zeros = _Ds1Framing8Zeros_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 10),
    _Ds1Framing8Zeros_Type()
)
ds1Framing8Zeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1Framing8Zeros.setStatus("deprecated")
_Ds1Framing16Zeros_Type = Counter32
_Ds1Framing16Zeros_Object = MibTableColumn
ds1Framing16Zeros = _Ds1Framing16Zeros_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 11),
    _Ds1Framing16Zeros_Type()
)
ds1Framing16Zeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1Framing16Zeros.setStatus("deprecated")
_Ds1FramingYellowAlarms_Type = Counter32
_Ds1FramingYellowAlarms_Object = MibTableColumn
ds1FramingYellowAlarms = _Ds1FramingYellowAlarms_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 12),
    _Ds1FramingYellowAlarms_Type()
)
ds1FramingYellowAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FramingYellowAlarms.setStatus("current")
_Ds1FramingRedAlarms_Type = Counter32
_Ds1FramingRedAlarms_Object = MibTableColumn
ds1FramingRedAlarms = _Ds1FramingRedAlarms_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 13),
    _Ds1FramingRedAlarms_Type()
)
ds1FramingRedAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FramingRedAlarms.setStatus("current")
_Ds1FramingBEEs_Type = Counter32
_Ds1FramingBEEs_Object = MibTableColumn
ds1FramingBEEs = _Ds1FramingBEEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 14),
    _Ds1FramingBEEs_Type()
)
ds1FramingBEEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FramingBEEs.setStatus("current")
_Ds1FramingPRBSs_Type = Counter32
_Ds1FramingPRBSs_Object = MibTableColumn
ds1FramingPRBSs = _Ds1FramingPRBSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 15),
    _Ds1FramingPRBSs_Type()
)
ds1FramingPRBSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FramingPRBSs.setStatus("current")
_Ds1FramingBERs_Type = Counter32
_Ds1FramingBERs_Object = MibTableColumn
ds1FramingBERs = _Ds1FramingBERs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 16),
    _Ds1FramingBERs_Type()
)
ds1FramingBERs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1FramingBERs.setStatus("current")
_Ds1PlcpTable_Object = MibTable
ds1PlcpTable = _Ds1PlcpTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2)
)
if mibBuilder.loadTexts:
    ds1PlcpTable.setStatus("current")
_Ds1PlcpEntry_Object = MibTableRow
ds1PlcpEntry = _Ds1PlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1)
)
ds1PlcpEntry.setIndexNames(
    (0, "Fore-DS1-MIB", "ds1PlcpBoard"),
    (0, "Fore-DS1-MIB", "ds1PlcpModule"),
    (0, "Fore-DS1-MIB", "ds1PlcpPort"),
)
if mibBuilder.loadTexts:
    ds1PlcpEntry.setStatus("current")
_Ds1PlcpBoard_Type = Integer32
_Ds1PlcpBoard_Object = MibTableColumn
ds1PlcpBoard = _Ds1PlcpBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 1),
    _Ds1PlcpBoard_Type()
)
ds1PlcpBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1PlcpBoard.setStatus("current")
_Ds1PlcpModule_Type = Integer32
_Ds1PlcpModule_Object = MibTableColumn
ds1PlcpModule = _Ds1PlcpModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 2),
    _Ds1PlcpModule_Type()
)
ds1PlcpModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1PlcpModule.setStatus("current")
_Ds1PlcpPort_Type = Integer32
_Ds1PlcpPort_Object = MibTableColumn
ds1PlcpPort = _Ds1PlcpPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 3),
    _Ds1PlcpPort_Type()
)
ds1PlcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1PlcpPort.setStatus("current")
_Ds1PlcpBIP8s_Type = Counter32
_Ds1PlcpBIP8s_Object = MibTableColumn
ds1PlcpBIP8s = _Ds1PlcpBIP8s_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 4),
    _Ds1PlcpBIP8s_Type()
)
ds1PlcpBIP8s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1PlcpBIP8s.setStatus("current")
_Ds1PlcpFERRs_Type = Counter32
_Ds1PlcpFERRs_Object = MibTableColumn
ds1PlcpFERRs = _Ds1PlcpFERRs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 5),
    _Ds1PlcpFERRs_Type()
)
ds1PlcpFERRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1PlcpFERRs.setStatus("current")
_Ds1PlcpFEBEs_Type = Counter32
_Ds1PlcpFEBEs_Object = MibTableColumn
ds1PlcpFEBEs = _Ds1PlcpFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 6),
    _Ds1PlcpFEBEs_Type()
)
ds1PlcpFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1PlcpFEBEs.setStatus("current")
_Ds1PlcpLOFs_Type = Counter32
_Ds1PlcpLOFs_Object = MibTableColumn
ds1PlcpLOFs = _Ds1PlcpLOFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 7),
    _Ds1PlcpLOFs_Type()
)
ds1PlcpLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1PlcpLOFs.setStatus("current")
_Ds1PlcpYellows_Type = Counter32
_Ds1PlcpYellows_Object = MibTableColumn
ds1PlcpYellows = _Ds1PlcpYellows_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 8),
    _Ds1PlcpYellows_Type()
)
ds1PlcpYellows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1PlcpYellows.setStatus("current")
_Ds1AtmTable_Object = MibTable
ds1AtmTable = _Ds1AtmTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3)
)
if mibBuilder.loadTexts:
    ds1AtmTable.setStatus("current")
_Ds1AtmEntry_Object = MibTableRow
ds1AtmEntry = _Ds1AtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1)
)
ds1AtmEntry.setIndexNames(
    (0, "Fore-DS1-MIB", "ds1AtmBoard"),
    (0, "Fore-DS1-MIB", "ds1AtmModule"),
    (0, "Fore-DS1-MIB", "ds1AtmPort"),
)
if mibBuilder.loadTexts:
    ds1AtmEntry.setStatus("current")
_Ds1AtmBoard_Type = Integer32
_Ds1AtmBoard_Object = MibTableColumn
ds1AtmBoard = _Ds1AtmBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 1),
    _Ds1AtmBoard_Type()
)
ds1AtmBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1AtmBoard.setStatus("current")
_Ds1AtmModule_Type = Integer32
_Ds1AtmModule_Object = MibTableColumn
ds1AtmModule = _Ds1AtmModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 2),
    _Ds1AtmModule_Type()
)
ds1AtmModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1AtmModule.setStatus("current")
_Ds1AtmPort_Type = Integer32
_Ds1AtmPort_Object = MibTableColumn
ds1AtmPort = _Ds1AtmPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 3),
    _Ds1AtmPort_Type()
)
ds1AtmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1AtmPort.setStatus("current")
_Ds1AtmHCSs_Type = Counter32
_Ds1AtmHCSs_Object = MibTableColumn
ds1AtmHCSs = _Ds1AtmHCSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 4),
    _Ds1AtmHCSs_Type()
)
ds1AtmHCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1AtmHCSs.setStatus("current")
_Ds1AtmRxCells_Type = Counter32
_Ds1AtmRxCells_Object = MibTableColumn
ds1AtmRxCells = _Ds1AtmRxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 5),
    _Ds1AtmRxCells_Type()
)
ds1AtmRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1AtmRxCells.setStatus("current")
_Ds1AtmTxCells_Type = Counter32
_Ds1AtmTxCells_Object = MibTableColumn
ds1AtmTxCells = _Ds1AtmTxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 6),
    _Ds1AtmTxCells_Type()
)
ds1AtmTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1AtmTxCells.setStatus("current")
_Ds1AtmUHCSs_Type = Counter32
_Ds1AtmUHCSs_Object = MibTableColumn
ds1AtmUHCSs = _Ds1AtmUHCSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 7),
    _Ds1AtmUHCSs_Type()
)
ds1AtmUHCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1AtmUHCSs.setStatus("current")
_Ds1AtmCHCSs_Type = Counter32
_Ds1AtmCHCSs_Object = MibTableColumn
ds1AtmCHCSs = _Ds1AtmCHCSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 8),
    _Ds1AtmCHCSs_Type()
)
ds1AtmCHCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1AtmCHCSs.setStatus("current")
_Ds1AtmLCDs_Type = Counter32
_Ds1AtmLCDs_Object = MibTableColumn
ds1AtmLCDs = _Ds1AtmLCDs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 9),
    _Ds1AtmLCDs_Type()
)
ds1AtmLCDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1AtmLCDs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-DS1-MIB",
    **{"foreDs1": foreDs1,
       "ds1ConfGroup": ds1ConfGroup,
       "ds1ConfTable": ds1ConfTable,
       "ds1ConfEntry": ds1ConfEntry,
       "ds1ConfBoard": ds1ConfBoard,
       "ds1ConfModule": ds1ConfModule,
       "ds1ConfPort": ds1ConfPort,
       "ds1LineType": ds1LineType,
       "ds1LineCoding": ds1LineCoding,
       "ds1SendCode": ds1SendCode,
       "ds1ReceiveCode": ds1ReceiveCode,
       "ds1LoopbackConfig": ds1LoopbackConfig,
       "ds1TxClockSource": ds1TxClockSource,
       "ds1LineStatus": ds1LineStatus,
       "ds1IdleUnassignedCells": ds1IdleUnassignedCells,
       "ds1LineTypeFraming": ds1LineTypeFraming,
       "ds1LineLength": ds1LineLength,
       "ds1RxScrambling": ds1RxScrambling,
       "ds1TxScrambling": ds1TxScrambling,
       "ds1TxPRBS": ds1TxPRBS,
       "ds1CRCErrThrSeconds": ds1CRCErrThrSeconds,
       "ds1CRCErrThrErrors": ds1CRCErrThrErrors,
       "ds1CRCErrFailEnable": ds1CRCErrFailEnable,
       "ds1SigFailBer": ds1SigFailBer,
       "ds1SigDegradeBer": ds1SigDegradeBer,
       "ds1BerErrorModel": ds1BerErrorModel,
       "ds1BerState": ds1BerState,
       "ds1StatsGroup": ds1StatsGroup,
       "ds1FramingTable": ds1FramingTable,
       "ds1FramingEntry": ds1FramingEntry,
       "ds1FramingBoard": ds1FramingBoard,
       "ds1FramingModule": ds1FramingModule,
       "ds1FramingPort": ds1FramingPort,
       "ds1FramingLOSs": ds1FramingLOSs,
       "ds1FramingLCVs": ds1FramingLCVs,
       "ds1FramingFERRs": ds1FramingFERRs,
       "ds1FramingOOFs": ds1FramingOOFs,
       "ds1FramingAISs": ds1FramingAISs,
       "ds1FramingB8ZSPatterns": ds1FramingB8ZSPatterns,
       "ds1Framing8Zeros": ds1Framing8Zeros,
       "ds1Framing16Zeros": ds1Framing16Zeros,
       "ds1FramingYellowAlarms": ds1FramingYellowAlarms,
       "ds1FramingRedAlarms": ds1FramingRedAlarms,
       "ds1FramingBEEs": ds1FramingBEEs,
       "ds1FramingPRBSs": ds1FramingPRBSs,
       "ds1FramingBERs": ds1FramingBERs,
       "ds1PlcpTable": ds1PlcpTable,
       "ds1PlcpEntry": ds1PlcpEntry,
       "ds1PlcpBoard": ds1PlcpBoard,
       "ds1PlcpModule": ds1PlcpModule,
       "ds1PlcpPort": ds1PlcpPort,
       "ds1PlcpBIP8s": ds1PlcpBIP8s,
       "ds1PlcpFERRs": ds1PlcpFERRs,
       "ds1PlcpFEBEs": ds1PlcpFEBEs,
       "ds1PlcpLOFs": ds1PlcpLOFs,
       "ds1PlcpYellows": ds1PlcpYellows,
       "ds1AtmTable": ds1AtmTable,
       "ds1AtmEntry": ds1AtmEntry,
       "ds1AtmBoard": ds1AtmBoard,
       "ds1AtmModule": ds1AtmModule,
       "ds1AtmPort": ds1AtmPort,
       "ds1AtmHCSs": ds1AtmHCSs,
       "ds1AtmRxCells": ds1AtmRxCells,
       "ds1AtmTxCells": ds1AtmTxCells,
       "ds1AtmUHCSs": ds1AtmUHCSs,
       "ds1AtmCHCSs": ds1AtmCHCSs,
       "ds1AtmLCDs": ds1AtmLCDs}
)
