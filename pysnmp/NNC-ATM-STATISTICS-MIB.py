# SNMP MIB module (NNC-ATM-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNC-ATM-STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:11 2024
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

(NncExtAbsIntvlNumberType,
 NncExtIntvlStateType,
 NncExtRelIntvlNumberType) = mibBuilder.importSymbols(
    "NNC-INTERVAL-STATISTICS-TC-MIB",
    "NncExtAbsIntvlNumberType",
    "NncExtIntvlStateType",
    "NncExtRelIntvlNumberType")

(NncExtCounter64,
 nncExtensions) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "NncExtCounter64",
    "nncExtensions")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

nncAtmStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncAtmStatisticsObjects_ObjectIdentity = ObjectIdentity
nncAtmStatisticsObjects = _NncAtmStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1)
)
_NncVpl15MinCurrentTable_Object = MibTable
nncVpl15MinCurrentTable = _NncVpl15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 1)
)
if mibBuilder.loadTexts:
    nncVpl15MinCurrentTable.setStatus("current")
_NncVpl15MinCurrentEntry_Object = MibTableRow
nncVpl15MinCurrentEntry = _NncVpl15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 1, 1)
)
nncVpl15MinCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    nncVpl15MinCurrentEntry.setStatus("current")
_NncVpl15MinCurrentState_Type = NncExtIntvlStateType
_NncVpl15MinCurrentState_Object = MibTableColumn
nncVpl15MinCurrentState = _NncVpl15MinCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 1, 1, 1),
    _NncVpl15MinCurrentState_Type()
)
nncVpl15MinCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinCurrentState.setStatus("current")
_NncVpl15MinCurrentAbsoluteIntervalNumber_Type = NncExtAbsIntvlNumberType
_NncVpl15MinCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncVpl15MinCurrentAbsoluteIntervalNumber = _NncVpl15MinCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 1, 1, 2),
    _NncVpl15MinCurrentAbsoluteIntervalNumber_Type()
)
nncVpl15MinCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinCurrentAbsoluteIntervalNumber.setStatus("current")
_NncVpl15MinCurrentClp0And1InCells_Type = NncExtCounter64
_NncVpl15MinCurrentClp0And1InCells_Object = MibTableColumn
nncVpl15MinCurrentClp0And1InCells = _NncVpl15MinCurrentClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 1, 1, 3),
    _NncVpl15MinCurrentClp0And1InCells_Type()
)
nncVpl15MinCurrentClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinCurrentClp0And1InCells.setStatus("current")
_NncVpl15MinCurrentClp0InCells_Type = NncExtCounter64
_NncVpl15MinCurrentClp0InCells_Object = MibTableColumn
nncVpl15MinCurrentClp0InCells = _NncVpl15MinCurrentClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 1, 1, 4),
    _NncVpl15MinCurrentClp0InCells_Type()
)
nncVpl15MinCurrentClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinCurrentClp0InCells.setStatus("current")
_NncVpl15MinCurrentDiscardClp0And1InCells_Type = NncExtCounter64
_NncVpl15MinCurrentDiscardClp0And1InCells_Object = MibTableColumn
nncVpl15MinCurrentDiscardClp0And1InCells = _NncVpl15MinCurrentDiscardClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 1, 1, 5),
    _NncVpl15MinCurrentDiscardClp0And1InCells_Type()
)
nncVpl15MinCurrentDiscardClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinCurrentDiscardClp0And1InCells.setStatus("current")
_NncVpl15MinCurrentDiscardClp0InCells_Type = NncExtCounter64
_NncVpl15MinCurrentDiscardClp0InCells_Object = MibTableColumn
nncVpl15MinCurrentDiscardClp0InCells = _NncVpl15MinCurrentDiscardClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 1, 1, 6),
    _NncVpl15MinCurrentDiscardClp0InCells_Type()
)
nncVpl15MinCurrentDiscardClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinCurrentDiscardClp0InCells.setStatus("current")
_NncVpl15MinCurrentTaggedInCells_Type = NncExtCounter64
_NncVpl15MinCurrentTaggedInCells_Object = MibTableColumn
nncVpl15MinCurrentTaggedInCells = _NncVpl15MinCurrentTaggedInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 1, 1, 7),
    _NncVpl15MinCurrentTaggedInCells_Type()
)
nncVpl15MinCurrentTaggedInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinCurrentTaggedInCells.setStatus("current")
_NncVpl15MinCurrentClp0And1OutCells_Type = NncExtCounter64
_NncVpl15MinCurrentClp0And1OutCells_Object = MibTableColumn
nncVpl15MinCurrentClp0And1OutCells = _NncVpl15MinCurrentClp0And1OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 1, 1, 8),
    _NncVpl15MinCurrentClp0And1OutCells_Type()
)
nncVpl15MinCurrentClp0And1OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinCurrentClp0And1OutCells.setStatus("current")
_NncVpl15MinCurrentClp0OutCells_Type = NncExtCounter64
_NncVpl15MinCurrentClp0OutCells_Object = MibTableColumn
nncVpl15MinCurrentClp0OutCells = _NncVpl15MinCurrentClp0OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 1, 1, 9),
    _NncVpl15MinCurrentClp0OutCells_Type()
)
nncVpl15MinCurrentClp0OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinCurrentClp0OutCells.setStatus("current")
_NncVpl15MinIntervalTable_Object = MibTable
nncVpl15MinIntervalTable = _NncVpl15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 2)
)
if mibBuilder.loadTexts:
    nncVpl15MinIntervalTable.setStatus("current")
_NncVpl15MinIntervalEntry_Object = MibTableRow
nncVpl15MinIntervalEntry = _NncVpl15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 2, 1)
)
nncVpl15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "NNC-ATM-STATISTICS-MIB", "nncVpl15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncVpl15MinIntervalEntry.setStatus("current")
_NncVpl15MinIntervalNumber_Type = NncExtRelIntvlNumberType
_NncVpl15MinIntervalNumber_Object = MibTableColumn
nncVpl15MinIntervalNumber = _NncVpl15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 2, 1, 1),
    _NncVpl15MinIntervalNumber_Type()
)
nncVpl15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncVpl15MinIntervalNumber.setStatus("current")
_NncVpl15MinIntervalState_Type = NncExtIntvlStateType
_NncVpl15MinIntervalState_Object = MibTableColumn
nncVpl15MinIntervalState = _NncVpl15MinIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 2, 1, 2),
    _NncVpl15MinIntervalState_Type()
)
nncVpl15MinIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinIntervalState.setStatus("current")
_NncVpl15MinIntervalAbsoluteIntervalNumber_Type = NncExtAbsIntvlNumberType
_NncVpl15MinIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncVpl15MinIntervalAbsoluteIntervalNumber = _NncVpl15MinIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 2, 1, 3),
    _NncVpl15MinIntervalAbsoluteIntervalNumber_Type()
)
nncVpl15MinIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinIntervalAbsoluteIntervalNumber.setStatus("current")
_NncVpl15MinIntervalClp0And1InCells_Type = NncExtCounter64
_NncVpl15MinIntervalClp0And1InCells_Object = MibTableColumn
nncVpl15MinIntervalClp0And1InCells = _NncVpl15MinIntervalClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 2, 1, 4),
    _NncVpl15MinIntervalClp0And1InCells_Type()
)
nncVpl15MinIntervalClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinIntervalClp0And1InCells.setStatus("current")
_NncVpl15MinIntervalClp0InCells_Type = NncExtCounter64
_NncVpl15MinIntervalClp0InCells_Object = MibTableColumn
nncVpl15MinIntervalClp0InCells = _NncVpl15MinIntervalClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 2, 1, 5),
    _NncVpl15MinIntervalClp0InCells_Type()
)
nncVpl15MinIntervalClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinIntervalClp0InCells.setStatus("current")
_NncVpl15MinIntervalDiscardClp0And1InCells_Type = NncExtCounter64
_NncVpl15MinIntervalDiscardClp0And1InCells_Object = MibTableColumn
nncVpl15MinIntervalDiscardClp0And1InCells = _NncVpl15MinIntervalDiscardClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 2, 1, 6),
    _NncVpl15MinIntervalDiscardClp0And1InCells_Type()
)
nncVpl15MinIntervalDiscardClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinIntervalDiscardClp0And1InCells.setStatus("current")
_NncVpl15MinIntervalDiscardClp0InCells_Type = NncExtCounter64
_NncVpl15MinIntervalDiscardClp0InCells_Object = MibTableColumn
nncVpl15MinIntervalDiscardClp0InCells = _NncVpl15MinIntervalDiscardClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 2, 1, 7),
    _NncVpl15MinIntervalDiscardClp0InCells_Type()
)
nncVpl15MinIntervalDiscardClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinIntervalDiscardClp0InCells.setStatus("current")
_NncVpl15MinIntervalTaggedInCells_Type = NncExtCounter64
_NncVpl15MinIntervalTaggedInCells_Object = MibTableColumn
nncVpl15MinIntervalTaggedInCells = _NncVpl15MinIntervalTaggedInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 2, 1, 8),
    _NncVpl15MinIntervalTaggedInCells_Type()
)
nncVpl15MinIntervalTaggedInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinIntervalTaggedInCells.setStatus("current")
_NncVpl15MinIntervalClp0And1OutCells_Type = NncExtCounter64
_NncVpl15MinIntervalClp0And1OutCells_Object = MibTableColumn
nncVpl15MinIntervalClp0And1OutCells = _NncVpl15MinIntervalClp0And1OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 2, 1, 9),
    _NncVpl15MinIntervalClp0And1OutCells_Type()
)
nncVpl15MinIntervalClp0And1OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinIntervalClp0And1OutCells.setStatus("current")
_NncVpl15MinIntervalClp0OutCells_Type = NncExtCounter64
_NncVpl15MinIntervalClp0OutCells_Object = MibTableColumn
nncVpl15MinIntervalClp0OutCells = _NncVpl15MinIntervalClp0OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 2, 1, 10),
    _NncVpl15MinIntervalClp0OutCells_Type()
)
nncVpl15MinIntervalClp0OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl15MinIntervalClp0OutCells.setStatus("current")
_NncVpl1HourCurrentTable_Object = MibTable
nncVpl1HourCurrentTable = _NncVpl1HourCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 3)
)
if mibBuilder.loadTexts:
    nncVpl1HourCurrentTable.setStatus("current")
