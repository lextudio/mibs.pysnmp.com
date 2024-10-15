# SNMP MIB module (ADTRAN-IF-PERF-HISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-IF-PERF-HISTORY-MIB
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

(adGenAOSCommon,
 adGenAOSConformance) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSCommon",
    "adGenAOSConformance")

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

adGenAosIfPerfHistoryMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 7)
)
adGenAosIfPerfHistoryMib.setRevisions(
        ("2013-08-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAosIfPerfHistory_ObjectIdentity = ObjectIdentity
adGenAosIfPerfHistory = _AdGenAosIfPerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7)
)
_AdIfPhCurTable_Object = MibTable
adIfPhCurTable = _AdIfPhCurTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1)
)
if mibBuilder.loadTexts:
    adIfPhCurTable.setStatus("current")
_AdIfPhCurEntry_Object = MibTableRow
adIfPhCurEntry = _AdIfPhCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1)
)
adIfPhCurEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adIfPhCurEntry.setStatus("current")
_AdIfPhCurTimeElapsed15Min_Type = HCPerfTimeElapsed
_AdIfPhCurTimeElapsed15Min_Object = MibTableColumn
adIfPhCurTimeElapsed15Min = _AdIfPhCurTimeElapsed15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 1),
    _AdIfPhCurTimeElapsed15Min_Type()
)
adIfPhCurTimeElapsed15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurTimeElapsed15Min.setStatus("current")
_AdIfPhCurValidIntervals15Min_Type = HCPerfValidIntervals
_AdIfPhCurValidIntervals15Min_Object = MibTableColumn
adIfPhCurValidIntervals15Min = _AdIfPhCurValidIntervals15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 2),
    _AdIfPhCurValidIntervals15Min_Type()
)
adIfPhCurValidIntervals15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurValidIntervals15Min.setStatus("current")
_AdIfPhCurInvalidIntervals15Min_Type = HCPerfInvalidIntervals
_AdIfPhCurInvalidIntervals15Min_Object = MibTableColumn
adIfPhCurInvalidIntervals15Min = _AdIfPhCurInvalidIntervals15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 3),
    _AdIfPhCurInvalidIntervals15Min_Type()
)
adIfPhCurInvalidIntervals15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInvalidIntervals15Min.setStatus("current")
_AdIfPhCurInOctets15Min_Type = HCPerfCurrentCount
_AdIfPhCurInOctets15Min_Object = MibTableColumn
adIfPhCurInOctets15Min = _AdIfPhCurInOctets15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 4),
    _AdIfPhCurInOctets15Min_Type()
)
adIfPhCurInOctets15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInOctets15Min.setStatus("current")
_AdIfPhCurInUcastPkts15Min_Type = HCPerfCurrentCount
_AdIfPhCurInUcastPkts15Min_Object = MibTableColumn
adIfPhCurInUcastPkts15Min = _AdIfPhCurInUcastPkts15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 5),
    _AdIfPhCurInUcastPkts15Min_Type()
)
adIfPhCurInUcastPkts15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInUcastPkts15Min.setStatus("current")
_AdIfPhCurInMcastPkts15Min_Type = HCPerfCurrentCount
_AdIfPhCurInMcastPkts15Min_Object = MibTableColumn
adIfPhCurInMcastPkts15Min = _AdIfPhCurInMcastPkts15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 6),
    _AdIfPhCurInMcastPkts15Min_Type()
)
adIfPhCurInMcastPkts15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInMcastPkts15Min.setStatus("current")
_AdIfPhCurInBcastPkts15Min_Type = HCPerfCurrentCount
_AdIfPhCurInBcastPkts15Min_Object = MibTableColumn
adIfPhCurInBcastPkts15Min = _AdIfPhCurInBcastPkts15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 7),
    _AdIfPhCurInBcastPkts15Min_Type()
)
adIfPhCurInBcastPkts15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInBcastPkts15Min.setStatus("current")
_AdIfPhCurInDiscards15Min_Type = HCPerfCurrentCount
_AdIfPhCurInDiscards15Min_Object = MibTableColumn
adIfPhCurInDiscards15Min = _AdIfPhCurInDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 8),
    _AdIfPhCurInDiscards15Min_Type()
)
adIfPhCurInDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInDiscards15Min.setStatus("current")
_AdIfPhCurInErrors15Min_Type = HCPerfCurrentCount
_AdIfPhCurInErrors15Min_Object = MibTableColumn
adIfPhCurInErrors15Min = _AdIfPhCurInErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 9),
    _AdIfPhCurInErrors15Min_Type()
)
adIfPhCurInErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInErrors15Min.setStatus("current")
_AdIfPhCurInUnknownProtos15Min_Type = HCPerfCurrentCount
_AdIfPhCurInUnknownProtos15Min_Object = MibTableColumn
adIfPhCurInUnknownProtos15Min = _AdIfPhCurInUnknownProtos15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 10),
    _AdIfPhCurInUnknownProtos15Min_Type()
)
adIfPhCurInUnknownProtos15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInUnknownProtos15Min.setStatus("current")
_AdIfPhCurOutOctets15Min_Type = HCPerfCurrentCount
_AdIfPhCurOutOctets15Min_Object = MibTableColumn
adIfPhCurOutOctets15Min = _AdIfPhCurOutOctets15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 11),
    _AdIfPhCurOutOctets15Min_Type()
)
adIfPhCurOutOctets15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurOutOctets15Min.setStatus("current")
_AdIfPhCurOutUcastPkts15Min_Type = HCPerfCurrentCount
_AdIfPhCurOutUcastPkts15Min_Object = MibTableColumn
adIfPhCurOutUcastPkts15Min = _AdIfPhCurOutUcastPkts15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 12),
    _AdIfPhCurOutUcastPkts15Min_Type()
)
adIfPhCurOutUcastPkts15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurOutUcastPkts15Min.setStatus("current")
_AdIfPhCurOutMcastPkts15Min_Type = HCPerfCurrentCount
_AdIfPhCurOutMcastPkts15Min_Object = MibTableColumn
adIfPhCurOutMcastPkts15Min = _AdIfPhCurOutMcastPkts15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 13),
    _AdIfPhCurOutMcastPkts15Min_Type()
)
adIfPhCurOutMcastPkts15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurOutMcastPkts15Min.setStatus("current")
_AdIfPhCurOutBcastPkts15Min_Type = HCPerfCurrentCount
_AdIfPhCurOutBcastPkts15Min_Object = MibTableColumn
adIfPhCurOutBcastPkts15Min = _AdIfPhCurOutBcastPkts15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 14),
    _AdIfPhCurOutBcastPkts15Min_Type()
)
adIfPhCurOutBcastPkts15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurOutBcastPkts15Min.setStatus("current")
_AdIfPhCurOutDiscards15Min_Type = HCPerfCurrentCount
_AdIfPhCurOutDiscards15Min_Object = MibTableColumn
adIfPhCurOutDiscards15Min = _AdIfPhCurOutDiscards15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 15),
    _AdIfPhCurOutDiscards15Min_Type()
)
adIfPhCurOutDiscards15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurOutDiscards15Min.setStatus("current")
_AdIfPhCurOutErrors15Min_Type = HCPerfCurrentCount
_AdIfPhCurOutErrors15Min_Object = MibTableColumn
adIfPhCurOutErrors15Min = _AdIfPhCurOutErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 16),
    _AdIfPhCurOutErrors15Min_Type()
)
adIfPhCurOutErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurOutErrors15Min.setStatus("current")
_AdIfPhCurTimeElapsed1Day_Type = HCPerfTimeElapsed
_AdIfPhCurTimeElapsed1Day_Object = MibTableColumn
adIfPhCurTimeElapsed1Day = _AdIfPhCurTimeElapsed1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 17),
    _AdIfPhCurTimeElapsed1Day_Type()
)
adIfPhCurTimeElapsed1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurTimeElapsed1Day.setStatus("current")
_AdIfPhCurValidIntervals1Day_Type = HCPerfValidIntervals
_AdIfPhCurValidIntervals1Day_Object = MibTableColumn
adIfPhCurValidIntervals1Day = _AdIfPhCurValidIntervals1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 18),
    _AdIfPhCurValidIntervals1Day_Type()
)
adIfPhCurValidIntervals1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurValidIntervals1Day.setStatus("current")
_AdIfPhCurInvalidIntervals1Day_Type = HCPerfInvalidIntervals
_AdIfPhCurInvalidIntervals1Day_Object = MibTableColumn
adIfPhCurInvalidIntervals1Day = _AdIfPhCurInvalidIntervals1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 19),
    _AdIfPhCurInvalidIntervals1Day_Type()
)
adIfPhCurInvalidIntervals1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInvalidIntervals1Day.setStatus("current")
_AdIfPhCurInOctets1Day_Type = HCPerfCurrentCount
_AdIfPhCurInOctets1Day_Object = MibTableColumn
adIfPhCurInOctets1Day = _AdIfPhCurInOctets1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 20),
    _AdIfPhCurInOctets1Day_Type()
)
adIfPhCurInOctets1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInOctets1Day.setStatus("current")
_AdIfPhCurInUcastPkts1Day_Type = HCPerfCurrentCount
_AdIfPhCurInUcastPkts1Day_Object = MibTableColumn
adIfPhCurInUcastPkts1Day = _AdIfPhCurInUcastPkts1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 21),
    _AdIfPhCurInUcastPkts1Day_Type()
)
adIfPhCurInUcastPkts1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInUcastPkts1Day.setStatus("current")
_AdIfPhCurInMcastPkts1Day_Type = HCPerfCurrentCount
_AdIfPhCurInMcastPkts1Day_Object = MibTableColumn
adIfPhCurInMcastPkts1Day = _AdIfPhCurInMcastPkts1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 22),
    _AdIfPhCurInMcastPkts1Day_Type()
)
adIfPhCurInMcastPkts1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInMcastPkts1Day.setStatus("current")
_AdIfPhCurInBcastPkts1Day_Type = HCPerfCurrentCount
_AdIfPhCurInBcastPkts1Day_Object = MibTableColumn
adIfPhCurInBcastPkts1Day = _AdIfPhCurInBcastPkts1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 23),
    _AdIfPhCurInBcastPkts1Day_Type()
)
adIfPhCurInBcastPkts1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInBcastPkts1Day.setStatus("current")
_AdIfPhCurInDiscards1Day_Type = HCPerfCurrentCount
_AdIfPhCurInDiscards1Day_Object = MibTableColumn
adIfPhCurInDiscards1Day = _AdIfPhCurInDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 24),
    _AdIfPhCurInDiscards1Day_Type()
)
adIfPhCurInDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInDiscards1Day.setStatus("current")
_AdIfPhCurInErrors1Day_Type = HCPerfCurrentCount
_AdIfPhCurInErrors1Day_Object = MibTableColumn
adIfPhCurInErrors1Day = _AdIfPhCurInErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 25),
    _AdIfPhCurInErrors1Day_Type()
)
adIfPhCurInErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInErrors1Day.setStatus("current")
_AdIfPhCurInUnknownProtos1Day_Type = HCPerfCurrentCount
_AdIfPhCurInUnknownProtos1Day_Object = MibTableColumn
adIfPhCurInUnknownProtos1Day = _AdIfPhCurInUnknownProtos1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 26),
    _AdIfPhCurInUnknownProtos1Day_Type()
)
adIfPhCurInUnknownProtos1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurInUnknownProtos1Day.setStatus("current")
_AdIfPhCurOutOctets1Day_Type = HCPerfCurrentCount
_AdIfPhCurOutOctets1Day_Object = MibTableColumn
adIfPhCurOutOctets1Day = _AdIfPhCurOutOctets1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 27),
    _AdIfPhCurOutOctets1Day_Type()
)
adIfPhCurOutOctets1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurOutOctets1Day.setStatus("current")
_AdIfPhCurOutUcastPkts1Day_Type = HCPerfCurrentCount
_AdIfPhCurOutUcastPkts1Day_Object = MibTableColumn
adIfPhCurOutUcastPkts1Day = _AdIfPhCurOutUcastPkts1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 28),
    _AdIfPhCurOutUcastPkts1Day_Type()
)
adIfPhCurOutUcastPkts1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurOutUcastPkts1Day.setStatus("current")
_AdIfPhCurOutMcastPkts1Day_Type = HCPerfCurrentCount
_AdIfPhCurOutMcastPkts1Day_Object = MibTableColumn
adIfPhCurOutMcastPkts1Day = _AdIfPhCurOutMcastPkts1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 29),
    _AdIfPhCurOutMcastPkts1Day_Type()
)
adIfPhCurOutMcastPkts1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurOutMcastPkts1Day.setStatus("current")
_AdIfPhCurOutBcastPkts1Day_Type = HCPerfCurrentCount
_AdIfPhCurOutBcastPkts1Day_Object = MibTableColumn
adIfPhCurOutBcastPkts1Day = _AdIfPhCurOutBcastPkts1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 30),
    _AdIfPhCurOutBcastPkts1Day_Type()
)
adIfPhCurOutBcastPkts1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurOutBcastPkts1Day.setStatus("current")
_AdIfPhCurOutDiscards1Day_Type = HCPerfCurrentCount
_AdIfPhCurOutDiscards1Day_Object = MibTableColumn
adIfPhCurOutDiscards1Day = _AdIfPhCurOutDiscards1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 31),
    _AdIfPhCurOutDiscards1Day_Type()
)
adIfPhCurOutDiscards1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurOutDiscards1Day.setStatus("current")
_AdIfPhCurOutErrors1Day_Type = HCPerfCurrentCount
_AdIfPhCurOutErrors1Day_Object = MibTableColumn
adIfPhCurOutErrors1Day = _AdIfPhCurOutErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 32),
    _AdIfPhCurOutErrors1Day_Type()
)
adIfPhCurOutErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPhCurOutErrors1Day.setStatus("current")
_AdIfPh15MinIntervalTable_Object = MibTable
adIfPh15MinIntervalTable = _AdIfPh15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2)
)
if mibBuilder.loadTexts:
    adIfPh15MinIntervalTable.setStatus("current")
