# SNMP MIB module (ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:33 2024
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

adGenAosMefPerCosPerEvcPerfHistoryMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 4)
)
adGenAosMefPerCosPerEvcPerfHistoryMib.setRevisions(
        ("2014-09-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAosMefPerCosPerEvcPerfHistory_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerEvcPerfHistory = _AdGenAosMefPerCosPerEvcPerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4)
)
_AdMefPerCosPerEvcPhCurTable_Object = MibTable
adMefPerCosPerEvcPhCurTable = _AdMefPerCosPerEvcPhCurTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1)
)
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurTable.setStatus("current")
_AdMefPerCosPerEvcPhCurEntry_Object = MibTableRow
adMefPerCosPerEvcPhCurEntry = _AdMefPerCosPerEvcPhCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1)
)
adMefPerCosPerEvcPhCurEntry.setIndexNames(
    (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEvcNameFixedLen"),
    (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurQueueNumber"),
)
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurEntry.setStatus("current")


class _AdMefPerCosPerEvcPhCurEvcNameFixedLen_Type(OctetString):
    """Custom type adMefPerCosPerEvcPhCurEvcNameFixedLen based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )


_AdMefPerCosPerEvcPhCurEvcNameFixedLen_Type.__name__ = "OctetString"
_AdMefPerCosPerEvcPhCurEvcNameFixedLen_Object = MibTableColumn
adMefPerCosPerEvcPhCurEvcNameFixedLen = _AdMefPerCosPerEvcPhCurEvcNameFixedLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 1),
    _AdMefPerCosPerEvcPhCurEvcNameFixedLen_Type()
)
adMefPerCosPerEvcPhCurEvcNameFixedLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurEvcNameFixedLen.setStatus("current")


class _AdMefPerCosPerEvcPhCurQueueNumber_Type(Unsigned32):
    """Custom type adMefPerCosPerEvcPhCurQueueNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdMefPerCosPerEvcPhCurQueueNumber_Type.__name__ = "Unsigned32"
_AdMefPerCosPerEvcPhCurQueueNumber_Object = MibTableColumn
adMefPerCosPerEvcPhCurQueueNumber = _AdMefPerCosPerEvcPhCurQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 2),
    _AdMefPerCosPerEvcPhCurQueueNumber_Type()
)
adMefPerCosPerEvcPhCurQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurQueueNumber.setStatus("current")
_AdMefPerCosPerEvcPhCurTimeElapsed15Min_Type = HCPerfTimeElapsed
_AdMefPerCosPerEvcPhCurTimeElapsed15Min_Object = MibTableColumn
adMefPerCosPerEvcPhCurTimeElapsed15Min = _AdMefPerCosPerEvcPhCurTimeElapsed15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 3),
    _AdMefPerCosPerEvcPhCurTimeElapsed15Min_Type()
)
adMefPerCosPerEvcPhCurTimeElapsed15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurTimeElapsed15Min.setStatus("current")
_AdMefPerCosPerEvcPhCurValidIntervals15Min_Type = HCPerfValidIntervals
_AdMefPerCosPerEvcPhCurValidIntervals15Min_Object = MibTableColumn
adMefPerCosPerEvcPhCurValidIntervals15Min = _AdMefPerCosPerEvcPhCurValidIntervals15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 4),
    _AdMefPerCosPerEvcPhCurValidIntervals15Min_Type()
)
adMefPerCosPerEvcPhCurValidIntervals15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurValidIntervals15Min.setStatus("current")
_AdMefPerCosPerEvcPhCurInvalidIntervals15Min_Type = HCPerfInvalidIntervals
_AdMefPerCosPerEvcPhCurInvalidIntervals15Min_Object = MibTableColumn
adMefPerCosPerEvcPhCurInvalidIntervals15Min = _AdMefPerCosPerEvcPhCurInvalidIntervals15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 5),
    _AdMefPerCosPerEvcPhCurInvalidIntervals15Min_Type()
)
adMefPerCosPerEvcPhCurInvalidIntervals15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurInvalidIntervals15Min.setStatus("current")
_AdMefPerCosPerEvcPhCurIngressGreenOctets15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurIngressGreenOctets15Min_Object = MibTableColumn
adMefPerCosPerEvcPhCurIngressGreenOctets15Min = _AdMefPerCosPerEvcPhCurIngressGreenOctets15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 6),
    _AdMefPerCosPerEvcPhCurIngressGreenOctets15Min_Type()
)
adMefPerCosPerEvcPhCurIngressGreenOctets15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurIngressGreenOctets15Min.setStatus("current")
_AdMefPerCosPerEvcPhCurIngressGreenFrames15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurIngressGreenFrames15Min_Object = MibTableColumn
adMefPerCosPerEvcPhCurIngressGreenFrames15Min = _AdMefPerCosPerEvcPhCurIngressGreenFrames15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 7),
    _AdMefPerCosPerEvcPhCurIngressGreenFrames15Min_Type()
)
adMefPerCosPerEvcPhCurIngressGreenFrames15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurIngressGreenFrames15Min.setStatus("current")
_AdMefPerCosPerEvcPhCurEgressGreenOctets15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurEgressGreenOctets15Min_Object = MibTableColumn
adMefPerCosPerEvcPhCurEgressGreenOctets15Min = _AdMefPerCosPerEvcPhCurEgressGreenOctets15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 8),
    _AdMefPerCosPerEvcPhCurEgressGreenOctets15Min_Type()
)
adMefPerCosPerEvcPhCurEgressGreenOctets15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurEgressGreenOctets15Min.setStatus("current")
_AdMefPerCosPerEvcPhCurEgressGreenFrames15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurEgressGreenFrames15Min_Object = MibTableColumn
adMefPerCosPerEvcPhCurEgressGreenFrames15Min = _AdMefPerCosPerEvcPhCurEgressGreenFrames15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 9),
    _AdMefPerCosPerEvcPhCurEgressGreenFrames15Min_Type()
)
adMefPerCosPerEvcPhCurEgressGreenFrames15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurEgressGreenFrames15Min.setStatus("current")
_AdMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min_Object = MibTableColumn
adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min = _AdMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 10),
    _AdMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min_Type()
)
adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min.setStatus("current")
_AdMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min_Object = MibTableColumn
adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min = _AdMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 11),
    _AdMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min_Type()
)
adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min.setStatus("current")
_AdMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min_Object = MibTableColumn
adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min = _AdMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 12),
    _AdMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min_Type()
)
adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min.setStatus("current")
_AdMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min_Object = MibTableColumn
adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min = _AdMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 13),
    _AdMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min_Type()
)
adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min.setStatus("current")
_AdMefPerCosPerEvcPhCurTimeElapsed1Day_Type = HCPerfTimeElapsed
_AdMefPerCosPerEvcPhCurTimeElapsed1Day_Object = MibTableColumn
adMefPerCosPerEvcPhCurTimeElapsed1Day = _AdMefPerCosPerEvcPhCurTimeElapsed1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 14),
    _AdMefPerCosPerEvcPhCurTimeElapsed1Day_Type()
)
adMefPerCosPerEvcPhCurTimeElapsed1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurTimeElapsed1Day.setStatus("current")
_AdMefPerCosPerEvcPhCurValidIntervals1Day_Type = HCPerfValidIntervals
_AdMefPerCosPerEvcPhCurValidIntervals1Day_Object = MibTableColumn
adMefPerCosPerEvcPhCurValidIntervals1Day = _AdMefPerCosPerEvcPhCurValidIntervals1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 15),
    _AdMefPerCosPerEvcPhCurValidIntervals1Day_Type()
)
adMefPerCosPerEvcPhCurValidIntervals1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurValidIntervals1Day.setStatus("current")
_AdMefPerCosPerEvcPhCurInvalidIntervals1Day_Type = HCPerfInvalidIntervals
_AdMefPerCosPerEvcPhCurInvalidIntervals1Day_Object = MibTableColumn
adMefPerCosPerEvcPhCurInvalidIntervals1Day = _AdMefPerCosPerEvcPhCurInvalidIntervals1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 16),
    _AdMefPerCosPerEvcPhCurInvalidIntervals1Day_Type()
)
adMefPerCosPerEvcPhCurInvalidIntervals1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurInvalidIntervals1Day.setStatus("current")
_AdMefPerCosPerEvcPhCurIngressGreenOctets1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurIngressGreenOctets1Day_Object = MibTableColumn
adMefPerCosPerEvcPhCurIngressGreenOctets1Day = _AdMefPerCosPerEvcPhCurIngressGreenOctets1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 17),
    _AdMefPerCosPerEvcPhCurIngressGreenOctets1Day_Type()
)
adMefPerCosPerEvcPhCurIngressGreenOctets1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurIngressGreenOctets1Day.setStatus("current")
_AdMefPerCosPerEvcPhCurIngressGreenFrames1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurIngressGreenFrames1Day_Object = MibTableColumn
adMefPerCosPerEvcPhCurIngressGreenFrames1Day = _AdMefPerCosPerEvcPhCurIngressGreenFrames1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 18),
    _AdMefPerCosPerEvcPhCurIngressGreenFrames1Day_Type()
)
adMefPerCosPerEvcPhCurIngressGreenFrames1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurIngressGreenFrames1Day.setStatus("current")
_AdMefPerCosPerEvcPhCurEgressGreenOctets1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurEgressGreenOctets1Day_Object = MibTableColumn
adMefPerCosPerEvcPhCurEgressGreenOctets1Day = _AdMefPerCosPerEvcPhCurEgressGreenOctets1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 19),
    _AdMefPerCosPerEvcPhCurEgressGreenOctets1Day_Type()
)
adMefPerCosPerEvcPhCurEgressGreenOctets1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurEgressGreenOctets1Day.setStatus("current")
_AdMefPerCosPerEvcPhCurEgressGreenFrames1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurEgressGreenFrames1Day_Object = MibTableColumn
adMefPerCosPerEvcPhCurEgressGreenFrames1Day = _AdMefPerCosPerEvcPhCurEgressGreenFrames1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 20),
    _AdMefPerCosPerEvcPhCurEgressGreenFrames1Day_Type()
)
adMefPerCosPerEvcPhCurEgressGreenFrames1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurEgressGreenFrames1Day.setStatus("current")
_AdMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day_Object = MibTableColumn
adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day = _AdMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 21),
    _AdMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day_Type()
)
adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day.setStatus("current")
_AdMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day_Object = MibTableColumn
adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day = _AdMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 22),
    _AdMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day_Type()
)
adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day.setStatus("current")
_AdMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day_Object = MibTableColumn
adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day = _AdMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 23),
    _AdMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day_Type()
)
adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day.setStatus("current")
_AdMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day_Object = MibTableColumn
adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day = _AdMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 24),
    _AdMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day_Type()
)
adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day.setStatus("current")
_AdMefPerCosPerEvcPh15MinIntervalTable_Object = MibTable
adMefPerCosPerEvcPh15MinIntervalTable = _AdMefPerCosPerEvcPh15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2)
)
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh15MinIntervalTable.setStatus("current")
_AdMefPerCosPerEvcPh15MinIntervalEntry_Object = MibTableRow
adMefPerCosPerEvcPh15MinIntervalEntry = _AdMefPerCosPerEvcPh15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1)
)
adMefPerCosPerEvcPh15MinIntervalEntry.setIndexNames(
    (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEvcNameFixedLen"),
    (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinQueueNumber"),
    (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh15MinIntervalEntry.setStatus("current")


class _AdMefPerCosPerEvcPh15MinEvcNameFixedLen_Type(OctetString):
    """Custom type adMefPerCosPerEvcPh15MinEvcNameFixedLen based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )


_AdMefPerCosPerEvcPh15MinEvcNameFixedLen_Type.__name__ = "OctetString"
_AdMefPerCosPerEvcPh15MinEvcNameFixedLen_Object = MibTableColumn
adMefPerCosPerEvcPh15MinEvcNameFixedLen = _AdMefPerCosPerEvcPh15MinEvcNameFixedLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 1),
    _AdMefPerCosPerEvcPh15MinEvcNameFixedLen_Type()
)
adMefPerCosPerEvcPh15MinEvcNameFixedLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh15MinEvcNameFixedLen.setStatus("current")


class _AdMefPerCosPerEvcPh15MinQueueNumber_Type(Unsigned32):
    """Custom type adMefPerCosPerEvcPh15MinQueueNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdMefPerCosPerEvcPh15MinQueueNumber_Type.__name__ = "Unsigned32"
_AdMefPerCosPerEvcPh15MinQueueNumber_Object = MibTableColumn
adMefPerCosPerEvcPh15MinQueueNumber = _AdMefPerCosPerEvcPh15MinQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 2),
    _AdMefPerCosPerEvcPh15MinQueueNumber_Type()
)
adMefPerCosPerEvcPh15MinQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh15MinQueueNumber.setStatus("current")


class _AdMefPerCosPerEvcPh15MinIntervalNumber_Type(Integer32):
    """Custom type adMefPerCosPerEvcPh15MinIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdMefPerCosPerEvcPh15MinIntervalNumber_Type.__name__ = "Integer32"
_AdMefPerCosPerEvcPh15MinIntervalNumber_Object = MibTableColumn
adMefPerCosPerEvcPh15MinIntervalNumber = _AdMefPerCosPerEvcPh15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 3),
    _AdMefPerCosPerEvcPh15MinIntervalNumber_Type()
)
adMefPerCosPerEvcPh15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh15MinIntervalNumber.setStatus("current")
_AdMefPerCosPerEvcPh15MinIngressGreenOctets_Type = HCPerfIntervalCount
_AdMefPerCosPerEvcPh15MinIngressGreenOctets_Object = MibTableColumn
adMefPerCosPerEvcPh15MinIngressGreenOctets = _AdMefPerCosPerEvcPh15MinIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 4),
    _AdMefPerCosPerEvcPh15MinIngressGreenOctets_Type()
)
adMefPerCosPerEvcPh15MinIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh15MinIngressGreenOctets.setStatus("current")
_AdMefPerCosPerEvcPh15MinIngressGreenFrames_Type = HCPerfIntervalCount
_AdMefPerCosPerEvcPh15MinIngressGreenFrames_Object = MibTableColumn
adMefPerCosPerEvcPh15MinIngressGreenFrames = _AdMefPerCosPerEvcPh15MinIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 5),
    _AdMefPerCosPerEvcPh15MinIngressGreenFrames_Type()
)
adMefPerCosPerEvcPh15MinIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh15MinIngressGreenFrames.setStatus("current")
_AdMefPerCosPerEvcPh15MinEgressGreenOctets_Type = HCPerfIntervalCount
_AdMefPerCosPerEvcPh15MinEgressGreenOctets_Object = MibTableColumn
adMefPerCosPerEvcPh15MinEgressGreenOctets = _AdMefPerCosPerEvcPh15MinEgressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 6),
    _AdMefPerCosPerEvcPh15MinEgressGreenOctets_Type()
)
adMefPerCosPerEvcPh15MinEgressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh15MinEgressGreenOctets.setStatus("current")
_AdMefPerCosPerEvcPh15MinEgressGreenFrames_Type = HCPerfIntervalCount
_AdMefPerCosPerEvcPh15MinEgressGreenFrames_Object = MibTableColumn
adMefPerCosPerEvcPh15MinEgressGreenFrames = _AdMefPerCosPerEvcPh15MinEgressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 7),
    _AdMefPerCosPerEvcPh15MinEgressGreenFrames_Type()
)
adMefPerCosPerEvcPh15MinEgressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh15MinEgressGreenFrames.setStatus("current")
_AdMefPerCosPerEvcPh15MinIngressGreenFrameDiscards_Type = HCPerfIntervalCount
_AdMefPerCosPerEvcPh15MinIngressGreenFrameDiscards_Object = MibTableColumn
adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards = _AdMefPerCosPerEvcPh15MinIngressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 8),
    _AdMefPerCosPerEvcPh15MinIngressGreenFrameDiscards_Type()
)
adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards.setStatus("current")
_AdMefPerCosPerEvcPh15MinEgressGreenFrameDiscards_Type = HCPerfIntervalCount
_AdMefPerCosPerEvcPh15MinEgressGreenFrameDiscards_Object = MibTableColumn
adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards = _AdMefPerCosPerEvcPh15MinEgressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 9),
    _AdMefPerCosPerEvcPh15MinEgressGreenFrameDiscards_Type()
)
adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards.setStatus("current")
_AdMefPerCosPerEvcPh15MinIngressGreenOctetDiscards_Type = HCPerfIntervalCount
_AdMefPerCosPerEvcPh15MinIngressGreenOctetDiscards_Object = MibTableColumn
adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards = _AdMefPerCosPerEvcPh15MinIngressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 10),
    _AdMefPerCosPerEvcPh15MinIngressGreenOctetDiscards_Type()
)
adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards.setStatus("current")
_AdMefPerCosPerEvcPh15MinEgressGreenOctetDiscards_Type = HCPerfIntervalCount
_AdMefPerCosPerEvcPh15MinEgressGreenOctetDiscards_Object = MibTableColumn
adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards = _AdMefPerCosPerEvcPh15MinEgressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 11),
    _AdMefPerCosPerEvcPh15MinEgressGreenOctetDiscards_Type()
)
adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards.setStatus("current")
_AdMefPerCosPerEvcPh1DayIntervalTable_Object = MibTable
adMefPerCosPerEvcPh1DayIntervalTable = _AdMefPerCosPerEvcPh1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3)
)
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh1DayIntervalTable.setStatus("current")
_AdMefPerCosPerEvcPh1DayIntervalEntry_Object = MibTableRow
adMefPerCosPerEvcPh1DayIntervalEntry = _AdMefPerCosPerEvcPh1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1)
)
adMefPerCosPerEvcPh1DayIntervalEntry.setIndexNames(
    (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEvcNameFixedLen"),
    (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayQueueNumber"),
    (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh1DayIntervalEntry.setStatus("current")


class _AdMefPerCosPerEvcPh1DayEvcNameFixedLen_Type(OctetString):
    """Custom type adMefPerCosPerEvcPh1DayEvcNameFixedLen based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )


_AdMefPerCosPerEvcPh1DayEvcNameFixedLen_Type.__name__ = "OctetString"
_AdMefPerCosPerEvcPh1DayEvcNameFixedLen_Object = MibTableColumn
adMefPerCosPerEvcPh1DayEvcNameFixedLen = _AdMefPerCosPerEvcPh1DayEvcNameFixedLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 1),
    _AdMefPerCosPerEvcPh1DayEvcNameFixedLen_Type()
)
adMefPerCosPerEvcPh1DayEvcNameFixedLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh1DayEvcNameFixedLen.setStatus("current")


