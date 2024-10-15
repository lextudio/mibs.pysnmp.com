# SNMP MIB module (PW-TDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PW-TDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:24 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(pwIndex,) = mibBuilder.importSymbols(
    "PW-STD-MIB",
    "pwIndex")

(PwCfgIndexOrzero,) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwCfgIndexOrzero")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

pwTDMMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 186)
)
pwTDMMIB.setRevisions(
        ("2009-06-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PwTDMCfgIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_PwTDMNotifications_ObjectIdentity = ObjectIdentity
pwTDMNotifications = _PwTDMNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 186, 0)
)
_PwTDMObjects_ObjectIdentity = ObjectIdentity
pwTDMObjects = _PwTDMObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 186, 1)
)
_PwTDMTable_Object = MibTable
pwTDMTable = _PwTDMTable_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 1)
)
if mibBuilder.loadTexts:
    pwTDMTable.setStatus("current")
_PwTDMEntry_Object = MibTableRow
pwTDMEntry = _PwTDMEntry_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 1, 1)
)
pwTDMEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwTDMEntry.setStatus("current")


class _PwTDMRate_Type(Integer32):
    """Custom type pwTDMRate based on Integer32"""
    defaultValue = 32


_PwTDMRate_Object = MibTableColumn
pwTDMRate = _PwTDMRate_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 1, 1, 1),
    _PwTDMRate_Type()
)
pwTDMRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTDMRate.setStatus("current")
_PwTDMIfIndex_Type = InterfaceIndexOrZero
_PwTDMIfIndex_Object = MibTableColumn
pwTDMIfIndex = _PwTDMIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 1, 1, 2),
    _PwTDMIfIndex_Type()
)
pwTDMIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTDMIfIndex.setStatus("current")
_PwGenTDMCfgIndex_Type = PwCfgIndexOrzero
_PwGenTDMCfgIndex_Object = MibTableColumn
pwGenTDMCfgIndex = _PwGenTDMCfgIndex_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 1, 1, 3),
    _PwGenTDMCfgIndex_Type()
)
pwGenTDMCfgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwGenTDMCfgIndex.setStatus("current")
_PwRelTDMCfgIndex_Type = PwCfgIndexOrzero
_PwRelTDMCfgIndex_Object = MibTableColumn
pwRelTDMCfgIndex = _PwRelTDMCfgIndex_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 1, 1, 4),
    _PwRelTDMCfgIndex_Type()
)
pwRelTDMCfgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwRelTDMCfgIndex.setStatus("current")


class _PwTDMConfigError_Type(Bits):
    """Custom type pwTDMConfigError based on Bits"""
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("peerPayloadSizeIncompatible", 3),
          ("peerRtpIncompatible", 2),
          ("tdmTypeIncompatible", 1))
    )

_PwTDMConfigError_Type.__name__ = "Bits"
_PwTDMConfigError_Object = MibTableColumn
pwTDMConfigError = _PwTDMConfigError_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 1, 1, 5),
    _PwTDMConfigError_Type()
)
pwTDMConfigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMConfigError.setStatus("current")


class _PwTDMTimeElapsed_Type(Integer32):
    """Custom type pwTDMTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_PwTDMTimeElapsed_Type.__name__ = "Integer32"
_PwTDMTimeElapsed_Object = MibTableColumn
pwTDMTimeElapsed = _PwTDMTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 1, 1, 6),
    _PwTDMTimeElapsed_Type()
)
pwTDMTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMTimeElapsed.setStatus("current")


class _PwTDMValidIntervals_Type(Integer32):
    """Custom type pwTDMValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_PwTDMValidIntervals_Type.__name__ = "Integer32"
_PwTDMValidIntervals_Object = MibTableColumn
pwTDMValidIntervals = _PwTDMValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 1, 1, 7),
    _PwTDMValidIntervals_Type()
)
pwTDMValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMValidIntervals.setStatus("current")


