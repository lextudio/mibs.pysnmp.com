# SNMP MIB module (CERENT-MSDWDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CERENT-MSDWDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:27 2024
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

(cerentGeneric,
 cerentModules,
 cerentRequirements) = mibBuilder.importSymbols(
    "CERENT-GLOBAL-REGISTRY",
    "cerentGeneric",
    "cerentModules",
    "cerentRequirements")

(CerentPeriod,) = mibBuilder.importSymbols(
    "CERENT-TC",
    "CerentPeriod")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cerentMsDwdmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 10, 80)
)
cerentMsDwdmMIB.setRevisions(
        ("1903-02-15 00:00",
         "1902-11-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ProtocolType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
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
        *(("eightGfc", 16),
          ("fastEthernet", 14),
          ("fddi", 15),
          ("fibreChOrOneGigEth", 5),
          ("oc768", 17),
          ("other", 1),
          ("otn", 18),
          ("sdh", 9),
          ("sonet", 8),
          ("sysplexIscCompatibility", 10),
          ("sysplexIscPeer", 11),
          ("sysplexTimerClo", 13),
          ("sysplexTimerEtr", 12),
          ("tenGigEth", 4),
          ("unframed", 7),
          ("unknown", 2))
    )



class IntervalType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMin", 1),
          ("oneDay", 2))
    )



class LocationAndIntervalType(Integer32, TextualConvention):
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
        *(("farEnd15Min", 3),
          ("farEndOneDay", 4),
          ("nearEnd15Min", 1),
          ("nearEndOneDay", 2))
    )



class MonitorType(Integer32, TextualConvention):
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
        *(("path", 1),
          ("section", 2),
          ("tcm1", 3),
          ("tcm2", 4))
    )



class RingDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eastWest", 2),
          ("westEast", 1))
    )



class SideIdentifier(Integer32, TextualConvention):
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
        *(("sideA", 1),
          ("sideB", 2),
          ("sideC", 3),
          ("sideD", 4),
          ("sideE", 5),
          ("sideF", 6),
          ("sideG", 7),
          ("sideH", 8),
          ("sideI", 9),
          ("sideJ", 10),
          ("sideK", 11),
          ("sideL", 12),
          ("sideM", 13),
          ("sideN", 14),
          ("sideO", 15),
          ("sideP", 16),
          ("sideQ", 17),
          ("sideR", 18),
          ("sideS", 19),
          ("sideT", 20),
          ("unknownSide", 0))
    )



class OpticalPortRule(Integer32, TextualConvention):
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("ad", 22),
          ("add", 11),
          ("com", 20),
          ("drop", 12),
          ("ead", 21),
          ("inputCom", 3),
          ("inputDc", 7),
          ("inputExpress", 9),
          ("inputLine", 1),
          ("inputOsc", 5),
          ("inputPassThru", 13),
          ("inputProtected", 16),
          ("inputRaman", 18),
          ("inputWorking", 14),
          ("outputCom", 4),
          ("outputDc", 8),
          ("outputExpress", 10),
          ("outputLine", 2),
          ("outputOsc", 6),
          ("outputProtected", 17),
          ("outputRaman", 19),
          ("outputWorking", 15))
    )



class LaserStatus(Integer32, TextualConvention):
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
        *(("apr", 3),
          ("none", 4),
          ("off", 2),
          ("on", 1))
    )



class OpticalAmplifierMode(Integer32, TextualConvention):
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
        *(("fixed-gain", 4),
          ("gain", 1),
          ("none", 3),
          ("power", 2))
    )



class OpticalBand(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              25,
              45,
              65,
              85,
              105,
              125,
              145)
        )
    )
    namedValues = NamedValues(
        *(("bn1530d33To1532d68", 5),
          ("bn1534d25To1536d61", 25),
          ("bn1538d19To1540d56", 45),
          ("bn1542d14To1544d53", 65),
          ("bn1546d12To1548d51", 85),
          ("bn1550d12To1552d52", 105),
          ("bn1554d13To1556d55", 125),
          ("bn1558d17To1560d61", 145),
          ("unknown", 1))
    )



class OpticalWavelength(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              7,
              10,
              12,
              15,
              17,
              20,
              22,
              23,
              24,
              25,
              27,
              30,
              32,
              35,
              37,
              40,
              42,
              43,
              44,
              45,
              47,
              50,
              52,
              55,
              57,
              60,
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
              87,
              90,
              92,
              95,
              97,
              100,
              102,
              103,
              104,
              105,
              107,
              110,
              112,
              115,
              117,
              120,
              122,
              123,
              124,
              125,
              127,
              130,
              132,
              135,
              137,
              140,
              142,
              143,
              144,
              145,
              147,
              150,
              152,
              155,
              157,
              160,
              162,
              164,
              166,
              168,
              170,
              172,
              174,
              176,
              178,
              180,
              182,
              184,
              186,
              188,
              190,
              192,
              194,
              196,
              198,
              200,
              205,
              210,
              215,
              220,
              225,
              230,
              235,
              240,
              245,
              250,
              255,
              260,
              265,
              270,
              275,
              280,
              285,
              290,
              295,
              300,
              305,
              310,
              315,
              320,
              325,
              330,
              335,
              340,
              345,
              350,
              355,
              360,
              365,
              370,
              375,
              380,
              385,
              390,
              395,
              400,
              405,
              410,
              415,
              420,
              425,
              430,
              435,
              440,
              445,
              450,
              455,
              460,
              465,
              470,
              475,
              480,
              485,
              490,
              500,
              505,
              510,
              515,
              520,
              530,
              540)
        )
    )
    namedValues = NamedValues(
        *(("firsttunablewv", 530),
          ("unknown", 1),
          ("wv1310", 73),
          ("wv1470", 66),
          ("wv1490", 76),
          ("wv1510", 68),
          ("wv1528d77", 540),
          ("wv1529d55", 3),
          ("wv1529d94", 4),
          ("wv1530", 78),
          ("wv1530d33", 5),
          ("wv1530d72", 7),
          ("wv1531d12", 10),
          ("wv1531d51", 12),
          ("wv1531d90", 15),
          ("wv1532d29", 17),
          ("wv1532d68", 20),
          ("wv1533d07", 22),
          ("wv1533d47", 23),
          ("wv1533d86", 24),
          ("wv1534d25", 25),
          ("wv1534d64", 27),
          ("wv1535d04", 30),
          ("wv1535d43", 32),
          ("wv1535d82", 35),
          ("wv1536d22", 37),
          ("wv1536d61", 40),
          ("wv1537d00", 42),
          ("wv1537d40", 43),
          ("wv1537d79", 44),
          ("wv1538d19", 45),
          ("wv1538d58", 47),
          ("wv1538d98", 50),
          ("wv1539d37", 52),
          ("wv1539d77", 55),
          ("wv1540d16", 57),
          ("wv1540d56", 60),
          ("wv1540d95", 62),
          ("wv1541d35", 63),
          ("wv1541d75", 64),
          ("wv1542d14", 65),
          ("wv1542d54", 67),
          ("wv1542d94", 70),
          ("wv1543d33", 72),
          ("wv1543d73", 75),
          ("wv1544d13", 77),
          ("wv1544d53", 80),
          ("wv1544d92", 82),
          ("wv1545d32", 83),
          ("wv1545d72", 84),
          ("wv1546d12", 85),
          ("wv1546d52", 87),
          ("wv1546d92", 90),
          ("wv1547d32", 92),
          ("wv1547d72", 95),
          ("wv1548d11", 97),
          ("wv1548d51", 100),
          ("wv1548d91", 102),
          ("wv1549d32", 103),
          ("wv1549d72", 104),
          ("wv1550", 74),
          ("wv1550d12", 105),
          ("wv1550d52", 107),
          ("wv1550d92", 110),
          ("wv1551d32", 112),
          ("wv1551d72", 115),
          ("wv1552d12", 117),
          ("wv1552d52", 120),
          ("wv1552d93", 122),
          ("wv1553d33", 123),
          ("wv1553d73", 124),
          ("wv1554d13", 125),
          ("wv1554d54", 127),
          ("wv1554d94", 130),
          ("wv1555d34", 132),
          ("wv1555d75", 135),
          ("wv1556d15", 137),
          ("wv1556d55", 140),
          ("wv1556d96", 142),
          ("wv1557d36", 143),
          ("wv1557d77", 144),
          ("wv1558d17", 145),
          ("wv1558d58", 147),
          ("wv1558d98", 150),
          ("wv1559d39", 152),
          ("wv1559d79", 155),
          ("wv1560d20", 157),
          ("wv1560d61", 160),
          ("wv1561d01", 162),
          ("wv1561d42", 164),
          ("wv1561d83", 166),
          ("wv1570", 79),
          ("wv1570d83", 168),
          ("wv1571d24", 170),
          ("wv1571d65", 172),
          ("wv1572d06", 174),
          ("wv1572d48", 176),
          ("wv1572d89", 178),
          ("wv1573d30", 180),
          ("wv1573d71", 182),
          ("wv1574d13", 184),
          ("wv1574d54", 186),
          ("wv1574d95", 188),
          ("wv1575d37", 190),
          ("wv1575d78", 192),
          ("wv1576d20", 194),
          ("wv1576d61", 196),
          ("wv1577d03", 198),
          ("wv1577d44", 200),
          ("wv1577d86", 205),
          ("wv1578d27", 210),
          ("wv1578d69", 215),
          ("wv1579d10", 220),
          ("wv1579d52", 225),
          ("wv1579d93", 230),
          ("wv1580d35", 235),
          ("wv1580d77", 240),
          ("wv1581d18", 245),
          ("wv1581d60", 250),
          ("wv1582d02", 255),
          ("wv1582d44", 260),
          ("wv1582d85", 265),
          ("wv1583d27", 270),
          ("wv1583d69", 275),
          ("wv1584d11", 280),
          ("wv1584d53", 285),
          ("wv1584d95", 290),
          ("wv1585d36", 295),
          ("wv1585d78", 300),
          ("wv1586d20", 305),
          ("wv1586d62", 310),
          ("wv1587d04", 315),
          ("wv1587d46", 320),
          ("wv1587d88", 325),
          ("wv1588d30", 330),
          ("wv1588d73", 335),
          ("wv1589d15", 340),
          ("wv1589d57", 345),
          ("wv1589d99", 350),
          ("wv1590", 69),
          ("wv1590d41", 355),
          ("wv1590d83", 360),
          ("wv1591d26", 365),
          ("wv1591d68", 370),
          ("wv1592d10", 375),
          ("wv1592d52", 380),
          ("wv1592d95", 385),
          ("wv1593d37", 390),
          ("wv1593d79", 395),
          ("wv1594d22", 400),
          ("wv1594d64", 405),
          ("wv1595d06", 410),
          ("wv1595d49", 415),
          ("wv1595d91", 420),
          ("wv1596d34", 425),
          ("wv1596d76", 430),
          ("wv1597d19", 435),
          ("wv1597d62", 440),
          ("wv1598d04", 445),
          ("wv1598d47", 450),
          ("wv1598d89", 455),
          ("wv1599d32", 460),
          ("wv1599d75", 465),
          ("wv1600d17", 470),
          ("wv1600d60", 475),
          ("wv1601d03", 480),
          ("wv1601d46", 485),
          ("wv1601d88", 490),
          ("wv1602d31", 500),
          ("wv1602d74", 505),
          ("wv1603d17", 510),
          ("wv1603d60", 515),
          ("wv1604d03", 520),
          ("wv1610", 81),
          ("wv850", 71))
    )



class OpticalPowerInDbm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 250),
        ValueRangeConstraint(-1000, -1000),
    )



class OpticalAttenInDb(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )



class TDCUCompensation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
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
              30)
        )
    )
    namedValues = NamedValues(
        *(("psnm0", 0),
          ("psnmCoarseMinus110", 16),
          ("psnmCoarseMinus1100", 25),
          ("psnmCoarseMinus1210", 26),
          ("psnmCoarseMinus1320", 27),
          ("psnmCoarseMinus1430", 28),
          ("psnmCoarseMinus1540", 29),
          ("psnmCoarseMinus1650", 30),
          ("psnmCoarseMinus220", 17),
          ("psnmCoarseMinus330", 18),
          ("psnmCoarseMinus440", 19),
          ("psnmCoarseMinus550", 20),
          ("psnmCoarseMinus660", 21),
          ("psnmCoarseMinus770", 22),
          ("psnmCoarseMinus880", 23),
          ("psnmCoarseMinus990", 24),
          ("psnmFineMinus135", 3),
          ("psnmFineMinus180", 4),
          ("psnmFineMinus225", 5),
          ("psnmFineMinus270", 6),
          ("psnmFineMinus315", 7),
          ("psnmFineMinus360", 8),
          ("psnmFineMinus405", 9),
          ("psnmFineMinus45", 1),
          ("psnmFineMinus450", 10),
          ("psnmFineMinus495", 11),
          ("psnmFineMinus540", 12),
          ("psnmFineMinus585", 13),
          ("psnmFineMinus630", 14),
          ("psnmFineMinus675", 15),
          ("psnmFineMinus90", 2),
          ("psnmNotApplicable", -1))
    )



# MIB Managed Objects in the order of their OIDs

_CerentMsDwdmMIBObjects_ObjectIdentity = ObjectIdentity
cerentMsDwdmMIBObjects = _CerentMsDwdmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40)
)
_CerentMsDwdmIf_ObjectIdentity = ObjectIdentity
cerentMsDwdmIf = _CerentMsDwdmIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1)
)
_CMsDwdmIfConfigTable_Object = MibTable
cMsDwdmIfConfigTable = _CMsDwdmIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 1)
)
if mibBuilder.loadTexts:
    cMsDwdmIfConfigTable.setStatus("current")