class _AdMefPerCosPerEvcPh1DayQueueNumber_Type(Unsigned32):
    """Custom type adMefPerCosPerEvcPh1DayQueueNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdMefPerCosPerEvcPh1DayQueueNumber_Type.__name__ = "Unsigned32"
_AdMefPerCosPerEvcPh1DayQueueNumber_Object = MibTableColumn
adMefPerCosPerEvcPh1DayQueueNumber = _AdMefPerCosPerEvcPh1DayQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 2),
    _AdMefPerCosPerEvcPh1DayQueueNumber_Type()
)
adMefPerCosPerEvcPh1DayQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh1DayQueueNumber.setStatus("current")


class _AdMefPerCosPerEvcPh1DayIntervalNumber_Type(Integer32):
    """Custom type adMefPerCosPerEvcPh1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AdMefPerCosPerEvcPh1DayIntervalNumber_Type.__name__ = "Integer32"
_AdMefPerCosPerEvcPh1DayIntervalNumber_Object = MibTableColumn
adMefPerCosPerEvcPh1DayIntervalNumber = _AdMefPerCosPerEvcPh1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 3),
    _AdMefPerCosPerEvcPh1DayIntervalNumber_Type()
)
adMefPerCosPerEvcPh1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh1DayIntervalNumber.setStatus("current")
_AdMefPerCosPerEvcPh1DayIngressGreenOctets_Type = HCPerfTotalCount
_AdMefPerCosPerEvcPh1DayIngressGreenOctets_Object = MibTableColumn
adMefPerCosPerEvcPh1DayIngressGreenOctets = _AdMefPerCosPerEvcPh1DayIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 4),
    _AdMefPerCosPerEvcPh1DayIngressGreenOctets_Type()
)
adMefPerCosPerEvcPh1DayIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh1DayIngressGreenOctets.setStatus("current")
_AdMefPerCosPerEvcPh1DayIngressGreenFrames_Type = HCPerfTotalCount
_AdMefPerCosPerEvcPh1DayIngressGreenFrames_Object = MibTableColumn
adMefPerCosPerEvcPh1DayIngressGreenFrames = _AdMefPerCosPerEvcPh1DayIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 5),
    _AdMefPerCosPerEvcPh1DayIngressGreenFrames_Type()
)
adMefPerCosPerEvcPh1DayIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh1DayIngressGreenFrames.setStatus("current")
_AdMefPerCosPerEvcPh1DayEgressGreenOctets_Type = HCPerfTotalCount
_AdMefPerCosPerEvcPh1DayEgressGreenOctets_Object = MibTableColumn
adMefPerCosPerEvcPh1DayEgressGreenOctets = _AdMefPerCosPerEvcPh1DayEgressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 6),
    _AdMefPerCosPerEvcPh1DayEgressGreenOctets_Type()
)
adMefPerCosPerEvcPh1DayEgressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh1DayEgressGreenOctets.setStatus("current")
_AdMefPerCosPerEvcPh1DayEgressGreenFrames_Type = HCPerfTotalCount
_AdMefPerCosPerEvcPh1DayEgressGreenFrames_Object = MibTableColumn
adMefPerCosPerEvcPh1DayEgressGreenFrames = _AdMefPerCosPerEvcPh1DayEgressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 7),
    _AdMefPerCosPerEvcPh1DayEgressGreenFrames_Type()
)
adMefPerCosPerEvcPh1DayEgressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh1DayEgressGreenFrames.setStatus("current")
_AdMefPerCosPerEvcPh1DayIngressGreenFrameDiscards_Type = HCPerfTotalCount
_AdMefPerCosPerEvcPh1DayIngressGreenFrameDiscards_Object = MibTableColumn
adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards = _AdMefPerCosPerEvcPh1DayIngressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 8),
    _AdMefPerCosPerEvcPh1DayIngressGreenFrameDiscards_Type()
)
adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards.setStatus("current")
_AdMefPerCosPerEvcPh1DayEgressGreenFrameDiscards_Type = HCPerfTotalCount
_AdMefPerCosPerEvcPh1DayEgressGreenFrameDiscards_Object = MibTableColumn
adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards = _AdMefPerCosPerEvcPh1DayEgressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 9),
    _AdMefPerCosPerEvcPh1DayEgressGreenFrameDiscards_Type()
)
adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards.setStatus("current")
_AdMefPerCosPerEvcPh1DayIngressGreenOctetDiscards_Type = HCPerfTotalCount
_AdMefPerCosPerEvcPh1DayIngressGreenOctetDiscards_Object = MibTableColumn
adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards = _AdMefPerCosPerEvcPh1DayIngressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 10),
    _AdMefPerCosPerEvcPh1DayIngressGreenOctetDiscards_Type()
)
adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards.setStatus("current")
_AdMefPerCosPerEvcPh1DayEgressGreenOctetDiscards_Type = HCPerfTotalCount
_AdMefPerCosPerEvcPh1DayEgressGreenOctetDiscards_Object = MibTableColumn
adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards = _AdMefPerCosPerEvcPh1DayEgressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 11),
    _AdMefPerCosPerEvcPh1DayEgressGreenOctetDiscards_Type()
)
adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards.setStatus("current")
_AdGenAosMefPerCosPerEvcPerfHistoryConformance_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerEvcPerfHistoryConformance = _AdGenAosMefPerCosPerEvcPerfHistoryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24)
)
_AdGenAosMefPerCosPerEvcPerfHistoryGroups_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerEvcPerfHistoryGroups = _AdGenAosMefPerCosPerEvcPerfHistoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 1)
)
_AdGenAosMefPerCosPerEvcPerfHistoryCompliances_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerEvcPerfHistoryCompliances = _AdGenAosMefPerCosPerEvcPerfHistoryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 2)
)

