# SNMP MIB module (ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:35 2024
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

adGenAosMefPerEvcPerfHistoryMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 3)
)
adGenAosMefPerEvcPerfHistoryMib.setRevisions(
        ("2014-09-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAosMefPerEvcPerfHistory_ObjectIdentity = ObjectIdentity
adGenAosMefPerEvcPerfHistory = _AdGenAosMefPerEvcPerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3)
)
_AdMefPerEvcPhCurTable_Object = MibTable
adMefPerEvcPhCurTable = _AdMefPerEvcPhCurTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1)
)
if mibBuilder.loadTexts:
    adMefPerEvcPhCurTable.setStatus("current")
_AdMefPerEvcPhCurEntry_Object = MibTableRow
adMefPerEvcPhCurEntry = _AdMefPerEvcPhCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1)
)
adMefPerEvcPhCurEntry.setIndexNames(
    (0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEvcNameFixedLen"),
)
if mibBuilder.loadTexts:
    adMefPerEvcPhCurEntry.setStatus("current")


class _AdMefPerEvcPhCurEvcNameFixedLen_Type(OctetString):
    """Custom type adMefPerEvcPhCurEvcNameFixedLen based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )


_AdMefPerEvcPhCurEvcNameFixedLen_Type.__name__ = "OctetString"
_AdMefPerEvcPhCurEvcNameFixedLen_Object = MibTableColumn
adMefPerEvcPhCurEvcNameFixedLen = _AdMefPerEvcPhCurEvcNameFixedLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 1),
    _AdMefPerEvcPhCurEvcNameFixedLen_Type()
)
adMefPerEvcPhCurEvcNameFixedLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurEvcNameFixedLen.setStatus("current")
_AdMefPerEvcPhCurTimeElapsed15Min_Type = HCPerfTimeElapsed
_AdMefPerEvcPhCurTimeElapsed15Min_Object = MibTableColumn
adMefPerEvcPhCurTimeElapsed15Min = _AdMefPerEvcPhCurTimeElapsed15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 2),
    _AdMefPerEvcPhCurTimeElapsed15Min_Type()
)
adMefPerEvcPhCurTimeElapsed15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurTimeElapsed15Min.setStatus("current")
_AdMefPerEvcPhCurValidIntervals15Min_Type = HCPerfValidIntervals
_AdMefPerEvcPhCurValidIntervals15Min_Object = MibTableColumn
adMefPerEvcPhCurValidIntervals15Min = _AdMefPerEvcPhCurValidIntervals15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 3),
    _AdMefPerEvcPhCurValidIntervals15Min_Type()
)
adMefPerEvcPhCurValidIntervals15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurValidIntervals15Min.setStatus("current")
_AdMefPerEvcPhCurInvalidIntervals15Min_Type = HCPerfInvalidIntervals
_AdMefPerEvcPhCurInvalidIntervals15Min_Object = MibTableColumn
adMefPerEvcPhCurInvalidIntervals15Min = _AdMefPerEvcPhCurInvalidIntervals15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 4),
    _AdMefPerEvcPhCurInvalidIntervals15Min_Type()
)
adMefPerEvcPhCurInvalidIntervals15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurInvalidIntervals15Min.setStatus("current")
_AdMefPerEvcPhCurIngressGreenOctets15Min_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurIngressGreenOctets15Min_Object = MibTableColumn
adMefPerEvcPhCurIngressGreenOctets15Min = _AdMefPerEvcPhCurIngressGreenOctets15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 5),
    _AdMefPerEvcPhCurIngressGreenOctets15Min_Type()
)
adMefPerEvcPhCurIngressGreenOctets15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurIngressGreenOctets15Min.setStatus("current")
_AdMefPerEvcPhCurIngressGreenFrames15Min_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurIngressGreenFrames15Min_Object = MibTableColumn
adMefPerEvcPhCurIngressGreenFrames15Min = _AdMefPerEvcPhCurIngressGreenFrames15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 6),
    _AdMefPerEvcPhCurIngressGreenFrames15Min_Type()
)
adMefPerEvcPhCurIngressGreenFrames15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurIngressGreenFrames15Min.setStatus("current")
_AdMefPerEvcPhCurEgressGreenOctets15Min_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurEgressGreenOctets15Min_Object = MibTableColumn
adMefPerEvcPhCurEgressGreenOctets15Min = _AdMefPerEvcPhCurEgressGreenOctets15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 7),
    _AdMefPerEvcPhCurEgressGreenOctets15Min_Type()
)
adMefPerEvcPhCurEgressGreenOctets15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurEgressGreenOctets15Min.setStatus("current")
_AdMefPerEvcPhCurEgressGreenFrames15Min_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurEgressGreenFrames15Min_Object = MibTableColumn
adMefPerEvcPhCurEgressGreenFrames15Min = _AdMefPerEvcPhCurEgressGreenFrames15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 8),
    _AdMefPerEvcPhCurEgressGreenFrames15Min_Type()
)
adMefPerEvcPhCurEgressGreenFrames15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurEgressGreenFrames15Min.setStatus("current")
_AdMefPerEvcPhCurIngressGreenFrameDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurIngressGreenFrameDiscards15Min_Object = MibTableColumn
adMefPerEvcPhCurIngressGreenFrameDiscards15Min = _AdMefPerEvcPhCurIngressGreenFrameDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 9),
    _AdMefPerEvcPhCurIngressGreenFrameDiscards15Min_Type()
)
adMefPerEvcPhCurIngressGreenFrameDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurIngressGreenFrameDiscards15Min.setStatus("current")
_AdMefPerEvcPhCurEgressGreenFrameDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurEgressGreenFrameDiscards15Min_Object = MibTableColumn
adMefPerEvcPhCurEgressGreenFrameDiscards15Min = _AdMefPerEvcPhCurEgressGreenFrameDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 10),
    _AdMefPerEvcPhCurEgressGreenFrameDiscards15Min_Type()
)
adMefPerEvcPhCurEgressGreenFrameDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurEgressGreenFrameDiscards15Min.setStatus("current")
_AdMefPerEvcPhCurIngressGreenOctetDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurIngressGreenOctetDiscards15Min_Object = MibTableColumn
adMefPerEvcPhCurIngressGreenOctetDiscards15Min = _AdMefPerEvcPhCurIngressGreenOctetDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 11),
    _AdMefPerEvcPhCurIngressGreenOctetDiscards15Min_Type()
)
adMefPerEvcPhCurIngressGreenOctetDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurIngressGreenOctetDiscards15Min.setStatus("current")
_AdMefPerEvcPhCurEgressGreenOctetDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurEgressGreenOctetDiscards15Min_Object = MibTableColumn
adMefPerEvcPhCurEgressGreenOctetDiscards15Min = _AdMefPerEvcPhCurEgressGreenOctetDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 12),
    _AdMefPerEvcPhCurEgressGreenOctetDiscards15Min_Type()
)
adMefPerEvcPhCurEgressGreenOctetDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurEgressGreenOctetDiscards15Min.setStatus("current")
_AdMefPerEvcPhCurTimeElapsed1Day_Type = HCPerfTimeElapsed
_AdMefPerEvcPhCurTimeElapsed1Day_Object = MibTableColumn
adMefPerEvcPhCurTimeElapsed1Day = _AdMefPerEvcPhCurTimeElapsed1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 13),
    _AdMefPerEvcPhCurTimeElapsed1Day_Type()
)
adMefPerEvcPhCurTimeElapsed1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurTimeElapsed1Day.setStatus("current")
_AdMefPerEvcPhCurValidIntervals1Day_Type = HCPerfValidIntervals
_AdMefPerEvcPhCurValidIntervals1Day_Object = MibTableColumn
adMefPerEvcPhCurValidIntervals1Day = _AdMefPerEvcPhCurValidIntervals1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 14),
    _AdMefPerEvcPhCurValidIntervals1Day_Type()
)
adMefPerEvcPhCurValidIntervals1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurValidIntervals1Day.setStatus("current")
_AdMefPerEvcPhCurInvalidIntervals1Day_Type = HCPerfInvalidIntervals
_AdMefPerEvcPhCurInvalidIntervals1Day_Object = MibTableColumn
adMefPerEvcPhCurInvalidIntervals1Day = _AdMefPerEvcPhCurInvalidIntervals1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 15),
    _AdMefPerEvcPhCurInvalidIntervals1Day_Type()
)
adMefPerEvcPhCurInvalidIntervals1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurInvalidIntervals1Day.setStatus("current")
_AdMefPerEvcPhCurIngressGreenOctets1Day_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurIngressGreenOctets1Day_Object = MibTableColumn
adMefPerEvcPhCurIngressGreenOctets1Day = _AdMefPerEvcPhCurIngressGreenOctets1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 16),
    _AdMefPerEvcPhCurIngressGreenOctets1Day_Type()
)
adMefPerEvcPhCurIngressGreenOctets1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurIngressGreenOctets1Day.setStatus("current")
_AdMefPerEvcPhCurIngressGreenFrames1Day_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurIngressGreenFrames1Day_Object = MibTableColumn
adMefPerEvcPhCurIngressGreenFrames1Day = _AdMefPerEvcPhCurIngressGreenFrames1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 17),
    _AdMefPerEvcPhCurIngressGreenFrames1Day_Type()
)
adMefPerEvcPhCurIngressGreenFrames1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurIngressGreenFrames1Day.setStatus("current")
_AdMefPerEvcPhCurEgressGreenOctets1Day_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurEgressGreenOctets1Day_Object = MibTableColumn
adMefPerEvcPhCurEgressGreenOctets1Day = _AdMefPerEvcPhCurEgressGreenOctets1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 18),
    _AdMefPerEvcPhCurEgressGreenOctets1Day_Type()
)
adMefPerEvcPhCurEgressGreenOctets1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurEgressGreenOctets1Day.setStatus("current")
_AdMefPerEvcPhCurEgressGreenFrames1Day_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurEgressGreenFrames1Day_Object = MibTableColumn
adMefPerEvcPhCurEgressGreenFrames1Day = _AdMefPerEvcPhCurEgressGreenFrames1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 19),
    _AdMefPerEvcPhCurEgressGreenFrames1Day_Type()
)
adMefPerEvcPhCurEgressGreenFrames1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurEgressGreenFrames1Day.setStatus("current")
_AdMefPerEvcPhCurIngressGreenFrameDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurIngressGreenFrameDiscards1Day_Object = MibTableColumn
adMefPerEvcPhCurIngressGreenFrameDiscards1Day = _AdMefPerEvcPhCurIngressGreenFrameDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 20),
    _AdMefPerEvcPhCurIngressGreenFrameDiscards1Day_Type()
)
adMefPerEvcPhCurIngressGreenFrameDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurIngressGreenFrameDiscards1Day.setStatus("current")
_AdMefPerEvcPhCurEgressGreenFrameDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurEgressGreenFrameDiscards1Day_Object = MibTableColumn
adMefPerEvcPhCurEgressGreenFrameDiscards1Day = _AdMefPerEvcPhCurEgressGreenFrameDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 21),
    _AdMefPerEvcPhCurEgressGreenFrameDiscards1Day_Type()
)
adMefPerEvcPhCurEgressGreenFrameDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurEgressGreenFrameDiscards1Day.setStatus("current")
_AdMefPerEvcPhCurIngressGreenOctetDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurIngressGreenOctetDiscards1Day_Object = MibTableColumn
adMefPerEvcPhCurIngressGreenOctetDiscards1Day = _AdMefPerEvcPhCurIngressGreenOctetDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 22),
    _AdMefPerEvcPhCurIngressGreenOctetDiscards1Day_Type()
)
adMefPerEvcPhCurIngressGreenOctetDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurIngressGreenOctetDiscards1Day.setStatus("current")
_AdMefPerEvcPhCurEgressGreenOctetDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerEvcPhCurEgressGreenOctetDiscards1Day_Object = MibTableColumn
adMefPerEvcPhCurEgressGreenOctetDiscards1Day = _AdMefPerEvcPhCurEgressGreenOctetDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 23),
    _AdMefPerEvcPhCurEgressGreenOctetDiscards1Day_Type()
)
adMefPerEvcPhCurEgressGreenOctetDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPhCurEgressGreenOctetDiscards1Day.setStatus("current")
_AdMefPerEvcPh15MinIntervalTable_Object = MibTable
adMefPerEvcPh15MinIntervalTable = _AdMefPerEvcPh15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2)
)
if mibBuilder.loadTexts:
    adMefPerEvcPh15MinIntervalTable.setStatus("current")
_AdMefPerEvcPh15MinIntervalEntry_Object = MibTableRow
adMefPerEvcPh15MinIntervalEntry = _AdMefPerEvcPh15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1)
)
adMefPerEvcPh15MinIntervalEntry.setIndexNames(
    (0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEvcNameFixedLen"),
    (0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    adMefPerEvcPh15MinIntervalEntry.setStatus("current")


class _AdMefPerEvcPh15MinEvcNameFixedLen_Type(OctetString):
    """Custom type adMefPerEvcPh15MinEvcNameFixedLen based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )


