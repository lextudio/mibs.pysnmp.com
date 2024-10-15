# SNMP MIB module (CISCO-SWITCH-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SWITCH-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:15 2024
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

(Percent,
 QosLayer2Cos) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "Percent",
    "QosLayer2Cos")

(QosIpPrecedence,
 QosMplsExpValue,
 QosMutationMapName,
 QosMutationMapNameOrEmpty,
 QosPolicerType,
 QosQueueNumber,
 QosThresholdNumber) = mibBuilder.importSymbols(
    "CISCO-QOS-TC-MIB",
    "QosIpPrecedence",
    "QosMplsExpValue",
    "QosMutationMapName",
    "QosMutationMapNameOrEmpty",
    "QosPolicerType",
    "QosQueueNumber",
    "QosThresholdNumber")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(IfDirection,) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IfDirection")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSwitchQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 580)
)
ciscoSwitchQosMIB.setRevisions(
        ("2016-06-30 00:00",
         "2014-09-19 00:00",
         "2013-09-26 00:00",
         "2013-04-22 00:00",
         "2010-11-17 00:00",
         "2009-07-20 00:00",
         "2009-02-23 00:00",
         "2006-11-20 00:00",
         "2006-09-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class QosStatsType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("droppedIngressPkts", 11),
          ("mcastDroppedBytes", 8),
          ("mcastDroppedPkts", 7),
          ("mcastRecvXbarPkts", 15),
          ("mcastSentBytes", 4),
          ("mcastSentPkts", 3),
          ("mcastSentXbarPkts", 14),
          ("receivedPkts", 10),
          ("sentPkts", 9),
          ("ucastDroppedBytes", 6),
          ("ucastDroppedOobfcBytes", 19),
          ("ucastDroppedOobfcPkts", 18),
          ("ucastDroppedPkts", 5),
          ("ucastRecvXbarPkts", 13),
          ("ucastSentBytes", 2),
          ("ucastSentOobfcBytes", 17),
          ("ucastSentOobfcPkts", 16),
          ("ucastSentPkts", 1),
          ("ucastSentXbarPkts", 12),
          ("ucastWatchdogDroppedPkts", 20))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSwitchQosMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSwitchQosMIBNotifs = _CiscoSwitchQosMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 0)
)
_CiscoSwitchQosMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSwitchQosMIBObjects = _CiscoSwitchQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1)
)
_CsqGlobals_ObjectIdentity = ObjectIdentity
csqGlobals = _CsqGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 1)
)
_CsqDscpRewriteEnable_Type = TruthValue
_CsqDscpRewriteEnable_Object = MibScalar
csqDscpRewriteEnable = _CsqDscpRewriteEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 1, 1),
    _CsqDscpRewriteEnable_Type()
)
csqDscpRewriteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqDscpRewriteEnable.setStatus("current")
_CsqPoliceRedirectedTrafficEnable_Type = TruthValue
_CsqPoliceRedirectedTrafficEnable_Object = MibScalar
csqPoliceRedirectedTrafficEnable = _CsqPoliceRedirectedTrafficEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 1, 2),
    _CsqPoliceRedirectedTrafficEnable_Type()
)
csqPoliceRedirectedTrafficEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqPoliceRedirectedTrafficEnable.setStatus("current")
_CsqPortQueueingModeEnable_Type = TruthValue
_CsqPortQueueingModeEnable_Object = MibScalar
csqPortQueueingModeEnable = _CsqPortQueueingModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 1, 3),
    _CsqPortQueueingModeEnable_Type()
)
csqPortQueueingModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqPortQueueingModeEnable.setStatus("current")
_CsqMarkingStatisticsEnable_Type = TruthValue
_CsqMarkingStatisticsEnable_Object = MibScalar
csqMarkingStatisticsEnable = _CsqMarkingStatisticsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 1, 4),
    _CsqMarkingStatisticsEnable_Type()
)
csqMarkingStatisticsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqMarkingStatisticsEnable.setStatus("current")
_CsqTenGOnlyMode_Type = TruthValue
_CsqTenGOnlyMode_Object = MibScalar
csqTenGOnlyMode = _CsqTenGOnlyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 1, 5),
    _CsqTenGOnlyMode_Type()
)
csqTenGOnlyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqTenGOnlyMode.setStatus("current")
_CsqServicePoolCellSize_Type = Unsigned32
_CsqServicePoolCellSize_Object = MibScalar
csqServicePoolCellSize = _CsqServicePoolCellSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 1, 6),
    _CsqServicePoolCellSize_Type()
)
csqServicePoolCellSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqServicePoolCellSize.setStatus("current")
_CsqMappings_ObjectIdentity = ObjectIdentity
csqMappings = _CsqMappings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2)
)
_CsqCosToDscpTable_Object = MibTable
csqCosToDscpTable = _CsqCosToDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 1)
)
if mibBuilder.loadTexts:
    csqCosToDscpTable.setStatus("current")
_CsqCosToDscpEntry_Object = MibTableRow
csqCosToDscpEntry = _CsqCosToDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 1, 1)
)
csqCosToDscpEntry.setIndexNames(
    (0, "CISCO-SWITCH-QOS-MIB", "csqCosToDscpCos"),
)
if mibBuilder.loadTexts:
    csqCosToDscpEntry.setStatus("current")
_CsqCosToDscpCos_Type = QosLayer2Cos
_CsqCosToDscpCos_Object = MibTableColumn
csqCosToDscpCos = _CsqCosToDscpCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 1, 1, 1),
    _CsqCosToDscpCos_Type()
)
csqCosToDscpCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqCosToDscpCos.setStatus("current")
_CsqCosToDscpDscp_Type = Dscp
_CsqCosToDscpDscp_Object = MibTableColumn
csqCosToDscpDscp = _CsqCosToDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 1, 1, 2),
    _CsqCosToDscpDscp_Type()
)
csqCosToDscpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqCosToDscpDscp.setStatus("current")
_CsqIpPrecToDscpTable_Object = MibTable
csqIpPrecToDscpTable = _CsqIpPrecToDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 2)
)
if mibBuilder.loadTexts:
    csqIpPrecToDscpTable.setStatus("current")
_CsqIpPrecToDscpEntry_Object = MibTableRow
csqIpPrecToDscpEntry = _CsqIpPrecToDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 2, 1)
)
csqIpPrecToDscpEntry.setIndexNames(
    (0, "CISCO-SWITCH-QOS-MIB", "csqIpPrecToDscpIpPrec"),
)
if mibBuilder.loadTexts:
    csqIpPrecToDscpEntry.setStatus("current")
_CsqIpPrecToDscpIpPrec_Type = QosIpPrecedence
_CsqIpPrecToDscpIpPrec_Object = MibTableColumn
csqIpPrecToDscpIpPrec = _CsqIpPrecToDscpIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 2, 1, 1),
    _CsqIpPrecToDscpIpPrec_Type()
)
csqIpPrecToDscpIpPrec.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIpPrecToDscpIpPrec.setStatus("current")
_CsqIpPrecToDscpDscp_Type = Dscp
_CsqIpPrecToDscpDscp_Object = MibTableColumn
csqIpPrecToDscpDscp = _CsqIpPrecToDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 2, 1, 2),
    _CsqIpPrecToDscpDscp_Type()
)
csqIpPrecToDscpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIpPrecToDscpDscp.setStatus("current")
_CsqExpToDscpTable_Object = MibTable
csqExpToDscpTable = _CsqExpToDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 3)
)
if mibBuilder.loadTexts:
    csqExpToDscpTable.setStatus("current")
_CsqExpToDscpEntry_Object = MibTableRow
csqExpToDscpEntry = _CsqExpToDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 3, 1)
)
csqExpToDscpEntry.setIndexNames(
    (0, "CISCO-SWITCH-QOS-MIB", "csqExpToDscpExp"),
)
if mibBuilder.loadTexts:
    csqExpToDscpEntry.setStatus("current")
_CsqExpToDscpExp_Type = QosMplsExpValue
_CsqExpToDscpExp_Object = MibTableColumn
csqExpToDscpExp = _CsqExpToDscpExp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 3, 1, 1),
    _CsqExpToDscpExp_Type()
)
csqExpToDscpExp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqExpToDscpExp.setStatus("current")
_CsqExpToDscpDscp_Type = Dscp
_CsqExpToDscpDscp_Object = MibTableColumn
csqExpToDscpDscp = _CsqExpToDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 3, 1, 2),
    _CsqExpToDscpDscp_Type()
)
csqExpToDscpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqExpToDscpDscp.setStatus("current")
_CsqDscpMappingTable_Object = MibTable
csqDscpMappingTable = _CsqDscpMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 4)
)
if mibBuilder.loadTexts:
    csqDscpMappingTable.setStatus("current")
_CsqDscpMappingEntry_Object = MibTableRow
csqDscpMappingEntry = _CsqDscpMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 4, 1)
)
csqDscpMappingEntry.setIndexNames(
    (0, "CISCO-SWITCH-QOS-MIB", "csqDscpMappingDscp"),
)
if mibBuilder.loadTexts:
    csqDscpMappingEntry.setStatus("current")
_CsqDscpMappingDscp_Type = Dscp
_CsqDscpMappingDscp_Object = MibTableColumn
csqDscpMappingDscp = _CsqDscpMappingDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 4, 1, 1),
    _CsqDscpMappingDscp_Type()
)
csqDscpMappingDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqDscpMappingDscp.setStatus("current")
_CsqDscpMappingCos_Type = QosLayer2Cos
_CsqDscpMappingCos_Object = MibTableColumn
csqDscpMappingCos = _CsqDscpMappingCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 4, 1, 2),
    _CsqDscpMappingCos_Type()
)
csqDscpMappingCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqDscpMappingCos.setStatus("current")
_CsqDscpMappingExp_Type = QosMplsExpValue
_CsqDscpMappingExp_Object = MibTableColumn
csqDscpMappingExp = _CsqDscpMappingExp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 4, 1, 3),
    _CsqDscpMappingExp_Type()
)
csqDscpMappingExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqDscpMappingExp.setStatus("current")
_CsqDscpMappingNormalBurstDscp_Type = Dscp
_CsqDscpMappingNormalBurstDscp_Object = MibTableColumn
csqDscpMappingNormalBurstDscp = _CsqDscpMappingNormalBurstDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 4, 1, 4),
    _CsqDscpMappingNormalBurstDscp_Type()
)
csqDscpMappingNormalBurstDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqDscpMappingNormalBurstDscp.setStatus("current")
_CsqDscpMappingMaxBurstDscp_Type = Dscp
_CsqDscpMappingMaxBurstDscp_Object = MibTableColumn
csqDscpMappingMaxBurstDscp = _CsqDscpMappingMaxBurstDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 2, 4, 1, 5),
    _CsqDscpMappingMaxBurstDscp_Type()
)
csqDscpMappingMaxBurstDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqDscpMappingMaxBurstDscp.setStatus("current")
_CsqMutations_ObjectIdentity = ObjectIdentity
csqMutations = _CsqMutations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3)
)
_CsqMaxCosMutationMap_Type = Unsigned32
_CsqMaxCosMutationMap_Object = MibScalar
csqMaxCosMutationMap = _CsqMaxCosMutationMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 1),
    _CsqMaxCosMutationMap_Type()
)
csqMaxCosMutationMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqMaxCosMutationMap.setStatus("current")
_CsqCosMutationTable_Object = MibTable
csqCosMutationTable = _CsqCosMutationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 2)
)
if mibBuilder.loadTexts:
    csqCosMutationTable.setStatus("current")
_CsqCosMutationEntry_Object = MibTableRow
csqCosMutationEntry = _CsqCosMutationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 2, 1)
)
csqCosMutationEntry.setIndexNames(
    (1, "CISCO-SWITCH-QOS-MIB", "csqCosMutationMapName"),
)
if mibBuilder.loadTexts:
    csqCosMutationEntry.setStatus("current")
_CsqCosMutationMapName_Type = QosMutationMapName
_CsqCosMutationMapName_Object = MibTableColumn
csqCosMutationMapName = _CsqCosMutationMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 2, 1, 1),
    _CsqCosMutationMapName_Type()
)
csqCosMutationMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqCosMutationMapName.setStatus("current")
_CsqCosMutationRowStatus_Type = RowStatus
_CsqCosMutationRowStatus_Object = MibTableColumn
csqCosMutationRowStatus = _CsqCosMutationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 2, 1, 2),
    _CsqCosMutationRowStatus_Type()
)
csqCosMutationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csqCosMutationRowStatus.setStatus("current")
_CsqCosMutationMappingTable_Object = MibTable
csqCosMutationMappingTable = _CsqCosMutationMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 3)
)
if mibBuilder.loadTexts:
    csqCosMutationMappingTable.setStatus("current")
_CsqCosMutationMappingEntry_Object = MibTableRow
csqCosMutationMappingEntry = _CsqCosMutationMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 3, 1)
)
csqCosMutationMappingEntry.setIndexNames(
    (0, "CISCO-SWITCH-QOS-MIB", "csqCosMutationMapName"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqCosMutationFromCos"),
)
if mibBuilder.loadTexts:
    csqCosMutationMappingEntry.setStatus("current")
_CsqCosMutationFromCos_Type = QosLayer2Cos
_CsqCosMutationFromCos_Object = MibTableColumn
csqCosMutationFromCos = _CsqCosMutationFromCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 3, 1, 1),
    _CsqCosMutationFromCos_Type()
)
csqCosMutationFromCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqCosMutationFromCos.setStatus("current")
_CsqCosMutationToCos_Type = QosLayer2Cos
_CsqCosMutationToCos_Object = MibTableColumn
csqCosMutationToCos = _CsqCosMutationToCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 3, 1, 2),
    _CsqCosMutationToCos_Type()
)
csqCosMutationToCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqCosMutationToCos.setStatus("current")
_CsqMaxDscpMutationMap_Type = Unsigned32
_CsqMaxDscpMutationMap_Object = MibScalar
csqMaxDscpMutationMap = _CsqMaxDscpMutationMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 4),
    _CsqMaxDscpMutationMap_Type()
)
csqMaxDscpMutationMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqMaxDscpMutationMap.setStatus("current")
_CsqDscpMutationTable_Object = MibTable
csqDscpMutationTable = _CsqDscpMutationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 5)
)
if mibBuilder.loadTexts:
    csqDscpMutationTable.setStatus("current")
_CsqDscpMutationEntry_Object = MibTableRow
csqDscpMutationEntry = _CsqDscpMutationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 5, 1)
)
csqDscpMutationEntry.setIndexNames(
    (1, "CISCO-SWITCH-QOS-MIB", "csqDscpMutationMapName"),
)
if mibBuilder.loadTexts:
    csqDscpMutationEntry.setStatus("current")
_CsqDscpMutationMapName_Type = QosMutationMapName
_CsqDscpMutationMapName_Object = MibTableColumn
csqDscpMutationMapName = _CsqDscpMutationMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 5, 1, 1),
    _CsqDscpMutationMapName_Type()
)
csqDscpMutationMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqDscpMutationMapName.setStatus("current")
_CsqDscpMutationRowStatus_Type = RowStatus
_CsqDscpMutationRowStatus_Object = MibTableColumn
csqDscpMutationRowStatus = _CsqDscpMutationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 5, 1, 2),
    _CsqDscpMutationRowStatus_Type()
)
csqDscpMutationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csqDscpMutationRowStatus.setStatus("current")
_CsqDscpMutationMappingTable_Object = MibTable
csqDscpMutationMappingTable = _CsqDscpMutationMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 6)
)
if mibBuilder.loadTexts:
    csqDscpMutationMappingTable.setStatus("current")
