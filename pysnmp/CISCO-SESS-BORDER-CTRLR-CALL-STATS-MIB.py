# SNMP MIB module (CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:11 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSbcCallStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 657)
)
ciscoSbcCallStatsMIB.setRevisions(
        ("2010-09-03 00:00",
         "2008-08-27 00:00",
         "2008-05-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoSbcPeriodicStatsInterval(Integer32, TextualConvention):
    status = "current"
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
        *(("fifteenMinute", 2),
          ("fiveMinute", 1),
          ("oneDay", 4),
          ("oneHour", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSbcCallStatsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSbcCallStatsMIBNotifs = _CiscoSbcCallStatsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 0)
)
_CiscoSbcCallStatsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSbcCallStatsMIBObjects = _CiscoSbcCallStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1)
)
_CsbCallStatsInstanceTable_Object = MibTable
csbCallStatsInstanceTable = _CsbCallStatsInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 1)
)
if mibBuilder.loadTexts:
    csbCallStatsInstanceTable.setStatus("current")
_CsbCallStatsInstanceEntry_Object = MibTableRow
csbCallStatsInstanceEntry = _CsbCallStatsInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 1, 1)
)
csbCallStatsInstanceEntry.setIndexNames(
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsInstanceIndex"),
)
if mibBuilder.loadTexts:
    csbCallStatsInstanceEntry.setStatus("current")
_CsbCallStatsInstanceIndex_Type = Unsigned32
_CsbCallStatsInstanceIndex_Object = MibTableColumn
csbCallStatsInstanceIndex = _CsbCallStatsInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 1, 1, 1),
    _CsbCallStatsInstanceIndex_Type()
)
csbCallStatsInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbCallStatsInstanceIndex.setStatus("current")
_CsbCallStatsInstancePhysicalIndex_Type = EntPhysicalIndexOrZero
_CsbCallStatsInstancePhysicalIndex_Object = MibTableColumn
csbCallStatsInstancePhysicalIndex = _CsbCallStatsInstancePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 1, 1, 2),
    _CsbCallStatsInstancePhysicalIndex_Type()
)
csbCallStatsInstancePhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsInstancePhysicalIndex.setStatus("current")
_CsbCallStatsTable_Object = MibTable
csbCallStatsTable = _CsbCallStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2)
)
if mibBuilder.loadTexts:
    csbCallStatsTable.setStatus("current")
_CsbCallStatsEntry_Object = MibTableRow
csbCallStatsEntry = _CsbCallStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1)
)
csbCallStatsEntry.setIndexNames(
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsInstanceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsServiceIndex"),
)
if mibBuilder.loadTexts:
    csbCallStatsEntry.setStatus("current")
_CsbCallStatsServiceIndex_Type = Unsigned32
_CsbCallStatsServiceIndex_Object = MibTableColumn
csbCallStatsServiceIndex = _CsbCallStatsServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 1),
    _CsbCallStatsServiceIndex_Type()
)
csbCallStatsServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbCallStatsServiceIndex.setStatus("current")
_CsbCallStatsSbcName_Type = SnmpAdminString
_CsbCallStatsSbcName_Object = MibTableColumn
csbCallStatsSbcName = _CsbCallStatsSbcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 2),
    _CsbCallStatsSbcName_Type()
)
csbCallStatsSbcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsSbcName.setStatus("current")
_CsbCallStatsCallsHigh_Type = Unsigned32
_CsbCallStatsCallsHigh_Object = MibTableColumn
csbCallStatsCallsHigh = _CsbCallStatsCallsHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 3),
    _CsbCallStatsCallsHigh_Type()
)
csbCallStatsCallsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsCallsHigh.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsCallsHigh.setUnits("calls per second")
_CsbCallStatsRate1Sec_Type = Gauge32
_CsbCallStatsRate1Sec_Object = MibTableColumn
csbCallStatsRate1Sec = _CsbCallStatsRate1Sec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 4),
    _CsbCallStatsRate1Sec_Type()
)
csbCallStatsRate1Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsRate1Sec.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsRate1Sec.setUnits("calls per second")
_CsbCallStatsCallsLow_Type = Unsigned32
_CsbCallStatsCallsLow_Object = MibTableColumn
csbCallStatsCallsLow = _CsbCallStatsCallsLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 5),
    _CsbCallStatsCallsLow_Type()
)
csbCallStatsCallsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsCallsLow.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsCallsLow.setUnits("calls per second")
_CsbCallStatsAvailableFlows_Type = Gauge32
_CsbCallStatsAvailableFlows_Object = MibTableColumn
csbCallStatsAvailableFlows = _CsbCallStatsAvailableFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 6),
    _CsbCallStatsAvailableFlows_Type()
)
csbCallStatsAvailableFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsAvailableFlows.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsAvailableFlows.setUnits("flows")
_CsbCallStatsUsedFlows_Type = Gauge32
_CsbCallStatsUsedFlows_Object = MibTableColumn
csbCallStatsUsedFlows = _CsbCallStatsUsedFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 7),
    _CsbCallStatsUsedFlows_Type()
)
csbCallStatsUsedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsUsedFlows.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsUsedFlows.setUnits("flows")
_CsbCallStatsPeakFlows_Type = Unsigned32
_CsbCallStatsPeakFlows_Object = MibTableColumn
csbCallStatsPeakFlows = _CsbCallStatsPeakFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 8),
    _CsbCallStatsPeakFlows_Type()
)
csbCallStatsPeakFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsPeakFlows.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsPeakFlows.setUnits("flows")
_CsbCallStatsTotalFlows_Type = Unsigned32
_CsbCallStatsTotalFlows_Object = MibTableColumn
csbCallStatsTotalFlows = _CsbCallStatsTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 9),
    _CsbCallStatsTotalFlows_Type()
)
csbCallStatsTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsTotalFlows.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsTotalFlows.setUnits("flows")
_CsbCallStatsUsedSigFlows_Type = Gauge32
_CsbCallStatsUsedSigFlows_Object = MibTableColumn
csbCallStatsUsedSigFlows = _CsbCallStatsUsedSigFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 10),
    _CsbCallStatsUsedSigFlows_Type()
)
csbCallStatsUsedSigFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsUsedSigFlows.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsUsedSigFlows.setUnits("signal flows")
_CsbCallStatsPeakSigFlows_Type = Unsigned32
_CsbCallStatsPeakSigFlows_Object = MibTableColumn
csbCallStatsPeakSigFlows = _CsbCallStatsPeakSigFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 11),
    _CsbCallStatsPeakSigFlows_Type()
)
csbCallStatsPeakSigFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsPeakSigFlows.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsPeakSigFlows.setUnits("signal flows")
_CsbCallStatsTotalSigFlows_Type = Unsigned32
_CsbCallStatsTotalSigFlows_Object = MibTableColumn
csbCallStatsTotalSigFlows = _CsbCallStatsTotalSigFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 12),
    _CsbCallStatsTotalSigFlows_Type()
)
csbCallStatsTotalSigFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsTotalSigFlows.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsTotalSigFlows.setUnits("signal flows")
_CsbCallStatsAvailablePktRate_Type = Gauge32
_CsbCallStatsAvailablePktRate_Object = MibTableColumn
csbCallStatsAvailablePktRate = _CsbCallStatsAvailablePktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 13),
    _CsbCallStatsAvailablePktRate_Type()
)
csbCallStatsAvailablePktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsAvailablePktRate.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsAvailablePktRate.setUnits("packets per second")
_CsbCallStatsUnclassifiedPkts_Type = Counter64
_CsbCallStatsUnclassifiedPkts_Object = MibTableColumn
csbCallStatsUnclassifiedPkts = _CsbCallStatsUnclassifiedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 14),
    _CsbCallStatsUnclassifiedPkts_Type()
)
csbCallStatsUnclassifiedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsUnclassifiedPkts.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsUnclassifiedPkts.setUnits("packets")
_CsbCallStatsRTPPktsSent_Type = Counter64
_CsbCallStatsRTPPktsSent_Object = MibTableColumn
csbCallStatsRTPPktsSent = _CsbCallStatsRTPPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 15),
    _CsbCallStatsRTPPktsSent_Type()
)
csbCallStatsRTPPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsRTPPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsRTPPktsSent.setUnits("packets")
_CsbCallStatsRTPPktsRcvd_Type = Counter64
_CsbCallStatsRTPPktsRcvd_Object = MibTableColumn
csbCallStatsRTPPktsRcvd = _CsbCallStatsRTPPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 16),
    _CsbCallStatsRTPPktsRcvd_Type()
)
csbCallStatsRTPPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsRTPPktsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsRTPPktsRcvd.setUnits("packets")
_CsbCallStatsRTPPktsDiscard_Type = Counter64
_CsbCallStatsRTPPktsDiscard_Object = MibTableColumn
csbCallStatsRTPPktsDiscard = _CsbCallStatsRTPPktsDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 17),
    _CsbCallStatsRTPPktsDiscard_Type()
)
csbCallStatsRTPPktsDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsRTPPktsDiscard.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsRTPPktsDiscard.setUnits("packets")
_CsbCallStatsRTPOctetsSent_Type = Counter64
_CsbCallStatsRTPOctetsSent_Object = MibTableColumn
csbCallStatsRTPOctetsSent = _CsbCallStatsRTPOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 18),
    _CsbCallStatsRTPOctetsSent_Type()
)
csbCallStatsRTPOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsRTPOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsRTPOctetsSent.setUnits("octets")
_CsbCallStatsRTPOctetsRcvd_Type = Counter64
_CsbCallStatsRTPOctetsRcvd_Object = MibTableColumn
csbCallStatsRTPOctetsRcvd = _CsbCallStatsRTPOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 19),
    _CsbCallStatsRTPOctetsRcvd_Type()
)
csbCallStatsRTPOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsRTPOctetsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsRTPOctetsRcvd.setUnits("octets")
_CsbCallStatsRTPOctetsDiscard_Type = Counter64
_CsbCallStatsRTPOctetsDiscard_Object = MibTableColumn
csbCallStatsRTPOctetsDiscard = _CsbCallStatsRTPOctetsDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 20),
    _CsbCallStatsRTPOctetsDiscard_Type()
)
csbCallStatsRTPOctetsDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsRTPOctetsDiscard.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsRTPOctetsDiscard.setUnits("octets")
_CsbCallStatsNoMediaCount_Type = Counter32
_CsbCallStatsNoMediaCount_Object = MibTableColumn
csbCallStatsNoMediaCount = _CsbCallStatsNoMediaCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 21),
    _CsbCallStatsNoMediaCount_Type()
)
csbCallStatsNoMediaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsNoMediaCount.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsNoMediaCount.setUnits("no media events")
_CsbCallStatsRouteErrors_Type = Counter32
_CsbCallStatsRouteErrors_Object = MibTableColumn
csbCallStatsRouteErrors = _CsbCallStatsRouteErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 22),
    _CsbCallStatsRouteErrors_Type()
)
csbCallStatsRouteErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsRouteErrors.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsRouteErrors.setUnits("route error events")
_CsbCallStatsAvailableTranscodeFlows_Type = Gauge32
_CsbCallStatsAvailableTranscodeFlows_Object = MibTableColumn
csbCallStatsAvailableTranscodeFlows = _CsbCallStatsAvailableTranscodeFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 23),
    _CsbCallStatsAvailableTranscodeFlows_Type()
)
csbCallStatsAvailableTranscodeFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsAvailableTranscodeFlows.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsAvailableTranscodeFlows.setUnits("flows")
_CsbCallStatsActiveTranscodeFlows_Type = Gauge32
_CsbCallStatsActiveTranscodeFlows_Object = MibTableColumn
csbCallStatsActiveTranscodeFlows = _CsbCallStatsActiveTranscodeFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 24),
    _CsbCallStatsActiveTranscodeFlows_Type()
)
csbCallStatsActiveTranscodeFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsActiveTranscodeFlows.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsActiveTranscodeFlows.setUnits("flows")
_CsbCallStatsPeakTranscodeFlows_Type = Unsigned32
_CsbCallStatsPeakTranscodeFlows_Object = MibTableColumn
csbCallStatsPeakTranscodeFlows = _CsbCallStatsPeakTranscodeFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 25),
    _CsbCallStatsPeakTranscodeFlows_Type()
)
csbCallStatsPeakTranscodeFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsPeakTranscodeFlows.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsPeakTranscodeFlows.setUnits("flows")
_CsbCallStatsTotalTranscodeFlows_Type = Unsigned32
_CsbCallStatsTotalTranscodeFlows_Object = MibTableColumn
csbCallStatsTotalTranscodeFlows = _CsbCallStatsTotalTranscodeFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 2, 1, 26),
    _CsbCallStatsTotalTranscodeFlows_Type()
)
csbCallStatsTotalTranscodeFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCallStatsTotalTranscodeFlows.setStatus("current")
if mibBuilder.loadTexts:
    csbCallStatsTotalTranscodeFlows.setUnits("flows")
