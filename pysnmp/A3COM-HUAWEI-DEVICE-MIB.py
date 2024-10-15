# SNMP MIB module (A3COM-HUAWEI-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:27 2024
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

(lswCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "lswCommon")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwLswDeviceAdmin = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18)
)
hwLswDeviceAdmin.setRevisions(
        ("2001-04-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HwLswTypeOfSlot(Integer32, TextualConvention):
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
              655,
              656,
              657,
              658,
              659,
              660,
              661,
              662,
              663,
              664,
              665,
              666,
              667,
              668,
              669,
              670,
              671,
              672,
              673,
              674,
              675,
              676,
              677,
              678,
              679,
              680,
              681,
              682,
              683,
              684,
              685,
              686,
              687,
              688,
              689,
              690,
              691,
              692,
              693,
              694,
              695,
              696,
              697,
              701,
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
              725,
              726,
              727,
              728,
              729,
              730,
              731,
              732,
              800,
              801,
              802,
              803,
              804,
              805,
              806,
              807,
              808,
              809,
              810,
              811,
              812,
              813,
              814,
              815,
              900,
              901,
              902,
              903,
              904,
              905,
              906,
              907,
              908,
              909,
              910,
              911,
              912,
              913,
              914,
              915,
              916,
              917,
              918,
              919,
              920,
              921,
              922,
              923,
              924,
              925,
              926,
              927,
              928,
              929,
              930,
              931,
              932,
              933,
              934,
              935,
              936,
              937,
              938,
              939,
              940,
              941,
              942,
              943,
              944,
              945,
              946,
              947,
              948,
              949,
              950,
              951,
              952,
              953,
              954,
              955,
              956,
              957,
              1201,
              1202,
              1203,
              1204,
              1205,
              1206,
              1207,
              1208,
              1209,
              1210,
              1211,
              1212,
              1213,
              1214,
              1215,
              1216,
              1217,
              1218,
              1219,
              1220,
              1221,
              1222,
              1223,
              1224,
              1225,
              1226,
              1227,
              1228,
              1229,
              1230)
        )
    )
    namedValues = NamedValues(
        *(("bOARD-TYPE-LS81FM24", 71),
          ("bOARD-TYPE-LS81FS24", 70),
          ("bOARD-TYPE-LS81FT48", 67),
          ("bOARD-TYPE-LS81GB8U", 68),
          ("bOARD-TYPE-LS81GP8U", 26),
          ("bOARD-TYPE-LS81GT8U", 69),
          ("bOARD-TYPE-LS82DSPU", 25),
          ("bOARD-TYPE-LS82FE48", 28),
          ("bOARD-TYPE-LS82GP20", 72),
          ("bOARD-TYPE-LS82GT20", 27),
          ("bOARD-TYPE-LS82HGMU", 84),
          ("bOARD-TYPE-LS82SRPB", 254),
          ("bOARD-TYPE-LS83FP20A", 83),
          ("bORAD-TYPE-LS83SRPC", 255),
          ("type-1000BASE-4GBIC", 54),
          ("type-1000BASE-4SFP", 53),
          ("type-1000BASE-FIXED-2SFP-T-2RJ45", 703),
          ("type-1000BASE-FIXED-4GBIC", 56),
          ("type-1000BASE-FIXED-4RJ45-4SFP-COMBO", 706),
          ("type-1000BASE-FIXED-4SFP", 55),
          ("type-1000BASE-LONG-FX", 12),
          ("type-1000BASE-LX-SM", 2),
          ("type-1000BASE-LX-SM-IR-SC", 41),
          ("type-1000BASE-LX-SM-LR-LC", 48),
          ("type-1000BASE-LX-SM-VLR-LC", 47),
          ("type-1000BASE-SX-MM", 3),
          ("type-1000BASE-SX-MM-SR-SC", 42),
          ("type-1000BASE-T-RJ45", 43),
          ("type-1000BASE-TX", 4),
          ("type-1000BASE-X-COMBO", 701),
          ("type-1000BASE-X-GBIC", 50),
          ("type-1000BASE-ZENITH-FX", 11),
          ("type-1000M-SFP", 18),
          ("type-100BASE-FX-MM-SR-SC", 45),
          ("type-100BASE-FX-SM-IR-SC", 44),
          ("type-100BASE-FX-SM-LR-SC", 49),
          ("type-100M-100BASE-TX", 7),
          ("type-100M-1310-BIDI", 705),
          ("type-100M-1550-BIDI", 704),
          ("type-100M-HUB", 8),
          ("type-100M-MULTIMODE-FX", 6),
          ("type-100M-MULTIMODE-FX-LC", 52),
          ("type-100M-SINGLEMODE-FX", 5),
          ("type-100M-SINGLEMODE-FX-LC", 51),
          ("type-10OR100M", 1),
          ("type-4T10OR100-4FX100MM", 15),
          ("type-4T10OR100-4FX100SM", 14),
          ("type-ADSL", 13),
          ("type-AHP1", 318),
          ("type-AHP2", 319),
          ("type-AHP4", 246),
          ("type-ASPL", 17),
          ("type-CLP1", 320),
          ("type-CLP2", 321),
          ("type-CLP4", 248),
          ("type-CR-IM-FW1A", 957),
          ("type-CR-IM-NAM1A", 942),
          ("type-CR-MRP-I", 489),
          ("type-CR-SF08C", 491),
          ("type-CR-SF18C", 490),
          ("type-CR-SPC-GP48LEF", 494),
          ("type-CR-SPC-GT48LEF", 495),
          ("type-CR-SPC-PUP4L-E", 497),
          ("type-CR-SPC-PUP4L-E-I", 936),
          ("type-CR-SPC-XP4L-E-I", 930),
          ("type-CR-SPC-XP4LEF", 493),
          ("type-CR-SPC-XP4LEF-I", 937),
          ("type-CR-SPC-XP8LEF", 492),
          ("type-CR-SPC-XP8LEF-I", 938),
          ("type-CR-SPE-3020-E", 496),
          ("type-CR-SPE-3020-E-I", 935),
          ("type-EPON-1000M", 702),
          ("type-ET16", 322),
          ("type-ET32", 250),
          ("type-EWPX1FWA0", 808),
          ("type-EWPX1G10XC0", 809),
          ("type-EWPX1G24XA0", 802),
          ("type-EWPX1G24XC0", 806),
          ("type-EWPX1G24XCE0", 814),
          ("type-EWPX1WAP0", 812),
          ("type-EWPX1WCM10C0", 810),
          ("type-EWPX1WCMB0", 805),
          ("type-EWPX1WCMC0", 807),
          ("type-EWPX1WCMCE0", 815),
          ("type-EWPX1WCMD0", 813),
          ("type-EWPX2CTGS16SC", 1230),
          ("type-EWPX2CTGS16SC0", 1213),
          ("type-EWPX2TGS16SC0", 691),
          ("type-EWPX2WCMD0", 686),
          ("type-EWPXM2GP24TSC0", 649),
          ("type-EWPXM2GP24TSD0", 645),
          ("type-EWPXM2GP24TXSD0", 646),
          ("type-EWPXM2GP48SC0", 651),
          ("type-EWPXM2GP48SD0", 648),
          ("type-EWPXM2MPUB0", 642),
          ("type-EWPXM2SRP12GB0", 643),
          ("type-EWPXM2SRPD0", 644),
          ("type-EWPXM2TGX2SC0", 650),
          ("type-EWPXM2TGX4SD0", 647),
          ("type-EWPXM3WCMD0", 1215),
          ("type-FP20", 66),
          ("type-FT32A", 81),
          ("type-FT48A", 37),
          ("type-FT48C", 65),
          ("type-GIGA-STACK-1M-PC", 46),
          ("type-GP24", 109),
          ("type-GP2U", 39),
          ("type-GP4U", 38),
          ("type-GP8U", 216),
          ("type-GT24", 108),
          ("type-GT4U", 82),
          ("type-GV48", 111),
          ("type-IM-ACG", 918),
          ("type-IM-FW-II", 914),
          ("type-IM-IPS", 915),
          ("type-IM-LB", 917),
          ("type-IM-NAM-II", 488),
          ("type-IM-NAT-II", 487),
          ("type-IM-SSL", 916),
          ("type-IMFW", 432),
          ("type-IMNAM", 400),
          ("type-IMNAT", 401),
          ("type-LS7500-GP48-SC", 652),
          ("type-LS7500-GP48-SD", 653),
          ("type-LS7500-GT48-SC", 654),
          ("type-LS7500-GT48-SD", 655),
          ("type-LS7500-SRPG1", 656),
          ("type-LS7500-SRPG2", 657),
          ("type-LS7500-XP4-SD", 658),
          ("type-LS7500-XP8-SD", 659),
          ("type-LS81FP48", 157),
          ("type-LS81FP48XL", 582),
          ("type-LS81FT48E", 153),
          ("type-LS81FT48F", 170),
          ("type-LS81FT48XL", 583),
          ("type-LS81FWA", 508),
          ("type-LS81GP12XL", 584),
          ("type-LS81GP16TM", 500),
          ("type-LS81GP24XL", 585),
          ("type-LS81GP2R", 505),
          ("type-LS81GP48", 220),
          ("type-LS81GP48XL", 586),
          ("type-LS81GP4R", 506),
          ("type-LS81GP4UB", 154),
          ("type-LS81GP8UB", 152),
          ("type-LS81GT24XL", 587),
          ("type-LS81GT48", 119),
          ("type-LS81GT48A", 156),
          ("type-LS81GT48B", 221),
          ("type-LS81GT48XL", 588),
          ("type-LS81GT8UE", 155),
          ("type-LS81IPSECA", 507),
          ("type-LS81MPUB", 581),
          ("type-LS81P12T", 151),
          ("type-LS81P12TE", 180),
          ("type-LS81PT4G", 172),
          ("type-LS81PT8G", 171),
          ("type-LS81SRPG0", 120),
          ("type-LS81SRPG1", 121),
          ("type-LS81SRPG13", 538),
          ("type-LS81SRPG14", 539),
          ("type-LS81SRPG15", 540),
          ("type-LS81SRPG2", 122),
          ("type-LS81SRPG3", 123),
          ("type-LS81T12P", 150),
          ("type-LS81T12PE", 179),
          ("type-LS81T16P", 222),
          ("type-LS81T32P", 223),
          ("type-LS81TGX1B", 536),
          ("type-LS81TGX1C", 176),
          ("type-LS81TGX2", 224),
          ("type-LS81TGX2XL", 589),
          ("type-LS81TGX4", 225),
          ("type-LS81VP4C", 501),
          ("type-LS81VSNP", 149),
          ("type-LS82GB4C", 22),
          ("type-LS82GP20A", 175),
          ("type-LS82GT20A", 174),
          ("type-LS82GT4C", 23),
          ("type-LS82O2CM", 19),
          ("type-LS82O4GM", 21),
          ("type-LS82P2CM", 20),
          ("type-LS82ST4C", 24),
          ("type-LS82T24B", 29),
          ("type-LS82VSNP", 509),
          ("type-LS8M1PT4GB0", 504),
          ("type-LS8M1PT8GB0", 503),
          ("type-LS8M1PT8P0", 502),
          ("type-LS8M1WCMA", 801),
          ("type-LSA1FB8U", 178),
          ("type-LSA1FP8U", 139),
          ("type-LSB1A4G8A", 63),
          ("type-LSB1A4G8B", 64),
          ("type-LSB1ACG1A0", 408),
          ("type-LSB1AFC1A0", 398),
          ("type-LSB1AHP4GCA", 247),
          ("type-LSB1CLP4GCA", 249),
          ("type-LSB1ET32GCA", 251),
          ("type-LSB1F32GA", 74),
          ("type-LSB1F32GB", 75),
          ("type-LSB1F32GC", 91),
          ("type-LSB1F32GCA", 190),
          ("type-LSB1F48GA", 33),
          ("type-LSB1F48GB", 34),
          ("type-LSB1FP20A", 35),
          ("type-LSB1FP20B", 36),
          ("type-LSB1FP20C", 90),
          ("type-LSB1FP20CA", 189),
          ("type-LSB1FT48A", 31),
          ("type-LSB1FT48B", 32),
          ("type-LSB1FT48C", 89),
          ("type-LSB1FW2A0", 379),
          ("type-LSB1FW8B", 184),
          ("type-LSB1FW8DB", 231),
          ("type-LSB1GP12A", 57),
          ("type-LSB1GP12B", 58),
          ("type-LSB1GP12C", 93),
          ("type-LSB1GP12CA", 194),
          ("type-LSB1GP12DB", 302),
          ("type-LSB1GP24B", 98),
          ("type-LSB1GP24C", 99),
          ("type-LSB1GP24CA", 195),
          ("type-LSB1GP24CB", 240),
          ("type-LSB1GP24DB", 229),
          ("type-LSB1GP24DC", 230),
          ("type-LSB1GP48DB", 241),
          ("type-LSB1GP48LDB", 380),
          ("type-LSB1GP8TB", 85),
          ("type-LSB1GP8TC", 86),
          ("type-LSB1GT12A", 78),
          ("type-LSB1GT12B", 79),
          ("type-LSB1GT12C", 92),
          ("type-LSB1GT12CA", 192),
          ("type-LSB1GT12DB", 303),
          ("type-LSB1GT24B", 96),
          ("type-LSB1GT24C", 97),
          ("type-LSB1GT24CA", 193),
          ("type-LSB1GT24DB", 228),
          ("type-LSB1GT48B", 117),
          ("type-LSB1GT48C", 118),
          ("type-LSB1GT48LDB", 307),
          ("type-LSB1GT8PB", 87),
          ("type-LSB1GT8PC", 88),
          ("type-LSB1GT8PCA", 196),
          ("type-LSB1GV48B", 102),
          ("type-LSB1GV48C", 103),
          ("type-LSB1GV48DA", 226),
          ("type-LSB1GV48DB", 183),
          ("type-LSB1IDSB", 186),
          ("type-LSB1IDSDB", 252),
          ("type-LSB1IPS1A0", 434),
          ("type-LSB1IPSB", 187),
          ("type-LSB1IPSEC8B", 185),
          ("type-LSB1IPSEC8DB", 232),
          ("type-LSB1LB1A0", 433),
          ("type-LSB1NAMB", 258),
          ("type-LSB1NATB", 165),
          ("type-LSB1P4G8A", 61),
          ("type-LSB1P4G8B", 62),
          ("type-LSB1P4G8C", 94),
          ("type-LSB1P4G8CA", 191),
          ("type-LSB1RGP2GDB", 350),
          ("type-LSB1RGP4GDB", 351),
          ("type-LSB1RSP2CA", 260),
          ("type-LSB1RSP2DC", 310),
          ("type-LSB1SP4B", 140),
          ("type-LSB1SP4C", 141),
          ("type-LSB1SP4CA", 201),
          ("type-LSB1SRP1M0", 300),
          ("type-LSB1SRP1M1", 301),
          ("type-LSB1SRP1N0", 105),
          ("type-LSB1SRP1N1", 106),
          ("type-LSB1SRP1N2", 107),
          ("type-LSB1SRP1N3", 163),
          ("type-LSB1SRP1N4", 337),
          ("type-LSB1SRP1N5", 338),
          ("type-LSB1SRP1N6", 339),
          ("type-LSB1SRP1N7", 340),
          ("type-LSB1SRP1NA0", 323),
          ("type-LSB1SRP1NA1", 324),
          ("type-LSB1SRP1NA2", 325),
          ("type-LSB1SRP1NA3", 326),
          ("type-LSB1SRP1NA4", 345),
          ("type-LSB1SRP1NA5", 346),
          ("type-LSB1SRP1NA6", 347),
          ("type-LSB1SRP1NA7", 348),
          ("type-LSB1SRP2E0", 313),
          ("type-LSB1SRP2E1", 314),
          ("type-LSB1SRP2E2", 315),
          ("type-LSB1SRP2E3", 316),
          ("type-LSB1SRP2N0", 181),
          ("type-LSB1SRP2N1", 253),
          ("type-LSB1SRP2N2", 257),
          ("type-LSB1SRP2N3", 182),
          ("type-LSB1SRP2N4", 341),
          ("type-LSB1SRP2N5", 342),
          ("type-LSB1SRP2N6", 343),
          ("type-LSB1SRP2N7", 344),
          ("type-LSB1SRPA", 30),
          ("type-LSB1SRPB", 73),
          ("type-LSB1SRPC", 104),
          ("type-LSB1SSL1A0", 399),
          ("type-LSB1TGX1A", 59),
          ("type-LSB1TGX1B", 60),
          ("type-LSB1TGX1C", 95),
          ("type-LSB1UP1B", 142),
          ("type-LSB1UP1C", 143),
          ("type-LSB1UP1CA", 200),
          ("type-LSB1VP2B", 164),
          ("type-LSB1VP2CA", 202),
          ("type-LSB1VP2DC", 311),
          ("type-LSB1VPNB", 166),
          ("type-LSB1WCM2A0", 804),
          ("type-LSB1XK1B", 158),
          ("type-LSB1XK1C", 159),
          ("type-LSB1XK1CA", 198),
          ("type-LSB1XK1DB", 304),
          ("type-LSB1XP2B", 100),
          ("type-LSB1XP2C", 101),
          ("type-LSB1XP2CA", 197),
          ("type-LSB1XP2CB", 242),
          ("type-LSB1XP2DB", 305),
          ("type-LSB1XP2DC", 306),
          ("type-LSB1XP4B", 144),
          ("type-LSB1XP4C", 145),
          ("type-LSB1XP4CA", 199),
          ("type-LSB1XP4DB", 312),
          ("type-LSB1XP4LDB", 244),
          ("type-LSB1XP4LDC", 245),
          ("type-LSB1XP4TDB", 308),
          ("type-LSB1XP4TDC", 309),
          ("type-LSB2FT48A", 76),
          ("type-LSB2FT48B", 77),
          ("type-LSB2FT48C", 116),
          ("type-LSB2FT48CA", 188),
          ("type-LSB2FW8DB", 355),
          ("type-LSB2GP24DB", 352),
          ("type-LSB2GP24DC", 353),
          ("type-LSB2GT24DB", 354),
          ("type-LSB2GV48DA", 349),
          ("type-LSB2GV48DB", 357),
          ("type-LSB2IPSEC8DB", 356),
          ("type-LSB2SRP1N0", 362),
          ("type-LSB2SRP1N1", 363),
          ("type-LSB2SRP1N2", 364),
          ("type-LSB2SRP1N3", 365),
          ("type-LSB2SRP1N4", 366),
          ("type-LSB2SRP1N5", 367),
          ("type-LSB2SRP1N6", 368),
          ("type-LSB2SRP1N7", 369),
          ("type-LSD1EP2A0", 525),
          ("type-LSD1GP12ES0", 574),
          ("type-LSD1GP16A0", 522),
          ("type-LSD1GP20A0", 516),
          ("type-LSD1GP20EA0", 520),
          ("type-LSD1GP20RA0", 521),
          ("type-LSD1GP20TA0", 517),
          ("type-LSD1GP20XA0", 519),
          ("type-LSD1GP24ES0", 547),
          ("type-LSD1GP24XES0", 549),
          ("type-LSD1GP36A0", 518),
          ("type-LSD1GP48ES0", 551),
          ("type-LSD1GT16A0", 523),
          ("type-LSD1GT16PES0", 546),
          ("type-LSD1GT24XES0", 548),
          ("type-LSD1MPUA", 515),
          ("type-LSD1RP2A0", 526),
          ("type-LSD1SRPA0", 543),
          ("type-LSD1SRPB0", 544),
          ("type-LSD1SRPC0", 545),
          ("type-LSD1XP1ES0", 573),
          ("type-LSD1XP2A0", 524),
          ("type-LSD1XP2ES0", 550),
          ("type-LSEXK1P", 218),
          ("type-LSEXP1P", 217),
          ("type-LSEXS1P", 219),
          ("type-LSG1GP8U", 112),
          ("type-LSG1GT8U", 113),
          ("type-LSG1TD1U", 115),
          ("type-LSG1TG1U", 114),
          ("type-LSGP8P", 167),
          ("type-LSH1PK2T", 707),
          ("type-LSP1XGT2P", 732),
          ("type-LSP5GP8P", 727),
          ("type-LSP5GT8P", 728),
          ("type-LSPM1CX2P", 271),
          ("type-LSPM1XP1P", 269),
          ("type-LSPM1XP2P", 270),
          ("type-LSPM2GP2P", 708),
          ("type-LSPM2SP2P", 725),
          ("type-LSPM2SP2PA", 726),
          ("type-LSQ1ACGASC0", 572),
          ("type-LSQ1AFCBSC0", 559),
          ("type-LSQ1AFDBSC0", 580),
          ("type-LSQ1CGP24TSC0", 570),
          ("type-LSQ1CGP24TSC3", 633),
          ("type-LSQ1CGV24PSC0", 604),
          ("type-LSQ1CGV24PSC1", 605),
          ("type-LSQ1CTGS16SC0", 1212),
          ("type-LSQ1FAB04A3", 693),
          ("type-LSQ1FAB04D3", 1226),
          ("type-LSQ1FAB08A0", 685),
          ("type-LSQ1FAB08A3", 694),
          ("type-LSQ1FAB08B0", 1229),
          ("type-LSQ1FAB08D3", 1225),
          ("type-LSQ1FAB12D3", 1224),
          ("type-LSQ1FP48SA", 528),
          ("type-LSQ1FP48USA0", 565),
          ("type-LSQ1FP48USA1", 566),
          ("type-LSQ1FV48SA", 514),
          ("type-LSQ1FV48USA0", 567),
          ("type-LSQ1FV48USA1", 568),
          ("type-LSQ1FWBSC0", 554),
          ("type-LSQ1FWBSC1", 577),
          ("type-LSQ1GP12EA", 532),
          ("type-LSQ1GP12SC0", 542),
          ("type-LSQ1GP12SC3", 623),
          ("type-LSQ1GP24SC", 529),
          ("type-LSQ1GP24TEB0", 606),
          ("type-LSQ1GP24TEB1", 607),
          ("type-LSQ1GP24TSA0", 663),
          ("type-LSQ1GP24TSC0", 571),
          ("type-LSQ1GP24TSC3", 624),
          ("type-LSQ1GP24TSD0", 608),
          ("type-LSQ1GP24TSD1", 609),
          ("type-LSQ1GP24TXSD0", 610),
          ("type-LSQ1GP24TXSD1", 611),
          ("type-LSQ1GP48EB0", 591),
          ("type-LSQ1GP48EB1", 620),
          ("type-LSQ1GP48SC0", 541),
          ("type-LSQ1GP48SC3", 625),
          ("type-LSQ1GP48SD0", 594),
          ("type-LSQ1GP48SD1", 595),
          ("type-LSQ1GT24SC", 530),
          ("type-LSQ1GT48SC0", 695),
          ("type-LSQ1GV24PSA0", 664),
          ("type-LSQ1GV24PSC0", 602),
          ("type-LSQ1GV24PSC1", 603),
          ("type-LSQ1GV40PSC0", 576),
          ("type-LSQ1GV48SA", 510),
          ("type-LSQ1GV48SC", 527),
          ("type-LSQ1GV48SC3", 626),
          ("type-LSQ1GV48SD0", 590),
          ("type-LSQ1GV48SD1", 593),
          ("type-LSQ1IAGSC0", 688),
          ("type-LSQ1IPSSC0", 592),
          ("type-LSQ1LBSC0", 637),
          ("type-LSQ1MPUA0", 552),
          ("type-LSQ1MPUA1", 553),
          ("type-LSQ1MPUA3", 627),
          ("type-LSQ1MPUB0", 560),
          ("type-LSQ1MPUB1", 561),
          ("type-LSQ1MPUB3", 632),
          ("type-LSQ1MPUB4", 634),
          ("type-LSQ1NAT24SC0", 638),
          ("type-LSQ1NSMSC0", 578),
          ("type-LSQ1NSMSC1", 579),
          ("type-LSQ1P24XGSC", 534),
          ("type-LSQ1PT16PSC0", 556),
          ("type-LSQ1PT16PSC1", 564),
          ("type-LSQ1PT4PSC0", 537),
          ("type-LSQ1PT4PSC1", 562),
          ("type-LSQ1PT8PSC0", 555),
          ("type-LSQ1PT8PSC1", 563),
          ("type-LSQ1QGC4SC0", 1217),
          ("type-LSQ1QGC4SC3", 1223),
          ("type-LSQ1QGS4SC0", 1216),
          ("type-LSQ1QGS4SC3", 1221),
          ("type-LSQ1QGS8SC3", 1219),
          ("type-LSQ1SRP12GB0", 575),
          ("type-LSQ1SRP12GB4", 639),
          ("type-LSQ1SRP1CB", 513),
          ("type-LSQ1SRP1CB3", 628),
          ("type-LSQ1SRP2XB", 512),
          ("type-LSQ1SRPA0", 596),
          ("type-LSQ1SRPA1", 597),
          ("type-LSQ1SRPA3", 629),
          ("type-LSQ1SRPB", 511),
          ("type-LSQ1SRPD0", 569),
          ("type-LSQ1SRPD3", 665),
          ("type-LSQ1SRPD4", 635),
          ("type-LSQ1SSLSC0", 636),
          ("type-LSQ1SUPA0", 666),
          ("type-LSQ1SUPA3", 692),
          ("type-LSQ1T24XGSC", 535),
          ("type-LSQ1TGS16SC0", 690),
          ("type-LSQ1TGS32SC3", 1220),
          ("type-LSQ1TGS48SC3", 1222),
          ("type-LSQ1TGS8EB3", 1227),
          ("type-LSQ1TGS8SC0", 640),
          ("type-LSQ1TGT24SC3", 1228),
          ("type-LSQ1TGX1EA", 533),
          ("type-LSQ1TGX2EB0", 612),
          ("type-LSQ1TGX2EB1", 613),
          ("type-LSQ1TGX2SC", 531),
          ("type-LSQ1TGX2SD0", 614),
          ("type-LSQ1TGX2SD1", 615),
          ("type-LSQ1TGX4EB0", 621),
          ("type-LSQ1TGX4EB1", 622),
          ("type-LSQ1TGX4SD0", 616),
          ("type-LSQ1TGX4SD1", 617),
          ("type-LSQ1TGX8SD0", 618),
          ("type-LSQ1TGX8SD1", 619),
          ("type-LSQ1WCMB0", 803),
          ("type-LSQ1WCMD0", 687),
          ("type-LSQ2FP48SA0", 598),
          ("type-LSQ2FP48SA1", 599),
          ("type-LSQ2FP48SA3", 630),
          ("type-LSQ2FT48SA0", 600),
          ("type-LSQ2FT48SA1", 601),
          ("type-LSQ2FT48SA3", 631),
          ("type-LSQ3PT4PSC0", 641),
          ("type-LSQ4PT16PSC0", 662),
          ("type-LSQ4PT4PSC0", 660),
          ("type-LSQ4PT8PSC0", 661),
          ("type-LSR1ACG1A1", 448),
          ("type-LSR1DGP10L1", 483),
          ("type-LSR1DPSP4L1", 480),
          ("type-LSR1DPUP1L1", 479),
          ("type-LSR1DRSP2L1", 900),
          ("type-LSR1DRUP1L1", 478),
          ("type-LSR1DTCP8L1", 481),
          ("type-LSR1DXP1L1", 482),
          ("type-LSR1FW2A1", 441),
          ("type-LSR1GP24LEB1", 421),
          ("type-LSR1GP24LEC1", 422),
          ("type-LSR1GP24LEF1", 444),
          ("type-LSR1GP48LEB1", 425),
          ("type-LSR1GP48LEC1", 426),
          ("type-LSR1GP48LEF1", 466),
          ("type-LSR1GT24LEC1", 420),
          ("type-LSR1GT48LEB1", 423),
          ("type-LSR1GT48LEC1", 424),
          ("type-LSR1IPS1A1", 449),
          ("type-LSR1LB1A1", 446),
          ("type-LSR1LN1BNL1", 484),
          ("type-LSR1LN2BL1", 485),
          ("type-LSR1NSM1A1", 447),
          ("type-LSR1SRP2B1", 416),
          ("type-LSR1SRP2B2", 418),
          ("type-LSR1SRP2C1", 417),
          ("type-LSR1SRP2C2", 419),
          ("type-LSR1SRP2D1", 486),
          ("type-LSR1SSL1A1", 442),
          ("type-LSR1WCM2A1", 811),
          ("type-LSR1WCM3A1", 927),
          ("type-LSR1XP16REB1", 465),
          ("type-LSR1XP16REC1", 919),
          ("type-LSR1XP2LEB1", 428),
          ("type-LSR1XP2LEC1", 429),
          ("type-LSR1XP4LEB1", 430),
          ("type-LSR1XP4LEC1", 431),
          ("type-LSR1XP4LEF1", 445),
          ("type-LSR2GP24LEB1", 450),
          ("type-LSR2GT24LEB1", 451),
          ("type-LSR2GT48LEB1", 452),
          ("type-LSR2GV48REB1", 427),
          ("type-LSR2SRP2B1", 943),
          ("type-LSR2SRP2B2", 944),
          ("type-LSR2SRP2C1", 696),
          ("type-LSR2SRP2C2", 697),
          ("type-LSR2SRP2D1", 945),
          ("type-LSSTK24G", 173),
          ("type-LST1ACG1A1", 476),
          ("type-LST1FW2A1", 473),
          ("type-LST1FW3A1", 941),
          ("type-LST1GP48LEA1", 906),
          ("type-LST1GP48LEB1", 436),
          ("type-LST1GP48LEC1", 413),
          ("type-LST1GP48LEF1", 467),
          ("type-LST1GP48LEY1", 909),
          ("type-LST1GP48LEZ1", 912),
          ("type-LST1GT48LEA1", 905),
          ("type-LST1GT48LEB1", 435),
          ("type-LST1GT48LEC1", 412),
          ("type-LST1GT48LEY1", 908),
          ("type-LST1IPS1A1", 477),
          ("type-LST1LB1A1", 475),
          ("type-LST1MRPNC1", 409),
          ("type-LST1NSM1A1", 474),
          ("type-LST1SF08B1", 411),
          ("type-LST1SF08C1", 498),
          ("type-LST1SF18B1", 410),
          ("type-LST1SF18C1", 499),
          ("type-LST1XP16LEB1", 928),
          ("type-LST1XP16LEC1", 929),
          ("type-LST1XP16LEY1", 948),
          ("type-LST1XP32REB1", 439),
          ("type-LST1XP32REC1", 440),
          ("type-LST1XP32REY1", 910),
          ("type-LST1XP4LEB1", 437),
          ("type-LST1XP4LEC1", 414),
          ("type-LST1XP8LEB1", 438),
          ("type-LST1XP8LEC1", 415),
          ("type-LST1XP8LEF1", 468),
          ("type-LST1XP8LEY1", 911),
          ("type-LST1XP8LEZ1", 913),
          ("type-LST2MRPNC1", 931),
          ("type-LST2SF08C1", 932),
          ("type-LST2SF18C1", 933),
          ("type-LST2XP32REB1", 925),
          ("type-LST2XP32REC1", 926),
          ("type-LST2XP32REY1", 947),
          ("type-LST2XP4LEB1", 923),
          ("type-LST2XP4LEC1", 924),
          ("type-LST2XP8LEA1", 907),
          ("type-LST2XP8LEB1", 920),
          ("type-LST2XP8LEC1", 921),
          ("type-LST2XP8LEF1", 922),
          ("type-LST3XP8LEB1", 939),
          ("type-LST3XP8LEC1", 940),
          ("type-LST3XP8LEY1", 946),
          ("type-LSU1FAB04A0", 667),
          ("type-LSU1FAB04B0", 1207),
          ("type-LSU1FAB04D0", 1211),
          ("type-LSU1FAB08A0", 668),
          ("type-LSU1FAB08B0", 1208),
          ("type-LSU1FAB08D0", 1206),
          ("type-LSU1FAB12B0", 1210),
          ("type-LSU1FAB12D0", 1209),
          ("type-LSU1GP24TSE0", 689),
          ("type-LSU1GP24TXEA0", 674),
          ("type-LSU1GP24TXEB0", 675),
          ("type-LSU1GP24TXSE0", 676),
          ("type-LSU1GP48EA0", 677),
          ("type-LSU1GP48EB0", 678),
          ("type-LSU1GP48SE0", 679),
          ("type-LSU1GT48EA0", 680),
          ("type-LSU1GT48SE0", 681),
          ("type-LSU1QGC4SF0", 1201),
          ("type-LSU1QGS4SF0", 1204),
          ("type-LSU1QGS8SF0", 1202),
          ("type-LSU1TGS32SF0", 1205),
          ("type-LSU1TGS48SF0", 1203),
          ("type-LSU1TGS8EA0", 669),
          ("type-LSU1TGS8EB0", 670),
          ("type-LSU1TGS8SE0", 671),
          ("type-LSU1TGT24SF0", 1218),
          ("type-LSU1TGX4EA0", 682),
          ("type-LSU1TGX4EB0", 683),
          ("type-LSU1TGX4SE0", 684),
          ("type-LSUM3WCMD0", 1214),
          ("type-LSUTGS16SC0", 672),
          ("type-LSW1XGT2P0", 731),
          ("type-LSW1XGT4P0", 730),
          ("type-LSWM148POEM", 715),
          ("type-LSWM1FC4P", 729),
          ("type-LSWM1FW10", 716),
          ("type-LSWM1GP16P", 710),
          ("type-LSWM1GT16P", 709),
          ("type-LSWM1IPS10", 718),
          ("type-LSWM1SP2P", 713),
          ("type-LSWM1SP4P", 714),
          ("type-LSWM1WCM10", 717),
          ("type-LSWM1WCM20", 719),
          ("type-LSWM1XP2P", 711),
          ("type-LSWM1XP4P", 712),
          ("type-LSXK1P", 168),
          ("type-LSXP2P", 169),
          ("type-LUS1SUPA0", 673),
          ("type-Main", 256),
          ("type-NULL", 0),
          ("type-PC4U", 80),
          ("type-PIC-CLF2G8L", 901),
          ("type-PIC-CLF4G8L", 902),
          ("type-PICAHP1L", 402),
          ("type-PICALP4L", 403),
          ("type-PICCHP4L", 404),
          ("type-PICCHS1G4L", 405),
          ("type-PICCLS4G4L", 406),
          ("type-PICCSP1L", 407),
          ("type-RGP2", 358),
          ("type-RGP4", 359),
          ("type-RSP2", 259),
          ("type-SA11MPUA0", 557),
          ("type-SA11MPUB0", 558),
          ("type-SP4", 146),
          ("type-SPC-GP24L", 453),
          ("type-SPC-GP24LA", 955),
          ("type-SPC-GP48L", 455),
          ("type-SPC-GP48L-S-SDI", 463),
          ("type-SPC-GP48LA", 951),
          ("type-SPC-GT48L", 454),
          ("type-SPC-GT48L-SDI", 462),
          ("type-SPC-GT48LA", 952),
          ("type-SPC-XP16RA", 956),
          ("type-SPC-XP2L", 456),
          ("type-SPC-XP2LA", 954),
          ("type-SPC-XP4L", 457),
          ("type-SPC-XP4L-S-SDI", 461),
          ("type-SPC-XP4LA", 953),
          ("type-SPE-1010-E-II", 470),
          ("type-SPE-1010-II", 469),
          ("type-SPE-1020-E-II", 472),
          ("type-SPE-1020-II", 471),
          ("type-SPE-2010-E", 459),
          ("type-SPE-2020-E", 460),
          ("type-SR01AHP1GWA", 327),
          ("type-SR01AHP2GWA", 328),
          ("type-SR01AHP4GWA", 262),
          ("type-SR01CLP1GWA", 329),
          ("type-SR01CLP2GWA", 330),
          ("type-SR01CLP4GWA", 263),
          ("type-SR01DCL1G8L", 390),
          ("type-SR01DCL2G8L", 391),
          ("type-SR01DET32G2L", 443),
          ("type-SR01DET8G8L", 392),
          ("type-SR01DGP10L", 373),
          ("type-SR01DGP20R", 376),
          ("type-SR01DGT20R", 384),
          ("type-SR01DPH2G6L", 388),
          ("type-SR01DPL2G6L", 387),
          ("type-SR01DPLP8L", 377),
          ("type-SR01DPS2G4L", 389),
          ("type-SR01DPSP4L", 385),
          ("type-SR01DPUP1L", 386),
          ("type-SR01DQCP4L", 396),
          ("type-SR01DRSP2L", 374),
          ("type-SR01DRUP1L", 375),
          ("type-SR01DTCP8L", 397),
          ("type-SR01DXP1L", 372),
          ("type-SR01DXP2R", 378),
          ("type-SR01ET16GWA", 331),
          ("type-SR01ET32GWA", 264),
          ("type-SR01F32GL", 134),
          ("type-SR01F32GW", 135),
          ("type-SR01F32GWA", 205),
          ("type-SR01FP20W", 132),
          ("type-SR01FP20WA", 204),
          ("type-SR01FT48L", 129),
          ("type-SR01FT48W", 130),
          ("type-SR01FT48WA", 203),
          ("type-SR01FW8VB", 236),
          ("type-SR01GP12L", 127),
          ("type-SR01GP12VB", 332),
          ("type-SR01GP12W", 128),
          ("type-SR01GP12WA", 209),
          ("type-SR01GP24VC", 234),
          ("type-SR01GP24WA", 210),
          ("type-SR01GT12W", 133),
          ("type-SR01GT12WA", 207),
          ("type-SR01GT24VB", 233),
          ("type-SR01GT24WA", 208),
          ("type-SR01GT8PL", 136),
          ("type-SR01GT8PW", 137),
          ("type-SR01GT8PWA", 211),
          ("type-SR01GV48VB", 227),
          ("type-SR01IDSVB", 265),
          ("type-SR01IPSEC8VB", 237),
          ("type-SR01LN1BNA0", 381),
          ("type-SR01LN1BQH0", 371),
          ("type-SR01LN2BNA0", 383),
          ("type-SR01LN2BQH0", 382),
          ("type-SR01NAML", 267),
          ("type-SR01NATL", 238),
          ("type-SR01P4G8W", 138),
          ("type-SR01P4G8WA", 206),
          ("type-SR01RSP2WA", 268),
          ("type-SR01SP4WA", 215),
          ("type-SR01SRPUA", 126),
          ("type-SR01SRPUB", 125),
          ("type-SR01SRPUC", 160),
          ("type-SR01SRPUD", 161),
          ("type-SR01SRPUE", 162),
          ("type-SR01SRPUEA", 336),
          ("type-SR01SRPUF", 266),
          ("type-SR01SRPUQ", 317),
          ("type-SR01UP1WA", 214),
          ("type-SR01VP2WA", 235),
          ("type-SR01VPNL", 239),
          ("type-SR01XK1VB", 333),
          ("type-SR01XK1W", 131),
          ("type-SR01XK1WA", 213),
          ("type-SR01XP2VC", 334),
          ("type-SR01XP2WA", 212),
          ("type-SR01XP4LVB", 335),
          ("type-SR01XP4LVC", 261),
          ("type-SR02FW8VB", 360),
          ("type-SR02IPSEC8VB", 361),
          ("type-SR02OPMA0", 464),
          ("type-SR02SRP1E3", 394),
          ("type-SR02SRP1F3", 904),
          ("type-SR02SRP1M3", 395),
          ("type-SR02SRP2E3", 393),
          ("type-SR02SRP2F3", 903),
          ("type-SR02SRP2G3", 934),
          ("type-SR02SRPUE", 370),
          ("type-SR06SRP2E3", 458),
          ("type-SR0M2SRP1G3", 950),
          ("type-SR0M2SRP2G3", 949),
          ("type-STACK", 10),
          ("type-STK-1000BASE-T", 272),
          ("type-TGX1A", 40),
          ("type-UP1", 147),
          ("type-VDSL", 9),
          ("type-VP2", 177),
          ("type-VSPL", 16),
          ("type-WX5002MPU", 800),
          ("type-XP2", 110),
          ("type-XP4", 148),
          ("type-XP4L", 243))
    )



