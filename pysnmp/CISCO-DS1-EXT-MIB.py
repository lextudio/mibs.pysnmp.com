# SNMP MIB module (CISCO-DS1-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DS1-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:04 2024
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

(BulkConfigResult,
 ConfigIterator) = mibBuilder.importSymbols(
    "CISCO-TC",
    "BulkConfigResult",
    "ConfigIterator")

(dsx1ConfigEntry,
 dsx1CurrentEntry,
 dsx1FarEndCurrentEntry,
 dsx1FarEndIntervalEntry,
 dsx1FarEndTotalEntry,
 dsx1IntervalEntry,
 dsx1TotalEntry) = mibBuilder.importSymbols(
    "DS1-MIB",
    "dsx1ConfigEntry",
    "dsx1CurrentEntry",
    "dsx1FarEndCurrentEntry",
    "dsx1FarEndIntervalEntry",
    "dsx1FarEndTotalEntry",
    "dsx1IntervalEntry",
    "dsx1TotalEntry")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDs1ExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 229)
)
ciscoDs1ExtMIB.setRevisions(
        ("2003-02-25 00:00",
         "2002-12-30 00:00",
         "2001-09-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PerfCurrent24HourCount(Gauge32, TextualConvention):
    status = "current"


class PerfPrevious24HourCount(Gauge32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoDs1MIBObjects_ObjectIdentity = ObjectIdentity
ciscoDs1MIBObjects = _CiscoDs1MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1)
)
_Cds1Config_ObjectIdentity = ObjectIdentity
cds1Config = _Cds1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 1)
)
_Cds1ConfigTable_Object = MibTable
cds1ConfigTable = _Cds1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cds1ConfigTable.setStatus("current")
_Cds1ConfigEntry_Object = MibTableRow
cds1ConfigEntry = _Cds1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cds1ConfigEntry.setStatus("current")


class _Cds1LineType_Type(Integer32):
    """Custom type cds1LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("dsx1D4", 3),
          ("dsx1DS2M12", 10),
          ("dsx1E1", 4),
          ("dsx1E1CRC", 5),
          ("dsx1E1CRCMF", 7),
          ("dsx1E1MF", 6),
          ("dsx1E1Q50", 20),
          ("dsx1E1Q50CRC", 21),
          ("dsx1E1Unframed", 9),
          ("dsx1ESF", 2),
          ("dsx1Unframed", 8),
          ("dsx2E2", 11),
          ("other", 1))
    )


_Cds1LineType_Type.__name__ = "Integer32"
_Cds1LineType_Object = MibTableColumn
cds1LineType = _Cds1LineType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 1, 1, 1, 1),
    _Cds1LineType_Type()
)
cds1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds1LineType.setStatus("current")


class _Cds1LoopbackCodeDetection_Type(TruthValue):
    """Custom type cds1LoopbackCodeDetection based on TruthValue"""


_Cds1LoopbackCodeDetection_Object = MibTableColumn
cds1LoopbackCodeDetection = _Cds1LoopbackCodeDetection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 1, 1, 1, 2),
    _Cds1LoopbackCodeDetection_Type()
)
cds1LoopbackCodeDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds1LoopbackCodeDetection.setStatus("current")


class _Cds1Repetition_Type(ConfigIterator):
    """Custom type cds1Repetition based on ConfigIterator"""
    defaultValue = 1


_Cds1Repetition_Object = MibTableColumn
cds1Repetition = _Cds1Repetition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 1, 1, 1, 3),
    _Cds1Repetition_Type()
)
cds1Repetition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds1Repetition.setStatus("current")
_Cds1RepetitionOwner_Type = OwnerString
_Cds1RepetitionOwner_Object = MibTableColumn
cds1RepetitionOwner = _Cds1RepetitionOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 1, 1, 1, 4),
    _Cds1RepetitionOwner_Type()
)
cds1RepetitionOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds1RepetitionOwner.setStatus("current")
_Cds1RepetitionResult_Type = BulkConfigResult
_Cds1RepetitionResult_Object = MibTableColumn
cds1RepetitionResult = _Cds1RepetitionResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 1, 1, 1, 5),
    _Cds1RepetitionResult_Type()
)
cds1RepetitionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1RepetitionResult.setStatus("current")
_Cds1CallConfigTable_Object = MibTable
cds1CallConfigTable = _Cds1CallConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cds1CallConfigTable.setStatus("current")
_Cds1CallConfigEntry_Object = MibTableRow
cds1CallConfigEntry = _Cds1CallConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cds1CallConfigEntry.setStatus("current")


class _Cds1CallTrunkConditionEnable_Type(TruthValue):
    """Custom type cds1CallTrunkConditionEnable based on TruthValue"""


_Cds1CallTrunkConditionEnable_Object = MibTableColumn
cds1CallTrunkConditionEnable = _Cds1CallTrunkConditionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 1, 2, 1, 1),
    _Cds1CallTrunkConditionEnable_Type()
)
cds1CallTrunkConditionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds1CallTrunkConditionEnable.setStatus("current")
_Cds1Alarm_ObjectIdentity = ObjectIdentity
cds1Alarm = _Cds1Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2)
)
_Cds1AlarmThresholdGroupTable_Object = MibTable
cds1AlarmThresholdGroupTable = _Cds1AlarmThresholdGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cds1AlarmThresholdGroupTable.setStatus("current")
_Cds1AlarmThresholdGroupEntry_Object = MibTableRow
cds1AlarmThresholdGroupEntry = _Cds1AlarmThresholdGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1)
)
cds1AlarmThresholdGroupEntry.setIndexNames(
    (0, "CISCO-DS1-EXT-MIB", "cds1AlarmThresholdGroupIndex"),
)
if mibBuilder.loadTexts:
    cds1AlarmThresholdGroupEntry.setStatus("current")


class _Cds1AlarmThresholdGroupIndex_Type(Integer32):
    """Custom type cds1AlarmThresholdGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Cds1AlarmThresholdGroupIndex_Type.__name__ = "Integer32"
_Cds1AlarmThresholdGroupIndex_Object = MibTableColumn
cds1AlarmThresholdGroupIndex = _Cds1AlarmThresholdGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 1),
    _Cds1AlarmThresholdGroupIndex_Type()
)
cds1AlarmThresholdGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cds1AlarmThresholdGroupIndex.setStatus("current")


class _Cds1Current15MinBESsThreshold_Type(Integer32):
    """Custom type cds1Current15MinBESsThreshold based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current15MinBESsThreshold_Type.__name__ = "Integer32"
_Cds1Current15MinBESsThreshold_Object = MibTableColumn
cds1Current15MinBESsThreshold = _Cds1Current15MinBESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 2),
    _Cds1Current15MinBESsThreshold_Type()
)
cds1Current15MinBESsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current15MinBESsThreshold.setStatus("current")


class _Cds1Current24HrBESsThreshold_Type(Integer32):
    """Custom type cds1Current24HrBESsThreshold based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current24HrBESsThreshold_Type.__name__ = "Integer32"
_Cds1Current24HrBESsThreshold_Object = MibTableColumn
cds1Current24HrBESsThreshold = _Cds1Current24HrBESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 3),
    _Cds1Current24HrBESsThreshold_Type()
)
cds1Current24HrBESsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current24HrBESsThreshold.setStatus("current")


