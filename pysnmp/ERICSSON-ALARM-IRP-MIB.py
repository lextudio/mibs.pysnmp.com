# SNMP MIB module (ERICSSON-ALARM-IRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERICSSON-ALARM-IRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:32 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

alarmIrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3881, 2)
)
alarmIrpMIB.setRevisions(
        ("2004-09-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DisplayString80(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class DisplayString200(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )



class ManagedObjectClass(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )



class ManagedObjectInstance(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )



class TypeOfEvent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              10,
              11,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("communicationsAlarm", 2),
          ("environmentalAlarm", 3),
          ("equipmentAlarm", 4),
          ("integrityViolation", 15),
          ("operationalViolation", 16),
          ("physicalViolation", 17),
          ("processingErrorAlarm", 10),
          ("qualityOfServiceAlarm", 11),
          ("securityServiceViolation", 18),
          ("timeDomainViolation", 19),
          ("unknown", 0))
    )



class PerceivedSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 5),
          ("critical", 1),
          ("indeterminate", 0),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )



class ProbableCause(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              151,
              152,
              153,
              154,
              155,
              156,
              301,
              302,
              303,
              305,
              306,
              307,
              308,
              310,
              311,
              313,
              315,
              316,
              317,
              321,
              322,
              323,
              324,
              325,
              326,
              327,
              330,
              332,
              333,
              334,
              336,
              339,
              340,
              342,
              343,
              344,
              345,
              346,
              347,
              348,
              350,
              351,
              353,
              354,
              356,
              357,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              415,
              416,
              417,
              418,
              501,
              502,
              503,
              504,
              505,
              507,
              508,
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
              525,
              526,
              527,
              528,
              529,
              530,
              531,
              532,
              533,
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
              561,
              562,
              563,
              564,
              565,
              566,
              567,
              568,
              569,
              570,
              571,
              572,
              573,
              574,
              5056)
        )
    )
    namedValues = NamedValues(
        *(("gsm1211AbisToBTSInterfaceFailure", 501),
          ("gsm1211AbisToTRXInterfaceFailure", 502),
          ("gsm1211AntennaProblem", 503),
          ("gsm1211BatteryBreakdown", 504),
          ("gsm1211BatteryChargingFault", 505),
          ("gsm1211BroadcastChannelFailure", 565),
          ("gsm1211ClockSynchronisationProblem", 5056),
          ("gsm1211CombinerProblem", 507),
          ("gsm1211ConnectionEstablishmentError", 566),
          ("gsm1211CoolingSystemFailure", 549),
          ("gsm1211DatabaseInconsistency", 537),
          ("gsm1211DiskProblem", 508),
          ("gsm1211ExcessiveReceiverTemperature", 510),
          ("gsm1211ExcessiveTransmitterOutputPower", 511),
          ("gsm1211ExcessiveTransmitterTemperature", 512),
          ("gsm1211ExternalEquipmentFailure", 550),
          ("gsm1211ExternalPowerSupplyFailure", 551),
          ("gsm1211ExternalTransmissionDeviceFailure", 552),
          ("gsm1211FileSystemCallUnsuccessful", 538),
          ("gsm1211FrequencyHoppingDegraded", 513),
          ("gsm1211FrequencyHoppingFailure", 514),
          ("gsm1211FrequencyRedefinitionFailed", 515),
          ("gsm1211InputParameterOutOfRange", 539),
          ("gsm1211InvalidMSUReceived", 568),
          ("gsm1211InvalidMessageReceived", 567),
          ("gsm1211InvalidParameter", 540),
          ("gsm1211InvalidPointer", 541),
          ("gsm1211LAPDLinkProtocolFailure", 569),
          ("gsm1211LineInterfaceFailure", 516),
          ("gsm1211LinkFailure", 517),
          ("gsm1211LocalAlarmIndication", 570),
          ("gsm1211LossOfSynchronisation", 518),
          ("gsm1211LostRedundancy", 519),
          ("gsm1211MainsBreakdownWithBatteryBackUp", 520),
          ("gsm1211MainsBreakdownWithoutBatteryBackUp", 521),
          ("gsm1211MessageNotExpected", 542),
          ("gsm1211MessageNotInitialised", 543),
          ("gsm1211MessageOutOfSequence", 544),
          ("gsm1211PowerSupplyFailure", 522),
          ("gsm1211ReceiverAntennaFault", 523),
          ("gsm1211ReceiverMulticouplerFailure", 525),
          ("gsm1211ReducedAlarmReporting", 561),
          ("gsm1211ReducedEventReporting", 562),
          ("gsm1211ReducedLoggingCapability", 563),
          ("gsm1211ReducedTransmitterOutputPower", 526),
          ("gsm1211RemoteAlarmIndication", 571),
          ("gsm1211RoutingFailure", 572),
          ("gsm1211SS7ProtocolFailure", 573),
          ("gsm1211SignalQualityEvaluationFault", 527),
          ("gsm1211SystemCallUnsuccessful", 545),
          ("gsm1211SystemResourcesOverload", 564),
          ("gsm1211TimeoutExpired", 546),
          ("gsm1211TimeslotHardwareFailure", 528),
          ("gsm1211TransceiverProblem", 529),
          ("gsm1211TranscoderOrRateAdapterProblem", 531),
          ("gsm1211TranscoderProblem", 530),
          ("gsm1211TransmissionError", 574),
          ("gsm1211TransmitterAntennaFailure", 532),
          ("gsm1211TransmitterAntennaNotAdjusted", 533),
          ("gsm1211TransmitterLowVoltageOrCurrent", 535),
          ("gsm1211TransmitterOffFrequency", 536),
          ("gsm1211VariableOutOfRange", 547),
          ("gsm1211WatchDogTimerExpired", 548),
          ("m3100AirCompressorFailure", 101),
          ("m3100AirConditioningFailure", 102),
          ("m3100AirDryerFailure", 103),
          ("m3100AlarmIndicationSignal", 1),
          ("m3100BackPlaneFailure", 51),
          ("m3100BatteryDischarging", 104),
          ("m3100BatteryFailure", 105),
          ("m3100CallSetupFailure", 2),
          ("m3100CommercialPowerFailure", 106),
          ("m3100CoolingFanFailure", 107),
          ("m3100CorruptData", 153),
          ("m3100DataSetProblem", 52),
          ("m3100DegradedSignal", 3),
          ("m3100EnclosureDoorOpen", 118),
          ("m3100EngineFailure", 108),
          ("m3100EquipmentIdentifierDuplication", 53),
          ("m3100ExcessiveBitErrorRate", 12),
          ("m3100ExplosiveGas", 119),
          ("m3100ExternalIfDeviceProblem", 54),
          ("m3100FarEndReceiverFailure", 4),
          ("m3100Fire", 120),
          ("m3100FireDetectorFailure", 109),
          ("m3100Flood", 121),
          ("m3100FramingError", 5),
          ("m3100FuseFailure", 110),
          ("m3100GeneratorFailure", 111),
          ("m3100HighHumidity", 122),
          ("m3100HighTemperature", 123),
          ("m3100HighWind", 124),
          ("m3100IceBuildUp", 125),
          ("m3100Indeterminate", 0),
          ("m3100LineCardProblem", 55),
          ("m3100LossOfFrame", 6),
          ("m3100LossOfMultiFrame", 16),
          ("m3100LossOfPointer", 7),
          ("m3100LossOfSignal", 8),
          ("m3100LowBatteryThreshold", 112),
          ("m3100LowCablePressure", 129),
          ("m3100LowFuel", 127),
          ("m3100LowHumidity", 128),
          ("m3100LowTemperature", 130),
          ("m3100LowWater", 131),
          ("m3100MemoryMismatch", 152),
          ("m3100MultiplexerProblem", 56),
          ("m3100NeIdentifierDuplication", 57),
          ("m3100OutOfCPUCycles", 154),
          ("m3100PathTraceMismatch", 13),
          ("m3100PayloadTypeMismatch", 9),
          ("m3100PowerProblem", 58),
          ("m3100ProcessorProblem", 59),
          ("m3100ProtectionPathFailure", 60),
          ("m3100PumpFailure", 113),
          ("m3100ReceiverFailure", 61),
          ("m3100RectifierFailure", 114),
          ("m3100RectifierHighVoltage", 115),
          ("m3100RectifierLowVoltage", 116),
          ("m3100RemoteAlarmInterface", 11),
          ("m3100ReplaceableUnitMissing", 62),
          ("m3100ReplaceableUnitProblem", 69),
          ("m3100ReplaceableUnitTypeMismatch", 63),
          ("m3100SignalLabelMismatch", 15),
          ("m3100Smoke", 132),
          ("m3100SoftwareDownloadFailure", 156),
          ("m3100SoftwareEnvironmentProblem", 155),
          ("m3100StorageCapacityProblem", 151),
          ("m3100SynchronisationSourceMismatch", 64),
          ("m3100TerminalProblem", 65),
          ("m3100TimingProblem", 66),
          ("m3100ToxicGas", 133),
          ("m3100TransmissionError", 10),
          ("m3100TransmitterFailure", 67),
          ("m3100TrunkCardProblem", 68),
          ("m3100Unavailable", 14),
          ("m3100VentilationSystemFailure", 117),
          ("x733AdapterError", 301),
          ("x733ApplicationSubsystemFailure", 302),
          ("x733BandwidthReduced", 303),
          ("x733CommunicationsProtocolError", 305),
          ("x733CommunicationsSubsystemFailure", 306),
          ("x733ConfigurationOrCustomizationError", 307),
          ("x733Congestion", 308),
          ("x733CpuCyclesLimitExceeded", 310),
          ("x733DTEDCEInterfaceError", 313),
          ("x733DataSetOrModemError", 311),
          ("x733EquipmentMalfunction", 315),
          ("x733ExcessiveVibration", 316),
          ("x733FileError", 317),
          ("x733HeatingOrVentilationOrCoolingSystemProblem", 321),
          ("x733HumidityUnacceptable", 322),
          ("x733InputDeviceError", 324),
          ("x733InputOutputDeviceError", 323),
          ("x733LANError", 325),
          ("x733LeakDetected", 326),
          ("x733LocalNodeTransmissionError", 327),
          ("x733MaterialSupplyExhausted", 330),
          ("x733OuputDeviceError", 333),
          ("x733OutOfMemory", 332),
          ("x733PerformanceDegraded", 334),
          ("x733PressureUnacceptable", 336),
          ("x733QueueSizeExceeded", 339),
          ("x733ReceiveFailure", 340),
          ("x733RemoteNodeTransmissionError", 342),
          ("x733ResourceAtOrNearingCapacity", 343),
          ("x733ResponseTimeExcessive", 344),
          ("x733RetransmissionRateExcessive", 345),
          ("x733SoftwareError", 346),
          ("x733SoftwareProgramAbnormallyTerminated", 347),
          ("x733SoftwareProgramError", 348),
          ("x733TemperatureUnacceptable", 350),
          ("x733ThresholdCrossed", 351),
          ("x733ToxicLeakDetected", 353),
          ("x733TransmitFailure", 354),
          ("x733UnderlyingResourceUnavailable", 356),
          ("x733VersionMismatch", 357),
          ("x736AuthenticationFailure", 401),
          ("x736BreachOfConfidentiality", 402),
          ("x736CableTamper", 403),
          ("x736DelayedInformation", 404),
          ("x736DenialOfService", 405),
          ("x736DuplicateInformation", 406),
          ("x736InformationMissing", 407),
          ("x736InformationModificationDetected", 408),
          ("x736InformationOutOfSequence", 409),
          ("x736IntrusionDetection", 410),
          ("x736KeyExpired", 411),
          ("x736NonRepudiationFailure", 412),
          ("x736OutOfHoursActivity", 413),
          ("x736OutOfService", 414),
          ("x736ProceduralError", 415),
          ("x736UnauthorizedAccessAttempt", 416),
          ("x736UnexpectedInformation", 417),
          ("x736UnspecifiedReason", 418))
    )



