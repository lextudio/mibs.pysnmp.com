# SNMP MIB module (CYAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:03 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

cyanAlarmMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20)
)
cyanAlarmMibModule.setRevisions(
        ("2014-12-07 06:01",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CyanProbablecauseTc(Integer32, TextualConvention):
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
              11,
              31,
              32,
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
              201,
              202,
              203,
              204,
              205,
              301,
              302,
              401,
              402)
        )
    )
    namedValues = NamedValues(
        *(("admin", 402),
          ("aps", 89),
          ("arp", 107),
          ("autoUpgrade", 11),
          ("batDgrade", 32),
          ("batFail", 31),
          ("ccm", 79),
          ("commDgrade", 102),
          ("commFail", 101),
          ("csf", 92),
          ("dmm", 100),
          ("envAlm", 301),
          ("envWrn", 302),
          ("eqptDgrade", 4),
          ("eqptFail", 3),
          ("eqptMismtch", 5),
          ("eqptRestart", 2),
          ("eqptUnexpected", 6),
          ("eqptWarning", 7),
          ("erpPort", 109),
          ("exmism", 93),
          ("farendCmd", 96),
          ("gtp", 84),
          ("holdover", 203),
          ("incmpld", 401),
          ("lmm", 99),
          ("loopback", 98),
          ("ltm", 88),
          ("na", 0),
          ("notConfig", 8),
          ("packetLpbk", 103),
          ("preAmp", 50),
          ("protCmd", 95),
          ("protFail", 78),
          ("protocolErr", 97),
          ("srcaddrmis", 106),
          ("syncDgrade", 202),
          ("syncExcmdActive", 205),
          ("syncFail", 201),
          ("tpAis", 54),
          ("tpBdi", 57),
          ("tpBiae", 64),
          ("tpFaclpbk", 71),
          ("tpFdi", 58),
          ("tpFiber", 74),
          ("tpGfp", 82),
          ("tpHighLoss", 72),
          ("tpIae", 63),
          ("tpLck", 66),
          ("tpLfd", 80),
          ("tpLink", 81),
          ("tpLoa", 86),
          ("tpLoc", 52),
          ("tpLof", 53),
          ("tpLoflom", 67),
          ("tpLol", 49),
          ("tpLom", 55),
          ("tpLoomfi", 110),
          ("tpLop", 90),
          ("tpLos", 51),
          ("tpLowLoss", 73),
          ("tpLtc", 76),
          ("tpLti", 87),
          ("tpMsim", 77),
          ("tpOci", 65),
          ("tpOorangeAlm", 69),
          ("tpOorangeWrn", 70),
          ("tpPlm", 75),
          ("tpPmi", 59),
          ("tpRdi", 61),
          ("tpSd", 60),
          ("tpSf", 56),
          ("tpSqm", 85),
          ("tpSsf", 68),
          ("tpTim", 62),
          ("tpTpt", 83),
          ("tpUneq", 91),
          ("tsa", 108),
          ("unequipped", 1),
          ("upm", 94),
          ("xcsholdover", 204),
          ("xcspktserr", 105),
          ("xcspktsloss", 104))
    )



class CyanAlarmstateTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("asCleared", 0),
          ("asSet", 1))
    )



