# SNMP MIB module (CADANT-MAP-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-MAP-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:06 2024
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

(cadSpectrum,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadSpectrum")

(FlowActivityState,) = mibBuilder.importSymbols(
    "CADANT-TC",
    "FlowActivityState")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

cadMapStatsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10)
)
cadMapStatsMib.setRevisions(
        ("2008-10-23 00:00",
         "2004-01-17 00:00",
         "2004-01-16 00:00",
         "2003-08-11 00:00",
         "2003-08-06 00:00",
         "2003-08-04 00:00",
         "2003-04-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CadMapStatsIUCTypeId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )



class CadMapStatsBwRequestQueuesPriorityId(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("docsispri0", 0),
          ("docsispri1", 1),
          ("docsispri2", 2),
          ("docsispri3", 3),
          ("docsispri4", 4),
          ("docsispri5", 5),
          ("docsispri6", 6),
          ("docsispri7", 7))
    )



# MIB Managed Objects in the order of their OIDs

_CadMapStatsBaseTable_Object = MibTable
cadMapStatsBaseTable = _CadMapStatsBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 1)
)
if mibBuilder.loadTexts:
    cadMapStatsBaseTable.setStatus("current")
_CadMapStatsBaseEntry_Object = MibTableRow
cadMapStatsBaseEntry = _CadMapStatsBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 1, 1)
)
cadMapStatsBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cadMapStatsBaseEntry.setStatus("current")
_CadMapStatsTotalMapsSent_Type = Counter64
_CadMapStatsTotalMapsSent_Object = MibTableColumn
cadMapStatsTotalMapsSent = _CadMapStatsTotalMapsSent_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 1, 1, 1),
    _CadMapStatsTotalMapsSent_Type()
)
cadMapStatsTotalMapsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalMapsSent.setStatus("current")
_CadMapStatsTotalFragmentedGrants_Type = Counter64
_CadMapStatsTotalFragmentedGrants_Object = MibTableColumn
cadMapStatsTotalFragmentedGrants = _CadMapStatsTotalFragmentedGrants_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 1, 1, 2),
    _CadMapStatsTotalFragmentedGrants_Type()
)
cadMapStatsTotalFragmentedGrants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalFragmentedGrants.setStatus("current")
_CadMapStatsTotalUgsQiTransitions_Type = Counter64
_CadMapStatsTotalUgsQiTransitions_Object = MibTableColumn
cadMapStatsTotalUgsQiTransitions = _CadMapStatsTotalUgsQiTransitions_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 1, 1, 3),
    _CadMapStatsTotalUgsQiTransitions_Type()
)
cadMapStatsTotalUgsQiTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalUgsQiTransitions.setStatus("current")
_CadMapStatsTotalUgsadTransitions_Type = Counter64
_CadMapStatsTotalUgsadTransitions_Object = MibTableColumn
cadMapStatsTotalUgsadTransitions = _CadMapStatsTotalUgsadTransitions_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 1, 1, 4),
    _CadMapStatsTotalUgsadTransitions_Type()
)
cadMapStatsTotalUgsadTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalUgsadTransitions.setStatus("current")
_CadMapStatsTotalUgsEHdrsSw_Type = Counter64
_CadMapStatsTotalUgsEHdrsSw_Object = MibTableColumn
cadMapStatsTotalUgsEHdrsSw = _CadMapStatsTotalUgsEHdrsSw_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 1, 1, 5),
    _CadMapStatsTotalUgsEHdrsSw_Type()
)
cadMapStatsTotalUgsEHdrsSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalUgsEHdrsSw.setStatus("current")
_CadMapStatsTotalBadMaps_Type = Counter64
_CadMapStatsTotalBadMaps_Object = MibTableColumn
cadMapStatsTotalBadMaps = _CadMapStatsTotalBadMaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 1, 1, 6),
    _CadMapStatsTotalBadMaps_Type()
)
cadMapStatsTotalBadMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalBadMaps.setStatus("current")
_CadMapStatsMSlotsTable_Object = MibTable
cadMapStatsMSlotsTable = _CadMapStatsMSlotsTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 2)
)
if mibBuilder.loadTexts:
    cadMapStatsMSlotsTable.setStatus("current")
