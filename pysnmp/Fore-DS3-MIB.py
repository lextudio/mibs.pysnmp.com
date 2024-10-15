# SNMP MIB module (Fore-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-DS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:55 2024
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

foreDs3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ds3ConfGroup_ObjectIdentity = ObjectIdentity
ds3ConfGroup = _Ds3ConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1)
)
_Ds3ConfTable_Object = MibTable
ds3ConfTable = _Ds3ConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ds3ConfTable.setStatus("current")
_Ds3ConfEntry_Object = MibTableRow
ds3ConfEntry = _Ds3ConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1)
)
ds3ConfEntry.setIndexNames(
    (0, "Fore-DS3-MIB", "ds3ConfBoard"),
    (0, "Fore-DS3-MIB", "ds3ConfModule"),
    (0, "Fore-DS3-MIB", "ds3ConfPort"),
)
if mibBuilder.loadTexts:
    ds3ConfEntry.setStatus("current")
_Ds3ConfBoard_Type = Integer32
_Ds3ConfBoard_Object = MibTableColumn
ds3ConfBoard = _Ds3ConfBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 1),
    _Ds3ConfBoard_Type()
)
ds3ConfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3ConfBoard.setStatus("current")
_Ds3ConfModule_Type = Integer32
_Ds3ConfModule_Object = MibTableColumn
ds3ConfModule = _Ds3ConfModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 2),
    _Ds3ConfModule_Type()
)
ds3ConfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3ConfModule.setStatus("current")
_Ds3ConfPort_Type = Integer32
_Ds3ConfPort_Object = MibTableColumn
ds3ConfPort = _Ds3ConfPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 3),
    _Ds3ConfPort_Type()
)
ds3ConfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3ConfPort.setStatus("current")


class _Ds3LineType_Type(Integer32):
    """Custom type ds3LineType based on Integer32"""
    defaultValue = 4

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
        *(("ds3CbitParity", 4),
          ("ds3ClearChannel", 5),
          ("ds3M23", 2),
          ("ds3Other", 1),
          ("ds3SYNTRAN", 3))
    )


_Ds3LineType_Type.__name__ = "Integer32"
_Ds3LineType_Object = MibTableColumn
ds3LineType = _Ds3LineType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 4),
    _Ds3LineType_Type()
)
ds3LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3LineType.setStatus("current")