# MIB Managed Objects in the order of their OIDs

_AlarmObjects_ObjectIdentity = ObjectIdentity
alarmObjects = _AlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1)
)


class _AlarmIrpVersion_Type(OctetString):
    """Custom type alarmIrpVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AlarmIrpVersion_Type.__name__ = "OctetString"
_AlarmIrpVersion_Object = MibScalar
alarmIrpVersion = _AlarmIrpVersion_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 1),
    _AlarmIrpVersion_Type()
)
alarmIrpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIrpVersion.setStatus("current")
_AlarmIndeterminateNumber_Type = Integer32
_AlarmIndeterminateNumber_Object = MibScalar
alarmIndeterminateNumber = _AlarmIndeterminateNumber_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 2),
    _AlarmIndeterminateNumber_Type()
)
alarmIndeterminateNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndeterminateNumber.setStatus("current")
_AlarmCriticalNumber_Type = Integer32
_AlarmCriticalNumber_Object = MibScalar
alarmCriticalNumber = _AlarmCriticalNumber_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 3),
    _AlarmCriticalNumber_Type()
)
alarmCriticalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCriticalNumber.setStatus("current")
_AlarmMajorNumber_Type = Integer32
_AlarmMajorNumber_Object = MibScalar
alarmMajorNumber = _AlarmMajorNumber_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 4),
    _AlarmMajorNumber_Type()
)
alarmMajorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMajorNumber.setStatus("current")
_AlarmMinorNumber_Type = Integer32
_AlarmMinorNumber_Object = MibScalar
alarmMinorNumber = _AlarmMinorNumber_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 5),
    _AlarmMinorNumber_Type()
)
alarmMinorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMinorNumber.setStatus("current")
_AlarmWarningNumber_Type = Integer32
_AlarmWarningNumber_Object = MibScalar
alarmWarningNumber = _AlarmWarningNumber_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 6),
    _AlarmWarningNumber_Type()
)
alarmWarningNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmWarningNumber.setStatus("current")
_AlarmNumber_Type = Integer32
_AlarmNumber_Object = MibScalar
alarmNumber = _AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 7),
    _AlarmNumber_Type()
)
alarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNumber.setStatus("current")
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1)
)
alarmEntry.setIndexNames(
    (0, "ERICSSON-ALARM-IRP-MIB", "alarmId"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")


class _AlarmId_Type(Integer32):
    """Custom type alarmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlarmId_Type.__name__ = "Integer32"