class _PwTDMValidDayIntervals_Type(Integer32):
    """Custom type pwTDMValidDayIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_PwTDMValidDayIntervals_Type.__name__ = "Integer32"
_PwTDMValidDayIntervals_Object = MibTableColumn
pwTDMValidDayIntervals = _PwTDMValidDayIntervals_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 1, 1, 8),
    _PwTDMValidDayIntervals_Type()
)
pwTDMValidDayIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMValidDayIntervals.setStatus("current")
_PwTDMLastEsTimeStamp_Type = TimeStamp
_PwTDMLastEsTimeStamp_Object = MibTableColumn
pwTDMLastEsTimeStamp = _PwTDMLastEsTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 1, 1, 11),
    _PwTDMLastEsTimeStamp_Type()
)
pwTDMLastEsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMLastEsTimeStamp.setStatus("current")
_PwTDMCfgIndexNext_Type = Unsigned32
_PwTDMCfgIndexNext_Object = MibScalar
pwTDMCfgIndexNext = _PwTDMCfgIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 2),
    _PwTDMCfgIndexNext_Type()
)
pwTDMCfgIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMCfgIndexNext.setStatus("current")
_PwTDMCfgTable_Object = MibTable
pwTDMCfgTable = _PwTDMCfgTable_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3)
)
if mibBuilder.loadTexts:
    pwTDMCfgTable.setStatus("current")
_PwTDMCfgEntry_Object = MibTableRow
pwTDMCfgEntry = _PwTDMCfgEntry_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1)
)
pwTDMCfgEntry.setIndexNames(
    (0, "PW-TDM-MIB", "pwTDMCfgIndex"),
)
if mibBuilder.loadTexts:
    pwTDMCfgEntry.setStatus("current")
_PwTDMCfgIndex_Type = PwTDMCfgIndex
_PwTDMCfgIndex_Object = MibTableColumn
pwTDMCfgIndex = _PwTDMCfgIndex_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 1),
    _PwTDMCfgIndex_Type()
)
pwTDMCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTDMCfgIndex.setStatus("current")
_PwTDMCfgRowStatus_Type = RowStatus
_PwTDMCfgRowStatus_Object = MibTableColumn
pwTDMCfgRowStatus = _PwTDMCfgRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 2),
    _PwTDMCfgRowStatus_Type()
)
pwTDMCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgRowStatus.setStatus("current")
_PwTDMCfgPayloadSize_Type = Unsigned32
_PwTDMCfgPayloadSize_Object = MibTableColumn
pwTDMCfgPayloadSize = _PwTDMCfgPayloadSize_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 4),
    _PwTDMCfgPayloadSize_Type()
)
pwTDMCfgPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgPayloadSize.setStatus("current")
_PwTDMCfgPktReorder_Type = TruthValue
_PwTDMCfgPktReorder_Object = MibTableColumn
pwTDMCfgPktReorder = _PwTDMCfgPktReorder_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 5),
    _PwTDMCfgPktReorder_Type()
)
pwTDMCfgPktReorder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgPktReorder.setStatus("current")


class _PwTDMCfgRtpHdrUsed_Type(TruthValue):
    """Custom type pwTDMCfgRtpHdrUsed based on TruthValue"""


_PwTDMCfgRtpHdrUsed_Object = MibTableColumn
pwTDMCfgRtpHdrUsed = _PwTDMCfgRtpHdrUsed_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 6),
    _PwTDMCfgRtpHdrUsed_Type()
)
pwTDMCfgRtpHdrUsed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgRtpHdrUsed.setStatus("current")


class _PwTDMCfgJtrBfrDepth_Type(Unsigned32):
    """Custom type pwTDMCfgJtrBfrDepth based on Unsigned32"""
    defaultValue = 3000


_PwTDMCfgJtrBfrDepth_Object = MibTableColumn
pwTDMCfgJtrBfrDepth = _PwTDMCfgJtrBfrDepth_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 7),
    _PwTDMCfgJtrBfrDepth_Type()
)
pwTDMCfgJtrBfrDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgJtrBfrDepth.setStatus("current")
if mibBuilder.loadTexts:
    pwTDMCfgJtrBfrDepth.setUnits("microsecond")


class _PwTDMCfgPayloadSuppression_Type(Integer32):
    """Custom type pwTDMCfgPayloadSuppression based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PwTDMCfgPayloadSuppression_Type.__name__ = "Integer32"
_PwTDMCfgPayloadSuppression_Object = MibTableColumn
pwTDMCfgPayloadSuppression = _PwTDMCfgPayloadSuppression_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 8),
    _PwTDMCfgPayloadSuppression_Type()
)
pwTDMCfgPayloadSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgPayloadSuppression.setStatus("current")


class _PwTDMCfgConsecPktsInSynch_Type(Unsigned32):
    """Custom type pwTDMCfgConsecPktsInSynch based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PwTDMCfgConsecPktsInSynch_Type.__name__ = "Unsigned32"
_PwTDMCfgConsecPktsInSynch_Object = MibTableColumn
pwTDMCfgConsecPktsInSynch = _PwTDMCfgConsecPktsInSynch_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 9),
    _PwTDMCfgConsecPktsInSynch_Type()
)
pwTDMCfgConsecPktsInSynch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgConsecPktsInSynch.setStatus("current")


class _PwTDMCfgConsecMissPktsOutSynch_Type(Unsigned32):
    """Custom type pwTDMCfgConsecMissPktsOutSynch based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_PwTDMCfgConsecMissPktsOutSynch_Type.__name__ = "Unsigned32"
_PwTDMCfgConsecMissPktsOutSynch_Object = MibTableColumn
pwTDMCfgConsecMissPktsOutSynch = _PwTDMCfgConsecMissPktsOutSynch_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 10),
    _PwTDMCfgConsecMissPktsOutSynch_Type()
)
pwTDMCfgConsecMissPktsOutSynch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgConsecMissPktsOutSynch.setStatus("current")


class _PwTDMCfgSetUp2SynchTimeOut_Type(Unsigned32):
    """Custom type pwTDMCfgSetUp2SynchTimeOut based on Unsigned32"""
    defaultValue = 5000


_PwTDMCfgSetUp2SynchTimeOut_Object = MibTableColumn
pwTDMCfgSetUp2SynchTimeOut = _PwTDMCfgSetUp2SynchTimeOut_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 11),
    _PwTDMCfgSetUp2SynchTimeOut_Type()
)
pwTDMCfgSetUp2SynchTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgSetUp2SynchTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    pwTDMCfgSetUp2SynchTimeOut.setUnits("millisecond")


class _PwTDMCfgPktReplacePolicy_Type(Integer32):
    """Custom type pwTDMCfgPktReplacePolicy based on Integer32"""
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
        *(("allOnes", 1),
          ("filler", 3),
          ("implementationSpecific", 2))
    )


_PwTDMCfgPktReplacePolicy_Type.__name__ = "Integer32"
_PwTDMCfgPktReplacePolicy_Object = MibTableColumn
pwTDMCfgPktReplacePolicy = _PwTDMCfgPktReplacePolicy_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 12),
    _PwTDMCfgPktReplacePolicy_Type()
)
pwTDMCfgPktReplacePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgPktReplacePolicy.setStatus("current")
_PwTDMCfgAvePktLossTimeWindow_Type = Integer32
_PwTDMCfgAvePktLossTimeWindow_Object = MibTableColumn
pwTDMCfgAvePktLossTimeWindow = _PwTDMCfgAvePktLossTimeWindow_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 13),
    _PwTDMCfgAvePktLossTimeWindow_Type()
)
pwTDMCfgAvePktLossTimeWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgAvePktLossTimeWindow.setStatus("current")
if mibBuilder.loadTexts:
    pwTDMCfgAvePktLossTimeWindow.setUnits("millisecond")
