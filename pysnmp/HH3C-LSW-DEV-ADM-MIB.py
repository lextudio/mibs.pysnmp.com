# SNMP MIB module (HH3C-LSW-DEV-ADM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LSW-DEV-ADM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:09 2024
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

(hh3clswCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3clswCommon")

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

hh3cLswDeviceAdmin = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18)
)
hh3cLswDeviceAdmin.setRevisions(
        ("2001-04-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cLswTypeOfSlot(Integer32, TextualConvention):
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
              733,
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
              958,
              959,
              960,
              961,
              962,
              963,
              964,
              965,
              966,
              967,
              968,
              969,
              970,
              971,
              972,
              973,
              974,
              976,
              977,
              978,
              979,
              980,
              981,
              982,
              983,
              984,
              985,
              986,
              987,
              988,
              989,
              990,
              991,
              992,
              993,
              994,
              995,
              996,
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
              1230,
              1231,
              1232,
              1233,
              1234,
              1235,
              1236,
              1237,
              1238,
              1239,
              1240,
              1241,
              1242,
              1243,
              1244,
              1245,
              1246,
              1247,
              1248,
              1249,
              1250,
              1251,
              1252,
              1253,
              1254,
              1255,
              1400,
              1401,
              1402,
              1403,
              1404,
              1405,
              1406,
              1407,
              1408,
              1409,
              1410)
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
          ("type-CR-IM-LB1A", 959),
          ("type-CR-IM-MAC1A", 965),
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
          ("type-EWPX3WCMD0", 1215),
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
          ("type-LSPM1XGT2P", 733),
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
          ("type-LSQ1GP48SA0", 1232),
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
          ("type-LSQ1TGX2SA0", 1233),
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
          ("type-LST1CP4RFD1", 970),
          ("type-LST1CP4RFD2", 987),
          ("type-LST1CP4RFG1", 971),
          ("type-LST1CP4RFG2", 988),
          ("type-LST1FW2A1", 473),
          ("type-LST1FW3A1", 941),
          ("type-LST1GP48LEA1", 906),
          ("type-LST1GP48LEB1", 436),
          ("type-LST1GP48LEC1", 413),
          ("type-LST1GP48LEC2", 961),
          ("type-LST1GP48LEF1", 467),
          ("type-LST1GP48LEY1", 909),
          ("type-LST1GP48LEZ1", 912),
          ("type-LST1GT48LEA1", 905),
          ("type-LST1GT48LEB1", 435),
          ("type-LST1GT48LEC1", 412),
          ("type-LST1GT48LEC2", 960),
          ("type-LST1GT48LEY1", 908),
          ("type-LST1IPS1A1", 477),
          ("type-LST1IPS2A1", 996),
          ("type-LST1LB1A1", 475),
          ("type-LST1MRPNC1", 409),
          ("type-LST1MRPNE1", 974),
          ("type-LST1NSM1A1", 474),
          ("type-LST1SF08B1", 411),
          ("type-LST1SF08C1", 498),
          ("type-LST1SF08E1", 972),
          ("type-LST1SF18B1", 410),
          ("type-LST1SF18C1", 499),
          ("type-LST1SF18E1", 973),
          ("type-LST1XLP16RFD1", 969),
          ("type-LST1XLP16RFD2", 986),
          ("type-LST1XP16LEB1", 928),
          ("type-LST1XP16LEC1", 929),
          ("type-LST1XP16LEC2", 962),
          ("type-LST1XP16LEY1", 948),
          ("type-LST1XP32REB1", 439),
          ("type-LST1XP32REC1", 440),
          ("type-LST1XP32REY1", 910),
          ("type-LST1XP40RFD1", 967),
          ("type-LST1XP40RFD2", 984),
          ("type-LST1XP40RFG1", 968),
          ("type-LST1XP40RFG2", 985),
          ("type-LST1XP48LFD1", 966),
          ("type-LST1XP48LFD2", 983),
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
          ("type-LST2XP32REC2", 964),
          ("type-LST2XP32REY1", 947),
          ("type-LST2XP4LEB1", 923),
          ("type-LST2XP4LEC1", 924),
          ("type-LST2XP8LEA1", 907),
          ("type-LST2XP8LEB1", 920),
          ("type-LST2XP8LEC1", 921),
          ("type-LST2XP8LEC2", 963),
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
          ("type-LSU1FAB08D9", 1254),
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
          ("type-LSU1QGS4SF9", 1251),
          ("type-LSU1QGS8SF0", 1202),
          ("type-LSU1QGS8SF9", 1250),
          ("type-LSU1SUPA0", 673),
          ("type-LSU1SUPB0", 1231),
          ("type-LSU1SUPB9", 1255),
          ("type-LSU1TGS32SF0", 1205),
          ("type-LSU1TGS32SF9", 1253),
          ("type-LSU1TGS48SF0", 1203),
          ("type-LSU1TGS48SF9", 1252),
          ("type-LSU1TGS8EA0", 669),
          ("type-LSU1TGS8EB0", 670),
          ("type-LSU1TGS8SE0", 671),
          ("type-LSU1TGT24SF0", 1218),
          ("type-LSU1TGT24SF9", 1249),
          ("type-LSU1TGX4EA0", 682),
          ("type-LSU1TGX4EB0", 683),
          ("type-LSU1TGX4SE0", 684),
          ("type-LSU3WCMD0", 1214),
          ("type-LSUTGS16SC0", 672),
          ("type-LSV1MPUA", 1236),
          ("type-LSV1QGS12SA", 1235),
          ("type-LSV1SRPUA", 1234),
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
          ("type-LSX1CGX8FB0", 976),
          ("type-LSX1FAB10B0", 1241),
          ("type-LSX1FAB10B1", 1243),
          ("type-LSX1FAB16B0", 1242),
          ("type-LSX1FAB16B1", 1244),
          ("type-LSX1QGS16EA0", 1245),
          ("type-LSX1QGS16EA1", 1247),
          ("type-LSX1QGS24FB0", 977),
          ("type-LSX1QGS24FB1", 978),
          ("type-LSX1SUP10A0", 1237),
          ("type-LSX1SUP10A1", 1239),
          ("type-LSX1SUP16A0", 1238),
          ("type-LSX1SUP16A1", 1240),
          ("type-LSX1TGS24FB0", 979),
          ("type-LSX1TGS24FB1", 980),
          ("type-LSX1TGS48EA0", 1246),
          ("type-LSX1TGS48EA1", 1248),
          ("type-LSX1TGS48FB0", 981),
          ("type-LSX1TGS48FB1", 982),
          ("type-LSXK1P", 168),
          ("type-LSXP2P", 169),
          ("type-MIC-CLP2L", 995),
          ("type-MIC-CLP4L", 994),
          ("type-MIC-ET16L", 993),
          ("type-MIC-GP4L", 990),
          ("type-MIC-GP8L", 991),
          ("type-MIC-SP4L", 992),
          ("type-MPE-1004", 989),
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
          ("type-RPU-5120-28SC-HI", 1400),
          ("type-RPU-5120-34C-HI", 1402),
          ("type-RPU-5120-52SC-HI", 1401),
          ("type-RPU-5120-58C-HI", 1403),
          ("type-RPU-5500-34C-HI", 1404),
          ("type-RPU-5500-34C-HI-D", 1406),
          ("type-RPU-5500-58C-HI", 1405),
          ("type-RPU-5500-58C-HI-D", 1407),
          ("type-RPU-5820V2-52Q", 1408),
          ("type-RPU-5820V2-52QF", 1409),
          ("type-RPU-5820V2-52QS-GE", 1410),
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
          ("type-SPC-XP16R", 958),
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

_Hh3cLswSystemPara_ObjectIdentity = ObjectIdentity
hh3cLswSystemPara = _Hh3cLswSystemPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1)
)
_Hh3cLswSysIpAddr_Type = IpAddress
_Hh3cLswSysIpAddr_Object = MibScalar
hh3cLswSysIpAddr = _Hh3cLswSysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 1),
    _Hh3cLswSysIpAddr_Type()
)
hh3cLswSysIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSysIpAddr.setStatus("current")
_Hh3cLswSysIpMask_Type = IpAddress
_Hh3cLswSysIpMask_Object = MibScalar
hh3cLswSysIpMask = _Hh3cLswSysIpMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 2),
    _Hh3cLswSysIpMask_Type()
)
hh3cLswSysIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSysIpMask.setStatus("current")


