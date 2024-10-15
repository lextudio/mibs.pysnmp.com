# SNMP MIB module (MEF-SOAM-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MEF-SOAM-PM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:48 2024
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

(Dot1afCfmIndexIntegerNextFree,
 Dot1agCfmMepIdOrZero,
 dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1afCfmIndexIntegerNextFree",
    "Dot1agCfmMepIdOrZero",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier")

(IEEE8021PriorityValue,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue")

(MefSoamTcAvailabilityType,
 MefSoamTcDataPatternType,
 MefSoamTcDelayMeasurementBinType,
 MefSoamTcMeasurementPeriodType,
 MefSoamTcOperationTimeType,
 MefSoamTcSessionType,
 MefSoamTcStatusType,
 MefSoamTcTestPatternType) = mibBuilder.importSymbols(
    "MEF-SOAM-TC-MIB",
    "MefSoamTcAvailabilityType",
    "MefSoamTcDataPatternType",
    "MefSoamTcDelayMeasurementBinType",
    "MefSoamTcMeasurementPeriodType",
    "MefSoamTcOperationTimeType",
    "MefSoamTcSessionType",
    "MefSoamTcStatusType",
    "MefSoamTcTestPatternType")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

mefSoamPmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3)
)
mefSoamPmMib.setRevisions(
        ("2012-01-13 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MefSoamPmNotifications_ObjectIdentity = ObjectIdentity
mefSoamPmNotifications = _MefSoamPmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 0)
)
_MefSoamPmMibObjects_ObjectIdentity = ObjectIdentity
mefSoamPmMibObjects = _MefSoamPmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1)
)
_MefSoamPmMep_ObjectIdentity = ObjectIdentity
mefSoamPmMep = _MefSoamPmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 1)
)
_MefSoamPmMepTable_Object = MibTable
mefSoamPmMepTable = _MefSoamPmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamPmMepTable.setStatus("current")
_MefSoamPmMepEntry_Object = MibTableRow
mefSoamPmMepEntry = _MefSoamPmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamPmMepEntry.setStatus("current")
_MefSoamPmMepOperNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_MefSoamPmMepOperNextIndex_Object = MibTableColumn
mefSoamPmMepOperNextIndex = _MefSoamPmMepOperNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 1, 1, 1, 1),
    _MefSoamPmMepOperNextIndex_Type()
)
mefSoamPmMepOperNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamPmMepOperNextIndex.setStatus("current")


class _MefSoamPmMepLmSingleEndedResponder_Type(TruthValue):
    """Custom type mefSoamPmMepLmSingleEndedResponder based on TruthValue"""


_MefSoamPmMepLmSingleEndedResponder_Object = MibTableColumn
mefSoamPmMepLmSingleEndedResponder = _MefSoamPmMepLmSingleEndedResponder_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 1, 1, 1, 2),
    _MefSoamPmMepLmSingleEndedResponder_Type()
)
mefSoamPmMepLmSingleEndedResponder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefSoamPmMepLmSingleEndedResponder.setStatus("current")


class _MefSoamPmMepSlmSingleEndedResponder_Type(TruthValue):
    """Custom type mefSoamPmMepSlmSingleEndedResponder based on TruthValue"""


_MefSoamPmMepSlmSingleEndedResponder_Object = MibTableColumn
mefSoamPmMepSlmSingleEndedResponder = _MefSoamPmMepSlmSingleEndedResponder_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 1, 1, 1, 3),
    _MefSoamPmMepSlmSingleEndedResponder_Type()
)
mefSoamPmMepSlmSingleEndedResponder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefSoamPmMepSlmSingleEndedResponder.setStatus("current")


class _MefSoamPmMepDmSingleEndedResponder_Type(TruthValue):
    """Custom type mefSoamPmMepDmSingleEndedResponder based on TruthValue"""


_MefSoamPmMepDmSingleEndedResponder_Object = MibTableColumn
mefSoamPmMepDmSingleEndedResponder = _MefSoamPmMepDmSingleEndedResponder_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 1, 1, 1, 4),
    _MefSoamPmMepDmSingleEndedResponder_Type()
)
mefSoamPmMepDmSingleEndedResponder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefSoamPmMepDmSingleEndedResponder.setStatus("current")
_MefSoamPmLmObjects_ObjectIdentity = ObjectIdentity
mefSoamPmLmObjects = _MefSoamPmLmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2)
)
_MefSoamLmCfgTable_Object = MibTable
mefSoamLmCfgTable = _MefSoamLmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mefSoamLmCfgTable.setStatus("current")
_MefSoamLmCfgEntry_Object = MibTableRow
mefSoamLmCfgEntry = _MefSoamLmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1)
)
mefSoamLmCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamLmCfgEntry.setStatus("current")


class _MefSoamLmCfgIndex_Type(Unsigned32):
    """Custom type mefSoamLmCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MefSoamLmCfgIndex_Type.__name__ = "Unsigned32"
_MefSoamLmCfgIndex_Object = MibTableColumn
mefSoamLmCfgIndex = _MefSoamLmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 1),
    _MefSoamLmCfgIndex_Type()
)
mefSoamLmCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamLmCfgIndex.setStatus("current")


class _MefSoamLmCfgType_Type(Integer32):
    """Custom type mefSoamLmCfgType based on Integer32"""
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
        *(("lmCcm", 3),
          ("lmLmm", 1),
          ("lmSlm", 2))
    )


_MefSoamLmCfgType_Type.__name__ = "Integer32"
_MefSoamLmCfgType_Object = MibTableColumn
mefSoamLmCfgType = _MefSoamLmCfgType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 2),
    _MefSoamLmCfgType_Type()
)
mefSoamLmCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgType.setStatus("current")


class _MefSoamLmCfgVersion_Type(Unsigned32):
    """Custom type mefSoamLmCfgVersion based on Unsigned32"""
    defaultValue = 0


_MefSoamLmCfgVersion_Object = MibTableColumn
mefSoamLmCfgVersion = _MefSoamLmCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 3),
    _MefSoamLmCfgVersion_Type()
)
mefSoamLmCfgVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgVersion.setStatus("current")


class _MefSoamLmCfgEnabled_Type(TruthValue):
    """Custom type mefSoamLmCfgEnabled based on TruthValue"""


_MefSoamLmCfgEnabled_Object = MibTableColumn
mefSoamLmCfgEnabled = _MefSoamLmCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 4),
    _MefSoamLmCfgEnabled_Type()
)
mefSoamLmCfgEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgEnabled.setStatus("current")


class _MefSoamLmCfgMeasurementEnable_Type(Bits):
    """Custom type mefSoamLmCfgMeasurementEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bAvailBackwardAvailable", 21),
          ("bAvailBackwardAvgFlr", 25),
          ("bAvailBackwardConsecutiveHighLoss", 20),
          ("bAvailBackwardHighLoss", 19),
          ("bAvailBackwardMaxFlr", 24),
          ("bAvailBackwardMinFlr", 23),
          ("bAvailBackwardUnavailable", 22),
          ("bAvailForwardAvailable", 14),
          ("bAvailForwardAvgFlr", 18),
          ("bAvailForwardConsecutiveHighLoss", 13),
          ("bAvailForwardHighLoss", 12),
          ("bAvailForwardMaxFlr", 17),
          ("bAvailForwardMinFlr", 16),
          ("bAvailForwardUnavailable", 15),
          ("bBackwardAvgFlr", 9),
          ("bBackwardMaxFlr", 8),
          ("bBackwardMinFlr", 7),
          ("bBackwardReceivedFrames", 6),
          ("bBackwardTransmitedFrames", 5),
          ("bForwardAvgFlr", 4),
          ("bForwardMaxFlr", 3),
          ("bForwardMinFlr", 2),
          ("bForwardReceivedFrames", 1),
          ("bForwardTransmitedFrames", 0),
          ("bMeasuredStatsAvailBackwardStatus", 29),
          ("bMeasuredStatsAvailForwardStatus", 28),
          ("bMeasuredStatsBackwardMeasuredFlr", 27),
          ("bMeasuredStatsForwardMeasuredFlr", 26),
          ("bSoamPdusReceived", 11),
          ("bSoamPdusSent", 10))
    )

_MefSoamLmCfgMeasurementEnable_Type.__name__ = "Bits"
_MefSoamLmCfgMeasurementEnable_Object = MibTableColumn
mefSoamLmCfgMeasurementEnable = _MefSoamLmCfgMeasurementEnable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 5),
    _MefSoamLmCfgMeasurementEnable_Type()
)
mefSoamLmCfgMeasurementEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgMeasurementEnable.setStatus("current")


class _MefSoamLmCfgMessagePeriod_Type(MefSoamTcMeasurementPeriodType):
    """Custom type mefSoamLmCfgMessagePeriod based on MefSoamTcMeasurementPeriodType"""
    defaultValue = 1000


_MefSoamLmCfgMessagePeriod_Object = MibTableColumn
mefSoamLmCfgMessagePeriod = _MefSoamLmCfgMessagePeriod_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 6),
    _MefSoamLmCfgMessagePeriod_Type()
)
mefSoamLmCfgMessagePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgMessagePeriod.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCfgMessagePeriod.setUnits("ms")
_MefSoamLmCfgPriority_Type = IEEE8021PriorityValue
_MefSoamLmCfgPriority_Object = MibTableColumn
mefSoamLmCfgPriority = _MefSoamLmCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 7),
    _MefSoamLmCfgPriority_Type()
)
mefSoamLmCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgPriority.setStatus("current")


class _MefSoamLmCfgFrameSize_Type(Unsigned32):
    """Custom type mefSoamLmCfgFrameSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9600),
    )


_MefSoamLmCfgFrameSize_Type.__name__ = "Unsigned32"
_MefSoamLmCfgFrameSize_Object = MibTableColumn
mefSoamLmCfgFrameSize = _MefSoamLmCfgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 8),
    _MefSoamLmCfgFrameSize_Type()
)
mefSoamLmCfgFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCfgFrameSize.setUnits("bytes")


class _MefSoamLmCfgDataPattern_Type(MefSoamTcDataPatternType):
    """Custom type mefSoamLmCfgDataPattern based on MefSoamTcDataPatternType"""


_MefSoamLmCfgDataPattern_Object = MibTableColumn
mefSoamLmCfgDataPattern = _MefSoamLmCfgDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 9),
    _MefSoamLmCfgDataPattern_Type()
)
mefSoamLmCfgDataPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgDataPattern.setStatus("current")


class _MefSoamLmCfgTestTlvIncluded_Type(TruthValue):
    """Custom type mefSoamLmCfgTestTlvIncluded based on TruthValue"""


_MefSoamLmCfgTestTlvIncluded_Object = MibTableColumn
mefSoamLmCfgTestTlvIncluded = _MefSoamLmCfgTestTlvIncluded_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 10),
    _MefSoamLmCfgTestTlvIncluded_Type()
)
mefSoamLmCfgTestTlvIncluded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgTestTlvIncluded.setStatus("current")


class _MefSoamLmCfgTestTlvPattern_Type(MefSoamTcTestPatternType):
    """Custom type mefSoamLmCfgTestTlvPattern based on MefSoamTcTestPatternType"""


_MefSoamLmCfgTestTlvPattern_Object = MibTableColumn
mefSoamLmCfgTestTlvPattern = _MefSoamLmCfgTestTlvPattern_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 11),
    _MefSoamLmCfgTestTlvPattern_Type()
)
mefSoamLmCfgTestTlvPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgTestTlvPattern.setStatus("current")


class _MefSoamLmCfgMeasurementInterval_Type(Unsigned32):
    """Custom type mefSoamLmCfgMeasurementInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 525600),
    )


_MefSoamLmCfgMeasurementInterval_Type.__name__ = "Unsigned32"
_MefSoamLmCfgMeasurementInterval_Object = MibTableColumn
mefSoamLmCfgMeasurementInterval = _MefSoamLmCfgMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 12),
    _MefSoamLmCfgMeasurementInterval_Type()
)
mefSoamLmCfgMeasurementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCfgMeasurementInterval.setUnits("minutes")


class _MefSoamLmCfgNumIntervalsStored_Type(Unsigned32):
    """Custom type mefSoamLmCfgNumIntervalsStored based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1000),
    )


_MefSoamLmCfgNumIntervalsStored_Type.__name__ = "Unsigned32"
_MefSoamLmCfgNumIntervalsStored_Object = MibTableColumn
mefSoamLmCfgNumIntervalsStored = _MefSoamLmCfgNumIntervalsStored_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 13),
    _MefSoamLmCfgNumIntervalsStored_Type()
)
mefSoamLmCfgNumIntervalsStored.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgNumIntervalsStored.setStatus("current")
_MefSoamLmCfgDestMacAddress_Type = MacAddress
_MefSoamLmCfgDestMacAddress_Object = MibTableColumn
mefSoamLmCfgDestMacAddress = _MefSoamLmCfgDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 14),
    _MefSoamLmCfgDestMacAddress_Type()
)
mefSoamLmCfgDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgDestMacAddress.setStatus("current")


class _MefSoamLmCfgDestMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type mefSoamLmCfgDestMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_MefSoamLmCfgDestMepId_Object = MibTableColumn
mefSoamLmCfgDestMepId = _MefSoamLmCfgDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 15),
    _MefSoamLmCfgDestMepId_Type()
)
mefSoamLmCfgDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgDestMepId.setStatus("current")


class _MefSoamLmCfgDestIsMepId_Type(TruthValue):
    """Custom type mefSoamLmCfgDestIsMepId based on TruthValue"""


_MefSoamLmCfgDestIsMepId_Object = MibTableColumn
mefSoamLmCfgDestIsMepId = _MefSoamLmCfgDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 16),
    _MefSoamLmCfgDestIsMepId_Type()
)
mefSoamLmCfgDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgDestIsMepId.setStatus("current")


class _MefSoamLmCfgStartTimeType_Type(MefSoamTcOperationTimeType):
    """Custom type mefSoamLmCfgStartTimeType based on MefSoamTcOperationTimeType"""


_MefSoamLmCfgStartTimeType_Object = MibTableColumn
mefSoamLmCfgStartTimeType = _MefSoamLmCfgStartTimeType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 17),
    _MefSoamLmCfgStartTimeType_Type()
)
mefSoamLmCfgStartTimeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgStartTimeType.setStatus("current")


class _MefSoamLmCfgFixedStartDateAndTime_Type(DateAndTime):
    """Custom type mefSoamLmCfgFixedStartDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_MefSoamLmCfgFixedStartDateAndTime_Object = MibTableColumn
mefSoamLmCfgFixedStartDateAndTime = _MefSoamLmCfgFixedStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 18),
    _MefSoamLmCfgFixedStartDateAndTime_Type()
)
mefSoamLmCfgFixedStartDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgFixedStartDateAndTime.setStatus("current")


class _MefSoamLmCfgRelativeStartTime_Type(TimeInterval):
    """Custom type mefSoamLmCfgRelativeStartTime based on TimeInterval"""
    defaultValue = 0


_MefSoamLmCfgRelativeStartTime_Object = MibTableColumn
mefSoamLmCfgRelativeStartTime = _MefSoamLmCfgRelativeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 19),
    _MefSoamLmCfgRelativeStartTime_Type()
)
mefSoamLmCfgRelativeStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgRelativeStartTime.setStatus("current")


class _MefSoamLmCfgStopTimeType_Type(MefSoamTcOperationTimeType):
    """Custom type mefSoamLmCfgStopTimeType based on MefSoamTcOperationTimeType"""


_MefSoamLmCfgStopTimeType_Object = MibTableColumn
mefSoamLmCfgStopTimeType = _MefSoamLmCfgStopTimeType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 20),
    _MefSoamLmCfgStopTimeType_Type()
)
mefSoamLmCfgStopTimeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgStopTimeType.setStatus("current")


class _MefSoamLmCfgFixedStopDateAndTime_Type(DateAndTime):
    """Custom type mefSoamLmCfgFixedStopDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_MefSoamLmCfgFixedStopDateAndTime_Object = MibTableColumn
mefSoamLmCfgFixedStopDateAndTime = _MefSoamLmCfgFixedStopDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 21),
    _MefSoamLmCfgFixedStopDateAndTime_Type()
)
mefSoamLmCfgFixedStopDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgFixedStopDateAndTime.setStatus("current")


class _MefSoamLmCfgRelativeStopTime_Type(TimeInterval):
    """Custom type mefSoamLmCfgRelativeStopTime based on TimeInterval"""
    defaultValue = 0


_MefSoamLmCfgRelativeStopTime_Object = MibTableColumn
mefSoamLmCfgRelativeStopTime = _MefSoamLmCfgRelativeStopTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 22),
    _MefSoamLmCfgRelativeStopTime_Type()
)
mefSoamLmCfgRelativeStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgRelativeStopTime.setStatus("current")


class _MefSoamLmCfgRepetitionTime_Type(Unsigned32):
    """Custom type mefSoamLmCfgRepetitionTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_MefSoamLmCfgRepetitionTime_Type.__name__ = "Unsigned32"
_MefSoamLmCfgRepetitionTime_Object = MibTableColumn
mefSoamLmCfgRepetitionTime = _MefSoamLmCfgRepetitionTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 23),
    _MefSoamLmCfgRepetitionTime_Type()
)
mefSoamLmCfgRepetitionTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgRepetitionTime.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCfgRepetitionTime.setUnits("seconds")


class _MefSoamLmCfgAlignMeasurementIntervals_Type(TruthValue):
    """Custom type mefSoamLmCfgAlignMeasurementIntervals based on TruthValue"""


_MefSoamLmCfgAlignMeasurementIntervals_Object = MibTableColumn
mefSoamLmCfgAlignMeasurementIntervals = _MefSoamLmCfgAlignMeasurementIntervals_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 24),
    _MefSoamLmCfgAlignMeasurementIntervals_Type()
)
mefSoamLmCfgAlignMeasurementIntervals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgAlignMeasurementIntervals.setStatus("current")


class _MefSoamLmCfgAlignMeasurementOffset_Type(Unsigned32):
    """Custom type mefSoamLmCfgAlignMeasurementOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 525600),
    )


_MefSoamLmCfgAlignMeasurementOffset_Type.__name__ = "Unsigned32"
_MefSoamLmCfgAlignMeasurementOffset_Object = MibTableColumn
mefSoamLmCfgAlignMeasurementOffset = _MefSoamLmCfgAlignMeasurementOffset_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 25),
    _MefSoamLmCfgAlignMeasurementOffset_Type()
)
mefSoamLmCfgAlignMeasurementOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgAlignMeasurementOffset.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCfgAlignMeasurementOffset.setUnits("minutes")


class _MefSoamLmCfgAvailabilityMeasurementInterval_Type(Unsigned32):
    """Custom type mefSoamLmCfgAvailabilityMeasurementInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 525600),
    )


_MefSoamLmCfgAvailabilityMeasurementInterval_Type.__name__ = "Unsigned32"
_MefSoamLmCfgAvailabilityMeasurementInterval_Object = MibTableColumn
mefSoamLmCfgAvailabilityMeasurementInterval = _MefSoamLmCfgAvailabilityMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 26),
    _MefSoamLmCfgAvailabilityMeasurementInterval_Type()
)
mefSoamLmCfgAvailabilityMeasurementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgAvailabilityMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCfgAvailabilityMeasurementInterval.setUnits("minutes")


class _MefSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Type(Unsigned32):
    """Custom type mefSoamLmCfgAvailabilityNumConsecutiveMeasPdus based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_MefSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Type.__name__ = "Unsigned32"
_MefSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Object = MibTableColumn
mefSoamLmCfgAvailabilityNumConsecutiveMeasPdus = _MefSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 27),
    _MefSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Type()
)
mefSoamLmCfgAvailabilityNumConsecutiveMeasPdus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgAvailabilityNumConsecutiveMeasPdus.setStatus("current")


class _MefSoamLmCfgAvailabilityFlrThreshold_Type(Unsigned32):
    """Custom type mefSoamLmCfgAvailabilityFlrThreshold based on Unsigned32"""
    defaultValue = 50000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCfgAvailabilityFlrThreshold_Type.__name__ = "Unsigned32"
_MefSoamLmCfgAvailabilityFlrThreshold_Object = MibTableColumn
mefSoamLmCfgAvailabilityFlrThreshold = _MefSoamLmCfgAvailabilityFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 28),
    _MefSoamLmCfgAvailabilityFlrThreshold_Type()
)
mefSoamLmCfgAvailabilityFlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgAvailabilityFlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCfgAvailabilityFlrThreshold.setUnits("milli-percent")


class _MefSoamLmCfgAvailabilityNumConsecutiveIntervals_Type(Unsigned32):
    """Custom type mefSoamLmCfgAvailabilityNumConsecutiveIntervals based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MefSoamLmCfgAvailabilityNumConsecutiveIntervals_Type.__name__ = "Unsigned32"
_MefSoamLmCfgAvailabilityNumConsecutiveIntervals_Object = MibTableColumn
mefSoamLmCfgAvailabilityNumConsecutiveIntervals = _MefSoamLmCfgAvailabilityNumConsecutiveIntervals_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 29),
    _MefSoamLmCfgAvailabilityNumConsecutiveIntervals_Type()
)
mefSoamLmCfgAvailabilityNumConsecutiveIntervals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgAvailabilityNumConsecutiveIntervals.setStatus("current")


class _MefSoamLmCfgAvailabilityNumConsecutiveHighFlr_Type(Unsigned32):
    """Custom type mefSoamLmCfgAvailabilityNumConsecutiveHighFlr based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MefSoamLmCfgAvailabilityNumConsecutiveHighFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCfgAvailabilityNumConsecutiveHighFlr_Object = MibTableColumn
mefSoamLmCfgAvailabilityNumConsecutiveHighFlr = _MefSoamLmCfgAvailabilityNumConsecutiveHighFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 30),
    _MefSoamLmCfgAvailabilityNumConsecutiveHighFlr_Type()
)
mefSoamLmCfgAvailabilityNumConsecutiveHighFlr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgAvailabilityNumConsecutiveHighFlr.setStatus("current")


class _MefSoamLmCfgSessionType_Type(MefSoamTcSessionType):
    """Custom type mefSoamLmCfgSessionType based on MefSoamTcSessionType"""


_MefSoamLmCfgSessionType_Object = MibTableColumn
mefSoamLmCfgSessionType = _MefSoamLmCfgSessionType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 31),
    _MefSoamLmCfgSessionType_Type()
)
mefSoamLmCfgSessionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgSessionType.setStatus("current")
_MefSoamLmCfgSessionStatus_Type = MefSoamTcStatusType
_MefSoamLmCfgSessionStatus_Object = MibTableColumn
mefSoamLmCfgSessionStatus = _MefSoamLmCfgSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 32),
    _MefSoamLmCfgSessionStatus_Type()
)
mefSoamLmCfgSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCfgSessionStatus.setStatus("current")


class _MefSoamLmCfgHistoryClear_Type(TruthValue):
    """Custom type mefSoamLmCfgHistoryClear based on TruthValue"""


_MefSoamLmCfgHistoryClear_Object = MibTableColumn
mefSoamLmCfgHistoryClear = _MefSoamLmCfgHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 33),
    _MefSoamLmCfgHistoryClear_Type()
)
mefSoamLmCfgHistoryClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgHistoryClear.setStatus("current")
_MefSoamLmCfgRowStatus_Type = RowStatus
_MefSoamLmCfgRowStatus_Object = MibTableColumn
mefSoamLmCfgRowStatus = _MefSoamLmCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 34),
    _MefSoamLmCfgRowStatus_Type()
)
mefSoamLmCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgRowStatus.setStatus("current")
_MefSoamLmMeasuredStatsTable_Object = MibTable
mefSoamLmMeasuredStatsTable = _MefSoamLmMeasuredStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsTable.setStatus("current")
_MefSoamLmMeasuredStatsEntry_Object = MibTableRow
mefSoamLmMeasuredStatsEntry = _MefSoamLmMeasuredStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2, 1)
)
mefSoamLmMeasuredStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsEntry.setStatus("current")


class _MefSoamLmMeasuredStatsForwardFlr_Type(Unsigned32):
    """Custom type mefSoamLmMeasuredStatsForwardFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmMeasuredStatsForwardFlr_Type.__name__ = "Unsigned32"
_MefSoamLmMeasuredStatsForwardFlr_Object = MibTableColumn
mefSoamLmMeasuredStatsForwardFlr = _MefSoamLmMeasuredStatsForwardFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2, 1, 1),
    _MefSoamLmMeasuredStatsForwardFlr_Type()
)
mefSoamLmMeasuredStatsForwardFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsForwardFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsForwardFlr.setUnits("milli-percent")


