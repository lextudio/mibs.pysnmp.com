# SNMP MIB module (WIENER-CRATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WIENER-CRATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:56 2024
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

wiener = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19947)
)
wiener.setRevisions(
        ("2019-04-03 00:00",
         "2016-02-18 00:00",
         "2008-10-09 00:00",
         "2008-05-06 00:00",
         "2008-04-15 00:00",
         "2008-04-10 00:00",
         "2008-04-02 00:00",
         "2007-09-10 00:00",
         "2007-03-16 00:00",
         "2005-02-01 00:00",
         "2004-06-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Float(Opaque, TextualConvention):
    status = "current"
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )



class OutputTripTime(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class OutputTripAction(Integer32, TextualConvention):
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
        *(("allOff", 3),
          ("channelOff", 1),
          ("ignore", 0),
          ("specialOff", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Crate_ObjectIdentity = ObjectIdentity
crate = _Crate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19947, 1)
)
if mibBuilder.loadTexts:
    crate.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19947, 1, 1)
)
if mibBuilder.loadTexts:
    system.setStatus("current")


class _SysMainSwitch_Type(Integer32):
    """Custom type sysMainSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SysMainSwitch_Type.__name__ = "Integer32"
_SysMainSwitch_Object = MibTableColumn
sysMainSwitch = _SysMainSwitch_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 1, 1),
    _SysMainSwitch_Type()
)
sysMainSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMainSwitch.setStatus("current")


class _SysStatus_Type(Bits):
    """Custom type sysStatus based on Bits"""
    namedValues = NamedValues(
        *(("busReset", 9),
          ("fantrayFailure", 5),
          ("inputFailure", 3),
          ("localControlOnly", 2),
          ("mainInhibit", 1),
          ("mainOn", 0),
          ("outputFailure", 4),
          ("plugAndPlayIncompatible", 8),
          ("sensorFailure", 6),
          ("supplyDerating", 10),
          ("supplyDerating2", 12),
          ("supplyFailure", 11),
          ("supplyFailure2", 13),
          ("vmeSysfail", 7))
    )

_SysStatus_Type.__name__ = "Bits"
_SysStatus_Object = MibTableColumn
sysStatus = _SysStatus_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 1, 2),
    _SysStatus_Type()
)
sysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStatus.setStatus("current")


class _SysVmeSysReset_Type(Integer32):
    """Custom type sysVmeSysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("trigger", 1)
    )


_SysVmeSysReset_Type.__name__ = "Integer32"
_SysVmeSysReset_Object = MibTableColumn
sysVmeSysReset = _SysVmeSysReset_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 1, 3),
    _SysVmeSysReset_Type()
)
sysVmeSysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysVmeSysReset.setStatus("current")
_SysHardwareReset_Type = Integer32
_SysHardwareReset_Object = MibTableColumn
sysHardwareReset = _SysHardwareReset_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 1, 4),
    _SysHardwareReset_Type()
)
sysHardwareReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHardwareReset.setStatus("current")


class _SysFactoryDefaults_Type(Integer32):
    """Custom type sysFactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SysFactoryDefaults_Type.__name__ = "Integer32"
_SysFactoryDefaults_Object = MibTableColumn
sysFactoryDefaults = _SysFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 1, 5),
    _SysFactoryDefaults_Type()
)
sysFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFactoryDefaults.setStatus("current")


class _SysConfigDoMeasurementCurrent_Type(Bits):
    """Custom type sysConfigDoMeasurementCurrent based on Bits"""
    namedValues = NamedValues(
        *(("ch0", 0),
          ("ch1", 1),
          ("ch2", 2),
          ("ch3", 3),
          ("ch4", 4),
          ("ch5", 5),
          ("ch6", 6),
          ("ch7", 7))
    )

_SysConfigDoMeasurementCurrent_Type.__name__ = "Bits"
_SysConfigDoMeasurementCurrent_Object = MibTableColumn
sysConfigDoMeasurementCurrent = _SysConfigDoMeasurementCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 1, 10),
    _SysConfigDoMeasurementCurrent_Type()
)
sysConfigDoMeasurementCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigDoMeasurementCurrent.setStatus("current")
_SysOperatingTime_Type = Integer32
_SysOperatingTime_Object = MibTableColumn
sysOperatingTime = _SysOperatingTime_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 1, 11),
    _SysOperatingTime_Type()
)
sysOperatingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysOperatingTime.setStatus("current")
if mibBuilder.loadTexts:
    sysOperatingTime.setUnits("s")


class _SysDebugMemory8_Type(Integer32):
    """Custom type sysDebugMemory8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SysDebugMemory8_Type.__name__ = "Integer32"
_SysDebugMemory8_Object = MibTableColumn
sysDebugMemory8 = _SysDebugMemory8_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 1, 1024),
    _SysDebugMemory8_Type()
)
sysDebugMemory8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDebugMemory8.setStatus("current")


class _SysDebugMemory16_Type(Integer32):
    """Custom type sysDebugMemory16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysDebugMemory16_Type.__name__ = "Integer32"
_SysDebugMemory16_Object = MibTableColumn
sysDebugMemory16 = _SysDebugMemory16_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 1, 1025),
    _SysDebugMemory16_Type()
)
sysDebugMemory16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDebugMemory16.setStatus("current")


class _SysDebugMemory32_Type(Integer32):
    """Custom type sysDebugMemory32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_SysDebugMemory32_Type.__name__ = "Integer32"
_SysDebugMemory32_Object = MibTableColumn
sysDebugMemory32 = _SysDebugMemory32_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 1, 1026),
    _SysDebugMemory32_Type()
)
sysDebugMemory32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDebugMemory32.setStatus("current")


class _SysDebug_Type(OctetString):
    """Custom type sysDebug based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(520, 520),
    )


_SysDebug_Type.__name__ = "OctetString"
_SysDebug_Object = MibTableColumn
sysDebug = _SysDebug_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 1, 1027),
    _SysDebug_Type()
)
sysDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDebug.setStatus("current")
_SysDebugDisplay_Type = OctetString
_SysDebugDisplay_Object = MibTableColumn
sysDebugDisplay = _SysDebugDisplay_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 1, 1028),
    _SysDebugDisplay_Type()
)
sysDebugDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDebugDisplay.setStatus("current")
_SysDebugBoot_Type = OctetString
_SysDebugBoot_Object = MibTableColumn
sysDebugBoot = _SysDebugBoot_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 1, 1029),
    _SysDebugBoot_Type()
)
sysDebugBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDebugBoot.setStatus("current")
_Input_ObjectIdentity = ObjectIdentity
input = _Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19947, 1, 2)
)
if mibBuilder.loadTexts:
    input.setStatus("current")
_Output_ObjectIdentity = ObjectIdentity
output = _Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3)
)
if mibBuilder.loadTexts:
    output.setStatus("current")


class _OutputNumber_Type(Integer32):
    """Custom type outputNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1999),
    )


_OutputNumber_Type.__name__ = "Integer32"
_OutputNumber_Object = MibScalar
outputNumber = _OutputNumber_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 1),
    _OutputNumber_Type()
)
outputNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputNumber.setStatus("current")
_OutputTable_Object = MibTable
outputTable = _OutputTable_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2)
)
if mibBuilder.loadTexts:
    outputTable.setStatus("current")
_OutputEntry_Object = MibTableRow
outputEntry = _OutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1)
)
outputEntry.setIndexNames(
    (0, "WIENER-CRATE-MIB", "outputIndex"),
)
if mibBuilder.loadTexts:
    outputEntry.setStatus("current")


