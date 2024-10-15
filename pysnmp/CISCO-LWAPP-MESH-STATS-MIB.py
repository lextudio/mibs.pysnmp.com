# SNMP MIB module (CISCO-LWAPP-MESH-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-MESH-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:43 2024
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

(cLApName,
 cLApSysMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApName",
    "cLApSysMacAddress")

(clMeshNeighborMacAddress,
 clMeshNodeBackhaul) = mibBuilder.importSymbols(
    "CISCO-LWAPP-MESH-MIB",
    "clMeshNeighborMacAddress",
    "clMeshNodeBackhaul")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappMeshStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 617)
)
ciscoLwappMeshStatsMIB.setRevisions(
        ("2010-09-01 00:00",
         "2007-03-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappMeshStatsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappMeshStatsMIBNotifs = _CiscoLwappMeshStatsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 0)
)
_CiscoLwappMeshStatsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMeshStatsMIBObjects = _CiscoLwappMeshStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1)
)
_CiscoLwappMeshNodeStats_ObjectIdentity = ObjectIdentity
ciscoLwappMeshNodeStats = _CiscoLwappMeshNodeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1)
)
_ClMeshNodeStatsTable_Object = MibTable
clMeshNodeStatsTable = _ClMeshNodeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1)
)
if mibBuilder.loadTexts:
    clMeshNodeStatsTable.setStatus("current")
_ClMeshNodeStatsEntry_Object = MibTableRow
clMeshNodeStatsEntry = _ClMeshNodeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1)
)
clMeshNodeStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    clMeshNodeStatsEntry.setStatus("current")
_ClMeshNodeMalformedNeighPkts_Type = Counter32
_ClMeshNodeMalformedNeighPkts_Object = MibTableColumn
clMeshNodeMalformedNeighPkts = _ClMeshNodeMalformedNeighPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 1),
    _ClMeshNodeMalformedNeighPkts_Type()
)
clMeshNodeMalformedNeighPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeMalformedNeighPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeMalformedNeighPkts.setUnits("packets")
_ClMeshNodePoorNeighSnrPkts_Type = Counter32
_ClMeshNodePoorNeighSnrPkts_Object = MibTableColumn
clMeshNodePoorNeighSnrPkts = _ClMeshNodePoorNeighSnrPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 2),
    _ClMeshNodePoorNeighSnrPkts_Type()
)
clMeshNodePoorNeighSnrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodePoorNeighSnrPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodePoorNeighSnrPkts.setUnits("packets")
_ClMeshNodeExcludedPkts_Type = Counter32
_ClMeshNodeExcludedPkts_Object = MibTableColumn
clMeshNodeExcludedPkts = _ClMeshNodeExcludedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 3),
    _ClMeshNodeExcludedPkts_Type()
)
clMeshNodeExcludedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeExcludedPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeExcludedPkts.setUnits("packets")
_ClMeshNodeRxNeighReq_Type = Counter32
_ClMeshNodeRxNeighReq_Object = MibTableColumn
clMeshNodeRxNeighReq = _ClMeshNodeRxNeighReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 4),
    _ClMeshNodeRxNeighReq_Type()
)
clMeshNodeRxNeighReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeRxNeighReq.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeRxNeighReq.setUnits("packets")
_ClMeshNodeRxNeighRsp_Type = Counter32
_ClMeshNodeRxNeighRsp_Object = MibTableColumn
clMeshNodeRxNeighRsp = _ClMeshNodeRxNeighRsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 5),
    _ClMeshNodeRxNeighRsp_Type()
)
clMeshNodeRxNeighRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeRxNeighRsp.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeRxNeighRsp.setUnits("packets")
_ClMeshNodeTxNeighReq_Type = Counter32
_ClMeshNodeTxNeighReq_Object = MibTableColumn
clMeshNodeTxNeighReq = _ClMeshNodeTxNeighReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 6),
    _ClMeshNodeTxNeighReq_Type()
)
clMeshNodeTxNeighReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeTxNeighReq.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeTxNeighReq.setUnits("packets")
_ClMeshNodeTxNeighRsp_Type = Counter32
_ClMeshNodeTxNeighRsp_Object = MibTableColumn
clMeshNodeTxNeighRsp = _ClMeshNodeTxNeighRsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 7),
    _ClMeshNodeTxNeighRsp_Type()
)
clMeshNodeTxNeighRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeTxNeighRsp.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeTxNeighRsp.setUnits("packets")
_ClMeshNodeParentChanges_Type = Counter32
_ClMeshNodeParentChanges_Object = MibTableColumn
clMeshNodeParentChanges = _ClMeshNodeParentChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 8),
    _ClMeshNodeParentChanges_Type()
)
clMeshNodeParentChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeParentChanges.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeParentChanges.setUnits("parent-switches")
_ClMeshNodeSecBackhaulCount_Type = Counter32
_ClMeshNodeSecBackhaulCount_Object = MibTableColumn
clMeshNodeSecBackhaulCount = _ClMeshNodeSecBackhaulCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 9),
    _ClMeshNodeSecBackhaulCount_Type()
)
clMeshNodeSecBackhaulCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeSecBackhaulCount.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeSecBackhaulCount.setUnits("packets")
_ClMeshNodeAssociationCount_Type = Counter32
_ClMeshNodeAssociationCount_Object = MibTableColumn
clMeshNodeAssociationCount = _ClMeshNodeAssociationCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 10),
    _ClMeshNodeAssociationCount_Type()
)
clMeshNodeAssociationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeAssociationCount.setStatus("current")
_ClMeshNodePktQueueStatsTable_Object = MibTable
clMeshNodePktQueueStatsTable = _ClMeshNodePktQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2)
)
if mibBuilder.loadTexts:
    clMeshNodePktQueueStatsTable.setStatus("current")