_NncVpl1HourCurrentEntry_Object = MibTableRow
nncVpl1HourCurrentEntry = _NncVpl1HourCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 3, 1)
)
nncVpl1HourCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    nncVpl1HourCurrentEntry.setStatus("current")
_NncVpl1HourCurrentState_Type = NncExtIntvlStateType
_NncVpl1HourCurrentState_Object = MibTableColumn
nncVpl1HourCurrentState = _NncVpl1HourCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 3, 1, 1),
    _NncVpl1HourCurrentState_Type()
)
nncVpl1HourCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourCurrentState.setStatus("current")
_NncVpl1HourCurrentAbsoluteIntervalNumber_Type = NncExtAbsIntvlNumberType
_NncVpl1HourCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncVpl1HourCurrentAbsoluteIntervalNumber = _NncVpl1HourCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 3, 1, 2),
    _NncVpl1HourCurrentAbsoluteIntervalNumber_Type()
)
nncVpl1HourCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourCurrentAbsoluteIntervalNumber.setStatus("current")
_NncVpl1HourCurrentClp0And1InCells_Type = NncExtCounter64
_NncVpl1HourCurrentClp0And1InCells_Object = MibTableColumn
nncVpl1HourCurrentClp0And1InCells = _NncVpl1HourCurrentClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 3, 1, 3),
    _NncVpl1HourCurrentClp0And1InCells_Type()
)
nncVpl1HourCurrentClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourCurrentClp0And1InCells.setStatus("current")
_NncVpl1HourCurrentClp0InCells_Type = NncExtCounter64
_NncVpl1HourCurrentClp0InCells_Object = MibTableColumn
nncVpl1HourCurrentClp0InCells = _NncVpl1HourCurrentClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 3, 1, 4),
    _NncVpl1HourCurrentClp0InCells_Type()
)
nncVpl1HourCurrentClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourCurrentClp0InCells.setStatus("current")
_NncVpl1HourCurrentDiscardClp0And1InCells_Type = NncExtCounter64
_NncVpl1HourCurrentDiscardClp0And1InCells_Object = MibTableColumn
nncVpl1HourCurrentDiscardClp0And1InCells = _NncVpl1HourCurrentDiscardClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 3, 1, 5),
    _NncVpl1HourCurrentDiscardClp0And1InCells_Type()
)
nncVpl1HourCurrentDiscardClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourCurrentDiscardClp0And1InCells.setStatus("current")
_NncVpl1HourCurrentDiscardClp0InCells_Type = NncExtCounter64
_NncVpl1HourCurrentDiscardClp0InCells_Object = MibTableColumn
nncVpl1HourCurrentDiscardClp0InCells = _NncVpl1HourCurrentDiscardClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 3, 1, 6),
    _NncVpl1HourCurrentDiscardClp0InCells_Type()
)
nncVpl1HourCurrentDiscardClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourCurrentDiscardClp0InCells.setStatus("current")
_NncVpl1HourCurrentTaggedInCells_Type = NncExtCounter64
_NncVpl1HourCurrentTaggedInCells_Object = MibTableColumn
nncVpl1HourCurrentTaggedInCells = _NncVpl1HourCurrentTaggedInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 3, 1, 7),
    _NncVpl1HourCurrentTaggedInCells_Type()
)
nncVpl1HourCurrentTaggedInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourCurrentTaggedInCells.setStatus("current")
_NncVpl1HourCurrentClp0And1OutCells_Type = NncExtCounter64
_NncVpl1HourCurrentClp0And1OutCells_Object = MibTableColumn
nncVpl1HourCurrentClp0And1OutCells = _NncVpl1HourCurrentClp0And1OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 3, 1, 8),
    _NncVpl1HourCurrentClp0And1OutCells_Type()
)
nncVpl1HourCurrentClp0And1OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourCurrentClp0And1OutCells.setStatus("current")
_NncVpl1HourCurrentClp0OutCells_Type = NncExtCounter64
_NncVpl1HourCurrentClp0OutCells_Object = MibTableColumn
nncVpl1HourCurrentClp0OutCells = _NncVpl1HourCurrentClp0OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 3, 1, 9),
    _NncVpl1HourCurrentClp0OutCells_Type()
)
nncVpl1HourCurrentClp0OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourCurrentClp0OutCells.setStatus("current")
_NncVpl1HourCurrentRowStatus_Type = RowStatus
_NncVpl1HourCurrentRowStatus_Object = MibTableColumn
nncVpl1HourCurrentRowStatus = _NncVpl1HourCurrentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 3, 1, 10),
    _NncVpl1HourCurrentRowStatus_Type()
)
nncVpl1HourCurrentRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncVpl1HourCurrentRowStatus.setStatus("current")
_NncVpl1HourIntervalTable_Object = MibTable
nncVpl1HourIntervalTable = _NncVpl1HourIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 4)
)
if mibBuilder.loadTexts:
    nncVpl1HourIntervalTable.setStatus("current")
_NncVpl1HourIntervalEntry_Object = MibTableRow
nncVpl1HourIntervalEntry = _NncVpl1HourIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 4, 1)
)
nncVpl1HourIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "NNC-ATM-STATISTICS-MIB", "nncVpl1HourIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncVpl1HourIntervalEntry.setStatus("current")
_NncVpl1HourIntervalNumber_Type = NncExtRelIntvlNumberType
_NncVpl1HourIntervalNumber_Object = MibTableColumn
nncVpl1HourIntervalNumber = _NncVpl1HourIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 4, 1, 1),
    _NncVpl1HourIntervalNumber_Type()
)
nncVpl1HourIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncVpl1HourIntervalNumber.setStatus("current")
_NncVpl1HourIntervalState_Type = NncExtIntvlStateType
_NncVpl1HourIntervalState_Object = MibTableColumn
nncVpl1HourIntervalState = _NncVpl1HourIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 4, 1, 2),
    _NncVpl1HourIntervalState_Type()
)
nncVpl1HourIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourIntervalState.setStatus("current")
_NncVpl1HourIntervalAbsoluteIntervalNumber_Type = NncExtAbsIntvlNumberType
_NncVpl1HourIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncVpl1HourIntervalAbsoluteIntervalNumber = _NncVpl1HourIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 4, 1, 3),
    _NncVpl1HourIntervalAbsoluteIntervalNumber_Type()
)
nncVpl1HourIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourIntervalAbsoluteIntervalNumber.setStatus("current")
_NncVpl1HourIntervalClp0And1InCells_Type = NncExtCounter64
_NncVpl1HourIntervalClp0And1InCells_Object = MibTableColumn
nncVpl1HourIntervalClp0And1InCells = _NncVpl1HourIntervalClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 4, 1, 4),
    _NncVpl1HourIntervalClp0And1InCells_Type()
)
nncVpl1HourIntervalClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourIntervalClp0And1InCells.setStatus("current")
_NncVpl1HourIntervalClp0InCells_Type = NncExtCounter64
_NncVpl1HourIntervalClp0InCells_Object = MibTableColumn
nncVpl1HourIntervalClp0InCells = _NncVpl1HourIntervalClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 4, 1, 5),
    _NncVpl1HourIntervalClp0InCells_Type()
)
nncVpl1HourIntervalClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourIntervalClp0InCells.setStatus("current")
_NncVpl1HourIntervalDiscardClp0And1InCells_Type = NncExtCounter64
_NncVpl1HourIntervalDiscardClp0And1InCells_Object = MibTableColumn
nncVpl1HourIntervalDiscardClp0And1InCells = _NncVpl1HourIntervalDiscardClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 4, 1, 6),
    _NncVpl1HourIntervalDiscardClp0And1InCells_Type()
)
nncVpl1HourIntervalDiscardClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourIntervalDiscardClp0And1InCells.setStatus("current")
_NncVpl1HourIntervalDiscardClp0InCells_Type = NncExtCounter64
_NncVpl1HourIntervalDiscardClp0InCells_Object = MibTableColumn
nncVpl1HourIntervalDiscardClp0InCells = _NncVpl1HourIntervalDiscardClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 4, 1, 7),
    _NncVpl1HourIntervalDiscardClp0InCells_Type()
)
nncVpl1HourIntervalDiscardClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourIntervalDiscardClp0InCells.setStatus("current")
_NncVpl1HourIntervalTaggedInCells_Type = NncExtCounter64
_NncVpl1HourIntervalTaggedInCells_Object = MibTableColumn
nncVpl1HourIntervalTaggedInCells = _NncVpl1HourIntervalTaggedInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 4, 1, 8),
    _NncVpl1HourIntervalTaggedInCells_Type()
)
nncVpl1HourIntervalTaggedInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourIntervalTaggedInCells.setStatus("current")
_NncVpl1HourIntervalClp0And1OutCells_Type = NncExtCounter64
_NncVpl1HourIntervalClp0And1OutCells_Object = MibTableColumn
nncVpl1HourIntervalClp0And1OutCells = _NncVpl1HourIntervalClp0And1OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 4, 1, 9),
    _NncVpl1HourIntervalClp0And1OutCells_Type()
)
nncVpl1HourIntervalClp0And1OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourIntervalClp0And1OutCells.setStatus("current")
_NncVpl1HourIntervalClp0OutCells_Type = NncExtCounter64
_NncVpl1HourIntervalClp0OutCells_Object = MibTableColumn
nncVpl1HourIntervalClp0OutCells = _NncVpl1HourIntervalClp0OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 4, 1, 10),
    _NncVpl1HourIntervalClp0OutCells_Type()
)
nncVpl1HourIntervalClp0OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpl1HourIntervalClp0OutCells.setStatus("current")
_NncVcl15MinCurrentTable_Object = MibTable
nncVcl15MinCurrentTable = _NncVcl15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 5)
)
if mibBuilder.loadTexts:
    nncVcl15MinCurrentTable.setStatus("current")