# Managed Objects groups

adMefPerCosPerEvcPhCurGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 1, 1)
)
adMefPerCosPerEvcPhCurGroup.setObjects(
      *(("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurTimeElapsed15Min"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurValidIntervals15Min"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurInvalidIntervals15Min"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenOctets15Min"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenFrames15Min"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenOctets15Min"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenFrames15Min"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurTimeElapsed1Day"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurValidIntervals1Day"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurInvalidIntervals1Day"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenOctets1Day"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenFrames1Day"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenOctets1Day"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenFrames1Day"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day"))
)
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPhCurGroup.setStatus("current")

adMefPerCosPerEvcPh15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 1, 2)
)
adMefPerCosPerEvcPh15MinIntervalGroup.setObjects(
      *(("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIngressGreenOctets"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIngressGreenFrames"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEgressGreenOctets"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEgressGreenFrames"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards"))
)
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh15MinIntervalGroup.setStatus("current")

adMefPerCosPerEvcPh1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 1, 3)
)
adMefPerCosPerEvcPh1DayIntervalGroup.setObjects(
      *(("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIngressGreenOctets"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIngressGreenFrames"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEgressGreenOctets"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEgressGreenFrames"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards"))
)
if mibBuilder.loadTexts:
    adMefPerCosPerEvcPh1DayIntervalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAosMefPerCosPerEvcPerfHistoryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAosMefPerCosPerEvcPerfHistoryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB",
    **{"adGenAosMefPerCosPerEvcPerfHistory": adGenAosMefPerCosPerEvcPerfHistory,
       "adMefPerCosPerEvcPhCurTable": adMefPerCosPerEvcPhCurTable,
       "adMefPerCosPerEvcPhCurEntry": adMefPerCosPerEvcPhCurEntry,
       "adMefPerCosPerEvcPhCurEvcNameFixedLen": adMefPerCosPerEvcPhCurEvcNameFixedLen,
       "adMefPerCosPerEvcPhCurQueueNumber": adMefPerCosPerEvcPhCurQueueNumber,
       "adMefPerCosPerEvcPhCurTimeElapsed15Min": adMefPerCosPerEvcPhCurTimeElapsed15Min,
       "adMefPerCosPerEvcPhCurValidIntervals15Min": adMefPerCosPerEvcPhCurValidIntervals15Min,
       "adMefPerCosPerEvcPhCurInvalidIntervals15Min": adMefPerCosPerEvcPhCurInvalidIntervals15Min,
       "adMefPerCosPerEvcPhCurIngressGreenOctets15Min": adMefPerCosPerEvcPhCurIngressGreenOctets15Min,
       "adMefPerCosPerEvcPhCurIngressGreenFrames15Min": adMefPerCosPerEvcPhCurIngressGreenFrames15Min,
       "adMefPerCosPerEvcPhCurEgressGreenOctets15Min": adMefPerCosPerEvcPhCurEgressGreenOctets15Min,
       "adMefPerCosPerEvcPhCurEgressGreenFrames15Min": adMefPerCosPerEvcPhCurEgressGreenFrames15Min,
       "adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min": adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min,
       "adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min": adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min,
       "adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min": adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min,
       "adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min": adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min,
       "adMefPerCosPerEvcPhCurTimeElapsed1Day": adMefPerCosPerEvcPhCurTimeElapsed1Day,
       "adMefPerCosPerEvcPhCurValidIntervals1Day": adMefPerCosPerEvcPhCurValidIntervals1Day,
       "adMefPerCosPerEvcPhCurInvalidIntervals1Day": adMefPerCosPerEvcPhCurInvalidIntervals1Day,
       "adMefPerCosPerEvcPhCurIngressGreenOctets1Day": adMefPerCosPerEvcPhCurIngressGreenOctets1Day,
       "adMefPerCosPerEvcPhCurIngressGreenFrames1Day": adMefPerCosPerEvcPhCurIngressGreenFrames1Day,
       "adMefPerCosPerEvcPhCurEgressGreenOctets1Day": adMefPerCosPerEvcPhCurEgressGreenOctets1Day,
       "adMefPerCosPerEvcPhCurEgressGreenFrames1Day": adMefPerCosPerEvcPhCurEgressGreenFrames1Day,
       "adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day": adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day,
       "adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day": adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day,
       "adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day": adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day,
       "adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day": adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day,
       "adMefPerCosPerEvcPh15MinIntervalTable": adMefPerCosPerEvcPh15MinIntervalTable,
       "adMefPerCosPerEvcPh15MinIntervalEntry": adMefPerCosPerEvcPh15MinIntervalEntry,
       "adMefPerCosPerEvcPh15MinEvcNameFixedLen": adMefPerCosPerEvcPh15MinEvcNameFixedLen,
       "adMefPerCosPerEvcPh15MinQueueNumber": adMefPerCosPerEvcPh15MinQueueNumber,
       "adMefPerCosPerEvcPh15MinIntervalNumber": adMefPerCosPerEvcPh15MinIntervalNumber,
       "adMefPerCosPerEvcPh15MinIngressGreenOctets": adMefPerCosPerEvcPh15MinIngressGreenOctets,
       "adMefPerCosPerEvcPh15MinIngressGreenFrames": adMefPerCosPerEvcPh15MinIngressGreenFrames,
       "adMefPerCosPerEvcPh15MinEgressGreenOctets": adMefPerCosPerEvcPh15MinEgressGreenOctets,
       "adMefPerCosPerEvcPh15MinEgressGreenFrames": adMefPerCosPerEvcPh15MinEgressGreenFrames,
       "adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards": adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards,
       "adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards": adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards,
       "adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards": adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards,
       "adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards": adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards,
       "adMefPerCosPerEvcPh1DayIntervalTable": adMefPerCosPerEvcPh1DayIntervalTable,
       "adMefPerCosPerEvcPh1DayIntervalEntry": adMefPerCosPerEvcPh1DayIntervalEntry,
       "adMefPerCosPerEvcPh1DayEvcNameFixedLen": adMefPerCosPerEvcPh1DayEvcNameFixedLen,
       "adMefPerCosPerEvcPh1DayQueueNumber": adMefPerCosPerEvcPh1DayQueueNumber,
       "adMefPerCosPerEvcPh1DayIntervalNumber": adMefPerCosPerEvcPh1DayIntervalNumber,
       "adMefPerCosPerEvcPh1DayIngressGreenOctets": adMefPerCosPerEvcPh1DayIngressGreenOctets,
       "adMefPerCosPerEvcPh1DayIngressGreenFrames": adMefPerCosPerEvcPh1DayIngressGreenFrames,
       "adMefPerCosPerEvcPh1DayEgressGreenOctets": adMefPerCosPerEvcPh1DayEgressGreenOctets,
       "adMefPerCosPerEvcPh1DayEgressGreenFrames": adMefPerCosPerEvcPh1DayEgressGreenFrames,
       "adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards": adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards,
       "adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards": adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards,
       "adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards": adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards,
       "adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards": adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards,
       "adGenAosMefPerCosPerEvcPerfHistoryConformance": adGenAosMefPerCosPerEvcPerfHistoryConformance,
       "adGenAosMefPerCosPerEvcPerfHistoryGroups": adGenAosMefPerCosPerEvcPerfHistoryGroups,
       "adMefPerCosPerEvcPhCurGroup": adMefPerCosPerEvcPhCurGroup,
       "adMefPerCosPerEvcPh15MinIntervalGroup": adMefPerCosPerEvcPh15MinIntervalGroup,
       "adMefPerCosPerEvcPh1DayIntervalGroup": adMefPerCosPerEvcPh1DayIntervalGroup,
       "adGenAosMefPerCosPerEvcPerfHistoryCompliances": adGenAosMefPerCosPerEvcPerfHistoryCompliances,
       "adGenAosMefPerCosPerEvcPerfHistoryCompliance": adGenAosMefPerCosPerEvcPerfHistoryCompliance,
       "adGenAosMefPerCosPerEvcPerfHistoryMib": adGenAosMefPerCosPerEvcPerfHistoryMib}
)
