# SNMP MIB module (BTI7800-EQUIPMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BTI7800-EQUIPMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:55 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

bTI7800_EQUIPMENT_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1)
)
bTI7800_EQUIPMENT_MIB.setRevisions(
        ("2012-06-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class Ipv4Prefix(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d/1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )



class InetAddressIP(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class String(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class CurrentDBStateType(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("backup-inprogress", 2),
          ("clear-failed", 14),
          ("clear-inprogress", 12),
          ("clear-success", 13),
          ("ready-to-backup", 1),
          ("ready-to-remove", 8),
          ("ready-to-restore", 3),
          ("remove-failed", 11),
          ("remove-inprogress", 9),
          ("remove-success", 10),
          ("restore-failed", 6),
          ("restore-inprogress", 4),
          ("restore-success", 5))
    )



class BicType(Integer32, TextualConvention):
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
        *(("cfp-bic", 2),
          ("qsfp-bic", 3),
          ("qsfp28-bic", 4),
          ("sfp-bic", 1))
    )



class DolOchIdType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class ObsoleteName(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class UfmType(Integer32, TextualConvention):
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
        *(("dual-bic-non-switching", 1),
          ("dual-bic-switching", 0),
          ("msa-non-switching", 3),
          ("msa-switching", 2),
          ("msa400-10g-100g-client", 5),
          ("msa400-10g-client", 4))
    )



class AmpModule(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class TransportType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1))
    )



class Role(Integer32, TextualConvention):
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
        *(("btiuser", 0),
          ("provisioning", 1),
          ("superuser", 2),
          ("surveillance", 3))
    )



