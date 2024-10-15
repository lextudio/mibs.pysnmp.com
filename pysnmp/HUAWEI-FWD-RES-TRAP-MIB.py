# SNMP MIB module (HUAWEI-FWD-RES-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-FWD-RES-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:52 2024
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

(entPhysicalName,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalName")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwFwdResTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227)
)
hwFwdResTrapMIB.setRevisions(
        ("2015-10-14 11:23",
         "2015-10-12 21:00",
         "2015-10-12 21:00",
         "2015-10-12 15:00",
         "2015-10-12 15:00",
         "2015-10-08 17:50",
         "2015-09-25 17:50",
         "2015-09-22 20:10",
         "2015-09-22 19:20",
         "2015-09-17 19:20",
         "2015-08-04 19:20",
         "2015-06-24 17:23",
         "2015-06-23 14:32",
         "2015-06-17 16:20",
         "2015-06-09 15:20",
         "2015-05-22 09:50",
         "2015-05-08 09:50",
         "2015-05-08 09:50",
         "2015-05-08 09:50",
         "2015-05-05 14:20",
         "2015-05-05 14:20",
         "2015-04-16 22:00",
         "2015-04-16 21:50",
         "2015-04-08 21:50",
         "2015-03-31 21:50",
         "2015-03-31 21:50",
         "2015-03-31 21:50",
         "2015-03-28 09:50",
         "2015-02-07 10:11",
         "2014-11-18 13:58",
         "2014-10-28 18:46",
         "2014-10-23 10:47",
         "2014-10-23 10:47",
         "2014-10-17 15:47",
         "2014-10-17 15:47",
         "2014-09-25 10:58",
         "2014-09-25 10:58",
         "2014-09-25 10:58",
         "2014-09-25 10:58",
         "2014-09-03 15:01",
         "2014-08-30 11:56",
         "2014-08-22 10:10",
         "2014-08-19 10:01",
         "2014-08-06 16:39",
         "2014-07-31 19:22",
         "2014-07-28 19:47",
         "2014-07-28 16:55",
         "2014-07-26 17:14",
         "2014-07-26 15:38",
         "2014-07-21 15:54",
         "2014-07-16 21:35",
         "2014-07-15 19:35",
         "2014-07-11 08:29",
         "2014-07-08 17:29",
         "2014-06-09 08:44",
         "2014-06-05 14:59",
         "2014-05-30 14:50",
         "2014-05-21 10:00",
         "2014-03-08 16:00",
         "2014-03-05 15:26",
         "2014-01-23 16:57",
         "2014-01-21 11:40",
         "2014-01-14 21:46",
         "2014-01-06 19:52",
         "2013-12-12 17:28",
         "2013-11-13 10:28",
         "2013-05-14 11:21",
         "2013-05-14 11:21",
         "2010-06-04 10:43")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwFwdResTrapObject_ObjectIdentity = ObjectIdentity
hwFwdResTrapObject = _HwFwdResTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1)
)
_HwEntPhysicalindex_Type = Unsigned32
_HwEntPhysicalindex_Object = MibScalar
hwEntPhysicalindex = _HwEntPhysicalindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 1),
    _HwEntPhysicalindex_Type()
)
hwEntPhysicalindex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEntPhysicalindex.setStatus("current")
_HwFwdResLackSlotStr_Type = OctetString
_HwFwdResLackSlotStr_Object = MibScalar
hwFwdResLackSlotStr = _HwFwdResLackSlotStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 2),
    _HwFwdResLackSlotStr_Type()
)
hwFwdResLackSlotStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFwdResLackSlotStr.setStatus("current")