_NncVcl15MinCurrentEntry_Object = MibTableRow
nncVcl15MinCurrentEntry = _NncVcl15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 5, 1)
)
nncVcl15MinCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    nncVcl15MinCurrentEntry.setStatus("current")
_NncVcl15MinCurrentState_Type = NncExtIntvlStateType
_NncVcl15MinCurrentState_Object = MibTableColumn
nncVcl15MinCurrentState = _NncVcl15MinCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 5, 1, 1),
    _NncVcl15MinCurrentState_Type()
)
nncVcl15MinCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinCurrentState.setStatus("current")
_NncVcl15MinCurrentAbsoluteIntervalNumber_Type = NncExtAbsIntvlNumberType
_NncVcl15MinCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncVcl15MinCurrentAbsoluteIntervalNumber = _NncVcl15MinCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 5, 1, 2),
    _NncVcl15MinCurrentAbsoluteIntervalNumber_Type()
)
nncVcl15MinCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinCurrentAbsoluteIntervalNumber.setStatus("current")
_NncVcl15MinCurrentClp0And1InCells_Type = NncExtCounter64
_NncVcl15MinCurrentClp0And1InCells_Object = MibTableColumn
nncVcl15MinCurrentClp0And1InCells = _NncVcl15MinCurrentClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 5, 1, 3),
    _NncVcl15MinCurrentClp0And1InCells_Type()
)
nncVcl15MinCurrentClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinCurrentClp0And1InCells.setStatus("current")
_NncVcl15MinCurrentClp0InCells_Type = NncExtCounter64
_NncVcl15MinCurrentClp0InCells_Object = MibTableColumn
nncVcl15MinCurrentClp0InCells = _NncVcl15MinCurrentClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 5, 1, 4),
    _NncVcl15MinCurrentClp0InCells_Type()
)
nncVcl15MinCurrentClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinCurrentClp0InCells.setStatus("current")
_NncVcl15MinCurrentDiscardClp0And1InCells_Type = NncExtCounter64
_NncVcl15MinCurrentDiscardClp0And1InCells_Object = MibTableColumn
nncVcl15MinCurrentDiscardClp0And1InCells = _NncVcl15MinCurrentDiscardClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 5, 1, 5),
    _NncVcl15MinCurrentDiscardClp0And1InCells_Type()
)
nncVcl15MinCurrentDiscardClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinCurrentDiscardClp0And1InCells.setStatus("current")
_NncVcl15MinCurrentDiscardClp0InCells_Type = NncExtCounter64
_NncVcl15MinCurrentDiscardClp0InCells_Object = MibTableColumn
nncVcl15MinCurrentDiscardClp0InCells = _NncVcl15MinCurrentDiscardClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 5, 1, 6),
    _NncVcl15MinCurrentDiscardClp0InCells_Type()
)
nncVcl15MinCurrentDiscardClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinCurrentDiscardClp0InCells.setStatus("current")
_NncVcl15MinCurrentTaggedInCells_Type = NncExtCounter64
_NncVcl15MinCurrentTaggedInCells_Object = MibTableColumn
nncVcl15MinCurrentTaggedInCells = _NncVcl15MinCurrentTaggedInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 5, 1, 7),
    _NncVcl15MinCurrentTaggedInCells_Type()
)
nncVcl15MinCurrentTaggedInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinCurrentTaggedInCells.setStatus("current")
_NncVcl15MinCurrentClp0And1OutCells_Type = NncExtCounter64
_NncVcl15MinCurrentClp0And1OutCells_Object = MibTableColumn
nncVcl15MinCurrentClp0And1OutCells = _NncVcl15MinCurrentClp0And1OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 5, 1, 8),
    _NncVcl15MinCurrentClp0And1OutCells_Type()
)
nncVcl15MinCurrentClp0And1OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinCurrentClp0And1OutCells.setStatus("current")
_NncVcl15MinCurrentClp0OutCells_Type = NncExtCounter64
_NncVcl15MinCurrentClp0OutCells_Object = MibTableColumn
nncVcl15MinCurrentClp0OutCells = _NncVcl15MinCurrentClp0OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 5, 1, 9),
    _NncVcl15MinCurrentClp0OutCells_Type()
)
nncVcl15MinCurrentClp0OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinCurrentClp0OutCells.setStatus("current")
_NncVcl15MinIntervalTable_Object = MibTable
nncVcl15MinIntervalTable = _NncVcl15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 6)
)
if mibBuilder.loadTexts:
    nncVcl15MinIntervalTable.setStatus("current")
_NncVcl15MinIntervalEntry_Object = MibTableRow
nncVcl15MinIntervalEntry = _NncVcl15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 6, 1)
)
nncVcl15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "NNC-ATM-STATISTICS-MIB", "nncVcl15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncVcl15MinIntervalEntry.setStatus("current")
_NncVcl15MinIntervalNumber_Type = NncExtRelIntvlNumberType
_NncVcl15MinIntervalNumber_Object = MibTableColumn
nncVcl15MinIntervalNumber = _NncVcl15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 6, 1, 1),
    _NncVcl15MinIntervalNumber_Type()
)
nncVcl15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncVcl15MinIntervalNumber.setStatus("current")
_NncVcl15MinIntervalState_Type = NncExtIntvlStateType
_NncVcl15MinIntervalState_Object = MibTableColumn
nncVcl15MinIntervalState = _NncVcl15MinIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 6, 1, 2),
    _NncVcl15MinIntervalState_Type()
)
nncVcl15MinIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinIntervalState.setStatus("current")
_NncVcl15MinIntervalAbsoluteIntervalNumber_Type = NncExtAbsIntvlNumberType
_NncVcl15MinIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncVcl15MinIntervalAbsoluteIntervalNumber = _NncVcl15MinIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 6, 1, 3),
    _NncVcl15MinIntervalAbsoluteIntervalNumber_Type()
)
nncVcl15MinIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinIntervalAbsoluteIntervalNumber.setStatus("current")
_NncVcl15MinIntervalClp0And1InCells_Type = NncExtCounter64
_NncVcl15MinIntervalClp0And1InCells_Object = MibTableColumn
nncVcl15MinIntervalClp0And1InCells = _NncVcl15MinIntervalClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 6, 1, 4),
    _NncVcl15MinIntervalClp0And1InCells_Type()
)
nncVcl15MinIntervalClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinIntervalClp0And1InCells.setStatus("current")
_NncVcl15MinIntervalClp0InCells_Type = NncExtCounter64
_NncVcl15MinIntervalClp0InCells_Object = MibTableColumn
nncVcl15MinIntervalClp0InCells = _NncVcl15MinIntervalClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 6, 1, 5),
    _NncVcl15MinIntervalClp0InCells_Type()
)
nncVcl15MinIntervalClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinIntervalClp0InCells.setStatus("current")
_NncVcl15MinIntervalDiscardClp0And1InCells_Type = NncExtCounter64
_NncVcl15MinIntervalDiscardClp0And1InCells_Object = MibTableColumn
nncVcl15MinIntervalDiscardClp0And1InCells = _NncVcl15MinIntervalDiscardClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 6, 1, 6),
    _NncVcl15MinIntervalDiscardClp0And1InCells_Type()
)
nncVcl15MinIntervalDiscardClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinIntervalDiscardClp0And1InCells.setStatus("current")
_NncVcl15MinIntervalDiscardClp0InCells_Type = NncExtCounter64
_NncVcl15MinIntervalDiscardClp0InCells_Object = MibTableColumn
nncVcl15MinIntervalDiscardClp0InCells = _NncVcl15MinIntervalDiscardClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 6, 1, 7),
    _NncVcl15MinIntervalDiscardClp0InCells_Type()
)
nncVcl15MinIntervalDiscardClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinIntervalDiscardClp0InCells.setStatus("current")
_NncVcl15MinIntervalTaggedInCells_Type = NncExtCounter64
_NncVcl15MinIntervalTaggedInCells_Object = MibTableColumn
nncVcl15MinIntervalTaggedInCells = _NncVcl15MinIntervalTaggedInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 6, 1, 8),
    _NncVcl15MinIntervalTaggedInCells_Type()
)
nncVcl15MinIntervalTaggedInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinIntervalTaggedInCells.setStatus("current")
_NncVcl15MinIntervalClp0And1OutCells_Type = NncExtCounter64
_NncVcl15MinIntervalClp0And1OutCells_Object = MibTableColumn
nncVcl15MinIntervalClp0And1OutCells = _NncVcl15MinIntervalClp0And1OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 6, 1, 9),
    _NncVcl15MinIntervalClp0And1OutCells_Type()
)
nncVcl15MinIntervalClp0And1OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinIntervalClp0And1OutCells.setStatus("current")
_NncVcl15MinIntervalClp0OutCells_Type = NncExtCounter64
_NncVcl15MinIntervalClp0OutCells_Object = MibTableColumn
nncVcl15MinIntervalClp0OutCells = _NncVcl15MinIntervalClp0OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 6, 1, 10),
    _NncVcl15MinIntervalClp0OutCells_Type()
)
nncVcl15MinIntervalClp0OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl15MinIntervalClp0OutCells.setStatus("current")
_NncVcl1HourCurrentTable_Object = MibTable
nncVcl1HourCurrentTable = _NncVcl1HourCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 7)
)
if mibBuilder.loadTexts:
    nncVcl1HourCurrentTable.setStatus("current")
_NncVcl1HourCurrentEntry_Object = MibTableRow
nncVcl1HourCurrentEntry = _NncVcl1HourCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 7, 1)
)
nncVcl1HourCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    nncVcl1HourCurrentEntry.setStatus("current")
_NncVcl1HourCurrentState_Type = NncExtIntvlStateType
_NncVcl1HourCurrentState_Object = MibTableColumn
nncVcl1HourCurrentState = _NncVcl1HourCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 7, 1, 1),
    _NncVcl1HourCurrentState_Type()
)
nncVcl1HourCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourCurrentState.setStatus("current")
_NncVcl1HourCurrentAbsoluteIntervalNumber_Type = NncExtAbsIntvlNumberType
_NncVcl1HourCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncVcl1HourCurrentAbsoluteIntervalNumber = _NncVcl1HourCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 7, 1, 2),
    _NncVcl1HourCurrentAbsoluteIntervalNumber_Type()
)
nncVcl1HourCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourCurrentAbsoluteIntervalNumber.setStatus("current")
_NncVcl1HourCurrentClp0And1InCells_Type = NncExtCounter64
_NncVcl1HourCurrentClp0And1InCells_Object = MibTableColumn
nncVcl1HourCurrentClp0And1InCells = _NncVcl1HourCurrentClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 7, 1, 3),
    _NncVcl1HourCurrentClp0And1InCells_Type()
)
nncVcl1HourCurrentClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourCurrentClp0And1InCells.setStatus("current")
_NncVcl1HourCurrentClp0InCells_Type = NncExtCounter64
_NncVcl1HourCurrentClp0InCells_Object = MibTableColumn
nncVcl1HourCurrentClp0InCells = _NncVcl1HourCurrentClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 7, 1, 4),
    _NncVcl1HourCurrentClp0InCells_Type()
)
nncVcl1HourCurrentClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourCurrentClp0InCells.setStatus("current")
_NncVcl1HourCurrentDiscardClp0And1InCells_Type = NncExtCounter64
_NncVcl1HourCurrentDiscardClp0And1InCells_Object = MibTableColumn
nncVcl1HourCurrentDiscardClp0And1InCells = _NncVcl1HourCurrentDiscardClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 7, 1, 5),
    _NncVcl1HourCurrentDiscardClp0And1InCells_Type()
)
nncVcl1HourCurrentDiscardClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourCurrentDiscardClp0And1InCells.setStatus("current")
_NncVcl1HourCurrentDiscardClp0InCells_Type = NncExtCounter64
_NncVcl1HourCurrentDiscardClp0InCells_Object = MibTableColumn
nncVcl1HourCurrentDiscardClp0InCells = _NncVcl1HourCurrentDiscardClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 7, 1, 6),
    _NncVcl1HourCurrentDiscardClp0InCells_Type()
)
nncVcl1HourCurrentDiscardClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourCurrentDiscardClp0InCells.setStatus("current")
_NncVcl1HourCurrentTaggedInCells_Type = NncExtCounter64
_NncVcl1HourCurrentTaggedInCells_Object = MibTableColumn
nncVcl1HourCurrentTaggedInCells = _NncVcl1HourCurrentTaggedInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 7, 1, 7),
    _NncVcl1HourCurrentTaggedInCells_Type()
)
nncVcl1HourCurrentTaggedInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourCurrentTaggedInCells.setStatus("current")
_NncVcl1HourCurrentClp0And1OutCells_Type = NncExtCounter64
_NncVcl1HourCurrentClp0And1OutCells_Object = MibTableColumn
nncVcl1HourCurrentClp0And1OutCells = _NncVcl1HourCurrentClp0And1OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 7, 1, 8),
    _NncVcl1HourCurrentClp0And1OutCells_Type()
)
nncVcl1HourCurrentClp0And1OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourCurrentClp0And1OutCells.setStatus("current")
_NncVcl1HourCurrentClp0OutCells_Type = NncExtCounter64
_NncVcl1HourCurrentClp0OutCells_Object = MibTableColumn
nncVcl1HourCurrentClp0OutCells = _NncVcl1HourCurrentClp0OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 7, 1, 9),
    _NncVcl1HourCurrentClp0OutCells_Type()
)
nncVcl1HourCurrentClp0OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourCurrentClp0OutCells.setStatus("current")
_NncVcl1HourCurrentRowStatus_Type = RowStatus
_NncVcl1HourCurrentRowStatus_Object = MibTableColumn
nncVcl1HourCurrentRowStatus = _NncVcl1HourCurrentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 7, 1, 10),
    _NncVcl1HourCurrentRowStatus_Type()
)
nncVcl1HourCurrentRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncVcl1HourCurrentRowStatus.setStatus("current")
_NncVcl1HourIntervalTable_Object = MibTable
nncVcl1HourIntervalTable = _NncVcl1HourIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 8)
)
if mibBuilder.loadTexts:
    nncVcl1HourIntervalTable.setStatus("current")
