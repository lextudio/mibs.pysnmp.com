# SNMP MIB module (CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:35 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

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

(xylanChassis,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanChassis")


# MODULE-IDENTITY


# Types definitions



class XylanChasType(Integer32):
    """Custom type XylanChasType based on Integer32"""
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("micro", 6),
          ("oa408", 28),
          ("oa512", 29),
          ("omni3wx", 14),
          ("omni5", 3),
          ("omni5cell", 7),
          ("omni5e", 9),
          ("omni5wx", 12),
          ("omni9", 4),
          ("omni9cell", 8),
          ("omni9e", 10),
          ("omni9wx", 13),
          ("omnicore13", 27),
          ("os1032", 20),
          ("os2016", 19),
          ("os2032", 18),
          ("os3032", 17),
          ("os4016", 16),
          ("os4024", 26),
          ("os5024", 15),
          ("os5032", 22),
          ("os6032", 21),
          ("other", 2),
          ("pizport", 11),
          ("pizza", 5),
          ("xframe3", 25),
          ("xframe5", 23),
          ("xframe9", 24))
    )





class XylanModuleSubunit(Integer32):
    """Custom type XylanModuleSubunit based on Integer32"""
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
        *(("base", 1),
          ("csm3", 4),
          ("hsm1", 2),
          ("hsm2", 3))
    )





class XylanModuleType(Integer32):
    """Custom type XylanModuleType based on Integer32"""
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
              250,
              251,
              252,
              253,
              254,
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
              272,
              273,
              274,
              275,
              276,
              279,
              280,
              281,
              282,
              283,
              291,
              292,
              293)
        )
    )
    namedValues = NamedValues(
        *(("asm2", 47),
          ("asxab622fm2", 242),
          ("asxab622fs2", 243),
          ("asxasmk622", 270),
          ("asxelsy", 269),
          ("asxrfm622", 191),
          ("asxrfs622", 192),
          ("asxu", 241),
          ("atm", 12),
          ("atm155fsh", 133),
          ("atm155fshe", 132),
          ("atm2155flx", 213),
          ("atm2155fmx", 211),
          ("atm2155fsx", 212),
          ("atm2155fu", 168),
          ("atm2155mu", 166),
          ("atm2155rfmce", 209),
          ("atm2155rlx", 215),
          ("atm2155rsx", 214),
          ("atm2155su", 167),
          ("atm2622m", 124),
          ("atm2622rfsh", 128),
          ("atm2622s", 123),
          ("atm2622sl", 125),
          ("atm2ceds3x", 210),
          ("atm2ds3", 203),
          ("atm2ds3u", 169),
          ("atm2e1u", 172),
          ("atm2e3", 204),
          ("atm2e3u", 170),
          ("atm2imae1u", 194),
          ("atm2imat1u", 193),
          ("atm2m", 23),
          ("atm2mux", 75),
          ("atm2rm", 78),
          ("atm2rs", 79),
          ("atm2s", 24),
          ("atm2sl", 86),
          ("atm2sux", 74),
          ("atm2t1u", 171),
          ("atm2utpu", 173),
          ("atmce2s2e", 53),
          ("atmce2s2t", 52),
          ("atmcese12", 196),
          ("atmcest12", 195),
          ("atmds3", 16),
          ("atmds3ux", 54),
          ("atme1ux", 58),
          ("atme3", 34),
          ("atme3ux", 55),
          ("atmoc3ux", 56),
          ("atms", 18),
          ("atmshfs", 77),
          ("atmsrm", 80),
          ("atmsrs", 81),
          ("atmsux", 73),
          ("atmt1ux", 57),
          ("atmutp", 19),
          ("atmuux", 76),
          ("cab155", 101),
          ("cab155c", 103),
          ("cab155fsl", 102),
          ("cab155s", 104),
          ("cab4imae1", 117),
          ("cab4imat1", 116),
          ("cab8imae1", 119),
          ("cab8imat1", 118),
          ("cabce4sp", 152),
          ("cabcee1", 109),
          ("cabcet1", 110),
          ("cabcm", 151),
          ("cabds1", 105),
          ("cabds3", 106),
          ("cabe1", 107),
          ("cabe3", 108),
          ("cabfrds18", 237),
          ("cabfre18", 238),
          ("cabfrsp4", 239),
          ("cabt12c1", 146),
          ("cabt12c2", 145),
          ("cabt12ds31", 148),
          ("cabt12ds32", 147),
          ("cabt12e31", 150),
          ("cabt12e32", 149),
          ("cabt12l1", 144),
          ("cabt12l2", 143),
          ("cabt12m1", 140),
          ("cabt12m2", 139),
          ("cabt12s1", 142),
          ("cabt12s2", 141),
          ("cabtds3", 244),
          ("cabte3", 245),
          ("cddi", 10),
          ("cop", 205),
          ("csm", 30),
          ("csm12fsl", 89),
          ("csm12l", 63),
          ("csm12s", 43),
          ("csm6m2s", 72),
          ("csm8c", 85),
          ("csma12", 44),
          ("csma122", 199),
          ("csma24", 45),
          ("csmfsl", 87),
          ("csmh", 42),
          ("csmsfsl", 88),
          ("csmu", 69),
          ("csou", 256),
          ("e1008pm", 66),
          ("e1008ps", 67),
          ("e100fmfd", 36),
          ("e100fsfd", 35),
          ("e100txfd", 37),
          ("e10m", 33),
          ("e12f", 70),
          ("e12o", 71),
          ("empty", 3),
          ("eni12", 13),
          ("eni16", 7),
          ("eni6", 14),
          ("eni8", 6),
          ("esm100c32", 189),
          ("esm12t", 21),
          ("esm32", 40),
          ("esm8f", 20),
          ("esmf16", 131),
          ("esmf8", 130),
          ("esx100fm12", 197),
          ("esx100fs12", 198),
          ("esxc12", 153),
          ("esxc16", 154),
          ("esxc32", 155),
          ("esxf16", 156),
          ("esxfm12", 177),
          ("esxfm24", 111),
          ("esxfm24a", 178),
          ("etel24", 165),
          ("fcsm", 41),
          ("fcsm622", 100),
          ("fddi", 9),
          ("fddis", 17),
          ("fddisc2", 51),
          ("fesm4", 84),
          ("fesmh2m", 82),
          ("fesmh2s", 83),
          ("gsmfm", 136),
          ("gsmfm2", 187),
          ("gsmfmh", 138),
          ("gsmfms", 137),
          ("gsmfs2", 188),
          ("gsmx1", 176),
          ("gso6", 216),
          ("gsxl2", 161),
          ("gsxl4", 162),
          ("gsxm2", 159),
          ("gsxm4", 160),
          ("gsxs2", 157),
          ("gsxs4", 158),
          ("hre", 32),
          ("hrevx", 267),
          ("hsm", 4),
          ("hsm2", 27),
          ("hsm3", 68),
          ("hsx", 179),
          ("hsxh", 224),
          ("invalid", 2),
          ("kesxc32", 254),
          ("kesxfm16", 252),
          ("kesxfs16", 253),
          ("kgsxm2", 251),
          ("kgsxs2", 272),
          ("kgsxsh2", 273),
          ("meth12", 64),
          ("meth32", 65),
          ("modTypeVsaFxo", 275),
          ("modTypeVsaFxoFxo", 293),
          ("modTypeVsaFxs", 279),
          ("modTypeVsaFxsFxo", 292),
          ("modTypeVsaFxsFxs", 291),
          ("modTypeVsb", 276),
          ("modTypeVsd128MB12CH", 274),
          ("modTypeVsd128MB24CH", 280),
          ("modTypeVsd128MB36CH", 281),
          ("modTypeVsd128MB48CH", 282),
          ("modTypeVsd128MB60CH", 283),
          ("mpm", 5),
          ("mpm1g", 38),
          ("mpm2", 15),
          ("mpm3", 208),
          ("mpmc", 120),
          ("mpmf", 121),
          ("mpmos", 122),
          ("mpo", 207),
          ("mpoatmdc", 266),
          ("mpx3", 246),
          ("mt12", 129),
          ("oa408", 219),
          ("oa408ce", 228),
          ("oa4cee1", 227),
          ("oa4cet1", 226),
          ("oa512", 220),
          ("oa512u", 221),
          ("oa5xx", 229),
          ("oa5xxesm", 230),
          ("oa5xxft1e1", 235),
          ("oa5xxisdnst", 233),
          ("oa5xxisdnu", 234),
          ("oa5xxser", 232),
          ("oa5xxvoip", 236),
          ("oa5xxwan", 231),
          ("oapmfe8", 225),
          ("ocab155c", 257),
          ("ocab155fm", 258),
          ("ocab155fs", 259),
          ("ocab155fsh", 260),
          ("ocab2488fs", 264),
          ("ocab2488fsh", 265),
          ("ocab622fm", 261),
          ("ocab622fs", 262),
          ("ocab622fsh", 263),
          ("ocd12cmid", 223),
          ("ocmbpc", 222),
          ("os4024c", 185),
          ("os4024cf", 184),
          ("os4024f", 183),
          ("os4024g", 182),
          ("os6000", 217),
          ("os6032e", 218),
          ("osgsmfm2", 201),
          ("osgsmfs2", 202),
          ("p1032", 98),
          ("p1032F", 99),
          ("p1032cf", 115),
          ("p10U", 46),
          ("p2016", 97),
          ("p2032", 96),
          ("p3032", 94),
          ("p3032X", 95),
          ("p4016", 93),
          ("p5024", 92),
          ("pfe", 200),
          ("pizprt", 39),
          ("pizza", 28),
          ("pizza5032", 175),
          ("pizza6032", 174),
          ("pizza6032x", 180),
          ("pme2", 135),
          ("pme32", 91),
          ("pme32r", 134),
          ("pme8", 90),
          ("pmfe24", 186),
          ("pmfe32r", 181),
          ("ptsmcd16", 126),
          ("ptsmcd32", 127),
          ("puplink", 48),
          ("res31", 31),
          ("res49", 49),
          ("res50", 50),
          ("tni", 8),
          ("tokf", 22),
          ("tsm1g", 114),
          ("tsmcd16", 112),
          ("tsmcd32", 113),
          ("tsmcd6", 29),
          ("tsxcd16", 163),
          ("tsxcd32", 164),
          ("unknown", 1),
          ("vsa", 268),
          ("vsd", 206),
          ("vsdplus", 250),
          ("wsm", 25),
          ("wsm2s", 59),
          ("wsm2snc", 60),
          ("wsmbri", 26),
          ("wsmprie1", 62),
          ("wsmprit1", 61),
          ("wsxds32", 240),
          ("wsxm013", 190),
          ("x100eni", 11))
    )





