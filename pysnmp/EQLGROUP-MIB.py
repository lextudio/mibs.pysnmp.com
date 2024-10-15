# SNMP MIB module (EQLGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLGROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:55 2024
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

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eqlgroupModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 1)
)
eqlgroupModule.setRevisions(
        ("2002-09-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UTFString(OctetString, TextualConvention):
    status = "current"
    displayHint = "t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class AdminAccountPrivilegeType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("global-admin", 0),
          ("pool-admin", 1),
          ("pool-admin-group-read", 2),
          ("volume-admin", 3))
    )



class AdminAccountType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 2),
          ("read-write", 1))
    )



# MIB Managed Objects in the order of their OIDs

_EqlgroupObjects_ObjectIdentity = ObjectIdentity
eqlgroupObjects = _EqlgroupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1)
)
_EqlStorageGroupTable_Object = MibTable
eqlStorageGroupTable = _EqlStorageGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eqlStorageGroupTable.setStatus("current")
_EqlStorageGroupEntry_Object = MibTableRow
eqlStorageGroupEntry = _EqlStorageGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1)
)
eqlStorageGroupEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupEntry.setStatus("current")
_EqlGroupId_Type = Integer32
_EqlGroupId_Object = MibTableColumn
eqlGroupId = _EqlGroupId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 1),
    _EqlGroupId_Type()
)
eqlGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlGroupId.setStatus("current")


class _EqlGroupIsSingleSubnet_Type(Integer32):
    """Custom type eqlGroupIsSingleSubnet based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multi-subnet", 2),
          ("single-subnet", 1))
    )


_EqlGroupIsSingleSubnet_Type.__name__ = "Integer32"
_EqlGroupIsSingleSubnet_Object = MibTableColumn
eqlGroupIsSingleSubnet = _EqlGroupIsSingleSubnet_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 2),
    _EqlGroupIsSingleSubnet_Type()
)
eqlGroupIsSingleSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupIsSingleSubnet.setStatus("current")
_EqlGroupDefaultGatewayIpAddress_Type = Integer32
_EqlGroupDefaultGatewayIpAddress_Object = MibTableColumn
eqlGroupDefaultGatewayIpAddress = _EqlGroupDefaultGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 3),
    _EqlGroupDefaultGatewayIpAddress_Type()
)
eqlGroupDefaultGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultGatewayIpAddress.setStatus("deprecated")
_EqlGroupDefaultMask_Type = IpAddress
_EqlGroupDefaultMask_Object = MibTableColumn
eqlGroupDefaultMask = _EqlGroupDefaultMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 4),
    _EqlGroupDefaultMask_Type()
)
eqlGroupDefaultMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultMask.setStatus("current")


class _EqlGroupDefaultRoutingProtocol_Type(Integer32):
    """Custom type eqlGroupDefaultRoutingProtocol based on Integer32"""
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
        *(("none", 1),
          ("ospf", 3),
          ("rip", 2))
    )


_EqlGroupDefaultRoutingProtocol_Type.__name__ = "Integer32"
_EqlGroupDefaultRoutingProtocol_Object = MibTableColumn
eqlGroupDefaultRoutingProtocol = _EqlGroupDefaultRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 5),
    _EqlGroupDefaultRoutingProtocol_Type()
)
eqlGroupDefaultRoutingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultRoutingProtocol.setStatus("current")


class _EqlGroupIsStorageOptimization_Type(Integer32):
    """Custom type eqlGroupIsStorageOptimization based on Integer32"""
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
        *(("capacity", 1),
          ("performance", 2),
          ("raid5", 3))
    )


_EqlGroupIsStorageOptimization_Type.__name__ = "Integer32"
_EqlGroupIsStorageOptimization_Object = MibTableColumn
eqlGroupIsStorageOptimization = _EqlGroupIsStorageOptimization_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 6),
    _EqlGroupIsStorageOptimization_Type()
)
eqlGroupIsStorageOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupIsStorageOptimization.setStatus("current")


class _EqlGroupDiskAddWaitTime_Type(Integer32):
    """Custom type eqlGroupDiskAddWaitTime based on Integer32"""
    defaultValue = 2


_EqlGroupDiskAddWaitTime_Object = MibTableColumn
eqlGroupDiskAddWaitTime = _EqlGroupDiskAddWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 7),
    _EqlGroupDiskAddWaitTime_Type()
)
eqlGroupDiskAddWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDiskAddWaitTime.setStatus("current")
_EqlGroupDefaultLanguage_Type = Integer32
_EqlGroupDefaultLanguage_Object = MibTableColumn
eqlGroupDefaultLanguage = _EqlGroupDefaultLanguage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 8),
    _EqlGroupDefaultLanguage_Type()
)
eqlGroupDefaultLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultLanguage.setStatus("deprecated")


class _EqlGroupDefaultSnapshotSize_Type(Integer32):
    """Custom type eqlGroupDefaultSnapshotSize based on Integer32"""
    defaultValue = 100


_EqlGroupDefaultSnapshotSize_Object = MibTableColumn
eqlGroupDefaultSnapshotSize = _EqlGroupDefaultSnapshotSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 9),
    _EqlGroupDefaultSnapshotSize_Type()
)
eqlGroupDefaultSnapshotSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultSnapshotSize.setStatus("current")


class _EqlGroupDefaultSnapshotWarningLevel_Type(Integer32):
    """Custom type eqlGroupDefaultSnapshotWarningLevel based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqlGroupDefaultSnapshotWarningLevel_Type.__name__ = "Integer32"
_EqlGroupDefaultSnapshotWarningLevel_Object = MibTableColumn
eqlGroupDefaultSnapshotWarningLevel = _EqlGroupDefaultSnapshotWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 10),
    _EqlGroupDefaultSnapshotWarningLevel_Type()
)
eqlGroupDefaultSnapshotWarningLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultSnapshotWarningLevel.setStatus("current")


class _EqlGroupDefaultSnapshotDeletePolicy_Type(Integer32):
    """Custom type eqlGroupDefaultSnapshotDeletePolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete-oldest", 2),
          ("make-volume-offline", 1),
          ("stop-snapshots", 3))
    )


_EqlGroupDefaultSnapshotDeletePolicy_Type.__name__ = "Integer32"
_EqlGroupDefaultSnapshotDeletePolicy_Object = MibTableColumn
eqlGroupDefaultSnapshotDeletePolicy = _EqlGroupDefaultSnapshotDeletePolicy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 11),
    _EqlGroupDefaultSnapshotDeletePolicy_Type()
)
eqlGroupDefaultSnapshotDeletePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultSnapshotDeletePolicy.setStatus("current")


class _EqlGroupTimeZone_Type(Integer32):
    """Custom type eqlGroupTimeZone based on Integer32"""
    defaultValue = 7

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
              455)
        )
    )
    namedValues = NamedValues(
        *(("act", 22),
          ("aet", 23),
          ("africa-Abidjan", 140),
          ("africa-Accra", 187),
          ("africa-Addis-Ababa", 172),
          ("africa-Algiers", 162),
          ("africa-Asmara", 168),
          ("africa-Bamako", 261),
          ("africa-Bangui", 137),
          ("africa-Banjul", 193),
          ("africa-Bissau", 201),
          ("africa-Blantyre", 274),
          ("africa-Brazzaville", 138),
          ("africa-Bujumbura", 83),
          ("africa-Cairo", 166),
          ("africa-Casablanca", 253),
          ("africa-Ceuta", 170),
          ("africa-Conakry", 194),
          ("africa-Dakar", 351),
          ("africa-Dar-es-Salaam", 373),
          ("africa-Djibouti", 158),
          ("africa-Douala", 144),
          ("africa-El-Aaiun", 167),
          ("africa-Freetown", 349),
          ("africa-Gaborone", 105),
          ("africa-Harare", 423),
          ("africa-Johannesburg", 421),
          ("africa-Juba", 449),
          ("africa-Kampala", 378),
          ("africa-Khartoum", 341),
          ("africa-Kigali", 337),
          ("africa-Kinshasa", 135),
          ("africa-Lagos", 290),
          ("africa-Libreville", 181),
          ("africa-Lome", 361),
          ("africa-Luanda", 39),
          ("africa-Lubumbashi", 136),
          ("africa-Lusaka", 422),
          ("africa-Malabo", 196),
          ("africa-Maputo", 285),
          ("africa-Maseru", 248),
          ("africa-Mbabane", 357),
          ("africa-Mogadishu", 352),
          ("africa-Monrovia", 247),
          ("africa-Nairobi", 225),
          ("africa-Ndjamena", 359),
          ("africa-Niamey", 288),
          ("africa-Nouakchott", 269),
          ("africa-Ouagadougou", 80),
          ("africa-Porto-Novo", 84),
          ("africa-Sao-Tome", 354),
          ("africa-Tripoli", 252),
          ("africa-Tunis", 367),
          ("africa-Windhoek", 286),
          ("agt", 28),
          ("america-Adak", 405),
          ("america-Anchorage", 401),
          ("america-Anguilla", 35),
          ("america-Antigua", 34),
          ("america-Araguaina", 92),
          ("america-Argentina-Buenos-Aires", 50),
          ("america-Argentina-Catamarca", 54),
          ("america-Argentina-Cordoba", 51),
          ("america-Argentina-Jujuy", 52),
          ("america-Argentina-La-Rioja", 55),
          ("america-Argentina-Mendoza", 57),
          ("america-Argentina-Rio-Gallegos", 58),
          ("america-Argentina-Salta", 434),
          ("america-Argentina-San-Juan", 56),
          ("america-Argentina-San-Luis", 432),
          ("america-Argentina-Tucuman", 53),
          ("america-Argentina-Ushuaia", 59),
          ("america-Aruba", 73),
          ("america-Asuncion", 317),
          ("america-Atikokan", 120),
          ("america-Bahia", 94),
          ("america-Bahia-Banderas", 441),
          ("america-Barbados", 77),
          ("america-Belem", 89),
          ("america-Belize", 107),
          ("america-Blanc-Sablon", 113),
          ("america-Boa-Vista", 99),
          ("america-Bogota", 150),
          ("america-Boise", 397),
          ("america-Cambridge-Bay", 124),
          ("america-Campo-Grande", 96),
          ("america-Cancun", 276),
          ("america-Caracas", 412),
          ("america-Cayenne", 185),
          ("america-Cayman", 236),
          ("america-Chicago", 390),
          ("america-Chihuahua", 280),
          ("america-Costa-Rica", 151),
          ("america-Creston", 452),
          ("america-Cuiaba", 97),
          ("america-Curacao", 38),
          ("america-Danmarkshavn", 190),
          ("america-Dawson", 133),
          ("america-Dawson-Creek", 130),
          ("america-Denver", 396),
          ("america-Detroit", 383),
          ("america-Dominica", 160),
          ("america-Edmonton", 127),
          ("america-Eirunepe", 101),
          ("america-El-Salvador", 355),
          ("america-Fortaleza", 90),
          ("america-Glace-Bay", 110),
          ("america-Godthab", 189),
          ("america-Goose-Bay", 112),
          ("america-Grand-Turk", 358),
          ("america-Grenada", 183),
          ("america-Guadeloupe", 195),
          ("america-Guatemala", 199),
          ("america-Guayaquil", 163),
          ("america-Guyana", 202),
          ("america-Halifax", 109),
          ("america-Havana", 152),
          ("america-Hermosillo", 281),
          ("america-Indiana-Indianapolis", 386),
          ("america-Indiana-Knox", 388),
          ("america-Indiana-Marengo", 387),
          ("america-Indiana-Petersburg", 392),
          ("america-Indiana-Tell-City", 425),
          ("america-Indiana-Vevay", 389),
          ("america-Indiana-Vincennes", 391),
          ("america-Indiana-Winamac", 426),
          ("america-Inuvik", 129),
          ("america-Iqaluit", 119),
          ("america-Jamaica", 222),
          ("america-Juneau", 402),
          ("america-Kentucky-Louisville", 384),
          ("america-Kentucky-Monticello", 385),
          ("america-Kralendijk", 447),
          ("america-La-Paz", 87),
          ("america-Lima", 301),
          ("america-Los-Angeles", 400),
          ("america-Lower-Princes", 448),
          ("america-Maceio", 93),
          ("america-Managua", 291),
          ("america-Manaus", 100),
          ("america-Marigot", 428),
          ("america-Martinique", 268),
          ("america-Matamoros", 439),
          ("america-Mazatlan", 279),
          ("america-Menominee", 393),
          ("america-Merida", 277),
          ("america-Metlakatla", 445),
          ("america-Mexico-City", 275),
          ("america-Miquelon", 309),
          ("america-Moncton", 111),
          ("america-Monterrey", 278),
          ("america-Montevideo", 407),
          ("america-Montreal", 114),
          ("america-Montserrat", 270),
          ("america-Nassau", 103),
          ("america-New-York", 382),
          ("america-Nipigon", 116),
          ("america-Nome", 404),
          ("america-Noronha", 88),
          ("america-North-Dakota-Beulah", 444),
          ("america-North-Dakota-Center", 394),
          ("america-North-Dakota-New-Salem", 395),
          ("america-Ojinaga", 436),
          ("america-Panama", 300),
          ("america-Pangnirtung", 118),
          ("america-Paramaribo", 353),
          ("america-Phoenix", 399),
          ("america-Port-au-Prince", 206),
          ("america-Port-of-Spain", 370),
          ("america-Porto-Velho", 98),
          ("america-Puerto-Rico", 311),
          ("america-Rainy-River", 123),
          ("america-Rankin-Inlet", 121),
          ("america-Recife", 91),
          ("america-Regina", 125),
          ("america-Resolute", 427),
          ("america-Rio-Branco", 102),
          ("america-Santa-Isabel", 437),
          ("america-Santarem", 433),
          ("america-Santiago", 142),
          ("america-Santo-Domingo", 161),
          ("america-Sao-Paulo", 95),
          ("america-Scoresbysund", 191),
          ("america-Shiprock", 398),
          ("america-Sitka", 446),
          ("america-St-Barthelemy", 431),
          ("america-St-Johns", 108),
          ("america-St-Kitts", 232),
          ("america-St-Lucia", 244),
          ("america-St-Thomas", 414),
          ("america-St-Vincent", 411),
          ("america-Swift-Current", 126),
          ("america-Tegucigalpa", 204),
          ("america-Thule", 192),
          ("america-Thunder-Bay", 117),
          ("america-Tijuana", 282),
          ("america-Toronto", 115),
          ("america-Tortola", 413),
          ("america-Vancouver", 131),
          ("america-Whitehorse", 132),
          ("america-Winnipeg", 122),
          ("america-Yakutat", 403),
          ("america-Yellowknife", 128),
          ("antarctica-Casey", 46),
          ("antarctica-Davis", 45),
          ("antarctica-DumontDUrville", 48),
          ("antarctica-Macquarie", 440),
          ("antarctica-Mawson", 44),
          ("antarctica-McMurdo", 40),
          ("antarctica-Palmer", 43),
          ("antarctica-Rothera", 42),
          ("antarctica-South-Pole", 41),
          ("antarctica-Syowa", 49),
          ("antarctica-Vostok", 47),
          ("arctic-Longyearbyen", 346),
          ("asia-Aden", 419),
          ("asia-Almaty", 237),
          ("asia-Amman", 223),
          ("asia-Anadyr", 336),
          ("asia-Aqtau", 240),
          ("asia-Aqtobe", 239),
          ("asia-Ashgabat", 366),
          ("asia-Baghdad", 217),
          ("asia-Bahrain", 82),
          ("asia-Baku", 75),
          ("asia-Bangkok", 362),
          ("asia-Beirut", 243),
          ("asia-Bishkek", 226),
          ("asia-Brunei", 86),
          ("asia-Calcutta", 215),
          ("asia-Choibalsan", 265),
          ("asia-Chongqing", 147),
          ("asia-Colombo", 246),
          ("asia-Damascus", 356),
          ("asia-Dhaka", 78),
          ("asia-Dili", 365),
          ("asia-Dubai", 32),
          ("asia-Dushanbe", 363),
          ("asia-Gaza", 312),
          ("asia-Harbin", 146),
          ("asia-Hebron", 450),
          ("asia-Ho-Chi-Minh", 430),
          ("asia-Hong-Kong", 203),
          ("asia-Hovd", 264),
          ("asia-Irkutsk", 330),
          ("asia-Jakarta", 208),
          ("asia-Jayapura", 211),
          ("asia-Jerusalem", 213),
          ("asia-Kabul", 33),
          ("asia-Kamchatka", 335),
          ("asia-Karachi", 307),
          ("asia-Kashgar", 149),
          ("asia-Kathmandu", 435),
          ("asia-Katmandu", 294),
          ("asia-Khandyga", 453),
          ("asia-Kolkata", 429),
          ("asia-Krasnoyarsk", 329),
          ("asia-Kuala-Lumpur", 283),
          ("asia-Kuching", 284),
          ("asia-Kuwait", 235),
          ("asia-Macau", 266),
          ("asia-Magadan", 334),
          ("asia-Makassar", 210),
          ("asia-Manila", 306),
          ("asia-Muscat", 299),
          ("asia-Nicosia", 155),
          ("asia-Novokuznetsk", 438),
          ("asia-Novosibirsk", 328),
          ("asia-Omsk", 327),
          ("asia-Oral", 241),
          ("asia-Phnom-Penh", 227),
          ("asia-Pontianak", 209),
          ("asia-Pyongyang", 233),
          ("asia-Qatar", 318),
          ("asia-Qyzylorda", 238),
          ("asia-Rangoon", 262),
          ("asia-Riyadh", 338),
          ("asia-Saigon", 415),
          ("asia-Sakhalin", 333),
          ("asia-Samarkand", 408),
          ("asia-Seoul", 234),
          ("asia-Shanghai", 145),
          ("asia-Singapore", 343),
          ("asia-Taipei", 372),
          ("asia-Tashkent", 409),
          ("asia-Tbilisi", 184),
          ("asia-Tehran", 218),
          ("asia-Thimphu", 104),
          ("asia-Tokyo", 224),
          ("asia-Ulaanbaatar", 263),
          ("asia-Urumqi", 148),
          ("asia-Ust-Nera", 455),
          ("asia-Vientiane", 242),
          ("asia-Vladivostok", 332),
          ("asia-Yakutsk", 331),
          ("asia-Yekaterinburg", 326),
          ("asia-Yerevan", 37),
          ("ast", 2),
          ("atlantic-Azores", 315),
          ("atlantic-Bermuda", 85),
          ("atlantic-Canary", 171),
          ("atlantic-Cape-Verde", 153),
          ("atlantic-Faroe", 179),
          ("atlantic-Jan-Mayen", 347),
          ("atlantic-Madeira", 314),
          ("atlantic-Reykjavik", 219),
          ("atlantic-South-Georgia", 198),
          ("atlantic-St-Helena", 344),
          ("atlantic-Stanley", 175),
          ("australia-Adelaide", 70),
          ("australia-Brisbane", 68),
          ("australia-Broken-Hill", 67),
          ("australia-Currie", 64),
          ("australia-Darwin", 71),
          ("australia-Eucla", 424),
          ("australia-Hobart", 63),
          ("australia-Lindeman", 69),
          ("australia-Lord-Howe", 62),
          ("australia-Melbourne", 65),
          ("australia-Perth", 72),
          ("australia-Sydney", 66),
          ("bet", 29),
          ("bst", 18),
          ("cat", 30),
          ("cnt", 27),
          ("cst", 6),
          ("ctt", 20),
          ("eat", 13),
          ("ect", 11),
          ("eet", 12),
          ("est", 7),
          ("europe-Amsterdam", 292),
          ("europe-Andorra", 31),
          ("europe-Athens", 197),
          ("europe-Belgrade", 321),
          ("europe-Berlin", 157),
          ("europe-Bratislava", 348),
          ("europe-Brussels", 79),
          ("europe-Bucharest", 320),
          ("europe-Budapest", 207),
          ("europe-Busingen", 454),
          ("europe-Chisinau", 255),
          ("europe-Copenhagen", 159),
          ("europe-Dublin", 212),
          ("europe-Gibraltar", 188),
          ("europe-Guernsey", 186),
          ("europe-Helsinki", 173),
          ("europe-Isle-of-Man", 214),
          ("europe-Istanbul", 369),
          ("europe-Jersey", 221),
          ("europe-Kaliningrad", 322),
          ("europe-Kiev", 374),
          ("europe-Lisbon", 313),
          ("europe-Ljubljana", 345),
          ("europe-London", 182),
          ("europe-Luxembourg", 250),
          ("europe-Madrid", 169),
          ("europe-Malta", 271),
          ("europe-Mariehamn", 74),
          ("europe-Minsk", 106),
          ("europe-Monaco", 254),
          ("europe-Moscow", 323),
          ("europe-Oslo", 293),
          ("europe-Paris", 180),
          ("europe-Podgorica", 256),
          ("europe-Prague", 156),
          ("europe-Riga", 251),
          ("europe-Rome", 220),
          ("europe-Samara", 325),
          ("europe-San-Marino", 350),
          ("europe-Sarajevo", 76),
          ("europe-Simferopol", 377),
          ("europe-Skopje", 260),
          ("europe-Sofia", 81),
          ("europe-Stockholm", 342),
          ("europe-Tallinn", 165),
          ("europe-Tirane", 36),
          ("europe-Tiraspol", 451),
          ("europe-Uzhgorod", 375),
          ("europe-Vaduz", 245),
          ("europe-Vatican", 410),
          ("europe-Vienna", 61),
          ("europe-Vilnius", 249),
          ("europe-Volgograd", 324),
          ("europe-Warsaw", 308),
          ("europe-Zagreb", 205),
          ("europe-Zaporozhye", 376),
          ("europe-Zurich", 139),
          ("gmt", 10),
          ("hst", 1),
          ("iet", 8),
          ("indian-Antananarivo", 257),
          ("indian-Chagos", 216),
          ("indian-Christmas", 154),
          ("indian-Cocos", 134),
          ("indian-Comoro", 231),
          ("indian-Kerguelen", 360),
          ("indian-Mahe", 340),
          ("indian-Maldives", 273),
          ("indian-Mauritius", 272),
          ("indian-Mayotte", 420),
          ("indian-Reunion", 319),
          ("ist", 17),
          ("jst", 21),
          ("met", 14),
          ("mit", 26),
          ("mst", 5),
          ("net", 15),
          ("nst", 25),
          ("pacific-Apia", 418),
          ("pacific-Auckland", 297),
          ("pacific-Chatham", 298),
          ("pacific-Chuuk", 443),
          ("pacific-Easter", 143),
          ("pacific-Efate", 416),
          ("pacific-Enderbury", 229),
          ("pacific-Fakaofo", 364),
          ("pacific-Fiji", 174),
          ("pacific-Funafuti", 371),
          ("pacific-Galapagos", 164),
          ("pacific-Gambier", 304),
          ("pacific-Guadalcanal", 339),
          ("pacific-Guam", 200),
          ("pacific-Honolulu", 406),
          ("pacific-Johnston", 379),
          ("pacific-Kiritimati", 230),
          ("pacific-Kosrae", 178),
          ("pacific-Kwajalein", 259),
          ("pacific-Majuro", 258),
          ("pacific-Marquesas", 303),
          ("pacific-Midway", 380),
          ("pacific-Nauru", 295),
          ("pacific-Niue", 296),
          ("pacific-Norfolk", 289),
          ("pacific-Noumea", 287),
          ("pacific-Pago-Pago", 60),
          ("pacific-Palau", 316),
          ("pacific-Pitcairn", 310),
          ("pacific-Pohnpei", 442),
          ("pacific-Ponape", 177),
          ("pacific-Port-Moresby", 305),
          ("pacific-Rarotonga", 141),
          ("pacific-Saipan", 267),
          ("pacific-Tahiti", 302),
          ("pacific-Tarawa", 228),
          ("pacific-Tongatapu", 368),
          ("pacific-Truk", 176),
          ("pacific-Wake", 381),
          ("pacific-Wallis", 417),
          ("plt", 16),
          ("pnt", 4),
          ("prt", 9),
          ("pst", 3),
          ("sst", 24),
          ("vst", 19))
    )


_EqlGroupTimeZone_Type.__name__ = "Integer32"
_EqlGroupTimeZone_Object = MibTableColumn
eqlGroupTimeZone = _EqlGroupTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 13),
    _EqlGroupTimeZone_Type()
)
eqlGroupTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupTimeZone.setStatus("current")


class _EqlGroupLogLevel_Type(Integer32):
    """Custom type eqlGroupLogLevel based on Integer32"""
    defaultValue = 60


_EqlGroupLogLevel_Object = MibTableColumn
eqlGroupLogLevel = _EqlGroupLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 14),
    _EqlGroupLogLevel_Type()
)
eqlGroupLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupLogLevel.setStatus("current")


class _EqlGroupDescription_Type(UTFString):
    """Custom type eqlGroupDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlGroupDescription_Type.__name__ = "UTFString"
_EqlGroupDescription_Object = MibTableColumn
eqlGroupDescription = _EqlGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 15),
    _EqlGroupDescription_Type()
)
eqlGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDescription.setStatus("current")


class _EqlGroupIscsiNamePrefix_Type(DisplayString):
    """Custom type eqlGroupIscsiNamePrefix based on DisplayString"""
    defaultValue = OctetString("iqn.2001-04.com.equallogic.")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlGroupIscsiNamePrefix_Type.__name__ = "DisplayString"