_CsbCurrPeriodicStatsTable_Object = MibTable
csbCurrPeriodicStatsTable = _CsbCurrPeriodicStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3)
)
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsTable.setStatus("current")
_CsbCurrPeriodicStatsEntry_Object = MibTableRow
csbCurrPeriodicStatsEntry = _CsbCurrPeriodicStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1)
)
csbCurrPeriodicStatsEntry.setIndexNames(
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsInstanceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsServiceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsInterval"),
)
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsEntry.setStatus("current")
_CsbCurrPeriodicStatsInterval_Type = CiscoSbcPeriodicStatsInterval
_CsbCurrPeriodicStatsInterval_Object = MibTableColumn
csbCurrPeriodicStatsInterval = _CsbCurrPeriodicStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 1),
    _CsbCurrPeriodicStatsInterval_Type()
)
csbCurrPeriodicStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsInterval.setStatus("current")
_CsbCurrPeriodicStatsActiveCalls_Type = Gauge32
_CsbCurrPeriodicStatsActiveCalls_Object = MibTableColumn
csbCurrPeriodicStatsActiveCalls = _CsbCurrPeriodicStatsActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 2),
    _CsbCurrPeriodicStatsActiveCalls_Type()
)
csbCurrPeriodicStatsActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsActiveCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsActiveCalls.setUnits("calls")
_CsbCurrPeriodicStatsActivatingCalls_Type = Gauge32
_CsbCurrPeriodicStatsActivatingCalls_Object = MibTableColumn
csbCurrPeriodicStatsActivatingCalls = _CsbCurrPeriodicStatsActivatingCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 3),
    _CsbCurrPeriodicStatsActivatingCalls_Type()
)
csbCurrPeriodicStatsActivatingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsActivatingCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsActivatingCalls.setUnits("calls")
_CsbCurrPeriodicStatsDeactivatingCalls_Type = Gauge32
_CsbCurrPeriodicStatsDeactivatingCalls_Object = MibTableColumn
csbCurrPeriodicStatsDeactivatingCalls = _CsbCurrPeriodicStatsDeactivatingCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 4),
    _CsbCurrPeriodicStatsDeactivatingCalls_Type()
)
csbCurrPeriodicStatsDeactivatingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsDeactivatingCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsDeactivatingCalls.setUnits("calls")
_CsbCurrPeriodicStatsTotalCallAttempts_Type = Gauge32
_CsbCurrPeriodicStatsTotalCallAttempts_Object = MibTableColumn
csbCurrPeriodicStatsTotalCallAttempts = _CsbCurrPeriodicStatsTotalCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 5),
    _CsbCurrPeriodicStatsTotalCallAttempts_Type()
)
csbCurrPeriodicStatsTotalCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsTotalCallAttempts.setStatus("current")
_CsbCurrPeriodicStatsFailedCallAttempts_Type = Gauge32
_CsbCurrPeriodicStatsFailedCallAttempts_Object = MibTableColumn
csbCurrPeriodicStatsFailedCallAttempts = _CsbCurrPeriodicStatsFailedCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 6),
    _CsbCurrPeriodicStatsFailedCallAttempts_Type()
)
csbCurrPeriodicStatsFailedCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsFailedCallAttempts.setStatus("current")
_CsbCurrPeriodicStatsCallRoutingFailure_Type = Gauge32
_CsbCurrPeriodicStatsCallRoutingFailure_Object = MibTableColumn
csbCurrPeriodicStatsCallRoutingFailure = _CsbCurrPeriodicStatsCallRoutingFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 7),
    _CsbCurrPeriodicStatsCallRoutingFailure_Type()
)
csbCurrPeriodicStatsCallRoutingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCallRoutingFailure.setStatus("current")
_CsbCurrPeriodicStatsCallResourceFailure_Type = Gauge32
_CsbCurrPeriodicStatsCallResourceFailure_Object = MibTableColumn
csbCurrPeriodicStatsCallResourceFailure = _CsbCurrPeriodicStatsCallResourceFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 8),
    _CsbCurrPeriodicStatsCallResourceFailure_Type()
)
csbCurrPeriodicStatsCallResourceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCallResourceFailure.setStatus("current")
_CsbCurrPeriodicStatsCallMediaFailure_Type = Gauge32
_CsbCurrPeriodicStatsCallMediaFailure_Object = MibTableColumn
csbCurrPeriodicStatsCallMediaFailure = _CsbCurrPeriodicStatsCallMediaFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 9),
    _CsbCurrPeriodicStatsCallMediaFailure_Type()
)
csbCurrPeriodicStatsCallMediaFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCallMediaFailure.setStatus("current")
_CsbCurrPeriodicStatsCallSigFailure_Type = Gauge32
_CsbCurrPeriodicStatsCallSigFailure_Object = MibTableColumn
csbCurrPeriodicStatsCallSigFailure = _CsbCurrPeriodicStatsCallSigFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 10),
    _CsbCurrPeriodicStatsCallSigFailure_Type()
)
csbCurrPeriodicStatsCallSigFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCallSigFailure.setStatus("current")
_CsbCurrPeriodicStatsActiveCallFailure_Type = Gauge32
_CsbCurrPeriodicStatsActiveCallFailure_Object = MibTableColumn
csbCurrPeriodicStatsActiveCallFailure = _CsbCurrPeriodicStatsActiveCallFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 11),
    _CsbCurrPeriodicStatsActiveCallFailure_Type()
)
csbCurrPeriodicStatsActiveCallFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsActiveCallFailure.setStatus("current")
_CsbCurrPeriodicStatsCongestionFailure_Type = Gauge32
_CsbCurrPeriodicStatsCongestionFailure_Object = MibTableColumn
csbCurrPeriodicStatsCongestionFailure = _CsbCurrPeriodicStatsCongestionFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 12),
    _CsbCurrPeriodicStatsCongestionFailure_Type()
)
csbCurrPeriodicStatsCongestionFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCongestionFailure.setStatus("current")
_CsbCurrPeriodicStatsCallSetupPolicyFailure_Type = Gauge32
_CsbCurrPeriodicStatsCallSetupPolicyFailure_Object = MibTableColumn
csbCurrPeriodicStatsCallSetupPolicyFailure = _CsbCurrPeriodicStatsCallSetupPolicyFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 13),
    _CsbCurrPeriodicStatsCallSetupPolicyFailure_Type()
)
csbCurrPeriodicStatsCallSetupPolicyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCallSetupPolicyFailure.setStatus("current")
_CsbCurrPeriodicStatsCallSetupNAPolicyFailure_Type = Gauge32
_CsbCurrPeriodicStatsCallSetupNAPolicyFailure_Object = MibTableColumn
csbCurrPeriodicStatsCallSetupNAPolicyFailure = _CsbCurrPeriodicStatsCallSetupNAPolicyFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 14),
    _CsbCurrPeriodicStatsCallSetupNAPolicyFailure_Type()
)
csbCurrPeriodicStatsCallSetupNAPolicyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCallSetupNAPolicyFailure.setStatus("current")
_CsbCurrPeriodicStatsCallSetupRoutingPolicyFailure_Type = Gauge32
_CsbCurrPeriodicStatsCallSetupRoutingPolicyFailure_Object = MibTableColumn
csbCurrPeriodicStatsCallSetupRoutingPolicyFailure = _CsbCurrPeriodicStatsCallSetupRoutingPolicyFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 15),
    _CsbCurrPeriodicStatsCallSetupRoutingPolicyFailure_Type()
)
csbCurrPeriodicStatsCallSetupRoutingPolicyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCallSetupRoutingPolicyFailure.setStatus("current")
_CsbCurrPeriodicStatsCallSetupCACPolicyFailure_Type = Gauge32
_CsbCurrPeriodicStatsCallSetupCACPolicyFailure_Object = MibTableColumn
csbCurrPeriodicStatsCallSetupCACPolicyFailure = _CsbCurrPeriodicStatsCallSetupCACPolicyFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 16),
    _CsbCurrPeriodicStatsCallSetupCACPolicyFailure_Type()
)
csbCurrPeriodicStatsCallSetupCACPolicyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCallSetupCACPolicyFailure.setStatus("current")
_CsbCurrPeriodicStatsCallSetupCACCallLimitFailure_Type = Gauge32
_CsbCurrPeriodicStatsCallSetupCACCallLimitFailure_Object = MibTableColumn
csbCurrPeriodicStatsCallSetupCACCallLimitFailure = _CsbCurrPeriodicStatsCallSetupCACCallLimitFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 17),
    _CsbCurrPeriodicStatsCallSetupCACCallLimitFailure_Type()
)
csbCurrPeriodicStatsCallSetupCACCallLimitFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCallSetupCACCallLimitFailure.setStatus("current")
_CsbCurrPeriodicStatsCallSetupCACRateLimitFailure_Type = Gauge32
_CsbCurrPeriodicStatsCallSetupCACRateLimitFailure_Object = MibTableColumn
csbCurrPeriodicStatsCallSetupCACRateLimitFailure = _CsbCurrPeriodicStatsCallSetupCACRateLimitFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 18),
    _CsbCurrPeriodicStatsCallSetupCACRateLimitFailure_Type()
)
csbCurrPeriodicStatsCallSetupCACRateLimitFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCallSetupCACRateLimitFailure.setStatus("current")
_CsbCurrPeriodicStatsCallSetupCACBandwidthFailure_Type = Gauge32
_CsbCurrPeriodicStatsCallSetupCACBandwidthFailure_Object = MibTableColumn
csbCurrPeriodicStatsCallSetupCACBandwidthFailure = _CsbCurrPeriodicStatsCallSetupCACBandwidthFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 19),
    _CsbCurrPeriodicStatsCallSetupCACBandwidthFailure_Type()
)
csbCurrPeriodicStatsCallSetupCACBandwidthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCallSetupCACBandwidthFailure.setStatus("current")
_CsbCurrPeriodicStatsCallSetupCACMediaLimitFailure_Type = Gauge32
_CsbCurrPeriodicStatsCallSetupCACMediaLimitFailure_Object = MibTableColumn
csbCurrPeriodicStatsCallSetupCACMediaLimitFailure = _CsbCurrPeriodicStatsCallSetupCACMediaLimitFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 20),
    _CsbCurrPeriodicStatsCallSetupCACMediaLimitFailure_Type()
)
csbCurrPeriodicStatsCallSetupCACMediaLimitFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCallSetupCACMediaLimitFailure.setStatus("current")
_CsbCurrPeriodicStatsCallSetupCACMediaUpdateFailure_Type = Gauge32
_CsbCurrPeriodicStatsCallSetupCACMediaUpdateFailure_Object = MibTableColumn
csbCurrPeriodicStatsCallSetupCACMediaUpdateFailure = _CsbCurrPeriodicStatsCallSetupCACMediaUpdateFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 21),
    _CsbCurrPeriodicStatsCallSetupCACMediaUpdateFailure_Type()
)
csbCurrPeriodicStatsCallSetupCACMediaUpdateFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCallSetupCACMediaUpdateFailure.setStatus("current")


