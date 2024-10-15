# SNMP MIB module (CISCO-WAN-CES-CONN-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-CES-CONN-STAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:58 2024
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

(cesmChan,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "cesmChan")

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

ciscoWanCesConnStatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 43)
)
ciscoWanCesConnStatMIB.setRevisions(
        ("2002-12-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CesmChanCntGrp_ObjectIdentity = ObjectIdentity
cesmChanCntGrp = _CesmChanCntGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2)
)
_CesmChanCntGrpTable_Object = MibTable
cesmChanCntGrpTable = _CesmChanCntGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cesmChanCntGrpTable.setStatus("current")
_CesmChanCntGrpEntry_Object = MibTableRow
cesmChanCntGrpEntry = _CesmChanCntGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1)
)
cesmChanCntGrpEntry.setIndexNames(
    (0, "CISCO-WAN-CES-CONN-STAT-MIB", "cesCntChanNum"),
)
if mibBuilder.loadTexts:
    cesmChanCntGrpEntry.setStatus("current")


class _CesCntChanNum_Type(Integer32):
    """Custom type cesCntChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 2064),
    )


_CesCntChanNum_Type.__name__ = "Integer32"
_CesCntChanNum_Object = MibTableColumn
cesCntChanNum = _CesCntChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 1),
    _CesCntChanNum_Type()
)
cesCntChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesCntChanNum.setStatus("current")


class _CesChanState_Type(Integer32):
    """Custom type cesChanState based on Integer32"""
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
        *(("alarm", 3),
          ("failed", 4),
          ("notConfigured", 1),
          ("okay", 2))
    )


_CesChanState_Type.__name__ = "Integer32"
_CesChanState_Object = MibTableColumn
cesChanState = _CesChanState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 2),
    _CesChanState_Type()
)
cesChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesChanState.setStatus("current")


class _CesXmtATMState_Type(Integer32):
    """Custom type cesXmtATMState based on Integer32"""
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
        *(("normal", 2),
          ("other", 1),
          ("sendingAIS", 3),
          ("sendingFERF", 4))
    )


_CesXmtATMState_Type.__name__ = "Integer32"
_CesXmtATMState_Object = MibTableColumn
cesXmtATMState = _CesXmtATMState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 3),
    _CesXmtATMState_Type()
)
cesXmtATMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesXmtATMState.setStatus("current")


class _CesRcvATMState_Type(Integer32):
    """Custom type cesRcvATMState based on Integer32"""
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
        *(("normal", 2),
          ("other", 1),
          ("receivingAIS", 3),
          ("receivingFERF", 4))
    )


_CesRcvATMState_Type.__name__ = "Integer32"
_CesRcvATMState_Object = MibTableColumn
cesRcvATMState = _CesRcvATMState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 4),
    _CesRcvATMState_Type()
)
cesRcvATMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesRcvATMState.setStatus("current")


class _CesCellLossStatus_Type(Integer32):
    """Custom type cesCellLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loss", 2),
          ("noLoss", 1))
    )


_CesCellLossStatus_Type.__name__ = "Integer32"
_CesCellLossStatus_Object = MibTableColumn
cesCellLossStatus = _CesCellLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 5),
    _CesCellLossStatus_Type()
)
cesCellLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesCellLossStatus.setStatus("current")
_CesReassCells_Type = Counter32
_CesReassCells_Object = MibTableColumn
cesReassCells = _CesReassCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 6),
    _CesReassCells_Type()
)
cesReassCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesReassCells.setStatus("current")
_CesGenCells_Type = Counter32
_CesGenCells_Object = MibTableColumn
cesGenCells = _CesGenCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 7),
    _CesGenCells_Type()
)
cesGenCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesGenCells.setStatus("current")
_CesHdrErrors_Type = Counter32
_CesHdrErrors_Object = MibTableColumn
cesHdrErrors = _CesHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 8),
    _CesHdrErrors_Type()
)
cesHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesHdrErrors.setStatus("current")
_CesPointerReframes_Type = Counter32
_CesPointerReframes_Object = MibTableColumn
cesPointerReframes = _CesPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 9),
    _CesPointerReframes_Type()
)
cesPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPointerReframes.setStatus("current")
_CesLostCells_Type = Counter32
_CesLostCells_Object = MibTableColumn
cesLostCells = _CesLostCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 10),
    _CesLostCells_Type()
)
cesLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesLostCells.setStatus("current")
_CesBufUnderflows_Type = Counter32
_CesBufUnderflows_Object = MibTableColumn
cesBufUnderflows = _CesBufUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 11),
    _CesBufUnderflows_Type()
)
cesBufUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesBufUnderflows.setStatus("current")
_CesBufOverflows_Type = Counter32
_CesBufOverflows_Object = MibTableColumn
cesBufOverflows = _CesBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 12),
    _CesBufOverflows_Type()
)
cesBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesBufOverflows.setStatus("current")
_CesIngrDiscardedBytes_Type = Counter32
_CesIngrDiscardedBytes_Object = MibTableColumn
cesIngrDiscardedBytes = _CesIngrDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 13),
    _CesIngrDiscardedBytes_Type()
)
cesIngrDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesIngrDiscardedBytes.setStatus("current")
_CesUflowInsCells_Type = Counter32
_CesUflowInsCells_Object = MibTableColumn
cesUflowInsCells = _CesUflowInsCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 14),
    _CesUflowInsCells_Type()
)
cesUflowInsCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesUflowInsCells.setStatus("current")
_CesOflowDropBytes_Type = Counter32
_CesOflowDropBytes_Object = MibTableColumn
cesOflowDropBytes = _CesOflowDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 15),
    _CesOflowDropBytes_Type()
)
cesOflowDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOflowDropBytes.setStatus("current")
_CesCellSeqMismatchCnt_Type = Counter32
_CesCellSeqMismatchCnt_Object = MibTableColumn
cesCellSeqMismatchCnt = _CesCellSeqMismatchCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 16),
    _CesCellSeqMismatchCnt_Type()
)
cesCellSeqMismatchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesCellSeqMismatchCnt.setStatus("current")


