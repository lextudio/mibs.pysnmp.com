# SNMP MIB module (DL5400-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DL5400-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:32 2024
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
 NotificationType,
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
    "NotificationType",
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class DL5400Validation(Integer32):
    """Custom type DL5400Validation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )





class DL5400commBaudRate(Integer32):
    """Custom type DL5400commBaudRate based on Integer32"""
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
        *(("bps115200", 8),
          ("bps1200", 1),
          ("bps19200", 5),
          ("bps2400", 2),
          ("bps38400", 6),
          ("bps4800", 3),
          ("bps57600", 7),
          ("bps9600", 4))
    )





class DL5400commParity(Integer32):
    """Custom type DL5400commParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 1),
          ("none", 3),
          ("odd", 2))
    )





class DL5400commStopBits(Integer32):
    """Custom type DL5400commStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("oneAndHalf", 2),
          ("two", 3))
    )





class DL5400commNumDataBits(Integer32):
    """Custom type DL5400commNumDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("seven", 7))
    )





class DL5400commFlowControl(Integer32):
    """Custom type DL5400commFlowControl based on Integer32"""
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
        *(("hwFlowControl", 3),
          ("none", 4),
          ("xoffUntilAny", 2),
          ("xoffUntilXon", 1))
    )





class TODYear(Integer32):
    """Custom type TODYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )





class TODMonth(Integer32):
    """Custom type TODMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )





class TODDay(Integer32):
    """Custom type TODDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )





class TODHour(Integer32):
    """Custom type TODHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )





class TODMinute(Integer32):
    """Custom type TODMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )





class TODSecond(Integer32):
    """Custom type TODSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )





class DL5400CardId(Integer32):
    """Custom type DL5400CardId based on Integer32"""
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
        *(("ds1", 4),
          ("enet", 3),
          ("mpm", 1),
          ("pp", 2))
    )





class DL5400PortId(Integer32):
    """Custom type DL5400PortId based on Integer32"""
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
        *(("comm1", 3),
          ("comm2", 4),
          ("dte", 1),
          ("net1", 5),
          ("net2", 6),
          ("net3", 7),
          ("net4", 8),
          ("net5", 9),
          ("net6", 10),
          ("net7", 11),
          ("net8", 12),
          ("nmsEthernet", 2))
    )





class DL5400TxClkSrc(Integer32):
    """Custom type DL5400TxClkSrc based on Integer32"""
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
        *(("autoTiming", 4),
          ("externalClock", 2),
          ("internalClock", 1),
          ("rcvrdTiming", 3))
    )





class DL5400Event(Integer32):
    """Custom type DL5400Event based on Integer32"""
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
              175)
        )
    )
    namedValues = NamedValues(
        *(("ev-admin-isnr", 6),
          ("ev-admin-oos", 7),
          ("ev-admin-oosmt", 8),
          ("ev-ais", 104),
          ("ev-ais-remit", 105),
          ("ev-back-high-temperature", 23),
          ("ev-back-high-temperature-remit", 24),
          ("ev-clkref-configchanged", 10),
          ("ev-cuisession-inactivitytimeout", 9),
          ("ev-dte-local-loopback-end", 171),
          ("ev-dte-local-loopback-start", 170),
          ("ev-dte-remote-loopback-end", 173),
          ("ev-dte-remote-loopback-start", 172),
          ("ev-exceeded-cv-consec-sec", 110),
          ("ev-exceeded-cv-consec-sec-remit", 111),
          ("ev-exceeded-es-15min-major-threshold", 122),
          ("ev-exceeded-es-15min-major-threshold-remit", 123),
          ("ev-exceeded-es-15min-minor-threshold", 120),
          ("ev-exceeded-es-15min-minor-threshold-remit", 121),
          ("ev-exceeded-es-24hr-major-threshold", 142),
          ("ev-exceeded-es-24hr-major-threshold-remit", 143),
          ("ev-exceeded-es-24hr-minor-threshold", 140),
          ("ev-exceeded-es-24hr-minor-threshold-remit", 141),
          ("ev-exceeded-pcv-15min-major-threshold", 118),
          ("ev-exceeded-pcv-15min-major-threshold-remit", 119),
          ("ev-exceeded-pcv-15min-minor-threshold", 116),
          ("ev-exceeded-pcv-15min-minor-threshold-remit", 117),
          ("ev-exceeded-pcv-24hr-major-threshold", 138),
          ("ev-exceeded-pcv-24hr-major-threshold-remit", 139),
          ("ev-exceeded-pcv-24hr-minor-threshold", 136),
          ("ev-exceeded-pcv-24hr-minor-threshold-remit", 137),
          ("ev-exceeded-sas-15min-major-threshold", 130),
          ("ev-exceeded-sas-15min-major-threshold-remit", 131),
          ("ev-exceeded-sas-15min-minor-threshold", 128),
          ("ev-exceeded-sas-15min-minor-threshold-remit", 129),
          ("ev-exceeded-sas-24hr-major-threshold", 150),
          ("ev-exceeded-sas-24hr-major-threshold-remit", 151),
          ("ev-exceeded-sas-24hr-minor-threshold", 148),
          ("ev-exceeded-sas-24hr-minor-threshold-remit", 149),
          ("ev-exceeded-ses-15min-major-threshold", 126),
          ("ev-exceeded-ses-15min-major-threshold-remit", 127),
          ("ev-exceeded-ses-15min-minor-threshold", 124),
          ("ev-exceeded-ses-15min-minor-threshold-remit", 125),
          ("ev-exceeded-ses-24hr-major-threshold", 146),
          ("ev-exceeded-ses-24hr-major-threshold-remit", 147),
          ("ev-exceeded-ses-24hr-minor-threshold", 144),
          ("ev-exceeded-ses-24hr-minor-threshold-remit", 145),
          ("ev-exceeded-ses-consec-sec", 112),
          ("ev-exceeded-ses-consec-sec-remit", 113),
          ("ev-exceeded-uas-15min-major-threshold", 134),
          ("ev-exceeded-uas-15min-major-threshold-remit", 135),
          ("ev-exceeded-uas-15min-minor-threshold", 132),
          ("ev-exceeded-uas-15min-minor-threshold-remit", 133),
          ("ev-exceeded-uas-24hr-major-threshold", 154),
          ("ev-exceeded-uas-24hr-major-threshold-remit", 155),
          ("ev-exceeded-uas-24hr-minor-threshold", 152),
          ("ev-exceeded-uas-24hr-minor-threshold-remit", 153),
          ("ev-exceeded-uas-consec-sec", 114),
          ("ev-exceeded-uas-consec-sec-remit", 115),
          ("ev-ext-clk-fail", 35),
          ("ev-ext-clk-ok", 36),
          ("ev-external-major-alarm-input", 25),
          ("ev-external-major-alarm-input-end", 26),
          ("ev-external-minor-alarm-input", 27),
          ("ev-external-minor-alarm-input-end", 28),
          ("ev-external-status-alarm-input", 29),
          ("ev-external-status-alarm-input-end", 30),
          ("ev-fan1-fail", 37),
          ("ev-fan1-ok", 38),
          ("ev-fan2-fail", 39),
          ("ev-fan2-ok", 40),
          ("ev-flash-checksum-fail", 14),
          ("ev-front-high-temperature", 21),
          ("ev-front-high-temperature-remit", 22),
          ("ev-lamptest-end", 18),
          ("ev-lamptest-start", 17),
          ("ev-lof", 102),
          ("ev-lof-remit", 103),
          ("ev-lost-signal", 100),
          ("ev-lost-signal-remit", 101),
          ("ev-mgmt-post-fail", 19),
          ("ev-mgmt-post-fail-remit", 20),
          ("ev-mlppp-insufficient-links", 68),
          ("ev-mlppp-insufficient-links-remit", 69),
          ("ev-mlppp-link-down", 174),
          ("ev-mlppp-link-up", 175),
          ("ev-mlppp-module-missing", 66),
          ("ev-mlppp-module-ok", 67),
          ("ev-mlppp-post-fail", 64),
          ("ev-mlppp-post-fail-remit", 65),
          ("ev-mod-all-ports-failed", 78),
          ("ev-mod-all-ports-ok", 79),
          ("ev-mod-appear", 1),
          ("ev-mod-cfg-match", 52),
          ("ev-mod-cfg-mismatch", 51),
          ("ev-mod-disappear", 2),
          ("ev-mod-fail", 70),
          ("ev-mod-hello", 73),
          ("ev-mod-init-fail", 74),
          ("ev-mod-init-ok", 75),
          ("ev-mod-no-resp", 72),
          ("ev-mod-some-ports-failed", 76),
          ("ev-mod-some-ports-ok", 77),
          ("ev-mod-up", 71),
          ("ev-module-processor-fail", 49),
          ("ev-module-processor-ok", 50),
          ("ev-net-BERT-end", 163),
          ("ev-net-BERT-start", 162),
          ("ev-net-local-loopback-end", 157),
          ("ev-net-local-loopback-start", 156),
          ("ev-net-payload-loopback-end", 161),
          ("ev-net-payload-loopback-start", 160),
          ("ev-net-remote-loopback-end", 159),
          ("ev-net-remote-loopback-start", 158),
          ("ev-packet-processor-missing", 45),
          ("ev-packet-processor-ok", 46),
          ("ev-packet-processor-post-fail", 43),
          ("ev-packet-processor-post-ok", 44),
          ("ev-ppp-echo-timeout", 164),
          ("ev-ppp-echo-timeout-remit", 165),
          ("ev-ppp-link-fallback", 168),
          ("ev-ppp-link-fallback-remit", 169),
          ("ev-ppp-loopback-line", 166),
          ("ev-ppp-loopback-line-remit", 167),
          ("ev-primary-clk-fail", 31),
          ("ev-primary-clk-ok", 32),
          ("ev-ps-fan-fail", 41),
          ("ev-ps-fan-ok", 42),
          ("ev-rai", 106),
          ("ev-rai-remit", 107),
          ("ev-ram-test-fail", 12),
          ("ev-red-alarm", 108),
          ("ev-red-alarm-remit", 109),
          ("ev-rom-checksum-fail", 13),
          ("ev-secondary-clk-fail", 33),
          ("ev-secondary-clk-ok", 34),
          ("ev-selftest-fail", 11),
          ("ev-system-initialized", 4),
          ("ev-system-reset", 3),
          ("ev-time-not-set", 15),
          ("ev-timeofday-changed", 5),
          ("ev-unit-restart", 16),
          ("ev-use-internal-clk", 55),
          ("ev-use-primary-clk", 53),
          ("ev-use-rx-clk1", 56),
          ("ev-use-rx-clk2", 57),
          ("ev-use-rx-clk3", 58),
          ("ev-use-rx-clk4", 59),
          ("ev-use-rx-clk5", 60),
          ("ev-use-rx-clk6", 61),
          ("ev-use-rx-clk7", 62),
          ("ev-use-rx-clk8", 63),
          ("ev-use-secondary-clk", 54),
          ("ev-voltage-exceeds", 47),
          ("ev-voltage-ok", 48))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Digital_link_ObjectIdentity = ObjectIdentity
digital_link = _Digital_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300)
)
_Dl5400_ObjectIdentity = ObjectIdentity
dl5400 = _Dl5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110)
)
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 1)
)
_UnitLevelConfig_ObjectIdentity = ObjectIdentity
unitLevelConfig = _UnitLevelConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1)
)


class _UnitSerialNum_Type(DisplayString):
    """Custom type unitSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UnitSerialNum_Type.__name__ = "DisplayString"
_UnitSerialNum_Object = MibScalar
unitSerialNum = _UnitSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 1),
    _UnitSerialNum_Type()
)
unitSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSerialNum.setStatus("mandatory")


class _UnitName_Type(DisplayString):
    """Custom type unitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UnitName_Type.__name__ = "DisplayString"
_UnitName_Object = MibScalar
unitName = _UnitName_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 2),
    _UnitName_Type()
)
unitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitName.setStatus("mandatory")


class _UnitHwRev_Type(DisplayString):
    """Custom type unitHwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_UnitHwRev_Type.__name__ = "DisplayString"
_UnitHwRev_Object = MibScalar
unitHwRev = _UnitHwRev_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 3),
    _UnitHwRev_Type()
)
unitHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitHwRev.setStatus("mandatory")


class _UnitSwRev_Type(DisplayString):
    """Custom type unitSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_UnitSwRev_Type.__name__ = "DisplayString"
