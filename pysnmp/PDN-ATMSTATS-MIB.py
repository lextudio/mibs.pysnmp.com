# SNMP MIB module (PDN-ATMSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-ATMSTATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:19 2024
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

(atmVclVci,
 atmVclVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdnAtm,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdnAtm")

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
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

pdnAtmStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3)
)
pdnAtmStatsMIB.setRevisions(
        ("1902-03-28 00:00",
         "1900-04-13 00:00",
         "1999-05-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnAtmVplStat_ObjectIdentity = ObjectIdentity
pdnAtmVplStat = _PdnAtmVplStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 1)
)
_PdnAtmVplStatTable_Object = MibTable
pdnAtmVplStatTable = _PdnAtmVplStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnAtmVplStatTable.setStatus("current")
_PdnAtmVplStatEntry_Object = MibTableRow
pdnAtmVplStatEntry = _PdnAtmVplStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 1, 1, 1)
)
pdnAtmVplStatEntry.setIndexNames(
    (0, "PDN-ATMSTATS-MIB", "pdnAtmVplStatIfIndex"),
    (0, "PDN-ATMSTATS-MIB", "pdnAtmVplStatVpi"),
)
if mibBuilder.loadTexts:
    pdnAtmVplStatEntry.setStatus("current")
_PdnAtmVplStatIfIndex_Type = Integer32
_PdnAtmVplStatIfIndex_Object = MibTableColumn
pdnAtmVplStatIfIndex = _PdnAtmVplStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 1, 1, 1, 1),
    _PdnAtmVplStatIfIndex_Type()
)
pdnAtmVplStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVplStatIfIndex.setStatus("current")
_PdnAtmVplStatVpi_Type = Integer32
_PdnAtmVplStatVpi_Object = MibTableColumn
pdnAtmVplStatVpi = _PdnAtmVplStatVpi_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 1, 1, 1, 2),
    _PdnAtmVplStatVpi_Type()
)
pdnAtmVplStatVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVplStatVpi.setStatus("current")
_PdnAtmVplStatTotalCellIns_Type = Counter32
_PdnAtmVplStatTotalCellIns_Object = MibTableColumn
pdnAtmVplStatTotalCellIns = _PdnAtmVplStatTotalCellIns_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 1, 1, 1, 3),
    _PdnAtmVplStatTotalCellIns_Type()
)
pdnAtmVplStatTotalCellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVplStatTotalCellIns.setStatus("current")
_PdnAtmVplStatClp0CellIns_Type = Counter32
_PdnAtmVplStatClp0CellIns_Object = MibTableColumn
pdnAtmVplStatClp0CellIns = _PdnAtmVplStatClp0CellIns_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 1, 1, 1, 4),
    _PdnAtmVplStatClp0CellIns_Type()
)
pdnAtmVplStatClp0CellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVplStatClp0CellIns.setStatus("current")
_PdnAtmVplStatTotalDiscards_Type = Counter32
_PdnAtmVplStatTotalDiscards_Object = MibTableColumn
pdnAtmVplStatTotalDiscards = _PdnAtmVplStatTotalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 1, 1, 1, 5),
    _PdnAtmVplStatTotalDiscards_Type()
)
pdnAtmVplStatTotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVplStatTotalDiscards.setStatus("current")
_PdnAtmVplStatClp0Discards_Type = Counter32
_PdnAtmVplStatClp0Discards_Object = MibTableColumn
pdnAtmVplStatClp0Discards = _PdnAtmVplStatClp0Discards_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 1, 1, 1, 6),
    _PdnAtmVplStatClp0Discards_Type()
)
pdnAtmVplStatClp0Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVplStatClp0Discards.setStatus("current")
_PdnAtmVplStatTotalCellOuts_Type = Counter32
_PdnAtmVplStatTotalCellOuts_Object = MibTableColumn
pdnAtmVplStatTotalCellOuts = _PdnAtmVplStatTotalCellOuts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 1, 1, 1, 7),
    _PdnAtmVplStatTotalCellOuts_Type()
)
pdnAtmVplStatTotalCellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVplStatTotalCellOuts.setStatus("current")
_PdnAtmVplStatClp0CellOuts_Type = Counter32
_PdnAtmVplStatClp0CellOuts_Object = MibTableColumn
pdnAtmVplStatClp0CellOuts = _PdnAtmVplStatClp0CellOuts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 1, 1, 1, 8),
    _PdnAtmVplStatClp0CellOuts_Type()
)
pdnAtmVplStatClp0CellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVplStatClp0CellOuts.setStatus("current")
_PdnAtmVplStatTaggedOuts_Type = Counter32
_PdnAtmVplStatTaggedOuts_Object = MibTableColumn
pdnAtmVplStatTaggedOuts = _PdnAtmVplStatTaggedOuts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 1, 1, 1, 9),
    _PdnAtmVplStatTaggedOuts_Type()
)
pdnAtmVplStatTaggedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVplStatTaggedOuts.setStatus("current")
_PdnAtmVclStat_ObjectIdentity = ObjectIdentity
pdnAtmVclStat = _PdnAtmVclStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2)
)
_PdnAtmVclStatTable_Object = MibTable
pdnAtmVclStatTable = _PdnAtmVclStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 2)
)
if mibBuilder.loadTexts:
    pdnAtmVclStatTable.setStatus("current")
