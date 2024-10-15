# SNMP MIB module (SUB10SYSTEMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUB10SYSTEMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:28 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

sub10Systems = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39003)
)
sub10Systems.setRevisions(
        ("2015-06-03 00:00",
         "2015-04-07 00:00",
         "2015-03-30 00:00",
         "2015-03-26 00:00",
         "2015-03-06 00:00",
         "2015-03-05 00:00",
         "2015-02-27 00:00",
         "2014-12-18 00:00",
         "2014-11-19 00:00",
         "2014-04-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Sub10EthInterfaceIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )



class Sub10EntryStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("entryInUse", 1),
          ("entryNotInUse", 2))
    )



class Sub10State(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stateDisabled", 0),
          ("stateEnabled", 1))
    )



class Sub10UnitType(Integer32, TextualConvention):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("baseband1000A", 2),
          ("baseband1000B", 3),
          ("baseband100A", 0),
          ("baseband100B", 1),
          ("e1000FCCA", 14),
          ("e1000FCCB", 15),
          ("e1000ROWA", 12),
          ("e1000ROWB", 13),
          ("v1000FCCA", 10),
          ("v1000FCCB2", 11),
          ("v1000ROWA", 8),
          ("v1000ROWB", 9),
          ("v100FCCA", 6),
          ("v100FCCB", 7),
          ("v100ROWA", 4),
          ("v100ROWB", 5))
    )



class Sub10TerminalType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("terminalA", 0),
          ("terminalB", 1))
    )



class Sub10Availability(Integer32, TextualConvention):
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
        *(("availabilityHigh", 0),
          ("availabilityLow", 2),
          ("availabilityMedium", 1))
    )



class Sub10AlignmentMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("modeAlignment", 1),
          ("modeNormal", 0))
    )



class Sub10AlignmentModeLock(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("modeLocked", 1),
          ("modeUnlocked", 0))
    )



class Sub10OperStatus(Integer32, TextualConvention):
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
        *(("opStatusDormant", 5),
          ("opStatusDown", 2),
          ("opStatusLowerLayerDown", 7),
          ("opStatusNotPresent", 6),
          ("opStatusTesting", 3),
          ("opStatusUnknown", 4),
          ("opStatusUp", 1))
    )



class Sub10Duplex(Integer32, TextualConvention):
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
        *(("fullDuplex", 2),
          ("halfDuplex", 1),
          ("unknownDuplex", 3))
    )



class Sub10MDIType(Integer32, TextualConvention):
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
        *(("mdi", 1),
          ("mdiUnknown", 3),
          ("mdix", 2))
    )



class Sub10RadioLinkState(Integer32, TextualConvention):
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
        *(("radioLinkStateDown", 0),
          ("radioLinkStateUnknown", 2),
          ("radioLinkStateUp", 1))
    )



class Sub10AlarmName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class Sub10MacAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "17a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )



class Sub10AlarmState(Integer32, TextualConvention):
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
        *(("cleared", 1),
          ("raised", 2),
          ("stateUnknown", 3))
    )



class Sub10DateTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "19a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )



class Sub10AlarmIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )



class Sub10MeasuredObject(Integer32, TextualConvention):
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
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
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
              335)
        )
    )
    namedValues = NamedValues(
        *(("sub10EthStats15mHistPkts1024TMax", 239),
          ("sub10EthStats15mHistPkts128T255", 236),
          ("sub10EthStats15mHistPkts256T511", 237),
          ("sub10EthStats15mHistPkts512T1023", 238),
          ("sub10EthStats15mHistPkts64Octets", 234),
          ("sub10EthStats15mHistPkts65T127", 235),
          ("sub10EthStats15mHistRxAlignErrs", 216),
          ("sub10EthStats15mHistRxBcastFrms", 212),
          ("sub10EthStats15mHistRxCRCErrs", 215),
          ("sub10EthStats15mHistRxFragments", 220),
          ("sub10EthStats15mHistRxGoodFrms", 211),
          ("sub10EthStats15mHistRxJabberFrms", 218),
          ("sub10EthStats15mHistRxMbpsAvg", 242),
          ("sub10EthStats15mHistRxMbpsMax", 241),
          ("sub10EthStats15mHistRxMbpsMin", 240),
          ("sub10EthStats15mHistRxMcastFrms", 213),
          ("sub10EthStats15mHistRxOctets", 210),
          ("sub10EthStats15mHistRxOversized", 217),
          ("sub10EthStats15mHistRxPauseFrms", 214),
          ("sub10EthStats15mHistRxSOFOvrns", 221),
          ("sub10EthStats15mHistRxUndersized", 219),
          ("sub10EthStats15mHistTxBcastFrms", 224),
          ("sub10EthStats15mHistTxCSenseErrs", 233),
          ("sub10EthStats15mHistTxCollsn", 228),
          ("sub10EthStats15mHistTxDeferred", 227),
          ("sub10EthStats15mHistTxExsvCollsn", 231),
          ("sub10EthStats15mHistTxGoodFrms", 223),
          ("sub10EthStats15mHistTxLtCollsn", 232),
          ("sub10EthStats15mHistTxMbpsAvg", 245),
          ("sub10EthStats15mHistTxMbpsMax", 244),
          ("sub10EthStats15mHistTxMbpsMin", 243),
          ("sub10EthStats15mHistTxMcastFrms", 225),
          ("sub10EthStats15mHistTxMlplCollsn", 230),
          ("sub10EthStats15mHistTxOctets", 222),
          ("sub10EthStats15mHistTxPauseFrms", 226),
          ("sub10EthStats15mHistTxSnglCollsn", 229),
          ("sub10EthStats1dHistPkts1024TMax", 329),
          ("sub10EthStats1dHistPkts128T255", 326),
          ("sub10EthStats1dHistPkts256T511", 327),
          ("sub10EthStats1dHistPkts512T1023", 328),
          ("sub10EthStats1dHistPkts64Octets", 324),
          ("sub10EthStats1dHistPkts65T127", 325),
          ("sub10EthStats1dHistRxAlignErrs", 306),
          ("sub10EthStats1dHistRxBcastFrms", 302),
          ("sub10EthStats1dHistRxCRCErrs", 305),
          ("sub10EthStats1dHistRxFragments", 310),
          ("sub10EthStats1dHistRxGoodFrms", 301),
          ("sub10EthStats1dHistRxJabberFrms", 308),
          ("sub10EthStats1dHistRxMbpsAvg", 332),
          ("sub10EthStats1dHistRxMbpsMax", 331),
          ("sub10EthStats1dHistRxMbpsMin", 330),
          ("sub10EthStats1dHistRxMcastFrms", 303),
          ("sub10EthStats1dHistRxOctets", 300),
          ("sub10EthStats1dHistRxOversized", 307),
          ("sub10EthStats1dHistRxPauseFrms", 304),
          ("sub10EthStats1dHistRxSOFOvrns", 311),
          ("sub10EthStats1dHistRxUndersized", 309),
          ("sub10EthStats1dHistTxBcastFrms", 314),
          ("sub10EthStats1dHistTxCSenseErrs", 323),
          ("sub10EthStats1dHistTxCollsn", 318),
          ("sub10EthStats1dHistTxDeferred", 317),
          ("sub10EthStats1dHistTxExsvCollsn", 321),
          ("sub10EthStats1dHistTxGoodFrms", 313),
          ("sub10EthStats1dHistTxLtCollsn", 322),
          ("sub10EthStats1dHistTxMbpsAvg", 335),
          ("sub10EthStats1dHistTxMbpsMax", 334),
          ("sub10EthStats1dHistTxMbpsMin", 333),
          ("sub10EthStats1dHistTxMcastFrms", 315),
          ("sub10EthStats1dHistTxMlplCollsn", 320),
          ("sub10EthStats1dHistTxOctets", 312),
          ("sub10EthStats1dHistTxPauseFrms", 316),
          ("sub10EthStats1dHistTxSnglCollsn", 319),
          ("sub10EthStats1mHistPkts1024TMax", 189),
          ("sub10EthStats1mHistPkts128T255", 186),
          ("sub10EthStats1mHistPkts256T511", 187),
          ("sub10EthStats1mHistPkts512T1023", 188),
          ("sub10EthStats1mHistPkts64Octets", 184),
          ("sub10EthStats1mHistPkts65T127", 185),
          ("sub10EthStats1mHistRxAlignErrs", 166),
          ("sub10EthStats1mHistRxBcastFrms", 162),
          ("sub10EthStats1mHistRxCRCErrs", 165),
          ("sub10EthStats1mHistRxFragments", 170),
          ("sub10EthStats1mHistRxGoodFrms", 161),
          ("sub10EthStats1mHistRxJabberFrms", 168),
          ("sub10EthStats1mHistRxMbpsAvg", 192),
          ("sub10EthStats1mHistRxMbpsMax", 191),
          ("sub10EthStats1mHistRxMbpsMin", 190),
          ("sub10EthStats1mHistRxMcastFrms", 163),
          ("sub10EthStats1mHistRxOctets", 160),
          ("sub10EthStats1mHistRxOversized", 167),
          ("sub10EthStats1mHistRxPauseFrms", 164),
          ("sub10EthStats1mHistRxSOFOvrns", 171),
          ("sub10EthStats1mHistRxUndersized", 169),
          ("sub10EthStats1mHistTxBcastFrms", 174),
          ("sub10EthStats1mHistTxCSenseErrs", 183),
          ("sub10EthStats1mHistTxCollsn", 178),
          ("sub10EthStats1mHistTxDeferred", 177),
          ("sub10EthStats1mHistTxExsvCollsn", 181),
          ("sub10EthStats1mHistTxGoodFrms", 173),
          ("sub10EthStats1mHistTxLtCollsn", 182),
          ("sub10EthStats1mHistTxMbpsAvg", 195),
          ("sub10EthStats1mHistTxMbpsMax", 194),
          ("sub10EthStats1mHistTxMbpsMin", 193),
          ("sub10EthStats1mHistTxMcastFrms", 175),
          ("sub10EthStats1mHistTxMlplCollsn", 180),
          ("sub10EthStats1mHistTxOctets", 172),
          ("sub10EthStats1mHistTxPauseFrms", 176),
          ("sub10EthStats1mHistTxSnglCollsn", 179),
          ("sub10EthStatsCurrRxMbps", 140),
          ("sub10EthStatsCurrRxMbpsAvg", 144),
          ("sub10EthStatsCurrRxMbpsMax", 143),
          ("sub10EthStatsCurrRxMbpsMin", 142),
          ("sub10EthStatsCurrTxMbps", 141),
          ("sub10EthStatsCurrTxMbpsAvg", 147),
          ("sub10EthStatsCurrTxMbpsMax", 146),
          ("sub10EthStatsCurrTxMbpsMin", 145),
          ("sub10RadioLclLinkStatus", 10),
          ("sub10RadioLclLnkLoss", 4),
          ("sub10RadioLclRxModulationMode", 11),
          ("sub10RadioLclRxPower", 2),
          ("sub10RadioLclTxModulationMode", 12),
          ("sub10RadioLclTxPower", 5),
          ("sub10RadioLclVectErr", 3),
          ("sub10RadioMgmtAPCMode", 7),
          ("sub10RadioMgmtAlignmentMode", 9),
          ("sub10RadioMgmtModulationMode", 8),
          ("sub10RadioMgmtTxRxFreq", 6),
          ("sub10RadioStats15mHist8PSKToQPSK", 114),
          ("sub10RadioStats15mHistAFERAvg", 107),
          ("sub10RadioStats15mHistAFERMax", 106),
          ("sub10RadioStats15mHistAFERMin", 105),
          ("sub10RadioStats15mHistLnkLossAvg", 101),
          ("sub10RadioStats15mHistLnkLossMax", 100),
          ("sub10RadioStats15mHistLnkLossMin", 99),
          ("sub10RadioStats15mHistMWUTempAvg", 104),
          ("sub10RadioStats15mHistMWUTempMax", 103),
          ("sub10RadioStats15mHistMWUTempMin", 102),
          ("sub10RadioStats15mHistQPSKTo8PSK", 113),
          ("sub10RadioStats15mHistRx8PSK", 116),
          ("sub10RadioStats15mHistRxBadFrms", 112),
          ("sub10RadioStats15mHistRxMgmtPkts", 110),
          ("sub10RadioStats15mHistRxPkts", 108),
          ("sub10RadioStats15mHistRxPowerAvg", 95),
          ("sub10RadioStats15mHistRxPowerMax", 94),
          ("sub10RadioStats15mHistRxPowerMin", 93),
          ("sub10RadioStats15mHistRxQPSK", 115),
          ("sub10RadioStats15mHistTx8PSK", 118),
          ("sub10RadioStats15mHistTxMgmtPkts", 111),
          ("sub10RadioStats15mHistTxPkts", 109),
          ("sub10RadioStats15mHistTxPowerAvg", 92),
          ("sub10RadioStats15mHistTxPowerMax", 91),
          ("sub10RadioStats15mHistTxPowerMin", 90),
          ("sub10RadioStats15mHistTxQPSK", 117),
          ("sub10RadioStats15mHistVectErrAvg", 98),
          ("sub10RadioStats15mHistVectErrMax", 97),
          ("sub10RadioStats15mHistVectErrMin", 96),
          ("sub10RadioStats1dHist8PSKToQPSK", 284),
          ("sub10RadioStats1dHistAFERAvg", 277),
          ("sub10RadioStats1dHistAFERMax", 276),
          ("sub10RadioStats1dHistAFERMin", 275),
          ("sub10RadioStats1dHistLnkLossAvg", 271),
          ("sub10RadioStats1dHistLnkLossMax", 270),
          ("sub10RadioStats1dHistLnkLossMin", 269),
          ("sub10RadioStats1dHistMWUTempAvg", 274),
          ("sub10RadioStats1dHistMWUTempMax", 273),
          ("sub10RadioStats1dHistMWUTempMin", 272),
          ("sub10RadioStats1dHistQPSKTo8PSK", 283),
          ("sub10RadioStats1dHistRx8PSK", 286),
          ("sub10RadioStats1dHistRxBadFrms", 282),
          ("sub10RadioStats1dHistRxMgmtPkts", 280),
          ("sub10RadioStats1dHistRxPkts", 278),
          ("sub10RadioStats1dHistRxPowerAvg", 265),
          ("sub10RadioStats1dHistRxPowerMax", 264),
          ("sub10RadioStats1dHistRxPowerMin", 263),
          ("sub10RadioStats1dHistRxQPSK", 285),
          ("sub10RadioStats1dHistTx8PSK", 288),
          ("sub10RadioStats1dHistTxMgmtPkts", 281),
          ("sub10RadioStats1dHistTxPkts", 279),
          ("sub10RadioStats1dHistTxPowerAvg", 262),
          ("sub10RadioStats1dHistTxPowerMax", 261),
          ("sub10RadioStats1dHistTxPowerMin", 260),
          ("sub10RadioStats1dHistTxQPSK", 287),
          ("sub10RadioStats1dHistVectErrAvg", 268),
          ("sub10RadioStats1dHistVectErrMax", 267),
          ("sub10RadioStats1dHistVectErrMin", 266),
          ("sub10RadioStats1mHist8PSKToQPSK", 74),
          ("sub10RadioStats1mHistAFERAvg", 67),
          ("sub10RadioStats1mHistAFERMax", 66),
          ("sub10RadioStats1mHistAFERMin", 65),
          ("sub10RadioStats1mHistLnkLossAvg", 61),
          ("sub10RadioStats1mHistLnkLossMax", 60),
          ("sub10RadioStats1mHistLnkLossMin", 59),
          ("sub10RadioStats1mHistMWUTempAvg", 64),
          ("sub10RadioStats1mHistMWUTempMax", 63),
          ("sub10RadioStats1mHistMWUTempMin", 62),
          ("sub10RadioStats1mHistQPSKTo8PSK", 73),
          ("sub10RadioStats1mHistRx8PSK", 76),
          ("sub10RadioStats1mHistRxBadFrms", 72),
          ("sub10RadioStats1mHistRxMgmtPkts", 70),
          ("sub10RadioStats1mHistRxPkts", 68),
          ("sub10RadioStats1mHistRxPowerAvg", 55),
          ("sub10RadioStats1mHistRxPowerMax", 54),
          ("sub10RadioStats1mHistRxPowerMin", 53),
          ("sub10RadioStats1mHistRxQPSK", 75),
          ("sub10RadioStats1mHistTx8PSK", 78),
          ("sub10RadioStats1mHistTxMgmtPkts", 71),
          ("sub10RadioStats1mHistTxPkts", 69),
          ("sub10RadioStats1mHistTxPowerAvg", 52),
          ("sub10RadioStats1mHistTxPowerMax", 51),
          ("sub10RadioStats1mHistTxPowerMin", 50),
          ("sub10RadioStats1mHistTxQPSK", 77),
          ("sub10RadioStats1mHistVectErrAvg", 58),
          ("sub10RadioStats1mHistVectErrMax", 57),
          ("sub10RadioStats1mHistVectErrMin", 56),
          ("sub10RadioStatsCurrAFERAvg", 37),
          ("sub10RadioStatsCurrAFERMax", 36),
          ("sub10RadioStatsCurrAFERMin", 35),
          ("sub10RadioStatsCurrLnkLossAvg", 31),
          ("sub10RadioStatsCurrLnkLossMax", 30),
          ("sub10RadioStatsCurrLnkLossMin", 29),
          ("sub10RadioStatsCurrMWUTempAvg", 34),
          ("sub10RadioStatsCurrMWUTempMax", 33),
          ("sub10RadioStatsCurrMWUTempMin", 32),
          ("sub10RadioStatsCurrRxPowerAvg", 25),
          ("sub10RadioStatsCurrRxPowerMax", 24),
          ("sub10RadioStatsCurrRxPowerMin", 23),
          ("sub10RadioStatsCurrTxPowerAvg", 22),
          ("sub10RadioStatsCurrTxPowerMax", 21),
          ("sub10RadioStatsCurrTxPowerMin", 20),
          ("sub10RadioStatsCurrVectErrAvg", 28),
          ("sub10RadioStatsCurrVectErrMax", 27),
          ("sub10RadioStatsCurrVectErrMin", 26),
          ("sub10UnitLclMWUTemperature", 1))
    )



class Sub10AlarmSeverity(Integer32, TextualConvention):
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )



class Sub10AlarmOperation(Integer32, TextualConvention):
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
        *(("equal", 5),
          ("greaterThan", 2),
          ("greaterThanOrEqual", 4),
          ("lessThan", 1),
          ("lessThanOrEqual", 3),
          ("notEqual", 6))
    )



class Sub10AlarmType(Integer32, TextualConvention):
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
        *(("sub10EthernetAlarm", 2),
          ("sub10RadioAlarm", 3),
          ("sub10UnitAlarm", 1))
    )



class Sub10NTPSyncStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ntpInSync", 1),
          ("ntpOutOfSync", 0))
    )



class Sub10VlanId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class Sub10VlanTagAction(Integer32, TextualConvention):
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
        *(("drop", 3),
          ("tag", 2),
          ("tagActionNone", 0),
          ("untag", 1))
    )



class Sub10VlanPriority(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class Sub10QoSQueue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class Sub10TxPowerLimit(Integer32, TextualConvention):
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
        *(("txPowerLimitMinus12", 4),
          ("txPowerLimitMinus15", 5),
          ("txPowerLimitMinus3", 1),
          ("txPowerLimitMinus6", 2),
          ("txPowerLimitMinus9", 3),
          ("txPowerLimitNone", 0))
    )



class Sub10RadioDataRate(Integer32, TextualConvention):
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
        *(("radioDataRate100", 4),
          ("radioDataRate1000", 0),
          ("radioDataRate300", 3),
          ("radioDataRate500", 2),
          ("radioDataRate700", 1))
    )



class Sub10UserGroup(Integer32, TextualConvention):
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
        *(("administration", 2),
          ("engineer", 4),
          ("maintenance", 3),
          ("operation", 1))
    )



class Sub10Snmpv3SecurityLevel(Integer32, TextualConvention):
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
        *(("authNoPriv", 2),
          ("authPriv", 3),
          ("noAuthNoPriv", 1))
    )



class Sub10Snmpv3AuthProtocol(Integer32, TextualConvention):
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
        *(("md5", 2),
          ("noAuth", 1),
          ("sha1", 3))
    )



class Sub10Snmpv3PrivProtocol(Integer32, TextualConvention):
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
        *(("aes", 3),
          ("des", 2),
          ("noPriv", 1))
    )



class Sub10MWUType(Integer32, TextualConvention):
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
        *(("mwuTypeEBand", 2),
          ("mwuTypeNone", 0),
          ("mwuTypeVBand", 1))
    )



class Sub10FirmwareBank(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )



class Sub10StatsGroup(Integer32, TextualConvention):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("statsGroupAll", 2),
          ("statsGroupEthernet15m", 11),
          ("statsGroupEthernet1d", 12),
          ("statsGroupEthernet1m", 10),
          ("statsGroupEthernet1s", 9),
          ("statsGroupEthernetCurr", 8),
          ("statsGroupNone", 1),
          ("statsGroupRadio15m", 6),
          ("statsGroupRadio1d", 7),
          ("statsGroupRadio1m", 5),
          ("statsGroupRadio1s", 4),
          ("statsGroupRadioCurr", 3),
          ("statsGroupRadioCurr60s", 13))
    )



class Sub10ThroughputMbps(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class Sub10ModulationMode(Integer32, TextualConvention):
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
        *(("mode8psk", 2),
          ("modebpsk", 0),
          ("modeqpsk", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Sub10Notifications_ObjectIdentity = ObjectIdentity
sub10Notifications = _Sub10Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 0)
)
_Sub10Unit_ObjectIdentity = ObjectIdentity
sub10Unit = _Sub10Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3)
)
_Sub10UnitStatus_ObjectIdentity = ObjectIdentity
sub10UnitStatus = _Sub10UnitStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1)
)
_Sub10UnitLocalStatus_ObjectIdentity = ObjectIdentity
sub10UnitLocalStatus = _Sub10UnitLocalStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1)
)
_Sub10UnitLclTime_Type = Sub10DateTime
_Sub10UnitLclTime_Object = MibScalar
sub10UnitLclTime = _Sub10UnitLclTime_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 1),
    _Sub10UnitLclTime_Type()
)
sub10UnitLclTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclTime.setStatus("current")
_Sub10UnitLclUnitType_Type = Sub10UnitType
_Sub10UnitLclUnitType_Object = MibScalar
sub10UnitLclUnitType = _Sub10UnitLclUnitType_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 2),
    _Sub10UnitLclUnitType_Type()
)
sub10UnitLclUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclUnitType.setStatus("current")
_Sub10UnitLclDescription_Type = DisplayString
_Sub10UnitLclDescription_Object = MibScalar
sub10UnitLclDescription = _Sub10UnitLclDescription_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 3),
    _Sub10UnitLclDescription_Type()
)
sub10UnitLclDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclDescription.setStatus("current")


class _Sub10UnitLclHWSerialNumber_Type(OctetString):
    """Custom type sub10UnitLclHWSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_Sub10UnitLclHWSerialNumber_Type.__name__ = "OctetString"
_Sub10UnitLclHWSerialNumber_Object = MibScalar
sub10UnitLclHWSerialNumber = _Sub10UnitLclHWSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 4),
    _Sub10UnitLclHWSerialNumber_Type()
)
sub10UnitLclHWSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclHWSerialNumber.setStatus("current")


class _Sub10UnitLclTerminalName_Type(OctetString):
    """Custom type sub10UnitLclTerminalName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Sub10UnitLclTerminalName_Type.__name__ = "OctetString"
_Sub10UnitLclTerminalName_Object = MibScalar
sub10UnitLclTerminalName = _Sub10UnitLclTerminalName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 5),
    _Sub10UnitLclTerminalName_Type()
)
sub10UnitLclTerminalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclTerminalName.setStatus("current")
_Sub10UnitLclTerminalType_Type = Sub10TerminalType
_Sub10UnitLclTerminalType_Object = MibScalar
sub10UnitLclTerminalType = _Sub10UnitLclTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 6),
    _Sub10UnitLclTerminalType_Type()
)
sub10UnitLclTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclTerminalType.setStatus("current")


class _Sub10UnitLclLinkName_Type(OctetString):
    """Custom type sub10UnitLclLinkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Sub10UnitLclLinkName_Type.__name__ = "OctetString"
_Sub10UnitLclLinkName_Object = MibScalar
sub10UnitLclLinkName = _Sub10UnitLclLinkName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 7),
    _Sub10UnitLclLinkName_Type()
)
sub10UnitLclLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclLinkName.setStatus("current")


class _Sub10UnitLclLinkId_Type(OctetString):
    """Custom type sub10UnitLclLinkId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10UnitLclLinkId_Type.__name__ = "OctetString"
_Sub10UnitLclLinkId_Object = MibScalar
sub10UnitLclLinkId = _Sub10UnitLclLinkId_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 8),
    _Sub10UnitLclLinkId_Type()
)
sub10UnitLclLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclLinkId.setStatus("current")
_Sub10UnitLclSiteName_Type = DisplayString
_Sub10UnitLclSiteName_Object = MibScalar
sub10UnitLclSiteName = _Sub10UnitLclSiteName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 9),
    _Sub10UnitLclSiteName_Type()
)
sub10UnitLclSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclSiteName.setStatus("current")
_Sub10UnitLclFirmwareLoadedBank_Type = Sub10FirmwareBank
_Sub10UnitLclFirmwareLoadedBank_Object = MibScalar
sub10UnitLclFirmwareLoadedBank = _Sub10UnitLclFirmwareLoadedBank_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 10),
    _Sub10UnitLclFirmwareLoadedBank_Type()
)
sub10UnitLclFirmwareLoadedBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclFirmwareLoadedBank.setStatus("current")


class _Sub10UnitLclFirmwareVersion_Type(OctetString):
    """Custom type sub10UnitLclFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Sub10UnitLclFirmwareVersion_Type.__name__ = "OctetString"
_Sub10UnitLclFirmwareVersion_Object = MibScalar
sub10UnitLclFirmwareVersion = _Sub10UnitLclFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 11),
    _Sub10UnitLclFirmwareVersion_Type()
)
sub10UnitLclFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclFirmwareVersion.setStatus("current")


class _Sub10UnitLclIpAddress_Type(OctetString):
    """Custom type sub10UnitLclIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )


_Sub10UnitLclIpAddress_Type.__name__ = "OctetString"
_Sub10UnitLclIpAddress_Object = MibScalar
sub10UnitLclIpAddress = _Sub10UnitLclIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 12),
    _Sub10UnitLclIpAddress_Type()
)
sub10UnitLclIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclIpAddress.setStatus("current")


class _Sub10UnitLclMWUTemperature_Type(Integer32):
    """Custom type sub10UnitLclMWUTemperature based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10UnitLclMWUTemperature_Type.__name__ = "Integer32"
_Sub10UnitLclMWUTemperature_Object = MibScalar
sub10UnitLclMWUTemperature = _Sub10UnitLclMWUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 13),
    _Sub10UnitLclMWUTemperature_Type()
)
sub10UnitLclMWUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclMWUTemperature.setStatus("current")


class _Sub10UnitLclNTPSyncStatus_Type(Sub10NTPSyncStatus):
    """Custom type sub10UnitLclNTPSyncStatus based on Sub10NTPSyncStatus"""


_Sub10UnitLclNTPSyncStatus_Object = MibScalar
sub10UnitLclNTPSyncStatus = _Sub10UnitLclNTPSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 14),
    _Sub10UnitLclNTPSyncStatus_Type()
)
sub10UnitLclNTPSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclNTPSyncStatus.setStatus("current")
_Sub10UnitLclAlarmStateTable_Object = MibTable
sub10UnitLclAlarmStateTable = _Sub10UnitLclAlarmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 15)
)
if mibBuilder.loadTexts:
    sub10UnitLclAlarmStateTable.setStatus("current")
_Sub10UnitLclAlarmStateEntry_Object = MibTableRow
sub10UnitLclAlarmStateEntry = _Sub10UnitLclAlarmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 15, 1)
)
sub10UnitLclAlarmStateEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10UnitLclAlarmStateIndex"),
)
if mibBuilder.loadTexts:
    sub10UnitLclAlarmStateEntry.setStatus("current")
_Sub10UnitLclAlarmStateIndex_Type = Sub10AlarmIndex
_Sub10UnitLclAlarmStateIndex_Object = MibTableColumn
sub10UnitLclAlarmStateIndex = _Sub10UnitLclAlarmStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 15, 1, 1),
    _Sub10UnitLclAlarmStateIndex_Type()
)
sub10UnitLclAlarmStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10UnitLclAlarmStateIndex.setStatus("current")


class _Sub10UnitLclAlarmState_Type(Sub10AlarmState):
    """Custom type sub10UnitLclAlarmState based on Sub10AlarmState"""


_Sub10UnitLclAlarmState_Object = MibTableColumn
sub10UnitLclAlarmState = _Sub10UnitLclAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 15, 1, 2),
    _Sub10UnitLclAlarmState_Type()
)
sub10UnitLclAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclAlarmState.setStatus("current")
_Sub10UnitLclAlarmStateTime_Type = Sub10DateTime
_Sub10UnitLclAlarmStateTime_Object = MibTableColumn
sub10UnitLclAlarmStateTime = _Sub10UnitLclAlarmStateTime_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 15, 1, 3),
    _Sub10UnitLclAlarmStateTime_Type()
)
sub10UnitLclAlarmStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclAlarmStateTime.setStatus("current")
_Sub10UnitLclRadioDataRate_Type = Sub10RadioDataRate
_Sub10UnitLclRadioDataRate_Object = MibScalar
sub10UnitLclRadioDataRate = _Sub10UnitLclRadioDataRate_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 16),
    _Sub10UnitLclRadioDataRate_Type()
)
sub10UnitLclRadioDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclRadioDataRate.setStatus("current")
_Sub10UnitLclMWUType_Type = Sub10MWUType
_Sub10UnitLclMWUType_Object = MibScalar
sub10UnitLclMWUType = _Sub10UnitLclMWUType_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 17),
    _Sub10UnitLclMWUType_Type()
)
sub10UnitLclMWUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclMWUType.setStatus("current")


class _Sub10UnitLclFPGAVersion_Type(OctetString):
    """Custom type sub10UnitLclFPGAVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10UnitLclFPGAVersion_Type.__name__ = "OctetString"
_Sub10UnitLclFPGAVersion_Object = MibScalar
sub10UnitLclFPGAVersion = _Sub10UnitLclFPGAVersion_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 1, 18),
    _Sub10UnitLclFPGAVersion_Type()
)
sub10UnitLclFPGAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitLclFPGAVersion.setStatus("current")
_Sub10UnitRemoteStatus_ObjectIdentity = ObjectIdentity
sub10UnitRemoteStatus = _Sub10UnitRemoteStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 2)
)
_Sub10UnitRmtUnitType_Type = Sub10UnitType
_Sub10UnitRmtUnitType_Object = MibScalar
sub10UnitRmtUnitType = _Sub10UnitRmtUnitType_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 2, 1),
    _Sub10UnitRmtUnitType_Type()
)
sub10UnitRmtUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitRmtUnitType.setStatus("current")
_Sub10UnitRmtTime_Type = Sub10DateTime
_Sub10UnitRmtTime_Object = MibScalar
sub10UnitRmtTime = _Sub10UnitRmtTime_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 2, 2),
    _Sub10UnitRmtTime_Type()
)
sub10UnitRmtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitRmtTime.setStatus("current")


class _Sub10UnitRmtTerminalName_Type(OctetString):
    """Custom type sub10UnitRmtTerminalName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Sub10UnitRmtTerminalName_Type.__name__ = "OctetString"
_Sub10UnitRmtTerminalName_Object = MibScalar
sub10UnitRmtTerminalName = _Sub10UnitRmtTerminalName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 2, 3),
    _Sub10UnitRmtTerminalName_Type()
)
sub10UnitRmtTerminalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitRmtTerminalName.setStatus("current")
_Sub10UnitRmtTerminalType_Type = Sub10TerminalType
_Sub10UnitRmtTerminalType_Object = MibScalar
sub10UnitRmtTerminalType = _Sub10UnitRmtTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 2, 4),
    _Sub10UnitRmtTerminalType_Type()
)
sub10UnitRmtTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitRmtTerminalType.setStatus("current")


class _Sub10UnitRmtLinkName_Type(OctetString):
    """Custom type sub10UnitRmtLinkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Sub10UnitRmtLinkName_Type.__name__ = "OctetString"
_Sub10UnitRmtLinkName_Object = MibScalar
sub10UnitRmtLinkName = _Sub10UnitRmtLinkName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 2, 5),
    _Sub10UnitRmtLinkName_Type()
)
sub10UnitRmtLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitRmtLinkName.setStatus("current")


class _Sub10UnitRmtLinkId_Type(OctetString):
    """Custom type sub10UnitRmtLinkId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10UnitRmtLinkId_Type.__name__ = "OctetString"
_Sub10UnitRmtLinkId_Object = MibScalar
sub10UnitRmtLinkId = _Sub10UnitRmtLinkId_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 2, 6),
    _Sub10UnitRmtLinkId_Type()
)
sub10UnitRmtLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitRmtLinkId.setStatus("current")


class _Sub10UnitRmtHWSerialNumber_Type(OctetString):
    """Custom type sub10UnitRmtHWSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_Sub10UnitRmtHWSerialNumber_Type.__name__ = "OctetString"
_Sub10UnitRmtHWSerialNumber_Object = MibScalar
sub10UnitRmtHWSerialNumber = _Sub10UnitRmtHWSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 2, 7),
    _Sub10UnitRmtHWSerialNumber_Type()
)
sub10UnitRmtHWSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitRmtHWSerialNumber.setStatus("current")


class _Sub10UnitRmtFirmwareVersion_Type(OctetString):
    """Custom type sub10UnitRmtFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Sub10UnitRmtFirmwareVersion_Type.__name__ = "OctetString"
_Sub10UnitRmtFirmwareVersion_Object = MibScalar
sub10UnitRmtFirmwareVersion = _Sub10UnitRmtFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 2, 8),
    _Sub10UnitRmtFirmwareVersion_Type()
)
sub10UnitRmtFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitRmtFirmwareVersion.setStatus("current")


class _Sub10UnitRmtIpAddress_Type(OctetString):
    """Custom type sub10UnitRmtIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )


_Sub10UnitRmtIpAddress_Type.__name__ = "OctetString"
_Sub10UnitRmtIpAddress_Object = MibScalar
sub10UnitRmtIpAddress = _Sub10UnitRmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 2, 9),
    _Sub10UnitRmtIpAddress_Type()
)
sub10UnitRmtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitRmtIpAddress.setStatus("current")


class _Sub10UnitRmtMWUTemperature_Type(Integer32):
    """Custom type sub10UnitRmtMWUTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10UnitRmtMWUTemperature_Type.__name__ = "Integer32"
_Sub10UnitRmtMWUTemperature_Object = MibScalar
sub10UnitRmtMWUTemperature = _Sub10UnitRmtMWUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 1, 2, 10),
    _Sub10UnitRmtMWUTemperature_Type()
)
sub10UnitRmtMWUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitRmtMWUTemperature.setStatus("current")
_Sub10UnitMgmt_ObjectIdentity = ObjectIdentity
sub10UnitMgmt = _Sub10UnitMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2)
)
_Sub10UnitMgmtSystem_ObjectIdentity = ObjectIdentity
sub10UnitMgmtSystem = _Sub10UnitMgmtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 1)
)


class _Sub10UnitMgmtTerminalName_Type(OctetString):
    """Custom type sub10UnitMgmtTerminalName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Sub10UnitMgmtTerminalName_Type.__name__ = "OctetString"
_Sub10UnitMgmtTerminalName_Object = MibScalar
sub10UnitMgmtTerminalName = _Sub10UnitMgmtTerminalName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 1, 1),
    _Sub10UnitMgmtTerminalName_Type()
)
sub10UnitMgmtTerminalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtTerminalName.setStatus("current")


class _Sub10UnitMgmtLinkName_Type(OctetString):
    """Custom type sub10UnitMgmtLinkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Sub10UnitMgmtLinkName_Type.__name__ = "OctetString"
_Sub10UnitMgmtLinkName_Object = MibScalar
sub10UnitMgmtLinkName = _Sub10UnitMgmtLinkName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 1, 2),
    _Sub10UnitMgmtLinkName_Type()
)
sub10UnitMgmtLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtLinkName.setStatus("current")


class _Sub10UnitMgmtLinkId_Type(OctetString):
    """Custom type sub10UnitMgmtLinkId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10UnitMgmtLinkId_Type.__name__ = "OctetString"
_Sub10UnitMgmtLinkId_Object = MibScalar
sub10UnitMgmtLinkId = _Sub10UnitMgmtLinkId_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 1, 3),
    _Sub10UnitMgmtLinkId_Type()
)
sub10UnitMgmtLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtLinkId.setStatus("current")
_Sub10UnitMgmtSiteName_Type = DisplayString
_Sub10UnitMgmtSiteName_Object = MibScalar
sub10UnitMgmtSiteName = _Sub10UnitMgmtSiteName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 1, 4),
    _Sub10UnitMgmtSiteName_Type()
)
sub10UnitMgmtSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSiteName.setStatus("current")


class _Sub10UnitMgmtContactName_Type(DisplayString):
    """Custom type sub10UnitMgmtContactName based on DisplayString"""
    defaultValue = OctetString("support@sub10systems.com")


_Sub10UnitMgmtContactName_Object = MibScalar
sub10UnitMgmtContactName = _Sub10UnitMgmtContactName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 1, 5),
    _Sub10UnitMgmtContactName_Type()
)
sub10UnitMgmtContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtContactName.setStatus("current")
_Sub10UnitMgmtIp_ObjectIdentity = ObjectIdentity
sub10UnitMgmtIp = _Sub10UnitMgmtIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 2)
)


class _Sub10UnitMgmtIpMode_Type(Integer32):
    """Custom type sub10UnitMgmtIpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 3),
          ("ipv4", 1),
          ("ipv6", 2))
    )


_Sub10UnitMgmtIpMode_Type.__name__ = "Integer32"
_Sub10UnitMgmtIpMode_Object = MibScalar
sub10UnitMgmtIpMode = _Sub10UnitMgmtIpMode_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 2, 1),
    _Sub10UnitMgmtIpMode_Type()
)
sub10UnitMgmtIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtIpMode.setStatus("current")


class _Sub10UnitMgmtIpAddress_Type(OctetString):
    """Custom type sub10UnitMgmtIpAddress based on OctetString"""
    defaultValue = OctetString("192.168.0.22")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )


_Sub10UnitMgmtIpAddress_Type.__name__ = "OctetString"
_Sub10UnitMgmtIpAddress_Object = MibScalar
sub10UnitMgmtIpAddress = _Sub10UnitMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 2, 2),
    _Sub10UnitMgmtIpAddress_Type()
)
sub10UnitMgmtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtIpAddress.setStatus("current")


class _Sub10UnitMgmtIpSubnetMask_Type(OctetString):
    """Custom type sub10UnitMgmtIpSubnetMask based on OctetString"""
    defaultValue = OctetString("255.255.255.0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )


_Sub10UnitMgmtIpSubnetMask_Type.__name__ = "OctetString"
_Sub10UnitMgmtIpSubnetMask_Object = MibScalar
sub10UnitMgmtIpSubnetMask = _Sub10UnitMgmtIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 2, 3),
    _Sub10UnitMgmtIpSubnetMask_Type()
)
sub10UnitMgmtIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtIpSubnetMask.setStatus("current")


class _Sub10UnitMgmtIpDefGateway_Type(OctetString):
    """Custom type sub10UnitMgmtIpDefGateway based on OctetString"""
    defaultValue = OctetString("192.168.0.1")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )


_Sub10UnitMgmtIpDefGateway_Type.__name__ = "OctetString"
_Sub10UnitMgmtIpDefGateway_Object = MibScalar
sub10UnitMgmtIpDefGateway = _Sub10UnitMgmtIpDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 2, 4),
    _Sub10UnitMgmtIpDefGateway_Type()
)
sub10UnitMgmtIpDefGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtIpDefGateway.setStatus("current")


class _Sub10UnitMgmtIpDHCP_Type(Sub10State):
    """Custom type sub10UnitMgmtIpDHCP based on Sub10State"""


_Sub10UnitMgmtIpDHCP_Object = MibScalar
sub10UnitMgmtIpDHCP = _Sub10UnitMgmtIpDHCP_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 2, 5),
    _Sub10UnitMgmtIpDHCP_Type()
)
sub10UnitMgmtIpDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtIpDHCP.setStatus("current")
_Sub10UnitMgmtVlan_ObjectIdentity = ObjectIdentity
sub10UnitMgmtVlan = _Sub10UnitMgmtVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 3)
)


class _Sub10UnitMgmtVlanState_Type(Sub10State):
    """Custom type sub10UnitMgmtVlanState based on Sub10State"""


_Sub10UnitMgmtVlanState_Object = MibScalar
sub10UnitMgmtVlanState = _Sub10UnitMgmtVlanState_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 3, 1),
    _Sub10UnitMgmtVlanState_Type()
)
sub10UnitMgmtVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtVlanState.setStatus("current")


class _Sub10UnitMgmtVlanId_Type(Sub10VlanId):
    """Custom type sub10UnitMgmtVlanId based on Sub10VlanId"""
    defaultValue = 0


_Sub10UnitMgmtVlanId_Object = MibScalar
sub10UnitMgmtVlanId = _Sub10UnitMgmtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 3, 2),
    _Sub10UnitMgmtVlanId_Type()
)
sub10UnitMgmtVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtVlanId.setStatus("current")


class _Sub10UnitMgmtVlanPriority_Type(Unsigned32):
    """Custom type sub10UnitMgmtVlanPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Sub10UnitMgmtVlanPriority_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtVlanPriority_Object = MibScalar
sub10UnitMgmtVlanPriority = _Sub10UnitMgmtVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 3, 3),
    _Sub10UnitMgmtVlanPriority_Type()
)
sub10UnitMgmtVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtVlanPriority.setStatus("current")


class _Sub10UnitMgmtVlanDSCP_Type(Unsigned32):
    """Custom type sub10UnitMgmtVlanDSCP based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Sub10UnitMgmtVlanDSCP_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtVlanDSCP_Object = MibScalar
sub10UnitMgmtVlanDSCP = _Sub10UnitMgmtVlanDSCP_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 3, 4),
    _Sub10UnitMgmtVlanDSCP_Type()
)
sub10UnitMgmtVlanDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtVlanDSCP.setStatus("current")


class _Sub10UnitMgmtVlanDEI_Type(Sub10State):
    """Custom type sub10UnitMgmtVlanDEI based on Sub10State"""


_Sub10UnitMgmtVlanDEI_Object = MibScalar
sub10UnitMgmtVlanDEI = _Sub10UnitMgmtVlanDEI_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 3, 5),
    _Sub10UnitMgmtVlanDEI_Type()
)
sub10UnitMgmtVlanDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtVlanDEI.setStatus("current")
_Sub10UnitMgmtUsers_ObjectIdentity = ObjectIdentity
sub10UnitMgmtUsers = _Sub10UnitMgmtUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 4)
)


class _Sub10UnitMgmtUsersNumber_Type(Unsigned32):
    """Custom type sub10UnitMgmtUsersNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Sub10UnitMgmtUsersNumber_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtUsersNumber_Object = MibScalar
sub10UnitMgmtUsersNumber = _Sub10UnitMgmtUsersNumber_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 4, 1),
    _Sub10UnitMgmtUsersNumber_Type()
)
sub10UnitMgmtUsersNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtUsersNumber.setStatus("current")
_Sub10UnitMgmtUserTable_Object = MibTable
sub10UnitMgmtUserTable = _Sub10UnitMgmtUserTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 4, 2)
)
if mibBuilder.loadTexts:
    sub10UnitMgmtUserTable.setStatus("current")
_Sub10UnitMgmtUserEntry_Object = MibTableRow
sub10UnitMgmtUserEntry = _Sub10UnitMgmtUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 4, 2, 1)
)
sub10UnitMgmtUserEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10UnitMgmtUserIndex"),
)
if mibBuilder.loadTexts:
    sub10UnitMgmtUserEntry.setStatus("current")


class _Sub10UnitMgmtUserIndex_Type(Unsigned32):
    """Custom type sub10UnitMgmtUserIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Sub10UnitMgmtUserIndex_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtUserIndex_Object = MibTableColumn
sub10UnitMgmtUserIndex = _Sub10UnitMgmtUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 4, 2, 1, 1),
    _Sub10UnitMgmtUserIndex_Type()
)
sub10UnitMgmtUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10UnitMgmtUserIndex.setStatus("current")


class _Sub10UnitMgmtUserRowStatus_Type(RowStatus):
    """Custom type sub10UnitMgmtUserRowStatus based on RowStatus"""


_Sub10UnitMgmtUserRowStatus_Object = MibTableColumn
sub10UnitMgmtUserRowStatus = _Sub10UnitMgmtUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 4, 2, 1, 2),
    _Sub10UnitMgmtUserRowStatus_Type()
)
sub10UnitMgmtUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sub10UnitMgmtUserRowStatus.setStatus("current")


class _Sub10UnitMgmtUserName_Type(OctetString):
    """Custom type sub10UnitMgmtUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Sub10UnitMgmtUserName_Type.__name__ = "OctetString"
_Sub10UnitMgmtUserName_Object = MibTableColumn
sub10UnitMgmtUserName = _Sub10UnitMgmtUserName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 4, 2, 1, 3),
    _Sub10UnitMgmtUserName_Type()
)
sub10UnitMgmtUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtUserName.setStatus("current")


class _Sub10UnitMgmtUserGroup_Type(Sub10UserGroup):
    """Custom type sub10UnitMgmtUserGroup based on Sub10UserGroup"""


_Sub10UnitMgmtUserGroup_Object = MibTableColumn
sub10UnitMgmtUserGroup = _Sub10UnitMgmtUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 4, 2, 1, 4),
    _Sub10UnitMgmtUserGroup_Type()
)
sub10UnitMgmtUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtUserGroup.setStatus("current")


class _Sub10UnitMgmtUserPassword_Type(OctetString):
    """Custom type sub10UnitMgmtUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_Sub10UnitMgmtUserPassword_Type.__name__ = "OctetString"
_Sub10UnitMgmtUserPassword_Object = MibTableColumn
sub10UnitMgmtUserPassword = _Sub10UnitMgmtUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 4, 2, 1, 5),
    _Sub10UnitMgmtUserPassword_Type()
)
sub10UnitMgmtUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtUserPassword.setStatus("current")


class _Sub10UnitMgmtUserPasswordVerify_Type(OctetString):
    """Custom type sub10UnitMgmtUserPasswordVerify based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_Sub10UnitMgmtUserPasswordVerify_Type.__name__ = "OctetString"
_Sub10UnitMgmtUserPasswordVerify_Object = MibTableColumn
sub10UnitMgmtUserPasswordVerify = _Sub10UnitMgmtUserPasswordVerify_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 4, 2, 1, 6),
    _Sub10UnitMgmtUserPasswordVerify_Type()
)
sub10UnitMgmtUserPasswordVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtUserPasswordVerify.setStatus("current")
_Sub10UnitMgmtTime_ObjectIdentity = ObjectIdentity
sub10UnitMgmtTime = _Sub10UnitMgmtTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 5)
)
_Sub10UnitMgmtTimeLocal_Type = Sub10DateTime
_Sub10UnitMgmtTimeLocal_Object = MibScalar
sub10UnitMgmtTimeLocal = _Sub10UnitMgmtTimeLocal_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 5, 1),
    _Sub10UnitMgmtTimeLocal_Type()
)
sub10UnitMgmtTimeLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtTimeLocal.setStatus("current")


class _Sub10UnitMgmtTimeNTPEnabled_Type(Sub10State):
    """Custom type sub10UnitMgmtTimeNTPEnabled based on Sub10State"""


_Sub10UnitMgmtTimeNTPEnabled_Object = MibScalar
sub10UnitMgmtTimeNTPEnabled = _Sub10UnitMgmtTimeNTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 5, 2),
    _Sub10UnitMgmtTimeNTPEnabled_Type()
)
sub10UnitMgmtTimeNTPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtTimeNTPEnabled.setStatus("current")


class _Sub10UnitMgmtTimeNTPServer1_Type(OctetString):
    """Custom type sub10UnitMgmtTimeNTPServer1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_Sub10UnitMgmtTimeNTPServer1_Type.__name__ = "OctetString"
_Sub10UnitMgmtTimeNTPServer1_Object = MibScalar
sub10UnitMgmtTimeNTPServer1 = _Sub10UnitMgmtTimeNTPServer1_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 5, 3),
    _Sub10UnitMgmtTimeNTPServer1_Type()
)
sub10UnitMgmtTimeNTPServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtTimeNTPServer1.setStatus("current")


class _Sub10UnitMgmtTimeNTPServer2_Type(OctetString):
    """Custom type sub10UnitMgmtTimeNTPServer2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_Sub10UnitMgmtTimeNTPServer2_Type.__name__ = "OctetString"
_Sub10UnitMgmtTimeNTPServer2_Object = MibScalar
sub10UnitMgmtTimeNTPServer2 = _Sub10UnitMgmtTimeNTPServer2_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 5, 4),
    _Sub10UnitMgmtTimeNTPServer2_Type()
)
sub10UnitMgmtTimeNTPServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtTimeNTPServer2.setStatus("current")


class _Sub10UnitMgmtTimeNTPPort_Type(Unsigned32):
    """Custom type sub10UnitMgmtTimeNTPPort based on Unsigned32"""
    defaultValue = 123

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Sub10UnitMgmtTimeNTPPort_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtTimeNTPPort_Object = MibScalar
sub10UnitMgmtTimeNTPPort = _Sub10UnitMgmtTimeNTPPort_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 5, 5),
    _Sub10UnitMgmtTimeNTPPort_Type()
)
sub10UnitMgmtTimeNTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtTimeNTPPort.setStatus("current")


class _Sub10UnitMgmtTimeNTPSyncStatus_Type(Sub10NTPSyncStatus):
    """Custom type sub10UnitMgmtTimeNTPSyncStatus based on Sub10NTPSyncStatus"""


_Sub10UnitMgmtTimeNTPSyncStatus_Object = MibScalar
sub10UnitMgmtTimeNTPSyncStatus = _Sub10UnitMgmtTimeNTPSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 5, 6),
    _Sub10UnitMgmtTimeNTPSyncStatus_Type()
)
sub10UnitMgmtTimeNTPSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtTimeNTPSyncStatus.setStatus("current")
_Sub10UnitMgmtDateTime_Type = DateAndTime
_Sub10UnitMgmtDateTime_Object = MibScalar
sub10UnitMgmtDateTime = _Sub10UnitMgmtDateTime_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 5, 7),
    _Sub10UnitMgmtDateTime_Type()
)
sub10UnitMgmtDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtDateTime.setStatus("current")
_Sub10UnitMgmtAlarms_ObjectIdentity = ObjectIdentity
sub10UnitMgmtAlarms = _Sub10UnitMgmtAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6)
)
_Sub10UnitMgmtAlarmTable_Object = MibTable
sub10UnitMgmtAlarmTable = _Sub10UnitMgmtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1)
)
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmTable.setStatus("current")
_Sub10UnitMgmtAlarmEntry_Object = MibTableRow
sub10UnitMgmtAlarmEntry = _Sub10UnitMgmtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1)
)
sub10UnitMgmtAlarmEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmIndex"),
)
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmEntry.setStatus("current")
_Sub10UnitMgmtAlarmIndex_Type = Sub10AlarmIndex
_Sub10UnitMgmtAlarmIndex_Object = MibTableColumn
sub10UnitMgmtAlarmIndex = _Sub10UnitMgmtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 1),
    _Sub10UnitMgmtAlarmIndex_Type()
)
sub10UnitMgmtAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmIndex.setStatus("current")


class _Sub10UnitMgmtAlarmRowStatus_Type(RowStatus):
    """Custom type sub10UnitMgmtAlarmRowStatus based on RowStatus"""


_Sub10UnitMgmtAlarmRowStatus_Object = MibTableColumn
sub10UnitMgmtAlarmRowStatus = _Sub10UnitMgmtAlarmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 2),
    _Sub10UnitMgmtAlarmRowStatus_Type()
)
sub10UnitMgmtAlarmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmRowStatus.setStatus("current")
_Sub10UnitMgmtAlarmName_Type = Sub10AlarmName
_Sub10UnitMgmtAlarmName_Object = MibTableColumn
sub10UnitMgmtAlarmName = _Sub10UnitMgmtAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 3),
    _Sub10UnitMgmtAlarmName_Type()
)
sub10UnitMgmtAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmName.setStatus("current")
_Sub10UnitMgmtAlarmSeverity_Type = Sub10AlarmSeverity
_Sub10UnitMgmtAlarmSeverity_Object = MibTableColumn
sub10UnitMgmtAlarmSeverity = _Sub10UnitMgmtAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 4),
    _Sub10UnitMgmtAlarmSeverity_Type()
)
sub10UnitMgmtAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmSeverity.setStatus("current")
_Sub10UnitMgmtAlarmMeasObject_Type = Sub10MeasuredObject
_Sub10UnitMgmtAlarmMeasObject_Object = MibTableColumn
sub10UnitMgmtAlarmMeasObject = _Sub10UnitMgmtAlarmMeasObject_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 5),
    _Sub10UnitMgmtAlarmMeasObject_Type()
)
sub10UnitMgmtAlarmMeasObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmMeasObject.setStatus("current")


class _Sub10UnitMgmtAlarmMonitorIntvl_Type(Unsigned32):
    """Custom type sub10UnitMgmtAlarmMonitorIntvl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_Sub10UnitMgmtAlarmMonitorIntvl_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtAlarmMonitorIntvl_Object = MibTableColumn
sub10UnitMgmtAlarmMonitorIntvl = _Sub10UnitMgmtAlarmMonitorIntvl_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 6),
    _Sub10UnitMgmtAlarmMonitorIntvl_Type()
)
sub10UnitMgmtAlarmMonitorIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmMonitorIntvl.setStatus("current")


class _Sub10UnitMgmtAlarmRaiseOper_Type(Sub10AlarmOperation):
    """Custom type sub10UnitMgmtAlarmRaiseOper based on Sub10AlarmOperation"""


_Sub10UnitMgmtAlarmRaiseOper_Object = MibTableColumn
sub10UnitMgmtAlarmRaiseOper = _Sub10UnitMgmtAlarmRaiseOper_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 7),
    _Sub10UnitMgmtAlarmRaiseOper_Type()
)
sub10UnitMgmtAlarmRaiseOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmRaiseOper.setStatus("current")


class _Sub10UnitMgmtAlarmRaiseThresh_Type(OctetString):
    """Custom type sub10UnitMgmtAlarmRaiseThresh based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10UnitMgmtAlarmRaiseThresh_Type.__name__ = "OctetString"
_Sub10UnitMgmtAlarmRaiseThresh_Object = MibTableColumn
sub10UnitMgmtAlarmRaiseThresh = _Sub10UnitMgmtAlarmRaiseThresh_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 8),
    _Sub10UnitMgmtAlarmRaiseThresh_Type()
)
sub10UnitMgmtAlarmRaiseThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmRaiseThresh.setStatus("current")


class _Sub10UnitMgmtAlarmClearOper_Type(Sub10AlarmOperation):
    """Custom type sub10UnitMgmtAlarmClearOper based on Sub10AlarmOperation"""


_Sub10UnitMgmtAlarmClearOper_Object = MibTableColumn
sub10UnitMgmtAlarmClearOper = _Sub10UnitMgmtAlarmClearOper_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 9),
    _Sub10UnitMgmtAlarmClearOper_Type()
)
sub10UnitMgmtAlarmClearOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmClearOper.setStatus("current")


class _Sub10UnitMgmtAlarmClearThresh_Type(OctetString):
    """Custom type sub10UnitMgmtAlarmClearThresh based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10UnitMgmtAlarmClearThresh_Type.__name__ = "OctetString"
_Sub10UnitMgmtAlarmClearThresh_Object = MibTableColumn
sub10UnitMgmtAlarmClearThresh = _Sub10UnitMgmtAlarmClearThresh_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 10),
    _Sub10UnitMgmtAlarmClearThresh_Type()
)
sub10UnitMgmtAlarmClearThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmClearThresh.setStatus("current")


class _Sub10UnitMgmtAlarmRaiseIntvls_Type(Unsigned32):
    """Custom type sub10UnitMgmtAlarmRaiseIntvls based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Sub10UnitMgmtAlarmRaiseIntvls_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtAlarmRaiseIntvls_Object = MibTableColumn
sub10UnitMgmtAlarmRaiseIntvls = _Sub10UnitMgmtAlarmRaiseIntvls_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 11),
    _Sub10UnitMgmtAlarmRaiseIntvls_Type()
)
sub10UnitMgmtAlarmRaiseIntvls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmRaiseIntvls.setStatus("current")


class _Sub10UnitMgmtAlarmClearIntvls_Type(Unsigned32):
    """Custom type sub10UnitMgmtAlarmClearIntvls based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Sub10UnitMgmtAlarmClearIntvls_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtAlarmClearIntvls_Object = MibTableColumn
sub10UnitMgmtAlarmClearIntvls = _Sub10UnitMgmtAlarmClearIntvls_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 12),
    _Sub10UnitMgmtAlarmClearIntvls_Type()
)
sub10UnitMgmtAlarmClearIntvls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmClearIntvls.setStatus("current")


class _Sub10UnitMgmtAlarmType_Type(Sub10AlarmType):
    """Custom type sub10UnitMgmtAlarmType based on Sub10AlarmType"""


_Sub10UnitMgmtAlarmType_Object = MibTableColumn
sub10UnitMgmtAlarmType = _Sub10UnitMgmtAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 13),
    _Sub10UnitMgmtAlarmType_Type()
)
sub10UnitMgmtAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmType.setStatus("current")


class _Sub10UnitMgmtAlarmSmtpAddress_Type(OctetString):
    """Custom type sub10UnitMgmtAlarmSmtpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Sub10UnitMgmtAlarmSmtpAddress_Type.__name__ = "OctetString"
_Sub10UnitMgmtAlarmSmtpAddress_Object = MibTableColumn
sub10UnitMgmtAlarmSmtpAddress = _Sub10UnitMgmtAlarmSmtpAddress_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 14),
    _Sub10UnitMgmtAlarmSmtpAddress_Type()
)
sub10UnitMgmtAlarmSmtpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmSmtpAddress.setStatus("current")


class _Sub10UnitMgmtAlarmToSyslog_Type(Sub10State):
    """Custom type sub10UnitMgmtAlarmToSyslog based on Sub10State"""


_Sub10UnitMgmtAlarmToSyslog_Object = MibTableColumn
sub10UnitMgmtAlarmToSyslog = _Sub10UnitMgmtAlarmToSyslog_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 15),
    _Sub10UnitMgmtAlarmToSyslog_Type()
)
sub10UnitMgmtAlarmToSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmToSyslog.setStatus("current")


class _Sub10UnitMgmtAlarmEnabled_Type(Sub10State):
    """Custom type sub10UnitMgmtAlarmEnabled based on Sub10State"""


_Sub10UnitMgmtAlarmEnabled_Object = MibTableColumn
sub10UnitMgmtAlarmEnabled = _Sub10UnitMgmtAlarmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 16),
    _Sub10UnitMgmtAlarmEnabled_Type()
)
sub10UnitMgmtAlarmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmEnabled.setStatus("current")


class _Sub10UnitMgmtAlarmMeasObjectVal_Type(DisplayString):
    """Custom type sub10UnitMgmtAlarmMeasObjectVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10UnitMgmtAlarmMeasObjectVal_Type.__name__ = "DisplayString"
_Sub10UnitMgmtAlarmMeasObjectVal_Object = MibTableColumn
sub10UnitMgmtAlarmMeasObjectVal = _Sub10UnitMgmtAlarmMeasObjectVal_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 17),
    _Sub10UnitMgmtAlarmMeasObjectVal_Type()
)
sub10UnitMgmtAlarmMeasObjectVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmMeasObjectVal.setStatus("current")


class _Sub10UnitMgmtAlarmToSNMP_Type(Sub10State):
    """Custom type sub10UnitMgmtAlarmToSNMP based on Sub10State"""


_Sub10UnitMgmtAlarmToSNMP_Object = MibTableColumn
sub10UnitMgmtAlarmToSNMP = _Sub10UnitMgmtAlarmToSNMP_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 18),
    _Sub10UnitMgmtAlarmToSNMP_Type()
)
sub10UnitMgmtAlarmToSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmToSNMP.setStatus("current")


class _Sub10UnitMgmtAlarmMeasObjIndex_Type(Unsigned32):
    """Custom type sub10UnitMgmtAlarmMeasObjIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Sub10UnitMgmtAlarmMeasObjIndex_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtAlarmMeasObjIndex_Object = MibTableColumn
sub10UnitMgmtAlarmMeasObjIndex = _Sub10UnitMgmtAlarmMeasObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 1, 1, 19),
    _Sub10UnitMgmtAlarmMeasObjIndex_Type()
)
sub10UnitMgmtAlarmMeasObjIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmMeasObjIndex.setStatus("current")


class _Sub10UnitMgmtAlarmsUserDefStart_Type(Sub10AlarmIndex):
    """Custom type sub10UnitMgmtAlarmsUserDefStart based on Sub10AlarmIndex"""
    defaultValue = 65


_Sub10UnitMgmtAlarmsUserDefStart_Object = MibScalar
sub10UnitMgmtAlarmsUserDefStart = _Sub10UnitMgmtAlarmsUserDefStart_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 6, 2),
    _Sub10UnitMgmtAlarmsUserDefStart_Type()
)
sub10UnitMgmtAlarmsUserDefStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmsUserDefStart.setStatus("current")
_Sub10UnitMgmtSnmp_ObjectIdentity = ObjectIdentity
sub10UnitMgmtSnmp = _Sub10UnitMgmtSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7)
)


class _Sub10UnitMgmtSnmpAgent_Type(Sub10State):
    """Custom type sub10UnitMgmtSnmpAgent based on Sub10State"""


_Sub10UnitMgmtSnmpAgent_Object = MibScalar
sub10UnitMgmtSnmpAgent = _Sub10UnitMgmtSnmpAgent_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 1),
    _Sub10UnitMgmtSnmpAgent_Type()
)
sub10UnitMgmtSnmpAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpAgent.setStatus("current")


class _Sub10UnitMgmtSnmpTraps_Type(Sub10State):
    """Custom type sub10UnitMgmtSnmpTraps based on Sub10State"""


_Sub10UnitMgmtSnmpTraps_Object = MibScalar
sub10UnitMgmtSnmpTraps = _Sub10UnitMgmtSnmpTraps_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 2),
    _Sub10UnitMgmtSnmpTraps_Type()
)
sub10UnitMgmtSnmpTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTraps.setStatus("current")


class _Sub10UnitMgmtSnmpv320Mib_Type(Sub10State):
    """Custom type sub10UnitMgmtSnmpv320Mib based on Sub10State"""


_Sub10UnitMgmtSnmpv320Mib_Object = MibScalar
sub10UnitMgmtSnmpv320Mib = _Sub10UnitMgmtSnmpv320Mib_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 3),
    _Sub10UnitMgmtSnmpv320Mib_Type()
)
sub10UnitMgmtSnmpv320Mib.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpv320Mib.setStatus("current")


class _Sub10UnitMgmtSnmpv3_Type(Sub10State):
    """Custom type sub10UnitMgmtSnmpv3 based on Sub10State"""


_Sub10UnitMgmtSnmpv3_Object = MibScalar
sub10UnitMgmtSnmpv3 = _Sub10UnitMgmtSnmpv3_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 4),
    _Sub10UnitMgmtSnmpv3_Type()
)
sub10UnitMgmtSnmpv3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpv3.setStatus("current")
_Sub10UnitMgmtSnmpTrpDstTable_Object = MibTable
sub10UnitMgmtSnmpTrpDstTable = _Sub10UnitMgmtSnmpTrpDstTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 5)
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTrpDstTable.setStatus("current")
_Sub10UnitMgmtSnmpTrpDstEntry_Object = MibTableRow
sub10UnitMgmtSnmpTrpDstEntry = _Sub10UnitMgmtSnmpTrpDstEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 5, 1)
)
sub10UnitMgmtSnmpTrpDstEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpTrpDstIndex"),
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTrpDstEntry.setStatus("current")


class _Sub10UnitMgmtSnmpTrpDstIndex_Type(Unsigned32):
    """Custom type sub10UnitMgmtSnmpTrpDstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Sub10UnitMgmtSnmpTrpDstIndex_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtSnmpTrpDstIndex_Object = MibTableColumn
sub10UnitMgmtSnmpTrpDstIndex = _Sub10UnitMgmtSnmpTrpDstIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 5, 1, 1),
    _Sub10UnitMgmtSnmpTrpDstIndex_Type()
)
sub10UnitMgmtSnmpTrpDstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTrpDstIndex.setStatus("current")


class _Sub10UnitMgmtSnmpTrpDstRowStatus_Type(RowStatus):
    """Custom type sub10UnitMgmtSnmpTrpDstRowStatus based on RowStatus"""


_Sub10UnitMgmtSnmpTrpDstRowStatus_Object = MibTableColumn
sub10UnitMgmtSnmpTrpDstRowStatus = _Sub10UnitMgmtSnmpTrpDstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 5, 1, 2),
    _Sub10UnitMgmtSnmpTrpDstRowStatus_Type()
)
sub10UnitMgmtSnmpTrpDstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTrpDstRowStatus.setStatus("current")


class _Sub10UnitMgmtSnmpTrpDstIpAddr_Type(OctetString):
    """Custom type sub10UnitMgmtSnmpTrpDstIpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Sub10UnitMgmtSnmpTrpDstIpAddr_Type.__name__ = "OctetString"
_Sub10UnitMgmtSnmpTrpDstIpAddr_Object = MibTableColumn
sub10UnitMgmtSnmpTrpDstIpAddr = _Sub10UnitMgmtSnmpTrpDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 5, 1, 3),
    _Sub10UnitMgmtSnmpTrpDstIpAddr_Type()
)
sub10UnitMgmtSnmpTrpDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTrpDstIpAddr.setStatus("current")


class _Sub10UnitMgmtSnmpTrpDstCommunity_Type(OctetString):
    """Custom type sub10UnitMgmtSnmpTrpDstCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10UnitMgmtSnmpTrpDstCommunity_Type.__name__ = "OctetString"
_Sub10UnitMgmtSnmpTrpDstCommunity_Object = MibTableColumn
sub10UnitMgmtSnmpTrpDstCommunity = _Sub10UnitMgmtSnmpTrpDstCommunity_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 5, 1, 4),
    _Sub10UnitMgmtSnmpTrpDstCommunity_Type()
)
sub10UnitMgmtSnmpTrpDstCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTrpDstCommunity.setStatus("current")


class _Sub10UnitMgmtSnmpEngineIdFormat_Type(Integer32):
    """Custom type sub10UnitMgmtSnmpEngineIdFormat based on Integer32"""
    defaultValue = 4

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
        *(("macAddress", 3),
          ("textString", 4),
          ("v4IpAddress", 1),
          ("v6IpAddress", 2))
    )


_Sub10UnitMgmtSnmpEngineIdFormat_Type.__name__ = "Integer32"
_Sub10UnitMgmtSnmpEngineIdFormat_Object = MibScalar
sub10UnitMgmtSnmpEngineIdFormat = _Sub10UnitMgmtSnmpEngineIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 6),
    _Sub10UnitMgmtSnmpEngineIdFormat_Type()
)
sub10UnitMgmtSnmpEngineIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpEngineIdFormat.setStatus("current")


class _Sub10UnitMgmtSnmpEngineIdText_Type(OctetString):
    """Custom type sub10UnitMgmtSnmpEngineIdText based on OctetString"""
    defaultValue = OctetString("Sub10Systems")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_Sub10UnitMgmtSnmpEngineIdText_Type.__name__ = "OctetString"
_Sub10UnitMgmtSnmpEngineIdText_Object = MibScalar
sub10UnitMgmtSnmpEngineIdText = _Sub10UnitMgmtSnmpEngineIdText_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 7),
    _Sub10UnitMgmtSnmpEngineIdText_Type()
)
sub10UnitMgmtSnmpEngineIdText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpEngineIdText.setStatus("current")


class _Sub10UnitMgmtSnmpEngineId_Type(OctetString):
    """Custom type sub10UnitMgmtSnmpEngineId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_Sub10UnitMgmtSnmpEngineId_Type.__name__ = "OctetString"
_Sub10UnitMgmtSnmpEngineId_Object = MibScalar
sub10UnitMgmtSnmpEngineId = _Sub10UnitMgmtSnmpEngineId_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 8),
    _Sub10UnitMgmtSnmpEngineId_Type()
)
sub10UnitMgmtSnmpEngineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpEngineId.setStatus("current")


class _Sub10UnitMgmtSnmpOperAuthProto_Type(Sub10Snmpv3AuthProtocol):
    """Custom type sub10UnitMgmtSnmpOperAuthProto based on Sub10Snmpv3AuthProtocol"""


_Sub10UnitMgmtSnmpOperAuthProto_Object = MibScalar
sub10UnitMgmtSnmpOperAuthProto = _Sub10UnitMgmtSnmpOperAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 9),
    _Sub10UnitMgmtSnmpOperAuthProto_Type()
)
sub10UnitMgmtSnmpOperAuthProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpOperAuthProto.setStatus("current")


class _Sub10UnitMgmtSnmpOperPrivProto_Type(Sub10Snmpv3PrivProtocol):
    """Custom type sub10UnitMgmtSnmpOperPrivProto based on Sub10Snmpv3PrivProtocol"""


_Sub10UnitMgmtSnmpOperPrivProto_Object = MibScalar
sub10UnitMgmtSnmpOperPrivProto = _Sub10UnitMgmtSnmpOperPrivProto_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 10),
    _Sub10UnitMgmtSnmpOperPrivProto_Type()
)
sub10UnitMgmtSnmpOperPrivProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpOperPrivProto.setStatus("current")


class _Sub10UnitMgmtSnmpAdminAuthProto_Type(Sub10Snmpv3AuthProtocol):
    """Custom type sub10UnitMgmtSnmpAdminAuthProto based on Sub10Snmpv3AuthProtocol"""


_Sub10UnitMgmtSnmpAdminAuthProto_Object = MibScalar
sub10UnitMgmtSnmpAdminAuthProto = _Sub10UnitMgmtSnmpAdminAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 11),
    _Sub10UnitMgmtSnmpAdminAuthProto_Type()
)
sub10UnitMgmtSnmpAdminAuthProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpAdminAuthProto.setStatus("current")


class _Sub10UnitMgmtSnmpAdminPrivProto_Type(Sub10Snmpv3PrivProtocol):
    """Custom type sub10UnitMgmtSnmpAdminPrivProto based on Sub10Snmpv3PrivProtocol"""


_Sub10UnitMgmtSnmpAdminPrivProto_Object = MibScalar
sub10UnitMgmtSnmpAdminPrivProto = _Sub10UnitMgmtSnmpAdminPrivProto_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 12),
    _Sub10UnitMgmtSnmpAdminPrivProto_Type()
)
sub10UnitMgmtSnmpAdminPrivProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpAdminPrivProto.setStatus("current")


class _Sub10UnitMgmtSnmpMaintAuthProto_Type(Sub10Snmpv3AuthProtocol):
    """Custom type sub10UnitMgmtSnmpMaintAuthProto based on Sub10Snmpv3AuthProtocol"""


_Sub10UnitMgmtSnmpMaintAuthProto_Object = MibScalar
sub10UnitMgmtSnmpMaintAuthProto = _Sub10UnitMgmtSnmpMaintAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 13),
    _Sub10UnitMgmtSnmpMaintAuthProto_Type()
)
sub10UnitMgmtSnmpMaintAuthProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpMaintAuthProto.setStatus("current")


class _Sub10UnitMgmtSnmpMaintPrivProto_Type(Sub10Snmpv3PrivProtocol):
    """Custom type sub10UnitMgmtSnmpMaintPrivProto based on Sub10Snmpv3PrivProtocol"""


_Sub10UnitMgmtSnmpMaintPrivProto_Object = MibScalar
sub10UnitMgmtSnmpMaintPrivProto = _Sub10UnitMgmtSnmpMaintPrivProto_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 14),
    _Sub10UnitMgmtSnmpMaintPrivProto_Type()
)
sub10UnitMgmtSnmpMaintPrivProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpMaintPrivProto.setStatus("current")
_Sub10UnitMgmtSnmpUserTable_Object = MibTable
sub10UnitMgmtSnmpUserTable = _Sub10UnitMgmtSnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 15)
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpUserTable.setStatus("current")
_Sub10UnitMgmtSnmpUserEntry_Object = MibTableRow
sub10UnitMgmtSnmpUserEntry = _Sub10UnitMgmtSnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 15, 1)
)
sub10UnitMgmtSnmpUserEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpUserIndex"),
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpUserEntry.setStatus("current")


class _Sub10UnitMgmtSnmpUserIndex_Type(Unsigned32):
    """Custom type sub10UnitMgmtSnmpUserIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Sub10UnitMgmtSnmpUserIndex_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtSnmpUserIndex_Object = MibTableColumn
sub10UnitMgmtSnmpUserIndex = _Sub10UnitMgmtSnmpUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 15, 1, 1),
    _Sub10UnitMgmtSnmpUserIndex_Type()
)
sub10UnitMgmtSnmpUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpUserIndex.setStatus("current")


class _Sub10UnitMgmtSnmpUserRowStatus_Type(RowStatus):
    """Custom type sub10UnitMgmtSnmpUserRowStatus based on RowStatus"""


_Sub10UnitMgmtSnmpUserRowStatus_Object = MibTableColumn
sub10UnitMgmtSnmpUserRowStatus = _Sub10UnitMgmtSnmpUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 15, 1, 2),
    _Sub10UnitMgmtSnmpUserRowStatus_Type()
)
sub10UnitMgmtSnmpUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpUserRowStatus.setStatus("current")


class _Sub10UnitMgmtSnmpUserName_Type(OctetString):
    """Custom type sub10UnitMgmtSnmpUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10UnitMgmtSnmpUserName_Type.__name__ = "OctetString"
_Sub10UnitMgmtSnmpUserName_Object = MibTableColumn
sub10UnitMgmtSnmpUserName = _Sub10UnitMgmtSnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 15, 1, 3),
    _Sub10UnitMgmtSnmpUserName_Type()
)
sub10UnitMgmtSnmpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpUserName.setStatus("current")


class _Sub10UnitMgmtSnmpUserGroup_Type(Sub10UserGroup):
    """Custom type sub10UnitMgmtSnmpUserGroup based on Sub10UserGroup"""


_Sub10UnitMgmtSnmpUserGroup_Object = MibTableColumn
sub10UnitMgmtSnmpUserGroup = _Sub10UnitMgmtSnmpUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 15, 1, 4),
    _Sub10UnitMgmtSnmpUserGroup_Type()
)
sub10UnitMgmtSnmpUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpUserGroup.setStatus("current")


class _Sub10UnitMgmtSnmpUserAuthPwd_Type(OctetString):
    """Custom type sub10UnitMgmtSnmpUserAuthPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_Sub10UnitMgmtSnmpUserAuthPwd_Type.__name__ = "OctetString"
_Sub10UnitMgmtSnmpUserAuthPwd_Object = MibTableColumn
sub10UnitMgmtSnmpUserAuthPwd = _Sub10UnitMgmtSnmpUserAuthPwd_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 15, 1, 5),
    _Sub10UnitMgmtSnmpUserAuthPwd_Type()
)
sub10UnitMgmtSnmpUserAuthPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpUserAuthPwd.setStatus("current")


class _Sub10UnitMgmtSnmpUserAuthPwdChk_Type(OctetString):
    """Custom type sub10UnitMgmtSnmpUserAuthPwdChk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_Sub10UnitMgmtSnmpUserAuthPwdChk_Type.__name__ = "OctetString"
_Sub10UnitMgmtSnmpUserAuthPwdChk_Object = MibTableColumn
sub10UnitMgmtSnmpUserAuthPwdChk = _Sub10UnitMgmtSnmpUserAuthPwdChk_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 15, 1, 6),
    _Sub10UnitMgmtSnmpUserAuthPwdChk_Type()
)
sub10UnitMgmtSnmpUserAuthPwdChk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpUserAuthPwdChk.setStatus("current")


class _Sub10UnitMgmtSnmpUserPrivPwd_Type(OctetString):
    """Custom type sub10UnitMgmtSnmpUserPrivPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_Sub10UnitMgmtSnmpUserPrivPwd_Type.__name__ = "OctetString"
_Sub10UnitMgmtSnmpUserPrivPwd_Object = MibTableColumn
sub10UnitMgmtSnmpUserPrivPwd = _Sub10UnitMgmtSnmpUserPrivPwd_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 15, 1, 7),
    _Sub10UnitMgmtSnmpUserPrivPwd_Type()
)
sub10UnitMgmtSnmpUserPrivPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpUserPrivPwd.setStatus("current")


class _Sub10UnitMgmtSnmpUserPrivPwdChk_Type(OctetString):
    """Custom type sub10UnitMgmtSnmpUserPrivPwdChk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_Sub10UnitMgmtSnmpUserPrivPwdChk_Type.__name__ = "OctetString"
_Sub10UnitMgmtSnmpUserPrivPwdChk_Object = MibTableColumn
sub10UnitMgmtSnmpUserPrivPwdChk = _Sub10UnitMgmtSnmpUserPrivPwdChk_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 15, 1, 8),
    _Sub10UnitMgmtSnmpUserPrivPwdChk_Type()
)
sub10UnitMgmtSnmpUserPrivPwdChk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpUserPrivPwdChk.setStatus("current")
_Sub10UnitMgmtSnmpAccessTable_Object = MibTable
sub10UnitMgmtSnmpAccessTable = _Sub10UnitMgmtSnmpAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 16)
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpAccessTable.setStatus("current")
_Sub10UnitMgmtSnmpAccessEntry_Object = MibTableRow
sub10UnitMgmtSnmpAccessEntry = _Sub10UnitMgmtSnmpAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 16, 1)
)
sub10UnitMgmtSnmpAccessEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpAccessIndex"),
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpAccessEntry.setStatus("current")


class _Sub10UnitMgmtSnmpAccessIndex_Type(Unsigned32):
    """Custom type sub10UnitMgmtSnmpAccessIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Sub10UnitMgmtSnmpAccessIndex_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtSnmpAccessIndex_Object = MibTableColumn
sub10UnitMgmtSnmpAccessIndex = _Sub10UnitMgmtSnmpAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 16, 1, 1),
    _Sub10UnitMgmtSnmpAccessIndex_Type()
)
sub10UnitMgmtSnmpAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpAccessIndex.setStatus("current")


class _Sub10UnitMgmtSnmpAccessRowStatus_Type(RowStatus):
    """Custom type sub10UnitMgmtSnmpAccessRowStatus based on RowStatus"""


_Sub10UnitMgmtSnmpAccessRowStatus_Object = MibTableColumn
sub10UnitMgmtSnmpAccessRowStatus = _Sub10UnitMgmtSnmpAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 16, 1, 2),
    _Sub10UnitMgmtSnmpAccessRowStatus_Type()
)
sub10UnitMgmtSnmpAccessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpAccessRowStatus.setStatus("current")


class _Sub10UnitMgmtSnmpAccessName_Type(OctetString):
    """Custom type sub10UnitMgmtSnmpAccessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10UnitMgmtSnmpAccessName_Type.__name__ = "OctetString"
_Sub10UnitMgmtSnmpAccessName_Object = MibTableColumn
sub10UnitMgmtSnmpAccessName = _Sub10UnitMgmtSnmpAccessName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 16, 1, 3),
    _Sub10UnitMgmtSnmpAccessName_Type()
)
sub10UnitMgmtSnmpAccessName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpAccessName.setStatus("current")


class _Sub10UnitMgmtSnmpAccessIpAddr_Type(OctetString):
    """Custom type sub10UnitMgmtSnmpAccessIpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Sub10UnitMgmtSnmpAccessIpAddr_Type.__name__ = "OctetString"
_Sub10UnitMgmtSnmpAccessIpAddr_Object = MibTableColumn
sub10UnitMgmtSnmpAccessIpAddr = _Sub10UnitMgmtSnmpAccessIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 16, 1, 4),
    _Sub10UnitMgmtSnmpAccessIpAddr_Type()
)
sub10UnitMgmtSnmpAccessIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpAccessIpAddr.setStatus("current")
_Sub10UnitMgmtSnmpTargetTable_Object = MibTable
sub10UnitMgmtSnmpTargetTable = _Sub10UnitMgmtSnmpTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 17)
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTargetTable.setStatus("current")
_Sub10UnitMgmtSnmpTargetEntry_Object = MibTableRow
sub10UnitMgmtSnmpTargetEntry = _Sub10UnitMgmtSnmpTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 17, 1)
)
sub10UnitMgmtSnmpTargetEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpTargetIndex"),
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTargetEntry.setStatus("current")


class _Sub10UnitMgmtSnmpTargetIndex_Type(Unsigned32):
    """Custom type sub10UnitMgmtSnmpTargetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Sub10UnitMgmtSnmpTargetIndex_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtSnmpTargetIndex_Object = MibTableColumn
sub10UnitMgmtSnmpTargetIndex = _Sub10UnitMgmtSnmpTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 17, 1, 1),
    _Sub10UnitMgmtSnmpTargetIndex_Type()
)
sub10UnitMgmtSnmpTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTargetIndex.setStatus("current")


class _Sub10UnitMgmtSnmpTargetRowStatus_Type(RowStatus):
    """Custom type sub10UnitMgmtSnmpTargetRowStatus based on RowStatus"""


_Sub10UnitMgmtSnmpTargetRowStatus_Object = MibTableColumn
sub10UnitMgmtSnmpTargetRowStatus = _Sub10UnitMgmtSnmpTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 17, 1, 2),
    _Sub10UnitMgmtSnmpTargetRowStatus_Type()
)
sub10UnitMgmtSnmpTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTargetRowStatus.setStatus("current")


class _Sub10UnitMgmtSnmpTargetName_Type(OctetString):
    """Custom type sub10UnitMgmtSnmpTargetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10UnitMgmtSnmpTargetName_Type.__name__ = "OctetString"
_Sub10UnitMgmtSnmpTargetName_Object = MibTableColumn
sub10UnitMgmtSnmpTargetName = _Sub10UnitMgmtSnmpTargetName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 17, 1, 3),
    _Sub10UnitMgmtSnmpTargetName_Type()
)
sub10UnitMgmtSnmpTargetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTargetName.setStatus("current")


class _Sub10UnitMgmtSnmpTargetIpAddr_Type(OctetString):
    """Custom type sub10UnitMgmtSnmpTargetIpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Sub10UnitMgmtSnmpTargetIpAddr_Type.__name__ = "OctetString"
_Sub10UnitMgmtSnmpTargetIpAddr_Object = MibTableColumn
sub10UnitMgmtSnmpTargetIpAddr = _Sub10UnitMgmtSnmpTargetIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 17, 1, 4),
    _Sub10UnitMgmtSnmpTargetIpAddr_Type()
)
sub10UnitMgmtSnmpTargetIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTargetIpAddr.setStatus("current")


class _Sub10UnitMgmtSnmpTargetUserName_Type(OctetString):
    """Custom type sub10UnitMgmtSnmpTargetUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10UnitMgmtSnmpTargetUserName_Type.__name__ = "OctetString"
_Sub10UnitMgmtSnmpTargetUserName_Object = MibTableColumn
sub10UnitMgmtSnmpTargetUserName = _Sub10UnitMgmtSnmpTargetUserName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 7, 17, 1, 5),
    _Sub10UnitMgmtSnmpTargetUserName_Type()
)
sub10UnitMgmtSnmpTargetUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTargetUserName.setStatus("current")
_Sub10UnitMgmtSmtp_ObjectIdentity = ObjectIdentity
sub10UnitMgmtSmtp = _Sub10UnitMgmtSmtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 8)
)
_Sub10UnitMgmtFirmware_ObjectIdentity = ObjectIdentity
sub10UnitMgmtFirmware = _Sub10UnitMgmtFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9)
)
_Sub10UnitMgmtFirmwareSelectBank_Type = Sub10FirmwareBank
_Sub10UnitMgmtFirmwareSelectBank_Object = MibScalar
sub10UnitMgmtFirmwareSelectBank = _Sub10UnitMgmtFirmwareSelectBank_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 1),
    _Sub10UnitMgmtFirmwareSelectBank_Type()
)
sub10UnitMgmtFirmwareSelectBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareSelectBank.setStatus("current")
_Sub10UnitMgmtFirmwareLoadedBank_Type = Sub10FirmwareBank
_Sub10UnitMgmtFirmwareLoadedBank_Object = MibScalar
sub10UnitMgmtFirmwareLoadedBank = _Sub10UnitMgmtFirmwareLoadedBank_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 2),
    _Sub10UnitMgmtFirmwareLoadedBank_Type()
)
sub10UnitMgmtFirmwareLoadedBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareLoadedBank.setStatus("current")


class _Sub10UnitMgmtFirmwareVersion_Type(OctetString):
    """Custom type sub10UnitMgmtFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Sub10UnitMgmtFirmwareVersion_Type.__name__ = "OctetString"
_Sub10UnitMgmtFirmwareVersion_Object = MibScalar
sub10UnitMgmtFirmwareVersion = _Sub10UnitMgmtFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 3),
    _Sub10UnitMgmtFirmwareVersion_Type()
)
sub10UnitMgmtFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareVersion.setStatus("current")


class _Sub10UnitMgmtFirmwareBootVersion_Type(OctetString):
    """Custom type sub10UnitMgmtFirmwareBootVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Sub10UnitMgmtFirmwareBootVersion_Type.__name__ = "OctetString"
_Sub10UnitMgmtFirmwareBootVersion_Object = MibScalar
sub10UnitMgmtFirmwareBootVersion = _Sub10UnitMgmtFirmwareBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 4),
    _Sub10UnitMgmtFirmwareBootVersion_Type()
)
sub10UnitMgmtFirmwareBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareBootVersion.setStatus("current")


class _Sub10UnitMgmtFirmwareAction_Type(Integer32):
    """Custom type sub10UnitMgmtFirmwareAction based on Integer32"""
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
        *(("fmwCopyInactiveBank", 3),
          ("fmwNone", 1),
          ("fmwReboot", 2),
          ("fmwUploadInactiveBank", 4))
    )


_Sub10UnitMgmtFirmwareAction_Type.__name__ = "Integer32"
_Sub10UnitMgmtFirmwareAction_Object = MibScalar
sub10UnitMgmtFirmwareAction = _Sub10UnitMgmtFirmwareAction_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 5),
    _Sub10UnitMgmtFirmwareAction_Type()
)
sub10UnitMgmtFirmwareAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareAction.setStatus("current")
_Sub10UnitMgmtFirmwareBankTable_Object = MibTable
sub10UnitMgmtFirmwareBankTable = _Sub10UnitMgmtFirmwareBankTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 6)
)
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareBankTable.setStatus("current")
_Sub10UnitMgmtFirmwareBankEntry_Object = MibTableRow
sub10UnitMgmtFirmwareBankEntry = _Sub10UnitMgmtFirmwareBankEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 6, 1)
)
sub10UnitMgmtFirmwareBankEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10UnitMgmtFirmwareBankIndex"),
)
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareBankEntry.setStatus("current")
_Sub10UnitMgmtFirmwareBankIndex_Type = Sub10FirmwareBank
_Sub10UnitMgmtFirmwareBankIndex_Object = MibTableColumn
sub10UnitMgmtFirmwareBankIndex = _Sub10UnitMgmtFirmwareBankIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 6, 1, 1),
    _Sub10UnitMgmtFirmwareBankIndex_Type()
)
sub10UnitMgmtFirmwareBankIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareBankIndex.setStatus("current")


class _Sub10UnitMgmtFirmwareBankVersion_Type(OctetString):
    """Custom type sub10UnitMgmtFirmwareBankVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Sub10UnitMgmtFirmwareBankVersion_Type.__name__ = "OctetString"
_Sub10UnitMgmtFirmwareBankVersion_Object = MibTableColumn
sub10UnitMgmtFirmwareBankVersion = _Sub10UnitMgmtFirmwareBankVersion_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 6, 1, 2),
    _Sub10UnitMgmtFirmwareBankVersion_Type()
)
sub10UnitMgmtFirmwareBankVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareBankVersion.setStatus("current")


class _Sub10UnitMgmtFirmwareBankImage_Type(OctetString):
    """Custom type sub10UnitMgmtFirmwareBankImage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Sub10UnitMgmtFirmwareBankImage_Type.__name__ = "OctetString"
_Sub10UnitMgmtFirmwareBankImage_Object = MibTableColumn
sub10UnitMgmtFirmwareBankImage = _Sub10UnitMgmtFirmwareBankImage_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 6, 1, 3),
    _Sub10UnitMgmtFirmwareBankImage_Type()
)
sub10UnitMgmtFirmwareBankImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareBankImage.setStatus("current")


class _Sub10UnitMgmtFirmwareUplImage_Type(OctetString):
    """Custom type sub10UnitMgmtFirmwareUplImage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Sub10UnitMgmtFirmwareUplImage_Type.__name__ = "OctetString"
_Sub10UnitMgmtFirmwareUplImage_Object = MibScalar
sub10UnitMgmtFirmwareUplImage = _Sub10UnitMgmtFirmwareUplImage_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 7),
    _Sub10UnitMgmtFirmwareUplImage_Type()
)
sub10UnitMgmtFirmwareUplImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareUplImage.setStatus("current")


class _Sub10UnitMgmtFirmwareUplSvrIp_Type(OctetString):
    """Custom type sub10UnitMgmtFirmwareUplSvrIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )


_Sub10UnitMgmtFirmwareUplSvrIp_Type.__name__ = "OctetString"
_Sub10UnitMgmtFirmwareUplSvrIp_Object = MibScalar
sub10UnitMgmtFirmwareUplSvrIp = _Sub10UnitMgmtFirmwareUplSvrIp_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 8),
    _Sub10UnitMgmtFirmwareUplSvrIp_Type()
)
sub10UnitMgmtFirmwareUplSvrIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareUplSvrIp.setStatus("current")
_Sub10UnitMgmtFirmwareFromBank_Type = Sub10FirmwareBank
_Sub10UnitMgmtFirmwareFromBank_Object = MibScalar
sub10UnitMgmtFirmwareFromBank = _Sub10UnitMgmtFirmwareFromBank_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 9),
    _Sub10UnitMgmtFirmwareFromBank_Type()
)
sub10UnitMgmtFirmwareFromBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareFromBank.setStatus("current")
_Sub10UnitMgmtFirmwareToBank_Type = Sub10FirmwareBank
_Sub10UnitMgmtFirmwareToBank_Object = MibScalar
sub10UnitMgmtFirmwareToBank = _Sub10UnitMgmtFirmwareToBank_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 10),
    _Sub10UnitMgmtFirmwareToBank_Type()
)
sub10UnitMgmtFirmwareToBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareToBank.setStatus("current")


class _Sub10UnitMgmtFirmwareActStatus_Type(Integer32):
    """Custom type sub10UnitMgmtFirmwareActStatus based on Integer32"""
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
        *(("fmwCopyBankFailed", 15),
          ("fmwCopyBankSuccess", 16),
          ("fmwCopyingBank", 13),
          ("fmwCopyingBankComplete", 14),
          ("fmwImageValidateFailed", 12),
          ("fmwImageValidateSuccess", 11),
          ("fmwUploadFailed", 2),
          ("fmwUploadFileNotFound", 4),
          ("fmwUploadInvalid", 5),
          ("fmwUploadSuccess", 1),
          ("fmwUploadTimeout", 3),
          ("fmwUploadWritingBank", 8),
          ("fmwUploadWritingBankComplete", 9),
          ("fmwUploadingImage", 6),
          ("fmwUploadingImageComplete", 7),
          ("fmwValidatingImage", 10))
    )


_Sub10UnitMgmtFirmwareActStatus_Type.__name__ = "Integer32"
_Sub10UnitMgmtFirmwareActStatus_Object = MibScalar
sub10UnitMgmtFirmwareActStatus = _Sub10UnitMgmtFirmwareActStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 11),
    _Sub10UnitMgmtFirmwareActStatus_Type()
)
sub10UnitMgmtFirmwareActStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareActStatus.setStatus("current")


class _Sub10UnitMgmtFirmwareActProgress_Type(Integer32):
    """Custom type sub10UnitMgmtFirmwareActProgress based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Sub10UnitMgmtFirmwareActProgress_Type.__name__ = "Integer32"
_Sub10UnitMgmtFirmwareActProgress_Object = MibScalar
sub10UnitMgmtFirmwareActProgress = _Sub10UnitMgmtFirmwareActProgress_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 9, 12),
    _Sub10UnitMgmtFirmwareActProgress_Type()
)
sub10UnitMgmtFirmwareActProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareActProgress.setStatus("current")
_Sub10UnitMgmtDNS_ObjectIdentity = ObjectIdentity
sub10UnitMgmtDNS = _Sub10UnitMgmtDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 10)
)
_Sub10UnitMgmtDNSTable_Object = MibTable
sub10UnitMgmtDNSTable = _Sub10UnitMgmtDNSTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 10, 1)
)
if mibBuilder.loadTexts:
    sub10UnitMgmtDNSTable.setStatus("current")
_Sub10UnitMgmtDNSEntry_Object = MibTableRow
sub10UnitMgmtDNSEntry = _Sub10UnitMgmtDNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 10, 1, 1)
)
sub10UnitMgmtDNSEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10UnitMgmtDNSIndex"),
)
if mibBuilder.loadTexts:
    sub10UnitMgmtDNSEntry.setStatus("current")


class _Sub10UnitMgmtDNSIndex_Type(Unsigned32):
    """Custom type sub10UnitMgmtDNSIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Sub10UnitMgmtDNSIndex_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtDNSIndex_Object = MibTableColumn
sub10UnitMgmtDNSIndex = _Sub10UnitMgmtDNSIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 10, 1, 1, 1),
    _Sub10UnitMgmtDNSIndex_Type()
)
sub10UnitMgmtDNSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10UnitMgmtDNSIndex.setStatus("current")


class _Sub10UnitMgmtDNServer_Type(OctetString):
    """Custom type sub10UnitMgmtDNServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )


_Sub10UnitMgmtDNServer_Type.__name__ = "OctetString"
_Sub10UnitMgmtDNServer_Object = MibTableColumn
sub10UnitMgmtDNServer = _Sub10UnitMgmtDNServer_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 10, 1, 1, 2),
    _Sub10UnitMgmtDNServer_Type()
)
sub10UnitMgmtDNServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtDNServer.setStatus("current")
_Sub10UnitMgmtEncryption_ObjectIdentity = ObjectIdentity
sub10UnitMgmtEncryption = _Sub10UnitMgmtEncryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 11)
)


class _Sub10UnitMgmtEncryptMode_Type(Integer32):
    """Custom type sub10UnitMgmtEncryptMode based on Integer32"""
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
        *(("encryptAES128", 1),
          ("encryptAES192", 2),
          ("encryptAES256", 3),
          ("encryptNone", 0))
    )


_Sub10UnitMgmtEncryptMode_Type.__name__ = "Integer32"
_Sub10UnitMgmtEncryptMode_Object = MibScalar
sub10UnitMgmtEncryptMode = _Sub10UnitMgmtEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 11, 1),
    _Sub10UnitMgmtEncryptMode_Type()
)
sub10UnitMgmtEncryptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtEncryptMode.setStatus("current")


class _Sub10UnitMgmtEncryptKey_Type(OctetString):
    """Custom type sub10UnitMgmtEncryptKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Sub10UnitMgmtEncryptKey_Type.__name__ = "OctetString"
_Sub10UnitMgmtEncryptKey_Object = MibScalar
sub10UnitMgmtEncryptKey = _Sub10UnitMgmtEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 11, 2),
    _Sub10UnitMgmtEncryptKey_Type()
)
sub10UnitMgmtEncryptKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtEncryptKey.setStatus("current")
_Sub10UnitMgmtLicense_ObjectIdentity = ObjectIdentity
sub10UnitMgmtLicense = _Sub10UnitMgmtLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 12)
)


class _Sub10UnitMgmtLicenseKey_Type(OctetString):
    """Custom type sub10UnitMgmtLicenseKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Sub10UnitMgmtLicenseKey_Type.__name__ = "OctetString"
_Sub10UnitMgmtLicenseKey_Object = MibScalar
sub10UnitMgmtLicenseKey = _Sub10UnitMgmtLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 12, 1),
    _Sub10UnitMgmtLicenseKey_Type()
)
sub10UnitMgmtLicenseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtLicenseKey.setStatus("current")


class _Sub10UnitMgmtLicenseAES_Type(Sub10State):
    """Custom type sub10UnitMgmtLicenseAES based on Sub10State"""


_Sub10UnitMgmtLicenseAES_Object = MibScalar
sub10UnitMgmtLicenseAES = _Sub10UnitMgmtLicenseAES_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 12, 2),
    _Sub10UnitMgmtLicenseAES_Type()
)
sub10UnitMgmtLicenseAES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10UnitMgmtLicenseAES.setStatus("current")
_Sub10UnitMgmtSyncE_ObjectIdentity = ObjectIdentity
sub10UnitMgmtSyncE = _Sub10UnitMgmtSyncE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 13)
)


class _Sub10UnitMgmtSyncEMode_Type(Integer32):
    """Custom type sub10UnitMgmtSyncEMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syncEConsumer", 2),
          ("syncENone", 0),
          ("syncEProvider", 1))
    )


_Sub10UnitMgmtSyncEMode_Type.__name__ = "Integer32"
_Sub10UnitMgmtSyncEMode_Object = MibScalar
sub10UnitMgmtSyncEMode = _Sub10UnitMgmtSyncEMode_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 13, 1),
    _Sub10UnitMgmtSyncEMode_Type()
)
sub10UnitMgmtSyncEMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtSyncEMode.setStatus("current")
_Sub10UnitMgmtActions_ObjectIdentity = ObjectIdentity
sub10UnitMgmtActions = _Sub10UnitMgmtActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 20)
)


class _Sub10UnitMgmtTransaction_Type(Integer32):
    """Custom type sub10UnitMgmtTransaction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("transactionCommit", 2),
          ("transactionNone", 1),
          ("transactionRollback", 3))
    )


_Sub10UnitMgmtTransaction_Type.__name__ = "Integer32"
_Sub10UnitMgmtTransaction_Object = MibScalar
sub10UnitMgmtTransaction = _Sub10UnitMgmtTransaction_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 20, 1),
    _Sub10UnitMgmtTransaction_Type()
)
sub10UnitMgmtTransaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtTransaction.setStatus("current")


class _Sub10UnitMgmtTransactionStatus_Type(Integer32):
    """Custom type sub10UnitMgmtTransactionStatus based on Integer32"""
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
        *(("transStatusActive", 2),
          ("transStatusCommitted", 3),
          ("transStatusNone", 1),
          ("transStatusRollback", 4))
    )


_Sub10UnitMgmtTransactionStatus_Type.__name__ = "Integer32"
_Sub10UnitMgmtTransactionStatus_Object = MibScalar
sub10UnitMgmtTransactionStatus = _Sub10UnitMgmtTransactionStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 20, 2),
    _Sub10UnitMgmtTransactionStatus_Type()
)
sub10UnitMgmtTransactionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtTransactionStatus.setStatus("current")


class _Sub10UnitMgmtRollbackTimeout_Type(Unsigned32):
    """Custom type sub10UnitMgmtRollbackTimeout based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_Sub10UnitMgmtRollbackTimeout_Type.__name__ = "Unsigned32"
_Sub10UnitMgmtRollbackTimeout_Object = MibScalar
sub10UnitMgmtRollbackTimeout = _Sub10UnitMgmtRollbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 20, 3),
    _Sub10UnitMgmtRollbackTimeout_Type()
)
sub10UnitMgmtRollbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtRollbackTimeout.setStatus("current")


class _Sub10UnitMgmtTransactionMode_Type(Sub10State):
    """Custom type sub10UnitMgmtTransactionMode based on Sub10State"""


_Sub10UnitMgmtTransactionMode_Object = MibScalar
sub10UnitMgmtTransactionMode = _Sub10UnitMgmtTransactionMode_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 20, 4),
    _Sub10UnitMgmtTransactionMode_Type()
)
sub10UnitMgmtTransactionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtTransactionMode.setStatus("current")


class _Sub10UnitMgmtResetAction_Type(Integer32):
    """Custom type sub10UnitMgmtResetAction based on Integer32"""
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
        *(("resetAlarmConfig", 5),
          ("resetFactoryDefaults", 2),
          ("resetFactoryDefaultsNoSave", 3),
          ("resetNone", 1),
          ("resetStatistics", 4))
    )


_Sub10UnitMgmtResetAction_Type.__name__ = "Integer32"
_Sub10UnitMgmtResetAction_Object = MibScalar
sub10UnitMgmtResetAction = _Sub10UnitMgmtResetAction_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 20, 5),
    _Sub10UnitMgmtResetAction_Type()
)
sub10UnitMgmtResetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtResetAction.setStatus("current")
_Sub10UnitMgmtResetStatsGroup_Type = Sub10StatsGroup
_Sub10UnitMgmtResetStatsGroup_Object = MibScalar
sub10UnitMgmtResetStatsGroup = _Sub10UnitMgmtResetStatsGroup_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 20, 6),
    _Sub10UnitMgmtResetStatsGroup_Type()
)
sub10UnitMgmtResetStatsGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtResetStatsGroup.setStatus("current")


class _Sub10UnitMgmtResetAlarmsType_Type(Integer32):
    """Custom type sub10UnitMgmtResetAlarmsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("resetAlarmTypeAll", 1),
          ("resetAlarmTypeFixed", 2),
          ("resetAlarmTypeUser", 3))
    )


_Sub10UnitMgmtResetAlarmsType_Type.__name__ = "Integer32"
_Sub10UnitMgmtResetAlarmsType_Object = MibScalar
sub10UnitMgmtResetAlarmsType = _Sub10UnitMgmtResetAlarmsType_Object(
    (1, 3, 6, 1, 4, 1, 39003, 3, 2, 20, 7),
    _Sub10UnitMgmtResetAlarmsType_Type()
)
sub10UnitMgmtResetAlarmsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10UnitMgmtResetAlarmsType.setStatus("current")
_Sub10Ethernet_ObjectIdentity = ObjectIdentity
sub10Ethernet = _Sub10Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 4)
)
_Sub10EthernetStatus_ObjectIdentity = ObjectIdentity
sub10EthernetStatus = _Sub10EthernetStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1)
)
_Sub10EthernetLocalStatus_ObjectIdentity = ObjectIdentity
sub10EthernetLocalStatus = _Sub10EthernetLocalStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 1)
)
_Sub10EthLclStatusTable_Object = MibTable
sub10EthLclStatusTable = _Sub10EthLclStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sub10EthLclStatusTable.setStatus("current")
_Sub10EthLclStatusEntry_Object = MibTableRow
sub10EthLclStatusEntry = _Sub10EthLclStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 1, 1, 1)
)
sub10EthLclStatusEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10EthIfIndex"),
)
if mibBuilder.loadTexts:
    sub10EthLclStatusEntry.setStatus("current")
_Sub10EthLclLinkStatus_Type = Sub10OperStatus
_Sub10EthLclLinkStatus_Object = MibTableColumn
sub10EthLclLinkStatus = _Sub10EthLclLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 1, 1, 1, 1),
    _Sub10EthLclLinkStatus_Type()
)
sub10EthLclLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthLclLinkStatus.setStatus("current")
_Sub10EthLclMacAddress_Type = Sub10MacAddress
_Sub10EthLclMacAddress_Object = MibTableColumn
sub10EthLclMacAddress = _Sub10EthLclMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 1, 1, 1, 2),
    _Sub10EthLclMacAddress_Type()
)
sub10EthLclMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthLclMacAddress.setStatus("current")


class _Sub10EthLclSpeed_Type(Unsigned32):
    """Custom type sub10EthLclSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Sub10EthLclSpeed_Type.__name__ = "Unsigned32"
_Sub10EthLclSpeed_Object = MibTableColumn
sub10EthLclSpeed = _Sub10EthLclSpeed_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 1, 1, 1, 3),
    _Sub10EthLclSpeed_Type()
)
sub10EthLclSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthLclSpeed.setStatus("current")
_Sub10EthLclDuplex_Type = Sub10Duplex
_Sub10EthLclDuplex_Object = MibTableColumn
sub10EthLclDuplex = _Sub10EthLclDuplex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 1, 1, 1, 4),
    _Sub10EthLclDuplex_Type()
)
sub10EthLclDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthLclDuplex.setStatus("current")
_Sub10EthLclMDI_Type = Sub10MDIType
_Sub10EthLclMDI_Object = MibTableColumn
sub10EthLclMDI = _Sub10EthLclMDI_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 1, 1, 1, 5),
    _Sub10EthLclMDI_Type()
)
sub10EthLclMDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthLclMDI.setStatus("current")
_Sub10EthIfIndex_Type = Sub10EthInterfaceIndex
_Sub10EthIfIndex_Object = MibTableColumn
sub10EthIfIndex = _Sub10EthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 1, 1, 1, 6),
    _Sub10EthIfIndex_Type()
)
sub10EthIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10EthIfIndex.setStatus("current")
_Sub10EthernetRemoteStatus_ObjectIdentity = ObjectIdentity
sub10EthernetRemoteStatus = _Sub10EthernetRemoteStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 2)
)
_Sub10EthRmtStatusTable_Object = MibTable
sub10EthRmtStatusTable = _Sub10EthRmtStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sub10EthRmtStatusTable.setStatus("current")
_Sub10EthRmtStatusEntry_Object = MibTableRow
sub10EthRmtStatusEntry = _Sub10EthRmtStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 2, 1, 1)
)
sub10EthRmtStatusEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10EthIfIndex"),
)
if mibBuilder.loadTexts:
    sub10EthRmtStatusEntry.setStatus("current")
_Sub10EthRmtLinkStatus_Type = Sub10OperStatus
_Sub10EthRmtLinkStatus_Object = MibTableColumn
sub10EthRmtLinkStatus = _Sub10EthRmtLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 2, 1, 1, 1),
    _Sub10EthRmtLinkStatus_Type()
)
sub10EthRmtLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthRmtLinkStatus.setStatus("current")
_Sub10EthRmtMacAddress_Type = Sub10MacAddress
_Sub10EthRmtMacAddress_Object = MibTableColumn
sub10EthRmtMacAddress = _Sub10EthRmtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 2, 1, 1, 2),
    _Sub10EthRmtMacAddress_Type()
)
sub10EthRmtMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthRmtMacAddress.setStatus("current")


class _Sub10EthRmtSpeed_Type(Unsigned32):
    """Custom type sub10EthRmtSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Sub10EthRmtSpeed_Type.__name__ = "Unsigned32"
_Sub10EthRmtSpeed_Object = MibTableColumn
sub10EthRmtSpeed = _Sub10EthRmtSpeed_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 2, 1, 1, 3),
    _Sub10EthRmtSpeed_Type()
)
sub10EthRmtSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthRmtSpeed.setStatus("current")
_Sub10EthRmtDuplex_Type = Sub10Duplex
_Sub10EthRmtDuplex_Object = MibTableColumn
sub10EthRmtDuplex = _Sub10EthRmtDuplex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 2, 1, 1, 4),
    _Sub10EthRmtDuplex_Type()
)
sub10EthRmtDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthRmtDuplex.setStatus("current")
_Sub10EthRmtMDI_Type = Sub10MDIType
_Sub10EthRmtMDI_Object = MibTableColumn
sub10EthRmtMDI = _Sub10EthRmtMDI_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 1, 2, 1, 1, 5),
    _Sub10EthRmtMDI_Type()
)
sub10EthRmtMDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthRmtMDI.setStatus("current")
_Sub10EthernetMgmt_ObjectIdentity = ObjectIdentity
sub10EthernetMgmt = _Sub10EthernetMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2)
)
_Sub10EthMgmtPhy_ObjectIdentity = ObjectIdentity
sub10EthMgmtPhy = _Sub10EthMgmtPhy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 1)
)
_Sub10EthMgmtPhyTable_Object = MibTable
sub10EthMgmtPhyTable = _Sub10EthMgmtPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sub10EthMgmtPhyTable.setStatus("current")
_Sub10EthMgmtPhyEntry_Object = MibTableRow
sub10EthMgmtPhyEntry = _Sub10EthMgmtPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 1, 1, 1)
)
sub10EthMgmtPhyEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10EthIfIndex"),
)
if mibBuilder.loadTexts:
    sub10EthMgmtPhyEntry.setStatus("current")


class _Sub10EthMgmtPhyAutoNeg_Type(Sub10State):
    """Custom type sub10EthMgmtPhyAutoNeg based on Sub10State"""


_Sub10EthMgmtPhyAutoNeg_Object = MibTableColumn
sub10EthMgmtPhyAutoNeg = _Sub10EthMgmtPhyAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 1, 1, 1, 1),
    _Sub10EthMgmtPhyAutoNeg_Type()
)
sub10EthMgmtPhyAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtPhyAutoNeg.setStatus("current")


class _Sub10EthMgmtPhySpeed_Type(Unsigned32):
    """Custom type sub10EthMgmtPhySpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Sub10EthMgmtPhySpeed_Type.__name__ = "Unsigned32"
_Sub10EthMgmtPhySpeed_Object = MibTableColumn
sub10EthMgmtPhySpeed = _Sub10EthMgmtPhySpeed_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 1, 1, 1, 2),
    _Sub10EthMgmtPhySpeed_Type()
)
sub10EthMgmtPhySpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtPhySpeed.setStatus("current")
_Sub10EthMgmtPhyDuplex_Type = Sub10Duplex
_Sub10EthMgmtPhyDuplex_Object = MibTableColumn
sub10EthMgmtPhyDuplex = _Sub10EthMgmtPhyDuplex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 1, 1, 1, 3),
    _Sub10EthMgmtPhyDuplex_Type()
)
sub10EthMgmtPhyDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtPhyDuplex.setStatus("current")
_Sub10EthMgmtPhyMDI_Type = Sub10MDIType
_Sub10EthMgmtPhyMDI_Object = MibTableColumn
sub10EthMgmtPhyMDI = _Sub10EthMgmtPhyMDI_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 1, 1, 1, 4),
    _Sub10EthMgmtPhyMDI_Type()
)
sub10EthMgmtPhyMDI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtPhyMDI.setStatus("current")
_Sub10EthMgmtVlan_ObjectIdentity = ObjectIdentity
sub10EthMgmtVlan = _Sub10EthMgmtVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 2)
)


class _Sub10EthMgmtVlanFiltering_Type(Sub10State):
    """Custom type sub10EthMgmtVlanFiltering based on Sub10State"""


_Sub10EthMgmtVlanFiltering_Object = MibScalar
sub10EthMgmtVlanFiltering = _Sub10EthMgmtVlanFiltering_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 2, 1),
    _Sub10EthMgmtVlanFiltering_Type()
)
sub10EthMgmtVlanFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtVlanFiltering.setStatus("current")


class _Sub10EthMgmtVlanDefaultEnabled_Type(Sub10State):
    """Custom type sub10EthMgmtVlanDefaultEnabled based on Sub10State"""


_Sub10EthMgmtVlanDefaultEnabled_Object = MibScalar
sub10EthMgmtVlanDefaultEnabled = _Sub10EthMgmtVlanDefaultEnabled_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 2, 2),
    _Sub10EthMgmtVlanDefaultEnabled_Type()
)
sub10EthMgmtVlanDefaultEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtVlanDefaultEnabled.setStatus("current")


class _Sub10EthMgmtVlanDefaultId_Type(Sub10VlanId):
    """Custom type sub10EthMgmtVlanDefaultId based on Sub10VlanId"""
    defaultValue = 0


_Sub10EthMgmtVlanDefaultId_Object = MibScalar
sub10EthMgmtVlanDefaultId = _Sub10EthMgmtVlanDefaultId_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 2, 3),
    _Sub10EthMgmtVlanDefaultId_Type()
)
sub10EthMgmtVlanDefaultId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtVlanDefaultId.setStatus("current")


class _Sub10EthMgmtVlanDefaultPriority_Type(Sub10VlanPriority):
    """Custom type sub10EthMgmtVlanDefaultPriority based on Sub10VlanPriority"""
    defaultValue = 0


_Sub10EthMgmtVlanDefaultPriority_Object = MibScalar
sub10EthMgmtVlanDefaultPriority = _Sub10EthMgmtVlanDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 2, 4),
    _Sub10EthMgmtVlanDefaultPriority_Type()
)
sub10EthMgmtVlanDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtVlanDefaultPriority.setStatus("current")


class _Sub10EthMgmtVlanDefaultDEI_Type(Sub10State):
    """Custom type sub10EthMgmtVlanDefaultDEI based on Sub10State"""


_Sub10EthMgmtVlanDefaultDEI_Object = MibScalar
sub10EthMgmtVlanDefaultDEI = _Sub10EthMgmtVlanDefaultDEI_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 2, 5),
    _Sub10EthMgmtVlanDefaultDEI_Type()
)
sub10EthMgmtVlanDefaultDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtVlanDefaultDEI.setStatus("current")


class _Sub10EthMgmtVlanIngressAction_Type(Sub10VlanTagAction):
    """Custom type sub10EthMgmtVlanIngressAction based on Sub10VlanTagAction"""


_Sub10EthMgmtVlanIngressAction_Object = MibScalar
sub10EthMgmtVlanIngressAction = _Sub10EthMgmtVlanIngressAction_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 2, 6),
    _Sub10EthMgmtVlanIngressAction_Type()
)
sub10EthMgmtVlanIngressAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthMgmtVlanIngressAction.setStatus("current")


class _Sub10EthMgmtVlanEgressAction_Type(Sub10VlanTagAction):
    """Custom type sub10EthMgmtVlanEgressAction based on Sub10VlanTagAction"""


_Sub10EthMgmtVlanEgressAction_Object = MibScalar
sub10EthMgmtVlanEgressAction = _Sub10EthMgmtVlanEgressAction_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 2, 7),
    _Sub10EthMgmtVlanEgressAction_Type()
)
sub10EthMgmtVlanEgressAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthMgmtVlanEgressAction.setStatus("current")
_Sub10EthMgmtVlanAllowedTable_Object = MibTable
sub10EthMgmtVlanAllowedTable = _Sub10EthMgmtVlanAllowedTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 2, 8)
)
if mibBuilder.loadTexts:
    sub10EthMgmtVlanAllowedTable.setStatus("current")
_Sub10EthMgmtVlanAllowedEntry_Object = MibTableRow
sub10EthMgmtVlanAllowedEntry = _Sub10EthMgmtVlanAllowedEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 2, 8, 1)
)
sub10EthMgmtVlanAllowedEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10EthMgmtVlanAllowedIndex"),
)
if mibBuilder.loadTexts:
    sub10EthMgmtVlanAllowedEntry.setStatus("current")


class _Sub10EthMgmtVlanAllowedIndex_Type(Unsigned32):
    """Custom type sub10EthMgmtVlanAllowedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Sub10EthMgmtVlanAllowedIndex_Type.__name__ = "Unsigned32"
_Sub10EthMgmtVlanAllowedIndex_Object = MibTableColumn
sub10EthMgmtVlanAllowedIndex = _Sub10EthMgmtVlanAllowedIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 2, 8, 1, 1),
    _Sub10EthMgmtVlanAllowedIndex_Type()
)
sub10EthMgmtVlanAllowedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10EthMgmtVlanAllowedIndex.setStatus("current")


class _Sub10EthMgmtVlanAllowedRowStatus_Type(RowStatus):
    """Custom type sub10EthMgmtVlanAllowedRowStatus based on RowStatus"""


_Sub10EthMgmtVlanAllowedRowStatus_Object = MibTableColumn
sub10EthMgmtVlanAllowedRowStatus = _Sub10EthMgmtVlanAllowedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 2, 8, 1, 2),
    _Sub10EthMgmtVlanAllowedRowStatus_Type()
)
sub10EthMgmtVlanAllowedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sub10EthMgmtVlanAllowedRowStatus.setStatus("current")


class _Sub10EthMgmtVlanAllowedId_Type(Sub10VlanId):
    """Custom type sub10EthMgmtVlanAllowedId based on Sub10VlanId"""
    defaultValue = 0


_Sub10EthMgmtVlanAllowedId_Object = MibTableColumn
sub10EthMgmtVlanAllowedId = _Sub10EthMgmtVlanAllowedId_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 2, 8, 1, 3),
    _Sub10EthMgmtVlanAllowedId_Type()
)
sub10EthMgmtVlanAllowedId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtVlanAllowedId.setStatus("current")
_Sub10EthMgmtQoS_ObjectIdentity = ObjectIdentity
sub10EthMgmtQoS = _Sub10EthMgmtQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3)
)


class _Sub10EthMgmtQoSActiveState_Type(Sub10State):
    """Custom type sub10EthMgmtQoSActiveState based on Sub10State"""


_Sub10EthMgmtQoSActiveState_Object = MibScalar
sub10EthMgmtQoSActiveState = _Sub10EthMgmtQoSActiveState_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 1),
    _Sub10EthMgmtQoSActiveState_Type()
)
sub10EthMgmtQoSActiveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSActiveState.setStatus("current")


class _Sub10EthMgmtQoSMode_Type(Integer32):
    """Custom type sub10EthMgmtQoSMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qosEthernet", 1),
          ("qosIPMPLS", 2))
    )


_Sub10EthMgmtQoSMode_Type.__name__ = "Integer32"
_Sub10EthMgmtQoSMode_Object = MibScalar
sub10EthMgmtQoSMode = _Sub10EthMgmtQoSMode_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 2),
    _Sub10EthMgmtQoSMode_Type()
)
sub10EthMgmtQoSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSMode.setStatus("current")


class _Sub10EthMgmtQoSUntaggedQueue_Type(Sub10QoSQueue):
    """Custom type sub10EthMgmtQoSUntaggedQueue based on Sub10QoSQueue"""
    defaultValue = 0


_Sub10EthMgmtQoSUntaggedQueue_Object = MibScalar
sub10EthMgmtQoSUntaggedQueue = _Sub10EthMgmtQoSUntaggedQueue_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 3),
    _Sub10EthMgmtQoSUntaggedQueue_Type()
)
sub10EthMgmtQoSUntaggedQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSUntaggedQueue.setStatus("current")
_Sub10EthMgmtQoSQTable_Object = MibTable
sub10EthMgmtQoSQTable = _Sub10EthMgmtQoSQTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 4)
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSQTable.setStatus("current")
_Sub10EthMgmtQoSQEntry_Object = MibTableRow
sub10EthMgmtQoSQEntry = _Sub10EthMgmtQoSQEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 4, 1)
)
sub10EthMgmtQoSQEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10EthMgmtQoSQIndex"),
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSQEntry.setStatus("current")


class _Sub10EthMgmtQoSQIndex_Type(Unsigned32):
    """Custom type sub10EthMgmtQoSQIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Sub10EthMgmtQoSQIndex_Type.__name__ = "Unsigned32"
_Sub10EthMgmtQoSQIndex_Object = MibTableColumn
sub10EthMgmtQoSQIndex = _Sub10EthMgmtQoSQIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 4, 1, 1),
    _Sub10EthMgmtQoSQIndex_Type()
)
sub10EthMgmtQoSQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSQIndex.setStatus("current")


class _Sub10EthMgmtQoSQSchedulingType_Type(Integer32):
    """Custom type sub10EthMgmtQoSQSchedulingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qosDWRR", 2),
          ("qosSPQ", 1))
    )


_Sub10EthMgmtQoSQSchedulingType_Type.__name__ = "Integer32"
_Sub10EthMgmtQoSQSchedulingType_Object = MibTableColumn
sub10EthMgmtQoSQSchedulingType = _Sub10EthMgmtQoSQSchedulingType_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 4, 1, 2),
    _Sub10EthMgmtQoSQSchedulingType_Type()
)
sub10EthMgmtQoSQSchedulingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSQSchedulingType.setStatus("current")


class _Sub10EthMgmtQoSQDWRRWeight_Type(Unsigned32):
    """Custom type sub10EthMgmtQoSQDWRRWeight based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Sub10EthMgmtQoSQDWRRWeight_Type.__name__ = "Unsigned32"
_Sub10EthMgmtQoSQDWRRWeight_Object = MibTableColumn
sub10EthMgmtQoSQDWRRWeight = _Sub10EthMgmtQoSQDWRRWeight_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 4, 1, 3),
    _Sub10EthMgmtQoSQDWRRWeight_Type()
)
sub10EthMgmtQoSQDWRRWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSQDWRRWeight.setStatus("current")


class _Sub10EthMgmtQoSQCongestionPolicy_Type(Integer32):
    """Custom type sub10EthMgmtQoSQCongestionPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("qosTailDrop", 1)
    )


_Sub10EthMgmtQoSQCongestionPolicy_Type.__name__ = "Integer32"
_Sub10EthMgmtQoSQCongestionPolicy_Object = MibTableColumn
sub10EthMgmtQoSQCongestionPolicy = _Sub10EthMgmtQoSQCongestionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 4, 1, 4),
    _Sub10EthMgmtQoSQCongestionPolicy_Type()
)
sub10EthMgmtQoSQCongestionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSQCongestionPolicy.setStatus("current")


class _Sub10EthMgmtQoSQSizeMax_Type(Unsigned32):
    """Custom type sub10EthMgmtQoSQSizeMax based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Sub10EthMgmtQoSQSizeMax_Type.__name__ = "Unsigned32"
_Sub10EthMgmtQoSQSizeMax_Object = MibTableColumn
sub10EthMgmtQoSQSizeMax = _Sub10EthMgmtQoSQSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 4, 1, 5),
    _Sub10EthMgmtQoSQSizeMax_Type()
)
sub10EthMgmtQoSQSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSQSizeMax.setStatus("current")


class _Sub10EthMgmtQoSQLen_Type(Unsigned32):
    """Custom type sub10EthMgmtQoSQLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Sub10EthMgmtQoSQLen_Type.__name__ = "Unsigned32"
_Sub10EthMgmtQoSQLen_Object = MibTableColumn
sub10EthMgmtQoSQLen = _Sub10EthMgmtQoSQLen_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 4, 1, 6),
    _Sub10EthMgmtQoSQLen_Type()
)
sub10EthMgmtQoSQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSQLen.setStatus("current")


class _Sub10EthMgmtQoSVlanMappingNumber_Type(Unsigned32):
    """Custom type sub10EthMgmtQoSVlanMappingNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Sub10EthMgmtQoSVlanMappingNumber_Type.__name__ = "Unsigned32"
_Sub10EthMgmtQoSVlanMappingNumber_Object = MibScalar
sub10EthMgmtQoSVlanMappingNumber = _Sub10EthMgmtQoSVlanMappingNumber_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 5),
    _Sub10EthMgmtQoSVlanMappingNumber_Type()
)
sub10EthMgmtQoSVlanMappingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSVlanMappingNumber.setStatus("current")
_Sub10EthMgmtQoSVlanTable_Object = MibTable
sub10EthMgmtQoSVlanTable = _Sub10EthMgmtQoSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 6)
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSVlanTable.setStatus("current")
_Sub10EthMgmtQoSVlanEntry_Object = MibTableRow
sub10EthMgmtQoSVlanEntry = _Sub10EthMgmtQoSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 6, 1)
)
sub10EthMgmtQoSVlanEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10EthMgmtQoSVlanIndex"),
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSVlanEntry.setStatus("current")


class _Sub10EthMgmtQoSVlanIndex_Type(Unsigned32):
    """Custom type sub10EthMgmtQoSVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Sub10EthMgmtQoSVlanIndex_Type.__name__ = "Unsigned32"
_Sub10EthMgmtQoSVlanIndex_Object = MibTableColumn
sub10EthMgmtQoSVlanIndex = _Sub10EthMgmtQoSVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 6, 1, 1),
    _Sub10EthMgmtQoSVlanIndex_Type()
)
sub10EthMgmtQoSVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSVlanIndex.setStatus("current")


class _Sub10EthMgmtQoSVlanId_Type(Sub10VlanId):
    """Custom type sub10EthMgmtQoSVlanId based on Sub10VlanId"""
    defaultValue = 0


_Sub10EthMgmtQoSVlanId_Object = MibTableColumn
sub10EthMgmtQoSVlanId = _Sub10EthMgmtQoSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 6, 1, 2),
    _Sub10EthMgmtQoSVlanId_Type()
)
sub10EthMgmtQoSVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSVlanId.setStatus("current")
_Sub10EthMgmtQoSVlanQueue_Type = Sub10QoSQueue
_Sub10EthMgmtQoSVlanQueue_Object = MibTableColumn
sub10EthMgmtQoSVlanQueue = _Sub10EthMgmtQoSVlanQueue_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 6, 1, 3),
    _Sub10EthMgmtQoSVlanQueue_Type()
)
sub10EthMgmtQoSVlanQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSVlanQueue.setStatus("current")
_Sub10EthMgmtQoSPCPTable_Object = MibTable
sub10EthMgmtQoSPCPTable = _Sub10EthMgmtQoSPCPTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 8)
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSPCPTable.setStatus("current")
_Sub10EthMgmtQoSPCPEntry_Object = MibTableRow
sub10EthMgmtQoSPCPEntry = _Sub10EthMgmtQoSPCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 8, 1)
)
sub10EthMgmtQoSPCPEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10EthMgmtQoSPCPIndex"),
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSPCPEntry.setStatus("current")


class _Sub10EthMgmtQoSPCPIndex_Type(Unsigned32):
    """Custom type sub10EthMgmtQoSPCPIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Sub10EthMgmtQoSPCPIndex_Type.__name__ = "Unsigned32"
_Sub10EthMgmtQoSPCPIndex_Object = MibTableColumn
sub10EthMgmtQoSPCPIndex = _Sub10EthMgmtQoSPCPIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 8, 1, 1),
    _Sub10EthMgmtQoSPCPIndex_Type()
)
sub10EthMgmtQoSPCPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSPCPIndex.setStatus("current")
_Sub10EthMgmtQoSPCPQueue_Type = Sub10QoSQueue
_Sub10EthMgmtQoSPCPQueue_Object = MibTableColumn
sub10EthMgmtQoSPCPQueue = _Sub10EthMgmtQoSPCPQueue_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 8, 1, 2),
    _Sub10EthMgmtQoSPCPQueue_Type()
)
sub10EthMgmtQoSPCPQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSPCPQueue.setStatus("current")


class _Sub10EthMgmtQoSDSCPMappingNumber_Type(Unsigned32):
    """Custom type sub10EthMgmtQoSDSCPMappingNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Sub10EthMgmtQoSDSCPMappingNumber_Type.__name__ = "Unsigned32"
_Sub10EthMgmtQoSDSCPMappingNumber_Object = MibScalar
sub10EthMgmtQoSDSCPMappingNumber = _Sub10EthMgmtQoSDSCPMappingNumber_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 9),
    _Sub10EthMgmtQoSDSCPMappingNumber_Type()
)
sub10EthMgmtQoSDSCPMappingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSDSCPMappingNumber.setStatus("current")
_Sub10EthMgmtQoSDSCPTable_Object = MibTable
sub10EthMgmtQoSDSCPTable = _Sub10EthMgmtQoSDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 10)
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSDSCPTable.setStatus("current")
_Sub10EthMgmtQoSDSCPEntry_Object = MibTableRow
sub10EthMgmtQoSDSCPEntry = _Sub10EthMgmtQoSDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 10, 1)
)
sub10EthMgmtQoSDSCPEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10EthMgmtQoSDSCPIndex"),
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSDSCPEntry.setStatus("current")


class _Sub10EthMgmtQoSDSCPIndex_Type(Unsigned32):
    """Custom type sub10EthMgmtQoSDSCPIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Sub10EthMgmtQoSDSCPIndex_Type.__name__ = "Unsigned32"
_Sub10EthMgmtQoSDSCPIndex_Object = MibTableColumn
sub10EthMgmtQoSDSCPIndex = _Sub10EthMgmtQoSDSCPIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 10, 1, 1),
    _Sub10EthMgmtQoSDSCPIndex_Type()
)
sub10EthMgmtQoSDSCPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSDSCPIndex.setStatus("current")


class _Sub10EthMgmtQoSDSCPMarking_Type(Unsigned32):
    """Custom type sub10EthMgmtQoSDSCPMarking based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Sub10EthMgmtQoSDSCPMarking_Type.__name__ = "Unsigned32"
_Sub10EthMgmtQoSDSCPMarking_Object = MibTableColumn
sub10EthMgmtQoSDSCPMarking = _Sub10EthMgmtQoSDSCPMarking_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 10, 1, 2),
    _Sub10EthMgmtQoSDSCPMarking_Type()
)
sub10EthMgmtQoSDSCPMarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSDSCPMarking.setStatus("current")
_Sub10EthMgmtQoSDSCPQueue_Type = Sub10QoSQueue
_Sub10EthMgmtQoSDSCPQueue_Object = MibTableColumn
sub10EthMgmtQoSDSCPQueue = _Sub10EthMgmtQoSDSCPQueue_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 10, 1, 3),
    _Sub10EthMgmtQoSDSCPQueue_Type()
)
sub10EthMgmtQoSDSCPQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSDSCPQueue.setStatus("current")


class _Sub10EthMgmtQoSMPLSMappingNumber_Type(Unsigned32):
    """Custom type sub10EthMgmtQoSMPLSMappingNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Sub10EthMgmtQoSMPLSMappingNumber_Type.__name__ = "Unsigned32"
_Sub10EthMgmtQoSMPLSMappingNumber_Object = MibScalar
sub10EthMgmtQoSMPLSMappingNumber = _Sub10EthMgmtQoSMPLSMappingNumber_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 11),
    _Sub10EthMgmtQoSMPLSMappingNumber_Type()
)
sub10EthMgmtQoSMPLSMappingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSMPLSMappingNumber.setStatus("current")
_Sub10EthMgmtQoSMPLSTable_Object = MibTable
sub10EthMgmtQoSMPLSTable = _Sub10EthMgmtQoSMPLSTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 12)
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSMPLSTable.setStatus("current")
_Sub10EthMgmtQoSMPLSEntry_Object = MibTableRow
sub10EthMgmtQoSMPLSEntry = _Sub10EthMgmtQoSMPLSEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 12, 1)
)
sub10EthMgmtQoSMPLSEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10EthMgmtQoSMPLSIndex"),
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSMPLSEntry.setStatus("current")


class _Sub10EthMgmtQoSMPLSIndex_Type(Unsigned32):
    """Custom type sub10EthMgmtQoSMPLSIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Sub10EthMgmtQoSMPLSIndex_Type.__name__ = "Unsigned32"
_Sub10EthMgmtQoSMPLSIndex_Object = MibTableColumn
sub10EthMgmtQoSMPLSIndex = _Sub10EthMgmtQoSMPLSIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 12, 1, 1),
    _Sub10EthMgmtQoSMPLSIndex_Type()
)
sub10EthMgmtQoSMPLSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSMPLSIndex.setStatus("current")


class _Sub10EthMgmtQoSMPLSTrafficClass_Type(Unsigned32):
    """Custom type sub10EthMgmtQoSMPLSTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Sub10EthMgmtQoSMPLSTrafficClass_Type.__name__ = "Unsigned32"
_Sub10EthMgmtQoSMPLSTrafficClass_Object = MibTableColumn
sub10EthMgmtQoSMPLSTrafficClass = _Sub10EthMgmtQoSMPLSTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 12, 1, 2),
    _Sub10EthMgmtQoSMPLSTrafficClass_Type()
)
sub10EthMgmtQoSMPLSTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSMPLSTrafficClass.setStatus("current")
_Sub10EthMgmtQoSMPLSQueue_Type = Sub10QoSQueue
_Sub10EthMgmtQoSMPLSQueue_Object = MibTableColumn
sub10EthMgmtQoSMPLSQueue = _Sub10EthMgmtQoSMPLSQueue_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 3, 12, 1, 3),
    _Sub10EthMgmtQoSMPLSQueue_Type()
)
sub10EthMgmtQoSMPLSQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtQoSMPLSQueue.setStatus("current")
_Sub10EthMgmtStats_ObjectIdentity = ObjectIdentity
sub10EthMgmtStats = _Sub10EthMgmtStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 4)
)
_Sub10EthMgmtStatsActiveTable_Object = MibTable
sub10EthMgmtStatsActiveTable = _Sub10EthMgmtStatsActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sub10EthMgmtStatsActiveTable.setStatus("current")
_Sub10EthMgmtStatsActiveEntry_Object = MibTableRow
sub10EthMgmtStatsActiveEntry = _Sub10EthMgmtStatsActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 4, 1, 1)
)
sub10EthMgmtStatsActiveEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10EthMgmtStatsActiveIndex"),
)
if mibBuilder.loadTexts:
    sub10EthMgmtStatsActiveEntry.setStatus("current")


class _Sub10EthMgmtStatsActiveIndex_Type(Unsigned32):
    """Custom type sub10EthMgmtStatsActiveIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Sub10EthMgmtStatsActiveIndex_Type.__name__ = "Unsigned32"
_Sub10EthMgmtStatsActiveIndex_Object = MibTableColumn
sub10EthMgmtStatsActiveIndex = _Sub10EthMgmtStatsActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 4, 1, 1, 1),
    _Sub10EthMgmtStatsActiveIndex_Type()
)
sub10EthMgmtStatsActiveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10EthMgmtStatsActiveIndex.setStatus("current")


class _Sub10EthMgmtStatsActiveName_Type(OctetString):
    """Custom type sub10EthMgmtStatsActiveName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10EthMgmtStatsActiveName_Type.__name__ = "OctetString"
_Sub10EthMgmtStatsActiveName_Object = MibTableColumn
sub10EthMgmtStatsActiveName = _Sub10EthMgmtStatsActiveName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 4, 1, 1, 2),
    _Sub10EthMgmtStatsActiveName_Type()
)
sub10EthMgmtStatsActiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthMgmtStatsActiveName.setStatus("current")


class _Sub10EthMgmtStatsActiveState_Type(Sub10State):
    """Custom type sub10EthMgmtStatsActiveState based on Sub10State"""


_Sub10EthMgmtStatsActiveState_Object = MibTableColumn
sub10EthMgmtStatsActiveState = _Sub10EthMgmtStatsActiveState_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 2, 4, 1, 1, 3),
    _Sub10EthMgmtStatsActiveState_Type()
)
sub10EthMgmtStatsActiveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10EthMgmtStatsActiveState.setStatus("current")
_Sub10EthernetStats_ObjectIdentity = ObjectIdentity
sub10EthernetStats = _Sub10EthernetStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3)
)


class _Sub10EthStatsTimeElapsed_Type(OctetString):
    """Custom type sub10EthStatsTimeElapsed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10EthStatsTimeElapsed_Type.__name__ = "OctetString"
_Sub10EthStatsTimeElapsed_Object = MibScalar
sub10EthStatsTimeElapsed = _Sub10EthStatsTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 1),
    _Sub10EthStatsTimeElapsed_Type()
)
sub10EthStatsTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsTimeElapsed.setStatus("current")
_Sub10EthernetStatsCurrent_ObjectIdentity = ObjectIdentity
sub10EthernetStatsCurrent = _Sub10EthernetStatsCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2)
)
_Sub10EthernetStatsCurrTable_Object = MibTable
sub10EthernetStatsCurrTable = _Sub10EthernetStatsCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sub10EthernetStatsCurrTable.setStatus("current")
_Sub10EthernetStatsCurrEntry_Object = MibTableRow
sub10EthernetStatsCurrEntry = _Sub10EthernetStatsCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1)
)
sub10EthernetStatsCurrEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10EthIfIndex"),
)
if mibBuilder.loadTexts:
    sub10EthernetStatsCurrEntry.setStatus("current")
_Sub10EthStatsCurrRxOctets_Type = Counter32
_Sub10EthStatsCurrRxOctets_Object = MibTableColumn
sub10EthStatsCurrRxOctets = _Sub10EthStatsCurrRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 1),
    _Sub10EthStatsCurrRxOctets_Type()
)
sub10EthStatsCurrRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxOctets.setStatus("current")
_Sub10EthStatsCurrRxGoodFrms_Type = Counter32
_Sub10EthStatsCurrRxGoodFrms_Object = MibTableColumn
sub10EthStatsCurrRxGoodFrms = _Sub10EthStatsCurrRxGoodFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 2),
    _Sub10EthStatsCurrRxGoodFrms_Type()
)
sub10EthStatsCurrRxGoodFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxGoodFrms.setStatus("current")
_Sub10EthStatsCurrRxBcastFrms_Type = Counter32
_Sub10EthStatsCurrRxBcastFrms_Object = MibTableColumn
sub10EthStatsCurrRxBcastFrms = _Sub10EthStatsCurrRxBcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 3),
    _Sub10EthStatsCurrRxBcastFrms_Type()
)
sub10EthStatsCurrRxBcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxBcastFrms.setStatus("current")
_Sub10EthStatsCurrRxMcastFrms_Type = Counter32
_Sub10EthStatsCurrRxMcastFrms_Object = MibTableColumn
sub10EthStatsCurrRxMcastFrms = _Sub10EthStatsCurrRxMcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 4),
    _Sub10EthStatsCurrRxMcastFrms_Type()
)
sub10EthStatsCurrRxMcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxMcastFrms.setStatus("current")
_Sub10EthStatsCurrRxPauseFrms_Type = Counter32
_Sub10EthStatsCurrRxPauseFrms_Object = MibTableColumn
sub10EthStatsCurrRxPauseFrms = _Sub10EthStatsCurrRxPauseFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 5),
    _Sub10EthStatsCurrRxPauseFrms_Type()
)
sub10EthStatsCurrRxPauseFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxPauseFrms.setStatus("current")
_Sub10EthStatsCurrRxCRCErrs_Type = Counter32
_Sub10EthStatsCurrRxCRCErrs_Object = MibTableColumn
sub10EthStatsCurrRxCRCErrs = _Sub10EthStatsCurrRxCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 6),
    _Sub10EthStatsCurrRxCRCErrs_Type()
)
sub10EthStatsCurrRxCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxCRCErrs.setStatus("current")
_Sub10EthStatsCurrRxAlignErrs_Type = Counter32
_Sub10EthStatsCurrRxAlignErrs_Object = MibTableColumn
sub10EthStatsCurrRxAlignErrs = _Sub10EthStatsCurrRxAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 7),
    _Sub10EthStatsCurrRxAlignErrs_Type()
)
sub10EthStatsCurrRxAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxAlignErrs.setStatus("current")
_Sub10EthStatsCurrRxOversized_Type = Counter32
_Sub10EthStatsCurrRxOversized_Object = MibTableColumn
sub10EthStatsCurrRxOversized = _Sub10EthStatsCurrRxOversized_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 8),
    _Sub10EthStatsCurrRxOversized_Type()
)
sub10EthStatsCurrRxOversized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxOversized.setStatus("current")
_Sub10EthStatsCurrRxJabberFrms_Type = Counter32
_Sub10EthStatsCurrRxJabberFrms_Object = MibTableColumn
sub10EthStatsCurrRxJabberFrms = _Sub10EthStatsCurrRxJabberFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 9),
    _Sub10EthStatsCurrRxJabberFrms_Type()
)
sub10EthStatsCurrRxJabberFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxJabberFrms.setStatus("current")
_Sub10EthStatsCurrRxUndersized_Type = Counter32
_Sub10EthStatsCurrRxUndersized_Object = MibTableColumn
sub10EthStatsCurrRxUndersized = _Sub10EthStatsCurrRxUndersized_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 10),
    _Sub10EthStatsCurrRxUndersized_Type()
)
sub10EthStatsCurrRxUndersized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxUndersized.setStatus("current")
_Sub10EthStatsCurrRxFragments_Type = Counter32
_Sub10EthStatsCurrRxFragments_Object = MibTableColumn
sub10EthStatsCurrRxFragments = _Sub10EthStatsCurrRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 11),
    _Sub10EthStatsCurrRxFragments_Type()
)
sub10EthStatsCurrRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxFragments.setStatus("current")
_Sub10EthStatsCurrRxSOFOvrns_Type = Counter32
_Sub10EthStatsCurrRxSOFOvrns_Object = MibTableColumn
sub10EthStatsCurrRxSOFOvrns = _Sub10EthStatsCurrRxSOFOvrns_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 12),
    _Sub10EthStatsCurrRxSOFOvrns_Type()
)
sub10EthStatsCurrRxSOFOvrns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxSOFOvrns.setStatus("current")
_Sub10EthStatsCurrTxOctets_Type = Counter32
_Sub10EthStatsCurrTxOctets_Object = MibTableColumn
sub10EthStatsCurrTxOctets = _Sub10EthStatsCurrTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 13),
    _Sub10EthStatsCurrTxOctets_Type()
)
sub10EthStatsCurrTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxOctets.setStatus("current")
_Sub10EthStatsCurrTxGoodFrms_Type = Counter32
_Sub10EthStatsCurrTxGoodFrms_Object = MibTableColumn
sub10EthStatsCurrTxGoodFrms = _Sub10EthStatsCurrTxGoodFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 14),
    _Sub10EthStatsCurrTxGoodFrms_Type()
)
sub10EthStatsCurrTxGoodFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxGoodFrms.setStatus("current")
_Sub10EthStatsCurrTxBcastFrms_Type = Counter32
_Sub10EthStatsCurrTxBcastFrms_Object = MibTableColumn
sub10EthStatsCurrTxBcastFrms = _Sub10EthStatsCurrTxBcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 15),
    _Sub10EthStatsCurrTxBcastFrms_Type()
)
sub10EthStatsCurrTxBcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxBcastFrms.setStatus("current")
_Sub10EthStatsCurrTxMcastFrms_Type = Counter32
_Sub10EthStatsCurrTxMcastFrms_Object = MibTableColumn
sub10EthStatsCurrTxMcastFrms = _Sub10EthStatsCurrTxMcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 16),
    _Sub10EthStatsCurrTxMcastFrms_Type()
)
sub10EthStatsCurrTxMcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxMcastFrms.setStatus("current")
_Sub10EthStatsCurrTxPauseFrms_Type = Counter32
_Sub10EthStatsCurrTxPauseFrms_Object = MibTableColumn
sub10EthStatsCurrTxPauseFrms = _Sub10EthStatsCurrTxPauseFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 17),
    _Sub10EthStatsCurrTxPauseFrms_Type()
)
sub10EthStatsCurrTxPauseFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxPauseFrms.setStatus("current")
_Sub10EthStatsCurrTxDeferred_Type = Counter32
_Sub10EthStatsCurrTxDeferred_Object = MibTableColumn
sub10EthStatsCurrTxDeferred = _Sub10EthStatsCurrTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 18),
    _Sub10EthStatsCurrTxDeferred_Type()
)
sub10EthStatsCurrTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxDeferred.setStatus("current")
_Sub10EthStatsCurrTxCollsn_Type = Counter32
_Sub10EthStatsCurrTxCollsn_Object = MibTableColumn
sub10EthStatsCurrTxCollsn = _Sub10EthStatsCurrTxCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 19),
    _Sub10EthStatsCurrTxCollsn_Type()
)
sub10EthStatsCurrTxCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxCollsn.setStatus("current")
_Sub10EthStatsCurrTxSnglCollsn_Type = Counter32
_Sub10EthStatsCurrTxSnglCollsn_Object = MibTableColumn
sub10EthStatsCurrTxSnglCollsn = _Sub10EthStatsCurrTxSnglCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 20),
    _Sub10EthStatsCurrTxSnglCollsn_Type()
)
sub10EthStatsCurrTxSnglCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxSnglCollsn.setStatus("current")
_Sub10EthStatsCurrTxMlplCollsn_Type = Counter32
_Sub10EthStatsCurrTxMlplCollsn_Object = MibTableColumn
sub10EthStatsCurrTxMlplCollsn = _Sub10EthStatsCurrTxMlplCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 21),
    _Sub10EthStatsCurrTxMlplCollsn_Type()
)
sub10EthStatsCurrTxMlplCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxMlplCollsn.setStatus("current")
_Sub10EthStatsCurrTxExsvCollsn_Type = Counter32
_Sub10EthStatsCurrTxExsvCollsn_Object = MibTableColumn
sub10EthStatsCurrTxExsvCollsn = _Sub10EthStatsCurrTxExsvCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 22),
    _Sub10EthStatsCurrTxExsvCollsn_Type()
)
sub10EthStatsCurrTxExsvCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxExsvCollsn.setStatus("current")
_Sub10EthStatsCurrTxLtCollsn_Type = Counter32
_Sub10EthStatsCurrTxLtCollsn_Object = MibTableColumn
sub10EthStatsCurrTxLtCollsn = _Sub10EthStatsCurrTxLtCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 23),
    _Sub10EthStatsCurrTxLtCollsn_Type()
)
sub10EthStatsCurrTxLtCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxLtCollsn.setStatus("current")
_Sub10EthStatsCurrTxCSenseErrs_Type = Counter32
_Sub10EthStatsCurrTxCSenseErrs_Object = MibTableColumn
sub10EthStatsCurrTxCSenseErrs = _Sub10EthStatsCurrTxCSenseErrs_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 24),
    _Sub10EthStatsCurrTxCSenseErrs_Type()
)
sub10EthStatsCurrTxCSenseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxCSenseErrs.setStatus("current")
_Sub10EthStatsCurrPkts64Octets_Type = Counter32
_Sub10EthStatsCurrPkts64Octets_Object = MibTableColumn
sub10EthStatsCurrPkts64Octets = _Sub10EthStatsCurrPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 25),
    _Sub10EthStatsCurrPkts64Octets_Type()
)
sub10EthStatsCurrPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrPkts64Octets.setStatus("current")
_Sub10EthStatsCurrPkts65T127_Type = Counter32
_Sub10EthStatsCurrPkts65T127_Object = MibTableColumn
sub10EthStatsCurrPkts65T127 = _Sub10EthStatsCurrPkts65T127_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 26),
    _Sub10EthStatsCurrPkts65T127_Type()
)
sub10EthStatsCurrPkts65T127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrPkts65T127.setStatus("current")
_Sub10EthStatsCurrPkts128T255_Type = Counter32
_Sub10EthStatsCurrPkts128T255_Object = MibTableColumn
sub10EthStatsCurrPkts128T255 = _Sub10EthStatsCurrPkts128T255_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 27),
    _Sub10EthStatsCurrPkts128T255_Type()
)
sub10EthStatsCurrPkts128T255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrPkts128T255.setStatus("current")
_Sub10EthStatsCurrPkts256T511_Type = Counter32
_Sub10EthStatsCurrPkts256T511_Object = MibTableColumn
sub10EthStatsCurrPkts256T511 = _Sub10EthStatsCurrPkts256T511_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 28),
    _Sub10EthStatsCurrPkts256T511_Type()
)
sub10EthStatsCurrPkts256T511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrPkts256T511.setStatus("current")
_Sub10EthStatsCurrPkts512T1023_Type = Counter32
_Sub10EthStatsCurrPkts512T1023_Object = MibTableColumn
sub10EthStatsCurrPkts512T1023 = _Sub10EthStatsCurrPkts512T1023_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 29),
    _Sub10EthStatsCurrPkts512T1023_Type()
)
sub10EthStatsCurrPkts512T1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrPkts512T1023.setStatus("current")
_Sub10EthStatsCurrPkts1024TMax_Type = Counter32
_Sub10EthStatsCurrPkts1024TMax_Object = MibTableColumn
sub10EthStatsCurrPkts1024TMax = _Sub10EthStatsCurrPkts1024TMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 30),
    _Sub10EthStatsCurrPkts1024TMax_Type()
)
sub10EthStatsCurrPkts1024TMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrPkts1024TMax.setStatus("current")
_Sub10EthStatsCurrRxMbps_Type = Sub10ThroughputMbps
_Sub10EthStatsCurrRxMbps_Object = MibTableColumn
sub10EthStatsCurrRxMbps = _Sub10EthStatsCurrRxMbps_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 31),
    _Sub10EthStatsCurrRxMbps_Type()
)
sub10EthStatsCurrRxMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxMbps.setStatus("current")
_Sub10EthStatsCurrTxMbps_Type = Sub10ThroughputMbps
_Sub10EthStatsCurrTxMbps_Object = MibTableColumn
sub10EthStatsCurrTxMbps = _Sub10EthStatsCurrTxMbps_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 32),
    _Sub10EthStatsCurrTxMbps_Type()
)
sub10EthStatsCurrTxMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxMbps.setStatus("current")
_Sub10EthStatsCurrRxMbpsMin_Type = Sub10ThroughputMbps
_Sub10EthStatsCurrRxMbpsMin_Object = MibTableColumn
sub10EthStatsCurrRxMbpsMin = _Sub10EthStatsCurrRxMbpsMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 33),
    _Sub10EthStatsCurrRxMbpsMin_Type()
)
sub10EthStatsCurrRxMbpsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxMbpsMin.setStatus("current")
_Sub10EthStatsCurrRxMbpsMax_Type = Sub10ThroughputMbps
_Sub10EthStatsCurrRxMbpsMax_Object = MibTableColumn
sub10EthStatsCurrRxMbpsMax = _Sub10EthStatsCurrRxMbpsMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 34),
    _Sub10EthStatsCurrRxMbpsMax_Type()
)
sub10EthStatsCurrRxMbpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxMbpsMax.setStatus("current")
_Sub10EthStatsCurrRxMbpsAvg_Type = Sub10ThroughputMbps
_Sub10EthStatsCurrRxMbpsAvg_Object = MibTableColumn
sub10EthStatsCurrRxMbpsAvg = _Sub10EthStatsCurrRxMbpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 35),
    _Sub10EthStatsCurrRxMbpsAvg_Type()
)
sub10EthStatsCurrRxMbpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRxMbpsAvg.setStatus("current")
_Sub10EthStatsCurrTxMbpsMin_Type = Sub10ThroughputMbps
_Sub10EthStatsCurrTxMbpsMin_Object = MibTableColumn
sub10EthStatsCurrTxMbpsMin = _Sub10EthStatsCurrTxMbpsMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 36),
    _Sub10EthStatsCurrTxMbpsMin_Type()
)
sub10EthStatsCurrTxMbpsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxMbpsMin.setStatus("current")
_Sub10EthStatsCurrTxMbpsMax_Type = Sub10ThroughputMbps
_Sub10EthStatsCurrTxMbpsMax_Object = MibTableColumn
sub10EthStatsCurrTxMbpsMax = _Sub10EthStatsCurrTxMbpsMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 37),
    _Sub10EthStatsCurrTxMbpsMax_Type()
)
sub10EthStatsCurrTxMbpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxMbpsMax.setStatus("current")
_Sub10EthStatsCurrTxMbpsAvg_Type = Sub10ThroughputMbps
_Sub10EthStatsCurrTxMbpsAvg_Object = MibTableColumn
sub10EthStatsCurrTxMbpsAvg = _Sub10EthStatsCurrTxMbpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 38),
    _Sub10EthStatsCurrTxMbpsAvg_Type()
)
sub10EthStatsCurrTxMbpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrTxMbpsAvg.setStatus("current")
_Sub10EthStatsCurrRmtRxMbpsAvg_Type = Sub10ThroughputMbps
_Sub10EthStatsCurrRmtRxMbpsAvg_Object = MibTableColumn
sub10EthStatsCurrRmtRxMbpsAvg = _Sub10EthStatsCurrRmtRxMbpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 39),
    _Sub10EthStatsCurrRmtRxMbpsAvg_Type()
)
sub10EthStatsCurrRmtRxMbpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRmtRxMbpsAvg.setStatus("current")
_Sub10EthStatsCurrRmtTxMbpsAvg_Type = Sub10ThroughputMbps
_Sub10EthStatsCurrRmtTxMbpsAvg_Object = MibTableColumn
sub10EthStatsCurrRmtTxMbpsAvg = _Sub10EthStatsCurrRmtTxMbpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 2, 1, 1, 40),
    _Sub10EthStatsCurrRmtTxMbpsAvg_Type()
)
sub10EthStatsCurrRmtTxMbpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStatsCurrRmtTxMbpsAvg.setStatus("current")
_Sub10EthernetStatsHistory_ObjectIdentity = ObjectIdentity
sub10EthernetStatsHistory = _Sub10EthernetStatsHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3)
)
_Sub10EthernetStats15mHistory_ObjectIdentity = ObjectIdentity
sub10EthernetStats15mHistory = _Sub10EthernetStats15mHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1)
)


class _Sub10EthStats15mHistIntvls_Type(Unsigned32):
    """Custom type sub10EthStats15mHistIntvls based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Sub10EthStats15mHistIntvls_Type.__name__ = "Unsigned32"
_Sub10EthStats15mHistIntvls_Object = MibScalar
sub10EthStats15mHistIntvls = _Sub10EthStats15mHistIntvls_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 1),
    _Sub10EthStats15mHistIntvls_Type()
)
sub10EthStats15mHistIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistIntvls.setStatus("current")
_Sub10EthStats15mHistTable_Object = MibTable
sub10EthStats15mHistTable = _Sub10EthStats15mHistTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sub10EthStats15mHistTable.setStatus("current")
_Sub10EthStats15mHistEntry_Object = MibTableRow
sub10EthStats15mHistEntry = _Sub10EthStats15mHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1)
)
sub10EthStats15mHistEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10EthIfIndex"),
    (0, "SUB10SYSTEMS-MIB", "sub10EthStats15mHistIntvl"),
)
if mibBuilder.loadTexts:
    sub10EthStats15mHistEntry.setStatus("current")


class _Sub10EthStats15mHistIntvl_Type(Unsigned32):
    """Custom type sub10EthStats15mHistIntvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Sub10EthStats15mHistIntvl_Type.__name__ = "Unsigned32"
_Sub10EthStats15mHistIntvl_Object = MibTableColumn
sub10EthStats15mHistIntvl = _Sub10EthStats15mHistIntvl_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 1),
    _Sub10EthStats15mHistIntvl_Type()
)
sub10EthStats15mHistIntvl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10EthStats15mHistIntvl.setStatus("current")
_Sub10EthStats15mHistTime_Type = Sub10DateTime
_Sub10EthStats15mHistTime_Object = MibTableColumn
sub10EthStats15mHistTime = _Sub10EthStats15mHistTime_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 2),
    _Sub10EthStats15mHistTime_Type()
)
sub10EthStats15mHistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTime.setStatus("current")
_Sub10EthStats15mHistRxOctets_Type = Counter64
_Sub10EthStats15mHistRxOctets_Object = MibTableColumn
sub10EthStats15mHistRxOctets = _Sub10EthStats15mHistRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 3),
    _Sub10EthStats15mHistRxOctets_Type()
)
sub10EthStats15mHistRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxOctets.setStatus("current")
_Sub10EthStats15mHistRxGoodFrms_Type = Counter64
_Sub10EthStats15mHistRxGoodFrms_Object = MibTableColumn
sub10EthStats15mHistRxGoodFrms = _Sub10EthStats15mHistRxGoodFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 4),
    _Sub10EthStats15mHistRxGoodFrms_Type()
)
sub10EthStats15mHistRxGoodFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxGoodFrms.setStatus("current")
_Sub10EthStats15mHistRxBcastFrms_Type = Counter64
_Sub10EthStats15mHistRxBcastFrms_Object = MibTableColumn
sub10EthStats15mHistRxBcastFrms = _Sub10EthStats15mHistRxBcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 5),
    _Sub10EthStats15mHistRxBcastFrms_Type()
)
sub10EthStats15mHistRxBcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxBcastFrms.setStatus("current")
_Sub10EthStats15mHistRxMcastFrms_Type = Counter64
_Sub10EthStats15mHistRxMcastFrms_Object = MibTableColumn
sub10EthStats15mHistRxMcastFrms = _Sub10EthStats15mHistRxMcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 6),
    _Sub10EthStats15mHistRxMcastFrms_Type()
)
sub10EthStats15mHistRxMcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxMcastFrms.setStatus("current")
_Sub10EthStats15mHistRxPauseFrms_Type = Counter64
_Sub10EthStats15mHistRxPauseFrms_Object = MibTableColumn
sub10EthStats15mHistRxPauseFrms = _Sub10EthStats15mHistRxPauseFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 7),
    _Sub10EthStats15mHistRxPauseFrms_Type()
)
sub10EthStats15mHistRxPauseFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxPauseFrms.setStatus("current")
_Sub10EthStats15mHistRxCRCErrs_Type = Counter64
_Sub10EthStats15mHistRxCRCErrs_Object = MibTableColumn
sub10EthStats15mHistRxCRCErrs = _Sub10EthStats15mHistRxCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 8),
    _Sub10EthStats15mHistRxCRCErrs_Type()
)
sub10EthStats15mHistRxCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxCRCErrs.setStatus("current")
_Sub10EthStats15mHistRxAlignErrs_Type = Counter64
_Sub10EthStats15mHistRxAlignErrs_Object = MibTableColumn
sub10EthStats15mHistRxAlignErrs = _Sub10EthStats15mHistRxAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 9),
    _Sub10EthStats15mHistRxAlignErrs_Type()
)
sub10EthStats15mHistRxAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxAlignErrs.setStatus("current")
_Sub10EthStats15mHistRxOversized_Type = Counter64
_Sub10EthStats15mHistRxOversized_Object = MibTableColumn
sub10EthStats15mHistRxOversized = _Sub10EthStats15mHistRxOversized_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 10),
    _Sub10EthStats15mHistRxOversized_Type()
)
sub10EthStats15mHistRxOversized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxOversized.setStatus("current")
_Sub10EthStats15mHistRxJabberFrms_Type = Counter64
_Sub10EthStats15mHistRxJabberFrms_Object = MibTableColumn
sub10EthStats15mHistRxJabberFrms = _Sub10EthStats15mHistRxJabberFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 11),
    _Sub10EthStats15mHistRxJabberFrms_Type()
)
sub10EthStats15mHistRxJabberFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxJabberFrms.setStatus("current")
_Sub10EthStats15mHistRxUndersized_Type = Counter64
_Sub10EthStats15mHistRxUndersized_Object = MibTableColumn
sub10EthStats15mHistRxUndersized = _Sub10EthStats15mHistRxUndersized_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 12),
    _Sub10EthStats15mHistRxUndersized_Type()
)
sub10EthStats15mHistRxUndersized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxUndersized.setStatus("current")
_Sub10EthStats15mHistRxFragments_Type = Counter64
_Sub10EthStats15mHistRxFragments_Object = MibTableColumn
sub10EthStats15mHistRxFragments = _Sub10EthStats15mHistRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 13),
    _Sub10EthStats15mHistRxFragments_Type()
)
sub10EthStats15mHistRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxFragments.setStatus("current")
_Sub10EthStats15mHistRxSOFOvrns_Type = Counter64
_Sub10EthStats15mHistRxSOFOvrns_Object = MibTableColumn
sub10EthStats15mHistRxSOFOvrns = _Sub10EthStats15mHistRxSOFOvrns_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 14),
    _Sub10EthStats15mHistRxSOFOvrns_Type()
)
sub10EthStats15mHistRxSOFOvrns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxSOFOvrns.setStatus("current")
_Sub10EthStats15mHistTxOctets_Type = Counter64
_Sub10EthStats15mHistTxOctets_Object = MibTableColumn
sub10EthStats15mHistTxOctets = _Sub10EthStats15mHistTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 15),
    _Sub10EthStats15mHistTxOctets_Type()
)
sub10EthStats15mHistTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxOctets.setStatus("current")
_Sub10EthStats15mHistTxGoodFrms_Type = Counter64
_Sub10EthStats15mHistTxGoodFrms_Object = MibTableColumn
sub10EthStats15mHistTxGoodFrms = _Sub10EthStats15mHistTxGoodFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 16),
    _Sub10EthStats15mHistTxGoodFrms_Type()
)
sub10EthStats15mHistTxGoodFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxGoodFrms.setStatus("current")
_Sub10EthStats15mHistTxBcastFrms_Type = Counter64
_Sub10EthStats15mHistTxBcastFrms_Object = MibTableColumn
sub10EthStats15mHistTxBcastFrms = _Sub10EthStats15mHistTxBcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 17),
    _Sub10EthStats15mHistTxBcastFrms_Type()
)
sub10EthStats15mHistTxBcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxBcastFrms.setStatus("current")
_Sub10EthStats15mHistTxMcastFrms_Type = Counter64
_Sub10EthStats15mHistTxMcastFrms_Object = MibTableColumn
sub10EthStats15mHistTxMcastFrms = _Sub10EthStats15mHistTxMcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 18),
    _Sub10EthStats15mHistTxMcastFrms_Type()
)
sub10EthStats15mHistTxMcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxMcastFrms.setStatus("current")
_Sub10EthStats15mHistTxPauseFrms_Type = Counter64
_Sub10EthStats15mHistTxPauseFrms_Object = MibTableColumn
sub10EthStats15mHistTxPauseFrms = _Sub10EthStats15mHistTxPauseFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 19),
    _Sub10EthStats15mHistTxPauseFrms_Type()
)
sub10EthStats15mHistTxPauseFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxPauseFrms.setStatus("current")
_Sub10EthStats15mHistTxDeferred_Type = Counter64
_Sub10EthStats15mHistTxDeferred_Object = MibTableColumn
sub10EthStats15mHistTxDeferred = _Sub10EthStats15mHistTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 20),
    _Sub10EthStats15mHistTxDeferred_Type()
)
sub10EthStats15mHistTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxDeferred.setStatus("current")
_Sub10EthStats15mHistTxCollsn_Type = Counter64
_Sub10EthStats15mHistTxCollsn_Object = MibTableColumn
sub10EthStats15mHistTxCollsn = _Sub10EthStats15mHistTxCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 21),
    _Sub10EthStats15mHistTxCollsn_Type()
)
sub10EthStats15mHistTxCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxCollsn.setStatus("current")
_Sub10EthStats15mHistTxSnglCollsn_Type = Counter64
_Sub10EthStats15mHistTxSnglCollsn_Object = MibTableColumn
sub10EthStats15mHistTxSnglCollsn = _Sub10EthStats15mHistTxSnglCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 22),
    _Sub10EthStats15mHistTxSnglCollsn_Type()
)
sub10EthStats15mHistTxSnglCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxSnglCollsn.setStatus("current")
_Sub10EthStats15mHistTxMlplCollsn_Type = Counter64
_Sub10EthStats15mHistTxMlplCollsn_Object = MibTableColumn
sub10EthStats15mHistTxMlplCollsn = _Sub10EthStats15mHistTxMlplCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 23),
    _Sub10EthStats15mHistTxMlplCollsn_Type()
)
sub10EthStats15mHistTxMlplCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxMlplCollsn.setStatus("current")
_Sub10EthStats15mHistTxExsvCollsn_Type = Counter64
_Sub10EthStats15mHistTxExsvCollsn_Object = MibTableColumn
sub10EthStats15mHistTxExsvCollsn = _Sub10EthStats15mHistTxExsvCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 24),
    _Sub10EthStats15mHistTxExsvCollsn_Type()
)
sub10EthStats15mHistTxExsvCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxExsvCollsn.setStatus("current")
_Sub10EthStats15mHistTxLtCollsn_Type = Counter64
_Sub10EthStats15mHistTxLtCollsn_Object = MibTableColumn
sub10EthStats15mHistTxLtCollsn = _Sub10EthStats15mHistTxLtCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 25),
    _Sub10EthStats15mHistTxLtCollsn_Type()
)
sub10EthStats15mHistTxLtCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxLtCollsn.setStatus("current")
_Sub10EthStats15mHistTxCSenseErrs_Type = Counter64
_Sub10EthStats15mHistTxCSenseErrs_Object = MibTableColumn
sub10EthStats15mHistTxCSenseErrs = _Sub10EthStats15mHistTxCSenseErrs_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 26),
    _Sub10EthStats15mHistTxCSenseErrs_Type()
)
sub10EthStats15mHistTxCSenseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxCSenseErrs.setStatus("current")
_Sub10EthStats15mHistPkts64Octets_Type = Counter64
_Sub10EthStats15mHistPkts64Octets_Object = MibTableColumn
sub10EthStats15mHistPkts64Octets = _Sub10EthStats15mHistPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 27),
    _Sub10EthStats15mHistPkts64Octets_Type()
)
sub10EthStats15mHistPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistPkts64Octets.setStatus("current")
_Sub10EthStats15mHistPkts65T127_Type = Counter64
_Sub10EthStats15mHistPkts65T127_Object = MibTableColumn
sub10EthStats15mHistPkts65T127 = _Sub10EthStats15mHistPkts65T127_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 28),
    _Sub10EthStats15mHistPkts65T127_Type()
)
sub10EthStats15mHistPkts65T127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistPkts65T127.setStatus("current")
_Sub10EthStats15mHistPkts128T255_Type = Counter64
_Sub10EthStats15mHistPkts128T255_Object = MibTableColumn
sub10EthStats15mHistPkts128T255 = _Sub10EthStats15mHistPkts128T255_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 29),
    _Sub10EthStats15mHistPkts128T255_Type()
)
sub10EthStats15mHistPkts128T255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistPkts128T255.setStatus("current")
_Sub10EthStats15mHistPkts256T511_Type = Counter64
_Sub10EthStats15mHistPkts256T511_Object = MibTableColumn
sub10EthStats15mHistPkts256T511 = _Sub10EthStats15mHistPkts256T511_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 30),
    _Sub10EthStats15mHistPkts256T511_Type()
)
sub10EthStats15mHistPkts256T511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistPkts256T511.setStatus("current")
_Sub10EthStats15mHistPkts512T1023_Type = Counter64
_Sub10EthStats15mHistPkts512T1023_Object = MibTableColumn
sub10EthStats15mHistPkts512T1023 = _Sub10EthStats15mHistPkts512T1023_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 31),
    _Sub10EthStats15mHistPkts512T1023_Type()
)
sub10EthStats15mHistPkts512T1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistPkts512T1023.setStatus("current")
_Sub10EthStats15mHistPkts1024TMax_Type = Counter64
_Sub10EthStats15mHistPkts1024TMax_Object = MibTableColumn
sub10EthStats15mHistPkts1024TMax = _Sub10EthStats15mHistPkts1024TMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 32),
    _Sub10EthStats15mHistPkts1024TMax_Type()
)
sub10EthStats15mHistPkts1024TMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistPkts1024TMax.setStatus("current")
_Sub10EthStats15mHistRxMbpsMin_Type = Sub10ThroughputMbps
_Sub10EthStats15mHistRxMbpsMin_Object = MibTableColumn
sub10EthStats15mHistRxMbpsMin = _Sub10EthStats15mHistRxMbpsMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 33),
    _Sub10EthStats15mHistRxMbpsMin_Type()
)
sub10EthStats15mHistRxMbpsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxMbpsMin.setStatus("current")
_Sub10EthStats15mHistRxMbpsMax_Type = Sub10ThroughputMbps
_Sub10EthStats15mHistRxMbpsMax_Object = MibTableColumn
sub10EthStats15mHistRxMbpsMax = _Sub10EthStats15mHistRxMbpsMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 34),
    _Sub10EthStats15mHistRxMbpsMax_Type()
)
sub10EthStats15mHistRxMbpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxMbpsMax.setStatus("current")
_Sub10EthStats15mHistRxMbpsAvg_Type = Sub10ThroughputMbps
_Sub10EthStats15mHistRxMbpsAvg_Object = MibTableColumn
sub10EthStats15mHistRxMbpsAvg = _Sub10EthStats15mHistRxMbpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 35),
    _Sub10EthStats15mHistRxMbpsAvg_Type()
)
sub10EthStats15mHistRxMbpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistRxMbpsAvg.setStatus("current")
_Sub10EthStats15mHistTxMbpsMin_Type = Sub10ThroughputMbps
_Sub10EthStats15mHistTxMbpsMin_Object = MibTableColumn
sub10EthStats15mHistTxMbpsMin = _Sub10EthStats15mHistTxMbpsMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 36),
    _Sub10EthStats15mHistTxMbpsMin_Type()
)
sub10EthStats15mHistTxMbpsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxMbpsMin.setStatus("current")
_Sub10EthStats15mHistTxMbpsMax_Type = Sub10ThroughputMbps
_Sub10EthStats15mHistTxMbpsMax_Object = MibTableColumn
sub10EthStats15mHistTxMbpsMax = _Sub10EthStats15mHistTxMbpsMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 37),
    _Sub10EthStats15mHistTxMbpsMax_Type()
)
sub10EthStats15mHistTxMbpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxMbpsMax.setStatus("current")
_Sub10EthStats15mHistTxMbpsAvg_Type = Sub10ThroughputMbps
_Sub10EthStats15mHistTxMbpsAvg_Object = MibTableColumn
sub10EthStats15mHistTxMbpsAvg = _Sub10EthStats15mHistTxMbpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 1, 2, 1, 38),
    _Sub10EthStats15mHistTxMbpsAvg_Type()
)
sub10EthStats15mHistTxMbpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats15mHistTxMbpsAvg.setStatus("current")
_Sub10EthStats1dHistory_ObjectIdentity = ObjectIdentity
sub10EthStats1dHistory = _Sub10EthStats1dHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2)
)


class _Sub10EthStats1dHistIntvls_Type(Unsigned32):
    """Custom type sub10EthStats1dHistIntvls based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Sub10EthStats1dHistIntvls_Type.__name__ = "Unsigned32"
_Sub10EthStats1dHistIntvls_Object = MibScalar
sub10EthStats1dHistIntvls = _Sub10EthStats1dHistIntvls_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 1),
    _Sub10EthStats1dHistIntvls_Type()
)
sub10EthStats1dHistIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistIntvls.setStatus("current")
_Sub10EthStats1dHistTable_Object = MibTable
sub10EthStats1dHistTable = _Sub10EthStats1dHistTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    sub10EthStats1dHistTable.setStatus("current")
_Sub10EthStats1dHistEntry_Object = MibTableRow
sub10EthStats1dHistEntry = _Sub10EthStats1dHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1)
)
sub10EthStats1dHistEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10EthIfIndex"),
    (0, "SUB10SYSTEMS-MIB", "sub10EthStats1dHistIntvl"),
)
if mibBuilder.loadTexts:
    sub10EthStats1dHistEntry.setStatus("current")


class _Sub10EthStats1dHistIntvl_Type(Unsigned32):
    """Custom type sub10EthStats1dHistIntvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Sub10EthStats1dHistIntvl_Type.__name__ = "Unsigned32"
_Sub10EthStats1dHistIntvl_Object = MibTableColumn
sub10EthStats1dHistIntvl = _Sub10EthStats1dHistIntvl_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 1),
    _Sub10EthStats1dHistIntvl_Type()
)
sub10EthStats1dHistIntvl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10EthStats1dHistIntvl.setStatus("current")
_Sub10EthStats1dHistTime_Type = Sub10DateTime
_Sub10EthStats1dHistTime_Object = MibTableColumn
sub10EthStats1dHistTime = _Sub10EthStats1dHistTime_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 2),
    _Sub10EthStats1dHistTime_Type()
)
sub10EthStats1dHistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTime.setStatus("current")
_Sub10EthStats1dHistRxOctets_Type = Counter64
_Sub10EthStats1dHistRxOctets_Object = MibTableColumn
sub10EthStats1dHistRxOctets = _Sub10EthStats1dHistRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 3),
    _Sub10EthStats1dHistRxOctets_Type()
)
sub10EthStats1dHistRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxOctets.setStatus("current")
_Sub10EthStats1dHistRxGoodFrms_Type = Counter64
_Sub10EthStats1dHistRxGoodFrms_Object = MibTableColumn
sub10EthStats1dHistRxGoodFrms = _Sub10EthStats1dHistRxGoodFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 4),
    _Sub10EthStats1dHistRxGoodFrms_Type()
)
sub10EthStats1dHistRxGoodFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxGoodFrms.setStatus("current")
_Sub10EthStats1dHistRxBcastFrms_Type = Counter64
_Sub10EthStats1dHistRxBcastFrms_Object = MibTableColumn
sub10EthStats1dHistRxBcastFrms = _Sub10EthStats1dHistRxBcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 5),
    _Sub10EthStats1dHistRxBcastFrms_Type()
)
sub10EthStats1dHistRxBcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxBcastFrms.setStatus("current")
_Sub10EthStats1dHistRxMcastFrms_Type = Counter64
_Sub10EthStats1dHistRxMcastFrms_Object = MibTableColumn
sub10EthStats1dHistRxMcastFrms = _Sub10EthStats1dHistRxMcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 6),
    _Sub10EthStats1dHistRxMcastFrms_Type()
)
sub10EthStats1dHistRxMcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxMcastFrms.setStatus("current")
_Sub10EthStats1dHistRxPauseFrms_Type = Counter64
_Sub10EthStats1dHistRxPauseFrms_Object = MibTableColumn
sub10EthStats1dHistRxPauseFrms = _Sub10EthStats1dHistRxPauseFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 7),
    _Sub10EthStats1dHistRxPauseFrms_Type()
)
sub10EthStats1dHistRxPauseFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxPauseFrms.setStatus("current")
_Sub10EthStats1dHistRxCRCErrs_Type = Counter64
_Sub10EthStats1dHistRxCRCErrs_Object = MibTableColumn
sub10EthStats1dHistRxCRCErrs = _Sub10EthStats1dHistRxCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 8),
    _Sub10EthStats1dHistRxCRCErrs_Type()
)
sub10EthStats1dHistRxCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxCRCErrs.setStatus("current")
_Sub10EthStats1dHistRxAlignErrs_Type = Counter64
_Sub10EthStats1dHistRxAlignErrs_Object = MibTableColumn
sub10EthStats1dHistRxAlignErrs = _Sub10EthStats1dHistRxAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 9),
    _Sub10EthStats1dHistRxAlignErrs_Type()
)
sub10EthStats1dHistRxAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxAlignErrs.setStatus("current")
_Sub10EthStats1dHistRxOversized_Type = Counter64
_Sub10EthStats1dHistRxOversized_Object = MibTableColumn
sub10EthStats1dHistRxOversized = _Sub10EthStats1dHistRxOversized_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 10),
    _Sub10EthStats1dHistRxOversized_Type()
)
sub10EthStats1dHistRxOversized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxOversized.setStatus("current")
_Sub10EthStats1dHistRxJabberFrms_Type = Counter64
_Sub10EthStats1dHistRxJabberFrms_Object = MibTableColumn
sub10EthStats1dHistRxJabberFrms = _Sub10EthStats1dHistRxJabberFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 11),
    _Sub10EthStats1dHistRxJabberFrms_Type()
)
sub10EthStats1dHistRxJabberFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxJabberFrms.setStatus("current")
_Sub10EthStats1dHistRxUndersized_Type = Counter64
_Sub10EthStats1dHistRxUndersized_Object = MibTableColumn
sub10EthStats1dHistRxUndersized = _Sub10EthStats1dHistRxUndersized_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 12),
    _Sub10EthStats1dHistRxUndersized_Type()
)
sub10EthStats1dHistRxUndersized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxUndersized.setStatus("current")
_Sub10EthStats1dHistRxFragments_Type = Counter64
_Sub10EthStats1dHistRxFragments_Object = MibTableColumn
sub10EthStats1dHistRxFragments = _Sub10EthStats1dHistRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 13),
    _Sub10EthStats1dHistRxFragments_Type()
)
sub10EthStats1dHistRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxFragments.setStatus("current")
_Sub10EthStats1dHistRxSOFOvrns_Type = Counter64
_Sub10EthStats1dHistRxSOFOvrns_Object = MibTableColumn
sub10EthStats1dHistRxSOFOvrns = _Sub10EthStats1dHistRxSOFOvrns_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 14),
    _Sub10EthStats1dHistRxSOFOvrns_Type()
)
sub10EthStats1dHistRxSOFOvrns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxSOFOvrns.setStatus("current")
_Sub10EthStats1dHistTxOctets_Type = Counter64
_Sub10EthStats1dHistTxOctets_Object = MibTableColumn
sub10EthStats1dHistTxOctets = _Sub10EthStats1dHistTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 15),
    _Sub10EthStats1dHistTxOctets_Type()
)
sub10EthStats1dHistTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxOctets.setStatus("current")
_Sub10EthStats1dHistTxGoodFrms_Type = Counter64
_Sub10EthStats1dHistTxGoodFrms_Object = MibTableColumn
sub10EthStats1dHistTxGoodFrms = _Sub10EthStats1dHistTxGoodFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 16),
    _Sub10EthStats1dHistTxGoodFrms_Type()
)
sub10EthStats1dHistTxGoodFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxGoodFrms.setStatus("current")
_Sub10EthStats1dHistTxBcastFrms_Type = Counter64
_Sub10EthStats1dHistTxBcastFrms_Object = MibTableColumn
sub10EthStats1dHistTxBcastFrms = _Sub10EthStats1dHistTxBcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 17),
    _Sub10EthStats1dHistTxBcastFrms_Type()
)
sub10EthStats1dHistTxBcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxBcastFrms.setStatus("current")
_Sub10EthStats1dHistTxMcastFrms_Type = Counter64
_Sub10EthStats1dHistTxMcastFrms_Object = MibTableColumn
sub10EthStats1dHistTxMcastFrms = _Sub10EthStats1dHistTxMcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 18),
    _Sub10EthStats1dHistTxMcastFrms_Type()
)
sub10EthStats1dHistTxMcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxMcastFrms.setStatus("current")
_Sub10EthStats1dHistTxPauseFrms_Type = Counter64
_Sub10EthStats1dHistTxPauseFrms_Object = MibTableColumn
sub10EthStats1dHistTxPauseFrms = _Sub10EthStats1dHistTxPauseFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 19),
    _Sub10EthStats1dHistTxPauseFrms_Type()
)
sub10EthStats1dHistTxPauseFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxPauseFrms.setStatus("current")
_Sub10EthStats1dHistTxDeferred_Type = Counter64
_Sub10EthStats1dHistTxDeferred_Object = MibTableColumn
sub10EthStats1dHistTxDeferred = _Sub10EthStats1dHistTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 20),
    _Sub10EthStats1dHistTxDeferred_Type()
)
sub10EthStats1dHistTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxDeferred.setStatus("current")
_Sub10EthStats1dHistTxCollsn_Type = Counter64
_Sub10EthStats1dHistTxCollsn_Object = MibTableColumn
sub10EthStats1dHistTxCollsn = _Sub10EthStats1dHistTxCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 21),
    _Sub10EthStats1dHistTxCollsn_Type()
)
sub10EthStats1dHistTxCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxCollsn.setStatus("current")
_Sub10EthStats1dHistTxSnglCollsn_Type = Counter64
_Sub10EthStats1dHistTxSnglCollsn_Object = MibTableColumn
sub10EthStats1dHistTxSnglCollsn = _Sub10EthStats1dHistTxSnglCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 22),
    _Sub10EthStats1dHistTxSnglCollsn_Type()
)
sub10EthStats1dHistTxSnglCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxSnglCollsn.setStatus("current")
_Sub10EthStats1dHistTxMlplCollsn_Type = Counter64
_Sub10EthStats1dHistTxMlplCollsn_Object = MibTableColumn
sub10EthStats1dHistTxMlplCollsn = _Sub10EthStats1dHistTxMlplCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 23),
    _Sub10EthStats1dHistTxMlplCollsn_Type()
)
sub10EthStats1dHistTxMlplCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxMlplCollsn.setStatus("current")
_Sub10EthStats1dHistTxExsvCollsn_Type = Counter64
_Sub10EthStats1dHistTxExsvCollsn_Object = MibTableColumn
sub10EthStats1dHistTxExsvCollsn = _Sub10EthStats1dHistTxExsvCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 24),
    _Sub10EthStats1dHistTxExsvCollsn_Type()
)
sub10EthStats1dHistTxExsvCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxExsvCollsn.setStatus("current")
_Sub10EthStats1dHistTxLtCollsn_Type = Counter64
_Sub10EthStats1dHistTxLtCollsn_Object = MibTableColumn
sub10EthStats1dHistTxLtCollsn = _Sub10EthStats1dHistTxLtCollsn_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 25),
    _Sub10EthStats1dHistTxLtCollsn_Type()
)
sub10EthStats1dHistTxLtCollsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxLtCollsn.setStatus("current")
_Sub10EthStats1dHistTxCSenseErrs_Type = Counter64
_Sub10EthStats1dHistTxCSenseErrs_Object = MibTableColumn
sub10EthStats1dHistTxCSenseErrs = _Sub10EthStats1dHistTxCSenseErrs_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 26),
    _Sub10EthStats1dHistTxCSenseErrs_Type()
)
sub10EthStats1dHistTxCSenseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxCSenseErrs.setStatus("current")
_Sub10EthStats1dHistPkts64Octets_Type = Counter64
_Sub10EthStats1dHistPkts64Octets_Object = MibTableColumn
sub10EthStats1dHistPkts64Octets = _Sub10EthStats1dHistPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 27),
    _Sub10EthStats1dHistPkts64Octets_Type()
)
sub10EthStats1dHistPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistPkts64Octets.setStatus("current")
_Sub10EthStats1dHistPkts65T127_Type = Counter64
_Sub10EthStats1dHistPkts65T127_Object = MibTableColumn
sub10EthStats1dHistPkts65T127 = _Sub10EthStats1dHistPkts65T127_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 28),
    _Sub10EthStats1dHistPkts65T127_Type()
)
sub10EthStats1dHistPkts65T127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistPkts65T127.setStatus("current")
_Sub10EthStats1dHistPkts128T255_Type = Counter64
_Sub10EthStats1dHistPkts128T255_Object = MibTableColumn
sub10EthStats1dHistPkts128T255 = _Sub10EthStats1dHistPkts128T255_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 29),
    _Sub10EthStats1dHistPkts128T255_Type()
)
sub10EthStats1dHistPkts128T255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistPkts128T255.setStatus("current")
_Sub10EthStats1dHistPkts256T511_Type = Counter64
_Sub10EthStats1dHistPkts256T511_Object = MibTableColumn
sub10EthStats1dHistPkts256T511 = _Sub10EthStats1dHistPkts256T511_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 30),
    _Sub10EthStats1dHistPkts256T511_Type()
)
sub10EthStats1dHistPkts256T511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistPkts256T511.setStatus("current")
_Sub10EthStats1dHistPkts512T1023_Type = Counter64
_Sub10EthStats1dHistPkts512T1023_Object = MibTableColumn
sub10EthStats1dHistPkts512T1023 = _Sub10EthStats1dHistPkts512T1023_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 31),
    _Sub10EthStats1dHistPkts512T1023_Type()
)
sub10EthStats1dHistPkts512T1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistPkts512T1023.setStatus("current")
_Sub10EthStats1dHistPkts1024TMax_Type = Counter64
_Sub10EthStats1dHistPkts1024TMax_Object = MibTableColumn
sub10EthStats1dHistPkts1024TMax = _Sub10EthStats1dHistPkts1024TMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 32),
    _Sub10EthStats1dHistPkts1024TMax_Type()
)
sub10EthStats1dHistPkts1024TMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistPkts1024TMax.setStatus("current")
_Sub10EthStats1dHistRxMbpsMin_Type = Sub10ThroughputMbps
_Sub10EthStats1dHistRxMbpsMin_Object = MibTableColumn
sub10EthStats1dHistRxMbpsMin = _Sub10EthStats1dHistRxMbpsMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 33),
    _Sub10EthStats1dHistRxMbpsMin_Type()
)
sub10EthStats1dHistRxMbpsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxMbpsMin.setStatus("current")
_Sub10EthStats1dHistRxMbpsMax_Type = Sub10ThroughputMbps
_Sub10EthStats1dHistRxMbpsMax_Object = MibTableColumn
sub10EthStats1dHistRxMbpsMax = _Sub10EthStats1dHistRxMbpsMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 34),
    _Sub10EthStats1dHistRxMbpsMax_Type()
)
sub10EthStats1dHistRxMbpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxMbpsMax.setStatus("current")
_Sub10EthStats1dHistRxMbpsAvg_Type = Sub10ThroughputMbps
_Sub10EthStats1dHistRxMbpsAvg_Object = MibTableColumn
sub10EthStats1dHistRxMbpsAvg = _Sub10EthStats1dHistRxMbpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 35),
    _Sub10EthStats1dHistRxMbpsAvg_Type()
)
sub10EthStats1dHistRxMbpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistRxMbpsAvg.setStatus("current")
_Sub10EthStats1dHistTxMbpsMin_Type = Sub10ThroughputMbps
_Sub10EthStats1dHistTxMbpsMin_Object = MibTableColumn
sub10EthStats1dHistTxMbpsMin = _Sub10EthStats1dHistTxMbpsMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 36),
    _Sub10EthStats1dHistTxMbpsMin_Type()
)
sub10EthStats1dHistTxMbpsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxMbpsMin.setStatus("current")
_Sub10EthStats1dHistTxMbpsMax_Type = Sub10ThroughputMbps
_Sub10EthStats1dHistTxMbpsMax_Object = MibTableColumn
sub10EthStats1dHistTxMbpsMax = _Sub10EthStats1dHistTxMbpsMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 37),
    _Sub10EthStats1dHistTxMbpsMax_Type()
)
sub10EthStats1dHistTxMbpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxMbpsMax.setStatus("current")
_Sub10EthStats1dHistTxMbpsAvg_Type = Sub10ThroughputMbps
_Sub10EthStats1dHistTxMbpsAvg_Object = MibTableColumn
sub10EthStats1dHistTxMbpsAvg = _Sub10EthStats1dHistTxMbpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 4, 3, 3, 2, 2, 1, 38),
    _Sub10EthStats1dHistTxMbpsAvg_Type()
)
sub10EthStats1dHistTxMbpsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10EthStats1dHistTxMbpsAvg.setStatus("current")
_Sub10Radio_ObjectIdentity = ObjectIdentity
sub10Radio = _Sub10Radio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 5)
)
_Sub10RadioStatus_ObjectIdentity = ObjectIdentity
sub10RadioStatus = _Sub10RadioStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1)
)
_Sub10RadioLocalStatus_ObjectIdentity = ObjectIdentity
sub10RadioLocalStatus = _Sub10RadioLocalStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 1)
)
_Sub10RadioLclLinkStatus_Type = Sub10RadioLinkState
_Sub10RadioLclLinkStatus_Object = MibScalar
sub10RadioLclLinkStatus = _Sub10RadioLclLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 1, 1),
    _Sub10RadioLclLinkStatus_Type()
)
sub10RadioLclLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioLclLinkStatus.setStatus("current")


class _Sub10RadioLclTxPower_Type(Integer32):
    """Custom type sub10RadioLclTxPower based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 30),
    )


_Sub10RadioLclTxPower_Type.__name__ = "Integer32"
_Sub10RadioLclTxPower_Object = MibScalar
sub10RadioLclTxPower = _Sub10RadioLclTxPower_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 1, 2),
    _Sub10RadioLclTxPower_Type()
)
sub10RadioLclTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioLclTxPower.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioLclTxPower.setUnits("dBm")


class _Sub10RadioLclRxPower_Type(OctetString):
    """Custom type sub10RadioLclRxPower based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioLclRxPower_Type.__name__ = "OctetString"
_Sub10RadioLclRxPower_Object = MibScalar
sub10RadioLclRxPower = _Sub10RadioLclRxPower_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 1, 3),
    _Sub10RadioLclRxPower_Type()
)
sub10RadioLclRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioLclRxPower.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioLclRxPower.setUnits("dBm")


class _Sub10RadioLclVectErr_Type(OctetString):
    """Custom type sub10RadioLclVectErr based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioLclVectErr_Type.__name__ = "OctetString"
_Sub10RadioLclVectErr_Object = MibScalar
sub10RadioLclVectErr = _Sub10RadioLclVectErr_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 1, 4),
    _Sub10RadioLclVectErr_Type()
)
sub10RadioLclVectErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioLclVectErr.setStatus("current")


class _Sub10RadioLclLnkLoss_Type(OctetString):
    """Custom type sub10RadioLclLnkLoss based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioLclLnkLoss_Type.__name__ = "OctetString"
_Sub10RadioLclLnkLoss_Object = MibScalar
sub10RadioLclLnkLoss = _Sub10RadioLclLnkLoss_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 1, 5),
    _Sub10RadioLclLnkLoss_Type()
)
sub10RadioLclLnkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioLclLnkLoss.setStatus("current")
_Sub10RadioLclAlignmentMode_Type = Sub10AlignmentMode
_Sub10RadioLclAlignmentMode_Object = MibScalar
sub10RadioLclAlignmentMode = _Sub10RadioLclAlignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 1, 6),
    _Sub10RadioLclAlignmentMode_Type()
)
sub10RadioLclAlignmentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioLclAlignmentMode.setStatus("current")
_Sub10RadioLclDataRate_Type = Sub10RadioDataRate
_Sub10RadioLclDataRate_Object = MibScalar
sub10RadioLclDataRate = _Sub10RadioLclDataRate_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 1, 7),
    _Sub10RadioLclDataRate_Type()
)
sub10RadioLclDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioLclDataRate.setStatus("current")
_Sub10RadioLclMWUType_Type = Sub10MWUType
_Sub10RadioLclMWUType_Object = MibScalar
sub10RadioLclMWUType = _Sub10RadioLclMWUType_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 1, 8),
    _Sub10RadioLclMWUType_Type()
)
sub10RadioLclMWUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioLclMWUType.setStatus("current")


class _Sub10RadioLclAFER_Type(OctetString):
    """Custom type sub10RadioLclAFER based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioLclAFER_Type.__name__ = "OctetString"
_Sub10RadioLclAFER_Object = MibScalar
sub10RadioLclAFER = _Sub10RadioLclAFER_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 1, 9),
    _Sub10RadioLclAFER_Type()
)
sub10RadioLclAFER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioLclAFER.setStatus("current")
_Sub10RadioLclRxModulationMode_Type = Sub10ModulationMode
_Sub10RadioLclRxModulationMode_Object = MibScalar
sub10RadioLclRxModulationMode = _Sub10RadioLclRxModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 1, 10),
    _Sub10RadioLclRxModulationMode_Type()
)
sub10RadioLclRxModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioLclRxModulationMode.setStatus("current")
_Sub10RadioLclTxModulationMode_Type = Sub10ModulationMode
_Sub10RadioLclTxModulationMode_Object = MibScalar
sub10RadioLclTxModulationMode = _Sub10RadioLclTxModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 1, 11),
    _Sub10RadioLclTxModulationMode_Type()
)
sub10RadioLclTxModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioLclTxModulationMode.setStatus("current")
_Sub10RadioRemoteStatus_ObjectIdentity = ObjectIdentity
sub10RadioRemoteStatus = _Sub10RadioRemoteStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 2)
)
_Sub10RadioRmtLinkStatus_Type = Sub10RadioLinkState
_Sub10RadioRmtLinkStatus_Object = MibScalar
sub10RadioRmtLinkStatus = _Sub10RadioRmtLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 2, 1),
    _Sub10RadioRmtLinkStatus_Type()
)
sub10RadioRmtLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioRmtLinkStatus.setStatus("current")


class _Sub10RadioRmtTxPower_Type(Integer32):
    """Custom type sub10RadioRmtTxPower based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioRmtTxPower_Type.__name__ = "Integer32"
_Sub10RadioRmtTxPower_Object = MibScalar
sub10RadioRmtTxPower = _Sub10RadioRmtTxPower_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 2, 2),
    _Sub10RadioRmtTxPower_Type()
)
sub10RadioRmtTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioRmtTxPower.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioRmtTxPower.setUnits("dBm")


class _Sub10RadioRmtRxPower_Type(OctetString):
    """Custom type sub10RadioRmtRxPower based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioRmtRxPower_Type.__name__ = "OctetString"
_Sub10RadioRmtRxPower_Object = MibScalar
sub10RadioRmtRxPower = _Sub10RadioRmtRxPower_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 2, 3),
    _Sub10RadioRmtRxPower_Type()
)
sub10RadioRmtRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioRmtRxPower.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioRmtRxPower.setUnits("dBm")


class _Sub10RadioRmtVectErr_Type(OctetString):
    """Custom type sub10RadioRmtVectErr based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioRmtVectErr_Type.__name__ = "OctetString"
_Sub10RadioRmtVectErr_Object = MibScalar
sub10RadioRmtVectErr = _Sub10RadioRmtVectErr_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 2, 4),
    _Sub10RadioRmtVectErr_Type()
)
sub10RadioRmtVectErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioRmtVectErr.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioRmtVectErr.setUnits("dBm")


class _Sub10RadioRmtLnkLoss_Type(OctetString):
    """Custom type sub10RadioRmtLnkLoss based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioRmtLnkLoss_Type.__name__ = "OctetString"
_Sub10RadioRmtLnkLoss_Object = MibScalar
sub10RadioRmtLnkLoss = _Sub10RadioRmtLnkLoss_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 2, 5),
    _Sub10RadioRmtLnkLoss_Type()
)
sub10RadioRmtLnkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioRmtLnkLoss.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioRmtLnkLoss.setUnits("dBm")
_Sub10RadioRmtAlignmentMode_Type = Sub10AlignmentMode
_Sub10RadioRmtAlignmentMode_Object = MibScalar
sub10RadioRmtAlignmentMode = _Sub10RadioRmtAlignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 2, 7),
    _Sub10RadioRmtAlignmentMode_Type()
)
sub10RadioRmtAlignmentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioRmtAlignmentMode.setStatus("current")


class _Sub10RadioRmtAFER_Type(OctetString):
    """Custom type sub10RadioRmtAFER based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioRmtAFER_Type.__name__ = "OctetString"
_Sub10RadioRmtAFER_Object = MibScalar
sub10RadioRmtAFER = _Sub10RadioRmtAFER_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 1, 2, 8),
    _Sub10RadioRmtAFER_Type()
)
sub10RadioRmtAFER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioRmtAFER.setStatus("current")
_Sub10RadioMgmt_ObjectIdentity = ObjectIdentity
sub10RadioMgmt = _Sub10RadioMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2)
)


class _Sub10RadioMgmtTxPowerLimit_Type(Sub10TxPowerLimit):
    """Custom type sub10RadioMgmtTxPowerLimit based on Sub10TxPowerLimit"""


_Sub10RadioMgmtTxPowerLimit_Object = MibScalar
sub10RadioMgmtTxPowerLimit = _Sub10RadioMgmtTxPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 1),
    _Sub10RadioMgmtTxPowerLimit_Type()
)
sub10RadioMgmtTxPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10RadioMgmtTxPowerLimit.setStatus("current")


class _Sub10RadioMgmtTxRxFreq_Type(Integer32):
    """Custom type sub10RadioMgmtTxRxFreq based on Integer32"""
    defaultValue = 36

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
        *(("e250Tx71250Rx81250", 0),
          ("e250Tx71500Rx81500", 1),
          ("e250Tx71750Rx81750", 2),
          ("e250Tx72000Rx82000", 3),
          ("e250Tx72250Rx82250", 4),
          ("e250Tx72500Rx82500", 5),
          ("e250Tx72750Rx82750", 6),
          ("e250Tx73000Rx83000", 7),
          ("e250Tx73250Rx83250", 8),
          ("e250Tx73500Rx83500", 9),
          ("e250Tx73750Rx83750", 10),
          ("e250Tx74000Rx84000", 11),
          ("e250Tx74250Rx84250", 12),
          ("e250Tx74500Rx84500", 13),
          ("e250Tx74750Rx84750", 14),
          ("e250Tx75000Rx85000", 15),
          ("e250Tx75250Rx85250", 16),
          ("e250Tx75500Rx85500", 17),
          ("e250Tx75750Rx85750", 18),
          ("e500Tx72375Rx82375", 19),
          ("e500Tx72625Rx82625", 20),
          ("e500Tx72875Rx82875", 21),
          ("e500Tx73125Rx83125", 22),
          ("e500Tx73375Rx83375", 23),
          ("e500Tx73625Rx83625", 24),
          ("e500Tx73875Rx83875", 25),
          ("e500Tx74125Rx84125", 26),
          ("e500Tx74375Rx84375", 27),
          ("e500Tx74625Rx84625", 28),
          ("v500Tx58500Rx61500", 29),
          ("v500Tx58500Rx62000", 30),
          ("v500Tx58500Rx62500", 31),
          ("v500Tx59000Rx61500", 32),
          ("v500Tx59000Rx62000", 33),
          ("v500Tx59000Rx62500", 34),
          ("v500Tx59500Rx61500", 35),
          ("v500Tx59500Rx62000", 36),
          ("v500Tx59500Rx62500", 37))
    )


_Sub10RadioMgmtTxRxFreq_Type.__name__ = "Integer32"
_Sub10RadioMgmtTxRxFreq_Object = MibScalar
sub10RadioMgmtTxRxFreq = _Sub10RadioMgmtTxRxFreq_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 2),
    _Sub10RadioMgmtTxRxFreq_Type()
)
sub10RadioMgmtTxRxFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10RadioMgmtTxRxFreq.setStatus("current")


class _Sub10RadioMgmtAPCMode_Type(Integer32):
    """Custom type sub10RadioMgmtAPCMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apcModeDisabled", 0),
          ("apcModeFixed", 2),
          ("apcModeVariable", 1))
    )


_Sub10RadioMgmtAPCMode_Type.__name__ = "Integer32"
_Sub10RadioMgmtAPCMode_Object = MibScalar
sub10RadioMgmtAPCMode = _Sub10RadioMgmtAPCMode_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 3),
    _Sub10RadioMgmtAPCMode_Type()
)
sub10RadioMgmtAPCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10RadioMgmtAPCMode.setStatus("current")


class _Sub10RadioMgmtModulationMode_Type(Sub10ModulationMode):
    """Custom type sub10RadioMgmtModulationMode based on Sub10ModulationMode"""


_Sub10RadioMgmtModulationMode_Object = MibScalar
sub10RadioMgmtModulationMode = _Sub10RadioMgmtModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 4),
    _Sub10RadioMgmtModulationMode_Type()
)
sub10RadioMgmtModulationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10RadioMgmtModulationMode.setStatus("current")


class _Sub10RadioMgmtAmod_Type(Sub10State):
    """Custom type sub10RadioMgmtAmod based on Sub10State"""


_Sub10RadioMgmtAmod_Object = MibScalar
sub10RadioMgmtAmod = _Sub10RadioMgmtAmod_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 5),
    _Sub10RadioMgmtAmod_Type()
)
sub10RadioMgmtAmod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10RadioMgmtAmod.setStatus("current")
_Sub10RadioMgmtAlignmentMode_Type = Sub10AlignmentMode
_Sub10RadioMgmtAlignmentMode_Object = MibScalar
sub10RadioMgmtAlignmentMode = _Sub10RadioMgmtAlignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 6),
    _Sub10RadioMgmtAlignmentMode_Type()
)
sub10RadioMgmtAlignmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10RadioMgmtAlignmentMode.setStatus("current")


class _Sub10RadioMgmtMWUChannelWidth_Type(Integer32):
    """Custom type sub10RadioMgmtMWUChannelWidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("channelWidth250", 0),
          ("channelWidth500", 1))
    )


_Sub10RadioMgmtMWUChannelWidth_Type.__name__ = "Integer32"
_Sub10RadioMgmtMWUChannelWidth_Object = MibScalar
sub10RadioMgmtMWUChannelWidth = _Sub10RadioMgmtMWUChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 8),
    _Sub10RadioMgmtMWUChannelWidth_Type()
)
sub10RadioMgmtMWUChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10RadioMgmtMWUChannelWidth.setStatus("current")
_Sub10RadioMgmtStats_ObjectIdentity = ObjectIdentity
sub10RadioMgmtStats = _Sub10RadioMgmtStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 9)
)


class _Sub10RadioMgmtStats1dPersist_Type(Sub10State):
    """Custom type sub10RadioMgmtStats1dPersist based on Sub10State"""


_Sub10RadioMgmtStats1dPersist_Object = MibScalar
sub10RadioMgmtStats1dPersist = _Sub10RadioMgmtStats1dPersist_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 9, 1),
    _Sub10RadioMgmtStats1dPersist_Type()
)
sub10RadioMgmtStats1dPersist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10RadioMgmtStats1dPersist.setStatus("current")
_Sub10RadioMgmtStatsActiveTable_Object = MibTable
sub10RadioMgmtStatsActiveTable = _Sub10RadioMgmtStatsActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 9, 4)
)
if mibBuilder.loadTexts:
    sub10RadioMgmtStatsActiveTable.setStatus("current")
_Sub10RadioMgmtStatsActiveEntry_Object = MibTableRow
sub10RadioMgmtStatsActiveEntry = _Sub10RadioMgmtStatsActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 9, 4, 1)
)
sub10RadioMgmtStatsActiveEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10RadioMgmtStatsActiveIndex"),
)
if mibBuilder.loadTexts:
    sub10RadioMgmtStatsActiveEntry.setStatus("current")


class _Sub10RadioMgmtStatsActiveIndex_Type(Unsigned32):
    """Custom type sub10RadioMgmtStatsActiveIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 29),
    )


_Sub10RadioMgmtStatsActiveIndex_Type.__name__ = "Unsigned32"
_Sub10RadioMgmtStatsActiveIndex_Object = MibTableColumn
sub10RadioMgmtStatsActiveIndex = _Sub10RadioMgmtStatsActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 9, 4, 1, 1),
    _Sub10RadioMgmtStatsActiveIndex_Type()
)
sub10RadioMgmtStatsActiveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10RadioMgmtStatsActiveIndex.setStatus("current")


class _Sub10RadioMgmtStatsActiveName_Type(OctetString):
    """Custom type sub10RadioMgmtStatsActiveName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Sub10RadioMgmtStatsActiveName_Type.__name__ = "OctetString"
_Sub10RadioMgmtStatsActiveName_Object = MibTableColumn
sub10RadioMgmtStatsActiveName = _Sub10RadioMgmtStatsActiveName_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 9, 4, 1, 2),
    _Sub10RadioMgmtStatsActiveName_Type()
)
sub10RadioMgmtStatsActiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioMgmtStatsActiveName.setStatus("current")


class _Sub10RadioMgmtStatsActiveState_Type(Sub10State):
    """Custom type sub10RadioMgmtStatsActiveState based on Sub10State"""


_Sub10RadioMgmtStatsActiveState_Object = MibTableColumn
sub10RadioMgmtStatsActiveState = _Sub10RadioMgmtStatsActiveState_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 9, 4, 1, 3),
    _Sub10RadioMgmtStatsActiveState_Type()
)
sub10RadioMgmtStatsActiveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10RadioMgmtStatsActiveState.setStatus("current")
_Sub10RadioMgmtDataRate_Type = Sub10RadioDataRate
_Sub10RadioMgmtDataRate_Object = MibScalar
sub10RadioMgmtDataRate = _Sub10RadioMgmtDataRate_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 2, 10),
    _Sub10RadioMgmtDataRate_Type()
)
sub10RadioMgmtDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sub10RadioMgmtDataRate.setStatus("current")
_Sub10RadioStats_ObjectIdentity = ObjectIdentity
sub10RadioStats = _Sub10RadioStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3)
)


class _Sub10RadioStatsTimeElapsed_Type(OctetString):
    """Custom type sub10RadioStatsTimeElapsed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsTimeElapsed_Type.__name__ = "OctetString"
_Sub10RadioStatsTimeElapsed_Object = MibScalar
sub10RadioStatsTimeElapsed = _Sub10RadioStatsTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 1),
    _Sub10RadioStatsTimeElapsed_Type()
)
sub10RadioStatsTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsTimeElapsed.setStatus("current")
_Sub10RadioStatsCurrent_ObjectIdentity = ObjectIdentity
sub10RadioStatsCurrent = _Sub10RadioStatsCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2)
)


class _Sub10RadioStatsCurrTxPowerMin_Type(Integer32):
    """Custom type sub10RadioStatsCurrTxPowerMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStatsCurrTxPowerMin_Type.__name__ = "Integer32"
_Sub10RadioStatsCurrTxPowerMin_Object = MibScalar
sub10RadioStatsCurrTxPowerMin = _Sub10RadioStatsCurrTxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 1),
    _Sub10RadioStatsCurrTxPowerMin_Type()
)
sub10RadioStatsCurrTxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrTxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrTxPowerMin.setUnits("dBm")


class _Sub10RadioStatsCurrTxPowerMax_Type(Integer32):
    """Custom type sub10RadioStatsCurrTxPowerMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStatsCurrTxPowerMax_Type.__name__ = "Integer32"
_Sub10RadioStatsCurrTxPowerMax_Object = MibScalar
sub10RadioStatsCurrTxPowerMax = _Sub10RadioStatsCurrTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 2),
    _Sub10RadioStatsCurrTxPowerMax_Type()
)
sub10RadioStatsCurrTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrTxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrTxPowerMax.setUnits("dBm")


class _Sub10RadioStatsCurrTxPowerAvg_Type(Integer32):
    """Custom type sub10RadioStatsCurrTxPowerAvg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStatsCurrTxPowerAvg_Type.__name__ = "Integer32"
_Sub10RadioStatsCurrTxPowerAvg_Object = MibScalar
sub10RadioStatsCurrTxPowerAvg = _Sub10RadioStatsCurrTxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 3),
    _Sub10RadioStatsCurrTxPowerAvg_Type()
)
sub10RadioStatsCurrTxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrTxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrTxPowerAvg.setUnits("dBm")


class _Sub10RadioStatsCurrRxPowerMin_Type(OctetString):
    """Custom type sub10RadioStatsCurrRxPowerMin based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrRxPowerMin_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrRxPowerMin_Object = MibScalar
sub10RadioStatsCurrRxPowerMin = _Sub10RadioStatsCurrRxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 4),
    _Sub10RadioStatsCurrRxPowerMin_Type()
)
sub10RadioStatsCurrRxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRxPowerMin.setUnits("dBm")


class _Sub10RadioStatsCurrRxPowerMax_Type(OctetString):
    """Custom type sub10RadioStatsCurrRxPowerMax based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrRxPowerMax_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrRxPowerMax_Object = MibScalar
sub10RadioStatsCurrRxPowerMax = _Sub10RadioStatsCurrRxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 5),
    _Sub10RadioStatsCurrRxPowerMax_Type()
)
sub10RadioStatsCurrRxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRxPowerMax.setUnits("dBm")


class _Sub10RadioStatsCurrRxPowerAvg_Type(OctetString):
    """Custom type sub10RadioStatsCurrRxPowerAvg based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrRxPowerAvg_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrRxPowerAvg_Object = MibScalar
sub10RadioStatsCurrRxPowerAvg = _Sub10RadioStatsCurrRxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 6),
    _Sub10RadioStatsCurrRxPowerAvg_Type()
)
sub10RadioStatsCurrRxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRxPowerAvg.setUnits("dBm")


class _Sub10RadioStatsCurrVectErrMin_Type(OctetString):
    """Custom type sub10RadioStatsCurrVectErrMin based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrVectErrMin_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrVectErrMin_Object = MibScalar
sub10RadioStatsCurrVectErrMin = _Sub10RadioStatsCurrVectErrMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 7),
    _Sub10RadioStatsCurrVectErrMin_Type()
)
sub10RadioStatsCurrVectErrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrVectErrMin.setStatus("current")


class _Sub10RadioStatsCurrVectErrMax_Type(OctetString):
    """Custom type sub10RadioStatsCurrVectErrMax based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrVectErrMax_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrVectErrMax_Object = MibScalar
sub10RadioStatsCurrVectErrMax = _Sub10RadioStatsCurrVectErrMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 8),
    _Sub10RadioStatsCurrVectErrMax_Type()
)
sub10RadioStatsCurrVectErrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrVectErrMax.setStatus("current")


class _Sub10RadioStatsCurrVectErrAvg_Type(OctetString):
    """Custom type sub10RadioStatsCurrVectErrAvg based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrVectErrAvg_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrVectErrAvg_Object = MibScalar
sub10RadioStatsCurrVectErrAvg = _Sub10RadioStatsCurrVectErrAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 9),
    _Sub10RadioStatsCurrVectErrAvg_Type()
)
sub10RadioStatsCurrVectErrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrVectErrAvg.setStatus("current")


class _Sub10RadioStatsCurrLnkLossMin_Type(OctetString):
    """Custom type sub10RadioStatsCurrLnkLossMin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrLnkLossMin_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrLnkLossMin_Object = MibScalar
sub10RadioStatsCurrLnkLossMin = _Sub10RadioStatsCurrLnkLossMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 10),
    _Sub10RadioStatsCurrLnkLossMin_Type()
)
sub10RadioStatsCurrLnkLossMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrLnkLossMin.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrLnkLossMin.setUnits("dBm")


class _Sub10RadioStatsCurrLnkLossMax_Type(OctetString):
    """Custom type sub10RadioStatsCurrLnkLossMax based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrLnkLossMax_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrLnkLossMax_Object = MibScalar
sub10RadioStatsCurrLnkLossMax = _Sub10RadioStatsCurrLnkLossMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 11),
    _Sub10RadioStatsCurrLnkLossMax_Type()
)
sub10RadioStatsCurrLnkLossMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrLnkLossMax.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrLnkLossMax.setUnits("dBm")


class _Sub10RadioStatsCurrLnkLossAvg_Type(OctetString):
    """Custom type sub10RadioStatsCurrLnkLossAvg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrLnkLossAvg_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrLnkLossAvg_Object = MibScalar
sub10RadioStatsCurrLnkLossAvg = _Sub10RadioStatsCurrLnkLossAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 12),
    _Sub10RadioStatsCurrLnkLossAvg_Type()
)
sub10RadioStatsCurrLnkLossAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrLnkLossAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrLnkLossAvg.setUnits("dBm")
_Sub10RadioStatsCurrRxFrms_Type = Counter64
_Sub10RadioStatsCurrRxFrms_Object = MibScalar
sub10RadioStatsCurrRxFrms = _Sub10RadioStatsCurrRxFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 13),
    _Sub10RadioStatsCurrRxFrms_Type()
)
sub10RadioStatsCurrRxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRxFrms.setStatus("current")
_Sub10RadioStatsCurrTxFrms_Type = Counter64
_Sub10RadioStatsCurrTxFrms_Object = MibScalar
sub10RadioStatsCurrTxFrms = _Sub10RadioStatsCurrTxFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 14),
    _Sub10RadioStatsCurrTxFrms_Type()
)
sub10RadioStatsCurrTxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrTxFrms.setStatus("current")
_Sub10RadioStatsCurrRxPkts_Type = Counter64
_Sub10RadioStatsCurrRxPkts_Object = MibScalar
sub10RadioStatsCurrRxPkts = _Sub10RadioStatsCurrRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 15),
    _Sub10RadioStatsCurrRxPkts_Type()
)
sub10RadioStatsCurrRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRxPkts.setStatus("current")
_Sub10RadioStatsCurrTxPkts_Type = Counter64
_Sub10RadioStatsCurrTxPkts_Object = MibScalar
sub10RadioStatsCurrTxPkts = _Sub10RadioStatsCurrTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 16),
    _Sub10RadioStatsCurrTxPkts_Type()
)
sub10RadioStatsCurrTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrTxPkts.setStatus("current")
_Sub10RadioStatsCurrRxMgmtPkts_Type = Counter64
_Sub10RadioStatsCurrRxMgmtPkts_Object = MibScalar
sub10RadioStatsCurrRxMgmtPkts = _Sub10RadioStatsCurrRxMgmtPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 17),
    _Sub10RadioStatsCurrRxMgmtPkts_Type()
)
sub10RadioStatsCurrRxMgmtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRxMgmtPkts.setStatus("current")
_Sub10RadioStatsCurrTxMgmtPkts_Type = Counter64
_Sub10RadioStatsCurrTxMgmtPkts_Object = MibScalar
sub10RadioStatsCurrTxMgmtPkts = _Sub10RadioStatsCurrTxMgmtPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 18),
    _Sub10RadioStatsCurrTxMgmtPkts_Type()
)
sub10RadioStatsCurrTxMgmtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrTxMgmtPkts.setStatus("current")
_Sub10RadioStatsCurrRxBadFrms_Type = Counter64
_Sub10RadioStatsCurrRxBadFrms_Object = MibScalar
sub10RadioStatsCurrRxBadFrms = _Sub10RadioStatsCurrRxBadFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 19),
    _Sub10RadioStatsCurrRxBadFrms_Type()
)
sub10RadioStatsCurrRxBadFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRxBadFrms.setStatus("current")


class _Sub10RadioStatsCurrMWUTempMin_Type(Integer32):
    """Custom type sub10RadioStatsCurrMWUTempMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStatsCurrMWUTempMin_Type.__name__ = "Integer32"
_Sub10RadioStatsCurrMWUTempMin_Object = MibScalar
sub10RadioStatsCurrMWUTempMin = _Sub10RadioStatsCurrMWUTempMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 24),
    _Sub10RadioStatsCurrMWUTempMin_Type()
)
sub10RadioStatsCurrMWUTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrMWUTempMin.setStatus("current")


class _Sub10RadioStatsCurrMWUTempMax_Type(Integer32):
    """Custom type sub10RadioStatsCurrMWUTempMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStatsCurrMWUTempMax_Type.__name__ = "Integer32"
_Sub10RadioStatsCurrMWUTempMax_Object = MibScalar
sub10RadioStatsCurrMWUTempMax = _Sub10RadioStatsCurrMWUTempMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 25),
    _Sub10RadioStatsCurrMWUTempMax_Type()
)
sub10RadioStatsCurrMWUTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrMWUTempMax.setStatus("current")


class _Sub10RadioStatsCurrMWUTempAvg_Type(Integer32):
    """Custom type sub10RadioStatsCurrMWUTempAvg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStatsCurrMWUTempAvg_Type.__name__ = "Integer32"
_Sub10RadioStatsCurrMWUTempAvg_Object = MibScalar
sub10RadioStatsCurrMWUTempAvg = _Sub10RadioStatsCurrMWUTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 26),
    _Sub10RadioStatsCurrMWUTempAvg_Type()
)
sub10RadioStatsCurrMWUTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrMWUTempAvg.setStatus("current")
_Sub10RadioStatsCurrQPSKTo8PSK_Type = Counter32
_Sub10RadioStatsCurrQPSKTo8PSK_Object = MibScalar
sub10RadioStatsCurrQPSKTo8PSK = _Sub10RadioStatsCurrQPSKTo8PSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 27),
    _Sub10RadioStatsCurrQPSKTo8PSK_Type()
)
sub10RadioStatsCurrQPSKTo8PSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrQPSKTo8PSK.setStatus("current")
_Sub10RadioStatsCurr8PSKToQPSK_Type = Counter32
_Sub10RadioStatsCurr8PSKToQPSK_Object = MibScalar
sub10RadioStatsCurr8PSKToQPSK = _Sub10RadioStatsCurr8PSKToQPSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 28),
    _Sub10RadioStatsCurr8PSKToQPSK_Type()
)
sub10RadioStatsCurr8PSKToQPSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurr8PSKToQPSK.setStatus("current")


class _Sub10RadioStatsCurrAFERMin_Type(OctetString):
    """Custom type sub10RadioStatsCurrAFERMin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrAFERMin_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrAFERMin_Object = MibScalar
sub10RadioStatsCurrAFERMin = _Sub10RadioStatsCurrAFERMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 29),
    _Sub10RadioStatsCurrAFERMin_Type()
)
sub10RadioStatsCurrAFERMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrAFERMin.setStatus("current")


class _Sub10RadioStatsCurrAFERMax_Type(OctetString):
    """Custom type sub10RadioStatsCurrAFERMax based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrAFERMax_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrAFERMax_Object = MibScalar
sub10RadioStatsCurrAFERMax = _Sub10RadioStatsCurrAFERMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 30),
    _Sub10RadioStatsCurrAFERMax_Type()
)
sub10RadioStatsCurrAFERMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrAFERMax.setStatus("current")


class _Sub10RadioStatsCurrAFERAvg_Type(OctetString):
    """Custom type sub10RadioStatsCurrAFERAvg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrAFERAvg_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrAFERAvg_Object = MibScalar
sub10RadioStatsCurrAFERAvg = _Sub10RadioStatsCurrAFERAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 31),
    _Sub10RadioStatsCurrAFERAvg_Type()
)
sub10RadioStatsCurrAFERAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrAFERAvg.setStatus("current")


class _Sub10RadioStatsCurrRmtTxPowerAvg_Type(Integer32):
    """Custom type sub10RadioStatsCurrRmtTxPowerAvg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStatsCurrRmtTxPowerAvg_Type.__name__ = "Integer32"
_Sub10RadioStatsCurrRmtTxPowerAvg_Object = MibScalar
sub10RadioStatsCurrRmtTxPowerAvg = _Sub10RadioStatsCurrRmtTxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 32),
    _Sub10RadioStatsCurrRmtTxPowerAvg_Type()
)
sub10RadioStatsCurrRmtTxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRmtTxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRmtTxPowerAvg.setUnits("dBm")


class _Sub10RadioStatsCurrRmtRxPowerAvg_Type(OctetString):
    """Custom type sub10RadioStatsCurrRmtRxPowerAvg based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrRmtRxPowerAvg_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrRmtRxPowerAvg_Object = MibScalar
sub10RadioStatsCurrRmtRxPowerAvg = _Sub10RadioStatsCurrRmtRxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 33),
    _Sub10RadioStatsCurrRmtRxPowerAvg_Type()
)
sub10RadioStatsCurrRmtRxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRmtRxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRmtRxPowerAvg.setUnits("dBm")


class _Sub10RadioStatsCurrRmtVectErrAvg_Type(OctetString):
    """Custom type sub10RadioStatsCurrRmtVectErrAvg based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrRmtVectErrAvg_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrRmtVectErrAvg_Object = MibScalar
sub10RadioStatsCurrRmtVectErrAvg = _Sub10RadioStatsCurrRmtVectErrAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 34),
    _Sub10RadioStatsCurrRmtVectErrAvg_Type()
)
sub10RadioStatsCurrRmtVectErrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRmtVectErrAvg.setStatus("current")


class _Sub10RadioStatsCurrRmtLnkLossAvg_Type(OctetString):
    """Custom type sub10RadioStatsCurrRmtLnkLossAvg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrRmtLnkLossAvg_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrRmtLnkLossAvg_Object = MibScalar
sub10RadioStatsCurrRmtLnkLossAvg = _Sub10RadioStatsCurrRmtLnkLossAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 35),
    _Sub10RadioStatsCurrRmtLnkLossAvg_Type()
)
sub10RadioStatsCurrRmtLnkLossAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRmtLnkLossAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRmtLnkLossAvg.setUnits("dBm")


class _Sub10RadioStatsCurrRmtMWUTempAvg_Type(Integer32):
    """Custom type sub10RadioStatsCurrRmtMWUTempAvg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStatsCurrRmtMWUTempAvg_Type.__name__ = "Integer32"
_Sub10RadioStatsCurrRmtMWUTempAvg_Object = MibScalar
sub10RadioStatsCurrRmtMWUTempAvg = _Sub10RadioStatsCurrRmtMWUTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 36),
    _Sub10RadioStatsCurrRmtMWUTempAvg_Type()
)
sub10RadioStatsCurrRmtMWUTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRmtMWUTempAvg.setStatus("current")


class _Sub10RadioStatsCurrRmtAFERAvg_Type(OctetString):
    """Custom type sub10RadioStatsCurrRmtAFERAvg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStatsCurrRmtAFERAvg_Type.__name__ = "OctetString"
_Sub10RadioStatsCurrRmtAFERAvg_Object = MibScalar
sub10RadioStatsCurrRmtAFERAvg = _Sub10RadioStatsCurrRmtAFERAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 37),
    _Sub10RadioStatsCurrRmtAFERAvg_Type()
)
sub10RadioStatsCurrRmtAFERAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRmtAFERAvg.setStatus("current")
_Sub10RadioStatsCurrRxQPSK_Type = Counter64
_Sub10RadioStatsCurrRxQPSK_Object = MibScalar
sub10RadioStatsCurrRxQPSK = _Sub10RadioStatsCurrRxQPSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 38),
    _Sub10RadioStatsCurrRxQPSK_Type()
)
sub10RadioStatsCurrRxQPSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRxQPSK.setStatus("current")
_Sub10RadioStatsCurrRx8PSK_Type = Counter64
_Sub10RadioStatsCurrRx8PSK_Object = MibScalar
sub10RadioStatsCurrRx8PSK = _Sub10RadioStatsCurrRx8PSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 39),
    _Sub10RadioStatsCurrRx8PSK_Type()
)
sub10RadioStatsCurrRx8PSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrRx8PSK.setStatus("current")
_Sub10RadioStatsCurrTxQPSK_Type = Counter64
_Sub10RadioStatsCurrTxQPSK_Object = MibScalar
sub10RadioStatsCurrTxQPSK = _Sub10RadioStatsCurrTxQPSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 40),
    _Sub10RadioStatsCurrTxQPSK_Type()
)
sub10RadioStatsCurrTxQPSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrTxQPSK.setStatus("current")
_Sub10RadioStatsCurrTx8PSK_Type = Counter64
_Sub10RadioStatsCurrTx8PSK_Object = MibScalar
sub10RadioStatsCurrTx8PSK = _Sub10RadioStatsCurrTx8PSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 2, 41),
    _Sub10RadioStatsCurrTx8PSK_Type()
)
sub10RadioStatsCurrTx8PSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStatsCurrTx8PSK.setStatus("current")
_Sub10RadioStatsHistory_ObjectIdentity = ObjectIdentity
sub10RadioStatsHistory = _Sub10RadioStatsHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3)
)
_Sub10RadioStats1mHistory_ObjectIdentity = ObjectIdentity
sub10RadioStats1mHistory = _Sub10RadioStats1mHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1)
)


class _Sub10RadioStats1mHistIntvls_Type(Unsigned32):
    """Custom type sub10RadioStats1mHistIntvls based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_Sub10RadioStats1mHistIntvls_Type.__name__ = "Unsigned32"
_Sub10RadioStats1mHistIntvls_Object = MibScalar
sub10RadioStats1mHistIntvls = _Sub10RadioStats1mHistIntvls_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 1),
    _Sub10RadioStats1mHistIntvls_Type()
)
sub10RadioStats1mHistIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistIntvls.setStatus("current")
_Sub10RadioStats1mHistTable_Object = MibTable
sub10RadioStats1mHistTable = _Sub10RadioStats1mHistTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sub10RadioStats1mHistTable.setStatus("current")
_Sub10RadioStats1mHistEntry_Object = MibTableRow
sub10RadioStats1mHistEntry = _Sub10RadioStats1mHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1)
)
sub10RadioStats1mHistEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10RadioStats1mHistIntvl"),
)
if mibBuilder.loadTexts:
    sub10RadioStats1mHistEntry.setStatus("current")


class _Sub10RadioStats1mHistIntvl_Type(Unsigned32):
    """Custom type sub10RadioStats1mHistIntvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Sub10RadioStats1mHistIntvl_Type.__name__ = "Unsigned32"
_Sub10RadioStats1mHistIntvl_Object = MibTableColumn
sub10RadioStats1mHistIntvl = _Sub10RadioStats1mHistIntvl_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 1),
    _Sub10RadioStats1mHistIntvl_Type()
)
sub10RadioStats1mHistIntvl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistIntvl.setStatus("current")
_Sub10RadioStats1mHistTime_Type = Sub10DateTime
_Sub10RadioStats1mHistTime_Object = MibTableColumn
sub10RadioStats1mHistTime = _Sub10RadioStats1mHistTime_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 2),
    _Sub10RadioStats1mHistTime_Type()
)
sub10RadioStats1mHistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistTime.setStatus("current")


class _Sub10RadioStats1mHistTxPowerMin_Type(Integer32):
    """Custom type sub10RadioStats1mHistTxPowerMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats1mHistTxPowerMin_Type.__name__ = "Integer32"
_Sub10RadioStats1mHistTxPowerMin_Object = MibTableColumn
sub10RadioStats1mHistTxPowerMin = _Sub10RadioStats1mHistTxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 3),
    _Sub10RadioStats1mHistTxPowerMin_Type()
)
sub10RadioStats1mHistTxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistTxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistTxPowerMin.setUnits("dBm")


class _Sub10RadioStats1mHistTxPowerMax_Type(Integer32):
    """Custom type sub10RadioStats1mHistTxPowerMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats1mHistTxPowerMax_Type.__name__ = "Integer32"
_Sub10RadioStats1mHistTxPowerMax_Object = MibTableColumn
sub10RadioStats1mHistTxPowerMax = _Sub10RadioStats1mHistTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 4),
    _Sub10RadioStats1mHistTxPowerMax_Type()
)
sub10RadioStats1mHistTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistTxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistTxPowerMax.setUnits("dBm")


class _Sub10RadioStats1mHistTxPowerAvg_Type(Integer32):
    """Custom type sub10RadioStats1mHistTxPowerAvg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats1mHistTxPowerAvg_Type.__name__ = "Integer32"
_Sub10RadioStats1mHistTxPowerAvg_Object = MibTableColumn
sub10RadioStats1mHistTxPowerAvg = _Sub10RadioStats1mHistTxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 5),
    _Sub10RadioStats1mHistTxPowerAvg_Type()
)
sub10RadioStats1mHistTxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistTxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistTxPowerAvg.setUnits("dBm")


class _Sub10RadioStats1mHistRxPowerMin_Type(OctetString):
    """Custom type sub10RadioStats1mHistRxPowerMin based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1mHistRxPowerMin_Type.__name__ = "OctetString"
_Sub10RadioStats1mHistRxPowerMin_Object = MibTableColumn
sub10RadioStats1mHistRxPowerMin = _Sub10RadioStats1mHistRxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 6),
    _Sub10RadioStats1mHistRxPowerMin_Type()
)
sub10RadioStats1mHistRxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistRxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistRxPowerMin.setUnits("dBm")


class _Sub10RadioStats1mHistRxPowerMax_Type(OctetString):
    """Custom type sub10RadioStats1mHistRxPowerMax based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1mHistRxPowerMax_Type.__name__ = "OctetString"
_Sub10RadioStats1mHistRxPowerMax_Object = MibTableColumn
sub10RadioStats1mHistRxPowerMax = _Sub10RadioStats1mHistRxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 7),
    _Sub10RadioStats1mHistRxPowerMax_Type()
)
sub10RadioStats1mHistRxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistRxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistRxPowerMax.setUnits("dBm")


class _Sub10RadioStats1mHistRxPowerAvg_Type(OctetString):
    """Custom type sub10RadioStats1mHistRxPowerAvg based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1mHistRxPowerAvg_Type.__name__ = "OctetString"
_Sub10RadioStats1mHistRxPowerAvg_Object = MibTableColumn
sub10RadioStats1mHistRxPowerAvg = _Sub10RadioStats1mHistRxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 8),
    _Sub10RadioStats1mHistRxPowerAvg_Type()
)
sub10RadioStats1mHistRxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistRxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistRxPowerAvg.setUnits("dBm")


class _Sub10RadioStats1mHistVectErrMin_Type(OctetString):
    """Custom type sub10RadioStats1mHistVectErrMin based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1mHistVectErrMin_Type.__name__ = "OctetString"
_Sub10RadioStats1mHistVectErrMin_Object = MibTableColumn
sub10RadioStats1mHistVectErrMin = _Sub10RadioStats1mHistVectErrMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 9),
    _Sub10RadioStats1mHistVectErrMin_Type()
)
sub10RadioStats1mHistVectErrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistVectErrMin.setStatus("current")


class _Sub10RadioStats1mHistVectErrMax_Type(OctetString):
    """Custom type sub10RadioStats1mHistVectErrMax based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1mHistVectErrMax_Type.__name__ = "OctetString"
_Sub10RadioStats1mHistVectErrMax_Object = MibTableColumn
sub10RadioStats1mHistVectErrMax = _Sub10RadioStats1mHistVectErrMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 10),
    _Sub10RadioStats1mHistVectErrMax_Type()
)
sub10RadioStats1mHistVectErrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistVectErrMax.setStatus("current")


class _Sub10RadioStats1mHistVectErrAvg_Type(OctetString):
    """Custom type sub10RadioStats1mHistVectErrAvg based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1mHistVectErrAvg_Type.__name__ = "OctetString"
_Sub10RadioStats1mHistVectErrAvg_Object = MibTableColumn
sub10RadioStats1mHistVectErrAvg = _Sub10RadioStats1mHistVectErrAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 11),
    _Sub10RadioStats1mHistVectErrAvg_Type()
)
sub10RadioStats1mHistVectErrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistVectErrAvg.setStatus("current")


class _Sub10RadioStats1mHistLnkLossMin_Type(OctetString):
    """Custom type sub10RadioStats1mHistLnkLossMin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1mHistLnkLossMin_Type.__name__ = "OctetString"
_Sub10RadioStats1mHistLnkLossMin_Object = MibTableColumn
sub10RadioStats1mHistLnkLossMin = _Sub10RadioStats1mHistLnkLossMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 12),
    _Sub10RadioStats1mHistLnkLossMin_Type()
)
sub10RadioStats1mHistLnkLossMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistLnkLossMin.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistLnkLossMin.setUnits("dBm")


class _Sub10RadioStats1mHistLnkLossMax_Type(OctetString):
    """Custom type sub10RadioStats1mHistLnkLossMax based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1mHistLnkLossMax_Type.__name__ = "OctetString"
_Sub10RadioStats1mHistLnkLossMax_Object = MibTableColumn
sub10RadioStats1mHistLnkLossMax = _Sub10RadioStats1mHistLnkLossMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 13),
    _Sub10RadioStats1mHistLnkLossMax_Type()
)
sub10RadioStats1mHistLnkLossMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistLnkLossMax.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistLnkLossMax.setUnits("dBm")


class _Sub10RadioStats1mHistLnkLossAvg_Type(OctetString):
    """Custom type sub10RadioStats1mHistLnkLossAvg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1mHistLnkLossAvg_Type.__name__ = "OctetString"
_Sub10RadioStats1mHistLnkLossAvg_Object = MibTableColumn
sub10RadioStats1mHistLnkLossAvg = _Sub10RadioStats1mHistLnkLossAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 14),
    _Sub10RadioStats1mHistLnkLossAvg_Type()
)
sub10RadioStats1mHistLnkLossAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistLnkLossAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistLnkLossAvg.setUnits("dBm")


class _Sub10RadioStats1mHistMWUTempMin_Type(Integer32):
    """Custom type sub10RadioStats1mHistMWUTempMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats1mHistMWUTempMin_Type.__name__ = "Integer32"
_Sub10RadioStats1mHistMWUTempMin_Object = MibTableColumn
sub10RadioStats1mHistMWUTempMin = _Sub10RadioStats1mHistMWUTempMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 15),
    _Sub10RadioStats1mHistMWUTempMin_Type()
)
sub10RadioStats1mHistMWUTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistMWUTempMin.setStatus("current")


class _Sub10RadioStats1mHistMWUTempMax_Type(Integer32):
    """Custom type sub10RadioStats1mHistMWUTempMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats1mHistMWUTempMax_Type.__name__ = "Integer32"
_Sub10RadioStats1mHistMWUTempMax_Object = MibTableColumn
sub10RadioStats1mHistMWUTempMax = _Sub10RadioStats1mHistMWUTempMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 16),
    _Sub10RadioStats1mHistMWUTempMax_Type()
)
sub10RadioStats1mHistMWUTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistMWUTempMax.setStatus("current")


class _Sub10RadioStats1mHistMWUTempAvg_Type(Integer32):
    """Custom type sub10RadioStats1mHistMWUTempAvg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats1mHistMWUTempAvg_Type.__name__ = "Integer32"
_Sub10RadioStats1mHistMWUTempAvg_Object = MibTableColumn
sub10RadioStats1mHistMWUTempAvg = _Sub10RadioStats1mHistMWUTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 17),
    _Sub10RadioStats1mHistMWUTempAvg_Type()
)
sub10RadioStats1mHistMWUTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistMWUTempAvg.setStatus("current")
_Sub10RadioStats1mHistRxFrms_Type = Counter64
_Sub10RadioStats1mHistRxFrms_Object = MibTableColumn
sub10RadioStats1mHistRxFrms = _Sub10RadioStats1mHistRxFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 22),
    _Sub10RadioStats1mHistRxFrms_Type()
)
sub10RadioStats1mHistRxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistRxFrms.setStatus("current")
_Sub10RadioStats1mHistTxFrms_Type = Counter64
_Sub10RadioStats1mHistTxFrms_Object = MibTableColumn
sub10RadioStats1mHistTxFrms = _Sub10RadioStats1mHistTxFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 23),
    _Sub10RadioStats1mHistTxFrms_Type()
)
sub10RadioStats1mHistTxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistTxFrms.setStatus("current")
_Sub10RadioStats1mHistRxPkts_Type = Counter64
_Sub10RadioStats1mHistRxPkts_Object = MibTableColumn
sub10RadioStats1mHistRxPkts = _Sub10RadioStats1mHistRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 24),
    _Sub10RadioStats1mHistRxPkts_Type()
)
sub10RadioStats1mHistRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistRxPkts.setStatus("current")
_Sub10RadioStats1mHistTxPkts_Type = Counter64
_Sub10RadioStats1mHistTxPkts_Object = MibTableColumn
sub10RadioStats1mHistTxPkts = _Sub10RadioStats1mHistTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 25),
    _Sub10RadioStats1mHistTxPkts_Type()
)
sub10RadioStats1mHistTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistTxPkts.setStatus("current")
_Sub10RadioStats1mHistRxMgmtPkts_Type = Counter64
_Sub10RadioStats1mHistRxMgmtPkts_Object = MibTableColumn
sub10RadioStats1mHistRxMgmtPkts = _Sub10RadioStats1mHistRxMgmtPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 26),
    _Sub10RadioStats1mHistRxMgmtPkts_Type()
)
sub10RadioStats1mHistRxMgmtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistRxMgmtPkts.setStatus("current")
_Sub10RadioStats1mHistTxMgmtPkts_Type = Counter64
_Sub10RadioStats1mHistTxMgmtPkts_Object = MibTableColumn
sub10RadioStats1mHistTxMgmtPkts = _Sub10RadioStats1mHistTxMgmtPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 27),
    _Sub10RadioStats1mHistTxMgmtPkts_Type()
)
sub10RadioStats1mHistTxMgmtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistTxMgmtPkts.setStatus("current")
_Sub10RadioStats1mHistRxBadFrms_Type = Counter64
_Sub10RadioStats1mHistRxBadFrms_Object = MibTableColumn
sub10RadioStats1mHistRxBadFrms = _Sub10RadioStats1mHistRxBadFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 28),
    _Sub10RadioStats1mHistRxBadFrms_Type()
)
sub10RadioStats1mHistRxBadFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistRxBadFrms.setStatus("current")
_Sub10RadioStats1mHistQPSKTo8PSK_Type = Counter32
_Sub10RadioStats1mHistQPSKTo8PSK_Object = MibTableColumn
sub10RadioStats1mHistQPSKTo8PSK = _Sub10RadioStats1mHistQPSKTo8PSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 29),
    _Sub10RadioStats1mHistQPSKTo8PSK_Type()
)
sub10RadioStats1mHistQPSKTo8PSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistQPSKTo8PSK.setStatus("current")
_Sub10RadioStats1mHist8PSKToQPSK_Type = Counter32
_Sub10RadioStats1mHist8PSKToQPSK_Object = MibTableColumn
sub10RadioStats1mHist8PSKToQPSK = _Sub10RadioStats1mHist8PSKToQPSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 30),
    _Sub10RadioStats1mHist8PSKToQPSK_Type()
)
sub10RadioStats1mHist8PSKToQPSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHist8PSKToQPSK.setStatus("current")


class _Sub10RadioStats1mHistAFERMin_Type(OctetString):
    """Custom type sub10RadioStats1mHistAFERMin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1mHistAFERMin_Type.__name__ = "OctetString"
_Sub10RadioStats1mHistAFERMin_Object = MibTableColumn
sub10RadioStats1mHistAFERMin = _Sub10RadioStats1mHistAFERMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 31),
    _Sub10RadioStats1mHistAFERMin_Type()
)
sub10RadioStats1mHistAFERMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistAFERMin.setStatus("current")


class _Sub10RadioStats1mHistAFERMax_Type(OctetString):
    """Custom type sub10RadioStats1mHistAFERMax based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1mHistAFERMax_Type.__name__ = "OctetString"
_Sub10RadioStats1mHistAFERMax_Object = MibTableColumn
sub10RadioStats1mHistAFERMax = _Sub10RadioStats1mHistAFERMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 32),
    _Sub10RadioStats1mHistAFERMax_Type()
)
sub10RadioStats1mHistAFERMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistAFERMax.setStatus("current")


class _Sub10RadioStats1mHistAFERAvg_Type(OctetString):
    """Custom type sub10RadioStats1mHistAFERAvg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1mHistAFERAvg_Type.__name__ = "OctetString"
_Sub10RadioStats1mHistAFERAvg_Object = MibTableColumn
sub10RadioStats1mHistAFERAvg = _Sub10RadioStats1mHistAFERAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 33),
    _Sub10RadioStats1mHistAFERAvg_Type()
)
sub10RadioStats1mHistAFERAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistAFERAvg.setStatus("current")
_Sub10RadioStats1mHistRxQPSK_Type = Counter32
_Sub10RadioStats1mHistRxQPSK_Object = MibTableColumn
sub10RadioStats1mHistRxQPSK = _Sub10RadioStats1mHistRxQPSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 34),
    _Sub10RadioStats1mHistRxQPSK_Type()
)
sub10RadioStats1mHistRxQPSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistRxQPSK.setStatus("current")
_Sub10RadioStats1mHistRx8PSK_Type = Counter32
_Sub10RadioStats1mHistRx8PSK_Object = MibTableColumn
sub10RadioStats1mHistRx8PSK = _Sub10RadioStats1mHistRx8PSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 35),
    _Sub10RadioStats1mHistRx8PSK_Type()
)
sub10RadioStats1mHistRx8PSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistRx8PSK.setStatus("current")
_Sub10RadioStats1mHistTxQPSK_Type = Counter32
_Sub10RadioStats1mHistTxQPSK_Object = MibTableColumn
sub10RadioStats1mHistTxQPSK = _Sub10RadioStats1mHistTxQPSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 36),
    _Sub10RadioStats1mHistTxQPSK_Type()
)
sub10RadioStats1mHistTxQPSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistTxQPSK.setStatus("current")
_Sub10RadioStats1mHistTx8PSK_Type = Counter32
_Sub10RadioStats1mHistTx8PSK_Object = MibTableColumn
sub10RadioStats1mHistTx8PSK = _Sub10RadioStats1mHistTx8PSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 1, 2, 1, 37),
    _Sub10RadioStats1mHistTx8PSK_Type()
)
sub10RadioStats1mHistTx8PSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1mHistTx8PSK.setStatus("current")
_Sub10RadioStats15mHistory_ObjectIdentity = ObjectIdentity
sub10RadioStats15mHistory = _Sub10RadioStats15mHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2)
)


class _Sub10RadioStats15mHistIntvls_Type(Unsigned32):
    """Custom type sub10RadioStats15mHistIntvls based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Sub10RadioStats15mHistIntvls_Type.__name__ = "Unsigned32"
_Sub10RadioStats15mHistIntvls_Object = MibScalar
sub10RadioStats15mHistIntvls = _Sub10RadioStats15mHistIntvls_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 1),
    _Sub10RadioStats15mHistIntvls_Type()
)
sub10RadioStats15mHistIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistIntvls.setStatus("current")
_Sub10RadioStats15mHistTable_Object = MibTable
sub10RadioStats15mHistTable = _Sub10RadioStats15mHistTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    sub10RadioStats15mHistTable.setStatus("current")
_Sub10RadioStats15mHistEntry_Object = MibTableRow
sub10RadioStats15mHistEntry = _Sub10RadioStats15mHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1)
)
sub10RadioStats15mHistEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10RadioStats15mHistIntvl"),
)
if mibBuilder.loadTexts:
    sub10RadioStats15mHistEntry.setStatus("current")


class _Sub10RadioStats15mHistIntvl_Type(Unsigned32):
    """Custom type sub10RadioStats15mHistIntvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Sub10RadioStats15mHistIntvl_Type.__name__ = "Unsigned32"
_Sub10RadioStats15mHistIntvl_Object = MibTableColumn
sub10RadioStats15mHistIntvl = _Sub10RadioStats15mHistIntvl_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 1),
    _Sub10RadioStats15mHistIntvl_Type()
)
sub10RadioStats15mHistIntvl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistIntvl.setStatus("current")
_Sub10RadioStats15mHistTime_Type = Sub10DateTime
_Sub10RadioStats15mHistTime_Object = MibTableColumn
sub10RadioStats15mHistTime = _Sub10RadioStats15mHistTime_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 2),
    _Sub10RadioStats15mHistTime_Type()
)
sub10RadioStats15mHistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistTime.setStatus("current")


class _Sub10RadioStats15mHistTxPowerMin_Type(Integer32):
    """Custom type sub10RadioStats15mHistTxPowerMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats15mHistTxPowerMin_Type.__name__ = "Integer32"
_Sub10RadioStats15mHistTxPowerMin_Object = MibTableColumn
sub10RadioStats15mHistTxPowerMin = _Sub10RadioStats15mHistTxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 3),
    _Sub10RadioStats15mHistTxPowerMin_Type()
)
sub10RadioStats15mHistTxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistTxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistTxPowerMin.setUnits("dBm")


class _Sub10RadioStats15mHistTxPowerMax_Type(Integer32):
    """Custom type sub10RadioStats15mHistTxPowerMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats15mHistTxPowerMax_Type.__name__ = "Integer32"
_Sub10RadioStats15mHistTxPowerMax_Object = MibTableColumn
sub10RadioStats15mHistTxPowerMax = _Sub10RadioStats15mHistTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 4),
    _Sub10RadioStats15mHistTxPowerMax_Type()
)
sub10RadioStats15mHistTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistTxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistTxPowerMax.setUnits("dBm")


class _Sub10RadioStats15mHistTxPowerAvg_Type(Integer32):
    """Custom type sub10RadioStats15mHistTxPowerAvg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats15mHistTxPowerAvg_Type.__name__ = "Integer32"
_Sub10RadioStats15mHistTxPowerAvg_Object = MibTableColumn
sub10RadioStats15mHistTxPowerAvg = _Sub10RadioStats15mHistTxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 5),
    _Sub10RadioStats15mHistTxPowerAvg_Type()
)
sub10RadioStats15mHistTxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistTxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistTxPowerAvg.setUnits("dBm")


class _Sub10RadioStats15mHistRxPowerMin_Type(OctetString):
    """Custom type sub10RadioStats15mHistRxPowerMin based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats15mHistRxPowerMin_Type.__name__ = "OctetString"
_Sub10RadioStats15mHistRxPowerMin_Object = MibTableColumn
sub10RadioStats15mHistRxPowerMin = _Sub10RadioStats15mHistRxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 6),
    _Sub10RadioStats15mHistRxPowerMin_Type()
)
sub10RadioStats15mHistRxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistRxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistRxPowerMin.setUnits("dBm")


class _Sub10RadioStats15mHistRxPowerMax_Type(OctetString):
    """Custom type sub10RadioStats15mHistRxPowerMax based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats15mHistRxPowerMax_Type.__name__ = "OctetString"
_Sub10RadioStats15mHistRxPowerMax_Object = MibTableColumn
sub10RadioStats15mHistRxPowerMax = _Sub10RadioStats15mHistRxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 7),
    _Sub10RadioStats15mHistRxPowerMax_Type()
)
sub10RadioStats15mHistRxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistRxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistRxPowerMax.setUnits("dBm")


class _Sub10RadioStats15mHistRxPowerAvg_Type(OctetString):
    """Custom type sub10RadioStats15mHistRxPowerAvg based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats15mHistRxPowerAvg_Type.__name__ = "OctetString"
_Sub10RadioStats15mHistRxPowerAvg_Object = MibTableColumn
sub10RadioStats15mHistRxPowerAvg = _Sub10RadioStats15mHistRxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 8),
    _Sub10RadioStats15mHistRxPowerAvg_Type()
)
sub10RadioStats15mHistRxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistRxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistRxPowerAvg.setUnits("dBm")


class _Sub10RadioStats15mHistVectErrMin_Type(OctetString):
    """Custom type sub10RadioStats15mHistVectErrMin based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats15mHistVectErrMin_Type.__name__ = "OctetString"
_Sub10RadioStats15mHistVectErrMin_Object = MibTableColumn
sub10RadioStats15mHistVectErrMin = _Sub10RadioStats15mHistVectErrMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 9),
    _Sub10RadioStats15mHistVectErrMin_Type()
)
sub10RadioStats15mHistVectErrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistVectErrMin.setStatus("current")


class _Sub10RadioStats15mHistVectErrMax_Type(OctetString):
    """Custom type sub10RadioStats15mHistVectErrMax based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats15mHistVectErrMax_Type.__name__ = "OctetString"
_Sub10RadioStats15mHistVectErrMax_Object = MibTableColumn
sub10RadioStats15mHistVectErrMax = _Sub10RadioStats15mHistVectErrMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 10),
    _Sub10RadioStats15mHistVectErrMax_Type()
)
sub10RadioStats15mHistVectErrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistVectErrMax.setStatus("current")


class _Sub10RadioStats15mHistVectErrAvg_Type(OctetString):
    """Custom type sub10RadioStats15mHistVectErrAvg based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats15mHistVectErrAvg_Type.__name__ = "OctetString"
_Sub10RadioStats15mHistVectErrAvg_Object = MibTableColumn
sub10RadioStats15mHistVectErrAvg = _Sub10RadioStats15mHistVectErrAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 11),
    _Sub10RadioStats15mHistVectErrAvg_Type()
)
sub10RadioStats15mHistVectErrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistVectErrAvg.setStatus("current")


class _Sub10RadioStats15mHistLnkLossMin_Type(OctetString):
    """Custom type sub10RadioStats15mHistLnkLossMin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats15mHistLnkLossMin_Type.__name__ = "OctetString"
_Sub10RadioStats15mHistLnkLossMin_Object = MibTableColumn
sub10RadioStats15mHistLnkLossMin = _Sub10RadioStats15mHistLnkLossMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 12),
    _Sub10RadioStats15mHistLnkLossMin_Type()
)
sub10RadioStats15mHistLnkLossMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistLnkLossMin.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistLnkLossMin.setUnits("dBm")


class _Sub10RadioStats15mHistLnkLossMax_Type(OctetString):
    """Custom type sub10RadioStats15mHistLnkLossMax based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats15mHistLnkLossMax_Type.__name__ = "OctetString"
_Sub10RadioStats15mHistLnkLossMax_Object = MibTableColumn
sub10RadioStats15mHistLnkLossMax = _Sub10RadioStats15mHistLnkLossMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 13),
    _Sub10RadioStats15mHistLnkLossMax_Type()
)
sub10RadioStats15mHistLnkLossMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistLnkLossMax.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistLnkLossMax.setUnits("dBm")


class _Sub10RadioStats15mHistLnkLossAvg_Type(OctetString):
    """Custom type sub10RadioStats15mHistLnkLossAvg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats15mHistLnkLossAvg_Type.__name__ = "OctetString"
_Sub10RadioStats15mHistLnkLossAvg_Object = MibTableColumn
sub10RadioStats15mHistLnkLossAvg = _Sub10RadioStats15mHistLnkLossAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 14),
    _Sub10RadioStats15mHistLnkLossAvg_Type()
)
sub10RadioStats15mHistLnkLossAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistLnkLossAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistLnkLossAvg.setUnits("dBm")


class _Sub10RadioStats15mHistMWUTempMin_Type(Integer32):
    """Custom type sub10RadioStats15mHistMWUTempMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats15mHistMWUTempMin_Type.__name__ = "Integer32"
_Sub10RadioStats15mHistMWUTempMin_Object = MibTableColumn
sub10RadioStats15mHistMWUTempMin = _Sub10RadioStats15mHistMWUTempMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 15),
    _Sub10RadioStats15mHistMWUTempMin_Type()
)
sub10RadioStats15mHistMWUTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistMWUTempMin.setStatus("current")


class _Sub10RadioStats15mHistMWUTempMax_Type(Integer32):
    """Custom type sub10RadioStats15mHistMWUTempMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats15mHistMWUTempMax_Type.__name__ = "Integer32"
_Sub10RadioStats15mHistMWUTempMax_Object = MibTableColumn
sub10RadioStats15mHistMWUTempMax = _Sub10RadioStats15mHistMWUTempMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 16),
    _Sub10RadioStats15mHistMWUTempMax_Type()
)
sub10RadioStats15mHistMWUTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistMWUTempMax.setStatus("current")


class _Sub10RadioStats15mHistMWUTempAvg_Type(Integer32):
    """Custom type sub10RadioStats15mHistMWUTempAvg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats15mHistMWUTempAvg_Type.__name__ = "Integer32"
_Sub10RadioStats15mHistMWUTempAvg_Object = MibTableColumn
sub10RadioStats15mHistMWUTempAvg = _Sub10RadioStats15mHistMWUTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 17),
    _Sub10RadioStats15mHistMWUTempAvg_Type()
)
sub10RadioStats15mHistMWUTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistMWUTempAvg.setStatus("current")
_Sub10RadioStats15mHistRxFrms_Type = Counter64
_Sub10RadioStats15mHistRxFrms_Object = MibTableColumn
sub10RadioStats15mHistRxFrms = _Sub10RadioStats15mHistRxFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 22),
    _Sub10RadioStats15mHistRxFrms_Type()
)
sub10RadioStats15mHistRxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistRxFrms.setStatus("current")
_Sub10RadioStats15mHistTxFrms_Type = Counter64
_Sub10RadioStats15mHistTxFrms_Object = MibTableColumn
sub10RadioStats15mHistTxFrms = _Sub10RadioStats15mHistTxFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 23),
    _Sub10RadioStats15mHistTxFrms_Type()
)
sub10RadioStats15mHistTxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistTxFrms.setStatus("current")
_Sub10RadioStats15mHistRxPkts_Type = Counter64
_Sub10RadioStats15mHistRxPkts_Object = MibTableColumn
sub10RadioStats15mHistRxPkts = _Sub10RadioStats15mHistRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 24),
    _Sub10RadioStats15mHistRxPkts_Type()
)
sub10RadioStats15mHistRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistRxPkts.setStatus("current")
_Sub10RadioStats15mHistTxPkts_Type = Counter64
_Sub10RadioStats15mHistTxPkts_Object = MibTableColumn
sub10RadioStats15mHistTxPkts = _Sub10RadioStats15mHistTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 25),
    _Sub10RadioStats15mHistTxPkts_Type()
)
sub10RadioStats15mHistTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistTxPkts.setStatus("current")
_Sub10RadioStats15mHistRxMgmtPkts_Type = Counter64
_Sub10RadioStats15mHistRxMgmtPkts_Object = MibTableColumn
sub10RadioStats15mHistRxMgmtPkts = _Sub10RadioStats15mHistRxMgmtPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 26),
    _Sub10RadioStats15mHistRxMgmtPkts_Type()
)
sub10RadioStats15mHistRxMgmtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistRxMgmtPkts.setStatus("current")
_Sub10RadioStats15mHistTxMgmtPkts_Type = Counter64
_Sub10RadioStats15mHistTxMgmtPkts_Object = MibTableColumn
sub10RadioStats15mHistTxMgmtPkts = _Sub10RadioStats15mHistTxMgmtPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 27),
    _Sub10RadioStats15mHistTxMgmtPkts_Type()
)
sub10RadioStats15mHistTxMgmtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistTxMgmtPkts.setStatus("current")
_Sub10RadioStats15mHistRxBadFrms_Type = Counter64
_Sub10RadioStats15mHistRxBadFrms_Object = MibTableColumn
sub10RadioStats15mHistRxBadFrms = _Sub10RadioStats15mHistRxBadFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 28),
    _Sub10RadioStats15mHistRxBadFrms_Type()
)
sub10RadioStats15mHistRxBadFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistRxBadFrms.setStatus("current")
_Sub10RadioStats15mHistQPSKTo8PSK_Type = Counter32
_Sub10RadioStats15mHistQPSKTo8PSK_Object = MibTableColumn
sub10RadioStats15mHistQPSKTo8PSK = _Sub10RadioStats15mHistQPSKTo8PSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 29),
    _Sub10RadioStats15mHistQPSKTo8PSK_Type()
)
sub10RadioStats15mHistQPSKTo8PSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistQPSKTo8PSK.setStatus("current")
_Sub10RadioStats15mHist8PSKToQPSK_Type = Counter32
_Sub10RadioStats15mHist8PSKToQPSK_Object = MibTableColumn
sub10RadioStats15mHist8PSKToQPSK = _Sub10RadioStats15mHist8PSKToQPSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 30),
    _Sub10RadioStats15mHist8PSKToQPSK_Type()
)
sub10RadioStats15mHist8PSKToQPSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHist8PSKToQPSK.setStatus("current")


class _Sub10RadioStats15mHistAFERMin_Type(OctetString):
    """Custom type sub10RadioStats15mHistAFERMin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats15mHistAFERMin_Type.__name__ = "OctetString"
_Sub10RadioStats15mHistAFERMin_Object = MibTableColumn
sub10RadioStats15mHistAFERMin = _Sub10RadioStats15mHistAFERMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 31),
    _Sub10RadioStats15mHistAFERMin_Type()
)
sub10RadioStats15mHistAFERMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistAFERMin.setStatus("current")


class _Sub10RadioStats15mHistAFERMax_Type(OctetString):
    """Custom type sub10RadioStats15mHistAFERMax based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats15mHistAFERMax_Type.__name__ = "OctetString"
_Sub10RadioStats15mHistAFERMax_Object = MibTableColumn
sub10RadioStats15mHistAFERMax = _Sub10RadioStats15mHistAFERMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 32),
    _Sub10RadioStats15mHistAFERMax_Type()
)
sub10RadioStats15mHistAFERMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistAFERMax.setStatus("current")


class _Sub10RadioStats15mHistAFERAvg_Type(OctetString):
    """Custom type sub10RadioStats15mHistAFERAvg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats15mHistAFERAvg_Type.__name__ = "OctetString"
_Sub10RadioStats15mHistAFERAvg_Object = MibTableColumn
sub10RadioStats15mHistAFERAvg = _Sub10RadioStats15mHistAFERAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 33),
    _Sub10RadioStats15mHistAFERAvg_Type()
)
sub10RadioStats15mHistAFERAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistAFERAvg.setStatus("current")
_Sub10RadioStats15mHistRxQPSK_Type = Counter32
_Sub10RadioStats15mHistRxQPSK_Object = MibTableColumn
sub10RadioStats15mHistRxQPSK = _Sub10RadioStats15mHistRxQPSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 34),
    _Sub10RadioStats15mHistRxQPSK_Type()
)
sub10RadioStats15mHistRxQPSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistRxQPSK.setStatus("current")
_Sub10RadioStats15mHistRx8PSK_Type = Counter32
_Sub10RadioStats15mHistRx8PSK_Object = MibTableColumn
sub10RadioStats15mHistRx8PSK = _Sub10RadioStats15mHistRx8PSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 35),
    _Sub10RadioStats15mHistRx8PSK_Type()
)
sub10RadioStats15mHistRx8PSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistRx8PSK.setStatus("current")
_Sub10RadioStats15mHistTxQPSK_Type = Counter32
_Sub10RadioStats15mHistTxQPSK_Object = MibTableColumn
sub10RadioStats15mHistTxQPSK = _Sub10RadioStats15mHistTxQPSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 36),
    _Sub10RadioStats15mHistTxQPSK_Type()
)
sub10RadioStats15mHistTxQPSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistTxQPSK.setStatus("current")
_Sub10RadioStats15mHistTx8PSK_Type = Counter32
_Sub10RadioStats15mHistTx8PSK_Object = MibTableColumn
sub10RadioStats15mHistTx8PSK = _Sub10RadioStats15mHistTx8PSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 2, 2, 1, 37),
    _Sub10RadioStats15mHistTx8PSK_Type()
)
sub10RadioStats15mHistTx8PSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats15mHistTx8PSK.setStatus("current")
_Sub10RadioStats1dHistory_ObjectIdentity = ObjectIdentity
sub10RadioStats1dHistory = _Sub10RadioStats1dHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3)
)


class _Sub10RadioStats1dHistIntvls_Type(Unsigned32):
    """Custom type sub10RadioStats1dHistIntvls based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Sub10RadioStats1dHistIntvls_Type.__name__ = "Unsigned32"
_Sub10RadioStats1dHistIntvls_Object = MibScalar
sub10RadioStats1dHistIntvls = _Sub10RadioStats1dHistIntvls_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 1),
    _Sub10RadioStats1dHistIntvls_Type()
)
sub10RadioStats1dHistIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistIntvls.setStatus("current")
_Sub10RadioStats1dHistTable_Object = MibTable
sub10RadioStats1dHistTable = _Sub10RadioStats1dHistTable_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    sub10RadioStats1dHistTable.setStatus("current")
_Sub10RadioStats1dHistEntry_Object = MibTableRow
sub10RadioStats1dHistEntry = _Sub10RadioStats1dHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1)
)
sub10RadioStats1dHistEntry.setIndexNames(
    (0, "SUB10SYSTEMS-MIB", "sub10RadioStats1dHistIntvl"),
)
if mibBuilder.loadTexts:
    sub10RadioStats1dHistEntry.setStatus("current")


class _Sub10RadioStats1dHistIntvl_Type(Unsigned32):
    """Custom type sub10RadioStats1dHistIntvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Sub10RadioStats1dHistIntvl_Type.__name__ = "Unsigned32"
_Sub10RadioStats1dHistIntvl_Object = MibTableColumn
sub10RadioStats1dHistIntvl = _Sub10RadioStats1dHistIntvl_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 1),
    _Sub10RadioStats1dHistIntvl_Type()
)
sub10RadioStats1dHistIntvl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistIntvl.setStatus("current")
_Sub10RadioStats1dHistTime_Type = Sub10DateTime
_Sub10RadioStats1dHistTime_Object = MibTableColumn
sub10RadioStats1dHistTime = _Sub10RadioStats1dHistTime_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 2),
    _Sub10RadioStats1dHistTime_Type()
)
sub10RadioStats1dHistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistTime.setStatus("current")


class _Sub10RadioStats1dHistTxPowerMin_Type(Integer32):
    """Custom type sub10RadioStats1dHistTxPowerMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats1dHistTxPowerMin_Type.__name__ = "Integer32"
_Sub10RadioStats1dHistTxPowerMin_Object = MibTableColumn
sub10RadioStats1dHistTxPowerMin = _Sub10RadioStats1dHistTxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 3),
    _Sub10RadioStats1dHistTxPowerMin_Type()
)
sub10RadioStats1dHistTxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistTxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistTxPowerMin.setUnits("dBm")


class _Sub10RadioStats1dHistTxPowerMax_Type(Integer32):
    """Custom type sub10RadioStats1dHistTxPowerMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats1dHistTxPowerMax_Type.__name__ = "Integer32"
_Sub10RadioStats1dHistTxPowerMax_Object = MibTableColumn
sub10RadioStats1dHistTxPowerMax = _Sub10RadioStats1dHistTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 4),
    _Sub10RadioStats1dHistTxPowerMax_Type()
)
sub10RadioStats1dHistTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistTxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistTxPowerMax.setUnits("dBm")


class _Sub10RadioStats1dHistTxPowerAvg_Type(Integer32):
    """Custom type sub10RadioStats1dHistTxPowerAvg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats1dHistTxPowerAvg_Type.__name__ = "Integer32"
_Sub10RadioStats1dHistTxPowerAvg_Object = MibTableColumn
sub10RadioStats1dHistTxPowerAvg = _Sub10RadioStats1dHistTxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 5),
    _Sub10RadioStats1dHistTxPowerAvg_Type()
)
sub10RadioStats1dHistTxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistTxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistTxPowerAvg.setUnits("dBm")


class _Sub10RadioStats1dHistRxPowerMin_Type(OctetString):
    """Custom type sub10RadioStats1dHistRxPowerMin based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1dHistRxPowerMin_Type.__name__ = "OctetString"
_Sub10RadioStats1dHistRxPowerMin_Object = MibTableColumn
sub10RadioStats1dHistRxPowerMin = _Sub10RadioStats1dHistRxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 6),
    _Sub10RadioStats1dHistRxPowerMin_Type()
)
sub10RadioStats1dHistRxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistRxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistRxPowerMin.setUnits("dBm")


class _Sub10RadioStats1dHistRxPowerMax_Type(OctetString):
    """Custom type sub10RadioStats1dHistRxPowerMax based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1dHistRxPowerMax_Type.__name__ = "OctetString"
_Sub10RadioStats1dHistRxPowerMax_Object = MibTableColumn
sub10RadioStats1dHistRxPowerMax = _Sub10RadioStats1dHistRxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 7),
    _Sub10RadioStats1dHistRxPowerMax_Type()
)
sub10RadioStats1dHistRxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistRxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistRxPowerMax.setUnits("dBm")


class _Sub10RadioStats1dHistRxPowerAvg_Type(OctetString):
    """Custom type sub10RadioStats1dHistRxPowerAvg based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1dHistRxPowerAvg_Type.__name__ = "OctetString"
_Sub10RadioStats1dHistRxPowerAvg_Object = MibTableColumn
sub10RadioStats1dHistRxPowerAvg = _Sub10RadioStats1dHistRxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 8),
    _Sub10RadioStats1dHistRxPowerAvg_Type()
)
sub10RadioStats1dHistRxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistRxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistRxPowerAvg.setUnits("dBm")


class _Sub10RadioStats1dHistVectErrMin_Type(OctetString):
    """Custom type sub10RadioStats1dHistVectErrMin based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1dHistVectErrMin_Type.__name__ = "OctetString"
_Sub10RadioStats1dHistVectErrMin_Object = MibTableColumn
sub10RadioStats1dHistVectErrMin = _Sub10RadioStats1dHistVectErrMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 9),
    _Sub10RadioStats1dHistVectErrMin_Type()
)
sub10RadioStats1dHistVectErrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistVectErrMin.setStatus("current")


class _Sub10RadioStats1dHistVectErrMax_Type(OctetString):
    """Custom type sub10RadioStats1dHistVectErrMax based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1dHistVectErrMax_Type.__name__ = "OctetString"
_Sub10RadioStats1dHistVectErrMax_Object = MibTableColumn
sub10RadioStats1dHistVectErrMax = _Sub10RadioStats1dHistVectErrMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 10),
    _Sub10RadioStats1dHistVectErrMax_Type()
)
sub10RadioStats1dHistVectErrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistVectErrMax.setStatus("current")


class _Sub10RadioStats1dHistVectErrAvg_Type(OctetString):
    """Custom type sub10RadioStats1dHistVectErrAvg based on OctetString"""
    defaultValue = OctetString("0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1dHistVectErrAvg_Type.__name__ = "OctetString"
_Sub10RadioStats1dHistVectErrAvg_Object = MibTableColumn
sub10RadioStats1dHistVectErrAvg = _Sub10RadioStats1dHistVectErrAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 11),
    _Sub10RadioStats1dHistVectErrAvg_Type()
)
sub10RadioStats1dHistVectErrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistVectErrAvg.setStatus("current")


class _Sub10RadioStats1dHistLnkLossMin_Type(OctetString):
    """Custom type sub10RadioStats1dHistLnkLossMin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1dHistLnkLossMin_Type.__name__ = "OctetString"
_Sub10RadioStats1dHistLnkLossMin_Object = MibTableColumn
sub10RadioStats1dHistLnkLossMin = _Sub10RadioStats1dHistLnkLossMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 12),
    _Sub10RadioStats1dHistLnkLossMin_Type()
)
sub10RadioStats1dHistLnkLossMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistLnkLossMin.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistLnkLossMin.setUnits("dBm")


class _Sub10RadioStats1dHistLnkLossMax_Type(OctetString):
    """Custom type sub10RadioStats1dHistLnkLossMax based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1dHistLnkLossMax_Type.__name__ = "OctetString"
_Sub10RadioStats1dHistLnkLossMax_Object = MibTableColumn
sub10RadioStats1dHistLnkLossMax = _Sub10RadioStats1dHistLnkLossMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 13),
    _Sub10RadioStats1dHistLnkLossMax_Type()
)
sub10RadioStats1dHistLnkLossMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistLnkLossMax.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistLnkLossMax.setUnits("dBm")


class _Sub10RadioStats1dHistLnkLossAvg_Type(OctetString):
    """Custom type sub10RadioStats1dHistLnkLossAvg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1dHistLnkLossAvg_Type.__name__ = "OctetString"
_Sub10RadioStats1dHistLnkLossAvg_Object = MibTableColumn
sub10RadioStats1dHistLnkLossAvg = _Sub10RadioStats1dHistLnkLossAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 14),
    _Sub10RadioStats1dHistLnkLossAvg_Type()
)
sub10RadioStats1dHistLnkLossAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistLnkLossAvg.setStatus("current")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistLnkLossAvg.setUnits("dBm")


class _Sub10RadioStats1dHistMWUTempMin_Type(Integer32):
    """Custom type sub10RadioStats1dHistMWUTempMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats1dHistMWUTempMin_Type.__name__ = "Integer32"
_Sub10RadioStats1dHistMWUTempMin_Object = MibTableColumn
sub10RadioStats1dHistMWUTempMin = _Sub10RadioStats1dHistMWUTempMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 15),
    _Sub10RadioStats1dHistMWUTempMin_Type()
)
sub10RadioStats1dHistMWUTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistMWUTempMin.setStatus("current")


class _Sub10RadioStats1dHistMWUTempMax_Type(Integer32):
    """Custom type sub10RadioStats1dHistMWUTempMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats1dHistMWUTempMax_Type.__name__ = "Integer32"
_Sub10RadioStats1dHistMWUTempMax_Object = MibTableColumn
sub10RadioStats1dHistMWUTempMax = _Sub10RadioStats1dHistMWUTempMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 16),
    _Sub10RadioStats1dHistMWUTempMax_Type()
)
sub10RadioStats1dHistMWUTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistMWUTempMax.setStatus("current")


class _Sub10RadioStats1dHistMWUTempAvg_Type(Integer32):
    """Custom type sub10RadioStats1dHistMWUTempAvg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Sub10RadioStats1dHistMWUTempAvg_Type.__name__ = "Integer32"
_Sub10RadioStats1dHistMWUTempAvg_Object = MibTableColumn
sub10RadioStats1dHistMWUTempAvg = _Sub10RadioStats1dHistMWUTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 17),
    _Sub10RadioStats1dHistMWUTempAvg_Type()
)
sub10RadioStats1dHistMWUTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistMWUTempAvg.setStatus("current")
_Sub10RadioStats1dHistRxFrms_Type = Counter64
_Sub10RadioStats1dHistRxFrms_Object = MibTableColumn
sub10RadioStats1dHistRxFrms = _Sub10RadioStats1dHistRxFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 22),
    _Sub10RadioStats1dHistRxFrms_Type()
)
sub10RadioStats1dHistRxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistRxFrms.setStatus("current")
_Sub10RadioStats1dHistTxFrms_Type = Counter64
_Sub10RadioStats1dHistTxFrms_Object = MibTableColumn
sub10RadioStats1dHistTxFrms = _Sub10RadioStats1dHistTxFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 23),
    _Sub10RadioStats1dHistTxFrms_Type()
)
sub10RadioStats1dHistTxFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistTxFrms.setStatus("current")
_Sub10RadioStats1dHistRxPkts_Type = Counter64
_Sub10RadioStats1dHistRxPkts_Object = MibTableColumn
sub10RadioStats1dHistRxPkts = _Sub10RadioStats1dHistRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 24),
    _Sub10RadioStats1dHistRxPkts_Type()
)
sub10RadioStats1dHistRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistRxPkts.setStatus("current")
_Sub10RadioStats1dHistTxPkts_Type = Counter64
_Sub10RadioStats1dHistTxPkts_Object = MibTableColumn
sub10RadioStats1dHistTxPkts = _Sub10RadioStats1dHistTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 25),
    _Sub10RadioStats1dHistTxPkts_Type()
)
sub10RadioStats1dHistTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistTxPkts.setStatus("current")
_Sub10RadioStats1dHistRxMgmtPkts_Type = Counter64
_Sub10RadioStats1dHistRxMgmtPkts_Object = MibTableColumn
sub10RadioStats1dHistRxMgmtPkts = _Sub10RadioStats1dHistRxMgmtPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 26),
    _Sub10RadioStats1dHistRxMgmtPkts_Type()
)
sub10RadioStats1dHistRxMgmtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistRxMgmtPkts.setStatus("current")
_Sub10RadioStats1dHistTxMgmtPkts_Type = Counter64
_Sub10RadioStats1dHistTxMgmtPkts_Object = MibTableColumn
sub10RadioStats1dHistTxMgmtPkts = _Sub10RadioStats1dHistTxMgmtPkts_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 27),
    _Sub10RadioStats1dHistTxMgmtPkts_Type()
)
sub10RadioStats1dHistTxMgmtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistTxMgmtPkts.setStatus("current")
_Sub10RadioStats1dHistRxBadFrms_Type = Counter64
_Sub10RadioStats1dHistRxBadFrms_Object = MibTableColumn
sub10RadioStats1dHistRxBadFrms = _Sub10RadioStats1dHistRxBadFrms_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 28),
    _Sub10RadioStats1dHistRxBadFrms_Type()
)
sub10RadioStats1dHistRxBadFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistRxBadFrms.setStatus("current")
_Sub10RadioStats1dHistQPSKTo8PSK_Type = Counter64
_Sub10RadioStats1dHistQPSKTo8PSK_Object = MibTableColumn
sub10RadioStats1dHistQPSKTo8PSK = _Sub10RadioStats1dHistQPSKTo8PSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 29),
    _Sub10RadioStats1dHistQPSKTo8PSK_Type()
)
sub10RadioStats1dHistQPSKTo8PSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistQPSKTo8PSK.setStatus("current")
_Sub10RadioStats1dHist8PSKToQPSK_Type = Counter64
_Sub10RadioStats1dHist8PSKToQPSK_Object = MibTableColumn
sub10RadioStats1dHist8PSKToQPSK = _Sub10RadioStats1dHist8PSKToQPSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 30),
    _Sub10RadioStats1dHist8PSKToQPSK_Type()
)
sub10RadioStats1dHist8PSKToQPSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHist8PSKToQPSK.setStatus("current")


class _Sub10RadioStats1dHistAFERMin_Type(OctetString):
    """Custom type sub10RadioStats1dHistAFERMin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1dHistAFERMin_Type.__name__ = "OctetString"
_Sub10RadioStats1dHistAFERMin_Object = MibTableColumn
sub10RadioStats1dHistAFERMin = _Sub10RadioStats1dHistAFERMin_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 31),
    _Sub10RadioStats1dHistAFERMin_Type()
)
sub10RadioStats1dHistAFERMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistAFERMin.setStatus("current")


class _Sub10RadioStats1dHistAFERMax_Type(OctetString):
    """Custom type sub10RadioStats1dHistAFERMax based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1dHistAFERMax_Type.__name__ = "OctetString"
_Sub10RadioStats1dHistAFERMax_Object = MibTableColumn
sub10RadioStats1dHistAFERMax = _Sub10RadioStats1dHistAFERMax_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 32),
    _Sub10RadioStats1dHistAFERMax_Type()
)
sub10RadioStats1dHistAFERMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistAFERMax.setStatus("current")


class _Sub10RadioStats1dHistAFERAvg_Type(OctetString):
    """Custom type sub10RadioStats1dHistAFERAvg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Sub10RadioStats1dHistAFERAvg_Type.__name__ = "OctetString"
_Sub10RadioStats1dHistAFERAvg_Object = MibTableColumn
sub10RadioStats1dHistAFERAvg = _Sub10RadioStats1dHistAFERAvg_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 33),
    _Sub10RadioStats1dHistAFERAvg_Type()
)
sub10RadioStats1dHistAFERAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistAFERAvg.setStatus("current")
_Sub10RadioStats1dHistRxQPSK_Type = Counter32
_Sub10RadioStats1dHistRxQPSK_Object = MibTableColumn
sub10RadioStats1dHistRxQPSK = _Sub10RadioStats1dHistRxQPSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 34),
    _Sub10RadioStats1dHistRxQPSK_Type()
)
sub10RadioStats1dHistRxQPSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistRxQPSK.setStatus("current")
_Sub10RadioStats1dHistRx8PSK_Type = Counter32
_Sub10RadioStats1dHistRx8PSK_Object = MibTableColumn
sub10RadioStats1dHistRx8PSK = _Sub10RadioStats1dHistRx8PSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 35),
    _Sub10RadioStats1dHistRx8PSK_Type()
)
sub10RadioStats1dHistRx8PSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistRx8PSK.setStatus("current")
_Sub10RadioStats1dHistTxQPSK_Type = Counter32
_Sub10RadioStats1dHistTxQPSK_Object = MibTableColumn
sub10RadioStats1dHistTxQPSK = _Sub10RadioStats1dHistTxQPSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 36),
    _Sub10RadioStats1dHistTxQPSK_Type()
)
sub10RadioStats1dHistTxQPSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistTxQPSK.setStatus("current")
_Sub10RadioStats1dHistTx8PSK_Type = Counter32
_Sub10RadioStats1dHistTx8PSK_Object = MibTableColumn
sub10RadioStats1dHistTx8PSK = _Sub10RadioStats1dHistTx8PSK_Object(
    (1, 3, 6, 1, 4, 1, 39003, 5, 3, 3, 3, 2, 1, 37),
    _Sub10RadioStats1dHistTx8PSK_Type()
)
sub10RadioStats1dHistTx8PSK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sub10RadioStats1dHistTx8PSK.setStatus("current")
_Sub10MIBConformance_ObjectIdentity = ObjectIdentity
sub10MIBConformance = _Sub10MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 20)
)
_Sub10MIBCompliances_ObjectIdentity = ObjectIdentity
sub10MIBCompliances = _Sub10MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 20, 1)
)
_Sub10MIBGroups_ObjectIdentity = ObjectIdentity
sub10MIBGroups = _Sub10MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2)
)

# Managed Objects groups

sub10UnitLocalStatusGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 2)
)
sub10UnitLocalStatusGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitLclTime"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclUnitType"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclDescription"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclHWSerialNumber"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclTerminalName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclTerminalType"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclLinkName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclLinkId"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclSiteName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclFirmwareLoadedBank"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclFirmwareVersion"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclIpAddress"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclMWUTemperature"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclNTPSyncStatus"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclRadioDataRate"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclMWUType"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclFPGAVersion"))
)
if mibBuilder.loadTexts:
    sub10UnitLocalStatusGrp.setStatus("current")

sub10UnitLclAlarmStateEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 3)
)
sub10UnitLclAlarmStateEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitLclAlarmState"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclAlarmStateTime"))
)
if mibBuilder.loadTexts:
    sub10UnitLclAlarmStateEntryGrp.setStatus("current")

sub10UnitRemoteStatusGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 4)
)
sub10UnitRemoteStatusGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitRmtUnitType"),
        ("SUB10SYSTEMS-MIB", "sub10UnitRmtTime"),
        ("SUB10SYSTEMS-MIB", "sub10UnitRmtTerminalName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitRmtTerminalType"),
        ("SUB10SYSTEMS-MIB", "sub10UnitRmtLinkName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitRmtLinkId"),
        ("SUB10SYSTEMS-MIB", "sub10UnitRmtHWSerialNumber"),
        ("SUB10SYSTEMS-MIB", "sub10UnitRmtFirmwareVersion"),
        ("SUB10SYSTEMS-MIB", "sub10UnitRmtIpAddress"),
        ("SUB10SYSTEMS-MIB", "sub10UnitRmtMWUTemperature"))
)
if mibBuilder.loadTexts:
    sub10UnitRemoteStatusGrp.setStatus("current")

sub10UnitMgmtSystemGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 5)
)
sub10UnitMgmtSystemGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtTerminalName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtLinkName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtLinkId"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSiteName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtContactName"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSystemGrp.setStatus("current")

sub10UnitMgmtIpGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 6)
)
sub10UnitMgmtIpGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtIpMode"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtIpAddress"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtIpSubnetMask"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtIpDefGateway"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtIpDHCP"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtIpGrp.setStatus("current")

sub10UnitMgmtVlanGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 7)
)
sub10UnitMgmtVlanGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtVlanState"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtVlanId"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtVlanPriority"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtVlanDSCP"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtVlanDEI"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtVlanGrp.setStatus("current")

sub10UnitMgmtUsersGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 8)
)
sub10UnitMgmtUsersGrp.setObjects(
    ("SUB10SYSTEMS-MIB", "sub10UnitMgmtUsersNumber")
)
if mibBuilder.loadTexts:
    sub10UnitMgmtUsersGrp.setStatus("current")

sub10UnitMgmtUserEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 9)
)
sub10UnitMgmtUserEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtUserRowStatus"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtUserName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtUserGroup"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtUserPassword"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtUserPasswordVerify"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtUserEntryGrp.setStatus("current")

sub10UnitMgmtTimeGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 10)
)
sub10UnitMgmtTimeGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtTimeLocal"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtTimeNTPEnabled"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtTimeNTPServer1"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtTimeNTPServer2"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtTimeNTPPort"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtTimeNTPSyncStatus"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtDateTime"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtTimeGrp.setStatus("current")

sub10UnitMgmtAlarmEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 11)
)
sub10UnitMgmtAlarmEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmRowStatus"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmSeverity"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmMeasObject"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmMonitorIntvl"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmRaiseOper"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmRaiseThresh"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmClearOper"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmClearThresh"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmRaiseIntvls"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmClearIntvls"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmType"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmSmtpAddress"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmToSyslog"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmEnabled"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmMeasObjectVal"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmToSNMP"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmMeasObjIndex"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmEntryGrp.setStatus("current")

sub10UnitMgmtAlarmsGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 12)
)
sub10UnitMgmtAlarmsGrp.setObjects(
    ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmsUserDefStart")
)
if mibBuilder.loadTexts:
    sub10UnitMgmtAlarmsGrp.setStatus("current")

sub10UnitMgmtSnmpGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 13)
)
sub10UnitMgmtSnmpGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpAgent"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpTraps"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpv320Mib"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpv3"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpEngineIdFormat"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpEngineIdText"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpEngineId"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpOperAuthProto"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpOperPrivProto"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpAdminAuthProto"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpAdminPrivProto"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpMaintAuthProto"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpMaintPrivProto"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpGrp.setStatus("current")

sub10UnitMgmtSnmpTrpDstEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 14)
)
sub10UnitMgmtSnmpTrpDstEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpTrpDstRowStatus"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpTrpDstIpAddr"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpTrpDstCommunity"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTrpDstEntryGrp.setStatus("current")

sub10UnitMgmtSnmpUserEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 15)
)
sub10UnitMgmtSnmpUserEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpUserRowStatus"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpUserName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpUserGroup"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpUserAuthPwd"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpUserAuthPwdChk"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpUserPrivPwd"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpUserPrivPwdChk"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpUserEntryGrp.setStatus("current")

sub10UnitMgmtSnmpAccessEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 16)
)
sub10UnitMgmtSnmpAccessEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpAccessRowStatus"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpAccessName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpAccessIpAddr"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpAccessEntryGrp.setStatus("current")

sub10UnitMgmtSnmpTargetEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 17)
)
sub10UnitMgmtSnmpTargetEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpTargetRowStatus"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpTargetName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpTargetIpAddr"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSnmpTargetUserName"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSnmpTargetEntryGrp.setStatus("current")

sub10UnitMgmtFirmwareGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 18)
)
sub10UnitMgmtFirmwareGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtFirmwareSelectBank"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtFirmwareLoadedBank"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtFirmwareVersion"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtFirmwareBootVersion"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtFirmwareAction"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtFirmwareUplImage"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtFirmwareUplSvrIp"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtFirmwareFromBank"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtFirmwareToBank"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtFirmwareActStatus"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtFirmwareActProgress"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareGrp.setStatus("current")

sub10UnitMgmtFirmwareBankEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 19)
)
sub10UnitMgmtFirmwareBankEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtFirmwareBankVersion"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtFirmwareBankImage"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtFirmwareBankEntryGrp.setStatus("current")

sub10UnitMgmtDNSEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 20)
)
sub10UnitMgmtDNSEntryGrp.setObjects(
    ("SUB10SYSTEMS-MIB", "sub10UnitMgmtDNServer")
)
if mibBuilder.loadTexts:
    sub10UnitMgmtDNSEntryGrp.setStatus("current")

sub10UnitMgmtEncryptionGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 21)
)
sub10UnitMgmtEncryptionGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtEncryptMode"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtEncryptKey"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtEncryptionGrp.setStatus("current")

sub10UnitMgmtLicenseGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 22)
)
sub10UnitMgmtLicenseGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtLicenseKey"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtLicenseAES"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtLicenseGrp.setStatus("current")

sub10UnitMgmtSyncEGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 23)
)
sub10UnitMgmtSyncEGrp.setObjects(
    ("SUB10SYSTEMS-MIB", "sub10UnitMgmtSyncEMode")
)
if mibBuilder.loadTexts:
    sub10UnitMgmtSyncEGrp.setStatus("current")

sub10UnitMgmtActionsGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 24)
)
sub10UnitMgmtActionsGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtTransaction"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtTransactionStatus"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtRollbackTimeout"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtTransactionMode"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtResetAction"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtResetStatsGroup"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtResetAlarmsType"))
)
if mibBuilder.loadTexts:
    sub10UnitMgmtActionsGrp.setStatus("current")

sub10EthLclStatusEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 25)
)
sub10EthLclStatusEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10EthLclLinkStatus"),
        ("SUB10SYSTEMS-MIB", "sub10EthLclMacAddress"),
        ("SUB10SYSTEMS-MIB", "sub10EthLclSpeed"),
        ("SUB10SYSTEMS-MIB", "sub10EthLclDuplex"),
        ("SUB10SYSTEMS-MIB", "sub10EthLclMDI"))
)
if mibBuilder.loadTexts:
    sub10EthLclStatusEntryGrp.setStatus("current")

sub10EthRmtStatusEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 26)
)
sub10EthRmtStatusEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10EthRmtLinkStatus"),
        ("SUB10SYSTEMS-MIB", "sub10EthRmtMacAddress"),
        ("SUB10SYSTEMS-MIB", "sub10EthRmtSpeed"),
        ("SUB10SYSTEMS-MIB", "sub10EthRmtDuplex"),
        ("SUB10SYSTEMS-MIB", "sub10EthRmtMDI"))
)
if mibBuilder.loadTexts:
    sub10EthRmtStatusEntryGrp.setStatus("current")

sub10EthMgmtPhyEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 27)
)
sub10EthMgmtPhyEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10EthMgmtPhyAutoNeg"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtPhySpeed"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtPhyDuplex"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtPhyMDI"))
)
if mibBuilder.loadTexts:
    sub10EthMgmtPhyEntryGrp.setStatus("current")

sub10EthMgmtVlanGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 28)
)
sub10EthMgmtVlanGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10EthMgmtVlanFiltering"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtVlanDefaultEnabled"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtVlanDefaultId"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtVlanDefaultPriority"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtVlanDefaultDEI"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtVlanIngressAction"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtVlanEgressAction"))
)
if mibBuilder.loadTexts:
    sub10EthMgmtVlanGrp.setStatus("current")

sub10EthMgmtVlanAllowedEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 29)
)
sub10EthMgmtVlanAllowedEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10EthMgmtVlanAllowedRowStatus"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtVlanAllowedId"))
)
if mibBuilder.loadTexts:
    sub10EthMgmtVlanAllowedEntryGrp.setStatus("current")

sub10EthMgmtQoSGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 30)
)
sub10EthMgmtQoSGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSActiveState"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSMode"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSUntaggedQueue"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSVlanMappingNumber"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSDSCPMappingNumber"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSMPLSMappingNumber"))
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSGrp.setStatus("current")

sub10EthMgmtQoSQEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 31)
)
sub10EthMgmtQoSQEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSQSchedulingType"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSQDWRRWeight"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSQCongestionPolicy"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSQSizeMax"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSQLen"))
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSQEntryGrp.setStatus("current")

sub10EthMgmtQoSVlanEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 32)
)
sub10EthMgmtQoSVlanEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSVlanId"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSVlanQueue"))
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSVlanEntryGrp.setStatus("current")

sub10EthMgmtQoSPCPEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 33)
)
sub10EthMgmtQoSPCPEntryGrp.setObjects(
    ("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSPCPQueue")
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSPCPEntryGrp.setStatus("current")

sub10EthMgmtQoSDSCPEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 34)
)
sub10EthMgmtQoSDSCPEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSDSCPMarking"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSDSCPQueue"))
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSDSCPEntryGrp.setStatus("current")

sub10EthMgmtQoSMPLSEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 35)
)
sub10EthMgmtQoSMPLSEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSMPLSTrafficClass"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtQoSMPLSQueue"))
)
if mibBuilder.loadTexts:
    sub10EthMgmtQoSMPLSEntryGrp.setStatus("current")

sub10EthMgmtStatsActiveEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 36)
)
sub10EthMgmtStatsActiveEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10EthMgmtStatsActiveName"),
        ("SUB10SYSTEMS-MIB", "sub10EthMgmtStatsActiveState"))
)
if mibBuilder.loadTexts:
    sub10EthMgmtStatsActiveEntryGrp.setStatus("current")

sub10EthernetStatsGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 37)
)
sub10EthernetStatsGrp.setObjects(
    ("SUB10SYSTEMS-MIB", "sub10EthStatsTimeElapsed")
)
if mibBuilder.loadTexts:
    sub10EthernetStatsGrp.setStatus("current")

sub10EthernetStatsCurrEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 38)
)
sub10EthernetStatsCurrEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxOctets"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxGoodFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxBcastFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxMcastFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxPauseFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxCRCErrs"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxAlignErrs"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxOversized"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxJabberFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxUndersized"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxFragments"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxSOFOvrns"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxOctets"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxGoodFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxBcastFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxMcastFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxPauseFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxDeferred"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxSnglCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxMlplCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxExsvCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxLtCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxCSenseErrs"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrPkts64Octets"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrPkts65T127"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrPkts128T255"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrPkts256T511"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrPkts512T1023"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrPkts1024TMax"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxMbps"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxMbps"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxMbpsMin"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxMbpsMax"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRxMbpsAvg"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxMbpsMin"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxMbpsMax"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrTxMbpsAvg"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRmtRxMbpsAvg"),
        ("SUB10SYSTEMS-MIB", "sub10EthStatsCurrRmtTxMbpsAvg"))
)
if mibBuilder.loadTexts:
    sub10EthernetStatsCurrEntryGrp.setStatus("current")

sub10EthernetStats15mHistoryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 39)
)
sub10EthernetStats15mHistoryGrp.setObjects(
    ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistIntvls")
)
if mibBuilder.loadTexts:
    sub10EthernetStats15mHistoryGrp.setStatus("current")

sub10EthStats15mHistEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 40)
)
sub10EthStats15mHistEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTime"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxOctets"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxGoodFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxBcastFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxMcastFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxPauseFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxCRCErrs"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxAlignErrs"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxOversized"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxJabberFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxUndersized"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxFragments"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxSOFOvrns"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxOctets"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxGoodFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxBcastFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxMcastFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxPauseFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxDeferred"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxSnglCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxMlplCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxExsvCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxLtCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxCSenseErrs"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistPkts64Octets"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistPkts65T127"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistPkts128T255"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistPkts256T511"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistPkts512T1023"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistPkts1024TMax"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxMbpsMin"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxMbpsMax"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistRxMbpsAvg"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxMbpsMin"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxMbpsMax"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats15mHistTxMbpsAvg"))
)
if mibBuilder.loadTexts:
    sub10EthStats15mHistEntryGrp.setStatus("current")

sub10EthStats1dHistoryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 41)
)
sub10EthStats1dHistoryGrp.setObjects(
    ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistIntvls")
)
if mibBuilder.loadTexts:
    sub10EthStats1dHistoryGrp.setStatus("current")

sub10EthStats1dHistEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 42)
)
sub10EthStats1dHistEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTime"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxOctets"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxGoodFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxBcastFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxMcastFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxPauseFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxCRCErrs"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxAlignErrs"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxOversized"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxJabberFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxUndersized"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxFragments"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxSOFOvrns"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxOctets"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxGoodFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxBcastFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxMcastFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxPauseFrms"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxDeferred"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxSnglCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxMlplCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxExsvCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxLtCollsn"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxCSenseErrs"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistPkts64Octets"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistPkts65T127"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistPkts128T255"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistPkts256T511"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistPkts512T1023"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistPkts1024TMax"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxMbpsMin"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxMbpsMax"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistRxMbpsAvg"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxMbpsMin"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxMbpsMax"),
        ("SUB10SYSTEMS-MIB", "sub10EthStats1dHistTxMbpsAvg"))
)
if mibBuilder.loadTexts:
    sub10EthStats1dHistEntryGrp.setStatus("current")

sub10RadioLocalStatusGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 43)
)
sub10RadioLocalStatusGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10RadioLclLinkStatus"),
        ("SUB10SYSTEMS-MIB", "sub10RadioLclTxPower"),
        ("SUB10SYSTEMS-MIB", "sub10RadioLclRxPower"),
        ("SUB10SYSTEMS-MIB", "sub10RadioLclVectErr"),
        ("SUB10SYSTEMS-MIB", "sub10RadioLclLnkLoss"),
        ("SUB10SYSTEMS-MIB", "sub10RadioLclAlignmentMode"),
        ("SUB10SYSTEMS-MIB", "sub10RadioLclDataRate"),
        ("SUB10SYSTEMS-MIB", "sub10RadioLclMWUType"),
        ("SUB10SYSTEMS-MIB", "sub10RadioLclAFER"),
        ("SUB10SYSTEMS-MIB", "sub10RadioLclRxModulationMode"),
        ("SUB10SYSTEMS-MIB", "sub10RadioLclTxModulationMode"))
)
if mibBuilder.loadTexts:
    sub10RadioLocalStatusGrp.setStatus("current")

sub10RadioRemoteStatusGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 44)
)
sub10RadioRemoteStatusGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10RadioRmtLinkStatus"),
        ("SUB10SYSTEMS-MIB", "sub10RadioRmtTxPower"),
        ("SUB10SYSTEMS-MIB", "sub10RadioRmtRxPower"),
        ("SUB10SYSTEMS-MIB", "sub10RadioRmtVectErr"),
        ("SUB10SYSTEMS-MIB", "sub10RadioRmtLnkLoss"),
        ("SUB10SYSTEMS-MIB", "sub10RadioRmtAlignmentMode"),
        ("SUB10SYSTEMS-MIB", "sub10RadioRmtAFER"))
)
if mibBuilder.loadTexts:
    sub10RadioRemoteStatusGrp.setStatus("current")

sub10RadioMgmtGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 45)
)
sub10RadioMgmtGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10RadioMgmtTxPowerLimit"),
        ("SUB10SYSTEMS-MIB", "sub10RadioMgmtTxRxFreq"),
        ("SUB10SYSTEMS-MIB", "sub10RadioMgmtAPCMode"),
        ("SUB10SYSTEMS-MIB", "sub10RadioMgmtModulationMode"),
        ("SUB10SYSTEMS-MIB", "sub10RadioMgmtAmod"),
        ("SUB10SYSTEMS-MIB", "sub10RadioMgmtAlignmentMode"),
        ("SUB10SYSTEMS-MIB", "sub10RadioMgmtMWUChannelWidth"),
        ("SUB10SYSTEMS-MIB", "sub10RadioMgmtDataRate"))
)
if mibBuilder.loadTexts:
    sub10RadioMgmtGrp.setStatus("current")

sub10RadioMgmtStatsGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 46)
)
sub10RadioMgmtStatsGrp.setObjects(
    ("SUB10SYSTEMS-MIB", "sub10RadioMgmtStats1dPersist")
)
if mibBuilder.loadTexts:
    sub10RadioMgmtStatsGrp.setStatus("current")

sub10RadioMgmtStatsActiveEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 47)
)
sub10RadioMgmtStatsActiveEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10RadioMgmtStatsActiveName"),
        ("SUB10SYSTEMS-MIB", "sub10RadioMgmtStatsActiveState"))
)
if mibBuilder.loadTexts:
    sub10RadioMgmtStatsActiveEntryGrp.setStatus("current")

sub10RadioStatsGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 48)
)
sub10RadioStatsGrp.setObjects(
    ("SUB10SYSTEMS-MIB", "sub10RadioStatsTimeElapsed")
)
if mibBuilder.loadTexts:
    sub10RadioStatsGrp.setStatus("current")

sub10RadioStatsCurrentGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 49)
)
sub10RadioStatsCurrentGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrTxPowerMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrTxPowerMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrTxPowerAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRxPowerMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRxPowerMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRxPowerAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrVectErrMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrVectErrMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrVectErrAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrLnkLossMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrLnkLossMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrLnkLossAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRxFrms"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrTxFrms"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRxPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrTxPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRxMgmtPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrTxMgmtPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRxBadFrms"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrMWUTempMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrMWUTempMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrMWUTempAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrQPSKTo8PSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurr8PSKToQPSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrAFERMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrAFERMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrAFERAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRmtTxPowerAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRmtRxPowerAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRmtVectErrAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRmtLnkLossAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRmtMWUTempAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRmtAFERAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRxQPSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrRx8PSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrTxQPSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStatsCurrTx8PSK"))
)
if mibBuilder.loadTexts:
    sub10RadioStatsCurrentGrp.setStatus("current")

sub10RadioStats1mHistoryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 50)
)
sub10RadioStats1mHistoryGrp.setObjects(
    ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistIntvls")
)
if mibBuilder.loadTexts:
    sub10RadioStats1mHistoryGrp.setStatus("current")

sub10RadioStats1mHistEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 51)
)
sub10RadioStats1mHistEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistTime"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistTxPowerMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistTxPowerMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistTxPowerAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistRxPowerMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistRxPowerMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistRxPowerAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistVectErrMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistVectErrMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistVectErrAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistLnkLossMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistLnkLossMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistLnkLossAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistMWUTempMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistMWUTempMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistMWUTempAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistRxFrms"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistTxFrms"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistRxPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistTxPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistRxMgmtPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistTxMgmtPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistRxBadFrms"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistQPSKTo8PSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHist8PSKToQPSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistAFERMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistAFERMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistAFERAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistRxQPSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistRx8PSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistTxQPSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1mHistTx8PSK"))
)
if mibBuilder.loadTexts:
    sub10RadioStats1mHistEntryGrp.setStatus("current")

sub10RadioStats15mHistoryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 52)
)
sub10RadioStats15mHistoryGrp.setObjects(
    ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistIntvls")
)
if mibBuilder.loadTexts:
    sub10RadioStats15mHistoryGrp.setStatus("current")

sub10RadioStats15mHistEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 53)
)
sub10RadioStats15mHistEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistTime"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistTxPowerMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistTxPowerMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistTxPowerAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistRxPowerMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistRxPowerMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistRxPowerAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistVectErrMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistVectErrMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistVectErrAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistLnkLossMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistLnkLossMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistLnkLossAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistMWUTempMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistMWUTempMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistMWUTempAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistRxFrms"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistTxFrms"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistRxPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistTxPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistRxMgmtPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistTxMgmtPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistRxBadFrms"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistQPSKTo8PSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHist8PSKToQPSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistAFERMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistAFERMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistAFERAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistRxQPSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistRx8PSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistTxQPSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats15mHistTx8PSK"))
)
if mibBuilder.loadTexts:
    sub10RadioStats15mHistEntryGrp.setStatus("current")

sub10RadioStats1dHistoryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 54)
)
sub10RadioStats1dHistoryGrp.setObjects(
    ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistIntvls")
)
if mibBuilder.loadTexts:
    sub10RadioStats1dHistoryGrp.setStatus("current")

sub10RadioStats1dHistEntryGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 55)
)
sub10RadioStats1dHistEntryGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistTime"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistTxPowerMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistTxPowerMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistTxPowerAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistRxPowerMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistRxPowerMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistRxPowerAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistVectErrMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistVectErrMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistVectErrAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistLnkLossMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistLnkLossMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistLnkLossAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistMWUTempMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistMWUTempMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistMWUTempAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistRxFrms"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistTxFrms"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistRxPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistTxPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistRxMgmtPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistTxMgmtPkts"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistRxBadFrms"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistQPSKTo8PSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHist8PSKToQPSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistAFERMin"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistAFERMax"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistAFERAvg"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistRxQPSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistRx8PSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistTxQPSK"),
        ("SUB10SYSTEMS-MIB", "sub10RadioStats1dHistTx8PSK"))
)
if mibBuilder.loadTexts:
    sub10RadioStats1dHistEntryGrp.setStatus("current")


# Notification objects

sub10UnitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 39003, 0, 1)
)
sub10UnitAlarm.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclAlarmState"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmSeverity"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmMeasObject"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmMeasObjectVal"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmRaiseOper"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmRaiseThresh"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmClearOper"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmClearThresh"))
)
if mibBuilder.loadTexts:
    sub10UnitAlarm.setStatus(
        "current"
    )

sub10EthernetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 39003, 0, 2)
)
sub10EthernetAlarm.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclAlarmState"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmSeverity"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmMeasObject"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmMeasObjectVal"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmRaiseOper"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmRaiseThresh"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmClearOper"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmClearThresh"))
)
if mibBuilder.loadTexts:
    sub10EthernetAlarm.setStatus(
        "current"
    )

sub10RadioAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 39003, 0, 3)
)
sub10RadioAlarm.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmName"),
        ("SUB10SYSTEMS-MIB", "sub10UnitLclAlarmState"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmSeverity"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmMeasObject"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmMeasObjectVal"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmRaiseOper"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmRaiseThresh"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmClearOper"),
        ("SUB10SYSTEMS-MIB", "sub10UnitMgmtAlarmClearThresh"))
)
if mibBuilder.loadTexts:
    sub10RadioAlarm.setStatus(
        "current"
    )


# Notifications groups

sub10NotificationsGrp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 39003, 20, 2, 1)
)
sub10NotificationsGrp.setObjects(
      *(("SUB10SYSTEMS-MIB", "sub10UnitAlarm"),
        ("SUB10SYSTEMS-MIB", "sub10EthernetAlarm"),
        ("SUB10SYSTEMS-MIB", "sub10RadioAlarm"))
)
if mibBuilder.loadTexts:
    sub10NotificationsGrp.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

sub10Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 39003, 20, 1, 1)
)
if mibBuilder.loadTexts:
    sub10Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUB10SYSTEMS-MIB",
    **{"Sub10EthInterfaceIndex": Sub10EthInterfaceIndex,
       "Sub10EntryStatus": Sub10EntryStatus,
       "Sub10State": Sub10State,
       "Sub10UnitType": Sub10UnitType,
       "Sub10TerminalType": Sub10TerminalType,
       "Sub10Availability": Sub10Availability,
       "Sub10AlignmentMode": Sub10AlignmentMode,
       "Sub10AlignmentModeLock": Sub10AlignmentModeLock,
       "Sub10OperStatus": Sub10OperStatus,
       "Sub10Duplex": Sub10Duplex,
       "Sub10MDIType": Sub10MDIType,
       "Sub10RadioLinkState": Sub10RadioLinkState,
       "Sub10AlarmName": Sub10AlarmName,
       "Sub10MacAddress": Sub10MacAddress,
       "Sub10AlarmState": Sub10AlarmState,
       "Sub10DateTime": Sub10DateTime,
       "Sub10AlarmIndex": Sub10AlarmIndex,
       "Sub10MeasuredObject": Sub10MeasuredObject,
       "Sub10AlarmSeverity": Sub10AlarmSeverity,
       "Sub10AlarmOperation": Sub10AlarmOperation,
       "Sub10AlarmType": Sub10AlarmType,
       "Sub10NTPSyncStatus": Sub10NTPSyncStatus,
       "Sub10VlanId": Sub10VlanId,
       "Sub10VlanTagAction": Sub10VlanTagAction,
       "Sub10VlanPriority": Sub10VlanPriority,
       "Sub10QoSQueue": Sub10QoSQueue,
       "Sub10TxPowerLimit": Sub10TxPowerLimit,
       "Sub10RadioDataRate": Sub10RadioDataRate,
       "Sub10UserGroup": Sub10UserGroup,
       "Sub10Snmpv3SecurityLevel": Sub10Snmpv3SecurityLevel,
       "Sub10Snmpv3AuthProtocol": Sub10Snmpv3AuthProtocol,
       "Sub10Snmpv3PrivProtocol": Sub10Snmpv3PrivProtocol,
       "Sub10MWUType": Sub10MWUType,
       "Sub10FirmwareBank": Sub10FirmwareBank,
       "Sub10StatsGroup": Sub10StatsGroup,
       "Sub10ThroughputMbps": Sub10ThroughputMbps,
       "Sub10ModulationMode": Sub10ModulationMode,
       "sub10Systems": sub10Systems,
       "sub10Notifications": sub10Notifications,
       "sub10UnitAlarm": sub10UnitAlarm,
       "sub10EthernetAlarm": sub10EthernetAlarm,
       "sub10RadioAlarm": sub10RadioAlarm,
       "sub10Unit": sub10Unit,
       "sub10UnitStatus": sub10UnitStatus,
       "sub10UnitLocalStatus": sub10UnitLocalStatus,
       "sub10UnitLclTime": sub10UnitLclTime,
       "sub10UnitLclUnitType": sub10UnitLclUnitType,
       "sub10UnitLclDescription": sub10UnitLclDescription,
       "sub10UnitLclHWSerialNumber": sub10UnitLclHWSerialNumber,
       "sub10UnitLclTerminalName": sub10UnitLclTerminalName,
       "sub10UnitLclTerminalType": sub10UnitLclTerminalType,
       "sub10UnitLclLinkName": sub10UnitLclLinkName,
       "sub10UnitLclLinkId": sub10UnitLclLinkId,
       "sub10UnitLclSiteName": sub10UnitLclSiteName,
       "sub10UnitLclFirmwareLoadedBank": sub10UnitLclFirmwareLoadedBank,
       "sub10UnitLclFirmwareVersion": sub10UnitLclFirmwareVersion,
       "sub10UnitLclIpAddress": sub10UnitLclIpAddress,
       "sub10UnitLclMWUTemperature": sub10UnitLclMWUTemperature,
       "sub10UnitLclNTPSyncStatus": sub10UnitLclNTPSyncStatus,
       "sub10UnitLclAlarmStateTable": sub10UnitLclAlarmStateTable,
       "sub10UnitLclAlarmStateEntry": sub10UnitLclAlarmStateEntry,
       "sub10UnitLclAlarmStateIndex": sub10UnitLclAlarmStateIndex,
       "sub10UnitLclAlarmState": sub10UnitLclAlarmState,
       "sub10UnitLclAlarmStateTime": sub10UnitLclAlarmStateTime,
       "sub10UnitLclRadioDataRate": sub10UnitLclRadioDataRate,
       "sub10UnitLclMWUType": sub10UnitLclMWUType,
       "sub10UnitLclFPGAVersion": sub10UnitLclFPGAVersion,
       "sub10UnitRemoteStatus": sub10UnitRemoteStatus,
       "sub10UnitRmtUnitType": sub10UnitRmtUnitType,
       "sub10UnitRmtTime": sub10UnitRmtTime,
       "sub10UnitRmtTerminalName": sub10UnitRmtTerminalName,
       "sub10UnitRmtTerminalType": sub10UnitRmtTerminalType,
       "sub10UnitRmtLinkName": sub10UnitRmtLinkName,
       "sub10UnitRmtLinkId": sub10UnitRmtLinkId,
       "sub10UnitRmtHWSerialNumber": sub10UnitRmtHWSerialNumber,
       "sub10UnitRmtFirmwareVersion": sub10UnitRmtFirmwareVersion,
       "sub10UnitRmtIpAddress": sub10UnitRmtIpAddress,
       "sub10UnitRmtMWUTemperature": sub10UnitRmtMWUTemperature,
       "sub10UnitMgmt": sub10UnitMgmt,
       "sub10UnitMgmtSystem": sub10UnitMgmtSystem,
       "sub10UnitMgmtTerminalName": sub10UnitMgmtTerminalName,
       "sub10UnitMgmtLinkName": sub10UnitMgmtLinkName,
       "sub10UnitMgmtLinkId": sub10UnitMgmtLinkId,
       "sub10UnitMgmtSiteName": sub10UnitMgmtSiteName,
       "sub10UnitMgmtContactName": sub10UnitMgmtContactName,
       "sub10UnitMgmtIp": sub10UnitMgmtIp,
       "sub10UnitMgmtIpMode": sub10UnitMgmtIpMode,
       "sub10UnitMgmtIpAddress": sub10UnitMgmtIpAddress,
       "sub10UnitMgmtIpSubnetMask": sub10UnitMgmtIpSubnetMask,
       "sub10UnitMgmtIpDefGateway": sub10UnitMgmtIpDefGateway,
       "sub10UnitMgmtIpDHCP": sub10UnitMgmtIpDHCP,
       "sub10UnitMgmtVlan": sub10UnitMgmtVlan,
       "sub10UnitMgmtVlanState": sub10UnitMgmtVlanState,
       "sub10UnitMgmtVlanId": sub10UnitMgmtVlanId,
       "sub10UnitMgmtVlanPriority": sub10UnitMgmtVlanPriority,
       "sub10UnitMgmtVlanDSCP": sub10UnitMgmtVlanDSCP,
       "sub10UnitMgmtVlanDEI": sub10UnitMgmtVlanDEI,
       "sub10UnitMgmtUsers": sub10UnitMgmtUsers,
       "sub10UnitMgmtUsersNumber": sub10UnitMgmtUsersNumber,
       "sub10UnitMgmtUserTable": sub10UnitMgmtUserTable,
       "sub10UnitMgmtUserEntry": sub10UnitMgmtUserEntry,
       "sub10UnitMgmtUserIndex": sub10UnitMgmtUserIndex,
       "sub10UnitMgmtUserRowStatus": sub10UnitMgmtUserRowStatus,
       "sub10UnitMgmtUserName": sub10UnitMgmtUserName,
       "sub10UnitMgmtUserGroup": sub10UnitMgmtUserGroup,
       "sub10UnitMgmtUserPassword": sub10UnitMgmtUserPassword,
       "sub10UnitMgmtUserPasswordVerify": sub10UnitMgmtUserPasswordVerify,
       "sub10UnitMgmtTime": sub10UnitMgmtTime,
       "sub10UnitMgmtTimeLocal": sub10UnitMgmtTimeLocal,
       "sub10UnitMgmtTimeNTPEnabled": sub10UnitMgmtTimeNTPEnabled,
       "sub10UnitMgmtTimeNTPServer1": sub10UnitMgmtTimeNTPServer1,
       "sub10UnitMgmtTimeNTPServer2": sub10UnitMgmtTimeNTPServer2,
       "sub10UnitMgmtTimeNTPPort": sub10UnitMgmtTimeNTPPort,
       "sub10UnitMgmtTimeNTPSyncStatus": sub10UnitMgmtTimeNTPSyncStatus,
       "sub10UnitMgmtDateTime": sub10UnitMgmtDateTime,
       "sub10UnitMgmtAlarms": sub10UnitMgmtAlarms,
       "sub10UnitMgmtAlarmTable": sub10UnitMgmtAlarmTable,
       "sub10UnitMgmtAlarmEntry": sub10UnitMgmtAlarmEntry,
       "sub10UnitMgmtAlarmIndex": sub10UnitMgmtAlarmIndex,
       "sub10UnitMgmtAlarmRowStatus": sub10UnitMgmtAlarmRowStatus,
       "sub10UnitMgmtAlarmName": sub10UnitMgmtAlarmName,
       "sub10UnitMgmtAlarmSeverity": sub10UnitMgmtAlarmSeverity,
       "sub10UnitMgmtAlarmMeasObject": sub10UnitMgmtAlarmMeasObject,
       "sub10UnitMgmtAlarmMonitorIntvl": sub10UnitMgmtAlarmMonitorIntvl,
       "sub10UnitMgmtAlarmRaiseOper": sub10UnitMgmtAlarmRaiseOper,
       "sub10UnitMgmtAlarmRaiseThresh": sub10UnitMgmtAlarmRaiseThresh,
       "sub10UnitMgmtAlarmClearOper": sub10UnitMgmtAlarmClearOper,
       "sub10UnitMgmtAlarmClearThresh": sub10UnitMgmtAlarmClearThresh,
       "sub10UnitMgmtAlarmRaiseIntvls": sub10UnitMgmtAlarmRaiseIntvls,
       "sub10UnitMgmtAlarmClearIntvls": sub10UnitMgmtAlarmClearIntvls,
       "sub10UnitMgmtAlarmType": sub10UnitMgmtAlarmType,
       "sub10UnitMgmtAlarmSmtpAddress": sub10UnitMgmtAlarmSmtpAddress,
       "sub10UnitMgmtAlarmToSyslog": sub10UnitMgmtAlarmToSyslog,
       "sub10UnitMgmtAlarmEnabled": sub10UnitMgmtAlarmEnabled,
       "sub10UnitMgmtAlarmMeasObjectVal": sub10UnitMgmtAlarmMeasObjectVal,
       "sub10UnitMgmtAlarmToSNMP": sub10UnitMgmtAlarmToSNMP,
       "sub10UnitMgmtAlarmMeasObjIndex": sub10UnitMgmtAlarmMeasObjIndex,
       "sub10UnitMgmtAlarmsUserDefStart": sub10UnitMgmtAlarmsUserDefStart,
       "sub10UnitMgmtSnmp": sub10UnitMgmtSnmp,
       "sub10UnitMgmtSnmpAgent": sub10UnitMgmtSnmpAgent,
       "sub10UnitMgmtSnmpTraps": sub10UnitMgmtSnmpTraps,
       "sub10UnitMgmtSnmpv320Mib": sub10UnitMgmtSnmpv320Mib,
       "sub10UnitMgmtSnmpv3": sub10UnitMgmtSnmpv3,
       "sub10UnitMgmtSnmpTrpDstTable": sub10UnitMgmtSnmpTrpDstTable,
       "sub10UnitMgmtSnmpTrpDstEntry": sub10UnitMgmtSnmpTrpDstEntry,
       "sub10UnitMgmtSnmpTrpDstIndex": sub10UnitMgmtSnmpTrpDstIndex,
       "sub10UnitMgmtSnmpTrpDstRowStatus": sub10UnitMgmtSnmpTrpDstRowStatus,
       "sub10UnitMgmtSnmpTrpDstIpAddr": sub10UnitMgmtSnmpTrpDstIpAddr,
       "sub10UnitMgmtSnmpTrpDstCommunity": sub10UnitMgmtSnmpTrpDstCommunity,
       "sub10UnitMgmtSnmpEngineIdFormat": sub10UnitMgmtSnmpEngineIdFormat,
       "sub10UnitMgmtSnmpEngineIdText": sub10UnitMgmtSnmpEngineIdText,
       "sub10UnitMgmtSnmpEngineId": sub10UnitMgmtSnmpEngineId,
       "sub10UnitMgmtSnmpOperAuthProto": sub10UnitMgmtSnmpOperAuthProto,
       "sub10UnitMgmtSnmpOperPrivProto": sub10UnitMgmtSnmpOperPrivProto,
       "sub10UnitMgmtSnmpAdminAuthProto": sub10UnitMgmtSnmpAdminAuthProto,
       "sub10UnitMgmtSnmpAdminPrivProto": sub10UnitMgmtSnmpAdminPrivProto,
       "sub10UnitMgmtSnmpMaintAuthProto": sub10UnitMgmtSnmpMaintAuthProto,
       "sub10UnitMgmtSnmpMaintPrivProto": sub10UnitMgmtSnmpMaintPrivProto,
       "sub10UnitMgmtSnmpUserTable": sub10UnitMgmtSnmpUserTable,
       "sub10UnitMgmtSnmpUserEntry": sub10UnitMgmtSnmpUserEntry,
       "sub10UnitMgmtSnmpUserIndex": sub10UnitMgmtSnmpUserIndex,
       "sub10UnitMgmtSnmpUserRowStatus": sub10UnitMgmtSnmpUserRowStatus,
       "sub10UnitMgmtSnmpUserName": sub10UnitMgmtSnmpUserName,
       "sub10UnitMgmtSnmpUserGroup": sub10UnitMgmtSnmpUserGroup,
       "sub10UnitMgmtSnmpUserAuthPwd": sub10UnitMgmtSnmpUserAuthPwd,
       "sub10UnitMgmtSnmpUserAuthPwdChk": sub10UnitMgmtSnmpUserAuthPwdChk,
       "sub10UnitMgmtSnmpUserPrivPwd": sub10UnitMgmtSnmpUserPrivPwd,
       "sub10UnitMgmtSnmpUserPrivPwdChk": sub10UnitMgmtSnmpUserPrivPwdChk,
       "sub10UnitMgmtSnmpAccessTable": sub10UnitMgmtSnmpAccessTable,
       "sub10UnitMgmtSnmpAccessEntry": sub10UnitMgmtSnmpAccessEntry,
       "sub10UnitMgmtSnmpAccessIndex": sub10UnitMgmtSnmpAccessIndex,
       "sub10UnitMgmtSnmpAccessRowStatus": sub10UnitMgmtSnmpAccessRowStatus,
       "sub10UnitMgmtSnmpAccessName": sub10UnitMgmtSnmpAccessName,
       "sub10UnitMgmtSnmpAccessIpAddr": sub10UnitMgmtSnmpAccessIpAddr,
       "sub10UnitMgmtSnmpTargetTable": sub10UnitMgmtSnmpTargetTable,
       "sub10UnitMgmtSnmpTargetEntry": sub10UnitMgmtSnmpTargetEntry,
       "sub10UnitMgmtSnmpTargetIndex": sub10UnitMgmtSnmpTargetIndex,
       "sub10UnitMgmtSnmpTargetRowStatus": sub10UnitMgmtSnmpTargetRowStatus,
       "sub10UnitMgmtSnmpTargetName": sub10UnitMgmtSnmpTargetName,
       "sub10UnitMgmtSnmpTargetIpAddr": sub10UnitMgmtSnmpTargetIpAddr,
       "sub10UnitMgmtSnmpTargetUserName": sub10UnitMgmtSnmpTargetUserName,
       "sub10UnitMgmtSmtp": sub10UnitMgmtSmtp,
       "sub10UnitMgmtFirmware": sub10UnitMgmtFirmware,
       "sub10UnitMgmtFirmwareSelectBank": sub10UnitMgmtFirmwareSelectBank,
       "sub10UnitMgmtFirmwareLoadedBank": sub10UnitMgmtFirmwareLoadedBank,
       "sub10UnitMgmtFirmwareVersion": sub10UnitMgmtFirmwareVersion,
       "sub10UnitMgmtFirmwareBootVersion": sub10UnitMgmtFirmwareBootVersion,
       "sub10UnitMgmtFirmwareAction": sub10UnitMgmtFirmwareAction,
       "sub10UnitMgmtFirmwareBankTable": sub10UnitMgmtFirmwareBankTable,
       "sub10UnitMgmtFirmwareBankEntry": sub10UnitMgmtFirmwareBankEntry,
       "sub10UnitMgmtFirmwareBankIndex": sub10UnitMgmtFirmwareBankIndex,
       "sub10UnitMgmtFirmwareBankVersion": sub10UnitMgmtFirmwareBankVersion,
       "sub10UnitMgmtFirmwareBankImage": sub10UnitMgmtFirmwareBankImage,
       "sub10UnitMgmtFirmwareUplImage": sub10UnitMgmtFirmwareUplImage,
       "sub10UnitMgmtFirmwareUplSvrIp": sub10UnitMgmtFirmwareUplSvrIp,
       "sub10UnitMgmtFirmwareFromBank": sub10UnitMgmtFirmwareFromBank,
       "sub10UnitMgmtFirmwareToBank": sub10UnitMgmtFirmwareToBank,
       "sub10UnitMgmtFirmwareActStatus": sub10UnitMgmtFirmwareActStatus,
       "sub10UnitMgmtFirmwareActProgress": sub10UnitMgmtFirmwareActProgress,
       "sub10UnitMgmtDNS": sub10UnitMgmtDNS,
       "sub10UnitMgmtDNSTable": sub10UnitMgmtDNSTable,
       "sub10UnitMgmtDNSEntry": sub10UnitMgmtDNSEntry,
       "sub10UnitMgmtDNSIndex": sub10UnitMgmtDNSIndex,
       "sub10UnitMgmtDNServer": sub10UnitMgmtDNServer,
       "sub10UnitMgmtEncryption": sub10UnitMgmtEncryption,
       "sub10UnitMgmtEncryptMode": sub10UnitMgmtEncryptMode,
       "sub10UnitMgmtEncryptKey": sub10UnitMgmtEncryptKey,
       "sub10UnitMgmtLicense": sub10UnitMgmtLicense,
       "sub10UnitMgmtLicenseKey": sub10UnitMgmtLicenseKey,
       "sub10UnitMgmtLicenseAES": sub10UnitMgmtLicenseAES,
       "sub10UnitMgmtSyncE": sub10UnitMgmtSyncE,
       "sub10UnitMgmtSyncEMode": sub10UnitMgmtSyncEMode,
       "sub10UnitMgmtActions": sub10UnitMgmtActions,
       "sub10UnitMgmtTransaction": sub10UnitMgmtTransaction,
       "sub10UnitMgmtTransactionStatus": sub10UnitMgmtTransactionStatus,
       "sub10UnitMgmtRollbackTimeout": sub10UnitMgmtRollbackTimeout,
       "sub10UnitMgmtTransactionMode": sub10UnitMgmtTransactionMode,
       "sub10UnitMgmtResetAction": sub10UnitMgmtResetAction,
       "sub10UnitMgmtResetStatsGroup": sub10UnitMgmtResetStatsGroup,
       "sub10UnitMgmtResetAlarmsType": sub10UnitMgmtResetAlarmsType,
       "sub10Ethernet": sub10Ethernet,
       "sub10EthernetStatus": sub10EthernetStatus,
       "sub10EthernetLocalStatus": sub10EthernetLocalStatus,
       "sub10EthLclStatusTable": sub10EthLclStatusTable,
       "sub10EthLclStatusEntry": sub10EthLclStatusEntry,
       "sub10EthLclLinkStatus": sub10EthLclLinkStatus,
       "sub10EthLclMacAddress": sub10EthLclMacAddress,
       "sub10EthLclSpeed": sub10EthLclSpeed,
       "sub10EthLclDuplex": sub10EthLclDuplex,
       "sub10EthLclMDI": sub10EthLclMDI,
       "sub10EthIfIndex": sub10EthIfIndex,
       "sub10EthernetRemoteStatus": sub10EthernetRemoteStatus,
       "sub10EthRmtStatusTable": sub10EthRmtStatusTable,
       "sub10EthRmtStatusEntry": sub10EthRmtStatusEntry,
       "sub10EthRmtLinkStatus": sub10EthRmtLinkStatus,
       "sub10EthRmtMacAddress": sub10EthRmtMacAddress,
       "sub10EthRmtSpeed": sub10EthRmtSpeed,
       "sub10EthRmtDuplex": sub10EthRmtDuplex,
       "sub10EthRmtMDI": sub10EthRmtMDI,
       "sub10EthernetMgmt": sub10EthernetMgmt,
       "sub10EthMgmtPhy": sub10EthMgmtPhy,
       "sub10EthMgmtPhyTable": sub10EthMgmtPhyTable,
       "sub10EthMgmtPhyEntry": sub10EthMgmtPhyEntry,
       "sub10EthMgmtPhyAutoNeg": sub10EthMgmtPhyAutoNeg,
       "sub10EthMgmtPhySpeed": sub10EthMgmtPhySpeed,
       "sub10EthMgmtPhyDuplex": sub10EthMgmtPhyDuplex,
       "sub10EthMgmtPhyMDI": sub10EthMgmtPhyMDI,
       "sub10EthMgmtVlan": sub10EthMgmtVlan,
       "sub10EthMgmtVlanFiltering": sub10EthMgmtVlanFiltering,
       "sub10EthMgmtVlanDefaultEnabled": sub10EthMgmtVlanDefaultEnabled,
       "sub10EthMgmtVlanDefaultId": sub10EthMgmtVlanDefaultId,
       "sub10EthMgmtVlanDefaultPriority": sub10EthMgmtVlanDefaultPriority,
       "sub10EthMgmtVlanDefaultDEI": sub10EthMgmtVlanDefaultDEI,
       "sub10EthMgmtVlanIngressAction": sub10EthMgmtVlanIngressAction,
       "sub10EthMgmtVlanEgressAction": sub10EthMgmtVlanEgressAction,
       "sub10EthMgmtVlanAllowedTable": sub10EthMgmtVlanAllowedTable,
       "sub10EthMgmtVlanAllowedEntry": sub10EthMgmtVlanAllowedEntry,
       "sub10EthMgmtVlanAllowedIndex": sub10EthMgmtVlanAllowedIndex,
       "sub10EthMgmtVlanAllowedRowStatus": sub10EthMgmtVlanAllowedRowStatus,
       "sub10EthMgmtVlanAllowedId": sub10EthMgmtVlanAllowedId,
       "sub10EthMgmtQoS": sub10EthMgmtQoS,
       "sub10EthMgmtQoSActiveState": sub10EthMgmtQoSActiveState,
       "sub10EthMgmtQoSMode": sub10EthMgmtQoSMode,
       "sub10EthMgmtQoSUntaggedQueue": sub10EthMgmtQoSUntaggedQueue,
       "sub10EthMgmtQoSQTable": sub10EthMgmtQoSQTable,
       "sub10EthMgmtQoSQEntry": sub10EthMgmtQoSQEntry,
       "sub10EthMgmtQoSQIndex": sub10EthMgmtQoSQIndex,
       "sub10EthMgmtQoSQSchedulingType": sub10EthMgmtQoSQSchedulingType,
       "sub10EthMgmtQoSQDWRRWeight": sub10EthMgmtQoSQDWRRWeight,
       "sub10EthMgmtQoSQCongestionPolicy": sub10EthMgmtQoSQCongestionPolicy,
       "sub10EthMgmtQoSQSizeMax": sub10EthMgmtQoSQSizeMax,
       "sub10EthMgmtQoSQLen": sub10EthMgmtQoSQLen,
       "sub10EthMgmtQoSVlanMappingNumber": sub10EthMgmtQoSVlanMappingNumber,
       "sub10EthMgmtQoSVlanTable": sub10EthMgmtQoSVlanTable,
       "sub10EthMgmtQoSVlanEntry": sub10EthMgmtQoSVlanEntry,
       "sub10EthMgmtQoSVlanIndex": sub10EthMgmtQoSVlanIndex,
       "sub10EthMgmtQoSVlanId": sub10EthMgmtQoSVlanId,
       "sub10EthMgmtQoSVlanQueue": sub10EthMgmtQoSVlanQueue,
       "sub10EthMgmtQoSPCPTable": sub10EthMgmtQoSPCPTable,
       "sub10EthMgmtQoSPCPEntry": sub10EthMgmtQoSPCPEntry,
       "sub10EthMgmtQoSPCPIndex": sub10EthMgmtQoSPCPIndex,
       "sub10EthMgmtQoSPCPQueue": sub10EthMgmtQoSPCPQueue,
       "sub10EthMgmtQoSDSCPMappingNumber": sub10EthMgmtQoSDSCPMappingNumber,
       "sub10EthMgmtQoSDSCPTable": sub10EthMgmtQoSDSCPTable,
       "sub10EthMgmtQoSDSCPEntry": sub10EthMgmtQoSDSCPEntry,
       "sub10EthMgmtQoSDSCPIndex": sub10EthMgmtQoSDSCPIndex,
       "sub10EthMgmtQoSDSCPMarking": sub10EthMgmtQoSDSCPMarking,
       "sub10EthMgmtQoSDSCPQueue": sub10EthMgmtQoSDSCPQueue,
       "sub10EthMgmtQoSMPLSMappingNumber": sub10EthMgmtQoSMPLSMappingNumber,
       "sub10EthMgmtQoSMPLSTable": sub10EthMgmtQoSMPLSTable,
       "sub10EthMgmtQoSMPLSEntry": sub10EthMgmtQoSMPLSEntry,
       "sub10EthMgmtQoSMPLSIndex": sub10EthMgmtQoSMPLSIndex,
       "sub10EthMgmtQoSMPLSTrafficClass": sub10EthMgmtQoSMPLSTrafficClass,
       "sub10EthMgmtQoSMPLSQueue": sub10EthMgmtQoSMPLSQueue,
       "sub10EthMgmtStats": sub10EthMgmtStats,
       "sub10EthMgmtStatsActiveTable": sub10EthMgmtStatsActiveTable,
       "sub10EthMgmtStatsActiveEntry": sub10EthMgmtStatsActiveEntry,
       "sub10EthMgmtStatsActiveIndex": sub10EthMgmtStatsActiveIndex,
       "sub10EthMgmtStatsActiveName": sub10EthMgmtStatsActiveName,
       "sub10EthMgmtStatsActiveState": sub10EthMgmtStatsActiveState,
       "sub10EthernetStats": sub10EthernetStats,
       "sub10EthStatsTimeElapsed": sub10EthStatsTimeElapsed,
       "sub10EthernetStatsCurrent": sub10EthernetStatsCurrent,
       "sub10EthernetStatsCurrTable": sub10EthernetStatsCurrTable,
       "sub10EthernetStatsCurrEntry": sub10EthernetStatsCurrEntry,
       "sub10EthStatsCurrRxOctets": sub10EthStatsCurrRxOctets,
       "sub10EthStatsCurrRxGoodFrms": sub10EthStatsCurrRxGoodFrms,
       "sub10EthStatsCurrRxBcastFrms": sub10EthStatsCurrRxBcastFrms,
       "sub10EthStatsCurrRxMcastFrms": sub10EthStatsCurrRxMcastFrms,
       "sub10EthStatsCurrRxPauseFrms": sub10EthStatsCurrRxPauseFrms,
       "sub10EthStatsCurrRxCRCErrs": sub10EthStatsCurrRxCRCErrs,
       "sub10EthStatsCurrRxAlignErrs": sub10EthStatsCurrRxAlignErrs,
       "sub10EthStatsCurrRxOversized": sub10EthStatsCurrRxOversized,
       "sub10EthStatsCurrRxJabberFrms": sub10EthStatsCurrRxJabberFrms,
       "sub10EthStatsCurrRxUndersized": sub10EthStatsCurrRxUndersized,
       "sub10EthStatsCurrRxFragments": sub10EthStatsCurrRxFragments,
       "sub10EthStatsCurrRxSOFOvrns": sub10EthStatsCurrRxSOFOvrns,
       "sub10EthStatsCurrTxOctets": sub10EthStatsCurrTxOctets,
       "sub10EthStatsCurrTxGoodFrms": sub10EthStatsCurrTxGoodFrms,
       "sub10EthStatsCurrTxBcastFrms": sub10EthStatsCurrTxBcastFrms,
       "sub10EthStatsCurrTxMcastFrms": sub10EthStatsCurrTxMcastFrms,
       "sub10EthStatsCurrTxPauseFrms": sub10EthStatsCurrTxPauseFrms,
       "sub10EthStatsCurrTxDeferred": sub10EthStatsCurrTxDeferred,
       "sub10EthStatsCurrTxCollsn": sub10EthStatsCurrTxCollsn,
       "sub10EthStatsCurrTxSnglCollsn": sub10EthStatsCurrTxSnglCollsn,
       "sub10EthStatsCurrTxMlplCollsn": sub10EthStatsCurrTxMlplCollsn,
       "sub10EthStatsCurrTxExsvCollsn": sub10EthStatsCurrTxExsvCollsn,
       "sub10EthStatsCurrTxLtCollsn": sub10EthStatsCurrTxLtCollsn,
       "sub10EthStatsCurrTxCSenseErrs": sub10EthStatsCurrTxCSenseErrs,
       "sub10EthStatsCurrPkts64Octets": sub10EthStatsCurrPkts64Octets,
       "sub10EthStatsCurrPkts65T127": sub10EthStatsCurrPkts65T127,
       "sub10EthStatsCurrPkts128T255": sub10EthStatsCurrPkts128T255,
       "sub10EthStatsCurrPkts256T511": sub10EthStatsCurrPkts256T511,
       "sub10EthStatsCurrPkts512T1023": sub10EthStatsCurrPkts512T1023,
       "sub10EthStatsCurrPkts1024TMax": sub10EthStatsCurrPkts1024TMax,
       "sub10EthStatsCurrRxMbps": sub10EthStatsCurrRxMbps,
       "sub10EthStatsCurrTxMbps": sub10EthStatsCurrTxMbps,
       "sub10EthStatsCurrRxMbpsMin": sub10EthStatsCurrRxMbpsMin,
       "sub10EthStatsCurrRxMbpsMax": sub10EthStatsCurrRxMbpsMax,
       "sub10EthStatsCurrRxMbpsAvg": sub10EthStatsCurrRxMbpsAvg,
       "sub10EthStatsCurrTxMbpsMin": sub10EthStatsCurrTxMbpsMin,
       "sub10EthStatsCurrTxMbpsMax": sub10EthStatsCurrTxMbpsMax,
       "sub10EthStatsCurrTxMbpsAvg": sub10EthStatsCurrTxMbpsAvg,
       "sub10EthStatsCurrRmtRxMbpsAvg": sub10EthStatsCurrRmtRxMbpsAvg,
       "sub10EthStatsCurrRmtTxMbpsAvg": sub10EthStatsCurrRmtTxMbpsAvg,
       "sub10EthernetStatsHistory": sub10EthernetStatsHistory,
       "sub10EthernetStats15mHistory": sub10EthernetStats15mHistory,
       "sub10EthStats15mHistIntvls": sub10EthStats15mHistIntvls,
       "sub10EthStats15mHistTable": sub10EthStats15mHistTable,
       "sub10EthStats15mHistEntry": sub10EthStats15mHistEntry,
       "sub10EthStats15mHistIntvl": sub10EthStats15mHistIntvl,
       "sub10EthStats15mHistTime": sub10EthStats15mHistTime,
       "sub10EthStats15mHistRxOctets": sub10EthStats15mHistRxOctets,
       "sub10EthStats15mHistRxGoodFrms": sub10EthStats15mHistRxGoodFrms,
       "sub10EthStats15mHistRxBcastFrms": sub10EthStats15mHistRxBcastFrms,
       "sub10EthStats15mHistRxMcastFrms": sub10EthStats15mHistRxMcastFrms,
       "sub10EthStats15mHistRxPauseFrms": sub10EthStats15mHistRxPauseFrms,
       "sub10EthStats15mHistRxCRCErrs": sub10EthStats15mHistRxCRCErrs,
       "sub10EthStats15mHistRxAlignErrs": sub10EthStats15mHistRxAlignErrs,
       "sub10EthStats15mHistRxOversized": sub10EthStats15mHistRxOversized,
       "sub10EthStats15mHistRxJabberFrms": sub10EthStats15mHistRxJabberFrms,
       "sub10EthStats15mHistRxUndersized": sub10EthStats15mHistRxUndersized,
       "sub10EthStats15mHistRxFragments": sub10EthStats15mHistRxFragments,
       "sub10EthStats15mHistRxSOFOvrns": sub10EthStats15mHistRxSOFOvrns,
       "sub10EthStats15mHistTxOctets": sub10EthStats15mHistTxOctets,
       "sub10EthStats15mHistTxGoodFrms": sub10EthStats15mHistTxGoodFrms,
       "sub10EthStats15mHistTxBcastFrms": sub10EthStats15mHistTxBcastFrms,
       "sub10EthStats15mHistTxMcastFrms": sub10EthStats15mHistTxMcastFrms,
       "sub10EthStats15mHistTxPauseFrms": sub10EthStats15mHistTxPauseFrms,
       "sub10EthStats15mHistTxDeferred": sub10EthStats15mHistTxDeferred,
       "sub10EthStats15mHistTxCollsn": sub10EthStats15mHistTxCollsn,
       "sub10EthStats15mHistTxSnglCollsn": sub10EthStats15mHistTxSnglCollsn,
       "sub10EthStats15mHistTxMlplCollsn": sub10EthStats15mHistTxMlplCollsn,
       "sub10EthStats15mHistTxExsvCollsn": sub10EthStats15mHistTxExsvCollsn,
       "sub10EthStats15mHistTxLtCollsn": sub10EthStats15mHistTxLtCollsn,
       "sub10EthStats15mHistTxCSenseErrs": sub10EthStats15mHistTxCSenseErrs,
       "sub10EthStats15mHistPkts64Octets": sub10EthStats15mHistPkts64Octets,
       "sub10EthStats15mHistPkts65T127": sub10EthStats15mHistPkts65T127,
       "sub10EthStats15mHistPkts128T255": sub10EthStats15mHistPkts128T255,
       "sub10EthStats15mHistPkts256T511": sub10EthStats15mHistPkts256T511,
       "sub10EthStats15mHistPkts512T1023": sub10EthStats15mHistPkts512T1023,
       "sub10EthStats15mHistPkts1024TMax": sub10EthStats15mHistPkts1024TMax,
       "sub10EthStats15mHistRxMbpsMin": sub10EthStats15mHistRxMbpsMin,
       "sub10EthStats15mHistRxMbpsMax": sub10EthStats15mHistRxMbpsMax,
       "sub10EthStats15mHistRxMbpsAvg": sub10EthStats15mHistRxMbpsAvg,
       "sub10EthStats15mHistTxMbpsMin": sub10EthStats15mHistTxMbpsMin,
       "sub10EthStats15mHistTxMbpsMax": sub10EthStats15mHistTxMbpsMax,
       "sub10EthStats15mHistTxMbpsAvg": sub10EthStats15mHistTxMbpsAvg,
       "sub10EthStats1dHistory": sub10EthStats1dHistory,
       "sub10EthStats1dHistIntvls": sub10EthStats1dHistIntvls,
       "sub10EthStats1dHistTable": sub10EthStats1dHistTable,
       "sub10EthStats1dHistEntry": sub10EthStats1dHistEntry,
       "sub10EthStats1dHistIntvl": sub10EthStats1dHistIntvl,
       "sub10EthStats1dHistTime": sub10EthStats1dHistTime,
       "sub10EthStats1dHistRxOctets": sub10EthStats1dHistRxOctets,
       "sub10EthStats1dHistRxGoodFrms": sub10EthStats1dHistRxGoodFrms,
       "sub10EthStats1dHistRxBcastFrms": sub10EthStats1dHistRxBcastFrms,
       "sub10EthStats1dHistRxMcastFrms": sub10EthStats1dHistRxMcastFrms,
       "sub10EthStats1dHistRxPauseFrms": sub10EthStats1dHistRxPauseFrms,
       "sub10EthStats1dHistRxCRCErrs": sub10EthStats1dHistRxCRCErrs,
       "sub10EthStats1dHistRxAlignErrs": sub10EthStats1dHistRxAlignErrs,
       "sub10EthStats1dHistRxOversized": sub10EthStats1dHistRxOversized,
       "sub10EthStats1dHistRxJabberFrms": sub10EthStats1dHistRxJabberFrms,
       "sub10EthStats1dHistRxUndersized": sub10EthStats1dHistRxUndersized,
       "sub10EthStats1dHistRxFragments": sub10EthStats1dHistRxFragments,
       "sub10EthStats1dHistRxSOFOvrns": sub10EthStats1dHistRxSOFOvrns,
       "sub10EthStats1dHistTxOctets": sub10EthStats1dHistTxOctets,
       "sub10EthStats1dHistTxGoodFrms": sub10EthStats1dHistTxGoodFrms,
       "sub10EthStats1dHistTxBcastFrms": sub10EthStats1dHistTxBcastFrms,
       "sub10EthStats1dHistTxMcastFrms": sub10EthStats1dHistTxMcastFrms,
       "sub10EthStats1dHistTxPauseFrms": sub10EthStats1dHistTxPauseFrms,
       "sub10EthStats1dHistTxDeferred": sub10EthStats1dHistTxDeferred,
       "sub10EthStats1dHistTxCollsn": sub10EthStats1dHistTxCollsn,
       "sub10EthStats1dHistTxSnglCollsn": sub10EthStats1dHistTxSnglCollsn,
       "sub10EthStats1dHistTxMlplCollsn": sub10EthStats1dHistTxMlplCollsn,
       "sub10EthStats1dHistTxExsvCollsn": sub10EthStats1dHistTxExsvCollsn,
       "sub10EthStats1dHistTxLtCollsn": sub10EthStats1dHistTxLtCollsn,
       "sub10EthStats1dHistTxCSenseErrs": sub10EthStats1dHistTxCSenseErrs,
       "sub10EthStats1dHistPkts64Octets": sub10EthStats1dHistPkts64Octets,
       "sub10EthStats1dHistPkts65T127": sub10EthStats1dHistPkts65T127,
       "sub10EthStats1dHistPkts128T255": sub10EthStats1dHistPkts128T255,
       "sub10EthStats1dHistPkts256T511": sub10EthStats1dHistPkts256T511,
       "sub10EthStats1dHistPkts512T1023": sub10EthStats1dHistPkts512T1023,
       "sub10EthStats1dHistPkts1024TMax": sub10EthStats1dHistPkts1024TMax,
       "sub10EthStats1dHistRxMbpsMin": sub10EthStats1dHistRxMbpsMin,
       "sub10EthStats1dHistRxMbpsMax": sub10EthStats1dHistRxMbpsMax,
       "sub10EthStats1dHistRxMbpsAvg": sub10EthStats1dHistRxMbpsAvg,
       "sub10EthStats1dHistTxMbpsMin": sub10EthStats1dHistTxMbpsMin,
       "sub10EthStats1dHistTxMbpsMax": sub10EthStats1dHistTxMbpsMax,
       "sub10EthStats1dHistTxMbpsAvg": sub10EthStats1dHistTxMbpsAvg,
       "sub10Radio": sub10Radio,
       "sub10RadioStatus": sub10RadioStatus,
       "sub10RadioLocalStatus": sub10RadioLocalStatus,
       "sub10RadioLclLinkStatus": sub10RadioLclLinkStatus,
       "sub10RadioLclTxPower": sub10RadioLclTxPower,
       "sub10RadioLclRxPower": sub10RadioLclRxPower,
       "sub10RadioLclVectErr": sub10RadioLclVectErr,
       "sub10RadioLclLnkLoss": sub10RadioLclLnkLoss,
       "sub10RadioLclAlignmentMode": sub10RadioLclAlignmentMode,
       "sub10RadioLclDataRate": sub10RadioLclDataRate,
       "sub10RadioLclMWUType": sub10RadioLclMWUType,
       "sub10RadioLclAFER": sub10RadioLclAFER,
       "sub10RadioLclRxModulationMode": sub10RadioLclRxModulationMode,
       "sub10RadioLclTxModulationMode": sub10RadioLclTxModulationMode,
       "sub10RadioRemoteStatus": sub10RadioRemoteStatus,
       "sub10RadioRmtLinkStatus": sub10RadioRmtLinkStatus,
       "sub10RadioRmtTxPower": sub10RadioRmtTxPower,
       "sub10RadioRmtRxPower": sub10RadioRmtRxPower,
       "sub10RadioRmtVectErr": sub10RadioRmtVectErr,
       "sub10RadioRmtLnkLoss": sub10RadioRmtLnkLoss,
       "sub10RadioRmtAlignmentMode": sub10RadioRmtAlignmentMode,
       "sub10RadioRmtAFER": sub10RadioRmtAFER,
       "sub10RadioMgmt": sub10RadioMgmt,
       "sub10RadioMgmtTxPowerLimit": sub10RadioMgmtTxPowerLimit,
       "sub10RadioMgmtTxRxFreq": sub10RadioMgmtTxRxFreq,
       "sub10RadioMgmtAPCMode": sub10RadioMgmtAPCMode,
       "sub10RadioMgmtModulationMode": sub10RadioMgmtModulationMode,
       "sub10RadioMgmtAmod": sub10RadioMgmtAmod,
       "sub10RadioMgmtAlignmentMode": sub10RadioMgmtAlignmentMode,
       "sub10RadioMgmtMWUChannelWidth": sub10RadioMgmtMWUChannelWidth,
       "sub10RadioMgmtStats": sub10RadioMgmtStats,
       "sub10RadioMgmtStats1dPersist": sub10RadioMgmtStats1dPersist,
       "sub10RadioMgmtStatsActiveTable": sub10RadioMgmtStatsActiveTable,
       "sub10RadioMgmtStatsActiveEntry": sub10RadioMgmtStatsActiveEntry,
       "sub10RadioMgmtStatsActiveIndex": sub10RadioMgmtStatsActiveIndex,
       "sub10RadioMgmtStatsActiveName": sub10RadioMgmtStatsActiveName,
       "sub10RadioMgmtStatsActiveState": sub10RadioMgmtStatsActiveState,
       "sub10RadioMgmtDataRate": sub10RadioMgmtDataRate,
       "sub10RadioStats": sub10RadioStats,
       "sub10RadioStatsTimeElapsed": sub10RadioStatsTimeElapsed,
       "sub10RadioStatsCurrent": sub10RadioStatsCurrent,
       "sub10RadioStatsCurrTxPowerMin": sub10RadioStatsCurrTxPowerMin,
       "sub10RadioStatsCurrTxPowerMax": sub10RadioStatsCurrTxPowerMax,
       "sub10RadioStatsCurrTxPowerAvg": sub10RadioStatsCurrTxPowerAvg,
       "sub10RadioStatsCurrRxPowerMin": sub10RadioStatsCurrRxPowerMin,
       "sub10RadioStatsCurrRxPowerMax": sub10RadioStatsCurrRxPowerMax,
       "sub10RadioStatsCurrRxPowerAvg": sub10RadioStatsCurrRxPowerAvg,
       "sub10RadioStatsCurrVectErrMin": sub10RadioStatsCurrVectErrMin,
       "sub10RadioStatsCurrVectErrMax": sub10RadioStatsCurrVectErrMax,
       "sub10RadioStatsCurrVectErrAvg": sub10RadioStatsCurrVectErrAvg,
       "sub10RadioStatsCurrLnkLossMin": sub10RadioStatsCurrLnkLossMin,
       "sub10RadioStatsCurrLnkLossMax": sub10RadioStatsCurrLnkLossMax,
       "sub10RadioStatsCurrLnkLossAvg": sub10RadioStatsCurrLnkLossAvg,
       "sub10RadioStatsCurrRxFrms": sub10RadioStatsCurrRxFrms,
       "sub10RadioStatsCurrTxFrms": sub10RadioStatsCurrTxFrms,
       "sub10RadioStatsCurrRxPkts": sub10RadioStatsCurrRxPkts,
       "sub10RadioStatsCurrTxPkts": sub10RadioStatsCurrTxPkts,
       "sub10RadioStatsCurrRxMgmtPkts": sub10RadioStatsCurrRxMgmtPkts,
       "sub10RadioStatsCurrTxMgmtPkts": sub10RadioStatsCurrTxMgmtPkts,
       "sub10RadioStatsCurrRxBadFrms": sub10RadioStatsCurrRxBadFrms,
       "sub10RadioStatsCurrMWUTempMin": sub10RadioStatsCurrMWUTempMin,
       "sub10RadioStatsCurrMWUTempMax": sub10RadioStatsCurrMWUTempMax,
       "sub10RadioStatsCurrMWUTempAvg": sub10RadioStatsCurrMWUTempAvg,
       "sub10RadioStatsCurrQPSKTo8PSK": sub10RadioStatsCurrQPSKTo8PSK,
       "sub10RadioStatsCurr8PSKToQPSK": sub10RadioStatsCurr8PSKToQPSK,
       "sub10RadioStatsCurrAFERMin": sub10RadioStatsCurrAFERMin,
       "sub10RadioStatsCurrAFERMax": sub10RadioStatsCurrAFERMax,
       "sub10RadioStatsCurrAFERAvg": sub10RadioStatsCurrAFERAvg,
       "sub10RadioStatsCurrRmtTxPowerAvg": sub10RadioStatsCurrRmtTxPowerAvg,
       "sub10RadioStatsCurrRmtRxPowerAvg": sub10RadioStatsCurrRmtRxPowerAvg,
       "sub10RadioStatsCurrRmtVectErrAvg": sub10RadioStatsCurrRmtVectErrAvg,
       "sub10RadioStatsCurrRmtLnkLossAvg": sub10RadioStatsCurrRmtLnkLossAvg,
       "sub10RadioStatsCurrRmtMWUTempAvg": sub10RadioStatsCurrRmtMWUTempAvg,
       "sub10RadioStatsCurrRmtAFERAvg": sub10RadioStatsCurrRmtAFERAvg,
       "sub10RadioStatsCurrRxQPSK": sub10RadioStatsCurrRxQPSK,
       "sub10RadioStatsCurrRx8PSK": sub10RadioStatsCurrRx8PSK,
       "sub10RadioStatsCurrTxQPSK": sub10RadioStatsCurrTxQPSK,
       "sub10RadioStatsCurrTx8PSK": sub10RadioStatsCurrTx8PSK,
       "sub10RadioStatsHistory": sub10RadioStatsHistory,
       "sub10RadioStats1mHistory": sub10RadioStats1mHistory,
       "sub10RadioStats1mHistIntvls": sub10RadioStats1mHistIntvls,
       "sub10RadioStats1mHistTable": sub10RadioStats1mHistTable,
       "sub10RadioStats1mHistEntry": sub10RadioStats1mHistEntry,
       "sub10RadioStats1mHistIntvl": sub10RadioStats1mHistIntvl,
       "sub10RadioStats1mHistTime": sub10RadioStats1mHistTime,
       "sub10RadioStats1mHistTxPowerMin": sub10RadioStats1mHistTxPowerMin,
       "sub10RadioStats1mHistTxPowerMax": sub10RadioStats1mHistTxPowerMax,
       "sub10RadioStats1mHistTxPowerAvg": sub10RadioStats1mHistTxPowerAvg,
       "sub10RadioStats1mHistRxPowerMin": sub10RadioStats1mHistRxPowerMin,
       "sub10RadioStats1mHistRxPowerMax": sub10RadioStats1mHistRxPowerMax,
       "sub10RadioStats1mHistRxPowerAvg": sub10RadioStats1mHistRxPowerAvg,
       "sub10RadioStats1mHistVectErrMin": sub10RadioStats1mHistVectErrMin,
       "sub10RadioStats1mHistVectErrMax": sub10RadioStats1mHistVectErrMax,
       "sub10RadioStats1mHistVectErrAvg": sub10RadioStats1mHistVectErrAvg,
       "sub10RadioStats1mHistLnkLossMin": sub10RadioStats1mHistLnkLossMin,
       "sub10RadioStats1mHistLnkLossMax": sub10RadioStats1mHistLnkLossMax,
       "sub10RadioStats1mHistLnkLossAvg": sub10RadioStats1mHistLnkLossAvg,
       "sub10RadioStats1mHistMWUTempMin": sub10RadioStats1mHistMWUTempMin,
       "sub10RadioStats1mHistMWUTempMax": sub10RadioStats1mHistMWUTempMax,
       "sub10RadioStats1mHistMWUTempAvg": sub10RadioStats1mHistMWUTempAvg,
       "sub10RadioStats1mHistRxFrms": sub10RadioStats1mHistRxFrms,
       "sub10RadioStats1mHistTxFrms": sub10RadioStats1mHistTxFrms,
       "sub10RadioStats1mHistRxPkts": sub10RadioStats1mHistRxPkts,
       "sub10RadioStats1mHistTxPkts": sub10RadioStats1mHistTxPkts,
       "sub10RadioStats1mHistRxMgmtPkts": sub10RadioStats1mHistRxMgmtPkts,
       "sub10RadioStats1mHistTxMgmtPkts": sub10RadioStats1mHistTxMgmtPkts,
       "sub10RadioStats1mHistRxBadFrms": sub10RadioStats1mHistRxBadFrms,
       "sub10RadioStats1mHistQPSKTo8PSK": sub10RadioStats1mHistQPSKTo8PSK,
       "sub10RadioStats1mHist8PSKToQPSK": sub10RadioStats1mHist8PSKToQPSK,
       "sub10RadioStats1mHistAFERMin": sub10RadioStats1mHistAFERMin,
       "sub10RadioStats1mHistAFERMax": sub10RadioStats1mHistAFERMax,
       "sub10RadioStats1mHistAFERAvg": sub10RadioStats1mHistAFERAvg,
       "sub10RadioStats1mHistRxQPSK": sub10RadioStats1mHistRxQPSK,
       "sub10RadioStats1mHistRx8PSK": sub10RadioStats1mHistRx8PSK,
       "sub10RadioStats1mHistTxQPSK": sub10RadioStats1mHistTxQPSK,
       "sub10RadioStats1mHistTx8PSK": sub10RadioStats1mHistTx8PSK,
       "sub10RadioStats15mHistory": sub10RadioStats15mHistory,
       "sub10RadioStats15mHistIntvls": sub10RadioStats15mHistIntvls,
       "sub10RadioStats15mHistTable": sub10RadioStats15mHistTable,
       "sub10RadioStats15mHistEntry": sub10RadioStats15mHistEntry,
       "sub10RadioStats15mHistIntvl": sub10RadioStats15mHistIntvl,
       "sub10RadioStats15mHistTime": sub10RadioStats15mHistTime,
       "sub10RadioStats15mHistTxPowerMin": sub10RadioStats15mHistTxPowerMin,
       "sub10RadioStats15mHistTxPowerMax": sub10RadioStats15mHistTxPowerMax,
       "sub10RadioStats15mHistTxPowerAvg": sub10RadioStats15mHistTxPowerAvg,
       "sub10RadioStats15mHistRxPowerMin": sub10RadioStats15mHistRxPowerMin,
       "sub10RadioStats15mHistRxPowerMax": sub10RadioStats15mHistRxPowerMax,
       "sub10RadioStats15mHistRxPowerAvg": sub10RadioStats15mHistRxPowerAvg,
       "sub10RadioStats15mHistVectErrMin": sub10RadioStats15mHistVectErrMin,
       "sub10RadioStats15mHistVectErrMax": sub10RadioStats15mHistVectErrMax,
       "sub10RadioStats15mHistVectErrAvg": sub10RadioStats15mHistVectErrAvg,
       "sub10RadioStats15mHistLnkLossMin": sub10RadioStats15mHistLnkLossMin,
       "sub10RadioStats15mHistLnkLossMax": sub10RadioStats15mHistLnkLossMax,
       "sub10RadioStats15mHistLnkLossAvg": sub10RadioStats15mHistLnkLossAvg,
       "sub10RadioStats15mHistMWUTempMin": sub10RadioStats15mHistMWUTempMin,
       "sub10RadioStats15mHistMWUTempMax": sub10RadioStats15mHistMWUTempMax,
       "sub10RadioStats15mHistMWUTempAvg": sub10RadioStats15mHistMWUTempAvg,
       "sub10RadioStats15mHistRxFrms": sub10RadioStats15mHistRxFrms,
       "sub10RadioStats15mHistTxFrms": sub10RadioStats15mHistTxFrms,
       "sub10RadioStats15mHistRxPkts": sub10RadioStats15mHistRxPkts,
       "sub10RadioStats15mHistTxPkts": sub10RadioStats15mHistTxPkts,
       "sub10RadioStats15mHistRxMgmtPkts": sub10RadioStats15mHistRxMgmtPkts,
       "sub10RadioStats15mHistTxMgmtPkts": sub10RadioStats15mHistTxMgmtPkts,
       "sub10RadioStats15mHistRxBadFrms": sub10RadioStats15mHistRxBadFrms,
       "sub10RadioStats15mHistQPSKTo8PSK": sub10RadioStats15mHistQPSKTo8PSK,
       "sub10RadioStats15mHist8PSKToQPSK": sub10RadioStats15mHist8PSKToQPSK,
       "sub10RadioStats15mHistAFERMin": sub10RadioStats15mHistAFERMin,
       "sub10RadioStats15mHistAFERMax": sub10RadioStats15mHistAFERMax,
       "sub10RadioStats15mHistAFERAvg": sub10RadioStats15mHistAFERAvg,
       "sub10RadioStats15mHistRxQPSK": sub10RadioStats15mHistRxQPSK,
       "sub10RadioStats15mHistRx8PSK": sub10RadioStats15mHistRx8PSK,
       "sub10RadioStats15mHistTxQPSK": sub10RadioStats15mHistTxQPSK,
       "sub10RadioStats15mHistTx8PSK": sub10RadioStats15mHistTx8PSK,
       "sub10RadioStats1dHistory": sub10RadioStats1dHistory,
       "sub10RadioStats1dHistIntvls": sub10RadioStats1dHistIntvls,
       "sub10RadioStats1dHistTable": sub10RadioStats1dHistTable,
       "sub10RadioStats1dHistEntry": sub10RadioStats1dHistEntry,
       "sub10RadioStats1dHistIntvl": sub10RadioStats1dHistIntvl,
       "sub10RadioStats1dHistTime": sub10RadioStats1dHistTime,
       "sub10RadioStats1dHistTxPowerMin": sub10RadioStats1dHistTxPowerMin,
       "sub10RadioStats1dHistTxPowerMax": sub10RadioStats1dHistTxPowerMax,
       "sub10RadioStats1dHistTxPowerAvg": sub10RadioStats1dHistTxPowerAvg,
       "sub10RadioStats1dHistRxPowerMin": sub10RadioStats1dHistRxPowerMin,
       "sub10RadioStats1dHistRxPowerMax": sub10RadioStats1dHistRxPowerMax,
       "sub10RadioStats1dHistRxPowerAvg": sub10RadioStats1dHistRxPowerAvg,
       "sub10RadioStats1dHistVectErrMin": sub10RadioStats1dHistVectErrMin,
       "sub10RadioStats1dHistVectErrMax": sub10RadioStats1dHistVectErrMax,
       "sub10RadioStats1dHistVectErrAvg": sub10RadioStats1dHistVectErrAvg,
       "sub10RadioStats1dHistLnkLossMin": sub10RadioStats1dHistLnkLossMin,
       "sub10RadioStats1dHistLnkLossMax": sub10RadioStats1dHistLnkLossMax,
       "sub10RadioStats1dHistLnkLossAvg": sub10RadioStats1dHistLnkLossAvg,
       "sub10RadioStats1dHistMWUTempMin": sub10RadioStats1dHistMWUTempMin,
       "sub10RadioStats1dHistMWUTempMax": sub10RadioStats1dHistMWUTempMax,
       "sub10RadioStats1dHistMWUTempAvg": sub10RadioStats1dHistMWUTempAvg,
       "sub10RadioStats1dHistRxFrms": sub10RadioStats1dHistRxFrms,
       "sub10RadioStats1dHistTxFrms": sub10RadioStats1dHistTxFrms,
       "sub10RadioStats1dHistRxPkts": sub10RadioStats1dHistRxPkts,
       "sub10RadioStats1dHistTxPkts": sub10RadioStats1dHistTxPkts,
       "sub10RadioStats1dHistRxMgmtPkts": sub10RadioStats1dHistRxMgmtPkts,
       "sub10RadioStats1dHistTxMgmtPkts": sub10RadioStats1dHistTxMgmtPkts,
       "sub10RadioStats1dHistRxBadFrms": sub10RadioStats1dHistRxBadFrms,
       "sub10RadioStats1dHistQPSKTo8PSK": sub10RadioStats1dHistQPSKTo8PSK,
       "sub10RadioStats1dHist8PSKToQPSK": sub10RadioStats1dHist8PSKToQPSK,
       "sub10RadioStats1dHistAFERMin": sub10RadioStats1dHistAFERMin,
       "sub10RadioStats1dHistAFERMax": sub10RadioStats1dHistAFERMax,
       "sub10RadioStats1dHistAFERAvg": sub10RadioStats1dHistAFERAvg,
       "sub10RadioStats1dHistRxQPSK": sub10RadioStats1dHistRxQPSK,
       "sub10RadioStats1dHistRx8PSK": sub10RadioStats1dHistRx8PSK,
       "sub10RadioStats1dHistTxQPSK": sub10RadioStats1dHistTxQPSK,
       "sub10RadioStats1dHistTx8PSK": sub10RadioStats1dHistTx8PSK,
       "sub10MIBConformance": sub10MIBConformance,
       "sub10MIBCompliances": sub10MIBCompliances,
       "sub10Compliance": sub10Compliance,
       "sub10MIBGroups": sub10MIBGroups,
       "sub10NotificationsGrp": sub10NotificationsGrp,
       "sub10UnitLocalStatusGrp": sub10UnitLocalStatusGrp,
       "sub10UnitLclAlarmStateEntryGrp": sub10UnitLclAlarmStateEntryGrp,
       "sub10UnitRemoteStatusGrp": sub10UnitRemoteStatusGrp,
       "sub10UnitMgmtSystemGrp": sub10UnitMgmtSystemGrp,
       "sub10UnitMgmtIpGrp": sub10UnitMgmtIpGrp,
       "sub10UnitMgmtVlanGrp": sub10UnitMgmtVlanGrp,
       "sub10UnitMgmtUsersGrp": sub10UnitMgmtUsersGrp,
       "sub10UnitMgmtUserEntryGrp": sub10UnitMgmtUserEntryGrp,
       "sub10UnitMgmtTimeGrp": sub10UnitMgmtTimeGrp,
       "sub10UnitMgmtAlarmEntryGrp": sub10UnitMgmtAlarmEntryGrp,
       "sub10UnitMgmtAlarmsGrp": sub10UnitMgmtAlarmsGrp,
       "sub10UnitMgmtSnmpGrp": sub10UnitMgmtSnmpGrp,
       "sub10UnitMgmtSnmpTrpDstEntryGrp": sub10UnitMgmtSnmpTrpDstEntryGrp,
       "sub10UnitMgmtSnmpUserEntryGrp": sub10UnitMgmtSnmpUserEntryGrp,
       "sub10UnitMgmtSnmpAccessEntryGrp": sub10UnitMgmtSnmpAccessEntryGrp,
       "sub10UnitMgmtSnmpTargetEntryGrp": sub10UnitMgmtSnmpTargetEntryGrp,
       "sub10UnitMgmtFirmwareGrp": sub10UnitMgmtFirmwareGrp,
       "sub10UnitMgmtFirmwareBankEntryGrp": sub10UnitMgmtFirmwareBankEntryGrp,
       "sub10UnitMgmtDNSEntryGrp": sub10UnitMgmtDNSEntryGrp,
       "sub10UnitMgmtEncryptionGrp": sub10UnitMgmtEncryptionGrp,
       "sub10UnitMgmtLicenseGrp": sub10UnitMgmtLicenseGrp,
       "sub10UnitMgmtSyncEGrp": sub10UnitMgmtSyncEGrp,
       "sub10UnitMgmtActionsGrp": sub10UnitMgmtActionsGrp,
       "sub10EthLclStatusEntryGrp": sub10EthLclStatusEntryGrp,
       "sub10EthRmtStatusEntryGrp": sub10EthRmtStatusEntryGrp,
       "sub10EthMgmtPhyEntryGrp": sub10EthMgmtPhyEntryGrp,
       "sub10EthMgmtVlanGrp": sub10EthMgmtVlanGrp,
       "sub10EthMgmtVlanAllowedEntryGrp": sub10EthMgmtVlanAllowedEntryGrp,
       "sub10EthMgmtQoSGrp": sub10EthMgmtQoSGrp,
       "sub10EthMgmtQoSQEntryGrp": sub10EthMgmtQoSQEntryGrp,
       "sub10EthMgmtQoSVlanEntryGrp": sub10EthMgmtQoSVlanEntryGrp,
       "sub10EthMgmtQoSPCPEntryGrp": sub10EthMgmtQoSPCPEntryGrp,
       "sub10EthMgmtQoSDSCPEntryGrp": sub10EthMgmtQoSDSCPEntryGrp,
       "sub10EthMgmtQoSMPLSEntryGrp": sub10EthMgmtQoSMPLSEntryGrp,
       "sub10EthMgmtStatsActiveEntryGrp": sub10EthMgmtStatsActiveEntryGrp,
       "sub10EthernetStatsGrp": sub10EthernetStatsGrp,
       "sub10EthernetStatsCurrEntryGrp": sub10EthernetStatsCurrEntryGrp,
       "sub10EthernetStats15mHistoryGrp": sub10EthernetStats15mHistoryGrp,
       "sub10EthStats15mHistEntryGrp": sub10EthStats15mHistEntryGrp,
       "sub10EthStats1dHistoryGrp": sub10EthStats1dHistoryGrp,
       "sub10EthStats1dHistEntryGrp": sub10EthStats1dHistEntryGrp,
       "sub10RadioLocalStatusGrp": sub10RadioLocalStatusGrp,
       "sub10RadioRemoteStatusGrp": sub10RadioRemoteStatusGrp,
       "sub10RadioMgmtGrp": sub10RadioMgmtGrp,
       "sub10RadioMgmtStatsGrp": sub10RadioMgmtStatsGrp,
       "sub10RadioMgmtStatsActiveEntryGrp": sub10RadioMgmtStatsActiveEntryGrp,
       "sub10RadioStatsGrp": sub10RadioStatsGrp,
       "sub10RadioStatsCurrentGrp": sub10RadioStatsCurrentGrp,
       "sub10RadioStats1mHistoryGrp": sub10RadioStats1mHistoryGrp,
       "sub10RadioStats1mHistEntryGrp": sub10RadioStats1mHistEntryGrp,
       "sub10RadioStats15mHistoryGrp": sub10RadioStats15mHistoryGrp,
       "sub10RadioStats15mHistEntryGrp": sub10RadioStats15mHistEntryGrp,
       "sub10RadioStats1dHistoryGrp": sub10RadioStats1dHistoryGrp,
       "sub10RadioStats1dHistEntryGrp": sub10RadioStats1dHistEntryGrp}
)