class XylanMPMStateType(Integer32):
    """Custom type XylanMPMStateType based on Integer32"""
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
        *(("invalid", 2),
          ("primary", 3),
          ("secondary", 4),
          ("unknown", 1))
    )





class XylanPSStateType(Integer32):
    """Custom type XylanPSStateType based on Integer32"""
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
        *(("bad", 4),
          ("notPresent", 2),
          ("okay", 3),
          ("unknown", 1))
    )





class XylanTempStateType(Integer32):
    """Custom type XylanTempStateType based on Integer32"""
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
        *(("notPresent", 2),
          ("overThreshold", 3),
          ("underThreshold", 4),
          ("unknown", 1))
    )





class XylanImageSyncStatus(Integer32):
    """Custom type XylanImageSyncStatus based on Integer32"""
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
        *(("insync", 1),
          ("newer", 2),
          ("older", 3),
          ("syncing", 5),
          ("unknown", 4))
    )





class XylanConfigSyncStatus(Integer32):
    """Custom type XylanConfigSyncStatus based on Integer32"""
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
        *(("bootvalues", 6),
          ("insync", 1),
          ("newer", 2),
          ("older", 3),
          ("syncing", 5),
          ("unknown", 4))
    )





class XylanConfigSyncEnable(Integer32):
    """Custom type XylanConfigSyncEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )





class XylanFFSFileAction(Integer32):
    """Custom type XylanFFSFileAction based on Integer32"""
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
        *(("deletingFrom", 3),
          ("none", 1),
          ("readingFrom", 4),
          ("writingTo", 2))
    )





class XylanFFSFileActionStatus(Integer32):
    """Custom type XylanFFSFileActionStatus based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("none", 1),
          ("successfull", 3))
    )





class XylanSerialPortSpeed(Integer32):
    """Custom type XylanSerialPortSpeed based on Integer32"""
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
        *(("b1200", 3),
          ("b19200", 5),
          ("b38400", 6),
          ("b9600", 4),
          ("invalid", 2),
          ("unknown", 1))
    )





class XylanSerialPortParity(Integer32):
    """Custom type XylanSerialPortParity based on Integer32"""
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
        *(("even", 3),
          ("none", 2),
          ("odd", 4),
          ("unknown", 1))
    )





class XylanSerialPortMode(Integer32):
    """Custom type XylanSerialPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("console", 2),
          ("down", 1),
          ("slip", 3))
    )





class XylanFTStateType(Integer32):
    """Custom type XylanFTStateType based on Integer32"""
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
        *(("bad", 4),
          ("notPresent", 2),
          ("okay", 3),
          ("unknown", 1))
    )





class XylanModPortTypes(Integer32):
    """Custom type XylanModPortTypes based on Integer32"""
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
        *(("atm", 17),
          ("atmds1", 31),
          ("cdas", 15),
          ("e1", 26),
          ("e100basef", 33),
          ("e100baset", 30),
          ("e3", 27),
          ("egigfm", 34),
          ("egigfmh", 36),
          ("egigfms", 35),
          ("empty", 3),
          ("ethaui", 7),
          ("ethbnc", 8),
          ("ethfiorl", 9),
          ("ethutp", 5),
          ("fdas", 13),
          ("fdxaui", 23),
          ("fdxaui2", 24),
          ("fsas", 12),
          ("invalid", 2),
          ("irp", 22),
          ("isdnbri", 29),
          ("oc12", 18),
          ("serial", 4),
          ("t1", 25),
          ("tok", 10),
          ("tok100", 32),
          ("tokfbr", 21),
          ("unknown", 1),
          ("usp", 28),
          ("xmpt11", 11),
          ("xmpt14", 14),
          ("xmpt16", 16),
          ("xmpt19", 19),
          ("xmpt20", 20),
          ("xmpt6", 6))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChasInfo_ObjectIdentity = ObjectIdentity
chasInfo = _ChasInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 1)
)


class _ChasMake_Type(DisplayString):
    """Custom type chasMake based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ChasMake_Type.__name__ = "DisplayString"
_ChasMake_Object = MibScalar
chasMake = _ChasMake_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 1, 1),
    _ChasMake_Type()
)
chasMake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasMake.setStatus("mandatory")
_ChasType_Type = XylanChasType
_ChasType_Object = MibScalar
chasType = _ChasType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 1, 2),
    _ChasType_Type()
)
chasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasType.setStatus("mandatory")


class _ChasDescription_Type(DisplayString):
    """Custom type chasDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ChasDescription_Type.__name__ = "DisplayString"
_ChasDescription_Object = MibScalar
chasDescription = _ChasDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 1, 3),
    _ChasDescription_Type()
)
chasDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasDescription.setStatus("mandatory")
_ChasPhysicalChanges_Type = Counter32
_ChasPhysicalChanges_Object = MibScalar
chasPhysicalChanges = _ChasPhysicalChanges_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 1, 4),
    _ChasPhysicalChanges_Type()
)
chasPhysicalChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPhysicalChanges.setStatus("mandatory")
_ChasLogicalChanges_Type = Counter32
_ChasLogicalChanges_Object = MibScalar
chasLogicalChanges = _ChasLogicalChanges_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 1, 5),
    _ChasLogicalChanges_Type()
)
chasLogicalChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasLogicalChanges.setStatus("mandatory")
_ChasNoOfResets_Type = Counter32
_ChasNoOfResets_Object = MibScalar
chasNoOfResets = _ChasNoOfResets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 1, 6),
    _ChasNoOfResets_Type()
)
chasNoOfResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasNoOfResets.setStatus("mandatory")
_ChasBaseMacAddress_Type = MacAddress
_ChasBaseMacAddress_Object = MibScalar
chasBaseMacAddress = _ChasBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 1, 7),
    _ChasBaseMacAddress_Type()
)
chasBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBaseMacAddress.setStatus("mandatory")


class _ChasFreeSlots_Type(Integer32):
    """Custom type chasFreeSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ChasFreeSlots_Type.__name__ = "Integer32"
_ChasFreeSlots_Object = MibScalar
chasFreeSlots = _ChasFreeSlots_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 1, 8),
    _ChasFreeSlots_Type()
)
chasFreeSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasFreeSlots.setStatus("mandatory")
_ChasIpAddrToPing_Type = IpAddress
_ChasIpAddrToPing_Object = MibScalar
chasIpAddrToPing = _ChasIpAddrToPing_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 1, 9),
    _ChasIpAddrToPing_Type()
)
chasIpAddrToPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasIpAddrToPing.setStatus("mandatory")


