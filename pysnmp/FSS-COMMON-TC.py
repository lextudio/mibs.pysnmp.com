# SNMP MIB module (FSS-COMMON-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FSS-COMMON-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:39 2024
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

(fssCommon,) = mibBuilder.importSymbols(
    "FSS-COMMON-SMI",
    "fssCommon")

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

fcTc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1)
)
fcTc.setRevisions(
        ("2016-01-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FCSeverity(Integer32, TextualConvention):
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
              9999)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("indeterminate", 7),
          ("major", 2),
          ("minor", 3),
          ("na", 0),
          ("not-alarmed", 4),
          ("not-reported", 5),
          ("other", 9999),
          ("warning", 6))
    )



class FCCondEffect(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("cl", 1),
          ("na", 0),
          ("other", 9999),
          ("sc", 2),
          ("tc", 3))
    )



class FCServEffect(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("nsa", 2),
          ("other", 9999),
          ("sa", 1))
    )



class FCLocation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("fend", 2),
          ("na", 0),
          ("nend", 1),
          ("other", 9999))
    )



class FCDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("other", 9999),
          ("receive", 1),
          ("transmit", 2))
    )



class FCTimePeriod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("hr-24", 2),
          ("min-15", 1),
          ("month-1", 4),
          ("na", 0),
          ("other", 9999),
          ("week-1", 3))
    )



class FCTrapType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("cond", 1),
          ("dbchg", 3),
          ("na", 0),
          ("other", 9999),
          ("tca", 2))
    )



class FCObjectName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )



class FCCondType(Integer32, TextualConvention):
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
              17,
              18,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              200,
              201,
              300,
              301,
              302,
              303,
              305,
              306,
              307,
              308,
              350,
              351,
              352,
              400,
              450,
              451,
              452,
              470,
              500,
              600,
              601,
              602,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008,
              1009,
              1010,
              1011,
              1012,
              1013,
              1014,
              1015,
              1016,
              1017,
              1018,
              1019,
              1020,
              1021,
              1022,
              1023,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1033,
              1034,
              1035,
              1036,
              1037,
              1038,
              1039,
              1040,
              1041,
              1042,
              1043,
              1044,
              1045,
              1046,
              1047,
              1048,
              1049,
              1050,
              1051,
              1052,
              1053,
              1054,
              1055,
              1056,
              1057,
              1058,
              1059,
              1060,
              1061,
              1062,
              1063,
              1064,
              1065,
              1066,
              1067,
              1068,
              1069,
              1070,
              1071,
              1072,
              1073,
              1074,
              1075,
              1076,
              1077,
              1078,
              1079,
              1080,
              1081,
              1082,
              1083,
              1084,
              1500,
              1600,
              1700)
        )
    )
    namedValues = NamedValues(
        *(("administrativeDown", 6),
          ("administrativeTesting", 7),
          ("alarmIndicationSignal", 1012),
          ("autoPowerReduction", 1081),
          ("backwardDefectIndication", 1006),
          ("backwardIncomingAlignmentError", 1010),
          ("certificateNotInstalled", 470),
          ("clientSignalFailDefect", 1017),
          ("cnLossOfSynchronization", 1022),
          ("cnOutOfRange", 1021),
          ("configurationStandBy", 10),
          ("databaseCorruption", 100),
          ("databaseLockedDbAlarmPresent", 104),
          ("databaseLockedDbRestoreInProgress", 102),
          ("databaseLockedIlfViolation", 105),
          ("databaseLockedShelfProvModePresent", 106),
          ("databaseLockedSoftwareUpgradeInProgress", 101),
          ("databaseLockedSysInitInProgress", 103),
          ("databaseSystemSignatureMismatch", 108),
          ("databaseVersionMismatch", 107),
          ("dipSessionActive", 1500),
          ("equipmentCurrExceededFeed", 15),
          ("equipmentFault", 1),
          ("equipmentInterConnectFailure", 12),
          ("equipmentLedOn", 5),
          ("equipmentMiscabledConnection", 13),
          ("equipmentMismatchAttributes", 3),
          ("equipmentOverTemperature", 1052),
          ("equipmentRemoved", 2),
          ("equipmentWarmup", 4),
          ("facilityLoopback2Active", 1034),
          ("facilityLoopbackActive", 1033),
          ("facilityTestsignalActive", 1036),
          ("fanCoolingFail", 14),
          ("fanFilterShouldBeCleaned", 1051),
          ("fanFilterShouldBeReplaced", 1050),
          ("firmwareBackwardCompatibleAll", 303),
          ("firmwareBackwardCompatibleLimited", 302),
          ("firmwareDownloadOrActivationFailure", 305),
          ("firmwareInitInProgress", 301),
          ("firmwareVersionMismatch", 300),
          ("forwardDefectIndication", 1007),
          ("generalCommunicationChannel0Failure", 500),
          ("highBER", 1023),
          ("ilfViolation", 350),
          ("ilfViolationCritical", 351),
          ("ilfViolationMajor", 352),
          ("incomingAlignmentError", 1011),
          ("incompatibleFirmware", 306),
          ("incompatibleHardware", 307),
          ("incompatibleSffHardware", 9),
          ("interConnectFailure", 451),
          ("interConnectFailureBladePiu", 16),
          ("lampTest", 17),
          ("lanTransmitLocalFault", 1030),
          ("lanTransmitOff", 1032),
          ("lanTransmitRemoteFault", 1031),
          ("linkDown", 1038),
          ("lldpFail", 1700),
          ("localFault", 1024),
          ("locked", 1014),
          ("lossOfAlignment", 1026),
          ("lossOfFECAlignment", 1028),
          ("lossOfFrame", 1004),
          ("lossOfFrameAndLossOfMultiframe", 1020),
          ("lossOfMultiframe", 1005),
          ("lossOfOmfIndication", 1019),
          ("lossOfSignal", 1003),
          ("lossOfSynchronization", 1027),
          ("lossofTandemConnection", 1015),
          ("manualOverrideActive", 1070),
          ("modeMismatch", 1076),
          ("multiplexStructureIdentifierMismatch", 1018),
          ("noFirmware", 308),
          ("omsPowerOutOfSpecificationHigh", 1077),
          ("omsPowerOutOfSpecificationLow", 1078),
          ("openConnectionIndication", 1013),
          ("opticalPowerReceive", 1001),
          ("opticalPowerTransmit", 1002),
          ("oscControlFailure", 1075),
          ("oscPowerOutOfSpecificationHigh", 1073),
          ("oscPowerOutOfSpecificationLow", 1074),
          ("otdrScanInProgress", 18),
          ("otsSpanlossPowerOutOfSpecificationHigh", 1079),
          ("otsSpanlossPowerOutOfSpecificationLow", 1080),
          ("overTemperatureEquipment", 8),
          ("pPPFailure", 1600),
          ("payloadMismatch", 1016),
          ("payloadMissingIndication", 1069),
          ("portLossOfLight", 1053),
          ("postBlockAutoLaserShutdown", 1064),
          ("postBlockAutoPowerReduction", 1065),
          ("postBlockAutoShutoffDisabled", 1082),
          ("postBlockManualLaserShutdown", 1066),
          ("postBlockSpanAdjustmentInProgress", 1068),
          ("powerOutOfSpecification", 1039),
          ("powerOutOfSpecificationHigh", 1040),
          ("powerOutOfSpecificationHighL1", 1041),
          ("powerOutOfSpecificationHighL2", 1042),
          ("powerOutOfSpecificationHighL3", 1043),
          ("powerOutOfSpecificationHighL4", 1044),
          ("powerOutOfSpecificationLow", 1045),
          ("powerOutOfSpecificationLowL1", 1046),
          ("powerOutOfSpecificationLowL2", 1047),
          ("powerOutOfSpecificationLowL3", 1048),
          ("powerOutOfSpecificationLowL4", 1049),
          ("powerProblem", 600),
          ("powerProblemA", 601),
          ("powerProblemB", 602),
          ("preBlockSpanAdjustmentInProgress", 1067),
          ("prod-specific", 0),
          ("reflectionTooHigh", 1072),
          ("remoteFault", 1025),
          ("remoteLANFault", 1029),
          ("shelfProvisioningMode", 11),
          ("signalDegrade", 1008),
          ("softwareReset", 400),
          ("softwareStageInProgress", 201),
          ("softwareVersionMismatch", 200),
          ("sysNameChanged", 452),
          ("sysNtpNotSynchronized", 450),
          ("terminalLoopbackActive", 1035),
          ("terminalTestsignalActive", 1037),
          ("thresholdCrossingAlertOpticalReceivePowerTooHigh", 1060),
          ("thresholdCrossingAlertOpticalReceivePowerTooLow", 1061),
          ("thresholdCrossingAlertOpticalTransmitPowerTooHigh", 1062),
          ("thresholdCrossingAlertOpticalTransmitPowerTooLow", 1063),
          ("thresholdCrossingAlertOscOpticalReceivePowerTooHigh", 1056),
          ("thresholdCrossingAlertOscOpticalReceivePowerTooLow", 1057),
          ("thresholdCrossingAlertOscOpticalTransmitPowerTooHigh", 1058),
          ("thresholdCrossingAlertOscOpticalTransmitPowerTooLow", 1059),
          ("thresholdCrossingAlertSpanlossVariationTooHigh", 1055),
          ("thresholdCrossingAlertSpanlossVariationTooLow", 1054),
          ("totalpowerOutOfSpecificationHigh", 1083),
          ("totalpowerOutOfSpecificationLow", 1084),
          ("trailTraceMismatch", 1009),
          ("unequippedIndication", 1071))
    )