_CsqDscpMutationMappingEntry_Object = MibTableRow
csqDscpMutationMappingEntry = _CsqDscpMutationMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 6, 1)
)
csqDscpMutationMappingEntry.setIndexNames(
    (0, "CISCO-SWITCH-QOS-MIB", "csqDscpMutationMapName"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqDscpMutationFromDscp"),
)
if mibBuilder.loadTexts:
    csqDscpMutationMappingEntry.setStatus("current")
_CsqDscpMutationFromDscp_Type = Dscp
_CsqDscpMutationFromDscp_Object = MibTableColumn
csqDscpMutationFromDscp = _CsqDscpMutationFromDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 6, 1, 1),
    _CsqDscpMutationFromDscp_Type()
)
csqDscpMutationFromDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqDscpMutationFromDscp.setStatus("current")
_CsqDscpMutationToDscp_Type = Dscp
_CsqDscpMutationToDscp_Object = MibTableColumn
csqDscpMutationToDscp = _CsqDscpMutationToDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 6, 1, 2),
    _CsqDscpMutationToDscp_Type()
)
csqDscpMutationToDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqDscpMutationToDscp.setStatus("current")
_CsqMaxExpMutationMap_Type = Unsigned32
_CsqMaxExpMutationMap_Object = MibScalar
csqMaxExpMutationMap = _CsqMaxExpMutationMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 7),
    _CsqMaxExpMutationMap_Type()
)
csqMaxExpMutationMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqMaxExpMutationMap.setStatus("current")
_CsqExpMutationTable_Object = MibTable
csqExpMutationTable = _CsqExpMutationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 8)
)
if mibBuilder.loadTexts:
    csqExpMutationTable.setStatus("current")
_CsqExpMutationEntry_Object = MibTableRow
csqExpMutationEntry = _CsqExpMutationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 8, 1)
)
csqExpMutationEntry.setIndexNames(
    (1, "CISCO-SWITCH-QOS-MIB", "csqExpMutationMapName"),
)
if mibBuilder.loadTexts:
    csqExpMutationEntry.setStatus("current")
_CsqExpMutationMapName_Type = QosMutationMapName
_CsqExpMutationMapName_Object = MibTableColumn
csqExpMutationMapName = _CsqExpMutationMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 8, 1, 1),
    _CsqExpMutationMapName_Type()
)
csqExpMutationMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqExpMutationMapName.setStatus("current")
_CsqExpMutationRowStatus_Type = RowStatus
_CsqExpMutationRowStatus_Object = MibTableColumn
csqExpMutationRowStatus = _CsqExpMutationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 8, 1, 2),
    _CsqExpMutationRowStatus_Type()
)
csqExpMutationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csqExpMutationRowStatus.setStatus("current")
_CsqExpMutationMappingTable_Object = MibTable
csqExpMutationMappingTable = _CsqExpMutationMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 9)
)
if mibBuilder.loadTexts:
    csqExpMutationMappingTable.setStatus("current")
_CsqExpMutationMappingEntry_Object = MibTableRow
csqExpMutationMappingEntry = _CsqExpMutationMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 9, 1)
)
csqExpMutationMappingEntry.setIndexNames(
    (0, "CISCO-SWITCH-QOS-MIB", "csqExpMutationMapName"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqExpMutationFromExp"),
)
if mibBuilder.loadTexts:
    csqExpMutationMappingEntry.setStatus("current")
_CsqExpMutationFromExp_Type = QosMplsExpValue
_CsqExpMutationFromExp_Object = MibTableColumn
csqExpMutationFromExp = _CsqExpMutationFromExp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 9, 1, 1),
    _CsqExpMutationFromExp_Type()
)
csqExpMutationFromExp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqExpMutationFromExp.setStatus("current")
_CsqExpMutationToExp_Type = QosMplsExpValue
_CsqExpMutationToExp_Object = MibTableColumn
csqExpMutationToExp = _CsqExpMutationToExp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 9, 1, 2),
    _CsqExpMutationToExp_Type()
)
csqExpMutationToExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqExpMutationToExp.setStatus("current")
_CsqIfMutationConfigTable_Object = MibTable
csqIfMutationConfigTable = _CsqIfMutationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 10)
)
if mibBuilder.loadTexts:
    csqIfMutationConfigTable.setStatus("current")
_CsqIfMutationConfigEntry_Object = MibTableRow
csqIfMutationConfigEntry = _CsqIfMutationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 10, 1)
)
csqIfMutationConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    csqIfMutationConfigEntry.setStatus("current")
_CsqIfCosMutationMap_Type = QosMutationMapNameOrEmpty
_CsqIfCosMutationMap_Object = MibTableColumn
csqIfCosMutationMap = _CsqIfCosMutationMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 10, 1, 1),
    _CsqIfCosMutationMap_Type()
)
csqIfCosMutationMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csqIfCosMutationMap.setStatus("current")
_CsqIfDscpMutationMap_Type = QosMutationMapNameOrEmpty
_CsqIfDscpMutationMap_Object = MibTableColumn
csqIfDscpMutationMap = _CsqIfDscpMutationMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 10, 1, 2),
    _CsqIfDscpMutationMap_Type()
)
csqIfDscpMutationMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csqIfDscpMutationMap.setStatus("current")
_CsqIfExpMutationMap_Type = QosMutationMapNameOrEmpty
_CsqIfExpMutationMap_Object = MibTableColumn
csqIfExpMutationMap = _CsqIfExpMutationMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 10, 1, 3),
    _CsqIfExpMutationMap_Type()
)
csqIfExpMutationMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csqIfExpMutationMap.setStatus("current")
_CsqIfMutationRowStatus_Type = RowStatus
_CsqIfMutationRowStatus_Object = MibTableColumn
csqIfMutationRowStatus = _CsqIfMutationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 3, 10, 1, 4),
    _CsqIfMutationRowStatus_Type()
)
csqIfMutationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csqIfMutationRowStatus.setStatus("current")
_CsqInterface_ObjectIdentity = ObjectIdentity
csqInterface = _CsqInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4)
)
_CsqIfConfigTable_Object = MibTable
csqIfConfigTable = _CsqIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 1)
)
if mibBuilder.loadTexts:
    csqIfConfigTable.setStatus("current")
_CsqIfConfigEntry_Object = MibTableRow
csqIfConfigEntry = _CsqIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 1, 1)
)
csqIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    csqIfConfigEntry.setStatus("current")
_CsqIfDefaultCos_Type = QosLayer2Cos
_CsqIfDefaultCos_Object = MibTableColumn
csqIfDefaultCos = _CsqIfDefaultCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 1, 1, 1),
    _CsqIfDefaultCos_Type()
)
csqIfDefaultCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfDefaultCos.setStatus("current")


class _CsqIfTrustState_Type(Integer32):
    """Custom type csqIfTrustState based on Integer32"""
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
        *(("trustCoS", 2),
          ("trustDscp", 4),
          ("trustIpPrec", 3),
          ("untrusted", 1))
    )


_CsqIfTrustState_Type.__name__ = "Integer32"
_CsqIfTrustState_Object = MibTableColumn
csqIfTrustState = _CsqIfTrustState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 1, 1, 2),
    _CsqIfTrustState_Type()
)
csqIfTrustState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfTrustState.setStatus("current")


class _CsqIfQueueModeCpb_Type(Bits):
    """Custom type csqIfQueueModeCpb based on Bits"""
    namedValues = NamedValues(
        *(("cos", 0),
          ("dscp", 1))
    )

_CsqIfQueueModeCpb_Type.__name__ = "Bits"
_CsqIfQueueModeCpb_Object = MibTableColumn
csqIfQueueModeCpb = _CsqIfQueueModeCpb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 1, 1, 3),
    _CsqIfQueueModeCpb_Type()
)
csqIfQueueModeCpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQueueModeCpb.setStatus("current")


class _CsqIfConfigQueueMode_Type(Integer32):
    """Custom type csqIfConfigQueueMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("dscp", 2))
    )


_CsqIfConfigQueueMode_Type.__name__ = "Integer32"
_CsqIfConfigQueueMode_Object = MibTableColumn
csqIfConfigQueueMode = _CsqIfConfigQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 1, 1, 4),
    _CsqIfConfigQueueMode_Type()
)
csqIfConfigQueueMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfConfigQueueMode.setStatus("current")
_CsqIfIngressPolicyMap_Type = SnmpAdminString
_CsqIfIngressPolicyMap_Object = MibTableColumn
csqIfIngressPolicyMap = _CsqIfIngressPolicyMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 1, 1, 5),
    _CsqIfIngressPolicyMap_Type()
)
csqIfIngressPolicyMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfIngressPolicyMap.setStatus("current")
_CsqIfEgressPolicyMap_Type = SnmpAdminString
_CsqIfEgressPolicyMap_Object = MibTableColumn
csqIfEgressPolicyMap = _CsqIfEgressPolicyMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 1, 1, 6),
    _CsqIfEgressPolicyMap_Type()
)
csqIfEgressPolicyMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfEgressPolicyMap.setStatus("current")
_CsqIfIngressQueueingEnable_Type = TruthValue
_CsqIfIngressQueueingEnable_Object = MibTableColumn
csqIfIngressQueueingEnable = _CsqIfIngressQueueingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 1, 1, 7),
    _CsqIfIngressQueueingEnable_Type()
)
csqIfIngressQueueingEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfIngressQueueingEnable.setStatus("current")
_CsqIfEgressQueueingEnable_Type = TruthValue
_CsqIfEgressQueueingEnable_Object = MibTableColumn
csqIfEgressQueueingEnable = _CsqIfEgressQueueingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 1, 1, 8),
    _CsqIfEgressQueueingEnable_Type()
)
csqIfEgressQueueingEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfEgressQueueingEnable.setStatus("current")


class _CsqIfQueueingTrustState_Type(Integer32):
    """Custom type csqIfQueueingTrustState based on Integer32"""
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
        *(("trustCoS", 2),
          ("trustDscp", 4),
          ("trustIpPrec", 3),
          ("untrusted", 1))
    )


_CsqIfQueueingTrustState_Type.__name__ = "Integer32"
_CsqIfQueueingTrustState_Object = MibTableColumn
csqIfQueueingTrustState = _CsqIfQueueingTrustState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 1, 1, 9),
    _CsqIfQueueingTrustState_Type()
)
csqIfQueueingTrustState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQueueingTrustState.setStatus("current")
_CsqIfCosToQueueTable_Object = MibTable
csqIfCosToQueueTable = _CsqIfCosToQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 2)
)
if mibBuilder.loadTexts:
    csqIfCosToQueueTable.setStatus("current")
_CsqIfCosToQueueEntry_Object = MibTableRow
csqIfCosToQueueEntry = _CsqIfCosToQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 2, 1)
)
csqIfCosToQueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfCosToQueueDirection"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfCosToQueueCos"),
)
if mibBuilder.loadTexts:
    csqIfCosToQueueEntry.setStatus("current")
_CsqIfCosToQueueDirection_Type = IfDirection
_CsqIfCosToQueueDirection_Object = MibTableColumn
csqIfCosToQueueDirection = _CsqIfCosToQueueDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 2, 1, 1),
    _CsqIfCosToQueueDirection_Type()
)
csqIfCosToQueueDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfCosToQueueDirection.setStatus("current")
_CsqIfCosToQueueCos_Type = QosLayer2Cos
_CsqIfCosToQueueCos_Object = MibTableColumn
csqIfCosToQueueCos = _CsqIfCosToQueueCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 2, 1, 2),
    _CsqIfCosToQueueCos_Type()
)
csqIfCosToQueueCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfCosToQueueCos.setStatus("current")
_CsqIfCosToQueueQueueNumber_Type = QosQueueNumber
_CsqIfCosToQueueQueueNumber_Object = MibTableColumn
csqIfCosToQueueQueueNumber = _CsqIfCosToQueueQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 2, 1, 3),
    _CsqIfCosToQueueQueueNumber_Type()
)
csqIfCosToQueueQueueNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfCosToQueueQueueNumber.setStatus("current")
_CsqIfCosToQueueThresholdNumber_Type = QosThresholdNumber
_CsqIfCosToQueueThresholdNumber_Object = MibTableColumn
csqIfCosToQueueThresholdNumber = _CsqIfCosToQueueThresholdNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 2, 1, 4),
    _CsqIfCosToQueueThresholdNumber_Type()
)
csqIfCosToQueueThresholdNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfCosToQueueThresholdNumber.setStatus("current")
_CsqIfDscpToQueueTable_Object = MibTable
csqIfDscpToQueueTable = _CsqIfDscpToQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 3)
)
if mibBuilder.loadTexts:
    csqIfDscpToQueueTable.setStatus("current")
_CsqIfDscpToQueueEntry_Object = MibTableRow
csqIfDscpToQueueEntry = _CsqIfDscpToQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 3, 1)
)
csqIfDscpToQueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfDscpToQueueDirection"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfDscpToQueueDscp"),
)
if mibBuilder.loadTexts:
    csqIfDscpToQueueEntry.setStatus("current")
_CsqIfDscpToQueueDirection_Type = IfDirection
_CsqIfDscpToQueueDirection_Object = MibTableColumn
csqIfDscpToQueueDirection = _CsqIfDscpToQueueDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 3, 1, 1),
    _CsqIfDscpToQueueDirection_Type()
)
csqIfDscpToQueueDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfDscpToQueueDirection.setStatus("current")
_CsqIfDscpToQueueDscp_Type = Dscp
_CsqIfDscpToQueueDscp_Object = MibTableColumn
csqIfDscpToQueueDscp = _CsqIfDscpToQueueDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 3, 1, 2),
    _CsqIfDscpToQueueDscp_Type()
)
csqIfDscpToQueueDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfDscpToQueueDscp.setStatus("current")
_CsqIfDscpToQueueQueueNumber_Type = QosQueueNumber
_CsqIfDscpToQueueQueueNumber_Object = MibTableColumn
csqIfDscpToQueueQueueNumber = _CsqIfDscpToQueueQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 3, 1, 3),
    _CsqIfDscpToQueueQueueNumber_Type()
)
csqIfDscpToQueueQueueNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfDscpToQueueQueueNumber.setStatus("current")
_CsqIfDscpToQueueThresholdNumber_Type = QosThresholdNumber
_CsqIfDscpToQueueThresholdNumber_Object = MibTableColumn
csqIfDscpToQueueThresholdNumber = _CsqIfDscpToQueueThresholdNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 3, 1, 4),
    _CsqIfDscpToQueueThresholdNumber_Type()
)
csqIfDscpToQueueThresholdNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfDscpToQueueThresholdNumber.setStatus("current")
_CsqIfDropConfigTable_Object = MibTable
csqIfDropConfigTable = _CsqIfDropConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 4)
)
if mibBuilder.loadTexts:
    csqIfDropConfigTable.setStatus("current")
_CsqIfDropConfigEntry_Object = MibTableRow
csqIfDropConfigEntry = _CsqIfDropConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 4, 1)
)
csqIfDropConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfDropConfigDirection"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfDropConfigQueueIndex"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfDropConfigThresholdIndex"),
)
if mibBuilder.loadTexts:
    csqIfDropConfigEntry.setStatus("current")
_CsqIfDropConfigDirection_Type = IfDirection
_CsqIfDropConfigDirection_Object = MibTableColumn
csqIfDropConfigDirection = _CsqIfDropConfigDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 4, 1, 1),
    _CsqIfDropConfigDirection_Type()
)
csqIfDropConfigDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfDropConfigDirection.setStatus("current")
_CsqIfDropConfigQueueIndex_Type = QosQueueNumber
_CsqIfDropConfigQueueIndex_Object = MibTableColumn
csqIfDropConfigQueueIndex = _CsqIfDropConfigQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 4, 1, 2),
    _CsqIfDropConfigQueueIndex_Type()
)
csqIfDropConfigQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfDropConfigQueueIndex.setStatus("current")
_CsqIfDropConfigThresholdIndex_Type = QosThresholdNumber
_CsqIfDropConfigThresholdIndex_Object = MibTableColumn
csqIfDropConfigThresholdIndex = _CsqIfDropConfigThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 4, 1, 3),
    _CsqIfDropConfigThresholdIndex_Type()
)
csqIfDropConfigThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfDropConfigThresholdIndex.setStatus("current")


class _CsqIfDropConfigDropAlgorithm_Type(Integer32):
    """Custom type csqIfDropConfigDropAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tailDrop", 1),
          ("wred", 2))
    )