class _Hh3cLswSysCpuRatio_Type(Integer32):
    """Custom type hh3cLswSysCpuRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cLswSysCpuRatio_Type.__name__ = "Integer32"
_Hh3cLswSysCpuRatio_Object = MibScalar
hh3cLswSysCpuRatio = _Hh3cLswSysCpuRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 3),
    _Hh3cLswSysCpuRatio_Type()
)
hh3cLswSysCpuRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSysCpuRatio.setStatus("current")


class _Hh3cLswSysVersion_Type(DisplayString):
    """Custom type hh3cLswSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cLswSysVersion_Type.__name__ = "DisplayString"
_Hh3cLswSysVersion_Object = MibScalar
hh3cLswSysVersion = _Hh3cLswSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 4),
    _Hh3cLswSysVersion_Type()
)
hh3cLswSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSysVersion.setStatus("current")
_Hh3cLswSysTime_Type = DateAndTime
_Hh3cLswSysTime_Object = MibScalar
hh3cLswSysTime = _Hh3cLswSysTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 5),
    _Hh3cLswSysTime_Type()
)
hh3cLswSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswSysTime.setStatus("current")


class _Hh3cLswSysUNMCastDropEnable_Type(Integer32):
    """Custom type hh3cLswSysUNMCastDropEnable based on Integer32"""
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


_Hh3cLswSysUNMCastDropEnable_Type.__name__ = "Integer32"
_Hh3cLswSysUNMCastDropEnable_Object = MibScalar
hh3cLswSysUNMCastDropEnable = _Hh3cLswSysUNMCastDropEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 6),
    _Hh3cLswSysUNMCastDropEnable_Type()
)
hh3cLswSysUNMCastDropEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswSysUNMCastDropEnable.setStatus("current")


class _Hh3cLswSysManagementVlan_Type(Integer32):
    """Custom type hh3cLswSysManagementVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cLswSysManagementVlan_Type.__name__ = "Integer32"
_Hh3cLswSysManagementVlan_Object = MibScalar
hh3cLswSysManagementVlan = _Hh3cLswSysManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 7),
    _Hh3cLswSysManagementVlan_Type()
)
hh3cLswSysManagementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswSysManagementVlan.setStatus("current")


class _Hh3cLswSysVlanRange_Type(DisplayString):
    """Custom type hh3cLswSysVlanRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Hh3cLswSysVlanRange_Type.__name__ = "DisplayString"
