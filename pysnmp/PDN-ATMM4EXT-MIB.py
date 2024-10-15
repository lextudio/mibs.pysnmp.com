# SNMP MIB module (PDN-ATMM4EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-ATMM4EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:18 2024
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

(atmfM4TcProtoCurrEntry,
 atmfM4TcProtoHistEntry,
 atmfM4VcTestEntry,
 atmfM4VpTestEntry) = mibBuilder.importSymbols(
    "ATM-FORUM-SNMP-M4-MIB",
    "atmfM4TcProtoCurrEntry",
    "atmfM4TcProtoHistEntry",
    "atmfM4VcTestEntry",
    "atmfM4VpTestEntry")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdnAtm,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdnAtm")

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

pdnAtmfM4ExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6)
)
pdnAtmfM4ExtMIB.setRevisions(
        ("2002-08-15 00:00",
         "2001-03-08 00:00",
         "2000-09-26 00:00",
         "2000-09-22 00:00",
         "2000-09-21 00:00",
         "2000-09-08 00:00",
         "2000-06-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PdnAtmfM4TestErrorCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("adminStatusDisabled", 8),
          ("badIfIndex", 1),
          ("noError", 0),
          ("noLoopbackAllocated", 5),
          ("noResourceAvailable", 4),
          ("noVccFound", 2),
          ("notOwner", 3),
          ("testCompleted", 6),
          ("testTimeOut", 7))
    )



# MIB Managed Objects in the order of their OIDs