class _CsbCurrPeriodicStatsTimestamp_Type(OctetString):
    """Custom type csbCurrPeriodicStatsTimestamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CsbCurrPeriodicStatsTimestamp_Type.__name__ = "OctetString"
_CsbCurrPeriodicStatsTimestamp_Object = MibTableColumn
csbCurrPeriodicStatsTimestamp = _CsbCurrPeriodicStatsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 22),
    _CsbCurrPeriodicStatsTimestamp_Type()
)
csbCurrPeriodicStatsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsTimestamp.setStatus("current")
_CsbCurrPeriodicStatsTranscodedCalls_Type = Gauge32
_CsbCurrPeriodicStatsTranscodedCalls_Object = MibTableColumn
csbCurrPeriodicStatsTranscodedCalls = _CsbCurrPeriodicStatsTranscodedCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 23),
    _CsbCurrPeriodicStatsTranscodedCalls_Type()
)
csbCurrPeriodicStatsTranscodedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsTranscodedCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsTranscodedCalls.setUnits("calls")
_CsbCurrPeriodicStatsTransratedCalls_Type = Gauge32
_CsbCurrPeriodicStatsTransratedCalls_Object = MibTableColumn
csbCurrPeriodicStatsTransratedCalls = _CsbCurrPeriodicStatsTransratedCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 24),
    _CsbCurrPeriodicStatsTransratedCalls_Type()
)
csbCurrPeriodicStatsTransratedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsTransratedCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsTransratedCalls.setUnits("calls")
_CsbCurrPeriodicStatsTotalCallUpdateFailure_Type = Gauge32
_CsbCurrPeriodicStatsTotalCallUpdateFailure_Object = MibTableColumn
csbCurrPeriodicStatsTotalCallUpdateFailure = _CsbCurrPeriodicStatsTotalCallUpdateFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 25),
    _CsbCurrPeriodicStatsTotalCallUpdateFailure_Type()
)
csbCurrPeriodicStatsTotalCallUpdateFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsTotalCallUpdateFailure.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsTotalCallUpdateFailure.setUnits("calls")
_CsbCurrPeriodicStatsActiveIpv6Calls_Type = Gauge32
_CsbCurrPeriodicStatsActiveIpv6Calls_Object = MibTableColumn
csbCurrPeriodicStatsActiveIpv6Calls = _CsbCurrPeriodicStatsActiveIpv6Calls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 26),
    _CsbCurrPeriodicStatsActiveIpv6Calls_Type()
)
csbCurrPeriodicStatsActiveIpv6Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsActiveIpv6Calls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsActiveIpv6Calls.setUnits("calls")
_CsbCurrPeriodicStatsActiveEmergencyCalls_Type = Gauge32
_CsbCurrPeriodicStatsActiveEmergencyCalls_Object = MibTableColumn
csbCurrPeriodicStatsActiveEmergencyCalls = _CsbCurrPeriodicStatsActiveEmergencyCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 27),
    _CsbCurrPeriodicStatsActiveEmergencyCalls_Type()
)
csbCurrPeriodicStatsActiveEmergencyCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsActiveEmergencyCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsActiveEmergencyCalls.setUnits("calls")
_CsbCurrPeriodicStatsActiveE2EmergencyCalls_Type = Gauge32
_CsbCurrPeriodicStatsActiveE2EmergencyCalls_Object = MibTableColumn
csbCurrPeriodicStatsActiveE2EmergencyCalls = _CsbCurrPeriodicStatsActiveE2EmergencyCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 28),
    _CsbCurrPeriodicStatsActiveE2EmergencyCalls_Type()
)
csbCurrPeriodicStatsActiveE2EmergencyCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsActiveE2EmergencyCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsActiveE2EmergencyCalls.setUnits("calls")
_CsbCurrPeriodicStatsImsRxActiveCalls_Type = Gauge32
_CsbCurrPeriodicStatsImsRxActiveCalls_Object = MibTableColumn
csbCurrPeriodicStatsImsRxActiveCalls = _CsbCurrPeriodicStatsImsRxActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 29),
    _CsbCurrPeriodicStatsImsRxActiveCalls_Type()
)
csbCurrPeriodicStatsImsRxActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsImsRxActiveCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsImsRxActiveCalls.setUnits("calls")
_CsbCurrPeriodicStatsImsRxCallSetupFaiures_Type = Gauge32
_CsbCurrPeriodicStatsImsRxCallSetupFaiures_Object = MibTableColumn
csbCurrPeriodicStatsImsRxCallSetupFaiures = _CsbCurrPeriodicStatsImsRxCallSetupFaiures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 30),
    _CsbCurrPeriodicStatsImsRxCallSetupFaiures_Type()
)
csbCurrPeriodicStatsImsRxCallSetupFaiures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsImsRxCallSetupFaiures.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsImsRxCallSetupFaiures.setUnits("failures")
_CsbCurrPeriodicStatsImsRxCallRenegotiationAttempts_Type = Gauge32
_CsbCurrPeriodicStatsImsRxCallRenegotiationAttempts_Object = MibTableColumn
csbCurrPeriodicStatsImsRxCallRenegotiationAttempts = _CsbCurrPeriodicStatsImsRxCallRenegotiationAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 31),
    _CsbCurrPeriodicStatsImsRxCallRenegotiationAttempts_Type()
)
csbCurrPeriodicStatsImsRxCallRenegotiationAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsImsRxCallRenegotiationAttempts.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsImsRxCallRenegotiationAttempts.setUnits("attempts")
_CsbCurrPeriodicStatsImsRxCallRenegotiationFailures_Type = Gauge32
_CsbCurrPeriodicStatsImsRxCallRenegotiationFailures_Object = MibTableColumn
csbCurrPeriodicStatsImsRxCallRenegotiationFailures = _CsbCurrPeriodicStatsImsRxCallRenegotiationFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 32),
    _CsbCurrPeriodicStatsImsRxCallRenegotiationFailures_Type()
)
csbCurrPeriodicStatsImsRxCallRenegotiationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsImsRxCallRenegotiationFailures.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsImsRxCallRenegotiationFailures.setUnits("failures")
_CsbCurrPeriodicStatsAudioTranscodedCalls_Type = Gauge32
_CsbCurrPeriodicStatsAudioTranscodedCalls_Object = MibTableColumn
csbCurrPeriodicStatsAudioTranscodedCalls = _CsbCurrPeriodicStatsAudioTranscodedCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 33),
    _CsbCurrPeriodicStatsAudioTranscodedCalls_Type()
)
csbCurrPeriodicStatsAudioTranscodedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsAudioTranscodedCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsAudioTranscodedCalls.setUnits("calls")
_CsbCurrPeriodicStatsFaxTranscodedCalls_Type = Gauge32
_CsbCurrPeriodicStatsFaxTranscodedCalls_Object = MibTableColumn
csbCurrPeriodicStatsFaxTranscodedCalls = _CsbCurrPeriodicStatsFaxTranscodedCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 34),
    _CsbCurrPeriodicStatsFaxTranscodedCalls_Type()
)
csbCurrPeriodicStatsFaxTranscodedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsFaxTranscodedCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsFaxTranscodedCalls.setUnits("calls")
_CsbCurrPeriodicStatsRtpDisallowedFailures_Type = Gauge32
_CsbCurrPeriodicStatsRtpDisallowedFailures_Object = MibTableColumn
csbCurrPeriodicStatsRtpDisallowedFailures = _CsbCurrPeriodicStatsRtpDisallowedFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 35),
    _CsbCurrPeriodicStatsRtpDisallowedFailures_Type()
)
csbCurrPeriodicStatsRtpDisallowedFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsRtpDisallowedFailures.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsRtpDisallowedFailures.setUnits("failures")
_CsbCurrPeriodicStatsSrtpDisallowedFailures_Type = Gauge32
_CsbCurrPeriodicStatsSrtpDisallowedFailures_Object = MibTableColumn
csbCurrPeriodicStatsSrtpDisallowedFailures = _CsbCurrPeriodicStatsSrtpDisallowedFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 36),
    _CsbCurrPeriodicStatsSrtpDisallowedFailures_Type()
)
csbCurrPeriodicStatsSrtpDisallowedFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsSrtpDisallowedFailures.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsSrtpDisallowedFailures.setUnits("failures")
_CsbCurrPeriodicStatsNonSrtpCalls_Type = Gauge32
_CsbCurrPeriodicStatsNonSrtpCalls_Object = MibTableColumn
csbCurrPeriodicStatsNonSrtpCalls = _CsbCurrPeriodicStatsNonSrtpCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 37),
    _CsbCurrPeriodicStatsNonSrtpCalls_Type()
)
csbCurrPeriodicStatsNonSrtpCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsNonSrtpCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsNonSrtpCalls.setUnits("calls")
_CsbCurrPeriodicStatsSrtpNonIwCalls_Type = Gauge32
_CsbCurrPeriodicStatsSrtpNonIwCalls_Object = MibTableColumn
csbCurrPeriodicStatsSrtpNonIwCalls = _CsbCurrPeriodicStatsSrtpNonIwCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 38),
    _CsbCurrPeriodicStatsSrtpNonIwCalls_Type()
)
csbCurrPeriodicStatsSrtpNonIwCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsSrtpNonIwCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsSrtpNonIwCalls.setUnits("calls")
_CsbCurrPeriodicStatsSrtpIwCalls_Type = Gauge32
_CsbCurrPeriodicStatsSrtpIwCalls_Object = MibTableColumn
csbCurrPeriodicStatsSrtpIwCalls = _CsbCurrPeriodicStatsSrtpIwCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 39),
    _CsbCurrPeriodicStatsSrtpIwCalls_Type()
)
csbCurrPeriodicStatsSrtpIwCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsSrtpIwCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsSrtpIwCalls.setUnits("calls")
_CsbCurrPeriodicStatsDtmfIw2833Calls_Type = Gauge32
_CsbCurrPeriodicStatsDtmfIw2833Calls_Object = MibTableColumn
csbCurrPeriodicStatsDtmfIw2833Calls = _CsbCurrPeriodicStatsDtmfIw2833Calls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 40),
    _CsbCurrPeriodicStatsDtmfIw2833Calls_Type()
)
csbCurrPeriodicStatsDtmfIw2833Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsDtmfIw2833Calls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsDtmfIw2833Calls.setUnits("calls")
_CsbCurrPeriodicStatsDtmfIwInbandCalls_Type = Gauge32
_CsbCurrPeriodicStatsDtmfIwInbandCalls_Object = MibTableColumn
csbCurrPeriodicStatsDtmfIwInbandCalls = _CsbCurrPeriodicStatsDtmfIwInbandCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 41),
    _CsbCurrPeriodicStatsDtmfIwInbandCalls_Type()
)
csbCurrPeriodicStatsDtmfIwInbandCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsDtmfIwInbandCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsDtmfIwInbandCalls.setUnits("calls")
_CsbCurrPeriodicStatsDtmfIw2833InbandCalls_Type = Gauge32
_CsbCurrPeriodicStatsDtmfIw2833InbandCalls_Object = MibTableColumn
csbCurrPeriodicStatsDtmfIw2833InbandCalls = _CsbCurrPeriodicStatsDtmfIw2833InbandCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 42),
    _CsbCurrPeriodicStatsDtmfIw2833InbandCalls_Type()
)
csbCurrPeriodicStatsDtmfIw2833InbandCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsDtmfIw2833InbandCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsDtmfIw2833InbandCalls.setUnits("calls")
_CsbCurrPeriodicStatsTotalTapsRequested_Type = Gauge32
_CsbCurrPeriodicStatsTotalTapsRequested_Object = MibTableColumn
csbCurrPeriodicStatsTotalTapsRequested = _CsbCurrPeriodicStatsTotalTapsRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 43),
    _CsbCurrPeriodicStatsTotalTapsRequested_Type()
)
csbCurrPeriodicStatsTotalTapsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsTotalTapsRequested.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsTotalTapsRequested.setUnits("attempts")
_CsbCurrPeriodicStatsTotalTapsSucceeded_Type = Gauge32
_CsbCurrPeriodicStatsTotalTapsSucceeded_Object = MibTableColumn
csbCurrPeriodicStatsTotalTapsSucceeded = _CsbCurrPeriodicStatsTotalTapsSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 44),
    _CsbCurrPeriodicStatsTotalTapsSucceeded_Type()
)
csbCurrPeriodicStatsTotalTapsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsTotalTapsSucceeded.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsTotalTapsSucceeded.setUnits("success")
_CsbCurrPeriodicStatsCurrentTaps_Type = Gauge32
_CsbCurrPeriodicStatsCurrentTaps_Object = MibTableColumn
csbCurrPeriodicStatsCurrentTaps = _CsbCurrPeriodicStatsCurrentTaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 45),
    _CsbCurrPeriodicStatsCurrentTaps_Type()
)
csbCurrPeriodicStatsCurrentTaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCurrentTaps.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsCurrentTaps.setUnits("taps")
_CsbCurrPeriodicIpsecCalls_Type = Gauge32
_CsbCurrPeriodicIpsecCalls_Object = MibTableColumn
csbCurrPeriodicIpsecCalls = _CsbCurrPeriodicIpsecCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 3, 1, 46),
    _CsbCurrPeriodicIpsecCalls_Type()
)
csbCurrPeriodicIpsecCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbCurrPeriodicIpsecCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbCurrPeriodicIpsecCalls.setUnits("calls")
_CsbHistoryStatsTable_Object = MibTable
csbHistoryStatsTable = _CsbHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4)
)
if mibBuilder.loadTexts:
    csbHistoryStatsTable.setStatus("current")
_CsbHistoryStatsEntry_Object = MibTableRow
csbHistoryStatsEntry = _CsbHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1)
)
csbHistoryStatsEntry.setIndexNames(
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsInstanceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsServiceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsInterval"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsElements"),
)
if mibBuilder.loadTexts:
    csbHistoryStatsEntry.setStatus("current")
_CsbHistoryStatsInterval_Type = CiscoSbcPeriodicStatsInterval
_CsbHistoryStatsInterval_Object = MibTableColumn
csbHistoryStatsInterval = _CsbHistoryStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 1),
    _CsbHistoryStatsInterval_Type()
)
csbHistoryStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbHistoryStatsInterval.setStatus("current")
_CsbHistoryStatsElements_Type = Unsigned32
_CsbHistoryStatsElements_Object = MibTableColumn
csbHistoryStatsElements = _CsbHistoryStatsElements_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 2),
    _CsbHistoryStatsElements_Type()
)
csbHistoryStatsElements.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbHistoryStatsElements.setStatus("current")
_CsbHistoryStatsActiveCalls_Type = Gauge32
_CsbHistoryStatsActiveCalls_Object = MibTableColumn
csbHistoryStatsActiveCalls = _CsbHistoryStatsActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 3),
    _CsbHistoryStatsActiveCalls_Type()
)
csbHistoryStatsActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsActiveCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsActiveCalls.setUnits("calls")
_CsbHistoryStatsTotalCallAttempts_Type = Gauge32
_CsbHistoryStatsTotalCallAttempts_Object = MibTableColumn
csbHistoryStatsTotalCallAttempts = _CsbHistoryStatsTotalCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 4),
    _CsbHistoryStatsTotalCallAttempts_Type()
)
csbHistoryStatsTotalCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsTotalCallAttempts.setStatus("current")
_CsbHistoryStatsFailedCallAttempts_Type = Gauge32
_CsbHistoryStatsFailedCallAttempts_Object = MibTableColumn
csbHistoryStatsFailedCallAttempts = _CsbHistoryStatsFailedCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 5),
    _CsbHistoryStatsFailedCallAttempts_Type()
)
csbHistoryStatsFailedCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsFailedCallAttempts.setStatus("current")
_CsbHistoryStatsCallRoutingFailure_Type = Gauge32
_CsbHistoryStatsCallRoutingFailure_Object = MibTableColumn
csbHistoryStatsCallRoutingFailure = _CsbHistoryStatsCallRoutingFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 6),
    _CsbHistoryStatsCallRoutingFailure_Type()
)
csbHistoryStatsCallRoutingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsCallRoutingFailure.setStatus("current")
_CsbHistoryStatsCallResourceFailure_Type = Gauge32
_CsbHistoryStatsCallResourceFailure_Object = MibTableColumn
csbHistoryStatsCallResourceFailure = _CsbHistoryStatsCallResourceFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 7),
    _CsbHistoryStatsCallResourceFailure_Type()
)
csbHistoryStatsCallResourceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsCallResourceFailure.setStatus("current")
_CsbHistoryStatsCallMediaFailure_Type = Gauge32
_CsbHistoryStatsCallMediaFailure_Object = MibTableColumn
csbHistoryStatsCallMediaFailure = _CsbHistoryStatsCallMediaFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 8),
    _CsbHistoryStatsCallMediaFailure_Type()
)
csbHistoryStatsCallMediaFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsCallMediaFailure.setStatus("current")
_CsbHistoryStatsFailSigFailure_Type = Gauge32
_CsbHistoryStatsFailSigFailure_Object = MibTableColumn
csbHistoryStatsFailSigFailure = _CsbHistoryStatsFailSigFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 9),
    _CsbHistoryStatsFailSigFailure_Type()
)
csbHistoryStatsFailSigFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsFailSigFailure.setStatus("current")
_CsbHistoryStatsActiveCallFailure_Type = Gauge32
_CsbHistoryStatsActiveCallFailure_Object = MibTableColumn
csbHistoryStatsActiveCallFailure = _CsbHistoryStatsActiveCallFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 10),
    _CsbHistoryStatsActiveCallFailure_Type()
)
csbHistoryStatsActiveCallFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsActiveCallFailure.setStatus("current")
_CsbHistoryStatsCongestionFailure_Type = Gauge32
_CsbHistoryStatsCongestionFailure_Object = MibTableColumn
csbHistoryStatsCongestionFailure = _CsbHistoryStatsCongestionFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 11),
    _CsbHistoryStatsCongestionFailure_Type()
)
csbHistoryStatsCongestionFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsCongestionFailure.setStatus("current")
_CsbHistoryStatsCallSetupPolicyFailure_Type = Gauge32
_CsbHistoryStatsCallSetupPolicyFailure_Object = MibTableColumn
csbHistoryStatsCallSetupPolicyFailure = _CsbHistoryStatsCallSetupPolicyFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 12),
    _CsbHistoryStatsCallSetupPolicyFailure_Type()
)
csbHistoryStatsCallSetupPolicyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsCallSetupPolicyFailure.setStatus("current")
_CsbHistoryStatsCallSetupNAPolicyFailure_Type = Gauge32
_CsbHistoryStatsCallSetupNAPolicyFailure_Object = MibTableColumn
csbHistoryStatsCallSetupNAPolicyFailure = _CsbHistoryStatsCallSetupNAPolicyFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 13),
    _CsbHistoryStatsCallSetupNAPolicyFailure_Type()
)
csbHistoryStatsCallSetupNAPolicyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsCallSetupNAPolicyFailure.setStatus("current")
_CsbHistoryStatsCallSetupRoutingPolicyFailure_Type = Gauge32
_CsbHistoryStatsCallSetupRoutingPolicyFailure_Object = MibTableColumn
csbHistoryStatsCallSetupRoutingPolicyFailure = _CsbHistoryStatsCallSetupRoutingPolicyFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 14),
    _CsbHistoryStatsCallSetupRoutingPolicyFailure_Type()
)
csbHistoryStatsCallSetupRoutingPolicyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsCallSetupRoutingPolicyFailure.setStatus("current")
_CsbHistoryStatsCallSetupCACPolicyFailure_Type = Gauge32
_CsbHistoryStatsCallSetupCACPolicyFailure_Object = MibTableColumn
csbHistoryStatsCallSetupCACPolicyFailure = _CsbHistoryStatsCallSetupCACPolicyFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 15),
    _CsbHistoryStatsCallSetupCACPolicyFailure_Type()
)
csbHistoryStatsCallSetupCACPolicyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsCallSetupCACPolicyFailure.setStatus("current")
_CsbHistoryStatsCallSetupCACCallLimitFailure_Type = Gauge32
_CsbHistoryStatsCallSetupCACCallLimitFailure_Object = MibTableColumn
csbHistoryStatsCallSetupCACCallLimitFailure = _CsbHistoryStatsCallSetupCACCallLimitFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 16),
    _CsbHistoryStatsCallSetupCACCallLimitFailure_Type()
)
csbHistoryStatsCallSetupCACCallLimitFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsCallSetupCACCallLimitFailure.setStatus("current")
_CsbHistoryStatsCallSetupCACRateLimitFailure_Type = Gauge32
_CsbHistoryStatsCallSetupCACRateLimitFailure_Object = MibTableColumn
csbHistoryStatsCallSetupCACRateLimitFailure = _CsbHistoryStatsCallSetupCACRateLimitFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 17),
    _CsbHistoryStatsCallSetupCACRateLimitFailure_Type()
)
csbHistoryStatsCallSetupCACRateLimitFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsCallSetupCACRateLimitFailure.setStatus("current")
_CsbHistoryStatsCallSetupCACBandwidthFailure_Type = Gauge32
_CsbHistoryStatsCallSetupCACBandwidthFailure_Object = MibTableColumn
csbHistoryStatsCallSetupCACBandwidthFailure = _CsbHistoryStatsCallSetupCACBandwidthFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 18),
    _CsbHistoryStatsCallSetupCACBandwidthFailure_Type()
)
csbHistoryStatsCallSetupCACBandwidthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsCallSetupCACBandwidthFailure.setStatus("current")
_CsbHistoryStatsCallSetupCACMediaLimitFailure_Type = Gauge32
_CsbHistoryStatsCallSetupCACMediaLimitFailure_Object = MibTableColumn
csbHistoryStatsCallSetupCACMediaLimitFailure = _CsbHistoryStatsCallSetupCACMediaLimitFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 19),
    _CsbHistoryStatsCallSetupCACMediaLimitFailure_Type()
)
csbHistoryStatsCallSetupCACMediaLimitFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsCallSetupCACMediaLimitFailure.setStatus("current")
_CsbHistoryStatsCallSetupCACMediaUpdateFailure_Type = Gauge32
_CsbHistoryStatsCallSetupCACMediaUpdateFailure_Object = MibTableColumn
csbHistoryStatsCallSetupCACMediaUpdateFailure = _CsbHistoryStatsCallSetupCACMediaUpdateFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 20),
    _CsbHistoryStatsCallSetupCACMediaUpdateFailure_Type()
)
csbHistoryStatsCallSetupCACMediaUpdateFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsCallSetupCACMediaUpdateFailure.setStatus("current")


class _CsbHistoryStatsTimestamp_Type(OctetString):
    """Custom type csbHistoryStatsTimestamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CsbHistoryStatsTimestamp_Type.__name__ = "OctetString"
