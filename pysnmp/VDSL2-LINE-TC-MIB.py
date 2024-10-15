# SNMP MIB module (VDSL2-LINE-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VDSL2-LINE-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:53 2024
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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

vdsl2TCMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 3)
)
vdsl2TCMIB.setRevisions(
        ("2009-09-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Xdsl2Unit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("xtuc", 1),
          ("xtur", 2))
    )



class Xdsl2Direction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("upstream", 1))
    )



class Xdsl2Band(Integer32, TextualConvention):
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
        *(("downstream", 2),
          ("ds1", 4),
          ("ds2", 6),
          ("ds3", 8),
          ("ds4", 10),
          ("upstream", 1),
          ("us0", 3),
          ("us1", 5),
          ("us2", 7),
          ("us3", 9),
          ("us4", 11))
    )



class Xdsl2TransmissionModeType(Bits, TextualConvention):
    status = "current"


class Xdsl2RaMode(Integer32, TextualConvention):
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
        *(("dynamicRa", 3),
          ("manual", 1),
          ("raInit", 2))
    )



class Xdsl2InitResult(Integer32, TextualConvention):
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
        *(("commFail", 3),
          ("configError", 1),
          ("configNotFeasible", 2),
          ("noFail", 0),
          ("noPeerAtu", 4),
          ("otherCause", 5))
    )



class Xdsl2OperationModes(Integer32, TextualConvention):
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
              20,
              21,
              22,
              23,
              26,
              27,
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
              48,
              49,
              50,
              51,
              52,
              53,
              58,
              59,
              60)
        )
    )
    namedValues = NamedValues(
        *(("ansit1413", 2),
          ("defMode", 1),
          ("etsi", 3),
          ("g9921IsdnNonOverlapped", 6),
          ("g9921PotsNonOverlapped", 4),
          ("g9921PotsOverlapped", 5),
          ("g9921isdnOverlapped", 7),
          ("g9921tcmIsdnNonOverlapped", 8),
          ("g9921tcmIsdnOverlapped", 9),
          ("g9921tcmIsdnSymmetric", 14),
          ("g9922potsNonOverlapped", 10),
          ("g9922potsOverlapped", 11),
          ("g9922tcmIsdnNonOverlapped", 12),
          ("g9922tcmIsdnOverlapped", 13),
          ("g9923AnnexIAllDigNonOverlapped", 30),
          ("g9923AnnexIAllDigOverlapped", 31),
          ("g9923AnnexJAllDigNonOverlapped", 32),
          ("g9923AnnexJAllDigOverlapped", 33),
          ("g9923AnnexLMode1NonOverlapped", 36),
          ("g9923AnnexLMode2NonOverlapped", 37),
          ("g9923AnnexLMode3Overlapped", 38),
          ("g9923AnnexLMode4Overlapped", 39),
          ("g9923AnnexMPotsNonOverlapped", 40),
          ("g9923AnnexMPotsOverlapped", 41),
          ("g9923IsdnNonOverlapped", 22),
          ("g9923PotsNonOverlapped", 20),
          ("g9923PotsOverlapped", 21),
          ("g9923isdnOverlapped", 23),
          ("g9924AnnexIAllDigNonOverlapped", 34),
          ("g9924AnnexIAllDigOverlapped", 35),
          ("g9924potsNonOverlapped", 26),
          ("g9924potsOverlapped", 27),
          ("g9925AnnexIAllDigNonOverlapped", 48),
          ("g9925AnnexIAllDigOverlapped", 49),
          ("g9925AnnexJAllDigNonOverlapped", 50),
          ("g9925AnnexJAllDigOverlapped", 51),
          ("g9925AnnexMPotsNonOverlapped", 52),
          ("g9925AnnexMPotsOverlapped", 53),
          ("g9925IsdnNonOverlapped", 44),
          ("g9925PotsNonOverlapped", 42),
          ("g9925PotsOverlapped", 43),
          ("g9925isdnOverlapped", 45),
          ("g9932AnnexA", 58),
          ("g9932AnnexB", 59),
          ("g9932AnnexC", 60))
    )



class Xdsl2PowerMngState(Integer32, TextualConvention):
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
        *(("l0", 1),
          ("l1", 2),
          ("l2", 3),
          ("l3", 4))
    )



class Xdsl2ConfPmsForce(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l0orL2toL3", 3),
          ("l0toL2", 2),
          ("l3toL0", 0))
    )