_UnitSwRev_Object = MibScalar
unitSwRev = _UnitSwRev_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 4),
    _UnitSwRev_Type()
)
unitSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSwRev.setStatus("mandatory")


class _UnitMibRev_Type(DisplayString):
    """Custom type unitMibRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UnitMibRev_Type.__name__ = "DisplayString"
_UnitMibRev_Object = MibScalar
unitMibRev = _UnitMibRev_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 5),
    _UnitMibRev_Type()
)
unitMibRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitMibRev.setStatus("mandatory")


class _UnitFrontPnl_Type(Integer32):
    """Custom type unitFrontPnl based on Integer32"""
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


_UnitFrontPnl_Type.__name__ = "Integer32"
_UnitFrontPnl_Object = MibScalar
unitFrontPnl = _UnitFrontPnl_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 6),
    _UnitFrontPnl_Type()
)
unitFrontPnl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitFrontPnl.setStatus("mandatory")
_UnitDateYear_Type = TODYear
_UnitDateYear_Object = MibScalar
unitDateYear = _UnitDateYear_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 7),
    _UnitDateYear_Type()
)
unitDateYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitDateYear.setStatus("mandatory")
_UnitDateMonth_Type = TODMonth
_UnitDateMonth_Object = MibScalar
unitDateMonth = _UnitDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 8),
    _UnitDateMonth_Type()
)
unitDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitDateMonth.setStatus("mandatory")
_UnitDateDay_Type = TODDay
_UnitDateDay_Object = MibScalar
unitDateDay = _UnitDateDay_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 9),
    _UnitDateDay_Type()
)
unitDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitDateDay.setStatus("mandatory")
_UnitTimeHour_Type = TODHour
_UnitTimeHour_Object = MibScalar
unitTimeHour = _UnitTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 10),
    _UnitTimeHour_Type()
)
unitTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTimeHour.setStatus("mandatory")
_UnitTimeMinute_Type = TODMinute
_UnitTimeMinute_Object = MibScalar
unitTimeMinute = _UnitTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 11),
    _UnitTimeMinute_Type()
)
unitTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTimeMinute.setStatus("mandatory")
_UnitTimeSecond_Type = TODSecond
_UnitTimeSecond_Object = MibScalar
unitTimeSecond = _UnitTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 12),
    _UnitTimeSecond_Type()
)
unitTimeSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTimeSecond.setStatus("mandatory")


class _UnitTimezone_Type(Integer32):
    """Custom type unitTimezone based on Integer32"""
    defaultValue = 1

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
              24)
        )
    )
    namedValues = NamedValues(
        *(("astTimezone", 10),
          ("cstTimezone", 7),
          ("estTimezone", 6),
          ("g01Timezone", 2),
          ("g02Timezone", 3),
          ("g03Timezone", 4),
          ("g04Timezone", 5),
          ("g11Timezone", 12),
          ("g12Timezone", 13),
          ("g13Timezone", 14),
          ("g14Timezone", 15),
          ("g15Timezone", 16),
          ("g16Timezone", 17),
          ("g17Timezone", 18),
          ("g18Timezone", 19),
          ("g19Timezone", 20),
          ("g20Timezone", 21),
          ("g21Timezone", 22),
          ("g22Timezone", 23),
          ("g23Timezone", 24),
          ("gmtTimezone", 1),
          ("hstTimezone", 11),
          ("mstTimezone", 8),
          ("pstTimezone", 9))
    )


_UnitTimezone_Type.__name__ = "Integer32"
_UnitTimezone_Object = MibScalar
unitTimezone = _UnitTimezone_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 13),
    _UnitTimezone_Type()
)
unitTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTimezone.setStatus("mandatory")


class _UnitLedStatus_Type(Integer32):
    """Custom type unitLedStatus based on Integer32"""
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
        *(("blink-Amber", 4),
          ("blink-Green", 3),
          ("blink-Red", 7),
          ("green", 2),
          ("off", 1),
          ("red", 6),
          ("solid-Amber", 5))
    )


_UnitLedStatus_Type.__name__ = "Integer32"
_UnitLedStatus_Object = MibScalar
unitLedStatus = _UnitLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 14),
    _UnitLedStatus_Type()
)
unitLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitLedStatus.setStatus("mandatory")


class _UnitTimeStamp_Type(DisplayString):
    """Custom type unitTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_UnitTimeStamp_Type.__name__ = "DisplayString"
_UnitTimeStamp_Object = MibScalar
unitTimeStamp = _UnitTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 15),
    _UnitTimeStamp_Type()
)
unitTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitTimeStamp.setStatus("mandatory")


class _UnitModelType_Type(Integer32):
    """Custom type unitModelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ml-pppNxDs1Enet", 1)
    )


_UnitModelType_Type.__name__ = "Integer32"
_UnitModelType_Object = MibScalar
unitModelType = _UnitModelType_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 16),
    _UnitModelType_Type()
)
unitModelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitModelType.setStatus("mandatory")


class _UnitRouteMode_Type(Integer32):
    """Custom type unitRouteMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastForward", 2),
          ("staticIp", 1))
    )


_UnitRouteMode_Type.__name__ = "Integer32"
_UnitRouteMode_Object = MibScalar
unitRouteMode = _UnitRouteMode_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 1, 17),
    _UnitRouteMode_Type()
)
unitRouteMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitRouteMode.setStatus("mandatory")
_UnitTelnetConfig_ObjectIdentity = ObjectIdentity
unitTelnetConfig = _UnitTelnetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 2)
)


class _UnitTelnetIdleTimeout_Type(Integer32):
    """Custom type unitTelnetIdleTimeout based on Integer32"""
    defaultValue = 0


_UnitTelnetIdleTimeout_Object = MibScalar
unitTelnetIdleTimeout = _UnitTelnetIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 2, 1),
    _UnitTelnetIdleTimeout_Type()
)
unitTelnetIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTelnetIdleTimeout.setStatus("mandatory")
_UnitDteEnetCfg_ObjectIdentity = ObjectIdentity
unitDteEnetCfg = _UnitDteEnetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 3)
)
_DteEnetTable_Object = MibTable
dteEnetTable = _DteEnetTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dteEnetTable.setStatus("mandatory")
_DteEnetEntry_Object = MibTableRow
dteEnetEntry = _DteEnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 3, 1, 1)
)
dteEnetEntry.setIndexNames(
    (0, "DL5400-MIB", "dteEnetIndex"),
)
if mibBuilder.loadTexts:
    dteEnetEntry.setStatus("mandatory")


class _DteEnetIndex_Type(Integer32):
    """Custom type dteEnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dte1", 1)
    )


_DteEnetIndex_Type.__name__ = "Integer32"
_DteEnetIndex_Object = MibTableColumn
dteEnetIndex = _DteEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 3, 1, 1, 1),
    _DteEnetIndex_Type()
)
dteEnetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dteEnetIndex.setStatus("mandatory")
_DteEnetIpAddress_Type = IpAddress
_DteEnetIpAddress_Object = MibTableColumn
dteEnetIpAddress = _DteEnetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 3, 1, 1, 2),
    _DteEnetIpAddress_Type()
)
dteEnetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dteEnetIpAddress.setStatus("mandatory")
_DteEnetSubnetMask_Type = IpAddress
_DteEnetSubnetMask_Object = MibTableColumn
dteEnetSubnetMask = _DteEnetSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 3, 1, 1, 3),
    _DteEnetSubnetMask_Type()
)
dteEnetSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dteEnetSubnetMask.setStatus("mandatory")


class _DteEnetMacAddress_Type(OctetString):
    """Custom type dteEnetMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_DteEnetMacAddress_Type.__name__ = "OctetString"
_DteEnetMacAddress_Object = MibTableColumn
dteEnetMacAddress = _DteEnetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 3, 1, 1, 4),
    _DteEnetMacAddress_Type()
)
dteEnetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dteEnetMacAddress.setStatus("mandatory")


class _DteEnetProtocol_Type(Integer32):
    """Custom type dteEnetProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee8023", 2))
    )


_DteEnetProtocol_Type.__name__ = "Integer32"
_DteEnetProtocol_Object = MibTableColumn
dteEnetProtocol = _DteEnetProtocol_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 3, 1, 1, 5),
    _DteEnetProtocol_Type()
)
dteEnetProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dteEnetProtocol.setStatus("mandatory")


class _DteEnetOper_Type(Integer32):
    """Custom type dteEnetOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autodetect", 1),
          ("hundredMb", 3),
          ("tenMb", 2))
    )


_DteEnetOper_Type.__name__ = "Integer32"
_DteEnetOper_Object = MibTableColumn
dteEnetOper = _DteEnetOper_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 3, 1, 1, 6),
    _DteEnetOper_Type()
)
dteEnetOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dteEnetOper.setStatus("mandatory")


