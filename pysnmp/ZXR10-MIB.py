# SNMP MIB module (ZXR10-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:57 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt")

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class AvailStatus(Integer32):
    """Custom type AvailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 0))
    )





class OperStatus(Integer32):
    """Custom type OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )





class PortProperty(Integer32):
    """Custom type PortProperty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("console", 4),
          ("electricity", 1),
          ("phoelecmix", 3),
          ("photo", 0))
    )





class MasterStatus(Integer32):
    """Custom type MasterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("member", 3),
          ("slave", 2))
    )





class UnitRunStatus(Integer32):
    """Custom type UnitRunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )





class PidUsedStatus(Integer32):
    """Custom type PidUsedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("used", 1))
    )





class BoolStatus(Integer32):
    """Custom type BoolStatus based on Integer32"""
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





class ProductID(Integer32):
    """Custom type ProductID based on Integer32"""
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
              42,
              43,
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
              417,
              418,
              419,
              420,
              5000)
        )
    )
    namedValues = NamedValues(
        *(("zxctn-6100", 409),
          ("zxr10RouterR10-1811-AC", 106),
          ("zxr10RouterR10-1811-DC", 107),
          ("zxr10RouterR10-1811E-AC", 114),
          ("zxr10RouterR10-1811E-DC", 115),
          ("zxr10RouterR10-1812-AC", 104),
          ("zxr10RouterR10-1812-DC", 105),
          ("zxr10RouterR10-1812E-AC", 112),
          ("zxr10RouterR10-1812E-DC", 113),
          ("zxr10RouterR10-1821-AC", 102),
          ("zxr10RouterR10-1821-DC", 103),
          ("zxr10RouterR10-1821E-AC", 110),
          ("zxr10RouterR10-1821E-DC", 111),
          ("zxr10RouterR10-1822-AC", 100),
          ("zxr10RouterR10-1822-DC", 101),
          ("zxr10RouterR10-1822E-AC", 108),
          ("zxr10RouterR10-1822E-DC", 109),
          ("zxr10RouterR10-1841-AC", 196),
          ("zxr10RouterR10-1841-DC", 200),
          ("zxr10RouterR10-1842-AC", 197),
          ("zxr10RouterR10-1842-DC", 201),
          ("zxr10RouterR10-1843-AC", 198),
          ("zxr10RouterR10-1843-DC", 202),
          ("zxr10RouterR10-1844-AC", 199),
          ("zxr10RouterR10-1844-DC", 203),
          ("zxr10RouterR10-2821-AC", 188),
          ("zxr10RouterR10-2821-DC", 192),
          ("zxr10RouterR10-2822-AC", 189),
          ("zxr10RouterR10-2822-DC", 193),
          ("zxr10RouterR10-2823-AC", 190),
          ("zxr10RouterR10-2823-DC", 194),
          ("zxr10RouterR10-2824-AC", 191),
          ("zxr10RouterR10-2824-DC", 195),
          ("zxr10RouterR10-2841-AC", 172),
          ("zxr10RouterR10-2841-DC", 176),
          ("zxr10RouterR10-2842-AC", 173),
          ("zxr10RouterR10-2842-DC", 177),
          ("zxr10RouterR10-2843-AC", 174),
          ("zxr10RouterR10-2843-DC", 178),
          ("zxr10RouterR10-2844-AC", 175),
          ("zxr10RouterR10-2844-DC", 179),
          ("zxr10RouterR10-2881-AC", 180),
          ("zxr10RouterR10-2881-DC", 184),
          ("zxr10RouterR10-2882-AC", 181),
          ("zxr10RouterR10-2882-DC", 185),
          ("zxr10RouterR10-2883-AC", 182),
          ("zxr10RouterR10-2883-DC", 186),
          ("zxr10RouterR10-2884-AC", 183),
          ("zxr10RouterR10-2884-DC", 187),
          ("zxr10RouterR10-3821-AC", 148),
          ("zxr10RouterR10-3821-DC", 152),
          ("zxr10RouterR10-3822-AC", 149),
          ("zxr10RouterR10-3822-DC", 153),
          ("zxr10RouterR10-3823-AC", 150),
          ("zxr10RouterR10-3823-DC", 154),
          ("zxr10RouterR10-3824-AC", 151),
          ("zxr10RouterR10-3824-DC", 155),
          ("zxr10RouterR10-3841-AC", 140),
          ("zxr10RouterR10-3841-DC", 144),
          ("zxr10RouterR10-3842-AC", 141),
          ("zxr10RouterR10-3842-DC", 145),
          ("zxr10RouterR10-3843-AC", 142),
          ("zxr10RouterR10-3843-DC", 146),
          ("zxr10RouterR10-3844-AC", 143),
          ("zxr10RouterR10-3844-DC", 147),
          ("zxr10RouterR10-3881-AC", 132),
          ("zxr10RouterR10-3881-DC", 136),
          ("zxr10RouterR10-3882-AC", 133),
          ("zxr10RouterR10-3882-DC", 137),
          ("zxr10RouterR10-3883-AC", 134),
          ("zxr10RouterR10-3883-DC", 138),
          ("zxr10RouterR10-3884-AC", 135),
          ("zxr10RouterR10-3884-DC", 139),
          ("zxr10RouterT1200", 26),
          ("zxr10RouterT128", 1),
          ("zxr10RouterT32", 3),
          ("zxr10RouterT600", 27),
          ("zxr10RouterT64", 2),
          ("zxr10Routergar-2604", 6),
          ("zxr10Routergar-2608", 4),
          ("zxr10Routergar-3608", 8),
          ("zxr10Routergar-7208", 9),
          ("zxr10Routerger2", 28),
          ("zxr10Routerger4", 29),
          ("zxr10Routerger8", 5),
          ("zxr10Switch-6902", 402),
          ("zxr10Switch-6905", 403),
          ("zxr10Switch-6907", 400),
          ("zxr10Switch-6908", 404),
          ("zxr10Switch-8902", 405),
          ("zxr10Switch-8905", 406),
          ("zxr10Switch-8908", 407),
          ("zxr10Switch-8912", 408),
          ("zxr10Switch-T240G", 401),
          ("zxr10Switch3206", 11),
          ("zxr10Switch3226", 24),
          ("zxr10Switch3226FI", 30),
          ("zxr10Switch3228", 13),
          ("zxr10Switch3228A", 35),
          ("zxr10Switch3228A-EI", 34),
          ("zxr10Switch3228A-FI", 36),
          ("zxr10Switch3252", 15),
          ("zxr10Switch3252A", 37),
          ("zxr10Switch3906", 12),
          ("zxr10Switch3928", 14),
          ("zxr10Switch3928A", 31),
          ("zxr10Switch3928A-PS", 418),
          ("zxr10Switch3928AFI", 32),
          ("zxr10Switch3928E", 419),
          ("zxr10Switch3928E-FI", 420),
          ("zxr10Switch3952", 16),
          ("zxr10Switch3952A", 33),
          ("zxr10Switch3952E", 42),
          ("zxr10Switch5224", 17),
          ("zxr10Switch5228", 18),
          ("zxr10Switch5228A", 38),
          ("zxr10Switch5228F", 19),
          ("zxr10Switch5252", 22),
          ("zxr10Switch5252A", 39),
          ("zxr10Switch5928", 20),
          ("zxr10Switch5928-PS", 417),
          ("zxr10Switch5928F", 21),
          ("zxr10Switch5952", 23),
          ("zxr10Switch5952E", 43),
          ("zxr10SwitchT160G", 7),
          ("zxr10SwitchT40G", 25),
          ("zxr10SwitchT64G", 10),
          ("zxr10UAS10600", 5000))
    )





class BoardType(Integer32):
    """Custom type BoardType based on Integer32"""
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
        *(("mcp-board", 6),
          ("mec-board", 4),
          ("npc-board", 3),
          ("sfc-board", 2),
          ("smp-board", 5),
          ("upc-board", 1))
    )





class NpcType(Integer32):
    """Custom type NpcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              129,
              130,
              131,
              161,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
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
              542,
              543,
              544,
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
              1085,
              1086,
              1087,
              1088,
              1089,
              1090,
              1091,
              1092,
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
              1168,
              1169,
              1170,
              1171,
              1172,
              1173,
              1174,
              1175,
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
              1235,
              1236,
              1237,
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
              2051,
              2052,
              2053,
              2054,
              2055,
              2564,
              2565,
              2566,
              2567,
              2568,
              2569,
              2570,
              2571,
              2572,
              2573,
              2574,
              3077,
              3078,
              3079,
              3080,
              3081,
              4103,
              4104,
              4609,
              4610,
              4611,
              4616,
              4617,
              4865,
              4866,
              4867,
              5001,
              5101,
              5102,
              5103,
              5129,
              5130,
              5131,
              5132,
              5133,
              5134,
              5135,
              5136,
              5137,
              5138,
              5139,
              5201,
              5301,
              5401,
              5642,
              5643,
              5644,
              5645,
              5646,
              5647)
        )
    )
    namedValues = NamedValues(
        *(("card-10gei-1", 1049),
          ("card-SF-24GE-H3", 1237),
          ("card-USFF-H3", 1236),
          ("card-UVFF-H3", 1229),
          ("card-UVSF-H3", 1228),
          ("card-UVTF-H3", 1235),
          ("card-UWSF-H3", 1230),
          ("card-atm155", 2051),
          ("card-atm155-4", 2055),
          ("card-atm155-8", 2053),
          ("card-atm155-rev", 2054),
          ("card-atm622", 2052),
          ("card-aux", 5130),
          ("card-bpts", 4867),
          ("card-ces", 180),
          ("card-cip", 181),
          ("card-dialer", 170),
          ("card-e1-16", 2564),
          ("card-e1-32", 2565),
          ("card-e1-c", 2567),
          ("card-e1-c-1", 2571),
          ("card-e1-c-2", 2572),
          ("card-e1-c-32", 2566),
          ("card-e1-c-4", 2568),
          ("card-e1-c-8", 2569),
          ("card-e1-c-8-ixbus", 2570),
          ("card-e1-c-8-pm7366", 2574),
          ("card-e1te", 4610),
          ("card-e1vi", 2573),
          ("card-e3", 4617),
          ("card-e3-c", 4616),
          ("card-fei-1", 517),
          ("card-fei-16", 525),
          ("card-fei-2", 526),
          ("card-fei-24", 524),
          ("card-fei-24-2-fi", 542),
          ("card-fei-24e", 532),
          ("card-fei-24eo", 533),
          ("card-fei-4", 527),
          ("card-fei-44-4-e", 522),
          ("card-fei-44-4-e-ez", 523),
          ("card-fei-44-4-fi", 529),
          ("card-fei-44-4-fi-ez", 530),
          ("card-fei-48", 520),
          ("card-fei-48-4-fi", 544),
          ("card-fei-8", 512),
          ("card-fei-b", 514),
          ("card-fei-b-es", 519),
          ("card-fei-b2", 518),
          ("card-fei-e", 516),
          ("card-fei-f", 513),
          ("card-fei-o", 515),
          ("card-fei-o-16", 528),
          ("card-fei-o24-2-fi", 543),
          ("card-fei-o8", 521),
          ("card-ge24a", 1206),
          ("card-ge24d", 1227),
          ("card-ge48a", 1205),
          ("card-gei-1", 1050),
          ("card-gei-10", 1059),
          ("card-gei-10-b", 1067),
          ("card-gei-12", 1034),
          ("card-gei-12-4e", 1039),
          ("card-gei-12-4e-ez", 1044),
          ("card-gei-1o-1e", 1063),
          ("card-gei-2", 1029),
          ("card-gei-24", 1038),
          ("card-gei-24-4e", 1040),
          ("card-gei-24-n-ez", 1076),
          ("card-gei-24ec", 1071),
          ("card-gei-24ec-den", 1085),
          ("card-gei-24ec-lit", 1079),
          ("card-gei-24ec-x11", 1105),
          ("card-gei-24ef", 1072),
          ("card-gei-24ef-den", 1086),
          ("card-gei-24ef-lit", 1080),
          ("card-gei-24ef-x11", 1104),
          ("card-gei-24f-fg", 1089),
          ("card-gei-24f-fg-den", 1091),
          ("card-gei-24f-fg-lit", 1090),
          ("card-gei-24hec", 1092),
          ("card-gei-24hec-den", 1094),
          ("card-gei-24hec-lit", 1093),
          ("card-gei-24hec-x11", 1108),
          ("card-gei-24hef", 1095),
          ("card-gei-24hef-den", 1097),
          ("card-gei-24hef-lit", 1096),
          ("card-gei-24hef-x11", 1106),
          ("card-gei-24hf-fg", 1098),
          ("card-gei-24hf-fg-den", 1100),
          ("card-gei-24hf-fg-lit", 1099),
          ("card-gei-24o-4e", 1052),
          ("card-gei-2e", 1061),
          ("card-gei-2o", 1062),
          ("card-gei-4", 1060),
          ("card-gei-4-12e", 1046),
          ("card-gei-4-12e-ez", 1048),
          ("card-gei-4-24e", 1047),
          ("card-gei-4-b", 1068),
          ("card-gei-4-d", 1113),
          ("card-gei-48ec", 1073),
          ("card-gei-48ec-den", 1087),
          ("card-gei-48ec-lit", 1081),
          ("card-gei-48ec-x11", 1109),
          ("card-gei-48ef", 1074),
          ("card-gei-48ef-den", 1088),
          ("card-gei-48ef-den-replace-ufsf", 1223),
          ("card-gei-48ef-lit", 1082),
          ("card-gei-48ef-replace-ufsf", 1224),
          ("card-gei-48ef-x11", 1107),
          ("card-gei-48f-fg", 1101),
          ("card-gei-48f-fg-den", 1103),
          ("card-gei-48f-fg-lit", 1102),
          ("card-gei-4b", 1066),
          ("card-gei-4o-24e-l", 1051),
          ("card-gei-4oi-24e", 1189),
          ("card-gei-4oi-48e", 1188),
          ("card-gei-8", 1025),
          ("card-gei-8-p4", 1064),
          ("card-gei-8-p4-ez", 1065),
          ("card-gei-8e", 1143),
          ("card-gei-8f", 1140),
          ("card-gei-e", 1032),
          ("card-gei-e-sfp", 1139),
          ("card-gei-f-2", 1058),
          ("card-gei-g-1", 1027),
          ("card-gei-g-2", 1028),
          ("card-gei-g-2-es", 1033),
          ("card-gei-h2", 1037),
          ("card-gei-h4", 1036),
          ("card-gei-l", 1026),
          ("card-gei-o", 1030),
          ("card-gei-o-g", 1031),
          ("card-gei-t2", 1045),
          ("card-gei-x", 1035),
          ("card-gei-x-1-ez", 1042),
          ("card-gei-x-1e", 1055),
          ("card-gei-x-1e-d", 1056),
          ("card-gei-x-1o-la", 1054),
          ("card-gei-x-1o-w", 1053),
          ("card-gei-x-2", 1041),
          ("card-gei-x-2ef", 1069),
          ("card-gei-x-2ef-den", 1083),
          ("card-gei-x-2ef-lit", 1077),
          ("card-gei-x-2ef-x11", 1110),
          ("card-gei-x-4ef", 1070),
          ("card-gei-x-4ef-den", 1084),
          ("card-gei-x-4ef-lit", 1078),
          ("card-gei-x-4ef-x11", 1111),
          ("card-gei-x-4o-48e", 1057),
          ("card-gei-x-8ef", 1114),
          ("card-gei-x-ez", 1043),
          ("card-gre", 163),
          ("card-l2tpdialer", 176),
          ("card-lffxs-2", 5135),
          ("card-lffxs-4", 5134),
          ("card-lfxo", 5133),
          ("card-lfxs", 5131),
          ("card-lhs", 5129),
          ("card-lhsu", 5132),
          ("card-loopback", 161),
          ("card-manage", 128),
          ("card-manage-lct", 131),
          ("card-manage-qx", 130),
          ("card-manage-qx-lct", 4611),
          ("card-manage-spec", 129),
          ("card-mefes", 534),
          ("card-megfs", 537),
          ("card-mfe-2", 531),
          ("card-mfef", 535),
          ("card-mfef-2", 539),
          ("card-mhs16", 5138),
          ("card-mhs8", 5137),
          ("card-mndec", 5139),
          ("card-mpc-tmcs-8-hg", 5643),
          ("card-mpc-tmcs-non-hg", 5642),
          ("card-mpc-umcs-12-hg", 5644),
          ("card-mpc-umcs-16-hg", 5645),
          ("card-mpc-umct-24-hg", 5646),
          ("card-mpc-umcu-12-hg", 5647),
          ("card-mppp", 165),
          ("card-msfes", 538),
          ("card-msgfs", 536),
          ("card-ndec", 5136),
          ("card-null", 167),
          ("card-oc12", 1540),
          ("card-oc192-1-ez", 1549),
          ("card-oc192b-1-ez", 1552),
          ("card-oc3", 1538),
          ("card-oc3-4", 1539),
          ("card-oc3-8", 1548),
          ("card-oc3-8-pm5351", 1550),
          ("card-oc3-c", 1543),
          ("card-oc3-c-2", 1551),
          ("card-oc48", 1541),
          ("card-oc48-2", 1542),
          ("card-oc48-2-dl", 1547),
          ("card-oc48-4", 1554),
          ("card-oc48-c", 1544),
          ("card-oc48-dl", 1545),
          ("card-oc48-sg", 1546),
          ("card-oc48f", 1553),
          ("card-port-channel", 168),
          ("card-qinq", 177),
          ("card-smb", 4609),
          ("card-stack", 1142),
          ("card-superpvc", 175),
          ("card-superqinq", 178),
          ("card-supervlan", 169),
          ("card-sygf-clkc-mmpi", 4865),
          ("card-sygf-gei-12ef-2x", 1168),
          ("card-sygf-gei-12ef-2x-clock", 1172),
          ("card-sygf-gei-12ef-2x-den", 1169),
          ("card-sygf-gei-12ef-2x-den-clock", 1173),
          ("card-sygf-gei-12ef-2x-den-ez", 1171),
          ("card-sygf-gei-12ef-2x-den-ez-clock", 1175),
          ("card-sygf-gei-12ef-2x-ez", 1170),
          ("card-sygf-gei-12ef-2x-ez-clock", 1174),
          ("card-t1-4", 3078),
          ("card-t1-c-1", 3079),
          ("card-t1-c-2", 3080),
          ("card-t1-c-4", 3077),
          ("card-t1-c-8-pm7366", 3081),
          ("card-t3", 4104),
          ("card-t3-c", 4103),
          ("card-tunnel", 164),
          ("card-ugse-gei-48ec", 1115),
          ("card-ugse-gei-48ec-den", 1117),
          ("card-ugse-gei-48ec-lit", 1116),
          ("card-ugsf-gei-48ef", 1118),
          ("card-ugsf-gei-48ef-den", 1120),
          ("card-ugsf-gei-48ef-lit", 1119),
          ("card-umhf-gei-x-2ef", 1184),
          ("card-umhf-gei-x-2ef-1ez", 1185),
          ("card-umhf-gei-x-2ef-1ez-left", 1187),
          ("card-umhf-gei-x-2ef-2ez", 1186),
          ("card-umhf-gei-x-4ef", 1144),
          ("card-umhf-gei-x-4ef-1ez", 1145),
          ("card-umhf-gei-x-4ef-1ez-left", 1147),
          ("card-umhf-gei-x-4ef-2ez", 1146),
          ("card-umop-12gefi-12epon", 1190),
          ("card-umop-12gefi-12epon-den", 1191),
          ("card-umop-12gefi-12epon-den-ez", 1193),
          ("card-umop-12gefi-12epon-ez", 1192),
          ("card-umop-12gefi-4epon", 1198),
          ("card-umop-12gefi-4epon-den", 1199),
          ("card-umop-12gefi-4epon-den-ez", 1201),
          ("card-umop-12gefi-4epon-ez", 1200),
          ("card-umop-12gefi-8epon", 1194),
          ("card-umop-12gefi-8epon-den", 1195),
          ("card-umop-12gefi-8epon-den-ez", 1197),
          ("card-umop-12gefi-8epon-ez", 1196),
          ("card-umte-gei-24ef", 1130),
          ("card-umte-gei-24ef-2x", 1133),
          ("card-umte-gei-24ef-2x-den", 1135),
          ("card-umte-gei-24ef-2x-lit", 1134),
          ("card-umte-gei-24ef-den", 1132),
          ("card-umte-gei-24ef-den-ez", 1138),
          ("card-umte-gei-24ef-ez", 1136),
          ("card-umte-gei-24ef-lit", 1131),
          ("card-umte-gei-24ef-lit-ez", 1137),
          ("card-umte1-gei-l2ef", 1158),
          ("card-umte1-gei-l2ef-2x", 1161),
          ("card-umte1-gei-l2ef-2x-den", 1163),
          ("card-umte1-gei-l2ef-2x-lit", 1162),
          ("card-umte1-gei-l2ef-den", 1160),
          ("card-umte1-gei-l2ef-den-ez", 1166),
          ("card-umte1-gei-l2ef-ez", 1164),
          ("card-umte1-gei-l2ef-lit", 1159),
          ("card-umte1-gei-l2ef-lit-ez", 1165),
          ("card-umtf-gei-24ef", 1121),
          ("card-umtf-gei-24ef-2x", 1124),
          ("card-umtf-gei-24ef-2x-den", 1126),
          ("card-umtf-gei-24ef-2x-lit", 1125),
          ("card-umtf-gei-24ef-den", 1123),
          ("card-umtf-gei-24ef-den-ez", 1129),
          ("card-umtf-gei-24ef-ez", 1127),
          ("card-umtf-gei-24ef-lit", 1122),
          ("card-umtf-gei-24ef-lit-ez", 1128),
          ("card-umtf1-gei-12ef-den-ez-replace-xgm", 1226),
          ("card-umtf1-gei-12ef-ez-replace-xgm", 1225),
          ("card-umtf1-gei-l2ef", 1149),
          ("card-umtf1-gei-l2ef-2x", 1152),
          ("card-umtf1-gei-l2ef-2x-den", 1154),
          ("card-umtf1-gei-l2ef-2x-lit", 1153),
          ("card-umtf1-gei-l2ef-den", 1151),
          ("card-umtf1-gei-l2ef-den-ez", 1157),
          ("card-umtf1-gei-l2ef-ez", 1155),
          ("card-umtf1-gei-l2ef-lit", 1150),
          ("card-umtf1-gei-l2ef-lit-ez", 1156),
          ("card-uni", 179),
          ("card-utqf-gei-12ef-1588-clock", 1210),
          ("card-utqf-gei-12ef-1588-clock-den", 1214),
          ("card-utqf-gei-12ef-1588-clock-den-ez", 1222),
          ("card-utqf-gei-12ef-1588-clock-ez", 1218),
          ("card-utqf-gei-12ef-1588-clock-left", 1208),
          ("card-utqf-gei-12ef-1588-clock-left-den", 1212),
          ("card-utqf-gei-12ef-1588-clock-left-den-ez", 1220),
          ("card-utqf-gei-12ef-1588-clock-left-ez", 1216),
          ("card-utqf-gei-12ef-1588-clock-no", 1207),
          ("card-utqf-gei-12ef-1588-clock-no-den", 1211),
          ("card-utqf-gei-12ef-1588-clock-no-den-ez", 1219),
          ("card-utqf-gei-12ef-1588-clock-no-ez", 1215),
          ("card-utqf-gei-12ef-1588-clock-right", 1209),
          ("card-utqf-gei-12ef-1588-clock-right-den", 1213),
          ("card-utqf-gei-12ef-1588-clock-right-den-ez", 1221),
          ("card-utqf-gei-12ef-1588-clock-right-ez", 1217),
          ("card-utqf-tphy-mmpi", 4866),
          ("card-uwsa8541-g-24", 1141),
          ("card-uxhf-2c-2xefi", 1202),
          ("card-uxhf-2c-2xefi-den", 1204),
          ("card-uxhf-2c-2xefi-lit", 1203),
          ("card-vbui", 171),
          ("card-vip", 182),
          ("card-virtual-access", 174),
          ("card-virtual-template", 173),
          ("card-vlan", 166),
          ("card-wan-x", 1112),
          ("ccard-gei-x2-n-ez", 1075),
          ("mcp-board", 5301),
          ("mec-board", 5401),
          ("sfc-board", 5101),
          ("sfc2-board", 5102),
          ("sfc3-board", 5103),
          ("smp-board", 5201),
          ("upc-board", 5001))
    )





class PortType(Integer32):
    """Custom type PortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              129,
              161,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
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
              512,
              1025,
              1026,
              1027,
              1028,
              1061,
              1062,
              1063,
              1190,
              1538,
              1539,
              1540,
              1541,
              1542,
              1543,
              2051,
              2052,
              2564,
              2565,
              2566,
              2567,
              2568,
              3077,
              3078,
              3590,
              3591,
              3592,
              3593,
              4103,
              4104,
              4616,
              4617,
              5129,
              5130,
              5131,
              5132,
              5133,
              5134,
              5135,
              5136,
              5137,
              5138,
              5139,
              5140,
              5141,
              5142,
              5143)
        )
    )
    namedValues = NamedValues(
        *(("port-async", 5134),
          ("port-atm155", 2051),
          ("port-atm622", 2052),
          ("port-aux", 5130),
          ("port-ces", 180),
          ("port-cip", 181),
          ("port-dialer", 170),
          ("port-e1", 2564),
          ("port-e1-c", 2565),
          ("port-e1-c-ixbus", 2566),
          ("port-e1vi", 2567),
          ("port-e1vi-serial", 2568),
          ("port-e3", 4616),
          ("port-e3-c", 4617),
          ("port-fei", 512),
          ("port-gei", 1025),
          ("port-gei-1o-1e", 1063),
          ("port-gei-2e", 1061),
          ("port-gei-2o", 1062),
          ("port-gei-epon", 1190),
          ("port-gei-x", 1026),
          ("port-gps", 5143),
          ("port-gre", 163),
          ("port-l2tpdialer", 176),
          ("port-lffxs-2", 5135),
          ("port-lfxo", 5133),
          ("port-lfxs", 5131),
          ("port-lhs", 5129),
          ("port-lhsu", 5132),
          ("port-loopback", 161),
          ("port-manage", 128),
          ("port-manage-lct", 5141),
          ("port-manage-qx", 5140),
          ("port-manage-spec", 129),
          ("port-mndec", 5137),
          ("port-mppp", 165),
          ("port-ndec", 5136),
          ("port-null", 167),
          ("port-oc12", 1539),
          ("port-oc192", 1543),
          ("port-oc3", 1538),
          ("port-oc3-c", 1541),
          ("port-oc48", 1540),
          ("port-oc48-c", 1542),
          ("port-port-channel", 168),
          ("port-qinq", 177),
          ("port-stack", 1028),
          ("port-superpvc", 175),
          ("port-superqinq", 178),
          ("port-supervlan", 169),
          ("port-t1", 3077),
          ("port-t1-c", 3078),
          ("port-t3", 4103),
          ("port-t3-c", 4104),
          ("port-tdm-e1", 3590),
          ("port-tdm-ether", 3591),
          ("port-tdm-inte-ether", 3592),
          ("port-tdm-t1", 3593),
          ("port-timer-abs", 5142),
          ("port-timer-ext", 5139),
          ("port-timer1588", 5138),
          ("port-tunnel", 164),
          ("port-uni", 179),
          ("port-vbui", 171),
          ("port-vip", 182),
          ("port-virtual-access", 174),
          ("port-virtual-template", 173),
          ("port-vlan", 166),
          ("port-wan-x", 1027))
    )





