# SNMP MIB module (JUNIPER-NSM-TRAPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-NSM-TRAPS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:57 2024
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

(jnxNsm,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxNsm")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

nsmTrapInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsmTrap_ObjectIdentity = ObjectIdentity
nsmTrap = _NsmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 6, 0)
)
_NsmDayID_Type = Integer32
_NsmDayID_Object = MibScalar
nsmDayID = _NsmDayID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 1),
    _NsmDayID_Type()
)
nsmDayID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmDayID.setStatus("current")


class _NsmRecordID_Type(Integer32):
    """Custom type nsmRecordID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NsmRecordID_Type.__name__ = "Integer32"
_NsmRecordID_Object = MibScalar
nsmRecordID = _NsmRecordID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 2),
    _NsmRecordID_Type()
)
nsmRecordID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmRecordID.setStatus("current")
_NsmTimeReceived_Type = DateAndTime
_NsmTimeReceived_Object = MibScalar
nsmTimeReceived = _NsmTimeReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 3),
    _NsmTimeReceived_Type()
)
nsmTimeReceived.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmTimeReceived.setStatus("current")
_NsmTimeGenerated_Type = DateAndTime
_NsmTimeGenerated_Object = MibScalar
nsmTimeGenerated = _NsmTimeGenerated_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 4),
    _NsmTimeGenerated_Type()
)
nsmTimeGenerated.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmTimeGenerated.setStatus("current")
_NsmDeviceDomain_Type = DisplayString
_NsmDeviceDomain_Object = MibScalar
nsmDeviceDomain = _NsmDeviceDomain_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 5),
    _NsmDeviceDomain_Type()
)
nsmDeviceDomain.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmDeviceDomain.setStatus("current")
_NsmDeviceDomainVer2_Type = Integer32
_NsmDeviceDomainVer2_Object = MibScalar
nsmDeviceDomainVer2 = _NsmDeviceDomainVer2_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 6),
    _NsmDeviceDomainVer2_Type()
)
nsmDeviceDomainVer2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmDeviceDomainVer2.setStatus("current")
_NsmDevice_Type = DisplayString
_NsmDevice_Object = MibScalar
nsmDevice = _NsmDevice_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 7),
    _NsmDevice_Type()
)
nsmDevice.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmDevice.setStatus("current")
_NsmDeviceIp_Type = IpAddress
_NsmDeviceIp_Object = MibScalar
nsmDeviceIp = _NsmDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 8),
    _NsmDeviceIp_Type()
)
nsmDeviceIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmDeviceIp.setStatus("current")


class _NsmCategory_Type(Integer32):
    """Custom type nsmCategory based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("config", 1),
          ("custom", 7),
          ("implicit", 9),
          ("info", 4),
          ("predefined", 5),
          ("predefined1", 6),
          ("profiler", 10),
          ("screen", 8),
          ("self", 0),
          ("traffic", 2))
    )


_NsmCategory_Type.__name__ = "Integer32"
_NsmCategory_Object = MibScalar
nsmCategory = _NsmCategory_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 9),
    _NsmCategory_Type()
)
nsmCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmCategory.setStatus("current")
_NsmSubcategory_Type = DisplayString
_NsmSubcategory_Object = MibScalar
nsmSubcategory = _NsmSubcategory_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 10),
    _NsmSubcategory_Type()
)
nsmSubcategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmSubcategory.setStatus("current")
_NsmSrcZone_Type = DisplayString
_NsmSrcZone_Object = MibScalar
nsmSrcZone = _NsmSrcZone_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 11),
    _NsmSrcZone_Type()
)
nsmSrcZone.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmSrcZone.setStatus("current")
_NsmSrcIfName_Type = DisplayString
_NsmSrcIfName_Object = MibScalar
nsmSrcIfName = _NsmSrcIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 12),
    _NsmSrcIfName_Type()
)
nsmSrcIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmSrcIfName.setStatus("current")
_NsmSrcAddr_Type = IpAddress
_NsmSrcAddr_Object = MibScalar
nsmSrcAddr = _NsmSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 13),
    _NsmSrcAddr_Type()
)
nsmSrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmSrcAddr.setStatus("current")


