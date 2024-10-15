# SNMP MIB module (ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:34 2024
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

(adGenAOSConformance,
 adGenAOSMef) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSConformance",
    "adGenAOSMef")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

(HCPerfCurrentCount,
 HCPerfIntervalCount,
 HCPerfInvalidIntervals,
 HCPerfTimeElapsed,
 HCPerfTotalCount,
 HCPerfValidIntervals) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount",
    "HCPerfIntervalCount",
    "HCPerfInvalidIntervals",
    "HCPerfTimeElapsed",
    "HCPerfTotalCount",
    "HCPerfValidIntervals")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

adGenAosMefPerCosPerUniPerfHistoryMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 2)
)
adGenAosMefPerCosPerUniPerfHistoryMib.setRevisions(
        ("2014-09-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAosMefPerCosPerUniPerfHistory_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerUniPerfHistory = _AdGenAosMefPerCosPerUniPerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2)
)
_AdMefPerCosPerUniPhCurTable_Object = MibTable
adMefPerCosPerUniPhCurTable = _AdMefPerCosPerUniPhCurTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1)
)
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurTable.setStatus("current")
_AdMefPerCosPerUniPhCurEntry_Object = MibTableRow
adMefPerCosPerUniPhCurEntry = _AdMefPerCosPerUniPhCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1)
)
adMefPerCosPerUniPhCurEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurQueueNumber"),
)
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurEntry.setStatus("current")