_CadMapStatsMSlotsEntry_Object = MibTableRow
cadMapStatsMSlotsEntry = _CadMapStatsMSlotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 2, 1)
)
cadMapStatsMSlotsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cadMapStatsMSlotsEntry.setStatus("current")
_CadMapStatsTotalMSlots_Type = Counter64
_CadMapStatsTotalMSlots_Object = MibTableColumn
cadMapStatsTotalMSlots = _CadMapStatsTotalMSlots_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 2, 1, 1),
    _CadMapStatsTotalMSlots_Type()
)
cadMapStatsTotalMSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalMSlots.setStatus("current")
_CadMapStatsTotalUCastGrantedMSlots_Type = Counter64
_CadMapStatsTotalUCastGrantedMSlots_Object = MibTableColumn
cadMapStatsTotalUCastGrantedMSlots = _CadMapStatsTotalUCastGrantedMSlots_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 2, 1, 2),
    _CadMapStatsTotalUCastGrantedMSlots_Type()
)
cadMapStatsTotalUCastGrantedMSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalUCastGrantedMSlots.setStatus("current")
_CadMapStatsTotalBwRequestMSlots_Type = Counter64
_CadMapStatsTotalBwRequestMSlots_Object = MibTableColumn
cadMapStatsTotalBwRequestMSlots = _CadMapStatsTotalBwRequestMSlots_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 2, 1, 3),
    _CadMapStatsTotalBwRequestMSlots_Type()
)
cadMapStatsTotalBwRequestMSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalBwRequestMSlots.setStatus("current")
_CadMapStatsTotalSkippedMSlots_Type = Counter64
_CadMapStatsTotalSkippedMSlots_Object = MibTableColumn
cadMapStatsTotalSkippedMSlots = _CadMapStatsTotalSkippedMSlots_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 2, 1, 4),
    _CadMapStatsTotalSkippedMSlots_Type()
)
cadMapStatsTotalSkippedMSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalSkippedMSlots.setStatus("current")
_CadMapStatsTotalLogicalNullPadMSlots_Type = Counter64
_CadMapStatsTotalLogicalNullPadMSlots_Object = MibTableColumn
cadMapStatsTotalLogicalNullPadMSlots = _CadMapStatsTotalLogicalNullPadMSlots_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 2, 1, 5),
    _CadMapStatsTotalLogicalNullPadMSlots_Type()
)
cadMapStatsTotalLogicalNullPadMSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalLogicalNullPadMSlots.setStatus("current")
_CadMapStatsMSlotsPerIUCTable_Object = MibTable
cadMapStatsMSlotsPerIUCTable = _CadMapStatsMSlotsPerIUCTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 3)
)
if mibBuilder.loadTexts:
    cadMapStatsMSlotsPerIUCTable.setStatus("current")
_CadMapStatsMSlotsPerIUCEntry_Object = MibTableRow
cadMapStatsMSlotsPerIUCEntry = _CadMapStatsMSlotsPerIUCEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 3, 1)
)
cadMapStatsMSlotsPerIUCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CADANT-MAP-STATS-MIB", "cadMapStatsMSlotsPerIUCId"),
)
if mibBuilder.loadTexts:
    cadMapStatsMSlotsPerIUCEntry.setStatus("current")