_AlarmId_Object = MibTableColumn
alarmId = _AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 1),
    _AlarmId_Type()
)
alarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmId.setStatus("current")
_AlarmManagedObjectClass_Type = ManagedObjectClass
_AlarmManagedObjectClass_Object = MibTableColumn
alarmManagedObjectClass = _AlarmManagedObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 2),
    _AlarmManagedObjectClass_Type()
)
alarmManagedObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmManagedObjectClass.setStatus("current")
_AlarmManagedObjectInstance_Type = ManagedObjectInstance
_AlarmManagedObjectInstance_Object = MibTableColumn
alarmManagedObjectInstance = _AlarmManagedObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 3),
    _AlarmManagedObjectInstance_Type()
)
alarmManagedObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmManagedObjectInstance.setStatus("current")
_AlarmEventTime_Type = DateAndTime
_AlarmEventTime_Object = MibTableColumn
alarmEventTime = _AlarmEventTime_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 4),
    _AlarmEventTime_Type()
)
alarmEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEventTime.setStatus("current")
_AlarmEventType_Type = TypeOfEvent
_AlarmEventType_Object = MibTableColumn
alarmEventType = _AlarmEventType_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 5),
    _AlarmEventType_Type()
)
alarmEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEventType.setStatus("current")
_AlarmProbableCause_Type = ProbableCause
_AlarmProbableCause_Object = MibTableColumn
alarmProbableCause = _AlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 6),
    _AlarmProbableCause_Type()
)
alarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProbableCause.setStatus("current")
_AlarmPerceivedSeverity_Type = PerceivedSeverity
_AlarmPerceivedSeverity_Object = MibTableColumn
alarmPerceivedSeverity = _AlarmPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 7),
    _AlarmPerceivedSeverity_Type()
)
alarmPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPerceivedSeverity.setStatus("current")
_AlarmSpecificProblem_Type = DisplayString80
_AlarmSpecificProblem_Object = MibTableColumn
alarmSpecificProblem = _AlarmSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 8),
    _AlarmSpecificProblem_Type()
)
alarmSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSpecificProblem.setStatus("current")
_AlarmAckUser_Type = DisplayString80
_AlarmAckUser_Object = MibTableColumn
alarmAckUser = _AlarmAckUser_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 9),
    _AlarmAckUser_Type()
)
alarmAckUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmAckUser.setStatus("current")
_AlarmAckTime_Type = DateAndTime
_AlarmAckTime_Object = MibTableColumn
alarmAckTime = _AlarmAckTime_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 10),
    _AlarmAckTime_Type()
)
alarmAckTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmAckTime.setStatus("current")
_AlarmCommentUser_Type = DisplayString80
_AlarmCommentUser_Object = MibTableColumn
alarmCommentUser = _AlarmCommentUser_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 11),
    _AlarmCommentUser_Type()
)
alarmCommentUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmCommentUser.setStatus("current")
_AlarmCommentText_Type = DisplayString200
_AlarmCommentText_Object = MibTableColumn
alarmCommentText = _AlarmCommentText_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 12),
    _AlarmCommentText_Type()
)
alarmCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmCommentText.setStatus("current")
_AlarmAdditionalText_Type = DisplayString200
_AlarmAdditionalText_Object = MibTableColumn
alarmAdditionalText = _AlarmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 8, 1, 13),
    _AlarmAdditionalText_Type()
)
alarmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAdditionalText.setStatus("current")
_NotificationId_Type = Integer32
_NotificationId_Object = MibScalar
notificationId = _NotificationId_Object(
    (1, 3, 6, 1, 4, 1, 3881, 2, 1, 9),
    _NotificationId_Type()
)
notificationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notificationId.setStatus("current")
_AlarmNotifications_ObjectIdentity = ObjectIdentity
alarmNotifications = _AlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3881, 2, 2)
)
_AlarmNotificationPrefix_ObjectIdentity = ObjectIdentity
alarmNotificationPrefix = _AlarmNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3881, 2, 2, 0)
)
_AlarmConformance_ObjectIdentity = ObjectIdentity
alarmConformance = _AlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3881, 2, 3)
)
_AlarmCompliances_ObjectIdentity = ObjectIdentity
alarmCompliances = _AlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3881, 2, 3, 1)
)
_AlarmGroups_ObjectIdentity = ObjectIdentity
alarmGroups = _AlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3881, 2, 3, 2)
)

