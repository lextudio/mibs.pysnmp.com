# SNMP MIB module (CISCO-ADSL-CAP-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ADSL-CAP-LINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:32 2024
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

(adslAtucIntervalNumber,
 adslLineConfProfileName) = mibBuilder.importSymbols(
    "ADSL-LINE-MIB",
    "adslAtucIntervalNumber",
    "adslLineConfProfileName")

(AdslPerfCurrDayCount,
 AdslPerfPrevDayCount) = mibBuilder.importSymbols(
    "ADSL-TC-MIB",
    "AdslPerfCurrDayCount",
    "AdslPerfPrevDayCount")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoAdslLineCapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 149)
)
ciscoAdslLineCapMIB.setRevisions(
        ("2001-03-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AdslLineCapDownstreamRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7168000, 7168000),
        ValueRangeConstraint(6272000, 6272000),
        ValueRangeConstraint(5120000, 5120000),
        ValueRangeConstraint(4480000, 4480000),
        ValueRangeConstraint(3200000, 3200000),
        ValueRangeConstraint(2688000, 2688000),
        ValueRangeConstraint(2560000, 2560000),
        ValueRangeConstraint(2240000, 2240000),
        ValueRangeConstraint(1920000, 1920000),
        ValueRangeConstraint(1600000, 1600000),
        ValueRangeConstraint(1280000, 1280000),
        ValueRangeConstraint(1024000, 1024000),
        ValueRangeConstraint(960000, 960000),
        ValueRangeConstraint(896000, 896000),
        ValueRangeConstraint(768000, 768000),
        ValueRangeConstraint(640000, 640000),
        ValueRangeConstraint(512000, 512000),
        ValueRangeConstraint(384000, 384000),
        ValueRangeConstraint(256000, 256000),
        ValueRangeConstraint(0, 0),
    )



class AdslLineCapUpstreamRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1088000, 1088000),
        ValueRangeConstraint(952000, 952000),
        ValueRangeConstraint(816000, 816000),
        ValueRangeConstraint(680000, 680000),
        ValueRangeConstraint(544000, 544000),
        ValueRangeConstraint(408000, 408000),
        ValueRangeConstraint(272000, 272000),
        ValueRangeConstraint(91000, 91000),
        ValueRangeConstraint(0, 0),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAdslLineCapMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAdslLineCapMIBObjects = _CiscoAdslLineCapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1)
)
_CAdslAtucCapPhysTable_Object = MibTable
cAdslAtucCapPhysTable = _CAdslAtucCapPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 2)
)
if mibBuilder.loadTexts:
    cAdslAtucCapPhysTable.setStatus("current")
_CAdslAtucCapPhysEntry_Object = MibTableRow
cAdslAtucCapPhysEntry = _CAdslAtucCapPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 2, 1)
)
cAdslAtucCapPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cAdslAtucCapPhysEntry.setStatus("current")


