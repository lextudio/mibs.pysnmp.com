# SNMP MIB module (SYNOPTICS-RMON-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYNOPTICS-RMON-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:04 2024
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

(products,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "products")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnpxRmonExt_ObjectIdentity = ObjectIdentity
snpxRmonExt = _SnpxRmonExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 8)
)
_SnpxRmonGetTabExt_ObjectIdentity = ObjectIdentity
snpxRmonGetTabExt = _SnpxRmonGetTabExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 8, 6)
)
_GetTable_ObjectIdentity = ObjectIdentity
getTable = _GetTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 8, 6, 1)
)
_GetTableTable_Object = MibTable
getTableTable = _GetTableTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 8, 6, 1, 1)
)
if mibBuilder.loadTexts:
    getTableTable.setStatus("mandatory")
_GetTableEntry_Object = MibTableRow
getTableEntry = _GetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 8, 6, 1, 1, 1)
)
getTableEntry.setIndexNames(
    (0, "SYNOPTICS-RMON-EXT-MIB", "getTableSource"),
    (0, "SYNOPTICS-RMON-EXT-MIB", "getTableIndex"),
)
if mibBuilder.loadTexts:
    getTableEntry.setStatus("mandatory")
_GetTableSource_Type = ObjectIdentifier
_GetTableSource_Object = MibTableColumn
getTableSource = _GetTableSource_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 8, 6, 1, 1, 1, 1),
    _GetTableSource_Type()
)
getTableSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    getTableSource.setStatus("mandatory")
_GetTableIndex_Type = ObjectIdentifier
_GetTableIndex_Object = MibTableColumn
getTableIndex = _GetTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 8, 6, 1, 1, 1, 2),
    _GetTableIndex_Type()
)
getTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    getTableIndex.setStatus("mandatory")


class _GetTableData_Type(OctetString):
    """Custom type getTableData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1200),
    )


_GetTableData_Type.__name__ = "OctetString"
_GetTableData_Object = MibTableColumn
getTableData = _GetTableData_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 8, 6, 1, 1, 1, 3),
    _GetTableData_Type()
)
getTableData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    getTableData.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOPTICS-RMON-EXT-MIB",
    **{"snpxRmonExt": snpxRmonExt,
       "snpxRmonGetTabExt": snpxRmonGetTabExt,
       "getTable": getTable,
       "getTableTable": getTableTable,
       "getTableEntry": getTableEntry,
       "getTableSource": getTableSource,
       "getTableIndex": getTableIndex,
       "getTableData": getTableData}
)