_PwTDMCfgExcessivePktLossThreshold_Type = Unsigned32
_PwTDMCfgExcessivePktLossThreshold_Object = MibTableColumn
pwTDMCfgExcessivePktLossThreshold = _PwTDMCfgExcessivePktLossThreshold_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 14),
    _PwTDMCfgExcessivePktLossThreshold_Type()
)
pwTDMCfgExcessivePktLossThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgExcessivePktLossThreshold.setStatus("current")
if mibBuilder.loadTexts:
    pwTDMCfgExcessivePktLossThreshold.setUnits("Percent")


class _PwTDMCfgAlarmThreshold_Type(Unsigned32):
    """Custom type pwTDMCfgAlarmThreshold based on Unsigned32"""
    defaultValue = 2500


_PwTDMCfgAlarmThreshold_Object = MibTableColumn
pwTDMCfgAlarmThreshold = _PwTDMCfgAlarmThreshold_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 15),
    _PwTDMCfgAlarmThreshold_Type()
)
pwTDMCfgAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    pwTDMCfgAlarmThreshold.setUnits("milisec")


class _PwTDMCfgClearAlarmThreshold_Type(Unsigned32):
    """Custom type pwTDMCfgClearAlarmThreshold based on Unsigned32"""
    defaultValue = 10000


_PwTDMCfgClearAlarmThreshold_Object = MibTableColumn
pwTDMCfgClearAlarmThreshold = _PwTDMCfgClearAlarmThreshold_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 16),
    _PwTDMCfgClearAlarmThreshold_Type()
)
pwTDMCfgClearAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgClearAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    pwTDMCfgClearAlarmThreshold.setUnits("milisec")


class _PwTDMCfgMissingPktsToSes_Type(Unsigned32):
    """Custom type pwTDMCfgMissingPktsToSes based on Unsigned32"""
    defaultValue = 30


_PwTDMCfgMissingPktsToSes_Object = MibTableColumn
pwTDMCfgMissingPktsToSes = _PwTDMCfgMissingPktsToSes_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 17),
    _PwTDMCfgMissingPktsToSes_Type()
)
pwTDMCfgMissingPktsToSes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgMissingPktsToSes.setStatus("current")
if mibBuilder.loadTexts:
    pwTDMCfgMissingPktsToSes.setUnits("Percent")


class _PwTDMCfgTimestampMode_Type(Integer32):
    """Custom type pwTDMCfgTimestampMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 2),
          ("differential", 3),
          ("notApplicable", 1))
    )


_PwTDMCfgTimestampMode_Type.__name__ = "Integer32"
_PwTDMCfgTimestampMode_Object = MibTableColumn
pwTDMCfgTimestampMode = _PwTDMCfgTimestampMode_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 18),
    _PwTDMCfgTimestampMode_Type()
)
pwTDMCfgTimestampMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgTimestampMode.setStatus("current")
_PwTDMCfgStorageType_Type = StorageType
_PwTDMCfgStorageType_Object = MibTableColumn
pwTDMCfgStorageType = _PwTDMCfgStorageType_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 19),
    _PwTDMCfgStorageType_Type()
)
pwTDMCfgStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgStorageType.setStatus("current")


class _PwTDMCfgPktFiller_Type(Unsigned32):
    """Custom type pwTDMCfgPktFiller based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PwTDMCfgPktFiller_Type.__name__ = "Unsigned32"
_PwTDMCfgPktFiller_Object = MibTableColumn
pwTDMCfgPktFiller = _PwTDMCfgPktFiller_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 20),
    _PwTDMCfgPktFiller_Type()
)
pwTDMCfgPktFiller.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgPktFiller.setStatus("current")
_PwTDMCfgName_Type = SnmpAdminString
_PwTDMCfgName_Object = MibTableColumn
pwTDMCfgName = _PwTDMCfgName_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 3, 1, 21),
    _PwTDMCfgName_Type()
)
pwTDMCfgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTDMCfgName.setStatus("current")
_PwTDMPerfCurrentTable_Object = MibTable
pwTDMPerfCurrentTable = _PwTDMPerfCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 5)
)
if mibBuilder.loadTexts:
    pwTDMPerfCurrentTable.setStatus("current")