_NncVcl1HourIntervalEntry_Object = MibTableRow
nncVcl1HourIntervalEntry = _NncVcl1HourIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 8, 1)
)
nncVcl1HourIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "NNC-ATM-STATISTICS-MIB", "nncVcl1HourIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncVcl1HourIntervalEntry.setStatus("current")
_NncVcl1HourIntervalNumber_Type = NncExtRelIntvlNumberType
_NncVcl1HourIntervalNumber_Object = MibTableColumn
nncVcl1HourIntervalNumber = _NncVcl1HourIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 8, 1, 1),
    _NncVcl1HourIntervalNumber_Type()
)
nncVcl1HourIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncVcl1HourIntervalNumber.setStatus("current")
_NncVcl1HourIntervalState_Type = NncExtIntvlStateType
_NncVcl1HourIntervalState_Object = MibTableColumn
nncVcl1HourIntervalState = _NncVcl1HourIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 8, 1, 2),
    _NncVcl1HourIntervalState_Type()
)
nncVcl1HourIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourIntervalState.setStatus("current")
_NncVcl1HourIntervalAbsoluteIntervalNumber_Type = NncExtAbsIntvlNumberType
_NncVcl1HourIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncVcl1HourIntervalAbsoluteIntervalNumber = _NncVcl1HourIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 8, 1, 3),
    _NncVcl1HourIntervalAbsoluteIntervalNumber_Type()
)
nncVcl1HourIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourIntervalAbsoluteIntervalNumber.setStatus("current")
_NncVcl1HourIntervalClp0And1InCells_Type = NncExtCounter64
_NncVcl1HourIntervalClp0And1InCells_Object = MibTableColumn
nncVcl1HourIntervalClp0And1InCells = _NncVcl1HourIntervalClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 8, 1, 4),
    _NncVcl1HourIntervalClp0And1InCells_Type()
)
nncVcl1HourIntervalClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourIntervalClp0And1InCells.setStatus("current")
_NncVcl1HourIntervalClp0InCells_Type = NncExtCounter64
_NncVcl1HourIntervalClp0InCells_Object = MibTableColumn
nncVcl1HourIntervalClp0InCells = _NncVcl1HourIntervalClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 8, 1, 5),
    _NncVcl1HourIntervalClp0InCells_Type()
)
nncVcl1HourIntervalClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourIntervalClp0InCells.setStatus("current")
_NncVcl1HourIntervalDiscardClp0And1InCells_Type = NncExtCounter64
_NncVcl1HourIntervalDiscardClp0And1InCells_Object = MibTableColumn
nncVcl1HourIntervalDiscardClp0And1InCells = _NncVcl1HourIntervalDiscardClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 8, 1, 6),
    _NncVcl1HourIntervalDiscardClp0And1InCells_Type()
)
nncVcl1HourIntervalDiscardClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourIntervalDiscardClp0And1InCells.setStatus("current")
_NncVcl1HourIntervalDiscardClp0InCells_Type = NncExtCounter64
_NncVcl1HourIntervalDiscardClp0InCells_Object = MibTableColumn
nncVcl1HourIntervalDiscardClp0InCells = _NncVcl1HourIntervalDiscardClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 8, 1, 7),
    _NncVcl1HourIntervalDiscardClp0InCells_Type()
)
nncVcl1HourIntervalDiscardClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourIntervalDiscardClp0InCells.setStatus("current")
_NncVcl1HourIntervalTaggedInCells_Type = NncExtCounter64
_NncVcl1HourIntervalTaggedInCells_Object = MibTableColumn
nncVcl1HourIntervalTaggedInCells = _NncVcl1HourIntervalTaggedInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 8, 1, 8),
    _NncVcl1HourIntervalTaggedInCells_Type()
)
nncVcl1HourIntervalTaggedInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourIntervalTaggedInCells.setStatus("current")
_NncVcl1HourIntervalClp0And1OutCells_Type = NncExtCounter64
_NncVcl1HourIntervalClp0And1OutCells_Object = MibTableColumn
nncVcl1HourIntervalClp0And1OutCells = _NncVcl1HourIntervalClp0And1OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 8, 1, 9),
    _NncVcl1HourIntervalClp0And1OutCells_Type()
)
nncVcl1HourIntervalClp0And1OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourIntervalClp0And1OutCells.setStatus("current")
_NncVcl1HourIntervalClp0OutCells_Type = NncExtCounter64
_NncVcl1HourIntervalClp0OutCells_Object = MibTableColumn
nncVcl1HourIntervalClp0OutCells = _NncVcl1HourIntervalClp0OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 8, 1, 10),
    _NncVcl1HourIntervalClp0OutCells_Type()
)
nncVcl1HourIntervalClp0OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVcl1HourIntervalClp0OutCells.setStatus("current")
_NncDepthOf15MinHistoricalStrata_Type = NncExtRelIntvlNumberType
_NncDepthOf15MinHistoricalStrata_Object = MibScalar
nncDepthOf15MinHistoricalStrata = _NncDepthOf15MinHistoricalStrata_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 9),
    _NncDepthOf15MinHistoricalStrata_Type()
)
nncDepthOf15MinHistoricalStrata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncDepthOf15MinHistoricalStrata.setStatus("current")
_NncVplStatTable_Object = MibTable
nncVplStatTable = _NncVplStatTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 10)
)
if mibBuilder.loadTexts:
    nncVplStatTable.setStatus("current")
_NncVplStatEntry_Object = MibTableRow
nncVplStatEntry = _NncVplStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 10, 1)
)
nncVplStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    nncVplStatEntry.setStatus("current")
_NncVplStatClp0And1InCells_Type = NncExtCounter64
_NncVplStatClp0And1InCells_Object = MibTableColumn
nncVplStatClp0And1InCells = _NncVplStatClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 10, 1, 1),
    _NncVplStatClp0And1InCells_Type()
)
nncVplStatClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVplStatClp0And1InCells.setStatus("current")
_NncVplStatClp0InCells_Type = NncExtCounter64
_NncVplStatClp0InCells_Object = MibTableColumn
nncVplStatClp0InCells = _NncVplStatClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 10, 1, 2),
    _NncVplStatClp0InCells_Type()
)
nncVplStatClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVplStatClp0InCells.setStatus("current")
_NncVplStatDiscardClp0And1InCells_Type = NncExtCounter64
_NncVplStatDiscardClp0And1InCells_Object = MibTableColumn
nncVplStatDiscardClp0And1InCells = _NncVplStatDiscardClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 10, 1, 3),
    _NncVplStatDiscardClp0And1InCells_Type()
)
nncVplStatDiscardClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVplStatDiscardClp0And1InCells.setStatus("current")
_NncVplStatDiscardClp0InCells_Type = NncExtCounter64
_NncVplStatDiscardClp0InCells_Object = MibTableColumn
nncVplStatDiscardClp0InCells = _NncVplStatDiscardClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 10, 1, 4),
    _NncVplStatDiscardClp0InCells_Type()
)
nncVplStatDiscardClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVplStatDiscardClp0InCells.setStatus("current")
_NncVplStatTaggedInCells_Type = NncExtCounter64
_NncVplStatTaggedInCells_Object = MibTableColumn
nncVplStatTaggedInCells = _NncVplStatTaggedInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 10, 1, 5),
    _NncVplStatTaggedInCells_Type()
)
nncVplStatTaggedInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVplStatTaggedInCells.setStatus("current")
_NncVplStatClp0And1OutCells_Type = NncExtCounter64
_NncVplStatClp0And1OutCells_Object = MibTableColumn
nncVplStatClp0And1OutCells = _NncVplStatClp0And1OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 10, 1, 6),
    _NncVplStatClp0And1OutCells_Type()
)
nncVplStatClp0And1OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVplStatClp0And1OutCells.setStatus("current")
_NncVplStatClp0OutCells_Type = NncExtCounter64
_NncVplStatClp0OutCells_Object = MibTableColumn
nncVplStatClp0OutCells = _NncVplStatClp0OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 10, 1, 7),
    _NncVplStatClp0OutCells_Type()
)
nncVplStatClp0OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVplStatClp0OutCells.setStatus("current")
_NncVclStatTable_Object = MibTable
nncVclStatTable = _NncVclStatTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 11)
)
if mibBuilder.loadTexts:
    nncVclStatTable.setStatus("current")