class _NsmSrcPort_Type(Integer32):
    """Custom type nsmSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsmSrcPort_Type.__name__ = "Integer32"
_NsmSrcPort_Object = MibScalar
nsmSrcPort = _NsmSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 14),
    _NsmSrcPort_Type()
)
nsmSrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmSrcPort.setStatus("current")
_NsmNatSrcAddr_Type = IpAddress
_NsmNatSrcAddr_Object = MibScalar
nsmNatSrcAddr = _NsmNatSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 15),
    _NsmNatSrcAddr_Type()
)
nsmNatSrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmNatSrcAddr.setStatus("current")


class _NsmNatSrcPort_Type(Integer32):
    """Custom type nsmNatSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsmNatSrcPort_Type.__name__ = "Integer32"
_NsmNatSrcPort_Object = MibScalar
nsmNatSrcPort = _NsmNatSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 16),
    _NsmNatSrcPort_Type()
)
nsmNatSrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmNatSrcPort.setStatus("current")
_NsmDstZone_Type = DisplayString
_NsmDstZone_Object = MibScalar
nsmDstZone = _NsmDstZone_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 17),
    _NsmDstZone_Type()
)
nsmDstZone.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmDstZone.setStatus("current")
_NsmDstIfName_Type = DisplayString
_NsmDstIfName_Object = MibScalar
nsmDstIfName = _NsmDstIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 18),
    _NsmDstIfName_Type()
)
nsmDstIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmDstIfName.setStatus("current")
_NsmDstAddr_Type = IpAddress
_NsmDstAddr_Object = MibScalar
nsmDstAddr = _NsmDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 19),
    _NsmDstAddr_Type()
)
nsmDstAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmDstAddr.setStatus("current")


class _NsmDstPort_Type(Integer32):
    """Custom type nsmDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsmDstPort_Type.__name__ = "Integer32"
_NsmDstPort_Object = MibScalar
nsmDstPort = _NsmDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 20),
    _NsmDstPort_Type()
)
nsmDstPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmDstPort.setStatus("current")
_NsmNatDstAddr_Type = IpAddress
_NsmNatDstAddr_Object = MibScalar
nsmNatDstAddr = _NsmNatDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 21),
    _NsmNatDstAddr_Type()
)
nsmNatDstAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmNatDstAddr.setStatus("current")


class _NsmNatDstPort_Type(Integer32):
    """Custom type nsmNatDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsmNatDstPort_Type.__name__ = "Integer32"
_NsmNatDstPort_Object = MibScalar
nsmNatDstPort = _NsmNatDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 22),
    _NsmNatDstPort_Type()
)
nsmNatDstPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmNatDstPort.setStatus("current")