_EqlGroupIscsiNamePrefix_Object = MibTableColumn
eqlGroupIscsiNamePrefix = _EqlGroupIscsiNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 16),
    _EqlGroupIscsiNamePrefix_Type()
)
eqlGroupIscsiNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupIscsiNamePrefix.setStatus("current")


class _EqlGroupDefaultAliasToVolumeName_Type(TruthValue):
    """Custom type eqlGroupDefaultAliasToVolumeName based on TruthValue"""


_EqlGroupDefaultAliasToVolumeName_Object = MibTableColumn
eqlGroupDefaultAliasToVolumeName = _EqlGroupDefaultAliasToVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 17),
    _EqlGroupDefaultAliasToVolumeName_Type()
)
eqlGroupDefaultAliasToVolumeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultAliasToVolumeName.setStatus("current")


class _EqlGroupEmailSrcDomain_Type(DisplayString):
    """Custom type eqlGroupEmailSrcDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqlGroupEmailSrcDomain_Type.__name__ = "DisplayString"
_EqlGroupEmailSrcDomain_Object = MibTableColumn
eqlGroupEmailSrcDomain = _EqlGroupEmailSrcDomain_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 18),
    _EqlGroupEmailSrcDomain_Type()
)
eqlGroupEmailSrcDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEmailSrcDomain.setStatus("current")


class _EqlGroupName_Type(DisplayString):
    """Custom type eqlGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlGroupName_Type.__name__ = "DisplayString"
_EqlGroupName_Object = MibTableColumn
eqlGroupName = _EqlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 19),
    _EqlGroupName_Type()
)
eqlGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupName.setStatus("current")
_EqlGroupIpAddr_Type = IpAddress
_EqlGroupIpAddr_Object = MibTableColumn
eqlGroupIpAddr = _EqlGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 20),
    _EqlGroupIpAddr_Type()
)
eqlGroupIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupIpAddr.setStatus("current")


class _EqlGroupEnableWebAccessSSL_Type(TruthValue):
    """Custom type eqlGroupEnableWebAccessSSL based on TruthValue"""


_EqlGroupEnableWebAccessSSL_Object = MibTableColumn
eqlGroupEnableWebAccessSSL = _EqlGroupEnableWebAccessSSL_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 21),
    _EqlGroupEnableWebAccessSSL_Type()
)
eqlGroupEnableWebAccessSSL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableWebAccessSSL.setStatus("current")


class _EqlGroupEnableWebAccessUnsecure_Type(TruthValue):
    """Custom type eqlGroupEnableWebAccessUnsecure based on TruthValue"""


_EqlGroupEnableWebAccessUnsecure_Object = MibTableColumn
eqlGroupEnableWebAccessUnsecure = _EqlGroupEnableWebAccessUnsecure_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 22),
    _EqlGroupEnableWebAccessUnsecure_Type()
)
eqlGroupEnableWebAccessUnsecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableWebAccessUnsecure.setStatus("current")


class _EqlGroupEnableCliAccessSSH_Type(TruthValue):
    """Custom type eqlGroupEnableCliAccessSSH based on TruthValue"""


_EqlGroupEnableCliAccessSSH_Object = MibTableColumn
eqlGroupEnableCliAccessSSH = _EqlGroupEnableCliAccessSSH_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 23),
    _EqlGroupEnableCliAccessSSH_Type()
)
eqlGroupEnableCliAccessSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableCliAccessSSH.setStatus("current")


class _EqlGroupEnableCliAccessUnsecure_Type(TruthValue):
    """Custom type eqlGroupEnableCliAccessUnsecure based on TruthValue"""


_EqlGroupEnableCliAccessUnsecure_Object = MibTableColumn
eqlGroupEnableCliAccessUnsecure = _EqlGroupEnableCliAccessUnsecure_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 24),
    _EqlGroupEnableCliAccessUnsecure_Type()
)
eqlGroupEnableCliAccessUnsecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableCliAccessUnsecure.setStatus("current")


class _EqlGroupEnableEmailNotifications_Type(TruthValue):
    """Custom type eqlGroupEnableEmailNotifications based on TruthValue"""


_EqlGroupEnableEmailNotifications_Object = MibTableColumn
eqlGroupEnableEmailNotifications = _EqlGroupEnableEmailNotifications_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 25),
    _EqlGroupEnableEmailNotifications_Type()
)
eqlGroupEnableEmailNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableEmailNotifications.setStatus("current")


class _EqlGroupEnableSNMPTraps_Type(TruthValue):
    """Custom type eqlGroupEnableSNMPTraps based on TruthValue"""


_EqlGroupEnableSNMPTraps_Object = MibTableColumn
eqlGroupEnableSNMPTraps = _EqlGroupEnableSNMPTraps_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 26),
    _EqlGroupEnableSNMPTraps_Type()
)
eqlGroupEnableSNMPTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableSNMPTraps.setStatus("current")


class _EqlGroupEnableSyslog_Type(TruthValue):
    """Custom type eqlGroupEnableSyslog based on TruthValue"""


_EqlGroupEnableSyslog_Object = MibTableColumn
eqlGroupEnableSyslog = _EqlGroupEnableSyslog_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 27),
    _EqlGroupEnableSyslog_Type()
)
eqlGroupEnableSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableSyslog.setStatus("current")
_EqlGroupEmailPriorityMask_Type = Integer32
_EqlGroupEmailPriorityMask_Object = MibTableColumn
eqlGroupEmailPriorityMask = _EqlGroupEmailPriorityMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 28),
    _EqlGroupEmailPriorityMask_Type()
)
eqlGroupEmailPriorityMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEmailPriorityMask.setStatus("current")
_EqlGroupSNMPPriorityMask_Type = Integer32
_EqlGroupSNMPPriorityMask_Object = MibTableColumn
eqlGroupSNMPPriorityMask = _EqlGroupSNMPPriorityMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 29),
    _EqlGroupSNMPPriorityMask_Type()
)
eqlGroupSNMPPriorityMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupSNMPPriorityMask.setStatus("deprecated")
_EqlGroupSysLogPriorityMask_Type = Integer32
_EqlGroupSysLogPriorityMask_Object = MibTableColumn
eqlGroupSysLogPriorityMask = _EqlGroupSysLogPriorityMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 30),
    _EqlGroupSysLogPriorityMask_Type()
)
eqlGroupSysLogPriorityMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupSysLogPriorityMask.setStatus("current")


class _EqlGroupDefaultSite_Type(DisplayString):
    """Custom type eqlGroupDefaultSite based on DisplayString"""
    defaultValue = OctetString("default")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlGroupDefaultSite_Type.__name__ = "DisplayString"
_EqlGroupDefaultSite_Object = MibTableColumn
eqlGroupDefaultSite = _EqlGroupDefaultSite_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 31),
    _EqlGroupDefaultSite_Type()
)
eqlGroupDefaultSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultSite.setStatus("current")


class _EqlGroupPasswd1_Type(OctetString):
    """Custom type eqlGroupPasswd1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlGroupPasswd1_Type.__name__ = "OctetString"
_EqlGroupPasswd1_Object = MibTableColumn
eqlGroupPasswd1 = _EqlGroupPasswd1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 32),
    _EqlGroupPasswd1_Type()
)
eqlGroupPasswd1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupPasswd1.setStatus("current")


class _EqlGroupPasswd2_Type(DisplayString):
    """Custom type eqlGroupPasswd2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlGroupPasswd2_Type.__name__ = "DisplayString"
_EqlGroupPasswd2_Object = MibTableColumn
eqlGroupPasswd2 = _EqlGroupPasswd2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 33),
    _EqlGroupPasswd2_Type()
)
eqlGroupPasswd2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlGroupPasswd2.setStatus("current")
_EqlGroupRowStatus_Type = RowStatus
_EqlGroupRowStatus_Object = MibTableColumn
eqlGroupRowStatus = _EqlGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 34),
    _EqlGroupRowStatus_Type()
)
eqlGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupRowStatus.setStatus("current")


class _EqlGroupObjectReuseScrub_Type(Integer32):
    """Custom type eqlGroupObjectReuseScrub based on Integer32"""
    defaultValue = 1

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


_EqlGroupObjectReuseScrub_Type.__name__ = "Integer32"
_EqlGroupObjectReuseScrub_Object = MibTableColumn
eqlGroupObjectReuseScrub = _EqlGroupObjectReuseScrub_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 35),
    _EqlGroupObjectReuseScrub_Type()
)
eqlGroupObjectReuseScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlGroupObjectReuseScrub.setStatus("deprecated")


class _EqlGroupEnableSSH_Type(TruthValue):
    """Custom type eqlGroupEnableSSH based on TruthValue"""


_EqlGroupEnableSSH_Object = MibTableColumn
eqlGroupEnableSSH = _EqlGroupEnableSSH_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 36),
    _EqlGroupEnableSSH_Type()
)
eqlGroupEnableSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableSSH.setStatus("deprecated")


class _EqlGroupEnableTelnet_Type(TruthValue):
    """Custom type eqlGroupEnableTelnet based on TruthValue"""


_EqlGroupEnableTelnet_Object = MibTableColumn
eqlGroupEnableTelnet = _EqlGroupEnableTelnet_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 37),
    _EqlGroupEnableTelnet_Type()
)
eqlGroupEnableTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableTelnet.setStatus("deprecated")


class _EqlGroupEnableFTP_Type(TruthValue):
    """Custom type eqlGroupEnableFTP based on TruthValue"""


_EqlGroupEnableFTP_Object = MibTableColumn
eqlGroupEnableFTP = _EqlGroupEnableFTP_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 38),
    _EqlGroupEnableFTP_Type()
)
eqlGroupEnableFTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableFTP.setStatus("current")


class _EqlGroupEmailSrcUserName_Type(DisplayString):
    """Custom type eqlGroupEmailSrcUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqlGroupEmailSrcUserName_Type.__name__ = "DisplayString"
_EqlGroupEmailSrcUserName_Object = MibTableColumn
eqlGroupEmailSrcUserName = _EqlGroupEmailSrcUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 39),
    _EqlGroupEmailSrcUserName_Type()
)
eqlGroupEmailSrcUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEmailSrcUserName.setStatus("current")


class _EqlGroupSyslogFacility_Type(Integer32):
    """Custom type eqlGroupSyslogFacility based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("auth", 5),
          ("authpriv", 11),
          ("cron", 10),
          ("daemon", 4),
          ("default", 0),
          ("ftp", 12),
          ("kern", 1),
          ("local0", 17),
          ("local1", 18),
          ("local2", 19),
          ("local3", 20),
          ("local4", 21),
          ("local5", 22),
          ("local6", 23),
          ("local7", 24),
          ("lpr", 7),
          ("mail", 3),
          ("news", 8),
          ("syslog", 6),
          ("user", 2),
          ("uucp", 9))
    )


_EqlGroupSyslogFacility_Type.__name__ = "Integer32"
_EqlGroupSyslogFacility_Object = MibTableColumn
eqlGroupSyslogFacility = _EqlGroupSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 40),
    _EqlGroupSyslogFacility_Type()
)
eqlGroupSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupSyslogFacility.setStatus("current")


class _EqlGroupEnableCLB_Type(TruthValue):
    """Custom type eqlGroupEnableCLB based on TruthValue"""


_EqlGroupEnableCLB_Object = MibTableColumn
eqlGroupEnableCLB = _EqlGroupEnableCLB_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 41),
    _EqlGroupEnableCLB_Type()
)
eqlGroupEnableCLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableCLB.setStatus("current")


class _EqlGroupEnableVolBal_Type(TruthValue):
    """Custom type eqlGroupEnableVolBal based on TruthValue"""


_EqlGroupEnableVolBal_Object = MibTableColumn
eqlGroupEnableVolBal = _EqlGroupEnableVolBal_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 42),
    _EqlGroupEnableVolBal_Type()
)
eqlGroupEnableVolBal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableVolBal.setStatus("current")


class _EqlGroupDiscoveryFilter_Type(TruthValue):
    """Custom type eqlGroupDiscoveryFilter based on TruthValue"""


_EqlGroupDiscoveryFilter_Object = MibTableColumn
eqlGroupDiscoveryFilter = _EqlGroupDiscoveryFilter_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 43),
    _EqlGroupDiscoveryFilter_Type()
)
eqlGroupDiscoveryFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDiscoveryFilter.setStatus("current")


class _EqlGroupEmailSupportContact_Type(DisplayString):
    """Custom type eqlGroupEmailSupportContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlGroupEmailSupportContact_Type.__name__ = "DisplayString"
_EqlGroupEmailSupportContact_Object = MibTableColumn
eqlGroupEmailSupportContact = _EqlGroupEmailSupportContact_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 44),
    _EqlGroupEmailSupportContact_Type()
)
eqlGroupEmailSupportContact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupEmailSupportContact.setStatus("current")


class _EqlGroupReplicationWindowSize_Type(Unsigned32):
    """Custom type eqlGroupReplicationWindowSize based on Unsigned32"""
    defaultValue = 72


_EqlGroupReplicationWindowSize_Object = MibTableColumn
eqlGroupReplicationWindowSize = _EqlGroupReplicationWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 45),
    _EqlGroupReplicationWindowSize_Type()
)
eqlGroupReplicationWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupReplicationWindowSize.setStatus("current")
if mibBuilder.loadTexts:
    eqlGroupReplicationWindowSize.setUnits("KB")


class _EqlGroupConfigurationFlags_Type(Bits):
    """Custom type eqlGroupConfigurationFlags based on Bits"""
    namedValues = NamedValues(
        *(("array-restart-flag", 2),
          ("cluster-pr-flag", 0),
          ("dcb-disable", 5),
          ("flag12", 12),
          ("flag13", 13),
          ("flag14", 14),
          ("flag15", 15),
          ("flag16", 16),
          ("flag17", 17),
          ("flag18", 18),
          ("flag19", 19),
          ("flag20", 20),
          ("flag21", 21),
          ("flag22", 22),
          ("flag23", 23),
          ("flag24", 24),
          ("flag25", 25),
          ("flag26", 26),
          ("flag27", 27),
          ("flag28", 28),
          ("flag29", 29),
          ("flag30", 30),
          ("flag31", 31),
          ("force-SCSI-QErr-OldBehavior", 4),
          ("ignore-group-conn", 1),
          ("lldp-vlanidneg-disable", 6),
          ("mpio-dynamic-scaling-mask0", 7),
          ("mpio-dynamic-scaling-mask1", 9),
          ("repl-use-jumbos", 3),
          ("sacl-disable", 11),
          ("unmap-disable", 8),
          ("volume-fix-run", 10))
    )

_EqlGroupConfigurationFlags_Type.__name__ = "Bits"
_EqlGroupConfigurationFlags_Object = MibTableColumn
eqlGroupConfigurationFlags = _EqlGroupConfigurationFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 46),
    _EqlGroupConfigurationFlags_Type()
)
eqlGroupConfigurationFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupConfigurationFlags.setStatus("current")


class _EqlGroupISCSIPortalGrpTag_Type(Integer32):
    """Custom type eqlGroupISCSIPortalGrpTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("configuredAndSetToOne", 9),
          ("configuredAndSetToZero", 8),
          ("notConfigured", 0))
    )


_EqlGroupISCSIPortalGrpTag_Type.__name__ = "Integer32"
_EqlGroupISCSIPortalGrpTag_Object = MibTableColumn
eqlGroupISCSIPortalGrpTag = _EqlGroupISCSIPortalGrpTag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 47),
    _EqlGroupISCSIPortalGrpTag_Type()
)
eqlGroupISCSIPortalGrpTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlGroupISCSIPortalGrpTag.setStatus("current")


class _EqlGroupMaxConcurrentReplicas_Type(Integer32):
    """Custom type eqlGroupMaxConcurrentReplicas based on Integer32"""
    defaultValue = 16


_EqlGroupMaxConcurrentReplicas_Object = MibTableColumn
eqlGroupMaxConcurrentReplicas = _EqlGroupMaxConcurrentReplicas_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 48),
    _EqlGroupMaxConcurrentReplicas_Type()
)
eqlGroupMaxConcurrentReplicas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupMaxConcurrentReplicas.setStatus("current")


class _EqlGroupDefaultThinWarn_Type(Unsigned32):
    """Custom type eqlGroupDefaultThinWarn based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EqlGroupDefaultThinWarn_Type.__name__ = "Unsigned32"
_EqlGroupDefaultThinWarn_Object = MibTableColumn
eqlGroupDefaultThinWarn = _EqlGroupDefaultThinWarn_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 49),
    _EqlGroupDefaultThinWarn_Type()
)
eqlGroupDefaultThinWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultThinWarn.setStatus("current")


class _EqlGroupDefaultThinMaxGrow_Type(Unsigned32):
    """Custom type eqlGroupDefaultThinMaxGrow based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EqlGroupDefaultThinMaxGrow_Type.__name__ = "Unsigned32"
_EqlGroupDefaultThinMaxGrow_Object = MibTableColumn
eqlGroupDefaultThinMaxGrow = _EqlGroupDefaultThinMaxGrow_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 50),
    _EqlGroupDefaultThinMaxGrow_Type()
)
eqlGroupDefaultThinMaxGrow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultThinMaxGrow.setStatus("current")
_EqlGroupDefaultMgmtGatewayIpAddressType_Type = InetAddressType
_EqlGroupDefaultMgmtGatewayIpAddressType_Object = MibTableColumn
eqlGroupDefaultMgmtGatewayIpAddressType = _EqlGroupDefaultMgmtGatewayIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 51),
    _EqlGroupDefaultMgmtGatewayIpAddressType_Type()
)
eqlGroupDefaultMgmtGatewayIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultMgmtGatewayIpAddressType.setStatus("current")
_EqlGroupDefaultMgmtGatewayIpAddress_Type = InetAddress
_EqlGroupDefaultMgmtGatewayIpAddress_Object = MibTableColumn
eqlGroupDefaultMgmtGatewayIpAddress = _EqlGroupDefaultMgmtGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 52),
    _EqlGroupDefaultMgmtGatewayIpAddress_Type()
)
eqlGroupDefaultMgmtGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultMgmtGatewayIpAddress.setStatus("current")


class _EqlGroupInet6AddrType_Type(InetAddressType):
    """Custom type eqlGroupInet6AddrType based on InetAddressType"""
    defaultValue = 2


_EqlGroupInet6AddrType_Object = MibTableColumn
eqlGroupInet6AddrType = _EqlGroupInet6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 53),
    _EqlGroupInet6AddrType_Type()
)
eqlGroupInet6AddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupInet6AddrType.setStatus("current")
_EqlGroupInet6Addr_Type = InetAddress
_EqlGroupInet6Addr_Object = MibTableColumn
eqlGroupInet6Addr = _EqlGroupInet6Addr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 54),
    _EqlGroupInet6Addr_Type()
)
eqlGroupInet6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupInet6Addr.setStatus("current")


class _EqlGroupInetAddrType_Type(InetAddressType):
    """Custom type eqlGroupInetAddrType based on InetAddressType"""
    defaultValue = 1


_EqlGroupInetAddrType_Object = MibTableColumn
eqlGroupInetAddrType = _EqlGroupInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 55),
    _EqlGroupInetAddrType_Type()
)
eqlGroupInetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupInetAddrType.setStatus("current")
_EqlGroupInetAddr_Type = InetAddress
_EqlGroupInetAddr_Object = MibTableColumn
eqlGroupInetAddr = _EqlGroupInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 56),
    _EqlGroupInetAddr_Type()
)
eqlGroupInetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupInetAddr.setStatus("current")


class _EqlGroupSupportSlowSwitch_Type(Integer32):
    """Custom type eqlGroupSupportSlowSwitch based on Integer32"""
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
        *(("automatic", 1),
          ("off", 0),
          ("on", 2))
    )


_EqlGroupSupportSlowSwitch_Type.__name__ = "Integer32"
_EqlGroupSupportSlowSwitch_Object = MibTableColumn
eqlGroupSupportSlowSwitch = _EqlGroupSupportSlowSwitch_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 57),
    _EqlGroupSupportSlowSwitch_Type()
)
eqlGroupSupportSlowSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupSupportSlowSwitch.setStatus("current")


class _EqlGroupProfileIndex_Type(Unsigned32):
    """Custom type eqlGroupProfileIndex based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EqlGroupProfileIndex_Type.__name__ = "Unsigned32"
_EqlGroupProfileIndex_Object = MibTableColumn
eqlGroupProfileIndex = _EqlGroupProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 58),
    _EqlGroupProfileIndex_Type()
)
eqlGroupProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlGroupProfileIndex.setStatus("current")


class _EqlGroupEnableSSHProtocolV1_Type(TruthValue):
    """Custom type eqlGroupEnableSSHProtocolV1 based on TruthValue"""


_EqlGroupEnableSSHProtocolV1_Object = MibTableColumn
eqlGroupEnableSSHProtocolV1 = _EqlGroupEnableSSHProtocolV1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 59),
    _EqlGroupEnableSSHProtocolV1_Type()
)
eqlGroupEnableSSHProtocolV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableSSHProtocolV1.setStatus("current")


class _EqlGroupEnableStandbyButton_Type(TruthValue):
    """Custom type eqlGroupEnableStandbyButton based on TruthValue"""


_EqlGroupEnableStandbyButton_Object = MibTableColumn
eqlGroupEnableStandbyButton = _EqlGroupEnableStandbyButton_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 60),
    _EqlGroupEnableStandbyButton_Type()
)
eqlGroupEnableStandbyButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableStandbyButton.setStatus("current")


class _EqlGroupLDAPLoginAuthEnable_Type(TruthValue):
    """Custom type eqlGroupLDAPLoginAuthEnable based on TruthValue"""


_EqlGroupLDAPLoginAuthEnable_Object = MibTableColumn
eqlGroupLDAPLoginAuthEnable = _EqlGroupLDAPLoginAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 61),
    _EqlGroupLDAPLoginAuthEnable_Type()
)
eqlGroupLDAPLoginAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupLDAPLoginAuthEnable.setStatus("current")


class _EqlGroupApplianceDiscovery_Type(Integer32):
    """Custom type eqlGroupApplianceDiscovery based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("discover", 0)
    )


_EqlGroupApplianceDiscovery_Type.__name__ = "Integer32"
_EqlGroupApplianceDiscovery_Object = MibTableColumn
eqlGroupApplianceDiscovery = _EqlGroupApplianceDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 62),
    _EqlGroupApplianceDiscovery_Type()
)
eqlGroupApplianceDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupApplianceDiscovery.setStatus("current")


class _EqlGroupDefaultDcbVlanId_Type(Unsigned32):
    """Custom type eqlGroupDefaultDcbVlanId based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_EqlGroupDefaultDcbVlanId_Type.__name__ = "Unsigned32"
_EqlGroupDefaultDcbVlanId_Object = MibTableColumn
eqlGroupDefaultDcbVlanId = _EqlGroupDefaultDcbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 63),
    _EqlGroupDefaultDcbVlanId_Type()
)
eqlGroupDefaultDcbVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultDcbVlanId.setStatus("current")


class _EqlGroupThermalShutdownOverride_Type(Integer32):
    """Custom type eqlGroupThermalShutdownOverride based on Integer32"""
    defaultValue = 0

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


_EqlGroupThermalShutdownOverride_Type.__name__ = "Integer32"
_EqlGroupThermalShutdownOverride_Object = MibTableColumn
eqlGroupThermalShutdownOverride = _EqlGroupThermalShutdownOverride_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 64),
    _EqlGroupThermalShutdownOverride_Type()
)
eqlGroupThermalShutdownOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupThermalShutdownOverride.setStatus("current")


class _EqlGroupEnableLegacyCryptos_Type(Integer32):
    """Custom type eqlGroupEnableLegacyCryptos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_EqlGroupEnableLegacyCryptos_Type.__name__ = "Integer32"
_EqlGroupEnableLegacyCryptos_Object = MibTableColumn
eqlGroupEnableLegacyCryptos = _EqlGroupEnableLegacyCryptos_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 65),
    _EqlGroupEnableLegacyCryptos_Type()
)
eqlGroupEnableLegacyCryptos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableLegacyCryptos.setStatus("current")


class _EqlGroupMaxReplSegments_Type(Integer32):
    """Custom type eqlGroupMaxReplSegments based on Integer32"""
    defaultValue = 60


_EqlGroupMaxReplSegments_Object = MibTableColumn
eqlGroupMaxReplSegments = _EqlGroupMaxReplSegments_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 66),
    _EqlGroupMaxReplSegments_Type()
)
eqlGroupMaxReplSegments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupMaxReplSegments.setStatus("current")


class _EqlGroupEnableVolumeRecovery_Type(TruthValue):
    """Custom type eqlGroupEnableVolumeRecovery based on TruthValue"""


_EqlGroupEnableVolumeRecovery_Object = MibTableColumn
eqlGroupEnableVolumeRecovery = _EqlGroupEnableVolumeRecovery_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 67),
    _EqlGroupEnableVolumeRecovery_Type()
)
eqlGroupEnableVolumeRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupEnableVolumeRecovery.setStatus("current")


