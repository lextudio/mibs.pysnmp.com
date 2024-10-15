# SNMP MIB module (TERAWAVE-teraAtom-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraAtom-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:13 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_TeraATMGroup_ObjectIdentity = ObjectIdentity
teraATMGroup = _TeraATMGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 13)
)
_TeraATMSubGroup1_ObjectIdentity = ObjectIdentity
teraATMSubGroup1 = _TeraATMSubGroup1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1)
)
_TeraAtmStatsSumTable_Object = MibTable
teraAtmStatsSumTable = _TeraAtmStatsSumTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 1)
)
if mibBuilder.loadTexts:
    teraAtmStatsSumTable.setStatus("mandatory")
_TeraAtmStatsSumTableEntry_Object = MibTableRow
teraAtmStatsSumTableEntry = _TeraAtmStatsSumTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 1, 1)
)
teraAtmStatsSumTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmIfIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVpi"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVci"),
)
if mibBuilder.loadTexts:
    teraAtmStatsSumTableEntry.setStatus("mandatory")
_TeraAtmIfIndex_Type = Integer32
_TeraAtmIfIndex_Object = MibTableColumn
teraAtmIfIndex = _TeraAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 1, 1, 1),
    _TeraAtmIfIndex_Type()
)
teraAtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmIfIndex.setStatus("mandatory")
_TeraAtmVpi_Type = Integer32
_TeraAtmVpi_Object = MibTableColumn
teraAtmVpi = _TeraAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 1, 1, 2),
    _TeraAtmVpi_Type()
)
teraAtmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmVpi.setStatus("mandatory")
_TeraAtmVci_Type = Integer32
_TeraAtmVci_Object = MibTableColumn
teraAtmVci = _TeraAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 1, 1, 3),
    _TeraAtmVci_Type()
)
teraAtmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmVci.setStatus("mandatory")
_TeraAtmStatsSumReceivedCells_Type = Counter32
_TeraAtmStatsSumReceivedCells_Object = MibTableColumn
teraAtmStatsSumReceivedCells = _TeraAtmStatsSumReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 1, 1, 4),
    _TeraAtmStatsSumReceivedCells_Type()
)
teraAtmStatsSumReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsSumReceivedCells.setStatus("mandatory")
_TeraAtmStatsSumReceivedDiscardCells_Type = Counter32
_TeraAtmStatsSumReceivedDiscardCells_Object = MibTableColumn
teraAtmStatsSumReceivedDiscardCells = _TeraAtmStatsSumReceivedDiscardCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 1, 1, 5),
    _TeraAtmStatsSumReceivedDiscardCells_Type()
)
teraAtmStatsSumReceivedDiscardCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsSumReceivedDiscardCells.setStatus("mandatory")
_TeraAtmStatsSumReceivedTaggedCells_Type = Counter32
_TeraAtmStatsSumReceivedTaggedCells_Object = MibTableColumn
teraAtmStatsSumReceivedTaggedCells = _TeraAtmStatsSumReceivedTaggedCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 1, 1, 6),
    _TeraAtmStatsSumReceivedTaggedCells_Type()
)
teraAtmStatsSumReceivedTaggedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsSumReceivedTaggedCells.setStatus("mandatory")
_TeraAtmStatsSumTransmittedCells_Type = Counter32
_TeraAtmStatsSumTransmittedCells_Object = MibTableColumn
teraAtmStatsSumTransmittedCells = _TeraAtmStatsSumTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 1, 1, 7),
    _TeraAtmStatsSumTransmittedCells_Type()
)
teraAtmStatsSumTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsSumTransmittedCells.setStatus("mandatory")
_TeraAtmStatsTable_Object = MibTable
teraAtmStatsTable = _TeraAtmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 2)
)
if mibBuilder.loadTexts:
    teraAtmStatsTable.setStatus("mandatory")
_TeraAtmStatsTableEntry_Object = MibTableRow
teraAtmStatsTableEntry = _TeraAtmStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 2, 1)
)
teraAtmStatsTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmIfIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVpi"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVci"),
)
if mibBuilder.loadTexts:
    teraAtmStatsTableEntry.setStatus("mandatory")
_TeraAtmStatsReceivedUserClp0Cells_Type = Counter32
_TeraAtmStatsReceivedUserClp0Cells_Object = MibTableColumn
teraAtmStatsReceivedUserClp0Cells = _TeraAtmStatsReceivedUserClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 2, 1, 1),
    _TeraAtmStatsReceivedUserClp0Cells_Type()
)
teraAtmStatsReceivedUserClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsReceivedUserClp0Cells.setStatus("mandatory")
_TeraAtmStatsReceivedUserClp1Cells_Type = Counter32
_TeraAtmStatsReceivedUserClp1Cells_Object = MibTableColumn
teraAtmStatsReceivedUserClp1Cells = _TeraAtmStatsReceivedUserClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 2, 1, 2),
    _TeraAtmStatsReceivedUserClp1Cells_Type()
)
teraAtmStatsReceivedUserClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsReceivedUserClp1Cells.setStatus("mandatory")
_TeraAtmStatsReceivedOamClp0Cells_Type = Counter32
_TeraAtmStatsReceivedOamClp0Cells_Object = MibTableColumn
teraAtmStatsReceivedOamClp0Cells = _TeraAtmStatsReceivedOamClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 2, 1, 3),
    _TeraAtmStatsReceivedOamClp0Cells_Type()
)
teraAtmStatsReceivedOamClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsReceivedOamClp0Cells.setStatus("mandatory")
_TeraAtmStatsReceivedOamClp1Cells_Type = Counter32
_TeraAtmStatsReceivedOamClp1Cells_Object = MibTableColumn
teraAtmStatsReceivedOamClp1Cells = _TeraAtmStatsReceivedOamClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 2, 1, 4),
    _TeraAtmStatsReceivedOamClp1Cells_Type()
)
teraAtmStatsReceivedOamClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsReceivedOamClp1Cells.setStatus("mandatory")
_TeraAtmStatsReceivedDiscardClp0Cells_Type = Counter32
_TeraAtmStatsReceivedDiscardClp0Cells_Object = MibTableColumn
teraAtmStatsReceivedDiscardClp0Cells = _TeraAtmStatsReceivedDiscardClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 2, 1, 5),
    _TeraAtmStatsReceivedDiscardClp0Cells_Type()
)
teraAtmStatsReceivedDiscardClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsReceivedDiscardClp0Cells.setStatus("mandatory")
_TeraAtmStatsReceivedDiscardClp1Cells_Type = Counter32
_TeraAtmStatsReceivedDiscardClp1Cells_Object = MibTableColumn
teraAtmStatsReceivedDiscardClp1Cells = _TeraAtmStatsReceivedDiscardClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 2, 1, 6),
    _TeraAtmStatsReceivedDiscardClp1Cells_Type()
)
teraAtmStatsReceivedDiscardClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsReceivedDiscardClp1Cells.setStatus("mandatory")
_TeraAtmStatsReceivedTaggedCells_Type = Counter32
_TeraAtmStatsReceivedTaggedCells_Object = MibTableColumn
teraAtmStatsReceivedTaggedCells = _TeraAtmStatsReceivedTaggedCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 2, 1, 7),
    _TeraAtmStatsReceivedTaggedCells_Type()
)
teraAtmStatsReceivedTaggedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsReceivedTaggedCells.setStatus("mandatory")
_TeraAtmStatsTransmittedUserClp0Cells_Type = Counter32
_TeraAtmStatsTransmittedUserClp0Cells_Object = MibTableColumn
teraAtmStatsTransmittedUserClp0Cells = _TeraAtmStatsTransmittedUserClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 2, 1, 8),
    _TeraAtmStatsTransmittedUserClp0Cells_Type()
)
teraAtmStatsTransmittedUserClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsTransmittedUserClp0Cells.setStatus("mandatory")
_TeraAtmStatsTransmittedUserClp1Cells_Type = Counter32
_TeraAtmStatsTransmittedUserClp1Cells_Object = MibTableColumn
teraAtmStatsTransmittedUserClp1Cells = _TeraAtmStatsTransmittedUserClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 2, 1, 9),
    _TeraAtmStatsTransmittedUserClp1Cells_Type()
)
teraAtmStatsTransmittedUserClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsTransmittedUserClp1Cells.setStatus("mandatory")
_TeraAtmStatsTransmittedOamClp0Cells_Type = Counter32
_TeraAtmStatsTransmittedOamClp0Cells_Object = MibTableColumn
teraAtmStatsTransmittedOamClp0Cells = _TeraAtmStatsTransmittedOamClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 2, 1, 10),
    _TeraAtmStatsTransmittedOamClp0Cells_Type()
)
teraAtmStatsTransmittedOamClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsTransmittedOamClp0Cells.setStatus("mandatory")
_TeraAtmStatsTransmittedOamClp1Cells_Type = Counter32
_TeraAtmStatsTransmittedOamClp1Cells_Object = MibTableColumn
teraAtmStatsTransmittedOamClp1Cells = _TeraAtmStatsTransmittedOamClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 2, 1, 11),
    _TeraAtmStatsTransmittedOamClp1Cells_Type()
)
teraAtmStatsTransmittedOamClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsTransmittedOamClp1Cells.setStatus("mandatory")
_TeraAtmStatsClearTable_Object = MibTable
teraAtmStatsClearTable = _TeraAtmStatsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 24)
)
if mibBuilder.loadTexts:
    teraAtmStatsClearTable.setStatus("mandatory")
_TeraAtmStatsClearTableEntry_Object = MibTableRow
teraAtmStatsClearTableEntry = _TeraAtmStatsClearTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 24, 1)
)
teraAtmStatsClearTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmIfIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVpi"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVci"),
)
if mibBuilder.loadTexts:
    teraAtmStatsClearTableEntry.setStatus("mandatory")


class _TeraAtmStatsStat_Type(Integer32):
    """Custom type teraAtmStatsStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_TeraAtmStatsStat_Type.__name__ = "Integer32"
_TeraAtmStatsStat_Object = MibTableColumn
teraAtmStatsStat = _TeraAtmStatsStat_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 1, 24, 1, 1),
    _TeraAtmStatsStat_Type()
)
teraAtmStatsStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmStatsStat.setStatus("mandatory")
_TeraATMSubGroup2_ObjectIdentity = ObjectIdentity
teraATMSubGroup2 = _TeraATMSubGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2)
)
_TeraAtmHistoryControlTable_Object = MibTable
teraAtmHistoryControlTable = _TeraAtmHistoryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 1)
)
if mibBuilder.loadTexts:
    teraAtmHistoryControlTable.setStatus("mandatory")
_TeraAtmHistoryControlTableEntry_Object = MibTableRow
teraAtmHistoryControlTableEntry = _TeraAtmHistoryControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 1, 1)
)
teraAtmHistoryControlTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmIfIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVpi"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVci"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmHistoryControlIndex"),
)
if mibBuilder.loadTexts:
    teraAtmHistoryControlTableEntry.setStatus("mandatory")


class _TeraAtmHistoryControlIndex_Type(Integer32):
    """Custom type teraAtmHistoryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraAtmHistoryControlIndex_Type.__name__ = "Integer32"
_TeraAtmHistoryControlIndex_Object = MibTableColumn
teraAtmHistoryControlIndex = _TeraAtmHistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 1, 1, 1),
    _TeraAtmHistoryControlIndex_Type()
)
teraAtmHistoryControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmHistoryControlIndex.setStatus("mandatory")


class _TeraAtmHistoryControlBucketsRequested_Type(Integer32):
    """Custom type teraAtmHistoryControlBucketsRequested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraAtmHistoryControlBucketsRequested_Type.__name__ = "Integer32"
_TeraAtmHistoryControlBucketsRequested_Object = MibTableColumn
teraAtmHistoryControlBucketsRequested = _TeraAtmHistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 1, 1, 2),
    _TeraAtmHistoryControlBucketsRequested_Type()
)
teraAtmHistoryControlBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmHistoryControlBucketsRequested.setStatus("mandatory")


class _TeraAtmHistoryControlBucketsGranted_Type(Integer32):
    """Custom type teraAtmHistoryControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraAtmHistoryControlBucketsGranted_Type.__name__ = "Integer32"
_TeraAtmHistoryControlBucketsGranted_Object = MibTableColumn
teraAtmHistoryControlBucketsGranted = _TeraAtmHistoryControlBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 1, 1, 3),
    _TeraAtmHistoryControlBucketsGranted_Type()
)
teraAtmHistoryControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmHistoryControlBucketsGranted.setStatus("mandatory")


class _TeraAtmHistoryControlInterval_Type(Integer32):
    """Custom type teraAtmHistoryControlInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TeraAtmHistoryControlInterval_Type.__name__ = "Integer32"
_TeraAtmHistoryControlInterval_Object = MibTableColumn
teraAtmHistoryControlInterval = _TeraAtmHistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 1, 1, 4),
    _TeraAtmHistoryControlInterval_Type()
)
teraAtmHistoryControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmHistoryControlInterval.setStatus("mandatory")


class _TeraAtmHistoryControlStatus_Type(Integer32):
    """Custom type teraAtmHistoryControlStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_TeraAtmHistoryControlStatus_Type.__name__ = "Integer32"
_TeraAtmHistoryControlStatus_Object = MibTableColumn
teraAtmHistoryControlStatus = _TeraAtmHistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 1, 1, 5),
    _TeraAtmHistoryControlStatus_Type()
)
teraAtmHistoryControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmHistoryControlStatus.setStatus("mandatory")
_TeraAtmStatsHistoryTable_Object = MibTable
teraAtmStatsHistoryTable = _TeraAtmStatsHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2)
)
if mibBuilder.loadTexts:
    teraAtmStatsHistoryTable.setStatus("mandatory")
_TeraAtmStatsHistoryTableEntry_Object = MibTableRow
teraAtmStatsHistoryTableEntry = _TeraAtmStatsHistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2, 1)
)
teraAtmStatsHistoryTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmIfIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVpi"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVci"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmHistoryControlIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmStatsHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    teraAtmStatsHistoryTableEntry.setStatus("mandatory")