class _DteEnetMode_Type(Integer32):
    """Custom type dteEnetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autodetect", 1),
          ("fullduplex", 3),
          ("halfduplex", 2))
    )


_DteEnetMode_Type.__name__ = "Integer32"
_DteEnetMode_Object = MibTableColumn
dteEnetMode = _DteEnetMode_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 3, 1, 1, 7),
    _DteEnetMode_Type()
)
dteEnetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dteEnetMode.setStatus("mandatory")
_DteEnetOperStatus_Type = DisplayString
_DteEnetOperStatus_Object = MibTableColumn
dteEnetOperStatus = _DteEnetOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 3, 1, 1, 8),
    _DteEnetOperStatus_Type()
)
dteEnetOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dteEnetOperStatus.setStatus("mandatory")
_DteEnetModeStatus_Type = DisplayString
_DteEnetModeStatus_Object = MibTableColumn
dteEnetModeStatus = _DteEnetModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 3, 1, 1, 9),
    _DteEnetModeStatus_Type()
)
dteEnetModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dteEnetModeStatus.setStatus("mandatory")
_Comm1SerialConfig_ObjectIdentity = ObjectIdentity
comm1SerialConfig = _Comm1SerialConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 5)
)


class _Comm1SerialPortState_Type(Integer32):
    """Custom type comm1SerialPortState based on Integer32"""
    defaultValue = 2

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


_Comm1SerialPortState_Type.__name__ = "Integer32"
_Comm1SerialPortState_Object = MibScalar
comm1SerialPortState = _Comm1SerialPortState_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 5, 1),
    _Comm1SerialPortState_Type()
)
comm1SerialPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm1SerialPortState.setStatus("mandatory")
_Comm1SerialBaudRate_Type = DL5400commBaudRate
_Comm1SerialBaudRate_Object = MibScalar
comm1SerialBaudRate = _Comm1SerialBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 5, 2),
    _Comm1SerialBaudRate_Type()
)
comm1SerialBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm1SerialBaudRate.setStatus("mandatory")
_Comm1SerialBitsPerWord_Type = DL5400commNumDataBits
_Comm1SerialBitsPerWord_Object = MibScalar
comm1SerialBitsPerWord = _Comm1SerialBitsPerWord_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 5, 3),
    _Comm1SerialBitsPerWord_Type()
)
comm1SerialBitsPerWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm1SerialBitsPerWord.setStatus("mandatory")
_Comm1SerialStopBits_Type = DL5400commStopBits
_Comm1SerialStopBits_Object = MibScalar
comm1SerialStopBits = _Comm1SerialStopBits_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 5, 4),
    _Comm1SerialStopBits_Type()
)
comm1SerialStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm1SerialStopBits.setStatus("mandatory")
_Comm1SerialParity_Type = DL5400commParity
_Comm1SerialParity_Object = MibScalar
comm1SerialParity = _Comm1SerialParity_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 5, 5),
    _Comm1SerialParity_Type()
)
comm1SerialParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm1SerialParity.setStatus("mandatory")
_Comm1SerialFlowControl_Type = DL5400commFlowControl
_Comm1SerialFlowControl_Object = MibScalar
comm1SerialFlowControl = _Comm1SerialFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 5, 6),
    _Comm1SerialFlowControl_Type()
)
comm1SerialFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm1SerialFlowControl.setStatus("mandatory")


class _Comm1SerialLogoutOnLos_Type(Integer32):
    """Custom type comm1SerialLogoutOnLos based on Integer32"""
    defaultValue = 2

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


_Comm1SerialLogoutOnLos_Type.__name__ = "Integer32"
_Comm1SerialLogoutOnLos_Object = MibScalar
comm1SerialLogoutOnLos = _Comm1SerialLogoutOnLos_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 5, 7),
    _Comm1SerialLogoutOnLos_Type()
)
comm1SerialLogoutOnLos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm1SerialLogoutOnLos.setStatus("mandatory")


class _Comm1SerialIdleTimeout_Type(Integer32):
    """Custom type comm1SerialIdleTimeout based on Integer32"""
    defaultValue = 0


_Comm1SerialIdleTimeout_Object = MibScalar
comm1SerialIdleTimeout = _Comm1SerialIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 5, 8),
    _Comm1SerialIdleTimeout_Type()
)
comm1SerialIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm1SerialIdleTimeout.setStatus("mandatory")
_Comm2SerialConfig_ObjectIdentity = ObjectIdentity
comm2SerialConfig = _Comm2SerialConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 6)
)


class _Comm2SerialPortState_Type(Integer32):
    """Custom type comm2SerialPortState based on Integer32"""
    defaultValue = 2

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


_Comm2SerialPortState_Type.__name__ = "Integer32"
_Comm2SerialPortState_Object = MibScalar
comm2SerialPortState = _Comm2SerialPortState_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 6, 1),
    _Comm2SerialPortState_Type()
)
comm2SerialPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm2SerialPortState.setStatus("mandatory")
_Comm2SerialBaudRate_Type = DL5400commBaudRate
_Comm2SerialBaudRate_Object = MibScalar
comm2SerialBaudRate = _Comm2SerialBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 6, 2),
    _Comm2SerialBaudRate_Type()
)
comm2SerialBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm2SerialBaudRate.setStatus("mandatory")
_Comm2SerialBitsPerWord_Type = DL5400commNumDataBits
_Comm2SerialBitsPerWord_Object = MibScalar
comm2SerialBitsPerWord = _Comm2SerialBitsPerWord_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 6, 3),
    _Comm2SerialBitsPerWord_Type()
)
comm2SerialBitsPerWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm2SerialBitsPerWord.setStatus("mandatory")
_Comm2SerialStopBits_Type = DL5400commStopBits
_Comm2SerialStopBits_Object = MibScalar
comm2SerialStopBits = _Comm2SerialStopBits_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 6, 4),
    _Comm2SerialStopBits_Type()
)
comm2SerialStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm2SerialStopBits.setStatus("mandatory")
_Comm2SerialParity_Type = DL5400commParity
_Comm2SerialParity_Object = MibScalar
comm2SerialParity = _Comm2SerialParity_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 6, 5),
    _Comm2SerialParity_Type()
)
comm2SerialParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm2SerialParity.setStatus("mandatory")
_Comm2SerialFlowControl_Type = DL5400commFlowControl
_Comm2SerialFlowControl_Object = MibScalar
comm2SerialFlowControl = _Comm2SerialFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 6, 6),
    _Comm2SerialFlowControl_Type()
)
comm2SerialFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm2SerialFlowControl.setStatus("mandatory")


class _Comm2SerialLogoutOnLos_Type(Integer32):
    """Custom type comm2SerialLogoutOnLos based on Integer32"""
    defaultValue = 2

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


_Comm2SerialLogoutOnLos_Type.__name__ = "Integer32"
_Comm2SerialLogoutOnLos_Object = MibScalar
comm2SerialLogoutOnLos = _Comm2SerialLogoutOnLos_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 6, 7),
    _Comm2SerialLogoutOnLos_Type()
)
comm2SerialLogoutOnLos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm2SerialLogoutOnLos.setStatus("mandatory")


class _Comm2SerialIdleTimeout_Type(Integer32):
    """Custom type comm2SerialIdleTimeout based on Integer32"""
    defaultValue = 0


_Comm2SerialIdleTimeout_Object = MibScalar
comm2SerialIdleTimeout = _Comm2SerialIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 6, 8),
    _Comm2SerialIdleTimeout_Type()
)
comm2SerialIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm2SerialIdleTimeout.setStatus("mandatory")


class _Comm2InMDmode_Type(Integer32):
    """Custom type comm2InMDmode based on Integer32"""
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


_Comm2InMDmode_Type.__name__ = "Integer32"
_Comm2InMDmode_Object = MibScalar
comm2InMDmode = _Comm2InMDmode_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 6, 9),
    _Comm2InMDmode_Type()
)
comm2InMDmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm2InMDmode.setStatus("mandatory")


class _Comm2InMDId_Type(DisplayString):
    """Custom type comm2InMDId based on DisplayString"""
    defaultValue = OctetString("0")


_Comm2InMDId_Object = MibScalar
comm2InMDId = _Comm2InMDId_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 6, 10),
    _Comm2InMDId_Type()
)
comm2InMDId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comm2InMDId.setStatus("mandatory")
_NetConfig_ObjectIdentity = ObjectIdentity
netConfig = _NetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7)
)
_NetPriTxClk_Type = DL5400TxClkSrc
_NetPriTxClk_Object = MibScalar
netPriTxClk = _NetPriTxClk_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 1),
    _NetPriTxClk_Type()
)
netPriTxClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netPriTxClk.setStatus("mandatory")
_NetPriLoopPort_Type = Integer32
_NetPriLoopPort_Object = MibScalar
netPriLoopPort = _NetPriLoopPort_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 2),
    _NetPriLoopPort_Type()
)
netPriLoopPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netPriLoopPort.setStatus("mandatory")
_NetSecTxClk_Type = DL5400TxClkSrc
_NetSecTxClk_Object = MibScalar
netSecTxClk = _NetSecTxClk_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 3),
    _NetSecTxClk_Type()
)
netSecTxClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSecTxClk.setStatus("mandatory")
_NetSecLoopPort_Type = Integer32
_NetSecLoopPort_Object = MibScalar
netSecLoopPort = _NetSecLoopPort_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 4),
    _NetSecLoopPort_Type()
)
netSecLoopPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSecLoopPort.setStatus("mandatory")


class _NetExtClkFrequency_Type(Integer32):
    """Custom type netExtClkFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freq1544kHZ", 2),
          ("freq8kHZ", 1))
    )


_NetExtClkFrequency_Type.__name__ = "Integer32"
_NetExtClkFrequency_Object = MibScalar
netExtClkFrequency = _NetExtClkFrequency_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 5),
    _NetExtClkFrequency_Type()
)
netExtClkFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netExtClkFrequency.setStatus("mandatory")
_NetPriStatus_Type = DisplayString
_NetPriStatus_Object = MibScalar
netPriStatus = _NetPriStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 6),
    _NetPriStatus_Type()
)
netPriStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPriStatus.setStatus("mandatory")
_NetSecStatus_Type = DisplayString
_NetSecStatus_Object = MibScalar
netSecStatus = _NetSecStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 7),
    _NetSecStatus_Type()
)
netSecStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netSecStatus.setStatus("mandatory")
_NetActiveStatus_Type = DisplayString
_NetActiveStatus_Object = MibScalar
netActiveStatus = _NetActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 8),
    _NetActiveStatus_Type()
)
netActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netActiveStatus.setStatus("mandatory")


class _NetSuppressYeldet_Type(Integer32):
    """Custom type netSuppressYeldet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowYelDet", 2),
          ("suppressYelDet", 1))
    )


_NetSuppressYeldet_Type.__name__ = "Integer32"
_NetSuppressYeldet_Object = MibScalar
netSuppressYeldet = _NetSuppressYeldet_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 9),
    _NetSuppressYeldet_Type()
)
netSuppressYeldet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSuppressYeldet.setStatus("mandatory")


class _NetLineType_Type(Integer32):
    """Custom type netLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_NetLineType_Type.__name__ = "Integer32"
_NetLineType_Object = MibScalar
netLineType = _NetLineType_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 10),
    _NetLineType_Type()
)
netLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLineType.setStatus("mandatory")
_NetPortTable_Object = MibTable
netPortTable = _NetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 11)
)
if mibBuilder.loadTexts:
    netPortTable.setStatus("mandatory")
_NetPortEntry_Object = MibTableRow
netPortEntry = _NetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 11, 1)
)
netPortEntry.setIndexNames(
    (0, "DL5400-MIB", "netPortIndex"),
)
if mibBuilder.loadTexts:
    netPortEntry.setStatus("mandatory")


class _NetPortIndex_Type(Integer32):
    """Custom type netPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NetPortIndex_Type.__name__ = "Integer32"
_NetPortIndex_Object = MibTableColumn
netPortIndex = _NetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 11, 1, 1),
    _NetPortIndex_Type()
)
netPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPortIndex.setStatus("mandatory")


class _NetAdmin_Type(Integer32):
    """Custom type netAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oos", 2),
          ("oos-mt", 3))
    )


_NetAdmin_Type.__name__ = "Integer32"
_NetAdmin_Object = MibTableColumn
netAdmin = _NetAdmin_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 11, 1, 2),
    _NetAdmin_Type()
)
netAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netAdmin.setStatus("mandatory")


class _NetFramingFormat_Type(Integer32):
    """Custom type netFramingFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("d4", 3),
          ("esf", 2))
    )


_NetFramingFormat_Type.__name__ = "Integer32"
_NetFramingFormat_Object = MibTableColumn
netFramingFormat = _NetFramingFormat_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 11, 1, 3),
    _NetFramingFormat_Type()
)
netFramingFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netFramingFormat.setStatus("mandatory")


class _NetLineCode_Type(Integer32):
    """Custom type netLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ami", 5),
          ("b8zs", 2))
    )


_NetLineCode_Type.__name__ = "Integer32"
_NetLineCode_Object = MibTableColumn
netLineCode = _NetLineCode_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 11, 1, 4),
    _NetLineCode_Type()
)
netLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLineCode.setStatus("mandatory")


class _NetLBO_Type(Integer32):
    """Custom type netLBO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ft0To133", 3),
          ("ft133To266", 4),
          ("ft266To399", 5),
          ("ft399To533", 6),
          ("ft533To655", 7),
          ("lbo-0dB", 8),
          ("lbo-15dB", 10),
          ("lbo-22p5dB", 11),
          ("lbo-7p5dB", 9))
    )


_NetLBO_Type.__name__ = "Integer32"
_NetLBO_Object = MibTableColumn
netLBO = _NetLBO_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 11, 1, 5),
    _NetLBO_Type()
)
netLBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLBO.setStatus("mandatory")


class _NetEGL_Type(Integer32):
    """Custom type netEGL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egl-30dB", 2),
          ("egl-36dB", 1))
    )


_NetEGL_Type.__name__ = "Integer32"
_NetEGL_Object = MibTableColumn
netEGL = _NetEGL_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 11, 1, 6),
    _NetEGL_Type()
)
netEGL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netEGL.setStatus("mandatory")


class _NetFDL_Type(Integer32):
    """Custom type netFDL based on Integer32"""
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
        *(("ansi", 2),
          ("att", 3),
          ("both", 4),
          ("none", 1))
    )


_NetFDL_Type.__name__ = "Integer32"
_NetFDL_Object = MibTableColumn
netFDL = _NetFDL_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 11, 1, 7),
    _NetFDL_Type()
)
netFDL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netFDL.setStatus("mandatory")


class _NetSetCode_Type(Integer32):
    """Custom type netSetCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NetSetCode_Type.__name__ = "Integer32"
_NetSetCode_Object = MibTableColumn
netSetCode = _NetSetCode_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 11, 1, 8),
    _NetSetCode_Type()
)
netSetCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSetCode.setStatus("mandatory")


class _NetClock_Type(Integer32):
    """Custom type netClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopTiming", 1),
          ("sysTiming", 3))
    )


_NetClock_Type.__name__ = "Integer32"
_NetClock_Object = MibTableColumn
netClock = _NetClock_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 11, 1, 9),
    _NetClock_Type()
)
netClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netClock.setStatus("mandatory")
_NetFrameStatus_Type = DisplayString
_NetFrameStatus_Object = MibTableColumn
netFrameStatus = _NetFrameStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 11, 1, 10),
    _NetFrameStatus_Type()
)
netFrameStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netFrameStatus.setStatus("mandatory")
_NetFrameUpTime_Type = TimeTicks
_NetFrameUpTime_Object = MibTableColumn
netFrameUpTime = _NetFrameUpTime_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 7, 11, 1, 11),
    _NetFrameUpTime_Type()
)
netFrameUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netFrameUpTime.setStatus("mandatory")
_UnitSnmpConfig_ObjectIdentity = ObjectIdentity
unitSnmpConfig = _UnitSnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 8)
)
_UnitSnmpTrapAddrTable_Object = MibTable
unitSnmpTrapAddrTable = _UnitSnmpTrapAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 8, 1)
)
if mibBuilder.loadTexts:
    unitSnmpTrapAddrTable.setStatus("mandatory")