class _Cds1Current15MinCSSsThreshold_Type(Integer32):
    """Custom type cds1Current15MinCSSsThreshold based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current15MinCSSsThreshold_Type.__name__ = "Integer32"
_Cds1Current15MinCSSsThreshold_Object = MibTableColumn
cds1Current15MinCSSsThreshold = _Cds1Current15MinCSSsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 4),
    _Cds1Current15MinCSSsThreshold_Type()
)
cds1Current15MinCSSsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current15MinCSSsThreshold.setStatus("current")


class _Cds1Current24HrCSSsThreshold_Type(Integer32):
    """Custom type cds1Current24HrCSSsThreshold based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current24HrCSSsThreshold_Type.__name__ = "Integer32"
_Cds1Current24HrCSSsThreshold_Object = MibTableColumn
cds1Current24HrCSSsThreshold = _Cds1Current24HrCSSsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 5),
    _Cds1Current24HrCSSsThreshold_Type()
)
cds1Current24HrCSSsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current24HrCSSsThreshold.setStatus("current")


class _Cds1Current15MinDMsThreshold_Type(Integer32):
    """Custom type cds1Current15MinDMsThreshold based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current15MinDMsThreshold_Type.__name__ = "Integer32"
_Cds1Current15MinDMsThreshold_Object = MibTableColumn
cds1Current15MinDMsThreshold = _Cds1Current15MinDMsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 6),
    _Cds1Current15MinDMsThreshold_Type()
)
cds1Current15MinDMsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current15MinDMsThreshold.setStatus("current")


class _Cds1Current24HrDMsThreshold_Type(Integer32):
    """Custom type cds1Current24HrDMsThreshold based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current24HrDMsThreshold_Type.__name__ = "Integer32"
_Cds1Current24HrDMsThreshold_Object = MibTableColumn
cds1Current24HrDMsThreshold = _Cds1Current24HrDMsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 7),
    _Cds1Current24HrDMsThreshold_Type()
)
cds1Current24HrDMsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current24HrDMsThreshold.setStatus("current")


class _Cds1Current15MinESsThreshold_Type(Integer32):
    """Custom type cds1Current15MinESsThreshold based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current15MinESsThreshold_Type.__name__ = "Integer32"
_Cds1Current15MinESsThreshold_Object = MibTableColumn
cds1Current15MinESsThreshold = _Cds1Current15MinESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 8),
    _Cds1Current15MinESsThreshold_Type()
)
cds1Current15MinESsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current15MinESsThreshold.setStatus("current")


class _Cds1Current24HrESsThreshold_Type(Integer32):
    """Custom type cds1Current24HrESsThreshold based on Integer32"""
    defaultValue = 121

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current24HrESsThreshold_Type.__name__ = "Integer32"
_Cds1Current24HrESsThreshold_Object = MibTableColumn
cds1Current24HrESsThreshold = _Cds1Current24HrESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 9),
    _Cds1Current24HrESsThreshold_Type()
)
cds1Current24HrESsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current24HrESsThreshold.setStatus("current")


class _Cds1Current15MinLCVsThreshold_Type(Integer32):
    """Custom type cds1Current15MinLCVsThreshold based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current15MinLCVsThreshold_Type.__name__ = "Integer32"
_Cds1Current15MinLCVsThreshold_Object = MibTableColumn
cds1Current15MinLCVsThreshold = _Cds1Current15MinLCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 10),
    _Cds1Current15MinLCVsThreshold_Type()
)
cds1Current15MinLCVsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current15MinLCVsThreshold.setStatus("current")


class _Cds1Current24HrLCVsThreshold_Type(Integer32):
    """Custom type cds1Current24HrLCVsThreshold based on Integer32"""
    defaultValue = 134

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current24HrLCVsThreshold_Type.__name__ = "Integer32"
_Cds1Current24HrLCVsThreshold_Object = MibTableColumn
cds1Current24HrLCVsThreshold = _Cds1Current24HrLCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 11),
    _Cds1Current24HrLCVsThreshold_Type()
)
cds1Current24HrLCVsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current24HrLCVsThreshold.setStatus("current")


class _Cds1Current15MinLESsThreshold_Type(Integer32):
    """Custom type cds1Current15MinLESsThreshold based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current15MinLESsThreshold_Type.__name__ = "Integer32"
_Cds1Current15MinLESsThreshold_Object = MibTableColumn
cds1Current15MinLESsThreshold = _Cds1Current15MinLESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 12),
    _Cds1Current15MinLESsThreshold_Type()
)
cds1Current15MinLESsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current15MinLESsThreshold.setStatus("current")


class _Cds1Current24HrLESsThreshold_Type(Integer32):
    """Custom type cds1Current24HrLESsThreshold based on Integer32"""
    defaultValue = 121

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current24HrLESsThreshold_Type.__name__ = "Integer32"
_Cds1Current24HrLESsThreshold_Object = MibTableColumn
cds1Current24HrLESsThreshold = _Cds1Current24HrLESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 13),
    _Cds1Current24HrLESsThreshold_Type()
)
cds1Current24HrLESsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current24HrLESsThreshold.setStatus("current")


class _Cds1Current15MinLSESsThreshold_Type(Integer32):
    """Custom type cds1Current15MinLSESsThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current15MinLSESsThreshold_Type.__name__ = "Integer32"
_Cds1Current15MinLSESsThreshold_Object = MibTableColumn
cds1Current15MinLSESsThreshold = _Cds1Current15MinLSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 14),
    _Cds1Current15MinLSESsThreshold_Type()
)
cds1Current15MinLSESsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current15MinLSESsThreshold.setStatus("current")


class _Cds1Current24HrLSESsThreshold_Type(Integer32):
    """Custom type cds1Current24HrLSESsThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current24HrLSESsThreshold_Type.__name__ = "Integer32"
_Cds1Current24HrLSESsThreshold_Object = MibTableColumn
cds1Current24HrLSESsThreshold = _Cds1Current24HrLSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 15),
    _Cds1Current24HrLSESsThreshold_Type()
)
cds1Current24HrLSESsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current24HrLSESsThreshold.setStatus("current")


class _Cds1Current15MinPCVsThreshold_Type(Integer32):
    """Custom type cds1Current15MinPCVsThreshold based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current15MinPCVsThreshold_Type.__name__ = "Integer32"
_Cds1Current15MinPCVsThreshold_Object = MibTableColumn
cds1Current15MinPCVsThreshold = _Cds1Current15MinPCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 16),
    _Cds1Current15MinPCVsThreshold_Type()
)
cds1Current15MinPCVsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current15MinPCVsThreshold.setStatus("current")


class _Cds1Current24HrPCVsThreshold_Type(Integer32):
    """Custom type cds1Current24HrPCVsThreshold based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current24HrPCVsThreshold_Type.__name__ = "Integer32"
_Cds1Current24HrPCVsThreshold_Object = MibTableColumn
cds1Current24HrPCVsThreshold = _Cds1Current24HrPCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 17),
    _Cds1Current24HrPCVsThreshold_Type()
)
cds1Current24HrPCVsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current24HrPCVsThreshold.setStatus("current")


class _Cds1Current15MinPSASsThreshold_Type(Integer32):
    """Custom type cds1Current15MinPSASsThreshold based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current15MinPSASsThreshold_Type.__name__ = "Integer32"
_Cds1Current15MinPSASsThreshold_Object = MibTableColumn
cds1Current15MinPSASsThreshold = _Cds1Current15MinPSASsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 18),
    _Cds1Current15MinPSASsThreshold_Type()
)
cds1Current15MinPSASsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current15MinPSASsThreshold.setStatus("current")


