# SNMP MIB module (Fore-E1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-E1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:57 2024
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

foreE1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_E1ConfGroup_ObjectIdentity = ObjectIdentity
e1ConfGroup = _E1ConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1)
)
_E1ConfTable_Object = MibTable
e1ConfTable = _E1ConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    e1ConfTable.setStatus("current")
_E1ConfEntry_Object = MibTableRow
e1ConfEntry = _E1ConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1)
)
e1ConfEntry.setIndexNames(
    (0, "Fore-E1-MIB", "e1ConfBoard"),
    (0, "Fore-E1-MIB", "e1ConfModule"),
    (0, "Fore-E1-MIB", "e1ConfPort"),
)
if mibBuilder.loadTexts:
    e1ConfEntry.setStatus("current")
_E1ConfBoard_Type = Integer32
_E1ConfBoard_Object = MibTableColumn
e1ConfBoard = _E1ConfBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 1),
    _E1ConfBoard_Type()
)
e1ConfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1ConfBoard.setStatus("current")
_E1ConfModule_Type = Integer32
_E1ConfModule_Object = MibTableColumn
e1ConfModule = _E1ConfModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 2),
    _E1ConfModule_Type()
)
e1ConfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1ConfModule.setStatus("current")
_E1ConfPort_Type = Integer32
_E1ConfPort_Object = MibTableColumn
e1ConfPort = _E1ConfPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 3),
    _E1ConfPort_Type()
)
e1ConfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1ConfPort.setStatus("current")


class _E1LineType_Type(Integer32):
    """Custom type e1LineType based on Integer32"""
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
        *(("e1CRC", 3),
          ("e1CRCMF", 5),
          ("e1MF", 4),
          ("e1NoCRC", 2),
          ("e1Other", 1))
    )


_E1LineType_Type.__name__ = "Integer32"
_E1LineType_Object = MibTableColumn
e1LineType = _E1LineType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 4),
    _E1LineType_Type()
)
e1LineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1LineType.setStatus("current")


class _E1LineCoding_Type(Integer32):
    """Custom type e1LineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1AMI", 3),
          ("e1HDB3", 2),
          ("e1Other", 1))
    )


_E1LineCoding_Type.__name__ = "Integer32"
_E1LineCoding_Object = MibTableColumn
e1LineCoding = _E1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 5),
    _E1LineCoding_Type()
)
e1LineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1LineCoding.setStatus("current")


class _E1SendCode_Type(Integer32):
    """Custom type e1SendCode based on Integer32"""
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
        *(("e1Send3in24Pattern", 7),
          ("e1Send511Pattern", 6),
          ("e1SendLineCode", 2),
          ("e1SendNoCode", 1),
          ("e1SendOtherTestPattern", 8),
          ("e1SendPayloadCode", 3),
          ("e1SendQRS", 5),
          ("e1SendResetCode", 4))
    )


_E1SendCode_Type.__name__ = "Integer32"
_E1SendCode_Object = MibTableColumn
e1SendCode = _E1SendCode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 6),
    _E1SendCode_Type()
)
e1SendCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1SendCode.setStatus("current")


class _E1ReceiveCode_Type(Integer32):
    """Custom type e1ReceiveCode based on Integer32"""
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
        *(("e1ReceiveLineCode", 2),
          ("e1ReceiveNoCode", 1),
          ("e1ReceivePayloadCode", 3),
          ("e1ReceiveResetCode", 4),
          ("e1Send3in24Pattern", 7),
          ("e1Send511Pattern", 6),
          ("e1SendOtherTestPattern", 8),
          ("e1SendQRS", 5))
    )


_E1ReceiveCode_Type.__name__ = "Integer32"
_E1ReceiveCode_Object = MibTableColumn
e1ReceiveCode = _E1ReceiveCode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 7),
    _E1ReceiveCode_Type()
)
e1ReceiveCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1ReceiveCode.setStatus("current")


class _E1LoopbackConfig_Type(Integer32):
    """Custom type e1LoopbackConfig based on Integer32"""
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
        *(("e1DiagLoop", 4),
          ("e1LineLoop", 2),
          ("e1NoLoop", 1),
          ("e1OtherLoop", 5),
          ("e1PayloadLoop", 3))
    )


_E1LoopbackConfig_Type.__name__ = "Integer32"
_E1LoopbackConfig_Object = MibTableColumn
e1LoopbackConfig = _E1LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 8),
    _E1LoopbackConfig_Type()
)
e1LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1LoopbackConfig.setStatus("current")


class _E1TxClockSource_Type(Integer32):
    """Custom type e1TxClockSource based on Integer32"""
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


_E1TxClockSource_Type.__name__ = "Integer32"
_E1TxClockSource_Object = MibTableColumn
e1TxClockSource = _E1TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 9),
    _E1TxClockSource_Type()
)
e1TxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1TxClockSource.setStatus("current")


class _E1LineStatus_Type(Integer32):
    """Custom type e1LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_E1LineStatus_Type.__name__ = "Integer32"