class _CAdslAtucCapCurrState_Type(Integer32):
    """Custom type cAdslAtucCapCurrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("downloadFailed", 6),
          ("downloading", 5),
          ("idle", 2),
          ("other", 1),
          ("steadyState", 4),
          ("testing", 7),
          ("training", 3))
    )


_CAdslAtucCapCurrState_Type.__name__ = "Integer32"
_CAdslAtucCapCurrState_Object = MibTableColumn
cAdslAtucCapCurrState = _CAdslAtucCapCurrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 2, 1, 1),
    _CAdslAtucCapCurrState_Type()
)
cAdslAtucCapCurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAtucCapCurrState.setStatus("current")
_CAdslAtucCapCurrRxGain_Type = Gauge32
_CAdslAtucCapCurrRxGain_Object = MibTableColumn
cAdslAtucCapCurrRxGain = _CAdslAtucCapCurrRxGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 2, 1, 2),
    _CAdslAtucCapCurrRxGain_Type()
)
cAdslAtucCapCurrRxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAtucCapCurrRxGain.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucCapCurrRxGain.setUnits("tenth dB")
_CAdslAtucCapCurrRxSnr_Type = Gauge32
_CAdslAtucCapCurrRxSnr_Object = MibTableColumn
cAdslAtucCapCurrRxSnr = _CAdslAtucCapCurrRxSnr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 2, 1, 3),
    _CAdslAtucCapCurrRxSnr_Type()
)
cAdslAtucCapCurrRxSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAtucCapCurrRxSnr.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucCapCurrRxSnr.setUnits("tenth dB")
_CAdslAturCapPhysTable_Object = MibTable
cAdslAturCapPhysTable = _CAdslAturCapPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 3)
)
if mibBuilder.loadTexts:
    cAdslAturCapPhysTable.setStatus("current")
_CAdslAturCapPhysEntry_Object = MibTableRow
cAdslAturCapPhysEntry = _CAdslAturCapPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 3, 1)
)
cAdslAturCapPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cAdslAturCapPhysEntry.setStatus("current")
_CAdslAturCapCurrRxGain_Type = Gauge32
_CAdslAturCapCurrRxGain_Object = MibTableColumn
cAdslAturCapCurrRxGain = _CAdslAturCapCurrRxGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 3, 1, 1),
    _CAdslAturCapCurrRxGain_Type()
)
cAdslAturCapCurrRxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAturCapCurrRxGain.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAturCapCurrRxGain.setUnits("tenth dB")
_CAdslAtucCapPerfDataTable_Object = MibTable
cAdslAtucCapPerfDataTable = _CAdslAtucCapPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 6)
)
if mibBuilder.loadTexts:
    cAdslAtucCapPerfDataTable.setStatus("current")
_CAdslAtucCapPerfDataEntry_Object = MibTableRow
cAdslAtucCapPerfDataEntry = _CAdslAtucCapPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 6, 1)
)
cAdslAtucCapPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cAdslAtucCapPerfDataEntry.setStatus("current")
_CAdslAtucCapPerfInitFailures_Type = Counter32
_CAdslAtucCapPerfInitFailures_Object = MibTableColumn
cAdslAtucCapPerfInitFailures = _CAdslAtucCapPerfInitFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 6, 1, 1),
    _CAdslAtucCapPerfInitFailures_Type()
)
cAdslAtucCapPerfInitFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAtucCapPerfInitFailures.setStatus("current")
_CAdslAtucCapPerfCurr15MinInitFailures_Type = PerfCurrentCount
_CAdslAtucCapPerfCurr15MinInitFailures_Object = MibTableColumn
cAdslAtucCapPerfCurr15MinInitFailures = _CAdslAtucCapPerfCurr15MinInitFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 6, 1, 2),
    _CAdslAtucCapPerfCurr15MinInitFailures_Type()
)
cAdslAtucCapPerfCurr15MinInitFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAtucCapPerfCurr15MinInitFailures.setStatus("current")
_CAdslAtucCapPerfCurr1DayInitFailures_Type = AdslPerfCurrDayCount
_CAdslAtucCapPerfCurr1DayInitFailures_Object = MibTableColumn
cAdslAtucCapPerfCurr1DayInitFailures = _CAdslAtucCapPerfCurr1DayInitFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 6, 1, 3),
    _CAdslAtucCapPerfCurr1DayInitFailures_Type()
)
cAdslAtucCapPerfCurr1DayInitFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAtucCapPerfCurr1DayInitFailures.setStatus("current")
_CAdslAtucCapPerfPrev1DayInitFailures_Type = AdslPerfPrevDayCount
_CAdslAtucCapPerfPrev1DayInitFailures_Object = MibTableColumn
cAdslAtucCapPerfPrev1DayInitFailures = _CAdslAtucCapPerfPrev1DayInitFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 6, 1, 4),
    _CAdslAtucCapPerfPrev1DayInitFailures_Type()
)
cAdslAtucCapPerfPrev1DayInitFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAtucCapPerfPrev1DayInitFailures.setStatus("current")
_CAdslAtucCapIntervalTable_Object = MibTable
cAdslAtucCapIntervalTable = _CAdslAtucCapIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 8)
)
if mibBuilder.loadTexts:
    cAdslAtucCapIntervalTable.setStatus("current")
_CAdslAtucCapIntervalEntry_Object = MibTableRow
cAdslAtucCapIntervalEntry = _CAdslAtucCapIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 8, 1)
)
cAdslAtucCapIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL-LINE-MIB", "adslAtucIntervalNumber"),
)
if mibBuilder.loadTexts:
    cAdslAtucCapIntervalEntry.setStatus("current")
_CAdslAtucCapIntervalInitFailures_Type = PerfIntervalCount
_CAdslAtucCapIntervalInitFailures_Object = MibTableColumn
cAdslAtucCapIntervalInitFailures = _CAdslAtucCapIntervalInitFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 8, 1, 1),
    _CAdslAtucCapIntervalInitFailures_Type()
)
cAdslAtucCapIntervalInitFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAtucCapIntervalInitFailures.setStatus("current")
_CAdslLineCapConfProfileTable_Object = MibTable
cAdslLineCapConfProfileTable = _CAdslLineCapConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14)
)
if mibBuilder.loadTexts:
    cAdslLineCapConfProfileTable.setStatus("current")
_CAdslLineCapConfProfileEntry_Object = MibTableRow
cAdslLineCapConfProfileEntry = _CAdslLineCapConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1)
)
cAdslLineCapConfProfileEntry.setIndexNames(
    (1, "ADSL-LINE-MIB", "adslLineConfProfileName"),
)
if mibBuilder.loadTexts:
    cAdslLineCapConfProfileEntry.setStatus("current")


class _CAdslLineCapConfTrainingMode_Type(Integer32):
    """Custom type cAdslLineCapConfTrainingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 2),
          ("standard", 1))
    )