_PdnAtmVclStatEntry_Object = MibTableRow
pdnAtmVclStatEntry = _PdnAtmVclStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 2, 1)
)
pdnAtmVclStatEntry.setIndexNames(
    (0, "PDN-ATMSTATS-MIB", "pdnAtmVclStatIfIndex"),
    (0, "PDN-ATMSTATS-MIB", "pdnAtmVclStatVpi"),
    (0, "PDN-ATMSTATS-MIB", "pdnAtmVclStatVci"),
)
if mibBuilder.loadTexts:
    pdnAtmVclStatEntry.setStatus("current")
_PdnAtmVclStatIfIndex_Type = Integer32
_PdnAtmVclStatIfIndex_Object = MibTableColumn
pdnAtmVclStatIfIndex = _PdnAtmVclStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 2, 1, 1),
    _PdnAtmVclStatIfIndex_Type()
)
pdnAtmVclStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclStatIfIndex.setStatus("current")
_PdnAtmVclStatVpi_Type = Integer32
_PdnAtmVclStatVpi_Object = MibTableColumn
pdnAtmVclStatVpi = _PdnAtmVclStatVpi_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 2, 1, 2),
    _PdnAtmVclStatVpi_Type()
)
pdnAtmVclStatVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclStatVpi.setStatus("current")
_PdnAtmVclStatVci_Type = Integer32
_PdnAtmVclStatVci_Object = MibTableColumn
pdnAtmVclStatVci = _PdnAtmVclStatVci_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 2, 1, 3),
    _PdnAtmVclStatVci_Type()
)
pdnAtmVclStatVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclStatVci.setStatus("current")
_PdnAtmVclStatTotalCellIns_Type = Counter32
_PdnAtmVclStatTotalCellIns_Object = MibTableColumn
pdnAtmVclStatTotalCellIns = _PdnAtmVclStatTotalCellIns_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 2, 1, 4),
    _PdnAtmVclStatTotalCellIns_Type()
)
pdnAtmVclStatTotalCellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclStatTotalCellIns.setStatus("current")
_PdnAtmVclStatClp0CellIns_Type = Counter32
_PdnAtmVclStatClp0CellIns_Object = MibTableColumn
pdnAtmVclStatClp0CellIns = _PdnAtmVclStatClp0CellIns_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 2, 1, 5),
    _PdnAtmVclStatClp0CellIns_Type()
)
pdnAtmVclStatClp0CellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclStatClp0CellIns.setStatus("current")
_PdnAtmVclStatTotalDiscards_Type = Counter32
_PdnAtmVclStatTotalDiscards_Object = MibTableColumn
pdnAtmVclStatTotalDiscards = _PdnAtmVclStatTotalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 2, 1, 6),
    _PdnAtmVclStatTotalDiscards_Type()
)
pdnAtmVclStatTotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclStatTotalDiscards.setStatus("current")
_PdnAtmVclStatClp0Discards_Type = Counter32
_PdnAtmVclStatClp0Discards_Object = MibTableColumn
pdnAtmVclStatClp0Discards = _PdnAtmVclStatClp0Discards_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 2, 1, 7),
    _PdnAtmVclStatClp0Discards_Type()
)
pdnAtmVclStatClp0Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclStatClp0Discards.setStatus("current")
_PdnAtmVclStatTotalCellOuts_Type = Counter32
_PdnAtmVclStatTotalCellOuts_Object = MibTableColumn
pdnAtmVclStatTotalCellOuts = _PdnAtmVclStatTotalCellOuts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 2, 1, 8),
    _PdnAtmVclStatTotalCellOuts_Type()
)
pdnAtmVclStatTotalCellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclStatTotalCellOuts.setStatus("current")
_PdnAtmVclStatClp0CellOuts_Type = Counter32
_PdnAtmVclStatClp0CellOuts_Object = MibTableColumn
pdnAtmVclStatClp0CellOuts = _PdnAtmVclStatClp0CellOuts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 2, 1, 9),
    _PdnAtmVclStatClp0CellOuts_Type()
)
pdnAtmVclStatClp0CellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclStatClp0CellOuts.setStatus("current")
_PdnAtmVclStatTaggedOuts_Type = Counter32
_PdnAtmVclStatTaggedOuts_Object = MibTableColumn
pdnAtmVclStatTaggedOuts = _PdnAtmVclStatTaggedOuts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 2, 1, 10),
    _PdnAtmVclStatTaggedOuts_Type()
)
pdnAtmVclStatTaggedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclStatTaggedOuts.setStatus("current")
_PdnAtmVclStatRowStatus_Type = RowStatus
_PdnAtmVclStatRowStatus_Object = MibTableColumn
pdnAtmVclStatRowStatus = _PdnAtmVclStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 2, 1, 11),
    _PdnAtmVclStatRowStatus_Type()
)
pdnAtmVclStatRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAtmVclStatRowStatus.setStatus("current")
_PdnAtmVclCurrTable_Object = MibTable
pdnAtmVclCurrTable = _PdnAtmVclCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 3)
)
if mibBuilder.loadTexts:
    pdnAtmVclCurrTable.setStatus("current")