class _Ds3LineCoding_Type(Integer32):
    """Custom type ds3LineCoding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3B3ZS", 2),
          ("ds3Other", 1))
    )


_Ds3LineCoding_Type.__name__ = "Integer32"
_Ds3LineCoding_Object = MibTableColumn
ds3LineCoding = _Ds3LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 5),
    _Ds3LineCoding_Type()
)
ds3LineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3LineCoding.setStatus("current")


class _Ds3SendCode_Type(Integer32):
    """Custom type ds3SendCode based on Integer32"""
    defaultValue = 1

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
        *(("ds3SendDS1LoopCode", 5),
          ("ds3SendLineCode", 2),
          ("ds3SendNoCode", 1),
          ("ds3SendPayloadCode", 3),
          ("ds3SendResetCode", 4),
          ("ds3SendTestPattern", 6))
    )


_Ds3SendCode_Type.__name__ = "Integer32"
_Ds3SendCode_Object = MibTableColumn
ds3SendCode = _Ds3SendCode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 6),
    _Ds3SendCode_Type()
)
ds3SendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3SendCode.setStatus("current")


class _Ds3ReceiveCode_Type(Integer32):
    """Custom type ds3ReceiveCode based on Integer32"""
    defaultValue = 1

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
        *(("ds3ReceiveDS1LoopCode", 5),
          ("ds3ReceiveLineCode", 2),
          ("ds3ReceiveNoCode", 1),
          ("ds3ReceivePayloadCode", 3),
          ("ds3ReceiveResetCode", 4),
          ("ds3ReceiveTestPattern", 6))
    )


_Ds3ReceiveCode_Type.__name__ = "Integer32"
_Ds3ReceiveCode_Object = MibTableColumn
ds3ReceiveCode = _Ds3ReceiveCode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 7),
    _Ds3ReceiveCode_Type()
)
ds3ReceiveCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3ReceiveCode.setStatus("current")


class _Ds3LoopbackConfig_Type(Integer32):
    """Custom type ds3LoopbackConfig based on Integer32"""
    defaultValue = 1

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
        *(("ds3CellLoop", 2),
          ("ds3DiagLoop", 4),
          ("ds3LineLoop", 5),
          ("ds3NoLoop", 1),
          ("ds3OtherLoop", 6),
          ("ds3PayloadLoop", 3))
    )


_Ds3LoopbackConfig_Type.__name__ = "Integer32"
_Ds3LoopbackConfig_Object = MibTableColumn
ds3LoopbackConfig = _Ds3LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 8),
    _Ds3LoopbackConfig_Type()
)
ds3LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3LoopbackConfig.setStatus("current")


class _Ds3TxClockSource_Type(Integer32):
    """Custom type ds3TxClockSource based on Integer32"""
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


_Ds3TxClockSource_Type.__name__ = "Integer32"
_Ds3TxClockSource_Object = MibTableColumn
ds3TxClockSource = _Ds3TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 9),
    _Ds3TxClockSource_Type()
)
ds3TxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3TxClockSource.setStatus("current")


class _Ds3RxScrambling_Type(Integer32):
    """Custom type ds3RxScrambling based on Integer32"""
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


_Ds3RxScrambling_Type.__name__ = "Integer32"
_Ds3RxScrambling_Object = MibTableColumn
ds3RxScrambling = _Ds3RxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 10),
    _Ds3RxScrambling_Type()
)
ds3RxScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3RxScrambling.setStatus("current")


class _Ds3TxScrambling_Type(Integer32):
    """Custom type ds3TxScrambling based on Integer32"""
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


_Ds3TxScrambling_Type.__name__ = "Integer32"
_Ds3TxScrambling_Object = MibTableColumn
ds3TxScrambling = _Ds3TxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 11),
    _Ds3TxScrambling_Type()
)
ds3TxScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3TxScrambling.setStatus("current")


class _Ds3LineStatus_Type(Integer32):
    """Custom type ds3LineStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_Ds3LineStatus_Type.__name__ = "Integer32"
_Ds3LineStatus_Object = MibTableColumn
ds3LineStatus = _Ds3LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 12),
    _Ds3LineStatus_Type()
)
ds3LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3LineStatus.setStatus("current")


class _Ds3IdleUnassignedCells_Type(Integer32):
    """Custom type ds3IdleUnassignedCells based on Integer32"""
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


_Ds3IdleUnassignedCells_Type.__name__ = "Integer32"
_Ds3IdleUnassignedCells_Object = MibTableColumn
ds3IdleUnassignedCells = _Ds3IdleUnassignedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 13),
    _Ds3IdleUnassignedCells_Type()
)
ds3IdleUnassignedCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3IdleUnassignedCells.setStatus("current")


class _Ds3LineTypeFraming_Type(Integer32):
    """Custom type ds3LineTypeFraming based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3Hcs", 1),
          ("ds3Plcp", 2))
    )


_Ds3LineTypeFraming_Type.__name__ = "Integer32"
_Ds3LineTypeFraming_Object = MibTableColumn
ds3LineTypeFraming = _Ds3LineTypeFraming_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 14),
    _Ds3LineTypeFraming_Type()
)
ds3LineTypeFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3LineTypeFraming.setStatus("current")


class _Ds3LineLength_Type(Integer32):
    """Custom type ds3LineLength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3LineGt225", 2),
          ("ds3LineLt225", 1))
    )


_Ds3LineLength_Type.__name__ = "Integer32"
_Ds3LineLength_Object = MibTableColumn
ds3LineLength = _Ds3LineLength_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 15),
    _Ds3LineLength_Type()
)
ds3LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3LineLength.setStatus("current")


class _Ds3PbitPErrThrSeconds_Type(Integer32):
    """Custom type ds3PbitPErrThrSeconds based on Integer32"""
    defaultValue = 10