_CsbHistoryStatsTimestamp_Object = MibTableColumn
csbHistoryStatsTimestamp = _CsbHistoryStatsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 21),
    _CsbHistoryStatsTimestamp_Type()
)
csbHistoryStatsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsTimestamp.setStatus("current")
_CsbHistroyStatsTranscodedCalls_Type = Gauge32
_CsbHistroyStatsTranscodedCalls_Object = MibTableColumn
csbHistroyStatsTranscodedCalls = _CsbHistroyStatsTranscodedCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 22),
    _CsbHistroyStatsTranscodedCalls_Type()
)
csbHistroyStatsTranscodedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistroyStatsTranscodedCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistroyStatsTranscodedCalls.setUnits("calls")
_CsbHistroyStatsTransratedCalls_Type = Gauge32
_CsbHistroyStatsTransratedCalls_Object = MibTableColumn
csbHistroyStatsTransratedCalls = _CsbHistroyStatsTransratedCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 23),
    _CsbHistroyStatsTransratedCalls_Type()
)
csbHistroyStatsTransratedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistroyStatsTransratedCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistroyStatsTransratedCalls.setUnits("calls")
_CsbHistoryStatsTotalCallUpdateFailure_Type = Gauge32
_CsbHistoryStatsTotalCallUpdateFailure_Object = MibTableColumn
csbHistoryStatsTotalCallUpdateFailure = _CsbHistoryStatsTotalCallUpdateFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 24),
    _CsbHistoryStatsTotalCallUpdateFailure_Type()
)
csbHistoryStatsTotalCallUpdateFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsTotalCallUpdateFailure.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsTotalCallUpdateFailure.setUnits("calls")
_CsbHistoryStatsActiveIpv6Calls_Type = Gauge32
_CsbHistoryStatsActiveIpv6Calls_Object = MibTableColumn
csbHistoryStatsActiveIpv6Calls = _CsbHistoryStatsActiveIpv6Calls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 25),
    _CsbHistoryStatsActiveIpv6Calls_Type()
)
csbHistoryStatsActiveIpv6Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsActiveIpv6Calls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsActiveIpv6Calls.setUnits("calls")
_CsbHistoryStatsActiveEmergencyCalls_Type = Gauge32
_CsbHistoryStatsActiveEmergencyCalls_Object = MibTableColumn
csbHistoryStatsActiveEmergencyCalls = _CsbHistoryStatsActiveEmergencyCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 26),
    _CsbHistoryStatsActiveEmergencyCalls_Type()
)
csbHistoryStatsActiveEmergencyCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsActiveEmergencyCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsActiveEmergencyCalls.setUnits("calls")
_CsbHistoryStatsActiveE2EmergencyCalls_Type = Gauge32
_CsbHistoryStatsActiveE2EmergencyCalls_Object = MibTableColumn
csbHistoryStatsActiveE2EmergencyCalls = _CsbHistoryStatsActiveE2EmergencyCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 27),
    _CsbHistoryStatsActiveE2EmergencyCalls_Type()
)
csbHistoryStatsActiveE2EmergencyCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsActiveE2EmergencyCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsActiveE2EmergencyCalls.setUnits("calls")
_CsbHistoryStatsImsRxActiveCalls_Type = Gauge32
_CsbHistoryStatsImsRxActiveCalls_Object = MibTableColumn
csbHistoryStatsImsRxActiveCalls = _CsbHistoryStatsImsRxActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 28),
    _CsbHistoryStatsImsRxActiveCalls_Type()
)
csbHistoryStatsImsRxActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsImsRxActiveCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsImsRxActiveCalls.setUnits("calls")
_CsbHistoryStatsImsRxCallSetupFailures_Type = Gauge32
_CsbHistoryStatsImsRxCallSetupFailures_Object = MibTableColumn
csbHistoryStatsImsRxCallSetupFailures = _CsbHistoryStatsImsRxCallSetupFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 29),
    _CsbHistoryStatsImsRxCallSetupFailures_Type()
)
csbHistoryStatsImsRxCallSetupFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsImsRxCallSetupFailures.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsImsRxCallSetupFailures.setUnits("failures")
_CsbHistoryStatsImsRxCallRenegotiationAttempts_Type = Gauge32
_CsbHistoryStatsImsRxCallRenegotiationAttempts_Object = MibTableColumn
csbHistoryStatsImsRxCallRenegotiationAttempts = _CsbHistoryStatsImsRxCallRenegotiationAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 30),
    _CsbHistoryStatsImsRxCallRenegotiationAttempts_Type()
)
csbHistoryStatsImsRxCallRenegotiationAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsImsRxCallRenegotiationAttempts.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsImsRxCallRenegotiationAttempts.setUnits("attempts")
_CsbHistoryStatsImsRxCallRenegotiationFailures_Type = Gauge32
_CsbHistoryStatsImsRxCallRenegotiationFailures_Object = MibTableColumn
csbHistoryStatsImsRxCallRenegotiationFailures = _CsbHistoryStatsImsRxCallRenegotiationFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 31),
    _CsbHistoryStatsImsRxCallRenegotiationFailures_Type()
)
csbHistoryStatsImsRxCallRenegotiationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsImsRxCallRenegotiationFailures.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsImsRxCallRenegotiationFailures.setUnits("failures")
_CsbHistoryStatsAudioTranscodedCalls_Type = Gauge32
_CsbHistoryStatsAudioTranscodedCalls_Object = MibTableColumn
csbHistoryStatsAudioTranscodedCalls = _CsbHistoryStatsAudioTranscodedCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 32),
    _CsbHistoryStatsAudioTranscodedCalls_Type()
)
csbHistoryStatsAudioTranscodedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsAudioTranscodedCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsAudioTranscodedCalls.setUnits("calls")
_CsbHistoryStatsFaxTranscodedCalls_Type = Gauge32
_CsbHistoryStatsFaxTranscodedCalls_Object = MibTableColumn
csbHistoryStatsFaxTranscodedCalls = _CsbHistoryStatsFaxTranscodedCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 33),
    _CsbHistoryStatsFaxTranscodedCalls_Type()
)
csbHistoryStatsFaxTranscodedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsFaxTranscodedCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsFaxTranscodedCalls.setUnits("calls")
_CsbHistoryStatsRtpDisallowedFailures_Type = Gauge32
_CsbHistoryStatsRtpDisallowedFailures_Object = MibTableColumn
csbHistoryStatsRtpDisallowedFailures = _CsbHistoryStatsRtpDisallowedFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 34),
    _CsbHistoryStatsRtpDisallowedFailures_Type()
)
csbHistoryStatsRtpDisallowedFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsRtpDisallowedFailures.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsRtpDisallowedFailures.setUnits("failures")
_CsbHistoryStatsSrtpDisallowedFailures_Type = Gauge32
_CsbHistoryStatsSrtpDisallowedFailures_Object = MibTableColumn
csbHistoryStatsSrtpDisallowedFailures = _CsbHistoryStatsSrtpDisallowedFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 35),
    _CsbHistoryStatsSrtpDisallowedFailures_Type()
)
csbHistoryStatsSrtpDisallowedFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsSrtpDisallowedFailures.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsSrtpDisallowedFailures.setUnits("failures")
_CsbHistoryStatsNonSrtpCalls_Type = Gauge32
_CsbHistoryStatsNonSrtpCalls_Object = MibTableColumn
csbHistoryStatsNonSrtpCalls = _CsbHistoryStatsNonSrtpCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 36),
    _CsbHistoryStatsNonSrtpCalls_Type()
)
csbHistoryStatsNonSrtpCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsNonSrtpCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsNonSrtpCalls.setUnits("calls")
_CsbHistoryStatsSrtpNonIwCalls_Type = Gauge32
_CsbHistoryStatsSrtpNonIwCalls_Object = MibTableColumn
csbHistoryStatsSrtpNonIwCalls = _CsbHistoryStatsSrtpNonIwCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 37),
    _CsbHistoryStatsSrtpNonIwCalls_Type()
)
csbHistoryStatsSrtpNonIwCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsSrtpNonIwCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsSrtpNonIwCalls.setUnits("calls")
_CsbHistoryStatsSrtpIwCalls_Type = Gauge32
_CsbHistoryStatsSrtpIwCalls_Object = MibTableColumn
csbHistoryStatsSrtpIwCalls = _CsbHistoryStatsSrtpIwCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 38),
    _CsbHistoryStatsSrtpIwCalls_Type()
)
csbHistoryStatsSrtpIwCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsSrtpIwCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsSrtpIwCalls.setUnits("calls")
_CsbHistoryStatsDtmfIw2833Calls_Type = Gauge32
_CsbHistoryStatsDtmfIw2833Calls_Object = MibTableColumn
csbHistoryStatsDtmfIw2833Calls = _CsbHistoryStatsDtmfIw2833Calls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 39),
    _CsbHistoryStatsDtmfIw2833Calls_Type()
)
csbHistoryStatsDtmfIw2833Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsDtmfIw2833Calls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsDtmfIw2833Calls.setUnits("calls")
_CsbHistoryStatsDtmfIwInbandCalls_Type = Gauge32
_CsbHistoryStatsDtmfIwInbandCalls_Object = MibTableColumn
csbHistoryStatsDtmfIwInbandCalls = _CsbHistoryStatsDtmfIwInbandCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 40),
    _CsbHistoryStatsDtmfIwInbandCalls_Type()
)
csbHistoryStatsDtmfIwInbandCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsDtmfIwInbandCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsDtmfIwInbandCalls.setUnits("calls")
_CsbHistoryStatsDtmfIw2833InbandCalls_Type = Gauge32
_CsbHistoryStatsDtmfIw2833InbandCalls_Object = MibTableColumn
csbHistoryStatsDtmfIw2833InbandCalls = _CsbHistoryStatsDtmfIw2833InbandCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 41),
    _CsbHistoryStatsDtmfIw2833InbandCalls_Type()
)
csbHistoryStatsDtmfIw2833InbandCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsDtmfIw2833InbandCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsDtmfIw2833InbandCalls.setUnits("calls")
_CsbHistoryStatsTotalTapsRequested_Type = Gauge32
_CsbHistoryStatsTotalTapsRequested_Object = MibTableColumn
csbHistoryStatsTotalTapsRequested = _CsbHistoryStatsTotalTapsRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 42),
    _CsbHistoryStatsTotalTapsRequested_Type()
)
csbHistoryStatsTotalTapsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsTotalTapsRequested.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsTotalTapsRequested.setUnits("attempts")
_CsbHistoryStatsTotalTapsSucceeded_Type = Gauge32
_CsbHistoryStatsTotalTapsSucceeded_Object = MibTableColumn
csbHistoryStatsTotalTapsSucceeded = _CsbHistoryStatsTotalTapsSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 43),
    _CsbHistoryStatsTotalTapsSucceeded_Type()
)
csbHistoryStatsTotalTapsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsTotalTapsSucceeded.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsTotalTapsSucceeded.setUnits("success")
_CsbHistoryStatsCurrentTaps_Type = Gauge32
_CsbHistoryStatsCurrentTaps_Object = MibTableColumn
csbHistoryStatsCurrentTaps = _CsbHistoryStatsCurrentTaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 44),
    _CsbHistoryStatsCurrentTaps_Type()
)
csbHistoryStatsCurrentTaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsCurrentTaps.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsCurrentTaps.setUnits("taps")
_CsbHistoryStatsIpsecCalls_Type = Gauge32
_CsbHistoryStatsIpsecCalls_Object = MibTableColumn
csbHistoryStatsIpsecCalls = _CsbHistoryStatsIpsecCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 4, 1, 45),
    _CsbHistoryStatsIpsecCalls_Type()
)
csbHistoryStatsIpsecCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbHistoryStatsIpsecCalls.setStatus("current")
if mibBuilder.loadTexts:
    csbHistoryStatsIpsecCalls.setUnits("calls")
