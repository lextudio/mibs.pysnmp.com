# SNMP MIB module (DSLAM-UPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DSLAM-UPC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:40 2024
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
 atmVclVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi",
    "atmVplVpi")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pgainDSLAM,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgainDSLAM")

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

pgUpcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PgUpcObjects_ObjectIdentity = ObjectIdentity
pgUpcObjects = _PgUpcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1)
)
_PgAtmUpcPortTable_Object = MibTable
pgAtmUpcPortTable = _PgAtmUpcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 1)
)
if mibBuilder.loadTexts:
    pgAtmUpcPortTable.setStatus("mandatory")
_PgAtmUpcPortEntry_Object = MibTableRow
pgAtmUpcPortEntry = _PgAtmUpcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 1, 1)
)
pgAtmUpcPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgAtmUpcPortEntry.setStatus("mandatory")


class _PgAtmUpcPortAdminStatus_Type(Integer32):
    """Custom type pgAtmUpcPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PgAtmUpcPortAdminStatus_Type.__name__ = "Integer32"
_PgAtmUpcPortAdminStatus_Object = MibTableColumn
pgAtmUpcPortAdminStatus = _PgAtmUpcPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 1, 1, 1),
    _PgAtmUpcPortAdminStatus_Type()
)
pgAtmUpcPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAtmUpcPortAdminStatus.setStatus("mandatory")
_PgAtmUpcVplTable_Object = MibTable
pgAtmUpcVplTable = _PgAtmUpcVplTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 2)
)
if mibBuilder.loadTexts:
    pgAtmUpcVplTable.setStatus("mandatory")
_PgAtmUpcVplEntry_Object = MibTableRow
pgAtmUpcVplEntry = _PgAtmUpcVplEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 2, 1)
)
pgAtmUpcVplEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    pgAtmUpcVplEntry.setStatus("mandatory")


class _PgAtmUpcVplAdminStatus_Type(Integer32):
    """Custom type pgAtmUpcVplAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PgAtmUpcVplAdminStatus_Type.__name__ = "Integer32"
_PgAtmUpcVplAdminStatus_Object = MibTableColumn
pgAtmUpcVplAdminStatus = _PgAtmUpcVplAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 2, 1, 1),
    _PgAtmUpcVplAdminStatus_Type()
)
pgAtmUpcVplAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAtmUpcVplAdminStatus.setStatus("mandatory")
_PgAtmUpcVclTable_Object = MibTable
pgAtmUpcVclTable = _PgAtmUpcVclTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 3)
)
if mibBuilder.loadTexts:
    pgAtmUpcVclTable.setStatus("mandatory")
_PgAtmUpcVclEntry_Object = MibTableRow
pgAtmUpcVclEntry = _PgAtmUpcVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 3, 1)
)
pgAtmUpcVclEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    pgAtmUpcVclEntry.setStatus("mandatory")