class _ChasDupMacSupport_Type(Integer32):
    """Custom type chasDupMacSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ChasDupMacSupport_Type.__name__ = "Integer32"
_ChasDupMacSupport_Object = MibScalar
chasDupMacSupport = _ChasDupMacSupport_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 1, 10),
    _ChasDupMacSupport_Type()
)
chasDupMacSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasDupMacSupport.setStatus("mandatory")


class _ChasNewDupMacSupport_Type(Integer32):
    """Custom type chasNewDupMacSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ChasNewDupMacSupport_Type.__name__ = "Integer32"
_ChasNewDupMacSupport_Object = MibScalar
chasNewDupMacSupport = _ChasNewDupMacSupport_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 1, 11),
    _ChasNewDupMacSupport_Type()
)
chasNewDupMacSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasNewDupMacSupport.setStatus("mandatory")
_ChasSonetMonitoring_Type = Integer32
_ChasSonetMonitoring_Object = MibScalar
chasSonetMonitoring = _ChasSonetMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 1, 12),
    _ChasSonetMonitoring_Type()
)
chasSonetMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSonetMonitoring.setStatus("mandatory")
_ChasVbusMode_Type = Integer32
_ChasVbusMode_Object = MibScalar
chasVbusMode = _ChasVbusMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 1, 13),
    _ChasVbusMode_Type()
)
chasVbusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasVbusMode.setStatus("mandatory")
_ChasPhysical_ObjectIdentity = ObjectIdentity
chasPhysical = _ChasPhysical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2)
)
_ChasModuleTable_Object = MibTable
chasModuleTable = _ChasModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    chasModuleTable.setStatus("mandatory")
_ChasModuleEntry_Object = MibTableRow
chasModuleEntry = _ChasModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1)
)
chasModuleEntry.setIndexNames(
    (0, "CHASSIS-MIB", "chasModuleSlot"),
    (0, "CHASSIS-MIB", "chasModuleSubUnit"),
)
if mibBuilder.loadTexts:
    chasModuleEntry.setStatus("mandatory")
_ChasModuleSlot_Type = Integer32
_ChasModuleSlot_Object = MibTableColumn
chasModuleSlot = _ChasModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 1),
    _ChasModuleSlot_Type()
)
chasModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleSlot.setStatus("mandatory")
_ChasModuleSubUnit_Type = XylanModuleSubunit
_ChasModuleSubUnit_Object = MibTableColumn
chasModuleSubUnit = _ChasModuleSubUnit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 2),
    _ChasModuleSubUnit_Type()
)
chasModuleSubUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleSubUnit.setStatus("mandatory")
_ChasModuleType_Type = XylanModuleType
_ChasModuleType_Object = MibTableColumn
chasModuleType = _ChasModuleType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 3),
    _ChasModuleType_Type()
)
chasModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleType.setStatus("mandatory")


class _ChasModulePartNum_Type(DisplayString):
    """Custom type chasModulePartNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_ChasModulePartNum_Type.__name__ = "DisplayString"
_ChasModulePartNum_Object = MibTableColumn
chasModulePartNum = _ChasModulePartNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 4),
    _ChasModulePartNum_Type()
)
chasModulePartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModulePartNum.setStatus("mandatory")


class _ChasModuleDescription_Type(DisplayString):
    """Custom type chasModuleDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ChasModuleDescription_Type.__name__ = "DisplayString"
_ChasModuleDescription_Object = MibTableColumn
chasModuleDescription = _ChasModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 5),
    _ChasModuleDescription_Type()
)
chasModuleDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasModuleDescription.setStatus("mandatory")


class _ChasModuleHwRevision_Type(Integer32):
    """Custom type chasModuleHwRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ChasModuleHwRevision_Type.__name__ = "Integer32"
_ChasModuleHwRevision_Object = MibTableColumn
chasModuleHwRevision = _ChasModuleHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 6),
    _ChasModuleHwRevision_Type()
)
chasModuleHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleHwRevision.setStatus("mandatory")


class _ChasModuleHwModLevel_Type(Integer32):
    """Custom type chasModuleHwModLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ChasModuleHwModLevel_Type.__name__ = "Integer32"
_ChasModuleHwModLevel_Object = MibTableColumn
chasModuleHwModLevel = _ChasModuleHwModLevel_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 7),
    _ChasModuleHwModLevel_Type()
)
chasModuleHwModLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleHwModLevel.setStatus("mandatory")


class _ChasModuleSerialNumber_Type(DisplayString):
    """Custom type chasModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_ChasModuleSerialNumber_Type.__name__ = "DisplayString"
_ChasModuleSerialNumber_Object = MibTableColumn
chasModuleSerialNumber = _ChasModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 8),
    _ChasModuleSerialNumber_Type()
)
chasModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleSerialNumber.setStatus("mandatory")


class _ChasModuleMfgDate_Type(DisplayString):
    """Custom type chasModuleMfgDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ChasModuleMfgDate_Type.__name__ = "DisplayString"
_ChasModuleMfgDate_Object = MibTableColumn
chasModuleMfgDate = _ChasModuleMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 9),
    _ChasModuleMfgDate_Type()
)
chasModuleMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleMfgDate.setStatus("mandatory")


class _ChasModuleFwVersion_Type(DisplayString):
    """Custom type chasModuleFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ChasModuleFwVersion_Type.__name__ = "DisplayString"
_ChasModuleFwVersion_Object = MibTableColumn
chasModuleFwVersion = _ChasModuleFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 10),
    _ChasModuleFwVersion_Type()
)
chasModuleFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleFwVersion.setStatus("mandatory")
_ChasModuleBaseMacAddress_Type = MacAddress
_ChasModuleBaseMacAddress_Object = MibTableColumn
chasModuleBaseMacAddress = _ChasModuleBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 11),
    _ChasModuleBaseMacAddress_Type()
)
chasModuleBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleBaseMacAddress.setStatus("mandatory")
_ChasModuleTimeStamp_Type = TimeTicks
_ChasModuleTimeStamp_Object = MibTableColumn
chasModuleTimeStamp = _ChasModuleTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 12),
    _ChasModuleTimeStamp_Type()
)
chasModuleTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleTimeStamp.setStatus("mandatory")


class _ChasModuleAdminStatus_Type(Integer32):
    """Custom type chasModuleAdminStatus based on Integer32"""
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
        *(("disable", 4),
          ("enable", 3),
          ("invalid", 2),
          ("load", 6),
          ("reset", 5),
          ("test", 7),
          ("unknown", 1))
    )


_ChasModuleAdminStatus_Type.__name__ = "Integer32"
_ChasModuleAdminStatus_Object = MibTableColumn
chasModuleAdminStatus = _ChasModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 13),
    _ChasModuleAdminStatus_Type()
)
chasModuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasModuleAdminStatus.setStatus("mandatory")


class _ChasModuleOperStatus_Type(Integer32):
    """Custom type chasModuleOperStatus based on Integer32"""
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
        *(("disabled", 4),
          ("fatalError", 10),
          ("invalid", 2),
          ("loadInProgress", 6),
          ("nonFatalError", 9),
          ("operational", 3),
          ("resetInProgress", 5),
          ("testing", 7),
          ("unknown", 1),
          ("warning", 8))
    )


_ChasModuleOperStatus_Type.__name__ = "Integer32"
_ChasModuleOperStatus_Object = MibTableColumn
chasModuleOperStatus = _ChasModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 14),
    _ChasModuleOperStatus_Type()
)
chasModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleOperStatus.setStatus("mandatory")
_ChasModuleLedStatus_Type = Integer32
_ChasModuleLedStatus_Object = MibTableColumn
chasModuleLedStatus = _ChasModuleLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 15),
    _ChasModuleLedStatus_Type()
)
chasModuleLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleLedStatus.setStatus("mandatory")
_ChasModuleVbusTxDiscards_Type = Counter32
_ChasModuleVbusTxDiscards_Object = MibTableColumn
chasModuleVbusTxDiscards = _ChasModuleVbusTxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 16),
    _ChasModuleVbusTxDiscards_Type()
)
chasModuleVbusTxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleVbusTxDiscards.setStatus("mandatory")
_ChasModuleVbusRxDiscards_Type = Counter32
_ChasModuleVbusRxDiscards_Object = MibTableColumn
chasModuleVbusRxDiscards = _ChasModuleVbusRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 17),
    _ChasModuleVbusRxDiscards_Type()
)
chasModuleVbusRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleVbusRxDiscards.setStatus("mandatory")


class _ChasModuleLedStatusExtend_Type(OctetString):
    """Custom type chasModuleLedStatusExtend based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ChasModuleLedStatusExtend_Type.__name__ = "OctetString"