class _Cds1Current24HrPSASsThreshold_Type(Integer32):
    """Custom type cds1Current24HrPSASsThreshold based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current24HrPSASsThreshold_Type.__name__ = "Integer32"
_Cds1Current24HrPSASsThreshold_Object = MibTableColumn
cds1Current24HrPSASsThreshold = _Cds1Current24HrPSASsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 19),
    _Cds1Current24HrPSASsThreshold_Type()
)
cds1Current24HrPSASsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current24HrPSASsThreshold.setStatus("current")


class _Cds1Current15MinSESsThreshold_Type(Integer32):
    """Custom type cds1Current15MinSESsThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current15MinSESsThreshold_Type.__name__ = "Integer32"
_Cds1Current15MinSESsThreshold_Object = MibTableColumn
cds1Current15MinSESsThreshold = _Cds1Current15MinSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 20),
    _Cds1Current15MinSESsThreshold_Type()
)
cds1Current15MinSESsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current15MinSESsThreshold.setStatus("current")


class _Cds1Current24HrSESsThreshold_Type(Integer32):
    """Custom type cds1Current24HrSESsThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current24HrSESsThreshold_Type.__name__ = "Integer32"
_Cds1Current24HrSESsThreshold_Object = MibTableColumn
cds1Current24HrSESsThreshold = _Cds1Current24HrSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 21),
    _Cds1Current24HrSESsThreshold_Type()
)
cds1Current24HrSESsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current24HrSESsThreshold.setStatus("current")


class _Cds1Current15MinSEFSsThreshold_Type(Integer32):
    """Custom type cds1Current15MinSEFSsThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current15MinSEFSsThreshold_Type.__name__ = "Integer32"
_Cds1Current15MinSEFSsThreshold_Object = MibTableColumn
cds1Current15MinSEFSsThreshold = _Cds1Current15MinSEFSsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 22),
    _Cds1Current15MinSEFSsThreshold_Type()
)
cds1Current15MinSEFSsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current15MinSEFSsThreshold.setStatus("current")


class _Cds1Current24HrSEFSsThreshold_Type(Integer32):
    """Custom type cds1Current24HrSEFSsThreshold based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current24HrSEFSsThreshold_Type.__name__ = "Integer32"
_Cds1Current24HrSEFSsThreshold_Object = MibTableColumn
cds1Current24HrSEFSsThreshold = _Cds1Current24HrSEFSsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 23),
    _Cds1Current24HrSEFSsThreshold_Type()
)
cds1Current24HrSEFSsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current24HrSEFSsThreshold.setStatus("current")


class _Cds1Current15MinUASsThreshold_Type(Integer32):
    """Custom type cds1Current15MinUASsThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current15MinUASsThreshold_Type.__name__ = "Integer32"
_Cds1Current15MinUASsThreshold_Object = MibTableColumn
cds1Current15MinUASsThreshold = _Cds1Current15MinUASsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 24),
    _Cds1Current15MinUASsThreshold_Type()
)
cds1Current15MinUASsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current15MinUASsThreshold.setStatus("current")


class _Cds1Current24HrUASsThreshold_Type(Integer32):
    """Custom type cds1Current24HrUASsThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1Current24HrUASsThreshold_Type.__name__ = "Integer32"
_Cds1Current24HrUASsThreshold_Object = MibTableColumn
cds1Current24HrUASsThreshold = _Cds1Current24HrUASsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 25),
    _Cds1Current24HrUASsThreshold_Type()
)
cds1Current24HrUASsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1Current24HrUASsThreshold.setStatus("current")
_Cds1AlarmThresholdGroupRowStatus_Type = RowStatus
_Cds1AlarmThresholdGroupRowStatus_Object = MibTableColumn
cds1AlarmThresholdGroupRowStatus = _Cds1AlarmThresholdGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 1, 1, 26),
    _Cds1AlarmThresholdGroupRowStatus_Type()
)
cds1AlarmThresholdGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cds1AlarmThresholdGroupRowStatus.setStatus("current")
_Cds1AlarmConfigTable_Object = MibTable
cds1AlarmConfigTable = _Cds1AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cds1AlarmConfigTable.setStatus("current")
_Cds1AlarmConfigEntry_Object = MibTableRow
cds1AlarmConfigEntry = _Cds1AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cds1AlarmConfigEntry.setStatus("current")


class _Cds1StatisticalAlarmSeverity_Type(Integer32):
    """Custom type cds1StatisticalAlarmSeverity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1),
          ("none", 3))
    )


_Cds1StatisticalAlarmSeverity_Type.__name__ = "Integer32"
_Cds1StatisticalAlarmSeverity_Object = MibTableColumn
cds1StatisticalAlarmSeverity = _Cds1StatisticalAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 2, 1, 1),
    _Cds1StatisticalAlarmSeverity_Type()
)
cds1StatisticalAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds1StatisticalAlarmSeverity.setStatus("current")


class _Cds1StatisticalAlarmState_Type(Bits):
    """Custom type cds1StatisticalAlarmState based on Bits"""
    namedValues = NamedValues(
        *(("cds1BES15Min", 0),
          ("cds1BES24Hr", 1),
          ("cds1CSS15Min", 2),
          ("cds1CSS24Hr", 3),
          ("cds1DM15Min", 4),
          ("cds1DM24Hr", 5),
          ("cds1ES15Min", 6),
          ("cds1ES24Hr", 7),
          ("cds1LCV15Min", 10),
          ("cds1LCV24Hr", 11),
          ("cds1LES15Min", 12),
          ("cds1LES24Hr", 13),
          ("cds1LSES15Min", 14),
          ("cds1LSES24Hr", 15),
          ("cds1PCV15Min", 8),
          ("cds1PCV24Hr", 9),
          ("cds1PSAS15Min", 16),
          ("cds1PSAS24Hr", 17),
          ("cds1SEFS15Min", 20),
          ("cds1SEFS24Hr", 21),
          ("cds1SES15Min", 18),
          ("cds1SES24Hr", 19),
          ("cds1UAS15Min", 22),
          ("cds1UAS24Hr", 23))
    )

_Cds1StatisticalAlarmState_Type.__name__ = "Bits"
_Cds1StatisticalAlarmState_Object = MibTableColumn
cds1StatisticalAlarmState = _Cds1StatisticalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 2, 1, 2),
    _Cds1StatisticalAlarmState_Type()
)
cds1StatisticalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1StatisticalAlarmState.setStatus("current")


class _Cds1AlarmUpCount_Type(Integer32):
    """Custom type cds1AlarmUpCount based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1AlarmUpCount_Type.__name__ = "Integer32"
_Cds1AlarmUpCount_Object = MibTableColumn
cds1AlarmUpCount = _Cds1AlarmUpCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 2, 1, 3),
    _Cds1AlarmUpCount_Type()
)
cds1AlarmUpCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds1AlarmUpCount.setStatus("current")


class _Cds1AlarmDownCount_Type(Integer32):
    """Custom type cds1AlarmDownCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1AlarmDownCount_Type.__name__ = "Integer32"
_Cds1AlarmDownCount_Object = MibTableColumn
cds1AlarmDownCount = _Cds1AlarmDownCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 2, 1, 4),
    _Cds1AlarmDownCount_Type()
)
cds1AlarmDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds1AlarmDownCount.setStatus("current")


class _Cds1AlarmThreshold_Type(Integer32):
    """Custom type cds1AlarmThreshold based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cds1AlarmThreshold_Type.__name__ = "Integer32"
_Cds1AlarmThreshold_Object = MibTableColumn
cds1AlarmThreshold = _Cds1AlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 2, 1, 5),
    _Cds1AlarmThreshold_Type()
)
cds1AlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds1AlarmThreshold.setStatus("current")


class _Cds1AlarmThresholdActiveGroup_Type(Integer32):
    """Custom type cds1AlarmThresholdActiveGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Cds1AlarmThresholdActiveGroup_Type.__name__ = "Integer32"