class _TeraAtmStatsHistorySampleIndex_Type(Integer32):
    """Custom type teraAtmStatsHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TeraAtmStatsHistorySampleIndex_Type.__name__ = "Integer32"
_TeraAtmStatsHistorySampleIndex_Object = MibTableColumn
teraAtmStatsHistorySampleIndex = _TeraAtmStatsHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2, 1, 1),
    _TeraAtmStatsHistorySampleIndex_Type()
)
teraAtmStatsHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsHistorySampleIndex.setStatus("mandatory")
_TeraAtmStatsHistoryIntervalStart_Type = TimeTicks
_TeraAtmStatsHistoryIntervalStart_Object = MibTableColumn
teraAtmStatsHistoryIntervalStart = _TeraAtmStatsHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2, 1, 2),
    _TeraAtmStatsHistoryIntervalStart_Type()
)
teraAtmStatsHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsHistoryIntervalStart.setStatus("mandatory")
_TeraAtmStatsHistoryReceivedUserClp0Cells_Type = Counter32
_TeraAtmStatsHistoryReceivedUserClp0Cells_Object = MibTableColumn
teraAtmStatsHistoryReceivedUserClp0Cells = _TeraAtmStatsHistoryReceivedUserClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2, 1, 3),
    _TeraAtmStatsHistoryReceivedUserClp0Cells_Type()
)
teraAtmStatsHistoryReceivedUserClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsHistoryReceivedUserClp0Cells.setStatus("mandatory")
_TeraAtmStatsHistoryReceivedUserClp1Cells_Type = Counter32
_TeraAtmStatsHistoryReceivedUserClp1Cells_Object = MibTableColumn
teraAtmStatsHistoryReceivedUserClp1Cells = _TeraAtmStatsHistoryReceivedUserClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2, 1, 4),
    _TeraAtmStatsHistoryReceivedUserClp1Cells_Type()
)
teraAtmStatsHistoryReceivedUserClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsHistoryReceivedUserClp1Cells.setStatus("mandatory")
_TeraAtmStatsHistoryReceivedOamClp0Cells_Type = Counter32
_TeraAtmStatsHistoryReceivedOamClp0Cells_Object = MibTableColumn
teraAtmStatsHistoryReceivedOamClp0Cells = _TeraAtmStatsHistoryReceivedOamClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2, 1, 5),
    _TeraAtmStatsHistoryReceivedOamClp0Cells_Type()
)
teraAtmStatsHistoryReceivedOamClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsHistoryReceivedOamClp0Cells.setStatus("mandatory")
_TeraAtmStatsHistoryReceivedOamClp1Cells_Type = Counter32
_TeraAtmStatsHistoryReceivedOamClp1Cells_Object = MibTableColumn
teraAtmStatsHistoryReceivedOamClp1Cells = _TeraAtmStatsHistoryReceivedOamClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2, 1, 6),
    _TeraAtmStatsHistoryReceivedOamClp1Cells_Type()
)
teraAtmStatsHistoryReceivedOamClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsHistoryReceivedOamClp1Cells.setStatus("mandatory")
_TeraAtmStatsHistoryReceivedDiscardClp0Cells_Type = Counter32
_TeraAtmStatsHistoryReceivedDiscardClp0Cells_Object = MibTableColumn
teraAtmStatsHistoryReceivedDiscardClp0Cells = _TeraAtmStatsHistoryReceivedDiscardClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2, 1, 7),
    _TeraAtmStatsHistoryReceivedDiscardClp0Cells_Type()
)
teraAtmStatsHistoryReceivedDiscardClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsHistoryReceivedDiscardClp0Cells.setStatus("mandatory")
_TeraAtmStatsHistoryReceivedDiscardClp1Cells_Type = Counter32
_TeraAtmStatsHistoryReceivedDiscardClp1Cells_Object = MibTableColumn
teraAtmStatsHistoryReceivedDiscardClp1Cells = _TeraAtmStatsHistoryReceivedDiscardClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2, 1, 8),
    _TeraAtmStatsHistoryReceivedDiscardClp1Cells_Type()
)
teraAtmStatsHistoryReceivedDiscardClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsHistoryReceivedDiscardClp1Cells.setStatus("mandatory")
_TeraAtmStatsHistoryReceivedTaggedCells_Type = Counter32
_TeraAtmStatsHistoryReceivedTaggedCells_Object = MibTableColumn
teraAtmStatsHistoryReceivedTaggedCells = _TeraAtmStatsHistoryReceivedTaggedCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2, 1, 9),
    _TeraAtmStatsHistoryReceivedTaggedCells_Type()
)
teraAtmStatsHistoryReceivedTaggedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsHistoryReceivedTaggedCells.setStatus("mandatory")
_TeraAtmStatsHistoryTransmittedUserClp0Cells_Type = Counter32
_TeraAtmStatsHistoryTransmittedUserClp0Cells_Object = MibTableColumn
teraAtmStatsHistoryTransmittedUserClp0Cells = _TeraAtmStatsHistoryTransmittedUserClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2, 1, 10),
    _TeraAtmStatsHistoryTransmittedUserClp0Cells_Type()
)
teraAtmStatsHistoryTransmittedUserClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsHistoryTransmittedUserClp0Cells.setStatus("mandatory")
_TeraAtmStatsHistoryTransmittedUserClp1Cells_Type = Counter32
_TeraAtmStatsHistoryTransmittedUserClp1Cells_Object = MibTableColumn
teraAtmStatsHistoryTransmittedUserClp1Cells = _TeraAtmStatsHistoryTransmittedUserClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2, 1, 11),
    _TeraAtmStatsHistoryTransmittedUserClp1Cells_Type()
)
teraAtmStatsHistoryTransmittedUserClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsHistoryTransmittedUserClp1Cells.setStatus("mandatory")
_TeraAtmStatsHistoryTransmittedOamClp0Cells_Type = Counter32
_TeraAtmStatsHistoryTransmittedOamClp0Cells_Object = MibTableColumn
teraAtmStatsHistoryTransmittedOamClp0Cells = _TeraAtmStatsHistoryTransmittedOamClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2, 1, 12),
    _TeraAtmStatsHistoryTransmittedOamClp0Cells_Type()
)
teraAtmStatsHistoryTransmittedOamClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsHistoryTransmittedOamClp0Cells.setStatus("mandatory")
_TeraAtmStatsHistoryTransmittedOamClp1Cells_Type = Counter32
_TeraAtmStatsHistoryTransmittedOamClp1Cells_Object = MibTableColumn
teraAtmStatsHistoryTransmittedOamClp1Cells = _TeraAtmStatsHistoryTransmittedOamClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 2, 2, 1, 13),
    _TeraAtmStatsHistoryTransmittedOamClp1Cells_Type()
)
teraAtmStatsHistoryTransmittedOamClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmStatsHistoryTransmittedOamClp1Cells.setStatus("mandatory")
_TeraATMSubGroup3_ObjectIdentity = ObjectIdentity
teraATMSubGroup3 = _TeraATMSubGroup3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 13, 3)
)
_TeraAtmILMIPollCfgTable_ObjectIdentity = ObjectIdentity
teraAtmILMIPollCfgTable = _TeraAtmILMIPollCfgTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 13, 3, 1)
)


class _TeraDefaultRegainTimeout_Type(Integer32):
    """Custom type teraDefaultRegainTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TeraDefaultRegainTimeout_Type.__name__ = "Integer32"
_TeraDefaultRegainTimeout_Object = MibScalar
teraDefaultRegainTimeout = _TeraDefaultRegainTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 3, 1, 1),
    _TeraDefaultRegainTimeout_Type()
)
teraDefaultRegainTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDefaultRegainTimeout.setStatus("mandatory")


class _TeraDefaultTestConnectTimeout_Type(Integer32):
    """Custom type teraDefaultTestConnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TeraDefaultTestConnectTimeout_Type.__name__ = "Integer32"
_TeraDefaultTestConnectTimeout_Object = MibScalar
teraDefaultTestConnectTimeout = _TeraDefaultTestConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 3, 1, 2),
    _TeraDefaultTestConnectTimeout_Type()
)
teraDefaultTestConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDefaultTestConnectTimeout.setStatus("mandatory")


class _TeraDefaultAllowedNumOfFailed_Type(Integer32):
    """Custom type teraDefaultAllowedNumOfFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraDefaultAllowedNumOfFailed_Type.__name__ = "Integer32"
_TeraDefaultAllowedNumOfFailed_Object = MibScalar
teraDefaultAllowedNumOfFailed = _TeraDefaultAllowedNumOfFailed_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 3, 1, 3),
    _TeraDefaultAllowedNumOfFailed_Type()
)
teraDefaultAllowedNumOfFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDefaultAllowedNumOfFailed.setStatus("mandatory")
_TeraATMPhyStatTable_Object = MibTable
teraATMPhyStatTable = _TeraATMPhyStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 4)
)
if mibBuilder.loadTexts:
    teraATMPhyStatTable.setStatus("mandatory")
_TeraATMPhyStatTableEntry_Object = MibTableRow
teraATMPhyStatTableEntry = _TeraATMPhyStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 4, 1)
)
teraATMPhyStatTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmIfIndex"),
)
if mibBuilder.loadTexts:
    teraATMPhyStatTableEntry.setStatus("mandatory")
_TeraATM_Seconds_Type = Counter32
_TeraATM_Seconds_Object = MibScalar
teraATM_Seconds = _TeraATM_Seconds_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 4, 1, 1),
    _TeraATM_Seconds_Type()
)
teraATM_Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraATM_Seconds.setStatus("mandatory")
_TeraATM_CorrectHCSError_Type = Counter32
_TeraATM_CorrectHCSError_Object = MibScalar
teraATM_CorrectHCSError = _TeraATM_CorrectHCSError_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 4, 1, 2),
    _TeraATM_CorrectHCSError_Type()
)
teraATM_CorrectHCSError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraATM_CorrectHCSError.setStatus("mandatory")
_TeraATM_UncorrectHCSError_Type = Counter32
_TeraATM_UncorrectHCSError_Object = MibScalar
teraATM_UncorrectHCSError = _TeraATM_UncorrectHCSError_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 4, 1, 3),
    _TeraATM_UncorrectHCSError_Type()
)
teraATM_UncorrectHCSError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraATM_UncorrectHCSError.setStatus("mandatory")
_TeraATM_ReceiveCell_Type = Counter64
_TeraATM_ReceiveCell_Object = MibScalar
teraATM_ReceiveCell = _TeraATM_ReceiveCell_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 4, 1, 4),
    _TeraATM_ReceiveCell_Type()
)
teraATM_ReceiveCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraATM_ReceiveCell.setStatus("mandatory")
_TeraATM_IDLECell_Type = Counter64
_TeraATM_IDLECell_Object = MibScalar
teraATM_IDLECell = _TeraATM_IDLECell_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 4, 1, 5),
    _TeraATM_IDLECell_Type()
)
teraATM_IDLECell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraATM_IDLECell.setStatus("mandatory")
_TeraATM_TransmitCell_Type = Counter64
_TeraATM_TransmitCell_Object = MibScalar
teraATM_TransmitCell = _TeraATM_TransmitCell_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 4, 1, 6),
    _TeraATM_TransmitCell_Type()
)
teraATM_TransmitCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraATM_TransmitCell.setStatus("mandatory")