class DolFconnEndpt1Type(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class DolFconnEndpt2Type(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class DebugLevel(Integer32, TextualConvention):
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
        *(("debug", 2),
          ("off", 3),
          ("trace", 1))
    )



class FeGroupNum(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class PasswdStr(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class RoadmType(Integer32, TextualConvention):
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
        *(("a2-port", 0),
          ("a20-port", 2),
          ("a9-port", 1))
    )



class StatisticPointType(Integer32, TextualConvention):
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
              228)
        )
    )
    namedValues = NamedValues(
        *(("apr", 167),
          ("apr-avg", 170),
          ("apr-max", 169),
          ("apr-min", 168),
          ("apr-std-avg", 171),
          ("bcast-pkts-rx", 95),
          ("bcast-pkts-tx", 96),
          ("ber-avg-l", 144),
          ("ber-avg-s", 135),
          ("ber-l", 141),
          ("ber-max-l", 143),
          ("ber-max-s", 134),
          ("ber-min-l", 142),
          ("ber-min-s", 133),
          ("ber-s", 132),
          ("cd", 39),
          ("cd-avg", 42),
          ("cd-max", 41),
          ("cd-min", 40),
          ("cfo", 47),
          ("cfo-avg", 50),
          ("cfo-max", 49),
          ("cfo-min", 48),
          ("cpu-load-avg", 164),
          ("cpu-load-max", 166),
          ("cpu-load-min", 165),
          ("cv-l", 136),
          ("cv-s", 127),
          ("dgd", 51),
          ("dgd-avg", 54),
          ("dgd-max", 53),
          ("dgd-min", 52),
          ("drp-pkts-rx", 101),
          ("drp-pkts-tx", 102),
          ("es-l", 137),
          ("es-s", 128),
          ("fan-rpm-avg", 178),
          ("fan-rpm-max", 180),
          ("fan-rpm-min", 179),
          ("fc-l", 140),
          ("fcse-pkts-rx", 99),
          ("fcse-pkts-tx", 100),
          ("fec-0cr", 31),
          ("fec-1cr", 30),
          ("fec-ber", 35),
          ("fec-ber-avg", 38),
          ("fec-ber-max", 37),
          ("fec-ber-min", 36),
          ("fec-bitcr", 32),
          ("fec-symcr", 33),
          ("fec-ucrcw", 34),
          ("fragments-rx", 107),
          ("fragments-tx", 108),
          ("ip-octs-rx", 205),
          ("ip-octs-tx", 206),
          ("ip-pkts-rx", 203),
          ("ip-pkts-tx", 204),
          ("ipv4-dip0-excp", 199),
          ("ipv4-hdr-chksum-excp", 211),
          ("ipv4-ihl-excp", 195),
          ("ipv4-mpls-ttl0-excp", 201),
          ("ipv4-mpls-ttl1-excp", 202),
          ("ipv4-pkt-len-excp", 196),
          ("ipv4-rx-ttl0-excp", 197),
          ("ipv4-sip-eq-dip-excp", 198),
          ("ipv4-sip-mc-excp", 200),
          ("jabbers-rx", 109),
          ("jabbers-tx", 110),
          ("lbc", 18),
          ("lbc-avg", 21),
          ("lbc-max", 20),
          ("lbc-min", 19),
          ("ltemp", 14),
          ("ltemp-avg", 17),
          ("ltemp-max", 16),
          ("ltemp-min", 15),
          ("mcast-pkts-rx", 97),
          ("mcast-pkts-tx", 98),
          ("mod-temp", 26),
          ("mod-temp-avg", 29),
          ("mod-temp-max", 28),
          ("mod-temp-min", 27),
          ("mpls-octs-rx", 209),
          ("mpls-octs-tx", 210),
          ("mpls-pkts-rx", 207),
          ("mpls-pkts-tx", 208),
          ("ms-bbe", 156),
          ("ms-ber", 160),
          ("ms-ber-avg", 163),
          ("ms-ber-max", 162),
          ("ms-ber-min", 161),
          ("ms-eb", 155),
          ("ms-es", 157),
          ("ms-ses", 158),
          ("ms-uas", 159),
          ("octs-ok-rx", 89),
          ("octs-ok-tx", 90),
          ("octs-rx", 87),
          ("octs-tx", 88),
          ("odu-bbe", 66),
          ("odu-ber", 70),
          ("odu-ber-avg", 73),
          ("odu-ber-max", 72),
          ("odu-ber-min", 71),
          ("odu-eb", 65),
          ("odu-es", 67),
          ("odu-lat", 74),
          ("odu-lat-avg", 77),
          ("odu-lat-max", 76),
          ("odu-lat-min", 75),
          ("odu-ses", 68),
          ("odu-uas", 69),
          ("opl-rx", 12),
          ("opl-rx-avg", 174),
          ("opl-rx-max", 173),
          ("opl-rx-min", 172),
          ("opl-tx", 13),
          ("opl-tx-avg", 177),
          ("opl-tx-max", 176),
          ("opl-tx-min", 175),
          ("opr", 1),
          ("opr-avg", 4),
          ("opr-max", 3),
          ("opr-min", 2),
          ("opr-std-avg", 10),
          ("opt", 5),
          ("opt-avg", 8),
          ("opt-back-ref-power", 9),
          ("opt-back-ref-ratio", 224),
          ("opt-back-ref-ratio-avg", 227),
          ("opt-back-ref-ratio-max", 226),
          ("opt-back-ref-ratio-min", 225),
          ("opt-back-ref-ratio-std-avg", 228),
          ("opt-max", 7),
          ("opt-min", 6),
          ("opt-std-avg", 11),
          ("opt-total", 220),
          ("opt-total-avg", 223),
          ("opt-total-max", 222),
          ("opt-total-min", 221),
          ("osize-pkts-rx", 105),
          ("osize-pkts-tx", 106),
          ("osnr", 184),
          ("osnr-avg", 187),
          ("osnr-max", 186),
          ("osnr-min", 185),
          ("otu-bbe", 56),
          ("otu-ber", 61),
          ("otu-ber-avg", 64),
          ("otu-ber-max", 63),
          ("otu-ber-min", 62),
          ("otu-eb", 55),
          ("otu-es", 57),
          ("otu-ofs", 59),
          ("otu-ses", 58),
          ("otu-uas", 60),
          ("pcs-ber", 83),
          ("pcs-ber-avg", 86),
          ("pcs-ber-max", 85),
          ("pcs-ber-min", 84),
          ("pcs-es", 80),
          ("pcs-ib", 78),
          ("pcs-ish", 79),
          ("pcs-ses", 81),
          ("pcs-uas", 82),
          ("pem-presence-avg", 181),
          ("pem-presence-max", 183),
          ("pem-presence-min", 182),
          ("pkts-1024-1518-oct-rx", 121),
          ("pkts-1024-1518-oct-tx", 122),
          ("pkts-128-255-oct-rx", 115),
          ("pkts-128-255-oct-tx", 116),
          ("pkts-256-511-oct-rx", 117),
          ("pkts-256-511-oct-tx", 118),
          ("pkts-512-1023-oct-rx", 119),
          ("pkts-512-1023-oct-tx", 120),
          ("pkts-64-oct-rx", 111),
          ("pkts-64-oct-tx", 112),
          ("pkts-65-127-oct-rx", 113),
          ("pkts-65-127-oct-tx", 114),
          ("pkts-ok-rx", 93),
          ("pkts-ok-tx", 94),
          ("pkts-over-1518-oct-rx", 123),
          ("pkts-over-1518-oct-tx", 124),
          ("pkts-paus-rx", 125),
          ("pkts-paus-tx", 126),
          ("pkts-rx", 91),
          ("pkts-tx", 92),
          ("prbs-be", 189),
          ("prbs-ber", 190),
          ("prbs-ber-avg", 193),
          ("prbs-ber-max", 192),
          ("prbs-ber-min", 191),
          ("prbs-lsss", 188),
          ("rs-bbe", 146),
          ("rs-ber", 151),
          ("rs-ber-avg", 154),
          ("rs-ber-max", 153),
          ("rs-ber-min", 152),
          ("rs-eb", 145),
          ("rs-es", 147),
          ("rs-ofs", 149),
          ("rs-ses", 148),
          ("rs-uas", 150),
          ("sefs-s", 130),
          ("ses-l", 138),
          ("ses-s", 129),
          ("snr", 43),
          ("snr-avg", 46),
          ("snr-max", 45),
          ("snr-min", 44),
          ("snr-x", 212),
          ("snr-x-avg", 215),
          ("snr-x-max", 214),
          ("snr-x-min", 213),
          ("snr-y", 216),
          ("snr-y-avg", 219),
          ("snr-y-max", 218),
          ("snr-y-min", 217),
          ("span-lngth", 194),
          ("uas-l", 139),
          ("uas-s", 131),
          ("usize-pkts-rx", 103),
          ("usize-pkts-tx", 104),
          ("volt", 22),
          ("volt-avg", 25),
          ("volt-max", 24),
          ("volt-min", 23))
    )