# MIB Managed Objects in the order of their OIDs

_HwLswSystemPara_ObjectIdentity = ObjectIdentity
hwLswSystemPara = _HwLswSystemPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1)
)
_HwLswSysIpAddr_Type = IpAddress
_HwLswSysIpAddr_Object = MibScalar
hwLswSysIpAddr = _HwLswSysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 1),
    _HwLswSysIpAddr_Type()
)
hwLswSysIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSysIpAddr.setStatus("current")
_HwLswSysIpMask_Type = IpAddress
_HwLswSysIpMask_Object = MibScalar
hwLswSysIpMask = _HwLswSysIpMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 2),
    _HwLswSysIpMask_Type()
)
hwLswSysIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSysIpMask.setStatus("current")


class _HwLswSysCpuRatio_Type(Integer32):
    """Custom type hwLswSysCpuRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwLswSysCpuRatio_Type.__name__ = "Integer32"
_HwLswSysCpuRatio_Object = MibScalar
hwLswSysCpuRatio = _HwLswSysCpuRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 3),
    _HwLswSysCpuRatio_Type()
)
hwLswSysCpuRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSysCpuRatio.setStatus("current")


class _HwLswSysVersion_Type(DisplayString):
    """Custom type hwLswSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwLswSysVersion_Type.__name__ = "DisplayString"
