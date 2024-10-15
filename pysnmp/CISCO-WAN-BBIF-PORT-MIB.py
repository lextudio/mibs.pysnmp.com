# SNMP MIB module (CISCO-WAN-BBIF-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-BBIF-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:55 2024
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

(bbIfCnf,
 bbIfCnt,
 bbIfStateGrp) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "bbIfCnf",
    "bbIfCnt",
    "bbIfStateGrp")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoWanBbifPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 32)
)
ciscoWanBbifPortMIB.setRevisions(
        ("2002-08-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BbIfCnfPortGrp_ObjectIdentity = ObjectIdentity
bbIfCnfPortGrp = _BbIfCnfPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 1)
)
_BbIfCnfPortGrpTable_Object = MibTable
bbIfCnfPortGrpTable = _BbIfCnfPortGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    bbIfCnfPortGrpTable.setStatus("current")
_BbIfCnfPortGrpEntry_Object = MibTableRow
bbIfCnfPortGrpEntry = _BbIfCnfPortGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 1, 1, 1)
)
bbIfCnfPortGrpEntry.setIndexNames(
    (0, "CISCO-WAN-BBIF-PORT-MIB", "bbIfNum"),
)
if mibBuilder.loadTexts:
    bbIfCnfPortGrpEntry.setStatus("current")


class _BbIfNum_Type(Integer32):
    """Custom type bbIfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BbIfNum_Type.__name__ = "Integer32"
_BbIfNum_Object = MibTableColumn
bbIfNum = _BbIfNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 1, 1, 1, 1),
    _BbIfNum_Type()
)
bbIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfNum.setStatus("current")


class _BbIfRowStatus_Type(Integer32):
    """Custom type bbIfRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 2),
          ("mod", 3))
    )


_BbIfRowStatus_Type.__name__ = "Integer32"
_BbIfRowStatus_Object = MibTableColumn
bbIfRowStatus = _BbIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 1, 1, 1, 2),
    _BbIfRowStatus_Type()
)
bbIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfRowStatus.setStatus("current")


class _BbIfAdmin_Type(Integer32):
    """Custom type bbIfAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1),
          ("writeOnly", 3))
    )


_BbIfAdmin_Type.__name__ = "Integer32"
_BbIfAdmin_Object = MibTableColumn
bbIfAdmin = _BbIfAdmin_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 1, 1, 1, 3),
    _BbIfAdmin_Type()
)
bbIfAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfAdmin.setStatus("current")


class _BbIfLineNum_Type(Integer32):
    """Custom type bbIfLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BbIfLineNum_Type.__name__ = "Integer32"
_BbIfLineNum_Object = MibTableColumn
bbIfLineNum = _BbIfLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 1, 1, 1, 4),
    _BbIfLineNum_Type()
)
bbIfLineNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfLineNum.setStatus("current")


class _BbIfIngrPctBandwidth_Type(Integer32):
    """Custom type bbIfIngrPctBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BbIfIngrPctBandwidth_Type.__name__ = "Integer32"
_BbIfIngrPctBandwidth_Object = MibTableColumn
bbIfIngrPctBandwidth = _BbIfIngrPctBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 1, 1, 1, 5),
    _BbIfIngrPctBandwidth_Type()
)
bbIfIngrPctBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfIngrPctBandwidth.setStatus("current")


class _BbIfEgrPctBandwidth_Type(Integer32):
    """Custom type bbIfEgrPctBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BbIfEgrPctBandwidth_Type.__name__ = "Integer32"
_BbIfEgrPctBandwidth_Object = MibTableColumn
bbIfEgrPctBandwidth = _BbIfEgrPctBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 1, 1, 1, 6),
    _BbIfEgrPctBandwidth_Type()
)
bbIfEgrPctBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfEgrPctBandwidth.setStatus("current")