class _OutputIndex_Type(Integer32):
    """Custom type outputIndex based on Integer32"""
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
              749,
              750,
              751,
              752,
              753,
              754,
              755,
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
              847,
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
              864,
              865,
              866,
              867,
              868,
              869,
              870,
              871,
              872,
              873,
              874,
              875,
              876,
              877,
              878,
              879,
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
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008,
              1009,
              1010,
              1011,
              1012,
              1013,
              1014,
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
              1999,
              2000)
        )
    )
    namedValues = NamedValues(
        *(("u0", 1),
          ("u1", 2),
          ("u10", 11),
          ("u100", 101),
          ("u1000", 1001),
          ("u1001", 1002),
          ("u1002", 1003),
          ("u1003", 1004),
          ("u1004", 1005),
          ("u1005", 1006),
          ("u1006", 1007),
          ("u1007", 1008),
          ("u1008", 1009),
          ("u1009", 1010),
          ("u101", 102),
          ("u1010", 1011),
          ("u1011", 1012),
          ("u1012", 1013),
          ("u1013", 1014),
          ("u1014", 1015),
          ("u1015", 1016),
          ("u1016", 1017),
          ("u1017", 1018),
          ("u1018", 1019),
          ("u1019", 1020),
          ("u102", 103),
          ("u1020", 1021),
          ("u1021", 1022),
          ("u1022", 1023),
          ("u1023", 1024),
          ("u1024", 1025),
          ("u1025", 1026),
          ("u1026", 1027),
          ("u1027", 1028),
          ("u1028", 1029),
          ("u1029", 1030),
          ("u103", 104),
          ("u1030", 1031),
          ("u1031", 1032),
          ("u1032", 1033),
          ("u1033", 1034),
          ("u1034", 1035),
          ("u1035", 1036),
          ("u1036", 1037),
          ("u1037", 1038),
          ("u1038", 1039),
          ("u1039", 1040),
          ("u104", 105),
          ("u1040", 1041),
          ("u1041", 1042),
          ("u1042", 1043),
          ("u1043", 1044),
          ("u1044", 1045),
          ("u1045", 1046),
          ("u1046", 1047),
          ("u1047", 1048),
          ("u1048", 1049),
          ("u1049", 1050),
          ("u105", 106),
          ("u1050", 1051),
          ("u1051", 1052),
          ("u1052", 1053),
          ("u1053", 1054),
          ("u1054", 1055),
          ("u1055", 1056),
          ("u1056", 1057),
          ("u1057", 1058),
          ("u1058", 1059),
          ("u1059", 1060),
          ("u106", 107),
          ("u1060", 1061),
          ("u1061", 1062),
          ("u1062", 1063),
          ("u1063", 1064),
          ("u1064", 1065),
          ("u1065", 1066),
          ("u1066", 1067),
          ("u1067", 1068),
          ("u1068", 1069),
          ("u1069", 1070),
          ("u107", 108),
          ("u1070", 1071),
          ("u1071", 1072),
          ("u1072", 1073),
          ("u1073", 1074),
          ("u1074", 1075),
          ("u1075", 1076),
          ("u1076", 1077),
          ("u1077", 1078),
          ("u1078", 1079),
          ("u1079", 1080),
          ("u108", 109),
          ("u1080", 1081),
          ("u1081", 1082),
          ("u1082", 1083),
          ("u1083", 1084),
          ("u1084", 1085),
          ("u1085", 1086),
          ("u1086", 1087),
          ("u1087", 1088),
          ("u1088", 1089),
          ("u1089", 1090),
          ("u109", 110),
          ("u1090", 1091),
          ("u1091", 1092),
          ("u1092", 1093),
          ("u1093", 1094),
          ("u1094", 1095),
          ("u1095", 1096),
          ("u1096", 1097),
          ("u1097", 1098),
          ("u1098", 1099),
          ("u1099", 1100),
          ("u11", 12),
          ("u110", 111),
          ("u1100", 1101),
          ("u1101", 1102),
          ("u1102", 1103),
          ("u1103", 1104),
          ("u1104", 1105),
          ("u1105", 1106),
          ("u1106", 1107),
          ("u1107", 1108),
          ("u1108", 1109),
          ("u1109", 1110),
          ("u111", 112),
          ("u1110", 1111),
          ("u1111", 1112),
          ("u1112", 1113),
          ("u1113", 1114),
          ("u1114", 1115),
          ("u1115", 1116),
          ("u1116", 1117),
          ("u1117", 1118),
          ("u1118", 1119),
          ("u1119", 1120),
          ("u112", 113),
          ("u1120", 1121),
          ("u1121", 1122),
          ("u1122", 1123),
          ("u1123", 1124),
          ("u1124", 1125),
          ("u1125", 1126),
          ("u1126", 1127),
          ("u1127", 1128),
          ("u1128", 1129),
          ("u1129", 1130),
          ("u113", 114),
          ("u1130", 1131),
          ("u1131", 1132),
          ("u1132", 1133),
          ("u1133", 1134),
          ("u1134", 1135),
          ("u1135", 1136),
          ("u1136", 1137),
          ("u1137", 1138),
          ("u1138", 1139),
          ("u1139", 1140),
          ("u114", 115),
          ("u1140", 1141),
          ("u1141", 1142),
          ("u1142", 1143),
          ("u1143", 1144),
          ("u1144", 1145),
          ("u1145", 1146),
          ("u1146", 1147),
          ("u1147", 1148),
          ("u1148", 1149),
          ("u1149", 1150),
          ("u115", 116),
          ("u1150", 1151),
          ("u1151", 1152),
          ("u1152", 1153),
          ("u1153", 1154),
          ("u1154", 1155),
          ("u1155", 1156),
          ("u1156", 1157),
          ("u1157", 1158),
          ("u1158", 1159),
          ("u1159", 1160),
          ("u116", 117),
          ("u1160", 1161),
          ("u1161", 1162),
          ("u1162", 1163),
          ("u1163", 1164),
          ("u1164", 1165),
          ("u1165", 1166),
          ("u1166", 1167),
          ("u1167", 1168),
          ("u1168", 1169),
          ("u1169", 1170),
          ("u117", 118),
          ("u1170", 1171),
          ("u1171", 1172),
          ("u1172", 1173),
          ("u1173", 1174),
          ("u1174", 1175),
          ("u1175", 1176),
          ("u1176", 1177),
          ("u1177", 1178),
          ("u1178", 1179),
          ("u1179", 1180),
          ("u118", 119),
          ("u1180", 1181),
          ("u1181", 1182),
          ("u1182", 1183),
          ("u1183", 1184),
          ("u1184", 1185),
          ("u1185", 1186),
          ("u1186", 1187),
          ("u1187", 1188),
          ("u1188", 1189),
          ("u1189", 1190),
          ("u119", 120),
          ("u1190", 1191),
          ("u1191", 1192),
          ("u1192", 1193),
          ("u1193", 1194),
          ("u1194", 1195),
          ("u1195", 1196),
          ("u1196", 1197),
          ("u1197", 1198),
          ("u1198", 1199),
          ("u1199", 1200),
          ("u12", 13),
          ("u120", 121),
          ("u1200", 1201),
          ("u1201", 1202),
          ("u1202", 1203),
          ("u1203", 1204),
          ("u1204", 1205),
          ("u1205", 1206),
          ("u1206", 1207),
          ("u1207", 1208),
          ("u1208", 1209),
          ("u1209", 1210),
          ("u121", 122),
          ("u1210", 1211),
          ("u1211", 1212),
          ("u1212", 1213),
          ("u1213", 1214),
          ("u1214", 1215),
          ("u1215", 1216),
          ("u1216", 1217),
          ("u1217", 1218),
          ("u1218", 1219),
          ("u1219", 1220),
          ("u122", 123),
          ("u1220", 1221),
          ("u1221", 1222),
          ("u1222", 1223),
          ("u1223", 1224),
          ("u1224", 1225),
          ("u1225", 1226),
          ("u1226", 1227),
          ("u1227", 1228),
          ("u1228", 1229),
          ("u1229", 1230),
          ("u123", 124),
          ("u1230", 1231),
          ("u1231", 1232),
          ("u1232", 1233),
          ("u1233", 1234),
          ("u1234", 1235),
          ("u1235", 1236),
          ("u1236", 1237),
          ("u1237", 1238),
          ("u1238", 1239),
          ("u1239", 1240),
          ("u124", 125),
          ("u1240", 1241),
          ("u1241", 1242),
          ("u1242", 1243),
          ("u1243", 1244),
          ("u1244", 1245),
          ("u1245", 1246),
          ("u1246", 1247),
          ("u1247", 1248),
          ("u1248", 1249),
          ("u1249", 1250),
          ("u125", 126),
          ("u1250", 1251),
          ("u1251", 1252),
          ("u1252", 1253),
          ("u1253", 1254),
          ("u1254", 1255),
          ("u1255", 1256),
          ("u1256", 1257),
          ("u1257", 1258),
          ("u1258", 1259),
          ("u1259", 1260),
          ("u126", 127),
          ("u1260", 1261),
          ("u1261", 1262),
          ("u1262", 1263),
          ("u1263", 1264),
          ("u1264", 1265),
          ("u1265", 1266),
          ("u1266", 1267),
          ("u1267", 1268),
          ("u1268", 1269),
          ("u1269", 1270),
          ("u127", 128),
          ("u1270", 1271),
          ("u1271", 1272),
          ("u1272", 1273),
          ("u1273", 1274),
          ("u1274", 1275),
          ("u1275", 1276),
          ("u1276", 1277),
          ("u1277", 1278),
          ("u1278", 1279),
          ("u1279", 1280),
          ("u128", 129),
          ("u1280", 1281),
          ("u1281", 1282),
          ("u1282", 1283),
          ("u1283", 1284),
          ("u1284", 1285),
          ("u1285", 1286),
          ("u1286", 1287),
          ("u1287", 1288),
          ("u1288", 1289),
          ("u1289", 1290),
          ("u129", 130),
          ("u1290", 1291),
          ("u1291", 1292),
          ("u1292", 1293),
          ("u1293", 1294),
          ("u1294", 1295),
          ("u1295", 1296),
          ("u1296", 1297),
          ("u1297", 1298),
          ("u1298", 1299),
          ("u1299", 1300),
          ("u13", 14),
          ("u130", 131),
          ("u1300", 1301),
          ("u1301", 1302),
          ("u1302", 1303),
          ("u1303", 1304),
          ("u1304", 1305),
          ("u1305", 1306),
          ("u1306", 1307),
          ("u1307", 1308),
          ("u1308", 1309),
          ("u1309", 1310),
          ("u131", 132),
          ("u1310", 1311),
          ("u1311", 1312),
          ("u1312", 1313),
          ("u1313", 1314),
          ("u1314", 1315),
          ("u1315", 1316),
          ("u1316", 1317),
          ("u1317", 1318),
          ("u1318", 1319),
          ("u1319", 1320),
          ("u132", 133),
          ("u1320", 1321),
          ("u1321", 1322),
          ("u1322", 1323),
          ("u1323", 1324),
          ("u1324", 1325),
          ("u1325", 1326),
          ("u1326", 1327),
          ("u1327", 1328),
          ("u1328", 1329),
          ("u1329", 1330),
          ("u133", 134),
          ("u1330", 1331),
          ("u1331", 1332),
          ("u1332", 1333),
          ("u1333", 1334),
          ("u1334", 1335),
          ("u1335", 1336),
          ("u1336", 1337),
          ("u1337", 1338),
          ("u1338", 1339),
          ("u1339", 1340),
          ("u134", 135),
          ("u1340", 1341),
          ("u1341", 1342),
          ("u1342", 1343),
          ("u1343", 1344),
          ("u1344", 1345),
          ("u1345", 1346),
          ("u1346", 1347),
          ("u1347", 1348),
          ("u1348", 1349),
          ("u1349", 1350),
          ("u135", 136),
          ("u1350", 1351),
          ("u1351", 1352),
          ("u1352", 1353),
          ("u1353", 1354),
          ("u1354", 1355),
          ("u1355", 1356),
          ("u1356", 1357),
          ("u1357", 1358),
          ("u1358", 1359),
          ("u1359", 1360),
          ("u136", 137),
          ("u1360", 1361),
          ("u1361", 1362),
          ("u1362", 1363),
          ("u1363", 1364),
          ("u1364", 1365),
          ("u1365", 1366),
          ("u1366", 1367),
          ("u1367", 1368),
          ("u1368", 1369),
          ("u1369", 1370),
          ("u137", 138),
          ("u1370", 1371),
          ("u1371", 1372),
          ("u1372", 1373),
          ("u1373", 1374),
          ("u1374", 1375),
          ("u1375", 1376),
          ("u1376", 1377),
          ("u1377", 1378),
          ("u1378", 1379),
          ("u1379", 1380),
          ("u138", 139),
          ("u1380", 1381),
          ("u1381", 1382),
          ("u1382", 1383),
          ("u1383", 1384),
          ("u1384", 1385),
          ("u1385", 1386),
          ("u1386", 1387),
          ("u1387", 1388),
          ("u1388", 1389),
          ("u1389", 1390),
          ("u139", 140),
          ("u1390", 1391),
          ("u1391", 1392),
          ("u1392", 1393),
          ("u1393", 1394),
          ("u1394", 1395),
          ("u1395", 1396),
          ("u1396", 1397),
          ("u1397", 1398),
          ("u1398", 1399),
          ("u1399", 1400),
          ("u14", 15),
          ("u140", 141),
          ("u1400", 1401),
          ("u1401", 1402),
          ("u1402", 1403),
          ("u1403", 1404),
          ("u1404", 1405),
          ("u1405", 1406),
          ("u1406", 1407),
          ("u1407", 1408),
          ("u1408", 1409),
          ("u1409", 1410),
          ("u141", 142),
          ("u1410", 1411),
          ("u1411", 1412),
          ("u1412", 1413),
          ("u1413", 1414),
          ("u1414", 1415),
          ("u1415", 1416),
          ("u1416", 1417),
          ("u1417", 1418),
          ("u1418", 1419),
          ("u1419", 1420),
          ("u142", 143),
          ("u1420", 1421),
          ("u1421", 1422),
          ("u1422", 1423),
          ("u1423", 1424),
          ("u1424", 1425),
          ("u1425", 1426),
          ("u1426", 1427),
          ("u1427", 1428),
          ("u1428", 1429),
          ("u1429", 1430),
          ("u143", 144),
          ("u1430", 1431),
          ("u1431", 1432),
          ("u1432", 1433),
          ("u1433", 1434),
          ("u1434", 1435),
          ("u1435", 1436),
          ("u1436", 1437),
          ("u1437", 1438),
          ("u1438", 1439),
          ("u1439", 1440),
          ("u144", 145),
          ("u1440", 1441),
          ("u1441", 1442),
          ("u1442", 1443),
          ("u1443", 1444),
          ("u1444", 1445),
          ("u1445", 1446),
          ("u1446", 1447),
          ("u1447", 1448),
          ("u1448", 1449),
          ("u1449", 1450),
          ("u145", 146),
          ("u1450", 1451),
          ("u1451", 1452),
          ("u1452", 1453),
          ("u1453", 1454),
          ("u1454", 1455),
          ("u1455", 1456),
          ("u1456", 1457),
          ("u1457", 1458),
          ("u1458", 1459),
          ("u1459", 1460),
          ("u146", 147),
          ("u1460", 1461),
          ("u1461", 1462),
          ("u1462", 1463),
          ("u1463", 1464),
          ("u1464", 1465),
          ("u1465", 1466),
          ("u1466", 1467),
          ("u1467", 1468),
          ("u1468", 1469),
          ("u1469", 1470),
          ("u147", 148),
          ("u1470", 1471),
          ("u1471", 1472),
          ("u1472", 1473),
          ("u1473", 1474),
          ("u1474", 1475),
          ("u1475", 1476),
          ("u1476", 1477),
          ("u1477", 1478),
          ("u1478", 1479),
          ("u1479", 1480),
          ("u148", 149),
          ("u1480", 1481),
          ("u1481", 1482),
          ("u1482", 1483),
          ("u1483", 1484),
          ("u1484", 1485),
          ("u1485", 1486),
          ("u1486", 1487),
          ("u1487", 1488),
          ("u1488", 1489),
          ("u1489", 1490),
          ("u149", 150),
          ("u1490", 1491),
          ("u1491", 1492),
          ("u1492", 1493),
          ("u1493", 1494),
          ("u1494", 1495),
          ("u1495", 1496),
          ("u1496", 1497),
          ("u1497", 1498),
          ("u1498", 1499),
          ("u1499", 1500),
          ("u15", 16),
          ("u150", 151),
          ("u1500", 1501),
          ("u1501", 1502),
          ("u1502", 1503),
          ("u1503", 1504),
          ("u1504", 1505),
          ("u1505", 1506),
          ("u1506", 1507),
          ("u1507", 1508),
          ("u1508", 1509),
          ("u1509", 1510),
          ("u151", 152),
          ("u1510", 1511),
          ("u1511", 1512),
          ("u1512", 1513),
          ("u1513", 1514),
          ("u1514", 1515),
          ("u1515", 1516),
          ("u1516", 1517),
          ("u1517", 1518),
          ("u1518", 1519),
          ("u1519", 1520),
          ("u152", 153),
          ("u1520", 1521),
          ("u1521", 1522),
          ("u1522", 1523),
          ("u1523", 1524),
          ("u1524", 1525),
          ("u1525", 1526),
          ("u1526", 1527),
          ("u1527", 1528),
          ("u1528", 1529),
          ("u1529", 1530),
          ("u153", 154),
          ("u1530", 1531),
          ("u1531", 1532),
          ("u1532", 1533),
          ("u1533", 1534),
          ("u1534", 1535),
          ("u1535", 1536),
          ("u1536", 1537),
          ("u1537", 1538),
          ("u1538", 1539),
          ("u1539", 1540),
          ("u154", 155),
          ("u1540", 1541),
          ("u1541", 1542),
          ("u1542", 1543),
          ("u1543", 1544),
          ("u1544", 1545),
          ("u1545", 1546),
          ("u1546", 1547),
          ("u1547", 1548),
          ("u1548", 1549),
          ("u1549", 1550),
          ("u155", 156),
          ("u1550", 1551),
          ("u1551", 1552),
          ("u1552", 1553),
          ("u1553", 1554),
          ("u1554", 1555),
          ("u1555", 1556),
          ("u1556", 1557),
          ("u1557", 1558),
          ("u1558", 1559),
          ("u1559", 1560),
          ("u156", 157),
          ("u1560", 1561),
          ("u1561", 1562),
          ("u1562", 1563),
          ("u1563", 1564),
          ("u1564", 1565),
          ("u1565", 1566),
          ("u1566", 1567),
          ("u1567", 1568),
          ("u1568", 1569),
          ("u1569", 1570),
          ("u157", 158),
          ("u1570", 1571),
          ("u1571", 1572),
          ("u1572", 1573),
          ("u1573", 1574),
          ("u1574", 1575),
          ("u1575", 1576),
          ("u1576", 1577),
          ("u1577", 1578),
          ("u1578", 1579),
          ("u1579", 1580),
          ("u158", 159),
          ("u1580", 1581),
          ("u1581", 1582),
          ("u1582", 1583),
          ("u1583", 1584),
          ("u1584", 1585),
          ("u1585", 1586),
          ("u1586", 1587),
          ("u1587", 1588),
          ("u1588", 1589),
          ("u1589", 1590),
          ("u159", 160),
          ("u1590", 1591),
          ("u1591", 1592),
          ("u1592", 1593),
          ("u1593", 1594),
          ("u1594", 1595),
          ("u1595", 1596),
          ("u1596", 1597),
          ("u1597", 1598),
          ("u1598", 1599),
          ("u1599", 1600),
          ("u16", 17),
          ("u160", 161),
          ("u1600", 1601),
          ("u1601", 1602),
          ("u1602", 1603),
          ("u1603", 1604),
          ("u1604", 1605),
          ("u1605", 1606),
          ("u1606", 1607),
          ("u1607", 1608),
          ("u1608", 1609),
          ("u1609", 1610),
          ("u161", 162),
          ("u1610", 1611),
          ("u1611", 1612),
          ("u1612", 1613),
          ("u1613", 1614),
          ("u1614", 1615),
          ("u1615", 1616),
          ("u1616", 1617),
          ("u1617", 1618),
          ("u1618", 1619),
          ("u1619", 1620),
          ("u162", 163),
          ("u1620", 1621),
          ("u1621", 1622),
          ("u1622", 1623),
          ("u1623", 1624),
          ("u1624", 1625),
          ("u1625", 1626),
          ("u1626", 1627),
          ("u1627", 1628),
          ("u1628", 1629),
          ("u1629", 1630),
          ("u163", 164),
          ("u1630", 1631),
          ("u1631", 1632),
          ("u1632", 1633),
          ("u1633", 1634),
          ("u1634", 1635),
          ("u1635", 1636),
          ("u1636", 1637),
          ("u1637", 1638),
          ("u1638", 1639),
          ("u1639", 1640),
          ("u164", 165),
          ("u1640", 1641),
          ("u1641", 1642),
          ("u1642", 1643),
          ("u1643", 1644),
          ("u1644", 1645),
          ("u1645", 1646),
          ("u1646", 1647),
          ("u1647", 1648),
          ("u1648", 1649),
          ("u1649", 1650),
          ("u165", 166),
          ("u1650", 1651),
          ("u1651", 1652),
          ("u1652", 1653),
          ("u1653", 1654),
          ("u1654", 1655),
          ("u1655", 1656),
          ("u1656", 1657),
          ("u1657", 1658),
          ("u1658", 1659),
          ("u1659", 1660),
          ("u166", 167),
          ("u1660", 1661),
          ("u1661", 1662),
          ("u1662", 1663),
          ("u1663", 1664),
          ("u1664", 1665),
          ("u1665", 1666),
          ("u1666", 1667),
          ("u1667", 1668),
          ("u1668", 1669),
          ("u1669", 1670),
          ("u167", 168),
          ("u1670", 1671),
          ("u1671", 1672),
          ("u1672", 1673),
          ("u1673", 1674),
          ("u1674", 1675),
          ("u1675", 1676),
          ("u1676", 1677),
          ("u1677", 1678),
          ("u1678", 1679),
          ("u1679", 1680),
          ("u168", 169),
          ("u1680", 1681),
          ("u1681", 1682),
          ("u1682", 1683),
          ("u1683", 1684),
          ("u1684", 1685),
          ("u1685", 1686),
          ("u1686", 1687),
          ("u1687", 1688),
          ("u1688", 1689),
          ("u1689", 1690),
          ("u169", 170),
          ("u1690", 1691),
          ("u1691", 1692),
          ("u1692", 1693),
          ("u1693", 1694),
          ("u1694", 1695),
          ("u1695", 1696),
          ("u1696", 1697),
          ("u1697", 1698),
          ("u1698", 1699),
          ("u1699", 1700),
          ("u17", 18),
          ("u170", 171),
          ("u1700", 1701),
          ("u1701", 1702),
          ("u1702", 1703),
          ("u1703", 1704),
          ("u1704", 1705),
          ("u1705", 1706),
          ("u1706", 1707),
          ("u1707", 1708),
          ("u1708", 1709),
          ("u1709", 1710),
          ("u171", 172),
          ("u1710", 1711),
          ("u1711", 1712),
          ("u1712", 1713),
          ("u1713", 1714),
          ("u1714", 1715),
          ("u1715", 1716),
          ("u1716", 1717),
          ("u1717", 1718),
          ("u1718", 1719),
          ("u1719", 1720),
          ("u172", 173),
          ("u1720", 1721),
          ("u1721", 1722),
          ("u1722", 1723),
          ("u1723", 1724),
          ("u1724", 1725),
          ("u1725", 1726),
          ("u1726", 1727),
          ("u1727", 1728),
          ("u1728", 1729),
          ("u1729", 1730),
          ("u173", 174),
          ("u1730", 1731),
          ("u1731", 1732),
          ("u1732", 1733),
          ("u1733", 1734),
          ("u1734", 1735),
          ("u1735", 1736),
          ("u1736", 1737),
          ("u1737", 1738),
          ("u1738", 1739),
          ("u1739", 1740),
          ("u174", 175),
          ("u1740", 1741),
          ("u1741", 1742),
          ("u1742", 1743),
          ("u1743", 1744),
          ("u1744", 1745),
          ("u1745", 1746),
          ("u1746", 1747),
          ("u1747", 1748),
          ("u1748", 1749),
          ("u1749", 1750),
          ("u175", 176),
          ("u1750", 1751),
          ("u1751", 1752),
          ("u1752", 1753),
          ("u1753", 1754),
          ("u1754", 1755),
          ("u1755", 1756),
          ("u1756", 1757),
          ("u1757", 1758),
          ("u1758", 1759),
          ("u1759", 1760),
          ("u176", 177),
          ("u1760", 1761),
          ("u1761", 1762),
          ("u1762", 1763),
          ("u1763", 1764),
          ("u1764", 1765),
          ("u1765", 1766),
          ("u1766", 1767),
          ("u1767", 1768),
          ("u1768", 1769),
          ("u1769", 1770),
          ("u177", 178),
          ("u1770", 1771),
          ("u1771", 1772),
          ("u1772", 1773),
          ("u1773", 1774),
          ("u1774", 1775),
          ("u1775", 1776),
          ("u1776", 1777),
          ("u1777", 1778),
          ("u1778", 1779),
          ("u1779", 1780),
          ("u178", 179),
          ("u1780", 1781),
          ("u1781", 1782),
          ("u1782", 1783),
          ("u1783", 1784),
          ("u1784", 1785),
          ("u1785", 1786),
          ("u1786", 1787),
          ("u1787", 1788),
          ("u1788", 1789),
          ("u1789", 1790),
          ("u179", 180),
          ("u1790", 1791),
          ("u1791", 1792),
          ("u1792", 1793),
          ("u1793", 1794),
          ("u1794", 1795),
          ("u1795", 1796),
          ("u1796", 1797),
          ("u1797", 1798),
          ("u1798", 1799),
          ("u1799", 1800),
          ("u18", 19),
          ("u180", 181),
          ("u1800", 1801),
          ("u1801", 1802),
          ("u1802", 1803),
          ("u1803", 1804),
          ("u1804", 1805),
          ("u1805", 1806),
          ("u1806", 1807),
          ("u1807", 1808),
          ("u1808", 1809),
          ("u1809", 1810),
          ("u181", 182),
          ("u1810", 1811),
          ("u1811", 1812),
          ("u1812", 1813),
          ("u1813", 1814),
          ("u1814", 1815),
          ("u1815", 1816),
          ("u1816", 1817),
          ("u1817", 1818),
          ("u1818", 1819),
          ("u1819", 1820),
          ("u182", 183),
          ("u1820", 1821),
          ("u1821", 1822),
          ("u1822", 1823),
          ("u1823", 1824),
          ("u1824", 1825),
          ("u1825", 1826),
          ("u1826", 1827),
          ("u1827", 1828),
          ("u1828", 1829),
          ("u1829", 1830),
          ("u183", 184),
          ("u1830", 1831),
          ("u1831", 1832),
          ("u1832", 1833),
          ("u1833", 1834),
          ("u1834", 1835),
          ("u1835", 1836),
          ("u1836", 1837),
          ("u1837", 1838),
          ("u1838", 1839),
          ("u1839", 1840),
          ("u184", 185),
          ("u1840", 1841),
          ("u1841", 1842),
          ("u1842", 1843),
          ("u1843", 1844),
          ("u1844", 1845),
          ("u1845", 1846),
          ("u1846", 1847),
          ("u1847", 1848),
          ("u1848", 1849),
          ("u1849", 1850),
          ("u185", 186),
          ("u1850", 1851),
          ("u1851", 1852),
          ("u1852", 1853),
          ("u1853", 1854),
          ("u1854", 1855),
          ("u1855", 1856),
          ("u1856", 1857),
          ("u1857", 1858),
          ("u1858", 1859),
          ("u1859", 1860),
          ("u186", 187),
          ("u1860", 1861),
          ("u1861", 1862),
          ("u1862", 1863),
          ("u1863", 1864),
          ("u1864", 1865),
          ("u1865", 1866),
          ("u1866", 1867),
          ("u1867", 1868),
          ("u1868", 1869),
          ("u1869", 1870),
          ("u187", 188),
          ("u1870", 1871),
          ("u1871", 1872),
          ("u1872", 1873),
          ("u1873", 1874),
          ("u1874", 1875),
          ("u1875", 1876),
          ("u1876", 1877),
          ("u1877", 1878),
          ("u1878", 1879),
          ("u1879", 1880),
          ("u188", 189),
          ("u1880", 1881),
          ("u1881", 1882),
          ("u1882", 1883),
          ("u1883", 1884),
          ("u1884", 1885),
          ("u1885", 1886),
          ("u1886", 1887),
          ("u1887", 1888),
          ("u1888", 1889),
          ("u1889", 1890),
          ("u189", 190),
          ("u1890", 1891),
          ("u1891", 1892),
          ("u1892", 1893),
          ("u1893", 1894),
          ("u1894", 1895),
          ("u1895", 1896),
          ("u1896", 1897),
          ("u1897", 1898),
          ("u1898", 1899),
          ("u1899", 1900),
          ("u19", 20),
          ("u190", 191),
          ("u1900", 1901),
          ("u1901", 1902),
          ("u1902", 1903),
          ("u1903", 1904),
          ("u1904", 1905),
          ("u1905", 1906),
          ("u1906", 1907),
          ("u1907", 1908),
          ("u1908", 1909),
          ("u1909", 1910),
          ("u191", 192),
          ("u1910", 1911),
          ("u1911", 1912),
          ("u1912", 1913),
          ("u1913", 1914),
          ("u1914", 1915),
          ("u1915", 1916),
          ("u1916", 1917),
          ("u1917", 1918),
          ("u1918", 1919),
          ("u1919", 1920),
          ("u192", 193),
          ("u1920", 1921),
          ("u1921", 1922),
          ("u1922", 1923),
          ("u1923", 1924),
          ("u1924", 1925),
          ("u1925", 1926),
          ("u1926", 1927),
          ("u1927", 1928),
          ("u1928", 1929),
          ("u1929", 1930),
          ("u193", 194),
          ("u1930", 1931),
          ("u1931", 1932),
          ("u1932", 1933),
          ("u1933", 1934),
          ("u1934", 1935),
          ("u1935", 1936),
          ("u1936", 1937),
          ("u1937", 1938),
          ("u1938", 1939),
          ("u1939", 1940),
          ("u194", 195),
          ("u1940", 1941),
          ("u1941", 1942),
          ("u1942", 1943),
          ("u1943", 1944),
          ("u1944", 1945),
          ("u1945", 1946),
          ("u1946", 1947),
          ("u1947", 1948),
          ("u1948", 1949),
          ("u1949", 1950),
          ("u195", 196),
          ("u1950", 1951),
          ("u1951", 1952),
          ("u1952", 1953),
          ("u1953", 1954),
          ("u1954", 1955),
          ("u1955", 1956),
          ("u1956", 1957),
          ("u1957", 1958),
          ("u1958", 1959),
          ("u1959", 1960),
          ("u196", 197),
          ("u1960", 1961),
          ("u1961", 1962),
          ("u1962", 1963),
          ("u1963", 1964),
          ("u1964", 1965),
          ("u1965", 1966),
          ("u1966", 1967),
          ("u1967", 1968),
          ("u1968", 1969),
          ("u1969", 1970),
          ("u197", 198),
          ("u1970", 1971),
          ("u1971", 1972),
          ("u1972", 1973),
          ("u1973", 1974),
          ("u1974", 1975),
          ("u1975", 1976),
          ("u1976", 1977),
          ("u1977", 1978),
          ("u1978", 1979),
          ("u1979", 1980),
          ("u198", 199),
          ("u1980", 1981),
          ("u1981", 1982),
          ("u1982", 1983),
          ("u1983", 1984),
          ("u1984", 1985),
          ("u1985", 1986),
          ("u1986", 1987),
          ("u1987", 1988),
          ("u1988", 1989),
          ("u1989", 1990),
          ("u199", 200),
          ("u1990", 1991),
          ("u1991", 1992),
          ("u1992", 1993),
          ("u1993", 1994),
          ("u1994", 1995),
          ("u1995", 1996),
          ("u1996", 1997),
          ("u1997", 1998),
          ("u1998", 1999),
          ("u1999", 2000),
          ("u2", 3),
          ("u20", 21),
          ("u200", 201),
          ("u201", 202),
          ("u202", 203),
          ("u203", 204),
          ("u204", 205),
          ("u205", 206),
          ("u206", 207),
          ("u207", 208),
          ("u208", 209),
          ("u209", 210),
          ("u21", 22),
          ("u210", 211),
          ("u211", 212),
          ("u212", 213),
          ("u213", 214),
          ("u214", 215),
          ("u215", 216),
          ("u216", 217),
          ("u217", 218),
          ("u218", 219),
          ("u219", 220),
          ("u22", 23),
          ("u220", 221),
          ("u221", 222),
          ("u222", 223),
          ("u223", 224),
          ("u224", 225),
          ("u225", 226),
          ("u226", 227),
          ("u227", 228),
          ("u228", 229),
          ("u229", 230),
          ("u23", 24),
          ("u230", 231),
          ("u231", 232),
          ("u232", 233),
          ("u233", 234),
          ("u234", 235),
          ("u235", 236),
          ("u236", 237),
          ("u237", 238),
          ("u238", 239),
          ("u239", 240),
          ("u24", 25),
          ("u240", 241),
          ("u241", 242),
          ("u242", 243),
          ("u243", 244),
          ("u244", 245),
          ("u245", 246),
          ("u246", 247),
          ("u247", 248),
          ("u248", 249),
          ("u249", 250),
          ("u25", 26),
          ("u250", 251),
          ("u251", 252),
          ("u252", 253),
          ("u253", 254),
          ("u254", 255),
          ("u255", 256),
          ("u256", 257),
          ("u257", 258),
          ("u258", 259),
          ("u259", 260),
          ("u26", 27),
          ("u260", 261),
          ("u261", 262),
          ("u262", 263),
          ("u263", 264),
          ("u264", 265),
          ("u265", 266),
          ("u266", 267),
          ("u267", 268),
          ("u268", 269),
          ("u269", 270),
          ("u27", 28),
          ("u270", 271),
          ("u271", 272),
          ("u272", 273),
          ("u273", 274),
          ("u274", 275),
          ("u275", 276),
          ("u276", 277),
          ("u277", 278),
          ("u278", 279),
          ("u279", 280),
          ("u28", 29),
          ("u280", 281),
          ("u281", 282),
          ("u282", 283),
          ("u283", 284),
          ("u284", 285),
          ("u285", 286),
          ("u286", 287),
          ("u287", 288),
          ("u288", 289),
          ("u289", 290),
          ("u29", 30),
          ("u290", 291),
          ("u291", 292),
          ("u292", 293),
          ("u293", 294),
          ("u294", 295),
          ("u295", 296),
          ("u296", 297),
          ("u297", 298),
          ("u298", 299),
          ("u299", 300),
          ("u3", 4),
          ("u30", 31),
          ("u300", 301),
          ("u301", 302),
          ("u302", 303),
          ("u303", 304),
          ("u304", 305),
          ("u305", 306),
          ("u306", 307),
          ("u307", 308),
          ("u308", 309),
          ("u309", 310),
          ("u31", 32),
          ("u310", 311),
          ("u311", 312),
          ("u312", 313),
          ("u313", 314),
          ("u314", 315),
          ("u315", 316),
          ("u316", 317),
          ("u317", 318),
          ("u318", 319),
          ("u319", 320),
          ("u32", 33),
          ("u320", 321),
          ("u321", 322),
          ("u322", 323),
          ("u323", 324),
          ("u324", 325),
          ("u325", 326),
          ("u326", 327),
          ("u327", 328),
          ("u328", 329),
          ("u329", 330),
          ("u33", 34),
          ("u330", 331),
          ("u331", 332),
          ("u332", 333),
          ("u333", 334),
          ("u334", 335),
          ("u335", 336),
          ("u336", 337),
          ("u337", 338),
          ("u338", 339),
          ("u339", 340),
          ("u34", 35),
          ("u340", 341),
          ("u341", 342),
          ("u342", 343),
          ("u343", 344),
          ("u344", 345),
          ("u345", 346),
          ("u346", 347),
          ("u347", 348),
          ("u348", 349),
          ("u349", 350),
          ("u35", 36),
          ("u350", 351),
          ("u351", 352),
          ("u352", 353),
          ("u353", 354),
          ("u354", 355),
          ("u355", 356),
          ("u356", 357),
          ("u357", 358),
          ("u358", 359),
          ("u359", 360),
          ("u36", 37),
          ("u360", 361),
          ("u361", 362),
          ("u362", 363),
          ("u363", 364),
          ("u364", 365),
          ("u365", 366),
          ("u366", 367),
          ("u367", 368),
          ("u368", 369),
          ("u369", 370),
          ("u37", 38),
          ("u370", 371),
          ("u371", 372),
          ("u372", 373),
          ("u373", 374),
          ("u374", 375),
          ("u375", 376),
          ("u376", 377),
          ("u377", 378),
          ("u378", 379),
          ("u379", 380),
          ("u38", 39),
          ("u380", 381),
          ("u381", 382),
          ("u382", 383),
          ("u383", 384),
          ("u384", 385),
          ("u385", 386),
          ("u386", 387),
          ("u387", 388),
          ("u388", 389),
          ("u389", 390),
          ("u39", 40),
          ("u390", 391),
          ("u391", 392),
          ("u392", 393),
          ("u393", 394),
          ("u394", 395),
          ("u395", 396),
          ("u396", 397),
          ("u397", 398),
          ("u398", 399),
          ("u399", 400),
          ("u4", 5),
          ("u40", 41),
          ("u400", 401),
          ("u401", 402),
          ("u402", 403),
          ("u403", 404),
          ("u404", 405),
          ("u405", 406),
          ("u406", 407),
          ("u407", 408),
          ("u408", 409),
          ("u409", 410),
          ("u41", 42),
          ("u410", 411),
          ("u411", 412),
          ("u412", 413),
          ("u413", 414),
          ("u414", 415),
          ("u415", 416),
          ("u416", 417),
          ("u417", 418),
          ("u418", 419),
          ("u419", 420),
          ("u42", 43),
          ("u420", 421),
          ("u421", 422),
          ("u422", 423),
          ("u423", 424),
          ("u424", 425),
          ("u425", 426),
          ("u426", 427),
          ("u427", 428),
          ("u428", 429),
          ("u429", 430),
          ("u43", 44),
          ("u430", 431),
          ("u431", 432),
          ("u432", 433),
          ("u433", 434),
          ("u434", 435),
          ("u435", 436),
          ("u436", 437),
          ("u437", 438),
          ("u438", 439),
          ("u439", 440),
          ("u44", 45),
          ("u440", 441),
          ("u441", 442),
          ("u442", 443),
          ("u443", 444),
          ("u444", 445),
          ("u445", 446),
          ("u446", 447),
          ("u447", 448),
          ("u448", 449),
          ("u449", 450),
          ("u45", 46),
          ("u450", 451),
          ("u451", 452),
          ("u452", 453),
          ("u453", 454),
          ("u454", 455),
          ("u455", 456),
          ("u456", 457),
          ("u457", 458),
          ("u458", 459),
          ("u459", 460),
          ("u46", 47),
          ("u460", 461),
          ("u461", 462),
          ("u462", 463),
          ("u463", 464),
          ("u464", 465),
          ("u465", 466),
          ("u466", 467),
          ("u467", 468),
          ("u468", 469),
          ("u469", 470),
          ("u47", 48),
          ("u470", 471),
          ("u471", 472),
          ("u472", 473),
          ("u473", 474),
          ("u474", 475),
          ("u475", 476),
          ("u476", 477),
          ("u477", 478),
          ("u478", 479),
          ("u479", 480),
          ("u48", 49),
          ("u480", 481),
          ("u481", 482),
          ("u482", 483),
          ("u483", 484),
          ("u484", 485),
          ("u485", 486),
          ("u486", 487),
          ("u487", 488),
          ("u488", 489),
          ("u489", 490),
          ("u49", 50),
          ("u490", 491),
          ("u491", 492),
          ("u492", 493),
          ("u493", 494),
          ("u494", 495),
          ("u495", 496),
          ("u496", 497),
          ("u497", 498),
          ("u498", 499),
          ("u499", 500),
          ("u5", 6),
          ("u50", 51),
          ("u500", 501),
          ("u501", 502),
          ("u502", 503),
          ("u503", 504),
          ("u504", 505),
          ("u505", 506),
          ("u506", 507),
          ("u507", 508),
          ("u508", 509),
          ("u509", 510),
          ("u51", 52),
          ("u510", 511),
          ("u511", 512),
          ("u512", 513),
          ("u513", 514),
          ("u514", 515),
          ("u515", 516),
          ("u516", 517),
          ("u517", 518),
          ("u518", 519),
          ("u519", 520),
          ("u52", 53),
          ("u520", 521),
          ("u521", 522),
          ("u522", 523),
          ("u523", 524),
          ("u524", 525),
          ("u525", 526),
          ("u526", 527),
          ("u527", 528),
          ("u528", 529),
          ("u529", 530),
          ("u53", 54),
          ("u530", 531),
          ("u531", 532),
          ("u532", 533),
          ("u533", 534),
          ("u534", 535),
          ("u535", 536),
          ("u536", 537),
          ("u537", 538),
          ("u538", 539),
          ("u539", 540),
          ("u54", 55),
          ("u540", 541),
          ("u541", 542),
          ("u542", 543),
          ("u543", 544),
          ("u544", 545),
          ("u545", 546),
          ("u546", 547),
          ("u547", 548),
          ("u548", 549),
          ("u549", 550),
          ("u55", 56),
          ("u550", 551),
          ("u551", 552),
          ("u552", 553),
          ("u553", 554),
          ("u554", 555),
          ("u555", 556),
          ("u556", 557),
          ("u557", 558),
          ("u558", 559),
          ("u559", 560),
          ("u56", 57),
          ("u560", 561),
          ("u561", 562),
          ("u562", 563),
          ("u563", 564),
          ("u564", 565),
          ("u565", 566),
          ("u566", 567),
          ("u567", 568),
          ("u568", 569),
          ("u569", 570),
          ("u57", 58),
          ("u570", 571),
          ("u571", 572),
          ("u572", 573),
          ("u573", 574),
          ("u574", 575),
          ("u575", 576),
          ("u576", 577),
          ("u577", 578),
          ("u578", 579),
          ("u579", 580),
          ("u58", 59),
          ("u580", 581),
          ("u581", 582),
          ("u582", 583),
          ("u583", 584),
          ("u584", 585),
          ("u585", 586),
          ("u586", 587),
          ("u587", 588),
          ("u588", 589),
          ("u589", 590),
          ("u59", 60),
          ("u590", 591),
          ("u591", 592),
          ("u592", 593),
          ("u593", 594),
          ("u594", 595),
          ("u595", 596),
          ("u596", 597),
          ("u597", 598),
          ("u598", 599),
          ("u599", 600),
          ("u6", 7),
          ("u60", 61),
          ("u600", 601),
          ("u601", 602),
          ("u602", 603),
          ("u603", 604),
          ("u604", 605),
          ("u605", 606),
          ("u606", 607),
          ("u607", 608),
          ("u608", 609),
          ("u609", 610),
          ("u61", 62),
          ("u610", 611),
          ("u611", 612),
          ("u612", 613),
          ("u613", 614),
          ("u614", 615),
          ("u615", 616),
          ("u616", 617),
          ("u617", 618),
          ("u618", 619),
          ("u619", 620),
          ("u62", 63),
          ("u620", 621),
          ("u621", 622),
          ("u622", 623),
          ("u623", 624),
          ("u624", 625),
          ("u625", 626),
          ("u626", 627),
          ("u627", 628),
          ("u628", 629),
          ("u629", 630),
          ("u63", 64),
          ("u630", 631),
          ("u631", 632),
          ("u632", 633),
          ("u633", 634),
          ("u634", 635),
          ("u635", 636),
          ("u636", 637),
          ("u637", 638),
          ("u638", 639),
          ("u639", 640),
          ("u64", 65),
          ("u640", 641),
          ("u641", 642),
          ("u642", 643),
          ("u643", 644),
          ("u644", 645),
          ("u645", 646),
          ("u646", 647),
          ("u647", 648),
          ("u648", 649),
          ("u649", 650),
          ("u65", 66),
          ("u650", 651),
          ("u651", 652),
          ("u652", 653),
          ("u653", 654),
          ("u654", 655),
          ("u655", 656),
          ("u656", 657),
          ("u657", 658),
          ("u658", 659),
          ("u659", 660),
          ("u66", 67),
          ("u660", 661),
          ("u661", 662),
          ("u662", 663),
          ("u663", 664),
          ("u664", 665),
          ("u665", 666),
          ("u666", 667),
          ("u667", 668),
          ("u668", 669),
          ("u669", 670),
          ("u67", 68),
          ("u670", 671),
          ("u671", 672),
          ("u672", 673),
          ("u673", 674),
          ("u674", 675),
          ("u675", 676),
          ("u676", 677),
          ("u677", 678),
          ("u678", 679),
          ("u679", 680),
          ("u68", 69),
          ("u680", 681),
          ("u681", 682),
          ("u682", 683),
          ("u683", 684),
          ("u684", 685),
          ("u685", 686),
          ("u686", 687),
          ("u687", 688),
          ("u688", 689),
          ("u689", 690),
          ("u69", 70),
          ("u690", 691),
          ("u691", 692),
          ("u692", 693),
          ("u693", 694),
          ("u694", 695),
          ("u695", 696),
          ("u696", 697),
          ("u697", 698),
          ("u698", 699),
          ("u699", 700),
          ("u7", 8),
          ("u70", 71),
          ("u700", 701),
          ("u701", 702),
          ("u702", 703),
          ("u703", 704),
          ("u704", 705),
          ("u705", 706),
          ("u706", 707),
          ("u707", 708),
          ("u708", 709),
          ("u709", 710),
          ("u71", 72),
          ("u710", 711),
          ("u711", 712),
          ("u712", 713),
          ("u713", 714),
          ("u714", 715),
          ("u715", 716),
          ("u716", 717),
          ("u717", 718),
          ("u718", 719),
          ("u719", 720),
          ("u72", 73),
          ("u720", 721),
          ("u721", 722),
          ("u722", 723),
          ("u723", 724),
          ("u724", 725),
          ("u725", 726),
          ("u726", 727),
          ("u727", 728),
          ("u728", 729),
          ("u729", 730),
          ("u73", 74),
          ("u730", 731),
          ("u731", 732),
          ("u732", 733),
          ("u733", 734),
          ("u734", 735),
          ("u735", 736),
          ("u736", 737),
          ("u737", 738),
          ("u738", 739),
          ("u739", 740),
          ("u74", 75),
          ("u740", 741),
          ("u741", 742),
          ("u742", 743),
          ("u743", 744),
          ("u744", 745),
          ("u745", 746),
          ("u746", 747),
          ("u747", 748),
          ("u748", 749),
          ("u749", 750),
          ("u75", 76),
          ("u750", 751),
          ("u751", 752),
          ("u752", 753),
          ("u753", 754),
          ("u754", 755),
          ("u755", 756),
          ("u756", 757),
          ("u757", 758),
          ("u758", 759),
          ("u759", 760),
          ("u76", 77),
          ("u760", 761),
          ("u761", 762),
          ("u762", 763),
          ("u763", 764),
          ("u764", 765),
          ("u765", 766),
          ("u766", 767),
          ("u767", 768),
          ("u768", 769),
          ("u769", 770),
          ("u77", 78),
          ("u770", 771),
          ("u771", 772),
          ("u772", 773),
          ("u773", 774),
          ("u774", 775),
          ("u775", 776),
          ("u776", 777),
          ("u777", 778),
          ("u778", 779),
          ("u779", 780),
          ("u78", 79),
          ("u780", 781),
          ("u781", 782),
          ("u782", 783),
          ("u783", 784),
          ("u784", 785),
          ("u785", 786),
          ("u786", 787),
          ("u787", 788),
          ("u788", 789),
          ("u789", 790),
          ("u79", 80),
          ("u790", 791),
          ("u791", 792),
          ("u792", 793),
          ("u793", 794),
          ("u794", 795),
          ("u795", 796),
          ("u796", 797),
          ("u797", 798),
          ("u798", 799),
          ("u799", 800),
          ("u8", 9),
          ("u80", 81),
          ("u800", 801),
          ("u801", 802),
          ("u802", 803),
          ("u803", 804),
          ("u804", 805),
          ("u805", 806),
          ("u806", 807),
          ("u807", 808),
          ("u808", 809),
          ("u809", 810),
          ("u81", 82),
          ("u810", 811),
          ("u811", 812),
          ("u812", 813),
          ("u813", 814),
          ("u814", 815),
          ("u815", 816),
          ("u816", 817),
          ("u817", 818),
          ("u818", 819),
          ("u819", 820),
          ("u82", 83),
          ("u820", 821),
          ("u821", 822),
          ("u822", 823),
          ("u823", 824),
          ("u824", 825),
          ("u825", 826),
          ("u826", 827),
          ("u827", 828),
          ("u828", 829),
          ("u829", 830),
          ("u83", 84),
          ("u830", 831),
          ("u831", 832),
          ("u832", 833),
          ("u833", 834),
          ("u834", 835),
          ("u835", 836),
          ("u836", 837),
          ("u837", 838),
          ("u838", 839),
          ("u839", 840),
          ("u84", 85),
          ("u840", 841),
          ("u841", 842),
          ("u842", 843),
          ("u843", 844),
          ("u844", 845),
          ("u845", 846),
          ("u846", 847),
          ("u847", 848),
          ("u848", 849),
          ("u849", 850),
          ("u85", 86),
          ("u850", 851),
          ("u851", 852),
          ("u852", 853),
          ("u853", 854),
          ("u854", 855),
          ("u855", 856),
          ("u856", 857),
          ("u857", 858),
          ("u858", 859),
          ("u859", 860),
          ("u86", 87),
          ("u860", 861),
          ("u861", 862),
          ("u862", 863),
          ("u863", 864),
          ("u864", 865),
          ("u865", 866),
          ("u866", 867),
          ("u867", 868),
          ("u868", 869),
          ("u869", 870),
          ("u87", 88),
          ("u870", 871),
          ("u871", 872),
          ("u872", 873),
          ("u873", 874),
          ("u874", 875),
          ("u875", 876),
          ("u876", 877),
          ("u877", 878),
          ("u878", 879),
          ("u879", 880),
          ("u88", 89),
          ("u880", 881),
          ("u881", 882),
          ("u882", 883),
          ("u883", 884),
          ("u884", 885),
          ("u885", 886),
          ("u886", 887),
          ("u887", 888),
          ("u888", 889),
          ("u889", 890),
          ("u89", 90),
          ("u890", 891),
          ("u891", 892),
          ("u892", 893),
          ("u893", 894),
          ("u894", 895),
          ("u895", 896),
          ("u896", 897),
          ("u897", 898),
          ("u898", 899),
          ("u899", 900),
          ("u9", 10),
          ("u90", 91),
          ("u900", 901),
          ("u901", 902),
          ("u902", 903),
          ("u903", 904),
          ("u904", 905),
          ("u905", 906),
          ("u906", 907),
          ("u907", 908),
          ("u908", 909),
          ("u909", 910),
          ("u91", 92),
          ("u910", 911),
          ("u911", 912),
          ("u912", 913),
          ("u913", 914),
          ("u914", 915),
          ("u915", 916),
          ("u916", 917),
          ("u917", 918),
          ("u918", 919),
          ("u919", 920),
          ("u92", 93),
          ("u920", 921),
          ("u921", 922),
          ("u922", 923),
          ("u923", 924),
          ("u924", 925),
          ("u925", 926),
          ("u926", 927),
          ("u927", 928),
          ("u928", 929),
          ("u929", 930),
          ("u93", 94),
          ("u930", 931),
          ("u931", 932),
          ("u932", 933),
          ("u933", 934),
          ("u934", 935),
          ("u935", 936),
          ("u936", 937),
          ("u937", 938),
          ("u938", 939),
          ("u939", 940),
          ("u94", 95),
          ("u940", 941),
          ("u941", 942),
          ("u942", 943),
          ("u943", 944),
          ("u944", 945),
          ("u945", 946),
          ("u946", 947),
          ("u947", 948),
          ("u948", 949),
          ("u949", 950),
          ("u95", 96),
          ("u950", 951),
          ("u951", 952),
          ("u952", 953),
          ("u953", 954),
          ("u954", 955),
          ("u955", 956),
          ("u956", 957),
          ("u957", 958),
          ("u958", 959),
          ("u959", 960),
          ("u96", 97),
          ("u960", 961),
          ("u961", 962),
          ("u962", 963),
          ("u963", 964),
          ("u964", 965),
          ("u965", 966),
          ("u966", 967),
          ("u967", 968),
          ("u968", 969),
          ("u969", 970),
          ("u97", 98),
          ("u970", 971),
          ("u971", 972),
          ("u972", 973),
          ("u973", 974),
          ("u974", 975),
          ("u975", 976),
          ("u976", 977),
          ("u977", 978),
          ("u978", 979),
          ("u979", 980),
          ("u98", 99),
          ("u980", 981),
          ("u981", 982),
          ("u982", 983),
          ("u983", 984),
          ("u984", 985),
          ("u985", 986),
          ("u986", 987),
          ("u987", 988),
          ("u988", 989),
          ("u989", 990),
          ("u99", 100),
          ("u990", 991),
          ("u991", 992),
          ("u992", 993),
          ("u993", 994),
          ("u994", 995),
          ("u995", 996),
          ("u996", 997),
          ("u997", 998),
          ("u998", 999),
          ("u999", 1000))
    )


