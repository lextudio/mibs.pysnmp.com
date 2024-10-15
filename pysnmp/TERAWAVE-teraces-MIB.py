# SNMP MIB module (TERAWAVE-teraces-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraces-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:22 2024
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
_BandwidthGroup_ObjectIdentity = ObjectIdentity
bandwidthGroup = _BandwidthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 9)
)
_TeraCESConfigTable_Object = MibTable
teraCESConfigTable = _TeraCESConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 1)
)
if mibBuilder.loadTexts:
    teraCESConfigTable.setStatus("mandatory")
_TeraCESConfigTableEntry_Object = MibTableRow
teraCESConfigTableEntry = _TeraCESConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 1, 1)
)
teraCESConfigTableEntry.setIndexNames(
    (0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"),
)
if mibBuilder.loadTexts:
    teraCESConfigTableEntry.setStatus("mandatory")


class _TeraCesSignalling_Type(Integer32):
    """Custom type teraCesSignalling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal1-no-signalling", 2),
          ("aal1-signalling", 1))
    )


_TeraCesSignalling_Type.__name__ = "Integer32"
_TeraCesSignalling_Object = MibTableColumn
teraCesSignalling = _TeraCesSignalling_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 1, 1, 1),
    _TeraCesSignalling_Type()
)
teraCesSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCesSignalling.setStatus("mandatory")


class _TeraCesCheckParity_Type(Integer32):
    """Custom type teraCesCheckParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal1-no-parity", 1),
          ("aal1-parity", 2))
    )


_TeraCesCheckParity_Type.__name__ = "Integer32"
_TeraCesCheckParity_Object = MibTableColumn
teraCesCheckParity = _TeraCesCheckParity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 1, 1, 2),
    _TeraCesCheckParity_Type()
)
teraCesCheckParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCesCheckParity.setStatus("mandatory")


class _TeraCesTestLine_Type(Integer32):
    """Custom type teraCesTestLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("line-test-relay-off", 2),
          ("line-test-relay-on", 3),
          ("no-action", 1))
    )


_TeraCesTestLine_Type.__name__ = "Integer32"
_TeraCesTestLine_Object = MibTableColumn
teraCesTestLine = _TeraCesTestLine_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 1, 1, 3),
    _TeraCesTestLine_Type()
)
teraCesTestLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCesTestLine.setStatus("mandatory")


class _TeraCesSRTSSize_Type(Integer32):
    """Custom type teraCesSRTSSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_TeraCesSRTSSize_Type.__name__ = "Integer32"
_TeraCesSRTSSize_Object = MibTableColumn
teraCesSRTSSize = _TeraCesSRTSSize_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 1, 1, 4),
    _TeraCesSRTSSize_Type()
)
teraCesSRTSSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCesSRTSSize.setStatus("mandatory")
_TeraCESStatTable_Object = MibTable
teraCESStatTable = _TeraCESStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 2)
)
if mibBuilder.loadTexts:
    teraCESStatTable.setStatus("mandatory")
_TeraCESStatTableEntry_Object = MibTableRow
teraCESStatTableEntry = _TeraCESStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 2, 1)
)
teraCESStatTableEntry.setIndexNames(
    (0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"),
)
if mibBuilder.loadTexts:
    teraCESStatTableEntry.setStatus("mandatory")
_TeraCESTCellCount_Type = Counter32
_TeraCESTCellCount_Object = MibTableColumn
teraCESTCellCount = _TeraCESTCellCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 2, 1, 1),
    _TeraCESTCellCount_Type()
)
teraCESTCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESTCellCount.setStatus("mandatory")
_TeraCESRLostCellCount_Type = Counter32
_TeraCESRLostCellCount_Object = MibTableColumn
teraCESRLostCellCount = _TeraCESRLostCellCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 2, 1, 2),
    _TeraCESRLostCellCount_Type()
)
teraCESRLostCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESRLostCellCount.setStatus("mandatory")
_TeraCESRReplacedCellCount_Type = Counter32
_TeraCESRReplacedCellCount_Object = MibTableColumn
teraCESRReplacedCellCount = _TeraCESRReplacedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 2, 1, 3),
    _TeraCESRReplacedCellCount_Type()
)
teraCESRReplacedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESRReplacedCellCount.setStatus("mandatory")
_TeraCESIntervalStatTable_Object = MibTable
teraCESIntervalStatTable = _TeraCESIntervalStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 3)
)
if mibBuilder.loadTexts:
    teraCESIntervalStatTable.setStatus("mandatory")