_CMsDwdmIfConfigEntry_Object = MibTableRow
cMsDwdmIfConfigEntry = _CMsDwdmIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 1, 1)
)
cMsDwdmIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cMsDwdmIfConfigEntry.setStatus("current")
_CMsDwdmIfConfigProtocol_Type = ProtocolType
_CMsDwdmIfConfigProtocol_Object = MibTableColumn
cMsDwdmIfConfigProtocol = _CMsDwdmIfConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 1, 1, 1),
    _CMsDwdmIfConfigProtocol_Type()
)
cMsDwdmIfConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfConfigProtocol.setStatus("current")


class _CMsDwdmIfConfigDataRate_Type(Integer32):
    """Custom type cMsDwdmIfConfigDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              50,
              55,
              60,
              70,
              80,
              90,
              100,
              110,
              120,
              130,
              140,
              150,
              160,
              170,
              180,
              190,
              200,
              210,
              220,
              230,
              240,
              250,
              280,
              290,
              300,
              310,
              320,
              330,
              340,
              350,
              360,
              370,
              380,
              390)
        )
    )
    namedValues = NamedValues(
        *(("dv6000", 120),
          ("e1t1", 300),
          ("e3t3", 310),
          ("eightGfc", 330),
          ("escon", 110),
          ("etrClo", 250),
          ("fc", 80),
          ("fe", 290),
          ("fourGfcFicon", 190),
          ("gigE", 60),
          ("hdtv", 140),
          ("infiniBand", 280),
          ("isc1", 210),
          ("isc3", 220),
          ("oc12", 160),
          ("oc192", 180),
          ("oc3", 150),
          ("oc3Ge", 320),
          ("oc48", 170),
          ("oc768", 340),
          ("oneGfcFicon", 90),
          ("oneGigIsc3", 230),
          ("oneHundredGe", 390),
          ("otu1", 350),
          ("otu2", 360),
          ("otu3", 370),
          ("otu4", 380),
          ("passThru", 10),
          ("sdiD1Video", 130),
          ("stm1", 20),
          ("stm16", 40),
          ("stm256", 55),
          ("stm4", 30),
          ("stm64", 50),
          ("tenGfc", 200),
          ("tenGigE", 70),
          ("twoGfcFiconIsc3", 100),
          ("twoGigIsc3", 240))
    )


_CMsDwdmIfConfigDataRate_Type.__name__ = "Integer32"
_CMsDwdmIfConfigDataRate_Object = MibTableColumn
cMsDwdmIfConfigDataRate = _CMsDwdmIfConfigDataRate_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 1, 1, 2),
    _CMsDwdmIfConfigDataRate_Type()
)
cMsDwdmIfConfigDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfConfigDataRate.setStatus("current")


class _CMsDwdmIfConfigLoopback_Type(Integer32):
    """Custom type cMsDwdmIfConfigLoopback based on Integer32"""
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
        *(("diagnosticLoop", 2),
          ("lineLoop", 3),
          ("noLoop", 1),
          ("otherLoop", 4))
    )


_CMsDwdmIfConfigLoopback_Type.__name__ = "Integer32"
_CMsDwdmIfConfigLoopback_Object = MibTableColumn
cMsDwdmIfConfigLoopback = _CMsDwdmIfConfigLoopback_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 1, 1, 3),
    _CMsDwdmIfConfigLoopback_Type()
)
cMsDwdmIfConfigLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfConfigLoopback.setStatus("current")
_CMsDwdmIfConfigWavelength_Type = OpticalWavelength
_CMsDwdmIfConfigWavelength_Object = MibTableColumn
cMsDwdmIfConfigWavelength = _CMsDwdmIfConfigWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 1, 1, 4),
    _CMsDwdmIfConfigWavelength_Type()
)
cMsDwdmIfConfigWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfConfigWavelength.setStatus("current")
_CMsDwdmIfConfigOtnStatus_Type = TruthValue
_CMsDwdmIfConfigOtnStatus_Object = MibTableColumn
cMsDwdmIfConfigOtnStatus = _CMsDwdmIfConfigOtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 1, 1, 5),
    _CMsDwdmIfConfigOtnStatus_Type()
)
cMsDwdmIfConfigOtnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfConfigOtnStatus.setStatus("current")
_CMsDwdmIfConfigFECStatus_Type = TruthValue
_CMsDwdmIfConfigFECStatus_Object = MibTableColumn
cMsDwdmIfConfigFECStatus = _CMsDwdmIfConfigFECStatus_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 1, 1, 6),
    _CMsDwdmIfConfigFECStatus_Type()
)
cMsDwdmIfConfigFECStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfConfigFECStatus.setStatus("current")


class _CMsDwdmIfOpticsValidIntervals_Type(Unsigned32):
    """Custom type cMsDwdmIfOpticsValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CMsDwdmIfOpticsValidIntervals_Type.__name__ = "Unsigned32"
_CMsDwdmIfOpticsValidIntervals_Object = MibTableColumn
cMsDwdmIfOpticsValidIntervals = _CMsDwdmIfOpticsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 1, 1, 7),
    _CMsDwdmIfOpticsValidIntervals_Type()
)
cMsDwdmIfOpticsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfOpticsValidIntervals.setStatus("current")


class _CMsDwdmIfOTNValidIntervals_Type(Unsigned32):
    """Custom type cMsDwdmIfOTNValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CMsDwdmIfOTNValidIntervals_Type.__name__ = "Unsigned32"
_CMsDwdmIfOTNValidIntervals_Object = MibTableColumn
cMsDwdmIfOTNValidIntervals = _CMsDwdmIfOTNValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 1, 1, 8),
    _CMsDwdmIfOTNValidIntervals_Type()
)
cMsDwdmIfOTNValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfOTNValidIntervals.setStatus("current")


class _CMsDwdmIfFECValidIntervals_Type(Unsigned32):
    """Custom type cMsDwdmIfFECValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CMsDwdmIfFECValidIntervals_Type.__name__ = "Unsigned32"
_CMsDwdmIfFECValidIntervals_Object = MibTableColumn
cMsDwdmIfFECValidIntervals = _CMsDwdmIfFECValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 1, 1, 9),
    _CMsDwdmIfFECValidIntervals_Type()
)
cMsDwdmIfFECValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfFECValidIntervals.setStatus("current")


class _CMsDwdmIfConfigFECMode_Type(Integer32):
    """Custom type cMsDwdmIfConfigFECMode based on Integer32"""
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
        *(("disable", 1),
          ("enableEnhanced", 3),
          ("enableEnhanced20", 6),
          ("enableEnhancedI4", 4),
          ("enableEnhancedI7", 5),
          ("enableHG7", 7),
          ("enableStandard", 2))
    )


_CMsDwdmIfConfigFECMode_Type.__name__ = "Integer32"
_CMsDwdmIfConfigFECMode_Object = MibTableColumn
cMsDwdmIfConfigFECMode = _CMsDwdmIfConfigFECMode_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 1, 1, 10),
    _CMsDwdmIfConfigFECMode_Type()
)
cMsDwdmIfConfigFECMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfConfigFECMode.setStatus("current")
_CMsDwdmIfTransportTable_Object = MibTable
cMsDwdmIfTransportTable = _CMsDwdmIfTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2)
)
if mibBuilder.loadTexts:
    cMsDwdmIfTransportTable.setStatus("current")
_CMsDwdmIfTransportEntry_Object = MibTableRow
cMsDwdmIfTransportEntry = _CMsDwdmIfTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1)
)
cMsDwdmIfTransportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cMsDwdmIfTransportEntry.setStatus("current")
_CMsDwdmIfTransportRingDirection_Type = RingDirection
_CMsDwdmIfTransportRingDirection_Object = MibTableColumn
cMsDwdmIfTransportRingDirection = _CMsDwdmIfTransportRingDirection_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 1),
    _CMsDwdmIfTransportRingDirection_Type()
)
cMsDwdmIfTransportRingDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportRingDirection.setStatus("obsolete")
_CMsDwdmIfTransportPortRule_Type = OpticalPortRule
_CMsDwdmIfTransportPortRule_Object = MibTableColumn
cMsDwdmIfTransportPortRule = _CMsDwdmIfTransportPortRule_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 2),
    _CMsDwdmIfTransportPortRule_Type()
)
cMsDwdmIfTransportPortRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportPortRule.setStatus("current")
_CMsDwdmIfTransportPower_Type = OpticalPowerInDbm
_CMsDwdmIfTransportPower_Object = MibTableColumn
cMsDwdmIfTransportPower = _CMsDwdmIfTransportPower_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 3),
    _CMsDwdmIfTransportPower_Type()
)
cMsDwdmIfTransportPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportPower.setStatus("current")
_CMsDwdmIfTransportReferencePower_Type = OpticalPowerInDbm
_CMsDwdmIfTransportReferencePower_Object = MibTableColumn
cMsDwdmIfTransportReferencePower = _CMsDwdmIfTransportReferencePower_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 4),
    _CMsDwdmIfTransportReferencePower_Type()
)
cMsDwdmIfTransportReferencePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportReferencePower.setStatus("current")


class _CMsDwdmIfTransportCalibratedPower_Type(OpticalPowerInDbm):
    """Custom type cMsDwdmIfTransportCalibratedPower based on OpticalPowerInDbm"""
    defaultValue = 0


_CMsDwdmIfTransportCalibratedPower_Object = MibTableColumn
cMsDwdmIfTransportCalibratedPower = _CMsDwdmIfTransportCalibratedPower_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 5),
    _CMsDwdmIfTransportCalibratedPower_Type()
)
cMsDwdmIfTransportCalibratedPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportCalibratedPower.setStatus("current")
_CMsDwdmIfTransportInsertionLoss_Type = OpticalAttenInDb
_CMsDwdmIfTransportInsertionLoss_Object = MibTableColumn
cMsDwdmIfTransportInsertionLoss = _CMsDwdmIfTransportInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 6),
    _CMsDwdmIfTransportInsertionLoss_Type()
)
cMsDwdmIfTransportInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportInsertionLoss.setStatus("current")
_CMsDwdmIfTransportLaserStatus_Type = LaserStatus
_CMsDwdmIfTransportLaserStatus_Object = MibTableColumn
cMsDwdmIfTransportLaserStatus = _CMsDwdmIfTransportLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 7),
    _CMsDwdmIfTransportLaserStatus_Type()
)
cMsDwdmIfTransportLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportLaserStatus.setStatus("current")
_CMsDwdmIfTransportAmplifierMode_Type = OpticalAmplifierMode
_CMsDwdmIfTransportAmplifierMode_Object = MibTableColumn
cMsDwdmIfTransportAmplifierMode = _CMsDwdmIfTransportAmplifierMode_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 8),
    _CMsDwdmIfTransportAmplifierMode_Type()
)
cMsDwdmIfTransportAmplifierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportAmplifierMode.setStatus("current")
_CMsDwdmIfTransportGain_Type = OpticalAttenInDb
_CMsDwdmIfTransportGain_Object = MibTableColumn
cMsDwdmIfTransportGain = _CMsDwdmIfTransportGain_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 9),
    _CMsDwdmIfTransportGain_Type()
)
cMsDwdmIfTransportGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportGain.setStatus("current")
_CMsDwdmIfTransportReferenceTilt_Type = OpticalAttenInDb
_CMsDwdmIfTransportReferenceTilt_Object = MibTableColumn
cMsDwdmIfTransportReferenceTilt = _CMsDwdmIfTransportReferenceTilt_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 10),
    _CMsDwdmIfTransportReferenceTilt_Type()
)
cMsDwdmIfTransportReferenceTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportReferenceTilt.setStatus("current")


class _CMsDwdmIfTransportCalibratedTilt_Type(OpticalAttenInDb):
    """Custom type cMsDwdmIfTransportCalibratedTilt based on OpticalAttenInDb"""
    defaultValue = 0


_CMsDwdmIfTransportCalibratedTilt_Object = MibTableColumn
cMsDwdmIfTransportCalibratedTilt = _CMsDwdmIfTransportCalibratedTilt_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 11),
    _CMsDwdmIfTransportCalibratedTilt_Type()
)
cMsDwdmIfTransportCalibratedTilt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportCalibratedTilt.setStatus("current")
_CMsDwdmIfTransportDCULoss_Type = OpticalAttenInDb
_CMsDwdmIfTransportDCULoss_Object = MibTableColumn
cMsDwdmIfTransportDCULoss = _CMsDwdmIfTransportDCULoss_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 12),
    _CMsDwdmIfTransportDCULoss_Type()
)
cMsDwdmIfTransportDCULoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportDCULoss.setStatus("current")