class _TeraATM_AdminStatus_Type(Integer32):
    """Custom type teraATM_AdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("run", 2),
          ("stop", 3))
    )


_TeraATM_AdminStatus_Type.__name__ = "Integer32"
_TeraATM_AdminStatus_Object = MibScalar
teraATM_AdminStatus = _TeraATM_AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 4, 1, 7),
    _TeraATM_AdminStatus_Type()
)
teraATM_AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraATM_AdminStatus.setStatus("mandatory")
_TeraAtmPortStatsTable_Object = MibTable
teraAtmPortStatsTable = _TeraAtmPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 5)
)
if mibBuilder.loadTexts:
    teraAtmPortStatsTable.setStatus("mandatory")
_TeraAtmPortStatsTableEntry_Object = MibTableRow
teraAtmPortStatsTableEntry = _TeraAtmPortStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 5, 1)
)
teraAtmPortStatsTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraAtmPortStatsTableEntry.setStatus("mandatory")
_TeraAtmPortStatsIngressUnassignedCells_Type = Counter32
_TeraAtmPortStatsIngressUnassignedCells_Object = MibTableColumn
teraAtmPortStatsIngressUnassignedCells = _TeraAtmPortStatsIngressUnassignedCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 5, 1, 1),
    _TeraAtmPortStatsIngressUnassignedCells_Type()
)
teraAtmPortStatsIngressUnassignedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsIngressUnassignedCells.setStatus("mandatory")
_TeraAtmPortStatsEgressUnassignedCells_Type = Counter32
_TeraAtmPortStatsEgressUnassignedCells_Object = MibTableColumn
teraAtmPortStatsEgressUnassignedCells = _TeraAtmPortStatsEgressUnassignedCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 5, 1, 2),
    _TeraAtmPortStatsEgressUnassignedCells_Type()
)
teraAtmPortStatsEgressUnassignedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsEgressUnassignedCells.setStatus("mandatory")
_TeraAtmPortStatsTransmittedClp0Cells_Type = Counter32
_TeraAtmPortStatsTransmittedClp0Cells_Object = MibTableColumn
teraAtmPortStatsTransmittedClp0Cells = _TeraAtmPortStatsTransmittedClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 5, 1, 3),
    _TeraAtmPortStatsTransmittedClp0Cells_Type()
)
teraAtmPortStatsTransmittedClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsTransmittedClp0Cells.setStatus("mandatory")
_TeraAtmPortStatsTransmittedClp1Cells_Type = Counter32
_TeraAtmPortStatsTransmittedClp1Cells_Object = MibTableColumn
teraAtmPortStatsTransmittedClp1Cells = _TeraAtmPortStatsTransmittedClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 5, 1, 4),
    _TeraAtmPortStatsTransmittedClp1Cells_Type()
)
teraAtmPortStatsTransmittedClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsTransmittedClp1Cells.setStatus("mandatory")
_TeraAtmPortStatsReceivedClp0Cells_Type = Counter32
_TeraAtmPortStatsReceivedClp0Cells_Object = MibTableColumn
teraAtmPortStatsReceivedClp0Cells = _TeraAtmPortStatsReceivedClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 5, 1, 5),
    _TeraAtmPortStatsReceivedClp0Cells_Type()
)
teraAtmPortStatsReceivedClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsReceivedClp0Cells.setStatus("mandatory")
_TeraAtmPortStatsReceivedClp1Cells_Type = Counter32
_TeraAtmPortStatsReceivedClp1Cells_Object = MibTableColumn
teraAtmPortStatsReceivedClp1Cells = _TeraAtmPortStatsReceivedClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 5, 1, 6),
    _TeraAtmPortStatsReceivedClp1Cells_Type()
)
teraAtmPortStatsReceivedClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsReceivedClp1Cells.setStatus("mandatory")
_TeraAtmPortStatsReceivedOamCells_Type = Counter32
_TeraAtmPortStatsReceivedOamCells_Object = MibTableColumn
teraAtmPortStatsReceivedOamCells = _TeraAtmPortStatsReceivedOamCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 5, 1, 7),
    _TeraAtmPortStatsReceivedOamCells_Type()
)
teraAtmPortStatsReceivedOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsReceivedOamCells.setStatus("mandatory")
_TeraAtmPortStatsReceivedRmCells_Type = Counter32
_TeraAtmPortStatsReceivedRmCells_Object = MibTableColumn
teraAtmPortStatsReceivedRmCells = _TeraAtmPortStatsReceivedRmCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 5, 1, 8),
    _TeraAtmPortStatsReceivedRmCells_Type()
)
teraAtmPortStatsReceivedRmCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsReceivedRmCells.setStatus("mandatory")
_TeraAtmPortStatsReceivedErroredOamCells_Type = Counter32
_TeraAtmPortStatsReceivedErroredOamCells_Object = MibTableColumn
teraAtmPortStatsReceivedErroredOamCells = _TeraAtmPortStatsReceivedErroredOamCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 5, 1, 9),
    _TeraAtmPortStatsReceivedErroredOamCells_Type()
)
teraAtmPortStatsReceivedErroredOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsReceivedErroredOamCells.setStatus("mandatory")
_TeraAtmPortStatsReceivedErroredRmCells_Type = Counter32
_TeraAtmPortStatsReceivedErroredRmCells_Object = MibTableColumn
teraAtmPortStatsReceivedErroredRmCells = _TeraAtmPortStatsReceivedErroredRmCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 5, 1, 10),
    _TeraAtmPortStatsReceivedErroredRmCells_Type()
)
teraAtmPortStatsReceivedErroredRmCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsReceivedErroredRmCells.setStatus("mandatory")
_TeraAtmPortStatsReceivedNonZerroGfcCells_Type = Counter32
_TeraAtmPortStatsReceivedNonZerroGfcCells_Object = MibTableColumn
teraAtmPortStatsReceivedNonZerroGfcCells = _TeraAtmPortStatsReceivedNonZerroGfcCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 5, 1, 11),
    _TeraAtmPortStatsReceivedNonZerroGfcCells_Type()
)
teraAtmPortStatsReceivedNonZerroGfcCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsReceivedNonZerroGfcCells.setStatus("mandatory")
_TeraAtmPortStatsHistoryTable_Object = MibTable
teraAtmPortStatsHistoryTable = _TeraAtmPortStatsHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 6)
)
if mibBuilder.loadTexts:
    teraAtmPortStatsHistoryTable.setStatus("mandatory")
_TeraAtmPortStatsHistoryTableEntry_Object = MibTableRow
teraAtmPortStatsHistoryTableEntry = _TeraAtmPortStatsHistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 6, 1)
)
teraAtmPortStatsHistoryTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmIfIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmHistoryControlIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmStatsHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    teraAtmPortStatsHistoryTableEntry.setStatus("mandatory")
_TeraAtmPortStatsHistoryIngressUnassignedCells_Type = Counter32
_TeraAtmPortStatsHistoryIngressUnassignedCells_Object = MibTableColumn
teraAtmPortStatsHistoryIngressUnassignedCells = _TeraAtmPortStatsHistoryIngressUnassignedCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 6, 1, 1),
    _TeraAtmPortStatsHistoryIngressUnassignedCells_Type()
)
teraAtmPortStatsHistoryIngressUnassignedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsHistoryIngressUnassignedCells.setStatus("mandatory")
_TeraAtmPortStatsHistoryEgressUnassignedCells_Type = Counter32
_TeraAtmPortStatsHistoryEgressUnassignedCells_Object = MibTableColumn
teraAtmPortStatsHistoryEgressUnassignedCells = _TeraAtmPortStatsHistoryEgressUnassignedCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 6, 1, 2),
    _TeraAtmPortStatsHistoryEgressUnassignedCells_Type()
)
teraAtmPortStatsHistoryEgressUnassignedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsHistoryEgressUnassignedCells.setStatus("mandatory")
_TeraAtmPortStatsHistoryTransmittedClp0Cells_Type = Counter32
_TeraAtmPortStatsHistoryTransmittedClp0Cells_Object = MibTableColumn
teraAtmPortStatsHistoryTransmittedClp0Cells = _TeraAtmPortStatsHistoryTransmittedClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 6, 1, 3),
    _TeraAtmPortStatsHistoryTransmittedClp0Cells_Type()
)
teraAtmPortStatsHistoryTransmittedClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsHistoryTransmittedClp0Cells.setStatus("mandatory")
_TeraAtmPortStatsHistoryTransmittedClp1Cells_Type = Counter32
_TeraAtmPortStatsHistoryTransmittedClp1Cells_Object = MibTableColumn
teraAtmPortStatsHistoryTransmittedClp1Cells = _TeraAtmPortStatsHistoryTransmittedClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 6, 1, 4),
    _TeraAtmPortStatsHistoryTransmittedClp1Cells_Type()
)
teraAtmPortStatsHistoryTransmittedClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsHistoryTransmittedClp1Cells.setStatus("mandatory")
_TeraAtmPortStatsHistoryReceivedClp0Cells_Type = Counter32
_TeraAtmPortStatsHistoryReceivedClp0Cells_Object = MibTableColumn
teraAtmPortStatsHistoryReceivedClp0Cells = _TeraAtmPortStatsHistoryReceivedClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 6, 1, 5),
    _TeraAtmPortStatsHistoryReceivedClp0Cells_Type()
)
teraAtmPortStatsHistoryReceivedClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsHistoryReceivedClp0Cells.setStatus("mandatory")
_TeraAtmPortStatsHistoryReceivedClp1Cells_Type = Counter32
_TeraAtmPortStatsHistoryReceivedClp1Cells_Object = MibTableColumn
teraAtmPortStatsHistoryReceivedClp1Cells = _TeraAtmPortStatsHistoryReceivedClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 6, 1, 6),
    _TeraAtmPortStatsHistoryReceivedClp1Cells_Type()
)
teraAtmPortStatsHistoryReceivedClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsHistoryReceivedClp1Cells.setStatus("mandatory")
_TeraAtmPortStatsHistoryReceivedOamCells_Type = Counter32
_TeraAtmPortStatsHistoryReceivedOamCells_Object = MibTableColumn
teraAtmPortStatsHistoryReceivedOamCells = _TeraAtmPortStatsHistoryReceivedOamCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 6, 1, 7),
    _TeraAtmPortStatsHistoryReceivedOamCells_Type()
)
teraAtmPortStatsHistoryReceivedOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsHistoryReceivedOamCells.setStatus("mandatory")
_TeraAtmPortStatsHistoryReceivedRmCells_Type = Counter32
_TeraAtmPortStatsHistoryReceivedRmCells_Object = MibTableColumn
teraAtmPortStatsHistoryReceivedRmCells = _TeraAtmPortStatsHistoryReceivedRmCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 6, 1, 8),
    _TeraAtmPortStatsHistoryReceivedRmCells_Type()
)
teraAtmPortStatsHistoryReceivedRmCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsHistoryReceivedRmCells.setStatus("mandatory")
_TeraAtmPortStatsHistoryReceivedErroredOamCells_Type = Counter32
_TeraAtmPortStatsHistoryReceivedErroredOamCells_Object = MibTableColumn
teraAtmPortStatsHistoryReceivedErroredOamCells = _TeraAtmPortStatsHistoryReceivedErroredOamCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 6, 1, 9),
    _TeraAtmPortStatsHistoryReceivedErroredOamCells_Type()
)
teraAtmPortStatsHistoryReceivedErroredOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsHistoryReceivedErroredOamCells.setStatus("mandatory")
_TeraAtmPortStatsHistoryReceivedErroredRmCells_Type = Counter32
_TeraAtmPortStatsHistoryReceivedErroredRmCells_Object = MibTableColumn
teraAtmPortStatsHistoryReceivedErroredRmCells = _TeraAtmPortStatsHistoryReceivedErroredRmCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 6, 1, 10),
    _TeraAtmPortStatsHistoryReceivedErroredRmCells_Type()
)
teraAtmPortStatsHistoryReceivedErroredRmCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsHistoryReceivedErroredRmCells.setStatus("mandatory")
_TeraAtmPortStatsHistoryReceivedNonZerroGfcCells_Type = Counter32
_TeraAtmPortStatsHistoryReceivedNonZerroGfcCells_Object = MibTableColumn
teraAtmPortStatsHistoryReceivedNonZerroGfcCells = _TeraAtmPortStatsHistoryReceivedNonZerroGfcCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 6, 1, 11),
    _TeraAtmPortStatsHistoryReceivedNonZerroGfcCells_Type()
)
teraAtmPortStatsHistoryReceivedNonZerroGfcCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortStatsHistoryReceivedNonZerroGfcCells.setStatus("mandatory")
_TeraAtmCc_ObjectIdentity = ObjectIdentity
teraAtmCc = _TeraAtmCc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 13, 7)
)
_TeraAtmCcControlTable_Object = MibTable
teraAtmCcControlTable = _TeraAtmCcControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 7, 1)
)
if mibBuilder.loadTexts:
    teraAtmCcControlTable.setStatus("mandatory")
_TeraAtmCcControlTableEntry_Object = MibTableRow
teraAtmCcControlTableEntry = _TeraAtmCcControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 7, 1, 1)
)
teraAtmCcControlTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmIfIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVpi"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVci"),
)
if mibBuilder.loadTexts:
    teraAtmCcControlTableEntry.setStatus("mandatory")


class _TeraAtmCcSourceControl_Type(Integer32):
    """Custom type teraAtmCcSourceControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2))
    )


_TeraAtmCcSourceControl_Type.__name__ = "Integer32"
_TeraAtmCcSourceControl_Object = MibTableColumn
teraAtmCcSourceControl = _TeraAtmCcSourceControl_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 7, 1, 1, 1),
    _TeraAtmCcSourceControl_Type()
)
teraAtmCcSourceControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmCcSourceControl.setStatus("mandatory")


class _TeraAtmCcSinkControl_Type(Integer32):
    """Custom type teraAtmCcSinkControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 4),
          ("enable", 3))
    )


_TeraAtmCcSinkControl_Type.__name__ = "Integer32"
_TeraAtmCcSinkControl_Object = MibTableColumn
teraAtmCcSinkControl = _TeraAtmCcSinkControl_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 7, 1, 1, 2),
    _TeraAtmCcSinkControl_Type()
)
teraAtmCcSinkControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmCcSinkControl.setStatus("mandatory")


class _TeraAtmCcType_Type(Integer32):
    """Custom type teraAtmCcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("end-to-End", 5),
          ("seg-to-Seg", 4))
    )


_TeraAtmCcType_Type.__name__ = "Integer32"
_TeraAtmCcType_Object = MibTableColumn
teraAtmCcType = _TeraAtmCcType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 7, 1, 1, 3),
    _TeraAtmCcType_Type()
)
teraAtmCcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmCcType.setStatus("mandatory")


class _TeraAtmCcTargetDir_Type(Integer32):
    """Custom type teraAtmCcTargetDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("upstream", 1))
    )


_TeraAtmCcTargetDir_Type.__name__ = "Integer32"
_TeraAtmCcTargetDir_Object = MibTableColumn
teraAtmCcTargetDir = _TeraAtmCcTargetDir_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 7, 1, 1, 4),
    _TeraAtmCcTargetDir_Type()
)
teraAtmCcTargetDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmCcTargetDir.setStatus("mandatory")


class _TeraAtmCcSinkDir_Type(Integer32):
    """Custom type teraAtmCcSinkDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("none", 0),
          ("upstream", 1))
    )


_TeraAtmCcSinkDir_Type.__name__ = "Integer32"
_TeraAtmCcSinkDir_Object = MibTableColumn
teraAtmCcSinkDir = _TeraAtmCcSinkDir_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 7, 1, 1, 5),
    _TeraAtmCcSinkDir_Type()
)
teraAtmCcSinkDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmCcSinkDir.setStatus("mandatory")


class _TeraAtmCcSourceResult_Type(Integer32):
    """Custom type teraAtmCcSourceResult based on Integer32"""
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
        *(("activationFailed", 4),
          ("activationInProgress", 3),
          ("activationSuccess", 2),
          ("none", 1))
    )


_TeraAtmCcSourceResult_Type.__name__ = "Integer32"
_TeraAtmCcSourceResult_Object = MibTableColumn
teraAtmCcSourceResult = _TeraAtmCcSourceResult_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 7, 1, 1, 6),
    _TeraAtmCcSourceResult_Type()
)
teraAtmCcSourceResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmCcSourceResult.setStatus("mandatory")


class _TeraAtmCcSinkResult_Type(Integer32):
    """Custom type teraAtmCcSinkResult based on Integer32"""
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
        *(("cc-Failed", 4),
          ("cc-OK", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_TeraAtmCcSinkResult_Type.__name__ = "Integer32"
_TeraAtmCcSinkResult_Object = MibTableColumn
teraAtmCcSinkResult = _TeraAtmCcSinkResult_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 7, 1, 1, 7),
    _TeraAtmCcSinkResult_Type()
)
teraAtmCcSinkResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmCcSinkResult.setStatus("mandatory")


class _TeraAtmCcRowStatus_Type(Integer32):
    """Custom type teraAtmCcRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("ok", 1))
    )


_TeraAtmCcRowStatus_Type.__name__ = "Integer32"
_TeraAtmCcRowStatus_Object = MibTableColumn
teraAtmCcRowStatus = _TeraAtmCcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 7, 1, 1, 8),
    _TeraAtmCcRowStatus_Type()
)
teraAtmCcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmCcRowStatus.setStatus("mandatory")
_TeraAtmPmControlTable_Object = MibTable
teraAtmPmControlTable = _TeraAtmPmControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 8)
)
if mibBuilder.loadTexts:
    teraAtmPmControlTable.setStatus("mandatory")
_TeraAtmPmControlTableEntry_Object = MibTableRow
teraAtmPmControlTableEntry = _TeraAtmPmControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 8, 1)
)
teraAtmPmControlTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmIfIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVpi"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVci"),
)
if mibBuilder.loadTexts:
    teraAtmPmControlTableEntry.setStatus("mandatory")


class _TeraAtmPmSourceControl_Type(Integer32):
    """Custom type teraAtmPmSourceControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2))
    )


_TeraAtmPmSourceControl_Type.__name__ = "Integer32"
_TeraAtmPmSourceControl_Object = MibTableColumn
teraAtmPmSourceControl = _TeraAtmPmSourceControl_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 8, 1, 1),
    _TeraAtmPmSourceControl_Type()
)
teraAtmPmSourceControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmPmSourceControl.setStatus("mandatory")


class _TeraAtmPmSourceBlockSize_Type(Integer32):
    """Custom type teraAtmPmSourceBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("number-1024", 1),
          ("number-128", 8),
          ("number-256", 4),
          ("number-512", 2))
    )


_TeraAtmPmSourceBlockSize_Type.__name__ = "Integer32"
_TeraAtmPmSourceBlockSize_Object = MibTableColumn
teraAtmPmSourceBlockSize = _TeraAtmPmSourceBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 8, 1, 2),
    _TeraAtmPmSourceBlockSize_Type()
)
teraAtmPmSourceBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmPmSourceBlockSize.setStatus("mandatory")


class _TeraAtmPmSinkControl_Type(Integer32):
    """Custom type teraAtmPmSinkControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 4),
          ("enable", 3))
    )


_TeraAtmPmSinkControl_Type.__name__ = "Integer32"
_TeraAtmPmSinkControl_Object = MibTableColumn
teraAtmPmSinkControl = _TeraAtmPmSinkControl_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 8, 1, 3),
    _TeraAtmPmSinkControl_Type()
)
teraAtmPmSinkControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmPmSinkControl.setStatus("mandatory")