class CyanTypeTc(Integer32, TextualConvention):
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
              96,
              97,
              98,
              99,
              100,
              101,
              106,
              107,
              108,
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
              126,
              127,
              128,
              129,
              130,
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
              143,
              144,
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
              204,
              207,
              299,
              300,
              301,
              303,
              304,
              305,
              306,
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
              374,
              375,
              376,
              377,
              378,
              379,
              380,
              381,
              382,
              383,
              384,
              385,
              386,
              387,
              388,
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
              556,
              557,
              558,
              559,
              560,
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
              575,
              576,
              577,
              578,
              580,
              601,
              602,
              603,
              604,
              605,
              702,
              703,
              704,
              705,
              706,
              707,
              708,
              709,
              710,
              711,
              712,
              713,
              714,
              715,
              716,
              717,
              718,
              719,
              720,
              721,
              722,
              723,
              724,
              725,
              726,
              727,
              728,
              729,
              730,
              731,
              732,
              733,
              734,
              735,
              736,
              737,
              738,
              800,
              801,
              802)
        )
    )
    namedValues = NamedValues(
        *(("asapT", 703),
          ("cimDcnipTtp", 509),
          ("cimDcnospfTtp", 510),
          ("cimIpinterface", 503),
          ("cimIpprotocolendpoint", 502),
          ("cimOspfarea", 506),
          ("cimOspfinterface", 505),
          ("cimOspfprotocolendpoint", 504),
          ("cimOspfservice", 501),
          ("cyan100gemfiberptp", 514),
          ("cyan10gafiberptp", 333),
          ("cyan10gaofiberptp", 462),
          ("cyan10gefiberptp", 356),
          ("cyan10gemfiberptp", 350),
          ("cyan10geofiberptp", 429),
          ("cyan10geopfiberptp", 474),
          ("cyan10gepfiberptp", 526),
          ("cyan10gfiberptp", 355),
          ("cyan10ggfiberptp", 547),
          ("cyan3r10gmrfiberptp", 472),
          ("cyan3rfiberptp", 332),
          ("cyanAdddropcwdmfiberptp", 330),
          ("cyanAdddropfiberptp", 337),
          ("cyanAdddropwwdmfiberptp", 452),
          ("cyanAfecotu2ttp", 512),
          ("cyanAmc", 207),
          ("cyanAmcslot", 13),
          ("cyanAug16Ttp", 318),
          ("cyanAug1Ttp", 316),
          ("cyanAug4Ttp", 317),
          ("cyanAug64Ttp", 319),
          ("cyanAugnprofile", 716),
          ("cyanAwg40", 26),
          ("cyanAwg40shelf", 27),
          ("cyanAwg96", 41),
          ("cyanAwg96shelf", 40),
          ("cyanBoss", 101),
          ("cyanBoss2", 146),
          ("cyanBossslot", 31),
          ("cyanBtm", 301),
          ("cyanBtmslot", 22),
          ("cyanBurstydegthresholdprofile", 711),
          ("cyanCem", 108),
          ("cyanCemi", 137),
          ("cyanCemslot", 30),
          ("cyanCfpnetworklanePtp", 577),
          ("cyanCfpslot", 38),
          ("cyanCfpxcvr", 202),
          ("cyanClientftp", 379),
          ("cyanCrossconnect", 601),
          ("cyanDcnptp", 408),
          ("cyanDerivedtimingreference", 357),
          ("cyanDscp2cospidprofile", 726),
          ("cyanDtm100g", 151),
          ("cyanDtm100g2", 156),
          ("cyanDtm4", 147),
          ("cyanDtm8", 128),
          ("cyanDtm8g", 126),
          ("cyanEdprofile", 735),
          ("cyanElectricalErpflowpoint", 537),
          ("cyanElectricalFlowpoint", 530),
          ("cyanElectricalFlowpointpool", 529),
          ("cyanElectricalLagflowpoint", 538),
          ("cyanElectricalOfflowpoint", 564),
          ("cyanElectricalPbbflowpoint", 536),
          ("cyanElectricalUniflowpoint", 539),
          ("cyanElectricalctp", 351),
          ("cyanElectricalgtp", 528),
          ("cyanEoamApi", 432),
          ("cyanEosApi", 423),
          ("cyanEqptClockTtp", 310),
          ("cyanEqptprofile", 737),
          ("cyanErp", 486),
          ("cyanErpProfile", 498),
          ("cyanErppGtp", 467),
          ("cyanErpv2Profile", 476),
          ("cyanEthbridge", 434),
          ("cyanEthbwprofile", 441),
          ("cyanEthcosprofile", 442),
          ("cyanEthernetttp", 406),
          ("cyanEthernetttpwpmstats", 460),
          ("cyanEthflowdomain", 433),
          ("cyanEthflowdomainfrmnt", 531),
          ("cyanEthflowdomainintfrmnt", 533),
          ("cyanEthflowpoint", 421),
          ("cyanEthflowpointpool", 411),
          ("cyanEthkbwprofile", 448),
          ("cyanEthlagflowpoint", 426),
          ("cyanEthlagfpp", 415),
          ("cyanEthlinkoamprofile", 446),
          ("cyanEthnni", 413),
          ("cyanEthoamprofile", 479),
          ("cyanEthpcp2cospidprofile", 714),
          ("cyanEthqueueprofile", 443),
          ("cyanEthscheduleprofile", 500),
          ("cyanEthuni", 412),
          ("cyanEtty100gTtp", 565),
          ("cyanEtty10gTtp", 418),
          ("cyanEttyTtp", 402),
          ("cyanEty31Ptp", 403),
          ("cyanEty32Ptp", 404),
          ("cyanEty32bPtp", 458),
          ("cyanEtyFpgaTtp", 527),
          ("cyanEtyLbTtp", 525),
          ("cyanEtyTtp", 407),
          ("cyanExtcc2mhzptp", 347),
          ("cyanExtcc2mhzrxttp", 346),
          ("cyanExttimingptp", 362),
          ("cyanExttimingreference", 360),
          ("cyanExttimingrxttp", 364),
          ("cyanExttimingtxttp", 363),
          ("cyanFan", 106),
          ("cyanFanslot", 33),
          ("cyanFc100FiconTtp", 542),
          ("cyanFc1200Ttp", 546),
          ("cyanFc200FiconxTtp", 543),
          ("cyanFc400Ttp", 544),
          ("cyanFc800Ttp", 545),
          ("cyanFiberotu2ttp", 385),
          ("cyanFiberptp", 353),
          ("cyanFiberttp", 354),
          ("cyanFimslot", 32),
          ("cyanFlx216", 150),
          ("cyanFtp", 438),
          ("cyanGfecotu2ttp", 416),
          ("cyanGfecotu4ttp", 517),
          ("cyanGfpTtp", 401),
          ("cyanGigeptp", 405),
          ("cyanGigeptpnopmstats", 459),
          ("cyanGigeptpnopmstatsroute", 461),
          ("cyanIngressoffp", 532),
          ("cyanInternalOdu2ttp", 570),
          ("cyanInternalOtu2ttp", 571),
          ("cyanInternalclockgen", 717),
          ("cyanLac8", 130),
          ("cyanLad2g", 96),
          ("cyanLad2gLgx", 127),
          ("cyanLad2p", 99),
          ("cyanLad2pLgx", 117),
          ("cyanLad4", 112),
          ("cyanLad40", 139),
          ("cyanLad40e", 140),
          ("cyanLad40eotmPtp", 471),
          ("cyanLad4a", 113),
          ("cyanLad8", 122),
          ("cyanLad8a", 123),
          ("cyanLad8e", 124),
          ("cyanLad8i", 138),
          ("cyanLad8x", 148),
          ("cyanLad8xotmPtp", 473),
          ("cyanLad96", 157),
          ("cyanLadaomsTtp", 335),
          ("cyanLadaotmPtp", 396),
          ("cyanLadeomsTtp", 420),
          ("cyanLadeotmPtp", 344),
          ("cyanLadeotsTtp", 419),
          ("cyanLadocgptp", 456),
          ("cyanLadomsTtp", 336),
          ("cyanLadoscTtp", 334),
          ("cyanLadotmPtp", 395),
          ("cyanLadotsTtp", 397),
          ("cyanLag", 393),
          ("cyanLagp", 709),
          ("cyanLamp", 16),
          ("cyanLampbtm", 300),
          ("cyanLampcoreeqpt", 14),
          ("cyanLampotmPtp", 394),
          ("cyanLampshelf", 15),
          ("cyanLedpanel", 131),
          ("cyanLgx3shelf", 19),
          ("cyanLinetimingttp", 331),
          ("cyanLinkftp", 349),
          ("cyanLme10g10", 141),
          ("cyanLme4", 121),
          ("cyanLogicalinterface", 550),
          ("cyanMaclimitprofile", 734),
          ("cyanMauTtp", 399),
          ("cyanMautTtp", 400),
          ("cyanMidstageptp", 309),
          ("cyanMinifan", 111),
          ("cyanMiniroot", 702),
          ("cyanMplsexp2cospidprofile", 568),
          ("cyanMplstpInterface", 552),
          ("cyanMplstpLabelrange", 562),
          ("cyanMplstpLsp", 554),
          ("cyanMplstpLspFrgmnt", 574),
          ("cyanMplstpMa", 559),
          ("cyanMplstpMd", 558),
          ("cyanMplstpMep", 560),
          ("cyanMplstpMepFrgmnt", 575),
          ("cyanMplstpMip", 561),
          ("cyanMplstpNode", 551),
          ("cyanMplstpOamApi", 563),
          ("cyanMplstpTunnel", 553),
          ("cyanMrflxptp", 513),
          ("cyanMs", 3),
          ("cyanMsaotu4ttp", 576),
          ("cyanMse1482", 114),
          ("cyanMsprPg", 484),
          ("cyanMsw10g12", 155),
          ("cyanMultifiber7tp", 567),
          ("cyanMultifibertp", 453),
          ("cyanMuxadddropfiberptp", 325),
          ("cyanNetty10gTtp", 475),
          ("cyanNetwork", 4),
          ("cyanNetworklaneTtp", 578),
          ("cyanOc192Ttp", 367),
          ("cyanOc48Ttp", 365),
          ("cyanOccctp", 414),
          ("cyanOccnimctp", 387),
          ("cyanOccrctp", 520),
          ("cyanOccttp", 388),
          ("cyanOcgettp", 454),
          ("cyanOcgptp", 326),
          ("cyanOcgttp", 386),
          ("cyanOcgwssfptp", 534),
          ("cyanOcgwssptp", 524),
          ("cyanOchtcaparameterprofile", 732),
          ("cyanOchttp", 389),
          ("cyanOdu0ttp", 463),
          ("cyanOdu1ctp", 375),
          ("cyanOdu1muxttp", 466),
          ("cyanOdu1nim", 373),
          ("cyanOdu1tcmTtp", 377),
          ("cyanOdu1ttp", 380),
          ("cyanOdu2ctp", 376),
          ("cyanOdu2ettp", 427),
          ("cyanOdu2muxttp", 465),
          ("cyanOdu2nim", 374),
          ("cyanOdu2tcmTtp", 378),
          ("cyanOdu2ttp", 381),
          ("cyanOdu4ttp", 518),
          ("cyanOduflexttp", 464),
          ("cyanOdukCtp", 540),
          ("cyanOfx4", 20),
          ("cyanOfx8", 42),
          ("cyanOla010", 166),
          ("cyanOla200", 163),
          ("cyanOla201", 164),
          ("cyanOla220", 165),
          ("cyanOla221", 167),
          ("cyanOlaocmotmPtp", 573),
          ("cyanOlaotmPtp", 572),
          ("cyanOmsTtp", 391),
          ("cyanOperationpanel", 107),
          ("cyanOppanelslot", 34),
          ("cyanOpticalfabricslot", 24),
          ("cyanOpticalpg", 483),
          ("cyanOpticaltcaparameterprofile", 706),
          ("cyanOscttp", 390),
          ("cyanOspflsdb", 507),
          ("cyanOspfneighbor", 508),
          ("cyanOtm04Ptp", 519),
          ("cyanOtmPtp", 352),
          ("cyanOtsTtp", 392),
          ("cyanOtu1ttp", 383),
          ("cyanOtu2ettp", 424),
          ("cyanOtu2fiberptp", 343),
          ("cyanOtu2ttp", 384),
          ("cyanOtu4fiberptp", 548),
          ("cyanOtu4ttp", 516),
          ("cyanOtukctp", 382),
          ("cyanPacketfabricslot", 25),
          ("cyanPathpg", 478),
          ("cyanPcapfile", 604),
          ("cyanPcp2colorprofile", 736),
          ("cyanPem", 304),
          ("cyanPem2", 299),
          ("cyanPemslot", 21),
          ("cyanPflinkttp", 348),
          ("cyanPg", 482),
          ("cyanPme216", 135),
          ("cyanPme412", 118),
          ("cyanPsw10", 152),
          ("cyanPsw100g", 154),
          ("cyanPsw10g20", 159),
          ("cyanPsw20", 116),
          ("cyanPsw618", 153),
          ("cyanPsx280", 115),
          ("cyanPwFlowdomain", 557),
          ("cyanPwFlowpoint", 555),
          ("cyanPwFlowpointpool", 556),
          ("cyanPxc280", 303),
          ("cyanR1g8sfp", 305),
          ("cyanRcm", 308),
          ("cyanRodu2ttp", 549),
          ("cyanRole", 801),
          ("cyanRtm2x", 306),
          ("cyanRtmslot", 23),
          ("cyanRxsdTtp", 329),
          ("cyanS0Ctp", 487),
          ("cyanS0Ttp", 491),
          ("cyanS16Ctp", 490),
          ("cyanS16Ttp", 494),
          ("cyanS16fiberptp", 340),
          ("cyanS16mrfiberptp", 341),
          ("cyanS1Ctp", 488),
          ("cyanS1Ttp", 492),
          ("cyanS1fiberptp", 338),
          ("cyanS4Ctp", 489),
          ("cyanS4Ttp", 493),
          ("cyanS4fiberptp", 339),
          ("cyanS64Ttp", 495),
          ("cyanS64fiberptp", 342),
          ("cyanSaug1Ttp", 315),
          ("cyanSaug4Ttp", 320),
          ("cyanSbconEsconTtp", 541),
          ("cyanSdhlinkftp", 345),
          ("cyanSdhsonetApi", 450),
          ("cyanSection155mTtp", 521),
          ("cyanSection2488mTtp", 523),
          ("cyanSection622mTtp", 522),
          ("cyanSethTtp", 455),
          ("cyanSethTxttp", 470),
          ("cyanSfecotu2ttp", 535),
          ("cyanSfppdslot", 39),
          ("cyanSfppslot", 37),
          ("cyanSfpslot", 12),
          ("cyanSfpxcvr", 204),
          ("cyanSft10g16", 149),
          ("cyanSft8", 129),
          ("cyanShelf16", 9),
          ("cyanShelf16slot", 8),
          ("cyanShelf16v2", 28),
          ("cyanShelf4", 29),
          ("cyanShelf8", 10),
          ("cyanShelfprofile", 713),
          ("cyanShelfslot", 17),
          ("cyanSmx28", 119),
          ("cyanSmx416", 120),
          ("cyanSonetsdhmsprofile", 712),
          ("cyanSonetsdhvcprofile", 715),
          ("cyanSshkeys", 802),
          ("cyanSta", 603),
          ("cyanStationclockgen", 718),
          ("cyanStm16Ttp", 366),
          ("cyanStm16msTtp", 313),
          ("cyanStm16rsTtp", 323),
          ("cyanStm1msTtp", 311),
          ("cyanStm1rsTtp", 321),
          ("cyanStm4msTtp", 312),
          ("cyanStm4rsTtp", 322),
          ("cyanStm64Ttp", 368),
          ("cyanStm64msTtp", 314),
          ("cyanStm64rsTtp", 324),
          ("cyanSubnetworkconnection", 602),
          ("cyanSvcApi", 605),
          ("cyanTesiexpressApi", 485),
          ("cyanTety100gTtp", 515),
          ("cyanTety10gTtp", 417),
          ("cyanTetyTtp", 398),
          ("cyanTimingreference", 361),
          ("cyanTimingrefftp", 358),
          ("cyanTimingrefprofile", 496),
          ("cyanTimingrefprofileline", 497),
          ("cyanTopologicalline", 5),
          ("cyanTopologicallink", 6),
          ("cyanTss", 359),
          ("cyanTsw10", 144),
          ("cyanTxextsdTtp", 327),
          ("cyanTxsdTtp", 328),
          ("cyanUfecotu2ttp", 428),
          ("cyanUser", 800),
          ("cyanUserburstydegthresholdprofile", 722),
          ("cyanUserdscp2cospidprofile", 727),
          ("cyanUsereqptprofile", 738),
          ("cyanUsererpProfile", 499),
          ("cyanUsererpv2Profile", 477),
          ("cyanUserethbwprofile", 445),
          ("cyanUserethkbwprofile", 449),
          ("cyanUserethlinkoamprofile", 447),
          ("cyanUserethoamprofile", 480),
          ("cyanUserethpcp2cospidprofile", 721),
          ("cyanUserethqueueprofile", 444),
          ("cyanUserethscheduleprofile", 511),
          ("cyanUserlagp", 725),
          ("cyanUsermplsexp2cospidprofile", 569),
          ("cyanUsermsprProfile", 724),
          ("cyanUserochtcaparamprofile", 733),
          ("cyanUseropticaltcaparamprofile", 708),
          ("cyanUserpgprofile", 723),
          ("cyanUsersonetsdhmsprofile", 720),
          ("cyanUsersonetsdhvcprofile", 719),
          ("cyanVcg", 439),
          ("cyanWmx", 136),
          ("cyanWmxotmPtp", 430),
          ("cyanWss402", 132),
          ("cyanWss404", 133),
          ("cyanWssF2", 160),
          ("cyanWssF4", 161),
          ("cyanWssF8", 162),
          ("cyanWssfotmPtp", 566),
          ("cyanWssfxXconApi", 580),
          ("cyanXc2800", 143),
          ("cyanXfpslot", 11),
          ("cyanXfpxcvr", 201),
          ("cyanXgewanTtp", 451),
          ("cyanZ22", 36),
          ("cyanZ22fan", 97),
          ("cyanZ33", 18),
          ("cyanZ33fan", 100),
          ("cyanZ77", 7),
          ("cyanZ77fan", 98),
          ("cyanZ77fanslot", 35),
          ("cyanmd", 457),
          ("dot1agma", 436),
          ("dot1agmd", 435),
          ("dot1agmep", 437),
          ("dot1agmip", 425),
          ("dot3ahmep", 431),
          ("eprotectiongroupT", 481),
          ("erpFlowpoint", 469),
          ("erpFlowpointpool", 468),
          ("ituOdu1gcc12tp", 371),
          ("ituOdu2gcc12tp", 372),
          ("ituOtu1gcc0tp", 369),
          ("ituOtu2gcc0tp", 370),
          ("mepTcaparameterprofile", 730),
          ("pbbEspTesi", 409),
          ("pbbFlowpoint", 422),
          ("pbbFlowpointpool", 410),
          ("pbbGtp", 440),
          ("pmpT", 705),
          ("tcaparameterprofile", 728),
          ("tcaparameterprofileT", 704),
          ("unavailable", 2),
          ("unequipped", 1),
          ("unknown", 0),
          ("userAsapT", 710),
          ("usermepTcaparameterprofile", 731),
          ("usertcaparameterprofile", 729),
          ("usertcaparameterprofileT", 707))
    )