class _CMsDwdmIfTransportOSRI_Type(Integer32):
    """Custom type cMsDwdmIfTransportOSRI based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("none", 3))
    )


_CMsDwdmIfTransportOSRI_Type.__name__ = "Integer32"
_CMsDwdmIfTransportOSRI_Object = MibTableColumn
cMsDwdmIfTransportOSRI = _CMsDwdmIfTransportOSRI_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 13),
    _CMsDwdmIfTransportOSRI_Type()
)
cMsDwdmIfTransportOSRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportOSRI.setStatus("current")
_CMsDwdmIfTransportExpectedGain_Type = OpticalAttenInDb
_CMsDwdmIfTransportExpectedGain_Object = MibTableColumn
cMsDwdmIfTransportExpectedGain = _CMsDwdmIfTransportExpectedGain_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 14),
    _CMsDwdmIfTransportExpectedGain_Type()
)
cMsDwdmIfTransportExpectedGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportExpectedGain.setStatus("current")
_CMsDwdmIfTransportSideIdentifier_Type = SideIdentifier
_CMsDwdmIfTransportSideIdentifier_Object = MibTableColumn
cMsDwdmIfTransportSideIdentifier = _CMsDwdmIfTransportSideIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 15),
    _CMsDwdmIfTransportSideIdentifier_Type()
)
cMsDwdmIfTransportSideIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportSideIdentifier.setStatus("current")
_CMsDwdmIfTransportAddPower_Type = OpticalPowerInDbm
_CMsDwdmIfTransportAddPower_Object = MibTableColumn
cMsDwdmIfTransportAddPower = _CMsDwdmIfTransportAddPower_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 16),
    _CMsDwdmIfTransportAddPower_Type()
)
cMsDwdmIfTransportAddPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportAddPower.setStatus("current")
_CMsDwdmIfTransportOSCPower_Type = OpticalPowerInDbm
_CMsDwdmIfTransportOSCPower_Object = MibTableColumn
cMsDwdmIfTransportOSCPower = _CMsDwdmIfTransportOSCPower_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 17),
    _CMsDwdmIfTransportOSCPower_Type()
)
cMsDwdmIfTransportOSCPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportOSCPower.setStatus("current")
_CMsDwdmIfTransportTDCUCompensation_Type = TDCUCompensation
_CMsDwdmIfTransportTDCUCompensation_Object = MibTableColumn
cMsDwdmIfTransportTDCUCompensation = _CMsDwdmIfTransportTDCUCompensation_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 2, 1, 18),
    _CMsDwdmIfTransportTDCUCompensation_Type()
)
cMsDwdmIfTransportTDCUCompensation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfTransportTDCUCompensation.setStatus("current")
_CMsDwdmIfMultiplexSectionTable_Object = MibTable
cMsDwdmIfMultiplexSectionTable = _CMsDwdmIfMultiplexSectionTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 3)
)
if mibBuilder.loadTexts:
    cMsDwdmIfMultiplexSectionTable.setStatus("current")
_CMsDwdmIfMultiplexSectionEntry_Object = MibTableRow
cMsDwdmIfMultiplexSectionEntry = _CMsDwdmIfMultiplexSectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 3, 1)
)
cMsDwdmIfMultiplexSectionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cMsDwdmIfMultiplexSectionEntry.setStatus("current")
_CMsDwdmIfMultiplexSectionRingDirection_Type = RingDirection
_CMsDwdmIfMultiplexSectionRingDirection_Object = MibTableColumn
cMsDwdmIfMultiplexSectionRingDirection = _CMsDwdmIfMultiplexSectionRingDirection_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 3, 1, 1),
    _CMsDwdmIfMultiplexSectionRingDirection_Type()
)
cMsDwdmIfMultiplexSectionRingDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsDwdmIfMultiplexSectionRingDirection.setStatus("obsolete")
_CMsDwdmIfMultiplexSectionPortRule_Type = OpticalPortRule
_CMsDwdmIfMultiplexSectionPortRule_Object = MibTableColumn
cMsDwdmIfMultiplexSectionPortRule = _CMsDwdmIfMultiplexSectionPortRule_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 3, 1, 2),
    _CMsDwdmIfMultiplexSectionPortRule_Type()
)
cMsDwdmIfMultiplexSectionPortRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfMultiplexSectionPortRule.setStatus("current")
_CMsDwdmIfMultiplexSectionPower_Type = OpticalPowerInDbm
_CMsDwdmIfMultiplexSectionPower_Object = MibTableColumn
cMsDwdmIfMultiplexSectionPower = _CMsDwdmIfMultiplexSectionPower_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 3, 1, 3),
    _CMsDwdmIfMultiplexSectionPower_Type()
)
cMsDwdmIfMultiplexSectionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfMultiplexSectionPower.setStatus("current")
_CMsDwdmIfMultiplexSectionReferencePower_Type = OpticalPowerInDbm
_CMsDwdmIfMultiplexSectionReferencePower_Object = MibTableColumn
cMsDwdmIfMultiplexSectionReferencePower = _CMsDwdmIfMultiplexSectionReferencePower_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 3, 1, 4),
    _CMsDwdmIfMultiplexSectionReferencePower_Type()
)
cMsDwdmIfMultiplexSectionReferencePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfMultiplexSectionReferencePower.setStatus("current")


class _CMsDwdmIfMultiplexSectionCalibratedPower_Type(OpticalPowerInDbm):
    """Custom type cMsDwdmIfMultiplexSectionCalibratedPower based on OpticalPowerInDbm"""
    defaultValue = 0


_CMsDwdmIfMultiplexSectionCalibratedPower_Object = MibTableColumn
cMsDwdmIfMultiplexSectionCalibratedPower = _CMsDwdmIfMultiplexSectionCalibratedPower_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 3, 1, 5),
    _CMsDwdmIfMultiplexSectionCalibratedPower_Type()
)
cMsDwdmIfMultiplexSectionCalibratedPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfMultiplexSectionCalibratedPower.setStatus("current")
_CMsDwdmIfMultiplexSectionInsertionLoss_Type = OpticalAttenInDb
_CMsDwdmIfMultiplexSectionInsertionLoss_Object = MibTableColumn
cMsDwdmIfMultiplexSectionInsertionLoss = _CMsDwdmIfMultiplexSectionInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 3, 1, 6),
    _CMsDwdmIfMultiplexSectionInsertionLoss_Type()
)
cMsDwdmIfMultiplexSectionInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfMultiplexSectionInsertionLoss.setStatus("current")
_CMsDwdmIfMultiplexSectionActualBand_Type = OpticalBand
_CMsDwdmIfMultiplexSectionActualBand_Object = MibTableColumn
cMsDwdmIfMultiplexSectionActualBand = _CMsDwdmIfMultiplexSectionActualBand_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 3, 1, 7),
    _CMsDwdmIfMultiplexSectionActualBand_Type()
)
cMsDwdmIfMultiplexSectionActualBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfMultiplexSectionActualBand.setStatus("current")
_CMsDwdmIfMultiplexSectionExpectedBand_Type = OpticalBand
_CMsDwdmIfMultiplexSectionExpectedBand_Object = MibTableColumn
cMsDwdmIfMultiplexSectionExpectedBand = _CMsDwdmIfMultiplexSectionExpectedBand_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 3, 1, 8),
    _CMsDwdmIfMultiplexSectionExpectedBand_Type()
)
cMsDwdmIfMultiplexSectionExpectedBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfMultiplexSectionExpectedBand.setStatus("current")
_CMsDwdmIfMultiplexSectionSideIdentifier_Type = SideIdentifier
_CMsDwdmIfMultiplexSectionSideIdentifier_Object = MibTableColumn
cMsDwdmIfMultiplexSectionSideIdentifier = _CMsDwdmIfMultiplexSectionSideIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 3, 1, 9),
    _CMsDwdmIfMultiplexSectionSideIdentifier_Type()
)
cMsDwdmIfMultiplexSectionSideIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfMultiplexSectionSideIdentifier.setStatus("current")
_CMsDwdmIfChannelTable_Object = MibTable
cMsDwdmIfChannelTable = _CMsDwdmIfChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 4)
)
if mibBuilder.loadTexts:
    cMsDwdmIfChannelTable.setStatus("current")
_CMsDwdmIfChannelEntry_Object = MibTableRow
cMsDwdmIfChannelEntry = _CMsDwdmIfChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 4, 1)
)
cMsDwdmIfChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cMsDwdmIfChannelEntry.setStatus("current")
_CMsDwdmIfChannelRingDirection_Type = RingDirection
_CMsDwdmIfChannelRingDirection_Object = MibTableColumn
cMsDwdmIfChannelRingDirection = _CMsDwdmIfChannelRingDirection_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 4, 1, 1),
    _CMsDwdmIfChannelRingDirection_Type()
)
cMsDwdmIfChannelRingDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsDwdmIfChannelRingDirection.setStatus("obsolete")
_CMsDwdmIfChannelPortRule_Type = OpticalPortRule
_CMsDwdmIfChannelPortRule_Object = MibTableColumn
cMsDwdmIfChannelPortRule = _CMsDwdmIfChannelPortRule_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 4, 1, 2),
    _CMsDwdmIfChannelPortRule_Type()
)
cMsDwdmIfChannelPortRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfChannelPortRule.setStatus("current")
_CMsDwdmIfChannelPower_Type = OpticalPowerInDbm
_CMsDwdmIfChannelPower_Object = MibTableColumn
cMsDwdmIfChannelPower = _CMsDwdmIfChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 4, 1, 3),
    _CMsDwdmIfChannelPower_Type()
)
cMsDwdmIfChannelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfChannelPower.setStatus("current")
_CMsDwdmIfChannelReferencePower_Type = OpticalPowerInDbm
_CMsDwdmIfChannelReferencePower_Object = MibTableColumn
cMsDwdmIfChannelReferencePower = _CMsDwdmIfChannelReferencePower_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 4, 1, 4),
    _CMsDwdmIfChannelReferencePower_Type()
)
cMsDwdmIfChannelReferencePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfChannelReferencePower.setStatus("current")


class _CMsDwdmIfChannelCalibratedPower_Type(OpticalPowerInDbm):
    """Custom type cMsDwdmIfChannelCalibratedPower based on OpticalPowerInDbm"""
    defaultValue = 0


_CMsDwdmIfChannelCalibratedPower_Object = MibTableColumn
cMsDwdmIfChannelCalibratedPower = _CMsDwdmIfChannelCalibratedPower_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 4, 1, 5),
    _CMsDwdmIfChannelCalibratedPower_Type()
)
cMsDwdmIfChannelCalibratedPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfChannelCalibratedPower.setStatus("current")
_CMsDwdmIfChannelInsertionLoss_Type = OpticalAttenInDb
_CMsDwdmIfChannelInsertionLoss_Object = MibTableColumn
cMsDwdmIfChannelInsertionLoss = _CMsDwdmIfChannelInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 4, 1, 6),
    _CMsDwdmIfChannelInsertionLoss_Type()
)
cMsDwdmIfChannelInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfChannelInsertionLoss.setStatus("current")
_CMsDwdmIfChannelActualWavelength_Type = OpticalWavelength
_CMsDwdmIfChannelActualWavelength_Object = MibTableColumn
cMsDwdmIfChannelActualWavelength = _CMsDwdmIfChannelActualWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 4, 1, 7),
    _CMsDwdmIfChannelActualWavelength_Type()
)
cMsDwdmIfChannelActualWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfChannelActualWavelength.setStatus("current")
_CMsDwdmIfChannelExpectedWavelength_Type = OpticalWavelength
_CMsDwdmIfChannelExpectedWavelength_Object = MibTableColumn
cMsDwdmIfChannelExpectedWavelength = _CMsDwdmIfChannelExpectedWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 4, 1, 8),
    _CMsDwdmIfChannelExpectedWavelength_Type()
)
cMsDwdmIfChannelExpectedWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmIfChannelExpectedWavelength.setStatus("current")
_CMsDwdmIfChannelSideIdentifier_Type = SideIdentifier
_CMsDwdmIfChannelSideIdentifier_Object = MibTableColumn
cMsDwdmIfChannelSideIdentifier = _CMsDwdmIfChannelSideIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 1, 4, 1, 9),
    _CMsDwdmIfChannelSideIdentifier_Type()
)
cMsDwdmIfChannelSideIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmIfChannelSideIdentifier.setStatus("current")
_CerentMsDwdmOtn_ObjectIdentity = ObjectIdentity
cerentMsDwdmOtn = _CerentMsDwdmOtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2)
)
_CMsDwdmOtnThresholdsTable_Object = MibTable
cMsDwdmOtnThresholdsTable = _CMsDwdmOtnThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 1)
)
if mibBuilder.loadTexts:
    cMsDwdmOtnThresholdsTable.setStatus("current")
_CMsDwdmOtnThresholdsEntry_Object = MibTableRow
cMsDwdmOtnThresholdsEntry = _CMsDwdmOtnThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 1, 1)
)
cMsDwdmOtnThresholdsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERENT-MSDWDM-MIB", "cMsDwdmOtnThreshMonType"),
    (0, "CERENT-MSDWDM-MIB", "cMsDwdmOtnThreshIntervalType"),
)
if mibBuilder.loadTexts:
    cMsDwdmOtnThresholdsEntry.setStatus("current")
_CMsDwdmOtnThreshMonType_Type = MonitorType
_CMsDwdmOtnThreshMonType_Object = MibTableColumn
cMsDwdmOtnThreshMonType = _CMsDwdmOtnThreshMonType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 1, 1, 1),
    _CMsDwdmOtnThreshMonType_Type()
)
cMsDwdmOtnThreshMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsDwdmOtnThreshMonType.setStatus("current")
_CMsDwdmOtnThreshIntervalType_Type = LocationAndIntervalType
_CMsDwdmOtnThreshIntervalType_Object = MibTableColumn
cMsDwdmOtnThreshIntervalType = _CMsDwdmOtnThreshIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 1, 1, 2),
    _CMsDwdmOtnThreshIntervalType_Type()
)
cMsDwdmOtnThreshIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsDwdmOtnThreshIntervalType.setStatus("current")
_CMsDwdmOtnThreshFC_Type = Unsigned32
_CMsDwdmOtnThreshFC_Object = MibTableColumn
cMsDwdmOtnThreshFC = _CMsDwdmOtnThreshFC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 1, 1, 3),
    _CMsDwdmOtnThreshFC_Type()
)
cMsDwdmOtnThreshFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmOtnThreshFC.setStatus("current")
_CMsDwdmOtnThreshES_Type = Unsigned32
_CMsDwdmOtnThreshES_Object = MibTableColumn
cMsDwdmOtnThreshES = _CMsDwdmOtnThreshES_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 1, 1, 4),
    _CMsDwdmOtnThreshES_Type()
)
cMsDwdmOtnThreshES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmOtnThreshES.setStatus("current")
_CMsDwdmOtnThreshSES_Type = Unsigned32
_CMsDwdmOtnThreshSES_Object = MibTableColumn
cMsDwdmOtnThreshSES = _CMsDwdmOtnThreshSES_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 1, 1, 5),
    _CMsDwdmOtnThreshSES_Type()
)
cMsDwdmOtnThreshSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmOtnThreshSES.setStatus("current")
_CMsDwdmOtnThreshUAS_Type = Unsigned32
_CMsDwdmOtnThreshUAS_Object = MibTableColumn
cMsDwdmOtnThreshUAS = _CMsDwdmOtnThreshUAS_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 1, 1, 6),
    _CMsDwdmOtnThreshUAS_Type()
)
cMsDwdmOtnThreshUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmOtnThreshUAS.setStatus("current")
_CMsDwdmOtnThreshBBE_Type = Unsigned32
_CMsDwdmOtnThreshBBE_Object = MibTableColumn
cMsDwdmOtnThreshBBE = _CMsDwdmOtnThreshBBE_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 1, 1, 7),
    _CMsDwdmOtnThreshBBE_Type()
)
cMsDwdmOtnThreshBBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmOtnThreshBBE.setStatus("current")
_CMsDwdmOtnCurrentTable_Object = MibTable
cMsDwdmOtnCurrentTable = _CMsDwdmOtnCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 2)
)
if mibBuilder.loadTexts:
    cMsDwdmOtnCurrentTable.setStatus("current")
_CMsDwdmOtnCurrentEntry_Object = MibTableRow
cMsDwdmOtnCurrentEntry = _CMsDwdmOtnCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 2, 1)
)
cMsDwdmOtnCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERENT-MSDWDM-MIB", "cMsDwdmOtnCurrentMonType"),
    (0, "CERENT-MSDWDM-MIB", "cMsDwdmOtnCurIntervalType"),
)
if mibBuilder.loadTexts:
    cMsDwdmOtnCurrentEntry.setStatus("current")
_CMsDwdmOtnCurrentMonType_Type = MonitorType
_CMsDwdmOtnCurrentMonType_Object = MibTableColumn
cMsDwdmOtnCurrentMonType = _CMsDwdmOtnCurrentMonType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 2, 1, 1),
    _CMsDwdmOtnCurrentMonType_Type()
)
cMsDwdmOtnCurrentMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsDwdmOtnCurrentMonType.setStatus("current")
_CMsDwdmOtnCurIntervalType_Type = LocationAndIntervalType
_CMsDwdmOtnCurIntervalType_Object = MibTableColumn
cMsDwdmOtnCurIntervalType = _CMsDwdmOtnCurIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 2, 1, 2),
    _CMsDwdmOtnCurIntervalType_Type()
)
cMsDwdmOtnCurIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsDwdmOtnCurIntervalType.setStatus("current")
_CMsDwdmOtnCurrentFC_Type = Counter32
_CMsDwdmOtnCurrentFC_Object = MibTableColumn
cMsDwdmOtnCurrentFC = _CMsDwdmOtnCurrentFC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 2, 1, 3),
    _CMsDwdmOtnCurrentFC_Type()
)
cMsDwdmOtnCurrentFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnCurrentFC.setStatus("current")
_CMsDwdmOtnCurrentES_Type = Counter32
_CMsDwdmOtnCurrentES_Object = MibTableColumn
cMsDwdmOtnCurrentES = _CMsDwdmOtnCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 2, 1, 4),
    _CMsDwdmOtnCurrentES_Type()
)
cMsDwdmOtnCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnCurrentES.setStatus("current")
_CMsDwdmOtnCurrentSES_Type = Counter32
_CMsDwdmOtnCurrentSES_Object = MibTableColumn
cMsDwdmOtnCurrentSES = _CMsDwdmOtnCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 2, 1, 5),
    _CMsDwdmOtnCurrentSES_Type()
)
cMsDwdmOtnCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnCurrentSES.setStatus("current")
_CMsDwdmOtnCurrentUAS_Type = Counter32
_CMsDwdmOtnCurrentUAS_Object = MibTableColumn
cMsDwdmOtnCurrentUAS = _CMsDwdmOtnCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 2, 1, 6),
    _CMsDwdmOtnCurrentUAS_Type()
)
cMsDwdmOtnCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnCurrentUAS.setStatus("current")
_CMsDwdmOtnCurrentBBE_Type = Counter32
_CMsDwdmOtnCurrentBBE_Object = MibTableColumn
cMsDwdmOtnCurrentBBE = _CMsDwdmOtnCurrentBBE_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 2, 1, 7),
    _CMsDwdmOtnCurrentBBE_Type()
)
cMsDwdmOtnCurrentBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnCurrentBBE.setStatus("current")
_CMsDwdmOtnCurrentESR_Type = Counter32
_CMsDwdmOtnCurrentESR_Object = MibTableColumn
cMsDwdmOtnCurrentESR = _CMsDwdmOtnCurrentESR_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 2, 1, 8),
    _CMsDwdmOtnCurrentESR_Type()
)
cMsDwdmOtnCurrentESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnCurrentESR.setStatus("current")
_CMsDwdmOtnCurrentSESR_Type = Counter32
_CMsDwdmOtnCurrentSESR_Object = MibTableColumn
cMsDwdmOtnCurrentSESR = _CMsDwdmOtnCurrentSESR_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 2, 1, 9),
    _CMsDwdmOtnCurrentSESR_Type()
)
cMsDwdmOtnCurrentSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnCurrentSESR.setStatus("current")
_CMsDwdmOtnCurrentBBER_Type = Counter32
_CMsDwdmOtnCurrentBBER_Object = MibTableColumn
cMsDwdmOtnCurrentBBER = _CMsDwdmOtnCurrentBBER_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 2, 1, 10),
    _CMsDwdmOtnCurrentBBER_Type()
)
cMsDwdmOtnCurrentBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnCurrentBBER.setStatus("current")
_CMsDwdmOtnIntervalTable_Object = MibTable
cMsDwdmOtnIntervalTable = _CMsDwdmOtnIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 3)
)
if mibBuilder.loadTexts:
    cMsDwdmOtnIntervalTable.setStatus("current")
_CMsDwdmOtnIntervalEntry_Object = MibTableRow
cMsDwdmOtnIntervalEntry = _CMsDwdmOtnIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 3, 1)
)
cMsDwdmOtnIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERENT-MSDWDM-MIB", "cMsDwdmOtnIntervalMonType"),
    (0, "CERENT-MSDWDM-MIB", "cMsDwdmOtnIntervalType"),
    (0, "CERENT-MSDWDM-MIB", "cMsDwdmOtnIntervalNum"),
)
if mibBuilder.loadTexts:
    cMsDwdmOtnIntervalEntry.setStatus("current")
_CMsDwdmOtnIntervalMonType_Type = MonitorType
_CMsDwdmOtnIntervalMonType_Object = MibTableColumn
cMsDwdmOtnIntervalMonType = _CMsDwdmOtnIntervalMonType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 3, 1, 1),
    _CMsDwdmOtnIntervalMonType_Type()
)
cMsDwdmOtnIntervalMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsDwdmOtnIntervalMonType.setStatus("current")
_CMsDwdmOtnIntervalType_Type = LocationAndIntervalType
_CMsDwdmOtnIntervalType_Object = MibTableColumn
cMsDwdmOtnIntervalType = _CMsDwdmOtnIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 3, 1, 2),
    _CMsDwdmOtnIntervalType_Type()
)
cMsDwdmOtnIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsDwdmOtnIntervalType.setStatus("current")


class _CMsDwdmOtnIntervalNum_Type(Integer32):
    """Custom type cMsDwdmOtnIntervalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CMsDwdmOtnIntervalNum_Type.__name__ = "Integer32"