_PdnAtmVclCurrEntry_Object = MibTableRow
pdnAtmVclCurrEntry = _PdnAtmVclCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 3, 1)
)
pdnAtmVclCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    pdnAtmVclCurrEntry.setStatus("current")
_PdnAtmVclCurrElapsedTime_Type = TimeInterval
_PdnAtmVclCurrElapsedTime_Object = MibTableColumn
pdnAtmVclCurrElapsedTime = _PdnAtmVclCurrElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 3, 1, 1),
    _PdnAtmVclCurrElapsedTime_Type()
)
pdnAtmVclCurrElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclCurrElapsedTime.setStatus("current")
_PdnAtmVclCurrTotalCellIns_Type = Gauge32
_PdnAtmVclCurrTotalCellIns_Object = MibTableColumn
pdnAtmVclCurrTotalCellIns = _PdnAtmVclCurrTotalCellIns_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 3, 1, 2),
    _PdnAtmVclCurrTotalCellIns_Type()
)
pdnAtmVclCurrTotalCellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclCurrTotalCellIns.setStatus("current")
_PdnAtmVclCurrTotalInDiscards_Type = Gauge32
_PdnAtmVclCurrTotalInDiscards_Object = MibTableColumn
pdnAtmVclCurrTotalInDiscards = _PdnAtmVclCurrTotalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 3, 1, 3),
    _PdnAtmVclCurrTotalInDiscards_Type()
)
pdnAtmVclCurrTotalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclCurrTotalInDiscards.setStatus("current")
_PdnAtmVclCurrTotalCellOuts_Type = Gauge32
_PdnAtmVclCurrTotalCellOuts_Object = MibTableColumn
pdnAtmVclCurrTotalCellOuts = _PdnAtmVclCurrTotalCellOuts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 3, 1, 4),
    _PdnAtmVclCurrTotalCellOuts_Type()
)
pdnAtmVclCurrTotalCellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclCurrTotalCellOuts.setStatus("current")
_PdnAtmVclCurrTotalOutDiscards_Type = Gauge32
_PdnAtmVclCurrTotalOutDiscards_Object = MibTableColumn
pdnAtmVclCurrTotalOutDiscards = _PdnAtmVclCurrTotalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 3, 1, 5),
    _PdnAtmVclCurrTotalOutDiscards_Type()
)
pdnAtmVclCurrTotalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclCurrTotalOutDiscards.setStatus("current")
_PdnAtmVclHistTable_Object = MibTable
pdnAtmVclHistTable = _PdnAtmVclHistTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 4)
)
if mibBuilder.loadTexts:
    pdnAtmVclHistTable.setStatus("current")
