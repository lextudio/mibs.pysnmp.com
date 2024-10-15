# SNMP MIB module (SONOMASYSTEMS-SONOMA-ATM-T1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMASYSTEMS-SONOMA-ATM-T1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:43 2024
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

_SonomaT1ATMAdapterGroup_ObjectIdentity = ObjectIdentity
sonomaT1ATMAdapterGroup = _SonomaT1ATMAdapterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5)
)
_AtmDs1ConfGroup_ObjectIdentity = ObjectIdentity
atmDs1ConfGroup = _AtmDs1ConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1)
)
_AtmDs1ConfPhyTable_Object = MibTable
atmDs1ConfPhyTable = _AtmDs1ConfPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1, 1)
)
if mibBuilder.loadTexts:
    atmDs1ConfPhyTable.setStatus("mandatory")
_AtmDs1ConfPhyEntry_Object = MibTableRow
atmDs1ConfPhyEntry = _AtmDs1ConfPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1, 1, 1)
)
atmDs1ConfPhyEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-T1-MIB", "atmDs1ConfPhysIndex"),
)
if mibBuilder.loadTexts:
    atmDs1ConfPhyEntry.setStatus("mandatory")
_AtmDs1ConfPhysIndex_Type = Integer32
_AtmDs1ConfPhysIndex_Object = MibTableColumn
atmDs1ConfPhysIndex = _AtmDs1ConfPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1, 1, 1, 1),
    _AtmDs1ConfPhysIndex_Type()
)
atmDs1ConfPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1ConfPhysIndex.setStatus("mandatory")


class _AtmDs1ConfLoopback_Type(Integer32):
    """Custom type atmDs1ConfLoopback based on Integer32"""
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
        *(("line", 3),
          ("local", 4),
          ("none", 1),
          ("payload", 2))
    )


_AtmDs1ConfLoopback_Type.__name__ = "Integer32"
_AtmDs1ConfLoopback_Object = MibTableColumn
atmDs1ConfLoopback = _AtmDs1ConfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1, 1, 1, 2),
    _AtmDs1ConfLoopback_Type()
)
atmDs1ConfLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs1ConfLoopback.setStatus("mandatory")


class _AtmDs1ConfTxClockSelect_Type(Integer32):
    """Custom type atmDs1ConfTxClockSelect based on Integer32"""
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


_AtmDs1ConfTxClockSelect_Type.__name__ = "Integer32"
_AtmDs1ConfTxClockSelect_Object = MibTableColumn
atmDs1ConfTxClockSelect = _AtmDs1ConfTxClockSelect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1, 1, 1, 3),
    _AtmDs1ConfTxClockSelect_Type()
)
atmDs1ConfTxClockSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs1ConfTxClockSelect.setStatus("mandatory")


class _AtmDs1ConfFillerCells_Type(Integer32):
    """Custom type atmDs1ConfFillerCells based on Integer32"""
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


_AtmDs1ConfFillerCells_Type.__name__ = "Integer32"
_AtmDs1ConfFillerCells_Object = MibTableColumn
atmDs1ConfFillerCells = _AtmDs1ConfFillerCells_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1, 1, 1, 4),
    _AtmDs1ConfFillerCells_Type()
)
atmDs1ConfFillerCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs1ConfFillerCells.setStatus("mandatory")


class _AtmDs1ConfLineBuildOut_Type(Integer32):
    """Custom type atmDs1ConfLineBuildOut based on Integer32"""
    defaultValue = 6

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("long-haul-0-0-dB", 6),
          ("long-haul-15-0-dB", 8),
          ("long-haul-22-5-dB", 9),
          ("long-haul-7-5-dB", 7),
          ("short-haul-0-133-FT", 1),
          ("short-haul-133-266-FT", 2),
          ("short-haul-266-399-FT", 3),
          ("short-haul-399-533-FT", 4),
          ("short-haul-533-655-FT", 5))
    )


_AtmDs1ConfLineBuildOut_Type.__name__ = "Integer32"
_AtmDs1ConfLineBuildOut_Object = MibTableColumn
atmDs1ConfLineBuildOut = _AtmDs1ConfLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1, 1, 1, 5),
    _AtmDs1ConfLineBuildOut_Type()
)
atmDs1ConfLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs1ConfLineBuildOut.setStatus("mandatory")
_AtmDs1StatsGroup_ObjectIdentity = ObjectIdentity
atmDs1StatsGroup = _AtmDs1StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2)
)
_AtmDs1StatsTable_Object = MibTable
atmDs1StatsTable = _AtmDs1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1)
)
if mibBuilder.loadTexts:
    atmDs1StatsTable.setStatus("mandatory")
