# SNMP MIB module (SONOMASYSTEMS-SONOMA-ATM-E1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMASYSTEMS-SONOMA-ATM-E1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:40 2024
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

(sonomaATM,) = mibBuilder.importSymbols(
    "SONOMASYSTEMS-SONOMA-MIB",
    "sonomaATM")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonomaE1ATMAdapterGroup_ObjectIdentity = ObjectIdentity
sonomaE1ATMAdapterGroup = _SonomaE1ATMAdapterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6)
)
_AtmE1ConfGroup_ObjectIdentity = ObjectIdentity
atmE1ConfGroup = _AtmE1ConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 1)
)
_AtmE1ConfPhyTable_Object = MibTable
atmE1ConfPhyTable = _AtmE1ConfPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 1, 1)
)
if mibBuilder.loadTexts:
    atmE1ConfPhyTable.setStatus("mandatory")
_AtmE1ConfPhyEntry_Object = MibTableRow
atmE1ConfPhyEntry = _AtmE1ConfPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 1, 1, 1)
)
atmE1ConfPhyEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-E1-MIB", "atmE1ConfPhysIndex"),
)
if mibBuilder.loadTexts:
    atmE1ConfPhyEntry.setStatus("mandatory")
_AtmE1ConfPhysIndex_Type = Integer32
_AtmE1ConfPhysIndex_Object = MibTableColumn
atmE1ConfPhysIndex = _AtmE1ConfPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 1, 1, 1, 1),
    _AtmE1ConfPhysIndex_Type()
)
atmE1ConfPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE1ConfPhysIndex.setStatus("mandatory")


class _AtmE1ConfLoopback_Type(Integer32):
    """Custom type atmE1ConfLoopback based on Integer32"""
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
        *(("disabled", 1),
          ("external", 3),
          ("internal", 2))
    )


_AtmE1ConfLoopback_Type.__name__ = "Integer32"
_AtmE1ConfLoopback_Object = MibTableColumn
atmE1ConfLoopback = _AtmE1ConfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 1, 1, 1, 2),
    _AtmE1ConfLoopback_Type()
)
atmE1ConfLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE1ConfLoopback.setStatus("mandatory")


class _AtmE1ConfTxClockSelect_Type(Integer32):
    """Custom type atmE1ConfTxClockSelect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("recovered", 2))
    )


_AtmE1ConfTxClockSelect_Type.__name__ = "Integer32"
_AtmE1ConfTxClockSelect_Object = MibTableColumn
atmE1ConfTxClockSelect = _AtmE1ConfTxClockSelect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 1, 1, 1, 3),
    _AtmE1ConfTxClockSelect_Type()
)
atmE1ConfTxClockSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE1ConfTxClockSelect.setStatus("mandatory")


class _AtmE1ConfFillerCells_Type(Integer32):
    """Custom type atmE1ConfFillerCells based on Integer32"""
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


_AtmE1ConfFillerCells_Type.__name__ = "Integer32"
_AtmE1ConfFillerCells_Object = MibTableColumn
atmE1ConfFillerCells = _AtmE1ConfFillerCells_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 1, 1, 1, 4),
    _AtmE1ConfFillerCells_Type()
)
atmE1ConfFillerCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE1ConfFillerCells.setStatus("mandatory")
_AtmE1StatsGroup_ObjectIdentity = ObjectIdentity
atmE1StatsGroup = _AtmE1StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2)
)
_AtmE1StatsTable_Object = MibTable
atmE1StatsTable = _AtmE1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1)
)
if mibBuilder.loadTexts:
    atmE1StatsTable.setStatus("mandatory")
_AtmE1StatsEntry_Object = MibTableRow
atmE1StatsEntry = _AtmE1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1)
)
atmE1StatsEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-E1-MIB", "atmE1StatsPhysIndex"),
)
if mibBuilder.loadTexts:
    atmE1StatsEntry.setStatus("mandatory")
_AtmE1StatsPhysIndex_Type = Integer32
_AtmE1StatsPhysIndex_Object = MibTableColumn
atmE1StatsPhysIndex = _AtmE1StatsPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1, 1),
    _AtmE1StatsPhysIndex_Type()
)
atmE1StatsPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE1StatsPhysIndex.setStatus("mandatory")
_AtmE1StatsNoSignals_Type = Counter32
_AtmE1StatsNoSignals_Object = MibTableColumn
atmE1StatsNoSignals = _AtmE1StatsNoSignals_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1, 2),
    _AtmE1StatsNoSignals_Type()
)
atmE1StatsNoSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE1StatsNoSignals.setStatus("mandatory")
_AtmE1StatsRAIDetects_Type = Counter32
_AtmE1StatsRAIDetects_Object = MibTableColumn
atmE1StatsRAIDetects = _AtmE1StatsRAIDetects_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1, 3),
    _AtmE1StatsRAIDetects_Type()
)
atmE1StatsRAIDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE1StatsRAIDetects.setStatus("mandatory")
_AtmE1StatsFASErrors_Type = Counter32
_AtmE1StatsFASErrors_Object = MibTableColumn
atmE1StatsFASErrors = _AtmE1StatsFASErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1, 4),
    _AtmE1StatsFASErrors_Type()
)
atmE1StatsFASErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE1StatsFASErrors.setStatus("mandatory")
_AtmE1StatsCVErrors_Type = Counter32
_AtmE1StatsCVErrors_Object = MibTableColumn
atmE1StatsCVErrors = _AtmE1StatsCVErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1, 5),
    _AtmE1StatsCVErrors_Type()
)
atmE1StatsCVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE1StatsCVErrors.setStatus("mandatory")
_AtmE1StatsCRCErrors_Type = Counter32
_AtmE1StatsCRCErrors_Object = MibTableColumn
atmE1StatsCRCErrors = _AtmE1StatsCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1, 6),
    _AtmE1StatsCRCErrors_Type()
)
atmE1StatsCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE1StatsCRCErrors.setStatus("mandatory")
_AtmE1StatsEBitErrors_Type = Counter32
_AtmE1StatsEBitErrors_Object = MibTableColumn
atmE1StatsEBitErrors = _AtmE1StatsEBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1, 7),
    _AtmE1StatsEBitErrors_Type()
)
atmE1StatsEBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE1StatsEBitErrors.setStatus("mandatory")
_AtmE1StatsSyncLossCount_Type = Counter32
_AtmE1StatsSyncLossCount_Object = MibTableColumn
atmE1StatsSyncLossCount = _AtmE1StatsSyncLossCount_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1, 8),
    _AtmE1StatsSyncLossCount_Type()
)
atmE1StatsSyncLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE1StatsSyncLossCount.setStatus("mandatory")
_AtmE1StatsHECErrors_Type = Counter32
_AtmE1StatsHECErrors_Object = MibTableColumn
atmE1StatsHECErrors = _AtmE1StatsHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1, 9),
    _AtmE1StatsHECErrors_Type()
)
atmE1StatsHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE1StatsHECErrors.setStatus("mandatory")


class _AtmE1StatsSignalLoss_Type(Integer32):
    """Custom type atmE1StatsSignalLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmE1StatsSignalLoss_Type.__name__ = "Integer32"