class _AdMefPerCosPerUniPhCurQueueNumber_Type(Unsigned32):
    """Custom type adMefPerCosPerUniPhCurQueueNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdMefPerCosPerUniPhCurQueueNumber_Type.__name__ = "Unsigned32"
_AdMefPerCosPerUniPhCurQueueNumber_Object = MibTableColumn
adMefPerCosPerUniPhCurQueueNumber = _AdMefPerCosPerUniPhCurQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 1),
    _AdMefPerCosPerUniPhCurQueueNumber_Type()
)
adMefPerCosPerUniPhCurQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurQueueNumber.setStatus("current")
_AdMefPerCosPerUniPhCurTimeElapsed15Min_Type = HCPerfTimeElapsed
_AdMefPerCosPerUniPhCurTimeElapsed15Min_Object = MibTableColumn
adMefPerCosPerUniPhCurTimeElapsed15Min = _AdMefPerCosPerUniPhCurTimeElapsed15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 2),
    _AdMefPerCosPerUniPhCurTimeElapsed15Min_Type()
)
adMefPerCosPerUniPhCurTimeElapsed15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurTimeElapsed15Min.setStatus("current")
_AdMefPerCosPerUniPhCurValidIntervals15Min_Type = HCPerfValidIntervals
_AdMefPerCosPerUniPhCurValidIntervals15Min_Object = MibTableColumn
adMefPerCosPerUniPhCurValidIntervals15Min = _AdMefPerCosPerUniPhCurValidIntervals15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 3),
    _AdMefPerCosPerUniPhCurValidIntervals15Min_Type()
)
adMefPerCosPerUniPhCurValidIntervals15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurValidIntervals15Min.setStatus("current")
_AdMefPerCosPerUniPhCurInvalidIntervals15Min_Type = HCPerfInvalidIntervals
_AdMefPerCosPerUniPhCurInvalidIntervals15Min_Object = MibTableColumn
adMefPerCosPerUniPhCurInvalidIntervals15Min = _AdMefPerCosPerUniPhCurInvalidIntervals15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 4),
    _AdMefPerCosPerUniPhCurInvalidIntervals15Min_Type()
)
adMefPerCosPerUniPhCurInvalidIntervals15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurInvalidIntervals15Min.setStatus("current")
_AdMefPerCosPerUniPhCurIngressGreenOctets15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurIngressGreenOctets15Min_Object = MibTableColumn
adMefPerCosPerUniPhCurIngressGreenOctets15Min = _AdMefPerCosPerUniPhCurIngressGreenOctets15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 5),
    _AdMefPerCosPerUniPhCurIngressGreenOctets15Min_Type()
)
adMefPerCosPerUniPhCurIngressGreenOctets15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurIngressGreenOctets15Min.setStatus("current")
_AdMefPerCosPerUniPhCurIngressGreenFrames15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurIngressGreenFrames15Min_Object = MibTableColumn
adMefPerCosPerUniPhCurIngressGreenFrames15Min = _AdMefPerCosPerUniPhCurIngressGreenFrames15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 6),
    _AdMefPerCosPerUniPhCurIngressGreenFrames15Min_Type()
)
adMefPerCosPerUniPhCurIngressGreenFrames15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurIngressGreenFrames15Min.setStatus("current")
_AdMefPerCosPerUniPhCurEgressGreenOctets15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurEgressGreenOctets15Min_Object = MibTableColumn
adMefPerCosPerUniPhCurEgressGreenOctets15Min = _AdMefPerCosPerUniPhCurEgressGreenOctets15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 7),
    _AdMefPerCosPerUniPhCurEgressGreenOctets15Min_Type()
)
adMefPerCosPerUniPhCurEgressGreenOctets15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurEgressGreenOctets15Min.setStatus("current")
_AdMefPerCosPerUniPhCurEgressGreenFrames15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurEgressGreenFrames15Min_Object = MibTableColumn
adMefPerCosPerUniPhCurEgressGreenFrames15Min = _AdMefPerCosPerUniPhCurEgressGreenFrames15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 8),
    _AdMefPerCosPerUniPhCurEgressGreenFrames15Min_Type()
)
adMefPerCosPerUniPhCurEgressGreenFrames15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurEgressGreenFrames15Min.setStatus("current")
_AdMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min_Object = MibTableColumn
adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min = _AdMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 9),
    _AdMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min_Type()
)
adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min.setStatus("current")
_AdMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min_Object = MibTableColumn
adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min = _AdMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 10),
    _AdMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min_Type()
)
adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min.setStatus("current")
_AdMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min_Object = MibTableColumn
adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min = _AdMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 11),
    _AdMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min_Type()
)
adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min.setStatus("current")
_AdMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min_Object = MibTableColumn
adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min = _AdMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 12),
    _AdMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min_Type()
)
adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min.setStatus("current")
_AdMefPerCosPerUniPhCurTimeElapsed1Day_Type = HCPerfTimeElapsed
_AdMefPerCosPerUniPhCurTimeElapsed1Day_Object = MibTableColumn
adMefPerCosPerUniPhCurTimeElapsed1Day = _AdMefPerCosPerUniPhCurTimeElapsed1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 13),
    _AdMefPerCosPerUniPhCurTimeElapsed1Day_Type()
)
adMefPerCosPerUniPhCurTimeElapsed1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurTimeElapsed1Day.setStatus("current")
_AdMefPerCosPerUniPhCurValidIntervals1Day_Type = HCPerfValidIntervals
_AdMefPerCosPerUniPhCurValidIntervals1Day_Object = MibTableColumn
adMefPerCosPerUniPhCurValidIntervals1Day = _AdMefPerCosPerUniPhCurValidIntervals1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 14),
    _AdMefPerCosPerUniPhCurValidIntervals1Day_Type()
)
adMefPerCosPerUniPhCurValidIntervals1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurValidIntervals1Day.setStatus("current")
_AdMefPerCosPerUniPhCurInvalidIntervals1Day_Type = HCPerfInvalidIntervals
_AdMefPerCosPerUniPhCurInvalidIntervals1Day_Object = MibTableColumn
adMefPerCosPerUniPhCurInvalidIntervals1Day = _AdMefPerCosPerUniPhCurInvalidIntervals1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 15),
    _AdMefPerCosPerUniPhCurInvalidIntervals1Day_Type()
)
adMefPerCosPerUniPhCurInvalidIntervals1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurInvalidIntervals1Day.setStatus("current")
_AdMefPerCosPerUniPhCurIngressGreenOctets1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurIngressGreenOctets1Day_Object = MibTableColumn
adMefPerCosPerUniPhCurIngressGreenOctets1Day = _AdMefPerCosPerUniPhCurIngressGreenOctets1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 16),
    _AdMefPerCosPerUniPhCurIngressGreenOctets1Day_Type()
)
adMefPerCosPerUniPhCurIngressGreenOctets1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurIngressGreenOctets1Day.setStatus("current")
_AdMefPerCosPerUniPhCurIngressGreenFrames1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurIngressGreenFrames1Day_Object = MibTableColumn
adMefPerCosPerUniPhCurIngressGreenFrames1Day = _AdMefPerCosPerUniPhCurIngressGreenFrames1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 17),
    _AdMefPerCosPerUniPhCurIngressGreenFrames1Day_Type()
)
adMefPerCosPerUniPhCurIngressGreenFrames1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurIngressGreenFrames1Day.setStatus("current")
_AdMefPerCosPerUniPhCurEgressGreenOctets1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurEgressGreenOctets1Day_Object = MibTableColumn
adMefPerCosPerUniPhCurEgressGreenOctets1Day = _AdMefPerCosPerUniPhCurEgressGreenOctets1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 18),
    _AdMefPerCosPerUniPhCurEgressGreenOctets1Day_Type()
)
adMefPerCosPerUniPhCurEgressGreenOctets1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurEgressGreenOctets1Day.setStatus("current")
_AdMefPerCosPerUniPhCurEgressGreenFrames1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurEgressGreenFrames1Day_Object = MibTableColumn
adMefPerCosPerUniPhCurEgressGreenFrames1Day = _AdMefPerCosPerUniPhCurEgressGreenFrames1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 19),
    _AdMefPerCosPerUniPhCurEgressGreenFrames1Day_Type()
)
adMefPerCosPerUniPhCurEgressGreenFrames1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurEgressGreenFrames1Day.setStatus("current")
_AdMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day_Object = MibTableColumn
adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day = _AdMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 20),
    _AdMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day_Type()
)
adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day.setStatus("current")
_AdMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day_Object = MibTableColumn
adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day = _AdMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 21),
    _AdMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day_Type()
)
adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day.setStatus("current")
_AdMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day_Object = MibTableColumn
adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day = _AdMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 22),
    _AdMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day_Type()
)
adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day.setStatus("current")
_AdMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day_Object = MibTableColumn
adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day = _AdMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 23),
    _AdMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day_Type()
)
adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day.setStatus("current")
_AdMefPerCosPerUniPh15MinIntervalTable_Object = MibTable
adMefPerCosPerUniPh15MinIntervalTable = _AdMefPerCosPerUniPh15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2)
)
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh15MinIntervalTable.setStatus("current")
_AdMefPerCosPerUniPh15MinIntervalEntry_Object = MibTableRow
adMefPerCosPerUniPh15MinIntervalEntry = _AdMefPerCosPerUniPh15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1)
)
adMefPerCosPerUniPh15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinQueueNumber"),
    (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh15MinIntervalEntry.setStatus("current")


class _AdMefPerCosPerUniPh15MinQueueNumber_Type(Unsigned32):
    """Custom type adMefPerCosPerUniPh15MinQueueNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdMefPerCosPerUniPh15MinQueueNumber_Type.__name__ = "Unsigned32"