class _PgAtmUpcVclAdminStatus_Type(Integer32):
    """Custom type pgAtmUpcVclAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PgAtmUpcVclAdminStatus_Type.__name__ = "Integer32"
_PgAtmUpcVclAdminStatus_Object = MibTableColumn
pgAtmUpcVclAdminStatus = _PgAtmUpcVclAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 3, 1, 1),
    _PgAtmUpcVclAdminStatus_Type()
)
pgAtmUpcVclAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAtmUpcVclAdminStatus.setStatus("mandatory")
_PgAtmVplStatTable_Object = MibTable
pgAtmVplStatTable = _PgAtmVplStatTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 4)
)
if mibBuilder.loadTexts:
    pgAtmVplStatTable.setStatus("mandatory")
_PgAtmVplStatEntry_Object = MibTableRow
pgAtmVplStatEntry = _PgAtmVplStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 4, 1)
)
pgAtmVplStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    pgAtmVplStatEntry.setStatus("mandatory")
_PgAtmVplStatTotalCellIns_Type = Counter64
_PgAtmVplStatTotalCellIns_Object = MibTableColumn
pgAtmVplStatTotalCellIns = _PgAtmVplStatTotalCellIns_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 4, 1, 1),
    _PgAtmVplStatTotalCellIns_Type()
)
pgAtmVplStatTotalCellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVplStatTotalCellIns.setStatus("mandatory")
_PgAtmVplStatClp0CellIns_Type = Counter64
_PgAtmVplStatClp0CellIns_Object = MibTableColumn
pgAtmVplStatClp0CellIns = _PgAtmVplStatClp0CellIns_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 4, 1, 2),
    _PgAtmVplStatClp0CellIns_Type()
)
pgAtmVplStatClp0CellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVplStatClp0CellIns.setStatus("mandatory")
_PgAtmVplStatTotalDiscards_Type = Counter64
_PgAtmVplStatTotalDiscards_Object = MibTableColumn
pgAtmVplStatTotalDiscards = _PgAtmVplStatTotalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 4, 1, 3),
    _PgAtmVplStatTotalDiscards_Type()
)
pgAtmVplStatTotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVplStatTotalDiscards.setStatus("mandatory")
_PgAtmVplStatClp0Discards_Type = Counter64
_PgAtmVplStatClp0Discards_Object = MibTableColumn
pgAtmVplStatClp0Discards = _PgAtmVplStatClp0Discards_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 4, 1, 4),
    _PgAtmVplStatClp0Discards_Type()
)
pgAtmVplStatClp0Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVplStatClp0Discards.setStatus("mandatory")
_PgAtmVplStatTotalCellOuts_Type = Counter64
_PgAtmVplStatTotalCellOuts_Object = MibTableColumn
pgAtmVplStatTotalCellOuts = _PgAtmVplStatTotalCellOuts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 4, 1, 5),
    _PgAtmVplStatTotalCellOuts_Type()
)
pgAtmVplStatTotalCellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVplStatTotalCellOuts.setStatus("mandatory")
_PgAtmVplStatClp0CellOuts_Type = Counter64
_PgAtmVplStatClp0CellOuts_Object = MibTableColumn
pgAtmVplStatClp0CellOuts = _PgAtmVplStatClp0CellOuts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 4, 1, 6),
    _PgAtmVplStatClp0CellOuts_Type()
)
pgAtmVplStatClp0CellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVplStatClp0CellOuts.setStatus("mandatory")
_PgAtmVplStatTaggedOuts_Type = Counter64
_PgAtmVplStatTaggedOuts_Object = MibTableColumn
pgAtmVplStatTaggedOuts = _PgAtmVplStatTaggedOuts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 4, 1, 7),
    _PgAtmVplStatTaggedOuts_Type()
)
pgAtmVplStatTaggedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVplStatTaggedOuts.setStatus("mandatory")
_PgAtmVplStatTotalNonConforming_Type = Counter64
_PgAtmVplStatTotalNonConforming_Object = MibTableColumn
pgAtmVplStatTotalNonConforming = _PgAtmVplStatTotalNonConforming_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 4, 1, 8),
    _PgAtmVplStatTotalNonConforming_Type()
)
pgAtmVplStatTotalNonConforming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVplStatTotalNonConforming.setStatus("mandatory")


class _PgAtmVplStatClearCounters_Type(Integer32):
    """Custom type pgAtmVplStatClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_PgAtmVplStatClearCounters_Type.__name__ = "Integer32"
_PgAtmVplStatClearCounters_Object = MibTableColumn
pgAtmVplStatClearCounters = _PgAtmVplStatClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 4, 1, 9),
    _PgAtmVplStatClearCounters_Type()
)
pgAtmVplStatClearCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pgAtmVplStatClearCounters.setStatus("mandatory")