_Cds1AlarmThresholdActiveGroup_Object = MibTableColumn
cds1AlarmThresholdActiveGroup = _Cds1AlarmThresholdActiveGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 2, 2, 1, 6),
    _Cds1AlarmThresholdActiveGroup_Type()
)
cds1AlarmThresholdActiveGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cds1AlarmThresholdActiveGroup.setStatus("current")
_Cds1Stats_ObjectIdentity = ObjectIdentity
cds1Stats = _Cds1Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3)
)
_Cds1CurrentTable_Object = MibTable
cds1CurrentTable = _Cds1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cds1CurrentTable.setStatus("current")
_Cds1CurrentEntry_Object = MibTableRow
cds1CurrentEntry = _Cds1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cds1CurrentEntry.setStatus("current")
_Cds1CurrentLSESs_Type = PerfCurrentCount
_Cds1CurrentLSESs_Object = MibTableColumn
cds1CurrentLSESs = _Cds1CurrentLSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 1, 1, 1),
    _Cds1CurrentLSESs_Type()
)
cds1CurrentLSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1CurrentLSESs.setStatus("current")
_Cds1CurrentPSASs_Type = PerfCurrentCount
_Cds1CurrentPSASs_Object = MibTableColumn
cds1CurrentPSASs = _Cds1CurrentPSASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 1, 1, 2),
    _Cds1CurrentPSASs_Type()
)
cds1CurrentPSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1CurrentPSASs.setStatus("current")
_Cds1IntervalTable_Object = MibTable
cds1IntervalTable = _Cds1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cds1IntervalTable.setStatus("current")
_Cds1IntervalEntry_Object = MibTableRow
cds1IntervalEntry = _Cds1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cds1IntervalEntry.setStatus("current")
_Cds1IntervalLSESs_Type = PerfIntervalCount
_Cds1IntervalLSESs_Object = MibTableColumn
cds1IntervalLSESs = _Cds1IntervalLSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 2, 1, 1),
    _Cds1IntervalLSESs_Type()
)
cds1IntervalLSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1IntervalLSESs.setStatus("current")
_Cds1IntervalPSASs_Type = PerfIntervalCount
_Cds1IntervalPSASs_Object = MibTableColumn
cds1IntervalPSASs = _Cds1IntervalPSASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 2, 1, 2),
    _Cds1IntervalPSASs_Type()
)
cds1IntervalPSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1IntervalPSASs.setStatus("current")
_Cds1TotalTable_Object = MibTable
cds1TotalTable = _Cds1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cds1TotalTable.setStatus("current")
_Cds1TotalEntry_Object = MibTableRow
cds1TotalEntry = _Cds1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cds1TotalEntry.setStatus("current")
_Cds1TotalLSESs_Type = PerfTotalCount
_Cds1TotalLSESs_Object = MibTableColumn
cds1TotalLSESs = _Cds1TotalLSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 3, 1, 1),
    _Cds1TotalLSESs_Type()
)
cds1TotalLSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1TotalLSESs.setStatus("current")
_Cds1TotalPSASs_Type = PerfTotalCount
_Cds1TotalPSASs_Object = MibTableColumn
cds1TotalPSASs = _Cds1TotalPSASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 3, 1, 2),
    _Cds1TotalPSASs_Type()
)
cds1TotalPSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1TotalPSASs.setStatus("current")
_Cds1FarEndCurrentTable_Object = MibTable
cds1FarEndCurrentTable = _Cds1FarEndCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cds1FarEndCurrentTable.setStatus("current")
_Cds1FarEndCurrentEntry_Object = MibTableRow
cds1FarEndCurrentEntry = _Cds1FarEndCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    cds1FarEndCurrentEntry.setStatus("current")
_Cds1FarEndCurrentLOFCs_Type = PerfCurrentCount
_Cds1FarEndCurrentLOFCs_Object = MibTableColumn
cds1FarEndCurrentLOFCs = _Cds1FarEndCurrentLOFCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 4, 1, 1),
    _Cds1FarEndCurrentLOFCs_Type()
)
cds1FarEndCurrentLOFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1FarEndCurrentLOFCs.setStatus("current")
_Cds1FarEndIntervalTable_Object = MibTable
cds1FarEndIntervalTable = _Cds1FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cds1FarEndIntervalTable.setStatus("current")
_Cds1FarEndIntervalEntry_Object = MibTableRow
cds1FarEndIntervalEntry = _Cds1FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    cds1FarEndIntervalEntry.setStatus("current")
_Cds1FarEndIntervalLOFCs_Type = PerfIntervalCount
_Cds1FarEndIntervalLOFCs_Object = MibTableColumn
cds1FarEndIntervalLOFCs = _Cds1FarEndIntervalLOFCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 5, 1, 1),
    _Cds1FarEndIntervalLOFCs_Type()
)
cds1FarEndIntervalLOFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1FarEndIntervalLOFCs.setStatus("current")
_Cds1FarEndTotalTable_Object = MibTable
cds1FarEndTotalTable = _Cds1FarEndTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cds1FarEndTotalTable.setStatus("current")
_Cds1FarEndTotalEntry_Object = MibTableRow
cds1FarEndTotalEntry = _Cds1FarEndTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    cds1FarEndTotalEntry.setStatus("current")
_Cds1FarEndTotalLOFCs_Type = PerfTotalCount
_Cds1FarEndTotalLOFCs_Object = MibTableColumn
cds1FarEndTotalLOFCs = _Cds1FarEndTotalLOFCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 6, 1, 1),
    _Cds1FarEndTotalLOFCs_Type()
)
cds1FarEndTotalLOFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1FarEndTotalLOFCs.setStatus("current")
_Cds1Current24HrStatsTable_Object = MibTable
cds1Current24HrStatsTable = _Cds1Current24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cds1Current24HrStatsTable.setStatus("current")
_Cds1Current24HrStatsEntry_Object = MibTableRow
cds1Current24HrStatsEntry = _Cds1Current24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 7, 1)
)
cds1Current24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cds1Current24HrStatsEntry.setStatus("current")
_Cds1Current24HrESs_Type = PerfCurrent24HourCount
_Cds1Current24HrESs_Object = MibTableColumn
cds1Current24HrESs = _Cds1Current24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 7, 1, 1),
    _Cds1Current24HrESs_Type()
)
cds1Current24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Current24HrESs.setStatus("current")
_Cds1Current24HrSESs_Type = PerfCurrent24HourCount
_Cds1Current24HrSESs_Object = MibTableColumn
cds1Current24HrSESs = _Cds1Current24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 7, 1, 2),
    _Cds1Current24HrSESs_Type()
)
cds1Current24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Current24HrSESs.setStatus("current")
_Cds1Current24HrSEFSs_Type = PerfCurrent24HourCount
_Cds1Current24HrSEFSs_Object = MibTableColumn
cds1Current24HrSEFSs = _Cds1Current24HrSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 7, 1, 3),
    _Cds1Current24HrSEFSs_Type()
)
cds1Current24HrSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Current24HrSEFSs.setStatus("current")
_Cds1Current24HrUASs_Type = PerfCurrent24HourCount
_Cds1Current24HrUASs_Object = MibTableColumn
cds1Current24HrUASs = _Cds1Current24HrUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 7, 1, 4),
    _Cds1Current24HrUASs_Type()
)
cds1Current24HrUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Current24HrUASs.setStatus("current")
_Cds1Current24HrCSSs_Type = PerfCurrent24HourCount
_Cds1Current24HrCSSs_Object = MibTableColumn
cds1Current24HrCSSs = _Cds1Current24HrCSSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 7, 1, 5),
    _Cds1Current24HrCSSs_Type()
)
cds1Current24HrCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Current24HrCSSs.setStatus("current")
_Cds1Current24HrPCVs_Type = PerfCurrent24HourCount
_Cds1Current24HrPCVs_Object = MibTableColumn
cds1Current24HrPCVs = _Cds1Current24HrPCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 7, 1, 6),
    _Cds1Current24HrPCVs_Type()
)
cds1Current24HrPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Current24HrPCVs.setStatus("current")
_Cds1Current24HrLESs_Type = PerfCurrent24HourCount
_Cds1Current24HrLESs_Object = MibTableColumn
cds1Current24HrLESs = _Cds1Current24HrLESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 7, 1, 7),
    _Cds1Current24HrLESs_Type()
)
cds1Current24HrLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Current24HrLESs.setStatus("current")
_Cds1Current24HrBESs_Type = PerfCurrent24HourCount
_Cds1Current24HrBESs_Object = MibTableColumn
cds1Current24HrBESs = _Cds1Current24HrBESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 7, 1, 8),
    _Cds1Current24HrBESs_Type()
)
cds1Current24HrBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Current24HrBESs.setStatus("current")
_Cds1Current24HrDMs_Type = PerfCurrent24HourCount
_Cds1Current24HrDMs_Object = MibTableColumn
cds1Current24HrDMs = _Cds1Current24HrDMs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 7, 1, 9),
    _Cds1Current24HrDMs_Type()
)
cds1Current24HrDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Current24HrDMs.setStatus("current")
_Cds1Current24HrLCVs_Type = PerfCurrent24HourCount
_Cds1Current24HrLCVs_Object = MibTableColumn
cds1Current24HrLCVs = _Cds1Current24HrLCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 7, 1, 10),
    _Cds1Current24HrLCVs_Type()
)
cds1Current24HrLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Current24HrLCVs.setStatus("current")
_Cds1Previous24HrStatsTable_Object = MibTable
cds1Previous24HrStatsTable = _Cds1Previous24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 8)
)
if mibBuilder.loadTexts:
    cds1Previous24HrStatsTable.setStatus("current")
