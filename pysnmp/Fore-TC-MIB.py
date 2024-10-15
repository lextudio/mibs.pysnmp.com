# SNMP MIB module (Fore-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:18 2024
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

(trapLogIndex,) = mibBuilder.importSymbols(
    "Fore-TrapLog-MIB",
    "trapLogIndex")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
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

foreTcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ForeTcConfigTable_Object = MibTable
foreTcConfigTable = _ForeTcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    foreTcConfigTable.setStatus("current")
_ForeTcConfigEntry_Object = MibTableRow
foreTcConfigEntry = _ForeTcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 1, 1)
)
foreTcConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreTcConfigEntry.setStatus("current")


class _ForeTcConfigCellScrambling_Type(Integer32):
    """Custom type foreTcConfigCellScrambling based on Integer32"""
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


_ForeTcConfigCellScrambling_Type.__name__ = "Integer32"
_ForeTcConfigCellScrambling_Object = MibTableColumn
foreTcConfigCellScrambling = _ForeTcConfigCellScrambling_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 1, 1, 1),
    _ForeTcConfigCellScrambling_Type()
)
foreTcConfigCellScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreTcConfigCellScrambling.setStatus("current")


class _ForeTcConfigEmptyCell_Type(Integer32):
    """Custom type foreTcConfigEmptyCell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("unassigned", 2))
    )


_ForeTcConfigEmptyCell_Type.__name__ = "Integer32"
_ForeTcConfigEmptyCell_Object = MibTableColumn
foreTcConfigEmptyCell = _ForeTcConfigEmptyCell_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 1, 1, 2),
    _ForeTcConfigEmptyCell_Type()
)
foreTcConfigEmptyCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreTcConfigEmptyCell.setStatus("current")


class _ForeTcConfigLoopback_Type(Integer32):
    """Custom type foreTcConfigLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcDiagLoop", 2),
          ("tcNoLoop", 1),
          ("tcPayloadLoop", 3))
    )


_ForeTcConfigLoopback_Type.__name__ = "Integer32"
_ForeTcConfigLoopback_Object = MibTableColumn
foreTcConfigLoopback = _ForeTcConfigLoopback_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 1, 1, 3),
    _ForeTcConfigLoopback_Type()
)
foreTcConfigLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreTcConfigLoopback.setStatus("current")