_PdnAtmfM4ExtObjects_ObjectIdentity = ObjectIdentity
pdnAtmfM4ExtObjects = _PdnAtmfM4ExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1)
)
_PdnAtmfM4TcProtoCurrExtTable_Object = MibTable
pdnAtmfM4TcProtoCurrExtTable = _PdnAtmfM4TcProtoCurrExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 1)
)
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoCurrExtTable.setStatus("current")
_PdnAtmfM4TcProtoCurrExtEntry_Object = MibTableRow
pdnAtmfM4TcProtoCurrExtEntry = _PdnAtmfM4TcProtoCurrExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoCurrExtEntry.setStatus("current")
_PdnAtmfM4TcProtoCurrCellIns_Type = Gauge32
_PdnAtmfM4TcProtoCurrCellIns_Object = MibTableColumn
pdnAtmfM4TcProtoCurrCellIns = _PdnAtmfM4TcProtoCurrCellIns_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 1, 1, 1),
    _PdnAtmfM4TcProtoCurrCellIns_Type()
)
pdnAtmfM4TcProtoCurrCellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoCurrCellIns.setStatus("current")
_PdnAtmfM4TcProtoCurrCellOuts_Type = Gauge32
_PdnAtmfM4TcProtoCurrCellOuts_Object = MibTableColumn
pdnAtmfM4TcProtoCurrCellOuts = _PdnAtmfM4TcProtoCurrCellOuts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 1, 1, 2),
    _PdnAtmfM4TcProtoCurrCellOuts_Type()
)
pdnAtmfM4TcProtoCurrCellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoCurrCellOuts.setStatus("current")
_PdnAtmfM4TcProtoCurrInDiscards_Type = Gauge32
_PdnAtmfM4TcProtoCurrInDiscards_Object = MibTableColumn
pdnAtmfM4TcProtoCurrInDiscards = _PdnAtmfM4TcProtoCurrInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 1, 1, 3),
    _PdnAtmfM4TcProtoCurrInDiscards_Type()
)
pdnAtmfM4TcProtoCurrInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoCurrInDiscards.setStatus("current")
_PdnAtmfM4TcProtoCurrOutDiscards_Type = Gauge32
_PdnAtmfM4TcProtoCurrOutDiscards_Object = MibTableColumn
pdnAtmfM4TcProtoCurrOutDiscards = _PdnAtmfM4TcProtoCurrOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 1, 1, 4),
    _PdnAtmfM4TcProtoCurrOutDiscards_Type()
)
pdnAtmfM4TcProtoCurrOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoCurrOutDiscards.setStatus("current")
_PdnAtmfM4TcProtoCurrLCDEvents_Type = Gauge32
_PdnAtmfM4TcProtoCurrLCDEvents_Object = MibTableColumn
pdnAtmfM4TcProtoCurrLCDEvents = _PdnAtmfM4TcProtoCurrLCDEvents_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 1, 1, 5),
    _PdnAtmfM4TcProtoCurrLCDEvents_Type()
)
pdnAtmfM4TcProtoCurrLCDEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoCurrLCDEvents.setStatus("current")
_PdnAtmfM4TcProtoCurrUnknownCells_Type = Gauge32
_PdnAtmfM4TcProtoCurrUnknownCells_Object = MibTableColumn
pdnAtmfM4TcProtoCurrUnknownCells = _PdnAtmfM4TcProtoCurrUnknownCells_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 1, 1, 6),
    _PdnAtmfM4TcProtoCurrUnknownCells_Type()
)
pdnAtmfM4TcProtoCurrUnknownCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoCurrUnknownCells.setStatus("current")
_PdnAtmfM4TcProtoCurrCorrectedHEC_Type = Gauge32
_PdnAtmfM4TcProtoCurrCorrectedHEC_Object = MibTableColumn
pdnAtmfM4TcProtoCurrCorrectedHEC = _PdnAtmfM4TcProtoCurrCorrectedHEC_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 1, 1, 7),
    _PdnAtmfM4TcProtoCurrCorrectedHEC_Type()
)
pdnAtmfM4TcProtoCurrCorrectedHEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoCurrCorrectedHEC.setStatus("current")
_PdnAtmfM4TcProtoHistExtTable_Object = MibTable
pdnAtmfM4TcProtoHistExtTable = _PdnAtmfM4TcProtoHistExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 2)
)
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoHistExtTable.setStatus("current")
_PdnAtmfM4TcProtoHistExtEntry_Object = MibTableRow
pdnAtmfM4TcProtoHistExtEntry = _PdnAtmfM4TcProtoHistExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoHistExtEntry.setStatus("current")
_PdnAtmfM4TcProtoHistCellIns_Type = Gauge32
_PdnAtmfM4TcProtoHistCellIns_Object = MibTableColumn
pdnAtmfM4TcProtoHistCellIns = _PdnAtmfM4TcProtoHistCellIns_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 2, 1, 1),
    _PdnAtmfM4TcProtoHistCellIns_Type()
)
pdnAtmfM4TcProtoHistCellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoHistCellIns.setStatus("current")
_PdnAtmfM4TcProtoHistCellOuts_Type = Gauge32
_PdnAtmfM4TcProtoHistCellOuts_Object = MibTableColumn
pdnAtmfM4TcProtoHistCellOuts = _PdnAtmfM4TcProtoHistCellOuts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 2, 1, 2),
    _PdnAtmfM4TcProtoHistCellOuts_Type()
)
pdnAtmfM4TcProtoHistCellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoHistCellOuts.setStatus("current")
_PdnAtmfM4TcProtoHistInDiscards_Type = Gauge32
_PdnAtmfM4TcProtoHistInDiscards_Object = MibTableColumn
pdnAtmfM4TcProtoHistInDiscards = _PdnAtmfM4TcProtoHistInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 2, 1, 3),
    _PdnAtmfM4TcProtoHistInDiscards_Type()
)
pdnAtmfM4TcProtoHistInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoHistInDiscards.setStatus("current")
_PdnAtmfM4TcProtoHistOutDiscards_Type = Gauge32
_PdnAtmfM4TcProtoHistOutDiscards_Object = MibTableColumn
pdnAtmfM4TcProtoHistOutDiscards = _PdnAtmfM4TcProtoHistOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 2, 1, 4),
    _PdnAtmfM4TcProtoHistOutDiscards_Type()
)
pdnAtmfM4TcProtoHistOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoHistOutDiscards.setStatus("current")
_PdnAtmfM4TcProtoHistLCDEvents_Type = Gauge32
_PdnAtmfM4TcProtoHistLCDEvents_Object = MibTableColumn
pdnAtmfM4TcProtoHistLCDEvents = _PdnAtmfM4TcProtoHistLCDEvents_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 2, 1, 5),
    _PdnAtmfM4TcProtoHistLCDEvents_Type()
)
pdnAtmfM4TcProtoHistLCDEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoHistLCDEvents.setStatus("current")
_PdnAtmfM4TcProtoHistUnknownCells_Type = Gauge32
_PdnAtmfM4TcProtoHistUnknownCells_Object = MibTableColumn
pdnAtmfM4TcProtoHistUnknownCells = _PdnAtmfM4TcProtoHistUnknownCells_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 2, 1, 6),
    _PdnAtmfM4TcProtoHistUnknownCells_Type()
)
pdnAtmfM4TcProtoHistUnknownCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoHistUnknownCells.setStatus("current")
_PdnAtmfM4TcProtoHistCorrectedHEC_Type = Gauge32
_PdnAtmfM4TcProtoHistCorrectedHEC_Object = MibTableColumn
pdnAtmfM4TcProtoHistCorrectedHEC = _PdnAtmfM4TcProtoHistCorrectedHEC_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 2, 1, 7),
    _PdnAtmfM4TcProtoHistCorrectedHEC_Type()
)
pdnAtmfM4TcProtoHistCorrectedHEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4TcProtoHistCorrectedHEC.setStatus("current")
_PdnAtmfM4TestTypes_ObjectIdentity = ObjectIdentity
pdnAtmfM4TestTypes = _PdnAtmfM4TestTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 3)
)
_PdnAtmfM4TestOAMLoopbackSegMultiCell_ObjectIdentity = ObjectIdentity
pdnAtmfM4TestOAMLoopbackSegMultiCell = _PdnAtmfM4TestOAMLoopbackSegMultiCell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pdnAtmfM4TestOAMLoopbackSegMultiCell.setStatus("current")
_PdnAtmfM4TestOAMLoopbackE2EMultiCell_ObjectIdentity = ObjectIdentity
pdnAtmfM4TestOAMLoopbackE2EMultiCell = _PdnAtmfM4TestOAMLoopbackE2EMultiCell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    pdnAtmfM4TestOAMLoopbackE2EMultiCell.setStatus("current")
_PdnAtmfM4VcLoopbackTestTable_Object = MibTable
pdnAtmfM4VcLoopbackTestTable = _PdnAtmfM4VcLoopbackTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 4)
)
if mibBuilder.loadTexts:
    pdnAtmfM4VcLoopbackTestTable.setStatus("current")
