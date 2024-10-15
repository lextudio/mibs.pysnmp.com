# SNMP MIB module (SUN-PLATFORM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUN-PLATFORM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:35 2024
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

(entLogicalEntry,
 entLogicalIndex,
 entPhysicalEntry,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLogicalEntry",
    "entLogicalIndex",
    "entPhysicalEntry",
    "entPhysicalIndex")

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
 RowPointer,
 RowStatus,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

sunPlatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101)
)
sunPlatMIB.setRevisions(
        ("2002-11-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SunPlatLogAdministrativeState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )



class SunPlatAdministrativeState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("shuttingDown", 3),
          ("unlocked", 2))
    )



class SunPlatOperationalState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )



class SunPlatAlarmPerceivedSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 6),
          ("critical", 2),
          ("indeterminate", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )



class SunPlatAlarmStatus(Integer32, TextualConvention):
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
        *(("cleared", 7),
          ("critical", 1),
          ("indeterminate", 4),
          ("major", 2),
          ("minor", 3),
          ("pending", 6),
          ("warning", 5))
    )



class SunPlatEquipmentHolderType(Integer32, TextualConvention):
    status = "current"
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
        *(("bay", 1),
          ("drawer", 3),
          ("rack", 5),
          ("shelf", 2),
          ("slot", 4))
    )



class SunPlatEquipmentHolderStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("holderEmpty", 1),
          ("inTheAcceptableList", 2),
          ("notInTheAcceptableList", 3),
          ("unknownType", 4))
    )



class SunPlatEquipmentHolderPower(Integer32, TextualConvention):
    status = "current"
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
        *(("other", 1),
          ("powerOff", 3),
          ("powerOn", 4),
          ("unknown", 2))
    )



class SunPlatCircuitPackAvailabilityStatus(Bits, TextualConvention):
    status = "current"


class SunPlatProbableCause(Integer32, TextualConvention):
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
              167,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303)
        )
    )
    namedValues = NamedValues(
        *(("aIS", 1),
          ("adapterError", 256),
          ("airCompressorFailure", 101),
          ("airConditioningFailure", 102),
          ("airDryerFailure", 103),
          ("antennaFailure", 71),
          ("applicationSubsystemFailure", 159),
          ("authenticationFailure", 288),
          ("backplaneFailure", 51),
          ("bandwidthReduced", 201),
          ("batteryChargingFailure", 72),
          ("batteryDischarging", 104),
          ("batteryFailure", 105),
          ("breachOfConfidentiality", 289),
          ("broadcastChannelFailure", 21),
          ("cableTamper", 290),
          ("callEstablishmentError", 257),
          ("callSetUpFailure", 2),
          ("commercialPowerFailure", 106),
          ("communicationsProtocolError", 258),
          ("communicationsSubsystemFailure", 259),
          ("configurationOrCustomisationError", 160),
          ("configurationOrCustomizationError", 260),
          ("congestion", 202),
          ("connectionEstablishmentError", 22),
          ("coolingFanFailure", 107),
          ("coolingSystemFailure", 134),
          ("corruptData", 153),
          ("cpuCyclesLimitExceeded", 261),
          ("dataSetOrModemError", 262),
          ("dataSetProblem", 52),
          ("databaseInconsistency", 161),
          ("degradedSignal", 3),
          ("delayedInformation", 291),
          ("demodulationFailure", 20),
          ("denialOfService", 292),
          ("diskFailure", 73),
          ("dteDceInterfaceError", 263),
          ("duplicateInformation", 293),
          ("enclosureDoorOpen", 118),
          ("engineFailure", 108),
          ("equipmentIdentifierDuplication", 53),
          ("equipmentMalfunction", 264),
          ("excessiveBER", 12),
          ("excessiveErrorRate", 203),
          ("excessiveResponseTime", 204),
          ("excessiveRetransmissionRate", 205),
          ("excessiveVibration", 265),
          ("explosiveGas", 119),
          ("externalEquipmentFailure", 135),
          ("externalIFDeviceProblem", 54),
          ("externalPointFailure", 136),
          ("farEndReceiverFailure", 4),
          ("fileError", 162),
          ("fire", 120),
          ("fireDetected", 266),
          ("fireDetectorFailure", 109),
          ("flood", 121),
          ("floodDetected", 267),
          ("framingError", 5),
          ("frequencyHoppingFailure", 74),
          ("fuseFailure", 110),
          ("generatorFailure", 111),
          ("heatingVentCoolingSystemProblem", 268),
          ("highHumidity", 122),
          ("highTemperature", 123),
          ("highWind", 124),
          ("humidityUnacceptable", 269),
          ("iODeviceError", 75),
          ("iceBuildUp", 125),
          ("informationMissing", 294),
          ("informationModificationDetected", 295),
          ("informationOutOfSequence", 296),
          ("inputDeviceError", 271),
          ("inputOutputDeviceError", 270),
          ("intrusionDetection", 126),
          ("invalidMessageReceived", 23),
          ("keyExpired", 297),
          ("lanError", 272),
          ("leakDetected", 273),
          ("lineCardProblem", 55),
          ("localNodeTransmissionError", 24),
          ("lossOfFrame", 6),
          ("lossOfMultiFrame", 16),
          ("lossOfPointer", 7),
          ("lossOfRealTime", 157),
          ("lossOfRedundancy", 77),
          ("lossOfSignal", 8),
          ("lossOfSynchronisation", 76),
          ("lowBatteryThreshold", 112),
          ("lowCablePressure", 129),
          ("lowFuel", 127),
          ("lowHumidity", 128),
          ("lowTemperature", 130),
          ("lowWater", 131),
          ("materialSupplyExhausted", 274),
          ("memoryMismatch", 152),
          ("modulationFailure", 19),
          ("multiplexerProblem", 56),
          ("nEIdentifierDuplication", 57),
          ("nonRepudiationFailure", 298),
          ("other", 255),
          ("ouputDeviceError", 275),
          ("outOfCPUCycles", 154),
          ("outOfHoursActivity", 299),
          ("outOfMemory", 163),
          ("outOfService", 300),
          ("pathTraceMismatch", 13),
          ("payloadTypeMismatch", 9),
          ("performanceDegraded", 276),
          ("powerProblem", 58),
          ("powerSupplyFailure", 78),
          ("pressureUnacceptable", 277),
          ("proceduralError", 301),
          ("processorProblem", 59),
          ("protectingResourceFailure", 82),
          ("protectionMechanismFailure", 81),
          ("protectionPathFailure", 60),
          ("pumpFailure", 113),
          ("queueSizeExceeded", 278),
          ("realTimeClockFailure", 70),
          ("receiveFailure", 17),
          ("receiverFailure", 61),
          ("rectifierFailure", 114),
          ("rectifierHighVoltage", 115),
          ("rectifierLowFVoltage", 116),
          ("reducedLoggingCapability", 206),
          ("reinitialized", 158),
          ("remoteAlarmInterface", 11),
          ("remoteNodeTransmissionError", 25),
          ("replaceableUnitMissing", 62),
          ("replaceableUnitProblem", 69),
          ("replaceableUnitTypeMismatch", 63),
          ("resourceAtOrNearingCapacity", 279),
          ("responseTimeExecessive", 280),
          ("retransmissionRateExcessive", 281),
          ("routingFailure", 26),
          ("sfwrDownloadFailure", 156),
          ("sfwrEnvironmentProblem", 155),
          ("signalLabelMismatch", 15),
          ("signalQualityEvaluationFailure", 79),
          ("smoke", 132),
          ("softwareError", 164),
          ("softwareProgramAbnormallyTerminated", 282),
          ("softwareProgramError", 283),
          ("storageCapacityProblem", 151),
          ("synchronizationSourceMismatch", 64),
          ("systemResourcesOverload", 207),
          ("temperatureUnacceptable", 284),
          ("terminalProblem", 65),
          ("thresholdCrossed", 285),
          ("timeoutExpired", 165),
          ("timingProblem", 66),
          ("toxicGas", 133),
          ("toxicLeakDetected", 286),
          ("tranceiverFailure", 80),
          ("transmissionError", 10),
          ("transmitFailure", 18),
          ("transmitterFailure", 67),
          ("trunkCardProblem", 68),
          ("unauthorizedAccessAttempt", 302),
          ("unavailable", 14),
          ("underlayingResourceUnavailable", 166),
          ("underlyingResourceUnavailable", 287),
          ("unexpectedInformation", 303),
          ("ventilationsSystemFailure", 117),
          ("versionMismatch", 167))
    )



class SunPlatPhysicalClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("other", 1),
          ("watchdog", 3))
    )



class SunPlatSensorClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("binary", 1),
          ("discrete", 3),
          ("numeric", 2))
    )



class SunPlatSensorType(Integer32, TextualConvention):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("airFlow", 13),
          ("counter", 7),
          ("current", 5),
          ("humidity", 10),
          ("lock", 9),
          ("other", 1),
          ("presence", 12),
          ("smokeDetection", 11),
          ("switch", 8),
          ("tachometer", 6),
          ("temperature", 3),
          ("unknown", 2),
          ("voltage", 4))
    )



class SunPlatBaseUnits(Integer32, TextualConvention):
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
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
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
              66)
        )
    )
    namedValues = NamedValues(
        *(("amps", 7),
          ("becquerels", 53),
          ("bits", 61),
          ("bytes", 62),
          ("candelas", 15),
          ("cfm", 19),
          ("colorTemperatureDegK", 60),
          ("coulombs", 10),
          ("cubicCentimeters", 33),
          ("cubicFeet", 31),
          ("cubicInches", 30),
          ("cubicMeters", 34),
          ("cycles", 40),
          ("dBA", 56),
          ("days", 25),
          ("dbC", 57),
          ("decibels", 55),
          ("degC", 3),
          ("degF", 4),
          ("degK", 5),
          ("doubleWords", 64),
          ("farads", 49),
          ("feet", 29),
          ("fluidOunces", 36),
          ("footPounds", 44),
          ("gauss", 46),
          ("gilberts", 47),
          ("gravities", 41),
          ("grays", 58),
          ("henries", 48),
          ("hertz", 21),
          ("hours", 24),
          ("inches", 28),
          ("joules", 9),
          ("kPa", 16),
          ("liters", 35),
          ("lumens", 13),
          ("lux", 14),
          ("meters", 32),
          ("mils", 27),
          ("minutes", 23),
          ("moles", 52),
          ("newtons", 18),
          ("nits", 12),
          ("ohms", 50),
          ("other", 1),
          ("ounceInches", 45),
          ("ounces", 42),
          ("percentage", 66),
          ("pounds", 43),
          ("ppm", 54),
          ("psi", 17),
          ("quadWords", 65),
          ("radians", 37),
          ("revolutions", 39),
          ("rpm", 20),
          ("seconds", 22),
          ("siemens", 51),
          ("sieverts", 59),
          ("steradians", 38),
          ("unknown", 2),
          ("va", 11),
          ("volts", 6),
          ("watts", 8),
          ("weeks", 26),
          ("words", 63))
    )



class SunPlatRateUnits(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("perDay", 7),
          ("perHour", 6),
          ("perMicroSecond", 2),
          ("perMilliSecond", 3),
          ("perMinute", 5),
          ("perMonth", 9),
          ("perSecond", 4),
          ("perWeek", 8),
          ("perYear", 10))
    )



class SunPlatNumericSensorEnabledThresholds(Bits, TextualConvention):
    status = "current"


class SunPlatNumericSensorThresholdResetAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )



class SunPlatAlarmType(Integer32, TextualConvention):
    status = "current"
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
        *(("audible", 2),
          ("motion", 4),
          ("other", 1),
          ("switch", 5),
          ("visible", 3))
    )



class SunPlatAlarmState(Integer32, TextualConvention):
    status = "current"
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
        *(("alternating", 4),
          ("off", 2),
          ("steady", 3),
          ("unknown", 1))
    )



class SunPlatAlarmUrgency(Integer32, TextualConvention):
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
        *(("critical", 6),
          ("informational", 4),
          ("nonCritical", 5),
          ("notSupported", 3),
          ("other", 2),
          ("unknown", 1),
          ("unrecoverable", 7))
    )



class SunPlatWatchdogAction(Integer32, TextualConvention):
    status = "current"
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
        *(("statusOnly", 1),
          ("systemInterrupt", 2),
          ("systemPowerCycle", 5),
          ("systemPowerOff", 4),
          ("systemReset", 3))
    )



class SunPlatWatchdogMonitoredEntity(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("application", 8),
          ("biosBootProcess", 7),
          ("firmwareBootProcess", 6),
          ("operatingSystem", 3),
          ("operatingSystemBootProcess", 4),
          ("operatingSystemShutdownProcess", 5),
          ("other", 2),
          ("serviceProcessor", 9),
          ("unknown", 1))
    )



class SunPlatPowerSupplyClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("battery", 3),
          ("other", 1),
          ("powerSupply", 2))
    )



class SunPlatFanClass(Integer32, TextualConvention):
    status = "current"
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
        *(("fan", 2),
          ("heatPipe", 4),
          ("other", 1),
          ("refrigeration", 3))
    )



class SunPlatBatteryStatus(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("charging", 6),
          ("chargingAndCritical", 9),
          ("chargingAndHigh", 7),
          ("chargingAndLow", 8),
          ("critical", 5),
          ("fullyCharged", 3),
          ("low", 4),
          ("other", 1),
          ("partiallyCharged", 11),
          ("undefined", 10),
          ("unknown", 2))
    )



class SunPlatUnitaryComputerSystemPowerState(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("fullPower", 2),
          ("hibernate", 9),
          ("powerCycle", 6),
          ("powerOff", 7),
          ("psLowPower", 3),
          ("psOther", 5),
          ("psStandby", 4),
          ("psWarning", 8),
          ("reset", 11),
          ("softOff", 10),
          ("unknown", 1))
    )



class SunPlatUnitaryComputerSystemApplicableSetting(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defaultSetting", 1),
          ("specifiedSetting", 2))
    )



class SunPlatLogicalClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminDomain", 3),
          ("computerSystem", 2),
          ("other", 1))
    )



class SunPlatLogicalStatus(Integer32, TextualConvention):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("lostComm", 12),
          ("noContact", 11),
          ("nonRecover", 10),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopped", 13),
          ("stopping", 7),
          ("stressed", 9),
          ("unknown", 4))
    )



class SunPlatIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class SunPlatPercentage(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_SunFire_ObjectIdentity = ObjectIdentity
sunFire = _SunFire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 70)
)
_SunPlatMIBObjects_ObjectIdentity = ObjectIdentity
sunPlatMIBObjects = _SunPlatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1)
)
_SunPlatMIBPhysicalObjects_ObjectIdentity = ObjectIdentity
sunPlatMIBPhysicalObjects = _SunPlatMIBPhysicalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1)
)
_SunPlatStartTime_Type = DateAndTime
_SunPlatStartTime_Object = MibScalar
sunPlatStartTime = _SunPlatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 1),
    _SunPlatStartTime_Type()
)
sunPlatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatStartTime.setStatus("current")
_SunPlatEquipmentTable_Object = MibTable
sunPlatEquipmentTable = _SunPlatEquipmentTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sunPlatEquipmentTable.setStatus("current")
_SunPlatEquipmentEntry_Object = MibTableRow
sunPlatEquipmentEntry = _SunPlatEquipmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sunPlatEquipmentEntry.setStatus("current")
_SunPlatEquipmentAdministrativeState_Type = SunPlatAdministrativeState
_SunPlatEquipmentAdministrativeState_Object = MibTableColumn
sunPlatEquipmentAdministrativeState = _SunPlatEquipmentAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 2, 1, 1),
    _SunPlatEquipmentAdministrativeState_Type()
)
sunPlatEquipmentAdministrativeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatEquipmentAdministrativeState.setStatus("current")
_SunPlatEquipmentOperationalState_Type = SunPlatOperationalState
_SunPlatEquipmentOperationalState_Object = MibTableColumn
sunPlatEquipmentOperationalState = _SunPlatEquipmentOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 2, 1, 2),
    _SunPlatEquipmentOperationalState_Type()
)
sunPlatEquipmentOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatEquipmentOperationalState.setStatus("current")
_SunPlatEquipmentAlarmStatus_Type = SunPlatAlarmStatus
_SunPlatEquipmentAlarmStatus_Object = MibTableColumn
sunPlatEquipmentAlarmStatus = _SunPlatEquipmentAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 2, 1, 3),
    _SunPlatEquipmentAlarmStatus_Type()
)
sunPlatEquipmentAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatEquipmentAlarmStatus.setStatus("current")


class _SunPlatEquipmentUnknownStatus_Type(TruthValue):
    """Custom type sunPlatEquipmentUnknownStatus based on TruthValue"""


_SunPlatEquipmentUnknownStatus_Object = MibTableColumn
sunPlatEquipmentUnknownStatus = _SunPlatEquipmentUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 2, 1, 4),
    _SunPlatEquipmentUnknownStatus_Type()
)
sunPlatEquipmentUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatEquipmentUnknownStatus.setStatus("current")
_SunPlatEquipmentLocationName_Type = SnmpAdminString
_SunPlatEquipmentLocationName_Object = MibTableColumn
sunPlatEquipmentLocationName = _SunPlatEquipmentLocationName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 2, 1, 5),
    _SunPlatEquipmentLocationName_Type()
)
sunPlatEquipmentLocationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatEquipmentLocationName.setStatus("current")
_SunPlatEquipmentHolderTable_Object = MibTable
sunPlatEquipmentHolderTable = _SunPlatEquipmentHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sunPlatEquipmentHolderTable.setStatus("current")
_SunPlatEquipmentHolderEntry_Object = MibTableRow
sunPlatEquipmentHolderEntry = _SunPlatEquipmentHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 3, 1)
)
sunPlatEquipmentHolderEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sunPlatEquipmentHolderEntry.setStatus("current")
_SunPlatEquipmentHolderType_Type = SunPlatEquipmentHolderType
_SunPlatEquipmentHolderType_Object = MibTableColumn
sunPlatEquipmentHolderType = _SunPlatEquipmentHolderType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 3, 1, 1),
    _SunPlatEquipmentHolderType_Type()
)
sunPlatEquipmentHolderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatEquipmentHolderType.setStatus("current")
_SunPlatEquipmentHolderAcceptableTypes_Type = SnmpAdminString
_SunPlatEquipmentHolderAcceptableTypes_Object = MibTableColumn
sunPlatEquipmentHolderAcceptableTypes = _SunPlatEquipmentHolderAcceptableTypes_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 3, 1, 2),
    _SunPlatEquipmentHolderAcceptableTypes_Type()
)
sunPlatEquipmentHolderAcceptableTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatEquipmentHolderAcceptableTypes.setStatus("current")
_SunPlatEquipmentHolderStatus_Type = SunPlatEquipmentHolderStatus
_SunPlatEquipmentHolderStatus_Object = MibTableColumn
sunPlatEquipmentHolderStatus = _SunPlatEquipmentHolderStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 3, 1, 3),
    _SunPlatEquipmentHolderStatus_Type()
)
sunPlatEquipmentHolderStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatEquipmentHolderStatus.setStatus("current")
_SunPlatEquipmentHolderPowered_Type = SunPlatEquipmentHolderPower
_SunPlatEquipmentHolderPowered_Object = MibTableColumn
sunPlatEquipmentHolderPowered = _SunPlatEquipmentHolderPowered_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 3, 1, 4),
    _SunPlatEquipmentHolderPowered_Type()
)
sunPlatEquipmentHolderPowered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatEquipmentHolderPowered.setStatus("current")
_SunPlatCircuitPackTable_Object = MibTable
sunPlatCircuitPackTable = _SunPlatCircuitPackTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sunPlatCircuitPackTable.setStatus("current")
_SunPlatCircuitPackEntry_Object = MibTableRow
sunPlatCircuitPackEntry = _SunPlatCircuitPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 4, 1)
)
sunPlatCircuitPackEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sunPlatCircuitPackEntry.setStatus("current")
_SunPlatCircuitPackType_Type = SnmpAdminString
_SunPlatCircuitPackType_Object = MibTableColumn
sunPlatCircuitPackType = _SunPlatCircuitPackType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 4, 1, 1),
    _SunPlatCircuitPackType_Type()
)
sunPlatCircuitPackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatCircuitPackType.setStatus("current")
_SunPlatCircuitPackAvailabilityStatus_Type = SunPlatCircuitPackAvailabilityStatus
_SunPlatCircuitPackAvailabilityStatus_Object = MibTableColumn
sunPlatCircuitPackAvailabilityStatus = _SunPlatCircuitPackAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 4, 1, 2),
    _SunPlatCircuitPackAvailabilityStatus_Type()
)
sunPlatCircuitPackAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatCircuitPackAvailabilityStatus.setStatus("current")
_SunPlatCircuitPackReplaceable_Type = TruthValue
_SunPlatCircuitPackReplaceable_Object = MibTableColumn
sunPlatCircuitPackReplaceable = _SunPlatCircuitPackReplaceable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 4, 1, 3),
    _SunPlatCircuitPackReplaceable_Type()
)
sunPlatCircuitPackReplaceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatCircuitPackReplaceable.setStatus("current")
_SunPlatCircuitPackHotSwappable_Type = TruthValue
_SunPlatCircuitPackHotSwappable_Object = MibTableColumn
sunPlatCircuitPackHotSwappable = _SunPlatCircuitPackHotSwappable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 4, 1, 4),
    _SunPlatCircuitPackHotSwappable_Type()
)
sunPlatCircuitPackHotSwappable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatCircuitPackHotSwappable.setStatus("current")
_SunPlatPhysicalTable_Object = MibTable
sunPlatPhysicalTable = _SunPlatPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 5)
)
if mibBuilder.loadTexts:
    sunPlatPhysicalTable.setStatus("current")
_SunPlatPhysicalEntry_Object = MibTableRow
sunPlatPhysicalEntry = _SunPlatPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 5, 1)
)
sunPlatPhysicalEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sunPlatPhysicalEntry.setStatus("current")
_SunPlatPhysicalClass_Type = SunPlatPhysicalClass
_SunPlatPhysicalClass_Object = MibTableColumn
sunPlatPhysicalClass = _SunPlatPhysicalClass_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 5, 1, 1),
    _SunPlatPhysicalClass_Type()
)
sunPlatPhysicalClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatPhysicalClass.setStatus("current")
_SunPlatSensorTable_Object = MibTable
sunPlatSensorTable = _SunPlatSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 6)
)
if mibBuilder.loadTexts:
    sunPlatSensorTable.setStatus("current")
_SunPlatSensorEntry_Object = MibTableRow
sunPlatSensorEntry = _SunPlatSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 6, 1)
)
sunPlatSensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sunPlatSensorEntry.setStatus("current")
_SunPlatSensorClass_Type = SunPlatSensorClass
_SunPlatSensorClass_Object = MibTableColumn
sunPlatSensorClass = _SunPlatSensorClass_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 6, 1, 1),
    _SunPlatSensorClass_Type()
)
sunPlatSensorClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatSensorClass.setStatus("current")
_SunPlatSensorType_Type = SunPlatSensorType
_SunPlatSensorType_Object = MibTableColumn
sunPlatSensorType = _SunPlatSensorType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 6, 1, 2),
    _SunPlatSensorType_Type()
)
sunPlatSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatSensorType.setStatus("current")
_SunPlatSensorLatency_Type = Unsigned32
_SunPlatSensorLatency_Object = MibTableColumn
sunPlatSensorLatency = _SunPlatSensorLatency_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 6, 1, 3),
    _SunPlatSensorLatency_Type()
)
sunPlatSensorLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatSensorLatency.setStatus("current")
if mibBuilder.loadTexts:
    sunPlatSensorLatency.setUnits("milliseconds")
_SunPlatBinarySensorTable_Object = MibTable
sunPlatBinarySensorTable = _SunPlatBinarySensorTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 7)
)
if mibBuilder.loadTexts:
    sunPlatBinarySensorTable.setStatus("current")
_SunPlatBinarySensorEntry_Object = MibTableRow
sunPlatBinarySensorEntry = _SunPlatBinarySensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 7, 1)
)
sunPlatBinarySensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sunPlatBinarySensorEntry.setStatus("current")
_SunPlatBinarySensorCurrent_Type = TruthValue
_SunPlatBinarySensorCurrent_Object = MibTableColumn
sunPlatBinarySensorCurrent = _SunPlatBinarySensorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 7, 1, 1),
    _SunPlatBinarySensorCurrent_Type()
)
sunPlatBinarySensorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatBinarySensorCurrent.setStatus("current")
_SunPlatBinarySensorExpected_Type = TruthValue
_SunPlatBinarySensorExpected_Object = MibTableColumn
sunPlatBinarySensorExpected = _SunPlatBinarySensorExpected_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 7, 1, 2),
    _SunPlatBinarySensorExpected_Type()
)
sunPlatBinarySensorExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatBinarySensorExpected.setStatus("current")
_SunPlatBinarySensorInterpretTrue_Type = SnmpAdminString
_SunPlatBinarySensorInterpretTrue_Object = MibTableColumn
sunPlatBinarySensorInterpretTrue = _SunPlatBinarySensorInterpretTrue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 7, 1, 3),
    _SunPlatBinarySensorInterpretTrue_Type()
)
sunPlatBinarySensorInterpretTrue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatBinarySensorInterpretTrue.setStatus("current")
_SunPlatBinarySensorInterpretFalse_Type = SnmpAdminString
_SunPlatBinarySensorInterpretFalse_Object = MibTableColumn
sunPlatBinarySensorInterpretFalse = _SunPlatBinarySensorInterpretFalse_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 7, 1, 4),
    _SunPlatBinarySensorInterpretFalse_Type()
)
sunPlatBinarySensorInterpretFalse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatBinarySensorInterpretFalse.setStatus("current")
_SunPlatNumericSensorTable_Object = MibTable
sunPlatNumericSensorTable = _SunPlatNumericSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8)
)
if mibBuilder.loadTexts:
    sunPlatNumericSensorTable.setStatus("current")