_CsbPerFlowStatsTable_Object = MibTable
csbPerFlowStatsTable = _CsbPerFlowStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5)
)
if mibBuilder.loadTexts:
    csbPerFlowStatsTable.setStatus("current")
_CsbPerFlowStatsEntry_Object = MibTableRow
csbPerFlowStatsEntry = _CsbPerFlowStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1)
)
csbPerFlowStatsEntry.setIndexNames(
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsInstanceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsServiceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsVdbeId"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsGateId"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsFlowPairId"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsSideId"),
)
if mibBuilder.loadTexts:
    csbPerFlowStatsEntry.setStatus("current")


class _CsbPerFlowStatsVdbeId_Type(Integer32):
    """Custom type csbPerFlowStatsVdbeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CsbPerFlowStatsVdbeId_Type.__name__ = "Integer32"
_CsbPerFlowStatsVdbeId_Object = MibTableColumn
csbPerFlowStatsVdbeId = _CsbPerFlowStatsVdbeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 1),
    _CsbPerFlowStatsVdbeId_Type()
)
csbPerFlowStatsVdbeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbPerFlowStatsVdbeId.setStatus("current")


class _CsbPerFlowStatsGateId_Type(Integer32):
    """Custom type csbPerFlowStatsGateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CsbPerFlowStatsGateId_Type.__name__ = "Integer32"
_CsbPerFlowStatsGateId_Object = MibTableColumn
csbPerFlowStatsGateId = _CsbPerFlowStatsGateId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 2),
    _CsbPerFlowStatsGateId_Type()
)
csbPerFlowStatsGateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbPerFlowStatsGateId.setStatus("current")


class _CsbPerFlowStatsFlowPairId_Type(Integer32):
    """Custom type csbPerFlowStatsFlowPairId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CsbPerFlowStatsFlowPairId_Type.__name__ = "Integer32"
_CsbPerFlowStatsFlowPairId_Object = MibTableColumn
csbPerFlowStatsFlowPairId = _CsbPerFlowStatsFlowPairId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 3),
    _CsbPerFlowStatsFlowPairId_Type()
)
csbPerFlowStatsFlowPairId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbPerFlowStatsFlowPairId.setStatus("current")


class _CsbPerFlowStatsSideId_Type(Integer32):
    """Custom type csbPerFlowStatsSideId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sideA", 1),
          ("sideB", 2))
    )


_CsbPerFlowStatsSideId_Type.__name__ = "Integer32"
_CsbPerFlowStatsSideId_Object = MibTableColumn
csbPerFlowStatsSideId = _CsbPerFlowStatsSideId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 4),
    _CsbPerFlowStatsSideId_Type()
)
csbPerFlowStatsSideId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbPerFlowStatsSideId.setStatus("current")


class _CsbPerFlowStatsFlowType_Type(Integer32):
    """Custom type csbPerFlowStatsFlowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("media", 1),
          ("signalling", 2))
    )


_CsbPerFlowStatsFlowType_Type.__name__ = "Integer32"
_CsbPerFlowStatsFlowType_Object = MibTableColumn
csbPerFlowStatsFlowType = _CsbPerFlowStatsFlowType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 5),
    _CsbPerFlowStatsFlowType_Type()
)
csbPerFlowStatsFlowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsFlowType.setStatus("current")
_CsbPerFlowStatsRTPPktsSent_Type = Counter64
_CsbPerFlowStatsRTPPktsSent_Object = MibTableColumn
csbPerFlowStatsRTPPktsSent = _CsbPerFlowStatsRTPPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 6),
    _CsbPerFlowStatsRTPPktsSent_Type()
)
csbPerFlowStatsRTPPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTPPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTPPktsSent.setUnits("packets")
_CsbPerFlowStatsRTPPktsRcvd_Type = Counter64
_CsbPerFlowStatsRTPPktsRcvd_Object = MibTableColumn
csbPerFlowStatsRTPPktsRcvd = _CsbPerFlowStatsRTPPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 7),
    _CsbPerFlowStatsRTPPktsRcvd_Type()
)
csbPerFlowStatsRTPPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTPPktsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTPPktsRcvd.setUnits("packets")
_CsbPerFlowStatsRTPPktsDiscard_Type = Counter64
_CsbPerFlowStatsRTPPktsDiscard_Object = MibTableColumn
csbPerFlowStatsRTPPktsDiscard = _CsbPerFlowStatsRTPPktsDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 8),
    _CsbPerFlowStatsRTPPktsDiscard_Type()
)
csbPerFlowStatsRTPPktsDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTPPktsDiscard.setStatus("current")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTPPktsDiscard.setUnits("packets")
_CsbPerFlowStatsRTPOctetsSent_Type = Counter64
_CsbPerFlowStatsRTPOctetsSent_Object = MibTableColumn
csbPerFlowStatsRTPOctetsSent = _CsbPerFlowStatsRTPOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 9),
    _CsbPerFlowStatsRTPOctetsSent_Type()
)
csbPerFlowStatsRTPOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTPOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTPOctetsSent.setUnits("octets")
_CsbPerFlowStatsRTPOctetsRcvd_Type = Counter64
_CsbPerFlowStatsRTPOctetsRcvd_Object = MibTableColumn
csbPerFlowStatsRTPOctetsRcvd = _CsbPerFlowStatsRTPOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 10),
    _CsbPerFlowStatsRTPOctetsRcvd_Type()
)
csbPerFlowStatsRTPOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTPOctetsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTPOctetsRcvd.setUnits("octets")
_CsbPerFlowStatsRTPOctetsDiscard_Type = Counter64
_CsbPerFlowStatsRTPOctetsDiscard_Object = MibTableColumn
csbPerFlowStatsRTPOctetsDiscard = _CsbPerFlowStatsRTPOctetsDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 11),
    _CsbPerFlowStatsRTPOctetsDiscard_Type()
)
csbPerFlowStatsRTPOctetsDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTPOctetsDiscard.setStatus("current")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTPOctetsDiscard.setUnits("octets")
_CsbPerFlowStatsRTCPPktsSent_Type = Counter64
_CsbPerFlowStatsRTCPPktsSent_Object = MibTableColumn
csbPerFlowStatsRTCPPktsSent = _CsbPerFlowStatsRTCPPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 12),
    _CsbPerFlowStatsRTCPPktsSent_Type()
)
csbPerFlowStatsRTCPPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTCPPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTCPPktsSent.setUnits("packets")
_CsbPerFlowStatsRTCPPktsRcvd_Type = Counter64
_CsbPerFlowStatsRTCPPktsRcvd_Object = MibTableColumn
csbPerFlowStatsRTCPPktsRcvd = _CsbPerFlowStatsRTCPPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 13),
    _CsbPerFlowStatsRTCPPktsRcvd_Type()
)
csbPerFlowStatsRTCPPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTCPPktsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTCPPktsRcvd.setUnits("packets")
_CsbPerFlowStatsRTCPPktsLost_Type = Counter64
_CsbPerFlowStatsRTCPPktsLost_Object = MibTableColumn
csbPerFlowStatsRTCPPktsLost = _CsbPerFlowStatsRTCPPktsLost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 14),
    _CsbPerFlowStatsRTCPPktsLost_Type()
)
csbPerFlowStatsRTCPPktsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTCPPktsLost.setStatus("current")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTCPPktsLost.setUnits("packets")
_CsbPerFlowStatsEPJitter_Type = Counter64
_CsbPerFlowStatsEPJitter_Object = MibTableColumn
csbPerFlowStatsEPJitter = _CsbPerFlowStatsEPJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 15),
    _CsbPerFlowStatsEPJitter_Type()
)
csbPerFlowStatsEPJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsEPJitter.setStatus("current")
if mibBuilder.loadTexts:
    csbPerFlowStatsEPJitter.setUnits("milliseconds")
_CsbPerFlowStatsTmanPerMbs_Type = Gauge32
_CsbPerFlowStatsTmanPerMbs_Object = MibTableColumn
csbPerFlowStatsTmanPerMbs = _CsbPerFlowStatsTmanPerMbs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 16),
    _CsbPerFlowStatsTmanPerMbs_Type()
)
csbPerFlowStatsTmanPerMbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsTmanPerMbs.setStatus("current")
if mibBuilder.loadTexts:
    csbPerFlowStatsTmanPerMbs.setUnits("bytes")
_CsbPerFlowStatsTmanPerSdr_Type = Gauge32
_CsbPerFlowStatsTmanPerSdr_Object = MibTableColumn
csbPerFlowStatsTmanPerSdr = _CsbPerFlowStatsTmanPerSdr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 17),
    _CsbPerFlowStatsTmanPerSdr_Type()
)
csbPerFlowStatsTmanPerSdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsTmanPerSdr.setStatus("current")
if mibBuilder.loadTexts:
    csbPerFlowStatsTmanPerSdr.setUnits("kilobytes per second")
_CsbPerFlowStatsDscpSettings_Type = SnmpAdminString
_CsbPerFlowStatsDscpSettings_Object = MibTableColumn
csbPerFlowStatsDscpSettings = _CsbPerFlowStatsDscpSettings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 18),
    _CsbPerFlowStatsDscpSettings_Type()
)
csbPerFlowStatsDscpSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsDscpSettings.setStatus("current")


class _CsbPerFlowStatsAdrStatus_Type(OctetString):
    """Custom type csbPerFlowStatsAdrStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CsbPerFlowStatsAdrStatus_Type.__name__ = "OctetString"
_CsbPerFlowStatsAdrStatus_Object = MibTableColumn
csbPerFlowStatsAdrStatus = _CsbPerFlowStatsAdrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 19),
    _CsbPerFlowStatsAdrStatus_Type()
)
csbPerFlowStatsAdrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsAdrStatus.setStatus("current")


