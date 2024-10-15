# SNMP MIB module (ChrComPmAtmATM-CELL-Interval-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ChrComPmAtmATM-CELL-Interval-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:00 2024
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

(chrComIfifIndex,) = mibBuilder.importSymbols(
    "ChrComIfifTable-MIB",
    "chrComIfifIndex")

(TruthValue,) = mibBuilder.importSymbols(
    "ChrTyp-MIB",
    "TruthValue")

(chrComPmAtm,) = mibBuilder.importSymbols(
    "Chromatis-MIB",
    "chrComPmAtm")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChrComPmAtmATM_CELL_IntervalTable_Object = MibTable
chrComPmAtmATM_CELL_IntervalTable = _ChrComPmAtmATM_CELL_IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2)
)
if mibBuilder.loadTexts:
    chrComPmAtmATM_CELL_IntervalTable.setStatus("current")
_ChrComPmAtmATM_CELL_IntervalEntry_Object = MibTableRow
chrComPmAtmATM_CELL_IntervalEntry = _ChrComPmAtmATM_CELL_IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1)
)
chrComPmAtmATM_CELL_IntervalEntry.setIndexNames(
    (0, "ChrComIfifTable-MIB", "chrComIfifIndex"),
    (0, "ChrComPmAtmATM-CELL-Interval-MIB", "chrComPmAtmIntervalNumber"),
)
if mibBuilder.loadTexts:
    chrComPmAtmATM_CELL_IntervalEntry.setStatus("current")


class _ChrComPmAtmIntervalNumber_Type(Unsigned32):
    """Custom type chrComPmAtmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ChrComPmAtmIntervalNumber_Type.__name__ = "Unsigned32"
_ChrComPmAtmIntervalNumber_Object = MibTableColumn
chrComPmAtmIntervalNumber = _ChrComPmAtmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 1),
    _ChrComPmAtmIntervalNumber_Type()
)
chrComPmAtmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmIntervalNumber.setStatus("current")
_ChrComPmAtmSuspectedInterval_Type = TruthValue
_ChrComPmAtmSuspectedInterval_Object = MibTableColumn
chrComPmAtmSuspectedInterval = _ChrComPmAtmSuspectedInterval_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 2),
    _ChrComPmAtmSuspectedInterval_Type()
)
chrComPmAtmSuspectedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmSuspectedInterval.setStatus("current")


class _ChrComPmAtmElapsedTime_Type(Unsigned32):
    """Custom type chrComPmAtmElapsedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmElapsedTime_Type.__name__ = "Unsigned32"
_ChrComPmAtmElapsedTime_Object = MibTableColumn
chrComPmAtmElapsedTime = _ChrComPmAtmElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 3),
    _ChrComPmAtmElapsedTime_Type()
)
chrComPmAtmElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmElapsedTime.setStatus("current")


class _ChrComPmAtmSuppressedIntrvls_Type(Gauge32):
    """Custom type chrComPmAtmSuppressedIntrvls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmSuppressedIntrvls_Type.__name__ = "Gauge32"
_ChrComPmAtmSuppressedIntrvls_Object = MibTableColumn
chrComPmAtmSuppressedIntrvls = _ChrComPmAtmSuppressedIntrvls_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 4),
    _ChrComPmAtmSuppressedIntrvls_Type()
)
chrComPmAtmSuppressedIntrvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmSuppressedIntrvls.setStatus("current")


class _ChrComPmAtmOCDS_Type(Gauge32):
    """Custom type chrComPmAtmOCDS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmOCDS_Type.__name__ = "Gauge32"
_ChrComPmAtmOCDS_Object = MibTableColumn
chrComPmAtmOCDS = _ChrComPmAtmOCDS_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 5),
    _ChrComPmAtmOCDS_Type()
)
chrComPmAtmOCDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmOCDS.setStatus("current")


class _ChrComPmAtmHECCells_Type(Gauge32):
    """Custom type chrComPmAtmHECCells based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmHECCells_Type.__name__ = "Gauge32"
_ChrComPmAtmHECCells_Object = MibTableColumn
chrComPmAtmHECCells = _ChrComPmAtmHECCells_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 6),
    _ChrComPmAtmHECCells_Type()
)
chrComPmAtmHECCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmHECCells.setStatus("current")


class _ChrComPmAtmCorrectableHECCells_Type(Gauge32):
    """Custom type chrComPmAtmCorrectableHECCells based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmCorrectableHECCells_Type.__name__ = "Gauge32"
_ChrComPmAtmCorrectableHECCells_Object = MibTableColumn
chrComPmAtmCorrectableHECCells = _ChrComPmAtmCorrectableHECCells_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 7),
    _ChrComPmAtmCorrectableHECCells_Type()
)
chrComPmAtmCorrectableHECCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmCorrectableHECCells.setStatus("current")


class _ChrComPmAtmDiscardedCells_Type(Gauge32):
    """Custom type chrComPmAtmDiscardedCells based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmDiscardedCells_Type.__name__ = "Gauge32"
_ChrComPmAtmDiscardedCells_Object = MibTableColumn
chrComPmAtmDiscardedCells = _ChrComPmAtmDiscardedCells_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 8),
    _ChrComPmAtmDiscardedCells_Type()
)
chrComPmAtmDiscardedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmDiscardedCells.setStatus("current")


class _ChrComPmAtmReceivedCells_Type(Gauge32):
    """Custom type chrComPmAtmReceivedCells based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmReceivedCells_Type.__name__ = "Gauge32"
_ChrComPmAtmReceivedCells_Object = MibTableColumn
chrComPmAtmReceivedCells = _ChrComPmAtmReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 9),
    _ChrComPmAtmReceivedCells_Type()
)
chrComPmAtmReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmReceivedCells.setStatus("current")