class AlarmType(Integer32):
    """Custom type AlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
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
              128,
              129,
              130,
              131)
        )
    )
    namedValues = NamedValues(
        *(("hardware-board", 2),
          ("hardware-environment", 1),
          ("hardware-port", 3),
          ("softprotocol-aaa", 112),
          ("softprotocol-acl", 86),
          ("softprotocol-alg", 91),
          ("softprotocol-amat", 101),
          ("softprotocol-arp", 78),
          ("softprotocol-bfd", 119),
          ("softprotocol-bgp", 71),
          ("softprotocol-cfm", 120),
          ("softprotocol-database", 66),
          ("softprotocol-dhcp", 94),
          ("softprotocol-drp", 72),
          ("softprotocol-ethoam", 107),
          ("softprotocol-fr", 106),
          ("softprotocol-fw", 115),
          ("softprotocol-icmp", 80),
          ("softprotocol-igmp", 75),
          ("softprotocol-igmp-snooping", 105),
          ("softprotocol-ip", 74),
          ("softprotocol-ipv6", 113),
          ("softprotocol-isis", 79),
          ("softprotocol-l2vpn", 102),
          ("softprotocol-ldp", 100),
          ("softprotocol-local-accounting", 98),
          ("softprotocol-loopdetect", 92),
          ("softprotocol-mac", 90),
          ("softprotocol-mix", 118),
          ("softprotocol-mld", 95),
          ("softprotocol-mux", 116),
          ("softprotocol-nat", 83),
          ("softprotocol-oam", 67),
          ("softprotocol-ospf", 69),
          ("softprotocol-pim", 114),
          ("softprotocol-ppp", 88),
          ("softprotocol-qos", 110),
          ("softprotocol-radius", 99),
          ("softprotocol-rip", 70),
          ("softprotocol-rmon", 82),
          ("softprotocol-ros", 65),
          ("softprotocol-rsvp", 103),
          ("softprotocol-scan", 89),
          ("softprotocol-security", 68),
          ("softprotocol-session", 93),
          ("softprotocol-snmp", 81),
          ("softprotocol-ssh", 108),
          ("softprotocol-stp", 96),
          ("softprotocol-tacacs", 111),
          ("softprotocol-tcp-udp", 73),
          ("softprotocol-tdm", 109),
          ("softprotocol-telnet", 76),
          ("softprotocol-udld", 117),
          ("softprotocol-udp", 77),
          ("softprotocol-urpf", 84),
          ("softprotocol-vlan", 97),
          ("softprotocol-vrrp", 87),
          ("softprotocol-vswitch", 85),
          ("softprotocol-zesr", 104),
          ("softprotocol-zess", 128),
          ("statistics-aps", 129),
          ("statistics-epon", 131),
          ("statistics-pdh-2m", 130))
    )





class PortWorkingType(Integer32):
    """Custom type PortWorkingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto-config", 0),
          ("full-duplex", 1),
          ("half-duplex", 2))
    )





class ShelfAttrib(Integer32):
    """Custom type ShelfAttrib based on Integer32"""
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
        *(("environshelf", 4),
          ("fanshelf", 2),
          ("powershelf", 3),
          ("workshelf", 1))
    )





class HostAttr(Integer32):
    """Custom type HostAttr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("global", 0),
          ("mng", 1),
          ("vrf", 2))
    )





class SystemDeviceType(Integer32):
    """Custom type SystemDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("single", 0),
          ("stack", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
_Zxr10systemconfig_ObjectIdentity = ObjectIdentity
zxr10systemconfig = _Zxr10systemconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 1)
)
_Zxr10SystemID_Type = ProductID
_Zxr10SystemID_Object = MibScalar
zxr10SystemID = _Zxr10SystemID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 1, 1),
    _Zxr10SystemID_Type()
)
zxr10SystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemID.setStatus("current")
_Zxr10SystemserialNo_Type = Integer32
_Zxr10SystemserialNo_Object = MibScalar
zxr10SystemserialNo = _Zxr10SystemserialNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 1, 2),
    _Zxr10SystemserialNo_Type()
)
zxr10SystemserialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemserialNo.setStatus("current")


class _Zxr10SystemDescrip_Type(DisplayString):
    """Custom type zxr10SystemDescrip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10SystemDescrip_Type.__name__ = "DisplayString"
_Zxr10SystemDescrip_Object = MibScalar
zxr10SystemDescrip = _Zxr10SystemDescrip_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 1, 3),
    _Zxr10SystemDescrip_Type()
)
zxr10SystemDescrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemDescrip.setStatus("current")
_Zxr10SystemTrapHost_Type = IpAddress
_Zxr10SystemTrapHost_Object = MibScalar
zxr10SystemTrapHost = _Zxr10SystemTrapHost_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 1, 4),
    _Zxr10SystemTrapHost_Type()
)
zxr10SystemTrapHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10SystemTrapHost.setStatus("current")


class _Zxr10SystemTrapCommunity_Type(DisplayString):
    """Custom type zxr10SystemTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10SystemTrapCommunity_Type.__name__ = "DisplayString"
_Zxr10SystemTrapCommunity_Object = MibScalar
zxr10SystemTrapCommunity = _Zxr10SystemTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 1, 5),
    _Zxr10SystemTrapCommunity_Type()
)
zxr10SystemTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10SystemTrapCommunity.setStatus("current")


class _Zxr10SystemVersion_Type(DisplayString):
    """Custom type zxr10SystemVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10SystemVersion_Type.__name__ = "DisplayString"
_Zxr10SystemVersion_Object = MibScalar
zxr10SystemVersion = _Zxr10SystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 1, 6),
    _Zxr10SystemVersion_Type()
)
zxr10SystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemVersion.setStatus("current")


class _Zxr10SystemVpnName_Type(DisplayString):
    """Custom type zxr10SystemVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Zxr10SystemVpnName_Type.__name__ = "DisplayString"
_Zxr10SystemVpnName_Object = MibScalar
zxr10SystemVpnName = _Zxr10SystemVpnName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 1, 7),
    _Zxr10SystemVpnName_Type()
)
zxr10SystemVpnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10SystemVpnName.setStatus("current")
_Zxr10SystemHostAttr_Type = HostAttr
_Zxr10SystemHostAttr_Object = MibScalar
zxr10SystemHostAttr = _Zxr10SystemHostAttr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 1, 8),
    _Zxr10SystemHostAttr_Type()
)
zxr10SystemHostAttr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10SystemHostAttr.setStatus("current")


class _Zxr10SystemEnableSecret_Type(DisplayString):
    """Custom type zxr10SystemEnableSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 16),
    )


_Zxr10SystemEnableSecret_Type.__name__ = "DisplayString"
_Zxr10SystemEnableSecret_Object = MibScalar
zxr10SystemEnableSecret = _Zxr10SystemEnableSecret_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 1, 9),
    _Zxr10SystemEnableSecret_Type()
)
zxr10SystemEnableSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10SystemEnableSecret.setStatus("current")
_Zxr10SystemDeviceType_Type = SystemDeviceType
_Zxr10SystemDeviceType_Object = MibScalar
zxr10SystemDeviceType = _Zxr10SystemDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 1, 12),
    _Zxr10SystemDeviceType_Type()
)
zxr10SystemDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemDeviceType.setStatus("current")
_Zxr10rack_ObjectIdentity = ObjectIdentity
zxr10rack = _Zxr10rack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2)
)
_Zxr10rackTable_Object = MibTable
zxr10rackTable = _Zxr10rackTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 1)
)
if mibBuilder.loadTexts:
    zxr10rackTable.setStatus("current")
_Zxr10rackEntry_Object = MibTableRow
zxr10rackEntry = _Zxr10rackEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 1, 1)
)
zxr10rackEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10RackNo"),
)
if mibBuilder.loadTexts:
    zxr10rackEntry.setStatus("current")
_Zxr10RackNo_Type = Integer32
_Zxr10RackNo_Object = MibTableColumn
zxr10RackNo = _Zxr10RackNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 1, 1, 1),
    _Zxr10RackNo_Type()
)
zxr10RackNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10RackNo.setStatus("current")
_Zxr10RackAttrib_Type = MasterStatus
_Zxr10RackAttrib_Object = MibTableColumn
zxr10RackAttrib = _Zxr10RackAttrib_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 1, 1, 2),
    _Zxr10RackAttrib_Type()
)
zxr10RackAttrib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10RackAttrib.setStatus("current")
_Zxr10RackAvailStatus_Type = AvailStatus
_Zxr10RackAvailStatus_Object = MibTableColumn
zxr10RackAvailStatus = _Zxr10RackAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 1, 1, 3),
    _Zxr10RackAvailStatus_Type()
)
zxr10RackAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10RackAvailStatus.setStatus("current")
_Zxr10shelfTable_Object = MibTable
zxr10shelfTable = _Zxr10shelfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 2)
)
if mibBuilder.loadTexts:
    zxr10shelfTable.setStatus("current")
_Zxr10shelfEntry_Object = MibTableRow
zxr10shelfEntry = _Zxr10shelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 2, 1)
)
zxr10shelfEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10RackNo"),
    (0, "ZXR10-MIB", "zxr10ShelfNo"),
)
if mibBuilder.loadTexts:
    zxr10shelfEntry.setStatus("current")
_Zxr10ShelfNo_Type = Integer32
_Zxr10ShelfNo_Object = MibTableColumn
zxr10ShelfNo = _Zxr10ShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 2, 1, 1),
    _Zxr10ShelfNo_Type()
)
zxr10ShelfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ShelfNo.setStatus("current")
_Zxr10ShelfAttrib_Type = Integer32
_Zxr10ShelfAttrib_Object = MibTableColumn
zxr10ShelfAttrib = _Zxr10ShelfAttrib_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 2, 1, 2),
    _Zxr10ShelfAttrib_Type()
)
zxr10ShelfAttrib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ShelfAttrib.setStatus("current")
_Zxr10ShelfAvailStatus_Type = AvailStatus
_Zxr10ShelfAvailStatus_Object = MibTableColumn
zxr10ShelfAvailStatus = _Zxr10ShelfAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 2, 1, 3),
    _Zxr10ShelfAvailStatus_Type()
)
zxr10ShelfAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ShelfAvailStatus.setStatus("current")
_Zxr10slotTable_Object = MibTable
zxr10slotTable = _Zxr10slotTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3)
)
if mibBuilder.loadTexts:
    zxr10slotTable.setStatus("current")
_Zxr10slotEntry_Object = MibTableRow
zxr10slotEntry = _Zxr10slotEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1)
)
zxr10slotEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10RackNo"),
    (0, "ZXR10-MIB", "zxr10ShelfNo"),
    (0, "ZXR10-MIB", "zxr10PosInRack"),
)
if mibBuilder.loadTexts:
    zxr10slotEntry.setStatus("current")
_Zxr10PaneNo_Type = Integer32
_Zxr10PaneNo_Object = MibTableColumn
zxr10PaneNo = _Zxr10PaneNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 1),
    _Zxr10PaneNo_Type()
)
zxr10PaneNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PaneNo.setStatus("current")
_Zxr10PosInRack_Type = Integer32
_Zxr10PosInRack_Object = MibTableColumn
zxr10PosInRack = _Zxr10PosInRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 2),
    _Zxr10PosInRack_Type()
)
zxr10PosInRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PosInRack.setStatus("current")
_Zxr10SlotBoardType_Type = BoardType
_Zxr10SlotBoardType_Object = MibTableColumn
zxr10SlotBoardType = _Zxr10SlotBoardType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 3),
    _Zxr10SlotBoardType_Type()
)
zxr10SlotBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SlotBoardType.setStatus("current")
_Zxr10SlotNPCType_Type = NpcType
_Zxr10SlotNPCType_Object = MibTableColumn
zxr10SlotNPCType = _Zxr10SlotNPCType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 4),
    _Zxr10SlotNPCType_Type()
)
zxr10SlotNPCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SlotNPCType.setStatus("current")
_Zxr10SlotPortsNumber_Type = Integer32
_Zxr10SlotPortsNumber_Object = MibTableColumn
zxr10SlotPortsNumber = _Zxr10SlotPortsNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 5),
    _Zxr10SlotPortsNumber_Type()
)
zxr10SlotPortsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SlotPortsNumber.setStatus("current")
_Zxr10SlotAvailStatus_Type = AvailStatus
_Zxr10SlotAvailStatus_Object = MibTableColumn
zxr10SlotAvailStatus = _Zxr10SlotAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 6),
    _Zxr10SlotAvailStatus_Type()
)
zxr10SlotAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SlotAvailStatus.setStatus("current")
_Zxr10SlotOperStatus_Type = OperStatus
_Zxr10SlotOperStatus_Object = MibTableColumn
zxr10SlotOperStatus = _Zxr10SlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 7),
    _Zxr10SlotOperStatus_Type()
)
zxr10SlotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SlotOperStatus.setStatus("current")
_Zxr10SlotMasterStatus_Type = MasterStatus
_Zxr10SlotMasterStatus_Object = MibTableColumn
zxr10SlotMasterStatus = _Zxr10SlotMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 8),
    _Zxr10SlotMasterStatus_Type()
)
zxr10SlotMasterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SlotMasterStatus.setStatus("current")
_Zxr10ReceiveTick_Type = TimeTicks
_Zxr10ReceiveTick_Object = MibTableColumn
zxr10ReceiveTick = _Zxr10ReceiveTick_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 9),
    _Zxr10ReceiveTick_Type()
)
zxr10ReceiveTick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ReceiveTick.setStatus("current")
_Zxr10SlotTemperature_Type = Integer32
_Zxr10SlotTemperature_Object = MibTableColumn
zxr10SlotTemperature = _Zxr10SlotTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 10),
    _Zxr10SlotTemperature_Type()
)
zxr10SlotTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SlotTemperature.setStatus("current")
_Zxr10SubcardMax_Type = Integer32
_Zxr10SubcardMax_Object = MibTableColumn
zxr10SubcardMax = _Zxr10SubcardMax_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 11),
    _Zxr10SubcardMax_Type()
)
zxr10SubcardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SubcardMax.setStatus("current")


class _Zxr10BootVersion_Type(DisplayString):
    """Custom type zxr10BootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Zxr10BootVersion_Type.__name__ = "DisplayString"