class _CounterClrButton_Type(Integer32):
    """Custom type counterClrButton based on Integer32"""
    defaultValue = 1

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


_CounterClrButton_Type.__name__ = "Integer32"
_CounterClrButton_Object = MibTableColumn
counterClrButton = _CounterClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 17),
    _CounterClrButton_Type()
)
counterClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClrButton.setStatus("current")
_CesChanSecUptime_Type = Counter32
_CesChanSecUptime_Object = MibTableColumn
cesChanSecUptime = _CesChanSecUptime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 18),
    _CesChanSecUptime_Type()
)
cesChanSecUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesChanSecUptime.setStatus("current")


class _CesChanSignalingStatus_Type(Integer32):
    """Custom type cesChanSignalingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off-hook", 1),
          ("on-hook", 2))
    )


_CesChanSignalingStatus_Type.__name__ = "Integer32"
_CesChanSignalingStatus_Object = MibTableColumn
cesChanSignalingStatus = _CesChanSignalingStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 19),
    _CesChanSignalingStatus_Type()
)
cesChanSignalingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesChanSignalingStatus.setStatus("current")


class _CesChanStatusBitMap_Type(Integer32):
    """Custom type cesChanStatusBitMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CesChanStatusBitMap_Type.__name__ = "Integer32"
_CesChanStatusBitMap_Object = MibTableColumn
cesChanStatusBitMap = _CesChanStatusBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2, 2, 1, 1, 20),
    _CesChanStatusBitMap_Type()
)
cesChanStatusBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesChanStatusBitMap.setStatus("current")
_CwcConnStatMIBConformance_ObjectIdentity = ObjectIdentity
cwcConnStatMIBConformance = _CwcConnStatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 43, 2)
)
_CwcConnStatMIBGroups_ObjectIdentity = ObjectIdentity
cwcConnStatMIBGroups = _CwcConnStatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 43, 2, 1)
)
_CwcConnStatMIBCompliances_ObjectIdentity = ObjectIdentity
cwcConnStatMIBCompliances = _CwcConnStatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 43, 2, 2)
)

# Managed Objects groups

cwcConnGenStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 43, 2, 1, 1)
)
cwcConnGenStatsGroup.setObjects(
      *(("CISCO-WAN-CES-CONN-STAT-MIB", "cesCntChanNum"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesChanState"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesXmtATMState"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesRcvATMState"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesCellLossStatus"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesReassCells"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesGenCells"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesHdrErrors"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesPointerReframes"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesLostCells"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesBufUnderflows"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesBufOverflows"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesIngrDiscardedBytes"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesUflowInsCells"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesOflowDropBytes"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesCellSeqMismatchCnt"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "counterClrButton"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesChanSecUptime"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesChanSignalingStatus"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesChanStatusBitMap"))
)
if mibBuilder.loadTexts:
    cwcConnGenStatsGroup.setStatus("current")

cwcConnStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 43, 2, 1, 2)
)
cwcConnStatsGroup.setObjects(
      *(("CISCO-WAN-CES-CONN-STAT-MIB", "cesPointerReframes"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesBufUnderflows"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesBufOverflows"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesIngrDiscardedBytes"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesUflowInsCells"),
        ("CISCO-WAN-CES-CONN-STAT-MIB", "cesOflowDropBytes"))
)
if mibBuilder.loadTexts:
    cwcConnStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwcConnStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 43, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cwcConnStatCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-CES-CONN-STAT-MIB",
    **{"cesmChanCntGrp": cesmChanCntGrp,
       "cesmChanCntGrpTable": cesmChanCntGrpTable,
       "cesmChanCntGrpEntry": cesmChanCntGrpEntry,
       "cesCntChanNum": cesCntChanNum,
       "cesChanState": cesChanState,
       "cesXmtATMState": cesXmtATMState,
       "cesRcvATMState": cesRcvATMState,
       "cesCellLossStatus": cesCellLossStatus,
       "cesReassCells": cesReassCells,
       "cesGenCells": cesGenCells,
       "cesHdrErrors": cesHdrErrors,
       "cesPointerReframes": cesPointerReframes,
       "cesLostCells": cesLostCells,
       "cesBufUnderflows": cesBufUnderflows,
       "cesBufOverflows": cesBufOverflows,
       "cesIngrDiscardedBytes": cesIngrDiscardedBytes,
       "cesUflowInsCells": cesUflowInsCells,
       "cesOflowDropBytes": cesOflowDropBytes,
       "cesCellSeqMismatchCnt": cesCellSeqMismatchCnt,
       "counterClrButton": counterClrButton,
       "cesChanSecUptime": cesChanSecUptime,
       "cesChanSignalingStatus": cesChanSignalingStatus,
       "cesChanStatusBitMap": cesChanStatusBitMap,
       "ciscoWanCesConnStatMIB": ciscoWanCesConnStatMIB,
       "cwcConnStatMIBConformance": cwcConnStatMIBConformance,
       "cwcConnStatMIBGroups": cwcConnStatMIBGroups,
       "cwcConnGenStatsGroup": cwcConnGenStatsGroup,
       "cwcConnStatsGroup": cwcConnStatsGroup,
       "cwcConnStatMIBCompliances": cwcConnStatMIBCompliances,
       "cwcConnStatCompliance": cwcConnStatCompliance}
)