_CMsDwdmOtnIntervalNum_Object = MibTableColumn
cMsDwdmOtnIntervalNum = _CMsDwdmOtnIntervalNum_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 3, 1, 3),
    _CMsDwdmOtnIntervalNum_Type()
)
cMsDwdmOtnIntervalNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsDwdmOtnIntervalNum.setStatus("current")
_CMsDwdmOtnIntervalFC_Type = Counter32
_CMsDwdmOtnIntervalFC_Object = MibTableColumn
cMsDwdmOtnIntervalFC = _CMsDwdmOtnIntervalFC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 3, 1, 4),
    _CMsDwdmOtnIntervalFC_Type()
)
cMsDwdmOtnIntervalFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnIntervalFC.setStatus("current")
_CMsDwdmOtnIntervalES_Type = Counter32
_CMsDwdmOtnIntervalES_Object = MibTableColumn
cMsDwdmOtnIntervalES = _CMsDwdmOtnIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 3, 1, 5),
    _CMsDwdmOtnIntervalES_Type()
)
cMsDwdmOtnIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnIntervalES.setStatus("current")
_CMsDwdmOtnIntervalSES_Type = Counter32
_CMsDwdmOtnIntervalSES_Object = MibTableColumn
cMsDwdmOtnIntervalSES = _CMsDwdmOtnIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 3, 1, 6),
    _CMsDwdmOtnIntervalSES_Type()
)
cMsDwdmOtnIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnIntervalSES.setStatus("current")
_CMsDwdmOtnIntervalUAS_Type = Counter32
_CMsDwdmOtnIntervalUAS_Object = MibTableColumn
cMsDwdmOtnIntervalUAS = _CMsDwdmOtnIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 3, 1, 7),
    _CMsDwdmOtnIntervalUAS_Type()
)
cMsDwdmOtnIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnIntervalUAS.setStatus("current")
_CMsDwdmOtnIntervalBBE_Type = Counter32
_CMsDwdmOtnIntervalBBE_Object = MibTableColumn
cMsDwdmOtnIntervalBBE = _CMsDwdmOtnIntervalBBE_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 3, 1, 8),
    _CMsDwdmOtnIntervalBBE_Type()
)
cMsDwdmOtnIntervalBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnIntervalBBE.setStatus("current")
_CMsDwdmOtnIntervalESR_Type = Counter32
_CMsDwdmOtnIntervalESR_Object = MibTableColumn
cMsDwdmOtnIntervalESR = _CMsDwdmOtnIntervalESR_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 3, 1, 9),
    _CMsDwdmOtnIntervalESR_Type()
)
cMsDwdmOtnIntervalESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnIntervalESR.setStatus("current")
_CMsDwdmOtnIntervalSESR_Type = Counter32
_CMsDwdmOtnIntervalSESR_Object = MibTableColumn
cMsDwdmOtnIntervalSESR = _CMsDwdmOtnIntervalSESR_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 3, 1, 10),
    _CMsDwdmOtnIntervalSESR_Type()
)
cMsDwdmOtnIntervalSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnIntervalSESR.setStatus("current")
_CMsDwdmOtnIntervalBBER_Type = Counter32
_CMsDwdmOtnIntervalBBER_Object = MibTableColumn
cMsDwdmOtnIntervalBBER = _CMsDwdmOtnIntervalBBER_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 3, 1, 11),
    _CMsDwdmOtnIntervalBBER_Type()
)
cMsDwdmOtnIntervalBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnIntervalBBER.setStatus("current")
_CMsDwdmOtnIntervalValidData_Type = TruthValue
_CMsDwdmOtnIntervalValidData_Object = MibTableColumn
cMsDwdmOtnIntervalValidData = _CMsDwdmOtnIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 2, 3, 1, 12),
    _CMsDwdmOtnIntervalValidData_Type()
)
cMsDwdmOtnIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmOtnIntervalValidData.setStatus("current")
_CerentMsDwdmFEC_ObjectIdentity = ObjectIdentity
cerentMsDwdmFEC = _CerentMsDwdmFEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3)
)
_CMsDwdmFECThresholdsTable_Object = MibTable
cMsDwdmFECThresholdsTable = _CMsDwdmFECThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 1)
)
if mibBuilder.loadTexts:
    cMsDwdmFECThresholdsTable.setStatus("current")
_CMsDwdmFECThresholdsEntry_Object = MibTableRow
cMsDwdmFECThresholdsEntry = _CMsDwdmFECThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 1, 1)
)
cMsDwdmFECThresholdsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERENT-MSDWDM-MIB", "cMsDwdmFECThreshIntervalType"),
)
if mibBuilder.loadTexts:
    cMsDwdmFECThresholdsEntry.setStatus("current")
_CMsDwdmFECThreshIntervalType_Type = CerentPeriod
_CMsDwdmFECThreshIntervalType_Object = MibTableColumn
cMsDwdmFECThreshIntervalType = _CMsDwdmFECThreshIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 1, 1, 1),
    _CMsDwdmFECThreshIntervalType_Type()
)
cMsDwdmFECThreshIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsDwdmFECThreshIntervalType.setStatus("current")
_CMsDwdmFECThreshBitErrCor_Type = Unsigned32
_CMsDwdmFECThreshBitErrCor_Object = MibTableColumn
cMsDwdmFECThreshBitErrCor = _CMsDwdmFECThreshBitErrCor_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 1, 1, 2),
    _CMsDwdmFECThreshBitErrCor_Type()
)
cMsDwdmFECThreshBitErrCor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmFECThreshBitErrCor.setStatus("current")
_CMsDwdmFECThreshByteErrCor_Type = Unsigned32
_CMsDwdmFECThreshByteErrCor_Object = MibTableColumn
cMsDwdmFECThreshByteErrCor = _CMsDwdmFECThreshByteErrCor_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 1, 1, 3),
    _CMsDwdmFECThreshByteErrCor_Type()
)
cMsDwdmFECThreshByteErrCor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmFECThreshByteErrCor.setStatus("current")
_CMsDwdmFECThreshZeroErrDet_Type = Unsigned32
_CMsDwdmFECThreshZeroErrDet_Object = MibTableColumn
cMsDwdmFECThreshZeroErrDet = _CMsDwdmFECThreshZeroErrDet_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 1, 1, 4),
    _CMsDwdmFECThreshZeroErrDet_Type()
)
cMsDwdmFECThreshZeroErrDet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmFECThreshZeroErrDet.setStatus("current")
_CMsDwdmFECThreshOneErrDet_Type = Unsigned32
_CMsDwdmFECThreshOneErrDet_Object = MibTableColumn
cMsDwdmFECThreshOneErrDet = _CMsDwdmFECThreshOneErrDet_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 1, 1, 5),
    _CMsDwdmFECThreshOneErrDet_Type()
)
cMsDwdmFECThreshOneErrDet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmFECThreshOneErrDet.setStatus("current")
_CMsDwdmFECThreshUncorWords_Type = Unsigned32
_CMsDwdmFECThreshUncorWords_Object = MibTableColumn
cMsDwdmFECThreshUncorWords = _CMsDwdmFECThreshUncorWords_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 1, 1, 6),
    _CMsDwdmFECThreshUncorWords_Type()
)
cMsDwdmFECThreshUncorWords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsDwdmFECThreshUncorWords.setStatus("current")
_CMsDwdmFECCurrentTable_Object = MibTable
cMsDwdmFECCurrentTable = _CMsDwdmFECCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 2)
)
if mibBuilder.loadTexts:
    cMsDwdmFECCurrentTable.setStatus("current")