class GroupIdType(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class FeDegreeNum(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



class MsaName(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class PreamplifierName(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class AlarmType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conditionClear", 2),
          ("conditionRaise", 1))
    )



class RevertiveTimeType(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 600),
    )



class RemoteUrl(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class Modulereload(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class CurrentStateType(Integer32, TextualConvention):
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
        *(("cancel-inprogress", 9),
          ("commit-failed", 8),
          ("commit-inprogress", 6),
          ("commit-success", 7),
          ("download-failed", 5),
          ("download-inprogress", 3),
          ("download-success", 4),
          ("not-initiated", 1),
          ("rollback-failed", 12),
          ("rollback-inprogress", 10),
          ("rollback-success", 11),
          ("url-set", 2))
    )



class BicName(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class StatValueType(Integer32, TextualConvention):
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
        *(("counter64", 1),
          ("decimal64", 2),
          ("float", 3))
    )



class OscIdType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class OdccIdType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class WdmIdType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class PortIdType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class DolFiberType(Integer32, TextualConvention):
    status = "current"
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
        *(("leaf", 2),
          ("ndsf", 4),
          ("ssmf", 1),
          ("teralight", 5),
          ("twrs", 3))
    )



class Files1(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class UpgradeStatusObjectType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("module-upgrade-status", 2),
          ("system-upgrade-status", 1))
    )



class CustomValType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class GroupConfigType(Integer32, TextualConvention):
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
        *(("eqlzLine", 5),
          ("eqlzTerm", 3),
          ("noEqlzLine", 4),
          ("noEqlzTerm", 2),
          ("none", 1),
          ("roadm", 6))
    )



class Wavelength(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class ValueUnion(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class Wavelength1(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class TimeOut(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class SysNameType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class Validity(Integer32, TextualConvention):
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
        *(("complete", 3),
          ("notAvailable", 1),
          ("partial", 2))
    )



class MetaCliDebugLevel(Integer32, TextualConvention):
    status = "current"
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
        *(("debug", 2),
          ("error", 5),
          ("info", 3),
          ("trace", 1),
          ("warning", 4))
    )



class GlobalDebugLevel(Integer32, TextualConvention):
    status = "current"
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



class MacAddr(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class ModuleName(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class DolSupportingEquipType(Integer32, TextualConvention):
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
        *(("ila", 5),
          ("mdeq", 1),
          ("preamp", 6),
          ("roadm2", 2),
          ("roadm20", 4),
          ("roadm9", 3))
    )



class WavelengthProtectionPortIdType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class SyslogLocalFacility(Integer32, TextualConvention):
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
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )



class UpgradeLocation(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class ChassisName(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class EqptDegreeType(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class NumSpectSlicesType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 384),
    )



class PortGridType(Integer32, TextualConvention):
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
        *(("flex", 3),
          ("ghz100", 1),
          ("ghz50", 2))
    )



class CustomValType255(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class DolPortIdType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class WavelengthProtectionGroupIdType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class RemoteLocation(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class CustomIdType32(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TransceiverName(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class ThresholdType(Integer32, TextualConvention):
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
        *(("alarmHigh", 2),
          ("alarmLow", 3),
          ("warningAlert", 1))
    )



class ProfileNameType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class PassStr(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class BinLengths(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              15,
              1440)
        )
    )
    namedValues = NamedValues(
        *(("a15Minute", 15),
          ("a1Day", 1440),
          ("a1Minute", 1),
          ("unTimed", 0))
    )



class Files(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class ChassisType(Integer32, TextualConvention):
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
        *(("a1-Slot", 3),
          ("a14-Slot", 0),
          ("a2-Slot", 2),
          ("a6-Slot", 1))
    )



class EqptConnType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eqDuplex", 1),
          ("loopback", 2))
    )



class PortDwdmType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alien", 2),
          ("native", 1))
    )



class ShmmAutoUpgradeStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )



class InventoryName(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class FePortIdType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class DolOchXconSrcType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class DolModule(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class DolConnectionType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class ThresholdEntityType(Integer32, TextualConvention):
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("a100ge", 3),
          ("a10ge", 1),
          ("a40ge", 2),
          ("client", 15),
          ("dcm", 16),
          ("line", 14),
          ("oc192", 9),
          ("och", 19),
          ("odu2", 6),
          ("odu2e", 18),
          ("odu3", 7),
          ("odu4", 8),
          ("osc", 13),
          ("otu2", 4),
          ("otu2e", 17),
          ("otu4", 5),
          ("stm64", 10),
          ("wanoc192", 11),
          ("wanstm64", 12))
    )



class EntityNameType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class DolFixedGridChannelName(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class CustomIdType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class PortType(Integer32, TextualConvention):
    status = "current"
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
        *(("chlport", 4),
          ("client", 2),
          ("dcm", 3),
          ("expport", 5),
          ("line", 1))
    )



class DolOscIdType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


class DolOmsIdType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1t"


# MIB Managed Objects in the order of their OIDs