class _NsmProtocol_Type(Integer32):
    """Custom type nsmProtocol based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("a-n", 107),
          ("a3pc", 34),
          ("adfsp", 68),
          ("ah", 51),
          ("ahip", 61),
          ("alnp", 63),
          ("apes", 99),
          ("argus", 13),
          ("aris", 104),
          ("ax-25", 93),
          ("bbn-rcc-mon", 10),
          ("bn", 49),
          ("br-sat-mon", 76),
          ("cbt", 7),
          ("cftp", 62),
          ("chaos", 16),
          ("compat-peer", 110),
          ("cphb", 73),
          ("cpnx", 72),
          ("crtp", 126),
          ("crudp", 127),
          ("dcn-meas", 19),
          ("ddp", 37),
          ("ddx", 116),
          ("dgp", 86),
          ("egp", 8),
          ("eigrp", 88),
          ("emcon", 14),
          ("encap", 98),
          ("esp", 50),
          ("etherip", 97),
          ("fc", 133),
          ("fire", 125),
          ("ggp", 3),
          ("gmtp", 100),
          ("gre", 47),
          ("hmp", 20),
          ("hop-0", 114),
          ("hopopt", 0),
          ("i-nslp", 52),
          ("iatp", 117),
          ("icmp", 1),
          ("idpr-1", 35),
          ("idpr-2", 45),
          ("idpr-cmt", 38),
          ("ifmp", 101),
          ("igmp", 2),
          ("igp", 9),
          ("il", 40),
          ("ip", 4),
          ("ipcomp", 108),
          ("ipcv", 71),
          ("ipip", 94),
          ("iplt", 129),
          ("ippc", 67),
          ("ipv6", 41),
          ("ipv6-frag", 44),
          ("ipv6-icmp", 58),
          ("ipv6-nonxt", 59),
          ("ipv6-opts", 60),
          ("ipv6-route", 43),
          ("ipx-in-ip", 111),
          ("irtp", 28),
          ("isis", 124),
          ("iso-ip", 80),
          ("iso-tp4", 29),
          ("kryptolan", 65),
          ("l2tp", 115),
          ("larp", 91),
          ("leaf-1", 25),
          ("leaf-2", 26),
          ("merit-inp", 32),
          ("mfe-nsp", 31),
          ("mhrp", 48),
          ("micp", 95),
          ("mobile", 55),
          ("mtp", 92),
          ("mux", 18),
          ("narp", 54),
          ("netblt", 30),
          ("nsfnet-igp", 85),
          ("nvp-ii", 11),
          ("ospfigp", 89),
          ("pgm", 113),
          ("pim", 103),
          ("pipe", 131),
          ("pnni", 102),
          ("prm", 21),
          ("ptp", 123),
          ("pup", 12),
          ("pvp", 75),
          ("qnx", 106),
          ("rdp", 27),
          ("reserved", 255),
          ("rsvp", 46),
          ("rsvp-e2e-ignore", 134),
          ("rvd", 66),
          ("sat-expak", 64),
          ("sat-mon", 69),
          ("scc-sp", 96),
          ("scps", 105),
          ("sctp", 132),
          ("sdpr", 42),
          ("secure-vmtp", 82),
          ("sep", 33),
          ("skip", 57),
          ("smp", 121),
          ("snp", 109),
          ("sprite-rcp", 90),
          ("sps", 130),
          ("srp", 119),
          ("sscopmce", 128),
          ("ssm", 122),
          ("st", 5),
          ("stp", 118),
          ("sun-nd", 77),
          ("swipe", 53),
          ("tcf", 87),
          ("tcp", 6),
          ("tlsp", 56),
          ("tp-plusplus", 39),
          ("trunk-1", 23),
          ("trunk-2", 24),
          ("ttp", 84),
          ("udp", 17),
          ("uti", 120),
          ("vines", 83),
          ("visa", 70),
          ("vmpt", 81),
          ("vrrp", 112),
          ("wb-expak", 79),
          ("wb-mon", 78),
          ("wsn", 74),
          ("xnet", 15),
          ("xns-idp", 22),
          ("xtp", 36))
    )


_NsmProtocol_Type.__name__ = "Integer32"
_NsmProtocol_Object = MibScalar
nsmProtocol = _NsmProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 23),
    _NsmProtocol_Type()
)
nsmProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmProtocol.setStatus("current")
_NsmRuleDomain_Type = DisplayString
_NsmRuleDomain_Object = MibScalar
nsmRuleDomain = _NsmRuleDomain_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 24),
    _NsmRuleDomain_Type()
)
nsmRuleDomain.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmRuleDomain.setStatus("current")


class _NsmRuleDomainVer_Type(Integer32):
    """Custom type nsmRuleDomainVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NsmRuleDomainVer_Type.__name__ = "Integer32"
_NsmRuleDomainVer_Object = MibScalar
nsmRuleDomainVer = _NsmRuleDomainVer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 25),
    _NsmRuleDomainVer_Type()
)
nsmRuleDomainVer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmRuleDomainVer.setStatus("current")
_NsmPolicy_Type = DisplayString
_NsmPolicy_Object = MibScalar
nsmPolicy = _NsmPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 26),
    _NsmPolicy_Type()
)
nsmPolicy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmPolicy.setStatus("current")


class _NsmRulebase_Type(Integer32):
    """Custom type nsmRulebase based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("backdoor", 5),
          ("fw", 2),
          ("honeypot", 4),
          ("idp", 3),
          ("main", 1),
          ("mpolicy", 8),
          ("none", 0),
          ("synpro", 6),
          ("vpn", 7))
    )


_NsmRulebase_Type.__name__ = "Integer32"
_NsmRulebase_Object = MibScalar
nsmRulebase = _NsmRulebase_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 27),
    _NsmRulebase_Type()
)
nsmRulebase.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmRulebase.setStatus("current")


class _NsmRuleNumber_Type(Integer32):
    """Custom type nsmRuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsmRuleNumber_Type.__name__ = "Integer32"
_NsmRuleNumber_Object = MibScalar
nsmRuleNumber = _NsmRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 28),
    _NsmRuleNumber_Type()
)
nsmRuleNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmRuleNumber.setStatus("current")