_SunPlatNumericSensorEntry_Object = MibTableRow
sunPlatNumericSensorEntry = _SunPlatNumericSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1)
)
sunPlatNumericSensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sunPlatNumericSensorEntry.setStatus("current")
_SunPlatNumericSensorBaseUnits_Type = SunPlatBaseUnits
_SunPlatNumericSensorBaseUnits_Object = MibTableColumn
sunPlatNumericSensorBaseUnits = _SunPlatNumericSensorBaseUnits_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 1),
    _SunPlatNumericSensorBaseUnits_Type()
)
sunPlatNumericSensorBaseUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatNumericSensorBaseUnits.setStatus("current")
_SunPlatNumericSensorExponent_Type = Integer32
_SunPlatNumericSensorExponent_Object = MibTableColumn
sunPlatNumericSensorExponent = _SunPlatNumericSensorExponent_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 2),
    _SunPlatNumericSensorExponent_Type()
)
sunPlatNumericSensorExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatNumericSensorExponent.setStatus("current")
_SunPlatNumericSensorRateUnits_Type = SunPlatRateUnits
_SunPlatNumericSensorRateUnits_Object = MibTableColumn
sunPlatNumericSensorRateUnits = _SunPlatNumericSensorRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 3),
    _SunPlatNumericSensorRateUnits_Type()
)
sunPlatNumericSensorRateUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatNumericSensorRateUnits.setStatus("current")
_SunPlatNumericSensorCurrent_Type = Integer32
_SunPlatNumericSensorCurrent_Object = MibTableColumn
sunPlatNumericSensorCurrent = _SunPlatNumericSensorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 4),
    _SunPlatNumericSensorCurrent_Type()
)
sunPlatNumericSensorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatNumericSensorCurrent.setStatus("current")
_SunPlatNumericSensorNormalMin_Type = Integer32
_SunPlatNumericSensorNormalMin_Object = MibTableColumn
sunPlatNumericSensorNormalMin = _SunPlatNumericSensorNormalMin_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 5),
    _SunPlatNumericSensorNormalMin_Type()
)
sunPlatNumericSensorNormalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatNumericSensorNormalMin.setStatus("current")
_SunPlatNumericSensorNormalMax_Type = Integer32
_SunPlatNumericSensorNormalMax_Object = MibTableColumn
sunPlatNumericSensorNormalMax = _SunPlatNumericSensorNormalMax_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 6),
    _SunPlatNumericSensorNormalMax_Type()
)
sunPlatNumericSensorNormalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatNumericSensorNormalMax.setStatus("current")
_SunPlatNumericSensorAccuracy_Type = SunPlatPercentage
_SunPlatNumericSensorAccuracy_Object = MibTableColumn
sunPlatNumericSensorAccuracy = _SunPlatNumericSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 7),
    _SunPlatNumericSensorAccuracy_Type()
)
sunPlatNumericSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatNumericSensorAccuracy.setStatus("current")
_SunPlatNumericSensorLowerThresholdNonCritical_Type = Integer32
_SunPlatNumericSensorLowerThresholdNonCritical_Object = MibTableColumn
sunPlatNumericSensorLowerThresholdNonCritical = _SunPlatNumericSensorLowerThresholdNonCritical_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 8),
    _SunPlatNumericSensorLowerThresholdNonCritical_Type()
)
sunPlatNumericSensorLowerThresholdNonCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatNumericSensorLowerThresholdNonCritical.setStatus("current")
_SunPlatNumericSensorUpperThresholdNonCritical_Type = Integer32
_SunPlatNumericSensorUpperThresholdNonCritical_Object = MibTableColumn
sunPlatNumericSensorUpperThresholdNonCritical = _SunPlatNumericSensorUpperThresholdNonCritical_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 9),
    _SunPlatNumericSensorUpperThresholdNonCritical_Type()
)
sunPlatNumericSensorUpperThresholdNonCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatNumericSensorUpperThresholdNonCritical.setStatus("current")
_SunPlatNumericSensorLowerThresholdCritical_Type = Integer32
_SunPlatNumericSensorLowerThresholdCritical_Object = MibTableColumn
sunPlatNumericSensorLowerThresholdCritical = _SunPlatNumericSensorLowerThresholdCritical_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 10),
    _SunPlatNumericSensorLowerThresholdCritical_Type()
)
sunPlatNumericSensorLowerThresholdCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatNumericSensorLowerThresholdCritical.setStatus("current")
_SunPlatNumericSensorUpperThresholdCritical_Type = Integer32
_SunPlatNumericSensorUpperThresholdCritical_Object = MibTableColumn
sunPlatNumericSensorUpperThresholdCritical = _SunPlatNumericSensorUpperThresholdCritical_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 11),
    _SunPlatNumericSensorUpperThresholdCritical_Type()
)
sunPlatNumericSensorUpperThresholdCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatNumericSensorUpperThresholdCritical.setStatus("current")
_SunPlatNumericSensorLowerThresholdFatal_Type = Integer32
_SunPlatNumericSensorLowerThresholdFatal_Object = MibTableColumn
sunPlatNumericSensorLowerThresholdFatal = _SunPlatNumericSensorLowerThresholdFatal_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 12),
    _SunPlatNumericSensorLowerThresholdFatal_Type()
)
sunPlatNumericSensorLowerThresholdFatal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatNumericSensorLowerThresholdFatal.setStatus("current")
_SunPlatNumericSensorUpperThresholdFatal_Type = Integer32
_SunPlatNumericSensorUpperThresholdFatal_Object = MibTableColumn
sunPlatNumericSensorUpperThresholdFatal = _SunPlatNumericSensorUpperThresholdFatal_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 13),
    _SunPlatNumericSensorUpperThresholdFatal_Type()
)
sunPlatNumericSensorUpperThresholdFatal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatNumericSensorUpperThresholdFatal.setStatus("current")
_SunPlatNumericSensorHysteresis_Type = Unsigned32
_SunPlatNumericSensorHysteresis_Object = MibTableColumn
sunPlatNumericSensorHysteresis = _SunPlatNumericSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 14),
    _SunPlatNumericSensorHysteresis_Type()
)
sunPlatNumericSensorHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatNumericSensorHysteresis.setStatus("current")
_SunPlatNumericSensorEnabledThresholds_Type = SunPlatNumericSensorEnabledThresholds
_SunPlatNumericSensorEnabledThresholds_Object = MibTableColumn
sunPlatNumericSensorEnabledThresholds = _SunPlatNumericSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 15),
    _SunPlatNumericSensorEnabledThresholds_Type()
)
sunPlatNumericSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatNumericSensorEnabledThresholds.setStatus("current")
_SunPlatNumericSensorRestoreDefaultThresholds_Type = SunPlatNumericSensorThresholdResetAction
_SunPlatNumericSensorRestoreDefaultThresholds_Object = MibTableColumn
sunPlatNumericSensorRestoreDefaultThresholds = _SunPlatNumericSensorRestoreDefaultThresholds_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 8, 1, 16),
    _SunPlatNumericSensorRestoreDefaultThresholds_Type()
)
sunPlatNumericSensorRestoreDefaultThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatNumericSensorRestoreDefaultThresholds.setStatus("current")
_SunPlatDiscreteSensorTable_Object = MibTable
sunPlatDiscreteSensorTable = _SunPlatDiscreteSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 9)
)
if mibBuilder.loadTexts:
    sunPlatDiscreteSensorTable.setStatus("current")
_SunPlatDiscreteSensorEntry_Object = MibTableRow
sunPlatDiscreteSensorEntry = _SunPlatDiscreteSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 9, 1)
)
sunPlatDiscreteSensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sunPlatDiscreteSensorEntry.setStatus("current")
_SunPlatDiscreteSensorCurrent_Type = SunPlatIndex
_SunPlatDiscreteSensorCurrent_Object = MibTableColumn
sunPlatDiscreteSensorCurrent = _SunPlatDiscreteSensorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 9, 1, 1),
    _SunPlatDiscreteSensorCurrent_Type()
)
sunPlatDiscreteSensorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatDiscreteSensorCurrent.setStatus("current")
_SunPlatDiscreteSensorStatesTable_Object = MibTable
sunPlatDiscreteSensorStatesTable = _SunPlatDiscreteSensorStatesTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 10)
)
if mibBuilder.loadTexts:
    sunPlatDiscreteSensorStatesTable.setStatus("current")
_SunPlatDiscreteSensorStatesEntry_Object = MibTableRow
sunPlatDiscreteSensorStatesEntry = _SunPlatDiscreteSensorStatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 10, 1)
)
sunPlatDiscreteSensorStatesEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SUN-PLATFORM-MIB", "sunPlatDiscreteSensorStatesIndex"),
)
if mibBuilder.loadTexts:
    sunPlatDiscreteSensorStatesEntry.setStatus("current")
_SunPlatDiscreteSensorStatesIndex_Type = SunPlatIndex
_SunPlatDiscreteSensorStatesIndex_Object = MibTableColumn
sunPlatDiscreteSensorStatesIndex = _SunPlatDiscreteSensorStatesIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 10, 1, 1),
    _SunPlatDiscreteSensorStatesIndex_Type()
)
sunPlatDiscreteSensorStatesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sunPlatDiscreteSensorStatesIndex.setStatus("current")
_SunPlatDiscreteSensorStatesInterpretation_Type = SnmpAdminString
_SunPlatDiscreteSensorStatesInterpretation_Object = MibTableColumn
sunPlatDiscreteSensorStatesInterpretation = _SunPlatDiscreteSensorStatesInterpretation_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 10, 1, 2),
    _SunPlatDiscreteSensorStatesInterpretation_Type()
)
sunPlatDiscreteSensorStatesInterpretation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatDiscreteSensorStatesInterpretation.setStatus("current")
_SunPlatDiscreteSensorStatesAcceptable_Type = TruthValue
_SunPlatDiscreteSensorStatesAcceptable_Object = MibTableColumn
sunPlatDiscreteSensorStatesAcceptable = _SunPlatDiscreteSensorStatesAcceptable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 10, 1, 3),
    _SunPlatDiscreteSensorStatesAcceptable_Type()
)
sunPlatDiscreteSensorStatesAcceptable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatDiscreteSensorStatesAcceptable.setStatus("current")
_SunPlatFanTable_Object = MibTable
sunPlatFanTable = _SunPlatFanTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 11)
)
if mibBuilder.loadTexts:
    sunPlatFanTable.setStatus("current")
_SunPlatFanEntry_Object = MibTableRow
sunPlatFanEntry = _SunPlatFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 11, 1)
)
sunPlatFanEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sunPlatFanEntry.setStatus("current")
_SunPlatFanClass_Type = SunPlatFanClass
_SunPlatFanClass_Object = MibTableColumn
sunPlatFanClass = _SunPlatFanClass_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 11, 1, 1),
    _SunPlatFanClass_Type()
)
sunPlatFanClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatFanClass.setStatus("current")
_SunPlatAlarmTable_Object = MibTable
sunPlatAlarmTable = _SunPlatAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 12)
)
if mibBuilder.loadTexts:
    sunPlatAlarmTable.setStatus("current")
