# SNMP MIB module (CISCO-ATM-CELL-LAYER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-CELL-LAYER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:47 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoAtmCellLayerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 133)
)
ciscoAtmCellLayerMIB.setRevisions(
        ("2002-06-28 00:00",
         "2000-05-02 00:00",
         "1999-05-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoAtmCellLayerMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmCellLayerMIBObjects = _CiscoAtmCellLayerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1)
)
_CaclConfig_ObjectIdentity = ObjectIdentity
caclConfig = _CaclConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 1)
)
_CaclConfigTable_Object = MibTable
caclConfigTable = _CaclConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 1, 1)
)
if mibBuilder.loadTexts:
    caclConfigTable.setStatus("current")
_CaclConfigEntry_Object = MibTableRow
caclConfigEntry = _CaclConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 1, 1, 1)
)
caclConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    caclConfigEntry.setStatus("current")


class _CaclNullCellHeader_Type(OctetString):
    """Custom type caclNullCellHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CaclNullCellHeader_Type.__name__ = "OctetString"
_CaclNullCellHeader_Object = MibTableColumn
caclNullCellHeader = _CaclNullCellHeader_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 1, 1, 1, 1),
    _CaclNullCellHeader_Type()
)
caclNullCellHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caclNullCellHeader.setStatus("current")


class _CaclNullCellPayload_Type(Unsigned32):
    """Custom type caclNullCellPayload based on Unsigned32"""
    defaultHexValue = 106

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CaclNullCellPayload_Type.__name__ = "Unsigned32"
_CaclNullCellPayload_Object = MibTableColumn
caclNullCellPayload = _CaclNullCellPayload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 1, 1, 1, 2),
    _CaclNullCellPayload_Type()
)
caclNullCellPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caclNullCellPayload.setStatus("current")


class _CaclHecCosetEnable_Type(TruthValue):
    """Custom type caclHecCosetEnable based on TruthValue"""


_CaclHecCosetEnable_Object = MibTableColumn
caclHecCosetEnable = _CaclHecCosetEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 1, 1, 1, 3),
    _CaclHecCosetEnable_Type()
)
caclHecCosetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caclHecCosetEnable.setStatus("current")


class _CaclPayloadScramblingEnable_Type(TruthValue):
    """Custom type caclPayloadScramblingEnable based on TruthValue"""


_CaclPayloadScramblingEnable_Object = MibTableColumn
caclPayloadScramblingEnable = _CaclPayloadScramblingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 1, 1, 1, 4),
    _CaclPayloadScramblingEnable_Type()
)
caclPayloadScramblingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caclPayloadScramblingEnable.setStatus("current")


class _CaclTimeElapsed_Type(Integer32):
    """Custom type caclTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_CaclTimeElapsed_Type.__name__ = "Integer32"
_CaclTimeElapsed_Object = MibTableColumn
caclTimeElapsed = _CaclTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 1, 1, 1, 5),
    _CaclTimeElapsed_Type()
)
caclTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclTimeElapsed.setStatus("current")


class _CaclValidIntervals_Type(Integer32):
    """Custom type caclValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CaclValidIntervals_Type.__name__ = "Integer32"
_CaclValidIntervals_Object = MibTableColumn
caclValidIntervals = _CaclValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 1, 1, 1, 6),
    _CaclValidIntervals_Type()
)
caclValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclValidIntervals.setStatus("current")


class _CaclInvalidIntervals_Type(Integer32):
    """Custom type caclInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CaclInvalidIntervals_Type.__name__ = "Integer32"
_CaclInvalidIntervals_Object = MibTableColumn
caclInvalidIntervals = _CaclInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 1, 1, 1, 7),
    _CaclInvalidIntervals_Type()
)
caclInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInvalidIntervals.setStatus("current")
_CaclStats_ObjectIdentity = ObjectIdentity
caclStats = _CaclStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2)
)
_CaclStatsTable_Object = MibTable
caclStatsTable = _CaclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1)
)
if mibBuilder.loadTexts:
    caclStatsTable.setStatus("current")
_CaclStatsEntry_Object = MibTableRow
caclStatsEntry = _CaclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1)
)
caclStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    caclStatsEntry.setStatus("current")
_CaclInRcvCLP0Cells_Type = Counter32
_CaclInRcvCLP0Cells_Object = MibTableColumn
caclInRcvCLP0Cells = _CaclInRcvCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 1),
    _CaclInRcvCLP0Cells_Type()
)
caclInRcvCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInRcvCLP0Cells.setStatus("current")
_CaclInRcvCLP1Cells_Type = Counter32
_CaclInRcvCLP1Cells_Object = MibTableColumn
caclInRcvCLP1Cells = _CaclInRcvCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 2),
    _CaclInRcvCLP1Cells_Type()
)
caclInRcvCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInRcvCLP1Cells.setStatus("current")
_CaclInValidOAMCells_Type = Counter32
_CaclInValidOAMCells_Object = MibTableColumn
caclInValidOAMCells = _CaclInValidOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 3),
    _CaclInValidOAMCells_Type()
)
caclInValidOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInValidOAMCells.setStatus("current")
_CaclInErrOAMCells_Type = Counter32
_CaclInErrOAMCells_Object = MibTableColumn
caclInErrOAMCells = _CaclInErrOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 4),
    _CaclInErrOAMCells_Type()
)
caclInErrOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInErrOAMCells.setStatus("current")
_CaclInGfcCells_Type = Counter32
_CaclInGfcCells_Object = MibTableColumn
caclInGfcCells = _CaclInGfcCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 5),
    _CaclInGfcCells_Type()
)
caclInGfcCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInGfcCells.setStatus("current")
_CaclInVpiVciErrCells_Type = Counter32
_CaclInVpiVciErrCells_Object = MibTableColumn
caclInVpiVciErrCells = _CaclInVpiVciErrCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 6),
    _CaclInVpiVciErrCells_Type()
)
caclInVpiVciErrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInVpiVciErrCells.setStatus("current")


class _CaclInLastUnknVpi_Type(Integer32):
    """Custom type caclInLastUnknVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CaclInLastUnknVpi_Type.__name__ = "Integer32"
_CaclInLastUnknVpi_Object = MibTableColumn
caclInLastUnknVpi = _CaclInLastUnknVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 7),
    _CaclInLastUnknVpi_Type()
)
caclInLastUnknVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInLastUnknVpi.setStatus("current")


class _CaclInLastUnknVci_Type(Integer32):
    """Custom type caclInLastUnknVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaclInLastUnknVci_Type.__name__ = "Integer32"