_PwTDMPerfCurrentEntry_Object = MibTableRow
pwTDMPerfCurrentEntry = _PwTDMPerfCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 5, 1)
)
pwTDMPerfCurrentEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwTDMPerfCurrentEntry.setStatus("current")
_PwTDMPerfCurrentMissingPkts_Type = PerfCurrentCount
_PwTDMPerfCurrentMissingPkts_Object = MibTableColumn
pwTDMPerfCurrentMissingPkts = _PwTDMPerfCurrentMissingPkts_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 5, 1, 1),
    _PwTDMPerfCurrentMissingPkts_Type()
)
pwTDMPerfCurrentMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfCurrentMissingPkts.setStatus("current")
_PwTDMPerfCurrentPktsReOrder_Type = PerfCurrentCount
_PwTDMPerfCurrentPktsReOrder_Object = MibTableColumn
pwTDMPerfCurrentPktsReOrder = _PwTDMPerfCurrentPktsReOrder_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 5, 1, 2),
    _PwTDMPerfCurrentPktsReOrder_Type()
)
pwTDMPerfCurrentPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfCurrentPktsReOrder.setStatus("current")
_PwTDMPerfCurrentJtrBfrUnderruns_Type = PerfCurrentCount
_PwTDMPerfCurrentJtrBfrUnderruns_Object = MibTableColumn
pwTDMPerfCurrentJtrBfrUnderruns = _PwTDMPerfCurrentJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 5, 1, 3),
    _PwTDMPerfCurrentJtrBfrUnderruns_Type()
)
pwTDMPerfCurrentJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfCurrentJtrBfrUnderruns.setStatus("current")
_PwTDMPerfCurrentMisOrderDropped_Type = PerfCurrentCount
_PwTDMPerfCurrentMisOrderDropped_Object = MibTableColumn
pwTDMPerfCurrentMisOrderDropped = _PwTDMPerfCurrentMisOrderDropped_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 5, 1, 4),
    _PwTDMPerfCurrentMisOrderDropped_Type()
)
pwTDMPerfCurrentMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfCurrentMisOrderDropped.setStatus("current")
_PwTDMPerfCurrentMalformedPkt_Type = PerfCurrentCount
_PwTDMPerfCurrentMalformedPkt_Object = MibTableColumn
pwTDMPerfCurrentMalformedPkt = _PwTDMPerfCurrentMalformedPkt_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 5, 1, 5),
    _PwTDMPerfCurrentMalformedPkt_Type()
)
pwTDMPerfCurrentMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfCurrentMalformedPkt.setStatus("current")
_PwTDMPerfCurrentESs_Type = PerfCurrentCount
_PwTDMPerfCurrentESs_Object = MibTableColumn
pwTDMPerfCurrentESs = _PwTDMPerfCurrentESs_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 5, 1, 6),
    _PwTDMPerfCurrentESs_Type()
)
pwTDMPerfCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfCurrentESs.setStatus("current")
_PwTDMPerfCurrentSESs_Type = PerfCurrentCount
_PwTDMPerfCurrentSESs_Object = MibTableColumn
pwTDMPerfCurrentSESs = _PwTDMPerfCurrentSESs_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 5, 1, 7),
    _PwTDMPerfCurrentSESs_Type()
)
pwTDMPerfCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfCurrentSESs.setStatus("current")
_PwTDMPerfCurrentUASs_Type = PerfCurrentCount
_PwTDMPerfCurrentUASs_Object = MibTableColumn
pwTDMPerfCurrentUASs = _PwTDMPerfCurrentUASs_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 5, 1, 8),
    _PwTDMPerfCurrentUASs_Type()
)
pwTDMPerfCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfCurrentUASs.setStatus("current")
_PwTDMPerfCurrentFC_Type = PerfCurrentCount
_PwTDMPerfCurrentFC_Object = MibTableColumn
pwTDMPerfCurrentFC = _PwTDMPerfCurrentFC_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 5, 1, 9),
    _PwTDMPerfCurrentFC_Type()
)
pwTDMPerfCurrentFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfCurrentFC.setStatus("current")
_PwTDMPerfIntervalTable_Object = MibTable
pwTDMPerfIntervalTable = _PwTDMPerfIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 6)
)
if mibBuilder.loadTexts:
    pwTDMPerfIntervalTable.setStatus("current")