class _MefSoamLmMeasuredStatsBackwardFlr_Type(Unsigned32):
    """Custom type mefSoamLmMeasuredStatsBackwardFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmMeasuredStatsBackwardFlr_Type.__name__ = "Unsigned32"
_MefSoamLmMeasuredStatsBackwardFlr_Object = MibTableColumn
mefSoamLmMeasuredStatsBackwardFlr = _MefSoamLmMeasuredStatsBackwardFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2, 1, 2),
    _MefSoamLmMeasuredStatsBackwardFlr_Type()
)
mefSoamLmMeasuredStatsBackwardFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsBackwardFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsBackwardFlr.setUnits("milli-percent")
_MefSoamLmMeasuredStatsAvailForwardStatus_Type = MefSoamTcAvailabilityType
_MefSoamLmMeasuredStatsAvailForwardStatus_Object = MibTableColumn
mefSoamLmMeasuredStatsAvailForwardStatus = _MefSoamLmMeasuredStatsAvailForwardStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2, 1, 3),
    _MefSoamLmMeasuredStatsAvailForwardStatus_Type()
)
mefSoamLmMeasuredStatsAvailForwardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsAvailForwardStatus.setStatus("current")
_MefSoamLmMeasuredStatsAvailBackwardStatus_Type = MefSoamTcAvailabilityType
_MefSoamLmMeasuredStatsAvailBackwardStatus_Object = MibTableColumn
mefSoamLmMeasuredStatsAvailBackwardStatus = _MefSoamLmMeasuredStatsAvailBackwardStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2, 1, 4),
    _MefSoamLmMeasuredStatsAvailBackwardStatus_Type()
)
mefSoamLmMeasuredStatsAvailBackwardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsAvailBackwardStatus.setStatus("current")
_MefSoamLmMeasuredStatsAvailForwardLastTransitionTime_Type = DateAndTime
_MefSoamLmMeasuredStatsAvailForwardLastTransitionTime_Object = MibTableColumn
mefSoamLmMeasuredStatsAvailForwardLastTransitionTime = _MefSoamLmMeasuredStatsAvailForwardLastTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2, 1, 5),
    _MefSoamLmMeasuredStatsAvailForwardLastTransitionTime_Type()
)
mefSoamLmMeasuredStatsAvailForwardLastTransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsAvailForwardLastTransitionTime.setStatus("current")
_MefSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Type = DateAndTime
_MefSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Object = MibTableColumn
mefSoamLmMeasuredStatsAvailBackwardLastTransitionTime = _MefSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2, 1, 6),
    _MefSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Type()
)
mefSoamLmMeasuredStatsAvailBackwardLastTransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsAvailBackwardLastTransitionTime.setStatus("current")
_MefSoamLmCurrentAvailStatsTable_Object = MibTable
mefSoamLmCurrentAvailStatsTable = _MefSoamLmCurrentAvailStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsTable.setStatus("current")
_MefSoamLmCurrentAvailStatsEntry_Object = MibTableRow
mefSoamLmCurrentAvailStatsEntry = _MefSoamLmCurrentAvailStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1)
)
mefSoamLmCurrentAvailStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsEntry.setStatus("current")
_MefSoamLmCurrentAvailStatsIndex_Type = Unsigned32
_MefSoamLmCurrentAvailStatsIndex_Object = MibTableColumn
mefSoamLmCurrentAvailStatsIndex = _MefSoamLmCurrentAvailStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 1),
    _MefSoamLmCurrentAvailStatsIndex_Type()
)
mefSoamLmCurrentAvailStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsIndex.setStatus("current")
_MefSoamLmCurrentAvailStatsStartTime_Type = DateAndTime
_MefSoamLmCurrentAvailStatsStartTime_Object = MibTableColumn
mefSoamLmCurrentAvailStatsStartTime = _MefSoamLmCurrentAvailStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 2),
    _MefSoamLmCurrentAvailStatsStartTime_Type()
)
mefSoamLmCurrentAvailStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsStartTime.setStatus("current")
_MefSoamLmCurrentAvailStatsElapsedTime_Type = TimeInterval
_MefSoamLmCurrentAvailStatsElapsedTime_Object = MibTableColumn
mefSoamLmCurrentAvailStatsElapsedTime = _MefSoamLmCurrentAvailStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 3),
    _MefSoamLmCurrentAvailStatsElapsedTime_Type()
)
mefSoamLmCurrentAvailStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsElapsedTime.setStatus("current")
_MefSoamLmCurrentAvailStatsSuspect_Type = TruthValue
_MefSoamLmCurrentAvailStatsSuspect_Object = MibTableColumn
mefSoamLmCurrentAvailStatsSuspect = _MefSoamLmCurrentAvailStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 4),
    _MefSoamLmCurrentAvailStatsSuspect_Type()
)
mefSoamLmCurrentAvailStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsSuspect.setStatus("current")
_MefSoamLmCurrentAvailStatsForwardHighLoss_Type = Unsigned32
_MefSoamLmCurrentAvailStatsForwardHighLoss_Object = MibTableColumn
mefSoamLmCurrentAvailStatsForwardHighLoss = _MefSoamLmCurrentAvailStatsForwardHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 5),
    _MefSoamLmCurrentAvailStatsForwardHighLoss_Type()
)
mefSoamLmCurrentAvailStatsForwardHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardHighLoss.setStatus("current")
_MefSoamLmCurrentAvailStatsBackwardHighLoss_Type = Unsigned32
_MefSoamLmCurrentAvailStatsBackwardHighLoss_Object = MibTableColumn
mefSoamLmCurrentAvailStatsBackwardHighLoss = _MefSoamLmCurrentAvailStatsBackwardHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 6),
    _MefSoamLmCurrentAvailStatsBackwardHighLoss_Type()
)
mefSoamLmCurrentAvailStatsBackwardHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardHighLoss.setStatus("current")
_MefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Type = Unsigned32
_MefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Object = MibTableColumn
mefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss = _MefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 7),
    _MefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Type()
)
mefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss.setStatus("current")
_MefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Type = Unsigned32
_MefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Object = MibTableColumn
mefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss = _MefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 8),
    _MefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Type()
)
mefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss.setStatus("current")
_MefSoamLmCurrentAvailStatsForwardAvailable_Type = Gauge32
_MefSoamLmCurrentAvailStatsForwardAvailable_Object = MibTableColumn
mefSoamLmCurrentAvailStatsForwardAvailable = _MefSoamLmCurrentAvailStatsForwardAvailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 9),
    _MefSoamLmCurrentAvailStatsForwardAvailable_Type()
)
mefSoamLmCurrentAvailStatsForwardAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardAvailable.setStatus("current")
_MefSoamLmCurrentAvailStatsBackwardAvailable_Type = Gauge32
_MefSoamLmCurrentAvailStatsBackwardAvailable_Object = MibTableColumn
mefSoamLmCurrentAvailStatsBackwardAvailable = _MefSoamLmCurrentAvailStatsBackwardAvailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 10),
    _MefSoamLmCurrentAvailStatsBackwardAvailable_Type()
)
mefSoamLmCurrentAvailStatsBackwardAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardAvailable.setStatus("current")
_MefSoamLmCurrentAvailStatsForwardUnavailable_Type = Gauge32
_MefSoamLmCurrentAvailStatsForwardUnavailable_Object = MibTableColumn
mefSoamLmCurrentAvailStatsForwardUnavailable = _MefSoamLmCurrentAvailStatsForwardUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 11),
    _MefSoamLmCurrentAvailStatsForwardUnavailable_Type()
)
mefSoamLmCurrentAvailStatsForwardUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardUnavailable.setStatus("current")
_MefSoamLmCurrentAvailStatsBackwardUnavailable_Type = Gauge32
_MefSoamLmCurrentAvailStatsBackwardUnavailable_Object = MibTableColumn
mefSoamLmCurrentAvailStatsBackwardUnavailable = _MefSoamLmCurrentAvailStatsBackwardUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 12),
    _MefSoamLmCurrentAvailStatsBackwardUnavailable_Type()
)
mefSoamLmCurrentAvailStatsBackwardUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardUnavailable.setStatus("current")


class _MefSoamLmCurrentAvailStatsForwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentAvailStatsForwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentAvailStatsForwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentAvailStatsForwardMinFlr_Object = MibTableColumn
mefSoamLmCurrentAvailStatsForwardMinFlr = _MefSoamLmCurrentAvailStatsForwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 13),
    _MefSoamLmCurrentAvailStatsForwardMinFlr_Type()
)
mefSoamLmCurrentAvailStatsForwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardMinFlr.setUnits("milli-percent")


class _MefSoamLmCurrentAvailStatsForwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentAvailStatsForwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentAvailStatsForwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentAvailStatsForwardMaxFlr_Object = MibTableColumn
mefSoamLmCurrentAvailStatsForwardMaxFlr = _MefSoamLmCurrentAvailStatsForwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 14),
    _MefSoamLmCurrentAvailStatsForwardMaxFlr_Type()
)
mefSoamLmCurrentAvailStatsForwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmCurrentAvailStatsForwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentAvailStatsForwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentAvailStatsForwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentAvailStatsForwardAvgFlr_Object = MibTableColumn
mefSoamLmCurrentAvailStatsForwardAvgFlr = _MefSoamLmCurrentAvailStatsForwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 15),
    _MefSoamLmCurrentAvailStatsForwardAvgFlr_Type()
)
mefSoamLmCurrentAvailStatsForwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardAvgFlr.setUnits("milli-percent")


class _MefSoamLmCurrentAvailStatsBackwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentAvailStatsBackwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentAvailStatsBackwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentAvailStatsBackwardMinFlr_Object = MibTableColumn
mefSoamLmCurrentAvailStatsBackwardMinFlr = _MefSoamLmCurrentAvailStatsBackwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 16),
    _MefSoamLmCurrentAvailStatsBackwardMinFlr_Type()
)
mefSoamLmCurrentAvailStatsBackwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardMinFlr.setUnits("milli-percent")


class _MefSoamLmCurrentAvailStatsBackwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentAvailStatsBackwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentAvailStatsBackwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentAvailStatsBackwardMaxFlr_Object = MibTableColumn
mefSoamLmCurrentAvailStatsBackwardMaxFlr = _MefSoamLmCurrentAvailStatsBackwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 17),
    _MefSoamLmCurrentAvailStatsBackwardMaxFlr_Type()
)
mefSoamLmCurrentAvailStatsBackwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmCurrentAvailStatsBackwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentAvailStatsBackwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentAvailStatsBackwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentAvailStatsBackwardAvgFlr_Object = MibTableColumn
mefSoamLmCurrentAvailStatsBackwardAvgFlr = _MefSoamLmCurrentAvailStatsBackwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 18),
    _MefSoamLmCurrentAvailStatsBackwardAvgFlr_Type()
)
mefSoamLmCurrentAvailStatsBackwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardAvgFlr.setUnits("milli-percent")
_MefSoamLmCurrentStatsTable_Object = MibTable
mefSoamLmCurrentStatsTable = _MefSoamLmCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsTable.setStatus("current")
_MefSoamLmCurrentStatsEntry_Object = MibTableRow
mefSoamLmCurrentStatsEntry = _MefSoamLmCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1)
)
mefSoamLmCurrentStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsEntry.setStatus("current")
_MefSoamLmCurrentStatsIndex_Type = Unsigned32
_MefSoamLmCurrentStatsIndex_Object = MibTableColumn
mefSoamLmCurrentStatsIndex = _MefSoamLmCurrentStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 1),
    _MefSoamLmCurrentStatsIndex_Type()
)
mefSoamLmCurrentStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsIndex.setStatus("current")
_MefSoamLmCurrentStatsStartTime_Type = DateAndTime
_MefSoamLmCurrentStatsStartTime_Object = MibTableColumn
mefSoamLmCurrentStatsStartTime = _MefSoamLmCurrentStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 2),
    _MefSoamLmCurrentStatsStartTime_Type()
)
mefSoamLmCurrentStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsStartTime.setStatus("current")
_MefSoamLmCurrentStatsElapsedTime_Type = TimeInterval
_MefSoamLmCurrentStatsElapsedTime_Object = MibTableColumn
mefSoamLmCurrentStatsElapsedTime = _MefSoamLmCurrentStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 3),
    _MefSoamLmCurrentStatsElapsedTime_Type()
)
mefSoamLmCurrentStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsElapsedTime.setStatus("current")
_MefSoamLmCurrentStatsSuspect_Type = TruthValue
_MefSoamLmCurrentStatsSuspect_Object = MibTableColumn
mefSoamLmCurrentStatsSuspect = _MefSoamLmCurrentStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 4),
    _MefSoamLmCurrentStatsSuspect_Type()
)
mefSoamLmCurrentStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsSuspect.setStatus("current")
_MefSoamLmCurrentStatsForwardTransmittedFrames_Type = Gauge32
_MefSoamLmCurrentStatsForwardTransmittedFrames_Object = MibTableColumn
mefSoamLmCurrentStatsForwardTransmittedFrames = _MefSoamLmCurrentStatsForwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 5),
    _MefSoamLmCurrentStatsForwardTransmittedFrames_Type()
)
mefSoamLmCurrentStatsForwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardTransmittedFrames.setStatus("current")
_MefSoamLmCurrentStatsForwardReceivedFrames_Type = Gauge32
_MefSoamLmCurrentStatsForwardReceivedFrames_Object = MibTableColumn
mefSoamLmCurrentStatsForwardReceivedFrames = _MefSoamLmCurrentStatsForwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 6),
    _MefSoamLmCurrentStatsForwardReceivedFrames_Type()
)
mefSoamLmCurrentStatsForwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardReceivedFrames.setStatus("current")


class _MefSoamLmCurrentStatsForwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentStatsForwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentStatsForwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentStatsForwardMinFlr_Object = MibTableColumn
mefSoamLmCurrentStatsForwardMinFlr = _MefSoamLmCurrentStatsForwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 7),
    _MefSoamLmCurrentStatsForwardMinFlr_Type()
)
mefSoamLmCurrentStatsForwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardMinFlr.setUnits("milli-percent")


class _MefSoamLmCurrentStatsForwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentStatsForwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentStatsForwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentStatsForwardMaxFlr_Object = MibTableColumn
mefSoamLmCurrentStatsForwardMaxFlr = _MefSoamLmCurrentStatsForwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 8),
    _MefSoamLmCurrentStatsForwardMaxFlr_Type()
)
mefSoamLmCurrentStatsForwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmCurrentStatsForwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentStatsForwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentStatsForwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentStatsForwardAvgFlr_Object = MibTableColumn
mefSoamLmCurrentStatsForwardAvgFlr = _MefSoamLmCurrentStatsForwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 9),
    _MefSoamLmCurrentStatsForwardAvgFlr_Type()
)
mefSoamLmCurrentStatsForwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardAvgFlr.setUnits("milli-percent")
_MefSoamLmCurrentStatsBackwardTransmittedFrames_Type = Gauge32
_MefSoamLmCurrentStatsBackwardTransmittedFrames_Object = MibTableColumn
mefSoamLmCurrentStatsBackwardTransmittedFrames = _MefSoamLmCurrentStatsBackwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 10),
    _MefSoamLmCurrentStatsBackwardTransmittedFrames_Type()
)
mefSoamLmCurrentStatsBackwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardTransmittedFrames.setStatus("current")
_MefSoamLmCurrentStatsBackwardReceivedFrames_Type = Gauge32
_MefSoamLmCurrentStatsBackwardReceivedFrames_Object = MibTableColumn
mefSoamLmCurrentStatsBackwardReceivedFrames = _MefSoamLmCurrentStatsBackwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 11),
    _MefSoamLmCurrentStatsBackwardReceivedFrames_Type()
)
mefSoamLmCurrentStatsBackwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardReceivedFrames.setStatus("current")


class _MefSoamLmCurrentStatsBackwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentStatsBackwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentStatsBackwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentStatsBackwardMinFlr_Object = MibTableColumn
mefSoamLmCurrentStatsBackwardMinFlr = _MefSoamLmCurrentStatsBackwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 12),
    _MefSoamLmCurrentStatsBackwardMinFlr_Type()
)
mefSoamLmCurrentStatsBackwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardMinFlr.setUnits("milli-percent")


class _MefSoamLmCurrentStatsBackwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentStatsBackwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentStatsBackwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentStatsBackwardMaxFlr_Object = MibTableColumn
mefSoamLmCurrentStatsBackwardMaxFlr = _MefSoamLmCurrentStatsBackwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 13),
    _MefSoamLmCurrentStatsBackwardMaxFlr_Type()
)
mefSoamLmCurrentStatsBackwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmCurrentStatsBackwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentStatsBackwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentStatsBackwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentStatsBackwardAvgFlr_Object = MibTableColumn
mefSoamLmCurrentStatsBackwardAvgFlr = _MefSoamLmCurrentStatsBackwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 14),
    _MefSoamLmCurrentStatsBackwardAvgFlr_Type()
)
mefSoamLmCurrentStatsBackwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardAvgFlr.setUnits("milli-percent")
_MefSoamLmCurrentStatsSoamPdusSent_Type = Gauge32
_MefSoamLmCurrentStatsSoamPdusSent_Object = MibTableColumn
mefSoamLmCurrentStatsSoamPdusSent = _MefSoamLmCurrentStatsSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 15),
    _MefSoamLmCurrentStatsSoamPdusSent_Type()
)
mefSoamLmCurrentStatsSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsSoamPdusSent.setStatus("current")
_MefSoamLmCurrentStatsSoamPdusReceived_Type = Gauge32
_MefSoamLmCurrentStatsSoamPdusReceived_Object = MibTableColumn
mefSoamLmCurrentStatsSoamPdusReceived = _MefSoamLmCurrentStatsSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 16),
    _MefSoamLmCurrentStatsSoamPdusReceived_Type()
)
mefSoamLmCurrentStatsSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsSoamPdusReceived.setStatus("current")
_MefSoamLmHistoryAvailStatsTable_Object = MibTable
mefSoamLmHistoryAvailStatsTable = _MefSoamLmHistoryAvailStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5)
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsTable.setStatus("current")
_MefSoamLmHistoryAvailStatsEntry_Object = MibTableRow
mefSoamLmHistoryAvailStatsEntry = _MefSoamLmHistoryAvailStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1)
)
mefSoamLmHistoryAvailStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsIndex"),
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsEntry.setStatus("current")
_MefSoamLmHistoryAvailStatsIndex_Type = Unsigned32
_MefSoamLmHistoryAvailStatsIndex_Object = MibTableColumn
mefSoamLmHistoryAvailStatsIndex = _MefSoamLmHistoryAvailStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 1),
    _MefSoamLmHistoryAvailStatsIndex_Type()
)
mefSoamLmHistoryAvailStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsIndex.setStatus("current")
_MefSoamLmHistoryAvailStatsEndTime_Type = DateAndTime
_MefSoamLmHistoryAvailStatsEndTime_Object = MibTableColumn
mefSoamLmHistoryAvailStatsEndTime = _MefSoamLmHistoryAvailStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 2),
    _MefSoamLmHistoryAvailStatsEndTime_Type()
)
mefSoamLmHistoryAvailStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsEndTime.setStatus("current")
_MefSoamLmHistoryAvailStatsElapsedTime_Type = TimeInterval
_MefSoamLmHistoryAvailStatsElapsedTime_Object = MibTableColumn
mefSoamLmHistoryAvailStatsElapsedTime = _MefSoamLmHistoryAvailStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 3),
    _MefSoamLmHistoryAvailStatsElapsedTime_Type()
)
mefSoamLmHistoryAvailStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsElapsedTime.setStatus("current")
_MefSoamLmHistoryAvailStatsSuspect_Type = TruthValue
_MefSoamLmHistoryAvailStatsSuspect_Object = MibTableColumn
mefSoamLmHistoryAvailStatsSuspect = _MefSoamLmHistoryAvailStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 4),
    _MefSoamLmHistoryAvailStatsSuspect_Type()
)
mefSoamLmHistoryAvailStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsSuspect.setStatus("current")
_MefSoamLmHistoryAvailStatsForwardHighLoss_Type = Unsigned32
_MefSoamLmHistoryAvailStatsForwardHighLoss_Object = MibTableColumn
mefSoamLmHistoryAvailStatsForwardHighLoss = _MefSoamLmHistoryAvailStatsForwardHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 5),
    _MefSoamLmHistoryAvailStatsForwardHighLoss_Type()
)
mefSoamLmHistoryAvailStatsForwardHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardHighLoss.setStatus("current")
_MefSoamLmHistoryAvailStatsBackwardHighLoss_Type = Unsigned32
_MefSoamLmHistoryAvailStatsBackwardHighLoss_Object = MibTableColumn
mefSoamLmHistoryAvailStatsBackwardHighLoss = _MefSoamLmHistoryAvailStatsBackwardHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 6),
    _MefSoamLmHistoryAvailStatsBackwardHighLoss_Type()
)
mefSoamLmHistoryAvailStatsBackwardHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardHighLoss.setStatus("current")
_MefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Type = Unsigned32
_MefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Object = MibTableColumn
mefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss = _MefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 7),
    _MefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Type()
)
mefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss.setStatus("current")
_MefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Type = Unsigned32
_MefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Object = MibTableColumn
mefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss = _MefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 8),
    _MefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Type()
)
mefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss.setStatus("current")
_MefSoamLmHistoryAvailStatsForwardAvailable_Type = Gauge32
_MefSoamLmHistoryAvailStatsForwardAvailable_Object = MibTableColumn
mefSoamLmHistoryAvailStatsForwardAvailable = _MefSoamLmHistoryAvailStatsForwardAvailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 9),
    _MefSoamLmHistoryAvailStatsForwardAvailable_Type()
)
mefSoamLmHistoryAvailStatsForwardAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardAvailable.setStatus("current")
_MefSoamLmHistoryAvailStatsBackwardAvailable_Type = Gauge32
_MefSoamLmHistoryAvailStatsBackwardAvailable_Object = MibTableColumn
mefSoamLmHistoryAvailStatsBackwardAvailable = _MefSoamLmHistoryAvailStatsBackwardAvailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 10),
    _MefSoamLmHistoryAvailStatsBackwardAvailable_Type()
)
mefSoamLmHistoryAvailStatsBackwardAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardAvailable.setStatus("current")
_MefSoamLmHistoryAvailStatsForwardUnavailable_Type = Gauge32
_MefSoamLmHistoryAvailStatsForwardUnavailable_Object = MibTableColumn
mefSoamLmHistoryAvailStatsForwardUnavailable = _MefSoamLmHistoryAvailStatsForwardUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 11),
    _MefSoamLmHistoryAvailStatsForwardUnavailable_Type()
)
mefSoamLmHistoryAvailStatsForwardUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardUnavailable.setStatus("current")
_MefSoamLmHistoryAvailStatsBackwardUnavailable_Type = Gauge32
_MefSoamLmHistoryAvailStatsBackwardUnavailable_Object = MibTableColumn
mefSoamLmHistoryAvailStatsBackwardUnavailable = _MefSoamLmHistoryAvailStatsBackwardUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 12),
    _MefSoamLmHistoryAvailStatsBackwardUnavailable_Type()
)
mefSoamLmHistoryAvailStatsBackwardUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardUnavailable.setStatus("current")


class _MefSoamLmHistoryAvailStatsForwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryAvailStatsForwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryAvailStatsForwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryAvailStatsForwardMinFlr_Object = MibTableColumn
mefSoamLmHistoryAvailStatsForwardMinFlr = _MefSoamLmHistoryAvailStatsForwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 13),
    _MefSoamLmHistoryAvailStatsForwardMinFlr_Type()
)
mefSoamLmHistoryAvailStatsForwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardMinFlr.setUnits("milli-percent")


class _MefSoamLmHistoryAvailStatsForwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryAvailStatsForwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryAvailStatsForwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryAvailStatsForwardMaxFlr_Object = MibTableColumn
mefSoamLmHistoryAvailStatsForwardMaxFlr = _MefSoamLmHistoryAvailStatsForwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 14),
    _MefSoamLmHistoryAvailStatsForwardMaxFlr_Type()
)
mefSoamLmHistoryAvailStatsForwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmHistoryAvailStatsForwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryAvailStatsForwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryAvailStatsForwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryAvailStatsForwardAvgFlr_Object = MibTableColumn
mefSoamLmHistoryAvailStatsForwardAvgFlr = _MefSoamLmHistoryAvailStatsForwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 15),
    _MefSoamLmHistoryAvailStatsForwardAvgFlr_Type()
)
mefSoamLmHistoryAvailStatsForwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardAvgFlr.setUnits("milli-percent")


class _MefSoamLmHistoryAvailStatsBackwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryAvailStatsBackwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryAvailStatsBackwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryAvailStatsBackwardMinFlr_Object = MibTableColumn
mefSoamLmHistoryAvailStatsBackwardMinFlr = _MefSoamLmHistoryAvailStatsBackwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 16),
    _MefSoamLmHistoryAvailStatsBackwardMinFlr_Type()
)
mefSoamLmHistoryAvailStatsBackwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardMinFlr.setUnits("milli-percent")


class _MefSoamLmHistoryAvailStatsBackwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryAvailStatsBackwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryAvailStatsBackwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryAvailStatsBackwardMaxFlr_Object = MibTableColumn
mefSoamLmHistoryAvailStatsBackwardMaxFlr = _MefSoamLmHistoryAvailStatsBackwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 17),
    _MefSoamLmHistoryAvailStatsBackwardMaxFlr_Type()
)
mefSoamLmHistoryAvailStatsBackwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmHistoryAvailStatsBackwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryAvailStatsBackwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryAvailStatsBackwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryAvailStatsBackwardAvgFlr_Object = MibTableColumn
mefSoamLmHistoryAvailStatsBackwardAvgFlr = _MefSoamLmHistoryAvailStatsBackwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 18),
    _MefSoamLmHistoryAvailStatsBackwardAvgFlr_Type()
)
mefSoamLmHistoryAvailStatsBackwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardAvgFlr.setUnits("milli-percent")
_MefSoamLmHistoryStatsTable_Object = MibTable
mefSoamLmHistoryStatsTable = _MefSoamLmHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsTable.setStatus("current")
_MefSoamLmHistoryStatsEntry_Object = MibTableRow
mefSoamLmHistoryStatsEntry = _MefSoamLmHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1)
)
mefSoamLmHistoryStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsIndex"),
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsEntry.setStatus("current")
_MefSoamLmHistoryStatsIndex_Type = Unsigned32
_MefSoamLmHistoryStatsIndex_Object = MibTableColumn
mefSoamLmHistoryStatsIndex = _MefSoamLmHistoryStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 1),
    _MefSoamLmHistoryStatsIndex_Type()
)
mefSoamLmHistoryStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsIndex.setStatus("current")
_MefSoamLmHistoryStatsEndTime_Type = DateAndTime
_MefSoamLmHistoryStatsEndTime_Object = MibTableColumn
mefSoamLmHistoryStatsEndTime = _MefSoamLmHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 2),
    _MefSoamLmHistoryStatsEndTime_Type()
)
mefSoamLmHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsEndTime.setStatus("current")
_MefSoamLmHistoryStatsElapsedTime_Type = TimeInterval
_MefSoamLmHistoryStatsElapsedTime_Object = MibTableColumn
mefSoamLmHistoryStatsElapsedTime = _MefSoamLmHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 3),
    _MefSoamLmHistoryStatsElapsedTime_Type()
)
mefSoamLmHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsElapsedTime.setStatus("current")
_MefSoamLmHistoryStatsSuspect_Type = TruthValue
_MefSoamLmHistoryStatsSuspect_Object = MibTableColumn
mefSoamLmHistoryStatsSuspect = _MefSoamLmHistoryStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 4),
    _MefSoamLmHistoryStatsSuspect_Type()
)
mefSoamLmHistoryStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsSuspect.setStatus("current")
_MefSoamLmHistoryStatsForwardTransmittedFrames_Type = Gauge32
_MefSoamLmHistoryStatsForwardTransmittedFrames_Object = MibTableColumn
mefSoamLmHistoryStatsForwardTransmittedFrames = _MefSoamLmHistoryStatsForwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 5),
    _MefSoamLmHistoryStatsForwardTransmittedFrames_Type()
)
mefSoamLmHistoryStatsForwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardTransmittedFrames.setStatus("current")
_MefSoamLmHistoryStatsForwardReceivedFrames_Type = Gauge32
_MefSoamLmHistoryStatsForwardReceivedFrames_Object = MibTableColumn
mefSoamLmHistoryStatsForwardReceivedFrames = _MefSoamLmHistoryStatsForwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 6),
    _MefSoamLmHistoryStatsForwardReceivedFrames_Type()
)
mefSoamLmHistoryStatsForwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardReceivedFrames.setStatus("current")


class _MefSoamLmHistoryStatsForwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryStatsForwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryStatsForwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryStatsForwardMinFlr_Object = MibTableColumn
mefSoamLmHistoryStatsForwardMinFlr = _MefSoamLmHistoryStatsForwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 7),
    _MefSoamLmHistoryStatsForwardMinFlr_Type()
)
mefSoamLmHistoryStatsForwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardMinFlr.setUnits("milli-percent")


class _MefSoamLmHistoryStatsForwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryStatsForwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryStatsForwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryStatsForwardMaxFlr_Object = MibTableColumn
mefSoamLmHistoryStatsForwardMaxFlr = _MefSoamLmHistoryStatsForwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 8),
    _MefSoamLmHistoryStatsForwardMaxFlr_Type()
)
mefSoamLmHistoryStatsForwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmHistoryStatsForwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryStatsForwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryStatsForwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryStatsForwardAvgFlr_Object = MibTableColumn
mefSoamLmHistoryStatsForwardAvgFlr = _MefSoamLmHistoryStatsForwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 9),
    _MefSoamLmHistoryStatsForwardAvgFlr_Type()
)
mefSoamLmHistoryStatsForwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardAvgFlr.setUnits("milli-percent")
_MefSoamLmHistoryStatsBackwardTransmittedFrames_Type = Gauge32
_MefSoamLmHistoryStatsBackwardTransmittedFrames_Object = MibTableColumn
mefSoamLmHistoryStatsBackwardTransmittedFrames = _MefSoamLmHistoryStatsBackwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 10),
    _MefSoamLmHistoryStatsBackwardTransmittedFrames_Type()
)
mefSoamLmHistoryStatsBackwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardTransmittedFrames.setStatus("current")
_MefSoamLmHistoryStatsBackwardReceivedFrames_Type = Gauge32
_MefSoamLmHistoryStatsBackwardReceivedFrames_Object = MibTableColumn
mefSoamLmHistoryStatsBackwardReceivedFrames = _MefSoamLmHistoryStatsBackwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 11),
    _MefSoamLmHistoryStatsBackwardReceivedFrames_Type()
)
mefSoamLmHistoryStatsBackwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardReceivedFrames.setStatus("current")


class _MefSoamLmHistoryStatsBackwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryStatsBackwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryStatsBackwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryStatsBackwardMinFlr_Object = MibTableColumn
mefSoamLmHistoryStatsBackwardMinFlr = _MefSoamLmHistoryStatsBackwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 12),
    _MefSoamLmHistoryStatsBackwardMinFlr_Type()
)
mefSoamLmHistoryStatsBackwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardMinFlr.setUnits("milli-percent")


class _MefSoamLmHistoryStatsBackwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryStatsBackwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryStatsBackwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryStatsBackwardMaxFlr_Object = MibTableColumn
mefSoamLmHistoryStatsBackwardMaxFlr = _MefSoamLmHistoryStatsBackwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 13),
    _MefSoamLmHistoryStatsBackwardMaxFlr_Type()
)
mefSoamLmHistoryStatsBackwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmHistoryStatsBackwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryStatsBackwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryStatsBackwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryStatsBackwardAvgFlr_Object = MibTableColumn
mefSoamLmHistoryStatsBackwardAvgFlr = _MefSoamLmHistoryStatsBackwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 14),
    _MefSoamLmHistoryStatsBackwardAvgFlr_Type()
)
mefSoamLmHistoryStatsBackwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardAvgFlr.setUnits("milli-percent")
_MefSoamLmHistoryStatsSoamPdusSent_Type = Gauge32
_MefSoamLmHistoryStatsSoamPdusSent_Object = MibTableColumn
mefSoamLmHistoryStatsSoamPdusSent = _MefSoamLmHistoryStatsSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 15),
    _MefSoamLmHistoryStatsSoamPdusSent_Type()
)
mefSoamLmHistoryStatsSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsSoamPdusSent.setStatus("current")
_MefSoamLmHistoryStatsSoamPdusReceived_Type = Gauge32
_MefSoamLmHistoryStatsSoamPdusReceived_Object = MibTableColumn
mefSoamLmHistoryStatsSoamPdusReceived = _MefSoamLmHistoryStatsSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 16),
    _MefSoamLmHistoryStatsSoamPdusReceived_Type()
)
mefSoamLmHistoryStatsSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsSoamPdusReceived.setStatus("current")
_MefSoamLmThresholdCfgTable_Object = MibTable
mefSoamLmThresholdCfgTable = _MefSoamLmThresholdCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7)
)
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgTable.setStatus("current")
_MefSoamLmThresholdCfgEntry_Object = MibTableRow
mefSoamLmThresholdCfgEntry = _MefSoamLmThresholdCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1)
)
mefSoamLmThresholdCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgEntry.setStatus("current")


class _MefSoamLmThresholdCfgIndex_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MefSoamLmThresholdCfgIndex_Type.__name__ = "Unsigned32"
_MefSoamLmThresholdCfgIndex_Object = MibTableColumn
mefSoamLmThresholdCfgIndex = _MefSoamLmThresholdCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 1),
    _MefSoamLmThresholdCfgIndex_Type()
)
mefSoamLmThresholdCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgIndex.setStatus("current")


class _MefSoamLmThresholdCfgEnable_Type(Bits):
    """Custom type mefSoamLmThresholdCfgEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bMefSoamLmAvailRatioBackwardThreshold", 13),
          ("bMefSoamLmAvailRatioForwardThreshold", 11),
          ("bMefSoamLmAvgFlrBackwardThreshold", 5),
          ("bMefSoamLmAvgFlrForwardThreshold", 2),
          ("bMefSoamLmBackwardConsecutiveHighLossThreshold", 9),
          ("bMefSoamLmBackwardHighLossThreshold", 8),
          ("bMefSoamLmForwardConsecutiveHighLossThreshold", 7),
          ("bMefSoamLmForwardHighLossThreshold", 6),
          ("bMefSoamLmMaxFlrBackwardThreshold", 4),
          ("bMefSoamLmMaxFlrForwardThreshold", 1),
          ("bMefSoamLmMeasuredFlrBackwardThreshold", 3),
          ("bMefSoamLmMeasuredFlrForwardThreshold", 0),
          ("bMefSoamLmUnavailBackwardThreshold", 12),
          ("bMefSoamLmUnavailForwardThreshold", 10))
    )