class _HwFwdResLackReasonId_Type(Integer32):
    """Custom type hwFwdResLackReasonId based on Integer32"""
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
              285,
              295,
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
              347)
        )
    )
    namedValues = NamedValues(
        *(("aclCarStat", 159),
          ("aclEntry", 61),
          ("aclEntryOutbound", 65),
          ("aclGroup", 62),
          ("aclGroupOutbound", 66),
          ("aclNhp", 133),
          ("aclNst", 148),
          ("aclRe", 132),
          ("aclResExceedThresHold", 212),
          ("apsRes", 255),
          ("apsResOverLoad", 270),
          ("arpNumLack", 76),
          ("arpNumOverLoad", 4),
          ("arpResExceedThresHold", 202),
          ("atIndex", 103),
          ("atmResExceedThresHold", 218),
          ("bfdGlobalIndex", 34),
          ("bfdIndex", 17),
          ("bfdRes", 188),
          ("bfdResExceedThresHold", 233),
          ("bfdaclNumLack", 82),
          ("bfdaclNumOverLoad", 10),
          ("bgp6ExtNum", 54),
          ("bgp6ExtNumLack", 91),
          ("bgpExtNum", 53),
          ("bgpExtNumLack", 90),
          ("bhvInCarExceedThresHold", 310),
          ("bhvOutCarExceedThresHold", 311),
          ("boardAclTCAMNumExhaust", 342),
          ("bridgeDomain", 185),
          ("carResExceedThresHold", 213),
          ("ccRecvNum", 43),
          ("ccSendNum", 42),
          ("cesResExceedThresHold", 219),
          ("chipinUserQueue", 257),
          ("chipouUserQueue", 258),
          ("comRull", 40),
          ("counter", 64),
          ("counterOutbound", 68),
          ("cpcarQueue", 254),
          ("cqWred", 250),
          ("dcnRes", 179),
          ("dcnResExceedThresHold", 237),
          ("defendResExceedThresHold", 238),
          ("devmResExceedThresHold", 221),
          ("dhcpsnpBindTableResOverLoad", 71),
          ("dhcpsnpResExceedThresHold", 240),
          ("diffservResExceedThresHold", 214),
          ("dp", 241),
          ("dpiRull", 39),
          ("dynLoadbNhpRes", 198),
          ("ecmpNextHopTable", 29),
          ("egressvlanxlateResOverLoad", 278),
          ("eoamRes", 181),
          ("erpsResExceed90ThresHold", 285),
          ("ethtestResExceedThresHold", 232),
          ("evcRes", 190),
          ("evpnResExceed90ThresHold", 301),
          ("evpnResOverLoad", 317),
          ("fesdrveResExceedThresHold", 217),
          ("fibArpFwdModeNumOverLoad", 73),
          ("fibResExceedThresHold", 201),
          ("fibv4NumExceedThresHold", 318),
          ("fibv4NumLack", 88),
          ("fibv4NumOverLoad", 2),
          ("fibv6NumExceedThresHold", 319),
          ("fibv6NumLack", 89),
          ("fibv6NumOverLoad", 3),
          ("flexQvctNum", 104),
          ("flexRes", 177),
          ("forwardvpnResOverLoad", 276),
          ("fvrfIndex", 14),
          ("fwdArp", 174),
          ("fwdBoardThresHoldToken", 99),
          ("fwdBoardToken", 94),
          ("fwdFibCheck", 175),
          ("fwdGlobal1ThresHoldToken", 98),
          ("fwdGlobal1Token", 93),
          ("fwdGlobal2ThresHoldToken", 100),
          ("fwdGlobal2Token", 95),
          ("fwdGlobal3ThresHoldToken", 101),
          ("fwdGlobal3Token", 96),
          ("fwdGlobal4ThresHoldToken", 102),
          ("fwdGlobal4Token", 97),
          ("fwdInAc", 168),
          ("fwdL2Entry", 171),
          ("fwdLem", 170),
          ("fwdMcMacfibv4", 172),
          ("fwdOutAc", 169),
          ("fwdSnoop", 173),
          ("fwdToken", 13),
          ("gid", 129),
          ("gidExceedThresHold", 307),
          ("greResExceedThresHold", 204),
          ("hostTablePrefixTable", 27),
          ("hqosResExceedThresHold", 211),
          ("imsResExceedThresHold", 235),
          ("inAclCar", 130),
          ("inAclStat", 157),
          ("inBehaviorSuppCar", 191),
          ("inCarRemark", 127),
          ("inFlowMapping", 107),
          ("inFlowQueueCbs", 111),
          ("inFlowQueuePbs", 113),
          ("inFlowQueueWfq", 109),
          ("inFlowWred", 105),
          ("inGQ", 121),
          ("inGQSshaper", 242),
          ("inGQTemp", 123),
          ("inGqResExceed90ThresHold", 343),
          ("inIFCarExceedThresHold", 305),
          ("inIPV4TCAMExceedThresHold", 312),
          ("inIPV4UCLTCAMExceedThresHold", 334),
          ("inIPV4UCLTCAMNumOverload", 338),
          ("inIPV6TCAMExceedThresHold", 314),
          ("inIPV6UCLTCAMExceedThresHold", 336),
          ("inIPV6UCLTCAMNumOverload", 340),
          ("inIPv4Acl", 134),
          ("inIPv6Acl", 135),
          ("inIfCar", 125),
          ("inIfCarStat", 160),
          ("inL2Acl", 162),
          ("inMirror", 140),
          ("inMirrorCapture", 142),
          ("inMirrorCar", 146),
          ("inProfSingleCar", 153),
          ("inProfSingleCarStat", 155),
          ("inProfSuppCar", 149),
          ("inProfSuppCarStat", 151),
          ("inQppbCar", 138),
          ("inRuleStatExceedThresHold", 308),
          ("inServiceTemp", 119),
          ("inSlotSqResExceed90ThresHold", 273),
          ("inSuppressCar", 144),
          ("inTmSqResExceed90ThresHold", 271),
          ("inUserQueue", 115),
          ("inUserQueueTemp", 117),
          ("inVI", 244),
          ("inVISshaper", 246),
          ("inVITemp", 248),
          ("incqServiceTemp", 251),
          ("ipfpmAclResOverLoad", 70),
          ("ipfpmRes", 196),
          ("ipfpmResExceedThresHold", 231),
          ("ipmcindex", 75),
          ("ipsecAclResOverLoad", 280),
          ("ipv4FullRull", 35),
          ("ipv4GreDecapsulationRes", 325),
          ("ipv4MaskRull", 36),
          ("ipv6FullRull", 37),
          ("ipv6GreDecapsulationRes", 326),
          ("ipv6MaskRull", 38),
          ("ipv6NdExceedThresHold", 320),
          ("ipv6NdNumLack", 77),
          ("ipv6NdNumOverLoad", 5),
          ("ipv6RoutingTablePrefixTable", 47),
          ("l2MfibNumExceed95ThresHold", 304),
          ("l2TrafLmt", 167),
          ("l2TrafLmtStat", 199),
          ("l2UserEntryOverload", 92),
          ("l2mcastResExceedThresHold", 200),
          ("l2mcindex", 74),
          ("l2tpv3ResExceed90ThresHold", 302),
          ("l2vpn", 183),
          ("l2vpnLinkLack", 80),
          ("l2vpnLinkOverLoad", 8),
          ("l3aclFailed", 72),
          ("l3mcastResExceedThresHold", 239),
          ("l3vpnResExceedThresHold", 203),
          ("largeExactlyMatchTable", 57),
          ("layer3InterfaceTable", 30),
          ("ldrResExceedThresHold", 206),
          ("linkEncap", 55),
          ("logicalInterface", 58),
          ("macMulticastIndex", 59),
          ("mainsubifRes", 178),
          ("mcMlidOverLoad", 25),
          ("mcOutIfNumOverload", 23),
          ("mcRepSerNumOverload", 22),
          ("mcTmgidOverLoad", 24),
          ("mcfibv4NumExceedThresHold", 321),
          ("mcfibv4NumLack", 83),
          ("mcfibv4NumOverLoad", 11),
          ("mcfibv6NumExceedThresHold", 322),
          ("mcfibv6NumLack", 84),
          ("mcfibv6NumOverLoad", 12),
          ("mcintNumLack", 81),
          ("mcintNumOverLoad", 9),
          ("mcv4StatId", 48),
          ("mcv6StatId", 49),
          ("meter", 63),
          ("meterOutbound", 67),
          ("mlpppResExceedThresHold", 220),
          ("mplsLdpStatResExceedThresHold", 347),
          ("mplsLinkLack", 87),
          ("mplsLinkOverLoad", 1),
          ("mplsResExceedThresHold", 205),
          ("mplsSRTELabelStackResExceedThresHold", 346),
          ("mplsSRTELabelStackResLack", 345),
          ("mplsvllResExceedThresHold", 208),
          ("multicastGroupExceed95ThresHold", 303),
          ("multicastIndex", 69),
          ("multioutlifResExceed90ThresHold", 295),
          ("ndIndex", 15),
          ("nextHopTable", 31),
          ("nhpNum", 50),
          ("nhpNumLack", 85),
          ("nqaResExceedThresHold", 226),
          ("nsIndex", 20),
          ("nscvmNum", 51),
          ("nscvmNumLack", 86),
          ("oam1agResExceedThresHold", 223),
          ("oam3ahResExceedThresHold", 225),
          ("oamRes", 256),
          ("oamResExceedThresHold", 222),
          ("oammaxResExceedThresHold", 234),
          ("outAclCar", 131),
          ("outAclStat", 158),
          ("outBehaviorSuppCar", 192),
          ("outCarRemark", 128),
          ("outFlowMapping", 108),
          ("outFlowQueueCbs", 112),
          ("outFlowQueuePbs", 114),
          ("outFlowQueueWfq", 110),
          ("outFlowWred", 106),
          ("outGQ", 122),
          ("outGQSshaper", 243),
          ("outGQTemp", 124),
          ("outGqResExceed90ThresHold", 344),
          ("outIFCarExceedThresHold", 306),
          ("outIPV4TCAMExceedThresHold", 313),
          ("outIPV4UCLTCAMExceedThresHold", 335),
          ("outIPV4UCLTCAMNumOverload", 339),
          ("outIPV6TCAMExceedThresHold", 315),
          ("outIPV6UCLTCAMExceedThresHold", 337),
          ("outIPV6UCLTCAMNumOverload", 341),
          ("outIPv4Acl", 136),
          ("outIPv6Acl", 137),
          ("outIfCar", 126),
          ("outIfCarStat", 161),
          ("outL2Acl", 163),
          ("outMirror", 141),
          ("outMirrorCapture", 143),
          ("outMirrorCar", 147),
          ("outProfSingleCar", 154),
          ("outProfSingleCarStat", 156),
          ("outProfSuppCar", 150),
          ("outProfSuppCarStat", 152),
          ("outQppbCar", 139),
          ("outRuleStatExceedThresHold", 309),
          ("outServiceTemp", 120),
          ("outSlotSqResExceed90ThresHold", 274),
          ("outSuppressCar", 145),
          ("outTmSqResExceed90ThresHold", 272),
          ("outUserQueue", 116),
          ("outUserQueueTemp", 118),
          ("outVI", 245),
          ("outVISshaper", 247),
          ("outVITemp", 249),
          ("outcqServiceTemp", 252),
          ("pbbBmacRes", 324),
          ("pbbResExceed90ThresHold", 328),
          ("pbbResOverLoad", 329),
          ("popgoRe", 253),
          ("protectgroupResOverLoad", 275),
          ("pwHqosOverLoad", 260),
          ("qinqRes", 189),
          ("qosNumLack", 79),
          ("qosNumOverLoad", 7),
          ("qppbAcl", 193),
          ("qppbGid", 194),
          ("qvctNumOverload", 33),
          ("remoteIntfRes", 323),
          ("resmResExceedThresHold", 216),
          ("rfc2544Res", 197),
          ("rfc2544ResExceedThresHold", 227),
          ("ringIndex", 21),
          ("routingTablePrefixTable", 28),
          ("sdResExceedThresHold", 228),
          ("semResOverLoad", 279),
          ("statNumLack", 78),
          ("statNumOverLoad", 6),
          ("statRes", 180),
          ("statResExceedThresHold", 215),
          ("tcamResExceedThresHold", 236),
          ("tcpFlagRull", 41),
          ("teResExceedThresHold", 207),
          ("tp1dmResExceedThresHold", 262),
          ("tp1dmResOverLoad", 266),
          ("tp2dmResExceedThresHold", 263),
          ("tp2dmResOverLoad", 267),
          ("tpDlmResExceedThresHold", 264),
          ("tpDlmResOverLoad", 268),
          ("tpSlmResExceedThresHold", 261),
          ("tpSlmResOverLoad", 265),
          ("tpapsResExceedThresHold", 230),
          ("tpoamCcResOverLoad", 269),
          ("tpoamResExceedThresHold", 229),
          ("trillMcOutIfNumOverload", 327),
          ("trillNhpIndex", 26),
          ("trunkDynAdjRes", 176),
          ("tunnelDecapsulationRes", 195),
          ("tunnelDecapsulationTable", 32),
          ("tunnelEncap", 56),
          ("tunnelIndex", 16),
          ("twampRes", 187),
          ("virtualPort", 60),
          ("vlan", 184),
          ("vlanxlateResOverLoad", 277),
          ("vllResExceedThresHold", 209),
          ("vplsLearnId", 18),
          ("vplsResExceed90ThresHold", 300),
          ("vplsResExceedThresHold", 210),
          ("vplsResOverLoad", 316),
          ("vrrpRes", 186),
          ("vsiIndex", 19),
          ("y1564Res", 182),
          ("y17311dmNum", 45),
          ("y17312dmNum", 46),
          ("y1731ResExceedThresHold", 224),
          ("y1731SlmNum", 44),
          ("y1731dlmNum", 52))
    )