_CsqIfDropConfigDropAlgorithm_Type.__name__ = "Integer32"
_CsqIfDropConfigDropAlgorithm_Object = MibTableColumn
csqIfDropConfigDropAlgorithm = _CsqIfDropConfigDropAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 4, 1, 4),
    _CsqIfDropConfigDropAlgorithm_Type()
)
csqIfDropConfigDropAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfDropConfigDropAlgorithm.setStatus("current")


class _CsqIfDropConfigDropThreshold_Type(Percent):
    """Custom type csqIfDropConfigDropThreshold based on Percent"""
    subtypeSpec = Percent.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CsqIfDropConfigDropThreshold_Type.__name__ = "Percent"
_CsqIfDropConfigDropThreshold_Object = MibTableColumn
csqIfDropConfigDropThreshold = _CsqIfDropConfigDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 4, 1, 5),
    _CsqIfDropConfigDropThreshold_Type()
)
csqIfDropConfigDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfDropConfigDropThreshold.setStatus("current")
_CsqIfDropConfigMinWredThreshold_Type = Percent
_CsqIfDropConfigMinWredThreshold_Object = MibTableColumn
csqIfDropConfigMinWredThreshold = _CsqIfDropConfigMinWredThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 4, 1, 6),
    _CsqIfDropConfigMinWredThreshold_Type()
)
csqIfDropConfigMinWredThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfDropConfigMinWredThreshold.setStatus("current")


class _CsqIfDropConfigMaxWredThreshold_Type(Percent):
    """Custom type csqIfDropConfigMaxWredThreshold based on Percent"""
    subtypeSpec = Percent.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CsqIfDropConfigMaxWredThreshold_Type.__name__ = "Percent"
_CsqIfDropConfigMaxWredThreshold_Object = MibTableColumn
csqIfDropConfigMaxWredThreshold = _CsqIfDropConfigMaxWredThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 4, 1, 7),
    _CsqIfDropConfigMaxWredThreshold_Type()
)
csqIfDropConfigMaxWredThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfDropConfigMaxWredThreshold.setStatus("current")


class _CsqIfDropConfigQueueBuffer_Type(Integer32):
    """Custom type csqIfDropConfigQueueBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 2),
          ("percent", 3),
          ("shared", 1))
    )


_CsqIfDropConfigQueueBuffer_Type.__name__ = "Integer32"
_CsqIfDropConfigQueueBuffer_Object = MibTableColumn
csqIfDropConfigQueueBuffer = _CsqIfDropConfigQueueBuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 4, 1, 8),
    _CsqIfDropConfigQueueBuffer_Type()
)
csqIfDropConfigQueueBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfDropConfigQueueBuffer.setStatus("current")
_CsqIfQueueTable_Object = MibTable
csqIfQueueTable = _CsqIfQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 5)
)
if mibBuilder.loadTexts:
    csqIfQueueTable.setStatus("current")
_CsqIfQueueEntry_Object = MibTableRow
csqIfQueueEntry = _CsqIfQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 5, 1)
)
csqIfQueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfQueueDirection"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfQueueNumber"),
)
if mibBuilder.loadTexts:
    csqIfQueueEntry.setStatus("current")
_CsqIfQueueDirection_Type = IfDirection
_CsqIfQueueDirection_Object = MibTableColumn
csqIfQueueDirection = _CsqIfQueueDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 5, 1, 1),
    _CsqIfQueueDirection_Type()
)
csqIfQueueDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfQueueDirection.setStatus("current")
_CsqIfQueueNumber_Type = QosQueueNumber
_CsqIfQueueNumber_Object = MibTableColumn
csqIfQueueNumber = _CsqIfQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 5, 1, 2),
    _CsqIfQueueNumber_Type()
)
csqIfQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfQueueNumber.setStatus("current")


class _CsqIfQueueWrrWeight_Type(Unsigned32):
    """Custom type csqIfQueueWrrWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CsqIfQueueWrrWeight_Type.__name__ = "Unsigned32"
_CsqIfQueueWrrWeight_Object = MibTableColumn
csqIfQueueWrrWeight = _CsqIfQueueWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 5, 1, 3),
    _CsqIfQueueWrrWeight_Type()
)
csqIfQueueWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfQueueWrrWeight.setStatus("current")
_CsqIfQueueSizeWeight_Type = Unsigned32
_CsqIfQueueSizeWeight_Object = MibTableColumn
csqIfQueueSizeWeight = _CsqIfQueueSizeWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 5, 1, 4),
    _CsqIfQueueSizeWeight_Type()
)
csqIfQueueSizeWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfQueueSizeWeight.setStatus("current")


class _CsqIfQueueStatsGranularity_Type(Integer32):
    """Custom type csqIfQueueStatsGranularity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("perQueue", 1),
          ("perQueueThresh", 2))
    )


_CsqIfQueueStatsGranularity_Type.__name__ = "Integer32"
_CsqIfQueueStatsGranularity_Object = MibTableColumn
csqIfQueueStatsGranularity = _CsqIfQueueStatsGranularity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 5, 1, 5),
    _CsqIfQueueStatsGranularity_Type()
)
csqIfQueueStatsGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQueueStatsGranularity.setStatus("current")
_CsqIfQueueClassMapName_Type = SnmpAdminString
_CsqIfQueueClassMapName_Object = MibTableColumn
csqIfQueueClassMapName = _CsqIfQueueClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 5, 1, 6),
    _CsqIfQueueClassMapName_Type()
)
csqIfQueueClassMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfQueueClassMapName.setStatus("current")


class _CsqIfQueueScheduling_Type(Integer32):
    """Custom type csqIfQueueScheduling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("srr", 2),
          ("wrr", 1))
    )


_CsqIfQueueScheduling_Type.__name__ = "Integer32"
_CsqIfQueueScheduling_Object = MibTableColumn
csqIfQueueScheduling = _CsqIfQueueScheduling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 5, 1, 7),
    _CsqIfQueueScheduling_Type()
)
csqIfQueueScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfQueueScheduling.setStatus("current")


class _CsqIfQueueSrrWeight_Type(Unsigned32):
    """Custom type csqIfQueueSrrWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CsqIfQueueSrrWeight_Type.__name__ = "Unsigned32"
_CsqIfQueueSrrWeight_Object = MibTableColumn
csqIfQueueSrrWeight = _CsqIfQueueSrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 5, 1, 8),
    _CsqIfQueueSrrWeight_Type()
)
csqIfQueueSrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfQueueSrrWeight.setStatus("current")
_CsqIfModeConfigTable_Object = MibTable
csqIfModeConfigTable = _CsqIfModeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 6)
)
if mibBuilder.loadTexts:
    csqIfModeConfigTable.setStatus("current")
_CsqIfModeConfigEntry_Object = MibTableRow
csqIfModeConfigEntry = _CsqIfModeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 6, 1)
)
csqIfModeConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    csqIfModeConfigEntry.setStatus("current")
_CsqIfVlanBasedQosModeEnable_Type = TruthValue
_CsqIfVlanBasedQosModeEnable_Object = MibTableColumn
csqIfVlanBasedQosModeEnable = _CsqIfVlanBasedQosModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 6, 1, 1),
    _CsqIfVlanBasedQosModeEnable_Type()
)
csqIfVlanBasedQosModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfVlanBasedQosModeEnable.setStatus("current")
_CsqIfConsistencyCheckTable_Object = MibTable
csqIfConsistencyCheckTable = _CsqIfConsistencyCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 7)
)
if mibBuilder.loadTexts:
    csqIfConsistencyCheckTable.setStatus("current")
_CsqIfConsistencyCheckEntry_Object = MibTableRow
csqIfConsistencyCheckEntry = _CsqIfConsistencyCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 7, 1)
)
csqIfConsistencyCheckEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    csqIfConsistencyCheckEntry.setStatus("current")
_CsqIfConsistencyCheckEnable_Type = TruthValue
_CsqIfConsistencyCheckEnable_Object = MibTableColumn
csqIfConsistencyCheckEnable = _CsqIfConsistencyCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 7, 1, 1),
    _CsqIfConsistencyCheckEnable_Type()
)
csqIfConsistencyCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqIfConsistencyCheckEnable.setStatus("current")
_CsqIfQosGroupInfoTable_Object = MibTable
csqIfQosGroupInfoTable = _CsqIfQosGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8)
)
if mibBuilder.loadTexts:
    csqIfQosGroupInfoTable.setStatus("current")
_CsqIfQosGroupInfoEntry_Object = MibTableRow
csqIfQosGroupInfoEntry = _CsqIfQosGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1)
)
csqIfQosGroupInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfQosGroupInfoDirection"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfQosGroupInfoGroupNumber"),
)
if mibBuilder.loadTexts:
    csqIfQosGroupInfoEntry.setStatus("current")
_CsqIfQosGroupInfoDirection_Type = IfDirection
_CsqIfQosGroupInfoDirection_Object = MibTableColumn
csqIfQosGroupInfoDirection = _CsqIfQosGroupInfoDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1, 1),
    _CsqIfQosGroupInfoDirection_Type()
)
csqIfQosGroupInfoDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfQosGroupInfoDirection.setStatus("current")
_CsqIfQosGroupInfoGroupNumber_Type = Unsigned32
_CsqIfQosGroupInfoGroupNumber_Object = MibTableColumn
csqIfQosGroupInfoGroupNumber = _CsqIfQosGroupInfoGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1, 2),
    _CsqIfQosGroupInfoGroupNumber_Type()
)
csqIfQosGroupInfoGroupNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfQosGroupInfoGroupNumber.setStatus("current")
_CsqIfQosGroupInfoQueueSize_Type = Unsigned32
_CsqIfQosGroupInfoQueueSize_Object = MibTableColumn
csqIfQosGroupInfoQueueSize = _CsqIfQosGroupInfoQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1, 3),
    _CsqIfQosGroupInfoQueueSize_Type()
)
csqIfQosGroupInfoQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQosGroupInfoQueueSize.setStatus("current")
_CsqIfQosGroupInfoHwMTU_Type = Unsigned32
_CsqIfQosGroupInfoHwMTU_Object = MibTableColumn
csqIfQosGroupInfoHwMTU = _CsqIfQosGroupInfoHwMTU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1, 4),
    _CsqIfQosGroupInfoHwMTU_Type()
)
csqIfQosGroupInfoHwMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQosGroupInfoHwMTU.setStatus("current")
_CsqIfQosGroupInfoMTU_Type = Unsigned32
_CsqIfQosGroupInfoMTU_Object = MibTableColumn
csqIfQosGroupInfoMTU = _CsqIfQosGroupInfoMTU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1, 5),
    _CsqIfQosGroupInfoMTU_Type()
)
csqIfQosGroupInfoMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQosGroupInfoMTU.setStatus("current")


class _CsqIfQosGroupInfoDropType_Type(Integer32):
    """Custom type csqIfQosGroupInfoDropType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("noDrop", 2),
          ("notApplicable", 3))
    )


_CsqIfQosGroupInfoDropType_Type.__name__ = "Integer32"
_CsqIfQosGroupInfoDropType_Object = MibTableColumn
csqIfQosGroupInfoDropType = _CsqIfQosGroupInfoDropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1, 6),
    _CsqIfQosGroupInfoDropType_Type()
)
csqIfQosGroupInfoDropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQosGroupInfoDropType.setStatus("current")
_CsqIfQosGroupInfoResumeThresh_Type = Unsigned32
_CsqIfQosGroupInfoResumeThresh_Object = MibTableColumn
csqIfQosGroupInfoResumeThresh = _CsqIfQosGroupInfoResumeThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1, 7),
    _CsqIfQosGroupInfoResumeThresh_Type()
)
csqIfQosGroupInfoResumeThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQosGroupInfoResumeThresh.setStatus("current")
_CsqIfQosGroupInfoPauseThresh_Type = Unsigned32
_CsqIfQosGroupInfoPauseThresh_Object = MibTableColumn
csqIfQosGroupInfoPauseThresh = _CsqIfQosGroupInfoPauseThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1, 8),
    _CsqIfQosGroupInfoPauseThresh_Type()
)
csqIfQosGroupInfoPauseThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQosGroupInfoPauseThresh.setStatus("current")


class _CsqIfQosGroupInfoScheduling_Type(Integer32):
    """Custom type csqIfQosGroupInfoScheduling based on Integer32"""
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
        *(("dwrr", 3),
          ("notApplicable", 4),
          ("priority", 2),
          ("wrr", 1))
    )


_CsqIfQosGroupInfoScheduling_Type.__name__ = "Integer32"
_CsqIfQosGroupInfoScheduling_Object = MibTableColumn
csqIfQosGroupInfoScheduling = _CsqIfQosGroupInfoScheduling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1, 9),
    _CsqIfQosGroupInfoScheduling_Type()
)
csqIfQosGroupInfoScheduling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQosGroupInfoScheduling.setStatus("current")
_CsqIfQosGroupInfoBandwidth_Type = Unsigned32
_CsqIfQosGroupInfoBandwidth_Object = MibTableColumn
csqIfQosGroupInfoBandwidth = _CsqIfQosGroupInfoBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1, 10),
    _CsqIfQosGroupInfoBandwidth_Type()
)
csqIfQosGroupInfoBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQosGroupInfoBandwidth.setStatus("current")


class _CsqIfQosGroupInfoBandwidthUnits_Type(Integer32):
    """Custom type csqIfQosGroupInfoBandwidthUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("notApplicable", 3),
          ("percentage", 2))
    )


_CsqIfQosGroupInfoBandwidthUnits_Type.__name__ = "Integer32"
_CsqIfQosGroupInfoBandwidthUnits_Object = MibTableColumn
csqIfQosGroupInfoBandwidthUnits = _CsqIfQosGroupInfoBandwidthUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1, 11),
    _CsqIfQosGroupInfoBandwidthUnits_Type()
)
csqIfQosGroupInfoBandwidthUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQosGroupInfoBandwidthUnits.setStatus("current")
_CsqIfQosGroupInfoShapeMinThresh_Type = Unsigned32
_CsqIfQosGroupInfoShapeMinThresh_Object = MibTableColumn
csqIfQosGroupInfoShapeMinThresh = _CsqIfQosGroupInfoShapeMinThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1, 12),
    _CsqIfQosGroupInfoShapeMinThresh_Type()
)
csqIfQosGroupInfoShapeMinThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQosGroupInfoShapeMinThresh.setStatus("current")
_CsqIfQosGroupInfoShapeMaxThresh_Type = Unsigned32
_CsqIfQosGroupInfoShapeMaxThresh_Object = MibTableColumn
csqIfQosGroupInfoShapeMaxThresh = _CsqIfQosGroupInfoShapeMaxThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1, 13),
    _CsqIfQosGroupInfoShapeMaxThresh_Type()
)
csqIfQosGroupInfoShapeMaxThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQosGroupInfoShapeMaxThresh.setStatus("current")


class _CsqIfQosGroupInfoShapeUnits_Type(Integer32):
    """Custom type csqIfQosGroupInfoShapeUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("notApplicable", 3),
          ("percentage", 2))
    )


_CsqIfQosGroupInfoShapeUnits_Type.__name__ = "Integer32"
_CsqIfQosGroupInfoShapeUnits_Object = MibTableColumn
csqIfQosGroupInfoShapeUnits = _CsqIfQosGroupInfoShapeUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 4, 8, 1, 14),
    _CsqIfQosGroupInfoShapeUnits_Type()
)
csqIfQosGroupInfoShapeUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQosGroupInfoShapeUnits.setStatus("current")
_CsqStatistics_ObjectIdentity = ObjectIdentity
csqStatistics = _CsqStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5)
)
_CsqIfStatsTable_Object = MibTable
csqIfStatsTable = _CsqIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 1)
)
if mibBuilder.loadTexts:
    csqIfStatsTable.setStatus("current")
_CsqIfStatsEntry_Object = MibTableRow
csqIfStatsEntry = _CsqIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 1, 1)
)
csqIfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfStatsDirection"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfStatsQueueNumber"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfStatsThresholdNumber"),
)
if mibBuilder.loadTexts:
    csqIfStatsEntry.setStatus("current")