class FCTcCondType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10001,
              10002,
              10003,
              10004,
              10005,
              10100,
              10101,
              10102,
              10200,
              10201,
              10202,
              10300,
              10301,
              10302,
              10303,
              10304,
              10305,
              10306,
              10307,
              10308,
              10400,
              10401,
              10500,
              10501,
              10600,
              10601,
              10602,
              10603,
              10700,
              10701,
              10702,
              10703,
              10704,
              10705,
              10800,
              10801,
              10900,
              10901,
              10902,
              10903,
              10904,
              10905,
              10906,
              11000,
              11001,
              11002,
              11003,
              11004,
              11100,
              11101,
              11102,
              11200,
              11300,
              11301)
        )
    )
    namedValues = NamedValues(
        *(("autoLogoffAssociationCancellation", 11000),
          ("autoLogoffCableDisconnect", 11002),
          ("autoLogoffPasswordChanged", 11003),
          ("autoLogoffSessionTimeout", 11001),
          ("cancelValidationTimerComplete", 10305),
          ("cancelValidationTimerFailed", 10306),
          ("cancelValidationTimerInProgress", 10304),
          ("copyFileComplete", 10701),
          ("copyFileFailure", 10702),
          ("copyFileFailureMd5check", 10704),
          ("copyFileFailureTransfer", 10703),
          ("copyFileFailureVerification", 10705),
          ("copyFileInProgress", 10700),
          ("databaseActivation", 10100),
          ("databaseActivationFailure", 10101),
          ("databaseActivationReversion", 10102),
          ("dateTimeModified", 10401),
          ("daylightSavingTimeAdjustment", 10400),
          ("entityOperStatusChangeToDormant", 10904),
          ("entityOperStatusChangeToDown", 10901),
          ("entityOperStatusChangeToLowerLayerDown", 10906),
          ("entityOperStatusChangeToNotPresent", 10905),
          ("entityOperStatusChangeToTesting", 10902),
          ("entityOperStatusChangeToUnknown", 10903),
          ("entityOperStatusChangeToUp", 10900),
          ("equipmentPlugin", 10800),
          ("equipmentPlugout", 10801),
          ("firmwareActivation", 10200),
          ("firmwareActivationComplete", 10201),
          ("firmwareActivationFailure", 10202),
          ("forcedLogoff", 11004),
          ("ipNotReachable", 11100),
          ("ipPingRequestTimedOut", 11102),
          ("ipReachable", 11101),
          ("lldpNbrInfoChanged", 11200),
          ("manualSwitch", 10001),
          ("otdrScanComplete", 11300),
          ("otdrScanFailure", 11301),
          ("prod-specific", 0),
          ("softwareActivation", 10300),
          ("softwareActivationComplete", 10301),
          ("softwareActivationFailure", 10302),
          ("softwareFailOver", 10308),
          ("softwareReversion", 10303),
          ("sysNtpSwitchOver", 10501),
          ("sysNtpSynchronized", 10500),
          ("systemRestartCold", 10600),
          ("systemRestartDbInitialization", 10602),
          ("systemRestartShfprov", 10603),
          ("systemRestartWarm", 10601),
          ("uBootFailOver", 10307),
          ("workingSwitchProtection", 10002),
          ("workingSwitchProtectionForced", 10004),
          ("workingSwitchProtectionManual", 10003),
          ("workingSwitchWorking", 10005))
    )