_PwTDMPerfIntervalEntry_Object = MibTableRow
pwTDMPerfIntervalEntry = _PwTDMPerfIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 6, 1)
)
pwTDMPerfIntervalEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
    (0, "PW-TDM-MIB", "pwTDMPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    pwTDMPerfIntervalEntry.setStatus("current")


class _PwTDMPerfIntervalNumber_Type(Unsigned32):
    """Custom type pwTDMPerfIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PwTDMPerfIntervalNumber_Type.__name__ = "Unsigned32"
_PwTDMPerfIntervalNumber_Object = MibTableColumn
pwTDMPerfIntervalNumber = _PwTDMPerfIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 6, 1, 1),
    _PwTDMPerfIntervalNumber_Type()
)
pwTDMPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTDMPerfIntervalNumber.setStatus("current")
_PwTDMPerfIntervalValidData_Type = TruthValue
_PwTDMPerfIntervalValidData_Object = MibTableColumn
pwTDMPerfIntervalValidData = _PwTDMPerfIntervalValidData_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 6, 1, 2),
    _PwTDMPerfIntervalValidData_Type()
)
pwTDMPerfIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfIntervalValidData.setStatus("current")
_PwTDMPerfIntervalDuration_Type = Unsigned32
_PwTDMPerfIntervalDuration_Object = MibTableColumn
pwTDMPerfIntervalDuration = _PwTDMPerfIntervalDuration_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 6, 1, 3),
    _PwTDMPerfIntervalDuration_Type()
)
pwTDMPerfIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfIntervalDuration.setStatus("current")
if mibBuilder.loadTexts:
    pwTDMPerfIntervalDuration.setUnits("seconds")
_PwTDMPerfIntervalMissingPkts_Type = PerfIntervalCount
_PwTDMPerfIntervalMissingPkts_Object = MibTableColumn
pwTDMPerfIntervalMissingPkts = _PwTDMPerfIntervalMissingPkts_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 6, 1, 4),
    _PwTDMPerfIntervalMissingPkts_Type()
)
pwTDMPerfIntervalMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfIntervalMissingPkts.setStatus("current")
_PwTDMPerfIntervalPktsReOrder_Type = PerfIntervalCount
_PwTDMPerfIntervalPktsReOrder_Object = MibTableColumn
pwTDMPerfIntervalPktsReOrder = _PwTDMPerfIntervalPktsReOrder_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 6, 1, 5),
    _PwTDMPerfIntervalPktsReOrder_Type()
)
pwTDMPerfIntervalPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfIntervalPktsReOrder.setStatus("current")
_PwTDMPerfIntervalJtrBfrUnderruns_Type = PerfIntervalCount
_PwTDMPerfIntervalJtrBfrUnderruns_Object = MibTableColumn
pwTDMPerfIntervalJtrBfrUnderruns = _PwTDMPerfIntervalJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 6, 1, 6),
    _PwTDMPerfIntervalJtrBfrUnderruns_Type()
)
pwTDMPerfIntervalJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfIntervalJtrBfrUnderruns.setStatus("current")
_PwTDMPerfIntervalMisOrderDropped_Type = PerfIntervalCount
_PwTDMPerfIntervalMisOrderDropped_Object = MibTableColumn
pwTDMPerfIntervalMisOrderDropped = _PwTDMPerfIntervalMisOrderDropped_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 6, 1, 7),
    _PwTDMPerfIntervalMisOrderDropped_Type()
)
pwTDMPerfIntervalMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfIntervalMisOrderDropped.setStatus("current")
_PwTDMPerfIntervalMalformedPkt_Type = PerfIntervalCount
_PwTDMPerfIntervalMalformedPkt_Object = MibTableColumn
pwTDMPerfIntervalMalformedPkt = _PwTDMPerfIntervalMalformedPkt_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 6, 1, 8),
    _PwTDMPerfIntervalMalformedPkt_Type()
)
pwTDMPerfIntervalMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfIntervalMalformedPkt.setStatus("current")
_PwTDMPerfIntervalESs_Type = PerfIntervalCount
_PwTDMPerfIntervalESs_Object = MibTableColumn
pwTDMPerfIntervalESs = _PwTDMPerfIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 6, 1, 9),
    _PwTDMPerfIntervalESs_Type()
)
pwTDMPerfIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfIntervalESs.setStatus("current")
_PwTDMPerfIntervalSESs_Type = PerfIntervalCount
_PwTDMPerfIntervalSESs_Object = MibTableColumn
pwTDMPerfIntervalSESs = _PwTDMPerfIntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 6, 1, 10),
    _PwTDMPerfIntervalSESs_Type()
)
pwTDMPerfIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfIntervalSESs.setStatus("current")
_PwTDMPerfIntervalUASs_Type = PerfIntervalCount
_PwTDMPerfIntervalUASs_Object = MibTableColumn
pwTDMPerfIntervalUASs = _PwTDMPerfIntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 6, 1, 11),
    _PwTDMPerfIntervalUASs_Type()
)
pwTDMPerfIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfIntervalUASs.setStatus("current")
_PwTDMPerfIntervalFC_Type = PerfIntervalCount
_PwTDMPerfIntervalFC_Object = MibTableColumn
pwTDMPerfIntervalFC = _PwTDMPerfIntervalFC_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 6, 1, 12),
    _PwTDMPerfIntervalFC_Type()
)
pwTDMPerfIntervalFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerfIntervalFC.setStatus("current")
_PwTDMPerf1DayIntervalTable_Object = MibTable
pwTDMPerf1DayIntervalTable = _PwTDMPerf1DayIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 7)
)
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalTable.setStatus("current")
_PwTDMPerf1DayIntervalEntry_Object = MibTableRow
pwTDMPerf1DayIntervalEntry = _PwTDMPerf1DayIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 7, 1)
)
pwTDMPerf1DayIntervalEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
    (0, "PW-TDM-MIB", "pwTDMPerf1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalEntry.setStatus("current")


class _PwTDMPerf1DayIntervalNumber_Type(Unsigned32):
    """Custom type pwTDMPerf1DayIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_PwTDMPerf1DayIntervalNumber_Type.__name__ = "Unsigned32"
_PwTDMPerf1DayIntervalNumber_Object = MibTableColumn
pwTDMPerf1DayIntervalNumber = _PwTDMPerf1DayIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 7, 1, 1),
    _PwTDMPerf1DayIntervalNumber_Type()
)
pwTDMPerf1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalNumber.setStatus("current")
_PwTDMPerf1DayIntervalValidData_Type = TruthValue
_PwTDMPerf1DayIntervalValidData_Object = MibTableColumn
pwTDMPerf1DayIntervalValidData = _PwTDMPerf1DayIntervalValidData_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 7, 1, 2),
    _PwTDMPerf1DayIntervalValidData_Type()
)
pwTDMPerf1DayIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalValidData.setStatus("current")
_PwTDMPerf1DayIntervalDuration_Type = Unsigned32
_PwTDMPerf1DayIntervalDuration_Object = MibTableColumn
pwTDMPerf1DayIntervalDuration = _PwTDMPerf1DayIntervalDuration_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 7, 1, 3),
    _PwTDMPerf1DayIntervalDuration_Type()
)
pwTDMPerf1DayIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalDuration.setStatus("current")
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalDuration.setUnits("seconds")
_PwTDMPerf1DayIntervalMissingPkts_Type = Counter32
_PwTDMPerf1DayIntervalMissingPkts_Object = MibTableColumn
pwTDMPerf1DayIntervalMissingPkts = _PwTDMPerf1DayIntervalMissingPkts_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 7, 1, 4),
    _PwTDMPerf1DayIntervalMissingPkts_Type()
)
pwTDMPerf1DayIntervalMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalMissingPkts.setStatus("current")
_PwTDMPerf1DayIntervalPktsReOrder_Type = Counter32
_PwTDMPerf1DayIntervalPktsReOrder_Object = MibTableColumn
pwTDMPerf1DayIntervalPktsReOrder = _PwTDMPerf1DayIntervalPktsReOrder_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 7, 1, 5),
    _PwTDMPerf1DayIntervalPktsReOrder_Type()
)
pwTDMPerf1DayIntervalPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalPktsReOrder.setStatus("current")
_PwTDMPerf1DayIntervalJtrBfrUnderruns_Type = Counter32
_PwTDMPerf1DayIntervalJtrBfrUnderruns_Object = MibTableColumn
pwTDMPerf1DayIntervalJtrBfrUnderruns = _PwTDMPerf1DayIntervalJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 7, 1, 6),
    _PwTDMPerf1DayIntervalJtrBfrUnderruns_Type()
)
pwTDMPerf1DayIntervalJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalJtrBfrUnderruns.setStatus("current")
_PwTDMPerf1DayIntervalMisOrderDropped_Type = Counter32
_PwTDMPerf1DayIntervalMisOrderDropped_Object = MibTableColumn
pwTDMPerf1DayIntervalMisOrderDropped = _PwTDMPerf1DayIntervalMisOrderDropped_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 7, 1, 7),
    _PwTDMPerf1DayIntervalMisOrderDropped_Type()
)
pwTDMPerf1DayIntervalMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalMisOrderDropped.setStatus("current")
_PwTDMPerf1DayIntervalMalformedPkt_Type = Counter32
_PwTDMPerf1DayIntervalMalformedPkt_Object = MibTableColumn
pwTDMPerf1DayIntervalMalformedPkt = _PwTDMPerf1DayIntervalMalformedPkt_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 7, 1, 8),
    _PwTDMPerf1DayIntervalMalformedPkt_Type()
)
pwTDMPerf1DayIntervalMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalMalformedPkt.setStatus("current")
_PwTDMPerf1DayIntervalESs_Type = Counter32
_PwTDMPerf1DayIntervalESs_Object = MibTableColumn
pwTDMPerf1DayIntervalESs = _PwTDMPerf1DayIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 7, 1, 9),
    _PwTDMPerf1DayIntervalESs_Type()
)
pwTDMPerf1DayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalESs.setStatus("current")
_PwTDMPerf1DayIntervalSESs_Type = Counter32
_PwTDMPerf1DayIntervalSESs_Object = MibTableColumn
pwTDMPerf1DayIntervalSESs = _PwTDMPerf1DayIntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 7, 1, 10),
    _PwTDMPerf1DayIntervalSESs_Type()
)
pwTDMPerf1DayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalSESs.setStatus("current")
_PwTDMPerf1DayIntervalUASs_Type = Counter32
_PwTDMPerf1DayIntervalUASs_Object = MibTableColumn
pwTDMPerf1DayIntervalUASs = _PwTDMPerf1DayIntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 7, 1, 11),
    _PwTDMPerf1DayIntervalUASs_Type()
)
pwTDMPerf1DayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalUASs.setStatus("current")
_PwTDMPerf1DayIntervalFC_Type = Counter32
_PwTDMPerf1DayIntervalFC_Object = MibTableColumn
pwTDMPerf1DayIntervalFC = _PwTDMPerf1DayIntervalFC_Object(
    (1, 3, 6, 1, 2, 1, 186, 1, 7, 1, 12),
    _PwTDMPerf1DayIntervalFC_Type()
)
pwTDMPerf1DayIntervalFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalFC.setStatus("current")
_PwTDMConformance_ObjectIdentity = ObjectIdentity
pwTDMConformance = _PwTDMConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 186, 2)
)
_PwTDMCompliances_ObjectIdentity = ObjectIdentity
pwTDMCompliances = _PwTDMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 186, 2, 1)
)
_PwTDMGroups_ObjectIdentity = ObjectIdentity
pwTDMGroups = _PwTDMGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 186, 2, 2)
)