_CadMapStatsMSlotsPerIUCId_Type = CadMapStatsIUCTypeId
_CadMapStatsMSlotsPerIUCId_Object = MibTableColumn
cadMapStatsMSlotsPerIUCId = _CadMapStatsMSlotsPerIUCId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 3, 1, 1),
    _CadMapStatsMSlotsPerIUCId_Type()
)
cadMapStatsMSlotsPerIUCId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMapStatsMSlotsPerIUCId.setStatus("current")
_CadMapStatsGrantedBCastMSlots_Type = Counter64
_CadMapStatsGrantedBCastMSlots_Object = MibTableColumn
cadMapStatsGrantedBCastMSlots = _CadMapStatsGrantedBCastMSlots_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 3, 1, 2),
    _CadMapStatsGrantedBCastMSlots_Type()
)
cadMapStatsGrantedBCastMSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsGrantedBCastMSlots.setStatus("current")
_CadMapStatsGrantedMCastMSlots_Type = Counter64
_CadMapStatsGrantedMCastMSlots_Object = MibTableColumn
cadMapStatsGrantedMCastMSlots = _CadMapStatsGrantedMCastMSlots_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 3, 1, 3),
    _CadMapStatsGrantedMCastMSlots_Type()
)
cadMapStatsGrantedMCastMSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsGrantedMCastMSlots.setStatus("current")
_CadMapStatsGrantedUCastMSlots_Type = Counter64
_CadMapStatsGrantedUCastMSlots_Object = MibTableColumn
cadMapStatsGrantedUCastMSlots = _CadMapStatsGrantedUCastMSlots_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 3, 1, 4),
    _CadMapStatsGrantedUCastMSlots_Type()
)
cadMapStatsGrantedUCastMSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsGrantedUCastMSlots.setStatus("current")
_CadMapStatsGrantedZeroSidMSlots_Type = Counter64
_CadMapStatsGrantedZeroSidMSlots_Object = MibTableColumn
cadMapStatsGrantedZeroSidMSlots = _CadMapStatsGrantedZeroSidMSlots_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 3, 1, 5),
    _CadMapStatsGrantedZeroSidMSlots_Type()
)
cadMapStatsGrantedZeroSidMSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsGrantedZeroSidMSlots.setStatus("current")
_CadMapStatsBwRequestsTable_Object = MibTable
cadMapStatsBwRequestsTable = _CadMapStatsBwRequestsTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 4)
)
if mibBuilder.loadTexts:
    cadMapStatsBwRequestsTable.setStatus("current")
_CadMapStatsBwRequestsEntry_Object = MibTableRow
cadMapStatsBwRequestsEntry = _CadMapStatsBwRequestsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 4, 1)
)
cadMapStatsBwRequestsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cadMapStatsBwRequestsEntry.setStatus("current")
_CadMapStatsTotalBwRequests_Type = Counter64
_CadMapStatsTotalBwRequests_Object = MibTableColumn
cadMapStatsTotalBwRequests = _CadMapStatsTotalBwRequests_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 4, 1, 1),
    _CadMapStatsTotalBwRequests_Type()
)
cadMapStatsTotalBwRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalBwRequests.setStatus("current")
_CadMapStatsTotalBwRequestSchedulerDrops_Type = Counter64
_CadMapStatsTotalBwRequestSchedulerDrops_Object = MibTableColumn
cadMapStatsTotalBwRequestSchedulerDrops = _CadMapStatsTotalBwRequestSchedulerDrops_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 4, 1, 2),
    _CadMapStatsTotalBwRequestSchedulerDrops_Type()
)
cadMapStatsTotalBwRequestSchedulerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalBwRequestSchedulerDrops.setStatus("current")
_CadMapStatsTotalBwRequestSuperGreedyDrops_Type = Counter64
_CadMapStatsTotalBwRequestSuperGreedyDrops_Object = MibTableColumn
cadMapStatsTotalBwRequestSuperGreedyDrops = _CadMapStatsTotalBwRequestSuperGreedyDrops_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 4, 1, 3),
    _CadMapStatsTotalBwRequestSuperGreedyDrops_Type()
)
cadMapStatsTotalBwRequestSuperGreedyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalBwRequestSuperGreedyDrops.setStatus("current")
_CadMapStatsPeakBwRequestSize_Type = Unsigned32
_CadMapStatsPeakBwRequestSize_Object = MibTableColumn
cadMapStatsPeakBwRequestSize = _CadMapStatsPeakBwRequestSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 4, 1, 4),
    _CadMapStatsPeakBwRequestSize_Type()
)
cadMapStatsPeakBwRequestSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsPeakBwRequestSize.setStatus("current")
_CadMapStatsPeakBwRequestsPerMap_Type = Unsigned32
_CadMapStatsPeakBwRequestsPerMap_Object = MibTableColumn
cadMapStatsPeakBwRequestsPerMap = _CadMapStatsPeakBwRequestsPerMap_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 4, 1, 5),
    _CadMapStatsPeakBwRequestsPerMap_Type()
)
cadMapStatsPeakBwRequestsPerMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsPeakBwRequestsPerMap.setStatus("current")
_CadMapStatsGrantPendingsTable_Object = MibTable
cadMapStatsGrantPendingsTable = _CadMapStatsGrantPendingsTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 5)
)
if mibBuilder.loadTexts:
    cadMapStatsGrantPendingsTable.setStatus("current")