class _ForeTcConfigFramingMode_Type(Integer32):
    """Custom type foreTcConfigFramingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcFramingDirect", 1),
          ("tcFramingPlcp", 2))
    )


_ForeTcConfigFramingMode_Type.__name__ = "Integer32"
_ForeTcConfigFramingMode_Object = MibTableColumn
foreTcConfigFramingMode = _ForeTcConfigFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 1, 1, 4),
    _ForeTcConfigFramingMode_Type()
)
foreTcConfigFramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreTcConfigFramingMode.setStatus("current")


class _ForeTcConfigStatus_Type(Integer32):
    """Custom type foreTcConfigStatus based on Integer32"""
    defaultValue = 1


_ForeTcConfigStatus_Object = MibTableColumn
foreTcConfigStatus = _ForeTcConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 1, 1, 5),
    _ForeTcConfigStatus_Type()
)
foreTcConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcConfigStatus.setStatus("current")
_ForeTcTotalTable_Object = MibTable
foreTcTotalTable = _ForeTcTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 2)
)
if mibBuilder.loadTexts:
    foreTcTotalTable.setStatus("current")
_ForeTcTotalEntry_Object = MibTableRow
foreTcTotalEntry = _ForeTcTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 2, 1)
)
foreTcTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreTcTotalEntry.setStatus("current")
_ForeTcTotalLcdSeconds_Type = Counter32
_ForeTcTotalLcdSeconds_Object = MibTableColumn
foreTcTotalLcdSeconds = _ForeTcTotalLcdSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 2, 1, 1),
    _ForeTcTotalLcdSeconds_Type()
)
foreTcTotalLcdSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcTotalLcdSeconds.setStatus("current")
_ForeTcTotalCorrectableHcs_Type = Counter32
_ForeTcTotalCorrectableHcs_Object = MibTableColumn
foreTcTotalCorrectableHcs = _ForeTcTotalCorrectableHcs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 2, 1, 2),
    _ForeTcTotalCorrectableHcs_Type()
)
foreTcTotalCorrectableHcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcTotalCorrectableHcs.setStatus("current")
_ForeTcTotalUncorrectableHcs_Type = Counter32
_ForeTcTotalUncorrectableHcs_Object = MibTableColumn
foreTcTotalUncorrectableHcs = _ForeTcTotalUncorrectableHcs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 2, 1, 3),
    _ForeTcTotalUncorrectableHcs_Type()
)
foreTcTotalUncorrectableHcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcTotalUncorrectableHcs.setStatus("current")
_ForeTcTotalTxCells_Type = Counter32
_ForeTcTotalTxCells_Object = MibTableColumn
foreTcTotalTxCells = _ForeTcTotalTxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 2, 1, 4),
    _ForeTcTotalTxCells_Type()
)
foreTcTotalTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcTotalTxCells.setStatus("current")
_ForeTcTotalRxCells_Type = Counter32
_ForeTcTotalRxCells_Object = MibTableColumn
foreTcTotalRxCells = _ForeTcTotalRxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 2, 1, 5),
    _ForeTcTotalRxCells_Type()
)
foreTcTotalRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcTotalRxCells.setStatus("current")
_ForeTcCurrentTable_Object = MibTable
foreTcCurrentTable = _ForeTcCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 4)
)
if mibBuilder.loadTexts:
    foreTcCurrentTable.setStatus("current")
_ForeTcCurrentEntry_Object = MibTableRow
foreTcCurrentEntry = _ForeTcCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 4, 1)
)
foreTcCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreTcCurrentEntry.setStatus("current")
_ForeTcCurrentErrSeconds_Type = Counter32
_ForeTcCurrentErrSeconds_Object = MibTableColumn
foreTcCurrentErrSeconds = _ForeTcCurrentErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 4, 1, 1),
    _ForeTcCurrentErrSeconds_Type()
)
foreTcCurrentErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcCurrentErrSeconds.setStatus("current")
_ForeTcCurrentSevErrSeconds_Type = Counter32
_ForeTcCurrentSevErrSeconds_Object = MibTableColumn
foreTcCurrentSevErrSeconds = _ForeTcCurrentSevErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 4, 1, 2),
    _ForeTcCurrentSevErrSeconds_Type()
)
foreTcCurrentSevErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcCurrentSevErrSeconds.setStatus("current")
_ForeTcCurrentUnavailSeconds_Type = Counter32
_ForeTcCurrentUnavailSeconds_Object = MibTableColumn
foreTcCurrentUnavailSeconds = _ForeTcCurrentUnavailSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 4, 1, 3),
    _ForeTcCurrentUnavailSeconds_Type()
)
foreTcCurrentUnavailSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcCurrentUnavailSeconds.setStatus("current")
_ForeTcCurrentCorrectableHcs_Type = Counter32
_ForeTcCurrentCorrectableHcs_Object = MibTableColumn
foreTcCurrentCorrectableHcs = _ForeTcCurrentCorrectableHcs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 4, 1, 4),
    _ForeTcCurrentCorrectableHcs_Type()
)
foreTcCurrentCorrectableHcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcCurrentCorrectableHcs.setStatus("current")
_ForeTcCurrentUncorrectableHcs_Type = Counter32
_ForeTcCurrentUncorrectableHcs_Object = MibTableColumn
foreTcCurrentUncorrectableHcs = _ForeTcCurrentUncorrectableHcs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 4, 1, 5),
    _ForeTcCurrentUncorrectableHcs_Type()
)
foreTcCurrentUncorrectableHcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcCurrentUncorrectableHcs.setStatus("current")
_ForeTcIntervalTable_Object = MibTable
foreTcIntervalTable = _ForeTcIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5)
)
if mibBuilder.loadTexts:
    foreTcIntervalTable.setStatus("current")
_ForeTcIntervalEntry_Object = MibTableRow
foreTcIntervalEntry = _ForeTcIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5, 1)
)
foreTcIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Fore-TC-MIB", "foreTcInterval"),
)
if mibBuilder.loadTexts:
    foreTcIntervalEntry.setStatus("current")
_ForeTcInterval_Type = Integer32
_ForeTcInterval_Object = MibTableColumn
foreTcInterval = _ForeTcInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5, 1, 1),
    _ForeTcInterval_Type()
)
foreTcInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcInterval.setStatus("current")
_ForeTcIntervalErrSeconds_Type = Counter32
_ForeTcIntervalErrSeconds_Object = MibTableColumn
foreTcIntervalErrSeconds = _ForeTcIntervalErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5, 1, 2),
    _ForeTcIntervalErrSeconds_Type()
)
foreTcIntervalErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcIntervalErrSeconds.setStatus("current")
_ForeTcIntervalSevErrSeconds_Type = Counter32
_ForeTcIntervalSevErrSeconds_Object = MibTableColumn
foreTcIntervalSevErrSeconds = _ForeTcIntervalSevErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5, 1, 3),
    _ForeTcIntervalSevErrSeconds_Type()
)
foreTcIntervalSevErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcIntervalSevErrSeconds.setStatus("current")
_ForeTcIntervalUnavailSeconds_Type = Counter32
_ForeTcIntervalUnavailSeconds_Object = MibTableColumn
foreTcIntervalUnavailSeconds = _ForeTcIntervalUnavailSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5, 1, 4),
    _ForeTcIntervalUnavailSeconds_Type()
)
foreTcIntervalUnavailSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcIntervalUnavailSeconds.setStatus("current")
_ForeTcIntervalCorrectableHcs_Type = Counter32
_ForeTcIntervalCorrectableHcs_Object = MibTableColumn
foreTcIntervalCorrectableHcs = _ForeTcIntervalCorrectableHcs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5, 1, 5),
    _ForeTcIntervalCorrectableHcs_Type()
)
foreTcIntervalCorrectableHcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcIntervalCorrectableHcs.setStatus("current")
_ForeTcIntervalUncorrectableHcs_Type = Counter32
_ForeTcIntervalUncorrectableHcs_Object = MibTableColumn
foreTcIntervalUncorrectableHcs = _ForeTcIntervalUncorrectableHcs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5, 1, 6),
    _ForeTcIntervalUncorrectableHcs_Type()
)
foreTcIntervalUncorrectableHcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreTcIntervalUncorrectableHcs.setStatus("current")

# Managed Objects groups


# Notification objects

foreTcLCDDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 0, 1)
)
foreTcLCDDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreTcLCDDetected.setStatus(
        "current"
    )

foreTcLCDCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 0, 2)
)
foreTcLCDCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreTcLCDCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-TC-MIB",
    **{"foreTcMib": foreTcMib,
       "foreTcLCDDetected": foreTcLCDDetected,
       "foreTcLCDCleared": foreTcLCDCleared,
       "foreTcConfigTable": foreTcConfigTable,
       "foreTcConfigEntry": foreTcConfigEntry,
       "foreTcConfigCellScrambling": foreTcConfigCellScrambling,
       "foreTcConfigEmptyCell": foreTcConfigEmptyCell,
       "foreTcConfigLoopback": foreTcConfigLoopback,
       "foreTcConfigFramingMode": foreTcConfigFramingMode,
       "foreTcConfigStatus": foreTcConfigStatus,
       "foreTcTotalTable": foreTcTotalTable,
       "foreTcTotalEntry": foreTcTotalEntry,
       "foreTcTotalLcdSeconds": foreTcTotalLcdSeconds,
       "foreTcTotalCorrectableHcs": foreTcTotalCorrectableHcs,
       "foreTcTotalUncorrectableHcs": foreTcTotalUncorrectableHcs,
       "foreTcTotalTxCells": foreTcTotalTxCells,
       "foreTcTotalRxCells": foreTcTotalRxCells,
       "foreTcCurrentTable": foreTcCurrentTable,
       "foreTcCurrentEntry": foreTcCurrentEntry,
       "foreTcCurrentErrSeconds": foreTcCurrentErrSeconds,
       "foreTcCurrentSevErrSeconds": foreTcCurrentSevErrSeconds,
       "foreTcCurrentUnavailSeconds": foreTcCurrentUnavailSeconds,
       "foreTcCurrentCorrectableHcs": foreTcCurrentCorrectableHcs,
       "foreTcCurrentUncorrectableHcs": foreTcCurrentUncorrectableHcs,
       "foreTcIntervalTable": foreTcIntervalTable,
       "foreTcIntervalEntry": foreTcIntervalEntry,
       "foreTcInterval": foreTcInterval,
       "foreTcIntervalErrSeconds": foreTcIntervalErrSeconds,
       "foreTcIntervalSevErrSeconds": foreTcIntervalSevErrSeconds,
       "foreTcIntervalUnavailSeconds": foreTcIntervalUnavailSeconds,
       "foreTcIntervalCorrectableHcs": foreTcIntervalCorrectableHcs,
       "foreTcIntervalUncorrectableHcs": foreTcIntervalUncorrectableHcs}
)