_Zxr10BootVersion_Object = MibTableColumn
zxr10BootVersion = _Zxr10BootVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 12),
    _Zxr10BootVersion_Type()
)
zxr10BootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10BootVersion.setStatus("current")


class _Zxr10PCBVersion_Type(DisplayString):
    """Custom type zxr10PCBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Zxr10PCBVersion_Type.__name__ = "DisplayString"
_Zxr10PCBVersion_Object = MibTableColumn
zxr10PCBVersion = _Zxr10PCBVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 13),
    _Zxr10PCBVersion_Type()
)
zxr10PCBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PCBVersion.setStatus("current")


class _Zxr10FPGAVer_Type(DisplayString):
    """Custom type zxr10FPGAVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Zxr10FPGAVer_Type.__name__ = "DisplayString"
_Zxr10FPGAVer_Object = MibTableColumn
zxr10FPGAVer = _Zxr10FPGAVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 14),
    _Zxr10FPGAVer_Type()
)
zxr10FPGAVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10FPGAVer.setStatus("current")


class _Zxr10McodeVer_Type(DisplayString):
    """Custom type zxr10McodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Zxr10McodeVer_Type.__name__ = "DisplayString"
_Zxr10McodeVer_Object = MibTableColumn
zxr10McodeVer = _Zxr10McodeVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 15),
    _Zxr10McodeVer_Type()
)
zxr10McodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10McodeVer.setStatus("current")
_Zxr10MasterQDRSRAMSize_Type = Integer32
_Zxr10MasterQDRSRAMSize_Object = MibTableColumn
zxr10MasterQDRSRAMSize = _Zxr10MasterQDRSRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 16),
    _Zxr10MasterQDRSRAMSize_Type()
)
zxr10MasterQDRSRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MasterQDRSRAMSize.setStatus("current")
_Zxr10SlaveQDRSRAMSize_Type = Integer32
_Zxr10SlaveQDRSRAMSize_Object = MibTableColumn
zxr10SlaveQDRSRAMSize = _Zxr10SlaveQDRSRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 17),
    _Zxr10SlaveQDRSRAMSize_Type()
)
zxr10SlaveQDRSRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SlaveQDRSRAMSize.setStatus("current")
_Zxr10camSize_Type = Integer32
_Zxr10camSize_Object = MibTableColumn
zxr10camSize = _Zxr10camSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 18),
    _Zxr10camSize_Type()
)
zxr10camSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10camSize.setStatus("current")


class _Zxr10BoardSilkLabel_Type(DisplayString):
    """Custom type zxr10BoardSilkLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Zxr10BoardSilkLabel_Type.__name__ = "DisplayString"
_Zxr10BoardSilkLabel_Object = MibTableColumn
zxr10BoardSilkLabel = _Zxr10BoardSilkLabel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 3, 1, 19),
    _Zxr10BoardSilkLabel_Type()
)
zxr10BoardSilkLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10BoardSilkLabel.setStatus("current")
_Zxr10portTable_Object = MibTable
zxr10portTable = _Zxr10portTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4)
)
if mibBuilder.loadTexts:
    zxr10portTable.setStatus("current")
_Zxr10portEntry_Object = MibTableRow
zxr10portEntry = _Zxr10portEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1)
)
zxr10portEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10RackNo"),
    (0, "ZXR10-MIB", "zxr10ShelfNo"),
    (0, "ZXR10-MIB", "zxr10PosInRack"),
    (0, "ZXR10-MIB", "zxr10PortNo"),
)
if mibBuilder.loadTexts:
    zxr10portEntry.setStatus("current")
_Zxr10PortIfIndex_Type = Integer32
_Zxr10PortIfIndex_Object = MibTableColumn
zxr10PortIfIndex = _Zxr10PortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 1),
    _Zxr10PortIfIndex_Type()
)
zxr10PortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortIfIndex.setStatus("current")
_Zxr10PortNo_Type = Integer32
_Zxr10PortNo_Object = MibTableColumn
zxr10PortNo = _Zxr10PortNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 2),
    _Zxr10PortNo_Type()
)
zxr10PortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortNo.setStatus("current")
_Zxr10PortType_Type = PortType
_Zxr10PortType_Object = MibTableColumn
zxr10PortType = _Zxr10PortType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 3),
    _Zxr10PortType_Type()
)
zxr10PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortType.setStatus("current")
_Zxr10PortWorkingType_Type = PortWorkingType
_Zxr10PortWorkingType_Object = MibTableColumn
zxr10PortWorkingType = _Zxr10PortWorkingType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 4),
    _Zxr10PortWorkingType_Type()
)
zxr10PortWorkingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortWorkingType.setStatus("current")
_Zxr10PortMTU_Type = Integer32
_Zxr10PortMTU_Object = MibTableColumn
zxr10PortMTU = _Zxr10PortMTU_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 5),
    _Zxr10PortMTU_Type()
)
zxr10PortMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortMTU.setStatus("current")


class _Zxr10PortSpeed_Type(DisplayString):
    """Custom type zxr10PortSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Zxr10PortSpeed_Type.__name__ = "DisplayString"
_Zxr10PortSpeed_Object = MibTableColumn
zxr10PortSpeed = _Zxr10PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 6),
    _Zxr10PortSpeed_Type()
)
zxr10PortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortSpeed.setStatus("current")
_Zxr10PortAvailStatus_Type = AvailStatus
_Zxr10PortAvailStatus_Object = MibTableColumn
zxr10PortAvailStatus = _Zxr10PortAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 7),
    _Zxr10PortAvailStatus_Type()
)
zxr10PortAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortAvailStatus.setStatus("current")
_Zxr10PortOperStatus_Type = OperStatus
_Zxr10PortOperStatus_Object = MibTableColumn
zxr10PortOperStatus = _Zxr10PortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 8),
    _Zxr10PortOperStatus_Type()
)
zxr10PortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortOperStatus.setStatus("current")
_Zxr10PortProtocolStatus_Type = OperStatus
_Zxr10PortProtocolStatus_Object = MibTableColumn
zxr10PortProtocolStatus = _Zxr10PortProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 9),
    _Zxr10PortProtocolStatus_Type()
)
zxr10PortProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortProtocolStatus.setStatus("current")
_Zxr10PortProperty_Type = PortProperty
_Zxr10PortProperty_Object = MibTableColumn
zxr10PortProperty = _Zxr10PortProperty_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 10),
    _Zxr10PortProperty_Type()
)
zxr10PortProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortProperty.setStatus("current")


class _Zxr10PortDesc_Type(DisplayString):
    """Custom type zxr10PortDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Zxr10PortDesc_Type.__name__ = "DisplayString"
_Zxr10PortDesc_Object = MibTableColumn
zxr10PortDesc = _Zxr10PortDesc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 11),
    _Zxr10PortDesc_Type()
)
zxr10PortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortDesc.setStatus("current")
_Zxr10_statistics_ObjectIdentity = ObjectIdentity
zxr10_statistics = _Zxr10_statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3)
)
_Zxr10SystemUnitTable_Object = MibTable
zxr10SystemUnitTable = _Zxr10SystemUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 1)
)
if mibBuilder.loadTexts:
    zxr10SystemUnitTable.setStatus("current")
_Zxr10SystemUnitEntry_Object = MibTableRow
zxr10SystemUnitEntry = _Zxr10SystemUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 1, 1)
)
zxr10SystemUnitEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10SystemUnitIndex"),
)
if mibBuilder.loadTexts:
    zxr10SystemUnitEntry.setStatus("current")
_Zxr10SystemUnitIndex_Type = Integer32
_Zxr10SystemUnitIndex_Object = MibTableColumn
zxr10SystemUnitIndex = _Zxr10SystemUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 1, 1, 1),
    _Zxr10SystemUnitIndex_Type()
)
zxr10SystemUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemUnitIndex.setStatus("current")
_Zxr10SystemUnitRunStatus_Type = UnitRunStatus
_Zxr10SystemUnitRunStatus_Object = MibTableColumn
zxr10SystemUnitRunStatus = _Zxr10SystemUnitRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 1, 1, 2),
    _Zxr10SystemUnitRunStatus_Type()
)
zxr10SystemUnitRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemUnitRunStatus.setStatus("current")
_Zxr10SystemMemSize_Type = Integer32
_Zxr10SystemMemSize_Object = MibTableColumn
zxr10SystemMemSize = _Zxr10SystemMemSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 1, 1, 3),
    _Zxr10SystemMemSize_Type()
)
zxr10SystemMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemMemSize.setStatus("current")
_Zxr10SystemMemUsed_Type = Integer32
_Zxr10SystemMemUsed_Object = MibTableColumn
zxr10SystemMemUsed = _Zxr10SystemMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 1, 1, 4),
    _Zxr10SystemMemUsed_Type()
)
zxr10SystemMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemMemUsed.setStatus("current")
_Zxr10SystemCpuUtility2m_Type = Integer32
_Zxr10SystemCpuUtility2m_Object = MibTableColumn
zxr10SystemCpuUtility2m = _Zxr10SystemCpuUtility2m_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 1, 1, 5),
    _Zxr10SystemCpuUtility2m_Type()
)
zxr10SystemCpuUtility2m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemCpuUtility2m.setStatus("current")
_Zxr10SystemCpuUtility5s_Type = Integer32
_Zxr10SystemCpuUtility5s_Object = MibTableColumn
zxr10SystemCpuUtility5s = _Zxr10SystemCpuUtility5s_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 1, 1, 6),
    _Zxr10SystemCpuUtility5s_Type()
)
zxr10SystemCpuUtility5s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemCpuUtility5s.setStatus("current")
_Zxr10SystemCpuUtility30s_Type = Integer32
_Zxr10SystemCpuUtility30s_Object = MibTableColumn
zxr10SystemCpuUtility30s = _Zxr10SystemCpuUtility30s_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 1, 1, 7),
    _Zxr10SystemCpuUtility30s_Type()
)
zxr10SystemCpuUtility30s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemCpuUtility30s.setStatus("current")
_Zxr10SystemPeakCpuUtility_Type = Integer32
_Zxr10SystemPeakCpuUtility_Object = MibTableColumn
zxr10SystemPeakCpuUtility = _Zxr10SystemPeakCpuUtility_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 1, 1, 8),
    _Zxr10SystemPeakCpuUtility_Type()
)
zxr10SystemPeakCpuUtility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemPeakCpuUtility.setStatus("current")
_Zxr10SystemUnitUpTime_Type = TimeTicks
_Zxr10SystemUnitUpTime_Object = MibTableColumn
zxr10SystemUnitUpTime = _Zxr10SystemUnitUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 1, 1, 9),
    _Zxr10SystemUnitUpTime_Type()
)
zxr10SystemUnitUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemUnitUpTime.setStatus("current")
_Zxr10SystemUnitPidNum_Type = Integer32
_Zxr10SystemUnitPidNum_Object = MibTableColumn
zxr10SystemUnitPidNum = _Zxr10SystemUnitPidNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 1, 1, 10),
    _Zxr10SystemUnitPidNum_Type()
)
zxr10SystemUnitPidNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemUnitPidNum.setStatus("current")
_Zxr10SystemCpuUtility1m_Type = Integer32
_Zxr10SystemCpuUtility1m_Object = MibTableColumn
zxr10SystemCpuUtility1m = _Zxr10SystemCpuUtility1m_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 1, 1, 11),
    _Zxr10SystemCpuUtility1m_Type()
)
zxr10SystemCpuUtility1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemCpuUtility1m.setStatus("current")
_Zxr10SystemCpuUtility5m_Type = Integer32
_Zxr10SystemCpuUtility5m_Object = MibTableColumn
zxr10SystemCpuUtility5m = _Zxr10SystemCpuUtility5m_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 1, 1, 12),
    _Zxr10SystemCpuUtility5m_Type()
)
zxr10SystemCpuUtility5m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SystemCpuUtility5m.setStatus("current")
_Zxr10UnitPidTable_Object = MibTable
zxr10UnitPidTable = _Zxr10UnitPidTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3)
)
if mibBuilder.loadTexts:
    zxr10UnitPidTable.setStatus("current")
_Zxr10UnitPidEntry_Object = MibTableRow
zxr10UnitPidEntry = _Zxr10UnitPidEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1)
)
zxr10UnitPidEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10SystemUnitIndex"),
    (0, "ZXR10-MIB", "zxr10UnitPidNo"),
)
if mibBuilder.loadTexts:
    zxr10UnitPidEntry.setStatus("current")
_Zxr10UnitPidNo_Type = Integer32
_Zxr10UnitPidNo_Object = MibTableColumn
zxr10UnitPidNo = _Zxr10UnitPidNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 1),
    _Zxr10UnitPidNo_Type()
)
zxr10UnitPidNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidNo.setStatus("current")


class _Zxr10UnitPidUsedStatus_Type(DisplayString):
    """Custom type zxr10UnitPidUsedStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10UnitPidUsedStatus_Type.__name__ = "DisplayString"
_Zxr10UnitPidUsedStatus_Object = MibTableColumn
zxr10UnitPidUsedStatus = _Zxr10UnitPidUsedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 2),
    _Zxr10UnitPidUsedStatus_Type()
)
zxr10UnitPidUsedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidUsedStatus.setStatus("current")


class _Zxr10UnitPidName_Type(DisplayString):
    """Custom type zxr10UnitPidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10UnitPidName_Type.__name__ = "DisplayString"
_Zxr10UnitPidName_Object = MibTableColumn
zxr10UnitPidName = _Zxr10UnitPidName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 3),
    _Zxr10UnitPidName_Type()
)
zxr10UnitPidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidName.setStatus("current")
_Zxr10UnitPidPrio_Type = Integer32
_Zxr10UnitPidPrio_Object = MibTableColumn
zxr10UnitPidPrio = _Zxr10UnitPidPrio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 4),
    _Zxr10UnitPidPrio_Type()
)
zxr10UnitPidPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidPrio.setStatus("current")
_Zxr10UnitPidStackSize_Type = Integer32
_Zxr10UnitPidStackSize_Object = MibTableColumn
zxr10UnitPidStackSize = _Zxr10UnitPidStackSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 5),
    _Zxr10UnitPidStackSize_Type()
)
zxr10UnitPidStackSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidStackSize.setStatus("current")
_Zxr10UnitPidCalledTimes_Type = Integer32
_Zxr10UnitPidCalledTimes_Object = MibTableColumn
zxr10UnitPidCalledTimes = _Zxr10UnitPidCalledTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 6),
    _Zxr10UnitPidCalledTimes_Type()
)
zxr10UnitPidCalledTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidCalledTimes.setStatus("current")
_Zxr10UnitPidCpuOccupanTime_Type = TimeTicks
_Zxr10UnitPidCpuOccupanTime_Object = MibTableColumn
zxr10UnitPidCpuOccupanTime = _Zxr10UnitPidCpuOccupanTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 7),
    _Zxr10UnitPidCpuOccupanTime_Type()
)
zxr10UnitPidCpuOccupanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidCpuOccupanTime.setStatus("current")
_Zxr10UnitPidInterruptTimes_Type = Integer32
_Zxr10UnitPidInterruptTimes_Object = MibTableColumn
zxr10UnitPidInterruptTimes = _Zxr10UnitPidInterruptTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 8),
    _Zxr10UnitPidInterruptTimes_Type()
)
zxr10UnitPidInterruptTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidInterruptTimes.setStatus("current")
_Zxr10UnitPidAsyQuenMsgMax_Type = Integer32
_Zxr10UnitPidAsyQuenMsgMax_Object = MibTableColumn
zxr10UnitPidAsyQuenMsgMax = _Zxr10UnitPidAsyQuenMsgMax_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 9),
    _Zxr10UnitPidAsyQuenMsgMax_Type()
)
zxr10UnitPidAsyQuenMsgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidAsyQuenMsgMax.setStatus("current")
_Zxr10UnitPidAsyQuenUsed_Type = Integer32
_Zxr10UnitPidAsyQuenUsed_Object = MibTableColumn
zxr10UnitPidAsyQuenUsed = _Zxr10UnitPidAsyQuenUsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 10),
    _Zxr10UnitPidAsyQuenUsed_Type()
)
zxr10UnitPidAsyQuenUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidAsyQuenUsed.setStatus("current")
_Zxr10UnitPidAsyQuenBlocked_Type = Integer32
_Zxr10UnitPidAsyQuenBlocked_Object = MibTableColumn
zxr10UnitPidAsyQuenBlocked = _Zxr10UnitPidAsyQuenBlocked_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 11),
    _Zxr10UnitPidAsyQuenBlocked_Type()
)
zxr10UnitPidAsyQuenBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidAsyQuenBlocked.setStatus("current")
_Zxr10UnitPidAsyQuenSendTimeouts_Type = Integer32
_Zxr10UnitPidAsyQuenSendTimeouts_Object = MibTableColumn
zxr10UnitPidAsyQuenSendTimeouts = _Zxr10UnitPidAsyQuenSendTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 12),
    _Zxr10UnitPidAsyQuenSendTimeouts_Type()
)
zxr10UnitPidAsyQuenSendTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidAsyQuenSendTimeouts.setStatus("current")
_Zxr10UnitPidAsyQuenRecTimeouts_Type = Integer32
_Zxr10UnitPidAsyQuenRecTimeouts_Object = MibTableColumn
zxr10UnitPidAsyQuenRecTimeouts = _Zxr10UnitPidAsyQuenRecTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 13),
    _Zxr10UnitPidAsyQuenRecTimeouts_Type()
)
zxr10UnitPidAsyQuenRecTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidAsyQuenRecTimeouts.setStatus("current")
_Zxr10UnitPidSynQuenMsgMax_Type = Integer32
_Zxr10UnitPidSynQuenMsgMax_Object = MibTableColumn
zxr10UnitPidSynQuenMsgMax = _Zxr10UnitPidSynQuenMsgMax_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 14),
    _Zxr10UnitPidSynQuenMsgMax_Type()
)
zxr10UnitPidSynQuenMsgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidSynQuenMsgMax.setStatus("current")
_Zxr10UnitPidSynQuenUsed_Type = Integer32
_Zxr10UnitPidSynQuenUsed_Object = MibTableColumn
zxr10UnitPidSynQuenUsed = _Zxr10UnitPidSynQuenUsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 15),
    _Zxr10UnitPidSynQuenUsed_Type()
)
zxr10UnitPidSynQuenUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidSynQuenUsed.setStatus("current")
_Zxr10UnitPidSynQuenBlocked_Type = Integer32
_Zxr10UnitPidSynQuenBlocked_Object = MibTableColumn
zxr10UnitPidSynQuenBlocked = _Zxr10UnitPidSynQuenBlocked_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 16),
    _Zxr10UnitPidSynQuenBlocked_Type()
)
zxr10UnitPidSynQuenBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidSynQuenBlocked.setStatus("current")
_Zxr10UnitPidSynQuenSendTimeouts_Type = Integer32
_Zxr10UnitPidSynQuenSendTimeouts_Object = MibTableColumn
zxr10UnitPidSynQuenSendTimeouts = _Zxr10UnitPidSynQuenSendTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 17),
    _Zxr10UnitPidSynQuenSendTimeouts_Type()
)
zxr10UnitPidSynQuenSendTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidSynQuenSendTimeouts.setStatus("current")
_Zxr10UnitPidSynQuenRecTimeouts_Type = Integer32
_Zxr10UnitPidSynQuenRecTimeouts_Object = MibTableColumn
zxr10UnitPidSynQuenRecTimeouts = _Zxr10UnitPidSynQuenRecTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 18),
    _Zxr10UnitPidSynQuenRecTimeouts_Type()
)
zxr10UnitPidSynQuenRecTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidSynQuenRecTimeouts.setStatus("current")
_Zxr10UnitPidTimerNamedUsed_Type = Integer32
_Zxr10UnitPidTimerNamedUsed_Object = MibTableColumn
zxr10UnitPidTimerNamedUsed = _Zxr10UnitPidTimerNamedUsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 19),
    _Zxr10UnitPidTimerNamedUsed_Type()
)
zxr10UnitPidTimerNamedUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidTimerNamedUsed.setStatus("current")
_Zxr10UnitPidTimerUnnamedUsed_Type = Integer32
_Zxr10UnitPidTimerUnnamedUsed_Object = MibTableColumn
zxr10UnitPidTimerUnnamedUsed = _Zxr10UnitPidTimerUnnamedUsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 3, 1, 20),
    _Zxr10UnitPidTimerUnnamedUsed_Type()
)
zxr10UnitPidTimerUnnamedUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitPidTimerUnnamedUsed.setStatus("current")
_Zxr10UnitCommStatTable_Object = MibTable
zxr10UnitCommStatTable = _Zxr10UnitCommStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 4)
)
if mibBuilder.loadTexts:
    zxr10UnitCommStatTable.setStatus("current")
