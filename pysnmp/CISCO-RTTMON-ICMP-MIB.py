# SNMP MIB module (CISCO-RTTMON-ICMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RTTMON-ICMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:48 2024
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

(rttMonCtrlAdminIndex,
 rttMonLatestOper,
 rttMonStats) = mibBuilder.importSymbols(
    "CISCO-RTTMON-MIB",
    "rttMonCtrlAdminIndex",
    "rttMonLatestOper",
    "rttMonStats")

(RttResponseSense,) = mibBuilder.importSymbols(
    "CISCO-RTTMON-TC-MIB",
    "RttResponseSense")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoRttMonIcmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 486)
)
ciscoRttMonIcmpMIB.setRevisions(
        ("2005-08-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RttMonIcmpJitterStatsTable_Object = MibTable
rttMonIcmpJitterStatsTable = _RttMonIcmpJitterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8)
)
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsTable.setStatus("current")
_RttMonIcmpJitterStatsEntry_Object = MibTableRow
rttMonIcmpJitterStatsEntry = _RttMonIcmpJitterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1)
)
rttMonIcmpJitterStatsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsStartTimeId"),
)
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsEntry.setStatus("current")
_RttMonIcmpJitterStatsStartTimeId_Type = TimeStamp
_RttMonIcmpJitterStatsStartTimeId_Object = MibTableColumn
rttMonIcmpJitterStatsStartTimeId = _RttMonIcmpJitterStatsStartTimeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 1),
    _RttMonIcmpJitterStatsStartTimeId_Type()
)
rttMonIcmpJitterStatsStartTimeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsStartTimeId.setStatus("current")
_RttMonIcmpJitterStatsCompletions_Type = Counter32
_RttMonIcmpJitterStatsCompletions_Object = MibTableColumn
rttMonIcmpJitterStatsCompletions = _RttMonIcmpJitterStatsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 2),
    _RttMonIcmpJitterStatsCompletions_Type()
)
rttMonIcmpJitterStatsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsCompletions.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsCompletions.setUnits("completions")
_RttMonIcmpJStatsOverThresholds_Type = Counter32
_RttMonIcmpJStatsOverThresholds_Object = MibTableColumn
rttMonIcmpJStatsOverThresholds = _RttMonIcmpJStatsOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 3),
    _RttMonIcmpJStatsOverThresholds_Type()
)
rttMonIcmpJStatsOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsOverThresholds.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsOverThresholds.setUnits("operations")
_RttMonIcmpJitterStatsNumRTTs_Type = Counter32
_RttMonIcmpJitterStatsNumRTTs_Object = MibTableColumn
rttMonIcmpJitterStatsNumRTTs = _RttMonIcmpJitterStatsNumRTTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 4),
    _RttMonIcmpJitterStatsNumRTTs_Type()
)
rttMonIcmpJitterStatsNumRTTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsNumRTTs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsNumRTTs.setUnits("packets")
_RttMonIcmpJitterStatsRTTSums_Type = Counter32
_RttMonIcmpJitterStatsRTTSums_Object = MibTableColumn
rttMonIcmpJitterStatsRTTSums = _RttMonIcmpJitterStatsRTTSums_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 5),
    _RttMonIcmpJitterStatsRTTSums_Type()
)
rttMonIcmpJitterStatsRTTSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsRTTSums.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsRTTSums.setUnits("milliseconds")
_RttMonIcmpJStatsRTTSum2Lows_Type = Counter32
_RttMonIcmpJStatsRTTSum2Lows_Object = MibTableColumn
rttMonIcmpJStatsRTTSum2Lows = _RttMonIcmpJStatsRTTSum2Lows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 6),
    _RttMonIcmpJStatsRTTSum2Lows_Type()
)
rttMonIcmpJStatsRTTSum2Lows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsRTTSum2Lows.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsRTTSum2Lows.setUnits("milliseconds")
_RttMonIcmpJStatsRTTSum2Highs_Type = Counter32
_RttMonIcmpJStatsRTTSum2Highs_Object = MibTableColumn
rttMonIcmpJStatsRTTSum2Highs = _RttMonIcmpJStatsRTTSum2Highs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 7),
    _RttMonIcmpJStatsRTTSum2Highs_Type()
)
rttMonIcmpJStatsRTTSum2Highs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsRTTSum2Highs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsRTTSum2Highs.setUnits("milliseconds")
_RttMonIcmpJitterStatsRTTMin_Type = Gauge32
_RttMonIcmpJitterStatsRTTMin_Object = MibTableColumn
rttMonIcmpJitterStatsRTTMin = _RttMonIcmpJitterStatsRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 8),
    _RttMonIcmpJitterStatsRTTMin_Type()
)
rttMonIcmpJitterStatsRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsRTTMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsRTTMin.setUnits("milliseconds")
_RttMonIcmpJitterStatsRTTMax_Type = Gauge32
_RttMonIcmpJitterStatsRTTMax_Object = MibTableColumn
rttMonIcmpJitterStatsRTTMax = _RttMonIcmpJitterStatsRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 9),
    _RttMonIcmpJitterStatsRTTMax_Type()
)
rttMonIcmpJitterStatsRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsRTTMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsRTTMax.setUnits("milliseconds")
_RttMonIcmpJitterStatsMinPosSD_Type = Gauge32
_RttMonIcmpJitterStatsMinPosSD_Object = MibTableColumn
rttMonIcmpJitterStatsMinPosSD = _RttMonIcmpJitterStatsMinPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 10),
    _RttMonIcmpJitterStatsMinPosSD_Type()
)
rttMonIcmpJitterStatsMinPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMinPosSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMinPosSD.setUnits("milliseconds")
_RttMonIcmpJitterStatsMaxPosSD_Type = Gauge32
_RttMonIcmpJitterStatsMaxPosSD_Object = MibTableColumn
rttMonIcmpJitterStatsMaxPosSD = _RttMonIcmpJitterStatsMaxPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 11),
    _RttMonIcmpJitterStatsMaxPosSD_Type()
)
rttMonIcmpJitterStatsMaxPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMaxPosSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMaxPosSD.setUnits("milliseconds")
_RttMonIcmpJitterStatsNumPosSDs_Type = Counter32
_RttMonIcmpJitterStatsNumPosSDs_Object = MibTableColumn
rttMonIcmpJitterStatsNumPosSDs = _RttMonIcmpJitterStatsNumPosSDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 12),
    _RttMonIcmpJitterStatsNumPosSDs_Type()
)
rttMonIcmpJitterStatsNumPosSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsNumPosSDs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsNumPosSDs.setUnits("occurrences")
_RttMonIcmpJitterStatsSumPosSDs_Type = Counter32
_RttMonIcmpJitterStatsSumPosSDs_Object = MibTableColumn
rttMonIcmpJitterStatsSumPosSDs = _RttMonIcmpJitterStatsSumPosSDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 13),
    _RttMonIcmpJitterStatsSumPosSDs_Type()
)
rttMonIcmpJitterStatsSumPosSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsSumPosSDs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsSumPosSDs.setUnits("milliseconds")
_RttMonIcmpJStatsSum2PosSDLows_Type = Counter32
_RttMonIcmpJStatsSum2PosSDLows_Object = MibTableColumn
rttMonIcmpJStatsSum2PosSDLows = _RttMonIcmpJStatsSum2PosSDLows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 14),
    _RttMonIcmpJStatsSum2PosSDLows_Type()
)
rttMonIcmpJStatsSum2PosSDLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2PosSDLows.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2PosSDLows.setUnits("milliseconds")
_RttMonIcmpJStatsSum2PosSDHighs_Type = Counter32
_RttMonIcmpJStatsSum2PosSDHighs_Object = MibTableColumn
rttMonIcmpJStatsSum2PosSDHighs = _RttMonIcmpJStatsSum2PosSDHighs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 15),
    _RttMonIcmpJStatsSum2PosSDHighs_Type()
)
rttMonIcmpJStatsSum2PosSDHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2PosSDHighs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2PosSDHighs.setUnits("milliseconds")
_RttMonIcmpJitterStatsMinNegSD_Type = Gauge32
_RttMonIcmpJitterStatsMinNegSD_Object = MibTableColumn
rttMonIcmpJitterStatsMinNegSD = _RttMonIcmpJitterStatsMinNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 16),
    _RttMonIcmpJitterStatsMinNegSD_Type()
)
rttMonIcmpJitterStatsMinNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMinNegSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMinNegSD.setUnits("milliseconds")
_RttMonIcmpJitterStatsMaxNegSD_Type = Gauge32
_RttMonIcmpJitterStatsMaxNegSD_Object = MibTableColumn
rttMonIcmpJitterStatsMaxNegSD = _RttMonIcmpJitterStatsMaxNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 17),
    _RttMonIcmpJitterStatsMaxNegSD_Type()
)
rttMonIcmpJitterStatsMaxNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMaxNegSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMaxNegSD.setUnits("milliseconds")
_RttMonIcmpJitterStatsNumNegSDs_Type = Counter32
_RttMonIcmpJitterStatsNumNegSDs_Object = MibTableColumn
rttMonIcmpJitterStatsNumNegSDs = _RttMonIcmpJitterStatsNumNegSDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 18),
    _RttMonIcmpJitterStatsNumNegSDs_Type()
)
rttMonIcmpJitterStatsNumNegSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsNumNegSDs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsNumNegSDs.setUnits("occurrences")
_RttMonIcmpJitterStatsSumNegSDs_Type = Counter32
_RttMonIcmpJitterStatsSumNegSDs_Object = MibTableColumn
rttMonIcmpJitterStatsSumNegSDs = _RttMonIcmpJitterStatsSumNegSDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 19),
    _RttMonIcmpJitterStatsSumNegSDs_Type()
)
rttMonIcmpJitterStatsSumNegSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsSumNegSDs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsSumNegSDs.setUnits("milliseconds")
_RttMonIcmpJStatsSum2NegSDLows_Type = Counter32
_RttMonIcmpJStatsSum2NegSDLows_Object = MibTableColumn
rttMonIcmpJStatsSum2NegSDLows = _RttMonIcmpJStatsSum2NegSDLows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 20),
    _RttMonIcmpJStatsSum2NegSDLows_Type()
)
rttMonIcmpJStatsSum2NegSDLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2NegSDLows.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2NegSDLows.setUnits("milliseconds")
_RttMonIcmpJStatsSum2NegSDHighs_Type = Counter32
_RttMonIcmpJStatsSum2NegSDHighs_Object = MibTableColumn
rttMonIcmpJStatsSum2NegSDHighs = _RttMonIcmpJStatsSum2NegSDHighs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 21),
    _RttMonIcmpJStatsSum2NegSDHighs_Type()
)
rttMonIcmpJStatsSum2NegSDHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2NegSDHighs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2NegSDHighs.setUnits("milliseconds")
_RttMonIcmpJitterStatsMinPosDS_Type = Gauge32
_RttMonIcmpJitterStatsMinPosDS_Object = MibTableColumn
rttMonIcmpJitterStatsMinPosDS = _RttMonIcmpJitterStatsMinPosDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 22),
    _RttMonIcmpJitterStatsMinPosDS_Type()
)
rttMonIcmpJitterStatsMinPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMinPosDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMinPosDS.setUnits("milliseconds")
_RttMonIcmpJitterStatsMaxPosDS_Type = Gauge32
_RttMonIcmpJitterStatsMaxPosDS_Object = MibTableColumn
rttMonIcmpJitterStatsMaxPosDS = _RttMonIcmpJitterStatsMaxPosDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 23),
    _RttMonIcmpJitterStatsMaxPosDS_Type()
)
rttMonIcmpJitterStatsMaxPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMaxPosDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMaxPosDS.setUnits("milliseconds")
_RttMonIcmpJitterStatsNumPosDSes_Type = Counter32
_RttMonIcmpJitterStatsNumPosDSes_Object = MibTableColumn
rttMonIcmpJitterStatsNumPosDSes = _RttMonIcmpJitterStatsNumPosDSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 24),
    _RttMonIcmpJitterStatsNumPosDSes_Type()
)
rttMonIcmpJitterStatsNumPosDSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsNumPosDSes.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsNumPosDSes.setUnits("occurrences")
_RttMonIcmpJitterStatsSumPosDSes_Type = Counter32
_RttMonIcmpJitterStatsSumPosDSes_Object = MibTableColumn
rttMonIcmpJitterStatsSumPosDSes = _RttMonIcmpJitterStatsSumPosDSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 25),
    _RttMonIcmpJitterStatsSumPosDSes_Type()
)
rttMonIcmpJitterStatsSumPosDSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsSumPosDSes.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsSumPosDSes.setUnits("milliseconds")
_RttMonIcmpJStatsSum2PosDSLows_Type = Counter32
_RttMonIcmpJStatsSum2PosDSLows_Object = MibTableColumn
rttMonIcmpJStatsSum2PosDSLows = _RttMonIcmpJStatsSum2PosDSLows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 26),
    _RttMonIcmpJStatsSum2PosDSLows_Type()
)
rttMonIcmpJStatsSum2PosDSLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2PosDSLows.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2PosDSLows.setUnits("milliseconds")
_RttMonIcmpJStatsSum2PosDSHighs_Type = Counter32
_RttMonIcmpJStatsSum2PosDSHighs_Object = MibTableColumn
rttMonIcmpJStatsSum2PosDSHighs = _RttMonIcmpJStatsSum2PosDSHighs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 27),
    _RttMonIcmpJStatsSum2PosDSHighs_Type()
)
rttMonIcmpJStatsSum2PosDSHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2PosDSHighs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2PosDSHighs.setUnits("milliseconds")
_RttMonIcmpJitterStatsMinNegDS_Type = Gauge32
_RttMonIcmpJitterStatsMinNegDS_Object = MibTableColumn
rttMonIcmpJitterStatsMinNegDS = _RttMonIcmpJitterStatsMinNegDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 28),
    _RttMonIcmpJitterStatsMinNegDS_Type()
)
rttMonIcmpJitterStatsMinNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMinNegDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMinNegDS.setUnits("milliseconds")
_RttMonIcmpJitterStatsMaxNegDS_Type = Gauge32
_RttMonIcmpJitterStatsMaxNegDS_Object = MibTableColumn
rttMonIcmpJitterStatsMaxNegDS = _RttMonIcmpJitterStatsMaxNegDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 29),
    _RttMonIcmpJitterStatsMaxNegDS_Type()
)
rttMonIcmpJitterStatsMaxNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMaxNegDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsMaxNegDS.setUnits("milliseconds")
_RttMonIcmpJitterStatsNumNegDSes_Type = Counter32
_RttMonIcmpJitterStatsNumNegDSes_Object = MibTableColumn
rttMonIcmpJitterStatsNumNegDSes = _RttMonIcmpJitterStatsNumNegDSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 30),
    _RttMonIcmpJitterStatsNumNegDSes_Type()
)
rttMonIcmpJitterStatsNumNegDSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsNumNegDSes.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsNumNegDSes.setUnits("occurrences")
_RttMonIcmpJitterStatsSumNegDSes_Type = Counter32
_RttMonIcmpJitterStatsSumNegDSes_Object = MibTableColumn
rttMonIcmpJitterStatsSumNegDSes = _RttMonIcmpJitterStatsSumNegDSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 31),
    _RttMonIcmpJitterStatsSumNegDSes_Type()
)
rttMonIcmpJitterStatsSumNegDSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsSumNegDSes.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsSumNegDSes.setUnits("milliseconds")
_RttMonIcmpJStatsSum2NegDSLows_Type = Counter32
_RttMonIcmpJStatsSum2NegDSLows_Object = MibTableColumn
rttMonIcmpJStatsSum2NegDSLows = _RttMonIcmpJStatsSum2NegDSLows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 32),
    _RttMonIcmpJStatsSum2NegDSLows_Type()
)
rttMonIcmpJStatsSum2NegDSLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2NegDSLows.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2NegDSLows.setUnits("milliseconds")
_RttMonIcmpJStatsSum2NegDSHighs_Type = Counter32
_RttMonIcmpJStatsSum2NegDSHighs_Object = MibTableColumn
rttMonIcmpJStatsSum2NegDSHighs = _RttMonIcmpJStatsSum2NegDSHighs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 33),
    _RttMonIcmpJStatsSum2NegDSHighs_Type()
)
rttMonIcmpJStatsSum2NegDSHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2NegDSHighs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsSum2NegDSHighs.setUnits("milliseconds")
_RttMonIcmpJitterStatsPktLosses_Type = Counter32
_RttMonIcmpJitterStatsPktLosses_Object = MibTableColumn
rttMonIcmpJitterStatsPktLosses = _RttMonIcmpJitterStatsPktLosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 34),
    _RttMonIcmpJitterStatsPktLosses_Type()
)
rttMonIcmpJitterStatsPktLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsPktLosses.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsPktLosses.setUnits("packets")
_RttMonIcmpJStatsPktOutSeqBoth_Type = Counter32
_RttMonIcmpJStatsPktOutSeqBoth_Object = MibTableColumn
rttMonIcmpJStatsPktOutSeqBoth = _RttMonIcmpJStatsPktOutSeqBoth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 35),
    _RttMonIcmpJStatsPktOutSeqBoth_Type()
)
rttMonIcmpJStatsPktOutSeqBoth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsPktOutSeqBoth.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsPktOutSeqBoth.setUnits("packets")
_RttMonIcmpJStatsPktOutSeqSDs_Type = Counter32
_RttMonIcmpJStatsPktOutSeqSDs_Object = MibTableColumn
rttMonIcmpJStatsPktOutSeqSDs = _RttMonIcmpJStatsPktOutSeqSDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 36),
    _RttMonIcmpJStatsPktOutSeqSDs_Type()
)
rttMonIcmpJStatsPktOutSeqSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsPktOutSeqSDs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsPktOutSeqSDs.setUnits("packets")
_RttMonIcmpJStatsPktOutSeqDSes_Type = Counter32
_RttMonIcmpJStatsPktOutSeqDSes_Object = MibTableColumn
rttMonIcmpJStatsPktOutSeqDSes = _RttMonIcmpJStatsPktOutSeqDSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 37),
    _RttMonIcmpJStatsPktOutSeqDSes_Type()
)
rttMonIcmpJStatsPktOutSeqDSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsPktOutSeqDSes.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsPktOutSeqDSes.setUnits("packets")
_RttMonIcmpJitterStatsPktSkippeds_Type = Counter32
_RttMonIcmpJitterStatsPktSkippeds_Object = MibTableColumn
rttMonIcmpJitterStatsPktSkippeds = _RttMonIcmpJitterStatsPktSkippeds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 38),
    _RttMonIcmpJitterStatsPktSkippeds_Type()
)
rttMonIcmpJitterStatsPktSkippeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsPktSkippeds.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsPktSkippeds.setUnits("packets")
_RttMonIcmpJitterStatsErrors_Type = Counter32
_RttMonIcmpJitterStatsErrors_Object = MibTableColumn
rttMonIcmpJitterStatsErrors = _RttMonIcmpJitterStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 39),
    _RttMonIcmpJitterStatsErrors_Type()
)
rttMonIcmpJitterStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsErrors.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsErrors.setUnits("errors")
_RttMonIcmpJitterStatsBusies_Type = Counter32
_RttMonIcmpJitterStatsBusies_Object = MibTableColumn
rttMonIcmpJitterStatsBusies = _RttMonIcmpJitterStatsBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 40),
    _RttMonIcmpJitterStatsBusies_Type()
)
rttMonIcmpJitterStatsBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsBusies.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsBusies.setUnits("busies")
_RttMonIcmpJitterStatsOWSumSDs_Type = Counter32
_RttMonIcmpJitterStatsOWSumSDs_Object = MibTableColumn
rttMonIcmpJitterStatsOWSumSDs = _RttMonIcmpJitterStatsOWSumSDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 41),
    _RttMonIcmpJitterStatsOWSumSDs_Type()
)
rttMonIcmpJitterStatsOWSumSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsOWSumSDs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsOWSumSDs.setUnits("milliseconds")
_RttMonIcmpJStatsOWSum2SDLows_Type = Counter32
_RttMonIcmpJStatsOWSum2SDLows_Object = MibTableColumn
rttMonIcmpJStatsOWSum2SDLows = _RttMonIcmpJStatsOWSum2SDLows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 42),
    _RttMonIcmpJStatsOWSum2SDLows_Type()
)
rttMonIcmpJStatsOWSum2SDLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsOWSum2SDLows.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsOWSum2SDLows.setUnits("milliseconds")
_RttMonIcmpJStatsOWSum2SDHighs_Type = Counter32
_RttMonIcmpJStatsOWSum2SDHighs_Object = MibTableColumn
rttMonIcmpJStatsOWSum2SDHighs = _RttMonIcmpJStatsOWSum2SDHighs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 43),
    _RttMonIcmpJStatsOWSum2SDHighs_Type()
)
rttMonIcmpJStatsOWSum2SDHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsOWSum2SDHighs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsOWSum2SDHighs.setUnits("milliseconds")
_RttMonIcmpJitterStatsOWMinSD_Type = Gauge32
_RttMonIcmpJitterStatsOWMinSD_Object = MibTableColumn
rttMonIcmpJitterStatsOWMinSD = _RttMonIcmpJitterStatsOWMinSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 44),
    _RttMonIcmpJitterStatsOWMinSD_Type()
)
rttMonIcmpJitterStatsOWMinSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsOWMinSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsOWMinSD.setUnits("milliseconds")
_RttMonIcmpJitterStatsOWMaxSD_Type = Gauge32
_RttMonIcmpJitterStatsOWMaxSD_Object = MibTableColumn
rttMonIcmpJitterStatsOWMaxSD = _RttMonIcmpJitterStatsOWMaxSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 45),
    _RttMonIcmpJitterStatsOWMaxSD_Type()
)
rttMonIcmpJitterStatsOWMaxSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsOWMaxSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsOWMaxSD.setUnits("milliseconds")
_RttMonIcmpJitterStatsOWSumDSes_Type = Counter32
_RttMonIcmpJitterStatsOWSumDSes_Object = MibTableColumn
rttMonIcmpJitterStatsOWSumDSes = _RttMonIcmpJitterStatsOWSumDSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 46),
    _RttMonIcmpJitterStatsOWSumDSes_Type()
)
rttMonIcmpJitterStatsOWSumDSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsOWSumDSes.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsOWSumDSes.setUnits("milliseconds")
_RttMonIcmpJStatsOWSum2DSLows_Type = Counter32
_RttMonIcmpJStatsOWSum2DSLows_Object = MibTableColumn
rttMonIcmpJStatsOWSum2DSLows = _RttMonIcmpJStatsOWSum2DSLows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 47),
    _RttMonIcmpJStatsOWSum2DSLows_Type()
)
rttMonIcmpJStatsOWSum2DSLows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsOWSum2DSLows.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsOWSum2DSLows.setUnits("milliseconds")
_RttMonIcmpJStatsOWSum2DSHighs_Type = Counter32
_RttMonIcmpJStatsOWSum2DSHighs_Object = MibTableColumn
rttMonIcmpJStatsOWSum2DSHighs = _RttMonIcmpJStatsOWSum2DSHighs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 48),
    _RttMonIcmpJStatsOWSum2DSHighs_Type()
)
rttMonIcmpJStatsOWSum2DSHighs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsOWSum2DSHighs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJStatsOWSum2DSHighs.setUnits("milliseconds")
_RttMonIcmpJitterStatsOWMinDS_Type = Gauge32
_RttMonIcmpJitterStatsOWMinDS_Object = MibTableColumn
rttMonIcmpJitterStatsOWMinDS = _RttMonIcmpJitterStatsOWMinDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 49),
    _RttMonIcmpJitterStatsOWMinDS_Type()
)
rttMonIcmpJitterStatsOWMinDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsOWMinDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsOWMinDS.setUnits("milliseconds")
_RttMonIcmpJitterStatsOWMaxDS_Type = Gauge32
_RttMonIcmpJitterStatsOWMaxDS_Object = MibTableColumn
rttMonIcmpJitterStatsOWMaxDS = _RttMonIcmpJitterStatsOWMaxDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 50),
    _RttMonIcmpJitterStatsOWMaxDS_Type()
)
rttMonIcmpJitterStatsOWMaxDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsOWMaxDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsOWMaxDS.setUnits("milliseconds")
_RttMonIcmpJitterStatsNumOWs_Type = Counter32
_RttMonIcmpJitterStatsNumOWs_Object = MibTableColumn
rttMonIcmpJitterStatsNumOWs = _RttMonIcmpJitterStatsNumOWs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 51),
    _RttMonIcmpJitterStatsNumOWs_Type()
)
rttMonIcmpJitterStatsNumOWs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsNumOWs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsNumOWs.setUnits("packets")
_RttMonIcmpJitterStatsAvgJ_Type = Gauge32
_RttMonIcmpJitterStatsAvgJ_Object = MibTableColumn
rttMonIcmpJitterStatsAvgJ = _RttMonIcmpJitterStatsAvgJ_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 52),
    _RttMonIcmpJitterStatsAvgJ_Type()
)
rttMonIcmpJitterStatsAvgJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsAvgJ.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsAvgJ.setUnits("milliseconds")
_RttMonIcmpJitterStatsAvgJSD_Type = Gauge32
_RttMonIcmpJitterStatsAvgJSD_Object = MibTableColumn
rttMonIcmpJitterStatsAvgJSD = _RttMonIcmpJitterStatsAvgJSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 53),
    _RttMonIcmpJitterStatsAvgJSD_Type()
)
rttMonIcmpJitterStatsAvgJSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsAvgJSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsAvgJSD.setUnits("milliseconds")
_RttMonIcmpJitterStatsAvgJDS_Type = Gauge32
_RttMonIcmpJitterStatsAvgJDS_Object = MibTableColumn
rttMonIcmpJitterStatsAvgJDS = _RttMonIcmpJitterStatsAvgJDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 54),
    _RttMonIcmpJitterStatsAvgJDS_Type()
)
rttMonIcmpJitterStatsAvgJDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsAvgJDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsAvgJDS.setUnits("milliseconds")
_RttMonIcmpJitterMinSucPktLoss_Type = Gauge32
_RttMonIcmpJitterMinSucPktLoss_Object = MibTableColumn
rttMonIcmpJitterMinSucPktLoss = _RttMonIcmpJitterMinSucPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 55),
    _RttMonIcmpJitterMinSucPktLoss_Type()
)
rttMonIcmpJitterMinSucPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterMinSucPktLoss.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterMinSucPktLoss.setUnits("packets")
_RttMonIcmpJitterMaxSucPktLoss_Type = Gauge32
_RttMonIcmpJitterMaxSucPktLoss_Object = MibTableColumn
rttMonIcmpJitterMaxSucPktLoss = _RttMonIcmpJitterMaxSucPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 56),
    _RttMonIcmpJitterMaxSucPktLoss_Type()
)
rttMonIcmpJitterMaxSucPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterMaxSucPktLoss.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterMaxSucPktLoss.setUnits("packets")
_RttMonIcmpJitterStatsIAJOut_Type = Gauge32
_RttMonIcmpJitterStatsIAJOut_Object = MibTableColumn
rttMonIcmpJitterStatsIAJOut = _RttMonIcmpJitterStatsIAJOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 57),
    _RttMonIcmpJitterStatsIAJOut_Type()
)
rttMonIcmpJitterStatsIAJOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsIAJOut.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsIAJOut.setUnits("milliseconds")
_RttMonIcmpJitterStatsIAJIn_Type = Gauge32
_RttMonIcmpJitterStatsIAJIn_Object = MibTableColumn
rttMonIcmpJitterStatsIAJIn = _RttMonIcmpJitterStatsIAJIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 58),
    _RttMonIcmpJitterStatsIAJIn_Type()
)
rttMonIcmpJitterStatsIAJIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsIAJIn.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsIAJIn.setUnits("milliseconds")
_RttMonIcmpJitterStatsPktLateAs_Type = Counter32
_RttMonIcmpJitterStatsPktLateAs_Object = MibTableColumn
rttMonIcmpJitterStatsPktLateAs = _RttMonIcmpJitterStatsPktLateAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 8, 1, 59),
    _RttMonIcmpJitterStatsPktLateAs_Type()
)
rttMonIcmpJitterStatsPktLateAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsPktLateAs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonIcmpJitterStatsPktLateAs.setUnits("packets")
_RttMonLatestIcmpJitterOperTable_Object = MibTable
rttMonLatestIcmpJitterOperTable = _RttMonLatestIcmpJitterOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4)
)
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOperTable.setStatus("current")
_RttMonLatestIcmpJitterOperEntry_Object = MibTableRow
rttMonLatestIcmpJitterOperEntry = _RttMonLatestIcmpJitterOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1)
)
rttMonLatestIcmpJitterOperEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOperEntry.setStatus("current")
_RttMonLatestIcmpJitterNumRTT_Type = Gauge32
_RttMonLatestIcmpJitterNumRTT_Object = MibTableColumn
rttMonLatestIcmpJitterNumRTT = _RttMonLatestIcmpJitterNumRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 1),
    _RttMonLatestIcmpJitterNumRTT_Type()
)
rttMonLatestIcmpJitterNumRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterNumRTT.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterNumRTT.setUnits("packets")
_RttMonLatestIcmpJitterRTTSum_Type = Gauge32
_RttMonLatestIcmpJitterRTTSum_Object = MibTableColumn
rttMonLatestIcmpJitterRTTSum = _RttMonLatestIcmpJitterRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 2),
    _RttMonLatestIcmpJitterRTTSum_Type()
)
rttMonLatestIcmpJitterRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterRTTSum.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterRTTSum.setUnits("milliseconds")
_RttMonLatestIcmpJitterRTTSum2_Type = Gauge32
_RttMonLatestIcmpJitterRTTSum2_Object = MibTableColumn
rttMonLatestIcmpJitterRTTSum2 = _RttMonLatestIcmpJitterRTTSum2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 3),
    _RttMonLatestIcmpJitterRTTSum2_Type()
)
rttMonLatestIcmpJitterRTTSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterRTTSum2.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterRTTSum2.setUnits("milliseconds")
_RttMonLatestIcmpJitterRTTMin_Type = Gauge32
_RttMonLatestIcmpJitterRTTMin_Object = MibTableColumn
rttMonLatestIcmpJitterRTTMin = _RttMonLatestIcmpJitterRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 4),
    _RttMonLatestIcmpJitterRTTMin_Type()
)
rttMonLatestIcmpJitterRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterRTTMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterRTTMin.setUnits("milliseconds")
_RttMonLatestIcmpJitterRTTMax_Type = Gauge32
_RttMonLatestIcmpJitterRTTMax_Object = MibTableColumn
rttMonLatestIcmpJitterRTTMax = _RttMonLatestIcmpJitterRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 5),
    _RttMonLatestIcmpJitterRTTMax_Type()
)
rttMonLatestIcmpJitterRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterRTTMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterRTTMax.setUnits("milliseconds")
_RttMonLatestIcmpJitterMinPosSD_Type = Gauge32
_RttMonLatestIcmpJitterMinPosSD_Object = MibTableColumn
rttMonLatestIcmpJitterMinPosSD = _RttMonLatestIcmpJitterMinPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 6),
    _RttMonLatestIcmpJitterMinPosSD_Type()
)
rttMonLatestIcmpJitterMinPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMinPosSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMinPosSD.setUnits("milliseconds")
_RttMonLatestIcmpJitterMaxPosSD_Type = Gauge32
_RttMonLatestIcmpJitterMaxPosSD_Object = MibTableColumn
rttMonLatestIcmpJitterMaxPosSD = _RttMonLatestIcmpJitterMaxPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 7),
    _RttMonLatestIcmpJitterMaxPosSD_Type()
)
rttMonLatestIcmpJitterMaxPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMaxPosSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMaxPosSD.setUnits("milliseconds")
_RttMonLatestIcmpJitterNumPosSD_Type = Gauge32
_RttMonLatestIcmpJitterNumPosSD_Object = MibTableColumn
rttMonLatestIcmpJitterNumPosSD = _RttMonLatestIcmpJitterNumPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 8),
    _RttMonLatestIcmpJitterNumPosSD_Type()
)
rttMonLatestIcmpJitterNumPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterNumPosSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterNumPosSD.setUnits("occurrences")
_RttMonLatestIcmpJitterSumPosSD_Type = Gauge32
_RttMonLatestIcmpJitterSumPosSD_Object = MibTableColumn
rttMonLatestIcmpJitterSumPosSD = _RttMonLatestIcmpJitterSumPosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 9),
    _RttMonLatestIcmpJitterSumPosSD_Type()
)
rttMonLatestIcmpJitterSumPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSumPosSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSumPosSD.setUnits("milliseconds")
_RttMonLatestIcmpJitterSum2PosSD_Type = Gauge32
_RttMonLatestIcmpJitterSum2PosSD_Object = MibTableColumn
rttMonLatestIcmpJitterSum2PosSD = _RttMonLatestIcmpJitterSum2PosSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 10),
    _RttMonLatestIcmpJitterSum2PosSD_Type()
)
rttMonLatestIcmpJitterSum2PosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSum2PosSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSum2PosSD.setUnits("milliseconds")
_RttMonLatestIcmpJitterMinNegSD_Type = Gauge32
_RttMonLatestIcmpJitterMinNegSD_Object = MibTableColumn
rttMonLatestIcmpJitterMinNegSD = _RttMonLatestIcmpJitterMinNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 11),
    _RttMonLatestIcmpJitterMinNegSD_Type()
)
rttMonLatestIcmpJitterMinNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMinNegSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMinNegSD.setUnits("milliseconds")
_RttMonLatestIcmpJitterMaxNegSD_Type = Gauge32
_RttMonLatestIcmpJitterMaxNegSD_Object = MibTableColumn
rttMonLatestIcmpJitterMaxNegSD = _RttMonLatestIcmpJitterMaxNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 12),
    _RttMonLatestIcmpJitterMaxNegSD_Type()
)
rttMonLatestIcmpJitterMaxNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMaxNegSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMaxNegSD.setUnits("milliseconds")
_RttMonLatestIcmpJitterNumNegSD_Type = Gauge32
_RttMonLatestIcmpJitterNumNegSD_Object = MibTableColumn
rttMonLatestIcmpJitterNumNegSD = _RttMonLatestIcmpJitterNumNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 13),
    _RttMonLatestIcmpJitterNumNegSD_Type()
)
rttMonLatestIcmpJitterNumNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterNumNegSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterNumNegSD.setUnits("occurrences")
_RttMonLatestIcmpJitterSumNegSD_Type = Gauge32
_RttMonLatestIcmpJitterSumNegSD_Object = MibTableColumn
rttMonLatestIcmpJitterSumNegSD = _RttMonLatestIcmpJitterSumNegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 14),
    _RttMonLatestIcmpJitterSumNegSD_Type()
)
rttMonLatestIcmpJitterSumNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSumNegSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSumNegSD.setUnits("milliseconds")
_RttMonLatestIcmpJitterSum2NegSD_Type = Gauge32
_RttMonLatestIcmpJitterSum2NegSD_Object = MibTableColumn
rttMonLatestIcmpJitterSum2NegSD = _RttMonLatestIcmpJitterSum2NegSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 15),
    _RttMonLatestIcmpJitterSum2NegSD_Type()
)
rttMonLatestIcmpJitterSum2NegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSum2NegSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSum2NegSD.setUnits("milliseconds")
_RttMonLatestIcmpJitterMinPosDS_Type = Gauge32
_RttMonLatestIcmpJitterMinPosDS_Object = MibTableColumn
rttMonLatestIcmpJitterMinPosDS = _RttMonLatestIcmpJitterMinPosDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 16),
    _RttMonLatestIcmpJitterMinPosDS_Type()
)
rttMonLatestIcmpJitterMinPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMinPosDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMinPosDS.setUnits("milliseconds")
_RttMonLatestIcmpJitterMaxPosDS_Type = Gauge32
_RttMonLatestIcmpJitterMaxPosDS_Object = MibTableColumn
rttMonLatestIcmpJitterMaxPosDS = _RttMonLatestIcmpJitterMaxPosDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 17),
    _RttMonLatestIcmpJitterMaxPosDS_Type()
)
rttMonLatestIcmpJitterMaxPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMaxPosDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMaxPosDS.setUnits("milliseconds")
_RttMonLatestIcmpJitterNumPosDS_Type = Gauge32
_RttMonLatestIcmpJitterNumPosDS_Object = MibTableColumn
rttMonLatestIcmpJitterNumPosDS = _RttMonLatestIcmpJitterNumPosDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 18),
    _RttMonLatestIcmpJitterNumPosDS_Type()
)
rttMonLatestIcmpJitterNumPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterNumPosDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterNumPosDS.setUnits("occurrences")
_RttMonLatestIcmpJitterSumPosDS_Type = Gauge32
_RttMonLatestIcmpJitterSumPosDS_Object = MibTableColumn
rttMonLatestIcmpJitterSumPosDS = _RttMonLatestIcmpJitterSumPosDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 19),
    _RttMonLatestIcmpJitterSumPosDS_Type()
)
rttMonLatestIcmpJitterSumPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSumPosDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSumPosDS.setUnits("milliseconds")
_RttMonLatestIcmpJitterSum2PosDS_Type = Gauge32
_RttMonLatestIcmpJitterSum2PosDS_Object = MibTableColumn
rttMonLatestIcmpJitterSum2PosDS = _RttMonLatestIcmpJitterSum2PosDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 20),
    _RttMonLatestIcmpJitterSum2PosDS_Type()
)
rttMonLatestIcmpJitterSum2PosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSum2PosDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSum2PosDS.setUnits("milliseconds")
_RttMonLatestIcmpJitterMinNegDS_Type = Gauge32
_RttMonLatestIcmpJitterMinNegDS_Object = MibTableColumn
rttMonLatestIcmpJitterMinNegDS = _RttMonLatestIcmpJitterMinNegDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 21),
    _RttMonLatestIcmpJitterMinNegDS_Type()
)
rttMonLatestIcmpJitterMinNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMinNegDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMinNegDS.setUnits("milliseconds")
_RttMonLatestIcmpJitterMaxNegDS_Type = Gauge32
_RttMonLatestIcmpJitterMaxNegDS_Object = MibTableColumn
rttMonLatestIcmpJitterMaxNegDS = _RttMonLatestIcmpJitterMaxNegDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 22),
    _RttMonLatestIcmpJitterMaxNegDS_Type()
)
rttMonLatestIcmpJitterMaxNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMaxNegDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMaxNegDS.setUnits("milliseconds")
_RttMonLatestIcmpJitterNumNegDS_Type = Gauge32
_RttMonLatestIcmpJitterNumNegDS_Object = MibTableColumn
rttMonLatestIcmpJitterNumNegDS = _RttMonLatestIcmpJitterNumNegDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 23),
    _RttMonLatestIcmpJitterNumNegDS_Type()
)
rttMonLatestIcmpJitterNumNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterNumNegDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterNumNegDS.setUnits("occurrences")
_RttMonLatestIcmpJitterSumNegDS_Type = Gauge32
_RttMonLatestIcmpJitterSumNegDS_Object = MibTableColumn
rttMonLatestIcmpJitterSumNegDS = _RttMonLatestIcmpJitterSumNegDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 24),
    _RttMonLatestIcmpJitterSumNegDS_Type()
)
rttMonLatestIcmpJitterSumNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSumNegDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSumNegDS.setUnits("milliseconds")
_RttMonLatestIcmpJitterSum2NegDS_Type = Gauge32
_RttMonLatestIcmpJitterSum2NegDS_Object = MibTableColumn
rttMonLatestIcmpJitterSum2NegDS = _RttMonLatestIcmpJitterSum2NegDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 25),
    _RttMonLatestIcmpJitterSum2NegDS_Type()
)
rttMonLatestIcmpJitterSum2NegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSum2NegDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSum2NegDS.setUnits("milliseconds")
_RttMonLatestIcmpJitterPktLoss_Type = Gauge32
_RttMonLatestIcmpJitterPktLoss_Object = MibTableColumn
rttMonLatestIcmpJitterPktLoss = _RttMonLatestIcmpJitterPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 26),
    _RttMonLatestIcmpJitterPktLoss_Type()
)
rttMonLatestIcmpJitterPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterPktLoss.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterPktLoss.setUnits("packets")
_RttMonLatestIcmpJPktOutSeqBoth_Type = Gauge32
_RttMonLatestIcmpJPktOutSeqBoth_Object = MibTableColumn
rttMonLatestIcmpJPktOutSeqBoth = _RttMonLatestIcmpJPktOutSeqBoth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 27),
    _RttMonLatestIcmpJPktOutSeqBoth_Type()
)
rttMonLatestIcmpJPktOutSeqBoth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJPktOutSeqBoth.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJPktOutSeqBoth.setUnits("packets")
_RttMonLatestIcmpJPktOutSeqSD_Type = Gauge32
_RttMonLatestIcmpJPktOutSeqSD_Object = MibTableColumn
rttMonLatestIcmpJPktOutSeqSD = _RttMonLatestIcmpJPktOutSeqSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 28),
    _RttMonLatestIcmpJPktOutSeqSD_Type()
)
rttMonLatestIcmpJPktOutSeqSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJPktOutSeqSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJPktOutSeqSD.setUnits("packets")
_RttMonLatestIcmpJPktOutSeqDS_Type = Gauge32
_RttMonLatestIcmpJPktOutSeqDS_Object = MibTableColumn
rttMonLatestIcmpJPktOutSeqDS = _RttMonLatestIcmpJPktOutSeqDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 29),
    _RttMonLatestIcmpJPktOutSeqDS_Type()
)
rttMonLatestIcmpJPktOutSeqDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJPktOutSeqDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJPktOutSeqDS.setUnits("packets")
_RttMonLatestIcmpJitterPktSkipped_Type = Gauge32
_RttMonLatestIcmpJitterPktSkipped_Object = MibTableColumn
rttMonLatestIcmpJitterPktSkipped = _RttMonLatestIcmpJitterPktSkipped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 30),
    _RttMonLatestIcmpJitterPktSkipped_Type()
)
rttMonLatestIcmpJitterPktSkipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterPktSkipped.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterPktSkipped.setUnits("packets")
_RttMonLatestIcmpJitterSense_Type = RttResponseSense
_RttMonLatestIcmpJitterSense_Object = MibTableColumn
rttMonLatestIcmpJitterSense = _RttMonLatestIcmpJitterSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 31),
    _RttMonLatestIcmpJitterSense_Type()
)
rttMonLatestIcmpJitterSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterSense.setStatus("current")
_RttMonLatestIcmpJitterPktLateA_Type = Gauge32
_RttMonLatestIcmpJitterPktLateA_Object = MibTableColumn
rttMonLatestIcmpJitterPktLateA = _RttMonLatestIcmpJitterPktLateA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 32),
    _RttMonLatestIcmpJitterPktLateA_Type()
)
rttMonLatestIcmpJitterPktLateA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterPktLateA.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterPktLateA.setUnits("packets")
_RttMonLatestIcmpJitterMinSucPktL_Type = Gauge32
_RttMonLatestIcmpJitterMinSucPktL_Object = MibTableColumn
rttMonLatestIcmpJitterMinSucPktL = _RttMonLatestIcmpJitterMinSucPktL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 33),
    _RttMonLatestIcmpJitterMinSucPktL_Type()
)
rttMonLatestIcmpJitterMinSucPktL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMinSucPktL.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMinSucPktL.setUnits("packets")
_RttMonLatestIcmpJitterMaxSucPktL_Type = Gauge32
_RttMonLatestIcmpJitterMaxSucPktL_Object = MibTableColumn
rttMonLatestIcmpJitterMaxSucPktL = _RttMonLatestIcmpJitterMaxSucPktL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 34),
    _RttMonLatestIcmpJitterMaxSucPktL_Type()
)
rttMonLatestIcmpJitterMaxSucPktL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMaxSucPktL.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterMaxSucPktL.setUnits("packets")
_RttMonLatestIcmpJitterOWSumSD_Type = Gauge32
_RttMonLatestIcmpJitterOWSumSD_Object = MibTableColumn
rttMonLatestIcmpJitterOWSumSD = _RttMonLatestIcmpJitterOWSumSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 35),
    _RttMonLatestIcmpJitterOWSumSD_Type()
)
rttMonLatestIcmpJitterOWSumSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWSumSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWSumSD.setUnits("milliseconds")
_RttMonLatestIcmpJitterOWSum2SD_Type = Gauge32
_RttMonLatestIcmpJitterOWSum2SD_Object = MibTableColumn
rttMonLatestIcmpJitterOWSum2SD = _RttMonLatestIcmpJitterOWSum2SD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 36),
    _RttMonLatestIcmpJitterOWSum2SD_Type()
)
rttMonLatestIcmpJitterOWSum2SD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWSum2SD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWSum2SD.setUnits("milliseconds")
_RttMonLatestIcmpJitterOWMinSD_Type = Gauge32
_RttMonLatestIcmpJitterOWMinSD_Object = MibTableColumn
rttMonLatestIcmpJitterOWMinSD = _RttMonLatestIcmpJitterOWMinSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 37),
    _RttMonLatestIcmpJitterOWMinSD_Type()
)
rttMonLatestIcmpJitterOWMinSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWMinSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWMinSD.setUnits("milliseconds")
_RttMonLatestIcmpJitterOWMaxSD_Type = Gauge32
_RttMonLatestIcmpJitterOWMaxSD_Object = MibTableColumn
rttMonLatestIcmpJitterOWMaxSD = _RttMonLatestIcmpJitterOWMaxSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 38),
    _RttMonLatestIcmpJitterOWMaxSD_Type()
)
rttMonLatestIcmpJitterOWMaxSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWMaxSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWMaxSD.setUnits("milliseconds")
_RttMonLatestIcmpJitterOWSumDS_Type = Gauge32
_RttMonLatestIcmpJitterOWSumDS_Object = MibTableColumn
rttMonLatestIcmpJitterOWSumDS = _RttMonLatestIcmpJitterOWSumDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 39),
    _RttMonLatestIcmpJitterOWSumDS_Type()
)
rttMonLatestIcmpJitterOWSumDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWSumDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWSumDS.setUnits("milliseconds")
_RttMonLatestIcmpJitterOWSum2DS_Type = Gauge32
_RttMonLatestIcmpJitterOWSum2DS_Object = MibTableColumn
rttMonLatestIcmpJitterOWSum2DS = _RttMonLatestIcmpJitterOWSum2DS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 40),
    _RttMonLatestIcmpJitterOWSum2DS_Type()
)
rttMonLatestIcmpJitterOWSum2DS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWSum2DS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWSum2DS.setUnits("milliseconds")
_RttMonLatestIcmpJitterOWMinDS_Type = Gauge32
_RttMonLatestIcmpJitterOWMinDS_Object = MibTableColumn
rttMonLatestIcmpJitterOWMinDS = _RttMonLatestIcmpJitterOWMinDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 41),
    _RttMonLatestIcmpJitterOWMinDS_Type()
)
rttMonLatestIcmpJitterOWMinDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWMinDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWMinDS.setUnits("milliseconds")
_RttMonLatestIcmpJitterOWMaxDS_Type = Gauge32
_RttMonLatestIcmpJitterOWMaxDS_Object = MibTableColumn
rttMonLatestIcmpJitterOWMaxDS = _RttMonLatestIcmpJitterOWMaxDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 42),
    _RttMonLatestIcmpJitterOWMaxDS_Type()
)
rttMonLatestIcmpJitterOWMaxDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWMaxDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWMaxDS.setUnits("milliseconds")
_RttMonLatestIcmpJitterNumOW_Type = Gauge32
_RttMonLatestIcmpJitterNumOW_Object = MibTableColumn
rttMonLatestIcmpJitterNumOW = _RttMonLatestIcmpJitterNumOW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 43),
    _RttMonLatestIcmpJitterNumOW_Type()
)
rttMonLatestIcmpJitterNumOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterNumOW.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterNumOW.setUnits("packets")
_RttMonLatestIcmpJitterAvgJitter_Type = Gauge32
_RttMonLatestIcmpJitterAvgJitter_Object = MibTableColumn
rttMonLatestIcmpJitterAvgJitter = _RttMonLatestIcmpJitterAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 44),
    _RttMonLatestIcmpJitterAvgJitter_Type()
)
rttMonLatestIcmpJitterAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterAvgJitter.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterAvgJitter.setUnits("milliseconds")
_RttMonLatestIcmpJitterAvgSDJ_Type = Gauge32
_RttMonLatestIcmpJitterAvgSDJ_Object = MibTableColumn
rttMonLatestIcmpJitterAvgSDJ = _RttMonLatestIcmpJitterAvgSDJ_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 45),
    _RttMonLatestIcmpJitterAvgSDJ_Type()
)
rttMonLatestIcmpJitterAvgSDJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterAvgSDJ.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterAvgSDJ.setUnits("milliseconds")
_RttMonLatestIcmpJitterAvgDSJ_Type = Gauge32
_RttMonLatestIcmpJitterAvgDSJ_Object = MibTableColumn
rttMonLatestIcmpJitterAvgDSJ = _RttMonLatestIcmpJitterAvgDSJ_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 46),
    _RttMonLatestIcmpJitterAvgDSJ_Type()
)
rttMonLatestIcmpJitterAvgDSJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterAvgDSJ.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterAvgDSJ.setUnits("milliseconds")
_RttMonLatestIcmpJitterOWAvgSD_Type = Gauge32
_RttMonLatestIcmpJitterOWAvgSD_Object = MibTableColumn
rttMonLatestIcmpJitterOWAvgSD = _RttMonLatestIcmpJitterOWAvgSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 47),
    _RttMonLatestIcmpJitterOWAvgSD_Type()
)
rttMonLatestIcmpJitterOWAvgSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWAvgSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWAvgSD.setUnits("milliseconds")
_RttMonLatestIcmpJitterOWAvgDS_Type = Gauge32
_RttMonLatestIcmpJitterOWAvgDS_Object = MibTableColumn
rttMonLatestIcmpJitterOWAvgDS = _RttMonLatestIcmpJitterOWAvgDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 48),
    _RttMonLatestIcmpJitterOWAvgDS_Type()
)
rttMonLatestIcmpJitterOWAvgDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWAvgDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterOWAvgDS.setUnits("milliseconds")
_RttMonLatestIcmpJitterIAJOut_Type = Gauge32
_RttMonLatestIcmpJitterIAJOut_Object = MibTableColumn
rttMonLatestIcmpJitterIAJOut = _RttMonLatestIcmpJitterIAJOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 49),
    _RttMonLatestIcmpJitterIAJOut_Type()
)
rttMonLatestIcmpJitterIAJOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterIAJOut.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterIAJOut.setUnits("milliseconds")
_RttMonLatestIcmpJitterIAJIn_Type = Gauge32
_RttMonLatestIcmpJitterIAJIn_Object = MibTableColumn
rttMonLatestIcmpJitterIAJIn = _RttMonLatestIcmpJitterIAJIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 4, 1, 50),
    _RttMonLatestIcmpJitterIAJIn_Type()
)
rttMonLatestIcmpJitterIAJIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterIAJIn.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestIcmpJitterIAJIn.setUnits("milliseconds")
_CiscoRttMonIcmpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoRttMonIcmpMIBNotifs = _CiscoRttMonIcmpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 486, 0)
)
_CiscoRttMonIcmpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoRttMonIcmpMIBObjects = _CiscoRttMonIcmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 486, 1)
)
_CiscoRttMonIcmpMIBConform_ObjectIdentity = ObjectIdentity
ciscoRttMonIcmpMIBConform = _CiscoRttMonIcmpMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 486, 2)
)
_CiscoRttMonIcmpCompliances_ObjectIdentity = ObjectIdentity
ciscoRttMonIcmpCompliances = _CiscoRttMonIcmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 486, 2, 1)
)
_CiscoRttMonIcmpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoRttMonIcmpMIBGroups = _CiscoRttMonIcmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 486, 2, 2)
)