_CadMapStatsGrantPendingsEntry_Object = MibTableRow
cadMapStatsGrantPendingsEntry = _CadMapStatsGrantPendingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 5, 1)
)
cadMapStatsGrantPendingsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cadMapStatsGrantPendingsEntry.setStatus("current")
_CadMapStatsTotalGrantPendings_Type = Counter64
_CadMapStatsTotalGrantPendings_Object = MibTableColumn
cadMapStatsTotalGrantPendings = _CadMapStatsTotalGrantPendings_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 5, 1, 1),
    _CadMapStatsTotalGrantPendings_Type()
)
cadMapStatsTotalGrantPendings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalGrantPendings.setStatus("current")
_CadMapStatsTotalGrantPendingDrops_Type = Counter64
_CadMapStatsTotalGrantPendingDrops_Object = MibTableColumn
cadMapStatsTotalGrantPendingDrops = _CadMapStatsTotalGrantPendingDrops_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 5, 1, 2),
    _CadMapStatsTotalGrantPendingDrops_Type()
)
cadMapStatsTotalGrantPendingDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalGrantPendingDrops.setStatus("current")
_CadMapStatsTotalGrantPendingPromos_Type = Counter64
_CadMapStatsTotalGrantPendingPromos_Object = MibTableColumn
cadMapStatsTotalGrantPendingPromos = _CadMapStatsTotalGrantPendingPromos_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 5, 1, 3),
    _CadMapStatsTotalGrantPendingPromos_Type()
)
cadMapStatsTotalGrantPendingPromos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsTotalGrantPendingPromos.setStatus("current")
_CadMapStatsPeakGrantPendingsPerMap_Type = Unsigned32
_CadMapStatsPeakGrantPendingsPerMap_Object = MibTableColumn
cadMapStatsPeakGrantPendingsPerMap = _CadMapStatsPeakGrantPendingsPerMap_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 5, 1, 4),
    _CadMapStatsPeakGrantPendingsPerMap_Type()
)
cadMapStatsPeakGrantPendingsPerMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsPeakGrantPendingsPerMap.setStatus("current")
_CadMapStatsBwRequestQueuesTable_Object = MibTable
cadMapStatsBwRequestQueuesTable = _CadMapStatsBwRequestQueuesTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 6)
)
if mibBuilder.loadTexts:
    cadMapStatsBwRequestQueuesTable.setStatus("current")
_CadMapStatsBwRequestQueuesEntry_Object = MibTableRow
cadMapStatsBwRequestQueuesEntry = _CadMapStatsBwRequestQueuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 6, 1)
)
cadMapStatsBwRequestQueuesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CADANT-MAP-STATS-MIB", "cadMapStatsBwRequestQueuesFlowState"),
    (0, "CADANT-MAP-STATS-MIB", "cadMapStatsBwRequestQueuesPriorityId"),
)
if mibBuilder.loadTexts:
    cadMapStatsBwRequestQueuesEntry.setStatus("current")