class _PgAtmVplStatAllClearCounters_Type(Integer32):
    """Custom type pgAtmVplStatAllClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_PgAtmVplStatAllClearCounters_Type.__name__ = "Integer32"
_PgAtmVplStatAllClearCounters_Object = MibScalar
pgAtmVplStatAllClearCounters = _PgAtmVplStatAllClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 5),
    _PgAtmVplStatAllClearCounters_Type()
)
pgAtmVplStatAllClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAtmVplStatAllClearCounters.setStatus("mandatory")
_PgAtmVclStatTable_Object = MibTable
pgAtmVclStatTable = _PgAtmVclStatTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 6)
)
if mibBuilder.loadTexts:
    pgAtmVclStatTable.setStatus("mandatory")
_PgAtmVclStatEntry_Object = MibTableRow
pgAtmVclStatEntry = _PgAtmVclStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 6, 1)
)
pgAtmVclStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    pgAtmVclStatEntry.setStatus("mandatory")
_PgAtmVclStatTotalCellIns_Type = Counter64
_PgAtmVclStatTotalCellIns_Object = MibTableColumn
pgAtmVclStatTotalCellIns = _PgAtmVclStatTotalCellIns_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 6, 1, 1),
    _PgAtmVclStatTotalCellIns_Type()
)
pgAtmVclStatTotalCellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVclStatTotalCellIns.setStatus("mandatory")
_PgAtmVclStatClp0CellIns_Type = Counter64
_PgAtmVclStatClp0CellIns_Object = MibTableColumn
pgAtmVclStatClp0CellIns = _PgAtmVclStatClp0CellIns_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 6, 1, 2),
    _PgAtmVclStatClp0CellIns_Type()
)
pgAtmVclStatClp0CellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVclStatClp0CellIns.setStatus("mandatory")
_PgAtmVclStatTotalDiscards_Type = Counter64
_PgAtmVclStatTotalDiscards_Object = MibTableColumn
pgAtmVclStatTotalDiscards = _PgAtmVclStatTotalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 6, 1, 3),
    _PgAtmVclStatTotalDiscards_Type()
)
pgAtmVclStatTotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVclStatTotalDiscards.setStatus("mandatory")
_PgAtmVclStatClp0Discards_Type = Counter64
_PgAtmVclStatClp0Discards_Object = MibTableColumn
pgAtmVclStatClp0Discards = _PgAtmVclStatClp0Discards_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 6, 1, 4),
    _PgAtmVclStatClp0Discards_Type()
)
pgAtmVclStatClp0Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVclStatClp0Discards.setStatus("mandatory")
_PgAtmVclStatTotalCellOuts_Type = Counter64
_PgAtmVclStatTotalCellOuts_Object = MibTableColumn
pgAtmVclStatTotalCellOuts = _PgAtmVclStatTotalCellOuts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 6, 1, 5),
    _PgAtmVclStatTotalCellOuts_Type()
)
pgAtmVclStatTotalCellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVclStatTotalCellOuts.setStatus("mandatory")
_PgAtmVclStatClp0CellOuts_Type = Counter64
_PgAtmVclStatClp0CellOuts_Object = MibTableColumn
pgAtmVclStatClp0CellOuts = _PgAtmVclStatClp0CellOuts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 6, 1, 6),
    _PgAtmVclStatClp0CellOuts_Type()
)
pgAtmVclStatClp0CellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVclStatClp0CellOuts.setStatus("mandatory")
_PgAtmVclStatTaggedOuts_Type = Counter64
_PgAtmVclStatTaggedOuts_Object = MibTableColumn
pgAtmVclStatTaggedOuts = _PgAtmVclStatTaggedOuts_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 6, 1, 7),
    _PgAtmVclStatTaggedOuts_Type()
)
pgAtmVclStatTaggedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVclStatTaggedOuts.setStatus("mandatory")
_PgAtmVclStatTotalNonConforming_Type = Counter64
_PgAtmVclStatTotalNonConforming_Object = MibTableColumn
pgAtmVclStatTotalNonConforming = _PgAtmVclStatTotalNonConforming_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 6, 1, 8),
    _PgAtmVclStatTotalNonConforming_Type()
)
pgAtmVclStatTotalNonConforming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgAtmVclStatTotalNonConforming.setStatus("mandatory")


class _PgAtmVclStatClearCounters_Type(Integer32):
    """Custom type pgAtmVclStatClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_PgAtmVclStatClearCounters_Type.__name__ = "Integer32"
