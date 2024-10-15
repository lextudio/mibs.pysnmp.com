# SNMP MIB module (CISCO-IETF-PW-TDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-PW-TDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:00 2024
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

(cpwVcIndex,) = mibBuilder.importSymbols(
    "CISCO-IETF-PW-MIB",
    "cpwVcIndex")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

cpwCTDMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 131)
)
cpwCTDMMIB.setRevisions(
        ("2006-07-21 00:00",
         "2006-03-01 00:00",
         "2005-10-23 00:00",
         "2005-07-12 00:00",
         "2004-04-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CpwTDMCfgIndex(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CpwCTDMNotifications_ObjectIdentity = ObjectIdentity
cpwCTDMNotifications = _CpwCTDMNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 0)
)
_CpwCTDMObjects_ObjectIdentity = ObjectIdentity
cpwCTDMObjects = _CpwCTDMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1)
)
_CpwCTDMTable_Object = MibTable
cpwCTDMTable = _CpwCTDMTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 1)
)
if mibBuilder.loadTexts:
    cpwCTDMTable.setStatus("current")
_CpwCTDMEntry_Object = MibTableRow
cpwCTDMEntry = _CpwCTDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 1, 1)
)
cpwCTDMEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
)
if mibBuilder.loadTexts:
    cpwCTDMEntry.setStatus("current")


class _CpwCTDMRate_Type(Integer32):
    """Custom type cpwCTDMRate based on Integer32"""
    defaultValue = 32


_CpwCTDMRate_Object = MibTableColumn
cpwCTDMRate = _CpwCTDMRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 1, 1, 1),
    _CpwCTDMRate_Type()
)
cpwCTDMRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpwCTDMRate.setStatus("current")
_CpwCTDMIfIndex_Type = InterfaceIndexOrZero
_CpwCTDMIfIndex_Object = MibTableColumn
cpwCTDMIfIndex = _CpwCTDMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 1, 1, 2),
    _CpwCTDMIfIndex_Type()
)
cpwCTDMIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpwCTDMIfIndex.setStatus("current")
_CpwCGenTDMCfgIndex_Type = CpwTDMCfgIndex
_CpwCGenTDMCfgIndex_Object = MibTableColumn
cpwCGenTDMCfgIndex = _CpwCGenTDMCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 1, 1, 3),
    _CpwCGenTDMCfgIndex_Type()
)
cpwCGenTDMCfgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpwCGenTDMCfgIndex.setStatus("current")
_CpwCRelTDMCfgIndex_Type = CpwTDMCfgIndex
_CpwCRelTDMCfgIndex_Object = MibTableColumn
cpwCRelTDMCfgIndex = _CpwCRelTDMCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 1, 1, 4),
    _CpwCRelTDMCfgIndex_Type()
)
cpwCRelTDMCfgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpwCRelTDMCfgIndex.setStatus("current")


class _CpwCTDMConfigError_Type(Bits):
    """Custom type cpwCTDMConfigError based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("peerPayloadSizeIncompatible", 3),
          ("peerRtpIncompatible", 2),
          ("tdmTypeIncompatible", 1))
    )

_CpwCTDMConfigError_Type.__name__ = "Bits"
_CpwCTDMConfigError_Object = MibTableColumn
cpwCTDMConfigError = _CpwCTDMConfigError_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 1, 1, 5),
    _CpwCTDMConfigError_Type()
)
cpwCTDMConfigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMConfigError.setStatus("current")


class _CpwCTDMTimeElapsed_Type(Integer32):
    """Custom type cpwCTDMTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_CpwCTDMTimeElapsed_Type.__name__ = "Integer32"
_CpwCTDMTimeElapsed_Object = MibTableColumn
cpwCTDMTimeElapsed = _CpwCTDMTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 1, 1, 6),
    _CpwCTDMTimeElapsed_Type()
)
cpwCTDMTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMTimeElapsed.setUnits("seconds")


class _CpwCTDMValidIntervals_Type(Integer32):
    """Custom type cpwCTDMValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CpwCTDMValidIntervals_Type.__name__ = "Integer32"
_CpwCTDMValidIntervals_Object = MibTableColumn
cpwCTDMValidIntervals = _CpwCTDMValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 1, 1, 7),
    _CpwCTDMValidIntervals_Type()
)
cpwCTDMValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMValidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMValidIntervals.setUnits("minutes")


class _CpwCTDMValidDayIntervals_Type(Integer32):
    """Custom type cpwCTDMValidDayIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CpwCTDMValidDayIntervals_Type.__name__ = "Integer32"
_CpwCTDMValidDayIntervals_Object = MibTableColumn
cpwCTDMValidDayIntervals = _CpwCTDMValidDayIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 1, 1, 8),
    _CpwCTDMValidDayIntervals_Type()
)
cpwCTDMValidDayIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMValidDayIntervals.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMValidDayIntervals.setUnits("days")


class _CpwCTDMCurrentIndications_Type(Bits):
    """Custom type cpwCTDMCurrentIndications based on Bits"""
    namedValues = NamedValues(
        *(("bufferOverrun", 4),
          ("bufferUnderrun", 5),
          ("excessivePktLossRate", 3),
          ("malformedPacket", 2),
          ("other", 0),
          ("packetLoss", 8),
          ("pktMisOrder", 7),
          ("remotePktLoss", 6),
          ("strayPacket", 1),
          ("tdmFault", 9))
    )

_CpwCTDMCurrentIndications_Type.__name__ = "Bits"
_CpwCTDMCurrentIndications_Object = MibTableColumn
cpwCTDMCurrentIndications = _CpwCTDMCurrentIndications_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 1, 1, 9),
    _CpwCTDMCurrentIndications_Type()
)
cpwCTDMCurrentIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMCurrentIndications.setStatus("current")