_CadMapStatsBwRequestQueuesFlowState_Type = FlowActivityState
_CadMapStatsBwRequestQueuesFlowState_Object = MibTableColumn
cadMapStatsBwRequestQueuesFlowState = _CadMapStatsBwRequestQueuesFlowState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 6, 1, 1),
    _CadMapStatsBwRequestQueuesFlowState_Type()
)
cadMapStatsBwRequestQueuesFlowState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMapStatsBwRequestQueuesFlowState.setStatus("current")
_CadMapStatsBwRequestQueuesPriorityId_Type = CadMapStatsBwRequestQueuesPriorityId
_CadMapStatsBwRequestQueuesPriorityId_Object = MibTableColumn
cadMapStatsBwRequestQueuesPriorityId = _CadMapStatsBwRequestQueuesPriorityId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 6, 1, 2),
    _CadMapStatsBwRequestQueuesPriorityId_Type()
)
cadMapStatsBwRequestQueuesPriorityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMapStatsBwRequestQueuesPriorityId.setStatus("current")
_CadMapStatsBwRequestQueuesNumAdds_Type = Counter64
_CadMapStatsBwRequestQueuesNumAdds_Object = MibTableColumn
cadMapStatsBwRequestQueuesNumAdds = _CadMapStatsBwRequestQueuesNumAdds_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 6, 1, 3),
    _CadMapStatsBwRequestQueuesNumAdds_Type()
)
cadMapStatsBwRequestQueuesNumAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsBwRequestQueuesNumAdds.setStatus("current")
_CadMapStatsBwRequestQueuesNumDrops_Type = Counter64
_CadMapStatsBwRequestQueuesNumDrops_Object = MibTableColumn
cadMapStatsBwRequestQueuesNumDrops = _CadMapStatsBwRequestQueuesNumDrops_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 6, 1, 4),
    _CadMapStatsBwRequestQueuesNumDrops_Type()
)
cadMapStatsBwRequestQueuesNumDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsBwRequestQueuesNumDrops.setStatus("current")
_CadMapStatsBwRequestQueuesNumPendings_Type = Counter64
_CadMapStatsBwRequestQueuesNumPendings_Object = MibTableColumn
cadMapStatsBwRequestQueuesNumPendings = _CadMapStatsBwRequestQueuesNumPendings_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 6, 1, 5),
    _CadMapStatsBwRequestQueuesNumPendings_Type()
)
cadMapStatsBwRequestQueuesNumPendings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsBwRequestQueuesNumPendings.setStatus("current")
_CadMapStatsBwRequestQueuesNumPromos_Type = Counter64
_CadMapStatsBwRequestQueuesNumPromos_Object = MibTableColumn
cadMapStatsBwRequestQueuesNumPromos = _CadMapStatsBwRequestQueuesNumPromos_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 6, 1, 6),
    _CadMapStatsBwRequestQueuesNumPromos_Type()
)
cadMapStatsBwRequestQueuesNumPromos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsBwRequestQueuesNumPromos.setStatus("current")
_CadMapStatsBwRequestQueuesNumElements_Type = Unsigned32
_CadMapStatsBwRequestQueuesNumElements_Object = MibTableColumn
cadMapStatsBwRequestQueuesNumElements = _CadMapStatsBwRequestQueuesNumElements_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 6, 1, 7),
    _CadMapStatsBwRequestQueuesNumElements_Type()
)
cadMapStatsBwRequestQueuesNumElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsBwRequestQueuesNumElements.setStatus("current")
_CadMapStatsBwRequestQueuesLatencySum_Type = Counter64
_CadMapStatsBwRequestQueuesLatencySum_Object = MibTableColumn
cadMapStatsBwRequestQueuesLatencySum = _CadMapStatsBwRequestQueuesLatencySum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 6, 1, 8),
    _CadMapStatsBwRequestQueuesLatencySum_Type()
)
cadMapStatsBwRequestQueuesLatencySum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsBwRequestQueuesLatencySum.setStatus("current")
_CadMapStatsPeriodicFlowsTable_Object = MibTable
cadMapStatsPeriodicFlowsTable = _CadMapStatsPeriodicFlowsTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 7)
)
if mibBuilder.loadTexts:
    cadMapStatsPeriodicFlowsTable.setStatus("current")