_AdIfPh15MinIntervalEntry_Object = MibTableRow
adIfPh15MinIntervalEntry = _AdIfPh15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1)
)
adIfPh15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    adIfPh15MinIntervalEntry.setStatus("current")


class _AdIfPh15MinIntervalNumber_Type(Integer32):
    """Custom type adIfPh15MinIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdIfPh15MinIntervalNumber_Type.__name__ = "Integer32"
_AdIfPh15MinIntervalNumber_Object = MibTableColumn
adIfPh15MinIntervalNumber = _AdIfPh15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 1),
    _AdIfPh15MinIntervalNumber_Type()
)
adIfPh15MinIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adIfPh15MinIntervalNumber.setStatus("current")
_AdIfPh15MinInOctets_Type = HCPerfIntervalCount
_AdIfPh15MinInOctets_Object = MibTableColumn
adIfPh15MinInOctets = _AdIfPh15MinInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 2),
    _AdIfPh15MinInOctets_Type()
)
adIfPh15MinInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh15MinInOctets.setStatus("current")
_AdIfPh15MinInUcastPkts_Type = HCPerfIntervalCount
_AdIfPh15MinInUcastPkts_Object = MibTableColumn
adIfPh15MinInUcastPkts = _AdIfPh15MinInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 3),
    _AdIfPh15MinInUcastPkts_Type()
)
adIfPh15MinInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh15MinInUcastPkts.setStatus("current")
_AdIfPh15MinInMcastPkts_Type = HCPerfIntervalCount
_AdIfPh15MinInMcastPkts_Object = MibTableColumn
adIfPh15MinInMcastPkts = _AdIfPh15MinInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 4),
    _AdIfPh15MinInMcastPkts_Type()
)
adIfPh15MinInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh15MinInMcastPkts.setStatus("current")
_AdIfPh15MinInBcastPkts_Type = HCPerfIntervalCount
_AdIfPh15MinInBcastPkts_Object = MibTableColumn
adIfPh15MinInBcastPkts = _AdIfPh15MinInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 5),
    _AdIfPh15MinInBcastPkts_Type()
)
adIfPh15MinInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh15MinInBcastPkts.setStatus("current")
_AdIfPh15MinInDiscards_Type = HCPerfIntervalCount
_AdIfPh15MinInDiscards_Object = MibTableColumn
adIfPh15MinInDiscards = _AdIfPh15MinInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 6),
    _AdIfPh15MinInDiscards_Type()
)
adIfPh15MinInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh15MinInDiscards.setStatus("current")
_AdIfPh15MinInErrors_Type = HCPerfIntervalCount
_AdIfPh15MinInErrors_Object = MibTableColumn
adIfPh15MinInErrors = _AdIfPh15MinInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 7),
    _AdIfPh15MinInErrors_Type()
)
adIfPh15MinInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh15MinInErrors.setStatus("current")
_AdIfPh15MinInUnknownProtos_Type = HCPerfIntervalCount
_AdIfPh15MinInUnknownProtos_Object = MibTableColumn
adIfPh15MinInUnknownProtos = _AdIfPh15MinInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 8),
    _AdIfPh15MinInUnknownProtos_Type()
)
adIfPh15MinInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh15MinInUnknownProtos.setStatus("current")
_AdIfPh15MinOutOctets_Type = HCPerfIntervalCount
_AdIfPh15MinOutOctets_Object = MibTableColumn
adIfPh15MinOutOctets = _AdIfPh15MinOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 9),
    _AdIfPh15MinOutOctets_Type()
)
adIfPh15MinOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh15MinOutOctets.setStatus("current")
_AdIfPh15MinOutUcastPkts_Type = HCPerfIntervalCount
_AdIfPh15MinOutUcastPkts_Object = MibTableColumn
adIfPh15MinOutUcastPkts = _AdIfPh15MinOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 10),
    _AdIfPh15MinOutUcastPkts_Type()
)
adIfPh15MinOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh15MinOutUcastPkts.setStatus("current")
_AdIfPh15MinOutMcastPkts_Type = HCPerfIntervalCount
_AdIfPh15MinOutMcastPkts_Object = MibTableColumn
adIfPh15MinOutMcastPkts = _AdIfPh15MinOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 11),
    _AdIfPh15MinOutMcastPkts_Type()
)
adIfPh15MinOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh15MinOutMcastPkts.setStatus("current")
_AdIfPh15MinOutBcastPkts_Type = HCPerfIntervalCount
_AdIfPh15MinOutBcastPkts_Object = MibTableColumn
adIfPh15MinOutBcastPkts = _AdIfPh15MinOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 12),
    _AdIfPh15MinOutBcastPkts_Type()
)
adIfPh15MinOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh15MinOutBcastPkts.setStatus("current")
_AdIfPh15MinOutDiscards_Type = HCPerfIntervalCount
_AdIfPh15MinOutDiscards_Object = MibTableColumn
adIfPh15MinOutDiscards = _AdIfPh15MinOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 13),
    _AdIfPh15MinOutDiscards_Type()
)
adIfPh15MinOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh15MinOutDiscards.setStatus("current")
_AdIfPh15MinOutErrors_Type = HCPerfIntervalCount
_AdIfPh15MinOutErrors_Object = MibTableColumn
adIfPh15MinOutErrors = _AdIfPh15MinOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 14),
    _AdIfPh15MinOutErrors_Type()
)
adIfPh15MinOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh15MinOutErrors.setStatus("current")
_AdIfPh1DayIntervalTable_Object = MibTable
adIfPh1DayIntervalTable = _AdIfPh1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3)
)
if mibBuilder.loadTexts:
    adIfPh1DayIntervalTable.setStatus("current")
_AdIfPh1DayIntervalEntry_Object = MibTableRow
adIfPh1DayIntervalEntry = _AdIfPh1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1)
)
adIfPh1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adIfPh1DayIntervalEntry.setStatus("current")


class _AdIfPh1DayIntervalNumber_Type(Integer32):
    """Custom type adIfPh1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AdIfPh1DayIntervalNumber_Type.__name__ = "Integer32"