_PdnAtmfM4VcLoopbackTestEntry_Object = MibTableRow
pdnAtmfM4VcLoopbackTestEntry = _PdnAtmfM4VcLoopbackTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pdnAtmfM4VcLoopbackTestEntry.setStatus("current")
_PdnAtmfM4VcLoopbackTestElpsTime_Type = TimeTicks
_PdnAtmfM4VcLoopbackTestElpsTime_Object = MibTableColumn
pdnAtmfM4VcLoopbackTestElpsTime = _PdnAtmfM4VcLoopbackTestElpsTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 4, 1, 1),
    _PdnAtmfM4VcLoopbackTestElpsTime_Type()
)
pdnAtmfM4VcLoopbackTestElpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4VcLoopbackTestElpsTime.setStatus("current")
_PdnAtmfM4VcLoopbackTestCellsSent_Type = Gauge32
_PdnAtmfM4VcLoopbackTestCellsSent_Object = MibTableColumn
pdnAtmfM4VcLoopbackTestCellsSent = _PdnAtmfM4VcLoopbackTestCellsSent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 4, 1, 2),
    _PdnAtmfM4VcLoopbackTestCellsSent_Type()
)
pdnAtmfM4VcLoopbackTestCellsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4VcLoopbackTestCellsSent.setStatus("current")
_PdnAtmfM4VcLoopbackTestCellsRcvd_Type = Gauge32
_PdnAtmfM4VcLoopbackTestCellsRcvd_Object = MibTableColumn
pdnAtmfM4VcLoopbackTestCellsRcvd = _PdnAtmfM4VcLoopbackTestCellsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 4, 1, 3),
    _PdnAtmfM4VcLoopbackTestCellsRcvd_Type()
)
pdnAtmfM4VcLoopbackTestCellsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4VcLoopbackTestCellsRcvd.setStatus("current")
_PdnAtmfM4VcLoopbackTestMinRTDelay_Type = Gauge32
_PdnAtmfM4VcLoopbackTestMinRTDelay_Object = MibTableColumn
pdnAtmfM4VcLoopbackTestMinRTDelay = _PdnAtmfM4VcLoopbackTestMinRTDelay_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 4, 1, 4),
    _PdnAtmfM4VcLoopbackTestMinRTDelay_Type()
)
pdnAtmfM4VcLoopbackTestMinRTDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4VcLoopbackTestMinRTDelay.setStatus("current")
if mibBuilder.loadTexts:
    pdnAtmfM4VcLoopbackTestMinRTDelay.setUnits("milliseconds")
_PdnAtmfM4VcLoopbackTestMaxRTDelay_Type = Gauge32
_PdnAtmfM4VcLoopbackTestMaxRTDelay_Object = MibTableColumn
pdnAtmfM4VcLoopbackTestMaxRTDelay = _PdnAtmfM4VcLoopbackTestMaxRTDelay_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 4, 1, 5),
    _PdnAtmfM4VcLoopbackTestMaxRTDelay_Type()
)
pdnAtmfM4VcLoopbackTestMaxRTDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4VcLoopbackTestMaxRTDelay.setStatus("current")
if mibBuilder.loadTexts:
    pdnAtmfM4VcLoopbackTestMaxRTDelay.setUnits("milliseconds")