_MefSoamLmThresholdCfgEnable_Type.__name__ = "Bits"
_MefSoamLmThresholdCfgEnable_Object = MibTableColumn
mefSoamLmThresholdCfgEnable = _MefSoamLmThresholdCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 2),
    _MefSoamLmThresholdCfgEnable_Type()
)
mefSoamLmThresholdCfgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgEnable.setStatus("current")


class _MefSoamLmThresholdCfgMeasuredFlrForwardThreshold_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgMeasuredFlrForwardThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmThresholdCfgMeasuredFlrForwardThreshold_Type.__name__ = "Unsigned32"
_MefSoamLmThresholdCfgMeasuredFlrForwardThreshold_Object = MibTableColumn
mefSoamLmThresholdCfgMeasuredFlrForwardThreshold = _MefSoamLmThresholdCfgMeasuredFlrForwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 3),
    _MefSoamLmThresholdCfgMeasuredFlrForwardThreshold_Type()
)
mefSoamLmThresholdCfgMeasuredFlrForwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgMeasuredFlrForwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgMeasuredFlrForwardThreshold.setUnits("milli-percent")


class _MefSoamLmThresholdCfgMaxFlrForwardThreshold_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgMaxFlrForwardThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmThresholdCfgMaxFlrForwardThreshold_Type.__name__ = "Unsigned32"
_MefSoamLmThresholdCfgMaxFlrForwardThreshold_Object = MibTableColumn
mefSoamLmThresholdCfgMaxFlrForwardThreshold = _MefSoamLmThresholdCfgMaxFlrForwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 4),
    _MefSoamLmThresholdCfgMaxFlrForwardThreshold_Type()
)
mefSoamLmThresholdCfgMaxFlrForwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgMaxFlrForwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgMaxFlrForwardThreshold.setUnits("milli-percent")


class _MefSoamLmThresholdCfgAvgFlrForwardThreshold_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgAvgFlrForwardThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmThresholdCfgAvgFlrForwardThreshold_Type.__name__ = "Unsigned32"
_MefSoamLmThresholdCfgAvgFlrForwardThreshold_Object = MibTableColumn
mefSoamLmThresholdCfgAvgFlrForwardThreshold = _MefSoamLmThresholdCfgAvgFlrForwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 5),
    _MefSoamLmThresholdCfgAvgFlrForwardThreshold_Type()
)
mefSoamLmThresholdCfgAvgFlrForwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgAvgFlrForwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgAvgFlrForwardThreshold.setUnits("milli-percent")


class _MefSoamLmThresholdCfgMeasuredFlrBackwardThreshold_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgMeasuredFlrBackwardThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmThresholdCfgMeasuredFlrBackwardThreshold_Type.__name__ = "Unsigned32"
_MefSoamLmThresholdCfgMeasuredFlrBackwardThreshold_Object = MibTableColumn
mefSoamLmThresholdCfgMeasuredFlrBackwardThreshold = _MefSoamLmThresholdCfgMeasuredFlrBackwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 6),
    _MefSoamLmThresholdCfgMeasuredFlrBackwardThreshold_Type()
)
mefSoamLmThresholdCfgMeasuredFlrBackwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgMeasuredFlrBackwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgMeasuredFlrBackwardThreshold.setUnits("milli-percent")


class _MefSoamLmThresholdCfgMaxFlrBackwardThreshold_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgMaxFlrBackwardThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmThresholdCfgMaxFlrBackwardThreshold_Type.__name__ = "Unsigned32"
_MefSoamLmThresholdCfgMaxFlrBackwardThreshold_Object = MibTableColumn
mefSoamLmThresholdCfgMaxFlrBackwardThreshold = _MefSoamLmThresholdCfgMaxFlrBackwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 7),
    _MefSoamLmThresholdCfgMaxFlrBackwardThreshold_Type()
)
mefSoamLmThresholdCfgMaxFlrBackwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgMaxFlrBackwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgMaxFlrBackwardThreshold.setUnits("milli-percent")


class _MefSoamLmThresholdCfgAvgFlrBackwardThreshold_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgAvgFlrBackwardThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmThresholdCfgAvgFlrBackwardThreshold_Type.__name__ = "Unsigned32"
_MefSoamLmThresholdCfgAvgFlrBackwardThreshold_Object = MibTableColumn
mefSoamLmThresholdCfgAvgFlrBackwardThreshold = _MefSoamLmThresholdCfgAvgFlrBackwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 8),
    _MefSoamLmThresholdCfgAvgFlrBackwardThreshold_Type()
)
mefSoamLmThresholdCfgAvgFlrBackwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgAvgFlrBackwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgAvgFlrBackwardThreshold.setUnits("milli-percent")


class _MefSoamLmThresholdCfgForwardHighLossThreshold_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgForwardHighLossThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamLmThresholdCfgForwardHighLossThreshold_Object = MibTableColumn
mefSoamLmThresholdCfgForwardHighLossThreshold = _MefSoamLmThresholdCfgForwardHighLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 9),
    _MefSoamLmThresholdCfgForwardHighLossThreshold_Type()
)
mefSoamLmThresholdCfgForwardHighLossThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgForwardHighLossThreshold.setStatus("current")


class _MefSoamLmThresholdCfgForwardConsecutiveHighLossThreshold_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgForwardConsecutiveHighLossThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamLmThresholdCfgForwardConsecutiveHighLossThreshold_Object = MibTableColumn
mefSoamLmThresholdCfgForwardConsecutiveHighLossThreshold = _MefSoamLmThresholdCfgForwardConsecutiveHighLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 10),
    _MefSoamLmThresholdCfgForwardConsecutiveHighLossThreshold_Type()
)
mefSoamLmThresholdCfgForwardConsecutiveHighLossThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgForwardConsecutiveHighLossThreshold.setStatus("current")


class _MefSoamLmThresholdCfgBackwardHighLossThreshold_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgBackwardHighLossThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamLmThresholdCfgBackwardHighLossThreshold_Object = MibTableColumn
mefSoamLmThresholdCfgBackwardHighLossThreshold = _MefSoamLmThresholdCfgBackwardHighLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 11),
    _MefSoamLmThresholdCfgBackwardHighLossThreshold_Type()
)
mefSoamLmThresholdCfgBackwardHighLossThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgBackwardHighLossThreshold.setStatus("current")


class _MefSoamLmThresholdCfgBackwardConsecutiveHighLossThreshold_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgBackwardConsecutiveHighLossThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamLmThresholdCfgBackwardConsecutiveHighLossThreshold_Object = MibTableColumn
mefSoamLmThresholdCfgBackwardConsecutiveHighLossThreshold = _MefSoamLmThresholdCfgBackwardConsecutiveHighLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 12),
    _MefSoamLmThresholdCfgBackwardConsecutiveHighLossThreshold_Type()
)
mefSoamLmThresholdCfgBackwardConsecutiveHighLossThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgBackwardConsecutiveHighLossThreshold.setStatus("current")


class _MefSoamLmThresholdCfgForwardUnavailCountThreshold_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgForwardUnavailCountThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamLmThresholdCfgForwardUnavailCountThreshold_Object = MibTableColumn
mefSoamLmThresholdCfgForwardUnavailCountThreshold = _MefSoamLmThresholdCfgForwardUnavailCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 13),
    _MefSoamLmThresholdCfgForwardUnavailCountThreshold_Type()
)
mefSoamLmThresholdCfgForwardUnavailCountThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgForwardUnavailCountThreshold.setStatus("current")


class _MefSoamLmThresholdCfgForwardAvailRatioThreshold_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgForwardAvailRatioThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmThresholdCfgForwardAvailRatioThreshold_Type.__name__ = "Unsigned32"
_MefSoamLmThresholdCfgForwardAvailRatioThreshold_Object = MibTableColumn
mefSoamLmThresholdCfgForwardAvailRatioThreshold = _MefSoamLmThresholdCfgForwardAvailRatioThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 14),
    _MefSoamLmThresholdCfgForwardAvailRatioThreshold_Type()
)
mefSoamLmThresholdCfgForwardAvailRatioThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgForwardAvailRatioThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgForwardAvailRatioThreshold.setUnits("milli-percent")


class _MefSoamLmThresholdCfgBackwardUnavailCountThreshold_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgBackwardUnavailCountThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamLmThresholdCfgBackwardUnavailCountThreshold_Object = MibTableColumn
mefSoamLmThresholdCfgBackwardUnavailCountThreshold = _MefSoamLmThresholdCfgBackwardUnavailCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 15),
    _MefSoamLmThresholdCfgBackwardUnavailCountThreshold_Type()
)
mefSoamLmThresholdCfgBackwardUnavailCountThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgBackwardUnavailCountThreshold.setStatus("current")


class _MefSoamLmThresholdCfgBackwardAvailRatioThreshold_Type(Unsigned32):
    """Custom type mefSoamLmThresholdCfgBackwardAvailRatioThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmThresholdCfgBackwardAvailRatioThreshold_Type.__name__ = "Unsigned32"
_MefSoamLmThresholdCfgBackwardAvailRatioThreshold_Object = MibTableColumn
mefSoamLmThresholdCfgBackwardAvailRatioThreshold = _MefSoamLmThresholdCfgBackwardAvailRatioThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 16),
    _MefSoamLmThresholdCfgBackwardAvailRatioThreshold_Type()
)
mefSoamLmThresholdCfgBackwardAvailRatioThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgBackwardAvailRatioThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgBackwardAvailRatioThreshold.setUnits("milli-percent")
_MefSoamLmThresholdCfgRowStatus_Type = RowStatus
_MefSoamLmThresholdCfgRowStatus_Object = MibTableColumn
mefSoamLmThresholdCfgRowStatus = _MefSoamLmThresholdCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 7, 1, 17),
    _MefSoamLmThresholdCfgRowStatus_Type()
)
mefSoamLmThresholdCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmThresholdCfgRowStatus.setStatus("current")
_MefSoamPmDmObjects_ObjectIdentity = ObjectIdentity
mefSoamPmDmObjects = _MefSoamPmDmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3)
)
_MefSoamDmCfgTable_Object = MibTable
mefSoamDmCfgTable = _MefSoamDmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mefSoamDmCfgTable.setStatus("current")
_MefSoamDmCfgEntry_Object = MibTableRow
mefSoamDmCfgEntry = _MefSoamDmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1)
)
mefSoamDmCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamDmCfgEntry.setStatus("current")


class _MefSoamDmCfgIndex_Type(Unsigned32):
    """Custom type mefSoamDmCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MefSoamDmCfgIndex_Type.__name__ = "Unsigned32"
_MefSoamDmCfgIndex_Object = MibTableColumn
mefSoamDmCfgIndex = _MefSoamDmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 1),
    _MefSoamDmCfgIndex_Type()
)
mefSoamDmCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamDmCfgIndex.setStatus("current")


class _MefSoamDmCfgType_Type(Integer32):
    """Custom type mefSoamDmCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dm1DmRx", 3),
          ("dm1DmTx", 2),
          ("dmDmm", 1))
    )


_MefSoamDmCfgType_Type.__name__ = "Integer32"
_MefSoamDmCfgType_Object = MibTableColumn
mefSoamDmCfgType = _MefSoamDmCfgType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 2),
    _MefSoamDmCfgType_Type()
)
mefSoamDmCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgType.setStatus("current")


class _MefSoamDmCfgVersion_Type(Unsigned32):
    """Custom type mefSoamDmCfgVersion based on Unsigned32"""
    defaultValue = 0


_MefSoamDmCfgVersion_Object = MibTableColumn
mefSoamDmCfgVersion = _MefSoamDmCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 3),
    _MefSoamDmCfgVersion_Type()
)
mefSoamDmCfgVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgVersion.setStatus("current")


class _MefSoamDmCfgEnabled_Type(TruthValue):
    """Custom type mefSoamDmCfgEnabled based on TruthValue"""


_MefSoamDmCfgEnabled_Object = MibTableColumn
mefSoamDmCfgEnabled = _MefSoamDmCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 4),
    _MefSoamDmCfgEnabled_Type()
)
mefSoamDmCfgEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgEnabled.setStatus("current")


class _MefSoamDmCfgMeasurementEnable_Type(Bits):
    """Custom type mefSoamDmCfgMeasurementEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bFrameDelayBackwardAvg", 13),
          ("bFrameDelayBackwardBins", 10),
          ("bFrameDelayBackwardMax", 12),
          ("bFrameDelayBackwardMin", 11),
          ("bFrameDelayForwardAvg", 9),
          ("bFrameDelayForwardBins", 6),
          ("bFrameDelayForwardMax", 8),
          ("bFrameDelayForwardMin", 7),
          ("bFrameDelayRangeBackwardAvg", 31),
          ("bFrameDelayRangeBackwardBins", 29),
          ("bFrameDelayRangeBackwardMax", 30),
          ("bFrameDelayRangeForwardAvg", 28),
          ("bFrameDelayRangeForwardBins", 26),
          ("bFrameDelayRangeForwardMax", 27),
          ("bFrameDelayRangeTwoWayAvg", 34),
          ("bFrameDelayRangeTwoWayBins", 32),
          ("bFrameDelayRangeTwoWayMax", 33),
          ("bFrameDelayTwoWayAvg", 5),
          ("bFrameDelayTwoWayBins", 2),
          ("bFrameDelayTwoWayMax", 4),
          ("bFrameDelayTwoWayMin", 3),
          ("bIfdvBackwardAvg", 21),
          ("bIfdvBackwardBins", 18),
          ("bIfdvBackwardMax", 20),
          ("bIfdvBackwardMin", 19),
          ("bIfdvForwardAvg", 17),
          ("bIfdvForwardBins", 14),
          ("bIfdvForwardMax", 16),
          ("bIfdvForwardMin", 15),
          ("bIfdvTwoWayAvg", 25),
          ("bIfdvTwoWayBins", 22),
          ("bIfdvTwoWayMax", 24),
          ("bIfdvTwoWayMin", 23),
          ("bMeasuredStatsFrameDelayBackward", 37),
          ("bMeasuredStatsFrameDelayForward", 36),
          ("bMeasuredStatsFrameDelayTwoWay", 35),
          ("bMeasuredStatsIfdvBackward", 40),
          ("bMeasuredStatsIfdvForward", 39),
          ("bMeasuredStatsIfdvTwoWay", 38),
          ("bSoamPdusReceived", 1),
          ("bSoamPdusSent", 0))
    )

