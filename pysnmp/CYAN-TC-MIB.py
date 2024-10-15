# SNMP MIB module (CYAN-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-TC-MIB
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

(cyanMibModules,) = mibBuilder.importSymbols(
    "CYAN-MIB",
    "cyanMibModules")

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

cyanTCModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 1)
)
cyanTCModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CyanActvStdbyTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("stdby", 0))
    )



class CyanAdminStateTc(Integer32, TextualConvention):
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
        *(("adminautoinservice", 2),
          ("adminlockeddis", 4),
          ("adminlockedmat", 3),
          ("adminunlocked", 1))
    )



class CyanAugStructureTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("au464c", 8),
          ("aug16", 7),
          ("notconfigured", 0),
          ("transparent", 9))
    )



class CyanChannelIdTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protect", 0),
          ("working", 1))
    )



class CyanEnDisabledTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class CyanFecModeTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fecEnhanced", 3),
          ("fecReedSolomon", 1))
    )



class CyanFppSubTypeTc(Integer32, TextualConvention):
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
        *(("nnimpls", 4),
          ("nnipbb", 3),
          ("unconfigured", 0),
          ("unitype1", 1),
          ("unitype2", 2))
    )



class CyanFppTypeTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("uni", 1))
    )



class CyanGfpUpiTc(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12,
              13,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("dvbAsiFrame", 18),
          ("dvbAsiTransparent", 9),
          ("esconTransparent", 5),
          ("ethernet64b66bFrame", 19),
          ("ethernet64b66bOrderedsetFrame", 20),
          ("ethernetframe", 1),
          ("fc1200Transparent", 21),
          ("fiberchannelAsyncTransparent", 12),
          ("fiberchannelBbwFrame", 11),
          ("fiberchannelTransparent", 3),
          ("ficonTransparent", 4),
          ("gbeTransparent", 6),
          ("ieee80217RprFrame", 10),
          ("ipv4Frame", 16),
          ("ipv6Frame", 17),
          ("maposFrame", 8),
          ("mplsFrame", 13),
          ("osiFrame", 15),
          ("pppFrame", 2))
    )



class CyanLEDTc(Integer32, TextualConvention):
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
        *(("amber", 6),
          ("amberBlinking", 5),
          ("amberBlinkingSlow", 11),
          ("blue", 8),
          ("blueBlinking", 7),
          ("blueBlinkingSlow", 12),
          ("green", 4),
          ("greenBlinking", 3),
          ("greenBlinkingSlow", 10),
          ("off", 0),
          ("red", 2),
          ("redBlinking", 1),
          ("redBlinkingSlow", 9))
    )



class CyanLayerRateTc(Bits, TextualConvention):
    status = "current"


class CyanLoopbackControlTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("facilitylpbk", 1),
          ("terminallpbk", 3))
    )



class CyanNationalizationTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 2),
          ("itu", 1))
    )



class CyanNimTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("monitoring", 1),
          ("terminating", 0))
    )



class CyanNoYesTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )



class CyanOffOnTc(Integer32, TextualConvention):
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
        *(("off", 0),
          ("on", 1),
          ("unknown", 2))
    )



class CyanOpStateQualTc(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("anr", 7),
          ("anrst", 9),
          ("au", 1),
          ("auma", 3),
          ("aurst", 4),
          ("ma", 2),
          ("maanr", 5),
          ("nr", 6),
          ("rst", 8))
    )



class CyanOpStateTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oos", 2))
    )