_SunPlatAlarmEntry_Object = MibTableRow
sunPlatAlarmEntry = _SunPlatAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 12, 1)
)
sunPlatAlarmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sunPlatAlarmEntry.setStatus("current")
_SunPlatAlarmType_Type = SunPlatAlarmType
_SunPlatAlarmType_Object = MibTableColumn
sunPlatAlarmType = _SunPlatAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 12, 1, 1),
    _SunPlatAlarmType_Type()
)
sunPlatAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatAlarmType.setStatus("current")
_SunPlatAlarmState_Type = SunPlatAlarmState
_SunPlatAlarmState_Object = MibTableColumn
sunPlatAlarmState = _SunPlatAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 12, 1, 2),
    _SunPlatAlarmState_Type()
)
sunPlatAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatAlarmState.setStatus("current")
_SunPlatAlarmUrgency_Type = SunPlatAlarmUrgency
_SunPlatAlarmUrgency_Object = MibTableColumn
sunPlatAlarmUrgency = _SunPlatAlarmUrgency_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 12, 1, 3),
    _SunPlatAlarmUrgency_Type()
)
sunPlatAlarmUrgency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatAlarmUrgency.setStatus("current")
_SunPlatWatchdogTable_Object = MibTable
sunPlatWatchdogTable = _SunPlatWatchdogTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 13)
)
if mibBuilder.loadTexts:
    sunPlatWatchdogTable.setStatus("current")
_SunPlatWatchdogEntry_Object = MibTableRow
sunPlatWatchdogEntry = _SunPlatWatchdogEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 13, 1)
)
sunPlatWatchdogEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sunPlatWatchdogEntry.setStatus("current")
_SunPlatWatchdogTimeout_Type = Unsigned32
_SunPlatWatchdogTimeout_Object = MibTableColumn
sunPlatWatchdogTimeout = _SunPlatWatchdogTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 13, 1, 1),
    _SunPlatWatchdogTimeout_Type()
)
sunPlatWatchdogTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatWatchdogTimeout.setStatus("current")
if mibBuilder.loadTexts:
    sunPlatWatchdogTimeout.setUnits("milliseconds")
_SunPlatWatchdogAction_Type = SunPlatWatchdogAction
_SunPlatWatchdogAction_Object = MibTableColumn
sunPlatWatchdogAction = _SunPlatWatchdogAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 13, 1, 2),
    _SunPlatWatchdogAction_Type()
)
sunPlatWatchdogAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatWatchdogAction.setStatus("current")
_SunPlatWatchdogLastExpired_Type = DateAndTime
_SunPlatWatchdogLastExpired_Object = MibTableColumn
sunPlatWatchdogLastExpired = _SunPlatWatchdogLastExpired_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 13, 1, 3),
    _SunPlatWatchdogLastExpired_Type()
)
sunPlatWatchdogLastExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatWatchdogLastExpired.setStatus("current")
_SunPlatWatchdogMonitoredEntity_Type = SunPlatWatchdogMonitoredEntity
_SunPlatWatchdogMonitoredEntity_Object = MibTableColumn
sunPlatWatchdogMonitoredEntity = _SunPlatWatchdogMonitoredEntity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 13, 1, 4),
    _SunPlatWatchdogMonitoredEntity_Type()
)
sunPlatWatchdogMonitoredEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatWatchdogMonitoredEntity.setStatus("current")
_SunPlatPowerSupplyTable_Object = MibTable
sunPlatPowerSupplyTable = _SunPlatPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 14)
)
if mibBuilder.loadTexts:
    sunPlatPowerSupplyTable.setStatus("current")
_SunPlatPowerSupplyEntry_Object = MibTableRow
sunPlatPowerSupplyEntry = _SunPlatPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 14, 1)
)
sunPlatPowerSupplyEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sunPlatPowerSupplyEntry.setStatus("current")
_SunPlatPowerSupplyClass_Type = SunPlatPowerSupplyClass
_SunPlatPowerSupplyClass_Object = MibTableColumn
sunPlatPowerSupplyClass = _SunPlatPowerSupplyClass_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 14, 1, 1),
    _SunPlatPowerSupplyClass_Type()
)
sunPlatPowerSupplyClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatPowerSupplyClass.setStatus("current")
_SunPlatBatteryTable_Object = MibTable
sunPlatBatteryTable = _SunPlatBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 15)
)
if mibBuilder.loadTexts:
    sunPlatBatteryTable.setStatus("current")
_SunPlatBatteryEntry_Object = MibTableRow
sunPlatBatteryEntry = _SunPlatBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 15, 1)
)
sunPlatBatteryEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sunPlatBatteryEntry.setStatus("current")
_SunPlatBatteryStatus_Type = SunPlatBatteryStatus
_SunPlatBatteryStatus_Object = MibTableColumn
sunPlatBatteryStatus = _SunPlatBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 1, 15, 1, 1),
    _SunPlatBatteryStatus_Type()
)
sunPlatBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatBatteryStatus.setStatus("current")
_SunPlatMIBLogicalObjects_ObjectIdentity = ObjectIdentity
sunPlatMIBLogicalObjects = _SunPlatMIBLogicalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2)
)
_SunPlatLogicalTable_Object = MibTable
sunPlatLogicalTable = _SunPlatLogicalTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sunPlatLogicalTable.setStatus("current")
_SunPlatLogicalEntry_Object = MibTableRow
sunPlatLogicalEntry = _SunPlatLogicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sunPlatLogicalEntry.setStatus("current")
_SunPlatLogicalClass_Type = SunPlatLogicalClass
_SunPlatLogicalClass_Object = MibTableColumn
sunPlatLogicalClass = _SunPlatLogicalClass_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 1, 1, 1),
    _SunPlatLogicalClass_Type()
)
sunPlatLogicalClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogicalClass.setStatus("current")
_SunPlatLogicalStatus_Type = SunPlatLogicalStatus
_SunPlatLogicalStatus_Object = MibTableColumn
sunPlatLogicalStatus = _SunPlatLogicalStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 1, 1, 2),
    _SunPlatLogicalStatus_Type()
)
sunPlatLogicalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogicalStatus.setStatus("current")
_SunPlatUnitaryComputerSystemTable_Object = MibTable
sunPlatUnitaryComputerSystemTable = _SunPlatUnitaryComputerSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sunPlatUnitaryComputerSystemTable.setStatus("current")
_SunPlatUnitaryComputerSystemEntry_Object = MibTableRow
sunPlatUnitaryComputerSystemEntry = _SunPlatUnitaryComputerSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 2, 1)
)
sunPlatUnitaryComputerSystemEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
)
if mibBuilder.loadTexts:
    sunPlatUnitaryComputerSystemEntry.setStatus("current")
_SunPlatUnitaryComputerSystemPowerState_Type = SunPlatUnitaryComputerSystemPowerState
_SunPlatUnitaryComputerSystemPowerState_Object = MibTableColumn
sunPlatUnitaryComputerSystemPowerState = _SunPlatUnitaryComputerSystemPowerState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 2, 1, 1),
    _SunPlatUnitaryComputerSystemPowerState_Type()
)
sunPlatUnitaryComputerSystemPowerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatUnitaryComputerSystemPowerState.setStatus("current")
_SunPlatUnitaryComputerSystemApplySettings_Type = SunPlatUnitaryComputerSystemApplicableSetting
_SunPlatUnitaryComputerSystemApplySettings_Object = MibTableColumn
sunPlatUnitaryComputerSystemApplySettings = _SunPlatUnitaryComputerSystemApplySettings_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 2, 1, 2),
    _SunPlatUnitaryComputerSystemApplySettings_Type()
)
sunPlatUnitaryComputerSystemApplySettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatUnitaryComputerSystemApplySettings.setStatus("current")
_SunPlatInitialLoadInfoTable_Object = MibTable
sunPlatInitialLoadInfoTable = _SunPlatInitialLoadInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 3)
)
if mibBuilder.loadTexts:
    sunPlatInitialLoadInfoTable.setStatus("current")
_SunPlatInitialLoadInfoEntry_Object = MibTableRow
sunPlatInitialLoadInfoEntry = _SunPlatInitialLoadInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 3, 1)
)
sunPlatInitialLoadInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
    (0, "SUN-PLATFORM-MIB", "sunPlatInitialLoadInfoIndex"),
)
if mibBuilder.loadTexts:
    sunPlatInitialLoadInfoEntry.setStatus("current")
_SunPlatInitialLoadInfoIndex_Type = SunPlatIndex
_SunPlatInitialLoadInfoIndex_Object = MibTableColumn
sunPlatInitialLoadInfoIndex = _SunPlatInitialLoadInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 3, 1, 1),
    _SunPlatInitialLoadInfoIndex_Type()
)
sunPlatInitialLoadInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sunPlatInitialLoadInfoIndex.setStatus("current")
_SunPlatInitialLoadInfoDescr_Type = SnmpAdminString
_SunPlatInitialLoadInfoDescr_Object = MibTableColumn
sunPlatInitialLoadInfoDescr = _SunPlatInitialLoadInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 3, 1, 2),
    _SunPlatInitialLoadInfoDescr_Type()
)
sunPlatInitialLoadInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatInitialLoadInfoDescr.setStatus("current")
_SunPlatInitialLoadInfoCurrentValue_Type = SnmpAdminString
_SunPlatInitialLoadInfoCurrentValue_Object = MibTableColumn
sunPlatInitialLoadInfoCurrentValue = _SunPlatInitialLoadInfoCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 3, 1, 3),
    _SunPlatInitialLoadInfoCurrentValue_Type()
)
sunPlatInitialLoadInfoCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatInitialLoadInfoCurrentValue.setStatus("current")
_SunPlatInitialLoadInfoDesiredValue_Type = SnmpAdminString
_SunPlatInitialLoadInfoDesiredValue_Object = MibTableColumn
sunPlatInitialLoadInfoDesiredValue = _SunPlatInitialLoadInfoDesiredValue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 2, 3, 1, 4),
    _SunPlatInitialLoadInfoDesiredValue_Type()
)
sunPlatInitialLoadInfoDesiredValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatInitialLoadInfoDesiredValue.setStatus("current")
_SunPlatMIBLogs_ObjectIdentity = ObjectIdentity
sunPlatMIBLogs = _SunPlatMIBLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3)
)
_SunPlatLogTable_Object = MibTable
sunPlatLogTable = _SunPlatLogTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sunPlatLogTable.setStatus("current")
_SunPlatLogEntry_Object = MibTableRow
sunPlatLogEntry = _SunPlatLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1, 1)
)
sunPlatLogEntry.setIndexNames(
    (0, "SUN-PLATFORM-MIB", "sunPlatLogType"),
)
if mibBuilder.loadTexts:
    sunPlatLogEntry.setStatus("current")
_SunPlatLogType_Type = ObjectIdentifier
_SunPlatLogType_Object = MibTableColumn
sunPlatLogType = _SunPlatLogType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1, 1, 1),
    _SunPlatLogType_Type()
)
sunPlatLogType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sunPlatLogType.setStatus("current")


class _SunPlatLogAdministrativeState_Type(SunPlatLogAdministrativeState):
    """Custom type sunPlatLogAdministrativeState based on SunPlatLogAdministrativeState"""


_SunPlatLogAdministrativeState_Object = MibTableColumn
sunPlatLogAdministrativeState = _SunPlatLogAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1, 1, 2),
    _SunPlatLogAdministrativeState_Type()
)
sunPlatLogAdministrativeState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sunPlatLogAdministrativeState.setStatus("current")
_SunPlatLogOperationalState_Type = SunPlatOperationalState
_SunPlatLogOperationalState_Object = MibTableColumn
sunPlatLogOperationalState = _SunPlatLogOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1, 1, 3),
    _SunPlatLogOperationalState_Type()
)
sunPlatLogOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogOperationalState.setStatus("current")
_SunPlatLogFullStatus_Type = TruthValue
_SunPlatLogFullStatus_Object = MibTableColumn
sunPlatLogFullStatus = _SunPlatLogFullStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1, 1, 4),
    _SunPlatLogFullStatus_Type()
)
sunPlatLogFullStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogFullStatus.setStatus("current")
_SunPlatLogCapacityThreshold_Type = SunPlatPercentage
_SunPlatLogCapacityThreshold_Object = MibTableColumn
sunPlatLogCapacityThreshold = _SunPlatLogCapacityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1, 1, 5),
    _SunPlatLogCapacityThreshold_Type()
)
sunPlatLogCapacityThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sunPlatLogCapacityThreshold.setStatus("current")
_SunPlatLogRowStatus_Type = RowStatus
_SunPlatLogRowStatus_Object = MibTableColumn
sunPlatLogRowStatus = _SunPlatLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 1, 1, 6),
    _SunPlatLogRowStatus_Type()
)
sunPlatLogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sunPlatLogRowStatus.setStatus("current")
_SunPlatLogRecordTable_Object = MibTable
sunPlatLogRecordTable = _SunPlatLogRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sunPlatLogRecordTable.setStatus("current")
_SunPlatLogRecordEntry_Object = MibTableRow
sunPlatLogRecordEntry = _SunPlatLogRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 2, 1)
)
sunPlatLogRecordEntry.setIndexNames(
    (0, "SUN-PLATFORM-MIB", "sunPlatLogType"),
    (0, "SUN-PLATFORM-MIB", "sunPlatLogRecordId"),
)
if mibBuilder.loadTexts:
    sunPlatLogRecordEntry.setStatus("current")