_TeraCESIntervalStatTableEntry_Object = MibTableRow
teraCESIntervalStatTableEntry = _TeraCESIntervalStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 3, 1)
)
teraCESIntervalStatTableEntry.setIndexNames(
    (0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"),
    (0, "TERAWAVE-teraces-MIB", "teraCESIntervalNumber"),
)
if mibBuilder.loadTexts:
    teraCESIntervalStatTableEntry.setStatus("mandatory")


class _TeraCESIntervalNumber_Type(Integer32):
    """Custom type teraCESIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_TeraCESIntervalNumber_Type.__name__ = "Integer32"
_TeraCESIntervalNumber_Object = MibTableColumn
teraCESIntervalNumber = _TeraCESIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 3, 1, 1),
    _TeraCESIntervalNumber_Type()
)
teraCESIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESIntervalNumber.setStatus("mandatory")
_TeraCESIntervalTCellCount_Type = Counter32
_TeraCESIntervalTCellCount_Object = MibTableColumn
teraCESIntervalTCellCount = _TeraCESIntervalTCellCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 3, 1, 2),
    _TeraCESIntervalTCellCount_Type()
)
teraCESIntervalTCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESIntervalTCellCount.setStatus("mandatory")
_TeraCESIntervalRLostCellCount_Type = Counter32
_TeraCESIntervalRLostCellCount_Object = MibTableColumn
teraCESIntervalRLostCellCount = _TeraCESIntervalRLostCellCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 3, 1, 3),
    _TeraCESIntervalRLostCellCount_Type()
)
teraCESIntervalRLostCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESIntervalRLostCellCount.setStatus("mandatory")
_TeraCESIntervalRReplacedCellCount_Type = Counter32
_TeraCESIntervalRReplacedCellCount_Object = MibTableColumn
teraCESIntervalRReplacedCellCount = _TeraCESIntervalRReplacedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 3, 1, 4),
    _TeraCESIntervalRReplacedCellCount_Type()
)
teraCESIntervalRReplacedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESIntervalRReplacedCellCount.setStatus("mandatory")
_TeraCESTotalStatTable_Object = MibTable
teraCESTotalStatTable = _TeraCESTotalStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 4)
)
if mibBuilder.loadTexts:
    teraCESTotalStatTable.setStatus("mandatory")
_TeraCESTotalStatTableEntry_Object = MibTableRow
teraCESTotalStatTableEntry = _TeraCESTotalStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 4, 1)
)
teraCESTotalStatTableEntry.setIndexNames(
    (0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"),
)
if mibBuilder.loadTexts:
    teraCESTotalStatTableEntry.setStatus("mandatory")
_TeraCESTotalTCellCount_Type = Counter32
_TeraCESTotalTCellCount_Object = MibTableColumn
teraCESTotalTCellCount = _TeraCESTotalTCellCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 4, 1, 1),
    _TeraCESTotalTCellCount_Type()
)
teraCESTotalTCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESTotalTCellCount.setStatus("mandatory")
_TeraCESTotalRLostCellCount_Type = Counter32
_TeraCESTotalRLostCellCount_Object = MibTableColumn
teraCESTotalRLostCellCount = _TeraCESTotalRLostCellCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 4, 1, 2),
    _TeraCESTotalRLostCellCount_Type()
)
teraCESTotalRLostCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESTotalRLostCellCount.setStatus("mandatory")
_TeraCESTotalRReplacedCellCount_Type = Counter32
_TeraCESTotalRReplacedCellCount_Object = MibTableColumn
teraCESTotalRReplacedCellCount = _TeraCESTotalRReplacedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 4, 1, 3),
    _TeraCESTotalRReplacedCellCount_Type()
)
teraCESTotalRReplacedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESTotalRReplacedCellCount.setStatus("mandatory")


class _TeraCESTotalStatStatus_Type(Integer32):
    """Custom type teraCESTotalStatStatus based on Integer32"""
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


_TeraCESTotalStatStatus_Type.__name__ = "Integer32"
_TeraCESTotalStatStatus_Object = MibTableColumn
teraCESTotalStatStatus = _TeraCESTotalStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 4, 1, 4),
    _TeraCESTotalStatStatus_Type()
)
teraCESTotalStatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCESTotalStatStatus.setStatus("mandatory")
_TeraAtmfCESIntervalStatsTable_Object = MibTable
teraAtmfCESIntervalStatsTable = _TeraAtmfCESIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 5)
)
if mibBuilder.loadTexts:
    teraAtmfCESIntervalStatsTable.setStatus("mandatory")
_TeraAtmfCESIntervalStatsTableEntry_Object = MibTableRow
teraAtmfCESIntervalStatsTableEntry = _TeraAtmfCESIntervalStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 5, 1)
)
teraAtmfCESIntervalStatsTableEntry.setIndexNames(
    (0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"),
    (0, "TERAWAVE-teraces-MIB", "teraAtmfCESIntervalNumber"),
)
if mibBuilder.loadTexts:
    teraAtmfCESIntervalStatsTableEntry.setStatus("mandatory")


class _TeraAtmfCESIntervalNumber_Type(Integer32):
    """Custom type teraAtmfCESIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_TeraAtmfCESIntervalNumber_Type.__name__ = "Integer32"
_TeraAtmfCESIntervalNumber_Object = MibTableColumn
teraAtmfCESIntervalNumber = _TeraAtmfCESIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 1),
    _TeraAtmfCESIntervalNumber_Type()
)
teraAtmfCESIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESIntervalNumber.setStatus("mandatory")
_TeraAtmfCESIntervalReassCells_Type = Counter32
_TeraAtmfCESIntervalReassCells_Object = MibTableColumn
teraAtmfCESIntervalReassCells = _TeraAtmfCESIntervalReassCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 2),
    _TeraAtmfCESIntervalReassCells_Type()
)
teraAtmfCESIntervalReassCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESIntervalReassCells.setStatus("mandatory")
_TeraAtmfCESIntervalHdrErrors_Type = Counter32
_TeraAtmfCESIntervalHdrErrors_Object = MibTableColumn
teraAtmfCESIntervalHdrErrors = _TeraAtmfCESIntervalHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 3),
    _TeraAtmfCESIntervalHdrErrors_Type()
)
teraAtmfCESIntervalHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESIntervalHdrErrors.setStatus("mandatory")
_TeraAtmfCESIntervalPointerReframes_Type = Counter32
_TeraAtmfCESIntervalPointerReframes_Object = MibTableColumn
teraAtmfCESIntervalPointerReframes = _TeraAtmfCESIntervalPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 4),
    _TeraAtmfCESIntervalPointerReframes_Type()
)
teraAtmfCESIntervalPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESIntervalPointerReframes.setStatus("mandatory")
_TeraAtmfCESIntervalPointerParityErrors_Type = Counter32
_TeraAtmfCESIntervalPointerParityErrors_Object = MibTableColumn
teraAtmfCESIntervalPointerParityErrors = _TeraAtmfCESIntervalPointerParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 5),
    _TeraAtmfCESIntervalPointerParityErrors_Type()
)
teraAtmfCESIntervalPointerParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESIntervalPointerParityErrors.setStatus("mandatory")
_TeraAtmfCESIntervalAal1SeqErrors_Type = Counter32
_TeraAtmfCESIntervalAal1SeqErrors_Object = MibTableColumn
teraAtmfCESIntervalAal1SeqErrors = _TeraAtmfCESIntervalAal1SeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 6),
    _TeraAtmfCESIntervalAal1SeqErrors_Type()
)
teraAtmfCESIntervalAal1SeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESIntervalAal1SeqErrors.setStatus("mandatory")
_TeraAtmfCESIntervalLostCells_Type = Counter32
_TeraAtmfCESIntervalLostCells_Object = MibTableColumn
teraAtmfCESIntervalLostCells = _TeraAtmfCESIntervalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 7),
    _TeraAtmfCESIntervalLostCells_Type()
)
teraAtmfCESIntervalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESIntervalLostCells.setStatus("mandatory")
_TeraAtmfCESIntervalMisinsertedCells_Type = Counter32
_TeraAtmfCESIntervalMisinsertedCells_Object = MibTableColumn
teraAtmfCESIntervalMisinsertedCells = _TeraAtmfCESIntervalMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 8),
    _TeraAtmfCESIntervalMisinsertedCells_Type()
)
teraAtmfCESIntervalMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESIntervalMisinsertedCells.setStatus("mandatory")
_TeraAtmfCESIntervalBufUnderflows_Type = Counter32
_TeraAtmfCESIntervalBufUnderflows_Object = MibTableColumn
teraAtmfCESIntervalBufUnderflows = _TeraAtmfCESIntervalBufUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 9),
    _TeraAtmfCESIntervalBufUnderflows_Type()
)
teraAtmfCESIntervalBufUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESIntervalBufUnderflows.setStatus("mandatory")
_TeraAtmfCESIntervalBufOverflows_Type = Counter32
_TeraAtmfCESIntervalBufOverflows_Object = MibTableColumn
teraAtmfCESIntervalBufOverflows = _TeraAtmfCESIntervalBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 10),
    _TeraAtmfCESIntervalBufOverflows_Type()
)
teraAtmfCESIntervalBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESIntervalBufOverflows.setStatus("mandatory")