_Ds3PbitPErrThrSeconds_Object = MibTableColumn
ds3PbitPErrThrSeconds = _Ds3PbitPErrThrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 16),
    _Ds3PbitPErrThrSeconds_Type()
)
ds3PbitPErrThrSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3PbitPErrThrSeconds.setStatus("current")
_Ds3PbitPErrThrErrors_Type = Integer32
_Ds3PbitPErrThrErrors_Object = MibTableColumn
ds3PbitPErrThrErrors = _Ds3PbitPErrThrErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 17),
    _Ds3PbitPErrThrErrors_Type()
)
ds3PbitPErrThrErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3PbitPErrThrErrors.setStatus("current")


class _Ds3PbitPErrFailEnable_Type(Integer32):
    """Custom type ds3PbitPErrFailEnable based on Integer32"""
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


_Ds3PbitPErrFailEnable_Type.__name__ = "Integer32"
_Ds3PbitPErrFailEnable_Object = MibTableColumn
ds3PbitPErrFailEnable = _Ds3PbitPErrFailEnable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 18),
    _Ds3PbitPErrFailEnable_Type()
)
ds3PbitPErrFailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3PbitPErrFailEnable.setStatus("current")
_Ds3SigFailBer_Type = Integer32
_Ds3SigFailBer_Object = MibTableColumn
ds3SigFailBer = _Ds3SigFailBer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 19),
    _Ds3SigFailBer_Type()
)
ds3SigFailBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3SigFailBer.setStatus("current")
_Ds3SigDegradeBer_Type = Integer32
_Ds3SigDegradeBer_Object = MibTableColumn
ds3SigDegradeBer = _Ds3SigDegradeBer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 20),
    _Ds3SigDegradeBer_Type()
)
ds3SigDegradeBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3SigDegradeBer.setStatus("current")


class _Ds3BerErrorModel_Type(Integer32):
    """Custom type ds3BerErrorModel based on Integer32"""
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


_Ds3BerErrorModel_Type.__name__ = "Integer32"
_Ds3BerErrorModel_Object = MibTableColumn
ds3BerErrorModel = _Ds3BerErrorModel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 21),
    _Ds3BerErrorModel_Type()
)
ds3BerErrorModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3BerErrorModel.setStatus("current")


class _Ds3BerState_Type(Integer32):
    """Custom type ds3BerState based on Integer32"""
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


_Ds3BerState_Type.__name__ = "Integer32"
_Ds3BerState_Object = MibTableColumn
ds3BerState = _Ds3BerState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 1, 1, 1, 22),
    _Ds3BerState_Type()
)
ds3BerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3BerState.setStatus("current")
_Ds3StatsGroup_ObjectIdentity = ObjectIdentity
ds3StatsGroup = _Ds3StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2)
)
_Ds3FramingTable_Object = MibTable
ds3FramingTable = _Ds3FramingTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ds3FramingTable.setStatus("current")
_Ds3FramingEntry_Object = MibTableRow
ds3FramingEntry = _Ds3FramingEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1)
)
ds3FramingEntry.setIndexNames(
    (0, "Fore-DS3-MIB", "ds3FramingBoard"),
    (0, "Fore-DS3-MIB", "ds3FramingModule"),
    (0, "Fore-DS3-MIB", "ds3FramingPort"),
)
if mibBuilder.loadTexts:
    ds3FramingEntry.setStatus("current")