_OutputIndex_Type.__name__ = "Integer32"
_OutputIndex_Object = MibTableColumn
outputIndex = _OutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 1),
    _OutputIndex_Type()
)
outputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outputIndex.setStatus("current")


class _OutputName_Type(DisplayString):
    """Custom type outputName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_OutputName_Type.__name__ = "DisplayString"
_OutputName_Object = MibTableColumn
outputName = _OutputName_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 2),
    _OutputName_Type()
)
outputName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputName.setStatus("current")


class _OutputGroup_Type(Integer32):
    """Custom type outputGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_OutputGroup_Type.__name__ = "Integer32"
_OutputGroup_Object = MibTableColumn
outputGroup = _OutputGroup_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 3),
    _OutputGroup_Type()
)
outputGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputGroup.setStatus("current")


class _OutputStatus_Type(Bits):
    """Custom type outputStatus based on Bits"""
    namedValues = NamedValues(
        *(("outputAdjusting", 15),
          ("outputConstantVoltage", 16),
          ("outputCurrentBoundsExceeded", 18),
          ("outputCurrentLimited", 10),
          ("outputEmergencyOff", 14),
          ("outputEnableKill", 13),
          ("outputFailureCurrentLimit", 19),
          ("outputFailureMaxCurrent", 5),
          ("outputFailureMaxPower", 7),
          ("outputFailureMaxSenseVoltage", 3),
          ("outputFailureMaxTemperature", 6),
          ("outputFailureMaxTerminalVoltage", 4),
          ("outputFailureMinSenseVoltage", 2),
          ("outputFailureTimeout", 9),
          ("outputInhibit", 1),
          ("outputLowCurrentRange", 17),
          ("outputOn", 0),
          ("outputRampDown", 12),
          ("outputRampUp", 11))
    )