_CMsDwdmFECCurrentEntry_Object = MibTableRow
cMsDwdmFECCurrentEntry = _CMsDwdmFECCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 2, 1)
)
cMsDwdmFECCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERENT-MSDWDM-MIB", "cMsDwdmFECCurIntervalType"),
)
if mibBuilder.loadTexts:
    cMsDwdmFECCurrentEntry.setStatus("current")
_CMsDwdmFECCurIntervalType_Type = CerentPeriod
_CMsDwdmFECCurIntervalType_Object = MibTableColumn
cMsDwdmFECCurIntervalType = _CMsDwdmFECCurIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 2, 1, 1),
    _CMsDwdmFECCurIntervalType_Type()
)
cMsDwdmFECCurIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsDwdmFECCurIntervalType.setStatus("current")
_CMsDwdmFECCurrentBitErrCor_Type = Counter32
_CMsDwdmFECCurrentBitErrCor_Object = MibTableColumn
cMsDwdmFECCurrentBitErrCor = _CMsDwdmFECCurrentBitErrCor_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 2, 1, 2),
    _CMsDwdmFECCurrentBitErrCor_Type()
)
cMsDwdmFECCurrentBitErrCor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmFECCurrentBitErrCor.setStatus("current")
_CMsDwdmFECCurrentByteErrCor_Type = Counter32
_CMsDwdmFECCurrentByteErrCor_Object = MibTableColumn
cMsDwdmFECCurrentByteErrCor = _CMsDwdmFECCurrentByteErrCor_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 2, 1, 3),
    _CMsDwdmFECCurrentByteErrCor_Type()
)
cMsDwdmFECCurrentByteErrCor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmFECCurrentByteErrCor.setStatus("current")
_CMsDwdmFECCurrentZeroErrDet_Type = Counter32
_CMsDwdmFECCurrentZeroErrDet_Object = MibTableColumn
cMsDwdmFECCurrentZeroErrDet = _CMsDwdmFECCurrentZeroErrDet_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 2, 1, 4),
    _CMsDwdmFECCurrentZeroErrDet_Type()
)
cMsDwdmFECCurrentZeroErrDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmFECCurrentZeroErrDet.setStatus("current")
_CMsDwdmFECCurrentOneErrDet_Type = Counter32
_CMsDwdmFECCurrentOneErrDet_Object = MibTableColumn
cMsDwdmFECCurrentOneErrDet = _CMsDwdmFECCurrentOneErrDet_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 2, 1, 5),
    _CMsDwdmFECCurrentOneErrDet_Type()
)
cMsDwdmFECCurrentOneErrDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmFECCurrentOneErrDet.setStatus("current")
_CMsDwdmFECCurrentUncorWords_Type = Counter32
_CMsDwdmFECCurrentUncorWords_Object = MibTableColumn
cMsDwdmFECCurrentUncorWords = _CMsDwdmFECCurrentUncorWords_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 2, 1, 6),
    _CMsDwdmFECCurrentUncorWords_Type()
)
cMsDwdmFECCurrentUncorWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmFECCurrentUncorWords.setStatus("current")
_CMsDwdmFECIntervalTable_Object = MibTable
cMsDwdmFECIntervalTable = _CMsDwdmFECIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 3)
)
if mibBuilder.loadTexts:
    cMsDwdmFECIntervalTable.setStatus("current")
_CMsDwdmFECIntervalEntry_Object = MibTableRow
cMsDwdmFECIntervalEntry = _CMsDwdmFECIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 3, 1)
)
cMsDwdmFECIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERENT-MSDWDM-MIB", "cMsDwdmFECIntervalType"),
    (0, "CERENT-MSDWDM-MIB", "cMsDwdmFECIntervalNum"),
)
if mibBuilder.loadTexts:
    cMsDwdmFECIntervalEntry.setStatus("current")
_CMsDwdmFECIntervalType_Type = CerentPeriod
_CMsDwdmFECIntervalType_Object = MibTableColumn
cMsDwdmFECIntervalType = _CMsDwdmFECIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 3, 1, 1),
    _CMsDwdmFECIntervalType_Type()
)
cMsDwdmFECIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsDwdmFECIntervalType.setStatus("current")


