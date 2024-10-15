# SNMP MIB module (SYNOPTICS-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYNOPTICS-ROOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:06 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

synoptics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45)
)
synoptics.setRevisions(
        ("2015-05-05 00:00",
         "2015-04-22 00:00",
         "2014-12-11 00:00",
         "2014-11-05 00:00",
         "2014-10-15 00:00",
         "2014-07-30 00:00",
         "2014-05-20 00:00",
         "2014-05-20 00:00",
         "2014-04-04 00:00",
         "2014-03-26 00:00",
         "2014-03-21 00:00",
         "2014-02-14 00:00",
         "2014-01-10 00:00",
         "2013-11-13 00:00",
         "2013-10-29 00:00",
         "2013-10-24 00:00",
         "2013-08-14 00:00",
         "2013-08-05 00:00",
         "2013-06-25 00:00",
         "2013-06-19 00:00",
         "2013-02-04 00:00",
         "2012-10-10 00:00",
         "2012-09-03 00:00",
         "2012-06-05 00:00",
         "2012-06-01 00:00",
         "2011-11-25 00:00",
         "2011-04-28 00:00",
         "2010-12-16 00:00",
         "2010-11-03 00:00",
         "2010-11-02 00:00",
         "2010-10-29 00:00",
         "2010-08-27 00:00",
         "2010-02-22 00:00",
         "2009-12-15 00:00",
         "2009-08-20 00:00",
         "2009-07-24 00:00",
         "2009-05-19 00:00",
         "2009-05-08 00:00",
         "2009-03-30 00:00",
         "2009-02-20 00:00",
         "2008-12-16 00:00",
         "2008-11-19 00:00",
         "2008-10-29 00:00",
         "2008-10-17 00:00",
         "2008-10-16 00:00",
         "2008-10-14 00:00",
         "2008-08-15 00:00",
         "2008-04-22 00:00",
         "2008-03-26 00:00",
         "2008-03-24 00:00",
         "2008-01-21 00:00",
         "2007-12-07 00:00",
         "2007-11-07 00:00",
         "2007-09-28 00:00",
         "2007-09-24 00:00",
         "2007-09-19 00:00",
         "2007-07-13 00:00",
         "2007-06-29 00:00",
         "2007-06-01 00:00",
         "2007-05-29 00:00",
         "2007-05-24 00:00",
         "2007-05-23 00:00",
         "2007-04-03 00:00",
         "2007-03-09 00:01",
         "2007-03-09 00:00",
         "2007-02-26 00:00",
         "2007-02-22 00:00",
         "2007-02-20 00:00",
         "2006-11-14 00:00",
         "2006-09-01 00:00",
         "2006-07-06 00:00",
         "2006-06-23 00:00",
         "2006-05-18 00:00",
         "2006-04-12 00:00",
         "2006-04-06 00:00",
         "2006-03-17 00:00",
         "2006-03-10 00:00",
         "2006-03-02 00:00",
         "2006-01-17 00:00",
         "2005-11-04 00:00",
         "2005-10-11 00:00",
         "2005-06-13 00:00",
         "2005-06-02 00:00",
         "2005-04-21 00:00",
         "2005-03-24 00:00",
         "2005-03-15 00:00",
         "2005-02-14 00:00",
         "2004-11-23 00:00",
         "2004-10-13 00:00",
         "2004-08-30 00:00",
         "2004-07-20 00:01",
         "2004-07-20 00:00",
         "2004-07-19 00:00",
         "2003-05-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SnpxBackplaneType(Integer32, TextualConvention):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("enetFastEnet", 10),
          ("enetFastGigEnet", 12),
          ("enetTrFastEnet", 9),
          ("enetTrFastEnetRed", 11),
          ("eth", 2),
          ("ethFddi", 4),
          ("ethTok", 3),
          ("ethTokFddi", 5),
          ("ethTokFddiRed", 7),
          ("ethTokRed", 6),
          ("other", 1),
          ("tok", 8))
    )



