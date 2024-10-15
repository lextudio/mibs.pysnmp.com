# SNMP MIB module (ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:36 2024
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

adGenAosMefPerUniPerfHistoryMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 1)
)
adGenAosMefPerUniPerfHistoryMib.setRevisions(
        ("2014-09-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAosMefPerUniPerfHistory_ObjectIdentity = ObjectIdentity
adGenAosMefPerUniPerfHistory = _AdGenAosMefPerUniPerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1)
)
_AdMefPerUniPhCurTable_Object = MibTable
adMefPerUniPhCurTable = _AdMefPerUniPhCurTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1)
)
if mibBuilder.loadTexts:
    adMefPerUniPhCurTable.setStatus("current")
_AdMefPerUniPhCurEntry_Object = MibTableRow
adMefPerUniPhCurEntry = _AdMefPerUniPhCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1)
)
adMefPerUniPhCurEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adMefPerUniPhCurEntry.setStatus("current")
_AdMefPerUniPhCurTimeElapsed15Min_Type = HCPerfTimeElapsed
_AdMefPerUniPhCurTimeElapsed15Min_Object = MibTableColumn
adMefPerUniPhCurTimeElapsed15Min = _AdMefPerUniPhCurTimeElapsed15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 1),
    _AdMefPerUniPhCurTimeElapsed15Min_Type()
)
adMefPerUniPhCurTimeElapsed15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurTimeElapsed15Min.setStatus("current")
_AdMefPerUniPhCurValidIntervals15Min_Type = HCPerfValidIntervals
_AdMefPerUniPhCurValidIntervals15Min_Object = MibTableColumn
adMefPerUniPhCurValidIntervals15Min = _AdMefPerUniPhCurValidIntervals15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 2),
    _AdMefPerUniPhCurValidIntervals15Min_Type()
)
adMefPerUniPhCurValidIntervals15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurValidIntervals15Min.setStatus("current")
_AdMefPerUniPhCurInvalidIntervals15Min_Type = HCPerfInvalidIntervals
_AdMefPerUniPhCurInvalidIntervals15Min_Object = MibTableColumn
adMefPerUniPhCurInvalidIntervals15Min = _AdMefPerUniPhCurInvalidIntervals15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 3),
    _AdMefPerUniPhCurInvalidIntervals15Min_Type()
)
adMefPerUniPhCurInvalidIntervals15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurInvalidIntervals15Min.setStatus("current")
_AdMefPerUniPhCurIngressGreenOctets15Min_Type = HCPerfCurrentCount
_AdMefPerUniPhCurIngressGreenOctets15Min_Object = MibTableColumn
adMefPerUniPhCurIngressGreenOctets15Min = _AdMefPerUniPhCurIngressGreenOctets15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 4),
    _AdMefPerUniPhCurIngressGreenOctets15Min_Type()
)
adMefPerUniPhCurIngressGreenOctets15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurIngressGreenOctets15Min.setStatus("current")
_AdMefPerUniPhCurIngressGreenFrames15Min_Type = HCPerfCurrentCount
_AdMefPerUniPhCurIngressGreenFrames15Min_Object = MibTableColumn
adMefPerUniPhCurIngressGreenFrames15Min = _AdMefPerUniPhCurIngressGreenFrames15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 5),
    _AdMefPerUniPhCurIngressGreenFrames15Min_Type()
)
adMefPerUniPhCurIngressGreenFrames15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurIngressGreenFrames15Min.setStatus("current")
_AdMefPerUniPhCurEgressGreenOctets15Min_Type = HCPerfCurrentCount
_AdMefPerUniPhCurEgressGreenOctets15Min_Object = MibTableColumn
adMefPerUniPhCurEgressGreenOctets15Min = _AdMefPerUniPhCurEgressGreenOctets15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 6),
    _AdMefPerUniPhCurEgressGreenOctets15Min_Type()
)
adMefPerUniPhCurEgressGreenOctets15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurEgressGreenOctets15Min.setStatus("current")
_AdMefPerUniPhCurEgressGreenFrames15Min_Type = HCPerfCurrentCount
_AdMefPerUniPhCurEgressGreenFrames15Min_Object = MibTableColumn
adMefPerUniPhCurEgressGreenFrames15Min = _AdMefPerUniPhCurEgressGreenFrames15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 7),
    _AdMefPerUniPhCurEgressGreenFrames15Min_Type()
)
adMefPerUniPhCurEgressGreenFrames15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurEgressGreenFrames15Min.setStatus("current")
_AdMefPerUniPhCurIngressGreenFrameDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerUniPhCurIngressGreenFrameDiscards15Min_Object = MibTableColumn
adMefPerUniPhCurIngressGreenFrameDiscards15Min = _AdMefPerUniPhCurIngressGreenFrameDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 8),
    _AdMefPerUniPhCurIngressGreenFrameDiscards15Min_Type()
)
adMefPerUniPhCurIngressGreenFrameDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurIngressGreenFrameDiscards15Min.setStatus("current")
_AdMefPerUniPhCurEgressGreenFrameDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerUniPhCurEgressGreenFrameDiscards15Min_Object = MibTableColumn
adMefPerUniPhCurEgressGreenFrameDiscards15Min = _AdMefPerUniPhCurEgressGreenFrameDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 9),
    _AdMefPerUniPhCurEgressGreenFrameDiscards15Min_Type()
)
adMefPerUniPhCurEgressGreenFrameDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurEgressGreenFrameDiscards15Min.setStatus("current")
_AdMefPerUniPhCurIngressGreenOctetDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerUniPhCurIngressGreenOctetDiscards15Min_Object = MibTableColumn
adMefPerUniPhCurIngressGreenOctetDiscards15Min = _AdMefPerUniPhCurIngressGreenOctetDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 10),
    _AdMefPerUniPhCurIngressGreenOctetDiscards15Min_Type()
)
adMefPerUniPhCurIngressGreenOctetDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurIngressGreenOctetDiscards15Min.setStatus("current")
_AdMefPerUniPhCurEgressGreenOctetDiscards15Min_Type = HCPerfCurrentCount
_AdMefPerUniPhCurEgressGreenOctetDiscards15Min_Object = MibTableColumn
adMefPerUniPhCurEgressGreenOctetDiscards15Min = _AdMefPerUniPhCurEgressGreenOctetDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 11),
    _AdMefPerUniPhCurEgressGreenOctetDiscards15Min_Type()
)
adMefPerUniPhCurEgressGreenOctetDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurEgressGreenOctetDiscards15Min.setStatus("current")
_AdMefPerUniPhCurTimeElapsed1Day_Type = HCPerfTimeElapsed
_AdMefPerUniPhCurTimeElapsed1Day_Object = MibTableColumn
adMefPerUniPhCurTimeElapsed1Day = _AdMefPerUniPhCurTimeElapsed1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 12),
    _AdMefPerUniPhCurTimeElapsed1Day_Type()
)
adMefPerUniPhCurTimeElapsed1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurTimeElapsed1Day.setStatus("current")
_AdMefPerUniPhCurValidIntervals1Day_Type = HCPerfValidIntervals
_AdMefPerUniPhCurValidIntervals1Day_Object = MibTableColumn
adMefPerUniPhCurValidIntervals1Day = _AdMefPerUniPhCurValidIntervals1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 13),
    _AdMefPerUniPhCurValidIntervals1Day_Type()
)
adMefPerUniPhCurValidIntervals1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurValidIntervals1Day.setStatus("current")
_AdMefPerUniPhCurInvalidIntervals1Day_Type = HCPerfInvalidIntervals
_AdMefPerUniPhCurInvalidIntervals1Day_Object = MibTableColumn
adMefPerUniPhCurInvalidIntervals1Day = _AdMefPerUniPhCurInvalidIntervals1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 14),
    _AdMefPerUniPhCurInvalidIntervals1Day_Type()
)
adMefPerUniPhCurInvalidIntervals1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurInvalidIntervals1Day.setStatus("current")
_AdMefPerUniPhCurIngressGreenOctets1Day_Type = HCPerfCurrentCount
_AdMefPerUniPhCurIngressGreenOctets1Day_Object = MibTableColumn
adMefPerUniPhCurIngressGreenOctets1Day = _AdMefPerUniPhCurIngressGreenOctets1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 15),
    _AdMefPerUniPhCurIngressGreenOctets1Day_Type()
)
adMefPerUniPhCurIngressGreenOctets1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurIngressGreenOctets1Day.setStatus("current")
_AdMefPerUniPhCurIngressGreenFrames1Day_Type = HCPerfCurrentCount
_AdMefPerUniPhCurIngressGreenFrames1Day_Object = MibTableColumn
adMefPerUniPhCurIngressGreenFrames1Day = _AdMefPerUniPhCurIngressGreenFrames1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 16),
    _AdMefPerUniPhCurIngressGreenFrames1Day_Type()
)
adMefPerUniPhCurIngressGreenFrames1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurIngressGreenFrames1Day.setStatus("current")
_AdMefPerUniPhCurEgressGreenOctets1Day_Type = HCPerfCurrentCount
_AdMefPerUniPhCurEgressGreenOctets1Day_Object = MibTableColumn
adMefPerUniPhCurEgressGreenOctets1Day = _AdMefPerUniPhCurEgressGreenOctets1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 17),
    _AdMefPerUniPhCurEgressGreenOctets1Day_Type()
)
adMefPerUniPhCurEgressGreenOctets1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurEgressGreenOctets1Day.setStatus("current")
_AdMefPerUniPhCurEgressGreenFrames1Day_Type = HCPerfCurrentCount
_AdMefPerUniPhCurEgressGreenFrames1Day_Object = MibTableColumn
adMefPerUniPhCurEgressGreenFrames1Day = _AdMefPerUniPhCurEgressGreenFrames1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 18),
    _AdMefPerUniPhCurEgressGreenFrames1Day_Type()
)
adMefPerUniPhCurEgressGreenFrames1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurEgressGreenFrames1Day.setStatus("current")
_AdMefPerUniPhCurIngressGreenFrameDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerUniPhCurIngressGreenFrameDiscards1Day_Object = MibTableColumn
adMefPerUniPhCurIngressGreenFrameDiscards1Day = _AdMefPerUniPhCurIngressGreenFrameDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 19),
    _AdMefPerUniPhCurIngressGreenFrameDiscards1Day_Type()
)
adMefPerUniPhCurIngressGreenFrameDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurIngressGreenFrameDiscards1Day.setStatus("current")
_AdMefPerUniPhCurEgressGreenFrameDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerUniPhCurEgressGreenFrameDiscards1Day_Object = MibTableColumn
adMefPerUniPhCurEgressGreenFrameDiscards1Day = _AdMefPerUniPhCurEgressGreenFrameDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 20),
    _AdMefPerUniPhCurEgressGreenFrameDiscards1Day_Type()
)
adMefPerUniPhCurEgressGreenFrameDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurEgressGreenFrameDiscards1Day.setStatus("current")
_AdMefPerUniPhCurIngressGreenOctetDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerUniPhCurIngressGreenOctetDiscards1Day_Object = MibTableColumn
adMefPerUniPhCurIngressGreenOctetDiscards1Day = _AdMefPerUniPhCurIngressGreenOctetDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 21),
    _AdMefPerUniPhCurIngressGreenOctetDiscards1Day_Type()
)
adMefPerUniPhCurIngressGreenOctetDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurIngressGreenOctetDiscards1Day.setStatus("current")
_AdMefPerUniPhCurEgressGreenOctetDiscards1Day_Type = HCPerfCurrentCount
_AdMefPerUniPhCurEgressGreenOctetDiscards1Day_Object = MibTableColumn
adMefPerUniPhCurEgressGreenOctetDiscards1Day = _AdMefPerUniPhCurEgressGreenOctetDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 22),
    _AdMefPerUniPhCurEgressGreenOctetDiscards1Day_Type()
)
adMefPerUniPhCurEgressGreenOctetDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPhCurEgressGreenOctetDiscards1Day.setStatus("current")
_AdMefPerUniPh15MinIntervalTable_Object = MibTable
adMefPerUniPh15MinIntervalTable = _AdMefPerUniPh15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2)
)
if mibBuilder.loadTexts:
    adMefPerUniPh15MinIntervalTable.setStatus("current")