class _EqlGroupSessionIdleTimeout_Type(Integer32):
    """Custom type eqlGroupSessionIdleTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_EqlGroupSessionIdleTimeout_Type.__name__ = "Integer32"
_EqlGroupSessionIdleTimeout_Object = MibTableColumn
eqlGroupSessionIdleTimeout = _EqlGroupSessionIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 68),
    _EqlGroupSessionIdleTimeout_Type()
)
eqlGroupSessionIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupSessionIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    eqlGroupSessionIdleTimeout.setUnits("minutes")


class _EqlGroupSessionIdleTimeoutEnable_Type(Integer32):
    """Custom type eqlGroupSessionIdleTimeoutEnable based on Integer32"""
    defaultValue = 0

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


_EqlGroupSessionIdleTimeoutEnable_Type.__name__ = "Integer32"
_EqlGroupSessionIdleTimeoutEnable_Object = MibTableColumn
eqlGroupSessionIdleTimeoutEnable = _EqlGroupSessionIdleTimeoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 69),
    _EqlGroupSessionIdleTimeoutEnable_Type()
)
eqlGroupSessionIdleTimeoutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupSessionIdleTimeoutEnable.setStatus("current")


class _EqlGroupSessionBannerEnable_Type(Integer32):
    """Custom type eqlGroupSessionBannerEnable based on Integer32"""
    defaultValue = 0

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


_EqlGroupSessionBannerEnable_Type.__name__ = "Integer32"
_EqlGroupSessionBannerEnable_Object = MibTableColumn
eqlGroupSessionBannerEnable = _EqlGroupSessionBannerEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 70),
    _EqlGroupSessionBannerEnable_Type()
)
eqlGroupSessionBannerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupSessionBannerEnable.setStatus("current")


class _EqlGroupDefaultVolSnapshotBorrowEnabled_Type(TruthValue):
    """Custom type eqlGroupDefaultVolSnapshotBorrowEnabled based on TruthValue"""


_EqlGroupDefaultVolSnapshotBorrowEnabled_Object = MibTableColumn
eqlGroupDefaultVolSnapshotBorrowEnabled = _EqlGroupDefaultVolSnapshotBorrowEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 71),
    _EqlGroupDefaultVolSnapshotBorrowEnabled_Type()
)
eqlGroupDefaultVolSnapshotBorrowEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupDefaultVolSnapshotBorrowEnabled.setStatus("current")


class _EqlGroupRecoveryLifeTimeEnable_Type(TruthValue):
    """Custom type eqlGroupRecoveryLifeTimeEnable based on TruthValue"""


_EqlGroupRecoveryLifeTimeEnable_Object = MibTableColumn
eqlGroupRecoveryLifeTimeEnable = _EqlGroupRecoveryLifeTimeEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 72),
    _EqlGroupRecoveryLifeTimeEnable_Type()
)
eqlGroupRecoveryLifeTimeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupRecoveryLifeTimeEnable.setStatus("current")


class _EqlGroupRecoveryLifeTime_Type(Integer32):
    """Custom type eqlGroupRecoveryLifeTime based on Integer32"""
    defaultValue = 0


_EqlGroupRecoveryLifeTime_Object = MibTableColumn
eqlGroupRecoveryLifeTime = _EqlGroupRecoveryLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 73),
    _EqlGroupRecoveryLifeTime_Type()
)
eqlGroupRecoveryLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupRecoveryLifeTime.setStatus("current")


class _EqlGroupTimeProtocol_Type(Integer32):
    """Custom type eqlGroupTimeProtocol based on Integer32"""
    defaultValue = 0


_EqlGroupTimeProtocol_Object = MibTableColumn
eqlGroupTimeProtocol = _EqlGroupTimeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 74),
    _EqlGroupTimeProtocol_Type()
)
eqlGroupTimeProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupTimeProtocol.setStatus("current")


class _EqlGroupRecoveryTrimmerFreq_Type(Integer32):
    """Custom type eqlGroupRecoveryTrimmerFreq based on Integer32"""
    defaultValue = 86400


_EqlGroupRecoveryTrimmerFreq_Object = MibTableColumn
eqlGroupRecoveryTrimmerFreq = _EqlGroupRecoveryTrimmerFreq_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 75),
    _EqlGroupRecoveryTrimmerFreq_Type()
)
eqlGroupRecoveryTrimmerFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupRecoveryTrimmerFreq.setStatus("current")


class _EqlGroupUpdateEnable_Type(Integer32):
    """Custom type eqlGroupUpdateEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_EqlGroupUpdateEnable_Type.__name__ = "Integer32"
_EqlGroupUpdateEnable_Object = MibTableColumn
eqlGroupUpdateEnable = _EqlGroupUpdateEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 76),
    _EqlGroupUpdateEnable_Type()
)
eqlGroupUpdateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupUpdateEnable.setStatus("current")
_EqlGroupUpdateLast_Type = Unsigned32
_EqlGroupUpdateLast_Object = MibTableColumn
eqlGroupUpdateLast = _EqlGroupUpdateLast_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 77),
    _EqlGroupUpdateLast_Type()
)
eqlGroupUpdateLast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupUpdateLast.setStatus("current")


class _EqlGroupDefaultSectorSize_Type(Integer32):
    """Custom type eqlGroupDefaultSectorSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sector-size-4096-bytes", 1),
          ("sector-size-512-bytes", 0))
    )


_EqlGroupDefaultSectorSize_Type.__name__ = "Integer32"
_EqlGroupDefaultSectorSize_Object = MibTableColumn
eqlGroupDefaultSectorSize = _EqlGroupDefaultSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 78),
    _EqlGroupDefaultSectorSize_Type()
)
eqlGroupDefaultSectorSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupDefaultSectorSize.setStatus("current")


class _EqlGroupCompressionScanFreq_Type(Integer32):
    """Custom type eqlGroupCompressionScanFreq based on Integer32"""
    defaultValue = 60


_EqlGroupCompressionScanFreq_Object = MibTableColumn
eqlGroupCompressionScanFreq = _EqlGroupCompressionScanFreq_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 80),
    _EqlGroupCompressionScanFreq_Type()
)
eqlGroupCompressionScanFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupCompressionScanFreq.setStatus("current")


class _EqlGroupRunCompressionScan_Type(Integer32):
    """Custom type eqlGroupRunCompressionScan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_EqlGroupRunCompressionScan_Type.__name__ = "Integer32"
_EqlGroupRunCompressionScan_Object = MibTableColumn
eqlGroupRunCompressionScan = _EqlGroupRunCompressionScan_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 81),
    _EqlGroupRunCompressionScan_Type()
)
eqlGroupRunCompressionScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupRunCompressionScan.setStatus("current")


class _EqlGroupMonitorReminderTimestamp_Type(Unsigned32):
    """Custom type eqlGroupMonitorReminderTimestamp based on Unsigned32"""
    defaultValue = 0


_EqlGroupMonitorReminderTimestamp_Object = MibTableColumn
eqlGroupMonitorReminderTimestamp = _EqlGroupMonitorReminderTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 1, 1, 82),
    _EqlGroupMonitorReminderTimestamp_Type()
)
eqlGroupMonitorReminderTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupMonitorReminderTimestamp.setStatus("current")
_EqlStorageGroupStatusTable_Object = MibTable
eqlStorageGroupStatusTable = _EqlStorageGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eqlStorageGroupStatusTable.setStatus("current")
_EqlStorageGroupStatusEntry_Object = MibTableRow
eqlStorageGroupStatusEntry = _EqlStorageGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1)
)
eqlStorageGroupStatusEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupStatusEntry.setStatus("current")
_EqlStorageGroupStatusPoolSpace_Type = Integer32
_EqlStorageGroupStatusPoolSpace_Object = MibTableColumn
eqlStorageGroupStatusPoolSpace = _EqlStorageGroupStatusPoolSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 1),
    _EqlStorageGroupStatusPoolSpace_Type()
)
eqlStorageGroupStatusPoolSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusPoolSpace.setStatus("current")
_EqlStorageGroupStatusPoolSpaceUsed_Type = Integer32
_EqlStorageGroupStatusPoolSpaceUsed_Object = MibTableColumn
eqlStorageGroupStatusPoolSpaceUsed = _EqlStorageGroupStatusPoolSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 2),
    _EqlStorageGroupStatusPoolSpaceUsed_Type()
)
eqlStorageGroupStatusPoolSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusPoolSpaceUsed.setStatus("current")
_EqlStorageGroupStatusTotalMembersOnLine_Type = Integer32
_EqlStorageGroupStatusTotalMembersOnLine_Object = MibTableColumn
eqlStorageGroupStatusTotalMembersOnLine = _EqlStorageGroupStatusTotalMembersOnLine_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 3),
    _EqlStorageGroupStatusTotalMembersOnLine_Type()
)
eqlStorageGroupStatusTotalMembersOnLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusTotalMembersOnLine.setStatus("current")
_EqlStorageGroupStatusPoolSpaceReserved_Type = Integer32
_EqlStorageGroupStatusPoolSpaceReserved_Object = MibTableColumn
eqlStorageGroupStatusPoolSpaceReserved = _EqlStorageGroupStatusPoolSpaceReserved_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 4),
    _EqlStorageGroupStatusPoolSpaceReserved_Type()
)
eqlStorageGroupStatusPoolSpaceReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusPoolSpaceReserved.setStatus("current")
_EqlStorageGroupStatusReservedSpaceInUse_Type = Integer32
_EqlStorageGroupStatusReservedSpaceInUse_Object = MibTableColumn
eqlStorageGroupStatusReservedSpaceInUse = _EqlStorageGroupStatusReservedSpaceInUse_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 5),
    _EqlStorageGroupStatusReservedSpaceInUse_Type()
)
eqlStorageGroupStatusReservedSpaceInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusReservedSpaceInUse.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusReservedSpaceInUse.setUnits("MB")
_EqlStorageGroupStatusDateAndTime_Type = Unsigned32
_EqlStorageGroupStatusDateAndTime_Object = MibTableColumn
eqlStorageGroupStatusDateAndTime = _EqlStorageGroupStatusDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 6),
    _EqlStorageGroupStatusDateAndTime_Type()
)
eqlStorageGroupStatusDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusDateAndTime.setStatus("current")
_EqlStorageGroupStatusSnapshotsInUse_Type = Integer32
_EqlStorageGroupStatusSnapshotsInUse_Object = MibTableColumn
eqlStorageGroupStatusSnapshotsInUse = _EqlStorageGroupStatusSnapshotsInUse_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 7),
    _EqlStorageGroupStatusSnapshotsInUse_Type()
)
eqlStorageGroupStatusSnapshotsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusSnapshotsInUse.setStatus("current")
_EqlStorageGroupStatusVolumesInUse_Type = Integer32
_EqlStorageGroupStatusVolumesInUse_Object = MibTableColumn
eqlStorageGroupStatusVolumesInUse = _EqlStorageGroupStatusVolumesInUse_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 8),
    _EqlStorageGroupStatusVolumesInUse_Type()
)
eqlStorageGroupStatusVolumesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusVolumesInUse.setStatus("current")
_EqlStorageGroupStatusSnapshotsOnline_Type = Integer32
_EqlStorageGroupStatusSnapshotsOnline_Object = MibTableColumn
eqlStorageGroupStatusSnapshotsOnline = _EqlStorageGroupStatusSnapshotsOnline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 9),
    _EqlStorageGroupStatusSnapshotsOnline_Type()
)
eqlStorageGroupStatusSnapshotsOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusSnapshotsOnline.setStatus("current")
_EqlStorageGroupStatusVolumesOnline_Type = Integer32
_EqlStorageGroupStatusVolumesOnline_Object = MibTableColumn
eqlStorageGroupStatusVolumesOnline = _EqlStorageGroupStatusVolumesOnline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 10),
    _EqlStorageGroupStatusVolumesOnline_Type()
)
eqlStorageGroupStatusVolumesOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusVolumesOnline.setStatus("current")
_EqlStorageGroupStatusSnapshotCount_Type = Integer32
_EqlStorageGroupStatusSnapshotCount_Object = MibTableColumn
eqlStorageGroupStatusSnapshotCount = _EqlStorageGroupStatusSnapshotCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 11),
    _EqlStorageGroupStatusSnapshotCount_Type()
)
eqlStorageGroupStatusSnapshotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusSnapshotCount.setStatus("current")
_EqlStorageGroupStatusVolumeCount_Type = Integer32
_EqlStorageGroupStatusVolumeCount_Object = MibTableColumn
eqlStorageGroupStatusVolumeCount = _EqlStorageGroupStatusVolumeCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 12),
    _EqlStorageGroupStatusVolumeCount_Type()
)
eqlStorageGroupStatusVolumeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusVolumeCount.setStatus("current")
_EqlStorageGroupStatusMemberCount_Type = Integer32
_EqlStorageGroupStatusMemberCount_Object = MibTableColumn
eqlStorageGroupStatusMemberCount = _EqlStorageGroupStatusMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 13),
    _EqlStorageGroupStatusMemberCount_Type()
)
eqlStorageGroupStatusMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusMemberCount.setStatus("current")
_EqlStorageGroupStatusMembersInUse_Type = Integer32
_EqlStorageGroupStatusMembersInUse_Object = MibTableColumn
eqlStorageGroupStatusMembersInUse = _EqlStorageGroupStatusMembersInUse_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 14),
    _EqlStorageGroupStatusMembersInUse_Type()
)
eqlStorageGroupStatusMembersInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusMembersInUse.setStatus("current")
_EqlStorageGroupStatusFreeSpace_Type = Integer32
_EqlStorageGroupStatusFreeSpace_Object = MibTableColumn
eqlStorageGroupStatusFreeSpace = _EqlStorageGroupStatusFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 15),
    _EqlStorageGroupStatusFreeSpace_Type()
)
eqlStorageGroupStatusFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusFreeSpace.setUnits("MB")
_EqlStorageGroupStatusPoolSpaceDelegated_Type = Integer32
_EqlStorageGroupStatusPoolSpaceDelegated_Object = MibTableColumn
eqlStorageGroupStatusPoolSpaceDelegated = _EqlStorageGroupStatusPoolSpaceDelegated_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 16),
    _EqlStorageGroupStatusPoolSpaceDelegated_Type()
)
eqlStorageGroupStatusPoolSpaceDelegated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusPoolSpaceDelegated.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusPoolSpaceDelegated.setUnits("MB")
_EqlStorageGroupStatusDelegatedUsedSpace_Type = Integer32
_EqlStorageGroupStatusDelegatedUsedSpace_Object = MibTableColumn
eqlStorageGroupStatusDelegatedUsedSpace = _EqlStorageGroupStatusDelegatedUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 17),
    _EqlStorageGroupStatusDelegatedUsedSpace_Type()
)
eqlStorageGroupStatusDelegatedUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusDelegatedUsedSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusDelegatedUsedSpace.setUnits("MB")
_EqlStorageGroupStatusReplReserveSpace_Type = Unsigned32
_EqlStorageGroupStatusReplReserveSpace_Object = MibTableColumn
eqlStorageGroupStatusReplReserveSpace = _EqlStorageGroupStatusReplReserveSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 18),
    _EqlStorageGroupStatusReplReserveSpace_Type()
)
eqlStorageGroupStatusReplReserveSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusReplReserveSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusReplReserveSpace.setUnits("MB")
_EqlStorageGroupStatusReplReserveInUse_Type = Unsigned32
_EqlStorageGroupStatusReplReserveInUse_Object = MibTableColumn
eqlStorageGroupStatusReplReserveInUse = _EqlStorageGroupStatusReplReserveInUse_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 19),
    _EqlStorageGroupStatusReplReserveInUse_Type()
)
eqlStorageGroupStatusReplReserveInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusReplReserveInUse.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusReplReserveInUse.setUnits("MB")
_EqlStorageGroupStatusVolumeSpaceSubscribed_Type = Unsigned32
_EqlStorageGroupStatusVolumeSpaceSubscribed_Object = MibTableColumn
eqlStorageGroupStatusVolumeSpaceSubscribed = _EqlStorageGroupStatusVolumeSpaceSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 20),
    _EqlStorageGroupStatusVolumeSpaceSubscribed_Type()
)
eqlStorageGroupStatusVolumeSpaceSubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusVolumeSpaceSubscribed.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusVolumeSpaceSubscribed.setUnits("MB")
_EqlStorageGroupStatusVolumeSpaceAllocated_Type = Unsigned32
_EqlStorageGroupStatusVolumeSpaceAllocated_Object = MibTableColumn
eqlStorageGroupStatusVolumeSpaceAllocated = _EqlStorageGroupStatusVolumeSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 21),
    _EqlStorageGroupStatusVolumeSpaceAllocated_Type()
)
eqlStorageGroupStatusVolumeSpaceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusVolumeSpaceAllocated.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusVolumeSpaceAllocated.setUnits("MB")
_EqlStorageGroupStatusFailbackSpace_Type = Unsigned32
_EqlStorageGroupStatusFailbackSpace_Object = MibTableColumn
eqlStorageGroupStatusFailbackSpace = _EqlStorageGroupStatusFailbackSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 22),
    _EqlStorageGroupStatusFailbackSpace_Type()
)
eqlStorageGroupStatusFailbackSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusFailbackSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusFailbackSpace.setUnits("MB")
_EqlStorageGroupStatusThinProvFreeSpace_Type = Integer32
_EqlStorageGroupStatusThinProvFreeSpace_Object = MibTableColumn
eqlStorageGroupStatusThinProvFreeSpace = _EqlStorageGroupStatusThinProvFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 23),
    _EqlStorageGroupStatusThinProvFreeSpace_Type()
)
eqlStorageGroupStatusThinProvFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusThinProvFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusThinProvFreeSpace.setUnits("MB")
_EqlStorageGroupStatusConnectionCount_Type = Integer32
_EqlStorageGroupStatusConnectionCount_Object = MibTableColumn
eqlStorageGroupStatusConnectionCount = _EqlStorageGroupStatusConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 24),
    _EqlStorageGroupStatusConnectionCount_Type()
)
eqlStorageGroupStatusConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusConnectionCount.setStatus("current")
_EqlStorageGroupStatusSnapReserveSpaceFree_Type = Unsigned32
_EqlStorageGroupStatusSnapReserveSpaceFree_Object = MibTableColumn
eqlStorageGroupStatusSnapReserveSpaceFree = _EqlStorageGroupStatusSnapReserveSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 25),
    _EqlStorageGroupStatusSnapReserveSpaceFree_Type()
)
eqlStorageGroupStatusSnapReserveSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusSnapReserveSpaceFree.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusSnapReserveSpaceFree.setUnits("MB")
_EqlStorageGroupStatusReplReserveSpaceFree_Type = Unsigned32
_EqlStorageGroupStatusReplReserveSpaceFree_Object = MibTableColumn
eqlStorageGroupStatusReplReserveSpaceFree = _EqlStorageGroupStatusReplReserveSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 26),
    _EqlStorageGroupStatusReplReserveSpaceFree_Type()
)
eqlStorageGroupStatusReplReserveSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusReplReserveSpaceFree.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusReplReserveSpaceFree.setUnits("MB")


class _EqlStorageGroupStatusGroupId_Type(OctetString):
    """Custom type eqlStorageGroupStatusGroupId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlStorageGroupStatusGroupId_Type.__name__ = "OctetString"
_EqlStorageGroupStatusGroupId_Object = MibTableColumn
eqlStorageGroupStatusGroupId = _EqlStorageGroupStatusGroupId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 27),
    _EqlStorageGroupStatusGroupId_Type()
)
eqlStorageGroupStatusGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusGroupId.setStatus("current")
_EqlStorageGroupStatusVirtualVolumeCount_Type = Unsigned32
_EqlStorageGroupStatusVirtualVolumeCount_Object = MibTableColumn
eqlStorageGroupStatusVirtualVolumeCount = _EqlStorageGroupStatusVirtualVolumeCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 28),
    _EqlStorageGroupStatusVirtualVolumeCount_Type()
)
eqlStorageGroupStatusVirtualVolumeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusVirtualVolumeCount.setStatus("current")
_EqlStorageGroupStatusVirtualVolumesOnline_Type = Unsigned32
_EqlStorageGroupStatusVirtualVolumesOnline_Object = MibTableColumn
eqlStorageGroupStatusVirtualVolumesOnline = _EqlStorageGroupStatusVirtualVolumesOnline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 29),
    _EqlStorageGroupStatusVirtualVolumesOnline_Type()
)
eqlStorageGroupStatusVirtualVolumesOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusVirtualVolumesOnline.setStatus("current")
_EqlStorageGroupStatusVirtualVolumesInUse_Type = Unsigned32
_EqlStorageGroupStatusVirtualVolumesInUse_Object = MibTableColumn
eqlStorageGroupStatusVirtualVolumesInUse = _EqlStorageGroupStatusVirtualVolumesInUse_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 30),
    _EqlStorageGroupStatusVirtualVolumesInUse_Type()
)
eqlStorageGroupStatusVirtualVolumesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusVirtualVolumesInUse.setStatus("current")
_EqlStorageGroupStatusVirtualVolumeSpaceSubscribed_Type = Unsigned32
_EqlStorageGroupStatusVirtualVolumeSpaceSubscribed_Object = MibTableColumn
eqlStorageGroupStatusVirtualVolumeSpaceSubscribed = _EqlStorageGroupStatusVirtualVolumeSpaceSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 31),
    _EqlStorageGroupStatusVirtualVolumeSpaceSubscribed_Type()
)
eqlStorageGroupStatusVirtualVolumeSpaceSubscribed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusVirtualVolumeSpaceSubscribed.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusVirtualVolumeSpaceSubscribed.setUnits("MB")
_EqlStorageGroupStatsTotalSpaceBorrowing_Type = Unsigned32
_EqlStorageGroupStatsTotalSpaceBorrowing_Object = MibTableColumn
eqlStorageGroupStatsTotalSpaceBorrowing = _EqlStorageGroupStatsTotalSpaceBorrowing_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 32),
    _EqlStorageGroupStatsTotalSpaceBorrowing_Type()
)
eqlStorageGroupStatsTotalSpaceBorrowing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatsTotalSpaceBorrowing.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatsTotalSpaceBorrowing.setUnits("MB")
_EqlStorageGroupStatusStorageContainerCount_Type = Integer32
_EqlStorageGroupStatusStorageContainerCount_Object = MibTableColumn
eqlStorageGroupStatusStorageContainerCount = _EqlStorageGroupStatusStorageContainerCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 34),
    _EqlStorageGroupStatusStorageContainerCount_Type()
)
eqlStorageGroupStatusStorageContainerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusStorageContainerCount.setStatus("current")
_EqlStorageGroupStatusStorageContainerVolumeCount_Type = Unsigned32
_EqlStorageGroupStatusStorageContainerVolumeCount_Object = MibTableColumn
eqlStorageGroupStatusStorageContainerVolumeCount = _EqlStorageGroupStatusStorageContainerVolumeCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 35),
    _EqlStorageGroupStatusStorageContainerVolumeCount_Type()
)
eqlStorageGroupStatusStorageContainerVolumeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusStorageContainerVolumeCount.setStatus("current")
_EqlStorageGroupStatusStorageContainerSnapCount_Type = Unsigned32
_EqlStorageGroupStatusStorageContainerSnapCount_Object = MibTableColumn
eqlStorageGroupStatusStorageContainerSnapCount = _EqlStorageGroupStatusStorageContainerSnapCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 36),
    _EqlStorageGroupStatusStorageContainerSnapCount_Type()
)
eqlStorageGroupStatusStorageContainerSnapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusStorageContainerSnapCount.setStatus("current")
_EqlStorageGroupStatusStorageContainerVolumesOnline_Type = Integer32
_EqlStorageGroupStatusStorageContainerVolumesOnline_Object = MibTableColumn
eqlStorageGroupStatusStorageContainerVolumesOnline = _EqlStorageGroupStatusStorageContainerVolumesOnline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 37),
    _EqlStorageGroupStatusStorageContainerVolumesOnline_Type()
)
eqlStorageGroupStatusStorageContainerVolumesOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusStorageContainerVolumesOnline.setStatus("current")
_EqlStorageGroupStatusStorageContainerSpaceReserved_Type = Counter64
_EqlStorageGroupStatusStorageContainerSpaceReserved_Object = MibTableColumn
eqlStorageGroupStatusStorageContainerSpaceReserved = _EqlStorageGroupStatusStorageContainerSpaceReserved_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 38),
    _EqlStorageGroupStatusStorageContainerSpaceReserved_Type()
)
eqlStorageGroupStatusStorageContainerSpaceReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusStorageContainerSpaceReserved.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusStorageContainerSpaceReserved.setUnits("MB")
_EqlStorageGroupStatusCompressedSpaceUsed_Type = Counter64
_EqlStorageGroupStatusCompressedSpaceUsed_Object = MibTableColumn
eqlStorageGroupStatusCompressedSpaceUsed = _EqlStorageGroupStatusCompressedSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 39),
    _EqlStorageGroupStatusCompressedSpaceUsed_Type()
)
eqlStorageGroupStatusCompressedSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusCompressedSpaceUsed.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusCompressedSpaceUsed.setUnits("MB")
_EqlStorageGroupStatusVirtualSpaceSize_Type = Counter64
_EqlStorageGroupStatusVirtualSpaceSize_Object = MibTableColumn
eqlStorageGroupStatusVirtualSpaceSize = _EqlStorageGroupStatusVirtualSpaceSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 40),
    _EqlStorageGroupStatusVirtualSpaceSize_Type()
)
eqlStorageGroupStatusVirtualSpaceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusVirtualSpaceSize.setStatus("current")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusVirtualSpaceSize.setUnits("MB")
_EqlStorageGroupStatusReplicationSnapCount_Type = Unsigned32
_EqlStorageGroupStatusReplicationSnapCount_Object = MibTableColumn
eqlStorageGroupStatusReplicationSnapCount = _EqlStorageGroupStatusReplicationSnapCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 41),
    _EqlStorageGroupStatusReplicationSnapCount_Type()
)
eqlStorageGroupStatusReplicationSnapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusReplicationSnapCount.setStatus("current")
_EqlStorageGroupStatusStorageContainerVolumesBound_Type = Integer32
_EqlStorageGroupStatusStorageContainerVolumesBound_Object = MibTableColumn
eqlStorageGroupStatusStorageContainerVolumesBound = _EqlStorageGroupStatusStorageContainerVolumesBound_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 2, 1, 42),
    _EqlStorageGroupStatusStorageContainerVolumesBound_Type()
)
eqlStorageGroupStatusStorageContainerVolumesBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupStatusStorageContainerVolumesBound.setStatus("current")
_EqlStorageGroupSiteTable_Object = MibTable
eqlStorageGroupSiteTable = _EqlStorageGroupSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eqlStorageGroupSiteTable.setStatus("current")
_EqlStorageGroupSiteEntry_Object = MibTableRow
eqlStorageGroupSiteEntry = _EqlStorageGroupSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 3, 1)
)
eqlStorageGroupSiteEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlGroupSiteIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupSiteEntry.setStatus("current")
_EqlGroupSiteIndex_Type = Integer32
_EqlGroupSiteIndex_Object = MibTableColumn
eqlGroupSiteIndex = _EqlGroupSiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 3, 1, 1),
    _EqlGroupSiteIndex_Type()
)
eqlGroupSiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlGroupSiteIndex.setStatus("current")


class _EqlGroupSiteName_Type(UTFString):
    """Custom type eqlGroupSiteName based on UTFString"""
    defaultValue = OctetString("default")

    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlGroupSiteName_Type.__name__ = "UTFString"
_EqlGroupSiteName_Object = MibTableColumn
eqlGroupSiteName = _EqlGroupSiteName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 3, 1, 2),
    _EqlGroupSiteName_Type()
)
eqlGroupSiteName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSiteName.setStatus("current")


class _EqlGroupSiteDescription_Type(UTFString):
    """Custom type eqlGroupSiteDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlGroupSiteDescription_Type.__name__ = "UTFString"