_NncVclStatEntry_Object = MibTableRow
nncVclStatEntry = _NncVclStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 11, 1)
)
nncVclStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    nncVclStatEntry.setStatus("current")
_NncVclStatClp0And1InCells_Type = NncExtCounter64
_NncVclStatClp0And1InCells_Object = MibTableColumn
nncVclStatClp0And1InCells = _NncVclStatClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 11, 1, 1),
    _NncVclStatClp0And1InCells_Type()
)
nncVclStatClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVclStatClp0And1InCells.setStatus("current")
_NncVclStatClp0InCells_Type = NncExtCounter64
_NncVclStatClp0InCells_Object = MibTableColumn
nncVclStatClp0InCells = _NncVclStatClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 11, 1, 2),
    _NncVclStatClp0InCells_Type()
)
nncVclStatClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVclStatClp0InCells.setStatus("current")
_NncVclStatDiscardClp0And1InCells_Type = NncExtCounter64
_NncVclStatDiscardClp0And1InCells_Object = MibTableColumn
nncVclStatDiscardClp0And1InCells = _NncVclStatDiscardClp0And1InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 11, 1, 3),
    _NncVclStatDiscardClp0And1InCells_Type()
)
nncVclStatDiscardClp0And1InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVclStatDiscardClp0And1InCells.setStatus("current")
_NncVclStatDiscardClp0InCells_Type = NncExtCounter64
_NncVclStatDiscardClp0InCells_Object = MibTableColumn
nncVclStatDiscardClp0InCells = _NncVclStatDiscardClp0InCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 11, 1, 4),
    _NncVclStatDiscardClp0InCells_Type()
)
nncVclStatDiscardClp0InCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVclStatDiscardClp0InCells.setStatus("current")
_NncVclStatTaggedInCells_Type = NncExtCounter64
_NncVclStatTaggedInCells_Object = MibTableColumn
nncVclStatTaggedInCells = _NncVclStatTaggedInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 11, 1, 5),
    _NncVclStatTaggedInCells_Type()
)
nncVclStatTaggedInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVclStatTaggedInCells.setStatus("current")
_NncVclStatClp0And1OutCells_Type = NncExtCounter64
_NncVclStatClp0And1OutCells_Object = MibTableColumn
nncVclStatClp0And1OutCells = _NncVclStatClp0And1OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 11, 1, 6),
    _NncVclStatClp0And1OutCells_Type()
)
nncVclStatClp0And1OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVclStatClp0And1OutCells.setStatus("current")
_NncVclStatClp0OutCells_Type = NncExtCounter64
_NncVclStatClp0OutCells_Object = MibTableColumn
nncVclStatClp0OutCells = _NncVclStatClp0OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 11, 1, 7),
    _NncVclStatClp0OutCells_Type()
)
nncVclStatClp0OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVclStatClp0OutCells.setStatus("current")
_NncAtmVplStatCounterTable_Object = MibTable
nncAtmVplStatCounterTable = _NncAtmVplStatCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 12)
)
if mibBuilder.loadTexts:
    nncAtmVplStatCounterTable.setStatus("current")
_NncAtmVplStatCounterEntry_Object = MibTableRow
nncAtmVplStatCounterEntry = _NncAtmVplStatCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 12, 1)
)
nncAtmVplStatCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "NNC-ATM-STATISTICS-MIB", "nncAtmVplStatCounterIndex"),
)
if mibBuilder.loadTexts:
    nncAtmVplStatCounterEntry.setStatus("current")


class _NncAtmVplStatCounterIndex_Type(Integer32):
    """Custom type nncAtmVplStatCounterIndex based on Integer32"""
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
        *(("daily", 2),
          ("hourly", 1),
          ("interval", 4),
          ("monthly", 3))
    )


_NncAtmVplStatCounterIndex_Type.__name__ = "Integer32"
_NncAtmVplStatCounterIndex_Object = MibTableColumn
nncAtmVplStatCounterIndex = _NncAtmVplStatCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 12, 1, 1),
    _NncAtmVplStatCounterIndex_Type()
)
nncAtmVplStatCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmVplStatCounterIndex.setStatus("current")


class _NncAtmVplStatCounterValue_Type(Integer32):
    """Custom type nncAtmVplStatCounterValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NncAtmVplStatCounterValue_Type.__name__ = "Integer32"
_NncAtmVplStatCounterValue_Object = MibTableColumn
nncAtmVplStatCounterValue = _NncAtmVplStatCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 12, 1, 2),
    _NncAtmVplStatCounterValue_Type()
)
nncAtmVplStatCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmVplStatCounterValue.setStatus("current")
_NncAtmVclStatCounterTable_Object = MibTable
nncAtmVclStatCounterTable = _NncAtmVclStatCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 13)
)
if mibBuilder.loadTexts:
    nncAtmVclStatCounterTable.setStatus("current")
_NncAtmVclStatCounterEntry_Object = MibTableRow
nncAtmVclStatCounterEntry = _NncAtmVclStatCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 13, 1)
)
nncAtmVclStatCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "NNC-ATM-STATISTICS-MIB", "nncAtmVclStatCounterIndex"),
)
if mibBuilder.loadTexts:
    nncAtmVclStatCounterEntry.setStatus("current")


class _NncAtmVclStatCounterIndex_Type(Integer32):
    """Custom type nncAtmVclStatCounterIndex based on Integer32"""
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
        *(("daily", 2),
          ("hourly", 1),
          ("interval", 4),
          ("monthly", 3))
    )


_NncAtmVclStatCounterIndex_Type.__name__ = "Integer32"
_NncAtmVclStatCounterIndex_Object = MibTableColumn
nncAtmVclStatCounterIndex = _NncAtmVclStatCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 13, 1, 1),
    _NncAtmVclStatCounterIndex_Type()
)
nncAtmVclStatCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmVclStatCounterIndex.setStatus("current")


class _NncAtmVclStatCounterValue_Type(Integer32):
    """Custom type nncAtmVclStatCounterValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NncAtmVclStatCounterValue_Type.__name__ = "Integer32"
_NncAtmVclStatCounterValue_Object = MibTableColumn
nncAtmVclStatCounterValue = _NncAtmVclStatCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 13, 1, 2),
    _NncAtmVclStatCounterValue_Type()
)
nncAtmVclStatCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmVclStatCounterValue.setStatus("current")
_NncDepthOf1HourHistoricalStrata_Type = NncExtRelIntvlNumberType
_NncDepthOf1HourHistoricalStrata_Object = MibScalar
nncDepthOf1HourHistoricalStrata = _NncDepthOf1HourHistoricalStrata_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 14),
    _NncDepthOf1HourHistoricalStrata_Type()
)
nncDepthOf1HourHistoricalStrata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncDepthOf1HourHistoricalStrata.setStatus("current")
_NncVpa15MinCurrentTable_Object = MibTable
nncVpa15MinCurrentTable = _NncVpa15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 15)
)
if mibBuilder.loadTexts:
    nncVpa15MinCurrentTable.setStatus("current")
_NncVpa15MinCurrentEntry_Object = MibTableRow
nncVpa15MinCurrentEntry = _NncVpa15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 15, 1)
)
nncVpa15MinCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    nncVpa15MinCurrentEntry.setStatus("current")
_NncVpa15MinCurrentState_Type = NncExtIntvlStateType
_NncVpa15MinCurrentState_Object = MibTableColumn
nncVpa15MinCurrentState = _NncVpa15MinCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 15, 1, 1),
    _NncVpa15MinCurrentState_Type()
)
nncVpa15MinCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa15MinCurrentState.setStatus("current")
_NncVpa15MinCurrentAbsoluteIntervalNumber_Type = Integer32
_NncVpa15MinCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncVpa15MinCurrentAbsoluteIntervalNumber = _NncVpa15MinCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 15, 1, 2),
    _NncVpa15MinCurrentAbsoluteIntervalNumber_Type()
)
nncVpa15MinCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa15MinCurrentAbsoluteIntervalNumber.setStatus("current")
_NncVpa15MinCurrentClp0And1OutCells_Type = Counter64
_NncVpa15MinCurrentClp0And1OutCells_Object = MibTableColumn
nncVpa15MinCurrentClp0And1OutCells = _NncVpa15MinCurrentClp0And1OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 15, 1, 3),
    _NncVpa15MinCurrentClp0And1OutCells_Type()
)
nncVpa15MinCurrentClp0And1OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa15MinCurrentClp0And1OutCells.setStatus("current")
_NncVpa15MinCurrentDiscardClp0And1Cells_Type = Counter64
_NncVpa15MinCurrentDiscardClp0And1Cells_Object = MibTableColumn
nncVpa15MinCurrentDiscardClp0And1Cells = _NncVpa15MinCurrentDiscardClp0And1Cells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 15, 1, 4),
    _NncVpa15MinCurrentDiscardClp0And1Cells_Type()
)
nncVpa15MinCurrentDiscardClp0And1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa15MinCurrentDiscardClp0And1Cells.setStatus("current")
_NncVpa15MinCurrentDiscardClp0Cells_Type = Counter64
_NncVpa15MinCurrentDiscardClp0Cells_Object = MibTableColumn
nncVpa15MinCurrentDiscardClp0Cells = _NncVpa15MinCurrentDiscardClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 15, 1, 6),
    _NncVpa15MinCurrentDiscardClp0Cells_Type()
)
nncVpa15MinCurrentDiscardClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa15MinCurrentDiscardClp0Cells.setStatus("current")
_NncVpa15MinIntervalTable_Object = MibTable
nncVpa15MinIntervalTable = _NncVpa15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 16)
)
if mibBuilder.loadTexts:
    nncVpa15MinIntervalTable.setStatus("current")
_NncVpa15MinIntervalEntry_Object = MibTableRow
nncVpa15MinIntervalEntry = _NncVpa15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 16, 1)
)
nncVpa15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "NNC-ATM-STATISTICS-MIB", "nncVpa15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncVpa15MinIntervalEntry.setStatus("current")
_NncVpa15MinIntervalNumber_Type = Integer32
_NncVpa15MinIntervalNumber_Object = MibTableColumn
nncVpa15MinIntervalNumber = _NncVpa15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 16, 1, 1),
    _NncVpa15MinIntervalNumber_Type()
)
nncVpa15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncVpa15MinIntervalNumber.setStatus("current")
_NncVpa15MinIntervalState_Type = NncExtIntvlStateType
_NncVpa15MinIntervalState_Object = MibTableColumn
nncVpa15MinIntervalState = _NncVpa15MinIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 16, 1, 2),
    _NncVpa15MinIntervalState_Type()
)
nncVpa15MinIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa15MinIntervalState.setStatus("current")
_NncVpa15MinIntervalAbsoluteIntervalNumber_Type = Integer32
_NncVpa15MinIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncVpa15MinIntervalAbsoluteIntervalNumber = _NncVpa15MinIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 16, 1, 3),
    _NncVpa15MinIntervalAbsoluteIntervalNumber_Type()
)
nncVpa15MinIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa15MinIntervalAbsoluteIntervalNumber.setStatus("current")
_NncVpa15MinIntervalClp0And1OutCells_Type = Counter64
_NncVpa15MinIntervalClp0And1OutCells_Object = MibTableColumn
nncVpa15MinIntervalClp0And1OutCells = _NncVpa15MinIntervalClp0And1OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 16, 1, 4),
    _NncVpa15MinIntervalClp0And1OutCells_Type()
)
nncVpa15MinIntervalClp0And1OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa15MinIntervalClp0And1OutCells.setStatus("current")
_NncVpa15MinIntervalDiscardClp0And1Cells_Type = Counter64
_NncVpa15MinIntervalDiscardClp0And1Cells_Object = MibTableColumn
nncVpa15MinIntervalDiscardClp0And1Cells = _NncVpa15MinIntervalDiscardClp0And1Cells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 16, 1, 5),
    _NncVpa15MinIntervalDiscardClp0And1Cells_Type()
)
nncVpa15MinIntervalDiscardClp0And1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa15MinIntervalDiscardClp0And1Cells.setStatus("current")
_NncVpa15MinIntervalDiscardClp0Cells_Type = Counter64
_NncVpa15MinIntervalDiscardClp0Cells_Object = MibTableColumn
nncVpa15MinIntervalDiscardClp0Cells = _NncVpa15MinIntervalDiscardClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 16, 1, 6),
    _NncVpa15MinIntervalDiscardClp0Cells_Type()
)
nncVpa15MinIntervalDiscardClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa15MinIntervalDiscardClp0Cells.setStatus("current")
_NncVpa1HourCurrentTable_Object = MibTable
nncVpa1HourCurrentTable = _NncVpa1HourCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 17)
)
if mibBuilder.loadTexts:
    nncVpa1HourCurrentTable.setStatus("current")