_Hh3cLswSysVlanRange_Object = MibScalar
hh3cLswSysVlanRange = _Hh3cLswSysVlanRange_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 8),
    _Hh3cLswSysVlanRange_Type()
)
hh3cLswSysVlanRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswSysVlanRange.setStatus("current")
_Hh3cLswSysManagementIpAddr_Type = IpAddress
_Hh3cLswSysManagementIpAddr_Object = MibScalar
hh3cLswSysManagementIpAddr = _Hh3cLswSysManagementIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 9),
    _Hh3cLswSysManagementIpAddr_Type()
)
hh3cLswSysManagementIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswSysManagementIpAddr.setStatus("current")
_Hh3cLswSysManagementIpMask_Type = IpAddress
_Hh3cLswSysManagementIpMask_Object = MibScalar
hh3cLswSysManagementIpMask = _Hh3cLswSysManagementIpMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 10),
    _Hh3cLswSysManagementIpMask_Type()
)
hh3cLswSysManagementIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswSysManagementIpMask.setStatus("current")
_Hh3cMacAddressCountPort_Type = Integer32
_Hh3cMacAddressCountPort_Object = MibScalar
hh3cMacAddressCountPort = _Hh3cMacAddressCountPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 11),
    _Hh3cMacAddressCountPort_Type()
)
hh3cMacAddressCountPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMacAddressCountPort.setStatus("current")
_Hh3cMacAddressCountMachine_Type = Integer32
_Hh3cMacAddressCountMachine_Object = MibScalar
hh3cMacAddressCountMachine = _Hh3cMacAddressCountMachine_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 12),
    _Hh3cMacAddressCountMachine_Type()
)
hh3cMacAddressCountMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMacAddressCountMachine.setStatus("current")
_Hh3cLswSysPhyMemory_Type = Unsigned32
_Hh3cLswSysPhyMemory_Object = MibScalar
hh3cLswSysPhyMemory = _Hh3cLswSysPhyMemory_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 13),
    _Hh3cLswSysPhyMemory_Type()
)
hh3cLswSysPhyMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSysPhyMemory.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLswSysPhyMemory.setUnits("byte")
_Hh3cLswSysMemory_Type = Unsigned32
_Hh3cLswSysMemory_Object = MibScalar
hh3cLswSysMemory = _Hh3cLswSysMemory_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 14),
    _Hh3cLswSysMemory_Type()
)
hh3cLswSysMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSysMemory.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLswSysMemory.setUnits("byte")
_Hh3cLswSysMemoryUsed_Type = Unsigned32
_Hh3cLswSysMemoryUsed_Object = MibScalar
hh3cLswSysMemoryUsed = _Hh3cLswSysMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 15),
    _Hh3cLswSysMemoryUsed_Type()
)
hh3cLswSysMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSysMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLswSysMemoryUsed.setUnits("byte")


class _Hh3cLswSysMemoryRatio_Type(Unsigned32):
    """Custom type hh3cLswSysMemoryRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cLswSysMemoryRatio_Type.__name__ = "Unsigned32"
_Hh3cLswSysMemoryRatio_Object = MibScalar
hh3cLswSysMemoryRatio = _Hh3cLswSysMemoryRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 16),
    _Hh3cLswSysMemoryRatio_Type()
)
hh3cLswSysMemoryRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSysMemoryRatio.setStatus("current")
_Hh3cLswSysTemperature_Type = Integer32
_Hh3cLswSysTemperature_Object = MibScalar
hh3cLswSysTemperature = _Hh3cLswSysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 1, 17),
    _Hh3cLswSysTemperature_Type()
)
hh3cLswSysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSysTemperature.setStatus("current")
_Hh3cLswSlotConf_ObjectIdentity = ObjectIdentity
hh3cLswSlotConf = _Hh3cLswSlotConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4)
)
_Hh3cLswFrameTable_Object = MibTable
hh3cLswFrameTable = _Hh3cLswFrameTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cLswFrameTable.setStatus("current")
_Hh3cLswFrameEntry_Object = MibTableRow
hh3cLswFrameEntry = _Hh3cLswFrameEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 2, 1)
)
hh3cLswFrameEntry.setIndexNames(
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
)
if mibBuilder.loadTexts:
    hh3cLswFrameEntry.setStatus("current")
_Hh3cLswFrameIndex_Type = Integer32
_Hh3cLswFrameIndex_Object = MibTableColumn
hh3cLswFrameIndex = _Hh3cLswFrameIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 2, 1, 1),
    _Hh3cLswFrameIndex_Type()
)
hh3cLswFrameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswFrameIndex.setStatus("current")
_Hh3cLswFrameType_Type = Integer32
_Hh3cLswFrameType_Object = MibTableColumn
hh3cLswFrameType = _Hh3cLswFrameType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 2, 1, 2),
    _Hh3cLswFrameType_Type()
)
hh3cLswFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswFrameType.setStatus("current")


class _Hh3cLswFrameDesc_Type(DisplayString):
    """Custom type hh3cLswFrameDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cLswFrameDesc_Type.__name__ = "DisplayString"
_Hh3cLswFrameDesc_Object = MibTableColumn
hh3cLswFrameDesc = _Hh3cLswFrameDesc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 2, 1, 3),
    _Hh3cLswFrameDesc_Type()
)
hh3cLswFrameDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswFrameDesc.setStatus("current")
_Hh3cLswSlotNumber_Type = Integer32
_Hh3cLswSlotNumber_Object = MibTableColumn
hh3cLswSlotNumber = _Hh3cLswSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 2, 1, 4),
    _Hh3cLswSlotNumber_Type()
)
hh3cLswSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotNumber.setStatus("current")


class _Hh3cLswFrameAdminStatus_Type(Integer32):
    """Custom type hh3cLswFrameAdminStatus based on Integer32"""
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


_Hh3cLswFrameAdminStatus_Type.__name__ = "Integer32"
_Hh3cLswFrameAdminStatus_Object = MibTableColumn
hh3cLswFrameAdminStatus = _Hh3cLswFrameAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 2, 1, 5),
    _Hh3cLswFrameAdminStatus_Type()
)
hh3cLswFrameAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswFrameAdminStatus.setStatus("current")
_Hh3cLswSlotTable_Object = MibTable
hh3cLswSlotTable = _Hh3cLswSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3)
)
if mibBuilder.loadTexts:
    hh3cLswSlotTable.setStatus("current")