_Zxr10UnitCommStatEntry_Object = MibTableRow
zxr10UnitCommStatEntry = _Zxr10UnitCommStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 4, 1)
)
zxr10UnitCommStatEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10SystemUnitIndex"),
    (0, "ZXR10-MIB", "zxr10UnitNo"),
)
if mibBuilder.loadTexts:
    zxr10UnitCommStatEntry.setStatus("current")
_Zxr10UnitNo_Type = Integer32
_Zxr10UnitNo_Object = MibTableColumn
zxr10UnitNo = _Zxr10UnitNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 4, 1, 1),
    _Zxr10UnitNo_Type()
)
zxr10UnitNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitNo.setStatus("current")
_Zxr10UnitsndMsgs_Type = Integer32
_Zxr10UnitsndMsgs_Object = MibTableColumn
zxr10UnitsndMsgs = _Zxr10UnitsndMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 4, 1, 2),
    _Zxr10UnitsndMsgs_Type()
)
zxr10UnitsndMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitsndMsgs.setStatus("current")
_Zxr10UnitsndBytes_Type = Integer32
_Zxr10UnitsndBytes_Object = MibTableColumn
zxr10UnitsndBytes = _Zxr10UnitsndBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 4, 1, 3),
    _Zxr10UnitsndBytes_Type()
)
zxr10UnitsndBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitsndBytes.setStatus("current")
_Zxr10UnitsndByteGigas_Type = Integer32
_Zxr10UnitsndByteGigas_Object = MibTableColumn
zxr10UnitsndByteGigas = _Zxr10UnitsndByteGigas_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 4, 1, 4),
    _Zxr10UnitsndByteGigas_Type()
)
zxr10UnitsndByteGigas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitsndByteGigas.setStatus("current")
_Zxr10UnitrcvMsgs_Type = Integer32
_Zxr10UnitrcvMsgs_Object = MibTableColumn
zxr10UnitrcvMsgs = _Zxr10UnitrcvMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 4, 1, 5),
    _Zxr10UnitrcvMsgs_Type()
)
zxr10UnitrcvMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitrcvMsgs.setStatus("current")
_Zxr10UnitrcvBytes_Type = Integer32
_Zxr10UnitrcvBytes_Object = MibTableColumn
zxr10UnitrcvBytes = _Zxr10UnitrcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 4, 1, 6),
    _Zxr10UnitrcvBytes_Type()
)
zxr10UnitrcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitrcvBytes.setStatus("current")
_Zxr10UnitrcvByteGigas_Type = Integer32
_Zxr10UnitrcvByteGigas_Object = MibTableColumn
zxr10UnitrcvByteGigas = _Zxr10UnitrcvByteGigas_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 3, 4, 1, 7),
    _Zxr10UnitrcvByteGigas_Type()
)
zxr10UnitrcvByteGigas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10UnitrcvByteGigas.setStatus("current")
_Zxr10_alarm_ObjectIdentity = ObjectIdentity
zxr10_alarm = _Zxr10_alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4)
)
_Zxr10HardwareEnvironAlarmTable_Object = MibTable
zxr10HardwareEnvironAlarmTable = _Zxr10HardwareEnvironAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 1)
)
if mibBuilder.loadTexts:
    zxr10HardwareEnvironAlarmTable.setStatus("current")
_Zxr10HardwareEnvironAlarmEntry_Object = MibTableRow
zxr10HardwareEnvironAlarmEntry = _Zxr10HardwareEnvironAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 1, 1)
)
zxr10HardwareEnvironAlarmEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10HardwareEnvironAlarmSlotNo"),
    (0, "ZXR10-MIB", "zxr10HardwareEnvironAlarmCode"),
)
if mibBuilder.loadTexts:
    zxr10HardwareEnvironAlarmEntry.setStatus("current")
_Zxr10HardwareEnvironAlarmRackNo_Type = Integer32
_Zxr10HardwareEnvironAlarmRackNo_Object = MibTableColumn
zxr10HardwareEnvironAlarmRackNo = _Zxr10HardwareEnvironAlarmRackNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 1, 1, 1),
    _Zxr10HardwareEnvironAlarmRackNo_Type()
)
zxr10HardwareEnvironAlarmRackNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareEnvironAlarmRackNo.setStatus("current")
_Zxr10HardwareEnvironAlarmShelfNo_Type = Integer32
_Zxr10HardwareEnvironAlarmShelfNo_Object = MibTableColumn
zxr10HardwareEnvironAlarmShelfNo = _Zxr10HardwareEnvironAlarmShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 1, 1, 2),
    _Zxr10HardwareEnvironAlarmShelfNo_Type()
)
zxr10HardwareEnvironAlarmShelfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareEnvironAlarmShelfNo.setStatus("current")
_Zxr10HardwareEnvironAlarmSlotNo_Type = Integer32
_Zxr10HardwareEnvironAlarmSlotNo_Object = MibTableColumn
zxr10HardwareEnvironAlarmSlotNo = _Zxr10HardwareEnvironAlarmSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 1, 1, 3),
    _Zxr10HardwareEnvironAlarmSlotNo_Type()
)
zxr10HardwareEnvironAlarmSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareEnvironAlarmSlotNo.setStatus("current")
_Zxr10HardwareEnvironAlarmCode_Type = Integer32
_Zxr10HardwareEnvironAlarmCode_Object = MibTableColumn
zxr10HardwareEnvironAlarmCode = _Zxr10HardwareEnvironAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 1, 1, 4),
    _Zxr10HardwareEnvironAlarmCode_Type()
)
zxr10HardwareEnvironAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareEnvironAlarmCode.setStatus("current")
_Zxr10HardwareEnvironAlarmLevel_Type = Integer32
_Zxr10HardwareEnvironAlarmLevel_Object = MibTableColumn
zxr10HardwareEnvironAlarmLevel = _Zxr10HardwareEnvironAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 1, 1, 5),
    _Zxr10HardwareEnvironAlarmLevel_Type()
)
zxr10HardwareEnvironAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareEnvironAlarmLevel.setStatus("current")
_Zxr10HardwareEnvironAlarmTime_Type = TimeTicks
_Zxr10HardwareEnvironAlarmTime_Object = MibTableColumn
zxr10HardwareEnvironAlarmTime = _Zxr10HardwareEnvironAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 1, 1, 6),
    _Zxr10HardwareEnvironAlarmTime_Type()
)
zxr10HardwareEnvironAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareEnvironAlarmTime.setStatus("current")
_Zxr10HardwareEnvironAlarmStatus_Type = BoolStatus
_Zxr10HardwareEnvironAlarmStatus_Object = MibTableColumn
zxr10HardwareEnvironAlarmStatus = _Zxr10HardwareEnvironAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 1, 1, 7),
    _Zxr10HardwareEnvironAlarmStatus_Type()
)
zxr10HardwareEnvironAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareEnvironAlarmStatus.setStatus("current")
_Zxr10HardwareEnvironAlarmType_Type = AlarmType
_Zxr10HardwareEnvironAlarmType_Object = MibTableColumn
zxr10HardwareEnvironAlarmType = _Zxr10HardwareEnvironAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 1, 1, 8),
    _Zxr10HardwareEnvironAlarmType_Type()
)
zxr10HardwareEnvironAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareEnvironAlarmType.setStatus("current")


class _Zxr10HardwareEnvironAlarmDescrip_Type(DisplayString):
    """Custom type zxr10HardwareEnvironAlarmDescrip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10HardwareEnvironAlarmDescrip_Type.__name__ = "DisplayString"
_Zxr10HardwareEnvironAlarmDescrip_Object = MibTableColumn
zxr10HardwareEnvironAlarmDescrip = _Zxr10HardwareEnvironAlarmDescrip_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 1, 1, 9),
    _Zxr10HardwareEnvironAlarmDescrip_Type()
)
zxr10HardwareEnvironAlarmDescrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareEnvironAlarmDescrip.setStatus("current")
_Zxr10HardwareBoardAlarmTable_Object = MibTable
zxr10HardwareBoardAlarmTable = _Zxr10HardwareBoardAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 2)
)
if mibBuilder.loadTexts:
    zxr10HardwareBoardAlarmTable.setStatus("current")
_Zxr10HardwareBoardAlarmEntry_Object = MibTableRow
zxr10HardwareBoardAlarmEntry = _Zxr10HardwareBoardAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 2, 1)
)
zxr10HardwareBoardAlarmEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10HardwareBoardAlarmSlotNo"),
    (0, "ZXR10-MIB", "zxr10HardwareBoardAlarmCode"),
)
if mibBuilder.loadTexts:
    zxr10HardwareBoardAlarmEntry.setStatus("current")
_Zxr10HardwareBoardAlarmRackNo_Type = Integer32
_Zxr10HardwareBoardAlarmRackNo_Object = MibTableColumn
zxr10HardwareBoardAlarmRackNo = _Zxr10HardwareBoardAlarmRackNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 2, 1, 1),
    _Zxr10HardwareBoardAlarmRackNo_Type()
)
zxr10HardwareBoardAlarmRackNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareBoardAlarmRackNo.setStatus("current")
_Zxr10HardwareBoardAlarmShelfNo_Type = Integer32
_Zxr10HardwareBoardAlarmShelfNo_Object = MibTableColumn
zxr10HardwareBoardAlarmShelfNo = _Zxr10HardwareBoardAlarmShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 2, 1, 2),
    _Zxr10HardwareBoardAlarmShelfNo_Type()
)
zxr10HardwareBoardAlarmShelfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareBoardAlarmShelfNo.setStatus("current")
_Zxr10HardwareBoardAlarmSlotNo_Type = Integer32
_Zxr10HardwareBoardAlarmSlotNo_Object = MibTableColumn
zxr10HardwareBoardAlarmSlotNo = _Zxr10HardwareBoardAlarmSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 2, 1, 3),
    _Zxr10HardwareBoardAlarmSlotNo_Type()
)
zxr10HardwareBoardAlarmSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareBoardAlarmSlotNo.setStatus("current")
_Zxr10HardwareBoardAlarmCode_Type = Integer32
_Zxr10HardwareBoardAlarmCode_Object = MibTableColumn
zxr10HardwareBoardAlarmCode = _Zxr10HardwareBoardAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 2, 1, 4),
    _Zxr10HardwareBoardAlarmCode_Type()
)
zxr10HardwareBoardAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareBoardAlarmCode.setStatus("current")
_Zxr10HardwareBoardAlarmLevel_Type = Integer32
_Zxr10HardwareBoardAlarmLevel_Object = MibTableColumn
zxr10HardwareBoardAlarmLevel = _Zxr10HardwareBoardAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 2, 1, 5),
    _Zxr10HardwareBoardAlarmLevel_Type()
)
zxr10HardwareBoardAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareBoardAlarmLevel.setStatus("current")
_Zxr10HardwareBoardAlarmTime_Type = TimeTicks
_Zxr10HardwareBoardAlarmTime_Object = MibTableColumn
zxr10HardwareBoardAlarmTime = _Zxr10HardwareBoardAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 2, 1, 6),
    _Zxr10HardwareBoardAlarmTime_Type()
)
zxr10HardwareBoardAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareBoardAlarmTime.setStatus("current")
_Zxr10HardwareBoardAlarmStatus_Type = BoolStatus
_Zxr10HardwareBoardAlarmStatus_Object = MibTableColumn
zxr10HardwareBoardAlarmStatus = _Zxr10HardwareBoardAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 2, 1, 7),
    _Zxr10HardwareBoardAlarmStatus_Type()
)
zxr10HardwareBoardAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareBoardAlarmStatus.setStatus("current")
_Zxr10HardwareBoardAlarmType_Type = AlarmType
_Zxr10HardwareBoardAlarmType_Object = MibTableColumn
zxr10HardwareBoardAlarmType = _Zxr10HardwareBoardAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 2, 1, 8),
    _Zxr10HardwareBoardAlarmType_Type()
)
zxr10HardwareBoardAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareBoardAlarmType.setStatus("current")


class _Zxr10HardwareBoardAlarmDescrip_Type(DisplayString):
    """Custom type zxr10HardwareBoardAlarmDescrip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10HardwareBoardAlarmDescrip_Type.__name__ = "DisplayString"
_Zxr10HardwareBoardAlarmDescrip_Object = MibTableColumn
zxr10HardwareBoardAlarmDescrip = _Zxr10HardwareBoardAlarmDescrip_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 2, 1, 9),
    _Zxr10HardwareBoardAlarmDescrip_Type()
)
zxr10HardwareBoardAlarmDescrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareBoardAlarmDescrip.setStatus("current")
_Zxr10HardwarePortAlarmTable_Object = MibTable
zxr10HardwarePortAlarmTable = _Zxr10HardwarePortAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 3)
)
if mibBuilder.loadTexts:
    zxr10HardwarePortAlarmTable.setStatus("current")
_Zxr10HardwarePortAlarmEntry_Object = MibTableRow
zxr10HardwarePortAlarmEntry = _Zxr10HardwarePortAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 3, 1)
)
zxr10HardwarePortAlarmEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10HardwarePortAlarmSlotNo"),
    (0, "ZXR10-MIB", "zxr10HardwarePortAlarmPortNo"),
    (0, "ZXR10-MIB", "zxr10HardwarePortAlarmCode"),
)
if mibBuilder.loadTexts:
    zxr10HardwarePortAlarmEntry.setStatus("current")
_Zxr10HardwarePortAlarmRackNo_Type = Integer32
_Zxr10HardwarePortAlarmRackNo_Object = MibTableColumn
zxr10HardwarePortAlarmRackNo = _Zxr10HardwarePortAlarmRackNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 3, 1, 1),
    _Zxr10HardwarePortAlarmRackNo_Type()
)
zxr10HardwarePortAlarmRackNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwarePortAlarmRackNo.setStatus("current")
_Zxr10HardwarePortAlarmShelfNo_Type = Integer32
_Zxr10HardwarePortAlarmShelfNo_Object = MibTableColumn
zxr10HardwarePortAlarmShelfNo = _Zxr10HardwarePortAlarmShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 3, 1, 2),
    _Zxr10HardwarePortAlarmShelfNo_Type()
)
zxr10HardwarePortAlarmShelfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwarePortAlarmShelfNo.setStatus("current")
_Zxr10HardwarePortAlarmSlotNo_Type = Integer32
_Zxr10HardwarePortAlarmSlotNo_Object = MibTableColumn
zxr10HardwarePortAlarmSlotNo = _Zxr10HardwarePortAlarmSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 3, 1, 3),
    _Zxr10HardwarePortAlarmSlotNo_Type()
)
zxr10HardwarePortAlarmSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwarePortAlarmSlotNo.setStatus("current")
_Zxr10HardwarePortAlarmPortNo_Type = Integer32
_Zxr10HardwarePortAlarmPortNo_Object = MibTableColumn
zxr10HardwarePortAlarmPortNo = _Zxr10HardwarePortAlarmPortNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 3, 1, 4),
    _Zxr10HardwarePortAlarmPortNo_Type()
)
zxr10HardwarePortAlarmPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwarePortAlarmPortNo.setStatus("current")
_Zxr10HardwarePortAlarmCode_Type = Integer32
_Zxr10HardwarePortAlarmCode_Object = MibTableColumn
zxr10HardwarePortAlarmCode = _Zxr10HardwarePortAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 3, 1, 5),
    _Zxr10HardwarePortAlarmCode_Type()
)
zxr10HardwarePortAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwarePortAlarmCode.setStatus("current")
_Zxr10HardwarePortAlarmLevel_Type = Integer32
_Zxr10HardwarePortAlarmLevel_Object = MibTableColumn
zxr10HardwarePortAlarmLevel = _Zxr10HardwarePortAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 3, 1, 6),
    _Zxr10HardwarePortAlarmLevel_Type()
)
zxr10HardwarePortAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwarePortAlarmLevel.setStatus("current")
_Zxr10HardwarePortAlarmTime_Type = TimeTicks
_Zxr10HardwarePortAlarmTime_Object = MibTableColumn
zxr10HardwarePortAlarmTime = _Zxr10HardwarePortAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 3, 1, 7),
    _Zxr10HardwarePortAlarmTime_Type()
)
zxr10HardwarePortAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwarePortAlarmTime.setStatus("current")
_Zxr10HardwarePortAlarmStatus_Type = BoolStatus
_Zxr10HardwarePortAlarmStatus_Object = MibTableColumn
zxr10HardwarePortAlarmStatus = _Zxr10HardwarePortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 3, 1, 8),
    _Zxr10HardwarePortAlarmStatus_Type()
)
zxr10HardwarePortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwarePortAlarmStatus.setStatus("current")
_Zxr10HardwarePortAlarmType_Type = AlarmType
_Zxr10HardwarePortAlarmType_Object = MibTableColumn
zxr10HardwarePortAlarmType = _Zxr10HardwarePortAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 3, 1, 9),
    _Zxr10HardwarePortAlarmType_Type()
)
zxr10HardwarePortAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwarePortAlarmType.setStatus("current")


