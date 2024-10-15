# SNMP MIB module (TNMS-NBI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TNMS-NBI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:30 2024
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

(AutonomousType,
 DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

svsProxEnms = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22)
)
svsProxEnms.setRevisions(
        ("2016-10-28 00:00",
         "2016-10-28 00:00",
         "2016-03-15 00:00",
         "2015-07-24 00:00",
         "2015-04-30 00:00",
         "2014-10-04 00:00",
         "2014-09-29 00:00",
         "2014-06-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DisplayString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class Boolean(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )



class TrapFilter(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sendTrapsOff", 2),
          ("sendTrapsOn", 1))
    )



class EnmsTimeStamp(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class InfoString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TPIndex(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class UniqueId(Unsigned32, TextualConvention):
    status = "current"


class NEId(UniqueId, TextualConvention):
    status = "current"


class ModuleId(UniqueId, TextualConvention):
    status = "current"


class PortId(UniqueId, TextualConvention):
    status = "current"


class TPId(UniqueId, TextualConvention):
    status = "current"


class PortConnId(UniqueId, TextualConvention):
    status = "current"


class SNCId(UniqueId, TextualConvention):
    status = "current"


class EthernetPathId(UniqueId, TextualConvention):
    status = "current"


class CCId(UniqueId, TextualConvention):
    status = "current"


class SubscriberId(UniqueId, TextualConvention):
    status = "current"


class ServiceId(UniqueId, TextualConvention):
    status = "current"


class VpcId(UniqueId, TextualConvention):
    status = "current"


class VccId(UniqueId, TextualConvention):
    status = "current"


class Bandwidth(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
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
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("critical", 4),
          ("indeterminate", 5),
          ("major", 3),
          ("minor", 2),
          ("nonAlarmed", 7),
          ("nonExistent", 6),
          ("notAlarmed", 8),
          ("warning", 1))
    )



class AlarmClass(Integer32, TextualConvention):
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
        *(("communication", 1),
          ("environment", 5),
          ("equipment", 4),
          ("processing", 3),
          ("quality", 2),
          ("security", 8),
          ("system", 6),
          ("threshold", 7),
          ("unknown", 0))
    )



class AlarmState(Integer32, TextualConvention):
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
        *(("acknowledged", 2),
          ("noAlarm", 1),
          ("unAcknowledged", 3))
    )



class OperationalState(Integer32, TextualConvention):
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
        *(("disabled", 3),
          ("enabled", 2),
          ("partiallyEnabled", 4),
          ("unknown", 1))
    )



class OperatingMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maintenance", 2),
          ("operation", 1))
    )



class AdministrativeState(Integer32, TextualConvention):
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
        *(("locked", 1),
          ("shuttingDown", 3),
          ("starting", 4),
          ("unknown", 0),
          ("unlocked", 2))
    )



class ProvisioningState(Integer32, TextualConvention):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("provisioned", 1),
          ("unprovisioned", 2))
    )



class UsageState(Integer32, TextualConvention):
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
        *(("active", 2),
          ("busy", 3),
          ("idle", 1))
    )



class ProtectionState(Integer32, TextualConvention):
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
        *(("non", 0),
          ("protecting", 2),
          ("working", 1))
    )



class EntityType(Integer32, TextualConvention):
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
        *(("ems", 10),
          ("ethernetPath", 11),
          ("module", 2),
          ("ne", 3),
          ("opmRequest", 13),
          ("other", 0),
          ("pmRequest", 12),
          ("port", 4),
          ("portConn", 6),
          ("proxy", 1),
          ("service", 9),
          ("subNetworkConn", 7),
          ("subscriber", 8),
          ("tp", 5))
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
              564,
              565,
              568,
              590,
              591,
              592,
              593,
              615,
              616,
              617,
              618,
              619,
              620,
              621,
              622,
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
              698,
              699,
              700,
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
              739,
              740,
              741,
              742,
              743,
              744,
              745,
              746,
              747,
              748,
              750,
              751,
              752,
              753,
              754,
              756,
              757,
              758,
              759,
              760,
              761,
              762,
              763,
              764,
              765,
              766,
              767,
              768,
              769,
              770,
              771,
              772,
              773,
              774,
              775,
              776,
              777,
              778,
              779,
              780,
              781,
              782,
              783,
              784,
              785,
              786,
              787,
              788,
              789,
              790,
              791,
              792,
              793,
              794,
              795,
              796,
              797,
              798,
              799,
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
              816,
              817,
              818,
              819,
              820,
              821,
              822,
              823,
              824,
              825,
              826,
              827,
              828,
              829,
              830,
              831,
              832,
              833,
              834,
              835,
              836,
              837,
              838,
              839,
              840,
              841,
              842,
              843,
              844,
              845,
              846,
              848,
              849,
              850,
              851,
              852,
              853,
              854,
              855,
              856,
              857,
              858,
              859,
              860,
              861,
              862,
              863,
              880,
              881,
              882,
              883,
              884,
              885,
              886,
              887,
              888,
              889,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              897,
              898,
              899,
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
              975,
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
              997,
              998,
              999,
              1000,
              1002,
              1005,
              1006,
              1007,
              1008,
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
              1093,
              1094,
              1095,
              1096,
              1097,
              1098,
              1099,
              1100,
              1101,
              1102,
              1103,
              1104,
              1105,
              1106,
              1107,
              1108,
              1109,
              1110,
              1111,
              1112,
              1113,
              1114,
              1115,
              1116,
              1117,
              1118,
              1119,
              1120,
              1121,
              1122,
              1123,
              1124,
              1125,
              1126,
              1127,
              1128,
              1129,
              1130,
              1131,
              1132,
              1133,
              1134,
              1135,
              1136,
              1137,
              1138,
              1139,
              1140,
              1141,
              1142,
              1143,
              1144,
              1145,
              1146,
              1147,
              1148,
              1149,
              1150,
              1151,
              1152,
              1153,
              1154,
              1155,
              1156,
              1157,
              1158,
              1159,
              1160,
              1161,
              1162,
              1163,
              1164,
              1165,
              1166,
              1167,
              1168,
              1169,
              1170,
              1171,
              1172,
              1173,
              1174,
              1175,
              1176,
              1177,
              1178,
              1179,
              1180,
              1181,
              1182,
              1183,
              1184,
              1185,
              1186,
              1187,
              1188,
              1189,
              1190,
              1191,
              1192,
              1193,
              1194,
              1195,
              1196,
              1197,
              1198,
              1199,
              1200,
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
              1256,
              1257,
              1258,
              1259,
              1260,
              1261,
              1262,
              1263,
              1264,
              1265,
              1266,
              1267,
              1268,
              1269,
              1270,
              1271,
              1272,
              1273,
              1274,
              1275,
              1276,
              1277,
              1278,
              1279,
              1280,
              1281,
              1282,
              1283,
              1284,
              1285,
              1286,
              1287,
              1288,
              1289,
              1290,
              1291,
              1292,
              1293,
              1294,
              1295,
              1296,
              1297,
              1298,
              1299,
              1300,
              1301,
              1302,
              1303,
              1304,
              1305,
              1306,
              1307,
              1308,
              1309,
              1310,
              1311,
              1312,
              1313,
              1314,
              1315,
              1316,
              1317,
              1318,
              1319,
              1320,
              1321,
              1322,
              1323,
              1324,
              1325,
              1326,
              1327,
              1328,
              1329,
              1330,
              1331,
              1332,
              1333,
              1334,
              1335,
              1336,
              1337,
              1338,
              1339,
              1340,
              1341,
              1342,
              1343,
              1344,
              1345,
              1346,
              1347,
              1348,
              1349,
              1350,
              1351,
              1352,
              1353,
              1354,
              1355,
              1356,
              1357,
              1358,
              1359,
              1360,
              1361,
              1362,
              1363,
              1364,
              1365,
              1366,
              1367,
              1368,
              1369,
              1370,
              1371,
              1372,
              1373,
              1374,
              1375,
              1376,
              1377,
              1378,
              1379,
              1380,
              1381,
              1382,
              1383,
              1384,
              1385,
              1386,
              1387,
              1388,
              1389,
              1390,
              1391,
              1392,
              1393,
              1394,
              1395,
              1396,
              1397,
              1398,
              1399,
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
              1410,
              1411,
              1412,
              1413,
              1414,
              1415,
              1416,
              1417,
              1418,
              1419,
              1420,
              1421,
              1422,
              1423,
              1424,
              1425,
              1426,
              1427,
              1428,
              1429,
              1430,
              1431,
              1432,
              1433,
              1434,
              1435,
              1436,
              1437,
              1438,
              1439,
              1440,
              1441,
              1442,
              1443,
              1444,
              1445,
              1446,
              1447,
              1448,
              1449,
              1450,
              1451,
              1452,
              1453,
              1454,
              1455,
              1456,
              1457,
              1458,
              1459,
              1460,
              1461,
              1462,
              1463,
              1464,
              1465,
              1466,
              1467,
              1468,
              1469,
              1470,
              1471,
              1472,
              1473,
              1474,
              1475,
              1476,
              1477,
              1478,
              1479,
              1480,
              1481,
              1482,
              1483,
              1484,
              1485,
              1486,
              1487,
              1488,
              1489,
              1490,
              1491,
              1492,
              1493,
              1494,
              1495,
              1496,
              1497,
              1498,
              1499,
              1500,
              1501,
              1502,
              1503,
              1504,
              1505,
              1506,
              1507,
              1508,
              1509,
              1510,
              1511,
              1512,
              1513,
              1514,
              1515,
              1516,
              1517,
              1518,
              1519,
              1520,
              1521,
              1522,
              1523,
              1524,
              1525,
              1526,
              1527,
              1528,
              1529,
              1530,
              1531,
              1532,
              1533,
              1534,
              1535,
              1536,
              1537,
              1538,
              1539,
              1540,
              1541,
              1542,
              1543,
              1544,
              1545,
              1546,
              1547,
              1548,
              1549,
              1550,
              1551,
              1552,
              1553,
              1554,
              1555,
              1556,
              1557,
              1558,
              1559,
              1560,
              1561,
              1562,
              1563,
              1564,
              1565,
              1566,
              1567,
              1568,
              1569,
              1570,
              1571,
              1572,
              1573,
              1574,
              1575,
              1576,
              1577,
              1578,
              1579,
              1580,
              1581,
              1582,
              1583,
              1584,
              1585,
              1586,
              1587,
              1588,
              1589,
              1590,
              1591,
              1592,
              1593,
              1594,
              1595,
              1596,
              1597,
              1598,
              1599,
              1600,
              1601,
              1602,
              1603,
              1604,
              1605,
              1606,
              1607,
              1608,
              1609,
              1610,
              1611,
              1612,
              1613,
              1614,
              1615,
              1616,
              1617,
              1618,
              1619,
              1620,
              1621,
              1622,
              1623,
              1624,
              1625,
              1626,
              1627,
              1628,
              1629,
              1630,
              1631,
              1632,
              1633,
              1634,
              1635,
              1636,
              1637,
              1638,
              1639,
              1640,
              1641,
              1642,
              1643,
              1644,
              1645,
              1646,
              1647,
              1648,
              1649,
              1650,
              1651,
              1652,
              1653,
              1654,
              1655,
              1656,
              1657,
              1658,
              1659,
              1660,
              1661,
              1662,
              1663,
              1664,
              1665,
              1666,
              1667,
              1668,
              1669,
              1670,
              1671,
              1672,
              1673,
              1674,
              1675,
              1676,
              1677,
              1678,
              1679,
              1680,
              1681,
              1682,
              1683,
              1684,
              1685,
              1686,
              1687,
              1688,
              1689,
              1690,
              1691,
              1692,
              1693,
              1694,
              1695,
              1696,
              1697,
              1698,
              1699,
              1700,
              1701,
              1702,
              1703,
              1704,
              1705,
              1706,
              1707,
              1708,
              1709,
              1710,
              1711,
              1712,
              1713,
              1714,
              1715,
              1716,
              1717,
              1718,
              1719,
              1720,
              1721,
              1722,
              1723,
              1724,
              1725,
              1726,
              1727,
              1728,
              1729,
              1730,
              1731,
              1732,
              1733,
              1734,
              1735,
              1736,
              1737,
              1738,
              1739,
              1740,
              1741,
              1742,
              1743,
              1744,
              1745,
              1746,
              1747,
              1748,
              1749,
              1750,
              1751,
              1752,
              1753,
              1754,
              1755,
              1756,
              1757,
              1758,
              1759,
              1760,
              1761,
              1762,
              1763,
              1764,
              1765,
              1766,
              1767,
              1768,
              1769,
              1770,
              1771,
              1772,
              1773,
              1774,
              1775,
              1776,
              1777,
              1778,
              1779,
              1780,
              1781,
              1782,
              1783,
              1784,
              1785,
              1786,
              1787,
              1788,
              1789,
              1790,
              1791,
              1792,
              1793,
              1794,
              1795,
              1796,
              1797,
              1798,
              1799,
              1800,
              1801,
              1802,
              1803,
              1804,
              1805,
              1806,
              1807,
              1808,
              1809,
              1810,
              1811,
              1812,
              1813,
              1814,
              1815,
              1816,
              1817,
              1818,
              1819,
              1820,
              1821,
              1822,
              1823,
              1824,
              1825,
              1826,
              1827,
              1828,
              1829,
              1830,
              1831,
              1832,
              1833,
              1834,
              1835,
              1836,
              1837,
              1838,
              1839,
              1840,
              1841,
              1842,
              1843,
              1844,
              1845,
              1846,
              1847,
              1848,
              1849,
              1850,
              1851,
              1852,
              1853,
              1854,
              1855,
              1856,
              1857,
              1858,
              1859,
              1860,
              1861,
              1862,
              1863,
              1864,
              1865,
              1866,
              1867,
              1868,
              1869,
              1870,
              1871,
              1872,
              1873,
              1874,
              1875,
              1876,
              1877,
              1878,
              1879,
              1880,
              1881,
              1882,
              1883,
              1884,
              1885,
              1886,
              1887,
              1888,
              1889,
              1890,
              1891,
              1892,
              1893,
              1894,
              1895,
              1896,
              1897,
              1898,
              1899,
              1900,
              1901,
              1902,
              1903,
              1904,
              1905,
              1906,
              1907,
              1908,
              1909,
              1910,
              1911,
              1912,
              1913,
              1914,
              1915,
              1916,
              1917,
              1918,
              1919,
              1920,
              1921,
              1922,
              1923,
              1924,
              1925,
              1926,
              1927,
              1928,
              1929,
              1930,
              1931,
              1932,
              1933,
              1934,
              1935,
              1936,
              1937,
              1938,
              1939,
              1940,
              1941,
              1942,
              1943,
              1944,
              1945,
              1946,
              1947,
              1948,
              1949,
              1950,
              1951,
              1952,
              1953,
              1954,
              1955,
              1956,
              1957,
              1958,
              1959,
              1960,
              1961,
              1962,
              1963,
              1964,
              1965,
              1966,
              1967,
              1968,
              1969,
              1970,
              1971,
              1972,
              1973,
              1974,
              1975,
              1976,
              1977,
              1978,
              1979,
              1980,
              1981,
              1982,
              1983,
              1984,
              1985,
              1986,
              1987,
              1988,
              1989,
              1990,
              1991,
              1992,
              1993,
              1994,
              1995,
              1996,
              1997,
              1998,
              2000,
              2001,
              2002,
              2003,
              2004,
              2005,
              2006,
              2007,
              2008,
              2009,
              2010,
              2011,
              2012,
              2013,
              2014,
              2015,
              2016,
              2017,
              2018,
              2019,
              2021,
              2022,
              2023,
              2024,
              2025,
              2026,
              2027,
              2028,
              2029,
              2030,
              2031,
              2032,
              2033,
              2034,
              2035,
              2036,
              2037,
              2039,
              2040,
              2041,
              2042,
              2043,
              2044,
              2045,
              2046,
              2047,
              2048,
              2049,
              2050,
              2051,
              2052,
              2053,
              2054,
              2055,
              2056,
              2057,
              2058,
              2059,
              2060,
              2061,
              2062,
              2063,
              2064,
              2065,
              2066,
              2067,
              2068,
              2069,
              2070,
              2071,
              2072,
              2073,
              2074,
              2075,
              2076,
              2077,
              2100,
              2101,
              2102,
              2103,
              2104,
              2105,
              2106,
              2107,
              2108,
              2109,
              2110,
              2111,
              2112,
              2113,
              2114,
              2115,
              2116,
              2117,
              2118,
              2119,
              2120,
              2121,
              2122,
              2123,
              2124,
              2125,
              2126,
              2127,
              2128,
              2129,
              2130,
              2131,
              2132,
              2133,
              2134,
              2135,
              2136,
              2137,
              2138,
              2139,
              2140,
              2141,
              2142,
              2143,
              2144,
              2145,
              2146,
              2147,
              2148,
              2149,
              2150,
              2151,
              2152,
              2153,
              2154,
              2155,
              2156,
              2157,
              2200,
              2201,
              2202,
              2203,
              2204,
              2205,
              2206,
              2207,
              2208,
              2209,
              2210,
              2211,
              2212,
              2213,
              2214,
              2215,
              2216,
              2217,
              2218,
              2219,
              2220,
              2221,
              2222,
              2223,
              2224,
              2225,
              2226,
              2227,
              2228,
              2229,
              2230,
              2231,
              2232,
              2233,
              2234,
              2235,
              2236,
              2237,
              2238,
              2239,
              2240,
              2241,
              2242,
              2243,
              2244,
              2245,
              2246,
              2247,
              2248,
              2249,
              2250,
              2251,
              2252,
              2253,
              2254,
              2255,
              2256,
              2257,
              2258,
              2259,
              2260,
              2261,
              2262,
              2263,
              2264,
              2265,
              2266,
              2267,
              2268,
              2269,
              2270,
              2271,
              2272,
              2273,
              2274,
              2275,
              2276,
              2277,
              2278,
              2279,
              2280,
              2281,
              2282,
              2283,
              2284,
              2285,
              2286,
              2287,
              2288,
              2289,
              2290,
              2291,
              2292,
              2293,
              2294,
              2295,
              2296,
              2297,
              2298,
              2299,
              2300,
              2301,
              2302,
              2303,
              2304,
              2305,
              2306,
              2307,
              2308,
              2309,
              2310,
              2311,
              2500,
              2501,
              3000,
              3001,
              3002,
              3003,
              3004,
              3005,
              3006,
              3007,
              3008,
              3009,
              3010,
              3011,
              3012,
              3013,
              3014,
              3015,
              3016,
              3017,
              3018,
              3019,
              3020,
              3021,
              3022,
              3023,
              3024,
              3025,
              3026,
              3027,
              3028,
              3029,
              3030,
              3031,
              3032,
              3033,
              3034,
              3035,
              3036,
              3037,
              3038,
              3039,
              3040,
              3041,
              3042,
              3043,
              3044,
              3045,
              3046,
              3047,
              3048,
              3049,
              3050,
              3051,
              3052,
              3053,
              3054,
              3055,
              3056,
              3057,
              3058,
              3059,
              3060,
              3061,
              3062,
              3063,
              3064,
              3065,
              3066,
              3067,
              3068,
              3069,
              3070,
              3071,
              3072,
              3073,
              3074,
              3075,
              3076,
              3077,
              3078,
              3079,
              3080,
              3081,
              3082,
              3083,
              3084,
              3085,
              3086,
              3087,
              3088,
              3089,
              3090,
              3091,
              3092,
              3093,
              3094,
              3095,
              3096,
              3097,
              3098,
              3099,
              3100,
              3101,
              3102,
              3103,
              3104,
              3105,
              3106,
              3107,
              3108,
              3109,
              3110,
              3111,
              3112,
              3113,
              3114,
              3115,
              3116,
              3117,
              3118,
              3119,
              3120,
              3121,
              3122,
              3123,
              3124,
              3125,
              3126,
              3127,
              3128,
              3129,
              3130,
              3131,
              3132,
              3133,
              3134,
              3135,
              3136,
              3137,
              3139,
              3140,
              3141,
              3142,
              3143,
              3144,
              3145,
              3146,
              3147,
              3148,
              3149,
              3150,
              3151,
              3152,
              3153,
              3154,
              3155,
              3156,
              3157,
              3158,
              3159,
              3160,
              3161,
              3162,
              3163,
              3164,
              3165,
              3166,
              3167,
              3168,
              3169,
              3170,
              3171,
              3172,
              3173,
              3174,
              3175,
              3176,
              3177,
              3178,
              3179,
              3180,
              3181,
              3182,
              3183,
              3184,
              3185,
              3186,
              3187,
              3188,
              3189,
              3190,
              3191,
              3192,
              3193,
              3194,
              3195,
              3196,
              3197,
              3198,
              3199,
              3200,
              3201,
              3202,
              3203,
              3228,
              3229,
              3230,
              3232,
              3233,
              3234,
              3235,
              3236,
              3238,
              3239,
              3242,
              3243,
              3244,
              3245,
              3246,
              3247,
              3248,
              3249,
              3250,
              3251,
              3252,
              3253,
              3254,
              3255,
              3256,
              3257,
              3258,
              3259,
              3260,
              3261,
              3262,
              3263,
              3264,
              3265,
              3266,
              3267,
              3268,
              3269,
              3270,
              3271,
              3272,
              3273,
              3274,
              3275,
              3276,
              3277,
              3278,
              3279,
              3280,
              3281,
              3282,
              3283,
              3284,
              3285,
              3286,
              3287,
              3288,
              3289,
              3290,
              3291,
              3292,
              3293,
              3294,
              3295,
              3296,
              3297,
              3298,
              3299,
              3300,
              3301,
              3302,
              3303,
              3304,
              3305,
              3306,
              3307,
              3308,
              3309,
              3310,
              3311,
              3312,
              3313,
              3314,
              3315,
              3316,
              3317,
              3318,
              3319,
              3320,
              3321,
              3322,
              3323,
              3324,
              3325,
              3326,
              3327,
              3328,
              3329,
              3330,
              3331,
              3332,
              3333,
              3334,
              3335,
              3336,
              3337,
              3338,
              3339,
              3340,
              3341,
              3342,
              3343,
              3344,
              3345,
              3346,
              3347,
              3348,
              3349,
              3350,
              3351,
              3352,
              3353,
              3354,
              3355,
              3356,
              3357,
              3358,
              3359,
              3360,
              3361,
              3362,
              3363,
              3364,
              3365,
              3366,
              3367,
              3368,
              3369,
              3370,
              3371,
              3372,
              3373,
              3374,
              3375,
              3376,
              3377,
              3378,
              3379,
              3380,
              3381,
              3382,
              3383,
              3384,
              3385,
              3386,
              3387,
              3388,
              3389,
              3390,
              3391,
              3392,
              3393,
              3394,
              3395,
              3396,
              3397,
              3398,
              3399,
              3400,
              3401,
              3402,
              3403,
              3404,
              3405,
              3406,
              3407,
              3408,
              3409,
              3410,
              3411,
              3412,
              3413,
              3414,
              3415,
              3416,
              3417,
              3418,
              3419,
              3420,
              3421,
              3422,
              3423,
              3424,
              3425,
              3426,
              3427,
              3428,
              3429,
              3430,
              3431,
              3432,
              3433,
              3434,
              3435,
              3436,
              3437,
              3438,
              3439,
              3440,
              3441,
              3442,
              3443,
              3444,
              3445,
              3446,
              3447,
              3448,
              3449,
              3450,
              3451,
              3452,
              3453,
              3454,
              3455,
              3456,
              3457,
              3458,
              3459,
              3460,
              3461,
              3462,
              3463,
              3464,
              3465,
              3466,
              3467,
              3468,
              3469,
              3470,
              3471,
              3472,
              3473,
              3474,
              3475,
              3476,
              3477,
              3478,
              3479,
              3480,
              3481,
              3482,
              3483,
              3484,
              3485,
              3486,
              3487,
              3488,
              3489,
              3490,
              3491,
              3492,
              3493,
              3494,
              3495,
              3496,
              3497,
              3498,
              3499,
              3500,
              3501,
              3502,
              3503,
              3504,
              3505,
              3506,
              3507,
              3508,
              3509,
              3510,
              3511,
              3512,
              3513,
              3514,
              3515,
              3516,
              3517,
              3518,
              3519,
              3520,
              3521,
              3522,
              3523,
              3524,
              3525,
              3526,
              3527,
              3528,
              3529,
              3530,
              3531,
              3532,
              3533,
              3534,
              3535,
              3536,
              3537,
              3538,
              3539,
              3540,
              3541,
              3543,
              3544,
              3545,
              3546,
              3547,
              3548,
              3549,
              3550,
              3551,
              3552,
              3553,
              3554,
              3555,
              3556,
              3557,
              3558,
              3559,
              3560,
              3561,
              3562,
              3563,
              3564,
              3565,
              3566,
              3567,
              3568,
              3569,
              3570,
              3571,
              3572,
              3573,
              3574,
              3575,
              3576,
              3577,
              3578,
              3579,
              3580,
              3581,
              3582,
              3583,
              3584,
              3585,
              3586,
              3587,
              3588,
              3589,
              3590,
              3591,
              3592,
              3593,
              3594,
              3595,
              3596,
              3597,
              3598,
              3599,
              3600,
              3601,
              3602,
              3603,
              3604,
              3605,
              3606,
              3607,
              3608,
              3609,
              3610,
              3611,
              3612,
              3613,
              3614,
              3615,
              3616,
              3617,
              3618,
              3619,
              3620,
              3621,
              3622,
              3623,
              3624,
              3625,
              3626,
              3627,
              3628,
              3629,
              3630,
              3631,
              3632,
              3633,
              3634,
              3635,
              3636,
              3637,
              3638,
              3639,
              3640,
              3641,
              3642,
              3643,
              3644,
              3645,
              3646,
              3647,
              3648,
              3649,
              3650,
              3651,
              3652,
              3653,
              3654,
              3655,
              3656,
              3657,
              3658,
              3659,
              3660,
              3661,
              3662,
              3663,
              3664,
              3665,
              3666,
              3667,
              3668,
              3669,
              3670,
              3671,
              3672,
              3673,
              3674,
              3675,
              3676,
              3677,
              3678,
              3679,
              3680,
              3681,
              3682,
              3683,
              3684,
              3685,
              3686,
              3687,
              3688,
              3689,
              3690,
              3691,
              3692,
              3850,
              3851,
              3852,
              3853,
              3854,
              3855,
              3856,
              3857,
              3858,
              3859,
              3860,
              3861,
              3862,
              3863,
              3864,
              3865,
              3866,
              3867,
              3868,
              3869,
              3870,
              3871,
              3872,
              3873,
              3874,
              3875,
              3876,
              3877,
              3878,
              3879,
              3880,
              3881,
              3882,
              3883,
              3884,
              3885,
              3886,
              3887,
              3888,
              3889,
              3890,
              3891,
              3892,
              3893,
              3894,
              3895,
              3896,
              3900,
              3901,
              3902,
              3903,
              3904,
              3905,
              3906,
              3907,
              3908,
              3909,
              3910,
              3911,
              3912,
              3913,
              3914,
              3915,
              3916,
              3917,
              3918,
              3919,
              3920,
              3921,
              3922,
              3923,
              3924,
              3925,
              3926,
              3927,
              3928,
              3929,
              3930,
              3931,
              3932,
              3933,
              3934,
              3935,
              3936,
              3937,
              3938,
              3939,
              3940,
              3941,
              3942,
              3943,
              3944,
              3945,
              3946,
              3947,
              3948,
              3949,
              3950,
              3951,
              3952,
              3953,
              3954,
              3955,
              3956,
              3957,
              3958,
              3959,
              3960,
              3961,
              3962,
              3963,
              3964,
              3965,
              3966,
              3967,
              3968,
              3969,
              3970,
              3971,
              3972,
              3973,
              3974,
              3975,
              3976,
              3977,
              3978,
              3979,
              3980,
              3981,
              3982,
              3983,
              3984,
              3985,
              3986,
              3987,
              3988,
              3989,
              3990,
              3991,
              3992,
              3993,
              3994,
              3995,
              3996,
              3997,
              3998,
              3999,
              4000,
              4001,
              4500,
              4501,
              4502,
              4503,
              4504,
              4505,
              4506,
              4507,
              4508,
              4509,
              4510,
              4511,
              4512,
              4513,
              4514,
              4515,
              4516,
              4517,
              4518,
              4519,
              4520,
              4521,
              4522,
              4523,
              4524,
              4525,
              4526,
              4527,
              4528,
              4529,
              4530,
              4531,
              4532,
              4533,
              4534,
              4535,
              4536,
              4537,
              4538,
              4539,
              4540,
              4541,
              4542,
              4543,
              4544,
              4545,
              4546,
              4547,
              4548,
              4549,
              4550,
              4551,
              4552,
              4553,
              4554,
              4555,
              4556,
              4557,
              4558,
              4559,
              4560,
              4800,
              4801,
              4802,
              4803,
              4804,
              4805,
              4806,
              4807,
              4808,
              4809,
              4810,
              4811,
              4812,
              4813,
              4814,
              4815,
              4816,
              4817,
              4818,
              4819,
              4820,
              4821,
              4822,
              4823,
              4824,
              4825,
              4826,
              4827,
              4828,
              4829,
              4830,
              4831,
              4832,
              4833,
              4834,
              4835,
              4836,
              4837,
              4838,
              4839,
              4840,
              4841,
              4842,
              4843,
              4844,
              4845,
              4846,
              4847,
              5510,
              5511,
              5512,
              5513,
              5514,
              5515,
              5516,
              5517,
              5518,
              5519,
              5520,
              5521,
              5522,
              5523,
              5524,
              5525,
              5526,
              5527,
              5528,
              5529,
              5530,
              5531,
              5532,
              5533,
              5534,
              5535,
              5536,
              5537,
              5538,
              5539,
              5540,
              5541,
              5542,
              5543,
              5544,
              5545,
              5546,
              5547,
              5548,
              5549,
              5550,
              5551,
              5552,
              5553,
              5554,
              5555,
              5556,
              5557,
              6000,
              6001,
              6002,
              6003,
              6004,
              6005,
              6006,
              6007,
              6008,
              6009,
              6010,
              6011,
              6012,
              6013,
              6014,
              6015,
              6016,
              6017,
              6018,
              6019,
              6020,
              6021,
              6022,
              6023,
              6024,
              6025,
              6026,
              6027,
              6028,
              6029,
              6030,
              6031,
              6032,
              6033,
              6034,
              6035,
              6036,
              6037,
              6038,
              6039,
              6040,
              6041,
              6042,
              6043,
              6044,
              6045,
              6046,
              6047,
              6048,
              6049,
              6050,
              6051,
              6052,
              6053,
              6054,
              6055,
              6056,
              6057,
              6058,
              6059,
              6060,
              6061,
              6062,
              6063,
              6064,
              6065,
              6066,
              6067,
              6068,
              6069,
              6070,
              6072,
              6073,
              6074,
              6075,
              6076,
              6077,
              6078,
              6079,
              6080,
              6081,
              6082,
              6083,
              6084,
              6085,
              6086,
              6087,
              6088,
              6089,
              6090,
              6091,
              6092,
              6093,
              6094,
              6095,
              6096,
              6097,
              6098,
              6099,
              6100,
              6101,
              6102,
              6103,
              6104,
              6105,
              6106,
              6107,
              6108,
              6109,
              6110,
              6111,
              6112,
              6113,
              6114,
              6115,
              6116,
              6117,
              6118,
              6119,
              6120,
              6121,
              6122,
              6123,
              6124,
              6125,
              6126,
              6127,
              6128,
              6129,
              6130,
              6131,
              6132,
              6133,
              6134,
              6135,
              6136,
              6137,
              6138,
              6139,
              6140,
              6141,
              6142,
              6143,
              6144,
              6145,
              6146,
              6147,
              6148,
              6149,
              6150,
              6151,
              6152,
              6153,
              6154,
              6155,
              6156,
              6157,
              6158,
              6159,
              6160,
              6161,
              6162,
              6163,
              6164,
              6165,
              6166,
              6167,
              6168,
              6169,
              6170,
              6171,
              6172,
              6173,
              6174,
              6175,
              6176,
              6177,
              6178,
              6179,
              6180,
              6181,
              6182,
              6183,
              6184,
              6185,
              6186,
              6187,
              6188,
              6189,
              6190,
              6191,
              6192,
              6193,
              6194,
              6195,
              6196,
              6197,
              6198,
              6199,
              6200,
              6201,
              6202,
              6203,
              6204,
              6205,
              6206,
              6207,
              6208,
              6209,
              6210,
              6211,
              6212,
              6213,
              6214,
              6215,
              6216,
              6217,
              6218,
              6219,
              6220,
              6221,
              6222,
              6223,
              6224,
              6225,
              6226,
              6227,
              6228,
              6229,
              6230,
              6231,
              6232,
              6233,
              6234,
              6235,
              6236,
              6237,
              6238,
              6239,
              6240,
              6241,
              6242,
              6243,
              6244,
              6245,
              6246,
              6247,
              6248,
              6249,
              6250,
              6251,
              6252,
              6253,
              6254,
              6255,
              6256,
              6257,
              6258,
              6259,
              6260,
              6261,
              6262,
              6263,
              6264,
              6265,
              6266,
              6267,
              6268,
              6269,
              6270,
              6271,
              6272,
              6273,
              6274,
              6275,
              6276,
              6277,
              6278,
              6279,
              6280,
              6281,
              6282,
              6283,
              6284,
              6285,
              6286,
              6287,
              6288,
              6289,
              6290,
              6291,
              6292,
              6293,
              6294,
              6295,
              6296,
              6297,
              6298,
              6299,
              6300,
              6301,
              6302,
              6303,
              6304,
              6305,
              6306,
              6307,
              6308,
              6309,
              6310,
              6311,
              6312,
              6313,
              6314,
              6315,
              6316,
              6317,
              6318,
              6319,
              6320,
              6321,
              6322,
              6323,
              6324,
              6325,
              6326,
              6327,
              6328,
              6329,
              6330,
              6331,
              6332,
              6333,
              6334,
              6335,
              6336,
              6337,
              6338,
              6339,
              6340,
              6341,
              6342,
              6343,
              6344,
              6345,
              6346,
              6347,
              6348,
              6349,
              6350,
              6351,
              6352,
              6353,
              6354,
              6355,
              6356,
              6357,
              6358,
              6359,
              6360,
              6361,
              6362,
              6363,
              6364,
              6365,
              6366,
              6367,
              6368,
              6369,
              6370,
              6371,
              6372,
              6373,
              6374,
              6375,
              6376,
              6377,
              6378,
              6379,
              6380,
              6381,
              6382,
              6383,
              6384,
              6385,
              6386,
              6387,
              6388,
              6389,
              6390,
              6391,
              6392,
              6393,
              6394,
              6395,
              6396,
              6397,
              6398,
              6399,
              6400,
              6401,
              6402,
              6403,
              6404,
              6405,
              6406,
              6407,
              6408,
              6409,
              6410,
              6411,
              6412,
              6413,
              6414,
              6415,
              6416,
              6417,
              6418,
              6419,
              6420,
              6421,
              6422,
              6423,
              6424,
              6425,
              6426,
              6427,
              6428,
              6429,
              6430,
              6431,
              6432,
              6433,
              6434,
              6435,
              6436,
              6437,
              6438,
              6439,
              6440,
              6441,
              6442,
              6443,
              6444,
              6445,
              6446,
              6447,
              6448,
              6449,
              6450,
              6451,
              6452,
              6453,
              6454,
              6455,
              6456,
              6457,
              6458,
              6459,
              6460,
              6461,
              6462,
              6463,
              6464,
              6465,
              6466,
              6467,
              6468,
              6469,
              6470,
              6471,
              6472,
              6473,
              6474,
              6475,
              6476,
              6477,
              6478,
              6479,
              6480,
              6481,
              6482,
              6483,
              6484,
              6485,
              6486,
              6487,
              6488,
              6489,
              6490,
              6491,
              6492,
              6493,
              6494,
              6495,
              6496,
              6497,
              6498,
              6499,
              6500,
              6501,
              6502,
              6503,
              6504,
              6505,
              6506,
              6507,
              6508,
              6509,
              6510,
              6511,
              6512,
              6513,
              6514,
              6515,
              6516,
              6517,
              6518,
              6519,
              6520,
              6521,
              6522,
              6523,
              6524,
              6525,
              6526,
              6527,
              6528,
              6529,
              6530,
              6531,
              6532,
              6533,
              6534,
              6535,
              6536,
              6537,
              6538,
              6539,
              6540,
              6541,
              6542,
              6543,
              6544,
              6545,
              6546,
              6547,
              6548,
              6549,
              6550,
              6551,
              6552,
              6553,
              6554,
              6555,
              6556,
              6557,
              6558,
              6559,
              6560,
              6561,
              6562,
              6563,
              6564,
              6565,
              6566,
              6567,
              6568,
              6569,
              6570,
              6571,
              6572,
              6573,
              6574,
              6575,
              6576,
              6577,
              6578,
              6579,
              6580,
              6581,
              6582,
              6583,
              6584,
              6585,
              6586,
              6587,
              6588,
              6589,
              6590,
              6591,
              6592,
              6593,
              6594,
              6595,
              6596,
              6597,
              6598,
              6599,
              6600,
              6601,
              6602,
              6603,
              6604,
              6605,
              6606,
              6607,
              6608,
              6609,
              6610,
              6611,
              6612,
              6613,
              6614,
              6615,
              6616,
              6617,
              6618,
              6619,
              6620,
              6621,
              6622,
              6623,
              6624,
              6625,
              6626,
              6627,
              6628,
              6629,
              6630,
              6631,
              6632,
              6633,
              6634,
              6635,
              6636,
              6637,
              6638,
              6639,
              6640,
              6641,
              6642,
              6643,
              6644,
              6645,
              6646,
              6647,
              6648,
              6649,
              6650,
              6651,
              6652,
              6653,
              6654,
              6655,
              6656,
              6657,
              6658,
              6659,
              6660,
              6661,
              6662,
              6663,
              6664,
              6665,
              6666,
              6667,
              6668,
              6669,
              6670,
              6671,
              6672,
              6673,
              6674,
              6675,
              6676,
              6677,
              6678,
              6679,
              6680,
              6681,
              6682,
              6683,
              6684,
              6685,
              6686,
              6687,
              6688,
              6689,
              6690,
              6691,
              6692,
              6693,
              6694,
              6695,
              6696,
              6697,
              6698,
              6699,
              6700,
              6701,
              6702,
              6703,
              6704,
              6705,
              6706,
              6707,
              6708,
              6709,
              6710,
              6711,
              6712,
              6713,
              6714,
              6715,
              6716,
              6717,
              6718,
              6719,
              6720,
              6721,
              6722,
              6723,
              6724,
              6725,
              6726,
              6727,
              6728,
              6729,
              6730,
              6731,
              6732,
              6733,
              6734,
              6735,
              6736,
              6737,
              6738,
              6739,
              6740,
              6741,
              6742,
              6743,
              6744,
              6745,
              6746,
              6747,
              6748,
              6749,
              6750,
              6751,
              6752,
              6753,
              6754,
              6755,
              6756,
              6757,
              6758,
              6759,
              6760,
              6761,
              6762,
              6763,
              6764,
              6765,
              6766,
              6767,
              6768,
              6769,
              6770,
              6771,
              6772,
              6773,
              6774,
              6775,
              6776,
              6777,
              6778,
              6779,
              6780,
              6781,
              6782,
              6783,
              6784,
              6785,
              6786,
              6787,
              6788,
              6789,
              6790,
              6791,
              6792,
              6793,
              6794,
              6795,
              6796,
              6797,
              6798,
              6799,
              6800,
              6801,
              6802,
              6803,
              6804,
              6805,
              6806,
              6807,
              6808,
              6809,
              6810,
              6811,
              6812,
              6813,
              6814,
              6815,
              6816,
              6817,
              6818,
              6819,
              6820,
              6821,
              6822,
              6823,
              6824,
              6825,
              6826,
              6827,
              6828,
              6829,
              6830,
              6831,
              6832,
              6833,
              6834,
              6835,
              6836,
              6837,
              6838,
              6839,
              6840,
              6841,
              6842,
              6843,
              6844,
              6845,
              6846,
              6847,
              6848,
              6849,
              6850,
              6851,
              6852,
              6853,
              6854,
              6855,
              6856,
              6857,
              6858,
              6859,
              6860,
              6861,
              6862,
              6863,
              6864,
              6865,
              6866,
              6867,
              6868,
              6869,
              6870,
              6871,
              6872,
              6873,
              6874,
              6875,
              6876,
              6877,
              6878,
              6879,
              6880,
              6881,
              6882,
              6883,
              6884,
              6885,
              6886,
              6887,
              6888,
              6889,
              6890,
              6891,
              6892,
              6893,
              6894,
              6895,
              6896,
              6897,
              6898,
              6899,
              6900,
              6901,
              6902,
              6903,
              6904,
              6905,
              6906,
              6907,
              6908,
              6909,
              6910,
              6911,
              6912,
              6913,
              6914,
              6915,
              6916,
              6917,
              6918,
              6919,
              6920,
              6921,
              6922,
              6923,
              6924,
              6925,
              6926,
              6927,
              6928,
              6929,
              6930,
              6931,
              6932,
              6933,
              6934,
              6935,
              6936,
              6937,
              6938,
              6939,
              6940,
              6941,
              6942,
              6943,
              6944,
              6945,
              6946,
              6947,
              6948,
              6949,
              6950,
              6951,
              6952,
              6953,
              6954,
              6955,
              6956,
              6957,
              6958,
              6959,
              6960,
              6961,
              6962,
              6963,
              6964,
              6965,
              6966,
              6967,
              6968,
              6969,
              6970,
              6971,
              6972,
              6973,
              6974,
              6975,
              6976,
              6977,
              6978,
              6979,
              6980,
              6981,
              6982,
              6983,
              6984,
              6985,
              6986,
              6987,
              6988,
              6989,
              6990,
              6991,
              7200,
              7201,
              7202,
              7220,
              7221,
              7222,
              7223,
              7224,
              7225,
              7226,
              7227,
              7228,
              7229,
              7230,
              7231,
              7232,
              7233,
              7234,
              7235,
              7236,
              7237,
              7238,
              7239,
              7240,
              7241,
              7242,
              7243,
              7244,
              7245,
              7246,
              7247,
              7248,
              7249,
              7250,
              7251,
              7252,
              7253,
              7254,
              7255,
              7256,
              7257,
              7258,
              7259,
              7260,
              7261,
              7262,
              7263,
              7264,
              7265,
              7266,
              7267,
              7268,
              7269,
              7270,
              7271,
              7272,
              7273,
              7274,
              7275,
              7276,
              7277,
              7278,
              7279,
              7280,
              7281,
              7282,
              7283,
              7284,
              7285,
              7286,
              7287,
              7288,
              7289,
              7290,
              7291,
              7292,
              7293,
              7294,
              7295,
              7296,
              7297,
              7298,
              7299,
              7300,
              7301,
              7302,
              7303,
              7304,
              7305,
              7306,
              7307,
              7308,
              7309,
              7310,
              7311,
              7312,
              7313,
              7314,
              7315,
              7316,
              7317,
              7318,
              7319,
              7320,
              7321,
              7322,
              7323,
              7324,
              7325,
              7326,
              7327,
              7328,
              7329,
              7330,
              7331,
              7332,
              7333,
              7334,
              7335,
              7336,
              7337,
              7338,
              7339,
              7340,
              7341,
              7342,
              7343,
              7344,
              7345,
              7346,
              7347,
              7348,
              7349,
              7350,
              7351,
              7352,
              7353,
              7354,
              7355,
              7356,
              7357,
              7358,
              7359,
              7360,
              7361,
              7362,
              7363,
              7364,
              7365,
              7366,
              7367,
              7368,
              7369,
              7370,
              7371,
              7372,
              7373,
              7374,
              7375,
              7376,
              7377,
              7378,
              7379,
              7380,
              7381,
              7382,
              7383,
              7384,
              7385,
              7386,
              7387,
              7388,
              7389,
              7390,
              7391,
              7392,
              7393,
              7394,
              7395,
              7396,
              7397,
              7398,
              7399,
              7400,
              7401,
              7402,
              7403,
              7404,
              7405,
              7406,
              7407,
              7408,
              7409,
              7410,
              7411,
              7412,
              7413,
              7414,
              7415,
              7416,
              7417,
              7418,
              7419,
              7420,
              7421,
              7422,
              7423,
              7424,
              7425,
              7426,
              7427,
              7428,
              7429,
              7430,
              7431,
              7432,
              7433,
              7434,
              7435,
              7436,
              7437,
              7438,
              7439,
              7440,
              7441,
              7442,
              7443,
              7444,
              7445,
              7446,
              7447,
              7448,
              7449,
              7450,
              7451,
              7452,
              7453,
              7454,
              7455,
              7456,
              7457,
              7458,
              7459,
              7460,
              7461,
              7462,
              7463,
              7464,
              7465,
              7466,
              7467,
              7468,
              7469,
              7470,
              7471,
              7472,
              7473,
              7474,
              7475,
              7476,
              7477,
              7478,
              7479,
              7480,
              7481,
              7482,
              7483,
              7484,
              7485,
              7486,
              7487,
              7488,
              7489,
              7490,
              7491,
              7492,
              7493,
              7494,
              7495,
              7496,
              7497,
              7498,
              7499,
              7500,
              7501,
              7502,
              7503,
              7504,
              7505,
              7506,
              7507,
              7508,
              7509,
              7510,
              7511,
              7512,
              7513,
              7514,
              7515,
              7516,
              7517,
              7518,
              7519,
              7520,
              7521,
              7522,
              7523,
              7524,
              7525,
              7526,
              7527,
              7528,
              7529,
              7530,
              7531,
              7532,
              7533,
              7534,
              7535,
              7536,
              7537,
              7538,
              7539,
              7540,
              7541,
              7542,
              7543,
              7544,
              7546,
              7547,
              7548,
              7549,
              7550,
              7551,
              7552,
              7553,
              7554,
              7555,
              7556,
              7557,
              7558,
              7559,
              7560,
              7561,
              7562,
              7563,
              7564,
              7565,
              7566,
              7567,
              7568,
              7569,
              7570,
              7571,
              7572,
              7573,
              7574,
              7575,
              7576,
              7577,
              7578,
              7579,
              7580,
              7581,
              7582,
              7583,
              7584,
              7585,
              7586,
              7587,
              7588,
              7589,
              7590,
              7591,
              7592,
              7593,
              7594,
              7595,
              7596,
              7597,
              7598,
              7599,
              7601,
              7602,
              7603,
              7604,
              7605,
              7606,
              7607,
              7608,
              7609,
              7610,
              7611,
              7612,
              7613,
              7614,
              7615,
              7616,
              7617,
              7618,
              7619,
              7620,
              7621,
              7622,
              7623,
              7624,
              7625,
              7626,
              7627,
              7628,
              7629,
              7630,
              7631,
              7632,
              7633,
              7634,
              7635,
              7636,
              7637,
              7638,
              7639,
              7640,
              7641,
              7642,
              7643,
              7644,
              7645,
              7646,
              7647,
              7648,
              7649,
              7650,
              7651,
              7652,
              7653,
              7654,
              7655,
              7656,
              7657,
              7658,
              7659,
              7660,
              7661,
              7662,
              7663,
              7664,
              7665,
              7666,
              7667,
              7668,
              7669,
              7670,
              7671,
              7672,
              7673,
              7674,
              7675,
              7676,
              7677,
              7678,
              7679,
              7680,
              7681,
              7682,
              7683,
              7684,
              7685,
              7686,
              7687,
              7688,
              7689,
              7690,
              7691,
              7692,
              7693,
              7694,
              7695,
              7696,
              7697,
              7698,
              7699,
              7700,
              7701,
              7702,
              7703,
              7704,
              7705,
              7706,
              7707,
              7708,
              7709,
              7710,
              7711,
              7712,
              7713,
              7714,
              7715,
              7716,
              7717,
              7719,
              7720,
              7721,
              7722,
              7723,
              7724,
              7725,
              7726,
              7727,
              7728,
              7729,
              7730,
              7731,
              7732,
              7733,
              7734,
              7735,
              7736,
              7737,
              7738,
              7739,
              7740,
              7741,
              7742,
              7743,
              7744,
              7746,
              7747,
              7748,
              7749,
              7750,
              7751,
              7753,
              7754,
              7755,
              7756,
              7757,
              7758,
              7759,
              7760,
              7761,
              7762,
              7763,
              7764,
              7765,
              7766,
              7767,
              7768,
              7769,
              7770,
              7771,
              7772,
              7773,
              7775,
              7776,
              7777,
              7778,
              7779,
              7780,
              7781,
              7782,
              7783,
              7784,
              7785,
              7786,
              7787,
              7788,
              7789,
              7799,
              7800,
              7801,
              7802,
              7803,
              7804,
              7805,
              7806,
              7807,
              7808,
              7809,
              7810,
              7811,
              7812,
              7813,
              7814,
              7815,
              7816,
              7817,
              7818,
              7819,
              7820,
              7821,
              7822,
              7823,
              7824,
              7825,
              7826,
              7827,
              7828,
              7829,
              7830,
              7831,
              7832,
              7833,
              7834,
              7835,
              7836,
              7837,
              7838,
              7839,
              7840,
              7841,
              7842,
              7843,
              7844,
              7845,
              7846,
              7847,
              7848,
              7849,
              7850,
              7851,
              7852,
              7853,
              7854,
              7855,
              7856,
              7857,
              7858,
              7859,
              7860,
              7861,
              7862,
              7863,
              7864,
              7865,
              7866,
              7867,
              7868,
              7869,
              7870,
              7871,
              7872,
              7873,
              7874,
              7875,
              7876,
              7877,
              7878,
              7879,
              7880,
              7881,
              7882,
              7883,
              7884,
              7885,
              7886,
              7887,
              7888,
              7889,
              7890,
              7891,
              7892,
              7893,
              7894,
              7895,
              7896,
              7897,
              7898,
              7899,
              7900,
              7901,
              7902,
              7903,
              7904,
              8000,
              8001,
              8002,
              8003,
              8004,
              8005,
              8006,
              8007,
              8008,
              8009,
              8010,
              8011,
              8012,
              8013,
              8014,
              8015,
              8016,
              8017,
              8018,
              8019,
              8020,
              8021,
              8022,
              8023,
              8024,
              8025,
              8026,
              8027,
              8028,
              8029,
              8030,
              8031,
              8032,
              8033,
              8034,
              8035,
              8036,
              8037,
              8038,
              8039,
              8040,
              8041,
              8042,
              8043,
              8044,
              8045,
              8046,
              8047,
              8048,
              8049,
              8050,
              8051,
              8052,
              8053,
              8054,
              8055,
              8056,
              8057,
              8058,
              8059,
              8060,
              8061,
              8062,
              8063,
              8064,
              8065,
              8066,
              8067,
              8068,
              8069,
              8070,
              8071,
              8072,
              8073,
              8074,
              8075,
              8076,
              8077,
              8078,
              8079,
              8080,
              8081,
              8082,
              8083,
              8084,
              8085,
              8086,
              8087,
              8088,
              8089,
              8090,
              8091,
              8092,
              8093,
              8094,
              8095,
              8096,
              8097,
              8098,
              8099,
              8100,
              8101,
              8102,
              8103,
              8104,
              8105,
              8106,
              8107,
              8108,
              8109,
              8110,
              8111,
              8112,
              8113,
              8114,
              8115,
              8116,
              8117,
              8118,
              8119,
              8120,
              8121,
              8122,
              8123,
              8124,
              8125,
              8126,
              8127,
              8128,
              8129,
              8130,
              8131,
              8132,
              8133,
              8134,
              8135,
              8136,
              8137,
              8138,
              8139,
              8140,
              8141,
              8142,
              8143,
              8144,
              8145,
              8146,
              8147,
              8148,
              8149,
              8150,
              8151,
              8152,
              8153,
              8154,
              8155,
              8156,
              8157,
              8158,
              8159,
              8160,
              8161,
              8162,
              8163,
              8164,
              8165,
              8166,
              8167,
              8168,
              8169,
              8170,
              8171,
              8172,
              8173,
              8174,
              8175,
              8176,
              8177,
              8178,
              8179,
              8180,
              8181,
              8182,
              8183,
              8184,
              8185,
              8186,
              8187,
              8188,
              8189,
              8190,
              8191,
              8192,
              8193,
              8194,
              8195,
              8196,
              8197,
              8198,
              8199,
              8200,
              8201,
              8202,
              8203,
              8204,
              8205,
              8206,
              8207,
              8208,
              8209,
              8210,
              8211,
              8212,
              8213,
              8214,
              8215,
              8216,
              8217,
              8218,
              8219,
              8220,
              8221,
              8222,
              8223,
              8224,
              8225,
              8226,
              8227,
              8228,
              8229,
              8230,
              8231,
              8232,
              8233,
              8234,
              8235,
              8236,
              8237,
              8238,
              8239,
              8240,
              8241,
              8242,
              8243,
              8244,
              8245,
              8246,
              8247,
              8248,
              8249,
              8250,
              8251,
              8252,
              8253,
              8254,
              8255,
              8256,
              8257,
              8258,
              8259,
              8260,
              8261,
              8262,
              8263,
              8264,
              8265,
              8266,
              8267,
              8268,
              8269,
              8270,
              8271,
              8272,
              8273,
              8274,
              8275,
              8276,
              8277,
              8278,
              8279,
              8280,
              8281,
              8282,
              8283,
              8284,
              8285,
              8286,
              8287,
              8288,
              8289,
              8290,
              8291,
              8292,
              8293,
              8294,
              8295,
              8296,
              8297,
              8298,
              8299,
              8300,
              8301,
              8302,
              8303,
              8304,
              8305,
              8306,
              8307,
              8308,
              8309,
              8310,
              8311,
              8312,
              8313,
              8314,
              8315,
              8316,
              8317,
              8318,
              8319,
              8320,
              8321,
              8322,
              8323,
              8324,
              8325,
              8326,
              8327,
              8328,
              8329,
              8330,
              8331,
              8332,
              8333,
              8334,
              8335,
              8336,
              8337,
              8338,
              8339,
              8340,
              8341,
              8342,
              8343,
              8344,
              8345,
              8346,
              8347,
              8348,
              8349,
              8350,
              8351,
              8352,
              8353,
              8354,
              8355,
              8356,
              8357,
              8358,
              8359,
              8360,
              8361,
              8362,
              8363,
              8364,
              8365,
              8366,
              8367,
              8368,
              8369,
              8371,
              8372,
              8374,
              8375,
              8376,
              8377,
              8378,
              8379,
              8380,
              8381,
              8382,
              8383,
              8384,
              8385,
              8386,
              8387,
              8388,
              8389,
              8390,
              8391,
              8392,
              8393,
              8394,
              8395,
              8396,
              8397,
              8700,
              8701,
              8702,
              8703,
              8704,
              8705,
              8706,
              8707,
              8708,
              8709,
              8710,
              8711,
              8712,
              8713,
              8714,
              8715,
              8716,
              8717,
              8718,
              8719,
              8720,
              8721,
              8722,
              8723,
              8724,
              8725,
              8726,
              8727,
              8728,
              8729,
              8730,
              8731,
              8732,
              8733,
              8734,
              8735,
              8736,
              8737,
              8738,
              8739,
              8740,
              8741,
              8742,
              8743,
              8744,
              8745,
              8746,
              8747,
              8748,
              8749,
              8750,
              8751,
              8752,
              8753,
              8754,
              8755,
              8756,
              8757,
              8758,
              8759,
              8760,
              8761,
              8762,
              8763,
              8764,
              8765,
              8766,
              8767,
              8768,
              8769,
              8770,
              8771,
              8772,
              8773,
              8774,
              8775,
              8776,
              8777,
              8778,
              8779,
              8780,
              8781,
              8782,
              8783,
              8784,
              8785,
              8786,
              8787,
              8788,
              8789,
              8790,
              8791,
              8792,
              8793,
              8794,
              9000,
              9001,
              9002,
              9003,
              9004,
              9005,
              9006,
              9007,
              9008,
              9009,
              9010,
              9011,
              9012,
              9013,
              9014,
              9015,
              9016,
              9017,
              9018,
              9019,
              9020,
              9021,
              9022,
              9023,
              9024,
              9025,
              9026,
              9027,
              9028,
              9100,
              9101,
              9102,
              9103,
              9104,
              9105,
              9106,
              9107,
              9108,
              9109,
              9110,
              9111,
              9112,
              9113,
              9114,
              9115,
              9116,
              9117,
              9118,
              9119,
              9120,
              9121,
              9122,
              9123,
              9124,
              9200,
              9201,
              9202,
              9203,
              9204,
              9205,
              9206,
              9207,
              9208,
              9209,
              9210,
              9211,
              9212,
              9213,
              9214,
              9215,
              9216,
              9217,
              9218,
              9219,
              9220,
              9221,
              9222,
              9223,
              9224,
              9225,
              9226,
              9227,
              9228,
              9229,
              9230,
              9231,
              9232,
              9233,
              9234,
              9235,
              9236,
              9237,
              9238,
              9239,
              9240,
              9241,
              9242,
              9243,
              9244,
              9245,
              9246,
              9247,
              9248,
              9249,
              9250,
              9251,
              9252,
              9253,
              9254,
              9255,
              9256,
              9257,
              9258,
              9259,
              9260,
              9261,
              9262,
              9263,
              9264,
              9265,
              9266,
              9267,
              9268,
              9269,
              9270,
              9271,
              9272,
              9273,
              9274,
              9275,
              9276,
              9277,
              9278,
              9279,
              9280,
              9281,
              9282,
              9283,
              9284,
              9285,
              9286,
              9287,
              9288,
              9289,
              9290,
              9291,
              9292,
              9293,
              9294,
              9295,
              9296,
              9297,
              9298,
              9299,
              9300,
              9301,
              9302,
              9303,
              9304,
              9305,
              9306,
              9307,
              9308,
              9309,
              9310,
              9311,
              9312,
              9313,
              9314,
              9315,
              9316,
              9317,
              9318,
              9319,
              9320,
              9321,
              9322,
              9323,
              9324,
              9325,
              9326,
              9327,
              9328,
              9329,
              9330,
              9331,
              9332,
              9333,
              9334,
              9335,
              9336,
              9337,
              9338,
              9339,
              9340,
              9341,
              9342,
              9343,
              9344,
              9345,
              9346,
              9347,
              9348,
              9349,
              9350,
              9351,
              9352,
              9353,
              9354,
              9355,
              9356,
              9357,
              9358,
              9359,
              9360,
              9361,
              9362,
              9363,
              9364,
              9365,
              9366,
              9367,
              9368,
              9369,
              9370,
              9371,
              9372,
              9373,
              9374,
              9375,
              9376,
              9377,
              9378,
              9379,
              9380,
              9381,
              9382,
              9383,
              9384,
              9385,
              9386,
              9387,
              9388,
              9389,
              9390,
              9391,
              9392,
              9393,
              9394,
              9395,
              9396,
              9397,
              9398,
              9399,
              9400,
              9401,
              9402,
              9403,
              9404,
              9405,
              9406,
              9407,
              9408,
              9409,
              9410,
              9411,
              9412,
              9413,
              9414,
              9415,
              9416,
              9417,
              9418,
              9419,
              9420,
              9421,
              9422,
              9423,
              9424,
              9425,
              9426,
              9427,
              9428,
              9429,
              9430,
              9431,
              9432,
              9433,
              9434,
              9435,
              9436,
              9437,
              9438,
              9439,
              9440,
              9441,
              9442,
              9443,
              9444,
              9445,
              9446,
              9447,
              9448,
              9449,
              9450,
              9451,
              9452,
              9453,
              9454,
              9455,
              9456,
              9457,
              9458,
              9459,
              9460,
              9461,
              9462,
              9463,
              9464,
              9465,
              9466,
              9467,
              9468,
              9469,
              9470,
              9471,
              9472,
              9473,
              9475,
              9476,
              9477,
              9478,
              9479,
              9480,
              9481,
              9482,
              9483,
              9484,
              9485,
              9486,
              9487,
              9488,
              9489,
              9490,
              9491,
              9492,
              9493,
              9494,
              9495,
              9496,
              9497,
              9498,
              9499,
              9500,
              9501,
              9502,
              9503,
              9504,
              9505,
              9506,
              9507,
              9508,
              9509,
              9510,
              9511,
              9512,
              9513,
              9514,
              9515,
              9516,
              9517,
              9518,
              9519,
              9520,
              9521,
              9522,
              9523,
              9524,
              9525,
              9526,
              9527,
              9528,
              9529,
              9530,
              9531,
              9532,
              9533,
              9534,
              9535,
              9536,
              9537,
              9538,
              9539,
              9540,
              9541,
              9542,
              9543,
              9544,
              9545,
              9546,
              9547,
              9548,
              9549,
              9550,
              9551,
              9552,
              9553,
              9554,
              9555,
              9556,
              9557,
              9558,
              9559,
              9560,
              9561,
              9562,
              9563,
              9564,
              9565,
              9566,
              9567,
              9568,
              9569,
              9570,
              9571,
              9572,
              9573,
              9574,
              9575,
              9576,
              9577,
              9578,
              9579,
              9580,
              9581,
              9582,
              9583,
              9584,
              9585,
              9586,
              9587,
              9588,
              9589,
              9590,
              9591,
              9592,
              9593,
              9594,
              9595,
              9596,
              9597,
              9598,
              9599,
              9600,
              9601,
              9602,
              9603,
              9604,
              9605,
              9606,
              9607,
              9608,
              9609,
              9610,
              9611,
              9612,
              9613,
              9614,
              9615,
              9616,
              9617,
              9618,
              9619,
              9620,
              9621,
              9622,
              9667,
              9668,
              9669,
              9671,
              9672,
              9673,
              9674,
              9675,
              9676,
              9677,
              9678,
              9679,
              9680,
              9681,
              9682,
              9683,
              9684,
              9685,
              9686,
              9687,
              9688,
              9689,
              9690,
              9691,
              9692,
              9693,
              9694,
              9695,
              9696,
              9697,
              9698,
              9699,
              9700,
              9701,
              9702,
              9703,
              9704,
              9705,
              9706,
              9707,
              9708,
              9709,
              9710,
              9711,
              9712,
              9713,
              9714,
              9715,
              9716,
              9717,
              9718,
              9719,
              9720,
              9721,
              9722,
              9723,
              9724,
              9725,
              9726,
              9727,
              9728,
              9729,
              9730,
              9731,
              9732,
              9733,
              9734,
              9735,
              9736,
              9737,
              9738,
              9739,
              9740,
              9741,
              9742,
              9743,
              9744,
              9745,
              9746,
              9747,
              9748,
              9749,
              9750,
              9751,
              9752,
              9753,
              9754,
              9755,
              9756,
              9757,
              9758,
              9759,
              9760,
              9761,
              9762,
              9763,
              9764,
              9765,
              9766,
              9767,
              9768,
              9769,
              9770,
              9771,
              9772,
              9773,
              9774,
              9775,
              9776,
              9777,
              9778,
              9779,
              9780,
              9781,
              9782,
              9783,
              9784,
              9785,
              9786,
              9787,
              9788,
              9789,
              9790,
              9791,
              9792,
              9793,
              9794,
              9795,
              9796,
              9797,
              9798,
              9799,
              9800,
              9801,
              9802,
              9803,
              9804,
              9805,
              9806,
              9807,
              9808,
              9809,
              9810,
              9811,
              9812,
              9813,
              9814,
              9815,
              9816,
              9817,
              9818,
              9819,
              9820,
              9821,
              9822,
              9823,
              9824,
              9825,
              9826,
              9827,
              9828,
              9829,
              9830,
              9831,
              9832,
              9833,
              9834,
              9835,
              9836,
              9837,
              9838,
              9839,
              9840,
              9841,
              9842,
              9843,
              9844,
              9845,
              9846,
              9847,
              9848,
              9849,
              9850,
              9851,
              9852,
              9853,
              9854,
              9855,
              9856,
              9857,
              9858,
              9859,
              9860,
              9861,
              9862,
              9863,
              9864,
              9865,
              9866,
              9867,
              9868,
              9869,
              9870,
              9871,
              9872,
              9873,
              9874,
              9875,
              9876,
              9877,
              9878,
              9879,
              9880,
              9881,
              9882,
              9883,
              9884,
              9885,
              9886,
              9887,
              9888,
              9889,
              9890,
              9891,
              9892,
              9893,
              9894,
              9895,
              9896,
              9897,
              9898,
              9899,
              9900,
              9901,
              9902,
              9903,
              9904,
              9905,
              9906,
              9907,
              9908,
              9909,
              9910,
              9911,
              9912,
              9913,
              9914,
              9915,
              9916,
              9917,
              9918,
              9919,
              9920,
              9921,
              9922,
              9923,
              9924,
              9925,
              9926,
              9927,
              9928,
              9929,
              9930,
              9931,
              9932,
              9933,
              9934,
              9935,
              9936,
              9937,
              9938,
              9939,
              9940,
              9941,
              9942,
              9943,
              9944,
              9945,
              9946,
              9947,
              9948,
              9949,
              9950,
              9951,
              9952,
              9953,
              9954,
              9955,
              9956,
              9957,
              9958,
              9959,
              9960,
              9961,
              9962,
              9963,
              9964,
              9965,
              9966,
              9967,
              9968,
              9969,
              9970,
              9971,
              9972,
              9973,
              9974,
              9975,
              9976,
              9977,
              9978,
              9979,
              9980,
              9981,
              9982,
              9983,
              9984,
              9985,
              9986,
              9987,
              9988,
              9989,
              9990,
              9991,
              9992,
              9993,
              9994,
              9995,
              9996,
              9997,
              9998,
              9999,
              10000,
              10001,
              10002,
              10003,
              10004,
              10005,
              10006,
              10007,
              10008,
              10009,
              10010,
              10011,
              10012,
              10013,
              10014,
              10015,
              10016,
              10017,
              10018,
              10019,
              10020,
              10021,
              10022,
              10023,
              10024,
              10051,
              10052,
              10053,
              10054,
              10055,
              10056,
              10057,
              10058,
              10059,
              10060,
              10061)
        )
    )
    namedValues = NamedValues(
        *(("aISL", 9948),
          ("aPSLinkCommunicationFailure", 4535),
          ("aRPPause", 10061),
          ("aSELos", 10060),
          ("abnormalCondition", 1838),
          ("abnormalConditionEquip", 1848),
          ("ac1", 1788),
          ("ac2", 1789),
          ("acPowerLoss", 9269),
          ("accMisConfig", 1048),
          ("accOptFault", 1046),
          ("accPortLinkLayerDown", 6634),
          ("accPortLoopDetected", 6635),
          ("accPortPhysLayerDown", 6636),
          ("accSfpMismatch", 1047),
          ("accountExpiredDisabled", 9527),
          ("acd", 1),
          ("acgPrealarm", 6002),
          ("acmT0", 2),
          ("acoopr", 3982),
          ("activeLoop", 976),
          ("adapterError", 3),
          ("adapterError2", 4),
          ("adapterError3", 5),
          ("adjacencyLost", 9956),
          ("advaais", 3900),
          ("advaaisl", 3998),
          ("advaaisp", 3858),
          ("advaaisv", 3872),
          ("advaclockfail", 3984),
          ("advacsf", 3885),
          ("advadegl", 3856),
          ("advadegp", 3865),
          ("advadegv", 3878),
          ("advaexcl", 3855),
          ("advaexcp", 3864),
          ("advaexcv", 3877),
          ("advaidle", 3884),
          ("advaloa", 3996),
          ("advalof", 3931),
          ("advalomp", 3863),
          ("advalopp", 3859),
          ("advalopv", 3873),
          ("advalos", 3932),
          ("advamnd", 3871),
          ("advaplcr", 3852),
          ("advaplct", 3850),
          ("advaplmp", 3862),
          ("advaplmv", 3876),
          ("advarai", 3882),
          ("advarei", 3883),
          ("advareil", 3854),
          ("advareip", 3866),
          ("advareiv", 3879),
          ("advarfi", 3938),
          ("advarfil", 3999),
          ("advarfip", 3867),
          ("advarfiv", 3880),
          ("advasfpinserted", 3959),
          ("advasfpmismatch", 3960),
          ("advasfpnonqualified", 3961),
          ("advasfpremoved", 3962),
          ("advasfptxfault", 3963),
          ("advasqm", 3869),
          ("advatimp", 3860),
          ("advatims", 3857),
          ("advatimv", 3874),
          ("advatlcr", 3853),
          ("advatlct", 3851),
          ("advauneqp", 3861),
          ("advauneqv", 3875),
          ("advaxfpmismatch", 3979),
          ("advaxfpnonqualified", 3980),
          ("advaxfpremoved", 3981),
          ("advaxfptxfault", 3978),
          ("agc", 6001),
          ("agcFailureProtSide", 6629),
          ("airCompressorFail", 9200),
          ("airCompressorFailure", 6),
          ("airConditioningFail", 9201),
          ("airConditioningFailure", 7),
          ("airDryerFail", 9202),
          ("airDryerFailure", 8),
          ("airDustFilterClogged", 3600),
          ("airFilterExchangeRequired", 793),
          ("ais", 9),
          ("ais10Inserted", 6003),
          ("ais11Inserted", 6004),
          ("ais12Inserted", 6005),
          ("ais13Inserted", 6006),
          ("ais14Inserted", 6007),
          ("ais15Inserted", 6008),
          ("ais16Inserted", 6009),
          ("ais1Inserted", 6010),
          ("ais2Inserted", 6011),
          ("ais3Inserted", 6012),
          ("ais4Inserted", 6013),
          ("ais5Inserted", 6014),
          ("ais6Inserted", 6015),
          ("ais7Inserted", 6016),
          ("ais8Inserted", 6017),
          ("ais9Inserted", 6018),
          ("aisA1", 10),
          ("aisB1", 11),
          ("aisInBitsPrimaryReference", 6805),
          ("aisInBitsSecondaryRef", 6809),
          ("aisInsertedOnAllTribs", 6019),
          ("aisInsertedUserSide", 6020),
          ("aisProtSide", 6603),
          ("aisReceived", 6498),
          ("aisSsf", 12),
          ("aisuk2", 13),
          ("alarmAIS", 3309),
          ("alarmAISVvirtualtributarypath", 2291),
          ("alarmAPSCONF", 3034),
          ("alarmASE-tab-gen-failed-PILOT", 3604),
          ("alarmAUAIS", 3311),
          ("alarmAULOP", 3312),
          ("alarmAlarmIndicationSignalOduTcmA", 3057),
          ("alarmAlarmIndicationSignalOduTcmB", 3058),
          ("alarmAlarmIndicationSignalOduTcmC", 3157),
          ("alarmAlsPulsesReceived", 3011),
          ("alarmApsProtocolFailure", 3037),
          ("alarmAttOnReceiverFiberHigherThanMonitor", 3041),
          ("alarmAttOnReceiverFiberLowerThanMonitor", 3040),
          ("alarmAutoShutdownLaserOffDueToErrFwd", 3115),
          ("alarmAutoShutdownTxRxLasersDueToHighTemp", 3660),
          ("alarmAutomaticShutdownByAisOdu", 3026),
          ("alarmAutomaticShutdownByAisOtu", 3022),
          ("alarmAutomaticShutdownbyEPC", 3035),
          ("alarmB1BIPS", 2276),
          ("alarmB1BIPSTCA", 2279),
          ("alarmB2BIPL", 2277),
          ("alarmB2BIPLTCA", 2280),
          ("alarmB3BIPPHigherOrderPath", 2287),
          ("alarmB3BIPPTCAHigherOrderPath", 2289),
          ("alarmB3BIPVTCAvirtualtributarypath", 2306),
          ("alarmB3BIPVvirtualtributarypath", 2302),
          ("alarmB3REIVTCAvirtualtributarypath", 2304),
          ("alarmB3REIVvirtualtributarypath", 2300),
          ("alarmBackwardDefectIndicationOdu", 3032),
          ("alarmBackwardDefectIndicationOduTcmA", 3069),
          ("alarmBackwardDefectIndicationOduTcmB", 3070),
          ("alarmBackwardDefectIndicationOduTcmC", 3162),
          ("alarmBackwardDefectIndicationOtu", 3025),
          ("alarmCRY-PWcannotBeEntered", 3592),
          ("alarmCardRemoved", 3007),
          ("alarmCurrentTooHigh", 3004),
          ("alarmCurrentTooLow", 3003),
          ("alarmDispertionTunningCondition", 3549),
          ("alarmE3T3LINEPCBITS", 2311),
          ("alarmENETDROPFRTCA", 2309),
          ("alarmENETFCEERROR", 2308),
          ("alarmEncryptionModuleFwpUpdateEnabled", 3661),
          ("alarmEncryptionModuleSelfTestFail", 3663),
          ("alarmEncryptionModuleSelfTestFailCritical", 3664),
          ("alarmEncryptionModuleSelfTestStarted", 3662),
          ("alarmEncryptionPortEncryptionSwitchOffEnabled", 3665),
          ("alarmEquipmentMismatch", 3177),
          ("alarmEquipmentMismatchAllowRzs", 9880),
          ("alarmEquipmentNotAccepted", 3175),
          ("alarmEquipmentNotApproved", 3176),
          ("alarmEquipmentNotSupportedByPhysicalLayer", 3081),
          ("alarmExternalInput1", 3254),
          ("alarmExternalInput10", 3255),
          ("alarmExternalInput11", 3256),
          ("alarmExternalInput12", 3257),
          ("alarmExternalInput2", 3258),
          ("alarmExternalInput3", 3259),
          ("alarmExternalInput4", 3260),
          ("alarmExternalInput5", 3261),
          ("alarmExternalInput6", 3262),
          ("alarmExternalInput7", 3263),
          ("alarmExternalInput8", 3264),
          ("alarmExternalInput9", 3265),
          ("alarmExternalLinkFailure", 3190),
          ("alarmFWD-ASE-PIL-Force-Fail", 3607),
          ("alarmFacilityDataRateNotSupported", 3036),
          ("alarmFacilityForcedOn", 3112),
          ("alarmFacilityLoopback", 3111),
          ("alarmFanPowerSupply1Failure", 3300),
          ("alarmFanPowerSupply2Failure", 3301),
          ("alarmGFPLOF", 3303),
          ("alarmGFPLossofCharacterSync", 3306),
          ("alarmGFPLossofClientSignal", 3305),
          ("alarmGFPPLM", 3304),
          ("alarmGFPTClientSignalFailure", 3307),
          ("alarmGfpLossOfClientSig", 3187),
          ("alarmHPB3BIP", 2259),
          ("alarmHPB3BIPTCA", 2261),
          ("alarmHPPLM", 3314),
          ("alarmHPRDI", 3313),
          ("alarmHPRDIC", 2258),
          ("alarmHPRDIP", 2256),
          ("alarmHPRDIS", 2257),
          ("alarmHPREITCA", 2260),
          ("alarmHPSD", 2254),
          ("alarmHPSF", 2255),
          ("alarmHPUNEQ", 3315),
          ("alarmHighCurrentThresholdCrossed", 3273),
          ("alarmHighOIPThresholdCrossed", 3279),
          ("alarmHighOOPThresholdCrossed", 3280),
          ("alarmHighTemperatureThresholdCrossed", 3281),
          ("alarmHighVoltageThresholdCrossed", 3282),
          ("alarmHighestCurrentThresholdCrossed", 3274),
          ("alarmHighestOIPThresholdCrossed", 3275),
          ("alarmHighestOOPThresholdCrossed", 3276),
          ("alarmHighestTemperatureThresholdCrossed", 3277),
          ("alarmHighestVoltageThresholdCrossed", 3278),
          ("alarmHwFailure", 3001),
          ("alarmIdleSignalReceived", 3012),
          ("alarmIfModTempOoR", 3200),
          ("alarmIndSig", 9954),
          ("alarmIndicationSig", 4842),
          ("alarmIndicationSignal", 8000),
          ("alarmIndicationSignalHigherOrderPath", 3105),
          ("alarmIndicationSignalLine", 3119),
          ("alarmIndicationSignalLowerOrderPath", 3124),
          ("alarmIndicationSignalOdu", 3019),
          ("alarmIndicationSignalOtu", 3020),
          ("alarmInputTIF", 3364),
          ("alarmInputTIF1", 3567),
          ("alarmInputTIF10", 3576),
          ("alarmInputTIF11", 3577),
          ("alarmInputTIF12", 3578),
          ("alarmInputTIF13", 3579),
          ("alarmInputTIF14", 3580),
          ("alarmInputTIF15", 3581),
          ("alarmInputTIF16", 3582),
          ("alarmInputTIF2", 3568),
          ("alarmInputTIF3", 3569),
          ("alarmInputTIF4", 3570),
          ("alarmInputTIF5", 3571),
          ("alarmInputTIF6", 3572),
          ("alarmInputTIF7", 3573),
          ("alarmInputTIF8", 3574),
          ("alarmInputTIF9", 3575),
          ("alarmInputVoltageFailure", 3010),
          ("alarmInternalHWFailure", 3326),
          ("alarmIntrusionRx", 3163),
          ("alarmIntrusionTx", 3164),
          ("alarmLOFLOMODU", 3027),
          ("alarmLOPVvirtualtributarypath", 2290),
          ("alarmLPB3BIP", 2269),
          ("alarmLPB3BIPTCA", 2273),
          ("alarmLPPLM", 3319),
          ("alarmLPRDI", 3318),
          ("alarmLPRDIC", 2266),
          ("alarmLPRDIP", 2264),
          ("alarmLPRDIS", 2265),
          ("alarmLPREIB3", 2267),
          ("alarmLPREIB3TCA", 2271),
          ("alarmLPREIV5", 2268),
          ("alarmLPREIV5TCA", 2272),
          ("alarmLPSD", 2262),
          ("alarmLPSF", 2263),
          ("alarmLPUNEQ", 3320),
          ("alarmLPV5BIP", 2270),
          ("alarmLPV5BIPTCA", 2274),
          ("alarmLaserBiasCurrAbnormal", 3116),
          ("alarmLaserBiasCurrentNormalizedtooHigh", 3165),
          ("alarmLaserTempOoR", 3201),
          ("alarmLaserTemperatureTooHi", 3181),
          ("alarmLaserTemperatureTooLow", 3180),
          ("alarmLineAIS", 3232),
          ("alarmLineANotAvailable", 3233),
          ("alarmLineBNotAvailable", 3234),
          ("alarmLineRDI", 3235),
          ("alarmLinkDown", 3310),
          ("alarmLockedDefectOdu", 3029),
          ("alarmLockedDefectOduTcmA", 3063),
          ("alarmLockedDefectOduTcmB", 3064),
          ("alarmLockedDefectOduTcmC", 3159),
          ("alarmLossOfCharSync", 3191),
          ("alarmLossOfCharSyncFromFarEnd", 3102),
          ("alarmLossOfFrame", 3184),
          ("alarmLossOfFrameMux", 3043),
          ("alarmLossOfFrameMuxFarEnd", 3044),
          ("alarmLossOfFrameOtu", 3182),
          ("alarmLossOfGfpFrame", 3185),
          ("alarmLossOfMultiFrameOtu", 3021),
          ("alarmLossOfPointerHigherOrderPath", 3106),
          ("alarmLossOfPointerLowerOrderPath", 3125),
          ("alarmLossOfReceiverClockRecovery", 3013),
          ("alarmLossofMultiframeHigherOrderPath", 3103),
          ("alarmLossofMultiframeLowerOrderPath", 3122),
          ("alarmLossofOIP", 3236),
          ("alarmLossofOOP", 3202),
          ("alarmLossofSequenceHigherOrderPath", 3104),
          ("alarmLossofSequenceLowerOrderPath", 3123),
          ("alarmLossofSignalonTxport", 3203),
          ("alarmLossofTandemConnectionOduTcmA", 3066),
          ("alarmLossofTandemConnectionOduTcmB", 3065),
          ("alarmLossofTandemConnectionOduTcmC", 3160),
          ("alarmLowCurrentThresholdCrossed", 3283),
          ("alarmLowOIPThresholdCrossed", 3289),
          ("alarmLowOOPThresholdCrossed", 3290),
          ("alarmLowTemperatureThresholdCrossed", 3291),
          ("alarmLowVoltageThresholdCrossed", 3292),
          ("alarmLowestCurrentThresholdCrossed", 3284),
          ("alarmLowestOIPThresholdCrossed", 3285),
          ("alarmLowestOOPThresholdCrossed", 3286),
          ("alarmLowestTemperatureThresholdCrossed", 3287),
          ("alarmLowestVoltageThresholdCrossed", 3288),
          ("alarmMSAIS", 3322),
          ("alarmMSB1BIP", 2250),
          ("alarmMSRDI", 3323),
          ("alarmMSREITCA", 2251),
          ("alarmMSRSB1BIPTCA", 2252),
          ("alarmMSRSB2BIPTCA", 2253),
          ("alarmMSSD", 3324),
          ("alarmMSSF", 2249),
          ("alarmMepNotPresentL2", 3565),
          ("alarmMismatch", 3174),
          ("alarmMultipleFanFailure", 3188),
          ("alarmMultiplexStructureIdentifierMismatchOPU", 3033),
          ("alarmMultiplexStructureIdentifierMismatchOPU1", 3183),
          ("alarmNTPnotSynchronized", 3589),
          ("alarmNoFeedback", 3238),
          ("alarmNotOk", 790),
          ("alarmOIPtooHigh", 3193),
          ("alarmOIPtooLow", 3197),
          ("alarmOOPOoR", 3199),
          ("alarmOOPtooHigh", 3198),
          ("alarmOOPtooLow", 3194),
          ("alarmOSC-Opt-CTRL-Fail-High", 3601),
          ("alarmOSC-Opt-CTRL-Fail-Low", 3602),
          ("alarmOn", 1924),
          ("alarmOosAins", 3155),
          ("alarmOosDisabled", 3101),
          ("alarmOosMaintenance", 3100),
          ("alarmOosManagement", 3099),
          ("alarmOpenConnectionIndicationOdu", 3028),
          ("alarmOpenConnectionIndicationOduTcmA", 3059),
          ("alarmOpenConnectionIndicationOduTcmB", 3060),
          ("alarmOpenConnectionIndicationOduTcmC", 3158),
          ("alarmOpticalInputPwrReceivedTooHigh", 3015),
          ("alarmOpticalInputPwrReceivedTooLow", 3014),
          ("alarmOpticalOutputPwrTransmittedTooHigh", 3016),
          ("alarmOpticalOutputPwrTransmittedTooLow", 3017),
          ("alarmOtuFecLossofFrame", 3230),
          ("alarmOutputTIF1", 3583),
          ("alarmOutputTIF2", 3584),
          ("alarmOutputTIF3", 3585),
          ("alarmOutputTIF4", 3586),
          ("alarmPLMVvirtualtributarypath", 2295),
          ("alarmPanelFailure", 1982),
          ("alarmPanelMissing", 1983),
          ("alarmPathAIS", 3242),
          ("alarmPathCV15Minutes", 3267),
          ("alarmPathCV24Hours", 3269),
          ("alarmPathES15Minutes", 3271),
          ("alarmPathES24Hours", 3272),
          ("alarmPathPLM", 3243),
          ("alarmPathRDI", 3244),
          ("alarmPathSES15Minutes", 3296),
          ("alarmPathSES24Hours", 3297),
          ("alarmPathSignalDegrade", 3245),
          ("alarmPathUAS15Minutes", 3298),
          ("alarmPathUAS24Hours", 3299),
          ("alarmPathUNEQ", 3246),
          ("alarmPayloadMismatchGfp", 3186),
          ("alarmPayloadMismatchHigherOrderPath", 3108),
          ("alarmPayloadMismatchLowOrderPath", 3128),
          ("alarmPayloadMismatchOPU", 3039),
          ("alarmPeerLink", 3038),
          ("alarmPlannedModuleMismatch", 3228),
          ("alarmPlannedModuleMissing", 3247),
          ("alarmPowerFail", 3325),
          ("alarmPowerMissing", 3002),
          ("alarmPowerSupplyFailure", 3302),
          ("alarmPowerSupplyUnitFailure", 3009),
          ("alarmPriVidNotEqualExtVidL2", 3566),
          ("alarmProtectionGroupFailure", 3248),
          ("alarmRDICPHigherOrderPath", 2285),
          ("alarmRDICVvirtualtributarypath", 2299),
          ("alarmRDIPPHigherOrderPath", 2283),
          ("alarmRDIPVvirtualtributarypath", 2297),
          ("alarmRDISPHigherOrderPath", 2284),
          ("alarmRDISVvirtualtributarypath", 2298),
          ("alarmREILTCA", 2278),
          ("alarmREIPHigherOrderPath", 2286),
          ("alarmREIPTCAHigherOrderPath", 2288),
          ("alarmRSTIM", 3308),
          ("alarmReceiverDisabled", 3113),
          ("alarmRemoteDefectIndicationHigherOrderPath", 3109),
          ("alarmRemoteDefectIndicationLine", 3120),
          ("alarmRemoteDefectIndicationLowerOrderPath", 3127),
          ("alarmRxLineAttenuationOoR", 3195),
          ("alarmRxLossofClock", 3229),
          ("alarmRxSignalOverload", 3239),
          ("alarmSDVvirtualtributarypath", 2292),
          ("alarmSFVvirtualtributarypath", 2293),
          ("alarmSectionCV15Minutes", 3266),
          ("alarmSectionCV24Hours", 3268),
          ("alarmSectionES15Minutes", 3270),
          ("alarmSectionSEFS15Minutes", 3293),
          ("alarmSectionSEFS24Hours", 3294),
          ("alarmSectionSES15Minutes", 3295),
          ("alarmSectionSignalDegrade", 3249),
          ("alarmSectionTraceInconsistency", 3018),
          ("alarmSectionTraceInconsistency1", 3250),
          ("alarmSectionTraceMismatch", 3192),
          ("alarmSectionTraceMismatch1", 3251),
          ("alarmSfCfmLevel0L2", 3633),
          ("alarmSfCfmLevel1L2", 3634),
          ("alarmSfCfmLevel2L2", 3635),
          ("alarmSfCfmLevel3L2", 3636),
          ("alarmSfCfmLevel4L2", 3637),
          ("alarmSfCfmLevel5L2", 3638),
          ("alarmSfCfmLevel6L2", 3639),
          ("alarmSfCfmLevel7L2", 3640),
          ("alarmShelfMismatch", 3000),
          ("alarmSignalDegradationonLinkVector", 3049),
          ("alarmSignalDegradeLine", 3121),
          ("alarmSignalDegradeOdu", 3031),
          ("alarmSignalDegradeOduTcmA", 3068),
          ("alarmSignalDegradeOduTcmB", 3067),
          ("alarmSignalDegradeOduTcmC", 3161),
          ("alarmSignalDegradeOlm", 3042),
          ("alarmSignalDegradeOtu", 3024),
          ("alarmSignalFailureonLinkVector", 3050),
          ("alarmSingleFanFailure", 3189),
          ("alarmSubModuleTempOoR", 3252),
          ("alarmSubModuleTempTooHigh", 3156),
          ("alarmSwitchFailed", 3008),
          ("alarmSwitchPositionError", 3253),
          ("alarmSwitchtoProtectionInhibited", 3117),
          ("alarmSwitchtoProtectionInhibitedL2", 3654),
          ("alarmSwitchtoWorkingInhibited", 3118),
          ("alarmSwitchtoWorkingInhibitedL2", 3641),
          ("alarmTIMHigherOrderPath", 2282),
          ("alarmTIMVvirtualtributarypath", 2296),
          ("alarmTSUBTEMPFHT", 3048),
          ("alarmTUAIS", 3316),
          ("alarmTULOM", 3321),
          ("alarmTULOP", 3317),
          ("alarmTemperatureTooHigh", 3178),
          ("alarmTemperatureTooLow", 3179),
          ("alarmTerminalLoopback", 3110),
          ("alarmThirdPartyPlug", 3166),
          ("alarmThres15MinExceededOduBbe", 3080),
          ("alarmThres15MinExceededOduES", 3054),
          ("alarmThres15MinExceededOduSES", 3055),
          ("alarmThres15MinExceededOduTcmABbe", 3077),
          ("alarmThres15MinExceededOduTcmAES", 3071),
          ("alarmThres15MinExceededOduTcmASES", 3073),
          ("alarmThres15MinExceededOduTcmAUAS", 3075),
          ("alarmThres15MinExceededOduTcmBBbe", 3078),
          ("alarmThres15MinExceededOduTcmBES", 3072),
          ("alarmThres15MinExceededOduTcmBSES", 3074),
          ("alarmThres15MinExceededOduTcmBUAS", 3076),
          ("alarmThres15MinExceededOduUAS", 3056),
          ("alarmThres15MinExceededOtuBbe", 3079),
          ("alarmThres15MinExceededOtuES", 3051),
          ("alarmThres15MinExceededOtuSES", 3052),
          ("alarmThres15MinExceededOtuUAS", 3053),
          ("alarmThres15MinExceededPhysConvCV", 3045),
          ("alarmThres15MinExceededPhysConvDE", 3046),
          ("alarmThres15MinExceededPhysConvES", 3047),
          ("alarmTraceIdentifierMismatchOdu", 3030),
          ("alarmTraceIdentifierMismatchOduTcmA", 3061),
          ("alarmTraceIdentifierMismatchOduTcmB", 3062),
          ("alarmTraceIdentifierMismatchOtu", 3023),
          ("alarmTransmittedDisabledAis", 3006),
          ("alarmTransmittedDisabledIdle", 3005),
          ("alarmTransmitterDisabledOff", 3114),
          ("alarmTurnupCondition", 3547),
          ("alarmTurnupFailed", 3548),
          ("alarmTxLineAttenuationOoR", 3196),
          ("alarmUNEQVvirtualtributarypath", 2294),
          ("alarmUnequippedHigherOrderPath", 3107),
          ("alarmUnequippedLowerOrderPath", 3126),
          ("alarmV5BIPVTCAvirtualtributarypath", 2307),
          ("alarmV5BIPVvirtualtributarypath", 2303),
          ("alarmV5REIVTCAvirtualtributarypath", 2305),
          ("alarmV5REIVvirtualtributarypath", 2301),
          ("alarmWarmUpRzs", 9881),
          ("alarmaisM13", 2310),
          ("alarmalarmIndicationSignalOpu", 3153),
          ("alarmapdHighVoltage", 3147),
          ("alarmapdLowVoltage", 3146),
          ("alarmattOnTransmitterFiberHigherThanMonitor", 3154),
          ("alarmattOnTransmitterFiberLowerThanMonitor", 3133),
          ("alarmautoShutdownSendingAisOpu", 3152),
          ("alarmelasticStoreOverflowTransmitter", 3130),
          ("alarmembeddedOperationsChannelFailure", 3144),
          ("alarmlinkControlProtocolFailure", 3148),
          ("alarmlossOfMultiframeVCG", 3136),
          ("alarmlossOfSequenceVCG", 3137),
          ("alarmlossOfSignalTransmitter", 3132),
          ("alarmlossOfTransmitterClockRecovery", 3129),
          ("alarmlossofAlignmentVCG", 3139),
          ("alarmoTDRMeasuringinProgress", 3142),
          ("alarmprotectionNotAvailable", 3143),
          ("alarmreceiverOverloadProtection", 3151),
          ("alarmremoved", 3140),
          ("alarmsectionSignalFailure", 3134),
          ("alarmsignalDegradeHigherOrderPath", 3135),
          ("alarmsignalDegradeSection", 3145),
          ("alarmthermoElectricCoolerCurrentTooHigh", 3150),
          ("alarmthermoElectricCoolerCurrentTooLow", 3149),
          ("alarmthermoElectricCoolerEndOfLife", 3131),
          ("alarmthres15MinExceededPhysConvCVDE", 3141),
          ("alignBankStatus", 6021),
          ("allChannelsDownloaded", 1083),
          ("allChannelsInService", 6022),
          ("allFansHaveFailed", 6652),
          ("allsyncref", 3901),
          ("alternateModulationSignal", 490),
          ("ampFailure", 3670),
          ("amplifierAbnormal", 3603),
          ("anotherUserInWriteAccess", 787),
          ("antennaConditionFault", 840),
          ("antennaConnectionStatus", 841),
          ("apcdFail", 4506),
          ("apdTemperatureClientTooHigh", 400),
          ("apdTemperatureRingTooHigh", 399),
          ("apf", 14),
          ("applicationCodeMismatch", 4524),
          ("aprShd", 9597),
          ("apsBackupRunning", 1902),
          ("apsMismatch", 7818),
          ("apsMismatchHiT75", 1965),
          ("apsMissing", 2128),
          ("apsVersionMismatch", 4516),
          ("apsbackupfailed", 2048),
          ("aseLow", 3529),
          ("aseTableBuild", 3511),
          ("aseTableGenFailHighBackreflection", 3524),
          ("aseTableGenFailLow", 3528),
          ("aseTableGenFailOscMissing", 3523),
          ("aseTableGenFailSignalInput", 3522),
          ("aseTableGenProcess", 3533),
          ("aseTableNotAvailable", 3512),
          ("asf", 15),
          ("atmBlockedFe", 9587),
          ("atmCcloc", 9568),
          ("atmConfigAborted", 9583),
          ("atmConfigAbortedFe", 9584),
          ("atmGrTimingMismatch", 9588),
          ("atmInsufficientLinks", 9585),
          ("atmInsufficientLinksFe", 9586),
          ("atmLcd", 9567),
          ("atmLif", 9575),
          ("atmLods", 9576),
          ("atmRdiIma", 9577),
          ("atmRxMisConnected", 9579),
          ("atmRxUnusableFe", 9581),
          ("atmStartupFe", 9582),
          ("atmTxMisConnected", 9578),
          ("atmTxUnusableFe", 9580),
          ("atmVcais", 9572),
          ("atmVcloc", 9574),
          ("atmVcrdi", 9573),
          ("atmVpais", 9569),
          ("atmVploc", 9571),
          ("atmVprdi", 9570),
          ("atpc", 6023),
          ("atpcFailureProtSide", 6628),
          ("attAtROOR", 782),
          ("attAtRTooHigh", 943),
          ("attAtRTooLow", 944),
          ("attAtTOOR", 783),
          ("attAtTTooHigh", 946),
          ("attAtTTooLow", 945),
          ("attRxMonHigh", 950),
          ("attRxMonLow", 949),
          ("attTxMonHigh", 952),
          ("attTxMonLow", 951),
          ("attenuationProblem", 792),
          ("auAlarmIndicationSignal", 8006),
          ("auLossOfPointer", 8039),
          ("auditTrailLogFullThreshold", 6677),
          ("authPWmissing", 3593),
          ("authenticationFailed", 1840),
          ("autoAmpShutdown", 3671),
          ("autoLaserShutdown", 6678),
          ("autoNegFail", 9453),
          ("autoNegotiationFail", 9618),
          ("autoPowerShutdown", 3527),
          ("autoShutdown", 3095),
          ("autoShutdownAlS", 3096),
          ("autoShutdownAmpAps", 9867),
          ("autoShutdownBlock", 3356),
          ("autoShutdownGAis", 9878),
          ("autoShutdownLaserOffDueToErrFwd", 3094),
          ("autoShutdownLaserOffDueToHighTemp", 3082),
          ("autoShutdownLaserOffDueToHighTxPwr", 3083),
          ("autoShutdownODU-CLK", 3588),
          ("autoShutdownOpuClientSignalFail", 3621),
          ("autoShutdownOpuFlxCSF", 3690),
          ("autoShutdownSendingAisLine", 3098),
          ("autoShutdownSendingIdle", 3097),
          ("autoShutdownSendingOciOdu", 3657),
          ("autoShutdownStbyProtection", 3560),
          ("autoSquelchNoMatchID", 6765),
          ("autoSwitchRingSDEast", 6753),
          ("autoSwitchRingSDEastK1", 6749),
          ("autoSwitchRingSDWest", 6755),
          ("autoSwitchRingSDWestK1", 6750),
          ("autoSwitchRingSFEast", 6754),
          ("autoSwitchRingSFEastK1", 6751),
          ("autoSwitchRingSFWest", 6756),
          ("autoSwitchRingSFWestK1", 6752),
          ("autoSwitchSpanSDEast", 6761),
          ("autoSwitchSpanSDEastK1", 6757),
          ("autoSwitchSpanSDWest", 6763),
          ("autoSwitchSpanSDWestK1", 6758),
          ("autoSwitchSpanSFEast", 6762),
          ("autoSwitchSpanSFEastK1", 6759),
          ("autoSwitchSpanSFWest", 6764),
          ("autoSwitchSpanSFWestK1", 6760),
          ("automaticPowerReduction", 3513),
          ("automaticPowerReductionForEyeSafety", 3555),
          ("automaticPowerReductionMode", 1002),
          ("autonegunknown", 3902),
          ("avghldovrfrqnotrdy", 3903),
          ("aw", 16),
          ("b0AlarmDem", 6024),
          ("b0AlarmInterfaceUnit", 6025),
          ("b0AlarmTrib1", 6026),
          ("b0AlarmTrib2", 6027),
          ("b0AlarmTrib3", 6028),
          ("b0AlarmTrib4", 6029),
          ("b1SD", 6030),
          ("b2SD", 6031),
          ("bERSDL", 9949),
          ("bERSFL", 9950),
          ("backPlaneLossOfSignal", 4555),
          ("backPlaneLossOfSignal1", 4557),
          ("backPlaneLossOfSignal2", 4558),
          ("backPlaneLossOfSignal3", 4559),
          ("backPlaneLossOfSignal4", 4560),
          ("backplaneEepromFailure", 6032),
          ("backplaneFailure", 17),
          ("backplaneInternalLinkFault", 6780),
          ("backupApsMissing", 2151),
          ("backupForcedToHalt", 3687),
          ("backupNotResponding", 3686),
          ("backwardInLos", 9490),
          ("backwardOscDitherLos", 9493),
          ("badBytesReceived", 2036),
          ("badConfigFile", 6680),
          ("badConfigSlaveUnits", 6564),
          ("badPacketsReceived", 2037),
          ("bampFail1", 9203),
          ("bampFail2", 9204),
          ("bampFail3", 9205),
          ("bampFail4", 9206),
          ("bampWarn1", 9207),
          ("bampWarn2", 9208),
          ("bampWarn3", 9209),
          ("bampWarn4", 9210),
          ("bandwithMismatch", 743),
          ("bandwithNotAvailable", 758),
          ("battDischarge", 18),
          ("battery", 19),
          ("batteryDischarg", 9211),
          ("batteryDischarging", 20),
          ("batteryFail", 9212),
          ("batteryFailure", 21),
          ("batteryFailure2", 616),
          ("batteryLow", 22),
          ("bb1Bb2DataInterfaceFailure", 6569),
          ("bckupntpsvrFailed", 3904),
          ("bdi", 465),
          ("bdiEgress", 4835),
          ("ber", 415),
          ("ber10Em3ProtSide", 6608),
          ("ber3", 23),
          ("ber56", 24),
          ("ber6", 757),
          ("berSdProtSide", 6604),
          ("bipolarViolationSignalFault", 824),
          ("bitRateError", 4554),
          ("bitsPll0OutOfLock", 6782),
          ("bitsPll1OutOfLock", 6783),
          ("boosterStageReceiveFail", 3430),
          ("boosterStageTransmitFail", 3428),
          ("bothPrimSecTrcOutService", 6803),
          ("bothReferencesBad", 6804),
          ("bpmismatch", 3994),
          ("brPwrRxTooHigh", 3521),
          ("btbCardMissing", 533),
          ("btbm", 1904),
          ("buffer", 25),
          ("builtInTestFailed", 9599),
          ("busDown", 6645),
          ("busFailure", 474),
          ("bwexceedednegspeed", 3905),
          ("bypassCardFailure", 6033),
          ("cEVHatchFail", 9235),
          ("cSFOPU", 9947),
          ("cableLosNext", 9958),
          ("cableLosPrevious", 9957),
          ("cableProblem", 26),
          ("cableReference", 27),
          ("cabs", 9972),
          ("calibrationFailure", 1872),
          ("calibrationFailureLine", 1873),
          ("calibrationFailureTrib1", 1874),
          ("calibrationFailureTrib2", 1875),
          ("calibrationFailureTrib3", 1876),
          ("calibrationFailureTrib4", 1877),
          ("callFailure", 9528),
          ("callSurvivabilityDegrade", 9565),
          ("canBusFailure", 461),
          ("capabilityLevelMismatch", 3503),
          ("cardBreakdown", 28),
          ("cardClockFailure", 4536),
          ("cardCommunicationFailure", 1939),
          ("cardDisabled", 29),
          ("cardFailure", 30),
          ("cardHwMaintenance", 6681),
          ("cardInUnconfiguredSlot", 31),
          ("cardInitializationInProgress", 9519),
          ("cardMismatch", 247),
          ("cardMissing", 246),
          ("cardMissing2", 6776),
          ("cardOverequipped", 7787),
          ("cardProblem", 32),
          ("cardTemperatureProblem", 458),
          ("cardTimingSubsysFault", 6802),
          ("cardTypeMisMatch", 6646),
          ("cardVariantMismatch", 4525),
          ("carrierFreqOffsetTooHigh", 3631),
          ("carrierFreqOffsetTooLow", 3630),
          ("ceElpsConfigurationMismatchNotif", 5545),
          ("ceElpsFailureOfProtocolNotif", 5549),
          ("ceElpsLackOfResponseNotif", 5546),
          ("ceElpsProtectionGroupFailedNotif", 5548),
          ("ceElpsProtectionNotAvailableNotif", 5547),
          ("ceElpsProtectionTypeMismatchNotif", 5544),
          ("ceEnvNotif", 5541),
          ("ceEqFreeRunningSyncModeNotif", 5529),
          ("ceEqHoldOverSyncModeNotif", 5530),
          ("ceEqMEAHWVMNotif", 5532),
          ("ceEqMEANotif", 5531),
          ("ceEqPROTNANotif", 5533),
          ("ceEqPowerFeedANotif", 5534),
          ("ceEqPowerFeedBNotif", 5535),
          ("ceEqReplUnitDegradeNotif", 5537),
          ("ceEqReplUnitFailedNotif", 5538),
          ("ceEqReplUnitMissingNotif", 5536),
          ("ceEqSWDownLoadFailureNotif", 5539),
          ("ceEqThermalNotif", 5540),
          ("ceErpsAPSMNotReceivedNotif", 5553),
          ("ceErpsFailureOfProtectionNotif", 5552),
          ("ceErpsProtectedVlanFailureNotif", 5554),
          ("ceErpsProvisioningMismatchNotif", 5551),
          ("ceErpsRingProtectionNotAvailNotif", 5555),
          ("ceErpsVlanProtectionNotAvailNotif", 5556),
          ("ceExtStatusNotif", 5557),
          ("ceLAGInterfaceFailureNotif", 5510),
          ("ceLAGInterfacePROTNANotif", 5511),
          ("ceMACANFNotif", 5515),
          ("ceMACLOSNotif", 5512),
          ("ceMACLOSYNCNotif", 5513),
          ("ceMACPortDyingGaspNotif", 5519),
          ("ceMACPortLinkFlappingNotif", 5518),
          ("ceMACSDNotif", 5517),
          ("ceMACSFNotif", 5516),
          ("ceMACTRDIENotif", 5514),
          ("ceMIEcfmY1731AISNotif", 5528),
          ("ceMIEcfmdot1agErrorCCMNotif", 5526),
          ("ceMIEcfmdot1agMACstatusNotif", 5524),
          ("ceMIEcfmdot1agRDICCMNotif", 5523),
          ("ceMIEcfmdot1agRemoteMepCCMNotif", 5525),
          ("ceMIEcfmdot1agXconCCMNotif", 5527),
          ("ceMSTGlobalErrTrap", 5520),
          ("ceMSTUnExpMSTPPDUReceivedTrap", 5521),
          ("ceRSTGlobalErrTrap", 5522),
          ("ceSntpPrimarySNTPServerUnreachable", 5542),
          ("ceSntpSecondarySNTPServerUnreachable", 5543),
          ("ceSyncERefFailureNotif", 5550),
          ("centralizedPowerMajor", 9214),
          ("centralizedPowerMinor", 9215),
          ("cfgFile", 33),
          ("cfmCcmError", 3644),
          ("cfmCcmLost", 3645),
          ("cfmCcmMacStatus", 3643),
          ("cfmCcmXConn", 3646),
          ("cfmRemoteDefectIndication", 3642),
          ("ch1", 6034),
          ("ch2", 6035),
          ("channelCountMismatch", 1903),
          ("channelCountMismatchC1", 985),
          ("channelCountMismatchC2", 986),
          ("channelCountMismatchC3", 987),
          ("channelCountMismatchC4", 988),
          ("channelForced", 6036),
          ("channelForcedViaExtSwitch", 6037),
          ("channelLicenseNotAvailable", 4545),
          ("channelMismatch", 3422),
          ("channelOnStandby", 6038),
          ("channelPowerMismatch1", 1005),
          ("channelPowerMismatch2", 1006),
          ("channelPowerMismatch3", 1007),
          ("channelPowerMismatch4", 1008),
          ("channelUpgradeOrderViolation", 1852),
          ("channelUpgradeOrderViolation1", 961),
          ("channelUpgradeOrderViolation2", 962),
          ("channelUpgradeOrderViolation3", 963),
          ("channelUpgradeOrderViolation4", 964),
          ("chargeCurrent", 34),
          ("checkHECgfpFailure", 9449),
          ("checksumConfigFileNok", 6679),
          ("chromaticDispersionTooHigh", 3627),
          ("chromaticDispersionTooLow", 3626),
          ("circuitDown", 6637),
          ("circuitIntrusiveTest", 6638),
          ("circuitUnprotected", 6639),
          ("circuitXcLoopback", 6748),
          ("ckSyncDem", 6039),
          ("ckSyncInterfaceUnit", 6040),
          ("ckSyncModule", 6041),
          ("ckSyncTrib1", 6042),
          ("ckSyncTrib2", 6043),
          ("ckSyncTrib3", 6044),
          ("ckSyncTrib4", 6045),
          ("ckSyncTribOcc", 6046),
          ("clientFailForwarding", 3346),
          ("clientModeMismatch", 3455),
          ("clientSignalFail", 3489),
          ("clientSignalFailGFP", 1960),
          ("clientSignalFailLossOfCharacterSynchronisationGFP", 9523),
          ("clientSignalFailOpu", 3619),
          ("clk", 35),
          ("clock", 36),
          ("clockBelowMinimumClockLevel", 845),
          ("clockFail", 471),
          ("clockFailTx", 506),
          ("clockFailure", 1822),
          ("clockModuleUsableAsTheOutputReference", 814),
          ("clockNotSelectedForOutput", 851),
          ("clockPllNotLocked", 822),
          ("clockPllStatusFault", 834),
          ("cltSignalFail", 2142),
          ("cltSignalFailGFP", 2156),
          ("cni", 37),
          ("coChannelXPICProtSide", 6622),
          ("coChannelXpic", 6047),
          ("comPowerFailure", 9258),
          ("commACFail", 9268),
          ("commercialPowerFailure", 38),
          ("commsLinkFail", 39),
          ("communicationFailure", 8186),
          ("communicationLossToH73", 1976),
          ("communicationLossToHDS", 2111),
          ("communicationLossToOTS", 1918),
          ("communicationProblemToH73", 1977),
          ("communicationProblemToHDS", 2112),
          ("communicationProblemToOTS", 1919),
          ("compactFlashFail", 1964),
          ("compactFlashFailure", 7845),
          ("compactFlashFailure0", 4548),
          ("compactFlashFailure1", 4549),
          ("compactFlashFull", 3473),
          ("compactFlashInsufficientSize", 3495),
          ("compactFlashInsufficientSize0", 4550),
          ("compactFlashInsufficientSize1", 4551),
          ("compactFlashMissing", 3498),
          ("conf", 40),
          ("confEquip", 41),
          ("confFail", 9959),
          ("configDownload", 6778),
          ("configFileNotFound", 6682),
          ("configNotApproved", 6683),
          ("configurableOpticalOutputPowerTransmittedTooHigh", 3530),
          ("configurableOpticalOutputPowerTransmittedTooLow", 3531),
          ("configurationError", 524),
          ("configurationMismatch", 9873),
          ("configurationStatus", 844),
          ("connectionCableFail", 3413),
          ("connectionEstablished", 2136),
          ("connectionIdMismatch", 936),
          ("connectionLossToGne", 977),
          ("connectionLossToLocalNE", 1916),
          ("connectionLossToNE", 930),
          ("connectionLossToRemoteNE", 1917),
          ("consecutiveSesProtection", 6499),
          ("constituentAttributeMismatch", 9605),
          ("continuous0", 970),
          ("controlOrCablingProblem", 1098),
          ("controllerInterfaceFail", 3496),
          ("conv2Synth", 6000),
          ("coolingFan11Failure", 1968),
          ("coolingFan12Failure", 1969),
          ("coolingFan1CommFailure", 1979),
          ("coolingFan1Failure", 1892),
          ("coolingFan1Missing", 1895),
          ("coolingFan21Failure", 1970),
          ("coolingFan22Failure", 1971),
          ("coolingFan2CommFailure", 1980),
          ("coolingFan2Failure", 1893),
          ("coolingFan2Missing", 1896),
          ("coolingFan31Failure", 1972),
          ("coolingFan32Failure", 1973),
          ("coolingFan3CommFailure", 1981),
          ("coolingFan3Failure", 1894),
          ("coolingFan3Missing", 1897),
          ("coolingFan4Failure", 2147),
          ("coolingFan4Missing", 2148),
          ("coolingFanFail", 9213),
          ("coolingFanFailure", 42),
          ("couplerDropLoss", 957),
          ("cpTunnelEstablishFailed", 3506),
          ("cpTunnelModificationInProgress", 3502),
          ("cpTunnelPrecompFailed", 3507),
          ("cpaMismatch", 4556),
          ("cpuAlarm", 6048),
          ("cpuFailure", 1811),
          ("craFail1", 9216),
          ("craFail2", 9217),
          ("craFail3", 9218),
          ("craFail4", 9219),
          ("craWarn1", 9220),
          ("craWarn2", 9221),
          ("craWarn3", 9222),
          ("craWarn4", 9223),
          ("crcErrorFaultStatus", 825),
          ("crcmismatch", 43),
          ("criAlrExtUnmangedNE", 617),
          ("critical", 44),
          ("criticalGeneralAlarm", 1922),
          ("crossconnectccm", 3906),
          ("cryptoOfficerPWmissing", 3591),
          ("ctneqpt", 3907),
          ("cv15minThresholdCrossed", 8082),
          ("cv24hThresholdCrossed", 8083),
          ("dChannelDropLossOfAlignment", 6049),
          ("dChannelInsertionLossOfAlignment", 6050),
          ("dataExpCableFault", 6051),
          ("dataExpCableMissing", 6052),
          ("dataRateMism", 2141),
          ("dataRateMismatch", 939),
          ("dataRateMismatchGFP", 9520),
          ("dataTransitionMissingDccm", 6064),
          ("dataTransitionMissingF1", 6065),
          ("dataTransitionMissingK11", 6066),
          ("dataTransitionMissingK12", 6067),
          ("dataTransitionMissingK4", 6068),
          ("dataTransitionMissingK7", 6069),
          ("databaseFailure", 3561),
          ("databaseMismatch", 3341),
          ("databaseNcuMismatch", 3342),
          ("databaseVersionMismatch", 3344),
          ("dbBackupFailed", 593),
          ("dbFullBackupFailed", 592),
          ("dbReplicationIncompleted", 3685),
          ("dbcorruption", 3993),
          ("dbdowngradeip", 3970),
          ("dbftfail", 3968),
          ("dbftip", 3969),
          ("dbit", 45),
          ("dbproip", 3991),
          ("dccBus", 46),
          ("dccFailure", 6500),
          ("dccLinkDown", 917),
          ("dccLinkDown2", 8011),
          ("dccerr", 9976),
          ("dcf", 1816),
          ("dcf1", 2059),
          ("dcf2", 2060),
          ("dcfMs", 9852),
          ("dcfRs", 9853),
          ("dcn2mLos", 9518),
          ("dcnCommunicationFail", 3345),
          ("dcnLinkDown", 565),
          ("dcnOverload", 934),
          ("dcnServerSignalFailure", 3395),
          ("debugInterfaceActive", 4847),
          ("dedicatedPrimaryGatewayFailure", 7810),
          ("dedicatedSecondaryGatewayFailure", 7811),
          ("deepDischarge", 47),
          ("defaultKBytes", 6684),
          ("defect", 766),
          ("defect-id-vcxo-failure", 9842),
          ("degrade", 9960),
          ("degradedSignal", 1959),
          ("degradedSignalDeg", 3424),
          ("degradedSignalOSC", 7803),
          ("degreeOfPolarization", 3448),
          ("dem1SyncSourceOn", 6053),
          ("dem2SyncSourceOn", 6054),
          ("demBlockFailure", 6501),
          ("demBlockFailureProtSide", 6609),
          ("demCardFailure", 6055),
          ("demSideFail", 6057),
          ("demStandbyOccSyncSourceOn", 6056),
          ("demSwitch", 6058),
          ("demSyncLos", 6059),
          ("demSyncOn", 6060),
          ("demSyncSourceOn", 6061),
          ("dhcpNoIPAddr", 9966),
          ("dhcpOutOfIPAddr", 9967),
          ("dhcpRelayFail", 9977),
          ("differentialGroupDelayTooHigh", 3625),
          ("differentialGroupDelayTooLow", 3624),
          ("disabledChannelPowerTooHigh", 3538),
          ("discrete1Fault", 1028),
          ("discrete2Fault", 1029),
          ("dispersionCompensationTooHigh", 3545),
          ("dispersionCompensationTooLow", 3544),
          ("divCardFailure", 6062),
          ("dlCEFCompleted", 9978),
          ("dm", 48),
          ("dopFail", 3463),
          ("downgradeChannelsInProgress", 1082),
          ("downloadStatus", 6063),
          ("dspProblem", 1097),
          ("dte", 49),
          ("dupIPAddr", 9968),
          ("dupIPAddrNet", 9969),
          ("duplexLinkFailure", 3688),
          ("duplicatedDHCPServer", 3478),
          ("dyinggasp", 3951),
          ("eEPROMFail", 3492),
          ("eLPSAPSMessageNotReceived", 9614),
          ("eLPSProtectionNotAvailable", 9615),
          ("eOpenConnectionIndication", 996),
          ("eRPSvLANProtectionNotAvailable", 9616),
          ("eastExtraTrafficPreemp", 6685),
          ("eberB2", 6502),
          ("eberRp", 6503),
          ("ebsl", 50),
          ("eepromF", 2155),
          ("eepromFailure", 6686),
          ("eepromFailure2", 6070),
          ("efmOamFault", 1037),
          ("efmfail", 3908),
          ("efmrce", 3909),
          ("efmrld", 3910),
          ("efmrls", 3911),
          ("egptProvMismatch", 9866),
          ("elasticStoreOverflowRx", 508),
          ("elasticStoreOverflowTx", 509),
          ("emsSystemAlarm", 523),
          ("enclosureDoorOpen", 51),
          ("encryptionPortKeyInitExchgMissed", 3666),
          ("encryptionSwitchedOff", 3596),
          ("engineFail", 9224),
          ("engineFailure", 52),
          ("engineOperating", 9225),
          ("engineSystemFault", 838),
          ("eni", 53),
          ("entityOutageIndication", 3552),
          ("envOH", 1827),
          ("eowUnavailable", 935),
          ("eqlzAdjust", 3667),
          ("eqp-critical-ocxo-failure", 9862),
          ("eqp-critical-vcxo-failure", 9860),
          ("eqp-minor-ocxo-failure", 9863),
          ("eqp-minor-vcxo-failure", 9861),
          ("eqptflt", 3952),
          ("eqptremoved", 3953),
          ("equalizationProgress", 3354),
          ("equipmentAlarm", 759),
          ("equipmentAlarmNoFeedback", 982),
          ("equipmentIdentifierDuplication", 54),
          ("equipmentMismatchAllow", 3398),
          ("equipmentProblem", 491),
          ("equipmentmismatch", 1795),
          ("equipmentnotaccepted", 1794),
          ("equipmentnotapproved", 1796),
          ("erroneousccm", 3912),
          ("errorCCMdefect", 9562),
          ("errorReadingCleiCode", 6688),
          ("errorReadingFanIdprom", 6689),
          ("errorReadingIdprom", 6687),
          ("es15Min", 6504),
          ("es15minThresholdCrossed", 8084),
          ("es24h", 6505),
          ("es24hThresholdCrossed", 8085),
          ("esmcfail", 3913),
          ("esw", 55),
          ("ethLossOfPointer", 4843),
          ("ethernetFail", 56),
          ("ethernetLinkFault", 1857),
          ("ethernetPortDown", 6633),
          ("ethernetSwitchFail", 1850),
          ("ew", 6072),
          ("exLof", 6314),
          ("excessClientLimit", 9850),
          ("excessTraffic", 9849),
          ("excessiveBER", 57),
          ("excessiveBitErrorRatioOSC", 7802),
          ("excessiveError", 1815),
          ("excessiveTempVariation", 9540),
          ("expGas", 9227),
          ("explosiveGas", 58),
          ("extensionHeaderMismatchGFP", 1957),
          ("externalAlarmInput", 6073),
          ("externalFanFail", 753),
          ("externalFanFailure", 8014),
          ("externalInput1", 8077),
          ("externalInput2", 8078),
          ("externalInput3", 8079),
          ("externalInput4", 8080),
          ("externalInput5", 8081),
          ("externalPortFault", 858),
          ("externalSyncSource1On", 6074),
          ("externalSyncSource2On", 6075),
          ("externalSyncSourceEnabled", 6076),
          ("externalSyncSourceNotPresent", 6077),
          ("f1Los", 6078),
          ("fabCapacityDeficiency", 9479),
          ("fabricConfigurationIsInvalid", 9621),
          ("fading", 6506),
          ("failedRestorePacketDB", 9617),
          ("failure", 9961),
          ("failureOfProtocolNoResponse", 4510),
          ("failureOfProtocolNoResponseEgress", 4841),
          ("failureOfProtocolProvisioningMismatch", 4509),
          ("failureOfProtocolProvisioningMismatchEgress", 4840),
          ("failureOfProtocolReceive", 9404),
          ("fan1Alarm", 6080),
          ("fan1Unit", 6082),
          ("fan2Alarm", 6081),
          ("fan2Unit", 6083),
          ("fanAlarm", 6079),
          ("fanExtendedClimateClass", 381),
          ("fanFailed", 6653),
          ("fanFailure", 473),
          ("fanFailure1", 510),
          ("fanFailure1U", 9602),
          ("fanFailure2", 511),
          ("fanFailure3", 512),
          ("fanFailureR", 6507),
          ("fanFilterMiss", 2154),
          ("fanFilterMissing", 3475),
          ("fanInsuf", 4517),
          ("fanInsufficient", 2145),
          ("fanIsNecessary", 746),
          ("fanLossOfRedundancy", 6654),
          ("fanMajor", 1940),
          ("fanMajorProblem", 7807),
          ("fanMinor", 1941),
          ("fanMinorProblem", 7808),
          ("fanMism", 4523),
          ("fanMismatch", 2146),
          ("fanNormalClimateClass", 382),
          ("fanPowerFail", 773),
          ("fanPowerFail1", 513),
          ("fanPowerFail2", 514),
          ("fanPowerSupplyFail1", 8019),
          ("fanPowerSupplyFail2", 8020),
          ("fanRemoved", 6655),
          ("fanUnit", 933),
          ("fanUnit1", 59),
          ("fanUnit1Failure", 9532),
          ("fanUnit2", 60),
          ("fanUnit2Failure", 9533),
          ("fanUnit3Failure", 9534),
          ("fanUnit4Failure", 9535),
          ("fanUnit5Failure", 9536),
          ("fanUnit6Failure", 9537),
          ("fanUnit7Failure", 9538),
          ("fanUnit8Failure", 9539),
          ("fanfailure", 8015),
          ("fanfailure1", 8016),
          ("fanfailure2", 8017),
          ("fanfailure3", 8018),
          ("farEndBlockError", 6084),
          ("farEndBlockErrorProtSide", 6623),
          ("farEndCommFailure", 3546),
          ("farEndInformationMismatch", 3554),
          ("farEndIpAddressUnknown", 3088),
          ("farEndRemoteFailure", 6085),
          ("farEndRemoteFailureProtSide", 6624),
          ("faultOnOpm", 3534),
          ("fca", 61),
          ("feLinkDown", 905),
          ("feedbackAbsent", 1882),
          ("feedbackDegraded", 1883),
          ("felinkDown", 8021),
          ("felne", 1807),
          ("ferFailure", 6508),
          ("fiberAttenuationCond", 3692),
          ("fiberAttenuationHigh", 3679),
          ("fiberAttenuationHighTx", 3682),
          ("fiberConnCommError", 3676),
          ("fiberConnDataFailure", 3678),
          ("fiberConnInvalid", 3674),
          ("fiberConnInvalidTx", 3680),
          ("fiberConnLos", 3672),
          ("fiberConnMismatch", 3675),
          ("fiberConnMismatchTx", 3681),
          ("fiberConnOptFault", 3673),
          ("fiberConnProtocolFailure", 3677),
          ("fiberConnectionMissing", 3553),
          ("fiberDeteriorate", 9598),
          ("fifoFlowProblem", 1998),
          ("fileError", 62),
          ("fileSynchronizationFail", 4552),
          ("fileSystemAlmostFull", 6690),
          ("filterExpired", 3460),
          ("fire", 63),
          ("fireDetectorFail", 9228),
          ("fireDetectorFailure", 64),
          ("firmwareMismatch", 1931),
          ("flash1Cfg", 65),
          ("flash2Cfg", 66),
          ("flashCapacityProblem", 1879),
          ("flashCfg", 67),
          ("flashMemory", 68),
          ("flood", 69),
          ("foc", 70),
          ("fop", 71),
          ("fopNoResponse", 9487),
          ("fopProvisioningMismatch", 9488),
          ("fopr", 1781),
          ("force-FWD-ASE-Pilot-ON", 3608),
          ("forceSwitchRingEast", 6693),
          ("forceSwitchRingEastK1", 6691),
          ("forceSwitchRingWest", 6694),
          ("forceSwitchRingWestK1", 6692),
          ("forceSwitchSpanEast", 6697),
          ("forceSwitchSpanEastK1", 6695),
          ("forceSwitchSpanWest", 6698),
          ("forceSwitchSpanWestK1", 6696),
          ("forced", 3914),
          ("forcedSwitchOverFailed", 6774),
          ("forcedSwitchOverInEffect", 6773),
          ("foreignConfig", 6699),
          ("forwardDefectIndication", 3490),
          ("forwardInLos", 9491),
          ("forwardOscDitherLos", 9492),
          ("fot", 1797),
          ("fpgaStatus", 9847),
          ("fportAttack", 411),
          ("fragileecc", 3890),
          ("frameAlignmentLoss", 6509),
          ("freeRunningSynchMode", 9936),
          ("freqOff", 9955),
          ("freqPlan16ComplTestAlarmProtSide", 6613),
          ("freqPlan2ComplTestAlarmProtSide", 6614),
          ("freqPlan4ComplTestAlarmProtSide", 6615),
          ("freqPlan8ComplTestAlarmProtSide", 6616),
          ("freqPlanFail", 6563),
          ("freqPlanFailProtSide", 6612),
          ("freqoff", 3915),
          ("frequencyControlParameterWithinSpecification", 812),
          ("frequencyDriftHighDegrade", 72),
          ("frequencyDriftLowDegrade", 73),
          ("frequencyHighDegrade", 74),
          ("frequencyHighFailure", 75),
          ("frequencyLowDegrade", 76),
          ("frequencyLowFailure", 77),
          ("frequencyMeasurementRangeExceeded", 832),
          ("frequencyMismatch", 748),
          ("frequencyMismatchEQPT", 7901),
          ("frequencyModeDegration", 811),
          ("frequencyPlan16ComplianceTestAlarm", 6086),
          ("frequencyPlan2ComplianceTestAlarm", 6087),
          ("frequencyPlan4ComplianceTestAlarm", 6088),
          ("frequencyPlan8ComplianceTestAlarm", 6089),
          ("frngsync", 3916),
          ("fspfext", 78),
          ("fstsync", 3917),
          ("ftmMissing", 1034),
          ("fuelLeak", 9231),
          ("fullPartialOperation", 778),
          ("functionNotSupported", 3458),
          ("fuseFail", 9232),
          ("fuseFail1", 516),
          ("fuseFail2", 517),
          ("fuseFailure", 79),
          ("fusefail1", 8022),
          ("fusefail2", 8023),
          ("fwdDefectIndication", 2143),
          ("fwpMismatchDownloadNotServiceAffecting", 3328),
          ("fwpMismatchDownloadServiceAffecting", 3327),
          ("gainAdoptFailedSpeq", 3653),
          ("gainProblem", 958),
          ("gainTiltNotSettable", 3352),
          ("gainTiltProb", 4507),
          ("gainTiltProblem", 1856),
          ("gainTooHighSpeq", 3651),
          ("gainTooLowSpeq", 3652),
          ("gasAlarm", 9233),
          ("gbESFPMissing", 791),
          ("gcccConnectionroblem", 2039),
          ("genAlrExtUnmangedNE", 621),
          ("generatorFail", 9234),
          ("generatorFailure", 80),
          ("genericAIS", 9999),
          ("genericEnv1", 81),
          ("genericEnv2", 82),
          ("genericEnv3", 83),
          ("genericEnv4", 84),
          ("genericEnv5", 85),
          ("genericEnv6", 86),
          ("genericEnv7", 87),
          ("genericEnv8", 88),
          ("genericEnv9", 89),
          ("genfilexferip", 3971),
          ("genoperip", 3972),
          ("gfpAlarmIndicationSignal", 3441),
          ("gfpClientSignalFail", 4515),
          ("gfpClientSignalFailFdi", 9942),
          ("gfpClientSignalFailLossOfCharacterSynchronisation", 3442),
          ("gfpClientSignalFailLossOfSignal", 3443),
          ("gfpClientSignalFailRdi", 9943),
          ("gfpDataRateMismatch", 3447),
          ("gfpExtHeaderMismatch", 3410),
          ("gfpExtensionHeaderMismatch", 7781),
          ("gfpLOCharSync", 925),
          ("gfpLOClientSig", 924),
          ("gfpLOF", 922),
          ("gfpLossOfCharacterSync", 8024),
          ("gfpLossOfFrameDelimiter", 8026),
          ("gfpLossofClientSignal", 8025),
          ("gfpNoFramesReceived", 3444),
          ("gfpOutOfSequence", 3445),
          ("gfpPLM", 923),
          ("gfpPayloadTypeMismatch", 8027),
          ("gfpUnexpectedChannelID", 3446),
          ("gfpUserPayloadMismatch", 3411),
          ("gfpexhmismatch", 3888),
          ("gfplfd", 3886),
          ("gfptClientSignalFailure", 926),
          ("gfptClientSignalFailureSec", 9552),
          ("gfptclientSignalFailure", 8028),
          ("gfpuplmismatch", 3887),
          ("gidmismatch", 3870),
          ("gpsEngineHwFault", 839),
          ("gpsEngineTrackingStatus", 842),
          ("gtmModuleProblem", 794),
          ("gtwyUnreachable", 9962),
          ("h73ApsMissing", 1961),
          ("h73RecoverMode", 2106),
          ("halfPartialOperation", 777),
          ("hardDisk", 90),
          ("hardwareFailure", 6700),
          ("hber", 6090),
          ("hberProtSide", 6610),
          ("hcoc27Dcf", 9555),
          ("hcoc9Dcf", 9554),
          ("hdsApsMissing", 2110),
          ("hdsRecoverMode", 2114),
          ("heaterFail1", 6091),
          ("heaterFail2", 6092),
          ("highAirflow", 9236),
          ("highBackReflectionPower", 9495),
          ("highBer", 3514),
          ("highCurrentThresholdCrossed", 8086),
          ("highEarlyWarning", 6093),
          ("highFastBer", 6094),
          ("highHumid", 9237),
          ("highHumidity", 91),
          ("highLineOutputPower", 9496),
          ("highLowTemperature", 9272),
          ("highOipThresholdCrossed", 8092),
          ("highOopThresholdCrossed", 8093),
          ("highPowerReceiveDetected", 1860),
          ("highPowerReceiveFailure", 1859),
          ("highTemp", 9238),
          ("highTempThresholdCrossed", 8094),
          ("highTemperature", 92),
          ("highVoltageThresholdCrossed", 8095),
          ("highWind", 93),
          ("highestCurrentThresholdCrossed", 8087),
          ("highestOipThresholdCrossed", 8088),
          ("highestOopThresholdCrossed", 8089),
          ("highestTempThresholdCrossed", 8090),
          ("highestVoltageThresholdCrossed", 8091),
          ("hitlessSwitchLossOfAlignment", 6095),
          ("hldovrsync", 3918),
          ("hocc-asic-failure", 9592),
          ("holdoverStateEntered", 6510),
          ("hopFerFailure", 6511),
          ("hopTraceIdMismatch", 6096),
          ("hopUnequipped", 6512),
          ("hpPayloadMismatch", 8070),
          ("hpRemoteDefetcIndication", 8060),
          ("hpUnequipped", 8113),
          ("hwConfigurationFault", 818),
          ("hwDegrade", 3668),
          ("hwInitializing", 3669),
          ("hwOprReachedHT", 3537),
          ("hwcfginconsistent", 3896),
          ("iLANFail", 3481),
          ("iLANFailed", 975),
          ("iLANRingBroken", 4527),
          ("iLinkFailure", 937),
          ("iNNCDown", 521),
          ("iceBuildUp", 94),
          ("icn", 95),
          ("iduBoardDemodParityAlarm", 6102),
          ("iduBoardLaserTxFail", 6103),
          ("iduBoardModulatorFpgaKo", 6104),
          ("iduBoardModulatorParityAlarm", 6105),
          ("iduBoardMtiSdhLocal", 6106),
          ("iduBoardMtiSdhRx", 6107),
          ("iduBoardOpticalTxRxAgeing", 6108),
          ("iduBoardSdhTribRxPllLock", 6109),
          ("iduBoardSdhTribTxPllLock", 6110),
          ("iduHardwareMismatch", 6111),
          ("iduOduIfCable", 6114),
          ("iduOduIfFskLof", 6112),
          ("iduOduIfLosRx", 6115),
          ("iduSoftwareMismatch", 6116),
          ("ifBoard", 6117),
          ("ifDemAlarm", 6118),
          ("ifModuleTempOoR", 775),
          ("imaGrpBlkFe", 8138),
          ("imaGrpCfgAbt", 8133),
          ("imaGrpCfgAbtFe", 8136),
          ("imaGrpGrtMismatch", 8132),
          ("imaGrpInsufLnks", 8134),
          ("imaGrpInsufLnksFe", 8137),
          ("imaGrpStartupFe", 8135),
          ("imaLnkLcd", 8139),
          ("imaLnkLif", 8140),
          ("imaLnkLods", 8141),
          ("imaLnkRdi", 8142),
          ("imaLnkRxmc", 8144),
          ("imaLnkRxuuFe", 8146),
          ("imaLnkTxmc", 8143),
          ("imaLnkTxuuFe", 8145),
          ("improperApsCodes", 6701),
          ("inactive", 9996),
          ("incomingAis", 485),
          ("incomingAis2", 6119),
          ("indeterminate", 96),
          ("indicationOfOutputControllerMastership", 833),
          ("initConfignotAccepted", 2035),
          ("inp", 97),
          ("inputDataDem", 6097),
          ("inputDataTrib1", 6098),
          ("inputDataTrib2", 6099),
          ("inputDataTrib3", 6100),
          ("inputDataTribOcc", 6101),
          ("inputLossOfLight", 1880),
          ("inputLossOfLight1", 1093),
          ("inputLossOfLight2", 1094),
          ("inputLossOfLight3", 1095),
          ("inputOpticalPowerTooLow", 2115),
          ("inputPllNotLocked", 823),
          ("inputPowerLow", 3449),
          ("inputReferenceAvailableStatus", 810),
          ("inputSignalDisabledTribProtSide", 6617),
          ("inputSignalLow", 98),
          ("inputVoltageFailure-1", 3609),
          ("inputVoltageFailure-2", 3610),
          ("installCEFCompleted", 9980),
          ("installCEFFail", 9981),
          ("installCEFProgress", 9982),
          ("insuffLockTimeForHoStab", 6784),
          ("intA", 99),
          ("intB", 100),
          ("intHWFail", 108),
          ("intQc", 486),
          ("intQcA", 492),
          ("intQcB", 493),
          ("intSmfA", 494),
          ("intSmfB", 495),
          ("intSra", 487),
          ("intSraA", 488),
          ("intSraB", 489),
          ("intZ", 110),
          ("intctneqpt", 3954),
          ("interfaceDown", 522),
          ("interfaceFailure", 6113),
          ("internalCardFailure", 6120),
          ("internalClockStateEntered", 6513),
          ("internalComError", 101),
          ("internalCommunicationProblem", 102),
          ("internalCommunicationProblem2", 103),
          ("internalCommunicationProblem3", 104),
          ("internalControlBusX", 105),
          ("internalControlBusXY", 106),
          ("internalControlBusY", 107),
          ("internalError", 525),
          ("internalHWFailure", 8029),
          ("internalLossOfSignal", 405),
          ("internalPortFault", 857),
          ("internalPowerTooHighFailure", 406),
          ("internalPowerTooLowFailure", 414),
          ("internalTraceIdentifierMismatch", 3421),
          ("internalTransmitDegraded", 407),
          ("internalTransmitFailureSON", 408),
          ("internalUnbalancedSignal", 780),
          ("interstageLossProblem", 475),
          ("intruder", 9240),
          ("intrusion", 9997),
          ("intrusionAtR", 947),
          ("intrusionAtT", 948),
          ("intrusionDetection", 109),
          ("intrusiveTestAccess", 6813),
          ("invalidCard", 6702),
          ("invalidGatewayAddress", 978),
          ("invalidLaserAttenuation", 591),
          ("invalidLaserFrequency", 590),
          ("invalidPortConfiguration", 6766),
          ("invalidProductCodeOrRev", 6703),
          ("invalidShelf", 6704),
          ("ip2OsiConfig", 413),
          ("ipaddrconflict", 3919),
          ("istm", 891),
          ("istmX", 892),
          ("istmY", 893),
          ("its", 111),
          ("jnxFanFailure", 2246),
          ("jnxFruFailed", 2242),
          ("jnxFruNotifMismatch", 2243),
          ("jnxFruPowerOff", 2245),
          ("jnxFruRemoval", 2244),
          ("jnxOpticsAvgPowerAlarm", 2210),
          ("jnxOpticsBiasCurrentHighAlarm", 2204),
          ("jnxOpticsBiasCurrentLowAlarm", 2205),
          ("jnxOpticsLOS", 2200),
          ("jnxOpticsLossofACPowerAlarm", 2212),
          ("jnxOpticsModuleTempHighThreshAlert", 2217),
          ("jnxOpticsModuleTempLowThreshAlert", 2218),
          ("jnxOpticsPowerHighAlarm", 2202),
          ("jnxOpticsPowerLowAlarm", 2203),
          ("jnxOpticsRxCarrierFreqHighThreshAlert", 2219),
          ("jnxOpticsRxCarrierFreqLowThreshAlert", 2220),
          ("jnxOpticsRxLossAvgPowerAlarm", 2211),
          ("jnxOpticsRxPLLLockAlarm", 2209),
          ("jnxOpticsRxPowerHighThreshAlert", 2215),
          ("jnxOpticsRxPowerLowThreshAlert", 2216),
          ("jnxOpticsTemperatureHighAlarm", 2206),
          ("jnxOpticsTemperaturelowAlarm", 2207),
          ("jnxOpticsTxPLLLockAlarm", 2208),
          ("jnxOpticsTxPowerHighThreshAlert", 2213),
          ("jnxOpticsTxPowerLowThreshAlert", 2214),
          ("jnxOpticsWavelenthLockErr", 2201),
          ("jnxOverTemperature", 2241),
          ("jnxPowerSupplyFailure", 2247),
          ("jnxoptIfOdukTcmBdiAlarm", 2234),
          ("jnxoptIfOdukTcmCSfAlarm", 2238),
          ("jnxoptIfOdukTcmDegAlarm", 2236),
          ("jnxoptIfOdukTcmIaeAlarm", 2237),
          ("jnxoptIfOdukTcmLckAlarm", 2233),
          ("jnxoptIfOdukTcmOciAlarm", 2232),
          ("jnxoptIfOdukTcmSSfAlarm", 2239),
          ("jnxoptIfOdukTcmTSfAlarm", 2240),
          ("jnxoptIfOdukTcmTimAlarm", 2235),
          ("jnxoptIfOtnLofAlarm", 2222),
          ("jnxoptIfOtnLomAlarm", 2223),
          ("jnxoptIfOtnLosAlarm", 2221),
          ("jnxoptIfOtuBdiAlarm", 2225),
          ("jnxoptIfOtuBiaeAlarm", 2228),
          ("jnxoptIfOtuDegAlarm", 2230),
          ("jnxoptIfOtuFecExcessiveErrsAlarm", 2231),
          ("jnxoptIfOtuIaeAlarm", 2227),
          ("jnxoptIfOtuSsfAlarm", 2224),
          ("jnxoptIfOtuTimAlarm", 2226),
          ("jnxoptIfOtuTsfAlarm", 2229),
          ("k5LosSide1", 6121),
          ("k5LosSide2", 6122),
          ("k5LosSide3", 6123),
          ("k5LosSide4", 6124),
          ("k5LosSide5", 6125),
          ("k5LosSide6", 6126),
          ("k5LosSide7", 6127),
          ("k6LosSide1", 6128),
          ("k6LosSide2", 6129),
          ("k6LosSide3", 6130),
          ("k6LosSide4", 6131),
          ("k6LosSide5", 6132),
          ("k6LosSide6", 6133),
          ("k6LosSide7", 6134),
          ("k7LosSide2", 6135),
          ("k7LosSide3", 6136),
          ("k7LosSide4", 6137),
          ("k7LosSide5", 6138),
          ("k7LosSide6", 6139),
          ("k7LosSide7", 6140),
          ("k7LosSide8", 6141),
          ("k7LosSideStdby", 6142),
          ("k8LosSide2", 6143),
          ("k8LosSide3", 6144),
          ("k8LosSide4", 6145),
          ("k8LosSide5", 6146),
          ("k8LosSide6", 6147),
          ("k8LosSide7", 6148),
          ("k8LosSide8", 6149),
          ("k8LosSideStdby", 6150),
          ("kP", 112),
          ("keyExchangedForced", 3597),
          ("krs", 113),
          ("ksd", 114),
          ("kss", 115),
          ("kzd", 116),
          ("lAGprotectionNotAvailable", 9613),
          ("lContFail", 123),
          ("lOpen", 3497),
          ("lTan", 172),
          ("lagmbrfail", 3989),
          ("lanaddr", 117),
          ("lapdConfigMismatch", 6705),
          ("lapdDown", 6640),
          ("laser", 6163),
          ("laser-4-TempTooHigh", 3605),
          ("laser-4-TempTooLow", 3606),
          ("laserAging", 769),
          ("laserBiasCurrAbnormal", 3086),
          ("laserBiasCurrentHigh", 6706),
          ("laserBiasEndOfLife", 8030),
          ("laserBiasEoL", 497),
          ("laserBiasOutOfLimits", 6514),
          ("laserCurrent", 118),
          ("laserCurrentTooHigh", 938),
          ("laserCurrentTooLow", 940),
          ("laserDegrade", 507),
          ("laserDisabled", 6707),
          ("laserEndOfLife", 3084),
          ("laserFail", 1791),
          ("laserFailure", 6708),
          ("laserOnDelay", 3655),
          ("laserPowerHigh", 119),
          ("laserPowerLow", 120),
          ("laserPowerOutOfLock", 6709),
          ("laserSafetyBusFailure", 7844),
          ("laserShutdown", 6710),
          ("laserStatus", 6164),
          ("laserTecEndOfLife", 8032),
          ("laserTecEoL", 498),
          ("laserTempOoR", 499),
          ("laserTempOutOfRange", 6711),
          ("laserTempTooHigh", 2025),
          ("laserTempTooLow", 2026),
          ("laserTemperatureClientFail", 398),
          ("laserTemperatureOutOfRange", 121),
          ("laserTemperatureProblem", 463),
          ("laserTemperatureRingFail", 397),
          ("laserWaveOutOfLock", 6712),
          ("laserdegrade", 8031),
          ("lasertempOutOfRange", 8033),
          ("latchOpen", 9525),
          ("latchTriggered", 10024),
          ("latencyTooHigh", 3562),
          ("latencyTooLow", 3563),
          ("lcascrc", 3868),
          ("lcndcn", 122),
          ("lcpfail", 3920),
          ("lcploopback", 3921),
          ("lctUserInWriteAccess", 788),
          ("ldFail", 9516),
          ("line1Dccm", 6151),
          ("line1Dccr", 6152),
          ("line1EDccr", 6153),
          ("line1RxClockLos", 6154),
          ("line1TxClockLos", 6155),
          ("line1WDccr", 6156),
          ("line2Dccm", 6157),
          ("line2Dccr", 6158),
          ("line2EDccr", 6159),
          ("line2RxClockLos", 6160),
          ("line2TxClockLos", 6161),
          ("line2WDccr", 6162),
          ("lineAlarmIndicationSignal", 8001),
          ("lineCardFreqNotSupported", 1914),
          ("lineOrderError", 2075),
          ("lineRefClockProblem", 1997),
          ("lineRemoteDefetcIndication", 8061),
          ("linefailure", 3330),
          ("linkAggregationControlProtocolFailure", 9489),
          ("linkAttenuationTooHigh", 3551),
          ("linkAttenuationTooLow", 3550),
          ("linkControlSequenceFail1", 989),
          ("linkControlSequenceFail2", 990),
          ("linkControlSequenceFail3", 991),
          ("linkControlSequenceFail4", 992),
          ("linkDown", 564),
          ("linkFailure", 8130),
          ("linkFailureCount15", 3404),
          ("linkFailureCount24", 3405),
          ("linkFailureNOSReceiveState", 3400),
          ("linkFailureNOSReceiveStateEgress", 3402),
          ("linkFailureNOSTransmitState", 3401),
          ("linkFailureNOSTransmitStateEgress", 3403),
          ("linkIdentificationCodeError", 6167),
          ("linkLoss", 904),
          ("linkManuallyShutDown", 4553),
          ("linkNotAvailable", 785),
          ("linkPortAStatus", 9844),
          ("linkPortBStatus", 9845),
          ("linkPortMStatus", 9846),
          ("linkRemoteFault", 784),
          ("linkStateMismatch", 3412),
          ("lnkDown", 3477),
          ("lnkInt", 124),
          ("lnkdeactivated", 3922),
          ("lnkdn", 3923),
          ("lnkdownautonegfailed", 3924),
          ("lnkdowncablefault", 3925),
          ("lnkdowncableremoved", 3926),
          ("lnkdownlpbkfault", 3927),
          ("lnkdownmasterslavecfg", 3928),
          ("lnkdownunisolated", 3929),
          ("loa", 125),
          ("loc", 126),
          ("localChassisConfiguring", 2005),
          ("localConf", 2011),
          ("localEquipmentMismatch", 2010),
          ("localFanFailure", 2021),
          ("localFault", 3508),
          ("localOscLevelAbnormal", 3629),
          ("localOscTemperatureTooHigh", 3623),
          ("localOscTemperatureTooLow", 3622),
          ("localOscill", 6168),
          ("localPowerFail", 2019),
          ("localTemperatureTooHigh", 2017),
          ("localVoltageTooHigh", 2015),
          ("localVoltageTooLow", 2013),
          ("localchassismismatch", 2006),
          ("localchassismissing", 2007),
          ("lockedDefect", 862),
          ("lockedDefectEgress", 4837),
          ("lockout", 3930),
          ("lockoutEastWorkRing", 6713),
          ("lockoutEastWorkSpan", 6714),
          ("lockoutProtAllSpans", 6715),
          ("lockoutProtEast", 6716),
          ("lockoutProtFromEastK1", 6717),
          ("lockoutProtFromWestK1", 6718),
          ("lockoutProtWest", 6719),
          ("lockoutWestWorkRing", 6720),
          ("lockoutWestWorkSpan", 6721),
          ("lof", 127),
          ("lofEgress", 7814),
          ("lofLom", 863),
          ("lofOtu", 752),
          ("lofProtSide", 6619),
          ("lofRfcoh", 6169),
          ("lofTrib", 6170),
          ("logIsFull", 1810),
          ("logMemoryThresholdCrossed", 6515),
          ("logOccupancyThresholdReached", 1809),
          ("logWriteFail", 6722),
          ("lom", 128),
          ("lomFarEnd", 129),
          ("loop", 472),
          ("loopNT1", 130),
          ("loopback", 2002),
          ("loopbackError", 3167),
          ("lop", 131),
          ("los", 132),
          ("los2Mbps", 6517),
          ("los2Mhz", 6518),
          ("losA1", 134),
          ("losA2", 135),
          ("losB1", 137),
          ("losB2", 138),
          ("losInBitsPrimaryReference", 6806),
          ("losInBitsSecondaryRef", 6810),
          ("losInDem", 6519),
          ("losInMod", 6520),
          ("losInRx", 6521),
          ("losInSTM", 6522),
          ("losInTx", 6523),
          ("losInXPICProtSide", 6621),
          ("losInXpic", 6524),
          ("losK21", 6171),
          ("losK22", 6172),
          ("losK5", 6173),
          ("losK6", 6174),
          ("losK7", 6175),
          ("losK8", 6176),
          ("losS2M", 139),
          ("losUK2", 164),
          ("losa", 133),
          ("losb", 136),
          ("losd", 760),
          ("losloc", 3933),
          ("loss48V", 140),
          ("lossAC", 141),
          ("lossAtApplicationInterface", 4000),
          ("lossAttProgress", 3532),
          ("lossOfActivity", 142),
          ("lossOfActivityRx", 912),
          ("lossOfActivityTx", 911),
          ("lossOfAddSignal", 927),
          ("lossOfCarrier", 143),
          ("lossOfClockLock", 3469),
          ("lossOfClockSignal6Mhz", 6516),
          ("lossOfClockSourceA", 849),
          ("lossOfClockSourceB", 850),
          ("lossOfClockSourceC", 846),
          ("lossOfClockSourceD", 855),
          ("lossOfCodeGroupDelineation", 4845),
          ("lossOfD2an", 144),
          ("lossOfFrame", 8034),
          ("lossOfFrameAndMultiframe", 3417),
          ("lossOfFrameAtOtu", 8036),
          ("lossOfFrameDelineation", 880),
          ("lossOfFrameDelineationGFP", 1956),
          ("lossOfFrameDelineationGfp", 9485),
          ("lossOfFrameDelineationSec", 9553),
          ("lossOfFrameOSC", 7801),
          ("lossOfFrameT31", 900),
          ("lossOfFrameT32", 901),
          ("lossOfHeartbeat", 1849),
          ("lossOfHigherBitsTimeSrc", 6807),
          ("lossOfInternalTiming", 145),
          ("lossOfLane", 3632),
          ("lossOfLaneAlign", 2152),
          ("lossOfLaneAlignment", 4503),
          ("lossOfLaneOtu", 9870),
          ("lossOfLight", 2120),
          ("lossOfLinkPulse", 505),
          ("lossOfLock", 747),
          ("lossOfLockT0", 146),
          ("lossOfLockT4", 147),
          ("lossOfLowerBitsTimingSrc", 6811),
          ("lossOfMfiOpu", 9871),
          ("lossOfMultiChannelSynchronisation", 1926),
          ("lossOfMultiframe", 8037),
          ("lossOfMultiframeOPU", 2153),
          ("lossOfMultiframeT31", 898),
          ("lossOfMultiframeT32", 899),
          ("lossOfOPUMultiframeIndicator", 4508),
          ("lossOfOip", 500),
          ("lossOfOop", 501),
          ("lossOfOpticalInputPower", 8044),
          ("lossOfOpticalOutputPower", 8045),
          ("lossOfPRBSLock", 3459),
          ("lossOfPilotSignal", 3556),
          ("lossOfPointer", 8040),
          ("lossOfProtectionSignal", 6525),
          ("lossOfSequence", 8074),
          ("lossOfSignal", 8042),
          ("lossOfSignalCPort", 3539),
          ("lossOfSignalCount15", 3408),
          ("lossOfSignalCount24", 3409),
          ("lossOfSignalGFP", 2140),
          ("lossOfSignalInGFP", 9619),
          ("lossOfSignalInput1", 1934),
          ("lossOfSignalInput2", 1935),
          ("lossOfSignalInput3", 1936),
          ("lossOfSignalInput4", 1937),
          ("lossOfSignalNPort", 9864),
          ("lossOfSignalOSC", 7800),
          ("lossOfSignalPQM", 965),
          ("lossOfSignalPayload", 7780),
          ("lossOfSignalT", 781),
          ("lossOfStationTimingInput", 4834),
          ("lossOfSyncCommPartner", 967),
          ("lossOfSyncInGFP", 9620),
          ("lossOfSynch", 568),
          ("lossOfSynchronization", 8046),
          ("lossOfSynchronizationCount15", 3406),
          ("lossOfSynchronizationCount24", 3407),
          ("lossOfSynchronizationWord", 1927),
          ("lossOfTCM", 998),
          ("lossOfTandemConnection", 460),
          ("lossOfTandemConnectionEgress", 4839),
          ("lossOfTestSeqSynchOpu", 3620),
          ("lossOfTimeReference", 3474),
          ("lossOfTiming", 148),
          ("lossOfTimingInput", 459),
          ("lossOfTimingOutput", 1820),
          ("lossOfTimingReference", 149),
          ("lossOfTimingSource", 6781),
          ("lossOfTimingT1", 150),
          ("lossOfTimingT11", 151),
          ("lossOfTimingT1121", 152),
          ("lossOfTimingT12", 153),
          ("lossOfTimingT1222", 154),
          ("lossOfTimingT13", 155),
          ("lossOfTimingT14", 156),
          ("lossOfTimingT15", 894),
          ("lossOfTimingT16", 895),
          ("lossOfTimingT17", 896),
          ("lossOfTimingT18", 897),
          ("lossOfTimingT2", 157),
          ("lossOfTimingT21", 158),
          ("lossOfTimingT22", 159),
          ("lossOfTimingT3", 160),
          ("lossOfTimingT31", 161),
          ("lossOfTimingT32", 162),
          ("lossOfTimingT4", 163),
          ("lossOip", 9514),
          ("lossOsc", 3520),
          ("lossTimingInput", 4511),
          ("lossofCommExtShelf", 8129),
          ("lossofLinkPulse", 8043),
          ("lossofsequencesynchronization", 2050),
          ("lossofsequencesynchronizationCom", 2116),
          ("lowBatteryVoltage", 9242),
          ("lowCFSUFlow", 3453),
          ("lowCablePressure", 165),
          ("lowCurrentThresholdCrossed", 8096),
          ("lowEarlyWarning", 6165),
          ("lowEdfaInputPower", 9494),
          ("lowFastBer", 6166),
          ("lowFuel", 167),
          ("lowHumid", 9244),
          ("lowHumidity", 168),
          ("lowLineOutputPower", 9497),
          ("lowOipThresholdCrossed", 8102),
          ("lowOopThresholdCrossed", 8103),
          ("lowOrderCapacityMismatch", 8199),
          ("lowTemp", 9246),
          ("lowTempThresholdCrossed", 8104),
          ("lowTemperature", 169),
          ("lowVoltageThresholdCrossed", 8105),
          ("lowWater", 170),
          ("lowerCoolingFanFail", 166),
          ("lowerCoolingFanMissing", 909),
          ("lowestCurrentThresholdCrossed", 8097),
          ("lowestOipThresholdCrossed", 8098),
          ("lowestOopThresholdCrossed", 8099),
          ("lowestTempThresholdCrossed", 8100),
          ("lowestVoltageThresholdCrossed", 8101),
          ("lpPayloadMismatch", 8071),
          ("lpRemoteDefectIndication", 8062),
          ("lpUnequipped", 8114),
          ("lpt", 972),
          ("lsa", 171),
          ("lscloss1", 1802),
          ("lscloss2", 1803),
          ("lscmismatch1", 1804),
          ("lscmismatch2", 1805),
          ("lsu1Missing", 907),
          ("lsu2Missing", 908),
          ("lsuMissing", 881),
          ("ltiT0", 173),
          ("ltiT0-minor", 1854),
          ("ltiT4", 174),
          ("ltiT4-minor", 1855),
          ("ltuFailure", 175),
          ("ltuMissing", 176),
          ("ltuTypeMismatch", 177),
          ("mIBFullMajor", 3472),
          ("mIBFullMinor", 3471),
          ("mIIConnectorProblem", 622),
          ("macsLimitReached", 1036),
          ("mainBattery", 6180),
          ("mainMasterOscSyncLos", 6177),
          ("mainRxReceivedLevelDown", 6526),
          ("mainTribSyncLos", 6178),
          ("majAlrExtUnmangedNE", 618),
          ("major", 178),
          ("manReversionRequired", 6641),
          ("manSwitchRingEast", 6725),
          ("manSwitchRingEastK1", 6723),
          ("manSwitchRingWest", 6726),
          ("manSwitchRingWestK1", 6724),
          ("manSwitchSpanEast", 6729),
          ("manSwitchSpanEastK1", 6727),
          ("manSwitchSpanWest", 6730),
          ("manSwitchSpanWestK1", 6728),
          ("mansw", 3361),
          ("manualOperation", 6179),
          ("manufacturingItemNumberFault", 836),
          ("masterOscSyncLos", 6185),
          ("masterOscSyncOn", 6186),
          ("mateCardClockFailure", 4526),
          ("maxKeyExchFail", 3595),
          ("maxKeyexchDegrade", 3594),
          ("maxPowerConsEquipModulesToHigh", 3396),
          ("maxPowerConsProvModulesToHigh", 3397),
          ("maximumInformationRate", 1930),
          ("maximumNumberOfUnsuccessfulLogins", 4520),
          ("meaChannelMismatch", 3659),
          ("meaSwRevision", 3684),
          ("measurementFailed", 3454),
          ("measurementFailure", 956),
          ("measurementFailureFSU", 1933),
          ("memberNotDeskewable", 9405),
          ("memoryCardFailure", 2074),
          ("messageLossSpeq", 3647),
          ("mgmtEthLinkDown", 9953),
          ("mgmtRestricted", 9963),
          ("mibDiscrepancy", 179),
          ("mibDownloadRunning", 789),
          ("mibEmNotValid", 180),
          ("mibFailure", 7817),
          ("mibFileMismatch", 4833),
          ("mibFlashFail", 181),
          ("mibFlashMissing", 182),
          ("mibNeNotValid", 183),
          ("mibs256required", 2049),
          ("midstageFault", 3085),
          ("minAlrExtUnmangedNE", 619),
          ("minor", 184),
          ("misMatched", 9965),
          ("misWired", 9964),
          ("miscDiscInput1", 1823),
          ("miscDiscInput2", 1824),
          ("miscDiscInput3", 1825),
          ("miscDiscInput4", 1826),
          ("miscellaneous", 9248),
          ("mismatch", 3955),
          ("mismatchOpticalModule", 2124),
          ("mismatchOpticalModule1", 1975),
          ("mismatchOpticalModule2", 2107),
          ("mismatchOpticalModule3", 2108),
          ("mismatchOpticalModule4", 2109),
          ("mismatchedModules", 848),
          ("missingOpticalModule", 2123),
          ("missingOpticalModule1", 1884),
          ("missingOpticalModule2", 1885),
          ("missingOpticalModule3", 1886),
          ("missingOpticalModule4", 1887),
          ("missingOpticalModuleLine1", 1942),
          ("mnd", 1780),
          ("mod", 186),
          ("modBlockFailure", 6527),
          ("modBlockFailureProtSide", 6630),
          ("modSideFail", 6183),
          ("modSyncOn", 6184),
          ("modemBoard", 6182),
          ("modulatorAlarm", 6181),
          ("modulatorOutOfLock", 6731),
          ("moduleBootProblem", 830),
          ("moduleCurrent", 187),
          ("moduleInsert", 2031),
          ("moduleMissing", 7789),
          ("moduleNotCertified", 7799),
          ("moduleProblem", 3456),
          ("moduleRemoved", 2032),
          ("moduleTypeMismatch", 3427),
          ("monitorPortAInputRefBad", 6785),
          ("monitorPortBInputRefBad", 6786),
          ("msAis", 6187),
          ("msAlarmIndicationSignal", 8002),
          ("msBersd", 9911),
          ("msBersf", 9912),
          ("msRdi", 6188),
          ("msRemoteDefectIndication", 8063),
          ("msRfi", 9913),
          ("msSignalDegraded", 8067),
          ("mspArchitectureMatchFailure", 6528),
          ("mspAutoSwitchSd", 6656),
          ("mspAutoSwitchSdFar", 6657),
          ("mspAutoSwitchSf", 6658),
          ("mspAutoSwitchSfFar", 6659),
          ("mspChannelMatchFailure", 6529),
          ("mspChannelMismatch", 6660),
          ("mspCpu1Failure", 6530),
          ("mspCpu2Failure", 6531),
          ("mspCpu3Failure", 6532),
          ("mspCpu4Failure", 6533),
          ("mspDirectionMatchFailure", 6534),
          ("mspFarEndProtectFail", 6661),
          ("mspForcedSwiToProt", 6662),
          ("mspForcedSwiToProtFar", 6663),
          ("mspForcedSwiToWork", 6664),
          ("mspForcedSwiToWorkFar", 6665),
          ("mspLockoutProtection", 6666),
          ("mspLockoutProtectionFar", 6667),
          ("mspManualSwitchProt", 6668),
          ("mspManualSwitchProtFar", 6669),
          ("mspModeMismatch", 6670),
          ("mspProtSwitchByteFail", 6671),
          ("mspProtSwitchDenial", 6672),
          ("mspSwitchToProtDnr", 6673),
          ("mspSwitchToProtDnrFar", 6674),
          ("mspSwitchToProtWtr", 6675),
          ("mspSwitchToProtWtrFar", 6676),
          ("mtieLimit1Exceeded", 826),
          ("mtieLimit2Exceeded", 827),
          ("mtxApsMissing", 1963),
          ("multiTransponderPowerFail", 2122),
          ("multiframeCableProblem", 188),
          ("multipleFanFail", 754),
          ("multipleFanFailure", 8047),
          ("multipleFansFailure", 1974),
          ("multipleRmNode", 1033),
          ("multiplexStructIndicationMism", 1099),
          ("multiplexStructureIdentifierMismatch", 3416),
          ("muxDemuxProblem", 795),
          ("mwbCommunicationProblem", 929),
          ("mwbModuleProblem", 928),
          ("nas", 189),
          ("nbit", 190),
          ("ncm", 191),
          ("neBreakdown", 192),
          ("neConfigurationBackupFailed", 4547),
          ("neFailure", 193),
          ("neInRealignment", 786),
          ("neNameMismatch", 4505),
          ("neProblem", 194),
          ("necUploadOrResynchFailed", 2001),
          ("negativeSlip", 1837),
          ("neighborUnreachable", 9566),
          ("netAMisConfig", 1045),
          ("netBMisConfig", 1044),
          ("netOptAFault", 1043),
          ("netOptBFault", 1042),
          ("netSfpAMismatch", 1041),
          ("networkReferenceClockQualityDown", 6535),
          ("nip", 971),
          ("nirFail1", 9249),
          ("nirFail2", 9250),
          ("nirFail3", 9251),
          ("nirFail4", 9252),
          ("nirWarn1", 9253),
          ("nirWarn2", 9254),
          ("nirWarn3", 9255),
          ("nirWarn4", 9256),
          ("nk", 195),
          ("no2MbitMode", 196),
          ("noASEDetected", 390),
          ("noClockEdgeInBitsPrimRef", 6808),
          ("noClockEdgeInBitsSecRef", 6812),
          ("noConfigFileLoaded", 6732),
          ("noConnectionToOCU40", 1899),
          ("noData", 496),
          ("noFramesReceivedGFP", 9524),
          ("noFreeLowOrderCapacity", 8198),
          ("noInputPower", 1786),
          ("noLightDetected", 3420),
          ("noLightDetectedC1", 979),
          ("noLightDetectedC2", 980),
          ("noLightDetectedC3", 983),
          ("noLightDetectedC4", 984),
          ("noOscDuringStartup", 391),
          ("noResponseReceived", 2000),
          ("noSlavePresent", 1928),
          ("noSsmStatus", 829),
          ("noSyncMaster", 1923),
          ("noTimingMaster", 993),
          ("noVCDBMigrationPossible", 1901),
          ("noValidT3Signal", 197),
          ("nodeIdMismatch", 6733),
          ("notEnoughProcesses", 1812),
          ("notInSynch", 1018),
          ("notificationQueueOverflow", 7812),
          ("notificationQueueOverflowHiT75", 1966),
          ("np", 469),
          ("npd", 198),
          ("npd2", 199),
          ("npf", 200),
          ("nr", 201),
          ("ntpPeerUnreachable", 9970),
          ("ntpServer1Unreachable", 3091),
          ("ntpServer2Unreachable", 3092),
          ("ntpServer3Unreachable", 3093),
          ("ntpServerAccessFailed", 1985),
          ("oA", 202),
          ("oCH", 203),
          ("oSCLaserFail", 208),
          ("oSCLaserTxFail", 7902),
          ("oSCbandLos", 9600),
          ("oaInputLos", 1831),
          ("oaOutputLos", 1832),
          ("oaPowerFailure", 1833),
          ("oaPumpBiasOutRange", 1834),
          ("oaTemperatureOutOfRange", 1835),
          ("oalActivationInProgress", 396),
          ("oalLaserDegrade", 392),
          ("oalLoopFail", 395),
          ("ochOci", 9907),
          ("oduAis", 9508),
          ("oduAutoShutdownRxAIS", 9874),
          ("oduAutoShutdownTxAIS", 9875),
          ("oduBdi", 9512),
          ("oduBersd", 9918),
          ("oduDeg", 9513),
          ("oduHardwareMismatch", 6189),
          ("oduLck", 9509),
          ("oduLine1RxClockLos", 6190),
          ("oduLine1TxClockLos", 6191),
          ("oduLine2RxClockLos", 6193),
          ("oduLine2TxClockLos", 6192),
          ("oduLofLom", 9507),
          ("oduMsim", 9501),
          ("oduOci", 9510),
          ("oduPlm", 9500),
          ("oduSwitch", 6194),
          ("oduSwitchMismatch", 6195),
          ("oduTim", 9511),
          ("oduTribMsiMismatch", 3658),
          ("ogicalLanesSkewTooHigh", 3691),
          ("ohBus", 204),
          ("ohBusRxFailureSide1", 6198),
          ("ohBusRxFailureSide2", 6199),
          ("ohBusRxFailureSide3", 6200),
          ("ohBusRxFailureSide4", 6201),
          ("ohBusRxFailureSide5", 6202),
          ("ohBusRxFailureSide6", 6203),
          ("ohBusRxFailureSide7", 6204),
          ("ohBusRxFailureSide8", 6205),
          ("ohBusRxFailureSideA", 6196),
          ("ohBusRxFailureSideB", 6197),
          ("ohBusRxSide1", 6230),
          ("ohBusRxSide2", 6231),
          ("ohBusRxSideA", 6206),
          ("ohBusRxSideB", 6209),
          ("ohBusRxSideB12", 6207),
          ("ohBusRxSideB13", 6208),
          ("ohBusRxSideB24", 6210),
          ("ohBusRxSideBStdby3", 6211),
          ("ohBusRxSideStdby", 6212),
          ("ohBusTxFailSide1", 6215),
          ("ohBusTxFailSide2", 6216),
          ("ohBusTxFailSide3", 6217),
          ("ohBusTxFailSide4", 6218),
          ("ohBusTxFailSide5", 6219),
          ("ohBusTxFailSide6", 6220),
          ("ohBusTxFailSide7", 6221),
          ("ohBusTxFailSide8", 6222),
          ("ohBusTxFailSideA", 6213),
          ("ohBusTxFailSideB", 6214),
          ("ohBusTxSide1", 6232),
          ("ohBusTxSide2", 6233),
          ("ohBusTxSideA", 6223),
          ("ohBusTxSideB", 6224),
          ("ohBusTxSideB12", 6225),
          ("ohBusTxSideB13", 6226),
          ("ohBusTxSideB24", 6227),
          ("ohBusTxSideBStdby3", 6228),
          ("ohBusTxSideStdby", 6229),
          ("oipTooHigh", 502),
          ("oipTooLow", 941),
          ("oliConnectionCableFail", 974),
          ("omdModuleProblem", 2118),
          ("onboardFlashFail", 2105),
          ("onboardFlashFailure", 3419),
          ("oopFail", 9515),
          ("oopOoR", 2027),
          ("oopTooHigh", 942),
          ("oopTooLow", 503),
          ("oosDisabledLckOduRx", 9876),
          ("oosDisabledLckOduTrmt", 9872),
          ("oosPrePostSig", 3399),
          ("oosPrePostSigAfterPrecompFailed", 3505),
          ("oosPrePostSigEstablishFailed", 3504),
          ("oosPrePostSigInSetUpProcess", 3500),
          ("oosPrePostSigInTearDownProcess", 3501),
          ("openConnectionIndication", 997),
          ("openConnectionIndicationEgress", 4838),
          ("openDoor", 9257),
          ("opmAbnormalCondition", 3536),
          ("optBoosterTemperature", 205),
          ("optLowSpeq", 3649),
          ("optPort1", 913),
          ("optPort2", 914),
          ("optPort3", 915),
          ("optPort4", 916),
          ("optPreampTemperature", 207),
          ("optReflection", 420),
          ("optRoutingParamNok", 6647),
          ("optSignalFailure", 3535),
          ("opticPowerReceiveTooLow", 206),
          ("opticalAmplifierGainFailure", 410),
          ("opticalAmplifierReceiveFailure", 468),
          ("opticalAmplifierTransmitDegrade", 412),
          ("opticalFilterTemperatureFailure", 409),
          ("opticalInputPowerTooHigh", 8048),
          ("opticalInputPowerTooLow", 8049),
          ("opticalPowerReceivedTooLow", 2138),
          ("opticalPowerTransmittedTooLow", 2137),
          ("opticalPowerTxLOS", 3087),
          ("opticalPreamplifierReceiveFailure", 3461),
          ("opticalTransmitPowerDegraded", 6537),
          ("opticalTransmitPowerOutOfRange", 6536),
          ("opuClientSignalFail", 4518),
          ("osaCalibrationDateExpired", 796),
          ("osaFail", 421),
          ("osaModuleProblem", 797),
          ("osaPowerFail", 455),
          ("oscDirectionMismatch", 1905),
          ("oscFiberMissingSpeq", 3648),
          ("oscLossOfLock", 7788),
          ("oscPwrTooHigh", 3509),
          ("oscPwrTooLow", 3510),
          ("oscTransmitDegrade", 3431),
          ("oscVersionMismatch", 995),
          ("oscmBranchError", 756),
          ("osi2IpConfig", 470),
          ("ospf-auth-key-exp", 9590),
          ("ospfIpServerNotAvailable", 3519),
          ("otm", 7202),
          ("otnLofAlarm", 9001),
          ("otnLomAlarm", 9002),
          ("otnLosAlarm", 9000),
          ("otnOduAisAlarm", 9016),
          ("otnOduBbeThreholdAlarm", 9024),
          ("otnOduBdiAlarm", 9019),
          ("otnOduEsThreholdAlarm", 9025),
          ("otnOduLckAlarm", 9018),
          ("otnOduOciAlarm", 9017),
          ("otnOduRxApsChange", 9023),
          ("otnOduSdAlarm", 9021),
          ("otnOduSesThreholdAlarm", 9026),
          ("otnOduSfAlarm", 9022),
          ("otnOduTtimAlarm", 9020),
          ("otnOduUasThreholdAlarm", 9027),
          ("otnOpuPMTAlarm", 9028),
          ("otnOtuAisAlarm", 9004),
          ("otnOtuBbeThreholdAlarm", 9012),
          ("otnOtuBdiAlarm", 9005),
          ("otnOtuEsThreholdAlarm", 9013),
          ("otnOtuFecDegradedErrsAlarm", 9011),
          ("otnOtuFecExcessiveErrsAlarm", 9010),
          ("otnOtuIaeAlarm", 9007),
          ("otnOtuSdAlarm", 9008),
          ("otnOtuSesThreholdAlarm", 9014),
          ("otnOtuSfAlarm", 9009),
          ("otnOtuTtimAlarm", 9006),
          ("otnOtuUasThreholdAlarm", 9015),
          ("otnWavelengthlockAlarm", 9003),
          ("otsApsMissing", 1962),
          ("otsRecoverMode", 9529),
          ("otuBdi", 9505),
          ("otuBersd", 9919),
          ("otuDeg", 9506),
          ("otuFecTypeMismatch", 9908),
          ("otuLof", 9502),
          ("otuLom", 9503),
          ("otuTim", 9504),
          ("outOfSequenceGFP", 9522),
          ("outOfSpace", 1814),
          ("outgoingDefectIndication", 418),
          ("outputFrequencyStatusWithinSpecification", 813),
          ("outputLossOfLight", 1881),
          ("outputPllStatus", 854),
          ("outputPortFault", 856),
          ("outputPortProblem", 2127),
          ("outputPower", 6234),
          ("outputPowerFault", 9865),
          ("outputPowerLow", 3451),
          ("overCurrent", 1925),
          ("overPower1M", 3450),
          ("overPowerRx", 2119),
          ("overPowerTx", 2121),
          ("overflow", 3476),
          ("overheadBdi", 9916),
          ("overheadFdi", 9925),
          ("overload", 764),
          ("overtemp", 3956),
          ("overvoltage", 3957),
          ("ows", 209),
          ("pLLUn", 3499),
          ("pLMVF", 3358),
          ("pam", 7200),
          ("partialLossOfCapacity", 9606),
          ("partialLossOfMultiChannelSynchronisation", 1929),
          ("partitioned", 776),
          ("partnerSubagentMissing", 1987),
          ("passwordExpired", 954),
          ("passwordExpiresSoon", 4519),
          ("passwordWillExpireSoon", 981),
          ("patchApplyCompleted", 9985),
          ("patchApplyFail", 9984),
          ("patchApplyProgress", 9983),
          ("patchDwCompleted", 9979),
          ("pathAlarmIndicationSignal", 8003),
          ("pathLabelMismatch", 4844),
          ("pathPayloadMismatch", 8072),
          ("pathProtSelectorAlarm", 6734),
          ("pathProtectionNotAvailable", 969),
          ("pathRemoteDefectIndication", 8064),
          ("pathSelectorMismatch", 6642),
          ("pathSignalDegraded", 8068),
          ("pathTraceIdMismatch", 6538),
          ("pathTraceInconsistency", 520),
          ("pathTraceMismatch", 210),
          ("pathTraceMismatchAsap", 2104),
          ("pathTraceMismatchEgress", 7820),
          ("pathUnequipped", 8115),
          ("payloadBdi", 9917),
          ("payloadFdi", 9926),
          ("payloadLabelMismatchGFP", 9486),
          ("payloadLengthIndicatorGfp", 9450),
          ("payloadMismatch", 861),
          ("payloadMissingIndication", 9932),
          ("pcbBusFail", 211),
          ("pccfail1", 1798),
          ("pccfail2", 1799),
          ("pccfail3", 1800),
          ("pcsSignalDegrade", 3363),
          ("pecloss", 1801),
          ("peerConfigMismatch", 3173),
          ("peerTime", 9848),
          ("performanceLogThresholdReached", 1915),
          ("phaseHwFault", 835),
          ("phaseMeasurementHwFault", 831),
          ("phaseShifter", 6235),
          ("pilot", 212),
          ("pilotReceiveLevelHigh", 3559),
          ("plannedCardMismatch", 8007),
          ("plannedCardMissing", 8008),
          ("plcr", 1783),
          ("plct", 1782),
          ("pllSyncFailureClient", 404),
          ("pllSyncFailureRing", 403),
          ("pllUnlock", 8188),
          ("plugInMismatch", 920),
          ("plugInMissing", 919),
          ("plugInNotApproved", 921),
          ("plugInSfpMismatch", 8053),
          ("plugInSfpMissing", 8054),
          ("plugInSfpNotAdvaApproved", 8055),
          ("plugInserted", 2034),
          ("plugRemoved", 2033),
          ("pmdFail", 3465),
          ("pnvmod", 213),
          ("poolAddressError", 4543),
          ("poolBaseMismatch", 4521),
          ("poolPortBaseMismatch", 4522),
          ("port1BothTimingLinkDown", 6787),
          ("port1TimingLinkDown", 6788),
          ("port2BothTimingLinkDown", 6789),
          ("port2TimingLinkDown", 6790),
          ("port3BothTimingLinkDown", 6791),
          ("port3TimingLinkDown", 6792),
          ("port4BothTimingLinkDown", 6793),
          ("port4TimingLinkDown", 6794),
          ("port5BothTimingLinkDown", 6795),
          ("port5TimingLinkDown", 6796),
          ("portAbsent", 886),
          ("portDisabled", 480),
          ("portInLoopbackMode", 6735),
          ("portMismatch", 887),
          ("portNotLinked", 483),
          ("portNotPartitioned", 481),
          ("portinLoopback", 9560),
          ("positionUnknownFault", 837),
          ("positiveSlip", 1836),
          ("powerA", 859),
          ("powerAMissing", 9603),
          ("powerB", 860),
          ("powerBMissing", 9604),
          ("powerBusFail", 417),
          ("powerConsumptionOverload", 1839),
          ("powerControlSuspicious", 1984),
          ("powerDifferentialAlarm", 966),
          ("powerDriftFailure", 955),
          ("powerDriftHighDegrade", 214),
          ("powerDriftLowDegrade", 215),
          ("powerDriftLowFailure", 798),
          ("powerEqualizationFail", 1988),
          ("powerFail", 515),
          ("powerLossSuspicious", 2135),
          ("powerModuleFailure", 4537),
          ("powerOutOfRange", 3457),
          ("powerOverLimit100G", 2149),
          ("powerProblem1", 216),
          ("powerProblem12", 217),
          ("powerProblem13", 185),
          ("powerProblem2", 218),
          ("powerProblem24", 393),
          ("powerProblem3", 219),
          ("powerProblem34", 220),
          ("powerProblem4", 221),
          ("powerSourceA-Fault", 1020),
          ("powerSourceB-Fault", 1021),
          ("powerSupply1Problem", 7782),
          ("powerSupply2Problem", 7783),
          ("powerSupply3Problem", 7784),
          ("powerSupply4Problem", 7785),
          ("powerSupplyA-AcFault", 1024),
          ("powerSupplyA-DcFault", 1022),
          ("powerSupplyA-Missing", 1026),
          ("powerSupplyB-AcFault", 1025),
          ("powerSupplyB-DcFault", 1023),
          ("powerSupplyB-Missing", 1027),
          ("powerSupplyFailure", 6775),
          ("powerSupplyFailure1U", 9601),
          ("powerSupplyFailure2", 6242),
          ("powerSupplyMajor", 9259),
          ("powerSupplyMinor", 9260),
          ("powerTooHighDegrade", 222),
          ("powerTooHighFailure", 223),
          ("powerTooLowDegrade", 224),
          ("powerTooLowFailure", 225),
          ("powersupplyFailure", 8056),
          ("ppcLimitExceededSpeq", 9869),
          ("ppcOutOfRangeSpeq", 3650),
          ("pqmModulemProblem", 799),
          ("prbsLossOfSeqSynch", 3618),
          ("prbsRcvActivated", 3616),
          ("prbsTrmtActivated", 3617),
          ("preamplifierStageTransmitFail", 3429),
          ("preemphaseFail", 1851),
          ("preemphasisFail", 3488),
          ("preemphasisFailure", 226),
          ("preemphasisSectionFail", 3423),
          ("pri", 227),
          ("primaryPathDown", 6643),
          ("primaryPower", 902),
          ("primntpsvrFailed", 3934),
          ("priorityChannelMismatch", 6539),
          ("probeLOSAsap", 1986),
          ("problemOpticalModule", 2139),
          ("processDown", 1813),
          ("processLockedOutSpeq", 9868),
          ("processProblem", 228),
          ("progflt", 9971),
          ("protMasterOscSync", 6237),
          ("protMasterOscSyncLos", 6238),
          ("protPassThroughXcUnres", 6767),
          ("protTribSyncLos", 6239),
          ("protectionBusX", 229),
          ("protectionBusXY", 230),
          ("protectionBusY", 231),
          ("protectionBypassCardFailure", 6236),
          ("protectionGroupProtectionFail", 2023),
          ("protectionGroupProtectionFailure", 8057),
          ("protectionGroupProtectionMismatch", 2024),
          ("protectionGroupprotectionMismatch", 8058),
          ("protectionLogicInconsistency", 402),
          ("protectionLogicProblem", 401),
          ("protectionRoleMismatch", 4514),
          ("protshelf", 1787),
          ("provPayloadMismatch", 3689),
          ("provisionError", 906),
          ("provisionerror", 8059),
          ("provisioningLocked", 3360),
          ("psFailure", 6540),
          ("psFilterAndDistributorPreAlarm", 6243),
          ("psUfab", 232),
          ("psUfan", 233),
          ("psu1", 6240),
          ("psu2", 6241),
          ("psu3", 6567),
          ("psu4", 6568),
          ("psuFault", 1040),
          ("psutp", 234),
          ("pump1TransmitDegrade", 3432),
          ("pump1TransmitFail", 3433),
          ("pump2TransmitDegrade", 3434),
          ("pump2TransmitFail", 3435),
          ("pump3TransmitDegrade", 3436),
          ("pump3TransmitFail", 3437),
          ("pump4TransmitDegrade", 3438),
          ("pump4TransmitFail", 3439),
          ("pumpDegrade", 3466),
          ("pumpFail", 3467),
          ("pumpFailure", 9261),
          ("pumpLaser1TempTooHigh", 3515),
          ("pumpLaser1TempTooLow", 3516),
          ("pumpLaser2TempTooHigh", 3517),
          ("pumpLaser2TempTooLow", 3518),
          ("pumpLaser3TempTooHigh", 3557),
          ("pumpLaser3TempTooLow", 3558),
          ("pumpLow", 235),
          ("pumpTemperature", 236),
          ("pumplaserfail", 1793),
          ("pumpsEol", 9593),
          ("pumpsManuallyDisabled", 4546),
          ("pumpsOff", 10059),
          ("pumpsShutdownTemperature", 9594),
          ("pumpsWarningTemperature", 9595),
          ("pwjbovrn", 3894),
          ("pwlatefrm", 3893),
          ("pwlof", 3892),
          ("pwr", 237),
          ("pwrControlSuspicious", 3485),
          ("pwrEqualizationFail", 3486),
          ("pwrLossSuspicious", 3487),
          ("pwrSupplyFailure", 9596),
          ("pwrlofs", 3891),
          ("pwrmod", 238),
          ("pwrnoinputunitfault", 3958),
          ("qA", 239),
          ("qInterfaceFault", 6244),
          ("qlink", 1790),
          ("qlinvalid", 3935),
          ("qlmismatch", 3936),
          ("qlsqlch", 3937),
          ("rAMFull", 3470),
          ("rFIL", 9951),
          ("radio15minG826BBEThresholdCrossed", 8244),
          ("radio15minG826ESThresholdCrossed", 8242),
          ("radio15minG826SESThresholdCrossed", 8243),
          ("radio1731AIS", 9776),
          ("radioACCESSSPIIntFail", 7824),
          ("radioACMSwitchLower", 8339),
          ("radioACMSwitchUpper", 8338),
          ("radioADMSideFail", 7762),
          ("radioAGCOFFinActiveCondition", 8148),
          ("radioAGCPREALMHSBY", 6851),
          ("radioAIS", 7703),
          ("radioAISHWProt", 7440),
          ("radioAISOut", 7709),
          ("radioAISRXAHWP", 7356),
          ("radioAISRXBHWP", 7220),
          ("radioAISTX", 8397),
          ("radioAISTXHWP", 7221),
          ("radioAISlocalIns", 7704),
          ("radioAISlocalInsA", 7705),
          ("radioAISlocalInsAP", 7706),
          ("radioAISlocalInsB", 7707),
          ("radioAISlocalInsBP", 7708),
          ("radioALCOFFinActiveCondition", 8149),
          ("radioATPCTxatMaxPower", 8291),
          ("radioATPCautodisabled", 8388),
          ("radioAUAIS", 8301),
          ("radioAULossOfPointer", 8302),
          ("radioAccessHWF", 7439),
          ("radioAccessModule1insertedbutnotenabled", 9799),
          ("radioAccessModule1insertedincorrectly", 9800),
          ("radioAccessModule2insertedbutnotenabled", 9808),
          ("radioAccessModule2insertedincorrectly", 9809),
          ("radioAccountLogisfilledtothefirstthreshold", 9839),
          ("radioAccountLogisfilledtothesecondthreshold", 9840),
          ("radioActiveAlarmPoint", 8258),
          ("radioAlarmIndicationSignalAISIn", 9816),
          ("radioAlignFPS", 7597),
          ("radioAlignmentFailure1", 7710),
          ("radioAlignmentFailure2", 7711),
          ("radioAsicAl", 7441),
          ("radioAutGC", 7357),
          ("radioAutonegotiationmismatch", 9830),
          ("radioAutonegspeedmismatchallocatedBWonport", 9722),
          ("radioB1BERexc", 7712),
          ("radioB1BerHWP", 7222),
          ("radioB1error", 9811),
          ("radioB2BERSFHWP", 7223),
          ("radioB2Ber3Prot", 7297),
          ("radioB2BerHWP", 7358),
          ("radioB2BerProt", 7296),
          ("radioB2computedBERthreshold", 8395),
          ("radioB2error", 9812),
          ("radioB3error", 9813),
          ("radioBBExpCF", 7361),
          ("radioBBExpCM", 7362),
          ("radioBBExpIf", 7363),
          ("radioBBI2CIntFail", 7823),
          ("radioBBSPIIntFail", 7822),
          ("radioBER4", 8233),
          ("radioBER5", 8234),
          ("radioBER6", 8235),
          ("radioBER7", 8236),
          ("radioBERTLbTestMode", 8289),
          ("radioBERexc", 7713),
          ("radioBERexcHSBY", 7714),
          ("radioBIP-2error", 9814),
          ("radioBSWForcedSwitch", 8151),
          ("radioBSWLockout", 8152),
          ("radioBSWManualSwitch", 8153),
          ("radioBSWTraffictoProtection", 8154),
          ("radioBipolarSwitchRequest", 8150),
          ("radioBoostOnlevel1", 8191),
          ("radioBoostOnlevel2", 8192),
          ("radioBoostOnlevel3", 8193),
          ("radioBoostOnlevel4", 8194),
          ("radioBoostOnlevel5", 8195),
          ("radioBufferOverflow", 8256),
          ("radioCCMContinuityCheckLoss", 9822),
          ("radioCCMPeerMEPStateDown", 9834),
          ("radioCCMforUNIShutdownDisabled", 8363),
          ("radioCCPairWrongCfg", 7225),
          ("radioCErrTrib", 7359),
          ("radioCFP", 7226),
          ("radioCKSyncDem1", 6846),
          ("radioCKSyncDem2", 6847),
          ("radioCLIsecurityalert", 9730),
          ("radioCNCTLossOfProtectionSignal", 8157),
          ("radioCNCTLossofClockSignal6MHz", 8156),
          ("radioCPSCardFail", 7821),
          ("radioCPUExpIf", 7227),
          ("radioCSUSyncFailed", 7829),
          ("radioCUEthernetSwicthFail", 7830),
          ("radioCUProtectionLost", 7842),
          ("radioCableCF", 7443),
          ("radioCableCOutoRg", 7444),
          ("radioCableInterfaceNotHybridIDU", 8383),
          ("radioCableInterfacePacketDischarging", 8384),
          ("radioCableInterfacePortMauStatusDown", 8385),
          ("radioCardAbsent", 8362),
          ("radioCardFail", 7715),
          ("radioCardInstalled", 8266),
          ("radioCardOp", 7777),
          ("radioCardRemoved", 8265),
          ("radioCarrierEquipmentOutofService", 9723),
          ("radioCarrierWaveinActiveCondition", 8155),
          ("radioChainNR", 7569),
          ("radioClStatSl6", 7445),
          ("radioClStatSl7", 7446),
          ("radioClock1LoSync", 8126),
          ("radioClock2LoSync", 8127),
          ("radioClockFail", 7770),
          ("radioClockLoSync", 7769),
          ("radioClockSourceFail", 7836),
          ("radioCodeErrTrib", 7447),
          ("radioColocatedMEPState", 8380),
          ("radioColocatedODUCommunicationFailure", 9738),
          ("radioCommFailure", 8264),
          ("radioConfMism", 7298),
          ("radioConfigCardStatus", 7837),
          ("radioConfigDbError", 7838),
          ("radioConfigFail", 7835),
          ("radioConfigdirectoryoversizelimit", 9729),
          ("radioConfigurationError", 8251),
          ("radioConfigurationNotSupported", 8390),
          ("radioCorruptData", 8262),
          ("radioCsu1ClockFail", 7831),
          ("radioCsu1GPSClockFail", 7833),
          ("radioCsu2ClockFail", 7832),
          ("radioCsu2GPSClockFail", 7834),
          ("radioD1Ch", 6988),
          ("radioD2Ch", 6989),
          ("radioD2mismatch", 7716),
          ("radioDCCFailure", 8394),
          ("radioDChanDroplos", 7449),
          ("radioDChanFail", 7229),
          ("radioDChanInslos", 7450),
          ("radioDEmbMismConf", 7452),
          ("radioDTMTrib1", 6839),
          ("radioDTMTrib2", 6840),
          ("radioDataTransMissA", 6838),
          ("radioDataTransMissB", 7228),
          ("radioDateLIdErr", 7448),
          ("radioDeMapper", 7451),
          ("radioDebugModeOff", 9789),
          ("radioDebugModeOn", 9788),
          ("radioDeviceHighTemperatureAlarm", 9803),
          ("radioDeviceLowTemperatureAlarm", 9804),
          ("radioDeviceoverheat", 9707),
          ("radioDeviceunderheat", 9708),
          ("radioDluFlow", 7717),
          ("radioDluFlowAl", 7607),
          ("radioDluFlowAl1", 7601),
          ("radioDluFlowAl10", 7610),
          ("radioDluFlowAl11", 7611),
          ("radioDluFlowAl12", 7612),
          ("radioDluFlowAl13", 7613),
          ("radioDluFlowAl14", 7614),
          ("radioDluFlowAl15", 7615),
          ("radioDluFlowAl16", 7616),
          ("radioDluFlowAl17", 7617),
          ("radioDluFlowAl18", 7618),
          ("radioDluFlowAl19", 7619),
          ("radioDluFlowAl2", 7602),
          ("radioDluFlowAl20", 7620),
          ("radioDluFlowAl21", 7621),
          ("radioDluFlowAl22", 7622),
          ("radioDluFlowAl23", 7623),
          ("radioDluFlowAl24", 7624),
          ("radioDluFlowAl25", 7625),
          ("radioDluFlowAl26", 7626),
          ("radioDluFlowAl27", 7627),
          ("radioDluFlowAl28", 7628),
          ("radioDluFlowAl29", 7629),
          ("radioDluFlowAl3", 7603),
          ("radioDluFlowAl30", 7630),
          ("radioDluFlowAl31", 7631),
          ("radioDluFlowAl32", 7632),
          ("radioDluFlowAl33", 7633),
          ("radioDluFlowAl34", 7634),
          ("radioDluFlowAl35", 7635),
          ("radioDluFlowAl36", 7636),
          ("radioDluFlowAl37", 7637),
          ("radioDluFlowAl38", 7638),
          ("radioDluFlowAl39", 7639),
          ("radioDluFlowAl4", 7604),
          ("radioDluFlowAl40", 7640),
          ("radioDluFlowAl41", 7641),
          ("radioDluFlowAl42", 7642),
          ("radioDluFlowAl43", 7643),
          ("radioDluFlowAl44", 7644),
          ("radioDluFlowAl45", 7645),
          ("radioDluFlowAl46", 7646),
          ("radioDluFlowAl47", 7647),
          ("radioDluFlowAl48", 7648),
          ("radioDluFlowAl49", 7649),
          ("radioDluFlowAl5", 7605),
          ("radioDluFlowAl50", 7650),
          ("radioDluFlowAl51", 7651),
          ("radioDluFlowAl52", 7652),
          ("radioDluFlowAl53", 7653),
          ("radioDluFlowAl54", 7654),
          ("radioDluFlowAl55", 7655),
          ("radioDluFlowAl56", 7656),
          ("radioDluFlowAl57", 7657),
          ("radioDluFlowAl58", 7658),
          ("radioDluFlowAl59", 7659),
          ("radioDluFlowAl6", 7606),
          ("radioDluFlowAl60", 7660),
          ("radioDluFlowAl61", 7661),
          ("radioDluFlowAl62", 7662),
          ("radioDluFlowAl63", 7663),
          ("radioDluFlowAl64", 7664),
          ("radioDluFlowAl65", 7665),
          ("radioDluFlowAl8", 7608),
          ("radioDluFlowAl9", 7609),
          ("radioDoubleKey", 7230),
          ("radioDownloadRequest", 8122),
          ("radioDryContactInput1", 9718),
          ("radioDryContactInput2", 9719),
          ("radioDryContactInput3", 9726),
          ("radioDryContactInput4", 9727),
          ("radioE-CCMCfgError", 9796),
          ("radioE-CCMLoss", 9756),
          ("radioE1Disconnected", 8276),
          ("radioE1LocOsc", 7453),
          ("radioE1T1P1Ais", 7454),
          ("radioE1T1P1Lcd", 7455),
          ("radioE1T1P1Lif", 7456),
          ("radioE1T1P1Lods", 7457),
          ("radioE1T1P1Lof", 7458),
          ("radioE1T1P1Los", 7459),
          ("radioE1T1P1Rfi", 7460),
          ("radioE1T1P2Ais", 7461),
          ("radioE1T1P2Lcd", 7462),
          ("radioE1T1P2Lif", 7463),
          ("radioE1T1P2Lods", 7464),
          ("radioE1T1P2Lof", 7465),
          ("radioE1T1P2Los", 7466),
          ("radioE1T1P2Rfi", 7467),
          ("radioE1T1P3Ais", 7468),
          ("radioE1T1P3Lcd", 7469),
          ("radioE1T1P3Lif", 7470),
          ("radioE1T1P3Lods", 7471),
          ("radioE1T1P3Lof", 7472),
          ("radioE1T1P3Los", 7473),
          ("radioE1T1P3Rfi", 7474),
          ("radioE1T1P4Ais", 7475),
          ("radioE1T1P4Lcd", 7476),
          ("radioE1T1P4Lif", 7477),
          ("radioE1T1P4Lods", 7478),
          ("radioE1T1P4Lof", 7479),
          ("radioE1T1P4Los", 7480),
          ("radioE1T1P4Rfi", 7481),
          ("radioE1T1P5Ais", 7482),
          ("radioE1T1P5Lcd", 7483),
          ("radioE1T1P5Lif", 7484),
          ("radioE1T1P5Lods", 7485),
          ("radioE1T1P5Lof", 7486),
          ("radioE1T1P5Los", 7487),
          ("radioE1T1P5Rfi", 7488),
          ("radioE1T1P6Ais", 7489),
          ("radioE1T1P6Lcd", 7490),
          ("radioE1T1P6Lif", 7491),
          ("radioE1T1P6Lods", 7492),
          ("radioE1T1P6Lof", 7493),
          ("radioE1T1P6Los", 7494),
          ("radioE1T1P6Rfi", 7495),
          ("radioE1T1P7Ais", 7496),
          ("radioE1T1P7Lcd", 7497),
          ("radioE1T1P7Lif", 7498),
          ("radioE1T1P7Lods", 7499),
          ("radioE1T1P7Lof", 7500),
          ("radioE1T1P7Los", 7501),
          ("radioE1T1P7Rfi", 7502),
          ("radioE1T1P8Ais", 7503),
          ("radioE1T1P8Lcd", 7504),
          ("radioE1T1P8Lif", 7505),
          ("radioE1T1P8Lof", 7507),
          ("radioE1T1P8Los", 7508),
          ("radioE1T1P8Rfi", 7509),
          ("radioE1T1P8ods", 7506),
          ("radioE1TestMode", 8292),
          ("radioE2promF", 7442),
          ("radioELPSAPSSwitchFailed", 8359),
          ("radioELPSMismatch", 8360),
          ("radioELPSProtectionPathFailure", 8357),
          ("radioELPSWorkingPathFailure", 8358),
          ("radioEOWRC1", 6853),
          ("radioEOWRC2", 6854),
          ("radioEPSOFFinActiveCondition", 8159),
          ("radioEcuUnitRemoved", 8158),
          ("radioEncryptionFailure", 8278),
          ("radioEncryptionOneway", 8279),
          ("radioEndofCableCompensation", 8119),
          ("radioEquipmentDoorOpen", 8241),
          ("radioEthIFault", 7360),
          ("radioEthLocOsc", 7510),
          ("radioEthSwitchGbEthPortLOS", 8223),
          ("radioEthSwitchGbEthPortLinkNotPresent", 8228),
          ("radioEthSwitchLAN1PortLinkNotPresent", 8225),
          ("radioEthSwitchLAN2PortLinkNotPresent", 8226),
          ("radioEthSwitchLAN3PortLinkNotPresent", 8227),
          ("radioEthSwitchTrunk1CapacityMismatch", 8230),
          ("radioEthSwitchTrunk2CapacityMismatch", 8231),
          ("radioEthernetDisconnected", 8327),
          ("radioExceedingProvisionedServiceFlows", 7841),
          ("radioExpSyncSource", 7231),
          ("radioExpectedSVRMismatch", 8232),
          ("radioExtEOW", 7232),
          ("radioExtSync1", 7364),
          ("radioExtSync2", 7365),
          ("radioExternalAlarm1", 8280),
          ("radioExternalAlarm2", 8281),
          ("radioExternalAlarm3", 8282),
          ("radioExternalAlarm4", 8283),
          ("radioExternalReferenceClockCutoff", 8160),
          ("radioFECSDH", 7755),
          ("radioFECSDHHSBY", 7756),
          ("radioFECSDL", 7757),
          ("radioFECSDLHSBY", 7758),
          ("radioFPGAIncompatibility", 8121),
          ("radioFPGAMism", 7513),
          ("radioFPGAProgrammingFailure", 8320),
          ("radioFailure", 9734),
          ("radioFan1failure", 9711),
          ("radioFan2failure", 9712),
          ("radioFan3failure", 9713),
          ("radioFan4failure", 9714),
          ("radioFanRequired", 8184),
          ("radioFantraypulledout", 9704),
          ("radioFarEndAlarm", 8255),
          ("radioFarEndSendingTS16LOMF", 9672),
          ("radioFarendLOF", 9733),
          ("radioFarendsendingAIS", 9671),
          ("radioFaultInOscillator", 8248),
          ("radioFaultinChangeOverFunction", 8240),
          ("radioFaultinEquipment", 8237),
          ("radioFaultinInstallationofEquipment", 8239),
          ("radioFaultinUnit", 8257),
          ("radioFif", 6984),
          ("radioForcedControlOn", 8238),
          ("radioForcedSwitch", 8161),
          ("radioFragmentationOperationalStatus", 8393),
          ("radioFrequencyMeasurement", 8162),
          ("radioG703Los", 6991),
          ("radioG8031ProtectionGroupFailed", 9855),
          ("radioGbEthAlarm1", 8334),
          ("radioGbEthAlarm2", 8335),
          ("radioGbEthAlarm3", 8336),
          ("radioGbEthAlarm4", 8337),
          ("radioHPB3Defect", 8308),
          ("radioHPDegrade", 9785),
          ("radioHPExcessiveError", 9786),
          ("radioHPPathLabelMismatch", 8307),
          ("radioHPRemoteDefect", 8306),
          ("radioHPRemoteError", 8305),
          ("radioHPSyncLoss", 6841),
          ("radioHPTraceIdentifierMismatch", 8304),
          ("radioHPUnequipped", 8303),
          ("radioHSBYConfigurationError", 9753),
          ("radioHWProtReq", 7516),
          ("radioHighBER", 8389),
          ("radioHitlessProtReq", 7514),
          ("radioHitlessSwitLoss", 7515),
          ("radioI2CDev", 7518),
          ("radioI2CIf", 7519),
          ("radioIDUCCMCfgError1plus1", 9746),
          ("radioIDUCCMContinuityCheckLoss1plus1", 9742),
          ("radioIDUCCMPeerMEPStateDown", 9744),
          ("radioIDUCCMRDIbitinthelastreceivedCCM", 9748),
          ("radioIDUCF", 7719),
          ("radioIDUContinuityCheckLoss", 8379),
          ("radioIDUContinuityCheckLoss1plus0", 9798),
          ("radioIDUHWMis", 7366),
          ("radioIDUMEPConfigurationError", 9701),
          ("radioIDUMEPContinuityCheckLoss", 9731),
          ("radioIDUMEPOperationalStatus", 9695),
          ("radioIDUMEPRemoteDefectIndication", 9697),
          ("radioIDUModeNotAuthorized", 8329),
          ("radioIDUsmisconfiguration", 8345),
          ("radioIFFailure", 7768),
          ("radioIFMgmt", 7517),
          ("radioIFSF", 7720),
          ("radioIMAGr1FE", 7527),
          ("radioIMAGr1NE", 7528),
          ("radioIMAGr2FE", 7529),
          ("radioIMAGr2NE", 7530),
          ("radioIU-OUCablemultiframeLoss", 9770),
          ("radioIU-OUEthernetpacketsdroppedbyFCSerror", 9774),
          ("radioIU-OULOFAlarm", 9769),
          ("radioIU-OURxE1NumberMismatch", 9772),
          ("radioIU-OUTxE1NumberMismatch", 9773),
          ("radioIUOUCableE1NumberOverflow", 8361),
          ("radioIduOduEber", 7521),
          ("radioIduOduFerf", 7522),
          ("radioIduOduFerfHWProt", 8128),
          ("radioIduOduIFLOS", 7775),
          ("radioIduOduIFLOSfHSBY", 7776),
          ("radioIduOduLof", 7523),
          ("radioIduOduOpCable", 7524),
          ("radioIduOduOvVol", 7520),
          ("radioIfRx", 8124),
          ("radioIfRxSynth", 7525),
          ("radioIfTxSynth", 7526),
          ("radioInAisProt", 7292),
          ("radioInAlCrit", 7702),
          ("radioInAlMaj", 7701),
          ("radioInAlMin", 7700),
          ("radioInAlTst", 7698),
          ("radioInAlWarn", 7699),
          ("radioIncomingSignalLevelIncorrect", 8260),
          ("radioInp1AlStat", 7531),
          ("radioInp2AlStat", 7532),
          ("radioInp3AlStat", 7533),
          ("radioInp4AlStat", 7534),
          ("radioInp5AlStat", 7535),
          ("radioInp6AlStat", 7536),
          ("radioJ0TraceIdentifierMismatch", 9777),
          ("radioJ1TraceIdentifierMismatch", 9780),
          ("radioJ2TraceIdentifierMismatch", 8374),
          ("radioLAGmemberstateunknown", 9807),
          ("radioLOF", 7742),
          ("radioLOFGP1X", 7376),
          ("radioLOFGP1Y", 7377),
          ("radioLOFGP2X", 7378),
          ("radioLOFGP2Y", 7379),
          ("radioLOFHSBY", 7743),
          ("radioLOFHWP", 6842),
          ("radioLOFfHSBY", 7596),
          ("radioLOPBXHWP", 7255),
          ("radioLOPHWP", 6990),
          ("radioLOPTXHWP", 7256),
          ("radioLOPWXHWP", 7257),
          ("radioLOS", 7744),
          ("radioLOS8Cl", 7375),
          ("radioLOSSF", 7382),
          ("radioLOSStby", 7258),
          ("radioLOSStby1", 7259),
          ("radioLOSUCh1", 7380),
          ("radioLOSUCh2", 7381),
          ("radioLPBIP2Defect", 8318),
          ("radioLPDegrade", 9783),
          ("radioLPG701OperationalstatusDown", 9680),
          ("radioLPG702OperationalstatusDown", 9681),
          ("radioLPG703OperationalstatusDown", 9682),
          ("radioLPG704OperationalstatusDown", 9683),
          ("radioLPG705OperationalstatusDown", 9684),
          ("radioLPG706OperationalstatusDown", 9685),
          ("radioLPG707OperationalstatusDown", 9686),
          ("radioLPG708OperationalstatusDown", 9687),
          ("radioLPG709OperationalstatusDown", 9688),
          ("radioLPG710OperationalstatusDown", 9689),
          ("radioLPG711OperationalstatusDown", 9690),
          ("radioLPG712OperationalstatusDown", 9691),
          ("radioLPG713OperationalstatusDown", 9692),
          ("radioLPG714OperationalstatusDown", 9693),
          ("radioLPG715OperationalstatusDown", 9694),
          ("radioLPGConfigurationError", 9732),
          ("radioLPGFailure", 9700),
          ("radioLPJ2TraceIdentifierMismatch", 9784),
          ("radioLPPathLabelMismatch", 8316),
          ("radioLPRemoteDefect", 8315),
          ("radioLPRemoteError", 8314),
          ("radioLPRemoteFailure", 9810),
          ("radioLPRemoteFault", 8317),
          ("radioLPTUAlarmIndicationSignal", 9782),
          ("radioLPTULossOfPointer", 9781),
          ("radioLPTraceIdentifierMismatch", 8313),
          ("radioLPUnequipped", 8312),
          ("radioLSIf", 7260),
          ("radioLaserDeg", 7233),
          ("radioLastTemporizedOperationFail", 8229),
          ("radioLicenceExpired", 8252),
          ("radioLicenceWillExpireinNearFuture", 8253),
          ("radioLicenceforFeatureIsNotAvailable", 8254),
          ("radioLine1", 7234),
          ("radioLine10", 7235),
          ("radioLine10HWp", 7722),
          ("radioLine11", 7236),
          ("radioLine11HWp", 7723),
          ("radioLine12", 7237),
          ("radioLine12HWp", 7724),
          ("radioLine13", 7238),
          ("radioLine13HWp", 7725),
          ("radioLine14", 7239),
          ("radioLine14HWp", 7726),
          ("radioLine15", 7240),
          ("radioLine15HWp", 7727),
          ("radioLine16", 7241),
          ("radioLine16HWp", 7728),
          ("radioLine17", 7242),
          ("radioLine17HWp", 7729),
          ("radioLine18", 7243),
          ("radioLine18HWp", 7730),
          ("radioLine19", 7244),
          ("radioLine19HWp", 7731),
          ("radioLine1DCCM", 7367),
          ("radioLine1DCCR", 7368),
          ("radioLine1EDCCR", 7369),
          ("radioLine1HWp", 7721),
          ("radioLine1WDCCR", 7370),
          ("radioLine2", 7245),
          ("radioLine20", 7246),
          ("radioLine20HWp", 7733),
          ("radioLine21", 7247),
          ("radioLine21HWp", 7734),
          ("radioLine2DCCM", 7371),
          ("radioLine2DCCR", 7372),
          ("radioLine2EDCCR", 7373),
          ("radioLine2HWp", 7732),
          ("radioLine2WDCCR", 7374),
          ("radioLine3", 7248),
          ("radioLine3HWp", 7735),
          ("radioLine4", 7249),
          ("radioLine4HWp", 7736),
          ("radioLine5", 7250),
          ("radioLine5HWp", 7737),
          ("radioLine6", 7251),
          ("radioLine6HWp", 7738),
          ("radioLine7", 7252),
          ("radioLine7HWp", 7739),
          ("radioLine8", 7253),
          ("radioLine8HWp", 7740),
          ("radioLine9", 7254),
          ("radioLine9HWp", 7741),
          ("radioLinkError", 7598),
          ("radioLinkFault", 7537),
          ("radioLinkReconfigurationFailure", 8319),
          ("radioLnkDwnP1", 7538),
          ("radioLnkDwnP2", 7539),
          ("radioLnkDwnP3", 7540),
          ("radioLnkDwnP4", 7541),
          ("radioLoRF", 7594),
          ("radioLocAlmLgOR", 7542),
          ("radioLocalAISInsertionOnHalfPayload", 8196),
          ("radioLocalSync", 8185),
          ("radioLoopProtectionE1AIS", 8375),
          ("radioLoopback", 8163),
          ("radioLossCap", 7543),
          ("radioLossOfCarrier", 7843),
          ("radioLossOfClock", 8294),
          ("radioLossPartCap", 7544),
          ("radioLossofCableFrame", 9735),
          ("radioLossofPointerTX", 8396),
          ("radioLossofSequence", 9815),
          ("radioLossofairflowfailure", 9703),
          ("radioLossofinputsignal", 9679),
          ("radioLowBatteryVoltage", 8271),
          ("radioMCFEthStatus", 7778),
          ("radioMCFQxIFFail", 7779),
          ("radioMMOLos", 7262),
          ("radioMSB2Defect", 8300),
          ("radioMSDegrade", 9779),
          ("radioMSExcessiveError", 9787),
          ("radioMSRemoteDefect", 8299),
          ("radioMSRemoteError", 8298),
          ("radioMaintenanceLoopback", 9817),
          ("radioManualOperationOff", 9791),
          ("radioManualOperationOn", 9790),
          ("radioManualSwitch", 8164),
          ("radioManualSwitchState", 8165),
          ("radioMasterA-CCMConfigurationError", 9757),
          ("radioMasterA-CCMLoss", 9754),
          ("radioMasterRDIreceivedinthelastA-CCM", 9759),
          ("radioMatDownloadFailure", 7825),
          ("radioMatSWMismatch", 7827),
          ("radioMatSwNotAligned", 7826),
          ("radioMemCk", 7261),
          ("radioMemKeyFail", 7546),
          ("radioMemoryKeyExtracted", 8365),
          ("radioMemoryKeyNotPresent", 9819),
          ("radioMemoryKeyforWrongNEType", 9820),
          ("radioMemoryKeywithmismatchingcontent", 9821),
          ("radioMismFailAct", 7299),
          ("radioMismIduOdu", 7547),
          ("radioMod1PSfail", 6848),
          ("radioMod2PSfail", 6849),
          ("radioModFail", 7263),
          ("radioModFailHSBY", 7549),
          ("radioModIfCabF", 7548),
          ("radioModSyncLoss", 6850),
          ("radioModeAlign", 8190),
          ("radioModuleInsertedbutnotenabled", 9717),
          ("radioModuleInsertedincorrectly", 9705),
          ("radioNEOverheating", 8366),
          ("radioNOIF140", 8120),
          ("radioNTPUpdate", 8275),
          ("radioNearEndSendingTS16LOMF", 9676),
          ("radioNearEnddetectsatestcode", 9673),
          ("radioNearEndinUnavailableSignalState", 9674),
          ("radioNearendLOF", 9667),
          ("radioNearendLossOfSignal", 9668),
          ("radioNearendsendingAIS", 9675),
          ("radioNearendsendingLOFIndication", 9669),
          ("radioNetworkReferenceClockQualityDown", 8166),
          ("radioNoActiveCSU", 7828),
          ("radioNoFreeChannel", 8259),
          ("radioNoIncomingRadioSignal", 8261),
          ("radioNoOutgoingRadioSignal", 8263),
          ("radioNotHybridIDU", 9737),
          ("radioOAMMAConfigurationError", 9823),
          ("radioOAMRDI", 9793),
          ("radioODUModeNotAuthorized", 8328),
          ("radioODUODUPortMauStatusDown", 8386),
          ("radioODUODUPortOperationalstatusdown", 8387),
          ("radioODUStatusabsent", 9768),
          ("radioODUStatusfailed", 9767),
          ("radioODUUnsupportedDynamicModulation", 8189),
          ("radioOHRXFail1", 7383),
          ("radioOHRXFail2", 7384),
          ("radioOHTXFail1", 7385),
          ("radioOHTXFail2", 7386),
          ("radioOUIU-OUMacAddressMismatch", 9771),
          ("radioOduCabRg", 7550),
          ("radioOduIf", 8125),
          ("radioOduPowFail", 7551),
          ("radioOneSynchSourceDown", 8381),
          ("radioOpStat", 7552),
          ("radioOpStatP1", 7553),
          ("radioOpStatP2", 7554),
          ("radioOpStatP3", 7555),
          ("radioOpStatP4", 7556),
          ("radioOpStatP5", 7557),
          ("radioOpStatP6", 7558),
          ("radioOpStatP7", 7559),
          ("radioOpStatP8", 7560),
          ("radioOperatingError", 8249),
          ("radioOperationalStatusF", 8202),
          ("radioOperationalStatusOSI1", 8204),
          ("radioOperationalStatusOSI10", 8213),
          ("radioOperationalStatusOSI11", 8214),
          ("radioOperationalStatusOSI12", 8215),
          ("radioOperationalStatusOSI13", 8216),
          ("radioOperationalStatusOSI14", 8217),
          ("radioOperationalStatusOSI15", 8218),
          ("radioOperationalStatusOSI16", 8219),
          ("radioOperationalStatusOSI2", 8205),
          ("radioOperationalStatusOSI3", 8206),
          ("radioOperationalStatusOSI4", 8207),
          ("radioOperationalStatusOSI5", 8208),
          ("radioOperationalStatusOSI6", 8209),
          ("radioOperationalStatusOSI7", 8210),
          ("radioOperationalStatusOSI8", 8211),
          ("radioOperationalStatusOSI9", 8212),
          ("radioOperationalStatusQ0", 8200),
          ("radioOperationalStatusQ1", 8201),
          ("radioOperationalStatusVbus", 8203),
          ("radioOperationalstatusDown", 9677),
          ("radioOperationalstatuswaschangedfromuptos", 9766),
          ("radioOpticalAlarm1", 8330),
          ("radioOpticalAlarm2", 8331),
          ("radioOpticalAlarm3", 8332),
          ("radioOpticalAlarm4", 8333),
          ("radioOpticalSFPLossOfSignal", 8367),
          ("radioOpticalSFPTXFault", 8368),
          ("radioOutBufFail", 7764),
          ("radioOverTemp", 7293),
          ("radioOvercurrent-undercurrentFPR", 9832),
          ("radioOvercurrentUndercurrentODUPSCondition", 8340),
          ("radioPChMGP1", 7387),
          ("radioPChMGP2", 7388),
          ("radioPDHProtectionSwitch", 8322),
          ("radioPPMissing", 7763),
          ("radioPRPSLocked", 7264),
          ("radioPS-1HighTemperatureAlarm", 9801),
          ("radioPS-2HighTemperatureAlarm", 9802),
          ("radioPSAdmStat", 7566),
          ("radioPSCMism", 7567),
          ("radioPSHstbyFail", 6852),
          ("radioPSProtectionLost", 7265),
          ("radioPWFail", 9818),
          ("radioPWFunctionAlarm", 9826),
          ("radioPWOperationalStatusDown", 8355),
          ("radioPWRemotePacketLoss", 8356),
          ("radioPWoperationalstatuswaschangedfromstoup", 9762),
          ("radioPacketsfromIDUDischargedbyODU", 9739),
          ("radioParDetFP1", 7561),
          ("radioParDetFP2", 7562),
          ("radioParDetFP3", 7563),
          ("radioParDetFP4", 7564),
          ("radioPortFailure", 8369),
          ("radioPortSpeedUnderCIRSum", 8351),
          ("radioPortSpeedUnderLimiter", 8350),
          ("radioPowAl", 7565),
          ("radioPower1InVoltageoutofrange", 9715),
          ("radioPower1OutProbleminPSoutput", 9716),
          ("radioPower2InVoltageoutofrange", 9724),
          ("radioPower2OutProbleminPSoutput", 9725),
          ("radioPowerSupplyFailuretoODU", 9765),
          ("radioPowerSupplyOverheat", 9706),
          ("radioPowerSupplytoODUFailure", 8343),
          ("radioPowerUp", 8273),
          ("radioPrimaryclocksourcefailed", 9678),
          ("radioPrioritySessionGranted", 8118),
          ("radioProbleminallpowersupplies", 9709),
          ("radioProtectionCCMCfgError", 9747),
          ("radioProtectionCCMContinuityCheckLoss", 9743),
          ("radioProtectionCCMPeerMEPStateDown", 9745),
          ("radioProtectionCCMRDIbitinthelastreceivedCCM", 9749),
          ("radioProtectionHSBYConfigurationError", 8377),
          ("radioProtectionMEPConfigurationError", 9702),
          ("radioProtectionMEPContinuityCheckLoss", 9699),
          ("radioProtectionMEPOperationalStatus", 9696),
          ("radioProtectionMEPRemoteDefectIndication", 9698),
          ("radioProtectionManualOperation", 8346),
          ("radioProtectionModeMismatchinColocatedODU", 8378),
          ("radioProtectionSelfTestFailure", 8348),
          ("radioProtectionSoftwareSwitchNotAllowed", 8349),
          ("radioProtectionSwitchFailure", 8290),
          ("radioProtectionSystemFailure", 8347),
          ("radioR1Ch", 6986),
          ("radioR1IfAl", 7568),
          ("radioR2Ch", 6987),
          ("radioR2IF", 7746),
          ("radioRCh", 6985),
          ("radioRDIreceivedinthelastE-CCM", 9761),
          ("radioRFRxSynth", 7572),
          ("radioRFSearch", 7266),
          ("radioRFTxSynth", 7573),
          ("radioRS", 7595),
          ("radioRS1", 7748),
          ("radioRS2", 7749),
          ("radioRS3", 7750),
          ("radioRS4", 7751),
          ("radioRSB1Defect", 8295),
          ("radioRSCLOF", 7267),
          ("radioRSDegrade", 9778),
          ("radioRSLLow", 8268),
          ("radioRSLossOfFrame", 8296),
          ("radioRSOutOfFrame", 8297),
          ("radioRSPIUnavailableStateRP", 8168),
          ("radioRTB1M", 7389),
          ("radioRTB2M", 7390),
          ("radioRTIB1", 7391),
          ("radioRTIB2", 7392),
          ("radioRTNSAPMB1", 7393),
          ("radioRTNSAPMB2", 7394),
          ("radioRUCLOS", 7268),
          ("radioRXAl", 7574),
          ("radioRXCardF", 7395),
          ("radioRXHSBY", 7753),
          ("radioRXLocalInternalClock", 8169),
          ("radioRXPLL6E", 7354),
          ("radioRXSection", 6855),
          ("radioRealTimeLostFault", 8250),
          ("radioReboot", 8274),
          ("radioReceiveProtectionSwitchFailure", 8321),
          ("radioRedundOpStat", 7571),
          ("radioRefSwCh", 7747),
          ("radioRemoteCardIdentifier", 8167),
          ("radioRemoteFaultIndication", 9831),
          ("radioRemoteFaultWest", 8277),
          ("radioRemoteIDUAlarm", 8284),
          ("radioRemoteIDUCCMMEPState", 9794),
          ("radioRemoteIDUExternalAlarm1", 8285),
          ("radioRemoteIDUExternalAlarm2", 8286),
          ("radioRemoteIDUExternalAlarm3", 8287),
          ("radioRemoteIDUExternalAlarm4", 8288),
          ("radioRemotePacketLoss", 9833),
          ("radioRemoteProtectionCCMMEPState", 9795),
          ("radioRemotefaultEast", 8272),
          ("radioRouteIdMismatch", 6541),
          ("radioRouteIdMismatchProtSide", 6627),
          ("radioRxDistExtr", 7269),
          ("radioRxDistPS", 7270),
          ("radioRxTxCF", 7772),
          ("radioRxopticalpowerabovemaxthreshold", 9720),
          ("radioRxopticalpowerbelowminthreshold", 9721),
          ("radioSCModIF", 7575),
          ("radioSCS1F", 7396),
          ("radioSCS2F", 7397),
          ("radioSDDADEinActiveCondition", 8170),
          ("radioSFPBIASCurrentAbnormal", 9857),
          ("radioSFPMissing", 8221),
          ("radioSFPModuleInstalled", 8323),
          ("radioSFPModuleRemoved", 8324),
          ("radioSFPModuleTxFault", 8325),
          ("radioSFPPayloadDisconnected", 8326),
          ("radioSFPRxPowerAbnormal", 9859),
          ("radioSFPTemperatureAbnormal", 9856),
          ("radioSFPTxFault", 8224),
          ("radioSFPTxPowerAbnormal", 9858),
          ("radioSFPmismatch", 9854),
          ("radioSHSBYF", 7402),
          ("radioSIFB1", 7399),
          ("radioSIFB2", 7400),
          ("radioSLOSDem1", 7407),
          ("radioSLOSDem2", 7408),
          ("radioSLOSMod1", 7409),
          ("radioSLOSMod2", 7410),
          ("radioSLOSRXDem1", 7411),
          ("radioSLOSRXDem2", 7412),
          ("radioSLOSTXMod1", 7413),
          ("radioSNMPAuthenticationFailure", 8220),
          ("radioSNRLow", 8270),
          ("radioSPIDev", 7584),
          ("radioSPIIf", 7585),
          ("radioSSMMissing", 8382),
          ("radioSTFStby", 7403),
          ("radioSTFStby1", 7404),
          ("radioSTFStby2", 7405),
          ("radioSTFStby3", 7406),
          ("radioSWM", 7754),
          ("radioSbusLink", 7271),
          ("radioScheduledActionFailure", 9750),
          ("radioSelfTestF", 7398),
          ("radioSeqAl", 7599),
          ("radioSerialNumberMemoryKeywithmismatchingcontent", 8341),
          ("radioServiceCCMLoss", 8353),
          ("radioServiceDownorServicePartial", 9829),
          ("radioServiceFlowsAlignmentAlrm", 7840),
          ("radioServiceFlowsNotAlignedWithProfiles", 7839),
          ("radioServiceStatusDown", 8352),
          ("radioSfwrHwMism", 7576),
          ("radioSignalDegrade", 8372),
          ("radioSignalLevelUnderThreshold", 9736),
          ("radioSlEquipMod", 7577),
          ("radioSlEquipOdu", 7578),
          ("radioSlEquipSec", 7579),
          ("radioSlaveA-CCMConfigurationError", 9758),
          ("radioSlaveA-CCMLoss", 9755),
          ("radioSlaveRDIreceivedinthelastA-CCM", 9760),
          ("radioSoftwM", 7401),
          ("radioSoftwareSwitchNotAllowed", 9728),
          ("radioSourceClockDeteriorate", 8371),
          ("radioSpeedValuelowerthantheLimiteronthatinterface", 9827),
          ("radioSpeedValuelowerthanthesumofallCIR", 9828),
          ("radioSrcAStatSl6", 7580),
          ("radioSrcAStatSl7", 7581),
          ("radioSrcBStatSl6", 7582),
          ("radioSrcBStatSl7", 7583),
          ("radioStandbySwitch", 8123),
          ("radioStandbySwitchMismatch", 7272),
          ("radioStationAlarmOff", 9764),
          ("radioStationAlarmOn", 9763),
          ("radioStbyEEprom", 7295),
          ("radioSumLicense", 7586),
          ("radioSwitchFail", 7587),
          ("radioSyncFromMod12", 6845),
          ("radioSyncFromModT1", 6843),
          ("radioSyncFromModT2", 6844),
          ("radioSynchAllSourcesDown", 9838),
          ("radioSynchConfigurationError", 9836),
          ("radioSynchMissingSSM", 9835),
          ("radioSynchOneSourceDown", 9837),
          ("radioSynchQualityLevelDegraded", 9824),
          ("radioSynchStatusChanged", 8171),
          ("radioSynchUnlockedPLL", 9825),
          ("radioSynchronization", 9792),
          ("radioSynthFail", 7773),
          ("radioSynthesizerUnlock", 8269),
          ("radioSystemEthernetPort", 9752),
          ("radioSystemFailure", 9841),
          ("radioSystemTypeMemoryKeywithmismatchingcontent", 8342),
          ("radioSystemTypeMismatchinPairedODUGroup", 8392),
          ("radioSystemTypeMismatchonColocatedODU", 9741),
          ("radioTIMHWP", 7273),
          ("radioTSProcT", 7511),
          ("radioTSProcTODU", 7512),
          ("radioTUAIS", 8310),
          ("radioTUG31", 7765),
          ("radioTUG32", 7766),
          ("radioTUG33", 7767),
          ("radioTULossOfMultiframe", 8309),
          ("radioTULossOfPointer", 8311),
          ("radioTX1PSF", 7415),
          ("radioTX2PSF", 7416),
          ("radioTXAl", 7591),
          ("radioTXAmp", 7417),
          ("radioTXBiasAl", 7592),
          ("radioTXPLL19E", 7353),
          ("radioTXPLL6E", 7355),
          ("radioTXPowerAlarm", 8376),
          ("radioTXPowerSupplyFail", 9710),
          ("radioTelemChan", 7588),
          ("radioTestGeneratorOn", 8247),
          ("radioTestMode", 8293),
          ("radioTestModeActive", 8246),
          ("radioTimeServerMissing", 8117),
          ("radioTransPwBias", 7589),
          ("radioTransPwDet", 7590),
          ("radioTransceiverTempHighAlarm", 9805),
          ("radioTransceiverTempLowAlarm", 9806),
          ("radioTrib10AISIN", 6897),
          ("radioTrib10AISINHWP", 6961),
          ("radioTrib10Code", 6913),
          ("radioTrib10CodeHWP", 6977),
          ("radioTrib10ConfAlm", 6865),
          ("radioTrib10ConfAlmHWP", 6929),
          ("radioTrib10LOS", 6881),
          ("radioTrib10LOSHWP", 6945),
          ("radioTrib11AISIN", 6898),
          ("radioTrib11AISINHWP", 6962),
          ("radioTrib11Code", 6914),
          ("radioTrib11CodeHWP", 6978),
          ("radioTrib11ConfAlm", 6866),
          ("radioTrib11ConfAlmHWP", 6930),
          ("radioTrib11LOS", 6882),
          ("radioTrib11LOSHWP", 6946),
          ("radioTrib12AISIN", 6899),
          ("radioTrib12AISINHWP", 6963),
          ("radioTrib12Code", 6915),
          ("radioTrib12CodeHWP", 6979),
          ("radioTrib12ConfAlm", 6867),
          ("radioTrib12ConfAlmHWP", 6931),
          ("radioTrib12LOS", 6883),
          ("radioTrib12LOSHWP", 6947),
          ("radioTrib13AISIN", 6900),
          ("radioTrib13AISINHWP", 6964),
          ("radioTrib13Code", 6916),
          ("radioTrib13CodeHWP", 6980),
          ("radioTrib13ConfAlm", 6868),
          ("radioTrib13ConfAlmHWP", 6932),
          ("radioTrib13LOS", 6884),
          ("radioTrib13LOSHWP", 6948),
          ("radioTrib14AISIN", 6901),
          ("radioTrib14AISINHWP", 6965),
          ("radioTrib14Code", 6917),
          ("radioTrib14CodeHWP", 6981),
          ("radioTrib14ConfAlm", 6869),
          ("radioTrib14ConfAlmHWP", 6933),
          ("radioTrib14LOS", 6885),
          ("radioTrib14LOSHWP", 6949),
          ("radioTrib15AISIN", 6902),
          ("radioTrib15AISINHWP", 6966),
          ("radioTrib15Code", 6918),
          ("radioTrib15CodeHWP", 6982),
          ("radioTrib15ConfAlm", 6870),
          ("radioTrib15ConfAlmHWP", 6934),
          ("radioTrib15LOS", 6886),
          ("radioTrib15LOSHWP", 6950),
          ("radioTrib16AISIN", 6903),
          ("radioTrib16AISINHWP", 6967),
          ("radioTrib16Code", 6919),
          ("radioTrib16CodeHWP", 6983),
          ("radioTrib16ConfAlm", 6871),
          ("radioTrib16ConfAlmHWP", 6935),
          ("radioTrib16LOS", 6887),
          ("radioTrib16LOSHWP", 6951),
          ("radioTrib1AISIN", 6888),
          ("radioTrib1AISINHWP", 6952),
          ("radioTrib1Code", 6904),
          ("radioTrib1CodeHWP", 6968),
          ("radioTrib1ConfAlm", 6856),
          ("radioTrib1ConfAlmHWP", 6920),
          ("radioTrib1DCCM", 7414),
          ("radioTrib1LOS", 6872),
          ("radioTrib1LOSHWP", 6936),
          ("radioTrib2AISIN", 6889),
          ("radioTrib2AISINHWP", 6953),
          ("radioTrib2Code", 6905),
          ("radioTrib2CodeHWP", 6969),
          ("radioTrib2ConfAlm", 6857),
          ("radioTrib2ConfAlmHWP", 6921),
          ("radioTrib2LOS", 6873),
          ("radioTrib2LOSHWP", 6937),
          ("radioTrib3AISIN", 6890),
          ("radioTrib3AISINHWP", 6954),
          ("radioTrib3Code", 6906),
          ("radioTrib3CodeHWP", 6970),
          ("radioTrib3ConfAlm", 6858),
          ("radioTrib3ConfAlmHWP", 6922),
          ("radioTrib3LOS", 6874),
          ("radioTrib3LOSHWP", 6938),
          ("radioTrib4AISIN", 6891),
          ("radioTrib4AISINHWP", 6955),
          ("radioTrib4Code", 6907),
          ("radioTrib4CodeHWP", 6971),
          ("radioTrib4ConfAlm", 6859),
          ("radioTrib4ConfAlmHWP", 6923),
          ("radioTrib4LOS", 6875),
          ("radioTrib4LOSHWP", 6939),
          ("radioTrib5AISIN", 6892),
          ("radioTrib5AISINHWP", 6956),
          ("radioTrib5Code", 6908),
          ("radioTrib5CodeHWP", 6972),
          ("radioTrib5ConfAlm", 6860),
          ("radioTrib5ConfAlmHWP", 6924),
          ("radioTrib5LOS", 6876),
          ("radioTrib5LOSHWP", 6940),
          ("radioTrib6AISIN", 6893),
          ("radioTrib6AISINHWP", 6957),
          ("radioTrib6Code", 6909),
          ("radioTrib6CodeHWP", 6973),
          ("radioTrib6ConfAlm", 6861),
          ("radioTrib6ConfAlmHWP", 6925),
          ("radioTrib6LOS", 6877),
          ("radioTrib6LOSHWP", 6941),
          ("radioTrib7AISIN", 6894),
          ("radioTrib7AISINHWP", 6958),
          ("radioTrib7Code", 6910),
          ("radioTrib7CodeHWP", 6974),
          ("radioTrib7ConfAlm", 6862),
          ("radioTrib7ConfAlmHWP", 6926),
          ("radioTrib7LOS", 6878),
          ("radioTrib7LOSHWP", 6942),
          ("radioTrib8AISIN", 6895),
          ("radioTrib8AISINHWP", 6959),
          ("radioTrib8Code", 6911),
          ("radioTrib8CodeHWP", 6975),
          ("radioTrib8ConfAlm", 6863),
          ("radioTrib8ConfAlmHWP", 6927),
          ("radioTrib8LOS", 6879),
          ("radioTrib8LOSHWP", 6943),
          ("radioTrib9AISIN", 6896),
          ("radioTrib9AISINHWP", 6960),
          ("radioTrib9Code", 6912),
          ("radioTrib9CodeHWP", 6976),
          ("radioTrib9ConfAlm", 6864),
          ("radioTrib9ConfAlmHWP", 6928),
          ("radioTrib9LOS", 6880),
          ("radioTrib9LOSHWP", 6944),
          ("radioTribE1ProtSide", 7570),
          ("radioTunFail1", 7274),
          ("radioTunFail10", 7275),
          ("radioTunFail11", 7276),
          ("radioTunFail12", 7277),
          ("radioTunFail13", 7278),
          ("radioTunFail14", 7279),
          ("radioTunFail15", 7280),
          ("radioTunFail16", 7281),
          ("radioTunFail2", 7282),
          ("radioTunFail3", 7283),
          ("radioTunFail4", 7284),
          ("radioTunFail5", 7285),
          ("radioTunFail6", 7286),
          ("radioTunFail7", 7287),
          ("radioTunFail8", 7288),
          ("radioTunFail9", 7289),
          ("radioTxDistExtr", 7290),
          ("radioTxDistPS", 7291),
          ("radioTxONforProtectingODUAlarm", 8197),
          ("radioTxRxE1NumberMismatch", 8364),
          ("radioUASFarEndBlockError", 8172),
          ("radioUHF", 7759),
          ("radioUNIShutdown", 8354),
          ("radioUNIShutdownCCMDisabled", 8344),
          ("radioUPAl", 7418),
          ("radioUSWForcedSwitch", 8177),
          ("radioUSWLockout", 8178),
          ("radioUSWManualSwitch", 8179),
          ("radioUSWTraffictoProtection", 8180),
          ("radioUloFlow", 7760),
          ("radioUloFlowAl1", 7666),
          ("radioUloFlowAl10", 7675),
          ("radioUloFlowAl11", 7676),
          ("radioUloFlowAl12", 7677),
          ("radioUloFlowAl13", 7678),
          ("radioUloFlowAl14", 7679),
          ("radioUloFlowAl15", 7680),
          ("radioUloFlowAl16", 7681),
          ("radioUloFlowAl17", 7682),
          ("radioUloFlowAl18", 7683),
          ("radioUloFlowAl19", 7684),
          ("radioUloFlowAl2", 7667),
          ("radioUloFlowAl20", 7685),
          ("radioUloFlowAl21", 7686),
          ("radioUloFlowAl22", 7687),
          ("radioUloFlowAl23", 7688),
          ("radioUloFlowAl24", 7689),
          ("radioUloFlowAl25", 7690),
          ("radioUloFlowAl26", 7691),
          ("radioUloFlowAl27", 7692),
          ("radioUloFlowAl28", 7693),
          ("radioUloFlowAl29", 7694),
          ("radioUloFlowAl3", 7668),
          ("radioUloFlowAl30", 7695),
          ("radioUloFlowAl31", 7696),
          ("radioUloFlowAl32", 7697),
          ("radioUloFlowAl4", 7669),
          ("radioUloFlowAl5", 7670),
          ("radioUloFlowAl6", 7671),
          ("radioUloFlowAl7", 7672),
          ("radioUloFlowAl8", 7673),
          ("radioUloFlowAl9", 7674),
          ("radioUnavailability", 8245),
          ("radioUnavailableStateB1", 8173),
          ("radioUnavailableStateB2", 8174),
          ("radioUnipolarSwitchRequest", 8175),
          ("radioUnkSystT", 7593),
          ("radioUnlock", 8267),
          ("radioUnsupportedSFPType", 8222),
          ("radioUserChannelLossofSignal", 8176),
          ("radioVCOFreqDev", 7419),
          ("radioVCXOFail", 7771),
          ("radioWCCCPair", 7420),
          ("radioWSLOSTx", 7761),
          ("radioWaySideRFCOHLOS", 8181),
          ("radioWaySideSOHLOS", 8182),
          ("radioWorkingEquipSwitchedToProtection", 8183),
          ("radioWrongRole-PriorityConfiguration", 9740),
          ("radioWrongRoleorPriorityConfiginPairedODUGroup", 8391),
          ("radioXPICOff", 7294),
          ("radiobackupKeyMism", 7224),
          ("radiohybrid-packetmismatch", 9751),
          ("radioradioLinkStatusDown", 9775),
          ("radioradioRfRXsignal", 9797),
          ("radiusServerUnavailable", 2117),
          ("ramanGainCritical", 9531),
          ("ramanGainDegraded", 3482),
          ("ramanGainFail", 3483),
          ("ramanGainProblem", 9530),
          ("ramanPumpPwrTooHigh", 3525),
          ("ramanPumpPwrTooLow", 3526),
          ("rdi", 240),
          ("rdiProtSide", 6625),
          ("rdncylockout", 3987),
          ("rdncymaintenance", 3988),
          ("rdncyoutofsync", 3986),
          ("rdncyswvermismatch", 3985),
          ("ready", 6245),
          ("receivePowerOutOfRange", 6736),
          ("receivedPqlBelowProvisionPqlStatus", 828),
          ("receiverFailBooster", 241),
          ("receiverFailPreamp", 432),
          ("receiverFailure", 6246),
          ("receiverfailure", 1792),
          ("recoverMode", 4544),
          ("rectifierFail", 9262),
          ("rectifierFailure", 242),
          ("rectifierHighVoltage", 9263),
          ("rectifierHighVoltageFailure", 243),
          ("rectifierLowVoltage", 9264),
          ("rectifierLowVoltageFailure", 244),
          ("rectifierPowerFailADSL", 9265),
          ("rectifierPowerFailDCL", 9267),
          ("rectifierPowerFailTrans", 9266),
          ("recurringLicenseExpired", 4538),
          ("reduceLogOverload", 9551),
          ("reduceNotificationOverload", 2126),
          ("redundantControllerFailed", 1878),
          ("redundantModuleStatus", 852),
          ("redundantPairCommFail", 6737),
          ("redundantPower", 903),
          ("redundantPwr", 245),
          ("refusedSwitchingChannel1", 6247),
          ("refusedSwitchingChannel2", 6248),
          ("refusedSwitchingChannel3", 6249),
          ("refusedSwitchingChannel4", 6250),
          ("refusedSwitchingChannel5", 6251),
          ("refusedSwitchingChannel6", 6252),
          ("refusedSwitchingChannel7", 6253),
          ("regeneratorPairUnavailable", 1906),
          ("rei", 1843),
          ("remote", 462),
          ("remoteAlarmIndication", 6542),
          ("remoteChassisConfiguring", 2008),
          ("remoteConf", 2012),
          ("remoteDefectIndication", 3491),
          ("remoteEquipmentMismatch", 2009),
          ("remoteEthernetLinkFault", 1858),
          ("remoteFailureIndication", 1817),
          ("remoteFanFailure", 2022),
          ("remoteFault", 9944),
          ("remoteLinkFailure", 9390),
          ("remoteLoopBackActivation", 6254),
          ("remoteMsi", 1853),
          ("remoteOutgoingDefectIndication", 527),
          ("remotePowerFail", 770),
          ("remotePowerFailAll", 768),
          ("remotePumpFailure", 387),
          ("remoteTemperatureTooHigh", 2018),
          ("remoteTerminalAlarm", 767),
          ("remoteVoltageTooHigh", 2016),
          ("remoteVoltageTooLow", 2014),
          ("remotechassismismatch", 2003),
          ("remotechassismissing", 2004),
          ("requestComLost", 1017),
          ("requestInProgress", 1000),
          ("requestQueueOverflow", 7813),
          ("resourceAccessDenied", 1841),
          ("retrieveStdbyEng", 9270),
          ("reversionFailed", 6644),
          ("rfDiversity", 6255),
          ("rfLos", 6256),
          ("rfMain", 6257),
          ("rfSwitchAlarm", 6258),
          ("ringFailure", 248),
          ("ringProblem", 249),
          ("rmtAIS", 8752),
          ("rmtAPSMismatch", 8761),
          ("rmtARP-REACH-MAX", 8777),
          ("rmtAUAIS", 8710),
          ("rmtAULOP", 8711),
          ("rmtAppdiskErr", 8788),
          ("rmtBUSERROR", 8768),
          ("rmtCES-AIS", 8767),
          ("rmtCES-RDI", 8766),
          ("rmtCSF", 8760),
          ("rmtDefectIndication", 2144),
          ("rmtELinkFail", 8747),
          ("rmtERROR-CCM", 8782),
          ("rmtEthLpb", 8792),
          ("rmtFANFAIL", 8746),
          ("rmtHPDEG", 8717),
          ("rmtHPEXC", 8716),
          ("rmtHPPLM", 8714),
          ("rmtHPRDI", 8715),
          ("rmtHPTIM", 8712),
          ("rmtHPUNEQ", 8713),
          ("rmtHighAppdisk", 8751),
          ("rmtHighRootfs", 8750),
          ("rmtHighSysMem", 8749),
          ("rmtHighTemp", 8744),
          ("rmtKByteMismatch", 8727),
          ("rmtLCK", 8755),
          ("rmtLOC", 8754),
          ("rmtLOF", 8701),
          ("rmtLOPS", 8762),
          ("rmtLOS", 8700),
          ("rmtLPDEG", 8726),
          ("rmtLPEXC", 8725),
          ("rmtLPPLM", 8723),
          ("rmtLPRDI", 8724),
          ("rmtLPTIM", 8721),
          ("rmtLPUNEQ", 8722),
          ("rmtLowTemp", 8745),
          ("rmtLsrMisMatch", 8729),
          ("rmtLsrOffLine", 8730),
          ("rmtMSAIS", 8706),
          ("rmtMSDEG", 8709),
          ("rmtMSEXC", 8708),
          ("rmtMSRDI", 8707),
          ("rmtMismerge", 8756),
          ("rmtONU-MISMATCH", 8780),
          ("rmtOOF", 8702),
          ("rmtOUTSIDEALM1", 8769),
          ("rmtOUTSIDEALM2", 8770),
          ("rmtOUTSIDEALM3", 8771),
          ("rmtOUTSIDEALM4", 8772),
          ("rmtOUTSIDEALM5", 8773),
          ("rmtOUTSIDEALM6", 8774),
          ("rmtOUTSIDEALM7", 8775),
          ("rmtOUTSIDEALM8", 8776),
          ("rmtPAIS", 8728),
          ("rmtPKGFAIL", 8731),
          ("rmtPKGNOTREADY", 8765),
          ("rmtPKGREMOVED", 8733),
          ("rmtPKGTYPE", 8732),
          ("rmtPTPLOS", 8742),
          ("rmtPTPLOT", 8741),
          ("rmtPTSF-lossAnnounce", 8786),
          ("rmtPTSF-lossSync", 8785),
          ("rmtPowerFail", 8743),
          ("rmtRDI", 8753),
          ("rmtRSDEG", 8705),
          ("rmtRSEXC", 8704),
          ("rmtRSTIM", 8703),
          ("rmtSD", 8778),
          ("rmtSF", 8779),
          ("rmtSSD", 8790),
          ("rmtSSF", 8789),
          ("rmtSWPKG-MISMATCH", 8748),
          ("rmtSYNC-Low-QL", 8791),
          ("rmtSYNCAIS", 8738),
          ("rmtSYNCBAD", 8739),
          ("rmtSYNCLOF", 8737),
          ("rmtSYNCLOS", 8736),
          ("rmtSYNCSSMMismatch", 8740),
          ("rmtSYSLTI", 8734),
          ("rmtSYSLTO", 8735),
          ("rmtSlotConfigError", 8764),
          ("rmtSomeRDI", 8783),
          ("rmtSomeRmepCCM", 8784),
          ("rmtTNL-SD", 8793),
          ("rmtTNL-SF", 8794),
          ("rmtTOD-MonitorAlarm", 8787),
          ("rmtTSF", 8763),
          ("rmtTUAIS", 8720),
          ("rmtTULOM", 8719),
          ("rmtTULOP", 8718),
          ("rmtUnexpMel", 8759),
          ("rmtUnexpMep", 8757),
          ("rmtUnexpPrd", 8758),
          ("rmtXCON", 8781),
          ("rmtefmlpbkfail", 3939),
          ("rmtinitlpbk", 3881),
          ("routeTripDelayTooHigh", 3598),
          ("routeTripDelayTooLow", 3599),
          ("routingTableDccConfMismatchBank1", 6261),
          ("routingTableDccConfMismatchBank2", 6262),
          ("routingTableIntegrityFailureBank1", 6263),
          ("routingTableIntegrityFailureBank2", 6264),
          ("routingTableNsapMismatchBank1", 6266),
          ("routingTableNsapMismatchBank2", 6267),
          ("rpr3oClockSpainFail", 744),
          ("rpr9oClockSpainFail", 745),
          ("rprLinkFailureEast", 2069),
          ("rprLinkFailureWest", 2070),
          ("rprMaxStationsExceeded", 2061),
          ("rprMiscablingEast", 2067),
          ("rprMiscablingWest", 2068),
          ("rprProtectionMisconfiguration", 2062),
          ("rprRinglet0A0Exceeding", 2065),
          ("rprRinglet1A0Exceeding", 2066),
          ("rprTopologyInconsistent", 2063),
          ("rprTopologyUnstable", 2064),
          ("rpsConfigurationMismatch", 1932),
          ("rpsLocked", 6259),
          ("rsTim", 6260),
          ("rsTraceMismatch", 8051),
          ("rsa", 250),
          ("rtmUnitForced", 6265),
          ("rx1ewPowerSupply", 6268),
          ("rx1wePowerSupply", 6269),
          ("rx2ewPowerSupply", 6270),
          ("rx2wePowerSupply", 6271),
          ("rx3ewPowerSupply", 6272),
          ("rx3wePowerSupply", 6273),
          ("rx4ewPowerSupply", 6274),
          ("rx4wePowerSupply", 6275),
          ("rx5ewPowerSupply", 6276),
          ("rx5wePowerSupply", 6277),
          ("rx6ewPowerSupply", 6278),
          ("rx6wePowerSupply", 6279),
          ("rx7ewPowerSupply", 6280),
          ("rx7wePowerSupply", 6281),
          ("rx8ewPowerSupply", 6282),
          ("rx8wePowerSupply", 6283),
          ("rxAisInserted", 6284),
          ("rxAlignment", 6285),
          ("rxAuAis1", 6286),
          ("rxAuAis2", 6287),
          ("rxAuAisP", 6288),
          ("rxAuAisW", 6289),
          ("rxAuLop1", 6290),
          ("rxAuLop2", 6291),
          ("rxAuLopP", 6292),
          ("rxAuLopW", 6293),
          ("rxB1SD", 6294),
          ("rxBlockFailure", 6543),
          ("rxCodeSide1", 6296),
          ("rxCodeSide2", 6297),
          ("rxCodeSideA", 6298),
          ("rxCodeSideB", 6299),
          ("rxCodeSideStdby", 6300),
          ("rxConnectedCardMismatch", 1913),
          ("rxDegrade", 253),
          ("rxDem1PowerSupply", 6301),
          ("rxDem2PowerSupply", 6302),
          ("rxDem3PowerSupply", 6303),
          ("rxDem4PowerSupply", 6304),
          ("rxDem5PowerSupply", 6305),
          ("rxDem6PowerSupply", 6306),
          ("rxDem7PowerSupply", 6307),
          ("rxDem8PowerSupply", 6308),
          ("rxDemStdbyPowerSupply", 6309),
          ("rxElasticStoreOverflow", 8012),
          ("rxFail", 254),
          ("rxInput1", 6310),
          ("rxInput2", 6311),
          ("rxInputP", 6312),
          ("rxInputW", 6313),
          ("rxLossOfClock", 8009),
          ("rxManualOperation", 6315),
          ("rxMgc", 6316),
          ("rxODUFailureProtSide", 6611),
          ("rxOduFailure", 6317),
          ("rxOnLineChannelFailure", 6318),
          ("rxOscillator", 6319),
          ("rxPowerFailure", 6320),
          ("rxSideCardFailure", 6295),
          ("rxSignalOverload", 918),
          ("rxSynthFailure", 6321),
          ("rxa", 251),
          ("rxb", 252),
          ("rxjabber", 3940),
          ("rxlineal", 255),
          ("rxsignalOverload", 8066),
          ("sCAZP", 9123),
          ("sCAZW", 9121),
          ("sCCFModuleAbsentAlarm", 2077),
          ("sCCFModuleFailure", 2076),
          ("sCCommunicationFailure", 4500),
          ("sCSWVersionMismatch", 8147),
          ("sCU", 9120),
          ("sCZAP", 9124),
          ("sCZAW", 9122),
          ("sEF", 9526),
          ("sFPAZP", 9108),
          ("sFPAZW", 9106),
          ("sFPU", 9105),
          ("sFPZAP", 9109),
          ("sFPZAW", 9107),
          ("sFWAZP", 9103),
          ("sFWAZW", 9101),
          ("sFWU", 9100),
          ("sFWZAP", 9104),
          ("sFWZAW", 9102),
          ("sLANRingBroken", 4528),
          ("sMPAZP", 9118),
          ("sMPAZW", 9116),
          ("sMPU", 9115),
          ("sMPZAP", 9119),
          ("sMPZAW", 9117),
          ("sMWAZP", 9113),
          ("sMWAZW", 9111),
          ("sMWU", 9110),
          ("sMWZAP", 9114),
          ("sMWZAW", 9112),
          ("sOEsysalmcorttxerr", 2248),
          ("sa4", 256),
          ("sc-mib-sync", 9589),
          ("sc1plus1SyncFailure", 4846),
          ("schedEqlzNeedsNTP", 3587),
          ("scm", 7201),
          ("scs1", 6322),
          ("scs2", 6323),
          ("sdCardFailure", 10001),
          ("sdCardMissing", 10000),
          ("sdRxReceivedLevelDown", 6545),
          ("secADSLVoltageDisc", 9241),
          ("secondSyncMasterDetected", 1015),
          ("sectionSignalDegraded", 8069),
          ("sectionTraceIdMismatch", 6546),
          ("sectionTraceInconsistency", 8050),
          ("sectionTraceMismatch", 416),
          ("sectiontraceMismatch", 8052),
          ("securityLogRollOver", 9986),
          ("securityViolation", 526),
          ("sefs15minThresholdCrossed", 8106),
          ("sefs24hThresholdCrossed", 8107),
          ("selectedDataInput", 6324),
          ("selectedInput", 6326),
          ("selfTestFail", 6325),
          ("sequenceMismatch", 9452),
          ("ser", 257),
          ("serialInterfaceFailure", 6547),
          ("serverNotInSynch", 6772),
          ("serverNotReachable", 6771),
          ("serverSignalFail", 258),
          ("serverSignalFailEgress", 7815),
          ("serverSignalFailOSC", 7819),
          ("serverSignalFailPayload", 7804),
          ("serverSignalFailTx", 3357),
          ("serverSignalFailureGfp", 3350),
          ("serverSignalFailureODU", 3540),
          ("serverSignalFailureODUcrs", 3656),
          ("serverSignalFailurePath", 3351),
          ("serverSignalFailureSectionRS", 3343),
          ("serverSignalFailureVf", 3348),
          ("serverSignalReduced", 3543),
          ("servicePathAlarmIndicationSignal", 8004),
          ("servicePathLossOfFrame", 8035),
          ("servicePathPayloadMismatch", 8073),
          ("servicePathRemoteDefectIndication", 8065),
          ("servicePathUnequipped", 8116),
          ("ses15Min", 6548),
          ("ses15minThresholdCrossed", 8108),
          ("ses24h", 6549),
          ("ses24hThresholdCrossed", 8109),
          ("sfcHwFault", 1019),
          ("sflcf", 4832),
          ("sfpAbsent", 8131),
          ("sfpFailure", 2071),
          ("sfpMismatch", 2072),
          ("sfpMissing", 1035),
          ("sfpMissingLine1", 1948),
          ("sfpMissingLine2", 1949),
          ("sfpMissingP1", 1944),
          ("sfpMissingP2", 1945),
          ("sfpMissingP3", 1946),
          ("sfpMissingP4", 1947),
          ("sfpMissingP5", 1989),
          ("sfpMissingP6", 1990),
          ("sfpMissingP7", 1991),
          ("sfpMissingP8", 1992),
          ("sfpUnqualified1", 1950),
          ("sfpUnqualified2", 1951),
          ("sfpUnqualified3", 1952),
          ("sfpUnqualified4", 1953),
          ("sfpUnqualified5", 1993),
          ("sfpUnqualified6", 1994),
          ("sfpUnqualified7", 1995),
          ("sfpUnqualified8", 1996),
          ("sfpUnqualifiedLine1", 1954),
          ("sfpUnqualifiedLine2", 1955),
          ("sfpmismatchport1", 2040),
          ("sfpmismatchport2", 2041),
          ("sfpmismatchport3", 2042),
          ("sfpmismatchport4", 2043),
          ("sfpmismatchport5", 2100),
          ("sfpmismatchport6", 2101),
          ("sfpmismatchport7", 2102),
          ("sfpmismatchport8", 2103),
          ("sfpmissingport1", 2044),
          ("sfpmissingport2", 2045),
          ("sfpmissingport3", 2046),
          ("sfpmissingport4", 2047),
          ("sfwrProblem", 259),
          ("sfwrProblemMajor", 260),
          ("shaperbtd", 3941),
          ("sharedData", 6327),
          ("shelfAddressChanged", 1081),
          ("shelfDcFilterFailure", 6738),
          ("shelfDcFilterRemoved", 6777),
          ("shelfInserted", 2030),
          ("shelfMissing", 3462),
          ("shelfRemoved", 2029),
          ("shutdownAmbientTemperature", 9498),
          ("side1", 6328),
          ("side1Sd", 6329),
          ("side2", 6330),
          ("side2Sd", 6331),
          ("sideA", 6332),
          ("sideA12", 6333),
          ("sideA12Sd", 6334),
          ("sideA13", 6335),
          ("sideA13Sd", 6336),
          ("sideASd", 6337),
          ("sideB", 6338),
          ("sideB12", 6339),
          ("sideB24", 6340),
          ("sideB3", 6341),
          ("sideBsd", 6342),
          ("signalDegradeB2", 6544),
          ("signalDegradeHighProtSide", 6605),
          ("signalDegradeLowProtSide", 6606),
          ("signalDegraded", 261),
          ("signalDegradedEgress", 4836),
          ("signalFailureOPU", 3541),
          ("signalFailureOnLink", 3349),
          ("signalLabelMismatch", 6550),
          ("signalLableMismatch", 262),
          ("signalToNoiseDegrade", 263),
          ("signalToNoiseDriftLowDegrade", 264),
          ("signalToNoiseFailure", 265),
          ("signalToNoiseRatioTooLow", 3628),
          ("signalfailure", 2275),
          ("silvxBLSRLaserShutdown", 7300),
          ("silvxBLSRPeerCommDown", 7302),
          ("silvxBridgeAndRollInProgress", 7317),
          ("silvxCCRefMism", 7437),
          ("silvxCGDegraded", 7322),
          ("silvxCGDiffDelayExceeded", 7323),
          ("silvxCGDown", 7321),
          ("silvxCGLossAlignment", 7325),
          ("silvxCGLossMultiframe", 7326),
          ("silvxCGSequenceError", 7324),
          ("silvxCardAdmDwn", 7424),
          ("silvxCardBoot", 7426),
          ("silvxCardLampTE", 7435),
          ("silvxCardPendRm", 7427),
          ("silvxCardTRCInit", 7431),
          ("silvxCleiLIMError", 7351),
          ("silvxCleiPortError", 7352),
          ("silvxEthernetServiceDegraded", 7320),
          ("silvxEthernetServiceDown", 7319),
          ("silvxEthernetServiceLocalCLF", 7341),
          ("silvxEthernetServiceRemoteCLF", 7342),
          ("silvxLIMHwMaintenanceRequired", 7347),
          ("silvxLIMSoftwareFailure", 7346),
          ("silvxLicenseExceeded", 7349),
          ("silvxLicenseExpired", 7350),
          ("silvxLicenseInvalid", 7348),
          ("silvxLimEepromFailure", 7308),
          ("silvxLimFpgaFailure", 7309),
          ("silvxLimFpgaVersionMismatch", 7310),
          ("silvxLimHardwareFailure", 7307),
          ("silvxLimHwConfigInvalid", 7305),
          ("silvxLimInvalid", 7306),
          ("silvxLimTemp", 7311),
          ("silvxMismatchedConfigRemoteCLF", 7344),
          ("silvxNetworkConnectionProblem", 7343),
          ("silvxNoSystemTimingSrcProv", 7339),
          ("silvxNodeLampTE", 7433),
          ("silvxPPGAutoSwitchToProtPDI", 7334),
          ("silvxPPGAutoSwitchToProtSD", 7336),
          ("silvxPPGAutoSwitchToProtSF", 7331),
          ("silvxPPGAutoSwitchToProtSFBER", 7333),
          ("silvxPPGAutoSwitchToProtTIM", 7335),
          ("silvxPPGAutoSwitchToProtWARM", 7332),
          ("silvxPPGAutoSwitchToProtWTR", 7338),
          ("silvxPPGForceToProtection", 7330),
          ("silvxPPGForceToWorking", 7329),
          ("silvxPPGLockoutProtection", 7328),
          ("silvxPPGMsToProt", 7337),
          ("silvxPathAlFail", 7429),
          ("silvxPathLbMism", 7432),
          ("silvxPeerDiscLostContact", 7327),
          ("silvxPortAdmDwn", 7425),
          ("silvxPortEepromFailure", 7315),
          ("silvxPortHardwareFailure", 7316),
          ("silvxPortInvalid", 7313),
          ("silvxPortMismatch", 7312),
          ("silvxPortMiss", 7436),
          ("silvxPortMissing", 7314),
          ("silvxRollToPathDown", 7318),
          ("silvxRxFifoOverfl", 7438),
          ("silvxSectionTraceIdMismatch", 7301),
          ("silvxShelfLampTE", 7434),
          ("silvxSigIPPMFail", 7428),
          ("silvxSoftwareActivation", 7345),
          ("silvxSysTimFreeRun", 7421),
          ("silvxSysTimLowSrc", 7422),
          ("silvxSysTimORef", 7423),
          ("silvxTRCPMCProb", 7430),
          ("silvxTimingModuleStablizing", 7340),
          ("silvxTrcPullinCapCfgMismatch", 7304),
          ("silvxTrcPullinCfgMismatch", 7303),
          ("slotLSBMismatch", 3440),
          ("smoke", 266),
          ("snmpEngineConnFailure", 9448),
          ("snmpTrapRegisterFailure", 9455),
          ("snmpdghostresourcesbusy", 3964),
          ("snmpdghostunresolved", 3965),
          ("snp", 267),
          ("softwareAbortCompleted", 9460),
          ("softwareAbortFail", 9459),
          ("softwareAbortProgress", 9458),
          ("softwareDownloadCompleted", 9987),
          ("softwareDownloadFailed", 6739),
          ("softwareDownloading", 6779),
          ("softwareExecCompleted", 9993),
          ("softwareExecFail", 9992),
          ("softwareExecPartial", 9457),
          ("softwareExecProgress", 9991),
          ("softwareInstallCompleted", 9990),
          ("softwareInstallFail", 9989),
          ("softwareInstallProgress", 9988),
          ("softwareManagementFailure", 2129),
          ("softwarePatchAbort", 9994),
          ("softwareUnpackFailed", 6740),
          ("softwareUpgradeAbort", 9995),
          ("softwareUpgradeActionRequired", 9622),
          ("someRDIdefect", 9564),
          ("someRMEPCCMdefect", 9563),
          ("somemacstatus", 3942),
          ("somerdi", 3943),
          ("someremotemepccm", 3944),
          ("spanLossHigh", 960),
          ("spanLossLow", 959),
          ("sqm", 268),
          ("sqnc", 3997),
          ("squelchEastWorkTraffic", 6741),
          ("squelchStatus", 9851),
          ("squelchWestWorkTraffic", 6742),
          ("ssfEast", 269),
          ("ssfEastExtra", 270),
          ("ssfExtra", 271),
          ("ssfProtSide", 6626),
          ("ssfProtection", 3425),
          ("ssfWest", 272),
          ("ssfWestExtra", 273),
          ("ssfWestWorking", 274),
          ("ssfWorking", 275),
          ("ssignalFailHigherOrderPath", 2281),
          ("standbyEngineTransfer", 9226),
          ("stationAlarm1", 6571),
          ("stationAlarm10", 6580),
          ("stationAlarm11", 6581),
          ("stationAlarm12", 6582),
          ("stationAlarm13", 6583),
          ("stationAlarm14", 6584),
          ("stationAlarm15", 6585),
          ("stationAlarm16", 6586),
          ("stationAlarm17", 6587),
          ("stationAlarm18", 6588),
          ("stationAlarm19", 6589),
          ("stationAlarm2", 6572),
          ("stationAlarm20", 6590),
          ("stationAlarm21", 6591),
          ("stationAlarm22", 6592),
          ("stationAlarm23", 6593),
          ("stationAlarm24", 6594),
          ("stationAlarm25", 6595),
          ("stationAlarm26", 6596),
          ("stationAlarm27", 6597),
          ("stationAlarm28", 6598),
          ("stationAlarm29", 6599),
          ("stationAlarm3", 6573),
          ("stationAlarm30", 6600),
          ("stationAlarm31", 6601),
          ("stationAlarm32", 6602),
          ("stationAlarm4", 6574),
          ("stationAlarm5", 6575),
          ("stationAlarm6", 6576),
          ("stationAlarm7", 6577),
          ("stationAlarm8", 6578),
          ("stationAlarm9", 6579),
          ("statusOfModuleToModuleCommunication", 809),
          ("statusOfSpiHw", 821),
          ("statusOfTheLocalOscillatorPhaseLockLoop", 816),
          ("statusOfTheNumericallyCntrlOscillPhaseLockLoop", 815),
          ("statusOfTheRubidiumInternalPhaseLockLoop", 817),
          ("statusPowerA", 819),
          ("statusPowerB", 820),
          ("stm1B1SdExp", 6343),
          ("stm1B1SdMain", 6344),
          ("stm1FailExp", 6345),
          ("stm1FailMain", 6346),
          ("storageCapacity", 276),
          ("storageCapacityProblem", 277),
          ("storageFailure", 1921),
          ("subAddressBoardFailure", 419),
          ("subBandLossOfSignal", 3452),
          ("subModTempOoR", 504),
          ("subModuleTempOutOfRange", 8075),
          ("subSystemFailure", 932),
          ("subSystemMissing", 931),
          ("subbandLoss", 804),
          ("subrackCoolingProblem", 534),
          ("subrackMissing", 7806),
          ("subrackOverequipped", 7805),
          ("subsysMissing", 3484),
          ("subsystemMismatchH73", 1978),
          ("subsystemMismatchHDS", 2113),
          ("sumAlarm", 278),
          ("svBackupSubunitFailure", 6551),
          ("swAbnormallyTerminated", 279),
          ("swDownloadFailure", 6562),
          ("swDownloadInOcu40Failed", 1898),
          ("swEnvProblem", 280),
          ("swIncomplete", 885),
          ("swIntegrityFailureBank1", 6347),
          ("swIntegrityFailureBank2", 6348),
          ("swNotAligned", 6565),
          ("swPatch", 9973),
          ("swProgramError", 282),
          ("swUpgrade", 9974),
          ("swUpgradeCommit", 9456),
          ("swUpgradeFault", 1039),
          ("swUpgradeHault", 1038),
          ("swUpgradeWait", 9975),
          ("swVersionMismatch", 6743),
          ("swVersionMismatch2", 6554),
          ("swapPreparationFailure", 1900),
          ("swapPreparationFailureProc", 2130),
          ("swdlactip", 3973),
          ("swdlftip", 3974),
          ("swdlinstip", 3975),
          ("swdlproip", 3990),
          ("swdlrvtip", 3992),
          ("swdlvalip", 3976),
          ("switch", 281),
          ("switchError", 547),
          ("switchExerciseRingFailed", 6768),
          ("switchExerciseSpanFailed", 6769),
          ("switchFabricNotEnough", 4502),
          ("switchFabricWithoutProtection", 4501),
          ("switchFailureInBsw", 6552),
          ("switchFailureInUsw", 6553),
          ("switchHsbyFailure", 6356),
          ("switchProblem", 973),
          ("switchProblem1", 438),
          ("switchProblem2", 437),
          ("switchProblem3", 805),
          ("switchProblem4", 806),
          ("switchProblemUpgradePath", 436),
          ("switchToDuplexInhibited", 3683),
          ("switcherror", 8076),
          ("switchingAlarmChannel1", 6349),
          ("switchingAlarmChannel2", 6350),
          ("switchingAlarmChannel3", 6351),
          ("switchingAlarmChannel4", 6352),
          ("switchingAlarmChannel5", 6353),
          ("switchingAlarmChannel6", 6354),
          ("switchingAlarmChannel7", 6355),
          ("switchingFabricLinkCommunicationFailure", 4534),
          ("switchingTestFailureStdby", 6364),
          ("switchingTestFailureStdbyChannel1", 6357),
          ("switchingTestFailureStdbyChannel2", 6358),
          ("switchingTestFailureStdbyChannel3", 6359),
          ("switchingTestFailureStdbyChannel4", 6360),
          ("switchingTestFailureStdbyChannel5", 6361),
          ("switchingTestFailureStdbyChannel6", 6362),
          ("switchingTestFailureStdbyChannel7", 6363),
          ("syncFail", 999),
          ("syncFailEgress", 7816),
          ("syncFailure", 3426),
          ("syncFailureMain", 6365),
          ("syncInProgress", 1920),
          ("syncOn", 6366),
          ("syncSignalMessageMismatch", 1821),
          ("synchronizationReferenceFailure", 9934),
          ("synchronizationSourceMismatch", 283),
          ("syncnotready", 3945),
          ("syncref", 3946),
          ("syncreffrc", 3947),
          ("syncreflck", 3948),
          ("syncrefman", 3949),
          ("syncrefwtr", 3950),
          ("synthetizer", 6367),
          ("syslogAuthenticationFailure", 2500),
          ("syslogConnectionFailure", 2501),
          ("systemBackupKey", 6368),
          ("systemBackupKeyNotAligned", 6566),
          ("systemBackupKeyNotInserted", 6369),
          ("systemClockHoldoverLonger", 1819),
          ("systemClockUnlock", 9556),
          ("systemForced1Plus0MasterConfig", 6370),
          ("systemInitInProgress", 6632),
          ("systemSwFault", 843),
          ("systemSwitchesFrozen", 6371),
          ("t0", 882),
          ("t0BusX", 284),
          ("t0BusY", 285),
          ("t0Quality", 286),
          ("t0X", 883),
          ("t0Y", 884),
          ("t11BadSSM", 2051),
          ("t12BadSSM", 2052),
          ("t13BadSSM", 2053),
          ("t14BadSSM", 2054),
          ("t15BadSSM", 2055),
          ("t16BadSSM", 2056),
          ("t17BadSSM", 2057),
          ("t18BadSSM", 2058),
          ("tIFActivatedAlarm", 1049),
          ("tIFActivatedAlarm1", 2131),
          ("tIFActivatedAlarm2", 2132),
          ("tIFActivatedAlarm3", 2133),
          ("tIFActivatedAlarm4", 2134),
          ("tIMR", 9952),
          ("tRepeater", 9274),
          ("tamperEvent", 3590),
          ("tandemConnectionSignalDegraded", 529),
          ("targetNEFailure", 7809),
          ("targetValueNotReached", 807),
          ("tcPathTraceMismatch", 530),
          ("tcRdi", 528),
          ("tcUnequipped", 531),
          ("tdcControlLoopLimit", 3464),
          ("telemetryInterface1", 287),
          ("telemetryInterface1-1", 638),
          ("telemetryInterface1-10", 639),
          ("telemetryInterface1-11", 640),
          ("telemetryInterface1-12", 641),
          ("telemetryInterface1-13", 642),
          ("telemetryInterface1-14", 643),
          ("telemetryInterface1-15", 644),
          ("telemetryInterface1-16", 646),
          ("telemetryInterface1-2", 637),
          ("telemetryInterface1-3", 636),
          ("telemetryInterface1-4", 630),
          ("telemetryInterface1-5", 631),
          ("telemetryInterface1-6", 632),
          ("telemetryInterface1-7", 633),
          ("telemetryInterface1-8", 634),
          ("telemetryInterface1-9", 635),
          ("telemetryInterface10", 288),
          ("telemetryInterface11", 289),
          ("telemetryInterface12", 290),
          ("telemetryInterface13", 291),
          ("telemetryInterface14", 292),
          ("telemetryInterface15", 293),
          ("telemetryInterface16", 294),
          ("telemetryInterface17", 295),
          ("telemetryInterface18", 296),
          ("telemetryInterface180-1", 1100),
          ("telemetryInterface180-10", 1101),
          ("telemetryInterface180-11", 1102),
          ("telemetryInterface180-12", 1103),
          ("telemetryInterface180-13", 1104),
          ("telemetryInterface180-14", 1105),
          ("telemetryInterface180-15", 1106),
          ("telemetryInterface180-16", 1107),
          ("telemetryInterface180-2", 1108),
          ("telemetryInterface180-3", 1109),
          ("telemetryInterface180-4", 1110),
          ("telemetryInterface180-5", 1111),
          ("telemetryInterface180-6", 1112),
          ("telemetryInterface180-7", 1113),
          ("telemetryInterface180-8", 1114),
          ("telemetryInterface180-9", 1115),
          ("telemetryInterface181-1", 1116),
          ("telemetryInterface181-10", 1117),
          ("telemetryInterface181-11", 1118),
          ("telemetryInterface181-12", 1119),
          ("telemetryInterface181-13", 1120),
          ("telemetryInterface181-14", 1121),
          ("telemetryInterface181-15", 1122),
          ("telemetryInterface181-16", 1123),
          ("telemetryInterface181-2", 1124),
          ("telemetryInterface181-3", 1125),
          ("telemetryInterface181-4", 1126),
          ("telemetryInterface181-5", 1127),
          ("telemetryInterface181-6", 1128),
          ("telemetryInterface181-7", 1129),
          ("telemetryInterface181-8", 1130),
          ("telemetryInterface181-9", 1131),
          ("telemetryInterface182-1", 1132),
          ("telemetryInterface182-10", 1133),
          ("telemetryInterface182-11", 1134),
          ("telemetryInterface182-12", 1135),
          ("telemetryInterface182-13", 1136),
          ("telemetryInterface182-14", 1137),
          ("telemetryInterface182-15", 1138),
          ("telemetryInterface182-16", 1139),
          ("telemetryInterface182-2", 1140),
          ("telemetryInterface182-3", 1141),
          ("telemetryInterface182-4", 1142),
          ("telemetryInterface182-5", 1143),
          ("telemetryInterface182-6", 1144),
          ("telemetryInterface182-7", 1145),
          ("telemetryInterface182-8", 1146),
          ("telemetryInterface182-9", 1147),
          ("telemetryInterface183-1", 1148),
          ("telemetryInterface183-10", 1149),
          ("telemetryInterface183-11", 1150),
          ("telemetryInterface183-12", 1151),
          ("telemetryInterface183-13", 1152),
          ("telemetryInterface183-14", 1153),
          ("telemetryInterface183-15", 1154),
          ("telemetryInterface183-16", 1155),
          ("telemetryInterface183-2", 1156),
          ("telemetryInterface183-3", 1157),
          ("telemetryInterface183-4", 1158),
          ("telemetryInterface183-5", 1159),
          ("telemetryInterface183-6", 1160),
          ("telemetryInterface183-7", 1161),
          ("telemetryInterface183-8", 1162),
          ("telemetryInterface183-9", 1163),
          ("telemetryInterface184-1", 1164),
          ("telemetryInterface184-10", 1165),
          ("telemetryInterface184-11", 1166),
          ("telemetryInterface184-12", 1167),
          ("telemetryInterface184-13", 1168),
          ("telemetryInterface184-14", 1169),
          ("telemetryInterface184-15", 1170),
          ("telemetryInterface184-16", 1171),
          ("telemetryInterface184-2", 1172),
          ("telemetryInterface184-3", 1173),
          ("telemetryInterface184-4", 1174),
          ("telemetryInterface184-5", 1175),
          ("telemetryInterface184-6", 1176),
          ("telemetryInterface184-7", 1177),
          ("telemetryInterface184-8", 1178),
          ("telemetryInterface184-9", 1179),
          ("telemetryInterface185-1", 1180),
          ("telemetryInterface185-10", 1181),
          ("telemetryInterface185-11", 1182),
          ("telemetryInterface185-12", 1183),
          ("telemetryInterface185-13", 1184),
          ("telemetryInterface185-14", 1185),
          ("telemetryInterface185-15", 1186),
          ("telemetryInterface185-16", 1187),
          ("telemetryInterface185-2", 1188),
          ("telemetryInterface185-3", 1189),
          ("telemetryInterface185-4", 1190),
          ("telemetryInterface185-5", 1191),
          ("telemetryInterface185-6", 1192),
          ("telemetryInterface185-7", 1193),
          ("telemetryInterface185-8", 1194),
          ("telemetryInterface185-9", 1195),
          ("telemetryInterface186-1", 1196),
          ("telemetryInterface186-10", 1197),
          ("telemetryInterface186-11", 1198),
          ("telemetryInterface186-12", 1199),
          ("telemetryInterface186-13", 1200),
          ("telemetryInterface186-14", 1201),
          ("telemetryInterface186-15", 1202),
          ("telemetryInterface186-16", 1203),
          ("telemetryInterface186-2", 1204),
          ("telemetryInterface186-3", 1205),
          ("telemetryInterface186-4", 1206),
          ("telemetryInterface186-5", 1207),
          ("telemetryInterface186-6", 1208),
          ("telemetryInterface186-7", 1209),
          ("telemetryInterface186-8", 1210),
          ("telemetryInterface186-9", 1211),
          ("telemetryInterface187-1", 1212),
          ("telemetryInterface187-10", 1213),
          ("telemetryInterface187-11", 1214),
          ("telemetryInterface187-12", 1215),
          ("telemetryInterface187-13", 1216),
          ("telemetryInterface187-14", 1217),
          ("telemetryInterface187-15", 1218),
          ("telemetryInterface187-16", 1219),
          ("telemetryInterface187-2", 1220),
          ("telemetryInterface187-3", 1221),
          ("telemetryInterface187-4", 1222),
          ("telemetryInterface187-5", 1223),
          ("telemetryInterface187-6", 1224),
          ("telemetryInterface187-7", 1225),
          ("telemetryInterface187-8", 1226),
          ("telemetryInterface187-9", 1227),
          ("telemetryInterface19", 297),
          ("telemetryInterface2", 298),
          ("telemetryInterface2-1", 655),
          ("telemetryInterface2-10", 656),
          ("telemetryInterface2-11", 657),
          ("telemetryInterface2-12", 658),
          ("telemetryInterface2-13", 659),
          ("telemetryInterface2-14", 660),
          ("telemetryInterface2-15", 661),
          ("telemetryInterface2-16", 662),
          ("telemetryInterface2-2", 654),
          ("telemetryInterface2-3", 653),
          ("telemetryInterface2-4", 647),
          ("telemetryInterface2-5", 648),
          ("telemetryInterface2-6", 649),
          ("telemetryInterface2-7", 650),
          ("telemetryInterface2-8", 651),
          ("telemetryInterface2-9", 652),
          ("telemetryInterface20", 299),
          ("telemetryInterface200-1", 1228),
          ("telemetryInterface200-10", 1229),
          ("telemetryInterface200-11", 1230),
          ("telemetryInterface200-12", 1231),
          ("telemetryInterface200-13", 1232),
          ("telemetryInterface200-14", 1233),
          ("telemetryInterface200-15", 1234),
          ("telemetryInterface200-16", 1235),
          ("telemetryInterface200-2", 1236),
          ("telemetryInterface200-3", 1237),
          ("telemetryInterface200-4", 1238),
          ("telemetryInterface200-5", 1239),
          ("telemetryInterface200-6", 1240),
          ("telemetryInterface200-7", 1241),
          ("telemetryInterface200-8", 1242),
          ("telemetryInterface200-9", 1243),
          ("telemetryInterface201-1", 1244),
          ("telemetryInterface201-10", 1245),
          ("telemetryInterface201-11", 1246),
          ("telemetryInterface201-12", 1247),
          ("telemetryInterface201-13", 1248),
          ("telemetryInterface201-14", 1249),
          ("telemetryInterface201-15", 1250),
          ("telemetryInterface201-16", 1251),
          ("telemetryInterface201-2", 1252),
          ("telemetryInterface201-3", 1253),
          ("telemetryInterface201-4", 1254),
          ("telemetryInterface201-5", 1255),
          ("telemetryInterface201-6", 1256),
          ("telemetryInterface201-7", 1257),
          ("telemetryInterface201-8", 1258),
          ("telemetryInterface201-9", 1259),
          ("telemetryInterface202-1", 1260),
          ("telemetryInterface202-10", 1261),
          ("telemetryInterface202-11", 1262),
          ("telemetryInterface202-12", 1263),
          ("telemetryInterface202-13", 1264),
          ("telemetryInterface202-14", 1265),
          ("telemetryInterface202-15", 1266),
          ("telemetryInterface202-16", 1267),
          ("telemetryInterface202-2", 1268),
          ("telemetryInterface202-3", 1269),
          ("telemetryInterface202-4", 1270),
          ("telemetryInterface202-5", 1271),
          ("telemetryInterface202-6", 1272),
          ("telemetryInterface202-7", 1273),
          ("telemetryInterface202-8", 1274),
          ("telemetryInterface202-9", 1275),
          ("telemetryInterface203-1", 1276),
          ("telemetryInterface203-10", 1277),
          ("telemetryInterface203-11", 1278),
          ("telemetryInterface203-12", 1279),
          ("telemetryInterface203-13", 1280),
          ("telemetryInterface203-14", 1281),
          ("telemetryInterface203-15", 1282),
          ("telemetryInterface203-16", 1283),
          ("telemetryInterface203-2", 1284),
          ("telemetryInterface203-3", 1285),
          ("telemetryInterface203-4", 1286),
          ("telemetryInterface203-5", 1287),
          ("telemetryInterface203-6", 1288),
          ("telemetryInterface203-7", 1289),
          ("telemetryInterface203-8", 1290),
          ("telemetryInterface203-9", 1291),
          ("telemetryInterface204-1", 1292),
          ("telemetryInterface204-10", 1293),
          ("telemetryInterface204-11", 1294),
          ("telemetryInterface204-12", 1295),
          ("telemetryInterface204-13", 1296),
          ("telemetryInterface204-14", 1297),
          ("telemetryInterface204-15", 1298),
          ("telemetryInterface204-16", 1299),
          ("telemetryInterface204-2", 1300),
          ("telemetryInterface204-3", 1301),
          ("telemetryInterface204-4", 1302),
          ("telemetryInterface204-5", 1303),
          ("telemetryInterface204-6", 1304),
          ("telemetryInterface204-7", 1305),
          ("telemetryInterface204-8", 1306),
          ("telemetryInterface204-9", 1307),
          ("telemetryInterface205-1", 1308),
          ("telemetryInterface205-10", 1309),
          ("telemetryInterface205-11", 1310),
          ("telemetryInterface205-12", 1311),
          ("telemetryInterface205-13", 1312),
          ("telemetryInterface205-14", 1313),
          ("telemetryInterface205-15", 1314),
          ("telemetryInterface205-16", 1315),
          ("telemetryInterface205-2", 1316),
          ("telemetryInterface205-3", 1317),
          ("telemetryInterface205-4", 1318),
          ("telemetryInterface205-5", 1319),
          ("telemetryInterface205-6", 1320),
          ("telemetryInterface205-7", 1321),
          ("telemetryInterface205-8", 1322),
          ("telemetryInterface205-9", 1323),
          ("telemetryInterface206-1", 1324),
          ("telemetryInterface206-10", 1325),
          ("telemetryInterface206-11", 1326),
          ("telemetryInterface206-12", 1327),
          ("telemetryInterface206-13", 1328),
          ("telemetryInterface206-14", 1329),
          ("telemetryInterface206-15", 1330),
          ("telemetryInterface206-16", 1331),
          ("telemetryInterface206-2", 1332),
          ("telemetryInterface206-3", 1333),
          ("telemetryInterface206-4", 1334),
          ("telemetryInterface206-5", 1335),
          ("telemetryInterface206-6", 1336),
          ("telemetryInterface206-7", 1337),
          ("telemetryInterface206-8", 1338),
          ("telemetryInterface206-9", 1339),
          ("telemetryInterface207-1", 1340),
          ("telemetryInterface207-10", 1341),
          ("telemetryInterface207-11", 1342),
          ("telemetryInterface207-12", 1343),
          ("telemetryInterface207-13", 1344),
          ("telemetryInterface207-14", 1345),
          ("telemetryInterface207-15", 1346),
          ("telemetryInterface207-16", 1347),
          ("telemetryInterface207-2", 1348),
          ("telemetryInterface207-3", 1349),
          ("telemetryInterface207-4", 1350),
          ("telemetryInterface207-5", 1351),
          ("telemetryInterface207-6", 1352),
          ("telemetryInterface207-7", 1353),
          ("telemetryInterface207-8", 1354),
          ("telemetryInterface207-9", 1355),
          ("telemetryInterface21", 300),
          ("telemetryInterface210-1", 1356),
          ("telemetryInterface210-10", 1357),
          ("telemetryInterface210-11", 1358),
          ("telemetryInterface210-12", 1359),
          ("telemetryInterface210-13", 1360),
          ("telemetryInterface210-14", 1361),
          ("telemetryInterface210-15", 1362),
          ("telemetryInterface210-16", 1363),
          ("telemetryInterface210-2", 1364),
          ("telemetryInterface210-3", 1365),
          ("telemetryInterface210-4", 1366),
          ("telemetryInterface210-5", 1367),
          ("telemetryInterface210-6", 1368),
          ("telemetryInterface210-7", 1369),
          ("telemetryInterface210-8", 1370),
          ("telemetryInterface210-9", 1371),
          ("telemetryInterface211-1", 1372),
          ("telemetryInterface211-10", 1373),
          ("telemetryInterface211-11", 1374),
          ("telemetryInterface211-12", 1375),
          ("telemetryInterface211-13", 1376),
          ("telemetryInterface211-14", 1377),
          ("telemetryInterface211-15", 1378),
          ("telemetryInterface211-16", 1379),
          ("telemetryInterface211-2", 1380),
          ("telemetryInterface211-3", 1381),
          ("telemetryInterface211-4", 1382),
          ("telemetryInterface211-5", 1383),
          ("telemetryInterface211-6", 1384),
          ("telemetryInterface211-7", 1385),
          ("telemetryInterface211-8", 1386),
          ("telemetryInterface211-9", 1387),
          ("telemetryInterface212-1", 1388),
          ("telemetryInterface212-10", 1389),
          ("telemetryInterface212-11", 1390),
          ("telemetryInterface212-12", 1391),
          ("telemetryInterface212-13", 1392),
          ("telemetryInterface212-14", 1393),
          ("telemetryInterface212-15", 1394),
          ("telemetryInterface212-16", 1395),
          ("telemetryInterface212-2", 1396),
          ("telemetryInterface212-3", 1397),
          ("telemetryInterface212-4", 1398),
          ("telemetryInterface212-5", 1399),
          ("telemetryInterface212-6", 1400),
          ("telemetryInterface212-7", 1401),
          ("telemetryInterface212-8", 1402),
          ("telemetryInterface212-9", 1403),
          ("telemetryInterface213-1", 1404),
          ("telemetryInterface213-10", 1405),
          ("telemetryInterface213-11", 1406),
          ("telemetryInterface213-12", 1407),
          ("telemetryInterface213-13", 1408),
          ("telemetryInterface213-14", 1409),
          ("telemetryInterface213-15", 1410),
          ("telemetryInterface213-16", 1411),
          ("telemetryInterface213-2", 1412),
          ("telemetryInterface213-3", 1413),
          ("telemetryInterface213-4", 1414),
          ("telemetryInterface213-5", 1415),
          ("telemetryInterface213-6", 1416),
          ("telemetryInterface213-7", 1417),
          ("telemetryInterface213-8", 1418),
          ("telemetryInterface213-9", 1419),
          ("telemetryInterface214-1", 1420),
          ("telemetryInterface214-10", 1421),
          ("telemetryInterface214-11", 1422),
          ("telemetryInterface214-12", 1423),
          ("telemetryInterface214-13", 1424),
          ("telemetryInterface214-14", 1425),
          ("telemetryInterface214-15", 1426),
          ("telemetryInterface214-16", 1427),
          ("telemetryInterface214-2", 1428),
          ("telemetryInterface214-3", 1429),
          ("telemetryInterface214-4", 1430),
          ("telemetryInterface214-5", 1431),
          ("telemetryInterface214-6", 1432),
          ("telemetryInterface214-7", 1433),
          ("telemetryInterface214-8", 1434),
          ("telemetryInterface214-9", 1435),
          ("telemetryInterface215-1", 1436),
          ("telemetryInterface215-10", 1437),
          ("telemetryInterface215-11", 1438),
          ("telemetryInterface215-12", 1439),
          ("telemetryInterface215-13", 1440),
          ("telemetryInterface215-14", 1441),
          ("telemetryInterface215-15", 1442),
          ("telemetryInterface215-16", 1443),
          ("telemetryInterface215-2", 1444),
          ("telemetryInterface215-3", 1445),
          ("telemetryInterface215-4", 1446),
          ("telemetryInterface215-5", 1447),
          ("telemetryInterface215-6", 1448),
          ("telemetryInterface215-7", 1449),
          ("telemetryInterface215-8", 1450),
          ("telemetryInterface215-9", 1451),
          ("telemetryInterface216-1", 1452),
          ("telemetryInterface216-10", 1453),
          ("telemetryInterface216-11", 1454),
          ("telemetryInterface216-12", 1455),
          ("telemetryInterface216-13", 1456),
          ("telemetryInterface216-14", 1457),
          ("telemetryInterface216-15", 1458),
          ("telemetryInterface216-16", 1459),
          ("telemetryInterface216-2", 1460),
          ("telemetryInterface216-3", 1461),
          ("telemetryInterface216-4", 1462),
          ("telemetryInterface216-5", 1463),
          ("telemetryInterface216-6", 1464),
          ("telemetryInterface216-7", 1465),
          ("telemetryInterface216-8", 1466),
          ("telemetryInterface216-9", 1467),
          ("telemetryInterface217-1", 1468),
          ("telemetryInterface217-10", 1469),
          ("telemetryInterface217-11", 1470),
          ("telemetryInterface217-12", 1471),
          ("telemetryInterface217-13", 1472),
          ("telemetryInterface217-14", 1473),
          ("telemetryInterface217-15", 1474),
          ("telemetryInterface217-16", 1475),
          ("telemetryInterface217-2", 1476),
          ("telemetryInterface217-3", 1477),
          ("telemetryInterface217-4", 1478),
          ("telemetryInterface217-5", 1479),
          ("telemetryInterface217-6", 1480),
          ("telemetryInterface217-7", 1481),
          ("telemetryInterface217-8", 1482),
          ("telemetryInterface217-9", 1483),
          ("telemetryInterface22", 301),
          ("telemetryInterface23", 302),
          ("telemetryInterface24", 303),
          ("telemetryInterface25", 304),
          ("telemetryInterface26", 305),
          ("telemetryInterface27", 306),
          ("telemetryInterface28", 307),
          ("telemetryInterface29", 308),
          ("telemetryInterface3", 309),
          ("telemetryInterface3-1", 671),
          ("telemetryInterface3-10", 672),
          ("telemetryInterface3-11", 673),
          ("telemetryInterface3-12", 674),
          ("telemetryInterface3-13", 675),
          ("telemetryInterface3-14", 676),
          ("telemetryInterface3-15", 677),
          ("telemetryInterface3-16", 678),
          ("telemetryInterface3-2", 670),
          ("telemetryInterface3-3", 669),
          ("telemetryInterface3-4", 663),
          ("telemetryInterface3-5", 664),
          ("telemetryInterface3-6", 665),
          ("telemetryInterface3-7", 666),
          ("telemetryInterface3-8", 667),
          ("telemetryInterface3-9", 668),
          ("telemetryInterface30", 310),
          ("telemetryInterface300-1", 1484),
          ("telemetryInterface300-10", 1485),
          ("telemetryInterface300-11", 1486),
          ("telemetryInterface300-12", 1487),
          ("telemetryInterface300-13", 1488),
          ("telemetryInterface300-14", 1489),
          ("telemetryInterface300-15", 1490),
          ("telemetryInterface300-16", 1491),
          ("telemetryInterface300-2", 1492),
          ("telemetryInterface300-3", 1493),
          ("telemetryInterface300-4", 1494),
          ("telemetryInterface300-5", 1495),
          ("telemetryInterface300-6", 1496),
          ("telemetryInterface300-7", 1497),
          ("telemetryInterface300-8", 1498),
          ("telemetryInterface300-9", 1499),
          ("telemetryInterface301-1", 1500),
          ("telemetryInterface301-10", 1501),
          ("telemetryInterface301-11", 1502),
          ("telemetryInterface301-12", 1503),
          ("telemetryInterface301-13", 1504),
          ("telemetryInterface301-14", 1505),
          ("telemetryInterface301-15", 1506),
          ("telemetryInterface301-16", 1507),
          ("telemetryInterface301-2", 1508),
          ("telemetryInterface301-3", 1509),
          ("telemetryInterface301-4", 1510),
          ("telemetryInterface301-5", 1511),
          ("telemetryInterface301-6", 1512),
          ("telemetryInterface301-7", 1513),
          ("telemetryInterface301-8", 1514),
          ("telemetryInterface301-9", 1515),
          ("telemetryInterface302-1", 1516),
          ("telemetryInterface302-10", 1517),
          ("telemetryInterface302-11", 1518),
          ("telemetryInterface302-12", 1519),
          ("telemetryInterface302-13", 1520),
          ("telemetryInterface302-14", 1521),
          ("telemetryInterface302-15", 1522),
          ("telemetryInterface302-16", 1523),
          ("telemetryInterface302-2", 1524),
          ("telemetryInterface302-3", 1525),
          ("telemetryInterface302-4", 1526),
          ("telemetryInterface302-5", 1527),
          ("telemetryInterface302-6", 1528),
          ("telemetryInterface302-7", 1529),
          ("telemetryInterface302-8", 1530),
          ("telemetryInterface302-9", 1531),
          ("telemetryInterface303-1", 1532),
          ("telemetryInterface303-10", 1533),
          ("telemetryInterface303-11", 1534),
          ("telemetryInterface303-12", 1535),
          ("telemetryInterface303-13", 1536),
          ("telemetryInterface303-14", 1537),
          ("telemetryInterface303-15", 1538),
          ("telemetryInterface303-16", 1539),
          ("telemetryInterface303-2", 1540),
          ("telemetryInterface303-3", 1541),
          ("telemetryInterface303-4", 1542),
          ("telemetryInterface303-5", 1543),
          ("telemetryInterface303-6", 1544),
          ("telemetryInterface303-7", 1545),
          ("telemetryInterface303-8", 1546),
          ("telemetryInterface303-9", 1547),
          ("telemetryInterface304-1", 1548),
          ("telemetryInterface304-10", 1549),
          ("telemetryInterface304-11", 1550),
          ("telemetryInterface304-12", 1551),
          ("telemetryInterface304-13", 1552),
          ("telemetryInterface304-14", 1553),
          ("telemetryInterface304-15", 1554),
          ("telemetryInterface304-16", 1555),
          ("telemetryInterface304-2", 1556),
          ("telemetryInterface304-3", 1557),
          ("telemetryInterface304-4", 1558),
          ("telemetryInterface304-5", 1559),
          ("telemetryInterface304-6", 1560),
          ("telemetryInterface304-7", 1561),
          ("telemetryInterface304-8", 1562),
          ("telemetryInterface304-9", 1563),
          ("telemetryInterface305-1", 1564),
          ("telemetryInterface305-10", 1565),
          ("telemetryInterface305-11", 1566),
          ("telemetryInterface305-12", 1567),
          ("telemetryInterface305-13", 1568),
          ("telemetryInterface305-14", 1569),
          ("telemetryInterface305-15", 1570),
          ("telemetryInterface305-16", 1571),
          ("telemetryInterface305-2", 1572),
          ("telemetryInterface305-3", 1573),
          ("telemetryInterface305-4", 1574),
          ("telemetryInterface305-5", 1575),
          ("telemetryInterface305-6", 1576),
          ("telemetryInterface305-7", 1577),
          ("telemetryInterface305-8", 1578),
          ("telemetryInterface305-9", 1579),
          ("telemetryInterface306-1", 1580),
          ("telemetryInterface306-10", 1581),
          ("telemetryInterface306-11", 1582),
          ("telemetryInterface306-12", 1583),
          ("telemetryInterface306-13", 1584),
          ("telemetryInterface306-14", 1585),
          ("telemetryInterface306-15", 1586),
          ("telemetryInterface306-16", 1587),
          ("telemetryInterface306-2", 1588),
          ("telemetryInterface306-3", 1589),
          ("telemetryInterface306-4", 1590),
          ("telemetryInterface306-5", 1591),
          ("telemetryInterface306-6", 1592),
          ("telemetryInterface306-7", 1593),
          ("telemetryInterface306-8", 1594),
          ("telemetryInterface306-9", 1595),
          ("telemetryInterface307-1", 1596),
          ("telemetryInterface307-10", 1597),
          ("telemetryInterface307-11", 1598),
          ("telemetryInterface307-12", 1599),
          ("telemetryInterface307-13", 1600),
          ("telemetryInterface307-14", 1601),
          ("telemetryInterface307-15", 1602),
          ("telemetryInterface307-16", 1603),
          ("telemetryInterface307-2", 1604),
          ("telemetryInterface307-3", 1605),
          ("telemetryInterface307-4", 1606),
          ("telemetryInterface307-5", 1607),
          ("telemetryInterface307-6", 1608),
          ("telemetryInterface307-7", 1609),
          ("telemetryInterface307-8", 1610),
          ("telemetryInterface307-9", 1611),
          ("telemetryInterface31", 311),
          ("telemetryInterface310-1", 1612),
          ("telemetryInterface310-10", 1613),
          ("telemetryInterface310-11", 1614),
          ("telemetryInterface310-12", 1615),
          ("telemetryInterface310-13", 1616),
          ("telemetryInterface310-14", 1617),
          ("telemetryInterface310-15", 1618),
          ("telemetryInterface310-16", 1619),
          ("telemetryInterface310-2", 1620),
          ("telemetryInterface310-3", 1621),
          ("telemetryInterface310-4", 1622),
          ("telemetryInterface310-5", 1623),
          ("telemetryInterface310-6", 1624),
          ("telemetryInterface310-7", 1625),
          ("telemetryInterface310-8", 1626),
          ("telemetryInterface310-9", 1627),
          ("telemetryInterface311-1", 1628),
          ("telemetryInterface311-10", 1629),
          ("telemetryInterface311-11", 1630),
          ("telemetryInterface311-12", 1631),
          ("telemetryInterface311-13", 1632),
          ("telemetryInterface311-14", 1633),
          ("telemetryInterface311-15", 1634),
          ("telemetryInterface311-16", 1635),
          ("telemetryInterface311-2", 1636),
          ("telemetryInterface311-3", 1637),
          ("telemetryInterface311-4", 1638),
          ("telemetryInterface311-5", 1639),
          ("telemetryInterface311-6", 1640),
          ("telemetryInterface311-7", 1641),
          ("telemetryInterface311-8", 1642),
          ("telemetryInterface311-9", 1643),
          ("telemetryInterface312-1", 1644),
          ("telemetryInterface312-10", 1645),
          ("telemetryInterface312-11", 1646),
          ("telemetryInterface312-12", 1647),
          ("telemetryInterface312-13", 1648),
          ("telemetryInterface312-14", 1649),
          ("telemetryInterface312-15", 1650),
          ("telemetryInterface312-16", 1651),
          ("telemetryInterface312-2", 1652),
          ("telemetryInterface312-3", 1653),
          ("telemetryInterface312-4", 1654),
          ("telemetryInterface312-5", 1655),
          ("telemetryInterface312-6", 1656),
          ("telemetryInterface312-7", 1657),
          ("telemetryInterface312-8", 1658),
          ("telemetryInterface312-9", 1659),
          ("telemetryInterface313-1", 1660),
          ("telemetryInterface313-10", 1661),
          ("telemetryInterface313-11", 1662),
          ("telemetryInterface313-12", 1663),
          ("telemetryInterface313-13", 1664),
          ("telemetryInterface313-14", 1665),
          ("telemetryInterface313-15", 1666),
          ("telemetryInterface313-16", 1667),
          ("telemetryInterface313-2", 1668),
          ("telemetryInterface313-3", 1669),
          ("telemetryInterface313-4", 1670),
          ("telemetryInterface313-5", 1671),
          ("telemetryInterface313-6", 1672),
          ("telemetryInterface313-7", 1673),
          ("telemetryInterface313-8", 1674),
          ("telemetryInterface313-9", 1675),
          ("telemetryInterface314-1", 1676),
          ("telemetryInterface314-10", 1677),
          ("telemetryInterface314-11", 1678),
          ("telemetryInterface314-12", 1679),
          ("telemetryInterface314-13", 1680),
          ("telemetryInterface314-14", 1681),
          ("telemetryInterface314-15", 1682),
          ("telemetryInterface314-16", 1683),
          ("telemetryInterface314-2", 1684),
          ("telemetryInterface314-3", 1685),
          ("telemetryInterface314-4", 1686),
          ("telemetryInterface314-5", 1687),
          ("telemetryInterface314-6", 1688),
          ("telemetryInterface314-7", 1689),
          ("telemetryInterface314-8", 1690),
          ("telemetryInterface314-9", 1691),
          ("telemetryInterface315-1", 1692),
          ("telemetryInterface315-10", 1693),
          ("telemetryInterface315-11", 1694),
          ("telemetryInterface315-12", 1695),
          ("telemetryInterface315-13", 1696),
          ("telemetryInterface315-14", 1697),
          ("telemetryInterface315-15", 1698),
          ("telemetryInterface315-16", 1699),
          ("telemetryInterface315-2", 1700),
          ("telemetryInterface315-3", 1701),
          ("telemetryInterface315-4", 1702),
          ("telemetryInterface315-5", 1703),
          ("telemetryInterface315-6", 1704),
          ("telemetryInterface315-7", 1705),
          ("telemetryInterface315-8", 1706),
          ("telemetryInterface315-9", 1707),
          ("telemetryInterface316-1", 1708),
          ("telemetryInterface316-10", 1709),
          ("telemetryInterface316-11", 1710),
          ("telemetryInterface316-12", 1711),
          ("telemetryInterface316-13", 1712),
          ("telemetryInterface316-14", 1713),
          ("telemetryInterface316-15", 1714),
          ("telemetryInterface316-16", 1715),
          ("telemetryInterface316-2", 1716),
          ("telemetryInterface316-3", 1717),
          ("telemetryInterface316-4", 1718),
          ("telemetryInterface316-5", 1719),
          ("telemetryInterface316-6", 1720),
          ("telemetryInterface316-7", 1721),
          ("telemetryInterface316-8", 1722),
          ("telemetryInterface316-9", 1723),
          ("telemetryInterface317-1", 1724),
          ("telemetryInterface317-10", 1725),
          ("telemetryInterface317-11", 1726),
          ("telemetryInterface317-12", 1727),
          ("telemetryInterface317-13", 1728),
          ("telemetryInterface317-14", 1729),
          ("telemetryInterface317-15", 1730),
          ("telemetryInterface317-16", 1731),
          ("telemetryInterface317-2", 1732),
          ("telemetryInterface317-3", 1733),
          ("telemetryInterface317-4", 1734),
          ("telemetryInterface317-5", 1735),
          ("telemetryInterface317-6", 1736),
          ("telemetryInterface317-7", 1737),
          ("telemetryInterface317-8", 1738),
          ("telemetryInterface317-9", 1739),
          ("telemetryInterface32", 312),
          ("telemetryInterface380-1", 1842),
          ("telemetryInterface4", 313),
          ("telemetryInterface4-1", 687),
          ("telemetryInterface4-10", 688),
          ("telemetryInterface4-11", 689),
          ("telemetryInterface4-12", 690),
          ("telemetryInterface4-13", 691),
          ("telemetryInterface4-14", 692),
          ("telemetryInterface4-15", 693),
          ("telemetryInterface4-16", 694),
          ("telemetryInterface4-2", 686),
          ("telemetryInterface4-3", 685),
          ("telemetryInterface4-4", 679),
          ("telemetryInterface4-5", 680),
          ("telemetryInterface4-6", 681),
          ("telemetryInterface4-7", 682),
          ("telemetryInterface4-8", 683),
          ("telemetryInterface4-9", 684),
          ("telemetryInterface5", 314),
          ("telemetryInterface5-1", 703),
          ("telemetryInterface5-10", 704),
          ("telemetryInterface5-11", 705),
          ("telemetryInterface5-12", 706),
          ("telemetryInterface5-13", 707),
          ("telemetryInterface5-14", 708),
          ("telemetryInterface5-15", 709),
          ("telemetryInterface5-16", 710),
          ("telemetryInterface5-2", 702),
          ("telemetryInterface5-3", 701),
          ("telemetryInterface5-4", 695),
          ("telemetryInterface5-5", 696),
          ("telemetryInterface5-6", 697),
          ("telemetryInterface5-7", 698),
          ("telemetryInterface5-8", 699),
          ("telemetryInterface5-9", 700),
          ("telemetryInterface501-1", 1740),
          ("telemetryInterface501-2", 1741),
          ("telemetryInterface511-1", 1742),
          ("telemetryInterface511-2", 1743),
          ("telemetryInterface521-1", 1744),
          ("telemetryInterface521-2", 1745),
          ("telemetryInterface531-1", 1746),
          ("telemetryInterface531-2", 1747),
          ("telemetryInterface541-1", 1748),
          ("telemetryInterface541-2", 1749),
          ("telemetryInterface551-1", 1750),
          ("telemetryInterface551-2", 1751),
          ("telemetryInterface561-1", 1752),
          ("telemetryInterface561-2", 1753),
          ("telemetryInterface571-1", 1754),
          ("telemetryInterface571-2", 1755),
          ("telemetryInterface581-1", 1756),
          ("telemetryInterface581-2", 1757),
          ("telemetryInterface591-1", 1758),
          ("telemetryInterface591-2", 1759),
          ("telemetryInterface6", 315),
          ("telemetryInterface6-1", 719),
          ("telemetryInterface6-10", 720),
          ("telemetryInterface6-11", 721),
          ("telemetryInterface6-12", 722),
          ("telemetryInterface6-13", 723),
          ("telemetryInterface6-14", 724),
          ("telemetryInterface6-15", 725),
          ("telemetryInterface6-16", 726),
          ("telemetryInterface6-2", 718),
          ("telemetryInterface6-3", 717),
          ("telemetryInterface6-4", 711),
          ("telemetryInterface6-5", 712),
          ("telemetryInterface6-6", 713),
          ("telemetryInterface6-7", 714),
          ("telemetryInterface6-8", 715),
          ("telemetryInterface6-9", 716),
          ("telemetryInterface601-1", 1760),
          ("telemetryInterface601-2", 1761),
          ("telemetryInterface611-1", 1762),
          ("telemetryInterface611-2", 1763),
          ("telemetryInterface621-1", 1764),
          ("telemetryInterface621-2", 1765),
          ("telemetryInterface631-1", 1766),
          ("telemetryInterface631-2", 1767),
          ("telemetryInterface641-1", 1768),
          ("telemetryInterface641-2", 1769),
          ("telemetryInterface651-1", 1770),
          ("telemetryInterface651-2", 1771),
          ("telemetryInterface661-1", 1772),
          ("telemetryInterface661-2", 1773),
          ("telemetryInterface671-1", 1774),
          ("telemetryInterface671-2", 1775),
          ("telemetryInterface681-1", 1776),
          ("telemetryInterface681-2", 1777),
          ("telemetryInterface691-1", 1778),
          ("telemetryInterface691-2", 1779),
          ("telemetryInterface7", 316),
          ("telemetryInterface7-1", 735),
          ("telemetryInterface7-10", 736),
          ("telemetryInterface7-11", 737),
          ("telemetryInterface7-12", 738),
          ("telemetryInterface7-13", 739),
          ("telemetryInterface7-14", 740),
          ("telemetryInterface7-15", 741),
          ("telemetryInterface7-16", 742),
          ("telemetryInterface7-2", 734),
          ("telemetryInterface7-3", 733),
          ("telemetryInterface7-4", 727),
          ("telemetryInterface7-5", 728),
          ("telemetryInterface7-6", 729),
          ("telemetryInterface7-7", 730),
          ("telemetryInterface7-8", 731),
          ("telemetryInterface7-9", 732),
          ("telemetryInterface8", 317),
          ("telemetryInterface9", 318),
          ("tellabsAGCoutOfGain", 9883),
          ("tellabsAISPath", 9431),
          ("tellabsAdminUnitAlarmIndicationSignal", 9394),
          ("tellabsAdminUnitLossOfPointer", 9393),
          ("tellabsAggOutputPowerExceeded", 9914),
          ("tellabsAlarmIndicationPanel", 9882),
          ("tellabsAutoPowerMgmtProgress", 9915),
          ("tellabsBersdPath", 9432),
          ("tellabsBersfPath", 9433),
          ("tellabsCablePLos", 9920),
          ("tellabsCablePLosDwdmInterface", 9921),
          ("tellabsCablePLosExpressInterface", 9922),
          ("tellabsCablePLosMidStageAccess", 9923),
          ("tellabsCablePLosPortInterface", 9924),
          ("tellabsControlBusFailureAIPSPI", 9888),
          ("tellabsControlBusFailureBCKPLNSPI", 9886),
          ("tellabsControlBusFailureIDSPI", 9885),
          ("tellabsControlBusFailureJTAG", 9884),
          ("tellabsControlBusFailureTDM", 9887),
          ("tellabsControlandTimCommFail", 9889),
          ("tellabsEthernetBersd", 9400),
          ("tellabsEthernetBersf", 9401),
          ("tellabsEthernetLinkFlap", 9402),
          ("tellabsEthernetRcvPlc", 9406),
          ("tellabsEthernetRcvTlc", 9407),
          ("tellabsEthernetRdi", 9403),
          ("tellabsEvcLoop", 9408),
          ("tellabsFabricDegrade", 9945),
          ("tellabsFabricFailure", 9946),
          ("tellabsFacilityLoopback", 9930),
          ("tellabsFacilityNotSupported", 9928),
          ("tellabsFansRunningHighSpeed", 9891),
          ("tellabsFiberMismatch", 9927),
          ("tellabsHOPathBersd", 9395),
          ("tellabsHOPathBersf", 9396),
          ("tellabsHOPathPlm", 9397),
          ("tellabsHOPathRfi", 9398),
          ("tellabsHOPathUneq", 9399),
          ("tellabsHighSpeedFan", 9427),
          ("tellabsHoldoverSynchMode", 9892),
          ("tellabsIDPromFailure", 9893),
          ("tellabsInhAlm", 9428),
          ("tellabsLayer2ResLow", 9391),
          ("tellabsLayer2ResUnavail", 9392),
          ("tellabsLopPath", 9434),
          ("tellabsLosExpressInterface", 9929),
          ("tellabsLossSynchBetweenSpms", 9890),
          ("tellabsMismatchofEquipment", 9894),
          ("tellabsMismatchofEquipmentHwVerMismatch", 9895),
          ("tellabsNetEquipmentInterconnectionFail", 9896),
          ("tellabsNoAirFilter", 9937),
          ("tellabsOpticalPowerOverload", 9910),
          ("tellabsOpticalPowerTargetUnreachable", 9909),
          ("tellabsPlmPath", 9435),
          ("tellabsPowerFeedA1Problem", 9898),
          ("tellabsPowerFeedA2Problem", 9938),
          ("tellabsPowerFeedA3Problem", 9939),
          ("tellabsPowerFeedAProblem", 9897),
          ("tellabsPowerFeedB1Problem", 9900),
          ("tellabsPowerFeedB2Problem", 9940),
          ("tellabsPowerFeedB3Problem", 9941),
          ("tellabsPowerFeedBProblem", 9899),
          ("tellabsPowerFuseProblemA", 9424),
          ("tellabsPowerFuseProblemB", 9425),
          ("tellabsPowerORFilterProblem", 9901),
          ("tellabsProprietaryAis", 9935),
          ("tellabsProtectionNotAvailable", 9933),
          ("tellabsRemoteLinkFailure", 9451),
          ("tellabsReplaceableUnitMissing", 9902),
          ("tellabsReplaceableUnitProblemDeg", 9903),
          ("tellabsReplaceableUnitProblemFail", 9904),
          ("tellabsRfiPath", 9436),
          ("tellabsShNumberIncorrect", 9426),
          ("tellabsSwBootAbnormal", 9905),
          ("tellabsTerminalLoopback", 9931),
          ("tellabsThermalProblem", 9906),
          ("tellabsThermalProblemNano", 9430),
          ("tellabsThermalProblemPico", 9454),
          ("tellabsThermalProblemUSS", 9429),
          ("tellabsUnequippedPath", 9437),
          ("tempProblemMajor", 2157),
          ("tempSafetyShutdown", 2028),
          ("temperaturRegulationRunning", 808),
          ("temperatureFail", 484),
          ("temperatureHigh", 319),
          ("temperatureProblem", 433),
          ("temperatureProblem1", 800),
          ("temperatureProblem2", 801),
          ("temperatureProblem3", 802),
          ("temperatureProblem4", 803),
          ("temperatureProblemMajor", 3418),
          ("temperatureProblemMinor", 3414),
          ("temperatureProblemTSCh1", 1073),
          ("temperatureProblemTSCh2", 1074),
          ("temperatureProblemTSCh3", 1075),
          ("temperatureProblemTSCh4", 1076),
          ("temperatureProblemVOA", 1096),
          ("temperatureTooHigh", 464),
          ("temperatureTooHighCritical", 1967),
          ("temperatureTooHighLine", 1867),
          ("temperatureTooHighTrib1", 1868),
          ("temperatureTooHighTrib2", 1869),
          ("temperatureTooHighTrib3", 1870),
          ("temperatureTooHighTrib4", 1871),
          ("temperatureTooLow", 482),
          ("test", 320),
          ("testFailed", 4533),
          ("testFailure", 1031),
          ("testalarm", 3977),
          ("testloop4b", 968),
          ("thres15MinExceededBbePcs", 9877),
          ("thres15MinExceededBbePcsRzs", 9879),
          ("thres15MinExceededFecBERCE", 3564),
          ("thres15MinExceededFecCE", 3331),
          ("thres15MinExceededFecES", 3333),
          ("thres15MinExceededFecSES", 3334),
          ("thres15MinExceededFecUBE", 3332),
          ("thres15MinExceededGfpCHEC", 3337),
          ("thres15MinExceededGfpTHEC", 3338),
          ("thres15MinExceededGfpTHecDisc", 3339),
          ("thres15MinExceededGfpTsuperblockDisc", 3340),
          ("thres15MinExceededMuxES", 3335),
          ("thres15MinExceededMuxSES", 3336),
          ("thres15MinExceededOduBBE", 3392),
          ("thres15MinExceededOduES", 3389),
          ("thres15MinExceededOduSES", 3390),
          ("thres15MinExceededOduTcmABBE", 3376),
          ("thres15MinExceededOduTcmAES", 3373),
          ("thres15MinExceededOduTcmASES", 3374),
          ("thres15MinExceededOduTcmAUAS", 3375),
          ("thres15MinExceededOduTcmBBBE", 3380),
          ("thres15MinExceededOduTcmBES", 3377),
          ("thres15MinExceededOduTcmBSES", 3378),
          ("thres15MinExceededOduTcmBUAS", 3379),
          ("thres15MinExceededOduTcmCBBE", 3384),
          ("thres15MinExceededOduTcmCES", 3381),
          ("thres15MinExceededOduTcmCSES", 3382),
          ("thres15MinExceededOduTcmCUAS", 3383),
          ("thres15MinExceededOduUAS", 3391),
          ("thres15MinExceededOtuBBE", 3388),
          ("thres15MinExceededOtuES", 3385),
          ("thres15MinExceededOtuSES", 3386),
          ("thres15MinExceededOtuUAS", 3387),
          ("thres15MinExceededPhysConvCVTX", 3614),
          ("thres15MinExceededPhysConvESTX", 3613),
          ("thres15MinExceededPhysConvSE", 3612),
          ("thres15MinExceededPhysConvSETX", 3615),
          ("thres15MinExceededSonetLineCV", 3371),
          ("thres15MinExceededSonetLineES", 3369),
          ("thres15MinExceededSonetLineSES", 3370),
          ("thres15MinExceededSonetLineUAS", 3372),
          ("thres15MinExceededSonetSectCV", 3368),
          ("thres15MinExceededSonetSectES", 3365),
          ("thres15MinExceededSonetSectSEFS", 3367),
          ("thres15MinExceededSonetSectSES", 3366),
          ("thresOptPowerCtrlFailureHigh", 3394),
          ("thresOptPowerCtrlFailureLow", 3393),
          ("thresholdAttenuation", 771),
          ("thresholdBBEHP15", 9409),
          ("thresholdBBEHP24", 9410),
          ("thresholdBBEMS15", 9362),
          ("thresholdBBEMS24", 9363),
          ("thresholdBBERS15", 9354),
          ("thresholdBBERS24", 9355),
          ("thresholdBCPKT15", 9276),
          ("thresholdBCPKT24", 9277),
          ("thresholdBEFEC15", 9278),
          ("thresholdBEFEC24", 9279),
          ("thresholdBERFEC15", 9280),
          ("thresholdBERFEC24", 9281),
          ("thresholdBERavg15", 7883),
          ("thresholdBERavg15FarEnd", 7884),
          ("thresholdBERavg24", 7885),
          ("thresholdBERavg24FarEnd", 7886),
          ("thresholdBSMinus15", 1846),
          ("thresholdBSMinus24", 1847),
          ("thresholdBSPlus15", 1844),
          ("thresholdBSPlus24", 1845),
          ("thresholdBadFramesRx15", 7851),
          ("thresholdBadFramesRx15FarEnd", 7852),
          ("thresholdBadFramesRx24", 7853),
          ("thresholdBadFramesRx24FarEnd", 7854),
          ("thresholdBadFramesTx15", 7855),
          ("thresholdBadFramesTx15FarEnd", 7856),
          ("thresholdBadFramesTx24", 7857),
          ("thresholdBadFramesTx24FarEnd", 7858),
          ("thresholdBadGFPSuperblocks15", 7875),
          ("thresholdBadGFPSuperblocks15FarEnd", 7876),
          ("thresholdBadGFPSuperblocks24", 7877),
          ("thresholdBadGFPSuperblocks24FarEnd", 7878),
          ("thresholdBbe15", 321),
          ("thresholdBbe15EgressFarEnd", 4803),
          ("thresholdBbe15EgressNearEnd", 4802),
          ("thresholdBbe15FarEnd", 322),
          ("thresholdBbe15IngressFarEnd", 4801),
          ("thresholdBbe15IngressNearEnd", 4800),
          ("thresholdBbe24", 323),
          ("thresholdBbe24EgressFarEnd", 4807),
          ("thresholdBbe24EgressNearEnd", 4806),
          ("thresholdBbe24FarEnd", 324),
          ("thresholdBbe24IngressFarEnd", 4805),
          ("thresholdBbe24IngressNearEnd", 4804),
          ("thresholdBbeAsap", 1066),
          ("thresholdBbeFarEndAsap", 1067),
          ("thresholdBbeOutAsap", 1068),
          ("thresholdCDHT15", 9462),
          ("thresholdCDHT24", 9464),
          ("thresholdCDLT15", 9461),
          ("thresholdCDLT24", 9463),
          ("thresholdCRCAE15", 9282),
          ("thresholdCRCAE24", 9283),
          ("thresholdCVDE15", 7847),
          ("thresholdCVDE15FarEnd", 7848),
          ("thresholdCVDE24", 7849),
          ("thresholdCVDE24FarEnd", 7850),
          ("thresholdCVL15", 9364),
          ("thresholdCVL24", 9365),
          ("thresholdCVOTU15", 9284),
          ("thresholdCVOTU24", 9285),
          ("thresholdCVP15", 9438),
          ("thresholdCVP24", 9439),
          ("thresholdCVS15", 9286),
          ("thresholdCVS24", 9287),
          ("thresholdCbes15", 466),
          ("thresholdCbes24", 467),
          ("thresholdCbesAsap", 1054),
          ("thresholdCrossed", 4504),
          ("thresholdCv15", 325),
          ("thresholdCv15FarEnd", 476),
          ("thresholdCv24", 326),
          ("thresholdCv24FarEnd", 477),
          ("thresholdCvAsap", 1050),
          ("thresholdCvFarEndAsap", 1059),
          ("thresholdCvOutAsap", 1058),
          ("thresholdDELAYODUHT15", 9288),
          ("thresholdDELAYODUHT24", 9289),
          ("thresholdDELAYODULT15", 9290),
          ("thresholdDELAYODULT24", 9291),
          ("thresholdDELAYODUTHT15", 9292),
          ("thresholdDELAYODUTHT24", 9293),
          ("thresholdDELAYODUTLT15", 9294),
          ("thresholdDELAYODUTLT24", 9295),
          ("thresholdDGDHT15", 9296),
          ("thresholdDGDHT24", 9297),
          ("thresholdDROP15", 9298),
          ("thresholdDROP24", 9299),
          ("thresholdDf15", 9543),
          ("thresholdDf24", 9544),
          ("thresholdDfAsap", 9546),
          ("thresholdDiscardedGFPframes15", 7879),
          ("thresholdDiscardedGFPframes15FarEnd", 7880),
          ("thresholdDiscardedGFPframes24", 7881),
          ("thresholdDiscardedGFPframes24FarEnd", 7882),
          ("thresholdDm", 9547),
          ("thresholdDmAsap", 9549),
          ("thresholdEBODU15", 9300),
          ("thresholdEBODU24", 9301),
          ("thresholdEBODUT15", 9302),
          ("thresholdEBODUT24", 9303),
          ("thresholdEBOTU15", 9304),
          ("thresholdEBOTU24", 9305),
          ("thresholdESHP15", 9411),
          ("thresholdESHP24", 9412),
          ("thresholdESL15", 9366),
          ("thresholdESL24", 9367),
          ("thresholdESMS15", 9368),
          ("thresholdESMS24", 9369),
          ("thresholdESODU15", 9306),
          ("thresholdESODU24", 9307),
          ("thresholdESODUT15", 9308),
          ("thresholdESODUT24", 9309),
          ("thresholdESOTU15", 9310),
          ("thresholdESOTU24", 9311),
          ("thresholdESP15", 9440),
          ("thresholdESP24", 9441),
          ("thresholdESRS15", 9356),
          ("thresholdESRS24", 9357),
          ("thresholdESS15", 9312),
          ("thresholdESS24", 9313),
          ("thresholdEs15", 327),
          ("thresholdEs15EgressFarEnd", 4811),
          ("thresholdEs15EgressNearEnd", 4810),
          ("thresholdEs15FarEnd", 328),
          ("thresholdEs15IngressFarEnd", 4809),
          ("thresholdEs15IngressNearEnd", 4808),
          ("thresholdEs24", 329),
          ("thresholdEs24EgressFarEnd", 4815),
          ("thresholdEs24EgressNearEnd", 4814),
          ("thresholdEs24FarEnd", 330),
          ("thresholdEs24IngressFarEnd", 4813),
          ("thresholdEs24IngressNearEnd", 4812),
          ("thresholdEsAsap", 1051),
          ("thresholdEsFarEndAsap", 1056),
          ("thresholdEsOutAsap", 1061),
          ("thresholdFCHP15", 9415),
          ("thresholdFCHP24", 9416),
          ("thresholdFCL15", 9370),
          ("thresholdFCL24", 9371),
          ("thresholdFCMS15", 9372),
          ("thresholdFCMS24", 9373),
          ("thresholdFCP15", 9444),
          ("thresholdFCP24", 9445),
          ("thresholdFCSErrorsRx15", 4529),
          ("thresholdFCSErrorsRx24", 4530),
          ("thresholdFCSErrorsTx15", 4531),
          ("thresholdFCSErrorsTx24", 4532),
          ("thresholdFRAG15", 9314),
          ("thresholdFRAG24", 9315),
          ("thresholdFcse15", 9541),
          ("thresholdFcse24", 9542),
          ("thresholdFcseAsap", 9545),
          ("thresholdGoodFramesRx15", 7859),
          ("thresholdGoodFramesRx15FarEnd", 7860),
          ("thresholdGoodFramesRx24", 7861),
          ("thresholdGoodFramesRx24FarEnd", 7862),
          ("thresholdGoodFramesTx15", 7863),
          ("thresholdGoodFramesTx15FarEnd", 7864),
          ("thresholdGoodFramesTx24", 7865),
          ("thresholdGoodFramesTx24FarEnd", 7866),
          ("thresholdGoodOctetsRx15", 7867),
          ("thresholdGoodOctetsRx15FarEnd", 7868),
          ("thresholdGoodOctetsRx24", 7869),
          ("thresholdGoodOctetsRx24FarEnd", 7870),
          ("thresholdGoodOctetsTx15", 7871),
          ("thresholdGoodOctetsTx15FarEnd", 7872),
          ("thresholdGoodOctetsTx24", 7873),
          ("thresholdGoodOctetsTx24FarEnd", 7874),
          ("thresholdHighCurrent", 537),
          ("thresholdHighOIP", 542),
          ("thresholdHighOOP", 546),
          ("thresholdHighTemp", 551),
          ("thresholdHighVolt", 555),
          ("thresholdHighestBbe15", 6814),
          ("thresholdHighestBbe15FarEnd", 6815),
          ("thresholdHighestBbe24", 6816),
          ("thresholdHighestBbe24FarEnd", 6817),
          ("thresholdHighestCurrent", 538),
          ("thresholdHighestCv15", 6830),
          ("thresholdHighestCv15FarEnd", 6831),
          ("thresholdHighestCv24", 6832),
          ("thresholdHighestCv24FarEnd", 6833),
          ("thresholdHighestEs15", 6818),
          ("thresholdHighestEs15FarEnd", 6819),
          ("thresholdHighestEs24", 6820),
          ("thresholdHighestEs24FarEnd", 6821),
          ("thresholdHighestOIP", 541),
          ("thresholdHighestOOP", 545),
          ("thresholdHighestSefs15", 6834),
          ("thresholdHighestSefs15FarEnd", 6835),
          ("thresholdHighestSefs24", 6836),
          ("thresholdHighestSefs24FarEnd", 6837),
          ("thresholdHighestSes15", 6822),
          ("thresholdHighestSes15FarEnd", 6823),
          ("thresholdHighestSes24", 6824),
          ("thresholdHighestSes24FarEnd", 6825),
          ("thresholdHighestTemp", 550),
          ("thresholdHighestUas15", 6826),
          ("thresholdHighestUas15FarEnd", 6827),
          ("thresholdHighestUas24", 6828),
          ("thresholdHighestUas24FarEnd", 6829),
          ("thresholdHighestVolt", 554),
          ("thresholdJABR15", 9316),
          ("thresholdJABR24", 9317),
          ("thresholdLBCHT15", 9374),
          ("thresholdLBCHT24", 9375),
          ("thresholdLBCLT15", 9376),
          ("thresholdLBCLT24", 9377),
          ("thresholdLOSS15", 9318),
          ("thresholdLOSS24", 9319),
          ("thresholdLTHT15", 9378),
          ("thresholdLTHT24", 9379),
          ("thresholdLTLT15", 9380),
          ("thresholdLTLT24", 9381),
          ("thresholdLowCurrent", 536),
          ("thresholdLowOIP", 540),
          ("thresholdLowOOP", 544),
          ("thresholdLowTemp", 549),
          ("thresholdLowVolt", 553),
          ("thresholdLowestCurrent", 535),
          ("thresholdLowestOIP", 539),
          ("thresholdLowestOOP", 543),
          ("thresholdLowestTemp", 548),
          ("thresholdLowestVolt", 552),
          ("thresholdMCPKT15", 9320),
          ("thresholdMCPKT24", 9321),
          ("thresholdMaxBER15FarEnd", 7887),
          ("thresholdMaxBER24FarEnd", 7888),
          ("thresholdMaxBer15", 750),
          ("thresholdMaxBer24", 751),
          ("thresholdMaxBerAsap", 1065),
          ("thresholdMaxDM15", 4512),
          ("thresholdMaxDM24", 4513),
          ("thresholdMaxDm", 9548),
          ("thresholdMaxDmAsap", 9550),
          ("thresholdMaxInputSpanLoss15", 3493),
          ("thresholdMaxInputSpanLoss24", 3494),
          ("thresholdOCTETS15", 10002),
          ("thresholdOCTETS24", 10003),
          ("thresholdOFRHT15", 10055),
          ("thresholdOFRHT24", 10056),
          ("thresholdOFRLT15", 10057),
          ("thresholdOFRLT24", 10058),
          ("thresholdOFSRS15", 9358),
          ("thresholdOFSRS24", 9359),
          ("thresholdOFTHT15", 10051),
          ("thresholdOFTHT24", 10052),
          ("thresholdOFTLT15", 10053),
          ("thresholdOFTLT24", 10054),
          ("thresholdOPRHT15", 9322),
          ("thresholdOPRHT24", 9323),
          ("thresholdOPRLT15", 9324),
          ("thresholdOPRLT24", 9325),
          ("thresholdOPTHT15", 10004),
          ("thresholdOPTHT24", 10005),
          ("thresholdOPTLT15", 10006),
          ("thresholdOPTLT24", 10007),
          ("thresholdOSNRLT15", 9465),
          ("thresholdOSNRLT24", 9466),
          ("thresholdOSPKT15", 9326),
          ("thresholdOSPKT24", 9327),
          ("thresholdOfs15", 331),
          ("thresholdOfs24", 332),
          ("thresholdPDLHT15", 10008),
          ("thresholdPDLHT24", 10009),
          ("thresholdPJCDIFFP15", 9418),
          ("thresholdPJCDIFFP24", 9419),
          ("thresholdPJCSPDET15", 9420),
          ("thresholdPJCSPDET24", 9421),
          ("thresholdPJCSPGEN15", 9422),
          ("thresholdPJCSPGEN24", 9423),
          ("thresholdPKT15", 9328),
          ("thresholdPKT24", 9329),
          ("thresholdPKTS1024TO1518OCTETS15", 10010),
          ("thresholdPKTS1024TO1518OCTETS24", 10011),
          ("thresholdPKTS128TO255OCTETS15", 10012),
          ("thresholdPKTS128TO255OCTETS24", 10013),
          ("thresholdPKTS256TO511OCTETS15", 10014),
          ("thresholdPKTS256TO511OCTETS24", 10015),
          ("thresholdPKTS512TO1023OCTETS15", 10016),
          ("thresholdPKTS512TO1023OCTETS24", 10017),
          ("thresholdPKTS64OCTETS15", 10018),
          ("thresholdPKTS64OCTETS24", 10019),
          ("thresholdPKTS65TO127OCTETS15", 10020),
          ("thresholdPKTS65TO127OCTETS24", 10021),
          ("thresholdPLavg15", 7889),
          ("thresholdPLavg15FarEnd", 7890),
          ("thresholdPLavg24", 7891),
          ("thresholdPLavg24FarEnd", 7892),
          ("thresholdPLmax15", 7893),
          ("thresholdPLmax15FarEnd", 7894),
          ("thresholdPLmax24", 7895),
          ("thresholdPLmax24FarEnd", 7896),
          ("thresholdPLmin15", 7897),
          ("thresholdPLmin15FarEnd", 7898),
          ("thresholdPLmin24", 7899),
          ("thresholdPLmin24FarEnd", 7900),
          ("thresholdPjeMinus15", 335),
          ("thresholdPjeMinus24", 336),
          ("thresholdPjePlus15", 333),
          ("thresholdPjePlus24", 334),
          ("thresholdPsw", 394),
          ("thresholdQFACTORLT15", 10022),
          ("thresholdQFACTORLT24", 10023),
          ("thresholdSE15", 9330),
          ("thresholdSE24", 9331),
          ("thresholdSEFSS15", 9332),
          ("thresholdSEFSS24", 9333),
          ("thresholdSESHP15", 9413),
          ("thresholdSESHP24", 9414),
          ("thresholdSESL15", 9388),
          ("thresholdSESL24", 9389),
          ("thresholdSESMS15", 9382),
          ("thresholdSESMS24", 9383),
          ("thresholdSESODU15", 9334),
          ("thresholdSESODU24", 9335),
          ("thresholdSESODUT15", 9336),
          ("thresholdSESODUT24", 9337),
          ("thresholdSESOTU15", 9338),
          ("thresholdSESOTU24", 9339),
          ("thresholdSESP15", 9442),
          ("thresholdSESP24", 9443),
          ("thresholdSESRS15", 9360),
          ("thresholdSESRS24", 9361),
          ("thresholdSESS15", 9340),
          ("thresholdSESS24", 9341),
          ("thresholdSNR", 772),
          ("thresholdSefs15", 337),
          ("thresholdSefs15FarEnd", 478),
          ("thresholdSefs24", 338),
          ("thresholdSefs24FarEnd", 479),
          ("thresholdSefsAsap", 1053),
          ("thresholdSefsOutAsap", 1064),
          ("thresholdSes15", 339),
          ("thresholdSes15EgressFarEnd", 4819),
          ("thresholdSes15EgressNearEnd", 4818),
          ("thresholdSes15FarEnd", 340),
          ("thresholdSes15IngressFarEnd", 4817),
          ("thresholdSes15IngressNearEnd", 4816),
          ("thresholdSes24", 341),
          ("thresholdSes24EgressFarEnd", 4823),
          ("thresholdSes24EgressNearEnd", 4822),
          ("thresholdSes24FarEnd", 342),
          ("thresholdSes24IngressFarEnd", 4821),
          ("thresholdSes24IngressNearEnd", 4820),
          ("thresholdSesAsap", 1052),
          ("thresholdSesFarEndAsap", 1057),
          ("thresholdSesOutAsap", 1062),
          ("thresholdUASHP15", 9417),
          ("thresholdUASL15", 9384),
          ("thresholdUASL24", 9385),
          ("thresholdUASMS15", 9386),
          ("thresholdUASMS24", 9387),
          ("thresholdUASODU15", 9342),
          ("thresholdUASODU24", 9343),
          ("thresholdUASODUT15", 9344),
          ("thresholdUASODUT24", 9345),
          ("thresholdUASOTU15", 9346),
          ("thresholdUASOTU24", 9347),
          ("thresholdUASP15", 9446),
          ("thresholdUASP24", 9447),
          ("thresholdUBEFEC15", 9348),
          ("thresholdUBEFEC24", 9349),
          ("thresholdUSPKT15", 9350),
          ("thresholdUSPKT24", 9351),
          ("thresholdUTILHT15", 9352),
          ("thresholdUTILHT24", 9353),
          ("thresholdUas15", 343),
          ("thresholdUas15EgressFarEnd", 4827),
          ("thresholdUas15EgressNearEnd", 4826),
          ("thresholdUas15FarEnd", 344),
          ("thresholdUas15IngressFarEnd", 4825),
          ("thresholdUas15IngressNearEnd", 4824),
          ("thresholdUas24", 345),
          ("thresholdUas24EgressFarEnd", 4831),
          ("thresholdUas24EgressNearEnd", 4830),
          ("thresholdUas24FarEnd", 346),
          ("thresholdUas24IngressFarEnd", 4829),
          ("thresholdUas24IngressNearEnd", 4828),
          ("thresholdUasAsap", 1055),
          ("thresholdUasFarEndAsap", 1060),
          ("thresholdUasOutAsap", 1063),
          ("thresholdUat", 347),
          ("thresholdUatFarEnd", 348),
          ("tifSensorActive", 7846),
          ("tiltControlFailure", 434),
          ("timRf", 6372),
          ("timTributary", 6373),
          ("timeTickProblem", 349),
          ("timing", 350),
          ("timingClockNotEnabled", 6797),
          ("timingControllerFreeRun", 6798),
          ("timingControllerHoldover", 6799),
          ("timingModuleLossOfLock", 6800),
          ("timingProblem", 351),
          ("timingReferenceDegrade", 2073),
          ("timingReferenceFailure", 1818),
          ("tl1NotificationQueueOverflow", 3479),
          ("tlFire", 9229),
          ("tlFlood", 9230),
          ("tlHighWater", 9239),
          ("tlLowCablePressure", 9245),
          ("tlLowFuel", 9243),
          ("tlLowWater", 9247),
          ("tlSmoke", 9271),
          ("tlToxicGas", 9273),
          ("tlabElpsConfigurationMismatchNotif", 9481),
          ("tlabElpsFailureOfProtocolNotif", 9484),
          ("tlabElpsLackOfResponseNotif", 9482),
          ("tlabElpsProtectionGroupFailedNotif", 9483),
          ("tlabElpsProtectionTypeMismatchNotif", 9480),
          ("tlabLAGInterfaceFailureNotif", 9470),
          ("tlabMACLOSNotif", 9473),
          ("tlabMACLOSSYNCNotif", 9472),
          ("tlabMACPortLinkFlappingNotif", 9467),
          ("tlabMACSDNotif", 9468),
          ("tlabMACSFNotif", 9469),
          ("tlabMACTRDIENotif", 9471),
          ("tlabMIEcfmdot1agErrorCCMNotif", 9477),
          ("tlabMIEcfmdot1agRDICCMNotif", 9475),
          ("tlabMIEcfmdot1agRemoteMepCCMNotif", 9476),
          ("tlabMIEcfmdot1agXconCCMNotif", 9478),
          ("tlabPktTpOamMepLDINotif", 9608),
          ("tlabPktTpOamMepLOCNotif", 9609),
          ("tlabPktTpOamMepMCNotif", 9610),
          ("tlabPktTpOamMepRDINotif", 9611),
          ("tlabPktTpOamMepUNPNotif", 9612),
          ("tlcr", 1785),
          ("tlct", 1784),
          ("tma1", 352),
          ("tma2", 353),
          ("tod-traceable-status", 9843),
          ("topologyDataCalculationInProgres", 3089),
          ("topologyDataInvalid", 3090),
          ("totalLossOfCapacity", 9607),
          ("toxicGas", 354),
          ("traceIdentifierMismatchOdu", 3169),
          ("traceIdentifierMismatchOduTcmA", 3170),
          ("traceIdentifierMismatchOduTcmB", 3171),
          ("traceIdentifierMismatchOduTcmC", 3172),
          ("traceIdentifierMismatchOtu", 3168),
          ("trafficfail", 3983),
          ("transactionLogMemoryThresholdCrossed", 6555),
          ("transmitDegradeAdd", 4539),
          ("transmitDegradeBooster1", 355),
          ("transmitDegradeBooster2", 356),
          ("transmitDegradeDrop", 4540),
          ("transmitDegradeOSC1", 456),
          ("transmitDegradeOSC2", 457),
          ("transmitDegradePreamp1", 357),
          ("transmitDegradePreamp2", 358),
          ("transmitDegradePreamp3", 388),
          ("transmitDegradePreamp4", 389),
          ("transmitDegradePump1", 422),
          ("transmitDegradePump2", 424),
          ("transmitDegradePump3", 426),
          ("transmitDegradePump4", 428),
          ("transmitDegradePump5", 430),
          ("transmitDegradeTSCh1", 1069),
          ("transmitDegradeTSCh2", 1070),
          ("transmitDegradeTSCh3", 1071),
          ("transmitDegradeTSCh4", 1072),
          ("transmitFailAdd", 4541),
          ("transmitFailBooster", 435),
          ("transmitFailDrop", 4542),
          ("transmitFailPreamp", 359),
          ("transmitFailPump1", 423),
          ("transmitFailPump2", 425),
          ("transmitFailPump3", 427),
          ("transmitFailPump4", 429),
          ("transmitFailPump5", 431),
          ("transmitFailTSCh1", 1077),
          ("transmitFailTSCh2", 1078),
          ("transmitFailTSCh3", 1079),
          ("transmitFailTSCh4", 1080),
          ("transmitPowerOutRange", 6744),
          ("transmitterDisabledEpc", 3329),
          ("trapComLost", 1016),
          ("tributary10Hdb3ViolationDetection", 6374),
          ("tributary10InputFailure", 6375),
          ("tributary10OutputFailure", 6376),
          ("tributary11Hdb3ViolationDetection", 6377),
          ("tributary11InputFailure", 6378),
          ("tributary11OutputFailure", 6379),
          ("tributary12Hdb3ViolationDetection", 6380),
          ("tributary12InputFailure", 6381),
          ("tributary12OutputFailure", 6382),
          ("tributary13Hdb3ViolationDetection", 6383),
          ("tributary13InputFailure", 6384),
          ("tributary13OutputFailure", 6385),
          ("tributary14Hdb3ViolationDetection", 6386),
          ("tributary14InputFailure", 6387),
          ("tributary14OutputFailure", 6388),
          ("tributary15Hdb3ViolationDetection", 6389),
          ("tributary15InputFailure", 6390),
          ("tributary15OutputFailure", 6391),
          ("tributary16Hdb3ViolationDetection", 6392),
          ("tributary16InputFailure", 6393),
          ("tributary16OutputFailure", 6394),
          ("tributary1Dccr", 6395),
          ("tributary1Hdb3ViolationDetection", 6396),
          ("tributary1InputFailure", 6397),
          ("tributary1OutputFailure", 6398),
          ("tributary1SyncSourceOn", 6399),
          ("tributary2Dccr", 6400),
          ("tributary2Hdb3ViolationDetection", 6401),
          ("tributary2InputFailure", 6402),
          ("tributary2OutputFailure", 6403),
          ("tributary2SyncSourceOn", 6404),
          ("tributary3Dccr", 6405),
          ("tributary3Hdb3ViolationDetection", 6406),
          ("tributary3InputFailure", 6407),
          ("tributary3OutputFailure", 6408),
          ("tributary3SyncSourceOn", 6409),
          ("tributary4Dccr", 6411),
          ("tributary4Hdb3ViolationDetection", 6412),
          ("tributary4InputFailure", 6413),
          ("tributary4OutputFailure", 6414),
          ("tributary4SyncSourceOn", 6410),
          ("tributary5Hdb3ViolationDetection", 6415),
          ("tributary5InputFailure", 6416),
          ("tributary5OutputFailure", 6417),
          ("tributary6Hdb3ViolationDetection", 6418),
          ("tributary6InputFailure", 6419),
          ("tributary6OutputFailure", 6420),
          ("tributary7Hdb3ViolationDetection", 6421),
          ("tributary7InputFailure", 6422),
          ("tributary7OutputFailure", 6423),
          ("tributary8Hdb3ViolationDetection", 6424),
          ("tributary8InputFailure", 6425),
          ("tributary8OutputFailure", 6426),
          ("tributary9Hdb3ViolationDetection", 6427),
          ("tributary9InputFailure", 6428),
          ("tributary9OutputFailure", 6429),
          ("tributaryADccr", 6430),
          ("tributaryAisInserted", 6431),
          ("tributaryBDccr", 6432),
          ("tributaryCDccr", 6433),
          ("tributaryConfiguration", 6434),
          ("tributaryDDccr", 6437),
          ("tributaryDccm", 6435),
          ("tributaryDccr", 6436),
          ("tributaryOccDccr", 6438),
          ("tributaryOccSyncSourceOn", 6439),
          ("tributarySwitch", 6440),
          ("tributarySyncLos", 6441),
          ("tributarySyncSourceOn", 6442),
          ("trunkDown", 6648),
          ("tsb", 360),
          ("tuAlarmIndicationSignal", 8005),
          ("tuLossOfMultiframe", 8038),
          ("tuLossOfPointer", 8041),
          ("tuningVoltageLevelClock", 6801),
          ("twoTimingMasters", 994),
          ("tx1PowerSupply", 6444),
          ("tx1ewPowerSupply", 6443),
          ("tx1wePowerSupply", 6445),
          ("tx2PowerSupply", 6447),
          ("tx2ewPowerSupply", 6446),
          ("tx2wePowerSupply", 6448),
          ("tx3PowerSupply", 6450),
          ("tx3ewPowerSupply", 6449),
          ("tx3wePowerSupply", 6451),
          ("tx4PowerSupply", 6453),
          ("tx4ewPowerSupply", 6452),
          ("tx4wePowerSupply", 6454),
          ("tx5PowerSupply", 6456),
          ("tx5ewPowerSupply", 6455),
          ("tx5wePowerSupply", 6457),
          ("tx6PowerSupply", 6459),
          ("tx6ewPowerSupply", 6458),
          ("tx6wePowerSupply", 6460),
          ("tx7PowerSupply", 6462),
          ("tx7ewPowerSupply", 6461),
          ("tx7wePowerSupply", 6463),
          ("tx8PowerSupply", 6465),
          ("tx8ewPowerSupply", 6464),
          ("tx8wePowerSupply", 6466),
          ("txAis", 362),
          ("txAmplifier", 6467),
          ("txAuAis", 6468),
          ("txAuLop", 6469),
          ("txB1Sd", 6470),
          ("txB2Eber", 6471),
          ("txB2Sd", 6472),
          ("txBlockFailure", 6556),
          ("txCkSync1", 6474),
          ("txCkSync2", 6475),
          ("txCkSyncP", 6476),
          ("txCkSyncW", 6477),
          ("txClockFailure", 8010),
          ("txDegrade", 364),
          ("txDegradeEQPT", 7903),
          ("txElasticStoreOverflow", 8013),
          ("txFail", 365),
          ("txFailEQPT", 7904),
          ("txFailProtSide", 6631),
          ("txFailure", 1808),
          ("txIfLos", 6478),
          ("txLOSProtSide", 6620),
          ("txLaserFailure", 8112),
          ("txLos", 6479),
          ("txManualOperation", 6480),
          ("txMsAis", 6481),
          ("txMsRdi", 6482),
          ("txOduFailure", 6483),
          ("txOnLineChanFailProtSide", 6618),
          ("txOnLineChannelFailure", 6484),
          ("txOscillator", 6485),
          ("txPowerLimited", 3353),
          ("txPowerWrong", 6486),
          ("txSideCardFailure", 6473),
          ("txSquelchOn", 6487),
          ("txStdbyPowerSupply", 6489),
          ("txSynth", 6488),
          ("txa", 361),
          ("txb", 363),
          ("txlineal", 366),
          ("typeMismatch", 367),
          ("uLedFail", 369),
          ("uPAlarm", 6570),
          ("uPortFailure", 3355),
          ("uas15minThresholdCrossed", 8110),
          ("uas24hThresholdCrossed", 8111),
          ("uat", 368),
          ("unauthorizedAccessAttempt", 8187),
          ("unavailableStateB1", 6557),
          ("unavailableStateB2", 6558),
          ("unavailableStateB3", 6559),
          ("unavailableStateFebe", 6560),
          ("unavailableStateRp", 6561),
          ("unbalancedSignal", 779),
          ("undef", 370),
          ("underCurrent", 4001),
          ("underCurrent1", 762),
          ("underCurrent12", 761),
          ("underCurrent2", 763),
          ("undertemp", 3966),
          ("undervoltage", 3967),
          ("unequipped", 371),
          ("unexpectedChannelIDGFP", 9521),
          ("uniMcuMissing", 2150),
          ("unidirectTestFailure", 1030),
          ("unitFailed", 1828),
          ("unitFailure", 6490),
          ("unitRemoval", 1829),
          ("unitTypeMismatch", 1830),
          ("unitUnknown", 372),
          ("unknown", 0),
          ("unprotectedCardProblem", 532),
          ("unqualifiedOpticalModule", 2125),
          ("unqualifiedOpticalModule1", 1888),
          ("unqualifiedOpticalModule2", 1889),
          ("unqualifiedOpticalModule3", 1890),
          ("unqualifiedOpticalModule4", 1891),
          ("unqualifiedOpticalModuleLine1", 1943),
          ("unreachedRmNode", 1032),
          ("unresolvedsatop", 3895),
          ("unspecifiedCriticalAlarm1", 1907),
          ("unspecifiedCriticalAlarm2", 1908),
          ("unspecifiedMajorAlarm1", 1909),
          ("unspecifiedMajorAlarm2", 1910),
          ("unspecifiedMinorAlarm1", 1911),
          ("unspecifiedMinorAlarm2", 1912),
          ("unsuccessfulLoginsExceeded", 953),
          ("unsymmetricLoad", 765),
          ("upperCoolingFanFail", 373),
          ("upperCoolingFanMissing", 910),
          ("userChBoard", 6491),
          ("userPayloadMismatchGFP", 1958),
          ("userlock", 9998),
          ("utif", 888),
          ("utifX", 889),
          ("utifY", 890),
          ("utifp", 1806),
          ("vcatlom", 3889),
          ("vcgfail", 3995),
          ("vcoFrequencyDeviation", 6492),
          ("vcxoStatus", 853),
          ("ventSystemFailure", 9275),
          ("ventilationSystemFailure", 374),
          ("versionMismatch", 375),
          ("virtualChannelAis", 3347),
          ("virtualTrunkDegradation", 6649),
          ("virtualTrunkDown", 6650),
          ("virtualTrunkSessionDown", 6651),
          ("voaControlFail", 3359),
          ("voaFailure", 6745),
          ("voaProblem", 376),
          ("voaProblem1", 383),
          ("voaProblem10", 444),
          ("voaProblem11", 445),
          ("voaProblem12", 453),
          ("voaProblem13", 454),
          ("voaProblem14", 447),
          ("voaProblem15", 448),
          ("voaProblem16", 449),
          ("voaProblem17", 450),
          ("voaProblem18", 446),
          ("voaProblem19", 452),
          ("voaProblem2", 384),
          ("voaProblem20", 451),
          ("voaProblem3", 385),
          ("voaProblem4", 386),
          ("voaProblem5", 439),
          ("voaProblem6", 440),
          ("voaProblem7", 441),
          ("voaProblem8", 442),
          ("voaProblem9", 443),
          ("voaThresholdCrossed", 7786),
          ("voltageOoR", 774),
          ("voltageProblem", 1861),
          ("voltageProblemLine", 1862),
          ("voltageProblemTrib1", 1863),
          ("voltageProblemTrib2", 1864),
          ("voltageProblemTrib3", 1865),
          ("voltageProblemTrib4", 1866),
          ("voltageTooHigh", 518),
          ("voltageTooLow", 519),
          ("vpAis", 615),
          ("vpnConnectionFail", 3480),
          ("wAN", 377),
          ("wControl", 9517),
          ("waitToRestore", 6770),
          ("warAlrExtUnmangedNE", 620),
          ("warning", 378),
          ("warningAmbientTemperature", 9499),
          ("wavelengthItuMismatch", 6746),
          ("westExtraTrafficPreemp", 6747),
          ("wrongCardVersion", 379),
          ("wrongLaserSafetyBusCabling", 3415),
          ("wrongSW", 380),
          ("wrongShelfType", 3468),
          ("wsAisInserted", 6493),
          ("wsChBoard", 6494),
          ("wsLos", 6495),
          ("wssModuleProblem", 1938),
          ("wtrTimerRunning", 3362),
          ("xconCCMdefect", 9561),
          ("xfp-crossing-threshold", 9591),
          ("xfpDecisionThresSetFailed", 3611),
          ("xfpMismatch", 9557),
          ("xfpWavOffset", 9558),
          ("xfpWavSetError", 9559),
          ("xpicFail", 6496),
          ("xpicFailProtSide", 6607),
          ("xpicIfInput", 6497))
    )



class TrafficDirection(Integer32, TextualConvention):
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
        *(("both", 4),
          ("inbound", 2),
          ("none", 1),
          ("outbound", 3),
          ("outboundClientToLine", 5),
          ("outboundLineToClient", 6),
          ("unknown", 0))
    )



class Directionality(Integer32, TextualConvention):
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
        *(("bidirectional", 3),
          ("unidirectional", 2),
          ("unknown", 1))
    )



class NEClass(Integer32, TextualConvention):
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
        *(("managementNode", 3),
          ("masterRingNode", 4),
          ("repeaterNode", 2),
          ("singleNode", 1),
          ("slaveRingNode", 5))
    )



class PTTechnology(Integer32, TextualConvention):
    status = "current"


class PTServiceType(Integer32, TextualConvention):
    status = "current"


class PTInterfaceType(Integer32, TextualConvention):
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
        *(("electrical", 2),
          ("optical", 1),
          ("radio", 3),
          ("unknown", 0))
    )



class PTProtectionType(Integer32, TextualConvention):
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
        *(("bshr2East", 5),
          ("bshr2EastExtra", 6),
          ("bshr2West", 7),
          ("bshr2WestExtra", 8),
          ("bshr4EastProtecting", 10),
          ("bshr4EastWorking", 9),
          ("bshr4TransoceanicEastProtecting", 14),
          ("bshr4TransoceanicEastWorking", 13),
          ("bshr4TransoceanicWestProtecting", 16),
          ("bshr4TransoceanicWestWorking", 15),
          ("bshr4WestProtecting", 12),
          ("bshr4WestWorking", 11),
          ("msLtpProtecting", 3),
          ("msLtpProtectingExtra", 4),
          ("msLtpWorking", 1),
          ("msLtpWorkingExtra", 2),
          ("unprotected", 0))
    )



class TPType(Integer32, TextualConvention):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 3),
          ("unknown", 1),
          ("variable", 2))
    )



class TPTerminationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connection", 1),
          ("trail", 2))
    )



class TPReliability(Integer32, TextualConvention):
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
        *(("preEmptive", 1),
          ("protected", 3),
          ("unprotected", 2))
    )



class SVProtection(Integer32, TextualConvention):
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
        *(("prEnd2End", 2),
          ("prInAndBetweenSubnetworks", 4),
          ("prInSubnetworks", 3),
          ("unprotected", 1))
    )



class SNCProtectionInfo(Integer32, TextualConvention):
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
        *(("extendedProtectionInfo", 3),
          ("simpleProtectionInfo", 2),
          ("unprotected", 1))
    )



class EthernetPathProtectionInfo(Integer32, TextualConvention):
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
        *(("lspOneToOne", 3),
          ("oneToOne", 2),
          ("ring", 4),
          ("unknown", 0),
          ("unprotected", 1))
    )



class EthernetPathType(Integer32, TextualConvention):
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
        *(("multipointToMultipoint", 2),
          ("pointToPoint", 1),
          ("rootedMultipoint", 3))
    )



class TPEndPointType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destinationTP", 2),
          ("sourceTP", 1))
    )



class TPTimeSlotHierarchy(OctetString, TextualConvention):
    status = "obsolete"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 29),
    )



class CharacteristicInfo(Integer32, TextualConvention):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unknown", 1)
    )



class NotificationType(Integer32, TextualConvention):
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
        *(("alarm", 5),
          ("attributeValueChange", 4),
          ("objectCreation", 1),
          ("objectDeletion", 2),
          ("other", 0),
          ("relationshipChange", 6),
          ("stateChange", 3))
    )



class LayerSet(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class FilterType(Integer32, TextualConvention):
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
        *(("ethernetPathObject", 5),
          ("neObject", 3),
          ("portObject", 2),
          ("sncObject", 4),
          ("tpObject", 1),
          ("unknown", 0))
    )



class PerfMonRequestId(UniqueId, TextualConvention):
    status = "current"


class PerfMonRequestState(Integer32, TextualConvention):
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
        *(("cancelled", 7),
          ("cancelling", 6),
          ("created", 1),
          ("deleting", 8),
          ("failed", 5),
          ("finished", 4),
          ("pending", 2),
          ("started", 3),
          ("unknown", 0))
    )



class PerfMonType(Integer32, TextualConvention):
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
        *(("pmCurrent", 2),
          ("pmHistory", 1),
          ("pmPoints", 3),
          ("unknown", 0))
    )



class PerfMonGranularity(Integer32, TextualConvention):
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
        *(("hours24", 2),
          ("minutes15", 1),
          ("unknown", 0))
    )



class PerfMonLocation(Integer32, TextualConvention):
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
        *(("farEnd", 2),
          ("nearEnd", 1),
          ("unknown", 0))
    )



class PerfMonDirection(Integer32, TextualConvention):
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
        *(("both", 4),
          ("incoming", 2),
          ("none", 1),
          ("outgoing", 3),
          ("unknown", 0))
    )



class PerfMonStatus(Integer32, TextualConvention):
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
        *(("incomplete", 3),
          ("invalid", 2),
          ("unknown", 0),
          ("valid", 1))
    )



class PerfMonThresholdType(Integer32, TextualConvention):
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
        *(("high", 3),
          ("highest", 4),
          ("low", 2),
          ("lowest", 1),
          ("unknown", 0))
    )



class OptPowerMonRequestId(UniqueId, TextualConvention):
    status = "current"


class OptPowerMonRequestState(Integer32, TextualConvention):
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
        *(("cancelled", 7),
          ("cancelling", 6),
          ("created", 1),
          ("deleting", 8),
          ("failed", 5),
          ("finished", 4),
          ("pending", 2),
          ("started", 3),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_Coriant_ObjectIdentity = ObjectIdentity
coriant = _Coriant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229)
)
_SvsProductMibs_ObjectIdentity = ObjectIdentity
svsProductMibs = _SvsProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6)
)
_EnmsNetworkSetup_ObjectIdentity = ObjectIdentity
enmsNetworkSetup = _EnmsNetworkSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1)
)
_EnmsNETable_Object = MibTable
enmsNETable = _EnmsNETable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1)
)
if mibBuilder.loadTexts:
    enmsNETable.setStatus("current")
_EnmsNEEntry_Object = MibTableRow
enmsNEEntry = _EnmsNEEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1)
)
enmsNEEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsNeNEId"),
)
if mibBuilder.loadTexts:
    enmsNEEntry.setStatus("current")
_EnmsNeNEId_Type = NEId
_EnmsNeNEId_Object = MibTableColumn
enmsNeNEId = _EnmsNeNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 1),
    _EnmsNeNEId_Type()
)
enmsNeNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeNEId.setStatus("current")
_EnmsNeType_Type = DisplayString
_EnmsNeType_Object = MibTableColumn
enmsNeType = _EnmsNeType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 2),
    _EnmsNeType_Type()
)
enmsNeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeType.setStatus("current")
_EnmsNeName_Type = DisplayString
_EnmsNeName_Object = MibTableColumn
enmsNeName = _EnmsNeName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 3),
    _EnmsNeName_Type()
)
enmsNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeName.setStatus("current")
_EnmsNeLocation_Type = DisplayString
_EnmsNeLocation_Object = MibTableColumn
enmsNeLocation = _EnmsNeLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 4),
    _EnmsNeLocation_Type()
)
enmsNeLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeLocation.setStatus("current")
_EnmsNeAlarmSeverity_Type = PerceivedSeverity
_EnmsNeAlarmSeverity_Object = MibTableColumn
enmsNeAlarmSeverity = _EnmsNeAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 5),
    _EnmsNeAlarmSeverity_Type()
)
enmsNeAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeAlarmSeverity.setStatus("current")
_EnmsNeOperatingMode_Type = OperatingMode
_EnmsNeOperatingMode_Object = MibTableColumn
enmsNeOperatingMode = _EnmsNeOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 6),
    _EnmsNeOperatingMode_Type()
)
enmsNeOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeOperatingMode.setStatus("current")
_EnmsNeOpState_Type = OperationalState
_EnmsNeOpState_Object = MibTableColumn
enmsNeOpState = _EnmsNeOpState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 7),
    _EnmsNeOpState_Type()
)
enmsNeOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeOpState.setStatus("current")
_EnmsNeCanBroadcast_Type = Boolean
_EnmsNeCanBroadcast_Object = MibTableColumn
enmsNeCanBroadcast = _EnmsNeCanBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 8),
    _EnmsNeCanBroadcast_Type()
)
enmsNeCanBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeCanBroadcast.setStatus("current")
_EnmsNeCanPathProtection_Type = Boolean
_EnmsNeCanPathProtection_Object = MibTableColumn
enmsNeCanPathProtection = _EnmsNeCanPathProtection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 9),
    _EnmsNeCanPathProtection_Type()
)
enmsNeCanPathProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeCanPathProtection.setStatus("current")
_EnmsNeClass_Type = NEClass
_EnmsNeClass_Object = MibTableColumn
enmsNeClass = _EnmsNeClass_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 10),
    _EnmsNeClass_Type()
)
enmsNeClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeClass.setStatus("current")
_EnmsNeExternalNEId_Type = InfoString
_EnmsNeExternalNEId_Object = MibTableColumn
enmsNeExternalNEId = _EnmsNeExternalNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 11),
    _EnmsNeExternalNEId_Type()
)
enmsNeExternalNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeExternalNEId.setStatus("obsolete")
_EnmsNeIsPseudoNE_Type = Boolean
_EnmsNeIsPseudoNE_Object = MibTableColumn
enmsNeIsPseudoNE = _EnmsNeIsPseudoNE_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 12),
    _EnmsNeIsPseudoNE_Type()
)
enmsNeIsPseudoNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeIsPseudoNE.setStatus("current")
_EnmsNeIdName_Type = DisplayString
_EnmsNeIdName_Object = MibTableColumn
enmsNeIdName = _EnmsNeIdName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 13),
    _EnmsNeIdName_Type()
)
enmsNeIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeIdName.setStatus("current")
_EnmsNeCommunicationState_Type = OperationalState
_EnmsNeCommunicationState_Object = MibTableColumn
enmsNeCommunicationState = _EnmsNeCommunicationState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 14),
    _EnmsNeCommunicationState_Type()
)
enmsNeCommunicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeCommunicationState.setStatus("current")
_EnmsNeDCNLocation_Type = DisplayString
_EnmsNeDCNLocation_Object = MibTableColumn
enmsNeDCNLocation = _EnmsNeDCNLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 15),
    _EnmsNeDCNLocation_Type()
)
enmsNeDCNLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeDCNLocation.setStatus("current")
_EnmsNeSystemContainer_Type = DisplayString
_EnmsNeSystemContainer_Object = MibTableColumn
enmsNeSystemContainer = _EnmsNeSystemContainer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 16),
    _EnmsNeSystemContainer_Type()
)
enmsNeSystemContainer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeSystemContainer.setStatus("current")
_EnmsNeUserText_Type = DisplayString
_EnmsNeUserText_Object = MibTableColumn
enmsNeUserText = _EnmsNeUserText_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 1, 1, 17),
    _EnmsNeUserText_Type()
)
enmsNeUserText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeUserText.setStatus("current")
_EnmsModuleTable_Object = MibTable
enmsModuleTable = _EnmsModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 2)
)
if mibBuilder.loadTexts:
    enmsModuleTable.setStatus("current")
_EnmsModuleEntry_Object = MibTableRow
enmsModuleEntry = _EnmsModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 2, 1)
)
enmsModuleEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsMoNEId"),
    (0, "TNMS-NBI-MIB", "enmsMoModuleId"),
)
if mibBuilder.loadTexts:
    enmsModuleEntry.setStatus("current")
_EnmsMoNEId_Type = NEId
_EnmsMoNEId_Object = MibTableColumn
enmsMoNEId = _EnmsMoNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 2, 1, 1),
    _EnmsMoNEId_Type()
)
enmsMoNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsMoNEId.setStatus("current")
_EnmsMoModuleId_Type = ModuleId
_EnmsMoModuleId_Object = MibTableColumn
enmsMoModuleId = _EnmsMoModuleId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 2, 1, 2),
    _EnmsMoModuleId_Type()
)
enmsMoModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsMoModuleId.setStatus("current")
_EnmsMoType_Type = DisplayString
_EnmsMoType_Object = MibTableColumn
enmsMoType = _EnmsMoType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 2, 1, 3),
    _EnmsMoType_Type()
)
enmsMoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsMoType.setStatus("obsolete")
_EnmsMoName_Type = DisplayString
_EnmsMoName_Object = MibTableColumn
enmsMoName = _EnmsMoName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 2, 1, 4),
    _EnmsMoName_Type()
)
enmsMoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsMoName.setStatus("current")
_EnmsMoOpState_Type = OperationalState
_EnmsMoOpState_Object = MibTableColumn
enmsMoOpState = _EnmsMoOpState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 2, 1, 5),
    _EnmsMoOpState_Type()
)
enmsMoOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsMoOpState.setStatus("current")
_EnmsMoShelf_Type = DisplayString
_EnmsMoShelf_Object = MibTableColumn
enmsMoShelf = _EnmsMoShelf_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 2, 1, 6),
    _EnmsMoShelf_Type()
)
enmsMoShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsMoShelf.setStatus("current")
_EnmsMoSlot_Type = DisplayString
_EnmsMoSlot_Object = MibTableColumn
enmsMoSlot = _EnmsMoSlot_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 2, 1, 7),
    _EnmsMoSlot_Type()
)
enmsMoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsMoSlot.setStatus("current")
_EnmsMoObjectType_Type = Integer32
_EnmsMoObjectType_Object = MibTableColumn
enmsMoObjectType = _EnmsMoObjectType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 2, 1, 8),
    _EnmsMoObjectType_Type()
)
enmsMoObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsMoObjectType.setStatus("current")
_EnmsPortTable_Object = MibTable
enmsPortTable = _EnmsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3)
)
if mibBuilder.loadTexts:
    enmsPortTable.setStatus("current")
_EnmsPortEntry_Object = MibTableRow
enmsPortEntry = _EnmsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1)
)
enmsPortEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsPtNEId"),
    (0, "TNMS-NBI-MIB", "enmsPtPortId"),
)
if mibBuilder.loadTexts:
    enmsPortEntry.setStatus("current")
_EnmsPtNEId_Type = NEId
_EnmsPtNEId_Object = MibTableColumn
enmsPtNEId = _EnmsPtNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 1),
    _EnmsPtNEId_Type()
)
enmsPtNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtNEId.setStatus("current")
_EnmsPtPortId_Type = PortId
_EnmsPtPortId_Object = MibTableColumn
enmsPtPortId = _EnmsPtPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 2),
    _EnmsPtPortId_Type()
)
enmsPtPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtPortId.setStatus("current")
_EnmsPtName_Type = DisplayString
_EnmsPtName_Object = MibTableColumn
enmsPtName = _EnmsPtName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 3),
    _EnmsPtName_Type()
)
enmsPtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtName.setStatus("current")
_EnmsPtModuleId_Type = ModuleId
_EnmsPtModuleId_Object = MibTableColumn
enmsPtModuleId = _EnmsPtModuleId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 4),
    _EnmsPtModuleId_Type()
)
enmsPtModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtModuleId.setStatus("obsolete")
_EnmsPtTechnology_Type = PTTechnology
_EnmsPtTechnology_Object = MibTableColumn
enmsPtTechnology = _EnmsPtTechnology_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 5),
    _EnmsPtTechnology_Type()
)
enmsPtTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtTechnology.setStatus("current")
_EnmsPtServiceType_Type = PTServiceType
_EnmsPtServiceType_Object = MibTableColumn
enmsPtServiceType = _EnmsPtServiceType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 6),
    _EnmsPtServiceType_Type()
)
enmsPtServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtServiceType.setStatus("current")
_EnmsPtInterfaceType_Type = PTInterfaceType
_EnmsPtInterfaceType_Object = MibTableColumn
enmsPtInterfaceType = _EnmsPtInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 7),
    _EnmsPtInterfaceType_Type()
)
enmsPtInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtInterfaceType.setStatus("current")
_EnmsPtBandwidth_Type = Bandwidth
_EnmsPtBandwidth_Object = MibTableColumn
enmsPtBandwidth = _EnmsPtBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 8),
    _EnmsPtBandwidth_Type()
)
enmsPtBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtBandwidth.setStatus("current")
_EnmsPtOpState_Type = OperationalState
_EnmsPtOpState_Object = MibTableColumn
enmsPtOpState = _EnmsPtOpState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 9),
    _EnmsPtOpState_Type()
)
enmsPtOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtOpState.setStatus("obsolete")
_EnmsPtOperatingMode_Type = OperatingMode
_EnmsPtOperatingMode_Object = MibTableColumn
enmsPtOperatingMode = _EnmsPtOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 10),
    _EnmsPtOperatingMode_Type()
)
enmsPtOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtOperatingMode.setStatus("obsolete")
_EnmsPtDirection_Type = Directionality
_EnmsPtDirection_Object = MibTableColumn
enmsPtDirection = _EnmsPtDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 11),
    _EnmsPtDirection_Type()
)
enmsPtDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtDirection.setStatus("current")
_EnmsPtCanBroadcast_Type = Boolean
_EnmsPtCanBroadcast_Object = MibTableColumn
enmsPtCanBroadcast = _EnmsPtCanBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 12),
    _EnmsPtCanBroadcast_Type()
)
enmsPtCanBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtCanBroadcast.setStatus("current")
_EnmsPtCanPathProtection_Type = Boolean
_EnmsPtCanPathProtection_Object = MibTableColumn
enmsPtCanPathProtection = _EnmsPtCanPathProtection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 13),
    _EnmsPtCanPathProtection_Type()
)
enmsPtCanPathProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtCanPathProtection.setStatus("current")
_EnmsPtAlarmSeverity_Type = PerceivedSeverity
_EnmsPtAlarmSeverity_Object = MibTableColumn
enmsPtAlarmSeverity = _EnmsPtAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 14),
    _EnmsPtAlarmSeverity_Type()
)
enmsPtAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtAlarmSeverity.setStatus("current")
_EnmsPtAdminState_Type = AdministrativeState
_EnmsPtAdminState_Object = MibTableColumn
enmsPtAdminState = _EnmsPtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 15),
    _EnmsPtAdminState_Type()
)
enmsPtAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtAdminState.setStatus("obsolete")
_EnmsPtOpStateTX_Type = OperationalState
_EnmsPtOpStateTX_Object = MibTableColumn
enmsPtOpStateTX = _EnmsPtOpStateTX_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 16),
    _EnmsPtOpStateTX_Type()
)
enmsPtOpStateTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtOpStateTX.setStatus("current")
_EnmsPtOpStateRX_Type = OperationalState
_EnmsPtOpStateRX_Object = MibTableColumn
enmsPtOpStateRX = _EnmsPtOpStateRX_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 17),
    _EnmsPtOpStateRX_Type()
)
enmsPtOpStateRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtOpStateRX.setStatus("current")
_EnmsPtModuleIdTX_Type = ModuleId
_EnmsPtModuleIdTX_Object = MibTableColumn
enmsPtModuleIdTX = _EnmsPtModuleIdTX_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 18),
    _EnmsPtModuleIdTX_Type()
)
enmsPtModuleIdTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtModuleIdTX.setStatus("current")
_EnmsPtModuleIdRX_Type = ModuleId
_EnmsPtModuleIdRX_Object = MibTableColumn
enmsPtModuleIdRX = _EnmsPtModuleIdRX_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 19),
    _EnmsPtModuleIdRX_Type()
)
enmsPtModuleIdRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtModuleIdRX.setStatus("current")
_EnmsPtLayerSet_Type = LayerSet
_EnmsPtLayerSet_Object = MibTableColumn
enmsPtLayerSet = _EnmsPtLayerSet_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 20),
    _EnmsPtLayerSet_Type()
)
enmsPtLayerSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtLayerSet.setStatus("current")
_EnmsPtProtectionType_Type = PTProtectionType
_EnmsPtProtectionType_Object = MibTableColumn
enmsPtProtectionType = _EnmsPtProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 21),
    _EnmsPtProtectionType_Type()
)
enmsPtProtectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtProtectionType.setStatus("current")
_EnmsPtObjectType_Type = Integer32
_EnmsPtObjectType_Object = MibTableColumn
enmsPtObjectType = _EnmsPtObjectType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 3, 1, 22),
    _EnmsPtObjectType_Type()
)
enmsPtObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPtObjectType.setStatus("current")
_EnmsTPTable_Object = MibTable
enmsTPTable = _EnmsTPTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4)
)
if mibBuilder.loadTexts:
    enmsTPTable.setStatus("current")
_EnmsTPEntry_Object = MibTableRow
enmsTPEntry = _EnmsTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1)
)
enmsTPEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsTpNEId"),
    (0, "TNMS-NBI-MIB", "enmsTpPortId"),
    (0, "TNMS-NBI-MIB", "enmsTpTPIdH"),
    (0, "TNMS-NBI-MIB", "enmsTpTPIdL"),
)
if mibBuilder.loadTexts:
    enmsTPEntry.setStatus("current")
_EnmsTpNEId_Type = NEId
_EnmsTpNEId_Object = MibTableColumn
enmsTpNEId = _EnmsTpNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 1),
    _EnmsTpNEId_Type()
)
enmsTpNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpNEId.setStatus("current")
_EnmsTpPortId_Type = PortId
_EnmsTpPortId_Object = MibTableColumn
enmsTpPortId = _EnmsTpPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 2),
    _EnmsTpPortId_Type()
)
enmsTpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpPortId.setStatus("current")
_EnmsTpTPIdH_Type = TPId
_EnmsTpTPIdH_Object = MibTableColumn
enmsTpTPIdH = _EnmsTpTPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 3),
    _EnmsTpTPIdH_Type()
)
enmsTpTPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpTPIdH.setStatus("current")
_EnmsTpTPIdL_Type = TPId
_EnmsTpTPIdL_Object = MibTableColumn
enmsTpTPIdL = _EnmsTpTPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 4),
    _EnmsTpTPIdL_Type()
)
enmsTpTPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpTPIdL.setStatus("current")
_EnmsTpTPIndex_Type = TPIndex
_EnmsTpTPIndex_Object = MibTableColumn
enmsTpTPIndex = _EnmsTpTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 5),
    _EnmsTpTPIndex_Type()
)
enmsTpTPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpTPIndex.setStatus("current")
_EnmsTpNxCount_Type = Integer32
_EnmsTpNxCount_Object = MibTableColumn
enmsTpNxCount = _EnmsTpNxCount_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 6),
    _EnmsTpNxCount_Type()
)
enmsTpNxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpNxCount.setStatus("current")
_EnmsTpName_Type = DisplayString
_EnmsTpName_Object = MibTableColumn
enmsTpName = _EnmsTpName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 7),
    _EnmsTpName_Type()
)
enmsTpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpName.setStatus("current")
_EnmsTpBandwidth_Type = Bandwidth
_EnmsTpBandwidth_Object = MibTableColumn
enmsTpBandwidth = _EnmsTpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 8),
    _EnmsTpBandwidth_Type()
)
enmsTpBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpBandwidth.setStatus("current")
_EnmsTpTPType_Type = TPType
_EnmsTpTPType_Object = MibTableColumn
enmsTpTPType = _EnmsTpTPType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 9),
    _EnmsTpTPType_Type()
)
enmsTpTPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpTPType.setStatus("obsolete")
_EnmsTpTerminType_Type = TPTerminationType
_EnmsTpTerminType_Object = MibTableColumn
enmsTpTerminType = _EnmsTpTerminType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 10),
    _EnmsTpTerminType_Type()
)
enmsTpTerminType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpTerminType.setStatus("current")
_EnmsTpDirection_Type = Directionality
_EnmsTpDirection_Object = MibTableColumn
enmsTpDirection = _EnmsTpDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 11),
    _EnmsTpDirection_Type()
)
enmsTpDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpDirection.setStatus("current")
_EnmsTpOpStateTX_Type = OperationalState
_EnmsTpOpStateTX_Object = MibTableColumn
enmsTpOpStateTX = _EnmsTpOpStateTX_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 12),
    _EnmsTpOpStateTX_Type()
)
enmsTpOpStateTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpOpStateTX.setStatus("current")
_EnmsTpOpStateRX_Type = OperationalState
_EnmsTpOpStateRX_Object = MibTableColumn
enmsTpOpStateRX = _EnmsTpOpStateRX_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 13),
    _EnmsTpOpStateRX_Type()
)
enmsTpOpStateRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpOpStateRX.setStatus("current")
_EnmsTpAlarmSeverity_Type = PerceivedSeverity
_EnmsTpAlarmSeverity_Object = MibTableColumn
enmsTpAlarmSeverity = _EnmsTpAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 14),
    _EnmsTpAlarmSeverity_Type()
)
enmsTpAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpAlarmSeverity.setStatus("current")
_EnmsTpAdminState_Type = AdministrativeState
_EnmsTpAdminState_Object = MibTableColumn
enmsTpAdminState = _EnmsTpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 15),
    _EnmsTpAdminState_Type()
)
enmsTpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpAdminState.setStatus("obsolete")
_EnmsTpUsageCountTX_Type = Integer32
_EnmsTpUsageCountTX_Object = MibTableColumn
enmsTpUsageCountTX = _EnmsTpUsageCountTX_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 16),
    _EnmsTpUsageCountTX_Type()
)
enmsTpUsageCountTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpUsageCountTX.setStatus("current")
_EnmsTpUsageCountRX_Type = Integer32
_EnmsTpUsageCountRX_Object = MibTableColumn
enmsTpUsageCountRX = _EnmsTpUsageCountRX_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 17),
    _EnmsTpUsageCountRX_Type()
)
enmsTpUsageCountRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpUsageCountRX.setStatus("current")
_EnmsTpUsageStateTX_Type = UsageState
_EnmsTpUsageStateTX_Object = MibTableColumn
enmsTpUsageStateTX = _EnmsTpUsageStateTX_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 18),
    _EnmsTpUsageStateTX_Type()
)
enmsTpUsageStateTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpUsageStateTX.setStatus("current")
_EnmsTpUsageStateRX_Type = UsageState
_EnmsTpUsageStateRX_Object = MibTableColumn
enmsTpUsageStateRX = _EnmsTpUsageStateRX_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 19),
    _EnmsTpUsageStateRX_Type()
)
enmsTpUsageStateRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpUsageStateRX.setStatus("current")
_EnmsTpReliability_Type = TPReliability
_EnmsTpReliability_Object = MibTableColumn
enmsTpReliability = _EnmsTpReliability_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 20),
    _EnmsTpReliability_Type()
)
enmsTpReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpReliability.setStatus("obsolete")
_EnmsTpLayerSet_Type = LayerSet
_EnmsTpLayerSet_Object = MibTableColumn
enmsTpLayerSet = _EnmsTpLayerSet_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 21),
    _EnmsTpLayerSet_Type()
)
enmsTpLayerSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpLayerSet.setStatus("current")
_EnmsTpBandwidthTX_Type = Bandwidth
_EnmsTpBandwidthTX_Object = MibTableColumn
enmsTpBandwidthTX = _EnmsTpBandwidthTX_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 22),
    _EnmsTpBandwidthTX_Type()
)
enmsTpBandwidthTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpBandwidthTX.setStatus("current")
_EnmsTpBandwidthRX_Type = Bandwidth
_EnmsTpBandwidthRX_Object = MibTableColumn
enmsTpBandwidthRX = _EnmsTpBandwidthRX_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 23),
    _EnmsTpBandwidthRX_Type()
)
enmsTpBandwidthRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpBandwidthRX.setStatus("current")
_EnmsTpParentPortId_Type = PortId
_EnmsTpParentPortId_Object = MibTableColumn
enmsTpParentPortId = _EnmsTpParentPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 24),
    _EnmsTpParentPortId_Type()
)
enmsTpParentPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpParentPortId.setStatus("current")
_EnmsTpParentTPIdH_Type = TPId
_EnmsTpParentTPIdH_Object = MibTableColumn
enmsTpParentTPIdH = _EnmsTpParentTPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 25),
    _EnmsTpParentTPIdH_Type()
)
enmsTpParentTPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpParentTPIdH.setStatus("current")
_EnmsTpParentTPIdL_Type = TPId
_EnmsTpParentTPIdL_Object = MibTableColumn
enmsTpParentTPIdL = _EnmsTpParentTPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 26),
    _EnmsTpParentTPIdL_Type()
)
enmsTpParentTPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpParentTPIdL.setStatus("current")
_EnmsTpFragmentLayer_Type = LayerSet
_EnmsTpFragmentLayer_Object = MibTableColumn
enmsTpFragmentLayer = _EnmsTpFragmentLayer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 27),
    _EnmsTpFragmentLayer_Type()
)
enmsTpFragmentLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpFragmentLayer.setStatus("current")
_EnmsTpObjectType_Type = Integer32
_EnmsTpObjectType_Object = MibTableColumn
enmsTpObjectType = _EnmsTpObjectType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 28),
    _EnmsTpObjectType_Type()
)
enmsTpObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpObjectType.setStatus("current")
_EnmsTpMuxPartnerTPIdH_Type = TPId
_EnmsTpMuxPartnerTPIdH_Object = MibTableColumn
enmsTpMuxPartnerTPIdH = _EnmsTpMuxPartnerTPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 29),
    _EnmsTpMuxPartnerTPIdH_Type()
)
enmsTpMuxPartnerTPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpMuxPartnerTPIdH.setStatus("current")
_EnmsTpMuxPartnerTPIdL_Type = TPId
_EnmsTpMuxPartnerTPIdL_Object = MibTableColumn
enmsTpMuxPartnerTPIdL = _EnmsTpMuxPartnerTPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 4, 1, 30),
    _EnmsTpMuxPartnerTPIdL_Type()
)
enmsTpMuxPartnerTPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTpMuxPartnerTPIdL.setStatus("current")
_EnmsPortConnTable_Object = MibTable
enmsPortConnTable = _EnmsPortConnTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 5)
)
if mibBuilder.loadTexts:
    enmsPortConnTable.setStatus("current")
_EnmsPortConnEntry_Object = MibTableRow
enmsPortConnEntry = _EnmsPortConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 5, 1)
)
enmsPortConnEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsPcPortConnId"),
)
if mibBuilder.loadTexts:
    enmsPortConnEntry.setStatus("current")
_EnmsPcPortConnId_Type = PortConnId
_EnmsPcPortConnId_Object = MibTableColumn
enmsPcPortConnId = _EnmsPcPortConnId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 5, 1, 1),
    _EnmsPcPortConnId_Type()
)
enmsPcPortConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPcPortConnId.setStatus("current")
_EnmsPcSrcNEId_Type = NEId
_EnmsPcSrcNEId_Object = MibTableColumn
enmsPcSrcNEId = _EnmsPcSrcNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 5, 1, 2),
    _EnmsPcSrcNEId_Type()
)
enmsPcSrcNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPcSrcNEId.setStatus("current")
_EnmsPcSrcPortId_Type = PortId
_EnmsPcSrcPortId_Object = MibTableColumn
enmsPcSrcPortId = _EnmsPcSrcPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 5, 1, 3),
    _EnmsPcSrcPortId_Type()
)
enmsPcSrcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPcSrcPortId.setStatus("current")
_EnmsPcDstNEId_Type = NEId
_EnmsPcDstNEId_Object = MibTableColumn
enmsPcDstNEId = _EnmsPcDstNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 5, 1, 4),
    _EnmsPcDstNEId_Type()
)
enmsPcDstNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPcDstNEId.setStatus("current")
_EnmsPcDstPortId_Type = PortId
_EnmsPcDstPortId_Object = MibTableColumn
enmsPcDstPortId = _EnmsPcDstPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 5, 1, 5),
    _EnmsPcDstPortId_Type()
)
enmsPcDstPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPcDstPortId.setStatus("current")
_EnmsPcName_Type = DisplayString
_EnmsPcName_Object = MibTableColumn
enmsPcName = _EnmsPcName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 5, 1, 6),
    _EnmsPcName_Type()
)
enmsPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPcName.setStatus("current")
_EnmsPcSrcAlarmSeverity_Type = PerceivedSeverity
_EnmsPcSrcAlarmSeverity_Object = MibTableColumn
enmsPcSrcAlarmSeverity = _EnmsPcSrcAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 5, 1, 7),
    _EnmsPcSrcAlarmSeverity_Type()
)
enmsPcSrcAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPcSrcAlarmSeverity.setStatus("current")
_EnmsPcDstAlarmSeverity_Type = PerceivedSeverity
_EnmsPcDstAlarmSeverity_Object = MibTableColumn
enmsPcDstAlarmSeverity = _EnmsPcDstAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 5, 1, 8),
    _EnmsPcDstAlarmSeverity_Type()
)
enmsPcDstAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPcDstAlarmSeverity.setStatus("current")
_EnmsPcBandwidth_Type = Bandwidth
_EnmsPcBandwidth_Object = MibTableColumn
enmsPcBandwidth = _EnmsPcBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 5, 1, 9),
    _EnmsPcBandwidth_Type()
)
enmsPcBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPcBandwidth.setStatus("current")
_EnmsPcDirection_Type = Directionality
_EnmsPcDirection_Object = MibTableColumn
enmsPcDirection = _EnmsPcDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 5, 1, 10),
    _EnmsPcDirection_Type()
)
enmsPcDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPcDirection.setStatus("current")
_EnmsPcLayerSet_Type = LayerSet
_EnmsPcLayerSet_Object = MibTableColumn
enmsPcLayerSet = _EnmsPcLayerSet_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 5, 1, 11),
    _EnmsPcLayerSet_Type()
)
enmsPcLayerSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPcLayerSet.setStatus("current")
_EnmsSNCTable_Object = MibTable
enmsSNCTable = _EnmsSNCTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6)
)
if mibBuilder.loadTexts:
    enmsSNCTable.setStatus("current")
_EnmsSNCEntry_Object = MibTableRow
enmsSNCEntry = _EnmsSNCEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1)
)
enmsSNCEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsScSNCId"),
)
if mibBuilder.loadTexts:
    enmsSNCEntry.setStatus("current")
_EnmsScSNCId_Type = SNCId
_EnmsScSNCId_Object = MibTableColumn
enmsScSNCId = _EnmsScSNCId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 1),
    _EnmsScSNCId_Type()
)
enmsScSNCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScSNCId.setStatus("current")
_EnmsScSrcNEId_Type = NEId
_EnmsScSrcNEId_Object = MibTableColumn
enmsScSrcNEId = _EnmsScSrcNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 2),
    _EnmsScSrcNEId_Type()
)
enmsScSrcNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScSrcNEId.setStatus("current")
_EnmsScSrcPortId_Type = PortId
_EnmsScSrcPortId_Object = MibTableColumn
enmsScSrcPortId = _EnmsScSrcPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 3),
    _EnmsScSrcPortId_Type()
)
enmsScSrcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScSrcPortId.setStatus("current")
_EnmsScSrcTPIdH_Type = TPId
_EnmsScSrcTPIdH_Object = MibTableColumn
enmsScSrcTPIdH = _EnmsScSrcTPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 4),
    _EnmsScSrcTPIdH_Type()
)
enmsScSrcTPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScSrcTPIdH.setStatus("current")
_EnmsScSrcTPIdL_Type = TPId
_EnmsScSrcTPIdL_Object = MibTableColumn
enmsScSrcTPIdL = _EnmsScSrcTPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 5),
    _EnmsScSrcTPIdL_Type()
)
enmsScSrcTPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScSrcTPIdL.setStatus("current")
_EnmsScDestNEId_Type = NEId
_EnmsScDestNEId_Object = MibTableColumn
enmsScDestNEId = _EnmsScDestNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 6),
    _EnmsScDestNEId_Type()
)
enmsScDestNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScDestNEId.setStatus("current")
_EnmsScDestPortId_Type = PortId
_EnmsScDestPortId_Object = MibTableColumn
enmsScDestPortId = _EnmsScDestPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 7),
    _EnmsScDestPortId_Type()
)
enmsScDestPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScDestPortId.setStatus("current")
_EnmsScDestTPIdH_Type = TPId
_EnmsScDestTPIdH_Object = MibTableColumn
enmsScDestTPIdH = _EnmsScDestTPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 8),
    _EnmsScDestTPIdH_Type()
)
enmsScDestTPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScDestTPIdH.setStatus("current")
_EnmsScDestTPIdL_Type = TPId
_EnmsScDestTPIdL_Object = MibTableColumn
enmsScDestTPIdL = _EnmsScDestTPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 9),
    _EnmsScDestTPIdL_Type()
)
enmsScDestTPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScDestTPIdL.setStatus("current")
_EnmsScSrc2NEId_Type = NEId
_EnmsScSrc2NEId_Object = MibTableColumn
enmsScSrc2NEId = _EnmsScSrc2NEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 10),
    _EnmsScSrc2NEId_Type()
)
enmsScSrc2NEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScSrc2NEId.setStatus("current")
_EnmsScSrc2PortId_Type = PortId
_EnmsScSrc2PortId_Object = MibTableColumn
enmsScSrc2PortId = _EnmsScSrc2PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 11),
    _EnmsScSrc2PortId_Type()
)
enmsScSrc2PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScSrc2PortId.setStatus("current")
_EnmsScSrc2TPIdH_Type = TPId
_EnmsScSrc2TPIdH_Object = MibTableColumn
enmsScSrc2TPIdH = _EnmsScSrc2TPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 12),
    _EnmsScSrc2TPIdH_Type()
)
enmsScSrc2TPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScSrc2TPIdH.setStatus("current")
_EnmsScSrc2TPIdL_Type = TPId
_EnmsScSrc2TPIdL_Object = MibTableColumn
enmsScSrc2TPIdL = _EnmsScSrc2TPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 13),
    _EnmsScSrc2TPIdL_Type()
)
enmsScSrc2TPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScSrc2TPIdL.setStatus("current")
_EnmsScDest2NEId_Type = NEId
_EnmsScDest2NEId_Object = MibTableColumn
enmsScDest2NEId = _EnmsScDest2NEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 14),
    _EnmsScDest2NEId_Type()
)
enmsScDest2NEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScDest2NEId.setStatus("current")
_EnmsScDest2PortId_Type = PortId
_EnmsScDest2PortId_Object = MibTableColumn
enmsScDest2PortId = _EnmsScDest2PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 15),
    _EnmsScDest2PortId_Type()
)
enmsScDest2PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScDest2PortId.setStatus("current")
_EnmsScDest2TPIdH_Type = TPId
_EnmsScDest2TPIdH_Object = MibTableColumn
enmsScDest2TPIdH = _EnmsScDest2TPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 16),
    _EnmsScDest2TPIdH_Type()
)
enmsScDest2TPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScDest2TPIdH.setStatus("current")
_EnmsScDest2TPIdL_Type = TPId
_EnmsScDest2TPIdL_Object = MibTableColumn
enmsScDest2TPIdL = _EnmsScDest2TPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 17),
    _EnmsScDest2TPIdL_Type()
)
enmsScDest2TPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScDest2TPIdL.setStatus("current")
_EnmsScServiceId_Type = ServiceId
_EnmsScServiceId_Object = MibTableColumn
enmsScServiceId = _EnmsScServiceId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 18),
    _EnmsScServiceId_Type()
)
enmsScServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScServiceId.setStatus("current")
_EnmsScName_Type = DisplayString
_EnmsScName_Object = MibTableColumn
enmsScName = _EnmsScName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 19),
    _EnmsScName_Type()
)
enmsScName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScName.setStatus("current")
_EnmsScOpState_Type = OperationalState
_EnmsScOpState_Object = MibTableColumn
enmsScOpState = _EnmsScOpState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 20),
    _EnmsScOpState_Type()
)
enmsScOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScOpState.setStatus("current")
_EnmsScAdminState_Type = AdministrativeState
_EnmsScAdminState_Object = MibTableColumn
enmsScAdminState = _EnmsScAdminState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 21),
    _EnmsScAdminState_Type()
)
enmsScAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScAdminState.setStatus("current")
_EnmsScAlarmSeverity_Type = PerceivedSeverity
_EnmsScAlarmSeverity_Object = MibTableColumn
enmsScAlarmSeverity = _EnmsScAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 22),
    _EnmsScAlarmSeverity_Type()
)
enmsScAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScAlarmSeverity.setStatus("current")
_EnmsScBandwidth_Type = Bandwidth
_EnmsScBandwidth_Object = MibTableColumn
enmsScBandwidth = _EnmsScBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 23),
    _EnmsScBandwidth_Type()
)
enmsScBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScBandwidth.setStatus("current")
_EnmsScDirection_Type = Directionality
_EnmsScDirection_Object = MibTableColumn
enmsScDirection = _EnmsScDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 24),
    _EnmsScDirection_Type()
)
enmsScDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScDirection.setStatus("current")
_EnmsScProtectionFlag_Type = Boolean
_EnmsScProtectionFlag_Object = MibTableColumn
enmsScProtectionFlag = _EnmsScProtectionFlag_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 25),
    _EnmsScProtectionFlag_Type()
)
enmsScProtectionFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScProtectionFlag.setStatus("obsolete")
_EnmsScProtectionInfo_Type = SNCProtectionInfo
_EnmsScProtectionInfo_Object = MibTableColumn
enmsScProtectionInfo = _EnmsScProtectionInfo_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 26),
    _EnmsScProtectionInfo_Type()
)
enmsScProtectionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScProtectionInfo.setStatus("current")
_EnmsScNxCount_Type = Unsigned32
_EnmsScNxCount_Object = MibTableColumn
enmsScNxCount = _EnmsScNxCount_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 27),
    _EnmsScNxCount_Type()
)
enmsScNxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScNxCount.setStatus("current")
_EnmsScSNCOwnerId_Type = SNCId
_EnmsScSNCOwnerId_Object = MibTableColumn
enmsScSNCOwnerId = _EnmsScSNCOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 28),
    _EnmsScSNCOwnerId_Type()
)
enmsScSNCOwnerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScSNCOwnerId.setStatus("current")
_EnmsScLayerSet_Type = LayerSet
_EnmsScLayerSet_Object = MibTableColumn
enmsScLayerSet = _EnmsScLayerSet_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 29),
    _EnmsScLayerSet_Type()
)
enmsScLayerSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScLayerSet.setStatus("current")
_EnmsScFragmentLayer_Type = LayerSet
_EnmsScFragmentLayer_Object = MibTableColumn
enmsScFragmentLayer = _EnmsScFragmentLayer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 30),
    _EnmsScFragmentLayer_Type()
)
enmsScFragmentLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScFragmentLayer.setStatus("current")
_EnmsScMinBandwidth_Type = Bandwidth
_EnmsScMinBandwidth_Object = MibTableColumn
enmsScMinBandwidth = _EnmsScMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 31),
    _EnmsScMinBandwidth_Type()
)
enmsScMinBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScMinBandwidth.setStatus("current")
_EnmsScRequiredBandwidth_Type = Boolean
_EnmsScRequiredBandwidth_Object = MibTableColumn
enmsScRequiredBandwidth = _EnmsScRequiredBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 6, 1, 32),
    _EnmsScRequiredBandwidth_Type()
)
enmsScRequiredBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsScRequiredBandwidth.setStatus("current")
_EnmsSNCTPTable_Object = MibTable
enmsSNCTPTable = _EnmsSNCTPTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 7)
)
if mibBuilder.loadTexts:
    enmsSNCTPTable.setStatus("current")
_EnmsSNCTPEntry_Object = MibTableRow
enmsSNCTPEntry = _EnmsSNCTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 7, 1)
)
enmsSNCTPEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsStSNCId"),
    (0, "TNMS-NBI-MIB", "enmsStTPNumber"),
)
if mibBuilder.loadTexts:
    enmsSNCTPEntry.setStatus("current")
_EnmsStSNCId_Type = SNCId
_EnmsStSNCId_Object = MibTableColumn
enmsStSNCId = _EnmsStSNCId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 7, 1, 1),
    _EnmsStSNCId_Type()
)
enmsStSNCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsStSNCId.setStatus("current")
_EnmsStTPNumber_Type = Unsigned32
_EnmsStTPNumber_Object = MibTableColumn
enmsStTPNumber = _EnmsStTPNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 7, 1, 2),
    _EnmsStTPNumber_Type()
)
enmsStTPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsStTPNumber.setStatus("current")
_EnmsStNEId_Type = NEId
_EnmsStNEId_Object = MibTableColumn
enmsStNEId = _EnmsStNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 7, 1, 3),
    _EnmsStNEId_Type()
)
enmsStNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsStNEId.setStatus("current")
_EnmsStPortId_Type = PortId
_EnmsStPortId_Object = MibTableColumn
enmsStPortId = _EnmsStPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 7, 1, 4),
    _EnmsStPortId_Type()
)
enmsStPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsStPortId.setStatus("current")
_EnmsStTPIdH_Type = TPId
_EnmsStTPIdH_Object = MibTableColumn
enmsStTPIdH = _EnmsStTPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 7, 1, 5),
    _EnmsStTPIdH_Type()
)
enmsStTPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsStTPIdH.setStatus("current")
_EnmsStTPIdL_Type = TPId
_EnmsStTPIdL_Object = MibTableColumn
enmsStTPIdL = _EnmsStTPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 7, 1, 6),
    _EnmsStTPIdL_Type()
)
enmsStTPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsStTPIdL.setStatus("current")
_EnmsStIsWorkingTP_Type = Boolean
_EnmsStIsWorkingTP_Object = MibTableColumn
enmsStIsWorkingTP = _EnmsStIsWorkingTP_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 7, 1, 7),
    _EnmsStIsWorkingTP_Type()
)
enmsStIsWorkingTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsStIsWorkingTP.setStatus("obsolete")
_EnmsStEndPointType_Type = TPEndPointType
_EnmsStEndPointType_Object = MibTableColumn
enmsStEndPointType = _EnmsStEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 7, 1, 8),
    _EnmsStEndPointType_Type()
)
enmsStEndPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsStEndPointType.setStatus("current")
_EnmsStTimeSlotHry_Type = TPTimeSlotHierarchy
_EnmsStTimeSlotHry_Object = MibTableColumn
enmsStTimeSlotHry = _EnmsStTimeSlotHry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 7, 1, 9),
    _EnmsStTimeSlotHry_Type()
)
enmsStTimeSlotHry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsStTimeSlotHry.setStatus("obsolete")
_EnmsSNCTHTable_Object = MibTable
enmsSNCTHTable = _EnmsSNCTHTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 8)
)
if mibBuilder.loadTexts:
    enmsSNCTHTable.setStatus("obsolete")
_EnmsSNCTHEntry_Object = MibTableRow
enmsSNCTHEntry = _EnmsSNCTHEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 8, 1)
)
enmsSNCTHEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsThSNCId"),
    (0, "TNMS-NBI-MIB", "enmsThTPNumber"),
    (0, "TNMS-NBI-MIB", "enmsThTPHierId"),
)
if mibBuilder.loadTexts:
    enmsSNCTHEntry.setStatus("obsolete")
_EnmsThSNCId_Type = SNCId
_EnmsThSNCId_Object = MibTableColumn
enmsThSNCId = _EnmsThSNCId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 8, 1, 1),
    _EnmsThSNCId_Type()
)
enmsThSNCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsThSNCId.setStatus("obsolete")
_EnmsThTPNumber_Type = Unsigned32
_EnmsThTPNumber_Object = MibTableColumn
enmsThTPNumber = _EnmsThTPNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 8, 1, 2),
    _EnmsThTPNumber_Type()
)
enmsThTPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsThTPNumber.setStatus("obsolete")
_EnmsThTPHierId_Type = CharacteristicInfo
_EnmsThTPHierId_Object = MibTableColumn
enmsThTPHierId = _EnmsThTPHierId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 8, 1, 3),
    _EnmsThTPHierId_Type()
)
enmsThTPHierId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsThTPHierId.setStatus("obsolete")
_EnmsThChannelNo_Type = Unsigned32
_EnmsThChannelNo_Object = MibTableColumn
enmsThChannelNo = _EnmsThChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 8, 1, 4),
    _EnmsThChannelNo_Type()
)
enmsThChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsThChannelNo.setStatus("obsolete")
_EnmsCCTable_Object = MibTable
enmsCCTable = _EnmsCCTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9)
)
if mibBuilder.loadTexts:
    enmsCCTable.setStatus("current")
_EnmsCCEntry_Object = MibTableRow
enmsCCEntry = _EnmsCCEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1)
)
enmsCCEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsCcNEId"),
    (0, "TNMS-NBI-MIB", "enmsCcCCId"),
)
if mibBuilder.loadTexts:
    enmsCCEntry.setStatus("current")
_EnmsCcNEId_Type = NEId
_EnmsCcNEId_Object = MibTableColumn
enmsCcNEId = _EnmsCcNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 1),
    _EnmsCcNEId_Type()
)
enmsCcNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcNEId.setStatus("current")
_EnmsCcCCId_Type = CCId
_EnmsCcCCId_Object = MibTableColumn
enmsCcCCId = _EnmsCcCCId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 2),
    _EnmsCcCCId_Type()
)
enmsCcCCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcCCId.setStatus("current")
_EnmsCcSrcNEId_Type = NEId
_EnmsCcSrcNEId_Object = MibTableColumn
enmsCcSrcNEId = _EnmsCcSrcNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 3),
    _EnmsCcSrcNEId_Type()
)
enmsCcSrcNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcSrcNEId.setStatus("current")
_EnmsCcSrcPortId_Type = PortId
_EnmsCcSrcPortId_Object = MibTableColumn
enmsCcSrcPortId = _EnmsCcSrcPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 4),
    _EnmsCcSrcPortId_Type()
)
enmsCcSrcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcSrcPortId.setStatus("current")
_EnmsCcSrcTPIdH_Type = TPId
_EnmsCcSrcTPIdH_Object = MibTableColumn
enmsCcSrcTPIdH = _EnmsCcSrcTPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 5),
    _EnmsCcSrcTPIdH_Type()
)
enmsCcSrcTPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcSrcTPIdH.setStatus("current")
_EnmsCcSrcTPIdL_Type = TPId
_EnmsCcSrcTPIdL_Object = MibTableColumn
enmsCcSrcTPIdL = _EnmsCcSrcTPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 6),
    _EnmsCcSrcTPIdL_Type()
)
enmsCcSrcTPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcSrcTPIdL.setStatus("current")
_EnmsCcDestNEId_Type = NEId
_EnmsCcDestNEId_Object = MibTableColumn
enmsCcDestNEId = _EnmsCcDestNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 7),
    _EnmsCcDestNEId_Type()
)
enmsCcDestNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcDestNEId.setStatus("current")
_EnmsCcDestPortId_Type = PortId
_EnmsCcDestPortId_Object = MibTableColumn
enmsCcDestPortId = _EnmsCcDestPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 8),
    _EnmsCcDestPortId_Type()
)
enmsCcDestPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcDestPortId.setStatus("current")
_EnmsCcDestTPIdH_Type = TPId
_EnmsCcDestTPIdH_Object = MibTableColumn
enmsCcDestTPIdH = _EnmsCcDestTPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 9),
    _EnmsCcDestTPIdH_Type()
)
enmsCcDestTPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcDestTPIdH.setStatus("current")
_EnmsCcDestTPIdL_Type = TPId
_EnmsCcDestTPIdL_Object = MibTableColumn
enmsCcDestTPIdL = _EnmsCcDestTPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 10),
    _EnmsCcDestTPIdL_Type()
)
enmsCcDestTPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcDestTPIdL.setStatus("current")
_EnmsCcSrc2NEId_Type = NEId
_EnmsCcSrc2NEId_Object = MibTableColumn
enmsCcSrc2NEId = _EnmsCcSrc2NEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 11),
    _EnmsCcSrc2NEId_Type()
)
enmsCcSrc2NEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcSrc2NEId.setStatus("current")
_EnmsCcSrc2PortId_Type = PortId
_EnmsCcSrc2PortId_Object = MibTableColumn
enmsCcSrc2PortId = _EnmsCcSrc2PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 12),
    _EnmsCcSrc2PortId_Type()
)
enmsCcSrc2PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcSrc2PortId.setStatus("current")
_EnmsCcSrc2TPIdH_Type = TPId
_EnmsCcSrc2TPIdH_Object = MibTableColumn
enmsCcSrc2TPIdH = _EnmsCcSrc2TPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 13),
    _EnmsCcSrc2TPIdH_Type()
)
enmsCcSrc2TPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcSrc2TPIdH.setStatus("current")
_EnmsCcSrc2TPIdL_Type = TPId
_EnmsCcSrc2TPIdL_Object = MibTableColumn
enmsCcSrc2TPIdL = _EnmsCcSrc2TPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 14),
    _EnmsCcSrc2TPIdL_Type()
)
enmsCcSrc2TPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcSrc2TPIdL.setStatus("current")
_EnmsCcDest2NEId_Type = NEId
_EnmsCcDest2NEId_Object = MibTableColumn
enmsCcDest2NEId = _EnmsCcDest2NEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 15),
    _EnmsCcDest2NEId_Type()
)
enmsCcDest2NEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcDest2NEId.setStatus("current")
_EnmsCcDest2PortId_Type = PortId
_EnmsCcDest2PortId_Object = MibTableColumn
enmsCcDest2PortId = _EnmsCcDest2PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 16),
    _EnmsCcDest2PortId_Type()
)
enmsCcDest2PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcDest2PortId.setStatus("current")
_EnmsCcDest2TPIdH_Type = TPId
_EnmsCcDest2TPIdH_Object = MibTableColumn
enmsCcDest2TPIdH = _EnmsCcDest2TPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 17),
    _EnmsCcDest2TPIdH_Type()
)
enmsCcDest2TPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcDest2TPIdH.setStatus("current")
_EnmsCcDest2TPIdL_Type = TPId
_EnmsCcDest2TPIdL_Object = MibTableColumn
enmsCcDest2TPIdL = _EnmsCcDest2TPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 18),
    _EnmsCcDest2TPIdL_Type()
)
enmsCcDest2TPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcDest2TPIdL.setStatus("current")
_EnmsCcOpState_Type = OperationalState
_EnmsCcOpState_Object = MibTableColumn
enmsCcOpState = _EnmsCcOpState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 19),
    _EnmsCcOpState_Type()
)
enmsCcOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcOpState.setStatus("current")
_EnmsCcDirection_Type = Directionality
_EnmsCcDirection_Object = MibTableColumn
enmsCcDirection = _EnmsCcDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 20),
    _EnmsCcDirection_Type()
)
enmsCcDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcDirection.setStatus("current")
_EnmsCcProtectionFlag_Type = Boolean
_EnmsCcProtectionFlag_Object = MibTableColumn
enmsCcProtectionFlag = _EnmsCcProtectionFlag_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 21),
    _EnmsCcProtectionFlag_Type()
)
enmsCcProtectionFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcProtectionFlag.setStatus("current")
_EnmsCcProtectionState_Type = ProtectionState
_EnmsCcProtectionState_Object = MibTableColumn
enmsCcProtectionState = _EnmsCcProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 22),
    _EnmsCcProtectionState_Type()
)
enmsCcProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcProtectionState.setStatus("current")
_EnmsCcNxCount_Type = Unsigned32
_EnmsCcNxCount_Object = MibTableColumn
enmsCcNxCount = _EnmsCcNxCount_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 9, 1, 23),
    _EnmsCcNxCount_Type()
)
enmsCcNxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsCcNxCount.setStatus("current")
_EnmsSNCSNCTable_Object = MibTable
enmsSNCSNCTable = _EnmsSNCSNCTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 10)
)
if mibBuilder.loadTexts:
    enmsSNCSNCTable.setStatus("current")
_EnmsSNCSNCEntry_Object = MibTableRow
enmsSNCSNCEntry = _EnmsSNCSNCEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 10, 1)
)
enmsSNCSNCEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsSsSNCId"),
    (0, "TNMS-NBI-MIB", "enmsSsServerSNCId"),
)
if mibBuilder.loadTexts:
    enmsSNCSNCEntry.setStatus("current")
_EnmsSsSNCId_Type = SNCId
_EnmsSsSNCId_Object = MibTableColumn
enmsSsSNCId = _EnmsSsSNCId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 10, 1, 1),
    _EnmsSsSNCId_Type()
)
enmsSsSNCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSsSNCId.setStatus("current")
_EnmsSsServerSNCId_Type = SNCId
_EnmsSsServerSNCId_Object = MibTableColumn
enmsSsServerSNCId = _EnmsSsServerSNCId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 10, 1, 2),
    _EnmsSsServerSNCId_Type()
)
enmsSsServerSNCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSsServerSNCId.setStatus("current")
_EnmsSNCCCTable_Object = MibTable
enmsSNCCCTable = _EnmsSNCCCTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 11)
)
if mibBuilder.loadTexts:
    enmsSNCCCTable.setStatus("current")
_EnmsSNCCCEntry_Object = MibTableRow
enmsSNCCCEntry = _EnmsSNCCCEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 11, 1)
)
enmsSNCCCEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsSNCCCSNCId"),
    (0, "TNMS-NBI-MIB", "enmsSNCCCCCId"),
)
if mibBuilder.loadTexts:
    enmsSNCCCEntry.setStatus("current")
_EnmsSNCCCSNCId_Type = SNCId
_EnmsSNCCCSNCId_Object = MibTableColumn
enmsSNCCCSNCId = _EnmsSNCCCSNCId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 11, 1, 1),
    _EnmsSNCCCSNCId_Type()
)
enmsSNCCCSNCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSNCCCSNCId.setStatus("current")
_EnmsSNCCCCCId_Type = CCId
_EnmsSNCCCCCId_Object = MibTableColumn
enmsSNCCCCCId = _EnmsSNCCCCCId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 11, 1, 2),
    _EnmsSNCCCCCId_Type()
)
enmsSNCCCCCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSNCCCCCId.setStatus("current")
_EnmsNeSNCTable_Object = MibTable
enmsNeSNCTable = _EnmsNeSNCTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12)
)
if mibBuilder.loadTexts:
    enmsNeSNCTable.setStatus("current")
_EnmsNeSNCEntry_Object = MibTableRow
enmsNeSNCEntry = _EnmsNeSNCEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1)
)
enmsNeSNCEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsNeScNeId"),
    (0, "TNMS-NBI-MIB", "enmsNeScSNCId"),
)
if mibBuilder.loadTexts:
    enmsNeSNCEntry.setStatus("current")
_EnmsNeScNeId_Type = NEId
_EnmsNeScNeId_Object = MibTableColumn
enmsNeScNeId = _EnmsNeScNeId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 1),
    _EnmsNeScNeId_Type()
)
enmsNeScNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScNeId.setStatus("current")
_EnmsNeScSNCId_Type = SNCId
_EnmsNeScSNCId_Object = MibTableColumn
enmsNeScSNCId = _EnmsNeScSNCId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 2),
    _EnmsNeScSNCId_Type()
)
enmsNeScSNCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScSNCId.setStatus("current")
_EnmsNeScSrcNEId_Type = NEId
_EnmsNeScSrcNEId_Object = MibTableColumn
enmsNeScSrcNEId = _EnmsNeScSrcNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 3),
    _EnmsNeScSrcNEId_Type()
)
enmsNeScSrcNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScSrcNEId.setStatus("current")
_EnmsNeScSrcPortId_Type = PortId
_EnmsNeScSrcPortId_Object = MibTableColumn
enmsNeScSrcPortId = _EnmsNeScSrcPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 4),
    _EnmsNeScSrcPortId_Type()
)
enmsNeScSrcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScSrcPortId.setStatus("current")
_EnmsNeScSrcTPIdH_Type = TPId
_EnmsNeScSrcTPIdH_Object = MibTableColumn
enmsNeScSrcTPIdH = _EnmsNeScSrcTPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 5),
    _EnmsNeScSrcTPIdH_Type()
)
enmsNeScSrcTPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScSrcTPIdH.setStatus("current")
_EnmsNeScSrcTPIdL_Type = TPId
_EnmsNeScSrcTPIdL_Object = MibTableColumn
enmsNeScSrcTPIdL = _EnmsNeScSrcTPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 6),
    _EnmsNeScSrcTPIdL_Type()
)
enmsNeScSrcTPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScSrcTPIdL.setStatus("current")
_EnmsNeScDestNEId_Type = NEId
_EnmsNeScDestNEId_Object = MibTableColumn
enmsNeScDestNEId = _EnmsNeScDestNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 7),
    _EnmsNeScDestNEId_Type()
)
enmsNeScDestNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScDestNEId.setStatus("current")
_EnmsNeScDestPortId_Type = PortId
_EnmsNeScDestPortId_Object = MibTableColumn
enmsNeScDestPortId = _EnmsNeScDestPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 8),
    _EnmsNeScDestPortId_Type()
)
enmsNeScDestPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScDestPortId.setStatus("current")
_EnmsNeScDestTPIdH_Type = TPId
_EnmsNeScDestTPIdH_Object = MibTableColumn
enmsNeScDestTPIdH = _EnmsNeScDestTPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 9),
    _EnmsNeScDestTPIdH_Type()
)
enmsNeScDestTPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScDestTPIdH.setStatus("current")
_EnmsNeScDestTPIdL_Type = TPId
_EnmsNeScDestTPIdL_Object = MibTableColumn
enmsNeScDestTPIdL = _EnmsNeScDestTPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 10),
    _EnmsNeScDestTPIdL_Type()
)
enmsNeScDestTPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScDestTPIdL.setStatus("current")
_EnmsNeScSrc2NEId_Type = NEId
_EnmsNeScSrc2NEId_Object = MibTableColumn
enmsNeScSrc2NEId = _EnmsNeScSrc2NEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 11),
    _EnmsNeScSrc2NEId_Type()
)
enmsNeScSrc2NEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScSrc2NEId.setStatus("current")
_EnmsNeScSrc2PortId_Type = PortId
_EnmsNeScSrc2PortId_Object = MibTableColumn
enmsNeScSrc2PortId = _EnmsNeScSrc2PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 12),
    _EnmsNeScSrc2PortId_Type()
)
enmsNeScSrc2PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScSrc2PortId.setStatus("current")
_EnmsNeScSrc2TPIdH_Type = TPId
_EnmsNeScSrc2TPIdH_Object = MibTableColumn
enmsNeScSrc2TPIdH = _EnmsNeScSrc2TPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 13),
    _EnmsNeScSrc2TPIdH_Type()
)
enmsNeScSrc2TPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScSrc2TPIdH.setStatus("current")
_EnmsNeScSrc2TPIdL_Type = TPId
_EnmsNeScSrc2TPIdL_Object = MibTableColumn
enmsNeScSrc2TPIdL = _EnmsNeScSrc2TPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 14),
    _EnmsNeScSrc2TPIdL_Type()
)
enmsNeScSrc2TPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScSrc2TPIdL.setStatus("current")
_EnmsNeScDest2NEId_Type = NEId
_EnmsNeScDest2NEId_Object = MibTableColumn
enmsNeScDest2NEId = _EnmsNeScDest2NEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 15),
    _EnmsNeScDest2NEId_Type()
)
enmsNeScDest2NEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScDest2NEId.setStatus("current")
_EnmsNeScDest2PortId_Type = PortId
_EnmsNeScDest2PortId_Object = MibTableColumn
enmsNeScDest2PortId = _EnmsNeScDest2PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 16),
    _EnmsNeScDest2PortId_Type()
)
enmsNeScDest2PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScDest2PortId.setStatus("current")
_EnmsNeScDest2TPIdH_Type = TPId
_EnmsNeScDest2TPIdH_Object = MibTableColumn
enmsNeScDest2TPIdH = _EnmsNeScDest2TPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 17),
    _EnmsNeScDest2TPIdH_Type()
)
enmsNeScDest2TPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScDest2TPIdH.setStatus("current")
_EnmsNeScDest2TPIdL_Type = TPId
_EnmsNeScDest2TPIdL_Object = MibTableColumn
enmsNeScDest2TPIdL = _EnmsNeScDest2TPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 18),
    _EnmsNeScDest2TPIdL_Type()
)
enmsNeScDest2TPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScDest2TPIdL.setStatus("current")
_EnmsNeScServiceId_Type = ServiceId
_EnmsNeScServiceId_Object = MibTableColumn
enmsNeScServiceId = _EnmsNeScServiceId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 19),
    _EnmsNeScServiceId_Type()
)
enmsNeScServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScServiceId.setStatus("current")
_EnmsNeScName_Type = DisplayString
_EnmsNeScName_Object = MibTableColumn
enmsNeScName = _EnmsNeScName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 20),
    _EnmsNeScName_Type()
)
enmsNeScName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScName.setStatus("current")
_EnmsNeScOpState_Type = OperationalState
_EnmsNeScOpState_Object = MibTableColumn
enmsNeScOpState = _EnmsNeScOpState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 21),
    _EnmsNeScOpState_Type()
)
enmsNeScOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScOpState.setStatus("current")
_EnmsNeScAdminState_Type = AdministrativeState
_EnmsNeScAdminState_Object = MibTableColumn
enmsNeScAdminState = _EnmsNeScAdminState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 22),
    _EnmsNeScAdminState_Type()
)
enmsNeScAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScAdminState.setStatus("current")
_EnmsNeScAlarmSeverity_Type = PerceivedSeverity
_EnmsNeScAlarmSeverity_Object = MibTableColumn
enmsNeScAlarmSeverity = _EnmsNeScAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 23),
    _EnmsNeScAlarmSeverity_Type()
)
enmsNeScAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScAlarmSeverity.setStatus("current")
_EnmsNeScBandwidth_Type = Bandwidth
_EnmsNeScBandwidth_Object = MibTableColumn
enmsNeScBandwidth = _EnmsNeScBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 24),
    _EnmsNeScBandwidth_Type()
)
enmsNeScBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScBandwidth.setStatus("current")
_EnmsNeScDirection_Type = Directionality
_EnmsNeScDirection_Object = MibTableColumn
enmsNeScDirection = _EnmsNeScDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 25),
    _EnmsNeScDirection_Type()
)
enmsNeScDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScDirection.setStatus("current")
_EnmsNeScProtectionFlag_Type = Boolean
_EnmsNeScProtectionFlag_Object = MibTableColumn
enmsNeScProtectionFlag = _EnmsNeScProtectionFlag_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 26),
    _EnmsNeScProtectionFlag_Type()
)
enmsNeScProtectionFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScProtectionFlag.setStatus("obsolete")
_EnmsNeScProtectionInfo_Type = SNCProtectionInfo
_EnmsNeScProtectionInfo_Object = MibTableColumn
enmsNeScProtectionInfo = _EnmsNeScProtectionInfo_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 27),
    _EnmsNeScProtectionInfo_Type()
)
enmsNeScProtectionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScProtectionInfo.setStatus("current")
_EnmsNeScNxCount_Type = Unsigned32
_EnmsNeScNxCount_Object = MibTableColumn
enmsNeScNxCount = _EnmsNeScNxCount_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 28),
    _EnmsNeScNxCount_Type()
)
enmsNeScNxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScNxCount.setStatus("current")
_EnmsNeScSNCOwnerId_Type = SNCId
_EnmsNeScSNCOwnerId_Object = MibTableColumn
enmsNeScSNCOwnerId = _EnmsNeScSNCOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 29),
    _EnmsNeScSNCOwnerId_Type()
)
enmsNeScSNCOwnerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScSNCOwnerId.setStatus("current")
_EnmsNeScLayerSet_Type = LayerSet
_EnmsNeScLayerSet_Object = MibTableColumn
enmsNeScLayerSet = _EnmsNeScLayerSet_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 30),
    _EnmsNeScLayerSet_Type()
)
enmsNeScLayerSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScLayerSet.setStatus("current")
_EnmsNeScFragmentLayer_Type = LayerSet
_EnmsNeScFragmentLayer_Object = MibTableColumn
enmsNeScFragmentLayer = _EnmsNeScFragmentLayer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 31),
    _EnmsNeScFragmentLayer_Type()
)
enmsNeScFragmentLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScFragmentLayer.setStatus("current")
_EnmsNeScMinBandwidth_Type = Bandwidth
_EnmsNeScMinBandwidth_Object = MibTableColumn
enmsNeScMinBandwidth = _EnmsNeScMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 32),
    _EnmsNeScMinBandwidth_Type()
)
enmsNeScMinBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScMinBandwidth.setStatus("current")
_EnmsNeScRequiredBandwidth_Type = Boolean
_EnmsNeScRequiredBandwidth_Object = MibTableColumn
enmsNeScRequiredBandwidth = _EnmsNeScRequiredBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 12, 1, 33),
    _EnmsNeScRequiredBandwidth_Type()
)
enmsNeScRequiredBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNeScRequiredBandwidth.setStatus("current")
_EnmsEthernetPathTable_Object = MibTable
enmsEthernetPathTable = _EnmsEthernetPathTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 13)
)
if mibBuilder.loadTexts:
    enmsEthernetPathTable.setStatus("current")
_EnmsEthernetPathEntry_Object = MibTableRow
enmsEthernetPathEntry = _EnmsEthernetPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 13, 1)
)
enmsEthernetPathEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsEvcEthernetPathId"),
)
if mibBuilder.loadTexts:
    enmsEthernetPathEntry.setStatus("current")
_EnmsEvcEthernetPathId_Type = EthernetPathId
_EnmsEvcEthernetPathId_Object = MibTableColumn
enmsEvcEthernetPathId = _EnmsEvcEthernetPathId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 13, 1, 1),
    _EnmsEvcEthernetPathId_Type()
)
enmsEvcEthernetPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsEvcEthernetPathId.setStatus("current")
_EnmsEvcName_Type = DisplayString
_EnmsEvcName_Object = MibTableColumn
enmsEvcName = _EnmsEvcName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 13, 1, 2),
    _EnmsEvcName_Type()
)
enmsEvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsEvcName.setStatus("current")
_EnmsEvcSVlanId_Type = Integer32
_EnmsEvcSVlanId_Object = MibTableColumn
enmsEvcSVlanId = _EnmsEvcSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 13, 1, 3),
    _EnmsEvcSVlanId_Type()
)
enmsEvcSVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsEvcSVlanId.setStatus("current")
_EnmsEvcType_Type = EthernetPathType
_EnmsEvcType_Object = MibTableColumn
enmsEvcType = _EnmsEvcType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 13, 1, 4),
    _EnmsEvcType_Type()
)
enmsEvcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsEvcType.setStatus("current")
_EnmsEvcServiceId_Type = ServiceId
_EnmsEvcServiceId_Object = MibTableColumn
enmsEvcServiceId = _EnmsEvcServiceId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 13, 1, 5),
    _EnmsEvcServiceId_Type()
)
enmsEvcServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsEvcServiceId.setStatus("current")
_EnmsEvcOpState_Type = OperationalState
_EnmsEvcOpState_Object = MibTableColumn
enmsEvcOpState = _EnmsEvcOpState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 13, 1, 6),
    _EnmsEvcOpState_Type()
)
enmsEvcOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsEvcOpState.setStatus("current")
_EnmsEvcAdminState_Type = AdministrativeState
_EnmsEvcAdminState_Object = MibTableColumn
enmsEvcAdminState = _EnmsEvcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 13, 1, 7),
    _EnmsEvcAdminState_Type()
)
enmsEvcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsEvcAdminState.setStatus("current")
_EnmsEvcAlarmSeverity_Type = PerceivedSeverity
_EnmsEvcAlarmSeverity_Object = MibTableColumn
enmsEvcAlarmSeverity = _EnmsEvcAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 1, 13, 1, 8),
    _EnmsEvcAlarmSeverity_Type()
)
enmsEvcAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsEvcAlarmSeverity.setStatus("current")
_EnmsService_ObjectIdentity = ObjectIdentity
enmsService = _EnmsService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2)
)
_EnmsSubscriberTable_Object = MibTable
enmsSubscriberTable = _EnmsSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 1)
)
if mibBuilder.loadTexts:
    enmsSubscriberTable.setStatus("current")
_EnmsSubscriberEntry_Object = MibTableRow
enmsSubscriberEntry = _EnmsSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 1, 1)
)
enmsSubscriberEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsSbSubscriberId"),
)
if mibBuilder.loadTexts:
    enmsSubscriberEntry.setStatus("current")
_EnmsSbSubscriberId_Type = SubscriberId
_EnmsSbSubscriberId_Object = MibTableColumn
enmsSbSubscriberId = _EnmsSbSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 1, 1, 1),
    _EnmsSbSubscriberId_Type()
)
enmsSbSubscriberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSbSubscriberId.setStatus("current")
_EnmsSbName_Type = DisplayString
_EnmsSbName_Object = MibTableColumn
enmsSbName = _EnmsSbName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 1, 1, 2),
    _EnmsSbName_Type()
)
enmsSbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSbName.setStatus("current")
_EnmsSbOrganisation_Type = DisplayString
_EnmsSbOrganisation_Object = MibTableColumn
enmsSbOrganisation = _EnmsSbOrganisation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 1, 1, 3),
    _EnmsSbOrganisation_Type()
)
enmsSbOrganisation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSbOrganisation.setStatus("current")
_EnmsSbContactPerson_Type = DisplayString
_EnmsSbContactPerson_Object = MibTableColumn
enmsSbContactPerson = _EnmsSbContactPerson_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 1, 1, 4),
    _EnmsSbContactPerson_Type()
)
enmsSbContactPerson.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSbContactPerson.setStatus("current")
_EnmsSbAddress_Type = DisplayString
_EnmsSbAddress_Object = MibTableColumn
enmsSbAddress = _EnmsSbAddress_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 1, 1, 5),
    _EnmsSbAddress_Type()
)
enmsSbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSbAddress.setStatus("current")
_EnmsSbPhone_Type = DisplayString
_EnmsSbPhone_Object = MibTableColumn
enmsSbPhone = _EnmsSbPhone_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 1, 1, 6),
    _EnmsSbPhone_Type()
)
enmsSbPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSbPhone.setStatus("current")
_EnmsSbFax_Type = DisplayString
_EnmsSbFax_Object = MibTableColumn
enmsSbFax = _EnmsSbFax_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 1, 1, 7),
    _EnmsSbFax_Type()
)
enmsSbFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSbFax.setStatus("current")
_EnmsSbEMail_Type = DisplayString
_EnmsSbEMail_Object = MibTableColumn
enmsSbEMail = _EnmsSbEMail_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 1, 1, 8),
    _EnmsSbEMail_Type()
)
enmsSbEMail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSbEMail.setStatus("current")
_EnmsSbURL_Type = DisplayString
_EnmsSbURL_Object = MibTableColumn
enmsSbURL = _EnmsSbURL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 1, 1, 9),
    _EnmsSbURL_Type()
)
enmsSbURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSbURL.setStatus("current")
_EnmsSbExternalReference_Type = DisplayString
_EnmsSbExternalReference_Object = MibTableColumn
enmsSbExternalReference = _EnmsSbExternalReference_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 1, 1, 10),
    _EnmsSbExternalReference_Type()
)
enmsSbExternalReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSbExternalReference.setStatus("current")
_EnmsServiceTable_Object = MibTable
enmsServiceTable = _EnmsServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 2)
)
if mibBuilder.loadTexts:
    enmsServiceTable.setStatus("current")
_EnmsServiceEntry_Object = MibTableRow
enmsServiceEntry = _EnmsServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 2, 1)
)
enmsServiceEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsSvServiceId"),
)
if mibBuilder.loadTexts:
    enmsServiceEntry.setStatus("current")
_EnmsSvServiceId_Type = ServiceId
_EnmsSvServiceId_Object = MibTableColumn
enmsSvServiceId = _EnmsSvServiceId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 2, 1, 1),
    _EnmsSvServiceId_Type()
)
enmsSvServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSvServiceId.setStatus("current")
_EnmsSvSubscriberId_Type = SubscriberId
_EnmsSvSubscriberId_Object = MibTableColumn
enmsSvSubscriberId = _EnmsSvSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 2, 1, 2),
    _EnmsSvSubscriberId_Type()
)
enmsSvSubscriberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSvSubscriberId.setStatus("current")
_EnmsSvLabel_Type = DisplayString
_EnmsSvLabel_Object = MibTableColumn
enmsSvLabel = _EnmsSvLabel_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 2, 1, 3),
    _EnmsSvLabel_Type()
)
enmsSvLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSvLabel.setStatus("current")
_EnmsSvOpState_Type = OperationalState
_EnmsSvOpState_Object = MibTableColumn
enmsSvOpState = _EnmsSvOpState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 2, 1, 4),
    _EnmsSvOpState_Type()
)
enmsSvOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSvOpState.setStatus("current")
_EnmsSvAdminState_Type = AdministrativeState
_EnmsSvAdminState_Object = MibTableColumn
enmsSvAdminState = _EnmsSvAdminState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 2, 1, 5),
    _EnmsSvAdminState_Type()
)
enmsSvAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSvAdminState.setStatus("current")
_EnmsSvDirection_Type = Directionality
_EnmsSvDirection_Object = MibTableColumn
enmsSvDirection = _EnmsSvDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 2, 1, 6),
    _EnmsSvDirection_Type()
)
enmsSvDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSvDirection.setStatus("obsolete")
_EnmsSvProtectionFlag_Type = Boolean
_EnmsSvProtectionFlag_Object = MibTableColumn
enmsSvProtectionFlag = _EnmsSvProtectionFlag_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 2, 1, 7),
    _EnmsSvProtectionFlag_Type()
)
enmsSvProtectionFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSvProtectionFlag.setStatus("obsolete")
_EnmsSvWriteProtected_Type = Boolean
_EnmsSvWriteProtected_Object = MibTableColumn
enmsSvWriteProtected = _EnmsSvWriteProtected_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 2, 1, 8),
    _EnmsSvWriteProtected_Type()
)
enmsSvWriteProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSvWriteProtected.setStatus("obsolete")
_EnmsSvServiceOwnerId_Type = ServiceId
_EnmsSvServiceOwnerId_Object = MibTableColumn
enmsSvServiceOwnerId = _EnmsSvServiceOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 2, 2, 1, 9),
    _EnmsSvServiceOwnerId_Type()
)
enmsSvServiceOwnerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSvServiceOwnerId.setStatus("current")
_EnmsAlarmTables_ObjectIdentity = ObjectIdentity
enmsAlarmTables = _EnmsAlarmTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3)
)
_EnmsAlarmTable_Object = MibTable
enmsAlarmTable = _EnmsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1)
)
if mibBuilder.loadTexts:
    enmsAlarmTable.setStatus("current")
_EnmsAlarmEntry_Object = MibTableRow
enmsAlarmEntry = _EnmsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1)
)
enmsAlarmEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsAlAlarmNumber"),
)
if mibBuilder.loadTexts:
    enmsAlarmEntry.setStatus("current")
_EnmsAlAlarmNumber_Type = Integer32
_EnmsAlAlarmNumber_Object = MibTableColumn
enmsAlAlarmNumber = _EnmsAlAlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 1),
    _EnmsAlAlarmNumber_Type()
)
enmsAlAlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlAlarmNumber.setStatus("current")
_EnmsAlSeverity_Type = PerceivedSeverity
_EnmsAlSeverity_Object = MibTableColumn
enmsAlSeverity = _EnmsAlSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 2),
    _EnmsAlSeverity_Type()
)
enmsAlSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlSeverity.setStatus("current")
_EnmsAlProbableCause_Type = ProbableCause
_EnmsAlProbableCause_Object = MibTableColumn
enmsAlProbableCause = _EnmsAlProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 3),
    _EnmsAlProbableCause_Type()
)
enmsAlProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlProbableCause.setStatus("current")
_EnmsAlClass_Type = AlarmClass
_EnmsAlClass_Object = MibTableColumn
enmsAlClass = _EnmsAlClass_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 4),
    _EnmsAlClass_Type()
)
enmsAlClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlClass.setStatus("current")
_EnmsAlServiceAffect_Type = Boolean
_EnmsAlServiceAffect_Object = MibTableColumn
enmsAlServiceAffect = _EnmsAlServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 5),
    _EnmsAlServiceAffect_Type()
)
enmsAlServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlServiceAffect.setStatus("current")
_EnmsAlState_Type = AlarmState
_EnmsAlState_Object = MibTableColumn
enmsAlState = _EnmsAlState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 6),
    _EnmsAlState_Type()
)
enmsAlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlState.setStatus("current")
_EnmsAlTimeStampFromNE_Type = Boolean
_EnmsAlTimeStampFromNE_Object = MibTableColumn
enmsAlTimeStampFromNE = _EnmsAlTimeStampFromNE_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 7),
    _EnmsAlTimeStampFromNE_Type()
)
enmsAlTimeStampFromNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlTimeStampFromNE.setStatus("current")
_EnmsAlTimeStamp_Type = EnmsTimeStamp
_EnmsAlTimeStamp_Object = MibTableColumn
enmsAlTimeStamp = _EnmsAlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 8),
    _EnmsAlTimeStamp_Type()
)
enmsAlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlTimeStamp.setStatus("current")
_EnmsAlEntityString_Type = DisplayString
_EnmsAlEntityString_Object = MibTableColumn
enmsAlEntityString = _EnmsAlEntityString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 9),
    _EnmsAlEntityString_Type()
)
enmsAlEntityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlEntityString.setStatus("current")
_EnmsAlEntityType_Type = EntityType
_EnmsAlEntityType_Object = MibTableColumn
enmsAlEntityType = _EnmsAlEntityType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 10),
    _EnmsAlEntityType_Type()
)
enmsAlEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlEntityType.setStatus("current")
_EnmsAlNEId_Type = NEId
_EnmsAlNEId_Object = MibTableColumn
enmsAlNEId = _EnmsAlNEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 11),
    _EnmsAlNEId_Type()
)
enmsAlNEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlNEId.setStatus("current")
_EnmsAlPortId_Type = PortId
_EnmsAlPortId_Object = MibTableColumn
enmsAlPortId = _EnmsAlPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 12),
    _EnmsAlPortId_Type()
)
enmsAlPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlPortId.setStatus("current")
_EnmsAlTPIdH_Type = TPId
_EnmsAlTPIdH_Object = MibTableColumn
enmsAlTPIdH = _EnmsAlTPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 13),
    _EnmsAlTPIdH_Type()
)
enmsAlTPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlTPIdH.setStatus("current")
_EnmsAlTPIdL_Type = TPId
_EnmsAlTPIdL_Object = MibTableColumn
enmsAlTPIdL = _EnmsAlTPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 14),
    _EnmsAlTPIdL_Type()
)
enmsAlTPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlTPIdL.setStatus("current")
_EnmsAlTPName_Type = DisplayString
_EnmsAlTPName_Object = MibTableColumn
enmsAlTPName = _EnmsAlTPName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 15),
    _EnmsAlTPName_Type()
)
enmsAlTPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlTPName.setStatus("current")
_EnmsAlModuleId_Type = ModuleId
_EnmsAlModuleId_Object = MibTableColumn
enmsAlModuleId = _EnmsAlModuleId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 16),
    _EnmsAlModuleId_Type()
)
enmsAlModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlModuleId.setStatus("current")
_EnmsAlProbableCauseString_Type = DisplayString
_EnmsAlProbableCauseString_Object = MibTableColumn
enmsAlProbableCauseString = _EnmsAlProbableCauseString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 17),
    _EnmsAlProbableCauseString_Type()
)
enmsAlProbableCauseString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlProbableCauseString.setStatus("current")
_EnmsAlNELocation_Type = DisplayString
_EnmsAlNELocation_Object = MibTableColumn
enmsAlNELocation = _EnmsAlNELocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 18),
    _EnmsAlNELocation_Type()
)
enmsAlNELocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlNELocation.setStatus("current")
_EnmsAlAffectedLocation_Type = DisplayString
_EnmsAlAffectedLocation_Object = MibTableColumn
enmsAlAffectedLocation = _EnmsAlAffectedLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 19),
    _EnmsAlAffectedLocation_Type()
)
enmsAlAffectedLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlAffectedLocation.setStatus("current")
_EnmsAlTrafficDirection_Type = TrafficDirection
_EnmsAlTrafficDirection_Object = MibTableColumn
enmsAlTrafficDirection = _EnmsAlTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 20),
    _EnmsAlTrafficDirection_Type()
)
enmsAlTrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlTrafficDirection.setStatus("current")
_EnmsAlAdditionalInformation_Type = DisplayString
_EnmsAlAdditionalInformation_Object = MibTableColumn
enmsAlAdditionalInformation = _EnmsAlAdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 21),
    _EnmsAlAdditionalInformation_Type()
)
enmsAlAdditionalInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlAdditionalInformation.setStatus("current")
_EnmsAlNeSystemContainer_Type = DisplayString
_EnmsAlNeSystemContainer_Object = MibTableColumn
enmsAlNeSystemContainer = _EnmsAlNeSystemContainer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 1, 1, 22),
    _EnmsAlNeSystemContainer_Type()
)
enmsAlNeSystemContainer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsAlNeSystemContainer.setStatus("current")
_EnmsAlarmsForNETable_Object = MibTable
enmsAlarmsForNETable = _EnmsAlarmsForNETable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2)
)
if mibBuilder.loadTexts:
    enmsAlarmsForNETable.setStatus("current")
_EnmsAlarmsForNEEntry_Object = MibTableRow
enmsAlarmsForNEEntry = _EnmsAlarmsForNEEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1)
)
enmsAlarmsForNEEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsA2NEId"),
    (0, "TNMS-NBI-MIB", "enmsA2Severity"),
    (0, "TNMS-NBI-MIB", "enmsA2AlarmNumber"),
)
if mibBuilder.loadTexts:
    enmsAlarmsForNEEntry.setStatus("current")
_EnmsA2NEId_Type = NEId
_EnmsA2NEId_Object = MibTableColumn
enmsA2NEId = _EnmsA2NEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 1),
    _EnmsA2NEId_Type()
)
enmsA2NEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2NEId.setStatus("current")
_EnmsA2Severity_Type = PerceivedSeverity
_EnmsA2Severity_Object = MibTableColumn
enmsA2Severity = _EnmsA2Severity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 2),
    _EnmsA2Severity_Type()
)
enmsA2Severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2Severity.setStatus("current")
_EnmsA2AlarmNumber_Type = Integer32
_EnmsA2AlarmNumber_Object = MibTableColumn
enmsA2AlarmNumber = _EnmsA2AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 3),
    _EnmsA2AlarmNumber_Type()
)
enmsA2AlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2AlarmNumber.setStatus("current")
_EnmsA2ProbableCause_Type = ProbableCause
_EnmsA2ProbableCause_Object = MibTableColumn
enmsA2ProbableCause = _EnmsA2ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 4),
    _EnmsA2ProbableCause_Type()
)
enmsA2ProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2ProbableCause.setStatus("current")
_EnmsA2Class_Type = AlarmClass
_EnmsA2Class_Object = MibTableColumn
enmsA2Class = _EnmsA2Class_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 5),
    _EnmsA2Class_Type()
)
enmsA2Class.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2Class.setStatus("current")
_EnmsA2ServiceAffect_Type = Boolean
_EnmsA2ServiceAffect_Object = MibTableColumn
enmsA2ServiceAffect = _EnmsA2ServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 6),
    _EnmsA2ServiceAffect_Type()
)
enmsA2ServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2ServiceAffect.setStatus("current")
_EnmsA2State_Type = AlarmState
_EnmsA2State_Object = MibTableColumn
enmsA2State = _EnmsA2State_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 7),
    _EnmsA2State_Type()
)
enmsA2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2State.setStatus("current")
_EnmsA2TimeStampFromNE_Type = Boolean
_EnmsA2TimeStampFromNE_Object = MibTableColumn
enmsA2TimeStampFromNE = _EnmsA2TimeStampFromNE_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 8),
    _EnmsA2TimeStampFromNE_Type()
)
enmsA2TimeStampFromNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2TimeStampFromNE.setStatus("current")
_EnmsA2TimeStamp_Type = EnmsTimeStamp
_EnmsA2TimeStamp_Object = MibTableColumn
enmsA2TimeStamp = _EnmsA2TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 9),
    _EnmsA2TimeStamp_Type()
)
enmsA2TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2TimeStamp.setStatus("current")
_EnmsA2EntityString_Type = DisplayString
_EnmsA2EntityString_Object = MibTableColumn
enmsA2EntityString = _EnmsA2EntityString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 10),
    _EnmsA2EntityString_Type()
)
enmsA2EntityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2EntityString.setStatus("current")
_EnmsA2EntityType_Type = EntityType
_EnmsA2EntityType_Object = MibTableColumn
enmsA2EntityType = _EnmsA2EntityType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 11),
    _EnmsA2EntityType_Type()
)
enmsA2EntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2EntityType.setStatus("current")
_EnmsA2PortId_Type = PortId
_EnmsA2PortId_Object = MibTableColumn
enmsA2PortId = _EnmsA2PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 12),
    _EnmsA2PortId_Type()
)
enmsA2PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2PortId.setStatus("current")
_EnmsA2TPIdH_Type = TPId
_EnmsA2TPIdH_Object = MibTableColumn
enmsA2TPIdH = _EnmsA2TPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 13),
    _EnmsA2TPIdH_Type()
)
enmsA2TPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2TPIdH.setStatus("current")
_EnmsA2TPIdL_Type = TPId
_EnmsA2TPIdL_Object = MibTableColumn
enmsA2TPIdL = _EnmsA2TPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 14),
    _EnmsA2TPIdL_Type()
)
enmsA2TPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2TPIdL.setStatus("current")
_EnmsA2TPName_Type = DisplayString
_EnmsA2TPName_Object = MibTableColumn
enmsA2TPName = _EnmsA2TPName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 15),
    _EnmsA2TPName_Type()
)
enmsA2TPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2TPName.setStatus("current")
_EnmsA2ModuleId_Type = ModuleId
_EnmsA2ModuleId_Object = MibTableColumn
enmsA2ModuleId = _EnmsA2ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 16),
    _EnmsA2ModuleId_Type()
)
enmsA2ModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2ModuleId.setStatus("current")
_EnmsA2ProbableCauseString_Type = DisplayString
_EnmsA2ProbableCauseString_Object = MibTableColumn
enmsA2ProbableCauseString = _EnmsA2ProbableCauseString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 17),
    _EnmsA2ProbableCauseString_Type()
)
enmsA2ProbableCauseString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2ProbableCauseString.setStatus("current")
_EnmsA2NELocation_Type = DisplayString
_EnmsA2NELocation_Object = MibTableColumn
enmsA2NELocation = _EnmsA2NELocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 18),
    _EnmsA2NELocation_Type()
)
enmsA2NELocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2NELocation.setStatus("current")
_EnmsA2AffectedLocation_Type = DisplayString
_EnmsA2AffectedLocation_Object = MibTableColumn
enmsA2AffectedLocation = _EnmsA2AffectedLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 19),
    _EnmsA2AffectedLocation_Type()
)
enmsA2AffectedLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2AffectedLocation.setStatus("current")
_EnmsA2TrafficDirection_Type = TrafficDirection
_EnmsA2TrafficDirection_Object = MibTableColumn
enmsA2TrafficDirection = _EnmsA2TrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 20),
    _EnmsA2TrafficDirection_Type()
)
enmsA2TrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2TrafficDirection.setStatus("current")
_EnmsA2AdditionalInformation_Type = DisplayString
_EnmsA2AdditionalInformation_Object = MibTableColumn
enmsA2AdditionalInformation = _EnmsA2AdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 21),
    _EnmsA2AdditionalInformation_Type()
)
enmsA2AdditionalInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2AdditionalInformation.setStatus("current")
_EnmsA2NeSystemContainer_Type = DisplayString
_EnmsA2NeSystemContainer_Object = MibTableColumn
enmsA2NeSystemContainer = _EnmsA2NeSystemContainer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 2, 1, 22),
    _EnmsA2NeSystemContainer_Type()
)
enmsA2NeSystemContainer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA2NeSystemContainer.setStatus("current")
_EnmsAlarmsForPortTable_Object = MibTable
enmsAlarmsForPortTable = _EnmsAlarmsForPortTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3)
)
if mibBuilder.loadTexts:
    enmsAlarmsForPortTable.setStatus("current")
_EnmsAlarmsForPortEntry_Object = MibTableRow
enmsAlarmsForPortEntry = _EnmsAlarmsForPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1)
)
enmsAlarmsForPortEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsA3NEId"),
    (0, "TNMS-NBI-MIB", "enmsA3PortId"),
    (0, "TNMS-NBI-MIB", "enmsA3Severity"),
    (0, "TNMS-NBI-MIB", "enmsA3AlarmNumber"),
)
if mibBuilder.loadTexts:
    enmsAlarmsForPortEntry.setStatus("current")
_EnmsA3NEId_Type = NEId
_EnmsA3NEId_Object = MibTableColumn
enmsA3NEId = _EnmsA3NEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 1),
    _EnmsA3NEId_Type()
)
enmsA3NEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3NEId.setStatus("current")
_EnmsA3PortId_Type = PortId
_EnmsA3PortId_Object = MibTableColumn
enmsA3PortId = _EnmsA3PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 2),
    _EnmsA3PortId_Type()
)
enmsA3PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3PortId.setStatus("current")
_EnmsA3Severity_Type = PerceivedSeverity
_EnmsA3Severity_Object = MibTableColumn
enmsA3Severity = _EnmsA3Severity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 3),
    _EnmsA3Severity_Type()
)
enmsA3Severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3Severity.setStatus("current")
_EnmsA3AlarmNumber_Type = Integer32
_EnmsA3AlarmNumber_Object = MibTableColumn
enmsA3AlarmNumber = _EnmsA3AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 4),
    _EnmsA3AlarmNumber_Type()
)
enmsA3AlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3AlarmNumber.setStatus("current")
_EnmsA3ProbableCause_Type = ProbableCause
_EnmsA3ProbableCause_Object = MibTableColumn
enmsA3ProbableCause = _EnmsA3ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 5),
    _EnmsA3ProbableCause_Type()
)
enmsA3ProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3ProbableCause.setStatus("current")
_EnmsA3Class_Type = AlarmClass
_EnmsA3Class_Object = MibTableColumn
enmsA3Class = _EnmsA3Class_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 6),
    _EnmsA3Class_Type()
)
enmsA3Class.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3Class.setStatus("current")
_EnmsA3ServiceAffect_Type = Boolean
_EnmsA3ServiceAffect_Object = MibTableColumn
enmsA3ServiceAffect = _EnmsA3ServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 7),
    _EnmsA3ServiceAffect_Type()
)
enmsA3ServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3ServiceAffect.setStatus("current")
_EnmsA3State_Type = AlarmState
_EnmsA3State_Object = MibTableColumn
enmsA3State = _EnmsA3State_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 8),
    _EnmsA3State_Type()
)
enmsA3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3State.setStatus("current")
_EnmsA3TimeStampFromNE_Type = Boolean
_EnmsA3TimeStampFromNE_Object = MibTableColumn
enmsA3TimeStampFromNE = _EnmsA3TimeStampFromNE_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 9),
    _EnmsA3TimeStampFromNE_Type()
)
enmsA3TimeStampFromNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3TimeStampFromNE.setStatus("current")
_EnmsA3TimeStamp_Type = EnmsTimeStamp
_EnmsA3TimeStamp_Object = MibTableColumn
enmsA3TimeStamp = _EnmsA3TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 10),
    _EnmsA3TimeStamp_Type()
)
enmsA3TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3TimeStamp.setStatus("current")
_EnmsA3EntityString_Type = DisplayString
_EnmsA3EntityString_Object = MibTableColumn
enmsA3EntityString = _EnmsA3EntityString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 11),
    _EnmsA3EntityString_Type()
)
enmsA3EntityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3EntityString.setStatus("current")
_EnmsA3EntityType_Type = EntityType
_EnmsA3EntityType_Object = MibTableColumn
enmsA3EntityType = _EnmsA3EntityType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 12),
    _EnmsA3EntityType_Type()
)
enmsA3EntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3EntityType.setStatus("current")
_EnmsA3TPIdH_Type = TPId
_EnmsA3TPIdH_Object = MibTableColumn
enmsA3TPIdH = _EnmsA3TPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 13),
    _EnmsA3TPIdH_Type()
)
enmsA3TPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3TPIdH.setStatus("current")
_EnmsA3TPIdL_Type = TPId
_EnmsA3TPIdL_Object = MibTableColumn
enmsA3TPIdL = _EnmsA3TPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 14),
    _EnmsA3TPIdL_Type()
)
enmsA3TPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3TPIdL.setStatus("current")
_EnmsA3TPName_Type = DisplayString
_EnmsA3TPName_Object = MibTableColumn
enmsA3TPName = _EnmsA3TPName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 15),
    _EnmsA3TPName_Type()
)
enmsA3TPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3TPName.setStatus("current")
_EnmsA3ProbableCauseString_Type = DisplayString
_EnmsA3ProbableCauseString_Object = MibTableColumn
enmsA3ProbableCauseString = _EnmsA3ProbableCauseString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 16),
    _EnmsA3ProbableCauseString_Type()
)
enmsA3ProbableCauseString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3ProbableCauseString.setStatus("current")
_EnmsA3NELocation_Type = DisplayString
_EnmsA3NELocation_Object = MibTableColumn
enmsA3NELocation = _EnmsA3NELocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 17),
    _EnmsA3NELocation_Type()
)
enmsA3NELocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3NELocation.setStatus("current")
_EnmsA3AffectedLocation_Type = DisplayString
_EnmsA3AffectedLocation_Object = MibTableColumn
enmsA3AffectedLocation = _EnmsA3AffectedLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 18),
    _EnmsA3AffectedLocation_Type()
)
enmsA3AffectedLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3AffectedLocation.setStatus("current")
_EnmsA3TrafficDirection_Type = TrafficDirection
_EnmsA3TrafficDirection_Object = MibTableColumn
enmsA3TrafficDirection = _EnmsA3TrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 19),
    _EnmsA3TrafficDirection_Type()
)
enmsA3TrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3TrafficDirection.setStatus("current")
_EnmsA3AdditionalInformation_Type = DisplayString
_EnmsA3AdditionalInformation_Object = MibTableColumn
enmsA3AdditionalInformation = _EnmsA3AdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 20),
    _EnmsA3AdditionalInformation_Type()
)
enmsA3AdditionalInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3AdditionalInformation.setStatus("current")
_EnmsA3NeSystemContainer_Type = DisplayString
_EnmsA3NeSystemContainer_Object = MibTableColumn
enmsA3NeSystemContainer = _EnmsA3NeSystemContainer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 3, 1, 21),
    _EnmsA3NeSystemContainer_Type()
)
enmsA3NeSystemContainer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA3NeSystemContainer.setStatus("current")
_EnmsAlarmsForTPTable_Object = MibTable
enmsAlarmsForTPTable = _EnmsAlarmsForTPTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4)
)
if mibBuilder.loadTexts:
    enmsAlarmsForTPTable.setStatus("current")
_EnmsAlarmsForTPEntry_Object = MibTableRow
enmsAlarmsForTPEntry = _EnmsAlarmsForTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1)
)
enmsAlarmsForTPEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsA4NEId"),
    (0, "TNMS-NBI-MIB", "enmsA4PortId"),
    (0, "TNMS-NBI-MIB", "enmsA4TPIdH"),
    (0, "TNMS-NBI-MIB", "enmsA4TPIdL"),
    (0, "TNMS-NBI-MIB", "enmsA4Severity"),
    (0, "TNMS-NBI-MIB", "enmsA4AlarmNumber"),
)
if mibBuilder.loadTexts:
    enmsAlarmsForTPEntry.setStatus("current")
_EnmsA4NEId_Type = NEId
_EnmsA4NEId_Object = MibTableColumn
enmsA4NEId = _EnmsA4NEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 1),
    _EnmsA4NEId_Type()
)
enmsA4NEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4NEId.setStatus("current")
_EnmsA4PortId_Type = PortId
_EnmsA4PortId_Object = MibTableColumn
enmsA4PortId = _EnmsA4PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 2),
    _EnmsA4PortId_Type()
)
enmsA4PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4PortId.setStatus("current")
_EnmsA4TPIdH_Type = TPId
_EnmsA4TPIdH_Object = MibTableColumn
enmsA4TPIdH = _EnmsA4TPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 3),
    _EnmsA4TPIdH_Type()
)
enmsA4TPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4TPIdH.setStatus("current")
_EnmsA4TPIdL_Type = TPId
_EnmsA4TPIdL_Object = MibTableColumn
enmsA4TPIdL = _EnmsA4TPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 4),
    _EnmsA4TPIdL_Type()
)
enmsA4TPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4TPIdL.setStatus("current")
_EnmsA4Severity_Type = PerceivedSeverity
_EnmsA4Severity_Object = MibTableColumn
enmsA4Severity = _EnmsA4Severity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 5),
    _EnmsA4Severity_Type()
)
enmsA4Severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4Severity.setStatus("current")
_EnmsA4AlarmNumber_Type = Integer32
_EnmsA4AlarmNumber_Object = MibTableColumn
enmsA4AlarmNumber = _EnmsA4AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 6),
    _EnmsA4AlarmNumber_Type()
)
enmsA4AlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4AlarmNumber.setStatus("current")
_EnmsA4ProbableCause_Type = ProbableCause
_EnmsA4ProbableCause_Object = MibTableColumn
enmsA4ProbableCause = _EnmsA4ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 7),
    _EnmsA4ProbableCause_Type()
)
enmsA4ProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4ProbableCause.setStatus("current")
_EnmsA4Class_Type = AlarmClass
_EnmsA4Class_Object = MibTableColumn
enmsA4Class = _EnmsA4Class_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 8),
    _EnmsA4Class_Type()
)
enmsA4Class.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4Class.setStatus("current")
_EnmsA4ServiceAffect_Type = Boolean
_EnmsA4ServiceAffect_Object = MibTableColumn
enmsA4ServiceAffect = _EnmsA4ServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 9),
    _EnmsA4ServiceAffect_Type()
)
enmsA4ServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4ServiceAffect.setStatus("current")
_EnmsA4State_Type = AlarmState
_EnmsA4State_Object = MibTableColumn
enmsA4State = _EnmsA4State_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 10),
    _EnmsA4State_Type()
)
enmsA4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4State.setStatus("current")
_EnmsA4TimeStampFromNE_Type = Boolean
_EnmsA4TimeStampFromNE_Object = MibTableColumn
enmsA4TimeStampFromNE = _EnmsA4TimeStampFromNE_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 11),
    _EnmsA4TimeStampFromNE_Type()
)
enmsA4TimeStampFromNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4TimeStampFromNE.setStatus("current")
_EnmsA4TimeStamp_Type = EnmsTimeStamp
_EnmsA4TimeStamp_Object = MibTableColumn
enmsA4TimeStamp = _EnmsA4TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 12),
    _EnmsA4TimeStamp_Type()
)
enmsA4TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4TimeStamp.setStatus("current")
_EnmsA4EntityString_Type = DisplayString
_EnmsA4EntityString_Object = MibTableColumn
enmsA4EntityString = _EnmsA4EntityString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 13),
    _EnmsA4EntityString_Type()
)
enmsA4EntityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4EntityString.setStatus("current")
_EnmsA4EntityType_Type = EntityType
_EnmsA4EntityType_Object = MibTableColumn
enmsA4EntityType = _EnmsA4EntityType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 14),
    _EnmsA4EntityType_Type()
)
enmsA4EntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4EntityType.setStatus("current")
_EnmsA4TPName_Type = DisplayString
_EnmsA4TPName_Object = MibTableColumn
enmsA4TPName = _EnmsA4TPName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 15),
    _EnmsA4TPName_Type()
)
enmsA4TPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4TPName.setStatus("current")
_EnmsA4ProbableCauseString_Type = DisplayString
_EnmsA4ProbableCauseString_Object = MibTableColumn
enmsA4ProbableCauseString = _EnmsA4ProbableCauseString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 16),
    _EnmsA4ProbableCauseString_Type()
)
enmsA4ProbableCauseString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4ProbableCauseString.setStatus("current")
_EnmsA4NELocation_Type = DisplayString
_EnmsA4NELocation_Object = MibTableColumn
enmsA4NELocation = _EnmsA4NELocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 17),
    _EnmsA4NELocation_Type()
)
enmsA4NELocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4NELocation.setStatus("current")
_EnmsA4AffectedLocation_Type = DisplayString
_EnmsA4AffectedLocation_Object = MibTableColumn
enmsA4AffectedLocation = _EnmsA4AffectedLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 18),
    _EnmsA4AffectedLocation_Type()
)
enmsA4AffectedLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4AffectedLocation.setStatus("current")
_EnmsA4TrafficDirection_Type = TrafficDirection
_EnmsA4TrafficDirection_Object = MibTableColumn
enmsA4TrafficDirection = _EnmsA4TrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 19),
    _EnmsA4TrafficDirection_Type()
)
enmsA4TrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4TrafficDirection.setStatus("current")
_EnmsA4AdditionalInformation_Type = DisplayString
_EnmsA4AdditionalInformation_Object = MibTableColumn
enmsA4AdditionalInformation = _EnmsA4AdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 20),
    _EnmsA4AdditionalInformation_Type()
)
enmsA4AdditionalInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4AdditionalInformation.setStatus("current")
_EnmsA4NeSystemContainer_Type = DisplayString
_EnmsA4NeSystemContainer_Object = MibTableColumn
enmsA4NeSystemContainer = _EnmsA4NeSystemContainer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 4, 1, 21),
    _EnmsA4NeSystemContainer_Type()
)
enmsA4NeSystemContainer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA4NeSystemContainer.setStatus("current")
_EnmsAlarmsForPortConnTable_Object = MibTable
enmsAlarmsForPortConnTable = _EnmsAlarmsForPortConnTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5)
)
if mibBuilder.loadTexts:
    enmsAlarmsForPortConnTable.setStatus("current")
_EnmsAlarmsForPortConnEntry_Object = MibTableRow
enmsAlarmsForPortConnEntry = _EnmsAlarmsForPortConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1)
)
enmsAlarmsForPortConnEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsA5PortConnId"),
    (0, "TNMS-NBI-MIB", "enmsA5Severity"),
    (0, "TNMS-NBI-MIB", "enmsA5AlarmNumber"),
)
if mibBuilder.loadTexts:
    enmsAlarmsForPortConnEntry.setStatus("current")
_EnmsA5PortConnId_Type = PortConnId
_EnmsA5PortConnId_Object = MibTableColumn
enmsA5PortConnId = _EnmsA5PortConnId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 1),
    _EnmsA5PortConnId_Type()
)
enmsA5PortConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5PortConnId.setStatus("current")
_EnmsA5Severity_Type = PerceivedSeverity
_EnmsA5Severity_Object = MibTableColumn
enmsA5Severity = _EnmsA5Severity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 2),
    _EnmsA5Severity_Type()
)
enmsA5Severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5Severity.setStatus("current")
_EnmsA5AlarmNumber_Type = Integer32
_EnmsA5AlarmNumber_Object = MibTableColumn
enmsA5AlarmNumber = _EnmsA5AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 3),
    _EnmsA5AlarmNumber_Type()
)
enmsA5AlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5AlarmNumber.setStatus("current")
_EnmsA5ProbableCause_Type = ProbableCause
_EnmsA5ProbableCause_Object = MibTableColumn
enmsA5ProbableCause = _EnmsA5ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 4),
    _EnmsA5ProbableCause_Type()
)
enmsA5ProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5ProbableCause.setStatus("current")
_EnmsA5Class_Type = AlarmClass
_EnmsA5Class_Object = MibTableColumn
enmsA5Class = _EnmsA5Class_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 5),
    _EnmsA5Class_Type()
)
enmsA5Class.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5Class.setStatus("current")
_EnmsA5ServiceAffect_Type = Boolean
_EnmsA5ServiceAffect_Object = MibTableColumn
enmsA5ServiceAffect = _EnmsA5ServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 6),
    _EnmsA5ServiceAffect_Type()
)
enmsA5ServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5ServiceAffect.setStatus("current")
_EnmsA5State_Type = AlarmState
_EnmsA5State_Object = MibTableColumn
enmsA5State = _EnmsA5State_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 7),
    _EnmsA5State_Type()
)
enmsA5State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5State.setStatus("current")
_EnmsA5TimeStampFromNE_Type = Boolean
_EnmsA5TimeStampFromNE_Object = MibTableColumn
enmsA5TimeStampFromNE = _EnmsA5TimeStampFromNE_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 8),
    _EnmsA5TimeStampFromNE_Type()
)
enmsA5TimeStampFromNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5TimeStampFromNE.setStatus("current")
_EnmsA5TimeStamp_Type = EnmsTimeStamp
_EnmsA5TimeStamp_Object = MibTableColumn
enmsA5TimeStamp = _EnmsA5TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 9),
    _EnmsA5TimeStamp_Type()
)
enmsA5TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5TimeStamp.setStatus("current")
_EnmsA5EntityString_Type = DisplayString
_EnmsA5EntityString_Object = MibTableColumn
enmsA5EntityString = _EnmsA5EntityString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 10),
    _EnmsA5EntityString_Type()
)
enmsA5EntityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5EntityString.setStatus("current")
_EnmsA5EntityType_Type = EntityType
_EnmsA5EntityType_Object = MibTableColumn
enmsA5EntityType = _EnmsA5EntityType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 11),
    _EnmsA5EntityType_Type()
)
enmsA5EntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5EntityType.setStatus("current")
_EnmsA5NEId_Type = NEId
_EnmsA5NEId_Object = MibTableColumn
enmsA5NEId = _EnmsA5NEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 12),
    _EnmsA5NEId_Type()
)
enmsA5NEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5NEId.setStatus("current")
_EnmsA5PortId_Type = PortId
_EnmsA5PortId_Object = MibTableColumn
enmsA5PortId = _EnmsA5PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 13),
    _EnmsA5PortId_Type()
)
enmsA5PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5PortId.setStatus("current")
_EnmsA5TPIdH_Type = TPId
_EnmsA5TPIdH_Object = MibTableColumn
enmsA5TPIdH = _EnmsA5TPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 14),
    _EnmsA5TPIdH_Type()
)
enmsA5TPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5TPIdH.setStatus("obsolete")
_EnmsA5TPIdL_Type = TPId
_EnmsA5TPIdL_Object = MibTableColumn
enmsA5TPIdL = _EnmsA5TPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 15),
    _EnmsA5TPIdL_Type()
)
enmsA5TPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5TPIdL.setStatus("obsolete")
_EnmsA5TPName_Type = DisplayString
_EnmsA5TPName_Object = MibTableColumn
enmsA5TPName = _EnmsA5TPName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 16),
    _EnmsA5TPName_Type()
)
enmsA5TPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5TPName.setStatus("obsolete")
_EnmsA5ModuleId_Type = ModuleId
_EnmsA5ModuleId_Object = MibTableColumn
enmsA5ModuleId = _EnmsA5ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 17),
    _EnmsA5ModuleId_Type()
)
enmsA5ModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5ModuleId.setStatus("current")
_EnmsA5ProbableCauseString_Type = DisplayString
_EnmsA5ProbableCauseString_Object = MibTableColumn
enmsA5ProbableCauseString = _EnmsA5ProbableCauseString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 18),
    _EnmsA5ProbableCauseString_Type()
)
enmsA5ProbableCauseString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5ProbableCauseString.setStatus("current")
_EnmsA5NELocation_Type = DisplayString
_EnmsA5NELocation_Object = MibTableColumn
enmsA5NELocation = _EnmsA5NELocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 19),
    _EnmsA5NELocation_Type()
)
enmsA5NELocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5NELocation.setStatus("current")
_EnmsA5AffectedLocation_Type = DisplayString
_EnmsA5AffectedLocation_Object = MibTableColumn
enmsA5AffectedLocation = _EnmsA5AffectedLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 20),
    _EnmsA5AffectedLocation_Type()
)
enmsA5AffectedLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5AffectedLocation.setStatus("current")
_EnmsA5TrafficDirection_Type = TrafficDirection
_EnmsA5TrafficDirection_Object = MibTableColumn
enmsA5TrafficDirection = _EnmsA5TrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 21),
    _EnmsA5TrafficDirection_Type()
)
enmsA5TrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5TrafficDirection.setStatus("current")
_EnmsA5AdditionalInformation_Type = DisplayString
_EnmsA5AdditionalInformation_Object = MibTableColumn
enmsA5AdditionalInformation = _EnmsA5AdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 5, 1, 22),
    _EnmsA5AdditionalInformation_Type()
)
enmsA5AdditionalInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA5AdditionalInformation.setStatus("current")
_EnmsAlarmsForSNCTable_Object = MibTable
enmsAlarmsForSNCTable = _EnmsAlarmsForSNCTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6)
)
if mibBuilder.loadTexts:
    enmsAlarmsForSNCTable.setStatus("current")
_EnmsAlarmsForSNCEntry_Object = MibTableRow
enmsAlarmsForSNCEntry = _EnmsAlarmsForSNCEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1)
)
enmsAlarmsForSNCEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsA6SNCId"),
    (0, "TNMS-NBI-MIB", "enmsA6Severity"),
    (0, "TNMS-NBI-MIB", "enmsA6AlarmNumber"),
)
if mibBuilder.loadTexts:
    enmsAlarmsForSNCEntry.setStatus("current")
_EnmsA6SNCId_Type = SNCId
_EnmsA6SNCId_Object = MibTableColumn
enmsA6SNCId = _EnmsA6SNCId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 1),
    _EnmsA6SNCId_Type()
)
enmsA6SNCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6SNCId.setStatus("current")
_EnmsA6Severity_Type = PerceivedSeverity
_EnmsA6Severity_Object = MibTableColumn
enmsA6Severity = _EnmsA6Severity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 2),
    _EnmsA6Severity_Type()
)
enmsA6Severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6Severity.setStatus("current")
_EnmsA6AlarmNumber_Type = Integer32
_EnmsA6AlarmNumber_Object = MibTableColumn
enmsA6AlarmNumber = _EnmsA6AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 3),
    _EnmsA6AlarmNumber_Type()
)
enmsA6AlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6AlarmNumber.setStatus("current")
_EnmsA6ProbableCause_Type = ProbableCause
_EnmsA6ProbableCause_Object = MibTableColumn
enmsA6ProbableCause = _EnmsA6ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 4),
    _EnmsA6ProbableCause_Type()
)
enmsA6ProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6ProbableCause.setStatus("current")
_EnmsA6Class_Type = AlarmClass
_EnmsA6Class_Object = MibTableColumn
enmsA6Class = _EnmsA6Class_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 5),
    _EnmsA6Class_Type()
)
enmsA6Class.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6Class.setStatus("current")
_EnmsA6ServiceAffect_Type = Boolean
_EnmsA6ServiceAffect_Object = MibTableColumn
enmsA6ServiceAffect = _EnmsA6ServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 6),
    _EnmsA6ServiceAffect_Type()
)
enmsA6ServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6ServiceAffect.setStatus("current")
_EnmsA6State_Type = AlarmState
_EnmsA6State_Object = MibTableColumn
enmsA6State = _EnmsA6State_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 7),
    _EnmsA6State_Type()
)
enmsA6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6State.setStatus("current")
_EnmsA6TimeStampFromNE_Type = Boolean
_EnmsA6TimeStampFromNE_Object = MibTableColumn
enmsA6TimeStampFromNE = _EnmsA6TimeStampFromNE_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 8),
    _EnmsA6TimeStampFromNE_Type()
)
enmsA6TimeStampFromNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6TimeStampFromNE.setStatus("current")
_EnmsA6TimeStamp_Type = EnmsTimeStamp
_EnmsA6TimeStamp_Object = MibTableColumn
enmsA6TimeStamp = _EnmsA6TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 9),
    _EnmsA6TimeStamp_Type()
)
enmsA6TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6TimeStamp.setStatus("current")
_EnmsA6EntityString_Type = DisplayString
_EnmsA6EntityString_Object = MibTableColumn
enmsA6EntityString = _EnmsA6EntityString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 10),
    _EnmsA6EntityString_Type()
)
enmsA6EntityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6EntityString.setStatus("current")
_EnmsA6EntityType_Type = EntityType
_EnmsA6EntityType_Object = MibTableColumn
enmsA6EntityType = _EnmsA6EntityType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 11),
    _EnmsA6EntityType_Type()
)
enmsA6EntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6EntityType.setStatus("current")
_EnmsA6NEId_Type = NEId
_EnmsA6NEId_Object = MibTableColumn
enmsA6NEId = _EnmsA6NEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 12),
    _EnmsA6NEId_Type()
)
enmsA6NEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6NEId.setStatus("current")
_EnmsA6PortId_Type = PortId
_EnmsA6PortId_Object = MibTableColumn
enmsA6PortId = _EnmsA6PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 13),
    _EnmsA6PortId_Type()
)
enmsA6PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6PortId.setStatus("current")
_EnmsA6TPIdH_Type = TPId
_EnmsA6TPIdH_Object = MibTableColumn
enmsA6TPIdH = _EnmsA6TPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 14),
    _EnmsA6TPIdH_Type()
)
enmsA6TPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6TPIdH.setStatus("current")
_EnmsA6TPIdL_Type = TPId
_EnmsA6TPIdL_Object = MibTableColumn
enmsA6TPIdL = _EnmsA6TPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 15),
    _EnmsA6TPIdL_Type()
)
enmsA6TPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6TPIdL.setStatus("current")
_EnmsA6TPName_Type = DisplayString
_EnmsA6TPName_Object = MibTableColumn
enmsA6TPName = _EnmsA6TPName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 16),
    _EnmsA6TPName_Type()
)
enmsA6TPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6TPName.setStatus("current")
_EnmsA6ModuleId_Type = ModuleId
_EnmsA6ModuleId_Object = MibTableColumn
enmsA6ModuleId = _EnmsA6ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 17),
    _EnmsA6ModuleId_Type()
)
enmsA6ModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6ModuleId.setStatus("current")
_EnmsA6ProbableCauseString_Type = DisplayString
_EnmsA6ProbableCauseString_Object = MibTableColumn
enmsA6ProbableCauseString = _EnmsA6ProbableCauseString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 18),
    _EnmsA6ProbableCauseString_Type()
)
enmsA6ProbableCauseString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6ProbableCauseString.setStatus("current")
_EnmsA6NELocation_Type = DisplayString
_EnmsA6NELocation_Object = MibTableColumn
enmsA6NELocation = _EnmsA6NELocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 19),
    _EnmsA6NELocation_Type()
)
enmsA6NELocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6NELocation.setStatus("current")
_EnmsA6AffectedLocation_Type = DisplayString
_EnmsA6AffectedLocation_Object = MibTableColumn
enmsA6AffectedLocation = _EnmsA6AffectedLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 20),
    _EnmsA6AffectedLocation_Type()
)
enmsA6AffectedLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6AffectedLocation.setStatus("current")
_EnmsA6TrafficDirection_Type = TrafficDirection
_EnmsA6TrafficDirection_Object = MibTableColumn
enmsA6TrafficDirection = _EnmsA6TrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 21),
    _EnmsA6TrafficDirection_Type()
)
enmsA6TrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6TrafficDirection.setStatus("current")
_EnmsA6AdditionalInformation_Type = DisplayString
_EnmsA6AdditionalInformation_Object = MibTableColumn
enmsA6AdditionalInformation = _EnmsA6AdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 6, 1, 22),
    _EnmsA6AdditionalInformation_Type()
)
enmsA6AdditionalInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA6AdditionalInformation.setStatus("current")
_EnmsAlarmsForServiceTable_Object = MibTable
enmsAlarmsForServiceTable = _EnmsAlarmsForServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7)
)
if mibBuilder.loadTexts:
    enmsAlarmsForServiceTable.setStatus("current")
_EnmsAlarmsForServiceEntry_Object = MibTableRow
enmsAlarmsForServiceEntry = _EnmsAlarmsForServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1)
)
enmsAlarmsForServiceEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsA7ServiceId"),
    (0, "TNMS-NBI-MIB", "enmsA7Severity"),
    (0, "TNMS-NBI-MIB", "enmsA7AlarmNumber"),
)
if mibBuilder.loadTexts:
    enmsAlarmsForServiceEntry.setStatus("current")
_EnmsA7ServiceId_Type = ServiceId
_EnmsA7ServiceId_Object = MibTableColumn
enmsA7ServiceId = _EnmsA7ServiceId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 1),
    _EnmsA7ServiceId_Type()
)
enmsA7ServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7ServiceId.setStatus("current")
_EnmsA7Severity_Type = PerceivedSeverity
_EnmsA7Severity_Object = MibTableColumn
enmsA7Severity = _EnmsA7Severity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 2),
    _EnmsA7Severity_Type()
)
enmsA7Severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7Severity.setStatus("current")
_EnmsA7AlarmNumber_Type = Integer32
_EnmsA7AlarmNumber_Object = MibTableColumn
enmsA7AlarmNumber = _EnmsA7AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 3),
    _EnmsA7AlarmNumber_Type()
)
enmsA7AlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7AlarmNumber.setStatus("current")
_EnmsA7ProbableCause_Type = ProbableCause
_EnmsA7ProbableCause_Object = MibTableColumn
enmsA7ProbableCause = _EnmsA7ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 4),
    _EnmsA7ProbableCause_Type()
)
enmsA7ProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7ProbableCause.setStatus("current")
_EnmsA7Class_Type = AlarmClass
_EnmsA7Class_Object = MibTableColumn
enmsA7Class = _EnmsA7Class_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 5),
    _EnmsA7Class_Type()
)
enmsA7Class.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7Class.setStatus("current")
_EnmsA7ServiceAffect_Type = Boolean
_EnmsA7ServiceAffect_Object = MibTableColumn
enmsA7ServiceAffect = _EnmsA7ServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 6),
    _EnmsA7ServiceAffect_Type()
)
enmsA7ServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7ServiceAffect.setStatus("current")
_EnmsA7State_Type = AlarmState
_EnmsA7State_Object = MibTableColumn
enmsA7State = _EnmsA7State_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 7),
    _EnmsA7State_Type()
)
enmsA7State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7State.setStatus("current")
_EnmsA7TimeStampFromNE_Type = Boolean
_EnmsA7TimeStampFromNE_Object = MibTableColumn
enmsA7TimeStampFromNE = _EnmsA7TimeStampFromNE_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 8),
    _EnmsA7TimeStampFromNE_Type()
)
enmsA7TimeStampFromNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7TimeStampFromNE.setStatus("current")
_EnmsA7TimeStamp_Type = EnmsTimeStamp
_EnmsA7TimeStamp_Object = MibTableColumn
enmsA7TimeStamp = _EnmsA7TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 9),
    _EnmsA7TimeStamp_Type()
)
enmsA7TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7TimeStamp.setStatus("current")
_EnmsA7EntityString_Type = DisplayString
_EnmsA7EntityString_Object = MibTableColumn
enmsA7EntityString = _EnmsA7EntityString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 10),
    _EnmsA7EntityString_Type()
)
enmsA7EntityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7EntityString.setStatus("current")
_EnmsA7EntityType_Type = EntityType
_EnmsA7EntityType_Object = MibTableColumn
enmsA7EntityType = _EnmsA7EntityType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 11),
    _EnmsA7EntityType_Type()
)
enmsA7EntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7EntityType.setStatus("current")
_EnmsA7NEId_Type = NEId
_EnmsA7NEId_Object = MibTableColumn
enmsA7NEId = _EnmsA7NEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 12),
    _EnmsA7NEId_Type()
)
enmsA7NEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7NEId.setStatus("current")
_EnmsA7PortId_Type = PortId
_EnmsA7PortId_Object = MibTableColumn
enmsA7PortId = _EnmsA7PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 13),
    _EnmsA7PortId_Type()
)
enmsA7PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7PortId.setStatus("current")
_EnmsA7TPIdH_Type = TPId
_EnmsA7TPIdH_Object = MibTableColumn
enmsA7TPIdH = _EnmsA7TPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 14),
    _EnmsA7TPIdH_Type()
)
enmsA7TPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7TPIdH.setStatus("current")
_EnmsA7TPIdL_Type = TPId
_EnmsA7TPIdL_Object = MibTableColumn
enmsA7TPIdL = _EnmsA7TPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 15),
    _EnmsA7TPIdL_Type()
)
enmsA7TPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7TPIdL.setStatus("current")
_EnmsA7TPName_Type = DisplayString
_EnmsA7TPName_Object = MibTableColumn
enmsA7TPName = _EnmsA7TPName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 16),
    _EnmsA7TPName_Type()
)
enmsA7TPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7TPName.setStatus("current")
_EnmsA7ModuleId_Type = ModuleId
_EnmsA7ModuleId_Object = MibTableColumn
enmsA7ModuleId = _EnmsA7ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 17),
    _EnmsA7ModuleId_Type()
)
enmsA7ModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7ModuleId.setStatus("current")
_EnmsA7ProbableCauseString_Type = DisplayString
_EnmsA7ProbableCauseString_Object = MibTableColumn
enmsA7ProbableCauseString = _EnmsA7ProbableCauseString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 18),
    _EnmsA7ProbableCauseString_Type()
)
enmsA7ProbableCauseString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7ProbableCauseString.setStatus("current")
_EnmsA7NELocation_Type = DisplayString
_EnmsA7NELocation_Object = MibTableColumn
enmsA7NELocation = _EnmsA7NELocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 19),
    _EnmsA7NELocation_Type()
)
enmsA7NELocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7NELocation.setStatus("current")
_EnmsA7AffectedLocation_Type = DisplayString
_EnmsA7AffectedLocation_Object = MibTableColumn
enmsA7AffectedLocation = _EnmsA7AffectedLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 20),
    _EnmsA7AffectedLocation_Type()
)
enmsA7AffectedLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7AffectedLocation.setStatus("current")
_EnmsA7TrafficDirection_Type = TrafficDirection
_EnmsA7TrafficDirection_Object = MibTableColumn
enmsA7TrafficDirection = _EnmsA7TrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 21),
    _EnmsA7TrafficDirection_Type()
)
enmsA7TrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7TrafficDirection.setStatus("current")
_EnmsA7AdditionalInformation_Type = DisplayString
_EnmsA7AdditionalInformation_Object = MibTableColumn
enmsA7AdditionalInformation = _EnmsA7AdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 7, 1, 22),
    _EnmsA7AdditionalInformation_Type()
)
enmsA7AdditionalInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA7AdditionalInformation.setStatus("current")
_EnmsAlarmsForModuleTable_Object = MibTable
enmsAlarmsForModuleTable = _EnmsAlarmsForModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8)
)
if mibBuilder.loadTexts:
    enmsAlarmsForModuleTable.setStatus("current")
_EnmsAlarmsForModuleEntry_Object = MibTableRow
enmsAlarmsForModuleEntry = _EnmsAlarmsForModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1)
)
enmsAlarmsForModuleEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsA8NEId"),
    (0, "TNMS-NBI-MIB", "enmsA8ModuleId"),
    (0, "TNMS-NBI-MIB", "enmsA8Severity"),
    (0, "TNMS-NBI-MIB", "enmsA8AlarmNumber"),
)
if mibBuilder.loadTexts:
    enmsAlarmsForModuleEntry.setStatus("current")
_EnmsA8NEId_Type = NEId
_EnmsA8NEId_Object = MibTableColumn
enmsA8NEId = _EnmsA8NEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 1),
    _EnmsA8NEId_Type()
)
enmsA8NEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8NEId.setStatus("current")
_EnmsA8ModuleId_Type = ModuleId
_EnmsA8ModuleId_Object = MibTableColumn
enmsA8ModuleId = _EnmsA8ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 2),
    _EnmsA8ModuleId_Type()
)
enmsA8ModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8ModuleId.setStatus("current")
_EnmsA8Severity_Type = PerceivedSeverity
_EnmsA8Severity_Object = MibTableColumn
enmsA8Severity = _EnmsA8Severity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 3),
    _EnmsA8Severity_Type()
)
enmsA8Severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8Severity.setStatus("current")
_EnmsA8AlarmNumber_Type = Integer32
_EnmsA8AlarmNumber_Object = MibTableColumn
enmsA8AlarmNumber = _EnmsA8AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 4),
    _EnmsA8AlarmNumber_Type()
)
enmsA8AlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8AlarmNumber.setStatus("current")
_EnmsA8ProbableCause_Type = ProbableCause
_EnmsA8ProbableCause_Object = MibTableColumn
enmsA8ProbableCause = _EnmsA8ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 5),
    _EnmsA8ProbableCause_Type()
)
enmsA8ProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8ProbableCause.setStatus("current")
_EnmsA8Class_Type = AlarmClass
_EnmsA8Class_Object = MibTableColumn
enmsA8Class = _EnmsA8Class_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 6),
    _EnmsA8Class_Type()
)
enmsA8Class.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8Class.setStatus("current")
_EnmsA8ServiceAffect_Type = Boolean
_EnmsA8ServiceAffect_Object = MibTableColumn
enmsA8ServiceAffect = _EnmsA8ServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 7),
    _EnmsA8ServiceAffect_Type()
)
enmsA8ServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8ServiceAffect.setStatus("current")
_EnmsA8State_Type = AlarmState
_EnmsA8State_Object = MibTableColumn
enmsA8State = _EnmsA8State_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 8),
    _EnmsA8State_Type()
)
enmsA8State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8State.setStatus("current")
_EnmsA8TimeStampFromNE_Type = Boolean
_EnmsA8TimeStampFromNE_Object = MibTableColumn
enmsA8TimeStampFromNE = _EnmsA8TimeStampFromNE_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 9),
    _EnmsA8TimeStampFromNE_Type()
)
enmsA8TimeStampFromNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8TimeStampFromNE.setStatus("current")
_EnmsA8TimeStamp_Type = EnmsTimeStamp
_EnmsA8TimeStamp_Object = MibTableColumn
enmsA8TimeStamp = _EnmsA8TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 10),
    _EnmsA8TimeStamp_Type()
)
enmsA8TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8TimeStamp.setStatus("current")
_EnmsA8EntityString_Type = DisplayString
_EnmsA8EntityString_Object = MibTableColumn
enmsA8EntityString = _EnmsA8EntityString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 11),
    _EnmsA8EntityString_Type()
)
enmsA8EntityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8EntityString.setStatus("current")
_EnmsA8EntityType_Type = EntityType
_EnmsA8EntityType_Object = MibTableColumn
enmsA8EntityType = _EnmsA8EntityType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 12),
    _EnmsA8EntityType_Type()
)
enmsA8EntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8EntityType.setStatus("current")
_EnmsA8PortId_Type = PortId
_EnmsA8PortId_Object = MibTableColumn
enmsA8PortId = _EnmsA8PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 13),
    _EnmsA8PortId_Type()
)
enmsA8PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8PortId.setStatus("obsolete")
_EnmsA8TPIdH_Type = TPId
_EnmsA8TPIdH_Object = MibTableColumn
enmsA8TPIdH = _EnmsA8TPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 14),
    _EnmsA8TPIdH_Type()
)
enmsA8TPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8TPIdH.setStatus("obsolete")
_EnmsA8TPIdL_Type = TPId
_EnmsA8TPIdL_Object = MibTableColumn
enmsA8TPIdL = _EnmsA8TPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 15),
    _EnmsA8TPIdL_Type()
)
enmsA8TPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8TPIdL.setStatus("obsolete")
_EnmsA8TPName_Type = DisplayString
_EnmsA8TPName_Object = MibTableColumn
enmsA8TPName = _EnmsA8TPName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 16),
    _EnmsA8TPName_Type()
)
enmsA8TPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8TPName.setStatus("obsolete")
_EnmsA8ProbableCauseString_Type = DisplayString
_EnmsA8ProbableCauseString_Object = MibTableColumn
enmsA8ProbableCauseString = _EnmsA8ProbableCauseString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 17),
    _EnmsA8ProbableCauseString_Type()
)
enmsA8ProbableCauseString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8ProbableCauseString.setStatus("current")
_EnmsA8NELocation_Type = DisplayString
_EnmsA8NELocation_Object = MibTableColumn
enmsA8NELocation = _EnmsA8NELocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 18),
    _EnmsA8NELocation_Type()
)
enmsA8NELocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8NELocation.setStatus("current")
_EnmsA8AffectedLocation_Type = DisplayString
_EnmsA8AffectedLocation_Object = MibTableColumn
enmsA8AffectedLocation = _EnmsA8AffectedLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 19),
    _EnmsA8AffectedLocation_Type()
)
enmsA8AffectedLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8AffectedLocation.setStatus("current")
_EnmsA8TrafficDirection_Type = TrafficDirection
_EnmsA8TrafficDirection_Object = MibTableColumn
enmsA8TrafficDirection = _EnmsA8TrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 20),
    _EnmsA8TrafficDirection_Type()
)
enmsA8TrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8TrafficDirection.setStatus("current")
_EnmsA8AdditionalInformation_Type = DisplayString
_EnmsA8AdditionalInformation_Object = MibTableColumn
enmsA8AdditionalInformation = _EnmsA8AdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 21),
    _EnmsA8AdditionalInformation_Type()
)
enmsA8AdditionalInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8AdditionalInformation.setStatus("current")
_EnmsA8NeSystemContainer_Type = DisplayString
_EnmsA8NeSystemContainer_Object = MibTableColumn
enmsA8NeSystemContainer = _EnmsA8NeSystemContainer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 8, 1, 22),
    _EnmsA8NeSystemContainer_Type()
)
enmsA8NeSystemContainer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA8NeSystemContainer.setStatus("current")
_EnmsAlarmsForEthernetPathTable_Object = MibTable
enmsAlarmsForEthernetPathTable = _EnmsAlarmsForEthernetPathTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9)
)
if mibBuilder.loadTexts:
    enmsAlarmsForEthernetPathTable.setStatus("current")
_EnmsAlarmsForEthernetPathEntry_Object = MibTableRow
enmsAlarmsForEthernetPathEntry = _EnmsAlarmsForEthernetPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1)
)
enmsAlarmsForEthernetPathEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsA9EthernetPathId"),
    (0, "TNMS-NBI-MIB", "enmsA9Severity"),
    (0, "TNMS-NBI-MIB", "enmsA9AlarmNumber"),
)
if mibBuilder.loadTexts:
    enmsAlarmsForEthernetPathEntry.setStatus("current")
_EnmsA9EthernetPathId_Type = EthernetPathId
_EnmsA9EthernetPathId_Object = MibTableColumn
enmsA9EthernetPathId = _EnmsA9EthernetPathId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 1),
    _EnmsA9EthernetPathId_Type()
)
enmsA9EthernetPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9EthernetPathId.setStatus("current")
_EnmsA9Severity_Type = PerceivedSeverity
_EnmsA9Severity_Object = MibTableColumn
enmsA9Severity = _EnmsA9Severity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 2),
    _EnmsA9Severity_Type()
)
enmsA9Severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9Severity.setStatus("current")
_EnmsA9AlarmNumber_Type = Integer32
_EnmsA9AlarmNumber_Object = MibTableColumn
enmsA9AlarmNumber = _EnmsA9AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 3),
    _EnmsA9AlarmNumber_Type()
)
enmsA9AlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9AlarmNumber.setStatus("current")
_EnmsA9ProbableCause_Type = ProbableCause
_EnmsA9ProbableCause_Object = MibTableColumn
enmsA9ProbableCause = _EnmsA9ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 4),
    _EnmsA9ProbableCause_Type()
)
enmsA9ProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9ProbableCause.setStatus("current")
_EnmsA9Class_Type = AlarmClass
_EnmsA9Class_Object = MibTableColumn
enmsA9Class = _EnmsA9Class_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 5),
    _EnmsA9Class_Type()
)
enmsA9Class.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9Class.setStatus("current")
_EnmsA9ServiceAffect_Type = Boolean
_EnmsA9ServiceAffect_Object = MibTableColumn
enmsA9ServiceAffect = _EnmsA9ServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 6),
    _EnmsA9ServiceAffect_Type()
)
enmsA9ServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9ServiceAffect.setStatus("current")
_EnmsA9State_Type = AlarmState
_EnmsA9State_Object = MibTableColumn
enmsA9State = _EnmsA9State_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 7),
    _EnmsA9State_Type()
)
enmsA9State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9State.setStatus("current")
_EnmsA9TimeStampFromNE_Type = Boolean
_EnmsA9TimeStampFromNE_Object = MibTableColumn
enmsA9TimeStampFromNE = _EnmsA9TimeStampFromNE_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 8),
    _EnmsA9TimeStampFromNE_Type()
)
enmsA9TimeStampFromNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9TimeStampFromNE.setStatus("current")
_EnmsA9TimeStamp_Type = EnmsTimeStamp
_EnmsA9TimeStamp_Object = MibTableColumn
enmsA9TimeStamp = _EnmsA9TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 9),
    _EnmsA9TimeStamp_Type()
)
enmsA9TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9TimeStamp.setStatus("current")
_EnmsA9EntityString_Type = DisplayString
_EnmsA9EntityString_Object = MibTableColumn
enmsA9EntityString = _EnmsA9EntityString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 10),
    _EnmsA9EntityString_Type()
)
enmsA9EntityString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9EntityString.setStatus("current")
_EnmsA9EntityType_Type = EntityType
_EnmsA9EntityType_Object = MibTableColumn
enmsA9EntityType = _EnmsA9EntityType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 11),
    _EnmsA9EntityType_Type()
)
enmsA9EntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9EntityType.setStatus("current")
_EnmsA9NEId_Type = NEId
_EnmsA9NEId_Object = MibTableColumn
enmsA9NEId = _EnmsA9NEId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 12),
    _EnmsA9NEId_Type()
)
enmsA9NEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9NEId.setStatus("current")
_EnmsA9PortId_Type = PortId
_EnmsA9PortId_Object = MibTableColumn
enmsA9PortId = _EnmsA9PortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 13),
    _EnmsA9PortId_Type()
)
enmsA9PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9PortId.setStatus("current")
_EnmsA9TPIdH_Type = TPId
_EnmsA9TPIdH_Object = MibTableColumn
enmsA9TPIdH = _EnmsA9TPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 14),
    _EnmsA9TPIdH_Type()
)
enmsA9TPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9TPIdH.setStatus("current")
_EnmsA9TPIdL_Type = TPId
_EnmsA9TPIdL_Object = MibTableColumn
enmsA9TPIdL = _EnmsA9TPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 15),
    _EnmsA9TPIdL_Type()
)
enmsA9TPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9TPIdL.setStatus("current")
_EnmsA9TPName_Type = DisplayString
_EnmsA9TPName_Object = MibTableColumn
enmsA9TPName = _EnmsA9TPName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 16),
    _EnmsA9TPName_Type()
)
enmsA9TPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9TPName.setStatus("current")
_EnmsA9ModuleId_Type = ModuleId
_EnmsA9ModuleId_Object = MibTableColumn
enmsA9ModuleId = _EnmsA9ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 17),
    _EnmsA9ModuleId_Type()
)
enmsA9ModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9ModuleId.setStatus("current")
_EnmsA9ProbableCauseString_Type = DisplayString
_EnmsA9ProbableCauseString_Object = MibTableColumn
enmsA9ProbableCauseString = _EnmsA9ProbableCauseString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 18),
    _EnmsA9ProbableCauseString_Type()
)
enmsA9ProbableCauseString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9ProbableCauseString.setStatus("current")
_EnmsA9NELocation_Type = DisplayString
_EnmsA9NELocation_Object = MibTableColumn
enmsA9NELocation = _EnmsA9NELocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 19),
    _EnmsA9NELocation_Type()
)
enmsA9NELocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9NELocation.setStatus("current")
_EnmsA9AffectedLocation_Type = DisplayString
_EnmsA9AffectedLocation_Object = MibTableColumn
enmsA9AffectedLocation = _EnmsA9AffectedLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 20),
    _EnmsA9AffectedLocation_Type()
)
enmsA9AffectedLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9AffectedLocation.setStatus("current")
_EnmsA9TrafficDirection_Type = TrafficDirection
_EnmsA9TrafficDirection_Object = MibTableColumn
enmsA9TrafficDirection = _EnmsA9TrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 21),
    _EnmsA9TrafficDirection_Type()
)
enmsA9TrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9TrafficDirection.setStatus("current")
_EnmsA9AdditionalInformation_Type = DisplayString
_EnmsA9AdditionalInformation_Object = MibTableColumn
enmsA9AdditionalInformation = _EnmsA9AdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 3, 9, 1, 22),
    _EnmsA9AdditionalInformation_Type()
)
enmsA9AdditionalInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsA9AdditionalInformation.setStatus("current")
_EnmsProxy_ObjectIdentity = ObjectIdentity
enmsProxy = _EnmsProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4)
)
_EnmsCounter_ObjectIdentity = ObjectIdentity
enmsCounter = _EnmsCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 1)
)
_EnmsSNMPTrapCnt_Type = Counter32
_EnmsSNMPTrapCnt_Object = MibScalar
enmsSNMPTrapCnt = _EnmsSNMPTrapCnt_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 1, 1),
    _EnmsSNMPTrapCnt_Type()
)
enmsSNMPTrapCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSNMPTrapCnt.setStatus("obsolete")
_EnmsSNMPGetCnt_Type = Counter32
_EnmsSNMPGetCnt_Object = MibScalar
enmsSNMPGetCnt = _EnmsSNMPGetCnt_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 1, 2),
    _EnmsSNMPGetCnt_Type()
)
enmsSNMPGetCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSNMPGetCnt.setStatus("obsolete")
_EnmsSNMPGetNextCnt_Type = Counter32
_EnmsSNMPGetNextCnt_Object = MibScalar
enmsSNMPGetNextCnt = _EnmsSNMPGetNextCnt_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 1, 3),
    _EnmsSNMPGetNextCnt_Type()
)
enmsSNMPGetNextCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSNMPGetNextCnt.setStatus("obsolete")
_EnmsSNMPSetCnt_Type = Counter32
_EnmsSNMPSetCnt_Object = MibScalar
enmsSNMPSetCnt = _EnmsSNMPSetCnt_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 1, 4),
    _EnmsSNMPSetCnt_Type()
)
enmsSNMPSetCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsSNMPSetCnt.setStatus("obsolete")
_EnmsControl_ObjectIdentity = ObjectIdentity
enmsControl = _EnmsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2)
)
_EnmsProxyName_Type = DisplayString
_EnmsProxyName_Object = MibScalar
enmsProxyName = _EnmsProxyName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2, 1),
    _EnmsProxyName_Type()
)
enmsProxyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsProxyName.setStatus("current")
_EnmsProxyOpState_Type = OperationalState
_EnmsProxyOpState_Object = MibScalar
enmsProxyOpState = _EnmsProxyOpState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2, 2),
    _EnmsProxyOpState_Type()
)
enmsProxyOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsProxyOpState.setStatus("current")
_EnmsNetworkName_Type = DisplayString
_EnmsNetworkName_Object = MibScalar
enmsNetworkName = _EnmsNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2, 3),
    _EnmsNetworkName_Type()
)
enmsNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsNetworkName.setStatus("current")
_EnmsTrapHistoryTableLength_Type = Integer32
_EnmsTrapHistoryTableLength_Object = MibScalar
enmsTrapHistoryTableLength = _EnmsTrapHistoryTableLength_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2, 4),
    _EnmsTrapHistoryTableLength_Type()
)
enmsTrapHistoryTableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsTrapHistoryTableLength.setStatus("current")
_EnmsTrapCounter_Type = Counter32
_EnmsTrapCounter_Object = MibScalar
enmsTrapCounter = _EnmsTrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2, 5),
    _EnmsTrapCounter_Type()
)
enmsTrapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapCounter.setStatus("current")
_EnmsProxyPSTAMP_Type = DisplayString
_EnmsProxyPSTAMP_Object = MibScalar
enmsProxyPSTAMP = _EnmsProxyPSTAMP_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2, 6),
    _EnmsProxyPSTAMP_Type()
)
enmsProxyPSTAMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsProxyPSTAMP.setStatus("current")
_EnmsEnterpriseId_Type = ObjectIdentifier
_EnmsEnterpriseId_Object = MibScalar
enmsEnterpriseId = _EnmsEnterpriseId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2, 7),
    _EnmsEnterpriseId_Type()
)
enmsEnterpriseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsEnterpriseId.setStatus("current")
_EnmsMIBVersion_Type = DisplayString
_EnmsMIBVersion_Object = MibScalar
enmsMIBVersion = _EnmsMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2, 8),
    _EnmsMIBVersion_Type()
)
enmsMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsMIBVersion.setStatus("current")
_EnmsEMSVersion_Type = DisplayString
_EnmsEMSVersion_Object = MibScalar
enmsEMSVersion = _EnmsEMSVersion_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2, 9),
    _EnmsEMSVersion_Type()
)
enmsEMSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsEMSVersion.setStatus("current")
_EnmsTimeStampFormat_Type = DisplayString
_EnmsTimeStampFormat_Object = MibScalar
enmsTimeStampFormat = _EnmsTimeStampFormat_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2, 10),
    _EnmsTimeStampFormat_Type()
)
enmsTimeStampFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTimeStampFormat.setStatus("current")
_EnmsHeartbeatInterval_Type = Integer32
_EnmsHeartbeatInterval_Object = MibScalar
enmsHeartbeatInterval = _EnmsHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2, 11),
    _EnmsHeartbeatInterval_Type()
)
enmsHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsHeartbeatInterval.setStatus("current")
_EnmsHeartbeatOpState_Type = OperationalState
_EnmsHeartbeatOpState_Object = MibScalar
enmsHeartbeatOpState = _EnmsHeartbeatOpState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2, 12),
    _EnmsHeartbeatOpState_Type()
)
enmsHeartbeatOpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsHeartbeatOpState.setStatus("current")
_EnmsInformTimeout_Type = Integer32
_EnmsInformTimeout_Object = MibScalar
enmsInformTimeout = _EnmsInformTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2, 13),
    _EnmsInformTimeout_Type()
)
enmsInformTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsInformTimeout.setStatus("current")
_EnmsInformMaxTries_Type = Integer32
_EnmsInformMaxTries_Object = MibScalar
enmsInformMaxTries = _EnmsInformMaxTries_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 4, 2, 14),
    _EnmsInformMaxTries_Type()
)
enmsInformMaxTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsInformMaxTries.setStatus("current")
_EnmsTrapGroup_ObjectIdentity = ObjectIdentity
enmsTrapGroup = _EnmsTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5)
)
_EnmsTrapHist_ObjectIdentity = ObjectIdentity
enmsTrapHist = _EnmsTrapHist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 1)
)
_EnmsTrapHistoryTable_Object = MibTable
enmsTrapHistoryTable = _EnmsTrapHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 1, 1)
)
if mibBuilder.loadTexts:
    enmsTrapHistoryTable.setStatus("current")
_EnmsTrapHistoryEntry_Object = MibTableRow
enmsTrapHistoryEntry = _EnmsTrapHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 1, 1, 1)
)
enmsTrapHistoryEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsHiTrapNumber"),
)
if mibBuilder.loadTexts:
    enmsTrapHistoryEntry.setStatus("current")
_EnmsHiTrapNumber_Type = Integer32
_EnmsHiTrapNumber_Object = MibTableColumn
enmsHiTrapNumber = _EnmsHiTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 1, 1, 1, 1),
    _EnmsHiTrapNumber_Type()
)
enmsHiTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsHiTrapNumber.setStatus("current")
_EnmsHiTrapEntityType_Type = EntityType
_EnmsHiTrapEntityType_Object = MibTableColumn
enmsHiTrapEntityType = _EnmsHiTrapEntityType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 1, 1, 1, 2),
    _EnmsHiTrapEntityType_Type()
)
enmsHiTrapEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsHiTrapEntityType.setStatus("current")
_EnmsHiTrapFirstId_Type = UniqueId
_EnmsHiTrapFirstId_Object = MibTableColumn
enmsHiTrapFirstId = _EnmsHiTrapFirstId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 1, 1, 1, 3),
    _EnmsHiTrapFirstId_Type()
)
enmsHiTrapFirstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsHiTrapFirstId.setStatus("current")
_EnmsHiTrapSecondId_Type = UniqueId
_EnmsHiTrapSecondId_Object = MibTableColumn
enmsHiTrapSecondId = _EnmsHiTrapSecondId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 1, 1, 1, 4),
    _EnmsHiTrapSecondId_Type()
)
enmsHiTrapSecondId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsHiTrapSecondId.setStatus("current")
_EnmsHiTrapTPIdH_Type = TPId
_EnmsHiTrapTPIdH_Object = MibTableColumn
enmsHiTrapTPIdH = _EnmsHiTrapTPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 1, 1, 1, 5),
    _EnmsHiTrapTPIdH_Type()
)
enmsHiTrapTPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsHiTrapTPIdH.setStatus("current")
_EnmsHiTrapTPIdL_Type = TPId
_EnmsHiTrapTPIdL_Object = MibTableColumn
enmsHiTrapTPIdL = _EnmsHiTrapTPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 1, 1, 1, 6),
    _EnmsHiTrapTPIdL_Type()
)
enmsHiTrapTPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsHiTrapTPIdL.setStatus("current")
_EnmsHiTrapNfyType_Type = NotificationType
_EnmsHiTrapNfyType_Object = MibTableColumn
enmsHiTrapNfyType = _EnmsHiTrapNfyType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 1, 1, 1, 7),
    _EnmsHiTrapNfyType_Type()
)
enmsHiTrapNfyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsHiTrapNfyType.setStatus("current")
_EnmsHiTrapCounter_Type = Counter32
_EnmsHiTrapCounter_Object = MibTableColumn
enmsHiTrapCounter = _EnmsHiTrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 1, 1, 1, 8),
    _EnmsHiTrapCounter_Type()
)
enmsHiTrapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsHiTrapCounter.setStatus("current")
_EnmsTrapVariable_ObjectIdentity = ObjectIdentity
enmsTrapVariable = _EnmsTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2)
)
_EnmsTrapTimeStamp_Type = EnmsTimeStamp
_EnmsTrapTimeStamp_Object = MibScalar
enmsTrapTimeStamp = _EnmsTrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 1),
    _EnmsTrapTimeStamp_Type()
)
enmsTrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapTimeStamp.setStatus("current")
_EnmsTrapEventSeverity_Type = PerceivedSeverity
_EnmsTrapEventSeverity_Object = MibScalar
enmsTrapEventSeverity = _EnmsTrapEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 2),
    _EnmsTrapEventSeverity_Type()
)
enmsTrapEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapEventSeverity.setStatus("current")
_EnmsTrapEventDetails_Type = DisplayString
_EnmsTrapEventDetails_Object = MibScalar
enmsTrapEventDetails = _EnmsTrapEventDetails_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 3),
    _EnmsTrapEventDetails_Type()
)
enmsTrapEventDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapEventDetails.setStatus("current")
_EnmsTrapEventProbableCause_Type = ProbableCause
_EnmsTrapEventProbableCause_Object = MibScalar
enmsTrapEventProbableCause = _EnmsTrapEventProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 4),
    _EnmsTrapEventProbableCause_Type()
)
enmsTrapEventProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapEventProbableCause.setStatus("current")


class _EnmsTrapStateName_Type(Integer32):
    """Custom type enmsTrapStateName based on Integer32"""
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
        *(("actualCreationState", 7),
          ("adminState", 2),
          ("communicationState", 10),
          ("opState", 1),
          ("opStateRX", 6),
          ("opStateTX", 5),
          ("protectionState", 9),
          ("requiredCreationState", 8),
          ("usageStateRX", 4),
          ("usageStateTX", 3))
    )


_EnmsTrapStateName_Type.__name__ = "Integer32"
_EnmsTrapStateName_Object = MibScalar
enmsTrapStateName = _EnmsTrapStateName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 5),
    _EnmsTrapStateName_Type()
)
enmsTrapStateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapStateName.setStatus("current")
_EnmsTrapStateOldValue_Type = Integer32
_EnmsTrapStateOldValue_Object = MibScalar
enmsTrapStateOldValue = _EnmsTrapStateOldValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 6),
    _EnmsTrapStateOldValue_Type()
)
enmsTrapStateOldValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapStateOldValue.setStatus("current")
_EnmsTrapStateNewValue_Type = Integer32
_EnmsTrapStateNewValue_Object = MibScalar
enmsTrapStateNewValue = _EnmsTrapStateNewValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 7),
    _EnmsTrapStateNewValue_Type()
)
enmsTrapStateNewValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapStateNewValue.setStatus("current")


class _EnmsTrapAttributeName_Type(Integer32):
    """Custom type enmsTrapAttributeName based on Integer32"""
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
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("accessState", 32),
          ("address", 24),
          ("alarmSeverity", 4),
          ("alarmState", 31),
          ("bandwidth", 12),
          ("bandwidthRequired", 47),
          ("bandwidthSink", 46),
          ("bandwidthSource", 45),
          ("canBroadcast", 6),
          ("canPathProtection", 7),
          ("contactPerson", 23),
          ("direction", 13),
          ("dstAlarmSeverity", 29),
          ("emAccessState", 33),
          ("email", 27),
          ("enmsNeUserText", 54),
          ("ethernetPathType", 52),
          ("fax", 26),
          ("hasPortconnection", 38),
          ("interfaceType", 11),
          ("label", 19),
          ("location", 3),
          ("moduleId", 17),
          ("name", 2),
          ("neClass", 8),
          ("neDCNLocation", 49),
          ("neIdName", 40),
          ("neState", 34),
          ("nxCount", 15),
          ("objectType", 48),
          ("operatingMode", 5),
          ("organisation", 22),
          ("ownerId", 39),
          ("phone", 25),
          ("protectionFlag", 20),
          ("protectionType", 41),
          ("provisioningState", 30),
          ("reliability", 18),
          ("serviceId", 53),
          ("serviceType", 10),
          ("srcAlarmSeverity", 28),
          ("subscriberId", 35),
          ("systemContainer", 50),
          ("technology", 9),
          ("terminType", 16),
          ("tpIndex", 14),
          ("type", 1),
          ("usageCountRX", 37),
          ("usageCountTX", 36),
          ("vLanId", 51),
          ("writeProtected", 21))
    )


_EnmsTrapAttributeName_Type.__name__ = "Integer32"
_EnmsTrapAttributeName_Object = MibScalar
enmsTrapAttributeName = _EnmsTrapAttributeName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 8),
    _EnmsTrapAttributeName_Type()
)
enmsTrapAttributeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapAttributeName.setStatus("current")
_EnmsTrapAttributeOldValue_Type = DisplayString
_EnmsTrapAttributeOldValue_Object = MibScalar
enmsTrapAttributeOldValue = _EnmsTrapAttributeOldValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 9),
    _EnmsTrapAttributeOldValue_Type()
)
enmsTrapAttributeOldValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapAttributeOldValue.setStatus("current")
_EnmsTrapAttributeNewValue_Type = DisplayString
_EnmsTrapAttributeNewValue_Object = MibScalar
enmsTrapAttributeNewValue = _EnmsTrapAttributeNewValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 10),
    _EnmsTrapAttributeNewValue_Type()
)
enmsTrapAttributeNewValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapAttributeNewValue.setStatus("current")
_EnmsTrapEventProbableCauseString_Type = DisplayString
_EnmsTrapEventProbableCauseString_Object = MibScalar
enmsTrapEventProbableCauseString = _EnmsTrapEventProbableCauseString_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 11),
    _EnmsTrapEventProbableCauseString_Type()
)
enmsTrapEventProbableCauseString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapEventProbableCauseString.setStatus("current")
_EnmsTrapNeIdName_Type = DisplayString
_EnmsTrapNeIdName_Object = MibScalar
enmsTrapNeIdName = _EnmsTrapNeIdName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 12),
    _EnmsTrapNeIdName_Type()
)
enmsTrapNeIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapNeIdName.setStatus("current")
_EnmsTrapNeLocationLct_Type = DisplayString
_EnmsTrapNeLocationLct_Object = MibScalar
enmsTrapNeLocationLct = _EnmsTrapNeLocationLct_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 13),
    _EnmsTrapNeLocationLct_Type()
)
enmsTrapNeLocationLct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapNeLocationLct.setStatus("current")
_EnmsTrapAffectedLocation_Type = DisplayString
_EnmsTrapAffectedLocation_Object = MibScalar
enmsTrapAffectedLocation = _EnmsTrapAffectedLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 14),
    _EnmsTrapAffectedLocation_Type()
)
enmsTrapAffectedLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapAffectedLocation.setStatus("current")
_EnmsTrapEventTrafficDirection_Type = DisplayString
_EnmsTrapEventTrafficDirection_Object = MibScalar
enmsTrapEventTrafficDirection = _EnmsTrapEventTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 2, 15),
    _EnmsTrapEventTrafficDirection_Type()
)
enmsTrapEventTrafficDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsTrapEventTrafficDirection.setStatus("current")
_EnmsTraps_ObjectIdentity = ObjectIdentity
enmsTraps = _EnmsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3)
)
_EnmsCommonTraps_ObjectIdentity = ObjectIdentity
enmsCommonTraps = _EnmsCommonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 1)
)
_EnmsNETraps_ObjectIdentity = ObjectIdentity
enmsNETraps = _EnmsNETraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 2)
)
_EnmsModuleTraps_ObjectIdentity = ObjectIdentity
enmsModuleTraps = _EnmsModuleTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 3)
)
_EnmsPortTraps_ObjectIdentity = ObjectIdentity
enmsPortTraps = _EnmsPortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 4)
)
_EnmsTPTraps_ObjectIdentity = ObjectIdentity
enmsTPTraps = _EnmsTPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 5)
)
_EnmsPortConnTraps_ObjectIdentity = ObjectIdentity
enmsPortConnTraps = _EnmsPortConnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 6)
)
_EnmsSNCTraps_ObjectIdentity = ObjectIdentity
enmsSNCTraps = _EnmsSNCTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 7)
)
_EnmsSubscriberTraps_ObjectIdentity = ObjectIdentity
enmsSubscriberTraps = _EnmsSubscriberTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 8)
)
_EnmsServiceTraps_ObjectIdentity = ObjectIdentity
enmsServiceTraps = _EnmsServiceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 9)
)
_EnmsEMSTraps_ObjectIdentity = ObjectIdentity
enmsEMSTraps = _EnmsEMSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 10)
)
_EnmsMonitorTraps_ObjectIdentity = ObjectIdentity
enmsMonitorTraps = _EnmsMonitorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 11)
)
_EnmsEthernetPathTraps_ObjectIdentity = ObjectIdentity
enmsEthernetPathTraps = _EnmsEthernetPathTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 12)
)
_EnmsPerfMonTraps_ObjectIdentity = ObjectIdentity
enmsPerfMonTraps = _EnmsPerfMonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 13)
)
_EnmsOptPowerMonTraps_ObjectIdentity = ObjectIdentity
enmsOptPowerMonTraps = _EnmsOptPowerMonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 14)
)
_EnmsTrapFilter_ObjectIdentity = ObjectIdentity
enmsTrapFilter = _EnmsTrapFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4)
)
_EnmsCommonTrapFilter_Type = TrapFilter
_EnmsCommonTrapFilter_Object = MibScalar
enmsCommonTrapFilter = _EnmsCommonTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 1),
    _EnmsCommonTrapFilter_Type()
)
enmsCommonTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsCommonTrapFilter.setStatus("current")
_EnmsNETrapFilter_Type = TrapFilter
_EnmsNETrapFilter_Object = MibScalar
enmsNETrapFilter = _EnmsNETrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 2),
    _EnmsNETrapFilter_Type()
)
enmsNETrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsNETrapFilter.setStatus("current")
_EnmsModuleTrapFilter_Type = TrapFilter
_EnmsModuleTrapFilter_Object = MibScalar
enmsModuleTrapFilter = _EnmsModuleTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 3),
    _EnmsModuleTrapFilter_Type()
)
enmsModuleTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsModuleTrapFilter.setStatus("current")
_EnmsPortTrapFilter_Type = TrapFilter
_EnmsPortTrapFilter_Object = MibScalar
enmsPortTrapFilter = _EnmsPortTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 4),
    _EnmsPortTrapFilter_Type()
)
enmsPortTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsPortTrapFilter.setStatus("current")
_EnmsTPTrapFilter_Type = TrapFilter
_EnmsTPTrapFilter_Object = MibScalar
enmsTPTrapFilter = _EnmsTPTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 5),
    _EnmsTPTrapFilter_Type()
)
enmsTPTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsTPTrapFilter.setStatus("current")
_EnmsPortConnTrapFilter_Type = TrapFilter
_EnmsPortConnTrapFilter_Object = MibScalar
enmsPortConnTrapFilter = _EnmsPortConnTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 6),
    _EnmsPortConnTrapFilter_Type()
)
enmsPortConnTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsPortConnTrapFilter.setStatus("current")
_EnmsSNCTrapFilter_Type = TrapFilter
_EnmsSNCTrapFilter_Object = MibScalar
enmsSNCTrapFilter = _EnmsSNCTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 7),
    _EnmsSNCTrapFilter_Type()
)
enmsSNCTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsSNCTrapFilter.setStatus("current")
_EnmsSubscriberTrapFilter_Type = TrapFilter
_EnmsSubscriberTrapFilter_Object = MibScalar
enmsSubscriberTrapFilter = _EnmsSubscriberTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 8),
    _EnmsSubscriberTrapFilter_Type()
)
enmsSubscriberTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsSubscriberTrapFilter.setStatus("current")
_EnmsServiceTrapFilter_Type = TrapFilter
_EnmsServiceTrapFilter_Object = MibScalar
enmsServiceTrapFilter = _EnmsServiceTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 9),
    _EnmsServiceTrapFilter_Type()
)
enmsServiceTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsServiceTrapFilter.setStatus("current")
_EnmsNEAlarmTrapFilter_Type = TrapFilter
_EnmsNEAlarmTrapFilter_Object = MibScalar
enmsNEAlarmTrapFilter = _EnmsNEAlarmTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 10),
    _EnmsNEAlarmTrapFilter_Type()
)
enmsNEAlarmTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsNEAlarmTrapFilter.setStatus("current")
_EnmsModuleAlarmTrapFilter_Type = TrapFilter
_EnmsModuleAlarmTrapFilter_Object = MibScalar
enmsModuleAlarmTrapFilter = _EnmsModuleAlarmTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 11),
    _EnmsModuleAlarmTrapFilter_Type()
)
enmsModuleAlarmTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsModuleAlarmTrapFilter.setStatus("current")
_EnmsPortAlarmTrapFilter_Type = TrapFilter
_EnmsPortAlarmTrapFilter_Object = MibScalar
enmsPortAlarmTrapFilter = _EnmsPortAlarmTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 12),
    _EnmsPortAlarmTrapFilter_Type()
)
enmsPortAlarmTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsPortAlarmTrapFilter.setStatus("current")
_EnmsTPAlarmTrapFilter_Type = TrapFilter
_EnmsTPAlarmTrapFilter_Object = MibScalar
enmsTPAlarmTrapFilter = _EnmsTPAlarmTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 13),
    _EnmsTPAlarmTrapFilter_Type()
)
enmsTPAlarmTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsTPAlarmTrapFilter.setStatus("current")
_EnmsEMSAlarmTrapFilter_Type = TrapFilter
_EnmsEMSAlarmTrapFilter_Object = MibScalar
enmsEMSAlarmTrapFilter = _EnmsEMSAlarmTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 14),
    _EnmsEMSAlarmTrapFilter_Type()
)
enmsEMSAlarmTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsEMSAlarmTrapFilter.setStatus("current")
_EnmsNeIdNameFilter_Type = TrapFilter
_EnmsNeIdNameFilter_Object = MibScalar
enmsNeIdNameFilter = _EnmsNeIdNameFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 15),
    _EnmsNeIdNameFilter_Type()
)
enmsNeIdNameFilter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enmsNeIdNameFilter.setStatus("current")
_EnmsMonitorTrapFilter_Type = TrapFilter
_EnmsMonitorTrapFilter_Object = MibScalar
enmsMonitorTrapFilter = _EnmsMonitorTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 16),
    _EnmsMonitorTrapFilter_Type()
)
enmsMonitorTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsMonitorTrapFilter.setStatus("current")
_EnmsEthernetPathTrapFilter_Type = TrapFilter
_EnmsEthernetPathTrapFilter_Object = MibScalar
enmsEthernetPathTrapFilter = _EnmsEthernetPathTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 17),
    _EnmsEthernetPathTrapFilter_Type()
)
enmsEthernetPathTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsEthernetPathTrapFilter.setStatus("current")
_EnmsPerfMonTrapFilter_Type = TrapFilter
_EnmsPerfMonTrapFilter_Object = MibScalar
enmsPerfMonTrapFilter = _EnmsPerfMonTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 18),
    _EnmsPerfMonTrapFilter_Type()
)
enmsPerfMonTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsPerfMonTrapFilter.setStatus("current")
_EnmsOptPowerMonTrapFilter_Type = TrapFilter
_EnmsOptPowerMonTrapFilter_Object = MibScalar
enmsOptPowerMonTrapFilter = _EnmsOptPowerMonTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 4, 19),
    _EnmsOptPowerMonTrapFilter_Type()
)
enmsOptPowerMonTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enmsOptPowerMonTrapFilter.setStatus("current")
_EnmsPerfMon_ObjectIdentity = ObjectIdentity
enmsPerfMon = _EnmsPerfMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6)
)
_EnmsPmRequestNextId_Type = PerfMonRequestId
_EnmsPmRequestNextId_Object = MibScalar
enmsPmRequestNextId = _EnmsPmRequestNextId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 1),
    _EnmsPmRequestNextId_Type()
)
enmsPmRequestNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmRequestNextId.setStatus("current")
_EnmsPerfMonRequestTable_Object = MibTable
enmsPerfMonRequestTable = _EnmsPerfMonRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 2)
)
if mibBuilder.loadTexts:
    enmsPerfMonRequestTable.setStatus("current")
_EnmsPerfMonRequestEntry_Object = MibTableRow
enmsPerfMonRequestEntry = _EnmsPerfMonRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 2, 1)
)
enmsPerfMonRequestEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsPmRequestId"),
)
if mibBuilder.loadTexts:
    enmsPerfMonRequestEntry.setStatus("current")
_EnmsPmRequestId_Type = PerfMonRequestId
_EnmsPmRequestId_Object = MibTableColumn
enmsPmRequestId = _EnmsPmRequestId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 2, 1, 1),
    _EnmsPmRequestId_Type()
)
enmsPmRequestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enmsPmRequestId.setStatus("current")
_EnmsPmRequestName_Type = DisplayString
_EnmsPmRequestName_Object = MibTableColumn
enmsPmRequestName = _EnmsPmRequestName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 2, 1, 2),
    _EnmsPmRequestName_Type()
)
enmsPmRequestName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsPmRequestName.setStatus("current")
_EnmsPmRequestRowStatus_Type = RowStatus
_EnmsPmRequestRowStatus_Object = MibTableColumn
enmsPmRequestRowStatus = _EnmsPmRequestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 2, 1, 3),
    _EnmsPmRequestRowStatus_Type()
)
enmsPmRequestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsPmRequestRowStatus.setStatus("current")
_EnmsPmRequestLastUpdate_Type = EnmsTimeStamp
_EnmsPmRequestLastUpdate_Object = MibTableColumn
enmsPmRequestLastUpdate = _EnmsPmRequestLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 2, 1, 4),
    _EnmsPmRequestLastUpdate_Type()
)
enmsPmRequestLastUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsPmRequestLastUpdate.setStatus("current")
_EnmsPmRequestInfo_Type = DisplayString
_EnmsPmRequestInfo_Object = MibTableColumn
enmsPmRequestInfo = _EnmsPmRequestInfo_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 2, 1, 5),
    _EnmsPmRequestInfo_Type()
)
enmsPmRequestInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsPmRequestInfo.setStatus("current")
_EnmsPmRequestState_Type = PerfMonRequestState
_EnmsPmRequestState_Object = MibTableColumn
enmsPmRequestState = _EnmsPmRequestState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 2, 1, 6),
    _EnmsPmRequestState_Type()
)
enmsPmRequestState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsPmRequestState.setStatus("current")
_EnmsPmRequestType_Type = PerfMonType
_EnmsPmRequestType_Object = MibTableColumn
enmsPmRequestType = _EnmsPmRequestType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 2, 1, 7),
    _EnmsPmRequestType_Type()
)
enmsPmRequestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsPmRequestType.setStatus("current")
_EnmsPmRequestStartTime_Type = EnmsTimeStamp
_EnmsPmRequestStartTime_Object = MibTableColumn
enmsPmRequestStartTime = _EnmsPmRequestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 2, 1, 8),
    _EnmsPmRequestStartTime_Type()
)
enmsPmRequestStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsPmRequestStartTime.setStatus("current")
_EnmsPmRequestEndTime_Type = EnmsTimeStamp
_EnmsPmRequestEndTime_Object = MibTableColumn
enmsPmRequestEndTime = _EnmsPmRequestEndTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 2, 1, 9),
    _EnmsPmRequestEndTime_Type()
)
enmsPmRequestEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsPmRequestEndTime.setStatus("current")
_EnmsPmRequestGranularity_Type = PerfMonGranularity
_EnmsPmRequestGranularity_Object = MibTableColumn
enmsPmRequestGranularity = _EnmsPmRequestGranularity_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 2, 1, 10),
    _EnmsPmRequestGranularity_Type()
)
enmsPmRequestGranularity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsPmRequestGranularity.setStatus("current")
_EnmsPmRequestFilterType_Type = FilterType
_EnmsPmRequestFilterType_Object = MibTableColumn
enmsPmRequestFilterType = _EnmsPmRequestFilterType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 2, 1, 11),
    _EnmsPmRequestFilterType_Type()
)
enmsPmRequestFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsPmRequestFilterType.setStatus("current")
_EnmsPmRequestFilterValue_Type = DisplayString
_EnmsPmRequestFilterValue_Object = MibTableColumn
enmsPmRequestFilterValue = _EnmsPmRequestFilterValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 2, 1, 12),
    _EnmsPmRequestFilterValue_Type()
)
enmsPmRequestFilterValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsPmRequestFilterValue.setStatus("current")
_EnmsPerfMonResultPmpTable_Object = MibTable
enmsPerfMonResultPmpTable = _EnmsPerfMonResultPmpTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3)
)
if mibBuilder.loadTexts:
    enmsPerfMonResultPmpTable.setStatus("current")
_EnmsPerfMonResultPmpEntry_Object = MibTableRow
enmsPerfMonResultPmpEntry = _EnmsPerfMonResultPmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1)
)
enmsPerfMonResultPmpEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsPmResultPmpReqId"),
    (0, "TNMS-NBI-MIB", "enmsPmResultPmpPmpNumber"),
)
if mibBuilder.loadTexts:
    enmsPerfMonResultPmpEntry.setStatus("current")
_EnmsPmResultPmpReqId_Type = PerfMonRequestId
_EnmsPmResultPmpReqId_Object = MibTableColumn
enmsPmResultPmpReqId = _EnmsPmResultPmpReqId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 1),
    _EnmsPmResultPmpReqId_Type()
)
enmsPmResultPmpReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpReqId.setStatus("current")
_EnmsPmResultPmpPmpNumber_Type = Unsigned32
_EnmsPmResultPmpPmpNumber_Object = MibTableColumn
enmsPmResultPmpPmpNumber = _EnmsPmResultPmpPmpNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 2),
    _EnmsPmResultPmpPmpNumber_Type()
)
enmsPmResultPmpPmpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpPmpNumber.setStatus("current")
_EnmsPmResultPmpNeId_Type = NEId
_EnmsPmResultPmpNeId_Object = MibTableColumn
enmsPmResultPmpNeId = _EnmsPmResultPmpNeId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 3),
    _EnmsPmResultPmpNeId_Type()
)
enmsPmResultPmpNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpNeId.setStatus("current")
_EnmsPmResultPmpPortId_Type = PortId
_EnmsPmResultPmpPortId_Object = MibTableColumn
enmsPmResultPmpPortId = _EnmsPmResultPmpPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 4),
    _EnmsPmResultPmpPortId_Type()
)
enmsPmResultPmpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpPortId.setStatus("current")
_EnmsPmResultPmpTPIdH_Type = TPId
_EnmsPmResultPmpTPIdH_Object = MibTableColumn
enmsPmResultPmpTPIdH = _EnmsPmResultPmpTPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 5),
    _EnmsPmResultPmpTPIdH_Type()
)
enmsPmResultPmpTPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpTPIdH.setStatus("current")
_EnmsPmResultPmpTPIdL_Type = TPId
_EnmsPmResultPmpTPIdL_Object = MibTableColumn
enmsPmResultPmpTPIdL = _EnmsPmResultPmpTPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 6),
    _EnmsPmResultPmpTPIdL_Type()
)
enmsPmResultPmpTPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpTPIdL.setStatus("current")
_EnmsPmResultPmpNeIdName_Type = DisplayString
_EnmsPmResultPmpNeIdName_Object = MibTableColumn
enmsPmResultPmpNeIdName = _EnmsPmResultPmpNeIdName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 7),
    _EnmsPmResultPmpNeIdName_Type()
)
enmsPmResultPmpNeIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpNeIdName.setStatus("current")
_EnmsPmResultPmpObjLocation_Type = DisplayString
_EnmsPmResultPmpObjLocation_Object = MibTableColumn
enmsPmResultPmpObjLocation = _EnmsPmResultPmpObjLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 8),
    _EnmsPmResultPmpObjLocation_Type()
)
enmsPmResultPmpObjLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpObjLocation.setStatus("current")
_EnmsPmResultPmpName_Type = DisplayString
_EnmsPmResultPmpName_Object = MibTableColumn
enmsPmResultPmpName = _EnmsPmResultPmpName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 9),
    _EnmsPmResultPmpName_Type()
)
enmsPmResultPmpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpName.setStatus("current")
_EnmsPmResultPmpLocation_Type = PerfMonLocation
_EnmsPmResultPmpLocation_Object = MibTableColumn
enmsPmResultPmpLocation = _EnmsPmResultPmpLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 10),
    _EnmsPmResultPmpLocation_Type()
)
enmsPmResultPmpLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpLocation.setStatus("current")
_EnmsPmResultPmpDirection_Type = PerfMonDirection
_EnmsPmResultPmpDirection_Object = MibTableColumn
enmsPmResultPmpDirection = _EnmsPmResultPmpDirection_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 11),
    _EnmsPmResultPmpDirection_Type()
)
enmsPmResultPmpDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpDirection.setStatus("current")
_EnmsPmResultPmpRetrievalTime_Type = EnmsTimeStamp
_EnmsPmResultPmpRetrievalTime_Object = MibTableColumn
enmsPmResultPmpRetrievalTime = _EnmsPmResultPmpRetrievalTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 12),
    _EnmsPmResultPmpRetrievalTime_Type()
)
enmsPmResultPmpRetrievalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpRetrievalTime.setStatus("current")
_EnmsPmResultPmpPeriodEndTime_Type = EnmsTimeStamp
_EnmsPmResultPmpPeriodEndTime_Object = MibTableColumn
enmsPmResultPmpPeriodEndTime = _EnmsPmResultPmpPeriodEndTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 13),
    _EnmsPmResultPmpPeriodEndTime_Type()
)
enmsPmResultPmpPeriodEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpPeriodEndTime.setStatus("current")
_EnmsPmResultPmpMonitoredTime_Type = Unsigned32
_EnmsPmResultPmpMonitoredTime_Object = MibTableColumn
enmsPmResultPmpMonitoredTime = _EnmsPmResultPmpMonitoredTime_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 14),
    _EnmsPmResultPmpMonitoredTime_Type()
)
enmsPmResultPmpMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpMonitoredTime.setStatus("current")
_EnmsPmResultPmpNumValues_Type = Unsigned32
_EnmsPmResultPmpNumValues_Object = MibTableColumn
enmsPmResultPmpNumValues = _EnmsPmResultPmpNumValues_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 15),
    _EnmsPmResultPmpNumValues_Type()
)
enmsPmResultPmpNumValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpNumValues.setStatus("current")
_EnmsPmResultPmpRelatedPaths_Type = DisplayString
_EnmsPmResultPmpRelatedPaths_Object = MibTableColumn
enmsPmResultPmpRelatedPaths = _EnmsPmResultPmpRelatedPaths_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 16),
    _EnmsPmResultPmpRelatedPaths_Type()
)
enmsPmResultPmpRelatedPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpRelatedPaths.setStatus("current")
_EnmsPmResultPmpRelatedServices_Type = DisplayString
_EnmsPmResultPmpRelatedServices_Object = MibTableColumn
enmsPmResultPmpRelatedServices = _EnmsPmResultPmpRelatedServices_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 17),
    _EnmsPmResultPmpRelatedServices_Type()
)
enmsPmResultPmpRelatedServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpRelatedServices.setStatus("current")
_EnmsPmResultPmpRelatedSubscribers_Type = DisplayString
_EnmsPmResultPmpRelatedSubscribers_Object = MibTableColumn
enmsPmResultPmpRelatedSubscribers = _EnmsPmResultPmpRelatedSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 3, 1, 18),
    _EnmsPmResultPmpRelatedSubscribers_Type()
)
enmsPmResultPmpRelatedSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultPmpRelatedSubscribers.setStatus("current")
_EnmsPerfMonResultValueTable_Object = MibTable
enmsPerfMonResultValueTable = _EnmsPerfMonResultValueTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 4)
)
if mibBuilder.loadTexts:
    enmsPerfMonResultValueTable.setStatus("current")
_EnmsPerfMonResultValueEntry_Object = MibTableRow
enmsPerfMonResultValueEntry = _EnmsPerfMonResultValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 4, 1)
)
enmsPerfMonResultValueEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsPmResultValReqId"),
    (0, "TNMS-NBI-MIB", "enmsPmResultValPmpNumber"),
    (0, "TNMS-NBI-MIB", "enmsPmResultValNumber"),
)
if mibBuilder.loadTexts:
    enmsPerfMonResultValueEntry.setStatus("current")
_EnmsPmResultValReqId_Type = PerfMonRequestId
_EnmsPmResultValReqId_Object = MibTableColumn
enmsPmResultValReqId = _EnmsPmResultValReqId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 4, 1, 1),
    _EnmsPmResultValReqId_Type()
)
enmsPmResultValReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultValReqId.setStatus("current")
_EnmsPmResultValPmpNumber_Type = Unsigned32
_EnmsPmResultValPmpNumber_Object = MibTableColumn
enmsPmResultValPmpNumber = _EnmsPmResultValPmpNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 4, 1, 2),
    _EnmsPmResultValPmpNumber_Type()
)
enmsPmResultValPmpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultValPmpNumber.setStatus("current")
_EnmsPmResultValNumber_Type = Unsigned32
_EnmsPmResultValNumber_Object = MibTableColumn
enmsPmResultValNumber = _EnmsPmResultValNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 4, 1, 3),
    _EnmsPmResultValNumber_Type()
)
enmsPmResultValNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultValNumber.setStatus("current")
_EnmsPmResultValParam_Type = DisplayString
_EnmsPmResultValParam_Object = MibTableColumn
enmsPmResultValParam = _EnmsPmResultValParam_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 4, 1, 4),
    _EnmsPmResultValParam_Type()
)
enmsPmResultValParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultValParam.setStatus("current")
_EnmsPmResultValValue_Type = DisplayString
_EnmsPmResultValValue_Object = MibTableColumn
enmsPmResultValValue = _EnmsPmResultValValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 4, 1, 5),
    _EnmsPmResultValValue_Type()
)
enmsPmResultValValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultValValue.setStatus("current")
_EnmsPmResultValUnit_Type = DisplayString
_EnmsPmResultValUnit_Object = MibTableColumn
enmsPmResultValUnit = _EnmsPmResultValUnit_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 4, 1, 6),
    _EnmsPmResultValUnit_Type()
)
enmsPmResultValUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultValUnit.setStatus("current")
_EnmsPmResultValStatus_Type = PerfMonStatus
_EnmsPmResultValStatus_Object = MibTableColumn
enmsPmResultValStatus = _EnmsPmResultValStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 4, 1, 7),
    _EnmsPmResultValStatus_Type()
)
enmsPmResultValStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultValStatus.setStatus("current")
_EnmsPerfMonResultThresholdTable_Object = MibTable
enmsPerfMonResultThresholdTable = _EnmsPerfMonResultThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 5)
)
if mibBuilder.loadTexts:
    enmsPerfMonResultThresholdTable.setStatus("current")
_EnmsPerfMonResultThresholdEntry_Object = MibTableRow
enmsPerfMonResultThresholdEntry = _EnmsPerfMonResultThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 5, 1)
)
enmsPerfMonResultThresholdEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsPmResultValReqId"),
    (0, "TNMS-NBI-MIB", "enmsPmResultValPmpNumber"),
    (0, "TNMS-NBI-MIB", "enmsPmResultValNumber"),
)
if mibBuilder.loadTexts:
    enmsPerfMonResultThresholdEntry.setStatus("current")
_EnmsPmResultThresholdReqId_Type = PerfMonRequestId
_EnmsPmResultThresholdReqId_Object = MibTableColumn
enmsPmResultThresholdReqId = _EnmsPmResultThresholdReqId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 5, 1, 1),
    _EnmsPmResultThresholdReqId_Type()
)
enmsPmResultThresholdReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultThresholdReqId.setStatus("current")
_EnmsPmResultThresholdPmpNumber_Type = Unsigned32
_EnmsPmResultThresholdPmpNumber_Object = MibTableColumn
enmsPmResultThresholdPmpNumber = _EnmsPmResultThresholdPmpNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 5, 1, 2),
    _EnmsPmResultThresholdPmpNumber_Type()
)
enmsPmResultThresholdPmpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultThresholdPmpNumber.setStatus("current")
_EnmsPmResultThresholdNumber_Type = Unsigned32
_EnmsPmResultThresholdNumber_Object = MibTableColumn
enmsPmResultThresholdNumber = _EnmsPmResultThresholdNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 5, 1, 3),
    _EnmsPmResultThresholdNumber_Type()
)
enmsPmResultThresholdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultThresholdNumber.setStatus("current")
_EnmsPmResultThresholdParam_Type = DisplayString
_EnmsPmResultThresholdParam_Object = MibTableColumn
enmsPmResultThresholdParam = _EnmsPmResultThresholdParam_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 5, 1, 4),
    _EnmsPmResultThresholdParam_Type()
)
enmsPmResultThresholdParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultThresholdParam.setStatus("current")
_EnmsPmResultThresholdType_Type = PerfMonThresholdType
_EnmsPmResultThresholdType_Object = MibTableColumn
enmsPmResultThresholdType = _EnmsPmResultThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 5, 1, 5),
    _EnmsPmResultThresholdType_Type()
)
enmsPmResultThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultThresholdType.setStatus("current")
_EnmsPmResultThresholdTriggerFlag_Type = Boolean
_EnmsPmResultThresholdTriggerFlag_Object = MibTableColumn
enmsPmResultThresholdTriggerFlag = _EnmsPmResultThresholdTriggerFlag_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 5, 1, 6),
    _EnmsPmResultThresholdTriggerFlag_Type()
)
enmsPmResultThresholdTriggerFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultThresholdTriggerFlag.setStatus("current")
_EnmsPmResultThresholdValue_Type = DisplayString
_EnmsPmResultThresholdValue_Object = MibTableColumn
enmsPmResultThresholdValue = _EnmsPmResultThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 5, 1, 7),
    _EnmsPmResultThresholdValue_Type()
)
enmsPmResultThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultThresholdValue.setStatus("current")
_EnmsPmResultThresholdUnit_Type = DisplayString
_EnmsPmResultThresholdUnit_Object = MibTableColumn
enmsPmResultThresholdUnit = _EnmsPmResultThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 6, 5, 1, 8),
    _EnmsPmResultThresholdUnit_Type()
)
enmsPmResultThresholdUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsPmResultThresholdUnit.setStatus("current")
_EnmsOptPowerMon_ObjectIdentity = ObjectIdentity
enmsOptPowerMon = _EnmsOptPowerMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7)
)
_EnmsOpmRequestNextId_Type = OptPowerMonRequestId
_EnmsOpmRequestNextId_Object = MibScalar
enmsOpmRequestNextId = _EnmsOpmRequestNextId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 1),
    _EnmsOpmRequestNextId_Type()
)
enmsOpmRequestNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsOpmRequestNextId.setStatus("current")
_EnmsOptPowerMonRequestTable_Object = MibTable
enmsOptPowerMonRequestTable = _EnmsOptPowerMonRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 2)
)
if mibBuilder.loadTexts:
    enmsOptPowerMonRequestTable.setStatus("current")
_EnmsOptPowerMonRequestEntry_Object = MibTableRow
enmsOptPowerMonRequestEntry = _EnmsOptPowerMonRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 2, 1)
)
enmsOptPowerMonRequestEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsOpmRequestId"),
)
if mibBuilder.loadTexts:
    enmsOptPowerMonRequestEntry.setStatus("current")
_EnmsOpmRequestId_Type = OptPowerMonRequestId
_EnmsOpmRequestId_Object = MibTableColumn
enmsOpmRequestId = _EnmsOpmRequestId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 2, 1, 1),
    _EnmsOpmRequestId_Type()
)
enmsOpmRequestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enmsOpmRequestId.setStatus("current")
_EnmsOpmRequestName_Type = DisplayString
_EnmsOpmRequestName_Object = MibTableColumn
enmsOpmRequestName = _EnmsOpmRequestName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 2, 1, 2),
    _EnmsOpmRequestName_Type()
)
enmsOpmRequestName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsOpmRequestName.setStatus("current")
_EnmsOpmRequestRowStatus_Type = RowStatus
_EnmsOpmRequestRowStatus_Object = MibTableColumn
enmsOpmRequestRowStatus = _EnmsOpmRequestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 2, 1, 3),
    _EnmsOpmRequestRowStatus_Type()
)
enmsOpmRequestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsOpmRequestRowStatus.setStatus("current")
_EnmsOpmRequestLastUpdate_Type = EnmsTimeStamp
_EnmsOpmRequestLastUpdate_Object = MibTableColumn
enmsOpmRequestLastUpdate = _EnmsOpmRequestLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 2, 1, 4),
    _EnmsOpmRequestLastUpdate_Type()
)
enmsOpmRequestLastUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsOpmRequestLastUpdate.setStatus("current")
_EnmsOpmRequestInfo_Type = DisplayString
_EnmsOpmRequestInfo_Object = MibTableColumn
enmsOpmRequestInfo = _EnmsOpmRequestInfo_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 2, 1, 5),
    _EnmsOpmRequestInfo_Type()
)
enmsOpmRequestInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsOpmRequestInfo.setStatus("current")
_EnmsOpmRequestState_Type = OptPowerMonRequestState
_EnmsOpmRequestState_Object = MibTableColumn
enmsOpmRequestState = _EnmsOpmRequestState_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 2, 1, 6),
    _EnmsOpmRequestState_Type()
)
enmsOpmRequestState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsOpmRequestState.setStatus("current")
_EnmsOpmRequestFilterType_Type = FilterType
_EnmsOpmRequestFilterType_Object = MibTableColumn
enmsOpmRequestFilterType = _EnmsOpmRequestFilterType_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 2, 1, 7),
    _EnmsOpmRequestFilterType_Type()
)
enmsOpmRequestFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsOpmRequestFilterType.setStatus("current")
_EnmsOpmRequestFilterValue_Type = DisplayString
_EnmsOpmRequestFilterValue_Object = MibTableColumn
enmsOpmRequestFilterValue = _EnmsOpmRequestFilterValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 2, 1, 8),
    _EnmsOpmRequestFilterValue_Type()
)
enmsOpmRequestFilterValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    enmsOpmRequestFilterValue.setStatus("current")
_EnmsOptPowerMonResultValueTable_Object = MibTable
enmsOptPowerMonResultValueTable = _EnmsOptPowerMonResultValueTable_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3)
)
if mibBuilder.loadTexts:
    enmsOptPowerMonResultValueTable.setStatus("current")
_EnmsOptPowerMonResultValueEntry_Object = MibTableRow
enmsOptPowerMonResultValueEntry = _EnmsOptPowerMonResultValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3, 1)
)
enmsOptPowerMonResultValueEntry.setIndexNames(
    (0, "TNMS-NBI-MIB", "enmsOpmResultValReqId"),
    (0, "TNMS-NBI-MIB", "enmsOpmResultValNumber"),
)
if mibBuilder.loadTexts:
    enmsOptPowerMonResultValueEntry.setStatus("current")
_EnmsOpmResultValReqId_Type = OptPowerMonRequestId
_EnmsOpmResultValReqId_Object = MibTableColumn
enmsOpmResultValReqId = _EnmsOpmResultValReqId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3, 1, 1),
    _EnmsOpmResultValReqId_Type()
)
enmsOpmResultValReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsOpmResultValReqId.setStatus("current")
_EnmsOpmResultValNumber_Type = Unsigned32
_EnmsOpmResultValNumber_Object = MibTableColumn
enmsOpmResultValNumber = _EnmsOpmResultValNumber_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3, 1, 2),
    _EnmsOpmResultValNumber_Type()
)
enmsOpmResultValNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsOpmResultValNumber.setStatus("current")
_EnmsOpmResultValNeId_Type = NEId
_EnmsOpmResultValNeId_Object = MibTableColumn
enmsOpmResultValNeId = _EnmsOpmResultValNeId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3, 1, 3),
    _EnmsOpmResultValNeId_Type()
)
enmsOpmResultValNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsOpmResultValNeId.setStatus("current")
_EnmsOpmResultValPortId_Type = PortId
_EnmsOpmResultValPortId_Object = MibTableColumn
enmsOpmResultValPortId = _EnmsOpmResultValPortId_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3, 1, 4),
    _EnmsOpmResultValPortId_Type()
)
enmsOpmResultValPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsOpmResultValPortId.setStatus("current")
_EnmsOpmResultValTPIdH_Type = TPId
_EnmsOpmResultValTPIdH_Object = MibTableColumn
enmsOpmResultValTPIdH = _EnmsOpmResultValTPIdH_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3, 1, 5),
    _EnmsOpmResultValTPIdH_Type()
)
enmsOpmResultValTPIdH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsOpmResultValTPIdH.setStatus("current")
_EnmsOpmResultValTPIdL_Type = TPId
_EnmsOpmResultValTPIdL_Object = MibTableColumn
enmsOpmResultValTPIdL = _EnmsOpmResultValTPIdL_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3, 1, 6),
    _EnmsOpmResultValTPIdL_Type()
)
enmsOpmResultValTPIdL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsOpmResultValTPIdL.setStatus("current")
_EnmsOpmResultValNeIdName_Type = DisplayString
_EnmsOpmResultValNeIdName_Object = MibTableColumn
enmsOpmResultValNeIdName = _EnmsOpmResultValNeIdName_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3, 1, 7),
    _EnmsOpmResultValNeIdName_Type()
)
enmsOpmResultValNeIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsOpmResultValNeIdName.setStatus("current")
_EnmsOpmResultValObjLocation_Type = DisplayString
_EnmsOpmResultValObjLocation_Object = MibTableColumn
enmsOpmResultValObjLocation = _EnmsOpmResultValObjLocation_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3, 1, 8),
    _EnmsOpmResultValObjLocation_Type()
)
enmsOpmResultValObjLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsOpmResultValObjLocation.setStatus("current")
_EnmsOpmResultValLane_Type = Unsigned32
_EnmsOpmResultValLane_Object = MibTableColumn
enmsOpmResultValLane = _EnmsOpmResultValLane_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3, 1, 9),
    _EnmsOpmResultValLane_Type()
)
enmsOpmResultValLane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsOpmResultValLane.setStatus("current")
_EnmsOpmResultValLayer_Type = DisplayString
_EnmsOpmResultValLayer_Object = MibTableColumn
enmsOpmResultValLayer = _EnmsOpmResultValLayer_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3, 1, 10),
    _EnmsOpmResultValLayer_Type()
)
enmsOpmResultValLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsOpmResultValLayer.setStatus("current")
_EnmsOpmResultValParam_Type = DisplayString
_EnmsOpmResultValParam_Object = MibTableColumn
enmsOpmResultValParam = _EnmsOpmResultValParam_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3, 1, 11),
    _EnmsOpmResultValParam_Type()
)
enmsOpmResultValParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsOpmResultValParam.setStatus("current")
_EnmsOpmResultValValue_Type = DisplayString
_EnmsOpmResultValValue_Object = MibTableColumn
enmsOpmResultValValue = _EnmsOpmResultValValue_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3, 1, 12),
    _EnmsOpmResultValValue_Type()
)
enmsOpmResultValValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsOpmResultValValue.setStatus("current")
_EnmsOpmResultValUnit_Type = DisplayString
_EnmsOpmResultValUnit_Object = MibTableColumn
enmsOpmResultValUnit = _EnmsOpmResultValUnit_Object(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 7, 3, 1, 13),
    _EnmsOpmResultValUnit_Type()
)
enmsOpmResultValUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enmsOpmResultValUnit.setStatus("current")

# Managed Objects groups


# Notification objects

enmsProxyStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 1, 1)
)
enmsProxyStateChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsProxyName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsProxyOpState"))
)
if mibBuilder.loadTexts:
    enmsProxyStateChangeTrap.setStatus(
        "current"
    )

enmsNEObjectCreationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 2, 1)
)
enmsNEObjectCreationTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsNeNEId"),
        ("TNMS-NBI-MIB", "enmsNeName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapNeIdName"),
        ("TNMS-NBI-MIB", "enmsNeSystemContainer"),
        ("TNMS-NBI-MIB", "enmsNeUserText"))
)
if mibBuilder.loadTexts:
    enmsNEObjectCreationTrap.setStatus(
        "current"
    )

enmsNEObjectDeletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 2, 2)
)
enmsNEObjectDeletionTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsNeNEId"),
        ("TNMS-NBI-MIB", "enmsNeName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapNeIdName"),
        ("TNMS-NBI-MIB", "enmsNeSystemContainer"),
        ("TNMS-NBI-MIB", "enmsNeUserText"))
)
if mibBuilder.loadTexts:
    enmsNEObjectDeletionTrap.setStatus(
        "current"
    )

enmsNEStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 2, 3)
)
enmsNEStateChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsNeNEId"),
        ("TNMS-NBI-MIB", "enmsNeName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapStateName"),
        ("TNMS-NBI-MIB", "enmsTrapStateOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapStateNewValue"),
        ("TNMS-NBI-MIB", "enmsTrapNeIdName"),
        ("TNMS-NBI-MIB", "enmsNeSystemContainer"),
        ("TNMS-NBI-MIB", "enmsNeUserText"))
)
if mibBuilder.loadTexts:
    enmsNEStateChangeTrap.setStatus(
        "current"
    )

enmsNEAttributeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 2, 4)
)
enmsNEAttributeChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsNeNEId"),
        ("TNMS-NBI-MIB", "enmsNeName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeName"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeNewValue"),
        ("TNMS-NBI-MIB", "enmsTrapNeIdName"),
        ("TNMS-NBI-MIB", "enmsNeSystemContainer"),
        ("TNMS-NBI-MIB", "enmsNeUserText"))
)
if mibBuilder.loadTexts:
    enmsNEAttributeChangeTrap.setStatus(
        "current"
    )

enmsNEAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 2, 5)
)
enmsNEAlarmTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsNeNEId"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsAlClass"),
        ("TNMS-NBI-MIB", "enmsAlState"),
        ("TNMS-NBI-MIB", "enmsAlTimeStamp"),
        ("TNMS-NBI-MIB", "enmsAlEntityString"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCauseString"),
        ("TNMS-NBI-MIB", "enmsNeName"),
        ("TNMS-NBI-MIB", "enmsTrapNeLocationLct"),
        ("TNMS-NBI-MIB", "enmsTrapNeIdName"),
        ("TNMS-NBI-MIB", "enmsTrapAffectedLocation"),
        ("TNMS-NBI-MIB", "enmsTrapEventTrafficDirection"),
        ("TNMS-NBI-MIB", "enmsAlServiceAffect"),
        ("TNMS-NBI-MIB", "enmsAlAdditionalInformation"),
        ("TNMS-NBI-MIB", "enmsAlNeSystemContainer"))
)
if mibBuilder.loadTexts:
    enmsNEAlarmTrap.setStatus(
        "current"
    )

enmsModuleObjectCreationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 3, 1)
)
enmsModuleObjectCreationTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsMoNEId"),
        ("TNMS-NBI-MIB", "enmsMoModuleId"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsModuleObjectCreationTrap.setStatus(
        "current"
    )

enmsModuleObjectDeletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 3, 2)
)
enmsModuleObjectDeletionTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsMoNEId"),
        ("TNMS-NBI-MIB", "enmsMoModuleId"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsModuleObjectDeletionTrap.setStatus(
        "current"
    )

enmsModuleStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 3, 3)
)
enmsModuleStateChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsMoNEId"),
        ("TNMS-NBI-MIB", "enmsMoModuleId"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapStateName"),
        ("TNMS-NBI-MIB", "enmsTrapStateOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapStateNewValue"))
)
if mibBuilder.loadTexts:
    enmsModuleStateChangeTrap.setStatus(
        "current"
    )

enmsModuleAttributeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 3, 4)
)
enmsModuleAttributeChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsMoNEId"),
        ("TNMS-NBI-MIB", "enmsMoModuleId"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeName"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeNewValue"))
)
if mibBuilder.loadTexts:
    enmsModuleAttributeChangeTrap.setStatus(
        "current"
    )

enmsModuleAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 3, 5)
)
enmsModuleAlarmTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsMoNEId"),
        ("TNMS-NBI-MIB", "enmsMoModuleId"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsAlClass"),
        ("TNMS-NBI-MIB", "enmsAlState"),
        ("TNMS-NBI-MIB", "enmsAlTimeStamp"),
        ("TNMS-NBI-MIB", "enmsAlEntityString"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCauseString"),
        ("TNMS-NBI-MIB", "enmsNeName"),
        ("TNMS-NBI-MIB", "enmsTrapNeLocationLct"),
        ("TNMS-NBI-MIB", "enmsTrapNeIdName"),
        ("TNMS-NBI-MIB", "enmsTrapAffectedLocation"),
        ("TNMS-NBI-MIB", "enmsTrapEventTrafficDirection"),
        ("TNMS-NBI-MIB", "enmsAlServiceAffect"),
        ("TNMS-NBI-MIB", "enmsAlAdditionalInformation"),
        ("TNMS-NBI-MIB", "enmsAlNeSystemContainer"))
)
if mibBuilder.loadTexts:
    enmsModuleAlarmTrap.setStatus(
        "current"
    )

enmsPortObjectCreationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 4, 1)
)
enmsPortObjectCreationTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsPtNEId"),
        ("TNMS-NBI-MIB", "enmsPtPortId"),
        ("TNMS-NBI-MIB", "enmsPtName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsPortObjectCreationTrap.setStatus(
        "current"
    )

enmsPortObjectDeletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 4, 2)
)
enmsPortObjectDeletionTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsPtNEId"),
        ("TNMS-NBI-MIB", "enmsPtPortId"),
        ("TNMS-NBI-MIB", "enmsPtName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsPortObjectDeletionTrap.setStatus(
        "current"
    )

enmsPortStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 4, 3)
)
enmsPortStateChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsPtNEId"),
        ("TNMS-NBI-MIB", "enmsPtPortId"),
        ("TNMS-NBI-MIB", "enmsPtName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapStateName"),
        ("TNMS-NBI-MIB", "enmsTrapStateOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapStateNewValue"))
)
if mibBuilder.loadTexts:
    enmsPortStateChangeTrap.setStatus(
        "current"
    )

enmsPortAttributeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 4, 4)
)
enmsPortAttributeChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsPtNEId"),
        ("TNMS-NBI-MIB", "enmsPtPortId"),
        ("TNMS-NBI-MIB", "enmsPtName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeName"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeNewValue"))
)
if mibBuilder.loadTexts:
    enmsPortAttributeChangeTrap.setStatus(
        "current"
    )

enmsPortAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 4, 5)
)
enmsPortAlarmTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsPtNEId"),
        ("TNMS-NBI-MIB", "enmsPtPortId"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsAlClass"),
        ("TNMS-NBI-MIB", "enmsAlState"),
        ("TNMS-NBI-MIB", "enmsAlTimeStamp"),
        ("TNMS-NBI-MIB", "enmsAlEntityString"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCauseString"),
        ("TNMS-NBI-MIB", "enmsNeName"),
        ("TNMS-NBI-MIB", "enmsTrapNeLocationLct"),
        ("TNMS-NBI-MIB", "enmsTrapNeIdName"),
        ("TNMS-NBI-MIB", "enmsTrapAffectedLocation"),
        ("TNMS-NBI-MIB", "enmsTrapEventTrafficDirection"),
        ("TNMS-NBI-MIB", "enmsAlServiceAffect"),
        ("TNMS-NBI-MIB", "enmsAlAdditionalInformation"),
        ("TNMS-NBI-MIB", "enmsAlNeSystemContainer"))
)
if mibBuilder.loadTexts:
    enmsPortAlarmTrap.setStatus(
        "current"
    )

enmsTPObjectCreationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 5, 1)
)
enmsTPObjectCreationTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsTpNEId"),
        ("TNMS-NBI-MIB", "enmsTpPortId"),
        ("TNMS-NBI-MIB", "enmsTpTPIdH"),
        ("TNMS-NBI-MIB", "enmsTpTPIdL"),
        ("TNMS-NBI-MIB", "enmsTpName"),
        ("TNMS-NBI-MIB", "enmsTpTPType"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsTPObjectCreationTrap.setStatus(
        "current"
    )

enmsTPObjectDeletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 5, 2)
)
enmsTPObjectDeletionTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsTpNEId"),
        ("TNMS-NBI-MIB", "enmsTpPortId"),
        ("TNMS-NBI-MIB", "enmsTpTPIdH"),
        ("TNMS-NBI-MIB", "enmsTpTPIdL"),
        ("TNMS-NBI-MIB", "enmsTpName"),
        ("TNMS-NBI-MIB", "enmsTpTPType"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsTPObjectDeletionTrap.setStatus(
        "current"
    )

enmsTPStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 5, 3)
)
enmsTPStateChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsTpNEId"),
        ("TNMS-NBI-MIB", "enmsTpPortId"),
        ("TNMS-NBI-MIB", "enmsTpTPIdH"),
        ("TNMS-NBI-MIB", "enmsTpTPIdL"),
        ("TNMS-NBI-MIB", "enmsTpName"),
        ("TNMS-NBI-MIB", "enmsTpTPType"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapStateName"),
        ("TNMS-NBI-MIB", "enmsTrapStateOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapStateNewValue"))
)
if mibBuilder.loadTexts:
    enmsTPStateChangeTrap.setStatus(
        "current"
    )

enmsTPAttributeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 5, 4)
)
enmsTPAttributeChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsTpNEId"),
        ("TNMS-NBI-MIB", "enmsTpPortId"),
        ("TNMS-NBI-MIB", "enmsTpTPIdH"),
        ("TNMS-NBI-MIB", "enmsTpTPIdL"),
        ("TNMS-NBI-MIB", "enmsTpName"),
        ("TNMS-NBI-MIB", "enmsTpTPType"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeName"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeNewValue"))
)
if mibBuilder.loadTexts:
    enmsTPAttributeChangeTrap.setStatus(
        "current"
    )

enmsTPAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 5, 5)
)
enmsTPAlarmTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsTpNEId"),
        ("TNMS-NBI-MIB", "enmsTpPortId"),
        ("TNMS-NBI-MIB", "enmsTpTPIdH"),
        ("TNMS-NBI-MIB", "enmsTpTPIdL"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsAlClass"),
        ("TNMS-NBI-MIB", "enmsAlState"),
        ("TNMS-NBI-MIB", "enmsAlTimeStamp"),
        ("TNMS-NBI-MIB", "enmsAlEntityString"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCauseString"),
        ("TNMS-NBI-MIB", "enmsNeName"),
        ("TNMS-NBI-MIB", "enmsTrapNeLocationLct"),
        ("TNMS-NBI-MIB", "enmsTrapNeIdName"),
        ("TNMS-NBI-MIB", "enmsTrapAffectedLocation"),
        ("TNMS-NBI-MIB", "enmsTrapEventTrafficDirection"),
        ("TNMS-NBI-MIB", "enmsAlServiceAffect"),
        ("TNMS-NBI-MIB", "enmsAlAdditionalInformation"),
        ("TNMS-NBI-MIB", "enmsAlNeSystemContainer"))
)
if mibBuilder.loadTexts:
    enmsTPAlarmTrap.setStatus(
        "current"
    )

enmsPortConnObjectCreationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 6, 1)
)
enmsPortConnObjectCreationTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsPcPortConnId"),
        ("TNMS-NBI-MIB", "enmsPcName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsPortConnObjectCreationTrap.setStatus(
        "current"
    )

enmsPortConnObjectDeletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 6, 2)
)
enmsPortConnObjectDeletionTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsPcPortConnId"),
        ("TNMS-NBI-MIB", "enmsPcName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsPortConnObjectDeletionTrap.setStatus(
        "current"
    )

enmsPortConnAttributeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 6, 3)
)
enmsPortConnAttributeChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsPcPortConnId"),
        ("TNMS-NBI-MIB", "enmsPcName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeName"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeNewValue"))
)
if mibBuilder.loadTexts:
    enmsPortConnAttributeChangeTrap.setStatus(
        "current"
    )

enmsSNCObjectCreationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 7, 1)
)
enmsSNCObjectCreationTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsScSNCId"),
        ("TNMS-NBI-MIB", "enmsScName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsSNCObjectCreationTrap.setStatus(
        "current"
    )

enmsSNCObjectDeletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 7, 2)
)
enmsSNCObjectDeletionTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsScSNCId"),
        ("TNMS-NBI-MIB", "enmsScName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsSNCObjectDeletionTrap.setStatus(
        "current"
    )

enmsSNCStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 7, 3)
)
enmsSNCStateChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsScSNCId"),
        ("TNMS-NBI-MIB", "enmsScName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapStateName"),
        ("TNMS-NBI-MIB", "enmsTrapStateOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapStateNewValue"))
)
if mibBuilder.loadTexts:
    enmsSNCStateChangeTrap.setStatus(
        "current"
    )

enmsSNCAttributeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 7, 4)
)
enmsSNCAttributeChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsScSNCId"),
        ("TNMS-NBI-MIB", "enmsScName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeName"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeNewValue"))
)
if mibBuilder.loadTexts:
    enmsSNCAttributeChangeTrap.setStatus(
        "current"
    )

enmsSNCTPRelationshipChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 7, 5)
)
enmsSNCTPRelationshipChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsScSNCId"),
        ("TNMS-NBI-MIB", "enmsScName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsSNCTPRelationshipChangeTrap.setStatus(
        "current"
    )

enmsSubscriberObjectCreationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 8, 1)
)
enmsSubscriberObjectCreationTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsSbSubscriberId"),
        ("TNMS-NBI-MIB", "enmsSbName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsSubscriberObjectCreationTrap.setStatus(
        "current"
    )

enmsSubscriberObjectDeletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 8, 2)
)
enmsSubscriberObjectDeletionTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsSbSubscriberId"),
        ("TNMS-NBI-MIB", "enmsSbName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsSubscriberObjectDeletionTrap.setStatus(
        "current"
    )

enmsSubscriberAttributeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 8, 3)
)
enmsSubscriberAttributeChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsSbSubscriberId"),
        ("TNMS-NBI-MIB", "enmsSbName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeName"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeNewValue"))
)
if mibBuilder.loadTexts:
    enmsSubscriberAttributeChangeTrap.setStatus(
        "current"
    )

enmsServiceObjectCreationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 9, 1)
)
enmsServiceObjectCreationTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsSvServiceId"),
        ("TNMS-NBI-MIB", "enmsSvLabel"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsServiceObjectCreationTrap.setStatus(
        "current"
    )

enmsServiceObjectDeletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 9, 2)
)
enmsServiceObjectDeletionTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsSvServiceId"),
        ("TNMS-NBI-MIB", "enmsSvLabel"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsServiceObjectDeletionTrap.setStatus(
        "current"
    )

enmsServiceStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 9, 3)
)
enmsServiceStateChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsSvServiceId"),
        ("TNMS-NBI-MIB", "enmsSvLabel"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapStateName"),
        ("TNMS-NBI-MIB", "enmsTrapStateOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapStateNewValue"))
)
if mibBuilder.loadTexts:
    enmsServiceStateChangeTrap.setStatus(
        "current"
    )

enmsServiceAttributeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 9, 4)
)
enmsServiceAttributeChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsSvServiceId"),
        ("TNMS-NBI-MIB", "enmsSvLabel"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeName"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeNewValue"))
)
if mibBuilder.loadTexts:
    enmsServiceAttributeChangeTrap.setStatus(
        "current"
    )

enmsEMSAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 10, 1)
)
enmsEMSAlarmTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsAlClass"),
        ("TNMS-NBI-MIB", "enmsAlState"),
        ("TNMS-NBI-MIB", "enmsAlTimeStamp"),
        ("TNMS-NBI-MIB", "enmsAlEntityString"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCauseString"),
        ("TNMS-NBI-MIB", "enmsAlAdditionalInformation"))
)
if mibBuilder.loadTexts:
    enmsEMSAlarmTrap.setStatus(
        "current"
    )

enmsHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 11, 1)
)
enmsHeartbeatTrap.setObjects(
    ("TNMS-NBI-MIB", "enmsProxyName")
)
if mibBuilder.loadTexts:
    enmsHeartbeatTrap.setStatus(
        "current"
    )

enmsEthernetPathObjectCreationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 12, 1)
)
enmsEthernetPathObjectCreationTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsEvcEthernetPathId"),
        ("TNMS-NBI-MIB", "enmsEvcName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsEthernetPathObjectCreationTrap.setStatus(
        "current"
    )

enmsEthernetPathObjectDeletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 12, 2)
)
enmsEthernetPathObjectDeletionTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsEvcEthernetPathId"),
        ("TNMS-NBI-MIB", "enmsEvcName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"))
)
if mibBuilder.loadTexts:
    enmsEthernetPathObjectDeletionTrap.setStatus(
        "current"
    )

enmsEthernetPathStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 12, 3)
)
enmsEthernetPathStateChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsEvcEthernetPathId"),
        ("TNMS-NBI-MIB", "enmsEvcName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapStateName"),
        ("TNMS-NBI-MIB", "enmsTrapStateOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapStateNewValue"))
)
if mibBuilder.loadTexts:
    enmsEthernetPathStateChangeTrap.setStatus(
        "current"
    )

enmsEthernetPathAttributeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 12, 4)
)
enmsEthernetPathAttributeChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsEvcEthernetPathId"),
        ("TNMS-NBI-MIB", "enmsEvcName"),
        ("TNMS-NBI-MIB", "enmsTrapEventDetails"),
        ("TNMS-NBI-MIB", "enmsTrapEventSeverity"),
        ("TNMS-NBI-MIB", "enmsTrapEventProbableCause"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeName"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeOldValue"),
        ("TNMS-NBI-MIB", "enmsTrapAttributeNewValue"))
)
if mibBuilder.loadTexts:
    enmsEthernetPathAttributeChangeTrap.setStatus(
        "current"
    )

enmsPerfMonRequestStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 13, 1)
)
enmsPerfMonRequestStateChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsPmRequestId"),
        ("TNMS-NBI-MIB", "enmsPmRequestName"),
        ("TNMS-NBI-MIB", "enmsPmRequestState"),
        ("TNMS-NBI-MIB", "enmsPmRequestInfo"))
)
if mibBuilder.loadTexts:
    enmsPerfMonRequestStateChangeTrap.setStatus(
        "current"
    )

enmsOptPowerMonRequestStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42229, 6, 22, 5, 3, 14, 1)
)
enmsOptPowerMonRequestStateChangeTrap.setObjects(
      *(("TNMS-NBI-MIB", "enmsTrapCounter"),
        ("TNMS-NBI-MIB", "enmsOpmRequestId"),
        ("TNMS-NBI-MIB", "enmsOpmRequestName"),
        ("TNMS-NBI-MIB", "enmsOpmRequestState"),
        ("TNMS-NBI-MIB", "enmsOpmRequestInfo"))
)
if mibBuilder.loadTexts:
    enmsOptPowerMonRequestStateChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TNMS-NBI-MIB",
    **{"DisplayString": DisplayString,
       "Boolean": Boolean,
       "TrapFilter": TrapFilter,
       "EnmsTimeStamp": EnmsTimeStamp,
       "InfoString": InfoString,
       "TPIndex": TPIndex,
       "UniqueId": UniqueId,
       "NEId": NEId,
       "ModuleId": ModuleId,
       "PortId": PortId,
       "TPId": TPId,
       "PortConnId": PortConnId,
       "SNCId": SNCId,
       "EthernetPathId": EthernetPathId,
       "CCId": CCId,
       "SubscriberId": SubscriberId,
       "ServiceId": ServiceId,
       "VpcId": VpcId,
       "VccId": VccId,
       "Bandwidth": Bandwidth,
       "PerceivedSeverity": PerceivedSeverity,
       "AlarmClass": AlarmClass,
       "AlarmState": AlarmState,
       "OperationalState": OperationalState,
       "OperatingMode": OperatingMode,
       "AdministrativeState": AdministrativeState,
       "ProvisioningState": ProvisioningState,
       "UsageState": UsageState,
       "ProtectionState": ProtectionState,
       "EntityType": EntityType,
       "ProbableCause": ProbableCause,
       "TrafficDirection": TrafficDirection,
       "Directionality": Directionality,
       "NEClass": NEClass,
       "PTTechnology": PTTechnology,
       "PTServiceType": PTServiceType,
       "PTInterfaceType": PTInterfaceType,
       "PTProtectionType": PTProtectionType,
       "TPType": TPType,
       "TPTerminationType": TPTerminationType,
       "TPReliability": TPReliability,
       "SVProtection": SVProtection,
       "SNCProtectionInfo": SNCProtectionInfo,
       "EthernetPathProtectionInfo": EthernetPathProtectionInfo,
       "EthernetPathType": EthernetPathType,
       "TPEndPointType": TPEndPointType,
       "TPTimeSlotHierarchy": TPTimeSlotHierarchy,
       "CharacteristicInfo": CharacteristicInfo,
       "NotificationType": NotificationType,
       "LayerSet": LayerSet,
       "FilterType": FilterType,
       "PerfMonRequestId": PerfMonRequestId,
       "PerfMonRequestState": PerfMonRequestState,
       "PerfMonType": PerfMonType,
       "PerfMonGranularity": PerfMonGranularity,
       "PerfMonLocation": PerfMonLocation,
       "PerfMonDirection": PerfMonDirection,
       "PerfMonStatus": PerfMonStatus,
       "PerfMonThresholdType": PerfMonThresholdType,
       "OptPowerMonRequestId": OptPowerMonRequestId,
       "OptPowerMonRequestState": OptPowerMonRequestState,
       "coriant": coriant,
       "svsProductMibs": svsProductMibs,
       "svsProxEnms": svsProxEnms,
       "enmsNetworkSetup": enmsNetworkSetup,
       "enmsNETable": enmsNETable,
       "enmsNEEntry": enmsNEEntry,
       "enmsNeNEId": enmsNeNEId,
       "enmsNeType": enmsNeType,
       "enmsNeName": enmsNeName,
       "enmsNeLocation": enmsNeLocation,
       "enmsNeAlarmSeverity": enmsNeAlarmSeverity,
       "enmsNeOperatingMode": enmsNeOperatingMode,
       "enmsNeOpState": enmsNeOpState,
       "enmsNeCanBroadcast": enmsNeCanBroadcast,
       "enmsNeCanPathProtection": enmsNeCanPathProtection,
       "enmsNeClass": enmsNeClass,
       "enmsNeExternalNEId": enmsNeExternalNEId,
       "enmsNeIsPseudoNE": enmsNeIsPseudoNE,
       "enmsNeIdName": enmsNeIdName,
       "enmsNeCommunicationState": enmsNeCommunicationState,
       "enmsNeDCNLocation": enmsNeDCNLocation,
       "enmsNeSystemContainer": enmsNeSystemContainer,
       "enmsNeUserText": enmsNeUserText,
       "enmsModuleTable": enmsModuleTable,
       "enmsModuleEntry": enmsModuleEntry,
       "enmsMoNEId": enmsMoNEId,
       "enmsMoModuleId": enmsMoModuleId,
       "enmsMoType": enmsMoType,
       "enmsMoName": enmsMoName,
       "enmsMoOpState": enmsMoOpState,
       "enmsMoShelf": enmsMoShelf,
       "enmsMoSlot": enmsMoSlot,
       "enmsMoObjectType": enmsMoObjectType,
       "enmsPortTable": enmsPortTable,
       "enmsPortEntry": enmsPortEntry,
       "enmsPtNEId": enmsPtNEId,
       "enmsPtPortId": enmsPtPortId,
       "enmsPtName": enmsPtName,
       "enmsPtModuleId": enmsPtModuleId,
       "enmsPtTechnology": enmsPtTechnology,
       "enmsPtServiceType": enmsPtServiceType,
       "enmsPtInterfaceType": enmsPtInterfaceType,
       "enmsPtBandwidth": enmsPtBandwidth,
       "enmsPtOpState": enmsPtOpState,
       "enmsPtOperatingMode": enmsPtOperatingMode,
       "enmsPtDirection": enmsPtDirection,
       "enmsPtCanBroadcast": enmsPtCanBroadcast,
       "enmsPtCanPathProtection": enmsPtCanPathProtection,
       "enmsPtAlarmSeverity": enmsPtAlarmSeverity,
       "enmsPtAdminState": enmsPtAdminState,
       "enmsPtOpStateTX": enmsPtOpStateTX,
       "enmsPtOpStateRX": enmsPtOpStateRX,
       "enmsPtModuleIdTX": enmsPtModuleIdTX,
       "enmsPtModuleIdRX": enmsPtModuleIdRX,
       "enmsPtLayerSet": enmsPtLayerSet,
       "enmsPtProtectionType": enmsPtProtectionType,
       "enmsPtObjectType": enmsPtObjectType,
       "enmsTPTable": enmsTPTable,
       "enmsTPEntry": enmsTPEntry,
       "enmsTpNEId": enmsTpNEId,
       "enmsTpPortId": enmsTpPortId,
       "enmsTpTPIdH": enmsTpTPIdH,
       "enmsTpTPIdL": enmsTpTPIdL,
       "enmsTpTPIndex": enmsTpTPIndex,
       "enmsTpNxCount": enmsTpNxCount,
       "enmsTpName": enmsTpName,
       "enmsTpBandwidth": enmsTpBandwidth,
       "enmsTpTPType": enmsTpTPType,
       "enmsTpTerminType": enmsTpTerminType,
       "enmsTpDirection": enmsTpDirection,
       "enmsTpOpStateTX": enmsTpOpStateTX,
       "enmsTpOpStateRX": enmsTpOpStateRX,
       "enmsTpAlarmSeverity": enmsTpAlarmSeverity,
       "enmsTpAdminState": enmsTpAdminState,
       "enmsTpUsageCountTX": enmsTpUsageCountTX,
       "enmsTpUsageCountRX": enmsTpUsageCountRX,
       "enmsTpUsageStateTX": enmsTpUsageStateTX,
       "enmsTpUsageStateRX": enmsTpUsageStateRX,
       "enmsTpReliability": enmsTpReliability,
       "enmsTpLayerSet": enmsTpLayerSet,
       "enmsTpBandwidthTX": enmsTpBandwidthTX,
       "enmsTpBandwidthRX": enmsTpBandwidthRX,
       "enmsTpParentPortId": enmsTpParentPortId,
       "enmsTpParentTPIdH": enmsTpParentTPIdH,
       "enmsTpParentTPIdL": enmsTpParentTPIdL,
       "enmsTpFragmentLayer": enmsTpFragmentLayer,
       "enmsTpObjectType": enmsTpObjectType,
       "enmsTpMuxPartnerTPIdH": enmsTpMuxPartnerTPIdH,
       "enmsTpMuxPartnerTPIdL": enmsTpMuxPartnerTPIdL,
       "enmsPortConnTable": enmsPortConnTable,
       "enmsPortConnEntry": enmsPortConnEntry,
       "enmsPcPortConnId": enmsPcPortConnId,
       "enmsPcSrcNEId": enmsPcSrcNEId,
       "enmsPcSrcPortId": enmsPcSrcPortId,
       "enmsPcDstNEId": enmsPcDstNEId,
       "enmsPcDstPortId": enmsPcDstPortId,
       "enmsPcName": enmsPcName,
       "enmsPcSrcAlarmSeverity": enmsPcSrcAlarmSeverity,
       "enmsPcDstAlarmSeverity": enmsPcDstAlarmSeverity,
       "enmsPcBandwidth": enmsPcBandwidth,
       "enmsPcDirection": enmsPcDirection,
       "enmsPcLayerSet": enmsPcLayerSet,
       "enmsSNCTable": enmsSNCTable,
       "enmsSNCEntry": enmsSNCEntry,
       "enmsScSNCId": enmsScSNCId,
       "enmsScSrcNEId": enmsScSrcNEId,
       "enmsScSrcPortId": enmsScSrcPortId,
       "enmsScSrcTPIdH": enmsScSrcTPIdH,
       "enmsScSrcTPIdL": enmsScSrcTPIdL,
       "enmsScDestNEId": enmsScDestNEId,
       "enmsScDestPortId": enmsScDestPortId,
       "enmsScDestTPIdH": enmsScDestTPIdH,
       "enmsScDestTPIdL": enmsScDestTPIdL,
       "enmsScSrc2NEId": enmsScSrc2NEId,
       "enmsScSrc2PortId": enmsScSrc2PortId,
       "enmsScSrc2TPIdH": enmsScSrc2TPIdH,
       "enmsScSrc2TPIdL": enmsScSrc2TPIdL,
       "enmsScDest2NEId": enmsScDest2NEId,
       "enmsScDest2PortId": enmsScDest2PortId,
       "enmsScDest2TPIdH": enmsScDest2TPIdH,
       "enmsScDest2TPIdL": enmsScDest2TPIdL,
       "enmsScServiceId": enmsScServiceId,
       "enmsScName": enmsScName,
       "enmsScOpState": enmsScOpState,
       "enmsScAdminState": enmsScAdminState,
       "enmsScAlarmSeverity": enmsScAlarmSeverity,
       "enmsScBandwidth": enmsScBandwidth,
       "enmsScDirection": enmsScDirection,
       "enmsScProtectionFlag": enmsScProtectionFlag,
       "enmsScProtectionInfo": enmsScProtectionInfo,
       "enmsScNxCount": enmsScNxCount,
       "enmsScSNCOwnerId": enmsScSNCOwnerId,
       "enmsScLayerSet": enmsScLayerSet,
       "enmsScFragmentLayer": enmsScFragmentLayer,
       "enmsScMinBandwidth": enmsScMinBandwidth,
       "enmsScRequiredBandwidth": enmsScRequiredBandwidth,
       "enmsSNCTPTable": enmsSNCTPTable,
       "enmsSNCTPEntry": enmsSNCTPEntry,
       "enmsStSNCId": enmsStSNCId,
       "enmsStTPNumber": enmsStTPNumber,
       "enmsStNEId": enmsStNEId,
       "enmsStPortId": enmsStPortId,
       "enmsStTPIdH": enmsStTPIdH,
       "enmsStTPIdL": enmsStTPIdL,
       "enmsStIsWorkingTP": enmsStIsWorkingTP,
       "enmsStEndPointType": enmsStEndPointType,
       "enmsStTimeSlotHry": enmsStTimeSlotHry,
       "enmsSNCTHTable": enmsSNCTHTable,
       "enmsSNCTHEntry": enmsSNCTHEntry,
       "enmsThSNCId": enmsThSNCId,
       "enmsThTPNumber": enmsThTPNumber,
       "enmsThTPHierId": enmsThTPHierId,
       "enmsThChannelNo": enmsThChannelNo,
       "enmsCCTable": enmsCCTable,
       "enmsCCEntry": enmsCCEntry,
       "enmsCcNEId": enmsCcNEId,
       "enmsCcCCId": enmsCcCCId,
       "enmsCcSrcNEId": enmsCcSrcNEId,
       "enmsCcSrcPortId": enmsCcSrcPortId,
       "enmsCcSrcTPIdH": enmsCcSrcTPIdH,
       "enmsCcSrcTPIdL": enmsCcSrcTPIdL,
       "enmsCcDestNEId": enmsCcDestNEId,
       "enmsCcDestPortId": enmsCcDestPortId,
       "enmsCcDestTPIdH": enmsCcDestTPIdH,
       "enmsCcDestTPIdL": enmsCcDestTPIdL,
       "enmsCcSrc2NEId": enmsCcSrc2NEId,
       "enmsCcSrc2PortId": enmsCcSrc2PortId,
       "enmsCcSrc2TPIdH": enmsCcSrc2TPIdH,
       "enmsCcSrc2TPIdL": enmsCcSrc2TPIdL,
       "enmsCcDest2NEId": enmsCcDest2NEId,
       "enmsCcDest2PortId": enmsCcDest2PortId,
       "enmsCcDest2TPIdH": enmsCcDest2TPIdH,
       "enmsCcDest2TPIdL": enmsCcDest2TPIdL,
       "enmsCcOpState": enmsCcOpState,
       "enmsCcDirection": enmsCcDirection,
       "enmsCcProtectionFlag": enmsCcProtectionFlag,
       "enmsCcProtectionState": enmsCcProtectionState,
       "enmsCcNxCount": enmsCcNxCount,
       "enmsSNCSNCTable": enmsSNCSNCTable,
       "enmsSNCSNCEntry": enmsSNCSNCEntry,
       "enmsSsSNCId": enmsSsSNCId,
       "enmsSsServerSNCId": enmsSsServerSNCId,
       "enmsSNCCCTable": enmsSNCCCTable,
       "enmsSNCCCEntry": enmsSNCCCEntry,
       "enmsSNCCCSNCId": enmsSNCCCSNCId,
       "enmsSNCCCCCId": enmsSNCCCCCId,
       "enmsNeSNCTable": enmsNeSNCTable,
       "enmsNeSNCEntry": enmsNeSNCEntry,
       "enmsNeScNeId": enmsNeScNeId,
       "enmsNeScSNCId": enmsNeScSNCId,
       "enmsNeScSrcNEId": enmsNeScSrcNEId,
       "enmsNeScSrcPortId": enmsNeScSrcPortId,
       "enmsNeScSrcTPIdH": enmsNeScSrcTPIdH,
       "enmsNeScSrcTPIdL": enmsNeScSrcTPIdL,
       "enmsNeScDestNEId": enmsNeScDestNEId,
       "enmsNeScDestPortId": enmsNeScDestPortId,
       "enmsNeScDestTPIdH": enmsNeScDestTPIdH,
       "enmsNeScDestTPIdL": enmsNeScDestTPIdL,
       "enmsNeScSrc2NEId": enmsNeScSrc2NEId,
       "enmsNeScSrc2PortId": enmsNeScSrc2PortId,
       "enmsNeScSrc2TPIdH": enmsNeScSrc2TPIdH,
       "enmsNeScSrc2TPIdL": enmsNeScSrc2TPIdL,
       "enmsNeScDest2NEId": enmsNeScDest2NEId,
       "enmsNeScDest2PortId": enmsNeScDest2PortId,
       "enmsNeScDest2TPIdH": enmsNeScDest2TPIdH,
       "enmsNeScDest2TPIdL": enmsNeScDest2TPIdL,
       "enmsNeScServiceId": enmsNeScServiceId,
       "enmsNeScName": enmsNeScName,
       "enmsNeScOpState": enmsNeScOpState,
       "enmsNeScAdminState": enmsNeScAdminState,
       "enmsNeScAlarmSeverity": enmsNeScAlarmSeverity,
       "enmsNeScBandwidth": enmsNeScBandwidth,
       "enmsNeScDirection": enmsNeScDirection,
       "enmsNeScProtectionFlag": enmsNeScProtectionFlag,
       "enmsNeScProtectionInfo": enmsNeScProtectionInfo,
       "enmsNeScNxCount": enmsNeScNxCount,
       "enmsNeScSNCOwnerId": enmsNeScSNCOwnerId,
       "enmsNeScLayerSet": enmsNeScLayerSet,
       "enmsNeScFragmentLayer": enmsNeScFragmentLayer,
       "enmsNeScMinBandwidth": enmsNeScMinBandwidth,
       "enmsNeScRequiredBandwidth": enmsNeScRequiredBandwidth,
       "enmsEthernetPathTable": enmsEthernetPathTable,
       "enmsEthernetPathEntry": enmsEthernetPathEntry,
       "enmsEvcEthernetPathId": enmsEvcEthernetPathId,
       "enmsEvcName": enmsEvcName,
       "enmsEvcSVlanId": enmsEvcSVlanId,
       "enmsEvcType": enmsEvcType,
       "enmsEvcServiceId": enmsEvcServiceId,
       "enmsEvcOpState": enmsEvcOpState,
       "enmsEvcAdminState": enmsEvcAdminState,
       "enmsEvcAlarmSeverity": enmsEvcAlarmSeverity,
       "enmsService": enmsService,
       "enmsSubscriberTable": enmsSubscriberTable,
       "enmsSubscriberEntry": enmsSubscriberEntry,
       "enmsSbSubscriberId": enmsSbSubscriberId,
       "enmsSbName": enmsSbName,
       "enmsSbOrganisation": enmsSbOrganisation,
       "enmsSbContactPerson": enmsSbContactPerson,
       "enmsSbAddress": enmsSbAddress,
       "enmsSbPhone": enmsSbPhone,
       "enmsSbFax": enmsSbFax,
       "enmsSbEMail": enmsSbEMail,
       "enmsSbURL": enmsSbURL,
       "enmsSbExternalReference": enmsSbExternalReference,
       "enmsServiceTable": enmsServiceTable,
       "enmsServiceEntry": enmsServiceEntry,
       "enmsSvServiceId": enmsSvServiceId,
       "enmsSvSubscriberId": enmsSvSubscriberId,
       "enmsSvLabel": enmsSvLabel,
       "enmsSvOpState": enmsSvOpState,
       "enmsSvAdminState": enmsSvAdminState,
       "enmsSvDirection": enmsSvDirection,
       "enmsSvProtectionFlag": enmsSvProtectionFlag,
       "enmsSvWriteProtected": enmsSvWriteProtected,
       "enmsSvServiceOwnerId": enmsSvServiceOwnerId,
       "enmsAlarmTables": enmsAlarmTables,
       "enmsAlarmTable": enmsAlarmTable,
       "enmsAlarmEntry": enmsAlarmEntry,
       "enmsAlAlarmNumber": enmsAlAlarmNumber,
       "enmsAlSeverity": enmsAlSeverity,
       "enmsAlProbableCause": enmsAlProbableCause,
       "enmsAlClass": enmsAlClass,
       "enmsAlServiceAffect": enmsAlServiceAffect,
       "enmsAlState": enmsAlState,
       "enmsAlTimeStampFromNE": enmsAlTimeStampFromNE,
       "enmsAlTimeStamp": enmsAlTimeStamp,
       "enmsAlEntityString": enmsAlEntityString,
       "enmsAlEntityType": enmsAlEntityType,
       "enmsAlNEId": enmsAlNEId,
       "enmsAlPortId": enmsAlPortId,
       "enmsAlTPIdH": enmsAlTPIdH,
       "enmsAlTPIdL": enmsAlTPIdL,
       "enmsAlTPName": enmsAlTPName,
       "enmsAlModuleId": enmsAlModuleId,
       "enmsAlProbableCauseString": enmsAlProbableCauseString,
       "enmsAlNELocation": enmsAlNELocation,
       "enmsAlAffectedLocation": enmsAlAffectedLocation,
       "enmsAlTrafficDirection": enmsAlTrafficDirection,
       "enmsAlAdditionalInformation": enmsAlAdditionalInformation,
       "enmsAlNeSystemContainer": enmsAlNeSystemContainer,
       "enmsAlarmsForNETable": enmsAlarmsForNETable,
       "enmsAlarmsForNEEntry": enmsAlarmsForNEEntry,
       "enmsA2NEId": enmsA2NEId,
       "enmsA2Severity": enmsA2Severity,
       "enmsA2AlarmNumber": enmsA2AlarmNumber,
       "enmsA2ProbableCause": enmsA2ProbableCause,
       "enmsA2Class": enmsA2Class,
       "enmsA2ServiceAffect": enmsA2ServiceAffect,
       "enmsA2State": enmsA2State,
       "enmsA2TimeStampFromNE": enmsA2TimeStampFromNE,
       "enmsA2TimeStamp": enmsA2TimeStamp,
       "enmsA2EntityString": enmsA2EntityString,
       "enmsA2EntityType": enmsA2EntityType,
       "enmsA2PortId": enmsA2PortId,
       "enmsA2TPIdH": enmsA2TPIdH,
       "enmsA2TPIdL": enmsA2TPIdL,
       "enmsA2TPName": enmsA2TPName,
       "enmsA2ModuleId": enmsA2ModuleId,
       "enmsA2ProbableCauseString": enmsA2ProbableCauseString,
       "enmsA2NELocation": enmsA2NELocation,
       "enmsA2AffectedLocation": enmsA2AffectedLocation,
       "enmsA2TrafficDirection": enmsA2TrafficDirection,
       "enmsA2AdditionalInformation": enmsA2AdditionalInformation,
       "enmsA2NeSystemContainer": enmsA2NeSystemContainer,
       "enmsAlarmsForPortTable": enmsAlarmsForPortTable,
       "enmsAlarmsForPortEntry": enmsAlarmsForPortEntry,
       "enmsA3NEId": enmsA3NEId,
       "enmsA3PortId": enmsA3PortId,
       "enmsA3Severity": enmsA3Severity,
       "enmsA3AlarmNumber": enmsA3AlarmNumber,
       "enmsA3ProbableCause": enmsA3ProbableCause,
       "enmsA3Class": enmsA3Class,
       "enmsA3ServiceAffect": enmsA3ServiceAffect,
       "enmsA3State": enmsA3State,
       "enmsA3TimeStampFromNE": enmsA3TimeStampFromNE,
       "enmsA3TimeStamp": enmsA3TimeStamp,
       "enmsA3EntityString": enmsA3EntityString,
       "enmsA3EntityType": enmsA3EntityType,
       "enmsA3TPIdH": enmsA3TPIdH,
       "enmsA3TPIdL": enmsA3TPIdL,
       "enmsA3TPName": enmsA3TPName,
       "enmsA3ProbableCauseString": enmsA3ProbableCauseString,
       "enmsA3NELocation": enmsA3NELocation,
       "enmsA3AffectedLocation": enmsA3AffectedLocation,
       "enmsA3TrafficDirection": enmsA3TrafficDirection,
       "enmsA3AdditionalInformation": enmsA3AdditionalInformation,
       "enmsA3NeSystemContainer": enmsA3NeSystemContainer,
       "enmsAlarmsForTPTable": enmsAlarmsForTPTable,
       "enmsAlarmsForTPEntry": enmsAlarmsForTPEntry,
       "enmsA4NEId": enmsA4NEId,
       "enmsA4PortId": enmsA4PortId,
       "enmsA4TPIdH": enmsA4TPIdH,
       "enmsA4TPIdL": enmsA4TPIdL,
       "enmsA4Severity": enmsA4Severity,
       "enmsA4AlarmNumber": enmsA4AlarmNumber,
       "enmsA4ProbableCause": enmsA4ProbableCause,
       "enmsA4Class": enmsA4Class,
       "enmsA4ServiceAffect": enmsA4ServiceAffect,
       "enmsA4State": enmsA4State,
       "enmsA4TimeStampFromNE": enmsA4TimeStampFromNE,
       "enmsA4TimeStamp": enmsA4TimeStamp,
       "enmsA4EntityString": enmsA4EntityString,
       "enmsA4EntityType": enmsA4EntityType,
       "enmsA4TPName": enmsA4TPName,
       "enmsA4ProbableCauseString": enmsA4ProbableCauseString,
       "enmsA4NELocation": enmsA4NELocation,
       "enmsA4AffectedLocation": enmsA4AffectedLocation,
       "enmsA4TrafficDirection": enmsA4TrafficDirection,
       "enmsA4AdditionalInformation": enmsA4AdditionalInformation,
       "enmsA4NeSystemContainer": enmsA4NeSystemContainer,
       "enmsAlarmsForPortConnTable": enmsAlarmsForPortConnTable,
       "enmsAlarmsForPortConnEntry": enmsAlarmsForPortConnEntry,
       "enmsA5PortConnId": enmsA5PortConnId,
       "enmsA5Severity": enmsA5Severity,
       "enmsA5AlarmNumber": enmsA5AlarmNumber,
       "enmsA5ProbableCause": enmsA5ProbableCause,
       "enmsA5Class": enmsA5Class,
       "enmsA5ServiceAffect": enmsA5ServiceAffect,
       "enmsA5State": enmsA5State,
       "enmsA5TimeStampFromNE": enmsA5TimeStampFromNE,
       "enmsA5TimeStamp": enmsA5TimeStamp,
       "enmsA5EntityString": enmsA5EntityString,
       "enmsA5EntityType": enmsA5EntityType,
       "enmsA5NEId": enmsA5NEId,
       "enmsA5PortId": enmsA5PortId,
       "enmsA5TPIdH": enmsA5TPIdH,
       "enmsA5TPIdL": enmsA5TPIdL,
       "enmsA5TPName": enmsA5TPName,
       "enmsA5ModuleId": enmsA5ModuleId,
       "enmsA5ProbableCauseString": enmsA5ProbableCauseString,
       "enmsA5NELocation": enmsA5NELocation,
       "enmsA5AffectedLocation": enmsA5AffectedLocation,
       "enmsA5TrafficDirection": enmsA5TrafficDirection,
       "enmsA5AdditionalInformation": enmsA5AdditionalInformation,
       "enmsAlarmsForSNCTable": enmsAlarmsForSNCTable,
       "enmsAlarmsForSNCEntry": enmsAlarmsForSNCEntry,
       "enmsA6SNCId": enmsA6SNCId,
       "enmsA6Severity": enmsA6Severity,
       "enmsA6AlarmNumber": enmsA6AlarmNumber,
       "enmsA6ProbableCause": enmsA6ProbableCause,
       "enmsA6Class": enmsA6Class,
       "enmsA6ServiceAffect": enmsA6ServiceAffect,
       "enmsA6State": enmsA6State,
       "enmsA6TimeStampFromNE": enmsA6TimeStampFromNE,
       "enmsA6TimeStamp": enmsA6TimeStamp,
       "enmsA6EntityString": enmsA6EntityString,
       "enmsA6EntityType": enmsA6EntityType,
       "enmsA6NEId": enmsA6NEId,
       "enmsA6PortId": enmsA6PortId,
       "enmsA6TPIdH": enmsA6TPIdH,
       "enmsA6TPIdL": enmsA6TPIdL,
       "enmsA6TPName": enmsA6TPName,
       "enmsA6ModuleId": enmsA6ModuleId,
       "enmsA6ProbableCauseString": enmsA6ProbableCauseString,
       "enmsA6NELocation": enmsA6NELocation,
       "enmsA6AffectedLocation": enmsA6AffectedLocation,
       "enmsA6TrafficDirection": enmsA6TrafficDirection,
       "enmsA6AdditionalInformation": enmsA6AdditionalInformation,
       "enmsAlarmsForServiceTable": enmsAlarmsForServiceTable,
       "enmsAlarmsForServiceEntry": enmsAlarmsForServiceEntry,
       "enmsA7ServiceId": enmsA7ServiceId,
       "enmsA7Severity": enmsA7Severity,
       "enmsA7AlarmNumber": enmsA7AlarmNumber,
       "enmsA7ProbableCause": enmsA7ProbableCause,
       "enmsA7Class": enmsA7Class,
       "enmsA7ServiceAffect": enmsA7ServiceAffect,
       "enmsA7State": enmsA7State,
       "enmsA7TimeStampFromNE": enmsA7TimeStampFromNE,
       "enmsA7TimeStamp": enmsA7TimeStamp,
       "enmsA7EntityString": enmsA7EntityString,
       "enmsA7EntityType": enmsA7EntityType,
       "enmsA7NEId": enmsA7NEId,
       "enmsA7PortId": enmsA7PortId,
       "enmsA7TPIdH": enmsA7TPIdH,
       "enmsA7TPIdL": enmsA7TPIdL,
       "enmsA7TPName": enmsA7TPName,
       "enmsA7ModuleId": enmsA7ModuleId,
       "enmsA7ProbableCauseString": enmsA7ProbableCauseString,
       "enmsA7NELocation": enmsA7NELocation,
       "enmsA7AffectedLocation": enmsA7AffectedLocation,
       "enmsA7TrafficDirection": enmsA7TrafficDirection,
       "enmsA7AdditionalInformation": enmsA7AdditionalInformation,
       "enmsAlarmsForModuleTable": enmsAlarmsForModuleTable,
       "enmsAlarmsForModuleEntry": enmsAlarmsForModuleEntry,
       "enmsA8NEId": enmsA8NEId,
       "enmsA8ModuleId": enmsA8ModuleId,
       "enmsA8Severity": enmsA8Severity,
       "enmsA8AlarmNumber": enmsA8AlarmNumber,
       "enmsA8ProbableCause": enmsA8ProbableCause,
       "enmsA8Class": enmsA8Class,
       "enmsA8ServiceAffect": enmsA8ServiceAffect,
       "enmsA8State": enmsA8State,
       "enmsA8TimeStampFromNE": enmsA8TimeStampFromNE,
       "enmsA8TimeStamp": enmsA8TimeStamp,
       "enmsA8EntityString": enmsA8EntityString,
       "enmsA8EntityType": enmsA8EntityType,
       "enmsA8PortId": enmsA8PortId,
       "enmsA8TPIdH": enmsA8TPIdH,
       "enmsA8TPIdL": enmsA8TPIdL,
       "enmsA8TPName": enmsA8TPName,
       "enmsA8ProbableCauseString": enmsA8ProbableCauseString,
       "enmsA8NELocation": enmsA8NELocation,
       "enmsA8AffectedLocation": enmsA8AffectedLocation,
       "enmsA8TrafficDirection": enmsA8TrafficDirection,
       "enmsA8AdditionalInformation": enmsA8AdditionalInformation,
       "enmsA8NeSystemContainer": enmsA8NeSystemContainer,
       "enmsAlarmsForEthernetPathTable": enmsAlarmsForEthernetPathTable,
       "enmsAlarmsForEthernetPathEntry": enmsAlarmsForEthernetPathEntry,
       "enmsA9EthernetPathId": enmsA9EthernetPathId,
       "enmsA9Severity": enmsA9Severity,
       "enmsA9AlarmNumber": enmsA9AlarmNumber,
       "enmsA9ProbableCause": enmsA9ProbableCause,
       "enmsA9Class": enmsA9Class,
       "enmsA9ServiceAffect": enmsA9ServiceAffect,
       "enmsA9State": enmsA9State,
       "enmsA9TimeStampFromNE": enmsA9TimeStampFromNE,
       "enmsA9TimeStamp": enmsA9TimeStamp,
       "enmsA9EntityString": enmsA9EntityString,
       "enmsA9EntityType": enmsA9EntityType,
       "enmsA9NEId": enmsA9NEId,
       "enmsA9PortId": enmsA9PortId,
       "enmsA9TPIdH": enmsA9TPIdH,
       "enmsA9TPIdL": enmsA9TPIdL,
       "enmsA9TPName": enmsA9TPName,
       "enmsA9ModuleId": enmsA9ModuleId,
       "enmsA9ProbableCauseString": enmsA9ProbableCauseString,
       "enmsA9NELocation": enmsA9NELocation,
       "enmsA9AffectedLocation": enmsA9AffectedLocation,
       "enmsA9TrafficDirection": enmsA9TrafficDirection,
       "enmsA9AdditionalInformation": enmsA9AdditionalInformation,
       "enmsProxy": enmsProxy,
       "enmsCounter": enmsCounter,
       "enmsSNMPTrapCnt": enmsSNMPTrapCnt,
       "enmsSNMPGetCnt": enmsSNMPGetCnt,
       "enmsSNMPGetNextCnt": enmsSNMPGetNextCnt,
       "enmsSNMPSetCnt": enmsSNMPSetCnt,
       "enmsControl": enmsControl,
       "enmsProxyName": enmsProxyName,
       "enmsProxyOpState": enmsProxyOpState,
       "enmsNetworkName": enmsNetworkName,
       "enmsTrapHistoryTableLength": enmsTrapHistoryTableLength,
       "enmsTrapCounter": enmsTrapCounter,
       "enmsProxyPSTAMP": enmsProxyPSTAMP,
       "enmsEnterpriseId": enmsEnterpriseId,
       "enmsMIBVersion": enmsMIBVersion,
       "enmsEMSVersion": enmsEMSVersion,
       "enmsTimeStampFormat": enmsTimeStampFormat,
       "enmsHeartbeatInterval": enmsHeartbeatInterval,
       "enmsHeartbeatOpState": enmsHeartbeatOpState,
       "enmsInformTimeout": enmsInformTimeout,
       "enmsInformMaxTries": enmsInformMaxTries,
       "enmsTrapGroup": enmsTrapGroup,
       "enmsTrapHist": enmsTrapHist,
       "enmsTrapHistoryTable": enmsTrapHistoryTable,
       "enmsTrapHistoryEntry": enmsTrapHistoryEntry,
       "enmsHiTrapNumber": enmsHiTrapNumber,
       "enmsHiTrapEntityType": enmsHiTrapEntityType,
       "enmsHiTrapFirstId": enmsHiTrapFirstId,
       "enmsHiTrapSecondId": enmsHiTrapSecondId,
       "enmsHiTrapTPIdH": enmsHiTrapTPIdH,
       "enmsHiTrapTPIdL": enmsHiTrapTPIdL,
       "enmsHiTrapNfyType": enmsHiTrapNfyType,
       "enmsHiTrapCounter": enmsHiTrapCounter,
       "enmsTrapVariable": enmsTrapVariable,
       "enmsTrapTimeStamp": enmsTrapTimeStamp,
       "enmsTrapEventSeverity": enmsTrapEventSeverity,
       "enmsTrapEventDetails": enmsTrapEventDetails,
       "enmsTrapEventProbableCause": enmsTrapEventProbableCause,
       "enmsTrapStateName": enmsTrapStateName,
       "enmsTrapStateOldValue": enmsTrapStateOldValue,
       "enmsTrapStateNewValue": enmsTrapStateNewValue,
       "enmsTrapAttributeName": enmsTrapAttributeName,
       "enmsTrapAttributeOldValue": enmsTrapAttributeOldValue,
       "enmsTrapAttributeNewValue": enmsTrapAttributeNewValue,
       "enmsTrapEventProbableCauseString": enmsTrapEventProbableCauseString,
       "enmsTrapNeIdName": enmsTrapNeIdName,
       "enmsTrapNeLocationLct": enmsTrapNeLocationLct,
       "enmsTrapAffectedLocation": enmsTrapAffectedLocation,
       "enmsTrapEventTrafficDirection": enmsTrapEventTrafficDirection,
       "enmsTraps": enmsTraps,
       "enmsCommonTraps": enmsCommonTraps,
       "enmsProxyStateChangeTrap": enmsProxyStateChangeTrap,
       "enmsNETraps": enmsNETraps,
       "enmsNEObjectCreationTrap": enmsNEObjectCreationTrap,
       "enmsNEObjectDeletionTrap": enmsNEObjectDeletionTrap,
       "enmsNEStateChangeTrap": enmsNEStateChangeTrap,
       "enmsNEAttributeChangeTrap": enmsNEAttributeChangeTrap,
       "enmsNEAlarmTrap": enmsNEAlarmTrap,
       "enmsModuleTraps": enmsModuleTraps,
       "enmsModuleObjectCreationTrap": enmsModuleObjectCreationTrap,
       "enmsModuleObjectDeletionTrap": enmsModuleObjectDeletionTrap,
       "enmsModuleStateChangeTrap": enmsModuleStateChangeTrap,
       "enmsModuleAttributeChangeTrap": enmsModuleAttributeChangeTrap,
       "enmsModuleAlarmTrap": enmsModuleAlarmTrap,
       "enmsPortTraps": enmsPortTraps,
       "enmsPortObjectCreationTrap": enmsPortObjectCreationTrap,
       "enmsPortObjectDeletionTrap": enmsPortObjectDeletionTrap,
       "enmsPortStateChangeTrap": enmsPortStateChangeTrap,
       "enmsPortAttributeChangeTrap": enmsPortAttributeChangeTrap,
       "enmsPortAlarmTrap": enmsPortAlarmTrap,
       "enmsTPTraps": enmsTPTraps,
       "enmsTPObjectCreationTrap": enmsTPObjectCreationTrap,
       "enmsTPObjectDeletionTrap": enmsTPObjectDeletionTrap,
       "enmsTPStateChangeTrap": enmsTPStateChangeTrap,
       "enmsTPAttributeChangeTrap": enmsTPAttributeChangeTrap,
       "enmsTPAlarmTrap": enmsTPAlarmTrap,
       "enmsPortConnTraps": enmsPortConnTraps,
       "enmsPortConnObjectCreationTrap": enmsPortConnObjectCreationTrap,
       "enmsPortConnObjectDeletionTrap": enmsPortConnObjectDeletionTrap,
       "enmsPortConnAttributeChangeTrap": enmsPortConnAttributeChangeTrap,
       "enmsSNCTraps": enmsSNCTraps,
       "enmsSNCObjectCreationTrap": enmsSNCObjectCreationTrap,
       "enmsSNCObjectDeletionTrap": enmsSNCObjectDeletionTrap,
       "enmsSNCStateChangeTrap": enmsSNCStateChangeTrap,
       "enmsSNCAttributeChangeTrap": enmsSNCAttributeChangeTrap,
       "enmsSNCTPRelationshipChangeTrap": enmsSNCTPRelationshipChangeTrap,
       "enmsSubscriberTraps": enmsSubscriberTraps,
       "enmsSubscriberObjectCreationTrap": enmsSubscriberObjectCreationTrap,
       "enmsSubscriberObjectDeletionTrap": enmsSubscriberObjectDeletionTrap,
       "enmsSubscriberAttributeChangeTrap": enmsSubscriberAttributeChangeTrap,
       "enmsServiceTraps": enmsServiceTraps,
       "enmsServiceObjectCreationTrap": enmsServiceObjectCreationTrap,
       "enmsServiceObjectDeletionTrap": enmsServiceObjectDeletionTrap,
       "enmsServiceStateChangeTrap": enmsServiceStateChangeTrap,
       "enmsServiceAttributeChangeTrap": enmsServiceAttributeChangeTrap,
       "enmsEMSTraps": enmsEMSTraps,
       "enmsEMSAlarmTrap": enmsEMSAlarmTrap,
       "enmsMonitorTraps": enmsMonitorTraps,
       "enmsHeartbeatTrap": enmsHeartbeatTrap,
       "enmsEthernetPathTraps": enmsEthernetPathTraps,
       "enmsEthernetPathObjectCreationTrap": enmsEthernetPathObjectCreationTrap,
       "enmsEthernetPathObjectDeletionTrap": enmsEthernetPathObjectDeletionTrap,
       "enmsEthernetPathStateChangeTrap": enmsEthernetPathStateChangeTrap,
       "enmsEthernetPathAttributeChangeTrap": enmsEthernetPathAttributeChangeTrap,
       "enmsPerfMonTraps": enmsPerfMonTraps,
       "enmsPerfMonRequestStateChangeTrap": enmsPerfMonRequestStateChangeTrap,
       "enmsOptPowerMonTraps": enmsOptPowerMonTraps,
       "enmsOptPowerMonRequestStateChangeTrap": enmsOptPowerMonRequestStateChangeTrap,
       "enmsTrapFilter": enmsTrapFilter,
       "enmsCommonTrapFilter": enmsCommonTrapFilter,
       "enmsNETrapFilter": enmsNETrapFilter,
       "enmsModuleTrapFilter": enmsModuleTrapFilter,
       "enmsPortTrapFilter": enmsPortTrapFilter,
       "enmsTPTrapFilter": enmsTPTrapFilter,
       "enmsPortConnTrapFilter": enmsPortConnTrapFilter,
       "enmsSNCTrapFilter": enmsSNCTrapFilter,
       "enmsSubscriberTrapFilter": enmsSubscriberTrapFilter,
       "enmsServiceTrapFilter": enmsServiceTrapFilter,
       "enmsNEAlarmTrapFilter": enmsNEAlarmTrapFilter,
       "enmsModuleAlarmTrapFilter": enmsModuleAlarmTrapFilter,
       "enmsPortAlarmTrapFilter": enmsPortAlarmTrapFilter,
       "enmsTPAlarmTrapFilter": enmsTPAlarmTrapFilter,
       "enmsEMSAlarmTrapFilter": enmsEMSAlarmTrapFilter,
       "enmsNeIdNameFilter": enmsNeIdNameFilter,
       "enmsMonitorTrapFilter": enmsMonitorTrapFilter,
       "enmsEthernetPathTrapFilter": enmsEthernetPathTrapFilter,
       "enmsPerfMonTrapFilter": enmsPerfMonTrapFilter,
       "enmsOptPowerMonTrapFilter": enmsOptPowerMonTrapFilter,
       "enmsPerfMon": enmsPerfMon,
       "enmsPmRequestNextId": enmsPmRequestNextId,
       "enmsPerfMonRequestTable": enmsPerfMonRequestTable,
       "enmsPerfMonRequestEntry": enmsPerfMonRequestEntry,
       "enmsPmRequestId": enmsPmRequestId,
       "enmsPmRequestName": enmsPmRequestName,
       "enmsPmRequestRowStatus": enmsPmRequestRowStatus,
       "enmsPmRequestLastUpdate": enmsPmRequestLastUpdate,
       "enmsPmRequestInfo": enmsPmRequestInfo,
       "enmsPmRequestState": enmsPmRequestState,
       "enmsPmRequestType": enmsPmRequestType,
       "enmsPmRequestStartTime": enmsPmRequestStartTime,
       "enmsPmRequestEndTime": enmsPmRequestEndTime,
       "enmsPmRequestGranularity": enmsPmRequestGranularity,
       "enmsPmRequestFilterType": enmsPmRequestFilterType,
       "enmsPmRequestFilterValue": enmsPmRequestFilterValue,
       "enmsPerfMonResultPmpTable": enmsPerfMonResultPmpTable,
       "enmsPerfMonResultPmpEntry": enmsPerfMonResultPmpEntry,
       "enmsPmResultPmpReqId": enmsPmResultPmpReqId,
       "enmsPmResultPmpPmpNumber": enmsPmResultPmpPmpNumber,
       "enmsPmResultPmpNeId": enmsPmResultPmpNeId,
       "enmsPmResultPmpPortId": enmsPmResultPmpPortId,
       "enmsPmResultPmpTPIdH": enmsPmResultPmpTPIdH,
       "enmsPmResultPmpTPIdL": enmsPmResultPmpTPIdL,
       "enmsPmResultPmpNeIdName": enmsPmResultPmpNeIdName,
       "enmsPmResultPmpObjLocation": enmsPmResultPmpObjLocation,
       "enmsPmResultPmpName": enmsPmResultPmpName,
       "enmsPmResultPmpLocation": enmsPmResultPmpLocation,
       "enmsPmResultPmpDirection": enmsPmResultPmpDirection,
       "enmsPmResultPmpRetrievalTime": enmsPmResultPmpRetrievalTime,
       "enmsPmResultPmpPeriodEndTime": enmsPmResultPmpPeriodEndTime,
       "enmsPmResultPmpMonitoredTime": enmsPmResultPmpMonitoredTime,
       "enmsPmResultPmpNumValues": enmsPmResultPmpNumValues,
       "enmsPmResultPmpRelatedPaths": enmsPmResultPmpRelatedPaths,
       "enmsPmResultPmpRelatedServices": enmsPmResultPmpRelatedServices,
       "enmsPmResultPmpRelatedSubscribers": enmsPmResultPmpRelatedSubscribers,
       "enmsPerfMonResultValueTable": enmsPerfMonResultValueTable,
       "enmsPerfMonResultValueEntry": enmsPerfMonResultValueEntry,
       "enmsPmResultValReqId": enmsPmResultValReqId,
       "enmsPmResultValPmpNumber": enmsPmResultValPmpNumber,
       "enmsPmResultValNumber": enmsPmResultValNumber,
       "enmsPmResultValParam": enmsPmResultValParam,
       "enmsPmResultValValue": enmsPmResultValValue,
       "enmsPmResultValUnit": enmsPmResultValUnit,
       "enmsPmResultValStatus": enmsPmResultValStatus,
       "enmsPerfMonResultThresholdTable": enmsPerfMonResultThresholdTable,
       "enmsPerfMonResultThresholdEntry": enmsPerfMonResultThresholdEntry,
       "enmsPmResultThresholdReqId": enmsPmResultThresholdReqId,
       "enmsPmResultThresholdPmpNumber": enmsPmResultThresholdPmpNumber,
       "enmsPmResultThresholdNumber": enmsPmResultThresholdNumber,
       "enmsPmResultThresholdParam": enmsPmResultThresholdParam,
       "enmsPmResultThresholdType": enmsPmResultThresholdType,
       "enmsPmResultThresholdTriggerFlag": enmsPmResultThresholdTriggerFlag,
       "enmsPmResultThresholdValue": enmsPmResultThresholdValue,
       "enmsPmResultThresholdUnit": enmsPmResultThresholdUnit,
       "enmsOptPowerMon": enmsOptPowerMon,
       "enmsOpmRequestNextId": enmsOpmRequestNextId,
       "enmsOptPowerMonRequestTable": enmsOptPowerMonRequestTable,
       "enmsOptPowerMonRequestEntry": enmsOptPowerMonRequestEntry,
       "enmsOpmRequestId": enmsOpmRequestId,
       "enmsOpmRequestName": enmsOpmRequestName,
       "enmsOpmRequestRowStatus": enmsOpmRequestRowStatus,
       "enmsOpmRequestLastUpdate": enmsOpmRequestLastUpdate,
       "enmsOpmRequestInfo": enmsOpmRequestInfo,
       "enmsOpmRequestState": enmsOpmRequestState,
       "enmsOpmRequestFilterType": enmsOpmRequestFilterType,
       "enmsOpmRequestFilterValue": enmsOpmRequestFilterValue,
       "enmsOptPowerMonResultValueTable": enmsOptPowerMonResultValueTable,
       "enmsOptPowerMonResultValueEntry": enmsOptPowerMonResultValueEntry,
       "enmsOpmResultValReqId": enmsOpmResultValReqId,
       "enmsOpmResultValNumber": enmsOpmResultValNumber,
       "enmsOpmResultValNeId": enmsOpmResultValNeId,
       "enmsOpmResultValPortId": enmsOpmResultValPortId,
       "enmsOpmResultValTPIdH": enmsOpmResultValTPIdH,
       "enmsOpmResultValTPIdL": enmsOpmResultValTPIdL,
       "enmsOpmResultValNeIdName": enmsOpmResultValNeIdName,
       "enmsOpmResultValObjLocation": enmsOpmResultValObjLocation,
       "enmsOpmResultValLane": enmsOpmResultValLane,
       "enmsOpmResultValLayer": enmsOpmResultValLayer,
       "enmsOpmResultValParam": enmsOpmResultValParam,
       "enmsOpmResultValValue": enmsOpmResultValValue,
       "enmsOpmResultValUnit": enmsOpmResultValUnit}
)
