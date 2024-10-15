# SNMP MIB module (NNC-EXT-PM-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNC-EXT-PM-STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:12 2024
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
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nncExtPmStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 65)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NncExtPmCellFlowDirType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("matrix", 2))
    )



class NncExtPmTestType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("end2end", 2),
          ("segment", 1))
    )



# MIB Managed Objects in the order of their OIDs

_NncExtPmStatisticsObjects_ObjectIdentity = ObjectIdentity
nncExtPmStatisticsObjects = _NncExtPmStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1)
)
_NncExtPm15MinCurrentTable_Object = MibTable
nncExtPm15MinCurrentTable = _NncExtPm15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1)
)
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentTable.setStatus("current")
_NncExtPm15MinCurrentEntry_Object = MibTableRow
nncExtPm15MinCurrentEntry = _NncExtPm15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1)
)
nncExtPm15MinCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentCellFlow"),
    (0, "NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentTest"),
)
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentEntry.setStatus("current")
_NncExtPm15MinCurrentCellFlow_Type = NncExtPmCellFlowDirType
_NncExtPm15MinCurrentCellFlow_Object = MibTableColumn
nncExtPm15MinCurrentCellFlow = _NncExtPm15MinCurrentCellFlow_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 1),
    _NncExtPm15MinCurrentCellFlow_Type()
)
nncExtPm15MinCurrentCellFlow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentCellFlow.setStatus("current")
_NncExtPm15MinCurrentTest_Type = NncExtPmTestType
_NncExtPm15MinCurrentTest_Object = MibTableColumn
nncExtPm15MinCurrentTest = _NncExtPm15MinCurrentTest_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 2),
    _NncExtPm15MinCurrentTest_Type()
)
nncExtPm15MinCurrentTest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentTest.setStatus("current")
_NncExtPm15MinCurrentState_Type = NncExtIntvlStateType
_NncExtPm15MinCurrentState_Object = MibTableColumn
nncExtPm15MinCurrentState = _NncExtPm15MinCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 3),
    _NncExtPm15MinCurrentState_Type()
)
nncExtPm15MinCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentState.setStatus("current")
_NncExtPm15MinCurrentAbsoluteIntervalNumber_Type = NncExtAbsIntvlNumberType
_NncExtPm15MinCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncExtPm15MinCurrentAbsoluteIntervalNumber = _NncExtPm15MinCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 4),
    _NncExtPm15MinCurrentAbsoluteIntervalNumber_Type()
)
nncExtPm15MinCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentAbsoluteIntervalNumber.setStatus("current")
_NncExtPm15MinCurrentSECBs_Type = NncExtCounter64
_NncExtPm15MinCurrentSECBs_Object = MibTableColumn
nncExtPm15MinCurrentSECBs = _NncExtPm15MinCurrentSECBs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 5),
    _NncExtPm15MinCurrentSECBs_Type()
)
nncExtPm15MinCurrentSECBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentSECBs.setStatus("current")
_NncExtPm15MinCurrentLostCellsClp0And1_Type = NncExtCounter64
_NncExtPm15MinCurrentLostCellsClp0And1_Object = MibTableColumn
nncExtPm15MinCurrentLostCellsClp0And1 = _NncExtPm15MinCurrentLostCellsClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 6),
    _NncExtPm15MinCurrentLostCellsClp0And1_Type()
)
nncExtPm15MinCurrentLostCellsClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentLostCellsClp0And1.setStatus("current")
_NncExtPm15MinCurrentLostCellsClp0_Type = NncExtCounter64
_NncExtPm15MinCurrentLostCellsClp0_Object = MibTableColumn
nncExtPm15MinCurrentLostCellsClp0 = _NncExtPm15MinCurrentLostCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 7),
    _NncExtPm15MinCurrentLostCellsClp0_Type()
)
nncExtPm15MinCurrentLostCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentLostCellsClp0.setStatus("current")
_NncExtPm15MinCurrentMisinsertedCells_Type = NncExtCounter64
_NncExtPm15MinCurrentMisinsertedCells_Object = MibTableColumn
nncExtPm15MinCurrentMisinsertedCells = _NncExtPm15MinCurrentMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 8),
    _NncExtPm15MinCurrentMisinsertedCells_Type()
)
nncExtPm15MinCurrentMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentMisinsertedCells.setStatus("current")
_NncExtPm15MinCurrentCellsClp0And1_Type = NncExtCounter64
_NncExtPm15MinCurrentCellsClp0And1_Object = MibTableColumn
nncExtPm15MinCurrentCellsClp0And1 = _NncExtPm15MinCurrentCellsClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 9),
    _NncExtPm15MinCurrentCellsClp0And1_Type()
)
nncExtPm15MinCurrentCellsClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentCellsClp0And1.setStatus("current")
_NncExtPm15MinCurrentCellsClp0_Type = NncExtCounter64
_NncExtPm15MinCurrentCellsClp0_Object = MibTableColumn
nncExtPm15MinCurrentCellsClp0 = _NncExtPm15MinCurrentCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 10),
    _NncExtPm15MinCurrentCellsClp0_Type()
)
nncExtPm15MinCurrentCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentCellsClp0.setStatus("current")
_NncExtPm15MinCurrentImpairedBlocks_Type = NncExtCounter64
_NncExtPm15MinCurrentImpairedBlocks_Object = MibTableColumn
nncExtPm15MinCurrentImpairedBlocks = _NncExtPm15MinCurrentImpairedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 11),
    _NncExtPm15MinCurrentImpairedBlocks_Type()
)
nncExtPm15MinCurrentImpairedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentImpairedBlocks.setStatus("current")
_NncExtPm15MinCurrentTotalLostCellsClp0And1_Type = NncExtCounter64
_NncExtPm15MinCurrentTotalLostCellsClp0And1_Object = MibTableColumn
nncExtPm15MinCurrentTotalLostCellsClp0And1 = _NncExtPm15MinCurrentTotalLostCellsClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 12),
    _NncExtPm15MinCurrentTotalLostCellsClp0And1_Type()
)
nncExtPm15MinCurrentTotalLostCellsClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentTotalLostCellsClp0And1.setStatus("current")
_NncExtPm15MinCurrentTotalLostCellsClp0_Type = NncExtCounter64
_NncExtPm15MinCurrentTotalLostCellsClp0_Object = MibTableColumn
nncExtPm15MinCurrentTotalLostCellsClp0 = _NncExtPm15MinCurrentTotalLostCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 13),
    _NncExtPm15MinCurrentTotalLostCellsClp0_Type()
)
nncExtPm15MinCurrentTotalLostCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentTotalLostCellsClp0.setStatus("current")
_NncExtPm15MinCurrentIBWithCellLossMisinsert_Type = NncExtCounter64
_NncExtPm15MinCurrentIBWithCellLossMisinsert_Object = MibTableColumn
nncExtPm15MinCurrentIBWithCellLossMisinsert = _NncExtPm15MinCurrentIBWithCellLossMisinsert_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 14),
    _NncExtPm15MinCurrentIBWithCellLossMisinsert_Type()
)
nncExtPm15MinCurrentIBWithCellLossMisinsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentIBWithCellLossMisinsert.setStatus("current")
_NncExtPm15MinCurrentCellLossRatioClp0And1_Type = NncExtCounter64
_NncExtPm15MinCurrentCellLossRatioClp0And1_Object = MibTableColumn
nncExtPm15MinCurrentCellLossRatioClp0And1 = _NncExtPm15MinCurrentCellLossRatioClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 15),
    _NncExtPm15MinCurrentCellLossRatioClp0And1_Type()
)
nncExtPm15MinCurrentCellLossRatioClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentCellLossRatioClp0And1.setStatus("current")
_NncExtPm15MinCurrentCellLossRatioClp0_Type = NncExtCounter64
_NncExtPm15MinCurrentCellLossRatioClp0_Object = MibTableColumn
nncExtPm15MinCurrentCellLossRatioClp0 = _NncExtPm15MinCurrentCellLossRatioClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 1, 1, 16),
    _NncExtPm15MinCurrentCellLossRatioClp0_Type()
)
nncExtPm15MinCurrentCellLossRatioClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentCellLossRatioClp0.setStatus("current")
_NncExtPm15MinIntervalTable_Object = MibTable
nncExtPm15MinIntervalTable = _NncExtPm15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2)
)
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalTable.setStatus("current")
_NncExtPm15MinIntervalEntry_Object = MibTableRow
nncExtPm15MinIntervalEntry = _NncExtPm15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1)
)
nncExtPm15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalCellFlow"),
    (0, "NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalTest"),
    (0, "NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalEntry.setStatus("current")
_NncExtPm15MinIntervalCellFlow_Type = NncExtPmCellFlowDirType
_NncExtPm15MinIntervalCellFlow_Object = MibTableColumn
nncExtPm15MinIntervalCellFlow = _NncExtPm15MinIntervalCellFlow_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 1),
    _NncExtPm15MinIntervalCellFlow_Type()
)
nncExtPm15MinIntervalCellFlow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalCellFlow.setStatus("current")
_NncExtPm15MinIntervalTest_Type = NncExtPmTestType
_NncExtPm15MinIntervalTest_Object = MibTableColumn
nncExtPm15MinIntervalTest = _NncExtPm15MinIntervalTest_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 2),
    _NncExtPm15MinIntervalTest_Type()
)
nncExtPm15MinIntervalTest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalTest.setStatus("current")
_NncExtPm15MinIntervalNumber_Type = NncExtRelIntvlNumberType
_NncExtPm15MinIntervalNumber_Object = MibTableColumn
nncExtPm15MinIntervalNumber = _NncExtPm15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 3),
    _NncExtPm15MinIntervalNumber_Type()
)
nncExtPm15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalNumber.setStatus("current")
_NncExtPm15MinIntervalState_Type = NncExtIntvlStateType
_NncExtPm15MinIntervalState_Object = MibTableColumn
nncExtPm15MinIntervalState = _NncExtPm15MinIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 4),
    _NncExtPm15MinIntervalState_Type()
)
nncExtPm15MinIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalState.setStatus("current")
_NncExtPm15MinIntervalAbsoluteIntervalNumber_Type = NncExtAbsIntvlNumberType
_NncExtPm15MinIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncExtPm15MinIntervalAbsoluteIntervalNumber = _NncExtPm15MinIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 5),
    _NncExtPm15MinIntervalAbsoluteIntervalNumber_Type()
)
nncExtPm15MinIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalAbsoluteIntervalNumber.setStatus("current")
_NncExtPm15MinIntervalSECBs_Type = NncExtCounter64
_NncExtPm15MinIntervalSECBs_Object = MibTableColumn
nncExtPm15MinIntervalSECBs = _NncExtPm15MinIntervalSECBs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 6),
    _NncExtPm15MinIntervalSECBs_Type()
)
nncExtPm15MinIntervalSECBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalSECBs.setStatus("current")
_NncExtPm15MinIntervalLostCellsClp0And1_Type = NncExtCounter64
_NncExtPm15MinIntervalLostCellsClp0And1_Object = MibTableColumn
nncExtPm15MinIntervalLostCellsClp0And1 = _NncExtPm15MinIntervalLostCellsClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 7),
    _NncExtPm15MinIntervalLostCellsClp0And1_Type()
)
nncExtPm15MinIntervalLostCellsClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalLostCellsClp0And1.setStatus("current")
_NncExtPm15MinIntervalLostCellsClp0_Type = NncExtCounter64
_NncExtPm15MinIntervalLostCellsClp0_Object = MibTableColumn
nncExtPm15MinIntervalLostCellsClp0 = _NncExtPm15MinIntervalLostCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 8),
    _NncExtPm15MinIntervalLostCellsClp0_Type()
)
nncExtPm15MinIntervalLostCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalLostCellsClp0.setStatus("current")
_NncExtPm15MinIntervalMisinsertedCells_Type = NncExtCounter64
_NncExtPm15MinIntervalMisinsertedCells_Object = MibTableColumn
nncExtPm15MinIntervalMisinsertedCells = _NncExtPm15MinIntervalMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 9),
    _NncExtPm15MinIntervalMisinsertedCells_Type()
)
nncExtPm15MinIntervalMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalMisinsertedCells.setStatus("current")
_NncExtPm15MinIntervalCellsClp0And1_Type = NncExtCounter64
_NncExtPm15MinIntervalCellsClp0And1_Object = MibTableColumn
nncExtPm15MinIntervalCellsClp0And1 = _NncExtPm15MinIntervalCellsClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 10),
    _NncExtPm15MinIntervalCellsClp0And1_Type()
)
nncExtPm15MinIntervalCellsClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalCellsClp0And1.setStatus("current")
_NncExtPm15MinIntervalCellsClp0_Type = NncExtCounter64
_NncExtPm15MinIntervalCellsClp0_Object = MibTableColumn
nncExtPm15MinIntervalCellsClp0 = _NncExtPm15MinIntervalCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 11),
    _NncExtPm15MinIntervalCellsClp0_Type()
)
nncExtPm15MinIntervalCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalCellsClp0.setStatus("current")
_NncExtPm15MinIntervalImpairedBlocks_Type = NncExtCounter64
_NncExtPm15MinIntervalImpairedBlocks_Object = MibTableColumn
nncExtPm15MinIntervalImpairedBlocks = _NncExtPm15MinIntervalImpairedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 12),
    _NncExtPm15MinIntervalImpairedBlocks_Type()
)
nncExtPm15MinIntervalImpairedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalImpairedBlocks.setStatus("current")
_NncExtPm15MinIntervalTotalLostCellsClp0And1_Type = NncExtCounter64
_NncExtPm15MinIntervalTotalLostCellsClp0And1_Object = MibTableColumn
nncExtPm15MinIntervalTotalLostCellsClp0And1 = _NncExtPm15MinIntervalTotalLostCellsClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 13),
    _NncExtPm15MinIntervalTotalLostCellsClp0And1_Type()
)
nncExtPm15MinIntervalTotalLostCellsClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalTotalLostCellsClp0And1.setStatus("current")
_NncExtPm15MinIntervalTotalLostCellsClp0_Type = NncExtCounter64
_NncExtPm15MinIntervalTotalLostCellsClp0_Object = MibTableColumn
nncExtPm15MinIntervalTotalLostCellsClp0 = _NncExtPm15MinIntervalTotalLostCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 14),
    _NncExtPm15MinIntervalTotalLostCellsClp0_Type()
)
nncExtPm15MinIntervalTotalLostCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalTotalLostCellsClp0.setStatus("current")
_NncExtPm15MinIntervalIBWithCellLossMisinsert_Type = NncExtCounter64
_NncExtPm15MinIntervalIBWithCellLossMisinsert_Object = MibTableColumn
nncExtPm15MinIntervalIBWithCellLossMisinsert = _NncExtPm15MinIntervalIBWithCellLossMisinsert_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 15),
    _NncExtPm15MinIntervalIBWithCellLossMisinsert_Type()
)
nncExtPm15MinIntervalIBWithCellLossMisinsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalIBWithCellLossMisinsert.setStatus("current")
_NncExtPm15MinIntervalCellLossRatioClp0And1_Type = NncExtCounter64
_NncExtPm15MinIntervalCellLossRatioClp0And1_Object = MibTableColumn
nncExtPm15MinIntervalCellLossRatioClp0And1 = _NncExtPm15MinIntervalCellLossRatioClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 16),
    _NncExtPm15MinIntervalCellLossRatioClp0And1_Type()
)
nncExtPm15MinIntervalCellLossRatioClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalCellLossRatioClp0And1.setStatus("current")
_NncExtPm15MinIntervalCellLossRatioClp0_Type = NncExtCounter64
_NncExtPm15MinIntervalCellLossRatioClp0_Object = MibTableColumn
nncExtPm15MinIntervalCellLossRatioClp0 = _NncExtPm15MinIntervalCellLossRatioClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 2, 1, 17),
    _NncExtPm15MinIntervalCellLossRatioClp0_Type()
)
nncExtPm15MinIntervalCellLossRatioClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalCellLossRatioClp0.setStatus("current")
_NncExtPm24HrCurrentTable_Object = MibTable
nncExtPm24HrCurrentTable = _NncExtPm24HrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3)
)
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentTable.setStatus("current")
_NncExtPm24HrCurrentEntry_Object = MibTableRow
nncExtPm24HrCurrentEntry = _NncExtPm24HrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1)
)
nncExtPm24HrCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentCellFlow"),
    (0, "NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentTest"),
)
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentEntry.setStatus("current")
_NncExtPm24HrCurrentCellFlow_Type = NncExtPmCellFlowDirType
_NncExtPm24HrCurrentCellFlow_Object = MibTableColumn
nncExtPm24HrCurrentCellFlow = _NncExtPm24HrCurrentCellFlow_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 1),
    _NncExtPm24HrCurrentCellFlow_Type()
)
nncExtPm24HrCurrentCellFlow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentCellFlow.setStatus("current")
_NncExtPm24HrCurrentTest_Type = NncExtPmTestType
_NncExtPm24HrCurrentTest_Object = MibTableColumn
nncExtPm24HrCurrentTest = _NncExtPm24HrCurrentTest_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 2),
    _NncExtPm24HrCurrentTest_Type()
)
nncExtPm24HrCurrentTest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentTest.setStatus("current")
_NncExtPm24HrCurrentState_Type = NncExtIntvlStateType
_NncExtPm24HrCurrentState_Object = MibTableColumn
nncExtPm24HrCurrentState = _NncExtPm24HrCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 3),
    _NncExtPm24HrCurrentState_Type()
)
nncExtPm24HrCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentState.setStatus("current")
_NncExtPm24HrCurrentAbsoluteIntervalNumber_Type = NncExtAbsIntvlNumberType
_NncExtPm24HrCurrentAbsoluteIntervalNumber_Object = MibTableColumn
nncExtPm24HrCurrentAbsoluteIntervalNumber = _NncExtPm24HrCurrentAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 4),
    _NncExtPm24HrCurrentAbsoluteIntervalNumber_Type()
)
nncExtPm24HrCurrentAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentAbsoluteIntervalNumber.setStatus("current")
_NncExtPm24HrCurrentSECBs_Type = NncExtCounter64
_NncExtPm24HrCurrentSECBs_Object = MibTableColumn
nncExtPm24HrCurrentSECBs = _NncExtPm24HrCurrentSECBs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 5),
    _NncExtPm24HrCurrentSECBs_Type()
)
nncExtPm24HrCurrentSECBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentSECBs.setStatus("current")
_NncExtPm24HrCurrentErroredCells_Type = NncExtCounter64
_NncExtPm24HrCurrentErroredCells_Object = MibTableColumn
nncExtPm24HrCurrentErroredCells = _NncExtPm24HrCurrentErroredCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 6),
    _NncExtPm24HrCurrentErroredCells_Type()
)
nncExtPm24HrCurrentErroredCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentErroredCells.setStatus("current")
_NncExtPm24HrCurrentLostCellsClp0And1_Type = NncExtCounter64
_NncExtPm24HrCurrentLostCellsClp0And1_Object = MibTableColumn
nncExtPm24HrCurrentLostCellsClp0And1 = _NncExtPm24HrCurrentLostCellsClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 7),
    _NncExtPm24HrCurrentLostCellsClp0And1_Type()
)
nncExtPm24HrCurrentLostCellsClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentLostCellsClp0And1.setStatus("current")
_NncExtPm24HrCurrentLostCellsClp0_Type = NncExtCounter64
_NncExtPm24HrCurrentLostCellsClp0_Object = MibTableColumn
nncExtPm24HrCurrentLostCellsClp0 = _NncExtPm24HrCurrentLostCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 8),
    _NncExtPm24HrCurrentLostCellsClp0_Type()
)
nncExtPm24HrCurrentLostCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentLostCellsClp0.setStatus("current")
_NncExtPm24HrCurrentMisinsertedCells_Type = NncExtCounter64
_NncExtPm24HrCurrentMisinsertedCells_Object = MibTableColumn
nncExtPm24HrCurrentMisinsertedCells = _NncExtPm24HrCurrentMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 9),
    _NncExtPm24HrCurrentMisinsertedCells_Type()
)
nncExtPm24HrCurrentMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentMisinsertedCells.setStatus("current")
_NncExtPm24HrCurrentCellsClp0And1_Type = NncExtCounter64
_NncExtPm24HrCurrentCellsClp0And1_Object = MibTableColumn
nncExtPm24HrCurrentCellsClp0And1 = _NncExtPm24HrCurrentCellsClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 10),
    _NncExtPm24HrCurrentCellsClp0And1_Type()
)
nncExtPm24HrCurrentCellsClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentCellsClp0And1.setStatus("current")
_NncExtPm24HrCurrentCellsClp0_Type = NncExtCounter64
_NncExtPm24HrCurrentCellsClp0_Object = MibTableColumn
nncExtPm24HrCurrentCellsClp0 = _NncExtPm24HrCurrentCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 11),
    _NncExtPm24HrCurrentCellsClp0_Type()
)
nncExtPm24HrCurrentCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentCellsClp0.setStatus("current")
_NncExtPm24HrCurrentImpairedBlocks_Type = NncExtCounter64
_NncExtPm24HrCurrentImpairedBlocks_Object = MibTableColumn
nncExtPm24HrCurrentImpairedBlocks = _NncExtPm24HrCurrentImpairedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 12),
    _NncExtPm24HrCurrentImpairedBlocks_Type()
)
nncExtPm24HrCurrentImpairedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentImpairedBlocks.setStatus("current")
_NncExtPm24HrCurrentTotalLostCellsClp0And1_Type = NncExtCounter64
_NncExtPm24HrCurrentTotalLostCellsClp0And1_Object = MibTableColumn
nncExtPm24HrCurrentTotalLostCellsClp0And1 = _NncExtPm24HrCurrentTotalLostCellsClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 13),
    _NncExtPm24HrCurrentTotalLostCellsClp0And1_Type()
)
nncExtPm24HrCurrentTotalLostCellsClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentTotalLostCellsClp0And1.setStatus("current")
_NncExtPm24HrCurrentTotalLostCellsClp0_Type = NncExtCounter64
_NncExtPm24HrCurrentTotalLostCellsClp0_Object = MibTableColumn
nncExtPm24HrCurrentTotalLostCellsClp0 = _NncExtPm24HrCurrentTotalLostCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 14),
    _NncExtPm24HrCurrentTotalLostCellsClp0_Type()
)
nncExtPm24HrCurrentTotalLostCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentTotalLostCellsClp0.setStatus("current")
_NncExtPm24HrCurrentSECBErrored_Type = NncExtCounter64
_NncExtPm24HrCurrentSECBErrored_Object = MibTableColumn
nncExtPm24HrCurrentSECBErrored = _NncExtPm24HrCurrentSECBErrored_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 15),
    _NncExtPm24HrCurrentSECBErrored_Type()
)
nncExtPm24HrCurrentSECBErrored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentSECBErrored.setStatus("current")
_NncExtPm24HrCurrentSECBMisinserted_Type = NncExtCounter64
_NncExtPm24HrCurrentSECBMisinserted_Object = MibTableColumn
nncExtPm24HrCurrentSECBMisinserted = _NncExtPm24HrCurrentSECBMisinserted_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 16),
    _NncExtPm24HrCurrentSECBMisinserted_Type()
)
nncExtPm24HrCurrentSECBMisinserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentSECBMisinserted.setStatus("current")
_NncExtPm24HrCurrentIBWithCellLossMisinsert_Type = NncExtCounter64
_NncExtPm24HrCurrentIBWithCellLossMisinsert_Object = MibTableColumn
nncExtPm24HrCurrentIBWithCellLossMisinsert = _NncExtPm24HrCurrentIBWithCellLossMisinsert_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 17),
    _NncExtPm24HrCurrentIBWithCellLossMisinsert_Type()
)
nncExtPm24HrCurrentIBWithCellLossMisinsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentIBWithCellLossMisinsert.setStatus("current")
_NncExtPm24HrCurrentCellLossRatioClp0And1_Type = NncExtCounter64
_NncExtPm24HrCurrentCellLossRatioClp0And1_Object = MibTableColumn
nncExtPm24HrCurrentCellLossRatioClp0And1 = _NncExtPm24HrCurrentCellLossRatioClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 18),
    _NncExtPm24HrCurrentCellLossRatioClp0And1_Type()
)
nncExtPm24HrCurrentCellLossRatioClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentCellLossRatioClp0And1.setStatus("current")
_NncExtPm24HrCurrentCellLossRatioClp0_Type = NncExtCounter64
_NncExtPm24HrCurrentCellLossRatioClp0_Object = MibTableColumn
nncExtPm24HrCurrentCellLossRatioClp0 = _NncExtPm24HrCurrentCellLossRatioClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 3, 1, 19),
    _NncExtPm24HrCurrentCellLossRatioClp0_Type()
)
nncExtPm24HrCurrentCellLossRatioClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentCellLossRatioClp0.setStatus("current")
_NncExtPm24HrIntervalTable_Object = MibTable
nncExtPm24HrIntervalTable = _NncExtPm24HrIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4)
)
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalTable.setStatus("current")
_NncExtPm24HrIntervalEntry_Object = MibTableRow
nncExtPm24HrIntervalEntry = _NncExtPm24HrIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1)
)
nncExtPm24HrIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalCellFlow"),
    (0, "NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalTest"),
    (0, "NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalNumber"),
)
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalEntry.setStatus("current")
_NncExtPm24HrIntervalCellFlow_Type = NncExtPmCellFlowDirType
_NncExtPm24HrIntervalCellFlow_Object = MibTableColumn
nncExtPm24HrIntervalCellFlow = _NncExtPm24HrIntervalCellFlow_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 1),
    _NncExtPm24HrIntervalCellFlow_Type()
)
nncExtPm24HrIntervalCellFlow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalCellFlow.setStatus("current")
_NncExtPm24HrIntervalTest_Type = NncExtPmTestType
_NncExtPm24HrIntervalTest_Object = MibTableColumn
nncExtPm24HrIntervalTest = _NncExtPm24HrIntervalTest_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 2),
    _NncExtPm24HrIntervalTest_Type()
)
nncExtPm24HrIntervalTest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalTest.setStatus("current")
_NncExtPm24HrIntervalNumber_Type = NncExtRelIntvlNumberType
_NncExtPm24HrIntervalNumber_Object = MibTableColumn
nncExtPm24HrIntervalNumber = _NncExtPm24HrIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 3),
    _NncExtPm24HrIntervalNumber_Type()
)
nncExtPm24HrIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalNumber.setStatus("current")
_NncExtPm24HrIntervalState_Type = NncExtIntvlStateType
_NncExtPm24HrIntervalState_Object = MibTableColumn
nncExtPm24HrIntervalState = _NncExtPm24HrIntervalState_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 4),
    _NncExtPm24HrIntervalState_Type()
)
nncExtPm24HrIntervalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalState.setStatus("current")
_NncExtPm24HrIntervalAbsoluteIntervalNumber_Type = NncExtAbsIntvlNumberType
_NncExtPm24HrIntervalAbsoluteIntervalNumber_Object = MibTableColumn
nncExtPm24HrIntervalAbsoluteIntervalNumber = _NncExtPm24HrIntervalAbsoluteIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 5),
    _NncExtPm24HrIntervalAbsoluteIntervalNumber_Type()
)
nncExtPm24HrIntervalAbsoluteIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalAbsoluteIntervalNumber.setStatus("current")
_NncExtPm24HrIntervalSECBs_Type = NncExtCounter64
_NncExtPm24HrIntervalSECBs_Object = MibTableColumn
nncExtPm24HrIntervalSECBs = _NncExtPm24HrIntervalSECBs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 6),
    _NncExtPm24HrIntervalSECBs_Type()
)
nncExtPm24HrIntervalSECBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalSECBs.setStatus("current")
_NncExtPm24HrIntervalErroredCells_Type = NncExtCounter64
_NncExtPm24HrIntervalErroredCells_Object = MibTableColumn
nncExtPm24HrIntervalErroredCells = _NncExtPm24HrIntervalErroredCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 7),
    _NncExtPm24HrIntervalErroredCells_Type()
)
nncExtPm24HrIntervalErroredCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalErroredCells.setStatus("current")
_NncExtPm24HrIntervalLostCellsClp0And1_Type = NncExtCounter64
_NncExtPm24HrIntervalLostCellsClp0And1_Object = MibTableColumn
nncExtPm24HrIntervalLostCellsClp0And1 = _NncExtPm24HrIntervalLostCellsClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 8),
    _NncExtPm24HrIntervalLostCellsClp0And1_Type()
)
nncExtPm24HrIntervalLostCellsClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalLostCellsClp0And1.setStatus("current")
_NncExtPm24HrIntervalLostCellsClp0_Type = NncExtCounter64
_NncExtPm24HrIntervalLostCellsClp0_Object = MibTableColumn
nncExtPm24HrIntervalLostCellsClp0 = _NncExtPm24HrIntervalLostCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 9),
    _NncExtPm24HrIntervalLostCellsClp0_Type()
)
nncExtPm24HrIntervalLostCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalLostCellsClp0.setStatus("current")
_NncExtPm24HrIntervalMisinsertedCells_Type = NncExtCounter64
_NncExtPm24HrIntervalMisinsertedCells_Object = MibTableColumn
nncExtPm24HrIntervalMisinsertedCells = _NncExtPm24HrIntervalMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 10),
    _NncExtPm24HrIntervalMisinsertedCells_Type()
)
nncExtPm24HrIntervalMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalMisinsertedCells.setStatus("current")
_NncExtPm24HrIntervalCellsClp0And1_Type = NncExtCounter64
_NncExtPm24HrIntervalCellsClp0And1_Object = MibTableColumn
nncExtPm24HrIntervalCellsClp0And1 = _NncExtPm24HrIntervalCellsClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 11),
    _NncExtPm24HrIntervalCellsClp0And1_Type()
)
nncExtPm24HrIntervalCellsClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalCellsClp0And1.setStatus("current")
_NncExtPm24HrIntervalCellsClp0_Type = NncExtCounter64
_NncExtPm24HrIntervalCellsClp0_Object = MibTableColumn
nncExtPm24HrIntervalCellsClp0 = _NncExtPm24HrIntervalCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 12),
    _NncExtPm24HrIntervalCellsClp0_Type()
)
nncExtPm24HrIntervalCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalCellsClp0.setStatus("current")
_NncExtPm24HrIntervalImpairedBlocks_Type = NncExtCounter64
_NncExtPm24HrIntervalImpairedBlocks_Object = MibTableColumn
nncExtPm24HrIntervalImpairedBlocks = _NncExtPm24HrIntervalImpairedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 13),
    _NncExtPm24HrIntervalImpairedBlocks_Type()
)
nncExtPm24HrIntervalImpairedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalImpairedBlocks.setStatus("current")
_NncExtPm24HrIntervalTotalLostCellsClp0And1_Type = NncExtCounter64
_NncExtPm24HrIntervalTotalLostCellsClp0And1_Object = MibTableColumn
nncExtPm24HrIntervalTotalLostCellsClp0And1 = _NncExtPm24HrIntervalTotalLostCellsClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 14),
    _NncExtPm24HrIntervalTotalLostCellsClp0And1_Type()
)
nncExtPm24HrIntervalTotalLostCellsClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalTotalLostCellsClp0And1.setStatus("current")
_NncExtPm24HrIntervalTotalLostCellsClp0_Type = NncExtCounter64
_NncExtPm24HrIntervalTotalLostCellsClp0_Object = MibTableColumn
nncExtPm24HrIntervalTotalLostCellsClp0 = _NncExtPm24HrIntervalTotalLostCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 15),
    _NncExtPm24HrIntervalTotalLostCellsClp0_Type()
)
nncExtPm24HrIntervalTotalLostCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalTotalLostCellsClp0.setStatus("current")
_NncExtPm24HrIntervalSECBErrored_Type = NncExtCounter64
_NncExtPm24HrIntervalSECBErrored_Object = MibTableColumn
nncExtPm24HrIntervalSECBErrored = _NncExtPm24HrIntervalSECBErrored_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 16),
    _NncExtPm24HrIntervalSECBErrored_Type()
)
nncExtPm24HrIntervalSECBErrored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalSECBErrored.setStatus("current")
_NncExtPm24HrIntervalSECBMisinserted_Type = NncExtCounter64
_NncExtPm24HrIntervalSECBMisinserted_Object = MibTableColumn
nncExtPm24HrIntervalSECBMisinserted = _NncExtPm24HrIntervalSECBMisinserted_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 17),
    _NncExtPm24HrIntervalSECBMisinserted_Type()
)
nncExtPm24HrIntervalSECBMisinserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalSECBMisinserted.setStatus("current")
_NncExtPm24HrIntervalIBWithCellLossMisinsert_Type = NncExtCounter64
_NncExtPm24HrIntervalIBWithCellLossMisinsert_Object = MibTableColumn
nncExtPm24HrIntervalIBWithCellLossMisinsert = _NncExtPm24HrIntervalIBWithCellLossMisinsert_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 18),
    _NncExtPm24HrIntervalIBWithCellLossMisinsert_Type()
)
nncExtPm24HrIntervalIBWithCellLossMisinsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalIBWithCellLossMisinsert.setStatus("current")
_NncExtPm24HrIntervalCellLossRatioClp0And1_Type = NncExtCounter64
_NncExtPm24HrIntervalCellLossRatioClp0And1_Object = MibTableColumn
nncExtPm24HrIntervalCellLossRatioClp0And1 = _NncExtPm24HrIntervalCellLossRatioClp0And1_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 19),
    _NncExtPm24HrIntervalCellLossRatioClp0And1_Type()
)
nncExtPm24HrIntervalCellLossRatioClp0And1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalCellLossRatioClp0And1.setStatus("current")
_NncExtPm24HrIntervalCellLossRatioClp0_Type = NncExtCounter64
_NncExtPm24HrIntervalCellLossRatioClp0_Object = MibTableColumn
nncExtPm24HrIntervalCellLossRatioClp0 = _NncExtPm24HrIntervalCellLossRatioClp0_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 1, 4, 1, 20),
    _NncExtPm24HrIntervalCellLossRatioClp0_Type()
)
nncExtPm24HrIntervalCellLossRatioClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalCellLossRatioClp0.setStatus("current")
_NncExtPmStatisticsTraps_ObjectIdentity = ObjectIdentity
nncExtPmStatisticsTraps = _NncExtPmStatisticsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 2)
)
_NncExtPmStatisticsGroups_ObjectIdentity = ObjectIdentity
nncExtPmStatisticsGroups = _NncExtPmStatisticsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 3)
)
_NncExtPmStatisticsCompliances_ObjectIdentity = ObjectIdentity
nncExtPmStatisticsCompliances = _NncExtPmStatisticsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 4)
)

