# SNMP MIB module (Fore-E3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-E3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:58 2024
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

foreE3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_E3ConfGroup_ObjectIdentity = ObjectIdentity
e3ConfGroup = _E3ConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1)
)
_E3ConfTable_Object = MibTable
e3ConfTable = _E3ConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    e3ConfTable.setStatus("current")
_E3ConfEntry_Object = MibTableRow
e3ConfEntry = _E3ConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1)
)
e3ConfEntry.setIndexNames(
    (0, "Fore-E3-MIB", "e3ConfBoard"),
    (0, "Fore-E3-MIB", "e3ConfModule"),
    (0, "Fore-E3-MIB", "e3ConfPort"),
)
if mibBuilder.loadTexts:
    e3ConfEntry.setStatus("current")
_E3ConfBoard_Type = Integer32
_E3ConfBoard_Object = MibTableColumn
e3ConfBoard = _E3ConfBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 1),
    _E3ConfBoard_Type()
)
e3ConfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3ConfBoard.setStatus("current")
_E3ConfModule_Type = Integer32
_E3ConfModule_Object = MibTableColumn
e3ConfModule = _E3ConfModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 2),
    _E3ConfModule_Type()
)
e3ConfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3ConfModule.setStatus("current")
_E3ConfPort_Type = Integer32
_E3ConfPort_Object = MibTableColumn
e3ConfPort = _E3ConfPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 3),
    _E3ConfPort_Type()
)
e3ConfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3ConfPort.setStatus("current")


class _E3LineType_Type(Integer32):
    """Custom type e3LineType based on Integer32"""
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
        *(("e3Framed", 2),
          ("e3OtherLineType", 1),
          ("e3Plcp", 3))
    )


_E3LineType_Type.__name__ = "Integer32"
_E3LineType_Object = MibTableColumn
e3LineType = _E3LineType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 4),
    _E3LineType_Type()
)
e3LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3LineType.setStatus("current")


class _E3LineCoding_Type(Integer32):
    """Custom type e3LineCoding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e3HDB3", 2),
          ("e3OtherLineCoding", 1))
    )


_E3LineCoding_Type.__name__ = "Integer32"
_E3LineCoding_Object = MibTableColumn
e3LineCoding = _E3LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 5),
    _E3LineCoding_Type()
)
e3LineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3LineCoding.setStatus("current")


class _E3SendCode_Type(Integer32):
    """Custom type e3SendCode based on Integer32"""
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
        *(("e3SendDS1LoopCode", 5),
          ("e3SendLineCode", 2),
          ("e3SendNoCode", 1),
          ("e3SendPayloadCode", 3),
          ("e3SendResetCode", 4),
          ("e3SendTestPattern", 6))
    )


_E3SendCode_Type.__name__ = "Integer32"
_E3SendCode_Object = MibTableColumn
e3SendCode = _E3SendCode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 6),
    _E3SendCode_Type()
)
e3SendCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3SendCode.setStatus("current")


class _E3ReceiveCode_Type(Integer32):
    """Custom type e3ReceiveCode based on Integer32"""
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
        *(("e3ReceiveDS1LoopCode", 5),
          ("e3ReceiveLineCode", 2),
          ("e3ReceiveNoCode", 1),
          ("e3ReceivePayloadCode", 3),
          ("e3ReceiveResetCode", 4),
          ("e3ReceiveTestPattern", 6))
    )


_E3ReceiveCode_Type.__name__ = "Integer32"
_E3ReceiveCode_Object = MibTableColumn
e3ReceiveCode = _E3ReceiveCode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 7),
    _E3ReceiveCode_Type()
)
e3ReceiveCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3ReceiveCode.setStatus("current")


class _E3LoopbackConfig_Type(Integer32):
    """Custom type e3LoopbackConfig based on Integer32"""
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
        *(("e3CellLoop", 2),
          ("e3DiagLoop", 4),
          ("e3LineLoop", 5),
          ("e3NoLoop", 1),
          ("e3OtherLoop", 6),
          ("e3PayloadLoop", 3))
    )


_E3LoopbackConfig_Type.__name__ = "Integer32"
_E3LoopbackConfig_Object = MibTableColumn
e3LoopbackConfig = _E3LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 8),
    _E3LoopbackConfig_Type()
)
e3LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3LoopbackConfig.setStatus("current")


class _E3TxClockSource_Type(Integer32):
    """Custom type e3TxClockSource based on Integer32"""
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


_E3TxClockSource_Type.__name__ = "Integer32"
_E3TxClockSource_Object = MibTableColumn
e3TxClockSource = _E3TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 9),
    _E3TxClockSource_Type()
)
e3TxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3TxClockSource.setStatus("current")


class _E3RxScrambling_Type(Integer32):
    """Custom type e3RxScrambling based on Integer32"""
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


_E3RxScrambling_Type.__name__ = "Integer32"
_E3RxScrambling_Object = MibTableColumn
e3RxScrambling = _E3RxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 10),
    _E3RxScrambling_Type()
)
e3RxScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3RxScrambling.setStatus("current")


class _E3TxScrambling_Type(Integer32):
    """Custom type e3TxScrambling based on Integer32"""
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


_E3TxScrambling_Type.__name__ = "Integer32"
_E3TxScrambling_Object = MibTableColumn
e3TxScrambling = _E3TxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 11),
    _E3TxScrambling_Type()
)
e3TxScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3TxScrambling.setStatus("current")


class _E3LineStatus_Type(Integer32):
    """Custom type e3LineStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_E3LineStatus_Type.__name__ = "Integer32"