_Cds1Previous24HrStatsEntry_Object = MibTableRow
cds1Previous24HrStatsEntry = _Cds1Previous24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 8, 1)
)
cds1Previous24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cds1Previous24HrStatsEntry.setStatus("current")
_Cds1Previous24HrESs_Type = PerfPrevious24HourCount
_Cds1Previous24HrESs_Object = MibTableColumn
cds1Previous24HrESs = _Cds1Previous24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 8, 1, 1),
    _Cds1Previous24HrESs_Type()
)
cds1Previous24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Previous24HrESs.setStatus("current")
_Cds1Previous24HrSESs_Type = PerfPrevious24HourCount
_Cds1Previous24HrSESs_Object = MibTableColumn
cds1Previous24HrSESs = _Cds1Previous24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 8, 1, 2),
    _Cds1Previous24HrSESs_Type()
)
cds1Previous24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Previous24HrSESs.setStatus("current")
_Cds1Previous24HrSEFSs_Type = PerfPrevious24HourCount
_Cds1Previous24HrSEFSs_Object = MibTableColumn
cds1Previous24HrSEFSs = _Cds1Previous24HrSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 8, 1, 3),
    _Cds1Previous24HrSEFSs_Type()
)
cds1Previous24HrSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Previous24HrSEFSs.setStatus("current")
_Cds1Previous24HrUASs_Type = PerfPrevious24HourCount
_Cds1Previous24HrUASs_Object = MibTableColumn
cds1Previous24HrUASs = _Cds1Previous24HrUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 8, 1, 4),
    _Cds1Previous24HrUASs_Type()
)
cds1Previous24HrUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Previous24HrUASs.setStatus("current")
_Cds1Previous24HrCSSs_Type = PerfPrevious24HourCount
_Cds1Previous24HrCSSs_Object = MibTableColumn
cds1Previous24HrCSSs = _Cds1Previous24HrCSSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 8, 1, 5),
    _Cds1Previous24HrCSSs_Type()
)
cds1Previous24HrCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Previous24HrCSSs.setStatus("current")
_Cds1Previous24HrPCVs_Type = PerfPrevious24HourCount
_Cds1Previous24HrPCVs_Object = MibTableColumn
cds1Previous24HrPCVs = _Cds1Previous24HrPCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 8, 1, 6),
    _Cds1Previous24HrPCVs_Type()
)
cds1Previous24HrPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Previous24HrPCVs.setStatus("current")
_Cds1Previous24HrLESs_Type = PerfPrevious24HourCount
_Cds1Previous24HrLESs_Object = MibTableColumn
cds1Previous24HrLESs = _Cds1Previous24HrLESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 8, 1, 7),
    _Cds1Previous24HrLESs_Type()
)
cds1Previous24HrLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Previous24HrLESs.setStatus("current")
_Cds1Previous24HrBESs_Type = PerfPrevious24HourCount
_Cds1Previous24HrBESs_Object = MibTableColumn
cds1Previous24HrBESs = _Cds1Previous24HrBESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 8, 1, 8),
    _Cds1Previous24HrBESs_Type()
)
cds1Previous24HrBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Previous24HrBESs.setStatus("current")
_Cds1Previous24HrDMs_Type = PerfPrevious24HourCount
_Cds1Previous24HrDMs_Object = MibTableColumn
cds1Previous24HrDMs = _Cds1Previous24HrDMs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 8, 1, 9),
    _Cds1Previous24HrDMs_Type()
)
cds1Previous24HrDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Previous24HrDMs.setStatus("current")
_Cds1Previous24HrLCVs_Type = PerfPrevious24HourCount
_Cds1Previous24HrLCVs_Object = MibTableColumn
cds1Previous24HrLCVs = _Cds1Previous24HrLCVs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 8, 1, 10),
    _Cds1Previous24HrLCVs_Type()
)
cds1Previous24HrLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Previous24HrLCVs.setStatus("current")
_Cds1Previous24HrLSESs_Type = PerfPrevious24HourCount
_Cds1Previous24HrLSESs_Object = MibTableColumn
cds1Previous24HrLSESs = _Cds1Previous24HrLSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 8, 1, 11),
    _Cds1Previous24HrLSESs_Type()
)
cds1Previous24HrLSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1Previous24HrLSESs.setStatus("current")
_Cds1ErrStatsTable_Object = MibTable
cds1ErrStatsTable = _Cds1ErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 9)
)
if mibBuilder.loadTexts:
    cds1ErrStatsTable.setStatus("current")