_ClMeshNodePktQueueStatsEntry_Object = MibTableRow
clMeshNodePktQueueStatsEntry = _ClMeshNodePktQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2, 1)
)
clMeshNodePktQueueStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueueIndex"),
)
if mibBuilder.loadTexts:
    clMeshNodePktQueueStatsEntry.setStatus("current")


class _ClMeshNodePktQueueIndex_Type(Integer32):
    """Custom type clMeshNodePktQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bronze", 4),
          ("gold", 2),
          ("management", 5),
          ("platinum", 3),
          ("silver", 1))
    )


_ClMeshNodePktQueueIndex_Type.__name__ = "Integer32"
_ClMeshNodePktQueueIndex_Object = MibTableColumn
clMeshNodePktQueueIndex = _ClMeshNodePktQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2, 1, 1),
    _ClMeshNodePktQueueIndex_Type()
)
clMeshNodePktQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clMeshNodePktQueueIndex.setStatus("current")
_ClMeshNodePktQueueAvg_Type = Gauge32
_ClMeshNodePktQueueAvg_Object = MibTableColumn
clMeshNodePktQueueAvg = _ClMeshNodePktQueueAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2, 1, 2),
    _ClMeshNodePktQueueAvg_Type()
)
clMeshNodePktQueueAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodePktQueueAvg.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodePktQueueAvg.setUnits("packets")
_ClMeshNodePktQueuePeak_Type = Gauge32
_ClMeshNodePktQueuePeak_Object = MibTableColumn
clMeshNodePktQueuePeak = _ClMeshNodePktQueuePeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2, 1, 3),
    _ClMeshNodePktQueuePeak_Type()
)
clMeshNodePktQueuePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodePktQueuePeak.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodePktQueuePeak.setUnits("packets")
_ClMeshNodePktQueuePktsDropped_Type = Counter32
_ClMeshNodePktQueuePktsDropped_Object = MibTableColumn
clMeshNodePktQueuePktsDropped = _ClMeshNodePktQueuePktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2, 1, 4),
    _ClMeshNodePktQueuePktsDropped_Type()
)
clMeshNodePktQueuePktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodePktQueuePktsDropped.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodePktQueuePktsDropped.setUnits("packets")
_ClMeshNodePktQueueTimeStamp_Type = TimeStamp
_ClMeshNodePktQueueTimeStamp_Object = MibTableColumn
clMeshNodePktQueueTimeStamp = _ClMeshNodePktQueueTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2, 1, 5),
    _ClMeshNodePktQueueTimeStamp_Type()
)
clMeshNodePktQueueTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodePktQueueTimeStamp.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodePktQueueTimeStamp.setUnits("seconds")
_ClMeshNodePktQueueSize_Type = Unsigned32
_ClMeshNodePktQueueSize_Object = MibTableColumn
clMeshNodePktQueueSize = _ClMeshNodePktQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2, 1, 6),
    _ClMeshNodePktQueueSize_Type()
)
clMeshNodePktQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodePktQueueSize.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodePktQueueSize.setUnits("packets")
_ClMeshNodeSecStatsTable_Object = MibTable
clMeshNodeSecStatsTable = _ClMeshNodeSecStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3)
)
if mibBuilder.loadTexts:
    clMeshNodeSecStatsTable.setStatus("current")
_ClMeshNodeSecStatsEntry_Object = MibTableRow
clMeshNodeSecStatsEntry = _ClMeshNodeSecStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1)
)
clMeshNodeSecStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    clMeshNodeSecStatsEntry.setStatus("current")
_ClMeshNodeSecTxPkts_Type = Counter32
_ClMeshNodeSecTxPkts_Object = MibTableColumn
clMeshNodeSecTxPkts = _ClMeshNodeSecTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 1),
    _ClMeshNodeSecTxPkts_Type()
)
clMeshNodeSecTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeSecTxPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeSecTxPkts.setUnits("packets")
_ClMeshNodeSecRxPkts_Type = Counter32
_ClMeshNodeSecRxPkts_Object = MibTableColumn
clMeshNodeSecRxPkts = _ClMeshNodeSecRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 2),
    _ClMeshNodeSecRxPkts_Type()
)
clMeshNodeSecRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeSecRxPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeSecRxPkts.setUnits("packets")
_ClMeshNodeAssocReqFailures_Type = Counter32
_ClMeshNodeAssocReqFailures_Object = MibTableColumn
clMeshNodeAssocReqFailures = _ClMeshNodeAssocReqFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 3),
    _ClMeshNodeAssocReqFailures_Type()
)
clMeshNodeAssocReqFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeAssocReqFailures.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeAssocReqFailures.setUnits("packets")
_ClMeshNodeAssocReqTimeouts_Type = Counter32
_ClMeshNodeAssocReqTimeouts_Object = MibTableColumn
clMeshNodeAssocReqTimeouts = _ClMeshNodeAssocReqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 4),
    _ClMeshNodeAssocReqTimeouts_Type()
)
clMeshNodeAssocReqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeAssocReqTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeAssocReqTimeouts.setUnits("packets")
_ClMeshNodeAssocReqSuccess_Type = Counter32
_ClMeshNodeAssocReqSuccess_Object = MibTableColumn
clMeshNodeAssocReqSuccess = _ClMeshNodeAssocReqSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 5),
    _ClMeshNodeAssocReqSuccess_Type()
)
clMeshNodeAssocReqSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeAssocReqSuccess.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeAssocReqSuccess.setUnits("packets")
_ClMeshNodeAuthReqFailures_Type = Counter32
_ClMeshNodeAuthReqFailures_Object = MibTableColumn
clMeshNodeAuthReqFailures = _ClMeshNodeAuthReqFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 6),
    _ClMeshNodeAuthReqFailures_Type()
)
clMeshNodeAuthReqFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeAuthReqFailures.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeAuthReqFailures.setUnits("packets")
_ClMeshNodeAuthReqTimeouts_Type = Counter32
_ClMeshNodeAuthReqTimeouts_Object = MibTableColumn
clMeshNodeAuthReqTimeouts = _ClMeshNodeAuthReqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 7),
    _ClMeshNodeAuthReqTimeouts_Type()
)
clMeshNodeAuthReqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeAuthReqTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeAuthReqTimeouts.setUnits("packets")
_ClMeshNodeAuthReqSuccess_Type = Counter32
_ClMeshNodeAuthReqSuccess_Object = MibTableColumn
clMeshNodeAuthReqSuccess = _ClMeshNodeAuthReqSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 8),
    _ClMeshNodeAuthReqSuccess_Type()
)
clMeshNodeAuthReqSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeAuthReqSuccess.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeAuthReqSuccess.setUnits("packets")
_ClMeshNodeReassocReqFailures_Type = Counter32
_ClMeshNodeReassocReqFailures_Object = MibTableColumn
clMeshNodeReassocReqFailures = _ClMeshNodeReassocReqFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 9),
    _ClMeshNodeReassocReqFailures_Type()
)
clMeshNodeReassocReqFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeReassocReqFailures.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeReassocReqFailures.setUnits("packets")
_ClMeshNodeReassocReqTimeouts_Type = Counter32
_ClMeshNodeReassocReqTimeouts_Object = MibTableColumn
clMeshNodeReassocReqTimeouts = _ClMeshNodeReassocReqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 10),
    _ClMeshNodeReassocReqTimeouts_Type()
)
clMeshNodeReassocReqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeReassocReqTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeReassocReqTimeouts.setUnits("packets")
_ClMeshNodeReassocReqSuccess_Type = Counter32
_ClMeshNodeReassocReqSuccess_Object = MibTableColumn
clMeshNodeReassocReqSuccess = _ClMeshNodeReassocReqSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 11),
    _ClMeshNodeReassocReqSuccess_Type()
)
clMeshNodeReassocReqSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeReassocReqSuccess.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeReassocReqSuccess.setUnits("packets")
_ClMeshNodeReauthReqFailures_Type = Counter32
_ClMeshNodeReauthReqFailures_Object = MibTableColumn
clMeshNodeReauthReqFailures = _ClMeshNodeReauthReqFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 12),
    _ClMeshNodeReauthReqFailures_Type()
)
clMeshNodeReauthReqFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeReauthReqFailures.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeReauthReqFailures.setUnits("packets")
_ClMeshNodeReauthReqTimeouts_Type = Counter32
_ClMeshNodeReauthReqTimeouts_Object = MibTableColumn
clMeshNodeReauthReqTimeouts = _ClMeshNodeReauthReqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 13),
    _ClMeshNodeReauthReqTimeouts_Type()
)
clMeshNodeReauthReqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeReauthReqTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeReauthReqTimeouts.setUnits("packets")
_ClMeshNodeReauthReqSuccess_Type = Counter32
_ClMeshNodeReauthReqSuccess_Object = MibTableColumn
clMeshNodeReauthReqSuccess = _ClMeshNodeReauthReqSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 14),
    _ClMeshNodeReauthReqSuccess_Type()
)
clMeshNodeReauthReqSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeReauthReqSuccess.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeReauthReqSuccess.setUnits("packets")
_ClMeshNodeUnknownAssocReq_Type = Counter32
_ClMeshNodeUnknownAssocReq_Object = MibTableColumn
clMeshNodeUnknownAssocReq = _ClMeshNodeUnknownAssocReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 15),
    _ClMeshNodeUnknownAssocReq_Type()
)
clMeshNodeUnknownAssocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeUnknownAssocReq.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeUnknownAssocReq.setUnits("packets")
_ClMeshNodeInvalidAssocReq_Type = Counter32
_ClMeshNodeInvalidAssocReq_Object = MibTableColumn
clMeshNodeInvalidAssocReq = _ClMeshNodeInvalidAssocReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 16),
    _ClMeshNodeInvalidAssocReq_Type()
)
clMeshNodeInvalidAssocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeInvalidAssocReq.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeInvalidAssocReq.setUnits("packets")
_ClMeshNodeUnknownReauthReq_Type = Counter32
_ClMeshNodeUnknownReauthReq_Object = MibTableColumn
clMeshNodeUnknownReauthReq = _ClMeshNodeUnknownReauthReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 17),
    _ClMeshNodeUnknownReauthReq_Type()
)
clMeshNodeUnknownReauthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeUnknownReauthReq.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeUnknownReauthReq.setUnits("packets")
_ClMeshNodeInvalidReauthReq_Type = Counter32
_ClMeshNodeInvalidReauthReq_Object = MibTableColumn
clMeshNodeInvalidReauthReq = _ClMeshNodeInvalidReauthReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 18),
    _ClMeshNodeInvalidReauthReq_Type()
)
clMeshNodeInvalidReauthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeInvalidReauthReq.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeInvalidReauthReq.setUnits("packets")
_ClMeshNodeUnknownReassocReq_Type = Counter32
_ClMeshNodeUnknownReassocReq_Object = MibTableColumn
clMeshNodeUnknownReassocReq = _ClMeshNodeUnknownReassocReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 19),
    _ClMeshNodeUnknownReassocReq_Type()
)
clMeshNodeUnknownReassocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeUnknownReassocReq.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeUnknownReassocReq.setUnits("packets")
_ClMeshNodeInvalidReassocReq_Type = Counter32
_ClMeshNodeInvalidReassocReq_Object = MibTableColumn
clMeshNodeInvalidReassocReq = _ClMeshNodeInvalidReassocReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 20),
    _ClMeshNodeInvalidReassocReq_Type()
)
clMeshNodeInvalidReassocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeInvalidReassocReq.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeInvalidReassocReq.setUnits("packets")
_CiscoLwappMeshNeighStats_ObjectIdentity = ObjectIdentity
ciscoLwappMeshNeighStats = _CiscoLwappMeshNeighStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2)
)
_ClMeshNeighStatsTable_Object = MibTable
clMeshNeighStatsTable = _ClMeshNeighStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1)
)
if mibBuilder.loadTexts:
    clMeshNeighStatsTable.setStatus("current")
_ClMeshNeighStatsEntry_Object = MibTableRow
clMeshNeighStatsEntry = _ClMeshNeighStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1, 1)
)
clMeshNeighStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-MESH-MIB", "clMeshNeighborMacAddress"),
)
if mibBuilder.loadTexts:
    clMeshNeighStatsEntry.setStatus("current")
_ClMeshNeighAsParentTxPkts_Type = Counter32
_ClMeshNeighAsParentTxPkts_Object = MibTableColumn
clMeshNeighAsParentTxPkts = _ClMeshNeighAsParentTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1, 1, 1),
    _ClMeshNeighAsParentTxPkts_Type()
)
clMeshNeighAsParentTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNeighAsParentTxPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNeighAsParentTxPkts.setUnits("packets")
_ClMeshNeighAsParentRxPkts_Type = Counter32
_ClMeshNeighAsParentRxPkts_Object = MibTableColumn
clMeshNeighAsParentRxPkts = _ClMeshNeighAsParentRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1, 1, 2),
    _ClMeshNeighAsParentRxPkts_Type()
)
clMeshNeighAsParentRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNeighAsParentRxPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNeighAsParentRxPkts.setUnits("packets")
_ClMeshNeighTotalTxPkts_Type = Counter32
_ClMeshNeighTotalTxPkts_Object = MibTableColumn
clMeshNeighTotalTxPkts = _ClMeshNeighTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1, 1, 3),
    _ClMeshNeighTotalTxPkts_Type()
)
clMeshNeighTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNeighTotalTxPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNeighTotalTxPkts.setUnits("packets")
_ClMeshNeighSuccessTxPkts_Type = Counter32
_ClMeshNeighSuccessTxPkts_Object = MibTableColumn
clMeshNeighSuccessTxPkts = _ClMeshNeighSuccessTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1, 1, 4),
    _ClMeshNeighSuccessTxPkts_Type()
)
clMeshNeighSuccessTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNeighSuccessTxPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNeighSuccessTxPkts.setUnits("packets")
_ClMeshNeighRetriesTxPkts_Type = Counter32
_ClMeshNeighRetriesTxPkts_Object = MibTableColumn
clMeshNeighRetriesTxPkts = _ClMeshNeighRetriesTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1, 1, 5),
    _ClMeshNeighRetriesTxPkts_Type()
)
clMeshNeighRetriesTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNeighRetriesTxPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNeighRetriesTxPkts.setUnits("packets")
_ClMeshNeighPoorSnrRxPkts_Type = Counter32
_ClMeshNeighPoorSnrRxPkts_Object = MibTableColumn
clMeshNeighPoorSnrRxPkts = _ClMeshNeighPoorSnrRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1, 1, 6),
    _ClMeshNeighPoorSnrRxPkts_Type()
)
clMeshNeighPoorSnrRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNeighPoorSnrRxPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNeighPoorSnrRxPkts.setUnits("packets")
_CiscoLwappMeshStatsMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMeshStatsMIBNotifObjects = _CiscoLwappMeshStatsMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 3)
)


class _ClMeshInitiatingApName_Type(SnmpAdminString):
    """Custom type clMeshInitiatingApName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClMeshInitiatingApName_Type.__name__ = "SnmpAdminString"
