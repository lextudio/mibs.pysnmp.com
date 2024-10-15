# SNMP MIB module (CERENT-454-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CERENT-454-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:20 2024
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

(cerentModules,
 cerentProducts) = mibBuilder.importSymbols(
    "CERENT-GLOBAL-REGISTRY",
    "cerentModules",
    "cerentProducts")

(CerentAlarmServiceAffecting,
 CerentAlarmSeverity,
 CerentAlarmStatus,
 CerentLocation,
 CerentMonitorType,
 CerentNotificationClass,
 CerentPeriod,
 CerentPortNumber) = mibBuilder.importSymbols(
    "CERENT-TC",
    "CerentAlarmServiceAffecting",
    "CerentAlarmSeverity",
    "CerentAlarmStatus",
    "CerentLocation",
    "CerentMonitorType",
    "CerentNotificationClass",
    "CerentPeriod",
    "CerentPortNumber")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cerent454MibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 10, 20)
)
cerent454MibModule.setRevisions(
        ("1904-10-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Cerent454AlarmType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              20,
              30,
              40,
              50,
              60,
              70,
              80,
              90,
              100,
              110,
              120,
              130,
              140,
              150,
              160,
              170,
              180,
              190,
              200,
              210,
              220,
              230,
              240,
              250,
              260,
              270,
              280,
              290,
              300,
              310,
              320,
              330,
              340,
              350,
              360,
              370,
              380,
              390,
              400,
              410,
              420,
              430,
              440,
              450,
              460,
              470,
              480,
              490,
              500,
              510,
              520,
              530,
              540,
              550,
              560,
              570,
              580,
              590,
              600,
              610,
              620,
              630,
              640,
              650,
              660,
              670,
              680,
              690,
              700,
              710,
              720,
              730,
              740,
              750,
              760,
              770,
              780,
              790,
              800,
              810,
              820,
              830,
              840,
              850,
              860,
              870,
              880,
              890,
              900,
              910,
              920,
              930,
              940,
              950,
              960,
              970,
              980,
              990,
              1000,
              1010,
              1020,
              1030,
              1040,
              1050,
              1060,
              1070,
              1080,
              1090,
              1100,
              1110,
              1120,
              1130,
              1140,
              1150,
              1160,
              1170,
              1180,
              1190,
              1200,
              1210,
              1220,
              1230,
              1240,
              1250,
              1260,
              1270,
              1280,
              1290,
              1300,
              1310,
              1320,
              1330,
              1340,
              1350,
              1360,
              1370,
              1380,
              1390,
              1400,
              1410,
              1420,
              1430,
              1440,
              1450,
              1460,
              1470,
              1480,
              1490,
              1500,
              1510,
              1520,
              1530,
              1540,
              1550,
              1560,
              1570,
              1580,
              1590,
              1600,
              1610,
              1620,
              1630,
              1640,
              1650,
              1660,
              1670,
              1680,
              1690,
              1700,
              1710,
              1720,
              1730,
              1740,
              1750,
              1760,
              1770,
              1780,
              1790,
              1800,
              1810,
              1820,
              1830,
              1840,
              1850,
              1860,
              1870,
              1880,
              1890,
              1900,
              1910,
              1920,
              1930,
              1940,
              1950,
              1960,
              1970,
              1980,
              1990,
              2000,
              2010,
              2020,
              2030,
              2040,
              2050,
              2060,
              2070,
              2080,
              2090,
              2100,
              2110,
              2120,
              2130,
              2140,
              2150,
              2160,
              2170,
              2180,
              2190,
              2200,
              2210,
              2220,
              2230,
              2240,
              2250,
              2260,
              2270,
              2280,
              2290,
              2300,
              2310,
              2320,
              2330,
              2340,
              2350,
              2360,
              2370,
              2380,
              2390,
              2400,
              2410,
              2420,
              2430,
              2440,
              2450,
              2460,
              2470,
              2480,
              2490,
              2500,
              2510,
              2520,
              2530,
              2540,
              2550,
              2560,
              2570,
              2580,
              2590,
              2600,
              2610,
              2620,
              2630,
              2640,
              2650,
              2660,
              2670,
              2680,
              2690,
              2700,
              2710,
              2720,
              2730,
              2740,
              2750,
              2760,
              2780,
              2790,
              2800,
              2810,
              2820,
              2830,
              2840,
              2850,
              2860,
              2870,
              2880,
              2890,
              2900,
              2910,
              2920,
              2930,
              2940,
              2950,
              2960,
              2970,
              2980,
              2990,
              3000,
              3010,
              3020,
              3030,
              3040,
              3050,
              3060,
              3070,
              3080,
              3090,
              3100,
              3110,
              3120,
              3130,
              3140,
              3150,
              3160,
              3170,
              3180,
              3190,
              3200,
              3210,
              3220,
              3230,
              3240,
              3250,
              3260,
              3270,
              3280,
              3290,
              3300,
              3310,
              3320,
              3330,
              3340,
              3350,
              3360,
              3370,
              3380,
              3390,
              3400,
              3410,
              3420,
              3430,
              3440,
              3450,
              3460,
              3470,
              3480,
              3490,
              3500,
              3510,
              3520,
              3530,
              3540,
              3550,
              3560,
              3570,
              3580,
              3590,
              3600,
              3610,
              3620,
              3630,
              3640,
              3650,
              3660,
              3670,
              3680,
              3710,
              3712,
              3714,
              3716,
              3718,
              3720,
              3722,
              3724,
              3726,
              3730,
              3740,
              3750,
              3760,
              3762,
              3764,
              3766,
              3768,
              3770,
              3780,
              3790,
              3800,
              3805,
              4000,
              4010,
              4020,
              4030,
              4040,
              4050,
              4060,
              4070,
              4080,
              4090,
              4100,
              4110,
              4120,
              4130,
              4140,
              4150,
              4160,
              4170,
              4180,
              4190,
              4200,
              4210,
              4220,
              4230,
              4240,
              4250,
              4260,
              4270,
              4280,
              4290,
              4300,
              4310,
              4320,
              4330,
              4340,
              4350,
              4360,
              4370,
              4380,
              4390,
              4400,
              4410,
              4420,
              4430,
              4440,
              4450,
              4460,
              4470,
              4480,
              4490,
              4500,
              4510,
              4520,
              4530,
              4540,
              4550,
              4560,
              4570,
              4755,
              4760,
              4765,
              4770,
              4780,
              4785,
              4790,
              4795,
              4800,
              4805,
              4810,
              4815,
              4820,
              4825,
              4830,
              4835,
              4840,
              4845,
              4850,
              4855,
              4860,
              4865,
              4870,
              4875,
              4880,
              4885,
              4890,
              4895,
              4900,
              4905,
              4910,
              4915,
              4920,
              4925,
              4930,
              4935,
              4940,
              4945,
              4950,
              4955,
              4960,
              4965,
              4970,
              4975,
              4980,
              4985,
              5000,
              5010,
              5020,
              5030,
              5040,
              5050,
              5060,
              5070,
              5080,
              5090,
              5100,
              5110,
              5120,
              5200,
              5210,
              5220,
              5230,
              5240,
              5250,
              5260,
              5270,
              5280,
              5290,
              5300,
              5310,
              5320,
              5330,
              5340,
              5350,
              5360,
              5370,
              5380,
              5390,
              5400,
              5410,
              5420,
              5430,
              5440,
              5450,
              5460,
              5470,
              5480,
              5490,
              5500,
              5510,
              5520,
              5530,
              5540,
              5550,
              5560,
              5570,
              5600,
              5610,
              5620,
              5630,
              5640,
              5650,
              5660,
              5670,
              5680,
              5690,
              5700,
              5710,
              5730,
              5740,
              5750,
              5770,
              5780,
              5790,
              5800,
              5810,
              5820,
              5830,
              5840,
              5850,
              5860,
              5870,
              5880,
              5890,
              5900,
              5910,
              5920,
              5930,
              5940,
              5950,
              6000,
              6010,
              6020,
              6030,
              6040,
              6050,
              6060,
              6070,
              6080,
              6090,
              6100,
              6110,
              6120,
              6130,
              6140,
              6150,
              6170,
              6180,
              6190,
              6200,
              6210,
              6220,
              6230,
              6240,
              6250,
              6260,
              6270,
              6280,
              6290,
              6300,
              6310,
              6330,
              6340,
              6350,
              6360,
              6370,
              6380,
              6390,
              6400,
              6410,
              6420,
              6430,
              6440,
              6450,
              6460,
              6470,
              6480,
              6490,
              6500,
              6510,
              6520,
              6530,
              6540,
              6550,
              6560,
              6570,
              6580,
              6590,
              6600,
              6610,
              6630,
              6640,
              6650,
              6660,
              6670,
              6680,
              6690,
              6700,
              6710,
              6720,
              6730,
              6740,
              6750,
              6760,
              6770,
              6780,
              6790,
              6800,
              6810,
              6820,
              6830,
              6840,
              6850,
              6860,
              6870,
              6880,
              6890,
              6900,
              6910,
              6920,
              6930,
              6940,
              6950,
              6960,
              6970,
              6975,
              6980,
              7000,
              7005,
              7010,
              7015,
              7055,
              7060,
              7160,
              7165,
              7185,
              7200,
              7210,
              7225,
              7230,
              7235,
              7240,
              7245,
              7250,
              7255,
              7260,
              7265,
              7275,
              7280,
              7285,
              7295,
              7300,
              7305,
              7310,
              7315,
              7320,
              7325,
              7330,
              7335,
              7340,
              7345,
              7350,
              7355,
              7360,
              7365,
              7370,
              7375,
              7380,
              7385,
              7390,
              7395,
              7400,
              7405,
              7410,
              7415,
              7420,
              7425,
              7430,
              7445,
              7450,
              7455,
              7460,
              7465,
              7475,
              7480,
              7485,
              7490,
              7495,
              7500,
              7510,
              7515,
              7520,
              7525,
              7530,
              7535,
              7540,
              7545,
              7550,
              7555,
              7560,
              7565,
              7570,
              7575,
              7580,
              7585,
              7590,
              7595,
              7600,
              7605,
              7610,
              7615,
              7620,
              7625,
              7630,
              7635,
              7640,
              7645,
              7650,
              7655,
              7660,
              7665,
              7670,
              7675,
              7680,
              7685,
              7690,
              7695,
              7700,
              7705,
              7710,
              7715,
              7720,
              7725,
              7730,
              7735,
              7740,
              7745,
              7750,
              7755,
              7760,
              7765,
              7770,
              7775,
              7780,
              7785,
              7790,
              7795,
              7800,
              7805,
              7810,
              7815,
              7820,
              7825,
              7830,
              7835,
              7840,
              7845,
              7850,
              7855,
              7860,
              7865,
              7870,
              7875,
              7880,
              7885,
              7890,
              7895,
              7900,
              7905,
              7910,
              7915,
              7930,
              7935,
              7945,
              7960,
              7970,
              7975,
              7980,
              7985,
              13100,
              13105,
              13110,
              13115,
              13120,
              13125,
              13130,
              13135,
              13140,
              13145,
              13150,
              13155,
              13160,
              13165,
              13170,
              13175,
              13180,
              13200,
              13205,
              13210,
              13215,
              13220,
              13225,
              13230,
              13235,
              13240,
              13245,
              13250,
              13255,
              13260,
              13270,
              13280,
              13290,
              13300,
              13310,
              13320,
              13330,
              13340,
              13350,
              13360,
              13370,
              13380,
              13390,
              13395,
              13400,
              13410,
              13420,
              13430,
              13440,
              13450,
              13460,
              13470,
              13480,
              13490,
              13510,
              13515,
              13520,
              13525,
              13530)
        )
    )
    namedValues = NamedValues(
        *(("a8b10bOutOfSync", 4755),
          ("activeVolumeSoftwareSignatureVerificationFailed", 7455),
          ("adminLockoutClear", 5050),
          ("adminLockoutOfUser", 5040),
          ("adminLogoutOfUser", 5020),
          ("aisAdministrationUnitAlarmIndicationSignal", 4040),
          ("aisMultiplexSectionAlarmIndicationSignal", 4010),
          ("aisTributaryUnitAlarmIndicationSignal", 4100),
          ("alarmCutoffIsInManualMode", 10),
          ("alarmIndicationSignal", 70),
          ("alarmIndicationSignalInTX", 5460),
          ("alarmIndicationSignalLine", 80),
          ("alarmIndicationSignalPath", 90),
          ("alarmIndicationSignalVT", 100),
          ("alarmUnknown", 1),
          ("alarmsAndEventsSuppressedForThisObject", 3590),
          ("alarmsSuppressedByUserCommand", 2730),
          ("alarmsSuppressedForMaintenance", 2740),
          ("alarmsSuppressedonOutOfGroupVcatMember", 6070),
          ("apcCannotSetValueDueToRangeLimits", 5780),
          ("apcWrongGain", 6740),
          ("apsChannelFailure", 110),
          ("apsChannelFarEndProtectionLineSignalDegrade", 3030),
          ("apsInvalidMode", 5490),
          ("archiveOfAuditLogFailed", 6350),
          ("auditLog100PercentFullOldestRecordsWillBeLost", 3764),
          ("auditLog80PercentFull", 3760),
          ("autoLaserShutdownDisabled", 6610),
          ("autoSensingDisabled", 7820),
          ("autoSensingUnableToDetectValidPayload", 7485),
          ("automaticLaserShutdown", 13180),
          ("automaticLaserShutoffDueToHighTemperature", 1730),
          ("automaticLogoutOfIdleUser", 5110),
          ("automaticPowerControlCorrectionSkipped", 5770),
          ("automaticPowerControlDisabled", 13245),
          ("automaticPowerControlFailure", 13235),
          ("automaticPowerControlTerminatedOnManualRequest", 6000),
          ("automaticSNCPSwitchCausedByAIS", 4350),
          ("automaticSNCPSwitchCausedByLOP", 4360),
          ("automaticSNCPSwitchCausedByPDI", 4380),
          ("automaticSNCPSwitchCausedBySDBER", 4400),
          ("automaticSNCPSwitchCausedBySFBER", 4390),
          ("automaticSNCPSwitchCausedByUNEQ", 4370),
          ("automaticSystemReset", 2150),
          ("automaticUPSRSwitchCausedByAIS", 2160),
          ("automaticUPSRSwitchCausedByLOP", 2170),
          ("automaticUPSRSwitchCausedByPDI", 2190),
          ("automaticUPSRSwitchCausedBySDBER", 2210),
          ("automaticUPSRSwitchCausedBySFBER", 2200),
          ("automaticUPSRSwitchCausedByUNEQ", 2180),
          ("automaticWdmAnsFinished", 5690),
          ("autonegotiationRemoteFailureIndication", 6490),
          ("autonomousMessagesInhibited", 3170),
          ("autonomousPMReportMessageInhibited", 2780),
          ("awgOverTemperature", 13470),
          ("awgTemperatureDegrade", 13450),
          ("awgTemperatureFailure", 13460),
          ("awgWarmUp", 13490),
          ("backPanelFacilityLoopback", 7870),
          ("backPanelTerminalLoopback", 7875),
          ("badPacketCountExceedsThreshold", 6470),
          ("batteryFailure", 5290),
          ("berThresholdExceededForSignalDegradeHighOrder", 4500),
          ("berThresholdExceededForSignalDegradeLine", 3360),
          ("berThresholdExceededForSignalDegradeLowOrder", 4520),
          ("berThresholdExceededForSignalDegradePath", 3370),
          ("berThresholdExceededForSignalDegradeVt", 6130),
          ("berThresholdExceededForSignalFailureHighOrder", 4510),
          ("berThresholdExceededForSignalFailureLine", 3380),
          ("berThresholdExceededForSignalFailureLowOrder", 4530),
          ("berThresholdExceededForSignalFailurePath", 3390),
          ("berThresholdExceededForSignalFailureVt", 6140),
          ("bertEnbl", 6970),
          ("bertSyncFail", 6975),
          ("biDirectionalFullPassThroughIsActive", 3090),
          ("bidirectionalForwardDetectionDown", 7780),
          ("bipolarViolation", 210),
          ("blsrMultiNodeTableUpdateCompleted", 2100),
          ("blsrOutOfSync", 2090),
          ("blsrSoftwareVersionMismatch", 6080),
          ("boardFailure", 1690),
          ("bothEndsOfFiberProvisionedAsEastOrBothAsWest", 3150),
          ("bridgeAndRollHasOccurred", 7055),
          ("bridgeAndRollIsPendingAValidSignal", 7060),
          ("cardPortsUnableToProvideProtection", 6920),
          ("carrierLossOnTheLAN", 220),
          ("caseTemperatureDegrade", 13420),
          ("cfmConfigurationError", 7360),
          ("cfmLoop", 7355),
          ("channelAutomaticProtectionSwitchModeMismatchAPS", 140),
          ("channelByteFailureAPS", 120),
          ("channelDefaultKAPS", 190),
          ("channelMSSPConnectionLossAPS", 4470),
          ("channelMSSPDefaultKAPS", 4460),
          ("channelMSSPImproperAPSCodeAPS", 4440),
          ("channelMSSPInconsistentAPSCode", 4430),
          ("channelMSSPNodeIdMismatchAPS", 4450),
          ("channelProtectionSwitchingChannelMatchFailureAPS", 130),
          ("channelShutdownDueToWavelengthDrift", 7465),
          ("chromaticDispersionValue", 7520),
          ("clockBusFailureTscA", 7160),
          ("clockBusFailureTscB", 7165),
          ("coldRestart", 2220),
          ("communicationFailurePeerToPeerSlotControlBusA", 3280),
          ("communicationFailurePeerToPeerSlotControlBusB", 3290),
          ("companionCardMissing", 7900),
          ("compositeClockHighLineVoltage", 6120),
          ("concatenationErrorSTS", 230),
          ("connectionEquipmentMismatch", 5260),
          ("connectionLoss", 200),
          ("controlBus1Failure", 990),
          ("controlBus2Failure", 1000),
          ("controlBusFailure", 980),
          ("controlEquipmentControlCommunicationsEquipmentFailure", 1370),
          ("controlEquipmentFailure", 950),
          ("controlPlaneUnverifiedClearedAlarmsPresent", 7905),
          ("controlProcessorFailure", 1380),
          ("controllerAToShelfSlotCommunicationFailure", 3300),
          ("controllerBToShelfSlotCommunicationFailure", 3310),
          ("coolingProfileMismatch", 7890),
          ("cppPeerNotResponding", 7265),
          ("crossConnectedCFMService", 7350),
          ("crossconnectLoopback", 5010),
          ("databaseBackupFailed", 3724),
          ("databaseRestoreFailed", 3726),
          ("dcuLossFailure", 7230),
          ("diagnosticFailure", 1700),
          ("disableInactiveClear", 5280),
          ("disableInactiveUser", 5270),
          ("doNotUseForSynchronization", 790),
          ("ds1LoopbackCommandSentToFarEnd", 6510),
          ("ds1LoopbackDueToFEACCommand", 1910),
          ("ds2LoopbackCommandSentToFarEnd", 1960),
          ("ds2LoopbackDueToFarEndCommand", 1950),
          ("ds3FrameFormatMismatch", 3600),
          ("ds3IdleCondition", 380),
          ("ds3LoopbackCommandSentToFarEnd", 1940),
          ("ds3LoopbackDueToFEACCommand", 1930),
          ("dspCommunicationFailure", 4980),
          ("dspFailure", 4985),
          ("duplicateNodeControllerDetected", 7970),
          ("duplicateNodeID", 2080),
          ("duplicateSerialNumberDetectedOnAPluggableEntity", 5570),
          ("duplicatedShelfIdentifier", 6380),
          ("e1LoopbackCommandSentToFarEnd", 4200),
          ("e1LoopbackDueToFEACCommand", 4190),
          ("e3IdleCondition", 4420),
          ("e3LoopbackCommandSentToFarEnd", 4270),
          ("e3LoopbackDueToFEACCommand", 4210),
          ("efmLinkMonitoringErroredFrameEvent", 6800),
          ("efmLinkMonitoringErroredFramePeriodEvent", 6810),
          ("efmLinkMonitoringErroredFrameSecondsSummary", 6820),
          ("efmLinkMonitoringErroredSymbolPeriodEvent", 6790),
          ("efmPeerMissing", 7330),
          ("efmRemoteFaultIndicationCriticalEvent", 6760),
          ("efmRemoteFaultIndicationDyingGasp", 6770),
          ("efmRemoteFaultIndicationLinkFault", 6780),
          ("efmRemoteLoopbackConfigured", 7325),
          ("efmRemoteLoopbackRequestFailed", 6830),
          ("embeddedOperationsChannelFailureLinkDown", 2040),
          ("encapsulationMismatchHighOrderPath", 5630),
          ("encapsulationMismatchLowOrderPath", 5640),
          ("encapsulationMismatchPath", 5610),
          ("encapsulationMismatchVT", 5620),
          ("enhancedRemoteFailureIndicationPathConnectivity", 5210),
          ("enhancedRemoteFailureIndicationPathPayload", 5220),
          ("enhancedRemoteFailureIndicationPathServer", 5200),
          ("eqptDegrade", 7335),
          ("equipmentFailure", 1660),
          ("equipmentHighLaserBias", 4825),
          ("equipmentHighLaserPeltier", 4835),
          ("equipmentHighLaserTemp", 4830),
          ("equipmentHighRxTemperature", 4960),
          ("equipmentHighTransceiverVoltage", 4850),
          ("equipmentHighTxPower", 4845),
          ("equipmentLowLaserBias", 4855),
          ("equipmentLowLaserPeltier", 4865),
          ("equipmentLowLaserTemp", 4860),
          ("equipmentLowRxTemperature", 4965),
          ("equipmentLowTransceiverVoltage", 4880),
          ("equipmentLowTxPower", 4875),
          ("equipmentPowerFailureAtConnectorA", 7000),
          ("equipmentPowerFailureAtConnectorB", 7005),
          ("equipmentPowerFailureAtReturnConnectorA", 7010),
          ("equipmentPowerFailureAtReturnConnectorB", 7015),
          ("equipmentRxLocked", 4885),
          ("equipmentSquelched", 4890),
          ("equipmentTxLocked", 4895),
          ("equipmentUnitPlugIn", 1840),
          ("equipmentUnitUnplugged", 1890),
          ("equipmentWavelengthMismatch", 4975),
          ("errorInStartupConfig", 3712),
          ("esmcFailure", 7615),
          ("etherRxExcessFlowCtrl", 3530),
          ("etherRxOverSubscribed", 3510),
          ("etherTxExcessFlowCtrl", 3520),
          ("etherTxOversubscribed", 3500),
          ("etherTxUnderrun", 3550),
          ("ethernetBridgeIsNewRootOfSpanningTree", 2010),
          ("ethernetBridgeTopologyChange", 2020),
          ("ethernetFlowPointFailed", 7800),
          ("ethernetOSCTerminationFailure", 7430),
          ("evaluationLicenseIsInUse", 7645),
          ("excessCollisionsOnTheLAN", 240),
          ("excessiveBackPropagation", 7340),
          ("excessiveSwitching", 40),
          ("exerciseRequestOnRing", 2850),
          ("exerciseRequestOnRingFailed", 3430),
          ("exerciseRequestOnSpan", 2860),
          ("exerciseRequestOnSpanFailed", 3440),
          ("exercisingRingSuccessfully", 3400),
          ("exercisingSpanSuccessfully", 3410),
          ("externalError", 30),
          ("extraTrafficPCADropped", 3490),
          ("extraTrafficPreempted", 2880),
          ("extremeHighVolt", 5300),
          ("extremeHighVoltBatteryA", 3620),
          ("extremeHighVoltBatteryB", 3640),
          ("extremeLowVolt", 5310),
          ("extremeLowVoltBatteryA", 3630),
          ("extremeLowVoltBatteryB", 3650),
          ("facilityFailure", 250),
          ("facilityHighRxPower", 4840),
          ("facilityLoopback", 1970),
          ("facilityLowRxPower", 4870),
          ("facilityTerminationEquipmentFailure", 1720),
          ("facilityTerminationEquipmentReceiverMissing", 1770),
          ("facilityTerminationEquipmentTransmitterMissing", 1780),
          ("failedToReceiveSynchronizationStatusMessage", 690),
          ("failureDetectedExternalToTheNE", 20),
          ("failureToReleaseFromProtection", 1740),
          ("failureToSwitchToProtection", 1790),
          ("failureToSwitchToProtectionHighOrderPath", 4540),
          ("failureToSwitchToProtectionLowOrderPath", 4550),
          ("failureToSwitchToProtectionPath", 1820),
          ("failureToSwitchToProtectionRing", 1800),
          ("failureToSwitchToProtectionSpan", 1810),
          ("fanFailure", 1830),
          ("farEndAIS", 260),
          ("farEndBERThresholdPassedForSignalDegradeRing", 3010),
          ("farEndBERThresholdPassedForSignalDegradeSpan", 3020),
          ("farEndBERThresholdPassedForSignalFailureRing", 2990),
          ("farEndBERThresholdPassedForSignalFailureSpan", 3000),
          ("farEndBlockError", 370),
          ("farEndCommonEquipmentFailureNonServiceAffecting", 330),
          ("farEndDS1EqptFailNonServiceAffecting", 280),
          ("farEndDS1EqptFailServiceAffecting", 290),
          ("farEndDS3EqptFailNonServiceAffecting", 310),
          ("farEndDS3EqptFailServiceAffecting", 320),
          ("farEndE1EqptFailNonServiceAffecting", 4230),
          ("farEndE1EqptFailServiceAffecting", 4240),
          ("farEndE3EqptFailNonServiceAffecting", 4280),
          ("farEndE3EqptFailServiceAffecting", 4260),
          ("farEndExercisingRing", 2970),
          ("farEndExercisingSpan", 2980),
          ("farEndForcedSwitchBackToWorkingSpan", 5810),
          ("farEndIDLE", 340),
          ("farEndLOF", 360),
          ("farEndLOS", 350),
          ("farEndLockoutOfProtectionAllSpans", 2920),
          ("farEndLockoutOfProtectionRing", 2910),
          ("farEndLockoutOfProtectionSpan", 3450),
          ("farEndLockoutOfWorkingRing", 2890),
          ("farEndLockoutOfWorkingSpan", 2900),
          ("farEndManualSwitchBackToWorkingSpan", 5800),
          ("farEndManualSwitchOfWorkingFacilityToProtectionRing", 2950),
          ("farEndManualSwitchOfWorkingFacilityToProtectionSpan", 2960),
          ("farEndMultipleDS1LOSDetectedOnDS3", 270),
          ("farEndMultipleE1LOSDetectedOnE3", 4220),
          ("farEndOfFiberIsProvisionedWithDifferentRingID", 3140),
          ("farEndProtectionLineFailure", 150),
          ("farEndSingleDS1LOS", 300),
          ("farEndSingleE1LOS", 4250),
          ("farEndWorkingFacilityForcedToSwitchToProtectionRing", 2930),
          ("farEndWorkingFacilityForcedToSwitchToProtectionSpan", 2940),
          ("fastAutomaticProtectionSwitching", 6840),
          ("fastAutomaticProtectionSwitchingConfigMismatch", 6850),
          ("fastStartSynchronizationMode", 860),
          ("faultInREPSegment", 7380),
          ("fcDistanceExtFuncNotEstablished", 6880),
          ("fecMismatch", 13170),
          ("fecUncorrectedWord", 4780),
          ("fiberTemperatureDegrade", 13430),
          ("fifthSynchronizationReferenceFailure", 670),
          ("firewallHasBeenDisabled", 5230),
          ("forcedSwitchBackToWorking", 2230),
          ("forcedSwitchBackToWorkingResultedInNoTrafficSwitch", 5560),
          ("forcedSwitchBackToWorkingRing", 2240),
          ("forcedSwitchBackToWorkingSpan", 2250),
          ("forcedSwitchRequest", 2690),
          ("forcedSwitchRequestOnRing", 3220),
          ("forcedSwitchRequestOnSpan", 3230),
          ("forcedSwitchToInternalClock", 3800),
          ("forcedSwitchToPrimaryReference", 3770),
          ("forcedSwitchToProtectResultedInNoTrafficSwitch", 5550),
          ("forcedSwitchToProtection", 2260),
          ("forcedSwitchToProtectionRing", 2270),
          ("forcedSwitchToProtectionSpan", 2280),
          ("forcedSwitchToSecondReference", 3780),
          ("forcedSwitchToThirdReference", 3790),
          ("forwardDefectIndication", 6420),
          ("fourthSynchronizationReferenceFailure", 660),
          ("freeMemoryOnCardNearZero", 2840),
          ("freeMemoryOnCardVeryLow", 2830),
          ("freeRunningSynchronizationMode", 840),
          ("frontPortLinkLoss", 6960),
          ("ftaMismatch", 6910),
          ("fuseAlarm", 1860),
          ("g811PrimaryReferenceClockTraceable", 4150),
          ("g812LocalNodeClockTraceable", 4170),
          ("g812TransitNodeClockTraceable", 4160),
          ("g813SynchronousEquipmentTimingSourceTraceable", 4180),
          ("gccTerminationFailure", 4785),
          ("gfpClientSignalFailDetected", 5700),
          ("gfpClientSignalFailDetectedDueToSigloss", 7495),
          ("gfpClientSignalFailDetectedDueToSyncloss", 7500),
          ("gfpExtensionHeaderMismatch", 5730),
          ("gfpFibreChannelDistanceExtensionBufferStarvation", 5670),
          ("gfpFibreChannelDistanceExtensionCreditStarvation", 5680),
          ("gfpFibreChannelDistanceExtensionMismatch", 5660),
          ("gfpLossOfFrameDelineation", 5710),
          ("gfpUserPayloadMismatch", 5650),
          ("gigaBitEthernetOutOfSync", 5380),
          ("highBitErrorRate", 7865),
          ("highOrderPathExcessiveErrors", 6550),
          ("highOrderPathSignalDegraded", 6540),
          ("highTemperature", 1670),
          ("highVolt", 5320),
          ("highVoltBatteryA", 4300),
          ("highVoltBatteryB", 4320),
          ("holdoverSynchronizationMode", 850),
          ("idleSignalCondition", 6170),
          ("idleSignalConditionInTx", 6180),
          ("improperAPSCode", 170),
          ("improperRemoval", 2070),
          ("incGfpOutOfFrame", 13520),
          ("incGfpSigLoss", 13525),
          ("incGfpSyncLoss", 13530),
          ("incSigloss", 13510),
          ("incSyncloss", 13515),
          ("incomingFailureCondition", 60),
          ("incomingOverheadSignalAbsent", 5740),
          ("inconsistentAPSCode", 160),
          ("industrialHighTemperature", 3805),
          ("inhibitSwitchToProtectRequestOnEquipment", 3340),
          ("inhibitSwitchToWorkingRequestOnEquipment", 3350),
          ("initializationInitiated", 2300),
          ("interconnectionEquipmentFailure", 1400),
          ("interconnectionEquipmentFailureProtectPayloadBus", 3330),
          ("interconnectionEquipmentFailureWorkingPayloadBus", 3320),
          ("interlinkFailure", 6730),
          ("internalError", 880),
          ("internalFault", 870),
          ("internalMessageError", 890),
          ("invalidAlarm", 3718),
          ("invalidLoginUsername", 5060),
          ("invalidMACAddress", 1680),
          ("invalidMuxponderConfiguration", 7885),
          ("ioSlotToXCONCommunicationFailure", 2790),
          ("iosConfigCopyFailed", 3660),
          ("iosConfigCopyInProgress", 3670),
          ("iosConfigCopySuccess", 3680),
          ("ipAddressAlreadyInUseWithinTheSameDccArea", 5500),
          ("isisAdjacencyFailure", 6290),
          ("kByteAPSChannelFailure", 5480),
          ("kBytesPassThroughIsActive", 3100),
          ("keyProgramOnAlteraFpgaFailed", 7960),
          ("lanConnectionPolarityReversed", 2760),
          ("laserApproachingEndOfLife", 5000),
          ("laserAutoPowerReduction", 13410),
          ("laserBiasDegrade", 13320),
          ("laserBiasFailure", 13330),
          ("laserShutdownDueToNonCiscoPPMInserted", 7425),
          ("laserShutdownDueToWavelengthDrift", 7415),
          ("laserTemperatureDegrade", 13340),
          ("lcasControlWordCrcCheckFailure", 5860),
          ("lcasSinkGroupError", 6860),
          ("lcasVcgMemberRxSideInDnuState", 6870),
          ("lcasVcgMemberRxSideInFailState", 5870),
          ("lcasVcgMemberTxSideInAddState", 5790),
          ("lcasVcgMemberTxSideInDnuState", 5850),
          ("licenseCountViolation", 7635),
          ("licenseIsExpired", 7630),
          ("licenseIsMissing", 7650),
          ("licenseWillExpireAnytimeAfter1DayButBefore14Days", 7625),
          ("licenseWillExpireWithin24Hours", 7620),
          ("lineDccTerminationFailure", 5360),
          ("lineIsInWaitToRestoreStateSDH", 4490),
          ("linkLayerKeepAliveFailure", 6480),
          ("lmpFailure", 6400),
          ("lmpHelloFSMToControlChannelDown", 3730),
          ("lmpNeighborDiscoveryHasFailed", 3740),
          ("lmpSignalDegrade", 6930),
          ("lmpSignalFailure", 6940),
          ("lmpUnallocatedDataLink", 6950),
          ("localFault", 7315),
          ("lockoutOfProtection", 2310),
          ("lockoutOfProtectionAllSpans", 3130),
          ("lockoutOfProtectionPath", 2340),
          ("lockoutOfProtectionRing", 2320),
          ("lockoutOfProtectionSpan", 2330),
          ("lockoutOfWorking", 2350),
          ("lockoutOfWorkingRing", 2360),
          ("lockoutOfWorkingSpan", 2370),
          ("lockoutSwitchRequest", 2700),
          ("lockoutSwitchRequestOnRing", 3240),
          ("lockoutSwitchRequestOnSpan", 3250),
          ("lofAdministrationUnitLossOfMultiFrame", 4560),
          ("loginOfUser", 5100),
          ("logoutOfUser", 5120),
          ("loopback", 1900),
          ("loopbackCommandSentToFarEndDS1", 1920),
          ("lopAdministrationUnitLossOfPointer", 4050),
          ("lopTributaryUnitLossOfPointer", 4090),
          ("losOfRamanSignal", 7245),
          ("lossOfAlignment", 5400),
          ("lossOfChannel", 13165),
          ("lossOfClockFromMateShelfController", 7210),
          ("lossOfContinuity", 13270),
          ("lossOfDFBSignal", 7835),
          ("lossOfFrame", 390),
          ("lossOfFrameInTX", 6200),
          ("lossOfMultiFrame", 4800),
          ("lossOfPointer", 400),
          ("lossOfPointerPath", 410),
          ("lossOfPointerVT", 420),
          ("lossOfSignal", 430),
          ("lossOfSignalForOpticalChannel", 5600),
          ("lossOfSynchronization", 610),
          ("lowOrderPathExcessiveErrors", 6570),
          ("lowOrderPathSignalDegraded", 6560),
          ("lowVolt", 5330),
          ("lowVoltBatteryA", 4290),
          ("lowVoltBatteryB", 4310),
          ("macBridgeDomainLimitReached", 7815),
          ("macSystemLimitReached", 7810),
          ("manualLaserRestart", 7420),
          ("manualSwitchBackToWorking", 2460),
          ("manualSwitchBackToWorkingResultedInNoTrafficSwitch", 5540),
          ("manualSwitchBackToWorkingRing", 2470),
          ("manualSwitchBackToWorkingSpan", 2480),
          ("manualSwitchOfWorkingFacilityOrEquipmentToProtectionPath", 2520),
          ("manualSwitchRequest", 2680),
          ("manualSwitchRequestOnRing", 3260),
          ("manualSwitchRequestOnSpan", 3270),
          ("manualSwitchToFifthReference", 2440),
          ("manualSwitchToFourthReference", 2430),
          ("manualSwitchToInternalClock", 2390),
          ("manualSwitchToPrimaryReference", 2400),
          ("manualSwitchToProtectResultedInNoTrafficSwitch", 5530),
          ("manualSwitchToProtection", 2490),
          ("manualSwitchToProtectionRing", 2500),
          ("manualSwitchToProtectionSpan", 2510),
          ("manualSwitchToSecondReference", 2410),
          ("manualSwitchToSixthReference", 2450),
          ("manualSwitchToThirdReference", 2420),
          ("manualSystemReset", 2380),
          ("manuallyCausedAbnormalCondition", 2000),
          ("manufacturingDataMemoryEEPROMFailure", 3460),
          ("masterKeyExchangeFailed", 7915),
          ("maxRPRStationNumberExceeded", 6640),
          ("mcastMacTableFull", 7250),
          ("mediumAccessControlFailure", 1710),
          ("minimumClockTraceableSDH", 4480),
          ("mismatchOfEquipmentAndAttributes", 900),
          ("moduleCommunicationFailure", 3762),
          ("msspMultiNodeTableUpdateCompleted", 4340),
          ("msspRingOutOfSync", 4330),
          ("msspSoftwareVersionMismatch", 6300),
          ("multicastMacAddressAliasing", 7255),
          ("multiplexSectionDccTerminationFailure", 5370),
          ("multiplexSectionExcessiveErrors", 6530),
          ("multiplexSectionSignalDegraded", 6520),
          ("nePowerFailureAtConnector", 1850),
          ("nePowerFailureAtConnectorA", 2810),
          ("nePowerFailureAtConnectorB", 2820),
          ("needToSaveRunningConfig", 3716),
          ("networkLoopback", 1980),
          ("networkMemoryPoolLow", 6590),
          ("networkTopologyIncomplete", 13215),
          ("noMoreResourcesAreAvailable", 7610),
          ("noStartupConfig", 3714),
          ("nodeIdMismatch", 180),
          ("nodeNameInUseWithinTheSameDccArea", 5510),
          ("nonCiscoPPMInserted", 6890),
          ("normalCondition", 2030),
          ("ntpOrSntpHostFailure", 3570),
          ("ochncMaintenance", 7235),
          ("oduk1AlarmIndicationSignal", 6010),
          ("oduk2AlarmIndicationSignal", 6020),
          ("oduk3AlarmIndicationSignal", 6030),
          ("oduk4AlarmIndicationSignal", 6040),
          ("odukLockedDefectPM", 4795),
          ("odukLockedDefectTCM1", 13110),
          ("odukLockedDefectTCM2", 13115),
          ("odukOpenConnectionIndication", 4805),
          ("odukOpenConnectionIndicationTCM1", 13125),
          ("odukOpenConnectionIndicationTCM2", 13130),
          ("odukPMAlarmIndicationSignal", 4760),
          ("odukPMBackwardDefectIndication", 4945),
          ("odukSignalDegrade", 4915),
          ("odukSignalDegradeTCM1", 13155),
          ("odukSignalDegradeTCM2", 13160),
          ("odukSignalFailure", 4905),
          ("odukSignalFailureTCM1", 13145),
          ("odukSignalFailureTCM2", 13150),
          ("odukTCM1AlarmIndicationSignal", 13100),
          ("odukTCM1BackwardDefectIndication", 4950),
          ("odukTCM2AlarmIndicationSignal", 13105),
          ("odukTCM2BackwardDefectIndication", 4955),
          ("odukTrailTraceIdentifierMismatch", 4815),
          ("odukTrailTraceIdentifierMismatchTCM1", 13135),
          ("odukTrailTraceIdentifierMismatchTCM2", 13140),
          ("openIOSlots", 7200),
          ("opticalAmplifierGainDegradeHigh", 13360),
          ("opticalAmplifierGainDegradeLow", 13350),
          ("opticalAmplifierGainFailureHigh", 13380),
          ("opticalAmplifierGainFailureLow", 13370),
          ("opticalAmplifierInitialization", 13480),
          ("opticalChannelActivationFailure", 13400),
          ("opticalChannelConnectionFailure", 13390),
          ("opticalChannelDeactivationFailure", 13205),
          ("opticalChannelIncomplete", 13395),
          ("opticalNetworkTypeMismatch", 13225),
          ("opticalPowerDegradeHigh", 13240),
          ("opticalPowerDegradeLow", 13230),
          ("opticalPowerFailureHigh", 13260),
          ("opticalPowerFailureLow", 13250),
          ("opticalSafetyRemoteInterlockOn", 5750),
          ("opticalTerminationIncomplete", 6410),
          ("optimized1Plus1ApsInvalidPrimarySection", 6110),
          ("optimized1Plus1ApsPrimaryFacility", 6090),
          ("optimized1Plus1ApsPrimarySectionMismatch", 6100),
          ("ospfHelloFail", 7185),
          ("ospfRoutingTableOverflow", 6600),
          ("otukAlarmIndicationSignal", 4765),
          ("otukIncomingAlignmentError", 4790),
          ("otukLossOfFrame", 13120),
          ("otukSMBackwardDefectIndication", 4770),
          ("otukSignalDegrade", 4910),
          ("otukSignalFailure", 4900),
          ("otukTrailTraceIdentifierMismatch", 4820),
          ("outOfChannelGroupBundle", 7365),
          ("outOfFrame", 440),
          ("outOfSynchronization", 620),
          ("outOfUseByAdministrativeCommand", 5410),
          ("outOfUseTransportFailure", 5420),
          ("outgoingFailureCondition", 810),
          ("overTemperatureUnitProtected", 7935),
          ("packetTransportServiceFailed", 7525),
          ("partialFanFailure", 3210),
          ("pathSelectorFailure", 450),
          ("payloadAutoSensingInProgress", 7490),
          ("payloadBusFailureToIOSlot12XCONSlot10", 1590),
          ("payloadBusFailureToIOSlot12XCONSlot8", 1470),
          ("payloadBusFailureToIOSlot13XCONSlot10", 1600),
          ("payloadBusFailureToIOSlot13XCONSlot8", 1480),
          ("payloadBusFailureToIOSlot14XCONSlot10", 1610),
          ("payloadBusFailureToIOSlot14XCONSlot8", 1490),
          ("payloadBusFailureToIOSlot15XCONSlot10", 1620),
          ("payloadBusFailureToIOSlot15XCONSlot8", 1500),
          ("payloadBusFailureToIOSlot16XCONSlot10", 1630),
          ("payloadBusFailureToIOSlot16XCONSlot8", 1510),
          ("payloadBusFailureToIOSlot17XCONSlot10", 1640),
          ("payloadBusFailureToIOSlot17XCONSlot8", 1520),
          ("payloadBusFailureToIOSlot1XCONSlot10", 1530),
          ("payloadBusFailureToIOSlot1XCONSlot8", 1410),
          ("payloadBusFailureToIOSlot2XCONSlot10", 1540),
          ("payloadBusFailureToIOSlot2XCONSlot8", 1420),
          ("payloadBusFailureToIOSlot3XCONSlot10", 1550),
          ("payloadBusFailureToIOSlot3XCONSlot8", 1430),
          ("payloadBusFailureToIOSlot4XCONSlot10", 1560),
          ("payloadBusFailureToIOSlot4XCONSlot8", 1440),
          ("payloadBusFailureToIOSlot5XCONSlot10", 1570),
          ("payloadBusFailureToIOSlot5XCONSlot8", 1450),
          ("payloadBusFailureToIOSlot6XCONSlot10", 1580),
          ("payloadBusFailureToIOSlot6XCONSlot8", 1460),
          ("payloadDefectIndication", 550),
          ("payloadDefectIndicationPath", 560),
          ("payloadLabelMismatchPath", 570),
          ("payloadMissingIndication", 6430),
          ("payloadTypeIdentifierMismatch", 4810),
          ("peerCardNotResponding", 3580),
          ("peerPortClientSignalFailDetected", 7460),
          ("peerStateMismatch", 2050),
          ("performanceMonitorThresholdCrossingAlert", 2120),
          ("plannedSwitchOver", 7590),
          ("pluggablePortMissing", 4920),
          ("pluggablePortRateMismatch", 4925),
          ("pluggablePortSecurityCodeMismatch", 4930),
          ("pluginModuleCommunicationFailure", 13220),
          ("pluginModuleRangeSettingsMismatch", 5840),
          ("pmdDegrade", 7510),
          ("portAddPowerDegradeHigh", 5930),
          ("portAddPowerDegradeLow", 5920),
          ("portAddPowerFailHigh", 5950),
          ("portAddPowerFailLow", 5940),
          ("portFAIL", 5900),
          ("powerConsumptionLimitHasCrossed", 7910),
          ("powerfailRestart", 2530),
          ("pprBackwardDefectIndication", 7300),
          ("pprCoordinatedMaintenance", 7305),
          ("pprForwardDefectIndication", 7295),
          ("pprTriggerThresholdBerExceeded", 7310),
          ("primaryNonVolatileBackupMemoryFailure", 960),
          ("primaryREPEdgePortElected", 7385),
          ("primarySynchronizationReferenceFailure", 630),
          ("proceduralError", 2060),
          ("programFailure", 940),
          ("protectLabelSwitchedPathAlarmIndicationSignal", 7765),
          ("protectLabelSwitchedPathDown", 7755),
          ("protectLabelSwitchedPathLinkDownIndication", 7845),
          ("protectLabelSwitchedPathLockReport", 7855),
          ("protectLabelSwitchedPathRemoteDefectIndication", 7775),
          ("protectLocalPseudowireNotForwarding", 7730),
          ("protectPseudowireConnectivityCheckDown", 7675),
          ("protectPseudowireControlPlaneDown", 7665),
          ("protectPseudowireLocalAcRxPortFault", 7700),
          ("protectPseudowireLocalAcTxPortFault", 7690),
          ("protectPseudowireNotForwarding", 7740),
          ("protectPseudowireRemoteAcRxPortFault", 7720),
          ("protectPseudowireRemoteAcTxPortFault", 7710),
          ("protectTpLockout", 7795),
          ("protectVolumeSoftwareSignatureVerificationFailed", 7450),
          ("protectionCardConfigurationMismatch", 7595),
          ("protectionSwitch", 2130),
          ("protectionUnitNotAvailable", 2110),
          ("provisioningMismatch", 6210),
          ("pseudowireDown", 7655),
          ("pseudowireTrafficSwitchedToProtection", 7680),
          ("ramanGainNotReached", 7285),
          ("ramanLaserShutdown", 7240),
          ("ramanPumpsCalibrationIsScheduledToRunInTheNextMinutes", 7985),
          ("ramanPumpsCalibrationProcedureIsRunning", 7980),
          ("ramanPwrProtOn", 7260),
          ("rdiHighOrderRemoteDefectOrAlarmIndication", 4080),
          ("rdiMultiplexSectionRemoteDefectOrAlarmIndication", 4020),
          ("rearPanelEthernetLinkRemoved", 5520),
          ("receiverFailure", 1750),
          ("recoveryOrServiceProtectionActionHasBeenInitiated", 2140),
          ("redundantPowerCapabilityLost", 3768),
          ("regeneratorSectionDccTerminationFailure", 6580),
          ("regeneratorSectionTraceIdentifierMismatch", 6230),
          ("remoteAlarmIndication", 460),
          ("remoteAlarmIndicationInTX", 5470),
          ("remoteAuthenticationFailSeeAuditLog", 6310),
          ("remoteDefectIndicationLine", 820),
          ("remoteDefectIndicationPath", 830),
          ("remoteFailureIndication", 470),
          ("remoteFailureIndicationLine", 480),
          ("remoteFailureIndicationPath", 490),
          ("remoteFailureIndicationVT", 500),
          ("remoteFault", 7320),
          ("remoteMaintenanceEndPointIsDown", 7345),
          ("repLinkFlapping", 7375),
          ("repNeighborAdjacencyFailure", 7370),
          ("replaceableEquipmentOrUnitIsMissing", 3470),
          ("reptdbchgMessagesInhibited", 3190),
          ("reservedBandwidthLinkRateExceededOnRinglet0", 6660),
          ("reservedBandwidthLinkRateExceededOnRinglet1", 6670),
          ("reservedForNetworkSynchronizationUse", 800),
          ("resourceAllocationFailed", 7830),
          ("restorationInProg", 7975),
          ("rfiLowOrderRemoteFailureOrAlarmIndication", 4140),
          ("ringIdMismatch", 13255),
          ("ringIsInWaitToRestoreState", 2670),
          ("ringIsSegmented", 3110),
          ("ringIsSquelchingHighOrderTraffic", 6450),
          ("ringIsSquelchingLowOrderTraffic", 6460),
          ("ringIsSquelchingStsTraffic", 6330),
          ("ringIsSquelchingTraffic", 2540),
          ("ringIsSquelchingVtTraffic", 6340),
          ("ringSwitchIsActiveOnTheEastSide", 3040),
          ("ringSwitchIsActiveOnTheWestSide", 3050),
          ("ringTopologyIsUnderConstruction", 3120),
          ("rmonHistoriesAndAlarmsResetReboot", 2710),
          ("rmonThresholdCrossingAlarm", 2720),
          ("routerProcessorSwitchOver", 7600),
          ("rprInterfaceInPassThroughMode", 6680),
          ("rprPeerNodeIsMissing", 6690),
          ("rprProtectionConfigurationMismatched", 6650),
          ("rprProtectionIsActive", 6630),
          ("rprRiFailure", 6700),
          ("rprSignalDegrade", 6720),
          ("rprSignalFailure", 6710),
          ("rprSpanMismatch", 6750),
          ("rprWrapped", 6360),
          ("rsvpHelloFSMToNeighborDown", 3720),
          ("runningLowOnResources", 7605),
          ("satellitePanelActiveLinkFailure", 7535),
          ("satellitePanelBatteryFailureA", 7585),
          ("satellitePanelBatteryFailureB", 7860),
          ("satellitePanelCommunicationFailure", 7540),
          ("satellitePanelDiscoveryFailure", 7530),
          ("satellitePanelFANManufacturingDataMemoryEEPROMFailure", 7565),
          ("satellitePanelFANUnitIsMissing", 7570),
          ("satellitePanelFanFailure", 7555),
          ("satellitePanelFanMismatchOfEquipmentAndAttributes", 7550),
          ("satellitePanelHighTemperature", 7580),
          ("satellitePanelImproperConfiguration", 7545),
          ("satellitePanelIndustrialHighTemperature", 7575),
          ("satellitePanelPartialFanFailure", 7560),
          ("sdccTerminationFailure", 50),
          ("sdhSpanIsInWaitToRestoreState", 4570),
          ("secondaryNonVolatileBackupMemoryFailure", 970),
          ("secondaryREPEdgePortElected", 7390),
          ("secondarySynchronizationReferenceFailure", 640),
          ("sectionTraceIdentifierMismatch", 6220),
          ("securityIntrusionDetPwd", 5240),
          ("securityIntrusionDetUser", 5250),
          ("securityInvalidLoginAlreadyLoggedOn", 5090),
          ("securityInvalidLoginLockedOut", 5080),
          ("securityInvalidLoginPassword", 5070),
          ("securityInvalidLoginUsername", 3722),
          ("securityInvalidLoginUsernameSeeAuditTrail", 3160),
          ("securityUserIDHasExpired", 3200),
          ("seqMismatchCount", 7945),
          ("sequenceMismatch", 5390),
          ("sessionTimeLimitExpired", 6270),
          ("severelyErroredFrame", 520),
          ("shelfCommunicationFailure", 6370),
          ("shutterInsertionLossVariationDegradeHigh", 13210),
          ("shutterInsertionLossVariationDegradeLow", 13200),
          ("shutterOpen", 13440),
          ("signalDegrade", 510),
          ("signalFailure", 530),
          ("signalLabelMismatchFailure", 540),
          ("signalLabelMismatchFailurePayloadLabelMismatchVT", 580),
          ("signalLabelMismatchFailureUnequippedVT", 600),
          ("signalLossOnDataInterface", 5880),
          ("signalingUnableToSetupCircuit", 3710),
          ("sixthSynchronizationReferenceFailure", 680),
          ("slaThresholdCrossAlert", 7725),
          ("slmfPLMHighOrderPathLabelMismatch", 4070),
          ("slmfPLMLowOrderPathLabelMismatch", 4120),
          ("slmfUnequippedHighOrderPathUnequipped", 4060),
          ("slmfUnequippedLowOrderPathUnequipped", 4110),
          ("slotCommunicationDisabled", 6260),
          ("smBackwardIncomingAlignmentError", 7825),
          ("softwareDownloadFailed", 3480),
          ("softwareDownloadInProgress", 2550),
          ("softwareFaultDataIntegrityFault", 930),
          ("softwareFaultOrFailure", 920),
          ("softwareMismatch", 6390),
          ("softwareSignatureVerificationFailed", 7445),
          ("sonetMinimumClockTraceable", 770),
          ("spanIsInWaitToRestoreState", 3420),
          ("spanLengthOutOfRange", 6150),
          ("spanMeasurementCannotBePerformed", 6440),
          ("spanSwitchIsActiveOnTheEastSide", 3060),
          ("spanSwitchIsActiveOnTheWestSide", 3070),
          ("squelchingPath", 2870),
          ("standbyDatabaseOutOfSync", 3766),
          ("standbyTccNEClockIsInternalClock", 7515),
          ("stcnREPGenerated", 7395),
          ("stmConcatenationError", 4410),
          ("stratum1PrimaryReferenceSourceTraceable", 710),
          ("stratum2Traceable", 730),
          ("stratum3ETraceable", 750),
          ("stratum3Traceable", 760),
          ("stratum4Traceable", 780),
          ("stsPathTraceIdentifierMismatch", 2800),
          ("suspendUser", 5340),
          ("suspendUserClear", 5350),
          ("switchToFifthReference", 2610),
          ("switchToFourthReference", 2600),
          ("switchToInternalClock", 2560),
          ("switchToPrimaryReference", 2570),
          ("switchToSecondReference", 2580),
          ("switchToSixthReference", 2620),
          ("switchToThirdReference", 2590),
          ("switchedBackToWorking", 2640),
          ("switchedToProtection", 2650),
          ("switchingMatrixModuleFailure", 2750),
          ("switchingMatrixModuleFailureProtect", 6250),
          ("switchingMatrixModuleFailureWorking", 6240),
          ("synchronizationLossOnDataInterface", 5890),
          ("synchronizationReferenceFrequencyOutOfBounds", 3560),
          ("synchronizationStatusMessagesAreDisabledOnThisInterface", 700),
          ("synchronizationSwitchingEquipmentFailure", 1880),
          ("synchronizationUnitFailure", 1870),
          ("synchronizedTraceabilityUnknown", 720),
          ("systemReboot", 2630),
          ("tccAToDCCAProcessorCommunicationFailure", 1180),
          ("tccAToShelfSlot10XCONBCommunicationFailure", 1100),
          ("tccAToShelfSlot11TCCBCommunicationFailure", 1110),
          ("tccAToShelfSlot12TRUNK3CommunicationFailure", 1120),
          ("tccAToShelfSlot13TRUNK4CommunicationFailure", 1130),
          ("tccAToShelfSlot14DROP5CommunicationFailure", 1140),
          ("tccAToShelfSlot15DROP6CommunicationFailure", 1150),
          ("tccAToShelfSlot16DROP7CommunicationFailure", 1160),
          ("tccAToShelfSlot17DROP8CommunicationFailure", 1170),
          ("tccAToShelfSlot1DROP1CommunicationFailure", 1010),
          ("tccAToShelfSlot2DROP2CommunicationFailure", 1020),
          ("tccAToShelfSlot3DROP3CommunicationFailure", 1030),
          ("tccAToShelfSlot4DROP4CommunicationFailure", 1040),
          ("tccAToShelfSlot5TRUNK1CommunicationFailure", 1050),
          ("tccAToShelfSlot6TRUNK2CommunicationFailure", 1060),
          ("tccAToShelfSlot7TCCACommunicationFailure", 1070),
          ("tccAToShelfSlot8XCONACommunicationFailure", 1080),
          ("tccAToShelfSlot9AICCommunicationFailure", 1090),
          ("tccBToDCCBProcessorCommunicationFailure", 1360),
          ("tccBToShelfSlot10XCONBCommunicationFailure", 1280),
          ("tccBToShelfSlot11TCCBCommunicationFailure", 1290),
          ("tccBToShelfSlot12TRUNK3CommunicationFailure", 1300),
          ("tccBToShelfSlot13TRUNK4CommunicationFailure", 1310),
          ("tccBToShelfSlot14DROP5CommunicationFailure", 1320),
          ("tccBToShelfSlot15DROP6CommunicationFailure", 1330),
          ("tccBToShelfSlot16DROP7CommunicationFailure", 1340),
          ("tccBToShelfSlot17DROP8CommunicationFailure", 1350),
          ("tccBToShelfSlot1DROP1CommunicationFailure", 1190),
          ("tccBToShelfSlot2DROP2CommunicationFailure", 1200),
          ("tccBToShelfSlot3DROP3CommunicationFailure", 1210),
          ("tccBToShelfSlot4DROP4CommunicationFailure", 1220),
          ("tccBToShelfSlot5TRUNK1CommunicationFailure", 1230),
          ("tccBToShelfSlot6TRUNK2CommunicationFailure", 1240),
          ("tccBToShelfSlot7TCCACommunicationFailure", 1250),
          ("tccBToShelfSlot8XCONACommunicationFailure", 1260),
          ("tccBToShelfSlot9AICCommunicationFailure", 1270),
          ("tci1ClockFailure", 4940),
          ("tci2ClockFailure", 4970),
          ("tciNotSelected", 4935),
          ("teTunnelDown", 7805),
          ("temperatureReadingMismatchBetweenSCCards", 6050),
          ("temporaryLicenseIsInUse", 7640),
          ("terminalLoopback", 1990),
          ("thirdSynchronizationReferenceFailure", 650),
          ("timHighOrderTraceIdentifierMismatchFailure", 4030),
          ("timLowOrderTraceIdentifierMismatchFailure", 4130),
          ("timSectionMonitorTraceIdentifierMismatchFailure", 13175),
          ("timSectionTraceIdentifierMismatchFailure", 4000),
          ("timeSlotInterchangeEquipmentFailure", 1650),
          ("tpTrafficSwitchedFromWorkingToProtection", 7785),
          ("tpTunnelDown", 7745),
          ("trafficStormOnLANLANTemporarilyDisabled", 3180),
          ("trailSignalFail", 6500),
          ("transitNodeClockTraceable", 740),
          ("transmitFailure", 1760),
          ("transportLayerFailure", 3540),
          ("trunkOduAlarmIndicationSignal", 7895),
          ("trunkPayloadTypeMismatch", 7880),
          ("unauthorizedIncomingSignalingRequest", 3750),
          ("unequippedPath", 590),
          ("uniDirectionalFullPassThroughIsActive", 3080),
          ("unitHighTemperature", 7930),
          ("universalTransponderModuleCommunicationFailure", 5830),
          ("universalTransponderModuleHardwareFailure", 5820),
          ("unqualifiedPPMInserted", 6900),
          ("unreachablePortTargetPower", 5910),
          ("usbSyncInProgress", 7480),
          ("usbWriteFailure", 7475),
          ("userLockedOut", 5030),
          ("userPasswordChangeRequired", 6280),
          ("variableOpticalAttenuatorDegradeHigh", 13290),
          ("variableOpticalAttenuatorDegradeLow", 13280),
          ("variableOpticalAttenuatorFailureHigh", 13310),
          ("variableOpticalAttenuatorFailureLow", 13300),
          ("vcatGroupDegraded", 5440),
          ("vcatGroupDown", 5430),
          ("vcatGroupIncomplete", 5450),
          ("virtualLanAlarmIndiacationSignal", 7225),
          ("vlbREPActivated", 7400),
          ("vlbREPTriggerSoakingDelayActive", 7405),
          ("voaControlLoopDisableDueToExcessiveCounterPropagationLight", 7275),
          ("voltageReadingMismatchBetweenSCCards", 6060),
          ("vtPathTraceIdentifierMismatch", 6190),
          ("waitToRestore", 3610),
          ("wanSyncloss", 7410),
          ("warmRestart", 2660),
          ("watchdogTimerTimeout", 910),
          ("wizardIsRunning", 7280),
          ("workQueueFull", 6980),
          ("workingFacilityOrEquipmentForcedToSwitchToProtectionPath", 2290),
          ("workingLabelSwitchedPathAlarmIndicationSignal", 7760),
          ("workingLabelSwitchedPathDown", 7750),
          ("workingLabelSwitchedPathLinkDownIndication", 7840),
          ("workingLabelSwitchedPathLockReport", 7850),
          ("workingLabelSwitchedPathRemoteDefectIndication", 7770),
          ("workingMemoryFailure", 1390),
          ("workingPseudowireConnectivityCheckDown", 7670),
          ("workingPseudowireControlPlaneDown", 7660),
          ("workingPseudowireLocalAcRxPortFault", 7695),
          ("workingPseudowireLocalAcTxPortFault", 7685),
          ("workingPseudowireNotForwarding", 7735),
          ("workingPseudowireRemoteAcRxPortFault", 7715),
          ("workingPseudowireRemoteAcTxPortFault", 7705),
          ("workingTpLockout", 7790))
    )



class Cerent454EntityClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              30,
              50,
              60,
              70,
              71,
              80,
              90,
              100,
              110,
              120,
              130,
              140,
              141,
              150,
              160,
              161,
              170,
              180,
              190,
              200,
              210,
              220,
              230,
              240,
              250,
              260,
              270,
              280,
              290,
              360,
              390,
              410,
              411,
              420,
              421,
              430,
              440,
              450,
              480,
              490,
              500,
              510,
              520,
              530,
              540,
              550,
              560,
              600,
              630,
              640,
              650,
              660,
              670,
              680,
              690,
              700,
              710,
              720,
              730,
              740,
              750,
              760,
              770,
              780,
              790,
              800,
              810,
              820,
              830,
              840,
              850,
              860,
              870,
              880,
              890,
              900,
              910,
              920,
              930,
              940,
              950,
              960,
              970,
              980,
              990,
              1000,
              1010,
              1020,
              1030,
              1040,
              1050,
              1060,
              1070,
              1080,
              1090,
              1100,
              1110,
              3200,
              3210,
              3220,
              3230,
              3240,
              3250,
              3260,
              3270,
              3280,
              3290,
              3300,
              3310,
              3320,
              3330,
              3350,
              3360)
        )
    )
    namedValues = NamedValues(
        *(("aip", 80),
          ("almExpPanel", 120),
          ("almIfExtnsn", 130),
          ("aots", 3200),
          ("backplane", 30),
          ("bic", 890),
          ("bits", 220),
          ("cap", 930),
          ("ce1000", 1020),
          ("ce100t", 840),
          ("cemr", 1030),
          ("chgrp", 3270),
          ("crs", 100),
          ("ds1", 390),
          ("ds3", 110),
          ("ds3i", 660),
          ("dwdm8b10b", 250),
          ("dwdmClient", 150),
          ("dwdmData", 940),
          ("dwdmFec", 230),
          ("dwdmOcn", 740),
          ("dwdmOptics", 180),
          ("dwdmOtn", 270),
          ("dwdmPm", 760),
          ("dwdmScl", 710),
          ("dwdmSfp", 700),
          ("dwdmSm", 750),
          ("dwdmTcm", 770),
          ("dwdmTcm1", 720),
          ("dwdmTcm2", 730),
          ("dwdmTrunk", 170),
          ("e1", 600),
          ("e1000t", 550),
          ("e100t", 540),
          ("e3", 630),
          ("e4", 640),
          ("ec1", 510),
          ("ec1p1", 980),
          ("ecu", 3300),
          ("entOptics", 830),
          ("envAlrm", 280),
          ("envCtrl", 290),
          ("eqpt", 50),
          ("escon", 880),
          ("ether", 1090),
          ("etherBridge", 560),
          ("extSynchRef", 260),
          ("fUdc", 430),
          ("fanTray", 90),
          ("fc", 970),
          ("fcmr", 820),
          ("fe", 3330),
          ("g1000", 670),
          ("ge", 960),
          ("gfp", 900),
          ("gige", 910),
          ("hdlc", 3280),
          ("ib", 3260),
          ("isc", 870),
          ("lcdFlash", 3310),
          ("lmp", 1040),
          ("lmpControlChannel", 1050),
          ("lmpDataLink", 1070),
          ("lmpTeLink", 1060),
          ("logFac", 950),
          ("ml1000", 690),
          ("ml100t", 680),
          ("mlFx", 990),
          ("mlmr", 1100),
          ("msISC", 3290),
          ("msUdc", 440),
          ("ne", 10),
          ("neRing", 360),
          ("neSynchRef", 240),
          ("och", 3230),
          ("ochTerm", 1000),
          ("ochnc", 3250),
          ("ocn", 70),
          ("odu0", 3350),
          ("odu1", 3360),
          ("oms", 3220),
          ("osc", 3240),
          ("ots", 3210),
          ("otu", 1110),
          ("port", 60),
          ("pos", 920),
          ("ppm", 850),
          ("ps", 520),
          ("psSts", 190),
          ("psVt", 530),
          ("pwr", 780),
          ("rpr", 1080),
          ("rsms", 200),
          ("shelf", 1010),
          ("spareSdcc", 450),
          ("stm1E", 650),
          ("stmn", 71),
          ("stsMon", 140),
          ("stsTerm", 160),
          ("stsTermVcat", 790),
          ("twor", 860),
          ("ucpCircuit", 480),
          ("ucpIpcc", 490),
          ("ucpNeighbor", 500),
          ("unknownEntity", 1),
          ("usb", 3320),
          ("vcMonHp", 141),
          ("vcMonLp", 411),
          ("vcTermHp", 161),
          ("vcTermLP", 421),
          ("vcatGroup", 810),
          ("vtMon", 410),
          ("vtTerm", 420),
          ("vtTermVcat", 800),
          ("xcSts", 210))
    )



# MIB Managed Objects in the order of their OIDs

_Cerent454Mib_ObjectIdentity = ObjectIdentity
cerent454Mib = _Cerent454Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10)
)
if mibBuilder.loadTexts:
    cerent454Mib.setStatus("current")
_Cerent454Conformance_ObjectIdentity = ObjectIdentity
cerent454Conformance = _Cerent454Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 10)
)
if mibBuilder.loadTexts:
    cerent454Conformance.setStatus("current")
_Cerent454Groups_ObjectIdentity = ObjectIdentity
cerent454Groups = _Cerent454Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 10, 10)
)
if mibBuilder.loadTexts:
    cerent454Groups.setStatus("current")
_Cerent454Compliance_ObjectIdentity = ObjectIdentity
cerent454Compliance = _Cerent454Compliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 10, 20)
)
if mibBuilder.loadTexts:
    cerent454Compliance.setStatus("current")
_Cerent454Objects_ObjectIdentity = ObjectIdentity
cerent454Objects = _Cerent454Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20)
)
if mibBuilder.loadTexts:
    cerent454Objects.setStatus("current")
_Cerent454GeneralGroup_ObjectIdentity = ObjectIdentity
cerent454GeneralGroup = _Cerent454GeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 20)
)
if mibBuilder.loadTexts:
    cerent454GeneralGroup.setStatus("current")
_Cerent454SoftwareVersion_Type = DisplayString
_Cerent454SoftwareVersion_Object = MibScalar
cerent454SoftwareVersion = _Cerent454SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 20, 10),
    _Cerent454SoftwareVersion_Type()
)
cerent454SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454SoftwareVersion.setStatus("current")
_Cerent454AlarmGroup_ObjectIdentity = ObjectIdentity
cerent454AlarmGroup = _Cerent454AlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30)
)
if mibBuilder.loadTexts:
    cerent454AlarmGroup.setStatus("current")
_Cerent454AlarmCount_Type = Unsigned32
_Cerent454AlarmCount_Object = MibScalar
cerent454AlarmCount = _Cerent454AlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 10),
    _Cerent454AlarmCount_Type()
)
cerent454AlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454AlarmCount.setStatus("current")
_Cerent454AlarmTable_Object = MibTable
cerent454AlarmTable = _Cerent454AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20)
)
if mibBuilder.loadTexts:
    cerent454AlarmTable.setStatus("current")
_Cerent454AlarmEntry_Object = MibTableRow
cerent454AlarmEntry = _Cerent454AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1)
)
cerent454AlarmEntry.setIndexNames(
    (0, "CERENT-454-MIB", "cerent454AlarmIndex"),
    (0, "CERENT-454-MIB", "cerent454AlarmType"),
)
if mibBuilder.loadTexts:
    cerent454AlarmEntry.setStatus("current")


class _Cerent454AlarmIndex_Type(Integer32):
    """Custom type cerent454AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Cerent454AlarmIndex_Type.__name__ = "Integer32"
_Cerent454AlarmIndex_Object = MibTableColumn
cerent454AlarmIndex = _Cerent454AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1, 10),
    _Cerent454AlarmIndex_Type()
)
cerent454AlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerent454AlarmIndex.setStatus("current")
_Cerent454AlarmObjectType_Type = Cerent454EntityClass
_Cerent454AlarmObjectType_Object = MibTableColumn
cerent454AlarmObjectType = _Cerent454AlarmObjectType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1, 20),
    _Cerent454AlarmObjectType_Type()
)
cerent454AlarmObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454AlarmObjectType.setStatus("current")
_Cerent454AlarmSlotNumber_Type = Integer32
_Cerent454AlarmSlotNumber_Object = MibTableColumn
cerent454AlarmSlotNumber = _Cerent454AlarmSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1, 30),
    _Cerent454AlarmSlotNumber_Type()
)
cerent454AlarmSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454AlarmSlotNumber.setStatus("current")
_Cerent454AlarmPortNumber_Type = CerentPortNumber
_Cerent454AlarmPortNumber_Object = MibTableColumn
cerent454AlarmPortNumber = _Cerent454AlarmPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1, 40),
    _Cerent454AlarmPortNumber_Type()
)
cerent454AlarmPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454AlarmPortNumber.setStatus("current")
_Cerent454AlarmLineNumber_Type = Integer32
_Cerent454AlarmLineNumber_Object = MibTableColumn
cerent454AlarmLineNumber = _Cerent454AlarmLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1, 50),
    _Cerent454AlarmLineNumber_Type()
)
cerent454AlarmLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454AlarmLineNumber.setStatus("current")
_Cerent454AlarmObjectIndex_Type = Integer32
_Cerent454AlarmObjectIndex_Object = MibTableColumn
cerent454AlarmObjectIndex = _Cerent454AlarmObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1, 60),
    _Cerent454AlarmObjectIndex_Type()
)
cerent454AlarmObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454AlarmObjectIndex.setStatus("current")
_Cerent454AlarmType_Type = Cerent454AlarmType
_Cerent454AlarmType_Object = MibTableColumn
cerent454AlarmType = _Cerent454AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1, 70),
    _Cerent454AlarmType_Type()
)
cerent454AlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454AlarmType.setStatus("current")
_Cerent454AlarmState_Type = CerentNotificationClass
_Cerent454AlarmState_Object = MibTableColumn
cerent454AlarmState = _Cerent454AlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1, 80),
    _Cerent454AlarmState_Type()
)
cerent454AlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454AlarmState.setStatus("current")
_Cerent454AlarmTimeStamp_Type = TimeStamp
_Cerent454AlarmTimeStamp_Object = MibTableColumn
cerent454AlarmTimeStamp = _Cerent454AlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1, 90),
    _Cerent454AlarmTimeStamp_Type()
)
cerent454AlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454AlarmTimeStamp.setStatus("current")
_Cerent454AlarmObjectName_Type = DisplayString
_Cerent454AlarmObjectName_Object = MibTableColumn
cerent454AlarmObjectName = _Cerent454AlarmObjectName_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1, 100),
    _Cerent454AlarmObjectName_Type()
)
cerent454AlarmObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454AlarmObjectName.setStatus("current")
_Cerent454AlarmAdditionalInfo_Type = DisplayString
_Cerent454AlarmAdditionalInfo_Object = MibTableColumn
cerent454AlarmAdditionalInfo = _Cerent454AlarmAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1, 110),
    _Cerent454AlarmAdditionalInfo_Type()
)
cerent454AlarmAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454AlarmAdditionalInfo.setStatus("current")
_Cerent454AlarmSeverity_Type = CerentAlarmSeverity
_Cerent454AlarmSeverity_Object = MibTableColumn
cerent454AlarmSeverity = _Cerent454AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1, 120),
    _Cerent454AlarmSeverity_Type()
)
cerent454AlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454AlarmSeverity.setStatus("current")
_Cerent454AlarmStatus_Type = CerentAlarmStatus
_Cerent454AlarmStatus_Object = MibTableColumn
cerent454AlarmStatus = _Cerent454AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1, 130),
    _Cerent454AlarmStatus_Type()
)
cerent454AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454AlarmStatus.setStatus("current")
_Cerent454AlarmServiceAffecting_Type = CerentAlarmServiceAffecting
_Cerent454AlarmServiceAffecting_Object = MibTableColumn
cerent454AlarmServiceAffecting = _Cerent454AlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 20, 1, 140),
    _Cerent454AlarmServiceAffecting_Type()
)
cerent454AlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454AlarmServiceAffecting.setStatus("current")
_Cerent454ReportedAlarmCount_Type = Unsigned32
_Cerent454ReportedAlarmCount_Object = MibScalar
cerent454ReportedAlarmCount = _Cerent454ReportedAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 30),
    _Cerent454ReportedAlarmCount_Type()
)
cerent454ReportedAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ReportedAlarmCount.setStatus("current")
_Cerent454ReportedAlarmTable_Object = MibTable
cerent454ReportedAlarmTable = _Cerent454ReportedAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 40)
)
if mibBuilder.loadTexts:
    cerent454ReportedAlarmTable.setStatus("current")
_Cerent454ReportedAlarmEntry_Object = MibTableRow
cerent454ReportedAlarmEntry = _Cerent454ReportedAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 40, 1)
)
cerent454ReportedAlarmEntry.setIndexNames(
    (0, "CERENT-454-MIB", "cerent454ReportedAlarmIndex"),
    (0, "CERENT-454-MIB", "cerent454ReportedAlarmType"),
)
if mibBuilder.loadTexts:
    cerent454ReportedAlarmEntry.setStatus("current")


class _Cerent454ReportedAlarmIndex_Type(Integer32):
    """Custom type cerent454ReportedAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Cerent454ReportedAlarmIndex_Type.__name__ = "Integer32"
_Cerent454ReportedAlarmIndex_Object = MibTableColumn
cerent454ReportedAlarmIndex = _Cerent454ReportedAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 40, 1, 10),
    _Cerent454ReportedAlarmIndex_Type()
)
cerent454ReportedAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerent454ReportedAlarmIndex.setStatus("current")
_Cerent454ReportedAlarmObjectType_Type = Cerent454EntityClass
_Cerent454ReportedAlarmObjectType_Object = MibTableColumn
cerent454ReportedAlarmObjectType = _Cerent454ReportedAlarmObjectType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 40, 1, 20),
    _Cerent454ReportedAlarmObjectType_Type()
)
cerent454ReportedAlarmObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ReportedAlarmObjectType.setStatus("current")
_Cerent454ReportedAlarmSlotNumber_Type = Integer32
_Cerent454ReportedAlarmSlotNumber_Object = MibTableColumn
cerent454ReportedAlarmSlotNumber = _Cerent454ReportedAlarmSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 40, 1, 30),
    _Cerent454ReportedAlarmSlotNumber_Type()
)
cerent454ReportedAlarmSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ReportedAlarmSlotNumber.setStatus("current")
_Cerent454ReportedAlarmPortNumber_Type = CerentPortNumber
_Cerent454ReportedAlarmPortNumber_Object = MibTableColumn
cerent454ReportedAlarmPortNumber = _Cerent454ReportedAlarmPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 40, 1, 40),
    _Cerent454ReportedAlarmPortNumber_Type()
)
cerent454ReportedAlarmPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ReportedAlarmPortNumber.setStatus("current")
_Cerent454ReportedAlarmObjectIndex_Type = Integer32
_Cerent454ReportedAlarmObjectIndex_Object = MibTableColumn
cerent454ReportedAlarmObjectIndex = _Cerent454ReportedAlarmObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 40, 1, 50),
    _Cerent454ReportedAlarmObjectIndex_Type()
)
cerent454ReportedAlarmObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ReportedAlarmObjectIndex.setStatus("current")
_Cerent454ReportedAlarmType_Type = Cerent454AlarmType
_Cerent454ReportedAlarmType_Object = MibTableColumn
cerent454ReportedAlarmType = _Cerent454ReportedAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 40, 1, 60),
    _Cerent454ReportedAlarmType_Type()
)
cerent454ReportedAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ReportedAlarmType.setStatus("current")
_Cerent454ReportedAlarmTimeStamp_Type = TimeStamp
_Cerent454ReportedAlarmTimeStamp_Object = MibTableColumn
cerent454ReportedAlarmTimeStamp = _Cerent454ReportedAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 40, 1, 70),
    _Cerent454ReportedAlarmTimeStamp_Type()
)
cerent454ReportedAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ReportedAlarmTimeStamp.setStatus("current")
_Cerent454ReportedAlarmObjectName_Type = DisplayString
_Cerent454ReportedAlarmObjectName_Object = MibTableColumn
cerent454ReportedAlarmObjectName = _Cerent454ReportedAlarmObjectName_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 40, 1, 80),
    _Cerent454ReportedAlarmObjectName_Type()
)
cerent454ReportedAlarmObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ReportedAlarmObjectName.setStatus("current")
_Cerent454ReportedAlarmAdditionalInfo_Type = DisplayString
_Cerent454ReportedAlarmAdditionalInfo_Object = MibTableColumn
cerent454ReportedAlarmAdditionalInfo = _Cerent454ReportedAlarmAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 40, 1, 90),
    _Cerent454ReportedAlarmAdditionalInfo_Type()
)
cerent454ReportedAlarmAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ReportedAlarmAdditionalInfo.setStatus("current")
_Cerent454ReportedAlarmSeverity_Type = CerentAlarmSeverity
_Cerent454ReportedAlarmSeverity_Object = MibTableColumn
cerent454ReportedAlarmSeverity = _Cerent454ReportedAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 40, 1, 100),
    _Cerent454ReportedAlarmSeverity_Type()
)
cerent454ReportedAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ReportedAlarmSeverity.setStatus("current")
_Cerent454ReportedAlarmStatus_Type = CerentAlarmStatus
_Cerent454ReportedAlarmStatus_Object = MibTableColumn
cerent454ReportedAlarmStatus = _Cerent454ReportedAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 40, 1, 110),
    _Cerent454ReportedAlarmStatus_Type()
)
cerent454ReportedAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ReportedAlarmStatus.setStatus("current")
_Cerent454ReportedAlarmServiceAffecting_Type = CerentAlarmServiceAffecting
_Cerent454ReportedAlarmServiceAffecting_Object = MibTableColumn
cerent454ReportedAlarmServiceAffecting = _Cerent454ReportedAlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 30, 40, 1, 120),
    _Cerent454ReportedAlarmServiceAffecting_Type()
)
cerent454ReportedAlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ReportedAlarmServiceAffecting.setStatus("current")
_Cerent454ThresholdGroup_ObjectIdentity = ObjectIdentity
cerent454ThresholdGroup = _Cerent454ThresholdGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 40)
)
if mibBuilder.loadTexts:
    cerent454ThresholdGroup.setStatus("current")
_Cerent454ThresholdTable_Object = MibTable
cerent454ThresholdTable = _Cerent454ThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 40, 10)
)
if mibBuilder.loadTexts:
    cerent454ThresholdTable.setStatus("current")
_Cerent454ThresholdEntry_Object = MibTableRow
cerent454ThresholdEntry = _Cerent454ThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 40, 10, 1)
)
cerent454ThresholdEntry.setIndexNames(
    (0, "CERENT-454-MIB", "cerent454ThresholdIndex"),
)
if mibBuilder.loadTexts:
    cerent454ThresholdEntry.setStatus("current")


class _Cerent454ThresholdIndex_Type(Integer32):
    """Custom type cerent454ThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Cerent454ThresholdIndex_Type.__name__ = "Integer32"
_Cerent454ThresholdIndex_Object = MibTableColumn
cerent454ThresholdIndex = _Cerent454ThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 40, 10, 1, 10),
    _Cerent454ThresholdIndex_Type()
)
cerent454ThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerent454ThresholdIndex.setStatus("current")
_Cerent454ThresholdMonitorType_Type = CerentMonitorType
_Cerent454ThresholdMonitorType_Object = MibTableColumn
cerent454ThresholdMonitorType = _Cerent454ThresholdMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 40, 10, 1, 20),
    _Cerent454ThresholdMonitorType_Type()
)
cerent454ThresholdMonitorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ThresholdMonitorType.setStatus("current")
_Cerent454ThresholdLocation_Type = CerentLocation
_Cerent454ThresholdLocation_Object = MibTableColumn
cerent454ThresholdLocation = _Cerent454ThresholdLocation_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 40, 10, 1, 30),
    _Cerent454ThresholdLocation_Type()
)
cerent454ThresholdLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ThresholdLocation.setStatus("current")
_Cerent454ThresholdPeriod_Type = CerentPeriod
_Cerent454ThresholdPeriod_Object = MibTableColumn
cerent454ThresholdPeriod = _Cerent454ThresholdPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 40, 10, 1, 40),
    _Cerent454ThresholdPeriod_Type()
)
cerent454ThresholdPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ThresholdPeriod.setStatus("current")
_Cerent454ThresholdSetValue_Type = Integer32
_Cerent454ThresholdSetValue_Object = MibTableColumn
cerent454ThresholdSetValue = _Cerent454ThresholdSetValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 40, 10, 1, 50),
    _Cerent454ThresholdSetValue_Type()
)
cerent454ThresholdSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ThresholdSetValue.setStatus("current")
_Cerent454ThresholdCurrentValue_Type = Integer32
_Cerent454ThresholdCurrentValue_Object = MibTableColumn
cerent454ThresholdCurrentValue = _Cerent454ThresholdCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 40, 10, 1, 60),
    _Cerent454ThresholdCurrentValue_Type()
)
cerent454ThresholdCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ThresholdCurrentValue.setStatus("current")


class _Cerent454ThresholdDetectType_Type(Integer32):
    """Custom type cerent454ThresholdDetectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("mon", 20),
          ("none", 10),
          ("term", 30),
          ("unknown", 1))
    )


_Cerent454ThresholdDetectType_Type.__name__ = "Integer32"
_Cerent454ThresholdDetectType_Object = MibTableColumn
cerent454ThresholdDetectType = _Cerent454ThresholdDetectType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 20, 40, 10, 1, 70),
    _Cerent454ThresholdDetectType_Type()
)
cerent454ThresholdDetectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454ThresholdDetectType.setStatus("current")
_Cerent454Events_ObjectIdentity = ObjectIdentity
cerent454Events = _Cerent454Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30)
)
if mibBuilder.loadTexts:
    cerent454Events.setStatus("current")
_Cerent454V2Events_ObjectIdentity = ObjectIdentity
cerent454V2Events = _Cerent454V2Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0)
)
if mibBuilder.loadTexts:
    cerent454V2Events.setStatus("current")
_CerentCommonObjects_ObjectIdentity = ObjectIdentity
cerentCommonObjects = _CerentCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 100)
)
if mibBuilder.loadTexts:
    cerentCommonObjects.setStatus("current")
_Cerent454CommonObjectsGroup_ObjectIdentity = ObjectIdentity
cerent454CommonObjectsGroup = _Cerent454CommonObjectsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 100, 10)
)
if mibBuilder.loadTexts:
    cerent454CommonObjectsGroup.setStatus("current")


class _Cerent454EnableNotification_Type(TruthValue):
    """Custom type cerent454EnableNotification based on TruthValue"""


_Cerent454EnableNotification_Object = MibScalar
cerent454EnableNotification = _Cerent454EnableNotification_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 100, 10, 10),
    _Cerent454EnableNotification_Type()
)
cerent454EnableNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerent454EnableNotification.setStatus("current")
_Cerent454NodeTime_Type = DisplayString
_Cerent454NodeTime_Object = MibScalar
cerent454NodeTime = _Cerent454NodeTime_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 100, 10, 20),
    _Cerent454NodeTime_Type()
)
cerent454NodeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454NodeTime.setStatus("current")
_Cerent454SentNotifications_Type = Counter32
_Cerent454SentNotifications_Object = MibScalar
cerent454SentNotifications = _Cerent454SentNotifications_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 100, 10, 30),
    _Cerent454SentNotifications_Type()
)
cerent454SentNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454SentNotifications.setStatus("current")
_Cerent454LastChangeTime_Type = TimeStamp
_Cerent454LastChangeTime_Object = MibScalar
cerent454LastChangeTime = _Cerent454LastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 100, 10, 40),
    _Cerent454LastChangeTime_Type()
)
cerent454LastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454LastChangeTime.setStatus("current")


class _Cerent454MultishelfEnabled_Type(TruthValue):
    """Custom type cerent454MultishelfEnabled based on TruthValue"""


_Cerent454MultishelfEnabled_Object = MibScalar
cerent454MultishelfEnabled = _Cerent454MultishelfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 100, 10, 50),
    _Cerent454MultishelfEnabled_Type()
)
cerent454MultishelfEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerent454MultishelfEnabled.setStatus("current")
_CerentCommonEvents_ObjectIdentity = ObjectIdentity
cerentCommonEvents = _CerentCommonEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 200)
)
if mibBuilder.loadTexts:
    cerentCommonEvents.setStatus("current")

# Managed Objects groups

node454Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 10, 10, 10)
)
node454Group.setObjects(
    ("CERENT-454-MIB", "cerent454SoftwareVersion")
)
if mibBuilder.loadTexts:
    node454Group.setStatus("current")

alarm454Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 10, 10, 20)
)
alarm454Group.setObjects(
      *(("CERENT-454-MIB", "cerent454AlarmCount"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmType"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"),
        ("CERENT-454-MIB", "cerent454AlarmTimeStamp"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmAdditionalInfo"))
)
if mibBuilder.loadTexts:
    alarm454Group.setStatus("current")

cerent454CommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 10, 10, 40)
)
cerent454CommonGroup.setObjects(
      *(("CERENT-454-MIB", "cerent454EnableNotification"),
        ("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454SentNotifications"),
        ("CERENT-454-MIB", "cerent454LastChangeTime"),
        ("CERENT-454-MIB", "cerent454MultishelfEnabled"))
)
if mibBuilder.loadTexts:
    cerent454CommonGroup.setStatus("current")

cerentThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 10, 10, 50)
)
cerentThresholdGroup.setObjects(
      *(("CERENT-454-MIB", "cerent454ThresholdMonitorType"),
        ("CERENT-454-MIB", "cerent454ThresholdLocation"),
        ("CERENT-454-MIB", "cerent454ThresholdPeriod"),
        ("CERENT-454-MIB", "cerent454ThresholdSetValue"),
        ("CERENT-454-MIB", "cerent454ThresholdCurrentValue"),
        ("CERENT-454-MIB", "cerent454ThresholdDetectType"))
)
if mibBuilder.loadTexts:
    cerentThresholdGroup.setStatus("current")

reportedAlarm454Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 10, 10, 80)
)
reportedAlarm454Group.setObjects(
      *(("CERENT-454-MIB", "cerent454ReportedAlarmCount"),
        ("CERENT-454-MIB", "cerent454ReportedAlarmObjectType"),
        ("CERENT-454-MIB", "cerent454ReportedAlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454ReportedAlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454ReportedAlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454ReportedAlarmType"),
        ("CERENT-454-MIB", "cerent454ReportedAlarmTimeStamp"),
        ("CERENT-454-MIB", "cerent454ReportedAlarmObjectName"),
        ("CERENT-454-MIB", "cerent454ReportedAlarmAdditionalInfo"),
        ("CERENT-454-MIB", "cerent454ReportedAlarmSeverity"),
        ("CERENT-454-MIB", "cerent454ReportedAlarmStatus"),
        ("CERENT-454-MIB", "cerent454ReportedAlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    reportedAlarm454Group.setStatus("current")


# Notification objects

alarmUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1)
)
alarmUnknown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    alarmUnknown.setStatus(
        "current"
    )

alarmCutoffIsInManualMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 10)
)
alarmCutoffIsInManualMode.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    alarmCutoffIsInManualMode.setStatus(
        "current"
    )

failureDetectedExternalToTheNE = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 20)
)
failureDetectedExternalToTheNE.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmAdditionalInfo"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    failureDetectedExternalToTheNE.setStatus(
        "current"
    )

externalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 30)
)
externalError.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    externalError.setStatus(
        "current"
    )

excessiveSwitching = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 40)
)
excessiveSwitching.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    excessiveSwitching.setStatus(
        "current"
    )

sdccTerminationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 50)
)
sdccTerminationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    sdccTerminationFailure.setStatus(
        "current"
    )

incomingFailureCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 60)
)
incomingFailureCondition.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    incomingFailureCondition.setStatus(
        "current"
    )

alarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 70)
)
alarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    alarmIndicationSignal.setStatus(
        "current"
    )

alarmIndicationSignalLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 80)
)
alarmIndicationSignalLine.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    alarmIndicationSignalLine.setStatus(
        "current"
    )

alarmIndicationSignalPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 90)
)
alarmIndicationSignalPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    alarmIndicationSignalPath.setStatus(
        "current"
    )

alarmIndicationSignalVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 100)
)
alarmIndicationSignalVT.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    alarmIndicationSignalVT.setStatus(
        "current"
    )

apsChannelFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 110)
)
apsChannelFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    apsChannelFailure.setStatus(
        "current"
    )

channelByteFailureAPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 120)
)
channelByteFailureAPS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    channelByteFailureAPS.setStatus(
        "current"
    )

channelProtectionSwitchingChannelMatchFailureAPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 130)
)
channelProtectionSwitchingChannelMatchFailureAPS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    channelProtectionSwitchingChannelMatchFailureAPS.setStatus(
        "current"
    )

channelAutomaticProtectionSwitchModeMismatchAPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 140)
)
channelAutomaticProtectionSwitchModeMismatchAPS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    channelAutomaticProtectionSwitchModeMismatchAPS.setStatus(
        "current"
    )

farEndProtectionLineFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 150)
)
farEndProtectionLineFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndProtectionLineFailure.setStatus(
        "current"
    )

inconsistentAPSCode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 160)
)
inconsistentAPSCode.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    inconsistentAPSCode.setStatus(
        "current"
    )

improperAPSCode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 170)
)
improperAPSCode.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    improperAPSCode.setStatus(
        "current"
    )

nodeIdMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 180)
)
nodeIdMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    nodeIdMismatch.setStatus(
        "current"
    )

channelDefaultKAPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 190)
)
channelDefaultKAPS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    channelDefaultKAPS.setStatus(
        "current"
    )

connectionLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 200)
)
connectionLoss.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    connectionLoss.setStatus(
        "current"
    )

bipolarViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 210)
)
bipolarViolation.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    bipolarViolation.setStatus(
        "current"
    )

carrierLossOnTheLAN = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 220)
)
carrierLossOnTheLAN.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    carrierLossOnTheLAN.setStatus(
        "current"
    )

concatenationErrorSTS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 230)
)
concatenationErrorSTS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    concatenationErrorSTS.setStatus(
        "current"
    )

excessCollisionsOnTheLAN = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 240)
)
excessCollisionsOnTheLAN.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    excessCollisionsOnTheLAN.setStatus(
        "current"
    )

facilityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 250)
)
facilityFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    facilityFailure.setStatus(
        "current"
    )

farEndAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 260)
)
farEndAIS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndAIS.setStatus(
        "current"
    )

farEndMultipleDS1LOSDetectedOnDS3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 270)
)
farEndMultipleDS1LOSDetectedOnDS3.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndMultipleDS1LOSDetectedOnDS3.setStatus(
        "current"
    )

farEndDS1EqptFailNonServiceAffecting = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 280)
)
farEndDS1EqptFailNonServiceAffecting.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndDS1EqptFailNonServiceAffecting.setStatus(
        "current"
    )

farEndDS1EqptFailServiceAffecting = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 290)
)
farEndDS1EqptFailServiceAffecting.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndDS1EqptFailServiceAffecting.setStatus(
        "current"
    )

farEndSingleDS1LOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 300)
)
farEndSingleDS1LOS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndSingleDS1LOS.setStatus(
        "current"
    )

farEndDS3EqptFailNonServiceAffecting = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 310)
)
farEndDS3EqptFailNonServiceAffecting.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndDS3EqptFailNonServiceAffecting.setStatus(
        "current"
    )

farEndDS3EqptFailServiceAffecting = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 320)
)
farEndDS3EqptFailServiceAffecting.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndDS3EqptFailServiceAffecting.setStatus(
        "current"
    )

farEndCommonEquipmentFailureNonServiceAffecting = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 330)
)
farEndCommonEquipmentFailureNonServiceAffecting.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndCommonEquipmentFailureNonServiceAffecting.setStatus(
        "current"
    )

farEndIDLE = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 340)
)
farEndIDLE.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndIDLE.setStatus(
        "current"
    )

farEndLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 350)
)
farEndLOS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndLOS.setStatus(
        "current"
    )

farEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 360)
)
farEndLOF.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndLOF.setStatus(
        "current"
    )

farEndBlockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 370)
)
farEndBlockError.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndBlockError.setStatus(
        "current"
    )

ds3IdleCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 380)
)
ds3IdleCondition.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ds3IdleCondition.setStatus(
        "current"
    )

lossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 390)
)
lossOfFrame.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lossOfFrame.setStatus(
        "current"
    )

lossOfPointer = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 400)
)
lossOfPointer.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lossOfPointer.setStatus(
        "current"
    )

lossOfPointerPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 410)
)
lossOfPointerPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lossOfPointerPath.setStatus(
        "current"
    )

lossOfPointerVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 420)
)
lossOfPointerVT.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lossOfPointerVT.setStatus(
        "current"
    )

lossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 430)
)
lossOfSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lossOfSignal.setStatus(
        "current"
    )

outOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 440)
)
outOfFrame.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    outOfFrame.setStatus(
        "current"
    )

pathSelectorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 450)
)
pathSelectorFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    pathSelectorFailure.setStatus(
        "current"
    )

remoteAlarmIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 460)
)
remoteAlarmIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    remoteAlarmIndication.setStatus(
        "current"
    )

remoteFailureIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 470)
)
remoteFailureIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    remoteFailureIndication.setStatus(
        "current"
    )

remoteFailureIndicationLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 480)
)
remoteFailureIndicationLine.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    remoteFailureIndicationLine.setStatus(
        "current"
    )

remoteFailureIndicationPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 490)
)
remoteFailureIndicationPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    remoteFailureIndicationPath.setStatus(
        "current"
    )

remoteFailureIndicationVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 500)
)
remoteFailureIndicationVT.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    remoteFailureIndicationVT.setStatus(
        "current"
    )

signalDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 510)
)
signalDegrade.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    signalDegrade.setStatus(
        "current"
    )

severelyErroredFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 520)
)
severelyErroredFrame.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    severelyErroredFrame.setStatus(
        "current"
    )

signalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 530)
)
signalFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    signalFailure.setStatus(
        "current"
    )

signalLabelMismatchFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 540)
)
signalLabelMismatchFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    signalLabelMismatchFailure.setStatus(
        "current"
    )

payloadDefectIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 550)
)
payloadDefectIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadDefectIndication.setStatus(
        "current"
    )

payloadDefectIndicationPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 560)
)
payloadDefectIndicationPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadDefectIndicationPath.setStatus(
        "current"
    )

payloadLabelMismatchPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 570)
)
payloadLabelMismatchPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadLabelMismatchPath.setStatus(
        "current"
    )

signalLabelMismatchFailurePayloadLabelMismatchVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 580)
)
signalLabelMismatchFailurePayloadLabelMismatchVT.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    signalLabelMismatchFailurePayloadLabelMismatchVT.setStatus(
        "current"
    )

unequippedPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 590)
)
unequippedPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    unequippedPath.setStatus(
        "current"
    )

signalLabelMismatchFailureUnequippedVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 600)
)
signalLabelMismatchFailureUnequippedVT.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    signalLabelMismatchFailureUnequippedVT.setStatus(
        "current"
    )

lossOfSynchronization = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 610)
)
lossOfSynchronization.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lossOfSynchronization.setStatus(
        "current"
    )

outOfSynchronization = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 620)
)
outOfSynchronization.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    outOfSynchronization.setStatus(
        "current"
    )

primarySynchronizationReferenceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 630)
)
primarySynchronizationReferenceFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    primarySynchronizationReferenceFailure.setStatus(
        "current"
    )

secondarySynchronizationReferenceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 640)
)
secondarySynchronizationReferenceFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    secondarySynchronizationReferenceFailure.setStatus(
        "current"
    )

thirdSynchronizationReferenceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 650)
)
thirdSynchronizationReferenceFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    thirdSynchronizationReferenceFailure.setStatus(
        "current"
    )

fourthSynchronizationReferenceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 660)
)
fourthSynchronizationReferenceFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    fourthSynchronizationReferenceFailure.setStatus(
        "current"
    )

fifthSynchronizationReferenceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 670)
)
fifthSynchronizationReferenceFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    fifthSynchronizationReferenceFailure.setStatus(
        "current"
    )

sixthSynchronizationReferenceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 680)
)
sixthSynchronizationReferenceFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    sixthSynchronizationReferenceFailure.setStatus(
        "current"
    )

failedToReceiveSynchronizationStatusMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 690)
)
failedToReceiveSynchronizationStatusMessage.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    failedToReceiveSynchronizationStatusMessage.setStatus(
        "current"
    )

synchronizationStatusMessagesAreDisabledOnThisInterface = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 700)
)
synchronizationStatusMessagesAreDisabledOnThisInterface.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    synchronizationStatusMessagesAreDisabledOnThisInterface.setStatus(
        "current"
    )

stratum1PrimaryReferenceSourceTraceable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 710)
)
stratum1PrimaryReferenceSourceTraceable.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    stratum1PrimaryReferenceSourceTraceable.setStatus(
        "current"
    )

synchronizedTraceabilityUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 720)
)
synchronizedTraceabilityUnknown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    synchronizedTraceabilityUnknown.setStatus(
        "current"
    )

stratum2Traceable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 730)
)
stratum2Traceable.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    stratum2Traceable.setStatus(
        "current"
    )

transitNodeClockTraceable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 740)
)
transitNodeClockTraceable.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    transitNodeClockTraceable.setStatus(
        "current"
    )

stratum3ETraceable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 750)
)
stratum3ETraceable.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    stratum3ETraceable.setStatus(
        "current"
    )

stratum3Traceable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 760)
)
stratum3Traceable.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    stratum3Traceable.setStatus(
        "current"
    )

sonetMinimumClockTraceable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 770)
)
sonetMinimumClockTraceable.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    sonetMinimumClockTraceable.setStatus(
        "current"
    )

stratum4Traceable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 780)
)
stratum4Traceable.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    stratum4Traceable.setStatus(
        "current"
    )

doNotUseForSynchronization = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 790)
)
doNotUseForSynchronization.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    doNotUseForSynchronization.setStatus(
        "current"
    )

reservedForNetworkSynchronizationUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 800)
)
reservedForNetworkSynchronizationUse.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    reservedForNetworkSynchronizationUse.setStatus(
        "current"
    )

outgoingFailureCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 810)
)
outgoingFailureCondition.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    outgoingFailureCondition.setStatus(
        "current"
    )

remoteDefectIndicationLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 820)
)
remoteDefectIndicationLine.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    remoteDefectIndicationLine.setStatus(
        "current"
    )

remoteDefectIndicationPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 830)
)
remoteDefectIndicationPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    remoteDefectIndicationPath.setStatus(
        "current"
    )

freeRunningSynchronizationMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 840)
)
freeRunningSynchronizationMode.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    freeRunningSynchronizationMode.setStatus(
        "current"
    )

holdoverSynchronizationMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 850)
)
holdoverSynchronizationMode.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    holdoverSynchronizationMode.setStatus(
        "current"
    )

fastStartSynchronizationMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 860)
)
fastStartSynchronizationMode.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    fastStartSynchronizationMode.setStatus(
        "current"
    )

internalFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 870)
)
internalFault.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    internalFault.setStatus(
        "current"
    )

internalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 880)
)
internalError.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    internalError.setStatus(
        "current"
    )

internalMessageError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 890)
)
internalMessageError.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    internalMessageError.setStatus(
        "current"
    )

mismatchOfEquipmentAndAttributes = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 900)
)
mismatchOfEquipmentAndAttributes.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    mismatchOfEquipmentAndAttributes.setStatus(
        "current"
    )

watchdogTimerTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 910)
)
watchdogTimerTimeout.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    watchdogTimerTimeout.setStatus(
        "current"
    )

softwareFaultOrFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 920)
)
softwareFaultOrFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    softwareFaultOrFailure.setStatus(
        "current"
    )

softwareFaultDataIntegrityFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 930)
)
softwareFaultDataIntegrityFault.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    softwareFaultDataIntegrityFault.setStatus(
        "current"
    )

programFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 940)
)
programFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    programFailure.setStatus(
        "current"
    )

controlEquipmentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 950)
)
controlEquipmentFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    controlEquipmentFailure.setStatus(
        "current"
    )

primaryNonVolatileBackupMemoryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 960)
)
primaryNonVolatileBackupMemoryFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    primaryNonVolatileBackupMemoryFailure.setStatus(
        "current"
    )

secondaryNonVolatileBackupMemoryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 970)
)
secondaryNonVolatileBackupMemoryFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    secondaryNonVolatileBackupMemoryFailure.setStatus(
        "current"
    )

controlBusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 980)
)
controlBusFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    controlBusFailure.setStatus(
        "current"
    )

controlBus1Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 990)
)
controlBus1Failure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    controlBus1Failure.setStatus(
        "current"
    )

controlBus2Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1000)
)
controlBus2Failure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    controlBus2Failure.setStatus(
        "current"
    )

tccAToShelfSlot1DROP1CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1010)
)
tccAToShelfSlot1DROP1CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot1DROP1CommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot2DROP2CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1020)
)
tccAToShelfSlot2DROP2CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot2DROP2CommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot3DROP3CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1030)
)
tccAToShelfSlot3DROP3CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot3DROP3CommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot4DROP4CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1040)
)
tccAToShelfSlot4DROP4CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot4DROP4CommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot5TRUNK1CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1050)
)
tccAToShelfSlot5TRUNK1CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot5TRUNK1CommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot6TRUNK2CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1060)
)
tccAToShelfSlot6TRUNK2CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot6TRUNK2CommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot7TCCACommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1070)
)
tccAToShelfSlot7TCCACommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot7TCCACommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot8XCONACommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1080)
)
tccAToShelfSlot8XCONACommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot8XCONACommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot9AICCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1090)
)
tccAToShelfSlot9AICCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot9AICCommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot10XCONBCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1100)
)
tccAToShelfSlot10XCONBCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot10XCONBCommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot11TCCBCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1110)
)
tccAToShelfSlot11TCCBCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot11TCCBCommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot12TRUNK3CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1120)
)
tccAToShelfSlot12TRUNK3CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot12TRUNK3CommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot13TRUNK4CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1130)
)
tccAToShelfSlot13TRUNK4CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot13TRUNK4CommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot14DROP5CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1140)
)
tccAToShelfSlot14DROP5CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot14DROP5CommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot15DROP6CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1150)
)
tccAToShelfSlot15DROP6CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot15DROP6CommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot16DROP7CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1160)
)
tccAToShelfSlot16DROP7CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot16DROP7CommunicationFailure.setStatus(
        "current"
    )

tccAToShelfSlot17DROP8CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1170)
)
tccAToShelfSlot17DROP8CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToShelfSlot17DROP8CommunicationFailure.setStatus(
        "current"
    )

tccAToDCCAProcessorCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1180)
)
tccAToDCCAProcessorCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccAToDCCAProcessorCommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot1DROP1CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1190)
)
tccBToShelfSlot1DROP1CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot1DROP1CommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot2DROP2CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1200)
)
tccBToShelfSlot2DROP2CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot2DROP2CommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot3DROP3CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1210)
)
tccBToShelfSlot3DROP3CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot3DROP3CommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot4DROP4CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1220)
)
tccBToShelfSlot4DROP4CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot4DROP4CommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot5TRUNK1CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1230)
)
tccBToShelfSlot5TRUNK1CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot5TRUNK1CommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot6TRUNK2CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1240)
)
tccBToShelfSlot6TRUNK2CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot6TRUNK2CommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot7TCCACommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1250)
)
tccBToShelfSlot7TCCACommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot7TCCACommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot8XCONACommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1260)
)
tccBToShelfSlot8XCONACommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot8XCONACommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot9AICCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1270)
)
tccBToShelfSlot9AICCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot9AICCommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot10XCONBCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1280)
)
tccBToShelfSlot10XCONBCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot10XCONBCommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot11TCCBCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1290)
)
tccBToShelfSlot11TCCBCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot11TCCBCommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot12TRUNK3CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1300)
)
tccBToShelfSlot12TRUNK3CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot12TRUNK3CommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot13TRUNK4CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1310)
)
tccBToShelfSlot13TRUNK4CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot13TRUNK4CommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot14DROP5CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1320)
)
tccBToShelfSlot14DROP5CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot14DROP5CommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot15DROP6CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1330)
)
tccBToShelfSlot15DROP6CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot15DROP6CommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot16DROP7CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1340)
)
tccBToShelfSlot16DROP7CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot16DROP7CommunicationFailure.setStatus(
        "current"
    )

tccBToShelfSlot17DROP8CommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1350)
)
tccBToShelfSlot17DROP8CommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToShelfSlot17DROP8CommunicationFailure.setStatus(
        "current"
    )

tccBToDCCBProcessorCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1360)
)
tccBToDCCBProcessorCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tccBToDCCBProcessorCommunicationFailure.setStatus(
        "current"
    )

controlEquipmentControlCommunicationsEquipmentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1370)
)
controlEquipmentControlCommunicationsEquipmentFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    controlEquipmentControlCommunicationsEquipmentFailure.setStatus(
        "current"
    )

controlProcessorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1380)
)
controlProcessorFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    controlProcessorFailure.setStatus(
        "current"
    )

workingMemoryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1390)
)
workingMemoryFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingMemoryFailure.setStatus(
        "current"
    )

interconnectionEquipmentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1400)
)
interconnectionEquipmentFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    interconnectionEquipmentFailure.setStatus(
        "current"
    )

payloadBusFailureToIOSlot1XCONSlot8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1410)
)
payloadBusFailureToIOSlot1XCONSlot8.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot1XCONSlot8.setStatus(
        "current"
    )

payloadBusFailureToIOSlot2XCONSlot8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1420)
)
payloadBusFailureToIOSlot2XCONSlot8.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot2XCONSlot8.setStatus(
        "current"
    )

payloadBusFailureToIOSlot3XCONSlot8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1430)
)
payloadBusFailureToIOSlot3XCONSlot8.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot3XCONSlot8.setStatus(
        "current"
    )

payloadBusFailureToIOSlot4XCONSlot8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1440)
)
payloadBusFailureToIOSlot4XCONSlot8.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot4XCONSlot8.setStatus(
        "current"
    )

payloadBusFailureToIOSlot5XCONSlot8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1450)
)
payloadBusFailureToIOSlot5XCONSlot8.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot5XCONSlot8.setStatus(
        "current"
    )

payloadBusFailureToIOSlot6XCONSlot8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1460)
)
payloadBusFailureToIOSlot6XCONSlot8.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot6XCONSlot8.setStatus(
        "current"
    )

payloadBusFailureToIOSlot12XCONSlot8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1470)
)
payloadBusFailureToIOSlot12XCONSlot8.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot12XCONSlot8.setStatus(
        "current"
    )

payloadBusFailureToIOSlot13XCONSlot8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1480)
)
payloadBusFailureToIOSlot13XCONSlot8.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot13XCONSlot8.setStatus(
        "current"
    )

payloadBusFailureToIOSlot14XCONSlot8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1490)
)
payloadBusFailureToIOSlot14XCONSlot8.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot14XCONSlot8.setStatus(
        "current"
    )

payloadBusFailureToIOSlot15XCONSlot8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1500)
)
payloadBusFailureToIOSlot15XCONSlot8.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot15XCONSlot8.setStatus(
        "current"
    )

payloadBusFailureToIOSlot16XCONSlot8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1510)
)
payloadBusFailureToIOSlot16XCONSlot8.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot16XCONSlot8.setStatus(
        "current"
    )

payloadBusFailureToIOSlot17XCONSlot8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1520)
)
payloadBusFailureToIOSlot17XCONSlot8.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot17XCONSlot8.setStatus(
        "current"
    )

payloadBusFailureToIOSlot1XCONSlot10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1530)
)
payloadBusFailureToIOSlot1XCONSlot10.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot1XCONSlot10.setStatus(
        "current"
    )

payloadBusFailureToIOSlot2XCONSlot10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1540)
)
payloadBusFailureToIOSlot2XCONSlot10.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot2XCONSlot10.setStatus(
        "current"
    )

payloadBusFailureToIOSlot3XCONSlot10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1550)
)
payloadBusFailureToIOSlot3XCONSlot10.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot3XCONSlot10.setStatus(
        "current"
    )

payloadBusFailureToIOSlot4XCONSlot10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1560)
)
payloadBusFailureToIOSlot4XCONSlot10.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot4XCONSlot10.setStatus(
        "current"
    )

payloadBusFailureToIOSlot5XCONSlot10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1570)
)
payloadBusFailureToIOSlot5XCONSlot10.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot5XCONSlot10.setStatus(
        "current"
    )

payloadBusFailureToIOSlot6XCONSlot10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1580)
)
payloadBusFailureToIOSlot6XCONSlot10.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot6XCONSlot10.setStatus(
        "current"
    )

payloadBusFailureToIOSlot12XCONSlot10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1590)
)
payloadBusFailureToIOSlot12XCONSlot10.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot12XCONSlot10.setStatus(
        "current"
    )

payloadBusFailureToIOSlot13XCONSlot10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1600)
)
payloadBusFailureToIOSlot13XCONSlot10.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot13XCONSlot10.setStatus(
        "current"
    )

payloadBusFailureToIOSlot14XCONSlot10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1610)
)
payloadBusFailureToIOSlot14XCONSlot10.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot14XCONSlot10.setStatus(
        "current"
    )

payloadBusFailureToIOSlot15XCONSlot10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1620)
)
payloadBusFailureToIOSlot15XCONSlot10.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot15XCONSlot10.setStatus(
        "current"
    )

payloadBusFailureToIOSlot16XCONSlot10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1630)
)
payloadBusFailureToIOSlot16XCONSlot10.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot16XCONSlot10.setStatus(
        "current"
    )

payloadBusFailureToIOSlot17XCONSlot10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1640)
)
payloadBusFailureToIOSlot17XCONSlot10.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadBusFailureToIOSlot17XCONSlot10.setStatus(
        "current"
    )

timeSlotInterchangeEquipmentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1650)
)
timeSlotInterchangeEquipmentFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    timeSlotInterchangeEquipmentFailure.setStatus(
        "current"
    )

equipmentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1660)
)
equipmentFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentFailure.setStatus(
        "current"
    )

highTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1670)
)
highTemperature.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    highTemperature.setStatus(
        "current"
    )

invalidMACAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1680)
)
invalidMACAddress.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    invalidMACAddress.setStatus(
        "current"
    )

boardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1690)
)
boardFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    boardFailure.setStatus(
        "current"
    )

diagnosticFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1700)
)
diagnosticFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    diagnosticFailure.setStatus(
        "current"
    )

mediumAccessControlFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1710)
)
mediumAccessControlFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    mediumAccessControlFailure.setStatus(
        "current"
    )

facilityTerminationEquipmentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1720)
)
facilityTerminationEquipmentFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    facilityTerminationEquipmentFailure.setStatus(
        "current"
    )

automaticLaserShutoffDueToHighTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1730)
)
automaticLaserShutoffDueToHighTemperature.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticLaserShutoffDueToHighTemperature.setStatus(
        "current"
    )

failureToReleaseFromProtection = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1740)
)
failureToReleaseFromProtection.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    failureToReleaseFromProtection.setStatus(
        "current"
    )

receiverFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1750)
)
receiverFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    receiverFailure.setStatus(
        "current"
    )

transmitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1760)
)
transmitFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    transmitFailure.setStatus(
        "current"
    )

facilityTerminationEquipmentReceiverMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1770)
)
facilityTerminationEquipmentReceiverMissing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    facilityTerminationEquipmentReceiverMissing.setStatus(
        "current"
    )

facilityTerminationEquipmentTransmitterMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1780)
)
facilityTerminationEquipmentTransmitterMissing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    facilityTerminationEquipmentTransmitterMissing.setStatus(
        "current"
    )

failureToSwitchToProtection = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1790)
)
failureToSwitchToProtection.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    failureToSwitchToProtection.setStatus(
        "current"
    )

failureToSwitchToProtectionRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1800)
)
failureToSwitchToProtectionRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    failureToSwitchToProtectionRing.setStatus(
        "current"
    )

failureToSwitchToProtectionSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1810)
)
failureToSwitchToProtectionSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    failureToSwitchToProtectionSpan.setStatus(
        "current"
    )

failureToSwitchToProtectionPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1820)
)
failureToSwitchToProtectionPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    failureToSwitchToProtectionPath.setStatus(
        "current"
    )

fanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1830)
)
fanFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    fanFailure.setStatus(
        "current"
    )

equipmentUnitPlugIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1840)
)
equipmentUnitPlugIn.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentUnitPlugIn.setStatus(
        "current"
    )

nePowerFailureAtConnector = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1850)
)
nePowerFailureAtConnector.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    nePowerFailureAtConnector.setStatus(
        "current"
    )

fuseAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1860)
)
fuseAlarm.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    fuseAlarm.setStatus(
        "current"
    )

synchronizationUnitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1870)
)
synchronizationUnitFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    synchronizationUnitFailure.setStatus(
        "current"
    )

synchronizationSwitchingEquipmentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1880)
)
synchronizationSwitchingEquipmentFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    synchronizationSwitchingEquipmentFailure.setStatus(
        "current"
    )

equipmentUnitUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1890)
)
equipmentUnitUnplugged.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentUnitUnplugged.setStatus(
        "current"
    )

loopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1900)
)
loopback.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    loopback.setStatus(
        "current"
    )

ds1LoopbackDueToFEACCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1910)
)
ds1LoopbackDueToFEACCommand.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ds1LoopbackDueToFEACCommand.setStatus(
        "current"
    )

loopbackCommandSentToFarEndDS1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1920)
)
loopbackCommandSentToFarEndDS1.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    loopbackCommandSentToFarEndDS1.setStatus(
        "current"
    )

ds3LoopbackDueToFEACCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1930)
)
ds3LoopbackDueToFEACCommand.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ds3LoopbackDueToFEACCommand.setStatus(
        "current"
    )

ds3LoopbackCommandSentToFarEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1940)
)
ds3LoopbackCommandSentToFarEnd.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ds3LoopbackCommandSentToFarEnd.setStatus(
        "current"
    )

ds2LoopbackDueToFarEndCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1950)
)
ds2LoopbackDueToFarEndCommand.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ds2LoopbackDueToFarEndCommand.setStatus(
        "current"
    )

ds2LoopbackCommandSentToFarEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1960)
)
ds2LoopbackCommandSentToFarEnd.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ds2LoopbackCommandSentToFarEnd.setStatus(
        "current"
    )

facilityLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1970)
)
facilityLoopback.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    facilityLoopback.setStatus(
        "current"
    )

networkLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1980)
)
networkLoopback.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    networkLoopback.setStatus(
        "current"
    )

terminalLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 1990)
)
terminalLoopback.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    terminalLoopback.setStatus(
        "current"
    )

manuallyCausedAbnormalCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2000)
)
manuallyCausedAbnormalCondition.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manuallyCausedAbnormalCondition.setStatus(
        "current"
    )

ethernetBridgeIsNewRootOfSpanningTree = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2010)
)
ethernetBridgeIsNewRootOfSpanningTree.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ethernetBridgeIsNewRootOfSpanningTree.setStatus(
        "current"
    )

ethernetBridgeTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2020)
)
ethernetBridgeTopologyChange.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ethernetBridgeTopologyChange.setStatus(
        "current"
    )

normalCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2030)
)
normalCondition.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    normalCondition.setStatus(
        "current"
    )

embeddedOperationsChannelFailureLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2040)
)
embeddedOperationsChannelFailureLinkDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    embeddedOperationsChannelFailureLinkDown.setStatus(
        "current"
    )

peerStateMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2050)
)
peerStateMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    peerStateMismatch.setStatus(
        "current"
    )

proceduralError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2060)
)
proceduralError.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    proceduralError.setStatus(
        "current"
    )

improperRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2070)
)
improperRemoval.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    improperRemoval.setStatus(
        "current"
    )

duplicateNodeID = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2080)
)
duplicateNodeID.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    duplicateNodeID.setStatus(
        "current"
    )

blsrOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2090)
)
blsrOutOfSync.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    blsrOutOfSync.setStatus(
        "current"
    )

blsrMultiNodeTableUpdateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2100)
)
blsrMultiNodeTableUpdateCompleted.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    blsrMultiNodeTableUpdateCompleted.setStatus(
        "current"
    )

protectionUnitNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2110)
)
protectionUnitNotAvailable.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectionUnitNotAvailable.setStatus(
        "current"
    )

performanceMonitorThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2120)
)
performanceMonitorThresholdCrossingAlert.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454ThresholdMonitorType"),
        ("CERENT-454-MIB", "cerent454ThresholdLocation"),
        ("CERENT-454-MIB", "cerent454ThresholdPeriod"),
        ("CERENT-454-MIB", "cerent454ThresholdSetValue"),
        ("CERENT-454-MIB", "cerent454ThresholdCurrentValue"),
        ("CERENT-454-MIB", "cerent454ThresholdDetectType"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    performanceMonitorThresholdCrossingAlert.setStatus(
        "current"
    )

protectionSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2130)
)
protectionSwitch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectionSwitch.setStatus(
        "current"
    )

recoveryOrServiceProtectionActionHasBeenInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2140)
)
recoveryOrServiceProtectionActionHasBeenInitiated.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    recoveryOrServiceProtectionActionHasBeenInitiated.setStatus(
        "current"
    )

automaticSystemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2150)
)
automaticSystemReset.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticSystemReset.setStatus(
        "current"
    )

automaticUPSRSwitchCausedByAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2160)
)
automaticUPSRSwitchCausedByAIS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticUPSRSwitchCausedByAIS.setStatus(
        "current"
    )

automaticUPSRSwitchCausedByLOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2170)
)
automaticUPSRSwitchCausedByLOP.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticUPSRSwitchCausedByLOP.setStatus(
        "current"
    )

automaticUPSRSwitchCausedByUNEQ = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2180)
)
automaticUPSRSwitchCausedByUNEQ.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticUPSRSwitchCausedByUNEQ.setStatus(
        "current"
    )

automaticUPSRSwitchCausedByPDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2190)
)
automaticUPSRSwitchCausedByPDI.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticUPSRSwitchCausedByPDI.setStatus(
        "current"
    )

automaticUPSRSwitchCausedBySFBER = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2200)
)
automaticUPSRSwitchCausedBySFBER.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticUPSRSwitchCausedBySFBER.setStatus(
        "current"
    )

automaticUPSRSwitchCausedBySDBER = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2210)
)
automaticUPSRSwitchCausedBySDBER.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticUPSRSwitchCausedBySDBER.setStatus(
        "current"
    )

coldRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2220)
)
coldRestart.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    coldRestart.setStatus(
        "current"
    )

forcedSwitchBackToWorking = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2230)
)
forcedSwitchBackToWorking.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchBackToWorking.setStatus(
        "current"
    )

forcedSwitchBackToWorkingRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2240)
)
forcedSwitchBackToWorkingRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchBackToWorkingRing.setStatus(
        "current"
    )

forcedSwitchBackToWorkingSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2250)
)
forcedSwitchBackToWorkingSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchBackToWorkingSpan.setStatus(
        "current"
    )

forcedSwitchToProtection = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2260)
)
forcedSwitchToProtection.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchToProtection.setStatus(
        "current"
    )

forcedSwitchToProtectionRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2270)
)
forcedSwitchToProtectionRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchToProtectionRing.setStatus(
        "current"
    )

forcedSwitchToProtectionSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2280)
)
forcedSwitchToProtectionSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchToProtectionSpan.setStatus(
        "current"
    )

workingFacilityOrEquipmentForcedToSwitchToProtectionPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2290)
)
workingFacilityOrEquipmentForcedToSwitchToProtectionPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingFacilityOrEquipmentForcedToSwitchToProtectionPath.setStatus(
        "current"
    )

initializationInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2300)
)
initializationInitiated.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    initializationInitiated.setStatus(
        "current"
    )

lockoutOfProtection = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2310)
)
lockoutOfProtection.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lockoutOfProtection.setStatus(
        "current"
    )

lockoutOfProtectionRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2320)
)
lockoutOfProtectionRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lockoutOfProtectionRing.setStatus(
        "current"
    )

lockoutOfProtectionSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2330)
)
lockoutOfProtectionSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lockoutOfProtectionSpan.setStatus(
        "current"
    )

lockoutOfProtectionPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2340)
)
lockoutOfProtectionPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lockoutOfProtectionPath.setStatus(
        "current"
    )

lockoutOfWorking = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2350)
)
lockoutOfWorking.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lockoutOfWorking.setStatus(
        "current"
    )

lockoutOfWorkingRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2360)
)
lockoutOfWorkingRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lockoutOfWorkingRing.setStatus(
        "current"
    )

lockoutOfWorkingSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2370)
)
lockoutOfWorkingSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lockoutOfWorkingSpan.setStatus(
        "current"
    )

manualSystemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2380)
)
manualSystemReset.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSystemReset.setStatus(
        "current"
    )

manualSwitchToInternalClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2390)
)
manualSwitchToInternalClock.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchToInternalClock.setStatus(
        "current"
    )

manualSwitchToPrimaryReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2400)
)
manualSwitchToPrimaryReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchToPrimaryReference.setStatus(
        "current"
    )

manualSwitchToSecondReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2410)
)
manualSwitchToSecondReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchToSecondReference.setStatus(
        "current"
    )

manualSwitchToThirdReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2420)
)
manualSwitchToThirdReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchToThirdReference.setStatus(
        "current"
    )

manualSwitchToFourthReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2430)
)
manualSwitchToFourthReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchToFourthReference.setStatus(
        "current"
    )

manualSwitchToFifthReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2440)
)
manualSwitchToFifthReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchToFifthReference.setStatus(
        "current"
    )

manualSwitchToSixthReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2450)
)
manualSwitchToSixthReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchToSixthReference.setStatus(
        "current"
    )

manualSwitchBackToWorking = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2460)
)
manualSwitchBackToWorking.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchBackToWorking.setStatus(
        "current"
    )

manualSwitchBackToWorkingRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2470)
)
manualSwitchBackToWorkingRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchBackToWorkingRing.setStatus(
        "current"
    )

manualSwitchBackToWorkingSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2480)
)
manualSwitchBackToWorkingSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchBackToWorkingSpan.setStatus(
        "current"
    )

manualSwitchToProtection = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2490)
)
manualSwitchToProtection.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchToProtection.setStatus(
        "current"
    )

manualSwitchToProtectionRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2500)
)
manualSwitchToProtectionRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchToProtectionRing.setStatus(
        "current"
    )

manualSwitchToProtectionSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2510)
)
manualSwitchToProtectionSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchToProtectionSpan.setStatus(
        "current"
    )

manualSwitchOfWorkingFacilityOrEquipmentToProtectionPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2520)
)
manualSwitchOfWorkingFacilityOrEquipmentToProtectionPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchOfWorkingFacilityOrEquipmentToProtectionPath.setStatus(
        "current"
    )

powerfailRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2530)
)
powerfailRestart.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    powerfailRestart.setStatus(
        "current"
    )

ringIsSquelchingTraffic = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2540)
)
ringIsSquelchingTraffic.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ringIsSquelchingTraffic.setStatus(
        "current"
    )

softwareDownloadInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2550)
)
softwareDownloadInProgress.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    softwareDownloadInProgress.setStatus(
        "current"
    )

switchToInternalClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2560)
)
switchToInternalClock.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    switchToInternalClock.setStatus(
        "current"
    )

switchToPrimaryReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2570)
)
switchToPrimaryReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    switchToPrimaryReference.setStatus(
        "current"
    )

switchToSecondReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2580)
)
switchToSecondReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    switchToSecondReference.setStatus(
        "current"
    )

switchToThirdReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2590)
)
switchToThirdReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    switchToThirdReference.setStatus(
        "current"
    )

switchToFourthReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2600)
)
switchToFourthReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    switchToFourthReference.setStatus(
        "current"
    )

switchToFifthReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2610)
)
switchToFifthReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    switchToFifthReference.setStatus(
        "current"
    )

switchToSixthReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2620)
)
switchToSixthReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    switchToSixthReference.setStatus(
        "current"
    )

systemReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2630)
)
systemReboot.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    systemReboot.setStatus(
        "current"
    )

switchedBackToWorking = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2640)
)
switchedBackToWorking.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    switchedBackToWorking.setStatus(
        "current"
    )

switchedToProtection = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2650)
)
switchedToProtection.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    switchedToProtection.setStatus(
        "current"
    )

warmRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2660)
)
warmRestart.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    warmRestart.setStatus(
        "current"
    )

ringIsInWaitToRestoreState = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2670)
)
ringIsInWaitToRestoreState.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ringIsInWaitToRestoreState.setStatus(
        "current"
    )

manualSwitchRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2680)
)
manualSwitchRequest.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchRequest.setStatus(
        "current"
    )

forcedSwitchRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2690)
)
forcedSwitchRequest.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchRequest.setStatus(
        "current"
    )

lockoutSwitchRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2700)
)
lockoutSwitchRequest.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lockoutSwitchRequest.setStatus(
        "current"
    )

rmonHistoriesAndAlarmsResetReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2710)
)
rmonHistoriesAndAlarmsResetReboot.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rmonHistoriesAndAlarmsResetReboot.setStatus(
        "current"
    )

rmonThresholdCrossingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2720)
)
rmonThresholdCrossingAlarm.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rmonThresholdCrossingAlarm.setStatus(
        "current"
    )

alarmsSuppressedByUserCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2730)
)
alarmsSuppressedByUserCommand.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    alarmsSuppressedByUserCommand.setStatus(
        "current"
    )

alarmsSuppressedForMaintenance = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2740)
)
alarmsSuppressedForMaintenance.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    alarmsSuppressedForMaintenance.setStatus(
        "current"
    )

switchingMatrixModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2750)
)
switchingMatrixModuleFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    switchingMatrixModuleFailure.setStatus(
        "current"
    )

lanConnectionPolarityReversed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2760)
)
lanConnectionPolarityReversed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lanConnectionPolarityReversed.setStatus(
        "current"
    )

autonomousPMReportMessageInhibited = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2780)
)
autonomousPMReportMessageInhibited.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    autonomousPMReportMessageInhibited.setStatus(
        "current"
    )

ioSlotToXCONCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2790)
)
ioSlotToXCONCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ioSlotToXCONCommunicationFailure.setStatus(
        "current"
    )

stsPathTraceIdentifierMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2800)
)
stsPathTraceIdentifierMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    stsPathTraceIdentifierMismatch.setStatus(
        "current"
    )

nePowerFailureAtConnectorA = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2810)
)
nePowerFailureAtConnectorA.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    nePowerFailureAtConnectorA.setStatus(
        "current"
    )

nePowerFailureAtConnectorB = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2820)
)
nePowerFailureAtConnectorB.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    nePowerFailureAtConnectorB.setStatus(
        "current"
    )

freeMemoryOnCardVeryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2830)
)
freeMemoryOnCardVeryLow.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    freeMemoryOnCardVeryLow.setStatus(
        "current"
    )

freeMemoryOnCardNearZero = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2840)
)
freeMemoryOnCardNearZero.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    freeMemoryOnCardNearZero.setStatus(
        "current"
    )

exerciseRequestOnRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2850)
)
exerciseRequestOnRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    exerciseRequestOnRing.setStatus(
        "current"
    )

exerciseRequestOnSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2860)
)
exerciseRequestOnSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    exerciseRequestOnSpan.setStatus(
        "current"
    )

squelchingPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2870)
)
squelchingPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    squelchingPath.setStatus(
        "current"
    )

extraTrafficPreempted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2880)
)
extraTrafficPreempted.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    extraTrafficPreempted.setStatus(
        "current"
    )

farEndLockoutOfWorkingRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2890)
)
farEndLockoutOfWorkingRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndLockoutOfWorkingRing.setStatus(
        "current"
    )

farEndLockoutOfWorkingSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2900)
)
farEndLockoutOfWorkingSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndLockoutOfWorkingSpan.setStatus(
        "current"
    )

farEndLockoutOfProtectionRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2910)
)
farEndLockoutOfProtectionRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndLockoutOfProtectionRing.setStatus(
        "current"
    )

farEndLockoutOfProtectionAllSpans = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2920)
)
farEndLockoutOfProtectionAllSpans.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndLockoutOfProtectionAllSpans.setStatus(
        "current"
    )

farEndWorkingFacilityForcedToSwitchToProtectionRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2930)
)
farEndWorkingFacilityForcedToSwitchToProtectionRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndWorkingFacilityForcedToSwitchToProtectionRing.setStatus(
        "current"
    )

farEndWorkingFacilityForcedToSwitchToProtectionSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2940)
)
farEndWorkingFacilityForcedToSwitchToProtectionSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndWorkingFacilityForcedToSwitchToProtectionSpan.setStatus(
        "current"
    )

farEndManualSwitchOfWorkingFacilityToProtectionRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2950)
)
farEndManualSwitchOfWorkingFacilityToProtectionRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndManualSwitchOfWorkingFacilityToProtectionRing.setStatus(
        "current"
    )

farEndManualSwitchOfWorkingFacilityToProtectionSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2960)
)
farEndManualSwitchOfWorkingFacilityToProtectionSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndManualSwitchOfWorkingFacilityToProtectionSpan.setStatus(
        "current"
    )

farEndExercisingRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2970)
)
farEndExercisingRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndExercisingRing.setStatus(
        "current"
    )

farEndExercisingSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2980)
)
farEndExercisingSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndExercisingSpan.setStatus(
        "current"
    )

farEndBERThresholdPassedForSignalFailureRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 2990)
)
farEndBERThresholdPassedForSignalFailureRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndBERThresholdPassedForSignalFailureRing.setStatus(
        "current"
    )

farEndBERThresholdPassedForSignalFailureSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3000)
)
farEndBERThresholdPassedForSignalFailureSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndBERThresholdPassedForSignalFailureSpan.setStatus(
        "current"
    )

farEndBERThresholdPassedForSignalDegradeRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3010)
)
farEndBERThresholdPassedForSignalDegradeRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndBERThresholdPassedForSignalDegradeRing.setStatus(
        "current"
    )

farEndBERThresholdPassedForSignalDegradeSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3020)
)
farEndBERThresholdPassedForSignalDegradeSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndBERThresholdPassedForSignalDegradeSpan.setStatus(
        "current"
    )

apsChannelFarEndProtectionLineSignalDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3030)
)
apsChannelFarEndProtectionLineSignalDegrade.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    apsChannelFarEndProtectionLineSignalDegrade.setStatus(
        "current"
    )

ringSwitchIsActiveOnTheEastSide = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3040)
)
ringSwitchIsActiveOnTheEastSide.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ringSwitchIsActiveOnTheEastSide.setStatus(
        "current"
    )

ringSwitchIsActiveOnTheWestSide = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3050)
)
ringSwitchIsActiveOnTheWestSide.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ringSwitchIsActiveOnTheWestSide.setStatus(
        "current"
    )

spanSwitchIsActiveOnTheEastSide = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3060)
)
spanSwitchIsActiveOnTheEastSide.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    spanSwitchIsActiveOnTheEastSide.setStatus(
        "current"
    )

spanSwitchIsActiveOnTheWestSide = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3070)
)
spanSwitchIsActiveOnTheWestSide.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    spanSwitchIsActiveOnTheWestSide.setStatus(
        "current"
    )

uniDirectionalFullPassThroughIsActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3080)
)
uniDirectionalFullPassThroughIsActive.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    uniDirectionalFullPassThroughIsActive.setStatus(
        "current"
    )

biDirectionalFullPassThroughIsActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3090)
)
biDirectionalFullPassThroughIsActive.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    biDirectionalFullPassThroughIsActive.setStatus(
        "current"
    )

kBytesPassThroughIsActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3100)
)
kBytesPassThroughIsActive.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    kBytesPassThroughIsActive.setStatus(
        "current"
    )

ringIsSegmented = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3110)
)
ringIsSegmented.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ringIsSegmented.setStatus(
        "current"
    )

ringTopologyIsUnderConstruction = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3120)
)
ringTopologyIsUnderConstruction.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ringTopologyIsUnderConstruction.setStatus(
        "current"
    )

lockoutOfProtectionAllSpans = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3130)
)
lockoutOfProtectionAllSpans.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lockoutOfProtectionAllSpans.setStatus(
        "current"
    )

farEndOfFiberIsProvisionedWithDifferentRingID = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3140)
)
farEndOfFiberIsProvisionedWithDifferentRingID.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndOfFiberIsProvisionedWithDifferentRingID.setStatus(
        "current"
    )

bothEndsOfFiberProvisionedAsEastOrBothAsWest = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3150)
)
bothEndsOfFiberProvisionedAsEastOrBothAsWest.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    bothEndsOfFiberProvisionedAsEastOrBothAsWest.setStatus(
        "current"
    )

securityInvalidLoginUsernameSeeAuditTrail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3160)
)
securityInvalidLoginUsernameSeeAuditTrail.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    securityInvalidLoginUsernameSeeAuditTrail.setStatus(
        "deprecated"
    )

autonomousMessagesInhibited = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3170)
)
autonomousMessagesInhibited.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    autonomousMessagesInhibited.setStatus(
        "current"
    )

trafficStormOnLANLANTemporarilyDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3180)
)
trafficStormOnLANLANTemporarilyDisabled.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    trafficStormOnLANLANTemporarilyDisabled.setStatus(
        "current"
    )

reptdbchgMessagesInhibited = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3190)
)
reptdbchgMessagesInhibited.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    reptdbchgMessagesInhibited.setStatus(
        "current"
    )

securityUserIDHasExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3200)
)
securityUserIDHasExpired.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    securityUserIDHasExpired.setStatus(
        "current"
    )

partialFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3210)
)
partialFanFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    partialFanFailure.setStatus(
        "current"
    )

forcedSwitchRequestOnRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3220)
)
forcedSwitchRequestOnRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchRequestOnRing.setStatus(
        "current"
    )

forcedSwitchRequestOnSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3230)
)
forcedSwitchRequestOnSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchRequestOnSpan.setStatus(
        "current"
    )

lockoutSwitchRequestOnRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3240)
)
lockoutSwitchRequestOnRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lockoutSwitchRequestOnRing.setStatus(
        "current"
    )

lockoutSwitchRequestOnSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3250)
)
lockoutSwitchRequestOnSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lockoutSwitchRequestOnSpan.setStatus(
        "current"
    )

manualSwitchRequestOnRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3260)
)
manualSwitchRequestOnRing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchRequestOnRing.setStatus(
        "current"
    )

manualSwitchRequestOnSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3270)
)
manualSwitchRequestOnSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchRequestOnSpan.setStatus(
        "current"
    )

communicationFailurePeerToPeerSlotControlBusA = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3280)
)
communicationFailurePeerToPeerSlotControlBusA.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    communicationFailurePeerToPeerSlotControlBusA.setStatus(
        "current"
    )

communicationFailurePeerToPeerSlotControlBusB = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3290)
)
communicationFailurePeerToPeerSlotControlBusB.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    communicationFailurePeerToPeerSlotControlBusB.setStatus(
        "current"
    )

controllerAToShelfSlotCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3300)
)
controllerAToShelfSlotCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    controllerAToShelfSlotCommunicationFailure.setStatus(
        "current"
    )

controllerBToShelfSlotCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3310)
)
controllerBToShelfSlotCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    controllerBToShelfSlotCommunicationFailure.setStatus(
        "current"
    )

interconnectionEquipmentFailureWorkingPayloadBus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3320)
)
interconnectionEquipmentFailureWorkingPayloadBus.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    interconnectionEquipmentFailureWorkingPayloadBus.setStatus(
        "current"
    )

interconnectionEquipmentFailureProtectPayloadBus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3330)
)
interconnectionEquipmentFailureProtectPayloadBus.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    interconnectionEquipmentFailureProtectPayloadBus.setStatus(
        "current"
    )

inhibitSwitchToProtectRequestOnEquipment = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3340)
)
inhibitSwitchToProtectRequestOnEquipment.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    inhibitSwitchToProtectRequestOnEquipment.setStatus(
        "current"
    )

inhibitSwitchToWorkingRequestOnEquipment = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3350)
)
inhibitSwitchToWorkingRequestOnEquipment.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    inhibitSwitchToWorkingRequestOnEquipment.setStatus(
        "current"
    )

berThresholdExceededForSignalDegradeLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3360)
)
berThresholdExceededForSignalDegradeLine.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    berThresholdExceededForSignalDegradeLine.setStatus(
        "current"
    )

berThresholdExceededForSignalDegradePath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3370)
)
berThresholdExceededForSignalDegradePath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    berThresholdExceededForSignalDegradePath.setStatus(
        "current"
    )

berThresholdExceededForSignalFailureLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3380)
)
berThresholdExceededForSignalFailureLine.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    berThresholdExceededForSignalFailureLine.setStatus(
        "current"
    )

berThresholdExceededForSignalFailurePath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3390)
)
berThresholdExceededForSignalFailurePath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    berThresholdExceededForSignalFailurePath.setStatus(
        "current"
    )

exercisingRingSuccessfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3400)
)
exercisingRingSuccessfully.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    exercisingRingSuccessfully.setStatus(
        "current"
    )

exercisingSpanSuccessfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3410)
)
exercisingSpanSuccessfully.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    exercisingSpanSuccessfully.setStatus(
        "current"
    )

spanIsInWaitToRestoreState = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3420)
)
spanIsInWaitToRestoreState.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    spanIsInWaitToRestoreState.setStatus(
        "current"
    )

exerciseRequestOnRingFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3430)
)
exerciseRequestOnRingFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    exerciseRequestOnRingFailed.setStatus(
        "current"
    )

exerciseRequestOnSpanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3440)
)
exerciseRequestOnSpanFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    exerciseRequestOnSpanFailed.setStatus(
        "current"
    )

farEndLockoutOfProtectionSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3450)
)
farEndLockoutOfProtectionSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndLockoutOfProtectionSpan.setStatus(
        "current"
    )

manufacturingDataMemoryEEPROMFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3460)
)
manufacturingDataMemoryEEPROMFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manufacturingDataMemoryEEPROMFailure.setStatus(
        "current"
    )

replaceableEquipmentOrUnitIsMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3470)
)
replaceableEquipmentOrUnitIsMissing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    replaceableEquipmentOrUnitIsMissing.setStatus(
        "current"
    )

softwareDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3480)
)
softwareDownloadFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    softwareDownloadFailed.setStatus(
        "current"
    )

extraTrafficPCADropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3490)
)
extraTrafficPCADropped.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    extraTrafficPCADropped.setStatus(
        "current"
    )

etherTxOversubscribed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3500)
)
etherTxOversubscribed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    etherTxOversubscribed.setStatus(
        "current"
    )

etherRxOverSubscribed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3510)
)
etherRxOverSubscribed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    etherRxOverSubscribed.setStatus(
        "current"
    )

etherTxExcessFlowCtrl = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3520)
)
etherTxExcessFlowCtrl.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    etherTxExcessFlowCtrl.setStatus(
        "current"
    )

etherRxExcessFlowCtrl = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3530)
)
etherRxExcessFlowCtrl.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    etherRxExcessFlowCtrl.setStatus(
        "current"
    )

transportLayerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3540)
)
transportLayerFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    transportLayerFailure.setStatus(
        "current"
    )

etherTxUnderrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3550)
)
etherTxUnderrun.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    etherTxUnderrun.setStatus(
        "current"
    )

synchronizationReferenceFrequencyOutOfBounds = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3560)
)
synchronizationReferenceFrequencyOutOfBounds.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    synchronizationReferenceFrequencyOutOfBounds.setStatus(
        "current"
    )

ntpOrSntpHostFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3570)
)
ntpOrSntpHostFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ntpOrSntpHostFailure.setStatus(
        "current"
    )

peerCardNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3580)
)
peerCardNotResponding.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    peerCardNotResponding.setStatus(
        "current"
    )

alarmsAndEventsSuppressedForThisObject = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3590)
)
alarmsAndEventsSuppressedForThisObject.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    alarmsAndEventsSuppressedForThisObject.setStatus(
        "current"
    )

ds3FrameFormatMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3600)
)
ds3FrameFormatMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ds3FrameFormatMismatch.setStatus(
        "current"
    )

waitToRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3610)
)
waitToRestore.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    waitToRestore.setStatus(
        "current"
    )

extremeHighVoltBatteryA = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3620)
)
extremeHighVoltBatteryA.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    extremeHighVoltBatteryA.setStatus(
        "current"
    )

extremeLowVoltBatteryA = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3630)
)
extremeLowVoltBatteryA.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    extremeLowVoltBatteryA.setStatus(
        "current"
    )

extremeHighVoltBatteryB = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3640)
)
extremeHighVoltBatteryB.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    extremeHighVoltBatteryB.setStatus(
        "current"
    )

extremeLowVoltBatteryB = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3650)
)
extremeLowVoltBatteryB.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    extremeLowVoltBatteryB.setStatus(
        "current"
    )

iosConfigCopyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3660)
)
iosConfigCopyFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    iosConfigCopyFailed.setStatus(
        "current"
    )

iosConfigCopyInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3670)
)
iosConfigCopyInProgress.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    iosConfigCopyInProgress.setStatus(
        "current"
    )

iosConfigCopySuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3680)
)
iosConfigCopySuccess.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    iosConfigCopySuccess.setStatus(
        "current"
    )

signalingUnableToSetupCircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3710)
)
signalingUnableToSetupCircuit.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    signalingUnableToSetupCircuit.setStatus(
        "current"
    )

errorInStartupConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3712)
)
errorInStartupConfig.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    errorInStartupConfig.setStatus(
        "current"
    )

noStartupConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3714)
)
noStartupConfig.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    noStartupConfig.setStatus(
        "current"
    )

needToSaveRunningConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3716)
)
needToSaveRunningConfig.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    needToSaveRunningConfig.setStatus(
        "current"
    )

invalidAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3718)
)
invalidAlarm.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    invalidAlarm.setStatus(
        "current"
    )

rsvpHelloFSMToNeighborDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3720)
)
rsvpHelloFSMToNeighborDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rsvpHelloFSMToNeighborDown.setStatus(
        "current"
    )

securityInvalidLoginUsername = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3722)
)
securityInvalidLoginUsername.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    securityInvalidLoginUsername.setStatus(
        "current"
    )

databaseBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3724)
)
databaseBackupFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    databaseBackupFailed.setStatus(
        "current"
    )

databaseRestoreFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3726)
)
databaseRestoreFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    databaseRestoreFailed.setStatus(
        "current"
    )

lmpHelloFSMToControlChannelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3730)
)
lmpHelloFSMToControlChannelDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lmpHelloFSMToControlChannelDown.setStatus(
        "current"
    )

lmpNeighborDiscoveryHasFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3740)
)
lmpNeighborDiscoveryHasFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lmpNeighborDiscoveryHasFailed.setStatus(
        "current"
    )

unauthorizedIncomingSignalingRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3750)
)
unauthorizedIncomingSignalingRequest.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    unauthorizedIncomingSignalingRequest.setStatus(
        "current"
    )

auditLog80PercentFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3760)
)
auditLog80PercentFull.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    auditLog80PercentFull.setStatus(
        "current"
    )

moduleCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3762)
)
moduleCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    moduleCommunicationFailure.setStatus(
        "current"
    )

auditLog100PercentFullOldestRecordsWillBeLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3764)
)
auditLog100PercentFullOldestRecordsWillBeLost.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    auditLog100PercentFullOldestRecordsWillBeLost.setStatus(
        "current"
    )

standbyDatabaseOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3766)
)
standbyDatabaseOutOfSync.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    standbyDatabaseOutOfSync.setStatus(
        "current"
    )

redundantPowerCapabilityLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3768)
)
redundantPowerCapabilityLost.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    redundantPowerCapabilityLost.setStatus(
        "current"
    )

forcedSwitchToPrimaryReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3770)
)
forcedSwitchToPrimaryReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchToPrimaryReference.setStatus(
        "current"
    )

forcedSwitchToSecondReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3780)
)
forcedSwitchToSecondReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchToSecondReference.setStatus(
        "current"
    )

forcedSwitchToThirdReference = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3790)
)
forcedSwitchToThirdReference.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchToThirdReference.setStatus(
        "current"
    )

forcedSwitchToInternalClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3800)
)
forcedSwitchToInternalClock.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchToInternalClock.setStatus(
        "current"
    )

industrialHighTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 3805)
)
industrialHighTemperature.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    industrialHighTemperature.setStatus(
        "current"
    )

timSectionTraceIdentifierMismatchFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4000)
)
timSectionTraceIdentifierMismatchFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    timSectionTraceIdentifierMismatchFailure.setStatus(
        "current"
    )

aisMultiplexSectionAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4010)
)
aisMultiplexSectionAlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    aisMultiplexSectionAlarmIndicationSignal.setStatus(
        "current"
    )

rdiMultiplexSectionRemoteDefectOrAlarmIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4020)
)
rdiMultiplexSectionRemoteDefectOrAlarmIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rdiMultiplexSectionRemoteDefectOrAlarmIndication.setStatus(
        "current"
    )

timHighOrderTraceIdentifierMismatchFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4030)
)
timHighOrderTraceIdentifierMismatchFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    timHighOrderTraceIdentifierMismatchFailure.setStatus(
        "current"
    )

aisAdministrationUnitAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4040)
)
aisAdministrationUnitAlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    aisAdministrationUnitAlarmIndicationSignal.setStatus(
        "current"
    )

lopAdministrationUnitLossOfPointer = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4050)
)
lopAdministrationUnitLossOfPointer.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lopAdministrationUnitLossOfPointer.setStatus(
        "current"
    )

slmfUnequippedHighOrderPathUnequipped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4060)
)
slmfUnequippedHighOrderPathUnequipped.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    slmfUnequippedHighOrderPathUnequipped.setStatus(
        "current"
    )

slmfPLMHighOrderPathLabelMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4070)
)
slmfPLMHighOrderPathLabelMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    slmfPLMHighOrderPathLabelMismatch.setStatus(
        "current"
    )

rdiHighOrderRemoteDefectOrAlarmIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4080)
)
rdiHighOrderRemoteDefectOrAlarmIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rdiHighOrderRemoteDefectOrAlarmIndication.setStatus(
        "current"
    )

lopTributaryUnitLossOfPointer = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4090)
)
lopTributaryUnitLossOfPointer.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lopTributaryUnitLossOfPointer.setStatus(
        "current"
    )

aisTributaryUnitAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4100)
)
aisTributaryUnitAlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    aisTributaryUnitAlarmIndicationSignal.setStatus(
        "current"
    )

slmfUnequippedLowOrderPathUnequipped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4110)
)
slmfUnequippedLowOrderPathUnequipped.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    slmfUnequippedLowOrderPathUnequipped.setStatus(
        "current"
    )

slmfPLMLowOrderPathLabelMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4120)
)
slmfPLMLowOrderPathLabelMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    slmfPLMLowOrderPathLabelMismatch.setStatus(
        "current"
    )

timLowOrderTraceIdentifierMismatchFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4130)
)
timLowOrderTraceIdentifierMismatchFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    timLowOrderTraceIdentifierMismatchFailure.setStatus(
        "current"
    )

rfiLowOrderRemoteFailureOrAlarmIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4140)
)
rfiLowOrderRemoteFailureOrAlarmIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rfiLowOrderRemoteFailureOrAlarmIndication.setStatus(
        "current"
    )

g811PrimaryReferenceClockTraceable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4150)
)
g811PrimaryReferenceClockTraceable.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    g811PrimaryReferenceClockTraceable.setStatus(
        "current"
    )

g812TransitNodeClockTraceable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4160)
)
g812TransitNodeClockTraceable.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    g812TransitNodeClockTraceable.setStatus(
        "current"
    )

g812LocalNodeClockTraceable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4170)
)
g812LocalNodeClockTraceable.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    g812LocalNodeClockTraceable.setStatus(
        "current"
    )

g813SynchronousEquipmentTimingSourceTraceable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4180)
)
g813SynchronousEquipmentTimingSourceTraceable.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    g813SynchronousEquipmentTimingSourceTraceable.setStatus(
        "current"
    )

e1LoopbackDueToFEACCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4190)
)
e1LoopbackDueToFEACCommand.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    e1LoopbackDueToFEACCommand.setStatus(
        "current"
    )

e1LoopbackCommandSentToFarEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4200)
)
e1LoopbackCommandSentToFarEnd.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    e1LoopbackCommandSentToFarEnd.setStatus(
        "current"
    )

e3LoopbackDueToFEACCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4210)
)
e3LoopbackDueToFEACCommand.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    e3LoopbackDueToFEACCommand.setStatus(
        "current"
    )

farEndMultipleE1LOSDetectedOnE3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4220)
)
farEndMultipleE1LOSDetectedOnE3.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndMultipleE1LOSDetectedOnE3.setStatus(
        "current"
    )

farEndE1EqptFailNonServiceAffecting = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4230)
)
farEndE1EqptFailNonServiceAffecting.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndE1EqptFailNonServiceAffecting.setStatus(
        "current"
    )

farEndE1EqptFailServiceAffecting = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4240)
)
farEndE1EqptFailServiceAffecting.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndE1EqptFailServiceAffecting.setStatus(
        "current"
    )

farEndSingleE1LOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4250)
)
farEndSingleE1LOS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndSingleE1LOS.setStatus(
        "current"
    )

farEndE3EqptFailServiceAffecting = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4260)
)
farEndE3EqptFailServiceAffecting.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndE3EqptFailServiceAffecting.setStatus(
        "current"
    )

e3LoopbackCommandSentToFarEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4270)
)
e3LoopbackCommandSentToFarEnd.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    e3LoopbackCommandSentToFarEnd.setStatus(
        "current"
    )

farEndE3EqptFailNonServiceAffecting = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4280)
)
farEndE3EqptFailNonServiceAffecting.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndE3EqptFailNonServiceAffecting.setStatus(
        "current"
    )

lowVoltBatteryA = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4290)
)
lowVoltBatteryA.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lowVoltBatteryA.setStatus(
        "current"
    )

highVoltBatteryA = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4300)
)
highVoltBatteryA.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    highVoltBatteryA.setStatus(
        "current"
    )

lowVoltBatteryB = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4310)
)
lowVoltBatteryB.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lowVoltBatteryB.setStatus(
        "current"
    )

highVoltBatteryB = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4320)
)
highVoltBatteryB.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    highVoltBatteryB.setStatus(
        "current"
    )

msspRingOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4330)
)
msspRingOutOfSync.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    msspRingOutOfSync.setStatus(
        "current"
    )

msspMultiNodeTableUpdateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4340)
)
msspMultiNodeTableUpdateCompleted.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    msspMultiNodeTableUpdateCompleted.setStatus(
        "current"
    )

automaticSNCPSwitchCausedByAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4350)
)
automaticSNCPSwitchCausedByAIS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticSNCPSwitchCausedByAIS.setStatus(
        "current"
    )

automaticSNCPSwitchCausedByLOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4360)
)
automaticSNCPSwitchCausedByLOP.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticSNCPSwitchCausedByLOP.setStatus(
        "current"
    )

automaticSNCPSwitchCausedByUNEQ = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4370)
)
automaticSNCPSwitchCausedByUNEQ.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticSNCPSwitchCausedByUNEQ.setStatus(
        "current"
    )

automaticSNCPSwitchCausedByPDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4380)
)
automaticSNCPSwitchCausedByPDI.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticSNCPSwitchCausedByPDI.setStatus(
        "current"
    )

automaticSNCPSwitchCausedBySFBER = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4390)
)
automaticSNCPSwitchCausedBySFBER.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticSNCPSwitchCausedBySFBER.setStatus(
        "current"
    )

automaticSNCPSwitchCausedBySDBER = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4400)
)
automaticSNCPSwitchCausedBySDBER.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticSNCPSwitchCausedBySDBER.setStatus(
        "current"
    )

stmConcatenationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4410)
)
stmConcatenationError.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    stmConcatenationError.setStatus(
        "current"
    )

e3IdleCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4420)
)
e3IdleCondition.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    e3IdleCondition.setStatus(
        "current"
    )

channelMSSPInconsistentAPSCode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4430)
)
channelMSSPInconsistentAPSCode.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    channelMSSPInconsistentAPSCode.setStatus(
        "current"
    )

channelMSSPImproperAPSCodeAPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4440)
)
channelMSSPImproperAPSCodeAPS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    channelMSSPImproperAPSCodeAPS.setStatus(
        "current"
    )

channelMSSPNodeIdMismatchAPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4450)
)
channelMSSPNodeIdMismatchAPS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    channelMSSPNodeIdMismatchAPS.setStatus(
        "current"
    )

channelMSSPDefaultKAPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4460)
)
channelMSSPDefaultKAPS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    channelMSSPDefaultKAPS.setStatus(
        "current"
    )

channelMSSPConnectionLossAPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4470)
)
channelMSSPConnectionLossAPS.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    channelMSSPConnectionLossAPS.setStatus(
        "current"
    )

minimumClockTraceableSDH = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4480)
)
minimumClockTraceableSDH.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    minimumClockTraceableSDH.setStatus(
        "current"
    )

lineIsInWaitToRestoreStateSDH = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4490)
)
lineIsInWaitToRestoreStateSDH.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lineIsInWaitToRestoreStateSDH.setStatus(
        "current"
    )

berThresholdExceededForSignalDegradeHighOrder = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4500)
)
berThresholdExceededForSignalDegradeHighOrder.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    berThresholdExceededForSignalDegradeHighOrder.setStatus(
        "current"
    )

berThresholdExceededForSignalFailureHighOrder = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4510)
)
berThresholdExceededForSignalFailureHighOrder.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    berThresholdExceededForSignalFailureHighOrder.setStatus(
        "current"
    )

berThresholdExceededForSignalDegradeLowOrder = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4520)
)
berThresholdExceededForSignalDegradeLowOrder.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    berThresholdExceededForSignalDegradeLowOrder.setStatus(
        "current"
    )

berThresholdExceededForSignalFailureLowOrder = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4530)
)
berThresholdExceededForSignalFailureLowOrder.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    berThresholdExceededForSignalFailureLowOrder.setStatus(
        "current"
    )

failureToSwitchToProtectionHighOrderPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4540)
)
failureToSwitchToProtectionHighOrderPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    failureToSwitchToProtectionHighOrderPath.setStatus(
        "current"
    )

failureToSwitchToProtectionLowOrderPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4550)
)
failureToSwitchToProtectionLowOrderPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    failureToSwitchToProtectionLowOrderPath.setStatus(
        "current"
    )

lofAdministrationUnitLossOfMultiFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4560)
)
lofAdministrationUnitLossOfMultiFrame.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lofAdministrationUnitLossOfMultiFrame.setStatus(
        "current"
    )

sdhSpanIsInWaitToRestoreState = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4570)
)
sdhSpanIsInWaitToRestoreState.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    sdhSpanIsInWaitToRestoreState.setStatus(
        "current"
    )

a8b10bOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4755)
)
a8b10bOutOfSync.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    a8b10bOutOfSync.setStatus(
        "current"
    )

odukPMAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4760)
)
odukPMAlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukPMAlarmIndicationSignal.setStatus(
        "current"
    )

otukAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4765)
)
otukAlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    otukAlarmIndicationSignal.setStatus(
        "current"
    )

otukSMBackwardDefectIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4770)
)
otukSMBackwardDefectIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    otukSMBackwardDefectIndication.setStatus(
        "current"
    )

odukBackwardDefectIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4775)
)
odukBackwardDefectIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukBackwardDefectIndication.setStatus(
        "current"
    )

fecUncorrectedWord = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4780)
)
fecUncorrectedWord.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    fecUncorrectedWord.setStatus(
        "current"
    )

gccTerminationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4785)
)
gccTerminationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    gccTerminationFailure.setStatus(
        "current"
    )

otukIncomingAlignmentError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4790)
)
otukIncomingAlignmentError.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    otukIncomingAlignmentError.setStatus(
        "current"
    )

odukLockedDefectPM = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4795)
)
odukLockedDefectPM.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukLockedDefectPM.setStatus(
        "current"
    )

lossOfMultiFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4800)
)
lossOfMultiFrame.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lossOfMultiFrame.setStatus(
        "current"
    )

odukOpenConnectionIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4805)
)
odukOpenConnectionIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukOpenConnectionIndication.setStatus(
        "current"
    )

payloadTypeIdentifierMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4810)
)
payloadTypeIdentifierMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadTypeIdentifierMismatch.setStatus(
        "current"
    )

odukTrailTraceIdentifierMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4815)
)
odukTrailTraceIdentifierMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukTrailTraceIdentifierMismatch.setStatus(
        "current"
    )

otukTrailTraceIdentifierMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4820)
)
otukTrailTraceIdentifierMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    otukTrailTraceIdentifierMismatch.setStatus(
        "current"
    )

equipmentHighLaserBias = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4825)
)
equipmentHighLaserBias.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentHighLaserBias.setStatus(
        "current"
    )

equipmentHighLaserTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4830)
)
equipmentHighLaserTemp.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentHighLaserTemp.setStatus(
        "current"
    )

equipmentHighLaserPeltier = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4835)
)
equipmentHighLaserPeltier.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentHighLaserPeltier.setStatus(
        "current"
    )

facilityHighRxPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4840)
)
facilityHighRxPower.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    facilityHighRxPower.setStatus(
        "current"
    )

equipmentHighTxPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4845)
)
equipmentHighTxPower.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentHighTxPower.setStatus(
        "current"
    )

equipmentHighTransceiverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4850)
)
equipmentHighTransceiverVoltage.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentHighTransceiverVoltage.setStatus(
        "current"
    )

equipmentLowLaserBias = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4855)
)
equipmentLowLaserBias.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentLowLaserBias.setStatus(
        "current"
    )

equipmentLowLaserTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4860)
)
equipmentLowLaserTemp.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentLowLaserTemp.setStatus(
        "current"
    )

equipmentLowLaserPeltier = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4865)
)
equipmentLowLaserPeltier.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentLowLaserPeltier.setStatus(
        "current"
    )

facilityLowRxPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4870)
)
facilityLowRxPower.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    facilityLowRxPower.setStatus(
        "current"
    )

equipmentLowTxPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4875)
)
equipmentLowTxPower.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentLowTxPower.setStatus(
        "current"
    )

equipmentLowTransceiverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4880)
)
equipmentLowTransceiverVoltage.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentLowTransceiverVoltage.setStatus(
        "current"
    )

equipmentRxLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4885)
)
equipmentRxLocked.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentRxLocked.setStatus(
        "current"
    )

equipmentSquelched = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4890)
)
equipmentSquelched.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentSquelched.setStatus(
        "current"
    )

equipmentTxLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4895)
)
equipmentTxLocked.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentTxLocked.setStatus(
        "current"
    )

otukSignalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4900)
)
otukSignalFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    otukSignalFailure.setStatus(
        "current"
    )

odukSignalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4905)
)
odukSignalFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukSignalFailure.setStatus(
        "current"
    )

otukSignalDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4910)
)
otukSignalDegrade.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    otukSignalDegrade.setStatus(
        "current"
    )

odukSignalDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4915)
)
odukSignalDegrade.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukSignalDegrade.setStatus(
        "current"
    )

pluggablePortMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4920)
)
pluggablePortMissing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    pluggablePortMissing.setStatus(
        "current"
    )

pluggablePortRateMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4925)
)
pluggablePortRateMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    pluggablePortRateMismatch.setStatus(
        "current"
    )

pluggablePortSecurityCodeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4930)
)
pluggablePortSecurityCodeMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    pluggablePortSecurityCodeMismatch.setStatus(
        "current"
    )

tciNotSelected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4935)
)
tciNotSelected.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tciNotSelected.setStatus(
        "current"
    )

tci1ClockFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4940)
)
tci1ClockFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tci1ClockFailure.setStatus(
        "current"
    )

odukPMBackwardDefectIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4945)
)
odukPMBackwardDefectIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukPMBackwardDefectIndication.setStatus(
        "current"
    )

odukTCM1BackwardDefectIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4950)
)
odukTCM1BackwardDefectIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukTCM1BackwardDefectIndication.setStatus(
        "current"
    )

odukTCM2BackwardDefectIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4955)
)
odukTCM2BackwardDefectIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukTCM2BackwardDefectIndication.setStatus(
        "current"
    )

equipmentHighRxTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4960)
)
equipmentHighRxTemperature.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentHighRxTemperature.setStatus(
        "current"
    )

equipmentLowRxTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4965)
)
equipmentLowRxTemperature.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentLowRxTemperature.setStatus(
        "current"
    )

tci2ClockFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4970)
)
tci2ClockFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tci2ClockFailure.setStatus(
        "current"
    )

equipmentWavelengthMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4975)
)
equipmentWavelengthMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentWavelengthMismatch.setStatus(
        "current"
    )

dspCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4980)
)
dspCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    dspCommunicationFailure.setStatus(
        "current"
    )

dspFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 4985)
)
dspFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    dspFailure.setStatus(
        "current"
    )

laserApproachingEndOfLife = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5000)
)
laserApproachingEndOfLife.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    laserApproachingEndOfLife.setStatus(
        "current"
    )

crossconnectLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5010)
)
crossconnectLoopback.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    crossconnectLoopback.setStatus(
        "current"
    )

adminLogoutOfUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5020)
)
adminLogoutOfUser.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    adminLogoutOfUser.setStatus(
        "current"
    )

userLockedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5030)
)
userLockedOut.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    userLockedOut.setStatus(
        "current"
    )

adminLockoutOfUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5040)
)
adminLockoutOfUser.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    adminLockoutOfUser.setStatus(
        "current"
    )

adminLockoutClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5050)
)
adminLockoutClear.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    adminLockoutClear.setStatus(
        "current"
    )

invalidLoginUsername = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5060)
)
invalidLoginUsername.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    invalidLoginUsername.setStatus(
        "current"
    )

securityInvalidLoginPassword = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5070)
)
securityInvalidLoginPassword.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    securityInvalidLoginPassword.setStatus(
        "current"
    )

securityInvalidLoginLockedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5080)
)
securityInvalidLoginLockedOut.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    securityInvalidLoginLockedOut.setStatus(
        "current"
    )

securityInvalidLoginAlreadyLoggedOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5090)
)
securityInvalidLoginAlreadyLoggedOn.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    securityInvalidLoginAlreadyLoggedOn.setStatus(
        "current"
    )

loginOfUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5100)
)
loginOfUser.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    loginOfUser.setStatus(
        "current"
    )

automaticLogoutOfIdleUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5110)
)
automaticLogoutOfIdleUser.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticLogoutOfIdleUser.setStatus(
        "current"
    )

logoutOfUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5120)
)
logoutOfUser.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    logoutOfUser.setStatus(
        "current"
    )

enhancedRemoteFailureIndicationPathServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5200)
)
enhancedRemoteFailureIndicationPathServer.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    enhancedRemoteFailureIndicationPathServer.setStatus(
        "current"
    )

enhancedRemoteFailureIndicationPathConnectivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5210)
)
enhancedRemoteFailureIndicationPathConnectivity.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    enhancedRemoteFailureIndicationPathConnectivity.setStatus(
        "current"
    )

enhancedRemoteFailureIndicationPathPayload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5220)
)
enhancedRemoteFailureIndicationPathPayload.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    enhancedRemoteFailureIndicationPathPayload.setStatus(
        "current"
    )

firewallHasBeenDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5230)
)
firewallHasBeenDisabled.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    firewallHasBeenDisabled.setStatus(
        "current"
    )

securityIntrusionDetPwd = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5240)
)
securityIntrusionDetPwd.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    securityIntrusionDetPwd.setStatus(
        "current"
    )

securityIntrusionDetUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5250)
)
securityIntrusionDetUser.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    securityIntrusionDetUser.setStatus(
        "current"
    )

connectionEquipmentMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5260)
)
connectionEquipmentMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    connectionEquipmentMismatch.setStatus(
        "current"
    )

disableInactiveUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5270)
)
disableInactiveUser.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    disableInactiveUser.setStatus(
        "current"
    )

disableInactiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5280)
)
disableInactiveClear.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    disableInactiveClear.setStatus(
        "current"
    )

batteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5290)
)
batteryFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    batteryFailure.setStatus(
        "current"
    )

extremeHighVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5300)
)
extremeHighVolt.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    extremeHighVolt.setStatus(
        "current"
    )

extremeLowVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5310)
)
extremeLowVolt.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    extremeLowVolt.setStatus(
        "current"
    )

highVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5320)
)
highVolt.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    highVolt.setStatus(
        "current"
    )

lowVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5330)
)
lowVolt.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lowVolt.setStatus(
        "current"
    )

suspendUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5340)
)
suspendUser.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    suspendUser.setStatus(
        "current"
    )

suspendUserClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5350)
)
suspendUserClear.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    suspendUserClear.setStatus(
        "current"
    )

lineDccTerminationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5360)
)
lineDccTerminationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lineDccTerminationFailure.setStatus(
        "current"
    )

multiplexSectionDccTerminationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5370)
)
multiplexSectionDccTerminationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    multiplexSectionDccTerminationFailure.setStatus(
        "current"
    )

gigaBitEthernetOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5380)
)
gigaBitEthernetOutOfSync.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    gigaBitEthernetOutOfSync.setStatus(
        "current"
    )

sequenceMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5390)
)
sequenceMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    sequenceMismatch.setStatus(
        "current"
    )

lossOfAlignment = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5400)
)
lossOfAlignment.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lossOfAlignment.setStatus(
        "current"
    )

outOfUseByAdministrativeCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5410)
)
outOfUseByAdministrativeCommand.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    outOfUseByAdministrativeCommand.setStatus(
        "current"
    )

outOfUseTransportFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5420)
)
outOfUseTransportFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    outOfUseTransportFailure.setStatus(
        "current"
    )

vcatGroupDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5430)
)
vcatGroupDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    vcatGroupDown.setStatus(
        "current"
    )

vcatGroupDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5440)
)
vcatGroupDegraded.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    vcatGroupDegraded.setStatus(
        "current"
    )

vcatGroupIncomplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5450)
)
vcatGroupIncomplete.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    vcatGroupIncomplete.setStatus(
        "current"
    )

alarmIndicationSignalInTX = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5460)
)
alarmIndicationSignalInTX.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    alarmIndicationSignalInTX.setStatus(
        "current"
    )

remoteAlarmIndicationInTX = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5470)
)
remoteAlarmIndicationInTX.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    remoteAlarmIndicationInTX.setStatus(
        "current"
    )

kByteAPSChannelFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5480)
)
kByteAPSChannelFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    kByteAPSChannelFailure.setStatus(
        "current"
    )

apsInvalidMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5490)
)
apsInvalidMode.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    apsInvalidMode.setStatus(
        "current"
    )

ipAddressAlreadyInUseWithinTheSameDccArea = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5500)
)
ipAddressAlreadyInUseWithinTheSameDccArea.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ipAddressAlreadyInUseWithinTheSameDccArea.setStatus(
        "current"
    )

nodeNameInUseWithinTheSameDccArea = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5510)
)
nodeNameInUseWithinTheSameDccArea.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    nodeNameInUseWithinTheSameDccArea.setStatus(
        "current"
    )

rearPanelEthernetLinkRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5520)
)
rearPanelEthernetLinkRemoved.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rearPanelEthernetLinkRemoved.setStatus(
        "current"
    )

manualSwitchToProtectResultedInNoTrafficSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5530)
)
manualSwitchToProtectResultedInNoTrafficSwitch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchToProtectResultedInNoTrafficSwitch.setStatus(
        "current"
    )

manualSwitchBackToWorkingResultedInNoTrafficSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5540)
)
manualSwitchBackToWorkingResultedInNoTrafficSwitch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualSwitchBackToWorkingResultedInNoTrafficSwitch.setStatus(
        "current"
    )

forcedSwitchToProtectResultedInNoTrafficSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5550)
)
forcedSwitchToProtectResultedInNoTrafficSwitch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchToProtectResultedInNoTrafficSwitch.setStatus(
        "current"
    )

forcedSwitchBackToWorkingResultedInNoTrafficSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5560)
)
forcedSwitchBackToWorkingResultedInNoTrafficSwitch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forcedSwitchBackToWorkingResultedInNoTrafficSwitch.setStatus(
        "current"
    )

duplicateSerialNumberDetectedOnAPluggableEntity = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5570)
)
duplicateSerialNumberDetectedOnAPluggableEntity.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    duplicateSerialNumberDetectedOnAPluggableEntity.setStatus(
        "current"
    )

lossOfSignalForOpticalChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5600)
)
lossOfSignalForOpticalChannel.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lossOfSignalForOpticalChannel.setStatus(
        "current"
    )

encapsulationMismatchPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5610)
)
encapsulationMismatchPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    encapsulationMismatchPath.setStatus(
        "current"
    )

encapsulationMismatchVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5620)
)
encapsulationMismatchVT.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    encapsulationMismatchVT.setStatus(
        "current"
    )

encapsulationMismatchHighOrderPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5630)
)
encapsulationMismatchHighOrderPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    encapsulationMismatchHighOrderPath.setStatus(
        "current"
    )

encapsulationMismatchLowOrderPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5640)
)
encapsulationMismatchLowOrderPath.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    encapsulationMismatchLowOrderPath.setStatus(
        "current"
    )

gfpUserPayloadMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5650)
)
gfpUserPayloadMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    gfpUserPayloadMismatch.setStatus(
        "current"
    )

gfpFibreChannelDistanceExtensionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5660)
)
gfpFibreChannelDistanceExtensionMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    gfpFibreChannelDistanceExtensionMismatch.setStatus(
        "current"
    )

gfpFibreChannelDistanceExtensionBufferStarvation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5670)
)
gfpFibreChannelDistanceExtensionBufferStarvation.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    gfpFibreChannelDistanceExtensionBufferStarvation.setStatus(
        "current"
    )

gfpFibreChannelDistanceExtensionCreditStarvation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5680)
)
gfpFibreChannelDistanceExtensionCreditStarvation.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    gfpFibreChannelDistanceExtensionCreditStarvation.setStatus(
        "current"
    )

automaticWdmAnsFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5690)
)
automaticWdmAnsFinished.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticWdmAnsFinished.setStatus(
        "current"
    )

gfpClientSignalFailDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5700)
)
gfpClientSignalFailDetected.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    gfpClientSignalFailDetected.setStatus(
        "current"
    )

gfpLossOfFrameDelineation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5710)
)
gfpLossOfFrameDelineation.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    gfpLossOfFrameDelineation.setStatus(
        "current"
    )

gfpExtensionHeaderMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5730)
)
gfpExtensionHeaderMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    gfpExtensionHeaderMismatch.setStatus(
        "current"
    )

incomingOverheadSignalAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5740)
)
incomingOverheadSignalAbsent.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    incomingOverheadSignalAbsent.setStatus(
        "current"
    )

opticalSafetyRemoteInterlockOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5750)
)
opticalSafetyRemoteInterlockOn.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalSafetyRemoteInterlockOn.setStatus(
        "current"
    )

automaticPowerControlCorrectionSkipped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5770)
)
automaticPowerControlCorrectionSkipped.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticPowerControlCorrectionSkipped.setStatus(
        "current"
    )

apcCannotSetValueDueToRangeLimits = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5780)
)
apcCannotSetValueDueToRangeLimits.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    apcCannotSetValueDueToRangeLimits.setStatus(
        "current"
    )

lcasVcgMemberTxSideInAddState = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5790)
)
lcasVcgMemberTxSideInAddState.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lcasVcgMemberTxSideInAddState.setStatus(
        "current"
    )

farEndManualSwitchBackToWorkingSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5800)
)
farEndManualSwitchBackToWorkingSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndManualSwitchBackToWorkingSpan.setStatus(
        "current"
    )

farEndForcedSwitchBackToWorkingSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5810)
)
farEndForcedSwitchBackToWorkingSpan.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    farEndForcedSwitchBackToWorkingSpan.setStatus(
        "current"
    )

universalTransponderModuleHardwareFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5820)
)
universalTransponderModuleHardwareFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    universalTransponderModuleHardwareFailure.setStatus(
        "current"
    )

universalTransponderModuleCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5830)
)
universalTransponderModuleCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    universalTransponderModuleCommunicationFailure.setStatus(
        "current"
    )

pluginModuleRangeSettingsMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5840)
)
pluginModuleRangeSettingsMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    pluginModuleRangeSettingsMismatch.setStatus(
        "current"
    )

lcasVcgMemberTxSideInDnuState = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5850)
)
lcasVcgMemberTxSideInDnuState.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lcasVcgMemberTxSideInDnuState.setStatus(
        "current"
    )

lcasControlWordCrcCheckFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5860)
)
lcasControlWordCrcCheckFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lcasControlWordCrcCheckFailure.setStatus(
        "current"
    )

lcasVcgMemberRxSideInFailState = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5870)
)
lcasVcgMemberRxSideInFailState.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lcasVcgMemberRxSideInFailState.setStatus(
        "current"
    )

signalLossOnDataInterface = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5880)
)
signalLossOnDataInterface.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    signalLossOnDataInterface.setStatus(
        "current"
    )

synchronizationLossOnDataInterface = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5890)
)
synchronizationLossOnDataInterface.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    synchronizationLossOnDataInterface.setStatus(
        "current"
    )

portFAIL = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5900)
)
portFAIL.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    portFAIL.setStatus(
        "current"
    )

unreachablePortTargetPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5910)
)
unreachablePortTargetPower.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    unreachablePortTargetPower.setStatus(
        "current"
    )

portAddPowerDegradeLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5920)
)
portAddPowerDegradeLow.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    portAddPowerDegradeLow.setStatus(
        "current"
    )

portAddPowerDegradeHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5930)
)
portAddPowerDegradeHigh.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    portAddPowerDegradeHigh.setStatus(
        "current"
    )

portAddPowerFailLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5940)
)
portAddPowerFailLow.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    portAddPowerFailLow.setStatus(
        "current"
    )

portAddPowerFailHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 5950)
)
portAddPowerFailHigh.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    portAddPowerFailHigh.setStatus(
        "current"
    )

automaticPowerControlTerminatedOnManualRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6000)
)
automaticPowerControlTerminatedOnManualRequest.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticPowerControlTerminatedOnManualRequest.setStatus(
        "current"
    )

oduk1AlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6010)
)
oduk1AlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    oduk1AlarmIndicationSignal.setStatus(
        "current"
    )

oduk2AlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6020)
)
oduk2AlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    oduk2AlarmIndicationSignal.setStatus(
        "current"
    )

oduk3AlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6030)
)
oduk3AlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    oduk3AlarmIndicationSignal.setStatus(
        "current"
    )

oduk4AlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6040)
)
oduk4AlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    oduk4AlarmIndicationSignal.setStatus(
        "current"
    )

temperatureReadingMismatchBetweenSCCards = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6050)
)
temperatureReadingMismatchBetweenSCCards.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    temperatureReadingMismatchBetweenSCCards.setStatus(
        "current"
    )

voltageReadingMismatchBetweenSCCards = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6060)
)
voltageReadingMismatchBetweenSCCards.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    voltageReadingMismatchBetweenSCCards.setStatus(
        "current"
    )

alarmsSuppressedonOutOfGroupVcatMember = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6070)
)
alarmsSuppressedonOutOfGroupVcatMember.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    alarmsSuppressedonOutOfGroupVcatMember.setStatus(
        "current"
    )

blsrSoftwareVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6080)
)
blsrSoftwareVersionMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    blsrSoftwareVersionMismatch.setStatus(
        "current"
    )

optimized1Plus1ApsPrimaryFacility = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6090)
)
optimized1Plus1ApsPrimaryFacility.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    optimized1Plus1ApsPrimaryFacility.setStatus(
        "current"
    )

optimized1Plus1ApsPrimarySectionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6100)
)
optimized1Plus1ApsPrimarySectionMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    optimized1Plus1ApsPrimarySectionMismatch.setStatus(
        "current"
    )

optimized1Plus1ApsInvalidPrimarySection = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6110)
)
optimized1Plus1ApsInvalidPrimarySection.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    optimized1Plus1ApsInvalidPrimarySection.setStatus(
        "current"
    )

compositeClockHighLineVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6120)
)
compositeClockHighLineVoltage.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    compositeClockHighLineVoltage.setStatus(
        "current"
    )

berThresholdExceededForSignalDegradeVt = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6130)
)
berThresholdExceededForSignalDegradeVt.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    berThresholdExceededForSignalDegradeVt.setStatus(
        "current"
    )

berThresholdExceededForSignalFailureVt = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6140)
)
berThresholdExceededForSignalFailureVt.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    berThresholdExceededForSignalFailureVt.setStatus(
        "current"
    )

spanLengthOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6150)
)
spanLengthOutOfRange.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    spanLengthOutOfRange.setStatus(
        "current"
    )

idleSignalCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6170)
)
idleSignalCondition.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    idleSignalCondition.setStatus(
        "current"
    )

idleSignalConditionInTx = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6180)
)
idleSignalConditionInTx.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    idleSignalConditionInTx.setStatus(
        "current"
    )

vtPathTraceIdentifierMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6190)
)
vtPathTraceIdentifierMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    vtPathTraceIdentifierMismatch.setStatus(
        "current"
    )

lossOfFrameInTX = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6200)
)
lossOfFrameInTX.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lossOfFrameInTX.setStatus(
        "current"
    )

provisioningMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6210)
)
provisioningMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    provisioningMismatch.setStatus(
        "current"
    )

sectionTraceIdentifierMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6220)
)
sectionTraceIdentifierMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    sectionTraceIdentifierMismatch.setStatus(
        "current"
    )

regeneratorSectionTraceIdentifierMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6230)
)
regeneratorSectionTraceIdentifierMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    regeneratorSectionTraceIdentifierMismatch.setStatus(
        "current"
    )

switchingMatrixModuleFailureWorking = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6240)
)
switchingMatrixModuleFailureWorking.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    switchingMatrixModuleFailureWorking.setStatus(
        "current"
    )

switchingMatrixModuleFailureProtect = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6250)
)
switchingMatrixModuleFailureProtect.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    switchingMatrixModuleFailureProtect.setStatus(
        "current"
    )

slotCommunicationDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6260)
)
slotCommunicationDisabled.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    slotCommunicationDisabled.setStatus(
        "current"
    )

sessionTimeLimitExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6270)
)
sessionTimeLimitExpired.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    sessionTimeLimitExpired.setStatus(
        "current"
    )

userPasswordChangeRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6280)
)
userPasswordChangeRequired.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    userPasswordChangeRequired.setStatus(
        "current"
    )

isisAdjacencyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6290)
)
isisAdjacencyFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    isisAdjacencyFailure.setStatus(
        "current"
    )

msspSoftwareVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6300)
)
msspSoftwareVersionMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    msspSoftwareVersionMismatch.setStatus(
        "current"
    )

remoteAuthenticationFailSeeAuditLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6310)
)
remoteAuthenticationFailSeeAuditLog.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    remoteAuthenticationFailSeeAuditLog.setStatus(
        "current"
    )

ringIsSquelchingStsTraffic = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6330)
)
ringIsSquelchingStsTraffic.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ringIsSquelchingStsTraffic.setStatus(
        "current"
    )

ringIsSquelchingVtTraffic = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6340)
)
ringIsSquelchingVtTraffic.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ringIsSquelchingVtTraffic.setStatus(
        "current"
    )

archiveOfAuditLogFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6350)
)
archiveOfAuditLogFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    archiveOfAuditLogFailed.setStatus(
        "current"
    )

rprWrapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6360)
)
rprWrapped.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rprWrapped.setStatus(
        "current"
    )

shelfCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6370)
)
shelfCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    shelfCommunicationFailure.setStatus(
        "current"
    )

duplicatedShelfIdentifier = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6380)
)
duplicatedShelfIdentifier.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    duplicatedShelfIdentifier.setStatus(
        "current"
    )

softwareMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6390)
)
softwareMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    softwareMismatch.setStatus(
        "current"
    )

lmpFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6400)
)
lmpFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lmpFailure.setStatus(
        "current"
    )

opticalTerminationIncomplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6410)
)
opticalTerminationIncomplete.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalTerminationIncomplete.setStatus(
        "current"
    )

forwardDefectIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6420)
)
forwardDefectIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    forwardDefectIndication.setStatus(
        "current"
    )

payloadMissingIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6430)
)
payloadMissingIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadMissingIndication.setStatus(
        "current"
    )

spanMeasurementCannotBePerformed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6440)
)
spanMeasurementCannotBePerformed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    spanMeasurementCannotBePerformed.setStatus(
        "current"
    )

ringIsSquelchingHighOrderTraffic = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6450)
)
ringIsSquelchingHighOrderTraffic.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ringIsSquelchingHighOrderTraffic.setStatus(
        "current"
    )

ringIsSquelchingLowOrderTraffic = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6460)
)
ringIsSquelchingLowOrderTraffic.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ringIsSquelchingLowOrderTraffic.setStatus(
        "current"
    )

badPacketCountExceedsThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6470)
)
badPacketCountExceedsThreshold.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    badPacketCountExceedsThreshold.setStatus(
        "current"
    )

linkLayerKeepAliveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6480)
)
linkLayerKeepAliveFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    linkLayerKeepAliveFailure.setStatus(
        "current"
    )

autonegotiationRemoteFailureIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6490)
)
autonegotiationRemoteFailureIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    autonegotiationRemoteFailureIndication.setStatus(
        "current"
    )

trailSignalFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6500)
)
trailSignalFail.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    trailSignalFail.setStatus(
        "current"
    )

ds1LoopbackCommandSentToFarEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6510)
)
ds1LoopbackCommandSentToFarEnd.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ds1LoopbackCommandSentToFarEnd.setStatus(
        "current"
    )

multiplexSectionSignalDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6520)
)
multiplexSectionSignalDegraded.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    multiplexSectionSignalDegraded.setStatus(
        "current"
    )

multiplexSectionExcessiveErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6530)
)
multiplexSectionExcessiveErrors.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    multiplexSectionExcessiveErrors.setStatus(
        "current"
    )

highOrderPathSignalDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6540)
)
highOrderPathSignalDegraded.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    highOrderPathSignalDegraded.setStatus(
        "current"
    )

highOrderPathExcessiveErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6550)
)
highOrderPathExcessiveErrors.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    highOrderPathExcessiveErrors.setStatus(
        "current"
    )

lowOrderPathSignalDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6560)
)
lowOrderPathSignalDegraded.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lowOrderPathSignalDegraded.setStatus(
        "current"
    )

lowOrderPathExcessiveErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6570)
)
lowOrderPathExcessiveErrors.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lowOrderPathExcessiveErrors.setStatus(
        "current"
    )

regeneratorSectionDccTerminationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6580)
)
regeneratorSectionDccTerminationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    regeneratorSectionDccTerminationFailure.setStatus(
        "current"
    )

networkMemoryPoolLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6590)
)
networkMemoryPoolLow.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    networkMemoryPoolLow.setStatus(
        "current"
    )

ospfRoutingTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6600)
)
ospfRoutingTableOverflow.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ospfRoutingTableOverflow.setStatus(
        "current"
    )

autoLaserShutdownDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6610)
)
autoLaserShutdownDisabled.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    autoLaserShutdownDisabled.setStatus(
        "current"
    )

rprProtectionIsActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6630)
)
rprProtectionIsActive.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rprProtectionIsActive.setStatus(
        "current"
    )

maxRPRStationNumberExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6640)
)
maxRPRStationNumberExceeded.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    maxRPRStationNumberExceeded.setStatus(
        "current"
    )

rprProtectionConfigurationMismatched = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6650)
)
rprProtectionConfigurationMismatched.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rprProtectionConfigurationMismatched.setStatus(
        "current"
    )

reservedBandwidthLinkRateExceededOnRinglet0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6660)
)
reservedBandwidthLinkRateExceededOnRinglet0.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    reservedBandwidthLinkRateExceededOnRinglet0.setStatus(
        "current"
    )

reservedBandwidthLinkRateExceededOnRinglet1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6670)
)
reservedBandwidthLinkRateExceededOnRinglet1.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    reservedBandwidthLinkRateExceededOnRinglet1.setStatus(
        "current"
    )

rprInterfaceInPassThroughMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6680)
)
rprInterfaceInPassThroughMode.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rprInterfaceInPassThroughMode.setStatus(
        "current"
    )

rprPeerNodeIsMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6690)
)
rprPeerNodeIsMissing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rprPeerNodeIsMissing.setStatus(
        "current"
    )

rprRiFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6700)
)
rprRiFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rprRiFailure.setStatus(
        "current"
    )

rprSignalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6710)
)
rprSignalFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rprSignalFailure.setStatus(
        "current"
    )

rprSignalDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6720)
)
rprSignalDegrade.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rprSignalDegrade.setStatus(
        "current"
    )

interlinkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6730)
)
interlinkFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    interlinkFailure.setStatus(
        "current"
    )

apcWrongGain = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6740)
)
apcWrongGain.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    apcWrongGain.setStatus(
        "current"
    )

rprSpanMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6750)
)
rprSpanMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rprSpanMismatch.setStatus(
        "current"
    )

efmRemoteFaultIndicationCriticalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6760)
)
efmRemoteFaultIndicationCriticalEvent.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    efmRemoteFaultIndicationCriticalEvent.setStatus(
        "current"
    )

efmRemoteFaultIndicationDyingGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6770)
)
efmRemoteFaultIndicationDyingGasp.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    efmRemoteFaultIndicationDyingGasp.setStatus(
        "current"
    )

efmRemoteFaultIndicationLinkFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6780)
)
efmRemoteFaultIndicationLinkFault.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    efmRemoteFaultIndicationLinkFault.setStatus(
        "current"
    )

efmLinkMonitoringErroredSymbolPeriodEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6790)
)
efmLinkMonitoringErroredSymbolPeriodEvent.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    efmLinkMonitoringErroredSymbolPeriodEvent.setStatus(
        "current"
    )

efmLinkMonitoringErroredFrameEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6800)
)
efmLinkMonitoringErroredFrameEvent.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    efmLinkMonitoringErroredFrameEvent.setStatus(
        "current"
    )

efmLinkMonitoringErroredFramePeriodEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6810)
)
efmLinkMonitoringErroredFramePeriodEvent.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    efmLinkMonitoringErroredFramePeriodEvent.setStatus(
        "current"
    )

efmLinkMonitoringErroredFrameSecondsSummary = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6820)
)
efmLinkMonitoringErroredFrameSecondsSummary.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    efmLinkMonitoringErroredFrameSecondsSummary.setStatus(
        "current"
    )

efmRemoteLoopbackRequestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6830)
)
efmRemoteLoopbackRequestFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    efmRemoteLoopbackRequestFailed.setStatus(
        "current"
    )

fastAutomaticProtectionSwitching = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6840)
)
fastAutomaticProtectionSwitching.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    fastAutomaticProtectionSwitching.setStatus(
        "current"
    )

fastAutomaticProtectionSwitchingConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6850)
)
fastAutomaticProtectionSwitchingConfigMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    fastAutomaticProtectionSwitchingConfigMismatch.setStatus(
        "current"
    )

lcasSinkGroupError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6860)
)
lcasSinkGroupError.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lcasSinkGroupError.setStatus(
        "current"
    )

lcasVcgMemberRxSideInDnuState = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6870)
)
lcasVcgMemberRxSideInDnuState.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lcasVcgMemberRxSideInDnuState.setStatus(
        "current"
    )

fcDistanceExtFuncNotEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6880)
)
fcDistanceExtFuncNotEstablished.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    fcDistanceExtFuncNotEstablished.setStatus(
        "current"
    )

nonCiscoPPMInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6890)
)
nonCiscoPPMInserted.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    nonCiscoPPMInserted.setStatus(
        "current"
    )

unqualifiedPPMInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6900)
)
unqualifiedPPMInserted.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    unqualifiedPPMInserted.setStatus(
        "current"
    )

ftaMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6910)
)
ftaMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ftaMismatch.setStatus(
        "current"
    )

cardPortsUnableToProvideProtection = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6920)
)
cardPortsUnableToProvideProtection.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    cardPortsUnableToProvideProtection.setStatus(
        "current"
    )

lmpSignalDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6930)
)
lmpSignalDegrade.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lmpSignalDegrade.setStatus(
        "current"
    )

lmpSignalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6940)
)
lmpSignalFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lmpSignalFailure.setStatus(
        "current"
    )

lmpUnallocatedDataLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6950)
)
lmpUnallocatedDataLink.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lmpUnallocatedDataLink.setStatus(
        "current"
    )

frontPortLinkLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6960)
)
frontPortLinkLoss.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    frontPortLinkLoss.setStatus(
        "current"
    )

bertEnbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6970)
)
bertEnbl.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    bertEnbl.setStatus(
        "current"
    )

bertSyncFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6975)
)
bertSyncFail.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    bertSyncFail.setStatus(
        "current"
    )

workQueueFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 6980)
)
workQueueFull.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workQueueFull.setStatus(
        "current"
    )

equipmentPowerFailureAtConnectorA = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7000)
)
equipmentPowerFailureAtConnectorA.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentPowerFailureAtConnectorA.setStatus(
        "current"
    )

equipmentPowerFailureAtConnectorB = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7005)
)
equipmentPowerFailureAtConnectorB.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentPowerFailureAtConnectorB.setStatus(
        "current"
    )

equipmentPowerFailureAtReturnConnectorA = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7010)
)
equipmentPowerFailureAtReturnConnectorA.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentPowerFailureAtReturnConnectorA.setStatus(
        "current"
    )

equipmentPowerFailureAtReturnConnectorB = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7015)
)
equipmentPowerFailureAtReturnConnectorB.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    equipmentPowerFailureAtReturnConnectorB.setStatus(
        "current"
    )

bridgeAndRollHasOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7055)
)
bridgeAndRollHasOccurred.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    bridgeAndRollHasOccurred.setStatus(
        "current"
    )

bridgeAndRollIsPendingAValidSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7060)
)
bridgeAndRollIsPendingAValidSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    bridgeAndRollIsPendingAValidSignal.setStatus(
        "current"
    )

clockBusFailureTscA = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7160)
)
clockBusFailureTscA.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    clockBusFailureTscA.setStatus(
        "current"
    )

clockBusFailureTscB = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7165)
)
clockBusFailureTscB.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    clockBusFailureTscB.setStatus(
        "current"
    )

ospfHelloFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7185)
)
ospfHelloFail.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ospfHelloFail.setStatus(
        "current"
    )

openIOSlots = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7200)
)
openIOSlots.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    openIOSlots.setStatus(
        "current"
    )

lossOfClockFromMateShelfController = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7210)
)
lossOfClockFromMateShelfController.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lossOfClockFromMateShelfController.setStatus(
        "current"
    )

virtualLanAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7225)
)
virtualLanAlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    virtualLanAlarmIndicationSignal.setStatus(
        "current"
    )

dcuLossFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7230)
)
dcuLossFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    dcuLossFailure.setStatus(
        "current"
    )

ochncMaintenance = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7235)
)
ochncMaintenance.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ochncMaintenance.setStatus(
        "current"
    )

ramanLaserShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7240)
)
ramanLaserShutdown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ramanLaserShutdown.setStatus(
        "current"
    )

losOfRamanSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7245)
)
losOfRamanSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    losOfRamanSignal.setStatus(
        "current"
    )

mcastMacTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7250)
)
mcastMacTableFull.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    mcastMacTableFull.setStatus(
        "current"
    )

multicastMacAddressAliasing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7255)
)
multicastMacAddressAliasing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    multicastMacAddressAliasing.setStatus(
        "current"
    )

ramanPwrProtOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7260)
)
ramanPwrProtOn.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ramanPwrProtOn.setStatus(
        "current"
    )

cppPeerNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7265)
)
cppPeerNotResponding.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    cppPeerNotResponding.setStatus(
        "current"
    )

voaControlLoopDisableDueToExcessiveCounterPropagationLight = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7275)
)
voaControlLoopDisableDueToExcessiveCounterPropagationLight.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    voaControlLoopDisableDueToExcessiveCounterPropagationLight.setStatus(
        "current"
    )

wizardIsRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7280)
)
wizardIsRunning.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    wizardIsRunning.setStatus(
        "current"
    )

ramanGainNotReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7285)
)
ramanGainNotReached.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ramanGainNotReached.setStatus(
        "current"
    )

pprForwardDefectIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7295)
)
pprForwardDefectIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    pprForwardDefectIndication.setStatus(
        "current"
    )

pprBackwardDefectIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7300)
)
pprBackwardDefectIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    pprBackwardDefectIndication.setStatus(
        "current"
    )

pprCoordinatedMaintenance = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7305)
)
pprCoordinatedMaintenance.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    pprCoordinatedMaintenance.setStatus(
        "current"
    )

pprTriggerThresholdBERExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7310)
)
pprTriggerThresholdBERExceeded.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    pprTriggerThresholdBERExceeded.setStatus(
        "current"
    )

localFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7315)
)
localFault.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    localFault.setStatus(
        "current"
    )

remoteFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7320)
)
remoteFault.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    remoteFault.setStatus(
        "current"
    )

efmRemoteLoopbackConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7325)
)
efmRemoteLoopbackConfigured.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    efmRemoteLoopbackConfigured.setStatus(
        "current"
    )

efmPeerMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7330)
)
efmPeerMissing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    efmPeerMissing.setStatus(
        "current"
    )

eqptDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7335)
)
eqptDegrade.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    eqptDegrade.setStatus(
        "current"
    )

excessiveBackPropagation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7340)
)
excessiveBackPropagation.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    excessiveBackPropagation.setStatus(
        "current"
    )

remoteMaintenanceEndPointIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7345)
)
remoteMaintenanceEndPointIsDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    remoteMaintenanceEndPointIsDown.setStatus(
        "current"
    )

crossConnectedCFMService = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7350)
)
crossConnectedCFMService.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    crossConnectedCFMService.setStatus(
        "current"
    )

cfmLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7355)
)
cfmLoop.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    cfmLoop.setStatus(
        "current"
    )

cfmConfigurationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7360)
)
cfmConfigurationError.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    cfmConfigurationError.setStatus(
        "current"
    )

outOfChannelGroupBundle = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7365)
)
outOfChannelGroupBundle.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    outOfChannelGroupBundle.setStatus(
        "current"
    )

repNeighborAdjacencyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7370)
)
repNeighborAdjacencyFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    repNeighborAdjacencyFailure.setStatus(
        "current"
    )

repLinkFlapping = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7375)
)
repLinkFlapping.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    repLinkFlapping.setStatus(
        "current"
    )

faultInREPSegment = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7380)
)
faultInREPSegment.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    faultInREPSegment.setStatus(
        "current"
    )

primaryREPEdgePortElected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7385)
)
primaryREPEdgePortElected.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    primaryREPEdgePortElected.setStatus(
        "current"
    )

secondaryREPEdgePortElected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7390)
)
secondaryREPEdgePortElected.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    secondaryREPEdgePortElected.setStatus(
        "current"
    )

stcnREPGenerated = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7395)
)
stcnREPGenerated.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    stcnREPGenerated.setStatus(
        "current"
    )

vlbREPActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7400)
)
vlbREPActivated.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    vlbREPActivated.setStatus(
        "current"
    )

vlbREPTriggerSoakingDelayActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7405)
)
vlbREPTriggerSoakingDelayActive.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    vlbREPTriggerSoakingDelayActive.setStatus(
        "current"
    )

wanSyncloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7410)
)
wanSyncloss.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    wanSyncloss.setStatus(
        "current"
    )

laserShutdownDueToWavelengthDrift = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7415)
)
laserShutdownDueToWavelengthDrift.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    laserShutdownDueToWavelengthDrift.setStatus(
        "current"
    )

manualLaserRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7420)
)
manualLaserRestart.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    manualLaserRestart.setStatus(
        "current"
    )

laserShutdownDueToNonCiscoPPMInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7425)
)
laserShutdownDueToNonCiscoPPMInserted.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    laserShutdownDueToNonCiscoPPMInserted.setStatus(
        "current"
    )

ethernetOSCTerminationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7430)
)
ethernetOSCTerminationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ethernetOSCTerminationFailure.setStatus(
        "current"
    )

softwareSignatureVerificationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7445)
)
softwareSignatureVerificationFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    softwareSignatureVerificationFailed.setStatus(
        "current"
    )

protectVolumeSoftwareSignatureVerificationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7450)
)
protectVolumeSoftwareSignatureVerificationFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectVolumeSoftwareSignatureVerificationFailed.setStatus(
        "current"
    )

activeVolumeSoftwareSignatureVerificationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7455)
)
activeVolumeSoftwareSignatureVerificationFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    activeVolumeSoftwareSignatureVerificationFailed.setStatus(
        "current"
    )

peerPortClientSignalFailDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7460)
)
peerPortClientSignalFailDetected.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    peerPortClientSignalFailDetected.setStatus(
        "current"
    )

channelShutdownDueToWavelengthDrift = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7465)
)
channelShutdownDueToWavelengthDrift.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    channelShutdownDueToWavelengthDrift.setStatus(
        "current"
    )

usbWriteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7475)
)
usbWriteFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    usbWriteFailure.setStatus(
        "current"
    )

usbSyncInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7480)
)
usbSyncInProgress.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    usbSyncInProgress.setStatus(
        "current"
    )

autoSensingUnableToDetectValidPayload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7485)
)
autoSensingUnableToDetectValidPayload.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    autoSensingUnableToDetectValidPayload.setStatus(
        "current"
    )

payloadAutoSensingInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7490)
)
payloadAutoSensingInProgress.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    payloadAutoSensingInProgress.setStatus(
        "current"
    )

gfpClientSignalFailDetectedDueToSigloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7495)
)
gfpClientSignalFailDetectedDueToSigloss.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    gfpClientSignalFailDetectedDueToSigloss.setStatus(
        "current"
    )

gfpClientSignalFailDetectedDueToSyncloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7500)
)
gfpClientSignalFailDetectedDueToSyncloss.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    gfpClientSignalFailDetectedDueToSyncloss.setStatus(
        "current"
    )

pmdDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7510)
)
pmdDegrade.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    pmdDegrade.setStatus(
        "current"
    )

standbyTccNEClockIsInternalClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7515)
)
standbyTccNEClockIsInternalClock.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    standbyTccNEClockIsInternalClock.setStatus(
        "current"
    )

chromaticDispersionValue = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7520)
)
chromaticDispersionValue.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    chromaticDispersionValue.setStatus(
        "current"
    )

packetTransportServiceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7525)
)
packetTransportServiceFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    packetTransportServiceFailed.setStatus(
        "current"
    )

satellitePanelDiscoveryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7530)
)
satellitePanelDiscoveryFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    satellitePanelDiscoveryFailure.setStatus(
        "current"
    )

satellitePanelActiveLinkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7535)
)
satellitePanelActiveLinkFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    satellitePanelActiveLinkFailure.setStatus(
        "current"
    )

satellitePanelCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7540)
)
satellitePanelCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    satellitePanelCommunicationFailure.setStatus(
        "current"
    )

satellitePanelImproperConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7545)
)
satellitePanelImproperConfiguration.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    satellitePanelImproperConfiguration.setStatus(
        "current"
    )

satellitePanelFanMismatchOfEquipmentAndAttributes = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7550)
)
satellitePanelFanMismatchOfEquipmentAndAttributes.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    satellitePanelFanMismatchOfEquipmentAndAttributes.setStatus(
        "current"
    )

satellitePanelFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7555)
)
satellitePanelFanFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    satellitePanelFanFailure.setStatus(
        "current"
    )

satellitePanelPartialFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7560)
)
satellitePanelPartialFanFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    satellitePanelPartialFanFailure.setStatus(
        "current"
    )

satellitePanelFANManufacturingDataMemoryEEPROMFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7565)
)
satellitePanelFANManufacturingDataMemoryEEPROMFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    satellitePanelFANManufacturingDataMemoryEEPROMFailure.setStatus(
        "current"
    )

satellitePanelFANUnitIsMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7570)
)
satellitePanelFANUnitIsMissing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    satellitePanelFANUnitIsMissing.setStatus(
        "current"
    )

satellitePanelIndustrialHighTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7575)
)
satellitePanelIndustrialHighTemperature.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    satellitePanelIndustrialHighTemperature.setStatus(
        "current"
    )

satellitePanelHighTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7580)
)
satellitePanelHighTemperature.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    satellitePanelHighTemperature.setStatus(
        "current"
    )

satellitePanelBatteryFailureA = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7585)
)
satellitePanelBatteryFailureA.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    satellitePanelBatteryFailureA.setStatus(
        "current"
    )

plannedSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7590)
)
plannedSwitchOver.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    plannedSwitchOver.setStatus(
        "current"
    )

protectionCardConfigurationMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7595)
)
protectionCardConfigurationMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectionCardConfigurationMismatch.setStatus(
        "current"
    )

routerProcessorSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7600)
)
routerProcessorSwitchOver.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    routerProcessorSwitchOver.setStatus(
        "current"
    )

runningLowOnResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7605)
)
runningLowOnResources.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    runningLowOnResources.setStatus(
        "current"
    )

noMoreResourcesAreAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7610)
)
noMoreResourcesAreAvailable.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    noMoreResourcesAreAvailable.setStatus(
        "current"
    )

esmcFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7615)
)
esmcFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    esmcFailure.setStatus(
        "current"
    )

licenseWillExpireWithin24Hours = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7620)
)
licenseWillExpireWithin24Hours.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    licenseWillExpireWithin24Hours.setStatus(
        "current"
    )

licenseWillExpireAnytimeAfter1DayButBefore14Days = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7625)
)
licenseWillExpireAnytimeAfter1DayButBefore14Days.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    licenseWillExpireAnytimeAfter1DayButBefore14Days.setStatus(
        "current"
    )

licenseIsExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7630)
)
licenseIsExpired.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    licenseIsExpired.setStatus(
        "current"
    )

licenseCountViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7635)
)
licenseCountViolation.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    licenseCountViolation.setStatus(
        "current"
    )

temporaryLicenseIsInUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7640)
)
temporaryLicenseIsInUse.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    temporaryLicenseIsInUse.setStatus(
        "current"
    )

evaluationLicenseIsInUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7645)
)
evaluationLicenseIsInUse.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    evaluationLicenseIsInUse.setStatus(
        "current"
    )

licenseIsMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7650)
)
licenseIsMissing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    licenseIsMissing.setStatus(
        "current"
    )

pseudowireDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7655)
)
pseudowireDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    pseudowireDown.setStatus(
        "current"
    )

workingPseudowireControlPlaneDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7660)
)
workingPseudowireControlPlaneDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingPseudowireControlPlaneDown.setStatus(
        "current"
    )

protectPseudowireControlPlaneDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7665)
)
protectPseudowireControlPlaneDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectPseudowireControlPlaneDown.setStatus(
        "current"
    )

workingPseudowireConnectivityCheckDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7670)
)
workingPseudowireConnectivityCheckDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingPseudowireConnectivityCheckDown.setStatus(
        "current"
    )

protectPseudowireConnectivityCheckDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7675)
)
protectPseudowireConnectivityCheckDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectPseudowireConnectivityCheckDown.setStatus(
        "current"
    )

pseudowireTrafficSwitchedToProtection = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7680)
)
pseudowireTrafficSwitchedToProtection.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    pseudowireTrafficSwitchedToProtection.setStatus(
        "current"
    )

workingPseudowireLocalAcTxPortFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7685)
)
workingPseudowireLocalAcTxPortFault.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingPseudowireLocalAcTxPortFault.setStatus(
        "current"
    )

protectPseudowireLocalAcTxPortFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7690)
)
protectPseudowireLocalAcTxPortFault.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectPseudowireLocalAcTxPortFault.setStatus(
        "current"
    )

workingPseudowireLocalAcRxPortFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7695)
)
workingPseudowireLocalAcRxPortFault.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingPseudowireLocalAcRxPortFault.setStatus(
        "current"
    )

protectPseudowireLocalAcRxPortFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7700)
)
protectPseudowireLocalAcRxPortFault.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectPseudowireLocalAcRxPortFault.setStatus(
        "current"
    )

workingPseudowireRemoteAcTxPortFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7705)
)
workingPseudowireRemoteAcTxPortFault.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingPseudowireRemoteAcTxPortFault.setStatus(
        "current"
    )

protectPseudowireRemoteAcTxPortFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7710)
)
protectPseudowireRemoteAcTxPortFault.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectPseudowireRemoteAcTxPortFault.setStatus(
        "current"
    )

workingPseudowireRemoteAcRxPortFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7715)
)
workingPseudowireRemoteAcRxPortFault.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingPseudowireRemoteAcRxPortFault.setStatus(
        "current"
    )

protectPseudowireRemoteAcRxPortFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7720)
)
protectPseudowireRemoteAcRxPortFault.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectPseudowireRemoteAcRxPortFault.setStatus(
        "current"
    )

slaThresholdCrossAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7725)
)
slaThresholdCrossAlert.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    slaThresholdCrossAlert.setStatus(
        "current"
    )

protectLocalPseudowireNotForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7730)
)
protectLocalPseudowireNotForwarding.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectLocalPseudowireNotForwarding.setStatus(
        "current"
    )

workingPseudowireNotForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7735)
)
workingPseudowireNotForwarding.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingPseudowireNotForwarding.setStatus(
        "current"
    )

protectPseudowireNotForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7740)
)
protectPseudowireNotForwarding.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectPseudowireNotForwarding.setStatus(
        "current"
    )

tpTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7745)
)
tpTunnelDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tpTunnelDown.setStatus(
        "current"
    )

workingLabelSwitchedPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7750)
)
workingLabelSwitchedPathDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingLabelSwitchedPathDown.setStatus(
        "current"
    )

protectLabelSwitchedPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7755)
)
protectLabelSwitchedPathDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectLabelSwitchedPathDown.setStatus(
        "current"
    )

workingLabelSwitchedPathAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7760)
)
workingLabelSwitchedPathAlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingLabelSwitchedPathAlarmIndicationSignal.setStatus(
        "current"
    )

protectLabelSwitchedPathAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7765)
)
protectLabelSwitchedPathAlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectLabelSwitchedPathAlarmIndicationSignal.setStatus(
        "current"
    )

workingLabelSwitchedPathRemoteDefectIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7770)
)
workingLabelSwitchedPathRemoteDefectIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingLabelSwitchedPathRemoteDefectIndication.setStatus(
        "current"
    )

protectLabelSwitchedPathRemoteDefectIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7775)
)
protectLabelSwitchedPathRemoteDefectIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectLabelSwitchedPathRemoteDefectIndication.setStatus(
        "current"
    )

bidirectionalForwardDetectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7780)
)
bidirectionalForwardDetectionDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    bidirectionalForwardDetectionDown.setStatus(
        "current"
    )

tpTrafficSwitchedFromWorkingToProtection = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7785)
)
tpTrafficSwitchedFromWorkingToProtection.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    tpTrafficSwitchedFromWorkingToProtection.setStatus(
        "current"
    )

workingTpLockout = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7790)
)
workingTpLockout.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingTpLockout.setStatus(
        "current"
    )

protectTpLockout = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7795)
)
protectTpLockout.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectTpLockout.setStatus(
        "current"
    )

ethernetFlowPointFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7800)
)
ethernetFlowPointFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ethernetFlowPointFailed.setStatus(
        "current"
    )

teTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7805)
)
teTunnelDown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    teTunnelDown.setStatus(
        "current"
    )

macSystemLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7810)
)
macSystemLimitReached.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    macSystemLimitReached.setStatus(
        "current"
    )

macBridgeDomainLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7815)
)
macBridgeDomainLimitReached.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    macBridgeDomainLimitReached.setStatus(
        "current"
    )

autoSensingDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7820)
)
autoSensingDisabled.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    autoSensingDisabled.setStatus(
        "current"
    )

smBackwardIncomingAlignmentError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7825)
)
smBackwardIncomingAlignmentError.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    smBackwardIncomingAlignmentError.setStatus(
        "current"
    )

resourceAllocationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7830)
)
resourceAllocationFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    resourceAllocationFailed.setStatus(
        "current"
    )

lossOfDFBSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7835)
)
lossOfDFBSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lossOfDFBSignal.setStatus(
        "current"
    )

workingLabelSwitchedPathLinkDownIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7840)
)
workingLabelSwitchedPathLinkDownIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingLabelSwitchedPathLinkDownIndication.setStatus(
        "current"
    )

protectLabelSwitchedPathLinkDownIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7845)
)
protectLabelSwitchedPathLinkDownIndication.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectLabelSwitchedPathLinkDownIndication.setStatus(
        "current"
    )

workingLabelSwitchedPathLockReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7850)
)
workingLabelSwitchedPathLockReport.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    workingLabelSwitchedPathLockReport.setStatus(
        "current"
    )

protectLabelSwitchedPathLockReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7855)
)
protectLabelSwitchedPathLockReport.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    protectLabelSwitchedPathLockReport.setStatus(
        "current"
    )

satellitePanelBatteryFailureB = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7860)
)
satellitePanelBatteryFailureB.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    satellitePanelBatteryFailureB.setStatus(
        "current"
    )

highBitErrorRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7865)
)
highBitErrorRate.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    highBitErrorRate.setStatus(
        "current"
    )

backPanelFacilityLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7870)
)
backPanelFacilityLoopback.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    backPanelFacilityLoopback.setStatus(
        "current"
    )

backPanelTerminalLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7875)
)
backPanelTerminalLoopback.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    backPanelTerminalLoopback.setStatus(
        "current"
    )

trunkPayloadTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7880)
)
trunkPayloadTypeMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    trunkPayloadTypeMismatch.setStatus(
        "current"
    )

invalidMuxponderConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7885)
)
invalidMuxponderConfiguration.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    invalidMuxponderConfiguration.setStatus(
        "current"
    )

coolingProfileMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7890)
)
coolingProfileMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    coolingProfileMismatch.setStatus(
        "current"
    )

trunkOduAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7895)
)
trunkOduAlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    trunkOduAlarmIndicationSignal.setStatus(
        "current"
    )

companionCardMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7900)
)
companionCardMissing.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    companionCardMissing.setStatus(
        "current"
    )

controlPlaneUnverifiedClearedAlarmsPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7905)
)
controlPlaneUnverifiedClearedAlarmsPresent.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    controlPlaneUnverifiedClearedAlarmsPresent.setStatus(
        "current"
    )

powerConsumptionLimitHasCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7910)
)
powerConsumptionLimitHasCrossed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    powerConsumptionLimitHasCrossed.setStatus(
        "current"
    )

masterKeyExchangeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7915)
)
masterKeyExchangeFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    masterKeyExchangeFailed.setStatus(
        "current"
    )

unitHighTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7930)
)
unitHighTemperature.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    unitHighTemperature.setStatus(
        "current"
    )

overTemperatureUnitProtected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7935)
)
overTemperatureUnitProtected.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    overTemperatureUnitProtected.setStatus(
        "current"
    )

seqMismatchCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7945)
)
seqMismatchCount.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    seqMismatchCount.setStatus(
        "current"
    )

keyProgramOnAlteraFpgaFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7960)
)
keyProgramOnAlteraFpgaFailed.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    keyProgramOnAlteraFpgaFailed.setStatus(
        "current"
    )

duplicateNodeControllerDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7970)
)
duplicateNodeControllerDetected.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    duplicateNodeControllerDetected.setStatus(
        "current"
    )

restorationInProg = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7975)
)
restorationInProg.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    restorationInProg.setStatus(
        "current"
    )

ramanPumpsCalibrationProcedureIsRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7980)
)
ramanPumpsCalibrationProcedureIsRunning.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ramanPumpsCalibrationProcedureIsRunning.setStatus(
        "current"
    )

ramanPumpsCalibrationIsScheduledToRunInTheNextMinutes = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 7985)
)
ramanPumpsCalibrationIsScheduledToRunInTheNextMinutes.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ramanPumpsCalibrationIsScheduledToRunInTheNextMinutes.setStatus(
        "current"
    )

odukTCM1AlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13100)
)
odukTCM1AlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukTCM1AlarmIndicationSignal.setStatus(
        "current"
    )

odukTCM2AlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13105)
)
odukTCM2AlarmIndicationSignal.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukTCM2AlarmIndicationSignal.setStatus(
        "current"
    )

odukLockedDefectTCM1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13110)
)
odukLockedDefectTCM1.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukLockedDefectTCM1.setStatus(
        "current"
    )

odukLockedDefectTCM2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13115)
)
odukLockedDefectTCM2.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukLockedDefectTCM2.setStatus(
        "current"
    )

otukLossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13120)
)
otukLossOfFrame.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    otukLossOfFrame.setStatus(
        "current"
    )

odukOpenConnectionIndicationTCM1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13125)
)
odukOpenConnectionIndicationTCM1.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukOpenConnectionIndicationTCM1.setStatus(
        "current"
    )

odukOpenConnectionIndicationTCM2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13130)
)
odukOpenConnectionIndicationTCM2.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukOpenConnectionIndicationTCM2.setStatus(
        "current"
    )

odukTrailTraceIdentifierMismatchTCM1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13135)
)
odukTrailTraceIdentifierMismatchTCM1.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukTrailTraceIdentifierMismatchTCM1.setStatus(
        "current"
    )

odukTrailTraceIdentifierMismatchTCM2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13140)
)
odukTrailTraceIdentifierMismatchTCM2.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukTrailTraceIdentifierMismatchTCM2.setStatus(
        "current"
    )

odukSignalFailureTCM1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13145)
)
odukSignalFailureTCM1.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukSignalFailureTCM1.setStatus(
        "current"
    )

odukSignalFailureTCM2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13150)
)
odukSignalFailureTCM2.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukSignalFailureTCM2.setStatus(
        "current"
    )

odukSignalDegradeTCM1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13155)
)
odukSignalDegradeTCM1.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukSignalDegradeTCM1.setStatus(
        "current"
    )

odukSignalDegradeTCM2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13160)
)
odukSignalDegradeTCM2.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    odukSignalDegradeTCM2.setStatus(
        "current"
    )

lossOfChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13165)
)
lossOfChannel.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lossOfChannel.setStatus(
        "current"
    )

fecMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13170)
)
fecMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    fecMismatch.setStatus(
        "current"
    )

timSectionMonitorTraceIdentifierMismatchFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13175)
)
timSectionMonitorTraceIdentifierMismatchFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    timSectionMonitorTraceIdentifierMismatchFailure.setStatus(
        "current"
    )

automaticLaserShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13180)
)
automaticLaserShutdown.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticLaserShutdown.setStatus(
        "current"
    )

shutterInsertionLossVariationDegradeLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13200)
)
shutterInsertionLossVariationDegradeLow.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    shutterInsertionLossVariationDegradeLow.setStatus(
        "current"
    )

opticalChannelDeactivationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13205)
)
opticalChannelDeactivationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalChannelDeactivationFailure.setStatus(
        "current"
    )

shutterInsertionLossVariationDegradeHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13210)
)
shutterInsertionLossVariationDegradeHigh.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    shutterInsertionLossVariationDegradeHigh.setStatus(
        "current"
    )

networkTopologyIncomplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13215)
)
networkTopologyIncomplete.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    networkTopologyIncomplete.setStatus(
        "current"
    )

pluginModuleCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13220)
)
pluginModuleCommunicationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    pluginModuleCommunicationFailure.setStatus(
        "current"
    )

opticalNetworkTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13225)
)
opticalNetworkTypeMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalNetworkTypeMismatch.setStatus(
        "current"
    )

opticalPowerDegradeLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13230)
)
opticalPowerDegradeLow.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalPowerDegradeLow.setStatus(
        "current"
    )

automaticPowerControlFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13235)
)
automaticPowerControlFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticPowerControlFailure.setStatus(
        "current"
    )

opticalPowerDegradeHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13240)
)
opticalPowerDegradeHigh.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalPowerDegradeHigh.setStatus(
        "current"
    )

automaticPowerControlDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13245)
)
automaticPowerControlDisabled.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    automaticPowerControlDisabled.setStatus(
        "current"
    )

opticalPowerFailureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13250)
)
opticalPowerFailureLow.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalPowerFailureLow.setStatus(
        "current"
    )

ringIdMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13255)
)
ringIdMismatch.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    ringIdMismatch.setStatus(
        "current"
    )

opticalPowerFailureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13260)
)
opticalPowerFailureHigh.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalPowerFailureHigh.setStatus(
        "current"
    )

lossOfContinuity = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13270)
)
lossOfContinuity.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    lossOfContinuity.setStatus(
        "current"
    )

variableOpticalAttenuatorDegradeLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13280)
)
variableOpticalAttenuatorDegradeLow.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    variableOpticalAttenuatorDegradeLow.setStatus(
        "current"
    )

variableOpticalAttenuatorDegradeHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13290)
)
variableOpticalAttenuatorDegradeHigh.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    variableOpticalAttenuatorDegradeHigh.setStatus(
        "current"
    )

variableOpticalAttenuatorFailureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13300)
)
variableOpticalAttenuatorFailureLow.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    variableOpticalAttenuatorFailureLow.setStatus(
        "current"
    )

variableOpticalAttenuatorFailureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13310)
)
variableOpticalAttenuatorFailureHigh.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    variableOpticalAttenuatorFailureHigh.setStatus(
        "current"
    )

laserBiasDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13320)
)
laserBiasDegrade.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    laserBiasDegrade.setStatus(
        "current"
    )

laserBiasFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13330)
)
laserBiasFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    laserBiasFailure.setStatus(
        "current"
    )

laserTemperatureDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13340)
)
laserTemperatureDegrade.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    laserTemperatureDegrade.setStatus(
        "current"
    )

opticalAmplifierGainDegradeLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13350)
)
opticalAmplifierGainDegradeLow.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalAmplifierGainDegradeLow.setStatus(
        "current"
    )

opticalAmplifierGainDegradeHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13360)
)
opticalAmplifierGainDegradeHigh.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalAmplifierGainDegradeHigh.setStatus(
        "current"
    )

opticalAmplifierGainFailureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13370)
)
opticalAmplifierGainFailureLow.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalAmplifierGainFailureLow.setStatus(
        "current"
    )

opticalAmplifierGainFailureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13380)
)
opticalAmplifierGainFailureHigh.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalAmplifierGainFailureHigh.setStatus(
        "current"
    )

opticalChannelConnectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13390)
)
opticalChannelConnectionFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalChannelConnectionFailure.setStatus(
        "current"
    )

opticalChannelIncomplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13395)
)
opticalChannelIncomplete.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalChannelIncomplete.setStatus(
        "current"
    )

opticalChannelActivationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13400)
)
opticalChannelActivationFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalChannelActivationFailure.setStatus(
        "current"
    )

laserAutoPowerReduction = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13410)
)
laserAutoPowerReduction.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    laserAutoPowerReduction.setStatus(
        "current"
    )

caseTemperatureDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13420)
)
caseTemperatureDegrade.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    caseTemperatureDegrade.setStatus(
        "current"
    )

fiberTemperatureDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13430)
)
fiberTemperatureDegrade.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    fiberTemperatureDegrade.setStatus(
        "current"
    )

shutterOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13440)
)
shutterOpen.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    shutterOpen.setStatus(
        "current"
    )

awgTemperatureDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13450)
)
awgTemperatureDegrade.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    awgTemperatureDegrade.setStatus(
        "current"
    )

awgTemperatureFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13460)
)
awgTemperatureFailure.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    awgTemperatureFailure.setStatus(
        "current"
    )

awgOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13470)
)
awgOverTemperature.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    awgOverTemperature.setStatus(
        "current"
    )

opticalAmplifierInitialization = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13480)
)
opticalAmplifierInitialization.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    opticalAmplifierInitialization.setStatus(
        "current"
    )

awgWarmUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13490)
)
awgWarmUp.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    awgWarmUp.setStatus(
        "current"
    )

incSigloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13510)
)
incSigloss.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    incSigloss.setStatus(
        "current"
    )

incSyncloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13515)
)
incSyncloss.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    incSyncloss.setStatus(
        "current"
    )

incGfpOutOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13520)
)
incGfpOutOfFrame.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    incGfpOutOfFrame.setStatus(
        "current"
    )

incGfpSigLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13525)
)
incGfpSigLoss.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    incGfpSigLoss.setStatus(
        "current"
    )

incGfpSyncLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 30, 0, 13530)
)
incGfpSyncLoss.setObjects(
      *(("CERENT-454-MIB", "cerent454NodeTime"),
        ("CERENT-454-MIB", "cerent454AlarmState"),
        ("CERENT-454-MIB", "cerent454AlarmObjectType"),
        ("CERENT-454-MIB", "cerent454AlarmObjectIndex"),
        ("CERENT-454-MIB", "cerent454AlarmSlotNumber"),
        ("CERENT-454-MIB", "cerent454AlarmPortNumber"),
        ("CERENT-454-MIB", "cerent454AlarmLineNumber"),
        ("CERENT-454-MIB", "cerent454AlarmObjectName"),
        ("CERENT-454-MIB", "cerent454AlarmSeverity"),
        ("CERENT-454-MIB", "cerent454AlarmStatus"),
        ("CERENT-454-MIB", "cerent454AlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    incGfpSyncLoss.setStatus(
        "current"
    )


# Notifications groups

event454Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 10, 10, 30)
)
event454Group.setObjects(
      *(("CERENT-454-MIB", "alarmUnknown"),
        ("CERENT-454-MIB", "alarmCutoffIsInManualMode"),
        ("CERENT-454-MIB", "failureDetectedExternalToTheNE"),
        ("CERENT-454-MIB", "externalError"),
        ("CERENT-454-MIB", "excessiveSwitching"),
        ("CERENT-454-MIB", "sdccTerminationFailure"),
        ("CERENT-454-MIB", "incomingFailureCondition"),
        ("CERENT-454-MIB", "alarmIndicationSignal"),
        ("CERENT-454-MIB", "alarmIndicationSignalLine"),
        ("CERENT-454-MIB", "alarmIndicationSignalPath"),
        ("CERENT-454-MIB", "alarmIndicationSignalVT"),
        ("CERENT-454-MIB", "apsChannelFailure"),
        ("CERENT-454-MIB", "channelByteFailureAPS"),
        ("CERENT-454-MIB", "channelProtectionSwitchingChannelMatchFailureAPS"),
        ("CERENT-454-MIB", "channelAutomaticProtectionSwitchModeMismatchAPS"),
        ("CERENT-454-MIB", "farEndProtectionLineFailure"),
        ("CERENT-454-MIB", "inconsistentAPSCode"),
        ("CERENT-454-MIB", "improperAPSCode"),
        ("CERENT-454-MIB", "nodeIdMismatch"),
        ("CERENT-454-MIB", "channelDefaultKAPS"),
        ("CERENT-454-MIB", "connectionLoss"),
        ("CERENT-454-MIB", "bipolarViolation"),
        ("CERENT-454-MIB", "carrierLossOnTheLAN"),
        ("CERENT-454-MIB", "concatenationErrorSTS"),
        ("CERENT-454-MIB", "excessCollisionsOnTheLAN"),
        ("CERENT-454-MIB", "facilityFailure"),
        ("CERENT-454-MIB", "farEndAIS"),
        ("CERENT-454-MIB", "farEndMultipleDS1LOSDetectedOnDS3"),
        ("CERENT-454-MIB", "farEndDS1EqptFailNonServiceAffecting"),
        ("CERENT-454-MIB", "farEndDS1EqptFailServiceAffecting"),
        ("CERENT-454-MIB", "farEndSingleDS1LOS"),
        ("CERENT-454-MIB", "farEndDS3EqptFailNonServiceAffecting"),
        ("CERENT-454-MIB", "farEndDS3EqptFailServiceAffecting"),
        ("CERENT-454-MIB", "farEndCommonEquipmentFailureNonServiceAffecting"),
        ("CERENT-454-MIB", "farEndIDLE"),
        ("CERENT-454-MIB", "farEndLOS"),
        ("CERENT-454-MIB", "farEndLOF"),
        ("CERENT-454-MIB", "farEndBlockError"),
        ("CERENT-454-MIB", "ds3IdleCondition"),
        ("CERENT-454-MIB", "lossOfFrame"),
        ("CERENT-454-MIB", "lossOfPointer"),
        ("CERENT-454-MIB", "lossOfPointerPath"),
        ("CERENT-454-MIB", "lossOfPointerVT"),
        ("CERENT-454-MIB", "lossOfSignal"),
        ("CERENT-454-MIB", "outOfFrame"),
        ("CERENT-454-MIB", "pathSelectorFailure"),
        ("CERENT-454-MIB", "remoteAlarmIndication"),
        ("CERENT-454-MIB", "remoteFailureIndication"),
        ("CERENT-454-MIB", "remoteFailureIndicationLine"),
        ("CERENT-454-MIB", "remoteFailureIndicationPath"),
        ("CERENT-454-MIB", "remoteFailureIndicationVT"),
        ("CERENT-454-MIB", "signalDegrade"),
        ("CERENT-454-MIB", "severelyErroredFrame"),
        ("CERENT-454-MIB", "signalFailure"),
        ("CERENT-454-MIB", "signalLabelMismatchFailure"),
        ("CERENT-454-MIB", "payloadDefectIndication"),
        ("CERENT-454-MIB", "payloadDefectIndicationPath"),
        ("CERENT-454-MIB", "payloadLabelMismatchPath"),
        ("CERENT-454-MIB", "signalLabelMismatchFailurePayloadLabelMismatchVT"),
        ("CERENT-454-MIB", "unequippedPath"),
        ("CERENT-454-MIB", "signalLabelMismatchFailureUnequippedVT"),
        ("CERENT-454-MIB", "lossOfSynchronization"),
        ("CERENT-454-MIB", "outOfSynchronization"),
        ("CERENT-454-MIB", "primarySynchronizationReferenceFailure"),
        ("CERENT-454-MIB", "secondarySynchronizationReferenceFailure"),
        ("CERENT-454-MIB", "thirdSynchronizationReferenceFailure"),
        ("CERENT-454-MIB", "fourthSynchronizationReferenceFailure"),
        ("CERENT-454-MIB", "fifthSynchronizationReferenceFailure"),
        ("CERENT-454-MIB", "sixthSynchronizationReferenceFailure"),
        ("CERENT-454-MIB", "failedToReceiveSynchronizationStatusMessage"),
        ("CERENT-454-MIB", "synchronizationStatusMessagesAreDisabledOnThisInterface"),
        ("CERENT-454-MIB", "stratum1PrimaryReferenceSourceTraceable"),
        ("CERENT-454-MIB", "synchronizedTraceabilityUnknown"),
        ("CERENT-454-MIB", "stratum2Traceable"),
        ("CERENT-454-MIB", "transitNodeClockTraceable"),
        ("CERENT-454-MIB", "stratum3ETraceable"),
        ("CERENT-454-MIB", "stratum3Traceable"),
        ("CERENT-454-MIB", "sonetMinimumClockTraceable"),
        ("CERENT-454-MIB", "stratum4Traceable"),
        ("CERENT-454-MIB", "doNotUseForSynchronization"),
        ("CERENT-454-MIB", "reservedForNetworkSynchronizationUse"),
        ("CERENT-454-MIB", "outgoingFailureCondition"),
        ("CERENT-454-MIB", "remoteDefectIndicationLine"),
        ("CERENT-454-MIB", "remoteDefectIndicationPath"),
        ("CERENT-454-MIB", "freeRunningSynchronizationMode"),
        ("CERENT-454-MIB", "holdoverSynchronizationMode"),
        ("CERENT-454-MIB", "fastStartSynchronizationMode"),
        ("CERENT-454-MIB", "internalFault"),
        ("CERENT-454-MIB", "internalError"),
        ("CERENT-454-MIB", "internalMessageError"),
        ("CERENT-454-MIB", "mismatchOfEquipmentAndAttributes"),
        ("CERENT-454-MIB", "watchdogTimerTimeout"),
        ("CERENT-454-MIB", "softwareFaultOrFailure"),
        ("CERENT-454-MIB", "softwareFaultDataIntegrityFault"),
        ("CERENT-454-MIB", "programFailure"),
        ("CERENT-454-MIB", "controlEquipmentFailure"),
        ("CERENT-454-MIB", "primaryNonVolatileBackupMemoryFailure"),
        ("CERENT-454-MIB", "secondaryNonVolatileBackupMemoryFailure"),
        ("CERENT-454-MIB", "controlBusFailure"),
        ("CERENT-454-MIB", "controlBus1Failure"),
        ("CERENT-454-MIB", "controlBus2Failure"),
        ("CERENT-454-MIB", "tccAToShelfSlot1DROP1CommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot2DROP2CommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot3DROP3CommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot4DROP4CommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot5TRUNK1CommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot6TRUNK2CommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot7TCCACommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot8XCONACommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot9AICCommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot10XCONBCommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot11TCCBCommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot12TRUNK3CommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot13TRUNK4CommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot14DROP5CommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot15DROP6CommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot16DROP7CommunicationFailure"),
        ("CERENT-454-MIB", "tccAToShelfSlot17DROP8CommunicationFailure"),
        ("CERENT-454-MIB", "tccAToDCCAProcessorCommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot1DROP1CommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot2DROP2CommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot3DROP3CommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot4DROP4CommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot5TRUNK1CommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot6TRUNK2CommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot7TCCACommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot8XCONACommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot9AICCommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot10XCONBCommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot11TCCBCommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot12TRUNK3CommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot13TRUNK4CommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot14DROP5CommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot15DROP6CommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot16DROP7CommunicationFailure"),
        ("CERENT-454-MIB", "tccBToShelfSlot17DROP8CommunicationFailure"),
        ("CERENT-454-MIB", "tccBToDCCBProcessorCommunicationFailure"),
        ("CERENT-454-MIB", "controlEquipmentControlCommunicationsEquipmentFailure"),
        ("CERENT-454-MIB", "controlProcessorFailure"),
        ("CERENT-454-MIB", "workingMemoryFailure"),
        ("CERENT-454-MIB", "interconnectionEquipmentFailure"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot1XCONSlot8"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot2XCONSlot8"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot3XCONSlot8"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot4XCONSlot8"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot5XCONSlot8"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot6XCONSlot8"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot12XCONSlot8"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot13XCONSlot8"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot14XCONSlot8"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot15XCONSlot8"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot16XCONSlot8"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot17XCONSlot8"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot1XCONSlot10"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot2XCONSlot10"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot3XCONSlot10"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot4XCONSlot10"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot5XCONSlot10"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot6XCONSlot10"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot12XCONSlot10"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot13XCONSlot10"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot14XCONSlot10"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot15XCONSlot10"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot16XCONSlot10"),
        ("CERENT-454-MIB", "payloadBusFailureToIOSlot17XCONSlot10"),
        ("CERENT-454-MIB", "timeSlotInterchangeEquipmentFailure"),
        ("CERENT-454-MIB", "equipmentFailure"),
        ("CERENT-454-MIB", "highTemperature"),
        ("CERENT-454-MIB", "invalidMACAddress"),
        ("CERENT-454-MIB", "boardFailure"),
        ("CERENT-454-MIB", "diagnosticFailure"),
        ("CERENT-454-MIB", "mediumAccessControlFailure"),
        ("CERENT-454-MIB", "facilityTerminationEquipmentFailure"),
        ("CERENT-454-MIB", "automaticLaserShutoffDueToHighTemperature"),
        ("CERENT-454-MIB", "failureToReleaseFromProtection"),
        ("CERENT-454-MIB", "receiverFailure"),
        ("CERENT-454-MIB", "transmitFailure"),
        ("CERENT-454-MIB", "facilityTerminationEquipmentReceiverMissing"),
        ("CERENT-454-MIB", "facilityTerminationEquipmentTransmitterMissing"),
        ("CERENT-454-MIB", "failureToSwitchToProtection"),
        ("CERENT-454-MIB", "failureToSwitchToProtectionRing"),
        ("CERENT-454-MIB", "failureToSwitchToProtectionSpan"),
        ("CERENT-454-MIB", "failureToSwitchToProtectionPath"),
        ("CERENT-454-MIB", "fanFailure"),
        ("CERENT-454-MIB", "equipmentUnitPlugIn"),
        ("CERENT-454-MIB", "nePowerFailureAtConnector"),
        ("CERENT-454-MIB", "fuseAlarm"),
        ("CERENT-454-MIB", "synchronizationUnitFailure"),
        ("CERENT-454-MIB", "synchronizationSwitchingEquipmentFailure"),
        ("CERENT-454-MIB", "equipmentUnitUnplugged"),
        ("CERENT-454-MIB", "loopback"),
        ("CERENT-454-MIB", "ds1LoopbackDueToFEACCommand"),
        ("CERENT-454-MIB", "loopbackCommandSentToFarEndDS1"),
        ("CERENT-454-MIB", "ds3LoopbackDueToFEACCommand"),
        ("CERENT-454-MIB", "ds3LoopbackCommandSentToFarEnd"),
        ("CERENT-454-MIB", "ds2LoopbackDueToFarEndCommand"),
        ("CERENT-454-MIB", "ds2LoopbackCommandSentToFarEnd"),
        ("CERENT-454-MIB", "facilityLoopback"),
        ("CERENT-454-MIB", "networkLoopback"),
        ("CERENT-454-MIB", "terminalLoopback"),
        ("CERENT-454-MIB", "manuallyCausedAbnormalCondition"),
        ("CERENT-454-MIB", "ethernetBridgeIsNewRootOfSpanningTree"),
        ("CERENT-454-MIB", "ethernetBridgeTopologyChange"),
        ("CERENT-454-MIB", "normalCondition"),
        ("CERENT-454-MIB", "embeddedOperationsChannelFailureLinkDown"),
        ("CERENT-454-MIB", "peerStateMismatch"),
        ("CERENT-454-MIB", "proceduralError"),
        ("CERENT-454-MIB", "improperRemoval"),
        ("CERENT-454-MIB", "duplicateNodeID"),
        ("CERENT-454-MIB", "blsrOutOfSync"),
        ("CERENT-454-MIB", "blsrMultiNodeTableUpdateCompleted"),
        ("CERENT-454-MIB", "protectionUnitNotAvailable"),
        ("CERENT-454-MIB", "performanceMonitorThresholdCrossingAlert"),
        ("CERENT-454-MIB", "protectionSwitch"),
        ("CERENT-454-MIB", "recoveryOrServiceProtectionActionHasBeenInitiated"),
        ("CERENT-454-MIB", "automaticSystemReset"),
        ("CERENT-454-MIB", "automaticUPSRSwitchCausedByAIS"),
        ("CERENT-454-MIB", "automaticUPSRSwitchCausedByLOP"),
        ("CERENT-454-MIB", "automaticUPSRSwitchCausedByUNEQ"),
        ("CERENT-454-MIB", "automaticUPSRSwitchCausedByPDI"),
        ("CERENT-454-MIB", "automaticUPSRSwitchCausedBySFBER"),
        ("CERENT-454-MIB", "automaticUPSRSwitchCausedBySDBER"),
        ("CERENT-454-MIB", "coldRestart"),
        ("CERENT-454-MIB", "forcedSwitchBackToWorking"),
        ("CERENT-454-MIB", "forcedSwitchBackToWorkingRing"),
        ("CERENT-454-MIB", "forcedSwitchBackToWorkingSpan"),
        ("CERENT-454-MIB", "forcedSwitchToProtection"),
        ("CERENT-454-MIB", "forcedSwitchToProtectionRing"),
        ("CERENT-454-MIB", "forcedSwitchToProtectionSpan"),
        ("CERENT-454-MIB", "workingFacilityOrEquipmentForcedToSwitchToProtectionPath"),
        ("CERENT-454-MIB", "initializationInitiated"),
        ("CERENT-454-MIB", "lockoutOfProtection"),
        ("CERENT-454-MIB", "lockoutOfProtectionRing"),
        ("CERENT-454-MIB", "lockoutOfProtectionSpan"),
        ("CERENT-454-MIB", "lockoutOfProtectionPath"),
        ("CERENT-454-MIB", "lockoutOfWorking"),
        ("CERENT-454-MIB", "lockoutOfWorkingRing"),
        ("CERENT-454-MIB", "lockoutOfWorkingSpan"),
        ("CERENT-454-MIB", "manualSystemReset"),
        ("CERENT-454-MIB", "manualSwitchToInternalClock"),
        ("CERENT-454-MIB", "manualSwitchToPrimaryReference"),
        ("CERENT-454-MIB", "manualSwitchToSecondReference"),
        ("CERENT-454-MIB", "manualSwitchToThirdReference"),
        ("CERENT-454-MIB", "manualSwitchToFourthReference"),
        ("CERENT-454-MIB", "manualSwitchToFifthReference"),
        ("CERENT-454-MIB", "manualSwitchToSixthReference"),
        ("CERENT-454-MIB", "manualSwitchBackToWorking"),
        ("CERENT-454-MIB", "manualSwitchBackToWorkingRing"),
        ("CERENT-454-MIB", "manualSwitchBackToWorkingSpan"),
        ("CERENT-454-MIB", "manualSwitchToProtection"),
        ("CERENT-454-MIB", "manualSwitchToProtectionRing"),
        ("CERENT-454-MIB", "manualSwitchToProtectionSpan"),
        ("CERENT-454-MIB", "manualSwitchOfWorkingFacilityOrEquipmentToProtectionPath"),
        ("CERENT-454-MIB", "powerfailRestart"),
        ("CERENT-454-MIB", "ringIsSquelchingTraffic"),
        ("CERENT-454-MIB", "softwareDownloadInProgress"),
        ("CERENT-454-MIB", "switchToInternalClock"),
        ("CERENT-454-MIB", "switchToPrimaryReference"),
        ("CERENT-454-MIB", "switchToSecondReference"),
        ("CERENT-454-MIB", "switchToThirdReference"),
        ("CERENT-454-MIB", "switchToFourthReference"),
        ("CERENT-454-MIB", "switchToFifthReference"),
        ("CERENT-454-MIB", "switchToSixthReference"),
        ("CERENT-454-MIB", "systemReboot"),
        ("CERENT-454-MIB", "switchedBackToWorking"),
        ("CERENT-454-MIB", "switchedToProtection"),
        ("CERENT-454-MIB", "warmRestart"),
        ("CERENT-454-MIB", "ringIsInWaitToRestoreState"),
        ("CERENT-454-MIB", "manualSwitchRequest"),
        ("CERENT-454-MIB", "forcedSwitchRequest"),
        ("CERENT-454-MIB", "lockoutSwitchRequest"),
        ("CERENT-454-MIB", "rmonHistoriesAndAlarmsResetReboot"),
        ("CERENT-454-MIB", "rmonThresholdCrossingAlarm"),
        ("CERENT-454-MIB", "alarmsSuppressedByUserCommand"),
        ("CERENT-454-MIB", "alarmsSuppressedForMaintenance"),
        ("CERENT-454-MIB", "switchingMatrixModuleFailure"),
        ("CERENT-454-MIB", "lanConnectionPolarityReversed"),
        ("CERENT-454-MIB", "autonomousPMReportMessageInhibited"),
        ("CERENT-454-MIB", "ioSlotToXCONCommunicationFailure"),
        ("CERENT-454-MIB", "stsPathTraceIdentifierMismatch"),
        ("CERENT-454-MIB", "nePowerFailureAtConnectorA"),
        ("CERENT-454-MIB", "nePowerFailureAtConnectorB"),
        ("CERENT-454-MIB", "freeMemoryOnCardVeryLow"),
        ("CERENT-454-MIB", "freeMemoryOnCardNearZero"),
        ("CERENT-454-MIB", "exerciseRequestOnRing"),
        ("CERENT-454-MIB", "exerciseRequestOnSpan"),
        ("CERENT-454-MIB", "squelchingPath"),
        ("CERENT-454-MIB", "extraTrafficPreempted"),
        ("CERENT-454-MIB", "farEndLockoutOfWorkingRing"),
        ("CERENT-454-MIB", "farEndLockoutOfWorkingSpan"),
        ("CERENT-454-MIB", "farEndLockoutOfProtectionRing"),
        ("CERENT-454-MIB", "farEndLockoutOfProtectionAllSpans"),
        ("CERENT-454-MIB", "farEndWorkingFacilityForcedToSwitchToProtectionRing"),
        ("CERENT-454-MIB", "farEndWorkingFacilityForcedToSwitchToProtectionSpan"),
        ("CERENT-454-MIB", "farEndManualSwitchOfWorkingFacilityToProtectionRing"),
        ("CERENT-454-MIB", "farEndManualSwitchOfWorkingFacilityToProtectionSpan"),
        ("CERENT-454-MIB", "farEndExercisingRing"),
        ("CERENT-454-MIB", "farEndExercisingSpan"),
        ("CERENT-454-MIB", "farEndBERThresholdPassedForSignalFailureRing"),
        ("CERENT-454-MIB", "farEndBERThresholdPassedForSignalFailureSpan"),
        ("CERENT-454-MIB", "farEndBERThresholdPassedForSignalDegradeRing"),
        ("CERENT-454-MIB", "farEndBERThresholdPassedForSignalDegradeSpan"),
        ("CERENT-454-MIB", "apsChannelFarEndProtectionLineSignalDegrade"),
        ("CERENT-454-MIB", "ringSwitchIsActiveOnTheEastSide"),
        ("CERENT-454-MIB", "ringSwitchIsActiveOnTheWestSide"),
        ("CERENT-454-MIB", "spanSwitchIsActiveOnTheEastSide"),
        ("CERENT-454-MIB", "spanSwitchIsActiveOnTheWestSide"),
        ("CERENT-454-MIB", "uniDirectionalFullPassThroughIsActive"),
        ("CERENT-454-MIB", "biDirectionalFullPassThroughIsActive"),
        ("CERENT-454-MIB", "kBytesPassThroughIsActive"),
        ("CERENT-454-MIB", "ringIsSegmented"),
        ("CERENT-454-MIB", "ringTopologyIsUnderConstruction"),
        ("CERENT-454-MIB", "lockoutOfProtectionAllSpans"),
        ("CERENT-454-MIB", "farEndOfFiberIsProvisionedWithDifferentRingID"),
        ("CERENT-454-MIB", "bothEndsOfFiberProvisionedAsEastOrBothAsWest"),
        ("CERENT-454-MIB", "autonomousMessagesInhibited"),
        ("CERENT-454-MIB", "trafficStormOnLANLANTemporarilyDisabled"),
        ("CERENT-454-MIB", "reptdbchgMessagesInhibited"),
        ("CERENT-454-MIB", "securityUserIDHasExpired"),
        ("CERENT-454-MIB", "partialFanFailure"),
        ("CERENT-454-MIB", "forcedSwitchRequestOnRing"),
        ("CERENT-454-MIB", "forcedSwitchRequestOnSpan"),
        ("CERENT-454-MIB", "lockoutSwitchRequestOnRing"),
        ("CERENT-454-MIB", "lockoutSwitchRequestOnSpan"),
        ("CERENT-454-MIB", "manualSwitchRequestOnRing"),
        ("CERENT-454-MIB", "manualSwitchRequestOnSpan"),
        ("CERENT-454-MIB", "communicationFailurePeerToPeerSlotControlBusA"),
        ("CERENT-454-MIB", "communicationFailurePeerToPeerSlotControlBusB"),
        ("CERENT-454-MIB", "controllerAToShelfSlotCommunicationFailure"),
        ("CERENT-454-MIB", "controllerBToShelfSlotCommunicationFailure"),
        ("CERENT-454-MIB", "interconnectionEquipmentFailureWorkingPayloadBus"),
        ("CERENT-454-MIB", "interconnectionEquipmentFailureProtectPayloadBus"),
        ("CERENT-454-MIB", "inhibitSwitchToProtectRequestOnEquipment"),
        ("CERENT-454-MIB", "inhibitSwitchToWorkingRequestOnEquipment"),
        ("CERENT-454-MIB", "exercisingRingSuccessfully"),
        ("CERENT-454-MIB", "exercisingSpanSuccessfully"),
        ("CERENT-454-MIB", "spanIsInWaitToRestoreState"),
        ("CERENT-454-MIB", "exerciseRequestOnRingFailed"),
        ("CERENT-454-MIB", "exerciseRequestOnSpanFailed"),
        ("CERENT-454-MIB", "farEndLockoutOfProtectionSpan"),
        ("CERENT-454-MIB", "manufacturingDataMemoryEEPROMFailure"),
        ("CERENT-454-MIB", "replaceableEquipmentOrUnitIsMissing"),
        ("CERENT-454-MIB", "softwareDownloadFailed"),
        ("CERENT-454-MIB", "extraTrafficPCADropped"),
        ("CERENT-454-MIB", "etherTxOversubscribed"),
        ("CERENT-454-MIB", "etherRxOverSubscribed"),
        ("CERENT-454-MIB", "etherTxExcessFlowCtrl"),
        ("CERENT-454-MIB", "etherRxExcessFlowCtrl"),
        ("CERENT-454-MIB", "transportLayerFailure"),
        ("CERENT-454-MIB", "etherTxUnderrun"),
        ("CERENT-454-MIB", "synchronizationReferenceFrequencyOutOfBounds"),
        ("CERENT-454-MIB", "ntpOrSntpHostFailure"),
        ("CERENT-454-MIB", "peerCardNotResponding"),
        ("CERENT-454-MIB", "alarmsAndEventsSuppressedForThisObject"),
        ("CERENT-454-MIB", "ds3FrameFormatMismatch"),
        ("CERENT-454-MIB", "timSectionTraceIdentifierMismatchFailure"),
        ("CERENT-454-MIB", "aisMultiplexSectionAlarmIndicationSignal"),
        ("CERENT-454-MIB", "rdiMultiplexSectionRemoteDefectOrAlarmIndication"),
        ("CERENT-454-MIB", "timHighOrderTraceIdentifierMismatchFailure"),
        ("CERENT-454-MIB", "aisAdministrationUnitAlarmIndicationSignal"),
        ("CERENT-454-MIB", "lopAdministrationUnitLossOfPointer"),
        ("CERENT-454-MIB", "slmfUnequippedHighOrderPathUnequipped"),
        ("CERENT-454-MIB", "slmfPLMHighOrderPathLabelMismatch"),
        ("CERENT-454-MIB", "rdiHighOrderRemoteDefectOrAlarmIndication"),
        ("CERENT-454-MIB", "lopTributaryUnitLossOfPointer"),
        ("CERENT-454-MIB", "aisTributaryUnitAlarmIndicationSignal"),
        ("CERENT-454-MIB", "slmfUnequippedLowOrderPathUnequipped"),
        ("CERENT-454-MIB", "slmfPLMLowOrderPathLabelMismatch"),
        ("CERENT-454-MIB", "timLowOrderTraceIdentifierMismatchFailure"),
        ("CERENT-454-MIB", "rfiLowOrderRemoteFailureOrAlarmIndication"),
        ("CERENT-454-MIB", "g811PrimaryReferenceClockTraceable"),
        ("CERENT-454-MIB", "g812TransitNodeClockTraceable"),
        ("CERENT-454-MIB", "g812LocalNodeClockTraceable"),
        ("CERENT-454-MIB", "g813SynchronousEquipmentTimingSourceTraceable"),
        ("CERENT-454-MIB", "e1LoopbackDueToFEACCommand"),
        ("CERENT-454-MIB", "e1LoopbackCommandSentToFarEnd"),
        ("CERENT-454-MIB", "e3LoopbackDueToFEACCommand"),
        ("CERENT-454-MIB", "farEndMultipleE1LOSDetectedOnE3"),
        ("CERENT-454-MIB", "farEndE1EqptFailNonServiceAffecting"),
        ("CERENT-454-MIB", "farEndE1EqptFailServiceAffecting"),
        ("CERENT-454-MIB", "farEndSingleE1LOS"),
        ("CERENT-454-MIB", "farEndE3EqptFailServiceAffecting"),
        ("CERENT-454-MIB", "e3LoopbackCommandSentToFarEnd"),
        ("CERENT-454-MIB", "farEndE3EqptFailNonServiceAffecting"),
        ("CERENT-454-MIB", "lowVoltBatteryA"),
        ("CERENT-454-MIB", "highVoltBatteryA"),
        ("CERENT-454-MIB", "lowVoltBatteryB"),
        ("CERENT-454-MIB", "highVoltBatteryB"),
        ("CERENT-454-MIB", "msspRingOutOfSync"),
        ("CERENT-454-MIB", "msspMultiNodeTableUpdateCompleted"),
        ("CERENT-454-MIB", "automaticSNCPSwitchCausedByAIS"),
        ("CERENT-454-MIB", "automaticSNCPSwitchCausedByLOP"),
        ("CERENT-454-MIB", "automaticSNCPSwitchCausedByUNEQ"),
        ("CERENT-454-MIB", "automaticSNCPSwitchCausedByPDI"),
        ("CERENT-454-MIB", "automaticSNCPSwitchCausedBySFBER"),
        ("CERENT-454-MIB", "automaticSNCPSwitchCausedBySDBER"),
        ("CERENT-454-MIB", "stmConcatenationError"),
        ("CERENT-454-MIB", "e3IdleCondition"),
        ("CERENT-454-MIB", "channelMSSPInconsistentAPSCode"),
        ("CERENT-454-MIB", "channelMSSPImproperAPSCodeAPS"),
        ("CERENT-454-MIB", "channelMSSPNodeIdMismatchAPS"),
        ("CERENT-454-MIB", "channelMSSPDefaultKAPS"),
        ("CERENT-454-MIB", "channelMSSPConnectionLossAPS"),
        ("CERENT-454-MIB", "minimumClockTraceableSDH"),
        ("CERENT-454-MIB", "lineIsInWaitToRestoreStateSDH"),
        ("CERENT-454-MIB", "berThresholdExceededForSignalDegradeHighOrder"),
        ("CERENT-454-MIB", "berThresholdExceededForSignalFailureHighOrder"),
        ("CERENT-454-MIB", "berThresholdExceededForSignalDegradeLowOrder"),
        ("CERENT-454-MIB", "berThresholdExceededForSignalFailureLowOrder"),
        ("CERENT-454-MIB", "failureToSwitchToProtectionHighOrderPath"),
        ("CERENT-454-MIB", "failureToSwitchToProtectionLowOrderPath"),
        ("CERENT-454-MIB", "a8b10bOutOfSync"),
        ("CERENT-454-MIB", "odukPMAlarmIndicationSignal"),
        ("CERENT-454-MIB", "otukAlarmIndicationSignal"),
        ("CERENT-454-MIB", "otukSMBackwardDefectIndication"),
        ("CERENT-454-MIB", "odukBackwardDefectIndication"),
        ("CERENT-454-MIB", "fecUncorrectedWord"),
        ("CERENT-454-MIB", "gccTerminationFailure"),
        ("CERENT-454-MIB", "otukIncomingAlignmentError"),
        ("CERENT-454-MIB", "odukLockedDefectPM"),
        ("CERENT-454-MIB", "lossOfMultiFrame"),
        ("CERENT-454-MIB", "odukOpenConnectionIndication"),
        ("CERENT-454-MIB", "payloadTypeIdentifierMismatch"),
        ("CERENT-454-MIB", "odukTrailTraceIdentifierMismatch"),
        ("CERENT-454-MIB", "otukTrailTraceIdentifierMismatch"),
        ("CERENT-454-MIB", "equipmentHighLaserBias"),
        ("CERENT-454-MIB", "equipmentHighLaserTemp"),
        ("CERENT-454-MIB", "equipmentHighLaserPeltier"),
        ("CERENT-454-MIB", "facilityHighRxPower"),
        ("CERENT-454-MIB", "equipmentHighTxPower"),
        ("CERENT-454-MIB", "equipmentHighTransceiverVoltage"),
        ("CERENT-454-MIB", "equipmentLowLaserBias"),
        ("CERENT-454-MIB", "equipmentLowLaserTemp"),
        ("CERENT-454-MIB", "equipmentLowLaserPeltier"),
        ("CERENT-454-MIB", "facilityLowRxPower"),
        ("CERENT-454-MIB", "equipmentLowTxPower"),
        ("CERENT-454-MIB", "equipmentLowTransceiverVoltage"),
        ("CERENT-454-MIB", "equipmentRxLocked"),
        ("CERENT-454-MIB", "equipmentSquelched"),
        ("CERENT-454-MIB", "equipmentTxLocked"),
        ("CERENT-454-MIB", "otukSignalFailure"),
        ("CERENT-454-MIB", "odukSignalFailure"),
        ("CERENT-454-MIB", "otukSignalDegrade"),
        ("CERENT-454-MIB", "odukSignalDegrade"),
        ("CERENT-454-MIB", "pluggablePortMissing"),
        ("CERENT-454-MIB", "pluggablePortRateMismatch"),
        ("CERENT-454-MIB", "pluggablePortSecurityCodeMismatch"),
        ("CERENT-454-MIB", "tciNotSelected"),
        ("CERENT-454-MIB", "tci1ClockFailure"),
        ("CERENT-454-MIB", "odukPMBackwardDefectIndication"),
        ("CERENT-454-MIB", "odukTCM1BackwardDefectIndication"),
        ("CERENT-454-MIB", "odukTCM2BackwardDefectIndication"),
        ("CERENT-454-MIB", "equipmentHighRxTemperature"),
        ("CERENT-454-MIB", "equipmentLowRxTemperature"),
        ("CERENT-454-MIB", "tci2ClockFailure"),
        ("CERENT-454-MIB", "equipmentWavelengthMismatch"),
        ("CERENT-454-MIB", "dspCommunicationFailure"),
        ("CERENT-454-MIB", "dspFailure"),
        ("CERENT-454-MIB", "laserApproachingEndOfLife"),
        ("CERENT-454-MIB", "crossconnectLoopback"),
        ("CERENT-454-MIB", "adminLogoutOfUser"),
        ("CERENT-454-MIB", "userLockedOut"),
        ("CERENT-454-MIB", "adminLockoutOfUser"),
        ("CERENT-454-MIB", "adminLockoutClear"),
        ("CERENT-454-MIB", "invalidLoginUsername"),
        ("CERENT-454-MIB", "securityInvalidLoginPassword"),
        ("CERENT-454-MIB", "securityInvalidLoginLockedOut"),
        ("CERENT-454-MIB", "securityInvalidLoginAlreadyLoggedOn"),
        ("CERENT-454-MIB", "loginOfUser"),
        ("CERENT-454-MIB", "automaticLogoutOfIdleUser"),
        ("CERENT-454-MIB", "logoutOfUser"),
        ("CERENT-454-MIB", "firewallHasBeenDisabled"),
        ("CERENT-454-MIB", "connectionEquipmentMismatch"),
        ("CERENT-454-MIB", "disableInactiveUser"),
        ("CERENT-454-MIB", "disableInactiveClear"),
        ("CERENT-454-MIB", "batteryFailure"),
        ("CERENT-454-MIB", "extremeHighVolt"),
        ("CERENT-454-MIB", "extremeLowVolt"),
        ("CERENT-454-MIB", "highVolt"),
        ("CERENT-454-MIB", "lowVolt"),
        ("CERENT-454-MIB", "suspendUser"),
        ("CERENT-454-MIB", "suspendUserClear"),
        ("CERENT-454-MIB", "lineDccTerminationFailure"),
        ("CERENT-454-MIB", "multiplexSectionDccTerminationFailure"),
        ("CERENT-454-MIB", "gigaBitEthernetOutOfSync"),
        ("CERENT-454-MIB", "sequenceMismatch"),
        ("CERENT-454-MIB", "lossOfAlignment"),
        ("CERENT-454-MIB", "outOfUseByAdministrativeCommand"),
        ("CERENT-454-MIB", "outOfUseTransportFailure"),
        ("CERENT-454-MIB", "vcatGroupDown"),
        ("CERENT-454-MIB", "vcatGroupDegraded"),
        ("CERENT-454-MIB", "vcatGroupIncomplete"),
        ("CERENT-454-MIB", "alarmIndicationSignalInTX"),
        ("CERENT-454-MIB", "remoteAlarmIndicationInTX"),
        ("CERENT-454-MIB", "kByteAPSChannelFailure"),
        ("CERENT-454-MIB", "apsInvalidMode"),
        ("CERENT-454-MIB", "ipAddressAlreadyInUseWithinTheSameDccArea"),
        ("CERENT-454-MIB", "nodeNameInUseWithinTheSameDccArea"),
        ("CERENT-454-MIB", "rearPanelEthernetLinkRemoved"),
        ("CERENT-454-MIB", "manualSwitchToProtectResultedInNoTrafficSwitch"),
        ("CERENT-454-MIB", "manualSwitchBackToWorkingResultedInNoTrafficSwitch"),
        ("CERENT-454-MIB", "forcedSwitchToProtectResultedInNoTrafficSwitch"),
        ("CERENT-454-MIB", "forcedSwitchBackToWorkingResultedInNoTrafficSwitch"),
        ("CERENT-454-MIB", "duplicateSerialNumberDetectedOnAPluggableEntity"),
        ("CERENT-454-MIB", "lossOfSignalForOpticalChannel"),
        ("CERENT-454-MIB", "encapsulationMismatchPath"),
        ("CERENT-454-MIB", "encapsulationMismatchVT"),
        ("CERENT-454-MIB", "encapsulationMismatchHighOrderPath"),
        ("CERENT-454-MIB", "encapsulationMismatchLowOrderPath"),
        ("CERENT-454-MIB", "gfpUserPayloadMismatch"),
        ("CERENT-454-MIB", "gfpFibreChannelDistanceExtensionMismatch"),
        ("CERENT-454-MIB", "gfpFibreChannelDistanceExtensionBufferStarvation"),
        ("CERENT-454-MIB", "gfpFibreChannelDistanceExtensionCreditStarvation"),
        ("CERENT-454-MIB", "gfpClientSignalFailDetected"),
        ("CERENT-454-MIB", "gfpLossOfFrameDelineation"),
        ("CERENT-454-MIB", "gfpExtensionHeaderMismatch"),
        ("CERENT-454-MIB", "lcasVcgMemberTxSideInAddState"),
        ("CERENT-454-MIB", "lcasVcgMemberTxSideInDnuState"),
        ("CERENT-454-MIB", "lcasControlWordCrcCheckFailure"),
        ("CERENT-454-MIB", "lcasVcgMemberRxSideInFailState"),
        ("CERENT-454-MIB", "signalLossOnDataInterface"),
        ("CERENT-454-MIB", "synchronizationLossOnDataInterface"),
        ("CERENT-454-MIB", "portFAIL"),
        ("CERENT-454-MIB", "unreachablePortTargetPower"),
        ("CERENT-454-MIB", "portAddPowerDegradeLow"),
        ("CERENT-454-MIB", "portAddPowerDegradeHigh"),
        ("CERENT-454-MIB", "portAddPowerFailLow"),
        ("CERENT-454-MIB", "portAddPowerFailHigh"),
        ("CERENT-454-MIB", "automaticWdmAnsFinished"),
        ("CERENT-454-MIB", "incomingOverheadSignalAbsent"),
        ("CERENT-454-MIB", "opticalSafetyRemoteInterlockOn"),
        ("CERENT-454-MIB", "automaticPowerControlCorrectionSkipped"),
        ("CERENT-454-MIB", "apcCannotSetValueDueToRangeLimits"),
        ("CERENT-454-MIB", "farEndManualSwitchBackToWorkingSpan"),
        ("CERENT-454-MIB", "farEndForcedSwitchBackToWorkingSpan"),
        ("CERENT-454-MIB", "universalTransponderModuleHardwareFailure"),
        ("CERENT-454-MIB", "universalTransponderModuleCommunicationFailure"),
        ("CERENT-454-MIB", "pluginModuleRangeSettingsMismatch"),
        ("CERENT-454-MIB", "automaticPowerControlTerminatedOnManualRequest"),
        ("CERENT-454-MIB", "oduk1AlarmIndicationSignal"),
        ("CERENT-454-MIB", "oduk2AlarmIndicationSignal"),
        ("CERENT-454-MIB", "oduk3AlarmIndicationSignal"),
        ("CERENT-454-MIB", "oduk4AlarmIndicationSignal"),
        ("CERENT-454-MIB", "temperatureReadingMismatchBetweenSCCards"),
        ("CERENT-454-MIB", "voltageReadingMismatchBetweenSCCards"),
        ("CERENT-454-MIB", "alarmsSuppressedonOutOfGroupVcatMember"),
        ("CERENT-454-MIB", "blsrSoftwareVersionMismatch"),
        ("CERENT-454-MIB", "optimized1Plus1ApsPrimaryFacility"),
        ("CERENT-454-MIB", "optimized1Plus1ApsPrimarySectionMismatch"),
        ("CERENT-454-MIB", "optimized1Plus1ApsInvalidPrimarySection"),
        ("CERENT-454-MIB", "compositeClockHighLineVoltage"),
        ("CERENT-454-MIB", "berThresholdExceededForSignalDegradeVt"),
        ("CERENT-454-MIB", "berThresholdExceededForSignalFailureVt"),
        ("CERENT-454-MIB", "spanLengthOutOfRange"),
        ("CERENT-454-MIB", "idleSignalCondition"),
        ("CERENT-454-MIB", "idleSignalConditionInTx"),
        ("CERENT-454-MIB", "vtPathTraceIdentifierMismatch"),
        ("CERENT-454-MIB", "lossOfFrameInTX"),
        ("CERENT-454-MIB", "provisioningMismatch"),
        ("CERENT-454-MIB", "sectionTraceIdentifierMismatch"),
        ("CERENT-454-MIB", "regeneratorSectionTraceIdentifierMismatch"),
        ("CERENT-454-MIB", "switchingMatrixModuleFailureWorking"),
        ("CERENT-454-MIB", "switchingMatrixModuleFailureProtect"),
        ("CERENT-454-MIB", "slotCommunicationDisabled"),
        ("CERENT-454-MIB", "sessionTimeLimitExpired"),
        ("CERENT-454-MIB", "userPasswordChangeRequired"),
        ("CERENT-454-MIB", "isisAdjacencyFailure"),
        ("CERENT-454-MIB", "msspSoftwareVersionMismatch"),
        ("CERENT-454-MIB", "remoteAuthenticationFailSeeAuditLog"),
        ("CERENT-454-MIB", "ringIsSquelchingStsTraffic"),
        ("CERENT-454-MIB", "ringIsSquelchingVtTraffic"),
        ("CERENT-454-MIB", "archiveOfAuditLogFailed"),
        ("CERENT-454-MIB", "rprWrapped"),
        ("CERENT-454-MIB", "shelfCommunicationFailure"),
        ("CERENT-454-MIB", "duplicatedShelfIdentifier"),
        ("CERENT-454-MIB", "softwareMismatch"),
        ("CERENT-454-MIB", "lmpFailure"),
        ("CERENT-454-MIB", "opticalTerminationIncomplete"),
        ("CERENT-454-MIB", "forwardDefectIndication"),
        ("CERENT-454-MIB", "payloadMissingIndication"),
        ("CERENT-454-MIB", "spanMeasurementCannotBePerformed"),
        ("CERENT-454-MIB", "ringIsSquelchingHighOrderTraffic"),
        ("CERENT-454-MIB", "ringIsSquelchingLowOrderTraffic"),
        ("CERENT-454-MIB", "badPacketCountExceedsThreshold"),
        ("CERENT-454-MIB", "linkLayerKeepAliveFailure"),
        ("CERENT-454-MIB", "autonegotiationRemoteFailureIndication"),
        ("CERENT-454-MIB", "trailSignalFail"),
        ("CERENT-454-MIB", "ds1LoopbackCommandSentToFarEnd"),
        ("CERENT-454-MIB", "multiplexSectionSignalDegraded"),
        ("CERENT-454-MIB", "multiplexSectionExcessiveErrors"),
        ("CERENT-454-MIB", "highOrderPathSignalDegraded"),
        ("CERENT-454-MIB", "highOrderPathExcessiveErrors"),
        ("CERENT-454-MIB", "lowOrderPathSignalDegraded"),
        ("CERENT-454-MIB", "lowOrderPathExcessiveErrors"),
        ("CERENT-454-MIB", "regeneratorSectionDccTerminationFailure"),
        ("CERENT-454-MIB", "networkMemoryPoolLow"),
        ("CERENT-454-MIB", "ospfRoutingTableOverflow"),
        ("CERENT-454-MIB", "autoLaserShutdownDisabled"),
        ("CERENT-454-MIB", "rprProtectionIsActive"),
        ("CERENT-454-MIB", "maxRPRStationNumberExceeded"),
        ("CERENT-454-MIB", "rprProtectionConfigurationMismatched"),
        ("CERENT-454-MIB", "reservedBandwidthLinkRateExceededOnRinglet0"),
        ("CERENT-454-MIB", "reservedBandwidthLinkRateExceededOnRinglet1"),
        ("CERENT-454-MIB", "rprInterfaceInPassThroughMode"),
        ("CERENT-454-MIB", "rprPeerNodeIsMissing"),
        ("CERENT-454-MIB", "rprRiFailure"),
        ("CERENT-454-MIB", "rprSignalFailure"),
        ("CERENT-454-MIB", "rprSignalDegrade"),
        ("CERENT-454-MIB", "interlinkFailure"),
        ("CERENT-454-MIB", "apcWrongGain"),
        ("CERENT-454-MIB", "rprSpanMismatch"),
        ("CERENT-454-MIB", "efmRemoteFaultIndicationCriticalEvent"),
        ("CERENT-454-MIB", "efmRemoteFaultIndicationDyingGasp"),
        ("CERENT-454-MIB", "efmRemoteFaultIndicationLinkFault"),
        ("CERENT-454-MIB", "efmLinkMonitoringErroredSymbolPeriodEvent"),
        ("CERENT-454-MIB", "efmLinkMonitoringErroredFrameEvent"),
        ("CERENT-454-MIB", "efmLinkMonitoringErroredFramePeriodEvent"),
        ("CERENT-454-MIB", "efmLinkMonitoringErroredFrameSecondsSummary"),
        ("CERENT-454-MIB", "efmRemoteLoopbackRequestFailed"),
        ("CERENT-454-MIB", "fastAutomaticProtectionSwitching"),
        ("CERENT-454-MIB", "fastAutomaticProtectionSwitchingConfigMismatch"),
        ("CERENT-454-MIB", "lcasSinkGroupError"),
        ("CERENT-454-MIB", "lcasVcgMemberRxSideInDnuState"),
        ("CERENT-454-MIB", "fcDistanceExtFuncNotEstablished"),
        ("CERENT-454-MIB", "nonCiscoPPMInserted"),
        ("CERENT-454-MIB", "unqualifiedPPMInserted"),
        ("CERENT-454-MIB", "ftaMismatch"),
        ("CERENT-454-MIB", "cardPortsUnableToProvideProtection"),
        ("CERENT-454-MIB", "lmpSignalDegrade"),
        ("CERENT-454-MIB", "lmpSignalFailure"),
        ("CERENT-454-MIB", "lmpUnallocatedDataLink"),
        ("CERENT-454-MIB", "frontPortLinkLoss"),
        ("CERENT-454-MIB", "bertEnbl"),
        ("CERENT-454-MIB", "bertSyncFail"),
        ("CERENT-454-MIB", "workQueueFull"),
        ("CERENT-454-MIB", "equipmentPowerFailureAtConnectorA"),
        ("CERENT-454-MIB", "equipmentPowerFailureAtConnectorB"),
        ("CERENT-454-MIB", "equipmentPowerFailureAtReturnConnectorA"),
        ("CERENT-454-MIB", "equipmentPowerFailureAtReturnConnectorB"),
        ("CERENT-454-MIB", "ospfHelloFail"),
        ("CERENT-454-MIB", "openIOSlots"),
        ("CERENT-454-MIB", "lossOfClockFromMateShelfController"),
        ("CERENT-454-MIB", "virtualLanAlarmIndicationSignal"),
        ("CERENT-454-MIB", "dcuLossFailure"),
        ("CERENT-454-MIB", "ochncMaintenance"),
        ("CERENT-454-MIB", "ramanLaserShutdown"),
        ("CERENT-454-MIB", "losOfRamanSignal"),
        ("CERENT-454-MIB", "mcastMacTableFull"),
        ("CERENT-454-MIB", "multicastMacAddressAliasing"),
        ("CERENT-454-MIB", "ramanPwrProtOn"),
        ("CERENT-454-MIB", "cppPeerNotResponding"),
        ("CERENT-454-MIB", "voaControlLoopDisableDueToExcessiveCounterPropagationLight"),
        ("CERENT-454-MIB", "wizardIsRunning"),
        ("CERENT-454-MIB", "ramanGainNotReached"),
        ("CERENT-454-MIB", "localFault"),
        ("CERENT-454-MIB", "remoteFault"),
        ("CERENT-454-MIB", "efmRemoteLoopbackConfigured"),
        ("CERENT-454-MIB", "efmPeerMissing"),
        ("CERENT-454-MIB", "eqptDegrade"),
        ("CERENT-454-MIB", "excessiveBackPropagation"),
        ("CERENT-454-MIB", "remoteMaintenanceEndPointIsDown"),
        ("CERENT-454-MIB", "crossConnectedCFMService"),
        ("CERENT-454-MIB", "cfmLoop"),
        ("CERENT-454-MIB", "cfmConfigurationError"),
        ("CERENT-454-MIB", "outOfChannelGroupBundle"),
        ("CERENT-454-MIB", "repNeighborAdjacencyFailure"),
        ("CERENT-454-MIB", "repLinkFlapping"),
        ("CERENT-454-MIB", "faultInREPSegment"),
        ("CERENT-454-MIB", "primaryREPEdgePortElected"),
        ("CERENT-454-MIB", "secondaryREPEdgePortElected"),
        ("CERENT-454-MIB", "stcnREPGenerated"),
        ("CERENT-454-MIB", "vlbREPActivated"),
        ("CERENT-454-MIB", "vlbREPTriggerSoakingDelayActive"),
        ("CERENT-454-MIB", "pprForwardDefectIndication"),
        ("CERENT-454-MIB", "pprBackwardDefectIndication"),
        ("CERENT-454-MIB", "pprCoordinatedMaintenance"),
        ("CERENT-454-MIB", "pprTriggerThresholdBERExceeded"),
        ("CERENT-454-MIB", "wanSyncloss"),
        ("CERENT-454-MIB", "laserShutdownDueToWavelengthDrift"),
        ("CERENT-454-MIB", "manualLaserRestart"),
        ("CERENT-454-MIB", "laserShutdownDueToNonCiscoPPMInserted"),
        ("CERENT-454-MIB", "ethernetOSCTerminationFailure"),
        ("CERENT-454-MIB", "enhancedRemoteFailureIndicationPathServer"),
        ("CERENT-454-MIB", "enhancedRemoteFailureIndicationPathConnectivity"),
        ("CERENT-454-MIB", "enhancedRemoteFailureIndicationPathPayload"),
        ("CERENT-454-MIB", "securityIntrusionDetPwd"),
        ("CERENT-454-MIB", "securityIntrusionDetUser"),
        ("CERENT-454-MIB", "backPanelFacilityLoopback"),
        ("CERENT-454-MIB", "backPanelTerminalLoopback"),
        ("CERENT-454-MIB", "trunkPayloadTypeMismatch"),
        ("CERENT-454-MIB", "invalidMuxponderConfiguration"),
        ("CERENT-454-MIB", "coolingProfileMismatch"),
        ("CERENT-454-MIB", "trunkOduAlarmIndicationSignal"),
        ("CERENT-454-MIB", "companionCardMissing"),
        ("CERENT-454-MIB", "masterKeyExchangeFailed"),
        ("CERENT-454-MIB", "powerConsumptionLimitHasCrossed"),
        ("CERENT-454-MIB", "controlPlaneUnverifiedClearedAlarmsPresent"),
        ("CERENT-454-MIB", "unitHighTemperature"),
        ("CERENT-454-MIB", "overTemperatureUnitProtected"),
        ("CERENT-454-MIB", "seqMismatchCount"),
        ("CERENT-454-MIB", "keyProgramOnAlteraFpgaFailed"),
        ("CERENT-454-MIB", "duplicateNodeControllerDetected"),
        ("CERENT-454-MIB", "restorationInProg"),
        ("CERENT-454-MIB", "ramanPumpsCalibrationProcedureIsRunning"),
        ("CERENT-454-MIB", "ramanPumpsCalibrationIsScheduledToRunInTheNextMinutes"),
        ("CERENT-454-MIB", "odukTCM1AlarmIndicationSignal"),
        ("CERENT-454-MIB", "odukTCM2AlarmIndicationSignal"),
        ("CERENT-454-MIB", "odukLockedDefectTCM1"),
        ("CERENT-454-MIB", "odukLockedDefectTCM2"),
        ("CERENT-454-MIB", "otukLossOfFrame"),
        ("CERENT-454-MIB", "odukOpenConnectionIndicationTCM1"),
        ("CERENT-454-MIB", "odukOpenConnectionIndicationTCM2"),
        ("CERENT-454-MIB", "odukTrailTraceIdentifierMismatchTCM1"),
        ("CERENT-454-MIB", "odukTrailTraceIdentifierMismatchTCM2"),
        ("CERENT-454-MIB", "odukSignalFailureTCM1"),
        ("CERENT-454-MIB", "odukSignalFailureTCM2"),
        ("CERENT-454-MIB", "odukSignalDegradeTCM1"),
        ("CERENT-454-MIB", "odukSignalDegradeTCM2"),
        ("CERENT-454-MIB", "lossOfChannel"),
        ("CERENT-454-MIB", "fecMismatch"),
        ("CERENT-454-MIB", "timSectionMonitorTraceIdentifierMismatchFailure"),
        ("CERENT-454-MIB", "automaticLaserShutdown"),
        ("CERENT-454-MIB", "shutterInsertionLossVariationDegradeLow"),
        ("CERENT-454-MIB", "opticalChannelDeactivationFailure"),
        ("CERENT-454-MIB", "shutterInsertionLossVariationDegradeHigh"),
        ("CERENT-454-MIB", "networkTopologyIncomplete"),
        ("CERENT-454-MIB", "pluginModuleCommunicationFailure"),
        ("CERENT-454-MIB", "opticalNetworkTypeMismatch"),
        ("CERENT-454-MIB", "forcedSwitchToPrimaryReference"),
        ("CERENT-454-MIB", "forcedSwitchToSecondReference"),
        ("CERENT-454-MIB", "forcedSwitchToThirdReference"),
        ("CERENT-454-MIB", "forcedSwitchToInternalClock"),
        ("CERENT-454-MIB", "industrialHighTemperature"),
        ("CERENT-454-MIB", "opticalPowerDegradeLow"),
        ("CERENT-454-MIB", "automaticPowerControlFailure"),
        ("CERENT-454-MIB", "opticalPowerDegradeHigh"),
        ("CERENT-454-MIB", "automaticPowerControlDisabled"),
        ("CERENT-454-MIB", "opticalPowerFailureLow"),
        ("CERENT-454-MIB", "ringIdMismatch"),
        ("CERENT-454-MIB", "opticalPowerFailureHigh"),
        ("CERENT-454-MIB", "lossOfContinuity"),
        ("CERENT-454-MIB", "variableOpticalAttenuatorDegradeLow"),
        ("CERENT-454-MIB", "variableOpticalAttenuatorDegradeHigh"),
        ("CERENT-454-MIB", "variableOpticalAttenuatorFailureLow"),
        ("CERENT-454-MIB", "variableOpticalAttenuatorFailureHigh"),
        ("CERENT-454-MIB", "laserBiasDegrade"),
        ("CERENT-454-MIB", "laserBiasFailure"),
        ("CERENT-454-MIB", "laserTemperatureDegrade"),
        ("CERENT-454-MIB", "opticalAmplifierGainDegradeLow"),
        ("CERENT-454-MIB", "opticalAmplifierGainDegradeHigh"),
        ("CERENT-454-MIB", "opticalAmplifierGainFailureLow"),
        ("CERENT-454-MIB", "opticalAmplifierGainFailureHigh"),
        ("CERENT-454-MIB", "opticalChannelConnectionFailure"),
        ("CERENT-454-MIB", "opticalChannelIncomplete"),
        ("CERENT-454-MIB", "opticalChannelActivationFailure"),
        ("CERENT-454-MIB", "laserAutoPowerReduction"),
        ("CERENT-454-MIB", "caseTemperatureDegrade"),
        ("CERENT-454-MIB", "fiberTemperatureDegrade"),
        ("CERENT-454-MIB", "shutterOpen"),
        ("CERENT-454-MIB", "awgTemperatureDegrade"),
        ("CERENT-454-MIB", "awgTemperatureFailure"),
        ("CERENT-454-MIB", "awgOverTemperature"),
        ("CERENT-454-MIB", "opticalAmplifierInitialization"),
        ("CERENT-454-MIB", "awgWarmUp"),
        ("CERENT-454-MIB", "incSigloss"),
        ("CERENT-454-MIB", "incSyncloss"),
        ("CERENT-454-MIB", "incGfpOutOfFrame"),
        ("CERENT-454-MIB", "incGfpSigLoss"),
        ("CERENT-454-MIB", "incGfpSyncLoss"),
        ("CERENT-454-MIB", "bridgeAndRollHasOccurred"),
        ("CERENT-454-MIB", "bridgeAndRollIsPendingAValidSignal"),
        ("CERENT-454-MIB", "clockBusFailureTscA"),
        ("CERENT-454-MIB", "clockBusFailureTscB"),
        ("CERENT-454-MIB", "waitToRestore"),
        ("CERENT-454-MIB", "extremeHighVoltBatteryA"),
        ("CERENT-454-MIB", "extremeLowVoltBatteryA"),
        ("CERENT-454-MIB", "extremeHighVoltBatteryB"),
        ("CERENT-454-MIB", "extremeLowVoltBatteryB"),
        ("CERENT-454-MIB", "iosConfigCopyFailed"),
        ("CERENT-454-MIB", "iosConfigCopyInProgress"),
        ("CERENT-454-MIB", "iosConfigCopySuccess"),
        ("CERENT-454-MIB", "signalingUnableToSetupCircuit"),
        ("CERENT-454-MIB", "errorInStartupConfig"),
        ("CERENT-454-MIB", "noStartupConfig"),
        ("CERENT-454-MIB", "needToSaveRunningConfig"),
        ("CERENT-454-MIB", "invalidAlarm"),
        ("CERENT-454-MIB", "rsvpHelloFSMToNeighborDown"),
        ("CERENT-454-MIB", "securityInvalidLoginUsername"),
        ("CERENT-454-MIB", "databaseBackupFailed"),
        ("CERENT-454-MIB", "databaseRestoreFailed"),
        ("CERENT-454-MIB", "lmpHelloFSMToControlChannelDown"),
        ("CERENT-454-MIB", "lmpNeighborDiscoveryHasFailed"),
        ("CERENT-454-MIB", "auditLog80PercentFull"),
        ("CERENT-454-MIB", "moduleCommunicationFailure"),
        ("CERENT-454-MIB", "auditLog100PercentFullOldestRecordsWillBeLost"),
        ("CERENT-454-MIB", "standbyDatabaseOutOfSync"),
        ("CERENT-454-MIB", "redundantPowerCapabilityLost"),
        ("CERENT-454-MIB", "lofAdministrationUnitLossOfMultiFrame"),
        ("CERENT-454-MIB", "sdhSpanIsInWaitToRestoreState"),
        ("CERENT-454-MIB", "berThresholdExceededForSignalDegradeLine"),
        ("CERENT-454-MIB", "berThresholdExceededForSignalDegradePath"),
        ("CERENT-454-MIB", "berThresholdExceededForSignalFailureLine"),
        ("CERENT-454-MIB", "berThresholdExceededForSignalFailurePath"),
        ("CERENT-454-MIB", "unauthorizedIncomingSignalingRequest"))
)
if mibBuilder.loadTexts:
    event454Group.setStatus(
        "current"
    )

event454DeprecatedGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 10, 10, 60)
)
event454DeprecatedGroup.setObjects(
    ("CERENT-454-MIB", "securityInvalidLoginUsernameSeeAuditTrail")
)
if mibBuilder.loadTexts:
    event454DeprecatedGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

cerent454BasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3607, 6, 10, 10, 20, 10)
)
if mibBuilder.loadTexts:
    cerent454BasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CERENT-454-MIB",
    **{"Cerent454AlarmType": Cerent454AlarmType,
       "Cerent454EntityClass": Cerent454EntityClass,
       "cerent454MibModule": cerent454MibModule,
       "cerent454Mib": cerent454Mib,
       "cerent454Conformance": cerent454Conformance,
       "cerent454Groups": cerent454Groups,
       "node454Group": node454Group,
       "alarm454Group": alarm454Group,
       "event454Group": event454Group,
       "cerent454CommonGroup": cerent454CommonGroup,
       "cerentThresholdGroup": cerentThresholdGroup,
       "event454DeprecatedGroup": event454DeprecatedGroup,
       "reportedAlarm454Group": reportedAlarm454Group,
       "cerent454Compliance": cerent454Compliance,
       "cerent454BasicCompliance": cerent454BasicCompliance,
       "cerent454Objects": cerent454Objects,
       "cerent454GeneralGroup": cerent454GeneralGroup,
       "cerent454SoftwareVersion": cerent454SoftwareVersion,
       "cerent454AlarmGroup": cerent454AlarmGroup,
       "cerent454AlarmCount": cerent454AlarmCount,
       "cerent454AlarmTable": cerent454AlarmTable,
       "cerent454AlarmEntry": cerent454AlarmEntry,
       "cerent454AlarmIndex": cerent454AlarmIndex,
       "cerent454AlarmObjectType": cerent454AlarmObjectType,
       "cerent454AlarmSlotNumber": cerent454AlarmSlotNumber,
       "cerent454AlarmPortNumber": cerent454AlarmPortNumber,
       "cerent454AlarmLineNumber": cerent454AlarmLineNumber,
       "cerent454AlarmObjectIndex": cerent454AlarmObjectIndex,
       "cerent454AlarmType": cerent454AlarmType,
       "cerent454AlarmState": cerent454AlarmState,
       "cerent454AlarmTimeStamp": cerent454AlarmTimeStamp,
       "cerent454AlarmObjectName": cerent454AlarmObjectName,
       "cerent454AlarmAdditionalInfo": cerent454AlarmAdditionalInfo,
       "cerent454AlarmSeverity": cerent454AlarmSeverity,
       "cerent454AlarmStatus": cerent454AlarmStatus,
       "cerent454AlarmServiceAffecting": cerent454AlarmServiceAffecting,
       "cerent454ReportedAlarmCount": cerent454ReportedAlarmCount,
       "cerent454ReportedAlarmTable": cerent454ReportedAlarmTable,
       "cerent454ReportedAlarmEntry": cerent454ReportedAlarmEntry,
       "cerent454ReportedAlarmIndex": cerent454ReportedAlarmIndex,
       "cerent454ReportedAlarmObjectType": cerent454ReportedAlarmObjectType,
       "cerent454ReportedAlarmSlotNumber": cerent454ReportedAlarmSlotNumber,
       "cerent454ReportedAlarmPortNumber": cerent454ReportedAlarmPortNumber,
       "cerent454ReportedAlarmObjectIndex": cerent454ReportedAlarmObjectIndex,
       "cerent454ReportedAlarmType": cerent454ReportedAlarmType,
       "cerent454ReportedAlarmTimeStamp": cerent454ReportedAlarmTimeStamp,
       "cerent454ReportedAlarmObjectName": cerent454ReportedAlarmObjectName,
       "cerent454ReportedAlarmAdditionalInfo": cerent454ReportedAlarmAdditionalInfo,
       "cerent454ReportedAlarmSeverity": cerent454ReportedAlarmSeverity,
       "cerent454ReportedAlarmStatus": cerent454ReportedAlarmStatus,
       "cerent454ReportedAlarmServiceAffecting": cerent454ReportedAlarmServiceAffecting,
       "cerent454ThresholdGroup": cerent454ThresholdGroup,
       "cerent454ThresholdTable": cerent454ThresholdTable,
       "cerent454ThresholdEntry": cerent454ThresholdEntry,
       "cerent454ThresholdIndex": cerent454ThresholdIndex,
       "cerent454ThresholdMonitorType": cerent454ThresholdMonitorType,
       "cerent454ThresholdLocation": cerent454ThresholdLocation,
       "cerent454ThresholdPeriod": cerent454ThresholdPeriod,
       "cerent454ThresholdSetValue": cerent454ThresholdSetValue,
       "cerent454ThresholdCurrentValue": cerent454ThresholdCurrentValue,
       "cerent454ThresholdDetectType": cerent454ThresholdDetectType,
       "cerent454Events": cerent454Events,
       "cerent454V2Events": cerent454V2Events,
       "alarmUnknown": alarmUnknown,
       "alarmCutoffIsInManualMode": alarmCutoffIsInManualMode,
       "failureDetectedExternalToTheNE": failureDetectedExternalToTheNE,
       "externalError": externalError,
       "excessiveSwitching": excessiveSwitching,
       "sdccTerminationFailure": sdccTerminationFailure,
       "incomingFailureCondition": incomingFailureCondition,
       "alarmIndicationSignal": alarmIndicationSignal,
       "alarmIndicationSignalLine": alarmIndicationSignalLine,
       "alarmIndicationSignalPath": alarmIndicationSignalPath,
       "alarmIndicationSignalVT": alarmIndicationSignalVT,
       "apsChannelFailure": apsChannelFailure,
       "channelByteFailureAPS": channelByteFailureAPS,
       "channelProtectionSwitchingChannelMatchFailureAPS": channelProtectionSwitchingChannelMatchFailureAPS,
       "channelAutomaticProtectionSwitchModeMismatchAPS": channelAutomaticProtectionSwitchModeMismatchAPS,
       "farEndProtectionLineFailure": farEndProtectionLineFailure,
       "inconsistentAPSCode": inconsistentAPSCode,
       "improperAPSCode": improperAPSCode,
       "nodeIdMismatch": nodeIdMismatch,
       "channelDefaultKAPS": channelDefaultKAPS,
       "connectionLoss": connectionLoss,
       "bipolarViolation": bipolarViolation,
       "carrierLossOnTheLAN": carrierLossOnTheLAN,
       "concatenationErrorSTS": concatenationErrorSTS,
       "excessCollisionsOnTheLAN": excessCollisionsOnTheLAN,
       "facilityFailure": facilityFailure,
       "farEndAIS": farEndAIS,
       "farEndMultipleDS1LOSDetectedOnDS3": farEndMultipleDS1LOSDetectedOnDS3,
       "farEndDS1EqptFailNonServiceAffecting": farEndDS1EqptFailNonServiceAffecting,
       "farEndDS1EqptFailServiceAffecting": farEndDS1EqptFailServiceAffecting,
       "farEndSingleDS1LOS": farEndSingleDS1LOS,
       "farEndDS3EqptFailNonServiceAffecting": farEndDS3EqptFailNonServiceAffecting,
       "farEndDS3EqptFailServiceAffecting": farEndDS3EqptFailServiceAffecting,
       "farEndCommonEquipmentFailureNonServiceAffecting": farEndCommonEquipmentFailureNonServiceAffecting,
       "farEndIDLE": farEndIDLE,
       "farEndLOS": farEndLOS,
       "farEndLOF": farEndLOF,
       "farEndBlockError": farEndBlockError,
       "ds3IdleCondition": ds3IdleCondition,
       "lossOfFrame": lossOfFrame,
       "lossOfPointer": lossOfPointer,
       "lossOfPointerPath": lossOfPointerPath,
       "lossOfPointerVT": lossOfPointerVT,
       "lossOfSignal": lossOfSignal,
       "outOfFrame": outOfFrame,
       "pathSelectorFailure": pathSelectorFailure,
       "remoteAlarmIndication": remoteAlarmIndication,
       "remoteFailureIndication": remoteFailureIndication,
       "remoteFailureIndicationLine": remoteFailureIndicationLine,
       "remoteFailureIndicationPath": remoteFailureIndicationPath,
       "remoteFailureIndicationVT": remoteFailureIndicationVT,
       "signalDegrade": signalDegrade,
       "severelyErroredFrame": severelyErroredFrame,
       "signalFailure": signalFailure,
       "signalLabelMismatchFailure": signalLabelMismatchFailure,
       "payloadDefectIndication": payloadDefectIndication,
       "payloadDefectIndicationPath": payloadDefectIndicationPath,
       "payloadLabelMismatchPath": payloadLabelMismatchPath,
       "signalLabelMismatchFailurePayloadLabelMismatchVT": signalLabelMismatchFailurePayloadLabelMismatchVT,
       "unequippedPath": unequippedPath,
       "signalLabelMismatchFailureUnequippedVT": signalLabelMismatchFailureUnequippedVT,
       "lossOfSynchronization": lossOfSynchronization,
       "outOfSynchronization": outOfSynchronization,
       "primarySynchronizationReferenceFailure": primarySynchronizationReferenceFailure,
       "secondarySynchronizationReferenceFailure": secondarySynchronizationReferenceFailure,
       "thirdSynchronizationReferenceFailure": thirdSynchronizationReferenceFailure,
       "fourthSynchronizationReferenceFailure": fourthSynchronizationReferenceFailure,
       "fifthSynchronizationReferenceFailure": fifthSynchronizationReferenceFailure,
       "sixthSynchronizationReferenceFailure": sixthSynchronizationReferenceFailure,
       "failedToReceiveSynchronizationStatusMessage": failedToReceiveSynchronizationStatusMessage,
       "synchronizationStatusMessagesAreDisabledOnThisInterface": synchronizationStatusMessagesAreDisabledOnThisInterface,
       "stratum1PrimaryReferenceSourceTraceable": stratum1PrimaryReferenceSourceTraceable,
       "synchronizedTraceabilityUnknown": synchronizedTraceabilityUnknown,
       "stratum2Traceable": stratum2Traceable,
       "transitNodeClockTraceable": transitNodeClockTraceable,
       "stratum3ETraceable": stratum3ETraceable,
       "stratum3Traceable": stratum3Traceable,
       "sonetMinimumClockTraceable": sonetMinimumClockTraceable,
       "stratum4Traceable": stratum4Traceable,
       "doNotUseForSynchronization": doNotUseForSynchronization,
       "reservedForNetworkSynchronizationUse": reservedForNetworkSynchronizationUse,
       "outgoingFailureCondition": outgoingFailureCondition,
       "remoteDefectIndicationLine": remoteDefectIndicationLine,
       "remoteDefectIndicationPath": remoteDefectIndicationPath,
       "freeRunningSynchronizationMode": freeRunningSynchronizationMode,
       "holdoverSynchronizationMode": holdoverSynchronizationMode,
       "fastStartSynchronizationMode": fastStartSynchronizationMode,
       "internalFault": internalFault,
       "internalError": internalError,
       "internalMessageError": internalMessageError,
       "mismatchOfEquipmentAndAttributes": mismatchOfEquipmentAndAttributes,
       "watchdogTimerTimeout": watchdogTimerTimeout,
       "softwareFaultOrFailure": softwareFaultOrFailure,
       "softwareFaultDataIntegrityFault": softwareFaultDataIntegrityFault,
       "programFailure": programFailure,
       "controlEquipmentFailure": controlEquipmentFailure,
       "primaryNonVolatileBackupMemoryFailure": primaryNonVolatileBackupMemoryFailure,
       "secondaryNonVolatileBackupMemoryFailure": secondaryNonVolatileBackupMemoryFailure,
       "controlBusFailure": controlBusFailure,
       "controlBus1Failure": controlBus1Failure,
       "controlBus2Failure": controlBus2Failure,
       "tccAToShelfSlot1DROP1CommunicationFailure": tccAToShelfSlot1DROP1CommunicationFailure,
       "tccAToShelfSlot2DROP2CommunicationFailure": tccAToShelfSlot2DROP2CommunicationFailure,
       "tccAToShelfSlot3DROP3CommunicationFailure": tccAToShelfSlot3DROP3CommunicationFailure,
       "tccAToShelfSlot4DROP4CommunicationFailure": tccAToShelfSlot4DROP4CommunicationFailure,
       "tccAToShelfSlot5TRUNK1CommunicationFailure": tccAToShelfSlot5TRUNK1CommunicationFailure,
       "tccAToShelfSlot6TRUNK2CommunicationFailure": tccAToShelfSlot6TRUNK2CommunicationFailure,
       "tccAToShelfSlot7TCCACommunicationFailure": tccAToShelfSlot7TCCACommunicationFailure,
       "tccAToShelfSlot8XCONACommunicationFailure": tccAToShelfSlot8XCONACommunicationFailure,
       "tccAToShelfSlot9AICCommunicationFailure": tccAToShelfSlot9AICCommunicationFailure,
       "tccAToShelfSlot10XCONBCommunicationFailure": tccAToShelfSlot10XCONBCommunicationFailure,
       "tccAToShelfSlot11TCCBCommunicationFailure": tccAToShelfSlot11TCCBCommunicationFailure,
       "tccAToShelfSlot12TRUNK3CommunicationFailure": tccAToShelfSlot12TRUNK3CommunicationFailure,
       "tccAToShelfSlot13TRUNK4CommunicationFailure": tccAToShelfSlot13TRUNK4CommunicationFailure,
       "tccAToShelfSlot14DROP5CommunicationFailure": tccAToShelfSlot14DROP5CommunicationFailure,
       "tccAToShelfSlot15DROP6CommunicationFailure": tccAToShelfSlot15DROP6CommunicationFailure,
       "tccAToShelfSlot16DROP7CommunicationFailure": tccAToShelfSlot16DROP7CommunicationFailure,
       "tccAToShelfSlot17DROP8CommunicationFailure": tccAToShelfSlot17DROP8CommunicationFailure,
       "tccAToDCCAProcessorCommunicationFailure": tccAToDCCAProcessorCommunicationFailure,
       "tccBToShelfSlot1DROP1CommunicationFailure": tccBToShelfSlot1DROP1CommunicationFailure,
       "tccBToShelfSlot2DROP2CommunicationFailure": tccBToShelfSlot2DROP2CommunicationFailure,
       "tccBToShelfSlot3DROP3CommunicationFailure": tccBToShelfSlot3DROP3CommunicationFailure,
       "tccBToShelfSlot4DROP4CommunicationFailure": tccBToShelfSlot4DROP4CommunicationFailure,
       "tccBToShelfSlot5TRUNK1CommunicationFailure": tccBToShelfSlot5TRUNK1CommunicationFailure,
       "tccBToShelfSlot6TRUNK2CommunicationFailure": tccBToShelfSlot6TRUNK2CommunicationFailure,
       "tccBToShelfSlot7TCCACommunicationFailure": tccBToShelfSlot7TCCACommunicationFailure,
       "tccBToShelfSlot8XCONACommunicationFailure": tccBToShelfSlot8XCONACommunicationFailure,
       "tccBToShelfSlot9AICCommunicationFailure": tccBToShelfSlot9AICCommunicationFailure,
       "tccBToShelfSlot10XCONBCommunicationFailure": tccBToShelfSlot10XCONBCommunicationFailure,
       "tccBToShelfSlot11TCCBCommunicationFailure": tccBToShelfSlot11TCCBCommunicationFailure,
       "tccBToShelfSlot12TRUNK3CommunicationFailure": tccBToShelfSlot12TRUNK3CommunicationFailure,
       "tccBToShelfSlot13TRUNK4CommunicationFailure": tccBToShelfSlot13TRUNK4CommunicationFailure,
       "tccBToShelfSlot14DROP5CommunicationFailure": tccBToShelfSlot14DROP5CommunicationFailure,
       "tccBToShelfSlot15DROP6CommunicationFailure": tccBToShelfSlot15DROP6CommunicationFailure,
       "tccBToShelfSlot16DROP7CommunicationFailure": tccBToShelfSlot16DROP7CommunicationFailure,
       "tccBToShelfSlot17DROP8CommunicationFailure": tccBToShelfSlot17DROP8CommunicationFailure,
       "tccBToDCCBProcessorCommunicationFailure": tccBToDCCBProcessorCommunicationFailure,
       "controlEquipmentControlCommunicationsEquipmentFailure": controlEquipmentControlCommunicationsEquipmentFailure,
       "controlProcessorFailure": controlProcessorFailure,
       "workingMemoryFailure": workingMemoryFailure,
       "interconnectionEquipmentFailure": interconnectionEquipmentFailure,
       "payloadBusFailureToIOSlot1XCONSlot8": payloadBusFailureToIOSlot1XCONSlot8,
       "payloadBusFailureToIOSlot2XCONSlot8": payloadBusFailureToIOSlot2XCONSlot8,
       "payloadBusFailureToIOSlot3XCONSlot8": payloadBusFailureToIOSlot3XCONSlot8,
       "payloadBusFailureToIOSlot4XCONSlot8": payloadBusFailureToIOSlot4XCONSlot8,
       "payloadBusFailureToIOSlot5XCONSlot8": payloadBusFailureToIOSlot5XCONSlot8,
       "payloadBusFailureToIOSlot6XCONSlot8": payloadBusFailureToIOSlot6XCONSlot8,
       "payloadBusFailureToIOSlot12XCONSlot8": payloadBusFailureToIOSlot12XCONSlot8,
       "payloadBusFailureToIOSlot13XCONSlot8": payloadBusFailureToIOSlot13XCONSlot8,
       "payloadBusFailureToIOSlot14XCONSlot8": payloadBusFailureToIOSlot14XCONSlot8,
       "payloadBusFailureToIOSlot15XCONSlot8": payloadBusFailureToIOSlot15XCONSlot8,
       "payloadBusFailureToIOSlot16XCONSlot8": payloadBusFailureToIOSlot16XCONSlot8,
       "payloadBusFailureToIOSlot17XCONSlot8": payloadBusFailureToIOSlot17XCONSlot8,
       "payloadBusFailureToIOSlot1XCONSlot10": payloadBusFailureToIOSlot1XCONSlot10,
       "payloadBusFailureToIOSlot2XCONSlot10": payloadBusFailureToIOSlot2XCONSlot10,
       "payloadBusFailureToIOSlot3XCONSlot10": payloadBusFailureToIOSlot3XCONSlot10,
       "payloadBusFailureToIOSlot4XCONSlot10": payloadBusFailureToIOSlot4XCONSlot10,
       "payloadBusFailureToIOSlot5XCONSlot10": payloadBusFailureToIOSlot5XCONSlot10,
       "payloadBusFailureToIOSlot6XCONSlot10": payloadBusFailureToIOSlot6XCONSlot10,
       "payloadBusFailureToIOSlot12XCONSlot10": payloadBusFailureToIOSlot12XCONSlot10,
       "payloadBusFailureToIOSlot13XCONSlot10": payloadBusFailureToIOSlot13XCONSlot10,
       "payloadBusFailureToIOSlot14XCONSlot10": payloadBusFailureToIOSlot14XCONSlot10,
       "payloadBusFailureToIOSlot15XCONSlot10": payloadBusFailureToIOSlot15XCONSlot10,
       "payloadBusFailureToIOSlot16XCONSlot10": payloadBusFailureToIOSlot16XCONSlot10,
       "payloadBusFailureToIOSlot17XCONSlot10": payloadBusFailureToIOSlot17XCONSlot10,
       "timeSlotInterchangeEquipmentFailure": timeSlotInterchangeEquipmentFailure,
       "equipmentFailure": equipmentFailure,
       "highTemperature": highTemperature,
       "invalidMACAddress": invalidMACAddress,
       "boardFailure": boardFailure,
       "diagnosticFailure": diagnosticFailure,
       "mediumAccessControlFailure": mediumAccessControlFailure,
       "facilityTerminationEquipmentFailure": facilityTerminationEquipmentFailure,
       "automaticLaserShutoffDueToHighTemperature": automaticLaserShutoffDueToHighTemperature,
       "failureToReleaseFromProtection": failureToReleaseFromProtection,
       "receiverFailure": receiverFailure,
       "transmitFailure": transmitFailure,
       "facilityTerminationEquipmentReceiverMissing": facilityTerminationEquipmentReceiverMissing,
       "facilityTerminationEquipmentTransmitterMissing": facilityTerminationEquipmentTransmitterMissing,
       "failureToSwitchToProtection": failureToSwitchToProtection,
       "failureToSwitchToProtectionRing": failureToSwitchToProtectionRing,
       "failureToSwitchToProtectionSpan": failureToSwitchToProtectionSpan,
       "failureToSwitchToProtectionPath": failureToSwitchToProtectionPath,
       "fanFailure": fanFailure,
       "equipmentUnitPlugIn": equipmentUnitPlugIn,
       "nePowerFailureAtConnector": nePowerFailureAtConnector,
       "fuseAlarm": fuseAlarm,
       "synchronizationUnitFailure": synchronizationUnitFailure,
       "synchronizationSwitchingEquipmentFailure": synchronizationSwitchingEquipmentFailure,
       "equipmentUnitUnplugged": equipmentUnitUnplugged,
       "loopback": loopback,
       "ds1LoopbackDueToFEACCommand": ds1LoopbackDueToFEACCommand,
       "loopbackCommandSentToFarEndDS1": loopbackCommandSentToFarEndDS1,
       "ds3LoopbackDueToFEACCommand": ds3LoopbackDueToFEACCommand,
       "ds3LoopbackCommandSentToFarEnd": ds3LoopbackCommandSentToFarEnd,
       "ds2LoopbackDueToFarEndCommand": ds2LoopbackDueToFarEndCommand,
       "ds2LoopbackCommandSentToFarEnd": ds2LoopbackCommandSentToFarEnd,
       "facilityLoopback": facilityLoopback,
       "networkLoopback": networkLoopback,
       "terminalLoopback": terminalLoopback,
       "manuallyCausedAbnormalCondition": manuallyCausedAbnormalCondition,
       "ethernetBridgeIsNewRootOfSpanningTree": ethernetBridgeIsNewRootOfSpanningTree,
       "ethernetBridgeTopologyChange": ethernetBridgeTopologyChange,
       "normalCondition": normalCondition,
       "embeddedOperationsChannelFailureLinkDown": embeddedOperationsChannelFailureLinkDown,
       "peerStateMismatch": peerStateMismatch,
       "proceduralError": proceduralError,
       "improperRemoval": improperRemoval,
       "duplicateNodeID": duplicateNodeID,
       "blsrOutOfSync": blsrOutOfSync,
       "blsrMultiNodeTableUpdateCompleted": blsrMultiNodeTableUpdateCompleted,
       "protectionUnitNotAvailable": protectionUnitNotAvailable,
       "performanceMonitorThresholdCrossingAlert": performanceMonitorThresholdCrossingAlert,
       "protectionSwitch": protectionSwitch,
       "recoveryOrServiceProtectionActionHasBeenInitiated": recoveryOrServiceProtectionActionHasBeenInitiated,
       "automaticSystemReset": automaticSystemReset,
       "automaticUPSRSwitchCausedByAIS": automaticUPSRSwitchCausedByAIS,
       "automaticUPSRSwitchCausedByLOP": automaticUPSRSwitchCausedByLOP,
       "automaticUPSRSwitchCausedByUNEQ": automaticUPSRSwitchCausedByUNEQ,
       "automaticUPSRSwitchCausedByPDI": automaticUPSRSwitchCausedByPDI,
       "automaticUPSRSwitchCausedBySFBER": automaticUPSRSwitchCausedBySFBER,
       "automaticUPSRSwitchCausedBySDBER": automaticUPSRSwitchCausedBySDBER,
       "coldRestart": coldRestart,
       "forcedSwitchBackToWorking": forcedSwitchBackToWorking,
       "forcedSwitchBackToWorkingRing": forcedSwitchBackToWorkingRing,
       "forcedSwitchBackToWorkingSpan": forcedSwitchBackToWorkingSpan,
       "forcedSwitchToProtection": forcedSwitchToProtection,
       "forcedSwitchToProtectionRing": forcedSwitchToProtectionRing,
       "forcedSwitchToProtectionSpan": forcedSwitchToProtectionSpan,
       "workingFacilityOrEquipmentForcedToSwitchToProtectionPath": workingFacilityOrEquipmentForcedToSwitchToProtectionPath,
       "initializationInitiated": initializationInitiated,
       "lockoutOfProtection": lockoutOfProtection,
       "lockoutOfProtectionRing": lockoutOfProtectionRing,
       "lockoutOfProtectionSpan": lockoutOfProtectionSpan,
       "lockoutOfProtectionPath": lockoutOfProtectionPath,
       "lockoutOfWorking": lockoutOfWorking,
       "lockoutOfWorkingRing": lockoutOfWorkingRing,
       "lockoutOfWorkingSpan": lockoutOfWorkingSpan,
       "manualSystemReset": manualSystemReset,
       "manualSwitchToInternalClock": manualSwitchToInternalClock,
       "manualSwitchToPrimaryReference": manualSwitchToPrimaryReference,
       "manualSwitchToSecondReference": manualSwitchToSecondReference,
       "manualSwitchToThirdReference": manualSwitchToThirdReference,
       "manualSwitchToFourthReference": manualSwitchToFourthReference,
       "manualSwitchToFifthReference": manualSwitchToFifthReference,
       "manualSwitchToSixthReference": manualSwitchToSixthReference,
       "manualSwitchBackToWorking": manualSwitchBackToWorking,
       "manualSwitchBackToWorkingRing": manualSwitchBackToWorkingRing,
       "manualSwitchBackToWorkingSpan": manualSwitchBackToWorkingSpan,
       "manualSwitchToProtection": manualSwitchToProtection,
       "manualSwitchToProtectionRing": manualSwitchToProtectionRing,
       "manualSwitchToProtectionSpan": manualSwitchToProtectionSpan,
       "manualSwitchOfWorkingFacilityOrEquipmentToProtectionPath": manualSwitchOfWorkingFacilityOrEquipmentToProtectionPath,
       "powerfailRestart": powerfailRestart,
       "ringIsSquelchingTraffic": ringIsSquelchingTraffic,
       "softwareDownloadInProgress": softwareDownloadInProgress,
       "switchToInternalClock": switchToInternalClock,
       "switchToPrimaryReference": switchToPrimaryReference,
       "switchToSecondReference": switchToSecondReference,
       "switchToThirdReference": switchToThirdReference,
       "switchToFourthReference": switchToFourthReference,
       "switchToFifthReference": switchToFifthReference,
       "switchToSixthReference": switchToSixthReference,
       "systemReboot": systemReboot,
       "switchedBackToWorking": switchedBackToWorking,
       "switchedToProtection": switchedToProtection,
       "warmRestart": warmRestart,
       "ringIsInWaitToRestoreState": ringIsInWaitToRestoreState,
       "manualSwitchRequest": manualSwitchRequest,
       "forcedSwitchRequest": forcedSwitchRequest,
       "lockoutSwitchRequest": lockoutSwitchRequest,
       "rmonHistoriesAndAlarmsResetReboot": rmonHistoriesAndAlarmsResetReboot,
       "rmonThresholdCrossingAlarm": rmonThresholdCrossingAlarm,
       "alarmsSuppressedByUserCommand": alarmsSuppressedByUserCommand,
       "alarmsSuppressedForMaintenance": alarmsSuppressedForMaintenance,
       "switchingMatrixModuleFailure": switchingMatrixModuleFailure,
       "lanConnectionPolarityReversed": lanConnectionPolarityReversed,
       "autonomousPMReportMessageInhibited": autonomousPMReportMessageInhibited,
       "ioSlotToXCONCommunicationFailure": ioSlotToXCONCommunicationFailure,
       "stsPathTraceIdentifierMismatch": stsPathTraceIdentifierMismatch,
       "nePowerFailureAtConnectorA": nePowerFailureAtConnectorA,
       "nePowerFailureAtConnectorB": nePowerFailureAtConnectorB,
       "freeMemoryOnCardVeryLow": freeMemoryOnCardVeryLow,
       "freeMemoryOnCardNearZero": freeMemoryOnCardNearZero,
       "exerciseRequestOnRing": exerciseRequestOnRing,
       "exerciseRequestOnSpan": exerciseRequestOnSpan,
       "squelchingPath": squelchingPath,
       "extraTrafficPreempted": extraTrafficPreempted,
       "farEndLockoutOfWorkingRing": farEndLockoutOfWorkingRing,
       "farEndLockoutOfWorkingSpan": farEndLockoutOfWorkingSpan,
       "farEndLockoutOfProtectionRing": farEndLockoutOfProtectionRing,
       "farEndLockoutOfProtectionAllSpans": farEndLockoutOfProtectionAllSpans,
       "farEndWorkingFacilityForcedToSwitchToProtectionRing": farEndWorkingFacilityForcedToSwitchToProtectionRing,
       "farEndWorkingFacilityForcedToSwitchToProtectionSpan": farEndWorkingFacilityForcedToSwitchToProtectionSpan,
       "farEndManualSwitchOfWorkingFacilityToProtectionRing": farEndManualSwitchOfWorkingFacilityToProtectionRing,
       "farEndManualSwitchOfWorkingFacilityToProtectionSpan": farEndManualSwitchOfWorkingFacilityToProtectionSpan,
       "farEndExercisingRing": farEndExercisingRing,
       "farEndExercisingSpan": farEndExercisingSpan,
       "farEndBERThresholdPassedForSignalFailureRing": farEndBERThresholdPassedForSignalFailureRing,
       "farEndBERThresholdPassedForSignalFailureSpan": farEndBERThresholdPassedForSignalFailureSpan,
       "farEndBERThresholdPassedForSignalDegradeRing": farEndBERThresholdPassedForSignalDegradeRing,
       "farEndBERThresholdPassedForSignalDegradeSpan": farEndBERThresholdPassedForSignalDegradeSpan,
       "apsChannelFarEndProtectionLineSignalDegrade": apsChannelFarEndProtectionLineSignalDegrade,
       "ringSwitchIsActiveOnTheEastSide": ringSwitchIsActiveOnTheEastSide,
       "ringSwitchIsActiveOnTheWestSide": ringSwitchIsActiveOnTheWestSide,
       "spanSwitchIsActiveOnTheEastSide": spanSwitchIsActiveOnTheEastSide,
       "spanSwitchIsActiveOnTheWestSide": spanSwitchIsActiveOnTheWestSide,
       "uniDirectionalFullPassThroughIsActive": uniDirectionalFullPassThroughIsActive,
       "biDirectionalFullPassThroughIsActive": biDirectionalFullPassThroughIsActive,
       "kBytesPassThroughIsActive": kBytesPassThroughIsActive,
       "ringIsSegmented": ringIsSegmented,
       "ringTopologyIsUnderConstruction": ringTopologyIsUnderConstruction,
       "lockoutOfProtectionAllSpans": lockoutOfProtectionAllSpans,
       "farEndOfFiberIsProvisionedWithDifferentRingID": farEndOfFiberIsProvisionedWithDifferentRingID,
       "bothEndsOfFiberProvisionedAsEastOrBothAsWest": bothEndsOfFiberProvisionedAsEastOrBothAsWest,
       "securityInvalidLoginUsernameSeeAuditTrail": securityInvalidLoginUsernameSeeAuditTrail,
       "autonomousMessagesInhibited": autonomousMessagesInhibited,
       "trafficStormOnLANLANTemporarilyDisabled": trafficStormOnLANLANTemporarilyDisabled,
       "reptdbchgMessagesInhibited": reptdbchgMessagesInhibited,
       "securityUserIDHasExpired": securityUserIDHasExpired,
       "partialFanFailure": partialFanFailure,
       "forcedSwitchRequestOnRing": forcedSwitchRequestOnRing,
       "forcedSwitchRequestOnSpan": forcedSwitchRequestOnSpan,
       "lockoutSwitchRequestOnRing": lockoutSwitchRequestOnRing,
       "lockoutSwitchRequestOnSpan": lockoutSwitchRequestOnSpan,
       "manualSwitchRequestOnRing": manualSwitchRequestOnRing,
       "manualSwitchRequestOnSpan": manualSwitchRequestOnSpan,
       "communicationFailurePeerToPeerSlotControlBusA": communicationFailurePeerToPeerSlotControlBusA,
       "communicationFailurePeerToPeerSlotControlBusB": communicationFailurePeerToPeerSlotControlBusB,
       "controllerAToShelfSlotCommunicationFailure": controllerAToShelfSlotCommunicationFailure,
       "controllerBToShelfSlotCommunicationFailure": controllerBToShelfSlotCommunicationFailure,
       "interconnectionEquipmentFailureWorkingPayloadBus": interconnectionEquipmentFailureWorkingPayloadBus,
       "interconnectionEquipmentFailureProtectPayloadBus": interconnectionEquipmentFailureProtectPayloadBus,
       "inhibitSwitchToProtectRequestOnEquipment": inhibitSwitchToProtectRequestOnEquipment,
       "inhibitSwitchToWorkingRequestOnEquipment": inhibitSwitchToWorkingRequestOnEquipment,
       "berThresholdExceededForSignalDegradeLine": berThresholdExceededForSignalDegradeLine,
       "berThresholdExceededForSignalDegradePath": berThresholdExceededForSignalDegradePath,
       "berThresholdExceededForSignalFailureLine": berThresholdExceededForSignalFailureLine,
       "berThresholdExceededForSignalFailurePath": berThresholdExceededForSignalFailurePath,
       "exercisingRingSuccessfully": exercisingRingSuccessfully,
       "exercisingSpanSuccessfully": exercisingSpanSuccessfully,
       "spanIsInWaitToRestoreState": spanIsInWaitToRestoreState,
       "exerciseRequestOnRingFailed": exerciseRequestOnRingFailed,
       "exerciseRequestOnSpanFailed": exerciseRequestOnSpanFailed,
       "farEndLockoutOfProtectionSpan": farEndLockoutOfProtectionSpan,
       "manufacturingDataMemoryEEPROMFailure": manufacturingDataMemoryEEPROMFailure,
       "replaceableEquipmentOrUnitIsMissing": replaceableEquipmentOrUnitIsMissing,
       "softwareDownloadFailed": softwareDownloadFailed,
       "extraTrafficPCADropped": extraTrafficPCADropped,
       "etherTxOversubscribed": etherTxOversubscribed,
       "etherRxOverSubscribed": etherRxOverSubscribed,
       "etherTxExcessFlowCtrl": etherTxExcessFlowCtrl,
       "etherRxExcessFlowCtrl": etherRxExcessFlowCtrl,
       "transportLayerFailure": transportLayerFailure,
       "etherTxUnderrun": etherTxUnderrun,
       "synchronizationReferenceFrequencyOutOfBounds": synchronizationReferenceFrequencyOutOfBounds,
       "ntpOrSntpHostFailure": ntpOrSntpHostFailure,
       "peerCardNotResponding": peerCardNotResponding,
       "alarmsAndEventsSuppressedForThisObject": alarmsAndEventsSuppressedForThisObject,
       "ds3FrameFormatMismatch": ds3FrameFormatMismatch,
       "waitToRestore": waitToRestore,
       "extremeHighVoltBatteryA": extremeHighVoltBatteryA,
       "extremeLowVoltBatteryA": extremeLowVoltBatteryA,
       "extremeHighVoltBatteryB": extremeHighVoltBatteryB,
       "extremeLowVoltBatteryB": extremeLowVoltBatteryB,
       "iosConfigCopyFailed": iosConfigCopyFailed,
       "iosConfigCopyInProgress": iosConfigCopyInProgress,
       "iosConfigCopySuccess": iosConfigCopySuccess,
       "signalingUnableToSetupCircuit": signalingUnableToSetupCircuit,
       "errorInStartupConfig": errorInStartupConfig,
       "noStartupConfig": noStartupConfig,
       "needToSaveRunningConfig": needToSaveRunningConfig,
       "invalidAlarm": invalidAlarm,
       "rsvpHelloFSMToNeighborDown": rsvpHelloFSMToNeighborDown,
       "securityInvalidLoginUsername": securityInvalidLoginUsername,
       "databaseBackupFailed": databaseBackupFailed,
       "databaseRestoreFailed": databaseRestoreFailed,
       "lmpHelloFSMToControlChannelDown": lmpHelloFSMToControlChannelDown,
       "lmpNeighborDiscoveryHasFailed": lmpNeighborDiscoveryHasFailed,
       "unauthorizedIncomingSignalingRequest": unauthorizedIncomingSignalingRequest,
       "auditLog80PercentFull": auditLog80PercentFull,
       "moduleCommunicationFailure": moduleCommunicationFailure,
       "auditLog100PercentFullOldestRecordsWillBeLost": auditLog100PercentFullOldestRecordsWillBeLost,
       "standbyDatabaseOutOfSync": standbyDatabaseOutOfSync,
       "redundantPowerCapabilityLost": redundantPowerCapabilityLost,
       "forcedSwitchToPrimaryReference": forcedSwitchToPrimaryReference,
       "forcedSwitchToSecondReference": forcedSwitchToSecondReference,
       "forcedSwitchToThirdReference": forcedSwitchToThirdReference,
       "forcedSwitchToInternalClock": forcedSwitchToInternalClock,
       "industrialHighTemperature": industrialHighTemperature,
       "timSectionTraceIdentifierMismatchFailure": timSectionTraceIdentifierMismatchFailure,
       "aisMultiplexSectionAlarmIndicationSignal": aisMultiplexSectionAlarmIndicationSignal,
       "rdiMultiplexSectionRemoteDefectOrAlarmIndication": rdiMultiplexSectionRemoteDefectOrAlarmIndication,
       "timHighOrderTraceIdentifierMismatchFailure": timHighOrderTraceIdentifierMismatchFailure,
       "aisAdministrationUnitAlarmIndicationSignal": aisAdministrationUnitAlarmIndicationSignal,
       "lopAdministrationUnitLossOfPointer": lopAdministrationUnitLossOfPointer,
       "slmfUnequippedHighOrderPathUnequipped": slmfUnequippedHighOrderPathUnequipped,
       "slmfPLMHighOrderPathLabelMismatch": slmfPLMHighOrderPathLabelMismatch,
       "rdiHighOrderRemoteDefectOrAlarmIndication": rdiHighOrderRemoteDefectOrAlarmIndication,
       "lopTributaryUnitLossOfPointer": lopTributaryUnitLossOfPointer,
       "aisTributaryUnitAlarmIndicationSignal": aisTributaryUnitAlarmIndicationSignal,
       "slmfUnequippedLowOrderPathUnequipped": slmfUnequippedLowOrderPathUnequipped,
       "slmfPLMLowOrderPathLabelMismatch": slmfPLMLowOrderPathLabelMismatch,
       "timLowOrderTraceIdentifierMismatchFailure": timLowOrderTraceIdentifierMismatchFailure,
       "rfiLowOrderRemoteFailureOrAlarmIndication": rfiLowOrderRemoteFailureOrAlarmIndication,
       "g811PrimaryReferenceClockTraceable": g811PrimaryReferenceClockTraceable,
       "g812TransitNodeClockTraceable": g812TransitNodeClockTraceable,
       "g812LocalNodeClockTraceable": g812LocalNodeClockTraceable,
       "g813SynchronousEquipmentTimingSourceTraceable": g813SynchronousEquipmentTimingSourceTraceable,
       "e1LoopbackDueToFEACCommand": e1LoopbackDueToFEACCommand,
       "e1LoopbackCommandSentToFarEnd": e1LoopbackCommandSentToFarEnd,
       "e3LoopbackDueToFEACCommand": e3LoopbackDueToFEACCommand,
       "farEndMultipleE1LOSDetectedOnE3": farEndMultipleE1LOSDetectedOnE3,
       "farEndE1EqptFailNonServiceAffecting": farEndE1EqptFailNonServiceAffecting,
       "farEndE1EqptFailServiceAffecting": farEndE1EqptFailServiceAffecting,
       "farEndSingleE1LOS": farEndSingleE1LOS,
       "farEndE3EqptFailServiceAffecting": farEndE3EqptFailServiceAffecting,
       "e3LoopbackCommandSentToFarEnd": e3LoopbackCommandSentToFarEnd,
       "farEndE3EqptFailNonServiceAffecting": farEndE3EqptFailNonServiceAffecting,
       "lowVoltBatteryA": lowVoltBatteryA,
       "highVoltBatteryA": highVoltBatteryA,
       "lowVoltBatteryB": lowVoltBatteryB,
       "highVoltBatteryB": highVoltBatteryB,
       "msspRingOutOfSync": msspRingOutOfSync,
       "msspMultiNodeTableUpdateCompleted": msspMultiNodeTableUpdateCompleted,
       "automaticSNCPSwitchCausedByAIS": automaticSNCPSwitchCausedByAIS,
       "automaticSNCPSwitchCausedByLOP": automaticSNCPSwitchCausedByLOP,
       "automaticSNCPSwitchCausedByUNEQ": automaticSNCPSwitchCausedByUNEQ,
       "automaticSNCPSwitchCausedByPDI": automaticSNCPSwitchCausedByPDI,
       "automaticSNCPSwitchCausedBySFBER": automaticSNCPSwitchCausedBySFBER,
       "automaticSNCPSwitchCausedBySDBER": automaticSNCPSwitchCausedBySDBER,
       "stmConcatenationError": stmConcatenationError,
       "e3IdleCondition": e3IdleCondition,
       "channelMSSPInconsistentAPSCode": channelMSSPInconsistentAPSCode,
       "channelMSSPImproperAPSCodeAPS": channelMSSPImproperAPSCodeAPS,
       "channelMSSPNodeIdMismatchAPS": channelMSSPNodeIdMismatchAPS,
       "channelMSSPDefaultKAPS": channelMSSPDefaultKAPS,
       "channelMSSPConnectionLossAPS": channelMSSPConnectionLossAPS,
       "minimumClockTraceableSDH": minimumClockTraceableSDH,
       "lineIsInWaitToRestoreStateSDH": lineIsInWaitToRestoreStateSDH,
       "berThresholdExceededForSignalDegradeHighOrder": berThresholdExceededForSignalDegradeHighOrder,
       "berThresholdExceededForSignalFailureHighOrder": berThresholdExceededForSignalFailureHighOrder,
       "berThresholdExceededForSignalDegradeLowOrder": berThresholdExceededForSignalDegradeLowOrder,
       "berThresholdExceededForSignalFailureLowOrder": berThresholdExceededForSignalFailureLowOrder,
       "failureToSwitchToProtectionHighOrderPath": failureToSwitchToProtectionHighOrderPath,
       "failureToSwitchToProtectionLowOrderPath": failureToSwitchToProtectionLowOrderPath,
       "lofAdministrationUnitLossOfMultiFrame": lofAdministrationUnitLossOfMultiFrame,
       "sdhSpanIsInWaitToRestoreState": sdhSpanIsInWaitToRestoreState,
       "a8b10bOutOfSync": a8b10bOutOfSync,
       "odukPMAlarmIndicationSignal": odukPMAlarmIndicationSignal,
       "otukAlarmIndicationSignal": otukAlarmIndicationSignal,
       "otukSMBackwardDefectIndication": otukSMBackwardDefectIndication,
       "odukBackwardDefectIndication": odukBackwardDefectIndication,
       "fecUncorrectedWord": fecUncorrectedWord,
       "gccTerminationFailure": gccTerminationFailure,
       "otukIncomingAlignmentError": otukIncomingAlignmentError,
       "odukLockedDefectPM": odukLockedDefectPM,
       "lossOfMultiFrame": lossOfMultiFrame,
       "odukOpenConnectionIndication": odukOpenConnectionIndication,
       "payloadTypeIdentifierMismatch": payloadTypeIdentifierMismatch,
       "odukTrailTraceIdentifierMismatch": odukTrailTraceIdentifierMismatch,
       "otukTrailTraceIdentifierMismatch": otukTrailTraceIdentifierMismatch,
       "equipmentHighLaserBias": equipmentHighLaserBias,
       "equipmentHighLaserTemp": equipmentHighLaserTemp,
       "equipmentHighLaserPeltier": equipmentHighLaserPeltier,
       "facilityHighRxPower": facilityHighRxPower,
       "equipmentHighTxPower": equipmentHighTxPower,
       "equipmentHighTransceiverVoltage": equipmentHighTransceiverVoltage,
       "equipmentLowLaserBias": equipmentLowLaserBias,
       "equipmentLowLaserTemp": equipmentLowLaserTemp,
       "equipmentLowLaserPeltier": equipmentLowLaserPeltier,
       "facilityLowRxPower": facilityLowRxPower,
       "equipmentLowTxPower": equipmentLowTxPower,
       "equipmentLowTransceiverVoltage": equipmentLowTransceiverVoltage,
       "equipmentRxLocked": equipmentRxLocked,
       "equipmentSquelched": equipmentSquelched,
       "equipmentTxLocked": equipmentTxLocked,
       "otukSignalFailure": otukSignalFailure,
       "odukSignalFailure": odukSignalFailure,
       "otukSignalDegrade": otukSignalDegrade,
       "odukSignalDegrade": odukSignalDegrade,
       "pluggablePortMissing": pluggablePortMissing,
       "pluggablePortRateMismatch": pluggablePortRateMismatch,
       "pluggablePortSecurityCodeMismatch": pluggablePortSecurityCodeMismatch,
       "tciNotSelected": tciNotSelected,
       "tci1ClockFailure": tci1ClockFailure,
       "odukPMBackwardDefectIndication": odukPMBackwardDefectIndication,
       "odukTCM1BackwardDefectIndication": odukTCM1BackwardDefectIndication,
       "odukTCM2BackwardDefectIndication": odukTCM2BackwardDefectIndication,
       "equipmentHighRxTemperature": equipmentHighRxTemperature,
       "equipmentLowRxTemperature": equipmentLowRxTemperature,
       "tci2ClockFailure": tci2ClockFailure,
       "equipmentWavelengthMismatch": equipmentWavelengthMismatch,
       "dspCommunicationFailure": dspCommunicationFailure,
       "dspFailure": dspFailure,
       "laserApproachingEndOfLife": laserApproachingEndOfLife,
       "crossconnectLoopback": crossconnectLoopback,
       "adminLogoutOfUser": adminLogoutOfUser,
       "userLockedOut": userLockedOut,
       "adminLockoutOfUser": adminLockoutOfUser,
       "adminLockoutClear": adminLockoutClear,
       "invalidLoginUsername": invalidLoginUsername,
       "securityInvalidLoginPassword": securityInvalidLoginPassword,
       "securityInvalidLoginLockedOut": securityInvalidLoginLockedOut,
       "securityInvalidLoginAlreadyLoggedOn": securityInvalidLoginAlreadyLoggedOn,
       "loginOfUser": loginOfUser,
       "automaticLogoutOfIdleUser": automaticLogoutOfIdleUser,
       "logoutOfUser": logoutOfUser,
       "enhancedRemoteFailureIndicationPathServer": enhancedRemoteFailureIndicationPathServer,
       "enhancedRemoteFailureIndicationPathConnectivity": enhancedRemoteFailureIndicationPathConnectivity,
       "enhancedRemoteFailureIndicationPathPayload": enhancedRemoteFailureIndicationPathPayload,
       "firewallHasBeenDisabled": firewallHasBeenDisabled,
       "securityIntrusionDetPwd": securityIntrusionDetPwd,
       "securityIntrusionDetUser": securityIntrusionDetUser,
       "connectionEquipmentMismatch": connectionEquipmentMismatch,
       "disableInactiveUser": disableInactiveUser,
       "disableInactiveClear": disableInactiveClear,
       "batteryFailure": batteryFailure,
       "extremeHighVolt": extremeHighVolt,
       "extremeLowVolt": extremeLowVolt,
       "highVolt": highVolt,
       "lowVolt": lowVolt,
       "suspendUser": suspendUser,
       "suspendUserClear": suspendUserClear,
       "lineDccTerminationFailure": lineDccTerminationFailure,
       "multiplexSectionDccTerminationFailure": multiplexSectionDccTerminationFailure,
       "gigaBitEthernetOutOfSync": gigaBitEthernetOutOfSync,
       "sequenceMismatch": sequenceMismatch,
       "lossOfAlignment": lossOfAlignment,
       "outOfUseByAdministrativeCommand": outOfUseByAdministrativeCommand,
       "outOfUseTransportFailure": outOfUseTransportFailure,
       "vcatGroupDown": vcatGroupDown,
       "vcatGroupDegraded": vcatGroupDegraded,
       "vcatGroupIncomplete": vcatGroupIncomplete,
       "alarmIndicationSignalInTX": alarmIndicationSignalInTX,
       "remoteAlarmIndicationInTX": remoteAlarmIndicationInTX,
       "kByteAPSChannelFailure": kByteAPSChannelFailure,
       "apsInvalidMode": apsInvalidMode,
       "ipAddressAlreadyInUseWithinTheSameDccArea": ipAddressAlreadyInUseWithinTheSameDccArea,
       "nodeNameInUseWithinTheSameDccArea": nodeNameInUseWithinTheSameDccArea,
       "rearPanelEthernetLinkRemoved": rearPanelEthernetLinkRemoved,
       "manualSwitchToProtectResultedInNoTrafficSwitch": manualSwitchToProtectResultedInNoTrafficSwitch,
       "manualSwitchBackToWorkingResultedInNoTrafficSwitch": manualSwitchBackToWorkingResultedInNoTrafficSwitch,
       "forcedSwitchToProtectResultedInNoTrafficSwitch": forcedSwitchToProtectResultedInNoTrafficSwitch,
       "forcedSwitchBackToWorkingResultedInNoTrafficSwitch": forcedSwitchBackToWorkingResultedInNoTrafficSwitch,
       "duplicateSerialNumberDetectedOnAPluggableEntity": duplicateSerialNumberDetectedOnAPluggableEntity,
       "lossOfSignalForOpticalChannel": lossOfSignalForOpticalChannel,
       "encapsulationMismatchPath": encapsulationMismatchPath,
       "encapsulationMismatchVT": encapsulationMismatchVT,
       "encapsulationMismatchHighOrderPath": encapsulationMismatchHighOrderPath,
       "encapsulationMismatchLowOrderPath": encapsulationMismatchLowOrderPath,
       "gfpUserPayloadMismatch": gfpUserPayloadMismatch,
       "gfpFibreChannelDistanceExtensionMismatch": gfpFibreChannelDistanceExtensionMismatch,
       "gfpFibreChannelDistanceExtensionBufferStarvation": gfpFibreChannelDistanceExtensionBufferStarvation,
       "gfpFibreChannelDistanceExtensionCreditStarvation": gfpFibreChannelDistanceExtensionCreditStarvation,
       "automaticWdmAnsFinished": automaticWdmAnsFinished,
       "gfpClientSignalFailDetected": gfpClientSignalFailDetected,
       "gfpLossOfFrameDelineation": gfpLossOfFrameDelineation,
       "gfpExtensionHeaderMismatch": gfpExtensionHeaderMismatch,
       "incomingOverheadSignalAbsent": incomingOverheadSignalAbsent,
       "opticalSafetyRemoteInterlockOn": opticalSafetyRemoteInterlockOn,
       "automaticPowerControlCorrectionSkipped": automaticPowerControlCorrectionSkipped,
       "apcCannotSetValueDueToRangeLimits": apcCannotSetValueDueToRangeLimits,
       "lcasVcgMemberTxSideInAddState": lcasVcgMemberTxSideInAddState,
       "farEndManualSwitchBackToWorkingSpan": farEndManualSwitchBackToWorkingSpan,
       "farEndForcedSwitchBackToWorkingSpan": farEndForcedSwitchBackToWorkingSpan,
       "universalTransponderModuleHardwareFailure": universalTransponderModuleHardwareFailure,
       "universalTransponderModuleCommunicationFailure": universalTransponderModuleCommunicationFailure,
       "pluginModuleRangeSettingsMismatch": pluginModuleRangeSettingsMismatch,
       "lcasVcgMemberTxSideInDnuState": lcasVcgMemberTxSideInDnuState,
       "lcasControlWordCrcCheckFailure": lcasControlWordCrcCheckFailure,
       "lcasVcgMemberRxSideInFailState": lcasVcgMemberRxSideInFailState,
       "signalLossOnDataInterface": signalLossOnDataInterface,
       "synchronizationLossOnDataInterface": synchronizationLossOnDataInterface,
       "portFAIL": portFAIL,
       "unreachablePortTargetPower": unreachablePortTargetPower,
       "portAddPowerDegradeLow": portAddPowerDegradeLow,
       "portAddPowerDegradeHigh": portAddPowerDegradeHigh,
       "portAddPowerFailLow": portAddPowerFailLow,
       "portAddPowerFailHigh": portAddPowerFailHigh,
       "automaticPowerControlTerminatedOnManualRequest": automaticPowerControlTerminatedOnManualRequest,
       "oduk1AlarmIndicationSignal": oduk1AlarmIndicationSignal,
       "oduk2AlarmIndicationSignal": oduk2AlarmIndicationSignal,
       "oduk3AlarmIndicationSignal": oduk3AlarmIndicationSignal,
       "oduk4AlarmIndicationSignal": oduk4AlarmIndicationSignal,
       "temperatureReadingMismatchBetweenSCCards": temperatureReadingMismatchBetweenSCCards,
       "voltageReadingMismatchBetweenSCCards": voltageReadingMismatchBetweenSCCards,
       "alarmsSuppressedonOutOfGroupVcatMember": alarmsSuppressedonOutOfGroupVcatMember,
       "blsrSoftwareVersionMismatch": blsrSoftwareVersionMismatch,
       "optimized1Plus1ApsPrimaryFacility": optimized1Plus1ApsPrimaryFacility,
       "optimized1Plus1ApsPrimarySectionMismatch": optimized1Plus1ApsPrimarySectionMismatch,
       "optimized1Plus1ApsInvalidPrimarySection": optimized1Plus1ApsInvalidPrimarySection,
       "compositeClockHighLineVoltage": compositeClockHighLineVoltage,
       "berThresholdExceededForSignalDegradeVt": berThresholdExceededForSignalDegradeVt,
       "berThresholdExceededForSignalFailureVt": berThresholdExceededForSignalFailureVt,
       "spanLengthOutOfRange": spanLengthOutOfRange,
       "idleSignalCondition": idleSignalCondition,
       "idleSignalConditionInTx": idleSignalConditionInTx,
       "vtPathTraceIdentifierMismatch": vtPathTraceIdentifierMismatch,
       "lossOfFrameInTX": lossOfFrameInTX,
       "provisioningMismatch": provisioningMismatch,
       "sectionTraceIdentifierMismatch": sectionTraceIdentifierMismatch,
       "regeneratorSectionTraceIdentifierMismatch": regeneratorSectionTraceIdentifierMismatch,
       "switchingMatrixModuleFailureWorking": switchingMatrixModuleFailureWorking,
       "switchingMatrixModuleFailureProtect": switchingMatrixModuleFailureProtect,
       "slotCommunicationDisabled": slotCommunicationDisabled,
       "sessionTimeLimitExpired": sessionTimeLimitExpired,
       "userPasswordChangeRequired": userPasswordChangeRequired,
       "isisAdjacencyFailure": isisAdjacencyFailure,
       "msspSoftwareVersionMismatch": msspSoftwareVersionMismatch,
       "remoteAuthenticationFailSeeAuditLog": remoteAuthenticationFailSeeAuditLog,
       "ringIsSquelchingStsTraffic": ringIsSquelchingStsTraffic,
       "ringIsSquelchingVtTraffic": ringIsSquelchingVtTraffic,
       "archiveOfAuditLogFailed": archiveOfAuditLogFailed,
       "rprWrapped": rprWrapped,
       "shelfCommunicationFailure": shelfCommunicationFailure,
       "duplicatedShelfIdentifier": duplicatedShelfIdentifier,
       "softwareMismatch": softwareMismatch,
       "lmpFailure": lmpFailure,
       "opticalTerminationIncomplete": opticalTerminationIncomplete,
       "forwardDefectIndication": forwardDefectIndication,
       "payloadMissingIndication": payloadMissingIndication,
       "spanMeasurementCannotBePerformed": spanMeasurementCannotBePerformed,
       "ringIsSquelchingHighOrderTraffic": ringIsSquelchingHighOrderTraffic,
       "ringIsSquelchingLowOrderTraffic": ringIsSquelchingLowOrderTraffic,
       "badPacketCountExceedsThreshold": badPacketCountExceedsThreshold,
       "linkLayerKeepAliveFailure": linkLayerKeepAliveFailure,
       "autonegotiationRemoteFailureIndication": autonegotiationRemoteFailureIndication,
       "trailSignalFail": trailSignalFail,
       "ds1LoopbackCommandSentToFarEnd": ds1LoopbackCommandSentToFarEnd,
       "multiplexSectionSignalDegraded": multiplexSectionSignalDegraded,
       "multiplexSectionExcessiveErrors": multiplexSectionExcessiveErrors,
       "highOrderPathSignalDegraded": highOrderPathSignalDegraded,
       "highOrderPathExcessiveErrors": highOrderPathExcessiveErrors,
       "lowOrderPathSignalDegraded": lowOrderPathSignalDegraded,
       "lowOrderPathExcessiveErrors": lowOrderPathExcessiveErrors,
       "regeneratorSectionDccTerminationFailure": regeneratorSectionDccTerminationFailure,
       "networkMemoryPoolLow": networkMemoryPoolLow,
       "ospfRoutingTableOverflow": ospfRoutingTableOverflow,
       "autoLaserShutdownDisabled": autoLaserShutdownDisabled,
       "rprProtectionIsActive": rprProtectionIsActive,
       "maxRPRStationNumberExceeded": maxRPRStationNumberExceeded,
       "rprProtectionConfigurationMismatched": rprProtectionConfigurationMismatched,
       "reservedBandwidthLinkRateExceededOnRinglet0": reservedBandwidthLinkRateExceededOnRinglet0,
       "reservedBandwidthLinkRateExceededOnRinglet1": reservedBandwidthLinkRateExceededOnRinglet1,
       "rprInterfaceInPassThroughMode": rprInterfaceInPassThroughMode,
       "rprPeerNodeIsMissing": rprPeerNodeIsMissing,
       "rprRiFailure": rprRiFailure,
       "rprSignalFailure": rprSignalFailure,
       "rprSignalDegrade": rprSignalDegrade,
       "interlinkFailure": interlinkFailure,
       "apcWrongGain": apcWrongGain,
       "rprSpanMismatch": rprSpanMismatch,
       "efmRemoteFaultIndicationCriticalEvent": efmRemoteFaultIndicationCriticalEvent,
       "efmRemoteFaultIndicationDyingGasp": efmRemoteFaultIndicationDyingGasp,
       "efmRemoteFaultIndicationLinkFault": efmRemoteFaultIndicationLinkFault,
       "efmLinkMonitoringErroredSymbolPeriodEvent": efmLinkMonitoringErroredSymbolPeriodEvent,
       "efmLinkMonitoringErroredFrameEvent": efmLinkMonitoringErroredFrameEvent,
       "efmLinkMonitoringErroredFramePeriodEvent": efmLinkMonitoringErroredFramePeriodEvent,
       "efmLinkMonitoringErroredFrameSecondsSummary": efmLinkMonitoringErroredFrameSecondsSummary,
       "efmRemoteLoopbackRequestFailed": efmRemoteLoopbackRequestFailed,
       "fastAutomaticProtectionSwitching": fastAutomaticProtectionSwitching,
       "fastAutomaticProtectionSwitchingConfigMismatch": fastAutomaticProtectionSwitchingConfigMismatch,
       "lcasSinkGroupError": lcasSinkGroupError,
       "lcasVcgMemberRxSideInDnuState": lcasVcgMemberRxSideInDnuState,
       "fcDistanceExtFuncNotEstablished": fcDistanceExtFuncNotEstablished,
       "nonCiscoPPMInserted": nonCiscoPPMInserted,
       "unqualifiedPPMInserted": unqualifiedPPMInserted,
       "ftaMismatch": ftaMismatch,
       "cardPortsUnableToProvideProtection": cardPortsUnableToProvideProtection,
       "lmpSignalDegrade": lmpSignalDegrade,
       "lmpSignalFailure": lmpSignalFailure,
       "lmpUnallocatedDataLink": lmpUnallocatedDataLink,
       "frontPortLinkLoss": frontPortLinkLoss,
       "bertEnbl": bertEnbl,
       "bertSyncFail": bertSyncFail,
       "workQueueFull": workQueueFull,
       "equipmentPowerFailureAtConnectorA": equipmentPowerFailureAtConnectorA,
       "equipmentPowerFailureAtConnectorB": equipmentPowerFailureAtConnectorB,
       "equipmentPowerFailureAtReturnConnectorA": equipmentPowerFailureAtReturnConnectorA,
       "equipmentPowerFailureAtReturnConnectorB": equipmentPowerFailureAtReturnConnectorB,
       "bridgeAndRollHasOccurred": bridgeAndRollHasOccurred,
       "bridgeAndRollIsPendingAValidSignal": bridgeAndRollIsPendingAValidSignal,
       "clockBusFailureTscA": clockBusFailureTscA,
       "clockBusFailureTscB": clockBusFailureTscB,
       "ospfHelloFail": ospfHelloFail,
       "openIOSlots": openIOSlots,
       "lossOfClockFromMateShelfController": lossOfClockFromMateShelfController,
       "virtualLanAlarmIndicationSignal": virtualLanAlarmIndicationSignal,
       "dcuLossFailure": dcuLossFailure,
       "ochncMaintenance": ochncMaintenance,
       "ramanLaserShutdown": ramanLaserShutdown,
       "losOfRamanSignal": losOfRamanSignal,
       "mcastMacTableFull": mcastMacTableFull,
       "multicastMacAddressAliasing": multicastMacAddressAliasing,
       "ramanPwrProtOn": ramanPwrProtOn,
       "cppPeerNotResponding": cppPeerNotResponding,
       "voaControlLoopDisableDueToExcessiveCounterPropagationLight": voaControlLoopDisableDueToExcessiveCounterPropagationLight,
       "wizardIsRunning": wizardIsRunning,
       "ramanGainNotReached": ramanGainNotReached,
       "pprForwardDefectIndication": pprForwardDefectIndication,
       "pprBackwardDefectIndication": pprBackwardDefectIndication,
       "pprCoordinatedMaintenance": pprCoordinatedMaintenance,
       "pprTriggerThresholdBERExceeded": pprTriggerThresholdBERExceeded,
       "localFault": localFault,
       "remoteFault": remoteFault,
       "efmRemoteLoopbackConfigured": efmRemoteLoopbackConfigured,
       "efmPeerMissing": efmPeerMissing,
       "eqptDegrade": eqptDegrade,
       "excessiveBackPropagation": excessiveBackPropagation,
       "remoteMaintenanceEndPointIsDown": remoteMaintenanceEndPointIsDown,
       "crossConnectedCFMService": crossConnectedCFMService,
       "cfmLoop": cfmLoop,
       "cfmConfigurationError": cfmConfigurationError,
       "outOfChannelGroupBundle": outOfChannelGroupBundle,
       "repNeighborAdjacencyFailure": repNeighborAdjacencyFailure,
       "repLinkFlapping": repLinkFlapping,
       "faultInREPSegment": faultInREPSegment,
       "primaryREPEdgePortElected": primaryREPEdgePortElected,
       "secondaryREPEdgePortElected": secondaryREPEdgePortElected,
       "stcnREPGenerated": stcnREPGenerated,
       "vlbREPActivated": vlbREPActivated,
       "vlbREPTriggerSoakingDelayActive": vlbREPTriggerSoakingDelayActive,
       "wanSyncloss": wanSyncloss,
       "laserShutdownDueToWavelengthDrift": laserShutdownDueToWavelengthDrift,
       "manualLaserRestart": manualLaserRestart,
       "laserShutdownDueToNonCiscoPPMInserted": laserShutdownDueToNonCiscoPPMInserted,
       "ethernetOSCTerminationFailure": ethernetOSCTerminationFailure,
       "softwareSignatureVerificationFailed": softwareSignatureVerificationFailed,
       "protectVolumeSoftwareSignatureVerificationFailed": protectVolumeSoftwareSignatureVerificationFailed,
       "activeVolumeSoftwareSignatureVerificationFailed": activeVolumeSoftwareSignatureVerificationFailed,
       "peerPortClientSignalFailDetected": peerPortClientSignalFailDetected,
       "channelShutdownDueToWavelengthDrift": channelShutdownDueToWavelengthDrift,
       "usbWriteFailure": usbWriteFailure,
       "usbSyncInProgress": usbSyncInProgress,
       "autoSensingUnableToDetectValidPayload": autoSensingUnableToDetectValidPayload,
       "payloadAutoSensingInProgress": payloadAutoSensingInProgress,
       "gfpClientSignalFailDetectedDueToSigloss": gfpClientSignalFailDetectedDueToSigloss,
       "gfpClientSignalFailDetectedDueToSyncloss": gfpClientSignalFailDetectedDueToSyncloss,
       "pmdDegrade": pmdDegrade,
       "standbyTccNEClockIsInternalClock": standbyTccNEClockIsInternalClock,
       "chromaticDispersionValue": chromaticDispersionValue,
       "packetTransportServiceFailed": packetTransportServiceFailed,
       "satellitePanelDiscoveryFailure": satellitePanelDiscoveryFailure,
       "satellitePanelActiveLinkFailure": satellitePanelActiveLinkFailure,
       "satellitePanelCommunicationFailure": satellitePanelCommunicationFailure,
       "satellitePanelImproperConfiguration": satellitePanelImproperConfiguration,
       "satellitePanelFanMismatchOfEquipmentAndAttributes": satellitePanelFanMismatchOfEquipmentAndAttributes,
       "satellitePanelFanFailure": satellitePanelFanFailure,
       "satellitePanelPartialFanFailure": satellitePanelPartialFanFailure,
       "satellitePanelFANManufacturingDataMemoryEEPROMFailure": satellitePanelFANManufacturingDataMemoryEEPROMFailure,
       "satellitePanelFANUnitIsMissing": satellitePanelFANUnitIsMissing,
       "satellitePanelIndustrialHighTemperature": satellitePanelIndustrialHighTemperature,
       "satellitePanelHighTemperature": satellitePanelHighTemperature,
       "satellitePanelBatteryFailureA": satellitePanelBatteryFailureA,
       "plannedSwitchOver": plannedSwitchOver,
       "protectionCardConfigurationMismatch": protectionCardConfigurationMismatch,
       "routerProcessorSwitchOver": routerProcessorSwitchOver,
       "runningLowOnResources": runningLowOnResources,
       "noMoreResourcesAreAvailable": noMoreResourcesAreAvailable,
       "esmcFailure": esmcFailure,
       "licenseWillExpireWithin24Hours": licenseWillExpireWithin24Hours,
       "licenseWillExpireAnytimeAfter1DayButBefore14Days": licenseWillExpireAnytimeAfter1DayButBefore14Days,
       "licenseIsExpired": licenseIsExpired,
       "licenseCountViolation": licenseCountViolation,
       "temporaryLicenseIsInUse": temporaryLicenseIsInUse,
       "evaluationLicenseIsInUse": evaluationLicenseIsInUse,
       "licenseIsMissing": licenseIsMissing,
       "pseudowireDown": pseudowireDown,
       "workingPseudowireControlPlaneDown": workingPseudowireControlPlaneDown,
       "protectPseudowireControlPlaneDown": protectPseudowireControlPlaneDown,
       "workingPseudowireConnectivityCheckDown": workingPseudowireConnectivityCheckDown,
       "protectPseudowireConnectivityCheckDown": protectPseudowireConnectivityCheckDown,
       "pseudowireTrafficSwitchedToProtection": pseudowireTrafficSwitchedToProtection,
       "workingPseudowireLocalAcTxPortFault": workingPseudowireLocalAcTxPortFault,
       "protectPseudowireLocalAcTxPortFault": protectPseudowireLocalAcTxPortFault,
       "workingPseudowireLocalAcRxPortFault": workingPseudowireLocalAcRxPortFault,
       "protectPseudowireLocalAcRxPortFault": protectPseudowireLocalAcRxPortFault,
       "workingPseudowireRemoteAcTxPortFault": workingPseudowireRemoteAcTxPortFault,
       "protectPseudowireRemoteAcTxPortFault": protectPseudowireRemoteAcTxPortFault,
       "workingPseudowireRemoteAcRxPortFault": workingPseudowireRemoteAcRxPortFault,
       "protectPseudowireRemoteAcRxPortFault": protectPseudowireRemoteAcRxPortFault,
       "slaThresholdCrossAlert": slaThresholdCrossAlert,
       "protectLocalPseudowireNotForwarding": protectLocalPseudowireNotForwarding,
       "workingPseudowireNotForwarding": workingPseudowireNotForwarding,
       "protectPseudowireNotForwarding": protectPseudowireNotForwarding,
       "tpTunnelDown": tpTunnelDown,
       "workingLabelSwitchedPathDown": workingLabelSwitchedPathDown,
       "protectLabelSwitchedPathDown": protectLabelSwitchedPathDown,
       "workingLabelSwitchedPathAlarmIndicationSignal": workingLabelSwitchedPathAlarmIndicationSignal,
       "protectLabelSwitchedPathAlarmIndicationSignal": protectLabelSwitchedPathAlarmIndicationSignal,
       "workingLabelSwitchedPathRemoteDefectIndication": workingLabelSwitchedPathRemoteDefectIndication,
       "protectLabelSwitchedPathRemoteDefectIndication": protectLabelSwitchedPathRemoteDefectIndication,
       "bidirectionalForwardDetectionDown": bidirectionalForwardDetectionDown,
       "tpTrafficSwitchedFromWorkingToProtection": tpTrafficSwitchedFromWorkingToProtection,
       "workingTpLockout": workingTpLockout,
       "protectTpLockout": protectTpLockout,
       "ethernetFlowPointFailed": ethernetFlowPointFailed,
       "teTunnelDown": teTunnelDown,
       "macSystemLimitReached": macSystemLimitReached,
       "macBridgeDomainLimitReached": macBridgeDomainLimitReached,
       "autoSensingDisabled": autoSensingDisabled,
       "smBackwardIncomingAlignmentError": smBackwardIncomingAlignmentError,
       "resourceAllocationFailed": resourceAllocationFailed,
       "lossOfDFBSignal": lossOfDFBSignal,
       "workingLabelSwitchedPathLinkDownIndication": workingLabelSwitchedPathLinkDownIndication,
       "protectLabelSwitchedPathLinkDownIndication": protectLabelSwitchedPathLinkDownIndication,
       "workingLabelSwitchedPathLockReport": workingLabelSwitchedPathLockReport,
       "protectLabelSwitchedPathLockReport": protectLabelSwitchedPathLockReport,
       "satellitePanelBatteryFailureB": satellitePanelBatteryFailureB,
       "highBitErrorRate": highBitErrorRate,
       "backPanelFacilityLoopback": backPanelFacilityLoopback,
       "backPanelTerminalLoopback": backPanelTerminalLoopback,
       "trunkPayloadTypeMismatch": trunkPayloadTypeMismatch,
       "invalidMuxponderConfiguration": invalidMuxponderConfiguration,
       "coolingProfileMismatch": coolingProfileMismatch,
       "trunkOduAlarmIndicationSignal": trunkOduAlarmIndicationSignal,
       "companionCardMissing": companionCardMissing,
       "controlPlaneUnverifiedClearedAlarmsPresent": controlPlaneUnverifiedClearedAlarmsPresent,
       "powerConsumptionLimitHasCrossed": powerConsumptionLimitHasCrossed,
       "masterKeyExchangeFailed": masterKeyExchangeFailed,
       "unitHighTemperature": unitHighTemperature,
       "overTemperatureUnitProtected": overTemperatureUnitProtected,
       "seqMismatchCount": seqMismatchCount,
       "keyProgramOnAlteraFpgaFailed": keyProgramOnAlteraFpgaFailed,
       "duplicateNodeControllerDetected": duplicateNodeControllerDetected,
       "restorationInProg": restorationInProg,
       "ramanPumpsCalibrationProcedureIsRunning": ramanPumpsCalibrationProcedureIsRunning,
       "ramanPumpsCalibrationIsScheduledToRunInTheNextMinutes": ramanPumpsCalibrationIsScheduledToRunInTheNextMinutes,
       "odukTCM1AlarmIndicationSignal": odukTCM1AlarmIndicationSignal,
       "odukTCM2AlarmIndicationSignal": odukTCM2AlarmIndicationSignal,
       "odukLockedDefectTCM1": odukLockedDefectTCM1,
       "odukLockedDefectTCM2": odukLockedDefectTCM2,
       "otukLossOfFrame": otukLossOfFrame,
       "odukOpenConnectionIndicationTCM1": odukOpenConnectionIndicationTCM1,
       "odukOpenConnectionIndicationTCM2": odukOpenConnectionIndicationTCM2,
       "odukTrailTraceIdentifierMismatchTCM1": odukTrailTraceIdentifierMismatchTCM1,
       "odukTrailTraceIdentifierMismatchTCM2": odukTrailTraceIdentifierMismatchTCM2,
       "odukSignalFailureTCM1": odukSignalFailureTCM1,
       "odukSignalFailureTCM2": odukSignalFailureTCM2,
       "odukSignalDegradeTCM1": odukSignalDegradeTCM1,
       "odukSignalDegradeTCM2": odukSignalDegradeTCM2,
       "lossOfChannel": lossOfChannel,
       "fecMismatch": fecMismatch,
       "timSectionMonitorTraceIdentifierMismatchFailure": timSectionMonitorTraceIdentifierMismatchFailure,
       "automaticLaserShutdown": automaticLaserShutdown,
       "shutterInsertionLossVariationDegradeLow": shutterInsertionLossVariationDegradeLow,
       "opticalChannelDeactivationFailure": opticalChannelDeactivationFailure,
       "shutterInsertionLossVariationDegradeHigh": shutterInsertionLossVariationDegradeHigh,
       "networkTopologyIncomplete": networkTopologyIncomplete,
       "pluginModuleCommunicationFailure": pluginModuleCommunicationFailure,
       "opticalNetworkTypeMismatch": opticalNetworkTypeMismatch,
       "opticalPowerDegradeLow": opticalPowerDegradeLow,
       "automaticPowerControlFailure": automaticPowerControlFailure,
       "opticalPowerDegradeHigh": opticalPowerDegradeHigh,
       "automaticPowerControlDisabled": automaticPowerControlDisabled,
       "opticalPowerFailureLow": opticalPowerFailureLow,
       "ringIdMismatch": ringIdMismatch,
       "opticalPowerFailureHigh": opticalPowerFailureHigh,
       "lossOfContinuity": lossOfContinuity,
       "variableOpticalAttenuatorDegradeLow": variableOpticalAttenuatorDegradeLow,
       "variableOpticalAttenuatorDegradeHigh": variableOpticalAttenuatorDegradeHigh,
       "variableOpticalAttenuatorFailureLow": variableOpticalAttenuatorFailureLow,
       "variableOpticalAttenuatorFailureHigh": variableOpticalAttenuatorFailureHigh,
       "laserBiasDegrade": laserBiasDegrade,
       "laserBiasFailure": laserBiasFailure,
       "laserTemperatureDegrade": laserTemperatureDegrade,
       "opticalAmplifierGainDegradeLow": opticalAmplifierGainDegradeLow,
       "opticalAmplifierGainDegradeHigh": opticalAmplifierGainDegradeHigh,
       "opticalAmplifierGainFailureLow": opticalAmplifierGainFailureLow,
       "opticalAmplifierGainFailureHigh": opticalAmplifierGainFailureHigh,
       "opticalChannelConnectionFailure": opticalChannelConnectionFailure,
       "opticalChannelIncomplete": opticalChannelIncomplete,
       "opticalChannelActivationFailure": opticalChannelActivationFailure,
       "laserAutoPowerReduction": laserAutoPowerReduction,
       "caseTemperatureDegrade": caseTemperatureDegrade,
       "fiberTemperatureDegrade": fiberTemperatureDegrade,
       "shutterOpen": shutterOpen,
       "awgTemperatureDegrade": awgTemperatureDegrade,
       "awgTemperatureFailure": awgTemperatureFailure,
       "awgOverTemperature": awgOverTemperature,
       "opticalAmplifierInitialization": opticalAmplifierInitialization,
       "awgWarmUp": awgWarmUp,
       "incSigloss": incSigloss,
       "incSyncloss": incSyncloss,
       "incGfpOutOfFrame": incGfpOutOfFrame,
       "incGfpSigLoss": incGfpSigLoss,
       "incGfpSyncLoss": incGfpSyncLoss,
       "cerentCommonObjects": cerentCommonObjects,
       "cerent454CommonObjectsGroup": cerent454CommonObjectsGroup,
       "cerent454EnableNotification": cerent454EnableNotification,
       "cerent454NodeTime": cerent454NodeTime,
       "cerent454SentNotifications": cerent454SentNotifications,
       "cerent454LastChangeTime": cerent454LastChangeTime,
       "cerent454MultishelfEnabled": cerent454MultishelfEnabled,
       "cerentCommonEvents": cerentCommonEvents}
)