_MefSoamDmCfgMeasurementEnable_Type.__name__ = "Bits"
_MefSoamDmCfgMeasurementEnable_Object = MibTableColumn
mefSoamDmCfgMeasurementEnable = _MefSoamDmCfgMeasurementEnable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 5),
    _MefSoamDmCfgMeasurementEnable_Type()
)
mefSoamDmCfgMeasurementEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasurementEnable.setStatus("current")


class _MefSoamDmCfgMessagePeriod_Type(MefSoamTcMeasurementPeriodType):
    """Custom type mefSoamDmCfgMessagePeriod based on MefSoamTcMeasurementPeriodType"""
    defaultValue = 100


_MefSoamDmCfgMessagePeriod_Object = MibTableColumn
mefSoamDmCfgMessagePeriod = _MefSoamDmCfgMessagePeriod_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 6),
    _MefSoamDmCfgMessagePeriod_Type()
)
mefSoamDmCfgMessagePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgMessagePeriod.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCfgMessagePeriod.setUnits("ms")
_MefSoamDmCfgPriority_Type = IEEE8021PriorityValue
_MefSoamDmCfgPriority_Object = MibTableColumn
mefSoamDmCfgPriority = _MefSoamDmCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 7),
    _MefSoamDmCfgPriority_Type()
)
mefSoamDmCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgPriority.setStatus("current")


class _MefSoamDmCfgFrameSize_Type(Unsigned32):
    """Custom type mefSoamDmCfgFrameSize based on Unsigned32"""
    defaultValue = 64


_MefSoamDmCfgFrameSize_Object = MibTableColumn
mefSoamDmCfgFrameSize = _MefSoamDmCfgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 8),
    _MefSoamDmCfgFrameSize_Type()
)
mefSoamDmCfgFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgFrameSize.setStatus("current")


class _MefSoamDmCfgDataPattern_Type(MefSoamTcDataPatternType):
    """Custom type mefSoamDmCfgDataPattern based on MefSoamTcDataPatternType"""


_MefSoamDmCfgDataPattern_Object = MibTableColumn
mefSoamDmCfgDataPattern = _MefSoamDmCfgDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 9),
    _MefSoamDmCfgDataPattern_Type()
)
mefSoamDmCfgDataPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgDataPattern.setStatus("current")


class _MefSoamDmCfgTestTlvIncluded_Type(TruthValue):
    """Custom type mefSoamDmCfgTestTlvIncluded based on TruthValue"""


_MefSoamDmCfgTestTlvIncluded_Object = MibTableColumn
mefSoamDmCfgTestTlvIncluded = _MefSoamDmCfgTestTlvIncluded_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 10),
    _MefSoamDmCfgTestTlvIncluded_Type()
)
mefSoamDmCfgTestTlvIncluded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgTestTlvIncluded.setStatus("current")


class _MefSoamDmCfgTestTlvPattern_Type(MefSoamTcTestPatternType):
    """Custom type mefSoamDmCfgTestTlvPattern based on MefSoamTcTestPatternType"""


_MefSoamDmCfgTestTlvPattern_Object = MibTableColumn
mefSoamDmCfgTestTlvPattern = _MefSoamDmCfgTestTlvPattern_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 11),
    _MefSoamDmCfgTestTlvPattern_Type()
)
mefSoamDmCfgTestTlvPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgTestTlvPattern.setStatus("current")


class _MefSoamDmCfgMeasurementInterval_Type(Unsigned32):
    """Custom type mefSoamDmCfgMeasurementInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_MefSoamDmCfgMeasurementInterval_Type.__name__ = "Unsigned32"
_MefSoamDmCfgMeasurementInterval_Object = MibTableColumn
mefSoamDmCfgMeasurementInterval = _MefSoamDmCfgMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 12),
    _MefSoamDmCfgMeasurementInterval_Type()
)
mefSoamDmCfgMeasurementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasurementInterval.setUnits("minutes")


class _MefSoamDmCfgNumIntervalsStored_Type(Unsigned32):
    """Custom type mefSoamDmCfgNumIntervalsStored based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1000),
    )


_MefSoamDmCfgNumIntervalsStored_Type.__name__ = "Unsigned32"
_MefSoamDmCfgNumIntervalsStored_Object = MibTableColumn
mefSoamDmCfgNumIntervalsStored = _MefSoamDmCfgNumIntervalsStored_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 13),
    _MefSoamDmCfgNumIntervalsStored_Type()
)
mefSoamDmCfgNumIntervalsStored.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgNumIntervalsStored.setStatus("current")
_MefSoamDmCfgDestMacAddress_Type = MacAddress
_MefSoamDmCfgDestMacAddress_Object = MibTableColumn
mefSoamDmCfgDestMacAddress = _MefSoamDmCfgDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 14),
    _MefSoamDmCfgDestMacAddress_Type()
)
mefSoamDmCfgDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgDestMacAddress.setStatus("current")


class _MefSoamDmCfgDestMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type mefSoamDmCfgDestMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_MefSoamDmCfgDestMepId_Object = MibTableColumn
mefSoamDmCfgDestMepId = _MefSoamDmCfgDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 15),
    _MefSoamDmCfgDestMepId_Type()
)
mefSoamDmCfgDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgDestMepId.setStatus("current")


class _MefSoamDmCfgDestIsMepId_Type(TruthValue):
    """Custom type mefSoamDmCfgDestIsMepId based on TruthValue"""


_MefSoamDmCfgDestIsMepId_Object = MibTableColumn
mefSoamDmCfgDestIsMepId = _MefSoamDmCfgDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 16),
    _MefSoamDmCfgDestIsMepId_Type()
)
mefSoamDmCfgDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgDestIsMepId.setStatus("current")
_MefSoamDmCfgSourceMacAddress_Type = MacAddress
_MefSoamDmCfgSourceMacAddress_Object = MibTableColumn
mefSoamDmCfgSourceMacAddress = _MefSoamDmCfgSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 17),
    _MefSoamDmCfgSourceMacAddress_Type()
)
mefSoamDmCfgSourceMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgSourceMacAddress.setStatus("current")


class _MefSoamDmCfgStartTimeType_Type(MefSoamTcOperationTimeType):
    """Custom type mefSoamDmCfgStartTimeType based on MefSoamTcOperationTimeType"""


_MefSoamDmCfgStartTimeType_Object = MibTableColumn
mefSoamDmCfgStartTimeType = _MefSoamDmCfgStartTimeType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 18),
    _MefSoamDmCfgStartTimeType_Type()
)
mefSoamDmCfgStartTimeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgStartTimeType.setStatus("current")


class _MefSoamDmCfgFixedStartDateAndTime_Type(DateAndTime):
    """Custom type mefSoamDmCfgFixedStartDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_MefSoamDmCfgFixedStartDateAndTime_Object = MibTableColumn
mefSoamDmCfgFixedStartDateAndTime = _MefSoamDmCfgFixedStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 19),
    _MefSoamDmCfgFixedStartDateAndTime_Type()
)
mefSoamDmCfgFixedStartDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgFixedStartDateAndTime.setStatus("current")


class _MefSoamDmCfgRelativeStartTime_Type(TimeInterval):
    """Custom type mefSoamDmCfgRelativeStartTime based on TimeInterval"""
    defaultValue = 0


_MefSoamDmCfgRelativeStartTime_Object = MibTableColumn
mefSoamDmCfgRelativeStartTime = _MefSoamDmCfgRelativeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 20),
    _MefSoamDmCfgRelativeStartTime_Type()
)
mefSoamDmCfgRelativeStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgRelativeStartTime.setStatus("current")


class _MefSoamDmCfgStopTimeType_Type(MefSoamTcOperationTimeType):
    """Custom type mefSoamDmCfgStopTimeType based on MefSoamTcOperationTimeType"""


_MefSoamDmCfgStopTimeType_Object = MibTableColumn
mefSoamDmCfgStopTimeType = _MefSoamDmCfgStopTimeType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 21),
    _MefSoamDmCfgStopTimeType_Type()
)
mefSoamDmCfgStopTimeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgStopTimeType.setStatus("current")


class _MefSoamDmCfgFixedStopDateAndTime_Type(DateAndTime):
    """Custom type mefSoamDmCfgFixedStopDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_MefSoamDmCfgFixedStopDateAndTime_Object = MibTableColumn
mefSoamDmCfgFixedStopDateAndTime = _MefSoamDmCfgFixedStopDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 22),
    _MefSoamDmCfgFixedStopDateAndTime_Type()
)
mefSoamDmCfgFixedStopDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgFixedStopDateAndTime.setStatus("current")


class _MefSoamDmCfgRelativeStopTime_Type(TimeInterval):
    """Custom type mefSoamDmCfgRelativeStopTime based on TimeInterval"""
    defaultValue = 0


_MefSoamDmCfgRelativeStopTime_Object = MibTableColumn
mefSoamDmCfgRelativeStopTime = _MefSoamDmCfgRelativeStopTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 23),
    _MefSoamDmCfgRelativeStopTime_Type()
)
mefSoamDmCfgRelativeStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgRelativeStopTime.setStatus("current")


class _MefSoamDmCfgRepetitionTime_Type(Unsigned32):
    """Custom type mefSoamDmCfgRepetitionTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_MefSoamDmCfgRepetitionTime_Type.__name__ = "Unsigned32"
_MefSoamDmCfgRepetitionTime_Object = MibTableColumn
mefSoamDmCfgRepetitionTime = _MefSoamDmCfgRepetitionTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 24),
    _MefSoamDmCfgRepetitionTime_Type()
)
mefSoamDmCfgRepetitionTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgRepetitionTime.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCfgRepetitionTime.setUnits("seconds")


class _MefSoamDmCfgAlignMeasurementIntervals_Type(TruthValue):
    """Custom type mefSoamDmCfgAlignMeasurementIntervals based on TruthValue"""


_MefSoamDmCfgAlignMeasurementIntervals_Object = MibTableColumn
mefSoamDmCfgAlignMeasurementIntervals = _MefSoamDmCfgAlignMeasurementIntervals_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 25),
    _MefSoamDmCfgAlignMeasurementIntervals_Type()
)
mefSoamDmCfgAlignMeasurementIntervals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgAlignMeasurementIntervals.setStatus("current")


class _MefSoamDmCfgAlignMeasurementOffset_Type(Unsigned32):
    """Custom type mefSoamDmCfgAlignMeasurementOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 525600),
    )


_MefSoamDmCfgAlignMeasurementOffset_Type.__name__ = "Unsigned32"
_MefSoamDmCfgAlignMeasurementOffset_Object = MibTableColumn
mefSoamDmCfgAlignMeasurementOffset = _MefSoamDmCfgAlignMeasurementOffset_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 26),
    _MefSoamDmCfgAlignMeasurementOffset_Type()
)
mefSoamDmCfgAlignMeasurementOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgAlignMeasurementOffset.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCfgAlignMeasurementOffset.setUnits("minutes")


class _MefSoamDmCfgNumMeasBinsPerFrameDelayInterval_Type(Unsigned32):
    """Custom type mefSoamDmCfgNumMeasBinsPerFrameDelayInterval based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_MefSoamDmCfgNumMeasBinsPerFrameDelayInterval_Type.__name__ = "Unsigned32"
_MefSoamDmCfgNumMeasBinsPerFrameDelayInterval_Object = MibTableColumn
mefSoamDmCfgNumMeasBinsPerFrameDelayInterval = _MefSoamDmCfgNumMeasBinsPerFrameDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 27),
    _MefSoamDmCfgNumMeasBinsPerFrameDelayInterval_Type()
)
mefSoamDmCfgNumMeasBinsPerFrameDelayInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgNumMeasBinsPerFrameDelayInterval.setStatus("current")


class _MefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Type(Unsigned32):
    """Custom type mefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_MefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Type.__name__ = "Unsigned32"
_MefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Object = MibTableColumn
mefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval = _MefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 28),
    _MefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Type()
)
mefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval.setStatus("current")


class _MefSoamDmCfgInterFrameDelayVariationSelectionOffset_Type(Unsigned32):
    """Custom type mefSoamDmCfgInterFrameDelayVariationSelectionOffset based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MefSoamDmCfgInterFrameDelayVariationSelectionOffset_Type.__name__ = "Unsigned32"
_MefSoamDmCfgInterFrameDelayVariationSelectionOffset_Object = MibTableColumn
mefSoamDmCfgInterFrameDelayVariationSelectionOffset = _MefSoamDmCfgInterFrameDelayVariationSelectionOffset_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 29),
    _MefSoamDmCfgInterFrameDelayVariationSelectionOffset_Type()
)
mefSoamDmCfgInterFrameDelayVariationSelectionOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgInterFrameDelayVariationSelectionOffset.setStatus("current")


class _MefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Type(Unsigned32):
    """Custom type mefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_MefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Type.__name__ = "Unsigned32"
_MefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Object = MibTableColumn
mefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval = _MefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 30),
    _MefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Type()
)
mefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval.setStatus("current")


class _MefSoamDmCfgSessionType_Type(MefSoamTcSessionType):
    """Custom type mefSoamDmCfgSessionType based on MefSoamTcSessionType"""


_MefSoamDmCfgSessionType_Object = MibTableColumn
mefSoamDmCfgSessionType = _MefSoamDmCfgSessionType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 31),
    _MefSoamDmCfgSessionType_Type()
)
mefSoamDmCfgSessionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgSessionType.setStatus("current")
_MefSoamDmCfgSessionStatus_Type = MefSoamTcStatusType
_MefSoamDmCfgSessionStatus_Object = MibTableColumn
mefSoamDmCfgSessionStatus = _MefSoamDmCfgSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 32),
    _MefSoamDmCfgSessionStatus_Type()
)
mefSoamDmCfgSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCfgSessionStatus.setStatus("current")


class _MefSoamDmCfgHistoryClear_Type(TruthValue):
    """Custom type mefSoamDmCfgHistoryClear based on TruthValue"""