_ClMeshInitiatingApName_Object = MibScalar
clMeshInitiatingApName = _ClMeshInitiatingApName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 3, 1),
    _ClMeshInitiatingApName_Type()
)
clMeshInitiatingApName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clMeshInitiatingApName.setStatus("current")
_CiscoLwappMeshAccessClass_ObjectIdentity = ObjectIdentity
ciscoLwappMeshAccessClass = _CiscoLwappMeshAccessClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4)
)
_ClMeshAccessClassTable_Object = MibTable
clMeshAccessClassTable = _ClMeshAccessClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4, 1)
)
if mibBuilder.loadTexts:
    clMeshAccessClassTable.setStatus("current")
_ClMeshAccessClassEntry_Object = MibTableRow
clMeshAccessClassEntry = _ClMeshAccessClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4, 1, 1)
)
clMeshAccessClassEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-MESH-MIB", "clMeshNeighborMacAddress"),
)
if mibBuilder.loadTexts:
    clMeshAccessClassEntry.setStatus("current")
_ClMeshAccessClassTotalTxPkts_Type = Counter32
_ClMeshAccessClassTotalTxPkts_Object = MibTableColumn
clMeshAccessClassTotalTxPkts = _ClMeshAccessClassTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4, 1, 1, 1),
    _ClMeshAccessClassTotalTxPkts_Type()
)
clMeshAccessClassTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshAccessClassTotalTxPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshAccessClassTotalTxPkts.setUnits("packets")
_ClMeshAccessClassSuccTxPkts_Type = Counter32
_ClMeshAccessClassSuccTxPkts_Object = MibTableColumn
clMeshAccessClassSuccTxPkts = _ClMeshAccessClassSuccTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4, 1, 1, 2),
    _ClMeshAccessClassSuccTxPkts_Type()
)
clMeshAccessClassSuccTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshAccessClassSuccTxPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshAccessClassSuccTxPkts.setUnits("packets")
_ClMeshAccessClassRetryPkts_Type = Counter32
_ClMeshAccessClassRetryPkts_Object = MibTableColumn
clMeshAccessClassRetryPkts = _ClMeshAccessClassRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4, 1, 1, 3),
    _ClMeshAccessClassRetryPkts_Type()
)
clMeshAccessClassRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshAccessClassRetryPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshAccessClassRetryPkts.setUnits("packets")
_ClMeshAccessClassRTSAttempts_Type = Counter32
_ClMeshAccessClassRTSAttempts_Object = MibTableColumn
clMeshAccessClassRTSAttempts = _ClMeshAccessClassRTSAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4, 1, 1, 4),
    _ClMeshAccessClassRTSAttempts_Type()
)
clMeshAccessClassRTSAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshAccessClassRTSAttempts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshAccessClassRTSAttempts.setUnits("packets")
_ClMeshAccessClassRTSSuccess_Type = Counter32
_ClMeshAccessClassRTSSuccess_Object = MibTableColumn
clMeshAccessClassRTSSuccess = _ClMeshAccessClassRTSSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4, 1, 1, 5),
    _ClMeshAccessClassRTSSuccess_Type()
)
clMeshAccessClassRTSSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshAccessClassRTSSuccess.setStatus("current")
if mibBuilder.loadTexts:
    clMeshAccessClassRTSSuccess.setUnits("packets")