_CsqIfStatsDirection_Type = IfDirection
_CsqIfStatsDirection_Object = MibTableColumn
csqIfStatsDirection = _CsqIfStatsDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 1, 1, 1),
    _CsqIfStatsDirection_Type()
)
csqIfStatsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfStatsDirection.setStatus("current")
_CsqIfStatsQueueNumber_Type = QosQueueNumber
_CsqIfStatsQueueNumber_Object = MibTableColumn
csqIfStatsQueueNumber = _CsqIfStatsQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 1, 1, 2),
    _CsqIfStatsQueueNumber_Type()
)
csqIfStatsQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfStatsQueueNumber.setStatus("current")
_CsqIfStatsThresholdNumber_Type = QosThresholdNumber
_CsqIfStatsThresholdNumber_Object = MibTableColumn
csqIfStatsThresholdNumber = _CsqIfStatsThresholdNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 1, 1, 3),
    _CsqIfStatsThresholdNumber_Type()
)
csqIfStatsThresholdNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfStatsThresholdNumber.setStatus("current")
_CsqIfStatsDropPkts_Type = Counter64
_CsqIfStatsDropPkts_Object = MibTableColumn
csqIfStatsDropPkts = _CsqIfStatsDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 1, 1, 4),
    _CsqIfStatsDropPkts_Type()
)
csqIfStatsDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfStatsDropPkts.setStatus("current")
_CsqModuleStatsTable_Object = MibTable
csqModuleStatsTable = _CsqModuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 2)
)
if mibBuilder.loadTexts:
    csqModuleStatsTable.setStatus("current")
_CsqModuleStatsEntry_Object = MibTableRow
csqModuleStatsEntry = _CsqModuleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 2, 1)
)
csqModuleStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    csqModuleStatsEntry.setStatus("current")
_CsqModuleDropByPolicingPackets_Type = Counter64
_CsqModuleDropByPolicingPackets_Object = MibTableColumn
csqModuleDropByPolicingPackets = _CsqModuleDropByPolicingPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 2, 1, 1),
    _CsqModuleDropByPolicingPackets_Type()
)
csqModuleDropByPolicingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleDropByPolicingPackets.setStatus("current")
_CsqModuleTosChangedIpPackets_Type = Counter64
_CsqModuleTosChangedIpPackets_Object = MibTableColumn
csqModuleTosChangedIpPackets = _CsqModuleTosChangedIpPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 2, 1, 2),
    _CsqModuleTosChangedIpPackets_Type()
)
csqModuleTosChangedIpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleTosChangedIpPackets.setStatus("current")
_CsqModuleCosChangedIpPackets_Type = Counter64
_CsqModuleCosChangedIpPackets_Object = MibTableColumn
csqModuleCosChangedIpPackets = _CsqModuleCosChangedIpPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 2, 1, 3),
    _CsqModuleCosChangedIpPackets_Type()
)
csqModuleCosChangedIpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleCosChangedIpPackets.setStatus("current")
_CsqModuleCosChangedNonIpPackets_Type = Counter64
_CsqModuleCosChangedNonIpPackets_Object = MibTableColumn
csqModuleCosChangedNonIpPackets = _CsqModuleCosChangedNonIpPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 2, 1, 4),
    _CsqModuleCosChangedNonIpPackets_Type()
)
csqModuleCosChangedNonIpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleCosChangedNonIpPackets.setStatus("current")
_CsqModuleExpChangedMplsPackets_Type = Counter64
_CsqModuleExpChangedMplsPackets_Object = MibTableColumn
csqModuleExpChangedMplsPackets = _CsqModuleExpChangedMplsPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 2, 1, 5),
    _CsqModuleExpChangedMplsPackets_Type()
)
csqModuleExpChangedMplsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleExpChangedMplsPackets.setStatus("current")
_CsqModuleStatsExtTable_Object = MibTable
csqModuleStatsExtTable = _CsqModuleStatsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3)
)
if mibBuilder.loadTexts:
    csqModuleStatsExtTable.setStatus("current")
_CsqModuleStatsExtEntry_Object = MibTableRow
csqModuleStatsExtEntry = _CsqModuleStatsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1)
)
csqModuleStatsExtEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    csqModuleStatsExtEntry.setStatus("current")
_CsqModuleTunnelEncapPackets_Type = Counter32
_CsqModuleTunnelEncapPackets_Object = MibTableColumn
csqModuleTunnelEncapPackets = _CsqModuleTunnelEncapPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 1),
    _CsqModuleTunnelEncapPackets_Type()
)
csqModuleTunnelEncapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleTunnelEncapPackets.setStatus("current")
_CsqModuleTunnelDecapPackets_Type = Counter32
_CsqModuleTunnelDecapPackets_Object = MibTableColumn
csqModuleTunnelDecapPackets = _CsqModuleTunnelDecapPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 2),
    _CsqModuleTunnelDecapPackets_Type()
)
csqModuleTunnelDecapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleTunnelDecapPackets.setStatus("current")
_CsqModuleDropByPolicingInOctets_Type = Counter64
_CsqModuleDropByPolicingInOctets_Object = MibTableColumn
csqModuleDropByPolicingInOctets = _CsqModuleDropByPolicingInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 3),
    _CsqModuleDropByPolicingInOctets_Type()
)
csqModuleDropByPolicingInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleDropByPolicingInOctets.setStatus("current")
_CsqModuleDropByPolicingOutOctets_Type = Counter64
_CsqModuleDropByPolicingOutOctets_Object = MibTableColumn
csqModuleDropByPolicingOutOctets = _CsqModuleDropByPolicingOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 4),
    _CsqModuleDropByPolicingOutOctets_Type()
)
csqModuleDropByPolicingOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleDropByPolicingOutOctets.setStatus("current")
_CsqModuleFwdByPolicingInPackets_Type = Counter32
_CsqModuleFwdByPolicingInPackets_Object = MibTableColumn
csqModuleFwdByPolicingInPackets = _CsqModuleFwdByPolicingInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 5),
    _CsqModuleFwdByPolicingInPackets_Type()
)
csqModuleFwdByPolicingInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleFwdByPolicingInPackets.setStatus("current")
_CsqModuleFwdByPolicingInOctets_Type = Counter64
_CsqModuleFwdByPolicingInOctets_Object = MibTableColumn
csqModuleFwdByPolicingInOctets = _CsqModuleFwdByPolicingInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 6),
    _CsqModuleFwdByPolicingInOctets_Type()
)
csqModuleFwdByPolicingInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleFwdByPolicingInOctets.setStatus("current")
_CsqModuleFwdByPolicingOutPackets_Type = Counter32
_CsqModuleFwdByPolicingOutPackets_Object = MibTableColumn
csqModuleFwdByPolicingOutPackets = _CsqModuleFwdByPolicingOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 7),
    _CsqModuleFwdByPolicingOutPackets_Type()
)
csqModuleFwdByPolicingOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleFwdByPolicingOutPackets.setStatus("current")
_CsqModuleFwdByPolicingOutOctets_Type = Counter64
_CsqModuleFwdByPolicingOutOctets_Object = MibTableColumn
csqModuleFwdByPolicingOutOctets = _CsqModuleFwdByPolicingOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 8),
    _CsqModuleFwdByPolicingOutOctets_Type()
)
csqModuleFwdByPolicingOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleFwdByPolicingOutOctets.setStatus("current")
_CsqModuleHighExceedInPackets_Type = Counter32
_CsqModuleHighExceedInPackets_Object = MibTableColumn
csqModuleHighExceedInPackets = _CsqModuleHighExceedInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 9),
    _CsqModuleHighExceedInPackets_Type()
)
csqModuleHighExceedInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleHighExceedInPackets.setStatus("current")
_CsqModuleHighExceedInOctets_Type = Counter64
_CsqModuleHighExceedInOctets_Object = MibTableColumn
csqModuleHighExceedInOctets = _CsqModuleHighExceedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 10),
    _CsqModuleHighExceedInOctets_Type()
)
csqModuleHighExceedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleHighExceedInOctets.setStatus("current")
_CsqModuleHighExceedOutPackets_Type = Counter32
_CsqModuleHighExceedOutPackets_Object = MibTableColumn
csqModuleHighExceedOutPackets = _CsqModuleHighExceedOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 11),
    _CsqModuleHighExceedOutPackets_Type()
)
csqModuleHighExceedOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleHighExceedOutPackets.setStatus("current")
_CsqModuleHighExceedOutOctets_Type = Counter64
_CsqModuleHighExceedOutOctets_Object = MibTableColumn
csqModuleHighExceedOutOctets = _CsqModuleHighExceedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 12),
    _CsqModuleHighExceedOutOctets_Type()
)
csqModuleHighExceedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleHighExceedOutOctets.setStatus("current")
_CsqModuleLowExceedInPackets_Type = Counter32
_CsqModuleLowExceedInPackets_Object = MibTableColumn
csqModuleLowExceedInPackets = _CsqModuleLowExceedInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 13),
    _CsqModuleLowExceedInPackets_Type()
)
csqModuleLowExceedInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleLowExceedInPackets.setStatus("current")
_CsqModuleLowExceedInOctets_Type = Counter64
_CsqModuleLowExceedInOctets_Object = MibTableColumn
csqModuleLowExceedInOctets = _CsqModuleLowExceedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 14),
    _CsqModuleLowExceedInOctets_Type()
)
csqModuleLowExceedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleLowExceedInOctets.setStatus("current")
_CsqModuleLowExceedOutPackets_Type = Counter32
_CsqModuleLowExceedOutPackets_Object = MibTableColumn
csqModuleLowExceedOutPackets = _CsqModuleLowExceedOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 15),
    _CsqModuleLowExceedOutPackets_Type()
)
csqModuleLowExceedOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleLowExceedOutPackets.setStatus("current")
_CsqModuleLowExceedOutOctets_Type = Counter64
_CsqModuleLowExceedOutOctets_Object = MibTableColumn
csqModuleLowExceedOutOctets = _CsqModuleLowExceedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 16),
    _CsqModuleLowExceedOutOctets_Type()
)
csqModuleLowExceedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleLowExceedOutOctets.setStatus("current")
_CsqModuleDropByAggPolicerInPackets_Type = Counter32
_CsqModuleDropByAggPolicerInPackets_Object = MibTableColumn
csqModuleDropByAggPolicerInPackets = _CsqModuleDropByAggPolicerInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 17),
    _CsqModuleDropByAggPolicerInPackets_Type()
)
csqModuleDropByAggPolicerInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleDropByAggPolicerInPackets.setStatus("current")
_CsqModuleDropByAggPolicerInOctets_Type = Counter64
_CsqModuleDropByAggPolicerInOctets_Object = MibTableColumn
csqModuleDropByAggPolicerInOctets = _CsqModuleDropByAggPolicerInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 18),
    _CsqModuleDropByAggPolicerInOctets_Type()
)
csqModuleDropByAggPolicerInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleDropByAggPolicerInOctets.setStatus("current")
_CsqModuleDropByAggPolicerOutPackets_Type = Counter32
_CsqModuleDropByAggPolicerOutPackets_Object = MibTableColumn
csqModuleDropByAggPolicerOutPackets = _CsqModuleDropByAggPolicerOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 19),
    _CsqModuleDropByAggPolicerOutPackets_Type()
)
csqModuleDropByAggPolicerOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleDropByAggPolicerOutPackets.setStatus("current")
_CsqModuleDropByAggPolicerOutOctets_Type = Counter64
_CsqModuleDropByAggPolicerOutOctets_Object = MibTableColumn
csqModuleDropByAggPolicerOutOctets = _CsqModuleDropByAggPolicerOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 20),
    _CsqModuleDropByAggPolicerOutOctets_Type()
)
csqModuleDropByAggPolicerOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleDropByAggPolicerOutOctets.setStatus("current")
_CsqModuleFwdByAggPolicerInPackets_Type = Counter32
_CsqModuleFwdByAggPolicerInPackets_Object = MibTableColumn
csqModuleFwdByAggPolicerInPackets = _CsqModuleFwdByAggPolicerInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 21),
    _CsqModuleFwdByAggPolicerInPackets_Type()
)
csqModuleFwdByAggPolicerInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleFwdByAggPolicerInPackets.setStatus("current")
_CsqModuleFwdByAggPolicerInOctets_Type = Counter64
_CsqModuleFwdByAggPolicerInOctets_Object = MibTableColumn
csqModuleFwdByAggPolicerInOctets = _CsqModuleFwdByAggPolicerInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 22),
    _CsqModuleFwdByAggPolicerInOctets_Type()
)
csqModuleFwdByAggPolicerInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleFwdByAggPolicerInOctets.setStatus("current")
_CsqModuleFwdByAggPolicerOutPackets_Type = Counter32
_CsqModuleFwdByAggPolicerOutPackets_Object = MibTableColumn
csqModuleFwdByAggPolicerOutPackets = _CsqModuleFwdByAggPolicerOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 23),
    _CsqModuleFwdByAggPolicerOutPackets_Type()
)
csqModuleFwdByAggPolicerOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleFwdByAggPolicerOutPackets.setStatus("current")
_CsqModuleFwdByAggPolicerOutOctets_Type = Counter64
_CsqModuleFwdByAggPolicerOutOctets_Object = MibTableColumn
csqModuleFwdByAggPolicerOutOctets = _CsqModuleFwdByAggPolicerOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 24),
    _CsqModuleFwdByAggPolicerOutOctets_Type()
)
csqModuleFwdByAggPolicerOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleFwdByAggPolicerOutOctets.setStatus("current")
_CsqModuleAggHighExceedInPackets_Type = Counter32
_CsqModuleAggHighExceedInPackets_Object = MibTableColumn
csqModuleAggHighExceedInPackets = _CsqModuleAggHighExceedInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 25),
    _CsqModuleAggHighExceedInPackets_Type()
)
csqModuleAggHighExceedInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleAggHighExceedInPackets.setStatus("current")
_CsqModuleAggHighExceedInOctets_Type = Counter64
_CsqModuleAggHighExceedInOctets_Object = MibTableColumn
csqModuleAggHighExceedInOctets = _CsqModuleAggHighExceedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 26),
    _CsqModuleAggHighExceedInOctets_Type()
)
csqModuleAggHighExceedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleAggHighExceedInOctets.setStatus("current")
_CsqModuleAggHighExceedOutPackets_Type = Counter32
_CsqModuleAggHighExceedOutPackets_Object = MibTableColumn
csqModuleAggHighExceedOutPackets = _CsqModuleAggHighExceedOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 27),
    _CsqModuleAggHighExceedOutPackets_Type()
)
csqModuleAggHighExceedOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleAggHighExceedOutPackets.setStatus("current")
_CsqModuleAggHighExceedOutOctets_Type = Counter64
_CsqModuleAggHighExceedOutOctets_Object = MibTableColumn
csqModuleAggHighExceedOutOctets = _CsqModuleAggHighExceedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 28),
    _CsqModuleAggHighExceedOutOctets_Type()
)
csqModuleAggHighExceedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleAggHighExceedOutOctets.setStatus("current")
_CsqModuleAggLowExceedInPackets_Type = Counter32
_CsqModuleAggLowExceedInPackets_Object = MibTableColumn
csqModuleAggLowExceedInPackets = _CsqModuleAggLowExceedInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 29),
    _CsqModuleAggLowExceedInPackets_Type()
)
csqModuleAggLowExceedInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleAggLowExceedInPackets.setStatus("current")
_CsqModuleAggLowExceedInOctets_Type = Counter64
_CsqModuleAggLowExceedInOctets_Object = MibTableColumn
csqModuleAggLowExceedInOctets = _CsqModuleAggLowExceedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 30),
    _CsqModuleAggLowExceedInOctets_Type()
)
csqModuleAggLowExceedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleAggLowExceedInOctets.setStatus("current")
_CsqModuleAggLowExceedOutPackets_Type = Counter32
_CsqModuleAggLowExceedOutPackets_Object = MibTableColumn
csqModuleAggLowExceedOutPackets = _CsqModuleAggLowExceedOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 31),
    _CsqModuleAggLowExceedOutPackets_Type()
)
csqModuleAggLowExceedOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleAggLowExceedOutPackets.setStatus("current")
_CsqModuleAggLowExceedOutOctets_Type = Counter64
_CsqModuleAggLowExceedOutOctets_Object = MibTableColumn
csqModuleAggLowExceedOutOctets = _CsqModuleAggLowExceedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 32),
    _CsqModuleAggLowExceedOutOctets_Type()
)
csqModuleAggLowExceedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleAggLowExceedOutOctets.setStatus("current")
_CsqModuleDropByNetflowInPackets_Type = Counter32
_CsqModuleDropByNetflowInPackets_Object = MibTableColumn
csqModuleDropByNetflowInPackets = _CsqModuleDropByNetflowInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 33),
    _CsqModuleDropByNetflowInPackets_Type()
)
csqModuleDropByNetflowInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleDropByNetflowInPackets.setStatus("current")
_CsqModuleDropByNetflowInOctets_Type = Counter64
_CsqModuleDropByNetflowInOctets_Object = MibTableColumn
csqModuleDropByNetflowInOctets = _CsqModuleDropByNetflowInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 34),
    _CsqModuleDropByNetflowInOctets_Type()
)
csqModuleDropByNetflowInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleDropByNetflowInOctets.setStatus("current")
_CsqModuleDropByNetflowOutPackets_Type = Counter32
_CsqModuleDropByNetflowOutPackets_Object = MibTableColumn
csqModuleDropByNetflowOutPackets = _CsqModuleDropByNetflowOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 35),
    _CsqModuleDropByNetflowOutPackets_Type()
)
csqModuleDropByNetflowOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleDropByNetflowOutPackets.setStatus("current")
_CsqModuleDropByNetflowOutOctets_Type = Counter64
_CsqModuleDropByNetflowOutOctets_Object = MibTableColumn
csqModuleDropByNetflowOutOctets = _CsqModuleDropByNetflowOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 36),
    _CsqModuleDropByNetflowOutOctets_Type()
)
csqModuleDropByNetflowOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleDropByNetflowOutOctets.setStatus("current")
_CsqModuleFwdByNetflowInPackets_Type = Counter32
_CsqModuleFwdByNetflowInPackets_Object = MibTableColumn
csqModuleFwdByNetflowInPackets = _CsqModuleFwdByNetflowInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 37),
    _CsqModuleFwdByNetflowInPackets_Type()
)
csqModuleFwdByNetflowInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleFwdByNetflowInPackets.setStatus("current")
_CsqModuleFwdByNetflowInOctets_Type = Counter64
_CsqModuleFwdByNetflowInOctets_Object = MibTableColumn
csqModuleFwdByNetflowInOctets = _CsqModuleFwdByNetflowInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 38),
    _CsqModuleFwdByNetflowInOctets_Type()
)
csqModuleFwdByNetflowInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleFwdByNetflowInOctets.setStatus("current")
_CsqModuleFwdByNetflowOutPackets_Type = Counter32
_CsqModuleFwdByNetflowOutPackets_Object = MibTableColumn
csqModuleFwdByNetflowOutPackets = _CsqModuleFwdByNetflowOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 39),
    _CsqModuleFwdByNetflowOutPackets_Type()
)
csqModuleFwdByNetflowOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleFwdByNetflowOutPackets.setStatus("current")
_CsqModuleFwdByNetflowOutOctets_Type = Counter64
_CsqModuleFwdByNetflowOutOctets_Object = MibTableColumn
csqModuleFwdByNetflowOutOctets = _CsqModuleFwdByNetflowOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 40),
    _CsqModuleFwdByNetflowOutOctets_Type()
)
csqModuleFwdByNetflowOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleFwdByNetflowOutOctets.setStatus("current")
_CsqModuleNetflowExceedInPackets_Type = Counter32
_CsqModuleNetflowExceedInPackets_Object = MibTableColumn
csqModuleNetflowExceedInPackets = _CsqModuleNetflowExceedInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 41),
    _CsqModuleNetflowExceedInPackets_Type()
)
csqModuleNetflowExceedInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleNetflowExceedInPackets.setStatus("current")
_CsqModuleNetflowExceedInOctets_Type = Counter64
_CsqModuleNetflowExceedInOctets_Object = MibTableColumn
csqModuleNetflowExceedInOctets = _CsqModuleNetflowExceedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 42),
    _CsqModuleNetflowExceedInOctets_Type()
)
csqModuleNetflowExceedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleNetflowExceedInOctets.setStatus("current")
_CsqModuleNetflowExceedOutPackets_Type = Counter32
_CsqModuleNetflowExceedOutPackets_Object = MibTableColumn
csqModuleNetflowExceedOutPackets = _CsqModuleNetflowExceedOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 43),
    _CsqModuleNetflowExceedOutPackets_Type()
)
csqModuleNetflowExceedOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleNetflowExceedOutPackets.setStatus("current")
_CsqModuleNetflowExceedOutOctets_Type = Counter64
_CsqModuleNetflowExceedOutOctets_Object = MibTableColumn
csqModuleNetflowExceedOutOctets = _CsqModuleNetflowExceedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 44),
    _CsqModuleNetflowExceedOutOctets_Type()
)
csqModuleNetflowExceedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleNetflowExceedOutOctets.setStatus("current")
_CsqModuleCosChangedPackets_Type = Counter32
_CsqModuleCosChangedPackets_Object = MibTableColumn
csqModuleCosChangedPackets = _CsqModuleCosChangedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 45),
    _CsqModuleCosChangedPackets_Type()
)
csqModuleCosChangedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleCosChangedPackets.setStatus("current")
_CsqModuleTrafficClassChangedPackets_Type = Counter32
_CsqModuleTrafficClassChangedPackets_Object = MibTableColumn
csqModuleTrafficClassChangedPackets = _CsqModuleTrafficClassChangedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 3, 1, 46),
    _CsqModuleTrafficClassChangedPackets_Type()
)
csqModuleTrafficClassChangedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqModuleTrafficClassChangedPackets.setStatus("current")
_CsqIfStatsExtTable_Object = MibTable
csqIfStatsExtTable = _CsqIfStatsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 4)
)
if mibBuilder.loadTexts:
    csqIfStatsExtTable.setStatus("current")