_HwLswSysVersion_Object = MibScalar
hwLswSysVersion = _HwLswSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 4),
    _HwLswSysVersion_Type()
)
hwLswSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSysVersion.setStatus("current")
_HwLswSysTime_Type = DateAndTime
_HwLswSysTime_Object = MibScalar
hwLswSysTime = _HwLswSysTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 5),
    _HwLswSysTime_Type()
)
hwLswSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswSysTime.setStatus("current")


class _HwLswSysUNMCastDropEnable_Type(Integer32):
    """Custom type hwLswSysUNMCastDropEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwLswSysUNMCastDropEnable_Type.__name__ = "Integer32"
_HwLswSysUNMCastDropEnable_Object = MibScalar
hwLswSysUNMCastDropEnable = _HwLswSysUNMCastDropEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 6),
    _HwLswSysUNMCastDropEnable_Type()
)
hwLswSysUNMCastDropEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswSysUNMCastDropEnable.setStatus("current")


class _HwLswSysManagementVlan_Type(Integer32):
    """Custom type hwLswSysManagementVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwLswSysManagementVlan_Type.__name__ = "Integer32"
_HwLswSysManagementVlan_Object = MibScalar
hwLswSysManagementVlan = _HwLswSysManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 7),
    _HwLswSysManagementVlan_Type()
)
hwLswSysManagementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswSysManagementVlan.setStatus("current")