_CiscoLwappMeshDataRateStats_ObjectIdentity = ObjectIdentity
ciscoLwappMeshDataRateStats = _CiscoLwappMeshDataRateStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 5)
)
_ClMeshDataRateStatsTable_Object = MibTable
clMeshDataRateStatsTable = _ClMeshDataRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 5, 1)
)
if mibBuilder.loadTexts:
    clMeshDataRateStatsTable.setStatus("current")
_ClMeshDataRateStatsEntry_Object = MibTableRow
clMeshDataRateStatsEntry = _ClMeshDataRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 5, 1, 1)
)
clMeshDataRateStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-MESH-MIB", "clMeshNeighborMacAddress"),
    (0, "CISCO-LWAPP-MESH-STATS-MIB", "cLMeshDataRateIndex"),
)
if mibBuilder.loadTexts:
    clMeshDataRateStatsEntry.setStatus("current")
_CLMeshDataRateIndex_Type = Unsigned32
_CLMeshDataRateIndex_Object = MibTableColumn
cLMeshDataRateIndex = _CLMeshDataRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 5, 1, 1, 1),
    _CLMeshDataRateIndex_Type()
)
cLMeshDataRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMeshDataRateIndex.setStatus("current")
if mibBuilder.loadTexts:
    cLMeshDataRateIndex.setUnits("Mbps")
