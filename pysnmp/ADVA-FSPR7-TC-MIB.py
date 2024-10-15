# SNMP MIB module (ADVA-FSPR7-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADVA-FSPR7-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:41 2024
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

(fspR7,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fspR7")

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

advaFspR7Tc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 8)
)
advaFspR7Tc.setRevisions(
        ("2014-10-15 00:00",
         "2014-09-29 00:00",
         "2013-12-04 00:00",
         "2013-08-20 00:00",
         "2011-05-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ApsRevertMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2),
          ("undefined", 0))
    )



class ApsRevertModeCaps(Bits, TextualConvention):
    status = "current"


class ApsType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("eth", 6),
          ("ethSncI", 13),
          ("ethSncN", 14),
          ("ethSncS", 15),
          ("ethSncT", 16),
          ("line", 2),
          ("mux", 11),
          ("path", 20),
          ("pcs", 12),
          ("phys", 7),
          ("sncI", 4),
          ("sncISM", 10),
          ("sncN", 3),
          ("sncNLine", 18),
          ("sncNPM", 8),
          ("sncNPath", 19),
          ("sncNTCM", 9),
          ("sncS", 5),
          ("undefined", 0))
    )



class ApsTypeCaps(Bits, TextualConvention):
    status = "current"


class ConnectionNotation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fromToNotation", 1),
          ("toFromNotation", 2),
          ("undefined", 0))
    )



class Counter64StringCaps(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class EntityClassName(Integer32, TextualConvention):
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
              34,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              46,
              47,
              49,
              57,
              58,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              72,
              73,
              74,
              75,
              105,
              106,
              111,
              116,
              118,
              119,
              141,
              144,
              145,
              146)
        )
    )
    namedValues = NamedValues(
        *(("ch", 16),
          ("conn", 42),
          ("crsCh", 47),
          ("crsDcn", 46),
          ("ech", 69),
          ("eoc", 29),
          ("eth", 57),
          ("fan", 11),
          ("fanc", 10),
          ("fc", 146),
          ("fch", 64),
          ("fcu", 4),
          ("fcuc", 3),
          ("ffpCh", 43),
          ("ffpOm", 44),
          ("ffpVch1", 119),
          ("fpl", 13),
          ("gcc0", 30),
          ("gcc1", 31),
          ("gcc2", 32),
          ("lan", 41),
          ("ldcc", 27),
          ("link", 34),
          ("mod", 6),
          ("modc", 5),
          ("ne", 1),
          ("ol", 14),
          ("om", 15),
          ("otl", 37),
          ("otlg", 74),
          ("owlg", 75),
          ("pc", 141),
          ("pch", 17),
          ("pdcc", 28),
          ("pl", 9),
          ("plc", 8),
          ("psh", 7),
          ("ptp", 12),
          ("rat", 105),
          ("sc", 33),
          ("sdcc", 26),
          ("sh", 40),
          ("shelf", 2),
          ("sts1", 19),
          ("sts24c", 21),
          ("sts3c", 20),
          ("sts48c", 22),
          ("tc", 106),
          ("tifi", 38),
          ("tifo", 39),
          ("uch", 145),
          ("undefined", 0),
          ("vc3", 23),
          ("vc4", 24),
          ("vc4c16", 66),
          ("vc4c8", 65),
          ("vch", 18),
          ("vch1", 118),
          ("vconn", 73),
          ("vech", 72),
          ("veth", 58),
          ("vom", 116),
          ("vs0", 67),
          ("vs1", 25),
          ("vsch", 68),
          ("vsffpCh", 111),
          ("vtp", 70),
          ("wch", 49),
          ("whitelist", 144))
    )



class EntityType(Integer32, TextualConvention):
    status = "current"


class EquipmentState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equipped", 1),
          ("undefined", 0),
          ("unequipped", 2))
    )



class FfpType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forced", 2),
          ("normal", 1),
          ("undefined", 0))
    )



class FfpTypeCaps(Bits, TextualConvention):
    status = "current"


class Grade(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("gradeA", 1),
          ("gradeB", 2),
          ("gradeC", 4),
          ("gradeGdps", 3),
          ("undefined", 0))
    )



class FspR7AdminState(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("ains", 3),
          ("dsbld", 6),
          ("is", 2),
          ("mgt", 4),
          ("mt", 5),
          ("pps", 7),
          ("uas", 1),
          ("undefined", 0))
    )



class FspR7AdminStateCaps(Bits, TextualConvention):
    status = "current"


class FspR7AidType(Integer32, TextualConvention):
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
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("ch", 4),
          ("dcn", 5),
          ("eqpt", 3),
          ("lif", 17),
          ("lifCp", 18),
          ("none", 1),
          ("ol", 6),
          ("om", 7),
          ("otl", 22),
          ("sh", 16),
          ("sts1", 8),
          ("sts24c", 10),
          ("sts3c", 9),
          ("sts48c", 11),
          ("sys", 2),
          ("tnlEth", 24),
          ("tnlOtn", 25),
          ("tnlWdm", 19),
          ("undefined", 0),
          ("vc3", 12),
          ("vc4", 13),
          ("vc4c16", 21),
          ("vc4c8", 20),
          ("vs1", 14),
          ("vs4c", 15))
    )



class FspR7AlarmListType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
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
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              92,
              93,
              94,
              95,
              96,
              97,
              99,
              100,
              101,
              103,
              104,
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
              118,
              119,
              120,
              122,
              123,
              125,
              127,
              128,
              129,
              131,
              132,
              133,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              148,
              149,
              150,
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
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              197,
              198,
              199,
              200,
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
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              272,
              274,
              276,
              277,
              278,
              279,
              280,
              281,
              283,
              285,
              287,
              289,
              291,
              293,
              294,
              295,
              296,
              297,
              298,
              300,
              301,
              302,
              304,
              306,
              308,
              310,
              311,
              313,
              315,
              317,
              319,
              321,
              323,
              325,
              327,
              329,
              330,
              331,
              332,
              333,
              334,
              335,
              336,
              337,
              338,
              339,
              340,
              341,
              342,
              343,
              344,
              345,
              346,
              347,
              348,
              350,
              352,
              354,
              356,
              358,
              360,
              362,
              364,
              366,
              367,
              368,
              369,
              370,
              371,
              373,
              375,
              377,
              379,
              381,
              383,
              385,
              386,
              387,
              389,
              390,
              391,
              392,
              393,
              394,
              395,
              396,
              397,
              398,
              399,
              400,
              401,
              402,
              403,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              420,
              422,
              423,
              424,
              432,
              434,
              435)
        )
    )
    namedValues = NamedValues(
        *(("alarmIndicationSignalHigherOrderPath", 70),
          ("alarmIndicationSignalLine", 65),
          ("alarmIndicationSignalLowerOrderPath", 66),
          ("alarmIndicationSignalOdu", 67),
          ("alarmIndicationSignalOduTcmA", 71),
          ("alarmIndicationSignalOduTcmB", 72),
          ("alarmIndicationSignalOduTcmC", 73),
          ("alarmIndicationSignalOpu", 68),
          ("alarmIndicationSignalOtu", 69),
          ("alarmInputTIF", 387),
          ("ampFailure", 34),
          ("amplifierAbnormal", 75),
          ("apsConfigMismatch", 80),
          ("apsProtocolFailure", 81),
          ("aseLow", 82),
          ("aseTableBuild", 166),
          ("aseTableGenFailHighBackreflection", 84),
          ("aseTableGenFailLow", 83),
          ("aseTableGenFailOscMissing", 85),
          ("aseTableGenFailPilot", 86),
          ("aseTableGenFailSignalinput", 87),
          ("aseTableGenProgress", 89),
          ("aseTableNotAvailable", 88),
          ("attOnReceiverFiberHigherThanMonitor", 277),
          ("attOnReceiverFiberLowerThanMonitor", 278),
          ("attOnTransmitterFiberHigherThanMonitor", 279),
          ("attOnTransmitterFiberLowerThanMonitor", 280),
          ("autoAmpShutdown", 164),
          ("autoPowerShutdown", 25),
          ("autoShutdownAls", 163),
          ("autoShutdownAmpAps", 165),
          ("autoShutdownBlock", 24),
          ("autoShutdownGAis", 422),
          ("autoShutdownLaserOffDueToErrFwd", 171),
          ("autoShutdownOpuClientSignalFail", 167),
          ("autoShutdownSendingAisLine", 159),
          ("autoShutdownSendingAisOdu", 160),
          ("autoShutdownSendingAisOpu", 161),
          ("autoShutdownSendingEPC", 168),
          ("autoShutdownSendingLckOdu", 169),
          ("autoShutdownSendingOciOdu", 170),
          ("autoShutdownToHighTemp", 18),
          ("autoShutdownToHighTxPwr", 19),
          ("autoShutdownTxRxLasersDueToHighTemp", 172),
          ("autoShutdownVfCSF", 435),
          ("automaticPowerReduction", 76),
          ("automaticPowerReductionForEyeSafety", 77),
          ("backreflectionTooHigh", 36),
          ("backupForcedToHalt", 125),
          ("backupNotResponding", 206),
          ("backwardDefectIndicationOdu", 92),
          ("backwardDefectIndicationOduTcmA", 94),
          ("backwardDefectIndicationOduTcmB", 95),
          ("backwardDefectIndicationOduTcmC", 96),
          ("backwardDefectIndicationOtu", 93),
          ("brPwrRxTooHigh", 293),
          ("capabilityLevelMismatch", 199),
          ("carrierFreqOffsetTooHigh", 300),
          ("carrierFreqOffsetTooLow", 301),
          ("channelMismatch", 64),
          ("chromaticDispersionTooHigh", 294),
          ("chromaticDispersionTooLow", 295),
          ("clientFailForwarding", 162),
          ("confOutPowerTransTooHigh", 26),
          ("confOutPowerTransTooLow", 27),
          ("configurationMismatch", 411),
          ("currentTooHigh", 276),
          ("databaseFailure", 111),
          ("databaseMismatch", 110),
          ("databaseNcuMismatch", 112),
          ("databaseVersionMismatch", 114),
          ("dbReplicationIncompleted", 113),
          ("dcnCommunicationFail", 243),
          ("differentialGroupDelayTooHigh", 310),
          ("dispersionCompensationTooHigh", 296),
          ("dispersionCompensationTooLow", 297),
          ("dispertionTunningCondition", 99),
          ("dsbdChannelPowerTooHigh", 29),
          ("duplexLinkFailure", 116),
          ("encryptionModuleCryPasswdError", 222),
          ("encryptionModuleCryPasswdMissing", 104),
          ("encryptionModuleFwpUpdateEnabled", 131),
          ("encryptionModuleSelfTestFail", 255),
          ("encryptionModuleSelfTestFailCritical", 256),
          ("encryptionModuleSelfTestStarted", 107),
          ("encryptionModuleTamperDetected", 385),
          ("encryptionPortAuthPasswdMissing", 90),
          ("encryptionPortEncryptionSwitchOffEnabled", 103),
          ("encryptionPortEncryptionSwitchedOff", 108),
          ("encryptionPortKeyExchangedForced", 151),
          ("encryptionPortKeyInitExchgMissed", 148),
          ("encryptionPortMaxKeyExchgFailuresReachedIs", 149),
          ("encryptionPortMaxKeyExchgFailuresReachedOos", 150),
          ("eqlzAdjust", 33),
          ("eqptProvMismatch", 35),
          ("equalizationProgress", 22),
          ("equipmentMismatch", 200),
          ("equipmentMismatchAllow", 423),
          ("equipmentNotAccepted", 197),
          ("equipmentNotApproved", 198),
          ("equipmentNotSupportedByPhysicalLayer", 201),
          ("facilityDataRateNotSupported", 261),
          ("facilityForcedOn", 127),
          ("facilityLoopback", 190),
          ("farEndCommFailure", 123),
          ("farEndIpAddressUnknown", 122),
          ("faultOnOpm", 215),
          ("fiberAttenuationCond", 63),
          ("fiberAttenuationHigh", 55),
          ("fiberAttenuationHighTx", 60),
          ("fiberConnCommError", 52),
          ("fiberConnDataFailure", 54),
          ("fiberConnInvalid", 50),
          ("fiberConnInvalidTx", 58),
          ("fiberConnLos", 48),
          ("fiberConnMismatch", 51),
          ("fiberConnMismatchTx", 59),
          ("fiberConnOptFault", 49),
          ("fiberConnProtocolFailure", 53),
          ("fwdAseTableFailPilot", 128),
          ("fwdAseTableOnPilot", 129),
          ("fwpMismatchDownloadNotServiceAffecting", 132),
          ("fwpMismatchDownloadServiceAffecting", 133),
          ("gainTiltNotSettable", 135),
          ("gfpLossOfClientSig", 188),
          ("highBer", 136),
          ("hwDegrade", 140),
          ("hwFailure", 141),
          ("hwInitializing", 138),
          ("hwOprReachedHT", 139),
          ("inputVoltageFailure", 401),
          ("inputVoltageFailurePort1", 402),
          ("inputVoltageFailurePort2", 403),
          ("laserBiasCurrAbnormal", 57),
          ("laserBiasCurrentNormalizedtooHigh", 331),
          ("laserEndOfLife", 20),
          ("laserFailure", 61),
          ("laserOnDelay", 152),
          ("laserTemperatureTooHigh", 14),
          ("laserTemperatureTooLow", 15),
          ("latencyTooHigh", 329),
          ("latencyTooLow", 330),
          ("linkControlProtocolFailure", 157),
          ("linkDown", 158),
          ("localFault", 173),
          ("localOscLevelAbnormal", 174),
          ("localOscTemperatureTooHigh", 332),
          ("localOscTemperatureTooLow", 333),
          ("lockedDefectOdu", 153),
          ("lockedDefectOduTcmA", 154),
          ("lockedDefectOduTcmB", 155),
          ("lockedDefectOduTcmC", 156),
          ("logicalLanesSkewTooHigh", 366),
          ("loopbackError", 189),
          ("losAttProgress", 186),
          ("lossOfCharSync", 100),
          ("lossOfCharSyncFromFarEnd", 101),
          ("lossOfFrame", 178),
          ("lossOfFrameLossOfMultiFrameOdu", 179),
          ("lossOfFrameMux", 176),
          ("lossOfFrameOtu", 177),
          ("lossOfGfpFrame", 175),
          ("lossOfLane", 180),
          ("lossOfLaneOtu", 407),
          ("lossOfMfiOpu", 409),
          ("lossOfMultiFrameOtu", 182),
          ("lossOfPilotSignal", 225),
          ("lossOfPointerHigherOrderPath", 185),
          ("lossOfPointerLowerOrderPath", 184),
          ("lossOfReceiverClockRecovery", 62),
          ("lossOfSignal", 11),
          ("lossOfSignalCPort", 30),
          ("lossOfSignalNPort", 31),
          ("lossOfSignalTransmitter", 120),
          ("lossOfTestSeqSynchOpu", 408),
          ("lossOsc", 187),
          ("lossofMultiframeHigherOrderPath", 183),
          ("lossofMultiframeLowerOrderPath", 181),
          ("lossofSequenceHigherOrderPath", 264),
          ("lossofSequenceLowerOrderPath", 263),
          ("lossofTandemConnectionOduTcmA", 191),
          ("lossofTandemConnectionOduTcmB", 192),
          ("lossofTandemConnectionOduTcmC", 193),
          ("mansw", 194),
          ("maxPowerConsEquipModulesToHigh", 237),
          ("maxPowerConsProvModulesToHigh", 236),
          ("meaSwRevision", 202),
          ("midstageFault", 204),
          ("mismatch", 203),
          ("multipleFanFailure", 119),
          ("multiplexStructureIdentifierMismatchOPU", 205),
          ("networkPathRestricted", 432),
          ("ntpForSchedEqlzRequired", 244),
          ("oTDRMeasuringinProgress", 221),
          ("oduAutoShutdownRxAIS", 412),
          ("oduAutoShutdownTxAIS", 413),
          ("oduTribMsiMismatch", 211),
          ("oosAins", 9),
          ("oosDisabled", 6),
          ("oosDisabledLckOduRx", 414),
          ("oosDisabledLckOduTrmt", 410),
          ("oosMaintenance", 8),
          ("oosManagement", 7),
          ("openConnectionIndicationOdu", 207),
          ("openConnectionIndicationOduTcmA", 208),
          ("openConnectionIndicationOduTcmB", 209),
          ("openConnectionIndicationOduTcmC", 210),
          ("opmAbnormalCondition", 214),
          ("optInputPwrReceivedTooHigh", 13),
          ("optInputPwrReceivedTooLow", 12),
          ("optOutputPowerTransTooHigh", 17),
          ("optOutputPowerTransTooLow", 16),
          ("optSignalFailure", 28),
          ("opuClientSignalFail", 109),
          ("oscOpticalPowerControlFailHigh", 219),
          ("oscOpticalPowerControlFailLow", 220),
          ("oscPwrTooHigh", 342),
          ("oscPwrTooLow", 343),
          ("outputPowerFault", 32),
          ("payloadMismatchGfp", 226),
          ("payloadMismatchHigherOrderPath", 229),
          ("payloadMismatchLowerOrderPath", 227),
          ("payloadMismatchOPU", 228),
          ("pcsSignalDegrade", 250),
          ("peerLink", 223),
          ("pilotReceiveLevelHigh", 224),
          ("powerMissing", 238),
          ("powerSupplyUnitFailure", 235),
          ("prbsLossOfSeqSynch", 231),
          ("prbsRcvActivated", 232),
          ("prbsTrmtActivated", 233),
          ("protectionNotAvailable", 234),
          ("provPayloadMismatch", 230),
          ("pumpLaser1TempTooHigh", 334),
          ("pumpLaser1TempTooLow", 335),
          ("pumpLaser2TempTooHigh", 336),
          ("pumpLaser2TempTooLow", 337),
          ("pumpLaser3TempTooHigh", 338),
          ("pumpLaser3TempTooLow", 339),
          ("pumpLaser4TempTooHigh", 340),
          ("pumpLaser4TempTooLow", 341),
          ("ramanPumpPwrTooHigh", 344),
          ("ramanPumpPwrTooLow", 345),
          ("receiverDisabled", 213),
          ("receiverOverloadProtection", 137),
          ("remoteDefectIndicationHigherOrderPath", 241),
          ("remoteDefectIndicationLine", 239),
          ("remoteDefectIndicationLowerOrderPath", 240),
          ("removed", 10),
          ("roundTripDelayTooHigh", 346),
          ("roundTripDelayTooLow", 347),
          ("sectionTraceMismatch", 391),
          ("serverSignalFail", 265),
          ("serverSignalFailTx", 260),
          ("serverSignalFailureGfp", 266),
          ("serverSignalFailureODU", 267),
          ("serverSignalFailurePath", 268),
          ("serverSignalFailureSectionRS", 269),
          ("serverSignalFailureVf", 21),
          ("signalDegradationonLinkVector", 247),
          ("signalDegradeLine", 246),
          ("signalDegradeOdu", 248),
          ("signalDegradeOduTcmA", 252),
          ("signalDegradeOduTcmB", 253),
          ("signalDegradeOduTcmC", 254),
          ("signalDegradeOlm", 245),
          ("signalDegradeOtu", 249),
          ("signalDegradeScn", 251),
          ("signalFailureOPU", 259),
          ("signalFailureOnLink", 257),
          ("signalFailureonLinkVector", 258),
          ("signalToNoiseRatioTooLow", 367),
          ("singleFanFailure", 118),
          ("subModuleTempTooHigh", 368),
          ("switchFailed", 274),
          ("switchToDuplexInhibited", 272),
          ("switchtoProtectionInhibited", 142),
          ("switchtoWorkingInhibited", 143),
          ("temperatureTooHigh", 369),
          ("temperatureTooLow", 370),
          ("terminalLoopback", 5),
          ("thermoElectricCoolerEndOfLife", 386),
          ("thres15MinExceededBbePcs", 420),
          ("thres15MinExceededFecBERCE", 291),
          ("thres15MinExceededFecCE", 298),
          ("thres15MinExceededFecES", 311),
          ("thres15MinExceededFecSES", 350),
          ("thres15MinExceededFecUBE", 383),
          ("thres15MinExceededOduBbe", 281),
          ("thres15MinExceededOduES", 315),
          ("thres15MinExceededOduSES", 354),
          ("thres15MinExceededOduTcmABbe", 285),
          ("thres15MinExceededOduTcmAES", 323),
          ("thres15MinExceededOduTcmASES", 360),
          ("thres15MinExceededOduTcmAUAS", 377),
          ("thres15MinExceededOduTcmBBbe", 287),
          ("thres15MinExceededOduTcmBES", 325),
          ("thres15MinExceededOduTcmBSES", 362),
          ("thres15MinExceededOduTcmBUAS", 379),
          ("thres15MinExceededOduTcmCBbe", 289),
          ("thres15MinExceededOduTcmCES", 327),
          ("thres15MinExceededOduTcmCSES", 364),
          ("thres15MinExceededOduTcmCUAS", 381),
          ("thres15MinExceededOduUAS", 373),
          ("thres15MinExceededOtuBbe", 283),
          ("thres15MinExceededOtuES", 317),
          ("thres15MinExceededOtuSES", 356),
          ("thres15MinExceededOtuUAS", 375),
          ("thres15MinExceededPhysConvCV", 304),
          ("thres15MinExceededPhysConvDE", 308),
          ("thres15MinExceededPhysConvES", 319),
          ("thres15MinExceededSonetLineCV", 302),
          ("thres15MinExceededSonetLineES", 313),
          ("thres15MinExceededSonetLineSES", 352),
          ("thres15MinExceededSonetLineUAS", 371),
          ("thres15MinExceededSonetSectCV", 306),
          ("thres15MinExceededSonetSectES", 321),
          ("thres15MinExceededSonetSectSEFS", 348),
          ("thres15MinExceededSonetSectSES", 358),
          ("thresOptPowerCtrlFailureHigh", 216),
          ("thresOptPowerCtrlFailureLow", 217),
          ("topologyDataCalculationInProgress", 97),
          ("traceIdentifierMismatchOdu", 389),
          ("traceIdentifierMismatchOduTcmA", 392),
          ("traceIdentifierMismatchOduTcmB", 393),
          ("traceIdentifierMismatchOduTcmC", 394),
          ("traceIdentifierMismatchOtu", 390),
          ("transmitterDisabledOff", 212),
          ("turnupCondition", 396),
          ("turnupFailed", 395),
          ("txPowerLimited", 218),
          ("uPortFailure", 23),
          ("undefined", 0),
          ("unequippedHigherOrderPath", 398),
          ("unequippedLowerOrderPath", 397),
          ("vfClientSignalFail", 434),
          ("virtualChannelAis", 74),
          ("voaControlFail", 399),
          ("voltageOutOfRange", 400),
          ("warmUp", 424),
          ("wtrTimerRunning", 406),
          ("xfpDecisionThresSetFailed", 115))
    )