_NncVpa1HourCurrentEntry_Object = MibTableRow
nncVpa1HourCurrentEntry = _NncVpa1HourCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 17, 1)
)
nncVpa1HourCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    nncVpa1HourCurrentEntry.setStatus("current")
_NncVpa1HourCurrentState_Type = NncExtIntvlStateType
_NncVpa1HourCurrentState_Object = MibTableColumn
nncVpa1HourCurrentState = _NncVpa1HourCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 17, 1, 1),
    _NncVpa1HourCurrentState_Type()
)
nncVpa1HourCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa1HourCurrentState.setStatus("current")
_NncVpa1HourCurrentAbsoluteIntervalNumber_Type = Integer32
_NncVpa1HourCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncVpa1HourCurrentAbsoluteIntervalNumber = _NncVpa1HourCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 17, 1, 2),
    _NncVpa1HourCurrentAbsoluteIntervalNumber_Type()
)
nncVpa1HourCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa1HourCurrentAbsoluteIntervalNumber.setStatus("current")
_NncVpa1HourCurrentClp0And1OutCells_Type = Counter64
_NncVpa1HourCurrentClp0And1OutCells_Object = MibTableColumn
nncVpa1HourCurrentClp0And1OutCells = _NncVpa1HourCurrentClp0And1OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 17, 1, 3),
    _NncVpa1HourCurrentClp0And1OutCells_Type()
)
nncVpa1HourCurrentClp0And1OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa1HourCurrentClp0And1OutCells.setStatus("current")
_NncVpa1HourCurrentDiscardClp0And1Cells_Type = Counter64
_NncVpa1HourCurrentDiscardClp0And1Cells_Object = MibTableColumn
nncVpa1HourCurrentDiscardClp0And1Cells = _NncVpa1HourCurrentDiscardClp0And1Cells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 17, 1, 4),
    _NncVpa1HourCurrentDiscardClp0And1Cells_Type()
)
nncVpa1HourCurrentDiscardClp0And1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa1HourCurrentDiscardClp0And1Cells.setStatus("current")
_NncVpa1HourCurrentDiscardClp0Cells_Type = Counter64
_NncVpa1HourCurrentDiscardClp0Cells_Object = MibTableColumn
nncVpa1HourCurrentDiscardClp0Cells = _NncVpa1HourCurrentDiscardClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 17, 1, 5),
    _NncVpa1HourCurrentDiscardClp0Cells_Type()
)
nncVpa1HourCurrentDiscardClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa1HourCurrentDiscardClp0Cells.setStatus("current")
_NncVpa1HourIntervalTable_Object = MibTable
nncVpa1HourIntervalTable = _NncVpa1HourIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 18)
)
if mibBuilder.loadTexts:
    nncVpa1HourIntervalTable.setStatus("current")
_NncVpa1HourIntervalEntry_Object = MibTableRow
nncVpa1HourIntervalEntry = _NncVpa1HourIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 18, 1)
)
nncVpa1HourIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "NNC-ATM-STATISTICS-MIB", "nncVpa1HourIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncVpa1HourIntervalEntry.setStatus("current")
_NncVpa1HourIntervalNumber_Type = Integer32
_NncVpa1HourIntervalNumber_Object = MibTableColumn
nncVpa1HourIntervalNumber = _NncVpa1HourIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 18, 1, 1),
    _NncVpa1HourIntervalNumber_Type()
)
nncVpa1HourIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncVpa1HourIntervalNumber.setStatus("current")
_NncVpa1HourIntervalState_Type = NncExtIntvlStateType
_NncVpa1HourIntervalState_Object = MibTableColumn
nncVpa1HourIntervalState = _NncVpa1HourIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 18, 1, 2),
    _NncVpa1HourIntervalState_Type()
)
nncVpa1HourIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa1HourIntervalState.setStatus("current")
_NncVpa1HourIntervalAbsoluteIntervalNumber_Type = Integer32
_NncVpa1HourIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncVpa1HourIntervalAbsoluteIntervalNumber = _NncVpa1HourIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 18, 1, 3),
    _NncVpa1HourIntervalAbsoluteIntervalNumber_Type()
)
nncVpa1HourIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa1HourIntervalAbsoluteIntervalNumber.setStatus("current")
_NncVpa1HourIntervalClp0And1OutCells_Type = Counter64
_NncVpa1HourIntervalClp0And1OutCells_Object = MibTableColumn
nncVpa1HourIntervalClp0And1OutCells = _NncVpa1HourIntervalClp0And1OutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 18, 1, 4),
    _NncVpa1HourIntervalClp0And1OutCells_Type()
)
nncVpa1HourIntervalClp0And1OutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa1HourIntervalClp0And1OutCells.setStatus("current")
_NncVpa1HourIntervalDiscardClp0And1Cells_Type = Counter64
_NncVpa1HourIntervalDiscardClp0And1Cells_Object = MibTableColumn
nncVpa1HourIntervalDiscardClp0And1Cells = _NncVpa1HourIntervalDiscardClp0And1Cells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 18, 1, 5),
    _NncVpa1HourIntervalDiscardClp0And1Cells_Type()
)
nncVpa1HourIntervalDiscardClp0And1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa1HourIntervalDiscardClp0And1Cells.setStatus("current")
_NncVpa1HourIntervalDiscardClp0Cells_Type = Counter64
_NncVpa1HourIntervalDiscardClp0Cells_Object = MibTableColumn
nncVpa1HourIntervalDiscardClp0Cells = _NncVpa1HourIntervalDiscardClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 1, 18, 1, 6),
    _NncVpa1HourIntervalDiscardClp0Cells_Type()
)
nncVpa1HourIntervalDiscardClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncVpa1HourIntervalDiscardClp0Cells.setStatus("current")
_NncAtmStatisticsTraps_ObjectIdentity = ObjectIdentity
nncAtmStatisticsTraps = _NncAtmStatisticsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 2)
)
_NncAtmStatisticsGroups_ObjectIdentity = ObjectIdentity
nncAtmStatisticsGroups = _NncAtmStatisticsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3)
)
_NncAtmStatisticsCompliances_ObjectIdentity = ObjectIdentity
nncAtmStatisticsCompliances = _NncAtmStatisticsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 4)
)

# Managed Objects groups

nncVpl15MinCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 1)
)
nncVpl15MinCurrentGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVpl15MinCurrentAbsoluteIntervalNumber"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinCurrentClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinCurrentClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinCurrentDiscardClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinCurrentDiscardClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinCurrentTaggedInCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinCurrentClp0And1OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinCurrentClp0OutCells"))
)
if mibBuilder.loadTexts:
    nncVpl15MinCurrentGroup.setStatus("current")

nncVpl15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 2)
)
nncVpl15MinIntervalGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVpl15MinIntervalAbsoluteIntervalNumber"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinIntervalClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinIntervalClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinIntervalDiscardClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinIntervalDiscardClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinIntervalTaggedInCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinIntervalClp0And1OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinIntervalClp0OutCells"))
)
if mibBuilder.loadTexts:
    nncVpl15MinIntervalGroup.setStatus("current")

nncVpl1HourCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 3)
)
nncVpl1HourCurrentGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVpl1HourCurrentAbsoluteIntervalNumber"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourCurrentClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourCurrentClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourCurrentDiscardClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourCurrentDiscardClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourCurrentTaggedInCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourCurrentClp0And1OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourCurrentClp0OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourCurrentRowStatus"))
)
if mibBuilder.loadTexts:
    nncVpl1HourCurrentGroup.setStatus("current")

nncVpl1HourIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 4)
)
nncVpl1HourIntervalGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVpl1HourIntervalAbsoluteIntervalNumber"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourIntervalClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourIntervalClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourIntervalDiscardClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourIntervalDiscardClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourIntervalTaggedInCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourIntervalClp0And1OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourIntervalClp0OutCells"))
)
if mibBuilder.loadTexts:
    nncVpl1HourIntervalGroup.setStatus("current")

nncVcl15MinCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 5)
)
nncVcl15MinCurrentGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVcl15MinCurrentState"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinCurrentAbsoluteIntervalNumber"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinCurrentClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinCurrentClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinCurrentDiscardClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinCurrentDiscardClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinCurrentTaggedInCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinCurrentClp0And1OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinCurrentClp0OutCells"))
)
if mibBuilder.loadTexts:
    nncVcl15MinCurrentGroup.setStatus("current")

nncVcl15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 6)
)
nncVcl15MinIntervalGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVcl15MinIntervalAbsoluteIntervalNumber"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinIntervalClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinIntervalClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinIntervalDiscardClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinIntervalDiscardClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinIntervalTaggedInCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinIntervalClp0And1OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinIntervalClp0OutCells"))
)
if mibBuilder.loadTexts:
    nncVcl15MinIntervalGroup.setStatus("current")

nncVcl1HourCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 7)
)
nncVcl1HourCurrentGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVcl1HourCurrentState"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourCurrentAbsoluteIntervalNumber"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourCurrentClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourCurrentClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourCurrentDiscardClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourCurrentDiscardClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourCurrentTaggedInCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourCurrentClp0And1OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourCurrentClp0OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourCurrentRowStatus"))
)
if mibBuilder.loadTexts:
    nncVcl1HourCurrentGroup.setStatus("current")

nncVcl1HourIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 8)
)
nncVcl1HourIntervalGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVcl1HourIntervalAbsoluteIntervalNumber"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourIntervalClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourIntervalClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourIntervalDiscardClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourIntervalDiscardClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourIntervalTaggedInCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourIntervalClp0And1OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourIntervalClp0OutCells"))
)
if mibBuilder.loadTexts:
    nncVcl1HourIntervalGroup.setStatus("current")

nncVplStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 9)
)
nncVplStatGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVplStatClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVplStatClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVplStatDiscardClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVplStatDiscardClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVplStatTaggedInCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVplStatClp0And1OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVplStatClp0OutCells"))
)
if mibBuilder.loadTexts:
    nncVplStatGroup.setStatus("current")

nncVclStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 10)
)
nncVclStatGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVclStatClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVclStatClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVclStatDiscardClp0And1InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVclStatDiscardClp0InCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVclStatTaggedInCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVclStatClp0And1OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVclStatClp0OutCells"))
)
if mibBuilder.loadTexts:
    nncVclStatGroup.setStatus("current")

nncVplIntervalStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 11)
)
nncVplIntervalStateGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVpl15MinCurrentState"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl15MinIntervalState"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourCurrentState"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpl1HourIntervalState"))
)
if mibBuilder.loadTexts:
    nncVplIntervalStateGroup.setStatus("current")

nncVclIntervalStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 12)
)
nncVclIntervalStateGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVcl15MinCurrentState"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl15MinIntervalState"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourCurrentState"),
        ("NNC-ATM-STATISTICS-MIB", "nncVcl1HourIntervalState"))
)
if mibBuilder.loadTexts:
    nncVclIntervalStateGroup.setStatus("current")

nncVplStatCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 13)
)
nncVplStatCounterGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncAtmVplStatCounterIndex"),
        ("NNC-ATM-STATISTICS-MIB", "nncAtmVplStatCounterValue"))
)
if mibBuilder.loadTexts:
    nncVplStatCounterGroup.setStatus("current")

nncVclStatCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 14)
)
nncVclStatCounterGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncAtmVclStatCounterIndex"),
        ("NNC-ATM-STATISTICS-MIB", "nncAtmVclStatCounterValue"))
)
if mibBuilder.loadTexts:
    nncVclStatCounterGroup.setStatus("current")

nncDepthOfHistoricalStrataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 15)
)
nncDepthOfHistoricalStrataGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncDepthOf15MinHistoricalStrata"),
        ("NNC-ATM-STATISTICS-MIB", "nncDepthOf1HourHistoricalStrata"))
)
if mibBuilder.loadTexts:
    nncDepthOfHistoricalStrataGroup.setStatus("current")

nncVpa15MinCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 16)
)
nncVpa15MinCurrentGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVpa15MinCurrentState"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa15MinCurrentAbsoluteIntervalNumber"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa15MinCurrentClp0And1OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa15MinCurrentDiscardClp0And1Cells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa15MinCurrentDiscardClp0Cells"))
)
if mibBuilder.loadTexts:
    nncVpa15MinCurrentGroup.setStatus("current")

nncVpa15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 17)
)
nncVpa15MinIntervalGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVpa15MinIntervalNumber"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa15MinIntervalState"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa15MinIntervalAbsoluteIntervalNumber"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa15MinIntervalClp0And1OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa15MinIntervalDiscardClp0And1Cells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa15MinIntervalDiscardClp0Cells"))
)
if mibBuilder.loadTexts:
    nncVpa15MinIntervalGroup.setStatus("current")

nncVpa1HourCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 18)
)
nncVpa1HourCurrentGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVpa1HourCurrentState"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa1HourCurrentAbsoluteIntervalNumber"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa1HourCurrentClp0And1OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa1HourCurrentDiscardClp0And1Cells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa1HourCurrentDiscardClp0Cells"))
)
if mibBuilder.loadTexts:
    nncVpa1HourCurrentGroup.setStatus("current")

nncVpa1HourIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 3, 19)
)
nncVpa1HourIntervalGroup.setObjects(
      *(("NNC-ATM-STATISTICS-MIB", "nncVpa1HourIntervalNumber"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa1HourIntervalState"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa1HourIntervalAbsoluteIntervalNumber"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa1HourIntervalClp0And1OutCells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa1HourIntervalDiscardClp0And1Cells"),
        ("NNC-ATM-STATISTICS-MIB", "nncVpa1HourIntervalDiscardClp0Cells"))
)
if mibBuilder.loadTexts:
    nncVpa1HourIntervalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncAtmStatisticsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 4, 1)
)
if mibBuilder.loadTexts:
    nncAtmStatisticsCompliance.setStatus(
        "current"
    )

nncAtmStatisticsServiceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 29, 4, 2)
)
if mibBuilder.loadTexts:
    nncAtmStatisticsServiceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNC-ATM-STATISTICS-MIB",
    **{"nncAtmStatistics": nncAtmStatistics,
       "nncAtmStatisticsObjects": nncAtmStatisticsObjects,
       "nncVpl15MinCurrentTable": nncVpl15MinCurrentTable,
       "nncVpl15MinCurrentEntry": nncVpl15MinCurrentEntry,
       "nncVpl15MinCurrentState": nncVpl15MinCurrentState,
       "nncVpl15MinCurrentAbsoluteIntervalNumber": nncVpl15MinCurrentAbsoluteIntervalNumber,
       "nncVpl15MinCurrentClp0And1InCells": nncVpl15MinCurrentClp0And1InCells,
       "nncVpl15MinCurrentClp0InCells": nncVpl15MinCurrentClp0InCells,
       "nncVpl15MinCurrentDiscardClp0And1InCells": nncVpl15MinCurrentDiscardClp0And1InCells,
       "nncVpl15MinCurrentDiscardClp0InCells": nncVpl15MinCurrentDiscardClp0InCells,
       "nncVpl15MinCurrentTaggedInCells": nncVpl15MinCurrentTaggedInCells,
       "nncVpl15MinCurrentClp0And1OutCells": nncVpl15MinCurrentClp0And1OutCells,
       "nncVpl15MinCurrentClp0OutCells": nncVpl15MinCurrentClp0OutCells,
       "nncVpl15MinIntervalTable": nncVpl15MinIntervalTable,
       "nncVpl15MinIntervalEntry": nncVpl15MinIntervalEntry,
       "nncVpl15MinIntervalNumber": nncVpl15MinIntervalNumber,
       "nncVpl15MinIntervalState": nncVpl15MinIntervalState,
       "nncVpl15MinIntervalAbsoluteIntervalNumber": nncVpl15MinIntervalAbsoluteIntervalNumber,
       "nncVpl15MinIntervalClp0And1InCells": nncVpl15MinIntervalClp0And1InCells,
       "nncVpl15MinIntervalClp0InCells": nncVpl15MinIntervalClp0InCells,
       "nncVpl15MinIntervalDiscardClp0And1InCells": nncVpl15MinIntervalDiscardClp0And1InCells,
       "nncVpl15MinIntervalDiscardClp0InCells": nncVpl15MinIntervalDiscardClp0InCells,
       "nncVpl15MinIntervalTaggedInCells": nncVpl15MinIntervalTaggedInCells,
       "nncVpl15MinIntervalClp0And1OutCells": nncVpl15MinIntervalClp0And1OutCells,
       "nncVpl15MinIntervalClp0OutCells": nncVpl15MinIntervalClp0OutCells,
       "nncVpl1HourCurrentTable": nncVpl1HourCurrentTable,
       "nncVpl1HourCurrentEntry": nncVpl1HourCurrentEntry,
       "nncVpl1HourCurrentState": nncVpl1HourCurrentState,
       "nncVpl1HourCurrentAbsoluteIntervalNumber": nncVpl1HourCurrentAbsoluteIntervalNumber,
       "nncVpl1HourCurrentClp0And1InCells": nncVpl1HourCurrentClp0And1InCells,
       "nncVpl1HourCurrentClp0InCells": nncVpl1HourCurrentClp0InCells,
       "nncVpl1HourCurrentDiscardClp0And1InCells": nncVpl1HourCurrentDiscardClp0And1InCells,
       "nncVpl1HourCurrentDiscardClp0InCells": nncVpl1HourCurrentDiscardClp0InCells,
       "nncVpl1HourCurrentTaggedInCells": nncVpl1HourCurrentTaggedInCells,
       "nncVpl1HourCurrentClp0And1OutCells": nncVpl1HourCurrentClp0And1OutCells,
       "nncVpl1HourCurrentClp0OutCells": nncVpl1HourCurrentClp0OutCells,
       "nncVpl1HourCurrentRowStatus": nncVpl1HourCurrentRowStatus,
       "nncVpl1HourIntervalTable": nncVpl1HourIntervalTable,
       "nncVpl1HourIntervalEntry": nncVpl1HourIntervalEntry,
       "nncVpl1HourIntervalNumber": nncVpl1HourIntervalNumber,
       "nncVpl1HourIntervalState": nncVpl1HourIntervalState,
       "nncVpl1HourIntervalAbsoluteIntervalNumber": nncVpl1HourIntervalAbsoluteIntervalNumber,
       "nncVpl1HourIntervalClp0And1InCells": nncVpl1HourIntervalClp0And1InCells,
       "nncVpl1HourIntervalClp0InCells": nncVpl1HourIntervalClp0InCells,
       "nncVpl1HourIntervalDiscardClp0And1InCells": nncVpl1HourIntervalDiscardClp0And1InCells,
       "nncVpl1HourIntervalDiscardClp0InCells": nncVpl1HourIntervalDiscardClp0InCells,
       "nncVpl1HourIntervalTaggedInCells": nncVpl1HourIntervalTaggedInCells,
       "nncVpl1HourIntervalClp0And1OutCells": nncVpl1HourIntervalClp0And1OutCells,
       "nncVpl1HourIntervalClp0OutCells": nncVpl1HourIntervalClp0OutCells,
       "nncVcl15MinCurrentTable": nncVcl15MinCurrentTable,
       "nncVcl15MinCurrentEntry": nncVcl15MinCurrentEntry,
       "nncVcl15MinCurrentState": nncVcl15MinCurrentState,
       "nncVcl15MinCurrentAbsoluteIntervalNumber": nncVcl15MinCurrentAbsoluteIntervalNumber,
       "nncVcl15MinCurrentClp0And1InCells": nncVcl15MinCurrentClp0And1InCells,
       "nncVcl15MinCurrentClp0InCells": nncVcl15MinCurrentClp0InCells,
       "nncVcl15MinCurrentDiscardClp0And1InCells": nncVcl15MinCurrentDiscardClp0And1InCells,
       "nncVcl15MinCurrentDiscardClp0InCells": nncVcl15MinCurrentDiscardClp0InCells,
       "nncVcl15MinCurrentTaggedInCells": nncVcl15MinCurrentTaggedInCells,
       "nncVcl15MinCurrentClp0And1OutCells": nncVcl15MinCurrentClp0And1OutCells,
       "nncVcl15MinCurrentClp0OutCells": nncVcl15MinCurrentClp0OutCells,
       "nncVcl15MinIntervalTable": nncVcl15MinIntervalTable,
       "nncVcl15MinIntervalEntry": nncVcl15MinIntervalEntry,
       "nncVcl15MinIntervalNumber": nncVcl15MinIntervalNumber,
       "nncVcl15MinIntervalState": nncVcl15MinIntervalState,
       "nncVcl15MinIntervalAbsoluteIntervalNumber": nncVcl15MinIntervalAbsoluteIntervalNumber,
       "nncVcl15MinIntervalClp0And1InCells": nncVcl15MinIntervalClp0And1InCells,
       "nncVcl15MinIntervalClp0InCells": nncVcl15MinIntervalClp0InCells,
       "nncVcl15MinIntervalDiscardClp0And1InCells": nncVcl15MinIntervalDiscardClp0And1InCells,
       "nncVcl15MinIntervalDiscardClp0InCells": nncVcl15MinIntervalDiscardClp0InCells,
       "nncVcl15MinIntervalTaggedInCells": nncVcl15MinIntervalTaggedInCells,
       "nncVcl15MinIntervalClp0And1OutCells": nncVcl15MinIntervalClp0And1OutCells,
       "nncVcl15MinIntervalClp0OutCells": nncVcl15MinIntervalClp0OutCells,
       "nncVcl1HourCurrentTable": nncVcl1HourCurrentTable,
       "nncVcl1HourCurrentEntry": nncVcl1HourCurrentEntry,
       "nncVcl1HourCurrentState": nncVcl1HourCurrentState,
       "nncVcl1HourCurrentAbsoluteIntervalNumber": nncVcl1HourCurrentAbsoluteIntervalNumber,
       "nncVcl1HourCurrentClp0And1InCells": nncVcl1HourCurrentClp0And1InCells,
       "nncVcl1HourCurrentClp0InCells": nncVcl1HourCurrentClp0InCells,
       "nncVcl1HourCurrentDiscardClp0And1InCells": nncVcl1HourCurrentDiscardClp0And1InCells,
       "nncVcl1HourCurrentDiscardClp0InCells": nncVcl1HourCurrentDiscardClp0InCells,
       "nncVcl1HourCurrentTaggedInCells": nncVcl1HourCurrentTaggedInCells,
       "nncVcl1HourCurrentClp0And1OutCells": nncVcl1HourCurrentClp0And1OutCells,
       "nncVcl1HourCurrentClp0OutCells": nncVcl1HourCurrentClp0OutCells,
       "nncVcl1HourCurrentRowStatus": nncVcl1HourCurrentRowStatus,
       "nncVcl1HourIntervalTable": nncVcl1HourIntervalTable,
       "nncVcl1HourIntervalEntry": nncVcl1HourIntervalEntry,
       "nncVcl1HourIntervalNumber": nncVcl1HourIntervalNumber,
       "nncVcl1HourIntervalState": nncVcl1HourIntervalState,
       "nncVcl1HourIntervalAbsoluteIntervalNumber": nncVcl1HourIntervalAbsoluteIntervalNumber,
       "nncVcl1HourIntervalClp0And1InCells": nncVcl1HourIntervalClp0And1InCells,
       "nncVcl1HourIntervalClp0InCells": nncVcl1HourIntervalClp0InCells,
       "nncVcl1HourIntervalDiscardClp0And1InCells": nncVcl1HourIntervalDiscardClp0And1InCells,
       "nncVcl1HourIntervalDiscardClp0InCells": nncVcl1HourIntervalDiscardClp0InCells,
       "nncVcl1HourIntervalTaggedInCells": nncVcl1HourIntervalTaggedInCells,
       "nncVcl1HourIntervalClp0And1OutCells": nncVcl1HourIntervalClp0And1OutCells,
       "nncVcl1HourIntervalClp0OutCells": nncVcl1HourIntervalClp0OutCells,
       "nncDepthOf15MinHistoricalStrata": nncDepthOf15MinHistoricalStrata,
       "nncVplStatTable": nncVplStatTable,
       "nncVplStatEntry": nncVplStatEntry,
       "nncVplStatClp0And1InCells": nncVplStatClp0And1InCells,
       "nncVplStatClp0InCells": nncVplStatClp0InCells,
       "nncVplStatDiscardClp0And1InCells": nncVplStatDiscardClp0And1InCells,
       "nncVplStatDiscardClp0InCells": nncVplStatDiscardClp0InCells,
       "nncVplStatTaggedInCells": nncVplStatTaggedInCells,
       "nncVplStatClp0And1OutCells": nncVplStatClp0And1OutCells,
       "nncVplStatClp0OutCells": nncVplStatClp0OutCells,
       "nncVclStatTable": nncVclStatTable,
       "nncVclStatEntry": nncVclStatEntry,
       "nncVclStatClp0And1InCells": nncVclStatClp0And1InCells,
       "nncVclStatClp0InCells": nncVclStatClp0InCells,
       "nncVclStatDiscardClp0And1InCells": nncVclStatDiscardClp0And1InCells,
       "nncVclStatDiscardClp0InCells": nncVclStatDiscardClp0InCells,
       "nncVclStatTaggedInCells": nncVclStatTaggedInCells,
       "nncVclStatClp0And1OutCells": nncVclStatClp0And1OutCells,
       "nncVclStatClp0OutCells": nncVclStatClp0OutCells,
       "nncAtmVplStatCounterTable": nncAtmVplStatCounterTable,
       "nncAtmVplStatCounterEntry": nncAtmVplStatCounterEntry,
       "nncAtmVplStatCounterIndex": nncAtmVplStatCounterIndex,
       "nncAtmVplStatCounterValue": nncAtmVplStatCounterValue,
       "nncAtmVclStatCounterTable": nncAtmVclStatCounterTable,
       "nncAtmVclStatCounterEntry": nncAtmVclStatCounterEntry,
       "nncAtmVclStatCounterIndex": nncAtmVclStatCounterIndex,
       "nncAtmVclStatCounterValue": nncAtmVclStatCounterValue,
       "nncDepthOf1HourHistoricalStrata": nncDepthOf1HourHistoricalStrata,
       "nncVpa15MinCurrentTable": nncVpa15MinCurrentTable,
       "nncVpa15MinCurrentEntry": nncVpa15MinCurrentEntry,
       "nncVpa15MinCurrentState": nncVpa15MinCurrentState,
       "nncVpa15MinCurrentAbsoluteIntervalNumber": nncVpa15MinCurrentAbsoluteIntervalNumber,
       "nncVpa15MinCurrentClp0And1OutCells": nncVpa15MinCurrentClp0And1OutCells,
       "nncVpa15MinCurrentDiscardClp0And1Cells": nncVpa15MinCurrentDiscardClp0And1Cells,
       "nncVpa15MinCurrentDiscardClp0Cells": nncVpa15MinCurrentDiscardClp0Cells,
       "nncVpa15MinIntervalTable": nncVpa15MinIntervalTable,
       "nncVpa15MinIntervalEntry": nncVpa15MinIntervalEntry,
       "nncVpa15MinIntervalNumber": nncVpa15MinIntervalNumber,
       "nncVpa15MinIntervalState": nncVpa15MinIntervalState,
       "nncVpa15MinIntervalAbsoluteIntervalNumber": nncVpa15MinIntervalAbsoluteIntervalNumber,
       "nncVpa15MinIntervalClp0And1OutCells": nncVpa15MinIntervalClp0And1OutCells,
       "nncVpa15MinIntervalDiscardClp0And1Cells": nncVpa15MinIntervalDiscardClp0And1Cells,
       "nncVpa15MinIntervalDiscardClp0Cells": nncVpa15MinIntervalDiscardClp0Cells,
       "nncVpa1HourCurrentTable": nncVpa1HourCurrentTable,
       "nncVpa1HourCurrentEntry": nncVpa1HourCurrentEntry,
       "nncVpa1HourCurrentState": nncVpa1HourCurrentState,
       "nncVpa1HourCurrentAbsoluteIntervalNumber": nncVpa1HourCurrentAbsoluteIntervalNumber,
       "nncVpa1HourCurrentClp0And1OutCells": nncVpa1HourCurrentClp0And1OutCells,
       "nncVpa1HourCurrentDiscardClp0And1Cells": nncVpa1HourCurrentDiscardClp0And1Cells,
       "nncVpa1HourCurrentDiscardClp0Cells": nncVpa1HourCurrentDiscardClp0Cells,
       "nncVpa1HourIntervalTable": nncVpa1HourIntervalTable,
       "nncVpa1HourIntervalEntry": nncVpa1HourIntervalEntry,
       "nncVpa1HourIntervalNumber": nncVpa1HourIntervalNumber,
       "nncVpa1HourIntervalState": nncVpa1HourIntervalState,
       "nncVpa1HourIntervalAbsoluteIntervalNumber": nncVpa1HourIntervalAbsoluteIntervalNumber,
       "nncVpa1HourIntervalClp0And1OutCells": nncVpa1HourIntervalClp0And1OutCells,
       "nncVpa1HourIntervalDiscardClp0And1Cells": nncVpa1HourIntervalDiscardClp0And1Cells,
       "nncVpa1HourIntervalDiscardClp0Cells": nncVpa1HourIntervalDiscardClp0Cells,
       "nncAtmStatisticsTraps": nncAtmStatisticsTraps,
       "nncAtmStatisticsGroups": nncAtmStatisticsGroups,
       "nncVpl15MinCurrentGroup": nncVpl15MinCurrentGroup,
       "nncVpl15MinIntervalGroup": nncVpl15MinIntervalGroup,
       "nncVpl1HourCurrentGroup": nncVpl1HourCurrentGroup,
       "nncVpl1HourIntervalGroup": nncVpl1HourIntervalGroup,
       "nncVcl15MinCurrentGroup": nncVcl15MinCurrentGroup,
       "nncVcl15MinIntervalGroup": nncVcl15MinIntervalGroup,
       "nncVcl1HourCurrentGroup": nncVcl1HourCurrentGroup,
       "nncVcl1HourIntervalGroup": nncVcl1HourIntervalGroup,
       "nncVplStatGroup": nncVplStatGroup,
       "nncVclStatGroup": nncVclStatGroup,
       "nncVplIntervalStateGroup": nncVplIntervalStateGroup,
       "nncVclIntervalStateGroup": nncVclIntervalStateGroup,
       "nncVplStatCounterGroup": nncVplStatCounterGroup,
       "nncVclStatCounterGroup": nncVclStatCounterGroup,
       "nncDepthOfHistoricalStrataGroup": nncDepthOfHistoricalStrataGroup,
       "nncVpa15MinCurrentGroup": nncVpa15MinCurrentGroup,
       "nncVpa15MinIntervalGroup": nncVpa15MinIntervalGroup,
       "nncVpa1HourCurrentGroup": nncVpa1HourCurrentGroup,
       "nncVpa1HourIntervalGroup": nncVpa1HourIntervalGroup,
       "nncAtmStatisticsCompliances": nncAtmStatisticsCompliances,
       "nncAtmStatisticsCompliance": nncAtmStatisticsCompliance,
       "nncAtmStatisticsServiceCompliance": nncAtmStatisticsServiceCompliance}
)
