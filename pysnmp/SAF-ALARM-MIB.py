# SNMP MIB module (SAF-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SAF-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:17 2024
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

(alarmActiveDateAndTime,
 alarmActiveIndex,
 alarmListName,
 alarmModelIndex) = mibBuilder.importSymbols(
    "ALARM-MIB",
    "alarmActiveDateAndTime",
    "alarmActiveIndex",
    "alarmListName",
    "alarmModelIndex")

(IANAItuEventType,) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType")

(ItuTrendIndication,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuTrendIndication")

(tehnika,) = mibBuilder.importSymbols(
    "SAF-ENTERPRISE",
    "tehnika")

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

(AutonomousType,
 DateAndTime,
 DisplayString,
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

safAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118)
)
safAlarmMIB.setRevisions(
        ("2012-12-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SafAlarmProbableCause(Integer32, TextualConvention):
    status = "current"
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
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              500,
              501,
              502,
              503,
              504,
              505,
              506,
              507,
              508,
              509,
              510,
              511,
              512,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              521,
              522,
              523,
              524,
              525,
              526,
              527,
              528,
              529,
              530,
              531,
              532,
              533,
              534,
              535,
              536,
              537,
              538,
              539,
              540,
              541,
              542,
              543,
              544,
              545,
              546,
              547,
              548,
              549,
              550,
              551,
              552,
              553,
              554,
              555,
              600,
              601,
              602,
              603,
              604,
              605,
              606,
              607,
              608,
              609,
              610,
              611,
              612,
              613,
              614,
              615,
              1024,
              1025)
        )
    )
    namedValues = NamedValues(
        *(("aIS", 1),
          ("adapterError", 500),
          ("airCompressorFailure", 101),
          ("airConditioningFailure", 102),
          ("airDryerFailure", 103),
          ("antennaFailure", 71),
          ("applicationSubsystemFailture", 501),
          ("applicationSubsystemFailure", 158),
          ("authenticationFailure", 600),
          ("backplaneFailure", 51),
          ("bandwidthReduced", 201),
          ("bandwidthReducedX733", 502),
          ("batteryChargingFailure", 72),
          ("batteryDischarging", 104),
          ("batteryFailure", 105),
          ("breachOfConfidentiality", 601),
          ("broadcastChannelFailure", 21),
          ("cableTamper", 602),
          ("callEstablishmentError", 503),
          ("callSetUpFailure", 2),
          ("commercialPowerFailure", 106),
          ("communicationsProtocolError", 504),
          ("communicationsSubsystemFailure", 505),
          ("configurationOrCustomisationError", 159),
          ("configurationOrCustomizationError", 506),
          ("congestion", 202),
          ("congestionX733", 507),
          ("connectionEstablishmentError", 22),
          ("coolingFanFailure", 107),
          ("coolingSystemFailure", 134),
          ("corruptData", 153),
          ("coruptData", 508),
          ("cpuCyclesLimitExceeded", 509),
          ("dataSetOrModemError", 510),
          ("dataSetProblem", 52),
          ("databaseInconsistency", 160),
          ("degradedSignal", 3),
          ("degradedSignalX733", 511),
          ("delayedInformation", 603),
          ("demodulationFailure", 20),
          ("denialOfService", 604),
          ("diskFailure", 73),
          ("dteDceInterfaceError", 512),
          ("duplicateInformation", 605),
          ("enclosureDoorOpen", 118),
          ("enclosureDoorOpenX733", 513),
          ("engineFailure", 108),
          ("equipmentIdentifierDuplication", 53),
          ("equipmentMalfunction", 514),
          ("excessiveBER", 12),
          ("excessiveErrorRate", 203),
          ("excessiveResponseTime", 204),
          ("excessiveRetransmissionRate", 205),
          ("excessiveVibration", 515),
          ("explosiveGas", 119),
          ("externalEquipmentFailure", 135),
          ("externalIFDeviceProblem", 54),
          ("externalPointFailure", 136),
          ("farEndReceiverFailure", 4),
          ("fileError", 161),
          ("fileErrorX733", 516),
          ("fire", 120),
          ("fireDetected", 517),
          ("fireDetectorFailure", 109),
          ("flood", 121),
          ("framingError", 5),
          ("framingErrorX733", 518),
          ("frequencyHoppingFailure", 74),
          ("fuseFailure", 110),
          ("generatorFailure", 111),
          ("heatingVentCoolingSystemProblem", 519),
          ("highHumidity", 122),
          ("highTemperature", 123),
          ("highWind", 124),
          ("humidityUnacceptable", 520),
          ("iODeviceError", 75),
          ("iceBuildUp", 125),
          ("informationMissing", 606),
          ("informationModificationDetected", 607),
          ("informationOutOfSequence", 608),
          ("inputDeviceError", 522),
          ("inputOutputDeviceError", 521),
          ("intrusionDetection", 126),
          ("invalidMessageReceived", 23),
          ("keyExpired", 609),
          ("lanError", 523),
          ("leakDetected", 524),
          ("lineCardProblem", 55),
          ("localNodeTransmissionError", 24),
          ("localNodeTransmissionErrorX733", 525),
          ("lossOfFrame", 6),
          ("lossOfFrameX733", 526),
          ("lossOfMultiFrame", 16),
          ("lossOfPointer", 7),
          ("lossOfRealTimel", 157),
          ("lossOfRedundancy", 77),
          ("lossOfSignal", 8),
          ("lossOfSignalX733", 527),
          ("lossOfSynchronisation", 76),
          ("lowBatteryThreshold", 112),
          ("lowCablePressure", 129),
          ("lowFuel", 127),
          ("lowHumidity", 128),
          ("lowTemperatue", 130),
          ("lowWater", 131),
          ("materialSupplyExhausted", 528),
          ("memoryMismatch", 152),
          ("modulationFailure", 19),
          ("multiplexerProblem", 56),
          ("multiplexerProblemX733", 529),
          ("nEIdentifierDuplication", 57),
          ("nonRepudiationFailure", 610),
          ("other", 1024),
          ("ouputDeviceError", 531),
          ("outOfCPUCycles", 154),
          ("outOfHoursActivity", 611),
          ("outOfMemory", 162),
          ("outOfMemoryX733", 530),
          ("outOfService", 612),
          ("pathTraceMismatch", 13),
          ("payloadTypeMismatch", 9),
          ("performanceDegraded", 532),
          ("powerProblem", 58),
          ("powerProblems", 533),
          ("powerSupplyFailure", 78),
          ("pressureUnacceptable", 534),
          ("proceduralError", 613),
          ("processorProblem", 59),
          ("processorProblems", 535),
          ("protectingResourceFailure", 82),
          ("protectionMechanismFailure", 81),
          ("protectionPathFailure", 60),
          ("pumpFailure", 113),
          ("pumpFailureX733", 536),
          ("queueSizeExceeded", 537),
          ("realTimeClockFailure", 70),
          ("receiveFailure", 17),
          ("receiveFailureX733", 538),
          ("receiverFailure", 61),
          ("receiverFailureX733", 539),
          ("rectifierFailure", 114),
          ("rectifierHighVoltage", 115),
          ("rectifierLowFVoltage", 116),
          ("reducedLoggingCapability", 206),
          ("remoteAlarmInterface", 11),
          ("remoteNodeTransmissionError", 25),
          ("remoteNodeTransmissionErrorX733", 540),
          ("replaceableUnitMissing", 62),
          ("replaceableUnitProblem", 69),
          ("replaceableUnitTypeMismatch", 63),
          ("resourceAtOrNearingCapacity", 541),
          ("responseTimeExecessive", 542),
          ("retransmissionRateExcessive", 543),
          ("routingFailure", 26),
          ("safEnterpriseSpecific", 1025),
          ("sfwrDownloadFailure", 156),
          ("sfwrEnvironmentProblem", 155),
          ("signalLabelMismatch", 15),
          ("signalQualityEvaluationFailure", 79),
          ("smoke", 132),
          ("softwareError", 163),
          ("softwareErrorX733", 544),
          ("softwareProgramAbnormallyTerminated", 545),
          ("softwareProgramError", 546),
          ("storageCapacityProblem", 151),
          ("storageCapacityProblemX733", 547),
          ("synchronizationSourceMismatch", 64),
          ("systemResourcesOverload", 207),
          ("temperatureUnacceptable", 548),
          ("terminalProblem", 65),
          ("thresholdCrossed", 549),
          ("timeoutExpired", 164),
          ("timingProblem", 66),
          ("timingProblemX733", 550),
          ("toxicGas", 133),
          ("toxicLeakDetected", 551),
          ("tranceiverFailure", 80),
          ("transmissionError", 10),
          ("transmitFailure", 18),
          ("transmitFailureX733", 552),
          ("transmiterFailure", 553),
          ("transmitterFailure", 67),
          ("trunkCardProblem", 68),
          ("unauthorizedAccessAttempt", 614),
          ("unavailable", 14),
          ("underlayingResourceUnavailable", 165),
          ("underlyingResourceUnavailable", 554),
          ("unexpectedInformation", 615),
          ("ventilationsSystemFailure", 117),
          ("versionMismatch", 166),
          ("versionMismatchX733", 555))
    )



class SafPerceivedSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("cleared", 1),
          ("critical", 3),
          ("event", 7),
          ("indeterminate", 2),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



# MIB Managed Objects in the order of their OIDs

_SafAlarmNotifications_ObjectIdentity = ObjectIdentity
safAlarmNotifications = _SafAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 0)
)
_SafAlarmObjects_ObjectIdentity = ObjectIdentity
safAlarmObjects = _SafAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1)
)
_SafAlarmActive_ObjectIdentity = ObjectIdentity
safAlarmActive = _SafAlarmActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1)
)
_SafAlarmActiveLastChanged_Type = TimeTicks
_SafAlarmActiveLastChanged_Object = MibScalar
safAlarmActiveLastChanged = _SafAlarmActiveLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 1),
    _SafAlarmActiveLastChanged_Type()
)
safAlarmActiveLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveLastChanged.setStatus("current")
_SafAlarmActiveTable_Object = MibTable
safAlarmActiveTable = _SafAlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2)
)
if mibBuilder.loadTexts:
    safAlarmActiveTable.setStatus("current")
_SafAlarmActiveEntry_Object = MibTableRow
safAlarmActiveEntry = _SafAlarmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1)
)
safAlarmActiveEntry.setIndexNames(
    (0, "SAF-ALARM-MIB", "safAlarmActiveIndex"),
)
if mibBuilder.loadTexts:
    safAlarmActiveEntry.setStatus("current")