# Managed Objects groups

ciscoRttMonIcmpJitterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 486, 2, 2, 1)
)
ciscoRttMonIcmpJitterGroup.setObjects(
      *(("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterNumRTT"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterRTTSum"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterRTTSum2"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterRTTMin"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterRTTMax"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterMinPosSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterMaxPosSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterNumPosSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterSumPosSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterSum2PosSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterMinNegSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterMaxNegSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterNumNegSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterSumNegSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterSum2NegSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterMinPosDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterMaxPosDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterNumPosDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterSumPosDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterSum2PosDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterMinNegDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterMaxNegDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterNumNegDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterSumNegDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterSum2NegDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterPktLoss"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJPktOutSeqBoth"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJPktOutSeqSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJPktOutSeqDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterPktSkipped"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterSense"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterPktLateA"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterMinSucPktL"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterMaxSucPktL"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterOWSumSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterOWSum2SD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterOWMinSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterOWMaxSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterOWSumDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterOWSum2DS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterOWMinDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterOWMaxDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterNumOW"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterAvgJitter"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterAvgSDJ"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterAvgDSJ"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterOWAvgSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterOWAvgDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterIAJOut"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonLatestIcmpJitterIAJIn"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsCompletions"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsOverThresholds"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsNumRTTs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsRTTSums"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsRTTSum2Lows"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsRTTSum2Highs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsRTTMin"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsRTTMax"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsMinPosSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsMaxPosSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsNumPosSDs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsSumPosSDs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsSum2PosSDLows"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsSum2PosSDHighs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsMinNegSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsMaxNegSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsNumNegSDs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsSumNegSDs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsSum2NegSDLows"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsSum2NegSDHighs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsMinPosDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsMaxPosDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsNumPosDSes"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsSumPosDSes"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsSum2PosDSLows"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsSum2PosDSHighs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsMinNegDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsMaxNegDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsNumNegDSes"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsSumNegDSes"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsSum2NegDSLows"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsSum2NegDSHighs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsPktLosses"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsPktOutSeqBoth"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsPktOutSeqSDs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsPktOutSeqDSes"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsPktSkippeds"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsErrors"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsBusies"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsOWSumSDs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsOWSum2SDLows"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsOWSum2SDHighs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsOWMinSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsOWMaxSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsOWSumDSes"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsOWSum2DSLows"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJStatsOWSum2DSHighs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsOWMinDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsOWMaxDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsNumOWs"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsAvgJ"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsAvgJSD"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsAvgJDS"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterMinSucPktLoss"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterMaxSucPktLoss"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsIAJOut"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsIAJIn"),
        ("CISCO-RTTMON-ICMP-MIB", "rttMonIcmpJitterStatsPktLateAs"))
)
if mibBuilder.loadTexts:
    ciscoRttMonIcmpJitterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoRttMonIcmpJitterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 486, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoRttMonIcmpJitterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RTTMON-ICMP-MIB",
    **{"rttMonIcmpJitterStatsTable": rttMonIcmpJitterStatsTable,
       "rttMonIcmpJitterStatsEntry": rttMonIcmpJitterStatsEntry,
       "rttMonIcmpJitterStatsStartTimeId": rttMonIcmpJitterStatsStartTimeId,
       "rttMonIcmpJitterStatsCompletions": rttMonIcmpJitterStatsCompletions,
       "rttMonIcmpJStatsOverThresholds": rttMonIcmpJStatsOverThresholds,
       "rttMonIcmpJitterStatsNumRTTs": rttMonIcmpJitterStatsNumRTTs,
       "rttMonIcmpJitterStatsRTTSums": rttMonIcmpJitterStatsRTTSums,
       "rttMonIcmpJStatsRTTSum2Lows": rttMonIcmpJStatsRTTSum2Lows,
       "rttMonIcmpJStatsRTTSum2Highs": rttMonIcmpJStatsRTTSum2Highs,
       "rttMonIcmpJitterStatsRTTMin": rttMonIcmpJitterStatsRTTMin,
       "rttMonIcmpJitterStatsRTTMax": rttMonIcmpJitterStatsRTTMax,
       "rttMonIcmpJitterStatsMinPosSD": rttMonIcmpJitterStatsMinPosSD,
       "rttMonIcmpJitterStatsMaxPosSD": rttMonIcmpJitterStatsMaxPosSD,
       "rttMonIcmpJitterStatsNumPosSDs": rttMonIcmpJitterStatsNumPosSDs,
       "rttMonIcmpJitterStatsSumPosSDs": rttMonIcmpJitterStatsSumPosSDs,
       "rttMonIcmpJStatsSum2PosSDLows": rttMonIcmpJStatsSum2PosSDLows,
       "rttMonIcmpJStatsSum2PosSDHighs": rttMonIcmpJStatsSum2PosSDHighs,
       "rttMonIcmpJitterStatsMinNegSD": rttMonIcmpJitterStatsMinNegSD,
       "rttMonIcmpJitterStatsMaxNegSD": rttMonIcmpJitterStatsMaxNegSD,
       "rttMonIcmpJitterStatsNumNegSDs": rttMonIcmpJitterStatsNumNegSDs,
       "rttMonIcmpJitterStatsSumNegSDs": rttMonIcmpJitterStatsSumNegSDs,
       "rttMonIcmpJStatsSum2NegSDLows": rttMonIcmpJStatsSum2NegSDLows,
       "rttMonIcmpJStatsSum2NegSDHighs": rttMonIcmpJStatsSum2NegSDHighs,
       "rttMonIcmpJitterStatsMinPosDS": rttMonIcmpJitterStatsMinPosDS,
       "rttMonIcmpJitterStatsMaxPosDS": rttMonIcmpJitterStatsMaxPosDS,
       "rttMonIcmpJitterStatsNumPosDSes": rttMonIcmpJitterStatsNumPosDSes,
       "rttMonIcmpJitterStatsSumPosDSes": rttMonIcmpJitterStatsSumPosDSes,
       "rttMonIcmpJStatsSum2PosDSLows": rttMonIcmpJStatsSum2PosDSLows,
       "rttMonIcmpJStatsSum2PosDSHighs": rttMonIcmpJStatsSum2PosDSHighs,
       "rttMonIcmpJitterStatsMinNegDS": rttMonIcmpJitterStatsMinNegDS,
       "rttMonIcmpJitterStatsMaxNegDS": rttMonIcmpJitterStatsMaxNegDS,
       "rttMonIcmpJitterStatsNumNegDSes": rttMonIcmpJitterStatsNumNegDSes,
       "rttMonIcmpJitterStatsSumNegDSes": rttMonIcmpJitterStatsSumNegDSes,
       "rttMonIcmpJStatsSum2NegDSLows": rttMonIcmpJStatsSum2NegDSLows,
       "rttMonIcmpJStatsSum2NegDSHighs": rttMonIcmpJStatsSum2NegDSHighs,
       "rttMonIcmpJitterStatsPktLosses": rttMonIcmpJitterStatsPktLosses,
       "rttMonIcmpJStatsPktOutSeqBoth": rttMonIcmpJStatsPktOutSeqBoth,
       "rttMonIcmpJStatsPktOutSeqSDs": rttMonIcmpJStatsPktOutSeqSDs,
       "rttMonIcmpJStatsPktOutSeqDSes": rttMonIcmpJStatsPktOutSeqDSes,
       "rttMonIcmpJitterStatsPktSkippeds": rttMonIcmpJitterStatsPktSkippeds,
       "rttMonIcmpJitterStatsErrors": rttMonIcmpJitterStatsErrors,
       "rttMonIcmpJitterStatsBusies": rttMonIcmpJitterStatsBusies,
       "rttMonIcmpJitterStatsOWSumSDs": rttMonIcmpJitterStatsOWSumSDs,
       "rttMonIcmpJStatsOWSum2SDLows": rttMonIcmpJStatsOWSum2SDLows,
       "rttMonIcmpJStatsOWSum2SDHighs": rttMonIcmpJStatsOWSum2SDHighs,
       "rttMonIcmpJitterStatsOWMinSD": rttMonIcmpJitterStatsOWMinSD,
       "rttMonIcmpJitterStatsOWMaxSD": rttMonIcmpJitterStatsOWMaxSD,
       "rttMonIcmpJitterStatsOWSumDSes": rttMonIcmpJitterStatsOWSumDSes,
       "rttMonIcmpJStatsOWSum2DSLows": rttMonIcmpJStatsOWSum2DSLows,
       "rttMonIcmpJStatsOWSum2DSHighs": rttMonIcmpJStatsOWSum2DSHighs,
       "rttMonIcmpJitterStatsOWMinDS": rttMonIcmpJitterStatsOWMinDS,
       "rttMonIcmpJitterStatsOWMaxDS": rttMonIcmpJitterStatsOWMaxDS,
       "rttMonIcmpJitterStatsNumOWs": rttMonIcmpJitterStatsNumOWs,
       "rttMonIcmpJitterStatsAvgJ": rttMonIcmpJitterStatsAvgJ,
       "rttMonIcmpJitterStatsAvgJSD": rttMonIcmpJitterStatsAvgJSD,
       "rttMonIcmpJitterStatsAvgJDS": rttMonIcmpJitterStatsAvgJDS,
       "rttMonIcmpJitterMinSucPktLoss": rttMonIcmpJitterMinSucPktLoss,
       "rttMonIcmpJitterMaxSucPktLoss": rttMonIcmpJitterMaxSucPktLoss,
       "rttMonIcmpJitterStatsIAJOut": rttMonIcmpJitterStatsIAJOut,
       "rttMonIcmpJitterStatsIAJIn": rttMonIcmpJitterStatsIAJIn,
       "rttMonIcmpJitterStatsPktLateAs": rttMonIcmpJitterStatsPktLateAs,
       "rttMonLatestIcmpJitterOperTable": rttMonLatestIcmpJitterOperTable,
       "rttMonLatestIcmpJitterOperEntry": rttMonLatestIcmpJitterOperEntry,
       "rttMonLatestIcmpJitterNumRTT": rttMonLatestIcmpJitterNumRTT,
       "rttMonLatestIcmpJitterRTTSum": rttMonLatestIcmpJitterRTTSum,
       "rttMonLatestIcmpJitterRTTSum2": rttMonLatestIcmpJitterRTTSum2,
       "rttMonLatestIcmpJitterRTTMin": rttMonLatestIcmpJitterRTTMin,
       "rttMonLatestIcmpJitterRTTMax": rttMonLatestIcmpJitterRTTMax,
       "rttMonLatestIcmpJitterMinPosSD": rttMonLatestIcmpJitterMinPosSD,
       "rttMonLatestIcmpJitterMaxPosSD": rttMonLatestIcmpJitterMaxPosSD,
       "rttMonLatestIcmpJitterNumPosSD": rttMonLatestIcmpJitterNumPosSD,
       "rttMonLatestIcmpJitterSumPosSD": rttMonLatestIcmpJitterSumPosSD,
       "rttMonLatestIcmpJitterSum2PosSD": rttMonLatestIcmpJitterSum2PosSD,
       "rttMonLatestIcmpJitterMinNegSD": rttMonLatestIcmpJitterMinNegSD,
       "rttMonLatestIcmpJitterMaxNegSD": rttMonLatestIcmpJitterMaxNegSD,
       "rttMonLatestIcmpJitterNumNegSD": rttMonLatestIcmpJitterNumNegSD,
       "rttMonLatestIcmpJitterSumNegSD": rttMonLatestIcmpJitterSumNegSD,
       "rttMonLatestIcmpJitterSum2NegSD": rttMonLatestIcmpJitterSum2NegSD,
       "rttMonLatestIcmpJitterMinPosDS": rttMonLatestIcmpJitterMinPosDS,
       "rttMonLatestIcmpJitterMaxPosDS": rttMonLatestIcmpJitterMaxPosDS,
       "rttMonLatestIcmpJitterNumPosDS": rttMonLatestIcmpJitterNumPosDS,
       "rttMonLatestIcmpJitterSumPosDS": rttMonLatestIcmpJitterSumPosDS,
       "rttMonLatestIcmpJitterSum2PosDS": rttMonLatestIcmpJitterSum2PosDS,
       "rttMonLatestIcmpJitterMinNegDS": rttMonLatestIcmpJitterMinNegDS,
       "rttMonLatestIcmpJitterMaxNegDS": rttMonLatestIcmpJitterMaxNegDS,
       "rttMonLatestIcmpJitterNumNegDS": rttMonLatestIcmpJitterNumNegDS,
       "rttMonLatestIcmpJitterSumNegDS": rttMonLatestIcmpJitterSumNegDS,
       "rttMonLatestIcmpJitterSum2NegDS": rttMonLatestIcmpJitterSum2NegDS,
       "rttMonLatestIcmpJitterPktLoss": rttMonLatestIcmpJitterPktLoss,
       "rttMonLatestIcmpJPktOutSeqBoth": rttMonLatestIcmpJPktOutSeqBoth,
       "rttMonLatestIcmpJPktOutSeqSD": rttMonLatestIcmpJPktOutSeqSD,
       "rttMonLatestIcmpJPktOutSeqDS": rttMonLatestIcmpJPktOutSeqDS,
       "rttMonLatestIcmpJitterPktSkipped": rttMonLatestIcmpJitterPktSkipped,
       "rttMonLatestIcmpJitterSense": rttMonLatestIcmpJitterSense,
       "rttMonLatestIcmpJitterPktLateA": rttMonLatestIcmpJitterPktLateA,
       "rttMonLatestIcmpJitterMinSucPktL": rttMonLatestIcmpJitterMinSucPktL,
       "rttMonLatestIcmpJitterMaxSucPktL": rttMonLatestIcmpJitterMaxSucPktL,
       "rttMonLatestIcmpJitterOWSumSD": rttMonLatestIcmpJitterOWSumSD,
       "rttMonLatestIcmpJitterOWSum2SD": rttMonLatestIcmpJitterOWSum2SD,
       "rttMonLatestIcmpJitterOWMinSD": rttMonLatestIcmpJitterOWMinSD,
       "rttMonLatestIcmpJitterOWMaxSD": rttMonLatestIcmpJitterOWMaxSD,
       "rttMonLatestIcmpJitterOWSumDS": rttMonLatestIcmpJitterOWSumDS,
       "rttMonLatestIcmpJitterOWSum2DS": rttMonLatestIcmpJitterOWSum2DS,
       "rttMonLatestIcmpJitterOWMinDS": rttMonLatestIcmpJitterOWMinDS,
       "rttMonLatestIcmpJitterOWMaxDS": rttMonLatestIcmpJitterOWMaxDS,
       "rttMonLatestIcmpJitterNumOW": rttMonLatestIcmpJitterNumOW,
       "rttMonLatestIcmpJitterAvgJitter": rttMonLatestIcmpJitterAvgJitter,
       "rttMonLatestIcmpJitterAvgSDJ": rttMonLatestIcmpJitterAvgSDJ,
       "rttMonLatestIcmpJitterAvgDSJ": rttMonLatestIcmpJitterAvgDSJ,
       "rttMonLatestIcmpJitterOWAvgSD": rttMonLatestIcmpJitterOWAvgSD,
       "rttMonLatestIcmpJitterOWAvgDS": rttMonLatestIcmpJitterOWAvgDS,
       "rttMonLatestIcmpJitterIAJOut": rttMonLatestIcmpJitterIAJOut,
       "rttMonLatestIcmpJitterIAJIn": rttMonLatestIcmpJitterIAJIn,
       "ciscoRttMonIcmpMIB": ciscoRttMonIcmpMIB,
       "ciscoRttMonIcmpMIBNotifs": ciscoRttMonIcmpMIBNotifs,
       "ciscoRttMonIcmpMIBObjects": ciscoRttMonIcmpMIBObjects,
       "ciscoRttMonIcmpMIBConform": ciscoRttMonIcmpMIBConform,
       "ciscoRttMonIcmpCompliances": ciscoRttMonIcmpCompliances,
       "ciscoRttMonIcmpJitterCompliance": ciscoRttMonIcmpJitterCompliance,
       "ciscoRttMonIcmpMIBGroups": ciscoRttMonIcmpMIBGroups,
       "ciscoRttMonIcmpJitterGroup": ciscoRttMonIcmpJitterGroup}
)