_MefSoamDmCfgHistoryClear_Object = MibTableColumn
mefSoamDmCfgHistoryClear = _MefSoamDmCfgHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 33),
    _MefSoamDmCfgHistoryClear_Type()
)
mefSoamDmCfgHistoryClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgHistoryClear.setStatus("current")
_MefSoamDmCfgRowStatus_Type = RowStatus
_MefSoamDmCfgRowStatus_Object = MibTableColumn
mefSoamDmCfgRowStatus = _MefSoamDmCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 34),
    _MefSoamDmCfgRowStatus_Type()
)
mefSoamDmCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgRowStatus.setStatus("current")
_MefSoamDmCfgMeasBinTable_Object = MibTable
mefSoamDmCfgMeasBinTable = _MefSoamDmCfgMeasBinTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasBinTable.setStatus("current")
_MefSoamDmCfgMeasBinEntry_Object = MibTableRow
mefSoamDmCfgMeasBinEntry = _MefSoamDmCfgMeasBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 2, 1)
)
mefSoamDmCfgMeasBinEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinType"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinNumber"),
)
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasBinEntry.setStatus("current")
_MefSoamDmCfgMeasBinType_Type = MefSoamTcDelayMeasurementBinType
_MefSoamDmCfgMeasBinType_Object = MibTableColumn
mefSoamDmCfgMeasBinType = _MefSoamDmCfgMeasBinType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 2, 1, 1),
    _MefSoamDmCfgMeasBinType_Type()
)
mefSoamDmCfgMeasBinType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasBinType.setStatus("current")
_MefSoamDmCfgMeasBinNumber_Type = Unsigned32
_MefSoamDmCfgMeasBinNumber_Object = MibTableColumn
mefSoamDmCfgMeasBinNumber = _MefSoamDmCfgMeasBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 2, 1, 2),
    _MefSoamDmCfgMeasBinNumber_Type()
)
mefSoamDmCfgMeasBinNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasBinNumber.setStatus("current")
_MefSoamDmCfgMeasBinLowerBound_Type = Unsigned32
_MefSoamDmCfgMeasBinLowerBound_Object = MibTableColumn
mefSoamDmCfgMeasBinLowerBound = _MefSoamDmCfgMeasBinLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 2, 1, 3),
    _MefSoamDmCfgMeasBinLowerBound_Type()
)
mefSoamDmCfgMeasBinLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasBinLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasBinLowerBound.setUnits("microseconds (us)")
_MefSoamDmMeasuredStatsTable_Object = MibTable
mefSoamDmMeasuredStatsTable = _MefSoamDmMeasuredStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsTable.setStatus("current")
_MefSoamDmMeasuredStatsEntry_Object = MibTableRow
mefSoamDmMeasuredStatsEntry = _MefSoamDmMeasuredStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 3, 1)
)
mefSoamDmMeasuredStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsEntry.setStatus("current")
_MefSoamDmMeasuredStatsFrameDelayTwoWay_Type = Unsigned32
_MefSoamDmMeasuredStatsFrameDelayTwoWay_Object = MibTableColumn
mefSoamDmMeasuredStatsFrameDelayTwoWay = _MefSoamDmMeasuredStatsFrameDelayTwoWay_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 3, 1, 1),
    _MefSoamDmMeasuredStatsFrameDelayTwoWay_Type()
)
mefSoamDmMeasuredStatsFrameDelayTwoWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsFrameDelayTwoWay.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsFrameDelayTwoWay.setUnits("microseconds")
_MefSoamDmMeasuredStatsFrameDelayForward_Type = Unsigned32
_MefSoamDmMeasuredStatsFrameDelayForward_Object = MibTableColumn
mefSoamDmMeasuredStatsFrameDelayForward = _MefSoamDmMeasuredStatsFrameDelayForward_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 3, 1, 2),
    _MefSoamDmMeasuredStatsFrameDelayForward_Type()
)
mefSoamDmMeasuredStatsFrameDelayForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsFrameDelayForward.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsFrameDelayForward.setUnits("microseconds")
_MefSoamDmMeasuredStatsFrameDelayBackward_Type = Unsigned32
_MefSoamDmMeasuredStatsFrameDelayBackward_Object = MibTableColumn
mefSoamDmMeasuredStatsFrameDelayBackward = _MefSoamDmMeasuredStatsFrameDelayBackward_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 3, 1, 3),
    _MefSoamDmMeasuredStatsFrameDelayBackward_Type()
)
mefSoamDmMeasuredStatsFrameDelayBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsFrameDelayBackward.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsFrameDelayBackward.setUnits("microseconds")
_MefSoamDmMeasuredStatsIfdvTwoWay_Type = Unsigned32
_MefSoamDmMeasuredStatsIfdvTwoWay_Object = MibTableColumn
mefSoamDmMeasuredStatsIfdvTwoWay = _MefSoamDmMeasuredStatsIfdvTwoWay_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 3, 1, 4),
    _MefSoamDmMeasuredStatsIfdvTwoWay_Type()
)
mefSoamDmMeasuredStatsIfdvTwoWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsIfdvTwoWay.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsIfdvTwoWay.setUnits("microseconds")
_MefSoamDmMeasuredStatsIfdvForward_Type = Unsigned32
_MefSoamDmMeasuredStatsIfdvForward_Object = MibTableColumn
mefSoamDmMeasuredStatsIfdvForward = _MefSoamDmMeasuredStatsIfdvForward_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 3, 1, 5),
    _MefSoamDmMeasuredStatsIfdvForward_Type()
)
mefSoamDmMeasuredStatsIfdvForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsIfdvForward.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsIfdvForward.setUnits("microseconds")
_MefSoamDmMeasuredStatsIfdvBackward_Type = Unsigned32
_MefSoamDmMeasuredStatsIfdvBackward_Object = MibTableColumn
mefSoamDmMeasuredStatsIfdvBackward = _MefSoamDmMeasuredStatsIfdvBackward_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 3, 1, 6),
    _MefSoamDmMeasuredStatsIfdvBackward_Type()
)
mefSoamDmMeasuredStatsIfdvBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsIfdvBackward.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsIfdvBackward.setUnits("microseconds")
_MefSoamDmCurrentStatsTable_Object = MibTable
mefSoamDmCurrentStatsTable = _MefSoamDmCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsTable.setStatus("current")
_MefSoamDmCurrentStatsEntry_Object = MibTableRow
mefSoamDmCurrentStatsEntry = _MefSoamDmCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1)
)
mefSoamDmCurrentStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsEntry.setStatus("current")
_MefSoamDmCurrentStatsIndex_Type = Unsigned32
_MefSoamDmCurrentStatsIndex_Object = MibTableColumn
mefSoamDmCurrentStatsIndex = _MefSoamDmCurrentStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 1),
    _MefSoamDmCurrentStatsIndex_Type()
)
mefSoamDmCurrentStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIndex.setStatus("current")
_MefSoamDmCurrentStatsStartTime_Type = DateAndTime
_MefSoamDmCurrentStatsStartTime_Object = MibTableColumn
mefSoamDmCurrentStatsStartTime = _MefSoamDmCurrentStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 2),
    _MefSoamDmCurrentStatsStartTime_Type()
)
mefSoamDmCurrentStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsStartTime.setStatus("current")
_MefSoamDmCurrentStatsElapsedTime_Type = TimeInterval
_MefSoamDmCurrentStatsElapsedTime_Object = MibTableColumn
mefSoamDmCurrentStatsElapsedTime = _MefSoamDmCurrentStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 3),
    _MefSoamDmCurrentStatsElapsedTime_Type()
)
mefSoamDmCurrentStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsElapsedTime.setStatus("current")
_MefSoamDmCurrentStatsSuspect_Type = TruthValue
_MefSoamDmCurrentStatsSuspect_Object = MibTableColumn
mefSoamDmCurrentStatsSuspect = _MefSoamDmCurrentStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 4),
    _MefSoamDmCurrentStatsSuspect_Type()
)
mefSoamDmCurrentStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsSuspect.setStatus("current")
_MefSoamDmCurrentStatsFrameDelayTwoWayMin_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayTwoWayMin_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayTwoWayMin = _MefSoamDmCurrentStatsFrameDelayTwoWayMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 5),
    _MefSoamDmCurrentStatsFrameDelayTwoWayMin_Type()
)
mefSoamDmCurrentStatsFrameDelayTwoWayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayTwoWayMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayTwoWayMin.setUnits("microseconds")
_MefSoamDmCurrentStatsFrameDelayTwoWayMax_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayTwoWayMax_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayTwoWayMax = _MefSoamDmCurrentStatsFrameDelayTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 6),
    _MefSoamDmCurrentStatsFrameDelayTwoWayMax_Type()
)
mefSoamDmCurrentStatsFrameDelayTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayTwoWayMax.setUnits("microseconds")
_MefSoamDmCurrentStatsFrameDelayTwoWayAvg_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayTwoWayAvg_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayTwoWayAvg = _MefSoamDmCurrentStatsFrameDelayTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 7),
    _MefSoamDmCurrentStatsFrameDelayTwoWayAvg_Type()
)
mefSoamDmCurrentStatsFrameDelayTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayTwoWayAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsFrameDelayForwardMin_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayForwardMin_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayForwardMin = _MefSoamDmCurrentStatsFrameDelayForwardMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 8),
    _MefSoamDmCurrentStatsFrameDelayForwardMin_Type()
)
mefSoamDmCurrentStatsFrameDelayForwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayForwardMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayForwardMin.setUnits("microseconds")
_MefSoamDmCurrentStatsFrameDelayForwardMax_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayForwardMax_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayForwardMax = _MefSoamDmCurrentStatsFrameDelayForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 9),
    _MefSoamDmCurrentStatsFrameDelayForwardMax_Type()
)
mefSoamDmCurrentStatsFrameDelayForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayForwardMax.setUnits("microseconds")
_MefSoamDmCurrentStatsFrameDelayForwardAvg_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayForwardAvg_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayForwardAvg = _MefSoamDmCurrentStatsFrameDelayForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 10),
    _MefSoamDmCurrentStatsFrameDelayForwardAvg_Type()
)
mefSoamDmCurrentStatsFrameDelayForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayForwardAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsFrameDelayBackwardMin_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayBackwardMin_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayBackwardMin = _MefSoamDmCurrentStatsFrameDelayBackwardMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 11),
    _MefSoamDmCurrentStatsFrameDelayBackwardMin_Type()
)
mefSoamDmCurrentStatsFrameDelayBackwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayBackwardMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayBackwardMin.setUnits("microseconds")
_MefSoamDmCurrentStatsFrameDelayBackwardMax_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayBackwardMax_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayBackwardMax = _MefSoamDmCurrentStatsFrameDelayBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 12),
    _MefSoamDmCurrentStatsFrameDelayBackwardMax_Type()
)
mefSoamDmCurrentStatsFrameDelayBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayBackwardMax.setUnits("microseconds")
_MefSoamDmCurrentStatsFrameDelayBackwardAvg_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayBackwardAvg_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayBackwardAvg = _MefSoamDmCurrentStatsFrameDelayBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 13),
    _MefSoamDmCurrentStatsFrameDelayBackwardAvg_Type()
)
mefSoamDmCurrentStatsFrameDelayBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayBackwardAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsIfdvForwardMin_Type = Unsigned32
_MefSoamDmCurrentStatsIfdvForwardMin_Object = MibTableColumn
mefSoamDmCurrentStatsIfdvForwardMin = _MefSoamDmCurrentStatsIfdvForwardMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 14),
    _MefSoamDmCurrentStatsIfdvForwardMin_Type()
)
mefSoamDmCurrentStatsIfdvForwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvForwardMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvForwardMin.setUnits("microseconds")
_MefSoamDmCurrentStatsIfdvForwardMax_Type = Unsigned32
_MefSoamDmCurrentStatsIfdvForwardMax_Object = MibTableColumn
mefSoamDmCurrentStatsIfdvForwardMax = _MefSoamDmCurrentStatsIfdvForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 15),
    _MefSoamDmCurrentStatsIfdvForwardMax_Type()
)
mefSoamDmCurrentStatsIfdvForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvForwardMax.setUnits("microseconds")
_MefSoamDmCurrentStatsIfdvForwardAvg_Type = Unsigned32
_MefSoamDmCurrentStatsIfdvForwardAvg_Object = MibTableColumn
mefSoamDmCurrentStatsIfdvForwardAvg = _MefSoamDmCurrentStatsIfdvForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 16),
    _MefSoamDmCurrentStatsIfdvForwardAvg_Type()
)
mefSoamDmCurrentStatsIfdvForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvForwardAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsIfdvBackwardMin_Type = Unsigned32
_MefSoamDmCurrentStatsIfdvBackwardMin_Object = MibTableColumn
mefSoamDmCurrentStatsIfdvBackwardMin = _MefSoamDmCurrentStatsIfdvBackwardMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 17),
    _MefSoamDmCurrentStatsIfdvBackwardMin_Type()
)
mefSoamDmCurrentStatsIfdvBackwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvBackwardMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvBackwardMin.setUnits("microseconds")
_MefSoamDmCurrentStatsIfdvBackwardMax_Type = Unsigned32
_MefSoamDmCurrentStatsIfdvBackwardMax_Object = MibTableColumn
mefSoamDmCurrentStatsIfdvBackwardMax = _MefSoamDmCurrentStatsIfdvBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 18),
    _MefSoamDmCurrentStatsIfdvBackwardMax_Type()
)
mefSoamDmCurrentStatsIfdvBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvBackwardMax.setUnits("microseconds")
_MefSoamDmCurrentStatsIfdvBackwardAvg_Type = Unsigned32
_MefSoamDmCurrentStatsIfdvBackwardAvg_Object = MibTableColumn
mefSoamDmCurrentStatsIfdvBackwardAvg = _MefSoamDmCurrentStatsIfdvBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 19),
    _MefSoamDmCurrentStatsIfdvBackwardAvg_Type()
)
mefSoamDmCurrentStatsIfdvBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvBackwardAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsIfdvTwoWayMin_Type = Unsigned32
_MefSoamDmCurrentStatsIfdvTwoWayMin_Object = MibTableColumn
mefSoamDmCurrentStatsIfdvTwoWayMin = _MefSoamDmCurrentStatsIfdvTwoWayMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 20),
    _MefSoamDmCurrentStatsIfdvTwoWayMin_Type()
)
mefSoamDmCurrentStatsIfdvTwoWayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvTwoWayMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvTwoWayMin.setUnits("microseconds")
_MefSoamDmCurrentStatsIfdvTwoWayMax_Type = Unsigned32
_MefSoamDmCurrentStatsIfdvTwoWayMax_Object = MibTableColumn
mefSoamDmCurrentStatsIfdvTwoWayMax = _MefSoamDmCurrentStatsIfdvTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 21),
    _MefSoamDmCurrentStatsIfdvTwoWayMax_Type()
)
mefSoamDmCurrentStatsIfdvTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvTwoWayMax.setUnits("microseconds")
_MefSoamDmCurrentStatsIfdvTwoWayAvg_Type = Unsigned32
_MefSoamDmCurrentStatsIfdvTwoWayAvg_Object = MibTableColumn
mefSoamDmCurrentStatsIfdvTwoWayAvg = _MefSoamDmCurrentStatsIfdvTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 22),
    _MefSoamDmCurrentStatsIfdvTwoWayAvg_Type()
)
mefSoamDmCurrentStatsIfdvTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsIfdvTwoWayAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsFrameDelayRangeForwardMax_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayRangeForwardMax_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayRangeForwardMax = _MefSoamDmCurrentStatsFrameDelayRangeForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 23),
    _MefSoamDmCurrentStatsFrameDelayRangeForwardMax_Type()
)
mefSoamDmCurrentStatsFrameDelayRangeForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayRangeForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayRangeForwardMax.setUnits("microseconds")
_MefSoamDmCurrentStatsFrameDelayRangeForwardAvg_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayRangeForwardAvg_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayRangeForwardAvg = _MefSoamDmCurrentStatsFrameDelayRangeForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 24),
    _MefSoamDmCurrentStatsFrameDelayRangeForwardAvg_Type()
)
mefSoamDmCurrentStatsFrameDelayRangeForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayRangeForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayRangeForwardAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsFrameDelayRangeBackwardMax_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayRangeBackwardMax_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayRangeBackwardMax = _MefSoamDmCurrentStatsFrameDelayRangeBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 25),
    _MefSoamDmCurrentStatsFrameDelayRangeBackwardMax_Type()
)
mefSoamDmCurrentStatsFrameDelayRangeBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayRangeBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayRangeBackwardMax.setUnits("microseconds")
_MefSoamDmCurrentStatsFrameDelayRangeBackwardAvg_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayRangeBackwardAvg_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayRangeBackwardAvg = _MefSoamDmCurrentStatsFrameDelayRangeBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 26),
    _MefSoamDmCurrentStatsFrameDelayRangeBackwardAvg_Type()
)
mefSoamDmCurrentStatsFrameDelayRangeBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayRangeBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayRangeBackwardAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsFrameDelayRangeTwoWayMax_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayRangeTwoWayMax_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayRangeTwoWayMax = _MefSoamDmCurrentStatsFrameDelayRangeTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 27),
    _MefSoamDmCurrentStatsFrameDelayRangeTwoWayMax_Type()
)
mefSoamDmCurrentStatsFrameDelayRangeTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayRangeTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayRangeTwoWayMax.setUnits("microseconds")
_MefSoamDmCurrentStatsFrameDelayRangeTwoWayAvg_Type = Unsigned32
_MefSoamDmCurrentStatsFrameDelayRangeTwoWayAvg_Object = MibTableColumn
mefSoamDmCurrentStatsFrameDelayRangeTwoWayAvg = _MefSoamDmCurrentStatsFrameDelayRangeTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 28),
    _MefSoamDmCurrentStatsFrameDelayRangeTwoWayAvg_Type()
)
mefSoamDmCurrentStatsFrameDelayRangeTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayRangeTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsFrameDelayRangeTwoWayAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsSoamPdusSent_Type = Gauge32
_MefSoamDmCurrentStatsSoamPdusSent_Object = MibTableColumn
mefSoamDmCurrentStatsSoamPdusSent = _MefSoamDmCurrentStatsSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 29),
    _MefSoamDmCurrentStatsSoamPdusSent_Type()
)
mefSoamDmCurrentStatsSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsSoamPdusSent.setStatus("current")
_MefSoamDmCurrentStatsSoamPdusReceived_Type = Gauge32
_MefSoamDmCurrentStatsSoamPdusReceived_Object = MibTableColumn
mefSoamDmCurrentStatsSoamPdusReceived = _MefSoamDmCurrentStatsSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 4, 1, 30),
    _MefSoamDmCurrentStatsSoamPdusReceived_Type()
)
mefSoamDmCurrentStatsSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsSoamPdusReceived.setStatus("current")
_MefSoamDmCurrentStatsBinsTable_Object = MibTable
mefSoamDmCurrentStatsBinsTable = _MefSoamDmCurrentStatsBinsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 5)
)
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsBinsTable.setStatus("current")
_MefSoamDmCurrentStatsBinsEntry_Object = MibTableRow
mefSoamDmCurrentStatsBinsEntry = _MefSoamDmCurrentStatsBinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 5, 1)
)
mefSoamDmCurrentStatsBinsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinType"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinNumber"),
)
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsBinsEntry.setStatus("current")
_MefSoamDmCurrentStatsBinsCounter_Type = Gauge32
_MefSoamDmCurrentStatsBinsCounter_Object = MibTableColumn
mefSoamDmCurrentStatsBinsCounter = _MefSoamDmCurrentStatsBinsCounter_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 5, 1, 1),
    _MefSoamDmCurrentStatsBinsCounter_Type()
)
mefSoamDmCurrentStatsBinsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsBinsCounter.setStatus("current")
_MefSoamDmHistoryStatsTable_Object = MibTable
mefSoamDmHistoryStatsTable = _MefSoamDmHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6)
)
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsTable.setStatus("current")
_MefSoamDmHistoryStatsEntry_Object = MibTableRow
mefSoamDmHistoryStatsEntry = _MefSoamDmHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1)
)
mefSoamDmHistoryStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsIndex"),
)
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsEntry.setStatus("current")
_MefSoamDmHistoryStatsIndex_Type = Unsigned32
_MefSoamDmHistoryStatsIndex_Object = MibTableColumn
mefSoamDmHistoryStatsIndex = _MefSoamDmHistoryStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 1),
    _MefSoamDmHistoryStatsIndex_Type()
)
mefSoamDmHistoryStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIndex.setStatus("current")
_MefSoamDmHistoryStatsEndTime_Type = DateAndTime
_MefSoamDmHistoryStatsEndTime_Object = MibTableColumn
mefSoamDmHistoryStatsEndTime = _MefSoamDmHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 2),
    _MefSoamDmHistoryStatsEndTime_Type()
)
mefSoamDmHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsEndTime.setStatus("current")
_MefSoamDmHistoryStatsElapsedTime_Type = TimeInterval
_MefSoamDmHistoryStatsElapsedTime_Object = MibTableColumn
mefSoamDmHistoryStatsElapsedTime = _MefSoamDmHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 3),
    _MefSoamDmHistoryStatsElapsedTime_Type()
)
mefSoamDmHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsElapsedTime.setStatus("current")
_MefSoamDmHistoryStatsSuspect_Type = TruthValue
_MefSoamDmHistoryStatsSuspect_Object = MibTableColumn
mefSoamDmHistoryStatsSuspect = _MefSoamDmHistoryStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 4),
    _MefSoamDmHistoryStatsSuspect_Type()
)
mefSoamDmHistoryStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsSuspect.setStatus("current")
_MefSoamDmHistoryStatsFrameDelayTwoWayMin_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayTwoWayMin_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayTwoWayMin = _MefSoamDmHistoryStatsFrameDelayTwoWayMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 5),
    _MefSoamDmHistoryStatsFrameDelayTwoWayMin_Type()
)
mefSoamDmHistoryStatsFrameDelayTwoWayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayTwoWayMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayTwoWayMin.setUnits("microseconds")
_MefSoamDmHistoryStatsFrameDelayTwoWayMax_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayTwoWayMax_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayTwoWayMax = _MefSoamDmHistoryStatsFrameDelayTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 6),
    _MefSoamDmHistoryStatsFrameDelayTwoWayMax_Type()
)
mefSoamDmHistoryStatsFrameDelayTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayTwoWayMax.setUnits("microseconds")
_MefSoamDmHistoryStatsFrameDelayTwoWayAvg_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayTwoWayAvg_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayTwoWayAvg = _MefSoamDmHistoryStatsFrameDelayTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 7),
    _MefSoamDmHistoryStatsFrameDelayTwoWayAvg_Type()
)
mefSoamDmHistoryStatsFrameDelayTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayTwoWayAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsFrameDelayForwardMin_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayForwardMin_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayForwardMin = _MefSoamDmHistoryStatsFrameDelayForwardMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 8),
    _MefSoamDmHistoryStatsFrameDelayForwardMin_Type()
)
mefSoamDmHistoryStatsFrameDelayForwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayForwardMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayForwardMin.setUnits("microseconds")
_MefSoamDmHistoryStatsFrameDelayForwardMax_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayForwardMax_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayForwardMax = _MefSoamDmHistoryStatsFrameDelayForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 9),
    _MefSoamDmHistoryStatsFrameDelayForwardMax_Type()
)
mefSoamDmHistoryStatsFrameDelayForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayForwardMax.setUnits("microseconds")
_MefSoamDmHistoryStatsFrameDelayForwardAvg_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayForwardAvg_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayForwardAvg = _MefSoamDmHistoryStatsFrameDelayForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 10),
    _MefSoamDmHistoryStatsFrameDelayForwardAvg_Type()
)
mefSoamDmHistoryStatsFrameDelayForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayForwardAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsFrameDelayBackwardMin_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayBackwardMin_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayBackwardMin = _MefSoamDmHistoryStatsFrameDelayBackwardMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 11),
    _MefSoamDmHistoryStatsFrameDelayBackwardMin_Type()
)
mefSoamDmHistoryStatsFrameDelayBackwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayBackwardMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayBackwardMin.setUnits("microseconds")
_MefSoamDmHistoryStatsFrameDelayBackwardMax_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayBackwardMax_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayBackwardMax = _MefSoamDmHistoryStatsFrameDelayBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 12),
    _MefSoamDmHistoryStatsFrameDelayBackwardMax_Type()
)
mefSoamDmHistoryStatsFrameDelayBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayBackwardMax.setUnits("microseconds")
_MefSoamDmHistoryStatsFrameDelayBackwardAvg_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayBackwardAvg_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayBackwardAvg = _MefSoamDmHistoryStatsFrameDelayBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 13),
    _MefSoamDmHistoryStatsFrameDelayBackwardAvg_Type()
)
mefSoamDmHistoryStatsFrameDelayBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayBackwardAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsIfdvForwardMin_Type = Unsigned32
_MefSoamDmHistoryStatsIfdvForwardMin_Object = MibTableColumn
mefSoamDmHistoryStatsIfdvForwardMin = _MefSoamDmHistoryStatsIfdvForwardMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 14),
    _MefSoamDmHistoryStatsIfdvForwardMin_Type()
)
mefSoamDmHistoryStatsIfdvForwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvForwardMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvForwardMin.setUnits("microseconds")
_MefSoamDmHistoryStatsIfdvForwardMax_Type = Unsigned32
_MefSoamDmHistoryStatsIfdvForwardMax_Object = MibTableColumn
mefSoamDmHistoryStatsIfdvForwardMax = _MefSoamDmHistoryStatsIfdvForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 15),
    _MefSoamDmHistoryStatsIfdvForwardMax_Type()
)
mefSoamDmHistoryStatsIfdvForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvForwardMax.setUnits("microseconds")
_MefSoamDmHistoryStatsIfdvForwardAvg_Type = Unsigned32
_MefSoamDmHistoryStatsIfdvForwardAvg_Object = MibTableColumn
mefSoamDmHistoryStatsIfdvForwardAvg = _MefSoamDmHistoryStatsIfdvForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 16),
    _MefSoamDmHistoryStatsIfdvForwardAvg_Type()
)
mefSoamDmHistoryStatsIfdvForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvForwardAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsIfdvBackwardMin_Type = Unsigned32
_MefSoamDmHistoryStatsIfdvBackwardMin_Object = MibTableColumn
mefSoamDmHistoryStatsIfdvBackwardMin = _MefSoamDmHistoryStatsIfdvBackwardMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 17),
    _MefSoamDmHistoryStatsIfdvBackwardMin_Type()
)
mefSoamDmHistoryStatsIfdvBackwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvBackwardMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvBackwardMin.setUnits("microseconds")
_MefSoamDmHistoryStatsIfdvBackwardMax_Type = Unsigned32
_MefSoamDmHistoryStatsIfdvBackwardMax_Object = MibTableColumn
mefSoamDmHistoryStatsIfdvBackwardMax = _MefSoamDmHistoryStatsIfdvBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 18),
    _MefSoamDmHistoryStatsIfdvBackwardMax_Type()
)
mefSoamDmHistoryStatsIfdvBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvBackwardMax.setUnits("microseconds")
_MefSoamDmHistoryStatsIfdvBackwardAvg_Type = Unsigned32
_MefSoamDmHistoryStatsIfdvBackwardAvg_Object = MibTableColumn
mefSoamDmHistoryStatsIfdvBackwardAvg = _MefSoamDmHistoryStatsIfdvBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 19),
    _MefSoamDmHistoryStatsIfdvBackwardAvg_Type()
)
mefSoamDmHistoryStatsIfdvBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvBackwardAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsIfdvTwoWayMin_Type = Unsigned32
_MefSoamDmHistoryStatsIfdvTwoWayMin_Object = MibTableColumn
mefSoamDmHistoryStatsIfdvTwoWayMin = _MefSoamDmHistoryStatsIfdvTwoWayMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 20),
    _MefSoamDmHistoryStatsIfdvTwoWayMin_Type()
)
mefSoamDmHistoryStatsIfdvTwoWayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvTwoWayMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvTwoWayMin.setUnits("microseconds")
_MefSoamDmHistoryStatsIfdvTwoWayMax_Type = Unsigned32
_MefSoamDmHistoryStatsIfdvTwoWayMax_Object = MibTableColumn
mefSoamDmHistoryStatsIfdvTwoWayMax = _MefSoamDmHistoryStatsIfdvTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 21),
    _MefSoamDmHistoryStatsIfdvTwoWayMax_Type()
)
mefSoamDmHistoryStatsIfdvTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvTwoWayMax.setUnits("microseconds")
_MefSoamDmHistoryStatsIfdvTwoWayAvg_Type = Unsigned32
_MefSoamDmHistoryStatsIfdvTwoWayAvg_Object = MibTableColumn
mefSoamDmHistoryStatsIfdvTwoWayAvg = _MefSoamDmHistoryStatsIfdvTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 22),
    _MefSoamDmHistoryStatsIfdvTwoWayAvg_Type()
)
mefSoamDmHistoryStatsIfdvTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsIfdvTwoWayAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsFrameDelayRangeForwardMax_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayRangeForwardMax_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayRangeForwardMax = _MefSoamDmHistoryStatsFrameDelayRangeForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 23),
    _MefSoamDmHistoryStatsFrameDelayRangeForwardMax_Type()
)
mefSoamDmHistoryStatsFrameDelayRangeForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayRangeForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayRangeForwardMax.setUnits("microseconds")
_MefSoamDmHistoryStatsFrameDelayRangeForwardAvg_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayRangeForwardAvg_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayRangeForwardAvg = _MefSoamDmHistoryStatsFrameDelayRangeForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 24),
    _MefSoamDmHistoryStatsFrameDelayRangeForwardAvg_Type()
)
mefSoamDmHistoryStatsFrameDelayRangeForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayRangeForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayRangeForwardAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsFrameDelayRangeBackwardMax_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayRangeBackwardMax_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayRangeBackwardMax = _MefSoamDmHistoryStatsFrameDelayRangeBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 25),
    _MefSoamDmHistoryStatsFrameDelayRangeBackwardMax_Type()
)
mefSoamDmHistoryStatsFrameDelayRangeBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayRangeBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayRangeBackwardMax.setUnits("microseconds")
_MefSoamDmHistoryStatsFrameDelayRangeBackwardAvg_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayRangeBackwardAvg_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayRangeBackwardAvg = _MefSoamDmHistoryStatsFrameDelayRangeBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 26),
    _MefSoamDmHistoryStatsFrameDelayRangeBackwardAvg_Type()
)
mefSoamDmHistoryStatsFrameDelayRangeBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayRangeBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayRangeBackwardAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsFrameDelayRangeTwoWayMax_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayRangeTwoWayMax_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayRangeTwoWayMax = _MefSoamDmHistoryStatsFrameDelayRangeTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 27),
    _MefSoamDmHistoryStatsFrameDelayRangeTwoWayMax_Type()
)
mefSoamDmHistoryStatsFrameDelayRangeTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayRangeTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayRangeTwoWayMax.setUnits("microseconds")
_MefSoamDmHistoryStatsFrameDelayRangeTwoWayAvg_Type = Unsigned32
_MefSoamDmHistoryStatsFrameDelayRangeTwoWayAvg_Object = MibTableColumn
mefSoamDmHistoryStatsFrameDelayRangeTwoWayAvg = _MefSoamDmHistoryStatsFrameDelayRangeTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 28),
    _MefSoamDmHistoryStatsFrameDelayRangeTwoWayAvg_Type()
)
mefSoamDmHistoryStatsFrameDelayRangeTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayRangeTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsFrameDelayRangeTwoWayAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsSoamPdusSent_Type = Gauge32
_MefSoamDmHistoryStatsSoamPdusSent_Object = MibTableColumn
mefSoamDmHistoryStatsSoamPdusSent = _MefSoamDmHistoryStatsSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 29),
    _MefSoamDmHistoryStatsSoamPdusSent_Type()
)
mefSoamDmHistoryStatsSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsSoamPdusSent.setStatus("current")
_MefSoamDmHistoryStatsSoamPdusReceived_Type = Gauge32
_MefSoamDmHistoryStatsSoamPdusReceived_Object = MibTableColumn
mefSoamDmHistoryStatsSoamPdusReceived = _MefSoamDmHistoryStatsSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 6, 1, 30),
    _MefSoamDmHistoryStatsSoamPdusReceived_Type()
)
mefSoamDmHistoryStatsSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsSoamPdusReceived.setStatus("current")
_MefSoamDmHistoryStatsBinsTable_Object = MibTable
mefSoamDmHistoryStatsBinsTable = _MefSoamDmHistoryStatsBinsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 7)
)
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsBinsTable.setStatus("current")
_MefSoamDmHistoryStatsBinsEntry_Object = MibTableRow
mefSoamDmHistoryStatsBinsEntry = _MefSoamDmHistoryStatsBinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 7, 1)
)
mefSoamDmHistoryStatsBinsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinType"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinNumber"),
)
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsBinsEntry.setStatus("current")
_MefSoamDmHistoryStatsBinsCounter_Type = Gauge32
_MefSoamDmHistoryStatsBinsCounter_Object = MibTableColumn
mefSoamDmHistoryStatsBinsCounter = _MefSoamDmHistoryStatsBinsCounter_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 7, 1, 1),
    _MefSoamDmHistoryStatsBinsCounter_Type()
)
mefSoamDmHistoryStatsBinsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsBinsCounter.setStatus("current")
_MefSoamDmThresholdCfgTable_Object = MibTable
mefSoamDmThresholdCfgTable = _MefSoamDmThresholdCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8)
)
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgTable.setStatus("current")
_MefSoamDmThresholdCfgEntry_Object = MibTableRow
mefSoamDmThresholdCfgEntry = _MefSoamDmThresholdCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1)
)
mefSoamDmThresholdCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgEntry.setStatus("current")


class _MefSoamDmThresholdCfgIndex_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MefSoamDmThresholdCfgIndex_Type.__name__ = "Unsigned32"
_MefSoamDmThresholdCfgIndex_Object = MibTableColumn
mefSoamDmThresholdCfgIndex = _MefSoamDmThresholdCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 1),
    _MefSoamDmThresholdCfgIndex_Type()
)
mefSoamDmThresholdCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgIndex.setStatus("current")