# Managed Objects groups

nncExtPm15MinCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 3, 1)
)
nncExtPm15MinCurrentGroup.setObjects(
      *(("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentCellFlow"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentTest"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentState"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentAbsoluteIntervalNumber"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentSECBs"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentLostCellsClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentLostCellsClp0"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentMisinsertedCells"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentCellsClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentCellsClp0"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentImpairedBlocks"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentTotalLostCellsClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentTotalLostCellsClp0"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentIBWithCellLossMisinsert"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentCellLossRatioClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinCurrentCellLossRatioClp0"))
)
if mibBuilder.loadTexts:
    nncExtPm15MinCurrentGroup.setStatus("current")

nncExtPm15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 3, 2)
)
nncExtPm15MinIntervalGroup.setObjects(
      *(("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalCellFlow"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalTest"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalNumber"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalState"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalAbsoluteIntervalNumber"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalSECBs"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalLostCellsClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalLostCellsClp0"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalMisinsertedCells"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalCellsClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalCellsClp0"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalImpairedBlocks"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalTotalLostCellsClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalTotalLostCellsClp0"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalIBWithCellLossMisinsert"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalCellLossRatioClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm15MinIntervalCellLossRatioClp0"))
)
if mibBuilder.loadTexts:
    nncExtPm15MinIntervalGroup.setStatus("current")