class _TeraAtmPmSourceType_Type(Integer32):
    """Custom type teraAtmPmSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("end-to-End", 5),
          ("seg-to-Seg", 4))
    )


_TeraAtmPmSourceType_Type.__name__ = "Integer32"
_TeraAtmPmSourceType_Object = MibTableColumn
teraAtmPmSourceType = _TeraAtmPmSourceType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 8, 1, 4),
    _TeraAtmPmSourceType_Type()
)
teraAtmPmSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmPmSourceType.setStatus("mandatory")


class _TeraAtmPmTargetDir_Type(Integer32):
    """Custom type teraAtmPmTargetDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("upstream", 1))
    )


_TeraAtmPmTargetDir_Type.__name__ = "Integer32"
_TeraAtmPmTargetDir_Object = MibTableColumn
teraAtmPmTargetDir = _TeraAtmPmTargetDir_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 8, 1, 5),
    _TeraAtmPmTargetDir_Type()
)
teraAtmPmTargetDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmPmTargetDir.setStatus("mandatory")


class _TeraAtmPmSinkDir_Type(Integer32):
    """Custom type teraAtmPmSinkDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("none", 0),
          ("upstream", 1))
    )


_TeraAtmPmSinkDir_Type.__name__ = "Integer32"
_TeraAtmPmSinkDir_Object = MibTableColumn
teraAtmPmSinkDir = _TeraAtmPmSinkDir_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 8, 1, 6),
    _TeraAtmPmSinkDir_Type()
)
teraAtmPmSinkDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPmSinkDir.setStatus("mandatory")


class _TeraAtmPmSourceResult_Type(Integer32):
    """Custom type teraAtmPmSourceResult based on Integer32"""
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
        *(("activationFailed", 4),
          ("activationInProgress", 3),
          ("activationSuccess", 2),
          ("none", 1))
    )


_TeraAtmPmSourceResult_Type.__name__ = "Integer32"
_TeraAtmPmSourceResult_Object = MibTableColumn
teraAtmPmSourceResult = _TeraAtmPmSourceResult_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 8, 1, 7),
    _TeraAtmPmSourceResult_Type()
)
teraAtmPmSourceResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPmSourceResult.setStatus("mandatory")


class _TeraAtmPmSinkResult_Type(Integer32):
    """Custom type teraAtmPmSinkResult based on Integer32"""
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


_TeraAtmPmSinkResult_Type.__name__ = "Integer32"
_TeraAtmPmSinkResult_Object = MibTableColumn
teraAtmPmSinkResult = _TeraAtmPmSinkResult_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 8, 1, 8),
    _TeraAtmPmSinkResult_Type()
)
teraAtmPmSinkResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPmSinkResult.setStatus("mandatory")


class _TeraAtmPmRowStatus_Type(Integer32):
    """Custom type teraAtmPmRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("ok", 1))
    )


_TeraAtmPmRowStatus_Type.__name__ = "Integer32"
_TeraAtmPmRowStatus_Object = MibTableColumn
teraAtmPmRowStatus = _TeraAtmPmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 8, 1, 9),
    _TeraAtmPmRowStatus_Type()
)
teraAtmPmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmPmRowStatus.setStatus("mandatory")
_TeraOamPmStatsTable_Object = MibTable
teraOamPmStatsTable = _TeraOamPmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 9)
)
if mibBuilder.loadTexts:
    teraOamPmStatsTable.setStatus("mandatory")
_TeraOamPmStatsTableEntry_Object = MibTableRow
teraOamPmStatsTableEntry = _TeraOamPmStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 9, 1)
)
teraOamPmStatsTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmIfIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVpi"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmVci"),
)
if mibBuilder.loadTexts:
    teraOamPmStatsTableEntry.setStatus("mandatory")
_TeraOamPmStatsTotalTUC0_Type = Counter32
_TeraOamPmStatsTotalTUC0_Object = MibTableColumn
teraOamPmStatsTotalTUC0 = _TeraOamPmStatsTotalTUC0_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 9, 1, 1),
    _TeraOamPmStatsTotalTUC0_Type()
)
teraOamPmStatsTotalTUC0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraOamPmStatsTotalTUC0.setStatus("mandatory")
_TeraOamPmStatsTotalTUC01_Type = Counter32
_TeraOamPmStatsTotalTUC01_Object = MibTableColumn
teraOamPmStatsTotalTUC01 = _TeraOamPmStatsTotalTUC01_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 9, 1, 2),
    _TeraOamPmStatsTotalTUC01_Type()
)
teraOamPmStatsTotalTUC01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraOamPmStatsTotalTUC01.setStatus("mandatory")
_TeraOamPmStatsTotalTRCC0_Type = Counter32
_TeraOamPmStatsTotalTRCC0_Object = MibTableColumn
teraOamPmStatsTotalTRCC0 = _TeraOamPmStatsTotalTRCC0_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 9, 1, 3),
    _TeraOamPmStatsTotalTRCC0_Type()
)
teraOamPmStatsTotalTRCC0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraOamPmStatsTotalTRCC0.setStatus("mandatory")
_TeraOamPmStatsTotalTRCC01_Type = Counter32
_TeraOamPmStatsTotalTRCC01_Object = MibTableColumn
teraOamPmStatsTotalTRCC01 = _TeraOamPmStatsTotalTRCC01_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 9, 1, 4),
    _TeraOamPmStatsTotalTRCC01_Type()
)
teraOamPmStatsTotalTRCC01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraOamPmStatsTotalTRCC01.setStatus("mandatory")


class _TeraOamPmStatsStat_Type(Integer32):
    """Custom type teraOamPmStatsStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_TeraOamPmStatsStat_Type.__name__ = "Integer32"
_TeraOamPmStatsStat_Object = MibTableColumn
teraOamPmStatsStat = _TeraOamPmStatsStat_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 9, 1, 5),
    _TeraOamPmStatsStat_Type()
)
teraOamPmStatsStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraOamPmStatsStat.setStatus("mandatory")
_TeraOamPmStatsTotalLostCLP0_Type = Counter32
_TeraOamPmStatsTotalLostCLP0_Object = MibTableColumn
teraOamPmStatsTotalLostCLP0 = _TeraOamPmStatsTotalLostCLP0_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 9, 1, 6),
    _TeraOamPmStatsTotalLostCLP0_Type()
)
teraOamPmStatsTotalLostCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraOamPmStatsTotalLostCLP0.setStatus("mandatory")
_TeraOamPmStatsTotalLostCLP01_Type = Counter32
_TeraOamPmStatsTotalLostCLP01_Object = MibTableColumn
teraOamPmStatsTotalLostCLP01 = _TeraOamPmStatsTotalLostCLP01_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 9, 1, 7),
    _TeraOamPmStatsTotalLostCLP01_Type()
)
teraOamPmStatsTotalLostCLP01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraOamPmStatsTotalLostCLP01.setStatus("mandatory")
_TeraOamPmStatsTotalMisinsertedCLP0_Type = Counter32
_TeraOamPmStatsTotalMisinsertedCLP0_Object = MibTableColumn
teraOamPmStatsTotalMisinsertedCLP0 = _TeraOamPmStatsTotalMisinsertedCLP0_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 9, 1, 8),
    _TeraOamPmStatsTotalMisinsertedCLP0_Type()
)
teraOamPmStatsTotalMisinsertedCLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraOamPmStatsTotalMisinsertedCLP0.setStatus("mandatory")
_TeraOamPmStatsTotalMisinsertedCLP01_Type = Counter32
_TeraOamPmStatsTotalMisinsertedCLP01_Object = MibTableColumn
teraOamPmStatsTotalMisinsertedCLP01 = _TeraOamPmStatsTotalMisinsertedCLP01_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 9, 1, 9),
    _TeraOamPmStatsTotalMisinsertedCLP01_Type()
)
teraOamPmStatsTotalMisinsertedCLP01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraOamPmStatsTotalMisinsertedCLP01.setStatus("mandatory")
_TeraAtmPVCIfControlTable_Object = MibTable
teraAtmPVCIfControlTable = _TeraAtmPVCIfControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 11)
)
if mibBuilder.loadTexts:
    teraAtmPVCIfControlTable.setStatus("mandatory")
_TeraAtmPVCIfControlTableEntry_Object = MibTableRow
teraAtmPVCIfControlTableEntry = _TeraAtmPVCIfControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 11, 1)
)
teraAtmPVCIfControlTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmIfIndex"),
)
if mibBuilder.loadTexts:
    teraAtmPVCIfControlTableEntry.setStatus("mandatory")


class _TeraAtmPVCIfMaxVpiBits_Type(Integer32):
    """Custom type teraAtmPVCIfMaxVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_TeraAtmPVCIfMaxVpiBits_Type.__name__ = "Integer32"
_TeraAtmPVCIfMaxVpiBits_Object = MibTableColumn
teraAtmPVCIfMaxVpiBits = _TeraAtmPVCIfMaxVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 11, 1, 1),
    _TeraAtmPVCIfMaxVpiBits_Type()
)
teraAtmPVCIfMaxVpiBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmPVCIfMaxVpiBits.setStatus("mandatory")


class _TeraAtmPVCIfMaxVciBits_Type(Integer32):
    """Custom type teraAtmPVCIfMaxVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TeraAtmPVCIfMaxVciBits_Type.__name__ = "Integer32"
_TeraAtmPVCIfMaxVciBits_Object = MibTableColumn
teraAtmPVCIfMaxVciBits = _TeraAtmPVCIfMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 11, 1, 2),
    _TeraAtmPVCIfMaxVciBits_Type()
)
teraAtmPVCIfMaxVciBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmPVCIfMaxVciBits.setStatus("mandatory")
_TeraAtmPVCIfMaxVCCs_Type = Integer32
_TeraAtmPVCIfMaxVCCs_Object = MibTableColumn
teraAtmPVCIfMaxVCCs = _TeraAtmPVCIfMaxVCCs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 11, 1, 3),
    _TeraAtmPVCIfMaxVCCs_Type()
)
teraAtmPVCIfMaxVCCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmPVCIfMaxVCCs.setStatus("mandatory")
_TeraAtmPVCIfILMIVpi_Type = Integer32
_TeraAtmPVCIfILMIVpi_Object = MibTableColumn
teraAtmPVCIfILMIVpi = _TeraAtmPVCIfILMIVpi_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 11, 1, 4),
    _TeraAtmPVCIfILMIVpi_Type()
)
teraAtmPVCIfILMIVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmPVCIfILMIVpi.setStatus("mandatory")
_TeraAtmPVCIfILMIVci_Type = Integer32
_TeraAtmPVCIfILMIVci_Object = MibTableColumn
teraAtmPVCIfILMIVci = _TeraAtmPVCIfILMIVci_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 11, 1, 5),
    _TeraAtmPVCIfILMIVci_Type()
)
teraAtmPVCIfILMIVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmPVCIfILMIVci.setStatus("mandatory")
_TeraAtmPVCIfPortBw_Type = Integer32
_TeraAtmPVCIfPortBw_Object = MibTableColumn
teraAtmPVCIfPortBw = _TeraAtmPVCIfPortBw_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 11, 1, 6),
    _TeraAtmPVCIfPortBw_Type()
)
teraAtmPVCIfPortBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmPVCIfPortBw.setStatus("mandatory")
_TeraAtmCardStatsTable_Object = MibTable
teraAtmCardStatsTable = _TeraAtmCardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 12)
)
if mibBuilder.loadTexts:
    teraAtmCardStatsTable.setStatus("mandatory")
_TeraAtmCardStatsTableEntry_Object = MibTableRow
teraAtmCardStatsTableEntry = _TeraAtmCardStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 12, 1)
)
teraAtmCardStatsTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "teraSlotIndex"),
)
if mibBuilder.loadTexts:
    teraAtmCardStatsTableEntry.setStatus("mandatory")
_TeraSlotIndex_Type = Counter32
_TeraSlotIndex_Object = MibTableColumn
teraSlotIndex = _TeraSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 12, 1, 1),
    _TeraSlotIndex_Type()
)
teraSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraSlotIndex.setStatus("mandatory")


class _TeraAtmCardStatsLSBState_Type(Integer32):
    """Custom type teraAtmCardStatsLSBState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("monitoringBus", 3),
          ("waitForBus", 2))
    )


_TeraAtmCardStatsLSBState_Type.__name__ = "Integer32"
_TeraAtmCardStatsLSBState_Object = MibTableColumn
teraAtmCardStatsLSBState = _TeraAtmCardStatsLSBState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 12, 1, 2),
    _TeraAtmCardStatsLSBState_Type()
)
teraAtmCardStatsLSBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmCardStatsLSBState.setStatus("mandatory")
_TeraAtmCardStatsLSBCrcCount_Type = Counter32
_TeraAtmCardStatsLSBCrcCount_Object = MibTableColumn
teraAtmCardStatsLSBCrcCount = _TeraAtmCardStatsLSBCrcCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 12, 1, 3),
    _TeraAtmCardStatsLSBCrcCount_Type()
)
teraAtmCardStatsLSBCrcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmCardStatsLSBCrcCount.setStatus("mandatory")
_TeraAtmCardStatsTransitionUpCount_Type = Counter32
_TeraAtmCardStatsTransitionUpCount_Object = MibTableColumn
teraAtmCardStatsTransitionUpCount = _TeraAtmCardStatsTransitionUpCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 12, 1, 4),
    _TeraAtmCardStatsTransitionUpCount_Type()
)
teraAtmCardStatsTransitionUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmCardStatsTransitionUpCount.setStatus("mandatory")
_TeraAtmCardStatsRxUnassignedCellCount_Type = Counter32
_TeraAtmCardStatsRxUnassignedCellCount_Object = MibTableColumn
teraAtmCardStatsRxUnassignedCellCount = _TeraAtmCardStatsRxUnassignedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 12, 1, 5),
    _TeraAtmCardStatsRxUnassignedCellCount_Type()
)
teraAtmCardStatsRxUnassignedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmCardStatsRxUnassignedCellCount.setStatus("mandatory")
_TeraAtmCardStatsLSBCrcLastSlot_Type = Integer32
_TeraAtmCardStatsLSBCrcLastSlot_Object = MibTableColumn
teraAtmCardStatsLSBCrcLastSlot = _TeraAtmCardStatsLSBCrcLastSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 12, 1, 6),
    _TeraAtmCardStatsLSBCrcLastSlot_Type()
)
teraAtmCardStatsLSBCrcLastSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmCardStatsLSBCrcLastSlot.setStatus("mandatory")
_TeraAtmCardStatsMrpVersion_Type = Integer32
_TeraAtmCardStatsMrpVersion_Object = MibTableColumn
teraAtmCardStatsMrpVersion = _TeraAtmCardStatsMrpVersion_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 12, 1, 7),
    _TeraAtmCardStatsMrpVersion_Type()
)
teraAtmCardStatsMrpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmCardStatsMrpVersion.setStatus("mandatory")
_TeraAtmCardStatsMrpFeature_Type = Integer32
_TeraAtmCardStatsMrpFeature_Object = MibTableColumn
teraAtmCardStatsMrpFeature = _TeraAtmCardStatsMrpFeature_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 12, 1, 8),
    _TeraAtmCardStatsMrpFeature_Type()
)
teraAtmCardStatsMrpFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmCardStatsMrpFeature.setStatus("mandatory")
_TeraAtmVclTable_Object = MibTable
teraAtmVclTable = _TeraAtmVclTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 13)
)
if mibBuilder.loadTexts:
    teraAtmVclTable.setStatus("mandatory")