_PdnAtmfM4VcLoopbackTestAvgRTDelay_Type = Gauge32
_PdnAtmfM4VcLoopbackTestAvgRTDelay_Object = MibTableColumn
pdnAtmfM4VcLoopbackTestAvgRTDelay = _PdnAtmfM4VcLoopbackTestAvgRTDelay_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 4, 1, 6),
    _PdnAtmfM4VcLoopbackTestAvgRTDelay_Type()
)
pdnAtmfM4VcLoopbackTestAvgRTDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4VcLoopbackTestAvgRTDelay.setStatus("current")
if mibBuilder.loadTexts:
    pdnAtmfM4VcLoopbackTestAvgRTDelay.setUnits("milliseconds")
_PdnAtmfM4VcLoopbackTestErrorCode_Type = PdnAtmfM4TestErrorCode
_PdnAtmfM4VcLoopbackTestErrorCode_Object = MibTableColumn
pdnAtmfM4VcLoopbackTestErrorCode = _PdnAtmfM4VcLoopbackTestErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 4, 1, 7),
    _PdnAtmfM4VcLoopbackTestErrorCode_Type()
)
pdnAtmfM4VcLoopbackTestErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4VcLoopbackTestErrorCode.setStatus("current")
_PdnAtmfM4Vc1CellLoopTable_Object = MibTable
pdnAtmfM4Vc1CellLoopTable = _PdnAtmfM4Vc1CellLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 5)
)
if mibBuilder.loadTexts:
    pdnAtmfM4Vc1CellLoopTable.setStatus("current")
_PdnAtmfM4Vc1CellLoopEntry_Object = MibTableRow
pdnAtmfM4Vc1CellLoopEntry = _PdnAtmfM4Vc1CellLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    pdnAtmfM4Vc1CellLoopEntry.setStatus("current")
_PdnAtmfM4Vc1CellLoopRTDelay_Type = Gauge32
_PdnAtmfM4Vc1CellLoopRTDelay_Object = MibTableColumn
pdnAtmfM4Vc1CellLoopRTDelay = _PdnAtmfM4Vc1CellLoopRTDelay_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 5, 1, 1),
    _PdnAtmfM4Vc1CellLoopRTDelay_Type()
)
pdnAtmfM4Vc1CellLoopRTDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4Vc1CellLoopRTDelay.setStatus("current")
if mibBuilder.loadTexts:
    pdnAtmfM4Vc1CellLoopRTDelay.setUnits("milliseconds")


class _PdnAtmfM4Vc1CellLoopReportedLocation_Type(OctetString):
    """Custom type pdnAtmfM4Vc1CellLoopReportedLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_PdnAtmfM4Vc1CellLoopReportedLocation_Type.__name__ = "OctetString"
_PdnAtmfM4Vc1CellLoopReportedLocation_Object = MibTableColumn
pdnAtmfM4Vc1CellLoopReportedLocation = _PdnAtmfM4Vc1CellLoopReportedLocation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 5, 1, 2),
    _PdnAtmfM4Vc1CellLoopReportedLocation_Type()
)
pdnAtmfM4Vc1CellLoopReportedLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4Vc1CellLoopReportedLocation.setStatus("current")
_PdnAtmfM4Vc1CellLoopErrorCode_Type = PdnAtmfM4TestErrorCode
_PdnAtmfM4Vc1CellLoopErrorCode_Object = MibTableColumn
pdnAtmfM4Vc1CellLoopErrorCode = _PdnAtmfM4Vc1CellLoopErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 5, 1, 3),
    _PdnAtmfM4Vc1CellLoopErrorCode_Type()
)
pdnAtmfM4Vc1CellLoopErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4Vc1CellLoopErrorCode.setStatus("current")
_PdnAtmfM4LoopbackLocationTable_Object = MibTable
pdnAtmfM4LoopbackLocationTable = _PdnAtmfM4LoopbackLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 6)
)
if mibBuilder.loadTexts:
    pdnAtmfM4LoopbackLocationTable.setStatus("current")
_PdnAtmfM4LoopbackLocationEntry_Object = MibTableRow
pdnAtmfM4LoopbackLocationEntry = _PdnAtmfM4LoopbackLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 6, 1)
)
pdnAtmfM4LoopbackLocationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnAtmfM4LoopbackLocationEntry.setStatus("current")


class _PdnAtmfM4LoopbackLocationCode_Type(OctetString):
    """Custom type pdnAtmfM4LoopbackLocationCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_PdnAtmfM4LoopbackLocationCode_Type.__name__ = "OctetString"