_ClMeshDataRateSuccTxPkts_Type = Counter32
_ClMeshDataRateSuccTxPkts_Object = MibTableColumn
clMeshDataRateSuccTxPkts = _ClMeshDataRateSuccTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 5, 1, 1, 2),
    _ClMeshDataRateSuccTxPkts_Type()
)
clMeshDataRateSuccTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshDataRateSuccTxPkts.setStatus("current")
if mibBuilder.loadTexts:
    clMeshDataRateSuccTxPkts.setUnits("packets")
_ClMeshDataRateTxAttempts_Type = Counter32
_ClMeshDataRateTxAttempts_Object = MibTableColumn
clMeshDataRateTxAttempts = _ClMeshDataRateTxAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 5, 1, 1, 3),
    _ClMeshDataRateTxAttempts_Type()
)
clMeshDataRateTxAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshDataRateTxAttempts.setStatus("current")
_CiscoLwappMeshStatsMIBConfigObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMeshStatsMIBConfigObjects = _CiscoLwappMeshStatsMIBConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 2)
)


class _ClMeshNodeQueueOverflowNotifEnabled_Type(TruthValue):
    """Custom type clMeshNodeQueueOverflowNotifEnabled based on TruthValue"""


_ClMeshNodeQueueOverflowNotifEnabled_Object = MibScalar
clMeshNodeQueueOverflowNotifEnabled = _ClMeshNodeQueueOverflowNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 2, 1),
    _ClMeshNodeQueueOverflowNotifEnabled_Type()
)
clMeshNodeQueueOverflowNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeQueueOverflowNotifEnabled.setStatus("current")


class _ClMeshNodeStatsTimeInterval_Type(TimeInterval):
    """Custom type clMeshNodeStatsTimeInterval based on TimeInterval"""
    defaultValue = 18000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18000, 90000),
    )