class _NsmAction_Type(Integer32):
    """Custom type nsmAction based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("close", 3),
          ("close-client", 4),
          ("close-server", 5),
          ("dismiss", 7),
          ("drop", 2),
          ("drop-packet", 1),
          ("ignore", 6),
          ("not-set", 8))
    )


_NsmAction_Type.__name__ = "Integer32"
_NsmAction_Object = MibScalar
nsmAction = _NsmAction_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 29),
    _NsmAction_Type()
)
nsmAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmAction.setStatus("current")


class _NsmSeverity_Type(Integer32):
    """Custom type nsmSeverity based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 7),
          ("info", 2),
          ("major", 5),
          ("minor", 4),
          ("not-set", 0),
          ("unused1", 1),
          ("unused2", 6),
          ("warning", 3))
    )


_NsmSeverity_Type.__name__ = "Integer32"
_NsmSeverity_Object = MibScalar
nsmSeverity = _NsmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 30),
    _NsmSeverity_Type()
)
nsmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmSeverity.setStatus("current")
_NsmIsAlert_Type = TruthValue
_NsmIsAlert_Object = MibScalar
nsmIsAlert = _NsmIsAlert_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 31),
    _NsmIsAlert_Type()
)
nsmIsAlert.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmIsAlert.setStatus("current")
_NsmMisc_Type = DisplayString
_NsmMisc_Object = MibScalar
nsmMisc = _NsmMisc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 32),
    _NsmMisc_Type()
)
nsmMisc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmMisc.setStatus("current")
_NsmUser_Type = DisplayString
_NsmUser_Object = MibScalar
nsmUser = _NsmUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 33),
    _NsmUser_Type()
)
nsmUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmUser.setStatus("current")
_NsmApp_Type = DisplayString
_NsmApp_Object = MibScalar
nsmApp = _NsmApp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 34),
    _NsmApp_Type()
)
nsmApp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmApp.setStatus("current")
_NsmUri_Type = DisplayString
_NsmUri_Object = MibScalar
nsmUri = _NsmUri_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 35),
    _NsmUri_Type()
)
nsmUri.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmUri.setStatus("current")
_NsmElapsedSecs_Type = Integer32
_NsmElapsedSecs_Object = MibScalar
nsmElapsedSecs = _NsmElapsedSecs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 36),
    _NsmElapsedSecs_Type()
)
nsmElapsedSecs.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmElapsedSecs.setStatus("current")
_NsmBytesIn_Type = Integer32
_NsmBytesIn_Object = MibScalar
nsmBytesIn = _NsmBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 37),
    _NsmBytesIn_Type()
)
nsmBytesIn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmBytesIn.setStatus("current")
_NsmBytesOut_Type = Integer32
_NsmBytesOut_Object = MibScalar
nsmBytesOut = _NsmBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 38),
    _NsmBytesOut_Type()
)
nsmBytesOut.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmBytesOut.setStatus("current")
_NsmBytesTotal_Type = Integer32
_NsmBytesTotal_Object = MibScalar
nsmBytesTotal = _NsmBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 39),
    _NsmBytesTotal_Type()
)
nsmBytesTotal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmBytesTotal.setStatus("current")
_NsmPacketsIn_Type = Integer32
_NsmPacketsIn_Object = MibScalar
nsmPacketsIn = _NsmPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 40),
    _NsmPacketsIn_Type()
)
nsmPacketsIn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmPacketsIn.setStatus("current")
_NsmPacketsOut_Type = Integer32
_NsmPacketsOut_Object = MibScalar
nsmPacketsOut = _NsmPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 41),
    _NsmPacketsOut_Type()
)
nsmPacketsOut.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmPacketsOut.setStatus("current")
_NsmPacketsTotal_Type = Integer32
_NsmPacketsTotal_Object = MibScalar
nsmPacketsTotal = _NsmPacketsTotal_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 42),
    _NsmPacketsTotal_Type()
)
nsmPacketsTotal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmPacketsTotal.setStatus("current")
_NsmRepeatCount_Type = Integer32
_NsmRepeatCount_Object = MibScalar
nsmRepeatCount = _NsmRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 43),
    _NsmRepeatCount_Type()
)
nsmRepeatCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmRepeatCount.setStatus("current")
_NsmHasPacketData_Type = TruthValue
_NsmHasPacketData_Object = MibScalar
nsmHasPacketData = _NsmHasPacketData_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 44),
    _NsmHasPacketData_Type()
)
nsmHasPacketData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmHasPacketData.setStatus("current")