_E1LineStatus_Object = MibTableColumn
e1LineStatus = _E1LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 10),
    _E1LineStatus_Type()
)
e1LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1LineStatus.setStatus("current")


class _E1IdleUnassignedCells_Type(Integer32):
    """Custom type e1IdleUnassignedCells based on Integer32"""
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


_E1IdleUnassignedCells_Type.__name__ = "Integer32"
_E1IdleUnassignedCells_Object = MibTableColumn
e1IdleUnassignedCells = _E1IdleUnassignedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 11),
    _E1IdleUnassignedCells_Type()
)
e1IdleUnassignedCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1IdleUnassignedCells.setStatus("current")


class _E1LineLength_Type(Integer32):
    """Custom type e1LineLength based on Integer32"""
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
        *(("e1Line110-220", 2),
          ("e1Line110-220Alt", 10),
          ("e1Line220-330", 3),
          ("e1Line220-330Alt", 11),
          ("e1Line330-440", 4),
          ("e1Line330-440Alt", 12),
          ("e1Line440-550", 5),
          ("e1Line440-550Alt", 13),
          ("e1Line550-660", 6),
          ("e1Line550-660Alt", 14),
          ("e1LineG703-120", 8),
          ("e1LineG703-120Alt", 16),
          ("e1LineG703-75", 7),
          ("e1LineG703-75Alt", 15),
          ("e1LineLt110", 1),
          ("e1LineLt110Alt", 9))
    )


_E1LineLength_Type.__name__ = "Integer32"
_E1LineLength_Object = MibTableColumn
e1LineLength = _E1LineLength_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 12),
    _E1LineLength_Type()
)
e1LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1LineLength.setStatus("current")