_HwFwdResLackReasonId_Type.__name__ = "Integer32"
_HwFwdResLackReasonId_Object = MibScalar
hwFwdResLackReasonId = _HwFwdResLackReasonId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 3),
    _HwFwdResLackReasonId_Type()
)
hwFwdResLackReasonId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFwdResLackReasonId.setStatus("current")
_HwFwdResThreshold_Type = Unsigned32
_HwFwdResThreshold_Object = MibScalar
hwFwdResThreshold = _HwFwdResThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 4),
    _HwFwdResThreshold_Type()
)
hwFwdResThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFwdResThreshold.setStatus("current")


class _HwL3FailedService_Type(OctetString):
    """Custom type hwL3FailedService based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwL3FailedService_Type.__name__ = "OctetString"
_HwL3FailedService_Object = MibScalar
hwL3FailedService = _HwL3FailedService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 5),
    _HwL3FailedService_Type()
)
hwL3FailedService.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL3FailedService.setStatus("current")


class _HwCommand_Type(OctetString):
    """Custom type hwCommand based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwCommand_Type.__name__ = "OctetString"
_HwCommand_Object = MibScalar
hwCommand = _HwCommand_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 6),
    _HwCommand_Type()
)
hwCommand.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCommand.setStatus("current")


class _HwViewName_Type(OctetString):
    """Custom type hwViewName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwViewName_Type.__name__ = "OctetString"
_HwViewName_Object = MibScalar
hwViewName = _HwViewName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 7),
    _HwViewName_Type()
)
hwViewName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwViewName.setStatus("current")


class _HwReasonDescription_Type(OctetString):
    """Custom type hwReasonDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwReasonDescription_Type.__name__ = "OctetString"