class _TeraAtmfCESIntervalCellLossStatus_Type(Integer32):
    """Custom type teraAtmfCESIntervalCellLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loss", 2),
          ("noloss", 1))
    )


_TeraAtmfCESIntervalCellLossStatus_Type.__name__ = "Integer32"
_TeraAtmfCESIntervalCellLossStatus_Object = MibTableColumn
teraAtmfCESIntervalCellLossStatus = _TeraAtmfCESIntervalCellLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 11),
    _TeraAtmfCESIntervalCellLossStatus_Type()
)
teraAtmfCESIntervalCellLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESIntervalCellLossStatus.setStatus("mandatory")
_TeraAtmfCESTotalStatsTable_Object = MibTable
teraAtmfCESTotalStatsTable = _TeraAtmfCESTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 6)
)
if mibBuilder.loadTexts:
    teraAtmfCESTotalStatsTable.setStatus("mandatory")
_TeraAtmfCESTotalStatsTableEntry_Object = MibTableRow
teraAtmfCESTotalStatsTableEntry = _TeraAtmfCESTotalStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 6, 1)
)
teraAtmfCESTotalStatsTableEntry.setIndexNames(
    (0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"),
)
if mibBuilder.loadTexts:
    teraAtmfCESTotalStatsTableEntry.setStatus("mandatory")
_TeraAtmfCESTotalReassCells_Type = Counter32
_TeraAtmfCESTotalReassCells_Object = MibTableColumn
teraAtmfCESTotalReassCells = _TeraAtmfCESTotalReassCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 1),
    _TeraAtmfCESTotalReassCells_Type()
)
teraAtmfCESTotalReassCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESTotalReassCells.setStatus("mandatory")
_TeraAtmfCESTotalHdrErrors_Type = Counter32
_TeraAtmfCESTotalHdrErrors_Object = MibTableColumn
teraAtmfCESTotalHdrErrors = _TeraAtmfCESTotalHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 2),
    _TeraAtmfCESTotalHdrErrors_Type()
)
teraAtmfCESTotalHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESTotalHdrErrors.setStatus("mandatory")
_TeraAtmfCESTotalPointerReframes_Type = Counter32
_TeraAtmfCESTotalPointerReframes_Object = MibTableColumn
teraAtmfCESTotalPointerReframes = _TeraAtmfCESTotalPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 3),
    _TeraAtmfCESTotalPointerReframes_Type()
)
teraAtmfCESTotalPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESTotalPointerReframes.setStatus("mandatory")
_TeraAtmfCESTotalPointerParityErrors_Type = Counter32
_TeraAtmfCESTotalPointerParityErrors_Object = MibTableColumn
teraAtmfCESTotalPointerParityErrors = _TeraAtmfCESTotalPointerParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 4),
    _TeraAtmfCESTotalPointerParityErrors_Type()
)
teraAtmfCESTotalPointerParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESTotalPointerParityErrors.setStatus("mandatory")
_TeraAtmfCESTotalAal1SeqErrors_Type = Counter32
_TeraAtmfCESTotalAal1SeqErrors_Object = MibTableColumn
teraAtmfCESTotalAal1SeqErrors = _TeraAtmfCESTotalAal1SeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 5),
    _TeraAtmfCESTotalAal1SeqErrors_Type()
)
teraAtmfCESTotalAal1SeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESTotalAal1SeqErrors.setStatus("mandatory")
_TeraAtmfCESTotalLostCells_Type = Counter32
_TeraAtmfCESTotalLostCells_Object = MibTableColumn
teraAtmfCESTotalLostCells = _TeraAtmfCESTotalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 6),
    _TeraAtmfCESTotalLostCells_Type()
)
teraAtmfCESTotalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESTotalLostCells.setStatus("mandatory")
_TeraAtmfCESTotalMisinsertedCells_Type = Counter32
_TeraAtmfCESTotalMisinsertedCells_Object = MibTableColumn
teraAtmfCESTotalMisinsertedCells = _TeraAtmfCESTotalMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 7),
    _TeraAtmfCESTotalMisinsertedCells_Type()
)
teraAtmfCESTotalMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESTotalMisinsertedCells.setStatus("mandatory")
_TeraAtmfCESTotalBufUnderflows_Type = Counter32
_TeraAtmfCESTotalBufUnderflows_Object = MibTableColumn
teraAtmfCESTotalBufUnderflows = _TeraAtmfCESTotalBufUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 8),
    _TeraAtmfCESTotalBufUnderflows_Type()
)
teraAtmfCESTotalBufUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESTotalBufUnderflows.setStatus("mandatory")
_TeraAtmfCESTotalBufOverflows_Type = Counter32
_TeraAtmfCESTotalBufOverflows_Object = MibTableColumn
teraAtmfCESTotalBufOverflows = _TeraAtmfCESTotalBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 9),
    _TeraAtmfCESTotalBufOverflows_Type()
)
teraAtmfCESTotalBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESTotalBufOverflows.setStatus("mandatory")


class _TeraAtmfCESTotalCellLossStatus_Type(Integer32):
    """Custom type teraAtmfCESTotalCellLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loss", 2),
          ("noloss", 1))
    )