_Hh3cLswSlotEntry_Object = MibTableRow
hh3cLswSlotEntry = _Hh3cLswSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1)
)
hh3cLswSlotEntry.setIndexNames(
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
)
if mibBuilder.loadTexts:
    hh3cLswSlotEntry.setStatus("current")
_Hh3cLswSlotIndex_Type = Integer32
_Hh3cLswSlotIndex_Object = MibTableColumn
hh3cLswSlotIndex = _Hh3cLswSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 1),
    _Hh3cLswSlotIndex_Type()
)
hh3cLswSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotIndex.setStatus("current")
_Hh3cLswSlotType_Type = Hh3cLswTypeOfSlot
_Hh3cLswSlotType_Object = MibTableColumn
hh3cLswSlotType = _Hh3cLswSlotType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 2),
    _Hh3cLswSlotType_Type()
)
hh3cLswSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotType.setStatus("current")


class _Hh3cLswSlotDesc_Type(DisplayString):
    """Custom type hh3cLswSlotDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cLswSlotDesc_Type.__name__ = "DisplayString"
_Hh3cLswSlotDesc_Object = MibTableColumn
hh3cLswSlotDesc = _Hh3cLswSlotDesc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 3),
    _Hh3cLswSlotDesc_Type()
)
hh3cLswSlotDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswSlotDesc.setStatus("current")
_Hh3cLswSlotCpuRatio_Type = Integer32
_Hh3cLswSlotCpuRatio_Object = MibTableColumn
hh3cLswSlotCpuRatio = _Hh3cLswSlotCpuRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 4),
    _Hh3cLswSlotCpuRatio_Type()
)
hh3cLswSlotCpuRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotCpuRatio.setStatus("current")


class _Hh3cLswSlotPcbVersion_Type(DisplayString):
    """Custom type hh3cLswSlotPcbVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cLswSlotPcbVersion_Type.__name__ = "DisplayString"
_Hh3cLswSlotPcbVersion_Object = MibTableColumn
hh3cLswSlotPcbVersion = _Hh3cLswSlotPcbVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 5),
    _Hh3cLswSlotPcbVersion_Type()
)
hh3cLswSlotPcbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotPcbVersion.setStatus("current")


class _Hh3cLswSlotSoftwareVersion_Type(DisplayString):
    """Custom type hh3cLswSlotSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cLswSlotSoftwareVersion_Type.__name__ = "DisplayString"
_Hh3cLswSlotSoftwareVersion_Object = MibTableColumn
hh3cLswSlotSoftwareVersion = _Hh3cLswSlotSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 6),
    _Hh3cLswSlotSoftwareVersion_Type()
)
hh3cLswSlotSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotSoftwareVersion.setStatus("current")
_Hh3cLswSubslotNumber_Type = Integer32
_Hh3cLswSubslotNumber_Object = MibTableColumn
hh3cLswSubslotNumber = _Hh3cLswSubslotNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 7),
    _Hh3cLswSubslotNumber_Type()
)
hh3cLswSubslotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSubslotNumber.setStatus("current")


class _Hh3cLswSlotAdminStatus_Type(Integer32):
    """Custom type hh3cLswSlotAdminStatus based on Integer32"""
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


_Hh3cLswSlotAdminStatus_Type.__name__ = "Integer32"
_Hh3cLswSlotAdminStatus_Object = MibTableColumn
hh3cLswSlotAdminStatus = _Hh3cLswSlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 8),
    _Hh3cLswSlotAdminStatus_Type()
)
hh3cLswSlotAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotAdminStatus.setStatus("current")


class _Hh3cLswSlotOperStatus_Type(Integer32):
    """Custom type hh3cLswSlotOperStatus based on Integer32"""
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


_Hh3cLswSlotOperStatus_Type.__name__ = "Integer32"
_Hh3cLswSlotOperStatus_Object = MibTableColumn
hh3cLswSlotOperStatus = _Hh3cLswSlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 9),
    _Hh3cLswSlotOperStatus_Type()
)
hh3cLswSlotOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswSlotOperStatus.setStatus("current")
_Hh3cLswSlotPhyMemory_Type = Unsigned32
_Hh3cLswSlotPhyMemory_Object = MibTableColumn
hh3cLswSlotPhyMemory = _Hh3cLswSlotPhyMemory_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 10),
    _Hh3cLswSlotPhyMemory_Type()
)
hh3cLswSlotPhyMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotPhyMemory.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLswSlotPhyMemory.setUnits("byte")
_Hh3cLswSlotMemory_Type = Unsigned32
_Hh3cLswSlotMemory_Object = MibTableColumn
hh3cLswSlotMemory = _Hh3cLswSlotMemory_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 11),
    _Hh3cLswSlotMemory_Type()
)
hh3cLswSlotMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotMemory.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLswSlotMemory.setUnits("byte")
_Hh3cLswSlotMemoryUsed_Type = Unsigned32
_Hh3cLswSlotMemoryUsed_Object = MibTableColumn
hh3cLswSlotMemoryUsed = _Hh3cLswSlotMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 12),
    _Hh3cLswSlotMemoryUsed_Type()
)
hh3cLswSlotMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLswSlotMemoryUsed.setUnits("byte")


class _Hh3cLswSlotMemoryRatio_Type(Unsigned32):
    """Custom type hh3cLswSlotMemoryRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cLswSlotMemoryRatio_Type.__name__ = "Unsigned32"