class _CsbPerFlowStatsQASettings_Type(OctetString):
    """Custom type csbPerFlowStatsQASettings based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CsbPerFlowStatsQASettings_Type.__name__ = "OctetString"
_CsbPerFlowStatsQASettings_Object = MibTableColumn
csbPerFlowStatsQASettings = _CsbPerFlowStatsQASettings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 20),
    _CsbPerFlowStatsQASettings_Type()
)
csbPerFlowStatsQASettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsQASettings.setStatus("current")
_CsbPerFlowStatsRTPPktsLost_Type = Counter64
_CsbPerFlowStatsRTPPktsLost_Object = MibTableColumn
csbPerFlowStatsRTPPktsLost = _CsbPerFlowStatsRTPPktsLost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 5, 1, 21),
    _CsbPerFlowStatsRTPPktsLost_Type()
)
csbPerFlowStatsRTPPktsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTPPktsLost.setStatus("current")
if mibBuilder.loadTexts:
    csbPerFlowStatsRTPPktsLost.setUnits("packets")
_CsbH248StatsTable_Object = MibTable
csbH248StatsTable = _CsbH248StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6)
)
if mibBuilder.loadTexts:
    csbH248StatsTable.setStatus("deprecated")
_CsbH248StatsEntry_Object = MibTableRow
csbH248StatsEntry = _CsbH248StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1)
)
csbH248StatsEntry.setIndexNames(
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsInstanceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsServiceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsCtrlrIndex"),
)
if mibBuilder.loadTexts:
    csbH248StatsEntry.setStatus("deprecated")


class _CsbH248StatsCtrlrIndex_Type(Integer32):
    """Custom type csbH248StatsCtrlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CsbH248StatsCtrlrIndex_Type.__name__ = "Integer32"
_CsbH248StatsCtrlrIndex_Object = MibTableColumn
csbH248StatsCtrlrIndex = _CsbH248StatsCtrlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1, 1),
    _CsbH248StatsCtrlrIndex_Type()
)
csbH248StatsCtrlrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbH248StatsCtrlrIndex.setStatus("deprecated")
_CsbH248StatsRequestsSent_Type = Counter32
_CsbH248StatsRequestsSent_Object = MibTableColumn
csbH248StatsRequestsSent = _CsbH248StatsRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1, 2),
    _CsbH248StatsRequestsSent_Type()
)
csbH248StatsRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRequestsSent.setStatus("deprecated")
_CsbH248StatsRequestsRcvd_Type = Counter32
_CsbH248StatsRequestsRcvd_Object = MibTableColumn
csbH248StatsRequestsRcvd = _CsbH248StatsRequestsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1, 3),
    _CsbH248StatsRequestsRcvd_Type()
)
csbH248StatsRequestsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRequestsRcvd.setStatus("deprecated")
_CsbH248StatsRequestsFailed_Type = Counter32
_CsbH248StatsRequestsFailed_Object = MibTableColumn
csbH248StatsRequestsFailed = _CsbH248StatsRequestsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1, 4),
    _CsbH248StatsRequestsFailed_Type()
)
csbH248StatsRequestsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRequestsFailed.setStatus("deprecated")
_CsbH248StatsRequestsRetried_Type = Counter32
_CsbH248StatsRequestsRetried_Object = MibTableColumn
csbH248StatsRequestsRetried = _CsbH248StatsRequestsRetried_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1, 5),
    _CsbH248StatsRequestsRetried_Type()
)
csbH248StatsRequestsRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRequestsRetried.setStatus("deprecated")
_CsbH248StatsRepliesSent_Type = Counter32
_CsbH248StatsRepliesSent_Object = MibTableColumn
csbH248StatsRepliesSent = _CsbH248StatsRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1, 6),
    _CsbH248StatsRepliesSent_Type()
)
csbH248StatsRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRepliesSent.setStatus("deprecated")
_CsbH248StatsRepliesRcvd_Type = Counter32
_CsbH248StatsRepliesRcvd_Object = MibTableColumn
csbH248StatsRepliesRcvd = _CsbH248StatsRepliesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1, 7),
    _CsbH248StatsRepliesRcvd_Type()
)
csbH248StatsRepliesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRepliesRcvd.setStatus("deprecated")
_CsbH248StatsRepliesRetried_Type = Counter32
_CsbH248StatsRepliesRetried_Object = MibTableColumn
csbH248StatsRepliesRetried = _CsbH248StatsRepliesRetried_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1, 8),
    _CsbH248StatsRepliesRetried_Type()
)
csbH248StatsRepliesRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRepliesRetried.setStatus("deprecated")
_CsbH248StatsSegPktsSent_Type = Counter32
_CsbH248StatsSegPktsSent_Object = MibTableColumn
csbH248StatsSegPktsSent = _CsbH248StatsSegPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1, 9),
    _CsbH248StatsSegPktsSent_Type()
)
csbH248StatsSegPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsSegPktsSent.setStatus("deprecated")
_CsbH248StatsSegPktsRcvd_Type = Counter32
_CsbH248StatsSegPktsRcvd_Object = MibTableColumn
csbH248StatsSegPktsRcvd = _CsbH248StatsSegPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1, 10),
    _CsbH248StatsSegPktsRcvd_Type()
)
csbH248StatsSegPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsSegPktsRcvd.setStatus("deprecated")


class _CsbH248StatsEstablishedTime_Type(OctetString):
    """Custom type csbH248StatsEstablishedTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CsbH248StatsEstablishedTime_Type.__name__ = "OctetString"
_CsbH248StatsEstablishedTime_Object = MibTableColumn
csbH248StatsEstablishedTime = _CsbH248StatsEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1, 11),
    _CsbH248StatsEstablishedTime_Type()
)
csbH248StatsEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsEstablishedTime.setStatus("deprecated")
_CsbH248StatsTMaxTimeoutVal_Type = Integer32
_CsbH248StatsTMaxTimeoutVal_Object = MibTableColumn
csbH248StatsTMaxTimeoutVal = _CsbH248StatsTMaxTimeoutVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1, 12),
    _CsbH248StatsTMaxTimeoutVal_Type()
)
csbH248StatsTMaxTimeoutVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsTMaxTimeoutVal.setStatus("deprecated")
if mibBuilder.loadTexts:
    csbH248StatsTMaxTimeoutVal.setUnits("milliseconds")
_CsbH248StatsRTT_Type = Gauge32
_CsbH248StatsRTT_Object = MibTableColumn
csbH248StatsRTT = _CsbH248StatsRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1, 13),
    _CsbH248StatsRTT_Type()
)
csbH248StatsRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRTT.setStatus("deprecated")
if mibBuilder.loadTexts:
    csbH248StatsRTT.setUnits("milliseconds")
_CsbH248StatsLT_Type = Gauge32
_CsbH248StatsLT_Object = MibTableColumn
csbH248StatsLT = _CsbH248StatsLT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 6, 1, 14),
    _CsbH248StatsLT_Type()
)
csbH248StatsLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsLT.setStatus("deprecated")
if mibBuilder.loadTexts:
    csbH248StatsLT.setUnits("milliseconds")
_CsbH248StatsRev1Table_Object = MibTable
csbH248StatsRev1Table = _CsbH248StatsRev1Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7)
)
if mibBuilder.loadTexts:
    csbH248StatsRev1Table.setStatus("current")
_CsbH248StatsRev1Entry_Object = MibTableRow
csbH248StatsRev1Entry = _CsbH248StatsRev1Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1)
)
csbH248StatsRev1Entry.setIndexNames(
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsInstanceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsServiceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsVdbeId"),
)
if mibBuilder.loadTexts:
    csbH248StatsRev1Entry.setStatus("current")


class _CsbH248StatsVdbeId_Type(Integer32):
    """Custom type csbH248StatsVdbeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CsbH248StatsVdbeId_Type.__name__ = "Integer32"
_CsbH248StatsVdbeId_Object = MibTableColumn
csbH248StatsVdbeId = _CsbH248StatsVdbeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1, 1),
    _CsbH248StatsVdbeId_Type()
)
csbH248StatsVdbeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbH248StatsVdbeId.setStatus("current")
_CsbH248StatsRequestsSentRev1_Type = Counter32
_CsbH248StatsRequestsSentRev1_Object = MibTableColumn
csbH248StatsRequestsSentRev1 = _CsbH248StatsRequestsSentRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1, 2),
    _CsbH248StatsRequestsSentRev1_Type()
)
csbH248StatsRequestsSentRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRequestsSentRev1.setStatus("current")
_CsbH248StatsRequestsRcvdRev1_Type = Counter32
_CsbH248StatsRequestsRcvdRev1_Object = MibTableColumn
csbH248StatsRequestsRcvdRev1 = _CsbH248StatsRequestsRcvdRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1, 3),
    _CsbH248StatsRequestsRcvdRev1_Type()
)
csbH248StatsRequestsRcvdRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRequestsRcvdRev1.setStatus("current")
_CsbH248StatsRequestsFailedRev1_Type = Counter32
_CsbH248StatsRequestsFailedRev1_Object = MibTableColumn
csbH248StatsRequestsFailedRev1 = _CsbH248StatsRequestsFailedRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1, 4),
    _CsbH248StatsRequestsFailedRev1_Type()
)
csbH248StatsRequestsFailedRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRequestsFailedRev1.setStatus("current")
_CsbH248StatsRequestsRetriedRev1_Type = Counter32
_CsbH248StatsRequestsRetriedRev1_Object = MibTableColumn
csbH248StatsRequestsRetriedRev1 = _CsbH248StatsRequestsRetriedRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1, 5),
    _CsbH248StatsRequestsRetriedRev1_Type()
)
csbH248StatsRequestsRetriedRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRequestsRetriedRev1.setStatus("current")
_CsbH248StatsRepliesSentRev1_Type = Counter32
_CsbH248StatsRepliesSentRev1_Object = MibTableColumn
csbH248StatsRepliesSentRev1 = _CsbH248StatsRepliesSentRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1, 6),
    _CsbH248StatsRepliesSentRev1_Type()
)
csbH248StatsRepliesSentRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRepliesSentRev1.setStatus("current")
_CsbH248StatsRepliesRcvdRev1_Type = Counter32
_CsbH248StatsRepliesRcvdRev1_Object = MibTableColumn
csbH248StatsRepliesRcvdRev1 = _CsbH248StatsRepliesRcvdRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1, 7),
    _CsbH248StatsRepliesRcvdRev1_Type()
)
csbH248StatsRepliesRcvdRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRepliesRcvdRev1.setStatus("current")
_CsbH248StatsRepliesRetriedRev1_Type = Counter32
_CsbH248StatsRepliesRetriedRev1_Object = MibTableColumn
csbH248StatsRepliesRetriedRev1 = _CsbH248StatsRepliesRetriedRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1, 8),
    _CsbH248StatsRepliesRetriedRev1_Type()
)
csbH248StatsRepliesRetriedRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRepliesRetriedRev1.setStatus("current")
_CsbH248StatsSegPktsSentRev1_Type = Counter32
_CsbH248StatsSegPktsSentRev1_Object = MibTableColumn
csbH248StatsSegPktsSentRev1 = _CsbH248StatsSegPktsSentRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1, 9),
    _CsbH248StatsSegPktsSentRev1_Type()
)
csbH248StatsSegPktsSentRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsSegPktsSentRev1.setStatus("current")
_CsbH248StatsSegPktsRcvdRev1_Type = Counter32
_CsbH248StatsSegPktsRcvdRev1_Object = MibTableColumn
csbH248StatsSegPktsRcvdRev1 = _CsbH248StatsSegPktsRcvdRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1, 10),
    _CsbH248StatsSegPktsRcvdRev1_Type()
)
csbH248StatsSegPktsRcvdRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsSegPktsRcvdRev1.setStatus("current")


