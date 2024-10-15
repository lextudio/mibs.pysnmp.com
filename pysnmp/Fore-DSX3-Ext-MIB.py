# SNMP MIB module (Fore-DSX3-Ext-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-DSX3-Ext-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:56 2024
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

(dsx3LineIndex,) = mibBuilder.importSymbols(
    "DS3-MIB",
    "dsx3LineIndex")

(asx,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "asx")

(trapLogIndex,) = mibBuilder.importSymbols(
    "Fore-TrapLog-MIB",
    "trapLogIndex")

(ifName,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifName")

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

foreDsx3Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ForeDsx3ConfigTable_Object = MibTable
foreDsx3ConfigTable = _ForeDsx3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    foreDsx3ConfigTable.setStatus("current")
_ForeDsx3ConfigEntry_Object = MibTableRow
foreDsx3ConfigEntry = _ForeDsx3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1)
)
foreDsx3ConfigEntry.setIndexNames(
    (0, "DS3-MIB", "dsx3LineIndex"),
)
if mibBuilder.loadTexts:
    foreDsx3ConfigEntry.setStatus("current")


class _ForeDsx3ConfigReceiveCode_Type(Integer32):
    """Custom type foreDsx3ConfigReceiveCode based on Integer32"""
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


_ForeDsx3ConfigReceiveCode_Type.__name__ = "Integer32"
_ForeDsx3ConfigReceiveCode_Object = MibTableColumn
foreDsx3ConfigReceiveCode = _ForeDsx3ConfigReceiveCode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 1),
    _ForeDsx3ConfigReceiveCode_Type()
)
foreDsx3ConfigReceiveCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3ConfigReceiveCode.setStatus("current")


class _ForeDsx3ConfigLineLength_Type(Integer32):
    """Custom type foreDsx3ConfigLineLength based on Integer32"""
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


_ForeDsx3ConfigLineLength_Type.__name__ = "Integer32"
_ForeDsx3ConfigLineLength_Object = MibTableColumn
foreDsx3ConfigLineLength = _ForeDsx3ConfigLineLength_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 2),
    _ForeDsx3ConfigLineLength_Type()
)
foreDsx3ConfigLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreDsx3ConfigLineLength.setStatus("current")


class _ForeDsx3ConfigStatus_Type(Integer32):
    """Custom type foreDsx3ConfigStatus based on Integer32"""
    defaultValue = 1


_ForeDsx3ConfigStatus_Object = MibTableColumn
foreDsx3ConfigStatus = _ForeDsx3ConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 3),
    _ForeDsx3ConfigStatus_Type()
)
foreDsx3ConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3ConfigStatus.setStatus("current")