_ChassisTable_Object = MibTable
chassisTable = _ChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1)
)
if mibBuilder.loadTexts:
    chassisTable.setStatus("current")
_ChassisEntry_Object = MibTableRow
chassisEntry = _ChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1)
)
chassisEntry.setIndexNames(
    (1, "BTI7800-EQUIPMENT-MIB", "chassisName"),
)
if mibBuilder.loadTexts:
    chassisEntry.setStatus("current")
_ChassisName_Type = String
_ChassisName_Object = MibTableColumn
chassisName = _ChassisName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 1),
    _ChassisName_Type()
)
chassisName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chassisName.setStatus("current")
_ChassisType_Type = ChassisType
_ChassisType_Object = MibTableColumn
chassisType = _ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 2),
    _ChassisType_Type()
)
chassisType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisType.setStatus("current")
_ChassisPEC_Type = String
_ChassisPEC_Object = MibTableColumn
chassisPEC = _ChassisPEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 3),
    _ChassisPEC_Type()
)
chassisPEC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisPEC.setStatus("current")


class _ChassisAdminStatus_Type(Integer32):
    """Custom type chassisAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_ChassisAdminStatus_Type.__name__ = "Integer32"
_ChassisAdminStatus_Object = MibTableColumn
chassisAdminStatus = _ChassisAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 4),
    _ChassisAdminStatus_Type()
)
chassisAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisAdminStatus.setStatus("current")


class _ChassisCustom1_Type(String):
    """Custom type chassisCustom1 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChassisCustom1_Type.__name__ = "String"
_ChassisCustom1_Object = MibTableColumn
chassisCustom1 = _ChassisCustom1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 5),
    _ChassisCustom1_Type()
)
chassisCustom1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisCustom1.setStatus("current")


class _ChassisCustom2_Type(String):
    """Custom type chassisCustom2 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChassisCustom2_Type.__name__ = "String"
_ChassisCustom2_Object = MibTableColumn
chassisCustom2 = _ChassisCustom2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 6),
    _ChassisCustom2_Type()
)
chassisCustom2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisCustom2.setStatus("current")


class _ChassisCustom3_Type(String):
    """Custom type chassisCustom3 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChassisCustom3_Type.__name__ = "String"
_ChassisCustom3_Object = MibTableColumn
chassisCustom3 = _ChassisCustom3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 7),
    _ChassisCustom3_Type()
)
chassisCustom3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisCustom3.setStatus("current")


class _ChassisOperationalStatus_Type(Integer32):
    """Custom type chassisOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 0),
          ("up", 1))
    )


_ChassisOperationalStatus_Type.__name__ = "Integer32"
_ChassisOperationalStatus_Object = MibTableColumn
chassisOperationalStatus = _ChassisOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 8),
    _ChassisOperationalStatus_Type()
)
chassisOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisOperationalStatus.setStatus("current")
_ChassisLocation_Type = String
_ChassisLocation_Object = MibTableColumn
chassisLocation = _ChassisLocation_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 9),
    _ChassisLocation_Type()
)
chassisLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisLocation.setStatus("current")
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("current")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1)
)
moduleEntry.setIndexNames(
    (0, "BTI7800-EQUIPMENT-MIB", "chassisName"),
    (1, "BTI7800-EQUIPMENT-MIB", "moduleName"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("current")
_ModuleName_Type = String
_ModuleName_Object = MibTableColumn
moduleName = _ModuleName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 1),
    _ModuleName_Type()
)
moduleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    moduleName.setStatus("current")
_ModulePEC_Type = String
_ModulePEC_Object = MibTableColumn
modulePEC = _ModulePEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 2),
    _ModulePEC_Type()
)
modulePEC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulePEC.setStatus("current")


class _ModuleAdminStatus_Type(Integer32):
    """Custom type moduleAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_ModuleAdminStatus_Type.__name__ = "Integer32"
_ModuleAdminStatus_Object = MibTableColumn
moduleAdminStatus = _ModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 3),
    _ModuleAdminStatus_Type()
)
moduleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleAdminStatus.setStatus("current")


class _ModuleCustom1_Type(String):
    """Custom type moduleCustom1 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModuleCustom1_Type.__name__ = "String"
_ModuleCustom1_Object = MibTableColumn
moduleCustom1 = _ModuleCustom1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 4),
    _ModuleCustom1_Type()
)
moduleCustom1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleCustom1.setStatus("current")


class _ModuleCustom2_Type(String):
    """Custom type moduleCustom2 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModuleCustom2_Type.__name__ = "String"
_ModuleCustom2_Object = MibTableColumn
moduleCustom2 = _ModuleCustom2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 5),
    _ModuleCustom2_Type()
)
moduleCustom2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleCustom2.setStatus("current")


class _ModuleCustom3_Type(String):
    """Custom type moduleCustom3 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModuleCustom3_Type.__name__ = "String"
_ModuleCustom3_Object = MibTableColumn
moduleCustom3 = _ModuleCustom3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 6),
    _ModuleCustom3_Type()
)
moduleCustom3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleCustom3.setStatus("current")


class _ModuleOperationalStatus_Type(Integer32):
    """Custom type moduleOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 0),
          ("up", 1))
    )