class FCTcaCondType(Integer32, TextualConvention):
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
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213)
        )
    )
    namedValues = NamedValues(
        *(("prod-specific", 0),
          ("tCABackgroundBlockErrors", 210),
          ("tCACodingViolations", 204),
          ("tCADelayMeasurement", 211),
          ("tCAErroredBlocks", 213),
          ("tCAErroredSeconds", 205),
          ("tCAFECCorrectedBits", 208),
          ("tCAFECCorrectedCodewords", 201),
          ("tCAFECCorrectedSymbols", 203),
          ("tCAFECUncorrectedBlocks", 207),
          ("tCAFECUncorrectedCodewords", 202),
          ("tCALaserBiasCurrentLane1TooHigh", 10),
          ("tCALaserBiasCurrentLane2TooHigh", 15),
          ("tCALaserBiasCurrentLane3TooHigh", 20),
          ("tCALaserBiasCurrentLane4TooHigh", 25),
          ("tCALaserBiasCurrentTooHigh", 5),
          ("tCAOpticalReceivePowerLane1TooHigh", 7),
          ("tCAOpticalReceivePowerLane1TooLow", 6),
          ("tCAOpticalReceivePowerLane2TooHigh", 12),
          ("tCAOpticalReceivePowerLane2TooLow", 11),
          ("tCAOpticalReceivePowerLane3TooHigh", 17),
          ("tCAOpticalReceivePowerLane3TooLow", 16),
          ("tCAOpticalReceivePowerLane4TooHigh", 22),
          ("tCAOpticalReceivePowerLane4TooLow", 21),
          ("tCAOpticalReceivePowerOscTooHigh", 31),
          ("tCAOpticalReceivePowerOscTooLow", 30),
          ("tCAOpticalReceivePowerTooHigh", 2),
          ("tCAOpticalReceivePowerTooLow", 1),
          ("tCAOpticalTransmitPowerLane1TooHigh", 9),
          ("tCAOpticalTransmitPowerLane1TooLow", 8),
          ("tCAOpticalTransmitPowerLane2TooHigh", 14),
          ("tCAOpticalTransmitPowerLane2TooLow", 13),
          ("tCAOpticalTransmitPowerLane3TooHigh", 19),
          ("tCAOpticalTransmitPowerLane3TooLow", 18),
          ("tCAOpticalTransmitPowerLane4TooHigh", 24),
          ("tCAOpticalTransmitPowerLane4TooLow", 23),
          ("tCAOpticalTransmitPowerOscTooHigh", 33),
          ("tCAOpticalTransmitPowerOscTooLow", 32),
          ("tCAOpticalTransmitPowerTooHigh", 4),
          ("tCAOpticalTransmitPowerTooLow", 3),
          ("tCASDFECCorrectedBits", 209),
          ("tCASeverelyErroredSeconds", 206),
          ("tCASpanlossVariationTooHigh", 29),
          ("tCASpanlossVariationTooLow", 28),
          ("tCATotalOpticalReceivePowerTooHigh", 27),
          ("tCATotalOpticalReceivePowerTooLow", 26),
          ("tCAUnavailableSeconds", 212))
    )



class FCStdObjectIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class FCStdTypeIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class FCTrapHistIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class FCMonType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("prod-specific", 0)
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSS-COMMON-TC",
    **{"FCSeverity": FCSeverity,
       "FCCondEffect": FCCondEffect,
       "FCServEffect": FCServEffect,
       "FCLocation": FCLocation,
       "FCDirection": FCDirection,
       "FCTimePeriod": FCTimePeriod,
       "FCTrapType": FCTrapType,
       "FCObjectName": FCObjectName,
       "FCCondType": FCCondType,
       "FCTcCondType": FCTcCondType,
       "FCTcaCondType": FCTcaCondType,
       "FCStdObjectIndex": FCStdObjectIndex,
       "FCStdTypeIndex": FCStdTypeIndex,
       "FCTrapHistIndex": FCTrapHistIndex,
       "FCMonType": FCMonType,
       "fcTc": fcTc}
)