class _CMsDwdmFECIntervalNum_Type(Integer32):
    """Custom type cMsDwdmFECIntervalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CMsDwdmFECIntervalNum_Type.__name__ = "Integer32"
_CMsDwdmFECIntervalNum_Object = MibTableColumn
cMsDwdmFECIntervalNum = _CMsDwdmFECIntervalNum_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 3, 1, 2),
    _CMsDwdmFECIntervalNum_Type()
)
cMsDwdmFECIntervalNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsDwdmFECIntervalNum.setStatus("current")
_CMsDwdmFECIntervalBitErrCor_Type = Counter32
_CMsDwdmFECIntervalBitErrCor_Object = MibTableColumn
cMsDwdmFECIntervalBitErrCor = _CMsDwdmFECIntervalBitErrCor_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 3, 1, 3),
    _CMsDwdmFECIntervalBitErrCor_Type()
)
cMsDwdmFECIntervalBitErrCor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmFECIntervalBitErrCor.setStatus("current")
_CMsDwdmFECIntervalByteErrCor_Type = Counter32
_CMsDwdmFECIntervalByteErrCor_Object = MibTableColumn
cMsDwdmFECIntervalByteErrCor = _CMsDwdmFECIntervalByteErrCor_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 3, 1, 4),
    _CMsDwdmFECIntervalByteErrCor_Type()
)
cMsDwdmFECIntervalByteErrCor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmFECIntervalByteErrCor.setStatus("current")
_CMsDwdmFECIntervalZeroErrDet_Type = Counter32
_CMsDwdmFECIntervalZeroErrDet_Object = MibTableColumn
cMsDwdmFECIntervalZeroErrDet = _CMsDwdmFECIntervalZeroErrDet_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 3, 1, 5),
    _CMsDwdmFECIntervalZeroErrDet_Type()
)
cMsDwdmFECIntervalZeroErrDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmFECIntervalZeroErrDet.setStatus("current")
_CMsDwdmFECIntervalOneErrDet_Type = Counter32
_CMsDwdmFECIntervalOneErrDet_Object = MibTableColumn
cMsDwdmFECIntervalOneErrDet = _CMsDwdmFECIntervalOneErrDet_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 3, 1, 6),
    _CMsDwdmFECIntervalOneErrDet_Type()
)
cMsDwdmFECIntervalOneErrDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmFECIntervalOneErrDet.setStatus("current")
_CMsDwdmFECIntervalUncorWords_Type = Counter32
_CMsDwdmFECIntervalUncorWords_Object = MibTableColumn
cMsDwdmFECIntervalUncorWords = _CMsDwdmFECIntervalUncorWords_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 3, 1, 7),
    _CMsDwdmFECIntervalUncorWords_Type()
)
cMsDwdmFECIntervalUncorWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmFECIntervalUncorWords.setStatus("current")
_CMsDwdmFECIntervalValidData_Type = TruthValue
_CMsDwdmFECIntervalValidData_Object = MibTableColumn
cMsDwdmFECIntervalValidData = _CMsDwdmFECIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 3, 3, 1, 8),
    _CMsDwdmFECIntervalValidData_Type()
)
cMsDwdmFECIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsDwdmFECIntervalValidData.setStatus("current")
_CerentMsDwdm8B10B_ObjectIdentity = ObjectIdentity
cerentMsDwdm8B10B = _CerentMsDwdm8B10B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4)
)
_C8B10BThresholdsTable_Object = MibTable
c8B10BThresholdsTable = _C8B10BThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1)
)
if mibBuilder.loadTexts:
    c8B10BThresholdsTable.setStatus("current")
_C8B10BThresholdsEntry_Object = MibTableRow
c8B10BThresholdsEntry = _C8B10BThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1)
)
c8B10BThresholdsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERENT-MSDWDM-MIB", "c8B10BThreshIntervalType"),
)
if mibBuilder.loadTexts:
    c8B10BThresholdsEntry.setStatus("current")
_C8B10BThreshIntervalType_Type = IntervalType
_C8B10BThreshIntervalType_Object = MibTableColumn
c8B10BThreshIntervalType = _C8B10BThreshIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 1),
    _C8B10BThreshIntervalType_Type()
)
c8B10BThreshIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c8B10BThreshIntervalType.setStatus("current")
_C8B10BThreshInvalidPkts_Type = Unsigned32
_C8B10BThreshInvalidPkts_Object = MibTableColumn
c8B10BThreshInvalidPkts = _C8B10BThreshInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 2),
    _C8B10BThreshInvalidPkts_Type()
)
c8B10BThreshInvalidPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c8B10BThreshInvalidPkts.setStatus("current")
_C8B10BThreshIPOverflow_Type = Unsigned32
_C8B10BThreshIPOverflow_Object = MibTableColumn
c8B10BThreshIPOverflow = _C8B10BThreshIPOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 3),
    _C8B10BThreshIPOverflow_Type()
)
c8B10BThreshIPOverflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c8B10BThreshIPOverflow.setStatus("current")
_C8B10BThreshHCInvalidPkts_Type = Counter64
_C8B10BThreshHCInvalidPkts_Object = MibTableColumn
c8B10BThreshHCInvalidPkts = _C8B10BThreshHCInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 4),
    _C8B10BThreshHCInvalidPkts_Type()
)
c8B10BThreshHCInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BThreshHCInvalidPkts.setStatus("current")
_C8B10BThreshValidPkts_Type = Unsigned32
_C8B10BThreshValidPkts_Object = MibTableColumn
c8B10BThreshValidPkts = _C8B10BThreshValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 5),
    _C8B10BThreshValidPkts_Type()
)
c8B10BThreshValidPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c8B10BThreshValidPkts.setStatus("current")
_C8B10BThreshVPOverflow_Type = Unsigned32
_C8B10BThreshVPOverflow_Object = MibTableColumn
c8B10BThreshVPOverflow = _C8B10BThreshVPOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 6),
    _C8B10BThreshVPOverflow_Type()
)
c8B10BThreshVPOverflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c8B10BThreshVPOverflow.setStatus("current")
_C8B10BThreshHCValidPkts_Type = Counter64
_C8B10BThreshHCValidPkts_Object = MibTableColumn
c8B10BThreshHCValidPkts = _C8B10BThreshHCValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 7),
    _C8B10BThreshHCValidPkts_Type()
)
c8B10BThreshHCValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BThreshHCValidPkts.setStatus("current")
_C8B10BThreshIdleSets_Type = Unsigned32
_C8B10BThreshIdleSets_Object = MibTableColumn
c8B10BThreshIdleSets = _C8B10BThreshIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 8),
    _C8B10BThreshIdleSets_Type()
)
c8B10BThreshIdleSets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c8B10BThreshIdleSets.setStatus("current")
_C8B10BThreshISOverflow_Type = Unsigned32
_C8B10BThreshISOverflow_Object = MibTableColumn
c8B10BThreshISOverflow = _C8B10BThreshISOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 9),
    _C8B10BThreshISOverflow_Type()
)
c8B10BThreshISOverflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c8B10BThreshISOverflow.setStatus("current")
_C8B10BThreshHCIdleSets_Type = Counter64
_C8B10BThreshHCIdleSets_Object = MibTableColumn
c8B10BThreshHCIdleSets = _C8B10BThreshHCIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 10),
    _C8B10BThreshHCIdleSets_Type()
)
c8B10BThreshHCIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BThreshHCIdleSets.setStatus("current")
_C8B10BThreshNonIdleSets_Type = Unsigned32
_C8B10BThreshNonIdleSets_Object = MibTableColumn
c8B10BThreshNonIdleSets = _C8B10BThreshNonIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 11),
    _C8B10BThreshNonIdleSets_Type()
)
c8B10BThreshNonIdleSets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c8B10BThreshNonIdleSets.setStatus("current")
_C8B10BThreshNISOverflow_Type = Unsigned32
_C8B10BThreshNISOverflow_Object = MibTableColumn
c8B10BThreshNISOverflow = _C8B10BThreshNISOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 12),
    _C8B10BThreshNISOverflow_Type()
)
c8B10BThreshNISOverflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c8B10BThreshNISOverflow.setStatus("current")
_C8B10BThreshHCNonIdleSets_Type = Counter64
_C8B10BThreshHCNonIdleSets_Object = MibTableColumn
c8B10BThreshHCNonIdleSets = _C8B10BThreshHCNonIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 13),
    _C8B10BThreshHCNonIdleSets_Type()
)
c8B10BThreshHCNonIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BThreshHCNonIdleSets.setStatus("current")
_C8B10BThreshDataSets_Type = Unsigned32
_C8B10BThreshDataSets_Object = MibTableColumn
c8B10BThreshDataSets = _C8B10BThreshDataSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 14),
    _C8B10BThreshDataSets_Type()
)
c8B10BThreshDataSets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c8B10BThreshDataSets.setStatus("current")
_C8B10BThreshDSOverflow_Type = Unsigned32
_C8B10BThreshDSOverflow_Object = MibTableColumn
c8B10BThreshDSOverflow = _C8B10BThreshDSOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 15),
    _C8B10BThreshDSOverflow_Type()
)
c8B10BThreshDSOverflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c8B10BThreshDSOverflow.setStatus("current")
_C8B10BThreshHCDataSets_Type = Counter64
_C8B10BThreshHCDataSets_Object = MibTableColumn
c8B10BThreshHCDataSets = _C8B10BThreshHCDataSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 16),
    _C8B10BThreshHCDataSets_Type()
)
c8B10BThreshHCDataSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BThreshHCDataSets.setStatus("current")
_C8B10BThreshCodeViols_Type = Unsigned32
_C8B10BThreshCodeViols_Object = MibTableColumn
c8B10BThreshCodeViols = _C8B10BThreshCodeViols_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 17),
    _C8B10BThreshCodeViols_Type()
)
c8B10BThreshCodeViols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c8B10BThreshCodeViols.setStatus("current")
_C8B10BThreshCVOverflow_Type = Unsigned32
_C8B10BThreshCVOverflow_Object = MibTableColumn
c8B10BThreshCVOverflow = _C8B10BThreshCVOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 18),
    _C8B10BThreshCVOverflow_Type()
)
c8B10BThreshCVOverflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    c8B10BThreshCVOverflow.setStatus("current")
_C8B10BThreshHCCodeViols_Type = Counter64
_C8B10BThreshHCCodeViols_Object = MibTableColumn
c8B10BThreshHCCodeViols = _C8B10BThreshHCCodeViols_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 1, 1, 19),
    _C8B10BThreshHCCodeViols_Type()
)
c8B10BThreshHCCodeViols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BThreshHCCodeViols.setStatus("current")
_C8B10BCurrentTable_Object = MibTable
c8B10BCurrentTable = _C8B10BCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2)
)
if mibBuilder.loadTexts:
    c8B10BCurrentTable.setStatus("current")
_C8B10BCurrentEntry_Object = MibTableRow
c8B10BCurrentEntry = _C8B10BCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1)
)
c8B10BCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERENT-MSDWDM-MIB", "c8B10BCurIntervalType"),
)
if mibBuilder.loadTexts:
    c8B10BCurrentEntry.setStatus("current")
_C8B10BCurIntervalType_Type = IntervalType
_C8B10BCurIntervalType_Object = MibTableColumn
c8B10BCurIntervalType = _C8B10BCurIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 1),
    _C8B10BCurIntervalType_Type()
)
c8B10BCurIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c8B10BCurIntervalType.setStatus("current")
_C8B10BCurrentCodeViols_Type = Counter32
_C8B10BCurrentCodeViols_Object = MibTableColumn
c8B10BCurrentCodeViols = _C8B10BCurrentCodeViols_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 2),
    _C8B10BCurrentCodeViols_Type()
)
c8B10BCurrentCodeViols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentCodeViols.setStatus("current")
_C8B10BCurrentCVOverflow_Type = Counter32
_C8B10BCurrentCVOverflow_Object = MibTableColumn
c8B10BCurrentCVOverflow = _C8B10BCurrentCVOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 3),
    _C8B10BCurrentCVOverflow_Type()
)
c8B10BCurrentCVOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentCVOverflow.setStatus("current")
_C8B10BCurrentHCCodeViols_Type = Counter64
_C8B10BCurrentHCCodeViols_Object = MibTableColumn
c8B10BCurrentHCCodeViols = _C8B10BCurrentHCCodeViols_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 4),
    _C8B10BCurrentHCCodeViols_Type()
)
c8B10BCurrentHCCodeViols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentHCCodeViols.setStatus("current")
_C8B10BCurrentValidPkts_Type = Counter32
_C8B10BCurrentValidPkts_Object = MibTableColumn
c8B10BCurrentValidPkts = _C8B10BCurrentValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 5),
    _C8B10BCurrentValidPkts_Type()
)
c8B10BCurrentValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentValidPkts.setStatus("current")
_C8B10BCurrentVPOverflow_Type = Counter32
_C8B10BCurrentVPOverflow_Object = MibTableColumn
c8B10BCurrentVPOverflow = _C8B10BCurrentVPOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 6),
    _C8B10BCurrentVPOverflow_Type()
)
c8B10BCurrentVPOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentVPOverflow.setStatus("current")
_C8B10BCurrentHCValidPkts_Type = Counter64
_C8B10BCurrentHCValidPkts_Object = MibTableColumn
c8B10BCurrentHCValidPkts = _C8B10BCurrentHCValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 7),
    _C8B10BCurrentHCValidPkts_Type()
)
c8B10BCurrentHCValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentHCValidPkts.setStatus("current")
_C8B10BCurrentInvalidPkts_Type = Counter32
_C8B10BCurrentInvalidPkts_Object = MibTableColumn
c8B10BCurrentInvalidPkts = _C8B10BCurrentInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 8),
    _C8B10BCurrentInvalidPkts_Type()
)
c8B10BCurrentInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentInvalidPkts.setStatus("current")
_C8B10BCurrentIPOverflow_Type = Counter32
_C8B10BCurrentIPOverflow_Object = MibTableColumn
c8B10BCurrentIPOverflow = _C8B10BCurrentIPOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 9),
    _C8B10BCurrentIPOverflow_Type()
)
c8B10BCurrentIPOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentIPOverflow.setStatus("current")
_C8B10BCurrentHCInvalidPkts_Type = Counter64
_C8B10BCurrentHCInvalidPkts_Object = MibTableColumn
c8B10BCurrentHCInvalidPkts = _C8B10BCurrentHCInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 10),
    _C8B10BCurrentHCInvalidPkts_Type()
)
c8B10BCurrentHCInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentHCInvalidPkts.setStatus("current")
_C8B10BCurrentIdleSets_Type = Counter32
_C8B10BCurrentIdleSets_Object = MibTableColumn
c8B10BCurrentIdleSets = _C8B10BCurrentIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 11),
    _C8B10BCurrentIdleSets_Type()
)
c8B10BCurrentIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentIdleSets.setStatus("current")
_C8B10BCurrentISOverflow_Type = Counter32
_C8B10BCurrentISOverflow_Object = MibTableColumn
c8B10BCurrentISOverflow = _C8B10BCurrentISOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 12),
    _C8B10BCurrentISOverflow_Type()
)
c8B10BCurrentISOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentISOverflow.setStatus("current")
_C8B10BCurrentHCIdleSets_Type = Counter64
_C8B10BCurrentHCIdleSets_Object = MibTableColumn
c8B10BCurrentHCIdleSets = _C8B10BCurrentHCIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 13),
    _C8B10BCurrentHCIdleSets_Type()
)
c8B10BCurrentHCIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentHCIdleSets.setStatus("current")
_C8B10BCurrentNonIdleSets_Type = Counter32
_C8B10BCurrentNonIdleSets_Object = MibTableColumn
c8B10BCurrentNonIdleSets = _C8B10BCurrentNonIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 14),
    _C8B10BCurrentNonIdleSets_Type()
)
c8B10BCurrentNonIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentNonIdleSets.setStatus("current")
_C8B10BCurrentNISOverflow_Type = Counter32
_C8B10BCurrentNISOverflow_Object = MibTableColumn
c8B10BCurrentNISOverflow = _C8B10BCurrentNISOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 15),
    _C8B10BCurrentNISOverflow_Type()
)
c8B10BCurrentNISOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentNISOverflow.setStatus("current")
_C8B10BCurrentHCNonIdleSets_Type = Counter64
_C8B10BCurrentHCNonIdleSets_Object = MibTableColumn
c8B10BCurrentHCNonIdleSets = _C8B10BCurrentHCNonIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 16),
    _C8B10BCurrentHCNonIdleSets_Type()
)
c8B10BCurrentHCNonIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentHCNonIdleSets.setStatus("current")
_C8B10BCurrentDataSets_Type = Counter32
_C8B10BCurrentDataSets_Object = MibTableColumn
c8B10BCurrentDataSets = _C8B10BCurrentDataSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 17),
    _C8B10BCurrentDataSets_Type()
)
c8B10BCurrentDataSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentDataSets.setStatus("current")
_C8B10BCurrentDSOverflow_Type = Counter32
_C8B10BCurrentDSOverflow_Object = MibTableColumn
c8B10BCurrentDSOverflow = _C8B10BCurrentDSOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 18),
    _C8B10BCurrentDSOverflow_Type()
)
c8B10BCurrentDSOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentDSOverflow.setStatus("current")
_C8B10BCurrentHCDataSets_Type = Counter64
_C8B10BCurrentHCDataSets_Object = MibTableColumn
c8B10BCurrentHCDataSets = _C8B10BCurrentHCDataSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 2, 1, 19),
    _C8B10BCurrentHCDataSets_Type()
)
c8B10BCurrentHCDataSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BCurrentHCDataSets.setStatus("current")
_C8B10BIntervalTable_Object = MibTable
c8B10BIntervalTable = _C8B10BIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3)
)
if mibBuilder.loadTexts:
    c8B10BIntervalTable.setStatus("current")
_C8B10BIntervalEntry_Object = MibTableRow
c8B10BIntervalEntry = _C8B10BIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1)
)
c8B10BIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERENT-MSDWDM-MIB", "c8B10BIntervalType"),
    (0, "CERENT-MSDWDM-MIB", "c8B10BIntervalNum"),
)
if mibBuilder.loadTexts:
    c8B10BIntervalEntry.setStatus("current")
_C8B10BIntervalType_Type = IntervalType
_C8B10BIntervalType_Object = MibTableColumn
c8B10BIntervalType = _C8B10BIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 1),
    _C8B10BIntervalType_Type()
)
c8B10BIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c8B10BIntervalType.setStatus("current")


class _C8B10BIntervalNum_Type(Integer32):
    """Custom type c8B10BIntervalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_C8B10BIntervalNum_Type.__name__ = "Integer32"
_C8B10BIntervalNum_Object = MibTableColumn
c8B10BIntervalNum = _C8B10BIntervalNum_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 2),
    _C8B10BIntervalNum_Type()
)
c8B10BIntervalNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    c8B10BIntervalNum.setStatus("current")
_C8B10BIntervalCodeViols_Type = Counter32
_C8B10BIntervalCodeViols_Object = MibTableColumn
c8B10BIntervalCodeViols = _C8B10BIntervalCodeViols_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 3),
    _C8B10BIntervalCodeViols_Type()
)
c8B10BIntervalCodeViols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalCodeViols.setStatus("current")
_C8B10BIntervalCVOverflow_Type = Counter32
_C8B10BIntervalCVOverflow_Object = MibTableColumn
c8B10BIntervalCVOverflow = _C8B10BIntervalCVOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 4),
    _C8B10BIntervalCVOverflow_Type()
)
c8B10BIntervalCVOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalCVOverflow.setStatus("current")
_C8B10BIntervalHCCodeViols_Type = Counter64
_C8B10BIntervalHCCodeViols_Object = MibTableColumn
c8B10BIntervalHCCodeViols = _C8B10BIntervalHCCodeViols_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 5),
    _C8B10BIntervalHCCodeViols_Type()
)
c8B10BIntervalHCCodeViols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalHCCodeViols.setStatus("current")
_C8B10BIntervalValidPkts_Type = Counter32
_C8B10BIntervalValidPkts_Object = MibTableColumn
c8B10BIntervalValidPkts = _C8B10BIntervalValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 6),
    _C8B10BIntervalValidPkts_Type()
)
c8B10BIntervalValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalValidPkts.setStatus("current")
_C8B10BIntervalVPOverflow_Type = Counter32
_C8B10BIntervalVPOverflow_Object = MibTableColumn
c8B10BIntervalVPOverflow = _C8B10BIntervalVPOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 7),
    _C8B10BIntervalVPOverflow_Type()
)
c8B10BIntervalVPOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalVPOverflow.setStatus("current")
_C8B10BIntervalHCValidPkts_Type = Counter64
_C8B10BIntervalHCValidPkts_Object = MibTableColumn
c8B10BIntervalHCValidPkts = _C8B10BIntervalHCValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 8),
    _C8B10BIntervalHCValidPkts_Type()
)
c8B10BIntervalHCValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalHCValidPkts.setStatus("current")
_C8B10BIntervalInvalidPkts_Type = Counter32
_C8B10BIntervalInvalidPkts_Object = MibTableColumn
c8B10BIntervalInvalidPkts = _C8B10BIntervalInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 9),
    _C8B10BIntervalInvalidPkts_Type()
)
c8B10BIntervalInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalInvalidPkts.setStatus("current")
_C8B10BIntervalIPOverflow_Type = Counter32
_C8B10BIntervalIPOverflow_Object = MibTableColumn
c8B10BIntervalIPOverflow = _C8B10BIntervalIPOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 10),
    _C8B10BIntervalIPOverflow_Type()
)
c8B10BIntervalIPOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalIPOverflow.setStatus("current")
_C8B10BIntervalHCInvalidPkts_Type = Counter64
_C8B10BIntervalHCInvalidPkts_Object = MibTableColumn
c8B10BIntervalHCInvalidPkts = _C8B10BIntervalHCInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 11),
    _C8B10BIntervalHCInvalidPkts_Type()
)
c8B10BIntervalHCInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalHCInvalidPkts.setStatus("current")
_C8B10BIntervalIdleSets_Type = Counter32
_C8B10BIntervalIdleSets_Object = MibTableColumn
c8B10BIntervalIdleSets = _C8B10BIntervalIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 12),
    _C8B10BIntervalIdleSets_Type()
)
c8B10BIntervalIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalIdleSets.setStatus("current")
_C8B10BIntervalISOverflow_Type = Counter32
_C8B10BIntervalISOverflow_Object = MibTableColumn
c8B10BIntervalISOverflow = _C8B10BIntervalISOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 13),
    _C8B10BIntervalISOverflow_Type()
)
c8B10BIntervalISOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalISOverflow.setStatus("current")
_C8B10BIntervalHCIdleSets_Type = Counter64
_C8B10BIntervalHCIdleSets_Object = MibTableColumn
c8B10BIntervalHCIdleSets = _C8B10BIntervalHCIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 14),
    _C8B10BIntervalHCIdleSets_Type()
)
c8B10BIntervalHCIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalHCIdleSets.setStatus("current")
_C8B10BIntervalNonIdleSets_Type = Counter32
_C8B10BIntervalNonIdleSets_Object = MibTableColumn
c8B10BIntervalNonIdleSets = _C8B10BIntervalNonIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 15),
    _C8B10BIntervalNonIdleSets_Type()
)
c8B10BIntervalNonIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalNonIdleSets.setStatus("current")
_C8B10BIntervalNISOverflow_Type = Counter32
_C8B10BIntervalNISOverflow_Object = MibTableColumn
c8B10BIntervalNISOverflow = _C8B10BIntervalNISOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 16),
    _C8B10BIntervalNISOverflow_Type()
)
c8B10BIntervalNISOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalNISOverflow.setStatus("current")
_C8B10BIntervalHCNonIdleSets_Type = Counter64
_C8B10BIntervalHCNonIdleSets_Object = MibTableColumn
c8B10BIntervalHCNonIdleSets = _C8B10BIntervalHCNonIdleSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 17),
    _C8B10BIntervalHCNonIdleSets_Type()
)
c8B10BIntervalHCNonIdleSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalHCNonIdleSets.setStatus("current")
_C8B10BIntervalDataSets_Type = Counter32
_C8B10BIntervalDataSets_Object = MibTableColumn
c8B10BIntervalDataSets = _C8B10BIntervalDataSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 18),
    _C8B10BIntervalDataSets_Type()
)
c8B10BIntervalDataSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalDataSets.setStatus("current")
_C8B10BIntervalDSOverflow_Type = Counter32
_C8B10BIntervalDSOverflow_Object = MibTableColumn
c8B10BIntervalDSOverflow = _C8B10BIntervalDSOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 19),
    _C8B10BIntervalDSOverflow_Type()
)
c8B10BIntervalDSOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalDSOverflow.setStatus("current")
_C8B10BIntervalHCDataSets_Type = Counter64
_C8B10BIntervalHCDataSets_Object = MibTableColumn
c8B10BIntervalHCDataSets = _C8B10BIntervalHCDataSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 20),
    _C8B10BIntervalHCDataSets_Type()
)
c8B10BIntervalHCDataSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalHCDataSets.setStatus("current")
_C8B10BIntervalValidData_Type = TruthValue
_C8B10BIntervalValidData_Object = MibTableColumn
c8B10BIntervalValidData = _C8B10BIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 40, 4, 3, 1, 21),
    _C8B10BIntervalValidData_Type()
)
c8B10BIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c8B10BIntervalValidData.setStatus("current")
_CerentMsDwdmMIBConformance_ObjectIdentity = ObjectIdentity
cerentMsDwdmMIBConformance = _CerentMsDwdmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 30)
)
_CerentMsDwdmMIBCompliances_ObjectIdentity = ObjectIdentity
cerentMsDwdmMIBCompliances = _CerentMsDwdmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 30, 1)
)
_CerentMsDwdmMIBGroups_ObjectIdentity = ObjectIdentity
cerentMsDwdmMIBGroups = _CerentMsDwdmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 30, 2)
)