_ModuleOperationalStatus_Type.__name__ = "Integer32"
_ModuleOperationalStatus_Object = MibTableColumn
moduleOperationalStatus = _ModuleOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 7),
    _ModuleOperationalStatus_Type()
)
moduleOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleOperationalStatus.setStatus("current")
_ModuleType_Type = UfmType
_ModuleType_Object = MibTableColumn
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 8),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleType.setStatus("current")
_MsaXcvrTable_Object = MibTable
msaXcvrTable = _MsaXcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3)
)
if mibBuilder.loadTexts:
    msaXcvrTable.setStatus("current")
_MsaXcvrEntry_Object = MibTableRow
msaXcvrEntry = _MsaXcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1)
)
msaXcvrEntry.setIndexNames(
    (0, "BTI7800-EQUIPMENT-MIB", "chassisName"),
    (0, "BTI7800-EQUIPMENT-MIB", "moduleName"),
    (1, "BTI7800-EQUIPMENT-MIB", "msaXcvrName"),
)
if mibBuilder.loadTexts:
    msaXcvrEntry.setStatus("current")
_MsaXcvrName_Type = String
_MsaXcvrName_Object = MibTableColumn
msaXcvrName = _MsaXcvrName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 1),
    _MsaXcvrName_Type()
)
msaXcvrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msaXcvrName.setStatus("current")
_MsaXcvrPEC_Type = String
_MsaXcvrPEC_Object = MibTableColumn
msaXcvrPEC = _MsaXcvrPEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 2),
    _MsaXcvrPEC_Type()
)
msaXcvrPEC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msaXcvrPEC.setStatus("current")


class _MsaXcvrAdminStatus_Type(Integer32):
    """Custom type msaXcvrAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MsaXcvrAdminStatus_Type.__name__ = "Integer32"
_MsaXcvrAdminStatus_Object = MibTableColumn
msaXcvrAdminStatus = _MsaXcvrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 3),
    _MsaXcvrAdminStatus_Type()
)
msaXcvrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msaXcvrAdminStatus.setStatus("current")


class _MsaXcvrCustom1_Type(String):
    """Custom type msaXcvrCustom1 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsaXcvrCustom1_Type.__name__ = "String"
_MsaXcvrCustom1_Object = MibTableColumn
msaXcvrCustom1 = _MsaXcvrCustom1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 4),
    _MsaXcvrCustom1_Type()
)
msaXcvrCustom1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msaXcvrCustom1.setStatus("current")


class _MsaXcvrCustom2_Type(String):
    """Custom type msaXcvrCustom2 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsaXcvrCustom2_Type.__name__ = "String"
_MsaXcvrCustom2_Object = MibTableColumn
msaXcvrCustom2 = _MsaXcvrCustom2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 5),
    _MsaXcvrCustom2_Type()
)
msaXcvrCustom2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msaXcvrCustom2.setStatus("current")


class _MsaXcvrCustom3_Type(String):
    """Custom type msaXcvrCustom3 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsaXcvrCustom3_Type.__name__ = "String"
_MsaXcvrCustom3_Object = MibTableColumn
msaXcvrCustom3 = _MsaXcvrCustom3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 6),
    _MsaXcvrCustom3_Type()
)
msaXcvrCustom3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msaXcvrCustom3.setStatus("current")


class _MsaXcvrOperationalStatus_Type(Integer32):
    """Custom type msaXcvrOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 0),
          ("up", 1))
    )


_MsaXcvrOperationalStatus_Type.__name__ = "Integer32"
_MsaXcvrOperationalStatus_Object = MibTableColumn
msaXcvrOperationalStatus = _MsaXcvrOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 7),
    _MsaXcvrOperationalStatus_Type()
)
msaXcvrOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msaXcvrOperationalStatus.setStatus("current")


class _MsaXcvrOpticalFormat_Type(Integer32):
    """Custom type msaXcvrOpticalFormat based on Integer32"""
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
        *(("fixedX1", 0),
          ("fixedX10", 2),
          ("fixedX4", 1),
          ("none", 7),
          ("tunableX1", 3),
          ("tunableX10", 5),
          ("tunableX2", 6),
          ("tunableX4", 4))
    )


_MsaXcvrOpticalFormat_Type.__name__ = "Integer32"
_MsaXcvrOpticalFormat_Object = MibTableColumn
msaXcvrOpticalFormat = _MsaXcvrOpticalFormat_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 8),
    _MsaXcvrOpticalFormat_Type()
)
msaXcvrOpticalFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msaXcvrOpticalFormat.setStatus("current")
_BicTable_Object = MibTable
bicTable = _BicTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4)
)
if mibBuilder.loadTexts:
    bicTable.setStatus("current")
_BicEntry_Object = MibTableRow
bicEntry = _BicEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1)
)
bicEntry.setIndexNames(
    (0, "BTI7800-EQUIPMENT-MIB", "chassisName"),
    (0, "BTI7800-EQUIPMENT-MIB", "moduleName"),
    (1, "BTI7800-EQUIPMENT-MIB", "bicName"),
)
if mibBuilder.loadTexts:
    bicEntry.setStatus("current")
_BicName_Type = String
_BicName_Object = MibTableColumn
bicName = _BicName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 1),
    _BicName_Type()
)
bicName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bicName.setStatus("current")
_BicPEC_Type = String
_BicPEC_Object = MibTableColumn
bicPEC = _BicPEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 2),
    _BicPEC_Type()
)
bicPEC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bicPEC.setStatus("current")


class _BicAdminStatus_Type(Integer32):
    """Custom type bicAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_BicAdminStatus_Type.__name__ = "Integer32"