_CadMapStatsPeriodicFlowsEntry_Object = MibTableRow
cadMapStatsPeriodicFlowsEntry = _CadMapStatsPeriodicFlowsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 7, 1)
)
cadMapStatsPeriodicFlowsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cadMapStatsPeriodicFlowsEntry.setStatus("current")
_CadMapStatsNumNrtpsFlows_Type = Unsigned32
_CadMapStatsNumNrtpsFlows_Object = MibTableColumn
cadMapStatsNumNrtpsFlows = _CadMapStatsNumNrtpsFlows_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 7, 1, 1),
    _CadMapStatsNumNrtpsFlows_Type()
)
cadMapStatsNumNrtpsFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsNumNrtpsFlows.setStatus("current")
_CadMapStatsNumRtpsFlows_Type = Unsigned32
_CadMapStatsNumRtpsFlows_Object = MibTableColumn
cadMapStatsNumRtpsFlows = _CadMapStatsNumRtpsFlows_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 7, 1, 2),
    _CadMapStatsNumRtpsFlows_Type()
)
cadMapStatsNumRtpsFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsNumRtpsFlows.setStatus("current")
_CadMapStatsNumUgsadActiveFlows_Type = Unsigned32
_CadMapStatsNumUgsadActiveFlows_Object = MibTableColumn
cadMapStatsNumUgsadActiveFlows = _CadMapStatsNumUgsadActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 7, 1, 3),
    _CadMapStatsNumUgsadActiveFlows_Type()
)
cadMapStatsNumUgsadActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsNumUgsadActiveFlows.setStatus("current")
_CadMapStatsNumUgsadPollingFlows_Type = Unsigned32
_CadMapStatsNumUgsadPollingFlows_Object = MibTableColumn
cadMapStatsNumUgsadPollingFlows = _CadMapStatsNumUgsadPollingFlows_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 7, 1, 4),
    _CadMapStatsNumUgsadPollingFlows_Type()
)
cadMapStatsNumUgsadPollingFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsNumUgsadPollingFlows.setStatus("current")
_CadMapStatsNumUgsFlows_Type = Unsigned32
_CadMapStatsNumUgsFlows_Object = MibTableColumn
cadMapStatsNumUgsFlows = _CadMapStatsNumUgsFlows_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 7, 1, 5),
    _CadMapStatsNumUgsFlows_Type()
)
cadMapStatsNumUgsFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsNumUgsFlows.setStatus("current")
_CadMapStatsNumBEPollingFlows_Type = Unsigned32
_CadMapStatsNumBEPollingFlows_Object = MibTableColumn
cadMapStatsNumBEPollingFlows = _CadMapStatsNumBEPollingFlows_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 7, 1, 6),
    _CadMapStatsNumBEPollingFlows_Type()
)
cadMapStatsNumBEPollingFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsNumBEPollingFlows.setStatus("current")


class _CadMapStatsNumBEFastPollingFlows_Type(Unsigned32):
    """Custom type cadMapStatsNumBEFastPollingFlows based on Unsigned32"""
    defaultValue = 0