_UnitSnmpTrapAddrEntry_Object = MibTableRow
unitSnmpTrapAddrEntry = _UnitSnmpTrapAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 8, 1, 1)
)
unitSnmpTrapAddrEntry.setIndexNames(
    (0, "DL5400-MIB", "unitSnmpTrapHostAddr"),
)
if mibBuilder.loadTexts:
    unitSnmpTrapAddrEntry.setStatus("mandatory")
_UnitSnmpTrapHostAddr_Type = IpAddress
_UnitSnmpTrapHostAddr_Object = MibTableColumn
unitSnmpTrapHostAddr = _UnitSnmpTrapHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 8, 1, 1, 1),
    _UnitSnmpTrapHostAddr_Type()
)
unitSnmpTrapHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSnmpTrapHostAddr.setStatus("mandatory")


class _UnitSnmpTrapDirection_Type(Integer32):
    """Custom type unitSnmpTrapDirection based on Integer32"""
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
          ("inBand", 2),
          ("outBand", 3))
    )


_UnitSnmpTrapDirection_Type.__name__ = "Integer32"
_UnitSnmpTrapDirection_Object = MibTableColumn
unitSnmpTrapDirection = _UnitSnmpTrapDirection_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 8, 1, 1, 2),
    _UnitSnmpTrapDirection_Type()
)
unitSnmpTrapDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSnmpTrapDirection.setStatus("mandatory")


class _UnitSnmpTrapDevState_Type(Integer32):
    """Custom type unitSnmpTrapDevState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("forward", 1))
    )


_UnitSnmpTrapDevState_Type.__name__ = "Integer32"
_UnitSnmpTrapDevState_Object = MibScalar
unitSnmpTrapDevState = _UnitSnmpTrapDevState_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 8, 2),
    _UnitSnmpTrapDevState_Type()
)
unitSnmpTrapDevState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSnmpTrapDevState.setStatus("mandatory")
_UnitSnmpTrapCommunity_Type = DisplayString
_UnitSnmpTrapCommunity_Object = MibScalar
unitSnmpTrapCommunity = _UnitSnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 8, 3),
    _UnitSnmpTrapCommunity_Type()
)
unitSnmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSnmpTrapCommunity.setStatus("mandatory")
_UnitPPPConfig_ObjectIdentity = ObjectIdentity
unitPPPConfig = _UnitPPPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9)
)
_PppPortTable_Object = MibTable
pppPortTable = _PppPortTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 1)
)
if mibBuilder.loadTexts:
    pppPortTable.setStatus("mandatory")
_PppPortEntry_Object = MibTableRow
pppPortEntry = _PppPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 1, 1)
)
pppPortEntry.setIndexNames(
    (0, "DL5400-MIB", "pppPortIndex"),
)
if mibBuilder.loadTexts:
    pppPortEntry.setStatus("mandatory")


class _PppPortIndex_Type(Integer32):
    """Custom type pppPortIndex based on Integer32"""
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
        *(("net1", 1),
          ("net2", 2),
          ("net3", 3),
          ("net4", 4),
          ("net5", 5),
          ("net6", 6),
          ("net7", 7),
          ("net8", 8))
    )


_PppPortIndex_Type.__name__ = "Integer32"
_PppPortIndex_Object = MibTableColumn
pppPortIndex = _PppPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 1, 1, 1),
    _PppPortIndex_Type()
)
pppPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppPortIndex.setStatus("mandatory")
_PppPortInitialMRU_Type = Integer32
_PppPortInitialMRU_Object = MibTableColumn
pppPortInitialMRU = _PppPortInitialMRU_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 1, 1, 2),
    _PppPortInitialMRU_Type()
)
pppPortInitialMRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppPortInitialMRU.setStatus("mandatory")


class _PppPortMagicNumber_Type(Integer32):
    """Custom type pppPortMagicNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_PppPortMagicNumber_Type.__name__ = "Integer32"
_PppPortMagicNumber_Object = MibTableColumn
pppPortMagicNumber = _PppPortMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 1, 1, 3),
    _PppPortMagicNumber_Type()
)
pppPortMagicNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppPortMagicNumber.setStatus("mandatory")


class _PppPortFcsSize_Type(Integer32):
    """Custom type pppPortFcsSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("size16bits", 1),
          ("size32bits", 2))
    )


_PppPortFcsSize_Type.__name__ = "Integer32"
_PppPortFcsSize_Object = MibTableColumn
pppPortFcsSize = _PppPortFcsSize_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 1, 1, 4),
    _PppPortFcsSize_Type()
)
pppPortFcsSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppPortFcsSize.setStatus("mandatory")


class _PppPortRestore_Type(Integer32):
    """Custom type pppPortRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_PppPortRestore_Type.__name__ = "Integer32"
_PppPortRestore_Object = MibTableColumn
pppPortRestore = _PppPortRestore_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 1, 1, 5),
    _PppPortRestore_Type()
)
pppPortRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppPortRestore.setStatus("mandatory")
_UnitMLPPPConfig_ObjectIdentity = ObjectIdentity
unitMLPPPConfig = _UnitMLPPPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 2)
)
_MlPPPIpAddress_Type = IpAddress
_MlPPPIpAddress_Object = MibScalar
mlPPPIpAddress = _MlPPPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 2, 1),
    _MlPPPIpAddress_Type()
)
mlPPPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlPPPIpAddress.setStatus("mandatory")
_MlPPPSubnetMask_Type = IpAddress
_MlPPPSubnetMask_Object = MibScalar
mlPPPSubnetMask = _MlPPPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 2, 2),
    _MlPPPSubnetMask_Type()
)
mlPPPSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlPPPSubnetMask.setStatus("mandatory")


class _MlPPPNumberedInterface_Type(Integer32):
    """Custom type mlPPPNumberedInterface based on Integer32"""
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


_MlPPPNumberedInterface_Type.__name__ = "Integer32"
_MlPPPNumberedInterface_Object = MibScalar
mlPPPNumberedInterface = _MlPPPNumberedInterface_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 2, 3),
    _MlPPPNumberedInterface_Type()
)
mlPPPNumberedInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlPPPNumberedInterface.setStatus("mandatory")
_MlPPPMRRU_Type = Integer32
_MlPPPMRRU_Object = MibScalar
mlPPPMRRU = _MlPPPMRRU_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 2, 4),
    _MlPPPMRRU_Type()
)
mlPPPMRRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlPPPMRRU.setStatus("mandatory")
_MlPPPBundleStatus_Type = DisplayString
_MlPPPBundleStatus_Object = MibScalar
mlPPPBundleStatus = _MlPPPBundleStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 2, 5),
    _MlPPPBundleStatus_Type()
)
mlPPPBundleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlPPPBundleStatus.setStatus("mandatory")
_MlPPPBundleUpTime_Type = TimeTicks
_MlPPPBundleUpTime_Object = MibScalar
mlPPPBundleUpTime = _MlPPPBundleUpTime_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 2, 6),
    _MlPPPBundleUpTime_Type()
)
mlPPPBundleUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlPPPBundleUpTime.setStatus("mandatory")
_MlPPPIPCPState_Type = DisplayString
_MlPPPIPCPState_Object = MibScalar
mlPPPIPCPState = _MlPPPIPCPState_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 2, 7),
    _MlPPPIPCPState_Type()
)
mlPPPIPCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlPPPIPCPState.setStatus("mandatory")
_MlPPPPortTable_Object = MibTable
mlPPPPortTable = _MlPPPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 3)
)
if mibBuilder.loadTexts:
    mlPPPPortTable.setStatus("mandatory")
_MlPPPPortEntry_Object = MibTableRow
mlPPPPortEntry = _MlPPPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 3, 1)
)
mlPPPPortEntry.setIndexNames(
    (0, "DL5400-MIB", "mlPPPPortIndex"),
)
if mibBuilder.loadTexts:
    mlPPPPortEntry.setStatus("mandatory")


class _MlPPPPortIndex_Type(Integer32):
    """Custom type mlPPPPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MlPPPPortIndex_Type.__name__ = "Integer32"
_MlPPPPortIndex_Object = MibTableColumn
mlPPPPortIndex = _MlPPPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 3, 1, 1),
    _MlPPPPortIndex_Type()
)
mlPPPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlPPPPortIndex.setStatus("mandatory")


class _MlPPPAdmin_Type(Integer32):
    """Custom type mlPPPAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oos", 2),
          ("oos-mt", 3))
    )


_MlPPPAdmin_Type.__name__ = "Integer32"
_MlPPPAdmin_Object = MibTableColumn
mlPPPAdmin = _MlPPPAdmin_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 3, 1, 2),
    _MlPPPAdmin_Type()
)
mlPPPAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlPPPAdmin.setStatus("mandatory")
_MlPPPStatus_Type = DisplayString
_MlPPPStatus_Object = MibTableColumn
mlPPPStatus = _MlPPPStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 3, 1, 3),
    _MlPPPStatus_Type()
)
mlPPPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlPPPStatus.setStatus("mandatory")
_MlPPPUpTime_Type = TimeTicks
_MlPPPUpTime_Object = MibTableColumn
mlPPPUpTime = _MlPPPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 3, 1, 4),
    _MlPPPUpTime_Type()
)
mlPPPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlPPPUpTime.setStatus("mandatory")
_MlPPPLCPState_Type = DisplayString
_MlPPPLCPState_Object = MibTableColumn
mlPPPLCPState = _MlPPPLCPState_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 9, 3, 1, 5),
    _MlPPPLCPState_Type()
)
mlPPPLCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlPPPLCPState.setStatus("mandatory")
_UnitRouterConfig_ObjectIdentity = ObjectIdentity
unitRouterConfig = _UnitRouterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 10)
)
_UnitStaticRoutingTable_Object = MibTable
unitStaticRoutingTable = _UnitStaticRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 10, 1)
)
if mibBuilder.loadTexts:
    unitStaticRoutingTable.setStatus("mandatory")
_StaticRoutingEntry_Object = MibTableRow
staticRoutingEntry = _StaticRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 10, 1, 1)
)
staticRoutingEntry.setIndexNames(
    (0, "DL5400-MIB", "routeDestination"),
)
if mibBuilder.loadTexts:
    staticRoutingEntry.setStatus("mandatory")
_RouteDestination_Type = IpAddress
_RouteDestination_Object = MibTableColumn
routeDestination = _RouteDestination_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 10, 1, 1, 1),
    _RouteDestination_Type()
)
routeDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeDestination.setStatus("mandatory")
_RouteNetworkMask_Type = IpAddress
_RouteNetworkMask_Object = MibTableColumn
routeNetworkMask = _RouteNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 10, 1, 1, 2),
    _RouteNetworkMask_Type()
)
routeNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeNetworkMask.setStatus("mandatory")
_RouteNextHopAddress_Type = IpAddress
_RouteNextHopAddress_Object = MibTableColumn
routeNextHopAddress = _RouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 10, 1, 1, 3),
    _RouteNextHopAddress_Type()
)
routeNextHopAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeNextHopAddress.setStatus("mandatory")
_RouteMetric_Type = Integer32
_RouteMetric_Object = MibTableColumn
routeMetric = _RouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 10, 1, 1, 4),
    _RouteMetric_Type()
)
routeMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeMetric.setStatus("mandatory")


class _RouteDirection_Type(Integer32):
    """Custom type routeDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("num", 2),
          ("wan", 1))
    )


_RouteDirection_Type.__name__ = "Integer32"
_RouteDirection_Object = MibTableColumn
routeDirection = _RouteDirection_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 10, 1, 1, 5),
    _RouteDirection_Type()
)
routeDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeDirection.setStatus("mandatory")
_RouteStatus_Type = DL5400Validation
_RouteStatus_Object = MibTableColumn
routeStatus = _RouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 10, 1, 1, 6),
    _RouteStatus_Type()
)
routeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeStatus.setStatus("mandatory")
_UnitArpConfig_ObjectIdentity = ObjectIdentity
unitArpConfig = _UnitArpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 11)
)


class _UnitClearArpTable_Type(Integer32):
    """Custom type unitClearArpTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_UnitClearArpTable_Type.__name__ = "Integer32"