_CsqIfStatsExtEntry_Object = MibTableRow
csqIfStatsExtEntry = _CsqIfStatsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 4, 1)
)
csqIfStatsExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfStatsDirection"),
)
if mibBuilder.loadTexts:
    csqIfStatsExtEntry.setStatus("current")
_CsqIfBpduDropPkts_Type = Counter64
_CsqIfBpduDropPkts_Object = MibTableColumn
csqIfBpduDropPkts = _CsqIfBpduDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 4, 1, 1),
    _CsqIfBpduDropPkts_Type()
)
csqIfBpduDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfBpduDropPkts.setStatus("current")
_CsqIfQosGroupStatsTable_Object = MibTable
csqIfQosGroupStatsTable = _CsqIfQosGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 5)
)
if mibBuilder.loadTexts:
    csqIfQosGroupStatsTable.setStatus("current")
_CsqIfQosGroupStatsEntry_Object = MibTableRow
csqIfQosGroupStatsEntry = _CsqIfQosGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 5, 1)
)
csqIfQosGroupStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfQosGroupStatsDirection"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfQosGroupStatsGroupNumber"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfQosGroupStatsType"),
)
if mibBuilder.loadTexts:
    csqIfQosGroupStatsEntry.setStatus("current")
_CsqIfQosGroupStatsDirection_Type = IfDirection
_CsqIfQosGroupStatsDirection_Object = MibTableColumn
csqIfQosGroupStatsDirection = _CsqIfQosGroupStatsDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 5, 1, 1),
    _CsqIfQosGroupStatsDirection_Type()
)
csqIfQosGroupStatsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfQosGroupStatsDirection.setStatus("current")
_CsqIfQosGroupStatsGroupNumber_Type = Unsigned32
_CsqIfQosGroupStatsGroupNumber_Object = MibTableColumn
csqIfQosGroupStatsGroupNumber = _CsqIfQosGroupStatsGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 5, 1, 2),
    _CsqIfQosGroupStatsGroupNumber_Type()
)
csqIfQosGroupStatsGroupNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfQosGroupStatsGroupNumber.setStatus("current")
_CsqIfQosGroupStatsType_Type = QosStatsType
_CsqIfQosGroupStatsType_Object = MibTableColumn
csqIfQosGroupStatsType = _CsqIfQosGroupStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 5, 1, 3),
    _CsqIfQosGroupStatsType_Type()
)
csqIfQosGroupStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfQosGroupStatsType.setStatus("current")
_CsqIfQosGroupStatsValue_Type = Counter64
_CsqIfQosGroupStatsValue_Object = MibTableColumn
csqIfQosGroupStatsValue = _CsqIfQosGroupStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 5, 1, 4),
    _CsqIfQosGroupStatsValue_Type()
)
csqIfQosGroupStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfQosGroupStatsValue.setStatus("current")
_CsqIfPriGrpInBufUsageTable_Object = MibTable
csqIfPriGrpInBufUsageTable = _CsqIfPriGrpInBufUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 6)
)
if mibBuilder.loadTexts:
    csqIfPriGrpInBufUsageTable.setStatus("current")
_CsqIfPriGrpInBufUsageEntry_Object = MibTableRow
csqIfPriGrpInBufUsageEntry = _CsqIfPriGrpInBufUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 6, 1)
)
csqIfPriGrpInBufUsageEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqIfPriGrpInBufUsageGrpNo"),
)
if mibBuilder.loadTexts:
    csqIfPriGrpInBufUsageEntry.setStatus("current")
_CsqIfPriGrpInBufUsageGrpNo_Type = Unsigned32
_CsqIfPriGrpInBufUsageGrpNo_Object = MibTableColumn
csqIfPriGrpInBufUsageGrpNo = _CsqIfPriGrpInBufUsageGrpNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 6, 1, 1),
    _CsqIfPriGrpInBufUsageGrpNo_Type()
)
csqIfPriGrpInBufUsageGrpNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqIfPriGrpInBufUsageGrpNo.setStatus("current")
_CsqIfPriGrpInBufUsageMinCount_Type = Unsigned32
_CsqIfPriGrpInBufUsageMinCount_Object = MibTableColumn
csqIfPriGrpInBufUsageMinCount = _CsqIfPriGrpInBufUsageMinCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 6, 1, 2),
    _CsqIfPriGrpInBufUsageMinCount_Type()
)
csqIfPriGrpInBufUsageMinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfPriGrpInBufUsageMinCount.setStatus("current")
_CsqIfPriGrpInBufUsageSharedCount_Type = Unsigned32
_CsqIfPriGrpInBufUsageSharedCount_Object = MibTableColumn
csqIfPriGrpInBufUsageSharedCount = _CsqIfPriGrpInBufUsageSharedCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 6, 1, 3),
    _CsqIfPriGrpInBufUsageSharedCount_Type()
)
csqIfPriGrpInBufUsageSharedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfPriGrpInBufUsageSharedCount.setStatus("current")
_CsqIfPriGrpInBufUsageHeadroomCount_Type = Unsigned32
_CsqIfPriGrpInBufUsageHeadroomCount_Object = MibTableColumn
csqIfPriGrpInBufUsageHeadroomCount = _CsqIfPriGrpInBufUsageHeadroomCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 6, 1, 4),
    _CsqIfPriGrpInBufUsageHeadroomCount_Type()
)
csqIfPriGrpInBufUsageHeadroomCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfPriGrpInBufUsageHeadroomCount.setStatus("current")
_CsqIfPriGrpInBufUsageGlobalHeadroomCount_Type = Unsigned32
_CsqIfPriGrpInBufUsageGlobalHeadroomCount_Object = MibTableColumn
csqIfPriGrpInBufUsageGlobalHeadroomCount = _CsqIfPriGrpInBufUsageGlobalHeadroomCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 6, 1, 5),
    _CsqIfPriGrpInBufUsageGlobalHeadroomCount_Type()
)
csqIfPriGrpInBufUsageGlobalHeadroomCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfPriGrpInBufUsageGlobalHeadroomCount.setStatus("current")
_CsqIfPriGrpInBufUsageSharedPeekCount_Type = Unsigned32
_CsqIfPriGrpInBufUsageSharedPeekCount_Object = MibTableColumn
csqIfPriGrpInBufUsageSharedPeekCount = _CsqIfPriGrpInBufUsageSharedPeekCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 6, 1, 6),
    _CsqIfPriGrpInBufUsageSharedPeekCount_Type()
)
csqIfPriGrpInBufUsageSharedPeekCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfPriGrpInBufUsageSharedPeekCount.setStatus("current")
_CsqIfPriGrpInBufUsageHeadroomPeekCount_Type = Unsigned32
_CsqIfPriGrpInBufUsageHeadroomPeekCount_Object = MibTableColumn
csqIfPriGrpInBufUsageHeadroomPeekCount = _CsqIfPriGrpInBufUsageHeadroomPeekCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 6, 1, 7),
    _CsqIfPriGrpInBufUsageHeadroomPeekCount_Type()
)
csqIfPriGrpInBufUsageHeadroomPeekCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqIfPriGrpInBufUsageHeadroomPeekCount.setStatus("current")
_CsqSharedPoolUsageTable_Object = MibTable
csqSharedPoolUsageTable = _CsqSharedPoolUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 7)
)
if mibBuilder.loadTexts:
    csqSharedPoolUsageTable.setStatus("current")
_CsqSharedPoolUsageEntry_Object = MibTableRow
csqSharedPoolUsageEntry = _CsqSharedPoolUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 7, 1)
)
csqSharedPoolUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqSharedPoolUsageInstNo"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqSharedPoolUsagePoolNo"),
)
if mibBuilder.loadTexts:
    csqSharedPoolUsageEntry.setStatus("current")
_CsqSharedPoolUsageInstNo_Type = Unsigned32
_CsqSharedPoolUsageInstNo_Object = MibTableColumn
csqSharedPoolUsageInstNo = _CsqSharedPoolUsageInstNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 7, 1, 1),
    _CsqSharedPoolUsageInstNo_Type()
)
csqSharedPoolUsageInstNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqSharedPoolUsageInstNo.setStatus("current")
_CsqSharedPoolUsagePoolNo_Type = Unsigned32
_CsqSharedPoolUsagePoolNo_Object = MibTableColumn
csqSharedPoolUsagePoolNo = _CsqSharedPoolUsagePoolNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 7, 1, 2),
    _CsqSharedPoolUsagePoolNo_Type()
)
csqSharedPoolUsagePoolNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqSharedPoolUsagePoolNo.setStatus("current")
_CsqSharedPoolUsageUsed_Type = Unsigned32
_CsqSharedPoolUsageUsed_Object = MibTableColumn
csqSharedPoolUsageUsed = _CsqSharedPoolUsageUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 7, 1, 3),
    _CsqSharedPoolUsageUsed_Type()
)
csqSharedPoolUsageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqSharedPoolUsageUsed.setStatus("current")
_CsqSharedPoolUsageRemain_Type = Unsigned32
_CsqSharedPoolUsageRemain_Object = MibTableColumn
csqSharedPoolUsageRemain = _CsqSharedPoolUsageRemain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 7, 1, 4),
    _CsqSharedPoolUsageRemain_Type()
)
csqSharedPoolUsageRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqSharedPoolUsageRemain.setStatus("current")
_CsqSharedPoolUsagePeak_Type = Unsigned32
_CsqSharedPoolUsagePeak_Object = MibTableColumn
csqSharedPoolUsagePeak = _CsqSharedPoolUsagePeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 7, 1, 5),
    _CsqSharedPoolUsagePeak_Type()
)
csqSharedPoolUsagePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqSharedPoolUsagePeak.setStatus("current")
_CsqSharedPoolUsageTotal_Type = Unsigned32
_CsqSharedPoolUsageTotal_Object = MibTableColumn
csqSharedPoolUsageTotal = _CsqSharedPoolUsageTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 7, 1, 6),
    _CsqSharedPoolUsageTotal_Type()
)
csqSharedPoolUsageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqSharedPoolUsageTotal.setStatus("current")
_CsqSharedPoolUsageUsedTx_Type = Unsigned32
_CsqSharedPoolUsageUsedTx_Object = MibTableColumn
csqSharedPoolUsageUsedTx = _CsqSharedPoolUsageUsedTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 7, 1, 7),
    _CsqSharedPoolUsageUsedTx_Type()
)
csqSharedPoolUsageUsedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqSharedPoolUsageUsedTx.setStatus("current")
_CsqSharedPoolUsageRemainTx_Type = Unsigned32
_CsqSharedPoolUsageRemainTx_Object = MibTableColumn
csqSharedPoolUsageRemainTx = _CsqSharedPoolUsageRemainTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 7, 1, 8),
    _CsqSharedPoolUsageRemainTx_Type()
)
csqSharedPoolUsageRemainTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqSharedPoolUsageRemainTx.setStatus("current")
_CsqSharedPoolUsagePeakTx_Type = Unsigned32
_CsqSharedPoolUsagePeakTx_Object = MibTableColumn
csqSharedPoolUsagePeakTx = _CsqSharedPoolUsagePeakTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 7, 1, 9),
    _CsqSharedPoolUsagePeakTx_Type()
)
csqSharedPoolUsagePeakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqSharedPoolUsagePeakTx.setStatus("current")
_CsqSharedPoolUsageTotalTx_Type = Unsigned32
_CsqSharedPoolUsageTotalTx_Object = MibTableColumn
csqSharedPoolUsageTotalTx = _CsqSharedPoolUsageTotalTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 7, 1, 10),
    _CsqSharedPoolUsageTotalTx_Type()
)
csqSharedPoolUsageTotalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqSharedPoolUsageTotalTx.setStatus("current")
_CsqSharedPoolUsageNameTx_Type = SnmpAdminString
_CsqSharedPoolUsageNameTx_Object = MibTableColumn
csqSharedPoolUsageNameTx = _CsqSharedPoolUsageNameTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 7, 1, 11),
    _CsqSharedPoolUsageNameTx_Type()
)
csqSharedPoolUsageNameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqSharedPoolUsageNameTx.setStatus("current")
_CsqHwSharedPoolUsageTable_Object = MibTable
csqHwSharedPoolUsageTable = _CsqHwSharedPoolUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 8)
)
if mibBuilder.loadTexts:
    csqHwSharedPoolUsageTable.setStatus("current")