_TeraAtmfCESTotalCellLossStatus_Type.__name__ = "Integer32"
_TeraAtmfCESTotalCellLossStatus_Object = MibTableColumn
teraAtmfCESTotalCellLossStatus = _TeraAtmfCESTotalCellLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 10),
    _TeraAtmfCESTotalCellLossStatus_Type()
)
teraAtmfCESTotalCellLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESTotalCellLossStatus.setStatus("mandatory")


class _TeraAtmfCESTotalStatsStatus_Type(Integer32):
    """Custom type teraAtmfCESTotalStatsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("clrall", 3),
          ("ok", 1))
    )


_TeraAtmfCESTotalStatsStatus_Type.__name__ = "Integer32"
_TeraAtmfCESTotalStatsStatus_Object = MibTableColumn
teraAtmfCESTotalStatsStatus = _TeraAtmfCESTotalStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 11),
    _TeraAtmfCESTotalStatsStatus_Type()
)
teraAtmfCESTotalStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAtmfCESTotalStatsStatus.setStatus("mandatory")
_TeraAtmfCESStandard7DayTotalStatsTable_Object = MibTable
teraAtmfCESStandard7DayTotalStatsTable = _TeraAtmfCESStandard7DayTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 7)
)
if mibBuilder.loadTexts:
    teraAtmfCESStandard7DayTotalStatsTable.setStatus("mandatory")
_TeraAtmfCESStandard7DayTotalStatsTableEntry_Object = MibTableRow
teraAtmfCESStandard7DayTotalStatsTableEntry = _TeraAtmfCESStandard7DayTotalStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 7, 1)
)
teraAtmfCESStandard7DayTotalStatsTableEntry.setIndexNames(
    (0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"),
    (0, "TERAWAVE-teraces-MIB", "teraAtmfCESStandard7DayTotalNumber"),
)
if mibBuilder.loadTexts:
    teraAtmfCESStandard7DayTotalStatsTableEntry.setStatus("mandatory")


class _TeraAtmfCESStandard7DayTotalNumber_Type(Integer32):
    """Custom type teraAtmfCESStandard7DayTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraAtmfCESStandard7DayTotalNumber_Type.__name__ = "Integer32"