_AdMefPerCosPerUniPh15MinQueueNumber_Object = MibTableColumn
adMefPerCosPerUniPh15MinQueueNumber = _AdMefPerCosPerUniPh15MinQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 1),
    _AdMefPerCosPerUniPh15MinQueueNumber_Type()
)
adMefPerCosPerUniPh15MinQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh15MinQueueNumber.setStatus("current")


class _AdMefPerCosPerUniPh15MinIntervalNumber_Type(Integer32):
    """Custom type adMefPerCosPerUniPh15MinIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdMefPerCosPerUniPh15MinIntervalNumber_Type.__name__ = "Integer32"
_AdMefPerCosPerUniPh15MinIntervalNumber_Object = MibTableColumn
adMefPerCosPerUniPh15MinIntervalNumber = _AdMefPerCosPerUniPh15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 2),
    _AdMefPerCosPerUniPh15MinIntervalNumber_Type()
)
adMefPerCosPerUniPh15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh15MinIntervalNumber.setStatus("current")
_AdMefPerCosPerUniPh15MinIngressGreenOctets_Type = HCPerfIntervalCount
_AdMefPerCosPerUniPh15MinIngressGreenOctets_Object = MibTableColumn
adMefPerCosPerUniPh15MinIngressGreenOctets = _AdMefPerCosPerUniPh15MinIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 3),
    _AdMefPerCosPerUniPh15MinIngressGreenOctets_Type()
)
adMefPerCosPerUniPh15MinIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh15MinIngressGreenOctets.setStatus("current")
_AdMefPerCosPerUniPh15MinIngressGreenFrames_Type = HCPerfIntervalCount
_AdMefPerCosPerUniPh15MinIngressGreenFrames_Object = MibTableColumn
adMefPerCosPerUniPh15MinIngressGreenFrames = _AdMefPerCosPerUniPh15MinIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 4),
    _AdMefPerCosPerUniPh15MinIngressGreenFrames_Type()
)
adMefPerCosPerUniPh15MinIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh15MinIngressGreenFrames.setStatus("current")
_AdMefPerCosPerUniPh15MinEgressGreenOctets_Type = HCPerfIntervalCount
_AdMefPerCosPerUniPh15MinEgressGreenOctets_Object = MibTableColumn
adMefPerCosPerUniPh15MinEgressGreenOctets = _AdMefPerCosPerUniPh15MinEgressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 5),
    _AdMefPerCosPerUniPh15MinEgressGreenOctets_Type()
)
adMefPerCosPerUniPh15MinEgressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh15MinEgressGreenOctets.setStatus("current")
_AdMefPerCosPerUniPh15MinEgressGreenFrames_Type = HCPerfIntervalCount
_AdMefPerCosPerUniPh15MinEgressGreenFrames_Object = MibTableColumn
adMefPerCosPerUniPh15MinEgressGreenFrames = _AdMefPerCosPerUniPh15MinEgressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 6),
    _AdMefPerCosPerUniPh15MinEgressGreenFrames_Type()
)
adMefPerCosPerUniPh15MinEgressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh15MinEgressGreenFrames.setStatus("current")
_AdMefPerCosPerUniPh15MinIngressGreenFrameDiscards_Type = HCPerfIntervalCount
_AdMefPerCosPerUniPh15MinIngressGreenFrameDiscards_Object = MibTableColumn
adMefPerCosPerUniPh15MinIngressGreenFrameDiscards = _AdMefPerCosPerUniPh15MinIngressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 7),
    _AdMefPerCosPerUniPh15MinIngressGreenFrameDiscards_Type()
)
adMefPerCosPerUniPh15MinIngressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh15MinIngressGreenFrameDiscards.setStatus("current")
_AdMefPerCosPerUniPh15MinEgressGreenFrameDiscards_Type = HCPerfIntervalCount
_AdMefPerCosPerUniPh15MinEgressGreenFrameDiscards_Object = MibTableColumn
adMefPerCosPerUniPh15MinEgressGreenFrameDiscards = _AdMefPerCosPerUniPh15MinEgressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 8),
    _AdMefPerCosPerUniPh15MinEgressGreenFrameDiscards_Type()
)
adMefPerCosPerUniPh15MinEgressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh15MinEgressGreenFrameDiscards.setStatus("current")
_AdMefPerCosPerUniPh15MinIngressGreenOctetDiscards_Type = HCPerfIntervalCount
_AdMefPerCosPerUniPh15MinIngressGreenOctetDiscards_Object = MibTableColumn
adMefPerCosPerUniPh15MinIngressGreenOctetDiscards = _AdMefPerCosPerUniPh15MinIngressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 9),
    _AdMefPerCosPerUniPh15MinIngressGreenOctetDiscards_Type()
)
adMefPerCosPerUniPh15MinIngressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh15MinIngressGreenOctetDiscards.setStatus("current")
_AdMefPerCosPerUniPh15MinEgressGreenOctetDiscards_Type = HCPerfIntervalCount
_AdMefPerCosPerUniPh15MinEgressGreenOctetDiscards_Object = MibTableColumn
adMefPerCosPerUniPh15MinEgressGreenOctetDiscards = _AdMefPerCosPerUniPh15MinEgressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 10),
    _AdMefPerCosPerUniPh15MinEgressGreenOctetDiscards_Type()
)
adMefPerCosPerUniPh15MinEgressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh15MinEgressGreenOctetDiscards.setStatus("current")
_AdMefPerCosPerUniPh1DayIntervalTable_Object = MibTable
adMefPerCosPerUniPh1DayIntervalTable = _AdMefPerCosPerUniPh1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3)
)
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh1DayIntervalTable.setStatus("current")
_AdMefPerCosPerUniPh1DayIntervalEntry_Object = MibTableRow
adMefPerCosPerUniPh1DayIntervalEntry = _AdMefPerCosPerUniPh1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1)
)
adMefPerCosPerUniPh1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayQueueNumber"),
    (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh1DayIntervalEntry.setStatus("current")


class _AdMefPerCosPerUniPh1DayQueueNumber_Type(Unsigned32):
    """Custom type adMefPerCosPerUniPh1DayQueueNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdMefPerCosPerUniPh1DayQueueNumber_Type.__name__ = "Unsigned32"
