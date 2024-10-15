# SNMP MIB module (BTI-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BTI-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:51 2024
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

(btiModules,) = mibBuilder.importSymbols(
    "BTI-MIB",
    "btiModules")

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

btiTcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 1, 2)
)
btiTcMib.setRevisions(
        ("2012-06-01 12:00",
         "2012-05-02 12:00",
         "2012-02-10 12:00",
         "2011-09-26 12:00",
         "2010-08-06 12:00",
         "2010-06-18 12:00",
         "2010-02-12 12:00",
         "2009-01-19 12:00",
         "2008-12-19 12:00",
         "2008-10-10 12:00",
         "2008-05-30 12:00",
         "2007-09-14 12:00",
         "2007-07-16 12:00",
         "2007-03-09 12:00",
         "2005-12-05 12:00",
         "2005-07-25 12:00",
         "2005-02-07 12:00",
         "2004-09-23 12:00",
         "2004-01-29 18:21",
         "2003-12-01 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FixedX10(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class FixedX100(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class FixedX1000(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-3"


class Unsigned64(Counter64, TextualConvention):
    status = "current"


class InitializeCmd(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("initialize", 2))
    )



class ShelfType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("expansion", 2),
          ("main", 1))
    )



class ShelfConfigType(Integer32, TextualConvention):
    status = "deprecated"
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
        *(("fiveSlot", 4),
          ("fiveSlotB", 8),
          ("fiveSlotC", 9),
          ("fourSlot", 3),
          ("fourSlotB", 6),
          ("fourSlotC", 7),
          ("sixSlot", 5),
          ("threeSlot", 2),
          ("twoSlot", 1),
          ("unknown", 10))
    )



class SlotType(Integer32, TextualConvention):
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
        *(("acPowerUnit", 4),
          ("coolingUnit", 3),
          ("regular", 1),
          ("shelfInterface", 2))
    )



class CpType(Integer32, TextualConvention):
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              20,
              25,
              29,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              41,
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
              72)
        )
    )
    namedValues = NamedValues(
        *(("c1adm", 29),
          ("c2adm", 63),
          ("c4md", 62),
          ("c8md", 25),
          ("c8md1", 59),
          ("c8md2", 60),
          ("ccm", 66),
          ("cdsc", 32),
          ("cs", 49),
          ("cu", 16),
          ("d1adm", 37),
          ("d2adm", 38),
          ("d32amd1", 54),
          ("d32amd2", 55),
          ("d32amd3", 56),
          ("d32amd4", 57),
          ("d32md1", 33),
          ("d32md2", 34),
          ("d32md3", 35),
          ("d32md4", 36),
          ("d40md", 71),
          ("d4adm", 39),
          ("d96md", 72),
          ("dcm", 70),
          ("dla", 68),
          ("esi", 15),
          ("fllr", 17),
          ("msi", 14),
          ("mxp", 61),
          ("nf", 46),
          ("oba", 2),
          ("oct", 43),
          ("ola", 3),
          ("olam", 4),
          ("opa", 5),
          ("osc", 20),
          ("pmt1", 12),
          ("pmt2", 13),
          ("pvx", 65),
          ("rob", 69),
          ("sba", 44),
          ("scp", 1),
          ("smf10", 51),
          ("smf15", 52),
          ("smf20", 53),
          ("smf30", 45),
          ("smf40", 18),
          ("smf5", 50),
          ("smf60", 6),
          ("smf80", 7),
          ("spa", 41),
          ("tpr", 64),
          ("wc200", 67),
          ("wm", 58),
          ("wr", 48),
          ("wt", 47))
    )



class OaType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("oba", 1),
          ("ola", 2),
          ("olam", 4),
          ("opa", 3),
          ("sba", 11),
          ("spa", 10))
    )



class XcvrType(Integer32, TextualConvention):
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
        *(("tpr", 4),
          ("wm", 3),
          ("wr", 2),
          ("wt", 1))
    )



class AmdType(Integer32, TextualConvention):
    status = "obsolete"
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
        *(("d32amd1", 1),
          ("d32amd2", 2),
          ("d32amd3", 3),
          ("d32amd4", 4))
    )



class AmdPortType(Integer32, TextualConvention):
    status = "obsolete"
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
              34)
        )
    )
    namedValues = NamedValues(
        *(("channel1", 2),
          ("channel10", 11),
          ("channel11", 12),
          ("channel12", 13),
          ("channel13", 14),
          ("channel14", 15),
          ("channel15", 16),
          ("channel16", 17),
          ("channel17", 18),
          ("channel18", 19),
          ("channel19", 20),
          ("channel2", 3),
          ("channel20", 21),
          ("channel21", 22),
          ("channel22", 23),
          ("channel23", 24),
          ("channel24", 25),
          ("channel25", 26),
          ("channel26", 27),
          ("channel27", 28),
          ("channel28", 29),
          ("channel29", 30),
          ("channel3", 4),
          ("channel30", 31),
          ("channel31", 32),
          ("channel32", 33),
          ("channel4", 5),
          ("channel5", 6),
          ("channel6", 7),
          ("channel7", 8),
          ("channel8", 9),
          ("channel9", 10),
          ("expansion", 34),
          ("line", 1))
    )



class OcnType(Integer32, TextualConvention):
    status = "current"
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
        *(("oc1", 1),
          ("oc12", 3),
          ("oc192", 5),
          ("oc3", 2),
          ("oc48", 4),
          ("oc768", 6))
    )



class StsnType(Integer32, TextualConvention):
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
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("sts1", 1),
          ("sts12c", 3),
          ("sts15c", 9),
          ("sts18c", 10),
          ("sts192c", 5),
          ("sts21c", 11),
          ("sts24c", 12),
          ("sts30c", 13),
          ("sts36c", 14),
          ("sts3c", 2),
          ("sts48c", 4),
          ("sts6c", 7),
          ("sts72c", 15),
          ("sts768c", 6),
          ("sts9c", 8))
    )