_HwReasonDescription_Object = MibScalar
hwReasonDescription = _HwReasonDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 8),
    _HwReasonDescription_Type()
)
hwReasonDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwReasonDescription.setStatus("current")
_HwFwdResLackVrId_Type = Unsigned32
_HwFwdResLackVrId_Object = MibScalar
hwFwdResLackVrId = _HwFwdResLackVrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 9),
    _HwFwdResLackVrId_Type()
)
hwFwdResLackVrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFwdResLackVrId.setStatus("current")


class _HwFwdProcFailForLCSOperationId_Type(Integer32):
    """Custom type hwFwdProcFailForLCSOperationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("l3vpnFibDownloadFailed", 1)
    )


_HwFwdProcFailForLCSOperationId_Type.__name__ = "Integer32"
_HwFwdProcFailForLCSOperationId_Object = MibScalar
hwFwdProcFailForLCSOperationId = _HwFwdProcFailForLCSOperationId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 10),
    _HwFwdProcFailForLCSOperationId_Type()
)
hwFwdProcFailForLCSOperationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFwdProcFailForLCSOperationId.setStatus("current")


class _HwFwdLicenseName_Type(OctetString):
    """Custom type hwFwdLicenseName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwFwdLicenseName_Type.__name__ = "OctetString"
_HwFwdLicenseName_Object = MibScalar
hwFwdLicenseName = _HwFwdLicenseName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 11),
    _HwFwdLicenseName_Type()
)
hwFwdLicenseName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFwdLicenseName.setStatus("current")
_HwFwdResTable_Object = MibTable
hwFwdResTable = _HwFwdResTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 12)
)
if mibBuilder.loadTexts:
    hwFwdResTable.setStatus("current")