class SnpxChassisType(Integer32, TextualConvention):
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
              237)
        )
    )
    namedValues = NamedValues(
        *(("m1032x", 16),
          ("m2300x", 23),
          ("m2310", 4),
          ("m2310x", 26),
          ("m2486", 21),
          ("m2715SA", 20),
          ("m271x", 8),
          ("m2810", 5),
          ("m2813", 9),
          ("m2813SA", 13),
          ("m2814", 10),
          ("m2814SA", 14),
          ("m28200EthSwitch", 31),
          ("m28xxx", 22),
          ("m2912", 6),
          ("m2914", 7),
          ("m2915", 11),
          ("m3000", 2),
          ("m3000FastEth", 28),
          ("m3030", 3),
          ("m5000", 12),
          ("m5005", 17),
          ("m5DN00x", 24),
          ("m810M", 15),
          ("mAlcatelEthConc", 18),
          ("mAlteon180e", 87),
          ("mAlteon184", 89),
          ("mAlteon2208", 103),
          ("mAlteon2216", 104),
          ("mAlteon2224", 102),
          ("mAlteon2424", 101),
          ("mAlteon3408", 105),
          ("mAlteon3416", 106),
          ("mAlteonAD3", 88),
          ("mAlteonAD4", 90),
          ("mAlteonAS2424SSL", 123),
          ("mAlteonSSL310", 118),
          ("mAlteonSSL310FIPS", 120),
          ("mAlteonSSL310Fiber", 119),
          ("mAlteonSSL410", 121),
          ("mAlteonSSL410Fiber", 122),
          ("mAlteonSwitch", 81),
          ("mBES1010-24T", 137),
          ("mBES1010-48T", 138),
          ("mBES1020-24T-PWR", 139),
          ("mBES1020-48T-PWR", 140),
          ("mBES110-24T", 145),
          ("mBES110-48T", 146),
          ("mBES120-24T-PWR", 147),
          ("mBES120-48T-PWR", 148),
          ("mBES2010-24T", 141),
          ("mBES2010-48T", 142),
          ("mBES2020-24T-PWR", 143),
          ("mBES2020-48T-PWR", 144),
          ("mBES210-24T", 149),
          ("mBES210-48T", 150),
          ("mBES220-24T-PWR", 151),
          ("mBES220-48T-PWR", 152),
          ("mBPS2000", 64),
          ("mBayStack10", 68),
          ("mBayStack100Hub", 27),
          ("mBayStack150", 41),
          ("mBayStack200", 45),
          ("mBayStack250", 46),
          ("mBayStack301", 35),
          ("mBayStack302", 39),
          ("mBayStack303-304", 44),
          ("mBayStack350", 40),
          ("mBayStack3580", 67),
          ("mBayStack380", 77),
          ("mBayStack380-24F", 95),
          ("mBayStack410", 49),
          ("mBayStack420", 69),
          ("mBayStack450", 48),
          ("mBayStack670", 60),
          ("mBayStackEth", 25),
          ("mBayStackTr", 36),
          ("mCent12Slot", 33),
          ("mCent1Slot", 34),
          ("mCent50N3Slot", 42),
          ("mCent50T3Slot", 43),
          ("mCent6Slot", 32),
          ("mERS1424", 91),
          ("mERS1612", 93),
          ("mERS1624", 94),
          ("mERS1648", 92),
          ("mERS2402", 100),
          ("mERS2500-26T", 159),
          ("mERS2500-26T-PWR", 160),
          ("mERS2500-50T", 161),
          ("mERS2500-50T-PWR", 162),
          ("mERS3510GT", 206),
          ("mERS3510GT-PWR-PLUS", 207),
          ("mERS3524GT", 204),
          ("mERS3524GT-PWR-PLUS", 205),
          ("mERS3526T", 202),
          ("mERS3526T-PWR-PLUS", 203),
          ("mERS3549GTS", 214),
          ("mERS3549GTS-PWR-PLUS", 215),
          ("mERS3550T", 236),
          ("mERS3550T-PWR-PLUS", 237),
          ("mERS4524GT", 165),
          ("mERS4524GT-PWR", 184),
          ("mERS4526FX", 158),
          ("mERS4526GTX", 166),
          ("mERS4526GTX-PWR", 167),
          ("mERS4526T", 163),
          ("mERS4526T-PWR", 164),
          ("mERS4526T-PWR-PLUS", 195),
          ("mERS4548GT", 154),
          ("mERS4548GT-PWR", 155),
          ("mERS4550T", 156),
          ("mERS4550T-PWR", 157),
          ("mERS4550T-PWR-PLUS", 196),
          ("mERS4826GTS", 199),
          ("mERS4826GTS-PWR-PLUS", 197),
          ("mERS4850GTS", 200),
          ("mERS4850GTS-PWR-PLUS", 198),
          ("mERS4926GTS", 225),
          ("mERS4926GTS-PWR-PLUS", 226),
          ("mERS4950GTS", 227),
          ("mERS4950GTS-PWR-PLUS", 228),
          ("mERS5510-24T", 96),
          ("mERS5510-48T", 97),
          ("mERS5520-24T-PWR", 115),
          ("mERS5520-48T-PWR", 116),
          ("mERS5530-24TFD", 130),
          ("mERS5632FD", 176),
          ("mERS5650TD", 175),
          ("mERS5650TD-PWR", 174),
          ("mERS5698TFD", 173),
          ("mERS5698TFD-PWR", 172),
          ("mERS59100GTS", 223),
          ("mERS59100GTS-PWR-PLUS", 224),
          ("mERS5928GTS", 218),
          ("mERS5928GTS-PWR-PLUS", 219),
          ("mERS5928GTS-UPWR", 222),
          ("mERS5952GTS", 220),
          ("mERS5952GTS-PWR-PLUS", 221),
          ("mERS6628XSGT", 185),
          ("mERS6632XTS", 186),
          ("mERS740", 61),
          ("mERS750", 62),
          ("mERS790", 63),
          ("mERS8003", 74),
          ("mERS8006", 59),
          ("mERS8010", 58),
          ("mERS8010co", 71),
          ("mERS8103", 76),
          ("mERS8106", 66),
          ("mERS8110", 65),
          ("mERS8110co", 73),
          ("mERS8306", 114),
          ("mERS8310", 113),
          ("mERS8603", 75),
          ("mERS8603r", 190),
          ("mERS8606", 57),
          ("mERS8610", 56),
          ("mERS8610co", 72),
          ("mERS8803r", 191),
          ("mERS8806", 192),
          ("mERS8810", 193),
          ("mERS8810co", 194),
          ("mES325-24G", 125),
          ("mES325-24T", 124),
          ("mES3510-24T", 131),
          ("mES425-24T", 109),
          ("mES425-48T", 108),
          ("mES460-24T-PWR", 82),
          ("mES470-24T", 98),
          ("mES470-24T-PWR", 128),
          ("mES470-48T", 78),
          ("mES470-48T-PWR", 129),
          ("mESU1860B", 180),
          ("mESU1860S", 179),
          ("mESU1860T", 170),
          ("mESU1860V", 178),
          ("mESU1880S", 171),
          ("mFVC10625", 37),
          ("mMERS4600", 169),
          ("mMERS64000", 181),
          ("mMERS8603R", 183),
          ("mMERS8611c0", 182),
          ("mMESU2400", 187),
          ("mMetro1200ESM", 70),
          ("mMetro1400ESM", 80),
          ("mMetro1450ESM", 79),
          ("mMetro3500", 136),
          ("mMetro8003", 86),
          ("mMetro8006", 85),
          ("mMetro8010", 83),
          ("mMetro8010co", 84),
          ("mMetroESU1800-24T", 111),
          ("mMetroESU1800-24T-LX-DC", 112),
          ("mMetroESU1850-12G-AC", 132),
          ("mMetroESU1850-12G-DC", 133),
          ("mMetroNext", 168),
          ("mNetApp8032", 235),
          ("mNnVPNGw3050", 117),
          ("mNnVPNGw3070", 135),
          ("mOME6500", 153),
          ("mPassport1050", 54),
          ("mPassport1051", 55),
          ("mPassport1100", 52),
          ("mPassport1150", 53),
          ("mPassport1200", 50),
          ("mPassport1250", 51),
          ("mSnas4050", 134),
          ("mSwitchNode", 38),
          ("mVSP4450GSX", 233),
          ("mVSP4450GSX-PWR-PLUS", 216),
          ("mVSP4450GTXHT-PWR-PLUS", 229),
          ("mVSP4826GTS", 208),
          ("mVSP4826GTS-PWR-PLUS", 209),
          ("mVSP4850GTS", 210),
          ("mVSP4850GTS-PWR-PLUS", 211),
          ("mVSP7024XLS", 201),
          ("mVSP7024XT", 217),
          ("mVSP7254XSQ", 231),
          ("mVSP7254XTQ", 232),
          ("mVSP8284XSQ", 213),
          ("mVSP8404", 230),
          ("mVSP9010", 212),
          ("mVSP9012", 189),
          ("mVSP9408", 234),
          ("mVSS5000", 177),
          ("mWC8180", 188),
          ("mWLANAccessPoint2220", 99),
          ("mWLANAccessPoint2221", 110),
          ("mWLANAccessPoint2225", 126),
          ("mWLANSecuritySwitch2250", 107),
          ("mWLANSecuritySwitch2270", 127),
          ("mXediaSwitch", 29),
          ("notUsed", 30),
          ("other", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1)
)
_Series1000_ObjectIdentity = ObjectIdentity
series1000 = _Series1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 1)
)
_S3SnmpAgent_ObjectIdentity = ObjectIdentity
s3SnmpAgent = _S3SnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 2)
)
_Series3000_ObjectIdentity = ObjectIdentity
series3000 = _Series3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3)
)
_SuperAgent_ObjectIdentity = ObjectIdentity
superAgent = _SuperAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 4)
)
_SpecialTraps_ObjectIdentity = ObjectIdentity
specialTraps = _SpecialTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 5)
)
_Series5000_ObjectIdentity = ObjectIdentity
series5000 = _Series5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6)
)
_LanSwitch_ObjectIdentity = ObjectIdentity
lanSwitch = _LanSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 7)
)
_SnpxRmonExt_ObjectIdentity = ObjectIdentity
snpxRmonExt = _SnpxRmonExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 8)
)
_WirelessLAN_ObjectIdentity = ObjectIdentity
wirelessLAN = _WirelessLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 9)
)
_PowerSupply_ObjectIdentity = ObjectIdentity
powerSupply = _PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 10)
)
_Wlan2200_ObjectIdentity = ObjectIdentity
wlan2200 = _Wlan2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11)
)
_Temporary_ObjectIdentity = ObjectIdentity
temporary = _Temporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 2)
)
_Registration_ObjectIdentity = ObjectIdentity
registration = _Registration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3)
)
_S3reg_other_ObjectIdentity = ObjectIdentity
s3reg_other = _S3reg_other_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 1)
)
_S3reg_3000_ObjectIdentity = ObjectIdentity
s3reg_3000 = _S3reg_3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 2)
)
_S3reg_3000_enetNMM_ObjectIdentity = ObjectIdentity
s3reg_3000_enetNMM = _S3reg_3000_enetNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 2, 1)
)
_S3reg_3000_trNMM_ObjectIdentity = ObjectIdentity
s3reg_3000_trNMM = _S3reg_3000_trNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 2, 2)
)
_S3reg_3000_FDDI_NMM_ObjectIdentity = ObjectIdentity
s3reg_3000_FDDI_NMM = _S3reg_3000_FDDI_NMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 2, 3)
)
_S3reg_3000_FastEthNMM_ObjectIdentity = ObjectIdentity
s3reg_3000_FastEthNMM = _S3reg_3000_FastEthNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 2, 4)
)
_S3reg_3000_ethSwitchNMM_ObjectIdentity = ObjectIdentity
s3reg_3000_ethSwitchNMM = _S3reg_3000_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 2, 5)
)
_S3reg_3030_ObjectIdentity = ObjectIdentity
s3reg_3030 = _S3reg_3030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 3)
)
_S3reg_3030_enetNMM_ObjectIdentity = ObjectIdentity
s3reg_3030_enetNMM = _S3reg_3030_enetNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 3, 1)
)
_S3reg_3030_trNMM_ObjectIdentity = ObjectIdentity
s3reg_3030_trNMM = _S3reg_3030_trNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 3, 2)
)
_S3reg_3030_FDDI_NMM_ObjectIdentity = ObjectIdentity
s3reg_3030_FDDI_NMM = _S3reg_3030_FDDI_NMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 3, 3)
)
_S3reg_3030_ethSwitchNMM_ObjectIdentity = ObjectIdentity
s3reg_3030_ethSwitchNMM = _S3reg_3030_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 3, 4)
)
_S3reg_2310_ObjectIdentity = ObjectIdentity
s3reg_2310 = _S3reg_2310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 4)
)
_S3reg_2310_enetNMM_ObjectIdentity = ObjectIdentity
s3reg_2310_enetNMM = _S3reg_2310_enetNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 4, 1)
)
_S3reg_2310_trNMM_ObjectIdentity = ObjectIdentity
s3reg_2310_trNMM = _S3reg_2310_trNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 4, 2)
)
_S3reg_2310_FDDI_NMM_ObjectIdentity = ObjectIdentity
s3reg_2310_FDDI_NMM = _S3reg_2310_FDDI_NMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 4, 3)
)
_S3reg_332X_ObjectIdentity = ObjectIdentity
s3reg_332X = _S3reg_332X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 5)
)
_S3reg_332XS_ObjectIdentity = ObjectIdentity
s3reg_332XS = _S3reg_332XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 6)
)
_S3reg_3356_ObjectIdentity = ObjectIdentity
s3reg_3356 = _S3reg_3356_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 7)
)
_S3reg_2810_ObjectIdentity = ObjectIdentity
s3reg_2810 = _S3reg_2810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 8)
)
_S3reg_2810_enetNMM_ObjectIdentity = ObjectIdentity
s3reg_2810_enetNMM = _S3reg_2810_enetNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 8, 1)
)
_S3reg_2715_ObjectIdentity = ObjectIdentity
s3reg_2715 = _S3reg_2715_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 9)
)
_S3reg_2715_trNMM_ObjectIdentity = ObjectIdentity
s3reg_2715_trNMM = _S3reg_2715_trNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 9, 1)
)
_S3reg_291X_ObjectIdentity = ObjectIdentity
s3reg_291X = _S3reg_291X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 10)
)
_S3reg_291X_FDDI_NMM_ObjectIdentity = ObjectIdentity
s3reg_291X_FDDI_NMM = _S3reg_291X_FDDI_NMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 10, 1)
)
_S3reg_3394_ObjectIdentity = ObjectIdentity
s3reg_3394 = _S3reg_3394_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 11)
)
_S3reg_281X_ObjectIdentity = ObjectIdentity
s3reg_281X = _S3reg_281X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 12)
)
_S3reg_281X_enetNMM_ObjectIdentity = ObjectIdentity
s3reg_281X_enetNMM = _S3reg_281X_enetNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 12, 1)
)
_S5reg_5000_ObjectIdentity = ObjectIdentity
s5reg_5000 = _S5reg_5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 13)
)
_S5reg_5000_ethNMM_ObjectIdentity = ObjectIdentity
s5reg_5000_ethNMM = _S5reg_5000_ethNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 13, 1)
)
_S5reg_5000_tokNMM_ObjectIdentity = ObjectIdentity
s5reg_5000_tokNMM = _S5reg_5000_tokNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 13, 2)
)
_S5reg_5000_fddNMM_ObjectIdentity = ObjectIdentity
s5reg_5000_fddNMM = _S5reg_5000_fddNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 13, 3)
)
_S5reg_5000_atmNMM_ObjectIdentity = ObjectIdentity
s5reg_5000_atmNMM = _S5reg_5000_atmNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 13, 4)
)
_S5reg_5000_ethSwitchNMM_ObjectIdentity = ObjectIdentity
s5reg_5000_ethSwitchNMM = _S5reg_5000_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 13, 5)
)
_S5reg_5000_ethFastEthNMM_ObjectIdentity = ObjectIdentity
s5reg_5000_ethFastEthNMM = _S5reg_5000_ethFastEthNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 13, 6)
)
_S5reg_5000_eth10_100SwitchNMM_ObjectIdentity = ObjectIdentity
s5reg_5000_eth10_100SwitchNMM = _S5reg_5000_eth10_100SwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 13, 7)
)
_S3reg_281XSA_ObjectIdentity = ObjectIdentity
s3reg_281XSA = _S3reg_281XSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 14)
)
_S3reg_281XSA_enetNMM_ObjectIdentity = ObjectIdentity
s3reg_281XSA_enetNMM = _S3reg_281XSA_enetNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 14, 1)
)
_Lsreg_28xxx_ObjectIdentity = ObjectIdentity
lsreg_28xxx = _Lsreg_28xxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 15)
)
_Lsreg_28xxx_NMM_ObjectIdentity = ObjectIdentity
lsreg_28xxx_NMM = _Lsreg_28xxx_NMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 15, 1)
)
_S3reg_8xx_ObjectIdentity = ObjectIdentity
s3reg_8xx = _S3reg_8xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 16)
)
_S3reg_810M_enetNMM_ObjectIdentity = ObjectIdentity
s3reg_810M_enetNMM = _S3reg_810M_enetNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 16, 1)
)
_S5reg_5005_ObjectIdentity = ObjectIdentity
s5reg_5005 = _S5reg_5005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 17)
)
_S5reg_5005_ethNMM_ObjectIdentity = ObjectIdentity
s5reg_5005_ethNMM = _S5reg_5005_ethNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 17, 1)
)
_S5reg_5005_tokNMM_ObjectIdentity = ObjectIdentity
s5reg_5005_tokNMM = _S5reg_5005_tokNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 17, 2)
)
_S5reg_5005_ethSwitchNMM_ObjectIdentity = ObjectIdentity
s5reg_5005_ethSwitchNMM = _S5reg_5005_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 17, 3)
)
_S5reg_5005_fddNMM_ObjectIdentity = ObjectIdentity
s5reg_5005_fddNMM = _S5reg_5005_fddNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 17, 4)
)
_S5reg_5005_ethFastEthNMM_ObjectIdentity = ObjectIdentity
s5reg_5005_ethFastEthNMM = _S5reg_5005_ethFastEthNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 17, 5)
)
_S5reg_5005_eth10_100SwitchNMM_ObjectIdentity = ObjectIdentity
s5reg_5005_eth10_100SwitchNMM = _S5reg_5005_eth10_100SwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 17, 7)
)
_S3reg_AlcatelConc_ObjectIdentity = ObjectIdentity
s3reg_AlcatelConc = _S3reg_AlcatelConc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 18)
)
_S3reg_AlcatelEthConc_enetNMM_ObjectIdentity = ObjectIdentity
s3reg_AlcatelEthConc_enetNMM = _S3reg_AlcatelEthConc_enetNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 18, 1)
)
_S3reg_271XSA_ObjectIdentity = ObjectIdentity
s3reg_271XSA = _S3reg_271XSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 19)
)
_S3reg_271XSA_trNMM_ObjectIdentity = ObjectIdentity
s3reg_271XSA_trNMM = _S3reg_271XSA_trNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 19, 1)
)
_Ecreg_1032x_ObjectIdentity = ObjectIdentity
ecreg_1032x = _Ecreg_1032x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 20)
)
_S3reg_1032x_NMM_ObjectIdentity = ObjectIdentity
s3reg_1032x_NMM = _S3reg_1032x_NMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 20, 1)
)
_Sreg_5DN00x_ObjectIdentity = ObjectIdentity
sreg_5DN00x = _Sreg_5DN00x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 21)
)
_Sreg_5DN00x_EthNMM_ObjectIdentity = ObjectIdentity
sreg_5DN00x_EthNMM = _Sreg_5DN00x_EthNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 21, 1)
)
_Sreg_BayStackEth_ObjectIdentity = ObjectIdentity
sreg_BayStackEth = _Sreg_BayStackEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 22)
)
_Sreg_BayStackEth_ethNMM_ObjectIdentity = ObjectIdentity
sreg_BayStackEth_ethNMM = _Sreg_BayStackEth_ethNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 22, 1)
)
_Sreg_2300x_ObjectIdentity = ObjectIdentity
sreg_2300x = _Sreg_2300x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 23)
)
_Sreg_2300x_NMM_ObjectIdentity = ObjectIdentity
sreg_2300x_NMM = _Sreg_2300x_NMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 23, 1)
)
_Sreg_2310x_ObjectIdentity = ObjectIdentity
sreg_2310x = _Sreg_2310x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 24)
)
_Sreg_2310x_NMM_ObjectIdentity = ObjectIdentity
sreg_2310x_NMM = _Sreg_2310x_NMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 24, 1)
)
_Sreg_Orion_ObjectIdentity = ObjectIdentity
sreg_Orion = _Sreg_Orion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 25)
)
_Sreg_Orion_ethNMM_ObjectIdentity = ObjectIdentity
sreg_Orion_ethNMM = _Sreg_Orion_ethNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 25, 1)
)
_Sreg_BayStack100Hub_ObjectIdentity = ObjectIdentity
sreg_BayStack100Hub = _Sreg_BayStack100Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 26)
)
_Sreg_BayStack100Unit_12Port_ObjectIdentity = ObjectIdentity
sreg_BayStack100Unit_12Port = _Sreg_BayStack100Unit_12Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 26, 1)
)
_Sreg_BayStackTr_ObjectIdentity = ObjectIdentity
sreg_BayStackTr = _Sreg_BayStackTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 27)
)
_Sreg_BayStackTr_trNMM_ObjectIdentity = ObjectIdentity
sreg_BayStackTr_trNMM = _Sreg_BayStackTr_trNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 27, 1)
)
_Lsreg_28200_ObjectIdentity = ObjectIdentity
lsreg_28200 = _Lsreg_28200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 28)
)
_Lsreg_28200_ethSwitchNMM_ObjectIdentity = ObjectIdentity
lsreg_28200_ethSwitchNMM = _Lsreg_28200_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 28, 1)
)
_Sreg_BayStack302_ObjectIdentity = ObjectIdentity
sreg_BayStack302 = _Sreg_BayStack302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 29)
)
_Sreg_BayStack302_9port_ObjectIdentity = ObjectIdentity
sreg_BayStack302_9port = _Sreg_BayStack302_9port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 29, 1)
)
_Sreg_BayStack350_ObjectIdentity = ObjectIdentity
sreg_BayStack350 = _Sreg_BayStack350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 30)
)
_Sreg_BayStack350_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack350_ethSwitchNMM = _Sreg_BayStack350_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 30, 1)
)
_Sreg_BayStack350_24T_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack350_24T_ethSwitchNMM = _Sreg_BayStack350_24T_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 30, 2)
)
_Sreg_BayStack150Eth_ObjectIdentity = ObjectIdentity
sreg_BayStack150Eth = _Sreg_BayStack150Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 31)
)
_Sreg_BayStack150Eth_ethNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack150Eth_ethNMM = _Sreg_BayStack150Eth_ethNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 31, 1)
)
_Sreg_BayStack303_304_ObjectIdentity = ObjectIdentity
sreg_BayStack303_304 = _Sreg_BayStack303_304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 32)
)
_Sreg_BayStack303_304_Sw_ObjectIdentity = ObjectIdentity
sreg_BayStack303_304_Sw = _Sreg_BayStack303_304_Sw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 32, 1)
)
_Sreg_BayStack303_24T_Sw_ObjectIdentity = ObjectIdentity
sreg_BayStack303_24T_Sw = _Sreg_BayStack303_24T_Sw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 32, 2)
)
_Sreg_BayStack200Eth_ObjectIdentity = ObjectIdentity
sreg_BayStack200Eth = _Sreg_BayStack200Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 33)
)
_Sreg_BayStack200Eth_ethNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack200Eth_ethNMM = _Sreg_BayStack200Eth_ethNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 33, 1)
)
_Sreg_BayStack250Eth_ObjectIdentity = ObjectIdentity
sreg_BayStack250Eth = _Sreg_BayStack250Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 34)
)
_Sreg_BayStack250Eth_ethNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack250Eth_ethNMM = _Sreg_BayStack250Eth_ethNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 34, 1)
)
_Sreg_BayStack450_ObjectIdentity = ObjectIdentity
sreg_BayStack450 = _Sreg_BayStack450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 35)
)
_Sreg_BayStack450_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack450_ethSwitchNMM = _Sreg_BayStack450_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 35, 1)
)
_Sreg_BayStack410_ObjectIdentity = ObjectIdentity
sreg_BayStack410 = _Sreg_BayStack410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 36)
)
_Sreg_BayStack410_24T_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack410_24T_ethSwitchNMM = _Sreg_BayStack410_24T_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 36, 1)
)
_Sreg_BayStackICS_ObjectIdentity = ObjectIdentity
sreg_BayStackICS = _Sreg_BayStackICS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 37)
)
_Sreg_BayStackICS_NMM_ObjectIdentity = ObjectIdentity
sreg_BayStackICS_NMM = _Sreg_BayStackICS_NMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 37, 1)
)
_S5reg_Accelar8010_ObjectIdentity = ObjectIdentity
s5reg_Accelar8010 = _S5reg_Accelar8010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 38)
)
_S5reg_Accelar8132TX_ObjectIdentity = ObjectIdentity
s5reg_Accelar8132TX = _S5reg_Accelar8132TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 38, 1)
)
_S5reg_Accelar8148TX_ObjectIdentity = ObjectIdentity
s5reg_Accelar8148TX = _S5reg_Accelar8148TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 38, 2)
)
_Sreg_BayStack670_ObjectIdentity = ObjectIdentity
sreg_BayStack670 = _Sreg_BayStack670_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 39)
)
_Sreg_BayStack670_wirelessLAN_ObjectIdentity = ObjectIdentity
sreg_BayStack670_wirelessLAN = _Sreg_BayStack670_wirelessLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 39, 1)
)
_Sreg_BPS2000_ObjectIdentity = ObjectIdentity
sreg_BPS2000 = _Sreg_BPS2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 40)
)
_Sreg_BPS2000_24T_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BPS2000_24T_ethSwitchNMM = _Sreg_BPS2000_24T_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 40, 1)
)
_Sreg_BayStack3580_ObjectIdentity = ObjectIdentity
sreg_BayStack3580 = _Sreg_BayStack3580_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 41)
)
_Sreg_BayStack3580_16F_gigEthSwitch_ObjectIdentity = ObjectIdentity
sreg_BayStack3580_16F_gigEthSwitch = _Sreg_BayStack3580_16F_gigEthSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 41, 1)
)
_Sreg_BayStack10_ObjectIdentity = ObjectIdentity
sreg_BayStack10 = _Sreg_BayStack10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 42)
)
_Sreg_BayStack10_powerSupplyUnit_ObjectIdentity = ObjectIdentity
sreg_BayStack10_powerSupplyUnit = _Sreg_BayStack10_powerSupplyUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 42, 1)
)
_Sreg_BayStack420_ObjectIdentity = ObjectIdentity
sreg_BayStack420 = _Sreg_BayStack420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 43)
)
_Sreg_BayStack420_24T_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack420_24T_ethSwitchNMM = _Sreg_BayStack420_24T_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 43, 1)
)
_Sreg_Metro1200ESM_ObjectIdentity = ObjectIdentity
sreg_Metro1200ESM = _Sreg_Metro1200ESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 44)
)
_Sreg_Metro1200ESM_12T_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_Metro1200ESM_12T_ethSwitchNMM = _Sreg_Metro1200ESM_12T_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 44, 1)
)
_Sreg_BayStack380_ObjectIdentity = ObjectIdentity
sreg_BayStack380 = _Sreg_BayStack380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 45)
)
_Sreg_BayStack380_24T_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack380_24T_ethSwitchNMM = _Sreg_BayStack380_24T_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 45, 1)
)
_Sreg_BayStack470_ObjectIdentity = ObjectIdentity
sreg_BayStack470 = _Sreg_BayStack470_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 46)
)
_Sreg_BayStack470_48T_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack470_48T_ethSwitchNMM = _Sreg_BayStack470_48T_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 46, 1)
)
_Sreg_Metro1450ESM_ObjectIdentity = ObjectIdentity
sreg_Metro1450ESM = _Sreg_Metro1450ESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 47)
)
_Sreg_Metro1450ESM_12T2GBIC_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_Metro1450ESM_12T2GBIC_ethSwitchNMM = _Sreg_Metro1450ESM_12T2GBIC_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 47, 1)
)
_Sreg_Metro1400ESM_ObjectIdentity = ObjectIdentity
sreg_Metro1400ESM = _Sreg_Metro1400ESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 48)
)
_Sreg_Metro1400ESM_12T2GBIC_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_Metro1400ESM_12T2GBIC_ethSwitchNMM = _Sreg_Metro1400ESM_12T2GBIC_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 48, 1)
)
_Sreg_BayStack460_24T_PWR_ObjectIdentity = ObjectIdentity
sreg_BayStack460_24T_PWR = _Sreg_BayStack460_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 49)
)
_Sreg_BayStack460_24T_PWR_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack460_24T_PWR_ethSwitchNMM = _Sreg_BayStack460_24T_PWR_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 49, 1)
)
_Sreg_Metro8000_ObjectIdentity = ObjectIdentity
sreg_Metro8000 = _Sreg_Metro8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 50)
)
_Sreg_Metro8000_8664GB_OPM_ObjectIdentity = ObjectIdentity
sreg_Metro8000_8664GB_OPM = _Sreg_Metro8000_8664GB_OPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 50, 1)
)
_Sreg_BayStack380_24F_ObjectIdentity = ObjectIdentity
sreg_BayStack380_24F = _Sreg_BayStack380_24F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 51)
)
_Sreg_BayStack380_24F_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack380_24F_ethSwitchNMM = _Sreg_BayStack380_24F_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 51, 1)
)
_Sreg_BayStack5510_24T_ObjectIdentity = ObjectIdentity
sreg_BayStack5510_24T = _Sreg_BayStack5510_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 52)
)
_Sreg_BayStack5510_24T_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack5510_24T_ethSwitchNMM = _Sreg_BayStack5510_24T_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 52, 1)
)
_Sreg_BayStack5510_48T_ObjectIdentity = ObjectIdentity
sreg_BayStack5510_48T = _Sreg_BayStack5510_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 53)
)
_Sreg_BayStack5510_48T_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack5510_48T_ethSwitchNMM = _Sreg_BayStack5510_48T_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 53, 1)
)
_Sreg_BayStack470_24T_ObjectIdentity = ObjectIdentity
sreg_BayStack470_24T = _Sreg_BayStack470_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 54)
)
_Sreg_BayStack470_24T_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack470_24T_ethSwitchNMM = _Sreg_BayStack470_24T_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 54, 1)
)
_Sreg_WLANAccessPoint2220_ObjectIdentity = ObjectIdentity
sreg_WLANAccessPoint2220 = _Sreg_WLANAccessPoint2220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 55)
)
_Sreg_WLANAccessPoint2220_wirelessAP_ObjectIdentity = ObjectIdentity
sreg_WLANAccessPoint2220_wirelessAP = _Sreg_WLANAccessPoint2220_wirelessAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 55, 1)
)
_Sreg_WLANSecuritySwitch2250_ObjectIdentity = ObjectIdentity
sreg_WLANSecuritySwitch2250 = _Sreg_WLANSecuritySwitch2250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 56)
)
_Sreg_BayStack425_ObjectIdentity = ObjectIdentity
sreg_BayStack425 = _Sreg_BayStack425_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 57)
)
_Sreg_BayStack425_48T_ObjectIdentity = ObjectIdentity
sreg_BayStack425_48T = _Sreg_BayStack425_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 57, 1)
)
_Sreg_BayStack425_24T_ObjectIdentity = ObjectIdentity
sreg_BayStack425_24T = _Sreg_BayStack425_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 57, 2)
)
_Sreg_WLANAccessPoint2221_ObjectIdentity = ObjectIdentity
sreg_WLANAccessPoint2221 = _Sreg_WLANAccessPoint2221_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 58)
)
_Sreg_WLANAccessPoint2221_wirelessAP_ObjectIdentity = ObjectIdentity
sreg_WLANAccessPoint2221_wirelessAP = _Sreg_WLANAccessPoint2221_wirelessAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 58, 1)
)
_Sreg_BayStack5520_ObjectIdentity = ObjectIdentity
sreg_BayStack5520 = _Sreg_BayStack5520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 59)
)
_Sreg_BayStack5520_24T_PWR_ObjectIdentity = ObjectIdentity
sreg_BayStack5520_24T_PWR = _Sreg_BayStack5520_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 59, 1)
)
_Sreg_BayStack5520_48T_PWR_ObjectIdentity = ObjectIdentity
sreg_BayStack5520_48T_PWR = _Sreg_BayStack5520_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 59, 2)
)
_Sreg_WLANSecuritySwitch_ObjectIdentity = ObjectIdentity
sreg_WLANSecuritySwitch = _Sreg_WLANSecuritySwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 60)
)
_Sreg_WLANSecuritySwitch2270_ObjectIdentity = ObjectIdentity
sreg_WLANSecuritySwitch2270 = _Sreg_WLANSecuritySwitch2270_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 60, 1)
)
_Sreg_BayStack325_ObjectIdentity = ObjectIdentity
sreg_BayStack325 = _Sreg_BayStack325_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 61)
)
_Sreg_BayStack325_24T_ObjectIdentity = ObjectIdentity
sreg_BayStack325_24T = _Sreg_BayStack325_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 61, 1)
)
_Sreg_BayStack325_24G_ObjectIdentity = ObjectIdentity
sreg_BayStack325_24G = _Sreg_BayStack325_24G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 61, 2)
)
_Sreg_WLANAccessPoint2225_ObjectIdentity = ObjectIdentity
sreg_WLANAccessPoint2225 = _Sreg_WLANAccessPoint2225_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 62)
)
_Sreg_WLANAccessPoint2225_wirelessAP_ObjectIdentity = ObjectIdentity
sreg_WLANAccessPoint2225_wirelessAP = _Sreg_WLANAccessPoint2225_wirelessAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 62, 1)
)
_Sreg_BayStack470_24T_PWR_ObjectIdentity = ObjectIdentity
sreg_BayStack470_24T_PWR = _Sreg_BayStack470_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 63)
)
_Sreg_BayStack470_24T_PWR_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack470_24T_PWR_ethSwitchNMM = _Sreg_BayStack470_24T_PWR_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 63, 1)
)
_Sreg_BayStack470_48T_PWR_ObjectIdentity = ObjectIdentity
sreg_BayStack470_48T_PWR = _Sreg_BayStack470_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 64)
)
_Sreg_BayStack470_48T_PWR_ethSwitchNMM_ObjectIdentity = ObjectIdentity
sreg_BayStack470_48T_PWR_ethSwitchNMM = _Sreg_BayStack470_48T_PWR_ethSwitchNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 64, 1)
)
_Sreg_EthernetRoutingSwitch5530_24TFD_ObjectIdentity = ObjectIdentity
sreg_EthernetRoutingSwitch5530_24TFD = _Sreg_EthernetRoutingSwitch5530_24TFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 65)
)
_Sreg_EthernetSwitch3510_24T_ObjectIdentity = ObjectIdentity
sreg_EthernetSwitch3510_24T = _Sreg_EthernetSwitch3510_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 66)
)
_Sreg_NortelWLAN_ObjectIdentity = ObjectIdentity
sreg_NortelWLAN = _Sreg_NortelWLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 67)
)
_Sreg_NortelWLAN2350_ObjectIdentity = ObjectIdentity
sreg_NortelWLAN2350 = _Sreg_NortelWLAN2350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 67, 1)
)
_Sreg_NortelWLAN2360_ObjectIdentity = ObjectIdentity
sreg_NortelWLAN2360 = _Sreg_NortelWLAN2360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 67, 2)
)
_Sreg_NortelWLAN2361_ObjectIdentity = ObjectIdentity
sreg_NortelWLAN2361 = _Sreg_NortelWLAN2361_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 67, 3)
)
_Sreg_NortelWLAN2370_ObjectIdentity = ObjectIdentity
sreg_NortelWLAN2370 = _Sreg_NortelWLAN2370_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 67, 4)
)
_Sreg_NortelWLAN2380_ObjectIdentity = ObjectIdentity
sreg_NortelWLAN2380 = _Sreg_NortelWLAN2380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 67, 5)
)
_Sreg_NortelMX2800_ObjectIdentity = ObjectIdentity
sreg_NortelMX2800 = _Sreg_NortelMX2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 67, 8)
)
_Sreg_SMB_BES_ObjectIdentity = ObjectIdentity
sreg_SMB_BES = _Sreg_SMB_BES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68)
)
_Sreg_SMB_BES_GIG_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_GIG = _Sreg_SMB_BES_GIG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 1)
)
_Sreg_SMB_BES_1010_24T_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_1010_24T = _Sreg_SMB_BES_1010_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 1, 1)
)
_Sreg_SMB_BES_1010_48T_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_1010_48T = _Sreg_SMB_BES_1010_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 1, 2)
)
_Sreg_SMB_BES_1020_24T_PWR_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_1020_24T_PWR = _Sreg_SMB_BES_1020_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 1, 3)
)
_Sreg_SMB_BES_1020_48T_PWR_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_1020_48T_PWR = _Sreg_SMB_BES_1020_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 1, 4)
)
_Sreg_SMB_BES_2010_24T_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_2010_24T = _Sreg_SMB_BES_2010_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 1, 5)
)
_Sreg_SMB_BES_2010_48T_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_2010_48T = _Sreg_SMB_BES_2010_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 1, 6)
)
_Sreg_SMB_BES_2020_24T_PWR_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_2020_24T_PWR = _Sreg_SMB_BES_2020_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 1, 7)
)
_Sreg_SMB_BES_2020_48T_PWR_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_2020_48T_PWR = _Sreg_SMB_BES_2020_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 1, 8)
)
_Sreg_SMB_BES_FE_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_FE = _Sreg_SMB_BES_FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 2)
)
_Sreg_SMB_BES_110_24T_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_110_24T = _Sreg_SMB_BES_110_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 2, 1)
)
_Sreg_SMB_BES_110_48T_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_110_48T = _Sreg_SMB_BES_110_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 2, 2)
)
_Sreg_SMB_BES_120_24T_PWR_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_120_24T_PWR = _Sreg_SMB_BES_120_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 2, 3)
)
_Sreg_SMB_BES_120_48T_PWR_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_120_48T_PWR = _Sreg_SMB_BES_120_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 2, 4)
)
_Sreg_SMB_BES_210_24T_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_210_24T = _Sreg_SMB_BES_210_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 2, 5)
)
_Sreg_SMB_BES_210_48T_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_210_48T = _Sreg_SMB_BES_210_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 2, 6)
)
_Sreg_SMB_BES_220_24T_PWR_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_220_24T_PWR = _Sreg_SMB_BES_220_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 2, 7)
)
_Sreg_SMB_BES_220_48T_PWR_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_220_48T_PWR = _Sreg_SMB_BES_220_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 2, 8)
)
_Sreg_SMB_BES_50_FE_12T_PWR_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_50_FE_12T_PWR = _Sreg_SMB_BES_50_FE_12T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 3)
)
_Sreg_SMB_BES_50_FE_24T_PWR_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_50_FE_24T_PWR = _Sreg_SMB_BES_50_FE_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 4)
)
_Sreg_SMB_BES_50_GE_12T_PWR_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_50_GE_12T_PWR = _Sreg_SMB_BES_50_GE_12T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 5)
)
_Sreg_SMB_BES_50_GE_24T_PWR_ObjectIdentity = ObjectIdentity
sreg_SMB_BES_50_GE_24T_PWR = _Sreg_SMB_BES_50_GE_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 68, 6)
)
_Sreg_SMB_BAP_ObjectIdentity = ObjectIdentity
sreg_SMB_BAP = _Sreg_SMB_BAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 69)
)
_Sreg_SMB_BAP_WirelessAccessPoint_ObjectIdentity = ObjectIdentity
sreg_SMB_BAP_WirelessAccessPoint = _Sreg_SMB_BAP_WirelessAccessPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 69, 1)
)
_Sreg_SMB_BAP_WirelessAccessPoint_BAP110_ObjectIdentity = ObjectIdentity
sreg_SMB_BAP_WirelessAccessPoint_BAP110 = _Sreg_SMB_BAP_WirelessAccessPoint_BAP110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 69, 1, 1)
)
_Sreg_SMB_BAP_WirelessAccessPoint_BAP120_ObjectIdentity = ObjectIdentity
sreg_SMB_BAP_WirelessAccessPoint_BAP120 = _Sreg_SMB_BAP_WirelessAccessPoint_BAP120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 69, 1, 2)
)
_Sreg_SMB_BSR_ObjectIdentity = ObjectIdentity
sreg_SMB_BSR = _Sreg_SMB_BSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 70)
)
_Sreg_SMB_BSR222_ObjectIdentity = ObjectIdentity
sreg_SMB_BSR222 = _Sreg_SMB_BSR222_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 70, 1)
)
_Sreg_SMB_BSR252_ObjectIdentity = ObjectIdentity
sreg_SMB_BSR252 = _Sreg_SMB_BSR252_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 70, 2)
)
_Sreg_ERS_45xx_ObjectIdentity = ObjectIdentity
sreg_ERS_45xx = _Sreg_ERS_45xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 71)
)
_Sreg_ERS_4548GT_ObjectIdentity = ObjectIdentity
sreg_ERS_4548GT = _Sreg_ERS_4548GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 71, 1)
)
_Sreg_ERS_4548GT_PWR_ObjectIdentity = ObjectIdentity
sreg_ERS_4548GT_PWR = _Sreg_ERS_4548GT_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 71, 2)
)
_Sreg_ERS_4550T_ObjectIdentity = ObjectIdentity
sreg_ERS_4550T = _Sreg_ERS_4550T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 71, 3)
)
_Sreg_ERS_4550T_PWR_ObjectIdentity = ObjectIdentity
sreg_ERS_4550T_PWR = _Sreg_ERS_4550T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 71, 4)
)
_Sreg_ERS_4526FX_ObjectIdentity = ObjectIdentity
sreg_ERS_4526FX = _Sreg_ERS_4526FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 71, 5)
)
_Sreg_ERS_4526GTX_PWR_ObjectIdentity = ObjectIdentity
sreg_ERS_4526GTX_PWR = _Sreg_ERS_4526GTX_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 71, 6)
)
_Sreg_ERS_4526GTX_ObjectIdentity = ObjectIdentity
sreg_ERS_4526GTX = _Sreg_ERS_4526GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 71, 7)
)
_Sreg_ERS_4524GT_ObjectIdentity = ObjectIdentity
sreg_ERS_4524GT = _Sreg_ERS_4524GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 71, 8)
)
_Sreg_ERS_4526T_PWR_ObjectIdentity = ObjectIdentity
sreg_ERS_4526T_PWR = _Sreg_ERS_4526T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 71, 9)
)
_Sreg_ERS_4526T_ObjectIdentity = ObjectIdentity
sreg_ERS_4526T = _Sreg_ERS_4526T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 71, 10)
)
_Sreg_ERS_4524GT_PWR_ObjectIdentity = ObjectIdentity
sreg_ERS_4524GT_PWR = _Sreg_ERS_4524GT_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 71, 11)
)
_Sreg_ERS_4526T_PWR_PLUS_ObjectIdentity = ObjectIdentity
sreg_ERS_4526T_PWR_PLUS = _Sreg_ERS_4526T_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 71, 12)
)
_Sreg_ERS_4550T_PWR_PLUS_ObjectIdentity = ObjectIdentity
sreg_ERS_4550T_PWR_PLUS = _Sreg_ERS_4550T_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 71, 13)
)
_Sreg_ERS_25xx_ObjectIdentity = ObjectIdentity
sreg_ERS_25xx = _Sreg_ERS_25xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 72)
)
_Sreg_ERS_2500_26T_ObjectIdentity = ObjectIdentity
sreg_ERS_2500_26T = _Sreg_ERS_2500_26T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 72, 1)
)
_Sreg_ERS_2500_26T_PWR_ObjectIdentity = ObjectIdentity
sreg_ERS_2500_26T_PWR = _Sreg_ERS_2500_26T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 72, 2)
)
_Sreg_ERS_2500_50T_ObjectIdentity = ObjectIdentity
sreg_ERS_2500_50T = _Sreg_ERS_2500_50T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 72, 3)
)
_Sreg_ERS_2500_50T_PWR_ObjectIdentity = ObjectIdentity
sreg_ERS_2500_50T_PWR = _Sreg_ERS_2500_50T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 72, 4)
)
_Sreg_SMB_BSG_ObjectIdentity = ObjectIdentity
sreg_SMB_BSG = _Sreg_SMB_BSG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 73)
)
_Sreg_SMB_BSGX4E_ObjectIdentity = ObjectIdentity
sreg_SMB_BSGX4E = _Sreg_SMB_BSGX4E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 73, 1)
)
_Sreg_SMB_BSG8EW_ObjectIdentity = ObjectIdentity
sreg_SMB_BSG8EW = _Sreg_SMB_BSG8EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 73, 2)
)
_Sreg_SMB_BSG12AW_ObjectIdentity = ObjectIdentity
sreg_SMB_BSG12AW = _Sreg_SMB_BSG12AW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 73, 3)
)
_Sreg_SMB_BSG12TW_ObjectIdentity = ObjectIdentity
sreg_SMB_BSG12TW = _Sreg_SMB_BSG12TW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 73, 4)
)
_Sreg_SMB_BSG12EW_ObjectIdentity = ObjectIdentity
sreg_SMB_BSG12EW = _Sreg_SMB_BSG12EW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 73, 5)
)
_Sreg_ERS_56xx_ObjectIdentity = ObjectIdentity
sreg_ERS_56xx = _Sreg_ERS_56xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 74)
)
_Sreg_ERS_5698_TFD_PWR_ObjectIdentity = ObjectIdentity
sreg_ERS_5698_TFD_PWR = _Sreg_ERS_5698_TFD_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 74, 1)
)
_Sreg_ERS_5698_TFD_ObjectIdentity = ObjectIdentity
sreg_ERS_5698_TFD = _Sreg_ERS_5698_TFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 74, 2)
)
_Sreg_ERS_5650_TD_PWR_ObjectIdentity = ObjectIdentity
sreg_ERS_5650_TD_PWR = _Sreg_ERS_5650_TD_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 74, 3)
)
_Sreg_ERS_5650_TD_ObjectIdentity = ObjectIdentity
sreg_ERS_5650_TD = _Sreg_ERS_5650_TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 74, 4)
)
_Sreg_ERS_5632_FD_ObjectIdentity = ObjectIdentity
sreg_ERS_5632_FD = _Sreg_ERS_5632_FD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 74, 5)
)
_Sreg_ESU_18xx_ObjectIdentity = ObjectIdentity
sreg_ESU_18xx = _Sreg_ESU_18xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 75)
)
_Sreg_ESU_1860_T_ObjectIdentity = ObjectIdentity
sreg_ESU_1860_T = _Sreg_ESU_1860_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 75, 1)
)
_Sreg_ESU_1880_S_ObjectIdentity = ObjectIdentity
sreg_ESU_1880_S = _Sreg_ESU_1880_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 75, 2)
)
_Sreg_ESU_1860_V_ObjectIdentity = ObjectIdentity
sreg_ESU_1860_V = _Sreg_ESU_1860_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 75, 3)
)
_Sreg_ESU_1860_S_ObjectIdentity = ObjectIdentity
sreg_ESU_1860_S = _Sreg_ESU_1860_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 75, 4)
)
_Sreg_ESU_1860_B_ObjectIdentity = ObjectIdentity
sreg_ESU_1860_B = _Sreg_ESU_1860_B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 75, 5)
)
_Sreg_ERS_66xx_ObjectIdentity = ObjectIdentity
sreg_ERS_66xx = _Sreg_ERS_66xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 76)
)
_Sreg_ERS_6628_XSGT_ObjectIdentity = ObjectIdentity
sreg_ERS_6628_XSGT = _Sreg_ERS_6628_XSGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 76, 1)
)
_Sreg_ERS_6632_XTS_ObjectIdentity = ObjectIdentity
sreg_ERS_6632_XTS = _Sreg_ERS_6632_XTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 76, 2)
)
_Sreg_WC_8xxx_ObjectIdentity = ObjectIdentity
sreg_WC_8xxx = _Sreg_WC_8xxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 77)
)
_Sreg_WC_8180_ObjectIdentity = ObjectIdentity
sreg_WC_8180 = _Sreg_WC_8180_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 77, 1)
)
_Sreg_ERS_48xx_ObjectIdentity = ObjectIdentity
sreg_ERS_48xx = _Sreg_ERS_48xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 78)
)
_Sreg_ERS_4826GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
sreg_ERS_4826GTS_PWR_PLUS = _Sreg_ERS_4826GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 78, 1)
)
_Sreg_ERS_4850GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
sreg_ERS_4850GTS_PWR_PLUS = _Sreg_ERS_4850GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 78, 2)
)
_Sreg_ERS_4826GTS_ObjectIdentity = ObjectIdentity
sreg_ERS_4826GTS = _Sreg_ERS_4826GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 78, 3)
)
_Sreg_ERS_4850GTS_ObjectIdentity = ObjectIdentity
sreg_ERS_4850GTS = _Sreg_ERS_4850GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 78, 4)
)
_Sreg_VSP_7xxx_ObjectIdentity = ObjectIdentity
sreg_VSP_7xxx = _Sreg_VSP_7xxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 79)
)
_Sreg_VSP_7024XLS_ObjectIdentity = ObjectIdentity
sreg_VSP_7024XLS = _Sreg_VSP_7024XLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 79, 1)
)
_Sreg_VSP_7024XT_ObjectIdentity = ObjectIdentity
sreg_VSP_7024XT = _Sreg_VSP_7024XT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 79, 2)
)
_Sreg_ERS_35xx_ObjectIdentity = ObjectIdentity
sreg_ERS_35xx = _Sreg_ERS_35xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 80)
)
_Sreg_ERS_3526T_ObjectIdentity = ObjectIdentity
sreg_ERS_3526T = _Sreg_ERS_3526T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 80, 1)
)
_Sreg_ERS_3526T_PWR_PLUS_ObjectIdentity = ObjectIdentity
sreg_ERS_3526T_PWR_PLUS = _Sreg_ERS_3526T_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 80, 2)
)
_Sreg_ERS_3524GT_ObjectIdentity = ObjectIdentity
sreg_ERS_3524GT = _Sreg_ERS_3524GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 80, 3)
)
_Sreg_ERS_3524GT_PWR_PLUS_ObjectIdentity = ObjectIdentity
sreg_ERS_3524GT_PWR_PLUS = _Sreg_ERS_3524GT_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 80, 4)
)
_Sreg_ERS_3510GT_ObjectIdentity = ObjectIdentity
sreg_ERS_3510GT = _Sreg_ERS_3510GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 80, 5)
)
_Sreg_ERS_3510GT_PWR_PLUS_ObjectIdentity = ObjectIdentity
sreg_ERS_3510GT_PWR_PLUS = _Sreg_ERS_3510GT_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 80, 6)
)
_Sreg_ERS_3549GTS_ObjectIdentity = ObjectIdentity
sreg_ERS_3549GTS = _Sreg_ERS_3549GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 80, 7)
)
_Sreg_ERS_3549GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
sreg_ERS_3549GTS_PWR_PLUS = _Sreg_ERS_3549GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 80, 8)
)
_Sreg_ERS_3550T_ObjectIdentity = ObjectIdentity
sreg_ERS_3550T = _Sreg_ERS_3550T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 80, 9)
)
_Sreg_ERS_3550T_PWR_PLUS_ObjectIdentity = ObjectIdentity
sreg_ERS_3550T_PWR_PLUS = _Sreg_ERS_3550T_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 80, 10)
)
_Sreg_ERS59xx_ObjectIdentity = ObjectIdentity
sreg_ERS59xx = _Sreg_ERS59xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 81)
)
_Sreg_ERS5928GTS_ObjectIdentity = ObjectIdentity
sreg_ERS5928GTS = _Sreg_ERS5928GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 81, 1)
)
_Sreg_ERS5928GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
sreg_ERS5928GTS_PWR_PLUS = _Sreg_ERS5928GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 81, 2)
)
_Sreg_ERS5952GTS_ObjectIdentity = ObjectIdentity
sreg_ERS5952GTS = _Sreg_ERS5952GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 81, 3)
)
_Sreg_ERS5952GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
sreg_ERS5952GTS_PWR_PLUS = _Sreg_ERS5952GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 81, 4)
)
_Sreg_ERS5928GTS_UPWR_ObjectIdentity = ObjectIdentity
sreg_ERS5928GTS_UPWR = _Sreg_ERS5928GTS_UPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 81, 5)
)
_Sreg_ERS59100GTS_ObjectIdentity = ObjectIdentity
sreg_ERS59100GTS = _Sreg_ERS59100GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 81, 6)
)
_Sreg_ERS59100GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
sreg_ERS59100GTS_PWR_PLUS = _Sreg_ERS59100GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 81, 7)
)
_Sreg_ERS49_ObjectIdentity = ObjectIdentity
sreg_ERS49 = _Sreg_ERS49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 82)
)
_Sreg_ERS4926GTS_ObjectIdentity = ObjectIdentity
sreg_ERS4926GTS = _Sreg_ERS4926GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 82, 1)
)
_Sreg_ERS4926GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
sreg_ERS4926GTS_PWR_PLUS = _Sreg_ERS4926GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 82, 2)
)
_Sreg_ERS4950GTS_ObjectIdentity = ObjectIdentity
sreg_ERS4950GTS = _Sreg_ERS4950GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 82, 3)
)
_Sreg_ERS4950GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
sreg_ERS4950GTS_PWR_PLUS = _Sreg_ERS4950GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 3, 82, 4)
)
_Policy_ObjectIdentity = ObjectIdentity
policy = _Policy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4)
)
_BayStackMibs_ObjectIdentity = ObjectIdentity
bayStackMibs = _BayStackMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5)
)
_NtwsTrapezeNetworks_ObjectIdentity = ObjectIdentity
ntwsTrapezeNetworks = _NtwsTrapezeNetworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6)
)
_AvayaWlanMibs_ObjectIdentity = ObjectIdentity
avayaWlanMibs = _AvayaWlanMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 7)
)
_AvayaWlan9100Mibs_ObjectIdentity = ObjectIdentity
avayaWlan9100Mibs = _AvayaWlan9100Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOPTICS-ROOT-MIB",
    **{"SnpxBackplaneType": SnpxBackplaneType,
       "SnpxChassisType": SnpxChassisType,
       "synoptics": synoptics,
       "products": products,
       "series1000": series1000,
       "s3SnmpAgent": s3SnmpAgent,
       "series3000": series3000,
       "superAgent": superAgent,
       "specialTraps": specialTraps,
       "series5000": series5000,
       "lanSwitch": lanSwitch,
       "snpxRmonExt": snpxRmonExt,
       "wirelessLAN": wirelessLAN,
       "powerSupply": powerSupply,
       "wlan2200": wlan2200,
       "temporary": temporary,
       "registration": registration,
       "s3reg-other": s3reg_other,
       "s3reg-3000": s3reg_3000,
       "s3reg-3000-enetNMM": s3reg_3000_enetNMM,
       "s3reg-3000-trNMM": s3reg_3000_trNMM,
       "s3reg-3000-FDDI-NMM": s3reg_3000_FDDI_NMM,
       "s3reg-3000-FastEthNMM": s3reg_3000_FastEthNMM,
       "s3reg-3000-ethSwitchNMM": s3reg_3000_ethSwitchNMM,
       "s3reg-3030": s3reg_3030,
       "s3reg-3030-enetNMM": s3reg_3030_enetNMM,
       "s3reg-3030-trNMM": s3reg_3030_trNMM,
       "s3reg-3030-FDDI-NMM": s3reg_3030_FDDI_NMM,
       "s3reg-3030-ethSwitchNMM": s3reg_3030_ethSwitchNMM,
       "s3reg-2310": s3reg_2310,
       "s3reg-2310-enetNMM": s3reg_2310_enetNMM,
       "s3reg-2310-trNMM": s3reg_2310_trNMM,
       "s3reg-2310-FDDI-NMM": s3reg_2310_FDDI_NMM,
       "s3reg-332X": s3reg_332X,
       "s3reg-332XS": s3reg_332XS,
       "s3reg-3356": s3reg_3356,
       "s3reg-2810": s3reg_2810,
       "s3reg-2810-enetNMM": s3reg_2810_enetNMM,
       "s3reg-2715": s3reg_2715,
       "s3reg-2715-trNMM": s3reg_2715_trNMM,
       "s3reg-291X": s3reg_291X,
       "s3reg-291X-FDDI-NMM": s3reg_291X_FDDI_NMM,
       "s3reg-3394": s3reg_3394,
       "s3reg-281X": s3reg_281X,
       "s3reg-281X-enetNMM": s3reg_281X_enetNMM,
       "s5reg-5000": s5reg_5000,
       "s5reg-5000-ethNMM": s5reg_5000_ethNMM,
       "s5reg-5000-tokNMM": s5reg_5000_tokNMM,
       "s5reg-5000-fddNMM": s5reg_5000_fddNMM,
       "s5reg-5000-atmNMM": s5reg_5000_atmNMM,
       "s5reg-5000-ethSwitchNMM": s5reg_5000_ethSwitchNMM,
       "s5reg-5000-ethFastEthNMM": s5reg_5000_ethFastEthNMM,
       "s5reg-5000-eth10-100SwitchNMM": s5reg_5000_eth10_100SwitchNMM,
       "s3reg-281XSA": s3reg_281XSA,
       "s3reg-281XSA-enetNMM": s3reg_281XSA_enetNMM,
       "lsreg-28xxx": lsreg_28xxx,
       "lsreg-28xxx-NMM": lsreg_28xxx_NMM,
       "s3reg-8xx": s3reg_8xx,
       "s3reg-810M-enetNMM": s3reg_810M_enetNMM,
       "s5reg-5005": s5reg_5005,
       "s5reg-5005-ethNMM": s5reg_5005_ethNMM,
       "s5reg-5005-tokNMM": s5reg_5005_tokNMM,
       "s5reg-5005-ethSwitchNMM": s5reg_5005_ethSwitchNMM,
       "s5reg-5005-fddNMM": s5reg_5005_fddNMM,
       "s5reg-5005-ethFastEthNMM": s5reg_5005_ethFastEthNMM,
       "s5reg-5005-eth10-100SwitchNMM": s5reg_5005_eth10_100SwitchNMM,
       "s3reg-AlcatelConc": s3reg_AlcatelConc,
       "s3reg-AlcatelEthConc-enetNMM": s3reg_AlcatelEthConc_enetNMM,
       "s3reg-271XSA": s3reg_271XSA,
       "s3reg-271XSA-trNMM": s3reg_271XSA_trNMM,
       "ecreg-1032x": ecreg_1032x,
       "s3reg-1032x-NMM": s3reg_1032x_NMM,
       "sreg-5DN00x": sreg_5DN00x,
       "sreg-5DN00x-EthNMM": sreg_5DN00x_EthNMM,
       "sreg-BayStackEth": sreg_BayStackEth,
       "sreg-BayStackEth-ethNMM": sreg_BayStackEth_ethNMM,
       "sreg-2300x": sreg_2300x,
       "sreg-2300x-NMM": sreg_2300x_NMM,
       "sreg-2310x": sreg_2310x,
       "sreg-2310x-NMM": sreg_2310x_NMM,
       "sreg-Orion": sreg_Orion,
       "sreg-Orion-ethNMM": sreg_Orion_ethNMM,
       "sreg-BayStack100Hub": sreg_BayStack100Hub,
       "sreg-BayStack100Unit-12Port": sreg_BayStack100Unit_12Port,
       "sreg-BayStackTr": sreg_BayStackTr,
       "sreg-BayStackTr-trNMM": sreg_BayStackTr_trNMM,
       "lsreg-28200": lsreg_28200,
       "lsreg-28200-ethSwitchNMM": lsreg_28200_ethSwitchNMM,
       "sreg-BayStack302": sreg_BayStack302,
       "sreg-BayStack302-9port": sreg_BayStack302_9port,
       "sreg-BayStack350": sreg_BayStack350,
       "sreg-BayStack350-ethSwitchNMM": sreg_BayStack350_ethSwitchNMM,
       "sreg-BayStack350-24T-ethSwitchNMM": sreg_BayStack350_24T_ethSwitchNMM,
       "sreg-BayStack150Eth": sreg_BayStack150Eth,
       "sreg-BayStack150Eth-ethNMM": sreg_BayStack150Eth_ethNMM,
       "sreg-BayStack303-304": sreg_BayStack303_304,
       "sreg-BayStack303-304-Sw": sreg_BayStack303_304_Sw,
       "sreg-BayStack303-24T-Sw": sreg_BayStack303_24T_Sw,
       "sreg-BayStack200Eth": sreg_BayStack200Eth,
       "sreg-BayStack200Eth-ethNMM": sreg_BayStack200Eth_ethNMM,
       "sreg-BayStack250Eth": sreg_BayStack250Eth,
       "sreg-BayStack250Eth-ethNMM": sreg_BayStack250Eth_ethNMM,
       "sreg-BayStack450": sreg_BayStack450,
       "sreg-BayStack450-ethSwitchNMM": sreg_BayStack450_ethSwitchNMM,
       "sreg-BayStack410": sreg_BayStack410,
       "sreg-BayStack410-24T-ethSwitchNMM": sreg_BayStack410_24T_ethSwitchNMM,
       "sreg-BayStackICS": sreg_BayStackICS,
       "sreg-BayStackICS-NMM": sreg_BayStackICS_NMM,
       "s5reg-Accelar8010": s5reg_Accelar8010,
       "s5reg-Accelar8132TX": s5reg_Accelar8132TX,
       "s5reg-Accelar8148TX": s5reg_Accelar8148TX,
       "sreg-BayStack670": sreg_BayStack670,
       "sreg-BayStack670-wirelessLAN": sreg_BayStack670_wirelessLAN,
       "sreg-BPS2000": sreg_BPS2000,
       "sreg-BPS2000-24T-ethSwitchNMM": sreg_BPS2000_24T_ethSwitchNMM,
       "sreg-BayStack3580": sreg_BayStack3580,
       "sreg-BayStack3580-16F-gigEthSwitch": sreg_BayStack3580_16F_gigEthSwitch,
       "sreg-BayStack10": sreg_BayStack10,
       "sreg-BayStack10-powerSupplyUnit": sreg_BayStack10_powerSupplyUnit,
       "sreg-BayStack420": sreg_BayStack420,
       "sreg-BayStack420-24T-ethSwitchNMM": sreg_BayStack420_24T_ethSwitchNMM,
       "sreg-Metro1200ESM": sreg_Metro1200ESM,
       "sreg-Metro1200ESM-12T-ethSwitchNMM": sreg_Metro1200ESM_12T_ethSwitchNMM,
       "sreg-BayStack380": sreg_BayStack380,
       "sreg-BayStack380-24T-ethSwitchNMM": sreg_BayStack380_24T_ethSwitchNMM,
       "sreg-BayStack470": sreg_BayStack470,
       "sreg-BayStack470-48T-ethSwitchNMM": sreg_BayStack470_48T_ethSwitchNMM,
       "sreg-Metro1450ESM": sreg_Metro1450ESM,
       "sreg-Metro1450ESM-12T2GBIC-ethSwitchNMM": sreg_Metro1450ESM_12T2GBIC_ethSwitchNMM,
       "sreg-Metro1400ESM": sreg_Metro1400ESM,
       "sreg-Metro1400ESM-12T2GBIC-ethSwitchNMM": sreg_Metro1400ESM_12T2GBIC_ethSwitchNMM,
       "sreg-BayStack460-24T-PWR": sreg_BayStack460_24T_PWR,
       "sreg-BayStack460-24T-PWR-ethSwitchNMM": sreg_BayStack460_24T_PWR_ethSwitchNMM,
       "sreg-Metro8000": sreg_Metro8000,
       "sreg-Metro8000-8664GB-OPM": sreg_Metro8000_8664GB_OPM,
       "sreg-BayStack380-24F": sreg_BayStack380_24F,
       "sreg-BayStack380-24F-ethSwitchNMM": sreg_BayStack380_24F_ethSwitchNMM,
       "sreg-BayStack5510-24T": sreg_BayStack5510_24T,
       "sreg-BayStack5510-24T-ethSwitchNMM": sreg_BayStack5510_24T_ethSwitchNMM,
       "sreg-BayStack5510-48T": sreg_BayStack5510_48T,
       "sreg-BayStack5510-48T-ethSwitchNMM": sreg_BayStack5510_48T_ethSwitchNMM,
       "sreg-BayStack470-24T": sreg_BayStack470_24T,
       "sreg-BayStack470-24T-ethSwitchNMM": sreg_BayStack470_24T_ethSwitchNMM,
       "sreg-WLANAccessPoint2220": sreg_WLANAccessPoint2220,
       "sreg-WLANAccessPoint2220-wirelessAP": sreg_WLANAccessPoint2220_wirelessAP,
       "sreg-WLANSecuritySwitch2250": sreg_WLANSecuritySwitch2250,
       "sreg-BayStack425": sreg_BayStack425,
       "sreg-BayStack425-48T": sreg_BayStack425_48T,
       "sreg-BayStack425-24T": sreg_BayStack425_24T,
       "sreg-WLANAccessPoint2221": sreg_WLANAccessPoint2221,
       "sreg-WLANAccessPoint2221-wirelessAP": sreg_WLANAccessPoint2221_wirelessAP,
       "sreg-BayStack5520": sreg_BayStack5520,
       "sreg-BayStack5520-24T-PWR": sreg_BayStack5520_24T_PWR,
       "sreg-BayStack5520-48T-PWR": sreg_BayStack5520_48T_PWR,
       "sreg-WLANSecuritySwitch": sreg_WLANSecuritySwitch,
       "sreg-WLANSecuritySwitch2270": sreg_WLANSecuritySwitch2270,
       "sreg-BayStack325": sreg_BayStack325,
       "sreg-BayStack325-24T": sreg_BayStack325_24T,
       "sreg-BayStack325-24G": sreg_BayStack325_24G,
       "sreg-WLANAccessPoint2225": sreg_WLANAccessPoint2225,
       "sreg-WLANAccessPoint2225-wirelessAP": sreg_WLANAccessPoint2225_wirelessAP,
       "sreg-BayStack470-24T-PWR": sreg_BayStack470_24T_PWR,
       "sreg-BayStack470-24T-PWR-ethSwitchNMM": sreg_BayStack470_24T_PWR_ethSwitchNMM,
       "sreg-BayStack470-48T-PWR": sreg_BayStack470_48T_PWR,
       "sreg-BayStack470-48T-PWR-ethSwitchNMM": sreg_BayStack470_48T_PWR_ethSwitchNMM,
       "sreg-EthernetRoutingSwitch5530-24TFD": sreg_EthernetRoutingSwitch5530_24TFD,
       "sreg-EthernetSwitch3510-24T": sreg_EthernetSwitch3510_24T,
       "sreg-NortelWLAN": sreg_NortelWLAN,
       "sreg-NortelWLAN2350": sreg_NortelWLAN2350,
       "sreg-NortelWLAN2360": sreg_NortelWLAN2360,
       "sreg-NortelWLAN2361": sreg_NortelWLAN2361,
       "sreg-NortelWLAN2370": sreg_NortelWLAN2370,
       "sreg-NortelWLAN2380": sreg_NortelWLAN2380,
       "sreg-NortelMX2800": sreg_NortelMX2800,
       "sreg-SMB-BES": sreg_SMB_BES,
       "sreg-SMB-BES-GIG": sreg_SMB_BES_GIG,
       "sreg-SMB-BES-1010-24T": sreg_SMB_BES_1010_24T,
       "sreg-SMB-BES-1010-48T": sreg_SMB_BES_1010_48T,
       "sreg-SMB-BES-1020-24T-PWR": sreg_SMB_BES_1020_24T_PWR,
       "sreg-SMB-BES-1020-48T-PWR": sreg_SMB_BES_1020_48T_PWR,
       "sreg-SMB-BES-2010-24T": sreg_SMB_BES_2010_24T,
       "sreg-SMB-BES-2010-48T": sreg_SMB_BES_2010_48T,
       "sreg-SMB-BES-2020-24T-PWR": sreg_SMB_BES_2020_24T_PWR,
       "sreg-SMB-BES-2020-48T-PWR": sreg_SMB_BES_2020_48T_PWR,
       "sreg-SMB-BES-FE": sreg_SMB_BES_FE,
       "sreg-SMB-BES-110-24T": sreg_SMB_BES_110_24T,
       "sreg-SMB-BES-110-48T": sreg_SMB_BES_110_48T,
       "sreg-SMB-BES-120-24T-PWR": sreg_SMB_BES_120_24T_PWR,
       "sreg-SMB-BES-120-48T-PWR": sreg_SMB_BES_120_48T_PWR,
       "sreg-SMB-BES-210-24T": sreg_SMB_BES_210_24T,
       "sreg-SMB-BES-210-48T": sreg_SMB_BES_210_48T,
       "sreg-SMB-BES-220-24T-PWR": sreg_SMB_BES_220_24T_PWR,
       "sreg-SMB-BES-220-48T-PWR": sreg_SMB_BES_220_48T_PWR,
       "sreg-SMB-BES-50-FE-12T-PWR": sreg_SMB_BES_50_FE_12T_PWR,
       "sreg-SMB-BES-50-FE-24T-PWR": sreg_SMB_BES_50_FE_24T_PWR,
       "sreg-SMB-BES-50-GE-12T-PWR": sreg_SMB_BES_50_GE_12T_PWR,
       "sreg-SMB-BES-50-GE-24T-PWR": sreg_SMB_BES_50_GE_24T_PWR,
       "sreg-SMB-BAP": sreg_SMB_BAP,
       "sreg-SMB-BAP-WirelessAccessPoint": sreg_SMB_BAP_WirelessAccessPoint,
       "sreg-SMB-BAP-WirelessAccessPoint-BAP110": sreg_SMB_BAP_WirelessAccessPoint_BAP110,
       "sreg-SMB-BAP-WirelessAccessPoint-BAP120": sreg_SMB_BAP_WirelessAccessPoint_BAP120,
       "sreg-SMB-BSR": sreg_SMB_BSR,
       "sreg-SMB-BSR222": sreg_SMB_BSR222,
       "sreg-SMB-BSR252": sreg_SMB_BSR252,
       "sreg-ERS-45xx": sreg_ERS_45xx,
       "sreg-ERS-4548GT": sreg_ERS_4548GT,
       "sreg-ERS-4548GT-PWR": sreg_ERS_4548GT_PWR,
       "sreg-ERS-4550T": sreg_ERS_4550T,
       "sreg-ERS-4550T-PWR": sreg_ERS_4550T_PWR,
       "sreg-ERS-4526FX": sreg_ERS_4526FX,
       "sreg-ERS-4526GTX-PWR": sreg_ERS_4526GTX_PWR,
       "sreg-ERS-4526GTX": sreg_ERS_4526GTX,
       "sreg-ERS-4524GT": sreg_ERS_4524GT,
       "sreg-ERS-4526T-PWR": sreg_ERS_4526T_PWR,
       "sreg-ERS-4526T": sreg_ERS_4526T,
       "sreg-ERS-4524GT-PWR": sreg_ERS_4524GT_PWR,
       "sreg-ERS-4526T-PWR-PLUS": sreg_ERS_4526T_PWR_PLUS,
       "sreg-ERS-4550T-PWR-PLUS": sreg_ERS_4550T_PWR_PLUS,
       "sreg-ERS-25xx": sreg_ERS_25xx,
       "sreg-ERS-2500-26T": sreg_ERS_2500_26T,
       "sreg-ERS-2500-26T-PWR": sreg_ERS_2500_26T_PWR,
       "sreg-ERS-2500-50T": sreg_ERS_2500_50T,
       "sreg-ERS-2500-50T-PWR": sreg_ERS_2500_50T_PWR,
       "sreg-SMB-BSG": sreg_SMB_BSG,
       "sreg-SMB-BSGX4E": sreg_SMB_BSGX4E,
       "sreg-SMB-BSG8EW": sreg_SMB_BSG8EW,
       "sreg-SMB-BSG12AW": sreg_SMB_BSG12AW,
       "sreg-SMB-BSG12TW": sreg_SMB_BSG12TW,
       "sreg-SMB-BSG12EW": sreg_SMB_BSG12EW,
       "sreg-ERS-56xx": sreg_ERS_56xx,
       "sreg-ERS-5698-TFD-PWR": sreg_ERS_5698_TFD_PWR,
       "sreg-ERS-5698-TFD": sreg_ERS_5698_TFD,
       "sreg-ERS-5650-TD-PWR": sreg_ERS_5650_TD_PWR,
       "sreg-ERS-5650-TD": sreg_ERS_5650_TD,
       "sreg-ERS-5632-FD": sreg_ERS_5632_FD,
       "sreg-ESU-18xx": sreg_ESU_18xx,
       "sreg-ESU-1860-T": sreg_ESU_1860_T,
       "sreg-ESU-1880-S": sreg_ESU_1880_S,
       "sreg-ESU-1860-V": sreg_ESU_1860_V,
       "sreg-ESU-1860-S": sreg_ESU_1860_S,
       "sreg-ESU-1860-B": sreg_ESU_1860_B,
       "sreg-ERS-66xx": sreg_ERS_66xx,
       "sreg-ERS-6628-XSGT": sreg_ERS_6628_XSGT,
       "sreg-ERS-6632-XTS": sreg_ERS_6632_XTS,
       "sreg-WC-8xxx": sreg_WC_8xxx,
       "sreg-WC-8180": sreg_WC_8180,
       "sreg-ERS-48xx": sreg_ERS_48xx,
       "sreg-ERS-4826GTS-PWR-PLUS": sreg_ERS_4826GTS_PWR_PLUS,
       "sreg-ERS-4850GTS-PWR-PLUS": sreg_ERS_4850GTS_PWR_PLUS,
       "sreg-ERS-4826GTS": sreg_ERS_4826GTS,
       "sreg-ERS-4850GTS": sreg_ERS_4850GTS,
       "sreg-VSP-7xxx": sreg_VSP_7xxx,
       "sreg-VSP-7024XLS": sreg_VSP_7024XLS,
       "sreg-VSP-7024XT": sreg_VSP_7024XT,
       "sreg-ERS-35xx": sreg_ERS_35xx,
       "sreg-ERS-3526T": sreg_ERS_3526T,
       "sreg-ERS-3526T-PWR-PLUS": sreg_ERS_3526T_PWR_PLUS,
       "sreg-ERS-3524GT": sreg_ERS_3524GT,
       "sreg-ERS-3524GT-PWR-PLUS": sreg_ERS_3524GT_PWR_PLUS,
       "sreg-ERS-3510GT": sreg_ERS_3510GT,
       "sreg-ERS-3510GT-PWR-PLUS": sreg_ERS_3510GT_PWR_PLUS,
       "sreg-ERS-3549GTS": sreg_ERS_3549GTS,
       "sreg-ERS-3549GTS-PWR-PLUS": sreg_ERS_3549GTS_PWR_PLUS,
       "sreg-ERS-3550T": sreg_ERS_3550T,
       "sreg-ERS-3550T-PWR-PLUS": sreg_ERS_3550T_PWR_PLUS,
       "sreg-ERS59xx": sreg_ERS59xx,
       "sreg-ERS5928GTS": sreg_ERS5928GTS,
       "sreg-ERS5928GTS-PWR-PLUS": sreg_ERS5928GTS_PWR_PLUS,
       "sreg-ERS5952GTS": sreg_ERS5952GTS,
       "sreg-ERS5952GTS-PWR-PLUS": sreg_ERS5952GTS_PWR_PLUS,
       "sreg-ERS5928GTS-UPWR": sreg_ERS5928GTS_UPWR,
       "sreg-ERS59100GTS": sreg_ERS59100GTS,
       "sreg-ERS59100GTS-PWR-PLUS": sreg_ERS59100GTS_PWR_PLUS,
       "sreg-ERS49": sreg_ERS49,
       "sreg-ERS4926GTS": sreg_ERS4926GTS,
       "sreg-ERS4926GTS-PWR-PLUS": sreg_ERS4926GTS_PWR_PLUS,
       "sreg-ERS4950GTS": sreg_ERS4950GTS,
       "sreg-ERS4950GTS-PWR-PLUS": sreg_ERS4950GTS_PWR_PLUS,
       "policy": policy,
       "bayStackMibs": bayStackMibs,
       "ntwsTrapezeNetworks": ntwsTrapezeNetworks,
       "avayaWlanMibs": avayaWlanMibs,
       "avayaWlan9100Mibs": avayaWlan9100Mibs}
)