class StmnType(Integer32, TextualConvention):
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
        *(("stm1", 1),
          ("stm16", 3),
          ("stm246", 5),
          ("stm4", 2),
          ("stm64", 4))
    )



class VcnType(Integer32, TextualConvention):
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
        *(("vc10c", 14),
          ("vc11", 4),
          ("vc12", 5),
          ("vc12c", 10),
          ("vc16c", 11),
          ("vc2", 1),
          ("vc24c", 12),
          ("vc2c", 13),
          ("vc3", 2),
          ("vc3c", 15),
          ("vc4", 3),
          ("vc4c", 6),
          ("vc5c", 16),
          ("vc6c", 7),
          ("vc7c", 8),
          ("vc8c", 9))
    )



class FcType(Integer32, TextualConvention):
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
        *(("fc1g", 1),
          ("fc2g", 2),
          ("fc4g", 3))
    )



class OdunType(Integer32, TextualConvention):
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
        *(("odu1", 1),
          ("odu2", 2),
          ("odu3", 3),
          ("subOdu1", 4))
    )



class CondReportType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("condition", 1))
    )



class CondSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("critical-major", 8),
          ("default", 7),
          ("major", 3),
          ("minor", 2),
          ("notAlarmed", 5),
          ("notReported", 6))
    )



class CondServiceAffecting(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonServiceAffecting", 1),
          ("serviceAffecting", 2))
    )