# Managed Objects groups

cerentMsDwdmIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 30, 2, 1)
)
cerentMsDwdmIfConfigGroup.setObjects(
      *(("CERENT-MSDWDM-MIB", "cMsDwdmIfConfigProtocol"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfConfigDataRate"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfConfigLoopback"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfConfigWavelength"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfConfigOtnStatus"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfConfigFECStatus"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfOpticsValidIntervals"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfOTNValidIntervals"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfFECValidIntervals"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfConfigFECMode"))
)
if mibBuilder.loadTexts:
    cerentMsDwdmIfConfigGroup.setStatus("current")

cerentMsDwdmOtnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 30, 2, 2)
)
cerentMsDwdmOtnGroup.setObjects(
      *(("CERENT-MSDWDM-MIB", "cMsDwdmOtnThreshFC"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnThreshES"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnThreshSES"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnThreshUAS"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnThreshBBE"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnCurrentFC"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnCurrentES"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnCurrentSES"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnCurrentUAS"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnCurrentBBE"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnCurrentESR"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnCurrentSESR"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnCurrentBBER"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnIntervalFC"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnIntervalES"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnIntervalSES"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnIntervalUAS"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnIntervalBBE"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnIntervalESR"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnIntervalSESR"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnIntervalBBER"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmOtnIntervalValidData"))
)
if mibBuilder.loadTexts:
    cerentMsDwdmOtnGroup.setStatus("current")

cerentMsDwdmFECGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 30, 2, 3)
)
cerentMsDwdmFECGroup.setObjects(
      *(("CERENT-MSDWDM-MIB", "cMsDwdmFECThreshBitErrCor"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECThreshByteErrCor"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECThreshZeroErrDet"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECThreshOneErrDet"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECThreshUncorWords"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECCurrentBitErrCor"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECCurrentByteErrCor"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECCurrentZeroErrDet"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECCurrentOneErrDet"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECCurrentUncorWords"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECIntervalBitErrCor"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECIntervalByteErrCor"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECIntervalZeroErrDet"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECIntervalOneErrDet"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECIntervalUncorWords"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmFECIntervalValidData"))
)
if mibBuilder.loadTexts:
    cerentMsDwdmFECGroup.setStatus("current")

cMsDwdmIfTransportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 30, 2, 5)
)
cMsDwdmIfTransportGroup.setObjects(
      *(("CERENT-MSDWDM-MIB", "cMsDwdmIfTransportPortRule"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfTransportPower"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfTransportReferencePower"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfTransportCalibratedPower"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfTransportInsertionLoss"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfTransportLaserStatus"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfTransportAmplifierMode"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfTransportGain"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfTransportReferenceTilt"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfTransportCalibratedTilt"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfTransportDCULoss"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfTransportExpectedGain"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfTransportOSRI"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfTransportSideIdentifier"))
)
if mibBuilder.loadTexts:
    cMsDwdmIfTransportGroup.setStatus("current")

cMsDwdmIfMultiplexSectionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 30, 2, 6)
)
cMsDwdmIfMultiplexSectionTableGroup.setObjects(
      *(("CERENT-MSDWDM-MIB", "cMsDwdmIfMultiplexSectionPortRule"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfMultiplexSectionPower"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfMultiplexSectionReferencePower"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfMultiplexSectionCalibratedPower"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfMultiplexSectionInsertionLoss"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfMultiplexSectionActualBand"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfMultiplexSectionExpectedBand"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfMultiplexSectionSideIdentifier"))
)
if mibBuilder.loadTexts:
    cMsDwdmIfMultiplexSectionTableGroup.setStatus("current")

cMsDwdmIfChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 30, 2, 7)
)
cMsDwdmIfChannelGroup.setObjects(
      *(("CERENT-MSDWDM-MIB", "cMsDwdmIfChannelPortRule"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfChannelPower"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfChannelReferencePower"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfChannelCalibratedPower"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfChannelInsertionLoss"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfChannelActualWavelength"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfChannelExpectedWavelength"),
        ("CERENT-MSDWDM-MIB", "cMsDwdmIfChannelSideIdentifier"))
)
if mibBuilder.loadTexts:
    cMsDwdmIfChannelGroup.setStatus("current")

cerent8B10BThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 30, 2, 8)
)
cerent8B10BThreshGroup.setObjects(
      *(("CERENT-MSDWDM-MIB", "c8B10BThreshInvalidPkts"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshValidPkts"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshIdleSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshNonIdleSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshDataSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshCodeViols"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalCodeViols"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshIPOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshVPOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshISOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshNISOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshDSOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshCVOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshHCInvalidPkts"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshHCValidPkts"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshHCIdleSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshHCNonIdleSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshHCDataSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BThreshHCCodeViols"))
)
if mibBuilder.loadTexts:
    cerent8B10BThreshGroup.setStatus("current")

