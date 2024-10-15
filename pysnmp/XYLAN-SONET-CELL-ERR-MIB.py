# SNMP MIB module (XYLAN-SONET-CELL-ERR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-SONET-CELL-ERR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:14 2024
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

(xylanSonetArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanSonetArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanSonetErrStats_ObjectIdentity = ObjectIdentity
xylanSonetErrStats = _XylanSonetErrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 2)
)
_XylanSonetPortStatTable_Object = MibTable
xylanSonetPortStatTable = _XylanSonetPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 2, 1)
)
if mibBuilder.loadTexts:
    xylanSonetPortStatTable.setStatus("mandatory")
_XylanSonetPortStatEntry_Object = MibTableRow
xylanSonetPortStatEntry = _XylanSonetPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 2, 1, 1)
)
xylanSonetPortStatEntry.setIndexNames(
    (0, "XYLAN-SONET-CELL-ERR-MIB", "xylanSonetPortStatSlotIndex"),
    (0, "XYLAN-SONET-CELL-ERR-MIB", "xylanSonetPortStatPortIndex"),
)
if mibBuilder.loadTexts:
    xylanSonetPortStatEntry.setStatus("mandatory")


class _XylanSonetPortStatSlotIndex_Type(Integer32):
    """Custom type xylanSonetPortStatSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XylanSonetPortStatSlotIndex_Type.__name__ = "Integer32"
_XylanSonetPortStatSlotIndex_Object = MibTableColumn
xylanSonetPortStatSlotIndex = _XylanSonetPortStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 2, 1, 1, 1),
    _XylanSonetPortStatSlotIndex_Type()
)
xylanSonetPortStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanSonetPortStatSlotIndex.setStatus("mandatory")
_XylanSonetPortStatPortIndex_Type = Integer32
_XylanSonetPortStatPortIndex_Object = MibTableColumn
xylanSonetPortStatPortIndex = _XylanSonetPortStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 2, 1, 1, 2),
    _XylanSonetPortStatPortIndex_Type()
)
xylanSonetPortStatPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanSonetPortStatPortIndex.setStatus("mandatory")
_XylanSonetPortStatRxCellCount_Type = Integer32
_XylanSonetPortStatRxCellCount_Object = MibTableColumn
xylanSonetPortStatRxCellCount = _XylanSonetPortStatRxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 2, 1, 1, 3),
    _XylanSonetPortStatRxCellCount_Type()
)
xylanSonetPortStatRxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanSonetPortStatRxCellCount.setStatus("mandatory")
_XylanSonetPortStatCorrHCSCellCount_Type = Integer32
_XylanSonetPortStatCorrHCSCellCount_Object = MibTableColumn
xylanSonetPortStatCorrHCSCellCount = _XylanSonetPortStatCorrHCSCellCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 2, 1, 1, 4),
    _XylanSonetPortStatCorrHCSCellCount_Type()
)
xylanSonetPortStatCorrHCSCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanSonetPortStatCorrHCSCellCount.setStatus("mandatory")
_XylanSonetPortStatUncorrHCSCellCount_Type = Integer32
_XylanSonetPortStatUncorrHCSCellCount_Object = MibTableColumn
xylanSonetPortStatUncorrHCSCellCount = _XylanSonetPortStatUncorrHCSCellCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 23, 2, 1, 1, 5),
    _XylanSonetPortStatUncorrHCSCellCount_Type()
)
xylanSonetPortStatUncorrHCSCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanSonetPortStatUncorrHCSCellCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-SONET-CELL-ERR-MIB",
    **{"xylanSonetErrStats": xylanSonetErrStats,
       "xylanSonetPortStatTable": xylanSonetPortStatTable,
       "xylanSonetPortStatEntry": xylanSonetPortStatEntry,
       "xylanSonetPortStatSlotIndex": xylanSonetPortStatSlotIndex,
       "xylanSonetPortStatPortIndex": xylanSonetPortStatPortIndex,
       "xylanSonetPortStatRxCellCount": xylanSonetPortStatRxCellCount,
       "xylanSonetPortStatCorrHCSCellCount": xylanSonetPortStatCorrHCSCellCount,
       "xylanSonetPortStatUncorrHCSCellCount": xylanSonetPortStatUncorrHCSCellCount}
)