_UnitClearArpTable_Object = MibScalar
unitClearArpTable = _UnitClearArpTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 11, 1),
    _UnitClearArpTable_Type()
)
unitClearArpTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitClearArpTable.setStatus("mandatory")
_UnitArpTable_Object = MibTable
unitArpTable = _UnitArpTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 11, 2)
)
if mibBuilder.loadTexts:
    unitArpTable.setStatus("mandatory")
_UnitArpEntry_Object = MibTableRow
unitArpEntry = _UnitArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 11, 2, 1)
)
unitArpEntry.setIndexNames(
    (0, "DL5400-MIB", "arpEntryNum"),
)
if mibBuilder.loadTexts:
    unitArpEntry.setStatus("mandatory")
_ArpEntryNum_Type = Integer32
_ArpEntryNum_Object = MibTableColumn
arpEntryNum = _ArpEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 11, 2, 1, 1),
    _ArpEntryNum_Type()
)
arpEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpEntryNum.setStatus("mandatory")
_ArpIPAddress_Type = IpAddress
_ArpIPAddress_Object = MibTableColumn
arpIPAddress = _ArpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 11, 2, 1, 2),
    _ArpIPAddress_Type()
)
arpIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIPAddress.setStatus("mandatory")


class _ArpMACAddress_Type(OctetString):
    """Custom type arpMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_ArpMACAddress_Type.__name__ = "OctetString"
_ArpMACAddress_Object = MibTableColumn
arpMACAddress = _ArpMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 11, 2, 1, 3),
    _ArpMACAddress_Type()
)
arpMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMACAddress.setStatus("mandatory")
_ArpPortNum_Type = Integer32
_ArpPortNum_Object = MibTableColumn
arpPortNum = _ArpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 1, 11, 2, 1, 4),
    _ArpPortNum_Type()
)
arpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpPortNum.setStatus("mandatory")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 2)
)
_UnitAlarmConfig_ObjectIdentity = ObjectIdentity
unitAlarmConfig = _UnitAlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 2, 1)
)
_UnitAlarmStatusTable_Object = MibTable
unitAlarmStatusTable = _UnitAlarmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 2, 1, 1)
)
if mibBuilder.loadTexts:
    unitAlarmStatusTable.setStatus("mandatory")
_UnitAlarmStatusEntry_Object = MibTableRow
unitAlarmStatusEntry = _UnitAlarmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 2, 1, 1, 1)
)
unitAlarmStatusEntry.setIndexNames(
    (0, "DL5400-MIB", "unitAlarmIndex"),
)
if mibBuilder.loadTexts:
    unitAlarmStatusEntry.setStatus("mandatory")
_UnitAlarmIndex_Type = Integer32
_UnitAlarmIndex_Object = MibTableColumn
unitAlarmIndex = _UnitAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 2, 1, 1, 1, 1),
    _UnitAlarmIndex_Type()
)
unitAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitAlarmIndex.setStatus("mandatory")


class _UnitAlarmSeverity_Type(Integer32):
    """Custom type unitAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("major", 3),
          ("minor", 2),
          ("status", 1))
    )


_UnitAlarmSeverity_Type.__name__ = "Integer32"
_UnitAlarmSeverity_Object = MibTableColumn
unitAlarmSeverity = _UnitAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 2, 1, 1, 1, 2),
    _UnitAlarmSeverity_Type()
)
unitAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitAlarmSeverity.setStatus("mandatory")
_UnitAlarmType_Type = DL5400Event
_UnitAlarmType_Object = MibTableColumn
unitAlarmType = _UnitAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 2, 1, 1, 1, 3),
    _UnitAlarmType_Type()
)
unitAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitAlarmType.setStatus("mandatory")
_UnitAlarmOriginCardNum_Type = DL5400CardId
_UnitAlarmOriginCardNum_Object = MibTableColumn
unitAlarmOriginCardNum = _UnitAlarmOriginCardNum_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 2, 1, 1, 1, 4),
    _UnitAlarmOriginCardNum_Type()
)
unitAlarmOriginCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitAlarmOriginCardNum.setStatus("mandatory")
_UnitAlarmOriginPortNum_Type = DL5400PortId
_UnitAlarmOriginPortNum_Object = MibTableColumn
unitAlarmOriginPortNum = _UnitAlarmOriginPortNum_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 2, 1, 1, 1, 5),
    _UnitAlarmOriginPortNum_Type()
)
unitAlarmOriginPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitAlarmOriginPortNum.setStatus("mandatory")
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 3)
)
_UnitEventTable_Object = MibTable
unitEventTable = _UnitEventTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 3, 1)
)
if mibBuilder.loadTexts:
    unitEventTable.setStatus("mandatory")
_UnitEventEntry_Object = MibTableRow
unitEventEntry = _UnitEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 3, 1, 1)
)
unitEventEntry.setIndexNames(
    (0, "DL5400-MIB", "unitEventIndex"),
)
if mibBuilder.loadTexts:
    unitEventEntry.setStatus("mandatory")
_UnitEventIndex_Type = Integer32
_UnitEventIndex_Object = MibTableColumn
unitEventIndex = _UnitEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 3, 1, 1, 1),
    _UnitEventIndex_Type()
)
unitEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitEventIndex.setStatus("mandatory")


class _UnitEventSeverity_Type(Integer32):
    """Custom type unitEventSeverity based on Integer32"""
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
        *(("clear", 4),
          ("information", 5),
          ("major", 3),
          ("minor", 2),
          ("status", 1))
    )


_UnitEventSeverity_Type.__name__ = "Integer32"
_UnitEventSeverity_Object = MibTableColumn
unitEventSeverity = _UnitEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 3, 1, 1, 2),
    _UnitEventSeverity_Type()
)
unitEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitEventSeverity.setStatus("mandatory")
_UnitEventHour_Type = TODHour
_UnitEventHour_Object = MibTableColumn
unitEventHour = _UnitEventHour_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 3, 1, 1, 3),
    _UnitEventHour_Type()
)
unitEventHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitEventHour.setStatus("mandatory")
_UnitEventMinute_Type = TODMinute
_UnitEventMinute_Object = MibTableColumn
unitEventMinute = _UnitEventMinute_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 3, 1, 1, 4),
    _UnitEventMinute_Type()
)
unitEventMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitEventMinute.setStatus("mandatory")
_UnitEventSecond_Type = TODSecond
_UnitEventSecond_Object = MibTableColumn
unitEventSecond = _UnitEventSecond_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 3, 1, 1, 5),
    _UnitEventSecond_Type()
)
unitEventSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitEventSecond.setStatus("mandatory")
_UnitEventMonth_Type = TODMonth
_UnitEventMonth_Object = MibTableColumn
unitEventMonth = _UnitEventMonth_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 3, 1, 1, 6),
    _UnitEventMonth_Type()
)
unitEventMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitEventMonth.setStatus("mandatory")
_UnitEventDay_Type = TODDay
_UnitEventDay_Object = MibTableColumn
unitEventDay = _UnitEventDay_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 3, 1, 1, 7),
    _UnitEventDay_Type()
)
unitEventDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitEventDay.setStatus("mandatory")
_UnitEventYear_Type = TODYear
_UnitEventYear_Object = MibTableColumn
unitEventYear = _UnitEventYear_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 3, 1, 1, 8),
    _UnitEventYear_Type()
)
unitEventYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitEventYear.setStatus("mandatory")
_UnitEventOriginCardNum_Type = DL5400CardId
_UnitEventOriginCardNum_Object = MibTableColumn
unitEventOriginCardNum = _UnitEventOriginCardNum_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 3, 1, 1, 9),
    _UnitEventOriginCardNum_Type()
)
unitEventOriginCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitEventOriginCardNum.setStatus("mandatory")
_UnitEventOriginPortNum_Type = DL5400PortId
_UnitEventOriginPortNum_Object = MibTableColumn
unitEventOriginPortNum = _UnitEventOriginPortNum_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 3, 1, 1, 10),
    _UnitEventOriginPortNum_Type()
)
unitEventOriginPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitEventOriginPortNum.setStatus("mandatory")
_UnitEventType_Type = DL5400Event
_UnitEventType_Object = MibTableColumn
unitEventType = _UnitEventType_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 3, 1, 1, 11),
    _UnitEventType_Type()
)
unitEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitEventType.setStatus("mandatory")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 4)
)
_ArpStats_ObjectIdentity = ObjectIdentity
arpStats = _ArpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1)
)
_ArpbadLengthField_Type = Counter32
_ArpbadLengthField_Object = MibScalar
arpbadLengthField = _ArpbadLengthField_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1, 1),
    _ArpbadLengthField_Type()
)
arpbadLengthField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpbadLengthField.setStatus("mandatory")
_ArpunsupportedHardware_Type = Counter32
_ArpunsupportedHardware_Object = MibScalar
arpunsupportedHardware = _ArpunsupportedHardware_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1, 2),
    _ArpunsupportedHardware_Type()
)
arpunsupportedHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpunsupportedHardware.setStatus("mandatory")
_ArpunsupportedProtocol_Type = Counter32
_ArpunsupportedProtocol_Object = MibScalar
arpunsupportedProtocol = _ArpunsupportedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1, 3),
    _ArpunsupportedProtocol_Type()
)
arpunsupportedProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpunsupportedProtocol.setStatus("mandatory")
_ArpinvalidSenderAddr_Type = Counter32
_ArpinvalidSenderAddr_Object = MibScalar
arpinvalidSenderAddr = _ArpinvalidSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1, 4),
    _ArpinvalidSenderAddr_Type()
)
arpinvalidSenderAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpinvalidSenderAddr.setStatus("mandatory")
_ArpinvalidTargetAddr_Type = Counter32
_ArpinvalidTargetAddr_Object = MibScalar
arpinvalidTargetAddr = _ArpinvalidTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1, 5),
    _ArpinvalidTargetAddr_Type()
)
arpinvalidTargetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpinvalidTargetAddr.setStatus("mandatory")
_ArpbadAddress_Type = Counter32
_ArpbadAddress_Object = MibScalar
arpbadAddress = _ArpbadAddress_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1, 6),
    _ArpbadAddress_Type()
)
arpbadAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpbadAddress.setStatus("mandatory")
_ArppktsReceived_Type = Counter32
_ArppktsReceived_Object = MibScalar
arppktsReceived = _ArppktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1, 7),
    _ArppktsReceived_Type()
)
arppktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arppktsReceived.setStatus("mandatory")
_ArpshortPktsReceived_Type = Counter32
_ArpshortPktsReceived_Object = MibScalar
arpshortPktsReceived = _ArpshortPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1, 8),
    _ArpshortPktsReceived_Type()
)
arpshortPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpshortPktsReceived.setStatus("mandatory")
_ArppktsFromMeReceived_Type = Counter32
_ArppktsFromMeReceived_Object = MibScalar
arppktsFromMeReceived = _ArppktsFromMeReceived_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1, 9),
    _ArppktsFromMeReceived_Type()
)
arppktsFromMeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arppktsFromMeReceived.setStatus("mandatory")
_ArpsrcBcstReceived_Type = Counter32
_ArpsrcBcstReceived_Object = MibScalar
arpsrcBcstReceived = _ArpsrcBcstReceived_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1, 10),
    _ArpsrcBcstReceived_Type()
)
arpsrcBcstReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpsrcBcstReceived.setStatus("mandatory")
_ArprepliedSent_Type = Counter32
_ArprepliedSent_Object = MibScalar
arprepliedSent = _ArprepliedSent_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1, 11),
    _ArprepliedSent_Type()
)
arprepliedSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arprepliedSent.setStatus("mandatory")
_ArpincomingRequests_Type = Counter32
_ArpincomingRequests_Object = MibScalar
arpincomingRequests = _ArpincomingRequests_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1, 12),
    _ArpincomingRequests_Type()
)
arpincomingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpincomingRequests.setStatus("mandatory")
_ArprequestSent_Type = Counter32
_ArprequestSent_Object = MibScalar
arprequestSent = _ArprequestSent_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1, 13),
    _ArprequestSent_Type()
)
arprequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arprequestSent.setStatus("mandatory")
_ArpnoMACAddr_Type = Counter32
_ArpnoMACAddr_Object = MibScalar
arpnoMACAddr = _ArpnoMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 1, 14),
    _ArpnoMACAddr_Type()
)
arpnoMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpnoMACAddr.setStatus("mandatory")
_HdlcStatsTable_Object = MibTable
hdlcStatsTable = _HdlcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 2)
)
if mibBuilder.loadTexts:
    hdlcStatsTable.setStatus("mandatory")
