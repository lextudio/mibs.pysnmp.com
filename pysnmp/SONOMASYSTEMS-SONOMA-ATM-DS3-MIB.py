# SNMP MIB module (SONOMASYSTEMS-SONOMA-ATM-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMASYSTEMS-SONOMA-ATM-DS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:39 2024
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

_SonomaDS3ATMAdapterGroup_ObjectIdentity = ObjectIdentity
sonomaDS3ATMAdapterGroup = _SonomaDS3ATMAdapterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2)
)
_AtmDs3ConfGroup_ObjectIdentity = ObjectIdentity
atmDs3ConfGroup = _AtmDs3ConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1)
)
_AtmDs3ConfPhyTable_Object = MibTable
atmDs3ConfPhyTable = _AtmDs3ConfPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    atmDs3ConfPhyTable.setStatus("mandatory")
_AtmDs3ConfPhyEntry_Object = MibTableRow
atmDs3ConfPhyEntry = _AtmDs3ConfPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1, 1)
)
atmDs3ConfPhyEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-DS3-MIB", "atmDs3ConfPhysIndex"),
)
if mibBuilder.loadTexts:
    atmDs3ConfPhyEntry.setStatus("mandatory")
_AtmDs3ConfPhysIndex_Type = Integer32
_AtmDs3ConfPhysIndex_Object = MibTableColumn
atmDs3ConfPhysIndex = _AtmDs3ConfPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1, 1, 1),
    _AtmDs3ConfPhysIndex_Type()
)
atmDs3ConfPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3ConfPhysIndex.setStatus("mandatory")


class _AtmDs3ConfFraming_Type(Integer32):
    """Custom type atmDs3ConfFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("framingDS3", 1),
          ("framingE3", 2))
    )


_AtmDs3ConfFraming_Type.__name__ = "Integer32"
_AtmDs3ConfFraming_Object = MibTableColumn
atmDs3ConfFraming = _AtmDs3ConfFraming_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1, 1, 2),
    _AtmDs3ConfFraming_Type()
)
atmDs3ConfFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3ConfFraming.setStatus("mandatory")


class _AtmDs3ConfInsGFCBits_Type(Integer32):
    """Custom type atmDs3ConfInsGFCBits based on Integer32"""
    defaultValue = 2

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


_AtmDs3ConfInsGFCBits_Type.__name__ = "Integer32"
_AtmDs3ConfInsGFCBits_Object = MibTableColumn
atmDs3ConfInsGFCBits = _AtmDs3ConfInsGFCBits_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1, 1, 3),
    _AtmDs3ConfInsGFCBits_Type()
)
atmDs3ConfInsGFCBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs3ConfInsGFCBits.setStatus("mandatory")


class _AtmDs3ConfSerBipolarIO_Type(Integer32):
    """Custom type atmDs3ConfSerBipolarIO based on Integer32"""
    defaultValue = 1

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


_AtmDs3ConfSerBipolarIO_Type.__name__ = "Integer32"
_AtmDs3ConfSerBipolarIO_Object = MibTableColumn
atmDs3ConfSerBipolarIO = _AtmDs3ConfSerBipolarIO_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1, 1, 4),
    _AtmDs3ConfSerBipolarIO_Type()
)
atmDs3ConfSerBipolarIO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs3ConfSerBipolarIO.setStatus("mandatory")


class _AtmDs3ConfScramblePld_Type(Integer32):
    """Custom type atmDs3ConfScramblePld based on Integer32"""
    defaultValue = 1

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


_AtmDs3ConfScramblePld_Type.__name__ = "Integer32"
_AtmDs3ConfScramblePld_Object = MibTableColumn
atmDs3ConfScramblePld = _AtmDs3ConfScramblePld_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1, 1, 5),
    _AtmDs3ConfScramblePld_Type()
)
atmDs3ConfScramblePld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs3ConfScramblePld.setStatus("mandatory")


class _AtmDs3ConfOverheadPLCP_Type(Integer32):
    """Custom type atmDs3ConfOverheadPLCP based on Integer32"""
    defaultValue = 1

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


_AtmDs3ConfOverheadPLCP_Type.__name__ = "Integer32"
_AtmDs3ConfOverheadPLCP_Object = MibTableColumn
atmDs3ConfOverheadPLCP = _AtmDs3ConfOverheadPLCP_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1, 1, 6),
    _AtmDs3ConfOverheadPLCP_Type()
)
atmDs3ConfOverheadPLCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs3ConfOverheadPLCP.setStatus("mandatory")


class _AtmDs3ConfGenerateFEBE_Type(Integer32):
    """Custom type atmDs3ConfGenerateFEBE based on Integer32"""
    defaultValue = 1

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


_AtmDs3ConfGenerateFEBE_Type.__name__ = "Integer32"
_AtmDs3ConfGenerateFEBE_Object = MibTableColumn
atmDs3ConfGenerateFEBE = _AtmDs3ConfGenerateFEBE_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1, 1, 7),
    _AtmDs3ConfGenerateFEBE_Type()
)
atmDs3ConfGenerateFEBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs3ConfGenerateFEBE.setStatus("mandatory")


class _AtmDs3ConfGenerateFEAC_Type(Integer32):
    """Custom type atmDs3ConfGenerateFEAC based on Integer32"""
    defaultValue = 2

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


_AtmDs3ConfGenerateFEAC_Type.__name__ = "Integer32"
_AtmDs3ConfGenerateFEAC_Object = MibTableColumn
atmDs3ConfGenerateFEAC = _AtmDs3ConfGenerateFEAC_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1, 1, 8),
    _AtmDs3ConfGenerateFEAC_Type()
)
atmDs3ConfGenerateFEAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs3ConfGenerateFEAC.setStatus("mandatory")


class _AtmDs3ConfLoopback_Type(Integer32):
    """Custom type atmDs3ConfLoopback based on Integer32"""
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


_AtmDs3ConfLoopback_Type.__name__ = "Integer32"
_AtmDs3ConfLoopback_Object = MibTableColumn
atmDs3ConfLoopback = _AtmDs3ConfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1, 1, 9),
    _AtmDs3ConfLoopback_Type()
)
atmDs3ConfLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs3ConfLoopback.setStatus("mandatory")


class _AtmDs3ConfCableLength_Type(Integer32):
    """Custom type atmDs3ConfCableLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greaterThan225Feet", 2),
          ("notGreaterThan225Feet", 1))
    )