_ChasModuleLedStatusExtend_Object = MibTableColumn
chasModuleLedStatusExtend = _ChasModuleLedStatusExtend_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 2, 1, 1, 18),
    _ChasModuleLedStatusExtend_Type()
)
chasModuleLedStatusExtend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasModuleLedStatusExtend.setStatus("mandatory")
_ChasController_ObjectIdentity = ObjectIdentity
chasController = _ChasController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3)
)
_ChasControlTable_Object = MibTable
chasControlTable = _ChasControlTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    chasControlTable.setStatus("mandatory")
_ChasControlEntry_Object = MibTableRow
chasControlEntry = _ChasControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1)
)
chasControlEntry.setIndexNames(
    (0, "CHASSIS-MIB", "chasControlSlot"),
)
if mibBuilder.loadTexts:
    chasControlEntry.setStatus("mandatory")
_ChasControlSlot_Type = Integer32
_ChasControlSlot_Object = MibTableColumn
chasControlSlot = _ChasControlSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 1),
    _ChasControlSlot_Type()
)
chasControlSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlSlot.setStatus("mandatory")
_ChasControlState_Type = XylanMPMStateType
_ChasControlState_Object = MibTableColumn
chasControlState = _ChasControlState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 2),
    _ChasControlState_Type()
)
chasControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlState.setStatus("mandatory")
_ChasControlDCEPortRate_Type = XylanSerialPortSpeed
_ChasControlDCEPortRate_Object = MibTableColumn
chasControlDCEPortRate = _ChasControlDCEPortRate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 3),
    _ChasControlDCEPortRate_Type()
)
chasControlDCEPortRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlDCEPortRate.setStatus("mandatory")


class _ChasControlDCEWordSize_Type(Integer32):
    """Custom type chasControlDCEWordSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 8),
    )


_ChasControlDCEWordSize_Type.__name__ = "Integer32"
_ChasControlDCEWordSize_Object = MibTableColumn
chasControlDCEWordSize = _ChasControlDCEWordSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 4),
    _ChasControlDCEWordSize_Type()
)
chasControlDCEWordSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlDCEWordSize.setStatus("mandatory")


class _ChasControlDCEStopBits_Type(Integer32):
    """Custom type chasControlDCEStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ChasControlDCEStopBits_Type.__name__ = "Integer32"
_ChasControlDCEStopBits_Object = MibTableColumn
chasControlDCEStopBits = _ChasControlDCEStopBits_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 5),
    _ChasControlDCEStopBits_Type()
)
chasControlDCEStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlDCEStopBits.setStatus("mandatory")
_ChasControlDCEParity_Type = XylanSerialPortParity
_ChasControlDCEParity_Object = MibTableColumn
chasControlDCEParity = _ChasControlDCEParity_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 6),
    _ChasControlDCEParity_Type()
)
chasControlDCEParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlDCEParity.setStatus("mandatory")
_ChasControlDTEPortRate_Type = XylanSerialPortSpeed
_ChasControlDTEPortRate_Object = MibTableColumn
chasControlDTEPortRate = _ChasControlDTEPortRate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 7),
    _ChasControlDTEPortRate_Type()
)
chasControlDTEPortRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlDTEPortRate.setStatus("mandatory")


class _ChasControlDTEWordSize_Type(Integer32):
    """Custom type chasControlDTEWordSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 8),
    )


_ChasControlDTEWordSize_Type.__name__ = "Integer32"
_ChasControlDTEWordSize_Object = MibTableColumn
chasControlDTEWordSize = _ChasControlDTEWordSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 8),
    _ChasControlDTEWordSize_Type()
)
chasControlDTEWordSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlDTEWordSize.setStatus("mandatory")


class _ChasControlDTEStopBits_Type(Integer32):
    """Custom type chasControlDTEStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ChasControlDTEStopBits_Type.__name__ = "Integer32"
_ChasControlDTEStopBits_Object = MibTableColumn
chasControlDTEStopBits = _ChasControlDTEStopBits_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 9),
    _ChasControlDTEStopBits_Type()
)
chasControlDTEStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlDTEStopBits.setStatus("mandatory")
_ChasControlDTEParity_Type = XylanSerialPortParity
_ChasControlDTEParity_Object = MibTableColumn
chasControlDTEParity = _ChasControlDTEParity_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 10),
    _ChasControlDTEParity_Type()
)
chasControlDTEParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlDTEParity.setStatus("mandatory")
_ChasControlIPAdd_Type = IpAddress
_ChasControlIPAdd_Object = MibTableColumn
chasControlIPAdd = _ChasControlIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 11),
    _ChasControlIPAdd_Type()
)
chasControlIPAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlIPAdd.setStatus("mandatory")


class _ChasControlBootCode_Type(DisplayString):
    """Custom type chasControlBootCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasControlBootCode_Type.__name__ = "DisplayString"
_ChasControlBootCode_Object = MibTableColumn
chasControlBootCode = _ChasControlBootCode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 12),
    _ChasControlBootCode_Type()
)
chasControlBootCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlBootCode.setStatus("mandatory")
_ChasControlFreeFFS_Type = Integer32
_ChasControlFreeFFS_Object = MibTableColumn
chasControlFreeFFS = _ChasControlFreeFFS_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 13),
    _ChasControlFreeFFS_Type()
)
chasControlFreeFFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlFreeFFS.setStatus("mandatory")
_ChasControlFreeBuffers_Type = Integer32
_ChasControlFreeBuffers_Object = MibTableColumn
chasControlFreeBuffers = _ChasControlFreeBuffers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 14),
    _ChasControlFreeBuffers_Type()
)
chasControlFreeBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlFreeBuffers.setStatus("mandatory")
_ChasControlBufferUtilization_Type = Gauge32
_ChasControlBufferUtilization_Object = MibTableColumn
chasControlBufferUtilization = _ChasControlBufferUtilization_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 15),
    _ChasControlBufferUtilization_Type()
)
chasControlBufferUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlBufferUtilization.setStatus("mandatory")
_ChasControlCPUUtilization_Type = Gauge32
_ChasControlCPUUtilization_Object = MibTableColumn
chasControlCPUUtilization = _ChasControlCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 16),
    _ChasControlCPUUtilization_Type()
)
chasControlCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlCPUUtilization.setStatus("mandatory")


class _ChasControlImageSuffix_Type(DisplayString):
    """Custom type chasControlImageSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_ChasControlImageSuffix_Type.__name__ = "DisplayString"
_ChasControlImageSuffix_Object = MibTableColumn
chasControlImageSuffix = _ChasControlImageSuffix_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 17),
    _ChasControlImageSuffix_Type()
)
chasControlImageSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlImageSuffix.setStatus("mandatory")
_ChasControlImageSyncStatus_Type = XylanImageSyncStatus
_ChasControlImageSyncStatus_Object = MibTableColumn
chasControlImageSyncStatus = _ChasControlImageSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 18),
    _ChasControlImageSyncStatus_Type()
)
chasControlImageSyncStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlImageSyncStatus.setStatus("mandatory")
_ChasControlConfigSyncStatus_Type = XylanConfigSyncStatus
_ChasControlConfigSyncStatus_Object = MibTableColumn
chasControlConfigSyncStatus = _ChasControlConfigSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 19),
    _ChasControlConfigSyncStatus_Type()
)
chasControlConfigSyncStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlConfigSyncStatus.setStatus("mandatory")
_ChasControlConfigSyncEnable_Type = XylanConfigSyncEnable
_ChasControlConfigSyncEnable_Object = MibTableColumn
chasControlConfigSyncEnable = _ChasControlConfigSyncEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 20),
    _ChasControlConfigSyncEnable_Type()
)
chasControlConfigSyncEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlConfigSyncEnable.setStatus("mandatory")
_ChasControlDCEPortMode_Type = XylanSerialPortMode
_ChasControlDCEPortMode_Object = MibTableColumn
chasControlDCEPortMode = _ChasControlDCEPortMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 21),
    _ChasControlDCEPortMode_Type()
)
chasControlDCEPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlDCEPortMode.setStatus("mandatory")
_ChasControlDTEPortMode_Type = XylanSerialPortMode
_ChasControlDTEPortMode_Object = MibTableColumn
chasControlDTEPortMode = _ChasControlDTEPortMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 22),
    _ChasControlDTEPortMode_Type()
)
chasControlDTEPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlDTEPortMode.setStatus("mandatory")
_ChasControlEthPortIPAddr_Type = IpAddress
_ChasControlEthPortIPAddr_Object = MibTableColumn
chasControlEthPortIPAddr = _ChasControlEthPortIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 23),
    _ChasControlEthPortIPAddr_Type()
)
chasControlEthPortIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlEthPortIPAddr.setStatus("mandatory")
_ChasControlEthPortSubMask_Type = IpAddress
_ChasControlEthPortSubMask_Object = MibTableColumn
chasControlEthPortSubMask = _ChasControlEthPortSubMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 24),
    _ChasControlEthPortSubMask_Type()
)
chasControlEthPortSubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlEthPortSubMask.setStatus("mandatory")
_ChasControlEthPortBcast_Type = IpAddress
_ChasControlEthPortBcast_Object = MibTableColumn
chasControlEthPortBcast = _ChasControlEthPortBcast_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 25),
    _ChasControlEthPortBcast_Type()
)
chasControlEthPortBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlEthPortBcast.setStatus("mandatory")
_ChasControlEthPortGateWay_Type = IpAddress
_ChasControlEthPortGateWay_Object = MibTableColumn
chasControlEthPortGateWay = _ChasControlEthPortGateWay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 26),
    _ChasControlEthPortGateWay_Type()
)
chasControlEthPortGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlEthPortGateWay.setStatus("mandatory")