_Hh3cLswSlotMemoryRatio_Object = MibTableColumn
hh3cLswSlotMemoryRatio = _Hh3cLswSlotMemoryRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 13),
    _Hh3cLswSlotMemoryRatio_Type()
)
hh3cLswSlotMemoryRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotMemoryRatio.setStatus("current")
_Hh3cLswSlotTemperature_Type = Integer32
_Hh3cLswSlotTemperature_Object = MibTableColumn
hh3cLswSlotTemperature = _Hh3cLswSlotTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 14),
    _Hh3cLswSlotTemperature_Type()
)
hh3cLswSlotTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotTemperature.setStatus("current")
_Hh3cLswSlotPktBufFree_Type = Integer32
_Hh3cLswSlotPktBufFree_Object = MibTableColumn
hh3cLswSlotPktBufFree = _Hh3cLswSlotPktBufFree_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 15),
    _Hh3cLswSlotPktBufFree_Type()
)
hh3cLswSlotPktBufFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotPktBufFree.setStatus("current")
_Hh3cLswSlotPktBufInit_Type = Integer32
_Hh3cLswSlotPktBufInit_Object = MibTableColumn
hh3cLswSlotPktBufInit = _Hh3cLswSlotPktBufInit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 16),
    _Hh3cLswSlotPktBufInit_Type()
)
hh3cLswSlotPktBufInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotPktBufInit.setStatus("current")
_Hh3cLswSlotPktBufMin_Type = Integer32
_Hh3cLswSlotPktBufMin_Object = MibTableColumn
hh3cLswSlotPktBufMin = _Hh3cLswSlotPktBufMin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 17),
    _Hh3cLswSlotPktBufMin_Type()
)
hh3cLswSlotPktBufMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotPktBufMin.setStatus("current")
_Hh3cLswSlotPktBufMiss_Type = Counter64
_Hh3cLswSlotPktBufMiss_Object = MibTableColumn
hh3cLswSlotPktBufMiss = _Hh3cLswSlotPktBufMiss_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 3, 1, 18),
    _Hh3cLswSlotPktBufMiss_Type()
)
hh3cLswSlotPktBufMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSlotPktBufMiss.setStatus("current")
_Hh3cLswSubslotTable_Object = MibTable
hh3cLswSubslotTable = _Hh3cLswSubslotTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 4)
)
if mibBuilder.loadTexts:
    hh3cLswSubslotTable.setStatus("current")
_Hh3cLswSubslotEntry_Object = MibTableRow
hh3cLswSubslotEntry = _Hh3cLswSubslotEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 4, 1)
)
hh3cLswSubslotEntry.setIndexNames(
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswSubslotIndex"),
)
if mibBuilder.loadTexts:
    hh3cLswSubslotEntry.setStatus("current")
_Hh3cLswSubslotIndex_Type = Integer32
_Hh3cLswSubslotIndex_Object = MibTableColumn
hh3cLswSubslotIndex = _Hh3cLswSubslotIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 4, 1, 1),
    _Hh3cLswSubslotIndex_Type()
)
hh3cLswSubslotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSubslotIndex.setStatus("current")
_Hh3cLswSubslotType_Type = Hh3cLswTypeOfSlot
_Hh3cLswSubslotType_Object = MibTableColumn
hh3cLswSubslotType = _Hh3cLswSubslotType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 4, 1, 2),
    _Hh3cLswSubslotType_Type()
)
hh3cLswSubslotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSubslotType.setStatus("current")
_Hh3cLswSubslotPortNum_Type = Integer32
_Hh3cLswSubslotPortNum_Object = MibTableColumn
hh3cLswSubslotPortNum = _Hh3cLswSubslotPortNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 4, 1, 3),
    _Hh3cLswSubslotPortNum_Type()
)
hh3cLswSubslotPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSubslotPortNum.setStatus("current")


class _Hh3cLswSubslotAdminStatus_Type(Integer32):
    """Custom type hh3cLswSubslotAdminStatus based on Integer32"""
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


_Hh3cLswSubslotAdminStatus_Type.__name__ = "Integer32"
_Hh3cLswSubslotAdminStatus_Object = MibTableColumn
hh3cLswSubslotAdminStatus = _Hh3cLswSubslotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 4, 1, 4),
    _Hh3cLswSubslotAdminStatus_Type()
)
hh3cLswSubslotAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSubslotAdminStatus.setStatus("current")
_Hh3cLswSubslotFirstIfIndex_Type = Integer32
_Hh3cLswSubslotFirstIfIndex_Object = MibTableColumn
hh3cLswSubslotFirstIfIndex = _Hh3cLswSubslotFirstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 4, 1, 5),
    _Hh3cLswSubslotFirstIfIndex_Type()
)
hh3cLswSubslotFirstIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswSubslotFirstIfIndex.setStatus("current")
_Hh3cLswPortTable_Object = MibTable
hh3cLswPortTable = _Hh3cLswPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 5)
)
if mibBuilder.loadTexts:
    hh3cLswPortTable.setStatus("current")
_Hh3cLswPortEntry_Object = MibTableRow
hh3cLswPortEntry = _Hh3cLswPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 5, 1)
)
hh3cLswPortEntry.setIndexNames(
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswSubslotIndex"),
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswPortIndex"),
)
if mibBuilder.loadTexts:
    hh3cLswPortEntry.setStatus("current")
_Hh3cLswPortIndex_Type = Integer32
_Hh3cLswPortIndex_Object = MibTableColumn
hh3cLswPortIndex = _Hh3cLswPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 5, 1, 1),
    _Hh3cLswPortIndex_Type()
)
hh3cLswPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswPortIndex.setStatus("current")


class _Hh3cLswPortType_Type(Integer32):
    """Custom type hh3cLswPortType based on Integer32"""
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
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219)
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
          ("type-CFP-100GBASE-LR4", 216),
          ("type-CFP-100GBASE-SR10", 217),
          ("type-CFP-40GBASE-LR4", 212),
          ("type-CFP-40GBASE-SR4", 215),
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
          ("type-CXP-100GBASE-SR10", 218),
          ("type-CXP-NO-CONNECTOR", 219),
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
          ("type-QSFP-PLUS-40GBASE-LR4", 214),
          ("type-QSFP-PLUS-40GBASE-SR4", 205),
          ("type-QSFP-PLUS-NO-CONNECTOR", 213),
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