class _E1LineTypeFraming_Type(Integer32):
    """Custom type e1LineTypeFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1Hcs", 2),
          ("e1Plcp", 3),
          ("other", 1))
    )


_E1LineTypeFraming_Type.__name__ = "Integer32"
_E1LineTypeFraming_Object = MibTableColumn
e1LineTypeFraming = _E1LineTypeFraming_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 13),
    _E1LineTypeFraming_Type()
)
e1LineTypeFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1LineTypeFraming.setStatus("current")


class _E1RxScrambling_Type(Integer32):
    """Custom type e1RxScrambling based on Integer32"""
    defaultValue = 1

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


_E1RxScrambling_Type.__name__ = "Integer32"
_E1RxScrambling_Object = MibTableColumn
e1RxScrambling = _E1RxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 14),
    _E1RxScrambling_Type()
)
e1RxScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1RxScrambling.setStatus("current")


class _E1TxScrambling_Type(Integer32):
    """Custom type e1TxScrambling based on Integer32"""
    defaultValue = 1

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


_E1TxScrambling_Type.__name__ = "Integer32"
_E1TxScrambling_Object = MibTableColumn
e1TxScrambling = _E1TxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 1, 1, 1, 15),
    _E1TxScrambling_Type()
)
e1TxScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1TxScrambling.setStatus("current")
_E1StatsGroup_ObjectIdentity = ObjectIdentity
e1StatsGroup = _E1StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2)
)
_E1FramingTable_Object = MibTable
e1FramingTable = _E1FramingTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    e1FramingTable.setStatus("current")
_E1FramingEntry_Object = MibTableRow
e1FramingEntry = _E1FramingEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1, 1)
)
e1FramingEntry.setIndexNames(
    (0, "Fore-E1-MIB", "e1FramingBoard"),
    (0, "Fore-E1-MIB", "e1FramingModule"),
    (0, "Fore-E1-MIB", "e1FramingPort"),
)
if mibBuilder.loadTexts:
    e1FramingEntry.setStatus("current")
_E1FramingBoard_Type = Integer32
_E1FramingBoard_Object = MibTableColumn
e1FramingBoard = _E1FramingBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1, 1, 1),
    _E1FramingBoard_Type()
)
e1FramingBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FramingBoard.setStatus("current")
_E1FramingModule_Type = Integer32
_E1FramingModule_Object = MibTableColumn
e1FramingModule = _E1FramingModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1, 1, 2),
    _E1FramingModule_Type()
)
e1FramingModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FramingModule.setStatus("current")
_E1FramingPort_Type = Integer32
_E1FramingPort_Object = MibTableColumn
e1FramingPort = _E1FramingPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1, 1, 3),
    _E1FramingPort_Type()
)
e1FramingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FramingPort.setStatus("current")
_E1FramingLCVs_Type = Counter32
_E1FramingLCVs_Object = MibTableColumn
e1FramingLCVs = _E1FramingLCVs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1, 1, 4),
    _E1FramingLCVs_Type()
)
e1FramingLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FramingLCVs.setStatus("current")
_E1FramingFERRs_Type = Counter32
_E1FramingFERRs_Object = MibTableColumn
e1FramingFERRs = _E1FramingFERRs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1, 1, 5),
    _E1FramingFERRs_Type()
)
e1FramingFERRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FramingFERRs.setStatus("current")
_E1FramingFEBEs_Type = Counter32
_E1FramingFEBEs_Object = MibTableColumn
e1FramingFEBEs = _E1FramingFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1, 1, 6),
    _E1FramingFEBEs_Type()
)
e1FramingFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FramingFEBEs.setStatus("current")
_E1FramingCRCs_Type = Counter32
_E1FramingCRCs_Object = MibTableColumn
e1FramingCRCs = _E1FramingCRCs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1, 1, 7),
    _E1FramingCRCs_Type()
)
e1FramingCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FramingCRCs.setStatus("current")
_E1FramingOOFs_Type = Counter32
_E1FramingOOFs_Object = MibTableColumn
e1FramingOOFs = _E1FramingOOFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1, 1, 8),
    _E1FramingOOFs_Type()
)
e1FramingOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FramingOOFs.setStatus("current")
_E1FramingLOSs_Type = Counter32
_E1FramingLOSs_Object = MibTableColumn
e1FramingLOSs = _E1FramingLOSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1, 1, 9),
    _E1FramingLOSs_Type()
)
e1FramingLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FramingLOSs.setStatus("current")
_E1FramingAISs_Type = Counter32
_E1FramingAISs_Object = MibTableColumn
e1FramingAISs = _E1FramingAISs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1, 1, 10),
    _E1FramingAISs_Type()
)
e1FramingAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FramingAISs.setStatus("current")
_E1FramingAISDs_Type = Counter32
_E1FramingAISDs_Object = MibTableColumn
e1FramingAISDs = _E1FramingAISDs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1, 1, 11),
    _E1FramingAISDs_Type()
)
e1FramingAISDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FramingAISDs.setStatus("current")
_E1FramingRedAlarms_Type = Counter32
_E1FramingRedAlarms_Object = MibTableColumn
e1FramingRedAlarms = _E1FramingRedAlarms_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1, 1, 12),
    _E1FramingRedAlarms_Type()
)
e1FramingRedAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FramingRedAlarms.setStatus("current")
_E1FramingYellowAlarms_Type = Counter32
_E1FramingYellowAlarms_Object = MibTableColumn
e1FramingYellowAlarms = _E1FramingYellowAlarms_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 1, 1, 13),
    _E1FramingYellowAlarms_Type()
)
e1FramingYellowAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1FramingYellowAlarms.setStatus("current")
_E1PlcpTable_Object = MibTable
e1PlcpTable = _E1PlcpTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    e1PlcpTable.setStatus("current")
_E1PlcpEntry_Object = MibTableRow
e1PlcpEntry = _E1PlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 2, 1)
)
e1PlcpEntry.setIndexNames(
    (0, "Fore-E1-MIB", "e1PlcpBoard"),
    (0, "Fore-E1-MIB", "e1PlcpModule"),
    (0, "Fore-E1-MIB", "e1PlcpPort"),
)
if mibBuilder.loadTexts:
    e1PlcpEntry.setStatus("current")
_E1PlcpBoard_Type = Integer32
_E1PlcpBoard_Object = MibTableColumn
e1PlcpBoard = _E1PlcpBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 2, 1, 1),
    _E1PlcpBoard_Type()
)
e1PlcpBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1PlcpBoard.setStatus("current")
_E1PlcpModule_Type = Integer32
_E1PlcpModule_Object = MibTableColumn
e1PlcpModule = _E1PlcpModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 2, 1, 2),
    _E1PlcpModule_Type()
)
e1PlcpModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1PlcpModule.setStatus("current")
_E1PlcpPort_Type = Integer32
_E1PlcpPort_Object = MibTableColumn
e1PlcpPort = _E1PlcpPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 2, 1, 3),
    _E1PlcpPort_Type()
)
e1PlcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1PlcpPort.setStatus("current")
_E1PlcpBIP8s_Type = Counter32
_E1PlcpBIP8s_Object = MibTableColumn
e1PlcpBIP8s = _E1PlcpBIP8s_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 2, 1, 4),
    _E1PlcpBIP8s_Type()
)
e1PlcpBIP8s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1PlcpBIP8s.setStatus("current")
_E1PlcpFERRs_Type = Counter32
_E1PlcpFERRs_Object = MibTableColumn
e1PlcpFERRs = _E1PlcpFERRs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 2, 1, 5),
    _E1PlcpFERRs_Type()
)
e1PlcpFERRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1PlcpFERRs.setStatus("current")
_E1PlcpFEBEs_Type = Counter32
_E1PlcpFEBEs_Object = MibTableColumn
e1PlcpFEBEs = _E1PlcpFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 2, 1, 6),
    _E1PlcpFEBEs_Type()
)
e1PlcpFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1PlcpFEBEs.setStatus("current")
_E1PlcpLOFs_Type = Counter32
_E1PlcpLOFs_Object = MibTableColumn
e1PlcpLOFs = _E1PlcpLOFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 2, 1, 7),
    _E1PlcpLOFs_Type()
)
e1PlcpLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1PlcpLOFs.setStatus("current")
_E1PlcpYellows_Type = Counter32
_E1PlcpYellows_Object = MibTableColumn
e1PlcpYellows = _E1PlcpYellows_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 2, 1, 8),
    _E1PlcpYellows_Type()
)
e1PlcpYellows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1PlcpYellows.setStatus("current")
_E1AtmTable_Object = MibTable
e1AtmTable = _E1AtmTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 3)
)
if mibBuilder.loadTexts:
    e1AtmTable.setStatus("current")
_E1AtmEntry_Object = MibTableRow
e1AtmEntry = _E1AtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 3, 1)
)
e1AtmEntry.setIndexNames(
    (0, "Fore-E1-MIB", "e1AtmBoard"),
    (0, "Fore-E1-MIB", "e1AtmModule"),
    (0, "Fore-E1-MIB", "e1AtmPort"),
)
if mibBuilder.loadTexts:
    e1AtmEntry.setStatus("current")
_E1AtmBoard_Type = Integer32
_E1AtmBoard_Object = MibTableColumn
e1AtmBoard = _E1AtmBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 3, 1, 1),
    _E1AtmBoard_Type()
)
e1AtmBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1AtmBoard.setStatus("current")
_E1AtmModule_Type = Integer32
_E1AtmModule_Object = MibTableColumn
e1AtmModule = _E1AtmModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 3, 1, 2),
    _E1AtmModule_Type()
)
e1AtmModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1AtmModule.setStatus("current")
_E1AtmPort_Type = Integer32
_E1AtmPort_Object = MibTableColumn
e1AtmPort = _E1AtmPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 3, 1, 3),
    _E1AtmPort_Type()
)
e1AtmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1AtmPort.setStatus("current")
_E1AtmHCSs_Type = Counter32
_E1AtmHCSs_Object = MibTableColumn
e1AtmHCSs = _E1AtmHCSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 3, 1, 4),
    _E1AtmHCSs_Type()
)
e1AtmHCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1AtmHCSs.setStatus("current")
_E1AtmRxCells_Type = Counter32
_E1AtmRxCells_Object = MibTableColumn
e1AtmRxCells = _E1AtmRxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 3, 1, 5),
    _E1AtmRxCells_Type()
)
e1AtmRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1AtmRxCells.setStatus("current")
_E1AtmTxCells_Type = Counter32
_E1AtmTxCells_Object = MibTableColumn
e1AtmTxCells = _E1AtmTxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 3, 1, 6),
    _E1AtmTxCells_Type()
)
e1AtmTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1AtmTxCells.setStatus("current")
_E1AtmUHCSs_Type = Counter32
_E1AtmUHCSs_Object = MibTableColumn
e1AtmUHCSs = _E1AtmUHCSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 3, 1, 7),
    _E1AtmUHCSs_Type()
)
e1AtmUHCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1AtmUHCSs.setStatus("current")
_E1AtmCHCSs_Type = Counter32
_E1AtmCHCSs_Object = MibTableColumn
e1AtmCHCSs = _E1AtmCHCSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 3, 1, 8),
    _E1AtmCHCSs_Type()
)
e1AtmCHCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1AtmCHCSs.setStatus("current")
_E1AtmLCDs_Type = Counter32
_E1AtmLCDs_Object = MibTableColumn
e1AtmLCDs = _E1AtmLCDs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 8, 2, 3, 1, 9),
    _E1AtmLCDs_Type()
)
e1AtmLCDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1AtmLCDs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-E1-MIB",
    **{"foreE1": foreE1,
       "e1ConfGroup": e1ConfGroup,
       "e1ConfTable": e1ConfTable,
       "e1ConfEntry": e1ConfEntry,
       "e1ConfBoard": e1ConfBoard,
       "e1ConfModule": e1ConfModule,
       "e1ConfPort": e1ConfPort,
       "e1LineType": e1LineType,
       "e1LineCoding": e1LineCoding,
       "e1SendCode": e1SendCode,
       "e1ReceiveCode": e1ReceiveCode,
       "e1LoopbackConfig": e1LoopbackConfig,
       "e1TxClockSource": e1TxClockSource,
       "e1LineStatus": e1LineStatus,
       "e1IdleUnassignedCells": e1IdleUnassignedCells,
       "e1LineLength": e1LineLength,
       "e1LineTypeFraming": e1LineTypeFraming,
       "e1RxScrambling": e1RxScrambling,
       "e1TxScrambling": e1TxScrambling,
       "e1StatsGroup": e1StatsGroup,
       "e1FramingTable": e1FramingTable,
       "e1FramingEntry": e1FramingEntry,
       "e1FramingBoard": e1FramingBoard,
       "e1FramingModule": e1FramingModule,
       "e1FramingPort": e1FramingPort,
       "e1FramingLCVs": e1FramingLCVs,
       "e1FramingFERRs": e1FramingFERRs,
       "e1FramingFEBEs": e1FramingFEBEs,
       "e1FramingCRCs": e1FramingCRCs,
       "e1FramingOOFs": e1FramingOOFs,
       "e1FramingLOSs": e1FramingLOSs,
       "e1FramingAISs": e1FramingAISs,
       "e1FramingAISDs": e1FramingAISDs,
       "e1FramingRedAlarms": e1FramingRedAlarms,
       "e1FramingYellowAlarms": e1FramingYellowAlarms,
       "e1PlcpTable": e1PlcpTable,
       "e1PlcpEntry": e1PlcpEntry,
       "e1PlcpBoard": e1PlcpBoard,
       "e1PlcpModule": e1PlcpModule,
       "e1PlcpPort": e1PlcpPort,
       "e1PlcpBIP8s": e1PlcpBIP8s,
       "e1PlcpFERRs": e1PlcpFERRs,
       "e1PlcpFEBEs": e1PlcpFEBEs,
       "e1PlcpLOFs": e1PlcpLOFs,
       "e1PlcpYellows": e1PlcpYellows,
       "e1AtmTable": e1AtmTable,
       "e1AtmEntry": e1AtmEntry,
       "e1AtmBoard": e1AtmBoard,
       "e1AtmModule": e1AtmModule,
       "e1AtmPort": e1AtmPort,
       "e1AtmHCSs": e1AtmHCSs,
       "e1AtmRxCells": e1AtmRxCells,
       "e1AtmTxCells": e1AtmTxCells,
       "e1AtmUHCSs": e1AtmUHCSs,
       "e1AtmCHCSs": e1AtmCHCSs,
       "e1AtmLCDs": e1AtmLCDs}
)