_ClMeshNodeStatsTimeInterval_Type.__name__ = "TimeInterval"
_ClMeshNodeStatsTimeInterval_Object = MibScalar
clMeshNodeStatsTimeInterval = _ClMeshNodeStatsTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 2, 2),
    _ClMeshNodeStatsTimeInterval_Type()
)
clMeshNodeStatsTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeStatsTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeStatsTimeInterval.setUnits("hundredths-seconds")


class _ClMeshNodeSecBackhaulChangeNotifEnabled_Type(TruthValue):
    """Custom type clMeshNodeSecBackhaulChangeNotifEnabled based on TruthValue"""


_ClMeshNodeSecBackhaulChangeNotifEnabled_Object = MibScalar
clMeshNodeSecBackhaulChangeNotifEnabled = _ClMeshNodeSecBackhaulChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 2, 3),
    _ClMeshNodeSecBackhaulChangeNotifEnabled_Type()
)
clMeshNodeSecBackhaulChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeSecBackhaulChangeNotifEnabled.setStatus("current")


class _ClMeshNodeExcessiveAssociationNotifEnabled_Type(TruthValue):
    """Custom type clMeshNodeExcessiveAssociationNotifEnabled based on TruthValue"""


_ClMeshNodeExcessiveAssociationNotifEnabled_Object = MibScalar
clMeshNodeExcessiveAssociationNotifEnabled = _ClMeshNodeExcessiveAssociationNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 2, 4),
    _ClMeshNodeExcessiveAssociationNotifEnabled_Type()
)
clMeshNodeExcessiveAssociationNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeExcessiveAssociationNotifEnabled.setStatus("current")