class FspR7AlarmProfileList(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
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
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              92,
              93,
              94,
              95,
              96,
              97,
              99,
              100,
              101,
              103,
              104,
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
              118,
              119,
              120,
              122,
              123,
              125,
              127,
              128,
              129,
              131,
              132,
              133,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              148,
              149,
              150,
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
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              197,
              198,
              199,
              200,
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
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              272,
              274,
              276,
              277,
              278,
              279,
              280,
              281,
              283,
              285,
              287,
              289,
              291,
              293,
              294,
              295,
              296,
              297,
              298,
              300,
              301,
              302,
              304,
              306,
              308,
              310,
              311,
              313,
              315,
              317,
              319,
              321,
              323,
              325,
              327,
              329,
              330,
              331,
              332,
              333,
              334,
              335,
              336,
              337,
              338,
              339,
              340,
              341,
              342,
              343,
              344,
              345,
              346,
              347,
              348,
              350,
              352,
              354,
              356,
              358,
              360,
              362,
              364,
              366,
              367,
              368,
              369,
              370,
              371,
              373,
              375,
              377,
              379,
              381,
              383,
              385,
              386,
              387,
              389,
              390,
              391,
              392,
              393,
              394,
              395,
              396,
              397,
              398,
              399,
              400,
              401,
              402,
              403,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              420,
              422,
              423,
              424,
              432,
              434,
              435,
              13006,
              13007,
              13008,
              13009,
              13010,
              100005,
              100006,
              100009,
              100010,
              100011,
              100012,
              100013,
              100014,
              100015,
              100016,
              120004,
              120005,
              120006,
              120007,
              120008,
              120009,
              120010,
              120011,
              120012)
        )
    )
    namedValues = NamedValues(
        *(("alarmIndicationSignalHigherOrderPath", 70),
          ("alarmIndicationSignalLine", 65),
          ("alarmIndicationSignalLowerOrderPath", 66),
          ("alarmIndicationSignalOdu", 67),
          ("alarmIndicationSignalOduTcmA", 71),
          ("alarmIndicationSignalOduTcmB", 72),
          ("alarmIndicationSignalOduTcmC", 73),
          ("alarmIndicationSignalOpu", 68),
          ("alarmIndicationSignalOtu", 69),
          ("alarmInputTIF", 387),
          ("ampFailure", 34),
          ("amplifierAbnormal", 75),
          ("apsConfigMismatch", 80),
          ("apsProtocolFailure", 81),
          ("aseLow", 82),
          ("aseTableBuild", 166),
          ("aseTableGenFailHighBackreflection", 84),
          ("aseTableGenFailLow", 83),
          ("aseTableGenFailOscMissing", 85),
          ("aseTableGenFailPilot", 86),
          ("aseTableGenFailSignalinput", 87),
          ("aseTableGenProgress", 89),
          ("aseTableNotAvailable", 88),
          ("attOnReceiverFiberHigherThanMonitor", 277),
          ("attOnReceiverFiberLowerThanMonitor", 278),
          ("attOnTransmitterFiberHigherThanMonitor", 279),
          ("attOnTransmitterFiberLowerThanMonitor", 280),
          ("autoAmpShutdown", 164),
          ("autoPowerShutdown", 25),
          ("autoShutdownAls", 163),
          ("autoShutdownAmpAps", 165),
          ("autoShutdownBlock", 24),
          ("autoShutdownGAis", 422),
          ("autoShutdownLaserOffDueToErrFwd", 171),
          ("autoShutdownOpuClientSignalFail", 167),
          ("autoShutdownSendingAisLine", 159),
          ("autoShutdownSendingAisOdu", 160),
          ("autoShutdownSendingAisOpu", 161),
          ("autoShutdownSendingEPC", 168),
          ("autoShutdownSendingLckOdu", 169),
          ("autoShutdownSendingOciOdu", 170),
          ("autoShutdownToHighTemp", 18),
          ("autoShutdownToHighTxPwr", 19),
          ("autoShutdownTxRxLasersDueToHighTemp", 172),
          ("autoShutdownVfCSF", 435),
          ("automaticPowerReduction", 76),
          ("automaticPowerReductionForEyeSafety", 77),
          ("backreflectionTooHigh", 36),
          ("backupForcedToHalt", 125),
          ("backupNotResponding", 206),
          ("backwardDefectIndicationOdu", 92),
          ("backwardDefectIndicationOduTcmA", 94),
          ("backwardDefectIndicationOduTcmB", 95),
          ("backwardDefectIndicationOduTcmC", 96),
          ("backwardDefectIndicationOtu", 93),
          ("brPwrRxTooHigh", 293),
          ("capabilityLevelMismatch", 199),
          ("carrierFreqOffsetTooHigh", 300),
          ("carrierFreqOffsetTooLow", 301),
          ("cfmCcmError", 13008),
          ("cfmCcmLost", 13009),
          ("cfmCcmMacStatus", 13007),
          ("cfmCcmXConn", 13010),
          ("cfmRemoteDefectIndication", 13006),
          ("channelMismatch", 64),
          ("chromaticDispersionTooHigh", 294),
          ("chromaticDispersionTooLow", 295),
          ("clientFailForwarding", 162),
          ("confOutPowerTransTooHigh", 26),
          ("confOutPowerTransTooLow", 27),
          ("configurationMismatch", 411),
          ("currentTooHigh", 276),
          ("databaseFailure", 111),
          ("databaseMismatch", 110),
          ("databaseNcuMismatch", 112),
          ("databaseVersionMismatch", 114),
          ("dbReplicationIncompleted", 113),
          ("dcnCommunicationFail", 243),
          ("differentialGroupDelayTooHigh", 310),
          ("dispersionCompensationTooHigh", 296),
          ("dispersionCompensationTooLow", 297),
          ("dispertionTunningCondition", 99),
          ("dsbdChannelPowerTooHigh", 29),
          ("duplexLinkFailure", 116),
          ("encryptionModuleCryPasswdError", 222),
          ("encryptionModuleCryPasswdMissing", 104),
          ("encryptionModuleFwpUpdateEnabled", 131),
          ("encryptionModuleSelfTestFail", 255),
          ("encryptionModuleSelfTestFailCritical", 256),
          ("encryptionModuleSelfTestStarted", 107),
          ("encryptionModuleTamperDetected", 385),
          ("encryptionPortAuthPasswdMissing", 90),
          ("encryptionPortEncryptionSwitchOffEnabled", 103),
          ("encryptionPortEncryptionSwitchedOff", 108),
          ("encryptionPortKeyExchangedForced", 151),
          ("encryptionPortKeyInitExchgMissed", 148),
          ("encryptionPortMaxKeyExchgFailuresReachedIs", 149),
          ("encryptionPortMaxKeyExchgFailuresReachedOos", 150),
          ("eqlzAdjust", 33),
          ("eqptProvMismatch", 35),
          ("equalizationProgress", 22),
          ("equipmentMismatch", 200),
          ("equipmentMismatchAllow", 423),
          ("equipmentNotAccepted", 197),
          ("equipmentNotApproved", 198),
          ("equipmentNotSupportedByPhysicalLayer", 201),
          ("facilityDataRateNotSupported", 261),
          ("facilityForcedOn", 127),
          ("facilityLoopback", 190),
          ("farEndCommFailure", 123),
          ("farEndIpAddressUnknown", 122),
          ("faultOnOpm", 215),
          ("fiberAttenuationCond", 63),
          ("fiberAttenuationHigh", 55),
          ("fiberAttenuationHighTx", 60),
          ("fiberConnCommError", 52),
          ("fiberConnDataFailure", 54),
          ("fiberConnInvalid", 50),
          ("fiberConnInvalidTx", 58),
          ("fiberConnLos", 48),
          ("fiberConnMismatch", 51),
          ("fiberConnMismatchTx", 59),
          ("fiberConnOptFault", 49),
          ("fiberConnProtocolFailure", 53),
          ("fwdAseTableFailPilot", 128),
          ("fwdAseTableOnPilot", 129),
          ("fwpMismatchDownloadNotServiceAffecting", 132),
          ("fwpMismatchDownloadServiceAffecting", 133),
          ("gainAdoptFailedSpeq", 120010),
          ("gainTiltNotSettable", 135),
          ("gainTooHighSpeq", 120008),
          ("gainTooLowSpeq", 120009),
          ("gfpLossOfClientSig", 188),
          ("highBer", 136),
          ("hwDegrade", 140),
          ("hwFailure", 141),
          ("hwInitializing", 138),
          ("hwOprReachedHT", 139),
          ("inputVoltageFailure", 401),
          ("inputVoltageFailurePort1", 402),
          ("inputVoltageFailurePort2", 403),
          ("laserBiasCurrAbnormal", 57),
          ("laserBiasCurrentNormalizedtooHigh", 331),
          ("laserEndOfLife", 20),
          ("laserFailure", 61),
          ("laserOnDelay", 152),
          ("laserTemperatureTooHigh", 14),
          ("laserTemperatureTooLow", 15),
          ("latencyTooHigh", 329),
          ("latencyTooLow", 330),
          ("linkControlProtocolFailure", 157),
          ("linkDown", 158),
          ("localFault", 173),
          ("localOscLevelAbnormal", 174),
          ("localOscTemperatureTooHigh", 332),
          ("localOscTemperatureTooLow", 333),
          ("lockedDefectOdu", 153),
          ("lockedDefectOduTcmA", 154),
          ("lockedDefectOduTcmB", 155),
          ("lockedDefectOduTcmC", 156),
          ("logicalLanesSkewTooHigh", 366),
          ("loopbackError", 189),
          ("losAttProgress", 186),
          ("lossOfCharSync", 100),
          ("lossOfCharSyncFromFarEnd", 101),
          ("lossOfFrame", 178),
          ("lossOfFrameLossOfMultiFrameOdu", 179),
          ("lossOfFrameMux", 176),
          ("lossOfFrameOtu", 177),
          ("lossOfGfpFrame", 175),
          ("lossOfLane", 180),
          ("lossOfLaneOtu", 407),
          ("lossOfMfiOpu", 409),
          ("lossOfMultiFrameOtu", 182),
          ("lossOfPilotSignal", 225),
          ("lossOfPointerHigherOrderPath", 185),
          ("lossOfPointerLowerOrderPath", 184),
          ("lossOfReceiverClockRecovery", 62),
          ("lossOfSignal", 11),
          ("lossOfSignalCPort", 30),
          ("lossOfSignalNPort", 31),
          ("lossOfSignalTransmitter", 120),
          ("lossOfTestSeqSynchOpu", 408),
          ("lossOsc", 187),
          ("lossofMultiframeHigherOrderPath", 183),
          ("lossofMultiframeLowerOrderPath", 181),
          ("lossofSequenceHigherOrderPath", 264),
          ("lossofSequenceLowerOrderPath", 263),
          ("lossofTandemConnectionOduTcmA", 191),
          ("lossofTandemConnectionOduTcmB", 192),
          ("lossofTandemConnectionOduTcmC", 193),
          ("mansw", 194),
          ("maxPowerConsEquipModulesToHigh", 237),
          ("maxPowerConsProvModulesToHigh", 236),
          ("meaSwRevision", 202),
          ("mepNotPresentL2", 100005),
          ("messageLossSpeq", 120004),
          ("midstageFault", 204),
          ("mismatch", 203),
          ("multipleFanFailure", 119),
          ("multiplexStructureIdentifierMismatchOPU", 205),
          ("networkPathRestricted", 432),
          ("ntpForSchedEqlzRequired", 244),
          ("oTDRMeasuringinProgress", 221),
          ("oduAutoShutdownRxAIS", 412),
          ("oduAutoShutdownTxAIS", 413),
          ("oduTribMsiMismatch", 211),
          ("oosAins", 9),
          ("oosDisabled", 6),
          ("oosDisabledLckOduRx", 414),
          ("oosDisabledLckOduTrmt", 410),
          ("oosMaintenance", 8),
          ("oosManagement", 7),
          ("openConnectionIndicationOdu", 207),
          ("openConnectionIndicationOduTcmA", 208),
          ("openConnectionIndicationOduTcmB", 209),
          ("openConnectionIndicationOduTcmC", 210),
          ("opmAbnormalCondition", 214),
          ("optInputPwrReceivedTooHigh", 13),
          ("optInputPwrReceivedTooLow", 12),
          ("optLowSpeq", 120006),
          ("optOutputPowerTransTooHigh", 17),
          ("optOutputPowerTransTooLow", 16),
          ("optSignalFailure", 28),
          ("opuClientSignalFail", 109),
          ("oscFiberMissingSpeq", 120005),
          ("oscOpticalPowerControlFailHigh", 219),
          ("oscOpticalPowerControlFailLow", 220),
          ("oscPwrTooHigh", 342),
          ("oscPwrTooLow", 343),
          ("outputPowerFault", 32),
          ("payloadMismatchGfp", 226),
          ("payloadMismatchHigherOrderPath", 229),
          ("payloadMismatchLowerOrderPath", 227),
          ("payloadMismatchOPU", 228),
          ("pcsSignalDegrade", 250),
          ("peerLink", 223),
          ("pilotReceiveLevelHigh", 224),
          ("powerMissing", 238),
          ("powerSupplyUnitFailure", 235),
          ("ppcLimitExceededSpeq", 120012),
          ("ppcOutOfRangeSpeq", 120007),
          ("prbsLossOfSeqSynch", 231),
          ("prbsRcvActivated", 232),
          ("prbsTrmtActivated", 233),
          ("priVidNotEqualExtVidL2", 100006),
          ("processLockedOutSpeq", 120011),
          ("protectionNotAvailable", 234),
          ("provPayloadMismatch", 230),
          ("pumpLaser1TempTooHigh", 334),
          ("pumpLaser1TempTooLow", 335),
          ("pumpLaser2TempTooHigh", 336),
          ("pumpLaser2TempTooLow", 337),
          ("pumpLaser3TempTooHigh", 338),
          ("pumpLaser3TempTooLow", 339),
          ("pumpLaser4TempTooHigh", 340),
          ("pumpLaser4TempTooLow", 341),
          ("ramanPumpPwrTooHigh", 344),
          ("ramanPumpPwrTooLow", 345),
          ("receiverDisabled", 213),
          ("receiverOverloadProtection", 137),
          ("remoteDefectIndicationHigherOrderPath", 241),
          ("remoteDefectIndicationLine", 239),
          ("remoteDefectIndicationLowerOrderPath", 240),
          ("removed", 10),
          ("roundTripDelayTooHigh", 346),
          ("roundTripDelayTooLow", 347),
          ("sectionTraceMismatch", 391),
          ("serverSignalFail", 265),
          ("serverSignalFailTx", 260),
          ("serverSignalFailureGfp", 266),
          ("serverSignalFailureODU", 267),
          ("serverSignalFailurePath", 268),
          ("serverSignalFailureSectionRS", 269),
          ("serverSignalFailureVf", 21),
          ("sfCfmLevel0L2", 100009),
          ("sfCfmLevel1L2", 100010),
          ("sfCfmLevel2L2", 100011),
          ("sfCfmLevel3L2", 100012),
          ("sfCfmLevel4L2", 100013),
          ("sfCfmLevel5L2", 100014),
          ("sfCfmLevel6L2", 100015),
          ("sfCfmLevel7L2", 100016),
          ("signalDegradationonLinkVector", 247),
          ("signalDegradeLine", 246),
          ("signalDegradeOdu", 248),
          ("signalDegradeOduTcmA", 252),
          ("signalDegradeOduTcmB", 253),
          ("signalDegradeOduTcmC", 254),
          ("signalDegradeOlm", 245),
          ("signalDegradeOtu", 249),
          ("signalDegradeScn", 251),
          ("signalFailureOPU", 259),
          ("signalFailureOnLink", 257),
          ("signalFailureonLinkVector", 258),
          ("signalToNoiseRatioTooLow", 367),
          ("singleFanFailure", 118),
          ("subModuleTempTooHigh", 368),
          ("switchFailed", 274),
          ("switchToDuplexInhibited", 272),
          ("switchtoProtectionInhibited", 142),
          ("switchtoWorkingInhibited", 143),
          ("temperatureTooHigh", 369),
          ("temperatureTooLow", 370),
          ("terminalLoopback", 5),
          ("thermoElectricCoolerEndOfLife", 386),
          ("thres15MinExceededBbePcs", 420),
          ("thres15MinExceededFecBERCE", 291),
          ("thres15MinExceededFecCE", 298),
          ("thres15MinExceededFecES", 311),
          ("thres15MinExceededFecSES", 350),
          ("thres15MinExceededFecUBE", 383),
          ("thres15MinExceededOduBbe", 281),
          ("thres15MinExceededOduES", 315),
          ("thres15MinExceededOduSES", 354),
          ("thres15MinExceededOduTcmABbe", 285),
          ("thres15MinExceededOduTcmAES", 323),
          ("thres15MinExceededOduTcmASES", 360),
          ("thres15MinExceededOduTcmAUAS", 377),
          ("thres15MinExceededOduTcmBBbe", 287),
          ("thres15MinExceededOduTcmBES", 325),
          ("thres15MinExceededOduTcmBSES", 362),
          ("thres15MinExceededOduTcmBUAS", 379),
          ("thres15MinExceededOduTcmCBbe", 289),
          ("thres15MinExceededOduTcmCES", 327),
          ("thres15MinExceededOduTcmCSES", 364),
          ("thres15MinExceededOduTcmCUAS", 381),
          ("thres15MinExceededOduUAS", 373),
          ("thres15MinExceededOtuBbe", 283),
          ("thres15MinExceededOtuES", 317),
          ("thres15MinExceededOtuSES", 356),
          ("thres15MinExceededOtuUAS", 375),
          ("thres15MinExceededPhysConvCV", 304),
          ("thres15MinExceededPhysConvDE", 308),
          ("thres15MinExceededPhysConvES", 319),
          ("thres15MinExceededSonetLineCV", 302),
          ("thres15MinExceededSonetLineES", 313),
          ("thres15MinExceededSonetLineSES", 352),
          ("thres15MinExceededSonetLineUAS", 371),
          ("thres15MinExceededSonetSectCV", 306),
          ("thres15MinExceededSonetSectES", 321),
          ("thres15MinExceededSonetSectSEFS", 348),
          ("thres15MinExceededSonetSectSES", 358),
          ("thresOptPowerCtrlFailureHigh", 216),
          ("thresOptPowerCtrlFailureLow", 217),
          ("topologyDataCalculationInProgress", 97),
          ("traceIdentifierMismatchOdu", 389),
          ("traceIdentifierMismatchOduTcmA", 392),
          ("traceIdentifierMismatchOduTcmB", 393),
          ("traceIdentifierMismatchOduTcmC", 394),
          ("traceIdentifierMismatchOtu", 390),
          ("transmitterDisabledOff", 212),
          ("turnupCondition", 396),
          ("turnupFailed", 395),
          ("txPowerLimited", 218),
          ("uPortFailure", 23),
          ("undefined", 0),
          ("unequippedHigherOrderPath", 398),
          ("unequippedLowerOrderPath", 397),
          ("vfClientSignalFail", 434),
          ("virtualChannelAis", 74),
          ("voaControlFail", 399),
          ("voltageOutOfRange", 400),
          ("warmUp", 424),
          ("wtrTimerRunning", 406),
          ("xfpDecisionThresSetFailed", 115))
    )