_CaclInLastUnknVci_Object = MibTableColumn
caclInLastUnknVci = _CaclInLastUnknVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 8),
    _CaclInLastUnknVci_Type()
)
caclInLastUnknVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInLastUnknVci.setStatus("current")
_CaclInXmtCLP0Cells_Type = Counter32
_CaclInXmtCLP0Cells_Object = MibTableColumn
caclInXmtCLP0Cells = _CaclInXmtCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 9),
    _CaclInXmtCLP0Cells_Type()
)
caclInXmtCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInXmtCLP0Cells.setStatus("current")
_CaclInXmtCLP1Cells_Type = Counter32
_CaclInXmtCLP1Cells_Object = MibTableColumn
caclInXmtCLP1Cells = _CaclInXmtCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 10),
    _CaclInXmtCLP1Cells_Type()
)
caclInXmtCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInXmtCLP1Cells.setStatus("current")
_CaclInValidRMCells_Type = Counter32
_CaclInValidRMCells_Object = MibTableColumn
caclInValidRMCells = _CaclInValidRMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 11),
    _CaclInValidRMCells_Type()
)
caclInValidRMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInValidRMCells.setStatus("current")
_CaclInRcvIdleCells_Type = Counter32
_CaclInRcvIdleCells_Object = MibTableColumn
caclInRcvIdleCells = _CaclInRcvIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 12),
    _CaclInRcvIdleCells_Type()
)
caclInRcvIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInRcvIdleCells.setStatus("current")
_CaclInHecErrDiscCells_Type = Counter32
_CaclInHecErrDiscCells_Object = MibTableColumn
caclInHecErrDiscCells = _CaclInHecErrDiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 13),
    _CaclInHecErrDiscCells_Type()
)
caclInHecErrDiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInHecErrDiscCells.setStatus("current")
_CaclInHecErrCorrectedCells_Type = Counter32
_CaclInHecErrCorrectedCells_Object = MibTableColumn
caclInHecErrCorrectedCells = _CaclInHecErrCorrectedCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 14),
    _CaclInHecErrCorrectedCells_Type()
)
caclInHecErrCorrectedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInHecErrCorrectedCells.setStatus("current")
_CaclInUpcCLP0DiscCells_Type = Counter32
_CaclInUpcCLP0DiscCells_Object = MibTableColumn
caclInUpcCLP0DiscCells = _CaclInUpcCLP0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 15),
    _CaclInUpcCLP0DiscCells_Type()
)
caclInUpcCLP0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInUpcCLP0DiscCells.setStatus("current")
_CaclInUpcTotalDiscCells_Type = Counter32
_CaclInUpcTotalDiscCells_Object = MibTableColumn
caclInUpcTotalDiscCells = _CaclInUpcTotalDiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 16),
    _CaclInUpcTotalDiscCells_Type()
)
caclInUpcTotalDiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInUpcTotalDiscCells.setStatus("current")
_CaclInUpcTotalNonCompCells_Type = Counter32
_CaclInUpcTotalNonCompCells_Object = MibTableColumn
caclInUpcTotalNonCompCells = _CaclInUpcTotalNonCompCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 17),
    _CaclInUpcTotalNonCompCells_Type()
)
caclInUpcTotalNonCompCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclInUpcTotalNonCompCells.setStatus("current")
_CaclOutXmtCLP0Cells_Type = Counter32
_CaclOutXmtCLP0Cells_Object = MibTableColumn
caclOutXmtCLP0Cells = _CaclOutXmtCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 18),
    _CaclOutXmtCLP0Cells_Type()
)
caclOutXmtCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclOutXmtCLP0Cells.setStatus("current")
_CaclOutXmtCLP1Cells_Type = Counter32
_CaclOutXmtCLP1Cells_Object = MibTableColumn
caclOutXmtCLP1Cells = _CaclOutXmtCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 19),
    _CaclOutXmtCLP1Cells_Type()
)
caclOutXmtCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclOutXmtCLP1Cells.setStatus("current")
_CaclOutValidOAMCells_Type = Counter32
_CaclOutValidOAMCells_Object = MibTableColumn
caclOutValidOAMCells = _CaclOutValidOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 20),
    _CaclOutValidOAMCells_Type()
)
caclOutValidOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclOutValidOAMCells.setStatus("current")
_CaclOutErrOAMCells_Type = Counter32
_CaclOutErrOAMCells_Object = MibTableColumn
caclOutErrOAMCells = _CaclOutErrOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 21),
    _CaclOutErrOAMCells_Type()
)
caclOutErrOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclOutErrOAMCells.setStatus("current")
_CaclOutVpiVciErrCells_Type = Counter32
_CaclOutVpiVciErrCells_Object = MibTableColumn
caclOutVpiVciErrCells = _CaclOutVpiVciErrCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 22),
    _CaclOutVpiVciErrCells_Type()
)
caclOutVpiVciErrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclOutVpiVciErrCells.setStatus("current")
_CaclOutRcvCLP0Cells_Type = Counter32
_CaclOutRcvCLP0Cells_Object = MibTableColumn
caclOutRcvCLP0Cells = _CaclOutRcvCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 23),
    _CaclOutRcvCLP0Cells_Type()
)
caclOutRcvCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclOutRcvCLP0Cells.setStatus("current")
_CaclOutRcvCLP1Cells_Type = Counter32
_CaclOutRcvCLP1Cells_Object = MibTableColumn
caclOutRcvCLP1Cells = _CaclOutRcvCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 24),
    _CaclOutRcvCLP1Cells_Type()
)
caclOutRcvCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclOutRcvCLP1Cells.setStatus("current")
_CaclOutRcvValidRMCells_Type = Counter32
_CaclOutRcvValidRMCells_Object = MibTableColumn
caclOutRcvValidRMCells = _CaclOutRcvValidRMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 25),
    _CaclOutRcvValidRMCells_Type()
)
caclOutRcvValidRMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclOutRcvValidRMCells.setStatus("current")
_CaclOutRcvIdleCells_Type = Counter32
_CaclOutRcvIdleCells_Object = MibTableColumn
caclOutRcvIdleCells = _CaclOutRcvIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 26),
    _CaclOutRcvIdleCells_Type()
)
caclOutRcvIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclOutRcvIdleCells.setStatus("current")
_CaclHInRcvCLP0Cells_Type = Counter64
_CaclHInRcvCLP0Cells_Object = MibTableColumn
caclHInRcvCLP0Cells = _CaclHInRcvCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 27),
    _CaclHInRcvCLP0Cells_Type()
)
caclHInRcvCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHInRcvCLP0Cells.setStatus("current")
_CaclHInRcvCLP1Cells_Type = Counter64
_CaclHInRcvCLP1Cells_Object = MibTableColumn
caclHInRcvCLP1Cells = _CaclHInRcvCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 28),
    _CaclHInRcvCLP1Cells_Type()
)
caclHInRcvCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHInRcvCLP1Cells.setStatus("current")
_CaclHOutXmtCLP0Cells_Type = Counter64
_CaclHOutXmtCLP0Cells_Object = MibTableColumn
caclHOutXmtCLP0Cells = _CaclHOutXmtCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 29),
    _CaclHOutXmtCLP0Cells_Type()
)
caclHOutXmtCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHOutXmtCLP0Cells.setStatus("current")
_CaclHOutXmtCLP1Cells_Type = Counter64
_CaclHOutXmtCLP1Cells_Object = MibTableColumn
caclHOutXmtCLP1Cells = _CaclHOutXmtCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 30),
    _CaclHOutXmtCLP1Cells_Type()
)
caclHOutXmtCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHOutXmtCLP1Cells.setStatus("current")
_CaclHighInRcvCLP0Cells_Type = Counter32
_CaclHighInRcvCLP0Cells_Object = MibTableColumn
caclHighInRcvCLP0Cells = _CaclHighInRcvCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 31),
    _CaclHighInRcvCLP0Cells_Type()
)
caclHighInRcvCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighInRcvCLP0Cells.setStatus("current")
_CaclHighInRcvCLP1Cells_Type = Counter32
_CaclHighInRcvCLP1Cells_Object = MibTableColumn
caclHighInRcvCLP1Cells = _CaclHighInRcvCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 32),
    _CaclHighInRcvCLP1Cells_Type()
)
caclHighInRcvCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighInRcvCLP1Cells.setStatus("current")
_CaclHighInValidOAMCells_Type = Counter32
_CaclHighInValidOAMCells_Object = MibTableColumn
caclHighInValidOAMCells = _CaclHighInValidOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 33),
    _CaclHighInValidOAMCells_Type()
)
caclHighInValidOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighInValidOAMCells.setStatus("current")
_CaclHighInVpiVciErrCells_Type = Counter32
_CaclHighInVpiVciErrCells_Object = MibTableColumn
caclHighInVpiVciErrCells = _CaclHighInVpiVciErrCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 34),
    _CaclHighInVpiVciErrCells_Type()
)
caclHighInVpiVciErrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighInVpiVciErrCells.setStatus("current")
_CaclHighInXmtCLP0Cells_Type = Counter32
_CaclHighInXmtCLP0Cells_Object = MibTableColumn
caclHighInXmtCLP0Cells = _CaclHighInXmtCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 35),
    _CaclHighInXmtCLP0Cells_Type()
)
caclHighInXmtCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighInXmtCLP0Cells.setStatus("current")
_CaclHighInXmtCLP1Cells_Type = Counter32
_CaclHighInXmtCLP1Cells_Object = MibTableColumn
caclHighInXmtCLP1Cells = _CaclHighInXmtCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 36),
    _CaclHighInXmtCLP1Cells_Type()
)
caclHighInXmtCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighInXmtCLP1Cells.setStatus("current")
_CaclHighInHecErrDiscCells_Type = Counter32
_CaclHighInHecErrDiscCells_Object = MibTableColumn
caclHighInHecErrDiscCells = _CaclHighInHecErrDiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 37),
    _CaclHighInHecErrDiscCells_Type()
)
caclHighInHecErrDiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighInHecErrDiscCells.setStatus("current")
_CaclHighInHecErrCorrectedCells_Type = Counter32
_CaclHighInHecErrCorrectedCells_Object = MibTableColumn
caclHighInHecErrCorrectedCells = _CaclHighInHecErrCorrectedCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 38),
    _CaclHighInHecErrCorrectedCells_Type()
)
caclHighInHecErrCorrectedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighInHecErrCorrectedCells.setStatus("current")
_CaclHighOutXmtCLP0Cells_Type = Counter32
_CaclHighOutXmtCLP0Cells_Object = MibTableColumn
caclHighOutXmtCLP0Cells = _CaclHighOutXmtCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 39),
    _CaclHighOutXmtCLP0Cells_Type()
)
caclHighOutXmtCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighOutXmtCLP0Cells.setStatus("current")
_CaclHighOutXmtCLP1Cells_Type = Counter32
_CaclHighOutXmtCLP1Cells_Object = MibTableColumn
caclHighOutXmtCLP1Cells = _CaclHighOutXmtCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 40),
    _CaclHighOutXmtCLP1Cells_Type()
)
caclHighOutXmtCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighOutXmtCLP1Cells.setStatus("current")
_CaclHighOutValidOAMCells_Type = Counter32
_CaclHighOutValidOAMCells_Object = MibTableColumn
caclHighOutValidOAMCells = _CaclHighOutValidOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 41),
    _CaclHighOutValidOAMCells_Type()
)
caclHighOutValidOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighOutValidOAMCells.setStatus("current")
_CaclHighOutRcvCLP0Cells_Type = Counter32
_CaclHighOutRcvCLP0Cells_Object = MibTableColumn
caclHighOutRcvCLP0Cells = _CaclHighOutRcvCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 42),
    _CaclHighOutRcvCLP0Cells_Type()
)
caclHighOutRcvCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighOutRcvCLP0Cells.setStatus("current")
_CaclHighOutRcvCLP1Cells_Type = Counter32
_CaclHighOutRcvCLP1Cells_Object = MibTableColumn
caclHighOutRcvCLP1Cells = _CaclHighOutRcvCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 1, 1, 43),
    _CaclHighOutRcvCLP1Cells_Type()
)
caclHighOutRcvCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighOutRcvCLP1Cells.setStatus("current")
_CaclIntervalStatsTable_Object = MibTable
caclIntervalStatsTable = _CaclIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2)
)
if mibBuilder.loadTexts:
    caclIntervalStatsTable.setStatus("current")