_TeraAtmfCESStandard7DayTotalNumber_Object = MibTableColumn
teraAtmfCESStandard7DayTotalNumber = _TeraAtmfCESStandard7DayTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 1),
    _TeraAtmfCESStandard7DayTotalNumber_Type()
)
teraAtmfCESStandard7DayTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESStandard7DayTotalNumber.setStatus("mandatory")
_TeraAtmfCESStandard7DayTotalReassCells_Type = Counter32
_TeraAtmfCESStandard7DayTotalReassCells_Object = MibTableColumn
teraAtmfCESStandard7DayTotalReassCells = _TeraAtmfCESStandard7DayTotalReassCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 2),
    _TeraAtmfCESStandard7DayTotalReassCells_Type()
)
teraAtmfCESStandard7DayTotalReassCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESStandard7DayTotalReassCells.setStatus("mandatory")
_TeraAtmfCESStandard7DayTotalHdrErrors_Type = Counter32
_TeraAtmfCESStandard7DayTotalHdrErrors_Object = MibTableColumn
teraAtmfCESStandard7DayTotalHdrErrors = _TeraAtmfCESStandard7DayTotalHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 3),
    _TeraAtmfCESStandard7DayTotalHdrErrors_Type()
)
teraAtmfCESStandard7DayTotalHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESStandard7DayTotalHdrErrors.setStatus("mandatory")
_TeraAtmfCESStandard7DayTotalPointerReframes_Type = Counter32
_TeraAtmfCESStandard7DayTotalPointerReframes_Object = MibTableColumn
teraAtmfCESStandard7DayTotalPointerReframes = _TeraAtmfCESStandard7DayTotalPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 4),
    _TeraAtmfCESStandard7DayTotalPointerReframes_Type()
)
teraAtmfCESStandard7DayTotalPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESStandard7DayTotalPointerReframes.setStatus("mandatory")
_TeraAtmfCESStandard7DayTotalPointerParityErrors_Type = Counter32
_TeraAtmfCESStandard7DayTotalPointerParityErrors_Object = MibTableColumn
teraAtmfCESStandard7DayTotalPointerParityErrors = _TeraAtmfCESStandard7DayTotalPointerParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 5),
    _TeraAtmfCESStandard7DayTotalPointerParityErrors_Type()
)
teraAtmfCESStandard7DayTotalPointerParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESStandard7DayTotalPointerParityErrors.setStatus("mandatory")
_TeraAtmfCESStandard7DayTotalAal1SeqErrors_Type = Counter32
_TeraAtmfCESStandard7DayTotalAal1SeqErrors_Object = MibTableColumn
teraAtmfCESStandard7DayTotalAal1SeqErrors = _TeraAtmfCESStandard7DayTotalAal1SeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 6),
    _TeraAtmfCESStandard7DayTotalAal1SeqErrors_Type()
)
teraAtmfCESStandard7DayTotalAal1SeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESStandard7DayTotalAal1SeqErrors.setStatus("mandatory")
_TeraAtmfCESStandard7DayTotalLostCells_Type = Counter32
_TeraAtmfCESStandard7DayTotalLostCells_Object = MibTableColumn
teraAtmfCESStandard7DayTotalLostCells = _TeraAtmfCESStandard7DayTotalLostCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 7),
    _TeraAtmfCESStandard7DayTotalLostCells_Type()
)
teraAtmfCESStandard7DayTotalLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESStandard7DayTotalLostCells.setStatus("mandatory")
_TeraAtmfCESStandard7DayTotalMisinsertedCells_Type = Counter32
_TeraAtmfCESStandard7DayTotalMisinsertedCells_Object = MibTableColumn
teraAtmfCESStandard7DayTotalMisinsertedCells = _TeraAtmfCESStandard7DayTotalMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 8),
    _TeraAtmfCESStandard7DayTotalMisinsertedCells_Type()
)
teraAtmfCESStandard7DayTotalMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESStandard7DayTotalMisinsertedCells.setStatus("mandatory")
_TeraAtmfCESStandard7DayTotalBufUnderflows_Type = Counter32
_TeraAtmfCESStandard7DayTotalBufUnderflows_Object = MibTableColumn
teraAtmfCESStandard7DayTotalBufUnderflows = _TeraAtmfCESStandard7DayTotalBufUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 9),
    _TeraAtmfCESStandard7DayTotalBufUnderflows_Type()
)
teraAtmfCESStandard7DayTotalBufUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESStandard7DayTotalBufUnderflows.setStatus("mandatory")
_TeraAtmfCESStandard7DayTotalBufOverflows_Type = Counter32
_TeraAtmfCESStandard7DayTotalBufOverflows_Object = MibTableColumn
teraAtmfCESStandard7DayTotalBufOverflows = _TeraAtmfCESStandard7DayTotalBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 10),
    _TeraAtmfCESStandard7DayTotalBufOverflows_Type()
)
teraAtmfCESStandard7DayTotalBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESStandard7DayTotalBufOverflows.setStatus("mandatory")