_EqlGroupSiteDescription_Object = MibTableColumn
eqlGroupSiteDescription = _EqlGroupSiteDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 3, 1, 3),
    _EqlGroupSiteDescription_Type()
)
eqlGroupSiteDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSiteDescription.setStatus("current")


class _EqlGroupSiteContactEmail_Type(DisplayString):
    """Custom type eqlGroupSiteContactEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlGroupSiteContactEmail_Type.__name__ = "DisplayString"
_EqlGroupSiteContactEmail_Object = MibTableColumn
eqlGroupSiteContactEmail = _EqlGroupSiteContactEmail_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 3, 1, 4),
    _EqlGroupSiteContactEmail_Type()
)
eqlGroupSiteContactEmail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSiteContactEmail.setStatus("current")


class _EqlGroupSiteContactPhone_Type(DisplayString):
    """Custom type eqlGroupSiteContactPhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlGroupSiteContactPhone_Type.__name__ = "DisplayString"
_EqlGroupSiteContactPhone_Object = MibTableColumn
eqlGroupSiteContactPhone = _EqlGroupSiteContactPhone_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 3, 1, 5),
    _EqlGroupSiteContactPhone_Type()
)
eqlGroupSiteContactPhone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSiteContactPhone.setStatus("current")


class _EqlGroupSiteContactMobile_Type(DisplayString):
    """Custom type eqlGroupSiteContactMobile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlGroupSiteContactMobile_Type.__name__ = "DisplayString"
_EqlGroupSiteContactMobile_Object = MibTableColumn
eqlGroupSiteContactMobile = _EqlGroupSiteContactMobile_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 3, 1, 6),
    _EqlGroupSiteContactMobile_Type()
)
eqlGroupSiteContactMobile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSiteContactMobile.setStatus("current")
_EqlGroupSiteRowStatus_Type = RowStatus
_EqlGroupSiteRowStatus_Object = MibTableColumn
eqlGroupSiteRowStatus = _EqlGroupSiteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 3, 1, 7),
    _EqlGroupSiteRowStatus_Type()
)
eqlGroupSiteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSiteRowStatus.setStatus("current")
_EqlStorageGroupDnsServerTable_Object = MibTable
eqlStorageGroupDnsServerTable = _EqlStorageGroupDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 4)
)
if mibBuilder.loadTexts:
    eqlStorageGroupDnsServerTable.setStatus("current")
_EqlStorageGroupDnsServerEntry_Object = MibTableRow
eqlStorageGroupDnsServerEntry = _EqlStorageGroupDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 4, 1)
)
eqlStorageGroupDnsServerEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlGroupDnsServerIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupDnsServerEntry.setStatus("current")
_EqlGroupDnsServerIndex_Type = Integer32
_EqlGroupDnsServerIndex_Object = MibTableColumn
eqlGroupDnsServerIndex = _EqlGroupDnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 4, 1, 1),
    _EqlGroupDnsServerIndex_Type()
)
eqlGroupDnsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlGroupDnsServerIndex.setStatus("current")
_EqlGroupDnsServerIpAddress_Type = IpAddress
_EqlGroupDnsServerIpAddress_Object = MibTableColumn
eqlGroupDnsServerIpAddress = _EqlGroupDnsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 4, 1, 2),
    _EqlGroupDnsServerIpAddress_Type()
)
eqlGroupDnsServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupDnsServerIpAddress.setStatus("current")
_EqlGroupDnsServerRowStatus_Type = RowStatus
_EqlGroupDnsServerRowStatus_Object = MibTableColumn
eqlGroupDnsServerRowStatus = _EqlGroupDnsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 4, 1, 3),
    _EqlGroupDnsServerRowStatus_Type()
)
eqlGroupDnsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupDnsServerRowStatus.setStatus("current")


class _EqlGroupDnsServerInetAddressType_Type(InetAddressType):
    """Custom type eqlGroupDnsServerInetAddressType based on InetAddressType"""


_EqlGroupDnsServerInetAddressType_Object = MibTableColumn
eqlGroupDnsServerInetAddressType = _EqlGroupDnsServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 4, 1, 4),
    _EqlGroupDnsServerInetAddressType_Type()
)
eqlGroupDnsServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupDnsServerInetAddressType.setStatus("current")
_EqlGroupDnsServerInetAddress_Type = InetAddress
_EqlGroupDnsServerInetAddress_Object = MibTableColumn
eqlGroupDnsServerInetAddress = _EqlGroupDnsServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 4, 1, 5),
    _EqlGroupDnsServerInetAddress_Type()
)
eqlGroupDnsServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupDnsServerInetAddress.setStatus("current")


class _EqlGroupDnsServerConfigState_Type(Integer32):
    """Custom type eqlGroupDnsServerConfigState based on Integer32"""
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
        *(("endConfig", 2),
          ("inProgress", 1),
          ("startConfig", 0))
    )


_EqlGroupDnsServerConfigState_Type.__name__ = "Integer32"
_EqlGroupDnsServerConfigState_Object = MibTableColumn
eqlGroupDnsServerConfigState = _EqlGroupDnsServerConfigState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 4, 1, 6),
    _EqlGroupDnsServerConfigState_Type()
)
eqlGroupDnsServerConfigState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupDnsServerConfigState.setStatus("current")
_EqlStorageGroupNtpServerTable_Object = MibTable
eqlStorageGroupNtpServerTable = _EqlStorageGroupNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 5)
)
if mibBuilder.loadTexts:
    eqlStorageGroupNtpServerTable.setStatus("current")
_EqlStorageGroupNtpServerEntry_Object = MibTableRow
eqlStorageGroupNtpServerEntry = _EqlStorageGroupNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 5, 1)
)
eqlStorageGroupNtpServerEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlGroupNtpServerIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupNtpServerEntry.setStatus("current")
_EqlGroupNtpServerIndex_Type = Integer32
_EqlGroupNtpServerIndex_Object = MibTableColumn
eqlGroupNtpServerIndex = _EqlGroupNtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 5, 1, 1),
    _EqlGroupNtpServerIndex_Type()
)
eqlGroupNtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlGroupNtpServerIndex.setStatus("current")
_EqlGroupNtpServerIpAddress_Type = IpAddress
_EqlGroupNtpServerIpAddress_Object = MibTableColumn
eqlGroupNtpServerIpAddress = _EqlGroupNtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 5, 1, 2),
    _EqlGroupNtpServerIpAddress_Type()
)
eqlGroupNtpServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupNtpServerIpAddress.setStatus("current")
_EqlGroupNtpServerRowStatus_Type = RowStatus
_EqlGroupNtpServerRowStatus_Object = MibTableColumn
eqlGroupNtpServerRowStatus = _EqlGroupNtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 5, 1, 3),
    _EqlGroupNtpServerRowStatus_Type()
)
eqlGroupNtpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupNtpServerRowStatus.setStatus("current")


class _EqlGroupNtpServerPort_Type(Integer32):
    """Custom type eqlGroupNtpServerPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EqlGroupNtpServerPort_Type.__name__ = "Integer32"
_EqlGroupNtpServerPort_Object = MibTableColumn
eqlGroupNtpServerPort = _EqlGroupNtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 5, 1, 4),
    _EqlGroupNtpServerPort_Type()
)
eqlGroupNtpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupNtpServerPort.setStatus("current")
_EqlGroupNtpServerInetAddressType_Type = InetAddressType
_EqlGroupNtpServerInetAddressType_Object = MibTableColumn
eqlGroupNtpServerInetAddressType = _EqlGroupNtpServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 5, 1, 5),
    _EqlGroupNtpServerInetAddressType_Type()
)
eqlGroupNtpServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupNtpServerInetAddressType.setStatus("current")
_EqlGroupNtpServerInetAddress_Type = InetAddress
_EqlGroupNtpServerInetAddress_Object = MibTableColumn
eqlGroupNtpServerInetAddress = _EqlGroupNtpServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 5, 1, 6),
    _EqlGroupNtpServerInetAddress_Type()
)
eqlGroupNtpServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupNtpServerInetAddress.setStatus("current")
_EqlStorageGroupChapServerTable_Object = MibTable
eqlStorageGroupChapServerTable = _EqlStorageGroupChapServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 6)
)
if mibBuilder.loadTexts:
    eqlStorageGroupChapServerTable.setStatus("current")
_EqlStorageGroupChapServerEntry_Object = MibTableRow
eqlStorageGroupChapServerEntry = _EqlStorageGroupChapServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 6, 1)
)
eqlStorageGroupChapServerEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlGroupChapServerIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupChapServerEntry.setStatus("current")
_EqlGroupChapServerIndex_Type = Integer32
_EqlGroupChapServerIndex_Object = MibTableColumn
eqlGroupChapServerIndex = _EqlGroupChapServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 6, 1, 1),
    _EqlGroupChapServerIndex_Type()
)
eqlGroupChapServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlGroupChapServerIndex.setStatus("current")
_EqlGroupChapServerIpAddress_Type = IpAddress
_EqlGroupChapServerIpAddress_Object = MibTableColumn
eqlGroupChapServerIpAddress = _EqlGroupChapServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 6, 1, 2),
    _EqlGroupChapServerIpAddress_Type()
)
eqlGroupChapServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupChapServerIpAddress.setStatus("current")
_EqlGroupChapServerRowStatus_Type = RowStatus
_EqlGroupChapServerRowStatus_Object = MibTableColumn
eqlGroupChapServerRowStatus = _EqlGroupChapServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 6, 1, 3),
    _EqlGroupChapServerRowStatus_Type()
)
eqlGroupChapServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupChapServerRowStatus.setStatus("current")


class _EqlGroupChapServerPort_Type(Integer32):
    """Custom type eqlGroupChapServerPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EqlGroupChapServerPort_Type.__name__ = "Integer32"
_EqlGroupChapServerPort_Object = MibTableColumn
eqlGroupChapServerPort = _EqlGroupChapServerPort_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 6, 1, 4),
    _EqlGroupChapServerPort_Type()
)
eqlGroupChapServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupChapServerPort.setStatus("current")


class _EqlGroupChapServerRADIUSSecret_Type(OctetString):
    """Custom type eqlGroupChapServerRADIUSSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlGroupChapServerRADIUSSecret_Type.__name__ = "OctetString"
_EqlGroupChapServerRADIUSSecret_Object = MibTableColumn
eqlGroupChapServerRADIUSSecret = _EqlGroupChapServerRADIUSSecret_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 6, 1, 5),
    _EqlGroupChapServerRADIUSSecret_Type()
)
eqlGroupChapServerRADIUSSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupChapServerRADIUSSecret.setStatus("current")
_EqlGroupChapServerInetAddressType_Type = InetAddressType
_EqlGroupChapServerInetAddressType_Object = MibTableColumn
eqlGroupChapServerInetAddressType = _EqlGroupChapServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 6, 1, 6),
    _EqlGroupChapServerInetAddressType_Type()
)
eqlGroupChapServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupChapServerInetAddressType.setStatus("current")
_EqlGroupChapServerInetAddress_Type = InetAddress
_EqlGroupChapServerInetAddress_Object = MibTableColumn
eqlGroupChapServerInetAddress = _EqlGroupChapServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 6, 1, 7),
    _EqlGroupChapServerInetAddress_Type()
)
eqlGroupChapServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupChapServerInetAddress.setStatus("current")
_EqlStorageGroupSMTPServerTable_Object = MibTable
eqlStorageGroupSMTPServerTable = _EqlStorageGroupSMTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 7)
)
if mibBuilder.loadTexts:
    eqlStorageGroupSMTPServerTable.setStatus("current")
_EqlStorageGroupSMTPServerEntry_Object = MibTableRow
eqlStorageGroupSMTPServerEntry = _EqlStorageGroupSMTPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 7, 1)
)
eqlStorageGroupSMTPServerEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlGroupSMTPServerIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupSMTPServerEntry.setStatus("current")
_EqlGroupSMTPServerIndex_Type = Integer32
_EqlGroupSMTPServerIndex_Object = MibTableColumn
eqlGroupSMTPServerIndex = _EqlGroupSMTPServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 7, 1, 1),
    _EqlGroupSMTPServerIndex_Type()
)
eqlGroupSMTPServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlGroupSMTPServerIndex.setStatus("current")
_EqlGroupSMTPServerIpAddress_Type = IpAddress
_EqlGroupSMTPServerIpAddress_Object = MibTableColumn
eqlGroupSMTPServerIpAddress = _EqlGroupSMTPServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 7, 1, 2),
    _EqlGroupSMTPServerIpAddress_Type()
)
eqlGroupSMTPServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSMTPServerIpAddress.setStatus("current")
_EqlGroupSMTPServerRowStatus_Type = RowStatus
_EqlGroupSMTPServerRowStatus_Object = MibTableColumn
eqlGroupSMTPServerRowStatus = _EqlGroupSMTPServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 7, 1, 3),
    _EqlGroupSMTPServerRowStatus_Type()
)
eqlGroupSMTPServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSMTPServerRowStatus.setStatus("current")


class _EqlGroupSMTPServerPort_Type(Integer32):
    """Custom type eqlGroupSMTPServerPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EqlGroupSMTPServerPort_Type.__name__ = "Integer32"
_EqlGroupSMTPServerPort_Object = MibTableColumn
eqlGroupSMTPServerPort = _EqlGroupSMTPServerPort_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 7, 1, 4),
    _EqlGroupSMTPServerPort_Type()
)
eqlGroupSMTPServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSMTPServerPort.setStatus("current")
_EqlGroupSMTPServerInetAddressType_Type = InetAddressType
_EqlGroupSMTPServerInetAddressType_Object = MibTableColumn
eqlGroupSMTPServerInetAddressType = _EqlGroupSMTPServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 7, 1, 5),
    _EqlGroupSMTPServerInetAddressType_Type()
)
eqlGroupSMTPServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSMTPServerInetAddressType.setStatus("current")
_EqlGroupSMTPServerInetAddress_Type = InetAddress
_EqlGroupSMTPServerInetAddress_Object = MibTableColumn
eqlGroupSMTPServerInetAddress = _EqlGroupSMTPServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 7, 1, 6),
    _EqlGroupSMTPServerInetAddress_Type()
)
eqlGroupSMTPServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSMTPServerInetAddress.setStatus("current")
_EqlStorageGroupSysLogServerTable_Object = MibTable
eqlStorageGroupSysLogServerTable = _EqlStorageGroupSysLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 8)
)
if mibBuilder.loadTexts:
    eqlStorageGroupSysLogServerTable.setStatus("current")
_EqlStorageGroupSysLogServerEntry_Object = MibTableRow
eqlStorageGroupSysLogServerEntry = _EqlStorageGroupSysLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 8, 1)
)
eqlStorageGroupSysLogServerEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlGroupSysLogServerIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupSysLogServerEntry.setStatus("current")
_EqlGroupSysLogServerIndex_Type = Integer32
_EqlGroupSysLogServerIndex_Object = MibTableColumn
eqlGroupSysLogServerIndex = _EqlGroupSysLogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 8, 1, 1),
    _EqlGroupSysLogServerIndex_Type()
)
eqlGroupSysLogServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlGroupSysLogServerIndex.setStatus("current")
_EqlGroupSysLogServerIpAddress_Type = IpAddress
_EqlGroupSysLogServerIpAddress_Object = MibTableColumn
eqlGroupSysLogServerIpAddress = _EqlGroupSysLogServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 8, 1, 2),
    _EqlGroupSysLogServerIpAddress_Type()
)
eqlGroupSysLogServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSysLogServerIpAddress.setStatus("current")
_EqlGroupSysLogServerRowStatus_Type = RowStatus
_EqlGroupSysLogServerRowStatus_Object = MibTableColumn
eqlGroupSysLogServerRowStatus = _EqlGroupSysLogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 8, 1, 3),
    _EqlGroupSysLogServerRowStatus_Type()
)
eqlGroupSysLogServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSysLogServerRowStatus.setStatus("current")
_EqlGroupSysLogServerInetAddressType_Type = InetAddressType
_EqlGroupSysLogServerInetAddressType_Object = MibTableColumn
eqlGroupSysLogServerInetAddressType = _EqlGroupSysLogServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 8, 1, 4),
    _EqlGroupSysLogServerInetAddressType_Type()
)
eqlGroupSysLogServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSysLogServerInetAddressType.setStatus("current")
_EqlGroupSysLogServerInetAddress_Type = InetAddress
_EqlGroupSysLogServerInetAddress_Object = MibTableColumn
eqlGroupSysLogServerInetAddress = _EqlGroupSysLogServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 8, 1, 5),
    _EqlGroupSysLogServerInetAddress_Type()
)
eqlGroupSysLogServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSysLogServerInetAddress.setStatus("current")
_EqlStorageGroupAlertEmailTable_Object = MibTable
eqlStorageGroupAlertEmailTable = _EqlStorageGroupAlertEmailTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 9)
)
if mibBuilder.loadTexts:
    eqlStorageGroupAlertEmailTable.setStatus("current")
_EqlStorageGroupAlertEmailEntry_Object = MibTableRow
eqlStorageGroupAlertEmailEntry = _EqlStorageGroupAlertEmailEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 9, 1)
)
eqlStorageGroupAlertEmailEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlGroupAlertEmailIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupAlertEmailEntry.setStatus("current")
_EqlGroupAlertEmailIndex_Type = Integer32
_EqlGroupAlertEmailIndex_Object = MibTableColumn
eqlGroupAlertEmailIndex = _EqlGroupAlertEmailIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 9, 1, 1),
    _EqlGroupAlertEmailIndex_Type()
)
eqlGroupAlertEmailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlGroupAlertEmailIndex.setStatus("current")


class _EqlGroupAlertEmailAddress_Type(DisplayString):
    """Custom type eqlGroupAlertEmailAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlGroupAlertEmailAddress_Type.__name__ = "DisplayString"
_EqlGroupAlertEmailAddress_Object = MibTableColumn
eqlGroupAlertEmailAddress = _EqlGroupAlertEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 9, 1, 2),
    _EqlGroupAlertEmailAddress_Type()
)
eqlGroupAlertEmailAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupAlertEmailAddress.setStatus("current")
_EqlGroupAlertEmailRowStatus_Type = RowStatus
_EqlGroupAlertEmailRowStatus_Object = MibTableColumn
eqlGroupAlertEmailRowStatus = _EqlGroupAlertEmailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 9, 1, 3),
    _EqlGroupAlertEmailRowStatus_Type()
)
eqlGroupAlertEmailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupAlertEmailRowStatus.setStatus("current")
_EqlStorageGroupAdminAccountTable_Object = MibTable
eqlStorageGroupAdminAccountTable = _EqlStorageGroupAdminAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10)
)
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountTable.setStatus("current")
_EqlStorageGroupAdminAccountEntry_Object = MibTableRow
eqlStorageGroupAdminAccountEntry = _EqlStorageGroupAdminAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1)
)
eqlStorageGroupAdminAccountEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountEntry.setStatus("current")
_EqlStorageGroupAdminAccountIndex_Type = Integer32
_EqlStorageGroupAdminAccountIndex_Object = MibTableColumn
eqlStorageGroupAdminAccountIndex = _EqlStorageGroupAdminAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 1),
    _EqlStorageGroupAdminAccountIndex_Type()
)
eqlStorageGroupAdminAccountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountIndex.setStatus("current")
_EqlStorageGroupAdminAccountRowStatus_Type = RowStatus
_EqlStorageGroupAdminAccountRowStatus_Object = MibTableColumn
eqlStorageGroupAdminAccountRowStatus = _EqlStorageGroupAdminAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 2),
    _EqlStorageGroupAdminAccountRowStatus_Type()
)
eqlStorageGroupAdminAccountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountRowStatus.setStatus("current")


class _EqlStorageGroupAdminAccountName_Type(DisplayString):
    """Custom type eqlStorageGroupAdminAccountName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlStorageGroupAdminAccountName_Type.__name__ = "DisplayString"
_EqlStorageGroupAdminAccountName_Object = MibTableColumn
eqlStorageGroupAdminAccountName = _EqlStorageGroupAdminAccountName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 3),
    _EqlStorageGroupAdminAccountName_Type()
)
eqlStorageGroupAdminAccountName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountName.setStatus("current")


class _EqlStorageGroupAdminAccountPassword_Type(OctetString):
    """Custom type eqlStorageGroupAdminAccountPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlStorageGroupAdminAccountPassword_Type.__name__ = "OctetString"
_EqlStorageGroupAdminAccountPassword_Object = MibTableColumn
eqlStorageGroupAdminAccountPassword = _EqlStorageGroupAdminAccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 4),
    _EqlStorageGroupAdminAccountPassword_Type()
)
eqlStorageGroupAdminAccountPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountPassword.setStatus("current")


class _EqlStorageGroupAdminAccountDescription_Type(UTFString):
    """Custom type eqlStorageGroupAdminAccountDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqlStorageGroupAdminAccountDescription_Type.__name__ = "UTFString"
_EqlStorageGroupAdminAccountDescription_Object = MibTableColumn
eqlStorageGroupAdminAccountDescription = _EqlStorageGroupAdminAccountDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 5),
    _EqlStorageGroupAdminAccountDescription_Type()
)
eqlStorageGroupAdminAccountDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountDescription.setStatus("current")


class _EqlStorageGroupAdminAccountType_Type(AdminAccountType):
    """Custom type eqlStorageGroupAdminAccountType based on AdminAccountType"""


_EqlStorageGroupAdminAccountType_Object = MibTableColumn
eqlStorageGroupAdminAccountType = _EqlStorageGroupAdminAccountType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 6),
    _EqlStorageGroupAdminAccountType_Type()
)
eqlStorageGroupAdminAccountType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountType.setStatus("current")


class _EqlStorageGroupAdminAccountContact_Type(DisplayString):
    """Custom type eqlStorageGroupAdminAccountContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlStorageGroupAdminAccountContact_Type.__name__ = "DisplayString"
_EqlStorageGroupAdminAccountContact_Object = MibTableColumn
eqlStorageGroupAdminAccountContact = _EqlStorageGroupAdminAccountContact_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 7),
    _EqlStorageGroupAdminAccountContact_Type()
)
eqlStorageGroupAdminAccountContact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountContact.setStatus("current")


class _EqlStorageGroupAdminAccountEmail_Type(DisplayString):
    """Custom type eqlStorageGroupAdminAccountEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlStorageGroupAdminAccountEmail_Type.__name__ = "DisplayString"
_EqlStorageGroupAdminAccountEmail_Object = MibTableColumn
eqlStorageGroupAdminAccountEmail = _EqlStorageGroupAdminAccountEmail_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 8),
    _EqlStorageGroupAdminAccountEmail_Type()
)
eqlStorageGroupAdminAccountEmail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountEmail.setStatus("current")


class _EqlStorageGroupAdminAccountPhone_Type(DisplayString):
    """Custom type eqlStorageGroupAdminAccountPhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlStorageGroupAdminAccountPhone_Type.__name__ = "DisplayString"