class _ChasControlEthPortRipMode_Type(Integer32):
    """Custom type chasControlEthPortRipMode based on Integer32"""
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
        *(("active", 3),
          ("deaf", 2),
          ("inactive", 4),
          ("silent", 1))
    )


_ChasControlEthPortRipMode_Type.__name__ = "Integer32"
_ChasControlEthPortRipMode_Object = MibTableColumn
chasControlEthPortRipMode = _ChasControlEthPortRipMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 27),
    _ChasControlEthPortRipMode_Type()
)
chasControlEthPortRipMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlEthPortRipMode.setStatus("mandatory")
_ChasControlEthPortRemoteHost_Type = IpAddress
_ChasControlEthPortRemoteHost_Object = MibTableColumn
chasControlEthPortRemoteHost = _ChasControlEthPortRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 28),
    _ChasControlEthPortRemoteHost_Type()
)
chasControlEthPortRemoteHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlEthPortRemoteHost.setStatus("mandatory")
_ChasControlEthPortRemoteMask_Type = IpAddress
_ChasControlEthPortRemoteMask_Object = MibTableColumn
chasControlEthPortRemoteMask = _ChasControlEthPortRemoteMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 1, 1, 29),
    _ChasControlEthPortRemoteMask_Type()
)
chasControlEthPortRemoteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlEthPortRemoteMask.setStatus("mandatory")
_ChasControlFFSTable_Object = MibTable
chasControlFFSTable = _ChasControlFFSTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    chasControlFFSTable.setStatus("mandatory")
_ChasControlFFSEntry_Object = MibTableRow
chasControlFFSEntry = _ChasControlFFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 2, 1)
)
chasControlFFSEntry.setIndexNames(
    (0, "CHASSIS-MIB", "chasControlFFSFileSlot"),
    (0, "CHASSIS-MIB", "chasControlFFSFileNameCks"),
)
if mibBuilder.loadTexts:
    chasControlFFSEntry.setStatus("mandatory")
_ChasControlFFSFileSlot_Type = Integer32
_ChasControlFFSFileSlot_Object = MibTableColumn
chasControlFFSFileSlot = _ChasControlFFSFileSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 2, 1, 1),
    _ChasControlFFSFileSlot_Type()
)
chasControlFFSFileSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlFFSFileSlot.setStatus("mandatory")
_ChasControlFFSFileNameCks_Type = Integer32
_ChasControlFFSFileNameCks_Object = MibTableColumn
chasControlFFSFileNameCks = _ChasControlFFSFileNameCks_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 2, 1, 2),
    _ChasControlFFSFileNameCks_Type()
)
chasControlFFSFileNameCks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlFFSFileNameCks.setStatus("mandatory")


class _ChasControlFFSFileName_Type(DisplayString):
    """Custom type chasControlFFSFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ChasControlFFSFileName_Type.__name__ = "DisplayString"
_ChasControlFFSFileName_Object = MibTableColumn
chasControlFFSFileName = _ChasControlFFSFileName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 2, 1, 3),
    _ChasControlFFSFileName_Type()
)
chasControlFFSFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlFFSFileName.setStatus("mandatory")
_ChasControlFFSFileSize_Type = Integer32
_ChasControlFFSFileSize_Object = MibTableColumn
chasControlFFSFileSize = _ChasControlFFSFileSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 2, 1, 4),
    _ChasControlFFSFileSize_Type()
)
chasControlFFSFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlFFSFileSize.setStatus("mandatory")
_ChasControlFFSFileDate_Type = TimeTicks
_ChasControlFFSFileDate_Object = MibTableColumn
chasControlFFSFileDate = _ChasControlFFSFileDate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 2, 1, 5),
    _ChasControlFFSFileDate_Type()
)
chasControlFFSFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlFFSFileDate.setStatus("mandatory")
_ChasControlFFSFileAction_Type = XylanFFSFileAction
_ChasControlFFSFileAction_Object = MibTableColumn
chasControlFFSFileAction = _ChasControlFFSFileAction_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 2, 1, 6),
    _ChasControlFFSFileAction_Type()
)
chasControlFFSFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlFFSFileAction.setStatus("mandatory")
_ChasControlFFSActionStatus_ObjectIdentity = ObjectIdentity
chasControlFFSActionStatus = _ChasControlFFSActionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 3)
)
_ChasControlLastFFSAction_Type = XylanFFSFileAction
_ChasControlLastFFSAction_Object = MibScalar
chasControlLastFFSAction = _ChasControlLastFFSAction_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 3, 1),
    _ChasControlLastFFSAction_Type()
)
chasControlLastFFSAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlLastFFSAction.setStatus("mandatory")
_ChasControlLastFFSActionSlot_Type = Integer32
_ChasControlLastFFSActionSlot_Object = MibScalar
chasControlLastFFSActionSlot = _ChasControlLastFFSActionSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 3, 2),
    _ChasControlLastFFSActionSlot_Type()
)
chasControlLastFFSActionSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlLastFFSActionSlot.setStatus("mandatory")


class _ChasControlLastFFSActionFileName_Type(DisplayString):
    """Custom type chasControlLastFFSActionFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ChasControlLastFFSActionFileName_Type.__name__ = "DisplayString"
_ChasControlLastFFSActionFileName_Object = MibScalar
chasControlLastFFSActionFileName = _ChasControlLastFFSActionFileName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 3, 3),
    _ChasControlLastFFSActionFileName_Type()
)
chasControlLastFFSActionFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlLastFFSActionFileName.setStatus("mandatory")
_ChasControlLastFFSActionDate_Type = TimeTicks
_ChasControlLastFFSActionDate_Object = MibScalar
chasControlLastFFSActionDate = _ChasControlLastFFSActionDate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 3, 4),
    _ChasControlLastFFSActionDate_Type()
)
chasControlLastFFSActionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlLastFFSActionDate.setStatus("mandatory")
_ChasControlLastFFSActionSource_Type = IpAddress
_ChasControlLastFFSActionSource_Object = MibScalar
chasControlLastFFSActionSource = _ChasControlLastFFSActionSource_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 3, 5),
    _ChasControlLastFFSActionSource_Type()
)
chasControlLastFFSActionSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlLastFFSActionSource.setStatus("mandatory")
_ChasControlLastFFSActionStatus_Type = XylanFFSFileActionStatus
_ChasControlLastFFSActionStatus_Object = MibScalar
chasControlLastFFSActionStatus = _ChasControlLastFFSActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 3, 3, 6),
    _ChasControlLastFFSActionStatus_Type()
)
chasControlLastFFSActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlLastFFSActionStatus.setStatus("mandatory")
_ChasPowerSupply_ObjectIdentity = ObjectIdentity
chasPowerSupply = _ChasPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 4)
)
_ChasPowerSupply1State_Type = XylanPSStateType
_ChasPowerSupply1State_Object = MibScalar
chasPowerSupply1State = _ChasPowerSupply1State_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 4, 1),
    _ChasPowerSupply1State_Type()
)
chasPowerSupply1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerSupply1State.setStatus("mandatory")
_ChasPowerSupply2State_Type = XylanPSStateType
_ChasPowerSupply2State_Object = MibScalar
chasPowerSupply2State = _ChasPowerSupply2State_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 4, 2),
    _ChasPowerSupply2State_Type()
)
chasPowerSupply2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerSupply2State.setStatus("mandatory")
_ChasEnvmnt_ObjectIdentity = ObjectIdentity
chasEnvmnt = _ChasEnvmnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 5)
)
_ChasEnvrmnt1TempRange1_Type = XylanTempStateType
_ChasEnvrmnt1TempRange1_Object = MibScalar
chasEnvrmnt1TempRange1 = _ChasEnvrmnt1TempRange1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 5, 1),
    _ChasEnvrmnt1TempRange1_Type()
)
chasEnvrmnt1TempRange1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEnvrmnt1TempRange1.setStatus("mandatory")
_ChasEnvrmnt1TempRange2_Type = XylanTempStateType
_ChasEnvrmnt1TempRange2_Object = MibScalar
chasEnvrmnt1TempRange2 = _ChasEnvrmnt1TempRange2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 5, 2),
    _ChasEnvrmnt1TempRange2_Type()
)
chasEnvrmnt1TempRange2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEnvrmnt1TempRange2.setStatus("mandatory")
_ChasEnvrmnt2TempRange1_Type = XylanTempStateType
_ChasEnvrmnt2TempRange1_Object = MibScalar
chasEnvrmnt2TempRange1 = _ChasEnvrmnt2TempRange1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 5, 3),
    _ChasEnvrmnt2TempRange1_Type()
)
chasEnvrmnt2TempRange1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEnvrmnt2TempRange1.setStatus("mandatory")
_ChasEnvrmnt2TempRange2_Type = XylanTempStateType
_ChasEnvrmnt2TempRange2_Object = MibScalar
chasEnvrmnt2TempRange2 = _ChasEnvrmnt2TempRange2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 5, 4),
    _ChasEnvrmnt2TempRange2_Type()
)
chasEnvrmnt2TempRange2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEnvrmnt2TempRange2.setStatus("mandatory")
_ChasStatus_ObjectIdentity = ObjectIdentity
chasStatus = _ChasStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 6)
)


