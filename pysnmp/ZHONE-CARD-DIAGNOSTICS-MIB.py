# SNMP MIB module (ZHONE-CARD-DIAGNOSTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-CARD-DIAGNOSTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:06 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(zhoneCard,
 zhoneModules,
 zhoneShelfIndex,
 zhoneSlotIndex) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneCard",
    "zhoneModules",
    "zhoneShelfIndex",
    "zhoneSlotIndex")

(ZhoneDiagAction,
 ZhoneDiagResult,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneDiagAction",
    "ZhoneDiagResult",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneCardDiagnosticsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 11)
)
zhoneCardDiagnosticsModule.setRevisions(
        ("2010-03-05 14:05",
         "2009-05-14 09:39",
         "2009-05-07 22:37",
         "2009-01-12 15:36",
         "2008-10-22 05:28",
         "2006-07-24 11:28",
         "2001-11-14 15:28",
         "2001-08-30 11:21",
         "2001-08-27 18:14",
         "2001-06-28 12:01",
         "2001-06-26 12:40",
         "2000-12-12 16:30",
         "2000-10-19 19:45",
         "2000-10-17 10:32",
         "2000-09-12 11:07")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneCardDiagNextTable_Object = MibTable
zhoneCardDiagNextTable = _ZhoneCardDiagNextTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 5)
)
if mibBuilder.loadTexts:
    zhoneCardDiagNextTable.setStatus("current")
_ZhoneCardDiagNextEntry_Object = MibTableRow
zhoneCardDiagNextEntry = _ZhoneCardDiagNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 5, 1)
)
zhoneCardDiagNextEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
)
if mibBuilder.loadTexts:
    zhoneCardDiagNextEntry.setStatus("current")


class _ZhoneCardDiagNextIndex_Type(Integer32):
    """Custom type zhoneCardDiagNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZhoneCardDiagNextIndex_Type.__name__ = "Integer32"
_ZhoneCardDiagNextIndex_Object = MibTableColumn
zhoneCardDiagNextIndex = _ZhoneCardDiagNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 5, 1, 1),
    _ZhoneCardDiagNextIndex_Type()
)
zhoneCardDiagNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCardDiagNextIndex.setStatus("current")
_ZhoneCardDiagTable_Object = MibTable
zhoneCardDiagTable = _ZhoneCardDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 6)
)
if mibBuilder.loadTexts:
    zhoneCardDiagTable.setStatus("current")
_ZhoneCardDiagEntry_Object = MibTableRow
zhoneCardDiagEntry = _ZhoneCardDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 6, 1)
)
zhoneCardDiagEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
    (0, "ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneCardDiagIndex"),
)
if mibBuilder.loadTexts:
    zhoneCardDiagEntry.setStatus("current")


class _ZhoneCardDiagIndex_Type(Integer32):
    """Custom type zhoneCardDiagIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZhoneCardDiagIndex_Type.__name__ = "Integer32"
_ZhoneCardDiagIndex_Object = MibTableColumn
zhoneCardDiagIndex = _ZhoneCardDiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 6, 1, 1),
    _ZhoneCardDiagIndex_Type()
)
zhoneCardDiagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCardDiagIndex.setStatus("current")


class _ZhoneCardDiagType_Type(Integer32):
    """Custom type zhoneCardDiagType based on Integer32"""
    defaultValue = 1

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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("backPlane", 12),
          ("cardEEprom", 3),
          ("fanTray", 8),
          ("frbus", 4),
          ("ioCard", 10),
          ("mezzanineCard", 11),
          ("midPlane", 13),
          ("pcmcia", 5),
          ("realTimeClock", 7),
          ("selftest", 1),
          ("shelfLamp", 6),
          ("shelfMonitor", 9),
          ("supvBus", 2))
    )


_ZhoneCardDiagType_Type.__name__ = "Integer32"
_ZhoneCardDiagType_Object = MibTableColumn
zhoneCardDiagType = _ZhoneCardDiagType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 6, 1, 2),
    _ZhoneCardDiagType_Type()
)
zhoneCardDiagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCardDiagType.setStatus("current")


class _ZhoneCardDiagAction_Type(ZhoneDiagAction):
    """Custom type zhoneCardDiagAction based on ZhoneDiagAction"""