class FspR7AlsMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("advaALS", 1),
          ("fastAls", 4),
          ("noALS", 3),
          ("sonetALS", 2),
          ("undefined", 0))
    )



class FspR7AlsModeCaps(Bits, TextualConvention):
    status = "current"


class FspR7AppType(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("controlplane", 5),
          ("lct", 1),
          ("snmp", 2),
          ("system", 6),
          ("tcli", 4),
          ("tl1", 3),
          ("undefined", 0))
    )



class FspR7ApsChannel(Integer32, TextualConvention):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("gfp", 12),
          ("line", 2),
          ("none", 1),
          ("path", 3),
          ("pm", 4),
          ("prop", 13),
          ("sm", 11),
          ("tcm1", 5),
          ("tcm2", 6),
          ("tcm3", 7),
          ("tcm4", 8),
          ("tcm5", 9),
          ("tcm6", 10),
          ("undefined", 0))
    )



class FspR7APSCommand(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manualSwitch", 2),
          ("release", 1),
          ("undefined", 0))
    )



class FspR7APSCommandCaps(Bits, TextualConvention):
    status = "current"


class FspR7AseTabOpr(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("build", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class FspR7AseTabOprCaps(Bits, TextualConvention):
    status = "current"


class FspR7EquipmentAssignState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assignable", 2),
          ("assigned", 1),
          ("notAssignable", 3),
          ("undefined", 0))
    )



class FspR7AutoThresReset(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rls", 1),
          ("rtf", 2),
          ("undefined", 0))
    )



class FspR7AutoThresResetCaps(Bits, TextualConvention):
    status = "current"


class FspR7Baund(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("baud115200", 7),
          ("baud19200", 4),
          ("baud2400", 1),
          ("baud38400", 5),
          ("baud4800", 2),
          ("baud57600", 6),
          ("baud9600", 3),
          ("undefined", 0))
    )



class FspR7BaundCaps(Bits, TextualConvention):
    status = "current"


class FspR7BERThreshold(Integer32, TextualConvention):
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
        *(("exp5", 1),
          ("exp6", 2),
          ("exp7", 3),
          ("exp8", 4),
          ("exp9", 5),
          ("undefined", 0))
    )



class FspR7BERThresholdCaps(Bits, TextualConvention):
    status = "current"


class FspR7BERThresholdSection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("exp7", 3),
          ("exp8", 4),
          ("exp9", 5),
          ("undefined", 0))
    )



class FspR7BERThresholdSectionCaps(Bits, TextualConvention):
    status = "current"


class FspR7BidirectionalChannel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tx1310rx1490", 1),
          ("tx1490rx1310", 2),
          ("undefined", 0))
    )



class FspR7BidirectionalChannelCaps(Bits, TextualConvention):
    status = "current"


class FspR7Bitrate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bitrate10", 1),
          ("bitrate100", 2),
          ("bitrate1000", 3),
          ("bitrate10000", 4),
          ("undefined", 0))
    )



class FspR7BitrateCaps(Bits, TextualConvention):
    status = "current"


class FspR7CapInventory(Integer32, TextualConvention):
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
              50)
        )
    )
    namedValues = NamedValues(
        *(("level0", 1),
          ("level1", 2),
          ("level2", 3),
          ("level3", 4),
          ("level4", 5),
          ("level5", 6),
          ("undefined", 0),
          ("unknown", 50))
    )



class FspR7CapInventoryCaps(Bits, TextualConvention):
    status = "current"


class FspR7Category(Integer32, TextualConvention):
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("accessory", 13),
          ("adm", 20),
          ("amplifier", 5),
          ("any", 16),
          ("att", 11),
          ("channelMod", 2),
          ("common", 10),
          ("dcm", 6),
          ("dummy", 9),
          ("ethernetMod", 18),
          ("fiber", 14),
          ("filter", 4),
          ("jumper", 12),
          ("oscm", 8),
          ("plug", 3),
          ("powerSplitter", 19),
          ("protectionMod", 15),
          ("roadm", 17),
          ("shelf", 1),
          ("switch", 7),
          ("undefined", 0))
    )



class FspR7CertApply(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apply", 2),
          ("none", 1),
          ("undefined", 0))
    )



class FspR7CertApplyCaps(Bits, TextualConvention):
    status = "current"


class FspR7ChannelBandwidth(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("band100G", 3),
          ("band125G", 4),
          ("band150G", 5),
          ("band175G", 6),
          ("band200G", 7),
          ("band225G", 8),
          ("band250G", 9),
          ("band275G", 10),
          ("band300G", 11),
          ("band50G", 1),
          ("band75G", 2),
          ("undefined", 0))
    )



class FspR7ChannelBandwidthCaps(Bits, TextualConvention):
    status = "current"


class FspR7ChannelIdentifier(Integer32, TextualConvention):
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
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
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
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
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
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
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
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
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
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              318,
              319,
              320,
              321,
              322,
              323,
              324,
              325,
              326,
              327,
              328,
              329,
              330,
              331,
              332,
              333,
              334,
              335,
              336,
              337,
              338,
              339,
              340,
              341,
              342,
              343,
              344,
              345,
              346,
              347,
              348,
              349,
              350,
              351,
              352,
              353,
              354,
              355,
              356,
              357,
              358,
              359,
              360,
              361,
              362,
              363,
              364,
              365,
              366,
              367,
              368,
              369,
              370,
              371,
              372,
              373,
              382,
              383,
              384,
              385,
              386,
              387,
              388,
              389,
              390,
              392,
              393,
              394,
              395,
              396,
              397,
              398,
              399,
              400,
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
              419,
              420,
              421,
              422,
              423,
              424,
              425,
              426,
              427,
              428,
              429,
              430,
              431,
              432,
              433,
              434,
              435,
              436,
              437,
              438,
              439,
              440,
              441,
              442,
              443,
              444,
              445,
              446,
              447,
              448,
              449,
              450,
              451,
              452,
              453,
              454,
              455,
              456,
              457,
              458,
              459,
              460,
              461,
              462,
              463,
              464,
              465,
              466,
              467,
              468,
              469,
              470,
              471,
              472,
              473,
              474,
              475,
              476,
              477,
              478,
              479,
              480,
              481,
              482,
              483,
              484,
              485,
              486,
              487,
              488,
              489,
              490,
              491,
              492,
              493,
              494,
              495,
              496,
              497,
              498,
              499,
              500)
        )
    )
    namedValues = NamedValues(
        *(("c1270", 189),
          ("c1290", 190),
          ("c1310", 191),
          ("c1330", 192),
          ("c1350", 193),
          ("c1370", 194),
          ("c1430", 195),
          ("c1450", 196),
          ("c1470", 91),
          ("c1490", 92),
          ("c1510", 93),
          ("c1530", 94),
          ("c1550", 95),
          ("c1570", 96),
          ("c1590", 97),
          ("c1610", 98),
          ("d01", 1),
          ("d02", 2),
          ("d03", 3),
          ("d04", 4),
          ("d05", 5),
          ("d06", 6),
          ("d07", 7),
          ("d08", 8),
          ("d09", 9),
          ("d10", 10),
          ("d11", 11),
          ("d12", 12),
          ("d13", 13),
          ("d14", 14),
          ("d15", 15),
          ("d16", 16),
          ("d17", 17),
          ("d18", 18),
          ("d19", 19),
          ("d20", 20),
          ("d21", 21),
          ("d22", 22),
          ("d23", 23),
          ("d24", 24),
          ("d25", 25),
          ("d26", 26),
          ("d27", 27),
          ("d28", 28),
          ("d29", 29),
          ("d30", 30),
          ("d31", 31),
          ("d32", 32),
          ("d33", 33),
          ("d34", 34),
          ("d35", 35),
          ("d36", 36),
          ("d37", 37),
          ("d38", 38),
          ("d39", 39),
          ("d40", 40),
          ("d41", 41),
          ("d42", 42),
          ("d43", 43),
          ("d44", 44),
          ("d45", 45),
          ("d46", 46),
          ("d47", 47),
          ("d48", 48),
          ("d49", 49),
          ("d50", 50),
          ("d51", 51),
          ("d52", 52),
          ("d53", 53),
          ("d54", 54),
          ("d55", 55),
          ("d56", 56),
          ("d57", 57),
          ("d58", 58),
          ("d59", 59),
          ("d60", 60),
          ("d61", 61),
          ("d62", 62),
          ("d63", 63),
          ("d64", 64),
          ("dc1", 65),
          ("dc2", 66),
          ("dc3", 67),
          ("dc4", 68),
          ("dc5", 69),
          ("dc6", 70),
          ("dc7", 71),
          ("dc8", 72),
          ("dc9", 81),
          ("dl1", 73),
          ("dl2", 74),
          ("dl3", 75),
          ("dl4", 76),
          ("dl5", 77),
          ("dl6", 78),
          ("dl7", 79),
          ("dl8", 80),
          ("dl9", 82),
          ("f19125", 499),
          ("f19126", 498),
          ("f19127", 497),
          ("f19128", 496),
          ("f19130", 495),
          ("f19131", 494),
          ("f19132", 493),
          ("f19133", 492),
          ("f19135", 491),
          ("f19136", 490),
          ("f19137", 489),
          ("f19138", 488),
          ("f19140", 487),
          ("f19141", 486),
          ("f19142", 485),
          ("f19143", 484),
          ("f19145", 483),
          ("f19146", 482),
          ("f19147", 481),
          ("f19148", 480),
          ("f19150", 479),
          ("f19151", 478),
          ("f19152", 477),
          ("f19153", 476),
          ("f19155", 475),
          ("f19156", 474),
          ("f19157", 473),
          ("f19158", 472),
          ("f19160", 471),
          ("f19161", 470),
          ("f19162", 469),
          ("f19163", 468),
          ("f19165", 467),
          ("f19166", 466),
          ("f19167", 465),
          ("f19168", 464),
          ("f19170", 463),
          ("f19171", 462),
          ("f19172", 461),
          ("f19173", 460),
          ("f19175", 459),
          ("f19176", 458),
          ("f19177", 457),
          ("f19178", 456),
          ("f19180", 455),
          ("f19181", 454),
          ("f19182", 453),
          ("f19183", 452),
          ("f19185", 451),
          ("f19186", 450),
          ("f19187", 449),
          ("f19188", 448),
          ("f19190", 447),
          ("f19191", 446),
          ("f19192", 445),
          ("f19193", 444),
          ("f19195", 443),
          ("f19196", 442),
          ("f19197", 441),
          ("f19198", 440),
          ("f19200", 188),
          ("f19201", 439),
          ("f19202", 438),
          ("f19203", 437),
          ("f19205", 147),
          ("f19206", 436),
          ("f19207", 435),
          ("f19208", 434),
          ("f19210", 187),
          ("f19211", 433),
          ("f19212", 432),
          ("f19213", 431),
          ("f19215", 146),
          ("f19216", 430),
          ("f19217", 429),
          ("f19218", 428),
          ("f19220", 186),
          ("f19221", 427),
          ("f19222", 426),
          ("f19223", 425),
          ("f19225", 145),
          ("f19226", 424),
          ("f19227", 423),
          ("f19228", 422),
          ("f19230", 185),
          ("f19231", 421),
          ("f19232", 420),
          ("f19233", 419),
          ("f19235", 144),
          ("f19236", 418),
          ("f19237", 417),
          ("f19238", 416),
          ("f19240", 184),
          ("f19241", 415),
          ("f19242", 414),
          ("f19243", 413),
          ("f19245", 143),
          ("f19246", 412),
          ("f19247", 411),
          ("f19248", 410),
          ("f19250", 183),
          ("f19251", 409),
          ("f19252", 408),
          ("f19253", 407),
          ("f19255", 142),
          ("f19256", 406),
          ("f19257", 405),
          ("f19258", 404),
          ("f19260", 182),
          ("f19261", 403),
          ("f19262", 402),
          ("f19263", 401),
          ("f19265", 141),
          ("f19266", 400),
          ("f19267", 399),
          ("f19268", 398),
          ("f19270", 181),
          ("f19271", 397),
          ("f19272", 396),
          ("f19273", 395),
          ("f19275", 140),
          ("f19276", 394),
          ("f19277", 393),
          ("f19278", 392),
          ("f19280", 180),
          ("f19282", 390),
          ("f19283", 389),
          ("f19285", 139),
          ("f19286", 388),
          ("f19287", 387),
          ("f19288", 386),
          ("f19290", 179),
          ("f19291", 385),
          ("f19292", 384),
          ("f19293", 383),
          ("f19295", 138),
          ("f19296", 382),
          ("f19300", 178),
          ("f19305", 137),
          ("f19310", 177),
          ("f19311", 373),
          ("f19312", 372),
          ("f19313", 371),
          ("f19315", 136),
          ("f19316", 370),
          ("f19317", 369),
          ("f19318", 368),
          ("f19320", 176),
          ("f19321", 367),
          ("f19322", 366),
          ("f19323", 365),
          ("f19325", 135),
          ("f19326", 364),
          ("f19327", 363),
          ("f19328", 362),
          ("f19330", 175),
          ("f19331", 361),
          ("f19332", 360),
          ("f19333", 359),
          ("f19335", 134),
          ("f19336", 358),
          ("f19337", 357),
          ("f19338", 356),
          ("f19340", 174),
          ("f19341", 355),
          ("f19342", 354),
          ("f19343", 353),
          ("f19345", 133),
          ("f19346", 352),
          ("f19347", 351),
          ("f19348", 350),
          ("f19350", 173),
          ("f19351", 349),
          ("f19352", 348),
          ("f19353", 347),
          ("f19355", 132),
          ("f19356", 346),
          ("f19357", 345),
          ("f19358", 344),
          ("f19360", 172),
          ("f19361", 343),
          ("f19362", 342),
          ("f19363", 341),
          ("f19365", 131),
          ("f19366", 340),
          ("f19367", 339),
          ("f19368", 338),
          ("f19370", 171),
          ("f19371", 337),
          ("f19372", 336),
          ("f19373", 335),
          ("f19375", 130),
          ("f19376", 334),
          ("f19377", 333),
          ("f19378", 332),
          ("f19380", 170),
          ("f19381", 331),
          ("f19382", 330),
          ("f19383", 329),
          ("f19385", 129),
          ("f19386", 328),
          ("f19387", 327),
          ("f19388", 326),
          ("f19390", 169),
          ("f19391", 325),
          ("f19392", 324),
          ("f19393", 323),
          ("f19395", 128),
          ("f19396", 322),
          ("f19397", 321),
          ("f19398", 320),
          ("f19400", 168),
          ("f19401", 319),
          ("f19402", 318),
          ("f19403", 317),
          ("f19405", 127),
          ("f19406", 316),
          ("f19407", 315),
          ("f19408", 314),
          ("f19410", 167),
          ("f19411", 313),
          ("f19412", 312),
          ("f19413", 311),
          ("f19415", 126),
          ("f19416", 310),
          ("f19417", 309),
          ("f19418", 308),
          ("f19420", 166),
          ("f19421", 307),
          ("f19422", 306),
          ("f19423", 305),
          ("f19425", 125),
          ("f19426", 304),
          ("f19427", 303),
          ("f19428", 302),
          ("f19430", 165),
          ("f19431", 301),
          ("f19432", 300),
          ("f19433", 299),
          ("f19435", 124),
          ("f19436", 298),
          ("f19437", 297),
          ("f19438", 296),
          ("f19440", 164),
          ("f19441", 295),
          ("f19442", 294),
          ("f19443", 293),
          ("f19445", 123),
          ("f19446", 292),
          ("f19447", 291),
          ("f19448", 290),
          ("f19450", 163),
          ("f19451", 289),
          ("f19452", 288),
          ("f19453", 287),
          ("f19455", 122),
          ("f19456", 286),
          ("f19457", 285),
          ("f19458", 284),
          ("f19460", 162),
          ("f19461", 283),
          ("f19462", 282),
          ("f19463", 281),
          ("f19465", 121),
          ("f19466", 280),
          ("f19467", 279),
          ("f19468", 278),
          ("f19470", 161),
          ("f19471", 277),
          ("f19472", 276),
          ("f19473", 275),
          ("f19475", 120),
          ("f19476", 274),
          ("f19477", 273),
          ("f19478", 272),
          ("f19480", 160),
          ("f19481", 271),
          ("f19482", 270),
          ("f19483", 269),
          ("f19485", 119),
          ("f19486", 268),
          ("f19487", 267),
          ("f19488", 266),
          ("f19490", 159),
          ("f19491", 265),
          ("f19492", 264),
          ("f19493", 263),
          ("f19495", 118),
          ("f19496", 262),
          ("f19497", 261),
          ("f19498", 260),
          ("f19500", 158),
          ("f19501", 259),
          ("f19502", 258),
          ("f19503", 257),
          ("f19505", 117),
          ("f19506", 256),
          ("f19507", 255),
          ("f19508", 254),
          ("f19510", 157),
          ("f19511", 253),
          ("f19512", 252),
          ("f19513", 251),
          ("f19515", 116),
          ("f19516", 250),
          ("f19517", 249),
          ("f19518", 248),
          ("f19520", 156),
          ("f19521", 247),
          ("f19522", 246),
          ("f19523", 245),
          ("f19525", 115),
          ("f19526", 244),
          ("f19527", 243),
          ("f19528", 242),
          ("f19530", 155),
          ("f19531", 241),
          ("f19532", 240),
          ("f19533", 239),
          ("f19535", 114),
          ("f19536", 238),
          ("f19537", 237),
          ("f19538", 236),
          ("f19540", 154),
          ("f19541", 235),
          ("f19542", 234),
          ("f19543", 233),
          ("f19545", 113),
          ("f19546", 232),
          ("f19547", 231),
          ("f19548", 230),
          ("f19550", 153),
          ("f19551", 229),
          ("f19552", 228),
          ("f19553", 227),
          ("f19555", 112),
          ("f19556", 226),
          ("f19557", 225),
          ("f19558", 224),
          ("f19560", 152),
          ("f19561", 223),
          ("f19562", 222),
          ("f19563", 221),
          ("f19565", 111),
          ("f19566", 220),
          ("f19567", 219),
          ("f19568", 218),
          ("f19570", 151),
          ("f19571", 217),
          ("f19572", 216),
          ("f19573", 215),
          ("f19575", 110),
          ("f19576", 214),
          ("f19577", 213),
          ("f19578", 212),
          ("f19580", 150),
          ("f19581", 211),
          ("f19582", 210),
          ("f19583", 209),
          ("f19585", 109),
          ("f19586", 208),
          ("f19587", 207),
          ("f19588", 206),
          ("f19590", 149),
          ("f19591", 205),
          ("f19592", 204),
          ("f19593", 203),
          ("f19595", 108),
          ("f19596", 202),
          ("f19597", 201),
          ("f19598", 200),
          ("f19600", 148),
          ("f19610", 107),
          ("g1310", 102),
          ("g1550", 103),
          ("g850", 101),
          ("notDefined", 500),
          ("notInGrid", 105),
          ("s1310", 99),
          ("s1490", 199),
          ("s1510", 106),
          ("s1610", 197),
          ("s1630", 100),
          ("t1650", 198),
          ("undefined", 0))
    )