_CaclIntervalStatsEntry_Object = MibTableRow
caclIntervalStatsEntry = _CaclIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1)
)
caclIntervalStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-CELL-LAYER-MIB", "caclIntervalNumber"),
)
if mibBuilder.loadTexts:
    caclIntervalStatsEntry.setStatus("current")


class _CaclIntervalNumber_Type(Integer32):
    """Custom type caclIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CaclIntervalNumber_Type.__name__ = "Integer32"
_CaclIntervalNumber_Object = MibTableColumn
caclIntervalNumber = _CaclIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 1),
    _CaclIntervalNumber_Type()
)
caclIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caclIntervalNumber.setStatus("current")
_CaclIntervalInRcvCLP0Cells_Type = Gauge32
_CaclIntervalInRcvCLP0Cells_Object = MibTableColumn
caclIntervalInRcvCLP0Cells = _CaclIntervalInRcvCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 2),
    _CaclIntervalInRcvCLP0Cells_Type()
)
caclIntervalInRcvCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInRcvCLP0Cells.setStatus("current")
_CaclIntervalInRcvCLP1Cells_Type = Gauge32
_CaclIntervalInRcvCLP1Cells_Object = MibTableColumn
caclIntervalInRcvCLP1Cells = _CaclIntervalInRcvCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 3),
    _CaclIntervalInRcvCLP1Cells_Type()
)
caclIntervalInRcvCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInRcvCLP1Cells.setStatus("current")
_CaclIntervalInValidOAMCells_Type = Gauge32
_CaclIntervalInValidOAMCells_Object = MibTableColumn
caclIntervalInValidOAMCells = _CaclIntervalInValidOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 4),
    _CaclIntervalInValidOAMCells_Type()
)
caclIntervalInValidOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInValidOAMCells.setStatus("current")
_CaclIntervalInErrOAMCells_Type = Gauge32
_CaclIntervalInErrOAMCells_Object = MibTableColumn
caclIntervalInErrOAMCells = _CaclIntervalInErrOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 5),
    _CaclIntervalInErrOAMCells_Type()
)
caclIntervalInErrOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInErrOAMCells.setStatus("current")
_CaclIntervalInGfcCells_Type = Gauge32
_CaclIntervalInGfcCells_Object = MibTableColumn
caclIntervalInGfcCells = _CaclIntervalInGfcCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 6),
    _CaclIntervalInGfcCells_Type()
)
caclIntervalInGfcCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInGfcCells.setStatus("current")
_CaclIntervalInVpiVciErrCells_Type = Gauge32
_CaclIntervalInVpiVciErrCells_Object = MibTableColumn
caclIntervalInVpiVciErrCells = _CaclIntervalInVpiVciErrCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 7),
    _CaclIntervalInVpiVciErrCells_Type()
)
caclIntervalInVpiVciErrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInVpiVciErrCells.setStatus("current")


class _CaclIntervalInLastUnknVpi_Type(Integer32):
    """Custom type caclIntervalInLastUnknVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CaclIntervalInLastUnknVpi_Type.__name__ = "Integer32"
_CaclIntervalInLastUnknVpi_Object = MibTableColumn
caclIntervalInLastUnknVpi = _CaclIntervalInLastUnknVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 8),
    _CaclIntervalInLastUnknVpi_Type()
)
caclIntervalInLastUnknVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInLastUnknVpi.setStatus("current")