class _ChasXylanOpaque_Type(OctetString):
    """Custom type chasXylanOpaque based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(252, 252),
    )


_ChasXylanOpaque_Type.__name__ = "OctetString"
_ChasXylanOpaque_Object = MibScalar
chasXylanOpaque = _ChasXylanOpaque_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 6, 1),
    _ChasXylanOpaque_Type()
)
chasXylanOpaque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasXylanOpaque.setStatus("mandatory")


class _ChasXylanCompaq_Type(OctetString):
    """Custom type chasXylanCompaq based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(310, 310),
    )


_ChasXylanCompaq_Type.__name__ = "OctetString"
_ChasXylanCompaq_Object = MibScalar
chasXylanCompaq = _ChasXylanCompaq_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 6, 2),
    _ChasXylanCompaq_Type()
)
chasXylanCompaq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasXylanCompaq.setStatus("mandatory")


class _ChasXylanPollData_Type(OctetString):
    """Custom type chasXylanPollData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(388, 388),
    )


_ChasXylanPollData_Type.__name__ = "OctetString"
_ChasXylanPollData_Object = MibScalar
chasXylanPollData = _ChasXylanPollData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 6, 3),
    _ChasXylanPollData_Type()
)
chasXylanPollData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasXylanPollData.setStatus("mandatory")
_ChasAccounting_ObjectIdentity = ObjectIdentity
chasAccounting = _ChasAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7)
)
_ChasAccountCdrCount_Type = Integer32
_ChasAccountCdrCount_Object = MibScalar
chasAccountCdrCount = _ChasAccountCdrCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 1),
    _ChasAccountCdrCount_Type()
)
chasAccountCdrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasAccountCdrCount.setStatus("mandatory")


class _ChasAccountMethodInUse_Type(Integer32):
    """Custom type chasAccountMethodInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("disk", 3),
          ("wire", 2))
    )


_ChasAccountMethodInUse_Type.__name__ = "Integer32"
_ChasAccountMethodInUse_Object = MibScalar
chasAccountMethodInUse = _ChasAccountMethodInUse_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 2),
    _ChasAccountMethodInUse_Type()
)
chasAccountMethodInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasAccountMethodInUse.setStatus("mandatory")
_ChasAccountDeviceInUse_Type = IpAddress
_ChasAccountDeviceInUse_Object = MibScalar
chasAccountDeviceInUse = _ChasAccountDeviceInUse_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 3),
    _ChasAccountDeviceInUse_Type()
)
chasAccountDeviceInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasAccountDeviceInUse.setStatus("mandatory")
_ChasAccountMaxCnxInUse_Type = Integer32
_ChasAccountMaxCnxInUse_Object = MibScalar
chasAccountMaxCnxInUse = _ChasAccountMaxCnxInUse_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 4),
    _ChasAccountMaxCnxInUse_Type()
)
chasAccountMaxCnxInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasAccountMaxCnxInUse.setStatus("mandatory")
_ChasAccountCdrNext_Type = Integer32
_ChasAccountCdrNext_Object = MibScalar
chasAccountCdrNext = _ChasAccountCdrNext_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 5),
    _ChasAccountCdrNext_Type()
)
chasAccountCdrNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasAccountCdrNext.setStatus("mandatory")
_ChasAccountFileCount_Type = Integer32
_ChasAccountFileCount_Object = MibScalar
chasAccountFileCount = _ChasAccountFileCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 6),
    _ChasAccountFileCount_Type()
)
chasAccountFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasAccountFileCount.setStatus("mandatory")


class _ChasAccountPollCycle_Type(Integer32):
    """Custom type chasAccountPollCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("polling", 2),
          ("waiting", 1))
    )


_ChasAccountPollCycle_Type.__name__ = "Integer32"
_ChasAccountPollCycle_Object = MibScalar
chasAccountPollCycle = _ChasAccountPollCycle_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 7),
    _ChasAccountPollCycle_Type()
)
chasAccountPollCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasAccountPollCycle.setStatus("mandatory")


class _ChasAccountConnectState_Type(Integer32):
    """Custom type chasAccountConnectState based on Integer32"""
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
        *(("closeHold", 6),
          ("closed", 1),
          ("open", 2),
          ("openAlternate", 5),
          ("openAlternateHold", 4),
          ("openHold", 3),
          ("unused", 0))
    )


_ChasAccountConnectState_Type.__name__ = "Integer32"
_ChasAccountConnectState_Object = MibScalar
chasAccountConnectState = _ChasAccountConnectState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 8),
    _ChasAccountConnectState_Type()
)
chasAccountConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasAccountConnectState.setStatus("mandatory")


class _ChasAccountMethod_Type(Integer32):
    """Custom type chasAccountMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("disk", 3),
          ("wire", 2))
    )


_ChasAccountMethod_Type.__name__ = "Integer32"
_ChasAccountMethod_Object = MibScalar
chasAccountMethod = _ChasAccountMethod_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 9),
    _ChasAccountMethod_Type()
)
chasAccountMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountMethod.setStatus("mandatory")
_ChasAccountDevicePrimary_Type = IpAddress
_ChasAccountDevicePrimary_Object = MibScalar
chasAccountDevicePrimary = _ChasAccountDevicePrimary_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 10),
    _ChasAccountDevicePrimary_Type()
)
chasAccountDevicePrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountDevicePrimary.setStatus("mandatory")
_ChasAccountDeviceSecondary_Type = IpAddress
_ChasAccountDeviceSecondary_Object = MibScalar
chasAccountDeviceSecondary = _ChasAccountDeviceSecondary_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 11),
    _ChasAccountDeviceSecondary_Type()
)
chasAccountDeviceSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountDeviceSecondary.setStatus("mandatory")
_ChasAccountDevicePort_Type = Integer32
_ChasAccountDevicePort_Object = MibScalar
chasAccountDevicePort = _ChasAccountDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 12),
    _ChasAccountDevicePort_Type()
)
chasAccountDevicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountDevicePort.setStatus("mandatory")


class _ChasAccountPeriods_Type(OctetString):
    """Custom type chasAccountPeriods based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ChasAccountPeriods_Type.__name__ = "OctetString"
_ChasAccountPeriods_Object = MibScalar
chasAccountPeriods = _ChasAccountPeriods_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 13),
    _ChasAccountPeriods_Type()
)
chasAccountPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountPeriods.setStatus("mandatory")


class _ChasAccountInterval_Type(Integer32):
    """Custom type chasAccountInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              8,
              12,
              48)
        )
    )
    namedValues = NamedValues(
        *(("hourly", 4),
          ("three-hours", 12),
          ("twice-daily", 48),
          ("two-hours", 8))
    )


_ChasAccountInterval_Type.__name__ = "Integer32"
_ChasAccountInterval_Object = MibScalar
chasAccountInterval = _ChasAccountInterval_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 14),
    _ChasAccountInterval_Type()
)
chasAccountInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountInterval.setStatus("mandatory")
_ChasAccountChargedServices_Type = Integer32
_ChasAccountChargedServices_Object = MibScalar
chasAccountChargedServices = _ChasAccountChargedServices_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 15),
    _ChasAccountChargedServices_Type()
)
chasAccountChargedServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountChargedServices.setStatus("mandatory")