_AdMefPerCosPerUniPh1DayQueueNumber_Object = MibTableColumn
adMefPerCosPerUniPh1DayQueueNumber = _AdMefPerCosPerUniPh1DayQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 1),
    _AdMefPerCosPerUniPh1DayQueueNumber_Type()
)
adMefPerCosPerUniPh1DayQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh1DayQueueNumber.setStatus("current")


class _AdMefPerCosPerUniPh1DayIntervalNumber_Type(Integer32):
    """Custom type adMefPerCosPerUniPh1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AdMefPerCosPerUniPh1DayIntervalNumber_Type.__name__ = "Integer32"
_AdMefPerCosPerUniPh1DayIntervalNumber_Object = MibTableColumn
adMefPerCosPerUniPh1DayIntervalNumber = _AdMefPerCosPerUniPh1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 2),
    _AdMefPerCosPerUniPh1DayIntervalNumber_Type()
)
adMefPerCosPerUniPh1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh1DayIntervalNumber.setStatus("current")
_AdMefPerCosPerUniPh1DayIngressGreenOctets_Type = HCPerfTotalCount
_AdMefPerCosPerUniPh1DayIngressGreenOctets_Object = MibTableColumn
adMefPerCosPerUniPh1DayIngressGreenOctets = _AdMefPerCosPerUniPh1DayIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 3),
    _AdMefPerCosPerUniPh1DayIngressGreenOctets_Type()
)
adMefPerCosPerUniPh1DayIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh1DayIngressGreenOctets.setStatus("current")
_AdMefPerCosPerUniPh1DayIngressGreenFrames_Type = HCPerfTotalCount
_AdMefPerCosPerUniPh1DayIngressGreenFrames_Object = MibTableColumn
adMefPerCosPerUniPh1DayIngressGreenFrames = _AdMefPerCosPerUniPh1DayIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 4),
    _AdMefPerCosPerUniPh1DayIngressGreenFrames_Type()
)
adMefPerCosPerUniPh1DayIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh1DayIngressGreenFrames.setStatus("current")
_AdMefPerCosPerUniPh1DayEgressGreenOctets_Type = HCPerfTotalCount
_AdMefPerCosPerUniPh1DayEgressGreenOctets_Object = MibTableColumn
adMefPerCosPerUniPh1DayEgressGreenOctets = _AdMefPerCosPerUniPh1DayEgressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 5),
    _AdMefPerCosPerUniPh1DayEgressGreenOctets_Type()
)
adMefPerCosPerUniPh1DayEgressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh1DayEgressGreenOctets.setStatus("current")
_AdMefPerCosPerUniPh1DayEgressGreenFrames_Type = HCPerfTotalCount
_AdMefPerCosPerUniPh1DayEgressGreenFrames_Object = MibTableColumn
adMefPerCosPerUniPh1DayEgressGreenFrames = _AdMefPerCosPerUniPh1DayEgressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 6),
    _AdMefPerCosPerUniPh1DayEgressGreenFrames_Type()
)
adMefPerCosPerUniPh1DayEgressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh1DayEgressGreenFrames.setStatus("current")
_AdMefPerCosPerUniPh1DayIngressGreenFrameDiscards_Type = HCPerfTotalCount
_AdMefPerCosPerUniPh1DayIngressGreenFrameDiscards_Object = MibTableColumn
adMefPerCosPerUniPh1DayIngressGreenFrameDiscards = _AdMefPerCosPerUniPh1DayIngressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 7),
    _AdMefPerCosPerUniPh1DayIngressGreenFrameDiscards_Type()
)
adMefPerCosPerUniPh1DayIngressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh1DayIngressGreenFrameDiscards.setStatus("current")
_AdMefPerCosPerUniPh1DayEgressGreenFrameDiscards_Type = HCPerfTotalCount
_AdMefPerCosPerUniPh1DayEgressGreenFrameDiscards_Object = MibTableColumn
adMefPerCosPerUniPh1DayEgressGreenFrameDiscards = _AdMefPerCosPerUniPh1DayEgressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 8),
    _AdMefPerCosPerUniPh1DayEgressGreenFrameDiscards_Type()
)
adMefPerCosPerUniPh1DayEgressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh1DayEgressGreenFrameDiscards.setStatus("current")
_AdMefPerCosPerUniPh1DayIngressGreenOctetDiscards_Type = HCPerfTotalCount
_AdMefPerCosPerUniPh1DayIngressGreenOctetDiscards_Object = MibTableColumn
adMefPerCosPerUniPh1DayIngressGreenOctetDiscards = _AdMefPerCosPerUniPh1DayIngressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 9),
    _AdMefPerCosPerUniPh1DayIngressGreenOctetDiscards_Type()
)
adMefPerCosPerUniPh1DayIngressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh1DayIngressGreenOctetDiscards.setStatus("current")
_AdMefPerCosPerUniPh1DayEgressGreenOctetDiscards_Type = HCPerfTotalCount
_AdMefPerCosPerUniPh1DayEgressGreenOctetDiscards_Object = MibTableColumn
adMefPerCosPerUniPh1DayEgressGreenOctetDiscards = _AdMefPerCosPerUniPh1DayEgressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 10),
    _AdMefPerCosPerUniPh1DayEgressGreenOctetDiscards_Type()
)
adMefPerCosPerUniPh1DayEgressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh1DayEgressGreenOctetDiscards.setStatus("current")
_AdGenAosMefPerCosPerUniPerfHistoryConformance_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerUniPerfHistoryConformance = _AdGenAosMefPerCosPerUniPerfHistoryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21)
)
_AdGenAosMefPerCosPerUniPerfHistoryGroups_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerUniPerfHistoryGroups = _AdGenAosMefPerCosPerUniPerfHistoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 1)
)
_AdGenAosMefPerCosPerUniPerfHistoryCompliances_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerUniPerfHistoryCompliances = _AdGenAosMefPerCosPerUniPerfHistoryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 2)
)

# Managed Objects groups

adMefPerCosPerUniPhCurGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 1, 1)
)
adMefPerCosPerUniPhCurGroup.setObjects(
      *(("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurTimeElapsed15Min"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurValidIntervals15Min"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurInvalidIntervals15Min"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenOctets15Min"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenFrames15Min"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenOctets15Min"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenFrames15Min"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurTimeElapsed1Day"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurValidIntervals1Day"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurInvalidIntervals1Day"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenOctets1Day"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenFrames1Day"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenOctets1Day"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenFrames1Day"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day"))
)
if mibBuilder.loadTexts:
    adMefPerCosPerUniPhCurGroup.setStatus("current")

adMefPerCosPerUniPh15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 1, 2)
)
adMefPerCosPerUniPh15MinIntervalGroup.setObjects(
      *(("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIngressGreenOctets"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIngressGreenFrames"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinEgressGreenOctets"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinEgressGreenFrames"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIngressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinEgressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIngressGreenOctetDiscards"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinEgressGreenOctetDiscards"))
)
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh15MinIntervalGroup.setStatus("current")

adMefPerCosPerUniPh1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 1, 3)
)
adMefPerCosPerUniPh1DayIntervalGroup.setObjects(
      *(("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIngressGreenOctets"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIngressGreenFrames"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayEgressGreenOctets"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayEgressGreenFrames"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIngressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayEgressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIngressGreenOctetDiscards"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayEgressGreenOctetDiscards"))
)
if mibBuilder.loadTexts:
    adMefPerCosPerUniPh1DayIntervalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAosMefPerCosPerUniPerfHistoryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAosMefPerCosPerUniPerfHistoryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB",
    **{"adGenAosMefPerCosPerUniPerfHistory": adGenAosMefPerCosPerUniPerfHistory,
       "adMefPerCosPerUniPhCurTable": adMefPerCosPerUniPhCurTable,
       "adMefPerCosPerUniPhCurEntry": adMefPerCosPerUniPhCurEntry,
       "adMefPerCosPerUniPhCurQueueNumber": adMefPerCosPerUniPhCurQueueNumber,
       "adMefPerCosPerUniPhCurTimeElapsed15Min": adMefPerCosPerUniPhCurTimeElapsed15Min,
       "adMefPerCosPerUniPhCurValidIntervals15Min": adMefPerCosPerUniPhCurValidIntervals15Min,
       "adMefPerCosPerUniPhCurInvalidIntervals15Min": adMefPerCosPerUniPhCurInvalidIntervals15Min,
       "adMefPerCosPerUniPhCurIngressGreenOctets15Min": adMefPerCosPerUniPhCurIngressGreenOctets15Min,
       "adMefPerCosPerUniPhCurIngressGreenFrames15Min": adMefPerCosPerUniPhCurIngressGreenFrames15Min,
       "adMefPerCosPerUniPhCurEgressGreenOctets15Min": adMefPerCosPerUniPhCurEgressGreenOctets15Min,
       "adMefPerCosPerUniPhCurEgressGreenFrames15Min": adMefPerCosPerUniPhCurEgressGreenFrames15Min,
       "adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min": adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min,
       "adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min": adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min,
       "adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min": adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min,
       "adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min": adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min,
       "adMefPerCosPerUniPhCurTimeElapsed1Day": adMefPerCosPerUniPhCurTimeElapsed1Day,
       "adMefPerCosPerUniPhCurValidIntervals1Day": adMefPerCosPerUniPhCurValidIntervals1Day,
       "adMefPerCosPerUniPhCurInvalidIntervals1Day": adMefPerCosPerUniPhCurInvalidIntervals1Day,
       "adMefPerCosPerUniPhCurIngressGreenOctets1Day": adMefPerCosPerUniPhCurIngressGreenOctets1Day,
       "adMefPerCosPerUniPhCurIngressGreenFrames1Day": adMefPerCosPerUniPhCurIngressGreenFrames1Day,
       "adMefPerCosPerUniPhCurEgressGreenOctets1Day": adMefPerCosPerUniPhCurEgressGreenOctets1Day,
       "adMefPerCosPerUniPhCurEgressGreenFrames1Day": adMefPerCosPerUniPhCurEgressGreenFrames1Day,
       "adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day": adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day,
       "adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day": adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day,
       "adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day": adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day,
       "adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day": adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day,
       "adMefPerCosPerUniPh15MinIntervalTable": adMefPerCosPerUniPh15MinIntervalTable,
       "adMefPerCosPerUniPh15MinIntervalEntry": adMefPerCosPerUniPh15MinIntervalEntry,
       "adMefPerCosPerUniPh15MinQueueNumber": adMefPerCosPerUniPh15MinQueueNumber,
       "adMefPerCosPerUniPh15MinIntervalNumber": adMefPerCosPerUniPh15MinIntervalNumber,
       "adMefPerCosPerUniPh15MinIngressGreenOctets": adMefPerCosPerUniPh15MinIngressGreenOctets,
       "adMefPerCosPerUniPh15MinIngressGreenFrames": adMefPerCosPerUniPh15MinIngressGreenFrames,
       "adMefPerCosPerUniPh15MinEgressGreenOctets": adMefPerCosPerUniPh15MinEgressGreenOctets,
       "adMefPerCosPerUniPh15MinEgressGreenFrames": adMefPerCosPerUniPh15MinEgressGreenFrames,
       "adMefPerCosPerUniPh15MinIngressGreenFrameDiscards": adMefPerCosPerUniPh15MinIngressGreenFrameDiscards,
       "adMefPerCosPerUniPh15MinEgressGreenFrameDiscards": adMefPerCosPerUniPh15MinEgressGreenFrameDiscards,
       "adMefPerCosPerUniPh15MinIngressGreenOctetDiscards": adMefPerCosPerUniPh15MinIngressGreenOctetDiscards,
       "adMefPerCosPerUniPh15MinEgressGreenOctetDiscards": adMefPerCosPerUniPh15MinEgressGreenOctetDiscards,
       "adMefPerCosPerUniPh1DayIntervalTable": adMefPerCosPerUniPh1DayIntervalTable,
       "adMefPerCosPerUniPh1DayIntervalEntry": adMefPerCosPerUniPh1DayIntervalEntry,
       "adMefPerCosPerUniPh1DayQueueNumber": adMefPerCosPerUniPh1DayQueueNumber,
       "adMefPerCosPerUniPh1DayIntervalNumber": adMefPerCosPerUniPh1DayIntervalNumber,
       "adMefPerCosPerUniPh1DayIngressGreenOctets": adMefPerCosPerUniPh1DayIngressGreenOctets,
       "adMefPerCosPerUniPh1DayIngressGreenFrames": adMefPerCosPerUniPh1DayIngressGreenFrames,
       "adMefPerCosPerUniPh1DayEgressGreenOctets": adMefPerCosPerUniPh1DayEgressGreenOctets,
       "adMefPerCosPerUniPh1DayEgressGreenFrames": adMefPerCosPerUniPh1DayEgressGreenFrames,
       "adMefPerCosPerUniPh1DayIngressGreenFrameDiscards": adMefPerCosPerUniPh1DayIngressGreenFrameDiscards,
       "adMefPerCosPerUniPh1DayEgressGreenFrameDiscards": adMefPerCosPerUniPh1DayEgressGreenFrameDiscards,
       "adMefPerCosPerUniPh1DayIngressGreenOctetDiscards": adMefPerCosPerUniPh1DayIngressGreenOctetDiscards,
       "adMefPerCosPerUniPh1DayEgressGreenOctetDiscards": adMefPerCosPerUniPh1DayEgressGreenOctetDiscards,
       "adGenAosMefPerCosPerUniPerfHistoryConformance": adGenAosMefPerCosPerUniPerfHistoryConformance,
       "adGenAosMefPerCosPerUniPerfHistoryGroups": adGenAosMefPerCosPerUniPerfHistoryGroups,
       "adMefPerCosPerUniPhCurGroup": adMefPerCosPerUniPhCurGroup,
       "adMefPerCosPerUniPh15MinIntervalGroup": adMefPerCosPerUniPh15MinIntervalGroup,
       "adMefPerCosPerUniPh1DayIntervalGroup": adMefPerCosPerUniPh1DayIntervalGroup,
       "adGenAosMefPerCosPerUniPerfHistoryCompliances": adGenAosMefPerCosPerUniPerfHistoryCompliances,
       "adGenAosMefPerCosPerUniPerfHistoryCompliance": adGenAosMefPerCosPerUniPerfHistoryCompliance,
       "adGenAosMefPerCosPerUniPerfHistoryMib": adGenAosMefPerCosPerUniPerfHistoryMib}
)