class _CpwCTDMLatchedIndications_Type(Bits):
    """Custom type cpwCTDMLatchedIndications based on Bits"""
    namedValues = NamedValues(
        *(("bufferOverrun", 4),
          ("bufferUnderrun", 5),
          ("excessivePktLossRate", 3),
          ("malformedPacket", 2),
          ("other", 0),
          ("packetLoss", 8),
          ("pktMisOrder", 7),
          ("remotePktLoss", 6),
          ("staryPacket", 1),
          ("tdmFault", 9))
    )

_CpwCTDMLatchedIndications_Type.__name__ = "Bits"
_CpwCTDMLatchedIndications_Object = MibTableColumn
cpwCTDMLatchedIndications = _CpwCTDMLatchedIndications_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 1, 1, 10),
    _CpwCTDMLatchedIndications_Type()
)
cpwCTDMLatchedIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMLatchedIndications.setStatus("current")
_CpwCTDMLastEsTimeStamp_Type = TimeStamp
_CpwCTDMLastEsTimeStamp_Object = MibTableColumn
cpwCTDMLastEsTimeStamp = _CpwCTDMLastEsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 1, 1, 11),
    _CpwCTDMLastEsTimeStamp_Type()
)
cpwCTDMLastEsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMLastEsTimeStamp.setStatus("current")
_CpwCTDMCfgIndexNext_Type = Unsigned32
_CpwCTDMCfgIndexNext_Object = MibScalar
cpwCTDMCfgIndexNext = _CpwCTDMCfgIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 2),
    _CpwCTDMCfgIndexNext_Type()
)
cpwCTDMCfgIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMCfgIndexNext.setStatus("current")
_CpwCTDMCfgTable_Object = MibTable
cpwCTDMCfgTable = _CpwCTDMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3)
)
if mibBuilder.loadTexts:
    cpwCTDMCfgTable.setStatus("current")
_CpwCTDMCfgEntry_Object = MibTableRow
cpwCTDMCfgEntry = _CpwCTDMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1)
)
cpwCTDMCfgEntry.setIndexNames(
    (0, "CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgIndex"),
)
if mibBuilder.loadTexts:
    cpwCTDMCfgEntry.setStatus("current")
_CpwCTDMCfgIndex_Type = CpwTDMCfgIndex
_CpwCTDMCfgIndex_Object = MibTableColumn
cpwCTDMCfgIndex = _CpwCTDMCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 1),
    _CpwCTDMCfgIndex_Type()
)
cpwCTDMCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwCTDMCfgIndex.setStatus("current")


class _CpwCTDMCfgConfErr_Type(Bits):
    """Custom type cpwCTDMCfgConfErr based on Bits"""
    namedValues = NamedValues(
        *(("jtrBfrDepth", 2),
          ("other", 0),
          ("payloadSize", 1))
    )

_CpwCTDMCfgConfErr_Type.__name__ = "Bits"
_CpwCTDMCfgConfErr_Object = MibTableColumn
cpwCTDMCfgConfErr = _CpwCTDMCfgConfErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 2),
    _CpwCTDMCfgConfErr_Type()
)
cpwCTDMCfgConfErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMCfgConfErr.setStatus("current")


class _CpwCTDMCfgPayloadSize_Type(Unsigned32):
    """Custom type cpwCTDMCfgPayloadSize based on Unsigned32"""
    defaultValue = 32


_CpwCTDMCfgPayloadSize_Object = MibTableColumn
cpwCTDMCfgPayloadSize = _CpwCTDMCfgPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 3),
    _CpwCTDMCfgPayloadSize_Type()
)
cpwCTDMCfgPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgPayloadSize.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMCfgPayloadSize.setUnits("bytes")


class _CpwCTDMCfgPktReorder_Type(TruthValue):
    """Custom type cpwCTDMCfgPktReorder based on TruthValue"""


_CpwCTDMCfgPktReorder_Object = MibTableColumn
cpwCTDMCfgPktReorder = _CpwCTDMCfgPktReorder_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 4),
    _CpwCTDMCfgPktReorder_Type()
)
cpwCTDMCfgPktReorder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgPktReorder.setStatus("current")


class _CpwCTDMCfgRtpHdrUsed_Type(TruthValue):
    """Custom type cpwCTDMCfgRtpHdrUsed based on TruthValue"""


_CpwCTDMCfgRtpHdrUsed_Object = MibTableColumn
cpwCTDMCfgRtpHdrUsed = _CpwCTDMCfgRtpHdrUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 5),
    _CpwCTDMCfgRtpHdrUsed_Type()
)
cpwCTDMCfgRtpHdrUsed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgRtpHdrUsed.setStatus("current")


class _CpwCTDMCfgJtrBfrDepth_Type(Unsigned32):
    """Custom type cpwCTDMCfgJtrBfrDepth based on Unsigned32"""
    defaultValue = 3000


_CpwCTDMCfgJtrBfrDepth_Object = MibTableColumn
cpwCTDMCfgJtrBfrDepth = _CpwCTDMCfgJtrBfrDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 6),
    _CpwCTDMCfgJtrBfrDepth_Type()
)
cpwCTDMCfgJtrBfrDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgJtrBfrDepth.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMCfgJtrBfrDepth.setUnits("microsecond")


class _CpwCTDMCfgPayloadSuppression_Type(Integer32):
    """Custom type cpwCTDMCfgPayloadSuppression based on Integer32"""
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


_CpwCTDMCfgPayloadSuppression_Type.__name__ = "Integer32"
_CpwCTDMCfgPayloadSuppression_Object = MibTableColumn
cpwCTDMCfgPayloadSuppression = _CpwCTDMCfgPayloadSuppression_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 7),
    _CpwCTDMCfgPayloadSuppression_Type()
)
cpwCTDMCfgPayloadSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgPayloadSuppression.setStatus("current")


class _CpwCTDMCfgConsecPktsInSynch_Type(Unsigned32):
    """Custom type cpwCTDMCfgConsecPktsInSynch based on Unsigned32"""
    defaultValue = 2


