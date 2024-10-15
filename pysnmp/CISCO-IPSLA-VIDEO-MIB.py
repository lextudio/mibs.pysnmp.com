# SNMP MIB module (CISCO-IPSLA-VIDEO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPSLA-VIDEO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:03 2024
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

(rttMonCtrlAdminIndex,) = mibBuilder.importSymbols(
    "CISCO-RTTMON-MIB",
    "rttMonCtrlAdminIndex")

(RttResponseSense,) = mibBuilder.importSymbols(
    "CISCO-RTTMON-TC-MIB",
    "RttResponseSense")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoIpslaVideoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 744)
)
ciscoIpslaVideoMIB.setRevisions(
        ("2010-06-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIpslaVideoMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIpslaVideoMIBNotifs = _CiscoIpslaVideoMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 0)
)
_CiscoIpslaVideoMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpslaVideoMIBObjects = _CiscoIpslaVideoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1)
)
_CipslaVideoLatestOper_ObjectIdentity = ObjectIdentity
cipslaVideoLatestOper = _CipslaVideoLatestOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1)
)
_CipslaLatestVideoStatsTable_Object = MibTable
cipslaLatestVideoStatsTable = _CipslaLatestVideoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cipslaLatestVideoStatsTable.setStatus("current")
_CipslaLatestVideoStatsEntry_Object = MibTableRow
cipslaLatestVideoStatsEntry = _CipslaLatestVideoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1)
)
cipslaLatestVideoStatsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    cipslaLatestVideoStatsEntry.setStatus("current")
_CipslaLatestVideoMinPosSD_Type = Gauge32
_CipslaLatestVideoMinPosSD_Object = MibTableColumn
cipslaLatestVideoMinPosSD = _CipslaLatestVideoMinPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 1),
    _CipslaLatestVideoMinPosSD_Type()
)
cipslaLatestVideoMinPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoMinPosSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoMinPosSD.setUnits("milliseconds")
_CipslaLatestVideoMaxPosSD_Type = Gauge32
_CipslaLatestVideoMaxPosSD_Object = MibTableColumn
cipslaLatestVideoMaxPosSD = _CipslaLatestVideoMaxPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 2),
    _CipslaLatestVideoMaxPosSD_Type()
)
cipslaLatestVideoMaxPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoMaxPosSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoMaxPosSD.setUnits("milliseconds")
_CipslaLatestVideoNumPosSD_Type = Gauge32
_CipslaLatestVideoNumPosSD_Object = MibTableColumn
cipslaLatestVideoNumPosSD = _CipslaLatestVideoNumPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 3),
    _CipslaLatestVideoNumPosSD_Type()
)
cipslaLatestVideoNumPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoNumPosSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoNumPosSD.setUnits("occurrences")
_CipslaLatestVideoSumPosSD_Type = Gauge32
_CipslaLatestVideoSumPosSD_Object = MibTableColumn
cipslaLatestVideoSumPosSD = _CipslaLatestVideoSumPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 4),
    _CipslaLatestVideoSumPosSD_Type()
)
cipslaLatestVideoSumPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoSumPosSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoSumPosSD.setUnits("milliseconds")
_CipslaLatestVideoSum2PosSD_Type = Gauge32
_CipslaLatestVideoSum2PosSD_Object = MibTableColumn
cipslaLatestVideoSum2PosSD = _CipslaLatestVideoSum2PosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 5),
    _CipslaLatestVideoSum2PosSD_Type()
)
cipslaLatestVideoSum2PosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoSum2PosSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoSum2PosSD.setUnits("milliseconds")
_CipslaLatestVideoMinNegSD_Type = Gauge32
_CipslaLatestVideoMinNegSD_Object = MibTableColumn
cipslaLatestVideoMinNegSD = _CipslaLatestVideoMinNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 6),
    _CipslaLatestVideoMinNegSD_Type()
)
cipslaLatestVideoMinNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoMinNegSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoMinNegSD.setUnits("milliseconds")
_CipslaLatestVideoMaxNegSD_Type = Gauge32
_CipslaLatestVideoMaxNegSD_Object = MibTableColumn
cipslaLatestVideoMaxNegSD = _CipslaLatestVideoMaxNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 7),
    _CipslaLatestVideoMaxNegSD_Type()
)
cipslaLatestVideoMaxNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoMaxNegSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoMaxNegSD.setUnits("milliseconds")
_CipslaLatestVideoNumNegSD_Type = Gauge32
_CipslaLatestVideoNumNegSD_Object = MibTableColumn
cipslaLatestVideoNumNegSD = _CipslaLatestVideoNumNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 8),
    _CipslaLatestVideoNumNegSD_Type()
)
cipslaLatestVideoNumNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoNumNegSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoNumNegSD.setUnits("occurrences")
_CipslaLatestVideoSumNegSD_Type = Gauge32
_CipslaLatestVideoSumNegSD_Object = MibTableColumn
cipslaLatestVideoSumNegSD = _CipslaLatestVideoSumNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 9),
    _CipslaLatestVideoSumNegSD_Type()
)
cipslaLatestVideoSumNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoSumNegSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoSumNegSD.setUnits("milliseconds")
_CipslaLatestVideoSum2NegSD_Type = Gauge32
_CipslaLatestVideoSum2NegSD_Object = MibTableColumn
cipslaLatestVideoSum2NegSD = _CipslaLatestVideoSum2NegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 10),
    _CipslaLatestVideoSum2NegSD_Type()
)
cipslaLatestVideoSum2NegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoSum2NegSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoSum2NegSD.setUnits("milliseconds")
_CipslaLatestVideoPktLossSD_Type = Gauge32
_CipslaLatestVideoPktLossSD_Object = MibTableColumn
cipslaLatestVideoPktLossSD = _CipslaLatestVideoPktLossSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 11),
    _CipslaLatestVideoPktLossSD_Type()
)
cipslaLatestVideoPktLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoPktLossSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoPktLossSD.setUnits("packets")
_CipslaLatestVideoPktOutSeq_Type = Gauge32
_CipslaLatestVideoPktOutSeq_Object = MibTableColumn
cipslaLatestVideoPktOutSeq = _CipslaLatestVideoPktOutSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 12),
    _CipslaLatestVideoPktOutSeq_Type()
)
cipslaLatestVideoPktOutSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoPktOutSeq.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoPktOutSeq.setUnits("packets")
_CipslaLatestVideoSense_Type = RttResponseSense
_CipslaLatestVideoSense_Object = MibTableColumn
cipslaLatestVideoSense = _CipslaLatestVideoSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 13),
    _CipslaLatestVideoSense_Type()
)
cipslaLatestVideoSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoSense.setStatus("current")
_CipslaLatestVideoOWSumSD_Type = Gauge32
_CipslaLatestVideoOWSumSD_Object = MibTableColumn
cipslaLatestVideoOWSumSD = _CipslaLatestVideoOWSumSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 14),
    _CipslaLatestVideoOWSumSD_Type()
)
cipslaLatestVideoOWSumSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoOWSumSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoOWSumSD.setUnits("milliseconds")
_CipslaLatestVideoOWSum2SD_Type = Gauge32
_CipslaLatestVideoOWSum2SD_Object = MibTableColumn
cipslaLatestVideoOWSum2SD = _CipslaLatestVideoOWSum2SD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 15),
    _CipslaLatestVideoOWSum2SD_Type()
)
cipslaLatestVideoOWSum2SD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoOWSum2SD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoOWSum2SD.setUnits("milliseconds")
_CipslaLatestVideoOWMinSD_Type = Gauge32
_CipslaLatestVideoOWMinSD_Object = MibTableColumn
cipslaLatestVideoOWMinSD = _CipslaLatestVideoOWMinSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 16),
    _CipslaLatestVideoOWMinSD_Type()
)
cipslaLatestVideoOWMinSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoOWMinSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoOWMinSD.setUnits("milliseconds")
_CipslaLatestVideoOWMaxSD_Type = Gauge32
_CipslaLatestVideoOWMaxSD_Object = MibTableColumn
cipslaLatestVideoOWMaxSD = _CipslaLatestVideoOWMaxSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 17),
    _CipslaLatestVideoOWMaxSD_Type()
)
cipslaLatestVideoOWMaxSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoOWMaxSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoOWMaxSD.setUnits("milliseconds")
_CipslaLatestVideoNumOWSD_Type = Gauge32
_CipslaLatestVideoNumOWSD_Object = MibTableColumn
cipslaLatestVideoNumOWSD = _CipslaLatestVideoNumOWSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 18),
    _CipslaLatestVideoNumOWSD_Type()
)
cipslaLatestVideoNumOWSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoNumOWSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoNumOWSD.setUnits("packets")
_CipslaLatestVideoAvgJitterSD_Type = Gauge32
_CipslaLatestVideoAvgJitterSD_Object = MibTableColumn
cipslaLatestVideoAvgJitterSD = _CipslaLatestVideoAvgJitterSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 19),
    _CipslaLatestVideoAvgJitterSD_Type()
)
cipslaLatestVideoAvgJitterSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoAvgJitterSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoAvgJitterSD.setUnits("milliseconds")
_CipslaLatestVideoIAJOut_Type = Gauge32
_CipslaLatestVideoIAJOut_Object = MibTableColumn
cipslaLatestVideoIAJOut = _CipslaLatestVideoIAJOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 20),
    _CipslaLatestVideoIAJOut_Type()
)
cipslaLatestVideoIAJOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoIAJOut.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoIAJOut.setUnits("milliseconds")
_CipslaLatestVideoErrSenseDescr_Type = SnmpAdminString
_CipslaLatestVideoErrSenseDescr_Object = MibTableColumn
cipslaLatestVideoErrSenseDescr = _CipslaLatestVideoErrSenseDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 21),
    _CipslaLatestVideoErrSenseDescr_Type()
)
cipslaLatestVideoErrSenseDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoErrSenseDescr.setStatus("current")
_CipslaLatestVideoUnSyncRTs_Type = Counter32
_CipslaLatestVideoUnSyncRTs_Object = MibTableColumn
cipslaLatestVideoUnSyncRTs = _CipslaLatestVideoUnSyncRTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 22),
    _CipslaLatestVideoUnSyncRTs_Type()
)
cipslaLatestVideoUnSyncRTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoUnSyncRTs.setStatus("current")
_CipslaLatestVideoOWSumSDHigh_Type = Gauge32
_CipslaLatestVideoOWSumSDHigh_Object = MibTableColumn
cipslaLatestVideoOWSumSDHigh = _CipslaLatestVideoOWSumSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 23),
    _CipslaLatestVideoOWSumSDHigh_Type()
)
cipslaLatestVideoOWSumSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoOWSumSDHigh.setStatus("current")
_CipslaLatestVideoOWSum2SDHigh_Type = Gauge32
_CipslaLatestVideoOWSum2SDHigh_Object = MibTableColumn
cipslaLatestVideoOWSum2SDHigh = _CipslaLatestVideoOWSum2SDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 24),
    _CipslaLatestVideoOWSum2SDHigh_Type()
)
cipslaLatestVideoOWSum2SDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoOWSum2SDHigh.setStatus("current")