_BicAdminStatus_Object = MibTableColumn
bicAdminStatus = _BicAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 3),
    _BicAdminStatus_Type()
)
bicAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bicAdminStatus.setStatus("current")


class _BicCustom1_Type(String):
    """Custom type bicCustom1 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BicCustom1_Type.__name__ = "String"
_BicCustom1_Object = MibTableColumn
bicCustom1 = _BicCustom1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 4),
    _BicCustom1_Type()
)
bicCustom1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bicCustom1.setStatus("current")


class _BicCustom2_Type(String):
    """Custom type bicCustom2 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BicCustom2_Type.__name__ = "String"
_BicCustom2_Object = MibTableColumn
bicCustom2 = _BicCustom2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 5),
    _BicCustom2_Type()
)
bicCustom2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bicCustom2.setStatus("current")


class _BicCustom3_Type(String):
    """Custom type bicCustom3 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BicCustom3_Type.__name__ = "String"
_BicCustom3_Object = MibTableColumn
bicCustom3 = _BicCustom3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 6),
    _BicCustom3_Type()
)
bicCustom3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bicCustom3.setStatus("current")


class _BicOperationalStatus_Type(Integer32):
    """Custom type bicOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 0),
          ("up", 1))
    )


_BicOperationalStatus_Type.__name__ = "Integer32"
_BicOperationalStatus_Object = MibTableColumn
bicOperationalStatus = _BicOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 7),
    _BicOperationalStatus_Type()
)
bicOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bicOperationalStatus.setStatus("current")
_BicType_Type = BicType
_BicType_Object = MibTableColumn
bicType = _BicType_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 8),
    _BicType_Type()
)
bicType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bicType.setStatus("current")
_XcvrTable_Object = MibTable
xcvrTable = _XcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5)
)
if mibBuilder.loadTexts:
    xcvrTable.setStatus("current")
_XcvrEntry_Object = MibTableRow
xcvrEntry = _XcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1)
)
xcvrEntry.setIndexNames(
    (0, "BTI7800-EQUIPMENT-MIB", "chassisName"),
    (0, "BTI7800-EQUIPMENT-MIB", "moduleName"),
    (0, "BTI7800-EQUIPMENT-MIB", "bicName"),
    (1, "BTI7800-EQUIPMENT-MIB", "xcvrName"),
)
if mibBuilder.loadTexts:
    xcvrEntry.setStatus("current")
_XcvrName_Type = String
_XcvrName_Object = MibTableColumn
xcvrName = _XcvrName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 1),
    _XcvrName_Type()
)
xcvrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcvrName.setStatus("current")
_XcvrPEC_Type = String
_XcvrPEC_Object = MibTableColumn
xcvrPEC = _XcvrPEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 2),
    _XcvrPEC_Type()
)
xcvrPEC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcvrPEC.setStatus("current")


class _XcvrAdminStatus_Type(Integer32):
    """Custom type xcvrAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_XcvrAdminStatus_Type.__name__ = "Integer32"
_XcvrAdminStatus_Object = MibTableColumn
xcvrAdminStatus = _XcvrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 3),
    _XcvrAdminStatus_Type()
)
xcvrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcvrAdminStatus.setStatus("current")


class _XcvrCustom1_Type(String):
    """Custom type xcvrCustom1 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcvrCustom1_Type.__name__ = "String"
_XcvrCustom1_Object = MibTableColumn
xcvrCustom1 = _XcvrCustom1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 4),
    _XcvrCustom1_Type()
)
xcvrCustom1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcvrCustom1.setStatus("current")


class _XcvrCustom2_Type(String):
    """Custom type xcvrCustom2 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcvrCustom2_Type.__name__ = "String"
_XcvrCustom2_Object = MibTableColumn
xcvrCustom2 = _XcvrCustom2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 5),
    _XcvrCustom2_Type()
)
xcvrCustom2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcvrCustom2.setStatus("current")


class _XcvrCustom3_Type(String):
    """Custom type xcvrCustom3 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcvrCustom3_Type.__name__ = "String"
_XcvrCustom3_Object = MibTableColumn
xcvrCustom3 = _XcvrCustom3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 6),
    _XcvrCustom3_Type()
)
xcvrCustom3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcvrCustom3.setStatus("current")