class _ChrComPmAtmTransmittedCells_Type(Gauge32):
    """Custom type chrComPmAtmTransmittedCells based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmTransmittedCells_Type.__name__ = "Gauge32"
_ChrComPmAtmTransmittedCells_Object = MibTableColumn
chrComPmAtmTransmittedCells = _ChrComPmAtmTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 10),
    _ChrComPmAtmTransmittedCells_Type()
)
chrComPmAtmTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmTransmittedCells.setStatus("current")


class _ChrComPmAtmDiscardedIngCells_Type(Gauge32):
    """Custom type chrComPmAtmDiscardedIngCells based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmDiscardedIngCells_Type.__name__ = "Gauge32"
_ChrComPmAtmDiscardedIngCells_Object = MibTableColumn
chrComPmAtmDiscardedIngCells = _ChrComPmAtmDiscardedIngCells_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 11),
    _ChrComPmAtmDiscardedIngCells_Type()
)
chrComPmAtmDiscardedIngCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmDiscardedIngCells.setStatus("current")


class _ChrComPmAtmDiscardedIngHighPrCells_Type(Gauge32):
    """Custom type chrComPmAtmDiscardedIngHighPrCells based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmDiscardedIngHighPrCells_Type.__name__ = "Gauge32"
_ChrComPmAtmDiscardedIngHighPrCells_Object = MibTableColumn
chrComPmAtmDiscardedIngHighPrCells = _ChrComPmAtmDiscardedIngHighPrCells_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 12),
    _ChrComPmAtmDiscardedIngHighPrCells_Type()
)
chrComPmAtmDiscardedIngHighPrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmDiscardedIngHighPrCells.setStatus("current")


class _ChrComPmAtmDiscardedEgCells_Type(Gauge32):
    """Custom type chrComPmAtmDiscardedEgCells based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmDiscardedEgCells_Type.__name__ = "Gauge32"
_ChrComPmAtmDiscardedEgCells_Object = MibTableColumn
chrComPmAtmDiscardedEgCells = _ChrComPmAtmDiscardedEgCells_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 13),
    _ChrComPmAtmDiscardedEgCells_Type()
)
chrComPmAtmDiscardedEgCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmDiscardedEgCells.setStatus("current")


class _ChrComPmAtmDiscardedEgHighPrCells_Type(Gauge32):
    """Custom type chrComPmAtmDiscardedEgHighPrCells based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmDiscardedEgHighPrCells_Type.__name__ = "Gauge32"
_ChrComPmAtmDiscardedEgHighPrCells_Object = MibTableColumn
chrComPmAtmDiscardedEgHighPrCells = _ChrComPmAtmDiscardedEgHighPrCells_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 14),
    _ChrComPmAtmDiscardedEgHighPrCells_Type()
)
chrComPmAtmDiscardedEgHighPrCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmDiscardedEgHighPrCells.setStatus("current")


class _ChrComPmAtmDiscardedUPC_Type(Gauge32):
    """Custom type chrComPmAtmDiscardedUPC based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmDiscardedUPC_Type.__name__ = "Gauge32"
_ChrComPmAtmDiscardedUPC_Object = MibTableColumn
chrComPmAtmDiscardedUPC = _ChrComPmAtmDiscardedUPC_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 15),
    _ChrComPmAtmDiscardedUPC_Type()
)
chrComPmAtmDiscardedUPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmDiscardedUPC.setStatus("current")


class _ChrComPmAtmTaggedUPC_Type(Gauge32):
    """Custom type chrComPmAtmTaggedUPC based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmTaggedUPC_Type.__name__ = "Gauge32"
_ChrComPmAtmTaggedUPC_Object = MibTableColumn
chrComPmAtmTaggedUPC = _ChrComPmAtmTaggedUPC_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 16),
    _ChrComPmAtmTaggedUPC_Type()
)
chrComPmAtmTaggedUPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmTaggedUPC.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ChrComPmAtmATM-CELL-Interval-MIB",
    **{"chrComPmAtmATM-CELL-IntervalTable": chrComPmAtmATM_CELL_IntervalTable,
       "chrComPmAtmATM-CELL-IntervalEntry": chrComPmAtmATM_CELL_IntervalEntry,
       "chrComPmAtmIntervalNumber": chrComPmAtmIntervalNumber,
       "chrComPmAtmSuspectedInterval": chrComPmAtmSuspectedInterval,
       "chrComPmAtmElapsedTime": chrComPmAtmElapsedTime,
       "chrComPmAtmSuppressedIntrvls": chrComPmAtmSuppressedIntrvls,
       "chrComPmAtmOCDS": chrComPmAtmOCDS,
       "chrComPmAtmHECCells": chrComPmAtmHECCells,
       "chrComPmAtmCorrectableHECCells": chrComPmAtmCorrectableHECCells,
       "chrComPmAtmDiscardedCells": chrComPmAtmDiscardedCells,
       "chrComPmAtmReceivedCells": chrComPmAtmReceivedCells,
       "chrComPmAtmTransmittedCells": chrComPmAtmTransmittedCells,
       "chrComPmAtmDiscardedIngCells": chrComPmAtmDiscardedIngCells,
       "chrComPmAtmDiscardedIngHighPrCells": chrComPmAtmDiscardedIngHighPrCells,
       "chrComPmAtmDiscardedEgCells": chrComPmAtmDiscardedEgCells,
       "chrComPmAtmDiscardedEgHighPrCells": chrComPmAtmDiscardedEgHighPrCells,
       "chrComPmAtmDiscardedUPC": chrComPmAtmDiscardedUPC,
       "chrComPmAtmTaggedUPC": chrComPmAtmTaggedUPC}
)