_Hh3cLswPortType_Type.__name__ = "Integer32"
_Hh3cLswPortType_Object = MibTableColumn
hh3cLswPortType = _Hh3cLswPortType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 5, 1, 2),
    _Hh3cLswPortType_Type()
)
hh3cLswPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswPortType.setStatus("current")
_Hh3cLswPortIfindex_Type = Integer32
_Hh3cLswPortIfindex_Object = MibTableColumn
hh3cLswPortIfindex = _Hh3cLswPortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 5, 1, 3),
    _Hh3cLswPortIfindex_Type()
)
hh3cLswPortIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswPortIfindex.setStatus("current")


class _Hh3cLswPortIsPlugged_Type(Integer32):
    """Custom type hh3cLswPortIsPlugged based on Integer32"""
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


_Hh3cLswPortIsPlugged_Type.__name__ = "Integer32"
_Hh3cLswPortIsPlugged_Object = MibTableColumn
hh3cLswPortIsPlugged = _Hh3cLswPortIsPlugged_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 5, 1, 4),
    _Hh3cLswPortIsPlugged_Type()
)
hh3cLswPortIsPlugged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswPortIsPlugged.setStatus("current")
_Hh3cLswPortLoopbackTable_Object = MibTable
hh3cLswPortLoopbackTable = _Hh3cLswPortLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 6)
)
if mibBuilder.loadTexts:
    hh3cLswPortLoopbackTable.setStatus("current")
_Hh3cLswPortLoopbackEntry_Object = MibTableRow
hh3cLswPortLoopbackEntry = _Hh3cLswPortLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cLswPortLoopbackEntry.setStatus("current")


class _Hh3cLswPortLoopbackIsSupport_Type(Integer32):
    """Custom type hh3cLswPortLoopbackIsSupport based on Integer32"""
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


_Hh3cLswPortLoopbackIsSupport_Type.__name__ = "Integer32"
_Hh3cLswPortLoopbackIsSupport_Object = MibTableColumn
hh3cLswPortLoopbackIsSupport = _Hh3cLswPortLoopbackIsSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 6, 1, 1),
    _Hh3cLswPortLoopbackIsSupport_Type()
)
hh3cLswPortLoopbackIsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswPortLoopbackIsSupport.setStatus("current")


class _Hh3cLswPortLoopbackOperate_Type(Integer32):
    """Custom type hh3cLswPortLoopbackOperate based on Integer32"""
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


_Hh3cLswPortLoopbackOperate_Type.__name__ = "Integer32"
_Hh3cLswPortLoopbackOperate_Object = MibTableColumn
hh3cLswPortLoopbackOperate = _Hh3cLswPortLoopbackOperate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 6, 1, 2),
    _Hh3cLswPortLoopbackOperate_Type()
)
hh3cLswPortLoopbackOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswPortLoopbackOperate.setStatus("current")


class _Hh3cLswPortLoopbackResult_Type(Integer32):
    """Custom type hh3cLswPortLoopbackResult based on Integer32"""
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


_Hh3cLswPortLoopbackResult_Type.__name__ = "Integer32"
_Hh3cLswPortLoopbackResult_Object = MibTableColumn
hh3cLswPortLoopbackResult = _Hh3cLswPortLoopbackResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 6, 1, 3),
    _Hh3cLswPortLoopbackResult_Type()
)
hh3cLswPortLoopbackResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswPortLoopbackResult.setStatus("current")


class _Hh3cLswPortLoopbackAutoStopSupport_Type(Integer32):
    """Custom type hh3cLswPortLoopbackAutoStopSupport based on Integer32"""
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


_Hh3cLswPortLoopbackAutoStopSupport_Type.__name__ = "Integer32"
_Hh3cLswPortLoopbackAutoStopSupport_Object = MibTableColumn
hh3cLswPortLoopbackAutoStopSupport = _Hh3cLswPortLoopbackAutoStopSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 6, 1, 4),
    _Hh3cLswPortLoopbackAutoStopSupport_Type()
)
hh3cLswPortLoopbackAutoStopSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswPortLoopbackAutoStopSupport.setStatus("current")


class _Hh3cLswPortLoopbackRemoteResult_Type(Integer32):
    """Custom type hh3cLswPortLoopbackRemoteResult based on Integer32"""
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


_Hh3cLswPortLoopbackRemoteResult_Type.__name__ = "Integer32"
_Hh3cLswPortLoopbackRemoteResult_Object = MibTableColumn
hh3cLswPortLoopbackRemoteResult = _Hh3cLswPortLoopbackRemoteResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 6, 1, 5),
    _Hh3cLswPortLoopbackRemoteResult_Type()
)
hh3cLswPortLoopbackRemoteResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswPortLoopbackRemoteResult.setStatus("current")


class _Hh3cLswPortLoopbackLocalResult_Type(Integer32):
    """Custom type hh3cLswPortLoopbackLocalResult based on Integer32"""
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


_Hh3cLswPortLoopbackLocalResult_Type.__name__ = "Integer32"
_Hh3cLswPortLoopbackLocalResult_Object = MibTableColumn
hh3cLswPortLoopbackLocalResult = _Hh3cLswPortLoopbackLocalResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 6, 1, 6),
    _Hh3cLswPortLoopbackLocalResult_Type()
)
hh3cLswPortLoopbackLocalResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswPortLoopbackLocalResult.setStatus("current")


class _Hh3cLswPortLoopbackInternalResult_Type(Integer32):
    """Custom type hh3cLswPortLoopbackInternalResult based on Integer32"""
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