_Ds3FramingBoard_Type = Integer32
_Ds3FramingBoard_Object = MibTableColumn
ds3FramingBoard = _Ds3FramingBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 1),
    _Ds3FramingBoard_Type()
)
ds3FramingBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FramingBoard.setStatus("current")
_Ds3FramingModule_Type = Integer32
_Ds3FramingModule_Object = MibTableColumn
ds3FramingModule = _Ds3FramingModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 2),
    _Ds3FramingModule_Type()
)
ds3FramingModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FramingModule.setStatus("current")
_Ds3FramingPort_Type = Integer32
_Ds3FramingPort_Object = MibTableColumn
ds3FramingPort = _Ds3FramingPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 3),
    _Ds3FramingPort_Type()
)
ds3FramingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FramingPort.setStatus("current")
_Ds3FramingLOSs_Type = Counter32
_Ds3FramingLOSs_Object = MibTableColumn
ds3FramingLOSs = _Ds3FramingLOSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 4),
    _Ds3FramingLOSs_Type()
)
ds3FramingLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FramingLOSs.setStatus("current")
_Ds3FramingLCVs_Type = Counter32
_Ds3FramingLCVs_Object = MibTableColumn
ds3FramingLCVs = _Ds3FramingLCVs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 5),
    _Ds3FramingLCVs_Type()
)
ds3FramingLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FramingLCVs.setStatus("current")
_Ds3FramingSumLCVs_Type = Counter32
_Ds3FramingSumLCVs_Object = MibTableColumn
ds3FramingSumLCVs = _Ds3FramingSumLCVs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 6),
    _Ds3FramingSumLCVs_Type()
)
ds3FramingSumLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FramingSumLCVs.setStatus("current")
_Ds3FramingFERRs_Type = Counter32
_Ds3FramingFERRs_Object = MibTableColumn
ds3FramingFERRs = _Ds3FramingFERRs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 7),
    _Ds3FramingFERRs_Type()
)
ds3FramingFERRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FramingFERRs.setStatus("current")
_Ds3FramingOOFs_Type = Counter32
_Ds3FramingOOFs_Object = MibTableColumn
ds3FramingOOFs = _Ds3FramingOOFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 8),
    _Ds3FramingOOFs_Type()
)
ds3FramingOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FramingOOFs.setStatus("current")
_Ds3FramingFERFs_Type = Counter32
_Ds3FramingFERFs_Object = MibTableColumn
ds3FramingFERFs = _Ds3FramingFERFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 9),
    _Ds3FramingFERFs_Type()
)
ds3FramingFERFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FramingFERFs.setStatus("current")
_Ds3FramingAISs_Type = Counter32
_Ds3FramingAISs_Object = MibTableColumn
ds3FramingAISs = _Ds3FramingAISs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 10),
    _Ds3FramingAISs_Type()
)
ds3FramingAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FramingAISs.setStatus("current")
_Ds3FramingPbitPERRs_Type = Counter32
_Ds3FramingPbitPERRs_Object = MibTableColumn
ds3FramingPbitPERRs = _Ds3FramingPbitPERRs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 11),
    _Ds3FramingPbitPERRs_Type()
)
ds3FramingPbitPERRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FramingPbitPERRs.setStatus("current")
_Ds3FramingCbitPERRs_Type = Counter32
_Ds3FramingCbitPERRs_Object = MibTableColumn
ds3FramingCbitPERRs = _Ds3FramingCbitPERRs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 12),
    _Ds3FramingCbitPERRs_Type()
)
ds3FramingCbitPERRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FramingCbitPERRs.setStatus("current")
_Ds3FramingFEBEs_Type = Counter32
_Ds3FramingFEBEs_Object = MibTableColumn
ds3FramingFEBEs = _Ds3FramingFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 13),
    _Ds3FramingFEBEs_Type()
)
ds3FramingFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FramingFEBEs.setStatus("current")
_Ds3FramingIDLEs_Type = Counter32
_Ds3FramingIDLEs_Object = MibTableColumn
ds3FramingIDLEs = _Ds3FramingIDLEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 1, 1, 14),
    _Ds3FramingIDLEs_Type()
)
ds3FramingIDLEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3FramingIDLEs.setStatus("current")
_Ds3PlcpTable_Object = MibTable
ds3PlcpTable = _Ds3PlcpTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ds3PlcpTable.setStatus("current")
_Ds3PlcpEntry_Object = MibTableRow
ds3PlcpEntry = _Ds3PlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1)
)
ds3PlcpEntry.setIndexNames(
    (0, "Fore-DS3-MIB", "ds3PlcpBoard"),
    (0, "Fore-DS3-MIB", "ds3PlcpModule"),
    (0, "Fore-DS3-MIB", "ds3PlcpPort"),
)
if mibBuilder.loadTexts:
    ds3PlcpEntry.setStatus("current")