class _CipslaLatestVideoNTPState_Type(Integer32):
    """Custom type cipslaLatestVideoNTPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outOfSync", 2),
          ("sync", 1))
    )


_CipslaLatestVideoNTPState_Type.__name__ = "Integer32"
_CipslaLatestVideoNTPState_Object = MibTableColumn
cipslaLatestVideoNTPState = _CipslaLatestVideoNTPState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 25),
    _CipslaLatestVideoNTPState_Type()
)
cipslaLatestVideoNTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoNTPState.setStatus("current")
_CipslaLatestVideoIPDVAvgSDJ_Type = Gauge32
_CipslaLatestVideoIPDVAvgSDJ_Object = MibTableColumn
cipslaLatestVideoIPDVAvgSDJ = _CipslaLatestVideoIPDVAvgSDJ_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 26),
    _CipslaLatestVideoIPDVAvgSDJ_Type()
)
cipslaLatestVideoIPDVAvgSDJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoIPDVAvgSDJ.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoIPDVAvgSDJ.setUnits("milliseconds")
_CipslaLatestVideoOWAvgSD_Type = Gauge32
_CipslaLatestVideoOWAvgSD_Object = MibTableColumn
cipslaLatestVideoOWAvgSD = _CipslaLatestVideoOWAvgSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 27),
    _CipslaLatestVideoOWAvgSD_Type()
)
cipslaLatestVideoOWAvgSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoOWAvgSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoOWAvgSD.setUnits("milliseconds")
_CipslaLatestVideoPktLateArrival_Type = Gauge32
_CipslaLatestVideoPktLateArrival_Object = MibTableColumn
cipslaLatestVideoPktLateArrival = _CipslaLatestVideoPktLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 1, 1, 1, 28),
    _CipslaLatestVideoPktLateArrival_Type()
)
cipslaLatestVideoPktLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaLatestVideoPktLateArrival.setStatus("current")
if mibBuilder.loadTexts:
    cipslaLatestVideoPktLateArrival.setUnits("packets")
_CipslaVideoStats_ObjectIdentity = ObjectIdentity
cipslaVideoStats = _CipslaVideoStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2)
)
_CipslaVideoAggStatsTable_Object = MibTable
cipslaVideoAggStatsTable = _CipslaVideoAggStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cipslaVideoAggStatsTable.setStatus("current")
_CipslaVideoAggStatsEntry_Object = MibTableRow
cipslaVideoAggStatsEntry = _CipslaVideoAggStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1)
)
cipslaVideoAggStatsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggStartTimeId"),
)
if mibBuilder.loadTexts:
    cipslaVideoAggStatsEntry.setStatus("current")
_CipslaVideoAggStartTimeId_Type = TimeStamp
_CipslaVideoAggStartTimeId_Object = MibTableColumn
cipslaVideoAggStartTimeId = _CipslaVideoAggStartTimeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 1),
    _CipslaVideoAggStartTimeId_Type()
)
cipslaVideoAggStartTimeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipslaVideoAggStartTimeId.setStatus("current")
_CipslaVideoAggCompletions_Type = Counter32
_CipslaVideoAggCompletions_Object = MibTableColumn
cipslaVideoAggCompletions = _CipslaVideoAggCompletions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 2),
    _CipslaVideoAggCompletions_Type()
)
cipslaVideoAggCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggCompletions.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggCompletions.setUnits("completions")
_CipslaVideoAggOverThresholds_Type = Counter32
_CipslaVideoAggOverThresholds_Object = MibTableColumn
cipslaVideoAggOverThresholds = _CipslaVideoAggOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 3),
    _CipslaVideoAggOverThresholds_Type()
)
cipslaVideoAggOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggOverThresholds.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggOverThresholds.setUnits("operations")
_CipslaVideoAggMinPosSD_Type = Gauge32
_CipslaVideoAggMinPosSD_Object = MibTableColumn
cipslaVideoAggMinPosSD = _CipslaVideoAggMinPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 4),
    _CipslaVideoAggMinPosSD_Type()
)
cipslaVideoAggMinPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggMinPosSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggMinPosSD.setUnits("milliseconds")
_CipslaVideoAggMaxPosSD_Type = Gauge32
_CipslaVideoAggMaxPosSD_Object = MibTableColumn
cipslaVideoAggMaxPosSD = _CipslaVideoAggMaxPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 5),
    _CipslaVideoAggMaxPosSD_Type()
)
cipslaVideoAggMaxPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggMaxPosSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggMaxPosSD.setUnits("milliseconds")
_CipslaVideoAggNumPosSD_Type = Counter32
_CipslaVideoAggNumPosSD_Object = MibTableColumn
cipslaVideoAggNumPosSD = _CipslaVideoAggNumPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 6),
    _CipslaVideoAggNumPosSD_Type()
)
cipslaVideoAggNumPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggNumPosSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggNumPosSD.setUnits("occurrences")
_CipslaVideoAggSumPosSD_Type = Counter32
_CipslaVideoAggSumPosSD_Object = MibTableColumn
cipslaVideoAggSumPosSD = _CipslaVideoAggSumPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 7),
    _CipslaVideoAggSumPosSD_Type()
)
cipslaVideoAggSumPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggSumPosSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggSumPosSD.setUnits("milliseconds")
_CipslaVideoAggSum2PosSDLow_Type = Counter32
_CipslaVideoAggSum2PosSDLow_Object = MibTableColumn
cipslaVideoAggSum2PosSDLow = _CipslaVideoAggSum2PosSDLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 8),
    _CipslaVideoAggSum2PosSDLow_Type()
)
cipslaVideoAggSum2PosSDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggSum2PosSDLow.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggSum2PosSDLow.setUnits("milliseconds")
_CipslaVideoAggSum2PosSDHigh_Type = Counter32
_CipslaVideoAggSum2PosSDHigh_Object = MibTableColumn
cipslaVideoAggSum2PosSDHigh = _CipslaVideoAggSum2PosSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 9),
    _CipslaVideoAggSum2PosSDHigh_Type()
)
cipslaVideoAggSum2PosSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggSum2PosSDHigh.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggSum2PosSDHigh.setUnits("milliseconds")
_CipslaVideoAggMinNegSD_Type = Gauge32
_CipslaVideoAggMinNegSD_Object = MibTableColumn
cipslaVideoAggMinNegSD = _CipslaVideoAggMinNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 10),
    _CipslaVideoAggMinNegSD_Type()
)
cipslaVideoAggMinNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggMinNegSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggMinNegSD.setUnits("milliseconds")
_CipslaVideoAggMaxNegSD_Type = Gauge32
_CipslaVideoAggMaxNegSD_Object = MibTableColumn
cipslaVideoAggMaxNegSD = _CipslaVideoAggMaxNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 11),
    _CipslaVideoAggMaxNegSD_Type()
)
cipslaVideoAggMaxNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggMaxNegSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggMaxNegSD.setUnits("milliseconds")
_CipslaVideoAggNumNegSD_Type = Counter32
_CipslaVideoAggNumNegSD_Object = MibTableColumn
cipslaVideoAggNumNegSD = _CipslaVideoAggNumNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 12),
    _CipslaVideoAggNumNegSD_Type()
)
cipslaVideoAggNumNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggNumNegSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggNumNegSD.setUnits("occurrences")
_CipslaVideoAggSumNegSD_Type = Counter32
_CipslaVideoAggSumNegSD_Object = MibTableColumn
cipslaVideoAggSumNegSD = _CipslaVideoAggSumNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 13),
    _CipslaVideoAggSumNegSD_Type()
)
cipslaVideoAggSumNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggSumNegSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggSumNegSD.setUnits("milliseconds")
_CipslaVideoAggSum2NegSDLow_Type = Counter32
_CipslaVideoAggSum2NegSDLow_Object = MibTableColumn
cipslaVideoAggSum2NegSDLow = _CipslaVideoAggSum2NegSDLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 14),
    _CipslaVideoAggSum2NegSDLow_Type()
)
cipslaVideoAggSum2NegSDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggSum2NegSDLow.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggSum2NegSDLow.setUnits("milliseconds")
_CipslaVideoAggSum2NegSDHigh_Type = Counter32
_CipslaVideoAggSum2NegSDHigh_Object = MibTableColumn
cipslaVideoAggSum2NegSDHigh = _CipslaVideoAggSum2NegSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 15),
    _CipslaVideoAggSum2NegSDHigh_Type()
)
cipslaVideoAggSum2NegSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggSum2NegSDHigh.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggSum2NegSDHigh.setUnits("milliseconds")
_CipslaVideoAggPktLossSD_Type = Counter32
_CipslaVideoAggPktLossSD_Object = MibTableColumn
cipslaVideoAggPktLossSD = _CipslaVideoAggPktLossSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 16),
    _CipslaVideoAggPktLossSD_Type()
)
cipslaVideoAggPktLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggPktLossSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggPktLossSD.setUnits("packets")
_CipslaVideoAggPktOutSeq_Type = Counter32
_CipslaVideoAggPktOutSeq_Object = MibTableColumn
cipslaVideoAggPktOutSeq = _CipslaVideoAggPktOutSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 17),
    _CipslaVideoAggPktOutSeq_Type()
)
cipslaVideoAggPktOutSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggPktOutSeq.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggPktOutSeq.setUnits("packets")
_CipslaVideoAggPktSkipped_Type = Counter32
_CipslaVideoAggPktSkipped_Object = MibTableColumn
cipslaVideoAggPktSkipped = _CipslaVideoAggPktSkipped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 18),
    _CipslaVideoAggPktSkipped_Type()
)
cipslaVideoAggPktSkipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggPktSkipped.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggPktSkipped.setUnits("packets")
_CipslaVideoAggErrors_Type = Counter32
_CipslaVideoAggErrors_Object = MibTableColumn
cipslaVideoAggErrors = _CipslaVideoAggErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 19),
    _CipslaVideoAggErrors_Type()
)
cipslaVideoAggErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggErrors.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggErrors.setUnits("errors")
_CipslaVideoAggBusies_Type = Counter32
_CipslaVideoAggBusies_Object = MibTableColumn
cipslaVideoAggBusies = _CipslaVideoAggBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 20),
    _CipslaVideoAggBusies_Type()
)
cipslaVideoAggBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggBusies.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggBusies.setUnits("busies")
_CipslaVideoAggOWSumSD_Type = Counter32
_CipslaVideoAggOWSumSD_Object = MibTableColumn
cipslaVideoAggOWSumSD = _CipslaVideoAggOWSumSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 21),
    _CipslaVideoAggOWSumSD_Type()
)
cipslaVideoAggOWSumSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggOWSumSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggOWSumSD.setUnits("milliseconds")
_CipslaVideoAggOWSum2SDLow_Type = Counter32
_CipslaVideoAggOWSum2SDLow_Object = MibTableColumn
cipslaVideoAggOWSum2SDLow = _CipslaVideoAggOWSum2SDLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 22),
    _CipslaVideoAggOWSum2SDLow_Type()
)
cipslaVideoAggOWSum2SDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggOWSum2SDLow.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggOWSum2SDLow.setUnits("milliseconds")
_CipslaVideoAggOWSum2SDHigh_Type = Counter32
_CipslaVideoAggOWSum2SDHigh_Object = MibTableColumn
cipslaVideoAggOWSum2SDHigh = _CipslaVideoAggOWSum2SDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 23),
    _CipslaVideoAggOWSum2SDHigh_Type()
)
cipslaVideoAggOWSum2SDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggOWSum2SDHigh.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggOWSum2SDHigh.setUnits("milliseconds")
_CipslaVideoAggOWMinSD_Type = Gauge32
_CipslaVideoAggOWMinSD_Object = MibTableColumn
cipslaVideoAggOWMinSD = _CipslaVideoAggOWMinSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 24),
    _CipslaVideoAggOWMinSD_Type()
)
cipslaVideoAggOWMinSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggOWMinSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggOWMinSD.setUnits("milliseconds")
_CipslaVideoAggOWMaxSD_Type = Gauge32
_CipslaVideoAggOWMaxSD_Object = MibTableColumn
cipslaVideoAggOWMaxSD = _CipslaVideoAggOWMaxSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 25),
    _CipslaVideoAggOWMaxSD_Type()
)
cipslaVideoAggOWMaxSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggOWMaxSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggOWMaxSD.setUnits("milliseconds")
_CipslaVideoAggNumOWSD_Type = Counter32
_CipslaVideoAggNumOWSD_Object = MibTableColumn
cipslaVideoAggNumOWSD = _CipslaVideoAggNumOWSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 26),
    _CipslaVideoAggNumOWSD_Type()
)
cipslaVideoAggNumOWSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggNumOWSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggNumOWSD.setUnits("packets")
_CipslaVideoAggAvgJSD_Type = Gauge32
_CipslaVideoAggAvgJSD_Object = MibTableColumn
cipslaVideoAggAvgJSD = _CipslaVideoAggAvgJSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 27),
    _CipslaVideoAggAvgJSD_Type()
)
cipslaVideoAggAvgJSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggAvgJSD.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggAvgJSD.setUnits("milliseconds")
_CipslaVideoAggIAJOut_Type = Gauge32
_CipslaVideoAggIAJOut_Object = MibTableColumn
cipslaVideoAggIAJOut = _CipslaVideoAggIAJOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 28),
    _CipslaVideoAggIAJOut_Type()
)
cipslaVideoAggIAJOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggIAJOut.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggIAJOut.setUnits("milliseconds")
_CipslaVideoAggIAJIn_Type = Gauge32
_CipslaVideoAggIAJIn_Object = MibTableColumn
cipslaVideoAggIAJIn = _CipslaVideoAggIAJIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 29),
    _CipslaVideoAggIAJIn_Type()
)
cipslaVideoAggIAJIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggIAJIn.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggIAJIn.setUnits("milliseconds")
_CipslaVideoAggPktLateArrival_Type = Counter32
_CipslaVideoAggPktLateArrival_Object = MibTableColumn
cipslaVideoAggPktLateArrival = _CipslaVideoAggPktLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 30),
    _CipslaVideoAggPktLateArrival_Type()
)
cipslaVideoAggPktLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggPktLateArrival.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggPktLateArrival.setUnits("packets")
_CipslaVideoAggUnSyncRTs_Type = Counter32
_CipslaVideoAggUnSyncRTs_Object = MibTableColumn
cipslaVideoAggUnSyncRTs = _CipslaVideoAggUnSyncRTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 31),
    _CipslaVideoAggUnSyncRTs_Type()
)
cipslaVideoAggUnSyncRTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggUnSyncRTs.setStatus("current")
_CipslaVideoAggOWSumSDHigh_Type = Counter32
_CipslaVideoAggOWSumSDHigh_Object = MibTableColumn
cipslaVideoAggOWSumSDHigh = _CipslaVideoAggOWSumSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 1, 2, 1, 1, 32),
    _CipslaVideoAggOWSumSDHigh_Type()
)
cipslaVideoAggOWSumSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipslaVideoAggOWSumSDHigh.setStatus("current")
if mibBuilder.loadTexts:
    cipslaVideoAggOWSumSDHigh.setUnits("packets")
_CiscoIpslaVideoMIBConform_ObjectIdentity = ObjectIdentity
ciscoIpslaVideoMIBConform = _CiscoIpslaVideoMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 2)
)
_CiscoIpslaVideoMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpslaVideoMIBCompliances = _CiscoIpslaVideoMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 2, 1)
)
_CiscoIpslaVideoMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpslaVideoMIBGroups = _CiscoIpslaVideoMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 2, 2)
)

# Managed Objects groups

ciscoIpslaVideoStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 2, 2, 1)
)
ciscoIpslaVideoStatsGroup.setObjects(
      *(("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoMinPosSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoMaxPosSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoNumPosSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoSumPosSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoSum2PosSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoMinNegSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoMaxNegSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoNumNegSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoSumNegSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoSum2NegSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoPktLossSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoPktOutSeq"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoSense"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoOWSumSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoOWSum2SD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoOWMinSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoOWMaxSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoNumOWSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoAvgJitterSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoIAJOut"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoErrSenseDescr"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoUnSyncRTs"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoOWSumSDHigh"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoOWSum2SDHigh"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoNTPState"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoIPDVAvgSDJ"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoOWAvgSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaLatestVideoPktLateArrival"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggCompletions"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggOverThresholds"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggMinPosSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggMaxPosSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggNumPosSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggSumPosSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggSum2PosSDLow"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggSum2PosSDHigh"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggMinNegSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggMaxNegSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggNumNegSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggSumNegSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggSum2NegSDLow"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggSum2NegSDHigh"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggPktLossSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggPktOutSeq"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggPktSkipped"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggErrors"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggBusies"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggOWSumSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggOWSum2SDLow"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggOWSum2SDHigh"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggOWMinSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggOWMaxSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggNumOWSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggAvgJSD"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggIAJOut"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggIAJIn"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggPktLateArrival"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggUnSyncRTs"),
        ("CISCO-IPSLA-VIDEO-MIB", "cipslaVideoAggOWSumSDHigh"))
)
if mibBuilder.loadTexts:
    ciscoIpslaVideoStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIpslaVideoMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 744, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpslaVideoMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSLA-VIDEO-MIB",
    **{"ciscoIpslaVideoMIB": ciscoIpslaVideoMIB,
       "ciscoIpslaVideoMIBNotifs": ciscoIpslaVideoMIBNotifs,
       "ciscoIpslaVideoMIBObjects": ciscoIpslaVideoMIBObjects,
       "cipslaVideoLatestOper": cipslaVideoLatestOper,
       "cipslaLatestVideoStatsTable": cipslaLatestVideoStatsTable,
       "cipslaLatestVideoStatsEntry": cipslaLatestVideoStatsEntry,
       "cipslaLatestVideoMinPosSD": cipslaLatestVideoMinPosSD,
       "cipslaLatestVideoMaxPosSD": cipslaLatestVideoMaxPosSD,
       "cipslaLatestVideoNumPosSD": cipslaLatestVideoNumPosSD,
       "cipslaLatestVideoSumPosSD": cipslaLatestVideoSumPosSD,
       "cipslaLatestVideoSum2PosSD": cipslaLatestVideoSum2PosSD,
       "cipslaLatestVideoMinNegSD": cipslaLatestVideoMinNegSD,
       "cipslaLatestVideoMaxNegSD": cipslaLatestVideoMaxNegSD,
       "cipslaLatestVideoNumNegSD": cipslaLatestVideoNumNegSD,
       "cipslaLatestVideoSumNegSD": cipslaLatestVideoSumNegSD,
       "cipslaLatestVideoSum2NegSD": cipslaLatestVideoSum2NegSD,
       "cipslaLatestVideoPktLossSD": cipslaLatestVideoPktLossSD,
       "cipslaLatestVideoPktOutSeq": cipslaLatestVideoPktOutSeq,
       "cipslaLatestVideoSense": cipslaLatestVideoSense,
       "cipslaLatestVideoOWSumSD": cipslaLatestVideoOWSumSD,
       "cipslaLatestVideoOWSum2SD": cipslaLatestVideoOWSum2SD,
       "cipslaLatestVideoOWMinSD": cipslaLatestVideoOWMinSD,
       "cipslaLatestVideoOWMaxSD": cipslaLatestVideoOWMaxSD,
       "cipslaLatestVideoNumOWSD": cipslaLatestVideoNumOWSD,
       "cipslaLatestVideoAvgJitterSD": cipslaLatestVideoAvgJitterSD,
       "cipslaLatestVideoIAJOut": cipslaLatestVideoIAJOut,
       "cipslaLatestVideoErrSenseDescr": cipslaLatestVideoErrSenseDescr,
       "cipslaLatestVideoUnSyncRTs": cipslaLatestVideoUnSyncRTs,
       "cipslaLatestVideoOWSumSDHigh": cipslaLatestVideoOWSumSDHigh,
       "cipslaLatestVideoOWSum2SDHigh": cipslaLatestVideoOWSum2SDHigh,
       "cipslaLatestVideoNTPState": cipslaLatestVideoNTPState,
       "cipslaLatestVideoIPDVAvgSDJ": cipslaLatestVideoIPDVAvgSDJ,
       "cipslaLatestVideoOWAvgSD": cipslaLatestVideoOWAvgSD,
       "cipslaLatestVideoPktLateArrival": cipslaLatestVideoPktLateArrival,
       "cipslaVideoStats": cipslaVideoStats,
       "cipslaVideoAggStatsTable": cipslaVideoAggStatsTable,
       "cipslaVideoAggStatsEntry": cipslaVideoAggStatsEntry,
       "cipslaVideoAggStartTimeId": cipslaVideoAggStartTimeId,
       "cipslaVideoAggCompletions": cipslaVideoAggCompletions,
       "cipslaVideoAggOverThresholds": cipslaVideoAggOverThresholds,
       "cipslaVideoAggMinPosSD": cipslaVideoAggMinPosSD,
       "cipslaVideoAggMaxPosSD": cipslaVideoAggMaxPosSD,
       "cipslaVideoAggNumPosSD": cipslaVideoAggNumPosSD,
       "cipslaVideoAggSumPosSD": cipslaVideoAggSumPosSD,
       "cipslaVideoAggSum2PosSDLow": cipslaVideoAggSum2PosSDLow,
       "cipslaVideoAggSum2PosSDHigh": cipslaVideoAggSum2PosSDHigh,
       "cipslaVideoAggMinNegSD": cipslaVideoAggMinNegSD,
       "cipslaVideoAggMaxNegSD": cipslaVideoAggMaxNegSD,
       "cipslaVideoAggNumNegSD": cipslaVideoAggNumNegSD,
       "cipslaVideoAggSumNegSD": cipslaVideoAggSumNegSD,
       "cipslaVideoAggSum2NegSDLow": cipslaVideoAggSum2NegSDLow,
       "cipslaVideoAggSum2NegSDHigh": cipslaVideoAggSum2NegSDHigh,
       "cipslaVideoAggPktLossSD": cipslaVideoAggPktLossSD,
       "cipslaVideoAggPktOutSeq": cipslaVideoAggPktOutSeq,
       "cipslaVideoAggPktSkipped": cipslaVideoAggPktSkipped,
       "cipslaVideoAggErrors": cipslaVideoAggErrors,
       "cipslaVideoAggBusies": cipslaVideoAggBusies,
       "cipslaVideoAggOWSumSD": cipslaVideoAggOWSumSD,
       "cipslaVideoAggOWSum2SDLow": cipslaVideoAggOWSum2SDLow,
       "cipslaVideoAggOWSum2SDHigh": cipslaVideoAggOWSum2SDHigh,
       "cipslaVideoAggOWMinSD": cipslaVideoAggOWMinSD,
       "cipslaVideoAggOWMaxSD": cipslaVideoAggOWMaxSD,
       "cipslaVideoAggNumOWSD": cipslaVideoAggNumOWSD,
       "cipslaVideoAggAvgJSD": cipslaVideoAggAvgJSD,
       "cipslaVideoAggIAJOut": cipslaVideoAggIAJOut,
       "cipslaVideoAggIAJIn": cipslaVideoAggIAJIn,
       "cipslaVideoAggPktLateArrival": cipslaVideoAggPktLateArrival,
       "cipslaVideoAggUnSyncRTs": cipslaVideoAggUnSyncRTs,
       "cipslaVideoAggOWSumSDHigh": cipslaVideoAggOWSumSDHigh,
       "ciscoIpslaVideoMIBConform": ciscoIpslaVideoMIBConform,
       "ciscoIpslaVideoMIBCompliances": ciscoIpslaVideoMIBCompliances,
       "ciscoIpslaVideoMIBCompliance": ciscoIpslaVideoMIBCompliance,
       "ciscoIpslaVideoMIBGroups": ciscoIpslaVideoMIBGroups,
       "ciscoIpslaVideoStatsGroup": ciscoIpslaVideoStatsGroup}
)