class _BbIfMinVpi_Type(Integer32):
    """Custom type bbIfMinVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_BbIfMinVpi_Type.__name__ = "Integer32"
_BbIfMinVpi_Object = MibTableColumn
bbIfMinVpi = _BbIfMinVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 1, 1, 1, 7),
    _BbIfMinVpi_Type()
)
bbIfMinVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfMinVpi.setStatus("current")


class _BbIfMaxVpi_Type(Integer32):
    """Custom type bbIfMaxVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_BbIfMaxVpi_Type.__name__ = "Integer32"
_BbIfMaxVpi_Object = MibTableColumn
bbIfMaxVpi = _BbIfMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 1, 1, 1, 8),
    _BbIfMaxVpi_Type()
)
bbIfMaxVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfMaxVpi.setStatus("current")
_BbIfSpeed_Type = Integer32
_BbIfSpeed_Object = MibTableColumn
bbIfSpeed = _BbIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 1, 1, 1, 9),
    _BbIfSpeed_Type()
)
bbIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfSpeed.setStatus("current")


class _BbIfMaxCellRatePct_Type(Integer32):
    """Custom type bbIfMaxCellRatePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BbIfMaxCellRatePct_Type.__name__ = "Integer32"
_BbIfMaxCellRatePct_Object = MibTableColumn
bbIfMaxCellRatePct = _BbIfMaxCellRatePct_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 1, 1, 1, 10),
    _BbIfMaxCellRatePct_Type()
)
bbIfMaxCellRatePct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfMaxCellRatePct.setStatus("current")


class _NextBbIfNumAvailable_Type(Integer32):
    """Custom type nextBbIfNumAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_NextBbIfNumAvailable_Type.__name__ = "Integer32"
_NextBbIfNumAvailable_Object = MibScalar
nextBbIfNumAvailable = _NextBbIfNumAvailable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1, 1, 2),
    _NextBbIfNumAvailable_Type()
)
nextBbIfNumAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextBbIfNumAvailable.setStatus("current")
_BbIfStateGrpTable_Object = MibTable
bbIfStateGrpTable = _BbIfStateGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    bbIfStateGrpTable.setStatus("current")
_BbIfStateGrpEntry_Object = MibTableRow
bbIfStateGrpEntry = _BbIfStateGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 3, 1, 1)
)
bbIfStateGrpEntry.setIndexNames(
    (0, "CISCO-WAN-BBIF-PORT-MIB", "bbStateIfNum"),
)
if mibBuilder.loadTexts:
    bbIfStateGrpEntry.setStatus("current")


class _BbStateIfNum_Type(Integer32):
    """Custom type bbStateIfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BbStateIfNum_Type.__name__ = "Integer32"
_BbStateIfNum_Object = MibTableColumn
bbStateIfNum = _BbStateIfNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 3, 1, 1, 1),
    _BbStateIfNum_Type()
)
bbStateIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbStateIfNum.setStatus("current")


class _BbIfState_Type(Integer32):
    """Custom type bbIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 6),
          ("linefailure", 4),
          ("lineinloopback", 7),
          ("notConfigured", 1),
          ("signallingfailure", 5))
    )


_BbIfState_Type.__name__ = "Integer32"
_BbIfState_Object = MibTableColumn
bbIfState = _BbIfState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 3, 1, 1, 2),
    _BbIfState_Type()
)
bbIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfState.setStatus("current")


class _BbIfOversubscribed_Type(Integer32):
    """Custom type bbIfOversubscribed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_BbIfOversubscribed_Type.__name__ = "Integer32"
_BbIfOversubscribed_Object = MibTableColumn
bbIfOversubscribed = _BbIfOversubscribed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 3, 1, 1, 3),
    _BbIfOversubscribed_Type()
)
bbIfOversubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfOversubscribed.setStatus("current")


class _BbIfIngrPercentUtil_Type(Integer32):
    """Custom type bbIfIngrPercentUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_BbIfIngrPercentUtil_Type.__name__ = "Integer32"