_Ds3PlcpBoard_Type = Integer32
_Ds3PlcpBoard_Object = MibTableColumn
ds3PlcpBoard = _Ds3PlcpBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 1),
    _Ds3PlcpBoard_Type()
)
ds3PlcpBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3PlcpBoard.setStatus("current")
_Ds3PlcpModule_Type = Integer32
_Ds3PlcpModule_Object = MibTableColumn
ds3PlcpModule = _Ds3PlcpModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 2),
    _Ds3PlcpModule_Type()
)
ds3PlcpModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3PlcpModule.setStatus("current")
_Ds3PlcpPort_Type = Integer32
_Ds3PlcpPort_Object = MibTableColumn
ds3PlcpPort = _Ds3PlcpPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 3),
    _Ds3PlcpPort_Type()
)
ds3PlcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3PlcpPort.setStatus("current")
_Ds3PlcpFERRs_Type = Counter32
_Ds3PlcpFERRs_Object = MibTableColumn
ds3PlcpFERRs = _Ds3PlcpFERRs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 4),
    _Ds3PlcpFERRs_Type()
)
ds3PlcpFERRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3PlcpFERRs.setStatus("current")
_Ds3PlcpLOFs_Type = Counter32
_Ds3PlcpLOFs_Object = MibTableColumn
ds3PlcpLOFs = _Ds3PlcpLOFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 5),
    _Ds3PlcpLOFs_Type()
)
ds3PlcpLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3PlcpLOFs.setStatus("current")
_Ds3PlcpBIP8s_Type = Counter32
_Ds3PlcpBIP8s_Object = MibTableColumn
ds3PlcpBIP8s = _Ds3PlcpBIP8s_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 6),
    _Ds3PlcpBIP8s_Type()
)
ds3PlcpBIP8s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3PlcpBIP8s.setStatus("current")
_Ds3PlcpFEBEs_Type = Counter32
_Ds3PlcpFEBEs_Object = MibTableColumn
ds3PlcpFEBEs = _Ds3PlcpFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 7),
    _Ds3PlcpFEBEs_Type()
)
ds3PlcpFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3PlcpFEBEs.setStatus("current")
_Ds3PlcpYellows_Type = Counter32
_Ds3PlcpYellows_Object = MibTableColumn
ds3PlcpYellows = _Ds3PlcpYellows_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 2, 1, 8),
    _Ds3PlcpYellows_Type()
)
ds3PlcpYellows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3PlcpYellows.setStatus("current")
_Ds3AtmTable_Object = MibTable
ds3AtmTable = _Ds3AtmTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ds3AtmTable.setStatus("current")
_Ds3AtmEntry_Object = MibTableRow
ds3AtmEntry = _Ds3AtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1)
)
ds3AtmEntry.setIndexNames(
    (0, "Fore-DS3-MIB", "ds3AtmBoard"),
    (0, "Fore-DS3-MIB", "ds3AtmModule"),
    (0, "Fore-DS3-MIB", "ds3AtmPort"),
)
if mibBuilder.loadTexts:
    ds3AtmEntry.setStatus("current")