class CyanProbablecausequalifierTc(Integer32, TextualConvention):
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
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
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
              380,
              381,
              382,
              383,
              384,
              385,
              386,
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
              441)
        )
    )
    namedValues = NamedValues(
        *(("airConditioningFail", 402),
          ("airDryerFail", 403),
          ("allPwrFeeds", 43),
          ("apdPwrSupply", 319),
          ("apsByteFail", 94),
          ("apsChMism", 105),
          ("apsModeMism", 96),
          ("apsincmpld", 106),
          ("batteryDischarge", 404),
          ("batteryFail", 405),
          ("blocked", 109),
          ("ccm", 107),
          ("cfgNotsupp", 75),
          ("comm1", 1),
          ("comm2", 2),
          ("commPowerFail", 426),
          ("compressorFail", 401),
          ("coolFanFail", 406),
          ("cooling", 307),
          ("cpuHi", 84),
          ("critical", 66),
          ("csf", 112),
          ("dbBad", 204),
          ("dbMism", 203),
          ("dccFail", 102),
          ("ddrPktCrc", 88),
          ("device", 381),
          ("deviceGpio", 384),
          ("dfltKbytes", 95),
          ("diskLow", 83),
          ("dsbld", 110),
          ("dupIpaddr", 61),
          ("dupNodename", 62),
          ("dyingGasp", 65),
          ("eccFail", 89),
          ("eidInvalid", 16),
          ("engineFail", 407),
          ("engineOperating", 408),
          ("error", 52),
          ("esmc", 100),
          ("exmism", 114),
          ("explosiveGas", 409),
          ("fail", 111),
          ("fanFilterDirty", 380),
          ("farEnd", 36),
          ("farendSfP", 90),
          ("farendSfW", 93),
          ("fire", 411),
          ("fireDetectorFail", 410),
          ("flood", 412),
          ("forced", 99),
          ("fuse1Fail", 21),
          ("fuse2Fail", 22),
          ("fuse3Fail", 23),
          ("fuse4Fail", 24),
          ("fuseFail", 413),
          ("gcc0Fail", 103),
          ("gcc12Fail", 104),
          ("generatorFail", 414),
          ("heatExchangerFail", 440),
          ("hiAirflow", 415),
          ("hiCurrent", 10),
          ("hiHumidity", 416),
          ("hiRxpwr", 4),
          ("hiRxpwrOh", 37),
          ("hiRxspanloss", 82),
          ("hiTemp", 301),
          ("hiTempIn", 303),
          ("hiTempOut", 305),
          ("hiTempRise", 12),
          ("hiTxpwr", 6),
          ("hiTxpwrOh", 39),
          ("hiVoltage", 8),
          ("hiWater", 417),
          ("hwInterLock", 321),
          ("i2cErr", 58),
          ("intrusion", 418),
          ("ip", 116),
          ("ipc", 86),
          ("lacp", 74),
          ("lbus", 87),
          ("lfd", 113),
          ("lockout", 97),
          ("lowBatteryVoltage", 419),
          ("lowCablePress", 422),
          ("lowCurrent", 11),
          ("lowFuel", 420),
          ("lowHumidity", 421),
          ("lowPostamprxpwr", 80),
          ("lowRxpwr", 5),
          ("lowRxpwrOh", 38),
          ("lowRxspanloss", 81),
          ("lowTemp", 302),
          ("lowTempIn", 304),
          ("lowTempOut", 306),
          ("lowTxpwr", 7),
          ("lowTxpwrOh", 40),
          ("lowVoltage", 9),
          ("lowWater", 423),
          ("macStat", 54),
          ("maint", 118),
          ("manual", 98),
          ("maxTca", 68),
          ("memAccess", 13),
          ("memFull", 17),
          ("memLow", 18),
          ("mfgmode", 85),
          ("midStage", 20),
          ("mismerge", 70),
          ("na", 0),
          ("noResp", 35),
          ("nodeIdMism", 92),
          ("och", 31),
          ("openDoor", 425),
          ("oscPrtcl", 101),
          ("overhead", 32),
          ("packet", 69),
          ("path", 108),
          ("payload", 33),
          ("powerSupplyFail", 428),
          ("protocol", 91),
          ("provMism", 34),
          ("pumpFail", 427),
          ("pwrA", 29),
          ("pwrAOverVltg", 14),
          ("pwrAUnderVltg", 15),
          ("pwrB", 30),
          ("pwrBOverVltg", 382),
          ("pwrBUnderVltg", 383),
          ("pwrFeed1Loss", 25),
          ("pwrFeed2Loss", 26),
          ("pwrFeed3Loss", 27),
          ("pwrFeed4Loss", 28),
          ("pwrFeedLoss", 67),
          ("pwrFeedOverVltg", 385),
          ("pwrFeedUnderVltg", 386),
          ("rdi", 55),
          ("rectifierFail", 429),
          ("rectifierFailMjr", 441),
          ("rectifierHiVoltage", 430),
          ("rectifierLowVoltage", 431),
          ("remoteAco", 439),
          ("rmep", 53),
          ("rtDiagNotsupp", 59),
          ("rx", 47),
          ("rxFifoErr", 320),
          ("rxFreq", 42),
          ("rxLaserHiCurrent", 313),
          ("rxLaserHiTemp", 311),
          ("rxLaserHiTxpwr", 315),
          ("rxLaserLowCurrent", 314),
          ("rxLaserLowTemp", 312),
          ("rxLaserLowTxpwr", 316),
          ("rxTec", 317),
          ("smoke", 432),
          ("sntpHost", 63),
          ("ssf", 64),
          ("ssm", 115),
          ("swBad", 202),
          ("swIncompatible", 207),
          ("swMism", 201),
          ("swUpgradeDsbld", 206),
          ("swUpgradeFail", 205),
          ("tec", 50),
          ("toxicGas", 433),
          ("tx", 46),
          ("txFreq", 41),
          ("txPayload", 49),
          ("unassigned", 3),
          ("uncertified", 60),
          ("unexmel", 71),
          ("unexmep", 72),
          ("unexperiod", 73),
          ("unitA", 44),
          ("unitB", 45),
          ("unitC", 56),
          ("unitD", 57),
          ("upm", 117),
          ("userDefinedAlm1", 424),
          ("userDefinedAlm2", 435),
          ("userDefinedAlm3", 436),
          ("userDefinedAlm4", 437),
          ("userDefinedAlm5", 438),
          ("ventilationFail", 434),
          ("warmUp", 19),
          ("wlenUnlocked", 318),
          ("xcon", 51),
          ("xover", 48))
    )