class FspR7ChannelIdentifierCaps(Bits, TextualConvention):
    status = "current"


class FspR7ChannelNumber(Integer32, TextualConvention):
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
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
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
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
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
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
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
              213,
              214,
              215)
        )
    )
    namedValues = NamedValues(
        *(("c1270", 206),
          ("c1290", 207),
          ("c1310", 208),
          ("c1330", 209),
          ("c1350", 210),
          ("c1370", 211),
          ("c1430", 212),
          ("c1450", 213),
          ("c1470", 90),
          ("c1490", 91),
          ("c1510", 92),
          ("c1530", 93),
          ("c1550", 94),
          ("c1570", 95),
          ("c1590", 96),
          ("c1610", 97),
          ("f18700", 64),
          ("f18705", 205),
          ("f18710", 63),
          ("f18715", 204),
          ("f18720", 62),
          ("f18725", 203),
          ("f18730", 61),
          ("f18735", 202),
          ("f18740", 80),
          ("f18745", 201),
          ("f18750", 60),
          ("f18755", 200),
          ("f18760", 59),
          ("f18765", 199),
          ("f18770", 58),
          ("f18775", 198),
          ("f18780", 57),
          ("f18785", 197),
          ("f18790", 79),
          ("f18795", 196),
          ("f18800", 56),
          ("f18805", 195),
          ("f18810", 55),
          ("f18815", 194),
          ("f18820", 54),
          ("f18825", 193),
          ("f18830", 53),
          ("f18835", 192),
          ("f18840", 78),
          ("f18845", 191),
          ("f18850", 52),
          ("f18855", 190),
          ("f18860", 51),
          ("f18865", 189),
          ("f18870", 50),
          ("f18875", 188),
          ("f18880", 49),
          ("f18885", 187),
          ("f18890", 77),
          ("f18895", 186),
          ("f18900", 82),
          ("f18905", 185),
          ("f18910", 76),
          ("f18915", 184),
          ("f18920", 48),
          ("f18925", 183),
          ("f18930", 47),
          ("f18935", 182),
          ("f18940", 46),
          ("f18945", 181),
          ("f18950", 45),
          ("f18955", 180),
          ("f18960", 75),
          ("f18965", 179),
          ("f18970", 44),
          ("f18975", 178),
          ("f18980", 43),
          ("f18985", 177),
          ("f18990", 42),
          ("f18995", 176),
          ("f19000", 41),
          ("f19005", 175),
          ("f19010", 74),
          ("f19015", 174),
          ("f19020", 40),
          ("f19025", 173),
          ("f19030", 39),
          ("f19035", 172),
          ("f19040", 38),
          ("f19045", 171),
          ("f19050", 37),
          ("f19055", 170),
          ("f19060", 73),
          ("f19065", 169),
          ("f19070", 36),
          ("f19075", 168),
          ("f19080", 35),
          ("f19085", 167),
          ("f19090", 34),
          ("f19095", 166),
          ("f19100", 33),
          ("f19105", 165),
          ("f19110", 164),
          ("f19115", 163),
          ("f19120", 162),
          ("f19125", 161),
          ("f19130", 160),
          ("f19135", 159),
          ("f19140", 158),
          ("f19145", 157),
          ("f19150", 156),
          ("f19155", 155),
          ("f19160", 154),
          ("f19165", 153),
          ("f19170", 152),
          ("f19175", 151),
          ("f19180", 150),
          ("f19185", 149),
          ("f19190", 148),
          ("f19195", 147),
          ("f19200", 32),
          ("f19205", 146),
          ("f19210", 31),
          ("f19215", 145),
          ("f19220", 30),
          ("f19225", 144),
          ("f19230", 29),
          ("f19235", 143),
          ("f19240", 72),
          ("f19245", 142),
          ("f19250", 28),
          ("f19255", 141),
          ("f19260", 27),
          ("f19265", 140),
          ("f19270", 26),
          ("f19275", 139),
          ("f19280", 25),
          ("f19285", 138),
          ("f19290", 71),
          ("f19295", 137),
          ("f19300", 24),
          ("f19305", 136),
          ("f19310", 23),
          ("f19315", 135),
          ("f19320", 22),
          ("f19325", 134),
          ("f19330", 21),
          ("f19335", 133),
          ("f19340", 70),
          ("f19345", 132),
          ("f19350", 20),
          ("f19355", 131),
          ("f19360", 19),
          ("f19365", 130),
          ("f19370", 18),
          ("f19375", 129),
          ("f19380", 17),
          ("f19385", 128),
          ("f19390", 69),
          ("f19395", 127),
          ("f19400", 81),
          ("f19405", 126),
          ("f19410", 68),
          ("f19415", 125),
          ("f19420", 16),
          ("f19425", 124),
          ("f19430", 15),
          ("f19435", 123),
          ("f19440", 14),
          ("f19445", 122),
          ("f19450", 13),
          ("f19455", 121),
          ("f19460", 67),
          ("f19465", 120),
          ("f19470", 12),
          ("f19475", 119),
          ("f19480", 11),
          ("f19485", 118),
          ("f19490", 10),
          ("f19495", 117),
          ("f19500", 9),
          ("f19505", 116),
          ("f19510", 66),
          ("f19515", 115),
          ("f19520", 8),
          ("f19525", 114),
          ("f19530", 7),
          ("f19535", 113),
          ("f19540", 6),
          ("f19545", 112),
          ("f19550", 5),
          ("f19555", 111),
          ("f19560", 65),
          ("f19565", 110),
          ("f19570", 4),
          ("f19575", 109),
          ("f19580", 3),
          ("f19585", 108),
          ("f19590", 2),
          ("f19595", 107),
          ("f19600", 1),
          ("f19605", 89),
          ("f19610", 106),
          ("f19615", 88),
          ("f19620", 87),
          ("f19625", 86),
          ("f19630", 85),
          ("f19635", 84),
          ("f19640", 83),
          ("g1310", 101),
          ("g1550", 102),
          ("g850", 100),
          ("nig", 104),
          ("null", 103),
          ("s1310", 98),
          ("s1490", 215),
          ("s1510", 105),
          ("s1630", 99),
          ("t1650", 214),
          ("undefined", 0))
    )



class FspR7ChannelNumberCaps(Bits, TextualConvention):
    status = "current"


class FspR7ChannelSpacing(Integer32, TextualConvention):
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
        *(("spacing100Ghz", 2),
          ("spacing200Ghz", 3),
          ("spacing25GHz", 4),
          ("spacing50Ghz", 1),
          ("spacingFlex", 5),
          ("undefined", 0))
    )



class FspR7ChannelSpacingCaps(Bits, TextualConvention):
    status = "current"


class FspR7CodeGain(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("mean", 2),
          ("undefined", 0))
    )



class FspR7CodeGainCaps(Bits, TextualConvention):
    status = "current"


class FspR7ColumnMark(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2),
          ("undefined", 0))
    )



class FspR7Conn(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bi", 1),
          ("undefined", 0),
          ("uni", 2))
    )



class FspR7ConnCaps(Bits, TextualConvention):
    status = "current"


class FspR7ConnectorType(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("din", 11),
          ("dsub44hd", 6),
          ("dsub8", 4),
          ("fcApc", 7),
          ("hdBnc", 10),
          ("lc", 1),
          ("mbnc", 9),
          ("mpo", 8),
          ("mupc", 3),
          ("rj45", 2),
          ("undefined", 0),
          ("usbS", 5))
    )



class FspR7ConnectorTypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7ConnectState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("busy", 4),
          ("idle", 1),
          ("idleReceive", 2),
          ("idleTransmit", 3),
          ("undefined", 0))
    )



class FspR7CpAuthType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("simple", 2),
          ("undefined", 0))
    )



class FspR7CpAuthTypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7DCFiberType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleMode", 1),
          ("trueWaveRs", 2),
          ("undefined", 0))
    )



class FspR7DCFiberTypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7DeploymentScenario(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("backToBack", 2),
          ("clientProt", 3),
          ("generic", 1),
          ("passThrough", 4),
          ("undefined", 0))
    )



class FspR7DeploymentScenarioCaps(Bits, TextualConvention):
    status = "current"


class FspR7DisableEnable(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("undefined", 0))
    )



class FspR7DisableEnableCaps(Bits, TextualConvention):
    status = "current"


class FspR7DispersionCompensation(Integer32, TextualConvention):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("dispertion10", 1),
          ("dispertion100", 6),
          ("dispertion160", 11),
          ("dispertion20", 2),
          ("dispertion240", 12),
          ("dispertion30", 7),
          ("dispertion320", 13),
          ("dispertion40", 3),
          ("dispertion50", 8),
          ("dispertion60", 4),
          ("dispertion70", 9),
          ("dispertion80", 5),
          ("dispertion90", 10),
          ("undefined", 0))
    )



class FspR7DispersionCompensationCaps(Bits, TextualConvention):
    status = "current"


class FspR7DispersionConfig(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oprCdc", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class FspR7DispersionConfigCaps(Bits, TextualConvention):
    status = "current"


class FspR7DispersionModes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("man", 2),
          ("undefined", 0))
    )



class FspR7DispersionModesCaps(Bits, TextualConvention):
    status = "current"


class FspR7EocProtAvailability(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("undefined", 0),
          ("yes", 2))
    )



class FspR7EdfaOutputPowerRating(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("pwrOut10", 1),
          ("pwrOut15", 5),
          ("pwrOut17", 2),
          ("pwrOut18", 3),
          ("pwrOut20", 4),
          ("pwrOut20UN10NU", 8),
          ("pwrOut26", 7),
          ("pwrOut27", 6),
          ("undefined", 0))
    )



class FspR7EdfaOutputPowerRatingCaps(Bits, TextualConvention):
    status = "current"


class FspR7EnableDisable(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("undefined", 0))
    )



class FspR7EnableDisableCaps(Bits, TextualConvention):
    status = "current"


class FspR7EncapsulationMethod(Integer32, TextualConvention):
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
        *(("gfpF", 5),
          ("gfpT", 4),
          ("gmp", 3),
          ("none", 1),
          ("tttgmp", 2),
          ("undefined", 0))
    )



class FspR7EntitySecondaryStates(Bits, TextualConvention):
    status = "current"