_Ds3AtmBoard_Type = Integer32
_Ds3AtmBoard_Object = MibTableColumn
ds3AtmBoard = _Ds3AtmBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1, 1),
    _Ds3AtmBoard_Type()
)
ds3AtmBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmBoard.setStatus("current")
_Ds3AtmModule_Type = Integer32
_Ds3AtmModule_Object = MibTableColumn
ds3AtmModule = _Ds3AtmModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1, 2),
    _Ds3AtmModule_Type()
)
ds3AtmModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmModule.setStatus("current")
_Ds3AtmPort_Type = Integer32
_Ds3AtmPort_Object = MibTableColumn
ds3AtmPort = _Ds3AtmPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1, 3),
    _Ds3AtmPort_Type()
)
ds3AtmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmPort.setStatus("current")
_Ds3AtmHCSs_Type = Counter32
_Ds3AtmHCSs_Object = MibTableColumn
ds3AtmHCSs = _Ds3AtmHCSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1, 4),
    _Ds3AtmHCSs_Type()
)
ds3AtmHCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmHCSs.setStatus("current")
_Ds3AtmRxCells_Type = Counter32
_Ds3AtmRxCells_Object = MibTableColumn
ds3AtmRxCells = _Ds3AtmRxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1, 5),
    _Ds3AtmRxCells_Type()
)
ds3AtmRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmRxCells.setStatus("current")
_Ds3AtmTxCells_Type = Counter32
_Ds3AtmTxCells_Object = MibTableColumn
ds3AtmTxCells = _Ds3AtmTxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1, 6),
    _Ds3AtmTxCells_Type()
)
ds3AtmTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmTxCells.setStatus("current")
_Ds3AtmLCDs_Type = Counter32
_Ds3AtmLCDs_Object = MibTableColumn
ds3AtmLCDs = _Ds3AtmLCDs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 3, 2, 3, 1, 7),
    _Ds3AtmLCDs_Type()
)
ds3AtmLCDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLCDs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-DS3-MIB",
    **{"foreDs3": foreDs3,
       "ds3ConfGroup": ds3ConfGroup,
       "ds3ConfTable": ds3ConfTable,
       "ds3ConfEntry": ds3ConfEntry,
       "ds3ConfBoard": ds3ConfBoard,
       "ds3ConfModule": ds3ConfModule,
       "ds3ConfPort": ds3ConfPort,
       "ds3LineType": ds3LineType,
       "ds3LineCoding": ds3LineCoding,
       "ds3SendCode": ds3SendCode,
       "ds3ReceiveCode": ds3ReceiveCode,
       "ds3LoopbackConfig": ds3LoopbackConfig,
       "ds3TxClockSource": ds3TxClockSource,
       "ds3RxScrambling": ds3RxScrambling,
       "ds3TxScrambling": ds3TxScrambling,
       "ds3LineStatus": ds3LineStatus,
       "ds3IdleUnassignedCells": ds3IdleUnassignedCells,
       "ds3LineTypeFraming": ds3LineTypeFraming,
       "ds3LineLength": ds3LineLength,
       "ds3PbitPErrThrSeconds": ds3PbitPErrThrSeconds,
       "ds3PbitPErrThrErrors": ds3PbitPErrThrErrors,
       "ds3PbitPErrFailEnable": ds3PbitPErrFailEnable,
       "ds3SigFailBer": ds3SigFailBer,
       "ds3SigDegradeBer": ds3SigDegradeBer,
       "ds3BerErrorModel": ds3BerErrorModel,
       "ds3BerState": ds3BerState,
       "ds3StatsGroup": ds3StatsGroup,
       "ds3FramingTable": ds3FramingTable,
       "ds3FramingEntry": ds3FramingEntry,
       "ds3FramingBoard": ds3FramingBoard,
       "ds3FramingModule": ds3FramingModule,
       "ds3FramingPort": ds3FramingPort,
       "ds3FramingLOSs": ds3FramingLOSs,
       "ds3FramingLCVs": ds3FramingLCVs,
       "ds3FramingSumLCVs": ds3FramingSumLCVs,
       "ds3FramingFERRs": ds3FramingFERRs,
       "ds3FramingOOFs": ds3FramingOOFs,
       "ds3FramingFERFs": ds3FramingFERFs,
       "ds3FramingAISs": ds3FramingAISs,
       "ds3FramingPbitPERRs": ds3FramingPbitPERRs,
       "ds3FramingCbitPERRs": ds3FramingCbitPERRs,
       "ds3FramingFEBEs": ds3FramingFEBEs,
       "ds3FramingIDLEs": ds3FramingIDLEs,
       "ds3PlcpTable": ds3PlcpTable,
       "ds3PlcpEntry": ds3PlcpEntry,
       "ds3PlcpBoard": ds3PlcpBoard,
       "ds3PlcpModule": ds3PlcpModule,
       "ds3PlcpPort": ds3PlcpPort,
       "ds3PlcpFERRs": ds3PlcpFERRs,
       "ds3PlcpLOFs": ds3PlcpLOFs,
       "ds3PlcpBIP8s": ds3PlcpBIP8s,
       "ds3PlcpFEBEs": ds3PlcpFEBEs,
       "ds3PlcpYellows": ds3PlcpYellows,
       "ds3AtmTable": ds3AtmTable,
       "ds3AtmEntry": ds3AtmEntry,
       "ds3AtmBoard": ds3AtmBoard,
       "ds3AtmModule": ds3AtmModule,
       "ds3AtmPort": ds3AtmPort,
       "ds3AtmHCSs": ds3AtmHCSs,
       "ds3AtmRxCells": ds3AtmRxCells,
       "ds3AtmTxCells": ds3AtmTxCells,
       "ds3AtmLCDs": ds3AtmLCDs}
)