_PdnAtmVclHistEntry_Object = MibTableRow
pdnAtmVclHistEntry = _PdnAtmVclHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 4, 1)
)
pdnAtmVclHistEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "PDN-ATMSTATS-MIB", "pdnAtmVclHistIndex"),
)
if mibBuilder.loadTexts:
    pdnAtmVclHistEntry.setStatus("current")


class _PdnAtmVclHistIndex_Type(Integer32):
    """Custom type pdnAtmVclHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PdnAtmVclHistIndex_Type.__name__ = "Integer32"
_PdnAtmVclHistIndex_Object = MibTableColumn
pdnAtmVclHistIndex = _PdnAtmVclHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 4, 1, 1),
    _PdnAtmVclHistIndex_Type()
)
pdnAtmVclHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnAtmVclHistIndex.setStatus("current")
_PdnAtmVclHistElapsedTime_Type = TimeInterval
_PdnAtmVclHistElapsedTime_Object = MibTableColumn
pdnAtmVclHistElapsedTime = _PdnAtmVclHistElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 4, 1, 2),
    _PdnAtmVclHistElapsedTime_Type()
)
pdnAtmVclHistElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclHistElapsedTime.setStatus("current")
_PdnAtmVclHistTotalCellIns_Type = Gauge32
_PdnAtmVclHistTotalCellIns_Object = MibTableColumn
pdnAtmVclHistTotalCellIns = _PdnAtmVclHistTotalCellIns_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 4, 1, 3),
    _PdnAtmVclHistTotalCellIns_Type()
)
pdnAtmVclHistTotalCellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclHistTotalCellIns.setStatus("current")
_PdnAtmVclHistTotalInDiscards_Type = Gauge32
_PdnAtmVclHistTotalInDiscards_Object = MibTableColumn
pdnAtmVclHistTotalInDiscards = _PdnAtmVclHistTotalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 4, 1, 4),
    _PdnAtmVclHistTotalInDiscards_Type()
)
pdnAtmVclHistTotalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclHistTotalInDiscards.setStatus("current")
_PdnAtmVclHistTotalCellOuts_Type = Gauge32
_PdnAtmVclHistTotalCellOuts_Object = MibTableColumn
pdnAtmVclHistTotalCellOuts = _PdnAtmVclHistTotalCellOuts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 4, 1, 5),
    _PdnAtmVclHistTotalCellOuts_Type()
)
pdnAtmVclHistTotalCellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclHistTotalCellOuts.setStatus("current")
_PdnAtmVclHistTotalOutDiscards_Type = Gauge32
_PdnAtmVclHistTotalOutDiscards_Object = MibTableColumn
pdnAtmVclHistTotalOutDiscards = _PdnAtmVclHistTotalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 2, 4, 1, 6),
    _PdnAtmVclHistTotalOutDiscards_Type()
)
pdnAtmVclHistTotalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmVclHistTotalOutDiscards.setStatus("current")
_PdnAtmStat_ObjectIdentity = ObjectIdentity
pdnAtmStat = _PdnAtmStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 3)
)
_PdnAtmStatTable_Object = MibTable
pdnAtmStatTable = _PdnAtmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 3, 1)
)
if mibBuilder.loadTexts:
    pdnAtmStatTable.setStatus("current")
_PdnAtmStatEntry_Object = MibTableRow
pdnAtmStatEntry = _PdnAtmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 3, 1, 1)
)
pdnAtmStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnAtmStatEntry.setStatus("current")
_PdnAtmStatHECErrors_Type = Counter32
_PdnAtmStatHECErrors_Object = MibTableColumn
pdnAtmStatHECErrors = _PdnAtmStatHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 3, 1, 1, 1),
    _PdnAtmStatHECErrors_Type()
)
pdnAtmStatHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmStatHECErrors.setStatus("current")
_PdnAtmStatLCDErrors_Type = Counter32
_PdnAtmStatLCDErrors_Object = MibTableColumn
pdnAtmStatLCDErrors = _PdnAtmStatLCDErrors_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 3, 3, 1, 1, 2),
    _PdnAtmStatLCDErrors_Type()
)
pdnAtmStatLCDErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmStatLCDErrors.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-ATMSTATS-MIB",
    **{"pdnAtmStatsMIB": pdnAtmStatsMIB,
       "pdnAtmVplStat": pdnAtmVplStat,
       "pdnAtmVplStatTable": pdnAtmVplStatTable,
       "pdnAtmVplStatEntry": pdnAtmVplStatEntry,
       "pdnAtmVplStatIfIndex": pdnAtmVplStatIfIndex,
       "pdnAtmVplStatVpi": pdnAtmVplStatVpi,
       "pdnAtmVplStatTotalCellIns": pdnAtmVplStatTotalCellIns,
       "pdnAtmVplStatClp0CellIns": pdnAtmVplStatClp0CellIns,
       "pdnAtmVplStatTotalDiscards": pdnAtmVplStatTotalDiscards,
       "pdnAtmVplStatClp0Discards": pdnAtmVplStatClp0Discards,
       "pdnAtmVplStatTotalCellOuts": pdnAtmVplStatTotalCellOuts,
       "pdnAtmVplStatClp0CellOuts": pdnAtmVplStatClp0CellOuts,
       "pdnAtmVplStatTaggedOuts": pdnAtmVplStatTaggedOuts,
       "pdnAtmVclStat": pdnAtmVclStat,
       "pdnAtmVclStatTable": pdnAtmVclStatTable,
       "pdnAtmVclStatEntry": pdnAtmVclStatEntry,
       "pdnAtmVclStatIfIndex": pdnAtmVclStatIfIndex,
       "pdnAtmVclStatVpi": pdnAtmVclStatVpi,
       "pdnAtmVclStatVci": pdnAtmVclStatVci,
       "pdnAtmVclStatTotalCellIns": pdnAtmVclStatTotalCellIns,
       "pdnAtmVclStatClp0CellIns": pdnAtmVclStatClp0CellIns,
       "pdnAtmVclStatTotalDiscards": pdnAtmVclStatTotalDiscards,
       "pdnAtmVclStatClp0Discards": pdnAtmVclStatClp0Discards,
       "pdnAtmVclStatTotalCellOuts": pdnAtmVclStatTotalCellOuts,
       "pdnAtmVclStatClp0CellOuts": pdnAtmVclStatClp0CellOuts,
       "pdnAtmVclStatTaggedOuts": pdnAtmVclStatTaggedOuts,
       "pdnAtmVclStatRowStatus": pdnAtmVclStatRowStatus,
       "pdnAtmVclCurrTable": pdnAtmVclCurrTable,
       "pdnAtmVclCurrEntry": pdnAtmVclCurrEntry,
       "pdnAtmVclCurrElapsedTime": pdnAtmVclCurrElapsedTime,
       "pdnAtmVclCurrTotalCellIns": pdnAtmVclCurrTotalCellIns,
       "pdnAtmVclCurrTotalInDiscards": pdnAtmVclCurrTotalInDiscards,
       "pdnAtmVclCurrTotalCellOuts": pdnAtmVclCurrTotalCellOuts,
       "pdnAtmVclCurrTotalOutDiscards": pdnAtmVclCurrTotalOutDiscards,
       "pdnAtmVclHistTable": pdnAtmVclHistTable,
       "pdnAtmVclHistEntry": pdnAtmVclHistEntry,
       "pdnAtmVclHistIndex": pdnAtmVclHistIndex,
       "pdnAtmVclHistElapsedTime": pdnAtmVclHistElapsedTime,
       "pdnAtmVclHistTotalCellIns": pdnAtmVclHistTotalCellIns,
       "pdnAtmVclHistTotalInDiscards": pdnAtmVclHistTotalInDiscards,
       "pdnAtmVclHistTotalCellOuts": pdnAtmVclHistTotalCellOuts,
       "pdnAtmVclHistTotalOutDiscards": pdnAtmVclHistTotalOutDiscards,
       "pdnAtmStat": pdnAtmStat,
       "pdnAtmStatTable": pdnAtmStatTable,
       "pdnAtmStatEntry": pdnAtmStatEntry,
       "pdnAtmStatHECErrors": pdnAtmStatHECErrors,
       "pdnAtmStatLCDErrors": pdnAtmStatLCDErrors}
)