_EqlStorageGroupAdminAccountPhone_Object = MibTableColumn
eqlStorageGroupAdminAccountPhone = _EqlStorageGroupAdminAccountPhone_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 9),
    _EqlStorageGroupAdminAccountPhone_Type()
)
eqlStorageGroupAdminAccountPhone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountPhone.setStatus("current")


class _EqlStorageGroupAdminAccountMobile_Type(DisplayString):
    """Custom type eqlStorageGroupAdminAccountMobile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlStorageGroupAdminAccountMobile_Type.__name__ = "DisplayString"
_EqlStorageGroupAdminAccountMobile_Object = MibTableColumn
eqlStorageGroupAdminAccountMobile = _EqlStorageGroupAdminAccountMobile_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 10),
    _EqlStorageGroupAdminAccountMobile_Type()
)
eqlStorageGroupAdminAccountMobile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountMobile.setStatus("current")


class _EqlStorageGroupAdminAccountStatus_Type(Integer32):
    """Custom type eqlStorageGroupAdminAccountStatus based on Integer32"""
    defaultValue = 1

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


_EqlStorageGroupAdminAccountStatus_Type.__name__ = "Integer32"
_EqlStorageGroupAdminAccountStatus_Object = MibTableColumn
eqlStorageGroupAdminAccountStatus = _EqlStorageGroupAdminAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 11),
    _EqlStorageGroupAdminAccountStatus_Type()
)
eqlStorageGroupAdminAccountStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountStatus.setStatus("current")


class _EqlStorageGroupAdminAccountCliFlags_Type(Integer32):
    """Custom type eqlStorageGroupAdminAccountCliFlags based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EqlStorageGroupAdminAccountCliFlags_Type.__name__ = "Integer32"
_EqlStorageGroupAdminAccountCliFlags_Object = MibTableColumn
eqlStorageGroupAdminAccountCliFlags = _EqlStorageGroupAdminAccountCliFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 12),
    _EqlStorageGroupAdminAccountCliFlags_Type()
)
eqlStorageGroupAdminAccountCliFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountCliFlags.setStatus("current")


class _EqlStorageGroupAdminAccountGuiFlags_Type(Integer32):
    """Custom type eqlStorageGroupAdminAccountGuiFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EqlStorageGroupAdminAccountGuiFlags_Type.__name__ = "Integer32"
_EqlStorageGroupAdminAccountGuiFlags_Object = MibTableColumn
eqlStorageGroupAdminAccountGuiFlags = _EqlStorageGroupAdminAccountGuiFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 13),
    _EqlStorageGroupAdminAccountGuiFlags_Type()
)
eqlStorageGroupAdminAccountGuiFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountGuiFlags.setStatus("current")


class _EqlStorageGroupAdminAccountPollInterval_Type(Integer32):
    """Custom type eqlStorageGroupAdminAccountPollInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_EqlStorageGroupAdminAccountPollInterval_Type.__name__ = "Integer32"
_EqlStorageGroupAdminAccountPollInterval_Object = MibTableColumn
eqlStorageGroupAdminAccountPollInterval = _EqlStorageGroupAdminAccountPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 14),
    _EqlStorageGroupAdminAccountPollInterval_Type()
)
eqlStorageGroupAdminAccountPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountPollInterval.setStatus("current")


class _EqlStorageGroupAdminAccountAuthType_Type(Integer32):
    """Custom type eqlStorageGroupAdminAccountAuthType based on Integer32"""
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
        *(("ldap", 2),
          ("local", 0),
          ("radius", 1))
    )


_EqlStorageGroupAdminAccountAuthType_Type.__name__ = "Integer32"
_EqlStorageGroupAdminAccountAuthType_Object = MibTableColumn
eqlStorageGroupAdminAccountAuthType = _EqlStorageGroupAdminAccountAuthType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 15),
    _EqlStorageGroupAdminAccountAuthType_Type()
)
eqlStorageGroupAdminAccountAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountAuthType.setStatus("current")
_EqlStorageGroupAdminAccountRecentLogin_Type = Counter32
_EqlStorageGroupAdminAccountRecentLogin_Object = MibTableColumn
eqlStorageGroupAdminAccountRecentLogin = _EqlStorageGroupAdminAccountRecentLogin_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 16),
    _EqlStorageGroupAdminAccountRecentLogin_Type()
)
eqlStorageGroupAdminAccountRecentLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountRecentLogin.setStatus("current")


class _EqlStorageGroupAdminAccountClass_Type(DisplayString):
    """Custom type eqlStorageGroupAdminAccountClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlStorageGroupAdminAccountClass_Type.__name__ = "DisplayString"
_EqlStorageGroupAdminAccountClass_Object = MibTableColumn
eqlStorageGroupAdminAccountClass = _EqlStorageGroupAdminAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 17),
    _EqlStorageGroupAdminAccountClass_Type()
)
eqlStorageGroupAdminAccountClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountClass.setStatus("current")


class _EqlStorageGroupAdminAccountPrivilege_Type(AdminAccountPrivilegeType):
    """Custom type eqlStorageGroupAdminAccountPrivilege based on AdminAccountPrivilegeType"""


_EqlStorageGroupAdminAccountPrivilege_Object = MibTableColumn
eqlStorageGroupAdminAccountPrivilege = _EqlStorageGroupAdminAccountPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 18),
    _EqlStorageGroupAdminAccountPrivilege_Type()
)
eqlStorageGroupAdminAccountPrivilege.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountPrivilege.setStatus("current")


class _EqlStorageGroupAdminAccountSnmpKey_Type(OctetString):
    """Custom type eqlStorageGroupAdminAccountSnmpKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_EqlStorageGroupAdminAccountSnmpKey_Type.__name__ = "OctetString"
_EqlStorageGroupAdminAccountSnmpKey_Object = MibTableColumn
eqlStorageGroupAdminAccountSnmpKey = _EqlStorageGroupAdminAccountSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 19),
    _EqlStorageGroupAdminAccountSnmpKey_Type()
)
eqlStorageGroupAdminAccountSnmpKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountSnmpKey.setStatus("current")


class _EqlStorageGroupAdminAccountSnmpKey2_Type(OctetString):
    """Custom type eqlStorageGroupAdminAccountSnmpKey2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_EqlStorageGroupAdminAccountSnmpKey2_Type.__name__ = "OctetString"
_EqlStorageGroupAdminAccountSnmpKey2_Object = MibTableColumn
eqlStorageGroupAdminAccountSnmpKey2 = _EqlStorageGroupAdminAccountSnmpKey2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 20),
    _EqlStorageGroupAdminAccountSnmpKey2_Type()
)
eqlStorageGroupAdminAccountSnmpKey2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountSnmpKey2.setStatus("current")


class _EqlStorageGroupAdminAccountCHAPPassword_Type(OctetString):
    """Custom type eqlStorageGroupAdminAccountCHAPPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlStorageGroupAdminAccountCHAPPassword_Type.__name__ = "OctetString"
_EqlStorageGroupAdminAccountCHAPPassword_Object = MibTableColumn
eqlStorageGroupAdminAccountCHAPPassword = _EqlStorageGroupAdminAccountCHAPPassword_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 21),
    _EqlStorageGroupAdminAccountCHAPPassword_Type()
)
eqlStorageGroupAdminAccountCHAPPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountCHAPPassword.setStatus("current")
_EqlStorageGroupAdminAccountKey_Type = Unsigned32
_EqlStorageGroupAdminAccountKey_Object = MibTableColumn
eqlStorageGroupAdminAccountKey = _EqlStorageGroupAdminAccountKey_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 22),
    _EqlStorageGroupAdminAccountKey_Type()
)
eqlStorageGroupAdminAccountKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountKey.setStatus("current")


class _EqlStorageGroupAdminAccountAdGroupName_Type(DisplayString):
    """Custom type eqlStorageGroupAdminAccountAdGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_EqlStorageGroupAdminAccountAdGroupName_Type.__name__ = "DisplayString"
_EqlStorageGroupAdminAccountAdGroupName_Object = MibTableColumn
eqlStorageGroupAdminAccountAdGroupName = _EqlStorageGroupAdminAccountAdGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 23),
    _EqlStorageGroupAdminAccountAdGroupName_Type()
)
eqlStorageGroupAdminAccountAdGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountAdGroupName.setStatus("current")


class _EqlStorageGroupAdminAccountSNMPPrivProt_Type(Integer32):
    """Custom type eqlStorageGroupAdminAccountSNMPPrivProt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aes128", 1),
          ("des", 0))
    )


_EqlStorageGroupAdminAccountSNMPPrivProt_Type.__name__ = "Integer32"
_EqlStorageGroupAdminAccountSNMPPrivProt_Object = MibTableColumn
eqlStorageGroupAdminAccountSNMPPrivProt = _EqlStorageGroupAdminAccountSNMPPrivProt_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 10, 1, 24),
    _EqlStorageGroupAdminAccountSNMPPrivProt_Type()
)
eqlStorageGroupAdminAccountSNMPPrivProt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountSNMPPrivProt.setStatus("current")
_EqlStorageGroupiSNSServerTable_Object = MibTable
eqlStorageGroupiSNSServerTable = _EqlStorageGroupiSNSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 11)
)
if mibBuilder.loadTexts:
    eqlStorageGroupiSNSServerTable.setStatus("current")
_EqlStorageGroupiSNSServerEntry_Object = MibTableRow
eqlStorageGroupiSNSServerEntry = _EqlStorageGroupiSNSServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 11, 1)
)
eqlStorageGroupiSNSServerEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlGroupiSNSServerIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupiSNSServerEntry.setStatus("current")
_EqlGroupiSNSServerIndex_Type = Integer32
_EqlGroupiSNSServerIndex_Object = MibTableColumn
eqlGroupiSNSServerIndex = _EqlGroupiSNSServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 11, 1, 1),
    _EqlGroupiSNSServerIndex_Type()
)
eqlGroupiSNSServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlGroupiSNSServerIndex.setStatus("current")
_EqlGroupiSNSServerRowStatus_Type = RowStatus
_EqlGroupiSNSServerRowStatus_Object = MibTableColumn
eqlGroupiSNSServerRowStatus = _EqlGroupiSNSServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 11, 1, 2),
    _EqlGroupiSNSServerRowStatus_Type()
)
eqlGroupiSNSServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupiSNSServerRowStatus.setStatus("current")
_EqlGroupiSNSServerIpAddress_Type = IpAddress
_EqlGroupiSNSServerIpAddress_Object = MibTableColumn
eqlGroupiSNSServerIpAddress = _EqlGroupiSNSServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 11, 1, 3),
    _EqlGroupiSNSServerIpAddress_Type()
)
eqlGroupiSNSServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupiSNSServerIpAddress.setStatus("current")


class _EqlGroupiSNSServerPort_Type(Integer32):
    """Custom type eqlGroupiSNSServerPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EqlGroupiSNSServerPort_Type.__name__ = "Integer32"
_EqlGroupiSNSServerPort_Object = MibTableColumn
eqlGroupiSNSServerPort = _EqlGroupiSNSServerPort_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 11, 1, 4),
    _EqlGroupiSNSServerPort_Type()
)
eqlGroupiSNSServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlGroupiSNSServerPort.setStatus("current")
_EqlGroupiSNSServerInetAddressType_Type = InetAddressType
_EqlGroupiSNSServerInetAddressType_Object = MibTableColumn
eqlGroupiSNSServerInetAddressType = _EqlGroupiSNSServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 11, 1, 5),
    _EqlGroupiSNSServerInetAddressType_Type()
)
eqlGroupiSNSServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupiSNSServerInetAddressType.setStatus("current")
_EqlGroupiSNSServerInetAddress_Type = InetAddress
_EqlGroupiSNSServerInetAddress_Object = MibTableColumn
eqlGroupiSNSServerInetAddress = _EqlGroupiSNSServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 11, 1, 6),
    _EqlGroupiSNSServerInetAddress_Type()
)
eqlGroupiSNSServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupiSNSServerInetAddress.setStatus("current")
_EqlGroupCompatibilityTable_Object = MibTable
eqlGroupCompatibilityTable = _EqlGroupCompatibilityTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 12)
)
if mibBuilder.loadTexts:
    eqlGroupCompatibilityTable.setStatus("current")
_EqlGroupCompatibilityEntry_Object = MibTableRow
eqlGroupCompatibilityEntry = _EqlGroupCompatibilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    eqlGroupCompatibilityEntry.setStatus("current")
_EqlGroupCurrentCompLevel_Type = Unsigned32
_EqlGroupCurrentCompLevel_Object = MibTableColumn
eqlGroupCurrentCompLevel = _EqlGroupCurrentCompLevel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 12, 1, 1),
    _EqlGroupCurrentCompLevel_Type()
)
eqlGroupCurrentCompLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlGroupCurrentCompLevel.setStatus("current")
_EqlStorageGroupCollectionTable_Object = MibTable
eqlStorageGroupCollectionTable = _EqlStorageGroupCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 13)
)
if mibBuilder.loadTexts:
    eqlStorageGroupCollectionTable.setStatus("current")
_EqlStorageGroupCollectionEntry_Object = MibTableRow
eqlStorageGroupCollectionEntry = _EqlStorageGroupCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 13, 1)
)
eqlStorageGroupCollectionEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupCollectionEntry.setStatus("current")


class _EqlGrpNoofVolCollections_Type(Unsigned32):
    """Custom type eqlGrpNoofVolCollections based on Unsigned32"""
    defaultValue = 0


_EqlGrpNoofVolCollections_Object = MibTableColumn
eqlGrpNoofVolCollections = _EqlGrpNoofVolCollections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 13, 1, 1),
    _EqlGrpNoofVolCollections_Type()
)
eqlGrpNoofVolCollections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlGrpNoofVolCollections.setStatus("current")


class _EqlGrpNoofSnapCollections_Type(Unsigned32):
    """Custom type eqlGrpNoofSnapCollections based on Unsigned32"""
    defaultValue = 0


_EqlGrpNoofSnapCollections_Object = MibTableColumn
eqlGrpNoofSnapCollections = _EqlGrpNoofSnapCollections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 13, 1, 2),
    _EqlGrpNoofSnapCollections_Type()
)
eqlGrpNoofSnapCollections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlGrpNoofSnapCollections.setStatus("current")


class _EqlGrpNoofOrphanSnapCollections_Type(Unsigned32):
    """Custom type eqlGrpNoofOrphanSnapCollections based on Unsigned32"""
    defaultValue = 0


_EqlGrpNoofOrphanSnapCollections_Object = MibTableColumn
eqlGrpNoofOrphanSnapCollections = _EqlGrpNoofOrphanSnapCollections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 13, 1, 3),
    _EqlGrpNoofOrphanSnapCollections_Type()
)
eqlGrpNoofOrphanSnapCollections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlGrpNoofOrphanSnapCollections.setStatus("current")
_EqlRADIUSTable_Object = MibTable
eqlRADIUSTable = _EqlRADIUSTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 14)
)
if mibBuilder.loadTexts:
    eqlRADIUSTable.setStatus("current")
_EqlRADIUSEntry_Object = MibTableRow
eqlRADIUSEntry = _EqlRADIUSEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 14, 1)
)
eqlRADIUSEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
)
if mibBuilder.loadTexts:
    eqlRADIUSEntry.setStatus("current")


class _EqlRADIUSSecret_Type(OctetString):
    """Custom type eqlRADIUSSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlRADIUSSecret_Type.__name__ = "OctetString"
_EqlRADIUSSecret_Object = MibTableColumn
eqlRADIUSSecret = _EqlRADIUSSecret_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 14, 1, 1),
    _EqlRADIUSSecret_Type()
)
eqlRADIUSSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlRADIUSSecret.setStatus("current")


class _EqlRADIUSLoginAuthEnable_Type(TruthValue):
    """Custom type eqlRADIUSLoginAuthEnable based on TruthValue"""


_EqlRADIUSLoginAuthEnable_Object = MibTableColumn
eqlRADIUSLoginAuthEnable = _EqlRADIUSLoginAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 14, 1, 2),
    _EqlRADIUSLoginAuthEnable_Type()
)
eqlRADIUSLoginAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlRADIUSLoginAuthEnable.setStatus("current")


class _EqlRADIUSAuthRecvTimeout_Type(Unsigned32):
    """Custom type eqlRADIUSAuthRecvTimeout based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_EqlRADIUSAuthRecvTimeout_Type.__name__ = "Unsigned32"
_EqlRADIUSAuthRecvTimeout_Object = MibTableColumn
eqlRADIUSAuthRecvTimeout = _EqlRADIUSAuthRecvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 14, 1, 3),
    _EqlRADIUSAuthRecvTimeout_Type()
)
eqlRADIUSAuthRecvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlRADIUSAuthRecvTimeout.setStatus("current")


class _EqlRADIUSAuthMaxRetries_Type(Unsigned32):
    """Custom type eqlRADIUSAuthMaxRetries based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EqlRADIUSAuthMaxRetries_Type.__name__ = "Unsigned32"
_EqlRADIUSAuthMaxRetries_Object = MibTableColumn
eqlRADIUSAuthMaxRetries = _EqlRADIUSAuthMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 14, 1, 4),
    _EqlRADIUSAuthMaxRetries_Type()
)
eqlRADIUSAuthMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlRADIUSAuthMaxRetries.setStatus("current")


class _EqlRADIUSLoginAcctEnable_Type(TruthValue):
    """Custom type eqlRADIUSLoginAcctEnable based on TruthValue"""


_EqlRADIUSLoginAcctEnable_Object = MibTableColumn
eqlRADIUSLoginAcctEnable = _EqlRADIUSLoginAcctEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 14, 1, 5),
    _EqlRADIUSLoginAcctEnable_Type()
)
eqlRADIUSLoginAcctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlRADIUSLoginAcctEnable.setStatus("current")


class _EqlRADIUSAcctRecvTimeout_Type(Unsigned32):
    """Custom type eqlRADIUSAcctRecvTimeout based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_EqlRADIUSAcctRecvTimeout_Type.__name__ = "Unsigned32"
_EqlRADIUSAcctRecvTimeout_Object = MibTableColumn
eqlRADIUSAcctRecvTimeout = _EqlRADIUSAcctRecvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 14, 1, 6),
    _EqlRADIUSAcctRecvTimeout_Type()
)
eqlRADIUSAcctRecvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlRADIUSAcctRecvTimeout.setStatus("current")


class _EqlRADIUSAcctMaxRetries_Type(Unsigned32):
    """Custom type eqlRADIUSAcctMaxRetries based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EqlRADIUSAcctMaxRetries_Type.__name__ = "Unsigned32"
_EqlRADIUSAcctMaxRetries_Object = MibTableColumn
eqlRADIUSAcctMaxRetries = _EqlRADIUSAcctMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 14, 1, 7),
    _EqlRADIUSAcctMaxRetries_Type()
)
eqlRADIUSAcctMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlRADIUSAcctMaxRetries.setStatus("current")


class _EqlRADIUSiscsiAuthEnable_Type(TruthValue):
    """Custom type eqlRADIUSiscsiAuthEnable based on TruthValue"""


_EqlRADIUSiscsiAuthEnable_Object = MibTableColumn
eqlRADIUSiscsiAuthEnable = _EqlRADIUSiscsiAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 14, 1, 8),
    _EqlRADIUSiscsiAuthEnable_Type()
)
eqlRADIUSiscsiAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlRADIUSiscsiAuthEnable.setStatus("current")


class _EqlLocaliscsiAuthEnable_Type(TruthValue):
    """Custom type eqlLocaliscsiAuthEnable based on TruthValue"""


_EqlLocaliscsiAuthEnable_Object = MibTableColumn
eqlLocaliscsiAuthEnable = _EqlLocaliscsiAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 14, 1, 9),
    _EqlLocaliscsiAuthEnable_Type()
)
eqlLocaliscsiAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlLocaliscsiAuthEnable.setStatus("current")


class _EqlRADIUSRequireAdminAttrEnable_Type(TruthValue):
    """Custom type eqlRADIUSRequireAdminAttrEnable based on TruthValue"""


_EqlRADIUSRequireAdminAttrEnable_Object = MibTableColumn
eqlRADIUSRequireAdminAttrEnable = _EqlRADIUSRequireAdminAttrEnable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 14, 1, 10),
    _EqlRADIUSRequireAdminAttrEnable_Type()
)
eqlRADIUSRequireAdminAttrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlRADIUSRequireAdminAttrEnable.setStatus("current")
_EqlRADIUSAcctServerTable_Object = MibTable
eqlRADIUSAcctServerTable = _EqlRADIUSAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 15)
)
if mibBuilder.loadTexts:
    eqlRADIUSAcctServerTable.setStatus("current")
_EqlRADIUSAcctServerEntry_Object = MibTableRow
eqlRADIUSAcctServerEntry = _EqlRADIUSAcctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 15, 1)
)
eqlRADIUSAcctServerEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlRADIUSAcctServerIndex"),
)
if mibBuilder.loadTexts:
    eqlRADIUSAcctServerEntry.setStatus("current")
_EqlRADIUSAcctServerIndex_Type = Integer32
_EqlRADIUSAcctServerIndex_Object = MibTableColumn
eqlRADIUSAcctServerIndex = _EqlRADIUSAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 15, 1, 1),
    _EqlRADIUSAcctServerIndex_Type()
)
eqlRADIUSAcctServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlRADIUSAcctServerIndex.setStatus("current")
_EqlRADIUSAcctServerIpAddress_Type = IpAddress
_EqlRADIUSAcctServerIpAddress_Object = MibTableColumn
eqlRADIUSAcctServerIpAddress = _EqlRADIUSAcctServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 15, 1, 2),
    _EqlRADIUSAcctServerIpAddress_Type()
)
eqlRADIUSAcctServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlRADIUSAcctServerIpAddress.setStatus("current")


class _EqlRADIUSAcctServerPort_Type(Integer32):
    """Custom type eqlRADIUSAcctServerPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EqlRADIUSAcctServerPort_Type.__name__ = "Integer32"
_EqlRADIUSAcctServerPort_Object = MibTableColumn
eqlRADIUSAcctServerPort = _EqlRADIUSAcctServerPort_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 15, 1, 3),
    _EqlRADIUSAcctServerPort_Type()
)
eqlRADIUSAcctServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlRADIUSAcctServerPort.setStatus("current")
_EqlRADIUSAcctServerRowStatus_Type = RowStatus
_EqlRADIUSAcctServerRowStatus_Object = MibTableColumn
eqlRADIUSAcctServerRowStatus = _EqlRADIUSAcctServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 15, 1, 4),
    _EqlRADIUSAcctServerRowStatus_Type()
)
eqlRADIUSAcctServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlRADIUSAcctServerRowStatus.setStatus("current")


class _EqlRADIUSAcctServerSecret_Type(OctetString):
    """Custom type eqlRADIUSAcctServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlRADIUSAcctServerSecret_Type.__name__ = "OctetString"
_EqlRADIUSAcctServerSecret_Object = MibTableColumn
eqlRADIUSAcctServerSecret = _EqlRADIUSAcctServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 15, 1, 5),
    _EqlRADIUSAcctServerSecret_Type()
)
eqlRADIUSAcctServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlRADIUSAcctServerSecret.setStatus("current")
_EqlRADIUSAcctServerInetAddressType_Type = InetAddressType
_EqlRADIUSAcctServerInetAddressType_Object = MibTableColumn
eqlRADIUSAcctServerInetAddressType = _EqlRADIUSAcctServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 15, 1, 6),
    _EqlRADIUSAcctServerInetAddressType_Type()
)
eqlRADIUSAcctServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlRADIUSAcctServerInetAddressType.setStatus("current")
_EqlRADIUSAcctServerInetAddress_Type = InetAddress
_EqlRADIUSAcctServerInetAddress_Object = MibTableColumn
eqlRADIUSAcctServerInetAddress = _EqlRADIUSAcctServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 15, 1, 7),
    _EqlRADIUSAcctServerInetAddress_Type()
)
eqlRADIUSAcctServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlRADIUSAcctServerInetAddress.setStatus("current")
_EqlUserSessionTable_Object = MibTable
eqlUserSessionTable = _EqlUserSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 16)
)
if mibBuilder.loadTexts:
    eqlUserSessionTable.setStatus("current")
_EqlUserSessionEntry_Object = MibTableRow
eqlUserSessionEntry = _EqlUserSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 16, 1)
)
eqlUserSessionEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlUserSessionIndex"),
)
if mibBuilder.loadTexts:
    eqlUserSessionEntry.setStatus("current")
_EqlUserSessionIndex_Type = Unsigned32
_EqlUserSessionIndex_Object = MibTableColumn
eqlUserSessionIndex = _EqlUserSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 16, 1, 1),
    _EqlUserSessionIndex_Type()
)
eqlUserSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlUserSessionIndex.setStatus("current")
_EqlUserSessionAdminAccountIndex_Type = Integer32
_EqlUserSessionAdminAccountIndex_Object = MibTableColumn
eqlUserSessionAdminAccountIndex = _EqlUserSessionAdminAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 16, 1, 2),
    _EqlUserSessionAdminAccountIndex_Type()
)
eqlUserSessionAdminAccountIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlUserSessionAdminAccountIndex.setStatus("current")
_EqlUserSessionStart_Type = Counter32
_EqlUserSessionStart_Object = MibTableColumn
eqlUserSessionStart = _EqlUserSessionStart_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 16, 1, 3),
    _EqlUserSessionStart_Type()
)
eqlUserSessionStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlUserSessionStart.setStatus("current")