class _HwLswSysVlanRange_Type(DisplayString):
    """Custom type hwLswSysVlanRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_HwLswSysVlanRange_Type.__name__ = "DisplayString"
_HwLswSysVlanRange_Object = MibScalar
hwLswSysVlanRange = _HwLswSysVlanRange_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 8),
    _HwLswSysVlanRange_Type()
)
hwLswSysVlanRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswSysVlanRange.setStatus("current")
_HwLswSysManagementIpAddr_Type = IpAddress
_HwLswSysManagementIpAddr_Object = MibScalar
hwLswSysManagementIpAddr = _HwLswSysManagementIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 9),
    _HwLswSysManagementIpAddr_Type()
)
hwLswSysManagementIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswSysManagementIpAddr.setStatus("current")
_HwLswSysManagementIpMask_Type = IpAddress
_HwLswSysManagementIpMask_Object = MibScalar
hwLswSysManagementIpMask = _HwLswSysManagementIpMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 10),
    _HwLswSysManagementIpMask_Type()
)
hwLswSysManagementIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswSysManagementIpMask.setStatus("current")
_HwMacAddressCountPort_Type = Integer32
_HwMacAddressCountPort_Object = MibScalar
hwMacAddressCountPort = _HwMacAddressCountPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 11),
    _HwMacAddressCountPort_Type()
)
hwMacAddressCountPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAddressCountPort.setStatus("current")
_HwMacAddressCountMachine_Type = Integer32
_HwMacAddressCountMachine_Object = MibScalar
hwMacAddressCountMachine = _HwMacAddressCountMachine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 12),
    _HwMacAddressCountMachine_Type()
)
hwMacAddressCountMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAddressCountMachine.setStatus("current")
_HwLswSysPhyMemory_Type = Unsigned32
_HwLswSysPhyMemory_Object = MibScalar
hwLswSysPhyMemory = _HwLswSysPhyMemory_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 13),
    _HwLswSysPhyMemory_Type()
)
hwLswSysPhyMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSysPhyMemory.setStatus("current")
if mibBuilder.loadTexts:
    hwLswSysPhyMemory.setUnits("byte")
_HwLswSysMemory_Type = Unsigned32
_HwLswSysMemory_Object = MibScalar
hwLswSysMemory = _HwLswSysMemory_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 14),
    _HwLswSysMemory_Type()
)
hwLswSysMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSysMemory.setStatus("current")
if mibBuilder.loadTexts:
    hwLswSysMemory.setUnits("byte")
_HwLswSysMemoryUsed_Type = Unsigned32
_HwLswSysMemoryUsed_Object = MibScalar
hwLswSysMemoryUsed = _HwLswSysMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 15),
    _HwLswSysMemoryUsed_Type()
)
hwLswSysMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSysMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    hwLswSysMemoryUsed.setUnits("byte")


class _HwLswSysMemoryRatio_Type(Unsigned32):
    """Custom type hwLswSysMemoryRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwLswSysMemoryRatio_Type.__name__ = "Unsigned32"
