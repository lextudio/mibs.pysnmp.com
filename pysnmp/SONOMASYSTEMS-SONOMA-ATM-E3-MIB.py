# SNMP MIB module (SONOMASYSTEMS-SONOMA-ATM-E3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMASYSTEMS-SONOMA-ATM-E3-MIB
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

_SonomaE3ATMAdapterGroup_ObjectIdentity = ObjectIdentity
sonomaE3ATMAdapterGroup = _SonomaE3ATMAdapterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3)
)
_AtmE3ConfGroup_ObjectIdentity = ObjectIdentity
atmE3ConfGroup = _AtmE3ConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1)
)
_AtmE3ConfPhyTable_Object = MibTable
atmE3ConfPhyTable = _AtmE3ConfPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1)
)
if mibBuilder.loadTexts:
    atmE3ConfPhyTable.setStatus("mandatory")
_AtmE3ConfPhyEntry_Object = MibTableRow
atmE3ConfPhyEntry = _AtmE3ConfPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1)
)
atmE3ConfPhyEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-E3-MIB", "atmE3ConfPhysIndex"),
)
if mibBuilder.loadTexts:
    atmE3ConfPhyEntry.setStatus("mandatory")
_AtmE3ConfPhysIndex_Type = Integer32
_AtmE3ConfPhysIndex_Object = MibTableColumn
atmE3ConfPhysIndex = _AtmE3ConfPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 1),
    _AtmE3ConfPhysIndex_Type()
)
atmE3ConfPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3ConfPhysIndex.setStatus("mandatory")