_SunPlatLogRecordId_Type = Unsigned32
_SunPlatLogRecordId_Object = MibTableColumn
sunPlatLogRecordId = _SunPlatLogRecordId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 2, 1, 1),
    _SunPlatLogRecordId_Type()
)
sunPlatLogRecordId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sunPlatLogRecordId.setStatus("current")
_SunPlatLogRecordLoggingTime_Type = DateAndTime
_SunPlatLogRecordLoggingTime_Object = MibTableColumn
sunPlatLogRecordLoggingTime = _SunPlatLogRecordLoggingTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 2, 1, 2),
    _SunPlatLogRecordLoggingTime_Type()
)
sunPlatLogRecordLoggingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordLoggingTime.setStatus("current")
_SunPlatLogRecordManagedObjectInstance_Type = RowPointer
_SunPlatLogRecordManagedObjectInstance_Object = MibTableColumn
sunPlatLogRecordManagedObjectInstance = _SunPlatLogRecordManagedObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 2, 1, 3),
    _SunPlatLogRecordManagedObjectInstance_Type()
)
sunPlatLogRecordManagedObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordManagedObjectInstance.setStatus("current")
_SunPlatLogRecordRowStatus_Type = RowStatus
_SunPlatLogRecordRowStatus_Object = MibTableColumn
sunPlatLogRecordRowStatus = _SunPlatLogRecordRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 2, 1, 4),
    _SunPlatLogRecordRowStatus_Type()
)
sunPlatLogRecordRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunPlatLogRecordRowStatus.setStatus("current")
_SunPlatLogRecordCorrelatedNotifications_Type = SnmpAdminString
_SunPlatLogRecordCorrelatedNotifications_Object = MibTableColumn
sunPlatLogRecordCorrelatedNotifications = _SunPlatLogRecordCorrelatedNotifications_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 2, 1, 5),
    _SunPlatLogRecordCorrelatedNotifications_Type()
)
sunPlatLogRecordCorrelatedNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordCorrelatedNotifications.setStatus("current")
_SunPlatLogRecordAdditionalTable_Object = MibTable
sunPlatLogRecordAdditionalTable = _SunPlatLogRecordAdditionalTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 3)
)
if mibBuilder.loadTexts:
    sunPlatLogRecordAdditionalTable.setStatus("current")
_SunPlatLogRecordAdditionalEntry_Object = MibTableRow
sunPlatLogRecordAdditionalEntry = _SunPlatLogRecordAdditionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 3, 1)
)
sunPlatLogRecordAdditionalEntry.setIndexNames(
    (0, "SUN-PLATFORM-MIB", "sunPlatLogType"),
    (0, "SUN-PLATFORM-MIB", "sunPlatLogRecordId"),
)
if mibBuilder.loadTexts:
    sunPlatLogRecordAdditionalEntry.setStatus("current")
_SunPlatLogRecordAdditionalInfo_Type = ObjectIdentifier
_SunPlatLogRecordAdditionalInfo_Object = MibTableColumn
sunPlatLogRecordAdditionalInfo = _SunPlatLogRecordAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 3, 1, 1),
    _SunPlatLogRecordAdditionalInfo_Type()
)
sunPlatLogRecordAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordAdditionalInfo.setStatus("current")
_SunPlatLogRecordAdditionalText_Type = SnmpAdminString
_SunPlatLogRecordAdditionalText_Object = MibTableColumn
sunPlatLogRecordAdditionalText = _SunPlatLogRecordAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 3, 1, 2),
    _SunPlatLogRecordAdditionalText_Type()
)
sunPlatLogRecordAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordAdditionalText.setStatus("current")
_SunPlatLogRecordAlarmTable_Object = MibTable
sunPlatLogRecordAlarmTable = _SunPlatLogRecordAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 4)
)
if mibBuilder.loadTexts:
    sunPlatLogRecordAlarmTable.setStatus("current")
_SunPlatLogRecordAlarmEntry_Object = MibTableRow
sunPlatLogRecordAlarmEntry = _SunPlatLogRecordAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 4, 1)
)
sunPlatLogRecordAlarmEntry.setIndexNames(
    (0, "SUN-PLATFORM-MIB", "sunPlatLogType"),
    (0, "SUN-PLATFORM-MIB", "sunPlatLogRecordId"),
)
if mibBuilder.loadTexts:
    sunPlatLogRecordAlarmEntry.setStatus("current")
_SunPlatLogRecordAlarmPerceivedSeverity_Type = SunPlatAlarmPerceivedSeverity
_SunPlatLogRecordAlarmPerceivedSeverity_Object = MibTableColumn
sunPlatLogRecordAlarmPerceivedSeverity = _SunPlatLogRecordAlarmPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 4, 1, 1),
    _SunPlatLogRecordAlarmPerceivedSeverity_Type()
)
sunPlatLogRecordAlarmPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordAlarmPerceivedSeverity.setStatus("current")
_SunPlatLogRecordAlarmProbableCause_Type = SunPlatProbableCause
_SunPlatLogRecordAlarmProbableCause_Object = MibTableColumn
sunPlatLogRecordAlarmProbableCause = _SunPlatLogRecordAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 4, 1, 2),
    _SunPlatLogRecordAlarmProbableCause_Type()
)
sunPlatLogRecordAlarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordAlarmProbableCause.setStatus("current")
_SunPlatLogRecordAlarmSpecificProblem_Type = SnmpAdminString
_SunPlatLogRecordAlarmSpecificProblem_Object = MibTableColumn
sunPlatLogRecordAlarmSpecificProblem = _SunPlatLogRecordAlarmSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 4, 1, 3),
    _SunPlatLogRecordAlarmSpecificProblem_Type()
)
sunPlatLogRecordAlarmSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordAlarmSpecificProblem.setStatus("current")
_SunPlatLogRecordAlarmRepairAction_Type = SnmpAdminString
_SunPlatLogRecordAlarmRepairAction_Object = MibTableColumn
sunPlatLogRecordAlarmRepairAction = _SunPlatLogRecordAlarmRepairAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 4, 1, 4),
    _SunPlatLogRecordAlarmRepairAction_Type()
)
sunPlatLogRecordAlarmRepairAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordAlarmRepairAction.setStatus("current")
_SunPlatLogRecordChangeTable_Object = MibTable
sunPlatLogRecordChangeTable = _SunPlatLogRecordChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5)
)
if mibBuilder.loadTexts:
    sunPlatLogRecordChangeTable.setStatus("current")
_SunPlatLogRecordChangeEntry_Object = MibTableRow
sunPlatLogRecordChangeEntry = _SunPlatLogRecordChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1)
)
sunPlatLogRecordChangeEntry.setIndexNames(
    (0, "SUN-PLATFORM-MIB", "sunPlatLogType"),
    (0, "SUN-PLATFORM-MIB", "sunPlatLogRecordId"),
)
if mibBuilder.loadTexts:
    sunPlatLogRecordChangeEntry.setStatus("current")
_SunPlatLogRecordChangeChangedOID_Type = VariablePointer
_SunPlatLogRecordChangeChangedOID_Object = MibTableColumn
sunPlatLogRecordChangeChangedOID = _SunPlatLogRecordChangeChangedOID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1, 1),
    _SunPlatLogRecordChangeChangedOID_Type()
)
sunPlatLogRecordChangeChangedOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordChangeChangedOID.setStatus("current")
_SunPlatLogRecordChangeNewInteger_Type = Integer32
_SunPlatLogRecordChangeNewInteger_Object = MibTableColumn
sunPlatLogRecordChangeNewInteger = _SunPlatLogRecordChangeNewInteger_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1, 2),
    _SunPlatLogRecordChangeNewInteger_Type()
)
sunPlatLogRecordChangeNewInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordChangeNewInteger.setStatus("current")
_SunPlatLogRecordChangeOldInteger_Type = Integer32
_SunPlatLogRecordChangeOldInteger_Object = MibTableColumn
sunPlatLogRecordChangeOldInteger = _SunPlatLogRecordChangeOldInteger_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1, 3),
    _SunPlatLogRecordChangeOldInteger_Type()
)
sunPlatLogRecordChangeOldInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordChangeOldInteger.setStatus("current")
_SunPlatLogRecordChangeNewString_Type = OctetString
_SunPlatLogRecordChangeNewString_Object = MibTableColumn
sunPlatLogRecordChangeNewString = _SunPlatLogRecordChangeNewString_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1, 4),
    _SunPlatLogRecordChangeNewString_Type()
)
sunPlatLogRecordChangeNewString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordChangeNewString.setStatus("current")
_SunPlatLogRecordChangeOldString_Type = OctetString
_SunPlatLogRecordChangeOldString_Object = MibTableColumn
sunPlatLogRecordChangeOldString = _SunPlatLogRecordChangeOldString_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1, 5),
    _SunPlatLogRecordChangeOldString_Type()
)
sunPlatLogRecordChangeOldString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordChangeOldString.setStatus("current")
_SunPlatLogRecordChangeNewOID_Type = ObjectIdentifier
_SunPlatLogRecordChangeNewOID_Object = MibTableColumn
sunPlatLogRecordChangeNewOID = _SunPlatLogRecordChangeNewOID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1, 6),
    _SunPlatLogRecordChangeNewOID_Type()
)
sunPlatLogRecordChangeNewOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordChangeNewOID.setStatus("current")
_SunPlatLogRecordChangeOldOID_Type = ObjectIdentifier
_SunPlatLogRecordChangeOldOID_Object = MibTableColumn
sunPlatLogRecordChangeOldOID = _SunPlatLogRecordChangeOldOID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 1, 3, 5, 1, 7),
    _SunPlatLogRecordChangeOldOID_Type()
)
sunPlatLogRecordChangeOldOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunPlatLogRecordChangeOldOID.setStatus("current")
_SunPlatMIBTraps_ObjectIdentity = ObjectIdentity
sunPlatMIBTraps = _SunPlatMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2)
)
_SunPlatMIBTrapPrefix_ObjectIdentity = ObjectIdentity
sunPlatMIBTrapPrefix = _SunPlatMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0)
)
_SunPlatMIBTrapData_ObjectIdentity = ObjectIdentity
sunPlatMIBTrapData = _SunPlatMIBTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1)
)
_SunPlatNotificationEventId_Type = Integer32
_SunPlatNotificationEventId_Object = MibScalar
sunPlatNotificationEventId = _SunPlatNotificationEventId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 1),
    _SunPlatNotificationEventId_Type()
)
sunPlatNotificationEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationEventId.setStatus("current")
_SunPlatNotificationTime_Type = DateAndTime
_SunPlatNotificationTime_Object = MibScalar
sunPlatNotificationTime = _SunPlatNotificationTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 2),
    _SunPlatNotificationTime_Type()
)
sunPlatNotificationTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationTime.setStatus("current")
_SunPlatNotificationObject_Type = RowPointer
_SunPlatNotificationObject_Object = MibScalar
sunPlatNotificationObject = _SunPlatNotificationObject_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 3),
    _SunPlatNotificationObject_Type()
)
sunPlatNotificationObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationObject.setStatus("current")
_SunPlatNotificationPerceivedSeverity_Type = SunPlatAlarmPerceivedSeverity
_SunPlatNotificationPerceivedSeverity_Object = MibScalar
sunPlatNotificationPerceivedSeverity = _SunPlatNotificationPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 4),
    _SunPlatNotificationPerceivedSeverity_Type()
)
sunPlatNotificationPerceivedSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationPerceivedSeverity.setStatus("current")
_SunPlatNotificationProbableCause_Type = SunPlatProbableCause
_SunPlatNotificationProbableCause_Object = MibScalar
sunPlatNotificationProbableCause = _SunPlatNotificationProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 5),
    _SunPlatNotificationProbableCause_Type()
)
sunPlatNotificationProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationProbableCause.setStatus("current")
_SunPlatNotificationSpecificProblem_Type = SnmpAdminString
_SunPlatNotificationSpecificProblem_Object = MibScalar
sunPlatNotificationSpecificProblem = _SunPlatNotificationSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 6),
    _SunPlatNotificationSpecificProblem_Type()
)
sunPlatNotificationSpecificProblem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationSpecificProblem.setStatus("current")
_SunPlatNotificationRepairAction_Type = SnmpAdminString
_SunPlatNotificationRepairAction_Object = MibScalar
sunPlatNotificationRepairAction = _SunPlatNotificationRepairAction_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 7),
    _SunPlatNotificationRepairAction_Type()
)
sunPlatNotificationRepairAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationRepairAction.setStatus("current")
_SunPlatNotificationAdditionalInfo_Type = ObjectIdentifier
_SunPlatNotificationAdditionalInfo_Object = MibScalar
sunPlatNotificationAdditionalInfo = _SunPlatNotificationAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 8),
    _SunPlatNotificationAdditionalInfo_Type()
)
sunPlatNotificationAdditionalInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationAdditionalInfo.setStatus("current")
_SunPlatNotificationAdditionalText_Type = SnmpAdminString
_SunPlatNotificationAdditionalText_Object = MibScalar
sunPlatNotificationAdditionalText = _SunPlatNotificationAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 9),
    _SunPlatNotificationAdditionalText_Type()
)
sunPlatNotificationAdditionalText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationAdditionalText.setStatus("current")
_SunPlatNotificationChangedOID_Type = VariablePointer
_SunPlatNotificationChangedOID_Object = MibScalar
sunPlatNotificationChangedOID = _SunPlatNotificationChangedOID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 10),
    _SunPlatNotificationChangedOID_Type()
)
sunPlatNotificationChangedOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationChangedOID.setStatus("current")
_SunPlatNotificationNewInteger_Type = Integer32
_SunPlatNotificationNewInteger_Object = MibScalar
sunPlatNotificationNewInteger = _SunPlatNotificationNewInteger_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 11),
    _SunPlatNotificationNewInteger_Type()
)
sunPlatNotificationNewInteger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationNewInteger.setStatus("current")
_SunPlatNotificationOldInteger_Type = Integer32
_SunPlatNotificationOldInteger_Object = MibScalar
sunPlatNotificationOldInteger = _SunPlatNotificationOldInteger_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 12),
    _SunPlatNotificationOldInteger_Type()
)
sunPlatNotificationOldInteger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationOldInteger.setStatus("current")
_SunPlatNotificationNewString_Type = OctetString
_SunPlatNotificationNewString_Object = MibScalar
sunPlatNotificationNewString = _SunPlatNotificationNewString_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 13),
    _SunPlatNotificationNewString_Type()
)
sunPlatNotificationNewString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationNewString.setStatus("current")
_SunPlatNotificationOldString_Type = OctetString
_SunPlatNotificationOldString_Object = MibScalar
sunPlatNotificationOldString = _SunPlatNotificationOldString_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 14),
    _SunPlatNotificationOldString_Type()
)
sunPlatNotificationOldString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationOldString.setStatus("current")
_SunPlatNotificationNewOID_Type = ObjectIdentifier
_SunPlatNotificationNewOID_Object = MibScalar
sunPlatNotificationNewOID = _SunPlatNotificationNewOID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 15),
    _SunPlatNotificationNewOID_Type()
)
sunPlatNotificationNewOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationNewOID.setStatus("current")
_SunPlatNotificationOldOID_Type = ObjectIdentifier
_SunPlatNotificationOldOID_Object = MibScalar
sunPlatNotificationOldOID = _SunPlatNotificationOldOID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 16),
    _SunPlatNotificationOldOID_Type()
)
sunPlatNotificationOldOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationOldOID.setStatus("current")
_SunPlatNotificationCorrelatedNotifications_Type = SnmpAdminString
_SunPlatNotificationCorrelatedNotifications_Object = MibScalar
sunPlatNotificationCorrelatedNotifications = _SunPlatNotificationCorrelatedNotifications_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 1, 17),
    _SunPlatNotificationCorrelatedNotifications_Type()
)
sunPlatNotificationCorrelatedNotifications.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunPlatNotificationCorrelatedNotifications.setStatus("current")
_SunPlatMIBConformances_ObjectIdentity = ObjectIdentity
sunPlatMIBConformances = _SunPlatMIBConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3)
)
_SunPlatMIBCompliances_ObjectIdentity = ObjectIdentity
sunPlatMIBCompliances = _SunPlatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 1)
)
_SunPlatMIBGroups_ObjectIdentity = ObjectIdentity
sunPlatMIBGroups = _SunPlatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2)
)
_SunPlatMIBObjectGroups_ObjectIdentity = ObjectIdentity
sunPlatMIBObjectGroups = _SunPlatMIBObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1)
)
_SunPlatMIBNotifGroups_ObjectIdentity = ObjectIdentity
sunPlatMIBNotifGroups = _SunPlatMIBNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 2)
)
entPhysicalEntry.registerAugmentions(
    ("SUN-PLATFORM-MIB",
     "sunPlatEquipmentEntry")
)
sunPlatEquipmentEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
entLogicalEntry.registerAugmentions(
    ("SUN-PLATFORM-MIB",
     "sunPlatLogicalEntry")
)
sunPlatLogicalEntry.setIndexNames(*entLogicalEntry.getIndexNames())