class Xdsl2LinePmMode(Bits, TextualConvention):
    status = "current"


class Xdsl2LineLdsf(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("inhibit", 0))
    )



class Xdsl2LdsfResult(Integer32, TextualConvention):
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
        *(("aborted", 6),
          ("adminUp", 9),
          ("cannotRun", 5),
          ("failed", 7),
          ("illegalMode", 8),
          ("inProgress", 3),
          ("noResources", 11),
          ("none", 1),
          ("success", 2),
          ("tableFull", 10),
          ("unsupported", 4))
    )



class Xdsl2LineBpsc(Integer32, TextualConvention):
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
          ("measure", 2))
    )



class Xdsl2BpscResult(Integer32, TextualConvention):
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
        *(("failed", 5),
          ("inProgress", 3),
          ("noResources", 6),
          ("none", 1),
          ("success", 2),
          ("unsupported", 4))
    )



class Xdsl2LineReset(Integer32, TextualConvention):
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
          ("reset", 2))
    )



class Xdsl2LineProfiles(Bits, TextualConvention):
    status = "current"


class Xdsl2LineClassMask(Integer32, TextualConvention):
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
        *(("a998ORb997M1cORc998B", 2),
          ("b997M1xOR998co", 3),
          ("b997M2x", 4),
          ("b998AdeM2x", 7),
          ("b998M1x", 5),
          ("b998M2x", 6),
          ("bHpeM1", 8),
          ("none", 1))
    )



class Xdsl2LineLimitMask(Bits, TextualConvention):
    status = "current"


class Xdsl2LineUs0Disable(Bits, TextualConvention):
    status = "current"


class Xdsl2LineUs0Mask(Bits, TextualConvention):
    status = "current"


class Xdsl2SymbolProtection(Integer32, TextualConvention):
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("eightSymbols", 10),
          ("elevenSymbols", 13),
          ("fifteenSymbols", 17),
          ("fiveSymbols", 7),
          ("fourSymbols", 6),
          ("fourteenSymbols", 16),
          ("halfSymbol", 2),
          ("nineSymbols", 11),
          ("noProtection", 1),
          ("sevenSymbols", 9),
          ("singleSymbol", 3),
          ("sixSymbols", 8),
          ("sixteenSymbols", 18),
          ("tenSymbols", 12),
          ("thirteeSymbols", 15),
          ("threeSymbols", 5),
          ("twelveSymbols", 14),
          ("twoSymbols", 4))
    )



class Xdsl2SymbolProtection8(Integer32, TextualConvention):
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("eightSymbols", 9),
          ("elevenSymbols", 12),
          ("fifteenSymbols", 16),
          ("fiveSymbols", 6),
          ("fourSymbols", 5),
          ("fourteenSymbols", 15),
          ("nineSymbols", 10),
          ("noProtection", 1),
          ("sevenSymbols", 8),
          ("singleSymbol", 2),
          ("sixSymbols", 7),
          ("sixteenSymbols", 17),
          ("tenSymbols", 11),
          ("thirteeSymbols", 14),
          ("threeSymbols", 4),
          ("twelveSymbols", 13),
          ("twoSymbols", 3))
    )



class Xdsl2MaxBer(Integer32, TextualConvention):
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
        *(("eminus3", 1),
          ("eminus5", 2),
          ("eminus7", 3))
    )



class Xdsl2ChInitPolicy(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("policy0", 1),
          ("policy1", 2))
    )



class Xdsl2ScMaskDs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )



class Xdsl2ScMaskUs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )



class Xdsl2CarMask(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class Xdsl2RfiBands(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class Xdsl2PsdMaskDs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )



class Xdsl2PsdMaskUs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )



class Xdsl2Tssi(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )



class Xdsl2LastTransmittedState(Integer32, TextualConvention):
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
              320)
        )
    )
    namedValues = NamedValues(
        *(("atucComb1", 2),
          ("atucComb2", 4),
          ("atucComb3", 8),
          ("atucEct", 16),
          ("atucExchmarker", 25),
          ("atucG9941", 0),
          ("atucIComb2", 9),
          ("atucIcomb1", 5),
          ("atucLineprob", 6),
          ("atucMedley", 24),
          ("atucMsg1", 21),
          ("atucMsg2", 26),
          ("atucMsgfmt", 10),
          ("atucMsgpcb", 11),
          ("atucParams", 29),
          ("atucQuiet1", 1),
          ("atucQuiet2", 3),
          ("atucQuiet3", 7),
          ("atucQuiet4", 12),
          ("atucReverb1", 13),
          ("atucReverb2", 15),
          ("atucReverb3", 17),
          ("atucReverb4", 19),
          ("atucReverb5", 22),
          ("atucReverb6", 27),
          ("atucReverb7", 30),
          ("atucSegue1", 20),
          ("atucSegue2", 23),
          ("atucSegue3", 28),
          ("atucSegue4", 31),
          ("atucShowtime", 32),
          ("atucTref1", 14),
          ("atucTref2", 18),
          ("aturComb1", 102),
          ("aturComb2", 104),
          ("aturComb3", 108),
          ("aturEct", 117),
          ("aturExchmarker", 124),
          ("aturG9941", 100),
          ("aturIcomb1", 105),
          ("aturIcomb2", 109),
          ("aturLineprob", 106),
          ("aturMedley", 123),
          ("aturMsg1", 122),
          ("aturMsg2", 125),
          ("aturMsgfmt", 110),
          ("aturMsgpcb", 111),
          ("aturParams", 128),
          ("aturQuiet1", 101),
          ("aturQuiet2", 103),
          ("aturQuiet3", 107),
          ("aturQuiet4", 113),
          ("aturQuiet5", 115),
          ("aturReverb1", 112),
          ("aturReverb2", 114),
          ("aturReverb3", 116),
          ("aturReverb4", 118),
          ("aturReverb5", 120),
          ("aturReverb6", 126),
          ("aturReverb7", 129),
          ("aturSegue1", 119),
          ("aturSegue2", 121),
          ("aturSegue3", 127),
          ("aturSegue4", 130),
          ("aturShowtime", 131),
          ("vtucChDiscov1", 202),
          ("vtucChDiscov2", 208),
          ("vtucEct", 214),
          ("vtucG9941", 200),
          ("vtucMedley", 219),
          ("vtucPeriodic1", 206),
          ("vtucPeriodic2", 216),
          ("vtucPilot1", 204),
          ("vtucPilot2", 212),
          ("vtucPilot3", 215),
          ("vtucQuiet1", 201),
          ("vtucQuiet2", 205),
          ("vtucShowtime", 221),
          ("vtucSynchro1", 203),
          ("vtucSynchro2", 207),
          ("vtucSynchro3", 209),
          ("vtucSynchro4", 211),
          ("vtucSynchro5", 218),
          ("vtucSynchro6", 220),
          ("vtucTeq", 213),
          ("vtucTraining1", 210),
          ("vtucTraining2", 217),
          ("vturChDiscov1", 302),
          ("vturChDiscov2", 307),
          ("vturEct", 314),
          ("vturG9941", 300),
          ("vturLineprobe", 304),
          ("vturMedley", 318),
          ("vturPeriodic1", 305),
          ("vturPeriodic2", 315),
          ("vturQuiet1", 301),
          ("vturQuiet2", 309),
          ("vturQuiet3", 313),
          ("vturShowtime", 320),
          ("vturSynchro1", 303),
          ("vturSynchro2", 306),
          ("vturSynchro3", 308),
          ("vturSynchro4", 311),
          ("vturSynchro5", 317),
          ("vturSynchro6", 319),
          ("vturTeq", 312),
          ("vturTraining1", 310),
          ("vturTraining2", 316))
    )



class Xdsl2LineStatus(Bits, TextualConvention):
    status = "current"


class Xdsl2ChInpReport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inpComputedUsingFormula", 1),
          ("inpEstimatedByXtur", 2))
    )



class Xdsl2ChAtmStatus(Bits, TextualConvention):
    status = "current"


class Xdsl2ChPtmStatus(Bits, TextualConvention):
    status = "current"


class Xdsl2UpboKLF(Integer32, TextualConvention):
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
        *(("auto", 1),
          ("disableUpbo", 3),
          ("override", 2))
    )



class Xdsl2BandUs(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              7,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("us1", 5),
          ("us2", 7),
          ("us3", 9),
          ("us4", 11))
    )