class _Zxr10HardwarePortAlarmDescrip_Type(DisplayString):
    """Custom type zxr10HardwarePortAlarmDescrip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10HardwarePortAlarmDescrip_Type.__name__ = "DisplayString"
_Zxr10HardwarePortAlarmDescrip_Object = MibTableColumn
zxr10HardwarePortAlarmDescrip = _Zxr10HardwarePortAlarmDescrip_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 3, 1, 10),
    _Zxr10HardwarePortAlarmDescrip_Type()
)
zxr10HardwarePortAlarmDescrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwarePortAlarmDescrip.setStatus("current")
_Zxr10SoftProtocolAlarmTable_Object = MibTable
zxr10SoftProtocolAlarmTable = _Zxr10SoftProtocolAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 4)
)
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmTable.setStatus("current")
_Zxr10SoftProtocolAlarmEntry_Object = MibTableRow
zxr10SoftProtocolAlarmEntry = _Zxr10SoftProtocolAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 4, 1)
)
zxr10SoftProtocolAlarmEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10SoftProtocolAlarmSaveCode"),
)
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmEntry.setStatus("current")
_Zxr10SoftProtocolAlarmSaveCode_Type = Integer32
_Zxr10SoftProtocolAlarmSaveCode_Object = MibTableColumn
zxr10SoftProtocolAlarmSaveCode = _Zxr10SoftProtocolAlarmSaveCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 4, 1, 1),
    _Zxr10SoftProtocolAlarmSaveCode_Type()
)
zxr10SoftProtocolAlarmSaveCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmSaveCode.setStatus("current")
_Zxr10SoftProtocolAlarmSaveLevel_Type = Integer32
_Zxr10SoftProtocolAlarmSaveLevel_Object = MibTableColumn
zxr10SoftProtocolAlarmSaveLevel = _Zxr10SoftProtocolAlarmSaveLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 4, 1, 2),
    _Zxr10SoftProtocolAlarmSaveLevel_Type()
)
zxr10SoftProtocolAlarmSaveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmSaveLevel.setStatus("current")
_Zxr10SoftProtocolAlarmSaveLasttime_Type = TimeTicks
_Zxr10SoftProtocolAlarmSaveLasttime_Object = MibTableColumn
zxr10SoftProtocolAlarmSaveLasttime = _Zxr10SoftProtocolAlarmSaveLasttime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 4, 1, 3),
    _Zxr10SoftProtocolAlarmSaveLasttime_Type()
)
zxr10SoftProtocolAlarmSaveLasttime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmSaveLasttime.setStatus("current")
_Zxr10SoftProtocolAlarmSaveTotaltimes_Type = Integer32
_Zxr10SoftProtocolAlarmSaveTotaltimes_Object = MibTableColumn
zxr10SoftProtocolAlarmSaveTotaltimes = _Zxr10SoftProtocolAlarmSaveTotaltimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 4, 1, 4),
    _Zxr10SoftProtocolAlarmSaveTotaltimes_Type()
)
zxr10SoftProtocolAlarmSaveTotaltimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmSaveTotaltimes.setStatus("current")
_Zxr10SoftProtocolAlarmSaveType_Type = AlarmType
_Zxr10SoftProtocolAlarmSaveType_Object = MibTableColumn
zxr10SoftProtocolAlarmSaveType = _Zxr10SoftProtocolAlarmSaveType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 4, 1, 5),
    _Zxr10SoftProtocolAlarmSaveType_Type()
)
zxr10SoftProtocolAlarmSaveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmSaveType.setStatus("current")
_Zxr10StatisticsAlarmTable_Object = MibTable
zxr10StatisticsAlarmTable = _Zxr10StatisticsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 5)
)
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmTable.setStatus("current")
_Zxr10StatisticsAlarmEntry_Object = MibTableRow
zxr10StatisticsAlarmEntry = _Zxr10StatisticsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 5, 1)
)
zxr10StatisticsAlarmEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10StatisticsAlarmSaveCode"),
)
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmEntry.setStatus("current")
_Zxr10StatisticsAlarmSaveCode_Type = Integer32
_Zxr10StatisticsAlarmSaveCode_Object = MibTableColumn
zxr10StatisticsAlarmSaveCode = _Zxr10StatisticsAlarmSaveCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 5, 1, 1),
    _Zxr10StatisticsAlarmSaveCode_Type()
)
zxr10StatisticsAlarmSaveCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmSaveCode.setStatus("current")
_Zxr10StatisticsAlarmSaveLevel_Type = Integer32
_Zxr10StatisticsAlarmSaveLevel_Object = MibTableColumn
zxr10StatisticsAlarmSaveLevel = _Zxr10StatisticsAlarmSaveLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 5, 1, 2),
    _Zxr10StatisticsAlarmSaveLevel_Type()
)
zxr10StatisticsAlarmSaveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmSaveLevel.setStatus("current")
_Zxr10StatisticsAlarmSaveLasttime_Type = TimeTicks
_Zxr10StatisticsAlarmSaveLasttime_Object = MibTableColumn
zxr10StatisticsAlarmSaveLasttime = _Zxr10StatisticsAlarmSaveLasttime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 5, 1, 3),
    _Zxr10StatisticsAlarmSaveLasttime_Type()
)
zxr10StatisticsAlarmSaveLasttime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmSaveLasttime.setStatus("current")
_Zxr10StatisticsAlarmSaveTotaltimes_Type = Integer32
_Zxr10StatisticsAlarmSaveTotaltimes_Object = MibTableColumn
zxr10StatisticsAlarmSaveTotaltimes = _Zxr10StatisticsAlarmSaveTotaltimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 5, 1, 4),
    _Zxr10StatisticsAlarmSaveTotaltimes_Type()
)
zxr10StatisticsAlarmSaveTotaltimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmSaveTotaltimes.setStatus("current")
_Zxr10StatisticsAlarmSaveType_Type = AlarmType
_Zxr10StatisticsAlarmSaveType_Object = MibTableColumn
zxr10StatisticsAlarmSaveType = _Zxr10StatisticsAlarmSaveType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 5, 1, 5),
    _Zxr10StatisticsAlarmSaveType_Type()
)
zxr10StatisticsAlarmSaveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmSaveType.setStatus("current")
_Zxr10HardwareAlarmTrapTable_Object = MibTable
zxr10HardwareAlarmTrapTable = _Zxr10HardwareAlarmTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6)
)
if mibBuilder.loadTexts:
    zxr10HardwareAlarmTrapTable.setStatus("current")
_Zxr10HardwareAlarmTrapEntry_Object = MibTableRow
zxr10HardwareAlarmTrapEntry = _Zxr10HardwareAlarmTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6, 1)
)
zxr10HardwareAlarmTrapEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10HardwareAlarmSlotNo"),
    (0, "ZXR10-MIB", "zxr10HardwareAlarmCode"),
)
if mibBuilder.loadTexts:
    zxr10HardwareAlarmTrapEntry.setStatus("current")
_Zxr10HardwareAlarmRackNo_Type = Integer32
_Zxr10HardwareAlarmRackNo_Object = MibTableColumn
zxr10HardwareAlarmRackNo = _Zxr10HardwareAlarmRackNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6, 1, 1),
    _Zxr10HardwareAlarmRackNo_Type()
)
zxr10HardwareAlarmRackNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareAlarmRackNo.setStatus("current")
_Zxr10HardwareAlarmShelfNo_Type = Integer32
_Zxr10HardwareAlarmShelfNo_Object = MibTableColumn
zxr10HardwareAlarmShelfNo = _Zxr10HardwareAlarmShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6, 1, 2),
    _Zxr10HardwareAlarmShelfNo_Type()
)
zxr10HardwareAlarmShelfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareAlarmShelfNo.setStatus("current")
_Zxr10HardwareAlarmSlotNo_Type = Integer32
_Zxr10HardwareAlarmSlotNo_Object = MibTableColumn
zxr10HardwareAlarmSlotNo = _Zxr10HardwareAlarmSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6, 1, 3),
    _Zxr10HardwareAlarmSlotNo_Type()
)
zxr10HardwareAlarmSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareAlarmSlotNo.setStatus("current")
_Zxr10HardwareAlarmPortNo_Type = Integer32
_Zxr10HardwareAlarmPortNo_Object = MibTableColumn
zxr10HardwareAlarmPortNo = _Zxr10HardwareAlarmPortNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6, 1, 4),
    _Zxr10HardwareAlarmPortNo_Type()
)
zxr10HardwareAlarmPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareAlarmPortNo.setStatus("current")
_Zxr10HardwareAlarmCode_Type = Integer32
_Zxr10HardwareAlarmCode_Object = MibTableColumn
zxr10HardwareAlarmCode = _Zxr10HardwareAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6, 1, 5),
    _Zxr10HardwareAlarmCode_Type()
)
zxr10HardwareAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareAlarmCode.setStatus("current")
_Zxr10HardwareAlarmLevel_Type = Integer32
_Zxr10HardwareAlarmLevel_Object = MibTableColumn
zxr10HardwareAlarmLevel = _Zxr10HardwareAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6, 1, 6),
    _Zxr10HardwareAlarmLevel_Type()
)
zxr10HardwareAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareAlarmLevel.setStatus("current")
_Zxr10HardwareAlarmTime_Type = TimeTicks
_Zxr10HardwareAlarmTime_Object = MibTableColumn
zxr10HardwareAlarmTime = _Zxr10HardwareAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6, 1, 7),
    _Zxr10HardwareAlarmTime_Type()
)
zxr10HardwareAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareAlarmTime.setStatus("current")
_Zxr10HardwareAlarmStatus_Type = BoolStatus
_Zxr10HardwareAlarmStatus_Object = MibTableColumn
zxr10HardwareAlarmStatus = _Zxr10HardwareAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6, 1, 8),
    _Zxr10HardwareAlarmStatus_Type()
)
zxr10HardwareAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareAlarmStatus.setStatus("current")
_Zxr10HardwareAlarmType_Type = AlarmType
_Zxr10HardwareAlarmType_Object = MibTableColumn
zxr10HardwareAlarmType = _Zxr10HardwareAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6, 1, 9),
    _Zxr10HardwareAlarmType_Type()
)
zxr10HardwareAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareAlarmType.setStatus("current")
_Zxr10HardwareAlarmVariableValue_Type = Integer32
_Zxr10HardwareAlarmVariableValue_Object = MibTableColumn
zxr10HardwareAlarmVariableValue = _Zxr10HardwareAlarmVariableValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6, 1, 10),
    _Zxr10HardwareAlarmVariableValue_Type()
)
zxr10HardwareAlarmVariableValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareAlarmVariableValue.setStatus("current")
_Zxr10HardwareAlarmValueRisingThreshold_Type = Integer32
_Zxr10HardwareAlarmValueRisingThreshold_Object = MibTableColumn
zxr10HardwareAlarmValueRisingThreshold = _Zxr10HardwareAlarmValueRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6, 1, 11),
    _Zxr10HardwareAlarmValueRisingThreshold_Type()
)
zxr10HardwareAlarmValueRisingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareAlarmValueRisingThreshold.setStatus("current")
_Zxr10HardwareAlarmValueFallingThreshold_Type = Integer32
_Zxr10HardwareAlarmValueFallingThreshold_Object = MibTableColumn
zxr10HardwareAlarmValueFallingThreshold = _Zxr10HardwareAlarmValueFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6, 1, 12),
    _Zxr10HardwareAlarmValueFallingThreshold_Type()
)
zxr10HardwareAlarmValueFallingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareAlarmValueFallingThreshold.setStatus("current")


class _Zxr10HardwareAlarmDescrip_Type(DisplayString):
    """Custom type zxr10HardwareAlarmDescrip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10HardwareAlarmDescrip_Type.__name__ = "DisplayString"
_Zxr10HardwareAlarmDescrip_Object = MibTableColumn
zxr10HardwareAlarmDescrip = _Zxr10HardwareAlarmDescrip_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 6, 1, 13),
    _Zxr10HardwareAlarmDescrip_Type()
)
zxr10HardwareAlarmDescrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10HardwareAlarmDescrip.setStatus("current")
_Zxr10SoftProtocolAlarmTrapTable_Object = MibTable
zxr10SoftProtocolAlarmTrapTable = _Zxr10SoftProtocolAlarmTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 7)
)
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmTrapTable.setStatus("current")
_Zxr10SoftProtocolAlarmTrapEntry_Object = MibTableRow
zxr10SoftProtocolAlarmTrapEntry = _Zxr10SoftProtocolAlarmTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 7, 1)
)
zxr10SoftProtocolAlarmTrapEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10SoftProtocolAlarmSlotNo"),
    (0, "ZXR10-MIB", "zxr10SoftProtocolAlarmCode"),
)
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmTrapEntry.setStatus("current")
_Zxr10SoftProtocolAlarmRackNo_Type = Integer32
_Zxr10SoftProtocolAlarmRackNo_Object = MibTableColumn
zxr10SoftProtocolAlarmRackNo = _Zxr10SoftProtocolAlarmRackNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 7, 1, 1),
    _Zxr10SoftProtocolAlarmRackNo_Type()
)
zxr10SoftProtocolAlarmRackNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmRackNo.setStatus("current")
_Zxr10SoftProtocolAlarmShelfNo_Type = Integer32
_Zxr10SoftProtocolAlarmShelfNo_Object = MibTableColumn
zxr10SoftProtocolAlarmShelfNo = _Zxr10SoftProtocolAlarmShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 7, 1, 2),
    _Zxr10SoftProtocolAlarmShelfNo_Type()
)
zxr10SoftProtocolAlarmShelfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmShelfNo.setStatus("current")
_Zxr10SoftProtocolAlarmSlotNo_Type = Integer32
_Zxr10SoftProtocolAlarmSlotNo_Object = MibTableColumn
zxr10SoftProtocolAlarmSlotNo = _Zxr10SoftProtocolAlarmSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 7, 1, 3),
    _Zxr10SoftProtocolAlarmSlotNo_Type()
)
zxr10SoftProtocolAlarmSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmSlotNo.setStatus("current")
_Zxr10SoftProtocolAlarmCode_Type = Integer32
_Zxr10SoftProtocolAlarmCode_Object = MibTableColumn
zxr10SoftProtocolAlarmCode = _Zxr10SoftProtocolAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 7, 1, 4),
    _Zxr10SoftProtocolAlarmCode_Type()
)
zxr10SoftProtocolAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmCode.setStatus("current")
_Zxr10SoftProtocolAlarmLevel_Type = Integer32
_Zxr10SoftProtocolAlarmLevel_Object = MibTableColumn
zxr10SoftProtocolAlarmLevel = _Zxr10SoftProtocolAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 7, 1, 5),
    _Zxr10SoftProtocolAlarmLevel_Type()
)
zxr10SoftProtocolAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmLevel.setStatus("current")
_Zxr10SoftProtocolAlarmTime_Type = TimeTicks
_Zxr10SoftProtocolAlarmTime_Object = MibTableColumn
zxr10SoftProtocolAlarmTime = _Zxr10SoftProtocolAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 7, 1, 6),
    _Zxr10SoftProtocolAlarmTime_Type()
)
zxr10SoftProtocolAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmTime.setStatus("current")
_Zxr10SoftProtocolAlarmStatus_Type = BoolStatus
_Zxr10SoftProtocolAlarmStatus_Object = MibTableColumn
zxr10SoftProtocolAlarmStatus = _Zxr10SoftProtocolAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 7, 1, 7),
    _Zxr10SoftProtocolAlarmStatus_Type()
)
zxr10SoftProtocolAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmStatus.setStatus("current")
_Zxr10SoftProtocolAlarmType_Type = AlarmType
_Zxr10SoftProtocolAlarmType_Object = MibTableColumn
zxr10SoftProtocolAlarmType = _Zxr10SoftProtocolAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 7, 1, 8),
    _Zxr10SoftProtocolAlarmType_Type()
)
zxr10SoftProtocolAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmType.setStatus("current")


class _Zxr10SoftProtocolAlarmDescrip_Type(DisplayString):
    """Custom type zxr10SoftProtocolAlarmDescrip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10SoftProtocolAlarmDescrip_Type.__name__ = "DisplayString"
_Zxr10SoftProtocolAlarmDescrip_Object = MibTableColumn
zxr10SoftProtocolAlarmDescrip = _Zxr10SoftProtocolAlarmDescrip_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 7, 1, 9),
    _Zxr10SoftProtocolAlarmDescrip_Type()
)
zxr10SoftProtocolAlarmDescrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmDescrip.setStatus("current")
_Zxr10StatisticsAlarmTrapTable_Object = MibTable
zxr10StatisticsAlarmTrapTable = _Zxr10StatisticsAlarmTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8)
)
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmTrapTable.setStatus("current")
_Zxr10StatisticsAlarmTrapEntry_Object = MibTableRow
zxr10StatisticsAlarmTrapEntry = _Zxr10StatisticsAlarmTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8, 1)
)
zxr10StatisticsAlarmTrapEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10StatisticsAlarmSlotNo"),
    (0, "ZXR10-MIB", "zxr10StatisticsAlarmCode"),
)
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmTrapEntry.setStatus("current")
_Zxr10StatisticsAlarmRackNo_Type = Integer32
_Zxr10StatisticsAlarmRackNo_Object = MibTableColumn
zxr10StatisticsAlarmRackNo = _Zxr10StatisticsAlarmRackNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8, 1, 1),
    _Zxr10StatisticsAlarmRackNo_Type()
)
zxr10StatisticsAlarmRackNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmRackNo.setStatus("current")
_Zxr10StatisticsAlarmShelfNo_Type = Integer32
_Zxr10StatisticsAlarmShelfNo_Object = MibTableColumn
zxr10StatisticsAlarmShelfNo = _Zxr10StatisticsAlarmShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8, 1, 2),
    _Zxr10StatisticsAlarmShelfNo_Type()
)
zxr10StatisticsAlarmShelfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmShelfNo.setStatus("current")
_Zxr10StatisticsAlarmSlotNo_Type = Integer32
_Zxr10StatisticsAlarmSlotNo_Object = MibTableColumn
zxr10StatisticsAlarmSlotNo = _Zxr10StatisticsAlarmSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8, 1, 3),
    _Zxr10StatisticsAlarmSlotNo_Type()
)
zxr10StatisticsAlarmSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmSlotNo.setStatus("current")
_Zxr10StatisticsAlarmPortNo_Type = Integer32
_Zxr10StatisticsAlarmPortNo_Object = MibTableColumn
zxr10StatisticsAlarmPortNo = _Zxr10StatisticsAlarmPortNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8, 1, 4),
    _Zxr10StatisticsAlarmPortNo_Type()
)
zxr10StatisticsAlarmPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmPortNo.setStatus("current")
_Zxr10StatisticsAlarmCode_Type = Integer32
_Zxr10StatisticsAlarmCode_Object = MibTableColumn
zxr10StatisticsAlarmCode = _Zxr10StatisticsAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8, 1, 5),
    _Zxr10StatisticsAlarmCode_Type()
)
zxr10StatisticsAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmCode.setStatus("current")
_Zxr10StatisticsAlarmLevel_Type = Integer32
_Zxr10StatisticsAlarmLevel_Object = MibTableColumn
zxr10StatisticsAlarmLevel = _Zxr10StatisticsAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8, 1, 6),
    _Zxr10StatisticsAlarmLevel_Type()
)
zxr10StatisticsAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmLevel.setStatus("current")
_Zxr10StatisticsAlarmTime_Type = TimeTicks
_Zxr10StatisticsAlarmTime_Object = MibTableColumn
zxr10StatisticsAlarmTime = _Zxr10StatisticsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8, 1, 7),
    _Zxr10StatisticsAlarmTime_Type()
)
zxr10StatisticsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmTime.setStatus("current")
_Zxr10StatisticsAlarmStatus_Type = BoolStatus
_Zxr10StatisticsAlarmStatus_Object = MibTableColumn
zxr10StatisticsAlarmStatus = _Zxr10StatisticsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8, 1, 8),
    _Zxr10StatisticsAlarmStatus_Type()
)
zxr10StatisticsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmStatus.setStatus("current")
_Zxr10StatisticsAlarmType_Type = AlarmType
_Zxr10StatisticsAlarmType_Object = MibTableColumn
zxr10StatisticsAlarmType = _Zxr10StatisticsAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8, 1, 9),
    _Zxr10StatisticsAlarmType_Type()
)
zxr10StatisticsAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmType.setStatus("current")
_Zxr10StatisticsAlarmVariableValue_Type = Integer32
_Zxr10StatisticsAlarmVariableValue_Object = MibTableColumn
zxr10StatisticsAlarmVariableValue = _Zxr10StatisticsAlarmVariableValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8, 1, 10),
    _Zxr10StatisticsAlarmVariableValue_Type()
)
zxr10StatisticsAlarmVariableValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmVariableValue.setStatus("current")
_Zxr10StatisticsAlarmValueRisingThreshold_Type = Integer32
_Zxr10StatisticsAlarmValueRisingThreshold_Object = MibTableColumn
zxr10StatisticsAlarmValueRisingThreshold = _Zxr10StatisticsAlarmValueRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8, 1, 11),
    _Zxr10StatisticsAlarmValueRisingThreshold_Type()
)
zxr10StatisticsAlarmValueRisingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmValueRisingThreshold.setStatus("current")
_Zxr10StatisticsAlarmValueFallingThreshold_Type = Integer32
_Zxr10StatisticsAlarmValueFallingThreshold_Object = MibTableColumn
zxr10StatisticsAlarmValueFallingThreshold = _Zxr10StatisticsAlarmValueFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8, 1, 12),
    _Zxr10StatisticsAlarmValueFallingThreshold_Type()
)
zxr10StatisticsAlarmValueFallingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmValueFallingThreshold.setStatus("current")


class _Zxr10StatisticsAlarmDescrip_Type(DisplayString):
    """Custom type zxr10StatisticsAlarmDescrip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10StatisticsAlarmDescrip_Type.__name__ = "DisplayString"
