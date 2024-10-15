# SNMP MIB module (MRV-IN-REACH-PRODUCT-DIVISION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-IN-REACH-PRODUCT-DIVISION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:35 2024
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


# Types definitions



class DateTime(OctetString):
    """Custom type DateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class AddressType(Integer32):
    """Custom type AddressType based on Integer32"""
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
        *(("ethernet", 5),
          ("ip", 4),
          ("local", 3),
          ("other", 2),
          ("unknown", 1))
    )





class TypedAddress(OctetString):
    """Custom type TypedAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )





class SoftwareType(Integer32):
    """Custom type SoftwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("bridge", 3),
          ("bridgeRouter", 5),
          ("bridgeRouterRepeater", 7),
          ("oem", 9),
          ("repeater", 4),
          ("router", 6),
          ("switch", 8),
          ("terminalServer", 1))
    )





class HardwareType(Integer32):
    """Custom type HardwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
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
              105,
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
              230)
        )
    )
    namedValues = NamedValues(
        *(("asy160", 91),
          ("br220", 93),
          ("br221", 95),
          ("br350", 105),
          ("br350ExpansionSlot", 107),
          ("br401", 80),
          ("br402", 109),
          ("br501", 103),
          ("br501c", 113),
          ("br501s", 112),
          ("br501sc", 114),
          ("dpXp1", 67),
          ("em1608", 29),
          ("etsmim", 62),
          ("fn1500", 66),
          ("ir7004", 132),
          ("ir7008", 133),
          ("ir7020", 32),
          ("ir7040", 126),
          ("ir7520", 30),
          ("ir8004", 134),
          ("ir8008", 135),
          ("ir8020", 130),
          ("ir8040", 131),
          ("ir9004", 139),
          ("ir9008", 140),
          ("ir9020", 31),
          ("ir9040", 125),
          ("ir9504", 141),
          ("irM700", 129),
          ("irM800", 128),
          ("irM900", 136),
          ("irMGR0AC", 137),
          ("irMGR0AC-IN", 138),
          ("irMgr0", 127),
          ("irMgr0Rdc", 124),
          ("lannetTs", 65),
          ("lb2Wan", 89),
          ("mx1100", 37),
          ("mx1120", 53),
          ("mx1400", 45),
          ("mx1450", 75),
          ("mx1500", 36),
          ("mx1500x8", 49),
          ("mx1520", 54),
          ("mx1600a", 74),
          ("mx1600b", 97),
          ("mx1600c", 98),
          ("mx1600d", 100),
          ("mx1604", 120),
          ("mx1608", 78),
          ("mx1608a", 117),
          ("mx1608b", 119),
          ("mx1620", 86),
          ("mx1640", 92),
          ("mx1710", 50),
          ("mx1800", 38),
          ("mx1820", 55),
          ("mx2120", 59),
          ("mx2210a", 79),
          ("mx2210b", 96),
          ("mx2220", 56),
          ("mx2240", 87),
          ("mx2710", 51),
          ("mx3010", 63),
          ("mx3210", 69),
          ("mx3510", 57),
          ("mx3610", 61),
          ("mx3710", 68),
          ("mx6020", 60),
          ("mx6025", 64),
          ("mx6220", 71),
          ("mx6510", 46),
          ("mx6625", 58),
          ("mx6710", 70),
          ("mx6800a", 81),
          ("mx6800b", 85),
          ("mx800a", 99),
          ("mx800b", 102),
          ("mxManF2", 35),
          ("mxNpcP1", 39),
          ("mxRb2", 47),
          ("mxTServJ8", 33),
          ("mxTservJ16", 34),
          ("mxTsrLJ16", 40),
          ("mxTsrvLJ8", 41),
          ("mxTsrvMj8", 42),
          ("mxTsrvNJ8", 43),
          ("mxTsrvOJ8", 44),
          ("n3000", 108),
          ("n3000Ias", 123),
          ("n3000SP", 230),
          ("nio1600", 90),
          ("notApplicable", 83),
          ("ps3m", 88),
          ("routeRunner", 116),
          ("routeRunnerIsdnSt", 115),
          ("routerRunnerIsdnU", 118),
          ("rp210", 84),
          ("rp211", 94),
          ("so3395aTs", 77),
          ("sw610", 110),
          ("sw610S", 111),
          ("tokenRing", 101),
          ("ts3395", 52),
          ("ts720", 76),
          ("unknown", 1))
    )





class ChassisType(Integer32):
    """Custom type ChassisType based on Integer32"""
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
        *(("mx45xx", 2),
          ("net9000", 3),
          ("net9000SWITCH", 4),
          ("other", 1))
    )