class _MefSoamDmThresholdCfgEnable_Type(Bits):
    """Custom type mefSoamDmThresholdCfgEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bMefSoamDmAvgFrameDelayBackwardThreshold", 18),
          ("bMefSoamDmAvgFrameDelayForwardThreshold", 10),
          ("bMefSoamDmAvgFrameDelayRangeBackwardThreshold", 23),
          ("bMefSoamDmAvgFrameDelayRangeForwardThreshold", 15),
          ("bMefSoamDmAvgFrameDelayRangeTwoWayThreshold", 7),
          ("bMefSoamDmAvgFrameDelayTwoWayThreshold", 2),
          ("bMefSoamDmAvgIfdvBackwardThreshold", 21),
          ("bMefSoamDmAvgIfdvForwardThreshold", 13),
          ("bMefSoamDmAvgIfdvTwoWayThreshold", 5),
          ("bMefSoamDmMaxFrameDelayBackwardThreshold", 17),
          ("bMefSoamDmMaxFrameDelayForwardThreshold", 9),
          ("bMefSoamDmMaxFrameDelayRangeBackwardThreshold", 22),
          ("bMefSoamDmMaxFrameDelayRangeForwardThreshold", 14),
          ("bMefSoamDmMaxFrameDelayRangeTwoWayThreshold", 6),
          ("bMefSoamDmMaxFrameDelayTwoWayThreshold", 1),
          ("bMefSoamDmMaxIfdvBackwardThreshold", 20),
          ("bMefSoamDmMaxIfdvForwardThreshold", 12),
          ("bMefSoamDmMaxIfdvTwoWayThreshold", 4),
          ("bMefSoamDmMeasuredFrameDelayBackwardThreshold", 16),
          ("bMefSoamDmMeasuredFrameDelayForwardThreshold", 8),
          ("bMefSoamDmMeasuredFrameDelayTwoWayThreshold", 0),
          ("bMefSoamDmMeasuredIfdvBackwardThreshold", 19),
          ("bMefSoamDmMeasuredIfdvForwardThreshold", 11),
          ("bMefSoamDmMeasuredIfdvTwoWayThreshold", 3))
    )

_MefSoamDmThresholdCfgEnable_Type.__name__ = "Bits"
_MefSoamDmThresholdCfgEnable_Object = MibTableColumn
mefSoamDmThresholdCfgEnable = _MefSoamDmThresholdCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 2),
    _MefSoamDmThresholdCfgEnable_Type()
)
mefSoamDmThresholdCfgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgEnable.setStatus("current")


class _MefSoamDmThresholdCfgMeasuredFrameDelayTwoWayThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMeasuredFrameDelayTwoWayThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMeasuredFrameDelayTwoWayThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMeasuredFrameDelayTwoWayThreshold = _MefSoamDmThresholdCfgMeasuredFrameDelayTwoWayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 3),
    _MefSoamDmThresholdCfgMeasuredFrameDelayTwoWayThreshold_Type()
)
mefSoamDmThresholdCfgMeasuredFrameDelayTwoWayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMeasuredFrameDelayTwoWayThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMeasuredFrameDelayTwoWayThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgMaxFrameDelayTwoWayThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMaxFrameDelayTwoWayThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMaxFrameDelayTwoWayThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMaxFrameDelayTwoWayThreshold = _MefSoamDmThresholdCfgMaxFrameDelayTwoWayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 4),
    _MefSoamDmThresholdCfgMaxFrameDelayTwoWayThreshold_Type()
)
mefSoamDmThresholdCfgMaxFrameDelayTwoWayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxFrameDelayTwoWayThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxFrameDelayTwoWayThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold = _MefSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 5),
    _MefSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Type()
)
mefSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgMeasuredIfdvTwoWayThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMeasuredIfdvTwoWayThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMeasuredIfdvTwoWayThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMeasuredIfdvTwoWayThreshold = _MefSoamDmThresholdCfgMeasuredIfdvTwoWayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 6),
    _MefSoamDmThresholdCfgMeasuredIfdvTwoWayThreshold_Type()
)
mefSoamDmThresholdCfgMeasuredIfdvTwoWayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMeasuredIfdvTwoWayThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMeasuredIfdvTwoWayThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgMaxIfdvTwoWayThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMaxIfdvTwoWayThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMaxIfdvTwoWayThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMaxIfdvTwoWayThreshold = _MefSoamDmThresholdCfgMaxIfdvTwoWayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 7),
    _MefSoamDmThresholdCfgMaxIfdvTwoWayThreshold_Type()
)
mefSoamDmThresholdCfgMaxIfdvTwoWayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxIfdvTwoWayThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxIfdvTwoWayThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgAvgIfdvTwoWayThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgAvgIfdvTwoWayThreshold = _MefSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 8),
    _MefSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Type()
)
mefSoamDmThresholdCfgAvgIfdvTwoWayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgIfdvTwoWayThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgIfdvTwoWayThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgMaxFrameDelayRangeTwoWayThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMaxFrameDelayRangeTwoWayThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMaxFrameDelayRangeTwoWayThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMaxFrameDelayRangeTwoWayThreshold = _MefSoamDmThresholdCfgMaxFrameDelayRangeTwoWayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 9),
    _MefSoamDmThresholdCfgMaxFrameDelayRangeTwoWayThreshold_Type()
)
mefSoamDmThresholdCfgMaxFrameDelayRangeTwoWayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxFrameDelayRangeTwoWayThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxFrameDelayRangeTwoWayThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgAvgFrameDelayRangeTwoWayThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgAvgFrameDelayRangeTwoWayThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgAvgFrameDelayRangeTwoWayThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgAvgFrameDelayRangeTwoWayThreshold = _MefSoamDmThresholdCfgAvgFrameDelayRangeTwoWayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 10),
    _MefSoamDmThresholdCfgAvgFrameDelayRangeTwoWayThreshold_Type()
)
mefSoamDmThresholdCfgAvgFrameDelayRangeTwoWayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgFrameDelayRangeTwoWayThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgFrameDelayRangeTwoWayThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgMeasuredFrameDelayForwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMeasuredFrameDelayForwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMeasuredFrameDelayForwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMeasuredFrameDelayForwardThreshold = _MefSoamDmThresholdCfgMeasuredFrameDelayForwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 11),
    _MefSoamDmThresholdCfgMeasuredFrameDelayForwardThreshold_Type()
)
mefSoamDmThresholdCfgMeasuredFrameDelayForwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMeasuredFrameDelayForwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMeasuredFrameDelayForwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgMaxFrameDelayForwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMaxFrameDelayForwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMaxFrameDelayForwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMaxFrameDelayForwardThreshold = _MefSoamDmThresholdCfgMaxFrameDelayForwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 12),
    _MefSoamDmThresholdCfgMaxFrameDelayForwardThreshold_Type()
)
mefSoamDmThresholdCfgMaxFrameDelayForwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxFrameDelayForwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxFrameDelayForwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgAvgFrameDelayForwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgAvgFrameDelayForwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgAvgFrameDelayForwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgAvgFrameDelayForwardThreshold = _MefSoamDmThresholdCfgAvgFrameDelayForwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 13),
    _MefSoamDmThresholdCfgAvgFrameDelayForwardThreshold_Type()
)
mefSoamDmThresholdCfgAvgFrameDelayForwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgFrameDelayForwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgFrameDelayForwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgMeasuredIfdvForwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMeasuredIfdvForwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMeasuredIfdvForwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMeasuredIfdvForwardThreshold = _MefSoamDmThresholdCfgMeasuredIfdvForwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 14),
    _MefSoamDmThresholdCfgMeasuredIfdvForwardThreshold_Type()
)
mefSoamDmThresholdCfgMeasuredIfdvForwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMeasuredIfdvForwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMeasuredIfdvForwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgMaxIfdvForwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMaxIfdvForwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMaxIfdvForwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMaxIfdvForwardThreshold = _MefSoamDmThresholdCfgMaxIfdvForwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 15),
    _MefSoamDmThresholdCfgMaxIfdvForwardThreshold_Type()
)
mefSoamDmThresholdCfgMaxIfdvForwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxIfdvForwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxIfdvForwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgAvgIfdvForwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgAvgIfdvForwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgAvgIfdvForwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgAvgIfdvForwardThreshold = _MefSoamDmThresholdCfgAvgIfdvForwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 16),
    _MefSoamDmThresholdCfgAvgIfdvForwardThreshold_Type()
)
mefSoamDmThresholdCfgAvgIfdvForwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgIfdvForwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgIfdvForwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgMaxFrameDelayRangeForwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMaxFrameDelayRangeForwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMaxFrameDelayRangeForwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMaxFrameDelayRangeForwardThreshold = _MefSoamDmThresholdCfgMaxFrameDelayRangeForwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 17),
    _MefSoamDmThresholdCfgMaxFrameDelayRangeForwardThreshold_Type()
)
mefSoamDmThresholdCfgMaxFrameDelayRangeForwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxFrameDelayRangeForwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxFrameDelayRangeForwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgAvgFrameDelayRangeForwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgAvgFrameDelayRangeForwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgAvgFrameDelayRangeForwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgAvgFrameDelayRangeForwardThreshold = _MefSoamDmThresholdCfgAvgFrameDelayRangeForwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 18),
    _MefSoamDmThresholdCfgAvgFrameDelayRangeForwardThreshold_Type()
)
mefSoamDmThresholdCfgAvgFrameDelayRangeForwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgFrameDelayRangeForwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgFrameDelayRangeForwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgMeasuredFrameDelayBackwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMeasuredFrameDelayBackwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMeasuredFrameDelayBackwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMeasuredFrameDelayBackwardThreshold = _MefSoamDmThresholdCfgMeasuredFrameDelayBackwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 19),
    _MefSoamDmThresholdCfgMeasuredFrameDelayBackwardThreshold_Type()
)
mefSoamDmThresholdCfgMeasuredFrameDelayBackwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMeasuredFrameDelayBackwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMeasuredFrameDelayBackwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgMaxFrameDelayBackwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMaxFrameDelayBackwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMaxFrameDelayBackwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMaxFrameDelayBackwardThreshold = _MefSoamDmThresholdCfgMaxFrameDelayBackwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 20),
    _MefSoamDmThresholdCfgMaxFrameDelayBackwardThreshold_Type()
)
mefSoamDmThresholdCfgMaxFrameDelayBackwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxFrameDelayBackwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxFrameDelayBackwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgAvgFrameDelayBackwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgAvgFrameDelayBackwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgAvgFrameDelayBackwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgAvgFrameDelayBackwardThreshold = _MefSoamDmThresholdCfgAvgFrameDelayBackwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 21),
    _MefSoamDmThresholdCfgAvgFrameDelayBackwardThreshold_Type()
)
mefSoamDmThresholdCfgAvgFrameDelayBackwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgFrameDelayBackwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgFrameDelayBackwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgMeasuredIfdvBackwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMeasuredIfdvBackwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMeasuredIfdvBackwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMeasuredIfdvBackwardThreshold = _MefSoamDmThresholdCfgMeasuredIfdvBackwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 22),
    _MefSoamDmThresholdCfgMeasuredIfdvBackwardThreshold_Type()
)
mefSoamDmThresholdCfgMeasuredIfdvBackwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMeasuredIfdvBackwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMeasuredIfdvBackwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgMaxIfdvBackwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMaxIfdvBackwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMaxIfdvBackwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMaxIfdvBackwardThreshold = _MefSoamDmThresholdCfgMaxIfdvBackwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 23),
    _MefSoamDmThresholdCfgMaxIfdvBackwardThreshold_Type()
)
mefSoamDmThresholdCfgMaxIfdvBackwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxIfdvBackwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxIfdvBackwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgAvgIfdvBackwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgAvgIfdvBackwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgAvgIfdvBackwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgAvgIfdvBackwardThreshold = _MefSoamDmThresholdCfgAvgIfdvBackwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 24),
    _MefSoamDmThresholdCfgAvgIfdvBackwardThreshold_Type()
)
mefSoamDmThresholdCfgAvgIfdvBackwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgIfdvBackwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgIfdvBackwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgMaxFrameDelayRangeBackwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgMaxFrameDelayRangeBackwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgMaxFrameDelayRangeBackwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgMaxFrameDelayRangeBackwardThreshold = _MefSoamDmThresholdCfgMaxFrameDelayRangeBackwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 25),
    _MefSoamDmThresholdCfgMaxFrameDelayRangeBackwardThreshold_Type()
)
mefSoamDmThresholdCfgMaxFrameDelayRangeBackwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxFrameDelayRangeBackwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgMaxFrameDelayRangeBackwardThreshold.setUnits("microseconds")


class _MefSoamDmThresholdCfgAvgFrameDelayRangeBackwardThreshold_Type(Unsigned32):
    """Custom type mefSoamDmThresholdCfgAvgFrameDelayRangeBackwardThreshold based on Unsigned32"""
    defaultValue = 4294967295


_MefSoamDmThresholdCfgAvgFrameDelayRangeBackwardThreshold_Object = MibTableColumn
mefSoamDmThresholdCfgAvgFrameDelayRangeBackwardThreshold = _MefSoamDmThresholdCfgAvgFrameDelayRangeBackwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 26),
    _MefSoamDmThresholdCfgAvgFrameDelayRangeBackwardThreshold_Type()
)
mefSoamDmThresholdCfgAvgFrameDelayRangeBackwardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgFrameDelayRangeBackwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgAvgFrameDelayRangeBackwardThreshold.setUnits("microseconds")
_MefSoamDmThresholdCfgRowStatus_Type = RowStatus
_MefSoamDmThresholdCfgRowStatus_Object = MibTableColumn
mefSoamDmThresholdCfgRowStatus = _MefSoamDmThresholdCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 8, 1, 27),
    _MefSoamDmThresholdCfgRowStatus_Type()
)
mefSoamDmThresholdCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmThresholdCfgRowStatus.setStatus("current")
_MefSoamPmNotificationCfg_ObjectIdentity = ObjectIdentity
mefSoamPmNotificationCfg = _MefSoamPmNotificationCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 4)
)


class _MefSoamPmNotificationCfgAlarmInterval_Type(Unsigned32):
    """Custom type mefSoamPmNotificationCfgAlarmInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_MefSoamPmNotificationCfgAlarmInterval_Type.__name__ = "Unsigned32"
_MefSoamPmNotificationCfgAlarmInterval_Object = MibScalar
mefSoamPmNotificationCfgAlarmInterval = _MefSoamPmNotificationCfgAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 4, 1),
    _MefSoamPmNotificationCfgAlarmInterval_Type()
)
mefSoamPmNotificationCfgAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefSoamPmNotificationCfgAlarmInterval.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamPmNotificationCfgAlarmInterval.setUnits("Seconds")


class _MefSoamPmNotificationCfgAlarmEnable_Type(Bits):
    """Custom type mefSoamPmNotificationCfgAlarmEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bAvailabilityChangeAlarm", 0),
          ("bDmSessionStartStopAlarm", 2),
          ("bLmSessionStartStopAlarm", 1),
          ("bPmThresholdAboveAlarm", 3),
          ("bPmThresholdSetClearAlarm", 4))
    )

_MefSoamPmNotificationCfgAlarmEnable_Type.__name__ = "Bits"
_MefSoamPmNotificationCfgAlarmEnable_Object = MibScalar
mefSoamPmNotificationCfgAlarmEnable = _MefSoamPmNotificationCfgAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 4, 2),
    _MefSoamPmNotificationCfgAlarmEnable_Type()
)
mefSoamPmNotificationCfgAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefSoamPmNotificationCfgAlarmEnable.setStatus("current")
_MefSoamPmNotificationObj_ObjectIdentity = ObjectIdentity
mefSoamPmNotificationObj = _MefSoamPmNotificationObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5)
)
_MefSoamPmNotificationObjDateAndTime_Type = DateAndTime
_MefSoamPmNotificationObjDateAndTime_Object = MibScalar
mefSoamPmNotificationObjDateAndTime = _MefSoamPmNotificationObjDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 1),
    _MefSoamPmNotificationObjDateAndTime_Type()
)
mefSoamPmNotificationObjDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjDateAndTime.setStatus("current")
_MefSoamPmNotificationObjThresholdId_Type = ObjectIdentifier
_MefSoamPmNotificationObjThresholdId_Object = MibScalar
mefSoamPmNotificationObjThresholdId = _MefSoamPmNotificationObjThresholdId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 2),
    _MefSoamPmNotificationObjThresholdId_Type()
)
mefSoamPmNotificationObjThresholdId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjThresholdId.setStatus("current")
_MefSoamPmNotificationObjThresholdConfig_Type = Unsigned32
_MefSoamPmNotificationObjThresholdConfig_Object = MibScalar
mefSoamPmNotificationObjThresholdConfig = _MefSoamPmNotificationObjThresholdConfig_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 3),
    _MefSoamPmNotificationObjThresholdConfig_Type()
)
mefSoamPmNotificationObjThresholdConfig.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjThresholdConfig.setStatus("current")
_MefSoamPmNotificationObjThresholdValue_Type = Unsigned32
_MefSoamPmNotificationObjThresholdValue_Object = MibScalar
mefSoamPmNotificationObjThresholdValue = _MefSoamPmNotificationObjThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 4),
    _MefSoamPmNotificationObjThresholdValue_Type()
)
mefSoamPmNotificationObjThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjThresholdValue.setStatus("current")
_MefSoamPmNotificationObjSuspect_Type = TruthValue
_MefSoamPmNotificationObjSuspect_Object = MibScalar
mefSoamPmNotificationObjSuspect = _MefSoamPmNotificationObjSuspect_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 5),
    _MefSoamPmNotificationObjSuspect_Type()
)
mefSoamPmNotificationObjSuspect.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjSuspect.setStatus("current")


class _MefSoamPmNotificationObjCrossingType_Type(Integer32):
    """Custom type mefSoamPmNotificationObjCrossingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aboveAlarm", 1),
          ("clearAlarm", 3),
          ("setAlarm", 2))
    )


_MefSoamPmNotificationObjCrossingType_Type.__name__ = "Integer32"
_MefSoamPmNotificationObjCrossingType_Object = MibScalar
mefSoamPmNotificationObjCrossingType = _MefSoamPmNotificationObjCrossingType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 6),
    _MefSoamPmNotificationObjCrossingType_Type()
)
mefSoamPmNotificationObjCrossingType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjCrossingType.setStatus("current")
_MefSoamPmNotificationObjDestinationMep_Type = MacAddress
_MefSoamPmNotificationObjDestinationMep_Object = MibScalar
mefSoamPmNotificationObjDestinationMep = _MefSoamPmNotificationObjDestinationMep_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 7),
    _MefSoamPmNotificationObjDestinationMep_Type()
)
mefSoamPmNotificationObjDestinationMep.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjDestinationMep.setStatus("current")
_MefSoamPmNotificationObjPriority_Type = MacAddress
_MefSoamPmNotificationObjPriority_Object = MibScalar
mefSoamPmNotificationObjPriority = _MefSoamPmNotificationObjPriority_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 8),
    _MefSoamPmNotificationObjPriority_Type()
)
mefSoamPmNotificationObjPriority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjPriority.setStatus("current")
_MefSoamPmMibConformance_ObjectIdentity = ObjectIdentity
mefSoamPmMibConformance = _MefSoamPmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2)
)
_MefSoamPmMibCompliances_ObjectIdentity = ObjectIdentity
mefSoamPmMibCompliances = _MefSoamPmMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 1)
)
_MefSoamPmMibGroups_ObjectIdentity = ObjectIdentity
mefSoamPmMibGroups = _MefSoamPmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2)
)
dot1agCfmMepEntry.registerAugmentions(
    ("MEF-SOAM-PM-MIB",
     "mefSoamPmMepEntry")
)
mefSoamPmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups

mefSoamPmMepMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 1)
)
mefSoamPmMepMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamPmMepOperNextIndex"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmMepSlmSingleEndedResponder"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmMepDmSingleEndedResponder"))
)
if mibBuilder.loadTexts:
    mefSoamPmMepMandatoryGroup.setStatus("current")

mefSoamPmMepOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 2)
)
mefSoamPmMepOptionalGroup.setObjects(
    ("MEF-SOAM-PM-MIB", "mefSoamPmMepLmSingleEndedResponder")
)
if mibBuilder.loadTexts:
    mefSoamPmMepOptionalGroup.setStatus("current")

mefSoamLmCfgMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 3)
)
mefSoamLmCfgMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmCfgType"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgEnabled"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgMeasurementEnable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgMessagePeriod"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgPriority"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgFrameSize"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgDataPattern"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgMeasurementInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgNumIntervalsStored"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgDestMacAddress"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgDestMepId"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgDestIsMepId"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgStartTimeType"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgFixedStartDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgRelativeStartTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgStopTimeType"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgFixedStopDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgRelativeStopTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgRepetitionTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgAvailabilityMeasurementInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgAvailabilityNumConsecutiveMeasPdus"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgAvailabilityFlrThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgAvailabilityNumConsecutiveIntervals"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgSessionType"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgSessionStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgHistoryClear"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgRowStatus"))
)
if mibBuilder.loadTexts:
    mefSoamLmCfgMandatoryGroup.setStatus("current")

mefSoamLmCfgOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 4)
)
mefSoamLmCfgOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmCfgVersion"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgTestTlvIncluded"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgTestTlvPattern"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgAlignMeasurementIntervals"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgAvailabilityNumConsecutiveHighFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgAlignMeasurementOffset"))
)
if mibBuilder.loadTexts:
    mefSoamLmCfgOptionalGroup.setStatus("current")

mefSoamLmMeasuredStatsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 5)
)
mefSoamLmMeasuredStatsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailForwardLastTransitionTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailBackwardLastTransitionTime"))
)
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsMandatoryGroup.setStatus("current")

mefSoamLmMeasuredStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 6)
)
mefSoamLmMeasuredStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsForwardFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsBackwardFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailForwardStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailBackwardStatus"))
)
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsOptionalGroup.setStatus("current")

mefSoamLmCurrentAvailStatsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 7)
)
mefSoamLmCurrentAvailStatsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsIndex"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsStartTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsElapsedTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardAvailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardAvailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardUnavailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardUnavailable"))
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsMandatoryGroup.setStatus("current")

mefSoamLmCurrentAvailStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 8)
)
mefSoamLmCurrentAvailStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardAvgFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardAvgFlr"))
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsOptionalGroup.setStatus("current")

mefSoamLmCurrentStatsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 9)
)
mefSoamLmCurrentStatsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsIndex"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsStartTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsElapsedTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsSoamPdusSent"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsSoamPdusReceived"))
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsMandatoryGroup.setStatus("current")

mefSoamLmCurrentStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 10)
)
mefSoamLmCurrentStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsForwardTransmittedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsForwardReceivedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsBackwardTransmittedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsBackwardReceivedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsForwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsForwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsForwardAvgFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsBackwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsBackwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsBackwardAvgFlr"))
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsOptionalGroup.setStatus("current")

mefSoamLmHistoryAvailStatsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 11)
)
mefSoamLmHistoryAvailStatsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsEndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsElapsedTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsForwardAvailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsBackwardAvailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsForwardUnavailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsBackwardUnavailable"))
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsMandatoryGroup.setStatus("current")

mefSoamLmHistoryAvailStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 12)
)
mefSoamLmHistoryAvailStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsForwardHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsBackwardHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsForwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsForwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsForwardAvgFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsBackwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsBackwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsBackwardAvgFlr"))
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsOptionalGroup.setStatus("current")

mefSoamLmHistoryStatsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 13)
)
mefSoamLmHistoryStatsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsEndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsElapsedTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsSoamPdusSent"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsSoamPdusReceived"))
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsMandatoryGroup.setStatus("current")

mefSoamLmHistoryStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 14)
)
mefSoamLmHistoryStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsForwardTransmittedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsForwardReceivedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsBackwardTransmittedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsBackwardReceivedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsForwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsForwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsForwardAvgFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsBackwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsBackwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsBackwardAvgFlr"))
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsOptionalGroup.setStatus("current")

mefSoamDmCfgMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 15)
)
mefSoamDmCfgMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmCfgType"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgEnabled"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasurementEnable"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgMessagePeriod"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgPriority"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgFrameSize"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgDataPattern"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasurementInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgNumIntervalsStored"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgDestMacAddress"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgDestMepId"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgDestIsMepId"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgStartTimeType"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgFixedStartDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgRelativeStartTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgStopTimeType"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgFixedStopDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgRelativeStopTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgRepetitionTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgAlignMeasurementIntervals"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgNumMeasBinsPerFrameDelayInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgSessionType"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgSessionStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgHistoryClear"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgRowStatus"))
)
if mibBuilder.loadTexts:
    mefSoamDmCfgMandatoryGroup.setStatus("current")

mefSoamDmCfgOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 16)
)
mefSoamDmCfgOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmCfgVersion"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgTestTlvIncluded"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgTestTlvPattern"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgSourceMacAddress"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgAlignMeasurementOffset"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgInterFrameDelayVariationSelectionOffset"))
)
if mibBuilder.loadTexts:
    mefSoamDmCfgOptionalGroup.setStatus("current")

mefSoamDmCfgMeasBinMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 17)
)
mefSoamDmCfgMeasBinMandatoryGroup.setObjects(
    ("MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinLowerBound")
)
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasBinMandatoryGroup.setStatus("current")

mefSoamDmMeasuredStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 18)
)
mefSoamDmMeasuredStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmMeasuredStatsFrameDelayTwoWay"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmMeasuredStatsFrameDelayForward"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmMeasuredStatsFrameDelayBackward"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmMeasuredStatsIfdvTwoWay"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmMeasuredStatsIfdvForward"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmMeasuredStatsIfdvBackward"))
)
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsOptionalGroup.setStatus("current")

mefSoamDmCurrentStatsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 19)
)
mefSoamDmCurrentStatsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsIndex"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsStartTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsElapsedTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayTwoWayMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayTwoWayMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayTwoWayAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayForwardMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayForwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayForwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayBackwardMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayBackwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayBackwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsIfdvForwardMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsIfdvForwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsIfdvForwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsIfdvBackwardMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsIfdvBackwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsIfdvBackwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayRangeForwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayRangeForwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayRangeBackwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayRangeBackwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsSoamPdusSent"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsSoamPdusReceived"))
)
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsMandatoryGroup.setStatus("current")

mefSoamDmCurrentStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 20)
)
mefSoamDmCurrentStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsIfdvTwoWayMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsIfdvTwoWayMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsIfdvTwoWayAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayRangeTwoWayMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsFrameDelayRangeTwoWayAvg"))
)
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsOptionalGroup.setStatus("current")

mefSoamDmCurrentStatsBinsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 21)
)
mefSoamDmCurrentStatsBinsMandatoryGroup.setObjects(
    ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsBinsCounter")
)
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsBinsMandatoryGroup.setStatus("current")

mefSoamDmHistoryStatsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 22)
)
mefSoamDmHistoryStatsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsEndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsElapsedTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayTwoWayMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayTwoWayMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayTwoWayAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayForwardMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayForwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayForwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayBackwardMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayBackwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayBackwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsIfdvForwardMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsIfdvForwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsIfdvForwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsIfdvBackwardMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsIfdvBackwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsIfdvBackwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayRangeForwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayRangeForwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayRangeBackwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayRangeBackwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsSoamPdusSent"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsSoamPdusReceived"))
)
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsMandatoryGroup.setStatus("current")

mefSoamDmHistoryStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 23)
)
mefSoamDmHistoryStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsIfdvTwoWayMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsIfdvTwoWayMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsIfdvTwoWayAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayRangeTwoWayMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsFrameDelayRangeTwoWayAvg"))
)
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsOptionalGroup.setStatus("current")

mefSoamDmHistoryStatsBinsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 24)
)
mefSoamDmHistoryStatsBinsMandatoryGroup.setObjects(
    ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsBinsCounter")
)
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsBinsMandatoryGroup.setStatus("current")

mefSoamLmThresholdMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 25)
)
mefSoamLmThresholdMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgEnable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgMaxFlrForwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgAvgFlrForwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgMaxFlrBackwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgAvgFlrBackwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgForwardUnavailCountThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgForwardAvailRatioThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgBackwardUnavailCountThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgBackwardAvailRatioThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgRowStatus"))
)
if mibBuilder.loadTexts:
    mefSoamLmThresholdMandatoryGroup.setStatus("current")

mefSoamLmThresholdOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 26)
)
mefSoamLmThresholdOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgForwardHighLossThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgForwardConsecutiveHighLossThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgBackwardHighLossThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgBackwardConsecutiveHighLossThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgMeasuredFlrForwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmThresholdCfgMeasuredFlrBackwardThreshold"))
)
if mibBuilder.loadTexts:
    mefSoamLmThresholdOptionalGroup.setStatus("current")

mefSoamDmThresholdMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 27)
)
mefSoamDmThresholdMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgEnable"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMaxFrameDelayTwoWayThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMaxFrameDelayForwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgAvgFrameDelayForwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMaxIfdvForwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgAvgIfdvForwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMaxFrameDelayRangeForwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgAvgFrameDelayRangeForwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMaxFrameDelayBackwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgAvgFrameDelayBackwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMaxIfdvBackwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgAvgIfdvBackwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMaxFrameDelayRangeBackwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgAvgFrameDelayRangeBackwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgRowStatus"))
)
if mibBuilder.loadTexts:
    mefSoamDmThresholdMandatoryGroup.setStatus("current")

mefSoamDmThresholdOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 28)
)
mefSoamDmThresholdOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMeasuredIfdvTwoWayThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMeasuredFrameDelayTwoWayThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMeasuredFrameDelayForwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMeasuredIfdvForwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMeasuredFrameDelayBackwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMeasuredIfdvBackwardThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMaxIfdvTwoWayThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgAvgIfdvTwoWayThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgMaxFrameDelayRangeTwoWayThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmThresholdCfgAvgFrameDelayRangeTwoWayThreshold"))
)
if mibBuilder.loadTexts:
    mefSoamDmThresholdOptionalGroup.setStatus("current")

mefSoamPmNotificationCfgMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 31)
)
mefSoamPmNotificationCfgMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamPmNotificationCfgAlarmInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationCfgAlarmEnable"))
)
if mibBuilder.loadTexts:
    mefSoamPmNotificationCfgMandatoryGroup.setStatus("current")

mefSoamPmNotificationObjMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 32)
)
mefSoamPmNotificationObjMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDestinationMep"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjPriority"))
)
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjMandatoryGroup.setStatus("current")

mefSoamPmNotificationObjOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 33)
)
mefSoamPmNotificationObjOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjThresholdConfig"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjThresholdId"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjThresholdValue"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjCrossingType"))
)
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjOptionalGroup.setStatus("current")


# Notification objects

mefSoamAvailabilityChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 0, 1)
)
mefSoamAvailabilityChangeAlarm.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailForwardStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailBackwardStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailForwardLastTransitionTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailBackwardLastTransitionTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardAvailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardUnavailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardAvailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardUnavailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDestinationMep"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjPriority"))
)
if mibBuilder.loadTexts:
    mefSoamAvailabilityChangeAlarm.setStatus(
        "current"
    )

mefSoamLmSessionStartStopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 0, 2)
)
mefSoamLmSessionStartStopAlarm.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmCfgSessionStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDestinationMep"))
)
if mibBuilder.loadTexts:
    mefSoamLmSessionStartStopAlarm.setStatus(
        "current"
    )

mefSoamDmSessionStartStopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 0, 3)
)
mefSoamDmSessionStartStopAlarm.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmCfgSessionStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDestinationMep"))
)
if mibBuilder.loadTexts:
    mefSoamDmSessionStartStopAlarm.setStatus(
        "current"
    )

mefSoamPmThresholdCrossingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 0, 4)
)
mefSoamPmThresholdCrossingAlarm.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjCrossingType"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjThresholdId"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjThresholdConfig"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjThresholdValue"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDestinationMep"))
)
if mibBuilder.loadTexts:
    mefSoamPmThresholdCrossingAlarm.setStatus(
        "current"
    )


# Notifications groups

mefSoamPmNotificationsMandatoryGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 29)
)
mefSoamPmNotificationsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamAvailabilityChangeAlarm"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmSessionStartStopAlarm"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmSessionStartStopAlarm"))
)
if mibBuilder.loadTexts:
    mefSoamPmNotificationsMandatoryGroup.setStatus(
        "current"
    )

mefSoamPmNotificationsOptionalGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 30)
)
mefSoamPmNotificationsOptionalGroup.setObjects(
    ("MEF-SOAM-PM-MIB", "mefSoamPmThresholdCrossingAlarm")
)
if mibBuilder.loadTexts:
    mefSoamPmNotificationsOptionalGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mefSoamPmMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamPmMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MEF-SOAM-PM-MIB",
    **{"mefSoamPmMib": mefSoamPmMib,
       "mefSoamPmNotifications": mefSoamPmNotifications,
       "mefSoamAvailabilityChangeAlarm": mefSoamAvailabilityChangeAlarm,
       "mefSoamLmSessionStartStopAlarm": mefSoamLmSessionStartStopAlarm,
       "mefSoamDmSessionStartStopAlarm": mefSoamDmSessionStartStopAlarm,
       "mefSoamPmThresholdCrossingAlarm": mefSoamPmThresholdCrossingAlarm,
       "mefSoamPmMibObjects": mefSoamPmMibObjects,
       "mefSoamPmMep": mefSoamPmMep,
       "mefSoamPmMepTable": mefSoamPmMepTable,
       "mefSoamPmMepEntry": mefSoamPmMepEntry,
       "mefSoamPmMepOperNextIndex": mefSoamPmMepOperNextIndex,
       "mefSoamPmMepLmSingleEndedResponder": mefSoamPmMepLmSingleEndedResponder,
       "mefSoamPmMepSlmSingleEndedResponder": mefSoamPmMepSlmSingleEndedResponder,
       "mefSoamPmMepDmSingleEndedResponder": mefSoamPmMepDmSingleEndedResponder,
       "mefSoamPmLmObjects": mefSoamPmLmObjects,
       "mefSoamLmCfgTable": mefSoamLmCfgTable,
       "mefSoamLmCfgEntry": mefSoamLmCfgEntry,
       "mefSoamLmCfgIndex": mefSoamLmCfgIndex,
       "mefSoamLmCfgType": mefSoamLmCfgType,
       "mefSoamLmCfgVersion": mefSoamLmCfgVersion,
       "mefSoamLmCfgEnabled": mefSoamLmCfgEnabled,
       "mefSoamLmCfgMeasurementEnable": mefSoamLmCfgMeasurementEnable,
       "mefSoamLmCfgMessagePeriod": mefSoamLmCfgMessagePeriod,
       "mefSoamLmCfgPriority": mefSoamLmCfgPriority,
       "mefSoamLmCfgFrameSize": mefSoamLmCfgFrameSize,
       "mefSoamLmCfgDataPattern": mefSoamLmCfgDataPattern,
       "mefSoamLmCfgTestTlvIncluded": mefSoamLmCfgTestTlvIncluded,
       "mefSoamLmCfgTestTlvPattern": mefSoamLmCfgTestTlvPattern,
       "mefSoamLmCfgMeasurementInterval": mefSoamLmCfgMeasurementInterval,
       "mefSoamLmCfgNumIntervalsStored": mefSoamLmCfgNumIntervalsStored,
       "mefSoamLmCfgDestMacAddress": mefSoamLmCfgDestMacAddress,
       "mefSoamLmCfgDestMepId": mefSoamLmCfgDestMepId,
       "mefSoamLmCfgDestIsMepId": mefSoamLmCfgDestIsMepId,
       "mefSoamLmCfgStartTimeType": mefSoamLmCfgStartTimeType,
       "mefSoamLmCfgFixedStartDateAndTime": mefSoamLmCfgFixedStartDateAndTime,
       "mefSoamLmCfgRelativeStartTime": mefSoamLmCfgRelativeStartTime,
       "mefSoamLmCfgStopTimeType": mefSoamLmCfgStopTimeType,
       "mefSoamLmCfgFixedStopDateAndTime": mefSoamLmCfgFixedStopDateAndTime,
       "mefSoamLmCfgRelativeStopTime": mefSoamLmCfgRelativeStopTime,
       "mefSoamLmCfgRepetitionTime": mefSoamLmCfgRepetitionTime,
       "mefSoamLmCfgAlignMeasurementIntervals": mefSoamLmCfgAlignMeasurementIntervals,
       "mefSoamLmCfgAlignMeasurementOffset": mefSoamLmCfgAlignMeasurementOffset,
       "mefSoamLmCfgAvailabilityMeasurementInterval": mefSoamLmCfgAvailabilityMeasurementInterval,
       "mefSoamLmCfgAvailabilityNumConsecutiveMeasPdus": mefSoamLmCfgAvailabilityNumConsecutiveMeasPdus,
       "mefSoamLmCfgAvailabilityFlrThreshold": mefSoamLmCfgAvailabilityFlrThreshold,
       "mefSoamLmCfgAvailabilityNumConsecutiveIntervals": mefSoamLmCfgAvailabilityNumConsecutiveIntervals,
       "mefSoamLmCfgAvailabilityNumConsecutiveHighFlr": mefSoamLmCfgAvailabilityNumConsecutiveHighFlr,
       "mefSoamLmCfgSessionType": mefSoamLmCfgSessionType,
       "mefSoamLmCfgSessionStatus": mefSoamLmCfgSessionStatus,
       "mefSoamLmCfgHistoryClear": mefSoamLmCfgHistoryClear,
       "mefSoamLmCfgRowStatus": mefSoamLmCfgRowStatus,
       "mefSoamLmMeasuredStatsTable": mefSoamLmMeasuredStatsTable,
       "mefSoamLmMeasuredStatsEntry": mefSoamLmMeasuredStatsEntry,
       "mefSoamLmMeasuredStatsForwardFlr": mefSoamLmMeasuredStatsForwardFlr,
       "mefSoamLmMeasuredStatsBackwardFlr": mefSoamLmMeasuredStatsBackwardFlr,
       "mefSoamLmMeasuredStatsAvailForwardStatus": mefSoamLmMeasuredStatsAvailForwardStatus,
       "mefSoamLmMeasuredStatsAvailBackwardStatus": mefSoamLmMeasuredStatsAvailBackwardStatus,
       "mefSoamLmMeasuredStatsAvailForwardLastTransitionTime": mefSoamLmMeasuredStatsAvailForwardLastTransitionTime,
       "mefSoamLmMeasuredStatsAvailBackwardLastTransitionTime": mefSoamLmMeasuredStatsAvailBackwardLastTransitionTime,
       "mefSoamLmCurrentAvailStatsTable": mefSoamLmCurrentAvailStatsTable,
       "mefSoamLmCurrentAvailStatsEntry": mefSoamLmCurrentAvailStatsEntry,
       "mefSoamLmCurrentAvailStatsIndex": mefSoamLmCurrentAvailStatsIndex,
       "mefSoamLmCurrentAvailStatsStartTime": mefSoamLmCurrentAvailStatsStartTime,
       "mefSoamLmCurrentAvailStatsElapsedTime": mefSoamLmCurrentAvailStatsElapsedTime,
       "mefSoamLmCurrentAvailStatsSuspect": mefSoamLmCurrentAvailStatsSuspect,
       "mefSoamLmCurrentAvailStatsForwardHighLoss": mefSoamLmCurrentAvailStatsForwardHighLoss,
       "mefSoamLmCurrentAvailStatsBackwardHighLoss": mefSoamLmCurrentAvailStatsBackwardHighLoss,
       "mefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss": mefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss,
       "mefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss": mefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss,
       "mefSoamLmCurrentAvailStatsForwardAvailable": mefSoamLmCurrentAvailStatsForwardAvailable,
       "mefSoamLmCurrentAvailStatsBackwardAvailable": mefSoamLmCurrentAvailStatsBackwardAvailable,
       "mefSoamLmCurrentAvailStatsForwardUnavailable": mefSoamLmCurrentAvailStatsForwardUnavailable,
       "mefSoamLmCurrentAvailStatsBackwardUnavailable": mefSoamLmCurrentAvailStatsBackwardUnavailable,
       "mefSoamLmCurrentAvailStatsForwardMinFlr": mefSoamLmCurrentAvailStatsForwardMinFlr,
       "mefSoamLmCurrentAvailStatsForwardMaxFlr": mefSoamLmCurrentAvailStatsForwardMaxFlr,
       "mefSoamLmCurrentAvailStatsForwardAvgFlr": mefSoamLmCurrentAvailStatsForwardAvgFlr,
       "mefSoamLmCurrentAvailStatsBackwardMinFlr": mefSoamLmCurrentAvailStatsBackwardMinFlr,
       "mefSoamLmCurrentAvailStatsBackwardMaxFlr": mefSoamLmCurrentAvailStatsBackwardMaxFlr,
       "mefSoamLmCurrentAvailStatsBackwardAvgFlr": mefSoamLmCurrentAvailStatsBackwardAvgFlr,
       "mefSoamLmCurrentStatsTable": mefSoamLmCurrentStatsTable,
       "mefSoamLmCurrentStatsEntry": mefSoamLmCurrentStatsEntry,
       "mefSoamLmCurrentStatsIndex": mefSoamLmCurrentStatsIndex,
       "mefSoamLmCurrentStatsStartTime": mefSoamLmCurrentStatsStartTime,
       "mefSoamLmCurrentStatsElapsedTime": mefSoamLmCurrentStatsElapsedTime,
       "mefSoamLmCurrentStatsSuspect": mefSoamLmCurrentStatsSuspect,
       "mefSoamLmCurrentStatsForwardTransmittedFrames": mefSoamLmCurrentStatsForwardTransmittedFrames,
       "mefSoamLmCurrentStatsForwardReceivedFrames": mefSoamLmCurrentStatsForwardReceivedFrames,
       "mefSoamLmCurrentStatsForwardMinFlr": mefSoamLmCurrentStatsForwardMinFlr,
       "mefSoamLmCurrentStatsForwardMaxFlr": mefSoamLmCurrentStatsForwardMaxFlr,
       "mefSoamLmCurrentStatsForwardAvgFlr": mefSoamLmCurrentStatsForwardAvgFlr,
       "mefSoamLmCurrentStatsBackwardTransmittedFrames": mefSoamLmCurrentStatsBackwardTransmittedFrames,
       "mefSoamLmCurrentStatsBackwardReceivedFrames": mefSoamLmCurrentStatsBackwardReceivedFrames,
       "mefSoamLmCurrentStatsBackwardMinFlr": mefSoamLmCurrentStatsBackwardMinFlr,
       "mefSoamLmCurrentStatsBackwardMaxFlr": mefSoamLmCurrentStatsBackwardMaxFlr,
       "mefSoamLmCurrentStatsBackwardAvgFlr": mefSoamLmCurrentStatsBackwardAvgFlr,
       "mefSoamLmCurrentStatsSoamPdusSent": mefSoamLmCurrentStatsSoamPdusSent,
       "mefSoamLmCurrentStatsSoamPdusReceived": mefSoamLmCurrentStatsSoamPdusReceived,
       "mefSoamLmHistoryAvailStatsTable": mefSoamLmHistoryAvailStatsTable,
       "mefSoamLmHistoryAvailStatsEntry": mefSoamLmHistoryAvailStatsEntry,
       "mefSoamLmHistoryAvailStatsIndex": mefSoamLmHistoryAvailStatsIndex,
       "mefSoamLmHistoryAvailStatsEndTime": mefSoamLmHistoryAvailStatsEndTime,
       "mefSoamLmHistoryAvailStatsElapsedTime": mefSoamLmHistoryAvailStatsElapsedTime,
       "mefSoamLmHistoryAvailStatsSuspect": mefSoamLmHistoryAvailStatsSuspect,
       "mefSoamLmHistoryAvailStatsForwardHighLoss": mefSoamLmHistoryAvailStatsForwardHighLoss,
       "mefSoamLmHistoryAvailStatsBackwardHighLoss": mefSoamLmHistoryAvailStatsBackwardHighLoss,
       "mefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss": mefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss,
       "mefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss": mefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss,
       "mefSoamLmHistoryAvailStatsForwardAvailable": mefSoamLmHistoryAvailStatsForwardAvailable,
       "mefSoamLmHistoryAvailStatsBackwardAvailable": mefSoamLmHistoryAvailStatsBackwardAvailable,
       "mefSoamLmHistoryAvailStatsForwardUnavailable": mefSoamLmHistoryAvailStatsForwardUnavailable,
       "mefSoamLmHistoryAvailStatsBackwardUnavailable": mefSoamLmHistoryAvailStatsBackwardUnavailable,
       "mefSoamLmHistoryAvailStatsForwardMinFlr": mefSoamLmHistoryAvailStatsForwardMinFlr,
       "mefSoamLmHistoryAvailStatsForwardMaxFlr": mefSoamLmHistoryAvailStatsForwardMaxFlr,
       "mefSoamLmHistoryAvailStatsForwardAvgFlr": mefSoamLmHistoryAvailStatsForwardAvgFlr,
       "mefSoamLmHistoryAvailStatsBackwardMinFlr": mefSoamLmHistoryAvailStatsBackwardMinFlr,
       "mefSoamLmHistoryAvailStatsBackwardMaxFlr": mefSoamLmHistoryAvailStatsBackwardMaxFlr,
       "mefSoamLmHistoryAvailStatsBackwardAvgFlr": mefSoamLmHistoryAvailStatsBackwardAvgFlr,
       "mefSoamLmHistoryStatsTable": mefSoamLmHistoryStatsTable,
       "mefSoamLmHistoryStatsEntry": mefSoamLmHistoryStatsEntry,
       "mefSoamLmHistoryStatsIndex": mefSoamLmHistoryStatsIndex,
       "mefSoamLmHistoryStatsEndTime": mefSoamLmHistoryStatsEndTime,
       "mefSoamLmHistoryStatsElapsedTime": mefSoamLmHistoryStatsElapsedTime,
       "mefSoamLmHistoryStatsSuspect": mefSoamLmHistoryStatsSuspect,
       "mefSoamLmHistoryStatsForwardTransmittedFrames": mefSoamLmHistoryStatsForwardTransmittedFrames,
       "mefSoamLmHistoryStatsForwardReceivedFrames": mefSoamLmHistoryStatsForwardReceivedFrames,
       "mefSoamLmHistoryStatsForwardMinFlr": mefSoamLmHistoryStatsForwardMinFlr,
       "mefSoamLmHistoryStatsForwardMaxFlr": mefSoamLmHistoryStatsForwardMaxFlr,
       "mefSoamLmHistoryStatsForwardAvgFlr": mefSoamLmHistoryStatsForwardAvgFlr,
       "mefSoamLmHistoryStatsBackwardTransmittedFrames": mefSoamLmHistoryStatsBackwardTransmittedFrames,
       "mefSoamLmHistoryStatsBackwardReceivedFrames": mefSoamLmHistoryStatsBackwardReceivedFrames,
       "mefSoamLmHistoryStatsBackwardMinFlr": mefSoamLmHistoryStatsBackwardMinFlr,
       "mefSoamLmHistoryStatsBackwardMaxFlr": mefSoamLmHistoryStatsBackwardMaxFlr,
       "mefSoamLmHistoryStatsBackwardAvgFlr": mefSoamLmHistoryStatsBackwardAvgFlr,
       "mefSoamLmHistoryStatsSoamPdusSent": mefSoamLmHistoryStatsSoamPdusSent,
       "mefSoamLmHistoryStatsSoamPdusReceived": mefSoamLmHistoryStatsSoamPdusReceived,
       "mefSoamLmThresholdCfgTable": mefSoamLmThresholdCfgTable,
       "mefSoamLmThresholdCfgEntry": mefSoamLmThresholdCfgEntry,
       "mefSoamLmThresholdCfgIndex": mefSoamLmThresholdCfgIndex,
       "mefSoamLmThresholdCfgEnable": mefSoamLmThresholdCfgEnable,
       "mefSoamLmThresholdCfgMeasuredFlrForwardThreshold": mefSoamLmThresholdCfgMeasuredFlrForwardThreshold,
       "mefSoamLmThresholdCfgMaxFlrForwardThreshold": mefSoamLmThresholdCfgMaxFlrForwardThreshold,
       "mefSoamLmThresholdCfgAvgFlrForwardThreshold": mefSoamLmThresholdCfgAvgFlrForwardThreshold,
       "mefSoamLmThresholdCfgMeasuredFlrBackwardThreshold": mefSoamLmThresholdCfgMeasuredFlrBackwardThreshold,
       "mefSoamLmThresholdCfgMaxFlrBackwardThreshold": mefSoamLmThresholdCfgMaxFlrBackwardThreshold,
       "mefSoamLmThresholdCfgAvgFlrBackwardThreshold": mefSoamLmThresholdCfgAvgFlrBackwardThreshold,
       "mefSoamLmThresholdCfgForwardHighLossThreshold": mefSoamLmThresholdCfgForwardHighLossThreshold,
       "mefSoamLmThresholdCfgForwardConsecutiveHighLossThreshold": mefSoamLmThresholdCfgForwardConsecutiveHighLossThreshold,
       "mefSoamLmThresholdCfgBackwardHighLossThreshold": mefSoamLmThresholdCfgBackwardHighLossThreshold,
       "mefSoamLmThresholdCfgBackwardConsecutiveHighLossThreshold": mefSoamLmThresholdCfgBackwardConsecutiveHighLossThreshold,
       "mefSoamLmThresholdCfgForwardUnavailCountThreshold": mefSoamLmThresholdCfgForwardUnavailCountThreshold,
       "mefSoamLmThresholdCfgForwardAvailRatioThreshold": mefSoamLmThresholdCfgForwardAvailRatioThreshold,
       "mefSoamLmThresholdCfgBackwardUnavailCountThreshold": mefSoamLmThresholdCfgBackwardUnavailCountThreshold,
       "mefSoamLmThresholdCfgBackwardAvailRatioThreshold": mefSoamLmThresholdCfgBackwardAvailRatioThreshold,
       "mefSoamLmThresholdCfgRowStatus": mefSoamLmThresholdCfgRowStatus,
       "mefSoamPmDmObjects": mefSoamPmDmObjects,
       "mefSoamDmCfgTable": mefSoamDmCfgTable,
       "mefSoamDmCfgEntry": mefSoamDmCfgEntry,
       "mefSoamDmCfgIndex": mefSoamDmCfgIndex,
       "mefSoamDmCfgType": mefSoamDmCfgType,
       "mefSoamDmCfgVersion": mefSoamDmCfgVersion,
       "mefSoamDmCfgEnabled": mefSoamDmCfgEnabled,
       "mefSoamDmCfgMeasurementEnable": mefSoamDmCfgMeasurementEnable,
       "mefSoamDmCfgMessagePeriod": mefSoamDmCfgMessagePeriod,
       "mefSoamDmCfgPriority": mefSoamDmCfgPriority,
       "mefSoamDmCfgFrameSize": mefSoamDmCfgFrameSize,
       "mefSoamDmCfgDataPattern": mefSoamDmCfgDataPattern,
       "mefSoamDmCfgTestTlvIncluded": mefSoamDmCfgTestTlvIncluded,
       "mefSoamDmCfgTestTlvPattern": mefSoamDmCfgTestTlvPattern,
       "mefSoamDmCfgMeasurementInterval": mefSoamDmCfgMeasurementInterval,
       "mefSoamDmCfgNumIntervalsStored": mefSoamDmCfgNumIntervalsStored,
       "mefSoamDmCfgDestMacAddress": mefSoamDmCfgDestMacAddress,
       "mefSoamDmCfgDestMepId": mefSoamDmCfgDestMepId,
       "mefSoamDmCfgDestIsMepId": mefSoamDmCfgDestIsMepId,
       "mefSoamDmCfgSourceMacAddress": mefSoamDmCfgSourceMacAddress,
       "mefSoamDmCfgStartTimeType": mefSoamDmCfgStartTimeType,
       "mefSoamDmCfgFixedStartDateAndTime": mefSoamDmCfgFixedStartDateAndTime,
       "mefSoamDmCfgRelativeStartTime": mefSoamDmCfgRelativeStartTime,
       "mefSoamDmCfgStopTimeType": mefSoamDmCfgStopTimeType,
       "mefSoamDmCfgFixedStopDateAndTime": mefSoamDmCfgFixedStopDateAndTime,
       "mefSoamDmCfgRelativeStopTime": mefSoamDmCfgRelativeStopTime,
       "mefSoamDmCfgRepetitionTime": mefSoamDmCfgRepetitionTime,
       "mefSoamDmCfgAlignMeasurementIntervals": mefSoamDmCfgAlignMeasurementIntervals,
       "mefSoamDmCfgAlignMeasurementOffset": mefSoamDmCfgAlignMeasurementOffset,
       "mefSoamDmCfgNumMeasBinsPerFrameDelayInterval": mefSoamDmCfgNumMeasBinsPerFrameDelayInterval,
       "mefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval": mefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval,
       "mefSoamDmCfgInterFrameDelayVariationSelectionOffset": mefSoamDmCfgInterFrameDelayVariationSelectionOffset,
       "mefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval": mefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval,
       "mefSoamDmCfgSessionType": mefSoamDmCfgSessionType,
       "mefSoamDmCfgSessionStatus": mefSoamDmCfgSessionStatus,
       "mefSoamDmCfgHistoryClear": mefSoamDmCfgHistoryClear,
       "mefSoamDmCfgRowStatus": mefSoamDmCfgRowStatus,
       "mefSoamDmCfgMeasBinTable": mefSoamDmCfgMeasBinTable,
       "mefSoamDmCfgMeasBinEntry": mefSoamDmCfgMeasBinEntry,
       "mefSoamDmCfgMeasBinType": mefSoamDmCfgMeasBinType,
       "mefSoamDmCfgMeasBinNumber": mefSoamDmCfgMeasBinNumber,
       "mefSoamDmCfgMeasBinLowerBound": mefSoamDmCfgMeasBinLowerBound,
       "mefSoamDmMeasuredStatsTable": mefSoamDmMeasuredStatsTable,
       "mefSoamDmMeasuredStatsEntry": mefSoamDmMeasuredStatsEntry,
       "mefSoamDmMeasuredStatsFrameDelayTwoWay": mefSoamDmMeasuredStatsFrameDelayTwoWay,
       "mefSoamDmMeasuredStatsFrameDelayForward": mefSoamDmMeasuredStatsFrameDelayForward,
       "mefSoamDmMeasuredStatsFrameDelayBackward": mefSoamDmMeasuredStatsFrameDelayBackward,
       "mefSoamDmMeasuredStatsIfdvTwoWay": mefSoamDmMeasuredStatsIfdvTwoWay,
       "mefSoamDmMeasuredStatsIfdvForward": mefSoamDmMeasuredStatsIfdvForward,
       "mefSoamDmMeasuredStatsIfdvBackward": mefSoamDmMeasuredStatsIfdvBackward,
       "mefSoamDmCurrentStatsTable": mefSoamDmCurrentStatsTable,
       "mefSoamDmCurrentStatsEntry": mefSoamDmCurrentStatsEntry,
       "mefSoamDmCurrentStatsIndex": mefSoamDmCurrentStatsIndex,
       "mefSoamDmCurrentStatsStartTime": mefSoamDmCurrentStatsStartTime,
       "mefSoamDmCurrentStatsElapsedTime": mefSoamDmCurrentStatsElapsedTime,
       "mefSoamDmCurrentStatsSuspect": mefSoamDmCurrentStatsSuspect,
       "mefSoamDmCurrentStatsFrameDelayTwoWayMin": mefSoamDmCurrentStatsFrameDelayTwoWayMin,
       "mefSoamDmCurrentStatsFrameDelayTwoWayMax": mefSoamDmCurrentStatsFrameDelayTwoWayMax,
       "mefSoamDmCurrentStatsFrameDelayTwoWayAvg": mefSoamDmCurrentStatsFrameDelayTwoWayAvg,
       "mefSoamDmCurrentStatsFrameDelayForwardMin": mefSoamDmCurrentStatsFrameDelayForwardMin,
       "mefSoamDmCurrentStatsFrameDelayForwardMax": mefSoamDmCurrentStatsFrameDelayForwardMax,
       "mefSoamDmCurrentStatsFrameDelayForwardAvg": mefSoamDmCurrentStatsFrameDelayForwardAvg,
       "mefSoamDmCurrentStatsFrameDelayBackwardMin": mefSoamDmCurrentStatsFrameDelayBackwardMin,
       "mefSoamDmCurrentStatsFrameDelayBackwardMax": mefSoamDmCurrentStatsFrameDelayBackwardMax,
       "mefSoamDmCurrentStatsFrameDelayBackwardAvg": mefSoamDmCurrentStatsFrameDelayBackwardAvg,
       "mefSoamDmCurrentStatsIfdvForwardMin": mefSoamDmCurrentStatsIfdvForwardMin,
       "mefSoamDmCurrentStatsIfdvForwardMax": mefSoamDmCurrentStatsIfdvForwardMax,
       "mefSoamDmCurrentStatsIfdvForwardAvg": mefSoamDmCurrentStatsIfdvForwardAvg,
       "mefSoamDmCurrentStatsIfdvBackwardMin": mefSoamDmCurrentStatsIfdvBackwardMin,
       "mefSoamDmCurrentStatsIfdvBackwardMax": mefSoamDmCurrentStatsIfdvBackwardMax,
       "mefSoamDmCurrentStatsIfdvBackwardAvg": mefSoamDmCurrentStatsIfdvBackwardAvg,
       "mefSoamDmCurrentStatsIfdvTwoWayMin": mefSoamDmCurrentStatsIfdvTwoWayMin,
       "mefSoamDmCurrentStatsIfdvTwoWayMax": mefSoamDmCurrentStatsIfdvTwoWayMax,
       "mefSoamDmCurrentStatsIfdvTwoWayAvg": mefSoamDmCurrentStatsIfdvTwoWayAvg,
       "mefSoamDmCurrentStatsFrameDelayRangeForwardMax": mefSoamDmCurrentStatsFrameDelayRangeForwardMax,
       "mefSoamDmCurrentStatsFrameDelayRangeForwardAvg": mefSoamDmCurrentStatsFrameDelayRangeForwardAvg,
       "mefSoamDmCurrentStatsFrameDelayRangeBackwardMax": mefSoamDmCurrentStatsFrameDelayRangeBackwardMax,
       "mefSoamDmCurrentStatsFrameDelayRangeBackwardAvg": mefSoamDmCurrentStatsFrameDelayRangeBackwardAvg,
       "mefSoamDmCurrentStatsFrameDelayRangeTwoWayMax": mefSoamDmCurrentStatsFrameDelayRangeTwoWayMax,
       "mefSoamDmCurrentStatsFrameDelayRangeTwoWayAvg": mefSoamDmCurrentStatsFrameDelayRangeTwoWayAvg,
       "mefSoamDmCurrentStatsSoamPdusSent": mefSoamDmCurrentStatsSoamPdusSent,
       "mefSoamDmCurrentStatsSoamPdusReceived": mefSoamDmCurrentStatsSoamPdusReceived,
       "mefSoamDmCurrentStatsBinsTable": mefSoamDmCurrentStatsBinsTable,
       "mefSoamDmCurrentStatsBinsEntry": mefSoamDmCurrentStatsBinsEntry,
       "mefSoamDmCurrentStatsBinsCounter": mefSoamDmCurrentStatsBinsCounter,
       "mefSoamDmHistoryStatsTable": mefSoamDmHistoryStatsTable,
       "mefSoamDmHistoryStatsEntry": mefSoamDmHistoryStatsEntry,
       "mefSoamDmHistoryStatsIndex": mefSoamDmHistoryStatsIndex,
       "mefSoamDmHistoryStatsEndTime": mefSoamDmHistoryStatsEndTime,
       "mefSoamDmHistoryStatsElapsedTime": mefSoamDmHistoryStatsElapsedTime,
       "mefSoamDmHistoryStatsSuspect": mefSoamDmHistoryStatsSuspect,
       "mefSoamDmHistoryStatsFrameDelayTwoWayMin": mefSoamDmHistoryStatsFrameDelayTwoWayMin,
       "mefSoamDmHistoryStatsFrameDelayTwoWayMax": mefSoamDmHistoryStatsFrameDelayTwoWayMax,
       "mefSoamDmHistoryStatsFrameDelayTwoWayAvg": mefSoamDmHistoryStatsFrameDelayTwoWayAvg,
       "mefSoamDmHistoryStatsFrameDelayForwardMin": mefSoamDmHistoryStatsFrameDelayForwardMin,
       "mefSoamDmHistoryStatsFrameDelayForwardMax": mefSoamDmHistoryStatsFrameDelayForwardMax,
       "mefSoamDmHistoryStatsFrameDelayForwardAvg": mefSoamDmHistoryStatsFrameDelayForwardAvg,
       "mefSoamDmHistoryStatsFrameDelayBackwardMin": mefSoamDmHistoryStatsFrameDelayBackwardMin,
       "mefSoamDmHistoryStatsFrameDelayBackwardMax": mefSoamDmHistoryStatsFrameDelayBackwardMax,
       "mefSoamDmHistoryStatsFrameDelayBackwardAvg": mefSoamDmHistoryStatsFrameDelayBackwardAvg,
       "mefSoamDmHistoryStatsIfdvForwardMin": mefSoamDmHistoryStatsIfdvForwardMin,
       "mefSoamDmHistoryStatsIfdvForwardMax": mefSoamDmHistoryStatsIfdvForwardMax,
       "mefSoamDmHistoryStatsIfdvForwardAvg": mefSoamDmHistoryStatsIfdvForwardAvg,
       "mefSoamDmHistoryStatsIfdvBackwardMin": mefSoamDmHistoryStatsIfdvBackwardMin,
       "mefSoamDmHistoryStatsIfdvBackwardMax": mefSoamDmHistoryStatsIfdvBackwardMax,
       "mefSoamDmHistoryStatsIfdvBackwardAvg": mefSoamDmHistoryStatsIfdvBackwardAvg,
       "mefSoamDmHistoryStatsIfdvTwoWayMin": mefSoamDmHistoryStatsIfdvTwoWayMin,
       "mefSoamDmHistoryStatsIfdvTwoWayMax": mefSoamDmHistoryStatsIfdvTwoWayMax,
       "mefSoamDmHistoryStatsIfdvTwoWayAvg": mefSoamDmHistoryStatsIfdvTwoWayAvg,
       "mefSoamDmHistoryStatsFrameDelayRangeForwardMax": mefSoamDmHistoryStatsFrameDelayRangeForwardMax,
       "mefSoamDmHistoryStatsFrameDelayRangeForwardAvg": mefSoamDmHistoryStatsFrameDelayRangeForwardAvg,
       "mefSoamDmHistoryStatsFrameDelayRangeBackwardMax": mefSoamDmHistoryStatsFrameDelayRangeBackwardMax,
       "mefSoamDmHistoryStatsFrameDelayRangeBackwardAvg": mefSoamDmHistoryStatsFrameDelayRangeBackwardAvg,
       "mefSoamDmHistoryStatsFrameDelayRangeTwoWayMax": mefSoamDmHistoryStatsFrameDelayRangeTwoWayMax,
       "mefSoamDmHistoryStatsFrameDelayRangeTwoWayAvg": mefSoamDmHistoryStatsFrameDelayRangeTwoWayAvg,
       "mefSoamDmHistoryStatsSoamPdusSent": mefSoamDmHistoryStatsSoamPdusSent,
       "mefSoamDmHistoryStatsSoamPdusReceived": mefSoamDmHistoryStatsSoamPdusReceived,
       "mefSoamDmHistoryStatsBinsTable": mefSoamDmHistoryStatsBinsTable,
       "mefSoamDmHistoryStatsBinsEntry": mefSoamDmHistoryStatsBinsEntry,
       "mefSoamDmHistoryStatsBinsCounter": mefSoamDmHistoryStatsBinsCounter,
       "mefSoamDmThresholdCfgTable": mefSoamDmThresholdCfgTable,
       "mefSoamDmThresholdCfgEntry": mefSoamDmThresholdCfgEntry,
       "mefSoamDmThresholdCfgIndex": mefSoamDmThresholdCfgIndex,
       "mefSoamDmThresholdCfgEnable": mefSoamDmThresholdCfgEnable,
       "mefSoamDmThresholdCfgMeasuredFrameDelayTwoWayThreshold": mefSoamDmThresholdCfgMeasuredFrameDelayTwoWayThreshold,
       "mefSoamDmThresholdCfgMaxFrameDelayTwoWayThreshold": mefSoamDmThresholdCfgMaxFrameDelayTwoWayThreshold,
       "mefSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold": mefSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold,
       "mefSoamDmThresholdCfgMeasuredIfdvTwoWayThreshold": mefSoamDmThresholdCfgMeasuredIfdvTwoWayThreshold,
       "mefSoamDmThresholdCfgMaxIfdvTwoWayThreshold": mefSoamDmThresholdCfgMaxIfdvTwoWayThreshold,
       "mefSoamDmThresholdCfgAvgIfdvTwoWayThreshold": mefSoamDmThresholdCfgAvgIfdvTwoWayThreshold,
       "mefSoamDmThresholdCfgMaxFrameDelayRangeTwoWayThreshold": mefSoamDmThresholdCfgMaxFrameDelayRangeTwoWayThreshold,
       "mefSoamDmThresholdCfgAvgFrameDelayRangeTwoWayThreshold": mefSoamDmThresholdCfgAvgFrameDelayRangeTwoWayThreshold,
       "mefSoamDmThresholdCfgMeasuredFrameDelayForwardThreshold": mefSoamDmThresholdCfgMeasuredFrameDelayForwardThreshold,
       "mefSoamDmThresholdCfgMaxFrameDelayForwardThreshold": mefSoamDmThresholdCfgMaxFrameDelayForwardThreshold,
       "mefSoamDmThresholdCfgAvgFrameDelayForwardThreshold": mefSoamDmThresholdCfgAvgFrameDelayForwardThreshold,
       "mefSoamDmThresholdCfgMeasuredIfdvForwardThreshold": mefSoamDmThresholdCfgMeasuredIfdvForwardThreshold,
       "mefSoamDmThresholdCfgMaxIfdvForwardThreshold": mefSoamDmThresholdCfgMaxIfdvForwardThreshold,
       "mefSoamDmThresholdCfgAvgIfdvForwardThreshold": mefSoamDmThresholdCfgAvgIfdvForwardThreshold,
       "mefSoamDmThresholdCfgMaxFrameDelayRangeForwardThreshold": mefSoamDmThresholdCfgMaxFrameDelayRangeForwardThreshold,
       "mefSoamDmThresholdCfgAvgFrameDelayRangeForwardThreshold": mefSoamDmThresholdCfgAvgFrameDelayRangeForwardThreshold,
       "mefSoamDmThresholdCfgMeasuredFrameDelayBackwardThreshold": mefSoamDmThresholdCfgMeasuredFrameDelayBackwardThreshold,
       "mefSoamDmThresholdCfgMaxFrameDelayBackwardThreshold": mefSoamDmThresholdCfgMaxFrameDelayBackwardThreshold,
       "mefSoamDmThresholdCfgAvgFrameDelayBackwardThreshold": mefSoamDmThresholdCfgAvgFrameDelayBackwardThreshold,
       "mefSoamDmThresholdCfgMeasuredIfdvBackwardThreshold": mefSoamDmThresholdCfgMeasuredIfdvBackwardThreshold,
       "mefSoamDmThresholdCfgMaxIfdvBackwardThreshold": mefSoamDmThresholdCfgMaxIfdvBackwardThreshold,
       "mefSoamDmThresholdCfgAvgIfdvBackwardThreshold": mefSoamDmThresholdCfgAvgIfdvBackwardThreshold,
       "mefSoamDmThresholdCfgMaxFrameDelayRangeBackwardThreshold": mefSoamDmThresholdCfgMaxFrameDelayRangeBackwardThreshold,
       "mefSoamDmThresholdCfgAvgFrameDelayRangeBackwardThreshold": mefSoamDmThresholdCfgAvgFrameDelayRangeBackwardThreshold,
       "mefSoamDmThresholdCfgRowStatus": mefSoamDmThresholdCfgRowStatus,
       "mefSoamPmNotificationCfg": mefSoamPmNotificationCfg,
       "mefSoamPmNotificationCfgAlarmInterval": mefSoamPmNotificationCfgAlarmInterval,
       "mefSoamPmNotificationCfgAlarmEnable": mefSoamPmNotificationCfgAlarmEnable,
       "mefSoamPmNotificationObj": mefSoamPmNotificationObj,
       "mefSoamPmNotificationObjDateAndTime": mefSoamPmNotificationObjDateAndTime,
       "mefSoamPmNotificationObjThresholdId": mefSoamPmNotificationObjThresholdId,
       "mefSoamPmNotificationObjThresholdConfig": mefSoamPmNotificationObjThresholdConfig,
       "mefSoamPmNotificationObjThresholdValue": mefSoamPmNotificationObjThresholdValue,
       "mefSoamPmNotificationObjSuspect": mefSoamPmNotificationObjSuspect,
       "mefSoamPmNotificationObjCrossingType": mefSoamPmNotificationObjCrossingType,
       "mefSoamPmNotificationObjDestinationMep": mefSoamPmNotificationObjDestinationMep,
       "mefSoamPmNotificationObjPriority": mefSoamPmNotificationObjPriority,
       "mefSoamPmMibConformance": mefSoamPmMibConformance,
       "mefSoamPmMibCompliances": mefSoamPmMibCompliances,
       "mefSoamPmMibCompliance": mefSoamPmMibCompliance,
       "mefSoamPmMibGroups": mefSoamPmMibGroups,
       "mefSoamPmMepMandatoryGroup": mefSoamPmMepMandatoryGroup,
       "mefSoamPmMepOptionalGroup": mefSoamPmMepOptionalGroup,
       "mefSoamLmCfgMandatoryGroup": mefSoamLmCfgMandatoryGroup,
       "mefSoamLmCfgOptionalGroup": mefSoamLmCfgOptionalGroup,
       "mefSoamLmMeasuredStatsMandatoryGroup": mefSoamLmMeasuredStatsMandatoryGroup,
       "mefSoamLmMeasuredStatsOptionalGroup": mefSoamLmMeasuredStatsOptionalGroup,
       "mefSoamLmCurrentAvailStatsMandatoryGroup": mefSoamLmCurrentAvailStatsMandatoryGroup,
       "mefSoamLmCurrentAvailStatsOptionalGroup": mefSoamLmCurrentAvailStatsOptionalGroup,
       "mefSoamLmCurrentStatsMandatoryGroup": mefSoamLmCurrentStatsMandatoryGroup,
       "mefSoamLmCurrentStatsOptionalGroup": mefSoamLmCurrentStatsOptionalGroup,
       "mefSoamLmHistoryAvailStatsMandatoryGroup": mefSoamLmHistoryAvailStatsMandatoryGroup,
       "mefSoamLmHistoryAvailStatsOptionalGroup": mefSoamLmHistoryAvailStatsOptionalGroup,
       "mefSoamLmHistoryStatsMandatoryGroup": mefSoamLmHistoryStatsMandatoryGroup,
       "mefSoamLmHistoryStatsOptionalGroup": mefSoamLmHistoryStatsOptionalGroup,
       "mefSoamDmCfgMandatoryGroup": mefSoamDmCfgMandatoryGroup,
       "mefSoamDmCfgOptionalGroup": mefSoamDmCfgOptionalGroup,
       "mefSoamDmCfgMeasBinMandatoryGroup": mefSoamDmCfgMeasBinMandatoryGroup,
       "mefSoamDmMeasuredStatsOptionalGroup": mefSoamDmMeasuredStatsOptionalGroup,
       "mefSoamDmCurrentStatsMandatoryGroup": mefSoamDmCurrentStatsMandatoryGroup,
       "mefSoamDmCurrentStatsOptionalGroup": mefSoamDmCurrentStatsOptionalGroup,
       "mefSoamDmCurrentStatsBinsMandatoryGroup": mefSoamDmCurrentStatsBinsMandatoryGroup,
       "mefSoamDmHistoryStatsMandatoryGroup": mefSoamDmHistoryStatsMandatoryGroup,
       "mefSoamDmHistoryStatsOptionalGroup": mefSoamDmHistoryStatsOptionalGroup,
       "mefSoamDmHistoryStatsBinsMandatoryGroup": mefSoamDmHistoryStatsBinsMandatoryGroup,
       "mefSoamLmThresholdMandatoryGroup": mefSoamLmThresholdMandatoryGroup,
       "mefSoamLmThresholdOptionalGroup": mefSoamLmThresholdOptionalGroup,
       "mefSoamDmThresholdMandatoryGroup": mefSoamDmThresholdMandatoryGroup,
       "mefSoamDmThresholdOptionalGroup": mefSoamDmThresholdOptionalGroup,
       "mefSoamPmNotificationsMandatoryGroup": mefSoamPmNotificationsMandatoryGroup,
       "mefSoamPmNotificationsOptionalGroup": mefSoamPmNotificationsOptionalGroup,
       "mefSoamPmNotificationCfgMandatoryGroup": mefSoamPmNotificationCfgMandatoryGroup,
       "mefSoamPmNotificationObjMandatoryGroup": mefSoamPmNotificationObjMandatoryGroup,
       "mefSoamPmNotificationObjOptionalGroup": mefSoamPmNotificationObjOptionalGroup}
)