class _EqlUserSessionProtocol_Type(Integer32):
    """Custom type eqlUserSessionProtocol based on Integer32"""
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
        *(("console", 1),
          ("gui", 4),
          ("gui-ssl", 5),
          ("root", 0),
          ("ssh", 3),
          ("telnet", 2))
    )


_EqlUserSessionProtocol_Type.__name__ = "Integer32"
_EqlUserSessionProtocol_Object = MibTableColumn
eqlUserSessionProtocol = _EqlUserSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 16, 1, 4),
    _EqlUserSessionProtocol_Type()
)
eqlUserSessionProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlUserSessionProtocol.setStatus("current")
_EqlUserSessionRemoteAddress_Type = IpAddress
_EqlUserSessionRemoteAddress_Object = MibTableColumn
eqlUserSessionRemoteAddress = _EqlUserSessionRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 16, 1, 5),
    _EqlUserSessionRemoteAddress_Type()
)
eqlUserSessionRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlUserSessionRemoteAddress.setStatus("current")
_EqlUserSessionLocalAddress_Type = IpAddress
_EqlUserSessionLocalAddress_Object = MibTableColumn
eqlUserSessionLocalAddress = _EqlUserSessionLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 16, 1, 6),
    _EqlUserSessionLocalAddress_Type()
)
eqlUserSessionLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlUserSessionLocalAddress.setStatus("current")
_EqlUserSessionRemoteInetAddressType_Type = InetAddressType
_EqlUserSessionRemoteInetAddressType_Object = MibTableColumn
eqlUserSessionRemoteInetAddressType = _EqlUserSessionRemoteInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 16, 1, 7),
    _EqlUserSessionRemoteInetAddressType_Type()
)
eqlUserSessionRemoteInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlUserSessionRemoteInetAddressType.setStatus("current")
_EqlUserSessionRemoteInetAddress_Type = InetAddress
_EqlUserSessionRemoteInetAddress_Object = MibTableColumn
eqlUserSessionRemoteInetAddress = _EqlUserSessionRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 16, 1, 8),
    _EqlUserSessionRemoteInetAddress_Type()
)
eqlUserSessionRemoteInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlUserSessionRemoteInetAddress.setStatus("current")
_EqlUserSessionLocalInetAddressType_Type = InetAddressType
_EqlUserSessionLocalInetAddressType_Object = MibTableColumn
eqlUserSessionLocalInetAddressType = _EqlUserSessionLocalInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 16, 1, 9),
    _EqlUserSessionLocalInetAddressType_Type()
)
eqlUserSessionLocalInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlUserSessionLocalInetAddressType.setStatus("current")
_EqlUserSessionLocalInetAddress_Type = InetAddress
_EqlUserSessionLocalInetAddress_Object = MibTableColumn
eqlUserSessionLocalInetAddress = _EqlUserSessionLocalInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 16, 1, 10),
    _EqlUserSessionLocalInetAddress_Type()
)
eqlUserSessionLocalInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlUserSessionLocalInetAddress.setStatus("current")
_EqlRecordVersionTable_Object = MibTable
eqlRecordVersionTable = _EqlRecordVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 17)
)
if mibBuilder.loadTexts:
    eqlRecordVersionTable.setStatus("current")
_EqlRecordVersionEntry_Object = MibTableRow
eqlRecordVersionEntry = _EqlRecordVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 17, 1)
)
eqlRecordVersionEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlRecordVersionTableType"),
)
if mibBuilder.loadTexts:
    eqlRecordVersionEntry.setStatus("current")
_EqlRecordVersionTableType_Type = Unsigned32
_EqlRecordVersionTableType_Object = MibTableColumn
eqlRecordVersionTableType = _EqlRecordVersionTableType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 17, 1, 1),
    _EqlRecordVersionTableType_Type()
)
eqlRecordVersionTableType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlRecordVersionTableType.setStatus("current")
_EqlRecordVersionMin_Type = Unsigned32
_EqlRecordVersionMin_Object = MibTableColumn
eqlRecordVersionMin = _EqlRecordVersionMin_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 17, 1, 2),
    _EqlRecordVersionMin_Type()
)
eqlRecordVersionMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlRecordVersionMin.setStatus("current")
_EqlRecordVersionMax_Type = Unsigned32
_EqlRecordVersionMax_Object = MibTableColumn
eqlRecordVersionMax = _EqlRecordVersionMax_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 17, 1, 3),
    _EqlRecordVersionMax_Type()
)
eqlRecordVersionMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlRecordVersionMax.setStatus("current")
_EqlGroupTaskTable_Object = MibTable
eqlGroupTaskTable = _EqlGroupTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 18)
)
if mibBuilder.loadTexts:
    eqlGroupTaskTable.setStatus("current")
_EqlGroupTaskEntry_Object = MibTableRow
eqlGroupTaskEntry = _EqlGroupTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 18, 1)
)
eqlGroupTaskEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlGroupTaskIndex"),
)
if mibBuilder.loadTexts:
    eqlGroupTaskEntry.setStatus("current")
_EqlGroupTaskIndex_Type = Unsigned32
_EqlGroupTaskIndex_Object = MibTableColumn
eqlGroupTaskIndex = _EqlGroupTaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 18, 1, 1),
    _EqlGroupTaskIndex_Type()
)
eqlGroupTaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlGroupTaskIndex.setStatus("current")
_EqlGroupTaskRowStatus_Type = RowStatus
_EqlGroupTaskRowStatus_Object = MibTableColumn
eqlGroupTaskRowStatus = _EqlGroupTaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 18, 1, 2),
    _EqlGroupTaskRowStatus_Type()
)
eqlGroupTaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupTaskRowStatus.setStatus("current")


class _EqlGroupTaskType_Type(Integer32):
    """Custom type eqlGroupTaskType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failback", 2),
          ("resync", 1))
    )


_EqlGroupTaskType_Type.__name__ = "Integer32"
_EqlGroupTaskType_Object = MibTableColumn
eqlGroupTaskType = _EqlGroupTaskType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 18, 1, 3),
    _EqlGroupTaskType_Type()
)
eqlGroupTaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupTaskType.setStatus("current")
_EqlGroupTaskContext_Type = RowPointer
_EqlGroupTaskContext_Object = MibTableColumn
eqlGroupTaskContext = _EqlGroupTaskContext_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 18, 1, 4),
    _EqlGroupTaskContext_Type()
)
eqlGroupTaskContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupTaskContext.setStatus("current")
_EqlGroupTaskNumSubTasks_Type = Unsigned32
_EqlGroupTaskNumSubTasks_Object = MibTableColumn
eqlGroupTaskNumSubTasks = _EqlGroupTaskNumSubTasks_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 18, 1, 5),
    _EqlGroupTaskNumSubTasks_Type()
)
eqlGroupTaskNumSubTasks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupTaskNumSubTasks.setStatus("current")


class _EqlGroupTaskSubTaskInProgress_Type(Integer32):
    """Custom type eqlGroupTaskSubTaskInProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10001,
              10002,
              10003,
              10004,
              10005,
              20001,
              20002,
              20003,
              20004,
              20005)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("primaryVolumeDemote", 10003),
          ("primaryVolumeOffline", 10001),
          ("primaryVolumePromote", 20005),
          ("primaryVolumeReplicationCancel", 10002),
          ("recoveryVolumeCreateReplica", 10005),
          ("recoveryVolumeDemote", 20004),
          ("recoveryVolumeDisableSchedules", 20001),
          ("recoveryVolumeFinalReplication", 20003),
          ("recoveryVolumeOffline", 20002),
          ("recoveryVolumeReplicationConfigure", 10004))
    )


_EqlGroupTaskSubTaskInProgress_Type.__name__ = "Integer32"
_EqlGroupTaskSubTaskInProgress_Object = MibTableColumn
eqlGroupTaskSubTaskInProgress = _EqlGroupTaskSubTaskInProgress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 18, 1, 6),
    _EqlGroupTaskSubTaskInProgress_Type()
)
eqlGroupTaskSubTaskInProgress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupTaskSubTaskInProgress.setStatus("current")
_EqlGroupTaskSubtaskStatus_Type = Unsigned32
_EqlGroupTaskSubtaskStatus_Object = MibTableColumn
eqlGroupTaskSubtaskStatus = _EqlGroupTaskSubtaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 18, 1, 7),
    _EqlGroupTaskSubtaskStatus_Type()
)
eqlGroupTaskSubtaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupTaskSubtaskStatus.setStatus("current")


class _EqlGroupTaskStatus_Type(Integer32):
    """Custom type eqlGroupTaskStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("complete", 3),
          ("in-progress", 2),
          ("user-action-required", 1))
    )


_EqlGroupTaskStatus_Type.__name__ = "Integer32"
_EqlGroupTaskStatus_Object = MibTableColumn
eqlGroupTaskStatus = _EqlGroupTaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 18, 1, 8),
    _EqlGroupTaskStatus_Type()
)
eqlGroupTaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupTaskStatus.setStatus("current")


class _EqlGroupTaskUserAction_Type(Integer32):
    """Custom type eqlGroupTaskUserAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("retry", 1)
    )


_EqlGroupTaskUserAction_Type.__name__ = "Integer32"
_EqlGroupTaskUserAction_Object = MibTableColumn
eqlGroupTaskUserAction = _EqlGroupTaskUserAction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 18, 1, 9),
    _EqlGroupTaskUserAction_Type()
)
eqlGroupTaskUserAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupTaskUserAction.setStatus("current")
_EqlGroupTaskStartTime_Type = Counter32
_EqlGroupTaskStartTime_Object = MibTableColumn
eqlGroupTaskStartTime = _EqlGroupTaskStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 18, 1, 10),
    _EqlGroupTaskStartTime_Type()
)
eqlGroupTaskStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupTaskStartTime.setStatus("current")
if mibBuilder.loadTexts:
    eqlGroupTaskStartTime.setUnits("seconds")


class _EqlGroupTaskReplication_Type(Integer32):
    """Custom type eqlGroupTaskReplication based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("network", 2),
          ("noreplication", 3))
    )


_EqlGroupTaskReplication_Type.__name__ = "Integer32"
_EqlGroupTaskReplication_Object = MibTableColumn
eqlGroupTaskReplication = _EqlGroupTaskReplication_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 18, 1, 11),
    _EqlGroupTaskReplication_Type()
)
eqlGroupTaskReplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupTaskReplication.setStatus("current")
_EqlStorageGroupProfileTable_Object = MibTable
eqlStorageGroupProfileTable = _EqlStorageGroupProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 20)
)
if mibBuilder.loadTexts:
    eqlStorageGroupProfileTable.setStatus("current")
_EqlStorageGroupProfileEntry_Object = MibTableRow
eqlStorageGroupProfileEntry = _EqlStorageGroupProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 20, 1)
)
eqlStorageGroupProfileEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlGroupProfileIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupProfileEntry.setStatus("current")
_EqlStorageGroupProfileVersion_Type = Unsigned32
_EqlStorageGroupProfileVersion_Object = MibTableColumn
eqlStorageGroupProfileVersion = _EqlStorageGroupProfileVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 20, 1, 1),
    _EqlStorageGroupProfileVersion_Type()
)
eqlStorageGroupProfileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupProfileVersion.setStatus("current")
_EqlStorageGroupProfileWeight_Type = Unsigned32
_EqlStorageGroupProfileWeight_Object = MibTableColumn
eqlStorageGroupProfileWeight = _EqlStorageGroupProfileWeight_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 20, 1, 2),
    _EqlStorageGroupProfileWeight_Type()
)
eqlStorageGroupProfileWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupProfileWeight.setStatus("current")
_EqlStorageGroupProfileMaxMembers_Type = Unsigned32
_EqlStorageGroupProfileMaxMembers_Object = MibTableColumn
eqlStorageGroupProfileMaxMembers = _EqlStorageGroupProfileMaxMembers_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 20, 1, 3),
    _EqlStorageGroupProfileMaxMembers_Type()
)
eqlStorageGroupProfileMaxMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupProfileMaxMembers.setStatus("current")
_EqlStorageGroupProfileMaxVolumes_Type = Unsigned32
_EqlStorageGroupProfileMaxVolumes_Object = MibTableColumn
eqlStorageGroupProfileMaxVolumes = _EqlStorageGroupProfileMaxVolumes_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 20, 1, 4),
    _EqlStorageGroupProfileMaxVolumes_Type()
)
eqlStorageGroupProfileMaxVolumes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupProfileMaxVolumes.setStatus("current")
_EqlStorageGroupProfileMaxSnapsPerGroup_Type = Unsigned32
_EqlStorageGroupProfileMaxSnapsPerGroup_Object = MibTableColumn
eqlStorageGroupProfileMaxSnapsPerGroup = _EqlStorageGroupProfileMaxSnapsPerGroup_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 20, 1, 5),
    _EqlStorageGroupProfileMaxSnapsPerGroup_Type()
)
eqlStorageGroupProfileMaxSnapsPerGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupProfileMaxSnapsPerGroup.setStatus("current")
_EqlStorageGroupProfileMaxSnapsPerVolume_Type = Unsigned32
_EqlStorageGroupProfileMaxSnapsPerVolume_Object = MibTableColumn
eqlStorageGroupProfileMaxSnapsPerVolume = _EqlStorageGroupProfileMaxSnapsPerVolume_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 20, 1, 6),
    _EqlStorageGroupProfileMaxSnapsPerVolume_Type()
)
eqlStorageGroupProfileMaxSnapsPerVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupProfileMaxSnapsPerVolume.setStatus("current")
_EqlStorageGroupProfileMaxReplicasPerVolume_Type = Unsigned32
_EqlStorageGroupProfileMaxReplicasPerVolume_Object = MibTableColumn
eqlStorageGroupProfileMaxReplicasPerVolume = _EqlStorageGroupProfileMaxReplicasPerVolume_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 20, 1, 7),
    _EqlStorageGroupProfileMaxReplicasPerVolume_Type()
)
eqlStorageGroupProfileMaxReplicasPerVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupProfileMaxReplicasPerVolume.setStatus("current")
_EqlStorageGroupProfileMaxReplVolumes_Type = Unsigned32
_EqlStorageGroupProfileMaxReplVolumes_Object = MibTableColumn
eqlStorageGroupProfileMaxReplVolumes = _EqlStorageGroupProfileMaxReplVolumes_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 20, 1, 8),
    _EqlStorageGroupProfileMaxReplVolumes_Type()
)
eqlStorageGroupProfileMaxReplVolumes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupProfileMaxReplVolumes.setStatus("current")
_EqlStorageGroupProfileMaxConnections_Type = Unsigned32
_EqlStorageGroupProfileMaxConnections_Object = MibTableColumn
eqlStorageGroupProfileMaxConnections = _EqlStorageGroupProfileMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 20, 1, 9),
    _EqlStorageGroupProfileMaxConnections_Type()
)
eqlStorageGroupProfileMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupProfileMaxConnections.setStatus("current")
_EqlStorageGroupProfileMaxPartners_Type = Unsigned32
_EqlStorageGroupProfileMaxPartners_Object = MibTableColumn
eqlStorageGroupProfileMaxPartners = _EqlStorageGroupProfileMaxPartners_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 20, 1, 10),
    _EqlStorageGroupProfileMaxPartners_Type()
)
eqlStorageGroupProfileMaxPartners.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupProfileMaxPartners.setStatus("current")
_EqlStorageGroupProfileMaxConnWarning_Type = Unsigned32
_EqlStorageGroupProfileMaxConnWarning_Object = MibTableColumn
eqlStorageGroupProfileMaxConnWarning = _EqlStorageGroupProfileMaxConnWarning_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 20, 1, 11),
    _EqlStorageGroupProfileMaxConnWarning_Type()
)
eqlStorageGroupProfileMaxConnWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupProfileMaxConnWarning.setStatus("current")
_EqlStorageGroupProfileMaxSyncReplVolumes_Type = Unsigned32
_EqlStorageGroupProfileMaxSyncReplVolumes_Object = MibTableColumn
eqlStorageGroupProfileMaxSyncReplVolumes = _EqlStorageGroupProfileMaxSyncReplVolumes_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 20, 1, 12),
    _EqlStorageGroupProfileMaxSyncReplVolumes_Type()
)
eqlStorageGroupProfileMaxSyncReplVolumes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupProfileMaxSyncReplVolumes.setStatus("current")
_EqlStorageGroupAdminAccountKeyTable_Object = MibTable
eqlStorageGroupAdminAccountKeyTable = _EqlStorageGroupAdminAccountKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 21)
)
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountKeyTable.setStatus("current")
_EqlStorageGroupAdminAccountKeyEntry_Object = MibTableRow
eqlStorageGroupAdminAccountKeyEntry = _EqlStorageGroupAdminAccountKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 21, 1)
)
eqlStorageGroupAdminAccountKeyEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountKey"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountKeyEntry.setStatus("current")
_EqlStorageGroupAdminAccountIndexValue_Type = Integer32
_EqlStorageGroupAdminAccountIndexValue_Object = MibTableColumn
eqlStorageGroupAdminAccountIndexValue = _EqlStorageGroupAdminAccountIndexValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 21, 1, 1),
    _EqlStorageGroupAdminAccountIndexValue_Type()
)
eqlStorageGroupAdminAccountIndexValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStorageGroupAdminAccountIndexValue.setStatus("current")
_EqlStorageGroupChapAccountTable_Object = MibTable
eqlStorageGroupChapAccountTable = _EqlStorageGroupChapAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 22)
)
if mibBuilder.loadTexts:
    eqlStorageGroupChapAccountTable.setStatus("current")
_EqlStorageGroupChapAccountEntry_Object = MibTableRow
eqlStorageGroupChapAccountEntry = _EqlStorageGroupChapAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 22, 1)
)
eqlStorageGroupChapAccountEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlStorageGroupChapAccountIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupChapAccountEntry.setStatus("current")
_EqlStorageGroupChapAccountIndex_Type = Integer32
_EqlStorageGroupChapAccountIndex_Object = MibTableColumn
eqlStorageGroupChapAccountIndex = _EqlStorageGroupChapAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 22, 1, 1),
    _EqlStorageGroupChapAccountIndex_Type()
)
eqlStorageGroupChapAccountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlStorageGroupChapAccountIndex.setStatus("current")
_EqlStorageGroupChapAccountRowStatus_Type = RowStatus
_EqlStorageGroupChapAccountRowStatus_Object = MibTableColumn
eqlStorageGroupChapAccountRowStatus = _EqlStorageGroupChapAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 22, 1, 2),
    _EqlStorageGroupChapAccountRowStatus_Type()
)
eqlStorageGroupChapAccountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupChapAccountRowStatus.setStatus("current")
_EqlStorageGroupChapAccountAdminAccountKey_Type = Unsigned32
_EqlStorageGroupChapAccountAdminAccountKey_Object = MibTableColumn
eqlStorageGroupChapAccountAdminAccountKey = _EqlStorageGroupChapAccountAdminAccountKey_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 22, 1, 3),
    _EqlStorageGroupChapAccountAdminAccountKey_Type()
)
eqlStorageGroupChapAccountAdminAccountKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupChapAccountAdminAccountKey.setStatus("current")


class _EqlStorageGroupChapAccountPublic_Type(TruthValue):
    """Custom type eqlStorageGroupChapAccountPublic based on TruthValue"""


_EqlStorageGroupChapAccountPublic_Object = MibTableColumn
eqlStorageGroupChapAccountPublic = _EqlStorageGroupChapAccountPublic_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 22, 1, 4),
    _EqlStorageGroupChapAccountPublic_Type()
)
eqlStorageGroupChapAccountPublic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupChapAccountPublic.setStatus("current")
_EqlLDAPServerTable_Object = MibTable
eqlLDAPServerTable = _EqlLDAPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 24)
)
if mibBuilder.loadTexts:
    eqlLDAPServerTable.setStatus("current")
_EqlLDAPServerEntry_Object = MibTableRow
eqlLDAPServerEntry = _EqlLDAPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 24, 1)
)
eqlLDAPServerEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlLDAPServerIndex"),
)
if mibBuilder.loadTexts:
    eqlLDAPServerEntry.setStatus("current")
_EqlLDAPServerIndex_Type = Integer32
_EqlLDAPServerIndex_Object = MibTableColumn
eqlLDAPServerIndex = _EqlLDAPServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 24, 1, 1),
    _EqlLDAPServerIndex_Type()
)
eqlLDAPServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlLDAPServerIndex.setStatus("current")


class _EqlLDAPServerBaseDN_Type(OctetString):
    """Custom type eqlLDAPServerBaseDN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_EqlLDAPServerBaseDN_Type.__name__ = "OctetString"
_EqlLDAPServerBaseDN_Object = MibTableColumn
eqlLDAPServerBaseDN = _EqlLDAPServerBaseDN_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 24, 1, 2),
    _EqlLDAPServerBaseDN_Type()
)
eqlLDAPServerBaseDN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLDAPServerBaseDN.setStatus("current")


class _EqlLDAPServerSecureProtocol_Type(Integer32):
    """Custom type eqlLDAPServerSecureProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tls", 1))
    )


_EqlLDAPServerSecureProtocol_Type.__name__ = "Integer32"
_EqlLDAPServerSecureProtocol_Object = MibTableColumn
eqlLDAPServerSecureProtocol = _EqlLDAPServerSecureProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 24, 1, 3),
    _EqlLDAPServerSecureProtocol_Type()
)
eqlLDAPServerSecureProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLDAPServerSecureProtocol.setStatus("current")
_EqlLDAPServerInetAddressType_Type = InetAddressType
_EqlLDAPServerInetAddressType_Object = MibTableColumn
eqlLDAPServerInetAddressType = _EqlLDAPServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 24, 1, 4),
    _EqlLDAPServerInetAddressType_Type()
)
eqlLDAPServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLDAPServerInetAddressType.setStatus("current")
_EqlLDAPServerInetAddress_Type = InetAddress
_EqlLDAPServerInetAddress_Object = MibTableColumn
eqlLDAPServerInetAddress = _EqlLDAPServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 24, 1, 5),
    _EqlLDAPServerInetAddress_Type()
)
eqlLDAPServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLDAPServerInetAddress.setStatus("current")


class _EqlLDAPServerPort_Type(Integer32):
    """Custom type eqlLDAPServerPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EqlLDAPServerPort_Type.__name__ = "Integer32"
_EqlLDAPServerPort_Object = MibTableColumn
eqlLDAPServerPort = _EqlLDAPServerPort_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 24, 1, 6),
    _EqlLDAPServerPort_Type()
)
eqlLDAPServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLDAPServerPort.setStatus("current")


class _EqlLDAPServerAnonymousAccess_Type(TruthValue):
    """Custom type eqlLDAPServerAnonymousAccess based on TruthValue"""


_EqlLDAPServerAnonymousAccess_Object = MibTableColumn
eqlLDAPServerAnonymousAccess = _EqlLDAPServerAnonymousAccess_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 24, 1, 7),
    _EqlLDAPServerAnonymousAccess_Type()
)
eqlLDAPServerAnonymousAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLDAPServerAnonymousAccess.setStatus("current")


class _EqlLDAPServerBindDN_Type(OctetString):
    """Custom type eqlLDAPServerBindDN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_EqlLDAPServerBindDN_Type.__name__ = "OctetString"
_EqlLDAPServerBindDN_Object = MibTableColumn
eqlLDAPServerBindDN = _EqlLDAPServerBindDN_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 24, 1, 8),
    _EqlLDAPServerBindDN_Type()
)
eqlLDAPServerBindDN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLDAPServerBindDN.setStatus("current")


class _EqlLDAPServerBindPassword_Type(OctetString):
    """Custom type eqlLDAPServerBindPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlLDAPServerBindPassword_Type.__name__ = "OctetString"
_EqlLDAPServerBindPassword_Object = MibTableColumn
eqlLDAPServerBindPassword = _EqlLDAPServerBindPassword_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 24, 1, 9),
    _EqlLDAPServerBindPassword_Type()
)
eqlLDAPServerBindPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLDAPServerBindPassword.setStatus("current")
_EqlLDAPServerRowStatus_Type = RowStatus
_EqlLDAPServerRowStatus_Object = MibTableColumn
eqlLDAPServerRowStatus = _EqlLDAPServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 24, 1, 10),
    _EqlLDAPServerRowStatus_Type()
)
eqlLDAPServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLDAPServerRowStatus.setStatus("current")
_EqlLdapLoginAccessTable_Object = MibTable
eqlLdapLoginAccessTable = _EqlLdapLoginAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 25)
)
if mibBuilder.loadTexts:
    eqlLdapLoginAccessTable.setStatus("current")
_EqlLdapLoginAccessEntry_Object = MibTableRow
eqlLdapLoginAccessEntry = _EqlLdapLoginAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 25, 1)
)
eqlLdapLoginAccessEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlLdapLoginAccessType"),
    (0, "EQLGROUP-MIB", "eqlLdapLoginAccessName"),
)
if mibBuilder.loadTexts:
    eqlLdapLoginAccessEntry.setStatus("current")