_HdlcStatsEntry_Object = MibTableRow
hdlcStatsEntry = _HdlcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 2, 1)
)
hdlcStatsEntry.setIndexNames(
    (0, "DL5400-MIB", "hdlcPortIndex"),
)
if mibBuilder.loadTexts:
    hdlcStatsEntry.setStatus("mandatory")
_HdlcPortIndex_Type = Integer32
_HdlcPortIndex_Object = MibTableColumn
hdlcPortIndex = _HdlcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 2, 1, 1),
    _HdlcPortIndex_Type()
)
hdlcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcPortIndex.setStatus("mandatory")
_HdlcLinkStatusBadFCSc_Type = Counter32
_HdlcLinkStatusBadFCSc_Object = MibTableColumn
hdlcLinkStatusBadFCSc = _HdlcLinkStatusBadFCSc_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 2, 1, 2),
    _HdlcLinkStatusBadFCSc_Type()
)
hdlcLinkStatusBadFCSc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcLinkStatusBadFCSc.setStatus("mandatory")
_HdlcFramesAborted_Type = Counter32
_HdlcFramesAborted_Object = MibTableColumn
hdlcFramesAborted = _HdlcFramesAborted_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 2, 1, 3),
    _HdlcFramesAborted_Type()
)
hdlcFramesAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcFramesAborted.setStatus("mandatory")
_HdlcFramesNotAligned_Type = Counter32
_HdlcFramesNotAligned_Object = MibTableColumn
hdlcFramesNotAligned = _HdlcFramesNotAligned_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 2, 1, 4),
    _HdlcFramesNotAligned_Type()
)
hdlcFramesNotAligned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcFramesNotAligned.setStatus("mandatory")
_HdlcOctetsRcv_Type = Counter32
_HdlcOctetsRcv_Object = MibTableColumn
hdlcOctetsRcv = _HdlcOctetsRcv_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 2, 1, 5),
    _HdlcOctetsRcv_Type()
)
hdlcOctetsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcOctetsRcv.setStatus("mandatory")
_HdlcPctsRcv_Type = Counter32
_HdlcPctsRcv_Object = MibTableColumn
hdlcPctsRcv = _HdlcPctsRcv_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 2, 1, 6),
    _HdlcPctsRcv_Type()
)
hdlcPctsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcPctsRcv.setStatus("mandatory")
_HdlcOctetsTrsmt_Type = Counter32
_HdlcOctetsTrsmt_Object = MibTableColumn
hdlcOctetsTrsmt = _HdlcOctetsTrsmt_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 2, 1, 7),
    _HdlcOctetsTrsmt_Type()
)
hdlcOctetsTrsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcOctetsTrsmt.setStatus("mandatory")
_HdlcPctsTrsmt_Type = Counter32
_HdlcPctsTrsmt_Object = MibTableColumn
hdlcPctsTrsmt = _HdlcPctsTrsmt_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 2, 1, 8),
    _HdlcPctsTrsmt_Type()
)
hdlcPctsTrsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcPctsTrsmt.setStatus("mandatory")
_MiscStats_ObjectIdentity = ObjectIdentity
miscStats = _MiscStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 3)
)
_MiscprotocolPctsDumped_Type = Counter32
_MiscprotocolPctsDumped_Object = MibScalar
miscprotocolPctsDumped = _MiscprotocolPctsDumped_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 3, 1),
    _MiscprotocolPctsDumped_Type()
)
miscprotocolPctsDumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscprotocolPctsDumped.setStatus("mandatory")
_MiscnonroutablePcts_Type = Counter32
_MiscnonroutablePcts_Object = MibScalar
miscnonroutablePcts = _MiscnonroutablePcts_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 3, 2),
    _MiscnonroutablePcts_Type()
)
miscnonroutablePcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscnonroutablePcts.setStatus("mandatory")
_ClrStats_ObjectIdentity = ObjectIdentity
clrStats = _ClrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 4)
)


class _ClearAllStats_Type(Integer32):
    """Custom type clearAllStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_ClearAllStats_Type.__name__ = "Integer32"
_ClearAllStats_Object = MibScalar
clearAllStats = _ClearAllStats_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 4, 1),
    _ClearAllStats_Type()
)
clearAllStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearAllStats.setStatus("mandatory")


class _ClearCur15Min_Type(Integer32):
    """Custom type clearCur15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_ClearCur15Min_Type.__name__ = "Integer32"
_ClearCur15Min_Object = MibScalar
clearCur15Min = _ClearCur15Min_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 4, 2),
    _ClearCur15Min_Type()
)
clearCur15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearCur15Min.setStatus("mandatory")


class _ClearCur24Hr_Type(Integer32):
    """Custom type clearCur24Hr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_ClearCur24Hr_Type.__name__ = "Integer32"
_ClearCur24Hr_Object = MibScalar
clearCur24Hr = _ClearCur24Hr_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 4, 3),
    _ClearCur24Hr_Type()
)
clearCur24Hr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearCur24Hr.setStatus("mandatory")


class _ClearOld15Min_Type(Integer32):
    """Custom type clearOld15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_ClearOld15Min_Type.__name__ = "Integer32"
_ClearOld15Min_Object = MibScalar
clearOld15Min = _ClearOld15Min_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 4, 4),
    _ClearOld15Min_Type()
)
clearOld15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearOld15Min.setStatus("mandatory")