class CyanOpuPayloadTypeTc(Integer32, TextualConvention):
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
              258)
        )
    )
    namedValues = NamedValues(
        *(("asynchcbrmap", 2),
          ("atmmap", 4),
          ("bitstreamwithtiming", 16),
          ("bitstreamwotiming", 17),
          ("bittransparent", 143),
          ("dvbAsiIntoOpu0", 27),
          ("experimental", 0),
          ("expmap", 1),
          ("fc100mapodu0", 12),
          ("fc1200mapodu2e", 8),
          ("fc1600mapoduflex", 28),
          ("fc200mapodu1", 13),
          ("fc400mapoduflex", 14),
          ("fc800mapodu2", 142),
          ("fc800mapoduflex", 15),
          ("gfpmap", 5),
          ("gfpmapextendedopu2", 9),
          ("ibDdrIntoOduflex", 19),
          ("ibQdrIntoOduflex", 20),
          ("ibSdrIntoOduflex", 18),
          ("nim", 258),
          ("notavailableais", 255),
          ("notavailablefault", 256),
          ("notavailablelck", 85),
          ("notavailableoci", 102),
          ("nulltest", 253),
          ("odumultiplex", 32),
          ("odumultiplexgmp", 33),
          ("opu01000bxmap", 7),
          ("prbstest", 254),
          ("reserved80", 128),
          ("reserved81", 129),
          ("reserved82", 130),
          ("reserved83", 131),
          ("reserved84", 132),
          ("reserved85", 133),
          ("reserved86", 134),
          ("reserved87", 135),
          ("reserved88", 136),
          ("reserved89", 137),
          ("reserved8a", 138),
          ("reserved8b", 139),
          ("reserved8c", 140),
          ("reserved8d", 141),
          ("sbconEsconIntoOpu0", 26),
          ("sdi1g4851g001IntoOpu1", 22),
          ("sdi1g485IntoOpu1", 23),
          ("sdi2g9701g001IntoOpuflex", 24),
          ("sdi2g970IntoOpuflex", 25),
          ("sdiIntoOpu0", 21),
          ("stm1mapodu0", 10),
          ("stm4mapodu0", 11),
          ("synchcbrmap", 3),
          ("undef1d", 29),
          ("undef1e", 30),
          ("undef1f", 31),
          ("undef22", 34),
          ("undef23", 35),
          ("undef24", 36),
          ("undef25", 37),
          ("undef26", 38),
          ("undef27", 39),
          ("undef28", 40),
          ("undef29", 41),
          ("undef2a", 42),
          ("undef2b", 43),
          ("undef2c", 44),
          ("undef2d", 45),
          ("undef2e", 46),
          ("undef2f", 47),
          ("undef30", 48),
          ("undef31", 49),
          ("undef32", 50),
          ("undef33", 51),
          ("undef34", 52),
          ("undef35", 53),
          ("undef36", 54),
          ("undef37", 55),
          ("undef38", 56),
          ("undef39", 57),
          ("undef3a", 58),
          ("undef3b", 59),
          ("undef3c", 60),
          ("undef3d", 61),
          ("undef3e", 62),
          ("undef3f", 63),
          ("undef40", 64),
          ("undef41", 65),
          ("undef42", 66),
          ("undef43", 67),
          ("undef44", 68),
          ("undef45", 69),
          ("undef46", 70),
          ("undef47", 71),
          ("undef48", 72),
          ("undef49", 73),
          ("undef4a", 74),
          ("undef4b", 75),
          ("undef4c", 76),
          ("undef4d", 77),
          ("undef4e", 78),
          ("undef4f", 79),
          ("undef50", 80),
          ("undef51", 81),
          ("undef52", 82),
          ("undef53", 83),
          ("undef54", 84),
          ("undef56", 86),
          ("undef57", 87),
          ("undef58", 88),
          ("undef59", 89),
          ("undef5a", 90),
          ("undef5b", 91),
          ("undef5c", 92),
          ("undef5d", 93),
          ("undef5e", 94),
          ("undef5f", 95),
          ("undef60", 96),
          ("undef61", 97),
          ("undef62", 98),
          ("undef63", 99),
          ("undef64", 100),
          ("undef65", 101),
          ("undef67", 103),
          ("undef68", 104),
          ("undef69", 105),
          ("undef6a", 106),
          ("undef6b", 107),
          ("undef6c", 108),
          ("undef6d", 109),
          ("undef6e", 110),
          ("undef6f", 111),
          ("undef70", 112),
          ("undef71", 113),
          ("undef72", 114),
          ("undef73", 115),
          ("undef74", 116),
          ("undef75", 117),
          ("undef76", 118),
          ("undef77", 119),
          ("undef78", 120),
          ("undef79", 121),
          ("undef7a", 122),
          ("undef7b", 123),
          ("undef7c", 124),
          ("undef7d", 125),
          ("undef7e", 126),
          ("undef7f", 127),
          ("undef90", 144),
          ("undef91", 145),
          ("undef92", 146),
          ("undef93", 147),
          ("undef94", 148),
          ("undef95", 149),
          ("undef96", 150),
          ("undef97", 151),
          ("undef98", 152),
          ("undef99", 153),
          ("undef9a", 154),
          ("undef9b", 155),
          ("undef9c", 156),
          ("undef9d", 157),
          ("undef9e", 158),
          ("undef9f", 159),
          ("undefA0", 160),
          ("undefA1", 161),
          ("undefA2", 162),
          ("undefA3", 163),
          ("undefA4", 164),
          ("undefA5", 165),
          ("undefA6", 166),
          ("undefA7", 167),
          ("undefA8", 168),
          ("undefA9", 169),
          ("undefAa", 170),
          ("undefAb", 171),
          ("undefAc", 172),
          ("undefAd", 173),
          ("undefAe", 174),
          ("undefAf", 175),
          ("undefB0", 176),
          ("undefB1", 177),
          ("undefB2", 178),
          ("undefB3", 179),
          ("undefB4", 180),
          ("undefB5", 181),
          ("undefB6", 182),
          ("undefB7", 183),
          ("undefB8", 184),
          ("undefB9", 185),
          ("undefBa", 186),
          ("undefBb", 187),
          ("undefBc", 188),
          ("undefBd", 189),
          ("undefBe", 190),
          ("undefBf", 191),
          ("undefC0", 192),
          ("undefC1", 193),
          ("undefC2", 194),
          ("undefC3", 195),
          ("undefC4", 196),
          ("undefC5", 197),
          ("undefC6", 198),
          ("undefC7", 199),
          ("undefC8", 200),
          ("undefC9", 201),
          ("undefCa", 202),
          ("undefCb", 203),
          ("undefCc", 204),
          ("undefCd", 205),
          ("undefCe", 206),
          ("undefCf", 207),
          ("undefD0", 208),
          ("undefD1", 209),
          ("undefD2", 210),
          ("undefD3", 211),
          ("undefD4", 212),
          ("undefD5", 213),
          ("undefD6", 214),
          ("undefD7", 215),
          ("undefD8", 216),
          ("undefD9", 217),
          ("undefDa", 218),
          ("undefDb", 219),
          ("undefDc", 220),
          ("undefDd", 221),
          ("undefDe", 222),
          ("undefDf", 223),
          ("undefE0", 224),
          ("undefE1", 225),
          ("undefE2", 226),
          ("undefE3", 227),
          ("undefE4", 228),
          ("undefE5", 229),
          ("undefE6", 230),
          ("undefE7", 231),
          ("undefE8", 232),
          ("undefE9", 233),
          ("undefEa", 234),
          ("undefEb", 235),
          ("undefEc", 236),
          ("undefEd", 237),
          ("undefEe", 238),
          ("undefEf", 239),
          ("undefF0", 240),
          ("undefF1", 241),
          ("undefF2", 242),
          ("undefF3", 243),
          ("undefF4", 244),
          ("undefF5", 245),
          ("undefF6", 246),
          ("undefF7", 247),
          ("undefF8", 248),
          ("undefF9", 249),
          ("undefFa", 250),
          ("undefFb", 251),
          ("undefFc", 252),
          ("unstable", 257),
          ("vc", 6))
    )