class _ChasAccountMaxCnx_Type(Integer32):
    """Custom type chasAccountMaxCnx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_ChasAccountMaxCnx_Type.__name__ = "Integer32"
_ChasAccountMaxCnx_Object = MibScalar
chasAccountMaxCnx = _ChasAccountMaxCnx_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 16),
    _ChasAccountMaxCnx_Type()
)
chasAccountMaxCnx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountMaxCnx.setStatus("mandatory")


class _ChasAccountFillingLevel_Type(Integer32):
    """Custom type chasAccountFillingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChasAccountFillingLevel_Type.__name__ = "Integer32"
_ChasAccountFillingLevel_Object = MibScalar
chasAccountFillingLevel = _ChasAccountFillingLevel_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 17),
    _ChasAccountFillingLevel_Type()
)
chasAccountFillingLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasAccountFillingLevel.setStatus("mandatory")


class _ChasAccountThreshold1_Type(Integer32):
    """Custom type chasAccountThreshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_ChasAccountThreshold1_Type.__name__ = "Integer32"
_ChasAccountThreshold1_Object = MibScalar
chasAccountThreshold1 = _ChasAccountThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 18),
    _ChasAccountThreshold1_Type()
)
chasAccountThreshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountThreshold1.setStatus("mandatory")


class _ChasAccountThreshold2_Type(Integer32):
    """Custom type chasAccountThreshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 80),
    )


_ChasAccountThreshold2_Type.__name__ = "Integer32"
_ChasAccountThreshold2_Object = MibScalar
chasAccountThreshold2 = _ChasAccountThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 19),
    _ChasAccountThreshold2_Type()
)
chasAccountThreshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountThreshold2.setStatus("mandatory")


class _ChasAccountThreshold3_Type(Integer32):
    """Custom type chasAccountThreshold3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 95),
    )


_ChasAccountThreshold3_Type.__name__ = "Integer32"
_ChasAccountThreshold3_Object = MibScalar
chasAccountThreshold3 = _ChasAccountThreshold3_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 20),
    _ChasAccountThreshold3_Type()
)
chasAccountThreshold3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountThreshold3.setStatus("mandatory")


class _ChasAccountTcpWriteTimer_Type(Integer32):
    """Custom type chasAccountTcpWriteTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ChasAccountTcpWriteTimer_Type.__name__ = "Integer32"
_ChasAccountTcpWriteTimer_Object = MibScalar
chasAccountTcpWriteTimer = _ChasAccountTcpWriteTimer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 21),
    _ChasAccountTcpWriteTimer_Type()
)
chasAccountTcpWriteTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountTcpWriteTimer.setStatus("mandatory")


class _ChasAccountHoldDownTimer_Type(Integer32):
    """Custom type chasAccountHoldDownTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_ChasAccountHoldDownTimer_Type.__name__ = "Integer32"
_ChasAccountHoldDownTimer_Object = MibScalar
chasAccountHoldDownTimer = _ChasAccountHoldDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 22),
    _ChasAccountHoldDownTimer_Type()
)
chasAccountHoldDownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountHoldDownTimer.setStatus("mandatory")
_ChasAccountFileSize_Type = Integer32
_ChasAccountFileSize_Object = MibScalar
chasAccountFileSize = _ChasAccountFileSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 23),
    _ChasAccountFileSize_Type()
)
chasAccountFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountFileSize.setStatus("mandatory")


class _ChasAccountCongStrategy_Type(Integer32):
    """Custom type chasAccountCongStrategy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acceptCalls", 1),
          ("refuseCalls", 2))
    )


_ChasAccountCongStrategy_Type.__name__ = "Integer32"
_ChasAccountCongStrategy_Object = MibScalar
chasAccountCongStrategy = _ChasAccountCongStrategy_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 24),
    _ChasAccountCongStrategy_Type()
)
chasAccountCongStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountCongStrategy.setStatus("mandatory")
_ChasAccountFileCountThreshold_Type = Integer32
_ChasAccountFileCountThreshold_Object = MibScalar
chasAccountFileCountThreshold = _ChasAccountFileCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 25),
    _ChasAccountFileCountThreshold_Type()
)
chasAccountFileCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountFileCountThreshold.setStatus("mandatory")


class _ChasAccountName_Type(OctetString):
    """Custom type chasAccountName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ChasAccountName_Type.__name__ = "OctetString"
_ChasAccountName_Object = MibScalar
chasAccountName = _ChasAccountName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 26),
    _ChasAccountName_Type()
)
chasAccountName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chasAccountName.setStatus("mandatory")


class _ChasAccountMake_Type(Integer32):
    """Custom type chasAccountMake based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ChasAccountMake_Type.__name__ = "Integer32"
_ChasAccountMake_Object = MibScalar
chasAccountMake = _ChasAccountMake_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 27),
    _ChasAccountMake_Type()
)
chasAccountMake.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountMake.setStatus("mandatory")


class _ChasAccountSwitch_Type(Integer32):
    """Custom type chasAccountSwitch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ChasAccountSwitch_Type.__name__ = "Integer32"
_ChasAccountSwitch_Object = MibScalar
chasAccountSwitch = _ChasAccountSwitch_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 7, 28),
    _ChasAccountSwitch_Type()
)
chasAccountSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasAccountSwitch.setStatus("mandatory")
_ChasFanTray_ObjectIdentity = ObjectIdentity
chasFanTray = _ChasFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 8)
)
_ChasFanTray1State_Type = XylanFTStateType
_ChasFanTray1State_Object = MibScalar
chasFanTray1State = _ChasFanTray1State_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 8, 1),
    _ChasFanTray1State_Type()
)
chasFanTray1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasFanTray1State.setStatus("mandatory")
_ChasFanTray2State_Type = XylanFTStateType
_ChasFanTray2State_Object = MibScalar
chasFanTray2State = _ChasFanTray2State_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 8, 2),
    _ChasFanTray2State_Type()
)
chasFanTray2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasFanTray2State.setStatus("mandatory")
_ChasDateAndTime_ObjectIdentity = ObjectIdentity
chasDateAndTime = _ChasDateAndTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 9)
)


class _ChasCurrentDateAndTime_Type(OctetString):
    """Custom type chasCurrentDateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_ChasCurrentDateAndTime_Type.__name__ = "OctetString"
_ChasCurrentDateAndTime_Object = MibScalar
chasCurrentDateAndTime = _ChasCurrentDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 9, 1),
    _ChasCurrentDateAndTime_Type()
)
chasCurrentDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasCurrentDateAndTime.setStatus("mandatory")


class _ChasTimezoneName_Type(DisplayString):
    """Custom type chasTimezoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ChasTimezoneName_Type.__name__ = "DisplayString"
_ChasTimezoneName_Object = MibScalar
chasTimezoneName = _ChasTimezoneName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 9, 2),
    _ChasTimezoneName_Type()
)
chasTimezoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasTimezoneName.setStatus("mandatory")


class _ChasTimezoneOffset_Type(Integer32):
    """Custom type chasTimezoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-780, 720),
    )


_ChasTimezoneOffset_Type.__name__ = "Integer32"
_ChasTimezoneOffset_Object = MibScalar
chasTimezoneOffset = _ChasTimezoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 9, 3),
    _ChasTimezoneOffset_Type()
)
chasTimezoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasTimezoneOffset.setStatus("mandatory")


class _ChasTimezoneDstAdmin_Type(Integer32):
    """Custom type chasTimezoneDstAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ChasTimezoneDstAdmin_Type.__name__ = "Integer32"
_ChasTimezoneDstAdmin_Object = MibScalar
chasTimezoneDstAdmin = _ChasTimezoneDstAdmin_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 9, 4),
    _ChasTimezoneDstAdmin_Type()
)
chasTimezoneDstAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasTimezoneDstAdmin.setStatus("mandatory")


class _ChasTimezoneDst_Type(OctetString):
    """Custom type chasTimezoneDst based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_ChasTimezoneDst_Type.__name__ = "OctetString"