_HwFwdResEntry_Object = MibTableRow
hwFwdResEntry = _HwFwdResEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 12, 1)
)
hwFwdResEntry.setIndexNames(
    (0, "HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResDevName"),
)
if mibBuilder.loadTexts:
    hwFwdResEntry.setStatus("current")


class _HwFwdResDevName_Type(OctetString):
    """Custom type hwFwdResDevName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwFwdResDevName_Type.__name__ = "OctetString"
_HwFwdResDevName_Object = MibTableColumn
hwFwdResDevName = _HwFwdResDevName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 12, 1, 1),
    _HwFwdResDevName_Type()
)
hwFwdResDevName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFwdResDevName.setStatus("current")
_HwFwdResLimit_Type = Unsigned32
_HwFwdResLimit_Object = MibTableColumn
hwFwdResLimit = _HwFwdResLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 12, 1, 2),
    _HwFwdResLimit_Type()
)
hwFwdResLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFwdResLimit.setStatus("current")
_HwFwdResCurThroughput_Type = Counter64
_HwFwdResCurThroughput_Object = MibTableColumn
hwFwdResCurThroughput = _HwFwdResCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 1, 12, 1, 3),
    _HwFwdResCurThroughput_Type()
)
hwFwdResCurThroughput.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFwdResCurThroughput.setStatus("current")
_HwFwdResTraps_ObjectIdentity = ObjectIdentity
hwFwdResTraps = _HwFwdResTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2)
)
_HwFwdResLacTrap_ObjectIdentity = ObjectIdentity
hwFwdResLacTrap = _HwFwdResLacTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1)
)
_HwFwdProcFailForLCSTrap_ObjectIdentity = ObjectIdentity
hwFwdProcFailForLCSTrap = _HwFwdProcFailForLCSTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 2)
)
_HwFwdEntryConflictTrap_ObjectIdentity = ObjectIdentity
hwFwdEntryConflictTrap = _HwFwdEntryConflictTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 3)
)
_HwFwdResTrapConformance_ObjectIdentity = ObjectIdentity
hwFwdResTrapConformance = _HwFwdResTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 3)
)
_HwFwdResTrapCompliances_ObjectIdentity = ObjectIdentity
hwFwdResTrapCompliances = _HwFwdResTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 3, 1)
)
_HwFwdResTrapGroups_ObjectIdentity = ObjectIdentity
hwFwdResTrapGroups = _HwFwdResTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 3, 2)
)

# Managed Objects groups

hwFwdResObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 3, 2, 1)
)
hwFwdResObjectGroup.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwEntPhysicalindex"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResThreshold"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwL3FailedService"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwCommand"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwViewName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwReasonDescription"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackVrId"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdProcFailForLCSOperationId"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdLicenseName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResDevName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLimit"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResCurThroughput"))
)
if mibBuilder.loadTexts:
    hwFwdResObjectGroup.setStatus("current")


# Notification objects

hwWholeFwdResLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 1)
)
hwWholeFwdResLack.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwEntPhysicalindex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwWholeFwdResLack.setStatus(
        "current"
    )

hwWholeFwdResLackResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 2)
)
hwWholeFwdResLackResume.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwEntPhysicalindex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwWholeFwdResLackResume.setStatus(
        "current"
    )

hwBoardFwdResLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 3)
)
hwBoardFwdResLack.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwEntPhysicalindex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwBoardFwdResLack.setStatus(
        "current"
    )

hwBoardFwdResLackResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 4)
)
hwBoardFwdResLackResume.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwEntPhysicalindex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwBoardFwdResLackResume.setStatus(
        "current"
    )

hwBoardL3FwdResLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 5)
)
hwBoardL3FwdResLack.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResThreshold"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwEntPhysicalindex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwBoardL3FwdResLack.setStatus(
        "current"
    )

hwBoardL3FwdResLackResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 6)
)
hwBoardL3FwdResLackResume.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResThreshold"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwEntPhysicalindex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwBoardL3FwdResLackResume.setStatus(
        "current"
    )

hwBoardL3ACLResLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 7)
)
hwBoardL3ACLResLack.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwL3FailedService"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwBoardL3ACLResLack.setStatus(
        "current"
    )

hwBoardL2mcResLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 8)
)
hwBoardL2mcResLack.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResThreshold"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwBoardL2mcResLack.setStatus(
        "current"
    )

hwBoardL2mcResLackResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 9)
)
hwBoardL2mcResLackResume.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResThreshold"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwBoardL2mcResLackResume.setStatus(
        "current"
    )

hwBoardIpmcResLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 10)
)
hwBoardIpmcResLack.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResThreshold"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwBoardIpmcResLack.setStatus(
        "current"
    )

hwBoardIpmcResLackResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 11)
)
hwBoardIpmcResLackResume.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResThreshold"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwBoardIpmcResLackResume.setStatus(
        "current"
    )

hwBoardServiceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 12)
)
hwBoardServiceFailed.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwCommand"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwViewName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwReasonDescription"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"))
)
if mibBuilder.loadTexts:
    hwBoardServiceFailed.setStatus(
        "current"
    )

hwWholeFwdResThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 13)
)
hwWholeFwdResThresholdExceed.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwEntPhysicalindex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwWholeFwdResThresholdExceed.setStatus(
        "current"
    )

hwWholeFwdResThresholdExceedResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 14)
)
hwWholeFwdResThresholdExceedResume.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwEntPhysicalindex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwWholeFwdResThresholdExceedResume.setStatus(
        "current"
    )

hwBoardFwdResThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 15)
)
hwBoardFwdResThresholdExceed.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwEntPhysicalindex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwBoardFwdResThresholdExceed.setStatus(
        "current"
    )

hwBoardFwdResThresholdExceedResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 16)
)
hwBoardFwdResThresholdExceedResume.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwEntPhysicalindex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwBoardFwdResThresholdExceedResume.setStatus(
        "current"
    )

hwBoardMplsPhpNonsupport = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 17)
)
hwBoardMplsPhpNonsupport.setObjects(
    ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr")
)
if mibBuilder.loadTexts:
    hwBoardMplsPhpNonsupport.setStatus(
        "current"
    )

hwBoardResThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 18)
)
hwBoardResThresholdExceed.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResThreshold"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwReasonDescription"))
)
if mibBuilder.loadTexts:
    hwBoardResThresholdExceed.setStatus(
        "current"
    )

hwBoardResThresholdExceedResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 19)
)
hwBoardResThresholdExceedResume.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResThreshold"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwReasonDescription"))
)
if mibBuilder.loadTexts:
    hwBoardResThresholdExceedResume.setStatus(
        "current"
    )

hwBoardResWarningThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 20)
)
hwBoardResWarningThresholdExceed.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResThreshold"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwReasonDescription"))
)
if mibBuilder.loadTexts:
    hwBoardResWarningThresholdExceed.setStatus(
        "current"
    )

hwBoardResWarningThresholdExceedResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 21)
)
hwBoardResWarningThresholdExceedResume.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResThreshold"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwReasonDescription"))
)
if mibBuilder.loadTexts:
    hwBoardResWarningThresholdExceedResume.setStatus(
        "current"
    )

hwBoardIPv6ACLResLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 22)
)
hwBoardIPv6ACLResLack.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwViewName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"))
)
if mibBuilder.loadTexts:
    hwBoardIPv6ACLResLack.setStatus(
        "current"
    )

hwBoardMplsPhpResLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 23)
)
hwBoardMplsPhpResLack.setObjects(
    ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr")
)
if mibBuilder.loadTexts:
    hwBoardMplsPhpResLack.setStatus(
        "current"
    )

hwBoardMplsNonSupport = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 24)
)
hwBoardMplsNonSupport.setObjects(
    ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr")
)
if mibBuilder.loadTexts:
    hwBoardMplsNonSupport.setStatus(
        "current"
    )

hwBoardMplsFwdResLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 25)
)
hwBoardMplsFwdResLack.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwEntPhysicalindex"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResThreshold"))
)
if mibBuilder.loadTexts:
    hwBoardMplsFwdResLack.setStatus(
        "current"
    )

hwBoardMplsFwdResLackResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 26)
)
hwBoardMplsFwdResLackResume.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwEntPhysicalindex"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResThreshold"))
)
if mibBuilder.loadTexts:
    hwBoardMplsFwdResLackResume.setStatus(
        "current"
    )

hwFwdResOverLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 27)
)
hwFwdResOverLimit.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLimit"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResCurThroughput"))
)
if mibBuilder.loadTexts:
    hwFwdResOverLimit.setStatus(
        "current"
    )

hwFwdResOverLimitResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 28)
)
hwFwdResOverLimitResume.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLimit"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResCurThroughput"))
)
if mibBuilder.loadTexts:
    hwFwdResOverLimitResume.setStatus(
        "current"
    )

hwFwdResOverThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 29)
)
hwFwdResOverThresh.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLimit"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResCurThroughput"))
)
if mibBuilder.loadTexts:
    hwFwdResOverThresh.setStatus(
        "current"
    )

hwFwdResOverThreshResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 1, 30)
)
hwFwdResOverThreshResume.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLimit"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResCurThroughput"))
)
if mibBuilder.loadTexts:
    hwFwdResOverThreshResume.setStatus(
        "current"
    )

hwFwdProcFailForLCS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 2, 1)
)
hwFwdProcFailForLCS.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdLicenseName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdProcFailForLCSOperationId"))
)
if mibBuilder.loadTexts:
    hwFwdProcFailForLCS.setStatus(
        "current"
    )

hwFwdProcFailForLCSResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 2, 2)
)
hwFwdProcFailForLCSResume.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdLicenseName"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdProcFailForLCSOperationId"))
)
if mibBuilder.loadTexts:
    hwFwdProcFailForLCSResume.setStatus(
        "current"
    )

hwFwdEntryConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 3, 1)
)
hwFwdEntryConflict.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwFwdEntryConflict.setStatus(
        "current"
    )

hwFwdEntryConflictResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 2, 3, 2)
)
hwFwdEntryConflictResume.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackSlotStr"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResLackReasonId"))
)
if mibBuilder.loadTexts:
    hwFwdEntryConflictResume.setStatus(
        "current"
    )


# Notifications groups

hwFwdResTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 3, 2, 2)
)
hwFwdResTrapGroup.setObjects(
      *(("HUAWEI-FWD-RES-TRAP-MIB", "hwWholeFwdResLack"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwWholeFwdResLackResume"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardFwdResLack"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardFwdResLackResume"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardL3FwdResLack"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardL3FwdResLackResume"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardL3ACLResLack"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardL2mcResLack"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardL2mcResLackResume"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardIpmcResLack"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardIpmcResLackResume"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardServiceFailed"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwWholeFwdResThresholdExceed"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwWholeFwdResThresholdExceedResume"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardFwdResThresholdExceed"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardFwdResThresholdExceedResume"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardMplsPhpNonsupport"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardResThresholdExceed"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardResThresholdExceedResume"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardResWarningThresholdExceed"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardResWarningThresholdExceedResume"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwBoardIPv6ACLResLack"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdProcFailForLCS"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdProcFailForLCSResume"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdEntryConflict"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdEntryConflictResume"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResOverLimit"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResOverLimitResume"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResOverThresh"),
        ("HUAWEI-FWD-RES-TRAP-MIB", "hwFwdResOverThreshResume"))
)
if mibBuilder.loadTexts:
    hwFwdResTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwFwdResTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 227, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwFwdResTrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-FWD-RES-TRAP-MIB",
    **{"hwFwdResTrapMIB": hwFwdResTrapMIB,
       "hwFwdResTrapObject": hwFwdResTrapObject,
       "hwEntPhysicalindex": hwEntPhysicalindex,
       "hwFwdResLackSlotStr": hwFwdResLackSlotStr,
       "hwFwdResLackReasonId": hwFwdResLackReasonId,
       "hwFwdResThreshold": hwFwdResThreshold,
       "hwL3FailedService": hwL3FailedService,
       "hwCommand": hwCommand,
       "hwViewName": hwViewName,
       "hwReasonDescription": hwReasonDescription,
       "hwFwdResLackVrId": hwFwdResLackVrId,
       "hwFwdProcFailForLCSOperationId": hwFwdProcFailForLCSOperationId,
       "hwFwdLicenseName": hwFwdLicenseName,
       "hwFwdResTable": hwFwdResTable,
       "hwFwdResEntry": hwFwdResEntry,
       "hwFwdResDevName": hwFwdResDevName,
       "hwFwdResLimit": hwFwdResLimit,
       "hwFwdResCurThroughput": hwFwdResCurThroughput,
       "hwFwdResTraps": hwFwdResTraps,
       "hwFwdResLacTrap": hwFwdResLacTrap,
       "hwWholeFwdResLack": hwWholeFwdResLack,
       "hwWholeFwdResLackResume": hwWholeFwdResLackResume,
       "hwBoardFwdResLack": hwBoardFwdResLack,
       "hwBoardFwdResLackResume": hwBoardFwdResLackResume,
       "hwBoardL3FwdResLack": hwBoardL3FwdResLack,
       "hwBoardL3FwdResLackResume": hwBoardL3FwdResLackResume,
       "hwBoardL3ACLResLack": hwBoardL3ACLResLack,
       "hwBoardL2mcResLack": hwBoardL2mcResLack,
       "hwBoardL2mcResLackResume": hwBoardL2mcResLackResume,
       "hwBoardIpmcResLack": hwBoardIpmcResLack,
       "hwBoardIpmcResLackResume": hwBoardIpmcResLackResume,
       "hwBoardServiceFailed": hwBoardServiceFailed,
       "hwWholeFwdResThresholdExceed": hwWholeFwdResThresholdExceed,
       "hwWholeFwdResThresholdExceedResume": hwWholeFwdResThresholdExceedResume,
       "hwBoardFwdResThresholdExceed": hwBoardFwdResThresholdExceed,
       "hwBoardFwdResThresholdExceedResume": hwBoardFwdResThresholdExceedResume,
       "hwBoardMplsPhpNonsupport": hwBoardMplsPhpNonsupport,
       "hwBoardResThresholdExceed": hwBoardResThresholdExceed,
       "hwBoardResThresholdExceedResume": hwBoardResThresholdExceedResume,
       "hwBoardResWarningThresholdExceed": hwBoardResWarningThresholdExceed,
       "hwBoardResWarningThresholdExceedResume": hwBoardResWarningThresholdExceedResume,
       "hwBoardIPv6ACLResLack": hwBoardIPv6ACLResLack,
       "hwBoardMplsPhpResLack": hwBoardMplsPhpResLack,
       "hwBoardMplsNonSupport": hwBoardMplsNonSupport,
       "hwBoardMplsFwdResLack": hwBoardMplsFwdResLack,
       "hwBoardMplsFwdResLackResume": hwBoardMplsFwdResLackResume,
       "hwFwdResOverLimit": hwFwdResOverLimit,
       "hwFwdResOverLimitResume": hwFwdResOverLimitResume,
       "hwFwdResOverThresh": hwFwdResOverThresh,
       "hwFwdResOverThreshResume": hwFwdResOverThreshResume,
       "hwFwdProcFailForLCSTrap": hwFwdProcFailForLCSTrap,
       "hwFwdProcFailForLCS": hwFwdProcFailForLCS,
       "hwFwdProcFailForLCSResume": hwFwdProcFailForLCSResume,
       "hwFwdEntryConflictTrap": hwFwdEntryConflictTrap,
       "hwFwdEntryConflict": hwFwdEntryConflict,
       "hwFwdEntryConflictResume": hwFwdEntryConflictResume,
       "hwFwdResTrapConformance": hwFwdResTrapConformance,
       "hwFwdResTrapCompliances": hwFwdResTrapCompliances,
       "hwFwdResTrapCompliance": hwFwdResTrapCompliance,
       "hwFwdResTrapGroups": hwFwdResTrapGroups,
       "hwFwdResObjectGroup": hwFwdResObjectGroup,
       "hwFwdResTrapGroup": hwFwdResTrapGroup}
)