_Cds1ErrStatsEntry_Object = MibTableRow
cds1ErrStatsEntry = _Cds1ErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 9, 1)
)
cds1ErrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cds1ErrStatsEntry.setStatus("current")
_Cds1LOSCounts_Type = Counter32
_Cds1LOSCounts_Object = MibTableColumn
cds1LOSCounts = _Cds1LOSCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 9, 1, 1),
    _Cds1LOSCounts_Type()
)
cds1LOSCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1LOSCounts.setStatus("current")
_Cds1OOFCounts_Type = Counter32
_Cds1OOFCounts_Object = MibTableColumn
cds1OOFCounts = _Cds1OOFCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 9, 1, 2),
    _Cds1OOFCounts_Type()
)
cds1OOFCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1OOFCounts.setStatus("current")
_Cds1RAICounts_Type = Counter32
_Cds1RAICounts_Object = MibTableColumn
cds1RAICounts = _Cds1RAICounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 9, 1, 3),
    _Cds1RAICounts_Type()
)
cds1RAICounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1RAICounts.setStatus("current")
_Cds1FECounts_Type = Counter32
_Cds1FECounts_Object = MibTableColumn
cds1FECounts = _Cds1FECounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 3, 9, 1, 4),
    _Cds1FECounts_Type()
)
cds1FECounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cds1FECounts.setStatus("current")
_Cds1NotificationPrefix_ObjectIdentity = ObjectIdentity
cds1NotificationPrefix = _Cds1NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 4)
)
_Cds1Notifications_ObjectIdentity = ObjectIdentity
cds1Notifications = _Cds1Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 4, 0)
)
_CiscoDs1MIBConformance_ObjectIdentity = ObjectIdentity
ciscoDs1MIBConformance = _CiscoDs1MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3)
)
_CiscoDs1MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDs1MIBCompliances = _CiscoDs1MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 1)
)
_CiscoDs1MIBGroups_ObjectIdentity = ObjectIdentity
ciscoDs1MIBGroups = _CiscoDs1MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2)
)
dsx1ConfigEntry.registerAugmentions(
    ("CISCO-DS1-EXT-MIB",
     "cds1ConfigEntry")
)
cds1ConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
dsx1ConfigEntry.registerAugmentions(
    ("CISCO-DS1-EXT-MIB",
     "cds1CallConfigEntry")
)
cds1CallConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
dsx1ConfigEntry.registerAugmentions(
    ("CISCO-DS1-EXT-MIB",
     "cds1AlarmConfigEntry")
)
cds1AlarmConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
dsx1CurrentEntry.registerAugmentions(
    ("CISCO-DS1-EXT-MIB",
     "cds1CurrentEntry")
)
cds1CurrentEntry.setIndexNames(*dsx1CurrentEntry.getIndexNames())
dsx1IntervalEntry.registerAugmentions(
    ("CISCO-DS1-EXT-MIB",
     "cds1IntervalEntry")
)
cds1IntervalEntry.setIndexNames(*dsx1IntervalEntry.getIndexNames())
dsx1TotalEntry.registerAugmentions(
    ("CISCO-DS1-EXT-MIB",
     "cds1TotalEntry")
)
cds1TotalEntry.setIndexNames(*dsx1TotalEntry.getIndexNames())
dsx1FarEndCurrentEntry.registerAugmentions(
    ("CISCO-DS1-EXT-MIB",
     "cds1FarEndCurrentEntry")
)
cds1FarEndCurrentEntry.setIndexNames(*dsx1FarEndCurrentEntry.getIndexNames())
dsx1FarEndIntervalEntry.registerAugmentions(
    ("CISCO-DS1-EXT-MIB",
     "cds1FarEndIntervalEntry")
)
cds1FarEndIntervalEntry.setIndexNames(*dsx1FarEndIntervalEntry.getIndexNames())
dsx1FarEndTotalEntry.registerAugmentions(
    ("CISCO-DS1-EXT-MIB",
     "cds1FarEndTotalEntry")
)
cds1FarEndTotalEntry.setIndexNames(*dsx1FarEndTotalEntry.getIndexNames())

# Managed Objects groups

ciscoDs1ConfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 1)
)
ciscoDs1ConfMIBGroup.setObjects(
      *(("CISCO-DS1-EXT-MIB", "cds1LineType"),
        ("CISCO-DS1-EXT-MIB", "cds1LoopbackCodeDetection"))
)
if mibBuilder.loadTexts:
    ciscoDs1ConfMIBGroup.setStatus("current")

ciscoDs1CurrentMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 2)
)
ciscoDs1CurrentMIBGroup.setObjects(
      *(("CISCO-DS1-EXT-MIB", "cds1CurrentLSESs"),
        ("CISCO-DS1-EXT-MIB", "cds1CurrentPSASs"))
)
if mibBuilder.loadTexts:
    ciscoDs1CurrentMIBGroup.setStatus("current")

ciscoDs1IntervalMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 3)
)
ciscoDs1IntervalMIBGroup.setObjects(
      *(("CISCO-DS1-EXT-MIB", "cds1IntervalLSESs"),
        ("CISCO-DS1-EXT-MIB", "cds1IntervalPSASs"))
)
if mibBuilder.loadTexts:
    ciscoDs1IntervalMIBGroup.setStatus("current")

ciscoDs1TotalMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 4)
)
ciscoDs1TotalMIBGroup.setObjects(
      *(("CISCO-DS1-EXT-MIB", "cds1TotalLSESs"),
        ("CISCO-DS1-EXT-MIB", "cds1TotalPSASs"))
)
if mibBuilder.loadTexts:
    ciscoDs1TotalMIBGroup.setStatus("current")

ciscoDs1FarEndStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 5)
)
ciscoDs1FarEndStatsMIBGroup.setObjects(
      *(("CISCO-DS1-EXT-MIB", "cds1FarEndCurrentLOFCs"),
        ("CISCO-DS1-EXT-MIB", "cds1FarEndIntervalLOFCs"),
        ("CISCO-DS1-EXT-MIB", "cds1FarEndTotalLOFCs"))
)
if mibBuilder.loadTexts:
    ciscoDs1FarEndStatsMIBGroup.setStatus("current")

ciscoDs1AlarmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 6)
)
ciscoDs1AlarmConfigGroup.setObjects(
      *(("CISCO-DS1-EXT-MIB", "cds1StatisticalAlarmSeverity"),
        ("CISCO-DS1-EXT-MIB", "cds1StatisticalAlarmState"),
        ("CISCO-DS1-EXT-MIB", "cds1AlarmUpCount"),
        ("CISCO-DS1-EXT-MIB", "cds1AlarmDownCount"),
        ("CISCO-DS1-EXT-MIB", "cds1AlarmThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1AlarmThresholdActiveGroup"))
)
if mibBuilder.loadTexts:
    ciscoDs1AlarmConfigGroup.setStatus("current")