class _TeraAtmfCESStandard7DayTotalCellLossStatus_Type(Integer32):
    """Custom type teraAtmfCESStandard7DayTotalCellLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loss", 2),
          ("noloss", 1))
    )


_TeraAtmfCESStandard7DayTotalCellLossStatus_Type.__name__ = "Integer32"
_TeraAtmfCESStandard7DayTotalCellLossStatus_Object = MibTableColumn
teraAtmfCESStandard7DayTotalCellLossStatus = _TeraAtmfCESStandard7DayTotalCellLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 11),
    _TeraAtmfCESStandard7DayTotalCellLossStatus_Type()
)
teraAtmfCESStandard7DayTotalCellLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESStandard7DayTotalCellLossStatus.setStatus("mandatory")


class _TeraAtmfCESStandard7DayDayTotalValidData_Type(Integer32):
    """Custom type teraAtmfCESStandard7DayDayTotalValidData based on Integer32"""
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


_TeraAtmfCESStandard7DayDayTotalValidData_Type.__name__ = "Integer32"
_TeraAtmfCESStandard7DayDayTotalValidData_Object = MibTableColumn
teraAtmfCESStandard7DayDayTotalValidData = _TeraAtmfCESStandard7DayDayTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 12),
    _TeraAtmfCESStandard7DayDayTotalValidData_Type()
)
teraAtmfCESStandard7DayDayTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAtmfCESStandard7DayDayTotalValidData.setStatus("mandatory")
_TeraCESTera7DayTotalStatTable_Object = MibTable
teraCESTera7DayTotalStatTable = _TeraCESTera7DayTotalStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 8)
)
if mibBuilder.loadTexts:
    teraCESTera7DayTotalStatTable.setStatus("mandatory")
_TeraCESTera7DayTotalStatTableEntry_Object = MibTableRow
teraCESTera7DayTotalStatTableEntry = _TeraCESTera7DayTotalStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 8, 1)
)
teraCESTera7DayTotalStatTableEntry.setIndexNames(
    (0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"),
    (0, "TERAWAVE-teraces-MIB", "teraCESTera7DayTotalNumber"),
)
if mibBuilder.loadTexts:
    teraCESTera7DayTotalStatTableEntry.setStatus("mandatory")


class _TeraCESTera7DayTotalNumber_Type(Integer32):
    """Custom type teraCESTera7DayTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraCESTera7DayTotalNumber_Type.__name__ = "Integer32"