class FspR7EntityType(Integer32, TextualConvention):
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
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
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
              122,
              123,
              124,
              125,
              126,
              127,
              130,
              131,
              132,
              133,
              137,
              138,
              140,
              141,
              142,
              143,
              148,
              149,
              150,
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
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              180,
              182,
              183,
              185,
              186,
              187,
              188,
              190,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              234,
              235,
              236,
              237,
              239,
              240,
              241,
              242,
              243,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              260,
              261,
              499,
              501,
              502,
              503,
              504,
              505,
              506,
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
              524,
              525,
              526,
              527,
              528,
              529,
              534,
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
              554,
              555,
              556,
              557,
              558,
              559,
              560,
              561,
              562,
              564,
              565,
              566,
              567,
              569,
              570,
              571,
              572,
              573,
              574,
              575,
              576,
              577,
              578,
              579,
              580,
              581,
              582,
              583,
              584,
              585,
              586,
              587,
              588,
              589,
              590,
              591,
              592,
              593,
              594,
              595,
              596,
              597,
              598,
              599,
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
              616,
              617,
              618,
              619,
              620,
              621,
              622,
              623,
              624,
              625,
              626,
              627,
              628,
              629,
              630,
              631,
              632,
              633,
              634,
              635,
              636,
              637,
              638,
              639,
              640,
              641,
              642,
              643,
              644,
              645,
              646,
              647,
              648,
              649,
              650,
              651,
              652,
              653,
              654,
              660,
              661,
              662,
              663,
              664,
              665,
              667,
              668,
              669,
              670,
              673,
              674,
              678,
              681,
              684,
              685,
              688,
              689,
              692,
              693,
              694,
              695,
              699,
              700,
              701,
              702,
              703,
              704,
              705,
              1000,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1101,
              1102,
              1103,
              1104,
              1105,
              1106,
              1107,
              1108,
              1109)
        )
    )
    namedValues = NamedValues(
        *(("conFanContainer", 1101),
          ("conModContainer", 1102),
          ("conPlugContainer", 1103),
          ("eqp10Tce100Gb", 251),
          ("eqp10Tce100gAes", 252),
          ("eqp10Wxc10g", 220),
          ("eqp10pca10g", 151),
          ("eqp10tcc100gtbD", 223),
          ("eqp10tcc10g", 186),
          ("eqp10tcc10gc", 111),
          ("eqp10tcc10gd", 110),
          ("eqp10tcc10gtd", 109),
          ("eqp10tccSdi10g", 242),
          ("eqp10tccs10gtd", 165),
          ("eqp10tce100g", 215),
          ("eqp10tce100gGf", 228),
          ("eqp11RoadmC96", 196),
          ("eqp16csmSfd", 112),
          ("eqp1Gsmud", 32),
          ("eqp1csmuD", 152),
          ("eqp1csmuEwD", 88),
          ("eqp1csmuG", 89),
          ("eqp1csmuc", 35),
          ("eqp1csmuewc", 36),
          ("eqp1pm", 41),
          ("eqp20Pca10G", 133),
          ("eqp2EdfaS20S10", 250),
          ("eqp2Raman", 192),
          ("eqp2RamanC15", 202),
          ("eqp2Tca2g5s", 91),
          ("eqp2Tcm2g5c", 99),
          ("eqp2Tcm2g5d", 98),
          ("eqp2Twcc2g7", 127),
          ("eqp2Wca10g", 130),
          ("eqp2Wcc10g", 177),
          ("eqp2Wcc10gAes", 180),
          ("eqp2absmc", 30),
          ("eqp2bsmd", 31),
          ("eqp2clsmSfd", 114),
          ("eqp2clsmd", 29),
          ("eqp2csmuEwc", 119),
          ("eqp2oscm", 76),
          ("eqp2otfm", 171),
          ("eqp2pca10g", 150),
          ("eqp2pm", 42),
          ("eqp2psm", 218),
          ("eqp2tca2g5", 58),
          ("eqp2tcm2g5", 57),
          ("eqp3BsmC", 90),
          ("eqp3bsmEwc", 115),
          ("eqp40Csm2hu", 126),
          ("eqp40Csm3huD", 161),
          ("eqp40Csm3huDi", 174),
          ("eqp40Csm3hudcD", 166),
          ("eqp40Csm3hudcDi", 167),
          ("eqp40csmd", 43),
          ("eqp4CfptD", 217),
          ("eqp4Tca4g", 96),
          ("eqp4Tcc10gtd", 95),
          ("eqp4Tcc40gtd", 149),
          ("eqp4Wce16g", 225),
          ("eqp4csmc", 39),
          ("eqp4csmd", 37),
          ("eqp4csmud", 38),
          ("eqp4gsmd", 33),
          ("eqp4opcm", 123),
          ("eqp4roadmC96", 239),
          ("eqp4roadmEC96", 243),
          ("eqp4tca1g3c", 67),
          ("eqp4tca1g3d", 66),
          ("eqp4tca4gc", 64),
          ("eqp4tca4gd", 63),
          ("eqp4tca4gus", 160),
          ("eqp4tcc10gc", 52),
          ("eqp4tcc10gd", 51),
          ("eqp4tcc2g5", 49),
          ("eqp4tcc2g5d", 50),
          ("eqp5gsmD", 169),
          ("eqp5psm", 162),
          ("eqp5tce10g", 235),
          ("eqp5tce10gaes", 234),
          ("eqp5tce10gtaesd", 182),
          ("eqp5tce10gtd", 164),
          ("eqp5tces10g", 237),
          ("eqp5tces10gaes", 236),
          ("eqp5tces10gtaesd", 214),
          ("eqp5tces10gtd", 194),
          ("eqp5wca16G", 260),
          ("eqp8AdmC96", 197),
          ("eqp8CcmC80", 175),
          ("eqp8Csmuc", 92),
          ("eqp8CxmC96", 198),
          ("eqp8RoadmC80", 178),
          ("eqp8Shm", 199),
          ("eqp8TceGl2g5c", 107),
          ("eqp8TceGl2g5d", 106),
          ("eqp8csmD", 170),
          ("eqp8gsmd", 34),
          ("eqp8otdr3hu", 172),
          ("eqp8psm", 255),
          ("eqp8roadmC40", 148),
          ("eqp8tca10gc", 60),
          ("eqp8tca10gd", 59),
          ("eqp8tce2g5c", 69),
          ("eqp8tce2g5d", 68),
          ("eqp96Csm4HuD", 216),
          ("eqp9RoadmC96", 224),
          ("eqp9ccmC96", 256),
          ("eqpAmpShgcv", 200),
          ("eqpAmpSlgcv", 201),
          ("eqpCem9hu", 143),
          ("eqpCfp10g", 205),
          ("eqpCfp4g", 204),
          ("eqpCfptCd", 261),
          ("eqpCustomc", 84),
          ("eqpCustomd", 85),
          ("eqpDcf", 44),
          ("eqpDcf1hu", 108),
          ("eqpDcg", 97),
          ("eqpDcm", 7),
          ("eqpDrm", 77),
          ("eqpEdfaD27", 176),
          ("eqpEdfaDgcb", 93),
          ("eqpEdfaDgcv", 117),
          ("eqpEdfaS20", 241),
          ("eqpEdfaS26", 193),
          ("eqpEdfaSgcb", 116),
          ("eqpEdfadgc", 47),
          ("eqpEdfas", 45),
          ("eqpEdfasgc", 46),
          ("eqpEdfmSgc", 102),
          ("eqpEroadmDc", 120),
          ("eqpF2kDemiV2", 103),
          ("eqpF2kSh5hu", 5),
          ("eqpF2kSh6hu", 6),
          ("eqpFan1hu", 185),
          ("eqpFan9hu", 163),
          ("eqpFcu7hu", 28),
          ("eqpIlm", 141),
          ("eqpNcu", 20),
          ("eqpNcu20085hu", 132),
          ("eqpNcu2e", 105),
          ("eqpNcu2p", 188),
          ("eqpNcuHp", 131),
          ("eqpNcuII", 142),
          ("eqpNcutif", 21),
          ("eqpOscm", 75),
          ("eqpOscmPn", 94),
          ("eqpOsfm", 40),
          ("eqpOsfmSf", 113),
          ("eqpPscu", 125),
          ("eqpPsm", 104),
          ("eqpPsu1huac", 25),
          ("eqpPsu1hudc", 86),
          ("eqpPsu7huac", 26),
          ("eqpPsu7hudc", 27),
          ("eqpPsu9huac", 190),
          ("eqpPsu9hudc", 159),
          ("eqpPtp", 499),
          ("eqpR6cu", 24),
          ("eqpRaman", 48),
          ("eqpRoadmC80", 157),
          ("eqpRsmolm", 73),
          ("eqpRsmsf", 74),
          ("eqpScu", 22),
          ("eqpScuII", 195),
          ("eqpScuS", 122),
          ("eqpScue", 23),
          ("eqpSfp2RxG", 247),
          ("eqpSfp2Rxe", 249),
          ("eqpSfp2TxG", 246),
          ("eqpSfp2Txe", 248),
          ("eqpSfpBG", 226),
          ("eqpSfpCdrC", 229),
          ("eqpSfpCdrD", 253),
          ("eqpSfpCdrG", 227),
          ("eqpSfpOdC", 154),
          ("eqpSfpOdG", 156),
          ("eqpSfpOsC", 153),
          ("eqpSfpOsG", 155),
          ("eqpSfpc", 80),
          ("eqpSfpe", 82),
          ("eqpSfpg", 81),
          ("eqpSfptD", 245),
          ("eqpSh1hu", 1),
          ("eqpSh1huDc", 2),
          ("eqpSh1huDcEtemp", 254),
          ("eqpSh1hudcm", 83),
          ("eqpSh1hupf", 183),
          ("eqpSh3hu", 3),
          ("eqpSh7hu", 4),
          ("eqpSh9hu", 8),
          ("eqpUnknown", 19),
          ("eqpUtm", 124),
          ("eqpVsm", 72),
          ("eqpWca10gc", 62),
          ("eqpWca10gd", 61),
          ("eqpWcc100gtD", 203),
          ("eqpWcc100gtbD", 240),
          ("eqpWcc10gc", 54),
          ("eqpWcc10gd", 53),
          ("eqpWcc10gtd", 118),
          ("eqpWcc2g71N", 55),
          ("eqpWcc2g7c", 87),
          ("eqpWcc2g7d", 56),
          ("eqpWcc40gtd", 140),
          ("eqpWce100G", 219),
          ("eqpWce100GB", 257),
          ("eqpWcelsc", 71),
          ("eqpWcelsd", 70),
          ("eqpWcm2g5c", 101),
          ("eqpWcm2g5d", 100),
          ("eqpXfpC", 137),
          ("eqpXfpD", 138),
          ("eqpXfpG", 78),
          ("eqpXfpOtnD", 187),
          ("eqpXfpTlnD", 213),
          ("eqpXfptD", 173),
          ("eqpccm8", 158),
          ("eqpsfpd", 79),
          ("eqpwca2g5", 65),
          ("fanContainer", 1107),
          ("filterCable", 1109),
          ("grpConn", 1004),
          ("grpCrsCh", 1104),
          ("grpCrsDcn", 1002),
          ("grpLanDcn", 1003),
          ("grpVirtualConn", 1006),
          ("grpffpCh", 1000),
          ("grpffpOm", 1001),
          ("grpffpVchN", 1005),
          ("ifType1000BaseT", 640),
          ("ifType100GbE", 660),
          ("ifType10GFC", 508),
          ("ifType10GbE", 503),
          ("ifType10GbELan", 663),
          ("ifType10GbEWan", 662),
          ("ifType10Gdw", 575),
          ("ifType10Gib", 628),
          ("ifType1GbE", 541),
          ("ifType1GbETH", 584),
          ("ifType2GCL", 540),
          ("ifType2GFC", 539),
          ("ifType2R", 560),
          ("ifType40GbE", 692),
          ("ifType4Gfc", 558),
          ("ifType5Gib", 649),
          ("ifType8Gfc", 627),
          ("ifTypeAdapt", 566),
          ("ifTypeAdaptd", 567),
          ("ifTypeBridge", 639),
          ("ifTypeCl", 538),
          ("ifTypeCtrans", 620),
          ("ifTypeDccL", 521),
          ("ifTypeDccP", 523),
          ("ifTypeDccS", 522),
          ("ifTypeDownMep", 625),
          ("ifTypeE100fx", 537),
          ("ifTypeE10or100bt", 536),
          ("ifTypeEdfa", 573),
          ("ifTypeEdfaMid", 574),
          ("ifTypeElan", 619),
          ("ifTypeEline", 618),
          ("ifTypeElinePPP", 616),
          ("ifTypeEncapIp", 601),
          ("ifTypeEoc", 542),
          ("ifTypeEtree", 617),
          ("ifTypeF10000", 629),
          ("ifTypeF10137", 705),
          ("ifTypeF10312", 516),
          ("ifTypeF103125", 695),
          ("ifTypeF10518", 517),
          ("ifTypeF1062", 510),
          ("ifTypeF10664", 605),
          ("ifTypeF10709", 554),
          ("ifTypeF11049", 644),
          ("ifTypeF11095", 555),
          ("ifTypeF11318", 556),
          ("ifTypeF1228", 699),
          ("ifTypeF125", 513),
          ("ifTypeF1250", 511),
          ("ifTypeF14025", 678),
          ("ifTypeF1483", 688),
          ("ifTypeF1485", 684),
          ("ifTypeF155", 548),
          ("ifTypeF166", 591),
          ("ifTypeF197", 580),
          ("ifTypeF200", 514),
          ("ifTypeF2125", 550),
          ("ifTypeF2457", 700),
          ("ifTypeF2488", 518),
          ("ifTypeF2500", 545),
          ("ifTypeF2666", 551),
          ("ifTypeF270", 681),
          ("ifTypeF2967", 689),
          ("ifTypeF2970", 685),
          ("ifTypeF3072", 701),
          ("ifTypeF39813", 607),
          ("ifTypeF41250", 694),
          ("ifTypeF4250", 552),
          ("ifTypeF4915", 702),
          ("ifTypeF5000", 650),
          ("ifTypeF6144", 703),
          ("ifTypeF622", 549),
          ("ifTypeF666", 592),
          ("ifTypeF8500", 610),
          ("ifTypeF9830", 704),
          ("ifTypeF9953", 515),
          ("ifTypeFC", 512),
          ("ifTypeFMep", 626),
          ("ifTypeFcu", 653),
          ("ifTypeFlowPoint", 614),
          ("ifTypeGBEFR", 569),
          ("ifTypeGcc0", 525),
          ("ifTypeGcc0S", 559),
          ("ifTypeGcc1", 526),
          ("ifTypeGcc2", 527),
          ("ifTypeGfpF", 519),
          ("ifTypeGfpT", 520),
          ("ifTypeI2C", 593),
          ("ifTypeIpWhiteList", 599),
          ("ifTypeLag", 615),
          ("ifTypeLanIp", 562),
          ("ifTypeLifIP", 594),
          ("ifTypeLifPbNum", 647),
          ("ifTypeLifSubUnn", 648),
          ("ifTypeLifVTeNum", 673),
          ("ifTypeLifVTeUnn", 674),
          ("ifTypeLifte", 597),
          ("ifTypeLifteNum", 645),
          ("ifTypeLifteUnn", 646),
          ("ifTypeLs", 557),
          ("ifTypeMa", 624),
          ("ifTypeMaComp", 638),
          ("ifTypeMaNet", 637),
          ("ifTypeMd", 623),
          ("ifTypeModem", 565),
          ("ifTypeOc12", 588),
          ("ifTypeOc192", 504),
          ("ifTypeOc3", 587),
          ("ifTypeOc48", 505),
          ("ifTypeOc768", 604),
          ("ifTypeOdu0", 652),
          ("ifTypeOdu1", 524),
          ("ifTypeOdu1E", 669),
          ("ifTypeOdu2", 606),
          ("ifTypeOdu2E", 668),
          ("ifTypeOdu2Lan", 670),
          ("ifTypeOdu3", 693),
          ("ifTypeOduFlx", 664),
          ("ifTypeOm", 529),
          ("ifTypeOptical", 661),
          ("ifTypeOspfIp", 600),
          ("ifTypeOt", 534),
          ("ifTypeOtdrCh", 636),
          ("ifTypeOtlc", 665),
          ("ifTypeOtu1", 501),
          ("ifTypeOtu1E", 642),
          ("ifTypeOtu1Fc", 578),
          ("ifTypeOtu1Fc2G", 579),
          ("ifTypeOtu1Lan", 577),
          ("ifTypeOtu1Stm1", 589),
          ("ifTypeOtu1Stm4", 590),
          ("ifTypeOtu2", 502),
          ("ifTypeOtu2E", 641),
          ("ifTypeOtu2F", 643),
          ("ifTypeOtu2Lan", 576),
          ("ifTypeOtu2eEth", 651),
          ("ifTypeOtu2p", 634),
          ("ifTypeOtu2pFC", 632),
          ("ifTypeOtu2pFC8", 630),
          ("ifTypeOtu2pIB", 631),
          ("ifTypeOtu2pLAN", 633),
          ("ifTypeOtu2ps", 667),
          ("ifTypeOtu3", 602),
          ("ifTypeOtu4", 654),
          ("ifTypePassive", 544),
          ("ifTypePb", 611),
          ("ifTypePolicer", 612),
          ("ifTypePppIp", 561),
          ("ifTypeQueue", 613),
          ("ifTypeRaman", 598),
          ("ifTypeSc", 546),
          ("ifTypeSerial", 564),
          ("ifTypeStm1", 585),
          ("ifTypeStm16", 506),
          ("ifTypeStm256", 603),
          ("ifTypeStm4", 586),
          ("ifTypeStm64", 507),
          ("ifTypeSts1", 572),
          ("ifTypeSts24c", 595),
          ("ifTypeSts3c", 582),
          ("ifTypeSts48c", 596),
          ("ifTypeSwitch", 543),
          ("ifTypeTif", 581),
          ("ifTypeTug", 622),
          ("ifTypeUch", 547),
          ("ifTypeUpMep", 635),
          ("ifTypeVc3", 571),
          ("ifTypeVc4", 570),
          ("ifTypeVc4c16", 609),
          ("ifTypeVc4c8", 608),
          ("ifTypeVs0", 621),
          ("ifTypeVs1", 583),
          ("ifTypeoch", 528),
          ("physTermPoint", 1105),
          ("protectionCable", 1108),
          ("undefined", 0),
          ("virtualTermPoint", 1106))
    )



class FspR7EqlzAdminState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("undefined", 0))
    )



class FspR7EqlzAdminStateCaps(Bits, TextualConvention):
    status = "current"


class FspR7ErrorFwdMode(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("ais", 1),
          ("epc", 2),
          ("idle", 3),
          ("lsrBrk", 5),
          ("lsrOff", 4),
          ("txOff", 6),
          ("undefined", 0))
    )



class FspR7ErrorFwdModeCaps(Bits, TextualConvention):
    status = "current"


class FspR7FanMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eco", 1),
          ("high1", 2),
          ("undefined", 0))
    )



class FspR7FanProfile(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eco", 1),
          ("high1", 2),
          ("undefined", 0))
    )



class FspR7FDStatus(Integer32, TextualConvention):
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
        *(("disabledAdmin", 5),
          ("disabledModule", 3),
          ("disabledPtp", 4),
          ("disabledSystem", 2),
          ("enabled", 1),
          ("undefined", 0))
    )



class FspR7FDStatusCaps(Bits, TextualConvention):
    status = "current"


class FspR7FecType(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("eFec", 2),
          ("eFec1", 4),
          ("eFec2", 5),
          ("eFec3", 6),
          ("eFec4", 7),
          ("eFec5", 9),
          ("eFec6", 10),
          ("eFecX", 8),
          ("gFec", 1),
          ("noFec", 3),
          ("undefined", 0))
    )



class FspR7FecTypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7FiberBrand(Integer32, TextualConvention):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("allWave", 5),
          ("g652", 1),
          ("g653", 2),
          ("g655", 3),
          ("leaf", 6),
          ("metrocor", 12),
          ("smf28e", 4),
          ("smfLs", 11),
          ("teraLight", 10),
          ("twCl", 9),
          ("twPl", 8),
          ("twRs", 7),
          ("undefined", 0))
    )



class FspR7FiberBrandCaps(Bits, TextualConvention):
    status = "current"


class FspR7FiberDetect(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("undefined", 0))
    )



class FspR7FiberDetectCaps(Bits, TextualConvention):
    status = "current"


class FspR7FlowControlMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hwControl", 2),
          ("none", 1),
          ("pause", 3),
          ("undefined", 0))
    )



class FspR7FlowControlModeCaps(Bits, TextualConvention):
    status = "current"


class FspR7ForceConfig(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 2),
          ("release", 1),
          ("undefined", 0))
    )



class FspR7ForceConfigCaps(Bits, TextualConvention):
    status = "current"


class FspR7ForcedStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("forcedDestroy", 2),
          ("undefined", 0))
    )



class FspR7ForcedStatusCaps(Bits, TextualConvention):
    status = "current"


class FspR7FrameFormat(Integer32, TextualConvention):
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("couplinglink", 7),
          ("ethernet", 4),
          ("fiberchannel", 5),
          ("infiniband", 6),
          ("notDefined", 99),
          ("otn", 1),
          ("sdh", 2),
          ("sonet", 3),
          ("transparent", 8),
          ("undefined", 0))
    )



class FspR7FrameFormatCaps(Bits, TextualConvention):
    status = "current"


class FspR7FunctionCrs(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("addDrop", 6),
          ("drop", 2),
          ("dropCont", 7),
          ("hairpin", 4),
          ("pass", 3),
          ("select", 5),
          ("undefined", 0))
    )



class FspR7FunctionCrsCaps(Bits, TextualConvention):
    status = "current"


class FspR7Gain(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gain24", 1),
          ("gain25", 2),
          ("undefined", 0))
    )



class FspR7GainCaps(Bits, TextualConvention):
    status = "current"


class FspR7GainRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2),
          ("lowUNlowNU", 3),
          ("undefined", 0))
    )



class FspR7GainRangeCaps(Bits, TextualConvention):
    status = "current"


class FspR7GropticsType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lr4", 2),
          ("sr10", 4),
          ("sr4", 1),
          ("undefined", 0),
          ("user", 3))
    )



class FspR7GropticsTypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7InitEqualization(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opr", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class FspR7InitEqualizationCaps(Bits, TextualConvention):
    status = "current"


class FspR7Integer32Caps(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d:4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class FspR7InterfaceFunction(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 6),
          ("edfa", 3),
          ("passive", 5),
          ("physicalTerm", 8),
          ("raman", 7),
          ("super", 4),
          ("switch", 2),
          ("transport", 1),
          ("undefined", 0))
    )