_CadMapStatsNumBEFastPollingFlows_Object = MibTableColumn
cadMapStatsNumBEFastPollingFlows = _CadMapStatsNumBEFastPollingFlows_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 10, 7, 1, 7),
    _CadMapStatsNumBEFastPollingFlows_Type()
)
cadMapStatsNumBEFastPollingFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMapStatsNumBEFastPollingFlows.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-MAP-STATS-MIB",
    **{"CadMapStatsIUCTypeId": CadMapStatsIUCTypeId,
       "CadMapStatsBwRequestQueuesPriorityId": CadMapStatsBwRequestQueuesPriorityId,
       "cadMapStatsMib": cadMapStatsMib,
       "cadMapStatsBaseTable": cadMapStatsBaseTable,
       "cadMapStatsBaseEntry": cadMapStatsBaseEntry,
       "cadMapStatsTotalMapsSent": cadMapStatsTotalMapsSent,
       "cadMapStatsTotalFragmentedGrants": cadMapStatsTotalFragmentedGrants,
       "cadMapStatsTotalUgsQiTransitions": cadMapStatsTotalUgsQiTransitions,
       "cadMapStatsTotalUgsadTransitions": cadMapStatsTotalUgsadTransitions,
       "cadMapStatsTotalUgsEHdrsSw": cadMapStatsTotalUgsEHdrsSw,
       "cadMapStatsTotalBadMaps": cadMapStatsTotalBadMaps,
       "cadMapStatsMSlotsTable": cadMapStatsMSlotsTable,
       "cadMapStatsMSlotsEntry": cadMapStatsMSlotsEntry,
       "cadMapStatsTotalMSlots": cadMapStatsTotalMSlots,
       "cadMapStatsTotalUCastGrantedMSlots": cadMapStatsTotalUCastGrantedMSlots,
       "cadMapStatsTotalBwRequestMSlots": cadMapStatsTotalBwRequestMSlots,
       "cadMapStatsTotalSkippedMSlots": cadMapStatsTotalSkippedMSlots,
       "cadMapStatsTotalLogicalNullPadMSlots": cadMapStatsTotalLogicalNullPadMSlots,
       "cadMapStatsMSlotsPerIUCTable": cadMapStatsMSlotsPerIUCTable,
       "cadMapStatsMSlotsPerIUCEntry": cadMapStatsMSlotsPerIUCEntry,
       "cadMapStatsMSlotsPerIUCId": cadMapStatsMSlotsPerIUCId,
       "cadMapStatsGrantedBCastMSlots": cadMapStatsGrantedBCastMSlots,
       "cadMapStatsGrantedMCastMSlots": cadMapStatsGrantedMCastMSlots,
       "cadMapStatsGrantedUCastMSlots": cadMapStatsGrantedUCastMSlots,
       "cadMapStatsGrantedZeroSidMSlots": cadMapStatsGrantedZeroSidMSlots,
       "cadMapStatsBwRequestsTable": cadMapStatsBwRequestsTable,
       "cadMapStatsBwRequestsEntry": cadMapStatsBwRequestsEntry,
       "cadMapStatsTotalBwRequests": cadMapStatsTotalBwRequests,
       "cadMapStatsTotalBwRequestSchedulerDrops": cadMapStatsTotalBwRequestSchedulerDrops,
       "cadMapStatsTotalBwRequestSuperGreedyDrops": cadMapStatsTotalBwRequestSuperGreedyDrops,
       "cadMapStatsPeakBwRequestSize": cadMapStatsPeakBwRequestSize,
       "cadMapStatsPeakBwRequestsPerMap": cadMapStatsPeakBwRequestsPerMap,
       "cadMapStatsGrantPendingsTable": cadMapStatsGrantPendingsTable,
       "cadMapStatsGrantPendingsEntry": cadMapStatsGrantPendingsEntry,
       "cadMapStatsTotalGrantPendings": cadMapStatsTotalGrantPendings,
       "cadMapStatsTotalGrantPendingDrops": cadMapStatsTotalGrantPendingDrops,
       "cadMapStatsTotalGrantPendingPromos": cadMapStatsTotalGrantPendingPromos,
       "cadMapStatsPeakGrantPendingsPerMap": cadMapStatsPeakGrantPendingsPerMap,
       "cadMapStatsBwRequestQueuesTable": cadMapStatsBwRequestQueuesTable,
       "cadMapStatsBwRequestQueuesEntry": cadMapStatsBwRequestQueuesEntry,
       "cadMapStatsBwRequestQueuesFlowState": cadMapStatsBwRequestQueuesFlowState,
       "cadMapStatsBwRequestQueuesPriorityId": cadMapStatsBwRequestQueuesPriorityId,
       "cadMapStatsBwRequestQueuesNumAdds": cadMapStatsBwRequestQueuesNumAdds,
       "cadMapStatsBwRequestQueuesNumDrops": cadMapStatsBwRequestQueuesNumDrops,
       "cadMapStatsBwRequestQueuesNumPendings": cadMapStatsBwRequestQueuesNumPendings,
       "cadMapStatsBwRequestQueuesNumPromos": cadMapStatsBwRequestQueuesNumPromos,
       "cadMapStatsBwRequestQueuesNumElements": cadMapStatsBwRequestQueuesNumElements,
       "cadMapStatsBwRequestQueuesLatencySum": cadMapStatsBwRequestQueuesLatencySum,
       "cadMapStatsPeriodicFlowsTable": cadMapStatsPeriodicFlowsTable,
       "cadMapStatsPeriodicFlowsEntry": cadMapStatsPeriodicFlowsEntry,
       "cadMapStatsNumNrtpsFlows": cadMapStatsNumNrtpsFlows,
       "cadMapStatsNumRtpsFlows": cadMapStatsNumRtpsFlows,
       "cadMapStatsNumUgsadActiveFlows": cadMapStatsNumUgsadActiveFlows,
       "cadMapStatsNumUgsadPollingFlows": cadMapStatsNumUgsadPollingFlows,
       "cadMapStatsNumUgsFlows": cadMapStatsNumUgsFlows,
       "cadMapStatsNumBEPollingFlows": cadMapStatsNumBEPollingFlows,
       "cadMapStatsNumBEFastPollingFlows": cadMapStatsNumBEFastPollingFlows}
)