# Managed Objects groups

pwTDMGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 186, 2, 2, 1)
)
pwTDMGroup.setObjects(
      *(("PW-TDM-MIB", "pwTDMRate"),
        ("PW-TDM-MIB", "pwTDMIfIndex"),
        ("PW-TDM-MIB", "pwGenTDMCfgIndex"),
        ("PW-TDM-MIB", "pwRelTDMCfgIndex"),
        ("PW-TDM-MIB", "pwTDMConfigError"),
        ("PW-TDM-MIB", "pwTDMTimeElapsed"),
        ("PW-TDM-MIB", "pwTDMValidIntervals"),
        ("PW-TDM-MIB", "pwTDMValidDayIntervals"),
        ("PW-TDM-MIB", "pwTDMLastEsTimeStamp"),
        ("PW-TDM-MIB", "pwTDMCfgIndexNext"),
        ("PW-TDM-MIB", "pwTDMCfgRowStatus"),
        ("PW-TDM-MIB", "pwTDMCfgPayloadSize"),
        ("PW-TDM-MIB", "pwTDMCfgPktReorder"),
        ("PW-TDM-MIB", "pwTDMCfgRtpHdrUsed"),
        ("PW-TDM-MIB", "pwTDMCfgJtrBfrDepth"),
        ("PW-TDM-MIB", "pwTDMCfgPayloadSuppression"),
        ("PW-TDM-MIB", "pwTDMCfgConsecPktsInSynch"),
        ("PW-TDM-MIB", "pwTDMCfgConsecMissPktsOutSynch"),
        ("PW-TDM-MIB", "pwTDMCfgSetUp2SynchTimeOut"),
        ("PW-TDM-MIB", "pwTDMCfgPktReplacePolicy"),
        ("PW-TDM-MIB", "pwTDMCfgAvePktLossTimeWindow"),
        ("PW-TDM-MIB", "pwTDMCfgExcessivePktLossThreshold"),
        ("PW-TDM-MIB", "pwTDMCfgAlarmThreshold"),
        ("PW-TDM-MIB", "pwTDMCfgClearAlarmThreshold"),
        ("PW-TDM-MIB", "pwTDMCfgMissingPktsToSes"),
        ("PW-TDM-MIB", "pwTDMCfgTimestampMode"),
        ("PW-TDM-MIB", "pwTDMCfgStorageType"),
        ("PW-TDM-MIB", "pwTDMCfgPktFiller"),
        ("PW-TDM-MIB", "pwTDMCfgName"))
)
if mibBuilder.loadTexts:
    pwTDMGroup.setStatus("current")

pwTDMPerfCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 186, 2, 2, 2)
)
pwTDMPerfCurrentGroup.setObjects(
      *(("PW-TDM-MIB", "pwTDMPerfCurrentMissingPkts"),
        ("PW-TDM-MIB", "pwTDMPerfCurrentPktsReOrder"),
        ("PW-TDM-MIB", "pwTDMPerfCurrentJtrBfrUnderruns"),
        ("PW-TDM-MIB", "pwTDMPerfCurrentMisOrderDropped"),
        ("PW-TDM-MIB", "pwTDMPerfCurrentMalformedPkt"),
        ("PW-TDM-MIB", "pwTDMPerfCurrentESs"),
        ("PW-TDM-MIB", "pwTDMPerfCurrentSESs"),
        ("PW-TDM-MIB", "pwTDMPerfCurrentUASs"),
        ("PW-TDM-MIB", "pwTDMPerfCurrentFC"))
)
if mibBuilder.loadTexts:
    pwTDMPerfCurrentGroup.setStatus("current")

pwTDMPerfIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 186, 2, 2, 3)
)
pwTDMPerfIntervalGroup.setObjects(
      *(("PW-TDM-MIB", "pwTDMPerfIntervalValidData"),
        ("PW-TDM-MIB", "pwTDMPerfIntervalDuration"),
        ("PW-TDM-MIB", "pwTDMPerfIntervalMissingPkts"),
        ("PW-TDM-MIB", "pwTDMPerfIntervalPktsReOrder"),
        ("PW-TDM-MIB", "pwTDMPerfIntervalJtrBfrUnderruns"),
        ("PW-TDM-MIB", "pwTDMPerfIntervalMisOrderDropped"),
        ("PW-TDM-MIB", "pwTDMPerfIntervalMalformedPkt"),
        ("PW-TDM-MIB", "pwTDMPerfIntervalESs"),
        ("PW-TDM-MIB", "pwTDMPerfIntervalSESs"),
        ("PW-TDM-MIB", "pwTDMPerfIntervalUASs"),
        ("PW-TDM-MIB", "pwTDMPerfIntervalFC"))
)
if mibBuilder.loadTexts:
    pwTDMPerfIntervalGroup.setStatus("current")