_CsqHwSharedPoolUsageEntry_Object = MibTableRow
csqHwSharedPoolUsageEntry = _CsqHwSharedPoolUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 8, 1)
)
csqHwSharedPoolUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqHwSharedPoolDeviceId"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqHwSharedPoolUsageInstNo"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqHwSharedPoolStatsDirection"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqHwSharedPoolStatsType"),
)
if mibBuilder.loadTexts:
    csqHwSharedPoolUsageEntry.setStatus("current")


class _CsqHwSharedPoolDeviceId_Type(Integer32):
    """Custom type csqHwSharedPoolDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("northStar", 1)
    )


_CsqHwSharedPoolDeviceId_Type.__name__ = "Integer32"
_CsqHwSharedPoolDeviceId_Object = MibTableColumn
csqHwSharedPoolDeviceId = _CsqHwSharedPoolDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 8, 1, 1),
    _CsqHwSharedPoolDeviceId_Type()
)
csqHwSharedPoolDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqHwSharedPoolDeviceId.setStatus("current")
_CsqHwSharedPoolUsageInstNo_Type = Unsigned32
_CsqHwSharedPoolUsageInstNo_Object = MibTableColumn
csqHwSharedPoolUsageInstNo = _CsqHwSharedPoolUsageInstNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 8, 1, 2),
    _CsqHwSharedPoolUsageInstNo_Type()
)
csqHwSharedPoolUsageInstNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqHwSharedPoolUsageInstNo.setStatus("current")


class _CsqHwSharedPoolStatsDirection_Type(Integer32):
    """Custom type csqHwSharedPoolStatsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("inputStats_egress", 3),
          ("inputStats_ingressHairpin", 2),
          ("inputStats_ingressStraight", 1),
          ("outputStats_egress", 6),
          ("outputStats_ingressHairpin", 5),
          ("outputStats_ingressStraight", 4))
    )


_CsqHwSharedPoolStatsDirection_Type.__name__ = "Integer32"
_CsqHwSharedPoolStatsDirection_Object = MibTableColumn
csqHwSharedPoolStatsDirection = _CsqHwSharedPoolStatsDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 8, 1, 3),
    _CsqHwSharedPoolStatsDirection_Type()
)
csqHwSharedPoolStatsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqHwSharedPoolStatsDirection.setStatus("current")


class _CsqHwSharedPoolStatsType_Type(Integer32):
    """Custom type csqHwSharedPoolStatsType based on Integer32"""
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
        *(("drop", 1),
          ("nodrop", 2),
          ("span", 3),
          ("sup", 4))
    )


_CsqHwSharedPoolStatsType_Type.__name__ = "Integer32"
_CsqHwSharedPoolStatsType_Object = MibTableColumn
csqHwSharedPoolStatsType = _CsqHwSharedPoolStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 8, 1, 4),
    _CsqHwSharedPoolStatsType_Type()
)
csqHwSharedPoolStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqHwSharedPoolStatsType.setStatus("current")
_CsqHwSharedPoolUsageUsed_Type = Unsigned32
_CsqHwSharedPoolUsageUsed_Object = MibTableColumn
csqHwSharedPoolUsageUsed = _CsqHwSharedPoolUsageUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 8, 1, 5),
    _CsqHwSharedPoolUsageUsed_Type()
)
csqHwSharedPoolUsageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqHwSharedPoolUsageUsed.setStatus("current")
_CsqHwSharedPoolUsageRemain_Type = Unsigned32
_CsqHwSharedPoolUsageRemain_Object = MibTableColumn
csqHwSharedPoolUsageRemain = _CsqHwSharedPoolUsageRemain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 8, 1, 6),
    _CsqHwSharedPoolUsageRemain_Type()
)
csqHwSharedPoolUsageRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqHwSharedPoolUsageRemain.setStatus("current")
_CsqHwSharedPoolUsageShared_Type = Unsigned32
_CsqHwSharedPoolUsageShared_Object = MibTableColumn
csqHwSharedPoolUsageShared = _CsqHwSharedPoolUsageShared_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 8, 1, 7),
    _CsqHwSharedPoolUsageShared_Type()
)
csqHwSharedPoolUsageShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqHwSharedPoolUsageShared.setStatus("current")
_CsqHwSharedPoolUsageTotal_Type = Unsigned32
_CsqHwSharedPoolUsageTotal_Object = MibTableColumn
csqHwSharedPoolUsageTotal = _CsqHwSharedPoolUsageTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 5, 8, 1, 8),
    _CsqHwSharedPoolUsageTotal_Type()
)
csqHwSharedPoolUsageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqHwSharedPoolUsageTotal.setStatus("current")
_CsqPolicerUsage_ObjectIdentity = ObjectIdentity
csqPolicerUsage = _CsqPolicerUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 6)
)
_CsqPolicerUsageTable_Object = MibTable
csqPolicerUsageTable = _CsqPolicerUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 6, 1)
)
if mibBuilder.loadTexts:
    csqPolicerUsageTable.setStatus("current")
_CsqPolicerUsageEntry_Object = MibTableRow
csqPolicerUsageEntry = _CsqPolicerUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 6, 1, 1)
)
csqPolicerUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-QOS-MIB", "csqPolicerType"),
)
if mibBuilder.loadTexts:
    csqPolicerUsageEntry.setStatus("current")
_CsqPolicerType_Type = QosPolicerType
_CsqPolicerType_Object = MibTableColumn
csqPolicerType = _CsqPolicerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 6, 1, 1, 1),
    _CsqPolicerType_Type()
)
csqPolicerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csqPolicerType.setStatus("current")
_CsqPolicerUsed_Type = Unsigned32
_CsqPolicerUsed_Object = MibTableColumn
csqPolicerUsed = _CsqPolicerUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 6, 1, 1, 2),
    _CsqPolicerUsed_Type()
)
csqPolicerUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqPolicerUsed.setStatus("current")
_CsqPolicerTotal_Type = Unsigned32
_CsqPolicerTotal_Object = MibTableColumn
csqPolicerTotal = _CsqPolicerTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 6, 1, 1, 3),
    _CsqPolicerTotal_Type()
)
csqPolicerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csqPolicerTotal.setStatus("current")
_CsqModule_ObjectIdentity = ObjectIdentity
csqModule = _CsqModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 7)
)
_CsqModuleDscpRewriteEnableTable_Object = MibTable
csqModuleDscpRewriteEnableTable = _CsqModuleDscpRewriteEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 7, 1)
)
if mibBuilder.loadTexts:
    csqModuleDscpRewriteEnableTable.setStatus("current")
_CsqModuleDscpRewriteEnableEntry_Object = MibTableRow
csqModuleDscpRewriteEnableEntry = _CsqModuleDscpRewriteEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 7, 1, 1)
)
csqModuleDscpRewriteEnableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    csqModuleDscpRewriteEnableEntry.setStatus("current")
_CsqModuleDscpRewriteEnable_Type = TruthValue
_CsqModuleDscpRewriteEnable_Object = MibTableColumn
csqModuleDscpRewriteEnable = _CsqModuleDscpRewriteEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 1, 7, 1, 1, 1),
    _CsqModuleDscpRewriteEnable_Type()
)
csqModuleDscpRewriteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csqModuleDscpRewriteEnable.setStatus("current")
_CiscoSwitchQosMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSwitchQosMIBConformance = _CiscoSwitchQosMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2)
)
_CiscoSwitchQosMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSwitchQosMIBCompliances = _CiscoSwitchQosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 1)
)
_CiscoSwitchQosMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSwitchQosMIBGroups = _CiscoSwitchQosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2)
)

# Managed Objects groups

ciscoSwitchQosMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 1)
)
ciscoSwitchQosMappingGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqCosToDscpDscp"),
        ("CISCO-SWITCH-QOS-MIB", "csqIpPrecToDscpDscp"),
        ("CISCO-SWITCH-QOS-MIB", "csqExpToDscpDscp"),
        ("CISCO-SWITCH-QOS-MIB", "csqDscpMappingCos"),
        ("CISCO-SWITCH-QOS-MIB", "csqDscpMappingExp"),
        ("CISCO-SWITCH-QOS-MIB", "csqDscpMappingNormalBurstDscp"),
        ("CISCO-SWITCH-QOS-MIB", "csqDscpMappingMaxBurstDscp"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosMappingGroup.setStatus("current")

ciscoSwitchQosMutationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 2)
)
ciscoSwitchQosMutationGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqMaxCosMutationMap"),
        ("CISCO-SWITCH-QOS-MIB", "csqMaxDscpMutationMap"),
        ("CISCO-SWITCH-QOS-MIB", "csqMaxExpMutationMap"),
        ("CISCO-SWITCH-QOS-MIB", "csqCosMutationRowStatus"),
        ("CISCO-SWITCH-QOS-MIB", "csqDscpMutationRowStatus"),
        ("CISCO-SWITCH-QOS-MIB", "csqExpMutationRowStatus"),
        ("CISCO-SWITCH-QOS-MIB", "csqCosMutationToCos"),
        ("CISCO-SWITCH-QOS-MIB", "csqDscpMutationToDscp"),
        ("CISCO-SWITCH-QOS-MIB", "csqExpMutationToExp"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfCosMutationMap"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfDscpMutationMap"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfExpMutationMap"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfMutationRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosMutationGroup.setStatus("current")

ciscoSwitchQosIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 3)
)
ciscoSwitchQosIfConfigGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqIfDefaultCos"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfTrustState"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfConfigGroup.setStatus("current")

ciscoSwitchQosIfCosToQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 4)
)
ciscoSwitchQosIfCosToQueueGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqIfCosToQueueQueueNumber"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfCosToQueueThresholdNumber"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfCosToQueueGroup.setStatus("current")

ciscoSwitchQosIfDropConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 5)
)
ciscoSwitchQosIfDropConfigGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqIfDropConfigDropAlgorithm"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfDropConfigDropThreshold"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfDropConfigMinWredThreshold"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfDropConfigMaxWredThreshold"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfDropConfigGroup.setStatus("current")

ciscoSwitchQosIfQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 6)
)
ciscoSwitchQosIfQueueGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqIfQueueWrrWeight"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfQueueSizeWeight"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfQueueStatsGranularity"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfQueueGroup.setStatus("current")

ciscoSwitchQosIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 7)
)
ciscoSwitchQosIfStatsGroup.setObjects(
    ("CISCO-SWITCH-QOS-MIB", "csqIfStatsDropPkts")
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfStatsGroup.setStatus("current")

ciscoSwitchQosModuleStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 8)
)
ciscoSwitchQosModuleStatsGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqModuleDropByPolicingPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleTosChangedIpPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleCosChangedIpPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleCosChangedNonIpPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleExpChangedMplsPackets"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosModuleStatsGroup.setStatus("current")

ciscoSwitchQosIfDscpAssignGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 9)
)
ciscoSwitchQosIfDscpAssignGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqIfDscpToQueueQueueNumber"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfDscpToQueueThresholdNumber"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfDscpAssignGroup.setStatus("current")

ciscoSwitchQosDscpRewriteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 10)
)
ciscoSwitchQosDscpRewriteGroup.setObjects(
    ("CISCO-SWITCH-QOS-MIB", "csqDscpRewriteEnable")
)
if mibBuilder.loadTexts:
    ciscoSwitchQosDscpRewriteGroup.setStatus("current")

ciscoSwitchQosRedirectPolicingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 11)
)
ciscoSwitchQosRedirectPolicingGroup.setObjects(
    ("CISCO-SWITCH-QOS-MIB", "csqPoliceRedirectedTrafficEnable")
)
if mibBuilder.loadTexts:
    ciscoSwitchQosRedirectPolicingGroup.setStatus("current")

ciscoSwitchQosPortQueueingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 12)
)
ciscoSwitchQosPortQueueingGroup.setObjects(
    ("CISCO-SWITCH-QOS-MIB", "csqPortQueueingModeEnable")
)
if mibBuilder.loadTexts:
    ciscoSwitchQosPortQueueingGroup.setStatus("current")

ciscoSwitchQosMarkingStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 13)
)
ciscoSwitchQosMarkingStatsGroup.setObjects(
    ("CISCO-SWITCH-QOS-MIB", "csqMarkingStatisticsEnable")
)
if mibBuilder.loadTexts:
    ciscoSwitchQosMarkingStatsGroup.setStatus("current")

ciscoSwitchQosIfCCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 14)
)
ciscoSwitchQosIfCCGroup.setObjects(
    ("CISCO-SWITCH-QOS-MIB", "csqIfConsistencyCheckEnable")
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfCCGroup.setStatus("current")

ciscoSwitchQosIfModeConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 15)
)
ciscoSwitchQosIfModeConfigGroup.setObjects(
    ("CISCO-SWITCH-QOS-MIB", "csqIfVlanBasedQosModeEnable")
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfModeConfigGroup.setStatus("current")

ciscoSwitchQosPolicerUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 16)
)
ciscoSwitchQosPolicerUsageGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqPolicerUsed"),
        ("CISCO-SWITCH-QOS-MIB", "csqPolicerTotal"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosPolicerUsageGroup.setStatus("current")

ciscoSwitchQosModuleStatsExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 17)
)
ciscoSwitchQosModuleStatsExtGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqModuleTunnelEncapPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleTunnelDecapPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleDropByPolicingInOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleDropByPolicingOutOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleFwdByPolicingInPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleFwdByPolicingOutPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleFwdByPolicingInOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleFwdByPolicingOutOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleHighExceedInPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleHighExceedOutPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleHighExceedInOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleHighExceedOutOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleLowExceedOutPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleLowExceedInPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleLowExceedInOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleLowExceedOutOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleDropByAggPolicerInPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleDropByAggPolicerOutPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleDropByAggPolicerInOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleDropByAggPolicerOutOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleFwdByAggPolicerInPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleFwdByAggPolicerOutPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleFwdByAggPolicerInOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleFwdByAggPolicerOutOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleAggHighExceedInPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleAggHighExceedOutPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleAggHighExceedInOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleAggHighExceedOutOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleAggLowExceedInPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleAggLowExceedOutPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleAggLowExceedInOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleAggLowExceedOutOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleDropByNetflowInPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleDropByNetflowOutPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleDropByNetflowInOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleDropByNetflowOutOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleFwdByNetflowInPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleFwdByNetflowOutPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleFwdByNetflowInOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleFwdByNetflowOutOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleNetflowExceedInPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleNetflowExceedOutPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleNetflowExceedInOctets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleNetflowExceedOutOctets"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosModuleStatsExtGroup.setStatus("current")

ciscoSwitchQosIfStatsExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 18)
)
ciscoSwitchQosIfStatsExtGroup.setObjects(
    ("CISCO-SWITCH-QOS-MIB", "csqIfBpduDropPkts")
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfStatsExtGroup.setStatus("current")

ciscoSwitchQosModuleDscpRewriteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 19)
)
ciscoSwitchQosModuleDscpRewriteGroup.setObjects(
    ("CISCO-SWITCH-QOS-MIB", "csqModuleDscpRewriteEnable")
)
if mibBuilder.loadTexts:
    ciscoSwitchQosModuleDscpRewriteGroup.setStatus("current")

ciscoSwitchQosModuleClassChangedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 20)
)
ciscoSwitchQosModuleClassChangedGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqModuleCosChangedPackets"),
        ("CISCO-SWITCH-QOS-MIB", "csqModuleTrafficClassChangedPackets"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosModuleClassChangedGroup.setStatus("current")

ciscoSwitchQosTenGOnlyModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 21)
)
ciscoSwitchQosTenGOnlyModeGroup.setObjects(
    ("CISCO-SWITCH-QOS-MIB", "csqTenGOnlyMode")
)
if mibBuilder.loadTexts:
    ciscoSwitchQosTenGOnlyModeGroup.setStatus("current")

ciscoSwitchQosIfQueueModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 22)
)
ciscoSwitchQosIfQueueModeGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqIfQueueModeCpb"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfConfigQueueMode"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfQueueModeGroup.setStatus("current")

ciscoSwitchQosIfLanQueuingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 23)
)
ciscoSwitchQosIfLanQueuingGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqIfQueueClassMapName"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfIngressPolicyMap"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfEgressPolicyMap"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfLanQueuingGroup.setStatus("current")

ciscoSwitchQosIfQueueBufferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 24)
)
ciscoSwitchQosIfQueueBufferGroup.setObjects(
    ("CISCO-SWITCH-QOS-MIB", "csqIfDropConfigQueueBuffer")
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfQueueBufferGroup.setStatus("current")

ciscoSwitchQosIfQueueSchedulingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 25)
)
ciscoSwitchQosIfQueueSchedulingGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqIfQueueScheduling"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfQueueSrrWeight"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfQueueSchedulingGroup.setStatus("current")

ciscoSwitchQosIfQueueingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 26)
)
ciscoSwitchQosIfQueueingGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqIfIngressQueueingEnable"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfEgressQueueingEnable"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfQueueingTrustState"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfQueueingGroup.setStatus("current")

ciscoSwitchQosIfQosGroupInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 27)
)
ciscoSwitchQosIfQosGroupInfoGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqIfQosGroupInfoQueueSize"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfQosGroupInfoHwMTU"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfQosGroupInfoMTU"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfQosGroupInfoDropType"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfQosGroupInfoResumeThresh"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfQosGroupInfoPauseThresh"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfQosGroupInfoScheduling"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfQosGroupInfoBandwidth"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfQosGroupInfoBandwidthUnits"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfQosGroupInfoGroup.setStatus("current")

ciscoSwitchQosIfQosGroupStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 28)
)
ciscoSwitchQosIfQosGroupStatsGroup.setObjects(
    ("CISCO-SWITCH-QOS-MIB", "csqIfQosGroupStatsValue")
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfQosGroupStatsGroup.setStatus("current")

ciscoSwitchQosIfPriGrpInBufUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 29)
)
ciscoSwitchQosIfPriGrpInBufUsageGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqIfPriGrpInBufUsageMinCount"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfPriGrpInBufUsageSharedCount"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfPriGrpInBufUsageHeadroomCount"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfPriGrpInBufUsageGlobalHeadroomCount"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfPriGrpInBufUsageSharedPeekCount"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfPriGrpInBufUsageHeadroomPeekCount"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfPriGrpInBufUsageGroup.setStatus("current")

ciscoSwitchQosServicePoolUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 30)
)
ciscoSwitchQosServicePoolUsageGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqSharedPoolUsageUsed"),
        ("CISCO-SWITCH-QOS-MIB", "csqSharedPoolUsageRemain"),
        ("CISCO-SWITCH-QOS-MIB", "csqSharedPoolUsagePeak"),
        ("CISCO-SWITCH-QOS-MIB", "csqSharedPoolUsageTotal"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosServicePoolUsageGroup.setStatus("current")

ciscoSwitchQosServicePoolCellSizeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 31)
)
ciscoSwitchQosServicePoolCellSizeGroup.setObjects(
    ("CISCO-SWITCH-QOS-MIB", "csqServicePoolCellSize")
)
if mibBuilder.loadTexts:
    ciscoSwitchQosServicePoolCellSizeGroup.setStatus("current")

ciscoSwitchQosIfQosGroupInfoShapeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 32)
)
ciscoSwitchQosIfQosGroupInfoShapeGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqIfQosGroupInfoShapeMinThresh"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfQosGroupInfoShapeMaxThresh"),
        ("CISCO-SWITCH-QOS-MIB", "csqIfQosGroupInfoShapeUnits"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosIfQosGroupInfoShapeGroup.setStatus("current")

ciscoSwitchQosHwServicePoolUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 33)
)
ciscoSwitchQosHwServicePoolUsageGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqHwSharedPoolUsageUsed"),
        ("CISCO-SWITCH-QOS-MIB", "csqHwSharedPoolUsageRemain"),
        ("CISCO-SWITCH-QOS-MIB", "csqHwSharedPoolUsageShared"),
        ("CISCO-SWITCH-QOS-MIB", "csqHwSharedPoolUsageTotal"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosHwServicePoolUsageGroup.setStatus("current")

ciscoSwitchQosServicePoolUsageTxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 2, 34)
)
ciscoSwitchQosServicePoolUsageTxGroup.setObjects(
      *(("CISCO-SWITCH-QOS-MIB", "csqSharedPoolUsageUsedTx"),
        ("CISCO-SWITCH-QOS-MIB", "csqSharedPoolUsageRemainTx"),
        ("CISCO-SWITCH-QOS-MIB", "csqSharedPoolUsagePeakTx"),
        ("CISCO-SWITCH-QOS-MIB", "csqSharedPoolUsageTotalTx"),
        ("CISCO-SWITCH-QOS-MIB", "csqSharedPoolUsageNameTx"))
)
if mibBuilder.loadTexts:
    ciscoSwitchQosServicePoolUsageTxGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSwitchQosMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosMIBCompliance.setStatus(
        "deprecated"
    )

ciscoSwitchQosMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoSwitchQosMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoSwitchQosMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoSwitchQosMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoSwitchQosMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosMIBComplianceRev6.setStatus(
        "deprecated"
    )

ciscoSwitchQosMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosMIBComplianceRev7.setStatus(
        "deprecated"
    )

ciscoSwitchQosMIBComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 580, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoSwitchQosMIBComplianceRev8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-QOS-MIB",
    **{"QosStatsType": QosStatsType,
       "ciscoSwitchQosMIB": ciscoSwitchQosMIB,
       "ciscoSwitchQosMIBNotifs": ciscoSwitchQosMIBNotifs,
       "ciscoSwitchQosMIBObjects": ciscoSwitchQosMIBObjects,
       "csqGlobals": csqGlobals,
       "csqDscpRewriteEnable": csqDscpRewriteEnable,
       "csqPoliceRedirectedTrafficEnable": csqPoliceRedirectedTrafficEnable,
       "csqPortQueueingModeEnable": csqPortQueueingModeEnable,
       "csqMarkingStatisticsEnable": csqMarkingStatisticsEnable,
       "csqTenGOnlyMode": csqTenGOnlyMode,
       "csqServicePoolCellSize": csqServicePoolCellSize,
       "csqMappings": csqMappings,
       "csqCosToDscpTable": csqCosToDscpTable,
       "csqCosToDscpEntry": csqCosToDscpEntry,
       "csqCosToDscpCos": csqCosToDscpCos,
       "csqCosToDscpDscp": csqCosToDscpDscp,
       "csqIpPrecToDscpTable": csqIpPrecToDscpTable,
       "csqIpPrecToDscpEntry": csqIpPrecToDscpEntry,
       "csqIpPrecToDscpIpPrec": csqIpPrecToDscpIpPrec,
       "csqIpPrecToDscpDscp": csqIpPrecToDscpDscp,
       "csqExpToDscpTable": csqExpToDscpTable,
       "csqExpToDscpEntry": csqExpToDscpEntry,
       "csqExpToDscpExp": csqExpToDscpExp,
       "csqExpToDscpDscp": csqExpToDscpDscp,
       "csqDscpMappingTable": csqDscpMappingTable,
       "csqDscpMappingEntry": csqDscpMappingEntry,
       "csqDscpMappingDscp": csqDscpMappingDscp,
       "csqDscpMappingCos": csqDscpMappingCos,
       "csqDscpMappingExp": csqDscpMappingExp,
       "csqDscpMappingNormalBurstDscp": csqDscpMappingNormalBurstDscp,
       "csqDscpMappingMaxBurstDscp": csqDscpMappingMaxBurstDscp,
       "csqMutations": csqMutations,
       "csqMaxCosMutationMap": csqMaxCosMutationMap,
       "csqCosMutationTable": csqCosMutationTable,
       "csqCosMutationEntry": csqCosMutationEntry,
       "csqCosMutationMapName": csqCosMutationMapName,
       "csqCosMutationRowStatus": csqCosMutationRowStatus,
       "csqCosMutationMappingTable": csqCosMutationMappingTable,
       "csqCosMutationMappingEntry": csqCosMutationMappingEntry,
       "csqCosMutationFromCos": csqCosMutationFromCos,
       "csqCosMutationToCos": csqCosMutationToCos,
       "csqMaxDscpMutationMap": csqMaxDscpMutationMap,
       "csqDscpMutationTable": csqDscpMutationTable,
       "csqDscpMutationEntry": csqDscpMutationEntry,
       "csqDscpMutationMapName": csqDscpMutationMapName,
       "csqDscpMutationRowStatus": csqDscpMutationRowStatus,
       "csqDscpMutationMappingTable": csqDscpMutationMappingTable,
       "csqDscpMutationMappingEntry": csqDscpMutationMappingEntry,
       "csqDscpMutationFromDscp": csqDscpMutationFromDscp,
       "csqDscpMutationToDscp": csqDscpMutationToDscp,
       "csqMaxExpMutationMap": csqMaxExpMutationMap,
       "csqExpMutationTable": csqExpMutationTable,
       "csqExpMutationEntry": csqExpMutationEntry,
       "csqExpMutationMapName": csqExpMutationMapName,
       "csqExpMutationRowStatus": csqExpMutationRowStatus,
       "csqExpMutationMappingTable": csqExpMutationMappingTable,
       "csqExpMutationMappingEntry": csqExpMutationMappingEntry,
       "csqExpMutationFromExp": csqExpMutationFromExp,
       "csqExpMutationToExp": csqExpMutationToExp,
       "csqIfMutationConfigTable": csqIfMutationConfigTable,
       "csqIfMutationConfigEntry": csqIfMutationConfigEntry,
       "csqIfCosMutationMap": csqIfCosMutationMap,
       "csqIfDscpMutationMap": csqIfDscpMutationMap,
       "csqIfExpMutationMap": csqIfExpMutationMap,
       "csqIfMutationRowStatus": csqIfMutationRowStatus,
       "csqInterface": csqInterface,
       "csqIfConfigTable": csqIfConfigTable,
       "csqIfConfigEntry": csqIfConfigEntry,
       "csqIfDefaultCos": csqIfDefaultCos,
       "csqIfTrustState": csqIfTrustState,
       "csqIfQueueModeCpb": csqIfQueueModeCpb,
       "csqIfConfigQueueMode": csqIfConfigQueueMode,
       "csqIfIngressPolicyMap": csqIfIngressPolicyMap,
       "csqIfEgressPolicyMap": csqIfEgressPolicyMap,
       "csqIfIngressQueueingEnable": csqIfIngressQueueingEnable,
       "csqIfEgressQueueingEnable": csqIfEgressQueueingEnable,
       "csqIfQueueingTrustState": csqIfQueueingTrustState,
       "csqIfCosToQueueTable": csqIfCosToQueueTable,
       "csqIfCosToQueueEntry": csqIfCosToQueueEntry,
       "csqIfCosToQueueDirection": csqIfCosToQueueDirection,
       "csqIfCosToQueueCos": csqIfCosToQueueCos,
       "csqIfCosToQueueQueueNumber": csqIfCosToQueueQueueNumber,
       "csqIfCosToQueueThresholdNumber": csqIfCosToQueueThresholdNumber,
       "csqIfDscpToQueueTable": csqIfDscpToQueueTable,
       "csqIfDscpToQueueEntry": csqIfDscpToQueueEntry,
       "csqIfDscpToQueueDirection": csqIfDscpToQueueDirection,
       "csqIfDscpToQueueDscp": csqIfDscpToQueueDscp,
       "csqIfDscpToQueueQueueNumber": csqIfDscpToQueueQueueNumber,
       "csqIfDscpToQueueThresholdNumber": csqIfDscpToQueueThresholdNumber,
       "csqIfDropConfigTable": csqIfDropConfigTable,
       "csqIfDropConfigEntry": csqIfDropConfigEntry,
       "csqIfDropConfigDirection": csqIfDropConfigDirection,
       "csqIfDropConfigQueueIndex": csqIfDropConfigQueueIndex,
       "csqIfDropConfigThresholdIndex": csqIfDropConfigThresholdIndex,
       "csqIfDropConfigDropAlgorithm": csqIfDropConfigDropAlgorithm,
       "csqIfDropConfigDropThreshold": csqIfDropConfigDropThreshold,
       "csqIfDropConfigMinWredThreshold": csqIfDropConfigMinWredThreshold,
       "csqIfDropConfigMaxWredThreshold": csqIfDropConfigMaxWredThreshold,
       "csqIfDropConfigQueueBuffer": csqIfDropConfigQueueBuffer,
       "csqIfQueueTable": csqIfQueueTable,
       "csqIfQueueEntry": csqIfQueueEntry,
       "csqIfQueueDirection": csqIfQueueDirection,
       "csqIfQueueNumber": csqIfQueueNumber,
       "csqIfQueueWrrWeight": csqIfQueueWrrWeight,
       "csqIfQueueSizeWeight": csqIfQueueSizeWeight,
       "csqIfQueueStatsGranularity": csqIfQueueStatsGranularity,
       "csqIfQueueClassMapName": csqIfQueueClassMapName,
       "csqIfQueueScheduling": csqIfQueueScheduling,
       "csqIfQueueSrrWeight": csqIfQueueSrrWeight,
       "csqIfModeConfigTable": csqIfModeConfigTable,
       "csqIfModeConfigEntry": csqIfModeConfigEntry,
       "csqIfVlanBasedQosModeEnable": csqIfVlanBasedQosModeEnable,
       "csqIfConsistencyCheckTable": csqIfConsistencyCheckTable,
       "csqIfConsistencyCheckEntry": csqIfConsistencyCheckEntry,
       "csqIfConsistencyCheckEnable": csqIfConsistencyCheckEnable,
       "csqIfQosGroupInfoTable": csqIfQosGroupInfoTable,
       "csqIfQosGroupInfoEntry": csqIfQosGroupInfoEntry,
       "csqIfQosGroupInfoDirection": csqIfQosGroupInfoDirection,
       "csqIfQosGroupInfoGroupNumber": csqIfQosGroupInfoGroupNumber,
       "csqIfQosGroupInfoQueueSize": csqIfQosGroupInfoQueueSize,
       "csqIfQosGroupInfoHwMTU": csqIfQosGroupInfoHwMTU,
       "csqIfQosGroupInfoMTU": csqIfQosGroupInfoMTU,
       "csqIfQosGroupInfoDropType": csqIfQosGroupInfoDropType,
       "csqIfQosGroupInfoResumeThresh": csqIfQosGroupInfoResumeThresh,
       "csqIfQosGroupInfoPauseThresh": csqIfQosGroupInfoPauseThresh,
       "csqIfQosGroupInfoScheduling": csqIfQosGroupInfoScheduling,
       "csqIfQosGroupInfoBandwidth": csqIfQosGroupInfoBandwidth,
       "csqIfQosGroupInfoBandwidthUnits": csqIfQosGroupInfoBandwidthUnits,
       "csqIfQosGroupInfoShapeMinThresh": csqIfQosGroupInfoShapeMinThresh,
       "csqIfQosGroupInfoShapeMaxThresh": csqIfQosGroupInfoShapeMaxThresh,
       "csqIfQosGroupInfoShapeUnits": csqIfQosGroupInfoShapeUnits,
       "csqStatistics": csqStatistics,
       "csqIfStatsTable": csqIfStatsTable,
       "csqIfStatsEntry": csqIfStatsEntry,
       "csqIfStatsDirection": csqIfStatsDirection,
       "csqIfStatsQueueNumber": csqIfStatsQueueNumber,
       "csqIfStatsThresholdNumber": csqIfStatsThresholdNumber,
       "csqIfStatsDropPkts": csqIfStatsDropPkts,
       "csqModuleStatsTable": csqModuleStatsTable,
       "csqModuleStatsEntry": csqModuleStatsEntry,
       "csqModuleDropByPolicingPackets": csqModuleDropByPolicingPackets,
       "csqModuleTosChangedIpPackets": csqModuleTosChangedIpPackets,
       "csqModuleCosChangedIpPackets": csqModuleCosChangedIpPackets,
       "csqModuleCosChangedNonIpPackets": csqModuleCosChangedNonIpPackets,
       "csqModuleExpChangedMplsPackets": csqModuleExpChangedMplsPackets,
       "csqModuleStatsExtTable": csqModuleStatsExtTable,
       "csqModuleStatsExtEntry": csqModuleStatsExtEntry,
       "csqModuleTunnelEncapPackets": csqModuleTunnelEncapPackets,
       "csqModuleTunnelDecapPackets": csqModuleTunnelDecapPackets,
       "csqModuleDropByPolicingInOctets": csqModuleDropByPolicingInOctets,
       "csqModuleDropByPolicingOutOctets": csqModuleDropByPolicingOutOctets,
       "csqModuleFwdByPolicingInPackets": csqModuleFwdByPolicingInPackets,
       "csqModuleFwdByPolicingInOctets": csqModuleFwdByPolicingInOctets,
       "csqModuleFwdByPolicingOutPackets": csqModuleFwdByPolicingOutPackets,
       "csqModuleFwdByPolicingOutOctets": csqModuleFwdByPolicingOutOctets,
       "csqModuleHighExceedInPackets": csqModuleHighExceedInPackets,
       "csqModuleHighExceedInOctets": csqModuleHighExceedInOctets,
       "csqModuleHighExceedOutPackets": csqModuleHighExceedOutPackets,
       "csqModuleHighExceedOutOctets": csqModuleHighExceedOutOctets,
       "csqModuleLowExceedInPackets": csqModuleLowExceedInPackets,
       "csqModuleLowExceedInOctets": csqModuleLowExceedInOctets,
       "csqModuleLowExceedOutPackets": csqModuleLowExceedOutPackets,
       "csqModuleLowExceedOutOctets": csqModuleLowExceedOutOctets,
       "csqModuleDropByAggPolicerInPackets": csqModuleDropByAggPolicerInPackets,
       "csqModuleDropByAggPolicerInOctets": csqModuleDropByAggPolicerInOctets,
       "csqModuleDropByAggPolicerOutPackets": csqModuleDropByAggPolicerOutPackets,
       "csqModuleDropByAggPolicerOutOctets": csqModuleDropByAggPolicerOutOctets,
       "csqModuleFwdByAggPolicerInPackets": csqModuleFwdByAggPolicerInPackets,
       "csqModuleFwdByAggPolicerInOctets": csqModuleFwdByAggPolicerInOctets,
       "csqModuleFwdByAggPolicerOutPackets": csqModuleFwdByAggPolicerOutPackets,
       "csqModuleFwdByAggPolicerOutOctets": csqModuleFwdByAggPolicerOutOctets,
       "csqModuleAggHighExceedInPackets": csqModuleAggHighExceedInPackets,
       "csqModuleAggHighExceedInOctets": csqModuleAggHighExceedInOctets,
       "csqModuleAggHighExceedOutPackets": csqModuleAggHighExceedOutPackets,
       "csqModuleAggHighExceedOutOctets": csqModuleAggHighExceedOutOctets,
       "csqModuleAggLowExceedInPackets": csqModuleAggLowExceedInPackets,
       "csqModuleAggLowExceedInOctets": csqModuleAggLowExceedInOctets,
       "csqModuleAggLowExceedOutPackets": csqModuleAggLowExceedOutPackets,
       "csqModuleAggLowExceedOutOctets": csqModuleAggLowExceedOutOctets,
       "csqModuleDropByNetflowInPackets": csqModuleDropByNetflowInPackets,
       "csqModuleDropByNetflowInOctets": csqModuleDropByNetflowInOctets,
       "csqModuleDropByNetflowOutPackets": csqModuleDropByNetflowOutPackets,
       "csqModuleDropByNetflowOutOctets": csqModuleDropByNetflowOutOctets,
       "csqModuleFwdByNetflowInPackets": csqModuleFwdByNetflowInPackets,
       "csqModuleFwdByNetflowInOctets": csqModuleFwdByNetflowInOctets,
       "csqModuleFwdByNetflowOutPackets": csqModuleFwdByNetflowOutPackets,
       "csqModuleFwdByNetflowOutOctets": csqModuleFwdByNetflowOutOctets,
       "csqModuleNetflowExceedInPackets": csqModuleNetflowExceedInPackets,
       "csqModuleNetflowExceedInOctets": csqModuleNetflowExceedInOctets,
       "csqModuleNetflowExceedOutPackets": csqModuleNetflowExceedOutPackets,
       "csqModuleNetflowExceedOutOctets": csqModuleNetflowExceedOutOctets,
       "csqModuleCosChangedPackets": csqModuleCosChangedPackets,
       "csqModuleTrafficClassChangedPackets": csqModuleTrafficClassChangedPackets,
       "csqIfStatsExtTable": csqIfStatsExtTable,
       "csqIfStatsExtEntry": csqIfStatsExtEntry,
       "csqIfBpduDropPkts": csqIfBpduDropPkts,
       "csqIfQosGroupStatsTable": csqIfQosGroupStatsTable,
       "csqIfQosGroupStatsEntry": csqIfQosGroupStatsEntry,
       "csqIfQosGroupStatsDirection": csqIfQosGroupStatsDirection,
       "csqIfQosGroupStatsGroupNumber": csqIfQosGroupStatsGroupNumber,
       "csqIfQosGroupStatsType": csqIfQosGroupStatsType,
       "csqIfQosGroupStatsValue": csqIfQosGroupStatsValue,
       "csqIfPriGrpInBufUsageTable": csqIfPriGrpInBufUsageTable,
       "csqIfPriGrpInBufUsageEntry": csqIfPriGrpInBufUsageEntry,
       "csqIfPriGrpInBufUsageGrpNo": csqIfPriGrpInBufUsageGrpNo,
       "csqIfPriGrpInBufUsageMinCount": csqIfPriGrpInBufUsageMinCount,
       "csqIfPriGrpInBufUsageSharedCount": csqIfPriGrpInBufUsageSharedCount,
       "csqIfPriGrpInBufUsageHeadroomCount": csqIfPriGrpInBufUsageHeadroomCount,
       "csqIfPriGrpInBufUsageGlobalHeadroomCount": csqIfPriGrpInBufUsageGlobalHeadroomCount,
       "csqIfPriGrpInBufUsageSharedPeekCount": csqIfPriGrpInBufUsageSharedPeekCount,
       "csqIfPriGrpInBufUsageHeadroomPeekCount": csqIfPriGrpInBufUsageHeadroomPeekCount,
       "csqSharedPoolUsageTable": csqSharedPoolUsageTable,
       "csqSharedPoolUsageEntry": csqSharedPoolUsageEntry,
       "csqSharedPoolUsageInstNo": csqSharedPoolUsageInstNo,
       "csqSharedPoolUsagePoolNo": csqSharedPoolUsagePoolNo,
       "csqSharedPoolUsageUsed": csqSharedPoolUsageUsed,
       "csqSharedPoolUsageRemain": csqSharedPoolUsageRemain,
       "csqSharedPoolUsagePeak": csqSharedPoolUsagePeak,
       "csqSharedPoolUsageTotal": csqSharedPoolUsageTotal,
       "csqSharedPoolUsageUsedTx": csqSharedPoolUsageUsedTx,
       "csqSharedPoolUsageRemainTx": csqSharedPoolUsageRemainTx,
       "csqSharedPoolUsagePeakTx": csqSharedPoolUsagePeakTx,
       "csqSharedPoolUsageTotalTx": csqSharedPoolUsageTotalTx,
       "csqSharedPoolUsageNameTx": csqSharedPoolUsageNameTx,
       "csqHwSharedPoolUsageTable": csqHwSharedPoolUsageTable,
       "csqHwSharedPoolUsageEntry": csqHwSharedPoolUsageEntry,
       "csqHwSharedPoolDeviceId": csqHwSharedPoolDeviceId,
       "csqHwSharedPoolUsageInstNo": csqHwSharedPoolUsageInstNo,
       "csqHwSharedPoolStatsDirection": csqHwSharedPoolStatsDirection,
       "csqHwSharedPoolStatsType": csqHwSharedPoolStatsType,
       "csqHwSharedPoolUsageUsed": csqHwSharedPoolUsageUsed,
       "csqHwSharedPoolUsageRemain": csqHwSharedPoolUsageRemain,
       "csqHwSharedPoolUsageShared": csqHwSharedPoolUsageShared,
       "csqHwSharedPoolUsageTotal": csqHwSharedPoolUsageTotal,
       "csqPolicerUsage": csqPolicerUsage,
       "csqPolicerUsageTable": csqPolicerUsageTable,
       "csqPolicerUsageEntry": csqPolicerUsageEntry,
       "csqPolicerType": csqPolicerType,
       "csqPolicerUsed": csqPolicerUsed,
       "csqPolicerTotal": csqPolicerTotal,
       "csqModule": csqModule,
       "csqModuleDscpRewriteEnableTable": csqModuleDscpRewriteEnableTable,
       "csqModuleDscpRewriteEnableEntry": csqModuleDscpRewriteEnableEntry,
       "csqModuleDscpRewriteEnable": csqModuleDscpRewriteEnable,
       "ciscoSwitchQosMIBConformance": ciscoSwitchQosMIBConformance,
       "ciscoSwitchQosMIBCompliances": ciscoSwitchQosMIBCompliances,
       "ciscoSwitchQosMIBCompliance": ciscoSwitchQosMIBCompliance,
       "ciscoSwitchQosMIBComplianceRev2": ciscoSwitchQosMIBComplianceRev2,
       "ciscoSwitchQosMIBComplianceRev3": ciscoSwitchQosMIBComplianceRev3,
       "ciscoSwitchQosMIBComplianceRev4": ciscoSwitchQosMIBComplianceRev4,
       "ciscoSwitchQosMIBComplianceRev5": ciscoSwitchQosMIBComplianceRev5,
       "ciscoSwitchQosMIBComplianceRev6": ciscoSwitchQosMIBComplianceRev6,
       "ciscoSwitchQosMIBComplianceRev7": ciscoSwitchQosMIBComplianceRev7,
       "ciscoSwitchQosMIBComplianceRev8": ciscoSwitchQosMIBComplianceRev8,
       "ciscoSwitchQosMIBGroups": ciscoSwitchQosMIBGroups,
       "ciscoSwitchQosMappingGroup": ciscoSwitchQosMappingGroup,
       "ciscoSwitchQosMutationGroup": ciscoSwitchQosMutationGroup,
       "ciscoSwitchQosIfConfigGroup": ciscoSwitchQosIfConfigGroup,
       "ciscoSwitchQosIfCosToQueueGroup": ciscoSwitchQosIfCosToQueueGroup,
       "ciscoSwitchQosIfDropConfigGroup": ciscoSwitchQosIfDropConfigGroup,
       "ciscoSwitchQosIfQueueGroup": ciscoSwitchQosIfQueueGroup,
       "ciscoSwitchQosIfStatsGroup": ciscoSwitchQosIfStatsGroup,
       "ciscoSwitchQosModuleStatsGroup": ciscoSwitchQosModuleStatsGroup,
       "ciscoSwitchQosIfDscpAssignGroup": ciscoSwitchQosIfDscpAssignGroup,
       "ciscoSwitchQosDscpRewriteGroup": ciscoSwitchQosDscpRewriteGroup,
       "ciscoSwitchQosRedirectPolicingGroup": ciscoSwitchQosRedirectPolicingGroup,
       "ciscoSwitchQosPortQueueingGroup": ciscoSwitchQosPortQueueingGroup,
       "ciscoSwitchQosMarkingStatsGroup": ciscoSwitchQosMarkingStatsGroup,
       "ciscoSwitchQosIfCCGroup": ciscoSwitchQosIfCCGroup,
       "ciscoSwitchQosIfModeConfigGroup": ciscoSwitchQosIfModeConfigGroup,
       "ciscoSwitchQosPolicerUsageGroup": ciscoSwitchQosPolicerUsageGroup,
       "ciscoSwitchQosModuleStatsExtGroup": ciscoSwitchQosModuleStatsExtGroup,
       "ciscoSwitchQosIfStatsExtGroup": ciscoSwitchQosIfStatsExtGroup,
       "ciscoSwitchQosModuleDscpRewriteGroup": ciscoSwitchQosModuleDscpRewriteGroup,
       "ciscoSwitchQosModuleClassChangedGroup": ciscoSwitchQosModuleClassChangedGroup,
       "ciscoSwitchQosTenGOnlyModeGroup": ciscoSwitchQosTenGOnlyModeGroup,
       "ciscoSwitchQosIfQueueModeGroup": ciscoSwitchQosIfQueueModeGroup,
       "ciscoSwitchQosIfLanQueuingGroup": ciscoSwitchQosIfLanQueuingGroup,
       "ciscoSwitchQosIfQueueBufferGroup": ciscoSwitchQosIfQueueBufferGroup,
       "ciscoSwitchQosIfQueueSchedulingGroup": ciscoSwitchQosIfQueueSchedulingGroup,
       "ciscoSwitchQosIfQueueingGroup": ciscoSwitchQosIfQueueingGroup,
       "ciscoSwitchQosIfQosGroupInfoGroup": ciscoSwitchQosIfQosGroupInfoGroup,
       "ciscoSwitchQosIfQosGroupStatsGroup": ciscoSwitchQosIfQosGroupStatsGroup,
       "ciscoSwitchQosIfPriGrpInBufUsageGroup": ciscoSwitchQosIfPriGrpInBufUsageGroup,
       "ciscoSwitchQosServicePoolUsageGroup": ciscoSwitchQosServicePoolUsageGroup,
       "ciscoSwitchQosServicePoolCellSizeGroup": ciscoSwitchQosServicePoolCellSizeGroup,
       "ciscoSwitchQosIfQosGroupInfoShapeGroup": ciscoSwitchQosIfQosGroupInfoShapeGroup,
       "ciscoSwitchQosHwServicePoolUsageGroup": ciscoSwitchQosHwServicePoolUsageGroup,
       "ciscoSwitchQosServicePoolUsageTxGroup": ciscoSwitchQosServicePoolUsageTxGroup}
)