_Zxr10StatisticsAlarmDescrip_Object = MibTableColumn
zxr10StatisticsAlarmDescrip = _Zxr10StatisticsAlarmDescrip_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 8, 1, 13),
    _Zxr10StatisticsAlarmDescrip_Type()
)
zxr10StatisticsAlarmDescrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmDescrip.setStatus("current")
_Zxr10AlarmTrap_ObjectIdentity = ObjectIdentity
zxr10AlarmTrap = _Zxr10AlarmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 20)
)
_Zxr10_objectID_ObjectIdentity = ObjectIdentity
zxr10_objectID = _Zxr10_objectID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100)
)
_Zxr10RouterT128SysID_ObjectIdentity = ObjectIdentity
zxr10RouterT128SysID = _Zxr10RouterT128SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 1)
)
if mibBuilder.loadTexts:
    zxr10RouterT128SysID.setStatus("current")
_Zxr10RouterT64SysID_ObjectIdentity = ObjectIdentity
zxr10RouterT64SysID = _Zxr10RouterT64SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 2)
)
if mibBuilder.loadTexts:
    zxr10RouterT64SysID.setStatus("current")
_Zxr10SwitchT32SysID_ObjectIdentity = ObjectIdentity
zxr10SwitchT32SysID = _Zxr10SwitchT32SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 3)
)
if mibBuilder.loadTexts:
    zxr10SwitchT32SysID.setStatus("current")
_Zxr10RouterGAR_2608SysID_ObjectIdentity = ObjectIdentity
zxr10RouterGAR_2608SysID = _Zxr10RouterGAR_2608SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 4)
)
if mibBuilder.loadTexts:
    zxr10RouterGAR_2608SysID.setStatus("current")
_Zxr10RouterGER8SysID_ObjectIdentity = ObjectIdentity
zxr10RouterGER8SysID = _Zxr10RouterGER8SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 5)
)
if mibBuilder.loadTexts:
    zxr10RouterGER8SysID.setStatus("current")
_Zxr10RouterGAR_2604SysID_ObjectIdentity = ObjectIdentity
zxr10RouterGAR_2604SysID = _Zxr10RouterGAR_2604SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 6)
)
if mibBuilder.loadTexts:
    zxr10RouterGAR_2604SysID.setStatus("current")
_Zxr10SwitchT160GSysID_ObjectIdentity = ObjectIdentity
zxr10SwitchT160GSysID = _Zxr10SwitchT160GSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 7)
)
if mibBuilder.loadTexts:
    zxr10SwitchT160GSysID.setStatus("current")
_Zxr10RouterGAR_3608SysID_ObjectIdentity = ObjectIdentity
zxr10RouterGAR_3608SysID = _Zxr10RouterGAR_3608SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 8)
)
if mibBuilder.loadTexts:
    zxr10RouterGAR_3608SysID.setStatus("current")
_Zxr10RouterGAR_7208SysID_ObjectIdentity = ObjectIdentity
zxr10RouterGAR_7208SysID = _Zxr10RouterGAR_7208SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 9)
)
if mibBuilder.loadTexts:
    zxr10RouterGAR_7208SysID.setStatus("current")
_Zxr10SwitchT64GSysID_ObjectIdentity = ObjectIdentity
zxr10SwitchT64GSysID = _Zxr10SwitchT64GSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 10)
)
if mibBuilder.loadTexts:
    zxr10SwitchT64GSysID.setStatus("current")
_Zxr10Switch3206SysID_ObjectIdentity = ObjectIdentity
zxr10Switch3206SysID = _Zxr10Switch3206SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 11)
)
if mibBuilder.loadTexts:
    zxr10Switch3206SysID.setStatus("current")
_Zxr10Switch3906SysID_ObjectIdentity = ObjectIdentity
zxr10Switch3906SysID = _Zxr10Switch3906SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 12)
)
if mibBuilder.loadTexts:
    zxr10Switch3906SysID.setStatus("current")
_Zxr10Switch3228SysID_ObjectIdentity = ObjectIdentity
zxr10Switch3228SysID = _Zxr10Switch3228SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 13)
)
if mibBuilder.loadTexts:
    zxr10Switch3228SysID.setStatus("current")
_Zxr10Switch3928SysID_ObjectIdentity = ObjectIdentity
zxr10Switch3928SysID = _Zxr10Switch3928SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 14)
)
if mibBuilder.loadTexts:
    zxr10Switch3928SysID.setStatus("current")
_Zxr10Switch3252SysID_ObjectIdentity = ObjectIdentity
zxr10Switch3252SysID = _Zxr10Switch3252SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 15)
)
if mibBuilder.loadTexts:
    zxr10Switch3252SysID.setStatus("current")
_Zxr10Switch3952SysID_ObjectIdentity = ObjectIdentity
zxr10Switch3952SysID = _Zxr10Switch3952SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 16)
)
if mibBuilder.loadTexts:
    zxr10Switch3952SysID.setStatus("current")
_Zxr10Switch5224SysID_ObjectIdentity = ObjectIdentity
zxr10Switch5224SysID = _Zxr10Switch5224SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 17)
)
if mibBuilder.loadTexts:
    zxr10Switch5224SysID.setStatus("current")
_Zxr10Switch5228SysID_ObjectIdentity = ObjectIdentity
zxr10Switch5228SysID = _Zxr10Switch5228SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 18)
)
if mibBuilder.loadTexts:
    zxr10Switch5228SysID.setStatus("current")
_Zxr10Switch5228FSysID_ObjectIdentity = ObjectIdentity
zxr10Switch5228FSysID = _Zxr10Switch5228FSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 19)
)
if mibBuilder.loadTexts:
    zxr10Switch5228FSysID.setStatus("current")
_Zxr10Switch5928SysID_ObjectIdentity = ObjectIdentity
zxr10Switch5928SysID = _Zxr10Switch5928SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 20)
)
if mibBuilder.loadTexts:
    zxr10Switch5928SysID.setStatus("current")
_Zxr10Switch5928FSysID_ObjectIdentity = ObjectIdentity
zxr10Switch5928FSysID = _Zxr10Switch5928FSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 21)
)
if mibBuilder.loadTexts:
    zxr10Switch5928FSysID.setStatus("current")
_Zxr10Switch5252SysID_ObjectIdentity = ObjectIdentity
zxr10Switch5252SysID = _Zxr10Switch5252SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 22)
)
if mibBuilder.loadTexts:
    zxr10Switch5252SysID.setStatus("current")
_Zxr10Switch5952SysID_ObjectIdentity = ObjectIdentity
zxr10Switch5952SysID = _Zxr10Switch5952SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 23)
)
if mibBuilder.loadTexts:
    zxr10Switch5952SysID.setStatus("current")
_Zxr10Switch3226SysID_ObjectIdentity = ObjectIdentity
zxr10Switch3226SysID = _Zxr10Switch3226SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 24)
)
if mibBuilder.loadTexts:
    zxr10Switch3226SysID.setStatus("current")
_Zxr10SwitchT40GSysID_ObjectIdentity = ObjectIdentity
zxr10SwitchT40GSysID = _Zxr10SwitchT40GSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 25)
)
if mibBuilder.loadTexts:
    zxr10SwitchT40GSysID.setStatus("current")
_Zxr10RouterT1200SysID_ObjectIdentity = ObjectIdentity
zxr10RouterT1200SysID = _Zxr10RouterT1200SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 26)
)
if mibBuilder.loadTexts:
    zxr10RouterT1200SysID.setStatus("current")
_Zxr10RouterT600SysID_ObjectIdentity = ObjectIdentity
zxr10RouterT600SysID = _Zxr10RouterT600SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 27)
)
if mibBuilder.loadTexts:
    zxr10RouterT600SysID.setStatus("current")
_Zxr10RouterGER2SysID_ObjectIdentity = ObjectIdentity
zxr10RouterGER2SysID = _Zxr10RouterGER2SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 28)
)
if mibBuilder.loadTexts:
    zxr10RouterGER2SysID.setStatus("current")
_Zxr10RouterGER4SysID_ObjectIdentity = ObjectIdentity
zxr10RouterGER4SysID = _Zxr10RouterGER4SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 29)
)
if mibBuilder.loadTexts:
    zxr10RouterGER4SysID.setStatus("current")
_Zxr10Switch3226FISysID_ObjectIdentity = ObjectIdentity
zxr10Switch3226FISysID = _Zxr10Switch3226FISysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 30)
)
if mibBuilder.loadTexts:
    zxr10Switch3226FISysID.setStatus("current")
_Zxr10Switch3928ASysID_ObjectIdentity = ObjectIdentity
zxr10Switch3928ASysID = _Zxr10Switch3928ASysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 31)
)
if mibBuilder.loadTexts:
    zxr10Switch3928ASysID.setStatus("current")
_Zxr10Switch3928AFISysID_ObjectIdentity = ObjectIdentity
zxr10Switch3928AFISysID = _Zxr10Switch3928AFISysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 32)
)
if mibBuilder.loadTexts:
    zxr10Switch3928AFISysID.setStatus("current")
_Zxr10Switch3952ASysID_ObjectIdentity = ObjectIdentity
zxr10Switch3952ASysID = _Zxr10Switch3952ASysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 33)
)
if mibBuilder.loadTexts:
    zxr10Switch3952ASysID.setStatus("current")
_Zxr10Switch3228A_EISysID_ObjectIdentity = ObjectIdentity
zxr10Switch3228A_EISysID = _Zxr10Switch3228A_EISysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 34)
)
if mibBuilder.loadTexts:
    zxr10Switch3228A_EISysID.setStatus("current")
_Zxr10Switch3228ASysID_ObjectIdentity = ObjectIdentity
zxr10Switch3228ASysID = _Zxr10Switch3228ASysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 35)
)
if mibBuilder.loadTexts:
    zxr10Switch3228ASysID.setStatus("current")
_Zxr10Switch3228A_FISysID_ObjectIdentity = ObjectIdentity
zxr10Switch3228A_FISysID = _Zxr10Switch3228A_FISysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 36)
)
if mibBuilder.loadTexts:
    zxr10Switch3228A_FISysID.setStatus("current")
_Zxr10Switch3252ASysID_ObjectIdentity = ObjectIdentity
zxr10Switch3252ASysID = _Zxr10Switch3252ASysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 37)
)
if mibBuilder.loadTexts:
    zxr10Switch3252ASysID.setStatus("current")
_Zxr10Switch5228ASysID_ObjectIdentity = ObjectIdentity
zxr10Switch5228ASysID = _Zxr10Switch5228ASysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 38)
)
if mibBuilder.loadTexts:
    zxr10Switch5228ASysID.setStatus("current")
_Zxr10Switch5252ASysID_ObjectIdentity = ObjectIdentity
zxr10Switch5252ASysID = _Zxr10Switch5252ASysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 39)
)
if mibBuilder.loadTexts:
    zxr10Switch5252ASysID.setStatus("current")
_Zxr10Switch5928ESysID_ObjectIdentity = ObjectIdentity
zxr10Switch5928ESysID = _Zxr10Switch5928ESysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 40)
)
if mibBuilder.loadTexts:
    zxr10Switch5928ESysID.setStatus("current")
_Zxr10Switch5928E_FISysID_ObjectIdentity = ObjectIdentity
zxr10Switch5928E_FISysID = _Zxr10Switch5928E_FISysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 41)
)
if mibBuilder.loadTexts:
    zxr10Switch5928E_FISysID.setStatus("current")
_Zxr10Switch3952ESysID_ObjectIdentity = ObjectIdentity
zxr10Switch3952ESysID = _Zxr10Switch3952ESysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 42)
)
if mibBuilder.loadTexts:
    zxr10Switch3952ESysID.setStatus("current")
_Zxr10Switch5952ESysID_ObjectIdentity = ObjectIdentity
zxr10Switch5952ESysID = _Zxr10Switch5952ESysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 43)
)
if mibBuilder.loadTexts:
    zxr10Switch5952ESysID.setStatus("current")
_Zxr10RouterR10_1822_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1822_ACSysID = _Zxr10RouterR10_1822_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 100)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1822_ACSysID.setStatus("current")
_Zxr10RouterR10_1822_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1822_DCSysID = _Zxr10RouterR10_1822_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 101)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1822_DCSysID.setStatus("current")
_Zxr10RouterR10_1821_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1821_ACSysID = _Zxr10RouterR10_1821_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 102)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1821_ACSysID.setStatus("current")
_Zxr10RouterR10_1821_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1821_DCSysID = _Zxr10RouterR10_1821_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 103)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1821_DCSysID.setStatus("current")
_Zxr10RouterR10_1812_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1812_ACSysID = _Zxr10RouterR10_1812_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 104)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1812_ACSysID.setStatus("current")
_Zxr10RouterR10_1812_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1812_DCSysID = _Zxr10RouterR10_1812_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 105)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1812_DCSysID.setStatus("current")
_Zxr10RouterR10_1811_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1811_ACSysID = _Zxr10RouterR10_1811_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 106)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1811_ACSysID.setStatus("current")
_Zxr10RouterR10_1811_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1811_DCSysID = _Zxr10RouterR10_1811_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 107)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1811_DCSysID.setStatus("current")
_Zxr10RouterR10_1822E_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1822E_ACSysID = _Zxr10RouterR10_1822E_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 108)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1822E_ACSysID.setStatus("current")
_Zxr10RouterR10_1822E_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1822E_DCSysID = _Zxr10RouterR10_1822E_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 109)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1822E_DCSysID.setStatus("current")
_Zxr10RouterR10_1821E_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1821E_ACSysID = _Zxr10RouterR10_1821E_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 110)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1821E_ACSysID.setStatus("current")
_Zxr10RouterR10_1821E_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1821E_DCSysID = _Zxr10RouterR10_1821E_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 111)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1821E_DCSysID.setStatus("current")
_Zxr10RouterR10_1812E_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1812E_ACSysID = _Zxr10RouterR10_1812E_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 112)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1812E_ACSysID.setStatus("current")
_Zxr10RouterR10_1812E_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1812E_DCSysID = _Zxr10RouterR10_1812E_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 113)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1812E_DCSysID.setStatus("current")
_Zxr10RouterR10_1811E_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1811E_ACSysID = _Zxr10RouterR10_1811E_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 114)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1811E_ACSysID.setStatus("current")
_Zxr10RouterR10_1811E_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1811E_DCSysID = _Zxr10RouterR10_1811E_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 115)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1811E_DCSysID.setStatus("current")
_Zxr10RouterR10_3881_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3881_ACSysID = _Zxr10RouterR10_3881_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 132)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3881_ACSysID.setStatus("current")
_Zxr10RouterR10_3882_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3882_ACSysID = _Zxr10RouterR10_3882_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 133)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3882_ACSysID.setStatus("current")
_Zxr10RouterR10_3883_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3883_ACSysID = _Zxr10RouterR10_3883_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 134)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3883_ACSysID.setStatus("current")
_Zxr10RouterR10_3884_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3884_ACSysID = _Zxr10RouterR10_3884_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 135)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3884_ACSysID.setStatus("current")
_Zxr10RouterR10_3881_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3881_DCSysID = _Zxr10RouterR10_3881_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 136)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3881_DCSysID.setStatus("current")
_Zxr10RouterR10_3882_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3882_DCSysID = _Zxr10RouterR10_3882_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 137)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3882_DCSysID.setStatus("current")
_Zxr10RouterR10_3883_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3883_DCSysID = _Zxr10RouterR10_3883_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 138)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3883_DCSysID.setStatus("current")
_Zxr10RouterR10_3884_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3884_DCSysID = _Zxr10RouterR10_3884_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 139)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3884_DCSysID.setStatus("current")
_Zxr10RouterR10_3841_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3841_ACSysID = _Zxr10RouterR10_3841_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 140)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3841_ACSysID.setStatus("current")
_Zxr10RouterR10_3842_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3842_ACSysID = _Zxr10RouterR10_3842_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 141)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3842_ACSysID.setStatus("current")
_Zxr10RouterR10_3843_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3843_ACSysID = _Zxr10RouterR10_3843_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 142)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3843_ACSysID.setStatus("current")
_Zxr10RouterR10_3844_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3844_ACSysID = _Zxr10RouterR10_3844_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 143)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3844_ACSysID.setStatus("current")
_Zxr10RouterR10_3841_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3841_DCSysID = _Zxr10RouterR10_3841_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 144)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3841_DCSysID.setStatus("current")
_Zxr10RouterR10_3842_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3842_DCSysID = _Zxr10RouterR10_3842_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 145)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3842_DCSysID.setStatus("current")
_Zxr10RouterR10_3843_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3843_DCSysID = _Zxr10RouterR10_3843_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 146)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3843_DCSysID.setStatus("current")
_Zxr10RouterR10_3844_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3844_DCSysID = _Zxr10RouterR10_3844_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 147)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3844_DCSysID.setStatus("current")
_Zxr10RouterR10_3821_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3821_ACSysID = _Zxr10RouterR10_3821_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 148)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3821_ACSysID.setStatus("current")
_Zxr10RouterR10_3822_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3822_ACSysID = _Zxr10RouterR10_3822_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 149)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3822_ACSysID.setStatus("current")
_Zxr10RouterR10_3823_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3823_ACSysID = _Zxr10RouterR10_3823_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 150)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3823_ACSysID.setStatus("current")
_Zxr10RouterR10_3824_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3824_ACSysID = _Zxr10RouterR10_3824_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 151)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3824_ACSysID.setStatus("current")
_Zxr10RouterR10_3821_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3821_DCSysID = _Zxr10RouterR10_3821_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 152)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3821_DCSysID.setStatus("current")
_Zxr10RouterR10_3822_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3822_DCSysID = _Zxr10RouterR10_3822_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 153)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3822_DCSysID.setStatus("current")
_Zxr10RouterR10_3823_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3823_DCSysID = _Zxr10RouterR10_3823_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 154)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3823_DCSysID.setStatus("current")
_Zxr10RouterR10_3824_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_3824_DCSysID = _Zxr10RouterR10_3824_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 155)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_3824_DCSysID.setStatus("current")
_Zxr10RouterR10_2841_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2841_ACSysID = _Zxr10RouterR10_2841_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 172)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2841_ACSysID.setStatus("current")
_Zxr10RouterR10_2842_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2842_ACSysID = _Zxr10RouterR10_2842_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 173)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2842_ACSysID.setStatus("current")
_Zxr10RouterR10_2843_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2843_ACSysID = _Zxr10RouterR10_2843_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 174)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2843_ACSysID.setStatus("current")
_Zxr10RouterR10_2844_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2844_ACSysID = _Zxr10RouterR10_2844_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 175)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2844_ACSysID.setStatus("current")
_Zxr10RouterR10_2841_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2841_DCSysID = _Zxr10RouterR10_2841_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 176)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2841_DCSysID.setStatus("current")
_Zxr10RouterR10_2842_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2842_DCSysID = _Zxr10RouterR10_2842_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 177)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2842_DCSysID.setStatus("current")
_Zxr10RouterR10_2843_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2843_DCSysID = _Zxr10RouterR10_2843_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 178)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2843_DCSysID.setStatus("current")
_Zxr10RouterR10_2844_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2844_DCSysID = _Zxr10RouterR10_2844_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 179)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2844_DCSysID.setStatus("current")
_Zxr10RouterR10_2881_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2881_ACSysID = _Zxr10RouterR10_2881_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 180)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2881_ACSysID.setStatus("current")
_Zxr10RouterR10_2882_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2882_ACSysID = _Zxr10RouterR10_2882_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 181)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2882_ACSysID.setStatus("current")
_Zxr10RouterR10_2883_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2883_ACSysID = _Zxr10RouterR10_2883_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 182)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2883_ACSysID.setStatus("current")
_Zxr10RouterR10_2884_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2884_ACSysID = _Zxr10RouterR10_2884_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 183)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2884_ACSysID.setStatus("current")
_Zxr10RouterR10_2881_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2881_DCSysID = _Zxr10RouterR10_2881_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 184)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2881_DCSysID.setStatus("current")
_Zxr10RouterR10_2882_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2882_DCSysID = _Zxr10RouterR10_2882_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 185)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2882_DCSysID.setStatus("current")
_Zxr10RouterR10_2883_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2883_DCSysID = _Zxr10RouterR10_2883_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 186)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2883_DCSysID.setStatus("current")
_Zxr10RouterR10_2884_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2884_DCSysID = _Zxr10RouterR10_2884_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 187)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2884_DCSysID.setStatus("current")
_Zxr10RouterR10_2821_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2821_ACSysID = _Zxr10RouterR10_2821_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 188)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2821_ACSysID.setStatus("current")
_Zxr10RouterR10_2822_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2822_ACSysID = _Zxr10RouterR10_2822_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 189)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2822_ACSysID.setStatus("current")
_Zxr10RouterR10_2823_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2823_ACSysID = _Zxr10RouterR10_2823_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 190)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2823_ACSysID.setStatus("current")
_Zxr10RouterR10_2824_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2824_ACSysID = _Zxr10RouterR10_2824_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 191)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2824_ACSysID.setStatus("current")
_Zxr10RouterR10_2821_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2821_DCSysID = _Zxr10RouterR10_2821_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 192)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2821_DCSysID.setStatus("current")
_Zxr10RouterR10_2822_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2822_DCSysID = _Zxr10RouterR10_2822_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 193)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2822_DCSysID.setStatus("current")
_Zxr10RouterR10_2823_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2823_DCSysID = _Zxr10RouterR10_2823_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 194)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2823_DCSysID.setStatus("current")
_Zxr10RouterR10_2824_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_2824_DCSysID = _Zxr10RouterR10_2824_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 195)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_2824_DCSysID.setStatus("current")
_Zxr10RouterR10_1841_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1841_ACSysID = _Zxr10RouterR10_1841_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 196)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1841_ACSysID.setStatus("current")
_Zxr10RouterR10_1842_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1842_ACSysID = _Zxr10RouterR10_1842_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 197)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1842_ACSysID.setStatus("current")
_Zxr10RouterR10_1843_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1843_ACSysID = _Zxr10RouterR10_1843_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 198)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1843_ACSysID.setStatus("current")
_Zxr10RouterR10_1844_ACSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1844_ACSysID = _Zxr10RouterR10_1844_ACSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 199)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1844_ACSysID.setStatus("current")
_Zxr10RouterR10_1841_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1841_DCSysID = _Zxr10RouterR10_1841_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 200)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1841_DCSysID.setStatus("current")
_Zxr10RouterR10_1842_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1842_DCSysID = _Zxr10RouterR10_1842_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 201)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1842_DCSysID.setStatus("current")
_Zxr10RouterR10_1843_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1843_DCSysID = _Zxr10RouterR10_1843_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 202)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1843_DCSysID.setStatus("current")
_Zxr10RouterR10_1844_DCSysID_ObjectIdentity = ObjectIdentity
zxr10RouterR10_1844_DCSysID = _Zxr10RouterR10_1844_DCSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 203)
)
if mibBuilder.loadTexts:
    zxr10RouterR10_1844_DCSysID.setStatus("current")
