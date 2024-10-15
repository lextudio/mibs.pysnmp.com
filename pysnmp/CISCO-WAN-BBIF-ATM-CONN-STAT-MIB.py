# SNMP MIB module (CISCO-WAN-BBIF-ATM-CONN-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-BBIF-ATM-CONN-STAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:53 2024
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

(bbChanCntGrp,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "bbChanCntGrp")

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

ciscoWanBbifAtmConnStatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 36)
)
ciscoWanBbifAtmConnStatMIB.setRevisions(
        ("2002-10-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BbChanCntGrpTable_Object = MibTable
bbChanCntGrpTable = _BbChanCntGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1)
)
if mibBuilder.loadTexts:
    bbChanCntGrpTable.setStatus("current")
_BbChanCntGrpEntry_Object = MibTableRow
bbChanCntGrpEntry = _BbChanCntGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1)
)
bbChanCntGrpEntry.setIndexNames(
    (0, "CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanCntNum"),
)
if mibBuilder.loadTexts:
    bbChanCntGrpEntry.setStatus("current")


class _BbChanCntNum_Type(Integer32):
    """Custom type bbChanCntNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4111),
    )


_BbChanCntNum_Type.__name__ = "Integer32"
_BbChanCntNum_Object = MibTableColumn
bbChanCntNum = _BbChanCntNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1, 1),
    _BbChanCntNum_Type()
)
bbChanCntNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanCntNum.setStatus("current")
_BbChanRcvClp0Cells_Type = Counter32
_BbChanRcvClp0Cells_Object = MibTableColumn
bbChanRcvClp0Cells = _BbChanRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1, 2),
    _BbChanRcvClp0Cells_Type()
)
bbChanRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanRcvClp0Cells.setStatus("current")
_BbChanRcvClp1Cells_Type = Counter32
_BbChanRcvClp1Cells_Object = MibTableColumn
bbChanRcvClp1Cells = _BbChanRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1, 3),
    _BbChanRcvClp1Cells_Type()
)
bbChanRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanRcvClp1Cells.setStatus("current")
_BbChanNonConformCellsAtGcra1Policer_Type = Counter32
_BbChanNonConformCellsAtGcra1Policer_Object = MibTableColumn
bbChanNonConformCellsAtGcra1Policer = _BbChanNonConformCellsAtGcra1Policer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1, 4),
    _BbChanNonConformCellsAtGcra1Policer_Type()
)
bbChanNonConformCellsAtGcra1Policer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanNonConformCellsAtGcra1Policer.setStatus("current")
_BbChanNonConformCellsAtGcra2Policer_Type = Counter32
_BbChanNonConformCellsAtGcra2Policer_Object = MibTableColumn
bbChanNonConformCellsAtGcra2Policer = _BbChanNonConformCellsAtGcra2Policer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1, 5),
    _BbChanNonConformCellsAtGcra2Policer_Type()
)
bbChanNonConformCellsAtGcra2Policer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanNonConformCellsAtGcra2Policer.setStatus("current")
_BbChanRcvEOFCells_Type = Counter32
_BbChanRcvEOFCells_Object = MibTableColumn
bbChanRcvEOFCells = _BbChanRcvEOFCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1, 6),
    _BbChanRcvEOFCells_Type()
)
bbChanRcvEOFCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanRcvEOFCells.setStatus("current")
_BbChanDscdClp0Cells_Type = Counter32
_BbChanDscdClp0Cells_Object = MibTableColumn
bbChanDscdClp0Cells = _BbChanDscdClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1, 7),
    _BbChanDscdClp0Cells_Type()
)
bbChanDscdClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanDscdClp0Cells.setStatus("current")
_BbChanDscdClp1Cells_Type = Counter32
_BbChanDscdClp1Cells_Object = MibTableColumn
bbChanDscdClp1Cells = _BbChanDscdClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1, 8),
    _BbChanDscdClp1Cells_Type()
)
bbChanDscdClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanDscdClp1Cells.setStatus("current")
_BbChanRcvCellsSent_Type = Counter32
_BbChanRcvCellsSent_Object = MibTableColumn
bbChanRcvCellsSent = _BbChanRcvCellsSent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1, 9),
    _BbChanRcvCellsSent_Type()
)
bbChanRcvCellsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanRcvCellsSent.setStatus("current")
_BbChanXmtClp0Cells_Type = Counter32
_BbChanXmtClp0Cells_Object = MibTableColumn
bbChanXmtClp0Cells = _BbChanXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1, 10),
    _BbChanXmtClp0Cells_Type()
)
bbChanXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanXmtClp0Cells.setStatus("current")
_BbChanXmtClp1Cells_Type = Counter32
_BbChanXmtClp1Cells_Object = MibTableColumn
bbChanXmtClp1Cells = _BbChanXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1, 11),
    _BbChanXmtClp1Cells_Type()
)
bbChanXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanXmtClp1Cells.setStatus("current")
_BbChanDscdClpZeroCellsToPort_Type = Counter32
_BbChanDscdClpZeroCellsToPort_Object = MibTableColumn
bbChanDscdClpZeroCellsToPort = _BbChanDscdClpZeroCellsToPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1, 12),
    _BbChanDscdClpZeroCellsToPort_Type()
)
bbChanDscdClpZeroCellsToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanDscdClpZeroCellsToPort.setStatus("current")
_BbChanDscdClpOneCellsToPort_Type = Counter32
_BbChanDscdClpOneCellsToPort_Object = MibTableColumn
bbChanDscdClpOneCellsToPort = _BbChanDscdClpOneCellsToPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1, 13),
    _BbChanDscdClpOneCellsToPort_Type()
)
bbChanDscdClpOneCellsToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanDscdClpOneCellsToPort.setStatus("current")


class _BbChanCntClrButton_Type(Integer32):
    """Custom type bbChanCntClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("resetCounters", 2))
    )