_E3LineStatus_Object = MibTableColumn
e3LineStatus = _E3LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 12),
    _E3LineStatus_Type()
)
e3LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3LineStatus.setStatus("current")


class _E3IdleUnassignedCells_Type(Integer32):
    """Custom type e3IdleUnassignedCells based on Integer32"""
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


_E3IdleUnassignedCells_Type.__name__ = "Integer32"
_E3IdleUnassignedCells_Object = MibTableColumn
e3IdleUnassignedCells = _E3IdleUnassignedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 13),
    _E3IdleUnassignedCells_Type()
)
e3IdleUnassignedCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3IdleUnassignedCells.setStatus("current")
_E3StatsGroup_ObjectIdentity = ObjectIdentity
e3StatsGroup = _E3StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2)
)
_E3FramingTable_Object = MibTable
e3FramingTable = _E3FramingTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    e3FramingTable.setStatus("current")
_E3FramingEntry_Object = MibTableRow
e3FramingEntry = _E3FramingEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1)
)
e3FramingEntry.setIndexNames(
    (0, "Fore-E3-MIB", "e3FramingBoard"),
    (0, "Fore-E3-MIB", "e3FramingModule"),
    (0, "Fore-E3-MIB", "e3FramingPort"),
)
if mibBuilder.loadTexts:
    e3FramingEntry.setStatus("current")
_E3FramingBoard_Type = Integer32
_E3FramingBoard_Object = MibTableColumn
e3FramingBoard = _E3FramingBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 1),
    _E3FramingBoard_Type()
)
e3FramingBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramingBoard.setStatus("current")
_E3FramingModule_Type = Integer32
_E3FramingModule_Object = MibTableColumn
e3FramingModule = _E3FramingModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 2),
    _E3FramingModule_Type()
)
e3FramingModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramingModule.setStatus("current")
_E3FramingPort_Type = Integer32
_E3FramingPort_Object = MibTableColumn
e3FramingPort = _E3FramingPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 3),
    _E3FramingPort_Type()
)
e3FramingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramingPort.setStatus("current")
_E3FramingLOSs_Type = Counter32
_E3FramingLOSs_Object = MibTableColumn
e3FramingLOSs = _E3FramingLOSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 4),
    _E3FramingLOSs_Type()
)
e3FramingLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramingLOSs.setStatus("current")
_E3FramingLCVs_Type = Counter32
_E3FramingLCVs_Object = MibTableColumn
e3FramingLCVs = _E3FramingLCVs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 5),
    _E3FramingLCVs_Type()
)
e3FramingLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramingLCVs.setStatus("current")
_E3FramingFERRs_Type = Counter32
_E3FramingFERRs_Object = MibTableColumn
e3FramingFERRs = _E3FramingFERRs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 6),
    _E3FramingFERRs_Type()
)
e3FramingFERRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramingFERRs.setStatus("current")
_E3FramingOOFs_Type = Counter32
_E3FramingOOFs_Object = MibTableColumn
e3FramingOOFs = _E3FramingOOFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 7),
    _E3FramingOOFs_Type()
)
e3FramingOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramingOOFs.setStatus("current")
_E3FramingFERFs_Type = Counter32
_E3FramingFERFs_Object = MibTableColumn
e3FramingFERFs = _E3FramingFERFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 8),
    _E3FramingFERFs_Type()
)
e3FramingFERFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramingFERFs.setStatus("current")
_E3FramingAISs_Type = Counter32
_E3FramingAISs_Object = MibTableColumn
e3FramingAISs = _E3FramingAISs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 9),
    _E3FramingAISs_Type()
)
e3FramingAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramingAISs.setStatus("current")
_E3FramingBIP8s_Type = Counter32
_E3FramingBIP8s_Object = MibTableColumn
e3FramingBIP8s = _E3FramingBIP8s_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 10),
    _E3FramingBIP8s_Type()
)
e3FramingBIP8s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramingBIP8s.setStatus("current")
_E3FramingFEBEs_Type = Counter32
_E3FramingFEBEs_Object = MibTableColumn
e3FramingFEBEs = _E3FramingFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 11),
    _E3FramingFEBEs_Type()
)
e3FramingFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3FramingFEBEs.setStatus("current")
_E3PlcpTable_Object = MibTable
e3PlcpTable = _E3PlcpTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    e3PlcpTable.setStatus("current")
_E3PlcpEntry_Object = MibTableRow
e3PlcpEntry = _E3PlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1)
)
e3PlcpEntry.setIndexNames(
    (0, "Fore-E3-MIB", "e3PlcpBoard"),
    (0, "Fore-E3-MIB", "e3PlcpModule"),
    (0, "Fore-E3-MIB", "e3PlcpPort"),
)
if mibBuilder.loadTexts:
    e3PlcpEntry.setStatus("current")