class CyanPowerClassTc(Integer32, TextualConvention):
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
        *(("powerclass1", 0),
          ("powerclass2", 1),
          ("powerclass3", 2),
          ("powerclass4", 3))
    )



class CyanRelayTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rsClose", 1),
          ("rsOpen", 0))
    )



class CyanSdhSnSignalLabelTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              18,
              19,
              20,
              21,
              22,
              24,
              26,
              27,
              254)
        )
    )
    namedValues = NamedValues(
        *(("asyncDs3Mapping", 4),
          ("asyncDs4naMapping", 18),
          ("asyncFddiMapping", 21),
          ("atmMapping", 19),
          ("dqdbMapping", 20),
          ("equippedNonspecific", 1),
          ("gfp", 27),
          ("hdlcLapsMapping", 24),
          ("hdlcOverSonetMapping", 22),
          ("lockedVtMode", 3),
          ("o181TestSignalMapping", 254),
          ("unequipped", 0),
          ("vtStructured", 2),
          ("xgeWan", 26))
    )



class CyanSecServiceStateTc(Bits, TextualConvention):
    status = "current"


class CyanSsBitsTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ss00", 0),
          ("ss10", 2))
    )



class CyanTPConnectionStateTc(Integer32, TextualConvention):
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
        *(("tpcsBiConnected", 3),
          ("tpcsNotConnected", 4),
          ("tpcsSinkConnected", 2),
          ("tpcsSourceConnected", 1))
    )



class CyanTimezoneTc(Integer32, TextualConvention):
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
              27)
        )
    )
    namedValues = NamedValues(
        *(("americaAdak", 26),
          ("americaAnchorage", 22),
          ("americaBoise", 18),
          ("americaChicago", 11),
          ("americaDenver", 17),
          ("americaDetroit", 2),
          ("americaIndianaIndianapolis", 5),
          ("americaIndianaKnox", 7),
          ("americaIndianaMarengo", 9),
          ("americaIndianaPetersburg", 13),
          ("americaIndianaTellCity", 12),
          ("americaIndianaVevay", 10),
          ("americaIndianaVincennes", 6),
          ("americaIndianaWinamac", 8),
          ("americaJuneau", 23),
          ("americaKentuckyLouisville", 3),
          ("americaKentuckyMonticello", 4),
          ("americaLosAngeles", 21),
          ("americaMenominee", 14),
          ("americaNewYork", 1),
          ("americaNome", 25),
          ("americaNorthDakotaCenter", 15),
          ("americaNorthDakotaNewSalem", 16),
          ("americaPhoenix", 20),
          ("americaShiprock", 19),
          ("americaYakutat", 24),
          ("pacificHonolulu", 27),
          ("utc", 0))
    )