_AdMefPerUniPh15MinIntervalEntry_Object = MibTableRow
adMefPerUniPh15MinIntervalEntry = _AdMefPerUniPh15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1)
)
adMefPerUniPh15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    adMefPerUniPh15MinIntervalEntry.setStatus("current")


class _AdMefPerUniPh15MinIntervalNumber_Type(Integer32):
    """Custom type adMefPerUniPh15MinIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdMefPerUniPh15MinIntervalNumber_Type.__name__ = "Integer32"
_AdMefPerUniPh15MinIntervalNumber_Object = MibTableColumn
adMefPerUniPh15MinIntervalNumber = _AdMefPerUniPh15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 1),
    _AdMefPerUniPh15MinIntervalNumber_Type()
)
adMefPerUniPh15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerUniPh15MinIntervalNumber.setStatus("current")
_AdMefPerUniPh15MinIngressGreenOctets_Type = HCPerfIntervalCount
_AdMefPerUniPh15MinIngressGreenOctets_Object = MibTableColumn
adMefPerUniPh15MinIngressGreenOctets = _AdMefPerUniPh15MinIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 2),
    _AdMefPerUniPh15MinIngressGreenOctets_Type()
)
adMefPerUniPh15MinIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh15MinIngressGreenOctets.setStatus("current")
_AdMefPerUniPh15MinIngressGreenFrames_Type = HCPerfIntervalCount
_AdMefPerUniPh15MinIngressGreenFrames_Object = MibTableColumn
adMefPerUniPh15MinIngressGreenFrames = _AdMefPerUniPh15MinIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 3),
    _AdMefPerUniPh15MinIngressGreenFrames_Type()
)
adMefPerUniPh15MinIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh15MinIngressGreenFrames.setStatus("current")
_AdMefPerUniPh15MinEgressGreenOctets_Type = HCPerfIntervalCount
_AdMefPerUniPh15MinEgressGreenOctets_Object = MibTableColumn
adMefPerUniPh15MinEgressGreenOctets = _AdMefPerUniPh15MinEgressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 4),
    _AdMefPerUniPh15MinEgressGreenOctets_Type()
)
adMefPerUniPh15MinEgressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh15MinEgressGreenOctets.setStatus("current")
_AdMefPerUniPh15MinEgressGreenFrames_Type = HCPerfIntervalCount
_AdMefPerUniPh15MinEgressGreenFrames_Object = MibTableColumn
adMefPerUniPh15MinEgressGreenFrames = _AdMefPerUniPh15MinEgressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 5),
    _AdMefPerUniPh15MinEgressGreenFrames_Type()
)
adMefPerUniPh15MinEgressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh15MinEgressGreenFrames.setStatus("current")
_AdMefPerUniPh15MinIngressGreenFrameDiscards_Type = HCPerfIntervalCount
_AdMefPerUniPh15MinIngressGreenFrameDiscards_Object = MibTableColumn
adMefPerUniPh15MinIngressGreenFrameDiscards = _AdMefPerUniPh15MinIngressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 6),
    _AdMefPerUniPh15MinIngressGreenFrameDiscards_Type()
)
adMefPerUniPh15MinIngressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh15MinIngressGreenFrameDiscards.setStatus("current")
_AdMefPerUniPh15MinEgressGreenFrameDiscards_Type = HCPerfIntervalCount
_AdMefPerUniPh15MinEgressGreenFrameDiscards_Object = MibTableColumn
adMefPerUniPh15MinEgressGreenFrameDiscards = _AdMefPerUniPh15MinEgressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 7),
    _AdMefPerUniPh15MinEgressGreenFrameDiscards_Type()
)
adMefPerUniPh15MinEgressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh15MinEgressGreenFrameDiscards.setStatus("current")
_AdMefPerUniPh15MinIngressGreenOctetDiscards_Type = HCPerfIntervalCount
_AdMefPerUniPh15MinIngressGreenOctetDiscards_Object = MibTableColumn
adMefPerUniPh15MinIngressGreenOctetDiscards = _AdMefPerUniPh15MinIngressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 8),
    _AdMefPerUniPh15MinIngressGreenOctetDiscards_Type()
)
adMefPerUniPh15MinIngressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh15MinIngressGreenOctetDiscards.setStatus("current")
_AdMefPerUniPh15MinEgressGreenOctetDiscards_Type = HCPerfIntervalCount
_AdMefPerUniPh15MinEgressGreenOctetDiscards_Object = MibTableColumn
adMefPerUniPh15MinEgressGreenOctetDiscards = _AdMefPerUniPh15MinEgressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 9),
    _AdMefPerUniPh15MinEgressGreenOctetDiscards_Type()
)
adMefPerUniPh15MinEgressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh15MinEgressGreenOctetDiscards.setStatus("current")
_AdMefPerUniPh1DayIntervalTable_Object = MibTable
adMefPerUniPh1DayIntervalTable = _AdMefPerUniPh1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3)
)
if mibBuilder.loadTexts:
    adMefPerUniPh1DayIntervalTable.setStatus("current")
_AdMefPerUniPh1DayIntervalEntry_Object = MibTableRow
adMefPerUniPh1DayIntervalEntry = _AdMefPerUniPh1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1)
)
adMefPerUniPh1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adMefPerUniPh1DayIntervalEntry.setStatus("current")


class _AdMefPerUniPh1DayIntervalNumber_Type(Integer32):
    """Custom type adMefPerUniPh1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AdMefPerUniPh1DayIntervalNumber_Type.__name__ = "Integer32"