_AtmE1StatsSignalLoss_Object = MibTableColumn
atmE1StatsSignalLoss = _AtmE1StatsSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1, 10),
    _AtmE1StatsSignalLoss_Type()
)
atmE1StatsSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE1StatsSignalLoss.setStatus("mandatory")


class _AtmE1StatsRAIDetect_Type(Integer32):
    """Custom type atmE1StatsRAIDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmE1StatsRAIDetect_Type.__name__ = "Integer32"
_AtmE1StatsRAIDetect_Object = MibTableColumn
atmE1StatsRAIDetect = _AtmE1StatsRAIDetect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1, 11),
    _AtmE1StatsRAIDetect_Type()
)
atmE1StatsRAIDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE1StatsRAIDetect.setStatus("mandatory")


class _AtmE1StatsSyncLoss_Type(Integer32):
    """Custom type atmE1StatsSyncLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmE1StatsSyncLoss_Type.__name__ = "Integer32"
_AtmE1StatsSyncLoss_Object = MibTableColumn
atmE1StatsSyncLoss = _AtmE1StatsSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1, 12),
    _AtmE1StatsSyncLoss_Type()
)
atmE1StatsSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE1StatsSyncLoss.setStatus("mandatory")


class _AtmE1StatsTxClockLoss_Type(Integer32):
    """Custom type atmE1StatsTxClockLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmE1StatsTxClockLoss_Type.__name__ = "Integer32"
_AtmE1StatsTxClockLoss_Object = MibTableColumn
atmE1StatsTxClockLoss = _AtmE1StatsTxClockLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1, 13),
    _AtmE1StatsTxClockLoss_Type()
)
atmE1StatsTxClockLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE1StatsTxClockLoss.setStatus("mandatory")


class _AtmE1StatsClearCounters_Type(Integer32):
    """Custom type atmE1StatsClearCounters based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmE1StatsClearCounters_Type.__name__ = "Integer32"
_AtmE1StatsClearCounters_Object = MibTableColumn
atmE1StatsClearCounters = _AtmE1StatsClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 6, 2, 1, 1, 14),
    _AtmE1StatsClearCounters_Type()
)
atmE1StatsClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE1StatsClearCounters.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMASYSTEMS-SONOMA-ATM-E1-MIB",
    **{"sonomaE1ATMAdapterGroup": sonomaE1ATMAdapterGroup,
       "atmE1ConfGroup": atmE1ConfGroup,
       "atmE1ConfPhyTable": atmE1ConfPhyTable,
       "atmE1ConfPhyEntry": atmE1ConfPhyEntry,
       "atmE1ConfPhysIndex": atmE1ConfPhysIndex,
       "atmE1ConfLoopback": atmE1ConfLoopback,
       "atmE1ConfTxClockSelect": atmE1ConfTxClockSelect,
       "atmE1ConfFillerCells": atmE1ConfFillerCells,
       "atmE1StatsGroup": atmE1StatsGroup,
       "atmE1StatsTable": atmE1StatsTable,
       "atmE1StatsEntry": atmE1StatsEntry,
       "atmE1StatsPhysIndex": atmE1StatsPhysIndex,
       "atmE1StatsNoSignals": atmE1StatsNoSignals,
       "atmE1StatsRAIDetects": atmE1StatsRAIDetects,
       "atmE1StatsFASErrors": atmE1StatsFASErrors,
       "atmE1StatsCVErrors": atmE1StatsCVErrors,
       "atmE1StatsCRCErrors": atmE1StatsCRCErrors,
       "atmE1StatsEBitErrors": atmE1StatsEBitErrors,
       "atmE1StatsSyncLossCount": atmE1StatsSyncLossCount,
       "atmE1StatsHECErrors": atmE1StatsHECErrors,
       "atmE1StatsSignalLoss": atmE1StatsSignalLoss,
       "atmE1StatsRAIDetect": atmE1StatsRAIDetect,
       "atmE1StatsSyncLoss": atmE1StatsSyncLoss,
       "atmE1StatsTxClockLoss": atmE1StatsTxClockLoss,
       "atmE1StatsClearCounters": atmE1StatsClearCounters}
)