class CyanTxControlTc(Integer32, TextualConvention):
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
        *(("als", 2),
          ("off", 0),
          ("on", 1))
    )



class CyanWdmTypeTc(Integer32, TextualConvention):
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
        *(("cwdm", 1),
          ("dwdm100gGrid", 4),
          ("dwdm200gGrid", 3),
          ("dwdm25gGrid", 6),
          ("dwdm50gGrid", 5),
          ("lanwdm", 2),
          ("nonwdm", 0),
          ("otherwdm", 7))
    )



class CyanXGOSignalTypeTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(22,
              23,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("otu1e", 34),
          ("otu2", 32),
          ("otu2e", 33),
          ("tp10gelan", 22),
          ("tp10gewan", 23))
    )



class CyanXcvrConnectorCodeTc(Integer32, TextualConvention):
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
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("bncTnc", 4),
          ("copperpigtail", 33),
          ("fiberjack", 6),
          ("fibrechannelcoax", 5),
          ("fibrechannelstyle1Copper", 2),
          ("fibrechannelstyle2Copper", 3),
          ("hssdcIi", 32),
          ("lc", 7),
          ("mpoParalleloptic", 12),
          ("mtRj", 8),
          ("mu", 9),
          ("opticalpigtail", 11),
          ("rj45", 34),
          ("sc", 1),
          ("sg", 10),
          ("unknownorunspecified", 0))
    )



class CyanXcvrIdentifierTc(Integer32, TextualConvention):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("cfp", 14),
          ("cfp2", 17),
          ("cfp4", 18),
          ("cxp", 15),
          ("dwdmSfp", 11),
          ("gbic", 1),
          ("modulesolderedtomotherboard", 2),
          ("msa100glh", 16),
          ("qsfp", 12),
          ("qsfpPlus", 13),
          ("sfpOrSfpplus", 3),
          ("unknownUnspecified", 0),
          ("x2", 10),
          ("xbi300pin", 4),
          ("xenpak", 5),
          ("xff", 7),
          ("xfp", 6),
          ("xfpE", 8),
          ("xpak", 9))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-TC-MIB",
    **{"CyanActvStdbyTc": CyanActvStdbyTc,
       "CyanAdminStateTc": CyanAdminStateTc,
       "CyanAugStructureTc": CyanAugStructureTc,
       "CyanChannelIdTc": CyanChannelIdTc,
       "CyanEnDisabledTc": CyanEnDisabledTc,
       "CyanFecModeTc": CyanFecModeTc,
       "CyanFppSubTypeTc": CyanFppSubTypeTc,
       "CyanFppTypeTc": CyanFppTypeTc,
       "CyanGfpUpiTc": CyanGfpUpiTc,
       "CyanLEDTc": CyanLEDTc,
       "CyanLayerRateTc": CyanLayerRateTc,
       "CyanLoopbackControlTc": CyanLoopbackControlTc,
       "CyanNationalizationTc": CyanNationalizationTc,
       "CyanNimTc": CyanNimTc,
       "CyanNoYesTc": CyanNoYesTc,
       "CyanOffOnTc": CyanOffOnTc,
       "CyanOpStateQualTc": CyanOpStateQualTc,
       "CyanOpStateTc": CyanOpStateTc,
       "CyanOpuPayloadTypeTc": CyanOpuPayloadTypeTc,
       "CyanPowerClassTc": CyanPowerClassTc,
       "CyanRelayTc": CyanRelayTc,
       "CyanSdhSnSignalLabelTc": CyanSdhSnSignalLabelTc,
       "CyanSecServiceStateTc": CyanSecServiceStateTc,
       "CyanSsBitsTc": CyanSsBitsTc,
       "CyanTPConnectionStateTc": CyanTPConnectionStateTc,
       "CyanTimezoneTc": CyanTimezoneTc,
       "CyanTxControlTc": CyanTxControlTc,
       "CyanWdmTypeTc": CyanWdmTypeTc,
       "CyanXGOSignalTypeTc": CyanXGOSignalTypeTc,
       "CyanXcvrConnectorCodeTc": CyanXcvrConnectorCodeTc,
       "CyanXcvrIdentifierTc": CyanXcvrIdentifierTc,
       "cyanTCModule": cyanTCModule}
)