_TeraAtmVclTableEntry_Object = MibTableRow
teraAtmVclTableEntry = _TeraAtmVclTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 13, 1)
)
teraAtmVclTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "ifIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "atmVclVpi"),
    (0, "TERAWAVE-teraAtom-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    teraAtmVclTableEntry.setStatus("mandatory")


class _TeraAtmVclTrafficPolicing_Type(Integer32):
    """Custom type teraAtmVclTrafficPolicing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_TeraAtmVclTrafficPolicing_Type.__name__ = "Integer32"
_TeraAtmVclTrafficPolicing_Object = MibTableColumn
teraAtmVclTrafficPolicing = _TeraAtmVclTrafficPolicing_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 13, 1, 1),
    _TeraAtmVclTrafficPolicing_Type()
)
teraAtmVclTrafficPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmVclTrafficPolicing.setStatus("mandatory")


class _TeraAtmVclRowStatus_Type(Integer32):
    """Custom type teraAtmVclRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 2))
    )


_TeraAtmVclRowStatus_Type.__name__ = "Integer32"
_TeraAtmVclRowStatus_Object = MibTableColumn
teraAtmVclRowStatus = _TeraAtmVclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 13, 1, 2),
    _TeraAtmVclRowStatus_Type()
)
teraAtmVclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmVclRowStatus.setStatus("mandatory")
_TeraAtmQueueStatsTable_Object = MibTable
teraAtmQueueStatsTable = _TeraAtmQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 14)
)
if mibBuilder.loadTexts:
    teraAtmQueueStatsTable.setStatus("mandatory")
_TeraAtmQueueStatsTableEntry_Object = MibTableRow
teraAtmQueueStatsTableEntry = _TeraAtmQueueStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 14, 1)
)
teraAtmQueueStatsTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "teraSlotIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmQueueIndex"),
)
if mibBuilder.loadTexts:
    teraAtmQueueStatsTableEntry.setStatus("mandatory")
_TeraAtmQueueIndex_Type = Integer32
_TeraAtmQueueIndex_Object = MibTableColumn
teraAtmQueueIndex = _TeraAtmQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 14, 1, 1),
    _TeraAtmQueueIndex_Type()
)
teraAtmQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmQueueIndex.setStatus("mandatory")
_TeraAtmQueueStatsSlotMask_Type = Integer32
_TeraAtmQueueStatsSlotMask_Object = MibTableColumn
teraAtmQueueStatsSlotMask = _TeraAtmQueueStatsSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 14, 1, 2),
    _TeraAtmQueueStatsSlotMask_Type()
)
teraAtmQueueStatsSlotMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmQueueStatsSlotMask.setStatus("mandatory")


class _TeraAtmQueueStatsCosType_Type(Integer32):
    """Custom type teraAtmQueueStatsCosType based on Integer32"""
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
        *(("cbr", 2),
          ("none", 1),
          ("nrtVbr", 4),
          ("rtVbr", 3),
          ("ubr", 5))
    )


_TeraAtmQueueStatsCosType_Type.__name__ = "Integer32"
_TeraAtmQueueStatsCosType_Object = MibTableColumn
teraAtmQueueStatsCosType = _TeraAtmQueueStatsCosType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 14, 1, 3),
    _TeraAtmQueueStatsCosType_Type()
)
teraAtmQueueStatsCosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmQueueStatsCosType.setStatus("mandatory")
_TeraAtmQueueStatsDiscardCellCount_Type = Counter32
_TeraAtmQueueStatsDiscardCellCount_Object = MibTableColumn
teraAtmQueueStatsDiscardCellCount = _TeraAtmQueueStatsDiscardCellCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 14, 1, 4),
    _TeraAtmQueueStatsDiscardCellCount_Type()
)
teraAtmQueueStatsDiscardCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmQueueStatsDiscardCellCount.setStatus("mandatory")
_TeraAtmMgmtChannelTable_Object = MibTable
teraAtmMgmtChannelTable = _TeraAtmMgmtChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 15)
)
if mibBuilder.loadTexts:
    teraAtmMgmtChannelTable.setStatus("mandatory")
_TeraAtmMgmtChannelTableEntry_Object = MibTableRow
teraAtmMgmtChannelTableEntry = _TeraAtmMgmtChannelTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 15, 1)
)
teraAtmMgmtChannelTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmIfIndex"),
)
if mibBuilder.loadTexts:
    teraAtmMgmtChannelTableEntry.setStatus("mandatory")


class _TeraAtmMgmtChannelVpiLow_Type(Integer32):
    """Custom type teraAtmMgmtChannelVpiLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TeraAtmMgmtChannelVpiLow_Type.__name__ = "Integer32"
_TeraAtmMgmtChannelVpiLow_Object = MibTableColumn
teraAtmMgmtChannelVpiLow = _TeraAtmMgmtChannelVpiLow_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 15, 1, 1),
    _TeraAtmMgmtChannelVpiLow_Type()
)
teraAtmMgmtChannelVpiLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmMgmtChannelVpiLow.setStatus("mandatory")


class _TeraAtmMgmtChannelVciLow_Type(Integer32):
    """Custom type teraAtmMgmtChannelVciLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TeraAtmMgmtChannelVciLow_Type.__name__ = "Integer32"
_TeraAtmMgmtChannelVciLow_Object = MibTableColumn
teraAtmMgmtChannelVciLow = _TeraAtmMgmtChannelVciLow_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 15, 1, 2),
    _TeraAtmMgmtChannelVciLow_Type()
)
teraAtmMgmtChannelVciLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmMgmtChannelVciLow.setStatus("mandatory")


class _TeraAtmMgmtChannelVpiHigh_Type(Integer32):
    """Custom type teraAtmMgmtChannelVpiHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TeraAtmMgmtChannelVpiHigh_Type.__name__ = "Integer32"
_TeraAtmMgmtChannelVpiHigh_Object = MibTableColumn
teraAtmMgmtChannelVpiHigh = _TeraAtmMgmtChannelVpiHigh_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 15, 1, 3),
    _TeraAtmMgmtChannelVpiHigh_Type()
)
teraAtmMgmtChannelVpiHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmMgmtChannelVpiHigh.setStatus("mandatory")


class _TeraAtmMgmtChannelVciHigh_Type(Integer32):
    """Custom type teraAtmMgmtChannelVciHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TeraAtmMgmtChannelVciHigh_Type.__name__ = "Integer32"
_TeraAtmMgmtChannelVciHigh_Object = MibTableColumn
teraAtmMgmtChannelVciHigh = _TeraAtmMgmtChannelVciHigh_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 15, 1, 4),
    _TeraAtmMgmtChannelVciHigh_Type()
)
teraAtmMgmtChannelVciHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmMgmtChannelVciHigh.setStatus("mandatory")
_TeraAtmDbg_ObjectIdentity = ObjectIdentity
teraAtmDbg = _TeraAtmDbg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 13, 16)
)
_TeraDebugTable_ObjectIdentity = ObjectIdentity
teraDebugTable = _TeraDebugTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 13, 16, 1)
)
_TeraDebug1_Type = Integer32
_TeraDebug1_Object = MibScalar
teraDebug1 = _TeraDebug1_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 16, 1, 1),
    _TeraDebug1_Type()
)
teraDebug1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDebug1.setStatus("mandatory")
_TeraDebug2_Type = Integer32
_TeraDebug2_Object = MibScalar
teraDebug2 = _TeraDebug2_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 16, 1, 2),
    _TeraDebug2_Type()
)
teraDebug2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDebug2.setStatus("mandatory")
_TeraDebug3_Type = Integer32
_TeraDebug3_Object = MibScalar
teraDebug3 = _TeraDebug3_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 16, 1, 3),
    _TeraDebug3_Type()
)
teraDebug3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDebug3.setStatus("mandatory")
_TeraAtmPortPVCAlarmStatTable_Object = MibTable
teraAtmPortPVCAlarmStatTable = _TeraAtmPortPVCAlarmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 17)
)
if mibBuilder.loadTexts:
    teraAtmPortPVCAlarmStatTable.setStatus("mandatory")
_TeraAtmPortPVCAlarmStatTableEntry_Object = MibTableRow
teraAtmPortPVCAlarmStatTableEntry = _TeraAtmPortPVCAlarmStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 17, 1)
)
teraAtmPortPVCAlarmStatTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "ifIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "atmVclVpi"),
    (0, "TERAWAVE-teraAtom-MIB", "atmVclVci"),
    (0, "TERAWAVE-teraAtom-MIB", "teraAtmPortPVCAlarmStatType"),
)
if mibBuilder.loadTexts:
    teraAtmPortPVCAlarmStatTableEntry.setStatus("mandatory")
_TeraAtmPortPVCAlarmStatType_Type = Integer32
_TeraAtmPortPVCAlarmStatType_Object = MibTableColumn
teraAtmPortPVCAlarmStatType = _TeraAtmPortPVCAlarmStatType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 17, 1, 1),
    _TeraAtmPortPVCAlarmStatType_Type()
)
teraAtmPortPVCAlarmStatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortPVCAlarmStatType.setStatus("mandatory")
_TeraAtmPortPVCAlarmStatVPI_Type = Integer32
_TeraAtmPortPVCAlarmStatVPI_Object = MibTableColumn
teraAtmPortPVCAlarmStatVPI = _TeraAtmPortPVCAlarmStatVPI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 17, 1, 2),
    _TeraAtmPortPVCAlarmStatVPI_Type()
)
teraAtmPortPVCAlarmStatVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortPVCAlarmStatVPI.setStatus("mandatory")
_TeraAtmPortPVCAlarmStatVCI_Type = Integer32
_TeraAtmPortPVCAlarmStatVCI_Object = MibTableColumn
teraAtmPortPVCAlarmStatVCI = _TeraAtmPortPVCAlarmStatVCI_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 17, 1, 3),
    _TeraAtmPortPVCAlarmStatVCI_Type()
)
teraAtmPortPVCAlarmStatVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortPVCAlarmStatVCI.setStatus("mandatory")
_TeraAtmPortPVCAlarmStatPort_Type = Integer32
_TeraAtmPortPVCAlarmStatPort_Object = MibTableColumn
teraAtmPortPVCAlarmStatPort = _TeraAtmPortPVCAlarmStatPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 17, 1, 4),
    _TeraAtmPortPVCAlarmStatPort_Type()
)
teraAtmPortPVCAlarmStatPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortPVCAlarmStatPort.setStatus("mandatory")
_TeraAtmPortPVCAlarmStatTime_Type = Integer32
_TeraAtmPortPVCAlarmStatTime_Object = MibTableColumn
teraAtmPortPVCAlarmStatTime = _TeraAtmPortPVCAlarmStatTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 17, 1, 5),
    _TeraAtmPortPVCAlarmStatTime_Type()
)
teraAtmPortPVCAlarmStatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortPVCAlarmStatTime.setStatus("mandatory")
_TeraAtmPortPVCAlarmStatReason_Type = Integer32
_TeraAtmPortPVCAlarmStatReason_Object = MibTableColumn
teraAtmPortPVCAlarmStatReason = _TeraAtmPortPVCAlarmStatReason_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 17, 1, 6),
    _TeraAtmPortPVCAlarmStatReason_Type()
)
teraAtmPortPVCAlarmStatReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmPortPVCAlarmStatReason.setStatus("mandatory")
_TeraAtmVplTable_Object = MibTable
teraAtmVplTable = _TeraAtmVplTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 18)
)
if mibBuilder.loadTexts:
    teraAtmVplTable.setStatus("mandatory")
_TeraAtmVplTableEntry_Object = MibTableRow
teraAtmVplTableEntry = _TeraAtmVplTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 18, 1)
)
teraAtmVplTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "ifIndex"),
    (0, "TERAWAVE-teraAtom-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    teraAtmVplTableEntry.setStatus("mandatory")


class _TeraAtmVplTrafficPolicing_Type(Integer32):
    """Custom type teraAtmVplTrafficPolicing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_TeraAtmVplTrafficPolicing_Type.__name__ = "Integer32"
_TeraAtmVplTrafficPolicing_Object = MibTableColumn
teraAtmVplTrafficPolicing = _TeraAtmVplTrafficPolicing_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 18, 1, 1),
    _TeraAtmVplTrafficPolicing_Type()
)
teraAtmVplTrafficPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmVplTrafficPolicing.setStatus("mandatory")


class _TeraAtmVplRowStatus_Type(Integer32):
    """Custom type teraAtmVplRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 2))
    )


_TeraAtmVplRowStatus_Type.__name__ = "Integer32"
_TeraAtmVplRowStatus_Object = MibTableColumn
teraAtmVplRowStatus = _TeraAtmVplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 18, 1, 2),
    _TeraAtmVplRowStatus_Type()
)
teraAtmVplRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmVplRowStatus.setStatus("mandatory")
_TeraFarEndAtmfAtmLayerTable_Object = MibTable
teraFarEndAtmfAtmLayerTable = _TeraFarEndAtmfAtmLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19)
)
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerTable.setStatus("mandatory")
_TeraFarEndAtmfAtmLayerTableEntry_Object = MibTableRow
teraFarEndAtmfAtmLayerTableEntry = _TeraFarEndAtmfAtmLayerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1)
)
teraFarEndAtmfAtmLayerTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "atmfAtmLayerIndex"),
)
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerTableEntry.setStatus("mandatory")
_TeraFarEndAtmfAtmLayerIndex_Type = Integer32
_TeraFarEndAtmfAtmLayerIndex_Object = MibTableColumn
teraFarEndAtmfAtmLayerIndex = _TeraFarEndAtmfAtmLayerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 1),
    _TeraFarEndAtmfAtmLayerIndex_Type()
)
teraFarEndAtmfAtmLayerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerIndex.setStatus("mandatory")


class _TeraFarEndAtmfAtmLayerMaxVPCs_Type(Integer32):
    """Custom type teraFarEndAtmfAtmLayerMaxVPCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TeraFarEndAtmfAtmLayerMaxVPCs_Type.__name__ = "Integer32"
_TeraFarEndAtmfAtmLayerMaxVPCs_Object = MibTableColumn
teraFarEndAtmfAtmLayerMaxVPCs = _TeraFarEndAtmfAtmLayerMaxVPCs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 2),
    _TeraFarEndAtmfAtmLayerMaxVPCs_Type()
)
teraFarEndAtmfAtmLayerMaxVPCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerMaxVPCs.setStatus("mandatory")


class _TeraFarEndAtmfAtmLayerMaxVCCs_Type(Integer32):
    """Custom type teraFarEndAtmfAtmLayerMaxVCCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435456),
    )