class _EqlLdapLoginAccessName_Type(DisplayString):
    """Custom type eqlLdapLoginAccessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_EqlLdapLoginAccessName_Type.__name__ = "DisplayString"
_EqlLdapLoginAccessName_Object = MibTableColumn
eqlLdapLoginAccessName = _EqlLdapLoginAccessName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 25, 1, 1),
    _EqlLdapLoginAccessName_Type()
)
eqlLdapLoginAccessName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLdapLoginAccessName.setStatus("current")


class _EqlLdapLoginAccessType_Type(Integer32):
    """Custom type eqlLdapLoginAccessType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adGroup", 1),
          ("ldapUser", 2))
    )


_EqlLdapLoginAccessType_Type.__name__ = "Integer32"
_EqlLdapLoginAccessType_Object = MibTableColumn
eqlLdapLoginAccessType = _EqlLdapLoginAccessType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 25, 1, 2),
    _EqlLdapLoginAccessType_Type()
)
eqlLdapLoginAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLdapLoginAccessType.setStatus("current")
_EqlLdapLoginAccessAccountPrivilege_Type = AdminAccountPrivilegeType
_EqlLdapLoginAccessAccountPrivilege_Object = MibTableColumn
eqlLdapLoginAccessAccountPrivilege = _EqlLdapLoginAccessAccountPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 25, 1, 3),
    _EqlLdapLoginAccessAccountPrivilege_Type()
)
eqlLdapLoginAccessAccountPrivilege.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLdapLoginAccessAccountPrivilege.setStatus("current")
_EqlLdapLoginAccessAccountType_Type = AdminAccountType
_EqlLdapLoginAccessAccountType_Object = MibTableColumn
eqlLdapLoginAccessAccountType = _EqlLdapLoginAccessAccountType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 25, 1, 4),
    _EqlLdapLoginAccessAccountType_Type()
)
eqlLdapLoginAccessAccountType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLdapLoginAccessAccountType.setStatus("current")
_EqlLdapLoginAccessRowStatus_Type = RowStatus
_EqlLdapLoginAccessRowStatus_Object = MibTableColumn
eqlLdapLoginAccessRowStatus = _EqlLdapLoginAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 25, 1, 5),
    _EqlLdapLoginAccessRowStatus_Type()
)
eqlLdapLoginAccessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLdapLoginAccessRowStatus.setStatus("current")


class _EqlLdapLoginAccessAdDomainName_Type(DisplayString):
    """Custom type eqlLdapLoginAccessAdDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_EqlLdapLoginAccessAdDomainName_Type.__name__ = "DisplayString"
_EqlLdapLoginAccessAdDomainName_Object = MibTableColumn
eqlLdapLoginAccessAdDomainName = _EqlLdapLoginAccessAdDomainName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 25, 1, 6),
    _EqlLdapLoginAccessAdDomainName_Type()
)
eqlLdapLoginAccessAdDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLdapLoginAccessAdDomainName.setStatus("current")
_EqlStorageGroupDnsSuffixTable_Object = MibTable
eqlStorageGroupDnsSuffixTable = _EqlStorageGroupDnsSuffixTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 26)
)
if mibBuilder.loadTexts:
    eqlStorageGroupDnsSuffixTable.setStatus("current")
_EqlStorageGroupDnsSuffixEntry_Object = MibTableRow
eqlStorageGroupDnsSuffixEntry = _EqlStorageGroupDnsSuffixEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 26, 1)
)
eqlStorageGroupDnsSuffixEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlGroupDnsSuffixIndex"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupDnsSuffixEntry.setStatus("current")
_EqlGroupDnsSuffixIndex_Type = Integer32
_EqlGroupDnsSuffixIndex_Object = MibTableColumn
eqlGroupDnsSuffixIndex = _EqlGroupDnsSuffixIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 26, 1, 1),
    _EqlGroupDnsSuffixIndex_Type()
)
eqlGroupDnsSuffixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlGroupDnsSuffixIndex.setStatus("current")
_EqlGroupDnsSuffixRowStatus_Type = RowStatus
_EqlGroupDnsSuffixRowStatus_Object = MibTableColumn
eqlGroupDnsSuffixRowStatus = _EqlGroupDnsSuffixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 26, 1, 2),
    _EqlGroupDnsSuffixRowStatus_Type()
)
eqlGroupDnsSuffixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupDnsSuffixRowStatus.setStatus("current")


class _EqlGroupDnsSuffixString_Type(DisplayString):
    """Custom type eqlGroupDnsSuffixString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EqlGroupDnsSuffixString_Type.__name__ = "DisplayString"
_EqlGroupDnsSuffixString_Object = MibTableColumn
eqlGroupDnsSuffixString = _EqlGroupDnsSuffixString_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 26, 1, 3),
    _EqlGroupDnsSuffixString_Type()
)
eqlGroupDnsSuffixString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupDnsSuffixString.setStatus("current")


class _EqlGroupDnsSuffixConfigState_Type(Integer32):
    """Custom type eqlGroupDnsSuffixConfigState based on Integer32"""
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
        *(("endConfig", 2),
          ("inProgress", 1),
          ("startConfig", 0))
    )


_EqlGroupDnsSuffixConfigState_Type.__name__ = "Integer32"
_EqlGroupDnsSuffixConfigState_Object = MibTableColumn
eqlGroupDnsSuffixConfigState = _EqlGroupDnsSuffixConfigState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 26, 1, 4),
    _EqlGroupDnsSuffixConfigState_Type()
)
eqlGroupDnsSuffixConfigState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupDnsSuffixConfigState.setStatus("current")
_EqlStorageGroupSnmpTable_Object = MibTable
eqlStorageGroupSnmpTable = _EqlStorageGroupSnmpTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 27)
)
if mibBuilder.loadTexts:
    eqlStorageGroupSnmpTable.setStatus("current")
_EqlStorageGroupSnmpEntry_Object = MibTableRow
eqlStorageGroupSnmpEntry = _EqlStorageGroupSnmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 27, 1)
)
eqlStorageGroupSnmpEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupSnmpEntry.setStatus("current")
_EqlStorageGroupSnmpRowStatus_Type = RowStatus
_EqlStorageGroupSnmpRowStatus_Object = MibTableColumn
eqlStorageGroupSnmpRowStatus = _EqlStorageGroupSnmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 27, 1, 1),
    _EqlStorageGroupSnmpRowStatus_Type()
)
eqlStorageGroupSnmpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupSnmpRowStatus.setStatus("current")


class _EqlStorageGroupSnmpManagersList_Type(OctetString):
    """Custom type eqlStorageGroupSnmpManagersList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlStorageGroupSnmpManagersList_Type.__name__ = "OctetString"
_EqlStorageGroupSnmpManagersList_Object = MibTableColumn
eqlStorageGroupSnmpManagersList = _EqlStorageGroupSnmpManagersList_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 27, 1, 2),
    _EqlStorageGroupSnmpManagersList_Type()
)
eqlStorageGroupSnmpManagersList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupSnmpManagersList.setStatus("current")


class _EqlStorageGroupSnmpTrapCommunity_Type(OctetString):
    """Custom type eqlStorageGroupSnmpTrapCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlStorageGroupSnmpTrapCommunity_Type.__name__ = "OctetString"
_EqlStorageGroupSnmpTrapCommunity_Object = MibTableColumn
eqlStorageGroupSnmpTrapCommunity = _EqlStorageGroupSnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 27, 1, 3),
    _EqlStorageGroupSnmpTrapCommunity_Type()
)
eqlStorageGroupSnmpTrapCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupSnmpTrapCommunity.setStatus("current")
_EqlGroupSessionBannerTable_Object = MibTable
eqlGroupSessionBannerTable = _EqlGroupSessionBannerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 28)
)
if mibBuilder.loadTexts:
    eqlGroupSessionBannerTable.setStatus("current")
_EqlGroupSessionBannerEntry_Object = MibTableRow
eqlGroupSessionBannerEntry = _EqlGroupSessionBannerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 28, 1)
)
eqlGroupSessionBannerEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
)
if mibBuilder.loadTexts:
    eqlGroupSessionBannerEntry.setStatus("current")
_EqlGroupSessionBannerRowStatus_Type = RowStatus
_EqlGroupSessionBannerRowStatus_Object = MibTableColumn
eqlGroupSessionBannerRowStatus = _EqlGroupSessionBannerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 28, 1, 1),
    _EqlGroupSessionBannerRowStatus_Type()
)
eqlGroupSessionBannerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSessionBannerRowStatus.setStatus("current")


class _EqlGroupSessionBannerText_Type(OctetString):
    """Custom type eqlGroupSessionBannerText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_EqlGroupSessionBannerText_Type.__name__ = "OctetString"
_EqlGroupSessionBannerText_Object = MibTableColumn
eqlGroupSessionBannerText = _EqlGroupSessionBannerText_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 28, 1, 2),
    _EqlGroupSessionBannerText_Type()
)
eqlGroupSessionBannerText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlGroupSessionBannerText.setStatus("current")
_EqlGroupSingleSignOnStatusTable_Object = MibTable
eqlGroupSingleSignOnStatusTable = _EqlGroupSingleSignOnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 29)
)
if mibBuilder.loadTexts:
    eqlGroupSingleSignOnStatusTable.setStatus("current")
_EqlGroupSingleSignOnStatusEntry_Object = MibTableRow
eqlGroupSingleSignOnStatusEntry = _EqlGroupSingleSignOnStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 29, 1)
)
eqlGroupSingleSignOnStatusEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
)
if mibBuilder.loadTexts:
    eqlGroupSingleSignOnStatusEntry.setStatus("current")


class _EqlGroupSingleSignOnStatus_Type(Integer32):
    """Custom type eqlGroupSingleSignOnStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-ready", 0),
          ("ready", 1))
    )


_EqlGroupSingleSignOnStatus_Type.__name__ = "Integer32"
_EqlGroupSingleSignOnStatus_Object = MibTableColumn
eqlGroupSingleSignOnStatus = _EqlGroupSingleSignOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 29, 1, 1),
    _EqlGroupSingleSignOnStatus_Type()
)
eqlGroupSingleSignOnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlGroupSingleSignOnStatus.setStatus("current")


class _EqlGroupSingleSignOnRegGroupName_Type(DisplayString):
    """Custom type eqlGroupSingleSignOnRegGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlGroupSingleSignOnRegGroupName_Type.__name__ = "DisplayString"
_EqlGroupSingleSignOnRegGroupName_Object = MibTableColumn
eqlGroupSingleSignOnRegGroupName = _EqlGroupSingleSignOnRegGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 29, 1, 2),
    _EqlGroupSingleSignOnRegGroupName_Type()
)
eqlGroupSingleSignOnRegGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlGroupSingleSignOnRegGroupName.setStatus("current")


class _EqlGroupSingleSignOnKrbRealm_Type(OctetString):
    """Custom type eqlGroupSingleSignOnKrbRealm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_EqlGroupSingleSignOnKrbRealm_Type.__name__ = "OctetString"
_EqlGroupSingleSignOnKrbRealm_Object = MibTableColumn
eqlGroupSingleSignOnKrbRealm = _EqlGroupSingleSignOnKrbRealm_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 29, 1, 3),
    _EqlGroupSingleSignOnKrbRealm_Type()
)
eqlGroupSingleSignOnKrbRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlGroupSingleSignOnKrbRealm.setStatus("current")
_EqlNextAvailableIndexTable_Object = MibTable
eqlNextAvailableIndexTable = _EqlNextAvailableIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 30)
)
if mibBuilder.loadTexts:
    eqlNextAvailableIndexTable.setStatus("current")
_EqlNextAvailableIndexEntry_Object = MibTableRow
eqlNextAvailableIndexEntry = _EqlNextAvailableIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 30, 1)
)
eqlNextAvailableIndexEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlNextAvailableIndexTableType"),
)
if mibBuilder.loadTexts:
    eqlNextAvailableIndexEntry.setStatus("current")
_EqlNextAvailableIndexTableType_Type = Unsigned32
_EqlNextAvailableIndexTableType_Object = MibTableColumn
eqlNextAvailableIndexTableType = _EqlNextAvailableIndexTableType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 30, 1, 1),
    _EqlNextAvailableIndexTableType_Type()
)
eqlNextAvailableIndexTableType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNextAvailableIndexTableType.setStatus("current")
_EqlNextAvailableIndexValue_Type = Unsigned32
_EqlNextAvailableIndexValue_Object = MibTableColumn
eqlNextAvailableIndexValue = _EqlNextAvailableIndexValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 30, 1, 2),
    _EqlNextAvailableIndexValue_Type()
)
eqlNextAvailableIndexValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNextAvailableIndexValue.setStatus("current")
_EqlStorageGroupSnmpReadOnlyCommunityTable_Object = MibTable
eqlStorageGroupSnmpReadOnlyCommunityTable = _EqlStorageGroupSnmpReadOnlyCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 31)
)
if mibBuilder.loadTexts:
    eqlStorageGroupSnmpReadOnlyCommunityTable.setStatus("current")
_EqlStorageGroupSnmpReadOnlyCommunityEntry_Object = MibTableRow
eqlStorageGroupSnmpReadOnlyCommunityEntry = _EqlStorageGroupSnmpReadOnlyCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 31, 1)
)
eqlStorageGroupSnmpReadOnlyCommunityEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
)
if mibBuilder.loadTexts:
    eqlStorageGroupSnmpReadOnlyCommunityEntry.setStatus("current")


class _EqlStorageGroupSnmpReadOnlyCommunity_Type(DisplayString):
    """Custom type eqlStorageGroupSnmpReadOnlyCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlStorageGroupSnmpReadOnlyCommunity_Type.__name__ = "DisplayString"
_EqlStorageGroupSnmpReadOnlyCommunity_Object = MibTableColumn
eqlStorageGroupSnmpReadOnlyCommunity = _EqlStorageGroupSnmpReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 31, 1, 1),
    _EqlStorageGroupSnmpReadOnlyCommunity_Type()
)
eqlStorageGroupSnmpReadOnlyCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlStorageGroupSnmpReadOnlyCommunity.setStatus("current")
_EqlEULAAcceptInfoTable_Object = MibTable
eqlEULAAcceptInfoTable = _EqlEULAAcceptInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 32)
)
if mibBuilder.loadTexts:
    eqlEULAAcceptInfoTable.setStatus("current")
_EqlEULAAcceptInfoEntry_Object = MibTableRow
eqlEULAAcceptInfoEntry = _EqlEULAAcceptInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 32, 1)
)
eqlEULAAcceptInfoEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlEULAAcceptInfoFirmwareType"),
)
if mibBuilder.loadTexts:
    eqlEULAAcceptInfoEntry.setStatus("current")


class _EqlEULAAcceptInfoFirmwareType_Type(Integer32):
    """Custom type eqlEULAAcceptInfoFirmwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fluidfs-nas", 2),
          ("peer-storage-array", 1))
    )


_EqlEULAAcceptInfoFirmwareType_Type.__name__ = "Integer32"
_EqlEULAAcceptInfoFirmwareType_Object = MibTableColumn
eqlEULAAcceptInfoFirmwareType = _EqlEULAAcceptInfoFirmwareType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 32, 1, 1),
    _EqlEULAAcceptInfoFirmwareType_Type()
)
eqlEULAAcceptInfoFirmwareType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlEULAAcceptInfoFirmwareType.setStatus("current")
_EqlEULAAcceptInfoRowStatus_Type = RowStatus
_EqlEULAAcceptInfoRowStatus_Object = MibTableColumn
eqlEULAAcceptInfoRowStatus = _EqlEULAAcceptInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 32, 1, 2),
    _EqlEULAAcceptInfoRowStatus_Type()
)
eqlEULAAcceptInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlEULAAcceptInfoRowStatus.setStatus("current")