class _CsbH248StatsEstablishedTimeRev1_Type(OctetString):
    """Custom type csbH248StatsEstablishedTimeRev1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CsbH248StatsEstablishedTimeRev1_Type.__name__ = "OctetString"
_CsbH248StatsEstablishedTimeRev1_Object = MibTableColumn
csbH248StatsEstablishedTimeRev1 = _CsbH248StatsEstablishedTimeRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1, 11),
    _CsbH248StatsEstablishedTimeRev1_Type()
)
csbH248StatsEstablishedTimeRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsEstablishedTimeRev1.setStatus("current")
_CsbH248StatsTMaxTimeoutValRev1_Type = Integer32
_CsbH248StatsTMaxTimeoutValRev1_Object = MibTableColumn
csbH248StatsTMaxTimeoutValRev1 = _CsbH248StatsTMaxTimeoutValRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1, 12),
    _CsbH248StatsTMaxTimeoutValRev1_Type()
)
csbH248StatsTMaxTimeoutValRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsTMaxTimeoutValRev1.setStatus("current")
if mibBuilder.loadTexts:
    csbH248StatsTMaxTimeoutValRev1.setUnits("milliseconds")
_CsbH248StatsRTTRev1_Type = Gauge32
_CsbH248StatsRTTRev1_Object = MibTableColumn
csbH248StatsRTTRev1 = _CsbH248StatsRTTRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1, 13),
    _CsbH248StatsRTTRev1_Type()
)
csbH248StatsRTTRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsRTTRev1.setStatus("current")
if mibBuilder.loadTexts:
    csbH248StatsRTTRev1.setUnits("milliseconds")
_CsbH248StatsLTRev1_Type = Gauge32
_CsbH248StatsLTRev1_Object = MibTableColumn
csbH248StatsLTRev1 = _CsbH248StatsLTRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 1, 7, 1, 14),
    _CsbH248StatsLTRev1_Type()
)
csbH248StatsLTRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbH248StatsLTRev1.setStatus("current")
if mibBuilder.loadTexts:
    csbH248StatsLTRev1.setUnits("milliseconds")
_CiscoSbcCallStatsMIBConform_ObjectIdentity = ObjectIdentity
ciscoSbcCallStatsMIBConform = _CiscoSbcCallStatsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2)
)
_CsbCallStatsMIBCompliances_ObjectIdentity = ObjectIdentity
csbCallStatsMIBCompliances = _CsbCallStatsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 1)
)
_CsbCallStatsMIBGroups_ObjectIdentity = ObjectIdentity
csbCallStatsMIBGroups = _CsbCallStatsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 2)
)

# Managed Objects groups

csbStatsInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 2, 1)
)
csbStatsInstanceGroup.setObjects(
    ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsInstancePhysicalIndex")
)
if mibBuilder.loadTexts:
    csbStatsInstanceGroup.setStatus("current")

csbGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 2, 2)
)
csbGlobalStatsGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsCallsHigh"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsRate1Sec"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsCallsLow"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsAvailableFlows"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsUsedFlows"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsTotalFlows"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsRTPPktsRcvd"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsRTPPktsDiscard"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsUsedSigFlows"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsTotalSigFlows"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsAvailablePktRate"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsPeakFlows"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsUnclassifiedPkts"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsRTPOctetsSent"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsRTPOctetsRcvd"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsRTPOctetsDiscard"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsPeakSigFlows"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsSbcName"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsRTPPktsSent"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsNoMediaCount"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsRouteErrors"))
)
if mibBuilder.loadTexts:
    csbGlobalStatsGroup.setStatus("current")

csbCurrPeriodicStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 2, 3)
)
csbCurrPeriodicStatsGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsActiveCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsActivatingCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsDeactivatingCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsTotalCallAttempts"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsFailedCallAttempts"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCallRoutingFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCallResourceFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCallMediaFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCallSigFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsActiveCallFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCongestionFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCallSetupPolicyFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCallSetupNAPolicyFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCallSetupRoutingPolicyFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCallSetupCACPolicyFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCallSetupCACCallLimitFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCallSetupCACRateLimitFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCallSetupCACBandwidthFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCallSetupCACMediaLimitFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCallSetupCACMediaUpdateFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsTimestamp"))
)
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsGroup.setStatus("current")

csbHistoryStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 2, 4)
)
csbHistoryStatsGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsActiveCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsTotalCallAttempts"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsFailedCallAttempts"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsCallRoutingFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsCallResourceFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsCallMediaFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsFailSigFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsActiveCallFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsCongestionFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsCallSetupPolicyFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsCallSetupNAPolicyFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsCallSetupRoutingPolicyFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsCallSetupCACPolicyFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsCallSetupCACCallLimitFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsCallSetupCACRateLimitFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsCallSetupCACBandwidthFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsCallSetupCACMediaLimitFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsCallSetupCACMediaUpdateFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsTimestamp"))
)
if mibBuilder.loadTexts:
    csbHistoryStatsGroup.setStatus("current")

csbPerFlowStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 2, 5)
)
csbPerFlowStatsGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsRTPPktsRcvd"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsRTPPktsSent"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsRTPPktsDiscard"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsRTCPPktsSent"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsRTPOctetsRcvd"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsRTPOctetsSent"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsRTPOctetsDiscard"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsRTCPPktsRcvd"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsRTCPPktsLost"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsFlowType"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsTmanPerMbs"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsTmanPerSdr"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsDscpSettings"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsAdrStatus"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsQASettings"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsEPJitter"))
)
if mibBuilder.loadTexts:
    csbPerFlowStatsGroup.setStatus("current")

csbH248StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 2, 6)
)
csbH248StatsGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRequestsSent"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRequestsRcvd"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRequestsFailed"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRequestsRetried"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRepliesSent"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRepliesRcvd"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRepliesRetried"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsSegPktsSent"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsSegPktsRcvd"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsTMaxTimeoutVal"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRTT"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsLT"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsEstablishedTime"))
)
if mibBuilder.loadTexts:
    csbH248StatsGroup.setStatus("deprecated")

csbH248StatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 2, 7)
)
csbH248StatsGroupRev1.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRequestsSentRev1"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRequestsRcvdRev1"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRequestsFailedRev1"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRequestsRetriedRev1"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRepliesSentRev1"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRepliesRcvdRev1"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRepliesRetriedRev1"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsSegPktsSentRev1"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsSegPktsRcvdRev1"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsEstablishedTimeRev1"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsTMaxTimeoutValRev1"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsRTTRev1"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbH248StatsLTRev1"))
)
if mibBuilder.loadTexts:
    csbH248StatsGroupRev1.setStatus("current")

csbGlobalStatsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 2, 8)
)
csbGlobalStatsGroupSup1.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsAvailableTranscodeFlows"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsActiveTranscodeFlows"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsPeakTranscodeFlows"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsTotalTranscodeFlows"))
)
if mibBuilder.loadTexts:
    csbGlobalStatsGroupSup1.setStatus("current")

csbCurrPeriodicStatsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 2, 9)
)
csbCurrPeriodicStatsGroupSup1.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsTranscodedCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsTransratedCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsTotalCallUpdateFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsActiveIpv6Calls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsActiveEmergencyCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsActiveE2EmergencyCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsImsRxActiveCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsImsRxCallSetupFaiures"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsImsRxCallRenegotiationAttempts"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsImsRxCallRenegotiationFailures"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsAudioTranscodedCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsFaxTranscodedCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsRtpDisallowedFailures"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsSrtpDisallowedFailures"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsNonSrtpCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsSrtpNonIwCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsSrtpIwCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsDtmfIw2833Calls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsDtmfIwInbandCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsDtmfIw2833InbandCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsTotalTapsRequested"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsTotalTapsSucceeded"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicStatsCurrentTaps"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCurrPeriodicIpsecCalls"))
)
if mibBuilder.loadTexts:
    csbCurrPeriodicStatsGroupSup1.setStatus("current")

csbHistoryStatsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 2, 10)
)
csbHistoryStatsGroupSup1.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistroyStatsTranscodedCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistroyStatsTransratedCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsTotalCallUpdateFailure"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsActiveIpv6Calls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsActiveEmergencyCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsActiveE2EmergencyCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsImsRxActiveCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsImsRxCallSetupFailures"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsImsRxCallRenegotiationAttempts"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsImsRxCallRenegotiationFailures"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsAudioTranscodedCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsFaxTranscodedCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsRtpDisallowedFailures"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsSrtpDisallowedFailures"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsNonSrtpCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsSrtpNonIwCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsSrtpIwCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsDtmfIw2833Calls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsDtmfIwInbandCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsDtmfIw2833InbandCalls"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsTotalTapsRequested"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsTotalTapsSucceeded"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsCurrentTaps"),
        ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbHistoryStatsIpsecCalls"))
)
if mibBuilder.loadTexts:
    csbHistoryStatsGroupSup1.setStatus("current")

csbPerFlowStatsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 2, 11)
)
csbPerFlowStatsGroupSup1.setObjects(
    ("CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbPerFlowStatsRTPPktsLost")
)
if mibBuilder.loadTexts:
    csbPerFlowStatsGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

csbCallStatsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 1, 1)
)
if mibBuilder.loadTexts:
    csbCallStatsMIBCompliance.setStatus(
        "deprecated"
    )

csbCallStatsMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 1, 2)
)
if mibBuilder.loadTexts:
    csbCallStatsMIBComplianceRev1.setStatus(
        "deprecated"
    )

csbCallStatsMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 657, 2, 1, 3)
)
if mibBuilder.loadTexts:
    csbCallStatsMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB",
    **{"CiscoSbcPeriodicStatsInterval": CiscoSbcPeriodicStatsInterval,
       "ciscoSbcCallStatsMIB": ciscoSbcCallStatsMIB,
       "ciscoSbcCallStatsMIBNotifs": ciscoSbcCallStatsMIBNotifs,
       "ciscoSbcCallStatsMIBObjects": ciscoSbcCallStatsMIBObjects,
       "csbCallStatsInstanceTable": csbCallStatsInstanceTable,
       "csbCallStatsInstanceEntry": csbCallStatsInstanceEntry,
       "csbCallStatsInstanceIndex": csbCallStatsInstanceIndex,
       "csbCallStatsInstancePhysicalIndex": csbCallStatsInstancePhysicalIndex,
       "csbCallStatsTable": csbCallStatsTable,
       "csbCallStatsEntry": csbCallStatsEntry,
       "csbCallStatsServiceIndex": csbCallStatsServiceIndex,
       "csbCallStatsSbcName": csbCallStatsSbcName,
       "csbCallStatsCallsHigh": csbCallStatsCallsHigh,
       "csbCallStatsRate1Sec": csbCallStatsRate1Sec,
       "csbCallStatsCallsLow": csbCallStatsCallsLow,
       "csbCallStatsAvailableFlows": csbCallStatsAvailableFlows,
       "csbCallStatsUsedFlows": csbCallStatsUsedFlows,
       "csbCallStatsPeakFlows": csbCallStatsPeakFlows,
       "csbCallStatsTotalFlows": csbCallStatsTotalFlows,
       "csbCallStatsUsedSigFlows": csbCallStatsUsedSigFlows,
       "csbCallStatsPeakSigFlows": csbCallStatsPeakSigFlows,
       "csbCallStatsTotalSigFlows": csbCallStatsTotalSigFlows,
       "csbCallStatsAvailablePktRate": csbCallStatsAvailablePktRate,
       "csbCallStatsUnclassifiedPkts": csbCallStatsUnclassifiedPkts,
       "csbCallStatsRTPPktsSent": csbCallStatsRTPPktsSent,
       "csbCallStatsRTPPktsRcvd": csbCallStatsRTPPktsRcvd,
       "csbCallStatsRTPPktsDiscard": csbCallStatsRTPPktsDiscard,
       "csbCallStatsRTPOctetsSent": csbCallStatsRTPOctetsSent,
       "csbCallStatsRTPOctetsRcvd": csbCallStatsRTPOctetsRcvd,
       "csbCallStatsRTPOctetsDiscard": csbCallStatsRTPOctetsDiscard,
       "csbCallStatsNoMediaCount": csbCallStatsNoMediaCount,
       "csbCallStatsRouteErrors": csbCallStatsRouteErrors,
       "csbCallStatsAvailableTranscodeFlows": csbCallStatsAvailableTranscodeFlows,
       "csbCallStatsActiveTranscodeFlows": csbCallStatsActiveTranscodeFlows,
       "csbCallStatsPeakTranscodeFlows": csbCallStatsPeakTranscodeFlows,
       "csbCallStatsTotalTranscodeFlows": csbCallStatsTotalTranscodeFlows,
       "csbCurrPeriodicStatsTable": csbCurrPeriodicStatsTable,
       "csbCurrPeriodicStatsEntry": csbCurrPeriodicStatsEntry,
       "csbCurrPeriodicStatsInterval": csbCurrPeriodicStatsInterval,
       "csbCurrPeriodicStatsActiveCalls": csbCurrPeriodicStatsActiveCalls,
       "csbCurrPeriodicStatsActivatingCalls": csbCurrPeriodicStatsActivatingCalls,
       "csbCurrPeriodicStatsDeactivatingCalls": csbCurrPeriodicStatsDeactivatingCalls,
       "csbCurrPeriodicStatsTotalCallAttempts": csbCurrPeriodicStatsTotalCallAttempts,
       "csbCurrPeriodicStatsFailedCallAttempts": csbCurrPeriodicStatsFailedCallAttempts,
       "csbCurrPeriodicStatsCallRoutingFailure": csbCurrPeriodicStatsCallRoutingFailure,
       "csbCurrPeriodicStatsCallResourceFailure": csbCurrPeriodicStatsCallResourceFailure,
       "csbCurrPeriodicStatsCallMediaFailure": csbCurrPeriodicStatsCallMediaFailure,
       "csbCurrPeriodicStatsCallSigFailure": csbCurrPeriodicStatsCallSigFailure,
       "csbCurrPeriodicStatsActiveCallFailure": csbCurrPeriodicStatsActiveCallFailure,
       "csbCurrPeriodicStatsCongestionFailure": csbCurrPeriodicStatsCongestionFailure,
       "csbCurrPeriodicStatsCallSetupPolicyFailure": csbCurrPeriodicStatsCallSetupPolicyFailure,
       "csbCurrPeriodicStatsCallSetupNAPolicyFailure": csbCurrPeriodicStatsCallSetupNAPolicyFailure,
       "csbCurrPeriodicStatsCallSetupRoutingPolicyFailure": csbCurrPeriodicStatsCallSetupRoutingPolicyFailure,
       "csbCurrPeriodicStatsCallSetupCACPolicyFailure": csbCurrPeriodicStatsCallSetupCACPolicyFailure,
       "csbCurrPeriodicStatsCallSetupCACCallLimitFailure": csbCurrPeriodicStatsCallSetupCACCallLimitFailure,
       "csbCurrPeriodicStatsCallSetupCACRateLimitFailure": csbCurrPeriodicStatsCallSetupCACRateLimitFailure,
       "csbCurrPeriodicStatsCallSetupCACBandwidthFailure": csbCurrPeriodicStatsCallSetupCACBandwidthFailure,
       "csbCurrPeriodicStatsCallSetupCACMediaLimitFailure": csbCurrPeriodicStatsCallSetupCACMediaLimitFailure,
       "csbCurrPeriodicStatsCallSetupCACMediaUpdateFailure": csbCurrPeriodicStatsCallSetupCACMediaUpdateFailure,
       "csbCurrPeriodicStatsTimestamp": csbCurrPeriodicStatsTimestamp,
       "csbCurrPeriodicStatsTranscodedCalls": csbCurrPeriodicStatsTranscodedCalls,
       "csbCurrPeriodicStatsTransratedCalls": csbCurrPeriodicStatsTransratedCalls,
       "csbCurrPeriodicStatsTotalCallUpdateFailure": csbCurrPeriodicStatsTotalCallUpdateFailure,
       "csbCurrPeriodicStatsActiveIpv6Calls": csbCurrPeriodicStatsActiveIpv6Calls,
       "csbCurrPeriodicStatsActiveEmergencyCalls": csbCurrPeriodicStatsActiveEmergencyCalls,
       "csbCurrPeriodicStatsActiveE2EmergencyCalls": csbCurrPeriodicStatsActiveE2EmergencyCalls,
       "csbCurrPeriodicStatsImsRxActiveCalls": csbCurrPeriodicStatsImsRxActiveCalls,
       "csbCurrPeriodicStatsImsRxCallSetupFaiures": csbCurrPeriodicStatsImsRxCallSetupFaiures,
       "csbCurrPeriodicStatsImsRxCallRenegotiationAttempts": csbCurrPeriodicStatsImsRxCallRenegotiationAttempts,
       "csbCurrPeriodicStatsImsRxCallRenegotiationFailures": csbCurrPeriodicStatsImsRxCallRenegotiationFailures,
       "csbCurrPeriodicStatsAudioTranscodedCalls": csbCurrPeriodicStatsAudioTranscodedCalls,
       "csbCurrPeriodicStatsFaxTranscodedCalls": csbCurrPeriodicStatsFaxTranscodedCalls,
       "csbCurrPeriodicStatsRtpDisallowedFailures": csbCurrPeriodicStatsRtpDisallowedFailures,
       "csbCurrPeriodicStatsSrtpDisallowedFailures": csbCurrPeriodicStatsSrtpDisallowedFailures,
       "csbCurrPeriodicStatsNonSrtpCalls": csbCurrPeriodicStatsNonSrtpCalls,
       "csbCurrPeriodicStatsSrtpNonIwCalls": csbCurrPeriodicStatsSrtpNonIwCalls,
       "csbCurrPeriodicStatsSrtpIwCalls": csbCurrPeriodicStatsSrtpIwCalls,
       "csbCurrPeriodicStatsDtmfIw2833Calls": csbCurrPeriodicStatsDtmfIw2833Calls,
       "csbCurrPeriodicStatsDtmfIwInbandCalls": csbCurrPeriodicStatsDtmfIwInbandCalls,
       "csbCurrPeriodicStatsDtmfIw2833InbandCalls": csbCurrPeriodicStatsDtmfIw2833InbandCalls,
       "csbCurrPeriodicStatsTotalTapsRequested": csbCurrPeriodicStatsTotalTapsRequested,
       "csbCurrPeriodicStatsTotalTapsSucceeded": csbCurrPeriodicStatsTotalTapsSucceeded,
       "csbCurrPeriodicStatsCurrentTaps": csbCurrPeriodicStatsCurrentTaps,
       "csbCurrPeriodicIpsecCalls": csbCurrPeriodicIpsecCalls,
       "csbHistoryStatsTable": csbHistoryStatsTable,
       "csbHistoryStatsEntry": csbHistoryStatsEntry,
       "csbHistoryStatsInterval": csbHistoryStatsInterval,
       "csbHistoryStatsElements": csbHistoryStatsElements,
       "csbHistoryStatsActiveCalls": csbHistoryStatsActiveCalls,
       "csbHistoryStatsTotalCallAttempts": csbHistoryStatsTotalCallAttempts,
       "csbHistoryStatsFailedCallAttempts": csbHistoryStatsFailedCallAttempts,
       "csbHistoryStatsCallRoutingFailure": csbHistoryStatsCallRoutingFailure,
       "csbHistoryStatsCallResourceFailure": csbHistoryStatsCallResourceFailure,
       "csbHistoryStatsCallMediaFailure": csbHistoryStatsCallMediaFailure,
       "csbHistoryStatsFailSigFailure": csbHistoryStatsFailSigFailure,
       "csbHistoryStatsActiveCallFailure": csbHistoryStatsActiveCallFailure,
       "csbHistoryStatsCongestionFailure": csbHistoryStatsCongestionFailure,
       "csbHistoryStatsCallSetupPolicyFailure": csbHistoryStatsCallSetupPolicyFailure,
       "csbHistoryStatsCallSetupNAPolicyFailure": csbHistoryStatsCallSetupNAPolicyFailure,
       "csbHistoryStatsCallSetupRoutingPolicyFailure": csbHistoryStatsCallSetupRoutingPolicyFailure,
       "csbHistoryStatsCallSetupCACPolicyFailure": csbHistoryStatsCallSetupCACPolicyFailure,
       "csbHistoryStatsCallSetupCACCallLimitFailure": csbHistoryStatsCallSetupCACCallLimitFailure,
       "csbHistoryStatsCallSetupCACRateLimitFailure": csbHistoryStatsCallSetupCACRateLimitFailure,
       "csbHistoryStatsCallSetupCACBandwidthFailure": csbHistoryStatsCallSetupCACBandwidthFailure,
       "csbHistoryStatsCallSetupCACMediaLimitFailure": csbHistoryStatsCallSetupCACMediaLimitFailure,
       "csbHistoryStatsCallSetupCACMediaUpdateFailure": csbHistoryStatsCallSetupCACMediaUpdateFailure,
       "csbHistoryStatsTimestamp": csbHistoryStatsTimestamp,
       "csbHistroyStatsTranscodedCalls": csbHistroyStatsTranscodedCalls,
       "csbHistroyStatsTransratedCalls": csbHistroyStatsTransratedCalls,
       "csbHistoryStatsTotalCallUpdateFailure": csbHistoryStatsTotalCallUpdateFailure,
       "csbHistoryStatsActiveIpv6Calls": csbHistoryStatsActiveIpv6Calls,
       "csbHistoryStatsActiveEmergencyCalls": csbHistoryStatsActiveEmergencyCalls,
       "csbHistoryStatsActiveE2EmergencyCalls": csbHistoryStatsActiveE2EmergencyCalls,
       "csbHistoryStatsImsRxActiveCalls": csbHistoryStatsImsRxActiveCalls,
       "csbHistoryStatsImsRxCallSetupFailures": csbHistoryStatsImsRxCallSetupFailures,
       "csbHistoryStatsImsRxCallRenegotiationAttempts": csbHistoryStatsImsRxCallRenegotiationAttempts,
       "csbHistoryStatsImsRxCallRenegotiationFailures": csbHistoryStatsImsRxCallRenegotiationFailures,
       "csbHistoryStatsAudioTranscodedCalls": csbHistoryStatsAudioTranscodedCalls,
       "csbHistoryStatsFaxTranscodedCalls": csbHistoryStatsFaxTranscodedCalls,
       "csbHistoryStatsRtpDisallowedFailures": csbHistoryStatsRtpDisallowedFailures,
       "csbHistoryStatsSrtpDisallowedFailures": csbHistoryStatsSrtpDisallowedFailures,
       "csbHistoryStatsNonSrtpCalls": csbHistoryStatsNonSrtpCalls,
       "csbHistoryStatsSrtpNonIwCalls": csbHistoryStatsSrtpNonIwCalls,
       "csbHistoryStatsSrtpIwCalls": csbHistoryStatsSrtpIwCalls,
       "csbHistoryStatsDtmfIw2833Calls": csbHistoryStatsDtmfIw2833Calls,
       "csbHistoryStatsDtmfIwInbandCalls": csbHistoryStatsDtmfIwInbandCalls,
       "csbHistoryStatsDtmfIw2833InbandCalls": csbHistoryStatsDtmfIw2833InbandCalls,
       "csbHistoryStatsTotalTapsRequested": csbHistoryStatsTotalTapsRequested,
       "csbHistoryStatsTotalTapsSucceeded": csbHistoryStatsTotalTapsSucceeded,
       "csbHistoryStatsCurrentTaps": csbHistoryStatsCurrentTaps,
       "csbHistoryStatsIpsecCalls": csbHistoryStatsIpsecCalls,
       "csbPerFlowStatsTable": csbPerFlowStatsTable,
       "csbPerFlowStatsEntry": csbPerFlowStatsEntry,
       "csbPerFlowStatsVdbeId": csbPerFlowStatsVdbeId,
       "csbPerFlowStatsGateId": csbPerFlowStatsGateId,
       "csbPerFlowStatsFlowPairId": csbPerFlowStatsFlowPairId,
       "csbPerFlowStatsSideId": csbPerFlowStatsSideId,
       "csbPerFlowStatsFlowType": csbPerFlowStatsFlowType,
       "csbPerFlowStatsRTPPktsSent": csbPerFlowStatsRTPPktsSent,
       "csbPerFlowStatsRTPPktsRcvd": csbPerFlowStatsRTPPktsRcvd,
       "csbPerFlowStatsRTPPktsDiscard": csbPerFlowStatsRTPPktsDiscard,
       "csbPerFlowStatsRTPOctetsSent": csbPerFlowStatsRTPOctetsSent,
       "csbPerFlowStatsRTPOctetsRcvd": csbPerFlowStatsRTPOctetsRcvd,
       "csbPerFlowStatsRTPOctetsDiscard": csbPerFlowStatsRTPOctetsDiscard,
       "csbPerFlowStatsRTCPPktsSent": csbPerFlowStatsRTCPPktsSent,
       "csbPerFlowStatsRTCPPktsRcvd": csbPerFlowStatsRTCPPktsRcvd,
       "csbPerFlowStatsRTCPPktsLost": csbPerFlowStatsRTCPPktsLost,
       "csbPerFlowStatsEPJitter": csbPerFlowStatsEPJitter,
       "csbPerFlowStatsTmanPerMbs": csbPerFlowStatsTmanPerMbs,
       "csbPerFlowStatsTmanPerSdr": csbPerFlowStatsTmanPerSdr,
       "csbPerFlowStatsDscpSettings": csbPerFlowStatsDscpSettings,
       "csbPerFlowStatsAdrStatus": csbPerFlowStatsAdrStatus,
       "csbPerFlowStatsQASettings": csbPerFlowStatsQASettings,
       "csbPerFlowStatsRTPPktsLost": csbPerFlowStatsRTPPktsLost,
       "csbH248StatsTable": csbH248StatsTable,
       "csbH248StatsEntry": csbH248StatsEntry,
       "csbH248StatsCtrlrIndex": csbH248StatsCtrlrIndex,
       "csbH248StatsRequestsSent": csbH248StatsRequestsSent,
       "csbH248StatsRequestsRcvd": csbH248StatsRequestsRcvd,
       "csbH248StatsRequestsFailed": csbH248StatsRequestsFailed,
       "csbH248StatsRequestsRetried": csbH248StatsRequestsRetried,
       "csbH248StatsRepliesSent": csbH248StatsRepliesSent,
       "csbH248StatsRepliesRcvd": csbH248StatsRepliesRcvd,
       "csbH248StatsRepliesRetried": csbH248StatsRepliesRetried,
       "csbH248StatsSegPktsSent": csbH248StatsSegPktsSent,
       "csbH248StatsSegPktsRcvd": csbH248StatsSegPktsRcvd,
       "csbH248StatsEstablishedTime": csbH248StatsEstablishedTime,
       "csbH248StatsTMaxTimeoutVal": csbH248StatsTMaxTimeoutVal,
       "csbH248StatsRTT": csbH248StatsRTT,
       "csbH248StatsLT": csbH248StatsLT,
       "csbH248StatsRev1Table": csbH248StatsRev1Table,
       "csbH248StatsRev1Entry": csbH248StatsRev1Entry,
       "csbH248StatsVdbeId": csbH248StatsVdbeId,
       "csbH248StatsRequestsSentRev1": csbH248StatsRequestsSentRev1,
       "csbH248StatsRequestsRcvdRev1": csbH248StatsRequestsRcvdRev1,
       "csbH248StatsRequestsFailedRev1": csbH248StatsRequestsFailedRev1,
       "csbH248StatsRequestsRetriedRev1": csbH248StatsRequestsRetriedRev1,
       "csbH248StatsRepliesSentRev1": csbH248StatsRepliesSentRev1,
       "csbH248StatsRepliesRcvdRev1": csbH248StatsRepliesRcvdRev1,
       "csbH248StatsRepliesRetriedRev1": csbH248StatsRepliesRetriedRev1,
       "csbH248StatsSegPktsSentRev1": csbH248StatsSegPktsSentRev1,
       "csbH248StatsSegPktsRcvdRev1": csbH248StatsSegPktsRcvdRev1,
       "csbH248StatsEstablishedTimeRev1": csbH248StatsEstablishedTimeRev1,
       "csbH248StatsTMaxTimeoutValRev1": csbH248StatsTMaxTimeoutValRev1,
       "csbH248StatsRTTRev1": csbH248StatsRTTRev1,
       "csbH248StatsLTRev1": csbH248StatsLTRev1,
       "ciscoSbcCallStatsMIBConform": ciscoSbcCallStatsMIBConform,
       "csbCallStatsMIBCompliances": csbCallStatsMIBCompliances,
       "csbCallStatsMIBCompliance": csbCallStatsMIBCompliance,
       "csbCallStatsMIBComplianceRev1": csbCallStatsMIBComplianceRev1,
       "csbCallStatsMIBComplianceRev2": csbCallStatsMIBComplianceRev2,
       "csbCallStatsMIBGroups": csbCallStatsMIBGroups,
       "csbStatsInstanceGroup": csbStatsInstanceGroup,
       "csbGlobalStatsGroup": csbGlobalStatsGroup,
       "csbCurrPeriodicStatsGroup": csbCurrPeriodicStatsGroup,
       "csbHistoryStatsGroup": csbHistoryStatsGroup,
       "csbPerFlowStatsGroup": csbPerFlowStatsGroup,
       "csbH248StatsGroup": csbH248StatsGroup,
       "csbH248StatsGroupRev1": csbH248StatsGroupRev1,
       "csbGlobalStatsGroupSup1": csbGlobalStatsGroupSup1,
       "csbCurrPeriodicStatsGroupSup1": csbCurrPeriodicStatsGroupSup1,
       "csbHistoryStatsGroupSup1": csbHistoryStatsGroupSup1,
       "csbPerFlowStatsGroupSup1": csbPerFlowStatsGroupSup1}
)