_AtmDs1StatsEntry_Object = MibTableRow
atmDs1StatsEntry = _AtmDs1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1)
)
atmDs1StatsEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-T1-MIB", "atmDs1StatsPhysIndex"),
)
if mibBuilder.loadTexts:
    atmDs1StatsEntry.setStatus("mandatory")
_AtmDs1StatsPhysIndex_Type = Integer32
_AtmDs1StatsPhysIndex_Object = MibTableColumn
atmDs1StatsPhysIndex = _AtmDs1StatsPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 1),
    _AtmDs1StatsPhysIndex_Type()
)
atmDs1StatsPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1StatsPhysIndex.setStatus("mandatory")
_AtmDs1StatsNoSignals_Type = Counter32
_AtmDs1StatsNoSignals_Object = MibTableColumn
atmDs1StatsNoSignals = _AtmDs1StatsNoSignals_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 2),
    _AtmDs1StatsNoSignals_Type()
)
atmDs1StatsNoSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1StatsNoSignals.setStatus("mandatory")
_AtmDs1StatsAISDetects_Type = Counter32
_AtmDs1StatsAISDetects_Object = MibTableColumn
atmDs1StatsAISDetects = _AtmDs1StatsAISDetects_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 3),
    _AtmDs1StatsAISDetects_Type()
)
atmDs1StatsAISDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1StatsAISDetects.setStatus("mandatory")
_AtmDs1StatsYelAlarmCount_Type = Counter32
_AtmDs1StatsYelAlarmCount_Object = MibTableColumn
atmDs1StatsYelAlarmCount = _AtmDs1StatsYelAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 4),
    _AtmDs1StatsYelAlarmCount_Type()
)
atmDs1StatsYelAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1StatsYelAlarmCount.setStatus("mandatory")
_AtmDs1StatsLCVErrors_Type = Counter32
_AtmDs1StatsLCVErrors_Object = MibTableColumn
atmDs1StatsLCVErrors = _AtmDs1StatsLCVErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 5),
    _AtmDs1StatsLCVErrors_Type()
)
atmDs1StatsLCVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1StatsLCVErrors.setStatus("mandatory")
_AtmDs1StatsPCVErrors_Type = Counter32
_AtmDs1StatsPCVErrors_Object = MibTableColumn
atmDs1StatsPCVErrors = _AtmDs1StatsPCVErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 6),
    _AtmDs1StatsPCVErrors_Type()
)
atmDs1StatsPCVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1StatsPCVErrors.setStatus("mandatory")
_AtmDs1StatsMOSErrors_Type = Counter32
_AtmDs1StatsMOSErrors_Object = MibTableColumn
atmDs1StatsMOSErrors = _AtmDs1StatsMOSErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 7),
    _AtmDs1StatsMOSErrors_Type()
)
atmDs1StatsMOSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1StatsMOSErrors.setStatus("mandatory")
_AtmDs1StatsSyncLossCount_Type = Counter32
_AtmDs1StatsSyncLossCount_Object = MibTableColumn
atmDs1StatsSyncLossCount = _AtmDs1StatsSyncLossCount_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 8),
    _AtmDs1StatsSyncLossCount_Type()
)
atmDs1StatsSyncLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1StatsSyncLossCount.setStatus("mandatory")
_AtmDs1StatsHECErrors_Type = Counter32
_AtmDs1StatsHECErrors_Object = MibTableColumn
atmDs1StatsHECErrors = _AtmDs1StatsHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 9),
    _AtmDs1StatsHECErrors_Type()
)
atmDs1StatsHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1StatsHECErrors.setStatus("mandatory")


class _AtmDs1StatsSignalLoss_Type(Integer32):
    """Custom type atmDs1StatsSignalLoss based on Integer32"""
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


_AtmDs1StatsSignalLoss_Type.__name__ = "Integer32"
_AtmDs1StatsSignalLoss_Object = MibTableColumn
atmDs1StatsSignalLoss = _AtmDs1StatsSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 10),
    _AtmDs1StatsSignalLoss_Type()
)
atmDs1StatsSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1StatsSignalLoss.setStatus("mandatory")


class _AtmDs1StatsAISDetect_Type(Integer32):
    """Custom type atmDs1StatsAISDetect based on Integer32"""
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