_CpwCTDMCfgConsecPktsInSynch_Object = MibTableColumn
cpwCTDMCfgConsecPktsInSynch = _CpwCTDMCfgConsecPktsInSynch_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 8),
    _CpwCTDMCfgConsecPktsInSynch_Type()
)
cpwCTDMCfgConsecPktsInSynch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgConsecPktsInSynch.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMCfgConsecPktsInSynch.setUnits("packets")


class _CpwCTDMCfgConsecMissPktsOutSynch_Type(Unsigned32):
    """Custom type cpwCTDMCfgConsecMissPktsOutSynch based on Unsigned32"""
    defaultValue = 10


_CpwCTDMCfgConsecMissPktsOutSynch_Object = MibTableColumn
cpwCTDMCfgConsecMissPktsOutSynch = _CpwCTDMCfgConsecMissPktsOutSynch_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 9),
    _CpwCTDMCfgConsecMissPktsOutSynch_Type()
)
cpwCTDMCfgConsecMissPktsOutSynch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgConsecMissPktsOutSynch.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMCfgConsecMissPktsOutSynch.setUnits("packets")


class _CpwCTDMCfgSetUp2SynchTimeOut_Type(Unsigned32):
    """Custom type cpwCTDMCfgSetUp2SynchTimeOut based on Unsigned32"""
    defaultValue = 5000


_CpwCTDMCfgSetUp2SynchTimeOut_Object = MibTableColumn
cpwCTDMCfgSetUp2SynchTimeOut = _CpwCTDMCfgSetUp2SynchTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 10),
    _CpwCTDMCfgSetUp2SynchTimeOut_Type()
)
cpwCTDMCfgSetUp2SynchTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgSetUp2SynchTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMCfgSetUp2SynchTimeOut.setUnits("millisecond")