_Hh3cLswPortLoopbackInternalResult_Type.__name__ = "Integer32"
_Hh3cLswPortLoopbackInternalResult_Object = MibTableColumn
hh3cLswPortLoopbackInternalResult = _Hh3cLswPortLoopbackInternalResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 6, 1, 7),
    _Hh3cLswPortLoopbackInternalResult_Type()
)
hh3cLswPortLoopbackInternalResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswPortLoopbackInternalResult.setStatus("current")


class _Hh3cLswPortLoopbackExternalResult_Type(Integer32):
    """Custom type hh3cLswPortLoopbackExternalResult based on Integer32"""
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


_Hh3cLswPortLoopbackExternalResult_Type.__name__ = "Integer32"
_Hh3cLswPortLoopbackExternalResult_Object = MibTableColumn
hh3cLswPortLoopbackExternalResult = _Hh3cLswPortLoopbackExternalResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 6, 1, 8),
    _Hh3cLswPortLoopbackExternalResult_Type()
)
hh3cLswPortLoopbackExternalResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswPortLoopbackExternalResult.setStatus("current")
_Hh3cLswFabricTable_Object = MibTable
hh3cLswFabricTable = _Hh3cLswFabricTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 7)
)
if mibBuilder.loadTexts:
    hh3cLswFabricTable.setStatus("current")
_Hh3cLswFabricEntry_Object = MibTableRow
hh3cLswFabricEntry = _Hh3cLswFabricEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 7, 1)
)
hh3cLswFabricEntry.setIndexNames(
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswSubslotIndex"),
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswFabricChannelIndex"),
)
if mibBuilder.loadTexts:
    hh3cLswFabricEntry.setStatus("current")
_Hh3cLswFabricChannelIndex_Type = Integer32
_Hh3cLswFabricChannelIndex_Object = MibTableColumn
hh3cLswFabricChannelIndex = _Hh3cLswFabricChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 7, 1, 1),
    _Hh3cLswFabricChannelIndex_Type()
)
hh3cLswFabricChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cLswFabricChannelIndex.setStatus("current")


class _Hh3cLswFabricUtilIn_Type(Integer32):
    """Custom type hh3cLswFabricUtilIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cLswFabricUtilIn_Type.__name__ = "Integer32"
_Hh3cLswFabricUtilIn_Object = MibTableColumn
hh3cLswFabricUtilIn = _Hh3cLswFabricUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 7, 1, 2),
    _Hh3cLswFabricUtilIn_Type()
)
hh3cLswFabricUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswFabricUtilIn.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLswFabricUtilIn.setUnits("one percent")


class _Hh3cLswFabricUtilOut_Type(Integer32):
    """Custom type hh3cLswFabricUtilOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cLswFabricUtilOut_Type.__name__ = "Integer32"
_Hh3cLswFabricUtilOut_Object = MibTableColumn
hh3cLswFabricUtilOut = _Hh3cLswFabricUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 7, 1, 3),
    _Hh3cLswFabricUtilOut_Type()
)
hh3cLswFabricUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswFabricUtilOut.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLswFabricUtilOut.setUnits("one percent")


class _Hh3cLswFabricPeakIn_Type(Integer32):
    """Custom type hh3cLswFabricPeakIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cLswFabricPeakIn_Type.__name__ = "Integer32"
_Hh3cLswFabricPeakIn_Object = MibTableColumn
hh3cLswFabricPeakIn = _Hh3cLswFabricPeakIn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 7, 1, 4),
    _Hh3cLswFabricPeakIn_Type()
)
hh3cLswFabricPeakIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswFabricPeakIn.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLswFabricPeakIn.setUnits("one percent")
_Hh3cLswFabricPeakInTime_Type = DateAndTime
_Hh3cLswFabricPeakInTime_Object = MibTableColumn
hh3cLswFabricPeakInTime = _Hh3cLswFabricPeakInTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 7, 1, 5),
    _Hh3cLswFabricPeakInTime_Type()
)
hh3cLswFabricPeakInTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswFabricPeakInTime.setStatus("current")


class _Hh3cLswFabricPeakOut_Type(Integer32):
    """Custom type hh3cLswFabricPeakOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cLswFabricPeakOut_Type.__name__ = "Integer32"