_CAdslLineCapConfTrainingMode_Type.__name__ = "Integer32"
_CAdslLineCapConfTrainingMode_Object = MibTableColumn
cAdslLineCapConfTrainingMode = _CAdslLineCapConfTrainingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1, 1),
    _CAdslLineCapConfTrainingMode_Type()
)
cAdslLineCapConfTrainingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslLineCapConfTrainingMode.setStatus("current")


class _CAdslLineCapConfInterleaveDelay_Type(Integer32):
    """Custom type cAdslLineCapConfInterleaveDelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("long", 3),
          ("none", 1),
          ("short", 2))
    )


_CAdslLineCapConfInterleaveDelay_Type.__name__ = "Integer32"
_CAdslLineCapConfInterleaveDelay_Object = MibTableColumn
cAdslLineCapConfInterleaveDelay = _CAdslLineCapConfInterleaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1, 2),
    _CAdslLineCapConfInterleaveDelay_Type()
)
cAdslLineCapConfInterleaveDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslLineCapConfInterleaveDelay.setStatus("current")


class _CAdslLineCapConfCpeSignature_Type(Integer32):
    """Custom type cAdslLineCapConfCpeSignature based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CAdslLineCapConfCpeSignature_Type.__name__ = "Integer32"
_CAdslLineCapConfCpeSignature_Object = MibTableColumn
cAdslLineCapConfCpeSignature = _CAdslLineCapConfCpeSignature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1, 3),
    _CAdslLineCapConfCpeSignature_Type()
)
cAdslLineCapConfCpeSignature.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslLineCapConfCpeSignature.setStatus("current")


class _CAdslAtucCapConfTargetSnrMgn_Type(Integer32):
    """Custom type cAdslAtucCapConfTargetSnrMgn based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_CAdslAtucCapConfTargetSnrMgn_Type.__name__ = "Integer32"
_CAdslAtucCapConfTargetSnrMgn_Object = MibTableColumn
cAdslAtucCapConfTargetSnrMgn = _CAdslAtucCapConfTargetSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1, 4),
    _CAdslAtucCapConfTargetSnrMgn_Type()
)
cAdslAtucCapConfTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucCapConfTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucCapConfTargetSnrMgn.setUnits("tenth dB")


class _CAdslAtucCapConfMinTxRate_Type(AdslLineCapDownstreamRate):
    """Custom type cAdslAtucCapConfMinTxRate based on AdslLineCapDownstreamRate"""
    defaultValue = 0


_CAdslAtucCapConfMinTxRate_Object = MibTableColumn
cAdslAtucCapConfMinTxRate = _CAdslAtucCapConfMinTxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1, 5),
    _CAdslAtucCapConfMinTxRate_Type()
)
cAdslAtucCapConfMinTxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucCapConfMinTxRate.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucCapConfMinTxRate.setUnits("bps")


class _CAdslAtucCapConfMaxTxRate_Type(AdslLineCapDownstreamRate):
    """Custom type cAdslAtucCapConfMaxTxRate based on AdslLineCapDownstreamRate"""
    defaultValue = 640000


_CAdslAtucCapConfMaxTxRate_Object = MibTableColumn
cAdslAtucCapConfMaxTxRate = _CAdslAtucCapConfMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1, 6),
    _CAdslAtucCapConfMaxTxRate_Type()
)
cAdslAtucCapConfMaxTxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucCapConfMaxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucCapConfMaxTxRate.setUnits("bps")


class _CAdslAtucCapConfDown136KBaudEnable_Type(TruthValue):
    """Custom type cAdslAtucCapConfDown136KBaudEnable based on TruthValue"""


_CAdslAtucCapConfDown136KBaudEnable_Object = MibTableColumn
cAdslAtucCapConfDown136KBaudEnable = _CAdslAtucCapConfDown136KBaudEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1, 7),
    _CAdslAtucCapConfDown136KBaudEnable_Type()
)
cAdslAtucCapConfDown136KBaudEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucCapConfDown136KBaudEnable.setStatus("current")


class _CAdslAtucCapConfUp68KBaudEnable_Type(TruthValue):
    """Custom type cAdslAtucCapConfUp68KBaudEnable based on TruthValue"""


_CAdslAtucCapConfUp68KBaudEnable_Object = MibTableColumn
cAdslAtucCapConfUp68KBaudEnable = _CAdslAtucCapConfUp68KBaudEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1, 8),
    _CAdslAtucCapConfUp68KBaudEnable_Type()
)
cAdslAtucCapConfUp68KBaudEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucCapConfUp68KBaudEnable.setStatus("current")


class _CAdslAtucCapConfUp17KBaudEnable_Type(TruthValue):
    """Custom type cAdslAtucCapConfUp17KBaudEnable based on TruthValue"""


_CAdslAtucCapConfUp17KBaudEnable_Object = MibTableColumn
cAdslAtucCapConfUp17KBaudEnable = _CAdslAtucCapConfUp17KBaudEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1, 9),
    _CAdslAtucCapConfUp17KBaudEnable_Type()
)
cAdslAtucCapConfUp17KBaudEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucCapConfUp17KBaudEnable.setStatus("current")


class _CAdslAtucCapConfPsdmLevel_Type(Integer32):
    """Custom type cAdslAtucCapConfPsdmLevel based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-52, -52),
        ValueRangeConstraint(-49, -49),
        ValueRangeConstraint(-46, -46),
        ValueRangeConstraint(-43, -43),
        ValueRangeConstraint(-40, -40),
        ValueRangeConstraint(-37, -37),
    )