nncExtPm24HrCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 3, 3)
)
nncExtPm24HrCurrentGroup.setObjects(
      *(("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentCellFlow"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentTest"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentState"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentAbsoluteIntervalNumber"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentSECBs"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentErroredCells"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentLostCellsClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentLostCellsClp0"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentMisinsertedCells"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentCellsClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentCellsClp0"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentImpairedBlocks"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentTotalLostCellsClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentTotalLostCellsClp0"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentSECBErrored"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentSECBMisinserted"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentIBWithCellLossMisinsert"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentCellLossRatioClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrCurrentCellLossRatioClp0"))
)
if mibBuilder.loadTexts:
    nncExtPm24HrCurrentGroup.setStatus("current")

nncExtPm24HrIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 3, 4)
)
nncExtPm24HrIntervalGroup.setObjects(
      *(("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalCellFlow"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalTest"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalNumber"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalState"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalAbsoluteIntervalNumber"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalSECBs"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalErroredCells"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalLostCellsClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalLostCellsClp0"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalMisinsertedCells"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalCellsClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalCellsClp0"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalImpairedBlocks"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalTotalLostCellsClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalTotalLostCellsClp0"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalSECBErrored"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalSECBMisinserted"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalIBWithCellLossMisinsert"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalCellLossRatioClp0And1"),
        ("NNC-EXT-PM-STATISTICS-MIB", "nncExtPm24HrIntervalCellLossRatioClp0"))
)
if mibBuilder.loadTexts:
    nncExtPm24HrIntervalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncExtPmStatisticsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 65, 4, 1)
)
if mibBuilder.loadTexts:
    nncExtPmStatisticsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNC-EXT-PM-STATISTICS-MIB",
    **{"NncExtPmCellFlowDirType": NncExtPmCellFlowDirType,
       "NncExtPmTestType": NncExtPmTestType,
       "nncExtPmStatistics": nncExtPmStatistics,
       "nncExtPmStatisticsObjects": nncExtPmStatisticsObjects,
       "nncExtPm15MinCurrentTable": nncExtPm15MinCurrentTable,
       "nncExtPm15MinCurrentEntry": nncExtPm15MinCurrentEntry,
       "nncExtPm15MinCurrentCellFlow": nncExtPm15MinCurrentCellFlow,
       "nncExtPm15MinCurrentTest": nncExtPm15MinCurrentTest,
       "nncExtPm15MinCurrentState": nncExtPm15MinCurrentState,
       "nncExtPm15MinCurrentAbsoluteIntervalNumber": nncExtPm15MinCurrentAbsoluteIntervalNumber,
       "nncExtPm15MinCurrentSECBs": nncExtPm15MinCurrentSECBs,
       "nncExtPm15MinCurrentLostCellsClp0And1": nncExtPm15MinCurrentLostCellsClp0And1,
       "nncExtPm15MinCurrentLostCellsClp0": nncExtPm15MinCurrentLostCellsClp0,
       "nncExtPm15MinCurrentMisinsertedCells": nncExtPm15MinCurrentMisinsertedCells,
       "nncExtPm15MinCurrentCellsClp0And1": nncExtPm15MinCurrentCellsClp0And1,
       "nncExtPm15MinCurrentCellsClp0": nncExtPm15MinCurrentCellsClp0,
       "nncExtPm15MinCurrentImpairedBlocks": nncExtPm15MinCurrentImpairedBlocks,
       "nncExtPm15MinCurrentTotalLostCellsClp0And1": nncExtPm15MinCurrentTotalLostCellsClp0And1,
       "nncExtPm15MinCurrentTotalLostCellsClp0": nncExtPm15MinCurrentTotalLostCellsClp0,
       "nncExtPm15MinCurrentIBWithCellLossMisinsert": nncExtPm15MinCurrentIBWithCellLossMisinsert,
       "nncExtPm15MinCurrentCellLossRatioClp0And1": nncExtPm15MinCurrentCellLossRatioClp0And1,
       "nncExtPm15MinCurrentCellLossRatioClp0": nncExtPm15MinCurrentCellLossRatioClp0,
       "nncExtPm15MinIntervalTable": nncExtPm15MinIntervalTable,
       "nncExtPm15MinIntervalEntry": nncExtPm15MinIntervalEntry,
       "nncExtPm15MinIntervalCellFlow": nncExtPm15MinIntervalCellFlow,
       "nncExtPm15MinIntervalTest": nncExtPm15MinIntervalTest,
       "nncExtPm15MinIntervalNumber": nncExtPm15MinIntervalNumber,
       "nncExtPm15MinIntervalState": nncExtPm15MinIntervalState,
       "nncExtPm15MinIntervalAbsoluteIntervalNumber": nncExtPm15MinIntervalAbsoluteIntervalNumber,
       "nncExtPm15MinIntervalSECBs": nncExtPm15MinIntervalSECBs,
       "nncExtPm15MinIntervalLostCellsClp0And1": nncExtPm15MinIntervalLostCellsClp0And1,
       "nncExtPm15MinIntervalLostCellsClp0": nncExtPm15MinIntervalLostCellsClp0,
       "nncExtPm15MinIntervalMisinsertedCells": nncExtPm15MinIntervalMisinsertedCells,
       "nncExtPm15MinIntervalCellsClp0And1": nncExtPm15MinIntervalCellsClp0And1,
       "nncExtPm15MinIntervalCellsClp0": nncExtPm15MinIntervalCellsClp0,
       "nncExtPm15MinIntervalImpairedBlocks": nncExtPm15MinIntervalImpairedBlocks,
       "nncExtPm15MinIntervalTotalLostCellsClp0And1": nncExtPm15MinIntervalTotalLostCellsClp0And1,
       "nncExtPm15MinIntervalTotalLostCellsClp0": nncExtPm15MinIntervalTotalLostCellsClp0,
       "nncExtPm15MinIntervalIBWithCellLossMisinsert": nncExtPm15MinIntervalIBWithCellLossMisinsert,
       "nncExtPm15MinIntervalCellLossRatioClp0And1": nncExtPm15MinIntervalCellLossRatioClp0And1,
       "nncExtPm15MinIntervalCellLossRatioClp0": nncExtPm15MinIntervalCellLossRatioClp0,
       "nncExtPm24HrCurrentTable": nncExtPm24HrCurrentTable,
       "nncExtPm24HrCurrentEntry": nncExtPm24HrCurrentEntry,
       "nncExtPm24HrCurrentCellFlow": nncExtPm24HrCurrentCellFlow,
       "nncExtPm24HrCurrentTest": nncExtPm24HrCurrentTest,
       "nncExtPm24HrCurrentState": nncExtPm24HrCurrentState,
       "nncExtPm24HrCurrentAbsoluteIntervalNumber": nncExtPm24HrCurrentAbsoluteIntervalNumber,
       "nncExtPm24HrCurrentSECBs": nncExtPm24HrCurrentSECBs,
       "nncExtPm24HrCurrentErroredCells": nncExtPm24HrCurrentErroredCells,
       "nncExtPm24HrCurrentLostCellsClp0And1": nncExtPm24HrCurrentLostCellsClp0And1,
       "nncExtPm24HrCurrentLostCellsClp0": nncExtPm24HrCurrentLostCellsClp0,
       "nncExtPm24HrCurrentMisinsertedCells": nncExtPm24HrCurrentMisinsertedCells,
       "nncExtPm24HrCurrentCellsClp0And1": nncExtPm24HrCurrentCellsClp0And1,
       "nncExtPm24HrCurrentCellsClp0": nncExtPm24HrCurrentCellsClp0,
       "nncExtPm24HrCurrentImpairedBlocks": nncExtPm24HrCurrentImpairedBlocks,
       "nncExtPm24HrCurrentTotalLostCellsClp0And1": nncExtPm24HrCurrentTotalLostCellsClp0And1,
       "nncExtPm24HrCurrentTotalLostCellsClp0": nncExtPm24HrCurrentTotalLostCellsClp0,
       "nncExtPm24HrCurrentSECBErrored": nncExtPm24HrCurrentSECBErrored,
       "nncExtPm24HrCurrentSECBMisinserted": nncExtPm24HrCurrentSECBMisinserted,
       "nncExtPm24HrCurrentIBWithCellLossMisinsert": nncExtPm24HrCurrentIBWithCellLossMisinsert,
       "nncExtPm24HrCurrentCellLossRatioClp0And1": nncExtPm24HrCurrentCellLossRatioClp0And1,
       "nncExtPm24HrCurrentCellLossRatioClp0": nncExtPm24HrCurrentCellLossRatioClp0,
       "nncExtPm24HrIntervalTable": nncExtPm24HrIntervalTable,
       "nncExtPm24HrIntervalEntry": nncExtPm24HrIntervalEntry,
       "nncExtPm24HrIntervalCellFlow": nncExtPm24HrIntervalCellFlow,
       "nncExtPm24HrIntervalTest": nncExtPm24HrIntervalTest,
       "nncExtPm24HrIntervalNumber": nncExtPm24HrIntervalNumber,
       "nncExtPm24HrIntervalState": nncExtPm24HrIntervalState,
       "nncExtPm24HrIntervalAbsoluteIntervalNumber": nncExtPm24HrIntervalAbsoluteIntervalNumber,
       "nncExtPm24HrIntervalSECBs": nncExtPm24HrIntervalSECBs,
       "nncExtPm24HrIntervalErroredCells": nncExtPm24HrIntervalErroredCells,
       "nncExtPm24HrIntervalLostCellsClp0And1": nncExtPm24HrIntervalLostCellsClp0And1,
       "nncExtPm24HrIntervalLostCellsClp0": nncExtPm24HrIntervalLostCellsClp0,
       "nncExtPm24HrIntervalMisinsertedCells": nncExtPm24HrIntervalMisinsertedCells,
       "nncExtPm24HrIntervalCellsClp0And1": nncExtPm24HrIntervalCellsClp0And1,
       "nncExtPm24HrIntervalCellsClp0": nncExtPm24HrIntervalCellsClp0,
       "nncExtPm24HrIntervalImpairedBlocks": nncExtPm24HrIntervalImpairedBlocks,
       "nncExtPm24HrIntervalTotalLostCellsClp0And1": nncExtPm24HrIntervalTotalLostCellsClp0And1,
       "nncExtPm24HrIntervalTotalLostCellsClp0": nncExtPm24HrIntervalTotalLostCellsClp0,
       "nncExtPm24HrIntervalSECBErrored": nncExtPm24HrIntervalSECBErrored,
       "nncExtPm24HrIntervalSECBMisinserted": nncExtPm24HrIntervalSECBMisinserted,
       "nncExtPm24HrIntervalIBWithCellLossMisinsert": nncExtPm24HrIntervalIBWithCellLossMisinsert,
       "nncExtPm24HrIntervalCellLossRatioClp0And1": nncExtPm24HrIntervalCellLossRatioClp0And1,
       "nncExtPm24HrIntervalCellLossRatioClp0": nncExtPm24HrIntervalCellLossRatioClp0,
       "nncExtPmStatisticsTraps": nncExtPmStatisticsTraps,
       "nncExtPmStatisticsGroups": nncExtPmStatisticsGroups,
       "nncExtPm15MinCurrentGroup": nncExtPm15MinCurrentGroup,
       "nncExtPm15MinIntervalGroup": nncExtPm15MinIntervalGroup,
       "nncExtPm24HrCurrentGroup": nncExtPm24HrCurrentGroup,
       "nncExtPm24HrIntervalGroup": nncExtPm24HrIntervalGroup,
       "nncExtPmStatisticsCompliances": nncExtPmStatisticsCompliances,
       "nncExtPmStatisticsCompliance": nncExtPmStatisticsCompliance}
)