class _ClearOld24Hr_Type(Integer32):
    """Custom type clearOld24Hr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_ClearOld24Hr_Type.__name__ = "Integer32"
_ClearOld24Hr_Object = MibScalar
clearOld24Hr = _ClearOld24Hr_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 4, 4, 5),
    _ClearOld24Hr_Type()
)
clearOld24Hr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearOld24Hr.setStatus("mandatory")
_Maintenance_ObjectIdentity = ObjectIdentity
maintenance = _Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 110, 5)
)
_MaintModTable_Object = MibTable
maintModTable = _MaintModTable_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 5, 1)
)
if mibBuilder.loadTexts:
    maintModTable.setStatus("mandatory")
_MaintModEntry_Object = MibTableRow
maintModEntry = _MaintModEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 5, 1, 1)
)
maintModEntry.setIndexNames(
    (0, "DL5400-MIB", "maintModIndex"),
)
if mibBuilder.loadTexts:
    maintModEntry.setStatus("mandatory")


class _MaintModIndex_Type(Integer32):
    """Custom type maintModIndex based on Integer32"""
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
        *(("ds1", 2),
          ("enet", 3),
          ("mpm", 4),
          ("pp", 1))
    )


_MaintModIndex_Type.__name__ = "Integer32"
_MaintModIndex_Object = MibTableColumn
maintModIndex = _MaintModIndex_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 5, 1, 1, 1),
    _MaintModIndex_Type()
)
maintModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintModIndex.setStatus("mandatory")
_MaintModStatus_Type = DisplayString
_MaintModStatus_Object = MibTableColumn
maintModStatus = _MaintModStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 5, 1, 1, 2),
    _MaintModStatus_Type()
)
maintModStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintModStatus.setStatus("mandatory")
_MaintOperstatus_Type = DisplayString
_MaintOperstatus_Object = MibTableColumn
maintOperstatus = _MaintOperstatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 110, 5, 1, 1, 3),
    _MaintOperstatus_Type()
)
maintOperstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintOperstatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dl5400ModulesAppear = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 1)
)
dl5400ModulesAppear.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ModulesAppear.setStatus(
        ""
    )

dl5400ModulesDisappear = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 2)
)
dl5400ModulesDisappear.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ModulesDisappear.setStatus(
        ""
    )

dl5400SelfTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 11)
)
dl5400SelfTestFail.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400SelfTestFail.setStatus(
        ""
    )

dl5400RamTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 12)
)
dl5400RamTestFail.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400RamTestFail.setStatus(
        ""
    )

dl5400RomChecksumFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 13)
)
dl5400RomChecksumFail.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400RomChecksumFail.setStatus(
        ""
    )

dl5400FlashChecksumFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 14)
)
dl5400FlashChecksumFail.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400FlashChecksumFail.setStatus(
        ""
    )

dl5400TimeNotSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 15)
)
dl5400TimeNotSet.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400TimeNotSet.setStatus(
        ""
    )

dl5400UnitRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 16)
)
dl5400UnitRestart.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400UnitRestart.setStatus(
        ""
    )

dl5400LampTestStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 17)
)
dl5400LampTestStart.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400LampTestStart.setStatus(
        ""
    )

dl5400LampTestEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 18)
)
dl5400LampTestEnd.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400LampTestEnd.setStatus(
        ""
    )

dl5400mgmtPOSTFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 19)
)
dl5400mgmtPOSTFail.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400mgmtPOSTFail.setStatus(
        ""
    )

dl5400mgmtPOSTok = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 20)
)
dl5400mgmtPOSTok.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400mgmtPOSTok.setStatus(
        ""
    )

dl5400FrontTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 21)
)
dl5400FrontTemperatureHigh.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400FrontTemperatureHigh.setStatus(
        ""
    )

dl5400FrontTemperatureOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 22)
)
dl5400FrontTemperatureOK.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400FrontTemperatureOK.setStatus(
        ""
    )

dl5400BackTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 23)
)
dl5400BackTemperatureHigh.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400BackTemperatureHigh.setStatus(
        ""
    )

dl5400BackTemperatureOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 24)
)
dl5400BackTemperatureOK.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400BackTemperatureOK.setStatus(
        ""
    )

dl5400ExternalMajorAlarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 25)
)
dl5400ExternalMajorAlarmStart.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ExternalMajorAlarmStart.setStatus(
        ""
    )

dl5400ExternalMajorAlarmEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 26)
)
dl5400ExternalMajorAlarmEnd.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ExternalMajorAlarmEnd.setStatus(
        ""
    )

dl5400ExternalMinorAlarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 27)
)
dl5400ExternalMinorAlarmStart.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ExternalMinorAlarmStart.setStatus(
        ""
    )

dl5400ExternalMinorAlarmEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 28)
)
dl5400ExternalMinorAlarmEnd.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ExternalMinorAlarmEnd.setStatus(
        ""
    )

dl5400ExternalStatusAlarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 29)
)
dl5400ExternalStatusAlarmStart.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ExternalStatusAlarmStart.setStatus(
        ""
    )

dl5400ExternalStatusAlarmEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 30)
)
dl5400ExternalStatusAlarmEnd.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ExternalStatusAlarmEnd.setStatus(
        ""
    )

dl5400PrimaryClockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 31)
)
dl5400PrimaryClockFail.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400PrimaryClockFail.setStatus(
        ""
    )

dl5400PrimaryClockOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 32)
)
dl5400PrimaryClockOk.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400PrimaryClockOk.setStatus(
        ""
    )

dl5400SecondaryClockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 33)
)
dl5400SecondaryClockFail.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400SecondaryClockFail.setStatus(
        ""
    )

dl5400SecondaryClockOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 34)
)
dl5400SecondaryClockOk.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400SecondaryClockOk.setStatus(
        ""
    )

dl5400ExternalClockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 35)
)
dl5400ExternalClockFail.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ExternalClockFail.setStatus(
        ""
    )

dl5400ExternalClockOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 36)
)
dl5400ExternalClockOk.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ExternalClockOk.setStatus(
        ""
    )

dl5400Fan1FailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 37)
)
dl5400Fan1FailAlarm.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400Fan1FailAlarm.setStatus(
        ""
    )

dl5400Fan1Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 38)
)
dl5400Fan1Ok.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400Fan1Ok.setStatus(
        ""
    )

dl5400Fan2FailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 39)
)
dl5400Fan2FailAlarm.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400Fan2FailAlarm.setStatus(
        ""
    )

dl5400Fan2Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 40)
)
dl5400Fan2Ok.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400Fan2Ok.setStatus(
        ""
    )

dl5400PSFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 41)
)
dl5400PSFanFailed.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400PSFanFailed.setStatus(
        ""
    )

dl5400PSFanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 42)
)
dl5400PSFanOK.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400PSFanOK.setStatus(
        ""
    )

dl5400PktProcessorPostFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 43)
)
dl5400PktProcessorPostFail.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400PktProcessorPostFail.setStatus(
        ""
    )

dl5400PktProcessorPostOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 44)
)
dl5400PktProcessorPostOk.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400PktProcessorPostOk.setStatus(
        ""
    )

dl5400PacketProcessorMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 45)
)
dl5400PacketProcessorMissing.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400PacketProcessorMissing.setStatus(
        ""
    )

dl5400PacketProcessorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 46)
)
dl5400PacketProcessorOk.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400PacketProcessorOk.setStatus(
        ""
    )

dl5400VoltageExceeds = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 47)
)
dl5400VoltageExceeds.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400VoltageExceeds.setStatus(
        ""
    )

dl5400VoltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 48)
)
dl5400VoltageOk.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400VoltageOk.setStatus(
        ""
    )

dl5400ModuleProcessorFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 49)
)
dl5400ModuleProcessorFail.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ModuleProcessorFail.setStatus(
        ""
    )

dl5400ModuleProcessorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 50)
)
dl5400ModuleProcessorOk.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ModuleProcessorOk.setStatus(
        ""
    )

dl5400ModulesCfgMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 51)
)
dl5400ModulesCfgMismatch.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ModulesCfgMismatch.setStatus(
        ""
    )

dl5400ModulesCfgMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 52)
)
dl5400ModulesCfgMatch.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ModulesCfgMatch.setStatus(
        ""
    )

dl5400UsePriClkAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 53)
)
dl5400UsePriClkAlarm.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400UsePriClkAlarm.setStatus(
        ""
    )

dl5400UseSecClkAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 54)
)
dl5400UseSecClkAlarm.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400UseSecClkAlarm.setStatus(
        ""
    )

dl5400UseIntClkAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 55)
)
dl5400UseIntClkAlarm.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400UseIntClkAlarm.setStatus(
        ""
    )

dl5400UseRxClk1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 56)
)
dl5400UseRxClk1Alarm.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400UseRxClk1Alarm.setStatus(
        ""
    )

dl5400UseRxClk2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 57)
)
dl5400UseRxClk2Alarm.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400UseRxClk2Alarm.setStatus(
        ""
    )

dl5400UseRxClk3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 58)
)
dl5400UseRxClk3Alarm.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400UseRxClk3Alarm.setStatus(
        ""
    )

dl5400UseRxClk4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 59)
)
dl5400UseRxClk4Alarm.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400UseRxClk4Alarm.setStatus(
        ""
    )

dl5400UseRxClk5Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 60)
)
dl5400UseRxClk5Alarm.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400UseRxClk5Alarm.setStatus(
        ""
    )

dl5400UseRxClk6Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 61)
)
dl5400UseRxClk6Alarm.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400UseRxClk6Alarm.setStatus(
        ""
    )

dl5400UseRxClk7Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 62)
)
dl5400UseRxClk7Alarm.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400UseRxClk7Alarm.setStatus(
        ""
    )

dl5400UseRxClk8Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 63)
)
dl5400UseRxClk8Alarm.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400UseRxClk8Alarm.setStatus(
        ""
    )

dl5400MLpppPOSTFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 64)
)
dl5400MLpppPOSTFail.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400MLpppPOSTFail.setStatus(
        ""
    )

dl5400MLpppPOSTok = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 65)
)
dl5400MLpppPOSTok.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400MLpppPOSTok.setStatus(
        ""
    )

dl5400MLpppModuleMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 66)
)
dl5400MLpppModuleMissing.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400MLpppModuleMissing.setStatus(
        ""
    )

dl5400MLpppModuleOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 67)
)
dl5400MLpppModuleOK.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400MLpppModuleOK.setStatus(
        ""
    )

dl5400MLpppInsufficientLinks = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 68)
)
dl5400MLpppInsufficientLinks.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400MLpppInsufficientLinks.setStatus(
        ""
    )

dl5400MLpppInsufficientLinksOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 69)
)
dl5400MLpppInsufficientLinksOk.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400MLpppInsufficientLinksOk.setStatus(
        ""
    )

dl5400ModulesFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 70)
)
dl5400ModulesFail.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ModulesFail.setStatus(
        ""
    )

dl5400ModulesUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 71)
)
dl5400ModulesUp.setObjects(
      *(("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400ModulesUp.setStatus(
        ""
    )

dl5400LossOfSignalStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 100)
)
dl5400LossOfSignalStart.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400LossOfSignalStart.setStatus(
        ""
    )

dl5400LossOfSignalEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 101)
)
dl5400LossOfSignalEnd.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400LossOfSignalEnd.setStatus(
        ""
    )

dl5400LossOfFrameStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 102)
)
dl5400LossOfFrameStart.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400LossOfFrameStart.setStatus(
        ""
    )

dl5400LossOfFrameEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 103)
)
dl5400LossOfFrameEnd.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400LossOfFrameEnd.setStatus(
        ""
    )

dl5400AisStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 104)
)
dl5400AisStart.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400AisStart.setStatus(
        ""
    )

dl5400AisEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 105)
)
dl5400AisEnd.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400AisEnd.setStatus(
        ""
    )

dl5400RaiStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 106)
)
dl5400RaiStart.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400RaiStart.setStatus(
        ""
    )

dl5400RaiEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 107)
)
dl5400RaiEnd.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400RaiEnd.setStatus(
        ""
    )

dl5400netLineRemoteLoopbackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 158)
)
dl5400netLineRemoteLoopbackStart.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400netLineRemoteLoopbackStart.setStatus(
        ""
    )

dl5400netLineRemoteLoopbackEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 159)
)
dl5400netLineRemoteLoopbackEnd.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400netLineRemoteLoopbackEnd.setStatus(
        ""
    )

dl5400pppEchoTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 164)
)
dl5400pppEchoTimeout.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400pppEchoTimeout.setStatus(
        ""
    )

dl5400pppEchoTimeoutRemit = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 165)
)
dl5400pppEchoTimeoutRemit.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400pppEchoTimeoutRemit.setStatus(
        ""
    )

dl5400pppLineLoopbackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 166)
)
dl5400pppLineLoopbackStart.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400pppLineLoopbackStart.setStatus(
        ""
    )

dl5400pppLineLoopbackEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 167)
)
dl5400pppLineLoopbackEnd.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400pppLineLoopbackEnd.setStatus(
        ""
    )

dl5400pppLinkFallbackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 168)
)
dl5400pppLinkFallbackStart.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400pppLinkFallbackStart.setStatus(
        ""
    )

dl5400pppLinkFallbackEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 169)
)
dl5400pppLinkFallbackEnd.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400pppLinkFallbackEnd.setStatus(
        ""
    )

dl5400dteLocalLoopbackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 170)
)
dl5400dteLocalLoopbackStart.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400dteLocalLoopbackStart.setStatus(
        ""
    )

dl5400dteLocalLoopbackEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 171)
)
dl5400dteLocalLoopbackEnd.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400dteLocalLoopbackEnd.setStatus(
        ""
    )

dl5400dteRemoteLoopbackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 172)
)
dl5400dteRemoteLoopbackStart.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400dteRemoteLoopbackStart.setStatus(
        ""
    )

dl5400dteRemoteLoopbackEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 173)
)
dl5400dteRemoteLoopbackEnd.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400dteRemoteLoopbackEnd.setStatus(
        ""
    )

dl5400MLpppLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 174)
)
dl5400MLpppLinkDown.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400MLpppLinkDown.setStatus(
        ""
    )

dl5400MLpppLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 110, 0, 175)
)
dl5400MLpppLinkUp.setObjects(
      *(("DL5400-MIB", "unitEventOriginPortNum"),
        ("DL5400-MIB", "unitEventSeverity"),
        ("DL5400-MIB", "unitTimeStamp"))
)
if mibBuilder.loadTexts:
    dl5400MLpppLinkUp.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DL5400-MIB",
    **{"DisplayString": DisplayString,
       "DL5400Validation": DL5400Validation,
       "DL5400commBaudRate": DL5400commBaudRate,
       "DL5400commParity": DL5400commParity,
       "DL5400commStopBits": DL5400commStopBits,
       "DL5400commNumDataBits": DL5400commNumDataBits,
       "DL5400commFlowControl": DL5400commFlowControl,
       "TODYear": TODYear,
       "TODMonth": TODMonth,
       "TODDay": TODDay,
       "TODHour": TODHour,
       "TODMinute": TODMinute,
       "TODSecond": TODSecond,
       "DL5400CardId": DL5400CardId,
       "DL5400PortId": DL5400PortId,
       "DL5400TxClkSrc": DL5400TxClkSrc,
       "DL5400Event": DL5400Event,
       "digital-link": digital_link,
       "dl5400": dl5400,
       "dl5400ModulesAppear": dl5400ModulesAppear,
       "dl5400ModulesDisappear": dl5400ModulesDisappear,
       "dl5400SelfTestFail": dl5400SelfTestFail,
       "dl5400RamTestFail": dl5400RamTestFail,
       "dl5400RomChecksumFail": dl5400RomChecksumFail,
       "dl5400FlashChecksumFail": dl5400FlashChecksumFail,
       "dl5400TimeNotSet": dl5400TimeNotSet,
       "dl5400UnitRestart": dl5400UnitRestart,
       "dl5400LampTestStart": dl5400LampTestStart,
       "dl5400LampTestEnd": dl5400LampTestEnd,
       "dl5400mgmtPOSTFail": dl5400mgmtPOSTFail,
       "dl5400mgmtPOSTok": dl5400mgmtPOSTok,
       "dl5400FrontTemperatureHigh": dl5400FrontTemperatureHigh,
       "dl5400FrontTemperatureOK": dl5400FrontTemperatureOK,
       "dl5400BackTemperatureHigh": dl5400BackTemperatureHigh,
       "dl5400BackTemperatureOK": dl5400BackTemperatureOK,
       "dl5400ExternalMajorAlarmStart": dl5400ExternalMajorAlarmStart,
       "dl5400ExternalMajorAlarmEnd": dl5400ExternalMajorAlarmEnd,
       "dl5400ExternalMinorAlarmStart": dl5400ExternalMinorAlarmStart,
       "dl5400ExternalMinorAlarmEnd": dl5400ExternalMinorAlarmEnd,
       "dl5400ExternalStatusAlarmStart": dl5400ExternalStatusAlarmStart,
       "dl5400ExternalStatusAlarmEnd": dl5400ExternalStatusAlarmEnd,
       "dl5400PrimaryClockFail": dl5400PrimaryClockFail,
       "dl5400PrimaryClockOk": dl5400PrimaryClockOk,
       "dl5400SecondaryClockFail": dl5400SecondaryClockFail,
       "dl5400SecondaryClockOk": dl5400SecondaryClockOk,
       "dl5400ExternalClockFail": dl5400ExternalClockFail,
       "dl5400ExternalClockOk": dl5400ExternalClockOk,
       "dl5400Fan1FailAlarm": dl5400Fan1FailAlarm,
       "dl5400Fan1Ok": dl5400Fan1Ok,
       "dl5400Fan2FailAlarm": dl5400Fan2FailAlarm,
       "dl5400Fan2Ok": dl5400Fan2Ok,
       "dl5400PSFanFailed": dl5400PSFanFailed,
       "dl5400PSFanOK": dl5400PSFanOK,
       "dl5400PktProcessorPostFail": dl5400PktProcessorPostFail,
       "dl5400PktProcessorPostOk": dl5400PktProcessorPostOk,
       "dl5400PacketProcessorMissing": dl5400PacketProcessorMissing,
       "dl5400PacketProcessorOk": dl5400PacketProcessorOk,
       "dl5400VoltageExceeds": dl5400VoltageExceeds,
       "dl5400VoltageOk": dl5400VoltageOk,
       "dl5400ModuleProcessorFail": dl5400ModuleProcessorFail,
       "dl5400ModuleProcessorOk": dl5400ModuleProcessorOk,
       "dl5400ModulesCfgMismatch": dl5400ModulesCfgMismatch,
       "dl5400ModulesCfgMatch": dl5400ModulesCfgMatch,
       "dl5400UsePriClkAlarm": dl5400UsePriClkAlarm,
       "dl5400UseSecClkAlarm": dl5400UseSecClkAlarm,
       "dl5400UseIntClkAlarm": dl5400UseIntClkAlarm,
       "dl5400UseRxClk1Alarm": dl5400UseRxClk1Alarm,
       "dl5400UseRxClk2Alarm": dl5400UseRxClk2Alarm,
       "dl5400UseRxClk3Alarm": dl5400UseRxClk3Alarm,
       "dl5400UseRxClk4Alarm": dl5400UseRxClk4Alarm,
       "dl5400UseRxClk5Alarm": dl5400UseRxClk5Alarm,
       "dl5400UseRxClk6Alarm": dl5400UseRxClk6Alarm,
       "dl5400UseRxClk7Alarm": dl5400UseRxClk7Alarm,
       "dl5400UseRxClk8Alarm": dl5400UseRxClk8Alarm,
       "dl5400MLpppPOSTFail": dl5400MLpppPOSTFail,
       "dl5400MLpppPOSTok": dl5400MLpppPOSTok,
       "dl5400MLpppModuleMissing": dl5400MLpppModuleMissing,
       "dl5400MLpppModuleOK": dl5400MLpppModuleOK,
       "dl5400MLpppInsufficientLinks": dl5400MLpppInsufficientLinks,
       "dl5400MLpppInsufficientLinksOk": dl5400MLpppInsufficientLinksOk,
       "dl5400ModulesFail": dl5400ModulesFail,
       "dl5400ModulesUp": dl5400ModulesUp,
       "dl5400LossOfSignalStart": dl5400LossOfSignalStart,
       "dl5400LossOfSignalEnd": dl5400LossOfSignalEnd,
       "dl5400LossOfFrameStart": dl5400LossOfFrameStart,
       "dl5400LossOfFrameEnd": dl5400LossOfFrameEnd,
       "dl5400AisStart": dl5400AisStart,
       "dl5400AisEnd": dl5400AisEnd,
       "dl5400RaiStart": dl5400RaiStart,
       "dl5400RaiEnd": dl5400RaiEnd,
       "dl5400netLineRemoteLoopbackStart": dl5400netLineRemoteLoopbackStart,
       "dl5400netLineRemoteLoopbackEnd": dl5400netLineRemoteLoopbackEnd,
       "dl5400pppEchoTimeout": dl5400pppEchoTimeout,
       "dl5400pppEchoTimeoutRemit": dl5400pppEchoTimeoutRemit,
       "dl5400pppLineLoopbackStart": dl5400pppLineLoopbackStart,
       "dl5400pppLineLoopbackEnd": dl5400pppLineLoopbackEnd,
       "dl5400pppLinkFallbackStart": dl5400pppLinkFallbackStart,
       "dl5400pppLinkFallbackEnd": dl5400pppLinkFallbackEnd,
       "dl5400dteLocalLoopbackStart": dl5400dteLocalLoopbackStart,
       "dl5400dteLocalLoopbackEnd": dl5400dteLocalLoopbackEnd,
       "dl5400dteRemoteLoopbackStart": dl5400dteRemoteLoopbackStart,
       "dl5400dteRemoteLoopbackEnd": dl5400dteRemoteLoopbackEnd,
       "dl5400MLpppLinkDown": dl5400MLpppLinkDown,
       "dl5400MLpppLinkUp": dl5400MLpppLinkUp,
       "configuration": configuration,
       "unitLevelConfig": unitLevelConfig,
       "unitSerialNum": unitSerialNum,
       "unitName": unitName,
       "unitHwRev": unitHwRev,
       "unitSwRev": unitSwRev,
       "unitMibRev": unitMibRev,
       "unitFrontPnl": unitFrontPnl,
       "unitDateYear": unitDateYear,
       "unitDateMonth": unitDateMonth,
       "unitDateDay": unitDateDay,
       "unitTimeHour": unitTimeHour,
       "unitTimeMinute": unitTimeMinute,
       "unitTimeSecond": unitTimeSecond,
       "unitTimezone": unitTimezone,
       "unitLedStatus": unitLedStatus,
       "unitTimeStamp": unitTimeStamp,
       "unitModelType": unitModelType,
       "unitRouteMode": unitRouteMode,
       "unitTelnetConfig": unitTelnetConfig,
       "unitTelnetIdleTimeout": unitTelnetIdleTimeout,
       "unitDteEnetCfg": unitDteEnetCfg,
       "dteEnetTable": dteEnetTable,
       "dteEnetEntry": dteEnetEntry,
       "dteEnetIndex": dteEnetIndex,
       "dteEnetIpAddress": dteEnetIpAddress,
       "dteEnetSubnetMask": dteEnetSubnetMask,
       "dteEnetMacAddress": dteEnetMacAddress,
       "dteEnetProtocol": dteEnetProtocol,
       "dteEnetOper": dteEnetOper,
       "dteEnetMode": dteEnetMode,
       "dteEnetOperStatus": dteEnetOperStatus,
       "dteEnetModeStatus": dteEnetModeStatus,
       "comm1SerialConfig": comm1SerialConfig,
       "comm1SerialPortState": comm1SerialPortState,
       "comm1SerialBaudRate": comm1SerialBaudRate,
       "comm1SerialBitsPerWord": comm1SerialBitsPerWord,
       "comm1SerialStopBits": comm1SerialStopBits,
       "comm1SerialParity": comm1SerialParity,
       "comm1SerialFlowControl": comm1SerialFlowControl,
       "comm1SerialLogoutOnLos": comm1SerialLogoutOnLos,
       "comm1SerialIdleTimeout": comm1SerialIdleTimeout,
       "comm2SerialConfig": comm2SerialConfig,
       "comm2SerialPortState": comm2SerialPortState,
       "comm2SerialBaudRate": comm2SerialBaudRate,
       "comm2SerialBitsPerWord": comm2SerialBitsPerWord,
       "comm2SerialStopBits": comm2SerialStopBits,
       "comm2SerialParity": comm2SerialParity,
       "comm2SerialFlowControl": comm2SerialFlowControl,
       "comm2SerialLogoutOnLos": comm2SerialLogoutOnLos,
       "comm2SerialIdleTimeout": comm2SerialIdleTimeout,
       "comm2InMDmode": comm2InMDmode,
       "comm2InMDId": comm2InMDId,
       "netConfig": netConfig,
       "netPriTxClk": netPriTxClk,
       "netPriLoopPort": netPriLoopPort,
       "netSecTxClk": netSecTxClk,
       "netSecLoopPort": netSecLoopPort,
       "netExtClkFrequency": netExtClkFrequency,
       "netPriStatus": netPriStatus,
       "netSecStatus": netSecStatus,
       "netActiveStatus": netActiveStatus,
       "netSuppressYeldet": netSuppressYeldet,
       "netLineType": netLineType,
       "netPortTable": netPortTable,
       "netPortEntry": netPortEntry,
       "netPortIndex": netPortIndex,
       "netAdmin": netAdmin,
       "netFramingFormat": netFramingFormat,
       "netLineCode": netLineCode,
       "netLBO": netLBO,
       "netEGL": netEGL,
       "netFDL": netFDL,
       "netSetCode": netSetCode,
       "netClock": netClock,
       "netFrameStatus": netFrameStatus,
       "netFrameUpTime": netFrameUpTime,
       "unitSnmpConfig": unitSnmpConfig,
       "unitSnmpTrapAddrTable": unitSnmpTrapAddrTable,
       "unitSnmpTrapAddrEntry": unitSnmpTrapAddrEntry,
       "unitSnmpTrapHostAddr": unitSnmpTrapHostAddr,
       "unitSnmpTrapDirection": unitSnmpTrapDirection,
       "unitSnmpTrapDevState": unitSnmpTrapDevState,
       "unitSnmpTrapCommunity": unitSnmpTrapCommunity,
       "unitPPPConfig": unitPPPConfig,
       "pppPortTable": pppPortTable,
       "pppPortEntry": pppPortEntry,
       "pppPortIndex": pppPortIndex,
       "pppPortInitialMRU": pppPortInitialMRU,
       "pppPortMagicNumber": pppPortMagicNumber,
       "pppPortFcsSize": pppPortFcsSize,
       "pppPortRestore": pppPortRestore,
       "unitMLPPPConfig": unitMLPPPConfig,
       "mlPPPIpAddress": mlPPPIpAddress,
       "mlPPPSubnetMask": mlPPPSubnetMask,
       "mlPPPNumberedInterface": mlPPPNumberedInterface,
       "mlPPPMRRU": mlPPPMRRU,
       "mlPPPBundleStatus": mlPPPBundleStatus,
       "mlPPPBundleUpTime": mlPPPBundleUpTime,
       "mlPPPIPCPState": mlPPPIPCPState,
       "mlPPPPortTable": mlPPPPortTable,
       "mlPPPPortEntry": mlPPPPortEntry,
       "mlPPPPortIndex": mlPPPPortIndex,
       "mlPPPAdmin": mlPPPAdmin,
       "mlPPPStatus": mlPPPStatus,
       "mlPPPUpTime": mlPPPUpTime,
       "mlPPPLCPState": mlPPPLCPState,
       "unitRouterConfig": unitRouterConfig,
       "unitStaticRoutingTable": unitStaticRoutingTable,
       "staticRoutingEntry": staticRoutingEntry,
       "routeDestination": routeDestination,
       "routeNetworkMask": routeNetworkMask,
       "routeNextHopAddress": routeNextHopAddress,
       "routeMetric": routeMetric,
       "routeDirection": routeDirection,
       "routeStatus": routeStatus,
       "unitArpConfig": unitArpConfig,
       "unitClearArpTable": unitClearArpTable,
       "unitArpTable": unitArpTable,
       "unitArpEntry": unitArpEntry,
       "arpEntryNum": arpEntryNum,
       "arpIPAddress": arpIPAddress,
       "arpMACAddress": arpMACAddress,
       "arpPortNum": arpPortNum,
       "alarms": alarms,
       "unitAlarmConfig": unitAlarmConfig,
       "unitAlarmStatusTable": unitAlarmStatusTable,
       "unitAlarmStatusEntry": unitAlarmStatusEntry,
       "unitAlarmIndex": unitAlarmIndex,
       "unitAlarmSeverity": unitAlarmSeverity,
       "unitAlarmType": unitAlarmType,
       "unitAlarmOriginCardNum": unitAlarmOriginCardNum,
       "unitAlarmOriginPortNum": unitAlarmOriginPortNum,
       "events": events,
       "unitEventTable": unitEventTable,
       "unitEventEntry": unitEventEntry,
       "unitEventIndex": unitEventIndex,
       "unitEventSeverity": unitEventSeverity,
       "unitEventHour": unitEventHour,
       "unitEventMinute": unitEventMinute,
       "unitEventSecond": unitEventSecond,
       "unitEventMonth": unitEventMonth,
       "unitEventDay": unitEventDay,
       "unitEventYear": unitEventYear,
       "unitEventOriginCardNum": unitEventOriginCardNum,
       "unitEventOriginPortNum": unitEventOriginPortNum,
       "unitEventType": unitEventType,
       "statistics": statistics,
       "arpStats": arpStats,
       "arpbadLengthField": arpbadLengthField,
       "arpunsupportedHardware": arpunsupportedHardware,
       "arpunsupportedProtocol": arpunsupportedProtocol,
       "arpinvalidSenderAddr": arpinvalidSenderAddr,
       "arpinvalidTargetAddr": arpinvalidTargetAddr,
       "arpbadAddress": arpbadAddress,
       "arppktsReceived": arppktsReceived,
       "arpshortPktsReceived": arpshortPktsReceived,
       "arppktsFromMeReceived": arppktsFromMeReceived,
       "arpsrcBcstReceived": arpsrcBcstReceived,
       "arprepliedSent": arprepliedSent,
       "arpincomingRequests": arpincomingRequests,
       "arprequestSent": arprequestSent,
       "arpnoMACAddr": arpnoMACAddr,
       "hdlcStatsTable": hdlcStatsTable,
       "hdlcStatsEntry": hdlcStatsEntry,
       "hdlcPortIndex": hdlcPortIndex,
       "hdlcLinkStatusBadFCSc": hdlcLinkStatusBadFCSc,
       "hdlcFramesAborted": hdlcFramesAborted,
       "hdlcFramesNotAligned": hdlcFramesNotAligned,
       "hdlcOctetsRcv": hdlcOctetsRcv,
       "hdlcPctsRcv": hdlcPctsRcv,
       "hdlcOctetsTrsmt": hdlcOctetsTrsmt,
       "hdlcPctsTrsmt": hdlcPctsTrsmt,
       "miscStats": miscStats,
       "miscprotocolPctsDumped": miscprotocolPctsDumped,
       "miscnonroutablePcts": miscnonroutablePcts,
       "clrStats": clrStats,
       "clearAllStats": clearAllStats,
       "clearCur15Min": clearCur15Min,
       "clearCur24Hr": clearCur24Hr,
       "clearOld15Min": clearOld15Min,
       "clearOld24Hr": clearOld24Hr,
       "maintenance": maintenance,
       "maintModTable": maintModTable,
       "maintModEntry": maintModEntry,
       "maintModIndex": maintModIndex,
       "maintModStatus": maintModStatus,
       "maintOperstatus": maintOperstatus}
)