pwTDMPerf1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 186, 2, 2, 4)
)
pwTDMPerf1DayIntervalGroup.setObjects(
      *(("PW-TDM-MIB", "pwTDMPerf1DayIntervalValidData"),
        ("PW-TDM-MIB", "pwTDMPerf1DayIntervalDuration"),
        ("PW-TDM-MIB", "pwTDMPerf1DayIntervalMissingPkts"),
        ("PW-TDM-MIB", "pwTDMPerf1DayIntervalPktsReOrder"),
        ("PW-TDM-MIB", "pwTDMPerf1DayIntervalJtrBfrUnderruns"),
        ("PW-TDM-MIB", "pwTDMPerf1DayIntervalMisOrderDropped"),
        ("PW-TDM-MIB", "pwTDMPerf1DayIntervalMalformedPkt"),
        ("PW-TDM-MIB", "pwTDMPerf1DayIntervalESs"),
        ("PW-TDM-MIB", "pwTDMPerf1DayIntervalSESs"),
        ("PW-TDM-MIB", "pwTDMPerf1DayIntervalUASs"),
        ("PW-TDM-MIB", "pwTDMPerf1DayIntervalFC"))
)
if mibBuilder.loadTexts:
    pwTDMPerf1DayIntervalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pwTDMModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 186, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pwTDMModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PW-TDM-MIB",
    **{"PwTDMCfgIndex": PwTDMCfgIndex,
       "pwTDMMIB": pwTDMMIB,
       "pwTDMNotifications": pwTDMNotifications,
       "pwTDMObjects": pwTDMObjects,
       "pwTDMTable": pwTDMTable,
       "pwTDMEntry": pwTDMEntry,
       "pwTDMRate": pwTDMRate,
       "pwTDMIfIndex": pwTDMIfIndex,
       "pwGenTDMCfgIndex": pwGenTDMCfgIndex,
       "pwRelTDMCfgIndex": pwRelTDMCfgIndex,
       "pwTDMConfigError": pwTDMConfigError,
       "pwTDMTimeElapsed": pwTDMTimeElapsed,
       "pwTDMValidIntervals": pwTDMValidIntervals,
       "pwTDMValidDayIntervals": pwTDMValidDayIntervals,
       "pwTDMLastEsTimeStamp": pwTDMLastEsTimeStamp,
       "pwTDMCfgIndexNext": pwTDMCfgIndexNext,
       "pwTDMCfgTable": pwTDMCfgTable,
       "pwTDMCfgEntry": pwTDMCfgEntry,
       "pwTDMCfgIndex": pwTDMCfgIndex,
       "pwTDMCfgRowStatus": pwTDMCfgRowStatus,
       "pwTDMCfgPayloadSize": pwTDMCfgPayloadSize,
       "pwTDMCfgPktReorder": pwTDMCfgPktReorder,
       "pwTDMCfgRtpHdrUsed": pwTDMCfgRtpHdrUsed,
       "pwTDMCfgJtrBfrDepth": pwTDMCfgJtrBfrDepth,
       "pwTDMCfgPayloadSuppression": pwTDMCfgPayloadSuppression,
       "pwTDMCfgConsecPktsInSynch": pwTDMCfgConsecPktsInSynch,
       "pwTDMCfgConsecMissPktsOutSynch": pwTDMCfgConsecMissPktsOutSynch,
       "pwTDMCfgSetUp2SynchTimeOut": pwTDMCfgSetUp2SynchTimeOut,
       "pwTDMCfgPktReplacePolicy": pwTDMCfgPktReplacePolicy,
       "pwTDMCfgAvePktLossTimeWindow": pwTDMCfgAvePktLossTimeWindow,
       "pwTDMCfgExcessivePktLossThreshold": pwTDMCfgExcessivePktLossThreshold,
       "pwTDMCfgAlarmThreshold": pwTDMCfgAlarmThreshold,
       "pwTDMCfgClearAlarmThreshold": pwTDMCfgClearAlarmThreshold,
       "pwTDMCfgMissingPktsToSes": pwTDMCfgMissingPktsToSes,
       "pwTDMCfgTimestampMode": pwTDMCfgTimestampMode,
       "pwTDMCfgStorageType": pwTDMCfgStorageType,
       "pwTDMCfgPktFiller": pwTDMCfgPktFiller,
       "pwTDMCfgName": pwTDMCfgName,
       "pwTDMPerfCurrentTable": pwTDMPerfCurrentTable,
       "pwTDMPerfCurrentEntry": pwTDMPerfCurrentEntry,
       "pwTDMPerfCurrentMissingPkts": pwTDMPerfCurrentMissingPkts,
       "pwTDMPerfCurrentPktsReOrder": pwTDMPerfCurrentPktsReOrder,
       "pwTDMPerfCurrentJtrBfrUnderruns": pwTDMPerfCurrentJtrBfrUnderruns,
       "pwTDMPerfCurrentMisOrderDropped": pwTDMPerfCurrentMisOrderDropped,
       "pwTDMPerfCurrentMalformedPkt": pwTDMPerfCurrentMalformedPkt,
       "pwTDMPerfCurrentESs": pwTDMPerfCurrentESs,
       "pwTDMPerfCurrentSESs": pwTDMPerfCurrentSESs,
       "pwTDMPerfCurrentUASs": pwTDMPerfCurrentUASs,
       "pwTDMPerfCurrentFC": pwTDMPerfCurrentFC,
       "pwTDMPerfIntervalTable": pwTDMPerfIntervalTable,
       "pwTDMPerfIntervalEntry": pwTDMPerfIntervalEntry,
       "pwTDMPerfIntervalNumber": pwTDMPerfIntervalNumber,
       "pwTDMPerfIntervalValidData": pwTDMPerfIntervalValidData,
       "pwTDMPerfIntervalDuration": pwTDMPerfIntervalDuration,
       "pwTDMPerfIntervalMissingPkts": pwTDMPerfIntervalMissingPkts,
       "pwTDMPerfIntervalPktsReOrder": pwTDMPerfIntervalPktsReOrder,
       "pwTDMPerfIntervalJtrBfrUnderruns": pwTDMPerfIntervalJtrBfrUnderruns,
       "pwTDMPerfIntervalMisOrderDropped": pwTDMPerfIntervalMisOrderDropped,
       "pwTDMPerfIntervalMalformedPkt": pwTDMPerfIntervalMalformedPkt,
       "pwTDMPerfIntervalESs": pwTDMPerfIntervalESs,
       "pwTDMPerfIntervalSESs": pwTDMPerfIntervalSESs,
       "pwTDMPerfIntervalUASs": pwTDMPerfIntervalUASs,
       "pwTDMPerfIntervalFC": pwTDMPerfIntervalFC,
       "pwTDMPerf1DayIntervalTable": pwTDMPerf1DayIntervalTable,
       "pwTDMPerf1DayIntervalEntry": pwTDMPerf1DayIntervalEntry,
       "pwTDMPerf1DayIntervalNumber": pwTDMPerf1DayIntervalNumber,
       "pwTDMPerf1DayIntervalValidData": pwTDMPerf1DayIntervalValidData,
       "pwTDMPerf1DayIntervalDuration": pwTDMPerf1DayIntervalDuration,
       "pwTDMPerf1DayIntervalMissingPkts": pwTDMPerf1DayIntervalMissingPkts,
       "pwTDMPerf1DayIntervalPktsReOrder": pwTDMPerf1DayIntervalPktsReOrder,
       "pwTDMPerf1DayIntervalJtrBfrUnderruns": pwTDMPerf1DayIntervalJtrBfrUnderruns,
       "pwTDMPerf1DayIntervalMisOrderDropped": pwTDMPerf1DayIntervalMisOrderDropped,
       "pwTDMPerf1DayIntervalMalformedPkt": pwTDMPerf1DayIntervalMalformedPkt,
       "pwTDMPerf1DayIntervalESs": pwTDMPerf1DayIntervalESs,
       "pwTDMPerf1DayIntervalSESs": pwTDMPerf1DayIntervalSESs,
       "pwTDMPerf1DayIntervalUASs": pwTDMPerf1DayIntervalUASs,
       "pwTDMPerf1DayIntervalFC": pwTDMPerf1DayIntervalFC,
       "pwTDMConformance": pwTDMConformance,
       "pwTDMCompliances": pwTDMCompliances,
       "pwTDMModuleCompliance": pwTDMModuleCompliance,
       "pwTDMGroups": pwTDMGroups,
       "pwTDMGroup": pwTDMGroup,
       "pwTDMPerfCurrentGroup": pwTDMPerfCurrentGroup,
       "pwTDMPerfIntervalGroup": pwTDMPerfIntervalGroup,
       "pwTDMPerf1DayIntervalGroup": pwTDMPerf1DayIntervalGroup}
)
