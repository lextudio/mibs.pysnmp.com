# SNMP MIB module (CTRON-LINE-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-LINE-STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:01 2024
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

(cabletron,) = mibBuilder.importSymbols(
    "CTRON-OIDS",
    "cabletron")

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

_CtSSA_ObjectIdentity = ObjectIdentity
ctSSA = _CtSSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497)
)
_CtDsx1LineStatisticsTable_Object = MibTable
ctDsx1LineStatisticsTable = _CtDsx1LineStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21)
)
if mibBuilder.loadTexts:
    ctDsx1LineStatisticsTable.setStatus("mandatory")
_CtDsx1LineStatisticsEntry_Object = MibTableRow
ctDsx1LineStatisticsEntry = _CtDsx1LineStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1)
)
ctDsx1LineStatisticsEntry.setIndexNames(
    (0, "CTRON-LINE-STATISTICS-MIB", "lsLineIndex"),
)
if mibBuilder.loadTexts:
    ctDsx1LineStatisticsEntry.setStatus("mandatory")
_LsLineIndex_Type = Integer32
_LsLineIndex_Object = MibTableColumn
lsLineIndex = _LsLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 1),
    _LsLineIndex_Type()
)
lsLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLineIndex.setStatus("mandatory")
_LsLayer1Up_Type = Integer32
_LsLayer1Up_Object = MibTableColumn
lsLayer1Up = _LsLayer1Up_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 2),
    _LsLayer1Up_Type()
)
lsLayer1Up.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLayer1Up.setStatus("mandatory")
_LsLayer1Down_Type = Integer32
_LsLayer1Down_Object = MibTableColumn
lsLayer1Down = _LsLayer1Down_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 3),
    _LsLayer1Down_Type()
)
lsLayer1Down.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLayer1Down.setStatus("mandatory")
_LsLayer1LOS_Type = Integer32
_LsLayer1LOS_Object = MibTableColumn
lsLayer1LOS = _LsLayer1LOS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 4),
    _LsLayer1LOS_Type()
)
lsLayer1LOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLayer1LOS.setStatus("mandatory")
_LsLayer1LOF_Type = Integer32
_LsLayer1LOF_Object = MibTableColumn
lsLayer1LOF = _LsLayer1LOF_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 5),
    _LsLayer1LOF_Type()
)
lsLayer1LOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLayer1LOF.setStatus("mandatory")
_LsLayer1RAI_Type = Integer32
_LsLayer1RAI_Object = MibTableColumn
lsLayer1RAI = _LsLayer1RAI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 6),
    _LsLayer1RAI_Type()
)
lsLayer1RAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLayer1RAI.setStatus("mandatory")
_LsLayer1AIS_Type = Integer32
_LsLayer1AIS_Object = MibTableColumn
lsLayer1AIS = _LsLayer1AIS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 7),
    _LsLayer1AIS_Type()
)
lsLayer1AIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLayer1AIS.setStatus("mandatory")
_LsLayer1LOSAll_Type = Integer32
_LsLayer1LOSAll_Object = MibTableColumn
lsLayer1LOSAll = _LsLayer1LOSAll_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 8),
    _LsLayer1LOSAll_Type()
)
lsLayer1LOSAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLayer1LOSAll.setStatus("mandatory")
_LsLayer1LOFAll_Type = Integer32
_LsLayer1LOFAll_Object = MibTableColumn
lsLayer1LOFAll = _LsLayer1LOFAll_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 9),
    _LsLayer1LOFAll_Type()
)
lsLayer1LOFAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLayer1LOFAll.setStatus("mandatory")
_LsLayer1RAIAll_Type = Integer32
_LsLayer1RAIAll_Object = MibTableColumn
lsLayer1RAIAll = _LsLayer1RAIAll_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 10),
    _LsLayer1RAIAll_Type()
)
lsLayer1RAIAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLayer1RAIAll.setStatus("mandatory")
_LsLayer1AISAll_Type = Integer32
_LsLayer1AISAll_Object = MibTableColumn
lsLayer1AISAll = _LsLayer1AISAll_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 11),
    _LsLayer1AISAll_Type()
)
lsLayer1AISAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLayer1AISAll.setStatus("mandatory")
_LsLayer1Interrupts_Type = Integer32
_LsLayer1Interrupts_Object = MibTableColumn
lsLayer1Interrupts = _LsLayer1Interrupts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 12),
    _LsLayer1Interrupts_Type()
)
lsLayer1Interrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsLayer1Interrupts.setStatus("mandatory")
_LsLayer1ClearStats_Type = Integer32
_LsLayer1ClearStats_Object = MibTableColumn
lsLayer1ClearStats = _LsLayer1ClearStats_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 21, 1, 13),
    _LsLayer1ClearStats_Type()
)
lsLayer1ClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsLayer1ClearStats.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-LINE-STATISTICS-MIB",
    **{"ctSSA": ctSSA,
       "ctDsx1LineStatisticsTable": ctDsx1LineStatisticsTable,
       "ctDsx1LineStatisticsEntry": ctDsx1LineStatisticsEntry,
       "lsLineIndex": lsLineIndex,
       "lsLayer1Up": lsLayer1Up,
       "lsLayer1Down": lsLayer1Down,
       "lsLayer1LOS": lsLayer1LOS,
       "lsLayer1LOF": lsLayer1LOF,
       "lsLayer1RAI": lsLayer1RAI,
       "lsLayer1AIS": lsLayer1AIS,
       "lsLayer1LOSAll": lsLayer1LOSAll,
       "lsLayer1LOFAll": lsLayer1LOFAll,
       "lsLayer1RAIAll": lsLayer1RAIAll,
       "lsLayer1AISAll": lsLayer1AISAll,
       "lsLayer1Interrupts": lsLayer1Interrupts,
       "lsLayer1ClearStats": lsLayer1ClearStats}
)