# Managed Objects groups

alarmAdminMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3881, 2, 3, 2, 1)
)
alarmAdminMandatoryGroup.setObjects(
    ("ERICSSON-ALARM-IRP-MIB", "alarmIrpVersion")
)
if mibBuilder.loadTexts:
    alarmAdminMandatoryGroup.setStatus("current")

alarmNumberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3881, 2, 3, 2, 2)
)
alarmNumberGroup.setObjects(
      *(("ERICSSON-ALARM-IRP-MIB", "alarmNumber"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmIndeterminateNumber"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmCriticalNumber"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmMajorNumber"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmMinorNumber"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmWarningNumber"))
)
if mibBuilder.loadTexts:
    alarmNumberGroup.setStatus("current")

alarmMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3881, 2, 3, 2, 3)
)
alarmMandatoryGroup.setObjects(
      *(("ERICSSON-ALARM-IRP-MIB", "notificationId"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmId"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectClass"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectInstance"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmEventTime"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmEventType"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmProbableCause"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmPerceivedSeverity"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmSpecificProblem"))
)
if mibBuilder.loadTexts:
    alarmMandatoryGroup.setStatus("current")

alarmOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3881, 2, 3, 2, 4)
)
alarmOptionalGroup.setObjects(
      *(("ERICSSON-ALARM-IRP-MIB", "alarmAckUser"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmAckTime"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmCommentUser"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmCommentText"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmAdditionalText"))
)
if mibBuilder.loadTexts:
    alarmOptionalGroup.setStatus("current")