_AdMefPerUniPh1DayIntervalNumber_Object = MibTableColumn
adMefPerUniPh1DayIntervalNumber = _AdMefPerUniPh1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 1),
    _AdMefPerUniPh1DayIntervalNumber_Type()
)
adMefPerUniPh1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerUniPh1DayIntervalNumber.setStatus("current")
_AdMefPerUniPh1DayIngressGreenOctets_Type = HCPerfTotalCount
_AdMefPerUniPh1DayIngressGreenOctets_Object = MibTableColumn
adMefPerUniPh1DayIngressGreenOctets = _AdMefPerUniPh1DayIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 2),
    _AdMefPerUniPh1DayIngressGreenOctets_Type()
)
adMefPerUniPh1DayIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh1DayIngressGreenOctets.setStatus("current")
_AdMefPerUniPh1DayIngressGreenFrames_Type = HCPerfTotalCount
_AdMefPerUniPh1DayIngressGreenFrames_Object = MibTableColumn
adMefPerUniPh1DayIngressGreenFrames = _AdMefPerUniPh1DayIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 3),
    _AdMefPerUniPh1DayIngressGreenFrames_Type()
)
adMefPerUniPh1DayIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh1DayIngressGreenFrames.setStatus("current")
_AdMefPerUniPh1DayEgressGreenOctets_Type = HCPerfTotalCount
_AdMefPerUniPh1DayEgressGreenOctets_Object = MibTableColumn
adMefPerUniPh1DayEgressGreenOctets = _AdMefPerUniPh1DayEgressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 4),
    _AdMefPerUniPh1DayEgressGreenOctets_Type()
)
adMefPerUniPh1DayEgressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh1DayEgressGreenOctets.setStatus("current")
_AdMefPerUniPh1DayEgressGreenFrames_Type = HCPerfTotalCount
_AdMefPerUniPh1DayEgressGreenFrames_Object = MibTableColumn
adMefPerUniPh1DayEgressGreenFrames = _AdMefPerUniPh1DayEgressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 5),
    _AdMefPerUniPh1DayEgressGreenFrames_Type()
)
adMefPerUniPh1DayEgressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh1DayEgressGreenFrames.setStatus("current")
_AdMefPerUniPh1DayIngressGreenFrameDiscards_Type = HCPerfTotalCount
_AdMefPerUniPh1DayIngressGreenFrameDiscards_Object = MibTableColumn
adMefPerUniPh1DayIngressGreenFrameDiscards = _AdMefPerUniPh1DayIngressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 6),
    _AdMefPerUniPh1DayIngressGreenFrameDiscards_Type()
)
adMefPerUniPh1DayIngressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh1DayIngressGreenFrameDiscards.setStatus("current")
_AdMefPerUniPh1DayEgressGreenFrameDiscards_Type = HCPerfTotalCount
_AdMefPerUniPh1DayEgressGreenFrameDiscards_Object = MibTableColumn
adMefPerUniPh1DayEgressGreenFrameDiscards = _AdMefPerUniPh1DayEgressGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 7),
    _AdMefPerUniPh1DayEgressGreenFrameDiscards_Type()
)
adMefPerUniPh1DayEgressGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh1DayEgressGreenFrameDiscards.setStatus("current")
_AdMefPerUniPh1DayIngressGreenOctetDiscards_Type = HCPerfTotalCount
_AdMefPerUniPh1DayIngressGreenOctetDiscards_Object = MibTableColumn
adMefPerUniPh1DayIngressGreenOctetDiscards = _AdMefPerUniPh1DayIngressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 8),
    _AdMefPerUniPh1DayIngressGreenOctetDiscards_Type()
)
adMefPerUniPh1DayIngressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh1DayIngressGreenOctetDiscards.setStatus("current")
_AdMefPerUniPh1DayEgressGreenOctetDiscards_Type = HCPerfTotalCount
_AdMefPerUniPh1DayEgressGreenOctetDiscards_Object = MibTableColumn
adMefPerUniPh1DayEgressGreenOctetDiscards = _AdMefPerUniPh1DayEgressGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 9),
    _AdMefPerUniPh1DayEgressGreenOctetDiscards_Type()
)
adMefPerUniPh1DayEgressGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniPh1DayEgressGreenOctetDiscards.setStatus("current")
_AdGenAosMefPerUniPerfHistoryConformance_ObjectIdentity = ObjectIdentity
adGenAosMefPerUniPerfHistoryConformance = _AdGenAosMefPerUniPerfHistoryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22)
)
_AdGenAosMefPerUniPerfHistoryGroups_ObjectIdentity = ObjectIdentity
adGenAosMefPerUniPerfHistoryGroups = _AdGenAosMefPerUniPerfHistoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 1)
)
_AdGenAosMefPerUniPerfHistoryCompliances_ObjectIdentity = ObjectIdentity
adGenAosMefPerUniPerfHistoryCompliances = _AdGenAosMefPerUniPerfHistoryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 2)
)