ciscoDs1Alarm15MinThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 7)
)
ciscoDs1Alarm15MinThreshGroup.setObjects(
      *(("CISCO-DS1-EXT-MIB", "cds1Current15MinLCVsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinLESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinPCVsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinSEFSsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinUASsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinLSESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinSESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinBESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinDMsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinCSSsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinPSASsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1AlarmThresholdGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoDs1Alarm15MinThreshGroup.setStatus("deprecated")

ciscoDs1Alarm24HrThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 8)
)
ciscoDs1Alarm24HrThreshGroup.setObjects(
      *(("CISCO-DS1-EXT-MIB", "cds1Current24HrLCVsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrLESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrPCVsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrSEFSsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrUASsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrLSESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrSESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrBESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrCSSsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrDMsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrPSASsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1AlarmThresholdGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoDs1Alarm24HrThreshGroup.setStatus("deprecated")

ciscoDs1Current24HrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 9)
)
ciscoDs1Current24HrMIBGroup.setObjects(
      *(("CISCO-DS1-EXT-MIB", "cds1Current24HrESs"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrSESs"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrSEFSs"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrUASs"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrCSSs"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrPCVs"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrLESs"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrBESs"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrDMs"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrLCVs"))
)
if mibBuilder.loadTexts:
    ciscoDs1Current24HrMIBGroup.setStatus("current")

ciscoDs1Previous24HrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 10)
)
ciscoDs1Previous24HrMIBGroup.setObjects(
      *(("CISCO-DS1-EXT-MIB", "cds1Previous24HrESs"),
        ("CISCO-DS1-EXT-MIB", "cds1Previous24HrSESs"),
        ("CISCO-DS1-EXT-MIB", "cds1Previous24HrSEFSs"),
        ("CISCO-DS1-EXT-MIB", "cds1Previous24HrUASs"),
        ("CISCO-DS1-EXT-MIB", "cds1Previous24HrCSSs"),
        ("CISCO-DS1-EXT-MIB", "cds1Previous24HrPCVs"),
        ("CISCO-DS1-EXT-MIB", "cds1Previous24HrLESs"),
        ("CISCO-DS1-EXT-MIB", "cds1Previous24HrBESs"),
        ("CISCO-DS1-EXT-MIB", "cds1Previous24HrDMs"),
        ("CISCO-DS1-EXT-MIB", "cds1Previous24HrLCVs"),
        ("CISCO-DS1-EXT-MIB", "cds1Previous24HrLSESs"))
)
if mibBuilder.loadTexts:
    ciscoDs1Previous24HrMIBGroup.setStatus("current")

ciscoDs1StatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 11)
)
ciscoDs1StatsMIBGroup.setObjects(
      *(("CISCO-DS1-EXT-MIB", "cds1LOSCounts"),
        ("CISCO-DS1-EXT-MIB", "cds1OOFCounts"),
        ("CISCO-DS1-EXT-MIB", "cds1RAICounts"),
        ("CISCO-DS1-EXT-MIB", "cds1FECounts"))
)
if mibBuilder.loadTexts:
    ciscoDs1StatsMIBGroup.setStatus("current")

ciscoDs1BulkConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 13)
)
ciscoDs1BulkConfGroup.setObjects(
      *(("CISCO-DS1-EXT-MIB", "cds1Repetition"),
        ("CISCO-DS1-EXT-MIB", "cds1RepetitionOwner"),
        ("CISCO-DS1-EXT-MIB", "cds1RepetitionResult"))
)
if mibBuilder.loadTexts:
    ciscoDs1BulkConfGroup.setStatus("current")

ciscoDs1AlarmThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 14)
)
ciscoDs1AlarmThreshGroup.setObjects(
    ("CISCO-DS1-EXT-MIB", "cds1AlarmThresholdGroupRowStatus")
)
if mibBuilder.loadTexts:
    ciscoDs1AlarmThreshGroup.setStatus("current")

ciscoDs1Alarm15MinThreshGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 15)
)
ciscoDs1Alarm15MinThreshGroupRev1.setObjects(
      *(("CISCO-DS1-EXT-MIB", "cds1Current15MinLCVsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinLESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinPCVsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinSEFSsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinUASsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinLSESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinSESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinBESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinDMsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinCSSsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current15MinPSASsThreshold"))
)
if mibBuilder.loadTexts:
    ciscoDs1Alarm15MinThreshGroupRev1.setStatus("current")

ciscoDs1Alarm24HrThreshGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 16)
)
ciscoDs1Alarm24HrThreshGroupRev1.setObjects(
      *(("CISCO-DS1-EXT-MIB", "cds1Current24HrLCVsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrLESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrPCVsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrSEFSsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrUASsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrLSESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrSESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrBESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrCSSsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrDMsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrESsThreshold"),
        ("CISCO-DS1-EXT-MIB", "cds1Current24HrPSASsThreshold"))
)
if mibBuilder.loadTexts:
    ciscoDs1Alarm24HrThreshGroupRev1.setStatus("current")

ciscoDs1CallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 17)
)
ciscoDs1CallGroup.setObjects(
    ("CISCO-DS1-EXT-MIB", "cds1CallTrunkConditionEnable")
)
if mibBuilder.loadTexts:
    ciscoDs1CallGroup.setStatus("current")


# Notification objects

cds1StatThresholdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 1, 4, 0, 1)
)
cds1StatThresholdAlarm.setObjects(
    ("CISCO-DS1-EXT-MIB", "cds1StatisticalAlarmState")
)
if mibBuilder.loadTexts:
    cds1StatThresholdAlarm.setStatus(
        "current"
    )


# Notifications groups

cds1NEOptionalNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 2, 12)
)
cds1NEOptionalNotificationsGroup.setObjects(
    ("CISCO-DS1-EXT-MIB", "cds1StatThresholdAlarm")
)
if mibBuilder.loadTexts:
    cds1NEOptionalNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoDs1MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDs1MIBCompliance.setStatus(
        "deprecated"
    )