_BbChanCntClrButton_Type.__name__ = "Integer32"
_BbChanCntClrButton_Object = MibTableColumn
bbChanCntClrButton = _BbChanCntClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3, 1, 1, 14),
    _BbChanCntClrButton_Type()
)
bbChanCntClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanCntClrButton.setStatus("current")
_CwbAtmConnStatMIBConformance_ObjectIdentity = ObjectIdentity
cwbAtmConnStatMIBConformance = _CwbAtmConnStatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 36, 2)
)
_CwbAtmConnStatMIBGroups_ObjectIdentity = ObjectIdentity
cwbAtmConnStatMIBGroups = _CwbAtmConnStatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 36, 2, 1)
)
_CwbAtmConnStatMIBCompliances_ObjectIdentity = ObjectIdentity
cwbAtmConnStatMIBCompliances = _CwbAtmConnStatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 36, 2, 2)
)

# Managed Objects groups

cwbAtmConnStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 36, 2, 1, 1)
)
cwbAtmConnStatsGroup.setObjects(
      *(("CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanCntNum"),
        ("CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanRcvClp0Cells"),
        ("CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanRcvClp1Cells"),
        ("CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanNonConformCellsAtGcra1Policer"),
        ("CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanNonConformCellsAtGcra2Policer"),
        ("CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanRcvEOFCells"),
        ("CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanDscdClp0Cells"),
        ("CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanDscdClp1Cells"),
        ("CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanRcvCellsSent"),
        ("CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanXmtClp0Cells"),
        ("CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanXmtClp1Cells"),
        ("CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanDscdClpZeroCellsToPort"),
        ("CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanDscdClpOneCellsToPort"),
        ("CISCO-WAN-BBIF-ATM-CONN-STAT-MIB", "bbChanCntClrButton"))
)
if mibBuilder.loadTexts:
    cwbAtmConnStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwbAtmConnStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 36, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cwbAtmConnStatCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-BBIF-ATM-CONN-STAT-MIB",
    **{"bbChanCntGrpTable": bbChanCntGrpTable,
       "bbChanCntGrpEntry": bbChanCntGrpEntry,
       "bbChanCntNum": bbChanCntNum,
       "bbChanRcvClp0Cells": bbChanRcvClp0Cells,
       "bbChanRcvClp1Cells": bbChanRcvClp1Cells,
       "bbChanNonConformCellsAtGcra1Policer": bbChanNonConformCellsAtGcra1Policer,
       "bbChanNonConformCellsAtGcra2Policer": bbChanNonConformCellsAtGcra2Policer,
       "bbChanRcvEOFCells": bbChanRcvEOFCells,
       "bbChanDscdClp0Cells": bbChanDscdClp0Cells,
       "bbChanDscdClp1Cells": bbChanDscdClp1Cells,
       "bbChanRcvCellsSent": bbChanRcvCellsSent,
       "bbChanXmtClp0Cells": bbChanXmtClp0Cells,
       "bbChanXmtClp1Cells": bbChanXmtClp1Cells,
       "bbChanDscdClpZeroCellsToPort": bbChanDscdClpZeroCellsToPort,
       "bbChanDscdClpOneCellsToPort": bbChanDscdClpOneCellsToPort,
       "bbChanCntClrButton": bbChanCntClrButton,
       "ciscoWanBbifAtmConnStatMIB": ciscoWanBbifAtmConnStatMIB,
       "cwbAtmConnStatMIBConformance": cwbAtmConnStatMIBConformance,
       "cwbAtmConnStatMIBGroups": cwbAtmConnStatMIBGroups,
       "cwbAtmConnStatsGroup": cwbAtmConnStatsGroup,
       "cwbAtmConnStatMIBCompliances": cwbAtmConnStatMIBCompliances,
       "cwbAtmConnStatCompliance": cwbAtmConnStatCompliance}
)