_OutputStatus_Type.__name__ = "Bits"
_OutputStatus_Object = MibTableColumn
outputStatus = _OutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 4),
    _OutputStatus_Type()
)
outputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputStatus.setStatus("current")
_OutputMeasurementSenseVoltage_Type = Float
_OutputMeasurementSenseVoltage_Object = MibTableColumn
outputMeasurementSenseVoltage = _OutputMeasurementSenseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 5),
    _OutputMeasurementSenseVoltage_Type()
)
outputMeasurementSenseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputMeasurementSenseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outputMeasurementSenseVoltage.setUnits("V")
_OutputMeasurementTerminalVoltage_Type = Float
_OutputMeasurementTerminalVoltage_Object = MibTableColumn
outputMeasurementTerminalVoltage = _OutputMeasurementTerminalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 6),
    _OutputMeasurementTerminalVoltage_Type()
)
outputMeasurementTerminalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputMeasurementTerminalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outputMeasurementTerminalVoltage.setUnits("V")
_OutputMeasurementCurrent_Type = Float
_OutputMeasurementCurrent_Object = MibTableColumn
outputMeasurementCurrent = _OutputMeasurementCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 7),
    _OutputMeasurementCurrent_Type()
)
outputMeasurementCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputMeasurementCurrent.setStatus("current")
if mibBuilder.loadTexts:
    outputMeasurementCurrent.setUnits("A")