class AssignedseverityTTc(Integer32, TextualConvention):
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
        *(("critical", 6),
          ("freeChoice", 2),
          ("indeterminate", 0),
          ("major", 5),
          ("minor", 4),
          ("nonalarmed", 1),
          ("warning", 3))
    )



class EventtypeTc(Integer32, TextualConvention):
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
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
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
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              61,
              62,
              63,
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
              91)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 6),
          ("aps", 74),
          ("attributevaluechange", 3),
          ("autoprovisioning", 56),
          ("autoupgradedone", 37),
          ("autoupgradeip", 36),
          ("backupstatusdone", 25),
          ("backupstatusfail", 26),
          ("backupstatusip", 24),
          ("clear", 79),
          ("coldrestart", 53),
          ("dbRestoredone", 28),
          ("dbRestorefail", 29),
          ("dbRestoreip", 27),
          ("eqptprotectionswitch", 81),
          ("equipped", 51),
          ("filetransferstatusdone", 22),
          ("filetransferstatusfail", 23),
          ("filetransferstatusip", 21),
          ("forced", 77),
          ("go2freerun", 72),
          ("heartbeat", 83),
          ("locked", 73),
          ("lockout", 75),
          ("loginend", 63),
          ("loginfail", 61),
          ("loginsucceed", 62),
          ("manual", 76),
          ("objectcreation", 1),
          ("objectdeletion", 2),
          ("parityerror", 57),
          ("physicaltopochange", 91),
          ("pll", 71),
          ("pmBeginunavailtime", 8),
          ("pmContses", 10),
          ("pmEndunavailtime", 9),
          ("pmStatechange", 11),
          ("pmStatechangetca", 12),
          ("protectionswitch", 82),
          ("revertive", 80),
          ("routechange", 5),
          ("ssm", 78),
          ("statechange", 4),
          ("swautorevertip", 39),
          ("swdwnlddone", 32),
          ("swdwnldfail", 33),
          ("swdwnldip", 31),
          ("swmanrevertip", 40),
          ("swmismatch", 55),
          ("swrevertdone", 38),
          ("swupgradedone", 35),
          ("swupgradeip", 34),
          ("tca", 7),
          ("unequipped", 52),
          ("unknown", 0),
          ("warmrestart", 54))
    )



# MIB Managed Objects in the order of their OIDs

_Cyan_ObjectIdentity = ObjectIdentity
cyan = _Cyan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533)
)
if mibBuilder.loadTexts:
    cyan.setStatus("current")
_CyanProducts_ObjectIdentity = ObjectIdentity
cyanProducts = _CyanProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 1)
)
if mibBuilder.loadTexts:
    cyanProducts.setStatus("current")
_CyanZ77_ObjectIdentity = ObjectIdentity
cyanZ77 = _CyanZ77_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 1, 1)
)
_CyanLAMP_ObjectIdentity = ObjectIdentity
cyanLAMP = _CyanLAMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 1, 2)
)
_CyanZ33_ObjectIdentity = ObjectIdentity
cyanZ33 = _CyanZ33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 1, 3)
)
_CyanZ22_ObjectIdentity = ObjectIdentity
cyanZ22 = _CyanZ22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 1, 5)
)
_CyanMibModules_ObjectIdentity = ObjectIdentity
cyanMibModules = _CyanMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5)
)
if mibBuilder.loadTexts:
    cyanMibModules.setStatus("current")
_CyanAlarmObjectTypes_ObjectIdentity = ObjectIdentity
cyanAlarmObjectTypes = _CyanAlarmObjectTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20)
)
if mibBuilder.loadTexts:
    cyanAlarmObjectTypes.setStatus("current")