_HwLswSysMemoryRatio_Object = MibScalar
hwLswSysMemoryRatio = _HwLswSysMemoryRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 16),
    _HwLswSysMemoryRatio_Type()
)
hwLswSysMemoryRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSysMemoryRatio.setStatus("current")
_HwLswSysTemperature_Type = Integer32
_HwLswSysTemperature_Object = MibScalar
hwLswSysTemperature = _HwLswSysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 1, 17),
    _HwLswSysTemperature_Type()
)
hwLswSysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSysTemperature.setStatus("current")
_HwLswSlotConf_ObjectIdentity = ObjectIdentity
hwLswSlotConf = _HwLswSlotConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4)
)
_HwLswFrameTable_Object = MibTable
hwLswFrameTable = _HwLswFrameTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 2)
)
if mibBuilder.loadTexts:
    hwLswFrameTable.setStatus("current")
_HwLswFrameEntry_Object = MibTableRow
hwLswFrameEntry = _HwLswFrameEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 2, 1)
)
hwLswFrameEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
)
if mibBuilder.loadTexts:
    hwLswFrameEntry.setStatus("current")
_HwLswFrameIndex_Type = Integer32
_HwLswFrameIndex_Object = MibTableColumn
hwLswFrameIndex = _HwLswFrameIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 2, 1, 1),
    _HwLswFrameIndex_Type()
)
hwLswFrameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswFrameIndex.setStatus("current")
_HwLswFrameType_Type = Integer32
_HwLswFrameType_Object = MibTableColumn
hwLswFrameType = _HwLswFrameType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 2, 1, 2),
    _HwLswFrameType_Type()
)
hwLswFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswFrameType.setStatus("current")


class _HwLswFrameDesc_Type(DisplayString):
    """Custom type hwLswFrameDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwLswFrameDesc_Type.__name__ = "DisplayString"
_HwLswFrameDesc_Object = MibTableColumn
hwLswFrameDesc = _HwLswFrameDesc_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 2, 1, 3),
    _HwLswFrameDesc_Type()
)
hwLswFrameDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswFrameDesc.setStatus("current")
_HwLswSlotNumber_Type = Integer32
_HwLswSlotNumber_Object = MibTableColumn
hwLswSlotNumber = _HwLswSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 2, 1, 4),
    _HwLswSlotNumber_Type()
)
hwLswSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSlotNumber.setStatus("current")


class _HwLswFrameAdminStatus_Type(Integer32):
    """Custom type hwLswFrameAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("normal", 1),
          ("other", 3))
    )


_HwLswFrameAdminStatus_Type.__name__ = "Integer32"
_HwLswFrameAdminStatus_Object = MibTableColumn
hwLswFrameAdminStatus = _HwLswFrameAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 2, 1, 5),
    _HwLswFrameAdminStatus_Type()
)
hwLswFrameAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswFrameAdminStatus.setStatus("current")
_HwLswSlotTable_Object = MibTable
hwLswSlotTable = _HwLswSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3)
)
if mibBuilder.loadTexts:
    hwLswSlotTable.setStatus("current")
_HwLswSlotEntry_Object = MibTableRow
hwLswSlotEntry = _HwLswSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1)
)
hwLswSlotEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
    (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"),
)
if mibBuilder.loadTexts:
    hwLswSlotEntry.setStatus("current")
_HwLswSlotIndex_Type = Integer32
_HwLswSlotIndex_Object = MibTableColumn
hwLswSlotIndex = _HwLswSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1, 1),
    _HwLswSlotIndex_Type()
)
hwLswSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSlotIndex.setStatus("current")
_HwLswSlotType_Type = HwLswTypeOfSlot
_HwLswSlotType_Object = MibTableColumn
hwLswSlotType = _HwLswSlotType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1, 2),
    _HwLswSlotType_Type()
)
hwLswSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSlotType.setStatus("current")


class _HwLswSlotDesc_Type(DisplayString):
    """Custom type hwLswSlotDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwLswSlotDesc_Type.__name__ = "DisplayString"
_HwLswSlotDesc_Object = MibTableColumn
hwLswSlotDesc = _HwLswSlotDesc_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1, 3),
    _HwLswSlotDesc_Type()
)
hwLswSlotDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswSlotDesc.setStatus("current")
_HwLswSlotCpuRatio_Type = Integer32
_HwLswSlotCpuRatio_Object = MibTableColumn
hwLswSlotCpuRatio = _HwLswSlotCpuRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1, 4),
    _HwLswSlotCpuRatio_Type()
)
hwLswSlotCpuRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSlotCpuRatio.setStatus("current")


class _HwLswSlotPcbVersion_Type(DisplayString):
    """Custom type hwLswSlotPcbVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwLswSlotPcbVersion_Type.__name__ = "DisplayString"
_HwLswSlotPcbVersion_Object = MibTableColumn
hwLswSlotPcbVersion = _HwLswSlotPcbVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1, 5),
    _HwLswSlotPcbVersion_Type()
)
hwLswSlotPcbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSlotPcbVersion.setStatus("current")


class _HwLswSlotSoftwareVersion_Type(DisplayString):
    """Custom type hwLswSlotSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwLswSlotSoftwareVersion_Type.__name__ = "DisplayString"
_HwLswSlotSoftwareVersion_Object = MibTableColumn
hwLswSlotSoftwareVersion = _HwLswSlotSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1, 6),
    _HwLswSlotSoftwareVersion_Type()
)
hwLswSlotSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSlotSoftwareVersion.setStatus("current")
_HwLswSubslotNumber_Type = Integer32
_HwLswSubslotNumber_Object = MibTableColumn
hwLswSubslotNumber = _HwLswSubslotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1, 7),
    _HwLswSubslotNumber_Type()
)
hwLswSubslotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSubslotNumber.setStatus("current")


class _HwLswSlotAdminStatus_Type(Integer32):
    """Custom type hwLswSlotAdminStatus based on Integer32"""
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
        *(("fault", 3),
          ("forbidden", 4),
          ("normal", 2),
          ("not-install", 1))
    )


_HwLswSlotAdminStatus_Type.__name__ = "Integer32"
_HwLswSlotAdminStatus_Object = MibTableColumn
hwLswSlotAdminStatus = _HwLswSlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1, 8),
    _HwLswSlotAdminStatus_Type()
)
hwLswSlotAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSlotAdminStatus.setStatus("current")


class _HwLswSlotOperStatus_Type(Integer32):
    """Custom type hwLswSlotOperStatus based on Integer32"""
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
        *(("disable", 1),
          ("enable", 2),
          ("reset", 3),
          ("test", 4))
    )


_HwLswSlotOperStatus_Type.__name__ = "Integer32"
_HwLswSlotOperStatus_Object = MibTableColumn
hwLswSlotOperStatus = _HwLswSlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1, 9),
    _HwLswSlotOperStatus_Type()
)
hwLswSlotOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswSlotOperStatus.setStatus("current")
_HwLswSlotPhyMemory_Type = Unsigned32
_HwLswSlotPhyMemory_Object = MibTableColumn
hwLswSlotPhyMemory = _HwLswSlotPhyMemory_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1, 10),
    _HwLswSlotPhyMemory_Type()
)
hwLswSlotPhyMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSlotPhyMemory.setStatus("current")
if mibBuilder.loadTexts:
    hwLswSlotPhyMemory.setUnits("byte")
_HwLswSlotMemory_Type = Unsigned32
_HwLswSlotMemory_Object = MibTableColumn
hwLswSlotMemory = _HwLswSlotMemory_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1, 11),
    _HwLswSlotMemory_Type()
)
hwLswSlotMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSlotMemory.setStatus("current")
if mibBuilder.loadTexts:
    hwLswSlotMemory.setUnits("byte")
_HwLswSlotMemoryUsed_Type = Unsigned32
_HwLswSlotMemoryUsed_Object = MibTableColumn
hwLswSlotMemoryUsed = _HwLswSlotMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1, 12),
    _HwLswSlotMemoryUsed_Type()
)
hwLswSlotMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSlotMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    hwLswSlotMemoryUsed.setUnits("byte")


class _HwLswSlotMemoryRatio_Type(Unsigned32):
    """Custom type hwLswSlotMemoryRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwLswSlotMemoryRatio_Type.__name__ = "Unsigned32"