_BbIfIngrPercentUtil_Object = MibTableColumn
bbIfIngrPercentUtil = _BbIfIngrPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 3, 1, 1, 4),
    _BbIfIngrPercentUtil_Type()
)
bbIfIngrPercentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfIngrPercentUtil.setStatus("current")


class _BbIfEgrPercentUtil_Type(Integer32):
    """Custom type bbIfEgrPercentUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_BbIfEgrPercentUtil_Type.__name__ = "Integer32"
_BbIfEgrPercentUtil_Object = MibTableColumn
bbIfEgrPercentUtil = _BbIfEgrPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 3, 1, 1, 5),
    _BbIfEgrPercentUtil_Type()
)
bbIfEgrPercentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfEgrPercentUtil.setStatus("current")
_BbIfCntGrp_ObjectIdentity = ObjectIdentity
bbIfCntGrp = _BbIfCntGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1)
)
_BbIfCntGrpTable_Object = MibTable
bbIfCntGrpTable = _BbIfCntGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    bbIfCntGrpTable.setStatus("current")
_BbIfCntGrpEntry_Object = MibTableRow
bbIfCntGrpEntry = _BbIfCntGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1)
)
bbIfCntGrpEntry.setIndexNames(
    (0, "CISCO-WAN-BBIF-PORT-MIB", "bbCntIfNum"),
)
if mibBuilder.loadTexts:
    bbIfCntGrpEntry.setStatus("current")


class _BbCntIfNum_Type(Integer32):
    """Custom type bbCntIfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BbCntIfNum_Type.__name__ = "Integer32"
_BbCntIfNum_Object = MibTableColumn
bbCntIfNum = _BbCntIfNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1, 1),
    _BbCntIfNum_Type()
)
bbCntIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbCntIfNum.setStatus("current")
_BbIfTotalCells_Type = Counter32
_BbIfTotalCells_Object = MibTableColumn
bbIfTotalCells = _BbIfTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1, 2),
    _BbIfTotalCells_Type()
)
bbIfTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfTotalCells.setStatus("current")
_BbIfRcvValidOAMCells_Type = Counter32
_BbIfRcvValidOAMCells_Object = MibTableColumn
bbIfRcvValidOAMCells = _BbIfRcvValidOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1, 3),
    _BbIfRcvValidOAMCells_Type()
)
bbIfRcvValidOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfRcvValidOAMCells.setStatus("current")
_BbIfRcvRmCells_Type = Counter32
_BbIfRcvRmCells_Object = MibTableColumn
bbIfRcvRmCells = _BbIfRcvRmCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1, 4),
    _BbIfRcvRmCells_Type()
)
bbIfRcvRmCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfRcvRmCells.setStatus("current")
_BbIfRcvClp0Cells_Type = Counter32
_BbIfRcvClp0Cells_Object = MibTableColumn
bbIfRcvClp0Cells = _BbIfRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1, 5),
    _BbIfRcvClp0Cells_Type()
)
bbIfRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfRcvClp0Cells.setStatus("current")
_BbIfRcvClp1Cells_Type = Counter32
_BbIfRcvClp1Cells_Object = MibTableColumn
bbIfRcvClp1Cells = _BbIfRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1, 6),
    _BbIfRcvClp1Cells_Type()
)
bbIfRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfRcvClp1Cells.setStatus("current")
_BbIfRcvClp0DiscCells_Type = Counter32
_BbIfRcvClp0DiscCells_Object = MibTableColumn
bbIfRcvClp0DiscCells = _BbIfRcvClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1, 7),
    _BbIfRcvClp0DiscCells_Type()
)
bbIfRcvClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfRcvClp0DiscCells.setStatus("current")
_BbIfRcvClp1DiscCells_Type = Counter32
_BbIfRcvClp1DiscCells_Object = MibTableColumn
bbIfRcvClp1DiscCells = _BbIfRcvClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1, 8),
    _BbIfRcvClp1DiscCells_Type()
)
bbIfRcvClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfRcvClp1DiscCells.setStatus("current")
_BbIfXmtOAMCells_Type = Counter32
_BbIfXmtOAMCells_Object = MibTableColumn
bbIfXmtOAMCells = _BbIfXmtOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1, 9),
    _BbIfXmtOAMCells_Type()
)
bbIfXmtOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfXmtOAMCells.setStatus("current")
_BbIfXmtRmCells_Type = Counter32
_BbIfXmtRmCells_Object = MibTableColumn
bbIfXmtRmCells = _BbIfXmtRmCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1, 10),
    _BbIfXmtRmCells_Type()
)
bbIfXmtRmCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfXmtRmCells.setStatus("current")
_BbIfXmtClp0Cells_Type = Counter32
_BbIfXmtClp0Cells_Object = MibTableColumn
bbIfXmtClp0Cells = _BbIfXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1, 11),
    _BbIfXmtClp0Cells_Type()
)
bbIfXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfXmtClp0Cells.setStatus("current")
_BbIfXmtClp1Cells_Type = Counter32
_BbIfXmtClp1Cells_Object = MibTableColumn
bbIfXmtClp1Cells = _BbIfXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1, 12),
    _BbIfXmtClp1Cells_Type()
)
bbIfXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfXmtClp1Cells.setStatus("current")