class _CpwCTDMCfgPktReplacePolicy_Type(Integer32):
    """Custom type cpwCTDMCfgPktReplacePolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ais", 1),
          ("implementationSpecific", 2))
    )


_CpwCTDMCfgPktReplacePolicy_Type.__name__ = "Integer32"
_CpwCTDMCfgPktReplacePolicy_Object = MibTableColumn
cpwCTDMCfgPktReplacePolicy = _CpwCTDMCfgPktReplacePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 11),
    _CpwCTDMCfgPktReplacePolicy_Type()
)
cpwCTDMCfgPktReplacePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgPktReplacePolicy.setStatus("current")


class _CpwCTDMCfgAvePktLossTimeWindow_Type(Integer32):
    """Custom type cpwCTDMCfgAvePktLossTimeWindow based on Integer32"""
    defaultValue = 20


_CpwCTDMCfgAvePktLossTimeWindow_Object = MibTableColumn
cpwCTDMCfgAvePktLossTimeWindow = _CpwCTDMCfgAvePktLossTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 12),
    _CpwCTDMCfgAvePktLossTimeWindow_Type()
)
cpwCTDMCfgAvePktLossTimeWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgAvePktLossTimeWindow.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMCfgAvePktLossTimeWindow.setUnits("millisecond")


class _CpwCTDMCfgExcessivePktLossThreshold_Type(Unsigned32):
    """Custom type cpwCTDMCfgExcessivePktLossThreshold based on Unsigned32"""
    defaultValue = 2


_CpwCTDMCfgExcessivePktLossThreshold_Object = MibTableColumn
cpwCTDMCfgExcessivePktLossThreshold = _CpwCTDMCfgExcessivePktLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 13),
    _CpwCTDMCfgExcessivePktLossThreshold_Type()
)
cpwCTDMCfgExcessivePktLossThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgExcessivePktLossThreshold.setStatus("current")


class _CpwCTDMCfgAlarmThreshold_Type(Unsigned32):
    """Custom type cpwCTDMCfgAlarmThreshold based on Unsigned32"""
    defaultValue = 2500


_CpwCTDMCfgAlarmThreshold_Object = MibTableColumn
cpwCTDMCfgAlarmThreshold = _CpwCTDMCfgAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 14),
    _CpwCTDMCfgAlarmThreshold_Type()
)
cpwCTDMCfgAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMCfgAlarmThreshold.setUnits("milliseconds")


class _CpwCTDMCfgClearAlarmThreshold_Type(Unsigned32):
    """Custom type cpwCTDMCfgClearAlarmThreshold based on Unsigned32"""
    defaultValue = 10000


_CpwCTDMCfgClearAlarmThreshold_Object = MibTableColumn
cpwCTDMCfgClearAlarmThreshold = _CpwCTDMCfgClearAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 15),
    _CpwCTDMCfgClearAlarmThreshold_Type()
)
cpwCTDMCfgClearAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgClearAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMCfgClearAlarmThreshold.setUnits("milliseconds")


class _CpwCTDMCfgMissingPktsToSes_Type(Unsigned32):
    """Custom type cpwCTDMCfgMissingPktsToSes based on Unsigned32"""
    defaultValue = 3


_CpwCTDMCfgMissingPktsToSes_Object = MibTableColumn
cpwCTDMCfgMissingPktsToSes = _CpwCTDMCfgMissingPktsToSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 16),
    _CpwCTDMCfgMissingPktsToSes_Type()
)
cpwCTDMCfgMissingPktsToSes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgMissingPktsToSes.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMCfgMissingPktsToSes.setUnits("seconds")


class _CpwCTDMCfgTimestampMode_Type(Integer32):
    """Custom type cpwCTDMCfgTimestampMode based on Integer32"""
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
        *(("absolute", 2),
          ("differential", 3),
          ("notApplicable", 1))
    )


_CpwCTDMCfgTimestampMode_Type.__name__ = "Integer32"
_CpwCTDMCfgTimestampMode_Object = MibTableColumn
cpwCTDMCfgTimestampMode = _CpwCTDMCfgTimestampMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 17),
    _CpwCTDMCfgTimestampMode_Type()
)
cpwCTDMCfgTimestampMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgTimestampMode.setStatus("current")


class _CpwCTDMCfgStorageType_Type(StorageType):
    """Custom type cpwCTDMCfgStorageType based on StorageType"""


_CpwCTDMCfgStorageType_Object = MibTableColumn
cpwCTDMCfgStorageType = _CpwCTDMCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 18),
    _CpwCTDMCfgStorageType_Type()
)
cpwCTDMCfgStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgStorageType.setStatus("current")
_CpwCTDMCfgRowStatus_Type = RowStatus
_CpwCTDMCfgRowStatus_Object = MibTableColumn
cpwCTDMCfgRowStatus = _CpwCTDMCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 3, 1, 19),
    _CpwCTDMCfgRowStatus_Type()
)
cpwCTDMCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwCTDMCfgRowStatus.setStatus("current")
_CpwCTDMPerfCurrentTable_Object = MibTable
cpwCTDMPerfCurrentTable = _CpwCTDMPerfCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 5)
)
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentTable.setStatus("current")
_CpwCTDMPerfCurrentEntry_Object = MibTableRow
cpwCTDMPerfCurrentEntry = _CpwCTDMPerfCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 5, 1)
)
cpwCTDMPerfCurrentEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
)
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentEntry.setStatus("current")
_CpwCTDMPerfCurrentMissingPkts_Type = PerfCurrentCount
_CpwCTDMPerfCurrentMissingPkts_Object = MibTableColumn
cpwCTDMPerfCurrentMissingPkts = _CpwCTDMPerfCurrentMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 5, 1, 1),
    _CpwCTDMPerfCurrentMissingPkts_Type()
)
cpwCTDMPerfCurrentMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentMissingPkts.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentMissingPkts.setUnits("packets")
_CpwCTDMPerfCurrentPktsReOrder_Type = PerfCurrentCount
_CpwCTDMPerfCurrentPktsReOrder_Object = MibTableColumn
cpwCTDMPerfCurrentPktsReOrder = _CpwCTDMPerfCurrentPktsReOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 5, 1, 2),
    _CpwCTDMPerfCurrentPktsReOrder_Type()
)
cpwCTDMPerfCurrentPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentPktsReOrder.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentPktsReOrder.setUnits("packets")
_CpwCTDMPerfCurrentJtrBfrUnderruns_Type = PerfCurrentCount
_CpwCTDMPerfCurrentJtrBfrUnderruns_Object = MibTableColumn
cpwCTDMPerfCurrentJtrBfrUnderruns = _CpwCTDMPerfCurrentJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 5, 1, 3),
    _CpwCTDMPerfCurrentJtrBfrUnderruns_Type()
)
cpwCTDMPerfCurrentJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentJtrBfrUnderruns.setStatus("current")
_CpwCTDMPerfCurrentMisOrderDropped_Type = PerfCurrentCount
_CpwCTDMPerfCurrentMisOrderDropped_Object = MibTableColumn
cpwCTDMPerfCurrentMisOrderDropped = _CpwCTDMPerfCurrentMisOrderDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 5, 1, 4),
    _CpwCTDMPerfCurrentMisOrderDropped_Type()
)
cpwCTDMPerfCurrentMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentMisOrderDropped.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentMisOrderDropped.setUnits("packets")
_CpwCTDMPerfCurrentMalformedPkt_Type = PerfCurrentCount
_CpwCTDMPerfCurrentMalformedPkt_Object = MibTableColumn
cpwCTDMPerfCurrentMalformedPkt = _CpwCTDMPerfCurrentMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 5, 1, 5),
    _CpwCTDMPerfCurrentMalformedPkt_Type()
)
cpwCTDMPerfCurrentMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentMalformedPkt.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentMalformedPkt.setUnits("packets")
_CpwCTDMPerfCurrentESs_Type = PerfCurrentCount
_CpwCTDMPerfCurrentESs_Object = MibTableColumn
cpwCTDMPerfCurrentESs = _CpwCTDMPerfCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 5, 1, 6),
    _CpwCTDMPerfCurrentESs_Type()
)
cpwCTDMPerfCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentESs.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentESs.setUnits("seconds")
_CpwCTDMPerfCurrentSESs_Type = PerfCurrentCount
_CpwCTDMPerfCurrentSESs_Object = MibTableColumn
cpwCTDMPerfCurrentSESs = _CpwCTDMPerfCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 5, 1, 7),
    _CpwCTDMPerfCurrentSESs_Type()
)
cpwCTDMPerfCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentSESs.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentSESs.setUnits("seconds")
_CpwCTDMPerfCurrentUASs_Type = PerfCurrentCount
_CpwCTDMPerfCurrentUASs_Object = MibTableColumn
cpwCTDMPerfCurrentUASs = _CpwCTDMPerfCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 5, 1, 8),
    _CpwCTDMPerfCurrentUASs_Type()
)
cpwCTDMPerfCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentUASs.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentUASs.setUnits("seconds")
_CpwCTDMPerfCurrentFC_Type = PerfCurrentCount
_CpwCTDMPerfCurrentFC_Object = MibTableColumn
cpwCTDMPerfCurrentFC = _CpwCTDMPerfCurrentFC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 5, 1, 9),
    _CpwCTDMPerfCurrentFC_Type()
)
cpwCTDMPerfCurrentFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentFC.setStatus("current")
_CpwCTDMPerfIntervalTable_Object = MibTable
cpwCTDMPerfIntervalTable = _CpwCTDMPerfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 6)
)
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalTable.setStatus("current")
_CpwCTDMPerfIntervalEntry_Object = MibTableRow
cpwCTDMPerfIntervalEntry = _CpwCTDMPerfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 6, 1)
)
cpwCTDMPerfIntervalEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
    (0, "CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalEntry.setStatus("current")
_CpwCTDMPerfIntervalNumber_Type = Unsigned32
_CpwCTDMPerfIntervalNumber_Object = MibTableColumn
cpwCTDMPerfIntervalNumber = _CpwCTDMPerfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 6, 1, 1),
    _CpwCTDMPerfIntervalNumber_Type()
)
cpwCTDMPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalNumber.setStatus("current")
_CpwCTDMPerfIntervalValidData_Type = TruthValue
_CpwCTDMPerfIntervalValidData_Object = MibTableColumn
cpwCTDMPerfIntervalValidData = _CpwCTDMPerfIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 6, 1, 2),
    _CpwCTDMPerfIntervalValidData_Type()
)
cpwCTDMPerfIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalValidData.setStatus("current")


class _CpwCTDMPerfIntervalDuration_Type(Unsigned32):
    """Custom type cpwCTDMPerfIntervalDuration based on Unsigned32"""
    defaultValue = 900


_CpwCTDMPerfIntervalDuration_Object = MibTableColumn
cpwCTDMPerfIntervalDuration = _CpwCTDMPerfIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 6, 1, 3),
    _CpwCTDMPerfIntervalDuration_Type()
)
cpwCTDMPerfIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalDuration.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalDuration.setUnits("seconds")
_CpwCTDMPerfIntervalMissingPkts_Type = PerfIntervalCount
_CpwCTDMPerfIntervalMissingPkts_Object = MibTableColumn
cpwCTDMPerfIntervalMissingPkts = _CpwCTDMPerfIntervalMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 6, 1, 4),
    _CpwCTDMPerfIntervalMissingPkts_Type()
)
cpwCTDMPerfIntervalMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalMissingPkts.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalMissingPkts.setUnits("packets")
_CpwCTDMPerfIntervalPktsReOrder_Type = PerfIntervalCount
_CpwCTDMPerfIntervalPktsReOrder_Object = MibTableColumn
cpwCTDMPerfIntervalPktsReOrder = _CpwCTDMPerfIntervalPktsReOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 6, 1, 5),
    _CpwCTDMPerfIntervalPktsReOrder_Type()
)
cpwCTDMPerfIntervalPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalPktsReOrder.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalPktsReOrder.setUnits("packets")
_CpwCTDMPerfIntervalJtrBfrUnderruns_Type = PerfIntervalCount
_CpwCTDMPerfIntervalJtrBfrUnderruns_Object = MibTableColumn
cpwCTDMPerfIntervalJtrBfrUnderruns = _CpwCTDMPerfIntervalJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 6, 1, 6),
    _CpwCTDMPerfIntervalJtrBfrUnderruns_Type()
)
cpwCTDMPerfIntervalJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalJtrBfrUnderruns.setStatus("current")
_CpwCTDMPerfIntervalMisOrderDropped_Type = PerfIntervalCount
_CpwCTDMPerfIntervalMisOrderDropped_Object = MibTableColumn
cpwCTDMPerfIntervalMisOrderDropped = _CpwCTDMPerfIntervalMisOrderDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 6, 1, 7),
    _CpwCTDMPerfIntervalMisOrderDropped_Type()
)
cpwCTDMPerfIntervalMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalMisOrderDropped.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalMisOrderDropped.setUnits("packets")
_CpwCTDMPerfIntervalMalformedPkt_Type = PerfIntervalCount
_CpwCTDMPerfIntervalMalformedPkt_Object = MibTableColumn
cpwCTDMPerfIntervalMalformedPkt = _CpwCTDMPerfIntervalMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 6, 1, 8),
    _CpwCTDMPerfIntervalMalformedPkt_Type()
)
cpwCTDMPerfIntervalMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalMalformedPkt.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalMalformedPkt.setUnits("packets")
_CpwCTDMPerfIntervalESs_Type = PerfIntervalCount
_CpwCTDMPerfIntervalESs_Object = MibTableColumn
cpwCTDMPerfIntervalESs = _CpwCTDMPerfIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 6, 1, 9),
    _CpwCTDMPerfIntervalESs_Type()
)
cpwCTDMPerfIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalESs.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalESs.setUnits("seconds")
_CpwCTDMPerfIntervalSESs_Type = PerfIntervalCount
_CpwCTDMPerfIntervalSESs_Object = MibTableColumn
cpwCTDMPerfIntervalSESs = _CpwCTDMPerfIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 6, 1, 10),
    _CpwCTDMPerfIntervalSESs_Type()
)
cpwCTDMPerfIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalSESs.setStatus("current")
_CpwCTDMPerfIntervalUASs_Type = PerfIntervalCount
_CpwCTDMPerfIntervalUASs_Object = MibTableColumn
cpwCTDMPerfIntervalUASs = _CpwCTDMPerfIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 6, 1, 11),
    _CpwCTDMPerfIntervalUASs_Type()
)
cpwCTDMPerfIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalUASs.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalUASs.setUnits("seconds")
_CpwCTDMPerfIntervalFC_Type = PerfIntervalCount
_CpwCTDMPerfIntervalFC_Object = MibTableColumn
cpwCTDMPerfIntervalFC = _CpwCTDMPerfIntervalFC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 6, 1, 12),
    _CpwCTDMPerfIntervalFC_Type()
)
cpwCTDMPerfIntervalFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalFC.setStatus("current")
_CpwCTDMPerf1DayIntervalTable_Object = MibTable
cpwCTDMPerf1DayIntervalTable = _CpwCTDMPerf1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 7)
)
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalTable.setStatus("current")
_CpwCTDMPerf1DayIntervalEntry_Object = MibTableRow
cpwCTDMPerf1DayIntervalEntry = _CpwCTDMPerf1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 7, 1)
)
cpwCTDMPerf1DayIntervalEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
    (0, "CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerf1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalEntry.setStatus("current")
_CpwCTDMPerf1DayIntervalNumber_Type = Unsigned32
_CpwCTDMPerf1DayIntervalNumber_Object = MibTableColumn
cpwCTDMPerf1DayIntervalNumber = _CpwCTDMPerf1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 7, 1, 1),
    _CpwCTDMPerf1DayIntervalNumber_Type()
)
cpwCTDMPerf1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalNumber.setStatus("current")
_CpwCTDMPerf1DayIntervalValidData_Type = TruthValue
_CpwCTDMPerf1DayIntervalValidData_Object = MibTableColumn
cpwCTDMPerf1DayIntervalValidData = _CpwCTDMPerf1DayIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 7, 1, 2),
    _CpwCTDMPerf1DayIntervalValidData_Type()
)
cpwCTDMPerf1DayIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalValidData.setStatus("current")
_CpwCTDMPerf1DayIntervalDuration_Type = Unsigned32
_CpwCTDMPerf1DayIntervalDuration_Object = MibTableColumn
cpwCTDMPerf1DayIntervalDuration = _CpwCTDMPerf1DayIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 7, 1, 3),
    _CpwCTDMPerf1DayIntervalDuration_Type()
)
cpwCTDMPerf1DayIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalDuration.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalDuration.setUnits("seconds")
_CpwCTDMPerf1DayIntervalMissingPkts_Type = Counter32
_CpwCTDMPerf1DayIntervalMissingPkts_Object = MibTableColumn
cpwCTDMPerf1DayIntervalMissingPkts = _CpwCTDMPerf1DayIntervalMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 7, 1, 4),
    _CpwCTDMPerf1DayIntervalMissingPkts_Type()
)
cpwCTDMPerf1DayIntervalMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalMissingPkts.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalMissingPkts.setUnits("packets")
_CpwCTDMPerf1DayIntervalPktsReOrder_Type = Counter32
_CpwCTDMPerf1DayIntervalPktsReOrder_Object = MibTableColumn
cpwCTDMPerf1DayIntervalPktsReOrder = _CpwCTDMPerf1DayIntervalPktsReOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 7, 1, 5),
    _CpwCTDMPerf1DayIntervalPktsReOrder_Type()
)
cpwCTDMPerf1DayIntervalPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalPktsReOrder.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalPktsReOrder.setUnits("packets")
_CpwCTDMPerf1DayIntervalJtrBfrUnderruns_Type = Counter32
_CpwCTDMPerf1DayIntervalJtrBfrUnderruns_Object = MibTableColumn
cpwCTDMPerf1DayIntervalJtrBfrUnderruns = _CpwCTDMPerf1DayIntervalJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 7, 1, 6),
    _CpwCTDMPerf1DayIntervalJtrBfrUnderruns_Type()
)
cpwCTDMPerf1DayIntervalJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalJtrBfrUnderruns.setStatus("current")
_CpwCTDMPerf1DayIntervalMisOrderDropped_Type = Counter32
_CpwCTDMPerf1DayIntervalMisOrderDropped_Object = MibTableColumn
cpwCTDMPerf1DayIntervalMisOrderDropped = _CpwCTDMPerf1DayIntervalMisOrderDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 7, 1, 7),
    _CpwCTDMPerf1DayIntervalMisOrderDropped_Type()
)
cpwCTDMPerf1DayIntervalMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalMisOrderDropped.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalMisOrderDropped.setUnits("packets")
_CpwCTDMPerf1DayIntervalMalformedPkt_Type = Counter32
_CpwCTDMPerf1DayIntervalMalformedPkt_Object = MibTableColumn
cpwCTDMPerf1DayIntervalMalformedPkt = _CpwCTDMPerf1DayIntervalMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 7, 1, 8),
    _CpwCTDMPerf1DayIntervalMalformedPkt_Type()
)
cpwCTDMPerf1DayIntervalMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalMalformedPkt.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalMalformedPkt.setUnits("packets")
_CpwCTDMPerf1DayIntervalESs_Type = Counter32
_CpwCTDMPerf1DayIntervalESs_Object = MibTableColumn
cpwCTDMPerf1DayIntervalESs = _CpwCTDMPerf1DayIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 7, 1, 9),
    _CpwCTDMPerf1DayIntervalESs_Type()
)
cpwCTDMPerf1DayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalESs.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalESs.setUnits("seconds")
_CpwCTDMPerf1DayIntervalSESs_Type = Counter32
_CpwCTDMPerf1DayIntervalSESs_Object = MibTableColumn
cpwCTDMPerf1DayIntervalSESs = _CpwCTDMPerf1DayIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 7, 1, 10),
    _CpwCTDMPerf1DayIntervalSESs_Type()
)
cpwCTDMPerf1DayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalSESs.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalSESs.setUnits("seconds")
_CpwCTDMPerf1DayIntervalUASs_Type = Counter32
_CpwCTDMPerf1DayIntervalUASs_Object = MibTableColumn
cpwCTDMPerf1DayIntervalUASs = _CpwCTDMPerf1DayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 7, 1, 11),
    _CpwCTDMPerf1DayIntervalUASs_Type()
)
cpwCTDMPerf1DayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalUASs.setStatus("current")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalUASs.setUnits("seconds")
_CpwCTDMPerf1DayIntervalFC_Type = Counter32
_CpwCTDMPerf1DayIntervalFC_Object = MibTableColumn
cpwCTDMPerf1DayIntervalFC = _CpwCTDMPerf1DayIntervalFC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 1, 7, 1, 12),
    _CpwCTDMPerf1DayIntervalFC_Type()
)
cpwCTDMPerf1DayIntervalFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalFC.setStatus("current")
_CpwCTDMConformance_ObjectIdentity = ObjectIdentity
cpwCTDMConformance = _CpwCTDMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 2)
)
_CpwCTDMGroups_ObjectIdentity = ObjectIdentity
cpwCTDMGroups = _CpwCTDMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 2, 1)
)
_CpwCTDMCompliances_ObjectIdentity = ObjectIdentity
cpwCTDMCompliances = _CpwCTDMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 2, 2)
)

# Managed Objects groups

cpwCTDMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 2, 1, 1)
)
cpwCTDMGroup.setObjects(
      *(("CISCO-IETF-PW-TDM-MIB", "cpwCTDMRate"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMIfIndex"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCGenTDMCfgIndex"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCRelTDMCfgIndex"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMConfigError"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMTimeElapsed"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMValidIntervals"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMValidDayIntervals"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCurrentIndications"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMLatchedIndications"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMLastEsTimeStamp"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgIndexNext"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgRowStatus"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgConfErr"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgPayloadSize"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgPktReorder"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgRtpHdrUsed"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgJtrBfrDepth"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgPayloadSuppression"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgConsecPktsInSynch"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgConsecMissPktsOutSynch"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgSetUp2SynchTimeOut"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgPktReplacePolicy"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgAvePktLossTimeWindow"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgExcessivePktLossThreshold"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgAlarmThreshold"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgClearAlarmThreshold"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgMissingPktsToSes"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgTimestampMode"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMCfgStorageType"))
)
if mibBuilder.loadTexts:
    cpwCTDMGroup.setStatus("current")

cpwCTDMPerfCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 2, 1, 2)
)
cpwCTDMPerfCurrentGroup.setObjects(
      *(("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfCurrentMissingPkts"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfCurrentPktsReOrder"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfCurrentJtrBfrUnderruns"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfCurrentMisOrderDropped"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfCurrentMalformedPkt"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfCurrentESs"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfCurrentSESs"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfCurrentUASs"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfCurrentFC"))
)
if mibBuilder.loadTexts:
    cpwCTDMPerfCurrentGroup.setStatus("current")

cpwCTDMPerfIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 2, 1, 3)
)
cpwCTDMPerfIntervalGroup.setObjects(
      *(("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfIntervalValidData"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfIntervalDuration"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfIntervalMissingPkts"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfIntervalPktsReOrder"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfIntervalJtrBfrUnderruns"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfIntervalMisOrderDropped"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfIntervalMalformedPkt"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfIntervalESs"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfIntervalSESs"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfIntervalUASs"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerfIntervalFC"))
)
if mibBuilder.loadTexts:
    cpwCTDMPerfIntervalGroup.setStatus("current")

cpwCTDMPerf1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 2, 1, 4)
)
cpwCTDMPerf1DayIntervalGroup.setObjects(
      *(("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerf1DayIntervalValidData"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerf1DayIntervalDuration"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerf1DayIntervalMissingPkts"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerf1DayIntervalPktsReOrder"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerf1DayIntervalJtrBfrUnderruns"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerf1DayIntervalMisOrderDropped"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerf1DayIntervalMalformedPkt"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerf1DayIntervalESs"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerf1DayIntervalSESs"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerf1DayIntervalUASs"),
        ("CISCO-IETF-PW-TDM-MIB", "cpwCTDMPerf1DayIntervalFC"))
)
if mibBuilder.loadTexts:
    cpwCTDMPerf1DayIntervalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cpwTDMModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 131, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpwTDMModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-PW-TDM-MIB",
    **{"CpwTDMCfgIndex": CpwTDMCfgIndex,
       "cpwCTDMMIB": cpwCTDMMIB,
       "cpwCTDMNotifications": cpwCTDMNotifications,
       "cpwCTDMObjects": cpwCTDMObjects,
       "cpwCTDMTable": cpwCTDMTable,
       "cpwCTDMEntry": cpwCTDMEntry,
       "cpwCTDMRate": cpwCTDMRate,
       "cpwCTDMIfIndex": cpwCTDMIfIndex,
       "cpwCGenTDMCfgIndex": cpwCGenTDMCfgIndex,
       "cpwCRelTDMCfgIndex": cpwCRelTDMCfgIndex,
       "cpwCTDMConfigError": cpwCTDMConfigError,
       "cpwCTDMTimeElapsed": cpwCTDMTimeElapsed,
       "cpwCTDMValidIntervals": cpwCTDMValidIntervals,
       "cpwCTDMValidDayIntervals": cpwCTDMValidDayIntervals,
       "cpwCTDMCurrentIndications": cpwCTDMCurrentIndications,
       "cpwCTDMLatchedIndications": cpwCTDMLatchedIndications,
       "cpwCTDMLastEsTimeStamp": cpwCTDMLastEsTimeStamp,
       "cpwCTDMCfgIndexNext": cpwCTDMCfgIndexNext,
       "cpwCTDMCfgTable": cpwCTDMCfgTable,
       "cpwCTDMCfgEntry": cpwCTDMCfgEntry,
       "cpwCTDMCfgIndex": cpwCTDMCfgIndex,
       "cpwCTDMCfgConfErr": cpwCTDMCfgConfErr,
       "cpwCTDMCfgPayloadSize": cpwCTDMCfgPayloadSize,
       "cpwCTDMCfgPktReorder": cpwCTDMCfgPktReorder,
       "cpwCTDMCfgRtpHdrUsed": cpwCTDMCfgRtpHdrUsed,
       "cpwCTDMCfgJtrBfrDepth": cpwCTDMCfgJtrBfrDepth,
       "cpwCTDMCfgPayloadSuppression": cpwCTDMCfgPayloadSuppression,
       "cpwCTDMCfgConsecPktsInSynch": cpwCTDMCfgConsecPktsInSynch,
       "cpwCTDMCfgConsecMissPktsOutSynch": cpwCTDMCfgConsecMissPktsOutSynch,
       "cpwCTDMCfgSetUp2SynchTimeOut": cpwCTDMCfgSetUp2SynchTimeOut,
       "cpwCTDMCfgPktReplacePolicy": cpwCTDMCfgPktReplacePolicy,
       "cpwCTDMCfgAvePktLossTimeWindow": cpwCTDMCfgAvePktLossTimeWindow,
       "cpwCTDMCfgExcessivePktLossThreshold": cpwCTDMCfgExcessivePktLossThreshold,
       "cpwCTDMCfgAlarmThreshold": cpwCTDMCfgAlarmThreshold,
       "cpwCTDMCfgClearAlarmThreshold": cpwCTDMCfgClearAlarmThreshold,
       "cpwCTDMCfgMissingPktsToSes": cpwCTDMCfgMissingPktsToSes,
       "cpwCTDMCfgTimestampMode": cpwCTDMCfgTimestampMode,
       "cpwCTDMCfgStorageType": cpwCTDMCfgStorageType,
       "cpwCTDMCfgRowStatus": cpwCTDMCfgRowStatus,
       "cpwCTDMPerfCurrentTable": cpwCTDMPerfCurrentTable,
       "cpwCTDMPerfCurrentEntry": cpwCTDMPerfCurrentEntry,
       "cpwCTDMPerfCurrentMissingPkts": cpwCTDMPerfCurrentMissingPkts,
       "cpwCTDMPerfCurrentPktsReOrder": cpwCTDMPerfCurrentPktsReOrder,
       "cpwCTDMPerfCurrentJtrBfrUnderruns": cpwCTDMPerfCurrentJtrBfrUnderruns,
       "cpwCTDMPerfCurrentMisOrderDropped": cpwCTDMPerfCurrentMisOrderDropped,
       "cpwCTDMPerfCurrentMalformedPkt": cpwCTDMPerfCurrentMalformedPkt,
       "cpwCTDMPerfCurrentESs": cpwCTDMPerfCurrentESs,
       "cpwCTDMPerfCurrentSESs": cpwCTDMPerfCurrentSESs,
       "cpwCTDMPerfCurrentUASs": cpwCTDMPerfCurrentUASs,
       "cpwCTDMPerfCurrentFC": cpwCTDMPerfCurrentFC,
       "cpwCTDMPerfIntervalTable": cpwCTDMPerfIntervalTable,
       "cpwCTDMPerfIntervalEntry": cpwCTDMPerfIntervalEntry,
       "cpwCTDMPerfIntervalNumber": cpwCTDMPerfIntervalNumber,
       "cpwCTDMPerfIntervalValidData": cpwCTDMPerfIntervalValidData,
       "cpwCTDMPerfIntervalDuration": cpwCTDMPerfIntervalDuration,
       "cpwCTDMPerfIntervalMissingPkts": cpwCTDMPerfIntervalMissingPkts,
       "cpwCTDMPerfIntervalPktsReOrder": cpwCTDMPerfIntervalPktsReOrder,
       "cpwCTDMPerfIntervalJtrBfrUnderruns": cpwCTDMPerfIntervalJtrBfrUnderruns,
       "cpwCTDMPerfIntervalMisOrderDropped": cpwCTDMPerfIntervalMisOrderDropped,
       "cpwCTDMPerfIntervalMalformedPkt": cpwCTDMPerfIntervalMalformedPkt,
       "cpwCTDMPerfIntervalESs": cpwCTDMPerfIntervalESs,
       "cpwCTDMPerfIntervalSESs": cpwCTDMPerfIntervalSESs,
       "cpwCTDMPerfIntervalUASs": cpwCTDMPerfIntervalUASs,
       "cpwCTDMPerfIntervalFC": cpwCTDMPerfIntervalFC,
       "cpwCTDMPerf1DayIntervalTable": cpwCTDMPerf1DayIntervalTable,
       "cpwCTDMPerf1DayIntervalEntry": cpwCTDMPerf1DayIntervalEntry,
       "cpwCTDMPerf1DayIntervalNumber": cpwCTDMPerf1DayIntervalNumber,
       "cpwCTDMPerf1DayIntervalValidData": cpwCTDMPerf1DayIntervalValidData,
       "cpwCTDMPerf1DayIntervalDuration": cpwCTDMPerf1DayIntervalDuration,
       "cpwCTDMPerf1DayIntervalMissingPkts": cpwCTDMPerf1DayIntervalMissingPkts,
       "cpwCTDMPerf1DayIntervalPktsReOrder": cpwCTDMPerf1DayIntervalPktsReOrder,
       "cpwCTDMPerf1DayIntervalJtrBfrUnderruns": cpwCTDMPerf1DayIntervalJtrBfrUnderruns,
       "cpwCTDMPerf1DayIntervalMisOrderDropped": cpwCTDMPerf1DayIntervalMisOrderDropped,
       "cpwCTDMPerf1DayIntervalMalformedPkt": cpwCTDMPerf1DayIntervalMalformedPkt,
       "cpwCTDMPerf1DayIntervalESs": cpwCTDMPerf1DayIntervalESs,
       "cpwCTDMPerf1DayIntervalSESs": cpwCTDMPerf1DayIntervalSESs,
       "cpwCTDMPerf1DayIntervalUASs": cpwCTDMPerf1DayIntervalUASs,
       "cpwCTDMPerf1DayIntervalFC": cpwCTDMPerf1DayIntervalFC,
       "cpwCTDMConformance": cpwCTDMConformance,
       "cpwCTDMGroups": cpwCTDMGroups,
       "cpwCTDMGroup": cpwCTDMGroup,
       "cpwCTDMPerfCurrentGroup": cpwCTDMPerfCurrentGroup,
       "cpwCTDMPerfIntervalGroup": cpwCTDMPerfIntervalGroup,
       "cpwCTDMPerf1DayIntervalGroup": cpwCTDMPerf1DayIntervalGroup,
       "cpwCTDMCompliances": cpwCTDMCompliances,
       "cpwTDMModuleCompliance": cpwTDMModuleCompliance}
)