_HwLswSlotMemoryRatio_Object = MibTableColumn
hwLswSlotMemoryRatio = _HwLswSlotMemoryRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1, 13),
    _HwLswSlotMemoryRatio_Type()
)
hwLswSlotMemoryRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSlotMemoryRatio.setStatus("current")
_HwLswSlotTemperature_Type = Integer32
_HwLswSlotTemperature_Object = MibTableColumn
hwLswSlotTemperature = _HwLswSlotTemperature_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 3, 1, 14),
    _HwLswSlotTemperature_Type()
)
hwLswSlotTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSlotTemperature.setStatus("current")
_HwLswSubslotTable_Object = MibTable
hwLswSubslotTable = _HwLswSubslotTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 4)
)
if mibBuilder.loadTexts:
    hwLswSubslotTable.setStatus("current")
_HwLswSubslotEntry_Object = MibTableRow
hwLswSubslotEntry = _HwLswSubslotEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 4, 1)
)
hwLswSubslotEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
    (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"),
    (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswSubslotIndex"),
)
if mibBuilder.loadTexts:
    hwLswSubslotEntry.setStatus("current")
_HwLswSubslotIndex_Type = Integer32
_HwLswSubslotIndex_Object = MibTableColumn
hwLswSubslotIndex = _HwLswSubslotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 4, 1, 1),
    _HwLswSubslotIndex_Type()
)
hwLswSubslotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSubslotIndex.setStatus("current")
_HwLswSubslotType_Type = HwLswTypeOfSlot
_HwLswSubslotType_Object = MibTableColumn
hwLswSubslotType = _HwLswSubslotType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 4, 1, 2),
    _HwLswSubslotType_Type()
)
hwLswSubslotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSubslotType.setStatus("current")
_HwLswSubslotPortNum_Type = Integer32
_HwLswSubslotPortNum_Object = MibTableColumn
hwLswSubslotPortNum = _HwLswSubslotPortNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 4, 1, 3),
    _HwLswSubslotPortNum_Type()
)
hwLswSubslotPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSubslotPortNum.setStatus("current")


class _HwLswSubslotAdminStatus_Type(Integer32):
    """Custom type hwLswSubslotAdminStatus based on Integer32"""
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
        *(("fault", 3),
          ("forbidden", 4),
          ("normal", 2),
          ("not-install", 1))
    )


_HwLswSubslotAdminStatus_Type.__name__ = "Integer32"
_HwLswSubslotAdminStatus_Object = MibTableColumn
hwLswSubslotAdminStatus = _HwLswSubslotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 4, 1, 4),
    _HwLswSubslotAdminStatus_Type()
)
hwLswSubslotAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSubslotAdminStatus.setStatus("current")
_HwLswSubslotFirstIfIndex_Type = Integer32
_HwLswSubslotFirstIfIndex_Object = MibTableColumn
hwLswSubslotFirstIfIndex = _HwLswSubslotFirstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 4, 1, 5),
    _HwLswSubslotFirstIfIndex_Type()
)
hwLswSubslotFirstIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswSubslotFirstIfIndex.setStatus("current")
_HwLswPortTable_Object = MibTable
hwLswPortTable = _HwLswPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 5)
)
if mibBuilder.loadTexts:
    hwLswPortTable.setStatus("current")
_HwLswPortEntry_Object = MibTableRow
hwLswPortEntry = _HwLswPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 5, 1)
)
hwLswPortEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
    (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"),
    (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswSubslotIndex"),
    (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswPortIndex"),
)
if mibBuilder.loadTexts:
    hwLswPortEntry.setStatus("current")
_HwLswPortIndex_Type = Integer32
_HwLswPortIndex_Object = MibTableColumn
hwLswPortIndex = _HwLswPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 5, 1, 1),
    _HwLswPortIndex_Type()
)
hwLswPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswPortIndex.setStatus("current")


class _HwLswPortType_Type(Integer32):
    """Custom type hwLswPortType based on Integer32"""
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
              212)
        )
    )
    namedValues = NamedValues(
        *(("type-100-1000-BASE-LX-SMF", 183),
          ("type-1000BASE-BIDI-SFP", 172),
          ("type-1000BASE-BX10-D-SFP", 142),
          ("type-1000BASE-BX10-U-SFP", 141),
          ("type-1000BASE-CWDM-SFP", 173),
          ("type-1000BASE-CX", 19),
          ("type-1000BASE-LONG-FX", 12),
          ("type-1000BASE-LONG-FX-LC", 21),
          ("type-1000BASE-LX-SFP", 45),
          ("type-1000BASE-LX-SM", 2),
          ("type-1000BASE-MM-SFP", 51),
          ("type-1000BASE-STK-SFP", 171),
          ("type-1000BASE-SX-MM", 3),
          ("type-1000BASE-SX-SFP", 44),
          ("type-1000BASE-T", 43),
          ("type-1000BASE-T-AN-SFP", 46),
          ("type-1000BASE-TX", 4),
          ("type-1000BASE-ZENITH-FX", 11),
          ("type-1000BASE-ZENITH-FX-LC", 20),
          ("type-1000BASE-ZX-SFP", 50),
          ("type-100BASE-BIDI-SFP", 174),
          ("type-100BASE-BX10-D-SFP", 140),
          ("type-100BASE-BX10-U-SFP", 139),
          ("type-100BASE-FX-BIDI", 138),
          ("type-100BASE-LX-SFP", 53),
          ("type-100BASE-MM-MTRJ", 73),
          ("type-100BASE-MM-SFP", 56),
          ("type-100BASE-SM-MTRJ", 72),
          ("type-100BASE-SX-SFP", 52),
          ("type-100BASE-T-AN-SFP", 54),
          ("type-100BASE-ZX-SFP", 55),
          ("type-100M-100BASE-TX", 7),
          ("type-100M-1310-BIDI", 180),
          ("type-100M-1550-BIDI", 179),
          ("type-100M-HUB", 8),
          ("type-100M-LONG-FX", 18),
          ("type-100M-MM-FX-LC", 25),
          ("type-100M-MM-FX-SC", 23),
          ("type-100M-MULTIMODE-FX", 6),
          ("type-100M-SINGLEMODE-FX", 5),
          ("type-100M-SM-FX-LC", 24),
          ("type-100M-SM-FX-SC", 22),
          ("type-10G-BASE-CX4", 97),
          ("type-10G-BASE-ER", 61),
          ("type-10G-BASE-EW", 65),
          ("type-10G-BASE-LW", 64),
          ("type-10G-BASE-LX4", 62),
          ("type-10G-BASE-SR", 60),
          ("type-10G-BASE-SW", 63),
          ("type-10G-ER-SM-LC", 68),
          ("type-10G-EW-SM-LC", 71),
          ("type-10G-LR-SM-LC", 66),
          ("type-10G-LW-SM-LC", 69),
          ("type-10G-SR-MM-LC", 67),
          ("type-10G-STACK", 150),
          ("type-10G-SW-MM-LC", 70),
          ("type-10G-ZR-SM-LC", 185),
          ("type-10G-ZW-SM-LC", 184),
          ("type-10GBASE-CX4", 49),
          ("type-10GBASE-LR-SM", 15),
          ("type-10GBASE-LR-XENPAK", 48),
          ("type-10GBASE-LX4-MM", 16),
          ("type-10GBASE-LX4-SM", 17),
          ("type-10GBASE-LX4-XENPAK", 47),
          ("type-10GBASE-ZR", 148),
          ("type-10GBase-T", 210),
          ("type-10OR100M", 1),
          ("type-10OR100M-db", 14),
          ("type-155-ATM-LX-SMF", 152),
          ("type-155-ATM-NO-CONNECTOR", 155),
          ("type-155-ATM-SX-MMF", 151),
          ("type-155-CPOS-E1-LX-SMF", 163),
          ("type-155-CPOS-E1-NO-CONNECTOR", 157),
          ("type-155-CPOS-E1-SX-MMF", 161),
          ("type-155-CPOS-T1-LX-SMF", 164),
          ("type-155-CPOS-T1-NO-CONNECTOR", 158),
          ("type-155-CPOS-T1-SX-MMF", 162),
          ("type-155-POS-LX-SMF", 42),
          ("type-155-POS-SX-MMF", 41),
          ("type-24G-CASCADE", 100),
          ("type-622-ATM-LX-SMF", 154),
          ("type-622-ATM-NO-CONNECTOR", 156),
          ("type-622-ATM-SX-MMF", 153),
          ("type-622-CPOS-E1-LX-SMF", 167),
          ("type-622-CPOS-E1-NO-CONNECTOR", 159),
          ("type-622-CPOS-E1-SX-MMF", 165),
          ("type-622-CPOS-T1-LX-SMF", 168),
          ("type-622-CPOS-T1-NO-CONNECTOR", 160),
          ("type-622-CPOS-T1-SX-MMF", 166),
          ("type-ADSL", 13),
          ("type-CFP-40GBASE-LR4", 212),
          ("type-CFP-NO-CONNECTOR", 211),
          ("type-COMBO-1000-BASE-LX", 32),
          ("type-COMBO-1000-BASE-LX-COPPER", 34),
          ("type-COMBO-1000-BASE-LX-FIBER", 33),
          ("type-COMBO-1000-BASE-SX", 35),
          ("type-COMBO-1000-BASE-SX-COPPER", 37),
          ("type-COMBO-1000-BASE-SX-FIBER", 36),
          ("type-COMBO-1000-BASE-ZX", 38),
          ("type-COMBO-1000-BASE-ZX-COPPER", 40),
          ("type-COMBO-1000-BASE-ZX-FIBER", 39),
          ("type-COMBO-NO-CONNECTOR", 31),
          ("type-E1-CONNECTOR", 169),
          ("type-GBIC-1000-BASE-LX", 28),
          ("type-GBIC-1000-BASE-SX", 29),
          ("type-GBIC-1000-BASE-T", 27),
          ("type-GBIC-1000-BASE-ZX", 30),
          ("type-GBIC-NO-CONNECTOR", 26),
          ("type-MINISAS-HD-STACK-CONNECTOR", 199),
          ("type-NULL", 0),
          ("type-OLT-1000BASE-BX-SFF-SC", 98),
          ("type-OLT-1000BASE-NO-CONNECTOR", 176),
          ("type-OLT-1000BASE-PX-SFP", 175),
          ("type-ONU-1000BASE-BX-SFF-SC", 99),
          ("type-ONU-1000BASE-PX-SFF", 200),
          ("type-POS-I-64-1", 125),
          ("type-POS-I-64-2", 126),
          ("type-POS-I-64-3", 127),
          ("type-POS-I-64-5", 128),
          ("type-POS-L-64-1", 133),
          ("type-POS-L-64-2", 134),
          ("type-POS-L-64-3", 135),
          ("type-POS-L-64-4", 198),
          ("type-POS-NO-CONNECTOR", 59),
          ("type-POS-OC12-IR-1-SM", 111),
          ("type-POS-OC12-IR-2-SM", 112),
          ("type-POS-OC12-IR-SM", 110),
          ("type-POS-OC12-LR-1-SM", 114),
          ("type-POS-OC12-LR-2-SM", 115),
          ("type-POS-OC12-LR-3-SM", 116),
          ("type-POS-OC12-LR-SM", 113),
          ("type-POS-OC12-SR-MM", 109),
          ("type-POS-OC3-IR-1-SM", 103),
          ("type-POS-OC3-IR-2-SM", 104),
          ("type-POS-OC3-IR-SM", 102),
          ("type-POS-OC3-LR-1-SM", 106),
          ("type-POS-OC3-LR-2-SM", 107),
          ("type-POS-OC3-LR-3-SM", 108),
          ("type-POS-OC3-LR-SM", 105),
          ("type-POS-OC3-SR-MM", 101),
          ("type-POS-OC48-IR-1-SM", 119),
          ("type-POS-OC48-IR-2-SM", 120),
          ("type-POS-OC48-IR-SM", 118),
          ("type-POS-OC48-IR-SM-LC", 95),
          ("type-POS-OC48-LR-1-SM", 122),
          ("type-POS-OC48-LR-2-SM", 123),
          ("type-POS-OC48-LR-3-SM", 124),
          ("type-POS-OC48-LR-SM", 121),
          ("type-POS-OC48-LR-SM-LC", 96),
          ("type-POS-OC48-SR-SM", 117),
          ("type-POS-OC48-SR-SM-LC", 94),
          ("type-POS-S-64-1", 129),
          ("type-POS-S-64-2", 130),
          ("type-POS-S-64-3", 131),
          ("type-POS-S-64-5", 132),
          ("type-POS-V-64-2", 136),
          ("type-POS-V-64-3", 137),
          ("type-QSFP-NO-CONNECTOR", 209),
          ("type-QSFP-PLUS-40GBASE-SR4", 205),
          ("type-QSFP-PLUS-STACK-CONNECTOR", 206),
          ("type-QSFP-PLUS-TO-4SFP-PLUS-STACK-CONNECTOR", 207),
          ("type-RPR-LOGIC10GE-CONNECTOR", 147),
          ("type-RPR-LOGICGE-CONNECTOR", 178),
          ("type-RPR-LOGICOC48-CONNECTOR", 182),
          ("type-RPR-LOGICPOS-CONNECTOR", 146),
          ("type-RPR-PHY10GE-CONNECTOR", 145),
          ("type-RPR-PHYGE-CONNECTOR", 177),
          ("type-RPR-PHYOC48-CONNECTOR", 181),
          ("type-RPR-PHYPOS-CONNECTOR", 144),
          ("type-RS485", 201),
          ("type-SFP-NO-CONNECTOR", 57),
          ("type-SFP-PLUS-10GBASE-Cu", 195),
          ("type-SFP-PLUS-10GBASE-ER", 202),
          ("type-SFP-PLUS-10GBASE-LR", 193),
          ("type-SFP-PLUS-10GBASE-LRM", 194),
          ("type-SFP-PLUS-10GBASE-SR", 192),
          ("type-SFP-PLUS-10GBASE-ZR", 203),
          ("type-SFP-PLUS-NO-CONNECTOR", 191),
          ("type-SFP-PLUS-STACK-CONNECTOR", 197),
          ("type-SFP-PLUS-UNKNOWN", 196),
          ("type-SFP-STACK-CONNECTOR", 208),
          ("type-SFP-UNKNOWN-CONNECTOR", 58),
          ("type-SGMII-100-BASE-FX-SFP", 188),
          ("type-SGMII-100-BASE-LX-SFP", 187),
          ("type-STACK", 10),
          ("type-STK-1000BASE-T", 143),
          ("type-T1-CONNECTOR", 170),
          ("type-TYPE-ERROR-CONNECTOR", 149),
          ("type-VDSL", 9),
          ("type-WLAN-RADIO", 189),
          ("type-XFP-10GBASE-CX4", 81),
          ("type-XFP-10GBASE-ER", 77),
          ("type-XFP-10GBASE-EW", 80),
          ("type-XFP-10GBASE-LR", 76),
          ("type-XFP-10GBASE-LW", 79),
          ("type-XFP-10GBASE-LX4", 82),
          ("type-XFP-10GBASE-SR", 75),
          ("type-XFP-10GBASE-SW", 78),
          ("type-XFP-10GBASE-ZR", 204),
          ("type-XFP-NO-CONNECTOR", 74),
          ("type-XFP-UNKNOWN", 83),
          ("type-XPK-10GBASE-CX4", 91),
          ("type-XPK-10GBASE-ER", 87),
          ("type-XPK-10GBASE-EW", 90),
          ("type-XPK-10GBASE-LR", 86),
          ("type-XPK-10GBASE-LW", 89),
          ("type-XPK-10GBASE-LX4", 92),
          ("type-XPK-10GBASE-SR", 85),
          ("type-XPK-10GBASE-SW", 88),
          ("type-XPK-10GBASE-ZR", 186),
          ("type-XPK-NOCONNECTOR", 84),
          ("type-XPK-UNKNOWN", 93))
    )