class _OutputMeasurementTemperature_Type(Integer32):
    """Custom type outputMeasurementTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-128,
              127)
        )
    )
    namedValues = NamedValues(
        *(("failure", 127),
          ("ok", -128))
    )


_OutputMeasurementTemperature_Type.__name__ = "Integer32"
_OutputMeasurementTemperature_Object = MibTableColumn
outputMeasurementTemperature = _OutputMeasurementTemperature_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 8),
    _OutputMeasurementTemperature_Type()
)
outputMeasurementTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputMeasurementTemperature.setStatus("current")
if mibBuilder.loadTexts:
    outputMeasurementTemperature.setUnits("deg.C")


class _OutputSwitch_Type(Integer32):
    """Custom type outputSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("clearEvents", 10),
          ("off", 0),
          ("on", 1),
          ("resetEmergencyOff", 2),
          ("setEmergencyOff", 3),
          ("setRippleMeasurementOn", 22),
          ("setVoltageMeasurementOn", 21),
          ("setVoltageRippleMeasurementOff", 20),
          ("setVoltageRippleMeasurementOn", 23))
    )


_OutputSwitch_Type.__name__ = "Integer32"
_OutputSwitch_Object = MibTableColumn
outputSwitch = _OutputSwitch_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 9),
    _OutputSwitch_Type()
)
outputSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputSwitch.setStatus("current")
_OutputVoltage_Type = Float
_OutputVoltage_Object = MibTableColumn
outputVoltage = _OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 10),
    _OutputVoltage_Type()
)
outputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outputVoltage.setUnits("V")


class _OutputAdjustVoltage_Type(Integer32):
    """Custom type outputAdjustVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_OutputAdjustVoltage_Type.__name__ = "Integer32"
_OutputAdjustVoltage_Object = MibTableColumn
outputAdjustVoltage = _OutputAdjustVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 11),
    _OutputAdjustVoltage_Type()
)
outputAdjustVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputAdjustVoltage.setStatus("obsolete")
_OutputCurrent_Type = Float
_OutputCurrent_Object = MibTableColumn
outputCurrent = _OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 12),
    _OutputCurrent_Type()
)
outputCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    outputCurrent.setUnits("A")
_OutputVoltageRiseRate_Type = Float
_OutputVoltageRiseRate_Object = MibTableColumn
outputVoltageRiseRate = _OutputVoltageRiseRate_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 13),
    _OutputVoltageRiseRate_Type()
)
outputVoltageRiseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputVoltageRiseRate.setStatus("current")
if mibBuilder.loadTexts:
    outputVoltageRiseRate.setUnits("V/s")
_OutputVoltageFallRate_Type = Float
_OutputVoltageFallRate_Object = MibTableColumn
outputVoltageFallRate = _OutputVoltageFallRate_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 14),
    _OutputVoltageFallRate_Type()
)
outputVoltageFallRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputVoltageFallRate.setStatus("current")
if mibBuilder.loadTexts:
    outputVoltageFallRate.setUnits("V/s")


class _OutputSupervisionBehavior_Type(Integer32):
    """Custom type outputSupervisionBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OutputSupervisionBehavior_Type.__name__ = "Integer32"
_OutputSupervisionBehavior_Object = MibTableColumn
outputSupervisionBehavior = _OutputSupervisionBehavior_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 15),
    _OutputSupervisionBehavior_Type()
)
outputSupervisionBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputSupervisionBehavior.setStatus("current")
_OutputSupervisionMinSenseVoltage_Type = Float
_OutputSupervisionMinSenseVoltage_Object = MibTableColumn
outputSupervisionMinSenseVoltage = _OutputSupervisionMinSenseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 16),
    _OutputSupervisionMinSenseVoltage_Type()
)
outputSupervisionMinSenseVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputSupervisionMinSenseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outputSupervisionMinSenseVoltage.setUnits("V")
_OutputSupervisionMaxSenseVoltage_Type = Float
_OutputSupervisionMaxSenseVoltage_Object = MibTableColumn
outputSupervisionMaxSenseVoltage = _OutputSupervisionMaxSenseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 17),
    _OutputSupervisionMaxSenseVoltage_Type()
)
outputSupervisionMaxSenseVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputSupervisionMaxSenseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outputSupervisionMaxSenseVoltage.setUnits("V")
_OutputSupervisionMaxTerminalVoltage_Type = Float
_OutputSupervisionMaxTerminalVoltage_Object = MibTableColumn
outputSupervisionMaxTerminalVoltage = _OutputSupervisionMaxTerminalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 18),
    _OutputSupervisionMaxTerminalVoltage_Type()
)
outputSupervisionMaxTerminalVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputSupervisionMaxTerminalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outputSupervisionMaxTerminalVoltage.setUnits("V")
_OutputSupervisionMaxCurrent_Type = Float
_OutputSupervisionMaxCurrent_Object = MibTableColumn
outputSupervisionMaxCurrent = _OutputSupervisionMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 19),
    _OutputSupervisionMaxCurrent_Type()
)
outputSupervisionMaxCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputSupervisionMaxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    outputSupervisionMaxCurrent.setUnits("A")
_OutputSupervisionMaxTemperature_Type = Integer32
_OutputSupervisionMaxTemperature_Object = MibTableColumn
outputSupervisionMaxTemperature = _OutputSupervisionMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 20),
    _OutputSupervisionMaxTemperature_Type()
)
outputSupervisionMaxTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputSupervisionMaxTemperature.setStatus("current")
if mibBuilder.loadTexts:
    outputSupervisionMaxTemperature.setUnits("deg.C")
_OutputConfigMaxSenseVoltage_Type = Float
_OutputConfigMaxSenseVoltage_Object = MibTableColumn
outputConfigMaxSenseVoltage = _OutputConfigMaxSenseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 21),
    _OutputConfigMaxSenseVoltage_Type()
)
outputConfigMaxSenseVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfigMaxSenseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outputConfigMaxSenseVoltage.setUnits("V")
_OutputConfigMaxTerminalVoltage_Type = Float
_OutputConfigMaxTerminalVoltage_Object = MibTableColumn
outputConfigMaxTerminalVoltage = _OutputConfigMaxTerminalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 22),
    _OutputConfigMaxTerminalVoltage_Type()
)
outputConfigMaxTerminalVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfigMaxTerminalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outputConfigMaxTerminalVoltage.setUnits("V")
_OutputConfigMaxCurrent_Type = Float
_OutputConfigMaxCurrent_Object = MibTableColumn
outputConfigMaxCurrent = _OutputConfigMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 23),
    _OutputConfigMaxCurrent_Type()
)
outputConfigMaxCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfigMaxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    outputConfigMaxCurrent.setUnits("A")
_OutputSupervisionMaxPower_Type = Float
_OutputSupervisionMaxPower_Object = MibTableColumn
outputSupervisionMaxPower = _OutputSupervisionMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 24),
    _OutputSupervisionMaxPower_Type()
)
outputSupervisionMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputSupervisionMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    outputSupervisionMaxPower.setUnits("W")
_OutputCurrentRiseRate_Type = Float
_OutputCurrentRiseRate_Object = MibTableColumn
outputCurrentRiseRate = _OutputCurrentRiseRate_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 25),
    _OutputCurrentRiseRate_Type()
)
outputCurrentRiseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputCurrentRiseRate.setStatus("current")
if mibBuilder.loadTexts:
    outputCurrentRiseRate.setUnits("A/s")
_OutputCurrentFallRate_Type = Float
_OutputCurrentFallRate_Object = MibTableColumn
outputCurrentFallRate = _OutputCurrentFallRate_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 26),
    _OutputCurrentFallRate_Type()
)
outputCurrentFallRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputCurrentFallRate.setStatus("current")
if mibBuilder.loadTexts:
    outputCurrentFallRate.setUnits("A/s")
_OutputTripTimeMaxCurrent_Type = OutputTripTime
_OutputTripTimeMaxCurrent_Object = MibTableColumn
outputTripTimeMaxCurrent = _OutputTripTimeMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 27),
    _OutputTripTimeMaxCurrent_Type()
)
outputTripTimeMaxCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripTimeMaxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    outputTripTimeMaxCurrent.setUnits("ms")
_OutputHardwareLimitVoltage_Type = Float
_OutputHardwareLimitVoltage_Object = MibTableColumn
outputHardwareLimitVoltage = _OutputHardwareLimitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 28),
    _OutputHardwareLimitVoltage_Type()
)
outputHardwareLimitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputHardwareLimitVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outputHardwareLimitVoltage.setUnits("V")
_OutputHardwareLimitCurrent_Type = Float
_OutputHardwareLimitCurrent_Object = MibTableColumn
outputHardwareLimitCurrent = _OutputHardwareLimitCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 29),
    _OutputHardwareLimitCurrent_Type()
)
outputHardwareLimitCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputHardwareLimitCurrent.setStatus("current")
if mibBuilder.loadTexts:
    outputHardwareLimitCurrent.setUnits("A")
_OutputConfigGainSenseVoltage_Type = Float
_OutputConfigGainSenseVoltage_Object = MibTableColumn
outputConfigGainSenseVoltage = _OutputConfigGainSenseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 30),
    _OutputConfigGainSenseVoltage_Type()
)
outputConfigGainSenseVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfigGainSenseVoltage.setStatus("current")
_OutputConfigOffsetSenseVoltage_Type = Float
_OutputConfigOffsetSenseVoltage_Object = MibTableColumn
outputConfigOffsetSenseVoltage = _OutputConfigOffsetSenseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 31),
    _OutputConfigOffsetSenseVoltage_Type()
)
outputConfigOffsetSenseVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfigOffsetSenseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outputConfigOffsetSenseVoltage.setUnits("V")
_OutputConfigGainTerminalVoltage_Type = Float
_OutputConfigGainTerminalVoltage_Object = MibTableColumn
outputConfigGainTerminalVoltage = _OutputConfigGainTerminalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 32),
    _OutputConfigGainTerminalVoltage_Type()
)
outputConfigGainTerminalVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfigGainTerminalVoltage.setStatus("current")
_OutputConfigOffsetTerminalVoltage_Type = Float
_OutputConfigOffsetTerminalVoltage_Object = MibTableColumn
outputConfigOffsetTerminalVoltage = _OutputConfigOffsetTerminalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 33),
    _OutputConfigOffsetTerminalVoltage_Type()
)
outputConfigOffsetTerminalVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfigOffsetTerminalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outputConfigOffsetTerminalVoltage.setUnits("V")
_OutputConfigGainCurrent_Type = Float
_OutputConfigGainCurrent_Object = MibTableColumn
outputConfigGainCurrent = _OutputConfigGainCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 34),
    _OutputConfigGainCurrent_Type()
)
outputConfigGainCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfigGainCurrent.setStatus("current")
_OutputConfigOffsetCurrent_Type = Float
_OutputConfigOffsetCurrent_Object = MibTableColumn
outputConfigOffsetCurrent = _OutputConfigOffsetCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 35),
    _OutputConfigOffsetCurrent_Type()
)
outputConfigOffsetCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfigOffsetCurrent.setStatus("current")
if mibBuilder.loadTexts:
    outputConfigOffsetCurrent.setUnits("V")


class _OutputUserConfig_Type(Integer32):
    """Custom type outputUserConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_OutputUserConfig_Type.__name__ = "Integer32"
_OutputUserConfig_Object = MibTableColumn
outputUserConfig = _OutputUserConfig_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 37),
    _OutputUserConfig_Type()
)
outputUserConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputUserConfig.setStatus("current")


class _OutputRegulationMode_Type(Integer32):
    """Custom type outputRegulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 0),
          ("moderate", 1),
          ("slow", 2))
    )


_OutputRegulationMode_Type.__name__ = "Integer32"
_OutputRegulationMode_Object = MibTableColumn
outputRegulationMode = _OutputRegulationMode_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 38),
    _OutputRegulationMode_Type()
)
outputRegulationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputRegulationMode.setStatus("current")
_OutputConfigMaxTemperature_Type = Integer32
_OutputConfigMaxTemperature_Object = MibTableColumn
outputConfigMaxTemperature = _OutputConfigMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 39),
    _OutputConfigMaxTemperature_Type()
)
outputConfigMaxTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfigMaxTemperature.setStatus("current")
if mibBuilder.loadTexts:
    outputConfigMaxTemperature.setUnits("deg.C")
_OutputResistance_Type = Float
_OutputResistance_Object = MibTableColumn
outputResistance = _OutputResistance_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 40),
    _OutputResistance_Type()
)
outputResistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputResistance.setStatus("current")
if mibBuilder.loadTexts:
    outputResistance.setUnits("Ohm")
_OutputTripTimeMinSenseVoltage_Type = OutputTripTime
_OutputTripTimeMinSenseVoltage_Object = MibTableColumn
outputTripTimeMinSenseVoltage = _OutputTripTimeMinSenseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 41),
    _OutputTripTimeMinSenseVoltage_Type()
)
outputTripTimeMinSenseVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripTimeMinSenseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outputTripTimeMinSenseVoltage.setUnits("ms")
_OutputTripTimeMaxSenseVoltage_Type = OutputTripTime
_OutputTripTimeMaxSenseVoltage_Object = MibTableColumn
outputTripTimeMaxSenseVoltage = _OutputTripTimeMaxSenseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 42),
    _OutputTripTimeMaxSenseVoltage_Type()
)
outputTripTimeMaxSenseVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripTimeMaxSenseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outputTripTimeMaxSenseVoltage.setUnits("ms")
_OutputTripTimeMaxTerminalVoltage_Type = OutputTripTime
_OutputTripTimeMaxTerminalVoltage_Object = MibTableColumn
outputTripTimeMaxTerminalVoltage = _OutputTripTimeMaxTerminalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 43),
    _OutputTripTimeMaxTerminalVoltage_Type()
)
outputTripTimeMaxTerminalVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripTimeMaxTerminalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outputTripTimeMaxTerminalVoltage.setUnits("ms")
_OutputTripTimeMaxTemperature_Type = OutputTripTime
_OutputTripTimeMaxTemperature_Object = MibTableColumn
outputTripTimeMaxTemperature = _OutputTripTimeMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 44),
    _OutputTripTimeMaxTemperature_Type()
)
outputTripTimeMaxTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripTimeMaxTemperature.setStatus("current")
if mibBuilder.loadTexts:
    outputTripTimeMaxTemperature.setUnits("ms")