class _XcvrOperationalStatus_Type(Integer32):
    """Custom type xcvrOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 0),
          ("up", 1))
    )


_XcvrOperationalStatus_Type.__name__ = "Integer32"
_XcvrOperationalStatus_Object = MibTableColumn
xcvrOperationalStatus = _XcvrOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 7),
    _XcvrOperationalStatus_Type()
)
xcvrOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcvrOperationalStatus.setStatus("current")


class _XcvrOpticalFormat_Type(Integer32):
    """Custom type xcvrOpticalFormat based on Integer32"""
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
        *(("fixedX1", 0),
          ("fixedX10", 2),
          ("fixedX4", 1),
          ("none", 7),
          ("tunableX1", 3),
          ("tunableX10", 5),
          ("tunableX2", 6),
          ("tunableX4", 4))
    )


_XcvrOpticalFormat_Type.__name__ = "Integer32"
_XcvrOpticalFormat_Object = MibTableColumn
xcvrOpticalFormat = _XcvrOpticalFormat_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 8),
    _XcvrOpticalFormat_Type()
)
xcvrOpticalFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcvrOpticalFormat.setStatus("current")
_PreamplifierTable_Object = MibTable
preamplifierTable = _PreamplifierTable_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6)
)
if mibBuilder.loadTexts:
    preamplifierTable.setStatus("current")
_PreamplifierEntry_Object = MibTableRow
preamplifierEntry = _PreamplifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1)
)
preamplifierEntry.setIndexNames(
    (0, "BTI7800-EQUIPMENT-MIB", "chassisName"),
    (0, "BTI7800-EQUIPMENT-MIB", "moduleName"),
    (1, "BTI7800-EQUIPMENT-MIB", "preamplifierName"),
)
if mibBuilder.loadTexts:
    preamplifierEntry.setStatus("current")
_PreamplifierName_Type = String
_PreamplifierName_Object = MibTableColumn
preamplifierName = _PreamplifierName_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 1),
    _PreamplifierName_Type()
)
preamplifierName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    preamplifierName.setStatus("current")
_PreamplifierPEC_Type = String
_PreamplifierPEC_Object = MibTableColumn
preamplifierPEC = _PreamplifierPEC_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 2),
    _PreamplifierPEC_Type()
)
preamplifierPEC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preamplifierPEC.setStatus("current")


class _PreamplifierAdminStatus_Type(Integer32):
    """Custom type preamplifierAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_PreamplifierAdminStatus_Type.__name__ = "Integer32"
_PreamplifierAdminStatus_Object = MibTableColumn
preamplifierAdminStatus = _PreamplifierAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 3),
    _PreamplifierAdminStatus_Type()
)
preamplifierAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preamplifierAdminStatus.setStatus("current")


class _PreamplifierCustom1_Type(String):
    """Custom type preamplifierCustom1 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PreamplifierCustom1_Type.__name__ = "String"
_PreamplifierCustom1_Object = MibTableColumn
preamplifierCustom1 = _PreamplifierCustom1_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 4),
    _PreamplifierCustom1_Type()
)
preamplifierCustom1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preamplifierCustom1.setStatus("current")


class _PreamplifierCustom2_Type(String):
    """Custom type preamplifierCustom2 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PreamplifierCustom2_Type.__name__ = "String"
_PreamplifierCustom2_Object = MibTableColumn
preamplifierCustom2 = _PreamplifierCustom2_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 5),
    _PreamplifierCustom2_Type()
)
preamplifierCustom2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preamplifierCustom2.setStatus("current")


class _PreamplifierCustom3_Type(String):
    """Custom type preamplifierCustom3 based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PreamplifierCustom3_Type.__name__ = "String"
_PreamplifierCustom3_Object = MibTableColumn
preamplifierCustom3 = _PreamplifierCustom3_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 6),
    _PreamplifierCustom3_Type()
)
preamplifierCustom3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preamplifierCustom3.setStatus("current")


class _PreamplifierOperationalStatus_Type(Integer32):
    """Custom type preamplifierOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 0),
          ("up", 1))
    )