_CAdslAtucCapConfPsdmLevel_Type.__name__ = "Integer32"
_CAdslAtucCapConfPsdmLevel_Object = MibTableColumn
cAdslAtucCapConfPsdmLevel = _CAdslAtucCapConfPsdmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1, 10),
    _CAdslAtucCapConfPsdmLevel_Type()
)
cAdslAtucCapConfPsdmLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucCapConfPsdmLevel.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucCapConfPsdmLevel.setUnits("dBm/Hz")


class _CAdslAturCapConfTargetSnrMgn_Type(Integer32):
    """Custom type cAdslAturCapConfTargetSnrMgn based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_CAdslAturCapConfTargetSnrMgn_Type.__name__ = "Integer32"
_CAdslAturCapConfTargetSnrMgn_Object = MibTableColumn
cAdslAturCapConfTargetSnrMgn = _CAdslAturCapConfTargetSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1, 11),
    _CAdslAturCapConfTargetSnrMgn_Type()
)
cAdslAturCapConfTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAturCapConfTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAturCapConfTargetSnrMgn.setUnits("tenth dB")


class _CAdslAturCapConfMinTxRate_Type(AdslLineCapUpstreamRate):
    """Custom type cAdslAturCapConfMinTxRate based on AdslLineCapUpstreamRate"""
    defaultValue = 0


_CAdslAturCapConfMinTxRate_Object = MibTableColumn
cAdslAturCapConfMinTxRate = _CAdslAturCapConfMinTxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1, 12),
    _CAdslAturCapConfMinTxRate_Type()
)
cAdslAturCapConfMinTxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAturCapConfMinTxRate.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAturCapConfMinTxRate.setUnits("bps")


class _CAdslAturCapConfMaxTxRate_Type(AdslLineCapUpstreamRate):
    """Custom type cAdslAturCapConfMaxTxRate based on AdslLineCapUpstreamRate"""
    defaultValue = 91000


_CAdslAturCapConfMaxTxRate_Object = MibTableColumn
cAdslAturCapConfMaxTxRate = _CAdslAturCapConfMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1, 13),
    _CAdslAturCapConfMaxTxRate_Type()
)
cAdslAturCapConfMaxTxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAturCapConfMaxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAturCapConfMaxTxRate.setUnits("bps")


class _CAdslAturCapConfPsdmLevel_Type(Integer32):
    """Custom type cAdslAturCapConfPsdmLevel based on Integer32"""
    defaultValue = -38

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-53, -53),
        ValueRangeConstraint(-50, -50),
        ValueRangeConstraint(-47, -47),
        ValueRangeConstraint(-44, -44),
        ValueRangeConstraint(-41, -41),
        ValueRangeConstraint(-38, -38),
    )


_CAdslAturCapConfPsdmLevel_Type.__name__ = "Integer32"
_CAdslAturCapConfPsdmLevel_Object = MibTableColumn
cAdslAturCapConfPsdmLevel = _CAdslAturCapConfPsdmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 1, 14, 1, 14),
    _CAdslAturCapConfPsdmLevel_Type()
)
cAdslAturCapConfPsdmLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAturCapConfPsdmLevel.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAturCapConfPsdmLevel.setUnits("dBm/Hz")
_CAdslLineCapMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
cAdslLineCapMIBNotificationsPrefix = _CAdslLineCapMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 2)
)
_CAdslLineCapMIBNotifications_ObjectIdentity = ObjectIdentity
cAdslLineCapMIBNotifications = _CAdslLineCapMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 2, 0)
)
_CiscoAdslLineCapMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAdslLineCapMIBConformance = _CiscoAdslLineCapMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 3)
)
_CiscoAdslLineCapMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAdslLineCapMIBCompliances = _CiscoAdslLineCapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 3, 1)
)
_CiscoAdslLineCapMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAdslLineCapMIBGroups = _CiscoAdslLineCapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 3, 2)
)

# Managed Objects groups

cAdslAtucCapBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 3, 2, 1)
)
cAdslAtucCapBasicGroup.setObjects(
      *(("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapCurrState"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapCurrRxGain"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapCurrRxSnr"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapPerfInitFailures"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslLineCapConfTrainingMode"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslLineCapConfInterleaveDelay"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslLineCapConfCpeSignature"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapConfTargetSnrMgn"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapConfMinTxRate"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapConfMaxTxRate"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapConfDown136KBaudEnable"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapConfUp68KBaudEnable"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapConfUp17KBaudEnable"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapConfPsdmLevel"))
)
if mibBuilder.loadTexts:
    cAdslAtucCapBasicGroup.setStatus("current")

cAdslAturBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 3, 2, 2)
)
cAdslAturBasicGroup.setObjects(
      *(("CISCO-ADSL-CAP-LINE-MIB", "cAdslAturCapCurrRxGain"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslLineCapConfTrainingMode"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAturCapConfTargetSnrMgn"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAturCapConfMinTxRate"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAturCapConfMaxTxRate"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAturCapConfPsdmLevel"))
)
if mibBuilder.loadTexts:
    cAdslAturBasicGroup.setStatus("current")

cAdslAturCapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 3, 2, 3)
)
cAdslAturCapGroup.setObjects(
      *(("CISCO-ADSL-CAP-LINE-MIB", "cAdslAturCapCurrRxGain"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAturCapConfTargetSnrMgn"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAturCapConfMinTxRate"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAturCapConfMaxTxRate"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAturCapConfPsdmLevel"))
)
if mibBuilder.loadTexts:
    cAdslAturCapGroup.setStatus("current")

cAdslAtucCapPM15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 3, 2, 4)
)
cAdslAtucCapPM15MinIntervalGroup.setObjects(
      *(("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapPerfCurr15MinInitFailures"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapIntervalInitFailures"))
)
if mibBuilder.loadTexts:
    cAdslAtucCapPM15MinIntervalGroup.setStatus("current")

cAdslAtucCapPM1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 3, 2, 5)
)
cAdslAtucCapPM1DayIntervalGroup.setObjects(
      *(("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapPerfCurr1DayInitFailures"),
        ("CISCO-ADSL-CAP-LINE-MIB", "cAdslAtucCapPerfPrev1DayInitFailures"))
)
if mibBuilder.loadTexts:
    cAdslAtucCapPM1DayIntervalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAdslLineCapMIBAtucCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAdslLineCapMIBAtucCompliance.setStatus(
        "current"
    )

ciscoAdslLineCapMIBAturCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 149, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoAdslLineCapMIBAturCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ADSL-CAP-LINE-MIB",
    **{"AdslLineCapDownstreamRate": AdslLineCapDownstreamRate,
       "AdslLineCapUpstreamRate": AdslLineCapUpstreamRate,
       "ciscoAdslLineCapMIB": ciscoAdslLineCapMIB,
       "ciscoAdslLineCapMIBObjects": ciscoAdslLineCapMIBObjects,
       "cAdslAtucCapPhysTable": cAdslAtucCapPhysTable,
       "cAdslAtucCapPhysEntry": cAdslAtucCapPhysEntry,
       "cAdslAtucCapCurrState": cAdslAtucCapCurrState,
       "cAdslAtucCapCurrRxGain": cAdslAtucCapCurrRxGain,
       "cAdslAtucCapCurrRxSnr": cAdslAtucCapCurrRxSnr,
       "cAdslAturCapPhysTable": cAdslAturCapPhysTable,
       "cAdslAturCapPhysEntry": cAdslAturCapPhysEntry,
       "cAdslAturCapCurrRxGain": cAdslAturCapCurrRxGain,
       "cAdslAtucCapPerfDataTable": cAdslAtucCapPerfDataTable,
       "cAdslAtucCapPerfDataEntry": cAdslAtucCapPerfDataEntry,
       "cAdslAtucCapPerfInitFailures": cAdslAtucCapPerfInitFailures,
       "cAdslAtucCapPerfCurr15MinInitFailures": cAdslAtucCapPerfCurr15MinInitFailures,
       "cAdslAtucCapPerfCurr1DayInitFailures": cAdslAtucCapPerfCurr1DayInitFailures,
       "cAdslAtucCapPerfPrev1DayInitFailures": cAdslAtucCapPerfPrev1DayInitFailures,
       "cAdslAtucCapIntervalTable": cAdslAtucCapIntervalTable,
       "cAdslAtucCapIntervalEntry": cAdslAtucCapIntervalEntry,
       "cAdslAtucCapIntervalInitFailures": cAdslAtucCapIntervalInitFailures,
       "cAdslLineCapConfProfileTable": cAdslLineCapConfProfileTable,
       "cAdslLineCapConfProfileEntry": cAdslLineCapConfProfileEntry,
       "cAdslLineCapConfTrainingMode": cAdslLineCapConfTrainingMode,
       "cAdslLineCapConfInterleaveDelay": cAdslLineCapConfInterleaveDelay,
       "cAdslLineCapConfCpeSignature": cAdslLineCapConfCpeSignature,
       "cAdslAtucCapConfTargetSnrMgn": cAdslAtucCapConfTargetSnrMgn,
       "cAdslAtucCapConfMinTxRate": cAdslAtucCapConfMinTxRate,
       "cAdslAtucCapConfMaxTxRate": cAdslAtucCapConfMaxTxRate,
       "cAdslAtucCapConfDown136KBaudEnable": cAdslAtucCapConfDown136KBaudEnable,
       "cAdslAtucCapConfUp68KBaudEnable": cAdslAtucCapConfUp68KBaudEnable,
       "cAdslAtucCapConfUp17KBaudEnable": cAdslAtucCapConfUp17KBaudEnable,
       "cAdslAtucCapConfPsdmLevel": cAdslAtucCapConfPsdmLevel,
       "cAdslAturCapConfTargetSnrMgn": cAdslAturCapConfTargetSnrMgn,
       "cAdslAturCapConfMinTxRate": cAdslAturCapConfMinTxRate,
       "cAdslAturCapConfMaxTxRate": cAdslAturCapConfMaxTxRate,
       "cAdslAturCapConfPsdmLevel": cAdslAturCapConfPsdmLevel,
       "cAdslLineCapMIBNotificationsPrefix": cAdslLineCapMIBNotificationsPrefix,
       "cAdslLineCapMIBNotifications": cAdslLineCapMIBNotifications,
       "ciscoAdslLineCapMIBConformance": ciscoAdslLineCapMIBConformance,
       "ciscoAdslLineCapMIBCompliances": ciscoAdslLineCapMIBCompliances,
       "ciscoAdslLineCapMIBAtucCompliance": ciscoAdslLineCapMIBAtucCompliance,
       "ciscoAdslLineCapMIBAturCompliance": ciscoAdslLineCapMIBAturCompliance,
       "ciscoAdslLineCapMIBGroups": ciscoAdslLineCapMIBGroups,
       "cAdslAtucCapBasicGroup": cAdslAtucCapBasicGroup,
       "cAdslAturBasicGroup": cAdslAturBasicGroup,
       "cAdslAturCapGroup": cAdslAturCapGroup,
       "cAdslAtucCapPM15MinIntervalGroup": cAdslAtucCapPM15MinIntervalGroup,
       "cAdslAtucCapPM1DayIntervalGroup": cAdslAtucCapPM1DayIntervalGroup}
)