_OutputTripTimeMaxPower_Type = OutputTripTime
_OutputTripTimeMaxPower_Object = MibTableColumn
outputTripTimeMaxPower = _OutputTripTimeMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 45),
    _OutputTripTimeMaxPower_Type()
)
outputTripTimeMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripTimeMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    outputTripTimeMaxPower.setUnits("ms")
_OutputTripTimeTimeout_Type = OutputTripTime
_OutputTripTimeTimeout_Object = MibTableColumn
outputTripTimeTimeout = _OutputTripTimeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 46),
    _OutputTripTimeTimeout_Type()
)
outputTripTimeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripTimeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    outputTripTimeTimeout.setUnits("ms")
_OutputTripActionMinSenseVoltage_Type = OutputTripAction
_OutputTripActionMinSenseVoltage_Object = MibTableColumn
outputTripActionMinSenseVoltage = _OutputTripActionMinSenseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 47),
    _OutputTripActionMinSenseVoltage_Type()
)
outputTripActionMinSenseVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripActionMinSenseVoltage.setStatus("current")
_OutputTripActionMaxSenseVoltage_Type = OutputTripAction
_OutputTripActionMaxSenseVoltage_Object = MibTableColumn
outputTripActionMaxSenseVoltage = _OutputTripActionMaxSenseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 48),
    _OutputTripActionMaxSenseVoltage_Type()
)
outputTripActionMaxSenseVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripActionMaxSenseVoltage.setStatus("current")
_OutputTripActionMaxTerminalVoltage_Type = OutputTripAction
_OutputTripActionMaxTerminalVoltage_Object = MibTableColumn
outputTripActionMaxTerminalVoltage = _OutputTripActionMaxTerminalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 49),
    _OutputTripActionMaxTerminalVoltage_Type()
)
outputTripActionMaxTerminalVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripActionMaxTerminalVoltage.setStatus("current")
_OutputTripActionMaxCurrent_Type = OutputTripAction
_OutputTripActionMaxCurrent_Object = MibTableColumn
outputTripActionMaxCurrent = _OutputTripActionMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 50),
    _OutputTripActionMaxCurrent_Type()
)
outputTripActionMaxCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripActionMaxCurrent.setStatus("current")
_OutputTripActionMaxTemperature_Type = OutputTripAction
_OutputTripActionMaxTemperature_Object = MibTableColumn
outputTripActionMaxTemperature = _OutputTripActionMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 51),
    _OutputTripActionMaxTemperature_Type()
)
outputTripActionMaxTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripActionMaxTemperature.setStatus("current")
_OutputTripActionMaxPower_Type = OutputTripAction
_OutputTripActionMaxPower_Object = MibTableColumn
outputTripActionMaxPower = _OutputTripActionMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 52),
    _OutputTripActionMaxPower_Type()
)
outputTripActionMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripActionMaxPower.setStatus("current")
_OutputTripActionExternalInhibit_Type = OutputTripAction
_OutputTripActionExternalInhibit_Object = MibTableColumn
outputTripActionExternalInhibit = _OutputTripActionExternalInhibit_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 53),
    _OutputTripActionExternalInhibit_Type()
)
outputTripActionExternalInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripActionExternalInhibit.setStatus("current")
_OutputTripActionTimeout_Type = OutputTripAction
_OutputTripActionTimeout_Object = MibTableColumn
outputTripActionTimeout = _OutputTripActionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 54),
    _OutputTripActionTimeout_Type()
)
outputTripActionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputTripActionTimeout.setStatus("current")
_OutputConfigDataS_Type = OctetString
_OutputConfigDataS_Object = MibTableColumn
outputConfigDataS = _OutputConfigDataS_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 1024),
    _OutputConfigDataS_Type()
)
outputConfigDataS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfigDataS.setStatus("current")
_OutputConfigDataU_Type = OctetString
_OutputConfigDataU_Object = MibTableColumn
outputConfigDataU = _OutputConfigDataU_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 2, 1, 1025),
    _OutputConfigDataU_Type()
)
outputConfigDataU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfigDataU.setStatus("current")


class _GroupsNumber_Type(Integer32):
    """Custom type groupsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1999),
    )


_GroupsNumber_Type.__name__ = "Integer32"
_GroupsNumber_Object = MibScalar
groupsNumber = _GroupsNumber_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 3),
    _GroupsNumber_Type()
)
groupsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupsNumber.setStatus("current")
_GroupsTable_Object = MibTable
groupsTable = _GroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 4)
)
if mibBuilder.loadTexts:
    groupsTable.setStatus("current")
_GroupsEntry_Object = MibTableRow
groupsEntry = _GroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 4, 1)
)
groupsEntry.setIndexNames(
    (0, "WIENER-CRATE-MIB", "groupsIndex"),
)
if mibBuilder.loadTexts:
    groupsEntry.setStatus("current")


class _GroupsIndex_Type(Integer32):
    """Custom type groupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1999),
    )


_GroupsIndex_Type.__name__ = "Integer32"
_GroupsIndex_Object = MibTableColumn
groupsIndex = _GroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 4, 1, 1),
    _GroupsIndex_Type()
)
groupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    groupsIndex.setStatus("current")


class _GroupsSwitch_Type(Integer32):
    """Custom type groupsSwitch based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("clearEvents", 10),
          ("disableAdjust", 6),
          ("disableKill", 4),
          ("enableAdjust", 7),
          ("enableKill", 5),
          ("off", 0),
          ("on", 1),
          ("resetEmergencyOff", 2),
          ("setEmergencyOff", 3),
          ("undefined", -1))
    )


_GroupsSwitch_Type.__name__ = "Integer32"
_GroupsSwitch_Object = MibTableColumn
groupsSwitch = _GroupsSwitch_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 4, 1, 9),
    _GroupsSwitch_Type()
)
groupsSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupsSwitch.setStatus("current")


class _ModuleNumber_Type(Integer32):
    """Custom type moduleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ModuleNumber_Type.__name__ = "Integer32"
_ModuleNumber_Object = MibScalar
moduleNumber = _ModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 5),
    _ModuleNumber_Type()
)
moduleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNumber.setStatus("current")
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("current")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1)
)
moduleEntry.setIndexNames(
    (0, "WIENER-CRATE-MIB", "moduleIndex"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("current")


class _ModuleIndex_Type(Integer32):
    """Custom type moduleIndex based on Integer32"""
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
        *(("ma0", 1),
          ("ma1", 2),
          ("ma2", 3),
          ("ma3", 4),
          ("ma4", 5),
          ("ma5", 6),
          ("ma6", 7),
          ("ma7", 8),
          ("ma8", 9),
          ("ma9", 10))
    )


_ModuleIndex_Type.__name__ = "Integer32"
_ModuleIndex_Object = MibTableColumn
moduleIndex = _ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 1),
    _ModuleIndex_Type()
)
moduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    moduleIndex.setStatus("current")


class _ModuleDescription_Type(OctetString):
    """Custom type moduleDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_ModuleDescription_Type.__name__ = "OctetString"
_ModuleDescription_Object = MibTableColumn
moduleDescription = _ModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 2),
    _ModuleDescription_Type()
)
moduleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDescription.setStatus("current")
_ModuleAuxiliaryMeasurementVoltage_ObjectIdentity = ObjectIdentity
moduleAuxiliaryMeasurementVoltage = _ModuleAuxiliaryMeasurementVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    moduleAuxiliaryMeasurementVoltage.setStatus("current")
_ModuleAuxiliaryMeasurementVoltage0_Type = Float
_ModuleAuxiliaryMeasurementVoltage0_Object = MibScalar
moduleAuxiliaryMeasurementVoltage0 = _ModuleAuxiliaryMeasurementVoltage0_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 3, 1),
    _ModuleAuxiliaryMeasurementVoltage0_Type()
)
moduleAuxiliaryMeasurementVoltage0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAuxiliaryMeasurementVoltage0.setStatus("current")
if mibBuilder.loadTexts:
    moduleAuxiliaryMeasurementVoltage0.setUnits("V")
_ModuleAuxiliaryMeasurementVoltage1_Type = Float
_ModuleAuxiliaryMeasurementVoltage1_Object = MibScalar
moduleAuxiliaryMeasurementVoltage1 = _ModuleAuxiliaryMeasurementVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 3, 2),
    _ModuleAuxiliaryMeasurementVoltage1_Type()
)
moduleAuxiliaryMeasurementVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAuxiliaryMeasurementVoltage1.setStatus("current")
if mibBuilder.loadTexts:
    moduleAuxiliaryMeasurementVoltage1.setUnits("V")
_ModuleHardwareLimitVoltage_Type = Float
_ModuleHardwareLimitVoltage_Object = MibTableColumn
moduleHardwareLimitVoltage = _ModuleHardwareLimitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 4),
    _ModuleHardwareLimitVoltage_Type()
)
moduleHardwareLimitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHardwareLimitVoltage.setStatus("current")
if mibBuilder.loadTexts:
    moduleHardwareLimitVoltage.setUnits("%")
_ModuleHardwareLimitCurrent_Type = Float
_ModuleHardwareLimitCurrent_Object = MibTableColumn
moduleHardwareLimitCurrent = _ModuleHardwareLimitCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 5),
    _ModuleHardwareLimitCurrent_Type()
)
moduleHardwareLimitCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHardwareLimitCurrent.setStatus("current")
if mibBuilder.loadTexts:
    moduleHardwareLimitCurrent.setUnits("%")
_ModuleRampSpeedVoltage_Type = Float
_ModuleRampSpeedVoltage_Object = MibTableColumn
moduleRampSpeedVoltage = _ModuleRampSpeedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 6),
    _ModuleRampSpeedVoltage_Type()
)
moduleRampSpeedVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleRampSpeedVoltage.setStatus("current")
if mibBuilder.loadTexts:
    moduleRampSpeedVoltage.setUnits("%")
_ModuleRampSpeedCurrent_Type = Float
_ModuleRampSpeedCurrent_Object = MibTableColumn
moduleRampSpeedCurrent = _ModuleRampSpeedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 7),
    _ModuleRampSpeedCurrent_Type()
)
moduleRampSpeedCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleRampSpeedCurrent.setStatus("current")
if mibBuilder.loadTexts:
    moduleRampSpeedCurrent.setUnits("%")


class _ModuleStatus_Type(Bits):
    """Custom type moduleStatus based on Bits"""
    namedValues = NamedValues(
        *(("moduleHardwareLimitVoltageIsGood", 5),
          ("moduleIsEventActive", 11),
          ("moduleIsFineAdjustment", 0),
          ("moduleIsGood", 12),
          ("moduleIsHighVoltageOn", 3),
          ("moduleIsInputError", 6),
          ("moduleIsKillEnable", 15),
          ("moduleIsLiveInsertion", 2),
          ("moduleIsNoRamp", 9),
          ("moduleIsNoSumError", 8),
          ("moduleNeedService", 4),
          ("moduleSafetyLoopIsGood", 10),
          ("moduleSupplyIsGood", 13),
          ("moduleTemperatureIsGood", 14))
    )

_ModuleStatus_Type.__name__ = "Bits"
_ModuleStatus_Object = MibTableColumn
moduleStatus = _ModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 8),
    _ModuleStatus_Type()
)
moduleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatus.setStatus("current")


class _ModuleEventStatus_Type(Bits):
    """Custom type moduleEventStatus based on Bits"""
    namedValues = NamedValues(
        *(("moduleEventInputError", 6),
          ("moduleEventLiveInsertion", 2),
          ("moduleEventPowerFail", 0),
          ("moduleEventSafetyLoopNotGood", 10),
          ("moduleEventService", 4),
          ("moduleEventSupplyNotGood", 13),
          ("moduleEventTemperatureNotGood", 14),
          ("moduleHardwareLimitVoltageNotGood", 5))
    )

_ModuleEventStatus_Type.__name__ = "Bits"
_ModuleEventStatus_Object = MibTableColumn
moduleEventStatus = _ModuleEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 9),
    _ModuleEventStatus_Type()
)
moduleEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEventStatus.setStatus("current")


class _ModuleEventChannelStatus_Type(Bits):
    """Custom type moduleEventChannelStatus based on Bits"""
    namedValues = NamedValues(
        *(("channel0", 0),
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
          ("channel33", 33),
          ("channel34", 34),
          ("channel35", 35),
          ("channel36", 36),
          ("channel37", 37),
          ("channel38", 38),
          ("channel39", 39),
          ("channel4", 4),
          ("channel40", 40),
          ("channel41", 41),
          ("channel42", 42),
          ("channel43", 43),
          ("channel44", 44),
          ("channel45", 45),
          ("channel46", 46),
          ("channel47", 47),
          ("channel5", 5),
          ("channel6", 6),
          ("channel7", 7),
          ("channel8", 8),
          ("channel9", 9))
    )

_ModuleEventChannelStatus_Type.__name__ = "Bits"
_ModuleEventChannelStatus_Object = MibTableColumn
moduleEventChannelStatus = _ModuleEventChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 10),
    _ModuleEventChannelStatus_Type()
)
moduleEventChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEventChannelStatus.setStatus("current")


class _ModuleDoClear_Type(Integer32):
    """Custom type moduleDoClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doClear", 1),
          ("nothing", 0))
    )


_ModuleDoClear_Type.__name__ = "Integer32"
_ModuleDoClear_Object = MibTableColumn
moduleDoClear = _ModuleDoClear_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 11),
    _ModuleDoClear_Type()
)
moduleDoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleDoClear.setStatus("current")
_ModuleAuxiliaryMeasurementTemperature_ObjectIdentity = ObjectIdentity
moduleAuxiliaryMeasurementTemperature = _ModuleAuxiliaryMeasurementTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 12)
)
if mibBuilder.loadTexts:
    moduleAuxiliaryMeasurementTemperature.setStatus("current")
_ModuleAuxiliaryMeasurementTemperature0_Type = Float
_ModuleAuxiliaryMeasurementTemperature0_Object = MibScalar
moduleAuxiliaryMeasurementTemperature0 = _ModuleAuxiliaryMeasurementTemperature0_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 12, 1),
    _ModuleAuxiliaryMeasurementTemperature0_Type()
)
moduleAuxiliaryMeasurementTemperature0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAuxiliaryMeasurementTemperature0.setStatus("current")
if mibBuilder.loadTexts:
    moduleAuxiliaryMeasurementTemperature0.setUnits("deg.C")
_ModuleAuxiliaryMeasurementTemperature1_Type = Float
_ModuleAuxiliaryMeasurementTemperature1_Object = MibScalar
moduleAuxiliaryMeasurementTemperature1 = _ModuleAuxiliaryMeasurementTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 12, 2),
    _ModuleAuxiliaryMeasurementTemperature1_Type()
)
moduleAuxiliaryMeasurementTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAuxiliaryMeasurementTemperature1.setStatus("current")
if mibBuilder.loadTexts:
    moduleAuxiliaryMeasurementTemperature1.setUnits("deg.C")
_ModuleAuxiliaryMeasurementTemperature2_Type = Float
_ModuleAuxiliaryMeasurementTemperature2_Object = MibScalar
moduleAuxiliaryMeasurementTemperature2 = _ModuleAuxiliaryMeasurementTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 12, 3),
    _ModuleAuxiliaryMeasurementTemperature2_Type()
)
moduleAuxiliaryMeasurementTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAuxiliaryMeasurementTemperature2.setStatus("current")
if mibBuilder.loadTexts:
    moduleAuxiliaryMeasurementTemperature2.setUnits("deg.C")
_ModuleAuxiliaryMeasurementTemperature3_Type = Float
_ModuleAuxiliaryMeasurementTemperature3_Object = MibScalar
moduleAuxiliaryMeasurementTemperature3 = _ModuleAuxiliaryMeasurementTemperature3_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 12, 4),
    _ModuleAuxiliaryMeasurementTemperature3_Type()
)
moduleAuxiliaryMeasurementTemperature3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAuxiliaryMeasurementTemperature3.setStatus("current")
if mibBuilder.loadTexts:
    moduleAuxiliaryMeasurementTemperature3.setUnits("deg.C")