class FspR7InterfaceType(Integer32, TextualConvention):
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
              34,
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
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              64,
              65,
              66,
              67,
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
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
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
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              160,
              161,
              162,
              163,
              164,
              165,
              167,
              168,
              169,
              170,
              173,
              174,
              178,
              181,
              184,
              185,
              188,
              189,
              192,
              193,
              194,
              195,
              199,
              200,
              201,
              202,
              203,
              204,
              205)
        )
    )
    namedValues = NamedValues(
        *(("ifType1000BaseT", 140),
          ("ifType100GbE", 160),
          ("ifType10GFC", 8),
          ("ifType10GbE", 3),
          ("ifType10GbELan", 163),
          ("ifType10GbEWan", 162),
          ("ifType10Gdw", 75),
          ("ifType10Gib", 128),
          ("ifType1GbE", 41),
          ("ifType1GbETH", 84),
          ("ifType2GCL", 40),
          ("ifType2GFC", 39),
          ("ifType2R", 60),
          ("ifType40GbE", 192),
          ("ifType4Gfc", 58),
          ("ifType5Gib", 149),
          ("ifType8Gfc", 127),
          ("ifTypeAdapt", 66),
          ("ifTypeAdaptd", 67),
          ("ifTypeBridge", 139),
          ("ifTypeCl", 38),
          ("ifTypeCtrans", 120),
          ("ifTypeDccL", 21),
          ("ifTypeDccP", 23),
          ("ifTypeDccS", 22),
          ("ifTypeDownMep", 125),
          ("ifTypeE100fx", 37),
          ("ifTypeE10or100bt", 36),
          ("ifTypeEdfa", 73),
          ("ifTypeEdfaMid", 74),
          ("ifTypeElan", 119),
          ("ifTypeEline", 118),
          ("ifTypeElinePPP", 116),
          ("ifTypeEncapIp", 101),
          ("ifTypeEoc", 42),
          ("ifTypeEtree", 117),
          ("ifTypeF10000", 129),
          ("ifTypeF10137", 205),
          ("ifTypeF10312", 16),
          ("ifTypeF103125", 195),
          ("ifTypeF10518", 17),
          ("ifTypeF1062", 10),
          ("ifTypeF10664", 105),
          ("ifTypeF10709", 54),
          ("ifTypeF11049", 144),
          ("ifTypeF11095", 55),
          ("ifTypeF11318", 56),
          ("ifTypeF1228", 199),
          ("ifTypeF125", 13),
          ("ifTypeF1250", 11),
          ("ifTypeF14025", 178),
          ("ifTypeF1483", 188),
          ("ifTypeF1485", 184),
          ("ifTypeF155", 48),
          ("ifTypeF166", 91),
          ("ifTypeF197", 80),
          ("ifTypeF200", 14),
          ("ifTypeF2125", 50),
          ("ifTypeF2457", 200),
          ("ifTypeF2488", 18),
          ("ifTypeF2500", 45),
          ("ifTypeF2666", 51),
          ("ifTypeF270", 181),
          ("ifTypeF2967", 189),
          ("ifTypeF2970", 185),
          ("ifTypeF3072", 201),
          ("ifTypeF39813", 107),
          ("ifTypeF41250", 194),
          ("ifTypeF4250", 52),
          ("ifTypeF4915", 202),
          ("ifTypeF5000", 150),
          ("ifTypeF6144", 203),
          ("ifTypeF622", 49),
          ("ifTypeF666", 92),
          ("ifTypeF8500", 110),
          ("ifTypeF9830", 204),
          ("ifTypeF9953", 15),
          ("ifTypeFC", 12),
          ("ifTypeFMep", 126),
          ("ifTypeFcu", 153),
          ("ifTypeFlowPoint", 114),
          ("ifTypeGBEFR", 69),
          ("ifTypeGcc0", 25),
          ("ifTypeGcc0S", 59),
          ("ifTypeGcc1", 26),
          ("ifTypeGcc2", 27),
          ("ifTypeGfpF", 19),
          ("ifTypeGfpT", 20),
          ("ifTypeI2C", 93),
          ("ifTypeIpWhiteList", 99),
          ("ifTypeLag", 115),
          ("ifTypeLanIp", 62),
          ("ifTypeLifIP", 94),
          ("ifTypeLifPbNum", 147),
          ("ifTypeLifSubUnn", 148),
          ("ifTypeLifVTeNum", 173),
          ("ifTypeLifVTeUnn", 174),
          ("ifTypeLifte", 97),
          ("ifTypeLifteNum", 145),
          ("ifTypeLifteUnn", 146),
          ("ifTypeLs", 57),
          ("ifTypeMa", 124),
          ("ifTypeMaComp", 138),
          ("ifTypeMaNet", 137),
          ("ifTypeMd", 123),
          ("ifTypeModem", 65),
          ("ifTypeOc12", 88),
          ("ifTypeOc192", 4),
          ("ifTypeOc3", 87),
          ("ifTypeOc48", 5),
          ("ifTypeOc768", 104),
          ("ifTypeOdu0", 152),
          ("ifTypeOdu1", 24),
          ("ifTypeOdu1E", 169),
          ("ifTypeOdu2", 106),
          ("ifTypeOdu2E", 168),
          ("ifTypeOdu2Lan", 170),
          ("ifTypeOdu3", 193),
          ("ifTypeOduFlx", 164),
          ("ifTypeOm", 29),
          ("ifTypeOptical", 161),
          ("ifTypeOspfIp", 100),
          ("ifTypeOt", 34),
          ("ifTypeOtdrCh", 136),
          ("ifTypeOtlc", 165),
          ("ifTypeOtu1", 1),
          ("ifTypeOtu1E", 142),
          ("ifTypeOtu1Fc", 78),
          ("ifTypeOtu1Fc2G", 79),
          ("ifTypeOtu1Lan", 77),
          ("ifTypeOtu1Stm1", 89),
          ("ifTypeOtu1Stm4", 90),
          ("ifTypeOtu2", 2),
          ("ifTypeOtu2E", 141),
          ("ifTypeOtu2F", 143),
          ("ifTypeOtu2Lan", 76),
          ("ifTypeOtu2eEth", 151),
          ("ifTypeOtu2p", 134),
          ("ifTypeOtu2pFC", 132),
          ("ifTypeOtu2pFC8", 130),
          ("ifTypeOtu2pIB", 131),
          ("ifTypeOtu2pLAN", 133),
          ("ifTypeOtu2ps", 167),
          ("ifTypeOtu3", 102),
          ("ifTypeOtu4", 154),
          ("ifTypePassive", 44),
          ("ifTypePb", 111),
          ("ifTypePolicer", 112),
          ("ifTypePppIp", 61),
          ("ifTypeQueue", 113),
          ("ifTypeRaman", 98),
          ("ifTypeSc", 46),
          ("ifTypeSerial", 64),
          ("ifTypeStm1", 85),
          ("ifTypeStm16", 6),
          ("ifTypeStm256", 103),
          ("ifTypeStm4", 86),
          ("ifTypeStm64", 7),
          ("ifTypeSts1", 72),
          ("ifTypeSts24c", 95),
          ("ifTypeSts3c", 82),
          ("ifTypeSts48c", 96),
          ("ifTypeSwitch", 43),
          ("ifTypeTif", 81),
          ("ifTypeTug", 122),
          ("ifTypeUch", 47),
          ("ifTypeUpMep", 135),
          ("ifTypeVc3", 71),
          ("ifTypeVc4", 70),
          ("ifTypeVc4c16", 109),
          ("ifTypeVc4c8", 108),
          ("ifTypeVs0", 121),
          ("ifTypeVs1", 83),
          ("ifTypeoch", 28),
          ("undefined", 0))
    )



class FspR7InterfaceTypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7InvertTelemetryInputLogic(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("almClosed", 1),
          ("almOpen", 2),
          ("undefined", 0))
    )



class FspR7InvertTelemetryInputLogicCaps(Bits, TextualConvention):
    status = "current"


class FspR7IpType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("numbered", 2),
          ("undefined", 0),
          ("unnumbered", 1))
    )



class FspR7IpTypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7IpMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 2),
          ("ipv4ipv6", 3),
          ("ipv6", 4),
          ("none", 1),
          ("undefined", 0))
    )



class FspR7IpModeCaps(Bits, TextualConvention):
    status = "current"


class FspR7Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class FspR7IPv6Type(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("numbered", 2),
          ("undefined", 0))
    )



class FspR7IPv6TypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7KeyLength(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("length2048", 1),
          ("length4096", 2),
          ("undefined", 0))
    )



class FspR7KeyLengthCaps(Bits, TextualConvention):
    status = "current"


class FspR7LacpMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("disable", 3),
          ("passive", 2),
          ("undefined", 0))
    )



class FspR7LacpModeCaps(Bits, TextualConvention):
    status = "current"


class FspR7LacpTimeout(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advaExtraShort", 1),
          ("long", 3),
          ("short", 2),
          ("undefined", 0))
    )



class FspR7LacpTimeoutCaps(Bits, TextualConvention):
    status = "current"


class FspR7LaneGroupInventory(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("f19275f19200", 5),
          ("f19355f19280", 4),
          ("f19435f19360", 3),
          ("f19515f19440", 2),
          ("f19595f19520", 1),
          ("f19600f19125", 7),
          ("f19600f19200", 6),
          ("undefined", 0))
    )



class FspR7LaneGroupInventoryCaps(Bits, TextualConvention):
    status = "current"


class FspR7LagFendState(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )



class FspR7LagIdFend(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )



class FspR7LagPorts(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )



class FspR7LagPortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type10gb", 2),
          ("type1gb", 1),
          ("undefined", 0))
    )



class FspR7LagPortTypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7LagStandby(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )



class FspR7LagState(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )



class FspR7LagSysIdFend(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class FspR7LaserDelayTimer(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enableLsrOffTm", 2),
          ("enableLsrOnTm", 3),
          ("undefined", 0))
    )



class FspR7LaserDelayTimerCaps(Bits, TextualConvention):
    status = "current"


class FspR7LaserForcedOperation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opr", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class FspR7LaserForcedOperationCaps(Bits, TextualConvention):
    status = "current"


class FspR7LineCoding(Integer32, TextualConvention):
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("dpQpsk", 4),
          ("dpsk", 2),
          ("mQam", 6),
          ("notDefined", 99),
          ("odbPsbt", 5),
          ("ofdm", 7),
          ("ookNrz", 1),
          ("qpsk", 3),
          ("undefined", 0))
    )



class FspR7LineCodingCaps(Bits, TextualConvention):
    status = "current"


class FspR7LossAttenuation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opr", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class FspR7LossAttenuationCaps(Bits, TextualConvention):
    status = "current"


class FspR7NoYes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("undefined", 0),
          ("yes", 2))
    )



class FspR7NoYesCaps(Bits, TextualConvention):
    status = "current"


class FspR7ManualAuto(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1),
          ("undefined", 0))
    )



class FspR7ManualAutoCaps(Bits, TextualConvention):
    status = "current"


class FspR7MaxBitErrorRate(Integer32, TextualConvention):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("ber1e10", 9),
          ("ber1e11", 10),
          ("ber1e12", 11),
          ("ber1e13", 12),
          ("ber1e14", 13),
          ("ber1e15", 14),
          ("ber1e2", 1),
          ("ber1e3", 2),
          ("ber1e4", 3),
          ("ber1e5", 4),
          ("ber1e6", 5),
          ("ber1e7", 6),
          ("ber1e8", 7),
          ("ber1e9", 8),
          ("undefined", 0))
    )



class FspR7MaxBitErrorRateCaps(Bits, TextualConvention):
    status = "current"


class FspR7Mapping(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frame", 1),
          ("trans", 2),
          ("undefined", 0))
    )



class FspR7MappingCaps(Bits, TextualConvention):
    status = "current"


class FspR7MonLevel(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("otnOdu", 3),
          ("otnOpu", 4),
          ("otnOtu", 2),
          ("pcs", 8),
          ("phys", 1),
          ("sonetLine", 6),
          ("sonetPath", 7),
          ("sonetSection", 5),
          ("undefined", 0))
    )



class FspR7MuxMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("otn", 2),
          ("sdhSonet", 1),
          ("undefined", 0))
    )



class FspR7MuxMethodCaps(Bits, TextualConvention):
    status = "current"


class FspR7NCTraceId(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("id1", 1),
          ("id2", 2),
          ("id3", 3),
          ("id4", 4),
          ("id5", 5),
          ("id6", 6),
          ("id7", 7),
          ("id8", 8),
          ("undefined", 0))
    )



class FspR7NCTRouteType(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("backPlane", 4),
          ("cable", 3),
          ("equipment", 5),
          ("fiber", 2),
          ("none", 1),
          ("provisioned", 6),
          ("undefined", 0))
    )



class FspR7NdpCleanup(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opr", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class FspR7NdpCleanupCaps(Bits, TextualConvention):
    status = "current"


class FspR7NewSshHostKey(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apply", 2),
          ("none", 1),
          ("undefined", 0))
    )



class FspR7NtpAdminState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dsbld", 6),
          ("is", 2),
          ("undefined", 0))
    )



class FspR7NtpSyncStatus(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("candidate", 4),
          ("discarded", 5),
          ("falseTicker", 3),
          ("inProgress", 6),
          ("noData", 1),
          ("notApplicable", 7),
          ("systemPeer", 2),
          ("undefined", 0))
    )



class FspR7NtpTest(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ntpTest", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class FspR7NtpTestStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("idle", 3),
          ("inProgress", 4),
          ("success", 1),
          ("undefined", 0))
    )



class FspR7NumberOfChannels(Integer32, TextualConvention):
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
        *(("channels20", 1),
          ("channels40", 2),
          ("channels8", 5),
          ("channels80", 3),
          ("channels96", 4),
          ("undefined", 0))
    )



class FspR7NumberOfChannelsCaps(Bits, TextualConvention):
    status = "current"


class FspR7NumberOfChannelsProv(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("channels20", 1),
          ("channels40", 2),
          ("channels80", 3),
          ("undefined", 0))
    )



class FspR7NumberOfChannelsProvCaps(Bits, TextualConvention):
    status = "current"


class FspR7OdtuType(Integer32, TextualConvention):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("odtu01", 1),
          ("odtu12", 2),
          ("odtu13", 5),
          ("odtu23", 6),
          ("odtu2dsh1", 3),
          ("odtu2dshTS", 4),
          ("odtu3dsh1", 7),
          ("odtu3dsh9", 8),
          ("odtu3dshTS", 9),
          ("odtu4dsh1", 10),
          ("odtu4dsh2", 11),
          ("odtu4dsh31", 13),
          ("odtu4dsh8", 12),
          ("odtu4dshTS", 14),
          ("undefined", 0))
    )



class FspR7OperState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("anr", 2),
          ("nr", 1),
          ("out", 3),
          ("un", 4),
          ("undefined", 0))
    )



class FspR7OpticalBand(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("bandA", 3),
          ("bandB", 4),
          ("bandC", 1),
          ("bandCandCi", 6),
          ("bandCi", 5),
          ("bandL", 2),
          ("undefined", 0))
    )



class FspR7OpticalBandCaps(Bits, TextualConvention):
    status = "current"


class FspR7OpticalFiberType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("multiMode", 2),
          ("singleMode", 1),
          ("undefined", 0))
    )



class FspR7OpticalFiberTypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7OpticalGroup(Integer32, TextualConvention):
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("d01d04", 1),
          ("d05d08", 2),
          ("d09d12", 3),
          ("d13d16", 4),
          ("d17d20", 5),
          ("d21d24", 6),
          ("d25d28", 7),
          ("d29d32", 8),
          ("d33d36", 9),
          ("d37d40", 10),
          ("d41d44", 11),
          ("d45d48", 12),
          ("d49d52", 13),
          ("d53d56", 14),
          ("d57d60", 15),
          ("d61d64", 16),
          ("f19230f19200", 26),
          ("f19270f19200", 31),
          ("f19270f19240", 25),
          ("f19310f19280", 24),
          ("f19350f19280", 30),
          ("f19350f19320", 23),
          ("f19390f19360", 22),
          ("f19430f19360", 29),
          ("f19430f19400", 21),
          ("f19470f19440", 20),
          ("f19510f19440", 28),
          ("f19510f19480", 19),
          ("f19550f19520", 18),
          ("f19590f19520", 27),
          ("f19590f19560", 17),
          ("undefined", 0))
    )



class FspR7OpticalGroupCaps(Bits, TextualConvention):
    status = "current"


class FspR7OpticalInterfaceReach(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6,
              7,
              8,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("extended", 11),
          ("hyperlong", 12),
          ("intra", 1),
          ("long", 4),
          ("longNR", 13),
          ("longn", 10),
          ("reg", 7),
          ("short", 2),
          ("shortIntra", 15),
          ("ulong", 6),
          ("ulongHaul", 14),
          ("ulongHaulC", 16),
          ("undefined", 0),
          ("vlong", 5),
          ("xlong", 8))
    )



class FspR7OpticalInterfaceReachCaps(Bits, TextualConvention):
    status = "current"


class FspR7OpticalLanes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lanesNumber4", 1),
          ("undefined", 0))
    )



class FspR7OpticalMultiplexLevel(Integer32, TextualConvention):
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("levelOm16D", 5),
          ("levelOm1C", 2),
          ("levelOm1D", 1),
          ("levelOm32D", 6),
          ("levelOm40D", 7),
          ("levelOm4C", 4),
          ("levelOm4D", 3),
          ("levelOmC", 9),
          ("levelOmD", 10),
          ("levelOt", 13),
          ("levelOtC", 12),
          ("levelOtD", 11),
          ("undefined", 0))
    )



class FspR7OpticalSubBand(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("d01d16", 1),
          ("d17d32", 2),
          ("d33d48", 3),
          ("d49d64", 4),
          ("undefined", 0))
    )



class FspR7OpticalSubBandCaps(Bits, TextualConvention):
    status = "current"


class FspR7OpuPayloadType(Integer32, TextualConvention):
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
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("pt01", 1),
          ("pt02", 2),
          ("pt03", 3),
          ("pt04", 4),
          ("pt05", 5),
          ("pt06", 6),
          ("pt07", 7),
          ("pt08", 8),
          ("pt09", 9),
          ("pt0A", 10),
          ("pt0B", 11),
          ("pt0C", 12),
          ("pt0D", 13),
          ("pt0E", 14),
          ("pt0F", 15),
          ("pt10", 16),
          ("pt11", 17),
          ("pt20", 18),
          ("pt21", 19),
          ("pt80", 20),
          ("pt81", 21),
          ("pt82", 22),
          ("pt83", 23),
          ("pt84", 24),
          ("pt85", 25),
          ("pt86", 26),
          ("pt87", 27),
          ("pt88", 28),
          ("pt89", 29),
          ("pt8A", 30),
          ("pt8B", 31),
          ("pt8C", 32),
          ("pt8D", 33),
          ("pt8E", 34),
          ("pt8F", 35),
          ("ptFD", 36),
          ("ptFE", 37),
          ("undefined", 0))
    )