_AtmDs3ConfCableLength_Type.__name__ = "Integer32"
_AtmDs3ConfCableLength_Object = MibTableColumn
atmDs3ConfCableLength = _AtmDs3ConfCableLength_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1, 1, 10),
    _AtmDs3ConfCableLength_Type()
)
atmDs3ConfCableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs3ConfCableLength.setStatus("mandatory")


class _AtmDs3ConfInternalEqualizer_Type(Integer32):
    """Custom type atmDs3ConfInternalEqualizer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("use", 1))
    )


_AtmDs3ConfInternalEqualizer_Type.__name__ = "Integer32"
_AtmDs3ConfInternalEqualizer_Object = MibTableColumn
atmDs3ConfInternalEqualizer = _AtmDs3ConfInternalEqualizer_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1, 1, 11),
    _AtmDs3ConfInternalEqualizer_Type()
)
atmDs3ConfInternalEqualizer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs3ConfInternalEqualizer.setStatus("mandatory")


class _AtmDs3ConfFillerCells_Type(Integer32):
    """Custom type atmDs3ConfFillerCells based on Integer32"""
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


_AtmDs3ConfFillerCells_Type.__name__ = "Integer32"
_AtmDs3ConfFillerCells_Object = MibTableColumn
atmDs3ConfFillerCells = _AtmDs3ConfFillerCells_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1, 1, 12),
    _AtmDs3ConfFillerCells_Type()
)
atmDs3ConfFillerCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs3ConfFillerCells.setStatus("mandatory")


class _AtmDs3ConfGenerateClock_Type(Integer32):
    """Custom type atmDs3ConfGenerateClock based on Integer32"""
    defaultValue = 2

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


_AtmDs3ConfGenerateClock_Type.__name__ = "Integer32"
_AtmDs3ConfGenerateClock_Object = MibTableColumn
atmDs3ConfGenerateClock = _AtmDs3ConfGenerateClock_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 1, 1, 1, 13),
    _AtmDs3ConfGenerateClock_Type()
)
atmDs3ConfGenerateClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs3ConfGenerateClock.setStatus("mandatory")
_AtmDs3StatsGroup_ObjectIdentity = ObjectIdentity
atmDs3StatsGroup = _AtmDs3StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2)
)
_AtmDs3PhyStatsTable_Object = MibTable
atmDs3PhyStatsTable = _AtmDs3PhyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    atmDs3PhyStatsTable.setStatus("mandatory")
_AtmDs3PhyStatsEntry_Object = MibTableRow
atmDs3PhyStatsEntry = _AtmDs3PhyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1)
)
atmDs3PhyStatsEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-DS3-MIB", "atmDs3PhyStatsPhysIndex"),
)
if mibBuilder.loadTexts:
    atmDs3PhyStatsEntry.setStatus("mandatory")
_AtmDs3PhyStatsPhysIndex_Type = Integer32
_AtmDs3PhyStatsPhysIndex_Object = MibTableColumn
atmDs3PhyStatsPhysIndex = _AtmDs3PhyStatsPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 1),
    _AtmDs3PhyStatsPhysIndex_Type()
)
atmDs3PhyStatsPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3PhyStatsPhysIndex.setStatus("mandatory")
_AtmDs3StatsAlarms_Type = Counter32
_AtmDs3StatsAlarms_Object = MibTableColumn
atmDs3StatsAlarms = _AtmDs3StatsAlarms_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 2),
    _AtmDs3StatsAlarms_Type()
)
atmDs3StatsAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsAlarms.setStatus("mandatory")
_AtmDs3StatsNoSignals_Type = Counter32
_AtmDs3StatsNoSignals_Object = MibTableColumn
atmDs3StatsNoSignals = _AtmDs3StatsNoSignals_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 3),
    _AtmDs3StatsNoSignals_Type()
)
atmDs3StatsNoSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsNoSignals.setStatus("mandatory")
_AtmDs3StatsNoDs3Frames_Type = Counter32
_AtmDs3StatsNoDs3Frames_Object = MibTableColumn
atmDs3StatsNoDs3Frames = _AtmDs3StatsNoDs3Frames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 4),
    _AtmDs3StatsNoDs3Frames_Type()
)
atmDs3StatsNoDs3Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsNoDs3Frames.setStatus("mandatory")
_AtmDs3StatsAisDetects_Type = Counter32
_AtmDs3StatsAisDetects_Object = MibTableColumn
atmDs3StatsAisDetects = _AtmDs3StatsAisDetects_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 5),
    _AtmDs3StatsAisDetects_Type()
)
atmDs3StatsAisDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsAisDetects.setStatus("mandatory")
_AtmDs3StatsFrameErrs_Type = Counter32
_AtmDs3StatsFrameErrs_Object = MibTableColumn
atmDs3StatsFrameErrs = _AtmDs3StatsFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 6),
    _AtmDs3StatsFrameErrs_Type()
)
atmDs3StatsFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsFrameErrs.setStatus("mandatory")
_AtmDs3StatsParityErrs_Type = Counter32
_AtmDs3StatsParityErrs_Object = MibTableColumn
atmDs3StatsParityErrs = _AtmDs3StatsParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 7),
    _AtmDs3StatsParityErrs_Type()
)
atmDs3StatsParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsParityErrs.setStatus("mandatory")
_AtmDs3StatsCpErrs_Type = Counter32
_AtmDs3StatsCpErrs_Object = MibTableColumn
atmDs3StatsCpErrs = _AtmDs3StatsCpErrs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 8),
    _AtmDs3StatsCpErrs_Type()
)
atmDs3StatsCpErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsCpErrs.setStatus("mandatory")
_AtmDs3StatsFeBlockErrs_Type = Counter32
_AtmDs3StatsFeBlockErrs_Object = MibTableColumn
atmDs3StatsFeBlockErrs = _AtmDs3StatsFeBlockErrs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 9),
    _AtmDs3StatsFeBlockErrs_Type()
)
atmDs3StatsFeBlockErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsFeBlockErrs.setStatus("mandatory")
_AtmDs3StatsBpvErrs_Type = Counter32
_AtmDs3StatsBpvErrs_Object = MibTableColumn
atmDs3StatsBpvErrs = _AtmDs3StatsBpvErrs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 10),
    _AtmDs3StatsBpvErrs_Type()
)
atmDs3StatsBpvErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsBpvErrs.setStatus("mandatory")
_AtmDs3StatsRemoteAlarms_Type = Counter32
_AtmDs3StatsRemoteAlarms_Object = MibTableColumn
atmDs3StatsRemoteAlarms = _AtmDs3StatsRemoteAlarms_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 11),
    _AtmDs3StatsRemoteAlarms_Type()
)
atmDs3StatsRemoteAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsRemoteAlarms.setStatus("mandatory")


class _AtmDs3StatsSignalLoss_Type(Integer32):
    """Custom type atmDs3StatsSignalLoss based on Integer32"""
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


_AtmDs3StatsSignalLoss_Type.__name__ = "Integer32"
_AtmDs3StatsSignalLoss_Object = MibTableColumn
atmDs3StatsSignalLoss = _AtmDs3StatsSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 12),
    _AtmDs3StatsSignalLoss_Type()
)
atmDs3StatsSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsSignalLoss.setStatus("mandatory")


class _AtmDs3StatsOutOfCell_Type(Integer32):
    """Custom type atmDs3StatsOutOfCell based on Integer32"""
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


_AtmDs3StatsOutOfCell_Type.__name__ = "Integer32"
_AtmDs3StatsOutOfCell_Object = MibTableColumn
atmDs3StatsOutOfCell = _AtmDs3StatsOutOfCell_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 13),
    _AtmDs3StatsOutOfCell_Type()
)
atmDs3StatsOutOfCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsOutOfCell.setStatus("mandatory")


class _AtmDs3StatsFifoOverflow_Type(Integer32):
    """Custom type atmDs3StatsFifoOverflow based on Integer32"""
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


_AtmDs3StatsFifoOverflow_Type.__name__ = "Integer32"
_AtmDs3StatsFifoOverflow_Object = MibTableColumn
atmDs3StatsFifoOverflow = _AtmDs3StatsFifoOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 14),
    _AtmDs3StatsFifoOverflow_Type()
)
atmDs3StatsFifoOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsFifoOverflow.setStatus("mandatory")


class _AtmDs3StatsRemoteAlarmInd_Type(Integer32):
    """Custom type atmDs3StatsRemoteAlarmInd based on Integer32"""
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


_AtmDs3StatsRemoteAlarmInd_Type.__name__ = "Integer32"
_AtmDs3StatsRemoteAlarmInd_Object = MibTableColumn
atmDs3StatsRemoteAlarmInd = _AtmDs3StatsRemoteAlarmInd_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 15),
    _AtmDs3StatsRemoteAlarmInd_Type()
)
atmDs3StatsRemoteAlarmInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsRemoteAlarmInd.setStatus("mandatory")


class _AtmDs3StatsFrameLoss_Type(Integer32):
    """Custom type atmDs3StatsFrameLoss based on Integer32"""
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


_AtmDs3StatsFrameLoss_Type.__name__ = "Integer32"
_AtmDs3StatsFrameLoss_Object = MibTableColumn
atmDs3StatsFrameLoss = _AtmDs3StatsFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 16),
    _AtmDs3StatsFrameLoss_Type()
)
atmDs3StatsFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsFrameLoss.setStatus("mandatory")


class _AtmDs3StatsSyncLoss_Type(Integer32):
    """Custom type atmDs3StatsSyncLoss based on Integer32"""
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


_AtmDs3StatsSyncLoss_Type.__name__ = "Integer32"
_AtmDs3StatsSyncLoss_Object = MibTableColumn
atmDs3StatsSyncLoss = _AtmDs3StatsSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 17),
    _AtmDs3StatsSyncLoss_Type()
)
atmDs3StatsSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsSyncLoss.setStatus("mandatory")


class _AtmDs3StatsPlcpAlarmState_Type(Integer32):
    """Custom type atmDs3StatsPlcpAlarmState based on Integer32"""
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


_AtmDs3StatsPlcpAlarmState_Type.__name__ = "Integer32"
_AtmDs3StatsPlcpAlarmState_Object = MibTableColumn
atmDs3StatsPlcpAlarmState = _AtmDs3StatsPlcpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 18),
    _AtmDs3StatsPlcpAlarmState_Type()
)
atmDs3StatsPlcpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsPlcpAlarmState.setStatus("mandatory")


class _AtmDs3StatsAisState_Type(Integer32):
    """Custom type atmDs3StatsAisState based on Integer32"""
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


_AtmDs3StatsAisState_Type.__name__ = "Integer32"
_AtmDs3StatsAisState_Object = MibTableColumn
atmDs3StatsAisState = _AtmDs3StatsAisState_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 19),
    _AtmDs3StatsAisState_Type()
)
atmDs3StatsAisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDs3StatsAisState.setStatus("mandatory")


class _AtmDs3StatsClearCounters_Type(Integer32):
    """Custom type atmDs3StatsClearCounters based on Integer32"""
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


_AtmDs3StatsClearCounters_Type.__name__ = "Integer32"
_AtmDs3StatsClearCounters_Object = MibTableColumn
atmDs3StatsClearCounters = _AtmDs3StatsClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 2, 2, 1, 1, 20),
    _AtmDs3StatsClearCounters_Type()
)
atmDs3StatsClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDs3StatsClearCounters.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMASYSTEMS-SONOMA-ATM-DS3-MIB",
    **{"sonomaDS3ATMAdapterGroup": sonomaDS3ATMAdapterGroup,
       "atmDs3ConfGroup": atmDs3ConfGroup,
       "atmDs3ConfPhyTable": atmDs3ConfPhyTable,
       "atmDs3ConfPhyEntry": atmDs3ConfPhyEntry,
       "atmDs3ConfPhysIndex": atmDs3ConfPhysIndex,
       "atmDs3ConfFraming": atmDs3ConfFraming,
       "atmDs3ConfInsGFCBits": atmDs3ConfInsGFCBits,
       "atmDs3ConfSerBipolarIO": atmDs3ConfSerBipolarIO,
       "atmDs3ConfScramblePld": atmDs3ConfScramblePld,
       "atmDs3ConfOverheadPLCP": atmDs3ConfOverheadPLCP,
       "atmDs3ConfGenerateFEBE": atmDs3ConfGenerateFEBE,
       "atmDs3ConfGenerateFEAC": atmDs3ConfGenerateFEAC,
       "atmDs3ConfLoopback": atmDs3ConfLoopback,
       "atmDs3ConfCableLength": atmDs3ConfCableLength,
       "atmDs3ConfInternalEqualizer": atmDs3ConfInternalEqualizer,
       "atmDs3ConfFillerCells": atmDs3ConfFillerCells,
       "atmDs3ConfGenerateClock": atmDs3ConfGenerateClock,
       "atmDs3StatsGroup": atmDs3StatsGroup,
       "atmDs3PhyStatsTable": atmDs3PhyStatsTable,
       "atmDs3PhyStatsEntry": atmDs3PhyStatsEntry,
       "atmDs3PhyStatsPhysIndex": atmDs3PhyStatsPhysIndex,
       "atmDs3StatsAlarms": atmDs3StatsAlarms,
       "atmDs3StatsNoSignals": atmDs3StatsNoSignals,
       "atmDs3StatsNoDs3Frames": atmDs3StatsNoDs3Frames,
       "atmDs3StatsAisDetects": atmDs3StatsAisDetects,
       "atmDs3StatsFrameErrs": atmDs3StatsFrameErrs,
       "atmDs3StatsParityErrs": atmDs3StatsParityErrs,
       "atmDs3StatsCpErrs": atmDs3StatsCpErrs,
       "atmDs3StatsFeBlockErrs": atmDs3StatsFeBlockErrs,
       "atmDs3StatsBpvErrs": atmDs3StatsBpvErrs,
       "atmDs3StatsRemoteAlarms": atmDs3StatsRemoteAlarms,
       "atmDs3StatsSignalLoss": atmDs3StatsSignalLoss,
       "atmDs3StatsOutOfCell": atmDs3StatsOutOfCell,
       "atmDs3StatsFifoOverflow": atmDs3StatsFifoOverflow,
       "atmDs3StatsRemoteAlarmInd": atmDs3StatsRemoteAlarmInd,
       "atmDs3StatsFrameLoss": atmDs3StatsFrameLoss,
       "atmDs3StatsSyncLoss": atmDs3StatsSyncLoss,
       "atmDs3StatsPlcpAlarmState": atmDs3StatsPlcpAlarmState,
       "atmDs3StatsAisState": atmDs3StatsAisState,
       "atmDs3StatsClearCounters": atmDs3StatsClearCounters}
)