_TeraFarEndAtmfAtmLayerMaxVCCs_Type.__name__ = "Integer32"
_TeraFarEndAtmfAtmLayerMaxVCCs_Object = MibTableColumn
teraFarEndAtmfAtmLayerMaxVCCs = _TeraFarEndAtmfAtmLayerMaxVCCs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 3),
    _TeraFarEndAtmfAtmLayerMaxVCCs_Type()
)
teraFarEndAtmfAtmLayerMaxVCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerMaxVCCs.setStatus("mandatory")


class _TeraFarEndAtmfAtmLayerConfiguredVPCs_Type(Integer32):
    """Custom type teraFarEndAtmfAtmLayerConfiguredVPCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TeraFarEndAtmfAtmLayerConfiguredVPCs_Type.__name__ = "Integer32"
_TeraFarEndAtmfAtmLayerConfiguredVPCs_Object = MibTableColumn
teraFarEndAtmfAtmLayerConfiguredVPCs = _TeraFarEndAtmfAtmLayerConfiguredVPCs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 4),
    _TeraFarEndAtmfAtmLayerConfiguredVPCs_Type()
)
teraFarEndAtmfAtmLayerConfiguredVPCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerConfiguredVPCs.setStatus("mandatory")


class _TeraFarEndAtmfAtmLayerConfiguredVCCs_Type(Integer32):
    """Custom type teraFarEndAtmfAtmLayerConfiguredVCCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435456),
    )


_TeraFarEndAtmfAtmLayerConfiguredVCCs_Type.__name__ = "Integer32"
_TeraFarEndAtmfAtmLayerConfiguredVCCs_Object = MibTableColumn
teraFarEndAtmfAtmLayerConfiguredVCCs = _TeraFarEndAtmfAtmLayerConfiguredVCCs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 5),
    _TeraFarEndAtmfAtmLayerConfiguredVCCs_Type()
)
teraFarEndAtmfAtmLayerConfiguredVCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerConfiguredVCCs.setStatus("mandatory")


class _TeraFarEndAtmfAtmLayerMaxVpiBits_Type(Integer32):
    """Custom type teraFarEndAtmfAtmLayerMaxVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_TeraFarEndAtmfAtmLayerMaxVpiBits_Type.__name__ = "Integer32"
_TeraFarEndAtmfAtmLayerMaxVpiBits_Object = MibTableColumn
teraFarEndAtmfAtmLayerMaxVpiBits = _TeraFarEndAtmfAtmLayerMaxVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 6),
    _TeraFarEndAtmfAtmLayerMaxVpiBits_Type()
)
teraFarEndAtmfAtmLayerMaxVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerMaxVpiBits.setStatus("mandatory")


class _TeraFarEndAtmfAtmLayerMaxVciBits_Type(Integer32):
    """Custom type teraFarEndAtmfAtmLayerMaxVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TeraFarEndAtmfAtmLayerMaxVciBits_Type.__name__ = "Integer32"
_TeraFarEndAtmfAtmLayerMaxVciBits_Object = MibTableColumn
teraFarEndAtmfAtmLayerMaxVciBits = _TeraFarEndAtmfAtmLayerMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 7),
    _TeraFarEndAtmfAtmLayerMaxVciBits_Type()
)
teraFarEndAtmfAtmLayerMaxVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerMaxVciBits.setStatus("mandatory")


class _TeraFarEndAtmfAtmLayerUniType_Type(Integer32):
    """Custom type teraFarEndAtmfAtmLayerUniType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_TeraFarEndAtmfAtmLayerUniType_Type.__name__ = "Integer32"
_TeraFarEndAtmfAtmLayerUniType_Object = MibTableColumn
teraFarEndAtmfAtmLayerUniType = _TeraFarEndAtmfAtmLayerUniType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 8),
    _TeraFarEndAtmfAtmLayerUniType_Type()
)
teraFarEndAtmfAtmLayerUniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerUniType.setStatus("mandatory")


class _TeraFarEndAtmfAtmLayerUniVersion_Type(Integer32):
    """Custom type teraFarEndAtmfAtmLayerUniVersion based on Integer32"""
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
        *(("unsupported", 5),
          ("version2point0", 1),
          ("version3point0", 2),
          ("version3point1", 3),
          ("version4point0", 4))
    )


_TeraFarEndAtmfAtmLayerUniVersion_Type.__name__ = "Integer32"
_TeraFarEndAtmfAtmLayerUniVersion_Object = MibTableColumn
teraFarEndAtmfAtmLayerUniVersion = _TeraFarEndAtmfAtmLayerUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 9),
    _TeraFarEndAtmfAtmLayerUniVersion_Type()
)
teraFarEndAtmfAtmLayerUniVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerUniVersion.setStatus("mandatory")


class _TeraFarEndAtmfAtmLayerDeviceType_Type(Integer32):
    """Custom type teraFarEndAtmfAtmLayerDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 2),
          ("user", 1))
    )


_TeraFarEndAtmfAtmLayerDeviceType_Type.__name__ = "Integer32"
_TeraFarEndAtmfAtmLayerDeviceType_Object = MibTableColumn
teraFarEndAtmfAtmLayerDeviceType = _TeraFarEndAtmfAtmLayerDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 10),
    _TeraFarEndAtmfAtmLayerDeviceType_Type()
)
teraFarEndAtmfAtmLayerDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerDeviceType.setStatus("mandatory")


class _TeraFarEndAtmfAtmLayerIlmiVersion_Type(Integer32):
    """Custom type teraFarEndAtmfAtmLayerIlmiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("version4point0", 2))
    )


_TeraFarEndAtmfAtmLayerIlmiVersion_Type.__name__ = "Integer32"
_TeraFarEndAtmfAtmLayerIlmiVersion_Object = MibTableColumn
teraFarEndAtmfAtmLayerIlmiVersion = _TeraFarEndAtmfAtmLayerIlmiVersion_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 11),
    _TeraFarEndAtmfAtmLayerIlmiVersion_Type()
)
teraFarEndAtmfAtmLayerIlmiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerIlmiVersion.setStatus("mandatory")


class _TeraFarEndAtmfAtmLayerNniSigVersion_Type(Integer32):
    """Custom type teraFarEndAtmfAtmLayerNniSigVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iisp", 2),
          ("pnniVersion1point0", 3),
          ("unsupported", 1))
    )


_TeraFarEndAtmfAtmLayerNniSigVersion_Type.__name__ = "Integer32"
_TeraFarEndAtmfAtmLayerNniSigVersion_Object = MibTableColumn
teraFarEndAtmfAtmLayerNniSigVersion = _TeraFarEndAtmfAtmLayerNniSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 12),
    _TeraFarEndAtmfAtmLayerNniSigVersion_Type()
)
teraFarEndAtmfAtmLayerNniSigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerNniSigVersion.setStatus("mandatory")


class _TeraFarEndAtmfAtmLayerMaxSvpcVpi_Type(Integer32):
    """Custom type teraFarEndAtmfAtmLayerMaxSvpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TeraFarEndAtmfAtmLayerMaxSvpcVpi_Type.__name__ = "Integer32"
_TeraFarEndAtmfAtmLayerMaxSvpcVpi_Object = MibTableColumn
teraFarEndAtmfAtmLayerMaxSvpcVpi = _TeraFarEndAtmfAtmLayerMaxSvpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 13),
    _TeraFarEndAtmfAtmLayerMaxSvpcVpi_Type()
)
teraFarEndAtmfAtmLayerMaxSvpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerMaxSvpcVpi.setStatus("mandatory")


class _TeraFarEndAtmfAtmLayerMaxSvccVpi_Type(Integer32):
    """Custom type teraFarEndAtmfAtmLayerMaxSvccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TeraFarEndAtmfAtmLayerMaxSvccVpi_Type.__name__ = "Integer32"
_TeraFarEndAtmfAtmLayerMaxSvccVpi_Object = MibTableColumn
teraFarEndAtmfAtmLayerMaxSvccVpi = _TeraFarEndAtmfAtmLayerMaxSvccVpi_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 14),
    _TeraFarEndAtmfAtmLayerMaxSvccVpi_Type()
)
teraFarEndAtmfAtmLayerMaxSvccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerMaxSvccVpi.setStatus("mandatory")


class _TeraFarEndAtmfAtmLayerMinSvccVci_Type(Integer32):
    """Custom type teraFarEndAtmfAtmLayerMinSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_TeraFarEndAtmfAtmLayerMinSvccVci_Type.__name__ = "Integer32"
_TeraFarEndAtmfAtmLayerMinSvccVci_Object = MibTableColumn
teraFarEndAtmfAtmLayerMinSvccVci = _TeraFarEndAtmfAtmLayerMinSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 19, 1, 15),
    _TeraFarEndAtmfAtmLayerMinSvccVci_Type()
)
teraFarEndAtmfAtmLayerMinSvccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfAtmLayerMinSvccVci.setStatus("mandatory")
_TeraFarEndAtmfVccTable_Object = MibTable
teraFarEndAtmfVccTable = _TeraFarEndAtmfVccTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20)
)
if mibBuilder.loadTexts:
    teraFarEndAtmfVccTable.setStatus("mandatory")
_TeraFarEndAtmfVccTableEntry_Object = MibTableRow
teraFarEndAtmfVccTableEntry = _TeraFarEndAtmfVccTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1)
)
teraFarEndAtmfVccTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAtom-MIB", "atmfVccPortIndex"),
)
if mibBuilder.loadTexts:
    teraFarEndAtmfVccTableEntry.setStatus("mandatory")


class _TeraFarEndAtmfVccPortIndex_Type(Integer32):
    """Custom type teraFarEndAtmfVccPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TeraFarEndAtmfVccPortIndex_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccPortIndex_Object = MibTableColumn
teraFarEndAtmfVccPortIndex = _TeraFarEndAtmfVccPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 1),
    _TeraFarEndAtmfVccPortIndex_Type()
)
teraFarEndAtmfVccPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccPortIndex.setStatus("mandatory")


class _TeraFarEndAtmfVccVpi_Type(Integer32):
    """Custom type teraFarEndAtmfVccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TeraFarEndAtmfVccVpi_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccVpi_Object = MibTableColumn
teraFarEndAtmfVccVpi = _TeraFarEndAtmfVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 2),
    _TeraFarEndAtmfVccVpi_Type()
)
teraFarEndAtmfVccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccVpi.setStatus("mandatory")


class _TeraFarEndAtmfVccVci_Type(Integer32):
    """Custom type teraFarEndAtmfVccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TeraFarEndAtmfVccVci_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccVci_Object = MibTableColumn
teraFarEndAtmfVccVci = _TeraFarEndAtmfVccVci_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 3),
    _TeraFarEndAtmfVccVci_Type()
)
teraFarEndAtmfVccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccVci.setStatus("mandatory")


class _TeraFarEndAtmfVccOperStatus_Type(Integer32):
    """Custom type teraFarEndAtmfVccOperStatus based on Integer32"""
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
        *(("end2endDown", 3),
          ("end2endUp", 2),
          ("localDown", 5),
          ("localUpEnd2endUnknown", 4),
          ("unknown", 1))
    )


_TeraFarEndAtmfVccOperStatus_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccOperStatus_Object = MibTableColumn
teraFarEndAtmfVccOperStatus = _TeraFarEndAtmfVccOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 4),
    _TeraFarEndAtmfVccOperStatus_Type()
)
teraFarEndAtmfVccOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccOperStatus.setStatus("mandatory")
_TeraFarEndAtmfVccTransmitTrafficDescriptorType_Type = ObjectIdentifier
_TeraFarEndAtmfVccTransmitTrafficDescriptorType_Object = MibTableColumn
teraFarEndAtmfVccTransmitTrafficDescriptorType = _TeraFarEndAtmfVccTransmitTrafficDescriptorType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 5),
    _TeraFarEndAtmfVccTransmitTrafficDescriptorType_Type()
)
teraFarEndAtmfVccTransmitTrafficDescriptorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccTransmitTrafficDescriptorType.setStatus("mandatory")


class _TeraFarEndAtmfVccTransmitTrafficDescriptorParam1_Type(Integer32):
    """Custom type teraFarEndAtmfVccTransmitTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TeraFarEndAtmfVccTransmitTrafficDescriptorParam1_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccTransmitTrafficDescriptorParam1_Object = MibTableColumn
teraFarEndAtmfVccTransmitTrafficDescriptorParam1 = _TeraFarEndAtmfVccTransmitTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 6),
    _TeraFarEndAtmfVccTransmitTrafficDescriptorParam1_Type()
)
teraFarEndAtmfVccTransmitTrafficDescriptorParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccTransmitTrafficDescriptorParam1.setStatus("mandatory")


class _TeraFarEndAtmfVccTransmitTrafficDescriptorParam2_Type(Integer32):
    """Custom type teraFarEndAtmfVccTransmitTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TeraFarEndAtmfVccTransmitTrafficDescriptorParam2_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccTransmitTrafficDescriptorParam2_Object = MibTableColumn
teraFarEndAtmfVccTransmitTrafficDescriptorParam2 = _TeraFarEndAtmfVccTransmitTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 7),
    _TeraFarEndAtmfVccTransmitTrafficDescriptorParam2_Type()
)
teraFarEndAtmfVccTransmitTrafficDescriptorParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccTransmitTrafficDescriptorParam2.setStatus("mandatory")


class _TeraFarEndAtmfVccTransmitTrafficDescriptorParam3_Type(Integer32):
    """Custom type teraFarEndAtmfVccTransmitTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TeraFarEndAtmfVccTransmitTrafficDescriptorParam3_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccTransmitTrafficDescriptorParam3_Object = MibTableColumn
teraFarEndAtmfVccTransmitTrafficDescriptorParam3 = _TeraFarEndAtmfVccTransmitTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 8),
    _TeraFarEndAtmfVccTransmitTrafficDescriptorParam3_Type()
)
teraFarEndAtmfVccTransmitTrafficDescriptorParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccTransmitTrafficDescriptorParam3.setStatus("mandatory")


class _TeraFarEndAtmfVccTransmitTrafficDescriptorParam4_Type(Integer32):
    """Custom type teraFarEndAtmfVccTransmitTrafficDescriptorParam4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TeraFarEndAtmfVccTransmitTrafficDescriptorParam4_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccTransmitTrafficDescriptorParam4_Object = MibTableColumn
teraFarEndAtmfVccTransmitTrafficDescriptorParam4 = _TeraFarEndAtmfVccTransmitTrafficDescriptorParam4_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 9),
    _TeraFarEndAtmfVccTransmitTrafficDescriptorParam4_Type()
)
teraFarEndAtmfVccTransmitTrafficDescriptorParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccTransmitTrafficDescriptorParam4.setStatus("mandatory")