_HwLswPortType_Type.__name__ = "Integer32"
_HwLswPortType_Object = MibTableColumn
hwLswPortType = _HwLswPortType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 5, 1, 2),
    _HwLswPortType_Type()
)
hwLswPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswPortType.setStatus("current")
_HwLswPortIfindex_Type = Integer32
_HwLswPortIfindex_Object = MibTableColumn
hwLswPortIfindex = _HwLswPortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 5, 1, 3),
    _HwLswPortIfindex_Type()
)
hwLswPortIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswPortIfindex.setStatus("current")


class _HwLswPortIsPlugged_Type(Integer32):
    """Custom type hwLswPortIsPlugged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("plugged", 1),
          ("unplugged", 0))
    )


_HwLswPortIsPlugged_Type.__name__ = "Integer32"
_HwLswPortIsPlugged_Object = MibTableColumn
hwLswPortIsPlugged = _HwLswPortIsPlugged_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 5, 1, 4),
    _HwLswPortIsPlugged_Type()
)
hwLswPortIsPlugged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswPortIsPlugged.setStatus("current")
_HwLswPortLoopbackTable_Object = MibTable
hwLswPortLoopbackTable = _HwLswPortLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 6)
)
if mibBuilder.loadTexts:
    hwLswPortLoopbackTable.setStatus("current")
_HwLswPortLoopbackEntry_Object = MibTableRow
hwLswPortLoopbackEntry = _HwLswPortLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 6, 1)
)
if mibBuilder.loadTexts:
    hwLswPortLoopbackEntry.setStatus("current")


class _HwLswPortLoopbackIsSupport_Type(Integer32):
    """Custom type hwLswPortLoopbackIsSupport based on Integer32"""
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
        *(("both", 2),
          ("externalOnly", 4),
          ("internalOnly", 3),
          ("neither", 1))
    )


_HwLswPortLoopbackIsSupport_Type.__name__ = "Integer32"
_HwLswPortLoopbackIsSupport_Object = MibTableColumn
hwLswPortLoopbackIsSupport = _HwLswPortLoopbackIsSupport_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 6, 1, 1),
    _HwLswPortLoopbackIsSupport_Type()
)
hwLswPortLoopbackIsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswPortLoopbackIsSupport.setStatus("current")


class _HwLswPortLoopbackOperate_Type(Integer32):
    """Custom type hwLswPortLoopbackOperate based on Integer32"""
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
        *(("externalLoopback", 2),
          ("internalLoopback", 1),
          ("localLoopback", 4),
          ("remoteLoopback", 3),
          ("stopRemoteOrLocalLoopBack", 0))
    )


_HwLswPortLoopbackOperate_Type.__name__ = "Integer32"
_HwLswPortLoopbackOperate_Object = MibTableColumn
hwLswPortLoopbackOperate = _HwLswPortLoopbackOperate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 6, 1, 2),
    _HwLswPortLoopbackOperate_Type()
)
hwLswPortLoopbackOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswPortLoopbackOperate.setStatus("current")


class _HwLswPortLoopbackResult_Type(Integer32):
    """Custom type hwLswPortLoopbackResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("testfailed", 2),
          ("testing", 0),
          ("testok", 1))
    )


_HwLswPortLoopbackResult_Type.__name__ = "Integer32"
_HwLswPortLoopbackResult_Object = MibTableColumn
hwLswPortLoopbackResult = _HwLswPortLoopbackResult_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 6, 1, 3),
    _HwLswPortLoopbackResult_Type()
)
hwLswPortLoopbackResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswPortLoopbackResult.setStatus("current")