class NotifCodeType(Integer32, TextualConvention):
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
              296)
        )
    )
    namedValues = NamedValues(
        *(("acpuFail", 1),
          ("acpuMiss", 2),
          ("acpuPlugin", 3),
          ("acpuUnk", 4),
          ("acpuUnplug", 5),
          ("actLpbkF", 6),
          ("actLpbkT", 7),
          ("airCompr", 216),
          ("airCond", 217),
          ("airDryr", 218),
          ("ais", 8),
          ("aisL", 9),
          ("aisO", 277),
          ("aisP", 10),
          ("ampCond", 11),
          ("ampTrans", 12),
          ("applDbRstPass", 13),
          ("apsd", 274),
          ("authenFailed", 207),
          ("autoProvFail", 14),
          ("batDschrd", 219),
          ("battery", 220),
          ("bdi", 209),
          ("bwMism", 15),
          ("cMism", 16),
          ("chnDfc", 281),
          ("clFan", 221),
          ("cmmtUpgrdPass", 17),
          ("cnxMea", 284),
          ("cnxVldTmout", 285),
          ("connMea", 18),
          ("contBus", 19),
          ("contCom", 20),
          ("contComE", 268),
          ("contComS", 267),
          ("cpMajor", 222),
          ("cpMinor", 223),
          ("cuFail", 21),
          ("cuFail1uMj", 22),
          ("cuFail1uMn", 23),
          ("cuFeedFailMj", 24),
          ("cuFeedFailMn", 25),
          ("cuMiss", 26),
          ("cuPlugin", 27),
          ("cuUnk", 28),
          ("cuUnplug", 29),
          ("dbBkupFail", 30),
          ("dbBkupPass", 31),
          ("dbBkupProg", 32),
          ("dbDltProg", 33),
          ("dbLoadFail", 34),
          ("dbLoadPass", 35),
          ("dbRecvryFail", 36),
          ("dbRstProg", 37),
          ("delayAvg", 260),
          ("delayMax", 259),
          ("delayVarAvg", 262),
          ("delayVarMax", 261),
          ("doorOpen", 224),
          ("dspCommFail", 38),
          ("engOprg", 226),
          ("engine", 225),
          ("eol", 39),
          ("esiMiss", 40),
          ("expShComDevUns", 41),
          ("expShComLnkDwn", 42),
          ("expShComLos", 43),
          ("explGs", 227),
          ("feci", 266),
          ("feedAFail", 44),
          ("feedAFuseFail", 289),
          ("feedBFail", 45),
          ("feedBFuseFail", 290),
          ("feim", 265),
          ("firDetr", 228),
          ("fire", 229),
          ("flFarEnd", 257),
          ("flNearEnd", 258),
          ("flood", 230),
          ("frcdWkSwBk", 46),
          ("frcdWkSwPr", 47),
          ("fuse", 231),
          ("fuseAlarm", 48),
          ("gen", 232),
          ("generic", 233),
          ("gfpPlm", 49),
          ("hiAir", 234),
          ("hiHum", 235),
          ("hiTemp", 50),
          ("hiWind", 236),
          ("hiWtr", 237),
          ("htThreshExceeded", 293),
          ("htasUnsupported", 295),
          ("hts", 292),
          ("htsThreshExceeded", 294),
          ("iaocb", 273),
          ("iaocm", 272),
          ("iaocp", 271),
          ("iceBuildup", 238),
          ("intruder", 239),
          ("invProv", 55),
          ("invkDbDltFail", 51),
          ("invkDbDltPass", 52),
          ("invkDbRstFail", 53),
          ("invkDbRstPass", 54),
          ("ipLckOut", 56),
          ("lf", 283),
          ("linkDown", 57),
          ("litChn", 58),
          ("loSpecRx", 269),
          ("loSync", 67),
          ("loTmRef", 68),
          ("loa", 59),
          ("lockProg", 210),
          ("lockoutOfPr", 60),
          ("lockoutOfWk", 61),
          ("lof", 62),
          ("lol", 63),
          ("lolightRx", 263),
          ("lolightTx", 264),
          ("lom", 64),
          ("lopP", 65),
          ("los", 66),
          ("lpbk", 69),
          ("lwBatvg", 240),
          ("lwFuel", 241),
          ("lwHum", 242),
          ("lwPres", 243),
          ("lwTemp", 244),
          ("lwWtr", 245),
          ("manWkSwBk", 70),
          ("manWkSwPr", 71),
          ("misc", 246),
          ("normal", 72),
          ("obrhtso", 73),
          ("oci", 204),
          ("oduPlm", 203),
          ("openDr", 247),
          ("oprHighFail", 288),
          ("oscLos", 74),
          ("otnPlm", 75),
          ("otuTti", 208),
          ("packPowerFail", 291),
          ("packUpgrdFail", 76),
          ("pmi", 275),
          ("portMea", 77),
          ("posRx", 278),
          ("posRxHigh", 286),
          ("posRxLow", 287),
          ("posTx", 279),
          ("power", 248),
          ("powerFail", 78),
          ("pump", 249),
          ("pwrBrwnt", 79),
          ("rcvdLockout", 296),
          ("rect", 250),
          ("rectHi", 251),
          ("rectLo", 252),
          ("relNumMea", 81),
          ("release", 80),
          ("replUnitDegrade", 282),
          ("replUnitFail", 82),
          ("replUnitIdMea", 83),
          ("replUnitMea", 84),
          ("replUnitMiss", 85),
          ("replUnitPlugin", 86),
          ("replUnitUnk", 87),
          ("replUnitUnplug", 88),
          ("replUnitUns", 89),
          ("rfi", 90),
          ("rpf", 91),
          ("scpRNChgFail", 93),
          ("scpRNChgPass", 94),
          ("scpRNChgProg", 95),
          ("scpRestart", 92),
          ("sd", 96),
          ("siFail", 97),
          ("siMiss", 98),
          ("siPlugin", 99),
          ("siUnk", 100),
          ("siUnplug", 101),
          ("smoke", 253),
          ("sqm", 102),
          ("srvrUnReachable", 205),
          ("srvrUnRspsive", 206),
          ("swBnkAFail", 103),
          ("swBnkBFail", 104),
          ("syncPri", 105),
          ("syncSec", 106),
          ("syncSwitchInt", 213),
          ("syncSwitchPri", 211),
          ("syncSwitchSec", 212),
          ("sysChkFail", 107),
          ("sysChkPass", 108),
          ("sysCom", 109),
          ("sysLoadFail", 110),
          ("sysLoadPass", 111),
          ("sysUpgrdFail", 112),
          ("sysUpgrdPass", 113),
          ("sysUpgrdProg", 114),
          ("tBdwUtlz", 214),
          ("tCtempHt", 176),
          ("tCtempHts", 177),
          ("tCv", 115),
          ("tCvL", 116),
          ("tCvOtu", 117),
          ("tCvP", 118),
          ("tCvS", 119),
          ("tEb", 120),
          ("tEs", 121),
          ("tEsL", 122),
          ("tEsP", 123),
          ("tEsS", 124),
          ("tFcP", 125),
          ("tFcseRx", 126),
          ("tFrdr", 127),
          ("tFrer", 128),
          ("tFrgt", 129),
          ("tHpBbe", 130),
          ("tHpEb", 131),
          ("tHpEs", 132),
          ("tHpSes", 133),
          ("tHpUas", 134),
          ("tInvBlk", 135),
          ("tJabr", 136),
          ("tLossRxHt", 270),
          ("tLtempHts", 179),
          ("tLtempLts", 180),
          ("tMsBbe", 137),
          ("tMsEb", 138),
          ("tMsEs", 139),
          ("tMsLossHt", 181),
          ("tMsSes", 140),
          ("tMsUas", 141),
          ("tNumBitsCr", 142),
          ("tNumBytesCr", 143),
          ("tObrHt", 182),
          ("tObrHts", 183),
          ("tObros", 280),
          ("tOprBht", 184),
          ("tOprHt", 185),
          ("tOprLt", 186),
          ("tOprRht", 187),
          ("tOptBht", 188),
          ("tOptBlt", 189),
          ("tOptHt", 190),
          ("tOptLt", 191),
          ("tOptRht", 192),
          ("tOptRlt", 193),
          ("tOsize", 145),
          ("tOtuBbe", 146),
          ("tOtuEb", 147),
          ("tOtuEs", 148),
          ("tOtuOfs", 149),
          ("tOtuSes", 150),
          ("tOtuUas", 151),
          ("tRsBbe", 152),
          ("tRsEb", 153),
          ("tRsEs", 154),
          ("tRsOfs", 155),
          ("tRsSes", 156),
          ("tRsUas", 157),
          ("tSSIOprHt", 195),
          ("tSefs", 158),
          ("tSefsOtu", 159),
          ("tSefsS", 160),
          ("tSemOtu", 161),
          ("tSes", 162),
          ("tSesL", 163),
          ("tSesP", 164),
          ("tSesS", 165),
          ("tTempHt", 196),
          ("tTfrcRx", 166),
          ("tTfrcTx", 167),
          ("tUas", 168),
          ("tUasL", 169),
          ("tUasP", 171),
          ("tUasS", 170),
          ("tUncrCdWrd", 172),
          ("tUsize", 173),
          ("tWavelength", 174),
          ("talna", 175),
          ("tim", 178),
          ("toxicGas", 254),
          ("tplna", 194),
          ("unassigned", 215),
          ("uneqO", 276),
          ("uneqP", 197),
          ("unsupported", 256),
          ("upgrdProg", 198),
          ("usrLckout", 199),
          ("ventn", 255),
          ("wkSwBk", 200),
          ("wkSwPr", 201),
          ("wna", 202))
    )



class EnvNotifCodeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("airCompr", 216),
          ("airCond", 217),
          ("airDryr", 218),
          ("batDschrd", 219),
          ("battery", 220),
          ("clFan", 221),
          ("cpMajor", 222),
          ("cpMinor", 223),
          ("doorOpen", 224),
          ("engOprg", 226),
          ("engine", 225),
          ("explGs", 227),
          ("firDetr", 228),
          ("fire", 229),
          ("flood", 230),
          ("fuse", 231),
          ("gen", 232),
          ("generic", 233),
          ("hiAir", 234),
          ("hiHum", 235),
          ("hiTemp", 50),
          ("hiWind", 236),
          ("hiWtr", 237),
          ("iceBuildup", 238),
          ("intruder", 239),
          ("lwBatvg", 240),
          ("lwFuel", 241),
          ("lwHum", 242),
          ("lwPres", 243),
          ("lwTemp", 244),
          ("lwWtr", 245),
          ("misc", 246),
          ("openDr", 247),
          ("power", 248),
          ("pump", 249),
          ("rect", 250),
          ("rectHi", 251),
          ("rectLo", 252),
          ("smoke", 253),
          ("toxicGas", 254),
          ("unassigned", 215),
          ("ventn", 255))
    )



class NotifObjectType(Integer32, TextualConvention):
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
              58)
        )
    )
    namedValues = NamedValues(
        *(("amd", 1),
          ("bri", 34),
          ("env", 52),
          ("eqpt", 2),
          ("fc", 3),
          ("fe", 4),
          ("ge", 5),
          ("ip", 6),
          ("lag", 31),
          ("ntpassoc", 58),
          ("oa", 11),
          ("oc12", 7),
          ("oc192", 8),
          ("oc3", 9),
          ("oc48", 10),
          ("odcc", 55),
          ("odu1", 35),
          ("osc", 54),
          ("ospf", 12),
          ("perCos", 51),
          ("perEvc", 50),
          ("port", 13),
          ("secu", 32),
          ("slaMsmt", 53),
          ("stm1", 14),
          ("stm16", 15),
          ("stm4", 16),
          ("stm64", 17),
          ("sts1", 18),
          ("sts12c", 19),
          ("sts15c", 43),
          ("sts18c", 44),
          ("sts21c", 45),
          ("sts24c", 46),
          ("sts30c", 47),
          ("sts36c", 48),
          ("sts3c", 20),
          ("sts48c", 21),
          ("sts6c", 41),
          ("sts72c", 49),
          ("sts9c", 42),
          ("subodu1", 36),
          ("vc4", 22),
          ("vc410c", 38),
          ("vc412c", 23),
          ("vc416c", 24),
          ("vc424c", 25),
          ("vc42c", 37),
          ("vc43c", 39),
          ("vc44c", 26),
          ("vc45c", 40),
          ("vc46c", 27),
          ("vc47c", 28),
          ("vc48c", 29),
          ("wch", 57),
          ("wdm", 56),
          ("xcvr", 30),
          ("xge", 33))
    )



class FiberType(Integer32, TextualConvention):
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
        *(("dsf", 2),
          ("multimode", 5),
          ("ndsf", 3),
          ("none", 1),
          ("nzdsf", 4))
    )



class WDMGrid(Integer32, TextualConvention):
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
        *(("ghz100", 3),
          ("ghz200", 4),
          ("ghz50", 2),
          ("nm20", 5),
          ("none", 1))
    )