class _AtmE3ConfFraming_Type(Integer32):
    """Custom type atmE3ConfFraming based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("framingE3", 2)
    )


_AtmE3ConfFraming_Type.__name__ = "Integer32"
_AtmE3ConfFraming_Object = MibTableColumn
atmE3ConfFraming = _AtmE3ConfFraming_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 2),
    _AtmE3ConfFraming_Type()
)
atmE3ConfFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3ConfFraming.setStatus("mandatory")


class _AtmE3ConfInsGFCBits_Type(Integer32):
    """Custom type atmE3ConfInsGFCBits based on Integer32"""
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


_AtmE3ConfInsGFCBits_Type.__name__ = "Integer32"
_AtmE3ConfInsGFCBits_Object = MibTableColumn
atmE3ConfInsGFCBits = _AtmE3ConfInsGFCBits_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 3),
    _AtmE3ConfInsGFCBits_Type()
)
atmE3ConfInsGFCBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE3ConfInsGFCBits.setStatus("mandatory")


class _AtmE3ConfSerBipolarIO_Type(Integer32):
    """Custom type atmE3ConfSerBipolarIO based on Integer32"""
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


_AtmE3ConfSerBipolarIO_Type.__name__ = "Integer32"
_AtmE3ConfSerBipolarIO_Object = MibTableColumn
atmE3ConfSerBipolarIO = _AtmE3ConfSerBipolarIO_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 4),
    _AtmE3ConfSerBipolarIO_Type()
)
atmE3ConfSerBipolarIO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE3ConfSerBipolarIO.setStatus("mandatory")


class _AtmE3ConfPayloadScrambling_Type(Integer32):
    """Custom type atmE3ConfPayloadScrambling based on Integer32"""
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


_AtmE3ConfPayloadScrambling_Type.__name__ = "Integer32"
_AtmE3ConfPayloadScrambling_Object = MibTableColumn
atmE3ConfPayloadScrambling = _AtmE3ConfPayloadScrambling_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 5),
    _AtmE3ConfPayloadScrambling_Type()
)
atmE3ConfPayloadScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE3ConfPayloadScrambling.setStatus("mandatory")


class _AtmE3ConfOverheadProcessing_Type(Integer32):
    """Custom type atmE3ConfOverheadProcessing based on Integer32"""
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


_AtmE3ConfOverheadProcessing_Type.__name__ = "Integer32"
_AtmE3ConfOverheadProcessing_Object = MibTableColumn
atmE3ConfOverheadProcessing = _AtmE3ConfOverheadProcessing_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 6),
    _AtmE3ConfOverheadProcessing_Type()
)
atmE3ConfOverheadProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE3ConfOverheadProcessing.setStatus("mandatory")


class _AtmE3ConfHDB3Encoding_Type(Integer32):
    """Custom type atmE3ConfHDB3Encoding based on Integer32"""
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


_AtmE3ConfHDB3Encoding_Type.__name__ = "Integer32"
_AtmE3ConfHDB3Encoding_Object = MibTableColumn
atmE3ConfHDB3Encoding = _AtmE3ConfHDB3Encoding_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 7),
    _AtmE3ConfHDB3Encoding_Type()
)
atmE3ConfHDB3Encoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE3ConfHDB3Encoding.setStatus("mandatory")


class _AtmE3ConfLoopback_Type(Integer32):
    """Custom type atmE3ConfLoopback based on Integer32"""
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


_AtmE3ConfLoopback_Type.__name__ = "Integer32"
_AtmE3ConfLoopback_Object = MibTableColumn
atmE3ConfLoopback = _AtmE3ConfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 8),
    _AtmE3ConfLoopback_Type()
)
atmE3ConfLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE3ConfLoopback.setStatus("mandatory")


class _AtmE3ConfCableLength_Type(Integer32):
    """Custom type atmE3ConfCableLength based on Integer32"""
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


_AtmE3ConfCableLength_Type.__name__ = "Integer32"
_AtmE3ConfCableLength_Object = MibTableColumn
atmE3ConfCableLength = _AtmE3ConfCableLength_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 9),
    _AtmE3ConfCableLength_Type()
)
atmE3ConfCableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE3ConfCableLength.setStatus("mandatory")


class _AtmE3ConfInternalEqualizer_Type(Integer32):
    """Custom type atmE3ConfInternalEqualizer based on Integer32"""
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


_AtmE3ConfInternalEqualizer_Type.__name__ = "Integer32"
_AtmE3ConfInternalEqualizer_Object = MibTableColumn
atmE3ConfInternalEqualizer = _AtmE3ConfInternalEqualizer_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 10),
    _AtmE3ConfInternalEqualizer_Type()
)
atmE3ConfInternalEqualizer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE3ConfInternalEqualizer.setStatus("mandatory")


class _AtmE3ConfFillerCells_Type(Integer32):
    """Custom type atmE3ConfFillerCells based on Integer32"""
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


_AtmE3ConfFillerCells_Type.__name__ = "Integer32"
_AtmE3ConfFillerCells_Object = MibTableColumn
atmE3ConfFillerCells = _AtmE3ConfFillerCells_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 11),
    _AtmE3ConfFillerCells_Type()
)
atmE3ConfFillerCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE3ConfFillerCells.setStatus("mandatory")


class _AtmE3ConfGenerateClock_Type(Integer32):
    """Custom type atmE3ConfGenerateClock based on Integer32"""
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


_AtmE3ConfGenerateClock_Type.__name__ = "Integer32"
_AtmE3ConfGenerateClock_Object = MibTableColumn
atmE3ConfGenerateClock = _AtmE3ConfGenerateClock_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 12),
    _AtmE3ConfGenerateClock_Type()
)
atmE3ConfGenerateClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE3ConfGenerateClock.setStatus("mandatory")
_AtmE3StatsGroup_ObjectIdentity = ObjectIdentity
atmE3StatsGroup = _AtmE3StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2)
)
_AtmE3StatsTable_Object = MibTable
atmE3StatsTable = _AtmE3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    atmE3StatsTable.setStatus("mandatory")
_AtmE3StatsEntry_Object = MibTableRow
atmE3StatsEntry = _AtmE3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1)
)
atmE3StatsEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-E3-MIB", "atmE3StatsPhysIndex"),
)
if mibBuilder.loadTexts:
    atmE3StatsEntry.setStatus("mandatory")
_AtmE3StatsPhysIndex_Type = Integer32
_AtmE3StatsPhysIndex_Object = MibTableColumn
atmE3StatsPhysIndex = _AtmE3StatsPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 1),
    _AtmE3StatsPhysIndex_Type()
)
atmE3StatsPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsPhysIndex.setStatus("mandatory")
_AtmE3StatsNoSignals_Type = Counter32
_AtmE3StatsNoSignals_Object = MibTableColumn
atmE3StatsNoSignals = _AtmE3StatsNoSignals_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 2),
    _AtmE3StatsNoSignals_Type()
)
atmE3StatsNoSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsNoSignals.setStatus("mandatory")
_AtmE3StatsNoE3Frames_Type = Counter32
_AtmE3StatsNoE3Frames_Object = MibTableColumn
atmE3StatsNoE3Frames = _AtmE3StatsNoE3Frames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 3),
    _AtmE3StatsNoE3Frames_Type()
)
atmE3StatsNoE3Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsNoE3Frames.setStatus("mandatory")
_AtmE3StatsFrameErrors_Type = Counter32
_AtmE3StatsFrameErrors_Object = MibTableColumn
atmE3StatsFrameErrors = _AtmE3StatsFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 4),
    _AtmE3StatsFrameErrors_Type()
)
atmE3StatsFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsFrameErrors.setStatus("mandatory")
_AtmE3StatsHECErrors_Type = Counter32
_AtmE3StatsHECErrors_Object = MibTableColumn
atmE3StatsHECErrors = _AtmE3StatsHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 5),
    _AtmE3StatsHECErrors_Type()
)
atmE3StatsHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsHECErrors.setStatus("mandatory")
_AtmE3StatsEMErrors_Type = Counter32
_AtmE3StatsEMErrors_Object = MibTableColumn
atmE3StatsEMErrors = _AtmE3StatsEMErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 6),
    _AtmE3StatsEMErrors_Type()
)
atmE3StatsEMErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsEMErrors.setStatus("mandatory")
_AtmE3StatsFeBlockErrors_Type = Counter32
_AtmE3StatsFeBlockErrors_Object = MibTableColumn
atmE3StatsFeBlockErrors = _AtmE3StatsFeBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 7),
    _AtmE3StatsFeBlockErrors_Type()
)
atmE3StatsFeBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsFeBlockErrors.setStatus("mandatory")
_AtmE3StatsBpvErrors_Type = Counter32
_AtmE3StatsBpvErrors_Object = MibTableColumn
atmE3StatsBpvErrors = _AtmE3StatsBpvErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 8),
    _AtmE3StatsBpvErrors_Type()
)
atmE3StatsBpvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsBpvErrors.setStatus("mandatory")
_AtmE3StatsPayloadTypeMismatches_Type = Counter32
_AtmE3StatsPayloadTypeMismatches_Object = MibTableColumn
atmE3StatsPayloadTypeMismatches = _AtmE3StatsPayloadTypeMismatches_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 9),
    _AtmE3StatsPayloadTypeMismatches_Type()
)
atmE3StatsPayloadTypeMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsPayloadTypeMismatches.setStatus("mandatory")
_AtmE3StatsTimingMarkers_Type = Counter32
_AtmE3StatsTimingMarkers_Object = MibTableColumn
atmE3StatsTimingMarkers = _AtmE3StatsTimingMarkers_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 10),
    _AtmE3StatsTimingMarkers_Type()
)
atmE3StatsTimingMarkers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsTimingMarkers.setStatus("mandatory")
_AtmE3StatsAISDetects_Type = Counter32
_AtmE3StatsAISDetects_Object = MibTableColumn
atmE3StatsAISDetects = _AtmE3StatsAISDetects_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 11),
    _AtmE3StatsAISDetects_Type()
)
atmE3StatsAISDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsAISDetects.setStatus("mandatory")
_AtmE3StatsRDIDetects_Type = Counter32
_AtmE3StatsRDIDetects_Object = MibTableColumn
atmE3StatsRDIDetects = _AtmE3StatsRDIDetects_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 12),
    _AtmE3StatsRDIDetects_Type()
)
atmE3StatsRDIDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsRDIDetects.setStatus("mandatory")


class _AtmE3StatsSignalLoss_Type(Integer32):
    """Custom type atmE3StatsSignalLoss based on Integer32"""
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


_AtmE3StatsSignalLoss_Type.__name__ = "Integer32"
_AtmE3StatsSignalLoss_Object = MibTableColumn
atmE3StatsSignalLoss = _AtmE3StatsSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 13),
    _AtmE3StatsSignalLoss_Type()
)
atmE3StatsSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsSignalLoss.setStatus("mandatory")


class _AtmE3StatsFrameLoss_Type(Integer32):
    """Custom type atmE3StatsFrameLoss based on Integer32"""
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


_AtmE3StatsFrameLoss_Type.__name__ = "Integer32"
_AtmE3StatsFrameLoss_Object = MibTableColumn
atmE3StatsFrameLoss = _AtmE3StatsFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 14),
    _AtmE3StatsFrameLoss_Type()
)
atmE3StatsFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsFrameLoss.setStatus("mandatory")


class _AtmE3StatsSyncLoss_Type(Integer32):
    """Custom type atmE3StatsSyncLoss based on Integer32"""
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


_AtmE3StatsSyncLoss_Type.__name__ = "Integer32"
_AtmE3StatsSyncLoss_Object = MibTableColumn
atmE3StatsSyncLoss = _AtmE3StatsSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 15),
    _AtmE3StatsSyncLoss_Type()
)
atmE3StatsSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsSyncLoss.setStatus("mandatory")


class _AtmE3StatsOutOfCell_Type(Integer32):
    """Custom type atmE3StatsOutOfCell based on Integer32"""
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


_AtmE3StatsOutOfCell_Type.__name__ = "Integer32"
_AtmE3StatsOutOfCell_Object = MibTableColumn
atmE3StatsOutOfCell = _AtmE3StatsOutOfCell_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 16),
    _AtmE3StatsOutOfCell_Type()
)
atmE3StatsOutOfCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsOutOfCell.setStatus("mandatory")


class _AtmE3StatsFIFOOverflow_Type(Integer32):
    """Custom type atmE3StatsFIFOOverflow based on Integer32"""
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


_AtmE3StatsFIFOOverflow_Type.__name__ = "Integer32"
_AtmE3StatsFIFOOverflow_Object = MibTableColumn
atmE3StatsFIFOOverflow = _AtmE3StatsFIFOOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 17),
    _AtmE3StatsFIFOOverflow_Type()
)
atmE3StatsFIFOOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsFIFOOverflow.setStatus("mandatory")


class _AtmE3StatsPayloadTypeMismatch_Type(Integer32):
    """Custom type atmE3StatsPayloadTypeMismatch based on Integer32"""
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


_AtmE3StatsPayloadTypeMismatch_Type.__name__ = "Integer32"
_AtmE3StatsPayloadTypeMismatch_Object = MibTableColumn
atmE3StatsPayloadTypeMismatch = _AtmE3StatsPayloadTypeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 18),
    _AtmE3StatsPayloadTypeMismatch_Type()
)
atmE3StatsPayloadTypeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsPayloadTypeMismatch.setStatus("mandatory")


class _AtmE3StatsTimingMarker_Type(Integer32):
    """Custom type atmE3StatsTimingMarker based on Integer32"""
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


_AtmE3StatsTimingMarker_Type.__name__ = "Integer32"
_AtmE3StatsTimingMarker_Object = MibTableColumn
atmE3StatsTimingMarker = _AtmE3StatsTimingMarker_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 19),
    _AtmE3StatsTimingMarker_Type()
)
atmE3StatsTimingMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsTimingMarker.setStatus("mandatory")


class _AtmE3StatsAISDetect_Type(Integer32):
    """Custom type atmE3StatsAISDetect based on Integer32"""
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


_AtmE3StatsAISDetect_Type.__name__ = "Integer32"
_AtmE3StatsAISDetect_Object = MibTableColumn
atmE3StatsAISDetect = _AtmE3StatsAISDetect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 20),
    _AtmE3StatsAISDetect_Type()
)
atmE3StatsAISDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsAISDetect.setStatus("mandatory")


class _AtmE3StatsRDIDetect_Type(Integer32):
    """Custom type atmE3StatsRDIDetect based on Integer32"""
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


_AtmE3StatsRDIDetect_Type.__name__ = "Integer32"
_AtmE3StatsRDIDetect_Object = MibTableColumn
atmE3StatsRDIDetect = _AtmE3StatsRDIDetect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 21),
    _AtmE3StatsRDIDetect_Type()
)
atmE3StatsRDIDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmE3StatsRDIDetect.setStatus("mandatory")


class _AtmE3StatsClearCounters_Type(Integer32):
    """Custom type atmE3StatsClearCounters based on Integer32"""
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


_AtmE3StatsClearCounters_Type.__name__ = "Integer32"
_AtmE3StatsClearCounters_Object = MibTableColumn
atmE3StatsClearCounters = _AtmE3StatsClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 22),
    _AtmE3StatsClearCounters_Type()
)
atmE3StatsClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmE3StatsClearCounters.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMASYSTEMS-SONOMA-ATM-E3-MIB",
    **{"sonomaE3ATMAdapterGroup": sonomaE3ATMAdapterGroup,
       "atmE3ConfGroup": atmE3ConfGroup,
       "atmE3ConfPhyTable": atmE3ConfPhyTable,
       "atmE3ConfPhyEntry": atmE3ConfPhyEntry,
       "atmE3ConfPhysIndex": atmE3ConfPhysIndex,
       "atmE3ConfFraming": atmE3ConfFraming,
       "atmE3ConfInsGFCBits": atmE3ConfInsGFCBits,
       "atmE3ConfSerBipolarIO": atmE3ConfSerBipolarIO,
       "atmE3ConfPayloadScrambling": atmE3ConfPayloadScrambling,
       "atmE3ConfOverheadProcessing": atmE3ConfOverheadProcessing,
       "atmE3ConfHDB3Encoding": atmE3ConfHDB3Encoding,
       "atmE3ConfLoopback": atmE3ConfLoopback,
       "atmE3ConfCableLength": atmE3ConfCableLength,
       "atmE3ConfInternalEqualizer": atmE3ConfInternalEqualizer,
       "atmE3ConfFillerCells": atmE3ConfFillerCells,
       "atmE3ConfGenerateClock": atmE3ConfGenerateClock,
       "atmE3StatsGroup": atmE3StatsGroup,
       "atmE3StatsTable": atmE3StatsTable,
       "atmE3StatsEntry": atmE3StatsEntry,
       "atmE3StatsPhysIndex": atmE3StatsPhysIndex,
       "atmE3StatsNoSignals": atmE3StatsNoSignals,
       "atmE3StatsNoE3Frames": atmE3StatsNoE3Frames,
       "atmE3StatsFrameErrors": atmE3StatsFrameErrors,
       "atmE3StatsHECErrors": atmE3StatsHECErrors,
       "atmE3StatsEMErrors": atmE3StatsEMErrors,
       "atmE3StatsFeBlockErrors": atmE3StatsFeBlockErrors,
       "atmE3StatsBpvErrors": atmE3StatsBpvErrors,
       "atmE3StatsPayloadTypeMismatches": atmE3StatsPayloadTypeMismatches,
       "atmE3StatsTimingMarkers": atmE3StatsTimingMarkers,
       "atmE3StatsAISDetects": atmE3StatsAISDetects,
       "atmE3StatsRDIDetects": atmE3StatsRDIDetects,
       "atmE3StatsSignalLoss": atmE3StatsSignalLoss,
       "atmE3StatsFrameLoss": atmE3StatsFrameLoss,
       "atmE3StatsSyncLoss": atmE3StatsSyncLoss,
       "atmE3StatsOutOfCell": atmE3StatsOutOfCell,
       "atmE3StatsFIFOOverflow": atmE3StatsFIFOOverflow,
       "atmE3StatsPayloadTypeMismatch": atmE3StatsPayloadTypeMismatch,
       "atmE3StatsTimingMarker": atmE3StatsTimingMarker,
       "atmE3StatsAISDetect": atmE3StatsAISDetect,
       "atmE3StatsRDIDetect": atmE3StatsRDIDetect,
       "atmE3StatsClearCounters": atmE3StatsClearCounters}
)