_E3PlcpBoard_Type = Integer32
_E3PlcpBoard_Object = MibTableColumn
e3PlcpBoard = _E3PlcpBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 1),
    _E3PlcpBoard_Type()
)
e3PlcpBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3PlcpBoard.setStatus("current")
_E3PlcpModule_Type = Integer32
_E3PlcpModule_Object = MibTableColumn
e3PlcpModule = _E3PlcpModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 2),
    _E3PlcpModule_Type()
)
e3PlcpModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3PlcpModule.setStatus("current")
_E3PlcpPort_Type = Integer32
_E3PlcpPort_Object = MibTableColumn
e3PlcpPort = _E3PlcpPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 3),
    _E3PlcpPort_Type()
)
e3PlcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3PlcpPort.setStatus("current")
_E3PlcpFERRs_Type = Counter32
_E3PlcpFERRs_Object = MibTableColumn
e3PlcpFERRs = _E3PlcpFERRs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 4),
    _E3PlcpFERRs_Type()
)
e3PlcpFERRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3PlcpFERRs.setStatus("current")
_E3PlcpLOFs_Type = Counter32
_E3PlcpLOFs_Object = MibTableColumn
e3PlcpLOFs = _E3PlcpLOFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 5),
    _E3PlcpLOFs_Type()
)
e3PlcpLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3PlcpLOFs.setStatus("current")
_E3PlcpBIP8s_Type = Counter32
_E3PlcpBIP8s_Object = MibTableColumn
e3PlcpBIP8s = _E3PlcpBIP8s_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 6),
    _E3PlcpBIP8s_Type()
)
e3PlcpBIP8s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3PlcpBIP8s.setStatus("current")
_E3PlcpFEBEs_Type = Counter32
_E3PlcpFEBEs_Object = MibTableColumn
e3PlcpFEBEs = _E3PlcpFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 7),
    _E3PlcpFEBEs_Type()
)
e3PlcpFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3PlcpFEBEs.setStatus("current")
_E3PlcpYellows_Type = Counter32
_E3PlcpYellows_Object = MibTableColumn
e3PlcpYellows = _E3PlcpYellows_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 8),
    _E3PlcpYellows_Type()
)
e3PlcpYellows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3PlcpYellows.setStatus("current")
_E3AtmTable_Object = MibTable
e3AtmTable = _E3AtmTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    e3AtmTable.setStatus("current")
_E3AtmEntry_Object = MibTableRow
e3AtmEntry = _E3AtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1)
)
e3AtmEntry.setIndexNames(
    (0, "Fore-E3-MIB", "e3AtmBoard"),
    (0, "Fore-E3-MIB", "e3AtmModule"),
    (0, "Fore-E3-MIB", "e3AtmPort"),
)
if mibBuilder.loadTexts:
    e3AtmEntry.setStatus("current")