_PdnAtmfM4LoopbackLocationCode_Object = MibTableColumn
pdnAtmfM4LoopbackLocationCode = _PdnAtmfM4LoopbackLocationCode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 6, 1, 1),
    _PdnAtmfM4LoopbackLocationCode_Type()
)
pdnAtmfM4LoopbackLocationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAtmfM4LoopbackLocationCode.setStatus("current")
_PdnAtmfM4VpLoopbackTestTable_Object = MibTable
pdnAtmfM4VpLoopbackTestTable = _PdnAtmfM4VpLoopbackTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 7)
)
if mibBuilder.loadTexts:
    pdnAtmfM4VpLoopbackTestTable.setStatus("current")
_PdnAtmfM4VpLoopbackTestEntry_Object = MibTableRow
pdnAtmfM4VpLoopbackTestEntry = _PdnAtmfM4VpLoopbackTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 7, 1)
)
if mibBuilder.loadTexts:
    pdnAtmfM4VpLoopbackTestEntry.setStatus("current")
_PdnAtmfM4VpLoopbackTestElpsTime_Type = TimeTicks
_PdnAtmfM4VpLoopbackTestElpsTime_Object = MibTableColumn
pdnAtmfM4VpLoopbackTestElpsTime = _PdnAtmfM4VpLoopbackTestElpsTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 7, 1, 1),
    _PdnAtmfM4VpLoopbackTestElpsTime_Type()
)
pdnAtmfM4VpLoopbackTestElpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4VpLoopbackTestElpsTime.setStatus("current")
_PdnAtmfM4VpLoopbackTestCellsSent_Type = Gauge32
_PdnAtmfM4VpLoopbackTestCellsSent_Object = MibTableColumn
pdnAtmfM4VpLoopbackTestCellsSent = _PdnAtmfM4VpLoopbackTestCellsSent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 7, 1, 2),
    _PdnAtmfM4VpLoopbackTestCellsSent_Type()
)
pdnAtmfM4VpLoopbackTestCellsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4VpLoopbackTestCellsSent.setStatus("current")
_PdnAtmfM4VpLoopbackTestCellsRcvd_Type = Gauge32
_PdnAtmfM4VpLoopbackTestCellsRcvd_Object = MibTableColumn
pdnAtmfM4VpLoopbackTestCellsRcvd = _PdnAtmfM4VpLoopbackTestCellsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 7, 1, 3),
    _PdnAtmfM4VpLoopbackTestCellsRcvd_Type()
)
pdnAtmfM4VpLoopbackTestCellsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4VpLoopbackTestCellsRcvd.setStatus("current")
_PdnAtmfM4VpLoopbackTestMinRTDelay_Type = Gauge32
_PdnAtmfM4VpLoopbackTestMinRTDelay_Object = MibTableColumn
pdnAtmfM4VpLoopbackTestMinRTDelay = _PdnAtmfM4VpLoopbackTestMinRTDelay_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 7, 1, 4),
    _PdnAtmfM4VpLoopbackTestMinRTDelay_Type()
)
pdnAtmfM4VpLoopbackTestMinRTDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4VpLoopbackTestMinRTDelay.setStatus("current")
if mibBuilder.loadTexts:
    pdnAtmfM4VpLoopbackTestMinRTDelay.setUnits("milliseconds")
_PdnAtmfM4VpLoopbackTestMaxRTDelay_Type = Gauge32
_PdnAtmfM4VpLoopbackTestMaxRTDelay_Object = MibTableColumn
pdnAtmfM4VpLoopbackTestMaxRTDelay = _PdnAtmfM4VpLoopbackTestMaxRTDelay_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 7, 1, 5),
    _PdnAtmfM4VpLoopbackTestMaxRTDelay_Type()
)
pdnAtmfM4VpLoopbackTestMaxRTDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4VpLoopbackTestMaxRTDelay.setStatus("current")
if mibBuilder.loadTexts:
    pdnAtmfM4VpLoopbackTestMaxRTDelay.setUnits("milliseconds")
_PdnAtmfM4VpLoopbackTestAvgRTDelay_Type = Gauge32
_PdnAtmfM4VpLoopbackTestAvgRTDelay_Object = MibTableColumn
pdnAtmfM4VpLoopbackTestAvgRTDelay = _PdnAtmfM4VpLoopbackTestAvgRTDelay_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 7, 1, 6),
    _PdnAtmfM4VpLoopbackTestAvgRTDelay_Type()
)
pdnAtmfM4VpLoopbackTestAvgRTDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4VpLoopbackTestAvgRTDelay.setStatus("current")
if mibBuilder.loadTexts:
    pdnAtmfM4VpLoopbackTestAvgRTDelay.setUnits("milliseconds")