class TimeZone(Integer32, TextualConvention):
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
              328)
        )
    )
    namedValues = NamedValues(
        *(("afghanistan", 1),
          ("albania", 2),
          ("algeria", 3),
          ("americanSamoa", 4),
          ("andorra", 5),
          ("anguilla", 8),
          ("antarctica", 9),
          ("antarcticaDavis", 10),
          ("antarcticaDumontDurville", 11),
          ("antarcticaMawson", 12),
          ("antigua", 13),
          ("argentina", 6),
          ("argentinaWesternProv", 7),
          ("armenia", 14),
          ("aruba", 15),
          ("ascension", 16),
          ("australiaAustralianCapitalTerritory", 17),
          ("australiaLordHoweIsland", 18),
          ("australiaNewSouthWales", 19),
          ("australiaNorthernTerritory", 20),
          ("australiaQueensland", 21),
          ("australiaSouth", 22),
          ("australiaTasmania", 23),
          ("australiaVictoria", 24),
          ("australiaWestern", 25),
          ("austria", 26),
          ("azerbaijan", 27),
          ("azores", 28),
          ("bahamas", 29),
          ("bahrain", 30),
          ("balearicIslands", 31),
          ("bangladesh", 32),
          ("barbados", 33),
          ("belarus", 34),
          ("belgium", 35),
          ("belize", 36),
          ("benin", 37),
          ("bermuda", 38),
          ("bhutan", 39),
          ("bolivia", 40),
          ("bonaire", 41),
          ("bosniaHercegovina", 42),
          ("botswana", 43),
          ("brazilAcre", 44),
          ("brazilAtlanticIslands", 45),
          ("brazilEast", 46),
          ("brazilWest", 47),
          ("britishIndianOceanTerritoryChagos", 48),
          ("britishVirginIslands", 49),
          ("brunei", 50),
          ("bulgaria", 51),
          ("burkinaFaso", 52),
          ("burundi", 53),
          ("cambodia", 54),
          ("cameroon", 55),
          ("canadaAtlantic", 56),
          ("canadaCentral", 57),
          ("canadaEastern", 58),
          ("canadaMountain", 59),
          ("canadaNewfoundland", 60),
          ("canadaPacificYukon", 61),
          ("canadaSaskatchewan", 62),
          ("canaryIslands", 63),
          ("cantonEnderburyIslands", 64),
          ("capeVerde", 65),
          ("carolineIslands", 66),
          ("caymanIslands", 67),
          ("centralAfricanRepublic", 68),
          ("chad", 69),
          ("channelIslands", 70),
          ("chathamIsland", 71),
          ("chile", 72),
          ("chinaPeoplesRepublic", 73),
          ("christmasIslands", 74),
          ("cocosIslands", 75),
          ("colombia", 76),
          ("congo", 77),
          ("cookIslands", 78),
          ("costaRica", 79),
          ("coteDivoire", 80),
          ("croatia", 81),
          ("cuba", 82),
          ("curacao", 83),
          ("cyprus", 84),
          ("czechRepublic", 85),
          ("denmark", 86),
          ("djibouti", 87),
          ("dominica", 88),
          ("dominicanRepublic", 89),
          ("easterIsland", 90),
          ("ecuador", 91),
          ("egypt", 92),
          ("elSalvador", 93),
          ("england", 94),
          ("equatorialGuinea", 95),
          ("eritrea", 96),
          ("estonia", 97),
          ("ethiopia", 98),
          ("falklandIslands", 99),
          ("faroeIsland", 100),
          ("fiji", 101),
          ("finland", 102),
          ("france", 103),
          ("francePierreMiquelon", 104),
          ("frenchGuiana", 105),
          ("frenchPolynesia", 106),
          ("gabon", 107),
          ("galapagos", 108),
          ("gambia", 109),
          ("gambierIsland", 110),
          ("georgia", 111),
          ("germany", 112),
          ("ghana", 113),
          ("gibraltar", 114),
          ("greece", 115),
          ("greenland", 116),
          ("greenlandScoresbysun", 117),
          ("greenlandThule", 118),
          ("greenwichMeanTimeUtc", 119),
          ("grenada", 120),
          ("grenadines", 121),
          ("guadeloupe", 122),
          ("guam", 123),
          ("guatemala", 124),
          ("guinea", 125),
          ("guineaBissau", 126),
          ("guyana", 127),
          ("haiti", 128),
          ("honduras", 129),
          ("hongKong", 130),
          ("hungary", 131),
          ("iceland", 132),
          ("india", 133),
          ("indonesiaCentral", 134),
          ("indonesiaEast", 135),
          ("indonesiaWest", 136),
          ("iran", 138),
          ("iraq", 137),
          ("irelandRepublicOf", 139),
          ("israel", 140),
          ("italy", 141),
          ("jamaica", 142),
          ("japan", 143),
          ("johnstonIsland", 144),
          ("jordan", 145),
          ("kazakhstan", 146),
          ("kenya", 147),
          ("kiribati", 148),
          ("kiribatiPhoenixIslands", 149),
          ("koreaDemRepublicOf", 150),
          ("koreaRepublicOf", 151),
          ("kosrae", 152),
          ("kuwait", 153),
          ("kwajalein", 154),
          ("kyrgyzstan", 155),
          ("laos", 156),
          ("latvia", 157),
          ("lebanon", 158),
          ("leewardIslands", 159),
          ("lesotho", 160),
          ("liberia", 161),
          ("libya", 162),
          ("liechtenstein", 163),
          ("lithuania", 164),
          ("luxembourg", 165),
          ("macedonia", 166),
          ("madagascar", 167),
          ("madeira", 168),
          ("malawi", 169),
          ("malaysia", 170),
          ("maldives", 171),
          ("mali", 172),
          ("mallorcaIsland", 173),
          ("malta", 174),
          ("marianaIsland", 175),
          ("marquesasIslands", 176),
          ("marshallIsland", 177),
          ("martinique", 178),
          ("mauritania", 179),
          ("mauritius", 180),
          ("mayotte", 181),
          ("melilla", 182),
          ("mexico", 183),
          ("mexicoBajaCalifnorte", 184),
          ("mexicoNayarit", 185),
          ("mexicoSinaloa", 186),
          ("mexicoSonora", 187),
          ("midwayIsland", 188),
          ("moldova", 189),
          ("moldovianreppridnestrovye", 190),
          ("moluccas", 191),
          ("monaco", 192),
          ("mongolia", 193),
          ("morocco", 194),
          ("mozambique", 195),
          ("myanmar", 196),
          ("namibia", 197),
          ("nauruRepublicOf", 198),
          ("nepal", 199),
          ("netherlands", 200),
          ("netherlandsAntilles", 201),
          ("nevisMontserrat", 202),
          ("newCaledonia", 203),
          ("newHebrides", 204),
          ("newZealand", 205),
          ("newZealandTokelauIslands", 206),
          ("nicaragua", 207),
          ("niger", 208),
          ("nigeria", 209),
          ("niueIsland", 210),
          ("norfolkIsland", 211),
          ("northSumatra", 214),
          ("northernIreland", 212),
          ("northernMarianaIslands", 213),
          ("norway", 215),
          ("oman", 216),
          ("pakistan", 217),
          ("palau", 218),
          ("panama", 219),
          ("papuaNewGuinea", 220),
          ("paraguay", 221),
          ("peru", 222),
          ("philippines", 223),
          ("pingelap", 224),
          ("poland", 225),
          ("ponapeIsland", 226),
          ("portugal", 227),
          ("principeIsland", 228),
          ("puertoRico", 229),
          ("qatar", 230),
          ("reunion", 231),
          ("romania", 232),
          ("russianFederationChitayakutsk", 233),
          ("russianFederationIrkutskulanude", 234),
          ("russianFederationKaliningrad", 235),
          ("russianFederationKamchatkaanadyr", 236),
          ("russianFederationKrasnoyarsktomsk", 237),
          ("russianFederationMagadankolyma", 238),
          ("russianFederationMoscowStPetersburg", 239),
          ("russianFederationNovosibirskomsk", 240),
          ("russianFederationSamaraizhevsk", 241),
          ("russianFederationVladivostokkhabarovsk", 242),
          ("russianFederationYekaterinburgperm", 243),
          ("rwanda", 244),
          ("saba", 245),
          ("samoa", 246),
          ("sanMarino", 247),
          ("saotomePrincipe", 248),
          ("saudiArabia", 249),
          ("scotland", 250),
          ("senegal", 251),
          ("seychelles", 252),
          ("sierraLeone", 253),
          ("singapore", 254),
          ("slovakia", 255),
          ("slovenia", 256),
          ("societyIsland", 257),
          ("solomonIslands", 258),
          ("somalia", 259),
          ("southAfrica", 260),
          ("southSumatra", 261),
          ("spain", 262),
          ("sriLanka", 263),
          ("stChristopher", 264),
          ("stCroix", 265),
          ("stHelena", 266),
          ("stJohn", 267),
          ("stKittsNevis", 268),
          ("stLucia", 269),
          ("stMaarten", 270),
          ("stPierreMiquelon", 271),
          ("stThomas", 272),
          ("stVincent", 273),
          ("sudan", 274),
          ("suriname", 275),
          ("swaziland", 276),
          ("sweden", 277),
          ("switzerland", 278),
          ("syria", 279),
          ("tahiti", 280),
          ("taiwan", 281),
          ("tajikistan", 282),
          ("tanzania", 283),
          ("thailand", 284),
          ("togo", 285),
          ("tonga", 286),
          ("trinidadAndTobago", 287),
          ("tuamotuIsland", 288),
          ("tubuaiIsland", 289),
          ("tunisia", 290),
          ("turkey", 291),
          ("turkmenistan", 292),
          ("turksAndCaicosIslands", 293),
          ("tuvalu", 294),
          ("uganda", 295),
          ("ukraine", 296),
          ("unitedArabEmirates", 297),
          ("unitedKingdom", 298),
          ("uruguay", 299),
          ("usaAlaska", 300),
          ("usaAleutian", 301),
          ("usaArizona", 302),
          ("usaCentral", 303),
          ("usaEastern", 304),
          ("usaHawaii", 305),
          ("usaIndianaEast", 306),
          ("usaMountain", 307),
          ("usaPacific", 308),
          ("uzbekistan", 309),
          ("vanuatu", 310),
          ("vaticanCity", 311),
          ("venezuela", 312),
          ("vietnam", 313),
          ("virginIslands", 314),
          ("wakeIsland", 315),
          ("wales", 316),
          ("wallisAndFutunaIslands", 317),
          ("westernSahara", 318),
          ("windwardIslands", 319),
          ("yemen", 320),
          ("yugoslavia", 321),
          ("zaireHautZaire", 322),
          ("zaireKasai", 323),
          ("zaireKinshasaMbandaka", 324),
          ("zaireKivu", 325),
          ("zaireShaba", 326),
          ("zambia", 327),
          ("zimbabwe", 328))
    )