_AdIfPh1DayIntervalNumber_Object = MibTableColumn
adIfPh1DayIntervalNumber = _AdIfPh1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 1),
    _AdIfPh1DayIntervalNumber_Type()
)
adIfPh1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adIfPh1DayIntervalNumber.setStatus("current")
_AdIfPh1DayInOctets_Type = HCPerfTotalCount
_AdIfPh1DayInOctets_Object = MibTableColumn
adIfPh1DayInOctets = _AdIfPh1DayInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 2),
    _AdIfPh1DayInOctets_Type()
)
adIfPh1DayInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh1DayInOctets.setStatus("current")
_AdIfPh1DayInUcastPkts_Type = HCPerfTotalCount
_AdIfPh1DayInUcastPkts_Object = MibTableColumn
adIfPh1DayInUcastPkts = _AdIfPh1DayInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 3),
    _AdIfPh1DayInUcastPkts_Type()
)
adIfPh1DayInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh1DayInUcastPkts.setStatus("current")
_AdIfPh1DayInMcastPkts_Type = HCPerfTotalCount
_AdIfPh1DayInMcastPkts_Object = MibTableColumn
adIfPh1DayInMcastPkts = _AdIfPh1DayInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 4),
    _AdIfPh1DayInMcastPkts_Type()
)
adIfPh1DayInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh1DayInMcastPkts.setStatus("current")
_AdIfPh1DayInBcastPkts_Type = HCPerfTotalCount
_AdIfPh1DayInBcastPkts_Object = MibTableColumn
adIfPh1DayInBcastPkts = _AdIfPh1DayInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 5),
    _AdIfPh1DayInBcastPkts_Type()
)
adIfPh1DayInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh1DayInBcastPkts.setStatus("current")
_AdIfPh1DayInDiscards_Type = HCPerfTotalCount
_AdIfPh1DayInDiscards_Object = MibTableColumn
adIfPh1DayInDiscards = _AdIfPh1DayInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 6),
    _AdIfPh1DayInDiscards_Type()
)
adIfPh1DayInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh1DayInDiscards.setStatus("current")
_AdIfPh1DayInErrors_Type = HCPerfTotalCount
_AdIfPh1DayInErrors_Object = MibTableColumn
adIfPh1DayInErrors = _AdIfPh1DayInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 7),
    _AdIfPh1DayInErrors_Type()
)
adIfPh1DayInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh1DayInErrors.setStatus("current")
_AdIfPh1DayInUnknownProtos_Type = HCPerfTotalCount
_AdIfPh1DayInUnknownProtos_Object = MibTableColumn
adIfPh1DayInUnknownProtos = _AdIfPh1DayInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 8),
    _AdIfPh1DayInUnknownProtos_Type()
)
adIfPh1DayInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh1DayInUnknownProtos.setStatus("current")
_AdIfPh1DayOutOctets_Type = HCPerfTotalCount
_AdIfPh1DayOutOctets_Object = MibTableColumn
adIfPh1DayOutOctets = _AdIfPh1DayOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 9),
    _AdIfPh1DayOutOctets_Type()
)
adIfPh1DayOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh1DayOutOctets.setStatus("current")
_AdIfPh1DayOutUcastPkts_Type = HCPerfTotalCount
_AdIfPh1DayOutUcastPkts_Object = MibTableColumn
adIfPh1DayOutUcastPkts = _AdIfPh1DayOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 10),
    _AdIfPh1DayOutUcastPkts_Type()
)
adIfPh1DayOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh1DayOutUcastPkts.setStatus("current")
_AdIfPh1DayOutMcastPkts_Type = HCPerfTotalCount
_AdIfPh1DayOutMcastPkts_Object = MibTableColumn
adIfPh1DayOutMcastPkts = _AdIfPh1DayOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 11),
    _AdIfPh1DayOutMcastPkts_Type()
)
adIfPh1DayOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh1DayOutMcastPkts.setStatus("current")
_AdIfPh1DayOutBcastPkts_Type = HCPerfTotalCount
_AdIfPh1DayOutBcastPkts_Object = MibTableColumn
adIfPh1DayOutBcastPkts = _AdIfPh1DayOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 12),
    _AdIfPh1DayOutBcastPkts_Type()
)
adIfPh1DayOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh1DayOutBcastPkts.setStatus("current")
_AdIfPh1DayOutDiscards_Type = HCPerfTotalCount
_AdIfPh1DayOutDiscards_Object = MibTableColumn
adIfPh1DayOutDiscards = _AdIfPh1DayOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 13),
    _AdIfPh1DayOutDiscards_Type()
)
adIfPh1DayOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh1DayOutDiscards.setStatus("current")
_AdIfPh1DayOutErrors_Type = HCPerfTotalCount
_AdIfPh1DayOutErrors_Object = MibTableColumn
adIfPh1DayOutErrors = _AdIfPh1DayOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 14),
    _AdIfPh1DayOutErrors_Type()
)
adIfPh1DayOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adIfPh1DayOutErrors.setStatus("current")
_AdGenAosIfPerfHistoryConformance_ObjectIdentity = ObjectIdentity
adGenAosIfPerfHistoryConformance = _AdGenAosIfPerfHistoryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16)
)
_AdGenAosIfPerfHistoryGroups_ObjectIdentity = ObjectIdentity
adGenAosIfPerfHistoryGroups = _AdGenAosIfPerfHistoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 1)
)
_AdGenAosIfPerfHistoryCompliances_ObjectIdentity = ObjectIdentity
adGenAosIfPerfHistoryCompliances = _AdGenAosIfPerfHistoryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 2)
)