_PdnAtmfM4VpLoopbackTestErrorCode_Type = PdnAtmfM4TestErrorCode
_PdnAtmfM4VpLoopbackTestErrorCode_Object = MibTableColumn
pdnAtmfM4VpLoopbackTestErrorCode = _PdnAtmfM4VpLoopbackTestErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 1, 7, 1, 7),
    _PdnAtmfM4VpLoopbackTestErrorCode_Type()
)
pdnAtmfM4VpLoopbackTestErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAtmfM4VpLoopbackTestErrorCode.setStatus("current")
_PdnAtmfM4ExtTraps_ObjectIdentity = ObjectIdentity
pdnAtmfM4ExtTraps = _PdnAtmfM4ExtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 2)
)
_PdnAtmfM4ExtTrapPrefix_ObjectIdentity = ObjectIdentity
pdnAtmfM4ExtTrapPrefix = _PdnAtmfM4ExtTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 2, 0)
)
_PdnAtmfM4ExtConformance_ObjectIdentity = ObjectIdentity
pdnAtmfM4ExtConformance = _PdnAtmfM4ExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 3)
)
_PdnAtmfM4Groups_ObjectIdentity = ObjectIdentity
pdnAtmfM4Groups = _PdnAtmfM4Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 3, 1)
)
_PdnAtmfM4Compliances_ObjectIdentity = ObjectIdentity
pdnAtmfM4Compliances = _PdnAtmfM4Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 3, 2)
)
atmfM4TcProtoCurrEntry.registerAugmentions(
    ("PDN-ATMM4EXT-MIB",
     "pdnAtmfM4TcProtoCurrExtEntry")
)
pdnAtmfM4TcProtoCurrExtEntry.setIndexNames(*atmfM4TcProtoCurrEntry.getIndexNames())
atmfM4TcProtoHistEntry.registerAugmentions(
    ("PDN-ATMM4EXT-MIB",
     "pdnAtmfM4TcProtoHistExtEntry")
)
pdnAtmfM4TcProtoHistExtEntry.setIndexNames(*atmfM4TcProtoHistEntry.getIndexNames())
atmfM4VcTestEntry.registerAugmentions(
    ("PDN-ATMM4EXT-MIB",
     "pdnAtmfM4VcLoopbackTestEntry")
)
pdnAtmfM4VcLoopbackTestEntry.setIndexNames(*atmfM4VcTestEntry.getIndexNames())
atmfM4VcTestEntry.registerAugmentions(
    ("PDN-ATMM4EXT-MIB",
     "pdnAtmfM4Vc1CellLoopEntry")
)
pdnAtmfM4Vc1CellLoopEntry.setIndexNames(*atmfM4VcTestEntry.getIndexNames())
atmfM4VpTestEntry.registerAugmentions(
    ("PDN-ATMM4EXT-MIB",
     "pdnAtmfM4VpLoopbackTestEntry")
)
pdnAtmfM4VpLoopbackTestEntry.setIndexNames(*atmfM4VpTestEntry.getIndexNames())

# Managed Objects groups

pdnAtmfM4TcCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 3, 1, 1)
)
pdnAtmfM4TcCurrGroup.setObjects(
      *(("PDN-ATMM4EXT-MIB", "pdnAtmfM4TcProtoCurrCellIns"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4TcProtoCurrCellOuts"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4TcProtoCurrInDiscards"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4TcProtoCurrOutDiscards"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4TcProtoCurrLCDEvents"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4TcProtoCurrUnknownCells"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4TcProtoCurrCorrectedHEC"))
)
if mibBuilder.loadTexts:
    pdnAtmfM4TcCurrGroup.setStatus("current")

pdnAtmfM4TcHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 3, 1, 2)
)
pdnAtmfM4TcHistGroup.setObjects(
      *(("PDN-ATMM4EXT-MIB", "pdnAtmfM4TcProtoHistCellIns"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4TcProtoHistCellOuts"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4TcProtoHistInDiscards"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4TcProtoHistOutDiscards"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4TcProtoHistLCDEvents"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4TcProtoHistUnknownCells"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4TcProtoHistCorrectedHEC"))
)
if mibBuilder.loadTexts:
    pdnAtmfM4TcHistGroup.setStatus("current")

pdnAtmfM4VcLoopbackTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 3, 1, 3)
)
pdnAtmfM4VcLoopbackTestGroup.setObjects(
      *(("PDN-ATMM4EXT-MIB", "pdnAtmfM4VcLoopbackTestElpsTime"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4VcLoopbackTestCellsSent"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4VcLoopbackTestCellsRcvd"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4VcLoopbackTestMinRTDelay"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4VcLoopbackTestMaxRTDelay"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4VcLoopbackTestAvgRTDelay"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4VcLoopbackTestErrorCode"))
)
if mibBuilder.loadTexts:
    pdnAtmfM4VcLoopbackTestGroup.setStatus("current")