class _HwLswPortLoopbackAutoStopSupport_Type(Integer32):
    """Custom type hwLswPortLoopbackAutoStopSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupport", 2),
          ("support", 1))
    )


_HwLswPortLoopbackAutoStopSupport_Type.__name__ = "Integer32"
_HwLswPortLoopbackAutoStopSupport_Object = MibTableColumn
hwLswPortLoopbackAutoStopSupport = _HwLswPortLoopbackAutoStopSupport_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 6, 1, 4),
    _HwLswPortLoopbackAutoStopSupport_Type()
)
hwLswPortLoopbackAutoStopSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswPortLoopbackAutoStopSupport.setStatus("current")


class _HwLswPortLoopbackRemoteResult_Type(Integer32):
    """Custom type hwLswPortLoopbackRemoteResult based on Integer32"""
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
        *(("loopbackTestFailed", 3),
          ("loopbackTestInit", 0),
          ("loopbackTestSuccessed", 2),
          ("loopbackTestTestAndFailed", 4),
          ("loopbackTesting", 1))
    )


_HwLswPortLoopbackRemoteResult_Type.__name__ = "Integer32"
_HwLswPortLoopbackRemoteResult_Object = MibTableColumn
hwLswPortLoopbackRemoteResult = _HwLswPortLoopbackRemoteResult_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 6, 1, 5),
    _HwLswPortLoopbackRemoteResult_Type()
)
hwLswPortLoopbackRemoteResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswPortLoopbackRemoteResult.setStatus("current")


class _HwLswPortLoopbackLocalResult_Type(Integer32):
    """Custom type hwLswPortLoopbackLocalResult based on Integer32"""
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
        *(("loopbackTestFailed", 3),
          ("loopbackTestInit", 0),
          ("loopbackTestSuccessed", 2),
          ("loopbackTestTestAndFailed", 4),
          ("loopbackTesting", 1))
    )


_HwLswPortLoopbackLocalResult_Type.__name__ = "Integer32"
_HwLswPortLoopbackLocalResult_Object = MibTableColumn
hwLswPortLoopbackLocalResult = _HwLswPortLoopbackLocalResult_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 6, 1, 6),
    _HwLswPortLoopbackLocalResult_Type()
)
hwLswPortLoopbackLocalResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswPortLoopbackLocalResult.setStatus("current")


class _HwLswPortLoopbackInternalResult_Type(Integer32):
    """Custom type hwLswPortLoopbackInternalResult based on Integer32"""
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
        *(("loopbackTestFailed", 3),
          ("loopbackTestInit", 0),
          ("loopbackTestSuccessed", 2),
          ("loopbackTestTestAndFailed", 4),
          ("loopbackTesting", 1))
    )


_HwLswPortLoopbackInternalResult_Type.__name__ = "Integer32"
_HwLswPortLoopbackInternalResult_Object = MibTableColumn
hwLswPortLoopbackInternalResult = _HwLswPortLoopbackInternalResult_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 6, 1, 7),
    _HwLswPortLoopbackInternalResult_Type()
)
hwLswPortLoopbackInternalResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswPortLoopbackInternalResult.setStatus("current")


class _HwLswPortLoopbackExternalResult_Type(Integer32):
    """Custom type hwLswPortLoopbackExternalResult based on Integer32"""
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
        *(("loopbackTestFailed", 3),
          ("loopbackTestInit", 0),
          ("loopbackTestSuccessed", 2),
          ("loopbackTestTestAndFailed", 4),
          ("loopbackTesting", 1))
    )


_HwLswPortLoopbackExternalResult_Type.__name__ = "Integer32"
_HwLswPortLoopbackExternalResult_Object = MibTableColumn
hwLswPortLoopbackExternalResult = _HwLswPortLoopbackExternalResult_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 6, 1, 8),
    _HwLswPortLoopbackExternalResult_Type()
)
hwLswPortLoopbackExternalResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswPortLoopbackExternalResult.setStatus("current")
_HwLswFabricTable_Object = MibTable
hwLswFabricTable = _HwLswFabricTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 7)
)
if mibBuilder.loadTexts:
    hwLswFabricTable.setStatus("current")
_HwLswFabricEntry_Object = MibTableRow
hwLswFabricEntry = _HwLswFabricEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 7, 1)
)
hwLswFabricEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
    (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"),
    (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswSubslotIndex"),
    (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswFabricChannelIndex"),
)
if mibBuilder.loadTexts:
    hwLswFabricEntry.setStatus("current")
_HwLswFabricChannelIndex_Type = Integer32
_HwLswFabricChannelIndex_Object = MibTableColumn
hwLswFabricChannelIndex = _HwLswFabricChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 7, 1, 1),
    _HwLswFabricChannelIndex_Type()
)
hwLswFabricChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLswFabricChannelIndex.setStatus("current")


class _HwLswFabricUtilIn_Type(Integer32):
    """Custom type hwLswFabricUtilIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwLswFabricUtilIn_Type.__name__ = "Integer32"
_HwLswFabricUtilIn_Object = MibTableColumn
hwLswFabricUtilIn = _HwLswFabricUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 7, 1, 2),
    _HwLswFabricUtilIn_Type()
)
hwLswFabricUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswFabricUtilIn.setStatus("current")
if mibBuilder.loadTexts:
    hwLswFabricUtilIn.setUnits("one percent")


class _HwLswFabricUtilOut_Type(Integer32):
    """Custom type hwLswFabricUtilOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwLswFabricUtilOut_Type.__name__ = "Integer32"
_HwLswFabricUtilOut_Object = MibTableColumn
hwLswFabricUtilOut = _HwLswFabricUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 7, 1, 3),
    _HwLswFabricUtilOut_Type()
)
hwLswFabricUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswFabricUtilOut.setStatus("current")
if mibBuilder.loadTexts:
    hwLswFabricUtilOut.setUnits("one percent")


class _HwLswFabricPeakIn_Type(Integer32):
    """Custom type hwLswFabricPeakIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwLswFabricPeakIn_Type.__name__ = "Integer32"
_HwLswFabricPeakIn_Object = MibTableColumn
hwLswFabricPeakIn = _HwLswFabricPeakIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 7, 1, 4),
    _HwLswFabricPeakIn_Type()
)
hwLswFabricPeakIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswFabricPeakIn.setStatus("current")
if mibBuilder.loadTexts:
    hwLswFabricPeakIn.setUnits("one percent")
_HwLswFabricPeakInTime_Type = DateAndTime
_HwLswFabricPeakInTime_Object = MibTableColumn
hwLswFabricPeakInTime = _HwLswFabricPeakInTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 7, 1, 5),
    _HwLswFabricPeakInTime_Type()
)
hwLswFabricPeakInTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswFabricPeakInTime.setStatus("current")


class _HwLswFabricPeakOut_Type(Integer32):
    """Custom type hwLswFabricPeakOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwLswFabricPeakOut_Type.__name__ = "Integer32"
_HwLswFabricPeakOut_Object = MibTableColumn
hwLswFabricPeakOut = _HwLswFabricPeakOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 7, 1, 6),
    _HwLswFabricPeakOut_Type()
)
hwLswFabricPeakOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswFabricPeakOut.setStatus("current")
if mibBuilder.loadTexts:
    hwLswFabricPeakOut.setUnits("one percent")
_HwLswFabricPeakOutTime_Type = DateAndTime
_HwLswFabricPeakOutTime_Object = MibTableColumn
hwLswFabricPeakOutTime = _HwLswFabricPeakOutTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 18, 4, 7, 1, 7),
    _HwLswFabricPeakOutTime_Type()
)
hwLswFabricPeakOutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswFabricPeakOutTime.setStatus("current")
hwLswPortEntry.registerAugmentions(
    ("A3COM-HUAWEI-DEVICE-MIB",
     "hwLswPortLoopbackEntry")
)
hwLswPortLoopbackEntry.setIndexNames(*hwLswPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DEVICE-MIB",
    **{"HwLswTypeOfSlot": HwLswTypeOfSlot,
       "hwLswDeviceAdmin": hwLswDeviceAdmin,
       "hwLswSystemPara": hwLswSystemPara,
       "hwLswSysIpAddr": hwLswSysIpAddr,
       "hwLswSysIpMask": hwLswSysIpMask,
       "hwLswSysCpuRatio": hwLswSysCpuRatio,
       "hwLswSysVersion": hwLswSysVersion,
       "hwLswSysTime": hwLswSysTime,
       "hwLswSysUNMCastDropEnable": hwLswSysUNMCastDropEnable,
       "hwLswSysManagementVlan": hwLswSysManagementVlan,
       "hwLswSysVlanRange": hwLswSysVlanRange,
       "hwLswSysManagementIpAddr": hwLswSysManagementIpAddr,
       "hwLswSysManagementIpMask": hwLswSysManagementIpMask,
       "hwMacAddressCountPort": hwMacAddressCountPort,
       "hwMacAddressCountMachine": hwMacAddressCountMachine,
       "hwLswSysPhyMemory": hwLswSysPhyMemory,
       "hwLswSysMemory": hwLswSysMemory,
       "hwLswSysMemoryUsed": hwLswSysMemoryUsed,
       "hwLswSysMemoryRatio": hwLswSysMemoryRatio,
       "hwLswSysTemperature": hwLswSysTemperature,
       "hwLswSlotConf": hwLswSlotConf,
       "hwLswFrameTable": hwLswFrameTable,
       "hwLswFrameEntry": hwLswFrameEntry,
       "hwLswFrameIndex": hwLswFrameIndex,
       "hwLswFrameType": hwLswFrameType,
       "hwLswFrameDesc": hwLswFrameDesc,
       "hwLswSlotNumber": hwLswSlotNumber,
       "hwLswFrameAdminStatus": hwLswFrameAdminStatus,
       "hwLswSlotTable": hwLswSlotTable,
       "hwLswSlotEntry": hwLswSlotEntry,
       "hwLswSlotIndex": hwLswSlotIndex,
       "hwLswSlotType": hwLswSlotType,
       "hwLswSlotDesc": hwLswSlotDesc,
       "hwLswSlotCpuRatio": hwLswSlotCpuRatio,
       "hwLswSlotPcbVersion": hwLswSlotPcbVersion,
       "hwLswSlotSoftwareVersion": hwLswSlotSoftwareVersion,
       "hwLswSubslotNumber": hwLswSubslotNumber,
       "hwLswSlotAdminStatus": hwLswSlotAdminStatus,
       "hwLswSlotOperStatus": hwLswSlotOperStatus,
       "hwLswSlotPhyMemory": hwLswSlotPhyMemory,
       "hwLswSlotMemory": hwLswSlotMemory,
       "hwLswSlotMemoryUsed": hwLswSlotMemoryUsed,
       "hwLswSlotMemoryRatio": hwLswSlotMemoryRatio,
       "hwLswSlotTemperature": hwLswSlotTemperature,
       "hwLswSubslotTable": hwLswSubslotTable,
       "hwLswSubslotEntry": hwLswSubslotEntry,
       "hwLswSubslotIndex": hwLswSubslotIndex,
       "hwLswSubslotType": hwLswSubslotType,
       "hwLswSubslotPortNum": hwLswSubslotPortNum,
       "hwLswSubslotAdminStatus": hwLswSubslotAdminStatus,
       "hwLswSubslotFirstIfIndex": hwLswSubslotFirstIfIndex,
       "hwLswPortTable": hwLswPortTable,
       "hwLswPortEntry": hwLswPortEntry,
       "hwLswPortIndex": hwLswPortIndex,
       "hwLswPortType": hwLswPortType,
       "hwLswPortIfindex": hwLswPortIfindex,
       "hwLswPortIsPlugged": hwLswPortIsPlugged,
       "hwLswPortLoopbackTable": hwLswPortLoopbackTable,
       "hwLswPortLoopbackEntry": hwLswPortLoopbackEntry,
       "hwLswPortLoopbackIsSupport": hwLswPortLoopbackIsSupport,
       "hwLswPortLoopbackOperate": hwLswPortLoopbackOperate,
       "hwLswPortLoopbackResult": hwLswPortLoopbackResult,
       "hwLswPortLoopbackAutoStopSupport": hwLswPortLoopbackAutoStopSupport,
       "hwLswPortLoopbackRemoteResult": hwLswPortLoopbackRemoteResult,
       "hwLswPortLoopbackLocalResult": hwLswPortLoopbackLocalResult,
       "hwLswPortLoopbackInternalResult": hwLswPortLoopbackInternalResult,
       "hwLswPortLoopbackExternalResult": hwLswPortLoopbackExternalResult,
       "hwLswFabricTable": hwLswFabricTable,
       "hwLswFabricEntry": hwLswFabricEntry,
       "hwLswFabricChannelIndex": hwLswFabricChannelIndex,
       "hwLswFabricUtilIn": hwLswFabricUtilIn,
       "hwLswFabricUtilOut": hwLswFabricUtilOut,
       "hwLswFabricPeakIn": hwLswFabricPeakIn,
       "hwLswFabricPeakInTime": hwLswFabricPeakInTime,
       "hwLswFabricPeakOut": hwLswFabricPeakOut,
       "hwLswFabricPeakOutTime": hwLswFabricPeakOutTime}
)