class AdminStatus(Integer32, TextualConvention):
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
        *(("autoEnabled", 3),
          ("disabled", 2),
          ("enabled", 1))
    )



class OperStatus(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )



class OperStatQlfr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )



class HoursAndMinutes(OctetString, TextualConvention):
    status = "current"
    displayHint = "7a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )



class PassivePortType(Integer32, TextualConvention):
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
              45)
        )
    )
    namedValues = NamedValues(
        *(("blue", 39),
          ("cband", 34),
          ("channel1", 1),
          ("channel10", 10),
          ("channel11", 11),
          ("channel12", 12),
          ("channel13", 13),
          ("channel14", 14),
          ("channel15", 15),
          ("channel16", 16),
          ("channel17", 17),
          ("channel18", 18),
          ("channel19", 19),
          ("channel2", 2),
          ("channel20", 20),
          ("channel21", 21),
          ("channel22", 22),
          ("channel23", 23),
          ("channel24", 24),
          ("channel25", 25),
          ("channel26", 26),
          ("channel27", 27),
          ("channel28", 28),
          ("channel29", 29),
          ("channel3", 3),
          ("channel30", 30),
          ("channel31", 31),
          ("channel32", 32),
          ("channel4", 4),
          ("channel5", 5),
          ("channel53", 41),
          ("channel55", 42),
          ("channel57", 43),
          ("channel59", 44),
          ("channel6", 6),
          ("channel7", 7),
          ("channel8", 8),
          ("channel9", 9),
          ("cwdm", 37),
          ("dwdm", 38),
          ("line", 33),
          ("passthru", 35),
          ("red", 40),
          ("upgrade", 36),
          ("wideband1310", 45))
    )



class XcvrProtocolType(Integer32, TextualConvention):
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
              36)
        )
    )
    namedValues = NamedValues(
        *(("autodetect", 2),
          ("escon", 3),
          ("fc100", 4),
          ("fc1200", 26),
          ("fc200", 5),
          ("fc400", 25),
          ("fddi", 6),
          ("fe", 7),
          ("ge", 8),
          ("none", 1),
          ("oc12", 10),
          ("oc192", 21),
          ("oc192EFec", 28),
          ("oc192Fec", 22),
          ("oc3", 9),
          ("oc48", 11),
          ("oc48fec", 12),
          ("odu1otu2Fec", 30),
          ("otu2eEFec", 34),
          ("otu2eFec", 33),
          ("smpte259", 13),
          ("smpte292", 15),
          ("smpte344", 14),
          ("stm1", 16),
          ("stm16", 18),
          ("stm4", 17),
          ("stm64", 23),
          ("stm64EFec", 29),
          ("stm64Fec", 24),
          ("tenGeLan", 19),
          ("tenGeLanEFec", 27),
          ("tenGeLanEFecEPCMF", 32),
          ("tenGeLanEFecEPV3", 36),
          ("tenGeLanFec", 20),
          ("tenGeLanFecEPCMF", 31),
          ("tenGeLanFecEPV3", 35))
    )