cerent8B10BStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 30, 2, 9)
)
cerent8B10BStatsGroup.setObjects(
      *(("CERENT-MSDWDM-MIB", "c8B10BCurrentCodeViols"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentCVOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentHCCodeViols"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentValidPkts"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentVPOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentHCValidPkts"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentInvalidPkts"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentIPOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentHCInvalidPkts"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentIdleSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentISOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentHCIdleSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentNonIdleSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentNISOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentHCNonIdleSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentDataSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentDSOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BCurrentHCDataSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalHCCodeViols"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalValidPkts"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalHCValidPkts"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalInvalidPkts"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalHCInvalidPkts"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalIdleSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalHCIdleSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalNonIdleSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalHCNonIdleSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalDataSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalHCDataSets"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalCVOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalVPOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalIPOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalISOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalNISOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalDSOverflow"),
        ("CERENT-MSDWDM-MIB", "c8B10BIntervalValidData"))
)
if mibBuilder.loadTexts:
    cerent8B10BStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cerentMsDwdmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3607, 5, 30, 1, 1)
)
if mibBuilder.loadTexts:
    cerentMsDwdmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CERENT-MSDWDM-MIB",
    **{"ProtocolType": ProtocolType,
       "IntervalType": IntervalType,
       "LocationAndIntervalType": LocationAndIntervalType,
       "MonitorType": MonitorType,
       "RingDirection": RingDirection,
       "SideIdentifier": SideIdentifier,
       "OpticalPortRule": OpticalPortRule,
       "LaserStatus": LaserStatus,
       "OpticalAmplifierMode": OpticalAmplifierMode,
       "OpticalBand": OpticalBand,
       "OpticalWavelength": OpticalWavelength,
       "OpticalPowerInDbm": OpticalPowerInDbm,
       "OpticalAttenInDb": OpticalAttenInDb,
       "TDCUCompensation": TDCUCompensation,
       "cerentMsDwdmMIB": cerentMsDwdmMIB,
       "cerentMsDwdmMIBObjects": cerentMsDwdmMIBObjects,
       "cerentMsDwdmIf": cerentMsDwdmIf,
       "cMsDwdmIfConfigTable": cMsDwdmIfConfigTable,
       "cMsDwdmIfConfigEntry": cMsDwdmIfConfigEntry,
       "cMsDwdmIfConfigProtocol": cMsDwdmIfConfigProtocol,
       "cMsDwdmIfConfigDataRate": cMsDwdmIfConfigDataRate,
       "cMsDwdmIfConfigLoopback": cMsDwdmIfConfigLoopback,
       "cMsDwdmIfConfigWavelength": cMsDwdmIfConfigWavelength,
       "cMsDwdmIfConfigOtnStatus": cMsDwdmIfConfigOtnStatus,
       "cMsDwdmIfConfigFECStatus": cMsDwdmIfConfigFECStatus,
       "cMsDwdmIfOpticsValidIntervals": cMsDwdmIfOpticsValidIntervals,
       "cMsDwdmIfOTNValidIntervals": cMsDwdmIfOTNValidIntervals,
       "cMsDwdmIfFECValidIntervals": cMsDwdmIfFECValidIntervals,
       "cMsDwdmIfConfigFECMode": cMsDwdmIfConfigFECMode,
       "cMsDwdmIfTransportTable": cMsDwdmIfTransportTable,
       "cMsDwdmIfTransportEntry": cMsDwdmIfTransportEntry,
       "cMsDwdmIfTransportRingDirection": cMsDwdmIfTransportRingDirection,
       "cMsDwdmIfTransportPortRule": cMsDwdmIfTransportPortRule,
       "cMsDwdmIfTransportPower": cMsDwdmIfTransportPower,
       "cMsDwdmIfTransportReferencePower": cMsDwdmIfTransportReferencePower,
       "cMsDwdmIfTransportCalibratedPower": cMsDwdmIfTransportCalibratedPower,
       "cMsDwdmIfTransportInsertionLoss": cMsDwdmIfTransportInsertionLoss,
       "cMsDwdmIfTransportLaserStatus": cMsDwdmIfTransportLaserStatus,
       "cMsDwdmIfTransportAmplifierMode": cMsDwdmIfTransportAmplifierMode,
       "cMsDwdmIfTransportGain": cMsDwdmIfTransportGain,
       "cMsDwdmIfTransportReferenceTilt": cMsDwdmIfTransportReferenceTilt,
       "cMsDwdmIfTransportCalibratedTilt": cMsDwdmIfTransportCalibratedTilt,
       "cMsDwdmIfTransportDCULoss": cMsDwdmIfTransportDCULoss,
       "cMsDwdmIfTransportOSRI": cMsDwdmIfTransportOSRI,
       "cMsDwdmIfTransportExpectedGain": cMsDwdmIfTransportExpectedGain,
       "cMsDwdmIfTransportSideIdentifier": cMsDwdmIfTransportSideIdentifier,
       "cMsDwdmIfTransportAddPower": cMsDwdmIfTransportAddPower,
       "cMsDwdmIfTransportOSCPower": cMsDwdmIfTransportOSCPower,
       "cMsDwdmIfTransportTDCUCompensation": cMsDwdmIfTransportTDCUCompensation,
       "cMsDwdmIfMultiplexSectionTable": cMsDwdmIfMultiplexSectionTable,
       "cMsDwdmIfMultiplexSectionEntry": cMsDwdmIfMultiplexSectionEntry,
       "cMsDwdmIfMultiplexSectionRingDirection": cMsDwdmIfMultiplexSectionRingDirection,
       "cMsDwdmIfMultiplexSectionPortRule": cMsDwdmIfMultiplexSectionPortRule,
       "cMsDwdmIfMultiplexSectionPower": cMsDwdmIfMultiplexSectionPower,
       "cMsDwdmIfMultiplexSectionReferencePower": cMsDwdmIfMultiplexSectionReferencePower,
       "cMsDwdmIfMultiplexSectionCalibratedPower": cMsDwdmIfMultiplexSectionCalibratedPower,
       "cMsDwdmIfMultiplexSectionInsertionLoss": cMsDwdmIfMultiplexSectionInsertionLoss,
       "cMsDwdmIfMultiplexSectionActualBand": cMsDwdmIfMultiplexSectionActualBand,
       "cMsDwdmIfMultiplexSectionExpectedBand": cMsDwdmIfMultiplexSectionExpectedBand,
       "cMsDwdmIfMultiplexSectionSideIdentifier": cMsDwdmIfMultiplexSectionSideIdentifier,
       "cMsDwdmIfChannelTable": cMsDwdmIfChannelTable,
       "cMsDwdmIfChannelEntry": cMsDwdmIfChannelEntry,
       "cMsDwdmIfChannelRingDirection": cMsDwdmIfChannelRingDirection,
       "cMsDwdmIfChannelPortRule": cMsDwdmIfChannelPortRule,
       "cMsDwdmIfChannelPower": cMsDwdmIfChannelPower,
       "cMsDwdmIfChannelReferencePower": cMsDwdmIfChannelReferencePower,
       "cMsDwdmIfChannelCalibratedPower": cMsDwdmIfChannelCalibratedPower,
       "cMsDwdmIfChannelInsertionLoss": cMsDwdmIfChannelInsertionLoss,
       "cMsDwdmIfChannelActualWavelength": cMsDwdmIfChannelActualWavelength,
       "cMsDwdmIfChannelExpectedWavelength": cMsDwdmIfChannelExpectedWavelength,
       "cMsDwdmIfChannelSideIdentifier": cMsDwdmIfChannelSideIdentifier,
       "cerentMsDwdmOtn": cerentMsDwdmOtn,
       "cMsDwdmOtnThresholdsTable": cMsDwdmOtnThresholdsTable,
       "cMsDwdmOtnThresholdsEntry": cMsDwdmOtnThresholdsEntry,
       "cMsDwdmOtnThreshMonType": cMsDwdmOtnThreshMonType,
       "cMsDwdmOtnThreshIntervalType": cMsDwdmOtnThreshIntervalType,
       "cMsDwdmOtnThreshFC": cMsDwdmOtnThreshFC,
       "cMsDwdmOtnThreshES": cMsDwdmOtnThreshES,
       "cMsDwdmOtnThreshSES": cMsDwdmOtnThreshSES,
       "cMsDwdmOtnThreshUAS": cMsDwdmOtnThreshUAS,
       "cMsDwdmOtnThreshBBE": cMsDwdmOtnThreshBBE,
       "cMsDwdmOtnCurrentTable": cMsDwdmOtnCurrentTable,
       "cMsDwdmOtnCurrentEntry": cMsDwdmOtnCurrentEntry,
       "cMsDwdmOtnCurrentMonType": cMsDwdmOtnCurrentMonType,
       "cMsDwdmOtnCurIntervalType": cMsDwdmOtnCurIntervalType,
       "cMsDwdmOtnCurrentFC": cMsDwdmOtnCurrentFC,
       "cMsDwdmOtnCurrentES": cMsDwdmOtnCurrentES,
       "cMsDwdmOtnCurrentSES": cMsDwdmOtnCurrentSES,
       "cMsDwdmOtnCurrentUAS": cMsDwdmOtnCurrentUAS,
       "cMsDwdmOtnCurrentBBE": cMsDwdmOtnCurrentBBE,
       "cMsDwdmOtnCurrentESR": cMsDwdmOtnCurrentESR,
       "cMsDwdmOtnCurrentSESR": cMsDwdmOtnCurrentSESR,
       "cMsDwdmOtnCurrentBBER": cMsDwdmOtnCurrentBBER,
       "cMsDwdmOtnIntervalTable": cMsDwdmOtnIntervalTable,
       "cMsDwdmOtnIntervalEntry": cMsDwdmOtnIntervalEntry,
       "cMsDwdmOtnIntervalMonType": cMsDwdmOtnIntervalMonType,
       "cMsDwdmOtnIntervalType": cMsDwdmOtnIntervalType,
       "cMsDwdmOtnIntervalNum": cMsDwdmOtnIntervalNum,
       "cMsDwdmOtnIntervalFC": cMsDwdmOtnIntervalFC,
       "cMsDwdmOtnIntervalES": cMsDwdmOtnIntervalES,
       "cMsDwdmOtnIntervalSES": cMsDwdmOtnIntervalSES,
       "cMsDwdmOtnIntervalUAS": cMsDwdmOtnIntervalUAS,
       "cMsDwdmOtnIntervalBBE": cMsDwdmOtnIntervalBBE,
       "cMsDwdmOtnIntervalESR": cMsDwdmOtnIntervalESR,
       "cMsDwdmOtnIntervalSESR": cMsDwdmOtnIntervalSESR,
       "cMsDwdmOtnIntervalBBER": cMsDwdmOtnIntervalBBER,
       "cMsDwdmOtnIntervalValidData": cMsDwdmOtnIntervalValidData,
       "cerentMsDwdmFEC": cerentMsDwdmFEC,
       "cMsDwdmFECThresholdsTable": cMsDwdmFECThresholdsTable,
       "cMsDwdmFECThresholdsEntry": cMsDwdmFECThresholdsEntry,
       "cMsDwdmFECThreshIntervalType": cMsDwdmFECThreshIntervalType,
       "cMsDwdmFECThreshBitErrCor": cMsDwdmFECThreshBitErrCor,
       "cMsDwdmFECThreshByteErrCor": cMsDwdmFECThreshByteErrCor,
       "cMsDwdmFECThreshZeroErrDet": cMsDwdmFECThreshZeroErrDet,
       "cMsDwdmFECThreshOneErrDet": cMsDwdmFECThreshOneErrDet,
       "cMsDwdmFECThreshUncorWords": cMsDwdmFECThreshUncorWords,
       "cMsDwdmFECCurrentTable": cMsDwdmFECCurrentTable,
       "cMsDwdmFECCurrentEntry": cMsDwdmFECCurrentEntry,
       "cMsDwdmFECCurIntervalType": cMsDwdmFECCurIntervalType,
       "cMsDwdmFECCurrentBitErrCor": cMsDwdmFECCurrentBitErrCor,
       "cMsDwdmFECCurrentByteErrCor": cMsDwdmFECCurrentByteErrCor,
       "cMsDwdmFECCurrentZeroErrDet": cMsDwdmFECCurrentZeroErrDet,
       "cMsDwdmFECCurrentOneErrDet": cMsDwdmFECCurrentOneErrDet,
       "cMsDwdmFECCurrentUncorWords": cMsDwdmFECCurrentUncorWords,
       "cMsDwdmFECIntervalTable": cMsDwdmFECIntervalTable,
       "cMsDwdmFECIntervalEntry": cMsDwdmFECIntervalEntry,
       "cMsDwdmFECIntervalType": cMsDwdmFECIntervalType,
       "cMsDwdmFECIntervalNum": cMsDwdmFECIntervalNum,
       "cMsDwdmFECIntervalBitErrCor": cMsDwdmFECIntervalBitErrCor,
       "cMsDwdmFECIntervalByteErrCor": cMsDwdmFECIntervalByteErrCor,
       "cMsDwdmFECIntervalZeroErrDet": cMsDwdmFECIntervalZeroErrDet,
       "cMsDwdmFECIntervalOneErrDet": cMsDwdmFECIntervalOneErrDet,
       "cMsDwdmFECIntervalUncorWords": cMsDwdmFECIntervalUncorWords,
       "cMsDwdmFECIntervalValidData": cMsDwdmFECIntervalValidData,
       "cerentMsDwdm8B10B": cerentMsDwdm8B10B,
       "c8B10BThresholdsTable": c8B10BThresholdsTable,
       "c8B10BThresholdsEntry": c8B10BThresholdsEntry,
       "c8B10BThreshIntervalType": c8B10BThreshIntervalType,
       "c8B10BThreshInvalidPkts": c8B10BThreshInvalidPkts,
       "c8B10BThreshIPOverflow": c8B10BThreshIPOverflow,
       "c8B10BThreshHCInvalidPkts": c8B10BThreshHCInvalidPkts,
       "c8B10BThreshValidPkts": c8B10BThreshValidPkts,
       "c8B10BThreshVPOverflow": c8B10BThreshVPOverflow,
       "c8B10BThreshHCValidPkts": c8B10BThreshHCValidPkts,
       "c8B10BThreshIdleSets": c8B10BThreshIdleSets,
       "c8B10BThreshISOverflow": c8B10BThreshISOverflow,
       "c8B10BThreshHCIdleSets": c8B10BThreshHCIdleSets,
       "c8B10BThreshNonIdleSets": c8B10BThreshNonIdleSets,
       "c8B10BThreshNISOverflow": c8B10BThreshNISOverflow,
       "c8B10BThreshHCNonIdleSets": c8B10BThreshHCNonIdleSets,
       "c8B10BThreshDataSets": c8B10BThreshDataSets,
       "c8B10BThreshDSOverflow": c8B10BThreshDSOverflow,
       "c8B10BThreshHCDataSets": c8B10BThreshHCDataSets,
       "c8B10BThreshCodeViols": c8B10BThreshCodeViols,
       "c8B10BThreshCVOverflow": c8B10BThreshCVOverflow,
       "c8B10BThreshHCCodeViols": c8B10BThreshHCCodeViols,
       "c8B10BCurrentTable": c8B10BCurrentTable,
       "c8B10BCurrentEntry": c8B10BCurrentEntry,
       "c8B10BCurIntervalType": c8B10BCurIntervalType,
       "c8B10BCurrentCodeViols": c8B10BCurrentCodeViols,
       "c8B10BCurrentCVOverflow": c8B10BCurrentCVOverflow,
       "c8B10BCurrentHCCodeViols": c8B10BCurrentHCCodeViols,
       "c8B10BCurrentValidPkts": c8B10BCurrentValidPkts,
       "c8B10BCurrentVPOverflow": c8B10BCurrentVPOverflow,
       "c8B10BCurrentHCValidPkts": c8B10BCurrentHCValidPkts,
       "c8B10BCurrentInvalidPkts": c8B10BCurrentInvalidPkts,
       "c8B10BCurrentIPOverflow": c8B10BCurrentIPOverflow,
       "c8B10BCurrentHCInvalidPkts": c8B10BCurrentHCInvalidPkts,
       "c8B10BCurrentIdleSets": c8B10BCurrentIdleSets,
       "c8B10BCurrentISOverflow": c8B10BCurrentISOverflow,
       "c8B10BCurrentHCIdleSets": c8B10BCurrentHCIdleSets,
       "c8B10BCurrentNonIdleSets": c8B10BCurrentNonIdleSets,
       "c8B10BCurrentNISOverflow": c8B10BCurrentNISOverflow,
       "c8B10BCurrentHCNonIdleSets": c8B10BCurrentHCNonIdleSets,
       "c8B10BCurrentDataSets": c8B10BCurrentDataSets,
       "c8B10BCurrentDSOverflow": c8B10BCurrentDSOverflow,
       "c8B10BCurrentHCDataSets": c8B10BCurrentHCDataSets,
       "c8B10BIntervalTable": c8B10BIntervalTable,
       "c8B10BIntervalEntry": c8B10BIntervalEntry,
       "c8B10BIntervalType": c8B10BIntervalType,
       "c8B10BIntervalNum": c8B10BIntervalNum,
       "c8B10BIntervalCodeViols": c8B10BIntervalCodeViols,
       "c8B10BIntervalCVOverflow": c8B10BIntervalCVOverflow,
       "c8B10BIntervalHCCodeViols": c8B10BIntervalHCCodeViols,
       "c8B10BIntervalValidPkts": c8B10BIntervalValidPkts,
       "c8B10BIntervalVPOverflow": c8B10BIntervalVPOverflow,
       "c8B10BIntervalHCValidPkts": c8B10BIntervalHCValidPkts,
       "c8B10BIntervalInvalidPkts": c8B10BIntervalInvalidPkts,
       "c8B10BIntervalIPOverflow": c8B10BIntervalIPOverflow,
       "c8B10BIntervalHCInvalidPkts": c8B10BIntervalHCInvalidPkts,
       "c8B10BIntervalIdleSets": c8B10BIntervalIdleSets,
       "c8B10BIntervalISOverflow": c8B10BIntervalISOverflow,
       "c8B10BIntervalHCIdleSets": c8B10BIntervalHCIdleSets,
       "c8B10BIntervalNonIdleSets": c8B10BIntervalNonIdleSets,
       "c8B10BIntervalNISOverflow": c8B10BIntervalNISOverflow,
       "c8B10BIntervalHCNonIdleSets": c8B10BIntervalHCNonIdleSets,
       "c8B10BIntervalDataSets": c8B10BIntervalDataSets,
       "c8B10BIntervalDSOverflow": c8B10BIntervalDSOverflow,
       "c8B10BIntervalHCDataSets": c8B10BIntervalHCDataSets,
       "c8B10BIntervalValidData": c8B10BIntervalValidData,
       "cerentMsDwdmMIBConformance": cerentMsDwdmMIBConformance,
       "cerentMsDwdmMIBCompliances": cerentMsDwdmMIBCompliances,
       "cerentMsDwdmMIBCompliance": cerentMsDwdmMIBCompliance,
       "cerentMsDwdmMIBGroups": cerentMsDwdmMIBGroups,
       "cerentMsDwdmIfConfigGroup": cerentMsDwdmIfConfigGroup,
       "cerentMsDwdmOtnGroup": cerentMsDwdmOtnGroup,
       "cerentMsDwdmFECGroup": cerentMsDwdmFECGroup,
       "cMsDwdmIfTransportGroup": cMsDwdmIfTransportGroup,
       "cMsDwdmIfMultiplexSectionTableGroup": cMsDwdmIfMultiplexSectionTableGroup,
       "cMsDwdmIfChannelGroup": cMsDwdmIfChannelGroup,
       "cerent8B10BThreshGroup": cerent8B10BThreshGroup,
       "cerent8B10BStatsGroup": cerent8B10BStatsGroup}
)