class _SafAlarmActiveIndex_Type(Unsigned32):
    """Custom type safAlarmActiveIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SafAlarmActiveIndex_Type.__name__ = "Unsigned32"
_SafAlarmActiveIndex_Object = MibTableColumn
safAlarmActiveIndex = _SafAlarmActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 1),
    _SafAlarmActiveIndex_Type()
)
safAlarmActiveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    safAlarmActiveIndex.setStatus("current")
_SafAlarmActiveManagedObj_Type = ObjectIdentifier
_SafAlarmActiveManagedObj_Object = MibTableColumn
safAlarmActiveManagedObj = _SafAlarmActiveManagedObj_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 2),
    _SafAlarmActiveManagedObj_Type()
)
safAlarmActiveManagedObj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveManagedObj.setStatus("current")
_SafAlarmActiveDateAndTime_Type = DateAndTime
_SafAlarmActiveDateAndTime_Object = MibTableColumn
safAlarmActiveDateAndTime = _SafAlarmActiveDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 3),
    _SafAlarmActiveDateAndTime_Type()
)
safAlarmActiveDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveDateAndTime.setStatus("current")
_SafAlarmActiveEventType_Type = IANAItuEventType
_SafAlarmActiveEventType_Object = MibTableColumn
safAlarmActiveEventType = _SafAlarmActiveEventType_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 4),
    _SafAlarmActiveEventType_Type()
)
safAlarmActiveEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveEventType.setStatus("current")
_SafAlarmActiveProbableCause_Type = SafAlarmProbableCause
_SafAlarmActiveProbableCause_Object = MibTableColumn
safAlarmActiveProbableCause = _SafAlarmActiveProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 5),
    _SafAlarmActiveProbableCause_Type()
)
safAlarmActiveProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveProbableCause.setStatus("current")
_SafAlarmActivePerceivedSeverity_Type = SafPerceivedSeverity
_SafAlarmActivePerceivedSeverity_Object = MibTableColumn
safAlarmActivePerceivedSeverity = _SafAlarmActivePerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 6),
    _SafAlarmActivePerceivedSeverity_Type()
)
safAlarmActivePerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActivePerceivedSeverity.setStatus("current")
_SafAlarmActiveThresholdTrigered_Type = Integer32
_SafAlarmActiveThresholdTrigered_Object = MibTableColumn
safAlarmActiveThresholdTrigered = _SafAlarmActiveThresholdTrigered_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 7),
    _SafAlarmActiveThresholdTrigered_Type()
)
safAlarmActiveThresholdTrigered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveThresholdTrigered.setStatus("current")
_SafAlarmActiveThresholdValue_Type = Integer32
_SafAlarmActiveThresholdValue_Object = MibTableColumn
safAlarmActiveThresholdValue = _SafAlarmActiveThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 8),
    _SafAlarmActiveThresholdValue_Type()
)
safAlarmActiveThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveThresholdValue.setStatus("current")
_SafAlarmActiveThresholdTTrigered_Type = DisplayString
_SafAlarmActiveThresholdTTrigered_Object = MibTableColumn
safAlarmActiveThresholdTTrigered = _SafAlarmActiveThresholdTTrigered_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 9),
    _SafAlarmActiveThresholdTTrigered_Type()
)
safAlarmActiveThresholdTTrigered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveThresholdTTrigered.setStatus("current")
_SafAlarmActiveThresholdTValue_Type = DisplayString
_SafAlarmActiveThresholdTValue_Object = MibTableColumn
safAlarmActiveThresholdTValue = _SafAlarmActiveThresholdTValue_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 10),
    _SafAlarmActiveThresholdTValue_Type()
)
safAlarmActiveThresholdTValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveThresholdTValue.setStatus("current")
_SafAlarmActiveAdditionalText_Type = SnmpAdminString
_SafAlarmActiveAdditionalText_Object = MibTableColumn
safAlarmActiveAdditionalText = _SafAlarmActiveAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 2, 1, 11),
    _SafAlarmActiveAdditionalText_Type()
)
safAlarmActiveAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveAdditionalText.setStatus("current")
_SafAlarmActiveLastChangedDateAndTime_Type = DateAndTime
_SafAlarmActiveLastChangedDateAndTime_Object = MibScalar
safAlarmActiveLastChangedDateAndTime = _SafAlarmActiveLastChangedDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 1, 1, 3),
    _SafAlarmActiveLastChangedDateAndTime_Type()
)
safAlarmActiveLastChangedDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safAlarmActiveLastChangedDateAndTime.setStatus("current")
_SafAlarmConformance_ObjectIdentity = ObjectIdentity
safAlarmConformance = _SafAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 3)
)
_SafAlarmGroups_ObjectIdentity = ObjectIdentity
safAlarmGroups = _SafAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 3, 2)
)

# Managed Objects groups

safAlarmActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 3, 2, 1)
)
safAlarmActiveGroup.setObjects(
      *(("SAF-ALARM-MIB", "safAlarmActiveLastChanged"),
        ("SAF-ALARM-MIB", "safAlarmActiveLastChangedDateAndTime"),
        ("SAF-ALARM-MIB", "safAlarmActiveManagedObj"),
        ("SAF-ALARM-MIB", "safAlarmActiveDateAndTime"),
        ("SAF-ALARM-MIB", "safAlarmActiveEventType"),
        ("SAF-ALARM-MIB", "safAlarmActiveProbableCause"),
        ("SAF-ALARM-MIB", "safAlarmActivePerceivedSeverity"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdTrigered"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdValue"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdTTrigered"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdTValue"),
        ("SAF-ALARM-MIB", "safAlarmActiveAdditionalText"))
)
if mibBuilder.loadTexts:
    safAlarmActiveGroup.setStatus("current")


# Notification objects

safAlarmActiveState = NotificationType(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 0, 2)
)
safAlarmActiveState.setObjects(
      *(("SAF-ALARM-MIB", "safAlarmActiveManagedObj"),
        ("SAF-ALARM-MIB", "safAlarmActiveDateAndTime"),
        ("SAF-ALARM-MIB", "safAlarmActiveEventType"),
        ("SAF-ALARM-MIB", "safAlarmActiveProbableCause"),
        ("SAF-ALARM-MIB", "safAlarmActivePerceivedSeverity"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdTrigered"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdValue"),
        ("SAF-ALARM-MIB", "safAlarmActiveAdditionalText"))
)
if mibBuilder.loadTexts:
    safAlarmActiveState.setStatus(
        "current"
    )

safAlarmActiveTState = NotificationType(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 0, 3)
)
safAlarmActiveTState.setObjects(
      *(("SAF-ALARM-MIB", "safAlarmActiveManagedObj"),
        ("SAF-ALARM-MIB", "safAlarmActiveDateAndTime"),
        ("SAF-ALARM-MIB", "safAlarmActiveEventType"),
        ("SAF-ALARM-MIB", "safAlarmActiveProbableCause"),
        ("SAF-ALARM-MIB", "safAlarmActivePerceivedSeverity"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdTTrigered"),
        ("SAF-ALARM-MIB", "safAlarmActiveThresholdTValue"),
        ("SAF-ALARM-MIB", "safAlarmActiveAdditionalText"))
)
if mibBuilder.loadTexts:
    safAlarmActiveTState.setStatus(
        "current"
    )

safAlarmClearState = NotificationType(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 0, 4)
)
safAlarmClearState.setObjects(
    ("SAF-ALARM-MIB", "safAlarmActiveManagedObj")
)
if mibBuilder.loadTexts:
    safAlarmClearState.setStatus(
        "deprecated"
    )


# Notifications groups

safAlarmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 3, 2, 2)
)
safAlarmNotificationsGroup.setObjects(
      *(("SAF-ALARM-MIB", "safAlarmActiveState"),
        ("SAF-ALARM-MIB", "safAlarmActiveTState"),
        ("SAF-ALARM-MIB", "safAlarmClearState"))
)
if mibBuilder.loadTexts:
    safAlarmNotificationsGroup.setStatus(
        "deprecated"
    )

safAlarmNotificationsGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7571, 100, 118, 3, 2, 3)
)
safAlarmNotificationsGroup1.setObjects(
      *(("SAF-ALARM-MIB", "safAlarmActiveState"),
        ("SAF-ALARM-MIB", "safAlarmActiveTState"))
)
if mibBuilder.loadTexts:
    safAlarmNotificationsGroup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAF-ALARM-MIB",
    **{"SafAlarmProbableCause": SafAlarmProbableCause,
       "SafPerceivedSeverity": SafPerceivedSeverity,
       "safAlarmMIB": safAlarmMIB,
       "safAlarmNotifications": safAlarmNotifications,
       "safAlarmActiveState": safAlarmActiveState,
       "safAlarmActiveTState": safAlarmActiveTState,
       "safAlarmClearState": safAlarmClearState,
       "safAlarmObjects": safAlarmObjects,
       "safAlarmActive": safAlarmActive,
       "safAlarmActiveLastChanged": safAlarmActiveLastChanged,
       "safAlarmActiveTable": safAlarmActiveTable,
       "safAlarmActiveEntry": safAlarmActiveEntry,
       "safAlarmActiveIndex": safAlarmActiveIndex,
       "safAlarmActiveManagedObj": safAlarmActiveManagedObj,
       "safAlarmActiveDateAndTime": safAlarmActiveDateAndTime,
       "safAlarmActiveEventType": safAlarmActiveEventType,
       "safAlarmActiveProbableCause": safAlarmActiveProbableCause,
       "safAlarmActivePerceivedSeverity": safAlarmActivePerceivedSeverity,
       "safAlarmActiveThresholdTrigered": safAlarmActiveThresholdTrigered,
       "safAlarmActiveThresholdValue": safAlarmActiveThresholdValue,
       "safAlarmActiveThresholdTTrigered": safAlarmActiveThresholdTTrigered,
       "safAlarmActiveThresholdTValue": safAlarmActiveThresholdTValue,
       "safAlarmActiveAdditionalText": safAlarmActiveAdditionalText,
       "safAlarmActiveLastChangedDateAndTime": safAlarmActiveLastChangedDateAndTime,
       "safAlarmConformance": safAlarmConformance,
       "safAlarmGroups": safAlarmGroups,
       "safAlarmActiveGroup": safAlarmActiveGroup,
       "safAlarmNotificationsGroup": safAlarmNotificationsGroup,
       "safAlarmNotificationsGroup1": safAlarmNotificationsGroup1}
)