_Zxr10Switch_6907SysID_ObjectIdentity = ObjectIdentity
zxr10Switch_6907SysID = _Zxr10Switch_6907SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 400)
)
if mibBuilder.loadTexts:
    zxr10Switch_6907SysID.setStatus("current")
_Zxr10Switch_T240GSysID_ObjectIdentity = ObjectIdentity
zxr10Switch_T240GSysID = _Zxr10Switch_T240GSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 401)
)
if mibBuilder.loadTexts:
    zxr10Switch_T240GSysID.setStatus("current")
_Zxr10Switch_6902SysID_ObjectIdentity = ObjectIdentity
zxr10Switch_6902SysID = _Zxr10Switch_6902SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 402)
)
if mibBuilder.loadTexts:
    zxr10Switch_6902SysID.setStatus("current")
_Zxr10Switch_6905SysID_ObjectIdentity = ObjectIdentity
zxr10Switch_6905SysID = _Zxr10Switch_6905SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 403)
)
if mibBuilder.loadTexts:
    zxr10Switch_6905SysID.setStatus("current")
_Zxr10Switch_6908SysID_ObjectIdentity = ObjectIdentity
zxr10Switch_6908SysID = _Zxr10Switch_6908SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 404)
)
if mibBuilder.loadTexts:
    zxr10Switch_6908SysID.setStatus("current")
_Zxr10Switch_8902SysID_ObjectIdentity = ObjectIdentity
zxr10Switch_8902SysID = _Zxr10Switch_8902SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 405)
)
if mibBuilder.loadTexts:
    zxr10Switch_8902SysID.setStatus("current")
_Zxr10Switch_8905SysID_ObjectIdentity = ObjectIdentity
zxr10Switch_8905SysID = _Zxr10Switch_8905SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 406)
)
if mibBuilder.loadTexts:
    zxr10Switch_8905SysID.setStatus("current")
_Zxr10Switch_8908SysID_ObjectIdentity = ObjectIdentity
zxr10Switch_8908SysID = _Zxr10Switch_8908SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 407)
)
if mibBuilder.loadTexts:
    zxr10Switch_8908SysID.setStatus("current")
_Zxr10Switch_8912SysID_ObjectIdentity = ObjectIdentity
zxr10Switch_8912SysID = _Zxr10Switch_8912SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 408)
)
if mibBuilder.loadTexts:
    zxr10Switch_8912SysID.setStatus("current")
_Zxctn_6100SysID_ObjectIdentity = ObjectIdentity
zxctn_6100SysID = _Zxctn_6100SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 409)
)
if mibBuilder.loadTexts:
    zxctn_6100SysID.setStatus("current")
_Zxr10Switch5928_PSSysID_ObjectIdentity = ObjectIdentity
zxr10Switch5928_PSSysID = _Zxr10Switch5928_PSSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 417)
)
if mibBuilder.loadTexts:
    zxr10Switch5928_PSSysID.setStatus("current")
_Zxr10Switch3928A_PSSysID_ObjectIdentity = ObjectIdentity
zxr10Switch3928A_PSSysID = _Zxr10Switch3928A_PSSysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 418)
)
if mibBuilder.loadTexts:
    zxr10Switch3928A_PSSysID.setStatus("current")
_Zxr10Switch3928ESysID_ObjectIdentity = ObjectIdentity
zxr10Switch3928ESysID = _Zxr10Switch3928ESysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 419)
)
if mibBuilder.loadTexts:
    zxr10Switch3928ESysID.setStatus("current")
_Zxr10Switch3928E_FISysID_ObjectIdentity = ObjectIdentity
zxr10Switch3928E_FISysID = _Zxr10Switch3928E_FISysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 420)
)
if mibBuilder.loadTexts:
    zxr10Switch3928E_FISysID.setStatus("current")
_Zxr10UAS10600SysID_ObjectIdentity = ObjectIdentity
zxr10UAS10600SysID = _Zxr10UAS10600SysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 100, 5000)
)
if mibBuilder.loadTexts:
    zxr10UAS10600SysID.setStatus("current")

# Managed Objects groups


# Notification objects

zxr10HardwareAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 20, 1)
)
zxr10HardwareAlarmTrap.setObjects(
      *(("ZXR10-MIB", "zxr10HardwareAlarmRackNo"),
        ("ZXR10-MIB", "zxr10HardwareAlarmShelfNo"),
        ("ZXR10-MIB", "zxr10HardwareAlarmSlotNo"),
        ("ZXR10-MIB", "zxr10HardwareAlarmPortNo"),
        ("ZXR10-MIB", "zxr10HardwareAlarmCode"),
        ("ZXR10-MIB", "zxr10HardwareAlarmLevel"),
        ("ZXR10-MIB", "zxr10HardwareAlarmTime"),
        ("ZXR10-MIB", "zxr10HardwareAlarmStatus"),
        ("ZXR10-MIB", "zxr10HardwareAlarmType"),
        ("ZXR10-MIB", "zxr10HardwareAlarmVariableValue"),
        ("ZXR10-MIB", "zxr10HardwareAlarmValueRisingThreshold"),
        ("ZXR10-MIB", "zxr10HardwareAlarmValueFallingThreshold"),
        ("ZXR10-MIB", "zxr10HardwareAlarmDescrip"))
)
if mibBuilder.loadTexts:
    zxr10HardwareAlarmTrap.setStatus(
        "current"
    )

zxr10SoftProtocolAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 20, 2)
)
zxr10SoftProtocolAlarmTrap.setObjects(
      *(("ZXR10-MIB", "zxr10SoftProtocolAlarmRackNo"),
        ("ZXR10-MIB", "zxr10SoftProtocolAlarmShelfNo"),
        ("ZXR10-MIB", "zxr10SoftProtocolAlarmSlotNo"),
        ("ZXR10-MIB", "zxr10SoftProtocolAlarmCode"),
        ("ZXR10-MIB", "zxr10SoftProtocolAlarmLevel"),
        ("ZXR10-MIB", "zxr10SoftProtocolAlarmTime"),
        ("ZXR10-MIB", "zxr10SoftProtocolAlarmStatus"),
        ("ZXR10-MIB", "zxr10SoftProtocolAlarmType"),
        ("ZXR10-MIB", "zxr10SoftProtocolAlarmDescrip"))
)
if mibBuilder.loadTexts:
    zxr10SoftProtocolAlarmTrap.setStatus(
        "current"
    )