_TeraCESTera7DayTotalNumber_Object = MibTableColumn
teraCESTera7DayTotalNumber = _TeraCESTera7DayTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 8, 1, 1),
    _TeraCESTera7DayTotalNumber_Type()
)
teraCESTera7DayTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESTera7DayTotalNumber.setStatus("mandatory")
_TeraCESTera7DayTotalTCellCount_Type = Counter32
_TeraCESTera7DayTotalTCellCount_Object = MibTableColumn
teraCESTera7DayTotalTCellCount = _TeraCESTera7DayTotalTCellCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 8, 1, 2),
    _TeraCESTera7DayTotalTCellCount_Type()
)
teraCESTera7DayTotalTCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESTera7DayTotalTCellCount.setStatus("mandatory")
_TeraCESTera7DayTotalRLostCellCount_Type = Counter32
_TeraCESTera7DayTotalRLostCellCount_Object = MibTableColumn
teraCESTera7DayTotalRLostCellCount = _TeraCESTera7DayTotalRLostCellCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 8, 1, 3),
    _TeraCESTera7DayTotalRLostCellCount_Type()
)
teraCESTera7DayTotalRLostCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESTera7DayTotalRLostCellCount.setStatus("mandatory")
_TeraCESTera7DayTotalRReplacedCellCount_Type = Counter32
_TeraCESTera7DayTotalRReplacedCellCount_Object = MibTableColumn
teraCESTera7DayTotalRReplacedCellCount = _TeraCESTera7DayTotalRReplacedCellCount_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 8, 1, 4),
    _TeraCESTera7DayTotalRReplacedCellCount_Type()
)
teraCESTera7DayTotalRReplacedCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESTera7DayTotalRReplacedCellCount.setStatus("mandatory")


class _TeraCESTera7DayDayTotalValidData_Type(Integer32):
    """Custom type teraCESTera7DayDayTotalValidData based on Integer32"""
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