class _TeraFarEndAtmfVccTransmitTrafficDescriptorParam5_Type(Integer32):
    """Custom type teraFarEndAtmfVccTransmitTrafficDescriptorParam5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TeraFarEndAtmfVccTransmitTrafficDescriptorParam5_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccTransmitTrafficDescriptorParam5_Object = MibTableColumn
teraFarEndAtmfVccTransmitTrafficDescriptorParam5 = _TeraFarEndAtmfVccTransmitTrafficDescriptorParam5_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 10),
    _TeraFarEndAtmfVccTransmitTrafficDescriptorParam5_Type()
)
teraFarEndAtmfVccTransmitTrafficDescriptorParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccTransmitTrafficDescriptorParam5.setStatus("mandatory")
_TeraFarEndAtmfVccReceiveTrafficDescriptorType_Type = ObjectIdentifier
_TeraFarEndAtmfVccReceiveTrafficDescriptorType_Object = MibTableColumn
teraFarEndAtmfVccReceiveTrafficDescriptorType = _TeraFarEndAtmfVccReceiveTrafficDescriptorType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 11),
    _TeraFarEndAtmfVccReceiveTrafficDescriptorType_Type()
)
teraFarEndAtmfVccReceiveTrafficDescriptorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccReceiveTrafficDescriptorType.setStatus("mandatory")


class _TeraFarEndAtmfVccReceiveTrafficDescriptorParam1_Type(Integer32):
    """Custom type teraFarEndAtmfVccReceiveTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TeraFarEndAtmfVccReceiveTrafficDescriptorParam1_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccReceiveTrafficDescriptorParam1_Object = MibTableColumn
teraFarEndAtmfVccReceiveTrafficDescriptorParam1 = _TeraFarEndAtmfVccReceiveTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 12),
    _TeraFarEndAtmfVccReceiveTrafficDescriptorParam1_Type()
)
teraFarEndAtmfVccReceiveTrafficDescriptorParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccReceiveTrafficDescriptorParam1.setStatus("mandatory")


class _TeraFarEndAtmfVccReceiveTrafficDescriptorParam2_Type(Integer32):
    """Custom type teraFarEndAtmfVccReceiveTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TeraFarEndAtmfVccReceiveTrafficDescriptorParam2_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccReceiveTrafficDescriptorParam2_Object = MibTableColumn
teraFarEndAtmfVccReceiveTrafficDescriptorParam2 = _TeraFarEndAtmfVccReceiveTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 13),
    _TeraFarEndAtmfVccReceiveTrafficDescriptorParam2_Type()
)
teraFarEndAtmfVccReceiveTrafficDescriptorParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccReceiveTrafficDescriptorParam2.setStatus("mandatory")


class _TeraFarEndAtmfVccReceiveTrafficDescriptorParam3_Type(Integer32):
    """Custom type teraFarEndAtmfVccReceiveTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TeraFarEndAtmfVccReceiveTrafficDescriptorParam3_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccReceiveTrafficDescriptorParam3_Object = MibTableColumn
teraFarEndAtmfVccReceiveTrafficDescriptorParam3 = _TeraFarEndAtmfVccReceiveTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 14),
    _TeraFarEndAtmfVccReceiveTrafficDescriptorParam3_Type()
)
teraFarEndAtmfVccReceiveTrafficDescriptorParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccReceiveTrafficDescriptorParam3.setStatus("mandatory")


class _TeraFarEndAtmfVccReceiveTrafficDescriptorParam4_Type(Integer32):
    """Custom type teraFarEndAtmfVccReceiveTrafficDescriptorParam4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TeraFarEndAtmfVccReceiveTrafficDescriptorParam4_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccReceiveTrafficDescriptorParam4_Object = MibTableColumn
teraFarEndAtmfVccReceiveTrafficDescriptorParam4 = _TeraFarEndAtmfVccReceiveTrafficDescriptorParam4_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 15),
    _TeraFarEndAtmfVccReceiveTrafficDescriptorParam4_Type()
)
teraFarEndAtmfVccReceiveTrafficDescriptorParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccReceiveTrafficDescriptorParam4.setStatus("mandatory")


class _TeraFarEndAtmfVccReceiveTrafficDescriptorParam5_Type(Integer32):
    """Custom type teraFarEndAtmfVccReceiveTrafficDescriptorParam5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TeraFarEndAtmfVccReceiveTrafficDescriptorParam5_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccReceiveTrafficDescriptorParam5_Object = MibTableColumn
teraFarEndAtmfVccReceiveTrafficDescriptorParam5 = _TeraFarEndAtmfVccReceiveTrafficDescriptorParam5_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 16),
    _TeraFarEndAtmfVccReceiveTrafficDescriptorParam5_Type()
)
teraFarEndAtmfVccReceiveTrafficDescriptorParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccReceiveTrafficDescriptorParam5.setStatus("mandatory")


class _TeraFarEndAtmfVccQoSCategory_Type(Integer32):
    """Custom type teraFarEndAtmfVccQoSCategory based on Integer32"""
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
        *(("deterministic", 2),
          ("other", 1),
          ("statistical", 3),
          ("unspecified", 4))
    )


_TeraFarEndAtmfVccQoSCategory_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccQoSCategory_Object = MibTableColumn
teraFarEndAtmfVccQoSCategory = _TeraFarEndAtmfVccQoSCategory_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 17),
    _TeraFarEndAtmfVccQoSCategory_Type()
)
teraFarEndAtmfVccQoSCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccQoSCategory.setStatus("mandatory")


class _TeraFarEndAtmfVccTransmitQoSClass_Type(Integer32):
    """Custom type teraFarEndAtmfVccTransmitQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TeraFarEndAtmfVccTransmitQoSClass_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccTransmitQoSClass_Object = MibTableColumn
teraFarEndAtmfVccTransmitQoSClass = _TeraFarEndAtmfVccTransmitQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 18),
    _TeraFarEndAtmfVccTransmitQoSClass_Type()
)
teraFarEndAtmfVccTransmitQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccTransmitQoSClass.setStatus("mandatory")


class _TeraFarEndAtmfVccReceiveQoSClass_Type(Integer32):
    """Custom type teraFarEndAtmfVccReceiveQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TeraFarEndAtmfVccReceiveQoSClass_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccReceiveQoSClass_Object = MibTableColumn
teraFarEndAtmfVccReceiveQoSClass = _TeraFarEndAtmfVccReceiveQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 19),
    _TeraFarEndAtmfVccReceiveQoSClass_Type()
)
teraFarEndAtmfVccReceiveQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccReceiveQoSClass.setStatus("mandatory")


class _TeraFarEndAtmfVccBestEffortIndicator_Type(Integer32):
    """Custom type teraFarEndAtmfVccBestEffortIndicator based on Integer32"""
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


_TeraFarEndAtmfVccBestEffortIndicator_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccBestEffortIndicator_Object = MibTableColumn
teraFarEndAtmfVccBestEffortIndicator = _TeraFarEndAtmfVccBestEffortIndicator_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 20),
    _TeraFarEndAtmfVccBestEffortIndicator_Type()
)
teraFarEndAtmfVccBestEffortIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccBestEffortIndicator.setStatus("mandatory")


class _TeraFarEndAtmfVccTransmitFrameDiscard_Type(Integer32):
    """Custom type teraFarEndAtmfVccTransmitFrameDiscard based on Integer32"""
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


_TeraFarEndAtmfVccTransmitFrameDiscard_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccTransmitFrameDiscard_Object = MibTableColumn
teraFarEndAtmfVccTransmitFrameDiscard = _TeraFarEndAtmfVccTransmitFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 21),
    _TeraFarEndAtmfVccTransmitFrameDiscard_Type()
)
teraFarEndAtmfVccTransmitFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccTransmitFrameDiscard.setStatus("mandatory")


class _TeraFarEndAtmfVccReceiveFrameDiscard_Type(Integer32):
    """Custom type teraFarEndAtmfVccReceiveFrameDiscard based on Integer32"""
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


_TeraFarEndAtmfVccReceiveFrameDiscard_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccReceiveFrameDiscard_Object = MibTableColumn
teraFarEndAtmfVccReceiveFrameDiscard = _TeraFarEndAtmfVccReceiveFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 22),
    _TeraFarEndAtmfVccReceiveFrameDiscard_Type()
)
teraFarEndAtmfVccReceiveFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccReceiveFrameDiscard.setStatus("mandatory")


class _TeraFarEndAtmfVccServiceCategory_Type(Integer32):
    """Custom type teraFarEndAtmfVccServiceCategory based on Integer32"""
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
        *(("abr", 5),
          ("cbr", 2),
          ("nrtVbr", 4),
          ("other", 1),
          ("rtVbr", 3),
          ("ubr", 6))
    )