_ChasTimezoneDst_Object = MibScalar
chasTimezoneDst = _ChasTimezoneDst_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 1, 9, 5),
    _ChasTimezoneDst_Type()
)
chasTimezoneDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasTimezoneDst.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHASSIS-MIB",
    **{"XylanChasType": XylanChasType,
       "XylanModuleSubunit": XylanModuleSubunit,
       "XylanModuleType": XylanModuleType,
       "XylanMPMStateType": XylanMPMStateType,
       "XylanPSStateType": XylanPSStateType,
       "XylanTempStateType": XylanTempStateType,
       "XylanImageSyncStatus": XylanImageSyncStatus,
       "XylanConfigSyncStatus": XylanConfigSyncStatus,
       "XylanConfigSyncEnable": XylanConfigSyncEnable,
       "XylanFFSFileAction": XylanFFSFileAction,
       "XylanFFSFileActionStatus": XylanFFSFileActionStatus,
       "XylanSerialPortSpeed": XylanSerialPortSpeed,
       "XylanSerialPortParity": XylanSerialPortParity,
       "XylanSerialPortMode": XylanSerialPortMode,
       "XylanFTStateType": XylanFTStateType,
       "XylanModPortTypes": XylanModPortTypes,
       "chasInfo": chasInfo,
       "chasMake": chasMake,
       "chasType": chasType,
       "chasDescription": chasDescription,
       "chasPhysicalChanges": chasPhysicalChanges,
       "chasLogicalChanges": chasLogicalChanges,
       "chasNoOfResets": chasNoOfResets,
       "chasBaseMacAddress": chasBaseMacAddress,
       "chasFreeSlots": chasFreeSlots,
       "chasIpAddrToPing": chasIpAddrToPing,
       "chasDupMacSupport": chasDupMacSupport,
       "chasNewDupMacSupport": chasNewDupMacSupport,
       "chasSonetMonitoring": chasSonetMonitoring,
       "chasVbusMode": chasVbusMode,
       "chasPhysical": chasPhysical,
       "chasModuleTable": chasModuleTable,
       "chasModuleEntry": chasModuleEntry,
       "chasModuleSlot": chasModuleSlot,
       "chasModuleSubUnit": chasModuleSubUnit,
       "chasModuleType": chasModuleType,
       "chasModulePartNum": chasModulePartNum,
       "chasModuleDescription": chasModuleDescription,
       "chasModuleHwRevision": chasModuleHwRevision,
       "chasModuleHwModLevel": chasModuleHwModLevel,
       "chasModuleSerialNumber": chasModuleSerialNumber,
       "chasModuleMfgDate": chasModuleMfgDate,
       "chasModuleFwVersion": chasModuleFwVersion,
       "chasModuleBaseMacAddress": chasModuleBaseMacAddress,
       "chasModuleTimeStamp": chasModuleTimeStamp,
       "chasModuleAdminStatus": chasModuleAdminStatus,
       "chasModuleOperStatus": chasModuleOperStatus,
       "chasModuleLedStatus": chasModuleLedStatus,
       "chasModuleVbusTxDiscards": chasModuleVbusTxDiscards,
       "chasModuleVbusRxDiscards": chasModuleVbusRxDiscards,
       "chasModuleLedStatusExtend": chasModuleLedStatusExtend,
       "chasController": chasController,
       "chasControlTable": chasControlTable,
       "chasControlEntry": chasControlEntry,
       "chasControlSlot": chasControlSlot,
       "chasControlState": chasControlState,
       "chasControlDCEPortRate": chasControlDCEPortRate,
       "chasControlDCEWordSize": chasControlDCEWordSize,
       "chasControlDCEStopBits": chasControlDCEStopBits,
       "chasControlDCEParity": chasControlDCEParity,
       "chasControlDTEPortRate": chasControlDTEPortRate,
       "chasControlDTEWordSize": chasControlDTEWordSize,
       "chasControlDTEStopBits": chasControlDTEStopBits,
       "chasControlDTEParity": chasControlDTEParity,
       "chasControlIPAdd": chasControlIPAdd,
       "chasControlBootCode": chasControlBootCode,
       "chasControlFreeFFS": chasControlFreeFFS,
       "chasControlFreeBuffers": chasControlFreeBuffers,
       "chasControlBufferUtilization": chasControlBufferUtilization,
       "chasControlCPUUtilization": chasControlCPUUtilization,
       "chasControlImageSuffix": chasControlImageSuffix,
       "chasControlImageSyncStatus": chasControlImageSyncStatus,
       "chasControlConfigSyncStatus": chasControlConfigSyncStatus,
       "chasControlConfigSyncEnable": chasControlConfigSyncEnable,
       "chasControlDCEPortMode": chasControlDCEPortMode,
       "chasControlDTEPortMode": chasControlDTEPortMode,
       "chasControlEthPortIPAddr": chasControlEthPortIPAddr,
       "chasControlEthPortSubMask": chasControlEthPortSubMask,
       "chasControlEthPortBcast": chasControlEthPortBcast,
       "chasControlEthPortGateWay": chasControlEthPortGateWay,
       "chasControlEthPortRipMode": chasControlEthPortRipMode,
       "chasControlEthPortRemoteHost": chasControlEthPortRemoteHost,
       "chasControlEthPortRemoteMask": chasControlEthPortRemoteMask,
       "chasControlFFSTable": chasControlFFSTable,
       "chasControlFFSEntry": chasControlFFSEntry,
       "chasControlFFSFileSlot": chasControlFFSFileSlot,
       "chasControlFFSFileNameCks": chasControlFFSFileNameCks,
       "chasControlFFSFileName": chasControlFFSFileName,
       "chasControlFFSFileSize": chasControlFFSFileSize,
       "chasControlFFSFileDate": chasControlFFSFileDate,
       "chasControlFFSFileAction": chasControlFFSFileAction,
       "chasControlFFSActionStatus": chasControlFFSActionStatus,
       "chasControlLastFFSAction": chasControlLastFFSAction,
       "chasControlLastFFSActionSlot": chasControlLastFFSActionSlot,
       "chasControlLastFFSActionFileName": chasControlLastFFSActionFileName,
       "chasControlLastFFSActionDate": chasControlLastFFSActionDate,
       "chasControlLastFFSActionSource": chasControlLastFFSActionSource,
       "chasControlLastFFSActionStatus": chasControlLastFFSActionStatus,
       "chasPowerSupply": chasPowerSupply,
       "chasPowerSupply1State": chasPowerSupply1State,
       "chasPowerSupply2State": chasPowerSupply2State,
       "chasEnvmnt": chasEnvmnt,
       "chasEnvrmnt1TempRange1": chasEnvrmnt1TempRange1,
       "chasEnvrmnt1TempRange2": chasEnvrmnt1TempRange2,
       "chasEnvrmnt2TempRange1": chasEnvrmnt2TempRange1,
       "chasEnvrmnt2TempRange2": chasEnvrmnt2TempRange2,
       "chasStatus": chasStatus,
       "chasXylanOpaque": chasXylanOpaque,
       "chasXylanCompaq": chasXylanCompaq,
       "chasXylanPollData": chasXylanPollData,
       "chasAccounting": chasAccounting,
       "chasAccountCdrCount": chasAccountCdrCount,
       "chasAccountMethodInUse": chasAccountMethodInUse,
       "chasAccountDeviceInUse": chasAccountDeviceInUse,
       "chasAccountMaxCnxInUse": chasAccountMaxCnxInUse,
       "chasAccountCdrNext": chasAccountCdrNext,
       "chasAccountFileCount": chasAccountFileCount,
       "chasAccountPollCycle": chasAccountPollCycle,
       "chasAccountConnectState": chasAccountConnectState,
       "chasAccountMethod": chasAccountMethod,
       "chasAccountDevicePrimary": chasAccountDevicePrimary,
       "chasAccountDeviceSecondary": chasAccountDeviceSecondary,
       "chasAccountDevicePort": chasAccountDevicePort,
       "chasAccountPeriods": chasAccountPeriods,
       "chasAccountInterval": chasAccountInterval,
       "chasAccountChargedServices": chasAccountChargedServices,
       "chasAccountMaxCnx": chasAccountMaxCnx,
       "chasAccountFillingLevel": chasAccountFillingLevel,
       "chasAccountThreshold1": chasAccountThreshold1,
       "chasAccountThreshold2": chasAccountThreshold2,
       "chasAccountThreshold3": chasAccountThreshold3,
       "chasAccountTcpWriteTimer": chasAccountTcpWriteTimer,
       "chasAccountHoldDownTimer": chasAccountHoldDownTimer,
       "chasAccountFileSize": chasAccountFileSize,
       "chasAccountCongStrategy": chasAccountCongStrategy,
       "chasAccountFileCountThreshold": chasAccountFileCountThreshold,
       "chasAccountName": chasAccountName,
       "chasAccountMake": chasAccountMake,
       "chasAccountSwitch": chasAccountSwitch,
       "chasFanTray": chasFanTray,
       "chasFanTray1State": chasFanTray1State,
       "chasFanTray2State": chasFanTray2State,
       "chasDateAndTime": chasDateAndTime,
       "chasCurrentDateAndTime": chasCurrentDateAndTime,
       "chasTimezoneName": chasTimezoneName,
       "chasTimezoneOffset": chasTimezoneOffset,
       "chasTimezoneDstAdmin": chasTimezoneDstAdmin,
       "chasTimezoneDst": chasTimezoneDst}
)