# Notification objects

alarmNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 3881, 2, 2, 0, 1)
)
alarmNew.setObjects(
      *(("ERICSSON-ALARM-IRP-MIB", "notificationId"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmId"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectClass"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectInstance"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmEventTime"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmEventType"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmProbableCause"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmPerceivedSeverity"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmSpecificProblem"))
)
if mibBuilder.loadTexts:
    alarmNew.setStatus(
        "current"
    )

alarmChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3881, 2, 2, 0, 2)
)
alarmChanged.setObjects(
      *(("ERICSSON-ALARM-IRP-MIB", "notificationId"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmId"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectClass"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectInstance"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmEventTime"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmEventType"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmProbableCause"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmPerceivedSeverity"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmSpecificProblem"))
)
if mibBuilder.loadTexts:
    alarmChanged.setStatus(
        "current"
    )

alarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3881, 2, 2, 0, 3)
)
alarmCleared.setObjects(
      *(("ERICSSON-ALARM-IRP-MIB", "notificationId"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmId"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectClass"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmManagedObjectInstance"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmEventTime"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmEventType"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmProbableCause"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmPerceivedSeverity"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmSpecificProblem"))
)
if mibBuilder.loadTexts:
    alarmCleared.setStatus(
        "current"
    )


# Notifications groups

alarmNotificationMandatoryGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3881, 2, 3, 2, 5)
)
alarmNotificationMandatoryGroup.setObjects(
      *(("ERICSSON-ALARM-IRP-MIB", "alarmNew"),
        ("ERICSSON-ALARM-IRP-MIB", "alarmCleared"))
)
if mibBuilder.loadTexts:
    alarmNotificationMandatoryGroup.setStatus(
        "current"
    )

alarmNotificationOptionalGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3881, 2, 3, 2, 6)
)
alarmNotificationOptionalGroup.setObjects(
    ("ERICSSON-ALARM-IRP-MIB", "alarmChanged")
)
if mibBuilder.loadTexts:
    alarmNotificationOptionalGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3881, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERICSSON-ALARM-IRP-MIB",
    **{"DisplayString80": DisplayString80,
       "DisplayString200": DisplayString200,
       "ManagedObjectClass": ManagedObjectClass,
       "ManagedObjectInstance": ManagedObjectInstance,
       "TypeOfEvent": TypeOfEvent,
       "PerceivedSeverity": PerceivedSeverity,
       "ProbableCause": ProbableCause,
       "alarmIrpMIB": alarmIrpMIB,
       "alarmObjects": alarmObjects,
       "alarmIrpVersion": alarmIrpVersion,
       "alarmIndeterminateNumber": alarmIndeterminateNumber,
       "alarmCriticalNumber": alarmCriticalNumber,
       "alarmMajorNumber": alarmMajorNumber,
       "alarmMinorNumber": alarmMinorNumber,
       "alarmWarningNumber": alarmWarningNumber,
       "alarmNumber": alarmNumber,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmId": alarmId,
       "alarmManagedObjectClass": alarmManagedObjectClass,
       "alarmManagedObjectInstance": alarmManagedObjectInstance,
       "alarmEventTime": alarmEventTime,
       "alarmEventType": alarmEventType,
       "alarmProbableCause": alarmProbableCause,
       "alarmPerceivedSeverity": alarmPerceivedSeverity,
       "alarmSpecificProblem": alarmSpecificProblem,
       "alarmAckUser": alarmAckUser,
       "alarmAckTime": alarmAckTime,
       "alarmCommentUser": alarmCommentUser,
       "alarmCommentText": alarmCommentText,
       "alarmAdditionalText": alarmAdditionalText,
       "notificationId": notificationId,
       "alarmNotifications": alarmNotifications,
       "alarmNotificationPrefix": alarmNotificationPrefix,
       "alarmNew": alarmNew,
       "alarmChanged": alarmChanged,
       "alarmCleared": alarmCleared,
       "alarmConformance": alarmConformance,
       "alarmCompliances": alarmCompliances,
       "alarmCompliance": alarmCompliance,
       "alarmGroups": alarmGroups,
       "alarmAdminMandatoryGroup": alarmAdminMandatoryGroup,
       "alarmNumberGroup": alarmNumberGroup,
       "alarmMandatoryGroup": alarmMandatoryGroup,
       "alarmOptionalGroup": alarmOptionalGroup,
       "alarmNotificationMandatoryGroup": alarmNotificationMandatoryGroup,
       "alarmNotificationOptionalGroup": alarmNotificationOptionalGroup}
)