# Managed Objects groups

adIfPhCurGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 1, 1)
)
adIfPhCurGroup.setObjects(
      *(("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurTimeElapsed15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurValidIntervals15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInvalidIntervals15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInOctets15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInUcastPkts15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInMcastPkts15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInBcastPkts15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInDiscards15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInErrors15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInUnknownProtos15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutOctets15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutUcastPkts15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutMcastPkts15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutBcastPkts15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutDiscards15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutErrors15Min"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurTimeElapsed1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurValidIntervals1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInvalidIntervals1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInOctets1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInUcastPkts1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInMcastPkts1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInBcastPkts1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInDiscards1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInErrors1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInUnknownProtos1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutOctets1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutUcastPkts1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutMcastPkts1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutBcastPkts1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutDiscards1Day"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutErrors1Day"))
)
if mibBuilder.loadTexts:
    adIfPhCurGroup.setStatus("current")

adIfPh15MinIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 1, 2)
)
adIfPh15MinIntervalGroup.setObjects(
      *(("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInOctets"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInUcastPkts"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInMcastPkts"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInBcastPkts"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInDiscards"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInErrors"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInUnknownProtos"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutOctets"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutUcastPkts"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutMcastPkts"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutBcastPkts"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutDiscards"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutErrors"))
)
if mibBuilder.loadTexts:
    adIfPh15MinIntervalGroup.setStatus("current")