_PreamplifierOperationalStatus_Type.__name__ = "Integer32"
_PreamplifierOperationalStatus_Object = MibTableColumn
preamplifierOperationalStatus = _PreamplifierOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 7),
    _PreamplifierOperationalStatus_Type()
)
preamplifierOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preamplifierOperationalStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BTI7800-EQUIPMENT-MIB",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "Ipv4Prefix": Ipv4Prefix,
       "InetAddressIP": InetAddressIP,
       "String": String,
       "CurrentDBStateType": CurrentDBStateType,
       "BicType": BicType,
       "DolOchIdType": DolOchIdType,
       "ObsoleteName": ObsoleteName,
       "UfmType": UfmType,
       "AmpModule": AmpModule,
       "TransportType": TransportType,
       "Role": Role,
       "DolFconnEndpt1Type": DolFconnEndpt1Type,
       "DolFconnEndpt2Type": DolFconnEndpt2Type,
       "DebugLevel": DebugLevel,
       "FeGroupNum": FeGroupNum,
       "PasswdStr": PasswdStr,
       "RoadmType": RoadmType,
       "StatisticPointType": StatisticPointType,
       "GroupIdType": GroupIdType,
       "FeDegreeNum": FeDegreeNum,
       "MsaName": MsaName,
       "PreamplifierName": PreamplifierName,
       "AlarmType": AlarmType,
       "RevertiveTimeType": RevertiveTimeType,
       "RemoteUrl": RemoteUrl,
       "Modulereload": Modulereload,
       "CurrentStateType": CurrentStateType,
       "BicName": BicName,
       "StatValueType": StatValueType,
       "OscIdType": OscIdType,
       "OdccIdType": OdccIdType,
       "WdmIdType": WdmIdType,
       "PortIdType": PortIdType,
       "DolFiberType": DolFiberType,
       "Files1": Files1,
       "UpgradeStatusObjectType": UpgradeStatusObjectType,
       "CustomValType": CustomValType,
       "GroupConfigType": GroupConfigType,
       "Wavelength": Wavelength,
       "ValueUnion": ValueUnion,
       "Wavelength1": Wavelength1,
       "TimeOut": TimeOut,
       "SysNameType": SysNameType,
       "Validity": Validity,
       "MetaCliDebugLevel": MetaCliDebugLevel,
       "GlobalDebugLevel": GlobalDebugLevel,
       "MacAddr": MacAddr,
       "ModuleName": ModuleName,
       "DolSupportingEquipType": DolSupportingEquipType,
       "WavelengthProtectionPortIdType": WavelengthProtectionPortIdType,
       "SyslogLocalFacility": SyslogLocalFacility,
       "UpgradeLocation": UpgradeLocation,
       "ChassisName": ChassisName,
       "EqptDegreeType": EqptDegreeType,
       "NumSpectSlicesType": NumSpectSlicesType,
       "PortGridType": PortGridType,
       "CustomValType255": CustomValType255,
       "DolPortIdType": DolPortIdType,
       "WavelengthProtectionGroupIdType": WavelengthProtectionGroupIdType,
       "RemoteLocation": RemoteLocation,
       "CustomIdType32": CustomIdType32,
       "TransceiverName": TransceiverName,
       "ThresholdType": ThresholdType,
       "ProfileNameType": ProfileNameType,
       "PassStr": PassStr,
       "BinLengths": BinLengths,
       "Files": Files,
       "ChassisType": ChassisType,
       "EqptConnType": EqptConnType,
       "PortDwdmType": PortDwdmType,
       "ShmmAutoUpgradeStatus": ShmmAutoUpgradeStatus,
       "InventoryName": InventoryName,
       "FePortIdType": FePortIdType,
       "DolOchXconSrcType": DolOchXconSrcType,
       "DolModule": DolModule,
       "DolConnectionType": DolConnectionType,
       "ThresholdEntityType": ThresholdEntityType,
       "EntityNameType": EntityNameType,
       "DolFixedGridChannelName": DolFixedGridChannelName,
       "CustomIdType": CustomIdType,
       "PortType": PortType,
       "DolOscIdType": DolOscIdType,
       "DolOmsIdType": DolOmsIdType,
       "bTI7800-EQUIPMENT-MIB": bTI7800_EQUIPMENT_MIB,
       "chassisTable": chassisTable,
       "chassisEntry": chassisEntry,
       "chassisName": chassisName,
       "chassisType": chassisType,
       "chassisPEC": chassisPEC,
       "chassisAdminStatus": chassisAdminStatus,
       "chassisCustom1": chassisCustom1,
       "chassisCustom2": chassisCustom2,
       "chassisCustom3": chassisCustom3,
       "chassisOperationalStatus": chassisOperationalStatus,
       "chassisLocation": chassisLocation,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleName": moduleName,
       "modulePEC": modulePEC,
       "moduleAdminStatus": moduleAdminStatus,
       "moduleCustom1": moduleCustom1,
       "moduleCustom2": moduleCustom2,
       "moduleCustom3": moduleCustom3,
       "moduleOperationalStatus": moduleOperationalStatus,
       "moduleType": moduleType,
       "msaXcvrTable": msaXcvrTable,
       "msaXcvrEntry": msaXcvrEntry,
       "msaXcvrName": msaXcvrName,
       "msaXcvrPEC": msaXcvrPEC,
       "msaXcvrAdminStatus": msaXcvrAdminStatus,
       "msaXcvrCustom1": msaXcvrCustom1,
       "msaXcvrCustom2": msaXcvrCustom2,
       "msaXcvrCustom3": msaXcvrCustom3,
       "msaXcvrOperationalStatus": msaXcvrOperationalStatus,
       "msaXcvrOpticalFormat": msaXcvrOpticalFormat,
       "bicTable": bicTable,
       "bicEntry": bicEntry,
       "bicName": bicName,
       "bicPEC": bicPEC,
       "bicAdminStatus": bicAdminStatus,
       "bicCustom1": bicCustom1,
       "bicCustom2": bicCustom2,
       "bicCustom3": bicCustom3,
       "bicOperationalStatus": bicOperationalStatus,
       "bicType": bicType,
       "xcvrTable": xcvrTable,
       "xcvrEntry": xcvrEntry,
       "xcvrName": xcvrName,
       "xcvrPEC": xcvrPEC,
       "xcvrAdminStatus": xcvrAdminStatus,
       "xcvrCustom1": xcvrCustom1,
       "xcvrCustom2": xcvrCustom2,
       "xcvrCustom3": xcvrCustom3,
       "xcvrOperationalStatus": xcvrOperationalStatus,
       "xcvrOpticalFormat": xcvrOpticalFormat,
       "preamplifierTable": preamplifierTable,
       "preamplifierEntry": preamplifierEntry,
       "preamplifierName": preamplifierName,
       "preamplifierPEC": preamplifierPEC,
       "preamplifierAdminStatus": preamplifierAdminStatus,
       "preamplifierCustom1": preamplifierCustom1,
       "preamplifierCustom2": preamplifierCustom2,
       "preamplifierCustom3": preamplifierCustom3,
       "preamplifierOperationalStatus": preamplifierOperationalStatus}
)
