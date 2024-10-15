# SNMP MIB module (PAIRGAIN-ATMTC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-ATMTC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:16 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pgAtmTcMIB,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgAtmTcMIB")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

pgatmTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PgatmTcMibObjects_ObjectIdentity = ObjectIdentity
pgatmTcMibObjects = _PgatmTcMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16, 1, 1)
)
_PgatmTcLayerTable_Object = MibTable
pgatmTcLayerTable = _PgatmTcLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pgatmTcLayerTable.setStatus("current")
_PgatmTcLayerEntry_Object = MibTableRow
pgatmTcLayerEntry = _PgatmTcLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16, 1, 1, 1, 1)
)
pgatmTcLayerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgatmTcLayerEntry.setStatus("current")
_PgatmTcTxCellCount_Type = Counter32
_PgatmTcTxCellCount_Object = MibTableColumn
pgatmTcTxCellCount = _PgatmTcTxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16, 1, 1, 1, 1, 1),
    _PgatmTcTxCellCount_Type()
)
pgatmTcTxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgatmTcTxCellCount.setStatus("current")
_PgatmTcRxCellCount_Type = Counter32
_PgatmTcRxCellCount_Object = MibTableColumn
pgatmTcRxCellCount = _PgatmTcRxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16, 1, 1, 1, 1, 2),
    _PgatmTcRxCellCount_Type()
)
pgatmTcRxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgatmTcRxCellCount.setStatus("current")
_PgatmTcNonMatchCount_Type = Counter32
_PgatmTcNonMatchCount_Object = MibTableColumn
pgatmTcNonMatchCount = _PgatmTcNonMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16, 1, 1, 1, 1, 3),
    _PgatmTcNonMatchCount_Type()
)
pgatmTcNonMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgatmTcNonMatchCount.setStatus("current")
_PgatmTcLOCDEventCount_Type = Counter32
_PgatmTcLOCDEventCount_Object = MibTableColumn
pgatmTcLOCDEventCount = _PgatmTcLOCDEventCount_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16, 1, 1, 1, 1, 4),
    _PgatmTcLOCDEventCount_Type()
)
pgatmTcLOCDEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgatmTcLOCDEventCount.setStatus("current")
_PgatmTcCorrHECError_Type = Counter32
_PgatmTcCorrHECError_Object = MibTableColumn
pgatmTcCorrHECError = _PgatmTcCorrHECError_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16, 1, 1, 1, 1, 5),
    _PgatmTcCorrHECError_Type()
)
pgatmTcCorrHECError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgatmTcCorrHECError.setStatus("current")
_PgatmTcUnCorrHECError_Type = Counter32
_PgatmTcUnCorrHECError_Object = MibTableColumn
pgatmTcUnCorrHECError = _PgatmTcUnCorrHECError_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16, 1, 1, 1, 1, 6),
    _PgatmTcUnCorrHECError_Type()
)
pgatmTcUnCorrHECError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgatmTcUnCorrHECError.setStatus("current")


class _PgatmTcLayerMode_Type(Integer32):
    """Custom type pgatmTcLayerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 2),
          ("normal", 1))
    )


_PgatmTcLayerMode_Type.__name__ = "Integer32"
_PgatmTcLayerMode_Object = MibTableColumn
pgatmTcLayerMode = _PgatmTcLayerMode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16, 1, 1, 1, 1, 7),
    _PgatmTcLayerMode_Type()
)
pgatmTcLayerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgatmTcLayerMode.setStatus("current")


class _PgatmTcScramble_Type(Integer32):
    """Custom type pgatmTcScramble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dss", 2),
          ("off", 0),
          ("sss", 1))
    )


_PgatmTcScramble_Type.__name__ = "Integer32"
_PgatmTcScramble_Object = MibTableColumn
pgatmTcScramble = _PgatmTcScramble_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16, 1, 1, 1, 1, 8),
    _PgatmTcScramble_Type()
)
pgatmTcScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgatmTcScramble.setStatus("current")


class _PgatmTcClearStats_Type(Integer32):
    """Custom type pgatmTcClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_PgatmTcClearStats_Type.__name__ = "Integer32"
_PgatmTcClearStats_Object = MibTableColumn
pgatmTcClearStats = _PgatmTcClearStats_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16, 1, 1, 1, 1, 9),
    _PgatmTcClearStats_Type()
)
pgatmTcClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgatmTcClearStats.setStatus("current")
_PgatmTcStatsLastCleared_Type = TimeStamp
_PgatmTcStatsLastCleared_Object = MibTableColumn
pgatmTcStatsLastCleared = _PgatmTcStatsLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 16, 1, 1, 1, 1, 10),
    _PgatmTcStatsLastCleared_Type()
)
pgatmTcStatsLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgatmTcStatsLastCleared.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-ATMTC-MIB",
    **{"pgatmTcMIB": pgatmTcMIB,
       "pgatmTcMibObjects": pgatmTcMibObjects,
       "pgatmTcLayerTable": pgatmTcLayerTable,
       "pgatmTcLayerEntry": pgatmTcLayerEntry,
       "pgatmTcTxCellCount": pgatmTcTxCellCount,
       "pgatmTcRxCellCount": pgatmTcRxCellCount,
       "pgatmTcNonMatchCount": pgatmTcNonMatchCount,
       "pgatmTcLOCDEventCount": pgatmTcLOCDEventCount,
       "pgatmTcCorrHECError": pgatmTcCorrHECError,
       "pgatmTcUnCorrHECError": pgatmTcUnCorrHECError,
       "pgatmTcLayerMode": pgatmTcLayerMode,
       "pgatmTcScramble": pgatmTcScramble,
       "pgatmTcClearStats": pgatmTcClearStats,
       "pgatmTcStatsLastCleared": pgatmTcStatsLastCleared}
)