adIfPh1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 1, 3)
)
adIfPh1DayIntervalGroup.setObjects(
      *(("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInOctets"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInUcastPkts"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInMcastPkts"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInBcastPkts"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInDiscards"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInErrors"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInUnknownProtos"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutOctets"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutUcastPkts"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutMcastPkts"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutBcastPkts"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutDiscards"),
        ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutErrors"))
)
if mibBuilder.loadTexts:
    adIfPh1DayIntervalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAosIfPerfHistoryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAosIfPerfHistoryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-IF-PERF-HISTORY-MIB",
    **{"adGenAosIfPerfHistory": adGenAosIfPerfHistory,
       "adIfPhCurTable": adIfPhCurTable,
       "adIfPhCurEntry": adIfPhCurEntry,
       "adIfPhCurTimeElapsed15Min": adIfPhCurTimeElapsed15Min,
       "adIfPhCurValidIntervals15Min": adIfPhCurValidIntervals15Min,
       "adIfPhCurInvalidIntervals15Min": adIfPhCurInvalidIntervals15Min,
       "adIfPhCurInOctets15Min": adIfPhCurInOctets15Min,
       "adIfPhCurInUcastPkts15Min": adIfPhCurInUcastPkts15Min,
       "adIfPhCurInMcastPkts15Min": adIfPhCurInMcastPkts15Min,
       "adIfPhCurInBcastPkts15Min": adIfPhCurInBcastPkts15Min,
       "adIfPhCurInDiscards15Min": adIfPhCurInDiscards15Min,
       "adIfPhCurInErrors15Min": adIfPhCurInErrors15Min,
       "adIfPhCurInUnknownProtos15Min": adIfPhCurInUnknownProtos15Min,
       "adIfPhCurOutOctets15Min": adIfPhCurOutOctets15Min,
       "adIfPhCurOutUcastPkts15Min": adIfPhCurOutUcastPkts15Min,
       "adIfPhCurOutMcastPkts15Min": adIfPhCurOutMcastPkts15Min,
       "adIfPhCurOutBcastPkts15Min": adIfPhCurOutBcastPkts15Min,
       "adIfPhCurOutDiscards15Min": adIfPhCurOutDiscards15Min,
       "adIfPhCurOutErrors15Min": adIfPhCurOutErrors15Min,
       "adIfPhCurTimeElapsed1Day": adIfPhCurTimeElapsed1Day,
       "adIfPhCurValidIntervals1Day": adIfPhCurValidIntervals1Day,
       "adIfPhCurInvalidIntervals1Day": adIfPhCurInvalidIntervals1Day,
       "adIfPhCurInOctets1Day": adIfPhCurInOctets1Day,
       "adIfPhCurInUcastPkts1Day": adIfPhCurInUcastPkts1Day,
       "adIfPhCurInMcastPkts1Day": adIfPhCurInMcastPkts1Day,
       "adIfPhCurInBcastPkts1Day": adIfPhCurInBcastPkts1Day,
       "adIfPhCurInDiscards1Day": adIfPhCurInDiscards1Day,
       "adIfPhCurInErrors1Day": adIfPhCurInErrors1Day,
       "adIfPhCurInUnknownProtos1Day": adIfPhCurInUnknownProtos1Day,
       "adIfPhCurOutOctets1Day": adIfPhCurOutOctets1Day,
       "adIfPhCurOutUcastPkts1Day": adIfPhCurOutUcastPkts1Day,
       "adIfPhCurOutMcastPkts1Day": adIfPhCurOutMcastPkts1Day,
       "adIfPhCurOutBcastPkts1Day": adIfPhCurOutBcastPkts1Day,
       "adIfPhCurOutDiscards1Day": adIfPhCurOutDiscards1Day,
       "adIfPhCurOutErrors1Day": adIfPhCurOutErrors1Day,
       "adIfPh15MinIntervalTable": adIfPh15MinIntervalTable,
       "adIfPh15MinIntervalEntry": adIfPh15MinIntervalEntry,
       "adIfPh15MinIntervalNumber": adIfPh15MinIntervalNumber,
       "adIfPh15MinInOctets": adIfPh15MinInOctets,
       "adIfPh15MinInUcastPkts": adIfPh15MinInUcastPkts,
       "adIfPh15MinInMcastPkts": adIfPh15MinInMcastPkts,
       "adIfPh15MinInBcastPkts": adIfPh15MinInBcastPkts,
       "adIfPh15MinInDiscards": adIfPh15MinInDiscards,
       "adIfPh15MinInErrors": adIfPh15MinInErrors,
       "adIfPh15MinInUnknownProtos": adIfPh15MinInUnknownProtos,
       "adIfPh15MinOutOctets": adIfPh15MinOutOctets,
       "adIfPh15MinOutUcastPkts": adIfPh15MinOutUcastPkts,
       "adIfPh15MinOutMcastPkts": adIfPh15MinOutMcastPkts,
       "adIfPh15MinOutBcastPkts": adIfPh15MinOutBcastPkts,
       "adIfPh15MinOutDiscards": adIfPh15MinOutDiscards,
       "adIfPh15MinOutErrors": adIfPh15MinOutErrors,
       "adIfPh1DayIntervalTable": adIfPh1DayIntervalTable,
       "adIfPh1DayIntervalEntry": adIfPh1DayIntervalEntry,
       "adIfPh1DayIntervalNumber": adIfPh1DayIntervalNumber,
       "adIfPh1DayInOctets": adIfPh1DayInOctets,
       "adIfPh1DayInUcastPkts": adIfPh1DayInUcastPkts,
       "adIfPh1DayInMcastPkts": adIfPh1DayInMcastPkts,
       "adIfPh1DayInBcastPkts": adIfPh1DayInBcastPkts,
       "adIfPh1DayInDiscards": adIfPh1DayInDiscards,
       "adIfPh1DayInErrors": adIfPh1DayInErrors,
       "adIfPh1DayInUnknownProtos": adIfPh1DayInUnknownProtos,
       "adIfPh1DayOutOctets": adIfPh1DayOutOctets,
       "adIfPh1DayOutUcastPkts": adIfPh1DayOutUcastPkts,
       "adIfPh1DayOutMcastPkts": adIfPh1DayOutMcastPkts,
       "adIfPh1DayOutBcastPkts": adIfPh1DayOutBcastPkts,
       "adIfPh1DayOutDiscards": adIfPh1DayOutDiscards,
       "adIfPh1DayOutErrors": adIfPh1DayOutErrors,
       "adGenAosIfPerfHistoryConformance": adGenAosIfPerfHistoryConformance,
       "adGenAosIfPerfHistoryGroups": adGenAosIfPerfHistoryGroups,
       "adIfPhCurGroup": adIfPhCurGroup,
       "adIfPh15MinIntervalGroup": adIfPh15MinIntervalGroup,
       "adIfPh1DayIntervalGroup": adIfPh1DayIntervalGroup,
       "adGenAosIfPerfHistoryCompliances": adGenAosIfPerfHistoryCompliances,
       "adGenAosIfPerfHistoryCompliance": adGenAosIfPerfHistoryCompliance,
       "adGenAosIfPerfHistoryMib": adGenAosIfPerfHistoryMib}
)