class _BbIfCntClrButton_Type(Integer32):
    """Custom type bbIfCntClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("resetCounter32s", 2))
    )


_BbIfCntClrButton_Type.__name__ = "Integer32"
_BbIfCntClrButton_Object = MibTableColumn
bbIfCntClrButton = _BbIfCntClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1, 13),
    _BbIfCntClrButton_Type()
)
bbIfCntClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbIfCntClrButton.setStatus("current")
_BbIfRcvErroredCells_Type = Counter32
_BbIfRcvErroredCells_Object = MibTableColumn
bbIfRcvErroredCells = _BbIfRcvErroredCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4, 1, 1, 1, 14),
    _BbIfRcvErroredCells_Type()
)
bbIfRcvErroredCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbIfRcvErroredCells.setStatus("current")
_CwbPortMIBConformance_ObjectIdentity = ObjectIdentity
cwbPortMIBConformance = _CwbPortMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 32, 2)
)
_CwbPortMIBGroups_ObjectIdentity = ObjectIdentity
cwbPortMIBGroups = _CwbPortMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 32, 2, 1)
)
_CwbPortMIBCompliances_ObjectIdentity = ObjectIdentity
cwbPortMIBCompliances = _CwbPortMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 32, 2, 2)
)

# Managed Objects groups

cwbPortGenearlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 32, 2, 1, 1)
)
cwbPortGenearlGroup.setObjects(
    ("CISCO-WAN-BBIF-PORT-MIB", "nextBbIfNumAvailable")
)
if mibBuilder.loadTexts:
    cwbPortGenearlGroup.setStatus("current")

cwbPortConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 32, 2, 1, 2)
)
cwbPortConfGroup.setObjects(
      *(("CISCO-WAN-BBIF-PORT-MIB", "bbIfNum"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfRowStatus"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfAdmin"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfLineNum"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfIngrPctBandwidth"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfEgrPctBandwidth"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfMinVpi"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfMaxVpi"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfSpeed"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfMaxCellRatePct"))
)
if mibBuilder.loadTexts:
    cwbPortConfGroup.setStatus("current")

cwbPortStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 32, 2, 1, 3)
)
cwbPortStateGroup.setObjects(
      *(("CISCO-WAN-BBIF-PORT-MIB", "bbStateIfNum"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfState"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfOversubscribed"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfIngrPercentUtil"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfEgrPercentUtil"))
)
if mibBuilder.loadTexts:
    cwbPortStateGroup.setStatus("current")

cwbPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 32, 2, 1, 4)
)
cwbPortStatsGroup.setObjects(
      *(("CISCO-WAN-BBIF-PORT-MIB", "bbCntIfNum"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfTotalCells"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfRcvValidOAMCells"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfRcvRmCells"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfRcvClp0Cells"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfRcvClp1Cells"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfRcvClp0DiscCells"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfRcvClp1DiscCells"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfXmtOAMCells"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfXmtRmCells"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfXmtClp0Cells"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfXmtClp1Cells"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfCntClrButton"),
        ("CISCO-WAN-BBIF-PORT-MIB", "bbIfRcvErroredCells"))
)
if mibBuilder.loadTexts:
    cwbPortStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwbPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 32, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cwbPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-BBIF-PORT-MIB",
    **{"bbIfCnfPortGrp": bbIfCnfPortGrp,
       "bbIfCnfPortGrpTable": bbIfCnfPortGrpTable,
       "bbIfCnfPortGrpEntry": bbIfCnfPortGrpEntry,
       "bbIfNum": bbIfNum,
       "bbIfRowStatus": bbIfRowStatus,
       "bbIfAdmin": bbIfAdmin,
       "bbIfLineNum": bbIfLineNum,
       "bbIfIngrPctBandwidth": bbIfIngrPctBandwidth,
       "bbIfEgrPctBandwidth": bbIfEgrPctBandwidth,
       "bbIfMinVpi": bbIfMinVpi,
       "bbIfMaxVpi": bbIfMaxVpi,
       "bbIfSpeed": bbIfSpeed,
       "bbIfMaxCellRatePct": bbIfMaxCellRatePct,
       "nextBbIfNumAvailable": nextBbIfNumAvailable,
       "bbIfStateGrpTable": bbIfStateGrpTable,
       "bbIfStateGrpEntry": bbIfStateGrpEntry,
       "bbStateIfNum": bbStateIfNum,
       "bbIfState": bbIfState,
       "bbIfOversubscribed": bbIfOversubscribed,
       "bbIfIngrPercentUtil": bbIfIngrPercentUtil,
       "bbIfEgrPercentUtil": bbIfEgrPercentUtil,
       "bbIfCntGrp": bbIfCntGrp,
       "bbIfCntGrpTable": bbIfCntGrpTable,
       "bbIfCntGrpEntry": bbIfCntGrpEntry,
       "bbCntIfNum": bbCntIfNum,
       "bbIfTotalCells": bbIfTotalCells,
       "bbIfRcvValidOAMCells": bbIfRcvValidOAMCells,
       "bbIfRcvRmCells": bbIfRcvRmCells,
       "bbIfRcvClp0Cells": bbIfRcvClp0Cells,
       "bbIfRcvClp1Cells": bbIfRcvClp1Cells,
       "bbIfRcvClp0DiscCells": bbIfRcvClp0DiscCells,
       "bbIfRcvClp1DiscCells": bbIfRcvClp1DiscCells,
       "bbIfXmtOAMCells": bbIfXmtOAMCells,
       "bbIfXmtRmCells": bbIfXmtRmCells,
       "bbIfXmtClp0Cells": bbIfXmtClp0Cells,
       "bbIfXmtClp1Cells": bbIfXmtClp1Cells,
       "bbIfCntClrButton": bbIfCntClrButton,
       "bbIfRcvErroredCells": bbIfRcvErroredCells,
       "ciscoWanBbifPortMIB": ciscoWanBbifPortMIB,
       "cwbPortMIBConformance": cwbPortMIBConformance,
       "cwbPortMIBGroups": cwbPortMIBGroups,
       "cwbPortGenearlGroup": cwbPortGenearlGroup,
       "cwbPortConfGroup": cwbPortConfGroup,
       "cwbPortStateGroup": cwbPortStateGroup,
       "cwbPortStatsGroup": cwbPortStatsGroup,
       "cwbPortMIBCompliances": cwbPortMIBCompliances,
       "cwbPortCompliance": cwbPortCompliance}
)