# Managed Objects groups

sunPlatGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 1)
)
sunPlatGeneralGroup.setObjects(
    ("SUN-PLATFORM-MIB", "sunPlatStartTime")
)
if mibBuilder.loadTexts:
    sunPlatGeneralGroup.setStatus("current")

sunPlatEquipmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 2)
)
sunPlatEquipmentGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatEquipmentOperationalState"),
        ("SUN-PLATFORM-MIB", "sunPlatEquipmentAdministrativeState"),
        ("SUN-PLATFORM-MIB", "sunPlatEquipmentAlarmStatus"),
        ("SUN-PLATFORM-MIB", "sunPlatEquipmentUnknownStatus"),
        ("SUN-PLATFORM-MIB", "sunPlatEquipmentLocationName"))
)
if mibBuilder.loadTexts:
    sunPlatEquipmentGroup.setStatus("current")

sunPlatEquipmentHolderGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 3)
)
sunPlatEquipmentHolderGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatEquipmentHolderType"),
        ("SUN-PLATFORM-MIB", "sunPlatEquipmentHolderAcceptableTypes"),
        ("SUN-PLATFORM-MIB", "sunPlatEquipmentHolderStatus"),
        ("SUN-PLATFORM-MIB", "sunPlatEquipmentHolderPowered"))
)
if mibBuilder.loadTexts:
    sunPlatEquipmentHolderGroup.setStatus("current")

sunPlatCircuitPackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 4)
)
sunPlatCircuitPackGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatCircuitPackType"),
        ("SUN-PLATFORM-MIB", "sunPlatCircuitPackAvailabilityStatus"),
        ("SUN-PLATFORM-MIB", "sunPlatCircuitPackReplaceable"),
        ("SUN-PLATFORM-MIB", "sunPlatCircuitPackHotSwappable"))
)
if mibBuilder.loadTexts:
    sunPlatCircuitPackGroup.setStatus("current")

sunPlatPhysicalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 5)
)
sunPlatPhysicalGroup.setObjects(
    ("SUN-PLATFORM-MIB", "sunPlatPhysicalClass")
)
if mibBuilder.loadTexts:
    sunPlatPhysicalGroup.setStatus("current")

sunPlatSensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 6)
)
sunPlatSensorGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatSensorClass"),
        ("SUN-PLATFORM-MIB", "sunPlatSensorType"),
        ("SUN-PLATFORM-MIB", "sunPlatSensorLatency"))
)
if mibBuilder.loadTexts:
    sunPlatSensorGroup.setStatus("current")

sunPlatBinarySensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 7)
)
sunPlatBinarySensorGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatBinarySensorCurrent"),
        ("SUN-PLATFORM-MIB", "sunPlatBinarySensorExpected"),
        ("SUN-PLATFORM-MIB", "sunPlatBinarySensorInterpretTrue"),
        ("SUN-PLATFORM-MIB", "sunPlatBinarySensorInterpretFalse"))
)
if mibBuilder.loadTexts:
    sunPlatBinarySensorGroup.setStatus("current")

sunPlatNumericSensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 8)
)
sunPlatNumericSensorGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatNumericSensorBaseUnits"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorExponent"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorRateUnits"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorCurrent"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorNormalMin"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorNormalMax"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorAccuracy"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorLowerThresholdNonCritical"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorUpperThresholdNonCritical"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorLowerThresholdCritical"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorUpperThresholdCritical"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorLowerThresholdFatal"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorUpperThresholdFatal"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorHysteresis"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorEnabledThresholds"),
        ("SUN-PLATFORM-MIB", "sunPlatNumericSensorRestoreDefaultThresholds"))
)
if mibBuilder.loadTexts:
    sunPlatNumericSensorGroup.setStatus("current")

sunPlatDiscreteSensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 9)
)
sunPlatDiscreteSensorGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatDiscreteSensorCurrent"),
        ("SUN-PLATFORM-MIB", "sunPlatDiscreteSensorStatesInterpretation"),
        ("SUN-PLATFORM-MIB", "sunPlatDiscreteSensorStatesAcceptable"))
)
if mibBuilder.loadTexts:
    sunPlatDiscreteSensorGroup.setStatus("current")

sunPlatFanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 10)
)
sunPlatFanGroup.setObjects(
    ("SUN-PLATFORM-MIB", "sunPlatFanClass")
)
if mibBuilder.loadTexts:
    sunPlatFanGroup.setStatus("current")

sunPlatAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 11)
)
sunPlatAlarmGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatAlarmType"),
        ("SUN-PLATFORM-MIB", "sunPlatAlarmState"),
        ("SUN-PLATFORM-MIB", "sunPlatAlarmUrgency"))
)
if mibBuilder.loadTexts:
    sunPlatAlarmGroup.setStatus("current")

sunPlatWatchdogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 12)
)
sunPlatWatchdogGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatWatchdogTimeout"),
        ("SUN-PLATFORM-MIB", "sunPlatWatchdogAction"),
        ("SUN-PLATFORM-MIB", "sunPlatWatchdogLastExpired"),
        ("SUN-PLATFORM-MIB", "sunPlatWatchdogMonitoredEntity"))
)
if mibBuilder.loadTexts:
    sunPlatWatchdogGroup.setStatus("current")

sunPlatPowerSupplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 13)
)
sunPlatPowerSupplyGroup.setObjects(
    ("SUN-PLATFORM-MIB", "sunPlatPowerSupplyClass")
)
if mibBuilder.loadTexts:
    sunPlatPowerSupplyGroup.setStatus("current")

sunPlatBatteryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 14)
)
sunPlatBatteryGroup.setObjects(
    ("SUN-PLATFORM-MIB", "sunPlatBatteryStatus")
)
if mibBuilder.loadTexts:
    sunPlatBatteryGroup.setStatus("current")

sunPlatLogicalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 15)
)
sunPlatLogicalGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatLogicalClass"),
        ("SUN-PLATFORM-MIB", "sunPlatLogicalStatus"))
)
if mibBuilder.loadTexts:
    sunPlatLogicalGroup.setStatus("current")

sunPlatUnitaryComputerSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 16)
)
sunPlatUnitaryComputerSystemGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatUnitaryComputerSystemPowerState"),
        ("SUN-PLATFORM-MIB", "sunPlatUnitaryComputerSystemApplySettings"),
        ("SUN-PLATFORM-MIB", "sunPlatInitialLoadInfoDescr"),
        ("SUN-PLATFORM-MIB", "sunPlatInitialLoadInfoCurrentValue"),
        ("SUN-PLATFORM-MIB", "sunPlatInitialLoadInfoDesiredValue"))
)
if mibBuilder.loadTexts:
    sunPlatUnitaryComputerSystemGroup.setStatus("current")

sunPlatLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 17)
)
sunPlatLogGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatLogAdministrativeState"),
        ("SUN-PLATFORM-MIB", "sunPlatLogOperationalState"),
        ("SUN-PLATFORM-MIB", "sunPlatLogFullStatus"),
        ("SUN-PLATFORM-MIB", "sunPlatLogCapacityThreshold"),
        ("SUN-PLATFORM-MIB", "sunPlatLogRowStatus"))
)
if mibBuilder.loadTexts:
    sunPlatLogGroup.setStatus("current")

sunPlatLogRecordGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 18)
)
sunPlatLogRecordGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatLogRecordLoggingTime"),
        ("SUN-PLATFORM-MIB", "sunPlatLogRecordManagedObjectInstance"),
        ("SUN-PLATFORM-MIB", "sunPlatLogRecordRowStatus"),
        ("SUN-PLATFORM-MIB", "sunPlatLogRecordCorrelatedNotifications"))
)
if mibBuilder.loadTexts:
    sunPlatLogRecordGroup.setStatus("current")

sunPlatLogRecordAdditionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 19)
)
sunPlatLogRecordAdditionalGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatLogRecordAdditionalInfo"),
        ("SUN-PLATFORM-MIB", "sunPlatLogRecordAdditionalText"))
)
if mibBuilder.loadTexts:
    sunPlatLogRecordAdditionalGroup.setStatus("current")

sunPlatLogRecordAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 20)
)
sunPlatLogRecordAlarmGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatLogRecordAlarmPerceivedSeverity"),
        ("SUN-PLATFORM-MIB", "sunPlatLogRecordAlarmProbableCause"),
        ("SUN-PLATFORM-MIB", "sunPlatLogRecordAlarmSpecificProblem"),
        ("SUN-PLATFORM-MIB", "sunPlatLogRecordAlarmRepairAction"))
)
if mibBuilder.loadTexts:
    sunPlatLogRecordAlarmGroup.setStatus("current")

sunPlatLogRecordChangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 21)
)
sunPlatLogRecordChangeGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeChangedOID"),
        ("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeNewInteger"),
        ("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeOldInteger"),
        ("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeNewString"),
        ("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeOldString"),
        ("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeNewOID"),
        ("SUN-PLATFORM-MIB", "sunPlatLogRecordChangeOldOID"))
)
if mibBuilder.loadTexts:
    sunPlatLogRecordChangeGroup.setStatus("current")

sunPlatNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 1, 22)
)
sunPlatNotificationObjectGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationPerceivedSeverity"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationProbableCause"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationSpecificProblem"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationRepairAction"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationChangedOID"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationNewInteger"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationOldInteger"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationNewString"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationOldString"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationNewOID"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationOldOID"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"))
)
if mibBuilder.loadTexts:
    sunPlatNotificationObjectGroup.setStatus("current")


# Notification objects

sunPlatObjectCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 1)
)
sunPlatObjectCreation.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"))
)
if mibBuilder.loadTexts:
    sunPlatObjectCreation.setStatus(
        "current"
    )

sunPlatObjectDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 2)
)
sunPlatObjectDeletion.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"))
)
if mibBuilder.loadTexts:
    sunPlatObjectDeletion.setStatus(
        "current"
    )

sunPlatCommunicationsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 3)
)
sunPlatCommunicationsAlarm.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationPerceivedSeverity"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationProbableCause"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationSpecificProblem"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationRepairAction"))
)
if mibBuilder.loadTexts:
    sunPlatCommunicationsAlarm.setStatus(
        "current"
    )

sunPlatEnvironmentalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 4)
)
sunPlatEnvironmentalAlarm.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationPerceivedSeverity"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationProbableCause"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationSpecificProblem"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationRepairAction"))
)
if mibBuilder.loadTexts:
    sunPlatEnvironmentalAlarm.setStatus(
        "current"
    )

sunPlatEquipmentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 5)
)
sunPlatEquipmentAlarm.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationPerceivedSeverity"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationProbableCause"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationSpecificProblem"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationRepairAction"))
)
if mibBuilder.loadTexts:
    sunPlatEquipmentAlarm.setStatus(
        "current"
    )

sunPlatProcessingErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 6)
)
sunPlatProcessingErrorAlarm.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationPerceivedSeverity"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationProbableCause"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationSpecificProblem"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationRepairAction"))
)
if mibBuilder.loadTexts:
    sunPlatProcessingErrorAlarm.setStatus(
        "current"
    )

sunPlatStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 7)
)
sunPlatStateChange.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationChangedOID"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationOldInteger"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationNewInteger"))
)
if mibBuilder.loadTexts:
    sunPlatStateChange.setStatus(
        "current"
    )

sunPlatAttributeChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 8)
)
sunPlatAttributeChangeInteger.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationChangedOID"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationOldInteger"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationNewInteger"))
)
if mibBuilder.loadTexts:
    sunPlatAttributeChangeInteger.setStatus(
        "current"
    )

sunPlatAttributeChangeString = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 9)
)
sunPlatAttributeChangeString.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationChangedOID"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationOldString"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationNewString"))
)
if mibBuilder.loadTexts:
    sunPlatAttributeChangeString.setStatus(
        "current"
    )

sunPlatAttributeChangeOID = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 10)
)
sunPlatAttributeChangeOID.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationChangedOID"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationOldOID"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationNewOID"))
)
if mibBuilder.loadTexts:
    sunPlatAttributeChangeOID.setStatus(
        "current"
    )

sunPlatQualityOfServiceAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 11)
)
sunPlatQualityOfServiceAlarm.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationPerceivedSeverity"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationProbableCause"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationSpecificProblem"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationRepairAction"))
)
if mibBuilder.loadTexts:
    sunPlatQualityOfServiceAlarm.setStatus(
        "current"
    )

sunPlatIndeterminateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 2, 0, 12)
)
sunPlatIndeterminateAlarm.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatNotificationEventId"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationTime"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationObject"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationCorrelatedNotifications"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalInfo"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationAdditionalText"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationPerceivedSeverity"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationProbableCause"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationSpecificProblem"),
        ("SUN-PLATFORM-MIB", "sunPlatNotificationRepairAction"))
)
if mibBuilder.loadTexts:
    sunPlatIndeterminateAlarm.setStatus(
        "current"
    )


# Notifications groups

sunPlatNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 2, 2, 1)
)
sunPlatNotificationsGroup.setObjects(
      *(("SUN-PLATFORM-MIB", "sunPlatObjectCreation"),
        ("SUN-PLATFORM-MIB", "sunPlatObjectDeletion"),
        ("SUN-PLATFORM-MIB", "sunPlatCommunicationsAlarm"),
        ("SUN-PLATFORM-MIB", "sunPlatEnvironmentalAlarm"),
        ("SUN-PLATFORM-MIB", "sunPlatEquipmentAlarm"),
        ("SUN-PLATFORM-MIB", "sunPlatProcessingErrorAlarm"),
        ("SUN-PLATFORM-MIB", "sunPlatStateChange"),
        ("SUN-PLATFORM-MIB", "sunPlatAttributeChangeInteger"),
        ("SUN-PLATFORM-MIB", "sunPlatAttributeChangeString"),
        ("SUN-PLATFORM-MIB", "sunPlatAttributeChangeOID"),
        ("SUN-PLATFORM-MIB", "sunPlatQualityOfServiceAlarm"),
        ("SUN-PLATFORM-MIB", "sunPlatIndeterminateAlarm"))
)
if mibBuilder.loadTexts:
    sunPlatNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

sunPlatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 42, 2, 70, 101, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sunPlatCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUN-PLATFORM-MIB",
    **{"SunPlatLogAdministrativeState": SunPlatLogAdministrativeState,
       "SunPlatAdministrativeState": SunPlatAdministrativeState,
       "SunPlatOperationalState": SunPlatOperationalState,
       "SunPlatAlarmPerceivedSeverity": SunPlatAlarmPerceivedSeverity,
       "SunPlatAlarmStatus": SunPlatAlarmStatus,
       "SunPlatEquipmentHolderType": SunPlatEquipmentHolderType,
       "SunPlatEquipmentHolderStatus": SunPlatEquipmentHolderStatus,
       "SunPlatEquipmentHolderPower": SunPlatEquipmentHolderPower,
       "SunPlatCircuitPackAvailabilityStatus": SunPlatCircuitPackAvailabilityStatus,
       "SunPlatProbableCause": SunPlatProbableCause,
       "SunPlatPhysicalClass": SunPlatPhysicalClass,
       "SunPlatSensorClass": SunPlatSensorClass,
       "SunPlatSensorType": SunPlatSensorType,
       "SunPlatBaseUnits": SunPlatBaseUnits,
       "SunPlatRateUnits": SunPlatRateUnits,
       "SunPlatNumericSensorEnabledThresholds": SunPlatNumericSensorEnabledThresholds,
       "SunPlatNumericSensorThresholdResetAction": SunPlatNumericSensorThresholdResetAction,
       "SunPlatAlarmType": SunPlatAlarmType,
       "SunPlatAlarmState": SunPlatAlarmState,
       "SunPlatAlarmUrgency": SunPlatAlarmUrgency,
       "SunPlatWatchdogAction": SunPlatWatchdogAction,
       "SunPlatWatchdogMonitoredEntity": SunPlatWatchdogMonitoredEntity,
       "SunPlatPowerSupplyClass": SunPlatPowerSupplyClass,
       "SunPlatFanClass": SunPlatFanClass,
       "SunPlatBatteryStatus": SunPlatBatteryStatus,
       "SunPlatUnitaryComputerSystemPowerState": SunPlatUnitaryComputerSystemPowerState,
       "SunPlatUnitaryComputerSystemApplicableSetting": SunPlatUnitaryComputerSystemApplicableSetting,
       "SunPlatLogicalClass": SunPlatLogicalClass,
       "SunPlatLogicalStatus": SunPlatLogicalStatus,
       "SunPlatIndex": SunPlatIndex,
       "SunPlatPercentage": SunPlatPercentage,
       "sun": sun,
       "products": products,
       "sunFire": sunFire,
       "sunPlatMIB": sunPlatMIB,
       "sunPlatMIBObjects": sunPlatMIBObjects,
       "sunPlatMIBPhysicalObjects": sunPlatMIBPhysicalObjects,
       "sunPlatStartTime": sunPlatStartTime,
       "sunPlatEquipmentTable": sunPlatEquipmentTable,
       "sunPlatEquipmentEntry": sunPlatEquipmentEntry,
       "sunPlatEquipmentAdministrativeState": sunPlatEquipmentAdministrativeState,
       "sunPlatEquipmentOperationalState": sunPlatEquipmentOperationalState,
       "sunPlatEquipmentAlarmStatus": sunPlatEquipmentAlarmStatus,
       "sunPlatEquipmentUnknownStatus": sunPlatEquipmentUnknownStatus,
       "sunPlatEquipmentLocationName": sunPlatEquipmentLocationName,
       "sunPlatEquipmentHolderTable": sunPlatEquipmentHolderTable,
       "sunPlatEquipmentHolderEntry": sunPlatEquipmentHolderEntry,
       "sunPlatEquipmentHolderType": sunPlatEquipmentHolderType,
       "sunPlatEquipmentHolderAcceptableTypes": sunPlatEquipmentHolderAcceptableTypes,
       "sunPlatEquipmentHolderStatus": sunPlatEquipmentHolderStatus,
       "sunPlatEquipmentHolderPowered": sunPlatEquipmentHolderPowered,
       "sunPlatCircuitPackTable": sunPlatCircuitPackTable,
       "sunPlatCircuitPackEntry": sunPlatCircuitPackEntry,
       "sunPlatCircuitPackType": sunPlatCircuitPackType,
       "sunPlatCircuitPackAvailabilityStatus": sunPlatCircuitPackAvailabilityStatus,
       "sunPlatCircuitPackReplaceable": sunPlatCircuitPackReplaceable,
       "sunPlatCircuitPackHotSwappable": sunPlatCircuitPackHotSwappable,
       "sunPlatPhysicalTable": sunPlatPhysicalTable,
       "sunPlatPhysicalEntry": sunPlatPhysicalEntry,
       "sunPlatPhysicalClass": sunPlatPhysicalClass,
       "sunPlatSensorTable": sunPlatSensorTable,
       "sunPlatSensorEntry": sunPlatSensorEntry,
       "sunPlatSensorClass": sunPlatSensorClass,
       "sunPlatSensorType": sunPlatSensorType,
       "sunPlatSensorLatency": sunPlatSensorLatency,
       "sunPlatBinarySensorTable": sunPlatBinarySensorTable,
       "sunPlatBinarySensorEntry": sunPlatBinarySensorEntry,
       "sunPlatBinarySensorCurrent": sunPlatBinarySensorCurrent,
       "sunPlatBinarySensorExpected": sunPlatBinarySensorExpected,
       "sunPlatBinarySensorInterpretTrue": sunPlatBinarySensorInterpretTrue,
       "sunPlatBinarySensorInterpretFalse": sunPlatBinarySensorInterpretFalse,
       "sunPlatNumericSensorTable": sunPlatNumericSensorTable,
       "sunPlatNumericSensorEntry": sunPlatNumericSensorEntry,
       "sunPlatNumericSensorBaseUnits": sunPlatNumericSensorBaseUnits,
       "sunPlatNumericSensorExponent": sunPlatNumericSensorExponent,
       "sunPlatNumericSensorRateUnits": sunPlatNumericSensorRateUnits,
       "sunPlatNumericSensorCurrent": sunPlatNumericSensorCurrent,
       "sunPlatNumericSensorNormalMin": sunPlatNumericSensorNormalMin,
       "sunPlatNumericSensorNormalMax": sunPlatNumericSensorNormalMax,
       "sunPlatNumericSensorAccuracy": sunPlatNumericSensorAccuracy,
       "sunPlatNumericSensorLowerThresholdNonCritical": sunPlatNumericSensorLowerThresholdNonCritical,
       "sunPlatNumericSensorUpperThresholdNonCritical": sunPlatNumericSensorUpperThresholdNonCritical,
       "sunPlatNumericSensorLowerThresholdCritical": sunPlatNumericSensorLowerThresholdCritical,
       "sunPlatNumericSensorUpperThresholdCritical": sunPlatNumericSensorUpperThresholdCritical,
       "sunPlatNumericSensorLowerThresholdFatal": sunPlatNumericSensorLowerThresholdFatal,
       "sunPlatNumericSensorUpperThresholdFatal": sunPlatNumericSensorUpperThresholdFatal,
       "sunPlatNumericSensorHysteresis": sunPlatNumericSensorHysteresis,
       "sunPlatNumericSensorEnabledThresholds": sunPlatNumericSensorEnabledThresholds,
       "sunPlatNumericSensorRestoreDefaultThresholds": sunPlatNumericSensorRestoreDefaultThresholds,
       "sunPlatDiscreteSensorTable": sunPlatDiscreteSensorTable,
       "sunPlatDiscreteSensorEntry": sunPlatDiscreteSensorEntry,
       "sunPlatDiscreteSensorCurrent": sunPlatDiscreteSensorCurrent,
       "sunPlatDiscreteSensorStatesTable": sunPlatDiscreteSensorStatesTable,
       "sunPlatDiscreteSensorStatesEntry": sunPlatDiscreteSensorStatesEntry,
       "sunPlatDiscreteSensorStatesIndex": sunPlatDiscreteSensorStatesIndex,
       "sunPlatDiscreteSensorStatesInterpretation": sunPlatDiscreteSensorStatesInterpretation,
       "sunPlatDiscreteSensorStatesAcceptable": sunPlatDiscreteSensorStatesAcceptable,
       "sunPlatFanTable": sunPlatFanTable,
       "sunPlatFanEntry": sunPlatFanEntry,
       "sunPlatFanClass": sunPlatFanClass,
       "sunPlatAlarmTable": sunPlatAlarmTable,
       "sunPlatAlarmEntry": sunPlatAlarmEntry,
       "sunPlatAlarmType": sunPlatAlarmType,
       "sunPlatAlarmState": sunPlatAlarmState,
       "sunPlatAlarmUrgency": sunPlatAlarmUrgency,
       "sunPlatWatchdogTable": sunPlatWatchdogTable,
       "sunPlatWatchdogEntry": sunPlatWatchdogEntry,
       "sunPlatWatchdogTimeout": sunPlatWatchdogTimeout,
       "sunPlatWatchdogAction": sunPlatWatchdogAction,
       "sunPlatWatchdogLastExpired": sunPlatWatchdogLastExpired,
       "sunPlatWatchdogMonitoredEntity": sunPlatWatchdogMonitoredEntity,
       "sunPlatPowerSupplyTable": sunPlatPowerSupplyTable,
       "sunPlatPowerSupplyEntry": sunPlatPowerSupplyEntry,
       "sunPlatPowerSupplyClass": sunPlatPowerSupplyClass,
       "sunPlatBatteryTable": sunPlatBatteryTable,
       "sunPlatBatteryEntry": sunPlatBatteryEntry,
       "sunPlatBatteryStatus": sunPlatBatteryStatus,
       "sunPlatMIBLogicalObjects": sunPlatMIBLogicalObjects,
       "sunPlatLogicalTable": sunPlatLogicalTable,
       "sunPlatLogicalEntry": sunPlatLogicalEntry,
       "sunPlatLogicalClass": sunPlatLogicalClass,
       "sunPlatLogicalStatus": sunPlatLogicalStatus,
       "sunPlatUnitaryComputerSystemTable": sunPlatUnitaryComputerSystemTable,
       "sunPlatUnitaryComputerSystemEntry": sunPlatUnitaryComputerSystemEntry,
       "sunPlatUnitaryComputerSystemPowerState": sunPlatUnitaryComputerSystemPowerState,
       "sunPlatUnitaryComputerSystemApplySettings": sunPlatUnitaryComputerSystemApplySettings,
       "sunPlatInitialLoadInfoTable": sunPlatInitialLoadInfoTable,
       "sunPlatInitialLoadInfoEntry": sunPlatInitialLoadInfoEntry,
       "sunPlatInitialLoadInfoIndex": sunPlatInitialLoadInfoIndex,
       "sunPlatInitialLoadInfoDescr": sunPlatInitialLoadInfoDescr,
       "sunPlatInitialLoadInfoCurrentValue": sunPlatInitialLoadInfoCurrentValue,
       "sunPlatInitialLoadInfoDesiredValue": sunPlatInitialLoadInfoDesiredValue,
       "sunPlatMIBLogs": sunPlatMIBLogs,
       "sunPlatLogTable": sunPlatLogTable,
       "sunPlatLogEntry": sunPlatLogEntry,
       "sunPlatLogType": sunPlatLogType,
       "sunPlatLogAdministrativeState": sunPlatLogAdministrativeState,
       "sunPlatLogOperationalState": sunPlatLogOperationalState,
       "sunPlatLogFullStatus": sunPlatLogFullStatus,
       "sunPlatLogCapacityThreshold": sunPlatLogCapacityThreshold,
       "sunPlatLogRowStatus": sunPlatLogRowStatus,
       "sunPlatLogRecordTable": sunPlatLogRecordTable,
       "sunPlatLogRecordEntry": sunPlatLogRecordEntry,
       "sunPlatLogRecordId": sunPlatLogRecordId,
       "sunPlatLogRecordLoggingTime": sunPlatLogRecordLoggingTime,
       "sunPlatLogRecordManagedObjectInstance": sunPlatLogRecordManagedObjectInstance,
       "sunPlatLogRecordRowStatus": sunPlatLogRecordRowStatus,
       "sunPlatLogRecordCorrelatedNotifications": sunPlatLogRecordCorrelatedNotifications,
       "sunPlatLogRecordAdditionalTable": sunPlatLogRecordAdditionalTable,
       "sunPlatLogRecordAdditionalEntry": sunPlatLogRecordAdditionalEntry,
       "sunPlatLogRecordAdditionalInfo": sunPlatLogRecordAdditionalInfo,
       "sunPlatLogRecordAdditionalText": sunPlatLogRecordAdditionalText,
       "sunPlatLogRecordAlarmTable": sunPlatLogRecordAlarmTable,
       "sunPlatLogRecordAlarmEntry": sunPlatLogRecordAlarmEntry,
       "sunPlatLogRecordAlarmPerceivedSeverity": sunPlatLogRecordAlarmPerceivedSeverity,
       "sunPlatLogRecordAlarmProbableCause": sunPlatLogRecordAlarmProbableCause,
       "sunPlatLogRecordAlarmSpecificProblem": sunPlatLogRecordAlarmSpecificProblem,
       "sunPlatLogRecordAlarmRepairAction": sunPlatLogRecordAlarmRepairAction,
       "sunPlatLogRecordChangeTable": sunPlatLogRecordChangeTable,
       "sunPlatLogRecordChangeEntry": sunPlatLogRecordChangeEntry,
       "sunPlatLogRecordChangeChangedOID": sunPlatLogRecordChangeChangedOID,
       "sunPlatLogRecordChangeNewInteger": sunPlatLogRecordChangeNewInteger,
       "sunPlatLogRecordChangeOldInteger": sunPlatLogRecordChangeOldInteger,
       "sunPlatLogRecordChangeNewString": sunPlatLogRecordChangeNewString,
       "sunPlatLogRecordChangeOldString": sunPlatLogRecordChangeOldString,
       "sunPlatLogRecordChangeNewOID": sunPlatLogRecordChangeNewOID,
       "sunPlatLogRecordChangeOldOID": sunPlatLogRecordChangeOldOID,
       "sunPlatMIBTraps": sunPlatMIBTraps,
       "sunPlatMIBTrapPrefix": sunPlatMIBTrapPrefix,
       "sunPlatObjectCreation": sunPlatObjectCreation,
       "sunPlatObjectDeletion": sunPlatObjectDeletion,
       "sunPlatCommunicationsAlarm": sunPlatCommunicationsAlarm,
       "sunPlatEnvironmentalAlarm": sunPlatEnvironmentalAlarm,
       "sunPlatEquipmentAlarm": sunPlatEquipmentAlarm,
       "sunPlatProcessingErrorAlarm": sunPlatProcessingErrorAlarm,
       "sunPlatStateChange": sunPlatStateChange,
       "sunPlatAttributeChangeInteger": sunPlatAttributeChangeInteger,
       "sunPlatAttributeChangeString": sunPlatAttributeChangeString,
       "sunPlatAttributeChangeOID": sunPlatAttributeChangeOID,
       "sunPlatQualityOfServiceAlarm": sunPlatQualityOfServiceAlarm,
       "sunPlatIndeterminateAlarm": sunPlatIndeterminateAlarm,
       "sunPlatMIBTrapData": sunPlatMIBTrapData,
       "sunPlatNotificationEventId": sunPlatNotificationEventId,
       "sunPlatNotificationTime": sunPlatNotificationTime,
       "sunPlatNotificationObject": sunPlatNotificationObject,
       "sunPlatNotificationPerceivedSeverity": sunPlatNotificationPerceivedSeverity,
       "sunPlatNotificationProbableCause": sunPlatNotificationProbableCause,
       "sunPlatNotificationSpecificProblem": sunPlatNotificationSpecificProblem,
       "sunPlatNotificationRepairAction": sunPlatNotificationRepairAction,
       "sunPlatNotificationAdditionalInfo": sunPlatNotificationAdditionalInfo,
       "sunPlatNotificationAdditionalText": sunPlatNotificationAdditionalText,
       "sunPlatNotificationChangedOID": sunPlatNotificationChangedOID,
       "sunPlatNotificationNewInteger": sunPlatNotificationNewInteger,
       "sunPlatNotificationOldInteger": sunPlatNotificationOldInteger,
       "sunPlatNotificationNewString": sunPlatNotificationNewString,
       "sunPlatNotificationOldString": sunPlatNotificationOldString,
       "sunPlatNotificationNewOID": sunPlatNotificationNewOID,
       "sunPlatNotificationOldOID": sunPlatNotificationOldOID,
       "sunPlatNotificationCorrelatedNotifications": sunPlatNotificationCorrelatedNotifications,
       "sunPlatMIBConformances": sunPlatMIBConformances,
       "sunPlatMIBCompliances": sunPlatMIBCompliances,
       "sunPlatCompliance": sunPlatCompliance,
       "sunPlatMIBGroups": sunPlatMIBGroups,
       "sunPlatMIBObjectGroups": sunPlatMIBObjectGroups,
       "sunPlatGeneralGroup": sunPlatGeneralGroup,
       "sunPlatEquipmentGroup": sunPlatEquipmentGroup,
       "sunPlatEquipmentHolderGroup": sunPlatEquipmentHolderGroup,
       "sunPlatCircuitPackGroup": sunPlatCircuitPackGroup,
       "sunPlatPhysicalGroup": sunPlatPhysicalGroup,
       "sunPlatSensorGroup": sunPlatSensorGroup,
       "sunPlatBinarySensorGroup": sunPlatBinarySensorGroup,
       "sunPlatNumericSensorGroup": sunPlatNumericSensorGroup,
       "sunPlatDiscreteSensorGroup": sunPlatDiscreteSensorGroup,
       "sunPlatFanGroup": sunPlatFanGroup,
       "sunPlatAlarmGroup": sunPlatAlarmGroup,
       "sunPlatWatchdogGroup": sunPlatWatchdogGroup,
       "sunPlatPowerSupplyGroup": sunPlatPowerSupplyGroup,
       "sunPlatBatteryGroup": sunPlatBatteryGroup,
       "sunPlatLogicalGroup": sunPlatLogicalGroup,
       "sunPlatUnitaryComputerSystemGroup": sunPlatUnitaryComputerSystemGroup,
       "sunPlatLogGroup": sunPlatLogGroup,
       "sunPlatLogRecordGroup": sunPlatLogRecordGroup,
       "sunPlatLogRecordAdditionalGroup": sunPlatLogRecordAdditionalGroup,
       "sunPlatLogRecordAlarmGroup": sunPlatLogRecordAlarmGroup,
       "sunPlatLogRecordChangeGroup": sunPlatLogRecordChangeGroup,
       "sunPlatNotificationObjectGroup": sunPlatNotificationObjectGroup,
       "sunPlatMIBNotifGroups": sunPlatMIBNotifGroups,
       "sunPlatNotificationsGroup": sunPlatNotificationsGroup}
)