_AtmDs1StatsAISDetect_Type.__name__ = "Integer32"
_AtmDs1StatsAISDetect_Object = MibTableColumn
atmDs1StatsAISDetect = _AtmDs1StatsAISDetect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 11),
    _AtmDs1StatsAISDetect_Type()
)
atmDs1StatsAISDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1StatsAISDetect.setStatus("mandatory")


class _AtmDs1StatsYellowAlarm_Type(Integer32):
    """Custom type atmDs1StatsYellowAlarm based on Integer32"""
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


_AtmDs1StatsYellowAlarm_Type.__name__ = "Integer32"
_AtmDs1StatsYellowAlarm_Object = MibTableColumn
atmDs1StatsYellowAlarm = _AtmDs1StatsYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 12),
    _AtmDs1StatsYellowAlarm_Type()
)
atmDs1StatsYellowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1StatsYellowAlarm.setStatus("mandatory")


class _AtmDs1StatsSyncLoss_Type(Integer32):
    """Custom type atmDs1StatsSyncLoss based on Integer32"""
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


_AtmDs1StatsSyncLoss_Type.__name__ = "Integer32"
_AtmDs1StatsSyncLoss_Object = MibTableColumn
atmDs1StatsSyncLoss = _AtmDs1StatsSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 13),
    _AtmDs1StatsSyncLoss_Type()
)
atmDs1StatsSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1StatsSyncLoss.setStatus("mandatory")


class _AtmDs1StatsTxClockLoss_Type(Integer32):
    """Custom type atmDs1StatsTxClockLoss based on Integer32"""
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


_AtmDs1StatsTxClockLoss_Type.__name__ = "Integer32"
_AtmDs1StatsTxClockLoss_Object = MibTableColumn
atmDs1StatsTxClockLoss = _AtmDs1StatsTxClockLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 14),
    _AtmDs1StatsTxClockLoss_Type()
)
atmDs1StatsTxClockLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs1StatsTxClockLoss.setStatus("mandatory")


class _AtmDs1StatsClearCounters_Type(Integer32):
    """Custom type atmDs1StatsClearCounters based on Integer32"""
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


_AtmDs1StatsClearCounters_Type.__name__ = "Integer32"
_AtmDs1StatsClearCounters_Object = MibTableColumn
atmDs1StatsClearCounters = _AtmDs1StatsClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 15),
    _AtmDs1StatsClearCounters_Type()
)
atmDs1StatsClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs1StatsClearCounters.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMASYSTEMS-SONOMA-ATM-T1-MIB",
    **{"sonomaT1ATMAdapterGroup": sonomaT1ATMAdapterGroup,
       "atmDs1ConfGroup": atmDs1ConfGroup,
       "atmDs1ConfPhyTable": atmDs1ConfPhyTable,
       "atmDs1ConfPhyEntry": atmDs1ConfPhyEntry,
       "atmDs1ConfPhysIndex": atmDs1ConfPhysIndex,
       "atmDs1ConfLoopback": atmDs1ConfLoopback,
       "atmDs1ConfTxClockSelect": atmDs1ConfTxClockSelect,
       "atmDs1ConfFillerCells": atmDs1ConfFillerCells,
       "atmDs1ConfLineBuildOut": atmDs1ConfLineBuildOut,
       "atmDs1StatsGroup": atmDs1StatsGroup,
       "atmDs1StatsTable": atmDs1StatsTable,
       "atmDs1StatsEntry": atmDs1StatsEntry,
       "atmDs1StatsPhysIndex": atmDs1StatsPhysIndex,
       "atmDs1StatsNoSignals": atmDs1StatsNoSignals,
       "atmDs1StatsAISDetects": atmDs1StatsAISDetects,
       "atmDs1StatsYelAlarmCount": atmDs1StatsYelAlarmCount,
       "atmDs1StatsLCVErrors": atmDs1StatsLCVErrors,
       "atmDs1StatsPCVErrors": atmDs1StatsPCVErrors,
       "atmDs1StatsMOSErrors": atmDs1StatsMOSErrors,
       "atmDs1StatsSyncLossCount": atmDs1StatsSyncLossCount,
       "atmDs1StatsHECErrors": atmDs1StatsHECErrors,
       "atmDs1StatsSignalLoss": atmDs1StatsSignalLoss,
       "atmDs1StatsAISDetect": atmDs1StatsAISDetect,
       "atmDs1StatsYellowAlarm": atmDs1StatsYellowAlarm,
       "atmDs1StatsSyncLoss": atmDs1StatsSyncLoss,
       "atmDs1StatsTxClockLoss": atmDs1StatsTxClockLoss,
       "atmDs1StatsClearCounters": atmDs1StatsClearCounters}
)