class FspR7OpuPayloadTypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7OptUpdate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opr", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class FspR7OptUpdateCaps(Bits, TextualConvention):
    status = "current"


class FspR7OscChannel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              99,
              100,
              106,
              197)
        )
    )
    namedValues = NamedValues(
        *(("s1310", 99),
          ("s1510", 106),
          ("s1610", 197),
          ("s1630", 100),
          ("undefined", 0))
    )



class FspR7OscChannelCaps(Bits, TextualConvention):
    status = "current"


class FspR7OscUsage(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("oscrx", 3),
          ("osctxandrx", 4),
          ("osctxctrl", 2),
          ("undefined", 0))
    )



class FspR7OscUsageCaps(Bits, TextualConvention):
    status = "current"


class FspR7OspfMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("passive", 3),
          ("undefined", 0))
    )



class FspR7OspfModeCaps(Bits, TextualConvention):
    status = "current"


class FspR7OtdrPeriod(Integer32, TextualConvention):
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
        *(("period20ms", 3),
          ("period40ms", 4),
          ("period5ms", 2),
          ("period60ms", 5),
          ("periodNone", 1),
          ("undefined", 0))
    )



class FspR7OtdrPeriodCaps(Bits, TextualConvention):
    status = "current"


class FspR7ParityBit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("undefined", 0))
    )



class FspR7ParityBitCaps(Bits, TextualConvention):
    status = "current"


class FspR7PathNode(Integer32, TextualConvention):
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
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
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
              118)
        )
    )
    namedValues = NamedValues(
        *(("node1", 1),
          ("node10", 10),
          ("node100", 100),
          ("node101", 101),
          ("node102", 102),
          ("node103", 103),
          ("node104", 104),
          ("node105", 105),
          ("node106", 106),
          ("node107", 107),
          ("node108", 108),
          ("node109", 109),
          ("node11", 11),
          ("node110", 110),
          ("node111", 111),
          ("node112", 112),
          ("node113", 113),
          ("node114", 114),
          ("node115", 115),
          ("node116", 116),
          ("node117", 117),
          ("node118", 118),
          ("node12", 12),
          ("node13", 13),
          ("node14", 14),
          ("node15", 15),
          ("node16", 16),
          ("node17", 17),
          ("node18", 18),
          ("node19", 19),
          ("node2", 2),
          ("node20", 20),
          ("node21", 21),
          ("node22", 22),
          ("node23", 23),
          ("node24", 24),
          ("node25", 25),
          ("node26", 26),
          ("node27", 27),
          ("node28", 28),
          ("node29", 29),
          ("node3", 3),
          ("node30", 30),
          ("node31", 31),
          ("node32", 32),
          ("node33", 33),
          ("node34", 34),
          ("node35", 35),
          ("node36", 36),
          ("node37", 37),
          ("node38", 38),
          ("node39", 39),
          ("node4", 4),
          ("node40", 40),
          ("node41", 41),
          ("node42", 42),
          ("node43", 43),
          ("node44", 44),
          ("node45", 45),
          ("node46", 46),
          ("node47", 47),
          ("node48", 48),
          ("node49", 49),
          ("node5", 5),
          ("node50", 50),
          ("node51", 51),
          ("node52", 52),
          ("node53", 53),
          ("node54", 54),
          ("node55", 55),
          ("node56", 56),
          ("node57", 57),
          ("node58", 58),
          ("node59", 59),
          ("node6", 6),
          ("node60", 60),
          ("node61", 61),
          ("node62", 62),
          ("node63", 63),
          ("node64", 64),
          ("node65", 65),
          ("node66", 66),
          ("node67", 67),
          ("node68", 68),
          ("node69", 69),
          ("node7", 7),
          ("node70", 70),
          ("node71", 71),
          ("node72", 72),
          ("node73", 73),
          ("node74", 74),
          ("node75", 75),
          ("node76", 76),
          ("node77", 77),
          ("node78", 78),
          ("node79", 79),
          ("node8", 8),
          ("node80", 80),
          ("node81", 81),
          ("node82", 82),
          ("node83", 83),
          ("node84", 84),
          ("node85", 85),
          ("node86", 86),
          ("node87", 87),
          ("node88", 88),
          ("node89", 89),
          ("node9", 9),
          ("node90", 90),
          ("node91", 91),
          ("node92", 92),
          ("node93", 93),
          ("node94", 94),
          ("node95", 95),
          ("node96", 96),
          ("node97", 97),
          ("node98", 98),
          ("node99", 99),
          ("undefined", 0))
    )



class FspR7PathNodeCaps(Bits, TextualConvention):
    status = "current"


class FspR7PathProt(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("protected", 4),
          ("undefined", 0),
          ("unprotActive", 2),
          ("unprotIdle", 3))
    )



class FspR7PlugDataRate(Integer32, TextualConvention):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("any", 8),
          ("rate103G", 13),
          ("rate10G", 7),
          ("rate10G2R", 11),
          ("rate112G", 14),
          ("rate11G", 9),
          ("rate16G", 15),
          ("rate2G1", 4),
          ("rate2G5", 5),
          ("rate3gSdi", 16),
          ("rate4G", 6),
          ("rate8G", 12),
          ("rateCouplingLink", 1),
          ("rateFE", 10),
          ("rateGBe", 3),
          ("rateHighSpeed", 2),
          ("undefined", 0))
    )



class FspR7PlugDataRateCaps(Bits, TextualConvention):
    status = "current"


class FspR7PmReset(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("curr", 3),
          ("none", 1),
          ("undefined", 0))
    )



class FspR7PmResetCaps(Bits, TextualConvention):
    status = "current"


class FspR7PmSnapshotStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("error", 4),
          ("inProgress", 2),
          ("none", 1),
          ("success", 3),
          ("undefined", 0))
    )



class FspR7PmSnapshotParameterTypes(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("attenuation", 3),
          ("attenuationOfVoa", 4),
          ("backreflectionPowerReceived", 6),
          ("inputPower", 2),
          ("oscGain", 5),
          ("oscPowerReceived", 8),
          ("outputPower", 1),
          ("ramanPumpPower", 7),
          ("rxLineAttenuation", 11),
          ("txLineAttenuation", 10),
          ("undefined", 0),
          ("variableGain", 9))
    )



class FspR7PortBehaviour(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("network", 2),
          ("undefined", 0))
    )



class FspR7PortBehaviourCaps(Bits, TextualConvention):
    status = "current"


class FspR7PortMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cTag", 2),
          ("port", 1),
          ("sTag", 3),
          ("undefined", 0))
    )



class FspR7PortModeCaps(Bits, TextualConvention):
    status = "current"


class FspR7PortRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iNni", 2),
          ("nni", 3),
          ("undefined", 0),
          ("uni", 1))
    )



class FspR7PortRoleCaps(Bits, TextualConvention):
    status = "current"


class FspR7PrbsPmReset(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("none", 1),
          ("undefined", 0))
    )



class FspR7PrbsPmResetCaps(Bits, TextualConvention):
    status = "current"


class FspR7ProtectionRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("protn", 2),
          ("undefined", 0),
          ("wkg", 1))
    )



class FspR7ProtectionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dpring", 1),
          ("line", 2),
          ("undefined", 0))
    )



class FspR7ProtectionTypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7Protocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("ospf", 3),
          ("static", 2),
          ("undefined", 0))
    )



class FspR7PsuOutputPower(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("pwrOut0w", 8),
          ("pwrOut1000w", 7),
          ("pwrOut120w", 1),
          ("pwrOut130w", 2),
          ("pwrOut150w", 10),
          ("pwrOut170w", 5),
          ("pwrOut200w", 6),
          ("pwrOut400w", 3),
          ("pwrOut600w", 4),
          ("pwrOut800w", 9),
          ("undefined", 0))
    )



class FspR7PsuOutputPowerCaps(Bits, TextualConvention):
    status = "current"


class FspR7RedLinedState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("undefined", 0),
          ("yes", 1))
    )



class FspR7RedLinedStateCaps(Bits, TextualConvention):
    status = "current"


class FspR7RenewMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2),
          ("undefined", 0))
    )



class FspR7RenewModeCaps(Bits, TextualConvention):
    status = "current"


class FspR7RlsMan(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("man", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class FspR7RlsManCaps(Bits, TextualConvention):
    status = "current"


class FspR7RoadmNumber(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("rNo1", 1),
          ("rNo10", 10),
          ("rNo2", 2),
          ("rNo3", 3),
          ("rNo4", 4),
          ("rNo5", 5),
          ("rNo6", 6),
          ("rNo7", 7),
          ("rNo8", 8),
          ("rNo9", 9),
          ("undefined", 0))
    )



class FspR7RoadmNumberCaps(Bits, TextualConvention):
    status = "current"


class FspR7RowStatus(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3),
          ("undefined", 0))
    )



class FspR7RowStatusCaps(Bits, TextualConvention):
    status = "current"


class FspR7Scrambling(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("undefined", 0))
    )



class FspR7ScramblingCaps(Bits, TextualConvention):
    status = "current"


class FspR7ScuRing(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("undefined", 0))
    )



class FspR7SignalDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cientToNetwork", 2),
          ("networkToClient", 1),
          ("networkToUpgrade", 4),
          ("undefined", 0),
          ("upgradeToNetwork", 3))
    )



class FspR7SingleFiberLocation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locationA", 1),
          ("locationB", 2),
          ("undefined", 0))
    )



class FspR7SingleFiberLocationCaps(Bits, TextualConvention):
    status = "current"


class FspR7SnmpHexString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class FspR7SnmpLongString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )



class FspR7SshHostKeyEncryptAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsa", 2),
          ("rsa", 1),
          ("rsa1", 3),
          ("undefined", 0))
    )



class FspR7SshHostKeyLength(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("length2048", 1),
          ("length4096", 2),
          ("undefined", 0))
    )



class FspR7Stages(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("st1", 1),
          ("st2", 2),
          ("undefined", 0))
    )



class FspR7StartPmSnapshot(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apply", 2),
          ("none", 1),
          ("undefined", 0))
    )



class FspR7StateConnection(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("invalidConfig", 6),
          ("mismatchChannel", 4),
          ("mismatchConnection", 3),
          ("mismatchEquipment", 2),
          ("mismatchPhysical", 5),
          ("nonStandard", 7),
          ("standard", 1),
          ("standardSpeq", 8),
          ("undefined", 0))
    )



class FspR7Stuff(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("undefined", 0),
          ("yes", 1))
    )



class FspR7StuffCaps(Bits, TextualConvention):
    status = "current"


class FspR7SupplyType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("front", 1),
          ("rear", 2),
          ("undefined", 0))
    )



class FspR7SupplyTypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7SwitchOverCause(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("buttonPushed", 11),
          ("gracefulShutdown", 9),
          ("noResponse", 4),
          ("notApplicable", 1),
          ("removed", 2),
          ("softwareException", 3),
          ("switchToDuplex", 10),
          ("undefined", 0))
    )



class FspR7SwitchOverCauseCaps(Bits, TextualConvention):
    status = "current"


class FspR7TelemetryOutput(Integer32, TextualConvention):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("fcuAlmCr", 6),
          ("fcuAlmMj", 7),
          ("fcuAlmMjGe", 9),
          ("fcuAlmMn", 8),
          ("fcuAlmMnGe", 10),
          ("neAlmCr", 1),
          ("neAlmMj", 2),
          ("neAlmMjGe", 4),
          ("neAlmMn", 3),
          ("neAlmMnGe", 5),
          ("none", 16),
          ("psuAlmCr", 11),
          ("psuAlmMj", 12),
          ("psuAlmMjGe", 14),
          ("psuAlmMn", 13),
          ("psuAlmMnGe", 15),
          ("undefined", 0))
    )



class FspR7TelemetryOutputCaps(Bits, TextualConvention):
    status = "current"


class FspR7PRBSTest(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iPRBS31", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class FspR7PRBSTestCaps(Bits, TextualConvention):
    status = "current"


class FspR7TifOutputReset(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opr", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class FspR7TifOutputResetCaps(Bits, TextualConvention):
    status = "current"


class FspR7TiltSet(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("minus1dB0", 1),
          ("minus1dB5", 2),
          ("minus2dB0", 3),
          ("undefined", 0))
    )



class FspR7TiltSetCaps(Bits, TextualConvention):
    status = "current"


class FspR7Topology(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("backToBack", 2),
          ("fabric", 4),
          ("mesh", 3),
          ("standAlone", 1),
          ("undefined", 0))
    )



class FspR7TopologyCaps(Bits, TextualConvention):
    status = "current"


class FspR7TopologyType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lad", 1),
          ("p2p", 3),
          ("ring", 2),
          ("undefined", 0),
          ("unknown", 4))
    )



class FspR7TrafficDirection(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("bidi", 1),
          ("rxcrs", 7),
          ("txcrs", 6),
          ("undefined", 0),
          ("uniCton", 2),
          ("uniEtow", 5),
          ("uniNtoc", 3),
          ("uniWtoe", 4))
    )



class FspR7TrafficDirectionCaps(Bits, TextualConvention):
    status = "current"


class FspR7TrapModeLegacy(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2),
          ("undefined", 0))
    )



class FspR7TransmissionMode(Integer32, TextualConvention):
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
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("adm", 12),
          ("cSelect", 16),
          ("dualClient", 17),
          ("mux", 5),
          ("muxDual", 14),
          ("muxE", 6),
          ("muxHst", 8),
          ("muxW", 7),
          ("nFixed", 15),
          ("obsolete", 11),
          ("regen1Way", 9),
          ("regen2Way", 10),
          ("trans", 1),
          ("transDual", 13),
          ("transE", 2),
          ("transHst", 4),
          ("transQuad", 21),
          ("transQuintuple", 22),
          ("transW", 3),
          ("undefined", 0),
          ("xc", 20))
    )



class FspR7TransmissionModeCaps(Bits, TextualConvention):
    status = "current"


class FspR7TurnupConfig(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oprTurnup", 2),
          ("rls", 1),
          ("undefined", 0))
    )



class FspR7TurnupConfigCaps(Bits, TextualConvention):
    status = "current"


class FspR7TxOffOnTm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enableTxOffTm", 2),
          ("enableTxOnTm", 3),
          ("undefined", 0))
    )



class FspR7TxOffOnTmCaps(Bits, TextualConvention):
    status = "current"


class FspR7TypeConnection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connection1Way", 1),
          ("connection2Way", 2),
          ("undefined", 0))
    )



class FspR7TypeConnectionCaps(Bits, TextualConvention):
    status = "current"


class FspR7TypeCrs(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("connection1Way", 1),
          ("connection1WayCont", 9),
          ("connection1WayDc", 6),
          ("connection1WayDcProt", 7),
          ("connection1WayMc", 5),
          ("connection1WayMcProt", 8),
          ("connection1WayProt", 3),
          ("connection2Way", 2),
          ("connection2WayCont", 10),
          ("connection2WayProt", 4),
          ("undefined", 0))
    )



class FspR7TypeCrsCaps(Bits, TextualConvention):
    status = "current"


class FspR7Unsigned32Caps(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d:4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class FspR7UntaggedFrames(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2),
          ("undefined", 0))
    )



class FspR7UntaggedFramesCaps(Bits, TextualConvention):
    status = "current"


class FspR7ValidityPeriod(Integer32, TextualConvention):
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
        *(("fiveYears", 5),
          ("fourYears", 4),
          ("oneYear", 1),
          ("threeYears", 3),
          ("twoYears", 2),
          ("undefined", 0))
    )



class FspR7ValidityPeriodCaps(Bits, TextualConvention):
    status = "current"


class FspR7VoaMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("att", 2),
          ("power", 1),
          ("undefined", 0))
    )



class FspR7VoaModeCaps(Bits, TextualConvention):
    status = "current"


class FspR7VSessChangeReason(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("accessRevoked", 7),
          ("accessTimeout", 6),
          ("none", 1),
          ("requestApproved", 3),
          ("requestDenied", 4),
          ("requestIssued", 2),
          ("requestTimeout", 5),
          ("undefined", 0))
    )



class FspR7VSessStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("undefined", 0),
          ("writeAcsGranted", 3),
          ("writeAcsRequested", 2))
    )



class FspR7VSessWriteAccess(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("grant", 3),
          ("none", 4),
          ("request", 1),
          ("revoke", 2),
          ("undefined", 0))
    )



class FspR7XfpDecisionThres(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwardRaman", 2),
          ("standard", 1),
          ("undefined", 0))
    )



class FspR7XfpDecisionThresCaps(Bits, TextualConvention):
    status = "current"


class FspR7YcableType(Integer32, TextualConvention):
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
        *(("undefined", 0),
          ("ycabMmLc", 2),
          ("ycabMmScLc", 4),
          ("ycabSmFcLc", 5),
          ("ycabSmLc", 1),
          ("ycabSmScLc", 3))
    )



class FspR7YcableTypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7FltrCableType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fltrCabLr4SmLc", 1),
          ("undefined", 0))
    )



class FspR7FltrCableTypeCaps(Bits, TextualConvention):
    status = "current"


class FspR7YesNo(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("undefined", 0),
          ("yes", 1))
    )