_ZhoneCardDiagAction_Object = MibTableColumn
zhoneCardDiagAction = _ZhoneCardDiagAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 6, 1, 3),
    _ZhoneCardDiagAction_Type()
)
zhoneCardDiagAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCardDiagAction.setStatus("current")


class _ZhoneCardDiagRepetition_Type(Integer32):
    """Custom type zhoneCardDiagRepetition based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_ZhoneCardDiagRepetition_Type.__name__ = "Integer32"
_ZhoneCardDiagRepetition_Object = MibTableColumn
zhoneCardDiagRepetition = _ZhoneCardDiagRepetition_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 6, 1, 4),
    _ZhoneCardDiagRepetition_Type()
)
zhoneCardDiagRepetition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCardDiagRepetition.setStatus("current")


class _ZhoneCardDiagDuration_Type(Integer32):
    """Custom type zhoneCardDiagDuration based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_ZhoneCardDiagDuration_Type.__name__ = "Integer32"
_ZhoneCardDiagDuration_Object = MibTableColumn
zhoneCardDiagDuration = _ZhoneCardDiagDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 6, 1, 5),
    _ZhoneCardDiagDuration_Type()
)
zhoneCardDiagDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCardDiagDuration.setStatus("current")
if mibBuilder.loadTexts:
    zhoneCardDiagDuration.setUnits("seconds")
_ZhoneCardDiagResult_Type = ZhoneDiagResult
_ZhoneCardDiagResult_Object = MibTableColumn
zhoneCardDiagResult = _ZhoneCardDiagResult_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 6, 1, 6),
    _ZhoneCardDiagResult_Type()
)
zhoneCardDiagResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCardDiagResult.setStatus("current")
_ZhoneCardDiagPassCount_Type = Counter32
_ZhoneCardDiagPassCount_Object = MibTableColumn
zhoneCardDiagPassCount = _ZhoneCardDiagPassCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 6, 1, 7),
    _ZhoneCardDiagPassCount_Type()
)
zhoneCardDiagPassCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCardDiagPassCount.setStatus("current")
_ZhoneCardDiagFailCount_Type = Counter32
_ZhoneCardDiagFailCount_Object = MibTableColumn
zhoneCardDiagFailCount = _ZhoneCardDiagFailCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 6, 1, 8),
    _ZhoneCardDiagFailCount_Type()
)
zhoneCardDiagFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCardDiagFailCount.setStatus("current")


class _ZhoneCardDiagDetails_Type(OctetString):
    """Custom type zhoneCardDiagDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneCardDiagDetails_Type.__name__ = "OctetString"
_ZhoneCardDiagDetails_Object = MibTableColumn
zhoneCardDiagDetails = _ZhoneCardDiagDetails_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 6, 1, 9),
    _ZhoneCardDiagDetails_Type()
)
zhoneCardDiagDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCardDiagDetails.setStatus("current")
_ZhoneCardDiagStartTime_Type = DateAndTime
_ZhoneCardDiagStartTime_Object = MibTableColumn
zhoneCardDiagStartTime = _ZhoneCardDiagStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 6, 1, 10),
    _ZhoneCardDiagStartTime_Type()
)
zhoneCardDiagStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCardDiagStartTime.setStatus("current")
_ZhoneCardDiagEndTime_Type = DateAndTime
_ZhoneCardDiagEndTime_Object = MibTableColumn
zhoneCardDiagEndTime = _ZhoneCardDiagEndTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 6, 1, 11),
    _ZhoneCardDiagEndTime_Type()
)
zhoneCardDiagEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCardDiagEndTime.setStatus("current")
_ZhoneCardDiagRowStatus_Type = ZhoneRowStatus
_ZhoneCardDiagRowStatus_Object = MibTableColumn
zhoneCardDiagRowStatus = _ZhoneCardDiagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 6, 1, 12),
    _ZhoneCardDiagRowStatus_Type()
)
zhoneCardDiagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneCardDiagRowStatus.setStatus("current")
_ZhoneTacTestTable_Object = MibTable
zhoneTacTestTable = _ZhoneTacTestTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 7)
)
if mibBuilder.loadTexts:
    zhoneTacTestTable.setStatus("current")
_ZhoneTacTestEntry_Object = MibTableRow
zhoneTacTestEntry = _ZhoneTacTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 7, 1)
)
zhoneTacTestEntry.setIndexNames(
    (0, "ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneTacIndex"),
)
if mibBuilder.loadTexts:
    zhoneTacTestEntry.setStatus("current")


class _ZhoneTacIndex_Type(Integer32):
    """Custom type zhoneTacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ZhoneTacIndex_Type.__name__ = "Integer32"