_TeraCESTera7DayDayTotalValidData_Type.__name__ = "Integer32"
_TeraCESTera7DayDayTotalValidData_Object = MibTableColumn
teraCESTera7DayDayTotalValidData = _TeraCESTera7DayDayTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 9, 8, 1, 5),
    _TeraCESTera7DayDayTotalValidData_Type()
)
teraCESTera7DayDayTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraCESTera7DayDayTotalValidData.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraces-MIB",
    **{"terawave": terawave,
       "bandwidthGroup": bandwidthGroup,
       "teraCESConfigTable": teraCESConfigTable,
       "teraCESConfigTableEntry": teraCESConfigTableEntry,
       "teraCesSignalling": teraCesSignalling,
       "teraCesCheckParity": teraCesCheckParity,
       "teraCesTestLine": teraCesTestLine,
       "teraCesSRTSSize": teraCesSRTSSize,
       "teraCESStatTable": teraCESStatTable,
       "teraCESStatTableEntry": teraCESStatTableEntry,
       "teraCESTCellCount": teraCESTCellCount,
       "teraCESRLostCellCount": teraCESRLostCellCount,
       "teraCESRReplacedCellCount": teraCESRReplacedCellCount,
       "teraCESIntervalStatTable": teraCESIntervalStatTable,
       "teraCESIntervalStatTableEntry": teraCESIntervalStatTableEntry,
       "teraCESIntervalNumber": teraCESIntervalNumber,
       "teraCESIntervalTCellCount": teraCESIntervalTCellCount,
       "teraCESIntervalRLostCellCount": teraCESIntervalRLostCellCount,
       "teraCESIntervalRReplacedCellCount": teraCESIntervalRReplacedCellCount,
       "teraCESTotalStatTable": teraCESTotalStatTable,
       "teraCESTotalStatTableEntry": teraCESTotalStatTableEntry,
       "teraCESTotalTCellCount": teraCESTotalTCellCount,
       "teraCESTotalRLostCellCount": teraCESTotalRLostCellCount,
       "teraCESTotalRReplacedCellCount": teraCESTotalRReplacedCellCount,
       "teraCESTotalStatStatus": teraCESTotalStatStatus,
       "teraAtmfCESIntervalStatsTable": teraAtmfCESIntervalStatsTable,
       "teraAtmfCESIntervalStatsTableEntry": teraAtmfCESIntervalStatsTableEntry,
       "teraAtmfCESIntervalNumber": teraAtmfCESIntervalNumber,
       "teraAtmfCESIntervalReassCells": teraAtmfCESIntervalReassCells,
       "teraAtmfCESIntervalHdrErrors": teraAtmfCESIntervalHdrErrors,
       "teraAtmfCESIntervalPointerReframes": teraAtmfCESIntervalPointerReframes,
       "teraAtmfCESIntervalPointerParityErrors": teraAtmfCESIntervalPointerParityErrors,
       "teraAtmfCESIntervalAal1SeqErrors": teraAtmfCESIntervalAal1SeqErrors,
       "teraAtmfCESIntervalLostCells": teraAtmfCESIntervalLostCells,
       "teraAtmfCESIntervalMisinsertedCells": teraAtmfCESIntervalMisinsertedCells,
       "teraAtmfCESIntervalBufUnderflows": teraAtmfCESIntervalBufUnderflows,
       "teraAtmfCESIntervalBufOverflows": teraAtmfCESIntervalBufOverflows,
       "teraAtmfCESIntervalCellLossStatus": teraAtmfCESIntervalCellLossStatus,
       "teraAtmfCESTotalStatsTable": teraAtmfCESTotalStatsTable,
       "teraAtmfCESTotalStatsTableEntry": teraAtmfCESTotalStatsTableEntry,
       "teraAtmfCESTotalReassCells": teraAtmfCESTotalReassCells,
       "teraAtmfCESTotalHdrErrors": teraAtmfCESTotalHdrErrors,
       "teraAtmfCESTotalPointerReframes": teraAtmfCESTotalPointerReframes,
       "teraAtmfCESTotalPointerParityErrors": teraAtmfCESTotalPointerParityErrors,
       "teraAtmfCESTotalAal1SeqErrors": teraAtmfCESTotalAal1SeqErrors,
       "teraAtmfCESTotalLostCells": teraAtmfCESTotalLostCells,
       "teraAtmfCESTotalMisinsertedCells": teraAtmfCESTotalMisinsertedCells,
       "teraAtmfCESTotalBufUnderflows": teraAtmfCESTotalBufUnderflows,
       "teraAtmfCESTotalBufOverflows": teraAtmfCESTotalBufOverflows,
       "teraAtmfCESTotalCellLossStatus": teraAtmfCESTotalCellLossStatus,
       "teraAtmfCESTotalStatsStatus": teraAtmfCESTotalStatsStatus,
       "teraAtmfCESStandard7DayTotalStatsTable": teraAtmfCESStandard7DayTotalStatsTable,
       "teraAtmfCESStandard7DayTotalStatsTableEntry": teraAtmfCESStandard7DayTotalStatsTableEntry,
       "teraAtmfCESStandard7DayTotalNumber": teraAtmfCESStandard7DayTotalNumber,
       "teraAtmfCESStandard7DayTotalReassCells": teraAtmfCESStandard7DayTotalReassCells,
       "teraAtmfCESStandard7DayTotalHdrErrors": teraAtmfCESStandard7DayTotalHdrErrors,
       "teraAtmfCESStandard7DayTotalPointerReframes": teraAtmfCESStandard7DayTotalPointerReframes,
       "teraAtmfCESStandard7DayTotalPointerParityErrors": teraAtmfCESStandard7DayTotalPointerParityErrors,
       "teraAtmfCESStandard7DayTotalAal1SeqErrors": teraAtmfCESStandard7DayTotalAal1SeqErrors,
       "teraAtmfCESStandard7DayTotalLostCells": teraAtmfCESStandard7DayTotalLostCells,
       "teraAtmfCESStandard7DayTotalMisinsertedCells": teraAtmfCESStandard7DayTotalMisinsertedCells,
       "teraAtmfCESStandard7DayTotalBufUnderflows": teraAtmfCESStandard7DayTotalBufUnderflows,
       "teraAtmfCESStandard7DayTotalBufOverflows": teraAtmfCESStandard7DayTotalBufOverflows,
       "teraAtmfCESStandard7DayTotalCellLossStatus": teraAtmfCESStandard7DayTotalCellLossStatus,
       "teraAtmfCESStandard7DayDayTotalValidData": teraAtmfCESStandard7DayDayTotalValidData,
       "teraCESTera7DayTotalStatTable": teraCESTera7DayTotalStatTable,
       "teraCESTera7DayTotalStatTableEntry": teraCESTera7DayTotalStatTableEntry,
       "teraCESTera7DayTotalNumber": teraCESTera7DayTotalNumber,
       "teraCESTera7DayTotalTCellCount": teraCESTera7DayTotalTCellCount,
       "teraCESTera7DayTotalRLostCellCount": teraCESTera7DayTotalRLostCellCount,
       "teraCESTera7DayTotalRReplacedCellCount": teraCESTera7DayTotalRReplacedCellCount,
       "teraCESTera7DayDayTotalValidData": teraCESTera7DayDayTotalValidData}
)