_Hh3cLswFabricPeakOut_Object = MibTableColumn
hh3cLswFabricPeakOut = _Hh3cLswFabricPeakOut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 7, 1, 6),
    _Hh3cLswFabricPeakOut_Type()
)
hh3cLswFabricPeakOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswFabricPeakOut.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLswFabricPeakOut.setUnits("one percent")
_Hh3cLswFabricPeakOutTime_Type = DateAndTime
_Hh3cLswFabricPeakOutTime_Object = MibTableColumn
hh3cLswFabricPeakOutTime = _Hh3cLswFabricPeakOutTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18, 4, 7, 1, 7),
    _Hh3cLswFabricPeakOutTime_Type()
)
hh3cLswFabricPeakOutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswFabricPeakOutTime.setStatus("current")
hh3cLswPortEntry.registerAugmentions(
    ("HH3C-LSW-DEV-ADM-MIB",
     "hh3cLswPortLoopbackEntry")
)
hh3cLswPortLoopbackEntry.setIndexNames(*hh3cLswPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LSW-DEV-ADM-MIB",
    **{"Hh3cLswTypeOfSlot": Hh3cLswTypeOfSlot,
       "hh3cLswDeviceAdmin": hh3cLswDeviceAdmin,
       "hh3cLswSystemPara": hh3cLswSystemPara,
       "hh3cLswSysIpAddr": hh3cLswSysIpAddr,
       "hh3cLswSysIpMask": hh3cLswSysIpMask,
       "hh3cLswSysCpuRatio": hh3cLswSysCpuRatio,
       "hh3cLswSysVersion": hh3cLswSysVersion,
       "hh3cLswSysTime": hh3cLswSysTime,
       "hh3cLswSysUNMCastDropEnable": hh3cLswSysUNMCastDropEnable,
       "hh3cLswSysManagementVlan": hh3cLswSysManagementVlan,
       "hh3cLswSysVlanRange": hh3cLswSysVlanRange,
       "hh3cLswSysManagementIpAddr": hh3cLswSysManagementIpAddr,
       "hh3cLswSysManagementIpMask": hh3cLswSysManagementIpMask,
       "hh3cMacAddressCountPort": hh3cMacAddressCountPort,
       "hh3cMacAddressCountMachine": hh3cMacAddressCountMachine,
       "hh3cLswSysPhyMemory": hh3cLswSysPhyMemory,
       "hh3cLswSysMemory": hh3cLswSysMemory,
       "hh3cLswSysMemoryUsed": hh3cLswSysMemoryUsed,
       "hh3cLswSysMemoryRatio": hh3cLswSysMemoryRatio,
       "hh3cLswSysTemperature": hh3cLswSysTemperature,
       "hh3cLswSlotConf": hh3cLswSlotConf,
       "hh3cLswFrameTable": hh3cLswFrameTable,
       "hh3cLswFrameEntry": hh3cLswFrameEntry,
       "hh3cLswFrameIndex": hh3cLswFrameIndex,
       "hh3cLswFrameType": hh3cLswFrameType,
       "hh3cLswFrameDesc": hh3cLswFrameDesc,
       "hh3cLswSlotNumber": hh3cLswSlotNumber,
       "hh3cLswFrameAdminStatus": hh3cLswFrameAdminStatus,
       "hh3cLswSlotTable": hh3cLswSlotTable,
       "hh3cLswSlotEntry": hh3cLswSlotEntry,
       "hh3cLswSlotIndex": hh3cLswSlotIndex,
       "hh3cLswSlotType": hh3cLswSlotType,
       "hh3cLswSlotDesc": hh3cLswSlotDesc,
       "hh3cLswSlotCpuRatio": hh3cLswSlotCpuRatio,
       "hh3cLswSlotPcbVersion": hh3cLswSlotPcbVersion,
       "hh3cLswSlotSoftwareVersion": hh3cLswSlotSoftwareVersion,
       "hh3cLswSubslotNumber": hh3cLswSubslotNumber,
       "hh3cLswSlotAdminStatus": hh3cLswSlotAdminStatus,
       "hh3cLswSlotOperStatus": hh3cLswSlotOperStatus,
       "hh3cLswSlotPhyMemory": hh3cLswSlotPhyMemory,
       "hh3cLswSlotMemory": hh3cLswSlotMemory,
       "hh3cLswSlotMemoryUsed": hh3cLswSlotMemoryUsed,
       "hh3cLswSlotMemoryRatio": hh3cLswSlotMemoryRatio,
       "hh3cLswSlotTemperature": hh3cLswSlotTemperature,
       "hh3cLswSlotPktBufFree": hh3cLswSlotPktBufFree,
       "hh3cLswSlotPktBufInit": hh3cLswSlotPktBufInit,
       "hh3cLswSlotPktBufMin": hh3cLswSlotPktBufMin,
       "hh3cLswSlotPktBufMiss": hh3cLswSlotPktBufMiss,
       "hh3cLswSubslotTable": hh3cLswSubslotTable,
       "hh3cLswSubslotEntry": hh3cLswSubslotEntry,
       "hh3cLswSubslotIndex": hh3cLswSubslotIndex,
       "hh3cLswSubslotType": hh3cLswSubslotType,
       "hh3cLswSubslotPortNum": hh3cLswSubslotPortNum,
       "hh3cLswSubslotAdminStatus": hh3cLswSubslotAdminStatus,
       "hh3cLswSubslotFirstIfIndex": hh3cLswSubslotFirstIfIndex,
       "hh3cLswPortTable": hh3cLswPortTable,
       "hh3cLswPortEntry": hh3cLswPortEntry,
       "hh3cLswPortIndex": hh3cLswPortIndex,
       "hh3cLswPortType": hh3cLswPortType,
       "hh3cLswPortIfindex": hh3cLswPortIfindex,
       "hh3cLswPortIsPlugged": hh3cLswPortIsPlugged,
       "hh3cLswPortLoopbackTable": hh3cLswPortLoopbackTable,
       "hh3cLswPortLoopbackEntry": hh3cLswPortLoopbackEntry,
       "hh3cLswPortLoopbackIsSupport": hh3cLswPortLoopbackIsSupport,
       "hh3cLswPortLoopbackOperate": hh3cLswPortLoopbackOperate,
       "hh3cLswPortLoopbackResult": hh3cLswPortLoopbackResult,
       "hh3cLswPortLoopbackAutoStopSupport": hh3cLswPortLoopbackAutoStopSupport,
       "hh3cLswPortLoopbackRemoteResult": hh3cLswPortLoopbackRemoteResult,
       "hh3cLswPortLoopbackLocalResult": hh3cLswPortLoopbackLocalResult,
       "hh3cLswPortLoopbackInternalResult": hh3cLswPortLoopbackInternalResult,
       "hh3cLswPortLoopbackExternalResult": hh3cLswPortLoopbackExternalResult,
       "hh3cLswFabricTable": hh3cLswFabricTable,
       "hh3cLswFabricEntry": hh3cLswFabricEntry,
       "hh3cLswFabricChannelIndex": hh3cLswFabricChannelIndex,
       "hh3cLswFabricUtilIn": hh3cLswFabricUtilIn,
       "hh3cLswFabricUtilOut": hh3cLswFabricUtilOut,
       "hh3cLswFabricPeakIn": hh3cLswFabricPeakIn,
       "hh3cLswFabricPeakInTime": hh3cLswFabricPeakInTime,
       "hh3cLswFabricPeakOut": hh3cLswFabricPeakOut,
       "hh3cLswFabricPeakOutTime": hh3cLswFabricPeakOutTime}
)