zxr10StatisticsAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 4, 20, 3)
)
zxr10StatisticsAlarmTrap.setObjects(
      *(("ZXR10-MIB", "zxr10StatisticsAlarmRackNo"),
        ("ZXR10-MIB", "zxr10StatisticsAlarmShelfNo"),
        ("ZXR10-MIB", "zxr10StatisticsAlarmSlotNo"),
        ("ZXR10-MIB", "zxr10StatisticsAlarmPortNo"),
        ("ZXR10-MIB", "zxr10StatisticsAlarmCode"),
        ("ZXR10-MIB", "zxr10StatisticsAlarmLevel"),
        ("ZXR10-MIB", "zxr10StatisticsAlarmTime"),
        ("ZXR10-MIB", "zxr10StatisticsAlarmStatus"),
        ("ZXR10-MIB", "zxr10StatisticsAlarmType"),
        ("ZXR10-MIB", "zxr10StatisticsAlarmVariableValue"),
        ("ZXR10-MIB", "zxr10StatisticsAlarmValueRisingThreshold"),
        ("ZXR10-MIB", "zxr10StatisticsAlarmValueFallingThreshold"),
        ("ZXR10-MIB", "zxr10StatisticsAlarmDescrip"))
)
if mibBuilder.loadTexts:
    zxr10StatisticsAlarmTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-MIB",
    **{"DisplayString": DisplayString,
       "AvailStatus": AvailStatus,
       "OperStatus": OperStatus,
       "PortProperty": PortProperty,
       "MasterStatus": MasterStatus,
       "UnitRunStatus": UnitRunStatus,
       "PidUsedStatus": PidUsedStatus,
       "BoolStatus": BoolStatus,
       "ProductID": ProductID,
       "BoardType": BoardType,
       "NpcType": NpcType,
       "PortType": PortType,
       "AlarmType": AlarmType,
       "PortWorkingType": PortWorkingType,
       "ShelfAttrib": ShelfAttrib,
       "HostAttr": HostAttr,
       "SystemDeviceType": SystemDeviceType,
       "zte": zte,
       "zxr10": zxr10,
       "zxr10systemconfig": zxr10systemconfig,
       "zxr10SystemID": zxr10SystemID,
       "zxr10SystemserialNo": zxr10SystemserialNo,
       "zxr10SystemDescrip": zxr10SystemDescrip,
       "zxr10SystemTrapHost": zxr10SystemTrapHost,
       "zxr10SystemTrapCommunity": zxr10SystemTrapCommunity,
       "zxr10SystemVersion": zxr10SystemVersion,
       "zxr10SystemVpnName": zxr10SystemVpnName,
       "zxr10SystemHostAttr": zxr10SystemHostAttr,
       "zxr10SystemEnableSecret": zxr10SystemEnableSecret,
       "zxr10SystemDeviceType": zxr10SystemDeviceType,
       "zxr10rack": zxr10rack,
       "zxr10rackTable": zxr10rackTable,
       "zxr10rackEntry": zxr10rackEntry,
       "zxr10RackNo": zxr10RackNo,
       "zxr10RackAttrib": zxr10RackAttrib,
       "zxr10RackAvailStatus": zxr10RackAvailStatus,
       "zxr10shelfTable": zxr10shelfTable,
       "zxr10shelfEntry": zxr10shelfEntry,
       "zxr10ShelfNo": zxr10ShelfNo,
       "zxr10ShelfAttrib": zxr10ShelfAttrib,
       "zxr10ShelfAvailStatus": zxr10ShelfAvailStatus,
       "zxr10slotTable": zxr10slotTable,
       "zxr10slotEntry": zxr10slotEntry,
       "zxr10PaneNo": zxr10PaneNo,
       "zxr10PosInRack": zxr10PosInRack,
       "zxr10SlotBoardType": zxr10SlotBoardType,
       "zxr10SlotNPCType": zxr10SlotNPCType,
       "zxr10SlotPortsNumber": zxr10SlotPortsNumber,
       "zxr10SlotAvailStatus": zxr10SlotAvailStatus,
       "zxr10SlotOperStatus": zxr10SlotOperStatus,
       "zxr10SlotMasterStatus": zxr10SlotMasterStatus,
       "zxr10ReceiveTick": zxr10ReceiveTick,
       "zxr10SlotTemperature": zxr10SlotTemperature,
       "zxr10SubcardMax": zxr10SubcardMax,
       "zxr10BootVersion": zxr10BootVersion,
       "zxr10PCBVersion": zxr10PCBVersion,
       "zxr10FPGAVer": zxr10FPGAVer,
       "zxr10McodeVer": zxr10McodeVer,
       "zxr10MasterQDRSRAMSize": zxr10MasterQDRSRAMSize,
       "zxr10SlaveQDRSRAMSize": zxr10SlaveQDRSRAMSize,
       "zxr10camSize": zxr10camSize,
       "zxr10BoardSilkLabel": zxr10BoardSilkLabel,
       "zxr10portTable": zxr10portTable,
       "zxr10portEntry": zxr10portEntry,
       "zxr10PortIfIndex": zxr10PortIfIndex,
       "zxr10PortNo": zxr10PortNo,
       "zxr10PortType": zxr10PortType,
       "zxr10PortWorkingType": zxr10PortWorkingType,
       "zxr10PortMTU": zxr10PortMTU,
       "zxr10PortSpeed": zxr10PortSpeed,
       "zxr10PortAvailStatus": zxr10PortAvailStatus,
       "zxr10PortOperStatus": zxr10PortOperStatus,
       "zxr10PortProtocolStatus": zxr10PortProtocolStatus,
       "zxr10PortProperty": zxr10PortProperty,
       "zxr10PortDesc": zxr10PortDesc,
       "zxr10-statistics": zxr10_statistics,
       "zxr10SystemUnitTable": zxr10SystemUnitTable,
       "zxr10SystemUnitEntry": zxr10SystemUnitEntry,
       "zxr10SystemUnitIndex": zxr10SystemUnitIndex,
       "zxr10SystemUnitRunStatus": zxr10SystemUnitRunStatus,
       "zxr10SystemMemSize": zxr10SystemMemSize,
       "zxr10SystemMemUsed": zxr10SystemMemUsed,
       "zxr10SystemCpuUtility2m": zxr10SystemCpuUtility2m,
       "zxr10SystemCpuUtility5s": zxr10SystemCpuUtility5s,
       "zxr10SystemCpuUtility30s": zxr10SystemCpuUtility30s,
       "zxr10SystemPeakCpuUtility": zxr10SystemPeakCpuUtility,
       "zxr10SystemUnitUpTime": zxr10SystemUnitUpTime,
       "zxr10SystemUnitPidNum": zxr10SystemUnitPidNum,
       "zxr10SystemCpuUtility1m": zxr10SystemCpuUtility1m,
       "zxr10SystemCpuUtility5m": zxr10SystemCpuUtility5m,
       "zxr10UnitPidTable": zxr10UnitPidTable,
       "zxr10UnitPidEntry": zxr10UnitPidEntry,
       "zxr10UnitPidNo": zxr10UnitPidNo,
       "zxr10UnitPidUsedStatus": zxr10UnitPidUsedStatus,
       "zxr10UnitPidName": zxr10UnitPidName,
       "zxr10UnitPidPrio": zxr10UnitPidPrio,
       "zxr10UnitPidStackSize": zxr10UnitPidStackSize,
       "zxr10UnitPidCalledTimes": zxr10UnitPidCalledTimes,
       "zxr10UnitPidCpuOccupanTime": zxr10UnitPidCpuOccupanTime,
       "zxr10UnitPidInterruptTimes": zxr10UnitPidInterruptTimes,
       "zxr10UnitPidAsyQuenMsgMax": zxr10UnitPidAsyQuenMsgMax,
       "zxr10UnitPidAsyQuenUsed": zxr10UnitPidAsyQuenUsed,
       "zxr10UnitPidAsyQuenBlocked": zxr10UnitPidAsyQuenBlocked,
       "zxr10UnitPidAsyQuenSendTimeouts": zxr10UnitPidAsyQuenSendTimeouts,
       "zxr10UnitPidAsyQuenRecTimeouts": zxr10UnitPidAsyQuenRecTimeouts,
       "zxr10UnitPidSynQuenMsgMax": zxr10UnitPidSynQuenMsgMax,
       "zxr10UnitPidSynQuenUsed": zxr10UnitPidSynQuenUsed,
       "zxr10UnitPidSynQuenBlocked": zxr10UnitPidSynQuenBlocked,
       "zxr10UnitPidSynQuenSendTimeouts": zxr10UnitPidSynQuenSendTimeouts,
       "zxr10UnitPidSynQuenRecTimeouts": zxr10UnitPidSynQuenRecTimeouts,
       "zxr10UnitPidTimerNamedUsed": zxr10UnitPidTimerNamedUsed,
       "zxr10UnitPidTimerUnnamedUsed": zxr10UnitPidTimerUnnamedUsed,
       "zxr10UnitCommStatTable": zxr10UnitCommStatTable,
       "zxr10UnitCommStatEntry": zxr10UnitCommStatEntry,
       "zxr10UnitNo": zxr10UnitNo,
       "zxr10UnitsndMsgs": zxr10UnitsndMsgs,
       "zxr10UnitsndBytes": zxr10UnitsndBytes,
       "zxr10UnitsndByteGigas": zxr10UnitsndByteGigas,
       "zxr10UnitrcvMsgs": zxr10UnitrcvMsgs,
       "zxr10UnitrcvBytes": zxr10UnitrcvBytes,
       "zxr10UnitrcvByteGigas": zxr10UnitrcvByteGigas,
       "zxr10-alarm": zxr10_alarm,
       "zxr10HardwareEnvironAlarmTable": zxr10HardwareEnvironAlarmTable,
       "zxr10HardwareEnvironAlarmEntry": zxr10HardwareEnvironAlarmEntry,
       "zxr10HardwareEnvironAlarmRackNo": zxr10HardwareEnvironAlarmRackNo,
       "zxr10HardwareEnvironAlarmShelfNo": zxr10HardwareEnvironAlarmShelfNo,
       "zxr10HardwareEnvironAlarmSlotNo": zxr10HardwareEnvironAlarmSlotNo,
       "zxr10HardwareEnvironAlarmCode": zxr10HardwareEnvironAlarmCode,
       "zxr10HardwareEnvironAlarmLevel": zxr10HardwareEnvironAlarmLevel,
       "zxr10HardwareEnvironAlarmTime": zxr10HardwareEnvironAlarmTime,
       "zxr10HardwareEnvironAlarmStatus": zxr10HardwareEnvironAlarmStatus,
       "zxr10HardwareEnvironAlarmType": zxr10HardwareEnvironAlarmType,
       "zxr10HardwareEnvironAlarmDescrip": zxr10HardwareEnvironAlarmDescrip,
       "zxr10HardwareBoardAlarmTable": zxr10HardwareBoardAlarmTable,
       "zxr10HardwareBoardAlarmEntry": zxr10HardwareBoardAlarmEntry,
       "zxr10HardwareBoardAlarmRackNo": zxr10HardwareBoardAlarmRackNo,
       "zxr10HardwareBoardAlarmShelfNo": zxr10HardwareBoardAlarmShelfNo,
       "zxr10HardwareBoardAlarmSlotNo": zxr10HardwareBoardAlarmSlotNo,
       "zxr10HardwareBoardAlarmCode": zxr10HardwareBoardAlarmCode,
       "zxr10HardwareBoardAlarmLevel": zxr10HardwareBoardAlarmLevel,
       "zxr10HardwareBoardAlarmTime": zxr10HardwareBoardAlarmTime,
       "zxr10HardwareBoardAlarmStatus": zxr10HardwareBoardAlarmStatus,
       "zxr10HardwareBoardAlarmType": zxr10HardwareBoardAlarmType,
       "zxr10HardwareBoardAlarmDescrip": zxr10HardwareBoardAlarmDescrip,
       "zxr10HardwarePortAlarmTable": zxr10HardwarePortAlarmTable,
       "zxr10HardwarePortAlarmEntry": zxr10HardwarePortAlarmEntry,
       "zxr10HardwarePortAlarmRackNo": zxr10HardwarePortAlarmRackNo,
       "zxr10HardwarePortAlarmShelfNo": zxr10HardwarePortAlarmShelfNo,
       "zxr10HardwarePortAlarmSlotNo": zxr10HardwarePortAlarmSlotNo,
       "zxr10HardwarePortAlarmPortNo": zxr10HardwarePortAlarmPortNo,
       "zxr10HardwarePortAlarmCode": zxr10HardwarePortAlarmCode,
       "zxr10HardwarePortAlarmLevel": zxr10HardwarePortAlarmLevel,
       "zxr10HardwarePortAlarmTime": zxr10HardwarePortAlarmTime,
       "zxr10HardwarePortAlarmStatus": zxr10HardwarePortAlarmStatus,
       "zxr10HardwarePortAlarmType": zxr10HardwarePortAlarmType,
       "zxr10HardwarePortAlarmDescrip": zxr10HardwarePortAlarmDescrip,
       "zxr10SoftProtocolAlarmTable": zxr10SoftProtocolAlarmTable,
       "zxr10SoftProtocolAlarmEntry": zxr10SoftProtocolAlarmEntry,
       "zxr10SoftProtocolAlarmSaveCode": zxr10SoftProtocolAlarmSaveCode,
       "zxr10SoftProtocolAlarmSaveLevel": zxr10SoftProtocolAlarmSaveLevel,
       "zxr10SoftProtocolAlarmSaveLasttime": zxr10SoftProtocolAlarmSaveLasttime,
       "zxr10SoftProtocolAlarmSaveTotaltimes": zxr10SoftProtocolAlarmSaveTotaltimes,
       "zxr10SoftProtocolAlarmSaveType": zxr10SoftProtocolAlarmSaveType,
       "zxr10StatisticsAlarmTable": zxr10StatisticsAlarmTable,
       "zxr10StatisticsAlarmEntry": zxr10StatisticsAlarmEntry,
       "zxr10StatisticsAlarmSaveCode": zxr10StatisticsAlarmSaveCode,
       "zxr10StatisticsAlarmSaveLevel": zxr10StatisticsAlarmSaveLevel,
       "zxr10StatisticsAlarmSaveLasttime": zxr10StatisticsAlarmSaveLasttime,
       "zxr10StatisticsAlarmSaveTotaltimes": zxr10StatisticsAlarmSaveTotaltimes,
       "zxr10StatisticsAlarmSaveType": zxr10StatisticsAlarmSaveType,
       "zxr10HardwareAlarmTrapTable": zxr10HardwareAlarmTrapTable,
       "zxr10HardwareAlarmTrapEntry": zxr10HardwareAlarmTrapEntry,
       "zxr10HardwareAlarmRackNo": zxr10HardwareAlarmRackNo,
       "zxr10HardwareAlarmShelfNo": zxr10HardwareAlarmShelfNo,
       "zxr10HardwareAlarmSlotNo": zxr10HardwareAlarmSlotNo,
       "zxr10HardwareAlarmPortNo": zxr10HardwareAlarmPortNo,
       "zxr10HardwareAlarmCode": zxr10HardwareAlarmCode,
       "zxr10HardwareAlarmLevel": zxr10HardwareAlarmLevel,
       "zxr10HardwareAlarmTime": zxr10HardwareAlarmTime,
       "zxr10HardwareAlarmStatus": zxr10HardwareAlarmStatus,
       "zxr10HardwareAlarmType": zxr10HardwareAlarmType,
       "zxr10HardwareAlarmVariableValue": zxr10HardwareAlarmVariableValue,
       "zxr10HardwareAlarmValueRisingThreshold": zxr10HardwareAlarmValueRisingThreshold,
       "zxr10HardwareAlarmValueFallingThreshold": zxr10HardwareAlarmValueFallingThreshold,
       "zxr10HardwareAlarmDescrip": zxr10HardwareAlarmDescrip,
       "zxr10SoftProtocolAlarmTrapTable": zxr10SoftProtocolAlarmTrapTable,
       "zxr10SoftProtocolAlarmTrapEntry": zxr10SoftProtocolAlarmTrapEntry,
       "zxr10SoftProtocolAlarmRackNo": zxr10SoftProtocolAlarmRackNo,
       "zxr10SoftProtocolAlarmShelfNo": zxr10SoftProtocolAlarmShelfNo,
       "zxr10SoftProtocolAlarmSlotNo": zxr10SoftProtocolAlarmSlotNo,
       "zxr10SoftProtocolAlarmCode": zxr10SoftProtocolAlarmCode,
       "zxr10SoftProtocolAlarmLevel": zxr10SoftProtocolAlarmLevel,
       "zxr10SoftProtocolAlarmTime": zxr10SoftProtocolAlarmTime,
       "zxr10SoftProtocolAlarmStatus": zxr10SoftProtocolAlarmStatus,
       "zxr10SoftProtocolAlarmType": zxr10SoftProtocolAlarmType,
       "zxr10SoftProtocolAlarmDescrip": zxr10SoftProtocolAlarmDescrip,
       "zxr10StatisticsAlarmTrapTable": zxr10StatisticsAlarmTrapTable,
       "zxr10StatisticsAlarmTrapEntry": zxr10StatisticsAlarmTrapEntry,
       "zxr10StatisticsAlarmRackNo": zxr10StatisticsAlarmRackNo,
       "zxr10StatisticsAlarmShelfNo": zxr10StatisticsAlarmShelfNo,
       "zxr10StatisticsAlarmSlotNo": zxr10StatisticsAlarmSlotNo,
       "zxr10StatisticsAlarmPortNo": zxr10StatisticsAlarmPortNo,
       "zxr10StatisticsAlarmCode": zxr10StatisticsAlarmCode,
       "zxr10StatisticsAlarmLevel": zxr10StatisticsAlarmLevel,
       "zxr10StatisticsAlarmTime": zxr10StatisticsAlarmTime,
       "zxr10StatisticsAlarmStatus": zxr10StatisticsAlarmStatus,
       "zxr10StatisticsAlarmType": zxr10StatisticsAlarmType,
       "zxr10StatisticsAlarmVariableValue": zxr10StatisticsAlarmVariableValue,
       "zxr10StatisticsAlarmValueRisingThreshold": zxr10StatisticsAlarmValueRisingThreshold,
       "zxr10StatisticsAlarmValueFallingThreshold": zxr10StatisticsAlarmValueFallingThreshold,
       "zxr10StatisticsAlarmDescrip": zxr10StatisticsAlarmDescrip,
       "zxr10AlarmTrap": zxr10AlarmTrap,
       "zxr10HardwareAlarmTrap": zxr10HardwareAlarmTrap,
       "zxr10SoftProtocolAlarmTrap": zxr10SoftProtocolAlarmTrap,
       "zxr10StatisticsAlarmTrap": zxr10StatisticsAlarmTrap,
       "zxr10-objectID": zxr10_objectID,
       "zxr10RouterT128SysID": zxr10RouterT128SysID,
       "zxr10RouterT64SysID": zxr10RouterT64SysID,
       "zxr10SwitchT32SysID": zxr10SwitchT32SysID,
       "zxr10RouterGAR-2608SysID": zxr10RouterGAR_2608SysID,
       "zxr10RouterGER8SysID": zxr10RouterGER8SysID,
       "zxr10RouterGAR-2604SysID": zxr10RouterGAR_2604SysID,
       "zxr10SwitchT160GSysID": zxr10SwitchT160GSysID,
       "zxr10RouterGAR-3608SysID": zxr10RouterGAR_3608SysID,
       "zxr10RouterGAR-7208SysID": zxr10RouterGAR_7208SysID,
       "zxr10SwitchT64GSysID": zxr10SwitchT64GSysID,
       "zxr10Switch3206SysID": zxr10Switch3206SysID,
       "zxr10Switch3906SysID": zxr10Switch3906SysID,
       "zxr10Switch3228SysID": zxr10Switch3228SysID,
       "zxr10Switch3928SysID": zxr10Switch3928SysID,
       "zxr10Switch3252SysID": zxr10Switch3252SysID,
       "zxr10Switch3952SysID": zxr10Switch3952SysID,
       "zxr10Switch5224SysID": zxr10Switch5224SysID,
       "zxr10Switch5228SysID": zxr10Switch5228SysID,
       "zxr10Switch5228FSysID": zxr10Switch5228FSysID,
       "zxr10Switch5928SysID": zxr10Switch5928SysID,
       "zxr10Switch5928FSysID": zxr10Switch5928FSysID,
       "zxr10Switch5252SysID": zxr10Switch5252SysID,
       "zxr10Switch5952SysID": zxr10Switch5952SysID,
       "zxr10Switch3226SysID": zxr10Switch3226SysID,
       "zxr10SwitchT40GSysID": zxr10SwitchT40GSysID,
       "zxr10RouterT1200SysID": zxr10RouterT1200SysID,
       "zxr10RouterT600SysID": zxr10RouterT600SysID,
       "zxr10RouterGER2SysID": zxr10RouterGER2SysID,
       "zxr10RouterGER4SysID": zxr10RouterGER4SysID,
       "zxr10Switch3226FISysID": zxr10Switch3226FISysID,
       "zxr10Switch3928ASysID": zxr10Switch3928ASysID,
       "zxr10Switch3928AFISysID": zxr10Switch3928AFISysID,
       "zxr10Switch3952ASysID": zxr10Switch3952ASysID,
       "zxr10Switch3228A-EISysID": zxr10Switch3228A_EISysID,
       "zxr10Switch3228ASysID": zxr10Switch3228ASysID,
       "zxr10Switch3228A-FISysID": zxr10Switch3228A_FISysID,
       "zxr10Switch3252ASysID": zxr10Switch3252ASysID,
       "zxr10Switch5228ASysID": zxr10Switch5228ASysID,
       "zxr10Switch5252ASysID": zxr10Switch5252ASysID,
       "zxr10Switch5928ESysID": zxr10Switch5928ESysID,
       "zxr10Switch5928E-FISysID": zxr10Switch5928E_FISysID,
       "zxr10Switch3952ESysID": zxr10Switch3952ESysID,
       "zxr10Switch5952ESysID": zxr10Switch5952ESysID,
       "zxr10RouterR10-1822-ACSysID": zxr10RouterR10_1822_ACSysID,
       "zxr10RouterR10-1822-DCSysID": zxr10RouterR10_1822_DCSysID,
       "zxr10RouterR10-1821-ACSysID": zxr10RouterR10_1821_ACSysID,
       "zxr10RouterR10-1821-DCSysID": zxr10RouterR10_1821_DCSysID,
       "zxr10RouterR10-1812-ACSysID": zxr10RouterR10_1812_ACSysID,
       "zxr10RouterR10-1812-DCSysID": zxr10RouterR10_1812_DCSysID,
       "zxr10RouterR10-1811-ACSysID": zxr10RouterR10_1811_ACSysID,
       "zxr10RouterR10-1811-DCSysID": zxr10RouterR10_1811_DCSysID,
       "zxr10RouterR10-1822E-ACSysID": zxr10RouterR10_1822E_ACSysID,
       "zxr10RouterR10-1822E-DCSysID": zxr10RouterR10_1822E_DCSysID,
       "zxr10RouterR10-1821E-ACSysID": zxr10RouterR10_1821E_ACSysID,
       "zxr10RouterR10-1821E-DCSysID": zxr10RouterR10_1821E_DCSysID,
       "zxr10RouterR10-1812E-ACSysID": zxr10RouterR10_1812E_ACSysID,
       "zxr10RouterR10-1812E-DCSysID": zxr10RouterR10_1812E_DCSysID,
       "zxr10RouterR10-1811E-ACSysID": zxr10RouterR10_1811E_ACSysID,
       "zxr10RouterR10-1811E-DCSysID": zxr10RouterR10_1811E_DCSysID,
       "zxr10RouterR10-3881-ACSysID": zxr10RouterR10_3881_ACSysID,
       "zxr10RouterR10-3882-ACSysID": zxr10RouterR10_3882_ACSysID,
       "zxr10RouterR10-3883-ACSysID": zxr10RouterR10_3883_ACSysID,
       "zxr10RouterR10-3884-ACSysID": zxr10RouterR10_3884_ACSysID,
       "zxr10RouterR10-3881-DCSysID": zxr10RouterR10_3881_DCSysID,
       "zxr10RouterR10-3882-DCSysID": zxr10RouterR10_3882_DCSysID,
       "zxr10RouterR10-3883-DCSysID": zxr10RouterR10_3883_DCSysID,
       "zxr10RouterR10-3884-DCSysID": zxr10RouterR10_3884_DCSysID,
       "zxr10RouterR10-3841-ACSysID": zxr10RouterR10_3841_ACSysID,
       "zxr10RouterR10-3842-ACSysID": zxr10RouterR10_3842_ACSysID,
       "zxr10RouterR10-3843-ACSysID": zxr10RouterR10_3843_ACSysID,
       "zxr10RouterR10-3844-ACSysID": zxr10RouterR10_3844_ACSysID,
       "zxr10RouterR10-3841-DCSysID": zxr10RouterR10_3841_DCSysID,
       "zxr10RouterR10-3842-DCSysID": zxr10RouterR10_3842_DCSysID,
       "zxr10RouterR10-3843-DCSysID": zxr10RouterR10_3843_DCSysID,
       "zxr10RouterR10-3844-DCSysID": zxr10RouterR10_3844_DCSysID,
       "zxr10RouterR10-3821-ACSysID": zxr10RouterR10_3821_ACSysID,
       "zxr10RouterR10-3822-ACSysID": zxr10RouterR10_3822_ACSysID,
       "zxr10RouterR10-3823-ACSysID": zxr10RouterR10_3823_ACSysID,
       "zxr10RouterR10-3824-ACSysID": zxr10RouterR10_3824_ACSysID,
       "zxr10RouterR10-3821-DCSysID": zxr10RouterR10_3821_DCSysID,
       "zxr10RouterR10-3822-DCSysID": zxr10RouterR10_3822_DCSysID,
       "zxr10RouterR10-3823-DCSysID": zxr10RouterR10_3823_DCSysID,
       "zxr10RouterR10-3824-DCSysID": zxr10RouterR10_3824_DCSysID,
       "zxr10RouterR10-2841-ACSysID": zxr10RouterR10_2841_ACSysID,
       "zxr10RouterR10-2842-ACSysID": zxr10RouterR10_2842_ACSysID,
       "zxr10RouterR10-2843-ACSysID": zxr10RouterR10_2843_ACSysID,
       "zxr10RouterR10-2844-ACSysID": zxr10RouterR10_2844_ACSysID,
       "zxr10RouterR10-2841-DCSysID": zxr10RouterR10_2841_DCSysID,
       "zxr10RouterR10-2842-DCSysID": zxr10RouterR10_2842_DCSysID,
       "zxr10RouterR10-2843-DCSysID": zxr10RouterR10_2843_DCSysID,
       "zxr10RouterR10-2844-DCSysID": zxr10RouterR10_2844_DCSysID,
       "zxr10RouterR10-2881-ACSysID": zxr10RouterR10_2881_ACSysID,
       "zxr10RouterR10-2882-ACSysID": zxr10RouterR10_2882_ACSysID,
       "zxr10RouterR10-2883-ACSysID": zxr10RouterR10_2883_ACSysID,
       "zxr10RouterR10-2884-ACSysID": zxr10RouterR10_2884_ACSysID,
       "zxr10RouterR10-2881-DCSysID": zxr10RouterR10_2881_DCSysID,
       "zxr10RouterR10-2882-DCSysID": zxr10RouterR10_2882_DCSysID,
       "zxr10RouterR10-2883-DCSysID": zxr10RouterR10_2883_DCSysID,
       "zxr10RouterR10-2884-DCSysID": zxr10RouterR10_2884_DCSysID,
       "zxr10RouterR10-2821-ACSysID": zxr10RouterR10_2821_ACSysID,
       "zxr10RouterR10-2822-ACSysID": zxr10RouterR10_2822_ACSysID,
       "zxr10RouterR10-2823-ACSysID": zxr10RouterR10_2823_ACSysID,
       "zxr10RouterR10-2824-ACSysID": zxr10RouterR10_2824_ACSysID,
       "zxr10RouterR10-2821-DCSysID": zxr10RouterR10_2821_DCSysID,
       "zxr10RouterR10-2822-DCSysID": zxr10RouterR10_2822_DCSysID,
       "zxr10RouterR10-2823-DCSysID": zxr10RouterR10_2823_DCSysID,
       "zxr10RouterR10-2824-DCSysID": zxr10RouterR10_2824_DCSysID,
       "zxr10RouterR10-1841-ACSysID": zxr10RouterR10_1841_ACSysID,
       "zxr10RouterR10-1842-ACSysID": zxr10RouterR10_1842_ACSysID,
       "zxr10RouterR10-1843-ACSysID": zxr10RouterR10_1843_ACSysID,
       "zxr10RouterR10-1844-ACSysID": zxr10RouterR10_1844_ACSysID,
       "zxr10RouterR10-1841-DCSysID": zxr10RouterR10_1841_DCSysID,
       "zxr10RouterR10-1842-DCSysID": zxr10RouterR10_1842_DCSysID,
       "zxr10RouterR10-1843-DCSysID": zxr10RouterR10_1843_DCSysID,
       "zxr10RouterR10-1844-DCSysID": zxr10RouterR10_1844_DCSysID,
       "zxr10Switch-6907SysID": zxr10Switch_6907SysID,
       "zxr10Switch-T240GSysID": zxr10Switch_T240GSysID,
       "zxr10Switch-6902SysID": zxr10Switch_6902SysID,
       "zxr10Switch-6905SysID": zxr10Switch_6905SysID,
       "zxr10Switch-6908SysID": zxr10Switch_6908SysID,
       "zxr10Switch-8902SysID": zxr10Switch_8902SysID,
       "zxr10Switch-8905SysID": zxr10Switch_8905SysID,
       "zxr10Switch-8908SysID": zxr10Switch_8908SysID,
       "zxr10Switch-8912SysID": zxr10Switch_8912SysID,
       "zxctn-6100SysID": zxctn_6100SysID,
       "zxr10Switch5928-PSSysID": zxr10Switch5928_PSSysID,
       "zxr10Switch3928A-PSSysID": zxr10Switch3928A_PSSysID,
       "zxr10Switch3928ESysID": zxr10Switch3928ESysID,
       "zxr10Switch3928E-FISysID": zxr10Switch3928E_FISysID,
       "zxr10UAS10600SysID": zxr10UAS10600SysID}
)