_PgAtmVclStatClearCounters_Object = MibTableColumn
pgAtmVclStatClearCounters = _PgAtmVclStatClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 6, 1, 9),
    _PgAtmVclStatClearCounters_Type()
)
pgAtmVclStatClearCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pgAtmVclStatClearCounters.setStatus("mandatory")


class _PgAtmVclStatAllClearCounters_Type(Integer32):
    """Custom type pgAtmVclStatAllClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_PgAtmVclStatAllClearCounters_Type.__name__ = "Integer32"
_PgAtmVclStatAllClearCounters_Object = MibScalar
pgAtmVclStatAllClearCounters = _PgAtmVclStatAllClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 11, 1, 7),
    _PgAtmVclStatAllClearCounters_Type()
)
pgAtmVclStatAllClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgAtmVclStatAllClearCounters.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSLAM-UPC-MIB",
    **{"pgUpcMIB": pgUpcMIB,
       "pgUpcObjects": pgUpcObjects,
       "pgAtmUpcPortTable": pgAtmUpcPortTable,
       "pgAtmUpcPortEntry": pgAtmUpcPortEntry,
       "pgAtmUpcPortAdminStatus": pgAtmUpcPortAdminStatus,
       "pgAtmUpcVplTable": pgAtmUpcVplTable,
       "pgAtmUpcVplEntry": pgAtmUpcVplEntry,
       "pgAtmUpcVplAdminStatus": pgAtmUpcVplAdminStatus,
       "pgAtmUpcVclTable": pgAtmUpcVclTable,
       "pgAtmUpcVclEntry": pgAtmUpcVclEntry,
       "pgAtmUpcVclAdminStatus": pgAtmUpcVclAdminStatus,
       "pgAtmVplStatTable": pgAtmVplStatTable,
       "pgAtmVplStatEntry": pgAtmVplStatEntry,
       "pgAtmVplStatTotalCellIns": pgAtmVplStatTotalCellIns,
       "pgAtmVplStatClp0CellIns": pgAtmVplStatClp0CellIns,
       "pgAtmVplStatTotalDiscards": pgAtmVplStatTotalDiscards,
       "pgAtmVplStatClp0Discards": pgAtmVplStatClp0Discards,
       "pgAtmVplStatTotalCellOuts": pgAtmVplStatTotalCellOuts,
       "pgAtmVplStatClp0CellOuts": pgAtmVplStatClp0CellOuts,
       "pgAtmVplStatTaggedOuts": pgAtmVplStatTaggedOuts,
       "pgAtmVplStatTotalNonConforming": pgAtmVplStatTotalNonConforming,
       "pgAtmVplStatClearCounters": pgAtmVplStatClearCounters,
       "pgAtmVplStatAllClearCounters": pgAtmVplStatAllClearCounters,
       "pgAtmVclStatTable": pgAtmVclStatTable,
       "pgAtmVclStatEntry": pgAtmVclStatEntry,
       "pgAtmVclStatTotalCellIns": pgAtmVclStatTotalCellIns,
       "pgAtmVclStatClp0CellIns": pgAtmVclStatClp0CellIns,
       "pgAtmVclStatTotalDiscards": pgAtmVclStatTotalDiscards,
       "pgAtmVclStatClp0Discards": pgAtmVclStatClp0Discards,
       "pgAtmVclStatTotalCellOuts": pgAtmVclStatTotalCellOuts,
       "pgAtmVclStatClp0CellOuts": pgAtmVclStatClp0CellOuts,
       "pgAtmVclStatTaggedOuts": pgAtmVclStatTaggedOuts,
       "pgAtmVclStatTotalNonConforming": pgAtmVclStatTotalNonConforming,
       "pgAtmVclStatClearCounters": pgAtmVclStatClearCounters,
       "pgAtmVclStatAllClearCounters": pgAtmVclStatAllClearCounters}
)