_AdMefPerEvcPh15MinEvcNameFixedLen_Type.__name__ = "OctetString"
_AdMefPerEvcPh15MinEvcNameFixedLen_Object = MibTableColumn
adMefPerEvcPh15MinEvcNameFixedLen = _AdMefPerEvcPh15MinEvcNameFixedLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 1),
    _AdMefPerEvcPh15MinEvcNameFixedLen_Type()
)
adMefPerEvcPh15MinEvcNameFixedLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerEvcPh15MinEvcNameFixedLen.setStatus("current")


class _AdMefPerEvcPh15MinIntervalNumber_Type(Integer32):
    """Custom type adMefPerEvcPh15MinIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdMefPerEvcPh15MinIntervalNumber_Type.__name__ = "Integer32"
_AdMefPerEvcPh15MinIntervalNumber_Object = MibTableColumn
adMefPerEvcPh15MinIntervalNumber = _AdMefPerEvcPh15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 2),
    _AdMefPerEvcPh15MinIntervalNumber_Type()
)
adMefPerEvcPh15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerEvcPh15MinIntervalNumber.setStatus("current")
_AdMefPerEvcPh15MinIngressGreenOctets_Type = HCPerfIntervalCount
_AdMefPerEvcPh15MinIngressGreenOctets_Object = MibTableColumn
adMefPerEvcPh15MinIngressGreenOctets = _AdMefPerEvcPh15MinIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 3),
    _AdMefPerEvcPh15MinIngressGreenOctets_Type()
)
adMefPerEvcPh15MinIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh15MinIngressGreenOctets.setStatus("current")
_AdMefPerEvcPh15MinIngressGreenFrames_Type = HCPerfIntervalCount
_AdMefPerEvcPh15MinIngressGreenFrames_Object = MibTableColumn
adMefPerEvcPh15MinIngressGreenFrames = _AdMefPerEvcPh15MinIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 4),
    _AdMefPerEvcPh15MinIngressGreenFrames_Type()
)
adMefPerEvcPh15MinIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh15MinIngressGreenFrames.setStatus("current")
_AdMefPerEvcPh15MinEgressGreenOctets_Type = HCPerfIntervalCount
_AdMefPerEvcPh15MinEgressGreenOctets_Object = MibTableColumn
adMefPerEvcPh15MinEgressGreenOctets = _AdMefPerEvcPh15MinEgressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 5),
    _AdMefPerEvcPh15MinEgressGreenOctets_Type()
)
adMefPerEvcPh15MinEgressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh15MinEgressGreenOctets.setStatus("current")
_AdMefPerEvcPh15MinEgressGreenFrames_Type = HCPerfIntervalCount
_AdMefPerEvcPh15MinEgressGreenFrames_Object = MibTableColumn
adMefPerEvcPh15MinEgressGreenFrames = _AdMefPerEvcPh15MinEgressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 6),
    _AdMefPerEvcPh15MinEgressGreenFrames_Type()
)
adMefPerEvcPh15MinEgressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh15MinEgressGreenFrames.setStatus("current")
_AdMefPerEvcPh15MinIngressGreenFrameDiscards_Type = HCPerfIntervalCount
_AdMefPerEvcPh15MinIngressGreenFrameDiscards_Object = MibTableColumn
adMefPerEvcPh15MinIngressGreenFrameDiscards = _AdMefPerEvcPh15MinIngressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 7),
    _AdMefPerEvcPh15MinIngressGreenFrameDiscards_Type()
)
adMefPerEvcPh15MinIngressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh15MinIngressGreenFrameDiscards.setStatus("current")
_AdMefPerEvcPh15MinEgressGreenFrameDiscards_Type = HCPerfIntervalCount
_AdMefPerEvcPh15MinEgressGreenFrameDiscards_Object = MibTableColumn
adMefPerEvcPh15MinEgressGreenFrameDiscards = _AdMefPerEvcPh15MinEgressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 8),
    _AdMefPerEvcPh15MinEgressGreenFrameDiscards_Type()
)
adMefPerEvcPh15MinEgressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh15MinEgressGreenFrameDiscards.setStatus("current")
_AdMefPerEvcPh15MinIngressGreenOctetDiscards_Type = HCPerfIntervalCount
_AdMefPerEvcPh15MinIngressGreenOctetDiscards_Object = MibTableColumn
adMefPerEvcPh15MinIngressGreenOctetDiscards = _AdMefPerEvcPh15MinIngressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 9),
    _AdMefPerEvcPh15MinIngressGreenOctetDiscards_Type()
)
adMefPerEvcPh15MinIngressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh15MinIngressGreenOctetDiscards.setStatus("current")
_AdMefPerEvcPh15MinEgressGreenOctetDiscards_Type = HCPerfIntervalCount
_AdMefPerEvcPh15MinEgressGreenOctetDiscards_Object = MibTableColumn
adMefPerEvcPh15MinEgressGreenOctetDiscards = _AdMefPerEvcPh15MinEgressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 10),
    _AdMefPerEvcPh15MinEgressGreenOctetDiscards_Type()
)
adMefPerEvcPh15MinEgressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh15MinEgressGreenOctetDiscards.setStatus("current")
_AdMefPerEvcPh1DayIntervalTable_Object = MibTable
adMefPerEvcPh1DayIntervalTable = _AdMefPerEvcPh1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3)
)
if mibBuilder.loadTexts:
    adMefPerEvcPh1DayIntervalTable.setStatus("current")
_AdMefPerEvcPh1DayIntervalEntry_Object = MibTableRow
adMefPerEvcPh1DayIntervalEntry = _AdMefPerEvcPh1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1)
)
adMefPerEvcPh1DayIntervalEntry.setIndexNames(
    (0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEvcNameFixedLen"),
    (0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adMefPerEvcPh1DayIntervalEntry.setStatus("current")


class _AdMefPerEvcPh1DayEvcNameFixedLen_Type(OctetString):
    """Custom type adMefPerEvcPh1DayEvcNameFixedLen based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )


_AdMefPerEvcPh1DayEvcNameFixedLen_Type.__name__ = "OctetString"
_AdMefPerEvcPh1DayEvcNameFixedLen_Object = MibTableColumn
adMefPerEvcPh1DayEvcNameFixedLen = _AdMefPerEvcPh1DayEvcNameFixedLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 1),
    _AdMefPerEvcPh1DayEvcNameFixedLen_Type()
)
adMefPerEvcPh1DayEvcNameFixedLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerEvcPh1DayEvcNameFixedLen.setStatus("current")


class _AdMefPerEvcPh1DayIntervalNumber_Type(Integer32):
    """Custom type adMefPerEvcPh1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AdMefPerEvcPh1DayIntervalNumber_Type.__name__ = "Integer32"
_AdMefPerEvcPh1DayIntervalNumber_Object = MibTableColumn
adMefPerEvcPh1DayIntervalNumber = _AdMefPerEvcPh1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 2),
    _AdMefPerEvcPh1DayIntervalNumber_Type()
)
adMefPerEvcPh1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerEvcPh1DayIntervalNumber.setStatus("current")
_AdMefPerEvcPh1DayIngressGreenOctets_Type = HCPerfTotalCount
_AdMefPerEvcPh1DayIngressGreenOctets_Object = MibTableColumn
adMefPerEvcPh1DayIngressGreenOctets = _AdMefPerEvcPh1DayIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 3),
    _AdMefPerEvcPh1DayIngressGreenOctets_Type()
)
adMefPerEvcPh1DayIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh1DayIngressGreenOctets.setStatus("current")
_AdMefPerEvcPh1DayIngressGreenFrames_Type = HCPerfTotalCount
_AdMefPerEvcPh1DayIngressGreenFrames_Object = MibTableColumn
adMefPerEvcPh1DayIngressGreenFrames = _AdMefPerEvcPh1DayIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 4),
    _AdMefPerEvcPh1DayIngressGreenFrames_Type()
)
adMefPerEvcPh1DayIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh1DayIngressGreenFrames.setStatus("current")
_AdMefPerEvcPh1DayEgressGreenOctets_Type = HCPerfTotalCount
_AdMefPerEvcPh1DayEgressGreenOctets_Object = MibTableColumn
adMefPerEvcPh1DayEgressGreenOctets = _AdMefPerEvcPh1DayEgressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 5),
    _AdMefPerEvcPh1DayEgressGreenOctets_Type()
)
adMefPerEvcPh1DayEgressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh1DayEgressGreenOctets.setStatus("current")
_AdMefPerEvcPh1DayEgressGreenFrames_Type = HCPerfTotalCount
_AdMefPerEvcPh1DayEgressGreenFrames_Object = MibTableColumn
adMefPerEvcPh1DayEgressGreenFrames = _AdMefPerEvcPh1DayEgressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 6),
    _AdMefPerEvcPh1DayEgressGreenFrames_Type()
)
adMefPerEvcPh1DayEgressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh1DayEgressGreenFrames.setStatus("current")
_AdMefPerEvcPh1DayIngressGreenFrameDiscards_Type = HCPerfTotalCount
_AdMefPerEvcPh1DayIngressGreenFrameDiscards_Object = MibTableColumn
adMefPerEvcPh1DayIngressGreenFrameDiscards = _AdMefPerEvcPh1DayIngressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 7),
    _AdMefPerEvcPh1DayIngressGreenFrameDiscards_Type()
)
adMefPerEvcPh1DayIngressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh1DayIngressGreenFrameDiscards.setStatus("current")
_AdMefPerEvcPh1DayEgressGreenFrameDiscards_Type = HCPerfTotalCount
_AdMefPerEvcPh1DayEgressGreenFrameDiscards_Object = MibTableColumn
adMefPerEvcPh1DayEgressGreenFrameDiscards = _AdMefPerEvcPh1DayEgressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 8),
    _AdMefPerEvcPh1DayEgressGreenFrameDiscards_Type()
)
adMefPerEvcPh1DayEgressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh1DayEgressGreenFrameDiscards.setStatus("current")
_AdMefPerEvcPh1DayIngressGreenOctetDiscards_Type = HCPerfTotalCount
_AdMefPerEvcPh1DayIngressGreenOctetDiscards_Object = MibTableColumn
adMefPerEvcPh1DayIngressGreenOctetDiscards = _AdMefPerEvcPh1DayIngressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 9),
    _AdMefPerEvcPh1DayIngressGreenOctetDiscards_Type()
)
adMefPerEvcPh1DayIngressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh1DayIngressGreenOctetDiscards.setStatus("current")
_AdMefPerEvcPh1DayEgressGreenOctetDiscards_Type = HCPerfTotalCount
_AdMefPerEvcPh1DayEgressGreenOctetDiscards_Object = MibTableColumn
adMefPerEvcPh1DayEgressGreenOctetDiscards = _AdMefPerEvcPh1DayEgressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 10),
    _AdMefPerEvcPh1DayEgressGreenOctetDiscards_Type()
)
adMefPerEvcPh1DayEgressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcPh1DayEgressGreenOctetDiscards.setStatus("current")
_AdGenAosMefPerEvcPerfHistoryConformance_ObjectIdentity = ObjectIdentity
adGenAosMefPerEvcPerfHistoryConformance = _AdGenAosMefPerEvcPerfHistoryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23)
)
_AdGenAosMefPerEvcPerfHistoryGroups_ObjectIdentity = ObjectIdentity
adGenAosMefPerEvcPerfHistoryGroups = _AdGenAosMefPerEvcPerfHistoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 1)
)
_AdGenAosMefPerEvcPerfHistoryCompliances_ObjectIdentity = ObjectIdentity
adGenAosMefPerEvcPerfHistoryCompliances = _AdGenAosMefPerEvcPerfHistoryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 2)
)

# Managed Objects groups

adMefPerEvcPhCurGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 1, 1)
)
adMefPerEvcPhCurGroup.setObjects(
      *(("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurTimeElapsed15Min"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurValidIntervals15Min"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurInvalidIntervals15Min"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenOctets15Min"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenFrames15Min"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenOctets15Min"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenFrames15Min"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenFrameDiscards15Min"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenFrameDiscards15Min"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenOctetDiscards15Min"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenOctetDiscards15Min"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurTimeElapsed1Day"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurValidIntervals1Day"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurInvalidIntervals1Day"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenOctets1Day"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenFrames1Day"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenOctets1Day"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenFrames1Day"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenFrameDiscards1Day"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenFrameDiscards1Day"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenOctetDiscards1Day"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenOctetDiscards1Day"))
)
if mibBuilder.loadTexts:
    adMefPerEvcPhCurGroup.setStatus("current")

adMefPerEvcPh15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 1, 2)
)
adMefPerEvcPh15MinIntervalGroup.setObjects(
      *(("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIngressGreenOctets"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIngressGreenFrames"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEgressGreenOctets"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEgressGreenFrames"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIngressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEgressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIngressGreenOctetDiscards"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEgressGreenOctetDiscards"))
)
if mibBuilder.loadTexts:
    adMefPerEvcPh15MinIntervalGroup.setStatus("current")

adMefPerEvcPh1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 1, 3)
)
adMefPerEvcPh1DayIntervalGroup.setObjects(
      *(("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIngressGreenOctets"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIngressGreenFrames"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEgressGreenOctets"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEgressGreenFrames"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIngressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEgressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIngressGreenOctetDiscards"),
        ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEgressGreenOctetDiscards"))
)
if mibBuilder.loadTexts:
    adMefPerEvcPh1DayIntervalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAosMefPerEvcPerfHistoryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAosMefPerEvcPerfHistoryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB",
    **{"adGenAosMefPerEvcPerfHistory": adGenAosMefPerEvcPerfHistory,
       "adMefPerEvcPhCurTable": adMefPerEvcPhCurTable,
       "adMefPerEvcPhCurEntry": adMefPerEvcPhCurEntry,
       "adMefPerEvcPhCurEvcNameFixedLen": adMefPerEvcPhCurEvcNameFixedLen,
       "adMefPerEvcPhCurTimeElapsed15Min": adMefPerEvcPhCurTimeElapsed15Min,
       "adMefPerEvcPhCurValidIntervals15Min": adMefPerEvcPhCurValidIntervals15Min,
       "adMefPerEvcPhCurInvalidIntervals15Min": adMefPerEvcPhCurInvalidIntervals15Min,
       "adMefPerEvcPhCurIngressGreenOctets15Min": adMefPerEvcPhCurIngressGreenOctets15Min,
       "adMefPerEvcPhCurIngressGreenFrames15Min": adMefPerEvcPhCurIngressGreenFrames15Min,
       "adMefPerEvcPhCurEgressGreenOctets15Min": adMefPerEvcPhCurEgressGreenOctets15Min,
       "adMefPerEvcPhCurEgressGreenFrames15Min": adMefPerEvcPhCurEgressGreenFrames15Min,
       "adMefPerEvcPhCurIngressGreenFrameDiscards15Min": adMefPerEvcPhCurIngressGreenFrameDiscards15Min,
       "adMefPerEvcPhCurEgressGreenFrameDiscards15Min": adMefPerEvcPhCurEgressGreenFrameDiscards15Min,
       "adMefPerEvcPhCurIngressGreenOctetDiscards15Min": adMefPerEvcPhCurIngressGreenOctetDiscards15Min,
       "adMefPerEvcPhCurEgressGreenOctetDiscards15Min": adMefPerEvcPhCurEgressGreenOctetDiscards15Min,
       "adMefPerEvcPhCurTimeElapsed1Day": adMefPerEvcPhCurTimeElapsed1Day,
       "adMefPerEvcPhCurValidIntervals1Day": adMefPerEvcPhCurValidIntervals1Day,
       "adMefPerEvcPhCurInvalidIntervals1Day": adMefPerEvcPhCurInvalidIntervals1Day,
       "adMefPerEvcPhCurIngressGreenOctets1Day": adMefPerEvcPhCurIngressGreenOctets1Day,
       "adMefPerEvcPhCurIngressGreenFrames1Day": adMefPerEvcPhCurIngressGreenFrames1Day,
       "adMefPerEvcPhCurEgressGreenOctets1Day": adMefPerEvcPhCurEgressGreenOctets1Day,
       "adMefPerEvcPhCurEgressGreenFrames1Day": adMefPerEvcPhCurEgressGreenFrames1Day,
       "adMefPerEvcPhCurIngressGreenFrameDiscards1Day": adMefPerEvcPhCurIngressGreenFrameDiscards1Day,
       "adMefPerEvcPhCurEgressGreenFrameDiscards1Day": adMefPerEvcPhCurEgressGreenFrameDiscards1Day,
       "adMefPerEvcPhCurIngressGreenOctetDiscards1Day": adMefPerEvcPhCurIngressGreenOctetDiscards1Day,
       "adMefPerEvcPhCurEgressGreenOctetDiscards1Day": adMefPerEvcPhCurEgressGreenOctetDiscards1Day,
       "adMefPerEvcPh15MinIntervalTable": adMefPerEvcPh15MinIntervalTable,
       "adMefPerEvcPh15MinIntervalEntry": adMefPerEvcPh15MinIntervalEntry,
       "adMefPerEvcPh15MinEvcNameFixedLen": adMefPerEvcPh15MinEvcNameFixedLen,
       "adMefPerEvcPh15MinIntervalNumber": adMefPerEvcPh15MinIntervalNumber,
       "adMefPerEvcPh15MinIngressGreenOctets": adMefPerEvcPh15MinIngressGreenOctets,
       "adMefPerEvcPh15MinIngressGreenFrames": adMefPerEvcPh15MinIngressGreenFrames,
       "adMefPerEvcPh15MinEgressGreenOctets": adMefPerEvcPh15MinEgressGreenOctets,
       "adMefPerEvcPh15MinEgressGreenFrames": adMefPerEvcPh15MinEgressGreenFrames,
       "adMefPerEvcPh15MinIngressGreenFrameDiscards": adMefPerEvcPh15MinIngressGreenFrameDiscards,
       "adMefPerEvcPh15MinEgressGreenFrameDiscards": adMefPerEvcPh15MinEgressGreenFrameDiscards,
       "adMefPerEvcPh15MinIngressGreenOctetDiscards": adMefPerEvcPh15MinIngressGreenOctetDiscards,
       "adMefPerEvcPh15MinEgressGreenOctetDiscards": adMefPerEvcPh15MinEgressGreenOctetDiscards,
       "adMefPerEvcPh1DayIntervalTable": adMefPerEvcPh1DayIntervalTable,
       "adMefPerEvcPh1DayIntervalEntry": adMefPerEvcPh1DayIntervalEntry,
       "adMefPerEvcPh1DayEvcNameFixedLen": adMefPerEvcPh1DayEvcNameFixedLen,
       "adMefPerEvcPh1DayIntervalNumber": adMefPerEvcPh1DayIntervalNumber,
       "adMefPerEvcPh1DayIngressGreenOctets": adMefPerEvcPh1DayIngressGreenOctets,
       "adMefPerEvcPh1DayIngressGreenFrames": adMefPerEvcPh1DayIngressGreenFrames,
       "adMefPerEvcPh1DayEgressGreenOctets": adMefPerEvcPh1DayEgressGreenOctets,
       "adMefPerEvcPh1DayEgressGreenFrames": adMefPerEvcPh1DayEgressGreenFrames,
       "adMefPerEvcPh1DayIngressGreenFrameDiscards": adMefPerEvcPh1DayIngressGreenFrameDiscards,
       "adMefPerEvcPh1DayEgressGreenFrameDiscards": adMefPerEvcPh1DayEgressGreenFrameDiscards,
       "adMefPerEvcPh1DayIngressGreenOctetDiscards": adMefPerEvcPh1DayIngressGreenOctetDiscards,
       "adMefPerEvcPh1DayEgressGreenOctetDiscards": adMefPerEvcPh1DayEgressGreenOctetDiscards,
       "adGenAosMefPerEvcPerfHistoryConformance": adGenAosMefPerEvcPerfHistoryConformance,
       "adGenAosMefPerEvcPerfHistoryGroups": adGenAosMefPerEvcPerfHistoryGroups,
       "adMefPerEvcPhCurGroup": adMefPerEvcPhCurGroup,
       "adMefPerEvcPh15MinIntervalGroup": adMefPerEvcPh15MinIntervalGroup,
       "adMefPerEvcPh1DayIntervalGroup": adMefPerEvcPh1DayIntervalGroup,
       "adGenAosMefPerEvcPerfHistoryCompliances": adGenAosMefPerEvcPerfHistoryCompliances,
       "adGenAosMefPerEvcPerfHistoryCompliance": adGenAosMefPerEvcPerfHistoryCompliance,
       "adGenAosMefPerEvcPerfHistoryMib": adGenAosMefPerEvcPerfHistoryMib}
)