_ModuleConfigDataS_Type = OctetString
_ModuleConfigDataS_Object = MibTableColumn
moduleConfigDataS = _ModuleConfigDataS_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 1024),
    _ModuleConfigDataS_Type()
)
moduleConfigDataS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleConfigDataS.setStatus("current")
_ModuleConfigDataU_Type = OctetString
_ModuleConfigDataU_Object = MibTableColumn
moduleConfigDataU = _ModuleConfigDataU_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 3, 6, 1, 1025),
    _ModuleConfigDataU_Type()
)
moduleConfigDataU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleConfigDataU.setStatus("current")
_Sensor_ObjectIdentity = ObjectIdentity
sensor = _Sensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19947, 1, 4)
)
if mibBuilder.loadTexts:
    sensor.setStatus("current")


class _SensorNumber_Type(Integer32):
    """Custom type sensorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SensorNumber_Type.__name__ = "Integer32"
_SensorNumber_Object = MibScalar
sensorNumber = _SensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 4, 1),
    _SensorNumber_Type()
)
sensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorNumber.setStatus("current")
_SensorTable_Object = MibTable
sensorTable = _SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sensorTable.setStatus("current")
_SensorEntry_Object = MibTableRow
sensorEntry = _SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 4, 2, 1)
)
sensorEntry.setIndexNames(
    (0, "WIENER-CRATE-MIB", "sensorIndex"),
)
if mibBuilder.loadTexts:
    sensorEntry.setStatus("current")


class _SensorIndex_Type(Integer32):
    """Custom type sensorIndex based on Integer32"""
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
        *(("temp1", 1),
          ("temp2", 2),
          ("temp3", 3),
          ("temp4", 4),
          ("temp5", 5),
          ("temp6", 6),
          ("temp7", 7),
          ("temp8", 8))
    )


_SensorIndex_Type.__name__ = "Integer32"
_SensorIndex_Object = MibTableColumn
sensorIndex = _SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 4, 2, 1, 1),
    _SensorIndex_Type()
)
sensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorIndex.setStatus("current")


class _SensorTemperature_Type(Integer32):
    """Custom type sensorTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_SensorTemperature_Type.__name__ = "Integer32"
_SensorTemperature_Object = MibTableColumn
sensorTemperature = _SensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 4, 2, 1, 2),
    _SensorTemperature_Type()
)
sensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTemperature.setStatus("current")
if mibBuilder.loadTexts:
    sensorTemperature.setUnits("deg.C")


class _SensorWarningThreshold_Type(Integer32):
    """Custom type sensorWarningThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SensorWarningThreshold_Type.__name__ = "Integer32"
_SensorWarningThreshold_Object = MibTableColumn
sensorWarningThreshold = _SensorWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 4, 2, 1, 3),
    _SensorWarningThreshold_Type()
)
sensorWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    sensorWarningThreshold.setUnits("deg.C")


class _SensorFailureThreshold_Type(Integer32):
    """Custom type sensorFailureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SensorFailureThreshold_Type.__name__ = "Integer32"
_SensorFailureThreshold_Object = MibTableColumn
sensorFailureThreshold = _SensorFailureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 4, 2, 1, 4),
    _SensorFailureThreshold_Type()
)
sensorFailureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorFailureThreshold.setStatus("current")
if mibBuilder.loadTexts:
    sensorFailureThreshold.setUnits("deg.C")


class _SensorAlarmThreshold_Type(Integer32):
    """Custom type sensorAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SensorAlarmThreshold_Type.__name__ = "Integer32"
_SensorAlarmThreshold_Object = MibTableColumn
sensorAlarmThreshold = _SensorAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 4, 2, 1, 6),
    _SensorAlarmThreshold_Type()
)
sensorAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    sensorAlarmThreshold.setUnits("deg.C")


class _SensorName_Type(DisplayString):
    """Custom type sensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_SensorName_Type.__name__ = "DisplayString"
_SensorName_Object = MibTableColumn
sensorName = _SensorName_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 4, 2, 1, 7),
    _SensorName_Type()
)
sensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorName.setStatus("current")


class _SensorID_Type(OctetString):
    """Custom type sensorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SensorID_Type.__name__ = "OctetString"
_SensorID_Object = MibTableColumn
sensorID = _SensorID_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 4, 2, 1, 8),
    _SensorID_Type()
)
sensorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorID.setStatus("current")
_SensorStatus_Type = Integer32
_SensorStatus_Object = MibTableColumn
sensorStatus = _SensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 4, 2, 1, 9),
    _SensorStatus_Type()
)
sensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorStatus.setStatus("current")
_Communication_ObjectIdentity = ObjectIdentity
communication = _Communication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5)
)
if mibBuilder.loadTexts:
    communication.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 1)
)
if mibBuilder.loadTexts:
    snmp.setStatus("current")
_SnmpCommunityTable_Object = MibTable
snmpCommunityTable = _SnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    snmpCommunityTable.setStatus("current")
_SnmpCommunityEntry_Object = MibTableRow
snmpCommunityEntry = _SnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 1, 1, 1)
)
snmpCommunityEntry.setIndexNames(
    (0, "WIENER-CRATE-MIB", "snmpAccessRight"),
)
if mibBuilder.loadTexts:
    snmpCommunityEntry.setStatus("current")


class _SnmpAccessRight_Type(Integer32):
    """Custom type snmpAccessRight based on Integer32"""
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
        *(("admin", 3),
          ("guru", 4),
          ("private", 2),
          ("public", 1))
    )


_SnmpAccessRight_Type.__name__ = "Integer32"
_SnmpAccessRight_Object = MibTableColumn
snmpAccessRight = _SnmpAccessRight_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 1, 1, 1, 1),
    _SnmpAccessRight_Type()
)
snmpAccessRight.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpAccessRight.setStatus("current")


class _SnmpCommunityName_Type(OctetString):
    """Custom type snmpCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_SnmpCommunityName_Type.__name__ = "OctetString"
_SnmpCommunityName_Object = MibTableColumn
snmpCommunityName = _SnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 1, 1, 1, 2),
    _SnmpCommunityName_Type()
)
snmpCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityName.setStatus("current")
_SnmpPort_Type = Integer32
_SnmpPort_Object = MibTableColumn
snmpPort = _SnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 1, 2),
    _SnmpPort_Type()
)
snmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPort.setStatus("current")
_HttpPort_Type = Integer32
_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 1, 3),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPort.setStatus("current")


class _FirmwareUpdate_Type(OctetString):
    """Custom type firmwareUpdate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_FirmwareUpdate_Type.__name__ = "OctetString"
_FirmwareUpdate_Object = MibScalar
firmwareUpdate = _FirmwareUpdate_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 1, 10),
    _FirmwareUpdate_Type()
)
firmwareUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdate.setStatus("current")
_IpDynamicAddress_Type = IpAddress
_IpDynamicAddress_Object = MibTableColumn
ipDynamicAddress = _IpDynamicAddress_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 1, 11),
    _IpDynamicAddress_Type()
)
ipDynamicAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDynamicAddress.setStatus("current")
_IpStaticAddress_Type = IpAddress
_IpStaticAddress_Object = MibTableColumn
ipStaticAddress = _IpStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 1, 12),
    _IpStaticAddress_Type()
)
ipStaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticAddress.setStatus("current")
_MacAddress_Type = MacAddress
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 1, 13),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_Can_ObjectIdentity = ObjectIdentity
can = _Can_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 2)
)
if mibBuilder.loadTexts:
    can.setStatus("current")
_CanBitRate_Type = Integer32
_CanBitRate_Object = MibScalar
canBitRate = _CanBitRate_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 2, 1),
    _CanBitRate_Type()
)
canBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    canBitRate.setStatus("current")


class _CanReceive_Type(OctetString):
    """Custom type canReceive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_CanReceive_Type.__name__ = "OctetString"
_CanReceive_Object = MibScalar
canReceive = _CanReceive_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 2, 2),
    _CanReceive_Type()
)
canReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    canReceive.setStatus("current")


class _CanTransmit_Type(OctetString):
    """Custom type canTransmit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_CanTransmit_Type.__name__ = "OctetString"
_CanTransmit_Object = MibScalar
canTransmit = _CanTransmit_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 2, 3),
    _CanTransmit_Type()
)
canTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    canTransmit.setStatus("current")


class _CanReceiveHv_Type(OctetString):
    """Custom type canReceiveHv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_CanReceiveHv_Type.__name__ = "OctetString"
_CanReceiveHv_Object = MibScalar
canReceiveHv = _CanReceiveHv_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 2, 4),
    _CanReceiveHv_Type()
)
canReceiveHv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    canReceiveHv.setStatus("current")


class _CanTransmitHv_Type(OctetString):
    """Custom type canTransmitHv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_CanTransmitHv_Type.__name__ = "OctetString"
_CanTransmitHv_Object = MibScalar
canTransmitHv = _CanTransmitHv_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 2, 5),
    _CanTransmitHv_Type()
)
canTransmitHv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    canTransmitHv.setStatus("current")


class _CanBitRateHv_Type(Integer32):
    """Custom type canBitRateHv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(125000, 1000000),
    )


_CanBitRateHv_Type.__name__ = "Integer32"
_CanBitRateHv_Object = MibScalar
canBitRateHv = _CanBitRateHv_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 5, 2, 6),
    _CanBitRateHv_Type()
)
canBitRateHv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    canBitRateHv.setStatus("current")
_Powersupply_ObjectIdentity = ObjectIdentity
powersupply = _Powersupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19947, 1, 6)
)
if mibBuilder.loadTexts:
    powersupply.setStatus("current")
_PsSerialNumber_Type = DisplayString
_PsSerialNumber_Object = MibTableColumn
psSerialNumber = _PsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 6, 2),
    _PsSerialNumber_Type()
)
psSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSerialNumber.setStatus("current")
_PsOperatingTime_Type = Integer32
_PsOperatingTime_Object = MibTableColumn
psOperatingTime = _PsOperatingTime_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 6, 3),
    _PsOperatingTime_Type()
)
psOperatingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psOperatingTime.setStatus("current")
if mibBuilder.loadTexts:
    psOperatingTime.setUnits("s")


class _PsAuxiliaryNumber_Type(Integer32):
    """Custom type psAuxiliaryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PsAuxiliaryNumber_Type.__name__ = "Integer32"
_PsAuxiliaryNumber_Object = MibScalar
psAuxiliaryNumber = _PsAuxiliaryNumber_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 6, 4),
    _PsAuxiliaryNumber_Type()
)
psAuxiliaryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAuxiliaryNumber.setStatus("current")
_PsAuxiliaryTable_Object = MibTable
psAuxiliaryTable = _PsAuxiliaryTable_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 6, 5)
)
if mibBuilder.loadTexts:
    psAuxiliaryTable.setStatus("current")
_PsAuxiliaryEntry_Object = MibTableRow
psAuxiliaryEntry = _PsAuxiliaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 6, 5, 1)
)
psAuxiliaryEntry.setIndexNames(
    (0, "WIENER-CRATE-MIB", "psAuxiliaryIndex"),
)
if mibBuilder.loadTexts:
    psAuxiliaryEntry.setStatus("current")


class _PsAuxiliaryIndex_Type(Integer32):
    """Custom type psAuxiliaryIndex based on Integer32"""
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
        *(("u0", 1),
          ("u1", 2),
          ("u2", 3),
          ("u3", 4),
          ("u4", 5),
          ("u5", 6),
          ("u6", 7),
          ("u7", 8))
    )


_PsAuxiliaryIndex_Type.__name__ = "Integer32"
_PsAuxiliaryIndex_Object = MibTableColumn
psAuxiliaryIndex = _PsAuxiliaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 6, 5, 1, 1),
    _PsAuxiliaryIndex_Type()
)
psAuxiliaryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psAuxiliaryIndex.setStatus("current")
_PsAuxiliaryMeasurementVoltage_Type = Float
_PsAuxiliaryMeasurementVoltage_Object = MibTableColumn
psAuxiliaryMeasurementVoltage = _PsAuxiliaryMeasurementVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 6, 5, 1, 3),
    _PsAuxiliaryMeasurementVoltage_Type()
)
psAuxiliaryMeasurementVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAuxiliaryMeasurementVoltage.setStatus("current")
if mibBuilder.loadTexts:
    psAuxiliaryMeasurementVoltage.setUnits("V")
_PsAuxiliaryMeasurementCurrent_Type = Float
_PsAuxiliaryMeasurementCurrent_Object = MibTableColumn
psAuxiliaryMeasurementCurrent = _PsAuxiliaryMeasurementCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 6, 5, 1, 4),
    _PsAuxiliaryMeasurementCurrent_Type()
)
psAuxiliaryMeasurementCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAuxiliaryMeasurementCurrent.setStatus("current")
if mibBuilder.loadTexts:
    psAuxiliaryMeasurementCurrent.setUnits("A")


class _PsDirectAccess_Type(OctetString):
    """Custom type psDirectAccess based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_PsDirectAccess_Type.__name__ = "OctetString"
_PsDirectAccess_Object = MibTableColumn
psDirectAccess = _PsDirectAccess_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 6, 1024),
    _PsDirectAccess_Type()
)
psDirectAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psDirectAccess.setStatus("current")
_Fantray_ObjectIdentity = ObjectIdentity
fantray = _Fantray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7)
)
if mibBuilder.loadTexts:
    fantray.setStatus("current")


class _FanSerialNumber_Type(DisplayString):
    """Custom type fanSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_FanSerialNumber_Type.__name__ = "DisplayString"
_FanSerialNumber_Object = MibTableColumn
fanSerialNumber = _FanSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7, 2),
    _FanSerialNumber_Type()
)
fanSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanSerialNumber.setStatus("current")
_FanOperatingTime_Type = Integer32
_FanOperatingTime_Object = MibTableColumn
fanOperatingTime = _FanOperatingTime_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7, 3),
    _FanOperatingTime_Type()
)
fanOperatingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanOperatingTime.setStatus("current")
if mibBuilder.loadTexts:
    fanOperatingTime.setUnits("s")
_FanAirTemperature_Type = Integer32
_FanAirTemperature_Object = MibTableColumn
fanAirTemperature = _FanAirTemperature_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7, 4),
    _FanAirTemperature_Type()
)
fanAirTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAirTemperature.setStatus("current")
if mibBuilder.loadTexts:
    fanAirTemperature.setUnits("deg.C")


class _FanSwitchOffDelay_Type(Integer32):
    """Custom type fanSwitchOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_FanSwitchOffDelay_Type.__name__ = "Integer32"
_FanSwitchOffDelay_Object = MibTableColumn
fanSwitchOffDelay = _FanSwitchOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7, 5),
    _FanSwitchOffDelay_Type()
)
fanSwitchOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanSwitchOffDelay.setStatus("current")
if mibBuilder.loadTexts:
    fanSwitchOffDelay.setUnits("s")
_FanNominalSpeed_Type = Integer32
_FanNominalSpeed_Object = MibTableColumn
fanNominalSpeed = _FanNominalSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7, 6),
    _FanNominalSpeed_Type()
)
fanNominalSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanNominalSpeed.setStatus("current")
if mibBuilder.loadTexts:
    fanNominalSpeed.setUnits("RPM")


class _FanNumberOfFans_Type(Integer32):
    """Custom type fanNumberOfFans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_FanNumberOfFans_Type.__name__ = "Integer32"
_FanNumberOfFans_Object = MibTableColumn
fanNumberOfFans = _FanNumberOfFans_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7, 7),
    _FanNumberOfFans_Type()
)
fanNumberOfFans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanNumberOfFans.setStatus("current")
if mibBuilder.loadTexts:
    fanNumberOfFans.setUnits("Fans")
_FanSpeedTable_Object = MibTable
fanSpeedTable = _FanSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7, 8)
)
if mibBuilder.loadTexts:
    fanSpeedTable.setStatus("current")
_FanSpeedEntry_Object = MibTableRow
fanSpeedEntry = _FanSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7, 8, 1)
)
fanSpeedEntry.setIndexNames(
    (0, "WIENER-CRATE-MIB", "fanNumber"),
)
if mibBuilder.loadTexts:
    fanSpeedEntry.setStatus("current")


class _FanNumber_Type(Integer32):
    """Custom type fanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_FanNumber_Type.__name__ = "Integer32"