ciscoDs1MIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoDs1MIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoDs1MIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoDs1MIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoDs1MIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 229, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoDs1MIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DS1-EXT-MIB",
    **{"PerfCurrent24HourCount": PerfCurrent24HourCount,
       "PerfPrevious24HourCount": PerfPrevious24HourCount,
       "ciscoDs1ExtMIB": ciscoDs1ExtMIB,
       "ciscoDs1MIBObjects": ciscoDs1MIBObjects,
       "cds1Config": cds1Config,
       "cds1ConfigTable": cds1ConfigTable,
       "cds1ConfigEntry": cds1ConfigEntry,
       "cds1LineType": cds1LineType,
       "cds1LoopbackCodeDetection": cds1LoopbackCodeDetection,
       "cds1Repetition": cds1Repetition,
       "cds1RepetitionOwner": cds1RepetitionOwner,
       "cds1RepetitionResult": cds1RepetitionResult,
       "cds1CallConfigTable": cds1CallConfigTable,
       "cds1CallConfigEntry": cds1CallConfigEntry,
       "cds1CallTrunkConditionEnable": cds1CallTrunkConditionEnable,
       "cds1Alarm": cds1Alarm,
       "cds1AlarmThresholdGroupTable": cds1AlarmThresholdGroupTable,
       "cds1AlarmThresholdGroupEntry": cds1AlarmThresholdGroupEntry,
       "cds1AlarmThresholdGroupIndex": cds1AlarmThresholdGroupIndex,
       "cds1Current15MinBESsThreshold": cds1Current15MinBESsThreshold,
       "cds1Current24HrBESsThreshold": cds1Current24HrBESsThreshold,
       "cds1Current15MinCSSsThreshold": cds1Current15MinCSSsThreshold,
       "cds1Current24HrCSSsThreshold": cds1Current24HrCSSsThreshold,
       "cds1Current15MinDMsThreshold": cds1Current15MinDMsThreshold,
       "cds1Current24HrDMsThreshold": cds1Current24HrDMsThreshold,
       "cds1Current15MinESsThreshold": cds1Current15MinESsThreshold,
       "cds1Current24HrESsThreshold": cds1Current24HrESsThreshold,
       "cds1Current15MinLCVsThreshold": cds1Current15MinLCVsThreshold,
       "cds1Current24HrLCVsThreshold": cds1Current24HrLCVsThreshold,
       "cds1Current15MinLESsThreshold": cds1Current15MinLESsThreshold,
       "cds1Current24HrLESsThreshold": cds1Current24HrLESsThreshold,
       "cds1Current15MinLSESsThreshold": cds1Current15MinLSESsThreshold,
       "cds1Current24HrLSESsThreshold": cds1Current24HrLSESsThreshold,
       "cds1Current15MinPCVsThreshold": cds1Current15MinPCVsThreshold,
       "cds1Current24HrPCVsThreshold": cds1Current24HrPCVsThreshold,
       "cds1Current15MinPSASsThreshold": cds1Current15MinPSASsThreshold,
       "cds1Current24HrPSASsThreshold": cds1Current24HrPSASsThreshold,
       "cds1Current15MinSESsThreshold": cds1Current15MinSESsThreshold,
       "cds1Current24HrSESsThreshold": cds1Current24HrSESsThreshold,
       "cds1Current15MinSEFSsThreshold": cds1Current15MinSEFSsThreshold,
       "cds1Current24HrSEFSsThreshold": cds1Current24HrSEFSsThreshold,
       "cds1Current15MinUASsThreshold": cds1Current15MinUASsThreshold,
       "cds1Current24HrUASsThreshold": cds1Current24HrUASsThreshold,
       "cds1AlarmThresholdGroupRowStatus": cds1AlarmThresholdGroupRowStatus,
       "cds1AlarmConfigTable": cds1AlarmConfigTable,
       "cds1AlarmConfigEntry": cds1AlarmConfigEntry,
       "cds1StatisticalAlarmSeverity": cds1StatisticalAlarmSeverity,
       "cds1StatisticalAlarmState": cds1StatisticalAlarmState,
       "cds1AlarmUpCount": cds1AlarmUpCount,
       "cds1AlarmDownCount": cds1AlarmDownCount,
       "cds1AlarmThreshold": cds1AlarmThreshold,
       "cds1AlarmThresholdActiveGroup": cds1AlarmThresholdActiveGroup,
       "cds1Stats": cds1Stats,
       "cds1CurrentTable": cds1CurrentTable,
       "cds1CurrentEntry": cds1CurrentEntry,
       "cds1CurrentLSESs": cds1CurrentLSESs,
       "cds1CurrentPSASs": cds1CurrentPSASs,
       "cds1IntervalTable": cds1IntervalTable,
       "cds1IntervalEntry": cds1IntervalEntry,
       "cds1IntervalLSESs": cds1IntervalLSESs,
       "cds1IntervalPSASs": cds1IntervalPSASs,
       "cds1TotalTable": cds1TotalTable,
       "cds1TotalEntry": cds1TotalEntry,
       "cds1TotalLSESs": cds1TotalLSESs,
       "cds1TotalPSASs": cds1TotalPSASs,
       "cds1FarEndCurrentTable": cds1FarEndCurrentTable,
       "cds1FarEndCurrentEntry": cds1FarEndCurrentEntry,
       "cds1FarEndCurrentLOFCs": cds1FarEndCurrentLOFCs,
       "cds1FarEndIntervalTable": cds1FarEndIntervalTable,
       "cds1FarEndIntervalEntry": cds1FarEndIntervalEntry,
       "cds1FarEndIntervalLOFCs": cds1FarEndIntervalLOFCs,
       "cds1FarEndTotalTable": cds1FarEndTotalTable,
       "cds1FarEndTotalEntry": cds1FarEndTotalEntry,
       "cds1FarEndTotalLOFCs": cds1FarEndTotalLOFCs,
       "cds1Current24HrStatsTable": cds1Current24HrStatsTable,
       "cds1Current24HrStatsEntry": cds1Current24HrStatsEntry,
       "cds1Current24HrESs": cds1Current24HrESs,
       "cds1Current24HrSESs": cds1Current24HrSESs,
       "cds1Current24HrSEFSs": cds1Current24HrSEFSs,
       "cds1Current24HrUASs": cds1Current24HrUASs,
       "cds1Current24HrCSSs": cds1Current24HrCSSs,
       "cds1Current24HrPCVs": cds1Current24HrPCVs,
       "cds1Current24HrLESs": cds1Current24HrLESs,
       "cds1Current24HrBESs": cds1Current24HrBESs,
       "cds1Current24HrDMs": cds1Current24HrDMs,
       "cds1Current24HrLCVs": cds1Current24HrLCVs,
       "cds1Previous24HrStatsTable": cds1Previous24HrStatsTable,
       "cds1Previous24HrStatsEntry": cds1Previous24HrStatsEntry,
       "cds1Previous24HrESs": cds1Previous24HrESs,
       "cds1Previous24HrSESs": cds1Previous24HrSESs,
       "cds1Previous24HrSEFSs": cds1Previous24HrSEFSs,
       "cds1Previous24HrUASs": cds1Previous24HrUASs,
       "cds1Previous24HrCSSs": cds1Previous24HrCSSs,
       "cds1Previous24HrPCVs": cds1Previous24HrPCVs,
       "cds1Previous24HrLESs": cds1Previous24HrLESs,
       "cds1Previous24HrBESs": cds1Previous24HrBESs,
       "cds1Previous24HrDMs": cds1Previous24HrDMs,
       "cds1Previous24HrLCVs": cds1Previous24HrLCVs,
       "cds1Previous24HrLSESs": cds1Previous24HrLSESs,
       "cds1ErrStatsTable": cds1ErrStatsTable,
       "cds1ErrStatsEntry": cds1ErrStatsEntry,
       "cds1LOSCounts": cds1LOSCounts,
       "cds1OOFCounts": cds1OOFCounts,
       "cds1RAICounts": cds1RAICounts,
       "cds1FECounts": cds1FECounts,
       "cds1NotificationPrefix": cds1NotificationPrefix,
       "cds1Notifications": cds1Notifications,
       "cds1StatThresholdAlarm": cds1StatThresholdAlarm,
       "ciscoDs1MIBConformance": ciscoDs1MIBConformance,
       "ciscoDs1MIBCompliances": ciscoDs1MIBCompliances,
       "ciscoDs1MIBCompliance": ciscoDs1MIBCompliance,
       "ciscoDs1MIBComplianceRev1": ciscoDs1MIBComplianceRev1,
       "ciscoDs1MIBComplianceRev2": ciscoDs1MIBComplianceRev2,
       "ciscoDs1MIBComplianceRev3": ciscoDs1MIBComplianceRev3,
       "ciscoDs1MIBGroups": ciscoDs1MIBGroups,
       "ciscoDs1ConfMIBGroup": ciscoDs1ConfMIBGroup,
       "ciscoDs1CurrentMIBGroup": ciscoDs1CurrentMIBGroup,
       "ciscoDs1IntervalMIBGroup": ciscoDs1IntervalMIBGroup,
       "ciscoDs1TotalMIBGroup": ciscoDs1TotalMIBGroup,
       "ciscoDs1FarEndStatsMIBGroup": ciscoDs1FarEndStatsMIBGroup,
       "ciscoDs1AlarmConfigGroup": ciscoDs1AlarmConfigGroup,
       "ciscoDs1Alarm15MinThreshGroup": ciscoDs1Alarm15MinThreshGroup,
       "ciscoDs1Alarm24HrThreshGroup": ciscoDs1Alarm24HrThreshGroup,
       "ciscoDs1Current24HrMIBGroup": ciscoDs1Current24HrMIBGroup,
       "ciscoDs1Previous24HrMIBGroup": ciscoDs1Previous24HrMIBGroup,
       "ciscoDs1StatsMIBGroup": ciscoDs1StatsMIBGroup,
       "cds1NEOptionalNotificationsGroup": cds1NEOptionalNotificationsGroup,
       "ciscoDs1BulkConfGroup": ciscoDs1BulkConfGroup,
       "ciscoDs1AlarmThreshGroup": ciscoDs1AlarmThreshGroup,
       "ciscoDs1Alarm15MinThreshGroupRev1": ciscoDs1Alarm15MinThreshGroupRev1,
       "ciscoDs1Alarm24HrThreshGroupRev1": ciscoDs1Alarm24HrThreshGroupRev1,
       "ciscoDs1CallGroup": ciscoDs1CallGroup}
)
