# SNMP MIB module (ITU-IANA-ALARM-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITU-IANA-ALARM-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:28 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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


# Types definitions


# TEXTUAL-CONVENTIONS



class IANAItuProbableCause(Integer32, TextualConvention):
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
          ("lossOfRealTimel", 157),
          ("lossOfRedundancy", 77),
          ("lossOfSignal", 8),
          ("lossOfSynchronisation", 76),
          ("lowBatteryThreshold", 112),
          ("lowCablePressure", 129),
          ("lowFuel", 127),
          ("lowHumidity", 128),
          ("lowTemperatue", 130),
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



class IANAItuEventType(Integer32, TextualConvention):
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
        *(("communicationsAlarm", 2),
          ("environmentalAlarm", 6),
          ("equipmentAlarm", 5),
          ("integrityViolation", 7),
          ("operationalViolation", 8),
          ("other", 1),
          ("physicalViolation", 9),
          ("processingErrorAlarm", 4),
          ("qualityOfServiceAlarm", 3),
          ("securityServiceOrMechanismViolation", 10),
          ("timeDomainViolation", 11))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITU-IANA-ALARM-TC",
    **{"IANAItuProbableCause": IANAItuProbableCause,
       "IANAItuEventType": IANAItuEventType}
)