class PMIntervalType(Integer32, TextualConvention):
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
        *(("day1", 2),
          ("min15", 1),
          ("untimed", 3))
    )



class PMValidity(Integer32, TextualConvention):
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
        *(("complete", 1),
          ("notAvailable", 2),
          ("partialCount", 3))
    )



class BERType(Integer32, TextualConvention):
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tenExpMinus10", 9),
          ("tenExpMinus11", 10),
          ("tenExpMinus12", 11),
          ("tenExpMinus3", 8),
          ("tenExpMinus4", 7),
          ("tenExpMinus5", 6),
          ("tenExpMinus6", 5),
          ("tenExpMinus7", 4),
          ("tenExpMinus8", 3),
          ("tenExpMinus9", 2))
    )



class ProtSwEvtType(Integer32, TextualConvention):
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
        *(("autoWorkSwBack", 2),
          ("autoWorkSwProt", 1),
          ("frcdWorkSwBack", 6),
          ("frcdWorkSwProt", 5),
          ("lockoutOfProt", 8),
          ("lockoutOfWork", 7),
          ("manWorkSwBack", 4),
          ("manWorkSwProt", 3),
          ("releaseProtSw", 9))
    )



class SyncSwEvtType(Integer32, TextualConvention):
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
        *(("syncSwToInternal", 3),
          ("syncSwToPrimaryRef", 1),
          ("syncSwToSecondaryRef", 2))
    )



class MediaRateType(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiated", 2),
          ("fd10", 5),
          ("fd100", 3),
          ("fd1000", 7),
          ("hd10", 6),
          ("hd100", 4),
          ("hd1000", 8),
          ("unknown", 1))
    )



class DuplexModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1))
    )



class MirrorConfigType(Integer32, TextualConvention):
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
        *(("mfp-both", 5),
          ("mfp-egress", 4),
          ("mfp-ingress", 3),
          ("mtp", 2),
          ("none", 1))
    )



class UpgradeCompleteStage(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("autoNr", 8),
          ("done", 6),
          ("inactive", 1),
          ("loadDone", 4),
          ("loadStarted", 3),
          ("reboot", 5),
          ("started", 2),
          ("systemDone", 7))
    )



class XCType(Integer32, TextualConvention):
    status = "current"
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
        *(("oneWay", 1),
          ("oneWayBr", 5),
          ("oneWayPr", 3),
          ("twoWay", 2),
          ("twoWayBr", 6),
          ("twoWayPr", 4))
    )



class ProtSwOpCmd(Integer32, TextualConvention):
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
        *(("frcdProtSw", 3),
          ("lockout", 4),
          ("manProtSw", 2),
          ("noOp", 1),
          ("release", 5))
    )



class ProtectionStatusType(Integer32, TextualConvention):
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
        *(("active", 2),
          ("forced", 4),
          ("lockout", 5),
          ("none", 1),
          ("standby", 3))
    )



class PMMontype(Integer32, TextualConvention):
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
              76)
        )
    )
    namedValues = NamedValues(
        *(("caseTemp", 1),
          ("cv", 28),
          ("cvl", 53),
          ("cvp", 35),
          ("cvs", 19),
          ("delayAvg", 74),
          ("delayMax", 73),
          ("delayVarAvg", 76),
          ("delayVarMax", 75),
          ("effectiveGain", 8),
          ("es", 29),
          ("esl", 54),
          ("esp", 36),
          ("ess", 20),
          ("farEndFL", 71),
          ("fcp", 39),
          ("fcse", 48),
          ("frdr", 47),
          ("frgt", 51),
          ("fsoopt", 9),
          ("hpbbe", 41),
          ("hpeb", 40),
          ("hpes", 42),
          ("hpses", 43),
          ("hpuas", 44),
          ("invblk", 31),
          ("jabr", 52),
          ("laser1Current", 10),
          ("laser1Power", 12),
          ("laser1Temp", 2),
          ("laser2Current", 11),
          ("laser2Power", 13),
          ("laser2Temp", 3),
          ("lbc", 18),
          ("msInsLoss", 7),
          ("msbbe", 58),
          ("mseb", 57),
          ("mses", 59),
          ("msses", 60),
          ("msuas", 61),
          ("nbitcr", 32),
          ("nbytcr", 33),
          ("nearEndFL", 72),
          ("obr", 14),
          ("opr", 4),
          ("opt", 6),
          ("osize", 50),
          ("otubbe", 63),
          ("otueb", 62),
          ("otues", 64),
          ("otuofs", 66),
          ("otuses", 65),
          ("otuuas", 70),
          ("rsbbe", 24),
          ("rseb", 23),
          ("rses", 25),
          ("rsofs", 27),
          ("rsses", 26),
          ("rsuas", 68),
          ("sefss", 22),
          ("ses", 30),
          ("sesl", 55),
          ("sesp", 37),
          ("sess", 21),
          ("ssiopr", 5),
          ("supplyVoltage", 17),
          ("temp", 16),
          ("tfrcrx", 45),
          ("tfrctx", 46),
          ("uas", 69),
          ("uasl", 56),
          ("uasp", 38),
          ("uass", 67),
          ("uncrcdw", 34),
          ("usize", 49),
          ("voa", 15))
    )



class SwitchIdxType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )



class ProtocolActionType(Integer32, TextualConvention):
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
        *(("discard", 1),
          ("peer", 2),
          ("tunnel", 3))
    )



class PvxPortType(Integer32, TextualConvention):
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
        *(("gccOtu2", 4),
          ("generic", 5),
          ("gigE", 1),
          ("lag", 3),
          ("mgmtVLan", 6),
          ("unknown", 0),
          ("xGigE", 2))
    )