# Managed Objects groups

adMefPerUniPhCurGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 1, 1)
)
adMefPerUniPhCurGroup.setObjects(
      *(("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurTimeElapsed15Min"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurValidIntervals15Min"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurInvalidIntervals15Min"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenOctets15Min"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenFrames15Min"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenOctets15Min"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenFrames15Min"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenFrameDiscards15Min"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenFrameDiscards15Min"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenOctetDiscards15Min"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenOctetDiscards15Min"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurTimeElapsed1Day"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurValidIntervals1Day"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurInvalidIntervals1Day"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenOctets1Day"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenFrames1Day"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenOctets1Day"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenFrames1Day"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenFrameDiscards1Day"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenFrameDiscards1Day"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenOctetDiscards1Day"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenOctetDiscards1Day"))
)
if mibBuilder.loadTexts:
    adMefPerUniPhCurGroup.setStatus("current")

adMefPerUniPh15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 1, 2)
)
adMefPerUniPh15MinIntervalGroup.setObjects(
      *(("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIngressGreenOctets"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIngressGreenFrames"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinEgressGreenOctets"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinEgressGreenFrames"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIngressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinEgressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIngressGreenOctetDiscards"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinEgressGreenOctetDiscards"))
)
if mibBuilder.loadTexts:
    adMefPerUniPh15MinIntervalGroup.setStatus("current")

adMefPerUniPh1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 1, 3)
)
adMefPerUniPh1DayIntervalGroup.setObjects(
      *(("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIngressGreenOctets"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIngressGreenFrames"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayEgressGreenOctets"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayEgressGreenFrames"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIngressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayEgressGreenFrameDiscards"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIngressGreenOctetDiscards"),
        ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayEgressGreenOctetDiscards"))
)
if mibBuilder.loadTexts:
    adMefPerUniPh1DayIntervalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAosMefPerUniPerfHistoryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAosMefPerUniPerfHistoryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB",
    **{"adGenAosMefPerUniPerfHistory": adGenAosMefPerUniPerfHistory,
       "adMefPerUniPhCurTable": adMefPerUniPhCurTable,
       "adMefPerUniPhCurEntry": adMefPerUniPhCurEntry,
       "adMefPerUniPhCurTimeElapsed15Min": adMefPerUniPhCurTimeElapsed15Min,
       "adMefPerUniPhCurValidIntervals15Min": adMefPerUniPhCurValidIntervals15Min,
       "adMefPerUniPhCurInvalidIntervals15Min": adMefPerUniPhCurInvalidIntervals15Min,
       "adMefPerUniPhCurIngressGreenOctets15Min": adMefPerUniPhCurIngressGreenOctets15Min,
       "adMefPerUniPhCurIngressGreenFrames15Min": adMefPerUniPhCurIngressGreenFrames15Min,
       "adMefPerUniPhCurEgressGreenOctets15Min": adMefPerUniPhCurEgressGreenOctets15Min,
       "adMefPerUniPhCurEgressGreenFrames15Min": adMefPerUniPhCurEgressGreenFrames15Min,
       "adMefPerUniPhCurIngressGreenFrameDiscards15Min": adMefPerUniPhCurIngressGreenFrameDiscards15Min,
       "adMefPerUniPhCurEgressGreenFrameDiscards15Min": adMefPerUniPhCurEgressGreenFrameDiscards15Min,
       "adMefPerUniPhCurIngressGreenOctetDiscards15Min": adMefPerUniPhCurIngressGreenOctetDiscards15Min,
       "adMefPerUniPhCurEgressGreenOctetDiscards15Min": adMefPerUniPhCurEgressGreenOctetDiscards15Min,
       "adMefPerUniPhCurTimeElapsed1Day": adMefPerUniPhCurTimeElapsed1Day,
       "adMefPerUniPhCurValidIntervals1Day": adMefPerUniPhCurValidIntervals1Day,
       "adMefPerUniPhCurInvalidIntervals1Day": adMefPerUniPhCurInvalidIntervals1Day,
       "adMefPerUniPhCurIngressGreenOctets1Day": adMefPerUniPhCurIngressGreenOctets1Day,
       "adMefPerUniPhCurIngressGreenFrames1Day": adMefPerUniPhCurIngressGreenFrames1Day,
       "adMefPerUniPhCurEgressGreenOctets1Day": adMefPerUniPhCurEgressGreenOctets1Day,
       "adMefPerUniPhCurEgressGreenFrames1Day": adMefPerUniPhCurEgressGreenFrames1Day,
       "adMefPerUniPhCurIngressGreenFrameDiscards1Day": adMefPerUniPhCurIngressGreenFrameDiscards1Day,
       "adMefPerUniPhCurEgressGreenFrameDiscards1Day": adMefPerUniPhCurEgressGreenFrameDiscards1Day,
       "adMefPerUniPhCurIngressGreenOctetDiscards1Day": adMefPerUniPhCurIngressGreenOctetDiscards1Day,
       "adMefPerUniPhCurEgressGreenOctetDiscards1Day": adMefPerUniPhCurEgressGreenOctetDiscards1Day,
       "adMefPerUniPh15MinIntervalTable": adMefPerUniPh15MinIntervalTable,
       "adMefPerUniPh15MinIntervalEntry": adMefPerUniPh15MinIntervalEntry,
       "adMefPerUniPh15MinIntervalNumber": adMefPerUniPh15MinIntervalNumber,
       "adMefPerUniPh15MinIngressGreenOctets": adMefPerUniPh15MinIngressGreenOctets,
       "adMefPerUniPh15MinIngressGreenFrames": adMefPerUniPh15MinIngressGreenFrames,
       "adMefPerUniPh15MinEgressGreenOctets": adMefPerUniPh15MinEgressGreenOctets,
       "adMefPerUniPh15MinEgressGreenFrames": adMefPerUniPh15MinEgressGreenFrames,
       "adMefPerUniPh15MinIngressGreenFrameDiscards": adMefPerUniPh15MinIngressGreenFrameDiscards,
       "adMefPerUniPh15MinEgressGreenFrameDiscards": adMefPerUniPh15MinEgressGreenFrameDiscards,
       "adMefPerUniPh15MinIngressGreenOctetDiscards": adMefPerUniPh15MinIngressGreenOctetDiscards,
       "adMefPerUniPh15MinEgressGreenOctetDiscards": adMefPerUniPh15MinEgressGreenOctetDiscards,
       "adMefPerUniPh1DayIntervalTable": adMefPerUniPh1DayIntervalTable,
       "adMefPerUniPh1DayIntervalEntry": adMefPerUniPh1DayIntervalEntry,
       "adMefPerUniPh1DayIntervalNumber": adMefPerUniPh1DayIntervalNumber,
       "adMefPerUniPh1DayIngressGreenOctets": adMefPerUniPh1DayIngressGreenOctets,
       "adMefPerUniPh1DayIngressGreenFrames": adMefPerUniPh1DayIngressGreenFrames,
       "adMefPerUniPh1DayEgressGreenOctets": adMefPerUniPh1DayEgressGreenOctets,
       "adMefPerUniPh1DayEgressGreenFrames": adMefPerUniPh1DayEgressGreenFrames,
       "adMefPerUniPh1DayIngressGreenFrameDiscards": adMefPerUniPh1DayIngressGreenFrameDiscards,
       "adMefPerUniPh1DayEgressGreenFrameDiscards": adMefPerUniPh1DayEgressGreenFrameDiscards,
       "adMefPerUniPh1DayIngressGreenOctetDiscards": adMefPerUniPh1DayIngressGreenOctetDiscards,
       "adMefPerUniPh1DayEgressGreenOctetDiscards": adMefPerUniPh1DayEgressGreenOctetDiscards,
       "adGenAosMefPerUniPerfHistoryConformance": adGenAosMefPerUniPerfHistoryConformance,
       "adGenAosMefPerUniPerfHistoryGroups": adGenAosMefPerUniPerfHistoryGroups,
       "adMefPerUniPhCurGroup": adMefPerUniPhCurGroup,
       "adMefPerUniPh15MinIntervalGroup": adMefPerUniPh15MinIntervalGroup,
       "adMefPerUniPh1DayIntervalGroup": adMefPerUniPh1DayIntervalGroup,
       "adGenAosMefPerUniPerfHistoryCompliances": adGenAosMefPerUniPerfHistoryCompliances,
       "adGenAosMefPerUniPerfHistoryCompliance": adGenAosMefPerUniPerfHistoryCompliance,
       "adGenAosMefPerUniPerfHistoryMib": adGenAosMefPerUniPerfHistoryMib}
)