_ZhoneTacIndex_Object = MibTableColumn
zhoneTacIndex = _ZhoneTacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 7, 1, 1),
    _ZhoneTacIndex_Type()
)
zhoneTacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneTacIndex.setStatus("current")


class _ZhoneTacInterfaceIndex_Type(InterfaceIndexOrZero):
    """Custom type zhoneTacInterfaceIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_ZhoneTacInterfaceIndex_Object = MibTableColumn
zhoneTacInterfaceIndex = _ZhoneTacInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 7, 1, 2),
    _ZhoneTacInterfaceIndex_Type()
)
zhoneTacInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneTacInterfaceIndex.setStatus("current")


class _ZhoneTacTestMode_Type(Integer32):
    """Custom type zhoneTacTestMode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mtacModeBridge", 1),
          ("mtacModeLookIn", 2),
          ("mtacModeLookOut", 3),
          ("mtacModeNone", 4))
    )


_ZhoneTacTestMode_Type.__name__ = "Integer32"
_ZhoneTacTestMode_Object = MibTableColumn
zhoneTacTestMode = _ZhoneTacTestMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 7, 1, 3),
    _ZhoneTacTestMode_Type()
)
zhoneTacTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneTacTestMode.setStatus("current")


class _ZhoneTacTestId_Type(Integer32):
    """Custom type zhoneTacTestId based on Integer32"""
    defaultValue = 1

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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("abortTest", 3),
          ("arbitrarySignalToneMeasurement", 18),
          ("calibration", 4),
          ("dcFeedSelf", 23),
          ("dcLoopResistance", 7),
          ("dialingSelfTest", 29),
          ("distanceToOpen", 12),
          ("drawAndBreakDialTone", 21),
          ("dtmfAndPulseDigitMeasurement", 15),
          ("fiveElementInsulationResistance", 9),
          ("foreignACCurrents", 13),
          ("foreignACVoltage", 6),
          ("foreignDCVoltage", 5),
          ("fuseTest", 31),
          ("howlerTest", 30),
          ("inwardCurrent", 22),
          ("meteringSelfTest", 27),
          ("noiseMeasurement", 16),
          ("none", 1),
          ("onAndOffHookSelfTest", 24),
          ("readLoopAndBatteryConditions", 32),
          ("receiverOffHook", 11),
          ("ringerEquivalencyNumber", 14),
          ("ringingMonitor", 26),
          ("ringingSelfTest", 25),
          ("runAllTests", 2),
          ("signalToNoiseRatio", 17),
          ("threeElementCapacitance", 10),
          ("threeElementInsulationResistance", 8),
          ("toneGeneration", 19),
          ("transHybridLoss", 20),
          ("transmissionSelfTest", 28))
    )


_ZhoneTacTestId_Type.__name__ = "Integer32"
_ZhoneTacTestId_Object = MibTableColumn
zhoneTacTestId = _ZhoneTacTestId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 7, 1, 4),
    _ZhoneTacTestId_Type()
)
zhoneTacTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneTacTestId.setStatus("current")


class _ZhoneTacTestParam1_Type(Integer32):
    """Custom type zhoneTacTestParam1 based on Integer32"""
    defaultValue = 0


_ZhoneTacTestParam1_Object = MibTableColumn
zhoneTacTestParam1 = _ZhoneTacTestParam1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 7, 1, 5),
    _ZhoneTacTestParam1_Type()
)
zhoneTacTestParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneTacTestParam1.setStatus("current")


class _ZhoneTacTestParam2_Type(Integer32):
    """Custom type zhoneTacTestParam2 based on Integer32"""
    defaultValue = 0


_ZhoneTacTestParam2_Object = MibTableColumn
zhoneTacTestParam2 = _ZhoneTacTestParam2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 7, 1, 6),
    _ZhoneTacTestParam2_Type()
)
zhoneTacTestParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneTacTestParam2.setStatus("current")


class _ZhoneTacTestParam3_Type(Integer32):
    """Custom type zhoneTacTestParam3 based on Integer32"""
    defaultValue = 0