class FspR7YesNoCaps(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADVA-FSPR7-TC-MIB",
    **{"ApsRevertMode": ApsRevertMode,
       "ApsRevertModeCaps": ApsRevertModeCaps,
       "ApsType": ApsType,
       "ApsTypeCaps": ApsTypeCaps,
       "ConnectionNotation": ConnectionNotation,
       "Counter64StringCaps": Counter64StringCaps,
       "EntityClassName": EntityClassName,
       "EntityType": EntityType,
       "EquipmentState": EquipmentState,
       "FfpType": FfpType,
       "FfpTypeCaps": FfpTypeCaps,
       "Grade": Grade,
       "FspR7AdminState": FspR7AdminState,
       "FspR7AdminStateCaps": FspR7AdminStateCaps,
       "FspR7AidType": FspR7AidType,
       "FspR7AlarmListType": FspR7AlarmListType,
       "FspR7AlarmProfileList": FspR7AlarmProfileList,
       "FspR7AlsMode": FspR7AlsMode,
       "FspR7AlsModeCaps": FspR7AlsModeCaps,
       "FspR7AppType": FspR7AppType,
       "FspR7ApsChannel": FspR7ApsChannel,
       "FspR7APSCommand": FspR7APSCommand,
       "FspR7APSCommandCaps": FspR7APSCommandCaps,
       "FspR7AseTabOpr": FspR7AseTabOpr,
       "FspR7AseTabOprCaps": FspR7AseTabOprCaps,
       "FspR7EquipmentAssignState": FspR7EquipmentAssignState,
       "FspR7AutoThresReset": FspR7AutoThresReset,
       "FspR7AutoThresResetCaps": FspR7AutoThresResetCaps,
       "FspR7Baund": FspR7Baund,
       "FspR7BaundCaps": FspR7BaundCaps,
       "FspR7BERThreshold": FspR7BERThreshold,
       "FspR7BERThresholdCaps": FspR7BERThresholdCaps,
       "FspR7BERThresholdSection": FspR7BERThresholdSection,
       "FspR7BERThresholdSectionCaps": FspR7BERThresholdSectionCaps,
       "FspR7BidirectionalChannel": FspR7BidirectionalChannel,
       "FspR7BidirectionalChannelCaps": FspR7BidirectionalChannelCaps,
       "FspR7Bitrate": FspR7Bitrate,
       "FspR7BitrateCaps": FspR7BitrateCaps,
       "FspR7CapInventory": FspR7CapInventory,
       "FspR7CapInventoryCaps": FspR7CapInventoryCaps,
       "FspR7Category": FspR7Category,
       "FspR7CertApply": FspR7CertApply,
       "FspR7CertApplyCaps": FspR7CertApplyCaps,
       "FspR7ChannelBandwidth": FspR7ChannelBandwidth,
       "FspR7ChannelBandwidthCaps": FspR7ChannelBandwidthCaps,
       "FspR7ChannelIdentifier": FspR7ChannelIdentifier,
       "FspR7ChannelIdentifierCaps": FspR7ChannelIdentifierCaps,
       "FspR7ChannelNumber": FspR7ChannelNumber,
       "FspR7ChannelNumberCaps": FspR7ChannelNumberCaps,
       "FspR7ChannelSpacing": FspR7ChannelSpacing,
       "FspR7ChannelSpacingCaps": FspR7ChannelSpacingCaps,
       "FspR7CodeGain": FspR7CodeGain,
       "FspR7CodeGainCaps": FspR7CodeGainCaps,
       "FspR7ColumnMark": FspR7ColumnMark,
       "FspR7Conn": FspR7Conn,
       "FspR7ConnCaps": FspR7ConnCaps,
       "FspR7ConnectorType": FspR7ConnectorType,
       "FspR7ConnectorTypeCaps": FspR7ConnectorTypeCaps,
       "FspR7ConnectState": FspR7ConnectState,
       "FspR7CpAuthType": FspR7CpAuthType,
       "FspR7CpAuthTypeCaps": FspR7CpAuthTypeCaps,
       "FspR7DCFiberType": FspR7DCFiberType,
       "FspR7DCFiberTypeCaps": FspR7DCFiberTypeCaps,
       "FspR7DeploymentScenario": FspR7DeploymentScenario,
       "FspR7DeploymentScenarioCaps": FspR7DeploymentScenarioCaps,
       "FspR7DisableEnable": FspR7DisableEnable,
       "FspR7DisableEnableCaps": FspR7DisableEnableCaps,
       "FspR7DispersionCompensation": FspR7DispersionCompensation,
       "FspR7DispersionCompensationCaps": FspR7DispersionCompensationCaps,
       "FspR7DispersionConfig": FspR7DispersionConfig,
       "FspR7DispersionConfigCaps": FspR7DispersionConfigCaps,
       "FspR7DispersionModes": FspR7DispersionModes,
       "FspR7DispersionModesCaps": FspR7DispersionModesCaps,
       "FspR7EocProtAvailability": FspR7EocProtAvailability,
       "FspR7EdfaOutputPowerRating": FspR7EdfaOutputPowerRating,
       "FspR7EdfaOutputPowerRatingCaps": FspR7EdfaOutputPowerRatingCaps,
       "FspR7EnableDisable": FspR7EnableDisable,
       "FspR7EnableDisableCaps": FspR7EnableDisableCaps,
       "FspR7EncapsulationMethod": FspR7EncapsulationMethod,
       "FspR7EntitySecondaryStates": FspR7EntitySecondaryStates,
       "FspR7EntityType": FspR7EntityType,
       "FspR7EqlzAdminState": FspR7EqlzAdminState,
       "FspR7EqlzAdminStateCaps": FspR7EqlzAdminStateCaps,
       "FspR7ErrorFwdMode": FspR7ErrorFwdMode,
       "FspR7ErrorFwdModeCaps": FspR7ErrorFwdModeCaps,
       "FspR7FanMode": FspR7FanMode,
       "FspR7FanProfile": FspR7FanProfile,
       "FspR7FDStatus": FspR7FDStatus,
       "FspR7FDStatusCaps": FspR7FDStatusCaps,
       "FspR7FecType": FspR7FecType,
       "FspR7FecTypeCaps": FspR7FecTypeCaps,
       "FspR7FiberBrand": FspR7FiberBrand,
       "FspR7FiberBrandCaps": FspR7FiberBrandCaps,
       "FspR7FiberDetect": FspR7FiberDetect,
       "FspR7FiberDetectCaps": FspR7FiberDetectCaps,
       "FspR7FlowControlMode": FspR7FlowControlMode,
       "FspR7FlowControlModeCaps": FspR7FlowControlModeCaps,
       "FspR7ForceConfig": FspR7ForceConfig,
       "FspR7ForceConfigCaps": FspR7ForceConfigCaps,
       "FspR7ForcedStatus": FspR7ForcedStatus,
       "FspR7ForcedStatusCaps": FspR7ForcedStatusCaps,
       "FspR7FrameFormat": FspR7FrameFormat,
       "FspR7FrameFormatCaps": FspR7FrameFormatCaps,
       "FspR7FunctionCrs": FspR7FunctionCrs,
       "FspR7FunctionCrsCaps": FspR7FunctionCrsCaps,
       "FspR7Gain": FspR7Gain,
       "FspR7GainCaps": FspR7GainCaps,
       "FspR7GainRange": FspR7GainRange,
       "FspR7GainRangeCaps": FspR7GainRangeCaps,
       "FspR7GropticsType": FspR7GropticsType,
       "FspR7GropticsTypeCaps": FspR7GropticsTypeCaps,
       "FspR7InitEqualization": FspR7InitEqualization,
       "FspR7InitEqualizationCaps": FspR7InitEqualizationCaps,
       "FspR7Integer32Caps": FspR7Integer32Caps,
       "FspR7InterfaceFunction": FspR7InterfaceFunction,
       "FspR7InterfaceType": FspR7InterfaceType,
       "FspR7InterfaceTypeCaps": FspR7InterfaceTypeCaps,
       "FspR7InvertTelemetryInputLogic": FspR7InvertTelemetryInputLogic,
       "FspR7InvertTelemetryInputLogicCaps": FspR7InvertTelemetryInputLogicCaps,
       "FspR7IpType": FspR7IpType,
       "FspR7IpTypeCaps": FspR7IpTypeCaps,
       "FspR7IpMode": FspR7IpMode,
       "FspR7IpModeCaps": FspR7IpModeCaps,
       "FspR7Ipv6Address": FspR7Ipv6Address,
       "FspR7IPv6Type": FspR7IPv6Type,
       "FspR7IPv6TypeCaps": FspR7IPv6TypeCaps,
       "FspR7KeyLength": FspR7KeyLength,
       "FspR7KeyLengthCaps": FspR7KeyLengthCaps,
       "FspR7LacpMode": FspR7LacpMode,
       "FspR7LacpModeCaps": FspR7LacpModeCaps,
       "FspR7LacpTimeout": FspR7LacpTimeout,
       "FspR7LacpTimeoutCaps": FspR7LacpTimeoutCaps,
       "FspR7LaneGroupInventory": FspR7LaneGroupInventory,
       "FspR7LaneGroupInventoryCaps": FspR7LaneGroupInventoryCaps,
       "FspR7LagFendState": FspR7LagFendState,
       "FspR7LagIdFend": FspR7LagIdFend,
       "FspR7LagPorts": FspR7LagPorts,
       "FspR7LagPortType": FspR7LagPortType,
       "FspR7LagPortTypeCaps": FspR7LagPortTypeCaps,
       "FspR7LagStandby": FspR7LagStandby,
       "FspR7LagState": FspR7LagState,
       "FspR7LagSysIdFend": FspR7LagSysIdFend,
       "FspR7LaserDelayTimer": FspR7LaserDelayTimer,
       "FspR7LaserDelayTimerCaps": FspR7LaserDelayTimerCaps,
       "FspR7LaserForcedOperation": FspR7LaserForcedOperation,
       "FspR7LaserForcedOperationCaps": FspR7LaserForcedOperationCaps,
       "FspR7LineCoding": FspR7LineCoding,
       "FspR7LineCodingCaps": FspR7LineCodingCaps,
       "FspR7LossAttenuation": FspR7LossAttenuation,
       "FspR7LossAttenuationCaps": FspR7LossAttenuationCaps,
       "FspR7NoYes": FspR7NoYes,
       "FspR7NoYesCaps": FspR7NoYesCaps,
       "FspR7ManualAuto": FspR7ManualAuto,
       "FspR7ManualAutoCaps": FspR7ManualAutoCaps,
       "FspR7MaxBitErrorRate": FspR7MaxBitErrorRate,
       "FspR7MaxBitErrorRateCaps": FspR7MaxBitErrorRateCaps,
       "FspR7Mapping": FspR7Mapping,
       "FspR7MappingCaps": FspR7MappingCaps,
       "FspR7MonLevel": FspR7MonLevel,
       "FspR7MuxMethod": FspR7MuxMethod,
       "FspR7MuxMethodCaps": FspR7MuxMethodCaps,
       "FspR7NCTraceId": FspR7NCTraceId,
       "FspR7NCTRouteType": FspR7NCTRouteType,
       "FspR7NdpCleanup": FspR7NdpCleanup,
       "FspR7NdpCleanupCaps": FspR7NdpCleanupCaps,
       "FspR7NewSshHostKey": FspR7NewSshHostKey,
       "FspR7NtpAdminState": FspR7NtpAdminState,
       "FspR7NtpSyncStatus": FspR7NtpSyncStatus,
       "FspR7NtpTest": FspR7NtpTest,
       "FspR7NtpTestStatus": FspR7NtpTestStatus,
       "FspR7NumberOfChannels": FspR7NumberOfChannels,
       "FspR7NumberOfChannelsCaps": FspR7NumberOfChannelsCaps,
       "FspR7NumberOfChannelsProv": FspR7NumberOfChannelsProv,
       "FspR7NumberOfChannelsProvCaps": FspR7NumberOfChannelsProvCaps,
       "FspR7OdtuType": FspR7OdtuType,
       "FspR7OperState": FspR7OperState,
       "FspR7OpticalBand": FspR7OpticalBand,
       "FspR7OpticalBandCaps": FspR7OpticalBandCaps,
       "FspR7OpticalFiberType": FspR7OpticalFiberType,
       "FspR7OpticalFiberTypeCaps": FspR7OpticalFiberTypeCaps,
       "FspR7OpticalGroup": FspR7OpticalGroup,
       "FspR7OpticalGroupCaps": FspR7OpticalGroupCaps,
       "FspR7OpticalInterfaceReach": FspR7OpticalInterfaceReach,
       "FspR7OpticalInterfaceReachCaps": FspR7OpticalInterfaceReachCaps,
       "FspR7OpticalLanes": FspR7OpticalLanes,
       "FspR7OpticalMultiplexLevel": FspR7OpticalMultiplexLevel,
       "FspR7OpticalSubBand": FspR7OpticalSubBand,
       "FspR7OpticalSubBandCaps": FspR7OpticalSubBandCaps,
       "FspR7OpuPayloadType": FspR7OpuPayloadType,
       "FspR7OpuPayloadTypeCaps": FspR7OpuPayloadTypeCaps,
       "FspR7OptUpdate": FspR7OptUpdate,
       "FspR7OptUpdateCaps": FspR7OptUpdateCaps,
       "FspR7OscChannel": FspR7OscChannel,
       "FspR7OscChannelCaps": FspR7OscChannelCaps,
       "FspR7OscUsage": FspR7OscUsage,
       "FspR7OscUsageCaps": FspR7OscUsageCaps,
       "FspR7OspfMode": FspR7OspfMode,
       "FspR7OspfModeCaps": FspR7OspfModeCaps,
       "FspR7OtdrPeriod": FspR7OtdrPeriod,
       "FspR7OtdrPeriodCaps": FspR7OtdrPeriodCaps,
       "FspR7ParityBit": FspR7ParityBit,
       "FspR7ParityBitCaps": FspR7ParityBitCaps,
       "FspR7PathNode": FspR7PathNode,
       "FspR7PathNodeCaps": FspR7PathNodeCaps,
       "FspR7PathProt": FspR7PathProt,
       "FspR7PlugDataRate": FspR7PlugDataRate,
       "FspR7PlugDataRateCaps": FspR7PlugDataRateCaps,
       "FspR7PmReset": FspR7PmReset,
       "FspR7PmResetCaps": FspR7PmResetCaps,
       "FspR7PmSnapshotStatus": FspR7PmSnapshotStatus,
       "FspR7PmSnapshotParameterTypes": FspR7PmSnapshotParameterTypes,
       "FspR7PortBehaviour": FspR7PortBehaviour,
       "FspR7PortBehaviourCaps": FspR7PortBehaviourCaps,
       "FspR7PortMode": FspR7PortMode,
       "FspR7PortModeCaps": FspR7PortModeCaps,
       "FspR7PortRole": FspR7PortRole,
       "FspR7PortRoleCaps": FspR7PortRoleCaps,
       "FspR7PrbsPmReset": FspR7PrbsPmReset,
       "FspR7PrbsPmResetCaps": FspR7PrbsPmResetCaps,
       "FspR7ProtectionRole": FspR7ProtectionRole,
       "FspR7ProtectionType": FspR7ProtectionType,
       "FspR7ProtectionTypeCaps": FspR7ProtectionTypeCaps,
       "FspR7Protocol": FspR7Protocol,
       "FspR7PsuOutputPower": FspR7PsuOutputPower,
       "FspR7PsuOutputPowerCaps": FspR7PsuOutputPowerCaps,
       "FspR7RedLinedState": FspR7RedLinedState,
       "FspR7RedLinedStateCaps": FspR7RedLinedStateCaps,
       "FspR7RenewMode": FspR7RenewMode,
       "FspR7RenewModeCaps": FspR7RenewModeCaps,
       "FspR7RlsMan": FspR7RlsMan,
       "FspR7RlsManCaps": FspR7RlsManCaps,
       "FspR7RoadmNumber": FspR7RoadmNumber,
       "FspR7RoadmNumberCaps": FspR7RoadmNumberCaps,
       "FspR7RowStatus": FspR7RowStatus,
       "FspR7RowStatusCaps": FspR7RowStatusCaps,
       "FspR7Scrambling": FspR7Scrambling,
       "FspR7ScramblingCaps": FspR7ScramblingCaps,
       "FspR7ScuRing": FspR7ScuRing,
       "FspR7SignalDirection": FspR7SignalDirection,
       "FspR7SingleFiberLocation": FspR7SingleFiberLocation,
       "FspR7SingleFiberLocationCaps": FspR7SingleFiberLocationCaps,
       "FspR7SnmpHexString": FspR7SnmpHexString,
       "FspR7SnmpLongString": FspR7SnmpLongString,
       "FspR7SshHostKeyEncryptAlgorithm": FspR7SshHostKeyEncryptAlgorithm,
       "FspR7SshHostKeyLength": FspR7SshHostKeyLength,
       "FspR7Stages": FspR7Stages,
       "FspR7StartPmSnapshot": FspR7StartPmSnapshot,
       "FspR7StateConnection": FspR7StateConnection,
       "FspR7Stuff": FspR7Stuff,
       "FspR7StuffCaps": FspR7StuffCaps,
       "FspR7SupplyType": FspR7SupplyType,
       "FspR7SupplyTypeCaps": FspR7SupplyTypeCaps,
       "FspR7SwitchOverCause": FspR7SwitchOverCause,
       "FspR7SwitchOverCauseCaps": FspR7SwitchOverCauseCaps,
       "FspR7TelemetryOutput": FspR7TelemetryOutput,
       "FspR7TelemetryOutputCaps": FspR7TelemetryOutputCaps,
       "FspR7PRBSTest": FspR7PRBSTest,
       "FspR7PRBSTestCaps": FspR7PRBSTestCaps,
       "FspR7TifOutputReset": FspR7TifOutputReset,
       "FspR7TifOutputResetCaps": FspR7TifOutputResetCaps,
       "FspR7TiltSet": FspR7TiltSet,
       "FspR7TiltSetCaps": FspR7TiltSetCaps,
       "FspR7Topology": FspR7Topology,
       "FspR7TopologyCaps": FspR7TopologyCaps,
       "FspR7TopologyType": FspR7TopologyType,
       "FspR7TrafficDirection": FspR7TrafficDirection,
       "FspR7TrafficDirectionCaps": FspR7TrafficDirectionCaps,
       "FspR7TrapModeLegacy": FspR7TrapModeLegacy,
       "FspR7TransmissionMode": FspR7TransmissionMode,
       "FspR7TransmissionModeCaps": FspR7TransmissionModeCaps,
       "FspR7TurnupConfig": FspR7TurnupConfig,
       "FspR7TurnupConfigCaps": FspR7TurnupConfigCaps,
       "FspR7TxOffOnTm": FspR7TxOffOnTm,
       "FspR7TxOffOnTmCaps": FspR7TxOffOnTmCaps,
       "FspR7TypeConnection": FspR7TypeConnection,
       "FspR7TypeConnectionCaps": FspR7TypeConnectionCaps,
       "FspR7TypeCrs": FspR7TypeCrs,
       "FspR7TypeCrsCaps": FspR7TypeCrsCaps,
       "FspR7Unsigned32Caps": FspR7Unsigned32Caps,
       "FspR7UntaggedFrames": FspR7UntaggedFrames,
       "FspR7UntaggedFramesCaps": FspR7UntaggedFramesCaps,
       "FspR7ValidityPeriod": FspR7ValidityPeriod,
       "FspR7ValidityPeriodCaps": FspR7ValidityPeriodCaps,
       "FspR7VoaMode": FspR7VoaMode,
       "FspR7VoaModeCaps": FspR7VoaModeCaps,
       "FspR7VSessChangeReason": FspR7VSessChangeReason,
       "FspR7VSessStatus": FspR7VSessStatus,
       "FspR7VSessWriteAccess": FspR7VSessWriteAccess,
       "FspR7XfpDecisionThres": FspR7XfpDecisionThres,
       "FspR7XfpDecisionThresCaps": FspR7XfpDecisionThresCaps,
       "FspR7YcableType": FspR7YcableType,
       "FspR7YcableTypeCaps": FspR7YcableTypeCaps,
       "FspR7FltrCableType": FspR7FltrCableType,
       "FspR7FltrCableTypeCaps": FspR7FltrCableTypeCaps,
       "FspR7YesNo": FspR7YesNo,
       "FspR7YesNoCaps": FspR7YesNoCaps,
       "advaFspR7Tc": advaFspR7Tc}
)