_E3AtmBoard_Type = Integer32
_E3AtmBoard_Object = MibTableColumn
e3AtmBoard = _E3AtmBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1, 1),
    _E3AtmBoard_Type()
)
e3AtmBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmBoard.setStatus("current")
_E3AtmModule_Type = Integer32
_E3AtmModule_Object = MibTableColumn
e3AtmModule = _E3AtmModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1, 2),
    _E3AtmModule_Type()
)
e3AtmModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmModule.setStatus("current")
_E3AtmPort_Type = Integer32
_E3AtmPort_Object = MibTableColumn
e3AtmPort = _E3AtmPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1, 3),
    _E3AtmPort_Type()
)
e3AtmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmPort.setStatus("current")
_E3AtmHCSs_Type = Counter32
_E3AtmHCSs_Object = MibTableColumn
e3AtmHCSs = _E3AtmHCSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1, 4),
    _E3AtmHCSs_Type()
)
e3AtmHCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmHCSs.setStatus("current")
_E3AtmRxCells_Type = Counter32
_E3AtmRxCells_Object = MibTableColumn
e3AtmRxCells = _E3AtmRxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1, 5),
    _E3AtmRxCells_Type()
)
e3AtmRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmRxCells.setStatus("current")
_E3AtmTxCells_Type = Counter32
_E3AtmTxCells_Object = MibTableColumn
e3AtmTxCells = _E3AtmTxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1, 6),
    _E3AtmTxCells_Type()
)
e3AtmTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmTxCells.setStatus("current")
_E3AtmLCDs_Type = Counter32
_E3AtmLCDs_Object = MibTableColumn
e3AtmLCDs = _E3AtmLCDs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1, 7),
    _E3AtmLCDs_Type()
)
e3AtmLCDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmLCDs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-E3-MIB",
    **{"foreE3": foreE3,
       "e3ConfGroup": e3ConfGroup,
       "e3ConfTable": e3ConfTable,
       "e3ConfEntry": e3ConfEntry,
       "e3ConfBoard": e3ConfBoard,
       "e3ConfModule": e3ConfModule,
       "e3ConfPort": e3ConfPort,
       "e3LineType": e3LineType,
       "e3LineCoding": e3LineCoding,
       "e3SendCode": e3SendCode,
       "e3ReceiveCode": e3ReceiveCode,
       "e3LoopbackConfig": e3LoopbackConfig,
       "e3TxClockSource": e3TxClockSource,
       "e3RxScrambling": e3RxScrambling,
       "e3TxScrambling": e3TxScrambling,
       "e3LineStatus": e3LineStatus,
       "e3IdleUnassignedCells": e3IdleUnassignedCells,
       "e3StatsGroup": e3StatsGroup,
       "e3FramingTable": e3FramingTable,
       "e3FramingEntry": e3FramingEntry,
       "e3FramingBoard": e3FramingBoard,
       "e3FramingModule": e3FramingModule,
       "e3FramingPort": e3FramingPort,
       "e3FramingLOSs": e3FramingLOSs,
       "e3FramingLCVs": e3FramingLCVs,
       "e3FramingFERRs": e3FramingFERRs,
       "e3FramingOOFs": e3FramingOOFs,
       "e3FramingFERFs": e3FramingFERFs,
       "e3FramingAISs": e3FramingAISs,
       "e3FramingBIP8s": e3FramingBIP8s,
       "e3FramingFEBEs": e3FramingFEBEs,
       "e3PlcpTable": e3PlcpTable,
       "e3PlcpEntry": e3PlcpEntry,
       "e3PlcpBoard": e3PlcpBoard,
       "e3PlcpModule": e3PlcpModule,
       "e3PlcpPort": e3PlcpPort,
       "e3PlcpFERRs": e3PlcpFERRs,
       "e3PlcpLOFs": e3PlcpLOFs,
       "e3PlcpBIP8s": e3PlcpBIP8s,
       "e3PlcpFEBEs": e3PlcpFEBEs,
       "e3PlcpYellows": e3PlcpYellows,
       "e3AtmTable": e3AtmTable,
       "e3AtmEntry": e3AtmEntry,
       "e3AtmBoard": e3AtmBoard,
       "e3AtmModule": e3AtmModule,
       "e3AtmPort": e3AtmPort,
       "e3AtmHCSs": e3AtmHCSs,
       "e3AtmRxCells": e3AtmRxCells,
       "e3AtmTxCells": e3AtmTxCells,
       "e3AtmLCDs": e3AtmLCDs}
)