_ZhoneTacTestParam3_Object = MibTableColumn
zhoneTacTestParam3 = _ZhoneTacTestParam3_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 7, 1, 7),
    _ZhoneTacTestParam3_Type()
)
zhoneTacTestParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneTacTestParam3.setStatus("current")


class _ZhoneTacTestParam4_Type(Integer32):
    """Custom type zhoneTacTestParam4 based on Integer32"""
    defaultValue = 0


_ZhoneTacTestParam4_Object = MibTableColumn
zhoneTacTestParam4 = _ZhoneTacTestParam4_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 7, 1, 8),
    _ZhoneTacTestParam4_Type()
)
zhoneTacTestParam4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneTacTestParam4.setStatus("current")


class _ZhoneTacTestParam5_Type(Integer32):
    """Custom type zhoneTacTestParam5 based on Integer32"""
    defaultValue = 0


_ZhoneTacTestParam5_Object = MibTableColumn
zhoneTacTestParam5 = _ZhoneTacTestParam5_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 7, 1, 9),
    _ZhoneTacTestParam5_Type()
)
zhoneTacTestParam5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneTacTestParam5.setStatus("current")
_ZhoneTacTestResultsTable_Object = MibTable
zhoneTacTestResultsTable = _ZhoneTacTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 12)
)
if mibBuilder.loadTexts:
    zhoneTacTestResultsTable.setStatus("current")
_ZhoneTacTestResultsEntry_Object = MibTableRow
zhoneTacTestResultsEntry = _ZhoneTacTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 12, 1)
)
zhoneTacTestResultsEntry.setIndexNames(
    (0, "ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneTacIndex"),
)
if mibBuilder.loadTexts:
    zhoneTacTestResultsEntry.setStatus("current")
_ZhoneTacTestResultsTimeStarted_Type = TimeTicks
_ZhoneTacTestResultsTimeStarted_Object = MibTableColumn
zhoneTacTestResultsTimeStarted = _ZhoneTacTestResultsTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 12, 1, 1),
    _ZhoneTacTestResultsTimeStarted_Type()
)
zhoneTacTestResultsTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTacTestResultsTimeStarted.setStatus("current")
_ZhoneTacTestResultsTimeEnded_Type = TimeTicks
_ZhoneTacTestResultsTimeEnded_Object = MibTableColumn
zhoneTacTestResultsTimeEnded = _ZhoneTacTestResultsTimeEnded_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 12, 1, 2),
    _ZhoneTacTestResultsTimeEnded_Type()
)
zhoneTacTestResultsTimeEnded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTacTestResultsTimeEnded.setStatus("current")


class _ZhoneTacTestResultStatus_Type(Integer32):
    """Custom type zhoneTacTestResultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("testAborted", 4),
          ("testCompleted", 3),
          ("testInProgress", 2),
          ("testNotStarted", 1),
          ("testNotSupported", 5))
    )


_ZhoneTacTestResultStatus_Type.__name__ = "Integer32"
_ZhoneTacTestResultStatus_Object = MibTableColumn
zhoneTacTestResultStatus = _ZhoneTacTestResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 12, 1, 3),
    _ZhoneTacTestResultStatus_Type()
)
zhoneTacTestResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTacTestResultStatus.setStatus("current")


class _ZhoneTacTestResultsOutput_Type(OctetString):
    """Custom type zhoneTacTestResultsOutput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8000),
    )


_ZhoneTacTestResultsOutput_Type.__name__ = "OctetString"
_ZhoneTacTestResultsOutput_Object = MibTableColumn
zhoneTacTestResultsOutput = _ZhoneTacTestResultsOutput_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 12, 1, 4),
    _ZhoneTacTestResultsOutput_Type()
)
zhoneTacTestResultsOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTacTestResultsOutput.setStatus("current")
_ZhoneTacTestTraps_ObjectIdentity = ObjectIdentity
zhoneTacTestTraps = _ZhoneTacTestTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 13)
)
if mibBuilder.loadTexts:
    zhoneTacTestTraps.setStatus("current")
_ZhoneRingerTraps_ObjectIdentity = ObjectIdentity
zhoneRingerTraps = _ZhoneRingerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 13, 0)
)
if mibBuilder.loadTexts:
    zhoneRingerTraps.setStatus("current")

# Managed Objects groups

zhoneCardDiagObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 6, 11, 1)
)
zhoneCardDiagObjects.setObjects(
      *(("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneCardDiagNextIndex"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneCardDiagType"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneCardDiagAction"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneCardDiagRepetition"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneCardDiagDuration"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneCardDiagResult"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneCardDiagPassCount"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneCardDiagFailCount"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneCardDiagDetails"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneCardDiagStartTime"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneCardDiagEndTime"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneCardDiagRowStatus"))
)
if mibBuilder.loadTexts:
    zhoneCardDiagObjects.setStatus("current")

zhoneTacTestObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 6, 11, 2)
)
zhoneTacTestObjects.setObjects(
      *(("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneTacInterfaceIndex"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneTacTestMode"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneTacTestId"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneTacTestResultsTimeStarted"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneTacTestResultsTimeEnded"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneTacTestResultStatus"),
        ("ZHONE-CARD-DIAGNOSTICS-MIB", "zhoneTacTestResultsOutput"))
)
if mibBuilder.loadTexts:
    zhoneTacTestObjects.setStatus("current")


# Notification objects

zhoneRingerStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 13, 0, 1)
)
if mibBuilder.loadTexts:
    zhoneRingerStatusAlarm.setStatus(
        "current"
    )

zhoneRingerBusFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 3, 13, 0, 2)
)
if mibBuilder.loadTexts:
    zhoneRingerBusFaultAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-CARD-DIAGNOSTICS-MIB",
    **{"zhoneCardDiagNextTable": zhoneCardDiagNextTable,
       "zhoneCardDiagNextEntry": zhoneCardDiagNextEntry,
       "zhoneCardDiagNextIndex": zhoneCardDiagNextIndex,
       "zhoneCardDiagTable": zhoneCardDiagTable,
       "zhoneCardDiagEntry": zhoneCardDiagEntry,
       "zhoneCardDiagIndex": zhoneCardDiagIndex,
       "zhoneCardDiagType": zhoneCardDiagType,
       "zhoneCardDiagAction": zhoneCardDiagAction,
       "zhoneCardDiagRepetition": zhoneCardDiagRepetition,
       "zhoneCardDiagDuration": zhoneCardDiagDuration,
       "zhoneCardDiagResult": zhoneCardDiagResult,
       "zhoneCardDiagPassCount": zhoneCardDiagPassCount,
       "zhoneCardDiagFailCount": zhoneCardDiagFailCount,
       "zhoneCardDiagDetails": zhoneCardDiagDetails,
       "zhoneCardDiagStartTime": zhoneCardDiagStartTime,
       "zhoneCardDiagEndTime": zhoneCardDiagEndTime,
       "zhoneCardDiagRowStatus": zhoneCardDiagRowStatus,
       "zhoneTacTestTable": zhoneTacTestTable,
       "zhoneTacTestEntry": zhoneTacTestEntry,
       "zhoneTacIndex": zhoneTacIndex,
       "zhoneTacInterfaceIndex": zhoneTacInterfaceIndex,
       "zhoneTacTestMode": zhoneTacTestMode,
       "zhoneTacTestId": zhoneTacTestId,
       "zhoneTacTestParam1": zhoneTacTestParam1,
       "zhoneTacTestParam2": zhoneTacTestParam2,
       "zhoneTacTestParam3": zhoneTacTestParam3,
       "zhoneTacTestParam4": zhoneTacTestParam4,
       "zhoneTacTestParam5": zhoneTacTestParam5,
       "zhoneTacTestResultsTable": zhoneTacTestResultsTable,
       "zhoneTacTestResultsEntry": zhoneTacTestResultsEntry,
       "zhoneTacTestResultsTimeStarted": zhoneTacTestResultsTimeStarted,
       "zhoneTacTestResultsTimeEnded": zhoneTacTestResultsTimeEnded,
       "zhoneTacTestResultStatus": zhoneTacTestResultStatus,
       "zhoneTacTestResultsOutput": zhoneTacTestResultsOutput,
       "zhoneTacTestTraps": zhoneTacTestTraps,
       "zhoneRingerTraps": zhoneRingerTraps,
       "zhoneRingerStatusAlarm": zhoneRingerStatusAlarm,
       "zhoneRingerBusFaultAlarm": zhoneRingerBusFaultAlarm,
       "zhoneCardDiagnosticsModule": zhoneCardDiagnosticsModule,
       "zhoneCardDiagObjects": zhoneCardDiagObjects,
       "zhoneTacTestObjects": zhoneTacTestObjects}
)