class _NsmVarDataEnum_Type(Integer32):
    """Custom type nsmVarDataEnum based on Integer32"""
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
        *(("aim", 37),
          ("arp", 15),
          ("attalarm", 45),
          ("bwmon", 32),
          ("dhcp", 29),
          ("dns", 17),
          ("finger", 18),
          ("ftp", 2),
          ("gnutella", 43),
          ("gnutella-v2", 23),
          ("gopher", 40),
          ("http", 7),
          ("icmp", 14),
          ("ident", 35),
          ("idp", 31),
          ("imap", 10),
          ("irc", 33),
          ("msn", 42),
          ("msn-v2", 21),
          ("msrpc-tcp", 5),
          ("msrpc-udp", 4),
          ("nfs", 44),
          ("nntp", 36),
          ("none", 0),
          ("pop3", 9),
          ("portmapper", 6),
          ("ptype", 19),
          ("rtsp", 12),
          ("rusers", 38),
          ("scan", 25),
          ("sip", 3),
          ("smb", 22),
          ("smtp", 8),
          ("tbd-24", 24),
          ("tbd-26", 26),
          ("tbd-27", 27),
          ("tbd-28", 28),
          ("tbd-30", 30),
          ("tbd-39", 39),
          ("tbd-41", 41),
          ("tcp", 16),
          ("telnet", 11),
          ("test", 1),
          ("whois", 13),
          ("ymsg", 34),
          ("ymsg-v2", 20))
    )


_NsmVarDataEnum_Type.__name__ = "Integer32"
_NsmVarDataEnum_Object = MibScalar
nsmVarDataEnum = _NsmVarDataEnum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 45),
    _NsmVarDataEnum_Type()
)
nsmVarDataEnum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmVarDataEnum.setStatus("current")
_NsmVarData_Type = OctetString
_NsmVarData_Object = MibScalar
nsmVarData = _NsmVarData_Object(
    (1, 3, 6, 1, 4, 1, 2636, 6, 1, 46),
    _NsmVarData_Type()
)
nsmVarData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsmVarData.setStatus("current")

# Managed Objects groups


# Notification objects

nsmTrapNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 6, 0, 1)
)
nsmTrapNotification.setObjects(
      *(("JUNIPER-NSM-TRAPS", "nsmDayID"),
        ("JUNIPER-NSM-TRAPS", "nsmRecordID"),
        ("JUNIPER-NSM-TRAPS", "nsmTimeReceived"),
        ("JUNIPER-NSM-TRAPS", "nsmTimeGenerated"),
        ("JUNIPER-NSM-TRAPS", "nsmDeviceDomain"),
        ("JUNIPER-NSM-TRAPS", "nsmDeviceDomainVer2"),
        ("JUNIPER-NSM-TRAPS", "nsmDevice"),
        ("JUNIPER-NSM-TRAPS", "nsmDeviceIp"),
        ("JUNIPER-NSM-TRAPS", "nsmCategory"),
        ("JUNIPER-NSM-TRAPS", "nsmSubcategory"),
        ("JUNIPER-NSM-TRAPS", "nsmSrcZone"),
        ("JUNIPER-NSM-TRAPS", "nsmSrcIfName"),
        ("JUNIPER-NSM-TRAPS", "nsmSrcAddr"),
        ("JUNIPER-NSM-TRAPS", "nsmSrcPort"),
        ("JUNIPER-NSM-TRAPS", "nsmNatSrcAddr"),
        ("JUNIPER-NSM-TRAPS", "nsmNatSrcPort"),
        ("JUNIPER-NSM-TRAPS", "nsmDstZone"),
        ("JUNIPER-NSM-TRAPS", "nsmDstIfName"),
        ("JUNIPER-NSM-TRAPS", "nsmDstAddr"),
        ("JUNIPER-NSM-TRAPS", "nsmDstPort"),
        ("JUNIPER-NSM-TRAPS", "nsmNatDstAddr"),
        ("JUNIPER-NSM-TRAPS", "nsmNatDstPort"),
        ("JUNIPER-NSM-TRAPS", "nsmProtocol"),
        ("JUNIPER-NSM-TRAPS", "nsmRuleDomain"),
        ("JUNIPER-NSM-TRAPS", "nsmRuleDomainVer"),
        ("JUNIPER-NSM-TRAPS", "nsmPolicy"),
        ("JUNIPER-NSM-TRAPS", "nsmRulebase"),
        ("JUNIPER-NSM-TRAPS", "nsmRuleNumber"),
        ("JUNIPER-NSM-TRAPS", "nsmAction"),
        ("JUNIPER-NSM-TRAPS", "nsmSeverity"),
        ("JUNIPER-NSM-TRAPS", "nsmIsAlert"),
        ("JUNIPER-NSM-TRAPS", "nsmMisc"),
        ("JUNIPER-NSM-TRAPS", "nsmUser"),
        ("JUNIPER-NSM-TRAPS", "nsmApp"),
        ("JUNIPER-NSM-TRAPS", "nsmUri"),
        ("JUNIPER-NSM-TRAPS", "nsmElapsedSecs"),
        ("JUNIPER-NSM-TRAPS", "nsmBytesIn"),
        ("JUNIPER-NSM-TRAPS", "nsmBytesOut"),
        ("JUNIPER-NSM-TRAPS", "nsmBytesTotal"),
        ("JUNIPER-NSM-TRAPS", "nsmPacketsIn"),
        ("JUNIPER-NSM-TRAPS", "nsmPacketsOut"),
        ("JUNIPER-NSM-TRAPS", "nsmPacketsTotal"),
        ("JUNIPER-NSM-TRAPS", "nsmRepeatCount"),
        ("JUNIPER-NSM-TRAPS", "nsmHasPacketData"),
        ("JUNIPER-NSM-TRAPS", "nsmVarDataEnum"))
)
if mibBuilder.loadTexts:
    nsmTrapNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-NSM-TRAPS",
    **{"nsmTrap": nsmTrap,
       "nsmTrapNotification": nsmTrapNotification,
       "nsmTrapInfo": nsmTrapInfo,
       "nsmDayID": nsmDayID,
       "nsmRecordID": nsmRecordID,
       "nsmTimeReceived": nsmTimeReceived,
       "nsmTimeGenerated": nsmTimeGenerated,
       "nsmDeviceDomain": nsmDeviceDomain,
       "nsmDeviceDomainVer2": nsmDeviceDomainVer2,
       "nsmDevice": nsmDevice,
       "nsmDeviceIp": nsmDeviceIp,
       "nsmCategory": nsmCategory,
       "nsmSubcategory": nsmSubcategory,
       "nsmSrcZone": nsmSrcZone,
       "nsmSrcIfName": nsmSrcIfName,
       "nsmSrcAddr": nsmSrcAddr,
       "nsmSrcPort": nsmSrcPort,
       "nsmNatSrcAddr": nsmNatSrcAddr,
       "nsmNatSrcPort": nsmNatSrcPort,
       "nsmDstZone": nsmDstZone,
       "nsmDstIfName": nsmDstIfName,
       "nsmDstAddr": nsmDstAddr,
       "nsmDstPort": nsmDstPort,
       "nsmNatDstAddr": nsmNatDstAddr,
       "nsmNatDstPort": nsmNatDstPort,
       "nsmProtocol": nsmProtocol,
       "nsmRuleDomain": nsmRuleDomain,
       "nsmRuleDomainVer": nsmRuleDomainVer,
       "nsmPolicy": nsmPolicy,
       "nsmRulebase": nsmRulebase,
       "nsmRuleNumber": nsmRuleNumber,
       "nsmAction": nsmAction,
       "nsmSeverity": nsmSeverity,
       "nsmIsAlert": nsmIsAlert,
       "nsmMisc": nsmMisc,
       "nsmUser": nsmUser,
       "nsmApp": nsmApp,
       "nsmUri": nsmUri,
       "nsmElapsedSecs": nsmElapsedSecs,
       "nsmBytesIn": nsmBytesIn,
       "nsmBytesOut": nsmBytesOut,
       "nsmBytesTotal": nsmBytesTotal,
       "nsmPacketsIn": nsmPacketsIn,
       "nsmPacketsOut": nsmPacketsOut,
       "nsmPacketsTotal": nsmPacketsTotal,
       "nsmRepeatCount": nsmRepeatCount,
       "nsmHasPacketData": nsmHasPacketData,
       "nsmVarDataEnum": nsmVarDataEnum,
       "nsmVarData": nsmVarData}
)