class PvxL1PortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gigE", 1),
          ("xGigE", 2))
    )



class MonitorPeriodType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hour24", 2),
          ("min15", 1))
    )



class CommandStateType(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 3),
          ("notSet", 6),
          ("ready", 1),
          ("rmepNotReady", 7),
          ("start", 2),
          ("stop", 5),
          ("testFailed", 4))
    )



class SlaTestRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiator", 1),
          ("responder", 2))
    )



class PmTestCmdState(Integer32, TextualConvention):
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
        *(("disable", 5),
          ("enable", 1),
          ("pmIsRunning", 4),
          ("pmSetupFailed", 3),
          ("pmSetupInProgress", 2))
    )



class CirTestResult(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("pass", 1))
    )



class PowerFeedModeType(Integer32, TextualConvention):
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
        *(("ac", 1),
          ("both", 4),
          ("dc", 2),
          ("none", 3))
    )



class ProfileNameType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class AreaID(IpAddress, TextualConvention):
    status = "current"


class DesignatedRouterPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class LoopbackType(Integer32, TextualConvention):
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
        *(("facilityLpbk", 1),
          ("noLoopback", 0),
          ("terminalLpbk", 2))
    )



class InetAddressType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dns", 16),
          ("ipv4", 1),
          ("ipv4z", 3),
          ("ipv6", 2),
          ("ipv6z", 4),
          ("unknown", 0))
    )



class InetAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class InetAddressIPv4(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class InetAddressIPv6(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:2x:2x:2x:2x:2x:2x:2x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class InetAddressIPv4z(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d%4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class InetAddressIPv6z(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:2x:2x:2x:2x:2x:2x:2x%4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )



class InetAddressDNS(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class ZeroBasedCounter32(Gauge32, TextualConvention):
    status = "current"


class LldpChassisIdSubtype(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("interfaceName", 6),
          ("local", 7),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("notPresent", 8),
          ("portComponent", 3))
    )



class LldpChassisId(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class LldpPortIdSubtype(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("agentCircuitId", 6),
          ("interfaceAlias", 1),
          ("interfaceName", 5),
          ("local", 7),
          ("macAddress", 3),
          ("networkAddress", 4),
          ("notPresent", 8),
          ("portComponent", 2))
    )



class LldpPortId(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BTI-TC-MIB",
    **{"FixedX10": FixedX10,
       "FixedX100": FixedX100,
       "FixedX1000": FixedX1000,
       "Unsigned64": Unsigned64,
       "InitializeCmd": InitializeCmd,
       "ShelfType": ShelfType,
       "ShelfConfigType": ShelfConfigType,
       "SlotType": SlotType,
       "CpType": CpType,
       "OaType": OaType,
       "XcvrType": XcvrType,
       "AmdType": AmdType,
       "AmdPortType": AmdPortType,
       "OcnType": OcnType,
       "StsnType": StsnType,
       "StmnType": StmnType,
       "VcnType": VcnType,
       "FcType": FcType,
       "OdunType": OdunType,
       "CondReportType": CondReportType,
       "CondSeverity": CondSeverity,
       "CondServiceAffecting": CondServiceAffecting,
       "NotifCodeType": NotifCodeType,
       "EnvNotifCodeType": EnvNotifCodeType,
       "NotifObjectType": NotifObjectType,
       "FiberType": FiberType,
       "WDMGrid": WDMGrid,
       "TimeZone": TimeZone,
       "AdminStatus": AdminStatus,
       "OperStatus": OperStatus,
       "OperStatQlfr": OperStatQlfr,
       "HoursAndMinutes": HoursAndMinutes,
       "PassivePortType": PassivePortType,
       "XcvrProtocolType": XcvrProtocolType,
       "PMIntervalType": PMIntervalType,
       "PMValidity": PMValidity,
       "BERType": BERType,
       "ProtSwEvtType": ProtSwEvtType,
       "SyncSwEvtType": SyncSwEvtType,
       "MediaRateType": MediaRateType,
       "DuplexModeType": DuplexModeType,
       "MirrorConfigType": MirrorConfigType,
       "UpgradeCompleteStage": UpgradeCompleteStage,
       "XCType": XCType,
       "ProtSwOpCmd": ProtSwOpCmd,
       "ProtectionStatusType": ProtectionStatusType,
       "PMMontype": PMMontype,
       "SwitchIdxType": SwitchIdxType,
       "ProtocolActionType": ProtocolActionType,
       "PvxPortType": PvxPortType,
       "PvxL1PortType": PvxL1PortType,
       "MonitorPeriodType": MonitorPeriodType,
       "CommandStateType": CommandStateType,
       "SlaTestRole": SlaTestRole,
       "PmTestCmdState": PmTestCmdState,
       "CirTestResult": CirTestResult,
       "PowerFeedModeType": PowerFeedModeType,
       "ProfileNameType": ProfileNameType,
       "AreaID": AreaID,
       "DesignatedRouterPriority": DesignatedRouterPriority,
       "LoopbackType": LoopbackType,
       "InetAddressType": InetAddressType,
       "InetAddress": InetAddress,
       "InetAddressIPv4": InetAddressIPv4,
       "InetAddressIPv6": InetAddressIPv6,
       "InetAddressIPv4z": InetAddressIPv4z,
       "InetAddressIPv6z": InetAddressIPv6z,
       "InetAddressDNS": InetAddressDNS,
       "ZeroBasedCounter32": ZeroBasedCounter32,
       "LldpChassisIdSubtype": LldpChassisIdSubtype,
       "LldpChassisId": LldpChassisId,
       "LldpPortIdSubtype": LldpPortIdSubtype,
       "LldpPortId": LldpPortId,
       "btiTcMib": btiTcMib}
)