class _EqlEULAAcceptInfoAccountName_Type(DisplayString):
    """Custom type eqlEULAAcceptInfoAccountName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlEULAAcceptInfoAccountName_Type.__name__ = "DisplayString"
_EqlEULAAcceptInfoAccountName_Object = MibTableColumn
eqlEULAAcceptInfoAccountName = _EqlEULAAcceptInfoAccountName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 32, 1, 3),
    _EqlEULAAcceptInfoAccountName_Type()
)
eqlEULAAcceptInfoAccountName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlEULAAcceptInfoAccountName.setStatus("current")
_EqlEULAAcceptInfoEULAVersion_Type = Unsigned32
_EqlEULAAcceptInfoEULAVersion_Object = MibTableColumn
eqlEULAAcceptInfoEULAVersion = _EqlEULAAcceptInfoEULAVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 32, 1, 4),
    _EqlEULAAcceptInfoEULAVersion_Type()
)
eqlEULAAcceptInfoEULAVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlEULAAcceptInfoEULAVersion.setStatus("current")
_EqlEULAAcceptInfoTimestamp_Type = Unsigned32
_EqlEULAAcceptInfoTimestamp_Object = MibTableColumn
eqlEULAAcceptInfoTimestamp = _EqlEULAAcceptInfoTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 1, 1, 32, 1, 5),
    _EqlEULAAcceptInfoTimestamp_Type()
)
eqlEULAAcceptInfoTimestamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlEULAAcceptInfoTimestamp.setStatus("current")
_EqlgroupNotifications_ObjectIdentity = ObjectIdentity
eqlgroupNotifications = _EqlgroupNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 1, 2)
)
_EqlgroupConformance_ObjectIdentity = ObjectIdentity
eqlgroupConformance = _EqlgroupConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 1, 3)
)
eqlStorageGroupEntry.registerAugmentions(
    ("EQLGROUP-MIB",
     "eqlGroupCompatibilityEntry")
)
eqlGroupCompatibilityEntry.setIndexNames(*eqlStorageGroupEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLGROUP-MIB",
    **{"UTFString": UTFString,
       "AdminAccountPrivilegeType": AdminAccountPrivilegeType,
       "AdminAccountType": AdminAccountType,
       "eqlgroupModule": eqlgroupModule,
       "eqlgroupObjects": eqlgroupObjects,
       "eqlStorageGroupTable": eqlStorageGroupTable,
       "eqlStorageGroupEntry": eqlStorageGroupEntry,
       "eqlGroupId": eqlGroupId,
       "eqlGroupIsSingleSubnet": eqlGroupIsSingleSubnet,
       "eqlGroupDefaultGatewayIpAddress": eqlGroupDefaultGatewayIpAddress,
       "eqlGroupDefaultMask": eqlGroupDefaultMask,
       "eqlGroupDefaultRoutingProtocol": eqlGroupDefaultRoutingProtocol,
       "eqlGroupIsStorageOptimization": eqlGroupIsStorageOptimization,
       "eqlGroupDiskAddWaitTime": eqlGroupDiskAddWaitTime,
       "eqlGroupDefaultLanguage": eqlGroupDefaultLanguage,
       "eqlGroupDefaultSnapshotSize": eqlGroupDefaultSnapshotSize,
       "eqlGroupDefaultSnapshotWarningLevel": eqlGroupDefaultSnapshotWarningLevel,
       "eqlGroupDefaultSnapshotDeletePolicy": eqlGroupDefaultSnapshotDeletePolicy,
       "eqlGroupTimeZone": eqlGroupTimeZone,
       "eqlGroupLogLevel": eqlGroupLogLevel,
       "eqlGroupDescription": eqlGroupDescription,
       "eqlGroupIscsiNamePrefix": eqlGroupIscsiNamePrefix,
       "eqlGroupDefaultAliasToVolumeName": eqlGroupDefaultAliasToVolumeName,
       "eqlGroupEmailSrcDomain": eqlGroupEmailSrcDomain,
       "eqlGroupName": eqlGroupName,
       "eqlGroupIpAddr": eqlGroupIpAddr,
       "eqlGroupEnableWebAccessSSL": eqlGroupEnableWebAccessSSL,
       "eqlGroupEnableWebAccessUnsecure": eqlGroupEnableWebAccessUnsecure,
       "eqlGroupEnableCliAccessSSH": eqlGroupEnableCliAccessSSH,
       "eqlGroupEnableCliAccessUnsecure": eqlGroupEnableCliAccessUnsecure,
       "eqlGroupEnableEmailNotifications": eqlGroupEnableEmailNotifications,
       "eqlGroupEnableSNMPTraps": eqlGroupEnableSNMPTraps,
       "eqlGroupEnableSyslog": eqlGroupEnableSyslog,
       "eqlGroupEmailPriorityMask": eqlGroupEmailPriorityMask,
       "eqlGroupSNMPPriorityMask": eqlGroupSNMPPriorityMask,
       "eqlGroupSysLogPriorityMask": eqlGroupSysLogPriorityMask,
       "eqlGroupDefaultSite": eqlGroupDefaultSite,
       "eqlGroupPasswd1": eqlGroupPasswd1,
       "eqlGroupPasswd2": eqlGroupPasswd2,
       "eqlGroupRowStatus": eqlGroupRowStatus,
       "eqlGroupObjectReuseScrub": eqlGroupObjectReuseScrub,
       "eqlGroupEnableSSH": eqlGroupEnableSSH,
       "eqlGroupEnableTelnet": eqlGroupEnableTelnet,
       "eqlGroupEnableFTP": eqlGroupEnableFTP,
       "eqlGroupEmailSrcUserName": eqlGroupEmailSrcUserName,
       "eqlGroupSyslogFacility": eqlGroupSyslogFacility,
       "eqlGroupEnableCLB": eqlGroupEnableCLB,
       "eqlGroupEnableVolBal": eqlGroupEnableVolBal,
       "eqlGroupDiscoveryFilter": eqlGroupDiscoveryFilter,
       "eqlGroupEmailSupportContact": eqlGroupEmailSupportContact,
       "eqlGroupReplicationWindowSize": eqlGroupReplicationWindowSize,
       "eqlGroupConfigurationFlags": eqlGroupConfigurationFlags,
       "eqlGroupISCSIPortalGrpTag": eqlGroupISCSIPortalGrpTag,
       "eqlGroupMaxConcurrentReplicas": eqlGroupMaxConcurrentReplicas,
       "eqlGroupDefaultThinWarn": eqlGroupDefaultThinWarn,
       "eqlGroupDefaultThinMaxGrow": eqlGroupDefaultThinMaxGrow,
       "eqlGroupDefaultMgmtGatewayIpAddressType": eqlGroupDefaultMgmtGatewayIpAddressType,
       "eqlGroupDefaultMgmtGatewayIpAddress": eqlGroupDefaultMgmtGatewayIpAddress,
       "eqlGroupInet6AddrType": eqlGroupInet6AddrType,
       "eqlGroupInet6Addr": eqlGroupInet6Addr,
       "eqlGroupInetAddrType": eqlGroupInetAddrType,
       "eqlGroupInetAddr": eqlGroupInetAddr,
       "eqlGroupSupportSlowSwitch": eqlGroupSupportSlowSwitch,
       "eqlGroupProfileIndex": eqlGroupProfileIndex,
       "eqlGroupEnableSSHProtocolV1": eqlGroupEnableSSHProtocolV1,
       "eqlGroupEnableStandbyButton": eqlGroupEnableStandbyButton,
       "eqlGroupLDAPLoginAuthEnable": eqlGroupLDAPLoginAuthEnable,
       "eqlGroupApplianceDiscovery": eqlGroupApplianceDiscovery,
       "eqlGroupDefaultDcbVlanId": eqlGroupDefaultDcbVlanId,
       "eqlGroupThermalShutdownOverride": eqlGroupThermalShutdownOverride,
       "eqlGroupEnableLegacyCryptos": eqlGroupEnableLegacyCryptos,
       "eqlGroupMaxReplSegments": eqlGroupMaxReplSegments,
       "eqlGroupEnableVolumeRecovery": eqlGroupEnableVolumeRecovery,
       "eqlGroupSessionIdleTimeout": eqlGroupSessionIdleTimeout,
       "eqlGroupSessionIdleTimeoutEnable": eqlGroupSessionIdleTimeoutEnable,
       "eqlGroupSessionBannerEnable": eqlGroupSessionBannerEnable,
       "eqlGroupDefaultVolSnapshotBorrowEnabled": eqlGroupDefaultVolSnapshotBorrowEnabled,
       "eqlGroupRecoveryLifeTimeEnable": eqlGroupRecoveryLifeTimeEnable,
       "eqlGroupRecoveryLifeTime": eqlGroupRecoveryLifeTime,
       "eqlGroupTimeProtocol": eqlGroupTimeProtocol,
       "eqlGroupRecoveryTrimmerFreq": eqlGroupRecoveryTrimmerFreq,
       "eqlGroupUpdateEnable": eqlGroupUpdateEnable,
       "eqlGroupUpdateLast": eqlGroupUpdateLast,
       "eqlGroupDefaultSectorSize": eqlGroupDefaultSectorSize,
       "eqlGroupCompressionScanFreq": eqlGroupCompressionScanFreq,
       "eqlGroupRunCompressionScan": eqlGroupRunCompressionScan,
       "eqlGroupMonitorReminderTimestamp": eqlGroupMonitorReminderTimestamp,
       "eqlStorageGroupStatusTable": eqlStorageGroupStatusTable,
       "eqlStorageGroupStatusEntry": eqlStorageGroupStatusEntry,
       "eqlStorageGroupStatusPoolSpace": eqlStorageGroupStatusPoolSpace,
       "eqlStorageGroupStatusPoolSpaceUsed": eqlStorageGroupStatusPoolSpaceUsed,
       "eqlStorageGroupStatusTotalMembersOnLine": eqlStorageGroupStatusTotalMembersOnLine,
       "eqlStorageGroupStatusPoolSpaceReserved": eqlStorageGroupStatusPoolSpaceReserved,
       "eqlStorageGroupStatusReservedSpaceInUse": eqlStorageGroupStatusReservedSpaceInUse,
       "eqlStorageGroupStatusDateAndTime": eqlStorageGroupStatusDateAndTime,
       "eqlStorageGroupStatusSnapshotsInUse": eqlStorageGroupStatusSnapshotsInUse,
       "eqlStorageGroupStatusVolumesInUse": eqlStorageGroupStatusVolumesInUse,
       "eqlStorageGroupStatusSnapshotsOnline": eqlStorageGroupStatusSnapshotsOnline,
       "eqlStorageGroupStatusVolumesOnline": eqlStorageGroupStatusVolumesOnline,
       "eqlStorageGroupStatusSnapshotCount": eqlStorageGroupStatusSnapshotCount,
       "eqlStorageGroupStatusVolumeCount": eqlStorageGroupStatusVolumeCount,
       "eqlStorageGroupStatusMemberCount": eqlStorageGroupStatusMemberCount,
       "eqlStorageGroupStatusMembersInUse": eqlStorageGroupStatusMembersInUse,
       "eqlStorageGroupStatusFreeSpace": eqlStorageGroupStatusFreeSpace,
       "eqlStorageGroupStatusPoolSpaceDelegated": eqlStorageGroupStatusPoolSpaceDelegated,
       "eqlStorageGroupStatusDelegatedUsedSpace": eqlStorageGroupStatusDelegatedUsedSpace,
       "eqlStorageGroupStatusReplReserveSpace": eqlStorageGroupStatusReplReserveSpace,
       "eqlStorageGroupStatusReplReserveInUse": eqlStorageGroupStatusReplReserveInUse,
       "eqlStorageGroupStatusVolumeSpaceSubscribed": eqlStorageGroupStatusVolumeSpaceSubscribed,
       "eqlStorageGroupStatusVolumeSpaceAllocated": eqlStorageGroupStatusVolumeSpaceAllocated,
       "eqlStorageGroupStatusFailbackSpace": eqlStorageGroupStatusFailbackSpace,
       "eqlStorageGroupStatusThinProvFreeSpace": eqlStorageGroupStatusThinProvFreeSpace,
       "eqlStorageGroupStatusConnectionCount": eqlStorageGroupStatusConnectionCount,
       "eqlStorageGroupStatusSnapReserveSpaceFree": eqlStorageGroupStatusSnapReserveSpaceFree,
       "eqlStorageGroupStatusReplReserveSpaceFree": eqlStorageGroupStatusReplReserveSpaceFree,
       "eqlStorageGroupStatusGroupId": eqlStorageGroupStatusGroupId,
       "eqlStorageGroupStatusVirtualVolumeCount": eqlStorageGroupStatusVirtualVolumeCount,
       "eqlStorageGroupStatusVirtualVolumesOnline": eqlStorageGroupStatusVirtualVolumesOnline,
       "eqlStorageGroupStatusVirtualVolumesInUse": eqlStorageGroupStatusVirtualVolumesInUse,
       "eqlStorageGroupStatusVirtualVolumeSpaceSubscribed": eqlStorageGroupStatusVirtualVolumeSpaceSubscribed,
       "eqlStorageGroupStatsTotalSpaceBorrowing": eqlStorageGroupStatsTotalSpaceBorrowing,
       "eqlStorageGroupStatusStorageContainerCount": eqlStorageGroupStatusStorageContainerCount,
       "eqlStorageGroupStatusStorageContainerVolumeCount": eqlStorageGroupStatusStorageContainerVolumeCount,
       "eqlStorageGroupStatusStorageContainerSnapCount": eqlStorageGroupStatusStorageContainerSnapCount,
       "eqlStorageGroupStatusStorageContainerVolumesOnline": eqlStorageGroupStatusStorageContainerVolumesOnline,
       "eqlStorageGroupStatusStorageContainerSpaceReserved": eqlStorageGroupStatusStorageContainerSpaceReserved,
       "eqlStorageGroupStatusCompressedSpaceUsed": eqlStorageGroupStatusCompressedSpaceUsed,
       "eqlStorageGroupStatusVirtualSpaceSize": eqlStorageGroupStatusVirtualSpaceSize,
       "eqlStorageGroupStatusReplicationSnapCount": eqlStorageGroupStatusReplicationSnapCount,
       "eqlStorageGroupStatusStorageContainerVolumesBound": eqlStorageGroupStatusStorageContainerVolumesBound,
       "eqlStorageGroupSiteTable": eqlStorageGroupSiteTable,
       "eqlStorageGroupSiteEntry": eqlStorageGroupSiteEntry,
       "eqlGroupSiteIndex": eqlGroupSiteIndex,
       "eqlGroupSiteName": eqlGroupSiteName,
       "eqlGroupSiteDescription": eqlGroupSiteDescription,
       "eqlGroupSiteContactEmail": eqlGroupSiteContactEmail,
       "eqlGroupSiteContactPhone": eqlGroupSiteContactPhone,
       "eqlGroupSiteContactMobile": eqlGroupSiteContactMobile,
       "eqlGroupSiteRowStatus": eqlGroupSiteRowStatus,
       "eqlStorageGroupDnsServerTable": eqlStorageGroupDnsServerTable,
       "eqlStorageGroupDnsServerEntry": eqlStorageGroupDnsServerEntry,
       "eqlGroupDnsServerIndex": eqlGroupDnsServerIndex,
       "eqlGroupDnsServerIpAddress": eqlGroupDnsServerIpAddress,
       "eqlGroupDnsServerRowStatus": eqlGroupDnsServerRowStatus,
       "eqlGroupDnsServerInetAddressType": eqlGroupDnsServerInetAddressType,
       "eqlGroupDnsServerInetAddress": eqlGroupDnsServerInetAddress,
       "eqlGroupDnsServerConfigState": eqlGroupDnsServerConfigState,
       "eqlStorageGroupNtpServerTable": eqlStorageGroupNtpServerTable,
       "eqlStorageGroupNtpServerEntry": eqlStorageGroupNtpServerEntry,
       "eqlGroupNtpServerIndex": eqlGroupNtpServerIndex,
       "eqlGroupNtpServerIpAddress": eqlGroupNtpServerIpAddress,
       "eqlGroupNtpServerRowStatus": eqlGroupNtpServerRowStatus,
       "eqlGroupNtpServerPort": eqlGroupNtpServerPort,
       "eqlGroupNtpServerInetAddressType": eqlGroupNtpServerInetAddressType,
       "eqlGroupNtpServerInetAddress": eqlGroupNtpServerInetAddress,
       "eqlStorageGroupChapServerTable": eqlStorageGroupChapServerTable,
       "eqlStorageGroupChapServerEntry": eqlStorageGroupChapServerEntry,
       "eqlGroupChapServerIndex": eqlGroupChapServerIndex,
       "eqlGroupChapServerIpAddress": eqlGroupChapServerIpAddress,
       "eqlGroupChapServerRowStatus": eqlGroupChapServerRowStatus,
       "eqlGroupChapServerPort": eqlGroupChapServerPort,
       "eqlGroupChapServerRADIUSSecret": eqlGroupChapServerRADIUSSecret,
       "eqlGroupChapServerInetAddressType": eqlGroupChapServerInetAddressType,
       "eqlGroupChapServerInetAddress": eqlGroupChapServerInetAddress,
       "eqlStorageGroupSMTPServerTable": eqlStorageGroupSMTPServerTable,
       "eqlStorageGroupSMTPServerEntry": eqlStorageGroupSMTPServerEntry,
       "eqlGroupSMTPServerIndex": eqlGroupSMTPServerIndex,
       "eqlGroupSMTPServerIpAddress": eqlGroupSMTPServerIpAddress,
       "eqlGroupSMTPServerRowStatus": eqlGroupSMTPServerRowStatus,
       "eqlGroupSMTPServerPort": eqlGroupSMTPServerPort,
       "eqlGroupSMTPServerInetAddressType": eqlGroupSMTPServerInetAddressType,
       "eqlGroupSMTPServerInetAddress": eqlGroupSMTPServerInetAddress,
       "eqlStorageGroupSysLogServerTable": eqlStorageGroupSysLogServerTable,
       "eqlStorageGroupSysLogServerEntry": eqlStorageGroupSysLogServerEntry,
       "eqlGroupSysLogServerIndex": eqlGroupSysLogServerIndex,
       "eqlGroupSysLogServerIpAddress": eqlGroupSysLogServerIpAddress,
       "eqlGroupSysLogServerRowStatus": eqlGroupSysLogServerRowStatus,
       "eqlGroupSysLogServerInetAddressType": eqlGroupSysLogServerInetAddressType,
       "eqlGroupSysLogServerInetAddress": eqlGroupSysLogServerInetAddress,
       "eqlStorageGroupAlertEmailTable": eqlStorageGroupAlertEmailTable,
       "eqlStorageGroupAlertEmailEntry": eqlStorageGroupAlertEmailEntry,
       "eqlGroupAlertEmailIndex": eqlGroupAlertEmailIndex,
       "eqlGroupAlertEmailAddress": eqlGroupAlertEmailAddress,
       "eqlGroupAlertEmailRowStatus": eqlGroupAlertEmailRowStatus,
       "eqlStorageGroupAdminAccountTable": eqlStorageGroupAdminAccountTable,
       "eqlStorageGroupAdminAccountEntry": eqlStorageGroupAdminAccountEntry,
       "eqlStorageGroupAdminAccountIndex": eqlStorageGroupAdminAccountIndex,
       "eqlStorageGroupAdminAccountRowStatus": eqlStorageGroupAdminAccountRowStatus,
       "eqlStorageGroupAdminAccountName": eqlStorageGroupAdminAccountName,
       "eqlStorageGroupAdminAccountPassword": eqlStorageGroupAdminAccountPassword,
       "eqlStorageGroupAdminAccountDescription": eqlStorageGroupAdminAccountDescription,
       "eqlStorageGroupAdminAccountType": eqlStorageGroupAdminAccountType,
       "eqlStorageGroupAdminAccountContact": eqlStorageGroupAdminAccountContact,
       "eqlStorageGroupAdminAccountEmail": eqlStorageGroupAdminAccountEmail,
       "eqlStorageGroupAdminAccountPhone": eqlStorageGroupAdminAccountPhone,
       "eqlStorageGroupAdminAccountMobile": eqlStorageGroupAdminAccountMobile,
       "eqlStorageGroupAdminAccountStatus": eqlStorageGroupAdminAccountStatus,
       "eqlStorageGroupAdminAccountCliFlags": eqlStorageGroupAdminAccountCliFlags,
       "eqlStorageGroupAdminAccountGuiFlags": eqlStorageGroupAdminAccountGuiFlags,
       "eqlStorageGroupAdminAccountPollInterval": eqlStorageGroupAdminAccountPollInterval,
       "eqlStorageGroupAdminAccountAuthType": eqlStorageGroupAdminAccountAuthType,
       "eqlStorageGroupAdminAccountRecentLogin": eqlStorageGroupAdminAccountRecentLogin,
       "eqlStorageGroupAdminAccountClass": eqlStorageGroupAdminAccountClass,
       "eqlStorageGroupAdminAccountPrivilege": eqlStorageGroupAdminAccountPrivilege,
       "eqlStorageGroupAdminAccountSnmpKey": eqlStorageGroupAdminAccountSnmpKey,
       "eqlStorageGroupAdminAccountSnmpKey2": eqlStorageGroupAdminAccountSnmpKey2,
       "eqlStorageGroupAdminAccountCHAPPassword": eqlStorageGroupAdminAccountCHAPPassword,
       "eqlStorageGroupAdminAccountKey": eqlStorageGroupAdminAccountKey,
       "eqlStorageGroupAdminAccountAdGroupName": eqlStorageGroupAdminAccountAdGroupName,
       "eqlStorageGroupAdminAccountSNMPPrivProt": eqlStorageGroupAdminAccountSNMPPrivProt,
       "eqlStorageGroupiSNSServerTable": eqlStorageGroupiSNSServerTable,
       "eqlStorageGroupiSNSServerEntry": eqlStorageGroupiSNSServerEntry,
       "eqlGroupiSNSServerIndex": eqlGroupiSNSServerIndex,
       "eqlGroupiSNSServerRowStatus": eqlGroupiSNSServerRowStatus,
       "eqlGroupiSNSServerIpAddress": eqlGroupiSNSServerIpAddress,
       "eqlGroupiSNSServerPort": eqlGroupiSNSServerPort,
       "eqlGroupiSNSServerInetAddressType": eqlGroupiSNSServerInetAddressType,
       "eqlGroupiSNSServerInetAddress": eqlGroupiSNSServerInetAddress,
       "eqlGroupCompatibilityTable": eqlGroupCompatibilityTable,
       "eqlGroupCompatibilityEntry": eqlGroupCompatibilityEntry,
       "eqlGroupCurrentCompLevel": eqlGroupCurrentCompLevel,
       "eqlStorageGroupCollectionTable": eqlStorageGroupCollectionTable,
       "eqlStorageGroupCollectionEntry": eqlStorageGroupCollectionEntry,
       "eqlGrpNoofVolCollections": eqlGrpNoofVolCollections,
       "eqlGrpNoofSnapCollections": eqlGrpNoofSnapCollections,
       "eqlGrpNoofOrphanSnapCollections": eqlGrpNoofOrphanSnapCollections,
       "eqlRADIUSTable": eqlRADIUSTable,
       "eqlRADIUSEntry": eqlRADIUSEntry,
       "eqlRADIUSSecret": eqlRADIUSSecret,
       "eqlRADIUSLoginAuthEnable": eqlRADIUSLoginAuthEnable,
       "eqlRADIUSAuthRecvTimeout": eqlRADIUSAuthRecvTimeout,
       "eqlRADIUSAuthMaxRetries": eqlRADIUSAuthMaxRetries,
       "eqlRADIUSLoginAcctEnable": eqlRADIUSLoginAcctEnable,
       "eqlRADIUSAcctRecvTimeout": eqlRADIUSAcctRecvTimeout,
       "eqlRADIUSAcctMaxRetries": eqlRADIUSAcctMaxRetries,
       "eqlRADIUSiscsiAuthEnable": eqlRADIUSiscsiAuthEnable,
       "eqlLocaliscsiAuthEnable": eqlLocaliscsiAuthEnable,
       "eqlRADIUSRequireAdminAttrEnable": eqlRADIUSRequireAdminAttrEnable,
       "eqlRADIUSAcctServerTable": eqlRADIUSAcctServerTable,
       "eqlRADIUSAcctServerEntry": eqlRADIUSAcctServerEntry,
       "eqlRADIUSAcctServerIndex": eqlRADIUSAcctServerIndex,
       "eqlRADIUSAcctServerIpAddress": eqlRADIUSAcctServerIpAddress,
       "eqlRADIUSAcctServerPort": eqlRADIUSAcctServerPort,
       "eqlRADIUSAcctServerRowStatus": eqlRADIUSAcctServerRowStatus,
       "eqlRADIUSAcctServerSecret": eqlRADIUSAcctServerSecret,
       "eqlRADIUSAcctServerInetAddressType": eqlRADIUSAcctServerInetAddressType,
       "eqlRADIUSAcctServerInetAddress": eqlRADIUSAcctServerInetAddress,
       "eqlUserSessionTable": eqlUserSessionTable,
       "eqlUserSessionEntry": eqlUserSessionEntry,
       "eqlUserSessionIndex": eqlUserSessionIndex,
       "eqlUserSessionAdminAccountIndex": eqlUserSessionAdminAccountIndex,
       "eqlUserSessionStart": eqlUserSessionStart,
       "eqlUserSessionProtocol": eqlUserSessionProtocol,
       "eqlUserSessionRemoteAddress": eqlUserSessionRemoteAddress,
       "eqlUserSessionLocalAddress": eqlUserSessionLocalAddress,
       "eqlUserSessionRemoteInetAddressType": eqlUserSessionRemoteInetAddressType,
       "eqlUserSessionRemoteInetAddress": eqlUserSessionRemoteInetAddress,
       "eqlUserSessionLocalInetAddressType": eqlUserSessionLocalInetAddressType,
       "eqlUserSessionLocalInetAddress": eqlUserSessionLocalInetAddress,
       "eqlRecordVersionTable": eqlRecordVersionTable,
       "eqlRecordVersionEntry": eqlRecordVersionEntry,
       "eqlRecordVersionTableType": eqlRecordVersionTableType,
       "eqlRecordVersionMin": eqlRecordVersionMin,
       "eqlRecordVersionMax": eqlRecordVersionMax,
       "eqlGroupTaskTable": eqlGroupTaskTable,
       "eqlGroupTaskEntry": eqlGroupTaskEntry,
       "eqlGroupTaskIndex": eqlGroupTaskIndex,
       "eqlGroupTaskRowStatus": eqlGroupTaskRowStatus,
       "eqlGroupTaskType": eqlGroupTaskType,
       "eqlGroupTaskContext": eqlGroupTaskContext,
       "eqlGroupTaskNumSubTasks": eqlGroupTaskNumSubTasks,
       "eqlGroupTaskSubTaskInProgress": eqlGroupTaskSubTaskInProgress,
       "eqlGroupTaskSubtaskStatus": eqlGroupTaskSubtaskStatus,
       "eqlGroupTaskStatus": eqlGroupTaskStatus,
       "eqlGroupTaskUserAction": eqlGroupTaskUserAction,
       "eqlGroupTaskStartTime": eqlGroupTaskStartTime,
       "eqlGroupTaskReplication": eqlGroupTaskReplication,
       "eqlStorageGroupProfileTable": eqlStorageGroupProfileTable,
       "eqlStorageGroupProfileEntry": eqlStorageGroupProfileEntry,
       "eqlStorageGroupProfileVersion": eqlStorageGroupProfileVersion,
       "eqlStorageGroupProfileWeight": eqlStorageGroupProfileWeight,
       "eqlStorageGroupProfileMaxMembers": eqlStorageGroupProfileMaxMembers,
       "eqlStorageGroupProfileMaxVolumes": eqlStorageGroupProfileMaxVolumes,
       "eqlStorageGroupProfileMaxSnapsPerGroup": eqlStorageGroupProfileMaxSnapsPerGroup,
       "eqlStorageGroupProfileMaxSnapsPerVolume": eqlStorageGroupProfileMaxSnapsPerVolume,
       "eqlStorageGroupProfileMaxReplicasPerVolume": eqlStorageGroupProfileMaxReplicasPerVolume,
       "eqlStorageGroupProfileMaxReplVolumes": eqlStorageGroupProfileMaxReplVolumes,
       "eqlStorageGroupProfileMaxConnections": eqlStorageGroupProfileMaxConnections,
       "eqlStorageGroupProfileMaxPartners": eqlStorageGroupProfileMaxPartners,
       "eqlStorageGroupProfileMaxConnWarning": eqlStorageGroupProfileMaxConnWarning,
       "eqlStorageGroupProfileMaxSyncReplVolumes": eqlStorageGroupProfileMaxSyncReplVolumes,
       "eqlStorageGroupAdminAccountKeyTable": eqlStorageGroupAdminAccountKeyTable,
       "eqlStorageGroupAdminAccountKeyEntry": eqlStorageGroupAdminAccountKeyEntry,
       "eqlStorageGroupAdminAccountIndexValue": eqlStorageGroupAdminAccountIndexValue,
       "eqlStorageGroupChapAccountTable": eqlStorageGroupChapAccountTable,
       "eqlStorageGroupChapAccountEntry": eqlStorageGroupChapAccountEntry,
       "eqlStorageGroupChapAccountIndex": eqlStorageGroupChapAccountIndex,
       "eqlStorageGroupChapAccountRowStatus": eqlStorageGroupChapAccountRowStatus,
       "eqlStorageGroupChapAccountAdminAccountKey": eqlStorageGroupChapAccountAdminAccountKey,
       "eqlStorageGroupChapAccountPublic": eqlStorageGroupChapAccountPublic,
       "eqlLDAPServerTable": eqlLDAPServerTable,
       "eqlLDAPServerEntry": eqlLDAPServerEntry,
       "eqlLDAPServerIndex": eqlLDAPServerIndex,
       "eqlLDAPServerBaseDN": eqlLDAPServerBaseDN,
       "eqlLDAPServerSecureProtocol": eqlLDAPServerSecureProtocol,
       "eqlLDAPServerInetAddressType": eqlLDAPServerInetAddressType,
       "eqlLDAPServerInetAddress": eqlLDAPServerInetAddress,
       "eqlLDAPServerPort": eqlLDAPServerPort,
       "eqlLDAPServerAnonymousAccess": eqlLDAPServerAnonymousAccess,
       "eqlLDAPServerBindDN": eqlLDAPServerBindDN,
       "eqlLDAPServerBindPassword": eqlLDAPServerBindPassword,
       "eqlLDAPServerRowStatus": eqlLDAPServerRowStatus,
       "eqlLdapLoginAccessTable": eqlLdapLoginAccessTable,
       "eqlLdapLoginAccessEntry": eqlLdapLoginAccessEntry,
       "eqlLdapLoginAccessName": eqlLdapLoginAccessName,
       "eqlLdapLoginAccessType": eqlLdapLoginAccessType,
       "eqlLdapLoginAccessAccountPrivilege": eqlLdapLoginAccessAccountPrivilege,
       "eqlLdapLoginAccessAccountType": eqlLdapLoginAccessAccountType,
       "eqlLdapLoginAccessRowStatus": eqlLdapLoginAccessRowStatus,
       "eqlLdapLoginAccessAdDomainName": eqlLdapLoginAccessAdDomainName,
       "eqlStorageGroupDnsSuffixTable": eqlStorageGroupDnsSuffixTable,
       "eqlStorageGroupDnsSuffixEntry": eqlStorageGroupDnsSuffixEntry,
       "eqlGroupDnsSuffixIndex": eqlGroupDnsSuffixIndex,
       "eqlGroupDnsSuffixRowStatus": eqlGroupDnsSuffixRowStatus,
       "eqlGroupDnsSuffixString": eqlGroupDnsSuffixString,
       "eqlGroupDnsSuffixConfigState": eqlGroupDnsSuffixConfigState,
       "eqlStorageGroupSnmpTable": eqlStorageGroupSnmpTable,
       "eqlStorageGroupSnmpEntry": eqlStorageGroupSnmpEntry,
       "eqlStorageGroupSnmpRowStatus": eqlStorageGroupSnmpRowStatus,
       "eqlStorageGroupSnmpManagersList": eqlStorageGroupSnmpManagersList,
       "eqlStorageGroupSnmpTrapCommunity": eqlStorageGroupSnmpTrapCommunity,
       "eqlGroupSessionBannerTable": eqlGroupSessionBannerTable,
       "eqlGroupSessionBannerEntry": eqlGroupSessionBannerEntry,
       "eqlGroupSessionBannerRowStatus": eqlGroupSessionBannerRowStatus,
       "eqlGroupSessionBannerText": eqlGroupSessionBannerText,
       "eqlGroupSingleSignOnStatusTable": eqlGroupSingleSignOnStatusTable,
       "eqlGroupSingleSignOnStatusEntry": eqlGroupSingleSignOnStatusEntry,
       "eqlGroupSingleSignOnStatus": eqlGroupSingleSignOnStatus,
       "eqlGroupSingleSignOnRegGroupName": eqlGroupSingleSignOnRegGroupName,
       "eqlGroupSingleSignOnKrbRealm": eqlGroupSingleSignOnKrbRealm,
       "eqlNextAvailableIndexTable": eqlNextAvailableIndexTable,
       "eqlNextAvailableIndexEntry": eqlNextAvailableIndexEntry,
       "eqlNextAvailableIndexTableType": eqlNextAvailableIndexTableType,
       "eqlNextAvailableIndexValue": eqlNextAvailableIndexValue,
       "eqlStorageGroupSnmpReadOnlyCommunityTable": eqlStorageGroupSnmpReadOnlyCommunityTable,
       "eqlStorageGroupSnmpReadOnlyCommunityEntry": eqlStorageGroupSnmpReadOnlyCommunityEntry,
       "eqlStorageGroupSnmpReadOnlyCommunity": eqlStorageGroupSnmpReadOnlyCommunity,
       "eqlEULAAcceptInfoTable": eqlEULAAcceptInfoTable,
       "eqlEULAAcceptInfoEntry": eqlEULAAcceptInfoEntry,
       "eqlEULAAcceptInfoFirmwareType": eqlEULAAcceptInfoFirmwareType,
       "eqlEULAAcceptInfoRowStatus": eqlEULAAcceptInfoRowStatus,
       "eqlEULAAcceptInfoAccountName": eqlEULAAcceptInfoAccountName,
       "eqlEULAAcceptInfoEULAVersion": eqlEULAAcceptInfoEULAVersion,
       "eqlEULAAcceptInfoTimestamp": eqlEULAAcceptInfoTimestamp,
       "eqlgroupNotifications": eqlgroupNotifications,
       "eqlgroupConformance": eqlgroupConformance}
)