pdnAtmfM4Vc1CellLoopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 3, 1, 4)
)
pdnAtmfM4Vc1CellLoopGroup.setObjects(
      *(("PDN-ATMM4EXT-MIB", "pdnAtmfM4Vc1CellLoopRTDelay"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4Vc1CellLoopReportedLocation"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4Vc1CellLoopErrorCode"))
)
if mibBuilder.loadTexts:
    pdnAtmfM4Vc1CellLoopGroup.setStatus("current")

pdnAtmfM4LoopbackLocationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 3, 1, 5)
)
pdnAtmfM4LoopbackLocationGroup.setObjects(
    ("PDN-ATMM4EXT-MIB", "pdnAtmfM4LoopbackLocationCode")
)
if mibBuilder.loadTexts:
    pdnAtmfM4LoopbackLocationGroup.setStatus("current")

pdnAtmfM4VpLoopbackTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 3, 1, 6)
)
pdnAtmfM4VpLoopbackTestGroup.setObjects(
      *(("PDN-ATMM4EXT-MIB", "pdnAtmfM4VpLoopbackTestElpsTime"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4VpLoopbackTestCellsSent"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4VpLoopbackTestCellsRcvd"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4VpLoopbackTestMinRTDelay"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4VpLoopbackTestMaxRTDelay"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4VpLoopbackTestAvgRTDelay"),
        ("PDN-ATMM4EXT-MIB", "pdnAtmfM4VpLoopbackTestErrorCode"))
)
if mibBuilder.loadTexts:
    pdnAtmfM4VpLoopbackTestGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnAtmfM4Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    pdnAtmfM4Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-ATMM4EXT-MIB",
    **{"PdnAtmfM4TestErrorCode": PdnAtmfM4TestErrorCode,
       "pdnAtmfM4ExtMIB": pdnAtmfM4ExtMIB,
       "pdnAtmfM4ExtObjects": pdnAtmfM4ExtObjects,
       "pdnAtmfM4TcProtoCurrExtTable": pdnAtmfM4TcProtoCurrExtTable,
       "pdnAtmfM4TcProtoCurrExtEntry": pdnAtmfM4TcProtoCurrExtEntry,
       "pdnAtmfM4TcProtoCurrCellIns": pdnAtmfM4TcProtoCurrCellIns,
       "pdnAtmfM4TcProtoCurrCellOuts": pdnAtmfM4TcProtoCurrCellOuts,
       "pdnAtmfM4TcProtoCurrInDiscards": pdnAtmfM4TcProtoCurrInDiscards,
       "pdnAtmfM4TcProtoCurrOutDiscards": pdnAtmfM4TcProtoCurrOutDiscards,
       "pdnAtmfM4TcProtoCurrLCDEvents": pdnAtmfM4TcProtoCurrLCDEvents,
       "pdnAtmfM4TcProtoCurrUnknownCells": pdnAtmfM4TcProtoCurrUnknownCells,
       "pdnAtmfM4TcProtoCurrCorrectedHEC": pdnAtmfM4TcProtoCurrCorrectedHEC,
       "pdnAtmfM4TcProtoHistExtTable": pdnAtmfM4TcProtoHistExtTable,
       "pdnAtmfM4TcProtoHistExtEntry": pdnAtmfM4TcProtoHistExtEntry,
       "pdnAtmfM4TcProtoHistCellIns": pdnAtmfM4TcProtoHistCellIns,
       "pdnAtmfM4TcProtoHistCellOuts": pdnAtmfM4TcProtoHistCellOuts,
       "pdnAtmfM4TcProtoHistInDiscards": pdnAtmfM4TcProtoHistInDiscards,
       "pdnAtmfM4TcProtoHistOutDiscards": pdnAtmfM4TcProtoHistOutDiscards,
       "pdnAtmfM4TcProtoHistLCDEvents": pdnAtmfM4TcProtoHistLCDEvents,
       "pdnAtmfM4TcProtoHistUnknownCells": pdnAtmfM4TcProtoHistUnknownCells,
       "pdnAtmfM4TcProtoHistCorrectedHEC": pdnAtmfM4TcProtoHistCorrectedHEC,
       "pdnAtmfM4TestTypes": pdnAtmfM4TestTypes,
       "pdnAtmfM4TestOAMLoopbackSegMultiCell": pdnAtmfM4TestOAMLoopbackSegMultiCell,
       "pdnAtmfM4TestOAMLoopbackE2EMultiCell": pdnAtmfM4TestOAMLoopbackE2EMultiCell,
       "pdnAtmfM4VcLoopbackTestTable": pdnAtmfM4VcLoopbackTestTable,
       "pdnAtmfM4VcLoopbackTestEntry": pdnAtmfM4VcLoopbackTestEntry,
       "pdnAtmfM4VcLoopbackTestElpsTime": pdnAtmfM4VcLoopbackTestElpsTime,
       "pdnAtmfM4VcLoopbackTestCellsSent": pdnAtmfM4VcLoopbackTestCellsSent,
       "pdnAtmfM4VcLoopbackTestCellsRcvd": pdnAtmfM4VcLoopbackTestCellsRcvd,
       "pdnAtmfM4VcLoopbackTestMinRTDelay": pdnAtmfM4VcLoopbackTestMinRTDelay,
       "pdnAtmfM4VcLoopbackTestMaxRTDelay": pdnAtmfM4VcLoopbackTestMaxRTDelay,
       "pdnAtmfM4VcLoopbackTestAvgRTDelay": pdnAtmfM4VcLoopbackTestAvgRTDelay,
       "pdnAtmfM4VcLoopbackTestErrorCode": pdnAtmfM4VcLoopbackTestErrorCode,
       "pdnAtmfM4Vc1CellLoopTable": pdnAtmfM4Vc1CellLoopTable,
       "pdnAtmfM4Vc1CellLoopEntry": pdnAtmfM4Vc1CellLoopEntry,
       "pdnAtmfM4Vc1CellLoopRTDelay": pdnAtmfM4Vc1CellLoopRTDelay,
       "pdnAtmfM4Vc1CellLoopReportedLocation": pdnAtmfM4Vc1CellLoopReportedLocation,
       "pdnAtmfM4Vc1CellLoopErrorCode": pdnAtmfM4Vc1CellLoopErrorCode,
       "pdnAtmfM4LoopbackLocationTable": pdnAtmfM4LoopbackLocationTable,
       "pdnAtmfM4LoopbackLocationEntry": pdnAtmfM4LoopbackLocationEntry,
       "pdnAtmfM4LoopbackLocationCode": pdnAtmfM4LoopbackLocationCode,
       "pdnAtmfM4VpLoopbackTestTable": pdnAtmfM4VpLoopbackTestTable,
       "pdnAtmfM4VpLoopbackTestEntry": pdnAtmfM4VpLoopbackTestEntry,
       "pdnAtmfM4VpLoopbackTestElpsTime": pdnAtmfM4VpLoopbackTestElpsTime,
       "pdnAtmfM4VpLoopbackTestCellsSent": pdnAtmfM4VpLoopbackTestCellsSent,
       "pdnAtmfM4VpLoopbackTestCellsRcvd": pdnAtmfM4VpLoopbackTestCellsRcvd,
       "pdnAtmfM4VpLoopbackTestMinRTDelay": pdnAtmfM4VpLoopbackTestMinRTDelay,
       "pdnAtmfM4VpLoopbackTestMaxRTDelay": pdnAtmfM4VpLoopbackTestMaxRTDelay,
       "pdnAtmfM4VpLoopbackTestAvgRTDelay": pdnAtmfM4VpLoopbackTestAvgRTDelay,
       "pdnAtmfM4VpLoopbackTestErrorCode": pdnAtmfM4VpLoopbackTestErrorCode,
       "pdnAtmfM4ExtTraps": pdnAtmfM4ExtTraps,
       "pdnAtmfM4ExtTrapPrefix": pdnAtmfM4ExtTrapPrefix,
       "pdnAtmfM4ExtConformance": pdnAtmfM4ExtConformance,
       "pdnAtmfM4Groups": pdnAtmfM4Groups,
       "pdnAtmfM4TcCurrGroup": pdnAtmfM4TcCurrGroup,
       "pdnAtmfM4TcHistGroup": pdnAtmfM4TcHistGroup,
       "pdnAtmfM4VcLoopbackTestGroup": pdnAtmfM4VcLoopbackTestGroup,
       "pdnAtmfM4Vc1CellLoopGroup": pdnAtmfM4Vc1CellLoopGroup,
       "pdnAtmfM4LoopbackLocationGroup": pdnAtmfM4LoopbackLocationGroup,
       "pdnAtmfM4VpLoopbackTestGroup": pdnAtmfM4VpLoopbackTestGroup,
       "pdnAtmfM4Compliances": pdnAtmfM4Compliances,
       "pdnAtmfM4Compliance": pdnAtmfM4Compliance}
)