class Xdsl2LinePsdMaskSelectUs(Integer32, TextualConvention):
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
        *(("adlu32Eu32", 1),
          ("adlu36Eu36", 2),
          ("adlu40Eu40", 3),
          ("adlu44Eu44", 4),
          ("adlu48Eu48", 5),
          ("adlu52Eu52", 6),
          ("adlu56Eu56", 7),
          ("adlu60Eu60", 8),
          ("adlu64Eu64", 9))
    )



class Xdsl2LineCeFlag(Bits, TextualConvention):
    status = "current"


class Xdsl2LineSnrMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("virtualNoiseDisabled", 1),
          ("virtualNoiseEnabled", 2))
    )



class Xdsl2LineTxRefVnDs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )



class Xdsl2LineTxRefVnUs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )



class Xdsl2BitsAlloc(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class Xdsl2MrefPsdDs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 192),
    )



class Xdsl2MrefPsdUs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VDSL2-LINE-TC-MIB",
    **{"Xdsl2Unit": Xdsl2Unit,
       "Xdsl2Direction": Xdsl2Direction,
       "Xdsl2Band": Xdsl2Band,
       "Xdsl2TransmissionModeType": Xdsl2TransmissionModeType,
       "Xdsl2RaMode": Xdsl2RaMode,
       "Xdsl2InitResult": Xdsl2InitResult,
       "Xdsl2OperationModes": Xdsl2OperationModes,
       "Xdsl2PowerMngState": Xdsl2PowerMngState,
       "Xdsl2ConfPmsForce": Xdsl2ConfPmsForce,
       "Xdsl2LinePmMode": Xdsl2LinePmMode,
       "Xdsl2LineLdsf": Xdsl2LineLdsf,
       "Xdsl2LdsfResult": Xdsl2LdsfResult,
       "Xdsl2LineBpsc": Xdsl2LineBpsc,
       "Xdsl2BpscResult": Xdsl2BpscResult,
       "Xdsl2LineReset": Xdsl2LineReset,
       "Xdsl2LineProfiles": Xdsl2LineProfiles,
       "Xdsl2LineClassMask": Xdsl2LineClassMask,
       "Xdsl2LineLimitMask": Xdsl2LineLimitMask,
       "Xdsl2LineUs0Disable": Xdsl2LineUs0Disable,
       "Xdsl2LineUs0Mask": Xdsl2LineUs0Mask,
       "Xdsl2SymbolProtection": Xdsl2SymbolProtection,
       "Xdsl2SymbolProtection8": Xdsl2SymbolProtection8,
       "Xdsl2MaxBer": Xdsl2MaxBer,
       "Xdsl2ChInitPolicy": Xdsl2ChInitPolicy,
       "Xdsl2ScMaskDs": Xdsl2ScMaskDs,
       "Xdsl2ScMaskUs": Xdsl2ScMaskUs,
       "Xdsl2CarMask": Xdsl2CarMask,
       "Xdsl2RfiBands": Xdsl2RfiBands,
       "Xdsl2PsdMaskDs": Xdsl2PsdMaskDs,
       "Xdsl2PsdMaskUs": Xdsl2PsdMaskUs,
       "Xdsl2Tssi": Xdsl2Tssi,
       "Xdsl2LastTransmittedState": Xdsl2LastTransmittedState,
       "Xdsl2LineStatus": Xdsl2LineStatus,
       "Xdsl2ChInpReport": Xdsl2ChInpReport,
       "Xdsl2ChAtmStatus": Xdsl2ChAtmStatus,
       "Xdsl2ChPtmStatus": Xdsl2ChPtmStatus,
       "Xdsl2UpboKLF": Xdsl2UpboKLF,
       "Xdsl2BandUs": Xdsl2BandUs,
       "Xdsl2LinePsdMaskSelectUs": Xdsl2LinePsdMaskSelectUs,
       "Xdsl2LineCeFlag": Xdsl2LineCeFlag,
       "Xdsl2LineSnrMode": Xdsl2LineSnrMode,
       "Xdsl2LineTxRefVnDs": Xdsl2LineTxRefVnDs,
       "Xdsl2LineTxRefVnUs": Xdsl2LineTxRefVnUs,
       "Xdsl2BitsAlloc": Xdsl2BitsAlloc,
       "Xdsl2MrefPsdDs": Xdsl2MrefPsdDs,
       "Xdsl2MrefPsdUs": Xdsl2MrefPsdUs,
       "vdsl2TCMIB": vdsl2TCMIB}
)