_CyanAlarmProbCause_Type = CyanProbablecauseTc
_CyanAlarmProbCause_Object = MibScalar
cyanAlarmProbCause = _CyanAlarmProbCause_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 1),
    _CyanAlarmProbCause_Type()
)
cyanAlarmProbCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmProbCause.setStatus("current")
_CyanAlarmProbCauseQualifier_Type = CyanProbablecausequalifierTc
_CyanAlarmProbCauseQualifier_Object = MibScalar
cyanAlarmProbCauseQualifier = _CyanAlarmProbCauseQualifier_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 2),
    _CyanAlarmProbCauseQualifier_Type()
)
cyanAlarmProbCauseQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmProbCauseQualifier.setStatus("current")
_CyanAlarmSourceType_Type = CyanTypeTc
_CyanAlarmSourceType_Object = MibScalar
cyanAlarmSourceType = _CyanAlarmSourceType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 3),
    _CyanAlarmSourceType_Type()
)
cyanAlarmSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmSourceType.setStatus("current")
_CyanAlarmSourceAddress_Type = DisplayString
_CyanAlarmSourceAddress_Object = MibScalar
cyanAlarmSourceAddress = _CyanAlarmSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 4),
    _CyanAlarmSourceAddress_Type()
)
cyanAlarmSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmSourceAddress.setStatus("current")
_CyanAlarmState_Type = CyanAlarmstateTc
_CyanAlarmState_Object = MibScalar
cyanAlarmState = _CyanAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 5),
    _CyanAlarmState_Type()
)
cyanAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmState.setStatus("current")
_CyanAlarmSeverity_Type = AssignedseverityTTc
_CyanAlarmSeverity_Object = MibScalar
cyanAlarmSeverity = _CyanAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 6),
    _CyanAlarmSeverity_Type()
)
cyanAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmSeverity.setStatus("current")
_CyanAlarmReportingTimeStamp_Type = Integer32
_CyanAlarmReportingTimeStamp_Object = MibScalar
cyanAlarmReportingTimeStamp = _CyanAlarmReportingTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 7),
    _CyanAlarmReportingTimeStamp_Type()
)
cyanAlarmReportingTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmReportingTimeStamp.setStatus("current")
_CyanAlarmAdditionalText_Type = DisplayString
_CyanAlarmAdditionalText_Object = MibScalar
cyanAlarmAdditionalText = _CyanAlarmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 8),
    _CyanAlarmAdditionalText_Type()
)
cyanAlarmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmAdditionalText.setStatus("current")
_CyanEventType_Type = EventtypeTc
_CyanEventType_Object = MibScalar
cyanEventType = _CyanEventType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 9),
    _CyanEventType_Type()
)
cyanEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventType.setStatus("current")
_CyanEventName_Type = DisplayString
_CyanEventName_Object = MibScalar
cyanEventName = _CyanEventName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 10),
    _CyanEventName_Type()
)
cyanEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventName.setStatus("current")
_CyanEventSourceType_Type = CyanTypeTc
_CyanEventSourceType_Object = MibScalar
cyanEventSourceType = _CyanEventSourceType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 11),
    _CyanEventSourceType_Type()
)
cyanEventSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventSourceType.setStatus("current")
_CyanEventSourceAddress_Type = DisplayString
_CyanEventSourceAddress_Object = MibScalar
cyanEventSourceAddress = _CyanEventSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 12),
    _CyanEventSourceAddress_Type()
)
cyanEventSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventSourceAddress.setStatus("current")
_CyanEventReportingTimeStamp_Type = Integer32
_CyanEventReportingTimeStamp_Object = MibScalar
cyanEventReportingTimeStamp = _CyanEventReportingTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 13),
    _CyanEventReportingTimeStamp_Type()
)
cyanEventReportingTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventReportingTimeStamp.setStatus("current")
_CyanEventAdditionalText_Type = DisplayString
_CyanEventAdditionalText_Object = MibScalar
cyanEventAdditionalText = _CyanEventAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 14),
    _CyanEventAdditionalText_Type()
)
cyanEventAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventAdditionalText.setStatus("current")
_CyanEventNodeName_Type = DisplayString
_CyanEventNodeName_Object = MibScalar
cyanEventNodeName = _CyanEventNodeName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 15),
    _CyanEventNodeName_Type()
)
cyanEventNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventNodeName.setStatus("current")
_CyanAlarmNodeName_Type = DisplayString
_CyanAlarmNodeName_Object = MibScalar
cyanAlarmNodeName = _CyanAlarmNodeName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 16),
    _CyanAlarmNodeName_Type()
)
cyanAlarmNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmNodeName.setStatus("current")
_CyanAlarmSourceDescription_Type = DisplayString
_CyanAlarmSourceDescription_Object = MibScalar
cyanAlarmSourceDescription = _CyanAlarmSourceDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 17),
    _CyanAlarmSourceDescription_Type()
)
cyanAlarmSourceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmSourceDescription.setStatus("current")
_CyanAlarmSourceOSSLabel_Type = DisplayString
_CyanAlarmSourceOSSLabel_Object = MibScalar
cyanAlarmSourceOSSLabel = _CyanAlarmSourceOSSLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 18),
    _CyanAlarmSourceOSSLabel_Type()
)
cyanAlarmSourceOSSLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmSourceOSSLabel.setStatus("current")
_CyanEventSourceDescription_Type = DisplayString
_CyanEventSourceDescription_Object = MibScalar
cyanEventSourceDescription = _CyanEventSourceDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 19),
    _CyanEventSourceDescription_Type()
)
cyanEventSourceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventSourceDescription.setStatus("current")
_CyanEventSourceOSSLabel_Type = DisplayString
_CyanEventSourceOSSLabel_Object = MibScalar
cyanEventSourceOSSLabel = _CyanEventSourceOSSLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 20),
    _CyanEventSourceOSSLabel_Type()
)
cyanEventSourceOSSLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventSourceOSSLabel.setStatus("current")
_CyanAlarmObjectGroups_ObjectIdentity = ObjectIdentity
cyanAlarmObjectGroups = _CyanAlarmObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 21)
)
if mibBuilder.loadTexts:
    cyanAlarmObjectGroups.setStatus("current")
_CyanAlarms_ObjectIdentity = ObjectIdentity
cyanAlarms = _CyanAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30)
)
if mibBuilder.loadTexts:
    cyanAlarms.setStatus("current")
_CyanEntityModules_ObjectIdentity = ObjectIdentity
cyanEntityModules = _CyanEntityModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30)
)
if mibBuilder.loadTexts:
    cyanEntityModules.setStatus("current")

# Managed Objects groups

cyanAlarmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 21, 1)
)
cyanAlarmObjectGroup.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmObjectGroup.setStatus("current")

cyanEventObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 21, 2)
)
cyanEventObjectGroup.setObjects(
      *(("CYAN-MIB", "cyanEventType"),
        ("CYAN-MIB", "cyanEventName"),
        ("CYAN-MIB", "cyanEventSourceType"),
        ("CYAN-MIB", "cyanEventSourceAddress"),
        ("CYAN-MIB", "cyanEventReportingTimeStamp"),
        ("CYAN-MIB", "cyanEventAdditionalText"),
        ("CYAN-MIB", "cyanEventNodeName"),
        ("CYAN-MIB", "cyanEventSourceDescription"),
        ("CYAN-MIB", "cyanEventSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanEventObjectGroup.setStatus("current")


# Notification objects

cyanAlarmNa = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 1)
)
cyanAlarmNa.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmNa.setStatus(
        "current"
    )

cyanAlarmUnequipped = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 2)
)
cyanAlarmUnequipped.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmUnequipped.setStatus(
        "current"
    )

cyanAlarmEqptRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 3)
)
cyanAlarmEqptRestart.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEqptRestart.setStatus(
        "current"
    )

cyanAlarmEqptFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 4)
)
cyanAlarmEqptFail.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEqptFail.setStatus(
        "current"
    )

cyanAlarmEqptDgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 5)
)
cyanAlarmEqptDgrade.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEqptDgrade.setStatus(
        "current"
    )

cyanAlarmEqptMismtch = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 6)
)
cyanAlarmEqptMismtch.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEqptMismtch.setStatus(
        "current"
    )

cyanAlarmEqptUnexpected = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 7)
)
cyanAlarmEqptUnexpected.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEqptUnexpected.setStatus(
        "current"
    )

cyanAlarmEqptWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 8)
)
cyanAlarmEqptWarning.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEqptWarning.setStatus(
        "current"
    )

cyanAlarmNotConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 9)
)
cyanAlarmNotConfig.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmNotConfig.setStatus(
        "current"
    )

cyanAlarmAutoUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 12)
)
cyanAlarmAutoUpgrade.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmAutoUpgrade.setStatus(
        "current"
    )

cyanAlarmBatFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 32)
)
cyanAlarmBatFail.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmBatFail.setStatus(
        "current"
    )

cyanAlarmBatDgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 33)
)
cyanAlarmBatDgrade.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmBatDgrade.setStatus(
        "current"
    )

cyanAlarmTpLol = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 50)
)
cyanAlarmTpLol.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLol.setStatus(
        "current"
    )

cyanAlarmPreAmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 51)
)
cyanAlarmPreAmp.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmPreAmp.setStatus(
        "current"
    )

cyanAlarmTpLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 52)
)
cyanAlarmTpLos.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLos.setStatus(
        "current"
    )

cyanAlarmTpLoc = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 53)
)
cyanAlarmTpLoc.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLoc.setStatus(
        "current"
    )

cyanAlarmTpLof = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 54)
)
cyanAlarmTpLof.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLof.setStatus(
        "current"
    )

cyanAlarmTpAis = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 55)
)
cyanAlarmTpAis.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpAis.setStatus(
        "current"
    )

cyanAlarmTpLom = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 56)
)
cyanAlarmTpLom.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLom.setStatus(
        "current"
    )

cyanAlarmTpSf = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 57)
)
cyanAlarmTpSf.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpSf.setStatus(
        "current"
    )

cyanAlarmTpBdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 58)
)
cyanAlarmTpBdi.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpBdi.setStatus(
        "current"
    )

cyanAlarmTpFdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 59)
)
cyanAlarmTpFdi.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpFdi.setStatus(
        "current"
    )

cyanAlarmTpPmi = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 60)
)
cyanAlarmTpPmi.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpPmi.setStatus(
        "current"
    )

cyanAlarmTpSd = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 61)
)
cyanAlarmTpSd.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpSd.setStatus(
        "current"
    )

cyanAlarmTpRdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 62)
)
cyanAlarmTpRdi.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpRdi.setStatus(
        "current"
    )

cyanAlarmTpTim = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 63)
)
cyanAlarmTpTim.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpTim.setStatus(
        "current"
    )

cyanAlarmTpIae = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 64)
)
cyanAlarmTpIae.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpIae.setStatus(
        "current"
    )

cyanAlarmTpBiae = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 65)
)
cyanAlarmTpBiae.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpBiae.setStatus(
        "current"
    )

cyanAlarmTpOci = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 66)
)
cyanAlarmTpOci.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpOci.setStatus(
        "current"
    )

cyanAlarmTpLck = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 67)
)
cyanAlarmTpLck.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLck.setStatus(
        "current"
    )

cyanAlarmTpLoflom = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 68)
)
cyanAlarmTpLoflom.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLoflom.setStatus(
        "current"
    )

cyanAlarmTpSsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 69)
)
cyanAlarmTpSsf.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpSsf.setStatus(
        "current"
    )

cyanAlarmTpOorangeAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 70)
)
cyanAlarmTpOorangeAlm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpOorangeAlm.setStatus(
        "current"
    )

cyanAlarmTpOorangeWrn = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 71)
)
cyanAlarmTpOorangeWrn.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpOorangeWrn.setStatus(
        "current"
    )

cyanAlarmTpFaclpbk = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 72)
)
cyanAlarmTpFaclpbk.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpFaclpbk.setStatus(
        "current"
    )

cyanAlarmTpHighLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 73)
)
cyanAlarmTpHighLoss.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpHighLoss.setStatus(
        "current"
    )

cyanAlarmTpLowLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 74)
)
cyanAlarmTpLowLoss.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLowLoss.setStatus(
        "current"
    )

cyanAlarmTpFiber = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 75)
)
cyanAlarmTpFiber.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpFiber.setStatus(
        "current"
    )

cyanAlarmTpPlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 76)
)
cyanAlarmTpPlm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpPlm.setStatus(
        "current"
    )

cyanAlarmTpLtc = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 77)
)
cyanAlarmTpLtc.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLtc.setStatus(
        "current"
    )

cyanAlarmTpMsim = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 78)
)
cyanAlarmTpMsim.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpMsim.setStatus(
        "current"
    )

cyanAlarmProtFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 79)
)
cyanAlarmProtFail.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmProtFail.setStatus(
        "current"
    )

cyanAlarmCcm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 80)
)
cyanAlarmCcm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmCcm.setStatus(
        "current"
    )

cyanAlarmTpLfd = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 81)
)
cyanAlarmTpLfd.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLfd.setStatus(
        "current"
    )

cyanAlarmTpLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 82)
)
cyanAlarmTpLink.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLink.setStatus(
        "current"
    )

cyanAlarmTpGfp = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 83)
)
cyanAlarmTpGfp.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpGfp.setStatus(
        "current"
    )

cyanAlarmTpTpt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 84)
)
cyanAlarmTpTpt.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpTpt.setStatus(
        "current"
    )

cyanAlarmGtp = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 85)
)
cyanAlarmGtp.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmGtp.setStatus(
        "current"
    )

cyanAlarmTpSqm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 86)
)
cyanAlarmTpSqm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpSqm.setStatus(
        "current"
    )

cyanAlarmTpLoa = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 87)
)
cyanAlarmTpLoa.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLoa.setStatus(
        "current"
    )

cyanAlarmTpLti = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 88)
)
cyanAlarmTpLti.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLti.setStatus(
        "current"
    )

cyanAlarmLtm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 89)
)
cyanAlarmLtm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmLtm.setStatus(
        "current"
    )

cyanAlarmAps = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 90)
)
cyanAlarmAps.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmAps.setStatus(
        "current"
    )

cyanAlarmTpLop = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 91)
)
cyanAlarmTpLop.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLop.setStatus(
        "current"
    )

cyanAlarmTpUneq = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 92)
)
cyanAlarmTpUneq.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpUneq.setStatus(
        "current"
    )

cyanAlarmCsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 93)
)
cyanAlarmCsf.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmCsf.setStatus(
        "current"
    )

cyanAlarmExmism = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 94)
)
cyanAlarmExmism.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmExmism.setStatus(
        "current"
    )

cyanAlarmUpm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 95)
)
cyanAlarmUpm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmUpm.setStatus(
        "current"
    )

cyanAlarmProtCmd = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 96)
)
cyanAlarmProtCmd.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmProtCmd.setStatus(
        "current"
    )

cyanAlarmFarendCmd = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 97)
)
cyanAlarmFarendCmd.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmFarendCmd.setStatus(
        "current"
    )

cyanAlarmProtocolErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 98)
)
cyanAlarmProtocolErr.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmProtocolErr.setStatus(
        "current"
    )

cyanAlarmLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 99)
)
cyanAlarmLoopback.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmLoopback.setStatus(
        "current"
    )

cyanAlarmLmm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 100)
)
cyanAlarmLmm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmLmm.setStatus(
        "current"
    )

cyanAlarmDmm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 101)
)
cyanAlarmDmm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmDmm.setStatus(
        "current"
    )

cyanAlarmCommFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 102)
)
cyanAlarmCommFail.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmCommFail.setStatus(
        "current"
    )

cyanAlarmCommDgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 103)
)
cyanAlarmCommDgrade.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmCommDgrade.setStatus(
        "current"
    )

cyanAlarmPacketLpbk = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 104)
)
cyanAlarmPacketLpbk.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmPacketLpbk.setStatus(
        "current"
    )

cyanAlarmXcspktsloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 105)
)
cyanAlarmXcspktsloss.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmXcspktsloss.setStatus(
        "current"
    )

cyanAlarmXcspktserr = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 106)
)
cyanAlarmXcspktserr.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmXcspktserr.setStatus(
        "current"
    )

cyanAlarmSrcaddrmis = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 107)
)
cyanAlarmSrcaddrmis.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmSrcaddrmis.setStatus(
        "current"
    )

cyanAlarmArp = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 108)
)
cyanAlarmArp.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmArp.setStatus(
        "current"
    )

cyanAlarmTsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 109)
)
cyanAlarmTsa.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTsa.setStatus(
        "current"
    )

cyanAlarmErpPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 110)
)
cyanAlarmErpPort.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmErpPort.setStatus(
        "current"
    )

cyanAlarmTpLoomfi = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 111)
)
cyanAlarmTpLoomfi.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLoomfi.setStatus(
        "current"
    )

cyanAlarmSyncFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 202)
)
cyanAlarmSyncFail.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmSyncFail.setStatus(
        "current"
    )

cyanAlarmSyncDgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 203)
)
cyanAlarmSyncDgrade.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmSyncDgrade.setStatus(
        "current"
    )

cyanAlarmHoldover = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 204)
)
cyanAlarmHoldover.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmHoldover.setStatus(
        "current"
    )

cyanAlarmXcsholdover = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 205)
)
cyanAlarmXcsholdover.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmXcsholdover.setStatus(
        "current"
    )

cyanAlarmSyncExcmdActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 206)
)
cyanAlarmSyncExcmdActive.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmSyncExcmdActive.setStatus(
        "current"
    )

cyanAlarmEnvAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 302)
)
cyanAlarmEnvAlm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEnvAlm.setStatus(
        "current"
    )

cyanAlarmEnvWrn = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 303)
)
cyanAlarmEnvWrn.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEnvWrn.setStatus(
        "current"
    )

cyanAlarmIncmpld = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 402)
)
cyanAlarmIncmpld.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmIncmpld.setStatus(
        "current"
    )

cyanAlarmAdmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 403)
)
cyanAlarmAdmin.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmAdmin.setStatus(
        "current"
    )

cyanEventTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 10008)
)
cyanEventTca.setObjects(
      *(("CYAN-MIB", "cyanEventType"),
        ("CYAN-MIB", "cyanEventName"),
        ("CYAN-MIB", "cyanEventSourceType"),
        ("CYAN-MIB", "cyanEventSourceAddress"),
        ("CYAN-MIB", "cyanEventReportingTimeStamp"),
        ("CYAN-MIB", "cyanEventAdditionalText"),
        ("CYAN-MIB", "cyanEventNodeName"),
        ("CYAN-MIB", "cyanEventSourceDescription"),
        ("CYAN-MIB", "cyanEventSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanEventTca.setStatus(
        "current"
    )


# Notifications groups

cyanAlarmGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 50)
)
cyanAlarmGroup.setObjects(
      *(("CYAN-MIB", "cyanAlarmNa"),
        ("CYAN-MIB", "cyanAlarmUnequipped"),
        ("CYAN-MIB", "cyanAlarmEqptRestart"),
        ("CYAN-MIB", "cyanAlarmEqptFail"),
        ("CYAN-MIB", "cyanAlarmEqptDgrade"),
        ("CYAN-MIB", "cyanAlarmEqptMismtch"),
        ("CYAN-MIB", "cyanAlarmEqptUnexpected"),
        ("CYAN-MIB", "cyanAlarmEqptWarning"),
        ("CYAN-MIB", "cyanAlarmNotConfig"),
        ("CYAN-MIB", "cyanAlarmAutoUpgrade"),
        ("CYAN-MIB", "cyanAlarmBatFail"),
        ("CYAN-MIB", "cyanAlarmBatDgrade"),
        ("CYAN-MIB", "cyanAlarmTpLol"),
        ("CYAN-MIB", "cyanAlarmPreAmp"),
        ("CYAN-MIB", "cyanAlarmTpLos"),
        ("CYAN-MIB", "cyanAlarmTpLoc"),
        ("CYAN-MIB", "cyanAlarmTpLof"),
        ("CYAN-MIB", "cyanAlarmTpAis"),
        ("CYAN-MIB", "cyanAlarmTpLom"),
        ("CYAN-MIB", "cyanAlarmTpSf"),
        ("CYAN-MIB", "cyanAlarmTpBdi"),
        ("CYAN-MIB", "cyanAlarmTpFdi"),
        ("CYAN-MIB", "cyanAlarmTpPmi"),
        ("CYAN-MIB", "cyanAlarmTpSd"),
        ("CYAN-MIB", "cyanAlarmTpRdi"),
        ("CYAN-MIB", "cyanAlarmTpTim"),
        ("CYAN-MIB", "cyanAlarmTpIae"),
        ("CYAN-MIB", "cyanAlarmTpBiae"),
        ("CYAN-MIB", "cyanAlarmTpOci"),
        ("CYAN-MIB", "cyanAlarmTpLck"),
        ("CYAN-MIB", "cyanAlarmTpLoflom"),
        ("CYAN-MIB", "cyanAlarmTpSsf"),
        ("CYAN-MIB", "cyanAlarmTpOorangeAlm"),
        ("CYAN-MIB", "cyanAlarmTpOorangeWrn"),
        ("CYAN-MIB", "cyanAlarmTpFaclpbk"),
        ("CYAN-MIB", "cyanAlarmTpHighLoss"),
        ("CYAN-MIB", "cyanAlarmTpLowLoss"),
        ("CYAN-MIB", "cyanAlarmTpFiber"),
        ("CYAN-MIB", "cyanAlarmTpPlm"),
        ("CYAN-MIB", "cyanAlarmTpLtc"),
        ("CYAN-MIB", "cyanAlarmTpMsim"),
        ("CYAN-MIB", "cyanAlarmProtFail"),
        ("CYAN-MIB", "cyanAlarmCcm"),
        ("CYAN-MIB", "cyanAlarmTpLfd"),
        ("CYAN-MIB", "cyanAlarmTpLink"),
        ("CYAN-MIB", "cyanAlarmTpGfp"),
        ("CYAN-MIB", "cyanAlarmTpTpt"),
        ("CYAN-MIB", "cyanAlarmGtp"),
        ("CYAN-MIB", "cyanAlarmTpSqm"),
        ("CYAN-MIB", "cyanAlarmTpLoa"),
        ("CYAN-MIB", "cyanAlarmTpLti"),
        ("CYAN-MIB", "cyanAlarmLtm"),
        ("CYAN-MIB", "cyanAlarmAps"),
        ("CYAN-MIB", "cyanAlarmTpLop"),
        ("CYAN-MIB", "cyanAlarmTpUneq"),
        ("CYAN-MIB", "cyanAlarmCsf"),
        ("CYAN-MIB", "cyanAlarmExmism"),
        ("CYAN-MIB", "cyanAlarmUpm"),
        ("CYAN-MIB", "cyanAlarmProtCmd"),
        ("CYAN-MIB", "cyanAlarmFarendCmd"),
        ("CYAN-MIB", "cyanAlarmProtocolErr"),
        ("CYAN-MIB", "cyanAlarmLoopback"),
        ("CYAN-MIB", "cyanAlarmLmm"),
        ("CYAN-MIB", "cyanAlarmDmm"),
        ("CYAN-MIB", "cyanAlarmCommFail"),
        ("CYAN-MIB", "cyanAlarmCommDgrade"),
        ("CYAN-MIB", "cyanAlarmPacketLpbk"),
        ("CYAN-MIB", "cyanAlarmXcspktsloss"),
        ("CYAN-MIB", "cyanAlarmXcspktserr"),
        ("CYAN-MIB", "cyanAlarmSrcaddrmis"),
        ("CYAN-MIB", "cyanAlarmArp"),
        ("CYAN-MIB", "cyanAlarmTsa"),
        ("CYAN-MIB", "cyanAlarmErpPort"),
        ("CYAN-MIB", "cyanAlarmTpLoomfi"),
        ("CYAN-MIB", "cyanAlarmSyncFail"),
        ("CYAN-MIB", "cyanAlarmSyncDgrade"),
        ("CYAN-MIB", "cyanAlarmHoldover"),
        ("CYAN-MIB", "cyanAlarmXcsholdover"),
        ("CYAN-MIB", "cyanAlarmSyncExcmdActive"),
        ("CYAN-MIB", "cyanAlarmEnvAlm"),
        ("CYAN-MIB", "cyanAlarmEnvWrn"),
        ("CYAN-MIB", "cyanAlarmIncmpld"),
        ("CYAN-MIB", "cyanAlarmAdmin"),
        ("CYAN-MIB", "cyanEventTca"))
)
if mibBuilder.loadTexts:
    cyanAlarmGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cyanAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 60)
)
if mibBuilder.loadTexts:
    cyanAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-MIB",
    **{"CyanProbablecauseTc": CyanProbablecauseTc,
       "CyanAlarmstateTc": CyanAlarmstateTc,
       "CyanTypeTc": CyanTypeTc,
       "CyanProbablecausequalifierTc": CyanProbablecausequalifierTc,
       "AssignedseverityTTc": AssignedseverityTTc,
       "EventtypeTc": EventtypeTc,
       "cyan": cyan,
       "cyanProducts": cyanProducts,
       "cyanZ77": cyanZ77,
       "cyanLAMP": cyanLAMP,
       "cyanZ33": cyanZ33,
       "cyanZ22": cyanZ22,
       "cyanMibModules": cyanMibModules,
       "cyanAlarmMibModule": cyanAlarmMibModule,
       "cyanAlarmObjectTypes": cyanAlarmObjectTypes,
       "cyanAlarmProbCause": cyanAlarmProbCause,
       "cyanAlarmProbCauseQualifier": cyanAlarmProbCauseQualifier,
       "cyanAlarmSourceType": cyanAlarmSourceType,
       "cyanAlarmSourceAddress": cyanAlarmSourceAddress,
       "cyanAlarmState": cyanAlarmState,
       "cyanAlarmSeverity": cyanAlarmSeverity,
       "cyanAlarmReportingTimeStamp": cyanAlarmReportingTimeStamp,
       "cyanAlarmAdditionalText": cyanAlarmAdditionalText,
       "cyanEventType": cyanEventType,
       "cyanEventName": cyanEventName,
       "cyanEventSourceType": cyanEventSourceType,
       "cyanEventSourceAddress": cyanEventSourceAddress,
       "cyanEventReportingTimeStamp": cyanEventReportingTimeStamp,
       "cyanEventAdditionalText": cyanEventAdditionalText,
       "cyanEventNodeName": cyanEventNodeName,
       "cyanAlarmNodeName": cyanAlarmNodeName,
       "cyanAlarmSourceDescription": cyanAlarmSourceDescription,
       "cyanAlarmSourceOSSLabel": cyanAlarmSourceOSSLabel,
       "cyanEventSourceDescription": cyanEventSourceDescription,
       "cyanEventSourceOSSLabel": cyanEventSourceOSSLabel,
       "cyanAlarmObjectGroups": cyanAlarmObjectGroups,
       "cyanAlarmObjectGroup": cyanAlarmObjectGroup,
       "cyanEventObjectGroup": cyanEventObjectGroup,
       "cyanAlarms": cyanAlarms,
       "cyanAlarmNa": cyanAlarmNa,
       "cyanAlarmUnequipped": cyanAlarmUnequipped,
       "cyanAlarmEqptRestart": cyanAlarmEqptRestart,
       "cyanAlarmEqptFail": cyanAlarmEqptFail,
       "cyanAlarmEqptDgrade": cyanAlarmEqptDgrade,
       "cyanAlarmEqptMismtch": cyanAlarmEqptMismtch,
       "cyanAlarmEqptUnexpected": cyanAlarmEqptUnexpected,
       "cyanAlarmEqptWarning": cyanAlarmEqptWarning,
       "cyanAlarmNotConfig": cyanAlarmNotConfig,
       "cyanAlarmAutoUpgrade": cyanAlarmAutoUpgrade,
       "cyanAlarmBatFail": cyanAlarmBatFail,
       "cyanAlarmBatDgrade": cyanAlarmBatDgrade,
       "cyanAlarmTpLol": cyanAlarmTpLol,
       "cyanAlarmPreAmp": cyanAlarmPreAmp,
       "cyanAlarmTpLos": cyanAlarmTpLos,
       "cyanAlarmTpLoc": cyanAlarmTpLoc,
       "cyanAlarmTpLof": cyanAlarmTpLof,
       "cyanAlarmTpAis": cyanAlarmTpAis,
       "cyanAlarmTpLom": cyanAlarmTpLom,
       "cyanAlarmTpSf": cyanAlarmTpSf,
       "cyanAlarmTpBdi": cyanAlarmTpBdi,
       "cyanAlarmTpFdi": cyanAlarmTpFdi,
       "cyanAlarmTpPmi": cyanAlarmTpPmi,
       "cyanAlarmTpSd": cyanAlarmTpSd,
       "cyanAlarmTpRdi": cyanAlarmTpRdi,
       "cyanAlarmTpTim": cyanAlarmTpTim,
       "cyanAlarmTpIae": cyanAlarmTpIae,
       "cyanAlarmTpBiae": cyanAlarmTpBiae,
       "cyanAlarmTpOci": cyanAlarmTpOci,
       "cyanAlarmTpLck": cyanAlarmTpLck,
       "cyanAlarmTpLoflom": cyanAlarmTpLoflom,
       "cyanAlarmTpSsf": cyanAlarmTpSsf,
       "cyanAlarmTpOorangeAlm": cyanAlarmTpOorangeAlm,
       "cyanAlarmTpOorangeWrn": cyanAlarmTpOorangeWrn,
       "cyanAlarmTpFaclpbk": cyanAlarmTpFaclpbk,
       "cyanAlarmTpHighLoss": cyanAlarmTpHighLoss,
       "cyanAlarmTpLowLoss": cyanAlarmTpLowLoss,
       "cyanAlarmTpFiber": cyanAlarmTpFiber,
       "cyanAlarmTpPlm": cyanAlarmTpPlm,
       "cyanAlarmTpLtc": cyanAlarmTpLtc,
       "cyanAlarmTpMsim": cyanAlarmTpMsim,
       "cyanAlarmProtFail": cyanAlarmProtFail,
       "cyanAlarmCcm": cyanAlarmCcm,
       "cyanAlarmTpLfd": cyanAlarmTpLfd,
       "cyanAlarmTpLink": cyanAlarmTpLink,
       "cyanAlarmTpGfp": cyanAlarmTpGfp,
       "cyanAlarmTpTpt": cyanAlarmTpTpt,
       "cyanAlarmGtp": cyanAlarmGtp,
       "cyanAlarmTpSqm": cyanAlarmTpSqm,
       "cyanAlarmTpLoa": cyanAlarmTpLoa,
       "cyanAlarmTpLti": cyanAlarmTpLti,
       "cyanAlarmLtm": cyanAlarmLtm,
       "cyanAlarmAps": cyanAlarmAps,
       "cyanAlarmTpLop": cyanAlarmTpLop,
       "cyanAlarmTpUneq": cyanAlarmTpUneq,
       "cyanAlarmCsf": cyanAlarmCsf,
       "cyanAlarmExmism": cyanAlarmExmism,
       "cyanAlarmUpm": cyanAlarmUpm,
       "cyanAlarmProtCmd": cyanAlarmProtCmd,
       "cyanAlarmFarendCmd": cyanAlarmFarendCmd,
       "cyanAlarmProtocolErr": cyanAlarmProtocolErr,
       "cyanAlarmLoopback": cyanAlarmLoopback,
       "cyanAlarmLmm": cyanAlarmLmm,
       "cyanAlarmDmm": cyanAlarmDmm,
       "cyanAlarmCommFail": cyanAlarmCommFail,
       "cyanAlarmCommDgrade": cyanAlarmCommDgrade,
       "cyanAlarmPacketLpbk": cyanAlarmPacketLpbk,
       "cyanAlarmXcspktsloss": cyanAlarmXcspktsloss,
       "cyanAlarmXcspktserr": cyanAlarmXcspktserr,
       "cyanAlarmSrcaddrmis": cyanAlarmSrcaddrmis,
       "cyanAlarmArp": cyanAlarmArp,
       "cyanAlarmTsa": cyanAlarmTsa,
       "cyanAlarmErpPort": cyanAlarmErpPort,
       "cyanAlarmTpLoomfi": cyanAlarmTpLoomfi,
       "cyanAlarmSyncFail": cyanAlarmSyncFail,
       "cyanAlarmSyncDgrade": cyanAlarmSyncDgrade,
       "cyanAlarmHoldover": cyanAlarmHoldover,
       "cyanAlarmXcsholdover": cyanAlarmXcsholdover,
       "cyanAlarmSyncExcmdActive": cyanAlarmSyncExcmdActive,
       "cyanAlarmEnvAlm": cyanAlarmEnvAlm,
       "cyanAlarmEnvWrn": cyanAlarmEnvWrn,
       "cyanAlarmIncmpld": cyanAlarmIncmpld,
       "cyanAlarmAdmin": cyanAlarmAdmin,
       "cyanEventTca": cyanEventTca,
       "cyanAlarmGroup": cyanAlarmGroup,
       "cyanAlarmCompliance": cyanAlarmCompliance,
       "cyanEntityModules": cyanEntityModules}
)