_FanNumber_Object = MibTableColumn
fanNumber = _FanNumber_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7, 8, 1, 1),
    _FanNumber_Type()
)
fanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanNumber.setStatus("current")
_FanSpeed_Type = Integer32
_FanSpeed_Object = MibTableColumn
fanSpeed = _FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7, 8, 1, 2),
    _FanSpeed_Type()
)
fanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    fanSpeed.setUnits("RPM")
_FanMaxSpeed_Type = Integer32
_FanMaxSpeed_Object = MibTableColumn
fanMaxSpeed = _FanMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7, 9),
    _FanMaxSpeed_Type()
)
fanMaxSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanMaxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    fanMaxSpeed.setUnits("RPM")
_FanMinSpeed_Type = Integer32
_FanMinSpeed_Object = MibTableColumn
fanMinSpeed = _FanMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7, 10),
    _FanMinSpeed_Type()
)
fanMinSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanMinSpeed.setStatus("current")
if mibBuilder.loadTexts:
    fanMinSpeed.setUnits("RPM")
_FanConfigMaxSpeed_Type = Integer32
_FanConfigMaxSpeed_Object = MibTableColumn
fanConfigMaxSpeed = _FanConfigMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7, 11),
    _FanConfigMaxSpeed_Type()
)
fanConfigMaxSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanConfigMaxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    fanConfigMaxSpeed.setUnits("RPM")
_FanConfigMinSpeed_Type = Integer32
_FanConfigMinSpeed_Object = MibTableColumn
fanConfigMinSpeed = _FanConfigMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 7, 12),
    _FanConfigMinSpeed_Type()
)
fanConfigMinSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanConfigMinSpeed.setStatus("current")
if mibBuilder.loadTexts:
    fanConfigMinSpeed.setUnits("RPM")
_Rack_ObjectIdentity = ObjectIdentity
rack = _Rack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19947, 1, 8)
)
if mibBuilder.loadTexts:
    rack.setStatus("current")
_Signal_ObjectIdentity = ObjectIdentity
signal = _Signal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19947, 1, 9)
)
if mibBuilder.loadTexts:
    signal.setStatus("current")


class _NumberOfAnalogInputs_Type(Integer32):
    """Custom type numberOfAnalogInputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_NumberOfAnalogInputs_Type.__name__ = "Integer32"
_NumberOfAnalogInputs_Object = MibTableColumn
numberOfAnalogInputs = _NumberOfAnalogInputs_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 9, 1),
    _NumberOfAnalogInputs_Type()
)
numberOfAnalogInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfAnalogInputs.setStatus("current")
_AnalogInputTable_Object = MibTable
analogInputTable = _AnalogInputTable_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 9, 2)
)
if mibBuilder.loadTexts:
    analogInputTable.setStatus("current")
_AnalogInputEntry_Object = MibTableRow
analogInputEntry = _AnalogInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 9, 2, 1)
)
analogInputEntry.setIndexNames(
    (0, "WIENER-CRATE-MIB", "analogInputIndex"),
)
if mibBuilder.loadTexts:
    analogInputEntry.setStatus("current")


class _AnalogInputIndex_Type(Integer32):
    """Custom type analogInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AnalogInputIndex_Type.__name__ = "Integer32"
_AnalogInputIndex_Object = MibTableColumn
analogInputIndex = _AnalogInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 9, 2, 1, 1),
    _AnalogInputIndex_Type()
)
analogInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    analogInputIndex.setStatus("current")
_AnalogMeasurementVoltage_Type = Float
_AnalogMeasurementVoltage_Object = MibTableColumn
analogMeasurementVoltage = _AnalogMeasurementVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 9, 2, 1, 2),
    _AnalogMeasurementVoltage_Type()
)
analogMeasurementVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogMeasurementVoltage.setStatus("current")
if mibBuilder.loadTexts:
    analogMeasurementVoltage.setUnits("V")
_AnalogMeasurementCurrent_Type = Float
_AnalogMeasurementCurrent_Object = MibTableColumn
analogMeasurementCurrent = _AnalogMeasurementCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 9, 2, 1, 3),
    _AnalogMeasurementCurrent_Type()
)
analogMeasurementCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogMeasurementCurrent.setStatus("current")
if mibBuilder.loadTexts:
    analogMeasurementCurrent.setUnits("A")


class _DigitalInput_Type(Bits):
    """Custom type digitalInput based on Bits"""
    namedValues = NamedValues(
        *(("d0", 0),
          ("d1", 1),
          ("d2", 2),
          ("d3", 3),
          ("d4", 4),
          ("d5", 5),
          ("d6", 6),
          ("d7", 7))
    )

_DigitalInput_Type.__name__ = "Bits"
_DigitalInput_Object = MibTableColumn
digitalInput = _DigitalInput_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 9, 5),
    _DigitalInput_Type()
)
digitalInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInput.setStatus("current")


class _DigitalOutput_Type(Bits):
    """Custom type digitalOutput based on Bits"""
    namedValues = NamedValues(
        *(("d0", 0),
          ("d1", 1),
          ("d2", 2),
          ("d3", 3),
          ("d4", 4),
          ("d5", 5),
          ("d6", 6),
          ("d7", 7))
    )

_DigitalOutput_Type.__name__ = "Bits"
_DigitalOutput_Object = MibTableColumn
digitalOutput = _DigitalOutput_Object(
    (1, 3, 6, 1, 4, 1, 19947, 1, 9, 6),
    _DigitalOutput_Type()
)
digitalOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalOutput.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WIENER-CRATE-MIB",
    **{"Float": Float,
       "OutputTripTime": OutputTripTime,
       "OutputTripAction": OutputTripAction,
       "wiener": wiener,
       "crate": crate,
       "system": system,
       "sysMainSwitch": sysMainSwitch,
       "sysStatus": sysStatus,
       "sysVmeSysReset": sysVmeSysReset,
       "sysHardwareReset": sysHardwareReset,
       "sysFactoryDefaults": sysFactoryDefaults,
       "sysConfigDoMeasurementCurrent": sysConfigDoMeasurementCurrent,
       "sysOperatingTime": sysOperatingTime,
       "sysDebugMemory8": sysDebugMemory8,
       "sysDebugMemory16": sysDebugMemory16,
       "sysDebugMemory32": sysDebugMemory32,
       "sysDebug": sysDebug,
       "sysDebugDisplay": sysDebugDisplay,
       "sysDebugBoot": sysDebugBoot,
       "input": input,
       "output": output,
       "outputNumber": outputNumber,
       "outputTable": outputTable,
       "outputEntry": outputEntry,
       "outputIndex": outputIndex,
       "outputName": outputName,
       "outputGroup": outputGroup,
       "outputStatus": outputStatus,
       "outputMeasurementSenseVoltage": outputMeasurementSenseVoltage,
       "outputMeasurementTerminalVoltage": outputMeasurementTerminalVoltage,
       "outputMeasurementCurrent": outputMeasurementCurrent,
       "outputMeasurementTemperature": outputMeasurementTemperature,
       "outputSwitch": outputSwitch,
       "outputVoltage": outputVoltage,
       "outputAdjustVoltage": outputAdjustVoltage,
       "outputCurrent": outputCurrent,
       "outputVoltageRiseRate": outputVoltageRiseRate,
       "outputVoltageFallRate": outputVoltageFallRate,
       "outputSupervisionBehavior": outputSupervisionBehavior,
       "outputSupervisionMinSenseVoltage": outputSupervisionMinSenseVoltage,
       "outputSupervisionMaxSenseVoltage": outputSupervisionMaxSenseVoltage,
       "outputSupervisionMaxTerminalVoltage": outputSupervisionMaxTerminalVoltage,
       "outputSupervisionMaxCurrent": outputSupervisionMaxCurrent,
       "outputSupervisionMaxTemperature": outputSupervisionMaxTemperature,
       "outputConfigMaxSenseVoltage": outputConfigMaxSenseVoltage,
       "outputConfigMaxTerminalVoltage": outputConfigMaxTerminalVoltage,
       "outputConfigMaxCurrent": outputConfigMaxCurrent,
       "outputSupervisionMaxPower": outputSupervisionMaxPower,
       "outputCurrentRiseRate": outputCurrentRiseRate,
       "outputCurrentFallRate": outputCurrentFallRate,
       "outputTripTimeMaxCurrent": outputTripTimeMaxCurrent,
       "outputHardwareLimitVoltage": outputHardwareLimitVoltage,
       "outputHardwareLimitCurrent": outputHardwareLimitCurrent,
       "outputConfigGainSenseVoltage": outputConfigGainSenseVoltage,
       "outputConfigOffsetSenseVoltage": outputConfigOffsetSenseVoltage,
       "outputConfigGainTerminalVoltage": outputConfigGainTerminalVoltage,
       "outputConfigOffsetTerminalVoltage": outputConfigOffsetTerminalVoltage,
       "outputConfigGainCurrent": outputConfigGainCurrent,
       "outputConfigOffsetCurrent": outputConfigOffsetCurrent,
       "outputUserConfig": outputUserConfig,
       "outputRegulationMode": outputRegulationMode,
       "outputConfigMaxTemperature": outputConfigMaxTemperature,
       "outputResistance": outputResistance,
       "outputTripTimeMinSenseVoltage": outputTripTimeMinSenseVoltage,
       "outputTripTimeMaxSenseVoltage": outputTripTimeMaxSenseVoltage,
       "outputTripTimeMaxTerminalVoltage": outputTripTimeMaxTerminalVoltage,
       "outputTripTimeMaxTemperature": outputTripTimeMaxTemperature,
       "outputTripTimeMaxPower": outputTripTimeMaxPower,
       "outputTripTimeTimeout": outputTripTimeTimeout,
       "outputTripActionMinSenseVoltage": outputTripActionMinSenseVoltage,
       "outputTripActionMaxSenseVoltage": outputTripActionMaxSenseVoltage,
       "outputTripActionMaxTerminalVoltage": outputTripActionMaxTerminalVoltage,
       "outputTripActionMaxCurrent": outputTripActionMaxCurrent,
       "outputTripActionMaxTemperature": outputTripActionMaxTemperature,
       "outputTripActionMaxPower": outputTripActionMaxPower,
       "outputTripActionExternalInhibit": outputTripActionExternalInhibit,
       "outputTripActionTimeout": outputTripActionTimeout,
       "outputConfigDataS": outputConfigDataS,
       "outputConfigDataU": outputConfigDataU,
       "groupsNumber": groupsNumber,
       "groupsTable": groupsTable,
       "groupsEntry": groupsEntry,
       "groupsIndex": groupsIndex,
       "groupsSwitch": groupsSwitch,
       "moduleNumber": moduleNumber,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleIndex": moduleIndex,
       "moduleDescription": moduleDescription,
       "moduleAuxiliaryMeasurementVoltage": moduleAuxiliaryMeasurementVoltage,
       "moduleAuxiliaryMeasurementVoltage0": moduleAuxiliaryMeasurementVoltage0,
       "moduleAuxiliaryMeasurementVoltage1": moduleAuxiliaryMeasurementVoltage1,
       "moduleHardwareLimitVoltage": moduleHardwareLimitVoltage,
       "moduleHardwareLimitCurrent": moduleHardwareLimitCurrent,
       "moduleRampSpeedVoltage": moduleRampSpeedVoltage,
       "moduleRampSpeedCurrent": moduleRampSpeedCurrent,
       "moduleStatus": moduleStatus,
       "moduleEventStatus": moduleEventStatus,
       "moduleEventChannelStatus": moduleEventChannelStatus,
       "moduleDoClear": moduleDoClear,
       "moduleAuxiliaryMeasurementTemperature": moduleAuxiliaryMeasurementTemperature,
       "moduleAuxiliaryMeasurementTemperature0": moduleAuxiliaryMeasurementTemperature0,
       "moduleAuxiliaryMeasurementTemperature1": moduleAuxiliaryMeasurementTemperature1,
       "moduleAuxiliaryMeasurementTemperature2": moduleAuxiliaryMeasurementTemperature2,
       "moduleAuxiliaryMeasurementTemperature3": moduleAuxiliaryMeasurementTemperature3,
       "moduleConfigDataS": moduleConfigDataS,
       "moduleConfigDataU": moduleConfigDataU,
       "sensor": sensor,
       "sensorNumber": sensorNumber,
       "sensorTable": sensorTable,
       "sensorEntry": sensorEntry,
       "sensorIndex": sensorIndex,
       "sensorTemperature": sensorTemperature,
       "sensorWarningThreshold": sensorWarningThreshold,
       "sensorFailureThreshold": sensorFailureThreshold,
       "sensorAlarmThreshold": sensorAlarmThreshold,
       "sensorName": sensorName,
       "sensorID": sensorID,
       "sensorStatus": sensorStatus,
       "communication": communication,
       "snmp": snmp,
       "snmpCommunityTable": snmpCommunityTable,
       "snmpCommunityEntry": snmpCommunityEntry,
       "snmpAccessRight": snmpAccessRight,
       "snmpCommunityName": snmpCommunityName,
       "snmpPort": snmpPort,
       "httpPort": httpPort,
       "firmwareUpdate": firmwareUpdate,
       "ipDynamicAddress": ipDynamicAddress,
       "ipStaticAddress": ipStaticAddress,
       "macAddress": macAddress,
       "can": can,
       "canBitRate": canBitRate,
       "canReceive": canReceive,
       "canTransmit": canTransmit,
       "canReceiveHv": canReceiveHv,
       "canTransmitHv": canTransmitHv,
       "canBitRateHv": canBitRateHv,
       "powersupply": powersupply,
       "psSerialNumber": psSerialNumber,
       "psOperatingTime": psOperatingTime,
       "psAuxiliaryNumber": psAuxiliaryNumber,
       "psAuxiliaryTable": psAuxiliaryTable,
       "psAuxiliaryEntry": psAuxiliaryEntry,
       "psAuxiliaryIndex": psAuxiliaryIndex,
       "psAuxiliaryMeasurementVoltage": psAuxiliaryMeasurementVoltage,
       "psAuxiliaryMeasurementCurrent": psAuxiliaryMeasurementCurrent,
       "psDirectAccess": psDirectAccess,
       "fantray": fantray,
       "fanSerialNumber": fanSerialNumber,
       "fanOperatingTime": fanOperatingTime,
       "fanAirTemperature": fanAirTemperature,
       "fanSwitchOffDelay": fanSwitchOffDelay,
       "fanNominalSpeed": fanNominalSpeed,
       "fanNumberOfFans": fanNumberOfFans,
       "fanSpeedTable": fanSpeedTable,
       "fanSpeedEntry": fanSpeedEntry,
       "fanNumber": fanNumber,
       "fanSpeed": fanSpeed,
       "fanMaxSpeed": fanMaxSpeed,
       "fanMinSpeed": fanMinSpeed,
       "fanConfigMaxSpeed": fanConfigMaxSpeed,
       "fanConfigMinSpeed": fanConfigMinSpeed,
       "rack": rack,
       "signal": signal,
       "numberOfAnalogInputs": numberOfAnalogInputs,
       "analogInputTable": analogInputTable,
       "analogInputEntry": analogInputEntry,
       "analogInputIndex": analogInputIndex,
       "analogMeasurementVoltage": analogMeasurementVoltage,
       "analogMeasurementCurrent": analogMeasurementCurrent,
       "digitalInput": digitalInput,
       "digitalOutput": digitalOutput}
)