_TeraFarEndAtmfVccServiceCategory_Type.__name__ = "Integer32"
_TeraFarEndAtmfVccServiceCategory_Object = MibTableColumn
teraFarEndAtmfVccServiceCategory = _TeraFarEndAtmfVccServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 4513, 13, 20, 1, 23),
    _TeraFarEndAtmfVccServiceCategory_Type()
)
teraFarEndAtmfVccServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraFarEndAtmfVccServiceCategory.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraAtom-MIB",
    **{"terawave": terawave,
       "teraATMGroup": teraATMGroup,
       "teraATMSubGroup1": teraATMSubGroup1,
       "teraAtmStatsSumTable": teraAtmStatsSumTable,
       "teraAtmStatsSumTableEntry": teraAtmStatsSumTableEntry,
       "teraAtmIfIndex": teraAtmIfIndex,
       "teraAtmVpi": teraAtmVpi,
       "teraAtmVci": teraAtmVci,
       "teraAtmStatsSumReceivedCells": teraAtmStatsSumReceivedCells,
       "teraAtmStatsSumReceivedDiscardCells": teraAtmStatsSumReceivedDiscardCells,
       "teraAtmStatsSumReceivedTaggedCells": teraAtmStatsSumReceivedTaggedCells,
       "teraAtmStatsSumTransmittedCells": teraAtmStatsSumTransmittedCells,
       "teraAtmStatsTable": teraAtmStatsTable,
       "teraAtmStatsTableEntry": teraAtmStatsTableEntry,
       "teraAtmStatsReceivedUserClp0Cells": teraAtmStatsReceivedUserClp0Cells,
       "teraAtmStatsReceivedUserClp1Cells": teraAtmStatsReceivedUserClp1Cells,
       "teraAtmStatsReceivedOamClp0Cells": teraAtmStatsReceivedOamClp0Cells,
       "teraAtmStatsReceivedOamClp1Cells": teraAtmStatsReceivedOamClp1Cells,
       "teraAtmStatsReceivedDiscardClp0Cells": teraAtmStatsReceivedDiscardClp0Cells,
       "teraAtmStatsReceivedDiscardClp1Cells": teraAtmStatsReceivedDiscardClp1Cells,
       "teraAtmStatsReceivedTaggedCells": teraAtmStatsReceivedTaggedCells,
       "teraAtmStatsTransmittedUserClp0Cells": teraAtmStatsTransmittedUserClp0Cells,
       "teraAtmStatsTransmittedUserClp1Cells": teraAtmStatsTransmittedUserClp1Cells,
       "teraAtmStatsTransmittedOamClp0Cells": teraAtmStatsTransmittedOamClp0Cells,
       "teraAtmStatsTransmittedOamClp1Cells": teraAtmStatsTransmittedOamClp1Cells,
       "teraAtmStatsClearTable": teraAtmStatsClearTable,
       "teraAtmStatsClearTableEntry": teraAtmStatsClearTableEntry,
       "teraAtmStatsStat": teraAtmStatsStat,
       "teraATMSubGroup2": teraATMSubGroup2,
       "teraAtmHistoryControlTable": teraAtmHistoryControlTable,
       "teraAtmHistoryControlTableEntry": teraAtmHistoryControlTableEntry,
       "teraAtmHistoryControlIndex": teraAtmHistoryControlIndex,
       "teraAtmHistoryControlBucketsRequested": teraAtmHistoryControlBucketsRequested,
       "teraAtmHistoryControlBucketsGranted": teraAtmHistoryControlBucketsGranted,
       "teraAtmHistoryControlInterval": teraAtmHistoryControlInterval,
       "teraAtmHistoryControlStatus": teraAtmHistoryControlStatus,
       "teraAtmStatsHistoryTable": teraAtmStatsHistoryTable,
       "teraAtmStatsHistoryTableEntry": teraAtmStatsHistoryTableEntry,
       "teraAtmStatsHistorySampleIndex": teraAtmStatsHistorySampleIndex,
       "teraAtmStatsHistoryIntervalStart": teraAtmStatsHistoryIntervalStart,
       "teraAtmStatsHistoryReceivedUserClp0Cells": teraAtmStatsHistoryReceivedUserClp0Cells,
       "teraAtmStatsHistoryReceivedUserClp1Cells": teraAtmStatsHistoryReceivedUserClp1Cells,
       "teraAtmStatsHistoryReceivedOamClp0Cells": teraAtmStatsHistoryReceivedOamClp0Cells,
       "teraAtmStatsHistoryReceivedOamClp1Cells": teraAtmStatsHistoryReceivedOamClp1Cells,
       "teraAtmStatsHistoryReceivedDiscardClp0Cells": teraAtmStatsHistoryReceivedDiscardClp0Cells,
       "teraAtmStatsHistoryReceivedDiscardClp1Cells": teraAtmStatsHistoryReceivedDiscardClp1Cells,
       "teraAtmStatsHistoryReceivedTaggedCells": teraAtmStatsHistoryReceivedTaggedCells,
       "teraAtmStatsHistoryTransmittedUserClp0Cells": teraAtmStatsHistoryTransmittedUserClp0Cells,
       "teraAtmStatsHistoryTransmittedUserClp1Cells": teraAtmStatsHistoryTransmittedUserClp1Cells,
       "teraAtmStatsHistoryTransmittedOamClp0Cells": teraAtmStatsHistoryTransmittedOamClp0Cells,
       "teraAtmStatsHistoryTransmittedOamClp1Cells": teraAtmStatsHistoryTransmittedOamClp1Cells,
       "teraATMSubGroup3": teraATMSubGroup3,
       "teraAtmILMIPollCfgTable": teraAtmILMIPollCfgTable,
       "teraDefaultRegainTimeout": teraDefaultRegainTimeout,
       "teraDefaultTestConnectTimeout": teraDefaultTestConnectTimeout,
       "teraDefaultAllowedNumOfFailed": teraDefaultAllowedNumOfFailed,
       "teraATMPhyStatTable": teraATMPhyStatTable,
       "teraATMPhyStatTableEntry": teraATMPhyStatTableEntry,
       "teraATM-Seconds": teraATM_Seconds,
       "teraATM-CorrectHCSError": teraATM_CorrectHCSError,
       "teraATM-UncorrectHCSError": teraATM_UncorrectHCSError,
       "teraATM-ReceiveCell": teraATM_ReceiveCell,
       "teraATM-IDLECell": teraATM_IDLECell,
       "teraATM-TransmitCell": teraATM_TransmitCell,
       "teraATM-AdminStatus": teraATM_AdminStatus,
       "teraAtmPortStatsTable": teraAtmPortStatsTable,
       "teraAtmPortStatsTableEntry": teraAtmPortStatsTableEntry,
       "teraAtmPortStatsIngressUnassignedCells": teraAtmPortStatsIngressUnassignedCells,
       "teraAtmPortStatsEgressUnassignedCells": teraAtmPortStatsEgressUnassignedCells,
       "teraAtmPortStatsTransmittedClp0Cells": teraAtmPortStatsTransmittedClp0Cells,
       "teraAtmPortStatsTransmittedClp1Cells": teraAtmPortStatsTransmittedClp1Cells,
       "teraAtmPortStatsReceivedClp0Cells": teraAtmPortStatsReceivedClp0Cells,
       "teraAtmPortStatsReceivedClp1Cells": teraAtmPortStatsReceivedClp1Cells,
       "teraAtmPortStatsReceivedOamCells": teraAtmPortStatsReceivedOamCells,
       "teraAtmPortStatsReceivedRmCells": teraAtmPortStatsReceivedRmCells,
       "teraAtmPortStatsReceivedErroredOamCells": teraAtmPortStatsReceivedErroredOamCells,
       "teraAtmPortStatsReceivedErroredRmCells": teraAtmPortStatsReceivedErroredRmCells,
       "teraAtmPortStatsReceivedNonZerroGfcCells": teraAtmPortStatsReceivedNonZerroGfcCells,
       "teraAtmPortStatsHistoryTable": teraAtmPortStatsHistoryTable,
       "teraAtmPortStatsHistoryTableEntry": teraAtmPortStatsHistoryTableEntry,
       "teraAtmPortStatsHistoryIngressUnassignedCells": teraAtmPortStatsHistoryIngressUnassignedCells,
       "teraAtmPortStatsHistoryEgressUnassignedCells": teraAtmPortStatsHistoryEgressUnassignedCells,
       "teraAtmPortStatsHistoryTransmittedClp0Cells": teraAtmPortStatsHistoryTransmittedClp0Cells,
       "teraAtmPortStatsHistoryTransmittedClp1Cells": teraAtmPortStatsHistoryTransmittedClp1Cells,
       "teraAtmPortStatsHistoryReceivedClp0Cells": teraAtmPortStatsHistoryReceivedClp0Cells,
       "teraAtmPortStatsHistoryReceivedClp1Cells": teraAtmPortStatsHistoryReceivedClp1Cells,
       "teraAtmPortStatsHistoryReceivedOamCells": teraAtmPortStatsHistoryReceivedOamCells,
       "teraAtmPortStatsHistoryReceivedRmCells": teraAtmPortStatsHistoryReceivedRmCells,
       "teraAtmPortStatsHistoryReceivedErroredOamCells": teraAtmPortStatsHistoryReceivedErroredOamCells,
       "teraAtmPortStatsHistoryReceivedErroredRmCells": teraAtmPortStatsHistoryReceivedErroredRmCells,
       "teraAtmPortStatsHistoryReceivedNonZerroGfcCells": teraAtmPortStatsHistoryReceivedNonZerroGfcCells,
       "teraAtmCc": teraAtmCc,
       "teraAtmCcControlTable": teraAtmCcControlTable,
       "teraAtmCcControlTableEntry": teraAtmCcControlTableEntry,
       "teraAtmCcSourceControl": teraAtmCcSourceControl,
       "teraAtmCcSinkControl": teraAtmCcSinkControl,
       "teraAtmCcType": teraAtmCcType,
       "teraAtmCcTargetDir": teraAtmCcTargetDir,
       "teraAtmCcSinkDir": teraAtmCcSinkDir,
       "teraAtmCcSourceResult": teraAtmCcSourceResult,
       "teraAtmCcSinkResult": teraAtmCcSinkResult,
       "teraAtmCcRowStatus": teraAtmCcRowStatus,
       "teraAtmPmControlTable": teraAtmPmControlTable,
       "teraAtmPmControlTableEntry": teraAtmPmControlTableEntry,
       "teraAtmPmSourceControl": teraAtmPmSourceControl,
       "teraAtmPmSourceBlockSize": teraAtmPmSourceBlockSize,
       "teraAtmPmSinkControl": teraAtmPmSinkControl,
       "teraAtmPmSourceType": teraAtmPmSourceType,
       "teraAtmPmTargetDir": teraAtmPmTargetDir,
       "teraAtmPmSinkDir": teraAtmPmSinkDir,
       "teraAtmPmSourceResult": teraAtmPmSourceResult,
       "teraAtmPmSinkResult": teraAtmPmSinkResult,
       "teraAtmPmRowStatus": teraAtmPmRowStatus,
       "teraOamPmStatsTable": teraOamPmStatsTable,
       "teraOamPmStatsTableEntry": teraOamPmStatsTableEntry,
       "teraOamPmStatsTotalTUC0": teraOamPmStatsTotalTUC0,
       "teraOamPmStatsTotalTUC01": teraOamPmStatsTotalTUC01,
       "teraOamPmStatsTotalTRCC0": teraOamPmStatsTotalTRCC0,
       "teraOamPmStatsTotalTRCC01": teraOamPmStatsTotalTRCC01,
       "teraOamPmStatsStat": teraOamPmStatsStat,
       "teraOamPmStatsTotalLostCLP0": teraOamPmStatsTotalLostCLP0,
       "teraOamPmStatsTotalLostCLP01": teraOamPmStatsTotalLostCLP01,
       "teraOamPmStatsTotalMisinsertedCLP0": teraOamPmStatsTotalMisinsertedCLP0,
       "teraOamPmStatsTotalMisinsertedCLP01": teraOamPmStatsTotalMisinsertedCLP01,
       "teraAtmPVCIfControlTable": teraAtmPVCIfControlTable,
       "teraAtmPVCIfControlTableEntry": teraAtmPVCIfControlTableEntry,
       "teraAtmPVCIfMaxVpiBits": teraAtmPVCIfMaxVpiBits,
       "teraAtmPVCIfMaxVciBits": teraAtmPVCIfMaxVciBits,
       "teraAtmPVCIfMaxVCCs": teraAtmPVCIfMaxVCCs,
       "teraAtmPVCIfILMIVpi": teraAtmPVCIfILMIVpi,
       "teraAtmPVCIfILMIVci": teraAtmPVCIfILMIVci,
       "teraAtmPVCIfPortBw": teraAtmPVCIfPortBw,
       "teraAtmCardStatsTable": teraAtmCardStatsTable,
       "teraAtmCardStatsTableEntry": teraAtmCardStatsTableEntry,
       "teraSlotIndex": teraSlotIndex,
       "teraAtmCardStatsLSBState": teraAtmCardStatsLSBState,
       "teraAtmCardStatsLSBCrcCount": teraAtmCardStatsLSBCrcCount,
       "teraAtmCardStatsTransitionUpCount": teraAtmCardStatsTransitionUpCount,
       "teraAtmCardStatsRxUnassignedCellCount": teraAtmCardStatsRxUnassignedCellCount,
       "teraAtmCardStatsLSBCrcLastSlot": teraAtmCardStatsLSBCrcLastSlot,
       "teraAtmCardStatsMrpVersion": teraAtmCardStatsMrpVersion,
       "teraAtmCardStatsMrpFeature": teraAtmCardStatsMrpFeature,
       "teraAtmVclTable": teraAtmVclTable,
       "teraAtmVclTableEntry": teraAtmVclTableEntry,
       "teraAtmVclTrafficPolicing": teraAtmVclTrafficPolicing,
       "teraAtmVclRowStatus": teraAtmVclRowStatus,
       "teraAtmQueueStatsTable": teraAtmQueueStatsTable,
       "teraAtmQueueStatsTableEntry": teraAtmQueueStatsTableEntry,
       "teraAtmQueueIndex": teraAtmQueueIndex,
       "teraAtmQueueStatsSlotMask": teraAtmQueueStatsSlotMask,
       "teraAtmQueueStatsCosType": teraAtmQueueStatsCosType,
       "teraAtmQueueStatsDiscardCellCount": teraAtmQueueStatsDiscardCellCount,
       "teraAtmMgmtChannelTable": teraAtmMgmtChannelTable,
       "teraAtmMgmtChannelTableEntry": teraAtmMgmtChannelTableEntry,
       "teraAtmMgmtChannelVpiLow": teraAtmMgmtChannelVpiLow,
       "teraAtmMgmtChannelVciLow": teraAtmMgmtChannelVciLow,
       "teraAtmMgmtChannelVpiHigh": teraAtmMgmtChannelVpiHigh,
       "teraAtmMgmtChannelVciHigh": teraAtmMgmtChannelVciHigh,
       "teraAtmDbg": teraAtmDbg,
       "teraDebugTable": teraDebugTable,
       "teraDebug1": teraDebug1,
       "teraDebug2": teraDebug2,
       "teraDebug3": teraDebug3,
       "teraAtmPortPVCAlarmStatTable": teraAtmPortPVCAlarmStatTable,
       "teraAtmPortPVCAlarmStatTableEntry": teraAtmPortPVCAlarmStatTableEntry,
       "teraAtmPortPVCAlarmStatType": teraAtmPortPVCAlarmStatType,
       "teraAtmPortPVCAlarmStatVPI": teraAtmPortPVCAlarmStatVPI,
       "teraAtmPortPVCAlarmStatVCI": teraAtmPortPVCAlarmStatVCI,
       "teraAtmPortPVCAlarmStatPort": teraAtmPortPVCAlarmStatPort,
       "teraAtmPortPVCAlarmStatTime": teraAtmPortPVCAlarmStatTime,
       "teraAtmPortPVCAlarmStatReason": teraAtmPortPVCAlarmStatReason,
       "teraAtmVplTable": teraAtmVplTable,
       "teraAtmVplTableEntry": teraAtmVplTableEntry,
       "teraAtmVplTrafficPolicing": teraAtmVplTrafficPolicing,
       "teraAtmVplRowStatus": teraAtmVplRowStatus,
       "teraFarEndAtmfAtmLayerTable": teraFarEndAtmfAtmLayerTable,
       "teraFarEndAtmfAtmLayerTableEntry": teraFarEndAtmfAtmLayerTableEntry,
       "teraFarEndAtmfAtmLayerIndex": teraFarEndAtmfAtmLayerIndex,
       "teraFarEndAtmfAtmLayerMaxVPCs": teraFarEndAtmfAtmLayerMaxVPCs,
       "teraFarEndAtmfAtmLayerMaxVCCs": teraFarEndAtmfAtmLayerMaxVCCs,
       "teraFarEndAtmfAtmLayerConfiguredVPCs": teraFarEndAtmfAtmLayerConfiguredVPCs,
       "teraFarEndAtmfAtmLayerConfiguredVCCs": teraFarEndAtmfAtmLayerConfiguredVCCs,
       "teraFarEndAtmfAtmLayerMaxVpiBits": teraFarEndAtmfAtmLayerMaxVpiBits,
       "teraFarEndAtmfAtmLayerMaxVciBits": teraFarEndAtmfAtmLayerMaxVciBits,
       "teraFarEndAtmfAtmLayerUniType": teraFarEndAtmfAtmLayerUniType,
       "teraFarEndAtmfAtmLayerUniVersion": teraFarEndAtmfAtmLayerUniVersion,
       "teraFarEndAtmfAtmLayerDeviceType": teraFarEndAtmfAtmLayerDeviceType,
       "teraFarEndAtmfAtmLayerIlmiVersion": teraFarEndAtmfAtmLayerIlmiVersion,
       "teraFarEndAtmfAtmLayerNniSigVersion": teraFarEndAtmfAtmLayerNniSigVersion,
       "teraFarEndAtmfAtmLayerMaxSvpcVpi": teraFarEndAtmfAtmLayerMaxSvpcVpi,
       "teraFarEndAtmfAtmLayerMaxSvccVpi": teraFarEndAtmfAtmLayerMaxSvccVpi,
       "teraFarEndAtmfAtmLayerMinSvccVci": teraFarEndAtmfAtmLayerMinSvccVci,
       "teraFarEndAtmfVccTable": teraFarEndAtmfVccTable,
       "teraFarEndAtmfVccTableEntry": teraFarEndAtmfVccTableEntry,
       "teraFarEndAtmfVccPortIndex": teraFarEndAtmfVccPortIndex,
       "teraFarEndAtmfVccVpi": teraFarEndAtmfVccVpi,
       "teraFarEndAtmfVccVci": teraFarEndAtmfVccVci,
       "teraFarEndAtmfVccOperStatus": teraFarEndAtmfVccOperStatus,
       "teraFarEndAtmfVccTransmitTrafficDescriptorType": teraFarEndAtmfVccTransmitTrafficDescriptorType,
       "teraFarEndAtmfVccTransmitTrafficDescriptorParam1": teraFarEndAtmfVccTransmitTrafficDescriptorParam1,
       "teraFarEndAtmfVccTransmitTrafficDescriptorParam2": teraFarEndAtmfVccTransmitTrafficDescriptorParam2,
       "teraFarEndAtmfVccTransmitTrafficDescriptorParam3": teraFarEndAtmfVccTransmitTrafficDescriptorParam3,
       "teraFarEndAtmfVccTransmitTrafficDescriptorParam4": teraFarEndAtmfVccTransmitTrafficDescriptorParam4,
       "teraFarEndAtmfVccTransmitTrafficDescriptorParam5": teraFarEndAtmfVccTransmitTrafficDescriptorParam5,
       "teraFarEndAtmfVccReceiveTrafficDescriptorType": teraFarEndAtmfVccReceiveTrafficDescriptorType,
       "teraFarEndAtmfVccReceiveTrafficDescriptorParam1": teraFarEndAtmfVccReceiveTrafficDescriptorParam1,
       "teraFarEndAtmfVccReceiveTrafficDescriptorParam2": teraFarEndAtmfVccReceiveTrafficDescriptorParam2,
       "teraFarEndAtmfVccReceiveTrafficDescriptorParam3": teraFarEndAtmfVccReceiveTrafficDescriptorParam3,
       "teraFarEndAtmfVccReceiveTrafficDescriptorParam4": teraFarEndAtmfVccReceiveTrafficDescriptorParam4,
       "teraFarEndAtmfVccReceiveTrafficDescriptorParam5": teraFarEndAtmfVccReceiveTrafficDescriptorParam5,
       "teraFarEndAtmfVccQoSCategory": teraFarEndAtmfVccQoSCategory,
       "teraFarEndAtmfVccTransmitQoSClass": teraFarEndAtmfVccTransmitQoSClass,
       "teraFarEndAtmfVccReceiveQoSClass": teraFarEndAtmfVccReceiveQoSClass,
       "teraFarEndAtmfVccBestEffortIndicator": teraFarEndAtmfVccBestEffortIndicator,
       "teraFarEndAtmfVccTransmitFrameDiscard": teraFarEndAtmfVccTransmitFrameDiscard,
       "teraFarEndAtmfVccReceiveFrameDiscard": teraFarEndAtmfVccReceiveFrameDiscard,
       "teraFarEndAtmfVccServiceCategory": teraFarEndAtmfVccServiceCategory}
)