class _CaclIntervalInLastUnknVci_Type(Integer32):
    """Custom type caclIntervalInLastUnknVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaclIntervalInLastUnknVci_Type.__name__ = "Integer32"
_CaclIntervalInLastUnknVci_Object = MibTableColumn
caclIntervalInLastUnknVci = _CaclIntervalInLastUnknVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 9),
    _CaclIntervalInLastUnknVci_Type()
)
caclIntervalInLastUnknVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInLastUnknVci.setStatus("current")
_CaclIntervalInXmtCLP0Cells_Type = Gauge32
_CaclIntervalInXmtCLP0Cells_Object = MibTableColumn
caclIntervalInXmtCLP0Cells = _CaclIntervalInXmtCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 10),
    _CaclIntervalInXmtCLP0Cells_Type()
)
caclIntervalInXmtCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInXmtCLP0Cells.setStatus("current")
_CaclIntervalInXmtCLP1Cells_Type = Gauge32
_CaclIntervalInXmtCLP1Cells_Object = MibTableColumn
caclIntervalInXmtCLP1Cells = _CaclIntervalInXmtCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 11),
    _CaclIntervalInXmtCLP1Cells_Type()
)
caclIntervalInXmtCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInXmtCLP1Cells.setStatus("current")
_CaclIntervalInValidRMCells_Type = Gauge32
_CaclIntervalInValidRMCells_Object = MibTableColumn
caclIntervalInValidRMCells = _CaclIntervalInValidRMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 12),
    _CaclIntervalInValidRMCells_Type()
)
caclIntervalInValidRMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInValidRMCells.setStatus("current")
_CaclIntervalInRcvIdleCells_Type = Gauge32
_CaclIntervalInRcvIdleCells_Object = MibTableColumn
caclIntervalInRcvIdleCells = _CaclIntervalInRcvIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 13),
    _CaclIntervalInRcvIdleCells_Type()
)
caclIntervalInRcvIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInRcvIdleCells.setStatus("current")
_CaclIntervalInHecErrDiscCells_Type = Gauge32
_CaclIntervalInHecErrDiscCells_Object = MibTableColumn
caclIntervalInHecErrDiscCells = _CaclIntervalInHecErrDiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 14),
    _CaclIntervalInHecErrDiscCells_Type()
)
caclIntervalInHecErrDiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInHecErrDiscCells.setStatus("current")
_CaclIntervalInHecErrCorrCells_Type = Gauge32
_CaclIntervalInHecErrCorrCells_Object = MibTableColumn
caclIntervalInHecErrCorrCells = _CaclIntervalInHecErrCorrCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 15),
    _CaclIntervalInHecErrCorrCells_Type()
)
caclIntervalInHecErrCorrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInHecErrCorrCells.setStatus("current")
_CaclIntervalInUpcCLP0DiscCells_Type = Gauge32
_CaclIntervalInUpcCLP0DiscCells_Object = MibTableColumn
caclIntervalInUpcCLP0DiscCells = _CaclIntervalInUpcCLP0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 16),
    _CaclIntervalInUpcCLP0DiscCells_Type()
)
caclIntervalInUpcCLP0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInUpcCLP0DiscCells.setStatus("current")
_CaclIntervalInUpcTotalDiscCells_Type = Gauge32
_CaclIntervalInUpcTotalDiscCells_Object = MibTableColumn
caclIntervalInUpcTotalDiscCells = _CaclIntervalInUpcTotalDiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 17),
    _CaclIntervalInUpcTotalDiscCells_Type()
)
caclIntervalInUpcTotalDiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInUpcTotalDiscCells.setStatus("current")
_CaclIntervalInUpcTotNonCmpCells_Type = Gauge32
_CaclIntervalInUpcTotNonCmpCells_Object = MibTableColumn
caclIntervalInUpcTotNonCmpCells = _CaclIntervalInUpcTotNonCmpCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 18),
    _CaclIntervalInUpcTotNonCmpCells_Type()
)
caclIntervalInUpcTotNonCmpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalInUpcTotNonCmpCells.setStatus("current")
_CaclIntervalOutXmtCLP0Cells_Type = Gauge32
_CaclIntervalOutXmtCLP0Cells_Object = MibTableColumn
caclIntervalOutXmtCLP0Cells = _CaclIntervalOutXmtCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 19),
    _CaclIntervalOutXmtCLP0Cells_Type()
)
caclIntervalOutXmtCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalOutXmtCLP0Cells.setStatus("current")
_CaclIntervalOutXmtCLP1Cells_Type = Gauge32
_CaclIntervalOutXmtCLP1Cells_Object = MibTableColumn
caclIntervalOutXmtCLP1Cells = _CaclIntervalOutXmtCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 20),
    _CaclIntervalOutXmtCLP1Cells_Type()
)
caclIntervalOutXmtCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalOutXmtCLP1Cells.setStatus("current")
_CaclIntervalOutValidOAMCells_Type = Gauge32
_CaclIntervalOutValidOAMCells_Object = MibTableColumn
caclIntervalOutValidOAMCells = _CaclIntervalOutValidOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 21),
    _CaclIntervalOutValidOAMCells_Type()
)
caclIntervalOutValidOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalOutValidOAMCells.setStatus("current")
_CaclIntervalOutErrOAMCells_Type = Gauge32
_CaclIntervalOutErrOAMCells_Object = MibTableColumn
caclIntervalOutErrOAMCells = _CaclIntervalOutErrOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 22),
    _CaclIntervalOutErrOAMCells_Type()
)
caclIntervalOutErrOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalOutErrOAMCells.setStatus("current")
_CaclIntervalOutVpiVciErrCells_Type = Gauge32
_CaclIntervalOutVpiVciErrCells_Object = MibTableColumn
caclIntervalOutVpiVciErrCells = _CaclIntervalOutVpiVciErrCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 23),
    _CaclIntervalOutVpiVciErrCells_Type()
)
caclIntervalOutVpiVciErrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalOutVpiVciErrCells.setStatus("current")
_CaclIntervalOutRcvCLP0Cells_Type = Gauge32
_CaclIntervalOutRcvCLP0Cells_Object = MibTableColumn
caclIntervalOutRcvCLP0Cells = _CaclIntervalOutRcvCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 24),
    _CaclIntervalOutRcvCLP0Cells_Type()
)
caclIntervalOutRcvCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalOutRcvCLP0Cells.setStatus("current")
_CaclIntervalOutRcvCLP1Cells_Type = Gauge32
_CaclIntervalOutRcvCLP1Cells_Object = MibTableColumn
caclIntervalOutRcvCLP1Cells = _CaclIntervalOutRcvCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 25),
    _CaclIntervalOutRcvCLP1Cells_Type()
)
caclIntervalOutRcvCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalOutRcvCLP1Cells.setStatus("current")
_CaclIntervalOutRcvValidRMCells_Type = Gauge32
_CaclIntervalOutRcvValidRMCells_Object = MibTableColumn
caclIntervalOutRcvValidRMCells = _CaclIntervalOutRcvValidRMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 26),
    _CaclIntervalOutRcvValidRMCells_Type()
)
caclIntervalOutRcvValidRMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalOutRcvValidRMCells.setStatus("current")
_CaclIntervalOutRcvIdleCells_Type = Gauge32
_CaclIntervalOutRcvIdleCells_Object = MibTableColumn
caclIntervalOutRcvIdleCells = _CaclIntervalOutRcvIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 27),
    _CaclIntervalOutRcvIdleCells_Type()
)
caclIntervalOutRcvIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclIntervalOutRcvIdleCells.setStatus("current")
_CaclHighIntervalInRcvCLP0Cells_Type = Gauge32
_CaclHighIntervalInRcvCLP0Cells_Object = MibTableColumn
caclHighIntervalInRcvCLP0Cells = _CaclHighIntervalInRcvCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 28),
    _CaclHighIntervalInRcvCLP0Cells_Type()
)
caclHighIntervalInRcvCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighIntervalInRcvCLP0Cells.setStatus("current")
_CaclHighIntervalInRcvCLP1Cells_Type = Gauge32
_CaclHighIntervalInRcvCLP1Cells_Object = MibTableColumn
caclHighIntervalInRcvCLP1Cells = _CaclHighIntervalInRcvCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 29),
    _CaclHighIntervalInRcvCLP1Cells_Type()
)
caclHighIntervalInRcvCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighIntervalInRcvCLP1Cells.setStatus("current")
_CaclHighIntervalInVpiVciErrCells_Type = Gauge32
_CaclHighIntervalInVpiVciErrCells_Object = MibTableColumn
caclHighIntervalInVpiVciErrCells = _CaclHighIntervalInVpiVciErrCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 30),
    _CaclHighIntervalInVpiVciErrCells_Type()
)
caclHighIntervalInVpiVciErrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighIntervalInVpiVciErrCells.setStatus("current")
_CaclHighIntervalInXmtCLP0Cells_Type = Gauge32
_CaclHighIntervalInXmtCLP0Cells_Object = MibTableColumn
caclHighIntervalInXmtCLP0Cells = _CaclHighIntervalInXmtCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 31),
    _CaclHighIntervalInXmtCLP0Cells_Type()
)
caclHighIntervalInXmtCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighIntervalInXmtCLP0Cells.setStatus("current")
_CaclHighIntervalInXmtCLP1Cells_Type = Gauge32
_CaclHighIntervalInXmtCLP1Cells_Object = MibTableColumn
caclHighIntervalInXmtCLP1Cells = _CaclHighIntervalInXmtCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 32),
    _CaclHighIntervalInXmtCLP1Cells_Type()
)
caclHighIntervalInXmtCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighIntervalInXmtCLP1Cells.setStatus("current")
_CaclHighIntervalInHecErrDiscCells_Type = Gauge32
_CaclHighIntervalInHecErrDiscCells_Object = MibTableColumn
caclHighIntervalInHecErrDiscCells = _CaclHighIntervalInHecErrDiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 33),
    _CaclHighIntervalInHecErrDiscCells_Type()
)
caclHighIntervalInHecErrDiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighIntervalInHecErrDiscCells.setStatus("current")
_CaclHighIntervalInHecErrCorrCells_Type = Gauge32
_CaclHighIntervalInHecErrCorrCells_Object = MibTableColumn
caclHighIntervalInHecErrCorrCells = _CaclHighIntervalInHecErrCorrCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 34),
    _CaclHighIntervalInHecErrCorrCells_Type()
)
caclHighIntervalInHecErrCorrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighIntervalInHecErrCorrCells.setStatus("current")
_CaclHighIntervalOutXmtCLP0Cells_Type = Gauge32
_CaclHighIntervalOutXmtCLP0Cells_Object = MibTableColumn
caclHighIntervalOutXmtCLP0Cells = _CaclHighIntervalOutXmtCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 35),
    _CaclHighIntervalOutXmtCLP0Cells_Type()
)
caclHighIntervalOutXmtCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighIntervalOutXmtCLP0Cells.setStatus("current")
_CaclHighIntervalOutXmtCLP1Cells_Type = Gauge32
_CaclHighIntervalOutXmtCLP1Cells_Object = MibTableColumn
caclHighIntervalOutXmtCLP1Cells = _CaclHighIntervalOutXmtCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 36),
    _CaclHighIntervalOutXmtCLP1Cells_Type()
)
caclHighIntervalOutXmtCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighIntervalOutXmtCLP1Cells.setStatus("current")
_CaclHighIntervalOutVpiVciErrCells_Type = Gauge32
_CaclHighIntervalOutVpiVciErrCells_Object = MibTableColumn
caclHighIntervalOutVpiVciErrCells = _CaclHighIntervalOutVpiVciErrCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 37),
    _CaclHighIntervalOutVpiVciErrCells_Type()
)
caclHighIntervalOutVpiVciErrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighIntervalOutVpiVciErrCells.setStatus("current")
_CaclHighIntervalOutRcvCLP0Cells_Type = Gauge32
_CaclHighIntervalOutRcvCLP0Cells_Object = MibTableColumn
caclHighIntervalOutRcvCLP0Cells = _CaclHighIntervalOutRcvCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 38),
    _CaclHighIntervalOutRcvCLP0Cells_Type()
)
caclHighIntervalOutRcvCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighIntervalOutRcvCLP0Cells.setStatus("current")
_CaclHighIntervalOutRcvCLP1Cells_Type = Gauge32
_CaclHighIntervalOutRcvCLP1Cells_Object = MibTableColumn
caclHighIntervalOutRcvCLP1Cells = _CaclHighIntervalOutRcvCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 2, 1, 39),
    _CaclHighIntervalOutRcvCLP1Cells_Type()
)
caclHighIntervalOutRcvCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHighIntervalOutRcvCLP1Cells.setStatus("current")
_CaclXStatsTable_Object = MibTable
caclXStatsTable = _CaclXStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 3)
)
if mibBuilder.loadTexts:
    caclXStatsTable.setStatus("current")
_CaclXStatsEntry_Object = MibTableRow
caclXStatsEntry = _CaclXStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    caclXStatsEntry.setStatus("current")
_CaclHCInValidOAMCells_Type = Counter64
_CaclHCInValidOAMCells_Object = MibTableColumn
caclHCInValidOAMCells = _CaclHCInValidOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 3, 1, 1),
    _CaclHCInValidOAMCells_Type()
)
caclHCInValidOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCInValidOAMCells.setStatus("current")
_CaclHCInVpiVciErrCells_Type = Counter64
_CaclHCInVpiVciErrCells_Object = MibTableColumn
caclHCInVpiVciErrCells = _CaclHCInVpiVciErrCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 3, 1, 2),
    _CaclHCInVpiVciErrCells_Type()
)
caclHCInVpiVciErrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCInVpiVciErrCells.setStatus("current")
_CaclHCInXmtCLP0Cells_Type = Counter64
_CaclHCInXmtCLP0Cells_Object = MibTableColumn
caclHCInXmtCLP0Cells = _CaclHCInXmtCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 3, 1, 3),
    _CaclHCInXmtCLP0Cells_Type()
)
caclHCInXmtCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCInXmtCLP0Cells.setStatus("current")
_CaclHCInXmtCLP1Cells_Type = Counter64
_CaclHCInXmtCLP1Cells_Object = MibTableColumn
caclHCInXmtCLP1Cells = _CaclHCInXmtCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 3, 1, 4),
    _CaclHCInXmtCLP1Cells_Type()
)
caclHCInXmtCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCInXmtCLP1Cells.setStatus("current")
_CaclHCInHecErrDiscCells_Type = Counter64
_CaclHCInHecErrDiscCells_Object = MibTableColumn
caclHCInHecErrDiscCells = _CaclHCInHecErrDiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 3, 1, 5),
    _CaclHCInHecErrDiscCells_Type()
)
caclHCInHecErrDiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCInHecErrDiscCells.setStatus("current")
_CaclHCInHecErrCorrectedCells_Type = Counter64
_CaclHCInHecErrCorrectedCells_Object = MibTableColumn
caclHCInHecErrCorrectedCells = _CaclHCInHecErrCorrectedCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 3, 1, 6),
    _CaclHCInHecErrCorrectedCells_Type()
)
caclHCInHecErrCorrectedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCInHecErrCorrectedCells.setStatus("current")
_CaclHCOutValidOAMCells_Type = Counter64
_CaclHCOutValidOAMCells_Object = MibTableColumn
caclHCOutValidOAMCells = _CaclHCOutValidOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 3, 1, 7),
    _CaclHCOutValidOAMCells_Type()
)
caclHCOutValidOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCOutValidOAMCells.setStatus("current")
_CaclHCOutRcvCLP0Cells_Type = Counter64
_CaclHCOutRcvCLP0Cells_Object = MibTableColumn
caclHCOutRcvCLP0Cells = _CaclHCOutRcvCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 3, 1, 8),
    _CaclHCOutRcvCLP0Cells_Type()
)
caclHCOutRcvCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCOutRcvCLP0Cells.setStatus("current")
_CaclHCOutRcvCLP1Cells_Type = Counter64
_CaclHCOutRcvCLP1Cells_Object = MibTableColumn
caclHCOutRcvCLP1Cells = _CaclHCOutRcvCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 3, 1, 9),
    _CaclHCOutRcvCLP1Cells_Type()
)
caclHCOutRcvCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCOutRcvCLP1Cells.setStatus("current")
_CaclXIntervalStatsTable_Object = MibTable
caclXIntervalStatsTable = _CaclXIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 4)
)
if mibBuilder.loadTexts:
    caclXIntervalStatsTable.setStatus("current")
_CaclXIntervalStatsEntry_Object = MibTableRow
caclXIntervalStatsEntry = _CaclXIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 4, 1)
)
caclXIntervalStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-CELL-LAYER-MIB", "caclIntervalNumber"),
)
if mibBuilder.loadTexts:
    caclXIntervalStatsEntry.setStatus("current")
_CaclHCIntervalInRcvCLP0Cells_Type = Counter64
_CaclHCIntervalInRcvCLP0Cells_Object = MibTableColumn
caclHCIntervalInRcvCLP0Cells = _CaclHCIntervalInRcvCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 4, 1, 1),
    _CaclHCIntervalInRcvCLP0Cells_Type()
)
caclHCIntervalInRcvCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCIntervalInRcvCLP0Cells.setStatus("current")
_CaclHCIntervalInRcvCLP1Cells_Type = Counter64
_CaclHCIntervalInRcvCLP1Cells_Object = MibTableColumn
caclHCIntervalInRcvCLP1Cells = _CaclHCIntervalInRcvCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 4, 1, 2),
    _CaclHCIntervalInRcvCLP1Cells_Type()
)
caclHCIntervalInRcvCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCIntervalInRcvCLP1Cells.setStatus("current")
_CaclHCIntervalInVpiVciErrCells_Type = Counter64
_CaclHCIntervalInVpiVciErrCells_Object = MibTableColumn
caclHCIntervalInVpiVciErrCells = _CaclHCIntervalInVpiVciErrCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 4, 1, 3),
    _CaclHCIntervalInVpiVciErrCells_Type()
)
caclHCIntervalInVpiVciErrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCIntervalInVpiVciErrCells.setStatus("current")
_CaclHCIntervalInXmtCLP0Cells_Type = Counter64
_CaclHCIntervalInXmtCLP0Cells_Object = MibTableColumn
caclHCIntervalInXmtCLP0Cells = _CaclHCIntervalInXmtCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 4, 1, 4),
    _CaclHCIntervalInXmtCLP0Cells_Type()
)
caclHCIntervalInXmtCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCIntervalInXmtCLP0Cells.setStatus("current")
_CaclHCIntervalInXmtCLP1Cells_Type = Counter64
_CaclHCIntervalInXmtCLP1Cells_Object = MibTableColumn
caclHCIntervalInXmtCLP1Cells = _CaclHCIntervalInXmtCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 4, 1, 5),
    _CaclHCIntervalInXmtCLP1Cells_Type()
)
caclHCIntervalInXmtCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCIntervalInXmtCLP1Cells.setStatus("current")
_CaclHCIntervalInHecErrDiscCells_Type = Counter64
_CaclHCIntervalInHecErrDiscCells_Object = MibTableColumn
caclHCIntervalInHecErrDiscCells = _CaclHCIntervalInHecErrDiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 4, 1, 6),
    _CaclHCIntervalInHecErrDiscCells_Type()
)
caclHCIntervalInHecErrDiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCIntervalInHecErrDiscCells.setStatus("current")
_CaclHCIntervalInHecErrCorrCells_Type = Counter64
_CaclHCIntervalInHecErrCorrCells_Object = MibTableColumn
caclHCIntervalInHecErrCorrCells = _CaclHCIntervalInHecErrCorrCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 4, 1, 7),
    _CaclHCIntervalInHecErrCorrCells_Type()
)
caclHCIntervalInHecErrCorrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCIntervalInHecErrCorrCells.setStatus("current")
_CaclHCIntervalOutXmtCLP0Cells_Type = Counter64
_CaclHCIntervalOutXmtCLP0Cells_Object = MibTableColumn
caclHCIntervalOutXmtCLP0Cells = _CaclHCIntervalOutXmtCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 4, 1, 8),
    _CaclHCIntervalOutXmtCLP0Cells_Type()
)
caclHCIntervalOutXmtCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCIntervalOutXmtCLP0Cells.setStatus("current")
_CaclHCIntervalOutXmtCLP1Cells_Type = Counter64
_CaclHCIntervalOutXmtCLP1Cells_Object = MibTableColumn
caclHCIntervalOutXmtCLP1Cells = _CaclHCIntervalOutXmtCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 4, 1, 9),
    _CaclHCIntervalOutXmtCLP1Cells_Type()
)
caclHCIntervalOutXmtCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCIntervalOutXmtCLP1Cells.setStatus("current")
_CaclHCIntervalOutVpiVciErrCells_Type = Counter64
_CaclHCIntervalOutVpiVciErrCells_Object = MibTableColumn
caclHCIntervalOutVpiVciErrCells = _CaclHCIntervalOutVpiVciErrCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 4, 1, 10),
    _CaclHCIntervalOutVpiVciErrCells_Type()
)
caclHCIntervalOutVpiVciErrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCIntervalOutVpiVciErrCells.setStatus("current")
_CaclHCIntervalOutRcvCLP0Cells_Type = Counter64
_CaclHCIntervalOutRcvCLP0Cells_Object = MibTableColumn
caclHCIntervalOutRcvCLP0Cells = _CaclHCIntervalOutRcvCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 4, 1, 11),
    _CaclHCIntervalOutRcvCLP0Cells_Type()
)
caclHCIntervalOutRcvCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCIntervalOutRcvCLP0Cells.setStatus("current")
_CaclHCIntervalOutRcvCLP1Cells_Type = Counter64
_CaclHCIntervalOutRcvCLP1Cells_Object = MibTableColumn
caclHCIntervalOutRcvCLP1Cells = _CaclHCIntervalOutRcvCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 2, 4, 1, 12),
    _CaclHCIntervalOutRcvCLP1Cells_Type()
)
caclHCIntervalOutRcvCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caclHCIntervalOutRcvCLP1Cells.setStatus("current")
_CaclMIBConformance_ObjectIdentity = ObjectIdentity
caclMIBConformance = _CaclMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3)
)
_CaclMIBCompliances_ObjectIdentity = ObjectIdentity
caclMIBCompliances = _CaclMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3, 1)
)
_CaclMIBGroups_ObjectIdentity = ObjectIdentity
caclMIBGroups = _CaclMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3, 2)
)
caclStatsEntry.registerAugmentions(
    ("CISCO-ATM-CELL-LAYER-MIB",
     "caclXStatsEntry")
)
caclXStatsEntry.setIndexNames(*caclStatsEntry.getIndexNames())

# Managed Objects groups

caclMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3, 2, 1)
)
caclMIBGroup.setObjects(
      *(("CISCO-ATM-CELL-LAYER-MIB", "caclNullCellHeader"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclNullCellPayload"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHecCosetEnable"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclPayloadScramblingEnable"))
)
if mibBuilder.loadTexts:
    caclMIBGroup.setStatus("current")

caclATMSwitchStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3, 2, 2)
)
caclATMSwitchStatsMIBGroup.setObjects(
      *(("CISCO-ATM-CELL-LAYER-MIB", "caclInRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInRcvCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInValidOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInErrOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInGfcCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInLastUnknVpi"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInLastUnknVci"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInValidRMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInRcvIdleCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInHecErrDiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInHecErrCorrectedCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInUpcCLP0DiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInUpcTotalDiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInUpcTotalNonCompCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutValidOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutErrOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutRcvCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutRcvValidRMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutRcvIdleCells"))
)
if mibBuilder.loadTexts:
    caclATMSwitchStatsMIBGroup.setStatus("deprecated")

caclATMEndSyatemStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3, 2, 3)
)
caclATMEndSyatemStatsMIBGroup.setObjects(
      *(("CISCO-ATM-CELL-LAYER-MIB", "caclInRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInRcvCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInValidOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInErrOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInGfcCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInLastUnknVpi"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInLastUnknVci"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInValidRMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInRcvIdleCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInHecErrDiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInHecErrCorrectedCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInUpcCLP0DiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInUpcTotalDiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInUpcTotalNonCompCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutValidOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutErrOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutVpiVciErrCells"))
)
if mibBuilder.loadTexts:
    caclATMEndSyatemStatsMIBGroup.setStatus("deprecated")

caclHighSpeedATMMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3, 2, 4)
)
caclHighSpeedATMMIBGroup.setObjects(
      *(("CISCO-ATM-CELL-LAYER-MIB", "caclHInRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHInRcvCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHOutXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHOutXmtCLP1Cells"))
)
if mibBuilder.loadTexts:
    caclHighSpeedATMMIBGroup.setStatus("deprecated")

caclIntervalStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3, 2, 5)
)
caclIntervalStatsMIBGroup.setObjects(
      *(("CISCO-ATM-CELL-LAYER-MIB", "caclTimeElapsed"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclValidIntervals"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInvalidIntervals"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInRcvCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInValidOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInErrOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInGfcCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInLastUnknVpi"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInLastUnknVci"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInValidRMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInRcvIdleCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInHecErrDiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInHecErrCorrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInUpcCLP0DiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInUpcTotalDiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInUpcTotNonCmpCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutValidOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutErrOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutRcvCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutRcvValidRMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutRcvIdleCells"))
)
if mibBuilder.loadTexts:
    caclIntervalStatsMIBGroup.setStatus("deprecated")

caclATMSwitchStatsMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3, 2, 6)
)
caclATMSwitchStatsMIBGroup1.setObjects(
      *(("CISCO-ATM-CELL-LAYER-MIB", "caclInXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutRcvCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutRcvValidRMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutRcvIdleCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighInXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighInXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighOutRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighOutRcvCLP1Cells"))
)
if mibBuilder.loadTexts:
    caclATMSwitchStatsMIBGroup1.setStatus("current")

caclATMStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3, 2, 7)
)
caclATMStatsMIBGroup.setObjects(
      *(("CISCO-ATM-CELL-LAYER-MIB", "caclInRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInRcvCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInValidOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInErrOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInGfcCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInLastUnknVpi"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInLastUnknVci"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInValidRMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInRcvIdleCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInHecErrDiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInHecErrCorrectedCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInUpcCLP0DiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInUpcTotalDiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInUpcTotalNonCompCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutValidOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutErrOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclOutVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighInRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighInRcvCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighInValidOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighInVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighInHecErrDiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighInHecErrCorrectedCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighOutXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighOutXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighOutValidOAMCells"))
)
if mibBuilder.loadTexts:
    caclATMStatsMIBGroup.setStatus("current")

caclHighSpeedATMMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3, 2, 8)
)
caclHighSpeedATMMIBGroup1.setObjects(
      *(("CISCO-ATM-CELL-LAYER-MIB", "caclHInRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHInRcvCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHOutXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHOutXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCInValidOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCInVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCInXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCInXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCInHecErrDiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCInHecErrCorrectedCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCOutValidOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCOutRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCOutRcvCLP1Cells"))
)
if mibBuilder.loadTexts:
    caclHighSpeedATMMIBGroup1.setStatus("current")

caclIntervalStatsMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3, 2, 9)
)
caclIntervalStatsMIBGroup1.setObjects(
      *(("CISCO-ATM-CELL-LAYER-MIB", "caclTimeElapsed"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclValidIntervals"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclInvalidIntervals"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInRcvCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInValidOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInErrOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInGfcCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInLastUnknVpi"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInLastUnknVci"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInValidRMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInRcvIdleCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInHecErrDiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInHecErrCorrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInUpcCLP0DiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInUpcTotalDiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalInUpcTotNonCmpCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutValidOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutErrOAMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutRcvCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutRcvValidRMCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclIntervalOutRcvIdleCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighIntervalInRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighIntervalInRcvCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighIntervalInVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighIntervalInXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighIntervalInXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighIntervalInHecErrDiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighIntervalInHecErrCorrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighIntervalOutXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighIntervalOutXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighIntervalOutVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighIntervalOutRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHighIntervalOutRcvCLP1Cells"))
)
if mibBuilder.loadTexts:
    caclIntervalStatsMIBGroup1.setStatus("current")

caclHCIntervalStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3, 2, 10)
)
caclHCIntervalStatsMIBGroup.setObjects(
      *(("CISCO-ATM-CELL-LAYER-MIB", "caclHCIntervalInRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCIntervalInRcvCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCIntervalInVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCIntervalInXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCIntervalInXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCIntervalInHecErrDiscCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCIntervalInHecErrCorrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCIntervalOutXmtCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCIntervalOutXmtCLP1Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCIntervalOutVpiVciErrCells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCIntervalOutRcvCLP0Cells"),
        ("CISCO-ATM-CELL-LAYER-MIB", "caclHCIntervalOutRcvCLP1Cells"))
)
if mibBuilder.loadTexts:
    caclHCIntervalStatsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

caclMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    caclMIBCompliance.setStatus(
        "deprecated"
    )

caclMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 133, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    caclMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-CELL-LAYER-MIB",
    **{"ciscoAtmCellLayerMIB": ciscoAtmCellLayerMIB,
       "ciscoAtmCellLayerMIBObjects": ciscoAtmCellLayerMIBObjects,
       "caclConfig": caclConfig,
       "caclConfigTable": caclConfigTable,
       "caclConfigEntry": caclConfigEntry,
       "caclNullCellHeader": caclNullCellHeader,
       "caclNullCellPayload": caclNullCellPayload,
       "caclHecCosetEnable": caclHecCosetEnable,
       "caclPayloadScramblingEnable": caclPayloadScramblingEnable,
       "caclTimeElapsed": caclTimeElapsed,
       "caclValidIntervals": caclValidIntervals,
       "caclInvalidIntervals": caclInvalidIntervals,
       "caclStats": caclStats,
       "caclStatsTable": caclStatsTable,
       "caclStatsEntry": caclStatsEntry,
       "caclInRcvCLP0Cells": caclInRcvCLP0Cells,
       "caclInRcvCLP1Cells": caclInRcvCLP1Cells,
       "caclInValidOAMCells": caclInValidOAMCells,
       "caclInErrOAMCells": caclInErrOAMCells,
       "caclInGfcCells": caclInGfcCells,
       "caclInVpiVciErrCells": caclInVpiVciErrCells,
       "caclInLastUnknVpi": caclInLastUnknVpi,
       "caclInLastUnknVci": caclInLastUnknVci,
       "caclInXmtCLP0Cells": caclInXmtCLP0Cells,
       "caclInXmtCLP1Cells": caclInXmtCLP1Cells,
       "caclInValidRMCells": caclInValidRMCells,
       "caclInRcvIdleCells": caclInRcvIdleCells,
       "caclInHecErrDiscCells": caclInHecErrDiscCells,
       "caclInHecErrCorrectedCells": caclInHecErrCorrectedCells,
       "caclInUpcCLP0DiscCells": caclInUpcCLP0DiscCells,
       "caclInUpcTotalDiscCells": caclInUpcTotalDiscCells,
       "caclInUpcTotalNonCompCells": caclInUpcTotalNonCompCells,
       "caclOutXmtCLP0Cells": caclOutXmtCLP0Cells,
       "caclOutXmtCLP1Cells": caclOutXmtCLP1Cells,
       "caclOutValidOAMCells": caclOutValidOAMCells,
       "caclOutErrOAMCells": caclOutErrOAMCells,
       "caclOutVpiVciErrCells": caclOutVpiVciErrCells,
       "caclOutRcvCLP0Cells": caclOutRcvCLP0Cells,
       "caclOutRcvCLP1Cells": caclOutRcvCLP1Cells,
       "caclOutRcvValidRMCells": caclOutRcvValidRMCells,
       "caclOutRcvIdleCells": caclOutRcvIdleCells,
       "caclHInRcvCLP0Cells": caclHInRcvCLP0Cells,
       "caclHInRcvCLP1Cells": caclHInRcvCLP1Cells,
       "caclHOutXmtCLP0Cells": caclHOutXmtCLP0Cells,
       "caclHOutXmtCLP1Cells": caclHOutXmtCLP1Cells,
       "caclHighInRcvCLP0Cells": caclHighInRcvCLP0Cells,
       "caclHighInRcvCLP1Cells": caclHighInRcvCLP1Cells,
       "caclHighInValidOAMCells": caclHighInValidOAMCells,
       "caclHighInVpiVciErrCells": caclHighInVpiVciErrCells,
       "caclHighInXmtCLP0Cells": caclHighInXmtCLP0Cells,
       "caclHighInXmtCLP1Cells": caclHighInXmtCLP1Cells,
       "caclHighInHecErrDiscCells": caclHighInHecErrDiscCells,
       "caclHighInHecErrCorrectedCells": caclHighInHecErrCorrectedCells,
       "caclHighOutXmtCLP0Cells": caclHighOutXmtCLP0Cells,
       "caclHighOutXmtCLP1Cells": caclHighOutXmtCLP1Cells,
       "caclHighOutValidOAMCells": caclHighOutValidOAMCells,
       "caclHighOutRcvCLP0Cells": caclHighOutRcvCLP0Cells,
       "caclHighOutRcvCLP1Cells": caclHighOutRcvCLP1Cells,
       "caclIntervalStatsTable": caclIntervalStatsTable,
       "caclIntervalStatsEntry": caclIntervalStatsEntry,
       "caclIntervalNumber": caclIntervalNumber,
       "caclIntervalInRcvCLP0Cells": caclIntervalInRcvCLP0Cells,
       "caclIntervalInRcvCLP1Cells": caclIntervalInRcvCLP1Cells,
       "caclIntervalInValidOAMCells": caclIntervalInValidOAMCells,
       "caclIntervalInErrOAMCells": caclIntervalInErrOAMCells,
       "caclIntervalInGfcCells": caclIntervalInGfcCells,
       "caclIntervalInVpiVciErrCells": caclIntervalInVpiVciErrCells,
       "caclIntervalInLastUnknVpi": caclIntervalInLastUnknVpi,
       "caclIntervalInLastUnknVci": caclIntervalInLastUnknVci,
       "caclIntervalInXmtCLP0Cells": caclIntervalInXmtCLP0Cells,
       "caclIntervalInXmtCLP1Cells": caclIntervalInXmtCLP1Cells,
       "caclIntervalInValidRMCells": caclIntervalInValidRMCells,
       "caclIntervalInRcvIdleCells": caclIntervalInRcvIdleCells,
       "caclIntervalInHecErrDiscCells": caclIntervalInHecErrDiscCells,
       "caclIntervalInHecErrCorrCells": caclIntervalInHecErrCorrCells,
       "caclIntervalInUpcCLP0DiscCells": caclIntervalInUpcCLP0DiscCells,
       "caclIntervalInUpcTotalDiscCells": caclIntervalInUpcTotalDiscCells,
       "caclIntervalInUpcTotNonCmpCells": caclIntervalInUpcTotNonCmpCells,
       "caclIntervalOutXmtCLP0Cells": caclIntervalOutXmtCLP0Cells,
       "caclIntervalOutXmtCLP1Cells": caclIntervalOutXmtCLP1Cells,
       "caclIntervalOutValidOAMCells": caclIntervalOutValidOAMCells,
       "caclIntervalOutErrOAMCells": caclIntervalOutErrOAMCells,
       "caclIntervalOutVpiVciErrCells": caclIntervalOutVpiVciErrCells,
       "caclIntervalOutRcvCLP0Cells": caclIntervalOutRcvCLP0Cells,
       "caclIntervalOutRcvCLP1Cells": caclIntervalOutRcvCLP1Cells,
       "caclIntervalOutRcvValidRMCells": caclIntervalOutRcvValidRMCells,
       "caclIntervalOutRcvIdleCells": caclIntervalOutRcvIdleCells,
       "caclHighIntervalInRcvCLP0Cells": caclHighIntervalInRcvCLP0Cells,
       "caclHighIntervalInRcvCLP1Cells": caclHighIntervalInRcvCLP1Cells,
       "caclHighIntervalInVpiVciErrCells": caclHighIntervalInVpiVciErrCells,
       "caclHighIntervalInXmtCLP0Cells": caclHighIntervalInXmtCLP0Cells,
       "caclHighIntervalInXmtCLP1Cells": caclHighIntervalInXmtCLP1Cells,
       "caclHighIntervalInHecErrDiscCells": caclHighIntervalInHecErrDiscCells,
       "caclHighIntervalInHecErrCorrCells": caclHighIntervalInHecErrCorrCells,
       "caclHighIntervalOutXmtCLP0Cells": caclHighIntervalOutXmtCLP0Cells,
       "caclHighIntervalOutXmtCLP1Cells": caclHighIntervalOutXmtCLP1Cells,
       "caclHighIntervalOutVpiVciErrCells": caclHighIntervalOutVpiVciErrCells,
       "caclHighIntervalOutRcvCLP0Cells": caclHighIntervalOutRcvCLP0Cells,
       "caclHighIntervalOutRcvCLP1Cells": caclHighIntervalOutRcvCLP1Cells,
       "caclXStatsTable": caclXStatsTable,
       "caclXStatsEntry": caclXStatsEntry,
       "caclHCInValidOAMCells": caclHCInValidOAMCells,
       "caclHCInVpiVciErrCells": caclHCInVpiVciErrCells,
       "caclHCInXmtCLP0Cells": caclHCInXmtCLP0Cells,
       "caclHCInXmtCLP1Cells": caclHCInXmtCLP1Cells,
       "caclHCInHecErrDiscCells": caclHCInHecErrDiscCells,
       "caclHCInHecErrCorrectedCells": caclHCInHecErrCorrectedCells,
       "caclHCOutValidOAMCells": caclHCOutValidOAMCells,
       "caclHCOutRcvCLP0Cells": caclHCOutRcvCLP0Cells,
       "caclHCOutRcvCLP1Cells": caclHCOutRcvCLP1Cells,
       "caclXIntervalStatsTable": caclXIntervalStatsTable,
       "caclXIntervalStatsEntry": caclXIntervalStatsEntry,
       "caclHCIntervalInRcvCLP0Cells": caclHCIntervalInRcvCLP0Cells,
       "caclHCIntervalInRcvCLP1Cells": caclHCIntervalInRcvCLP1Cells,
       "caclHCIntervalInVpiVciErrCells": caclHCIntervalInVpiVciErrCells,
       "caclHCIntervalInXmtCLP0Cells": caclHCIntervalInXmtCLP0Cells,
       "caclHCIntervalInXmtCLP1Cells": caclHCIntervalInXmtCLP1Cells,
       "caclHCIntervalInHecErrDiscCells": caclHCIntervalInHecErrDiscCells,
       "caclHCIntervalInHecErrCorrCells": caclHCIntervalInHecErrCorrCells,
       "caclHCIntervalOutXmtCLP0Cells": caclHCIntervalOutXmtCLP0Cells,
       "caclHCIntervalOutXmtCLP1Cells": caclHCIntervalOutXmtCLP1Cells,
       "caclHCIntervalOutVpiVciErrCells": caclHCIntervalOutVpiVciErrCells,
       "caclHCIntervalOutRcvCLP0Cells": caclHCIntervalOutRcvCLP0Cells,
       "caclHCIntervalOutRcvCLP1Cells": caclHCIntervalOutRcvCLP1Cells,
       "caclMIBConformance": caclMIBConformance,
       "caclMIBCompliances": caclMIBCompliances,
       "caclMIBCompliance": caclMIBCompliance,
       "caclMIBCompliance1": caclMIBCompliance1,
       "caclMIBGroups": caclMIBGroups,
       "caclMIBGroup": caclMIBGroup,
       "caclATMSwitchStatsMIBGroup": caclATMSwitchStatsMIBGroup,
       "caclATMEndSyatemStatsMIBGroup": caclATMEndSyatemStatsMIBGroup,
       "caclHighSpeedATMMIBGroup": caclHighSpeedATMMIBGroup,
       "caclIntervalStatsMIBGroup": caclIntervalStatsMIBGroup,
       "caclATMSwitchStatsMIBGroup1": caclATMSwitchStatsMIBGroup1,
       "caclATMStatsMIBGroup": caclATMStatsMIBGroup,
       "caclHighSpeedATMMIBGroup1": caclHighSpeedATMMIBGroup1,
       "caclIntervalStatsMIBGroup1": caclIntervalStatsMIBGroup1,
       "caclHCIntervalStatsMIBGroup": caclHCIntervalStatsMIBGroup}
)