class _ClMeshNodeExcessiveAssociationThreshold_Type(Unsigned32):
    """Custom type clMeshNodeExcessiveAssociationThreshold based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ClMeshNodeExcessiveAssociationThreshold_Type.__name__ = "Unsigned32"
_ClMeshNodeExcessiveAssociationThreshold_Object = MibScalar
clMeshNodeExcessiveAssociationThreshold = _ClMeshNodeExcessiveAssociationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 2, 5),
    _ClMeshNodeExcessiveAssociationThreshold_Type()
)
clMeshNodeExcessiveAssociationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeExcessiveAssociationThreshold.setStatus("current")
_CiscoLwappMeshStatsMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappMeshStatsMIBConform = _CiscoLwappMeshStatsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3)
)
_CiscoLwappMeshStatsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappMeshStatsMIBCompliances = _CiscoLwappMeshStatsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 1)
)
_CiscoLwappMeshStatsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappMeshStatsMIBGroups = _CiscoLwappMeshStatsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2)
)

# Managed Objects groups

ciscoLwappMeshNodeStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 1)
)
ciscoLwappMeshNodeStatsGroup.setObjects(
      *(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeMalformedNeighPkts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePoorNeighSnrPkts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeExcludedPkts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeRxNeighReq"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeRxNeighRsp"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeTxNeighReq"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeTxNeighRsp"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeParentChanges"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNodeStatsGroup.setStatus("current")

ciscoLwappMeshNodePktQueueStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 2)
)
ciscoLwappMeshNodePktQueueStatsGroup.setObjects(
      *(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueueAvg"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueuePeak"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueuePktsDropped"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueueTimeStamp"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueueSize"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNodePktQueueStatsGroup.setStatus("current")

ciscoLwappMeshNodeSecStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 3)
)
ciscoLwappMeshNodeSecStatsGroup.setObjects(
      *(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeSecTxPkts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeSecRxPkts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAssocReqFailures"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAssocReqTimeouts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAssocReqSuccess"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAuthReqFailures"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAuthReqTimeouts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAuthReqSuccess"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeReassocReqFailures"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeReassocReqTimeouts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeReassocReqSuccess"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeReauthReqFailures"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeReauthReqTimeouts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeReauthReqSuccess"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeUnknownAssocReq"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeInvalidAssocReq"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeUnknownReauthReq"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeInvalidReauthReq"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeUnknownReassocReq"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeInvalidReassocReq"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNodeSecStatsGroup.setStatus("current")

ciscoLwappMeshStatsConfigObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 4)
)
ciscoLwappMeshStatsConfigObjsGroup.setObjects(
      *(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeQueueOverflowNotifEnabled"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeStatsTimeInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshStatsConfigObjsGroup.setStatus("current")

ciscoLwappMeshNeighStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 6)
)
ciscoLwappMeshNeighStatsGroup.setObjects(
      *(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNeighAsParentTxPkts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNeighAsParentRxPkts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNeighTotalTxPkts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNeighSuccessTxPkts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNeighRetriesTxPkts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNeighPoorSnrRxPkts"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNeighStatsGroup.setStatus("current")

ciscoLwappMeshStatsNotifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 7)
)
ciscoLwappMeshStatsNotifObjsGroup.setObjects(
    ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshInitiatingApName")
)
if mibBuilder.loadTexts:
    ciscoLwappMeshStatsNotifObjsGroup.setStatus("current")

ciscoLwappMeshAccessClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 8)
)
ciscoLwappMeshAccessClassGroup.setObjects(
      *(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshAccessClassTotalTxPkts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshAccessClassSuccTxPkts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshAccessClassRetryPkts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshAccessClassRTSAttempts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshAccessClassRTSSuccess"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshAccessClassGroup.setStatus("current")

ciscoLwappMeshDataRateStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 9)
)
ciscoLwappMeshDataRateStatsGroup.setObjects(
      *(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshDataRateSuccTxPkts"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshDataRateTxAttempts"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshDataRateStatsGroup.setStatus("current")

ciscoLwappMeshNodeStatsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 10)
)
ciscoLwappMeshNodeStatsGroupSup1.setObjects(
      *(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeSecBackhaulCount"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAssociationCount"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNodeStatsGroupSup1.setStatus("current")

ciscoLwappMeshStatsConfigObjsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 11)
)
ciscoLwappMeshStatsConfigObjsGroupSup1.setObjects(
      *(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeSecBackhaulChangeNotifEnabled"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeExcessiveAssociationNotifEnabled"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeExcessiveAssociationThreshold"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshStatsConfigObjsGroupSup1.setStatus("current")


# Notification objects

ciscoLwappMeshQueueOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 0, 1)
)
ciscoLwappMeshQueueOverflow.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueuePeak"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueuePktsDropped"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshQueueOverflow.setStatus(
        "current"
    )

ciscoLwappMeshExcessiveAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 0, 2)
)
ciscoLwappMeshExcessiveAssociation.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAssociationCount"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshExcessiveAssociation.setStatus(
        "current"
    )

ciscoLwappMeshSecBackhaulChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 0, 3)
)
ciscoLwappMeshSecBackhaulChange.setObjects(
      *(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshInitiatingApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaul"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeSecBackhaulCount"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshSecBackhaulChange.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappMeshStatsNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 5)
)
ciscoLwappMeshStatsNotifsGroup.setObjects(
    ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshQueueOverflow")
)
if mibBuilder.loadTexts:
    ciscoLwappMeshStatsNotifsGroup.setStatus(
        "current"
    )

ciscoLwappMeshStatsNotifsGroupSup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 12)
)
ciscoLwappMeshStatsNotifsGroupSup1.setObjects(
      *(("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshExcessiveAssociation"),
        ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshSecBackhaulChange"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshStatsNotifsGroupSup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappMeshStatsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappMeshStatsMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappMeshStatsMIBComplianceR01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappMeshStatsMIBComplianceR01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-MESH-STATS-MIB",
    **{"ciscoLwappMeshStatsMIB": ciscoLwappMeshStatsMIB,
       "ciscoLwappMeshStatsMIBNotifs": ciscoLwappMeshStatsMIBNotifs,
       "ciscoLwappMeshQueueOverflow": ciscoLwappMeshQueueOverflow,
       "ciscoLwappMeshExcessiveAssociation": ciscoLwappMeshExcessiveAssociation,
       "ciscoLwappMeshSecBackhaulChange": ciscoLwappMeshSecBackhaulChange,
       "ciscoLwappMeshStatsMIBObjects": ciscoLwappMeshStatsMIBObjects,
       "ciscoLwappMeshNodeStats": ciscoLwappMeshNodeStats,
       "clMeshNodeStatsTable": clMeshNodeStatsTable,
       "clMeshNodeStatsEntry": clMeshNodeStatsEntry,
       "clMeshNodeMalformedNeighPkts": clMeshNodeMalformedNeighPkts,
       "clMeshNodePoorNeighSnrPkts": clMeshNodePoorNeighSnrPkts,
       "clMeshNodeExcludedPkts": clMeshNodeExcludedPkts,
       "clMeshNodeRxNeighReq": clMeshNodeRxNeighReq,
       "clMeshNodeRxNeighRsp": clMeshNodeRxNeighRsp,
       "clMeshNodeTxNeighReq": clMeshNodeTxNeighReq,
       "clMeshNodeTxNeighRsp": clMeshNodeTxNeighRsp,
       "clMeshNodeParentChanges": clMeshNodeParentChanges,
       "clMeshNodeSecBackhaulCount": clMeshNodeSecBackhaulCount,
       "clMeshNodeAssociationCount": clMeshNodeAssociationCount,
       "clMeshNodePktQueueStatsTable": clMeshNodePktQueueStatsTable,
       "clMeshNodePktQueueStatsEntry": clMeshNodePktQueueStatsEntry,
       "clMeshNodePktQueueIndex": clMeshNodePktQueueIndex,
       "clMeshNodePktQueueAvg": clMeshNodePktQueueAvg,
       "clMeshNodePktQueuePeak": clMeshNodePktQueuePeak,
       "clMeshNodePktQueuePktsDropped": clMeshNodePktQueuePktsDropped,
       "clMeshNodePktQueueTimeStamp": clMeshNodePktQueueTimeStamp,
       "clMeshNodePktQueueSize": clMeshNodePktQueueSize,
       "clMeshNodeSecStatsTable": clMeshNodeSecStatsTable,
       "clMeshNodeSecStatsEntry": clMeshNodeSecStatsEntry,
       "clMeshNodeSecTxPkts": clMeshNodeSecTxPkts,
       "clMeshNodeSecRxPkts": clMeshNodeSecRxPkts,
       "clMeshNodeAssocReqFailures": clMeshNodeAssocReqFailures,
       "clMeshNodeAssocReqTimeouts": clMeshNodeAssocReqTimeouts,
       "clMeshNodeAssocReqSuccess": clMeshNodeAssocReqSuccess,
       "clMeshNodeAuthReqFailures": clMeshNodeAuthReqFailures,
       "clMeshNodeAuthReqTimeouts": clMeshNodeAuthReqTimeouts,
       "clMeshNodeAuthReqSuccess": clMeshNodeAuthReqSuccess,
       "clMeshNodeReassocReqFailures": clMeshNodeReassocReqFailures,
       "clMeshNodeReassocReqTimeouts": clMeshNodeReassocReqTimeouts,
       "clMeshNodeReassocReqSuccess": clMeshNodeReassocReqSuccess,
       "clMeshNodeReauthReqFailures": clMeshNodeReauthReqFailures,
       "clMeshNodeReauthReqTimeouts": clMeshNodeReauthReqTimeouts,
       "clMeshNodeReauthReqSuccess": clMeshNodeReauthReqSuccess,
       "clMeshNodeUnknownAssocReq": clMeshNodeUnknownAssocReq,
       "clMeshNodeInvalidAssocReq": clMeshNodeInvalidAssocReq,
       "clMeshNodeUnknownReauthReq": clMeshNodeUnknownReauthReq,
       "clMeshNodeInvalidReauthReq": clMeshNodeInvalidReauthReq,
       "clMeshNodeUnknownReassocReq": clMeshNodeUnknownReassocReq,
       "clMeshNodeInvalidReassocReq": clMeshNodeInvalidReassocReq,
       "ciscoLwappMeshNeighStats": ciscoLwappMeshNeighStats,
       "clMeshNeighStatsTable": clMeshNeighStatsTable,
       "clMeshNeighStatsEntry": clMeshNeighStatsEntry,
       "clMeshNeighAsParentTxPkts": clMeshNeighAsParentTxPkts,
       "clMeshNeighAsParentRxPkts": clMeshNeighAsParentRxPkts,
       "clMeshNeighTotalTxPkts": clMeshNeighTotalTxPkts,
       "clMeshNeighSuccessTxPkts": clMeshNeighSuccessTxPkts,
       "clMeshNeighRetriesTxPkts": clMeshNeighRetriesTxPkts,
       "clMeshNeighPoorSnrRxPkts": clMeshNeighPoorSnrRxPkts,
       "ciscoLwappMeshStatsMIBNotifObjects": ciscoLwappMeshStatsMIBNotifObjects,
       "clMeshInitiatingApName": clMeshInitiatingApName,
       "ciscoLwappMeshAccessClass": ciscoLwappMeshAccessClass,
       "clMeshAccessClassTable": clMeshAccessClassTable,
       "clMeshAccessClassEntry": clMeshAccessClassEntry,
       "clMeshAccessClassTotalTxPkts": clMeshAccessClassTotalTxPkts,
       "clMeshAccessClassSuccTxPkts": clMeshAccessClassSuccTxPkts,
       "clMeshAccessClassRetryPkts": clMeshAccessClassRetryPkts,
       "clMeshAccessClassRTSAttempts": clMeshAccessClassRTSAttempts,
       "clMeshAccessClassRTSSuccess": clMeshAccessClassRTSSuccess,
       "ciscoLwappMeshDataRateStats": ciscoLwappMeshDataRateStats,
       "clMeshDataRateStatsTable": clMeshDataRateStatsTable,
       "clMeshDataRateStatsEntry": clMeshDataRateStatsEntry,
       "cLMeshDataRateIndex": cLMeshDataRateIndex,
       "clMeshDataRateSuccTxPkts": clMeshDataRateSuccTxPkts,
       "clMeshDataRateTxAttempts": clMeshDataRateTxAttempts,
       "ciscoLwappMeshStatsMIBConfigObjects": ciscoLwappMeshStatsMIBConfigObjects,
       "clMeshNodeQueueOverflowNotifEnabled": clMeshNodeQueueOverflowNotifEnabled,
       "clMeshNodeStatsTimeInterval": clMeshNodeStatsTimeInterval,
       "clMeshNodeSecBackhaulChangeNotifEnabled": clMeshNodeSecBackhaulChangeNotifEnabled,
       "clMeshNodeExcessiveAssociationNotifEnabled": clMeshNodeExcessiveAssociationNotifEnabled,
       "clMeshNodeExcessiveAssociationThreshold": clMeshNodeExcessiveAssociationThreshold,
       "ciscoLwappMeshStatsMIBConform": ciscoLwappMeshStatsMIBConform,
       "ciscoLwappMeshStatsMIBCompliances": ciscoLwappMeshStatsMIBCompliances,
       "ciscoLwappMeshStatsMIBCompliance": ciscoLwappMeshStatsMIBCompliance,
       "ciscoLwappMeshStatsMIBComplianceR01": ciscoLwappMeshStatsMIBComplianceR01,
       "ciscoLwappMeshStatsMIBGroups": ciscoLwappMeshStatsMIBGroups,
       "ciscoLwappMeshNodeStatsGroup": ciscoLwappMeshNodeStatsGroup,
       "ciscoLwappMeshNodePktQueueStatsGroup": ciscoLwappMeshNodePktQueueStatsGroup,
       "ciscoLwappMeshNodeSecStatsGroup": ciscoLwappMeshNodeSecStatsGroup,
       "ciscoLwappMeshStatsConfigObjsGroup": ciscoLwappMeshStatsConfigObjsGroup,
       "ciscoLwappMeshStatsNotifsGroup": ciscoLwappMeshStatsNotifsGroup,
       "ciscoLwappMeshNeighStatsGroup": ciscoLwappMeshNeighStatsGroup,
       "ciscoLwappMeshStatsNotifObjsGroup": ciscoLwappMeshStatsNotifObjsGroup,
       "ciscoLwappMeshAccessClassGroup": ciscoLwappMeshAccessClassGroup,
       "ciscoLwappMeshDataRateStatsGroup": ciscoLwappMeshDataRateStatsGroup,
       "ciscoLwappMeshNodeStatsGroupSup1": ciscoLwappMeshNodeStatsGroupSup1,
       "ciscoLwappMeshStatsConfigObjsGroupSup1": ciscoLwappMeshStatsConfigObjsGroupSup1,
       "ciscoLwappMeshStatsNotifsGroupSup1": ciscoLwappMeshStatsNotifsGroupSup1}
)