class _ForeDsx3LineTypeFraming_Type(Integer32):
    """Custom type foreDsx3LineTypeFraming based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e3G751", 1),
          ("e3G832", 2))
    )


_ForeDsx3LineTypeFraming_Type.__name__ = "Integer32"
_ForeDsx3LineTypeFraming_Object = MibTableColumn
foreDsx3LineTypeFraming = _ForeDsx3LineTypeFraming_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 4),
    _ForeDsx3LineTypeFraming_Type()
)
foreDsx3LineTypeFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3LineTypeFraming.setStatus("current")


class _ForeDsx3PbitPerrThrSeconds_Type(Integer32):
    """Custom type foreDsx3PbitPerrThrSeconds based on Integer32"""
    defaultValue = 10


_ForeDsx3PbitPerrThrSeconds_Object = MibTableColumn
foreDsx3PbitPerrThrSeconds = _ForeDsx3PbitPerrThrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 5),
    _ForeDsx3PbitPerrThrSeconds_Type()
)
foreDsx3PbitPerrThrSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreDsx3PbitPerrThrSeconds.setStatus("current")
_ForeDsx3PbitPerrThrErrors_Type = Integer32
_ForeDsx3PbitPerrThrErrors_Object = MibTableColumn
foreDsx3PbitPerrThrErrors = _ForeDsx3PbitPerrThrErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 6),
    _ForeDsx3PbitPerrThrErrors_Type()
)
foreDsx3PbitPerrThrErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreDsx3PbitPerrThrErrors.setStatus("current")


class _ForeDsx3PbitPerrFailEnable_Type(Integer32):
    """Custom type foreDsx3PbitPerrFailEnable based on Integer32"""
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


_ForeDsx3PbitPerrFailEnable_Type.__name__ = "Integer32"
_ForeDsx3PbitPerrFailEnable_Object = MibTableColumn
foreDsx3PbitPerrFailEnable = _ForeDsx3PbitPerrFailEnable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 7),
    _ForeDsx3PbitPerrFailEnable_Type()
)
foreDsx3PbitPerrFailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreDsx3PbitPerrFailEnable.setStatus("current")
_ForeDsx3SignalDegradeBer_Type = Integer32
_ForeDsx3SignalDegradeBer_Object = MibTableColumn
foreDsx3SignalDegradeBer = _ForeDsx3SignalDegradeBer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 8),
    _ForeDsx3SignalDegradeBer_Type()
)
foreDsx3SignalDegradeBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreDsx3SignalDegradeBer.setStatus("current")
_ForeDsx3SignalFailBer_Type = Integer32
_ForeDsx3SignalFailBer_Object = MibTableColumn
foreDsx3SignalFailBer = _ForeDsx3SignalFailBer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 9),
    _ForeDsx3SignalFailBer_Type()
)
foreDsx3SignalFailBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreDsx3SignalFailBer.setStatus("current")


class _ForeDsx3BerErrorModel_Type(Integer32):
    """Custom type foreDsx3BerErrorModel based on Integer32"""
    defaultValue = 1

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


_ForeDsx3BerErrorModel_Type.__name__ = "Integer32"
_ForeDsx3BerErrorModel_Object = MibTableColumn
foreDsx3BerErrorModel = _ForeDsx3BerErrorModel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 10),
    _ForeDsx3BerErrorModel_Type()
)
foreDsx3BerErrorModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreDsx3BerErrorModel.setStatus("current")


class _ForeDsx3BerState_Type(Integer32):
    """Custom type foreDsx3BerState based on Integer32"""
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


_ForeDsx3BerState_Type.__name__ = "Integer32"
_ForeDsx3BerState_Object = MibTableColumn
foreDsx3BerState = _ForeDsx3BerState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 11),
    _ForeDsx3BerState_Type()
)
foreDsx3BerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3BerState.setStatus("current")
_ForeDsx3TotalTable_Object = MibTable
foreDsx3TotalTable = _ForeDsx3TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2)
)
if mibBuilder.loadTexts:
    foreDsx3TotalTable.setStatus("current")
_ForeDsx3TotalEntry_Object = MibTableRow
foreDsx3TotalEntry = _ForeDsx3TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1)
)
foreDsx3TotalEntry.setIndexNames(
    (0, "DS3-MIB", "dsx3LineIndex"),
)
if mibBuilder.loadTexts:
    foreDsx3TotalEntry.setStatus("current")
_ForeDsx3TotalFramingLOSs_Type = Counter32
_ForeDsx3TotalFramingLOSs_Object = MibTableColumn
foreDsx3TotalFramingLOSs = _ForeDsx3TotalFramingLOSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 1),
    _ForeDsx3TotalFramingLOSs_Type()
)
foreDsx3TotalFramingLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3TotalFramingLOSs.setStatus("current")
_ForeDsx3TotalFramingLCVs_Type = Counter32
_ForeDsx3TotalFramingLCVs_Object = MibTableColumn
foreDsx3TotalFramingLCVs = _ForeDsx3TotalFramingLCVs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 2),
    _ForeDsx3TotalFramingLCVs_Type()
)
foreDsx3TotalFramingLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3TotalFramingLCVs.setStatus("current")
_ForeDsx3TotalFramingSumLCVs_Type = Counter32
_ForeDsx3TotalFramingSumLCVs_Object = MibTableColumn
foreDsx3TotalFramingSumLCVs = _ForeDsx3TotalFramingSumLCVs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 3),
    _ForeDsx3TotalFramingSumLCVs_Type()
)
foreDsx3TotalFramingSumLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3TotalFramingSumLCVs.setStatus("current")
_ForeDsx3TotalFramingFERRs_Type = Counter32
_ForeDsx3TotalFramingFERRs_Object = MibTableColumn
foreDsx3TotalFramingFERRs = _ForeDsx3TotalFramingFERRs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 4),
    _ForeDsx3TotalFramingFERRs_Type()
)
foreDsx3TotalFramingFERRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3TotalFramingFERRs.setStatus("current")
_ForeDsx3TotalFramingOOFs_Type = Counter32
_ForeDsx3TotalFramingOOFs_Object = MibTableColumn
foreDsx3TotalFramingOOFs = _ForeDsx3TotalFramingOOFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 5),
    _ForeDsx3TotalFramingOOFs_Type()
)
foreDsx3TotalFramingOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3TotalFramingOOFs.setStatus("current")
_ForeDsx3TotalFramingFERFs_Type = Counter32
_ForeDsx3TotalFramingFERFs_Object = MibTableColumn
foreDsx3TotalFramingFERFs = _ForeDsx3TotalFramingFERFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 6),
    _ForeDsx3TotalFramingFERFs_Type()
)
foreDsx3TotalFramingFERFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3TotalFramingFERFs.setStatus("current")
_ForeDsx3TotalFramingAISs_Type = Counter32
_ForeDsx3TotalFramingAISs_Object = MibTableColumn
foreDsx3TotalFramingAISs = _ForeDsx3TotalFramingAISs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 7),
    _ForeDsx3TotalFramingAISs_Type()
)
foreDsx3TotalFramingAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3TotalFramingAISs.setStatus("current")
_ForeDsx3TotalFramingPbitPERRs_Type = Counter32
_ForeDsx3TotalFramingPbitPERRs_Object = MibTableColumn
foreDsx3TotalFramingPbitPERRs = _ForeDsx3TotalFramingPbitPERRs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 8),
    _ForeDsx3TotalFramingPbitPERRs_Type()
)
foreDsx3TotalFramingPbitPERRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3TotalFramingPbitPERRs.setStatus("current")
_ForeDsx3TotalFramingCbitPERRs_Type = Counter32
_ForeDsx3TotalFramingCbitPERRs_Object = MibTableColumn
foreDsx3TotalFramingCbitPERRs = _ForeDsx3TotalFramingCbitPERRs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 9),
    _ForeDsx3TotalFramingCbitPERRs_Type()
)
foreDsx3TotalFramingCbitPERRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3TotalFramingCbitPERRs.setStatus("current")
_ForeDsx3TotalFramingFEBEs_Type = Counter32
_ForeDsx3TotalFramingFEBEs_Object = MibTableColumn
foreDsx3TotalFramingFEBEs = _ForeDsx3TotalFramingFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 10),
    _ForeDsx3TotalFramingFEBEs_Type()
)
foreDsx3TotalFramingFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3TotalFramingFEBEs.setStatus("current")
_ForeDsx3TotalFramingIDLEs_Type = Counter32
_ForeDsx3TotalFramingIDLEs_Object = MibTableColumn
foreDsx3TotalFramingIDLEs = _ForeDsx3TotalFramingIDLEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 11),
    _ForeDsx3TotalFramingIDLEs_Type()
)
foreDsx3TotalFramingIDLEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreDsx3TotalFramingIDLEs.setStatus("current")

# Managed Objects groups


# Notification objects

foreDsx3LOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 1)
)
foreDsx3LOFDetected.setObjects(
      *(("DS3-MIB", "dsx3LineIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreDsx3LOFDetected.setStatus(
        "current"
    )

foreDsx3LOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 2)
)
foreDsx3LOFCleared.setObjects(
      *(("DS3-MIB", "dsx3LineIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreDsx3LOFCleared.setStatus(
        "current"
    )

foreDsx3AISDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 3)
)
foreDsx3AISDetected.setObjects(
      *(("DS3-MIB", "dsx3LineIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreDsx3AISDetected.setStatus(
        "current"
    )

foreDsx3AISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 4)
)
foreDsx3AISCleared.setObjects(
      *(("DS3-MIB", "dsx3LineIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreDsx3AISCleared.setStatus(
        "current"
    )

foreDsx3FERFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 5)
)
foreDsx3FERFDetected.setObjects(
      *(("DS3-MIB", "dsx3LineIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreDsx3FERFDetected.setStatus(
        "current"
    )

foreDsx3FERFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 6)
)
foreDsx3FERFCleared.setObjects(
      *(("DS3-MIB", "dsx3LineIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreDsx3FERFCleared.setStatus(
        "current"
    )

foreDsx3LOSDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 7)
)
foreDsx3LOSDetected.setObjects(
      *(("DS3-MIB", "dsx3LineIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreDsx3LOSDetected.setStatus(
        "current"
    )

foreDsx3LOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 8)
)
foreDsx3LOSCleared.setObjects(
      *(("DS3-MIB", "dsx3LineIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreDsx3LOSCleared.setStatus(
        "current"
    )

foreDsx3IdleDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 9)
)
foreDsx3IdleDetected.setObjects(
      *(("DS3-MIB", "dsx3LineIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreDsx3IdleDetected.setStatus(
        "current"
    )

foreDsx3IdleCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 10)
)
foreDsx3IdleCleared.setObjects(
      *(("DS3-MIB", "dsx3LineIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreDsx3IdleCleared.setStatus(
        "current"
    )

foreDsx3TrailChangeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 11)
)
foreDsx3TrailChangeDetected.setObjects(
      *(("DS3-MIB", "dsx3LineIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreDsx3TrailChangeDetected.setStatus(
        "current"
    )

foreDsx3PbitPerrDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 12)
)
foreDsx3PbitPerrDetected.setObjects(
      *(("DS3-MIB", "dsx3LineIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreDsx3PbitPerrDetected.setStatus(
        "current"
    )

foreDsx3PbitPerrCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 13)
)
foreDsx3PbitPerrCleared.setObjects(
      *(("DS3-MIB", "dsx3LineIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreDsx3PbitPerrCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-DSX3-Ext-MIB",
    **{"foreDsx3Mib": foreDsx3Mib,
       "foreDsx3LOFDetected": foreDsx3LOFDetected,
       "foreDsx3LOFCleared": foreDsx3LOFCleared,
       "foreDsx3AISDetected": foreDsx3AISDetected,
       "foreDsx3AISCleared": foreDsx3AISCleared,
       "foreDsx3FERFDetected": foreDsx3FERFDetected,
       "foreDsx3FERFCleared": foreDsx3FERFCleared,
       "foreDsx3LOSDetected": foreDsx3LOSDetected,
       "foreDsx3LOSCleared": foreDsx3LOSCleared,
       "foreDsx3IdleDetected": foreDsx3IdleDetected,
       "foreDsx3IdleCleared": foreDsx3IdleCleared,
       "foreDsx3TrailChangeDetected": foreDsx3TrailChangeDetected,
       "foreDsx3PbitPerrDetected": foreDsx3PbitPerrDetected,
       "foreDsx3PbitPerrCleared": foreDsx3PbitPerrCleared,
       "foreDsx3ConfigTable": foreDsx3ConfigTable,
       "foreDsx3ConfigEntry": foreDsx3ConfigEntry,
       "foreDsx3ConfigReceiveCode": foreDsx3ConfigReceiveCode,
       "foreDsx3ConfigLineLength": foreDsx3ConfigLineLength,
       "foreDsx3ConfigStatus": foreDsx3ConfigStatus,
       "foreDsx3LineTypeFraming": foreDsx3LineTypeFraming,
       "foreDsx3PbitPerrThrSeconds": foreDsx3PbitPerrThrSeconds,
       "foreDsx3PbitPerrThrErrors": foreDsx3PbitPerrThrErrors,
       "foreDsx3PbitPerrFailEnable": foreDsx3PbitPerrFailEnable,
       "foreDsx3SignalDegradeBer": foreDsx3SignalDegradeBer,
       "foreDsx3SignalFailBer": foreDsx3SignalFailBer,
       "foreDsx3BerErrorModel": foreDsx3BerErrorModel,
       "foreDsx3BerState": foreDsx3BerState,
       "foreDsx3TotalTable": foreDsx3TotalTable,
       "foreDsx3TotalEntry": foreDsx3TotalEntry,
       "foreDsx3TotalFramingLOSs": foreDsx3TotalFramingLOSs,
       "foreDsx3TotalFramingLCVs": foreDsx3TotalFramingLCVs,
       "foreDsx3TotalFramingSumLCVs": foreDsx3TotalFramingSumLCVs,
       "foreDsx3TotalFramingFERRs": foreDsx3TotalFramingFERRs,
       "foreDsx3TotalFramingOOFs": foreDsx3TotalFramingOOFs,
       "foreDsx3TotalFramingFERFs": foreDsx3TotalFramingFERFs,
       "foreDsx3TotalFramingAISs": foreDsx3TotalFramingAISs,
       "foreDsx3TotalFramingPbitPERRs": foreDsx3TotalFramingPbitPERRs,
       "foreDsx3TotalFramingCbitPERRs": foreDsx3TotalFramingCbitPERRs,
       "foreDsx3TotalFramingFEBEs": foreDsx3TotalFramingFEBEs,
       "foreDsx3TotalFramingIDLEs": foreDsx3TotalFramingIDLEs}
)