class IOType(Integer32):
    """Custom type IOType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              128,
              129,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              155,
              156,
              157,
              158,
              160,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
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
              207,
              209,
              210,
              214,
              224,
              225,
              226,
              227,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239)
        )
    )
    namedValues = NamedValues(
        *(("bri8", 34),
          ("dualE1120", 37),
          ("dualE175", 32),
          ("dualT1", 33),
          ("io101", 238),
          ("io119", 239),
          ("io201", 192),
          ("io201a", 202),
          ("io202", 193),
          ("io202a", 203),
          ("io203", 195),
          ("io203a", 204),
          ("io204", 194),
          ("io205", 210),
          ("io205x12", 209),
          ("io206", 199),
          ("io231", 197),
          ("io251", 196),
          ("io253", 200),
          ("io254", 198),
          ("io255", 214),
          ("io256", 201),
          ("io301x12", 160),
          ("io351d", 35),
          ("io352d", 36),
          ("io411", 226),
          ("io412", 234),
          ("io461", 237),
          ("io462", 233),
          ("io463x2", 191),
          ("io464x4", 190),
          ("io465x2", 189),
          ("io466x4", 188),
          ("io467x2", 185),
          ("io467x4", 184),
          ("io468x2", 187),
          ("io468x4", 186),
          ("io469x2", 183),
          ("io470x4", 182),
          ("io511x3", 177),
          ("io512x3", 176),
          ("io513", 180),
          ("io514", 179),
          ("io520", 178),
          ("io521", 174),
          ("io522", 175),
          ("io601", 144),
          ("io601A", 147),
          ("io602", 145),
          ("io602A", 148),
          ("io603", 146),
          ("io603A", 149),
          ("io604", 150),
          ("io616", 16),
          ("io621", 155),
          ("io622", 156),
          ("io623", 157),
          ("io624", 158),
          ("io625", 128),
          ("io626", 129),
          ("io721", 225),
          ("io722", 224),
          ("io723", 232),
          ("io724", 227),
          ("io725", 231),
          ("ioRepeater", 207),
          ("ioTS16a", 235),
          ("ioTS16b", 236),
          ("singleE1120", 40),
          ("singleE175", 39),
          ("singleT1", 38))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MrvInReachProductDivision_ObjectIdentity = ObjectIdentity
mrvInReachProductDivision = _MrvInReachProductDivision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33)
)
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8)
)
_TerminalServer_ObjectIdentity = ObjectIdentity
terminalServer = _TerminalServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1)
)
_TsMxCard1M_ObjectIdentity = ObjectIdentity
tsMxCard1M = _TsMxCard1M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 1)
)
_TsMxBox1M_ObjectIdentity = ObjectIdentity
tsMxBox1M = _TsMxBox1M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 2)
)
_TsMxCard_ObjectIdentity = ObjectIdentity
tsMxCard = _TsMxCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 3)
)
_TsMxBox_ObjectIdentity = ObjectIdentity
tsMxBox = _TsMxBox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 4)
)
_TsN9_ObjectIdentity = ObjectIdentity
tsN9 = _TsN9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 5)
)
_TsPrint_ObjectIdentity = ObjectIdentity
tsPrint = _TsPrint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 6)
)
_TsX25_ObjectIdentity = ObjectIdentity
tsX25 = _TsX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 7)
)
_Em1608_ObjectIdentity = ObjectIdentity
em1608 = _Em1608_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 29)
)
_Ir7520_ObjectIdentity = ObjectIdentity
ir7520 = _Ir7520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 30)
)
_Ir9020_ObjectIdentity = ObjectIdentity
ir9020 = _Ir9020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 31)
)
_Ir7020_ObjectIdentity = ObjectIdentity
ir7020 = _Ir7020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 32)
)
_IrMgr0Rdc_ObjectIdentity = ObjectIdentity
irMgr0Rdc = _IrMgr0Rdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 124)
)
_Ir9040_ObjectIdentity = ObjectIdentity
ir9040 = _Ir9040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 125)
)
_Ir7040_ObjectIdentity = ObjectIdentity
ir7040 = _Ir7040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 126)
)
_IrMgr0_ObjectIdentity = ObjectIdentity
irMgr0 = _IrMgr0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 127)
)
_IrM800_ObjectIdentity = ObjectIdentity
irM800 = _IrM800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 128)
)
_IrM700_ObjectIdentity = ObjectIdentity
irM700 = _IrM700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 129)
)
_Ir8020_ObjectIdentity = ObjectIdentity
ir8020 = _Ir8020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 130)
)
_Ir8040_ObjectIdentity = ObjectIdentity
ir8040 = _Ir8040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 131)
)
_Ir7004_ObjectIdentity = ObjectIdentity
ir7004 = _Ir7004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 132)
)
_Ir7008_ObjectIdentity = ObjectIdentity
ir7008 = _Ir7008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 133)
)
_Ir8004_ObjectIdentity = ObjectIdentity
ir8004 = _Ir8004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 134)
)
_Ir8008_ObjectIdentity = ObjectIdentity
ir8008 = _Ir8008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 135)
)
_IrM900_ObjectIdentity = ObjectIdentity
irM900 = _IrM900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 136)
)
_IrMGR0AC_ObjectIdentity = ObjectIdentity
irMGR0AC = _IrMGR0AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 137)
)
_IrMGR0AC_IN_ObjectIdentity = ObjectIdentity
irMGR0AC_IN = _IrMGR0AC_IN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 138)
)
_Ir9004_ObjectIdentity = ObjectIdentity
ir9004 = _Ir9004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 139)
)
_Ir9008_ObjectIdentity = ObjectIdentity
ir9008 = _Ir9008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 140)
)
_Ir9504_ObjectIdentity = ObjectIdentity
ir9504 = _Ir9504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 1, 141)
)
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 3)
)
_Repeater_ObjectIdentity = ObjectIdentity
repeater = _Repeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 4)
)
_RpMx_ObjectIdentity = ObjectIdentity
rpMx = _RpMx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 4, 1)
)
_RpN9_ObjectIdentity = ObjectIdentity
rpN9 = _RpN9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 4, 2)
)
_BridgeRouter_ObjectIdentity = ObjectIdentity
bridgeRouter = _BridgeRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 5)
)
_BridgeRouterMx_ObjectIdentity = ObjectIdentity
bridgeRouterMx = _BridgeRouterMx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 5, 1)
)
_BridgeRouterN9_ObjectIdentity = ObjectIdentity
bridgeRouterN9 = _BridgeRouterN9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 5, 2)
)
_BridgeRouterN3_ObjectIdentity = ObjectIdentity
bridgeRouterN3 = _BridgeRouterN3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 5, 3)
)
_BridgeRouterN2_ObjectIdentity = ObjectIdentity
bridgeRouterN2 = _BridgeRouterN2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 5, 4)
)
_BridgeRouterEB_ObjectIdentity = ObjectIdentity
bridgeRouterEB = _BridgeRouterEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 5, 5)
)
_BridgeRouterRepeater_ObjectIdentity = ObjectIdentity
bridgeRouterRepeater = _BridgeRouterRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 7)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 8)
)
_Oem_ObjectIdentity = ObjectIdentity
oem = _Oem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 9)
)
_NetVantage_ObjectIdentity = ObjectIdentity
netVantage = _NetVantage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 9, 1)
)
_Nv8516TT_ObjectIdentity = ObjectIdentity
nv8516TT = _Nv8516TT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 9, 1, 1)
)
_Nv8516FF_ObjectIdentity = ObjectIdentity
nv8516FF = _Nv8516FF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 9, 1, 2)
)
_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 10)
)
_NbaseSwitch_ObjectIdentity = ObjectIdentity
nbaseSwitch = _NbaseSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 10, 1)
)
_NbaseSwitchN9_ObjectIdentity = ObjectIdentity
nbaseSwitchN9 = _NbaseSwitchN9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 8, 10, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-IN-REACH-PRODUCT-DIVISION-MIB",
    **{"DateTime": DateTime,
       "AddressType": AddressType,
       "TypedAddress": TypedAddress,
       "SoftwareType": SoftwareType,
       "HardwareType": HardwareType,
       "ChassisType": ChassisType,
       "IOType": IOType,
       "mrvInReachProductDivision": mrvInReachProductDivision,
       "agent": agent,
       "terminalServer": terminalServer,
       "tsMxCard1M": tsMxCard1M,
       "tsMxBox1M": tsMxBox1M,
       "tsMxCard": tsMxCard,
       "tsMxBox": tsMxBox,
       "tsN9": tsN9,
       "tsPrint": tsPrint,
       "tsX25": tsX25,
       "em1608": em1608,
       "ir7520": ir7520,
       "ir9020": ir9020,
       "ir7020": ir7020,
       "irMgr0Rdc": irMgr0Rdc,
       "ir9040": ir9040,
       "ir7040": ir7040,
       "irMgr0": irMgr0,
       "irM800": irM800,
       "irM700": irM700,
       "ir8020": ir8020,
       "ir8040": ir8040,
       "ir7004": ir7004,
       "ir7008": ir7008,
       "ir8004": ir8004,
       "ir8008": ir8008,
       "irM900": irM900,
       "irMGR0AC": irMGR0AC,
       "irMGR0AC-IN": irMGR0AC_IN,
       "ir9004": ir9004,
       "ir9008": ir9008,
       "ir9504": ir9504,
       "bridge": bridge,
       "repeater": repeater,
       "rpMx": rpMx,
       "rpN9": rpN9,
       "bridgeRouter": bridgeRouter,
       "bridgeRouterMx": bridgeRouterMx,
       "bridgeRouterN9": bridgeRouterN9,
       "bridgeRouterN3": bridgeRouterN3,
       "bridgeRouterN2": bridgeRouterN2,
       "bridgeRouterEB": bridgeRouterEB,
       "bridgeRouterRepeater": bridgeRouterRepeater,
       "switch": switch,
       "oem": oem,
       "netVantage": netVantage,
       "nv8516TT": nv8516TT,
       "nv8516FF": nv8516FF,
       "nbase": nbase,
       "nbaseSwitch": nbaseSwitch,
       "nbaseSwitchN9": nbaseSwitchN9}
)
